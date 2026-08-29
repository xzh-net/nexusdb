"""
MCP 数据库分析服务
"""

import argparse
from typing import List, Dict, Any
from mcp.server.mcpserver import MCPServer

from nexusdb.tools.tables import list_tables, describe_table
from nexusdb.db.connection import db_manager

# 创建 MCP 服务器
mcp = MCPServer("Database Analyzer")


@mcp.tool()
def list_tables_tool(database: str) -> List[str]:
    """
    获取数据库所有表
    
    Args:
        database: 数据库标识（A 或 B）
        
    Returns:
        表名列表
    """
    try:
        tables = list_tables(database)
        return tables
    except Exception as e:
        return [f"错误: {str(e)}"]


@mcp.tool()
def describe_table_tool(database: str, table: str) -> List[Dict[str, Any]]:
    """
    查看表结构
    
    Args:
        database: 数据库标识（A 或 B）
        table: 表名
        
    Returns:
        字段信息列表
    """
    try:
        columns = describe_table(database, table)
        return columns
    except Exception as e:
        return [{"error": str(e)}]


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="MCP 数据库分析服务")
    parser.add_argument(
        "--mode",
        choices=["stdio", "sse"],
        default="stdio",
        help="传输模式：stdio（默认）或 sse"
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="SSE 模式监听地址（默认：127.0.0.1）"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="SSE 模式端口号（默认：8000）"
    )
    return parser.parse_args()


def main():
    """主函数"""
    args = parse_args()
    
    print("启动 MCP 数据库分析服务...")
    print("可用工具:")
    print("  - list_tables_tool: 获取数据库所有表")
    print("  - describe_table_tool: 查看表结构")
    
    if args.mode == "sse":
        print(f"\nSSE 服务模式: http://{args.host}:{args.port}")
        print(f"SSE 端点: http://{args.host}:{args.port}/sse")
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        print("\nstdio 模式运行中...")
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
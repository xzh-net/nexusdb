"""
MCP 数据库分析服务
"""

import sys
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


def main():
    """主函数"""
    print("启动 MCP 数据库分析服务...", file=sys.stderr)
    print("可用工具:", file=sys.stderr)
    print("  - list_tables_tool: 获取数据库所有表", file=sys.stderr)
    print("  - describe_table_tool: 查看表结构", file=sys.stderr)
    print("stdio 模式运行中...", file=sys.stderr)
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
"""
表操作工具模块
"""

from typing import List, Dict, Any

from nexusdb.db.connection import db_manager
from nexusdb.config import DATABASES


def list_tables(database: str) -> List[str]:
    """
    获取数据库所有表
    
    Args:
        database: 数据库标识（A 或 B）
        
    Returns:
        表名列表
    """
    conn = db_manager.get_connection(database)
    if not conn:
        raise Exception(f"无法连接到数据库 {database}")
    
    try:
        with conn.cursor() as cursor:
            # 查询所有表
            cursor.execute("SHOW TABLES")
            result = cursor.fetchall()
            
            # 提取表名
            table_name_key = f"Tables_in_{DATABASES[database]['database']}"
            tables = [row[table_name_key] for row in result]
            
            return tables
    except Exception as e:
        raise Exception(f"获取表列表失败: {e}")


def describe_table(database: str, table: str) -> List[Dict[str, Any]]:
    """
    查看表结构
    
    Args:
        database: 数据库标识（A 或 B）
        table: 表名
        
    Returns:
        字段信息列表
    """
    conn = db_manager.get_connection(database)
    if not conn:
        raise Exception(f"无法连接到数据库 {database}")
    
    try:
        with conn.cursor() as cursor:
            # 查询表结构
            cursor.execute(f"DESCRIBE {table}")
            result = cursor.fetchall()
            
            # 格式化结果
            columns = []
            for row in result:
                columns.append({
                    "column": row["Field"],
                    "type": row["Type"],
                    "nullable": row["Null"] == "YES",
                    "key": row["Key"],
                    "default": row["Default"],
                    "extra": row["Extra"]
                })
            
            return columns
    except Exception as e:
        raise Exception(f"获取表结构失败: {e}")
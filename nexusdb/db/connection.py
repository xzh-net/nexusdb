"""
数据库连接管理模块
"""

import pymysql
from typing import Optional

from nexusdb.config import DATABASES


class DatabaseConnection:
    """数据库连接管理类"""
    
    def __init__(self):
        self.connections = {}
    
    def get_connection(self, database_key: str) -> Optional[pymysql.Connection]:
        """
        获取数据库连接
        
        Args:
            database_key: 数据库标识（A 或 B）
            
        Returns:
            pymysql.Connection 或 None
        """
        if database_key not in DATABASES:
            raise ValueError(f"未知的数据库标识: {database_key}")
        
        # 如果连接已存在且未关闭，直接返回
        if database_key in self.connections:
            conn = self.connections[database_key]
            try:
                # 检查连接是否仍然有效
                conn.ping(reconnect=False)
                return conn
            except Exception:
                # 连接已失效，关闭并重新创建
                try:
                    conn.close()
                except Exception:
                    pass
                del self.connections[database_key]
        
        # 创建新连接
        config = DATABASES[database_key]
        try:
            conn = pymysql.connect(
                host=config["host"],
                port=config["port"],
                user=config["user"],
                password=config["password"],
                database=config["database"],
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.connections[database_key] = conn
            return conn
        except Exception as e:
            print(f"连接数据库 {database_key} 失败: {e}")
            return None
    
    def close_connection(self, database_key: str):
        """关闭指定数据库连接"""
        if database_key in self.connections:
            try:
                self.connections[database_key].close()
            except Exception:
                pass
            del self.connections[database_key]
    
    def close_all(self):
        """关闭所有连接"""
        for key in list(self.connections.keys()):
            self.close_connection(key)


# 全局连接管理实例
db_manager = DatabaseConnection()
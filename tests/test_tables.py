"""
表操作工具测试 - pytest格式
"""

import pytest
from nexusdb.tools.tables import list_tables, describe_table


class TestListTables:
    """list_tables 测试类"""
    
    def test_list_tables_returns_list(self):
        """测试返回值类型"""
        result = list_tables("A")
        assert isinstance(result, list)
    
    def test_list_tables_contains_tables(self):
        """测试返回的表列表不为空"""
        result = list_tables("A")
        assert len(result) > 0
    
    def test_list_tables_invalid_database(self):
        """测试无效数据库标识"""
        with pytest.raises(Exception):
            list_tables("INVALID")


class TestDescribeTable:
    """describe_table 测试类"""
    
    def test_describe_table_returns_list(self):
        """测试返回值类型"""
        result = describe_table("A", "hr_bd_land")
        assert isinstance(result, list)
    
    def test_describe_table_contains_columns(self):
        """测试返回的字段列表不为空"""
        result = describe_table("A", "hr_bd_land")
        assert len(result) > 0
    
    def test_describe_table_column_structure(self):
        """测试字段结构"""
        result = describe_table("A", "hr_bd_land")
        for column in result:
            assert "column" in column
            assert "type" in column
            assert "nullable" in column
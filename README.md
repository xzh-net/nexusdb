# NexusDB

MCP数据库分析服务，为AI Agent提供数据库分析能力。

## 项目结构

```
nexusdb/
├── nexusdb/                    # Python包
│   ├── __init__.py
│   ├── __main__.py
│   ├── config.py              # 数据库配置
│   ├── server.py              # MCP服务器
│   ├── db/
│   │   ├── __init__.py
│   │   └── connection.py      # 数据库连接
│   └── tools/
│       ├── __init__.py
│       └── tables.py          # 表操作工具
├── tests/
│   ├── __init__.py
│   └── test_tables.py         # pytest测试
├── .opencode/
│   └── config.json            # MCP配置
├── .gitignore
├── pyproject.toml
└── README.md
```

## 安装

```bash
pip install -e .
```

## 使用

### 启动MCP服务器

```bash
python -m nexusdb.server
```

### 配置OpenCode

`.opencode/config.json` 已自动配置：

```json
{
  "mcpServers": {
    "db-analyzer": {
      "command": "python",
      "args": ["-m", "nexusdb.server"]
    }
  }
}
```

## 测试

### 安装测试依赖

```bash
pip install pytest
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行指定测试文件
pytest tests/test_tables.py

# 详细输出
pytest -v

# 只运行某个类
pytest tests/test_tables.py::TestListTables

# 只运行某个方法
pytest tests/test_tables.py::TestListTables::test_list_tables_returns_list
```


## MCP工具

| 工具 | 说明 |
|------|------|
| `list_tables_tool` | 获取数据库所有表 |
| `describe_table_tool` | 查看表结构 |

## 配置

编辑 `nexusdb/config.py` 修改数据库连接：

```python
DB_A = {
    "host": "192.168.1.161",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "geo"
}
```
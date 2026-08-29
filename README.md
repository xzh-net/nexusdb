# NexusDB

MCP数据库分析服务，为AI Agent提供数据库分析能力。

## 项目结构

```
nexusdb/
├── nexusdb/                   # Python包
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

### 启动模式

支持两种传输模式：

| 模式 | 命令 | 适用场景 |
|------|------|----------|
| stdio | `python -m nexusdb.server` | OpenCode集成（默认） |
| sse | `python -m nexusdb.server --mode sse` | 服务部署、多用户 |

### OpenCode集成（stdio模式）

配置完成后，OpenCode会自动启动MCP服务，无需手动运行。

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

### SSE服务模式

启动服务：

```bash
# 默认配置（127.0.0.1:8000）
python -m nexusdb.server --mode sse

# 自定义地址和端口
python -m nexusdb.server --mode sse --host 0.0.0.0 --port 9000
```

启动后显示：

```
SSE 服务模式: http://127.0.0.1:8000
SSE 端点: http://127.0.0.1:8000/sse
```

### 连接SSE服务

OpenCode配置（`.opencode/config.json`）：

```json
{
  "mcpServers": {
    "db-analyzer": {
      "url": "http://localhost:8000/sse"
    }
  }
}
```

## MCP客户端配置

### OpenCode

在项目根目录创建 `.opencode/config.json`：

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

### Claude Code

在项目根目录创建 `.mcp.json`：

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

### Cursor

在项目根目录创建 `.cursor/mcp.json`：

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

### 通用SSE模式配置

任何支持MCP的客户端都可以连接SSE服务：

```json
{
  "mcpServers": {
    "db-analyzer": {
      "url": "http://localhost:8000/sse"
    }
  }
}
```

## 自然语言调用

配置完成后，在对话中直接使用自然语言：

| 示例 | 说明 |
|------|------|
| "列出数据库A的所有表" | 调用 list_tables_tool |
| "查看hr_bd_land表的结构" | 调用 describe_table_tool |

## 测试

### 安装测试依赖

```bash
pip install pytest
```

### 运行pytest测试

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

### MCP Inspector测试

使用MCP Inspector交互式测试工具：

#### 测试stdio模式

```bash
npx @modelcontextprotocol/inspector python -m nexusdb.server
```

#### 测试SSE模式

**终端1** - 启动SSE服务：

```bash
python -m nexusdb.server --mode sse --port 8000
```

**终端2** - 启动Inspector连接服务：

```bash
npx @modelcontextprotocol/inspector http://localhost:8000/sse
```

打开浏览器访问Inspector界面，可以：
- 查看所有可用工具
- 交互式测试每个工具
- 查看请求/响应详情


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
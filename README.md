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
├── opencode.json            # OpenCode MCP配置
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

本项目仅支持 stdio 模式，用于本地 OpenCode 集成。

```bash
python -m nexusdb.server
```

### OpenCode集成

配置完成后，OpenCode 会自动启动 MCP 服务，无需手动运行。

## MCP客户端配置

### OpenCode

支持两种配置方式：全局配置和项目配置。

#### 全局配置（推荐）

全局配置对所有项目生效。编辑 `~/.config/opencode/opencode.json`：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "db-analyzer": {
      "type": "local",
      "command": ["python", "-m", "nexusdb.server"],
      "enabled": true
    }
  }
}
```

> Windows 路径：`C:\Users\<用户名>\.config\opencode\opencode.json`

#### 项目配置

仅对当前项目生效。在项目根目录创建 `opencode.json`：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "db-analyzer": {
      "type": "local",
      "command": ["python", "-m", "nexusdb.server"],
      "enabled": true
    }
  }
}
```

项目配置会覆盖全局配置中的同名 MCP 服务器。

#### 验证配置

```bash
# 列出所有已配置的 MCP 服务器及连接状态
opencode mcp list
```

输出示例：

```
Name          Type    Status  Command
db-analyzer   local   ready   python -m nexusdb.server
```

其他管理命令：

```bash
# 认证 OAuth 类型的 MCP 服务器
opencode mcp auth <server-name>

# 移除 OAuth 凭据
opencode mcp logout <server-name>

# 调试连接问题
opencode mcp debug <server-name>
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

```bash
npx @modelcontextprotocol/inspector python -m nexusdb.server
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
    "host": "127.0.0.1",
    "port": 3306,
    "user": "your_user",
    "password": "your_password",
    "database": "your_database"
}
```
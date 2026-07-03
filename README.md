# Python CI/CD Test

一个用于学习和测试 Python CI/CD 流程的示例项目，集成了 GitHub Actions 自动化流水线和 pre-commit 本地检查。

## 📁 项目结构

```
python_ci_cd_test/
├── .github/workflows/ci.yml    # GitHub Actions CI/CD 工作流
├── .pre-commit-config.yaml     # Pre-commit 钩子配置
├── src/
│   ├── __init__.py
│   ├── calculator.py           # 计算器模块（加减乘除）
│   └── utils.py                # 工具函数（字符串反转、回文、词数）
├── tests/
│   ├── test_calculator.py      # 计算器测试
│   └── test_utils.py           # 工具函数测试
├── pyproject.toml              # 项目配置 + 依赖管理
├── uv.toml                     # uv 包管理器配置（使用清华镜像）
├── uv.lock                     # 依赖锁定文件
└── pytest.ini                  # Pytest 配置
```

## 🚀 快速开始

### 环境要求

- Python >= 3.11
- [uv](https://docs.astral.sh/uv/)（推荐的 Python 包管理器）

### 安装依赖

```bash
uv sync --all-extras --dev
```

### 运行测试

```bash
uv run pytest -v
```

## 🔧 开发工具

项目集成了以下开发工具，全部通过 pre-commit 自动运行：

| 工具 | 用途 |
|------|------|
| **black** | 代码格式化 |
| **isort** | import 语句排序 |
| **flake8** | 代码静态检查 |
| **mypy** | 类型检查 |
| **pytest** | 单元测试 |

### 激活 pre-commit

```bash
uv run pre-commit install
```

激活后，每次 `git commit` 都会自动运行所有检查工具。

### 手动运行所有检查

```bash
uv run pre-commit run --all-files
```

## 🔄 CI/CD 流水线

每次 push 或 PR 到 `main`/`develop` 分支时，GitHub Actions 会自动执行：

```
Push/PR → 代码检查（flake8、black、isort、mypy）→ 测试（pytest）→ 覆盖率报告
                                                                      ↓
                                                              部署到 GitHub Pages
```

覆盖率报告部署成功后可通过以下地址访问：

```
https://<你的用户名>.github.io/python_ci_cd_test/
```

## 📄 许可证

MIT License

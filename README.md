# 数学证明研究仓库

这是一个由 `uv` 管理的 Python 3.13 数学研究仓库。当前工作围绕“三块十进制拼接 Exact Lift”问题展开，重点是把证明拆成可追踪、可回退、可复核的研究记录。

## 从这里开始

- [AGENTS.md](AGENTS.md)：agent 可用工具、工作边界和证明记录规则。
- [CONTRIBUTING.md](CONTRIBUTING.md)：修改、计算实验和提交规范。
- [docs/proofs/exact-lift/README.md](docs/proofs/exact-lift/README.md)：证明树入口。
- [docs/proofs/exact-lift/status.md](docs/proofs/exact-lift/status.md)：当前严格状态和剩余核心。

主不存在性命题目前尚未完成证明。结构化章节会明确区分已严格完成的局部结果、有限证书、待证路线和失效/降级路线。

## 环境

项目要求 Python 3.13，版本由 [.python-version](.python-version) 指定，依赖由 [pyproject.toml](pyproject.toml) 和 [uv.lock](uv.lock) 管理。

```bash
uv sync --locked
uv run python scripts/proof_tree.py check
uv run python main.py
```

若本机的 uv 缓存目录不可写，可临时指定缓存位置后运行：

```bash
UV_CACHE_DIR=/tmp/math-uv-cache uv sync --locked
UV_CACHE_DIR=/tmp/math-uv-cache uv run python scripts/proof_tree.py check
```

## 仓库结构

```text
.
├── AGENTS.md
├── CONTRIBUTING.md
├── main.py
├── scripts/
├── docs/proofs/exact-lift/
│   ├── problem-and-carrier.md
│   ├── global-framework.md
│   ├── branches/{a2-only,double-deficit,a1-only}.md
│   ├── status.md
│   ├── notation.md
│   ├── dependency-map.md
│   ├── conclusion.md
│   └── archive/                  # 原始总稿快照
├── pyproject.toml
└── uv.lock
```

迁移前的 `exact_lift_research_synthesis_2026-08-10.md` 已原样归档到 `docs/proofs/exact-lift/archive/`；日常编辑请使用 `docs/proofs/exact-lift/` 下的结构化文件。

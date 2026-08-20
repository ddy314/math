# 贡献与证明记录规范

本仓库把 Git 当作证明研究的实验记录。一次提交应尽量只表达一个可复核的主题，例如“拆分 DD 章节”“补充 A2 的有限证书”“修正统一符号”，不要把格式重排、依赖升级和新猜想混在一起。

## 开始工作

```bash
uv sync --locked
git status --short
uv run python scripts/proof_tree.py check
```

## 修改证明

结构化文件位于 `docs/proofs/exact-lift/`。每一条新增结论至少应包含：

- 命题或目标；
- 假设和变量范围；
- 推导或证书；
- 依赖的定义、引理和文件；
- 当前状态及其理由；
- 如果有计算，给出可重跑命令和边界。

先从对应分支 `README.md` 选择现有规范专题或 `*-ledger.md`。主线状态写入规范专题，细粒度 continuation 写入匹配的依赖账本，并把摘要同步回分支 README；不要为同一研究链继续增加平行小文件。确需新文件时，必须同时把它加入分支 README，否则 `proof_tree.py check` 会拒绝不可达文档。

状态只允许使用以下四类：

| 状态 | 含义 |
|---|---|
| `已严格完成` | 推导在写明的假设下闭合，没有依赖未声明的无界步骤。 |
| `有限证书` | 只覆盖显式有限范围，不能外推到全局。 |
| `待证` | 研究方向或尚未闭合的引理。 |
| `失效/降级` | 已知有逻辑缺口、退化或不保持原结构。 |

## 计算实验

优先使用确定性、整数化和可复核的程序。实验记录应写清楚：

- 输入范围与筛选条件；
- 使用的 Python/包版本（由 `uv.lock` 定义）；
- 运行命令；
- 输出和失败条件；
- 它是证明、有限证书，还是仅用于诊断。

计算结果默认放在 `/tmp` 或被 `.gitignore` 排除的目录中。若结果本身是证明所需的证书，应提交生成它的短脚本和足够小的证书，而不是只提交海量输出。稳定证书放在分支脚本顶层；细粒度研究核对放在 `scripts/exact-lift/<branch>/research-checks/<dependency-theme>/`。

## 文档和检查

修改文档后运行：

```bash
uv run python scripts/proof_tree.py check
git diff --check
```

修改 Python 后再运行：

```bash
uv run python -m compileall main.py scripts
uv run python -m pytest
```

当前项目还没有强制测试套件；这不等于数学结论已经验证。没有测试时，应在交付说明中明确写出“结构/语法检查通过”和“数学全局证明仍未完成”的边界。

## 提交前检查

提交前查看完整 diff，确认没有意外改动根目录原始快照、`uv.lock` 或用户已有文件。提交信息建议使用简短动词开头，例如：

```text
docs: split exact-lift proof tree
research: record DD open core
chore: add proof tree validator
```

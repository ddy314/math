# AGENTS.md

## 仓库目标

这是一个以数学证明研究为中心的 Python/`uv` 仓库。当前主线是“三块十进制拼接 Exact Lift”问题：把三个正既约有理数的分子、分母分别按十进制拼接，并研究拼接比值是否能等于三个有理数平方和的平方根。

仓库的首要产物是可审计的证明记录，而不是一个已经完成的不存在性定理。任何 agent 都必须保留以下事实：

- `A_2`-only、double-deficit（DD）和 `A_1`-only 三个分支仍未全部关闭；
- 有限枚举只能证明明确有界的切片，不能替代无界参数的全局证明；
- “已严格完成”“有限证书”“待证”“失效或降级路线”必须分开记录；
- 数学结论必须能追溯到具体文件、章节、假设和验证命令。

## 先读什么

按下面顺序建立上下文：

1. `README.md`：仓库入口、运行方式和当前状态。
2. `docs/proofs/README.md`：证明资料总索引。
3. `docs/proofs/exact-lift/README.md`：Exact Lift 证明树和研究入口。
4. `docs/proofs/exact-lift/status.md`：已完成、未完成和下一步目标。
5. 与当前任务对应的分支入口：`branches/a2-only/README.md`、`branches/double-deficit/README.md` 或 `branches/a1-only/README.md`，再进入其中的规范专题或按依赖归并的研究账本。
6. `docs/proofs/exact-lift/archive/`：只在需要核对迁移前原文时读取，不作为日常编辑入口。

## 目录约定

```text
.
├── AGENTS.md                         # agent 工作规则
├── README.md                         # 项目入口
├── CONTRIBUTING.md                   # 修改、验证和提交规范
├── pyproject.toml                    # uv/Python 项目元数据与依赖
├── uv.lock                           # 锁定依赖，提交后保持同步
├── main.py                           # 轻量入口程序
├── scripts/                          # 稳定证书入口；细粒度核对在分支 research-checks/
├── docs/
│   ├── README.md                     # 文档总索引
│   └── proofs/
│       ├── README.md                 # 证明资料入口
│       └── exact-lift/
│           ├── README.md             # 研究树入口
│           ├── problem-and-carrier.md
│           ├── global-framework.md
│           ├── branches/              # 三个异常分支目录
│           │   ├── a2-only/           # A2 规范专题 + 五本依赖账本
│           │   ├── double-deficit/    # DD 主干/frontier + 三本依赖账本
│           │   └── a1-only/           # A1 规范专题 + 四本依赖账本
│           ├── status.md              # 严格状态和剩余核心
│           ├── notation.md            # 统一符号及旧记号映射
│           ├── dependency-map.md      # 公式依赖图
│           ├── conclusion.md          # 当前研究结论
│           ├── claim-template.md      # 新证明条目模板
│           └── archive/               # 原始总稿等不可变快照
```

结构化证明文件是日常编辑的唯一规范来源；分支 README 和主干专题承载当前结论，`*-ledger.md` 保留细粒度推导与来源锚点。`archive/` 保存迁移前的历史快照，除非明确进行迁移，不要直接修改。

## 可用工具

所有 Python 命令优先通过 `uv` 执行，以使用 `.python-version` 和 `uv.lock` 对应的环境。

### 仓库命令

```bash
uv sync --locked
uv run python scripts/proof_tree.py list
uv run python scripts/proof_tree.py check
uv run python main.py
git diff --check
```

`proof_tree.py check` 检查证明树的必需文件、章节锚点、状态文件中的未完成声明和 Markdown 内部链接。它是结构检查，不是数学证明器。

### 已安装 Python 工具按用途分组

- 符号与精确算术：`sympy`、`symengine`、`gmpy2`、`python-flint`、`mpmath`。
- 数论与有限域：`galois`、`z3-solver`、`pysmt`、`python-sat`。
- 数值与科学计算：`numpy`、`scipy`、`numba`、`scikit-learn`、`statsmodels`。
- 优化与约束：`cvxpy`、`ortools`、`pulp`。
- 数据、图和可视化：`pandas`、`polars`、`networkx`、`matplotlib`、`plotly`。
- 实验与工程辅助：`hypothesis`、`joblib`、`cloudpickle`、`rich`、`tqdm`、`pydantic`。
- Notebook 环境：`jupyterlab`、`ipykernel`、`ipywidgets`。

调用示例：

```bash
uv run python -c "import sympy as sp; print(sp.factorint(1234567890))"
uv run python -m pytest
uv run jupyter lab
```

如果需要新增依赖，使用 `uv add <package>`；不要手工编辑 `uv.lock`。如果只是一次性实验，优先使用已有依赖或在 `/tmp` 保存临时结果，不把生成物写入证明树。

## 证明工作流

每个新证明结果按以下顺序处理：

1. 在对应分支文件中写出明确命题、变量范围和依赖章节。
2. 将状态标为 `已严格完成`、`有限证书`、`待证` 或 `失效/降级` 之一。
3. 给出完整推导，区分必要条件、充分条件、有限计算和猜想。
4. 如使用计算，记录参数边界、程序路径、运行命令、输出摘要和是否覆盖无界参数。
5. 同步更新 `status.md`、`dependency-map.md` 或 `README.md` 中受影响的导航。
6. 运行 `uv run python scripts/proof_tree.py check` 和 `git diff --check`。

禁止把下面几种推理写成全局结论：

- “每个固定前缀只有有限候选”推出“所有前缀的并集有限”；
- 有限枚举没有给出参数上界却推出全局为空；
- 局部同余、数值实验或启发式高度估计直接推出不存在性；
- 高斯翻面改变了尺度就默认它仍保持原十进制 coefficient plane；
- 只因为脚本运行完成，就称某个证明分支已经关闭。

## 修改范围和交付要求

- 保留用户已有的未提交改动；先用 `git status --short` 和 `git diff` 判断范围。
- 数学迁移优先采用“机械拆分 + 人工补导航”的方式，不静默改写公式或降低证明状态。
- 新结果优先写入最具体的现有规范专题或依赖账本，并同步分支 README；只有现有主题确实无法容纳时才新增小写 kebab-case 文件，且必须立即加入分支入口导航。
- 新的细粒度核对脚本放入对应分支 `research-checks/<dependency-theme>/`；分支脚本顶层只保留稳定证书与主入口。
- 不提交 `.venv`、缓存、Notebook checkpoint、临时 PDF 或大规模计算输出。
- 报告时明确说明：改了哪些文件、哪些结论只是整理、运行了哪些验证、哪些数学缺口仍存在。

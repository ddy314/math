# 三块十进制拼接 Exact Lift

给定三个正既约有理数 `ai/bi`，把三个分子按十进制拼成 `alpha`，把三个分母按同样顺序拼成 `beta`。问题是：拼接比值能否等于三个有理数平方和的平方根？

```math
\frac{a_1\,10^{n_2+n_3}+a_2\,10^{n_3}+a_3}
     {b_1\,10^{m_2+m_3}+b_2\,10^{m_3}+b_3}
=\sqrt{\left(\frac{a_1}{b_1}\right)^2+
       \left(\frac{a_2}{b_2}\right)^2+
       \left(\frac{a_3}{b_3}\right)^2}.
```

`ni,mi` 是各块的十进制位数；块无前导零，逐块既约。

**主不存在性命题尚未完成证明。** 正权平均已把候选穷尽分成 A2、DD、A1 三个异常分支，三者仍有无界核心。后两分母都是一位的完整子域已经由高度归约和精确证书排除；这一结果没有关闭整个问题。

## 三个入口

1. [PROOF.md](PROOF.md)：唯一现行证明稿。从原方程、公共引理到三个分支的完整推导；每个命题注明状态、范围、依赖。
2. [RESEARCH.md](RESEARCH.md)：按数学目标组织的路线、剩余系统和撤回原因。研究过程不夹在当前定理之间。
3. [CHECKS.md](CHECKS.md)：统一核对目录。列出证书覆盖、运行入口与计算的作用。

旧日期笔记、重复专题和巨型 ledger 已退出现行目录。全部迁移前原文及脚本保存在 [来源库](history/README.md)，可按路线、原文件或内容检索；历史里的“关闭”不自动成为当前定理。

## 运行

Python 3.13 和依赖由 `uv` 管理。

```bash
uv sync --locked
uv run python main.py
uv run python main.py check
uv run python main.py list claims --branch a1
uv run python main.py verify norm-mod9 a1-kernels
uv run python main.py verify --group quick
```

完整证书按需运行，部分枚举需要 C++17/20 编译器和 Boost 头文件。所有中间可执行文件和日志都写入临时目录。

```bash
uv run python main.py verify a1-e4
uv run python main.py verify dd-eight-tail dd-eight-tail-factored
uv run python main.py list sources --route a2-fixed3
uv run python main.py source search 'LK17G'
```

## 仓库结构

```text
.
├── README.md             # 问题和使用入口
├── PROOF.md              # 唯一现行证明正文
├── RESEARCH.md           # 分离的研究路线与审计
├── CHECKS.md             # 证书覆盖与运行目录
├── AGENTS.md             # 后续研究规则
├── CONTRIBUTING.md       # 编辑和验证规范
├── main.py               # 统一命令入口
├── repository.py         # 状态、来源检索与结构验证
├── registry/
│   ├── claims.json       # 命题、状态、依赖和来源范围
│   └── checks.json       # 核对入口与运行模式
├── checks/
│   ├── common/           # 公共必要条件和完整子域
│   ├── a2/               # A2 符号与局部算术
│   ├── dd/               # DD gap、预算和尾证书
│   └── a1/               # A1 contact、深度和有限末端
├── history/
│   ├── README.md         # 保全规则
│   ├── sources.json      # 原文件和 ledger 记录校验目录
│   └── 2026-10-01-sources.zip
├── tests/                # 命题依赖、来源和命令入口的验证
├── pyproject.toml
└── uv.lock
```

修改正文前读 [贡献规范](CONTRIBUTING.md)。新推导应接入现有命题或路线；不要重新建立按日期追加的平行证明树。

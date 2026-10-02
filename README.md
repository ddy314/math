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

A2 的第一块已限为 13 种。奇尾分母的尾长至多六位，整个奇尾候选集合有限；这个有限性不给有效前缀范围，也没有排除其余有限例外。偶尾的二进、五进及原 source 归约，以及特定第二分母形状的无界子域排除，见 [A2-G01–G15](PROOF.md#a2-g01)。

目前已完整排除下列 A2 子域：

| 原条件 | 覆盖 | 证明与证书 |
|---|---|---|
| `m3=1` 或 `m3=2` | 任意前缀与第二块位数 | [F01](PROOF.md#a2-f01)、[F02](PROOF.md#a2-f02) |
| `m2=2,3,4` | 任意尾长；有效界后穷尽 | [F05](PROOF.md#a2-f05)、[F06](PROOF.md#a2-f06) |
| `m3=3,5∣b2b3` | 奇尾、偶尾及任意前缀 | [F04](PROOF.md#a2-f04)、[F07](PROOF.md#a2-f07) |
| 奇尾 `m3=3,gcd(b2,b3)=1` | 任意前缀与第二块位数 | [F08](PROOF.md#a2-f08) |
| `b2∣b1·10^m2`，包含全部 `b2=10^t` | 六种分母形状；前缀及尾长均无上限，显式指数界后完整排除 | [G12](PROOF.md#a2-g12) |
| `b2=r·10^t,1≤r≤99,10∤r`，且 `(b1,a1,r)≠(1,2,24)` | 一至两位有效数字后接任意多个零；任意尾长 | [G13](PROOF.md#a2-g13)、[G14](PROOF.md#a2-g14) |
| `b2=r·10^t,1≤r≤99,10∤r`，且 `m2≤26` 或 `m3≤38` | 包含 `r=24` 的剩余形状；另一块长度不另设搜索界 | [F09](PROOF.md#a2-f09) |
| 偶尾 `m3=3,4,5,6`；第二分母二进主导，或尾主导且 `v2(b2)≥v2(b1)+m2` | 明示两个有界类，覆盖任意前缀 | [F03](PROOF.md#a2-f03) |

两位有效数字的第二分母只余 G14/F09 的必要族：`b1=1,a1=2,b2=24·10^(2E−1),b3=8·10^(3E−1),E≥13`。[G15](PROOF.md#a2-g15) 还要求 `816·100^E−31` 的每个 `3 mod4` 素因子出现偶数次，并排除四组无限指数余类。`E=13` 通过这个平方和障碍，但其原分子恢复尚未完成；这不是原解存在性结论。

[G10](PROOF.md#a2-g10) 给每个固定原前两块的可计算尾长界，并有统一相对界 `m3≤10m2`；后两分母不含 5 时 `m3≤3m2`。[G09](PROOF.md#a2-g09) 给每个固定尾长的非有效有限性。这两种结果都没有关闭所有前缀、所有尾长的无限并集。

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
uv run python main.py verify a2-first-block
uv run python main.py verify a2-binary-chambers
uv run python main.py verify a2-one-digit-tail a2-one-digit-tail-cpp
uv run python main.py verify a2-two-digit-tail a2-two-digit-tail-cpp
uv run python main.py verify a2-fixed-prefix a2-fixed-prefix-three a2-fixed-prefix-four
uv run python main.py verify a2-short-prefix-even a2-short-prefix-even-six
uv run python main.py verify a2-three-digit-five a2-three-digit-five-cpp
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

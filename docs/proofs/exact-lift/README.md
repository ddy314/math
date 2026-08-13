# 三块十进制拼接 Exact Lift

这是当前仓库的主证明树。原始总稿为 2026-08-10 的研究综述；迁移后的章节文件按数学依赖和研究分支拆开，便于逐文件审阅、回退和比较。

## 入口树

```text
exact-lift/
├── problem-and-carrier.md    # §§1–2：问题、拼接、正权平均和三分支
├── global-framework.md       # §§3–11：整数球面、尾部正规化、统一算术框架
├── branches/
│   ├── a2-only.md             # §§12–16：A2 的终端系统和开放核
│   ├── double-deficit.md      # §§17–27：DD 基线及 2026-08-13 后续进展
│   └── a1-only.md             # §§28–31：A1 saturated 支
├── status.md                  # §§32–39：错误路线、严格状态和下一步
├── notation.md                # §§40–41：符号表和迁移映射
├── dependency-map.md          # §42：关键公式依赖图
├── conclusion.md              # §43：当前研究结论
└── archive/
    └── exact_lift_research_synthesis_2026-08-10.md
```

## 当前状态

主不存在性命题尚未完成证明。当前最明确的剩余工作是：

- `A_2`：关闭 `m_2 >= 11` 的 deep-even source 双 Hensel / Gaussian ellipse 系统；
- `DD`：§27.33 把 `n_3=8S_12-1` 整层关闭，故严格相对界更新为 `n_3<=8S_12-2`，并得到 prefix-uniform 解析锥 `n_3<31S_12/4+6581/960`；
- `DD`：调用经典 Schmidt Subspace Theorem 后得到非有效渐近界 `limsup m_3/S_12<=5` 与 `limsup n_3/S_12<=6.308883577618...`。这不是有效绝对高度界，更不是 DD 全局空性；
- `DD`：假想逼近该 frontier 的序列已被压到 moving pair-max Gaussian core `(C_L,Pi)`；一般结构线仍剩 projective/common-scale allocation 与单侧 moving tail factor的兼容性问题；
- `DD` 的最高层中 `S_12 = 4, n_3 = 31` 已由完整有限证书关闭：`m_3 = 11,...,21` 的统一判别式均非平方，`m_3 = 22,...,26` 的 primitive denominator-tail 核为空。新得到的通用 `F_-` 大除数不依赖 resonance，但尚未导出全局绝对高度界；
- `DD` 的 `S_12=5,n_3=39` 已由后期有限证书全部关闭；
- `A_1`：为 saturated `L = 1` 支的 decimal shift `g` 找到全局界或直接矛盾。

先读 [严格证明状态](status.md)，再进入相应分支。DD 后续工作已并入
[double-deficit.md](branches/double-deficit.md)；不要把非有效渐近界、frontier 条件结论或有限切片写成 DD 全局关闭。

## 如何维护

新增内容应尽量遵循以下顺序：命题 → 假设 → 推导 → 依赖 → 状态 → 验证/开放缺口。若某个结论被否定，不删除历史推导，而是在对应章节标为 `失效/降级` 并说明原因。

原始总稿原样保留在 `archive/`，不再在根目录保留第二个可编辑副本。快照不是新的章节编辑入口。

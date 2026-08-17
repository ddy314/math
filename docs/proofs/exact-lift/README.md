# 三块十进制拼接 Exact Lift

这是当前仓库的主证明树。原始总稿为 2026-08-10 的研究综述；迁移后的章节文件按数学依赖和研究分支拆开，便于逐文件审阅、回退和比较。

## 入口树

```text
exact-lift/
├── problem-and-carrier.md    # §§1–2：问题、拼接、正权平均和三分支
├── global-framework.md       # §§3–11：整数球面、尾部正规化、统一算术框架
├── branches/
│   ├── a2-only.md             # §§12–16：A2 的终端系统和开放核
│   ├── a2-decimal-ellipse-phase.md # A2 ellipse / Gaussian angle 的十进制相位压缩
│   ├── a2-ellipse-to-defect-window.md # ellipse 到 finite-defect remainder 的桥
│   ├── a2-low-defect-angle-squeeze.md # A2 两个低商状态的 angle squeeze
│   ├── a2-endpoint-lattice-progress-2026-08-17.md # endpoint shell、height split、rho^2 slot lattice 与审计 no-go
│   ├── double-deficit.md      # §§17–27：DD 基线及 2026-08-13 后续进展
│   ├── dd-rational-contact-frontier.md # 2026-08-16：DD frontier rational contact / Bad-Good / cofactor 系统
│   ├── dd-frontier-continuation-2026-08-16.md # Bad closure、orientation reconstruction、双 lattice sheet 与最新 no-go
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

- `A_2`：关闭 `m_2 >= 11` 的 deep-even 终端系统；已合并的 ellipse/defect 工作把连续 Gaussian angle 送入 finite-defect remainder；最新 [endpoint lattice continuation](branches/a2-endpoint-lattice-progress-2026-08-17.md) 又把七个 defect 状态全部压入固定余量带，并把最危险 `(a,k)=(9,2)` 压到 `C/D<3/250`、`x<2/19`、`y>249/250`、`zeta<251/250` 的 endpoint core；
- `A_2`：最新 continuation 还得到 high/low-`m` 二分、low-`m` 的线性深 `v_5(N_0)`、基础 square-depth 尺度 `L_0>1000C`，并用 `rho^2` Gaussian factor 的精确 `2`-进赋值与 Archimedean slot 排除整个 reflection 精确中线 `M=2m` 的 high-2 allocation；这仍不是 A2 全局空性；
- `A_2`：本轮同时审计并降级若干看似新的 source/reflection 深 `5`-进 endpoint congruence；它们完整代回 determinant/source split 后属于 decimal-place 重写，后续不得重复计作独立 obstruction；
- `DD`：§27.33 把 `n_3=8S_12-1` 整层关闭，故严格相对界更新为 `n_3<=8S_12-2`，并得到 prefix-uniform 解析锥 `n_3<31S_12/4+6581/960`；
- `DD`：调用经典 Schmidt Subspace Theorem 后得到非有效渐近界 `limsup m_3/S_12<=5` 与 `limsup n_3/S_12<=6.308883577618...`。这不是有效绝对高度界，更不是 DD 全局空性；
- `DD`：假想逼近该 frontier 的序列已被压到 moving pair-max Gaussian core；一般结构线仍剩 projective/common-scale allocation 与单侧 moving tail factor的兼容性问题；
- `DD frontier`：后续的 [rational-contact frontier](branches/dd-rational-contact-frontier.md) 已把 rational-contact 子支进一步压到固定曲面、完整 prime-power sign contact 与 cofactor Lorentz 系统，并证明第一阶 rough height 与 real/5-adic cofactor proximity 都精确达到临界等号；因此普通 first-order GCD / Ridout / fixed-target Subspace 方法不能再重复收费；
- `DD frontier continuation`：最新 [continuation note](branches/dd-frontier-continuation-2026-08-16.md) 在 full rational-contact frontier 上关闭 Bad，建立 Good square-Plücker 正规形，并证明 secondary repeat 与 radius repeat 等价；pair-max Gaussian orientation 可由 derivative gcd 唯一重构，正确的 second-order Newton resultant天然退化；
- `DD frontier continuation`：normalized near-square 的两个因子被精确展开为既有 `Z` 与 `q_c^2 U` source channels，因此完整 `2/5`-adic CRT phase不增加 rank；terminal denominator/source 被进一步包装成两张 exact `2x3` lattice sheet，自然 mixed determinant 在 main `C_L` 上横截；
- `DD frontier continuation`：full rational-contact 的 moving-core entropy可进一步压成 `10^{o(S)}`，但这仍不是 eventual emptiness。下一步应转向 global slot capacity / split-prime digit-shell，而不是继续堆同素数 Gaussian resultant；
- `DD` 的最高层中 `S_12 = 4, n_3 = 31` 已由完整有限证书关闭：`m_3 = 11,...,21` 的统一判别式均非平方，`m_3 = 22,...,26` 的 primitive denominator-tail 核为空。新得到的通用 `F_-` 大除数不依赖 resonance，但尚未导出全局绝对高度界；
- `DD` 的 `S_12=5,n_3=39` 已由后期有限证书全部关闭；
- `A_1`：为 saturated `L = 1` 支的 decimal shift `g` 找到全局界或直接矛盾。

先读 [严格证明状态](status.md)，再进入相应分支。A2 的 terminal 基线见
[a2-only.md](branches/a2-only.md)，最新 endpoint/height/allocation continuation 见
[a2-endpoint-lattice-progress-2026-08-17.md](branches/a2-endpoint-lattice-progress-2026-08-17.md)。DD 全局/历史主线保留在
[double-deficit.md](branches/double-deficit.md)；假想 `6.308883...` frontier 的 rational-contact 基线见
[dd-rational-contact-frontier.md](branches/dd-rational-contact-frontier.md)，其后续 Bad closure、orientation reconstruction、near-square closure audit 与双 lattice sheet 见
[dd-frontier-continuation-2026-08-16.md](branches/dd-frontier-continuation-2026-08-16.md)。不要把非有效渐近界、frontier 条件结论、subexponential counting、有限切片或 A2 的单个 allocation 子族排除写成全局关闭。

## 如何维护

新增内容应尽量遵循以下顺序：命题 → 假设 → 推导 → 依赖 → 状态 → 验证/开放缺口。若某个结论被否定，不删除历史推导，而是在对应章节标为 `失效/降级` 并说明原因。

原始总稿原样保留在 `archive/`，不再在根目录保留第二个可编辑副本。快照不是新的章节编辑入口。

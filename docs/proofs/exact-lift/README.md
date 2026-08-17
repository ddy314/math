# 三块十进制拼接 Exact Lift

这是当前仓库的主证明树。原始总稿为 2026-08-10 的研究综述；迁移后的章节文件按数学依赖和研究分支拆开，便于逐文件审阅、回退和比较。

## 入口树

```text
exact-lift/
├── problem-and-carrier.md    # §§1–2：问题、拼接、正权平均和三分支
├── global-framework.md       # §§3–11：整数球面、尾部正规化、统一算术框架
├── branches/
│   ├── a2-only/               # A2 主干与按依赖合并的四个专题文件
│   ├── double-deficit/        # DD 主干与统一 frontier 文件
│   └── a1-only/               # A1 主干、rational contact、top layer、diagonal
├── status.md                  # §§32–39：错误路线、严格状态和下一步
├── notation.md                # §§40–41：符号表和迁移映射
├── dependency-map.md          # §42：关键公式依赖图
├── conclusion.md              # §43：当前研究结论
└── archive/
    └── exact_lift_research_synthesis_2026-08-10.md
```

## 当前状态

主不存在性命题尚未完成证明。当前最明确的剩余工作是：

- `A_2`：关闭 `m_2 >= 11` 的 deep-even 终端系统；已合并的 ellipse/defect 工作把连续 Gaussian angle 送入 finite-defect remainder；最新 [endpoint lattice continuation](branches/a2-only/endpoint-lattice.md) 又把七个 defect 状态全部压入固定余量带，并把最危险 `(a,k)=(9,2)` 压到 `C/D<3/250`、`x<2/19`、`y>249/250`、`zeta<251/250` 的 endpoint core；
- `A_2`：最新 continuation 还得到 high/low-`m` 二分、low-`m` 的线性深 `v_5(N_0)`、基础 square-depth 尺度 `L_0>1000C`，并用 `rho^2` Gaussian factor 的精确 `2`-进赋值与 Archimedean slot 排除整个 reflection 精确中线 `M=2m` 的 high-2 allocation；这仍不是 A2 全局空性；
- `A_2`：继续令 `eta=2m-M` 后，`eta=-1` 也由统一槽上界严格排除，`eta=1` 先由粗槽压成十五型，再由 exact concatenation、`q_0` prefix barrier 与 Gaussian norm 素数支持压到五个 `(d,c_Q,k_h,slot)` 类型；`k_h=3` 只强迫四坐标共享 `3`，LCM sphere 并非自动整体本原，故该型仍待证。另有 `(1,2,31,1,+)` 的明确粗区间交点，证明“只靠 slot 窄窗统一排除所有 `eta`”不足；
- `A_2`：本轮同时审计并降级若干看似新的 source/reflection 深 `5`-进 endpoint congruence；它们完整代回 determinant/source split 后属于 decimal-place 重写，后续不得重复计作独立 obstruction；
- `A_2`：任意 `eta` 的 quotient-Hensel 核现已提升为同一 Gaussian 商的精确因式分解；唯一中心 `5`-进单位 `r_E` 的提升商 `z_E` 由 denominator 缺口 `H` 模 `g` 唯一确定，并与顶部补余量组成整数核 `(z_E,chi_E)`。完整 `g`-factor 可约，但所得 canonical child 的斜率严格远离 A2 prefix window，故同型下降路线已降级。独立的 `C|F(3)` 现被正规化为正奇 `5`-进单位 `Xi_C`；相邻点还给出互素大除数 `D-C,D+C` 及 `Xi_-,Xi_+`，三个 cofactor 在 `2^m5^d` 上共享同一 `Y`-平方类。尚待证明该 odd-prime reciprocity/resultant 系统与中心核不相容；
- `A_2`：上述三 cofactor 的 secant cubic 已进一步给出严格递增/凹性及精确相邻-gap 核；除以 `2^m5^d` 后两个 gap 之比在 `(1,2)`，各恰含一个 `2`，而其差恰有 `v_2=m+1,v_5=d`。模 `g^2` 的纯 quadratic-character 提升则自动退化为 principal square。下一步必须把 gap 的精确加法与 `D-C,D+C` 的奇除数结构联立；这仍不是 A2 空性；
- `A_2`：gap 的 additive CRT 中 `tilde(T)_2` 还精确含 \(5^d\)；真正的 \(2,5\)-primitive 正整数 `hat(T)_2` 与 \(10c_ug\) 互素且恒为 `3 mod 4`。完整代入 canonical square 后，它仍精确退化成旧 odd inert excess，不能重复计作新 obstruction。新的 gcd laws 已把 denominator excess 压到显式接触；进一步的正 shifted factorization 证明所有未饱和 \(qf\) 接触赋值为偶数，故 odd denominator excess 只剩完整 prime-power 在 \(\mathscr L_{23}=9T/2+a_3\) 中饱和。对真正的 \(q\)-carrier，saturation/resultant 又强迫 \(K^2\equiv26\pmod p\)，排除第一 valuation branch，并把无界结构例外缩成固定素数 \(11,23\)；这两个固定 Hensel lift、generic middle/third、source 与 endpoint-external 通道仍待排除；
- `A_2`：canonical allocation 随后进一步删除 generic middle branch，并在整数层证明 \(q\mid DK-N\)。饱和后的两个 denominator channel 现只读取纯 prefix gcd \(\gcd(q,K^2-26)\) 与 \(\gcd(f,b_2^2(K^2-26)-Q^2N_0)\)；quotient \((DK-N)/q\) 的非 \(3\) inert primes 被锁到真实 sphere height \(H_0\)。这些是严格的全局降维，但两个 prefix gcd、固定 \(11,23\) lift 与 height channel 尚未全部排除；
- `DD`：§27.33 把 `n_3=8S_12-1` 整层关闭，故严格相对界更新为 `n_3<=8S_12-2`，并得到 prefix-uniform 解析锥 `n_3<31S_12/4+6581/960`；
- `DD`：调用经典 Schmidt Subspace Theorem 后得到非有效渐近界 `limsup m_3/S_12<=5` 与 `limsup n_3/S_12<=6.308883577618...`。这不是有效绝对高度界，更不是 DD 全局空性；
- `DD`：假想逼近该 frontier 的序列已被压到 moving pair-max Gaussian core；一般结构线仍剩 projective/common-scale allocation 与单侧 moving tail factor的兼容性问题；
- `DD frontier`：后续的 [rational-contact frontier](branches/double-deficit/frontier.md) 已把 rational-contact 子支进一步压到固定曲面、完整 prime-power sign contact 与 cofactor Lorentz 系统，并证明第一阶 rough height 与 real/5-adic cofactor proximity 都精确达到临界等号；因此普通 first-order GCD / Ridout / fixed-target Subspace 方法不能再重复收费；
- `DD frontier continuation`：最新 continuation 已合并到 [frontier 文件](branches/double-deficit/frontier.md)，在 full rational-contact frontier 上关闭 Bad，建立 Good square-Plücker 正规形，并证明 secondary repeat 与 radius repeat 等价；pair-max Gaussian orientation 可由 derivative gcd 唯一重构，正确的 second-order Newton resultant天然退化；
- `DD frontier continuation`：normalized near-square 的两个因子被精确展开为既有 `Z` 与 `q_c^2 U` source channels，因此完整 `2/5`-adic CRT phase不增加 rank；terminal denominator/source 被进一步包装成两张 exact `2x3` lattice sheet，自然 mixed determinant 在 main `C_L` 上横截；
- `DD frontier continuation`：full rational-contact 的 moving-core entropy可进一步压成 `10^{o(S)}`，但这仍不是 eventual emptiness。下一步应转向 global slot capacity / split-prime digit-shell，而不是继续堆同素数 Gaussian resultant；
- `DD` 的最高层中 `S_12 = 4, n_3 = 31` 已由完整有限证书关闭：`m_3 = 11,...,21` 的统一判别式均非平方，`m_3 = 22,...,26` 的 primitive denominator-tail 核为空。新得到的通用 `F_-` 大除数不依赖 resonance，但尚未导出全局绝对高度界；
- `DD` 的 `S_12=5,n_3=39` 已由后期有限证书全部关闭；
- `A_1`：为 saturated `L = 1` 支的 decimal shift `g` 找到全局界或直接矛盾。

先读 [严格证明状态](status.md)，再进入相应分支的入口文件：[A2 README](branches/a2-only/README.md)、[DD README](branches/double-deficit/README.md)、[A1 README](branches/a1-only/README.md)。不要把非有效渐近界、frontier 条件结论、subexponential counting、有限切片或 A2 的单个 allocation 子族排除写成全局关闭。

## 如何维护

新增内容应尽量遵循以下顺序：命题 → 假设 → 推导 → 依赖 → 状态 → 验证/开放缺口。若某个结论被否定，不删除历史推导，而是在对应章节标为 `失效/降级` 并说明原因。

原始总稿原样保留在 `archive/`，不再在根目录保留第二个可编辑副本。快照不是新的章节编辑入口。

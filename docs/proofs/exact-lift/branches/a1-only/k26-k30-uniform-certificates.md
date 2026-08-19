# A1 minimal diagonal: uniform fixed-layer certificates `k=26..30`

> 日期：2026-08-19。依赖 `uniform-layer-finite-box.md` 与 `uniform-2adic-prefix.md`。

本文继续 generic fixed-`k` finite-box certificate，把此前 `k<=25` 的有限层前沿推进到

\[
\boxed{k=g=26,27,28,29,30.}
\]

每一层都重新：

1. 精确 factor `b_1=10^{2k+1}-w` 与 `Q=10b_1+1`；
2. 构造完整 minimal-diagonal odd-prime supply `H_{k,w}`；
3. 用 `p`-adic root lifting 求 prefix 的 exact valuation floor；
4. 由 cross-corridor + decade 推出 theorem-derived finite exponent box；
5. 对盒内每个 exact rational state 检查旧的、更宽的 one-sided near-integer window
   \[
   5.09\,10^{-k}<\lceil\rho\rceil-\rho<50.45\,10^{-k}.
   \]

所有层的命中数均为 `0`。由于新 sharpened window `[15.09,39.003]` 严格包含于旧窗口，这些证书自动也是当前理论的更强有限排除。

状态：**已严格完成；附带脚本可精确复核。**

---

## 1. 结果总表

`H counts` 按 `w=1,2,3,4` 排列。

| `k` | `H counts` | `x* floor` | `y* floor` | exponent box `(xmin,xmax;ymin,ymax)` | decade states | wide-gap hits |
|---:|---|---:|---:|---|---:|---:|
| 26 | `(128,24,32,256)` | `-28` | `-66` | `(-329,239;-126,49)` | `146,580` | `0` |
| 27 | `(12288,160,32,512)` | `-29` | `-67` | `(-339,245;-130,51)` | `4,238,867` | `0` |
| 28 | `(256,768,16,64)` | `-30` | `-70` | `(-330,255;-126,52)` | `390,688` | `0` |
| 29 | `(64,96,128,256)` | `-31` | `-72` | `(-343,263;-131,54)` | `196,277` | `0` |
| 30 | `(32768,128,64,64)` | `-32` | `-75` | `(-378,273;-145,56)` | `11,672,944` | `0` |

因此

\[
\boxed{
26\le k=g\le30
\Longrightarrow
\text{minimal diagonal empty}.}
\tag{1}
\]

结合旧证书：

\[
\boxed{
1\le k=g\le30
\Longrightarrow
\text{minimal diagonal empty}.}
\tag{2}
\]

首个尚未由 fixed-layer certificate 关闭的层推进到

\[
\boxed{k=g\ge31.}
\tag{3}
\]

---

## 2. `2`-adic floor 与统一闭式一致

`uniform-2adic-prefix.md` 已证明对所有 `k>=3`

\[
\underline x_*(k)=-k-2.
\]

上表五层依次得到

\[
-28,-29,-30,-31,-32,
\]

与闭式完全一致。因此这些层真正需要 root lifting 的只有 `5`-adic prefix depth。

各层六类型的 `max v_5(N)` 为：

\[
\begin{array}{c|c}
k&((1,1),(1,2),(1,3),(1,4),(3,1),(3,2))\\ \hline
26&(37,37,37,40,37,38)\\
27&(39,38,40,39,40,39)\\
28&(40,41,40,42,40,40)\\
29&(42,43,42,41,42,42)\\
30&(45,43,43,43,43,43)
\end{array}
\]

因此

\[
\underline y_*(k)=-k-\max v_5(N)
\]

正好给表中的 `-66,-67,-70,-72,-75`。

---

## 3. `k=30` 的大 supply 不改变证书性质

`k=30,w=1` 的完整 odd-prime supply 达到

\[
|H_{30,1}|=32768.
\]

因此该层 decade state 数上升到一千一百余万。实际复核可把 `h` supply 分块并行；每个 worker 使用相同的 exact integer/rational inequalities，最终只对互不相交的 `h` 子集计数再求和。

这只是计算调度，不引入概率步骤，也不改变 certificate：总计

\[
\boxed{11,672,944}
\]

个 decade states 全部被检查，wide-gap hit 总数严格为

\[
\boxed0.
\]

---

## 4. 与 uniform central/deep 证明线的关系

这些 fixed-layer certificates 是保险线，不取代当前 `k`-uniform 的 central/deep 攻击。

当前统一理论已经把所有 `k>=26` 分成：

- central denominator：有限 type-gap + finite `U` generalized Pell families；
- deep denominator：valuation/resonance lattice + unit-square + directed Q-side supply。

本文的作用是把真正可能需要统一理论处理的首层从 `26` 再推到 `31`，并为后续任何全局高度界提供更宽的已验证基区间。

---

## 5. 可复核脚本

脚本：

`../../../../../scripts/exact-lift/a1-only/check_a1_top_diag_uniform_layers_26_30.py`

它复用 `check_a1_top_diag_uniform_layers.py` 中的 exact supply、root-lifting、box 与 rational-gap routines，并对上表 metadata 与 `0` hit 逐层断言。
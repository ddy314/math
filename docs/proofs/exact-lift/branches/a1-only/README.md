# `A_1`-only 分支

这是 `A_1` 分支的规范编辑入口。当前 minimal diagonal 的 central denominator 已统一关闭；double-deep 也已从二维指数格压到唯一 moderate `HL` 与 one-sided 2-extreme `E_2` 两支。

## 阅读顺序

1. [`core.md`](core.md)：A1 主框架与审计边界。
2. [`rational-contact.md`](rational-contact.md)：rational-contact、denominator funnel、resonance、cross-corridor、fixed-prefix finite theorem。
3. [`top-layer.md`](top-layer.md)：moving-prefix、`d=2` endpoint kernel、positive excess、minimal-surplus 分裂。
4. [`diagonal.md`](diagonal.md)：`k=g` minimal diagonal、valuation normal form、odd-prime supply。
5. [`near-integer-tail.md`](near-integer-tail.md)、[`positive-tail-residual.md`](positive-tail-residual.md)、[`sharp-positive-tail-window.md`](sharp-positive-tail-window.md)：
   \[
   \boxed{15.09\,10^{-k}<N_0-\rho<39.003\,10^{-k}.}
   \]
6. [`uniform-2adic-prefix.md`](uniform-2adic-prefix.md)：
   \[
   \boxed{\underline x_*(k)=-k-2.}
   \]
7. [`gap-denominator-normal-form.md`](gap-denominator-normal-form.md)：normalized gap 按 reduced denominator 分成 central / deep。
8. [`central-gap-2adic.md`](central-gap-2adic.md)、[`central-gap-sign-collapse.md`](central-gap-sign-collapse.md)、[`central-supply-pell-normal-form.md`](central-supply-pell-normal-form.md)、[`central-double-square-valuation-lock.md`](central-double-square-valuation-lock.md)、[`central-modular-exhaustion.md`](central-modular-exhaustion.md)：central 从 144 个 type-gap 压成 finite cells，最终 all-`k` exact modular cover 归零。
9. [`deep-gap-valuation-normal-form.md`](deep-gap-valuation-normal-form.md)、[`deep-gap-unit-square.md`](deep-gap-unit-square.md)：deep resonance/parity 与 2/5-adic unit-square locks。
10. [`deep-q-side-proper-divisor.md`](deep-q-side-proper-divisor.md)、[`deep-b1-block-loss.md`](deep-b1-block-loss.md)：strict 2-deep 的 Q-side direction、proper-divisor cap、`b_1` whole-block loss。
11. [`deep-complement-height.md`](deep-complement-height.md)、[`deep-first-complement-remainder.md`](deep-first-complement-remainder.md)、[`deep-balanced-collapse.md`](deep-balanced-collapse.md)：complement rational approximation、first remainder、fully-balanced collapse。
12. [`deep-universal-factorization.md`](deep-universal-factorization.md)、[`deep-four-factor-frame.md`](deep-four-factor-frame.md)：single / double deep 共享的 factor-pair 与 complementary four-factor frame。
13. [`deep-moderate-factorization.md`](deep-moderate-factorization.md)、[`deep-moderate-three-pattern.md`](deep-moderate-three-pattern.md)、[`deep-moderate-factor-quotients.md`](deep-moderate-factor-quotients.md)：moderate double-deep 的 finite `r` 与 LL/LH/HL 模板。
14. [`deep-typewise-r-window.md`](deep-typewise-r-window.md)、[`deep-moderate-block-partition.md`](deep-moderate-block-partition.md)、[`deep-moderate-adjugate-gcd-lock.md`](deep-moderate-adjugate-gcd-lock.md)、[`deep-hl-mod4-orientation.md`](deep-hl-mod4-orientation.md)：typewise finite `r`、`r_10` whole-block partition、gcd lock、HL orientation。
15. [`deep-double-5high-collapse.md`](deep-double-5high-collapse.md)：全部 double-deep 5-high 分支为空。
16. [`deep-ll-pell-normal-form.md`](deep-ll-pell-normal-form.md)、[`deep-ll-modular-exhaustion.md`](deep-ll-modular-exhaustion.md)：LL 化成 fixed Pell families，并对六 prefix 类型 exact modular exhaustion 到 `0`。
17. [`deep-root-factor-splitting.md`](deep-root-factor-splitting.md)：说明 moderate root-square 在 four-factor frame 中自动因式分裂，不能重复算独立 obstacle。
18. [`deep-hl-5adic-hensel-lock.md`](deep-hl-5adic-hensel-lock.md)：当前唯一 moderate 分支 HL 的 exact growing-depth 5-adic Hensel lock。
19. [`deep-extreme-classification.md`](deep-extreme-classification.md)、[`deep-extreme-height-collapse.md`](deep-extreme-height-collapse.md)：extreme 只能单侧；5-extreme 空；只剩 2-extreme `E_2`。
20. [`uniform-layer-finite-box.md`](uniform-layer-finite-box.md)、[`k24-k25-uniform-certificates.md`](k24-k25-uniform-certificates.md)、[`k26-k30-uniform-certificates.md`](k26-k30-uniform-certificates.md)、[`k31-uniform-certificate.md`](k31-uniform-certificate.md)：fixed-layer 保险证书。

## 当前严格状态

A1 整体仍为 `待证`。

minimal diagonal 已有：

\[
\boxed{1\le k=g\le31\Longrightarrow\text{empty}.}
\]

central denominator 已有统一结论：

\[
\boxed{k=g\ge26\Longrightarrow\text{central denominator empty}.}
\]

所以任何尚存 minimal-diagonal candidate 必须满足

\[
\boxed{k=g\ge32}
\qquad\text{且}\qquad
\boxed{\text{deep denominator}.}
\]

统一 deep 理论本身从 `k>=31` 已有效，因此 `k=31` fixed certificate 只是独立保险层。

对全部 `k>=3`：

\[
\Gamma_k:=10^k(N_0-\rho),
\qquad
\boxed{15.09<\Gamma_k<39.003.}
\]

并且 `rho<N_0`、saturated sector 为空、`ell>=k-1`。

## Central denominator：已完全关闭

`central-modular-exhaustion.md` 对 93,580,902 个 local-compatible finite states 做 exact periodic cover：

\[
93,580,902\longrightarrow33\text{ 个 }(t,k\bmod420)\longrightarrow\boxed0.
\]

因此 central 不再是待解核心。

## Deep：统一 skeleton

写

\[
\Gamma_k=\frac\gamma D,
\qquad D=2^A5^B,
\]

并把 non-deep side 留在 numerator 的 2/5 powers 记为

\[
\lambda=2^{\lambda_2}5^{\lambda_5}.
\]

则

\[
\boxed{DTN_0-\gamma=h\lambda,}
\qquad T=10^k,
\]

其中

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1,
\]

且 `s` 仍是 `1 mod 4` whole-block selector。

### complement height / first remainder

令

\[
M=Qb_1/h,
\qquad
\mu=\frac{MD}{\lambda T^2}.
\]

有

\[
1000<\mu<10001,
\]

\[
0<\frac{MDN_0}{\lambda T^3}-1000<\frac{390100}{T^2}.
\]

并定义

\[
J_1:=\frac{M\gamma+C_0\lambda}{T}\in\mathbf Z,
\]

\[
R_1:=10(1-20w)\lambda T+J_1,
\]

则

\[
\boxed{MDN_0=1000\lambda T^3+R_1,}
\]

\[
\boxed{14300\lambda T<R_1<390100\lambda T.}
\]

这条 first remainder 已用于关闭整个 double-deep 5-high 方向。

### fully-balanced 已排除

若

\[
A+v_2(w)+v_2(N_0)\ge k+\lambda_2,
\]

且

\[
B+v_5(N_0)\ge k+\lambda_5,
\]

则无解。因此每个 deep candidate 至少有一个 shallow side。

### universal factor / four-factor

对任意 single / double deep，存在正整数 `t,a,b`：

\[
\boxed{10\gamma T-wDN_0=sa,}
\]

\[
\boxed{100\gamma T-(10w-1)DN_0=qb,}
\]

\[
\boxed{ab=t.}
\]

写

\[
\bar q=Q/q,
\qquad
\bar s=b_1/s,
\]

还有

\[
\boxed{qb-10sa=DN_0,}
\]

\[
\boxed{\bar s b-\bar q a=10\lambda T.}
\]

并产生 complementary square

\[
S^2=100\lambda^2T^2+4tM,
\]

及

\[
S-10\lambda T=2a\bar q,
\qquad
S+10\lambda T=2b\bar s.
\]

## Double-deep：只剩 2-high / 5-low

### moderate

moderate 指

\[
A,B\le2k+3.
\]

此时

\[
\frac tD=r\in\mathbf Z,
\]

且 `deep-typewise-r-window.md` 给六类型：

\[
\begin{array}{c|c}
(z,w)&r\\ \hline
(1,1)&761760\le r\le10885221\\
(1,2)&542890\le r\le8400003\\
(1,3)&361000\le r\le6236387\\
(1,4)&216090\le r\le4394372\\
(3,1)&384160\le r\le15204352\\
(3,2)&299290\le r\le13677244
\end{array}
\]

transition strips 已排除，原三模板为 LL/LH/HL。

#### LH：已关闭

`deep-double-5high-collapse.md` 用 first remainder 证明 moderate 5-high `LH` 全空；此前 5-extreme 也已空。所以 double-deep 不存在任何 5-high state。

#### LL：已关闭

LL 有

\[
D\mid r,
\]

并化成 fixed Pell family

\[
Y^2=A_{\gamma,r,D}L^2+B_{\gamma,r,D},
\qquad L=10^k/D.
\]

六类型 exact modular exhaustion 的统计：

\[
\begin{array}{c|r|r|r|r|r|r}
(z,w)&\text{local}&P_0&k\bmod420&P_1&k\bmod277200&\text{final}\\ \hline
(1,1)&57,278,520&593,553&1,016,555&93,222&6,980&0\\
(1,2)&19,206,685&93,027&155,388&13,674&916&0\\
(1,3)&25,308,717&162,735&258,880&20,743&1,530&0\\
(1,4)&4,331,873&18,342&28,788&2,271&154&0\\
(3,1)&306,099,009&3,156,352&5,421,691&500,727&37,426&0\\
(3,2)&110,439,962&575,335&974,681&86,545&6,020&0
\end{array}
\]

总 local-compatible fixed families：

\[
\boxed{522,664,766},
\]

最终 periodic survivors：

\[
\boxed0.
\]

所以

\[
\boxed{\text{moderate LL empty for all six types and all }k\ge31.}
\]

#### moderate 当前只剩 HL

因此：

\[
\boxed{\text{moderate double-deep}=HL.}
\]

HL 满足

\[
\boxed{A=2k+3-v_2(r),}
\]

\[
\boxed{B+2\nu_5=v_5(r)\le10.}
\]

对 `(1,2),(1,3),(1,4)` 更强为 `<=9`。

写

\[
r_{10}=r/2^{v_2(r)}5^{v_5(r)},
\qquad \alpha\beta=r_{10},
\qquad \gcd(\alpha,\beta)=1.
\]

HL orientation：

\[
\alpha\equiv3\pmod4\quad(w=1,3),
\qquad
\alpha\equiv1\pmod4\quad(w=2,4),
\]

\[
\boxed{\beta\equiv3\pmod4.}
\]

adjugate 还给

\[
\boxed{\gcd(N_0,\gamma)\mid r_{10}<15,214,000.}
\]

HL 的 exact 5-adic Hensel lock 为：若

\[
r=5^{a_5}r_5,
\qquad N_0=5^{\nu_5}n,
\]

则

\[
\boxed{
v_5\left(r_5\gamma+C_0 2^{2k+3-v_2(r)}n^2\right)
=k+1-a_5+\nu_5.}
\]

这是当前 moderate 的主攻击入口。

`deep-root-factor-splitting.md` 同时确认 denominator-free root square 在 full four-factor frame 中会自动因式分裂，不能重复当作独立 obstacle。

### extreme：只剩 `E_2`

双 extreme 不可能；5-extreme 已由 height bound 排除。唯一 extreme 为

\[
\boxed{E_2:\quad A=2k+3+E,\quad E>0,}
\]

且其 5-side 必 shallow-low。现有 bound：

\[
\boxed{B+\nu_5<7+0.570k,}
\]

更深的 2-side 可用更强 `8+0.139k` bound。

所以完整 double-deep 已变成

\[
\boxed{\text{double-deep}=HL_{\rm moderate}\cup E_2.}
\]

两支都是 2-high / 5-low。

## Single-deep

single-deep 尚未关闭，但不再拥有独立框架：它与 double-deep 共用

- complement height；
- first remainder；
- universal factor pair；
- complementary four-factor frame；
- 2/5 unit-square locks。

下一阶段应在同一 skeleton 下按 single-2 / single-5 的 `lambda_2,lambda_5` 平移处理。

## Fixed-layer 保险线

完整 exact certificates 当前关闭

\[
\boxed{k=1,2,\ldots,31.}
\]

最新 `k=31`：

\[
(|H_1|,|H_2|,|H_3|,|H_4|)=(16384,96,16,96),
\]

finite box

\[
(x,y)\in[-321,284]\times[-120,58],
\]

exact decade states：

\[
\boxed{6,146,672},
\]

并继续检查旧的更宽 window

\[
5.09<10^{31}(\lceil\rho\rceil-\rho)<50.45,
\]

得到

\[
\boxed{0\text{ hits}.}
\]

所以首个未关闭 fixed layer 是

\[
\boxed{k=32.}
\]

## 下一步

minimal diagonal 当前真正只需继续三个统一核心：

1. **moderate HL**：把 growing 5-adic Hensel lock 与 stripped equations / Q-side orientation 联立，争取再做一次 finite descent；
2. **2-extreme `E_2`**：利用 first remainder + pure-2 excess denominator 压缩 `E`；
3. **single-deep**：在同一 universal factor frame 下处理 `lambda` 平移后的 single-2 / single-5。

`d=1,0,-1` 等其他 A1 top-layer 无界核心仍待处理；本 README 的“关闭”均只指上述 minimal diagonal 子问题。

## 主要可复核脚本

位于 [`scripts/exact-lift/a1-only/`](../../../../../scripts/exact-lift/a1-only/)：

- `check_a1_top_diag_uniform_layers.py`：`k=6..23`；
- `check_a1_top_diag_uniform_layers_24_25.py`：`k=24,25`；
- `check_a1_top_diag_uniform_layers_26_30.py`：`k=26..30`；
- `check_a1_top_diag_uniform_layer_31.py`：`k=31`；
- `check_a1_central_modular_exhaustion.cpp`：全部 central `k>=26`；
- `check_a1_deep_ll_modular_exhaustion.cpp`：全部 moderate LL `k>=31`；
- `check_a1_deep_gap_unit_square.py`；
- 以及 near-integer、k1..k6 等历史审计脚本。
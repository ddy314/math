# `A_1`-only 分支

这是 `A_1` 分支的规范编辑入口。当前 minimal diagonal 的 central denominator 已经统一关闭；真正剩余的无界核心只在 `k>=31` 的 deep denominator。

## 阅读顺序

1. [`core.md`](core.md)：A1 主框架与审计边界。
2. [`rational-contact.md`](rational-contact.md)：rational-contact、denominator funnel、resonance、cross-corridor 与 fixed-prefix finite theorem。
3. [`top-layer.md`](top-layer.md)：moving-prefix、`d=2` endpoint kernel、positive excess 与 minimal-surplus 分裂。
4. [`diagonal.md`](diagonal.md)：`k=g` minimal diagonal、valuation normal form、odd-prime supply。
5. [`near-integer-tail.md`](near-integer-tail.md)、[`positive-tail-residual.md`](positive-tail-residual.md)、[`sharp-positive-tail-window.md`](sharp-positive-tail-window.md)：
   \[
   \boxed{15.09\,10^{-k}<N_0-\rho<39.003\,10^{-k}.}
   \]
6. [`uniform-2adic-prefix.md`](uniform-2adic-prefix.md)：
   \[
   \boxed{\underline x_*(k)=-k-2.}
   \]
7. [`gap-denominator-normal-form.md`](gap-denominator-normal-form.md)：按 normalized gap reduced denominator 分成 central / deep。
8. [`central-gap-2adic.md`](central-gap-2adic.md)、[`central-gap-sign-collapse.md`](central-gap-sign-collapse.md)、[`central-crossing-sharp.md`](central-crossing-sharp.md)：central `144 -> 48 -> 30`。
9. [`central-supply-pell-normal-form.md`](central-supply-pell-normal-form.md)、[`central-pell-local-squareclass.md`](central-pell-local-squareclass.md)、[`central-double-square-valuation-lock.md`](central-double-square-valuation-lock.md)：把 30 个 central type-gap 压成绝对有限 `t=U-U_0` cells。
10. [`central-modular-exhaustion.md`](central-modular-exhaustion.md)：exact finite modular cover；全部 central `k>=26` 统一为空。
11. [`deep-gap-valuation-normal-form.md`](deep-gap-valuation-normal-form.md)、[`deep-gap-unit-square.md`](deep-gap-unit-square.md)：deep resonance/parity 与 2/5-adic unit-square locks。
12. [`deep-q-side-proper-divisor.md`](deep-q-side-proper-divisor.md)、[`deep-b1-block-loss.md`](deep-b1-block-loss.md)：strict 2-deep 的 Q-side direction、proper-divisor cap 与 `b_1` whole-block loss。
13. [`deep-complement-height.md`](deep-complement-height.md)：`T^-2` rational approximation 与 deep logarithmic height bound。
14. [`deep-balanced-collapse.md`](deep-balanced-collapse.md)：任意 fully-balanced deep state 全部为空。
15. [`deep-universal-factorization.md`](deep-universal-factorization.md)、[`deep-four-factor-frame.md`](deep-four-factor-frame.md)：single / double deep 共享的 universal factor-pair 与 complementary four-factor frame。
16. [`deep-global-factorization.md`](deep-global-factorization.md)：double-deep 的 bounded renormalized parameter `t/D` 与 excess denominator。
17. [`deep-moderate-factorization.md`](deep-moderate-factorization.md)、[`deep-moderate-three-pattern.md`](deep-moderate-three-pattern.md)、[`deep-moderate-factor-quotients.md`](deep-moderate-factor-quotients.md)、[`deep-moderate-root-normal-form.md`](deep-moderate-root-normal-form.md)：moderate double-deep 从二维 `(A,B)` 压成 LL/LH/HL 三模板、finite `r` 与 root branches。
18. [`deep-extreme-classification.md`](deep-extreme-classification.md)、[`deep-extreme-height-collapse.md`](deep-extreme-height-collapse.md)：extreme 只能单侧发生，且 5-extreme 已完全排除；只剩 one-sided 2-extreme。
19. [`uniform-layer-finite-box.md`](uniform-layer-finite-box.md)、[`k24-k25-uniform-certificates.md`](k24-k25-uniform-certificates.md)、[`k26-k30-uniform-certificates.md`](k26-k30-uniform-certificates.md)：fixed-layer 保险证书。
20. [`short-tail-saturation.md`](short-tail-saturation.md)：历史中间记录；saturated 已被后续结果排除。

## 当前状态

A1 整体仍为 `待证`。minimal diagonal 已严格得到：

\[
\boxed{1\le k=g\le30\Longrightarrow\text{empty}.}
\]

并且

\[
\boxed{k=g\ge26\Longrightarrow\text{central denominator empty}.}
\]

因此任何尚存 minimal-diagonal candidate 必须满足

\[
\boxed{k=g\ge31}
\qquad\text{且}\qquad
\boxed{\text{deep denominator}.}
\]

对全部 `k>=3`：

\[
\Gamma_k:=10^k(N_0-\rho),
\qquad
\boxed{15.09<\Gamma_k<39.003.}
\]

同时 `rho<N_0`、saturated sector 为空、`ell>=k-1`。

## Central denominator：已完全关闭

central 经 2-adic、sign、Euclidean descent、local squareclass 与 double-square valuation lock 后，只需检查 93,580,902 个 local-compatible `t`。`central-modular-exhaustion.md` 用 `ord_p(10)|420` 的公共素数把它们压到 33 个 `(t,k mod 420)` 状态，再用补充素数做 CRT compatibility，最终存活数为

\[
\boxed{0}.
\]

所以 central Pell / primitive-divisor 已不再是待解核心。

## Deep denominator：统一框架

写

\[
\Gamma_k=\frac\gamma D,
\qquad
D=2^A5^B,
\]

并把非 deep 一侧留在 numerator 的 `2/5` powers 写成

\[
\lambda=2^{\lambda_2}5^{\lambda_5}.
\]

则

\[
\boxed{DTN_0-\gamma=h\lambda,}
\qquad T=10^k,
\]

其中完整 odd-prime supply 为

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1
\]

（`s` 仍 obey `1 mod4` whole-block selector）。

### complement-height

令

\[
M=Qb_1/h,
\qquad
\mu=\frac{MD}{\lambda T^2}.
\]

已有

\[
1000<\mu<10001,
\]

\[
\boxed{
0<\frac{MDN_0}{\lambda T^3}-1000
<\frac{390100}{T^2}.}
\]

因此 general deep 必须满足

\[
\boxed{
2^{(3k+\lambda_2-A-e-\nu_2)_+}
5^{(3k+\lambda_5-B-\nu_5)_+}
>
\frac{10^{2k}}{390100},}
\]

其中

\[
e=v_2(w),\qquad
\nu_p=v_p(N_0).
\]

### fully-balanced deep 已排除

`deep-balanced-collapse.md` 证明：若

\[
A+e+\nu_2\ge k+\lambda_2,
\qquad
B+\nu_5\ge k+\lambda_5,
\]

则必无解。故每个 deep candidate 至少有一侧 shallow：

\[
\boxed{
A+e+\nu_2<k+\lambda_2
\quad\text{或}\quad
B+\nu_5<k+\lambda_5.}
\]

证明中会产生 bounded integer

\[
15091\le J\le390069
\]

并把 `Gamma_k` 化成

\[
\Gamma_k=
\frac{N_0(JT^2-C_0)}
{T(1000T^2+J+10(1-20w))},
\]

再由 denominator odd-part 得到尺寸矛盾。

### universal factor-pair

对任意 single / double deep，`deep-universal-factorization.md` 证明存在正整数 `t,a,b`：

\[
\boxed{
X_1:=10\gamma T-wDN_0=sa,}
\]

\[
\boxed{
X_2:=100\gamma T-(10w-1)DN_0=qb,}
\]

\[
\boxed{ab=t,}
\]

并且

\[
\boxed{
X_1X_2=t h.}
\]

同时

\[
\boxed{
t\equiv-1000\lambda\gamma T^2\pmod D,}
\]

且

\[
\boxed{
196000\lambda<\frac tD<15214000\lambda.}
\]

因此 single / double deep 现在共享同一套 divisor skeleton。

### complementary four-factor frame

写

\[
\bar q=Q/q,
\qquad
\bar s=b_1/s.
\]

则还有精确对偶关系

\[
\boxed{qb-10sa=DN_0,}
\]

\[
\boxed{\bar s b-\bar q a=10\lambda T.}
\]

并产生两条额外 integer-square identities：

\[
\boxed{R^2=D^2N_0^2+40th,}
\]

\[
\boxed{S^2=100\lambda^2T^2+4tM.}
\]

进一步

\[
\boxed{S-10\lambda T=2a\bar q,}
\qquad
\boxed{S+10\lambda T=2b\bar s,}
\]

所以

\[
\boxed{X_2(S-10\lambda T)=2tQ,}
\]

\[
\boxed{X_1(S+10\lambda T)=2tb_1.}
\]

prime supply 与 complementary supply 都已经显式接入同一组 `(a,b,t)`。

## Double-deep：当前已压成四类

### moderate：`A,B<=2k+3`

此时

\[
\frac tD=r\in\mathbf Z,
\qquad
\boxed{196000<r<15214000,}
\]

所以

\[
v_2(r)\le23,
\qquad
v_5(r)\le10.
\]

所有 2/5 transition strips 在 `k>=31` 均已排除，high-high 又被 fully-balanced theorem 排除，因此只剩三种模板：

\[
\boxed{LL:}
\qquad
A+2\nu_2+e=v_2(r),
\quad
B+2\nu_5=v_5(r),
\]

\[
\boxed{LH:}
\qquad
A+2\nu_2+e=v_2(r),
\quad
B=2k+3-v_5(r),
\]

\[
\boxed{HL:}
\qquad
A=2k+3-v_2(r),
\quad
B+2\nu_5=v_5(r).
\]

因此 moderate 已不再有二维 exponent freedom。

若

\[
r_{10}=r/2^{v_2(r)}5^{v_5(r)},
\]

则在三模板中把 `a,b` 的显式 2/5 powers 除尽后，都有

\[
\boxed{\alpha\beta=r_{10}.}
\]

所以剩余 quotient 只来自 finite divisor pair。

moderate 还具有 denominator-free root normal form：存在整数 `Z>0`：

\[
\boxed{
Z^2=(10N_0T+r)^2+400N_0Tr(10T^2-w),}
\]

\[
\boxed{
\Gamma_k=
\frac{10(20w-1)N_0T-r+Z}{2000T^2}.}
\]

于是 `D` 只是这个有理数约分后恢复出的 2/5 denominator。并且

\[
Z^2\equiv r^2\pmod T,
\]

所以 LL/LH/HL 可解释成 2-adic / 5-adic square-root 的 `(+,+),(+,-),(-,+)` 三种 branch；`(-,-)` 即已排除的 high-high。

### extreme

两侧不能同时 extreme，因为 `D<10000T^2`。

`deep-extreme-height-collapse.md` 进一步证明 5-extreme 完全为空。因此唯一 extreme 分支是

\[
\boxed{E_2:\quad A=2k+3+E,\ E>0,}
\]

并且必有 5-side shallow-low：

\[
\boxed{B+\nu_5<7+0.570k.}
\]

这里

\[
v_2(t)=2k+3,
\qquad
v_5(t)=2B+2\nu_5,
\]

故

\[
\boxed{
\frac tD
=
\frac{5^{B+2\nu_5}r_{10}}{2^E},
\qquad
196000<\frac tD<15214000.}
\]

所以 extreme 剩余已经是 pure-2 denominator descent。

综上 double-deep 当前只有

\[
\boxed{LL\cup LH\cup HL\cup E_2.}
\]

没有 transition、high-high、double-extreme 或 5-extreme。

## Strict 2-deep supply loss

unit-square lock 继续给

\[
w\text{ odd}\Rightarrow q\equiv1\pmod4,
\qquad
w\text{ even}\Rightarrow q\equiv3\pmod4,
\]

并有

\[
q\le Q/7\quad(w=1,3,4),
\qquad q\le Q/3\quad(w=2).
\]

结合 `b_1` whole-block loss：

\[
\boxed{
h\le
\begin{cases}
Qb_1/21,&w=1,\\
Qb_1/42,&w=2,\\
Qb_1/7,&w=3,\\
Qb_1/84,&w=4.
\end{cases}}
\]

strict 5-low 还保留 Legendre lock。

## Fixed-layer 保险线

完整 exact certificates 当前关闭

\[
\boxed{k=1,2,\ldots,30.}
\]

`k=31` 尚未计入：此前 `w=4` 的 Q-side factorization 未完整结束，因此不使用 partial factor data 冒充证书。

## 下一步

minimal diagonal 现在只需处理 deep，且结构已经进一步分层：

1. moderate double-deep：对 LL/LH/HL 的 finite `r`、`alpha beta=r_10` 与 four-factor frame 做 periodic modular exhaustion / resultant；
2. 2-extreme：继续 pure-2 denominator descent，结合 Q-side direction 与 complement-height；
3. single-deep：利用 universal factorization / four-factor frame，不再维护独立的第三尾方法；
4. fixed-layer certificate 仅作保险线继续推进。

`d=1,0,-1` 等其他 A1 无界核心仍待处理。

## 可复核脚本

分支脚本位于 [`scripts/exact-lift/a1-only/`](../../../../../scripts/exact-lift/a1-only/)。主要包括：

- `check_a1_top_diag_uniform_layers.py`：`k=6..23`；
- `check_a1_top_diag_uniform_layers_24_25.py`：`k=24,25`；
- `check_a1_top_diag_uniform_layers_26_30.py`：`k=26..30`；
- `check_a1_central_modular_exhaustion.cpp`：全部 central `k>=26`；
- `check_a1_deep_gap_unit_square.py`；
- `check_a1_deep_moderate_factorization.py`；
- `check_a1_deep_universal_factorization.py`；
- 以及早期 near-integer / finite-layer 审计脚本。
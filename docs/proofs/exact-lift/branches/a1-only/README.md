# `A_1`-only 分支

这是 `A_1` 分支的规范编辑入口。当前 minimal diagonal 的 central denominator 已经统一关闭；真正剩余的无界核心只在 deep denominator。

## 阅读顺序

1. [`core.md`](core.md)：A1 主框架与审计边界。
2. [`rational-contact.md`](rational-contact.md)：rational-contact、integer-gap、denominator funnel、resonance、cross-corridor 与 fixed-prefix finite theorem。
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
7. [`gap-denominator-normal-form.md`](gap-denominator-normal-form.md)：按 normalized gap 的 reduced denominator 分成 central / deep。
8. [`central-gap-2adic.md`](central-gap-2adic.md)、[`central-gap-sign-collapse.md`](central-gap-sign-collapse.md)、[`central-crossing-sharp.md`](central-crossing-sharp.md)：central `144 -> 48 -> 30`，并收紧唯一 sign crossing。
9. [`central-supply-pell-normal-form.md`](central-supply-pell-normal-form.md)、[`central-pell-local-squareclass.md`](central-pell-local-squareclass.md)、[`central-double-square-valuation-lock.md`](central-double-square-valuation-lock.md)：把 30 个 central type-gap 化成绝对有限 `t=U-U_0` cells。
10. [`central-modular-exhaustion.md`](central-modular-exhaustion.md)：对全部 93,580,902 个 local-compatible `t` 做 exact finite modular cover，最终 `0` 状态；因此 central 对所有 `k>=26` 统一为空。
11. [`deep-gap-valuation-normal-form.md`](deep-gap-valuation-normal-form.md)：deep excess `(A,B)` 与 2/5 resonance/parity lattice。
12. [`deep-gap-unit-square.md`](deep-gap-unit-square.md)：mod-8 unit square、mod-5 Legendre lock 与 Q-side direction。
13. [`deep-q-side-proper-divisor.md`](deep-q-side-proper-divisor.md)、[`deep-b1-block-loss.md`](deep-b1-block-loss.md)：strict 2-deep 的 Q-side proper-divisor 与 `b_1` whole-block loss。
14. [`deep-complement-height.md`](deep-complement-height.md)：从 complement quotient 得到 `T^-2` 级 rational approximation 与 deep logarithmic height bound。
15. [`uniform-layer-finite-box.md`](uniform-layer-finite-box.md)、[`k24-k25-uniform-certificates.md`](k24-k25-uniform-certificates.md)、[`k26-k30-uniform-certificates.md`](k26-k30-uniform-certificates.md)：fixed-layer 保险证书。
16. [`short-tail-saturation.md`](short-tail-saturation.md)：历史中间记录；saturated 已被后续结果排除。

## 当前状态

A1 整体仍为 `待证`，但 minimal diagonal 已严格得到两条互补结论。

第一，fixed-layer certificates 已关闭

\[
\boxed{1\le k=g\le30.}
\]

第二，central denominator sector 已统一关闭

\[
\boxed{
 k=g\ge26
 \Longrightarrow
 \text{central denominator impossible}.}
\]

因此任何尚存 minimal-diagonal candidate 必须同时满足

\[
\boxed{k=g\ge31}
\]

和

\[
\boxed{\text{deep denominator}.}
\]

对全部 `k>=3`，写

\[
\Gamma_k:=10^k(N_0-\rho),
\]

则

\[
\boxed{15.09<\Gamma_k<39.003.}
\]

并且 `rho<N_0`、saturated sector 为空、`ell>=k-1`。

## Central denominator：已关闭

central 意味着 reduced denominator `d|10^k`，所以 `Gamma_k` 是整数。此前只剩 30 个 `(z,w,Gamma)`。

Euclidean descent 引入绝对有限参数 `U`，令

\[
c=2^{v_2(\Gamma)}5^{v_5(\Gamma)},\qquad
r=\Gamma/c,\qquad
L=10^k/c,
\]

\[
U_0=10c\Gamma(20w-1),\qquad t=U-U_0.
\]

`U` 有与 `k` 无关的严格有限窗，并且 supply-Pell square 与原 contact square 联立后给

\[
\boxed{
v_2(N_0)=\frac{v_2(t)-v_2(w(10w-1))}{2},
\qquad
v_5(N_0)=\frac{v_5(t)}2.}
\]

再加 `Q_2/Q_5` unit-square 后，30 个 type-gap 合计只需检查

\[
\boxed{93,580,902}
\]

个 `t`。

`central-modular-exhaustion.md` 使用公共素数集

\[
\{3,7,11,13,29,31,37,41,43,61,71,101,127,211,239,241,271,281,421,1933,2161,2689,3541,4649\}
\]

（全部满足 `ord_p(10)|420`），把它们压成 33 个 `(t,k mod420)` 状态；再用

\[
\{17,19,73,89,113,137,251,337,1009,4201\}
\]

做 CRT compatibility，最终

\[
\boxed{0}
\]

个状态存活。

所以 central Pell / primitive-divisor 不再是待解核心。

## Deep denominator：唯一统一核心

写

\[
\Gamma_k=\frac{\gamma}{2^A5^B},
\qquad
A=(a-k)_+,
\quad B=(b-k)_+,
\]

其中至少一个正。

已有 valuation/resonance：

- `w=2,4`：`A>0` 时 `A` 必为奇数；
- `w=1,3`、`v_2(N)=0`：`A=1` resonance，strict-low 只允许 `A=3,5,...`；
- `w=1,3`、`v_2(N)=1`：`A=1` high-side、`A=2` resonance，strict-low 只允许 `A=4,6,...`；
- `B>v_5(N)` 时 `B≡v_5(N) (mod 2)`，而 `B=v_5(N)` 是 5-adic resonance。

strict 2-low 还有

\[
\gamma QN_2 5^B\equiv1\pmod8,
\]

从而 Q-side divisor `q|Q` 被定向：

\[
w\text{ odd}\Rightarrow q\equiv1\pmod4,
\qquad
w\text{ even}\Rightarrow q\equiv3\pmod4.
\]

并有

\[
q\le Q/7\quad(w=1,3,4),
\qquad q\le Q/3\quad(w=2).
\]

结合 `b_1` whole-block loss，strict 2-deep 的 odd supply 满足

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

### 新的 complement-height inequality

令

\[
D=2^A5^B,
\qquad
DTN_0-\gamma=h\lambda,
\qquad
M=Qb_1/h,
\qquad T=10^k.
\]

则

\[
\mu:=\frac{MD}{\lambda T^2}
\]

严格满足

\[
1000<\mu<10001,
\]

并产生

\[
\boxed{
0<\frac{MDN_0}{\lambda T^3}-1000
<\frac{390100}{T^2}.}
\]

因此这个有理数的既约分母必须大于 `T^2/390100`。

若

\[
e=v_2(w),\qquad
\nu_2=v_2(N_0),\qquad
\nu_5=v_5(N_0),
\]

则 general deep 必须满足

\[
\boxed{
2^{(3k+\lambda_2-A-e-\nu_2)_+}
5^{(3k+\lambda_5-B-\nu_5)_+}
>
\frac{10^{2k}}{390100}.}
\]

特别地 double-deep `A,B>0` 有

\[
\boxed{
2^{\min(A+e+\nu_2,3k)}
5^{\min(B+\nu_5,3k)}
<390100\,10^k.}
\]

并推出

\[
B+\nu_5<3k,
\]

而若 `A+e+nu_2>=3k`，则更强地

\[
\boxed{B+\nu_5<8+0.139k.}
\]

这已经把 double-deep 从无界二维平面压入显式 logarithmic height strip。

## Fixed-layer 保险线

`k=26..30` 仍使用旧的更宽窗口 `[5.09,50.45]` 做 exact finite-box check，因此是当前 sharpened theory 的更强验证：

| `k` | `H counts (w=1..4)` | decade states | hits |
|---:|---|---:|---:|
| 26 | `(128,24,32,256)` | `146580` | 0 |
| 27 | `(12288,160,32,512)` | `4238867` | 0 |
| 28 | `(256,768,16,64)` | `390688` | 0 |
| 29 | `(64,96,128,256)` | `196277` | 0 |
| 30 | `(32768,128,64,64)` | `11672944` | 0 |

`k=31` 尚未计入证书；此前本地 factorization 的 `w=4` Q-side 未完整结束，因此不使用 partial factor data 冒充结论。

## 下一步

minimal diagonal 现在只需处理 deep：

1. 先把 `deep-complement-height.md` 的 denominator lower bound 与原 resonance/cross-corridor 坐标联立，继续压缩 single-deep 与 double-deep 的允许斜率；
2. 对 strict 2-deep 同时使用 Q-side orientation、proper-divisor cap、`b_1` block loss；
3. 对 strict 5-deep 使用 Legendre unit lock；
4. fixed-layer 证书只作为保险线继续推进，不再分散 central 上的工作。

`d=1,0,-1` 等其他 A1 无界核心仍待处理。

## 可复核脚本

分支脚本位于 [`scripts/exact-lift/a1-only/`](../../../../../scripts/exact-lift/a1-only/)。主要包括：

- `check_a1_top_diag_uniform_layers.py`：`k=6..23`；
- `check_a1_top_diag_uniform_layers_24_25.py`：`k=24,25`；
- `check_a1_top_diag_uniform_layers_26_30.py`：`k=26..30`；
- `check_a1_central_double_square_valuations.py`；
- `check_a1_central_modular_exhaustion.cpp`：全部 central `k>=26`；
- `check_a1_deep_gap_unit_square.py`；
- 以及早期 `k=1..5`、`k=6`、near-integer constants 等审计脚本。
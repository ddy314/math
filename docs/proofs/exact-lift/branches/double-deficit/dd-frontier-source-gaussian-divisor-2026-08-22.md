# DD frontier: source Gaussian divisor 与 source-lift 分离

> 日期：2026-08-22
>
> 作用域：假想 corrected `6.308883...` terminal one-channel frontier。所有 `main` statement 默认删除总高度 `o(S)` 的 coefficient / denominator-normal-form exceptional core。

## 1. derivative orientation 的 source-only projection

已有 derivative Gaussian integer

\[
D_{\rm der}
=2\widetilde rL_{\rm clean}q_c-iP_0,
\]

以及

\[
\boxed{\Pi\mid D_{\rm der},
\qquad N(\Pi)=C_L.}
\tag{1.1}
\]

clean source为

\[
q_c^2L_{\rm clean}=VA_0-5^TR_0,
\qquad V=C_Lv_0.
\tag{1.2}
\]

将 `(1.1)` 乘 `q_c`，使用 `(1.2)`：

\[
\begin{aligned}
q_cD_{\rm der}
&=2\widetilde r q_c^2L_{\rm clean}-iP_0q_c\\
&=2\widetilde rC_Lv_0A_0
-2\widetilde r5^TR_0-iP_0q_c.
\end{aligned}
\]

因为 `Pi|C_L`，第一项自动被 `Pi` 整除。因此得到不含 `C_L,A_0,L_clean` 的 carrier：

\[
\boxed{
\Pi\mid\mathcal S_{\rm src},
\qquad
\mathcal S_{\rm src}
:=2\widetilde r5^TR_0+iP_0q_c.
}
\tag{Source-Gaussian}
\]

所以

\[
\boxed{
C_L\mid N(\mathcal S_{\rm src})
}
\tag{1.3}
\]

在 main effective-core 意义下成立。

这给出 derivative orientation 的反向读取：固定 `q_c` 与 slow data 后，pair-max core只能来自一个固定 Gaussian integer的 Gaussian divisors。

## 2. hidden-square parent

该 divisibility并不是新的 height obstruction。已有 hidden square

\[
(C_LP_1)^2+P_0^2
=4\widetilde r^{\,2}5^TR_0L_{\rm clean}.
\tag{2.1}
\]

乘以 `q_c^2`，再用 `(1.2)`：

\[
P_0^2q_c^2
=4\widetilde r^{\,2}5^TR_0
(C_Lv_0A_0-5^TR_0)
-C_L^2(q_cP_1)^2.
\]

因此

\[
\boxed{
N(\mathcal S_{\rm src})
=C_L\left(
4\widetilde r^{\,2}5^TR_0v_0A_0
-C_L(q_cP_1)^2
\right).
}
\tag{Source-norm-parent}
\]

所以 `(1.3)` 是 hidden square + clean source 的 source-side projection；不能把 `C_L|N(S_src)` 再当一份新的 p-adic height收费。

## 3. counting consequence

虽然不是新 height，`(Source-Gaussian)` 对 counting 是有用的。

固定 `q_c` 与同一个 subexponential slow-data fiber后，`S_src` 完全固定。任意 admissible `(C_L,Pi)` 的 main Gaussian orientation满足

\[
\Pi\mid S_{\rm src}.
\]

Gaussian divisor bound给

\[
\boxed{
\#\{(C_L,\Pi)\text{ for fixed }q_c\}
=10^{o(S)}.
}
\tag{3.1}
\]

这与此前通过 derivative gcd / rational axis得到的 entropy collapse相容，但不要求进入 full-rational sign branch。

因此 one-channel terminal 上，`C_L/Pi` 本身没有独立的正线性 divisor-choice entropy；剩余 source lift仍由 `q_c` 的短 interval控制。

## 4. 不同 source lifts 的 pairwise common-core bound

固定 slow data，写

\[
\mathcal S(q)=A+iBq,
\qquad
A:=2\widetilde r5^TR_0,
\quad B:=P_0.
\]

取两个不同 source lifts `q_1,q_2`。若 Gaussian integer `Gamma` 同时整除两个 source carriers，则

\[
\Gamma\mid iB(q_1-q_2).
\tag{4.1}
\]

main pair-max prime与 `B=P_0` 的 overlap只有 `10^{o(S)}` 高度，所以删去 exceptional core后，`Gamma` 的 norm必须进入 rational difference `q_1-q_2`。

source congruence为

\[
s\theta q_c\equiv-5^T\widetilde r\pmod{2^{m_2}}.
\]

删除 `s theta` 的 `o(S)` 2-adic coefficient后，可把同一 fiber中的 lifts写成

\[
q_j=q_0+2^{m_2-o(S)}k_j.
\]

由于 main pair-max primes为 odd non-decimal primes，`2`-power对其不可见；因此 `(4.1)` 的 main rational norm进入

\[
k_1-k_2
\]

外加 `10^{o(S)}` coefficient core。

而 lift index range为

\[
0\le k<10^{\delta_*S+o(S)},
\qquad
\delta_*=0.007853581954\ldots.
\]

所以两个不同 source lifts的 main pair-max cores只能共享

\[
\boxed{
\log\gcd(C_{L,1},C_{L,2})
\le\delta_*S+o(S)
}
\tag{Source-lift-core-separation}
\]

的高度。

更精确地说，若保留 Gaussian orientation，则共同 oriented divisor的 norm也满足同一 bound。

## 5. 解释与边界

本文给出两点：

1. fixed `q_c` 时 `(C_L,Pi)` 只来自 fixed Gaussian integer `S_src` 的 divisors，因此只有 `10^{o(S)}` choices；
2. 不同 `q_c` lifts对应的 pair-max main cores在高度 `S` 尺度上几乎彼此分离，其 common part最多 `delta_*S+o(S)`。

这仍不产生 emptiness：长度 `10^{S+o(S)}` 的整数区间可以容纳许多彼此几乎互素的大数。因此不能从 pairwise core separation单独推出 contradiction。

但 terminal 的最后 source freedom现在可规范表示为：

\[
\boxed{
\text{一个长度 }10^{\delta_*S+o(S)}\text{ 的 source-lift index，}
\text{每个 index仅对应 }10^{o(S)}\text{ 个 Gaussian pair-max divisors。}
}
\]

任何下一步 strict-gap theorem只需再对这个 short source-lift index提供一个独立 global restriction；无需重新处理 exponential orientation choices。

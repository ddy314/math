# DD frontier: projective source / pair-max 极化

> 日期：2026-08-22
>
> 作用域：假想 corrected `6.308883...` terminal one-channel frontier，删除总高度 `o(S)` 的 denominator-normal-form exceptional core。

本文接续 `dd-frontier-source-core-projective-denominator-2026-08-22.md`。前者证明 source core `q_c` 的 main rough part完整进入 projective denominator `Z_0`。本文证明 moving pair-max core `C_L` 恰好呈相反行为：其 main prime在 stereographic numerator 与 denominator 中都是 units。

## 1. one-channel denominator pattern

terminal one-channel reduction有

\[
b_1=h v_1B_1,
\qquad
b_2=h v_2B_2,
\qquad
b_3=h v_1v_2B_3,
\]

且

\[
(B_1B_2B_3,v_1v_2)=1,
\]

\[
\log v_1=o(S),
\qquad
v_2=C_L\cdot10^{o(S)}.
\]

所以删去 `h,v_1,B_i` 与 coefficient overlaps造成的 `10^{o(S)}` exceptional core后，对任意 main

\[
p^e\Vert C_L
\]

都有 denominator valuation pattern

\[
\boxed{
v_p(b_1)=0,
\qquad
v_p(b_2)=v_p(b_3)=e.
}
\tag{1.1}
\]

因此 lcm denominator `q_lcm` 在 `p` 处也有 valuation `e`。

## 2. ghost coordinates 的 local pattern

由

\[
y_i=a_i\frac{q_{\rm lcm}}{b_i}
\]

与 reducedness `(a_i,b_i)=1`：

\[
\boxed{
v_p(y_1)\ge e,
\qquad
v_p(y_2)=v_p(y_3)=0.
}
\tag{2.1}
\]

one-channel pair-max给 oriented square depth

\[
\Pi^2\mid y_2+i y_3,
\qquad N(\Pi)=C_L.
\]

所以在 rational valuation上

\[
\boxed{v_p(y_2^2+y_3^2)\ge2e.}
\tag{2.2}
\]

sphere equation

\[
H_{\rm sph}^2=y_1^2+y_2^2+y_3^2
\]

与 `(2.1)--(2.2)` 因而给

\[
\boxed{v_p(H_{\rm sph})\ge e.}
\tag{2.3}
\]

这与已有 one-channel global statement `C_L|H_sph,y_1` 一致。

## 3. `C_L` 不进入 projective denominator

因为 `y_3` 是 `p`-unit，而 `H_sph` 被 `p` 整除：

\[
\boxed{v_p(H_{\rm sph}+y_3)=0.}
\tag{3.1}
\]

projective denominator exact formula

\[
Z_0=\frac{H_{\rm sph}+y_3}{((y_1,y_2),H_{\rm sph}+y_3)}
\]

立刻给

\[
\boxed{v_p(Z_0)=0.}
\tag{CL-Z0-unit}
\]

聚合 main core：

\[
\boxed{
\log(C_L,Z_0)=o(S).
}
\tag{3.2}
\]

这与 source theorem

\[
q_c/10^{o(S)}\mid Z_0
\]

形成鲜明极化。

## 4. `C_L` 也不进入 stereographic numerator

stereographic numerator为

\[
y_1+i y_2.
\]

其 Gaussian norm：

\[
N(y_1+i y_2)=y_1^2+y_2^2.
\]

由 `(2.1)`：

\[
y_1^2+y_2^2\equiv y_2^2\not\equiv0\pmod p.
\]

因此

\[
\boxed{v_p\bigl(N(y_1+i y_2)\bigr)=0.}
\tag{CL-stereo-num-unit}
\]

所以 `p=pi bar pi` 的两个 Gaussian orientations都不整除 `y_1+i y_2`。

最终 primitive stereographic coordinate

\[
z=\frac{y_1+i y_2}{H_{\rm sph}+y_3}
\]

在 main `C_L` support上是 Gaussian unit：

\[
\boxed{
v_\pi(z)=v_{\bar\pi}(z)=0.
}
\tag{CL-stereo-unit}
\]

## 5. terminal projective polarization theorem

综合 source-core theorem与本文：

\[
\boxed{
q_c/10^{o(S)}\mid Z_0,
\qquad
(C_L,Z_0)=10^{o(S)}.
}
\tag{Projective-polarization-1}
\]

而 main `C_L` 也不进入 stereographic numerator：

\[
\boxed{
\gcd\bigl(C_L,N(y_1+i y_2)\bigr)=10^{o(S)}.
}
\tag{Projective-polarization-2}
\]

所以 terminal 的两个大 rough core在 projective geometry中承担完全不同角色：

- `q_c` 是 projective denominator core；
- `C_L` 的 Gaussian orientation只存在于 pair-max line `y_2+i y_3`，并不会自动传播到 primitive stereographic coordinate `z`。

## 6. 方法边界

这一极化说明，单纯把 terminal pair-max orientation“接回” coefficient circle / `Z_0` 的策略不能直接产生 `C_L`-deep projective contact：main `C_L` support上 `z` 已经是 Gaussian unit。

因此任何真正作用于 `C_L` 的后续 global compatibility都必须显式保留 pair-max line `y_2+i y_3`、derivative/secondary orientation或 raw denominator/numerator reconstruction；不能只经过最低项 stereographic coordinate。

# DD frontier: source core 强制进入 projective denominator

> 日期：2026-08-22
>
> 作用域：假想满足
> \[
> n/S\to6.308883577618\ldots
> \]
> 的 corrected terminal one-channel frontier。
>
> 本文只使用 terminal sphere bridge 与 projective denominator 的 exact formula；不使用已经撤销的 discriminant-root / 5-adic mismatch 链。

## 1. terminal sphere 输入

terminal sphere bridge 给

\[
\boxed{
H_{\rm sph}-y_3=2\cdot5^T\rho_0,
\qquad \log\rho_0=o(S),
}
\tag{1.1}
\]

以及

\[
\boxed{
H_{\rm sph}+y_3=q_c^2K_+.
}
\tag{1.2}
\]

其中

\[
\log q_c=z_*S+o(S),
\qquad
z_*=0.308883577618\ldots.
\]

另一方面写

\[
g=(y_1,y_2),
\qquad y_1=gX,\quad y_2=gY,\quad (X,Y)=1,
\]

并令

\[
r_p=v_p(g),
\qquad
\omega_p=v_p(X^2+Y^2).
\]

sphere factorization 为

\[
(H_{\rm sph}-y_3)(H_{\rm sph}+y_3)
=g^2(X^2+Y^2).
\tag{1.3}
\]

最低项 projective denominator 满足 exact formula

\[
\boxed{
Z_0=\frac{H_{\rm sph}+y_3}
{(g,H_{\rm sph}+y_3)}.
}
\tag{1.4}
\]

## 2. 逐素数 lower bound

固定奇素数 `p != 5`，记

\[
e:=v_p(q_c),
\quad
t:=v_p(H_{\rm sph}-y_3)=v_p(\rho_0),
\quad	h:=v_p(H_{\rm sph}+y_3).
\]

由 `(1.2)`：

\[
\boxed{h\ge2e.}
\tag{2.1}
\]

由 `(1.3)`：

\[
\boxed{t+h=2r_p+\omega_p.}
\tag{2.2}
\]

从 `(1.4)`：

\[
 v_p(Z_0)=h-\min(r_p,h)=\max(0,h-r_p).
\tag{2.3}
\]

由 `(2.2)` 与 `omega_p>=0`：

\[
2r_p\le t+h,
\qquad
r_p\le\left\lfloor\frac{t+h}{2}\right\rfloor.
\]

因此

\[
\begin{aligned}
v_p(Z_0)
&\ge
\max\left(0,
h-\left\lfloor\frac{t+h}{2}\right\rfloor\right)\\
&=
\max\left(0,
\left\lceil\frac{h-t}{2}\right\rceil\right)\\
&\ge
\boxed{
\max\left(0,e-\left\lfloor\frac t2\right\rfloor\right).}
\end{aligned}
\tag{Source-Z0-local}
\]

特别地，若 `p` 不整除 `rho_0`，则 `t=0`，于是

\[
\boxed{v_p(Z_0)\ge v_p(q_c).}
\tag{2.4}
\]

因此 source core 的每个非 decimal、非 sphere-gap exceptional prime-power 都完整进入 projective denominator。

## 3. 全局整数形式

定义 `rho_0` 的平方根因子

\[
\boxed{
R_\rho:=\prod_{p\nmid10}p^{\lfloor v_p(\rho_0)/2\rfloor}.
}
\tag{3.1}
\]

以及 source 的 non-decimal core

\[
q_c^\circ:=\operatorname{core}_{10}(q_c).
\]

`(Source-Z0-local)` 逐 prime 相乘给

\[
\boxed{
\frac{q_c^\circ}{(q_c^\circ,R_\rho)}\mid Z_0.
}
\tag{Source-Z0-global}
\]

由于

\[
R_\rho^2\mid\rho_0,
\qquad
\log\rho_0=o(S),
\]

有

\[
\log R_\rho=o(S).
\]

corrected equality rigidity同时使 `q_c` 的 decimal-prime部分只有 `o(S)` 高度，因此

\[
\boxed{
\log\gcd(q_c,Z_0)
\ge\log q_c-o(S)
=z_*S-o(S).
}
\tag{Source-Z0-height}
\]

等价地，在 effective-core 意义下

\[
\boxed{q_c/10^{o(S)}\mid Z_0.}
\tag{Source-Z0-effective}
\]

## 4. 一个更精确的局部解释

若 `t=0`，则 `(2.2)` 给

\[
h=2r_p+\omega_p.
\]

于是 `(2.3)` 精确化为

\[
\boxed{
v_p(Z_0)=r_p+\omega_p.}
\tag{4.1}
\]

所以 source prime在 `H+y_3` 中的深度分成：

- 两份 common ghost scale `2r_p`；
- 一份 primitive angular depth `omega_p`。

projective primitive 化只删去一份 `r_p`，剩下

\[
r_p+\omega_p
\]

仍至少是 `h/2`。因此 `q_c^2|H+y_3` 自动留下至少一整份 `q_c` 于 `Z_0`。

这不是估计损失，而是 stereographic primitive denominator 的结构性行为。

## 5. 对 `q-Z` sharp payer 路线的影响

canonical `t_2=1` 已有 sharp allocation

\[
D_{qZ}^2\mid\gamma\,a\,Z_0^2,
\qquad D_{qZ}=(q,Z).
\]

在 terminal equality ray 上

\[
\log\gamma=o(S),
\]

而 sphere gap 的 non-decimal extra core也只有 `o(S)` 高度。此前一个自然设想是进一步证明 `Z_0=10^{o(S)}`，从而迫使 `(q,Z)` 很小。

`(Source-Z0-height)` 说明这条设想不可能成立：

\[
\boxed{
\log Z_0\ge z_*S-o(S)
=0.308883577618\ldots S-o(S).
}
\]

而 terminal 中

\[
\log q/S\to z_*,
\qquad
\log Z/S\to z_*.
\]

所以 `Z_0` 本身具有足够的 leading height去支付整个 `q-Z` gcd。

因此：

\[
\boxed{
\text{terminal `q-Z` sharp payer 在 projective denominator 槽上是结构性临界的。}
}
\tag{qZ-projective-critical}
\]

不能再以“把 `Z_0` 压到次指数”作为 strict-gap 策略。

## 6. 当前方法边界

本文得到的是 source/projective 的正面结构定理，同时关闭一条潜在路线：

1. `q_c` 的 main rough core自动进入 `Z_0`；
2. `Z_0` 因而至少具有 `z_*S` 级高度；
3. `D_{qZ}^2|gamma a Z_0^2` 在 terminal source scale 上可以完全临界；
4. 后续 strict-gap 不能依靠证明 projective denominator 很小。

真正仍有希望产生新信息的对象必须区分 source core `q_c` 与 moving pair-max core `C_L/Pi`，而不是继续向 `Z_0` 收费。

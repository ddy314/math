# A2 angle sign-pair 的 pure-`c_Q` unsaturated no-go

> **依赖：** `spontaneous-angle-pair-q0-depth.md`。
>
> **严格状态：**前一文件证明 pure `c_Q`-supported angle sign-pair common depth为 `min(v_p(Delta_0),2v_p(c_Q))`。本文证明不能仅靠 local `c_Q` geometry把 `v_p(Delta_0)` 强迫到完整 square depth `2v_p(c_Q)`：first-layer conic `x=-2,Delta_0=0` 对所有 genuine non-`3` inert primes均光滑，因而 unsaturated intermediate depth 是正常的 simple Hensel freedom。这个 no-go 阻止后续错误地从 `Q` 与 `b_3` 都含 `c_Q` 推出 angle pair gcd 自动 `1 mod 4`。本文不构造真实 global decimal solution，也不关闭 A2。

---

## 1. first-layer conic

对 pure `c_Q` prime `p`，前一文件给

\[
p\mid Q_0\Longrightarrow x=-2\pmod p,
\]

而 angle sign-pair common contact进一步要求

\[
\Delta_0(x,y)=2025x^2-18y-y^2=0\pmod p.
\]

所以

\[
\boxed{(y+9)^2=8181.}
\tag{1.1}
\]

其 partial derivatives 为

\[
\boxed{\partial_x\Delta_0=4050x,\qquad
\partial_y\Delta_0=-18-2y.}
\tag{1.2}
\]

在 `x=-2` 上

\[
\partial_x\Delta_0=-8100.
\]
对 genuine non-`3` inert prime `p`，`p\ne2,3,5`，故

\[
\boxed{\partial_x\Delta_0\not\equiv0\pmod p.}
\tag{1.3}
\]

同时若 `partial_y Delta_0=0`，则 `y=-9`，代入 (1.1) 会要求

\[
p\mid8181=3^4\cdot101.
\]
除 `3` 外只剩 `101=1 mod4`。因此 genuine non-`3` inert prime还满足

\[
\boxed{\partial_y\Delta_0\not\equiv0\pmod p.}
\tag{1.4}
\]

所以 pair-common conic在所有目标 inert primes上都是 smooth transverse curve。

---

## 2. why the `c_Q^2` cap does not force even depth

Write

\[
c:=v_p(c_Q)>0.
\]
For a pure `c_Q` prime, `q` is a unit and

\[
v_p(Q_0)=v_p(x+2)=c.
\]
The angle-pair depth law is

\[
\boxed{v_p(D_O)=\min\{v_p(\Delta_0),2c\}.}
\tag{2.1}
\]

One might hope that because `c_Q` occurs once in `Q` and once in `b_3`, every common pair contact automatically reaches `2c`. Equations (1.3)--(1.4) show why this is false locally.

Fix a first-layer root `(x_0,y_0)=(-2,y_0)`. Since `partial_y Delta_0` is a unit, the p-adic implicit-function theorem gives a unique smooth branch

\[
y=Y(x)
\]
with

\[
\Delta_0(x,Y(x))=0.
\]
For an actual `c_Q` displacement

\[
x=x_0+p^c\xi,
\qquad \xi\in\mathbf Z_p^\times,
\]
let `y_*:=Y(x)`. For any integer `d>=1`, perturb

\[
y=y_*+p^d\eta,
\qquad \eta\in\mathbf Z_p^\times.
\]
Taylor expansion gives

\[
\Delta_0(x,y)
=p^d\eta\,\partial_y\Delta_0(x,y_*)+O(p^{2d}).
\]
Because the derivative is a unit,

\[
\boxed{v_p(\Delta_0)=d.}
\tag{2.2}
\]

In particular every intermediate depth

\[
1\le d<2c
\]
is locally allowed. Choosing odd `d` gives an odd sign-pair common contribution through (2.1).

This is a local deformation statement only: the real decimal orbit may still fail to realize a chosen lift. But it proves that local algebra alone cannot upgrade the `2c` cap to a forced `2c` saturation.

---

## 3. consequence for global parity strategy

The pure `c_Q` part of `D_O` has the exact dichotomy:

\[
\boxed{
\begin{array}{c|c}
 v_p(\Delta_0)\ge2c & v_p(D_O)=2c\text{ (even)}\\
 v_p(\Delta_0)<2c & v_p(D_O)=v_p(\Delta_0)\text{ (simple unsaturated)}.
\end{array}}
\tag{3.1}
\]

The second row cannot be removed by another singular-discriminant audit: the underlying curve is smooth. Therefore a proof of

\[
D_O\equiv1\pmod4
\]
(if true) must use a global input such as decimal-orbit synchronization, natural representatives, or coupling to the additive/height ledger. It cannot follow merely from the square occurrence of `c_Q` in the third denominator data.

So the angle sign-pair common-gcd frontier is now exactly

\[
\boxed{\text{simple unsaturated }Q_0\text{-primary depth on }x=-2,\Delta_0=0.}
\]

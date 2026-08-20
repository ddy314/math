# A2 actual-angle / conjugate-additive cross roots避开整个 `(0,1)` decimal interval

> **依赖：** `spontaneous-sphere-roots.md`、`spontaneous-single-branch.md`、`spontaneous-sign-companion-parity.md`。
>
> **严格状态：**actual angle sheet `O_+=0` 的 sphere已 split 为两个 rational roots `z_1,z_2`，并且在真实 endpoint 中 `z_2<z_1<-4.778`。本文把 additive sign companion `Theta_+=0` 加入：它只把 actual additive root `z_Theta` 换成 `-z_Theta`，所以 cross branches是 `L(tau,-z_i)=0`。证明每支恰有一根 `<0`、另一根 `>1`，因此整个真实 decimal interval `0<tau<=10^-11` 无 root。本文仍不把 real separation提升成 modular emptiness，也不宣称 A2 closure。

---

## 1. 两条 cross quadratics

记

\[
s=9+y,
\qquad
c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.
\]

对任意 sphere root `z`，compact equation为

\[
\mathscr L(\tau,z)
=55\tau^2+18(z-s)\tau+s^2-4sz-c.
\tag{1.1}
\]

actual additive carrier `Theta_-=0` 的 normalized root记作 `z_Theta`。sign companion `Theta_+=0` 精确对应

\[
\boxed{z=-z_\Theta.}
\tag{1.2}
\]

因此若 actual angle sphere root为 `z_i`，cross condition是

\[
-z_\Theta=z_i
\iff
z_\Theta=-z_i.
\]

利用 `L(tau,z)=0 iff z_Theta=z`，得到

\[
\boxed{
\mathscr L_i^\#(\tau)
:=\mathscr L(\tau,-z_i)=0,
\qquad i=1,2.
}
\tag{1.3}
\]

展开：

\[
\boxed{
\mathscr L_i^\#
=55\tau^2-18(s+z_i)\tau+s^2+4sz_i-c.
}
\tag{1.4}
\]

每支 leading coefficient均为 `55>0`。

---

## 2. `tau=0` 时统一严格为负

真实 endpoint：

\[
\frac{249}{250}<y<1,
\qquad
9<s<10,
\]

而 `spontaneous-sphere-roots.md` 已证明

\[
\boxed{z_2<z_1<-4.778<-4.}
\tag{2.1}
\]

由于 `c>0`：

\[
\begin{aligned}
\mathscr L_i^\#(0)
&=s^2+4sz_i-c\\
&<100-16s\\
&<100-16\cdot9\\
&=-44.
\end{aligned}
\]

所以

\[
\boxed{
\mathscr L_i^\#(0)<-44<0.
}
\tag{2.2}
\]

---

## 3. `tau=1` 时也统一严格为负

写

\[
A(\tau)=55\tau^2-18s\tau+s^2-c,
\]

\[
B(\tau)=18\tau-4s.
\]

则

\[
\mathscr L_i^\#=A-Bz_i.
\]

在 `tau=1`：

\[
A(1)=y^2-26-c<-25.
\tag{3.1}
\]

同时

\[
B(1)=18-4(9+y)=-18-4y<0,
\]

而 `z_i<0`，所以

\[
B(1)z_i>0.
\]

故

\[
\boxed{
\mathscr L_i^\#(1)
=A(1)-B(1)z_i
<A(1)<-25.
}
\tag{3.2}
\]

---

## 4. 两根的位置

`L_i#` 是开口向上的实二次式。由 (2.2) 它取负值，所以 discriminant必严格为正，存在两个不同实根：

\[
r_{i,-}<r_{i,+}.
\]

开口向上的二次式只在两根之间为负。由

\[
\mathscr L_i^\#(0)<0,
\qquad
\mathscr L_i^\#(1)<0,
\]
可知 `0` 与 `1` 都位于同一负区间，因此

\[
\boxed{
r_{i,-}<0<1<r_{i,+},
\qquad i=1,2.
}
\tag{4.1}
\]

特别地整个区间

\[
\boxed{0\le\tau\le1}
\]
都不包含 root。

而真实 endpoint有

\[
0<\tau_{actual}=10^{-M}\le10^{-11}<1.
\]

所以

\[
\boxed{
\mathscr L_i^\#(10^{-M})\ne0
\quad\text{over }\mathbf R,
\qquad i=1,2.
}
\tag{4.2}
\]

---

## 5. 四 sign combinations 的 Archimedean 状态

结合已有文件：

- `O_+ / Theta_-`（actual/actual）：pure-spontaneous real roots全部 `>1`；
- `O_+ / Theta_+`（actual/conjugate）：本文证明两根分别 `<0` 与 `>1`；
- `O_- / Theta_-`（conjugate/actual）：`spontaneous-cross-sign-biquadratic.md` 的 norm在整个实轴严格正，无 real root；
- `O_- / Theta_+` 可由同一 conjugate-angle quadratic extension处理；其 real third-numerator sphere本身已经不存在，因此同样没有真实 endpoint mechanism。

因此四个 sign carriers产生的 residual parity都没有 Archimedean near-root解释。剩余问题纯粹是 modular / decimal multiplicative orbit / natural representative。

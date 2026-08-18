# A2 conjugate-angle cross-sign branch as a quadratic norm with no real `tau` root

> **依赖：** `spontaneous-cross-sign-sphere.md`、`spontaneous-cross-sign-height-shadow.md`、`spontaneous-single-branch.md`。
>
> **严格状态：**`spontaneous-cross-sign-sphere.md` 已证明 conjugate angle sheet `O_-=0` 的 exact sphere引入唯一 quadratic coordinate `v^2=-2X_cross`，且 `X_cross>56` 在真实 endpoint 上严格成立。本文把 sphere 的两个 third-numerator roots显式写成 `z_±=Z_c±Z_vv`，再把 additive root条件写成两个 conjugate compact quadratics。其 quadratic norm在整个真实 `tau` 轴上严格为正，因此 cross-sign common branch没有任何 real decimal root；所有 surviving contact只能来自 genuine finite-field / p-adic wrapping。本文不把实轴空性误写成模素数空性，也不宣称 A2 closure。

---

## 1. normalized sphere

沿用

\[
x=\frac{b_2}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}},
\qquad
\tau=10^{-M},
\qquad
s:=9+y.
\]

定义

\[
n:=\frac{2025x^2+y^2}{100},
\qquad
c:=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.
\tag{1.1}
\]

第三块 normalized coordinates：

\[
\bar w=\frac{b_3}{T10^M},
\qquad
\bar\zeta=\frac{a_3}{T10^M}.
\]

exact sphere：

\[
\boxed{
\mathscr S(\bar w,\bar\zeta)
=x^2\bar w^2(s+\bar\zeta)^2
-(x+2+\bar w)^2
\left(n\bar w^2+x^2\bar\zeta^2\right).
}
\tag{1.2}
\]

令

\[
d:=225x^2-y,
\]

\[
A_{\rm sp}:=4d^2-xy^2(99x-4),
\]

\[
\boxed{
W:=\frac{A_{\rm sp}}{2y^2(x+2)}.
}
\tag{1.3}
\]

conjugate angle carrier `O_-=0` 对应

\[
\boxed{\bar w=W.}
\tag{1.4}
\]

---

## 2. `bar zeta` quadratic 的 center 与 quadratic coordinate

继续定义

\[
\boxed{
H:=202500x^4-99x^2y^2-1800x^2y+4xy^2+4y^2,
}
\tag{2.1}
\]

\[
\boxed{
H^\vee:=H+2y^2(x+2)^2,
}
\tag{2.2}
\]

\[
\boxed{
D_z:=101250x^4-49x^2y^2-900x^2y+4xy^2+4y^2.
}
\tag{2.3}
\]

`spontaneous-cross-sign-sphere.md` 的 cross polynomial为

\[
\boxed{
\begin{aligned}
X_\times={}&205031250x^6+2025x^4y^2-1822500x^4y\\
&+8100x^3y^2-99x^2y^4-1800x^2y^3\\
&+4050x^2y^2+4xy^4+4y^4.
\end{aligned}}
\tag{2.4}
\]

并定义 quadratic coordinate

\[
\boxed{v^2=-2X_\times.}
\tag{2.5}
\]

把 `bar w=W` 代入 sphere，视为 `bar zeta` 的二次式，其 leading coefficient精确为

\[
\boxed{
[\bar\zeta^2]\,\mathscr S(W,\bar\zeta)
=-\frac{2x^2D_z}{y^2}.
}
\tag{2.6}
\]

quadratic center为

\[
\boxed{
Z_c
:=\frac{sH^2}
{8y^2(x+2)^2D_z}.
}
\tag{2.7}
\]

定义

\[
\boxed{
Z_v
:=\frac{HH^\vee}
{80xy^3(x+2)^2D_z}.
}
\tag{2.8}
\]

由 discriminant factorization

\[
\operatorname{Disc}_{\bar\zeta}
=-\frac{x^2H^2(H^\vee)^2X_\times}
{200y^{10}(x+2)^4}
\]
与 (2.5)，quadratic formula给两根（交换 `+/-` 只改变标签）：

\[
\boxed{
Z_\pm=Z_c\pm Z_vv.
}
\tag{2.9}
\]

checker还直接在 quotient ring

\[
\mathbf Q(x,y)[v]/(v^2+2X_\times)
\]
验证

\[
\boxed{
\mathscr S(W,Z_c+Z_vv)=0.
}
\tag{2.10}
\]

所以 conjugate-angle sphere不是黑箱 quartic；它只有一个 quadratic coordinate `v`。

---

## 3. endpoint 中所有 root formula denominator 都是正 unit

当前 closed endpoint rectangle为

\[
\frac1{10}\le x\le\frac2{19},
\qquad
\frac{249}{250}\le y\le1.
\tag{3.1}
\]

### 3.1 `H>0`

对 `H`：

\[
\partial_xH
=810000x^3-198xy^2-3600xy+4y^2.
\]

在 (3.1) 上粗略估计

\[
\partial_xH
>810
-\frac{396}{19}
-\frac{7200}{19}>0.
\tag{3.2}
\]

另一方面

\[
\partial_yH
=-198x^2y-1800x^2+8xy+8y.
\]

舍去第一负项并用 `x>=1/10`：

\[
\partial_yH
<-18+8\frac2{19}+8<0.
\tag{3.3}
\]

所以 `H` 对 `x` 增、对 `y` 减，最小值在 `(1/10,1)`：

\[
\boxed{
H\ge H(1/10,1)=\frac{283}{50}>0.
}
\tag{3.4}
\]

由定义：

\[
\boxed{H^\vee>H>0.}
\tag{3.5}
\]

### 3.2 `D_z>0`

同理

\[
\partial_xD_z
=405000x^3-98xy^2-1800xy+4y^2
\]
满足

\[
\partial_xD_z
>405-rac{196}{19}-\frac{3600}{19}>0.
\tag{3.6}
\]

而

\[
\partial_yD_z
=-98x^2y-900x^2+8xy+8y
\]
满足

\[
\partial_yD_z
<-9+8\frac2{19}+8<0.
\tag{3.7}
\]

故

\[
\boxed{
D_z\ge D_z(1/10,1)=\frac{1007}{200}>0.
}
\tag{3.8}
\]

因此 (2.7)–(2.9) 在整个真实 endpoint上没有 pole。

此外已有

\[
\boxed{X_\times>56>0.}
\tag{3.9}
\]

---

## 4. compact additive branch在 quadratic extension中的两张 sheets

`spontaneous-single-branch.md` 的 universal compact equation对任意 fixed sphere root `z` 为

\[
\boxed{
\mathscr L(\tau,z)
=55\tau^2+18(z-s)\tau+s^2-4sz-c.
}
\tag{4.1}
\]

令

\[
\boxed{
A(\tau)
:=55\tau^2-18s\tau+s^2-c,
}
\tag{4.2}
\]

\[
\boxed{
B(\tau):=18\tau-4s=2(9\tau-2s).
}
\tag{4.3}
\]

则

\[
\mathscr L(\tau,z)=A(\tau)+B(\tau)z.
\]

代入 (2.9)：

\[
\boxed{
\mathscr L_\pm^\times(\tau)
=A+B Z_c\pm BZ_vv.
}
\tag{4.4}
\]

这正是 conjugate-angle 与 additive actual root的两个 cross-sign branches。

因此其 pure-prefix elimination只是 quadratic norm：

\[
\boxed{
\begin{aligned}
\mathcal N_\times(\tau)
&:=\mathscr L_+^\times(\tau)
\mathscr L_-^\times(\tau)\\
&=(A+B Z_c)^2+2X_\times B^2Z_v^2.
\end{aligned}}
\tag{4.5}
\]

这里使用 `v^2=-2X_cross`。

所以任何清分母后出现的 degree-4 `tau` polynomial都只是 (4.5) 的 quadratic norm，而不是新的独立 quartic obstruction。

---

## 5. 无分母整数 norm

为了避免在 `D_z` 上作不必要的 rational bookkeeping，定义公共正 denominator

\[
\boxed{
\mathscr D
:=200x^2y^3(x+2)^2D_z>0.
}
\tag{5.1}
\]

再定义

\[
\boxed{
A_0
:=100x^2(55\tau^2-18s\tau+s^2)
-(x+2)^2(2025x^2+y^2),
}
\tag{5.2}
\]

于是 `A=A_0/(100x^2)`。

定义

\[
\boxed{
U_\times
:=2y^3(x+2)^2D_zA_0
+25x^2ysH^2B,
}
\tag{5.3}
\]

以及

\[
\boxed{
V_\times
:=5xBHH^\vee.
}
\tag{5.4}
\]

直接清分母：

\[
\boxed{
\mathscr D(A+BZ_c)=U_\times,
\qquad
\mathscr D(BZ_v)=V_\times.
}
\tag{5.5}
\]

因此定义 polynomial norm

\[
\boxed{
\mathfrak N_\times
:=U_\times^2+2X_\times V_\times^2.
}
\tag{5.6}
\]

有 exact identity

\[
\boxed{
\mathfrak N_\times
=\mathscr D^2\mathcal N_\times.
}
\tag{5.7}
\]

所以实际 modular work可以直接使用 `N_frak`；不必引入 rational root coordinates。

---

## 6. `已严格完成`：cross-sign norm在整个实 `tau` 轴严格为正

由 (3.9)：

\[
X_\times>0.
\]

所以 (4.5) 是两个非负实数项之和：

\[
\mathcal N_\times
=(A+BZ_c)^2+2X_\times B^2Z_v^2
\ge0.
\tag{6.1}
\]

若等号成立，则因为 `X_cross,Z_v` 在 endpoint均非零，必须

\[
B(\tau)=0.
\]

于是

\[
\boxed{
\tau=\frac{2s}{9}.
}
\tag{6.2}
\]

此时

\[
\begin{aligned}
A\left(\frac{2s}{9}\right)
&=55\frac{4s^2}{81}
-18s\frac{2s}{9}
+s^2-c\\
&=-\frac{23}{81}s^2-c.
\end{aligned}
\]

故

\[
\boxed{
A(2s/9)<0.
}
\tag{6.3}
\]

而 `B=0` 时

\[
A+BZ_c=A\ne0.
\]

与等号条件矛盾。因此：

\[
\boxed{
\mathcal N_\times(\tau)>0
\qquad\forall\tau\in\mathbf R.
}
\tag{6.4}
\]

等价地，由 `D>0`：

\[
\boxed{
\mathfrak N_\times(\tau)>0
\qquad\forall\tau\in\mathbf R.
}
\tag{6.5}
\]

这比“真实 decimal phase不靠近 root”更强：cross-sign norm在实轴根本没有 root。

---

## 7. 对 global parity 的意义

现在四种主要 simple external geometry具有如下 real 状态：

1. actual pure-spontaneous sheets：所有 real `tau` roots严格 `>1`；
2. additive height companion `J_H`：所有 real `tau` roots严格 `>1`；
3. omega-content biquadratic branch：两张 real `y` roots都避开真实 numerator window；
4. conjugate-angle cross-sign branch：quadratic norm `N_cross` 在整个 real `tau` 轴严格正，因此无任何 real root。

所以 `spontaneous-residual-parity-doubling.md` / `spontaneous-sign-companion-parity.md` 强迫出来的多份 residual inert parity都不能由 Archimedean near-root解释。

剩余机制已经纯化为：

\[
\boxed{
\text{simple finite-field roots}
+\text{decimal multiplicative orbit}
+\text{prime-power / natural representative synchronization}.
}
\]

本文仍没有把 real-root emptiness提升为 modular emptiness。下一步若继续 cross-sign sector，应研究 (5.6) 的 singular bad reduction或它与 `tau=10^{-M}` multiplicative subgroup的统一 interaction，而不是再做实根分析。

# A2 conjugate-angle cross-sign branch as a quadratic norm with no real `tau` root

> **依赖：** `spontaneous-cross-sign-sphere.md`、`spontaneous-cross-sign-height-shadow.md`、`spontaneous-single-branch.md`。
>
> **严格状态：**conjugate angle sheet `O_-=0` 的 exact sphere只有一个 quadratic coordinate `v^2=-2X_cross`。本文显式写出两条 third-numerator orientations，并证明与 additive root相交得到的 quadratic norm在整个实 `tau` 轴上严格为正。因此 cross-sign common sector不存在任何 real decimal root；剩余接触只能来自真正的 finite-field / p-adic wrapping。本文不把实轴空性提升成 modular 空性，也不宣称 A2 closure。

---

## 1. normalized sphere

记

\[
x=\frac{b_2}{10^M},\qquad
y=\frac{a_2}{10^{M-1}},\qquad
\tau=10^{-M},\qquad s=9+y,
\]

\[
n=\frac{2025x^2+y^2}{100},\qquad
c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.
\]

exact sphere 为

\[
\mathscr S(w,z)
=x^2w^2(s+z)^2-(x+2+w)^2(nw^2+x^2z^2).
\tag{1.1}
\]

令

\[
d=225x^2-y,\qquad
A_{\rm sp}=4d^2-xy^2(99x-4),
\]

\[
W=\frac{A_{\rm sp}}{2y^2(x+2)}.
\tag{1.2}
\]

`O_-=0` 对应 conjugate angle root

\[
\boxed{w=W.}
\tag{1.3}
\]

---

## 2. sphere 的两个 quadratic orientations

定义

\[
H=202500x^4-99x^2y^2-1800x^2y+4xy^2+4y^2,
\tag{2.1}
\]

\[
H^\vee=H+2y^2(x+2)^2,
\tag{2.2}
\]

\[
D_z=101250x^4-49x^2y^2-900x^2y+4xy^2+4y^2,
\tag{2.3}
\]

以及

\[
\begin{aligned}
X_\times={}&205031250x^6+2025x^4y^2-1822500x^4y\\
&+8100x^3y^2-99x^2y^4-1800x^2y^3\\
&+4050x^2y^2+4xy^4+4y^4.
\end{aligned}
\tag{2.4}
\]

`spontaneous-cross-sign-sphere.md` 已给

\[
\operatorname{Disc}_{z}\mathscr S(W,z)
=-\frac{x^2H^2(H^\vee)^2X_\times}
{200y^{10}(x+2)^4}.
\tag{2.5}
\]

定义 quadratic coordinate

\[
\boxed{v^2=-2X_\times.}
\tag{2.6}
\]

把 `S(W,z)` 看成 `z` 的二次式，其 leading coefficient为

\[
[z^2]\mathscr S(W,z)=-\frac{2x^2D_z}{y^2},
\tag{2.7}
\]

center 为

\[
\boxed{
Z_c=\frac{sH^2}{8y^2(x+2)^2D_z}.
}
\tag{2.8}
\]

再令

\[
\boxed{
Z_v=\frac{HH^\vee}{80xy^3(x+2)^2D_z}.
}
\tag{2.9}
\]

quadratic formula因此给两根（正负号只决定标签）：

\[
\boxed{Z_\pm=Z_c\pm Z_vv.}
\tag{2.10}
\]

checker直接在

\[
\mathbf Q(x,y)[v]/(v^2+2X_\times)
\]
中验证

\[
\mathscr S(W,Z_c+Z_vv)=0.
\tag{2.11}
\]

---

## 3. endpoint 中 root formula 没有 pole

使用闭 endpoint box

\[
\frac1{10}\le x\le\frac2{19},\qquad
\frac{249}{250}\le y\le1.
\tag{3.1}
\]

对 `H`：

\[
\partial_xH
=810000x^3-198xy^2-3600xy+4y^2
>810-\frac{396}{19}-\frac{7200}{19}>0,
\]

\[
\partial_yH
=-198x^2y-1800x^2+8xy+8y
<-18+\frac{16}{19}+8<0.
\]

因此

\[
\boxed{H\ge H(1/10,1)=\frac{283}{50}>0.}
\tag{3.2}
\]

从而

\[
\boxed{H^\vee>H>0.}
\tag{3.3}
\]

同理：

\[
\partial_xD_z
>405-\frac{196}{19}-\frac{3600}{19}>0,
\]

\[
\partial_yD_z
<-9+\frac{16}{19}+8<0,
\]

故

\[
\boxed{D_z\ge D_z(1/10,1)=\frac{1007}{200}>0.}
\tag{3.4}
\]

已有 exact endpoint estimate

\[
\boxed{X_\times>56>0.}
\tag{3.5}
\]

所以 (2.8)–(2.10) 的 denominator 在整个真实 endpoint上均为正。

---

## 4. additive compact branches

对任意 fixed sphere root `z`，universal compact equation为

\[
\mathscr L(\tau,z)
=55\tau^2+18(z-s)\tau+s^2-4sz-c.
\tag{4.1}
\]

写成

\[
\boxed{\mathscr L(\tau,z)=A(\tau)+B(\tau)z,}
\tag{4.2}
\]

其中

\[
A(\tau)=55\tau^2-18s\tau+s^2-c,
\tag{4.3}
\]

\[
B(\tau)=18\tau-4s=2(9\tau-2s).
\tag{4.4}
\]

代入 (2.10)：

\[
\boxed{
\mathscr L_\pm^\times
=A+BZ_c\pm BZ_vv.
}
\tag{4.5}
\]

因此两支的 quadratic norm 是

\[
\boxed{
\begin{aligned}
\mathcal N_\times(\tau)
&=\mathscr L_+^\times\mathscr L_-^\times\\
&=(A+BZ_c)^2+2X_\times B^2Z_v^2.
\end{aligned}}
\tag{4.6}
\]

任何清分母后出现的 quartic `tau` eliminant都只是这个 quadratic norm，不是新的独立 quartic obstruction。

---

## 5. exact polynomial norm

定义公共正 denominator

\[
\boxed{
\mathscr D=200x^2y^3(x+2)^2D_z.
}
\tag{5.1}
\]

以及

\[
A_0
=100x^2(55\tau^2-18s\tau+s^2)
-(x+2)^2(2025x^2+y^2),
\tag{5.2}
\]

故 `A=A_0/(100x^2)`。

定义

\[
\boxed{
U_\times
=2y^3(x+2)^2D_zA_0+25x^2ysH^2B,
}
\tag{5.3}
\]

和（注意 `B=2(9tau-2s)`）

\[
\boxed{
V_\times
=5x(9\tau-2s)HH^\vee.
}
\tag{5.4}
\]

则 exact clearing identities 是

\[
\boxed{
\mathscr D(A+BZ_c)=U_\times,
\qquad
\mathscr D(BZ_v)=V_\times.
}
\tag{5.5}
\]

因此定义

\[
\boxed{
\mathfrak N_\times
=U_\times^2+2X_\times V_\times^2,
}
\tag{5.6}
\]

有

\[
\boxed{
\mathfrak N_\times
=\mathscr D^2\mathcal N_\times.
}
\tag{5.7}
\]

这给 modular work 一个完全 polynomial 的自然代表。

---

## 6. `已严格完成`：整个实 `tau` 轴无根

由 `X_cross>0`，(4.6) 是两个非负项之和：

\[
\mathcal N_\times
=(A+BZ_c)^2+2X_\times B^2Z_v^2\ge0.
\]

因为 endpoint 中 `Z_v!=0`，若等号成立，必须

\[
B(\tau)=0,
\]
即

\[
\boxed{\tau=\frac{2s}{9}.}
\tag{6.1}
\]

但此时

\[
\begin{aligned}
A(2s/9)
&=55\frac{4s^2}{81}-18s\frac{2s}{9}+s^2-c\\
&=-\frac{23}{81}s^2-c<0.
\end{aligned}
\tag{6.2}
\]

所以 `A+BZ_c=A!=0`，矛盾。故

\[
\boxed{
\mathcal N_\times(\tau)>0
\quad\text{for every }\tau\in\mathbf R.
}
\tag{6.3}
\]

由于 `D>0`，亦有

\[
\boxed{
\mathfrak N_\times(\tau)>0
\quad\text{for every }\tau\in\mathbf R.
}
\tag{6.4}
\]

这比“actual decimal phase离 roots 很远”更强：cross-sign common norm在整个实轴根本没有 root。

---

## 7. frontier

现在几类主要 external simple geometry的 Archimedean 状态已统一：

- actual pure-spontaneous branches：所有 real `tau` roots `>1`；
- additive height companion `J_H`：所有 real `tau` roots `>1`；
- omega-content branch：两张 real numerator roots避开真实 `y` window；
- conjugate-angle cross-sign branch：`N_cross(tau)>0` 对所有 real `tau`。

所以 global parity ledger留下的 residual primes都只能靠 genuine modular wrapping / decimal multiplicative orbit产生，而不能解释为 real near-root。

本文仍未把这一点提升为 modular emptiness。下一步最值得做的是审计 polynomial norm `N_frak` 的 singular bad reduction，或寻找它与 `tau=10^{-M}` multiplicative subgroup之间的统一 natural-representative约束。

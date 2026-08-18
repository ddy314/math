# A2 pure-spontaneous branch 的全部实 `tau` roots 都大于 `1`

> **依赖：** `spontaneous-sphere-roots.md`、`spontaneous-single-branch.md`。
>
> **严格状态：**`spontaneous-single-branch.md` 只证明了每支 repeated critical point `tau_i^*>12/5`，并未排除较小 simple real root靠近 `tau=0`。本文补上这一缺口：利用 `Theta` third-numerator root 与第一 sphere root在 `tau=1` 的 exact gap，证明两支 quadratic `L_i` 在 `tau=1` 仍严格为正。结合 vertex `>12/5` 与 positive discriminant，得到两支的两个 real roots全部严格 `>1`。因此真实 decimal phase `tau<=10^-11` 与所有 pure-spontaneous real roots有统一巨大间隔；剩余 common contact只能来自 genuine p-adic wrapping。本文不把 Archimedean separation误写成 modular空性，A2 仍 open。

---

## 1. compact branch quadratic

沿用

\[
\tau=10^{-M},
\qquad
s:=9+y,
\]

以及两个 rational sphere roots

\[
z_i:=\bar\zeta_i,
\qquad i=1,2.
\]

记

\[
\boxed{
c(x,y)
:=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.}
\tag{1.1}

`spontaneous-single-branch.md` 已证明每支长度方程是

\[
\boxed{
\mathscr L_i(\tau)
=55\tau^2+18(z_i-s)\tau+s^2-4sz_i-c.
}
\tag{1.2}

其 vertex 为

\[
\boxed{
\tau_i^*=\frac{9(s-z_i)}{55}
>\frac{12}{5}.
}
\tag{1.3}

并且 discriminant

\[
\mathscr D_i>0
\]
在真实 endpoint上严格成立。因此每支有两个不同 real roots。

本文只需证明

\[
\boxed{\mathscr L_i(1)>0.}
\tag{1.4}

---

## 2. `L_i` 就是 Theta root 与 sphere root 的有符号距离

`Theta_dec=0` 的 normalized third-numerator root为

\[
\boxed{
\bar\zeta_\Theta(\tau)
=
\frac{
 x^2(s^2-18s\tau+55\tau^2)
 -\frac1{100}(x+2)^2(2025x^2+y^2)
}
{2x^2(2s-9\tau)}.
}
\tag{2.1}

从定义直接展开：

\[
\boxed{
\mathscr L_i(\tau)
=2(2s-9\tau)
\bigl(\bar\zeta_\Theta(\tau)-z_i\bigr).
}
\tag{2.2}

在 `tau=1`：

\[
2s-9=2y+9>0.
\]
所以

\[
\boxed{
\mathscr L_i(1)>0
\iff
\bar\zeta_\Theta(1)>z_i.
}
\tag{2.3}

已有 `spontaneous-sphere-roots.md` 的 strict ordering

\[
\boxed{z_2<z_1.}
\tag{2.4}

因此只需证明

\[
\boxed{\bar\zeta_\Theta(1)>z_1.}
\tag{2.5}

---

## 3. 定义关键 gap

endpoint rectangle为

\[
\boxed{
\frac1{10}\le x\le\frac2{19},
\qquad
\frac{249}{250}\le y\le1.
}
\tag{3.1}

实际 endpoint使用开区间；为了单调性证书方便，这里在闭包上证明更强结论。

定义

\[
\boxed{
G(x,y)
:=\bar\zeta_\Theta(1)-z_1(x,y).
}
\tag{3.2}

这里

\[
\bar\zeta_\Theta(1)
=
\frac{
 x^2(y^2-26)
 -\frac1{100}(x+2)^2(2025x^2+y^2)
}
{2x^2(2y+9)},
\tag{3.3}

因为

\[
s^2-18s+55=y^2-26.
\]

第一 sphere root为

\[
\boxed{
 z_1
=-\frac{A_+A_{sp}}
{400x^2y^3(x+2)^2},
}
\tag{3.4}

其中

\[
A_+
=202500x^4+99x^2y^2-4xy^2-4y^2,
\]

\[
A_{sp}
=4(225x^2-y)^2-xy^2(99x-4).
\]

所有 denominator在 (3.1) 上严格为正。

---

## 4. `有限 exact 证书`：`G` 对 `x` 增、对 `y` 减

直接求导并清去正 denominator。记

\[
\partial_xG
=\frac{P_x(x,y)}
{100x^3y^3(x+2)^3(2y+9)},
\tag{4.1}

\[
\partial_yG
=\frac{P_y(x,y)}
{400x^2y^4(x+2)^2(2y+9)^2}.
\tag{4.2}

本文不把 `P_x,P_y` 的几十项展开塞进正文；checker使用 exact rational Bernstein basis对整个 rectangle (3.1) 做符号证书。

映射

\[
x=\frac1{10}
+u\left(\frac2{19}-\frac1{10}\right),
\]

\[
y=\frac{249}{250}
+v\left(1-\frac{249}{250}\right),
\qquad
0\le u,v\le1.
\]

对 `P_x` 的 bidegree `(9,5)` Bernstein coefficients全部严格正；最小系数为

\[
\boxed{
\frac{2307239659}{400000}>0.
}
\tag{4.3}

对 `-P_y` 的 bidegree `(8,6)` Bernstein coefficients也全部严格正；最小系数为

\[
\boxed{
\frac{121236551}{2000}>0.
}
\tag{4.4}

因此在整个闭 rectangle 上：

\[
\boxed{
\partial_xG>0,
\qquad
\partial_yG<0.
}
\tag{4.5}

所以 `G` 的全局最小值位于

\[
\boxed{
x=\frac1{10},\qquad y=1.}
\tag{4.6}

---

## 5. exact 最小 gap

直接代入 (4.6)：

\[
\boxed{
G\left(\frac1{10},1\right)
=\frac{28283}{3880800}>0.
}
\tag{5.1}

因此整个 endpoint box都有

\[
\boxed{
\bar\zeta_\Theta(1)-z_1
\ge
\frac{28283}{3880800}>0.
}
\tag{5.2}

再用 `z_2<z_1`：

\[
\boxed{
\bar\zeta_\Theta(1)>z_1>z_2.
}
\tag{5.3}

由 (2.2)：

\[
\boxed{
\mathscr L_1(1)>0,
\qquad
\mathscr L_2(1)>0.
}
\tag{5.4}

事实上第一支最坏边界的 exact function value为

\[
\boxed{
\mathscr L_1(1)
=\frac{28283}{176400}>0
}
\]
在 `(x,y)=(1/10,1)` 达到该最小-gap配置。

---

## 6. 两个 real roots 全部大于 `1`

每个 `L_i` 是开口向上的二次式，且：

\[
\mathscr D_i>0,
\]
所以有两个不同 real roots，记

\[
\tau_{i,-}<\tau_i^*<\tau_{i,+}.
\]

又由 (1.3)：

\[
\tau_i^*>\frac{12}{5}>1.
\]

故 `tau=1` 位于 vertex 左侧。

若较小 root满足

\[
\tau_{i,-}\le1,
\]
则 `tau=1` 位于两 roots之间或恰在 root上，从而必有

\[
\mathscr L_i(1)\le0,
\]
与 (5.4) 矛盾。

因此

\[
\boxed{
1<\tau_{i,-}<\tau_i^*<\tau_{i,+}
\qquad(i=1,2).
}
\tag{6.1}

这是对**全部 simple real roots**的统一位置定理，而不只是 repeated critical point。

---

## 7. 与真实 decimal phase 的统一 gap

当前无界 endpoint有

\[
M\ge11,
\]
所以

\[
\boxed{0<\tau=10^{-M}\le10^{-11}.}
\tag{7.1}

结合 (6.1)：

\[
\boxed{
\tau_{i,\pm}-10^{-M}
>1-10^{-11}
\qquad(i=1,2).
}
\tag{7.2}

所以 alpha-free pure spontaneous 的所有实 branch roots都与真实 decimal orbit相差接近一个完整单位；不存在任何 Archimedean near-root mechanism。

---

## 8. 严格边界

本文**没有**从 (7.2) 推出模 `p` 空性。一个很大的 `p`-adic root仍可在实数轴上离 actual phase很远。

严格新结论是：

\[
\boxed{
\text{pure spontaneous branch 的所有 real roots都 } >1,
\quad
\tau_{actual}\le10^{-11}.
}
\]

因此：

- repeated-root real criticality 已彻底排除；
- simple-root real approximation也彻底排除；
- 剩余 common carrier只能通过 genuine p-adic wrapping / decimal multiplicative orbit产生。

后续若继续 alpha-free sector，应直接研究 prime-power orbit / natural representative；继续做 real-root或普通 discriminant character已不会增加约束。

A2 仍保持 open。
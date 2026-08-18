# A2 additive height companion `J_H` 的全部实 decimal roots都大于 `1`

> **依赖：** `spontaneous-height-parity-ledger.md`、`spontaneous-residual-parity-doubling.md`。
>
> **严格状态：**`J_H` 已知是 positive primitive `3 mod 4` integer，并通过 exact identity与 `widehat(T)_2` 共享相同 height part。本文进一步证明：把 `J_H=0` 看成 decimal phase `tau=10^{-M}` 的二次方程时，它若有实根，则两个实根全部严格大于 `1`；真实 endpoint `tau<=10^-11` 与它们有统一巨大距离。因此 `J_H` residual只能通过 genuine p-adic / multiplicative-decimal wrapping出现。本文不把实根分离误写成模素数空性，也不宣称 A2 closure。

---

## 1. normalized quadratic

沿用

\[
x=\frac{b_2}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}},
\qquad
\tau=10^{-M},
\]

并记

\[
s:=9+y.
\]

`spontaneous-height-parity-ledger.md` 的 pure-decimal additive-height carrier

\[
\mathcal J_H
=B^2(5K^2-36K+55)-Q^2N_0
\]
满足

\[
\boxed{
\frac{100\mathcal J_H}{10^{4M}}
=G_H(x,y,\tau),
}
\tag{1.1}
\]

其中

\[
\boxed{
G_H
=100x^2\left(5s^2-36s\tau+55\tau^2\right)
-(x+2)^2(2025x^2+y^2).
}
\tag{1.2}
\]

对固定 `(x,y)`，这是关于 `tau` 的开口向上二次式。

当前 endpoint box 为

\[
\boxed{
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1.
}
\tag{1.3}
\]

---

## 2. vertex 统一位于 `3.27` 之后

(1.2) 关于 `tau` 的 derivative 为

\[
\partial_\tau G_H
=100x^2(-36s+110\tau).
\]

所以 vertex 为

\[
\boxed{
\tau_H^*=\frac{18s}{55}
=\frac{18(y+9)}{55}.
}
\tag{2.1}
\]

由 `y>249/250`：

\[
\tau_H^*
>\frac{18}{55}\left(9+\frac{249}{250}\right)
=\frac{44982}{13750}
>3.
\tag{2.2}
\]

特别地

\[
\boxed{\tau_H^*>1.}
\tag{2.3}
\]

---

## 3. `tau=1` 时仍严格为正

代入 `tau=1`：

\[
5s^2-36s+55
=5y^2+54y+136.
\]

所以

\[
\boxed{
G_H(x,y,1)
=100x^2(5y^2+54y+136)
-(x+2)^2(2025x^2+y^2).
}
\tag{3.1}
\]

第一项用 box 下端粗界：

\[
100x^2(5y^2+54y+136)
>
5\left(\frac{249}{250}\right)^2
+54\frac{249}{250}+136.
\]

右端为

\[
\frac{12172701}{62500}>194.
\tag{3.2}
\]

第二项用 box 上端粗界：

\[
(x+2)^2(2025x^2+y^2)
<
\left(2+\frac2{19}\right)^2
\left(2025\left(\frac2{19}\right)^2+1\right).
\]

右端精确为

\[
\frac{1494400}{14440}<104.
\tag{3.3}
\]

因此

\[
\boxed{
G_H(x,y,1)>90>0.
}
\tag{3.4}
\]

这里故意使用很松的整数余量；无需做 endpoint 单调性或 Bernstein 审计。

---

## 4. 所有 real roots 都大于 `1`

若 `G_H` 的 discriminant <0，则没有 real root，结论自动成立。

现在假设 discriminant >=0，并记 real roots

\[
\tau_-\le\tau_+.
\]

因为开口向上，vertex 是两根中点：

\[
\tau_-\le\tau_H^*\le\tau_+.
\]

由 (2.3)，`tau_H^*>1`。

若

\[
\tau_-\le1,
\]
则 `tau_+>=tau_H^*>1`，所以 `tau=1` 位于两 roots 之间或恰在左 root上，从而必须有

\[
G_H(1)\le0,
\]
与 (3.4) 矛盾。

故

\[
\boxed{
1<\tau_-\le\tau_H^*\le\tau_+.
}
\tag{4.1}
\]

若 discriminant=0，则唯一 double root就是 `tau_H^*>3`，同样满足结论。

因此统一得到：

\[
\boxed{
J_H=0\text{ 的所有实 decimal roots 都严格大于 }1.
}
\tag{4.2}
\]

---

## 5. 与真实 decimal orbit 的距离

无界 endpoint 中

\[
M\ge11,
\]
故

\[
0<\tau_{actual}=10^{-M}\le10^{-11}.
\]

所以任意 real root `tau_r` 都满足

\[
\boxed{
\tau_r-\tau_{actual}>1-10^{-11}.
}
\tag{5.1}
\]

因此 `J_H` 的 real geometry不会产生 near-root；任何 prime divisibility / Hensel lift都必须来自真正的 modular wrapping。

---

## 6. 与 global parity ledger 的关系

现在三类关键 simple residual 都有同一 Archimedean 状态：

1. `spontaneous-pure-root-gap.md`：pure spontaneous `L_1,L_2` 的全部 real roots `>1`；
2. 本文：additive height companion `J_H` 的全部 real roots `>1`；
3. `spontaneous-omega-content-biquadratic.md`：omega-content 两个 real numerator roots避开真实 `y` window。

所以 `spontaneous-residual-parity-doubling.md` 强迫出来的 companion inert parity不能解释为真实根靠近 endpoint；只剩 decimal multiplicative orbit / natural representative。

这仍不是模 `p` 空性。后续若要关闭 residual parity，必须真正控制 `10^{-M}` 在这些 simple algebraic branches上的 prime-power orbit或 modulus-vs-height，而不是继续重复 real-root分析。

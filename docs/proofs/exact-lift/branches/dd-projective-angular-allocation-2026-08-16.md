# DD projective angular allocation — 2026-08-16

> 本文接续 [`double-deficit.md`](double-deficit.md) §§56--61，对一般 DD 的 projective denominator / 5-adic allocation 做进一步精确化。
> 本文结论不要求进入 `6.308883...` frontier；它们是在原 §57--61 假设和符号下的严格局部算术结论。
>
> **状态边界：**本文关闭的是“5-adic angular depth 可以再次支付 projective denominator / 两条 carrier contact”的重复支付通道；它本身还不是 DD 全局空性。

---

## 1. 基线

沿用 overlap 参数化

\[
Q=\eta Q_1,
\qquad
\tau=\eta v,
\qquad
(LQ_1,v)=1,
\qquad
(L,\eta)=1.
\]

无 \(E_D\) eliminant 为

\[
\Xi
=(LQ+\tau)^2(LQ+2\tau)^2
(10^{2k}+10^{2d}).
\tag{1.1}
\]

若两个独立 carrier residual 同时满足

\[
5^h\mid\mathcal E_{12},
\qquad
5^h\mid\mathcal E_{13},
\]

则已有

\[
\boxed{
h\le2v_5(Z_0)+v_5(\Xi).}
\tag{1.2}
\]

projective point 写成

\[
z=\frac{X_0+iY_0}{Z_0},
\]

并令

\[
g=(y_1,y_2),
\qquad r_5=v_5(g).
\]

已有 exact formula

\[
\boxed{
Z_0=\frac{H+y_3}{(g,H+y_3)}.
}
\tag{1.3}
\]

同时

\[
(H-y_3)(H+y_3)=y_1^2+y_2^2.
\tag{1.4}
\]

---

## 2. 当 \(5\mid L\) 时两个 moving factors 都是 5-adic units

设

\[
\ell_5:=v_5(L)>0.
\]

由

\[
(L,\eta)=1
\]

得到

\[
v_5(\eta)=0.
\]

又由

\[
(LQ_1,v)=1
\]

得到

\[
v_5(v)=0.
\]

于是

\[
LQ+\tau
=\eta(LQ_1+v),
\]

\[
LQ+2\tau
=\eta(LQ_1+2v).
\]

模 \(5\) 有

\[
LQ_1+v\equiv v\not\equiv0,
\]

\[
LQ_1+2v\equiv2v\not\equiv0.
\]

故

\[
\boxed{
v_5(LQ+\tau)=v_5(LQ+2\tau)=0.}
\tag{2.1}
\]

因此 `(1.1)` 在 5-adic place 的 valuation 完全退化为 decimal baseline：

\[
\boxed{
v_5(\Xi)=v_5(10^{2k}+10^{2d}).}
\tag{2.2}
\]

而直接分情况 \(k<d,k>d,k=d\) 得到

\[
\boxed{
v_5(10^{2k}+10^{2d})=2\min(k,d).}
\tag{2.3}
\]

所以

\[
\boxed{v_5(\Xi)=2\min(k,d).}
\tag{Moving-unit}
\]

**结论：**当 \(5\mid L\) 时，§56 中列出的两个单侧 moving factors 在 5-adic place 完全不能支付任何额外深度。

---

## 3. 一个 odd-prime two-factor lemma

令 \(p\) 为奇素数，\(A,B\in\mathbf Z\)，并记

\[
s=\min(v_p(A),v_p(B)).
\]

若

\[
v_p(A-B)>s,
\]

则

\[
\boxed{v_p(A+B)=s.}
\tag{3.1}
\]

证明：写

\[
A=p^sA_0,
\qquad
B=p^sB_0,
\]

至少一个 \(A_0,B_0\) 为 unit。由

\[
p\mid A_0-B_0
\]

可知二者事实上都是 units 且

\[
A_0\equiv B_0\not\equiv0\pmod p.
\]

因为 \(p\ne2\)，

\[
A_0+B_0\equiv2A_0\not\equiv0\pmod p.
\]

故 (3.1) 成立。

---

## 4. 5-adic angular depth 不会进入 \(Z_0\)

令

\[
s_5:=\min(v_5(H),v_5(y_3)).
\]

sphere gap 为

\[
H-y_3=La,
\]

故

\[
v_5(H-y_3)=\ell_5+v_5(a).
\tag{4.1}
\]

真正的 angular case 正是 gap depth 超过共同 multiplicative scale 的情况，即

\[
\ell_5+v_5(a)>s_5.
\tag{4.2}
\]

对 `(3.1)` 取

\[
A=H,
\qquad B=y_3,
\qquad p=5,
\]

由 `(4.2)` 得

\[
\boxed{v_5(H+y_3)=s_5.}
\tag{4.3}
\]

再由 `(1.3)`：

\[
\begin{aligned}
v_5(Z_0)
&=v_5(H+y_3)
-
\min(r_5,v_5(H+y_3))\\
&=s_5-\min(r_5,s_5).
\end{aligned}
\]

所以

\[
\boxed{
v_5(Z_0)=\max(0,s_5-r_5).}
\tag{Angular-Z0-collapse}
\]

右边只测量 \(H,y_3\) 的 common multiplicative scale 相对于 \((y_1,y_2)\) common scale 的差；它**完全不含** primitive Gaussian angular depth

\[
\omega_5=v_5(X^2+Y^2).
\]

这比旧的

\[
v_5(Z_0)=\max(0,r_5+\omega_5-v_5(La))
\]

更清楚地说明了支付结构：一旦 \(5\)-adic sphere gap 已经深过共同尺度，angular depth 在因子化

\[
(H-y_3)(H+y_3)
\]

中全部进入第一因子 \(H-y_3\)，不会再出现在 complementary projective denominator 中。

换言之：

\[
\boxed{
\text{5-adic angular depth}
\not\longrightarrow Z_0
\quad\text{(after common-scale baseline is separated).}
}
\tag{4.4}
\]

---

## 5. 与 bottom-edge exclusion 合并

旧 §60 已证明，若 primitive prefix angle 有正 5-adic depth

\[
\omega_5>0,
\]

则

\[
\boxed{v_5(U_{12}^{\rm prim})=0.}
\tag{5.1}
\]

因此 primitive bottom carrier edge 不接收 angular depth。

同时 determinant ultrametric theorem 对

\[
\theta_{12},\theta_{13},\theta_{23}
\]

要求三个 valuation 中两个最小值相等。删去 decimal forced baseline 后，由 `(5.1)` 有

\[
v_5(\theta_{12})=0.
\]

于是必有

\[
\boxed{
\min(v_5(\theta_{13}),v_5(\theta_{23}))=0.
}
\tag{5.2}
\]

所以 angular depth至多进入一条上侧 carrier edge；它不可能同时进入两条独立 carrier residual。

---

## 6. angular depth 对 simultaneous carrier contact 的零贡献

将 `(Moving-unit)` 与 `(Angular-Z0-collapse)` 代入无 \(E_D\) bound `(1.2)`：

\[
\boxed{
h
\le
2\max(0,s_5-r_5)
+2\min(k,d).}
\tag{6.1}
\]

右端只包含：

1. common-scale discrepancy \(s_5-r_5\)；
2. explicit decimal baseline \(2\min(k,d)\)。

**primitive angular depth \(\omega_5\) 完全消失。**

因此得到严格 allocation lemma：

\[
\boxed{
\begin{array}{c}
5\mid L,\quad
v_5(H-y_3)>\min(v_5(H),v_5(y_3)),\quad
\omega_5>0\\[2mm]
\Longrightarrow\\[2mm]
\text{任何两条独立 carrier residual 的共同 5-depth，}\
\text{扣除 decimal/common-scale baseline 后都不能由 }\omega_5\text{ 支付。}
\end{array}
}
\tag{Angular-no-double-pay}
\]

结合 `(5.2)`，angular depth 既不能进入 bottom edge，也不能进入 projective denominator，也不能进入 simultaneous upper-edge contact。

---

## 7. 对一般 5-adic allocation 的更新

旧 §61 将 \(v_5(L)\) 分成：

- common-scale / multiplicative；
- genuine angular。

现在第二支可以进一步精确化：

### genuine angular excess

若某一正线性深度确实由

\[
\omega_5=v_5(X^2+Y^2)
\]

承担，那么这份深度只能作为 **sphere-gap angular depth** 存在；它不能再次支付：

- \(Z_0\)；
- primitive bottom edge；
- 两条独立 carrier residual；
- \((LQ+\tau)/\eta\) 或 \((LQ+2\tau)/\eta\) 的 5-depth。

所以凡是后续论证能够证明“同一正线性 excess 必须再出现于任意上述第二通道”，genuine-angular branch 会立即矛盾。

这将一般 projective/common-scale allocation 的开放部分进一步压缩到：

\[
\boxed{
\text{common multiplicative scale}
\quad\cup\quad
\text{至多一条 single-edge angular contact}.
}
\]

真正尚未关闭的是前者，以及如何从 global DD carrier/tail system 强迫 angular excess 必须发生第二次独立接触。

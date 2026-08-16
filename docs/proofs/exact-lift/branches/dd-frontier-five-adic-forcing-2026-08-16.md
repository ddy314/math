# DD frontier 5-adic forcing — 2026-08-16

> 本文接续 [`dd-projective-angular-allocation-2026-08-16.md`](dd-projective-angular-allocation-2026-08-16.md)，并专门回到假想
> \[
> \frac{n_3}{S}\to6.308883577618\ldots
> \]
> 的 terminal frontier。
>
> **结论：**frontier 上球面 gap 的主 \(5\)-进深度不可能由 \(H,y_3\) 的共同 multiplicative scale 支付；它被强制进入 genuine Gaussian angular channel。

---

## 1. terminal 5-adic data

沿用 terminal overlap：

\[
b_3=BJC_0q_c\theta s,
\qquad
\frac{10^m}{B}=2\cdot5^T.
\tag{1.1}
\]

frontier 比例为

\[
\frac mS\to2.808883577618\ldots,
\]

\[
\frac TS\to1.872589051745\ldots,
\]

\[
m_1+m_2=S.
\tag{1.2}
\]

并且 sphere bridge 已给出

\[
\boxed{H-y_3=2\cdot5^T\rho_0,}
\tag{1.3}
\]

其中

\[
\log\rho_0=o(S).
\]

因此

\[
\boxed{v_5(H-y_3)=T+o(S).}
\tag{1.4}
\]

---

## 2. 第三分母自身已经含有 \(5^{m-T}\)

由 `(1.1)`：

\[
B=\frac{10^m}{2\cdot5^T}
=2^{m-1}5^{m-T}.
\]

所以无条件有

\[
\boxed{v_5(b_3)\ge m-T.}
\tag{2.1}
\]

记

\[
e_i=v_5(b_i),
\qquad
E=\max(e_1,e_2,e_3).
\]

全局定义

\[
q=\operatorname{lcm}(b_1,b_2,b_3)
\]

给出

\[
\boxed{v_5(q/b_3)=E-e_3.}
\tag{2.2}
\]

由于 sufficiently large frontier 上 `(2.1)` 给 \(e_3>0\)，而

\[
(a_3,b_3)=1,
\]

故

\[
v_5(a_3)=0.
\]

因此

\[
y_3=a_3\frac q{b_3}
\]

满足

\[
\boxed{v_5(y_3)=E-e_3.}
\tag{2.3}
\]

---

## 3. prefix digit length 给共同尺度一个严格线性上界

对 \(i=1,2\)，因为

\[
1\le b_i<10^{m_i},
\]

若 \(5^{e_i}\mid b_i\)，则

\[
5^{e_i}<10^{m_i},
\]

故

\[
\boxed{e_i<\frac{m_i}{\log_{10}5}.}
\tag{3.1}
\]

又

\[
m_1+m_2=S,
\]

所以

\[
\boxed{
\max(e_1,e_2)
<\frac{S}{\log_{10}5}.
}
\tag{3.2}
\]

由 `(2.2)` 和 `(2.1)`：

\[
\begin{aligned}
E-e_3
&\le
\max\left(
0,
\max(e_1,e_2)-e_3
\right)\\
&<
\max\left(
0,
\frac{S}{\log_{10}5}-(m-T)
\right).
\end{aligned}
\]

因此

\[
\boxed{
\frac{v_5(y_3)}S
\le
\frac1{\log_{10}5}
-\frac mS+\frac TS+o(1).
}
\tag{3.3}
\]

代入 frontier 极限：

\[
\frac1{\log_{10}5}
=1.430676558073\ldots,
\]

故

\[
\boxed{
\limsup\frac{v_5(y_3)}S
\le
0.494382032200\ldots.
}
\tag{3.4}
\]

记

\[
s_5=\min(v_5(H),v_5(y_3)).
\]

显然

\[
s_5\le v_5(y_3),
\]

从而

\[
\boxed{
\limsup\frac{s_5}{S}
\le0.494382032200\ldots.
}
\tag{3.5}
\]

---

## 4. gap depth 与共同尺度之间存在巨大严格余量

另一方面 `(1.4)` 给

\[
\frac{v_5(H-y_3)}S
\to1.872589051745\ldots.
\]

结合 `(3.5)`：

\[
\boxed{
\frac{v_5(H-y_3)-s_5}{S}
\ge
1.378207019545\ldots-o(1).
}
\tag{4.1}
\]

特别地，对 sufficiently large frontier：

\[
\boxed{v_5(H-y_3)>s_5.}
\tag{4.2}
\]

因此 odd-prime two-factor lemma 立即给

\[
\boxed{v_5(H+y_3)=s_5.}
\tag{4.3}
\]

也就是说，球面两个因子中只有小因子 \(H-y_3\) 能承载那份 \(T\)-级深度；互补因子 \(H+y_3\) 只保留共同尺度。

---

## 5. frontier 的主 5-depth 被强制为 angular

由

\[
(H-y_3)(H+y_3)=y_1^2+y_2^2
\]

和 `(4.3)`：

\[
\boxed{
v_5(y_1^2+y_2^2)
=T+s_5+o(S).}
\tag{5.1}
\]

而 \(H,y_3\) 的共同 multiplicative scale 至多只有 `(3.5)` 的高度。

因此至少

\[
1.378207019545\ldots S-o(S)
\]

的 gap depth 无法由 \(H,y_3\) common scale 解释；它只能来自二平方和在 \(\mathbf Q_5(i)=\mathbf Q_5\) 中的高阶 angular cancellation。

所以 frontier 上：

\[
\boxed{
\text{common-scale-only 5-adic branch 不存在。}
}
\tag{Frontier-5-angular}
\]

更精确地，主 \(5\)-进 gap excess 被强制进入 genuine Gaussian angular channel。

---

## 6. 与 projective angular allocation 的合并

[`dd-projective-angular-allocation-2026-08-16.md`](dd-projective-angular-allocation-2026-08-16.md) 已证明，在 genuine angular case：

1. angular depth 不进入 \(Z_0\)；
2. primitive bottom carrier edge 为 5-adic unit；
3. angular depth不能同时进入两条独立 carrier residual；
4. 当 \(5\mid L\) 时，\((LQ+\tau)/\eta\) 与 \((LQ+2\tau)/\eta\) 都是 5-adic units。

本文件进一步说明：在 terminal frontier 上，这个 angular case不是可选分支，而是被 `(4.1)` **强制发生**。

因此 terminal frontier 的 5-adic 主深度已经没有 common-scale 逃逸通道；它只能停留在单一 sphere-angle slot 中，不能被再次用于支付 projective / carrier excess。

这为下一步与 moving odd split-prime core \(C_L\) 联立留下了更干净的边界：

\[
\boxed{
\text{frontier 的 }5\text{-adic budget 已单槽饱和，}
\quad
C_L\text{ 的任何新正线性兼容性要求都必须另行支付。}
}
\]

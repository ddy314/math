# DD frontier 5-adic factor allocation — 2026-08-16

> 本文接续 [`dd-projective-angular-allocation-2026-08-16.md`](dd-projective-angular-allocation-2026-08-16.md)，并专门回到假想
> \[
> \frac{n_3}{S}\to6.308883577618\ldots
> \]
> 的 terminal frontier。
>
> **修正说明：**早期版本曾把 \(H-y_3\) 超出 \((H,y_3)\) common scale 的深度直接判成 primitive Gaussian angular depth。该跳步不成立，因为
> \(y_1,y_2\) 自身还可能携带大的共同 ghost scale。本文保留正确的 factor-asymmetry 结论，并把最终状态改写成 exact `common-ghost + angular` 分配。
>
> **状态边界：**本文不关闭 DD frontier；它精确限制 5-adic 深度可以藏在哪里。

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

sphere bridge 已给出

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

所以

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

sufficiently large frontier 上 `(2.1)` 给 \(e_3>0\)，又

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

## 3. prefix digit length 给 \(y_3\) 的 5-depth 一个严格线性上界

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

得到

\[
\boxed{
\limsup\frac{v_5(y_3)}S
\le
0.494382032200\ldots.
}
\tag{3.4}
\]

令

\[
s_5=\min(v_5(H),v_5(y_3)).
\]

则

\[
\boxed{
\limsup\frac{s_5}{S}
\le0.494382032200\ldots.
}
\tag{3.5}
\]

---

## 4. sphere 两因子的 5-adic valuation 被完全定向

由 `(1.4)` 与 `(3.5)`：

\[
\boxed{
\frac{v_5(H-y_3)-s_5}{S}
\ge
1.378207019545\ldots-o(1).
}
\tag{4.1}
\]

所以 sufficiently large frontier 上

\[
\boxed{v_5(H-y_3)>s_5.}
\tag{4.2}
\]

对奇素数 \(5\) 使用 elementary two-factor lemma：若

\[
s=\min(v_5(A),v_5(B)),
\qquad
v_5(A-B)>s,
\]

则

\[
v_5(A+B)=s.
\]

取

\[
A=H,
\qquad B=y_3,
\]

得到

\[
\boxed{v_5(H+y_3)=s_5.}
\tag{4.3}
\]

因此

\[
\boxed{
v_5(y_1^2+y_2^2)
=T+s_5+o(S).}
\tag{4.4}
\]

这里必须强调：`(4.4)` 只规定总二平方和 valuation；它尚未区分 \(y_1,y_2\) 的共同 ghost scale 与 primitive angle。

---

## 5. 正确的 `common-ghost + angular` 分解

写

\[
g=(y_1,y_2),
\qquad
y_1=gX,
\qquad
y_2=gY,
\qquad(X,Y)=1.
\]

定义

\[
r_5=v_5(g),
\qquad
\omega_5=v_5(X^2+Y^2).
\]

则 `(4.4)` 精确给出

\[
\boxed{
2r_5+\omega_5
=T+s_5+o(S).
}
\tag{5.1}
\]

所以 frontier 的主 5-adic budget 只能分配到两个槽：

1. `common-ghost`：\(2r_5\)；
2. `primitive angular`：\(\omega_5\)。

原先从 `(4.1)` 直接推出 \(\omega_5\) 线性大的论证是错误的，因为 \(r_5\) 也可以是线性大的。

---

## 6. projective denominator 对 angular 深度仍然零收费

projective denominator 的 exact formula 为

\[
Z_0=\frac{H+y_3}{(g,H+y_3)}.
\]

由 `(4.3)`：

\[
\boxed{
v_5(Z_0)
=s_5-\min(r_5,s_5)
=\max(0,s_5-r_5).}
\tag{6.1}
\]

这条式子仍然是一个真实的新简化：\(v_5(Z_0)\) **完全不含** \(\omega_5\)。

所以无论 `(5.1)` 中 angular slot 占多少，primitive angular depth 都不能再被 \(Z_0\) 重复支付。

特别地：

- 若 \(r_5\ge s_5\)，则
  \[
  \boxed{v_5(Z_0)=0;}
  \]
- 若 \(r_5<s_5\)，则
  \[
  v_5(Z_0)=s_5-r_5
  \le0.494382032200\ldots S+o(S).
  \]

---

## 7. 与 angular/bottom exclusion 合并后的正确状态

[`dd-projective-angular-allocation-2026-08-16.md`](dd-projective-angular-allocation-2026-08-16.md) 的 conditional angular conclusions 保持有效：若

\[
\omega_5>0,
\]

则 primitive bottom carrier edge 不接收该 angular depth；determinant ultrametric 又阻止它同时进入两条 independent upper carrier edges；且当 \(5\mid L\) 时两个 normalized tail moving factors 都是 5-adic units。

因此当前 frontier 5-adic 状态应写成：

\[
\boxed{
2r_5+\omega_5=T+s_5+o(S),
\qquad
s_5\le0.494382032200\ldots S+o(S),
}
\]

其中：

- \(\omega_5\) 不能再次支付 \(Z_0\) 或 simultaneous carrier contact；
- 尚未关闭的主要逃逸是线性大的 common-ghost scale \(r_5\)，以及 angular depth 只停留在单一允许槽中的情形。

换言之，frontier 的 5-adic 问题已经从“common scale / angular / projective / moving factor 多槽混合”压成了：

\[
\boxed{
\text{common ghost scale }r_5
\quad\cup\quad
\text{single-slot angular remainder }\omega_5.
}
\]

下一步应优先把 \(r_5\) 用 denominator overlap \(g_*\)、primitive recovery 与 reducedness 精确参数化；若能证明 \(r_5\) 的线性部分必须进入已被 pair-max / carrier 使用的同一 denominator slot，就会产生真正的 capacity surplus。

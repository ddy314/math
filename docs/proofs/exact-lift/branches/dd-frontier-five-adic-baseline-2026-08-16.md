# DD frontier primitive 5-adic baseline — 2026-08-16

> 本文继续 [`dd-frontier-five-adic-forcing-2026-08-16.md`](dd-frontier-five-adic-forcing-2026-08-16.md) 修正后的 `common-ghost + angular` 分解。
> 适用范围是同一个假想 \(6.308883577618\ldots\) terminal frontier，并采用其规范化取向
> \[
> (m_1,m_2;n_1,n_2)
> =(o(S),S-o(S);S-o(S),o(S)).
> \]
>
> **核心结论：**frontier 的 primitive \(5\)-adic angular depth在 leading order 上由 denominator 的 \(5\)-adic exponent pattern完全决定，并不是新的独立 entropy。

---

## 1. denominator 与 numerator 的 small side

记

\[
e_i=v_5(b_i),
\qquad
E=\max(e_1,e_2,e_3).
\]

frontier digit shape 给

\[
m_1=o(S),
\qquad
n_2=o(S).
\]

因此

\[
\boxed{e_1=o(S),}
\tag{1.1}
\]

并且

\[
\boxed{v_5(a_2)=o(S).}
\tag{1.2}
\]

terminal overlap 为

\[
t=(10^mQ,b_3),
\qquad
u=\frac{10^mQ}{t}=2\cdot5^TU,
\qquad
v=\frac{b_3}{t}=V,
\]

其中 \(U,V\) 为 5-adic units。故

\[
v_5(b_3)=v_5(t)
=m+v_5(Q)-T.
\]

terminal slow-data normalization 给

\[
v_5(Q)=o(S),
\]

所以

\[
\boxed{e_3=m-T+o(S).}
\tag{1.3}
\]

frontier 比例还满足

\[
\boxed{3T=2m+o(S),}
\tag{1.4}
\]

因为

\[
\frac mS\to2.808883577618\ldots,
\qquad
\frac TS\to1.872589051745\ldots.
\]

---

## 2. \(s_5\) 实际上等于第三 ghost 的 denominator deficit

全局

\[
q=\operatorname{lcm}(b_1,b_2,b_3)
\]

给

\[
y_i=a_i\frac q{b_i}.
\]

由于 sufficiently large frontier 上 \(e_3>0\)，reducedness 给

\[
v_5(a_3)=0.
\]

所以

\[
\boxed{v_5(y_3)=E-e_3.}
\tag{2.1}
\]

前一文件已证明

\[
v_5(H-y_3)>v_5(y_3)
\]

对 sufficiently large frontier 成立。因此

\[
H=y_3+(H-y_3)
\]

直接给

\[
\boxed{v_5(H)=v_5(y_3)=E-e_3.}
\tag{2.2}
\]

故

\[
\boxed{s_5:=\min(v_5(H),v_5(y_3))=E-e_3.}
\tag{2.3}
\]

这里没有剩余误差。

---

## 3. common ghost scale \(r_5\) 的 leading formula

令

\[
g=(y_1,y_2),
\qquad
r_5=v_5(g).
\]

由

\[
v_5(y_1)=E-e_1+v_5(a_1),
\]

\[
v_5(y_2)=E-e_2+v_5(a_2),
\]

以及 `(1.1)`--`(1.2)`：

\[
v_5(y_1)\ge E-o(S),
\]

\[
v_5(y_2)=E-e_2+o(S).
\]

因为 \(e_2\ge0\)，两式取最小得到

\[
\boxed{r_5=E-e_2+o(S).}
\tag{3.1}
\]

这说明 common ghost scale 也不是独立变量；leading order 上它就是总 \(5\)-进 denominator maximum 相对第二分母的 deficit。

---

## 4. primitive angular depth 的 denominator-only formula

写

\[
y_1=gX,
\qquad
y_2=gY,
\qquad(X,Y)=1,
\]

并令

\[
\omega_5=v_5(X^2+Y^2).
\]

前一文件已得

\[
2r_5+\omega_5=T+s_5+o(S).
\tag{4.1}
\]

代入 `(2.3)` 与 `(3.1)`：

\[
2(E-e_2)+\omega_5
=T+(E-e_3)+o(S),
\]

所以

\[
\boxed{
\omega_5
=T-E+2e_2-e_3+o(S).
}
\tag{4.2}
\]

因为 `(1.1)` 给 \(e_1=o(S)\)，leading order 上

\[
E=\max(e_2,e_3)+o(S).
\]

分两种情况。

### 4.1 tail 5-max：\(e_2\le e_3+o(S)\)

此时 \(E=e_3+o(S)\)，故

\[
\omega_5
=T+2e_2-2e_3+o(S).
\]

由 `(1.3)`--`(1.4)`：

\[
T-2e_3
=T-2(m-T)+o(S)
=3T-2m+o(S)
=o(S).
\]

因此

\[
\boxed{\omega_5=2e_2+o(S).}
\tag{4.3}
\]

### 4.2 prefix 5-max：\(e_2\ge e_3+o(S)\)

此时 \(E=e_2+o(S)\)，故

\[
\omega_5
=T+e_2-e_3+o(S).
\]

而

\[
T-e_3
=T-(m-T)+o(S)
=2T-m+o(S).
\]

由 \(3T=2m+o(S)\)：

\[
2T-m=m-T+o(S)=e_3+o(S).
\]

所以

\[
\boxed{\omega_5=e_2+e_3+o(S).}
\tag{4.4}
\]

统一得到

\[
\boxed{
\omega_5
=e_2+\min(e_2,e_3)+o(S).
}
\tag{5-adic-baseline}
\]

---

## 5. 解释：primitive angle 已被 denominator baseline 完全支付

右端

\[
e_2+\min(e_2,e_3)
\]

只依赖 \((b_2,b_3)\) 的 5-adic exponent pattern。它可以写成

\[
\boxed{
\omega_5
=v_5(b_2)+v_5((b_2,b_3))+o(S).
}
\tag{5.1}
\]

所以 terminal frontier 的 primitive Gaussian angle 虽然可能具有正线性深度，但它在 leading order 上**没有独立算术自由度**：每一份深度都已经由 denominator 5-adic baseline 预先决定。

这解释了此前多个 5-adic / projective 尝试为何不断达到临界等号：

\[
\boxed{
\text{frontier 5-adic angle}
=\text{denominator baseline}+o(S).
}
\]

因此后续若要关闭 terminal frontier，不应再把 \(\omega_5\) 当成一份可额外收费的 height。

---

## 6. 与 projective no-double-pay 的最终合并

虽然 \(\omega_5\) 没有独立 entropy，前两份 continuation 仍给出重要的“不重复计费”信息：

- \(\omega_5\) 不进入 \(Z_0\)；
- \(\omega_5>0\) 时 primitive bottom carrier 不接收同一份 angular depth；
- angular depth 不能同时进入两条 independent upper carrier edges；
- normalized tail moving factors在 \(5\mid L\) 时都是 5-adic units。

现在这些结论应解释为：**denominator 已经支付的 5-adic baseline 不能再被 projective/carrier 层重复使用。**

所以 terminal frontier 剩余的真正正线性未决对象继续是 odd split-prime moving core \(C_L\) 及其 digit-shell compatibility，而不是 5-adic angular entropy。

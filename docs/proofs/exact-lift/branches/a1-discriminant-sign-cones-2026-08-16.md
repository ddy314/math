# A1 discriminant-sign prefix cones — 2026-08-16

本文继续 moving-prefix 四层主线。A1 的 universal discriminant square 还携带一个此前未显式利用的符号信息：平方根恰好是 `|P-R-r_3|`。

这把所有候选分成两个几何支，并直接把前两分母拼接 `Q` 的位数长度 `m_1+m_2` 与 `k+2g` 联系起来。

本文结论均为 **已严格完成**。

---

## 1. 判别平方的精确平方根

A1 rational contact 为

\[
P-R=\theta(R-r_3),
\qquad
\theta=\frac{b_3}{10^\ell D}>0.
\tag{1}
\]

所以

\[
P=(1+\theta)R-\theta r_3.
\tag{2}
\]

又

\[
R^2-r_3^2=r_1^2+r_2^2.
\]

直接展开：

\[
\begin{aligned}
P^2-(1+2\theta)(r_1^2+r_2^2)
&=((1+\theta)R-\theta r_3)^2
 -(1+2\theta)(R^2-r_3^2)\\
&=\left(\theta R-(1+\theta)r_3\right)^2.
\end{aligned}
\]

而由 (1)

\[
\theta R-(1+\theta)r_3
=(P-R)-r_3.
\]

因此

\[
\boxed{
P^2-(1+2\theta)(r_1^2+r_2^2)
=(P-R-r_3)^2.
}
\tag{3}
\]

所以 universal discriminant 的两个根号符号对应以下两个真实几何区域：

\[
\boxed{P-R\ge r_3}
\qquad\text{与}\qquad
\boxed{P-R<r_3}.
\]

---

## 2. `theta` 的十进制 mantissa 形式

记

\[
\sigma=\frac{b_3}{10^{m_3}}.
\]

因为 `b_3` 恰有 `m_3` 位，

\[
\boxed{\frac1{10}\le\sigma<1.}
\tag{4}
\]

又 `m_3=g+\ell`、`D=10^gQ`，故

\[
\theta
=\frac{b_3}{10^\ell 10^gQ}
=\boxed{\frac\sigma Q}.
\tag{5}
\]

因此

\[
\boxed{
\frac1{10Q}\le\theta<\frac1Q.
}
\]

---

## 3. Outer-contact 支：`P-R >= r_3`

假设

\[
P-R\ge r_3.
\tag{6}
\]

由 (1)：

\[
\theta(R-r_3)\ge r_3,
\]

所以

\[
\theta R\ge(1+\theta)r_3
\]

并得到

\[
\frac R{r_3}
\ge1+\frac1\theta.
\tag{7}
\]

由 `\theta<1/Q`：

\[
1+\frac1\theta>Q+1,
\]

故

\[
\boxed{Q<\frac R{r_3}.}
\tag{8}
\]

现在记统一四层参数

\[
\boxed{h=s_1-g\in\{-1,0,1,2\}.}
\]

第一 carrier 给出

\[
R<10^kr_1,
\]

而位数窗给出

\[
r_1<10^{s_1+1}=10^{g+h+1},
\qquad
r_3>10^{-g-1}.
\]

于是

\[
\frac R{r_3}
<10^{k+2g+h+2}.
\]

结合 (8)：

\[
\boxed{Q<10^{k+2g+h+2}.}
\tag{9}
\]

`Q=b_1 10^{m_2}+b_2` 正好是两个分母块的十进制拼接，所以

\[
\operatorname{digits}(Q)=m_1+m_2.
\]

由 (9) 得

\[
\boxed{
m_1+m_2\le k+2g+h+2.
}
\tag{10}
\]

这就是 outer-contact 的短分母锥。

由于 `h\le2`，粗化为

\[
\boxed{m_1+m_2\le k+2g+4.}
\tag{11}
\]

---

## 4. Inner-contact 支：`P-R < r_3`

现在假设

\[
P-R<r_3.
\tag{12}
\]

由 (1)：

\[
\theta(R-r_3)<r_3,
\]

故

\[
\frac R{r_3}<1+\frac1\theta.
\]

由 `\theta\ge1/(10Q)`：

\[
\boxed{
\frac R{r_3}<1+10Q.
}
\tag{13}
\]

另一方面

\[
R>r_2>10^{k+g-1},
\qquad
r_3<10^{1-g},
\]

所以

\[
\boxed{
\frac R{r_3}>10^{k+2g-2}.
}
\tag{14}
\]

令

\[
q_0=k+2g.
\]

由 (13)–(14)：

\[
10^{q_0-2}<1+10Q,
\]

所以

\[
Q>\frac{10^{q_0-2}-1}{10}
=10^{q_0-3}-\frac1{10}.
\tag{15}
\]

当

\[
q_0\ge3
\]

时，`Q` 是正整数，因此 (15) 强迫

\[
\boxed{Q\ge10^{q_0-3}.}
\tag{16}
\]

所以 `Q` 至少有 `q_0-2` 位：

\[
\boxed{
m_1+m_2\ge k+2g-2,
\qquad(k+2g\ge3).
}
\tag{17}
\]

这就是 inner-contact 的长分母锥。

对 `k+2g=1,2`，(15) 仍保留为正确实数下界，但不给出新的位数信息；这不影响 universal 四层定理。

---

## 5. 符号由分母总长在远区自动决定

令

\[
M_{12}=m_1+m_2.
\]

由 (10)：若

\[
M_{12}>k+2g+h+2,
\]

则 outer-contact 不可能，所以候选必须属于 inner-contact。

而当 `k+2g\ge3` 时，由 (17)：若

\[
M_{12}<k+2g-2,
\]

则 inner-contact 不可能，所以候选必须属于 outer-contact。

因此只有窄带

\[
\boxed{
k+2g-2
\le M_{12}\le
k+2g+h+2}
\tag{18}
\]

可能同时容纳两个判别式符号。

其整数层宽度为

\[
(h+2)-(-2)+1=h+5\le7.
\]

所以在四层主线中：

- 很短的前缀分母长度自动选择 outer root；
- 很长的前缀分母长度自动选择 inner root；
- 真正需要同时保留两个根号符号的，只是围绕 `m_1+m_2\asymp k+2g` 的至多七层 transition strip。

---

## 6. 当前用途

这一步没有声称 A1 已全局关闭，但它把此前抽象的 `\pm` 根分支转化为一个可审计的前缀高度分解：

\[
\boxed{
\text{outer root}\Rightarrow
m_1+m_2\le k+2g+h+2,
}
\]

\[
\boxed{
\text{inner root}\Rightarrow
m_1+m_2\ge k+2g-2
\quad(k+2g\ge3).
}
\]

下一步可分别针对：

1. outer 的短分母锥，利用分子位数 surplus 相对更大这一事实做整除/小因子分析；
2. inner 的长分母锥，利用 `Q` 大导致 contact 极窄这一事实做 rational-gap / p-adic 分析；
3. transition strip，只有常数宽度，可按 `h=-1,0,1,2` 做更精确的边界归约。

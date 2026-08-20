# A1 minimal diagonal: full 2-high denominator cap

> 日期：2026-08-20。依赖 `deep-q-side-proper-divisor.md`、`deep-b1-block-loss.md` 与 `deep-double-2high-master.md`。当前 `k>=32`。

本文把 Q-side proper-divisor loss 与 `b_1` whole-block loss 反向用于 numerator identity，得到对全部 surviving double-deep master 的显式 denominator cap

\[
\boxed{D<C_wT^2.}
\]

状态：**已严格完成。**

---

## 1. selected Q factor 的 upper bound

strict 2-deep 中已有

\[
q\le\frac Q{m_w},
\]

其中

\[
\boxed{
(m_1,m_2,m_3,m_4)=(7,3,7,7).}
\tag{1}

---

## 2. numerator identity 给 selected `s` 下界

在 double-deep `lambda=1`：

\[
h=D(TN_0-\Gamma).
\]

当前

\[
TN_0-\Gamma>\frac{T^2}{11}.
\]

所以

\[
\boxed{h>DT^2/11.}
\tag{2}

而

\[
h=qs,
\qquad q<Q/m_w.
\]

使用 `Q<101T^2`：

\[
s=\frac hq
>\frac{DT^2/11}{101T^2/m_w}
=\frac{m_wD}{1111}.
\]

即

\[
\boxed{s>m_wD/1111.}
\tag{3}

---

## 3. `b_1` whole-block upper bound

结构性 block loss：

\[
s\le\frac{b_1}{c_w},
\]

其中

\[
\boxed{
(c_1,c_2,c_3,c_4)=(3,14,1,12).}
\tag{4}

又

\[
b_1<10T^2.
\]

结合 (3)-(4)：

\[
\frac{m_wD}{1111}
<\frac{10T^2}{c_w}.
\]

所以

\[
\boxed{
D<\frac{11110}{m_wc_w}T^2.}
\tag{5}

取整洁安全常数：

\[
\boxed{
\begin{array}{c|c}
w&C_w\\ \hline
1&530\\
2&265\\
3&1588\\
4&133
\end{array}}
\tag{6}

于是

\[
\boxed{D<C_wT^2.}
\tag{7}

---

## 4. master offset `eta` 的显式斜率 cap

master 中

\[
D=2^{2k+3+\eta}5^B,
\qquad T^2=2^{2k}5^{2k}.
\]

代入 (7)：

\[
2^{3+\eta}5^B<C_w5^{2k}.
\]

故

\[
\boxed{
\eta<\log_2C_w-3+(2k-B)\log_25.}
\tag{8}

这对 `eta<=0` moderate 自动满足；对 former `E_2` 则把 pure-2 excess 从无界 half-line 压进显式线性楔形。

尤其 w=4 的常数最强：

\[
2^{3+\eta}5^B<133\,5^{2k}.
\]

---

## 5. 额外尺度信息

由 complement quotient

\[
M=uv<10001T^2/D
\]

和 `v>=m_w`，还有

\[
\boxed{
u<\frac{10001}{m_w}\frac{T^2}{D}.}
\tag{9}

所以 eta 增长时 complementary `u` 会被强制迅速变小；一旦 RHS<1，该 branch 直接空。该 endpoint 与 (7) 等价地提供另一种 extreme-descent接口。

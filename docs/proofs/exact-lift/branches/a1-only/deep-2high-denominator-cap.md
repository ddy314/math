# A1 minimal diagonal: full 2-high denominator cap

> 日期：2026-08-20。依赖 `deep-q-side-proper-divisor.md`、`deep-b1-block-loss.md`、`deep-complement-height.md` 与 `deep-double-2high-master.md`。当前 `k>=32`。

本文把 Q-side proper-divisor direction 与 `b_1` whole-block loss 反向用于 complement quotient，得到对全部 surviving double-deep master 的显式 denominator cap。

最终 sharpened 版本是

\[
\boxed{
D<
\begin{cases}
477T^2,&w=1,\\
239T^2,&w=2,\\
1429T^2,&w=3,\\
120T^2,&w=4.
\end{cases}}
\]

状态：**已严格完成。**

---

## 1. 两个 complementary divisors 都有固定下界

写

\[
u=b_1/s,
\qquad v=Q/q.
\]

### `v` 的下界

strict 2-deep 中 Q-side orientation 已证明 `q` 是 proper divisor，并且

\[
q\le Q/m_w,
\]

其中

\[
\boxed{
(m_1,m_2,m_3,m_4)=(7,3,7,7).}
\tag{1}

所以

\[
\boxed{v=Q/q\ge m_w.}
\tag{2}

### `u` 的下界

whole-block selector `s` 只能选择 `b_1` 的 `1 mod4` odd prime-power blocks。结构性 loss 给

\[
s\le b_1/c_w,
\]

其中

\[
\boxed{
(c_1,c_2,c_3,c_4)=(3,14,1,12).}
\tag{3}

因此

\[
\boxed{u=b_1/s\ge c_w.}
\tag{4}

于是 complement product

\[
M=uv
\]

满足

\[
\boxed{
M\ge c_wm_w.}
\tag{5}

四个 w：

\[
\boxed{
(c_wm_w)=(21,42,7,84).}
\tag{6}

---

## 2. complement-height 直接给 sharp D cap

`deep-complement-height.md` 对 double-deep `lambda=1` 给

\[
\mu:=\frac{MD}{T^2}<10001.
\]

所以

\[
D<\frac{10001}{M}T^2.
\]

结合 (5)：

\[
\boxed{
D<\frac{10001}{c_wm_w}T^2.}
\tag{7}

数值：

\[
\begin{array}{c|c|c}
w&10001/(c_wm_w)&\text{safe integer cap}\\ \hline
1&<476.24&477\\
2&<238.12&239\\
3&<1428.72&1429\\
4&<119.06&120
\end{array}
\]

所以

\[
\boxed{
D<
\begin{cases}
477T^2,&w=1,\\
239T^2,&w=2,\\
1429T^2,&w=3,\\
120T^2,&w=4.
\end{cases}}
\tag{8}

这比此前经 `h` 粗界得到的 `530,265,1588,133` 全部更强，而且证明更直接。

---

## 3. master offset `eta` 的显式斜率 cap

master 中

\[
D=2^{2k+3+\eta}5^B,
\qquad
T^2=2^{2k}5^{2k}.
\]

若用 (8) 中对应安全常数 `C_w`：

\[
2^{3+\eta}5^B<C_w5^{2k}.
\]

故

\[
\boxed{
\eta<\log_2C_w-3+(2k-B)\log_25.}
\tag{9}

这对 `eta<=0` moderate 自动满足；对 `eta>0` pure-2 denominator side 则把 excess 压进显式线性楔形。

特别是 `w=4`：

\[
\boxed{2^{3+\eta}5^B<120\,5^{2k}.}
\]

---

## 4. complementary size endpoint

由

\[
M<10001T^2/D
\]

和 `v>=m_w`：

\[
\boxed{
u<\frac{10001}{m_w}\frac{T^2}{D}.}
\tag{10}

同理由 `u>=c_w`：

\[
\boxed{v<\frac{10001}{c_w}\frac{T^2}{D}.}
\tag{11}

所以 denominator `D/T^2` 越接近其 typewise cap，两个 complementary divisors 就越被迫贴近各自的最小 structural blocks。

这给 extreme `eta>0` 一个后续 finite endpoint：当右侧区间宽度小于 1 时，`u` 或 `v` 会被唯一锁死到 fixed small divisor，从而可直接代回 master equation。

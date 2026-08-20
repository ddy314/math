# A1 minimal diagonal: full 2-high denominator cap

> 日期：2026-08-20。依赖 `deep-q-side-proper-divisor.md`、`deep-b1-sharp-mandatory-blocks.md`、`deep-complement-height.md` 与 `deep-double-2high-master.md`。当前 `k>=32`。

本文把 Q-side proper-divisor direction 与 sharpened `b_1` mandatory-block loss 反向用于 complement quotient，得到对全部 surviving double-deep master 的显式 denominator cap。

最终版本：

\[
\boxed{
D<
\begin{cases}
159T^2,&w=1,\\
88T^2,&w=2,\\
1429T^2,&w=3,\\
120T^2,&w=4.
\end{cases}}
\]

状态：**已严格完成。**

---

## 1. 两个 complementary divisors 的 sharp fixed minima

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
\boxed{(m_1,m_2,m_3,m_4)=(7,3,7,7).}
\tag{1}

所以

\[
\boxed{v\ge m_w.}
\tag{2}

### `u` 的 sharpened 下界

`deep-b1-sharp-mandatory-blocks.md` 给

\[
\boxed{(c_1,c_2,c_3,c_4)=(9,38,1,12),}
\tag{3}

且

\[
\boxed{u\ge c_w.}
\tag{4}

这里：

- `w=1`：整个 3-primary block至少 `3^2`，故 `u>=9`；
- `w=2`：mandatory `3 mod4` odd prime不可能是 3,7,11，所以至少 19，加 fixed factor 2 得 `u>=38`；
- `w=3`：仍保留 `u>=1`；
- `w=4`：`2^2*3` mandatory，故 `u>=12`。

因此

\[
\boxed{M=uv\ge c_wm_w,}
\tag{5}

即

\[
\boxed{(c_wm_w)=(63,114,7,84).}
\tag{6}

---

## 2. complement-height 给 sharp D cap

`deep-complement-height.md` 在 double-deep `lambda=1`：

\[
\mu:=\frac{MD}{T^2}<10001.
\]

所以

\[
D<\frac{10001}{M}T^2
\le\frac{10001}{c_wm_w}T^2.
\]

数值：

\[
\begin{array}{c|c|c}
w&10001/(c_wm_w)&\text{safe cap}\\ \hline
1&<158.75&159\\
2&<87.73&88\\
3&<1428.72&1429\\
4&<119.06&120
\end{array}
\]

因此

\[
\boxed{
D<
\begin{cases}
159T^2,&w=1,\\
88T^2,&w=2,\\
1429T^2,&w=3,\\
120T^2,&w=4.
\end{cases}}
\tag{7}

`w=1,2` 相比旧 cap `477,239` 分别再缩约 3 倍和 2.7 倍。

---

## 3. master offset `eta` 的显式斜率 cap

master：

\[
D=2^{2k+3+\eta}5^B,
\qquad T^2=2^{2k}5^{2k}.
\]

若记 (7) 中 safe cap 为 `C_w`：

\[
2^{3+\eta}5^B<C_w5^{2k}.
\]

因此

\[
\boxed{
\eta<\log_2C_w-3+(2k-B)\log_25.}
\tag{8}

这对 `eta<=0` moderate 自动满足；对 `eta>0` pure-2 denominator side 则给显式线性楔形。

特别地：

\[
\boxed{w=2:\quad2^{3+\eta}5^B<88\,5^{2k}.}
\]

---

## 4. complementary size endpoint

由

\[
M<10001T^2/D
\]

可分别得到

\[
\boxed{u<\frac{10001}{m_w}\frac{T^2}{D},}
\]

\[
\boxed{v<\frac{10001}{c_w}\frac{T^2}{D}.}
\tag{9}

所以 denominator `D/T^2` 越靠近 (7) 的 cap，`u,v` 越被迫贴近其 fixed mandatory minima。

这正是 `deep-2high-endpoint-collapse.md` 的 finite endpoint 机制；使用本文 sharp `c_w` 后，`w=1,2` endpoint thresholds 也应同步加强。

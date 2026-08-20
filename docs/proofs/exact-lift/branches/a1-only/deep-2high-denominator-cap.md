# A1 minimal diagonal: full 2-high denominator cap

> 日期：2026-08-20。依赖 `deep-q-side-proper-divisor.md`、`deep-b1-sharp-mandatory-blocks.md`、`deep-w1-joint-complement-minimum.md`、`deep-complement-height.md` 与 `deep-double-2high-master.md`。当前 `k>=32`。

本文给全部 surviving double-deep 2-high master 的 denominator cap。`w=1` 还使用 u/v 周期不能同时取独立最小值的 joint refinement。

最终：

\[
\boxed{
D<
\begin{cases}
17T^2,&w=1,\\
88T^2,&w=2,\\
1429T^2,&w=3,\\
120T^2,&w=4.
\end{cases}}
\]

状态：**已严格完成。**

---

## 1. independent complement minima

写

\[
u=b_1/s,
\qquad v=Q/q.
\]

Q-side proper-divisor orientation：

\[
\boxed{(v_{\min})=(7,3,7,7).}
\]

`deep-b1-sharp-mandatory-blocks.md`：

\[
\boxed{(u_{\min})=(27,38,1,12).}
\]

所以 independent product minima 为

\[
\boxed{uv\ge(189,114,7,84).}
\tag{1}

---

## 2. w=1 joint improvement

`deep-w1-joint-complement-minimum.md` 利用：

- `v3(b1)=2+v3(2k+1)`；
- `7|Q iff k=0 mod3`；
- `19|Q iff k=4 mod9`；
- `3,11 not|Q`；

证明独立 minima `u=27`,`v=7` 不能同时出现，并最终得到

\[
\boxed{w=1:\quad M=uv\ge621.}
\tag{2}

其余三型暂保留 independent minima：

\[
\boxed{
M\ge
\begin{cases}
114,&w=2,\\
7,&w=3,\\
84,&w=4.
\end{cases}}
\tag{3}

---

## 3. complement-height 转成 D cap

在 double-deep：

\[
\mu:=MD/T^2<10001.
\]

因此

\[
D<\frac{10001}{M}T^2.
\]

由 (2)-(3)：

\[
\boxed{
D<
\begin{cases}
17T^2,&w=1,\\
88T^2,&w=2,\\
1429T^2,&w=3,\\
120T^2,&w=4.
\end{cases}}
\tag{4}

其中 w=1 的精确 ratio 是

\[
10001/621<16.11,
\]

所以 `17T^2` 是整洁 safe cap。

---

## 4. master offset `eta` slope

master：

\[
D=2^{2k+3+\eta}5^B,
\qquad T^2=2^{2k}5^{2k}.
\]

若 `C_w=(17,88,1429,120)`：

\[
2^{3+\eta}5^B<C_w5^{2k}.
\]

所以

\[
\boxed{
\eta<\log_2C_w-3+(2k-B)\log_25.}
\tag{5}

`w=1` 现在尤其强：

\[
\boxed{2^{3+\eta}5^B<17\,5^{2k}.}
\]

---

## 5. complement size endpoint

仍有

\[
M<10001T^2/D.
\]

所以任何更强的 joint lower bound on M 都会立即转成 D/T^2 cap。`w=1` 展示了这种“period-coupled complement minimum”比单独 u/v minima 强得多；后续可对 w=2,3,4继续寻找类似 coupling。

# A1 minimal diagonal: tiny complementary divisors in moderate HL

> 日期：2026-08-20。依赖 `deep-hl-q-superlinear.md` 与 complement-height identity。

本文证明 moderate HL 中两个 complementary divisors 都远小于 decimal center `T=10^k`：

\[
\boxed{u<5\cdot10^{-6}T,}
\qquad
\boxed{v<10^{-5}T.}
\]

相应 selected supply factors `s,q` 都远大于 T。

状态：**已严格完成。**

---

## 1. `v` 已由 sharp q bound 控制

`deep-hl-q-superlinear.md` 给

\[
q>10,900,000T.
\]

而

\[
Q<101T^2.
\]

所以

\[
\boxed{
v=Q/q<\frac{101}{10,900,000}T<10^{-5}T.}
\tag{1}

---

## 2. `5^d` 相对 `sqrt M` 很小

moderate HL 中

\[
M=uv,
\qquad
1000<\mu:=MD/T^2<10001.
\]

记

\[
a_2=v_2(r),
\qquad a_5=v_5(r),
\qquad d=k+1-(B+\nu_5).
\]

直接计算：

\[
\frac{T^2}{D5^{2d}}
=2^{a_2-3}5^{a_5-2}.
\]

因为

\[
a_2\ge0,
\qquad a_5\ge1,
\]

故

\[
2^{a_2-3}5^{a_5-2}\ge\frac1{40}.
\]

于是

\[
\boxed{
\frac M{5^{2d}}
=\mu\frac{T^2}{D5^{2d}}
>25.}
\tag{2}

所以

\[
\boxed{5^d<\frac{\sqrt M}{5}.}
\tag{3}

---

## 3. 用 complement quadratic 控制 `u`

stripped complement equation

\[
2\beta u-\alpha v=5^d
\]

结合 `uv=M`，把 `v=M/u` 代入：

\[
2\beta u^2-5^d u-\alpha M=0.
\]

正根：

\[
\boxed{
u=
\frac{5^d+\sqrt{5^{2d}+8\alpha\beta M}}
{4\beta}.}
\tag{4}

因为

\[
\alpha\beta=r_{10},
\]

由 (2)-(3)：

\[
5^d+\sqrt{5^{2d}+8r_{10}M}
<\sqrt M\left(\frac15+\sqrt{\frac1{25}+8r_{10}}\right).
\]

对 `r_10>=1` 可用安全界

\[
\frac15+\sqrt{\frac1{25}+8r_{10}}
<3.04\sqrt{r_{10}}.
\]

所以

\[
\boxed{
\frac uT
<0.76\sqrt{\frac{10001r_{10}}D}.}
\tag{5}

---

## 4. 再次利用 `D/r_10` cancellation

`deep-hl-q-superlinear.md` 已证明

\[
\frac D{r_{10}}
=\frac{2^{2k+3}5^{B+a_5}}r
\ge
\frac{25\cdot2^{2k+3}}{15,204,352}.
\]

所以

\[
\frac{r_{10}}D
\le
\frac{15,204,352}{25\cdot2^{2k+3}}.
\]

代入 (5)，最弱层 `k=32`：

\[
\frac uT
<0.76\sqrt{
\frac{10001\cdot15,204,352}
{25\cdot2^{67}}
}
<4.9\cdot10^{-6}.
\]

故取整洁安全界

\[
\boxed{u<5\cdot10^{-6}T.}
\tag{6}

以后 k 每增加 1，该相对界至少再缩小一半。

---

## 5. selected factors 反向巨大

因为

\[
b_1=10T^2-w>9T^2,
\]

由 `su=b1` 与 (6)：

\[
\boxed{
s>1.8\cdot10^6T.}
\tag{7}

而 q 已有

\[
\boxed{q>10.9\cdot10^6T.}
\tag{8}

所以 moderate HL 的 four-factor frame 呈现强烈尺度分离：

\[
\boxed{
\max(u,v)<10^{-5}T
\ll T
\ll\min(s,q).}
\tag{9}

---

## 6. 当前意义

one-exponent family

\[
2\beta u-\alpha v=5^d
\]

现在只发生在两个 `o(T)` complementary divisors 之间，而它们的母体 `b_1,Q` 都是 `Theta(T^2)`。

后续应优先利用：

- small-divisor structure of `10^(2d+c)-const`；
- primitive/cyclotomic blocks forced into the large selected factors `s,q`；
- contact Q-side lifted block now living inside a selected factor `q>>T` while its complement `v<<T`。

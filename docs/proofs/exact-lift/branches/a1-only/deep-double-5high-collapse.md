# A1 minimal diagonal: double-deep 5-high collapse

> 日期：2026-08-20。依赖 `deep-first-complement-remainder.md`、`deep-moderate-three-pattern.md`、`deep-extreme-height-collapse.md`。当前范围 `k=g>=31`。

本文证明 double-deep 中所有 5-adic high branches 都为空。

`deep-extreme-height-collapse.md` 已经关闭 5-extreme；本文进一步关闭 moderate 5-high，也就是此前三模板中的 `LH`。

最终：

\[
\boxed{\text{double-deep 不存在任何 5-high candidate}.}
\]

因此 moderate double-deep 只剩 `LL` 与 `HL`，二者都在 5-low，并统一满足

\[
\boxed{B+2\nu_5=v_5(r)\le10.}
\]

状态：**已严格完成。**

---

## 1. moderate `LH` 的 5-adic depth

在 moderate double-deep 中有

\[
196000<r<15214000,
\qquad v_5(r)\le10.
\]

`LH` 模板由 `deep-moderate-three-pattern.md` 给出

\[
\boxed{B=2k+3-v_5(r).}
\tag{1}
\]

记

\[
Y:=B+\nu_5=v_5(MDN_0).
\]

则由 `v_5(r)<=10`：

\[
\boxed{Y\ge2k-7.}
\tag{2}
\]

另一方面 `deep-complement-height.md` 已证明所有 double-deep 都满足

\[
\boxed{B+\nu_5<3k,}
\]

所以

\[
\boxed{Y<3k.}
\tag{3}
\]

---

## 2. first remainder 必须承载全部 5-adic depth

在 double-deep 中 `lambda=1`。`deep-first-complement-remainder.md` 给出

\[
MDN_0=1000T^3+R_1,
\]

以及

\[
\boxed{14300T<R_1<390100T.}
\tag{4}
\]

第一项满足

\[
v_5(1000T^3)=3k+3.
\]

由 (3)：

\[
Y<3k<3k+3.
\]

所以 `MDN_0` 的较浅 5-adic valuation 不可能来自 `1000T^3`，而必须由 `R_1` 精确承担：

\[
\boxed{v_5(R_1)=Y.}
\tag{5}
\]

特别地

\[
\boxed{5^Y\mid R_1.}
\tag{6}
\]

---

## 3. real size 与 `5^Y` 矛盾

由 (2)：

\[
5^Y\ge5^{2k-7}.
\]

而

\[
\frac{5^{2k-7}}{T}
=
\frac{5^{2k-7}}{2^k5^k}
=
\frac1{5^7}\left(\frac52\right)^k.
\]

在 `k=31`：

\[
\frac1{5^7}\left(\frac52\right)^{31}
>27,000,000
>390100.
\]

该比值以后每增加一个 `k` 再乘 `5/2>1`。因此对所有 `k>=31`：

\[
\boxed{5^{2k-7}>390100T.}
\tag{7}
\]

结合 (4)、(6)：

\[
0<R_1<390100T<5^Y,
\qquad 5^Y\mid R_1,
\]

矛盾。

所以

\[
\boxed{\text{moderate LH 完全为空}.}
\tag{8}
\]

---

## 4. 所有 5-high double-deep 均为空

5-adic high branch 只有两种来源：

1. moderate `LH`；
2. 5-extreme。

本文关闭第一种；`deep-extreme-height-collapse.md` 已关闭第二种。因此

\[
\boxed{\text{double-deep 中所有 5-high states 为空}.}
\tag{9}
\]

于是 moderate double-deep 只剩

\[
\boxed{LL\cup HL.}
\]

两者都处于 5-low。由 `deep-moderate-three-pattern.md` 的 low formula：

\[
\boxed{B+2\nu_5=v_5(r)\le10.}
\tag{10}
\]

特别地

\[
\boxed{B\le10.}
\tag{11}
\]

所以整个 moderate double-deep 的 5-denominator 已被压入十层绝对有限带。

---

## 5. 当前 double-deep 核心

此前 double-deep 的五模板为

\[
LL,\ LH,\ HL,\ E_2,\ E_5.
\]

现在：

- `LH`：本文关闭；
- `E_5`：`deep-extreme-height-collapse.md` 关闭；
- high-high：`deep-balanced-collapse.md` 关闭。

因此只剩

\[
\boxed{LL\cup HL\cup E_2.}
\]

也就是说所有尚存 double-deep 都是 **5-low**；2-side 才是唯一还可能发生 high / extreme 的方向。
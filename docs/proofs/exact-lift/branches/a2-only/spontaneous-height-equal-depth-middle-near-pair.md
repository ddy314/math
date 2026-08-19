# A2 serial middle carrier 的 short near-pair

> **依赖：** `spontaneous-height-equal-depth-serial-tropical-bridge.md`。
>
> **严格状态：**本文把 serial middle carrier `C_BE` 再改写为两项 close pair。定义 `A_P=4K^2-36K+55` 与 `C_-=A_P beta-b_3P`，则 `C_BE=A_P beta+b_3P`，两者只相差 `2b_3P=O(TN^2)`，但都处在 `839..843` 的 `TN^3` 短窗口。对每一个 genuine deep equal-depth target，`C_BE` 至少有 `h+1` 层，而 `C_-` 精确只有 `h` 层。于是 first tropical node有一个完全 natural 的 `deep/exact` near-pair。本文不利用该 pair 完成 modulus-height contradiction，因此不关闭 A2。

---

## 1. exact close-pair decomposition

沿用

\[
P=6K^2-36K+55,
\qquad
F_{\rm dec}=TQ+2b_3,
\qquad
\beta=TQ+b_3,
\]

\[
C_{BE}=F_{\rm dec}P-2K^2\beta.
\]

定义

\[
\boxed{A_P:=4K^2-36K+55=P-2K^2.}
\tag{1.1}
\]

因为

\[
F_{\rm dec}P-2K^2\beta
=(TQ+2b_3)P-2K^2(TQ+b_3),
\]
直接整理得到

\[
\boxed{
C_+:=C_{BE}=A_P\beta+b_3P.}
\tag{1.2}
\]

定义 conjugate

\[
\boxed{
C_-:=A_P\beta-b_3P.}
\tag{1.3}
\]

于是

\[
\boxed{C_+-C_-=2b_3P,}
\tag{1.4}
\]

\[
\boxed{C_++C_-=2A_P\beta.}
\tag{1.5}
\]

所以 `(C_+,C_-)` 是一个完全由真实 decimal/prefix quantities构成的 close pair。

---

## 2. target local units

固定 genuine deep equal-depth target `p`：

\[
v_p(P)=v_p(\beta)=h\ge1.
\]

当前 separation给

\[
p\nmid2Kb_3.
\]

又由 `p|P` 与 (1.1)：

\[
A_P\equiv-2K^2\pmod p,
\]
所以

\[
\boxed{p\nmid A_P.}
\tag{2.1}
\]

因此两项

\[
A_P\beta,
\qquad
b_3P
\]
都具有精确赋值

\[
\boxed{h.}
\tag{2.2}
\]

serial bridge 已证明

\[
v_p(C_+)=h+c_p,
\qquad
c_p\ge1.
\]

所以

\[
\boxed{v_p(C_+)\ge h+1.}
\tag{2.3}
\]

---

## 3. conjugate is exact baseline for every deep target

写

\[
A_P\beta=p^hu,
\qquad
b_3P=p^hv,
\]
其中 `u,v` 为 `p`-units。

由 (1.2)、(2.3)：

\[
u+v\equiv0\pmod p.
\]

所以

\[
u-v\equiv-2v\not\equiv0\pmod p
\]
因为 `p` 为 odd。由 (1.3)：

\[
\boxed{v_p(C_-)=h.}
\tag{3.1}
\]

这是无条件的 deep-target exactness，不要求 first-node strict-extra。

因此：

\[
\boxed{
\begin{array}{c|c}
\text{carrier}&p\text{-depth}\\ \hline
C_+&h+c_p\ge h+1\\
C_-&h.
\end{array}}
\tag{3.2}
\]

若进一步处在 first-node strict-extra

\[
r_B=h<\rho_p,
\qquad
r_+>h,
\]
serial bridge给 `c_p>h`，所以

\[
\boxed{v_p(C_+)>2h,\qquad v_p(C_-)=h.}
\tag{3.3}
\]

---

## 4. same short Archimedean window

serial bridge已有

\[
839TN^3<C_+<843TN^3.
\tag{4.1}
\]

又 dual-short carrier 已给

\[
0<P<600N^2,
\]
以及

\[
0<b_3<\frac{843}{1000}T.
\]

由 (1.4)：

\[
0<C_+-C_-=2b_3P
<\frac{2\cdot843\cdot600}{1000}TN^2
<1012TN^2.
\tag{4.2}
\]

因为 `N>=10^11`，serial bridge 的实际 lower margin大于 `0.328 TN^3`，而 (4.2) 小于 `1.012*10^-8 TN^3`。因此仍有

\[
\boxed{839TN^3<C_-.}
\tag{4.3}
\]

显然 `C_-<C_+<843TN^3`，故

\[
\boxed{
839TN^3<C_-<C_+<843TN^3.}
\tag{4.4}
\]

特别地两者都为正，且都恰有

\[
\boxed{m+3M+3}
\]
个十进制数字。

---

## 5. relative gap

由 (1.4)、(4.2)、(4.4)：

\[
\boxed{
0<C_+-C_-<1012TN^2,}
\tag{5.1}
\]
而两者都大于 `839TN^3`。因此

\[
\boxed{
0<\frac{C_+-C_-}{C_-}
<\frac{1012}{839N}.}
\tag{5.2}
\]

所以 pair 的相对距离是 `O(10^{-M})`。

---

## 6. current use

`C_+/C_-` 给 first serial node 一个和此前 `E_+/E_-` 类似但更短的 natural pair：

- same decimal length；
- relative gap `O(1/N)`；
- target prime在 actual sheet `C_+` 至少多一层；
- conjugate `C_-` 对所有 deep target精确只有 baseline `h`。

因此 first-node higher cancellation不再需要通过抽象 normalized units描述；它已经有一个 short natural near-pair可用于后续 gcd、modulus-height 或 parity allocation。

A2 仍为 `待证`。

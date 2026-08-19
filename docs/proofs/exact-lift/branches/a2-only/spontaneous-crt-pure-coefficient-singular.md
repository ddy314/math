# A2 pure-spontaneous descendant coefficient singularity 只剩 projective ratio gates

> **依赖：** `spontaneous-crt-pure-prefix-elimination.md`、`spontaneous-single-branch.md`。
>
> **严格状态：**generic pure-spontaneous descendant compatibility在 branch quadratic 上降成 `A_63 tau+B_63=0`；只有 `A_63=B_63=0` 时 decimal phase不能被唯一恢复。本文直接消去 prefix norm ratio `c`，证明 coefficient-singular locus分解成两个只依赖 projective ratio `u=z/s=a_3/(TK)` 的齐次 gate `H_4,H_24`，次数分别 4 与24。因此 singular coefficient branch不会重新长回二维 local family；它只是一维 ratio bad locus。本文不排除这些 finite-field ratio roots，因此不关闭 A2。

---

## 1. branch remainder

沿用 compact single-branch variables

\[
s=9+y,
\qquad z=z_i(x,y),
\]

\[
c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2},
\qquad
\tau=10^{-M}.
\]

universal descendant cubic modulo branch quadratic给 primitive linear remainder

\[
\boxed{
\widetilde E_{63}
\equiv A_{63}(s,z,c)\tau+B_{63}(s,z,c)
\pmod{L_z}.}
\tag{1.1}

已有

\[
\deg A_{63}=7,
\qquad A_{63}\text{ 有 }20\text{ 项},
\]

\[
\deg B_{63}=8,
\qquad B_{63}\text{ 有 }24\text{ 项}.
\]

在

\[
A_{63}\not\equiv0\pmod p
\]
时

\[
\tau\equiv-B_{63}A_{63}^{-1}\pmod p
\]
唯一，所以只需单列 coefficient-singular branch

\[
\boxed{A_{63}=B_{63}=0.}
\tag{1.2}

---

## 2. eliminate `c`

把 `A_63,B_63` 看成 `c` 的多项式：

\[
\deg_c A_{63}=3,
\qquad
\deg_c B_{63}=4.
\]

直接求 resultant并取 primitive part，得到完全因子化：

\[
\boxed{
\operatorname{Res}_c(A_{63},B_{63})
=2^{72}3^{32}5^9 11^9\,
H_4(s,z)H_{24}(s,z).}
\tag{2.1}

这里

\[
\boxed{
\begin{aligned}
H_4(s,z)={}&31476144004s^4
+114775877404s^3z\\
&+90353275489s^2z^2
-46902675456sz^3\\
&-29520930816z^4,
\end{aligned}}
\tag{2.2}

而 `H_24` 是 primitive homogeneous degree-24 polynomial，恰有25个 nonzero monomials。

完整 `H_24` coefficients由 checker从 `A_63,B_63` 直接重建并验证 factorization；正文不重复塞入机械大整数。

当前 genuine pure-spontaneous prime已排除 fixed coefficient primes `2,3,5,11`，所以 (2.1) 给严格必要条件

\[
\boxed{
A_{63}=B_{63}=0
\Longrightarrow
H_4(s,z)=0
\quad\text{或}\quad
H_{24}(s,z)=0.}
\tag{2.3}

---

## 3. both gates are projective

`H_4,H_24` 都是齐次式：

\[
H_4(s,z)=s^4 h_4(z/s),
\]

\[
H_{24}(s,z)=s^{24}h_{24}(z/s).
\]

而 genuine branch中 `s` 是 unit。因此 coefficient singularity只依赖

\[
\boxed{u:=z/s.}
\tag{3.1}

真实意义上

\[
u=rac{\bar\zeta}{9+y}
=rac{a_3}{TK}.}
\tag{3.2}

所以原来可能看似依赖

\[
(s,z,c,\tau)
\]
四个坐标的 singular coefficient condition，实际上已降成一个单 projective ratio 的 finite-field root问题。

---

## 4. low-degree ratio gate

令 `s=1,z=u`，低次 gate为

\[
\boxed{
\begin{aligned}
h_4(u)={}&
-29520930816u^4
-46902675456u^3\\
&+90353275489u^2
+114775877404u\\
&+31476144004.
\end{aligned}}
\tag{4.1}

其 discriminant support为

\[
\boxed{
2^{21}3^{13}5^{13}7^6 11^{12}13^3 19\,29^2\,163\,
6661944924691447.}
\tag{4.2}

本文只记录该 bad-prime support，不把 discriminant character误当作 generic closure：simple roots of `h_4` 仍可存在于其它 primes。

真实 roots约为

\[
-2.273557786\ldots,
\qquad
1.718575838\ldots,
\]

另有一对非实共轭根。该 real information只用于后续 Archimedean audit，不是 modular exclusion。

---

## 5. no renewed Hensel dimension

因此 pure-spontaneous descendant branch的 local structure现在严格分成：

### generic coefficient

\[
A_{63}\ne0:
\quad
\boxed{\tau=-B_{63}/A_{63}}
\]
唯一，随后 `C/D` 也由 descendant defect map唯一恢复。

### coefficient singular

\[
A_{63}=0:
\]
common compatibility还要求 `B_63=0`，从而

\[
\boxed{h_4(u)=0\quad\text{或}\quad h_{24}(u)=0.}
\]
只剩一维 projective ratio root。

所以 coefficient singularity不会重新产生一个自由 `(tau,c)` Hensel sheet；其维数已经被 resultant压缩。

---

## 6. next use

后续最值得做的是：

1. 把 `h_4/h_24` 与两张 explicit sphere ratio `u_i=z_i/(9+y)` 联立；
2. 或对 generic `A_63!=0` 分支把 `tau=-B/A` 清成 natural decimal representative，与 `tau=10^{-M}` 的 orbit做高度/符号同步。

单独继续审 `h_4/h_24` 的 ordinary discriminant不会自动关闭 simple roots。

A2 仍为 `待证`。

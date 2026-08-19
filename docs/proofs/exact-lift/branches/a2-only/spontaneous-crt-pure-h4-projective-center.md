# A2 `H_4` coefficient-singular component 的 fixed projective norm center

> **依赖：** `spontaneous-crt-pure-coefficient-singular.md`、`spontaneous-crt-pure-h4-prefix.md`、`spontaneous-single-branch.md`。
>
> **严格状态：**低次 coefficient-singular component满足 `h_4(u)=0`, `u=z/s`。本文继续把 `A_63=B_63=0` projectivize，令 `v=c/s^2`。关于 `v` 的 subresultant在 quotient ring modulo `h_4` 中精确退化成 `C_4(u)(1296v-3097)`。因此除一个固定 coefficient-exception resultant外，所有 `H_4` singular roots都强迫同一个 projective norm ratio `v=3097/1296 mod p`。真实 endpoint却有 `0<v<21/20`，所以该 singular component与真实 norm ratio存在统一 Archimedean gap，只能通过 p-adic wrapping实现。本文保留固定 coefficient exceptions，不关闭 A2。

---

## 1. projectivize the coefficient equations

coefficient-singular branch为

\[
A_{63}(s,z,c)=0,
\qquad
B_{63}(s,z,c)=0.
\]

两式是 weighted homogeneous，其中

\[
\deg s=\deg z=1,
\qquad
\deg c=2.
\]

在 genuine branch中 `s` 为 unit，所以定义

\[
\boxed{u:=z/s,}
\qquad
\boxed{v:=c/s^2.}
\tag{1.1}

除去 `s^7,s^8`，得到

\[
a(u,v)=0,
\qquad
b(u,v)=0,
\]
其中

\[
\deg_v a=3,
\qquad
\deg_v b=4.
\]

低次 resultant component为

\[
\boxed{h_4(u)=0,}
\tag{1.2}

其中 `h_4` 为前一文件的 irreducible quartic。

---

## 2. the final `v`-subresultant is linear

对 `a,b` 关于 `v` 取 subresultant sequence。最后一个非零的正次数 subresultant次数恰为 `1`：

\[
S_1(u,v)=A_1(u)v+B_1(u).
\]

现在在 quotient

\[
\mathbf Q[u]/(h_4)
\]
中把两个 coefficient降到 degree `<4`。exact computation给

\[
\boxed{
1296B_1(u)+3097A_1(u)
\equiv0\pmod{h_4(u)}.}
\tag{2.1}

而 `A_1 mod h_4` 是一个 nonzero fixed scalar乘一个 primitive cubic `C_4(u)`：

\[
\boxed{
A_1(u)\equiv\kappa\,C_4(u)\pmod{h_4},}
\qquad \kappa\in\mathbf Q^\times.
\tag{2.2}

`C_4` 的完整大整数 coefficients由 checker重建；这里只需要其次数

\[
\boxed{\deg C_4=3.}
\tag{2.3}

因此 modulo `h_4`：

\[
\boxed{
S_1(u,v)
\equiv
\frac{\kappa C_4(u)}{1296}
(1296v-3097).}
\tag{2.4}

---

## 3. fixed coefficient-exception integer

定义固定 nonzero integer

\[
\boxed{
\mathfrak E_4
:=\operatorname{Res}_u(h_4,C_4).}
\tag{3.1}

它是一个 315 位整数。其显式已知 small-prime content为

\[
\boxed{
2^{84}3^{83}5^{13}7^{11}11^{12}13^{40}29^2}
\tag{3.2}

乘一个固定 171 位余因子。

本文不需要把该余因子完全分解；所有

\[
p\mid\mathfrak E_4
\]
只是**有限 coefficient exceptions**，应按 fixed-prime audit处理，而不是混进 generic moving branch。

若

\[
p\nmid2\cdot3\cdot\mathfrak E_4
\]
且 `h_4(u)=0`，则 `C_4(u)` 为 unit。由 `A=B=0` 与 (2.4)：

\[
\boxed{
1296v-3097\equiv0\pmod p.}
\tag{3.3}

所以 generic low singular component具有 universal projective center

\[
\boxed{
\frac{c}{s^2}
\equiv\frac{3097}{1296}\pmod p.}
\tag{3.4}

---

## 4. the real endpoint ratio is below `21/20`

真实 ratio为

\[
\boxed{
 v_{real}
=
\frac{(x+2)^2(2025x^2+y^2)}
{100x^2(9+y)^2}.}
\tag{4.1}

endpoint box：

\[
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1.
\]

粗但严格地：

\[
(x+2)^2<\left(\frac{40}{19}\right)^2,
\]

\[
2025x^2+y^2
<2025\left(\frac2{19}\right)^2+1
=\frac{8461}{361},
\]

\[
100x^2>1,
\qquad
(9+y)^2>\left(\frac{2499}{250}\right)^2.
\]

因此

\[
\boxed{
0<v_{real}
<\frac{846100000000}{813854775321}
<\frac{21}{20}.}
\tag{4.2}

另一方面

\[
\boxed{
\frac{3097}{1296}>\frac{119}{50}>2.38.}
\tag{4.3}

所以 generic `H_4` projective center与真实 endpoint严格分离：

\[
\boxed{
\frac{3097}{1296}-v_{real}
>\frac{119}{50}-\frac{21}{20}
=\frac{133}{100}.}
\tag{4.4}

至少有 `1.33` 的固定实数 gap。

---

## 5. interpretation

除 fixed coefficient exceptions `p|E_4` 外，`H_4` coefficient singularity不再是一条任意 ratio curve：

\[
\boxed{
 h_4(u)=0,
\qquad
 v=3097/1296.}
\tag{5.1}

因此它同时固定 third/prefix projective direction和 prefix norm projective scale。

真实 endpoint中 `v<1.05`，而 modular center是 `>2.38`。故任何 surviving generic root必须依赖真正的 p-adic wrapping；没有 real-near singular degeneration。

这仍不是 global contradiction，因为 congruence不要求实数接近。下一步若要关闭 `H_4` branch，应把 fixed gap (4.4) 与清分母 natural numerator的 required p-depth联立，或逐个审计 `E_4` 的 finite coefficient primes。

A2 仍为 `待证`。

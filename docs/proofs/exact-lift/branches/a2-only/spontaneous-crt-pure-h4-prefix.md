# A2 coefficient-singular `H_4` 产生两张新的 irreducible pure-prefix curves

> **依赖：** `spontaneous-crt-pure-coefficient-singular.md`、`spontaneous-sphere-roots.md`、`spontaneous-prefix-branch-audit.md`。
>
> **严格状态：**coefficient-singular branch `A_63=B_63=0` 的低次 projective gate为 quartic `h_4(u)=0`, `u=z/s`。本文把两张 explicit sphere ratio `u_i=z_i/(9+y)` 代入，清分母后得到两张只含 `(x,y)` 的 primitive curves。它们分别 degree 32/40，在 `Q[x,y]` 中均不可约，并且与所有主要旧 prefix collision gates `A_sp,A_+,A_-,Delta_0,225x^2-y,C_*` 两两互素。因此 `h_4` singularity不是旧 source/common-alpha/central/prefix-defect shadow，而是一条 genuinely new pure-prefix bad locus。本文不排除其 finite-field roots，因此不关闭 A2。

---

## 1. projective quartic

前一文件得到

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
\tag{1.1}

coefficient-singular branch若进入低次 component，必须

\[
\boxed{h_4(z/s)=0,}
\qquad
s=9+y.
\tag{1.2}

两张 sphere roots为

\[
\boxed{
z_1=-\frac{A_+A_{sp}}
{400x^2y^3(x+2)^2},}
\tag{1.3}

\[
\boxed{
z_2=\frac{A_{sp}G_*}
{400x^2y^3(x+2)^2\Delta_0}.}
\tag{1.4}

所有 denominator在 genuine pure-spontaneous sector中为 units。

---

## 2. branch-specific primitive numerators

定义

\[
\boxed{
\mathscr S_{4,i}(x,y)
:=\operatorname{primnum}
 h_4\!\left(\frac{z_i(x,y)}{9+y}\right),
\qquad i=1,2.}
\tag{2.1}

exact expansion给：

\[
\boxed{
\deg\mathscr S_{4,1}=32,
\qquad
\#\operatorname{supp}(\mathscr S_{4,1})=137,}
\tag{2.2}

\[
\boxed{
\deg\mathscr S_{4,2}=40,
\qquad
\#\operatorname{supp}(\mathscr S_{4,2})=272.}
\tag{2.3}

两者 integer content均为 `1`，所以已经 primitive。

完整 coefficients由 checker从 (1.1),(1.3),(1.4) 重建；正文不手抄数百项。

---

## 3. both prefix curves are irreducible over `Q`

对两张 primitive numerator做 exact multivariate factorization：

\[
\boxed{
\mathscr S_{4,1}\text{ 在 }\mathbf Q[x,y]\text{ 中不可约},}
\tag{3.1}

\[
\boxed{
\mathscr S_{4,2}\text{ 在 }\mathbf Q[x,y]\text{ 中不可约}.}
\tag{3.2}

因此低次 ratio singularity没有继续分裂成一堆旧小 gate；每张 sphere orientation只产生一张真正的 irreducible prefix curve。

这不表示它们在有限域中无根；这里只是结构独立性结论。

---

## 4. gcd audit against all principal old prefix gates

沿用旧 objects：

\[
d=225x^2-y,
\]

\[
A_{sp}=4d^2-xy^2(99x-4),
\]

\[
A_-=A_{sp}-2y^2(x+2)^2,
\]

\[
A_+=202500x^4+99x^2y^2-4xy^2-4y^2,
\]

\[
\Delta_0=2025x^2-18y-y^2,
\]
以及 branch-collision central kernel

\[
\begin{aligned}
C_*={}&164025x^4+656100x^3
+2381x^2y^2+41400x^2y\\
&+842400x^2+324xy^2+324y^2.
\end{aligned}
\]

对每个

\[
F\in\{d,A_{sp},A_-,A_+,\Delta_0,C_*\}
\]
exact polynomial gcd均给

\[
\boxed{
\gcd(\mathscr S_{4,1},F)
=\gcd(\mathscr S_{4,2},F)=1.}
\tag{4.1}

所以 `H_4` singular curves不是以下任何旧 mechanism 的 component：

- source line `d=0`；
- spontaneous coefficient degeneration `A_sp=0`；
- common-alpha branch `A_-=0`；
- sphere numerator factor `A_+=0`；
- prefix norm defect `Delta_0=0`；
- central branch collision `C_*=0`。

---

## 5. source-line restriction as an independent sanity audit

虽然 genuine branch已排除 source line，仍可把

\[
y=225x^2
\]
作为 independence sanity check。

此时两张 sphere roots合并为

\[
z_1=z_2
=\frac{9x^2(99x-4)^2}{16(x+2)^2}.
\]

将 full pure-prefix descendant resultant限制到该 line，并 primitive factor，可见一个显式 factor

\[
\boxed{(25x^2+1)^5.}
\tag{5.1}

对 inert prime `p=3 mod4`，`25x^2+1=0` 会强迫 `-1` 为平方，因此该 factor本身无 genuine inert root。

剩余还有一个 degree-8 与一个 degree-30 factor，所以 full descendant prefix carrier并不在 source line上恒等消失。这再次确认新 compatibility不是旧 source equation的重写。

本文不把 source-line剩余 factors计入 genuine branch obstruction，因为该 line本来已经由 prime-source separation排除。

---

## 6. revised coefficient-singular frontier

coefficient singularity现在严格分成：

1. low ratio component `h_4=0`：两张新 irreducible prefix curves `S_{4,1},S_{4,2}`；
2. high ratio component `h_24=0`：尚未做 branch-specific factorization。

所以 generic decimal-phase recovery失败的低次部分已经完全转化为两个 independent pure-prefix bad loci；它不会回流到任何已知 boundary/collision gate。

下一步若继续 singular side，应对 `h_24` 做同样 gcd/factor audit；若继续 generic side，则应使用 `X_{63,i}^{pref}` 的 natural representative/prime-product budget。

A2 仍为 `待证`。

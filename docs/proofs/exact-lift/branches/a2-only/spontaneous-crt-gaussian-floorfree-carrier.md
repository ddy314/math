# A2 CRT/Gaussian orientation 的 floor-free integer carrier

> **依赖：** `spontaneous-crt-gaussian-slot-orientation.md`、`endpoint-lattice.md` §§16.33–16.38。
>
> **严格状态：**前一文件用 `Q_Delta=floor(Delta_+/(D^2-C^2))` 构造 normalized orientation reader。本文直接在未取 floor 的 real quotient上乘回全部 lattice scale与 CRT modulus，得到 ordinary integer `P_Delta=2^{A_G}Delta_+-5^{B_G}k_h^3(D^2-C^2)`。其符号与 Gaussian high-factor side完全等价，并且距离零有固定相对 margin。因此 Gaussian side已经可由 additive exact gap `Delta_+` 本身读取，不依赖 Euclidean quotient的取整误差。本文不单独关闭 A2。

---

## 1. lattice exponents

定义

\[
\boxed{
A_G:=\frac{M+5\eta}{2}+8,
\qquad
B_G:=3M-d-\eta-3.}
\tag{1.1}
\]

在 reflection high-2 lattice 中二者均为正整数。

前一文件已证明，对 real CRT quotient

\[
Y_\Delta:=\frac{\Delta_+}{D^2-C^2}
\]
有

\[
\boxed{
\mathcal Y_{\Delta,G}
:=\frac{2^{A_G}}{5^{B_G}k_h^3}Y_\Delta
=
\frac{1000s^2x^2}{\sigma_\varepsilon^3}\Psi_\Delta.}
\tag{1.2}
\]

这里所有量均为正，且

\[
\frac1{17}<\Psi_\Delta<\frac{1001}{15000}.
\]

---

## 2. define the floor-free integer

定义

\[
\boxed{
\mathscr P_\Delta
:=
2^{A_G}\Delta_+
-5^{B_G}k_h^3(D^2-C^2).}
\tag{2.1}
\]

`Delta_+,D,C,k_h` 均为整数，所以 `P_Delta` 是 ordinary integer。

直接除以正整数

\[
5^{B_G}k_h^3(D^2-C^2)
\]
得到 exact identity

\[
\boxed{
\frac{\mathscr P_\Delta}
{5^{B_G}k_h^3(D^2-C^2)}
=
\mathcal Y_{\Delta,G}-1.}
\tag{2.2}
\]

因此其符号完全由未取 floor 的 Gaussian-normalized CRT quotient决定。

---

## 3. minus side is uniformly positive

前一文件的 raw bound给

\[
\frac{44}{25}
<\mathcal Y_{\Delta,G}
<\frac{12}{5}
\qquad(\varepsilon=-1).
\]

由 (2.2)：

\[
\boxed{
\frac{19}{25}
<
\frac{\mathscr P_\Delta}
{5^{B_G}k_h^3(D^2-C^2)}
<\frac75.}
\tag{3.1}
\]

特别地

\[
\boxed{
\varepsilon=-1
\Longrightarrow
\mathscr P_\Delta>0.}
\tag{3.2}
\]

---

## 4. plus side is uniformly negative

同理，plus side有

\[
\frac{51}{100}
<\mathcal Y_{\Delta,G}
<\frac7{10}
\qquad(\varepsilon=+1).
\]

所以

\[
\boxed{
-\frac{49}{100}
<
\frac{\mathscr P_\Delta}
{5^{B_G}k_h^3(D^2-C^2)}
<-\frac3{10}.}
\tag{4.1}
\]

特别地

\[
\boxed{
\varepsilon=+1
\Longrightarrow
\mathscr P_\Delta<0.}
\tag{4.2}
\]

两侧距离零都有绝对常数 margin；这里完全没有 floor correction。

---

## 5. exact orientation equivalence

high factor只有 `epsilon=±1` 两侧，所以 §§3–4 合并为

\[
\boxed{
\operatorname{sgn}(\mathscr P_\Delta)=-\varepsilon.}
\tag{5.1}
\]

即

\[
\boxed{
\varepsilon=-1
\iff\mathscr P_\Delta>0,
\qquad
\varepsilon=+1
\iff\mathscr P_\Delta<0.}
\tag{5.2}
\]

因此

\[
\boxed{\mathscr P_\Delta\ne0.}
\tag{5.3}
\]

由于 `D` 为偶数、`C` 为奇数，`D^2-C^2` 为奇数；`k_h` 也为奇数，而 `A_G>=1`。所以 (2.1) 的第一项为偶数、第二项为奇数：

\[
\boxed{\mathscr P_\Delta\equiv1\pmod2.}
\tag{5.4}
\]

这是一个 nonzero odd signed integer carrier。

---

## 6. relation to the quotient carrier

令 Euclidean remainder

\[
R_\Delta
:=\Delta_+-Q_\Delta(D^2-C^2),
\qquad
0\le R_\Delta<D^2-C^2.
\tag{6.1}
\]

前一文件定义

\[
\mathscr O_\Delta
:=2^{A_G}Q_\Delta-5^{B_G}k_h^3.
\]

于是 exact 有

\[
\boxed{
\mathscr P_\Delta
=(D^2-C^2)\mathscr O_\Delta
+2^{A_G}R_\Delta.}
\tag{6.2}
\]

所以 `P_Delta` 是 quotient sign carrier的 floor-free parent。真正的 additive data位于 `P_Delta`：它直接使用 exact gap `Delta_+`，而不是先做 Euclidean division。

---

## 7. interface with the centered Hensel sign

`spontaneous-crt-hensel-sign-bridge.md` 使用

\[
\operatorname{sgn}(\chi_E)
=\operatorname{sgn}(\varepsilon z_E),
\qquad z_E\ne0.
\]

由 (5.1) 可直接把 `O_Delta` 替换为更自然的 `P_Delta`：

\[
\boxed{
\mathscr P_\Delta\,z_E\,\chi_E<0.}
\tag{7.1}
\]

因此 CRT exact gap、Gaussian side和 centered Hensel kernel现在共享一个完全 floor-free 的 signed integer interface。

后续若 additive CRT residue / natural representative能独立推出 `P_Delta z_E chi_E>0`，即直接形成矛盾。

A2 仍为 `待证`。

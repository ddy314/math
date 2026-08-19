# A2 floor-free carrier 与 CRT modulus 的 adjacent-contact overlap

> **依赖：** `spontaneous-crt-gaussian-floorfree-carrier.md`、`spontaneous-crt-quotient-source-scale.md`、`endpoint-lattice.md` §§16.33–16.38。
>
> **严格状态：**当 `|P_Delta|≡3 mod4` 时，它产生新的 odd-inert parity；CRT modulus `D^2-C^2` 本身也为 `3 mod4`。本文审计两份 parity能否由同一 prime复用。由于 `P_Delta` 模 CRT modulus只剩 `2^{A_G}Delta_+`，common gcd精确等于 `gcd(Delta_+,D^2-C^2)`。利用 `D Delta_+` 的显式整数式，在 `D-C`、`D+C` 两张互素 denominator sheet上得到 exact divisibility decompositions：任何 common prime的完整 exponent必须进入两个固定-sign adjacent contact carrier `F_2` 或 `F_4`。二者绝对值都只有约 `50 c_u^2 T N^2`。因此 parity reuse要么分裂成不同 residual primes，要么支付给这两个短 contact carriers之一。本文不证明 `F_2,F_4` 无 genuine roots，因此不关闭 A2。

---

## 1. common gcd reduces to the right gap

定义

\[
M_\Delta:=D^2-C^2=(D-C)(D+C).
\]

`D` 为偶、`C` 为奇，所以 `M_Delta` 为 positive odd integer，并且

\[
\gcd(D-C,D+C)=1.
\tag{1.1}
\]

floor-free carrier为

\[
\mathscr P_\Delta
=2^{A_G}\Delta_+-5^{B_G}k_h^3M_\Delta.
\]

因为 `M_Delta` 为 odd，`2^{A_G}` 在其每个 prime factor上为 unit。因此

\[
\boxed{
\gcd(\mathscr P_\Delta,M_\Delta)
=\gcd(\Delta_+,M_\Delta).}
\tag{1.2}
\]

并且由 (1.1)：

\[
\boxed{
\gcd(\Delta_+,M_\Delta)
=\gcd(\Delta_+,D-C)\,\gcd(\Delta_+,D+C).}
\tag{1.3}
\]

两因子互素。

---

## 2. exact integer formula for `D Delta_+`

沿用

\[
N_s:=3D-C.
\]

已有

\[
\boxed{
\begin{aligned}
D\Delta_+
={}&c_u^2\Bigl[
D^2(TK^2-14KT-4Ka_3+37T+14a_3)\\
&+DN_s(-2KT+7T+2a_3)+TN_s^2
\Bigr]\\
&-z^2N_s(TN_s+2a_3D).
\end{aligned}}
\tag{2.1}
\]

该式是下面两张 denominator sheet 的 complete natural representative。

---

## 3. `D-C` sheet: full common depth enters `F_2`

定义

\[
\boxed{
\begin{aligned}
F_2:={}&
c_u^2[TK^2-(18T+4a_3)K+55T+18a_3]\\
&-4z^2(T+a_3).
\end{aligned}}
\tag{3.1}
\]

直接展开 (2.1) 得 exact decomposition

\[
\boxed{
D\Delta_+
=D^2F_2+(C-D)R_2,}
\tag{3.2}
\]

其中

\[
\boxed{
\begin{aligned}
R_2={}&CT(c_u^2-z^2)
+2DKTc_u^2-12DTc_u^2+5DTz^2\\
&-2Da_3c_u^2+2Da_3z^2.
\end{aligned}}
\tag{3.3}
\]

固定 odd prime `p` 且

\[
p^k\mid\Delta_+,
\qquad
p^k\mid D-C.
\]

由 `gcd(C,D)=1`，若 `p|D-C` 则 `p∤D`。因此 (3.2) 给

\[
\boxed{p^k\mid F_2.}
\tag{3.4}
\]

注意这是完整 common exponent `k`，不是只读 first layer。

---

## 4. `D+C` sheet: full common depth enters `F_4`

定义

\[
\boxed{
\begin{aligned}
F_4:={}&
c_u^2[TK^2-(22T+4a_3)K+81T+22a_3]\\
&-8z^2(2T+a_3).
\end{aligned}}
\tag{4.1}
\]

同样 exact 展开：

\[
\boxed{
D\Delta_+
=D^2F_4+(C+D)R_4,}
\tag{4.2}
\]

其中

\[
\boxed{
\begin{aligned}
R_4={}&CT(c_u^2-z^2)
+2DKTc_u^2-14DTc_u^2+7DTz^2\\
&-2Da_3c_u^2+2Da_3z^2.
\end{aligned}}
\tag{4.3}
\]

因此

\[
p^k\mid\Delta_+,
\qquad p^k\mid D+C
\]
强迫

\[
\boxed{p^k\mid F_4.}
\tag{4.4}
\]

---

## 5. both contact carriers have fixed Archimedean sign

利用 source identity

\[
\frac z{c_u}=\frac{TQ}{b_3}=\frac Qw,
\qquad w:=\frac{b_3}{T},
\tag{5.1}
\]

以及 normalized variables

\[
s:=\frac KN,
\qquad x:=\frac BN,
\qquad \zeta:=\frac{a_3}{T},
\]
有

\[
\frac{F_2}{c_u^2TN^2}
=s^2-rac{(18+4\zeta)s}{N}
+rac{55+18\zeta}{N^2}
-4\left(\frac{2+x}{w}\right)^2(1+\zeta),
\tag{5.2}
\]

\[
\frac{F_4}{c_u^2TN^2}
=s^2-rac{(22+4\zeta)s}{N}
+rac{81+22\zeta}{N^2}
-8\left(\frac{2+x}{w}\right)^2(2+\zeta).
\tag{5.3}
\]

当前 endpoint box为

\[
\frac1{10}<x<\frac2{19},
\quad
\frac{2499}{250}<s<10,
\quad
1<\zeta<\frac{251}{250},
\quad
\frac{837}{1000}<w<\frac{843}{1000},
\quad N\ge10^{11}.
\]

直接取端点可得到安全 strict windows

\[
\boxed{
49<\frac{F_2}{c_u^2TN^2}<51,}
\tag{5.4}
\]

\[
\boxed{
48<\frac{-F_4}{c_u^2TN^2}<53.}
\tag{5.5}
\]

所以

\[
\boxed{F_2>0,\qquad F_4<0.}
\tag{5.6}
\]

两张 overlap sheet分别由一个 positive 和一个 negative short natural carrier读取，尺度都只有 `~50 c_u^2 T N^2`。

---

## 6. canonical parity-reuse dichotomy

当

\[
|\mathscr P_\Delta|\equiv3\pmod4
\]
时，`P_Delta` 强迫一份 odd-inert parity；另一方面

\[
M_\Delta=D^2-C^2\equiv3\pmod4
\]
也强迫一份。

定义

\[
G_{PM}:=\gcd(|\mathscr P_\Delta|,M_\Delta).
\]

约去 common gcd：

\[
P_1:=|\mathscr P_\Delta|/G_{PM},
\qquad
M_1:=M_\Delta/G_{PM},
\]
且

\[
\gcd(P_1,M_1)=1.
\]

若

\[
G_{PM}\equiv1\pmod4,
\]
则

\[
P_1\equiv M_1\equiv3\pmod4,
\]
所以两份 parity必须由两个不同 residual primes承担。

若

\[
G_{PM}\equiv3\pmod4,
\]
则 common gcd本身承担 odd-inert parity；而 §§3–4 说明其中每一枚 genuine common prime的完整 exponent都必须进入 `F_2` 或 `F_4`。

因此

\[
\boxed{
\text{`P_Delta` / CRT-modulus parity reuse}
\Longrightarrow
\begin{cases}
\text{two distinct residual inert suppliers},\\
\text{or}\quad
\text{full-depth adjacent contact in }F_2\text{ or }F_4.
\end{cases}}
\tag{6.1}
\]

这把“新 parity是否会被旧 CRT modulus免费复用”改写成一个明确的 short-contact问题。

---

## 7. current frontier

下一步若能证明 genuine inert roots of `F_2,F_4` 只能落在 fixed / already-paid support，四个 `eta=1` parity-active types就会真正获得 distinct-prime surcharge。

目前 `F_2,F_4` 的 quadratic discriminants仍允许 simple moving roots，因此本文不把 short contact误称为空性。它的作用是把 common support从两个大 integers压到两条 explicit adjacent-secant natural representatives。

A2 仍为 `待证`。

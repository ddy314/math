# A2 cross-sign sphere 在 height-1 sheet 上的 exact square shadow

> **依赖：** `spontaneous-cross-sign-sphere.md`、`spontaneous-height-parity-ledger.md`。
>
> **严格状态：**`spontaneous-cross-sign-sphere.md` 已证明 conjugate-angle sphere 的唯一 quadratic extension 为 `v^2=-2X_cross`，并在 height-2 orientation 上给出 `2X_cross=-square`。该文件把 height-1 relative character留作开放项。本文补齐这一项：构造一个 exact integer syzygy，证明在 `H_1=0` 上同样有 `-2X_cross=square`。所以对两张 moving height orientations，cross-sign quadratic character都自动满足；它不能为 moving-height parity提供第二条独立 Legendre obstruction。仅 `X_cross=0` 的 discriminant collision仍需作为 singular intersection单列。

---

## 1. notation

沿用 normalized decimal variables

\[
x=B/N_{\rm dec},
\qquad
y=10A/N_{\rm dec}.
\]

height-1 polynomial为

\[
\boxed{
H_1
=202500x^4+(101x^2+4x+4)y^2.}
\tag{1.1}

定义

\[
\boxed{C_1:=101x^2+4x+4.}
\tag{1.2}

cross-sign sphere的 quadratic polynomial为

\[
\boxed{
\begin{aligned}
X_\times={}&205031250x^6+2025x^4y^2-1822500x^4y\\
&+8100x^3y^2-99x^2y^4-1800x^2y^3\\
&+4050x^2y^2+4xy^4+4y^4.
\end{aligned}}
\tag{1.3}

conjugate-angle sphere有 third-numerator root的 generic inert character gate为

\[
\left(\frac{-2X_\times}{p}\right)=1.
\tag{1.4}

---

## 2. exact square syzygy

定义

\[
\boxed{
S_1
:=90x\left[
225x^2(9x-2)(11x+2)-C_1y
\right].}
\tag{2.1}

再定义整数多项式

\[
\boxed{
\begin{aligned}
Q_1={}&20252025x^6+16200x^5-9999x^4y^2-181800x^4y+48600x^4\\
&+8x^3y^2-7200x^3y+64800x^3\\
&+24x^2y^2-7200x^2y+32400x^2\\
&+32xy^2+16y^2.
\end{aligned}}
\tag{2.2}

直接展开得到 exact identity

\[
\boxed{
S_1^2+2C_1^2X_\times
=2H_1Q_1.}
\tag{2.3}

这条式子在 `Z[x,y]` 中成立，不使用任何 modular root 假设。

---

## 3. genuine height-1 root 上 `C_1` 是 unit

固定 genuine non-`3` inert moving height prime，并假设

\[
H_1=0\pmod p.
\]

若同时 `C_1=0`，由 (1.1) 得

\[
202500x^4=0\pmod p.
\]
对 `p!=2,3,5` 且 external `x` 为 unit不可能。因此

\[
\boxed{C_1\ne0\pmod p.}
\tag{3.1}

所以可以在 `F_p` 中除以 `C_1^2`。

---

## 4. height-1 cross-sign character自动满足

在 `H_1=0` 上，(2.3) 退化为

\[
S_1^2+2C_1^2X_\times=0.
\]
因此

\[
\boxed{
-2X_\times
=\left(\frac{S_1}{C_1}\right)^2
\pmod p.}
\tag{4.1}

若 `X_cross` 为 unit，则右边非零，立即有

\[
\boxed{
\left(\frac{-2X_\times}{p}\right)=1.}
\tag{4.2}

所以 conjugate-angle cross-sign sphere要求的 quadratic character在 `H_1` sheet 上自动成立。

等价地，对 `p=3 mod4`：

\[
\boxed{
\left(\frac{2X_\times}{p}\right)=-1,}
\tag{4.3}

与 `spontaneous-cross-sign-sphere.md` 在 `H_2` sheet 上得到的结果完全一致。

---

## 5. both height sheets are now character shadows

旧 `H_2` syzygy为

\[
X_\times
=H_2-50x^2(2025x^2-2y^2-27y)^2,
\]
故在 `H_2=0` 上

\[
2X_\times
=-\left[10x(2025x^2-2y^2-27y)\right]^2.
\]

结合本文 (4.1)：

\[
\boxed{
\begin{array}{c|c}
H_1=0&-2X_\times=(S_1/C_1)^2\\
H_2=0&-2X_\times=[10x(2025x^2-2y^2-27y)]^2
\end{array}}
\tag{5.1}

因此两张 moving height orientations 都已经把 cross-sign quadratic extension split over the residue field。

---

## 6. updated cross-sign frontier

`spontaneous-cross-sign-sphere.md` 原先列出的 “height-1 orientation 与 `X_cross` 的相对 character” 可以删除。

对 moving height pool，cross-sign sphere尚有独立内容的只剩：

\[
\boxed{X_\times=0}
\]
的 discriminant collision / higher-depth intersection，以及不依附 height sheet的 generic cross-sign decimal orbit。

因此若目标仍是关闭 moving-height equal-depth shell，继续叠加 `(-2X_cross/p)=1` 不会增加约束；应转向 `X_cross=0` singular collision或 global natural representative。
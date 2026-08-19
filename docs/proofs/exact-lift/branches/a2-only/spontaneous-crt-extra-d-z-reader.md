# A2 additive CRT 的 extra-`d` centered-`z_E` reader

> **依赖：** `spontaneous-crt-gap-full5-residue.md`、`spontaneous-crt-gaussian-floorfree-carrier.md`、`endpoint-lattice.md` §§16.22–16.24。
>
> **严格状态：**前一文件证明 floor-free orientation carrier `P_Delta` 在完整 `5^lambda` 上具有显式 unit residue；endpoint Hensel kernel已有 exact lift `g r_E=c_+c_u+5^{lambda-d}z_E`。本文把两式合并。由于 reflection 中 `lambda>2d`，平方 lift 的二次 `z_E^2` 项在模 `5^lambda` 自动消失；除去公共 `5^{lambda-d}` 后，恰好剩下 `d` 个 digits，并线性读取 `z_E mod 5^d`。因此由 decimal defect `H mod g` 唯一中心化的 `z_E` 现在还必须满足一个来自 additive CRT/Gaussian carrier的独立 `5^d` 余类。本文把旧 extra-`d` alignment变成显式双模 compatibility，但尚未证明该系统无解，因此不关闭 A2。

---

## 1. full-`5` CRT residue

令

\[
\boxed{
R_\Delta^{(5)}
:=D(20-4K)-2C.}
\tag{1.1}
\]

前一文件给

\[
\boxed{
\mathscr P_\Delta
\equiv
2^{A_G}c_u^2a_3R_\Delta^{(5)}
\pmod{5^\lambda}.}
\tag{1.2}
\]

并证明

\[
5\nmid R_\Delta^{(5)}c_ua_3\mathscr P_\Delta.
\tag{1.3}
\]

---

## 2. exact centered Hensel lift

`endpoint-lattice.md` §16.23 定义

\[
\boxed{
n_5:=5^{\lambda-d}}
\tag{2.1}
\]

以及 centered odd representative `z_E`，并有 exact identity

\[
\boxed{
g r_E=c_+c_u+n_5z_E.}
\tag{2.2}
\]

reflection 的 primitive `5`-depth满足

\[
\nu_5=\lambda-2d>0.
\tag{2.3}
\]

因此

\[
2(\lambda-d)=\lambda+\nu_5>\lambda,
\]
即

\[
\boxed{n_5^2\equiv0\pmod{5^\lambda}.}
\tag{2.4}
\]

---

## 3. square the Hensel lift only to first order in `z_E`

由 (2.2)：

\[
c_+c_u=gr_E-n_5z_E.
\]

平方：

\[
c_+^2c_u^2
=g^2r_E^2-2gr_En_5z_E+n_5^2z_E^2.
\]

使用 (2.4)：

\[
\boxed{
c_+^2c_u^2
\equiv
g^2r_E^2-2gr_En_5z_E
\pmod{5^\lambda}.}
\tag{3.1}
\]

所以 full `5^lambda` 层只保留 `z_E` 的**线性**修正；quadratic lift自动落到模数之外。

---

## 4. define the top-`d` digit carrier

将 (1.2) 乘以 `c_+^2`，再代入 (3.1)：

\[
\begin{aligned}
c_+^2\mathscr P_\Delta
\equiv{}&
2^{A_G}a_3R_\Delta^{(5)}g^2r_E^2\\
&-2^{A_G+1}a_3R_\Delta^{(5)}gr_E\,n_5z_E
\pmod{5^\lambda}.
\end{aligned}
\tag{4.1}
\]

特别地，第一层模 `n_5` 已给

\[
\boxed{
n_5\mid
\left(
c_+^2\mathscr P_\Delta
-2^{A_G}a_3R_\Delta^{(5)}g^2r_E^2
\right).}
\tag{4.2}
\]

因此定义 ordinary integer

\[
\boxed{
\mathscr Z_\Delta
:=
\frac{
c_+^2\mathscr P_\Delta
-2^{A_G}a_3R_\Delta^{(5)}g^2r_E^2
}{n_5}.}
\tag{4.3}
\]

由于

\[
5^\lambda=n_5\,5^d,
\]
把 (4.1) 除以 `n_5` 正好得到最后 `d` digits：

\[
\boxed{
\mathscr Z_\Delta
\equiv
-2^{A_G+1}a_3R_\Delta^{(5)}gr_Ez_E
\pmod{5^d}.}
\tag{4.4}
\]

---

## 5. eliminate `r_E` from the coefficient

由 (2.2)：

\[
gr_E\equiv c_+c_u\pmod{n_5}.
\]

又因 `lambda>2d`：

\[
\lambda-d>d,
\]
故该同余当然可降到模 `5^d`：

\[
\boxed{gr_E\equiv c_+c_u\pmod{5^d}.}
\tag{5.1}
\]

代入 (4.4)：

\[
\boxed{
\mathscr Z_\Delta
\equiv
-2^{A_G+1}a_3R_\Delta^{(5)}c_+c_u z_E
\pmod{5^d}.}
\tag{5.2}
\]

所有 coefficient都是 `5`-进 units：

\[
5\nmid2a_3R_\Delta^{(5)}c_+c_u.
\]

因此可以唯一反解

\[
\boxed{
z_E
\equiv
-\left(
2^{A_G+1}a_3R_\Delta^{(5)}c_+c_u
\right)^{-1}
\mathscr Z_\Delta
\pmod{5^d}.}
\tag{5.3}
\]

这是真正的 extra-`d` digit reader。

---

## 6. combine with the decimal-defect centered representative

同一个 `z_E` 此前已经由真实 denominator defect `H` 唯一确定：

\[
\boxed{
-\frac g2<z_E<\frac g2,}
\tag{6.1}
\]

\[
\boxed{
c_-z_E
\equiv-5^{d+1}H
\pmod g,}
\tag{6.2}
\]

并且

\[
\gcd(z_E,g)=1.
\]

由于

\[
\gcd(g,5)=1,
\]
(5.3),(6.2) 形成真正的 coprime two-modulus compatibility：

\[
\boxed{
\begin{cases}
 c_-z_E\equiv-5^{d+1}H\pmod g,\\[1mm]
 2^{A_G+1}a_3R_\Delta^{(5)}c_+c_u z_E
 \equiv-\mathscr Z_\Delta\pmod{5^d},\\[1mm]
 |z_E|<g/2.
\end{cases}}
\tag{6.3}
\]

第一式已经唯一选出 `z_E` 的 centered integer；第二式因此不是新的自由选择，而是对该唯一自然代表施加一个深 `5^d` compatibility test。

---

## 7. relation to the old extra-`d` alignment

`endpoint-lattice.md` §16.8 曾把 Gaussian quotient kernel压成两个 `5`-primitive vectors，其 projective determinant仍被迫额外对齐恰好 `d` 位。此前这份 `d`-depth主要以 Gaussian orientation存在。

本文表明 additive CRT exact gap也读取**同一层数**：

\[
5^\lambda
=
5^{\lambda-d}\cdot5^d
\]

中的前 `lambda-d` digits由 centered scalar `r_E` 读取，最后 `d` digits恰线性读取 `z_E`。

所以 old extra-`d` alignment现在有一个纯整数 additive representative `Z_Delta`，而不是只存在于 Gaussian determinant中。

---

## 8. revised frontier

当前 reflection high-2 mixed kernel可以按下面顺序完全 canonical 化：

\[
H\bmod g
\Longrightarrow
z_E\in(-g/2,g/2)
\Longrightarrow
r_E
\Longrightarrow
\mathscr P_\Delta
\Longrightarrow
\mathscr Z_\Delta\bmod5^d.
\]

真正新的 closure target是证明唯一 centered `z_E` 从 (6.2) 得到的自然值不满足 (5.3)。由于 `d` 随 `M` 可线性增长，这不再是固定层的小同余；它是一个无界 mixed-radix compatibility。

若能把 (5.3) 进一步只写成 `(H,C)` 或 `(z_E,chi_E)` 的低高度函数，就有机会利用 `|z_E|<g/2` 与 signed bridge `P_Delta z_E chi_E<0` 完成矛盾。

A2 仍为 `待证`。

# A2 dual additive gaps 的 full-`5^lambda` Möbius synchronization

> **依赖：** `spontaneous-crt-gap-full5-residue.md`、`endpoint-lattice.md` §§16.34–16.38。
>
> **严格状态：**前一层给出右 gap `Delta_+` 的 full-`5^lambda` residue。本文把 exact curvature `Gamma_Delta=Delta_--Delta_+` 加回去，得到左 gap `Delta_-` 的同深 residue。两者的比值因此在模 `5^lambda` 下等于一个只含 `(qW_q,D,C)` 的 source Möbius ratio。Archimedean 上，真实 gap ratio 的 excess over `1` 约为 `60/K`，source ratio只约为 `1/K`，所以二者严格有序。其 cross-determinant 是正整数、被 `5^lambda` 整除；除去该完整 `5`-层后得到一个 normalized value落在固定 `(6,10)` 窗口的新 positive carrier。本文不证明该 carrier为空，因此不关闭 A2。

---

## 1. right gap full residue

沿用

\[
\Delta_+:=\frac{\Xi_+-\Xi_C}{L}>0,
\qquad L=2^m5^d,
\]

以及前一文件的 full-depth residue

\[
\boxed{
\Delta_+
\equiv
c_u^2a_3[D(20-4K)-2C]
\pmod{5^\lambda}.}
\tag{1.1}
\]

同时

\[
\boxed{v_5(\Delta_+)=0.}
\tag{1.2}
\]

---

## 2. curvature modulo `5^lambda`

记

\[
\Gamma_\Delta:=\Delta_--\Delta_+.
\]

`endpoint-lattice.md` (16.245) 给 exact formula

\[
\boxed{
\Gamma_\Delta
=2^{m+1}5^dc_u^2
\{g((2K-9)T-a_3)-H_0\}.}
\tag{2.1}
\]

使用

\[
H_0=g(3T+a_3)-5^\lambda C
\]
可把 bracket 精确写成

\[
g((2K-12)T-2a_3)+5^\lambda C.
\]

因为 `T` 的 `5`-进深度为 `m=lambda+d`，乘上前面的 `5^d` 后，所有含 `T` 或 `5^lambda C` 的项在模 `5^lambda` 下消失。只剩

\[
\Gamma_\Delta
\equiv
-2^{m+2}5^dg c_u^2a_3
\pmod{5^\lambda}.
\]

而

\[
D=g2^m5^d,
\]
所以

\[
\boxed{
\Gamma_\Delta
\equiv-4Dc_u^2a_3
\pmod{5^\lambda}.}
\tag{2.2}
\]

---

## 3. left gap full residue

由 `Delta_-=Delta_++Gamma_Delta`，结合 (1.1),(2.2)：

\[
\boxed{
\Delta_-
\equiv
c_u^2a_3[D(16-4K)-2C]
\pmod{5^\lambda}.}
\tag{3.1}
\]

模 `5` 仍有

\[
\Delta_-
\equiv-2c_u^2a_3C\not\equiv0\pmod5,
\]
所以

\[
\boxed{v_5(\Delta_-)=0.}
\tag{3.2}
\]

用

\[
qW_q=DK-(3D-C)
\]
可写成对称 height form：

\[
\boxed{
\Delta_-
\equiv
2c_u^2a_3(2D+C-2qW_q)
\pmod{5^\lambda},}
\tag{3.3-}
\]

\[
\boxed{
\Delta_+
\equiv
2c_u^2a_3(4D+C-2qW_q)
\pmod{5^\lambda}.}
\tag{3.3+}
\]

---

## 4. positive source Möbius pair

真实 endpoint 中 `K` 巨大，因此定义两个正整数

\[
\boxed{
A_s:=2qW_q-2D-C
=2D(K-4)+C,}
\tag{4.1}
\]

\[
\boxed{
B_s:=2qW_q-4D-C
=2D(K-5)+C.}
\tag{4.2}
\]

显然

\[
A_s=B_s+2D>B_s>0.
\]

因为 `5|D` 而 `5\nmid C`：

\[
\boxed{5\nmid A_sB_s.}
\tag{4.3}
\]

(3.3±) 于是等价于

\[
\Delta_-\equiv-2c_u^2a_3A_s,
\qquad
\Delta_+\equiv-2c_u^2a_3B_s
\pmod{5^\lambda}.
\]

消去共同 unit：

\[
\boxed{
\Delta_-B_s
\equiv
\Delta_+A_s
\pmod{5^\lambda}.}
\tag{4.4}
\]

或者在 unit ratio语言中

\[
\boxed{
\frac{\Delta_-}{\Delta_+}
\equiv
\frac{A_s}{B_s}
\pmod{5^\lambda}.}
\tag{4.5}
\]

---

## 5. the real gap ratio is much steeper

由 `Delta_-=Delta_++Gamma_Delta`：

\[
\frac{\Delta_-}{\Delta_+}
=1+\frac{\Gamma_\Delta}{\Delta_+}.
\]

`endpoint-lattice.md` 已给 bracket的安全窗口

\[
gT(2K-15)
<g((2K-9)T-a_3)-H_0
<2gTK.
\tag{5.1}
\]

于是 (2.1) 与 `D=g2^m5^d` 给

\[
2Dc_u^2T(2K-15)
<\Gamma_\Delta
<4Dc_u^2TK.
\tag{5.2}
\]

另一方面 `spontaneous-crt-quotient-source-scale.md` 已证明

\[
\frac{TK^2}{17}
<\mathscr S_+
<\frac{TK^2}{15},
\]
且

\[
\Delta_+=c_u^2D\mathscr S_+.
\]

所以对当前 `K>9*10^11`：

\[
\boxed{
1+\frac{59}{K}
<
\frac{\Delta_-}{\Delta_+}
<
1+\frac{68}{K}.}
\tag{5.3}
\]

这里下界只用

\[
\frac{30(2K-15)}{K^2}>rac{59}{K}
\qquad(K>450).
\]

---

## 6. source ratio has only `1/K` excess

由 (4.1),(4.2)：

\[
\frac{A_s}{B_s}
=1+\frac{2D}{2D(K-5)+C}
=1+\frac1{K-5+C/(2D)}.
\]

而

\[
0<\frac C{2D}<\frac3{500}<1.
\]

所以

\[
\boxed{
1+\frac1{K-4}
<
\frac{A_s}{B_s}
<
1+\frac1{K-5}.}
\tag{6.1}
\]

因此 `K>10` 时：

\[
\boxed{
\frac{57}{K}
<
\frac{\Delta_-}{\Delta_+}
-
\frac{A_s}{B_s}
<
\frac{68}{K}.}
\tag{6.2}
\]

真实 cubic-gap curvature相对于 source Möbius slope存在固定数量级差，不可能在实数上相等。

---

## 7. positive full-depth cross-determinant

定义

\[
\boxed{
\mathscr E_\Delta
:=\Delta_-B_s-\Delta_+A_s.}
\tag{7.1}
\]

由 (4.4)：

\[
\boxed{5^\lambda\mid\mathscr E_\Delta.}
\tag{7.2}
\]

由 (6.2) 与正性：

\[
\mathscr E_\Delta
=\Delta_+B_s
\left(
\frac{\Delta_-}{\Delta_+}
-
\frac{A_s}{B_s}
\right)>0.
\tag{7.3}
\]

使用

\[
\frac{c_u^2DTK^2}{17}<\Delta_+<\frac{c_u^2DTK^2}{15},
\]

\[
2D(K-5)<B_s<2D(K-4),
\]
和 (6.2)，可安全得到

\[
\boxed{
6c_u^2D^2TK^2
<\mathscr E_\Delta
<10c_u^2D^2TK^2.}
\tag{7.4}
\]

因此定义 positive integer

\[
\boxed{
\widehat{\mathscr E}_\Delta
:=\frac{\mathscr E_\Delta}{5^\lambda}
\in\mathbf Z_{>0}.}
\tag{7.5}
\]

由于 `T=L5^lambda`：

\[
\boxed{
6c_u^2D^2LK^2
<\widehat{\mathscr E}_\Delta
<10c_u^2D^2LK^2.}
\tag{7.6}
\]

所以 normalized cross-determinant拥有固定 `(6,10)` Archimedean window。

---

## 8. role of the new carrier

`Ehat_Delta` 同时读取：

1. additive cubic curvature `Delta_-/Delta_+`；
2. source reduced-height ratio `qW_q/D`；
3. 完整 reflection `5^lambda` synchronization；
4. 一个固定 positive natural-representative window。

它没有自动变成 `<1`，所以本文不把 (7.6) 冒充高度矛盾。真正可继续收费的是：把 `Ehat_Delta` 与 `Z_Delta` 的 extra-`d` reader或三 cofactor 的 `3 mod4` parity联立，检查同一 full-`5` cancellation是否还能同时承担 centered Hensel digit。

A2 仍为 `待证`。

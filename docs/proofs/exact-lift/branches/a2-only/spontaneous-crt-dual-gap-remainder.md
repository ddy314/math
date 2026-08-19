# A2 dual-gap synchronization 产生的 short `3 mod 4` remainder

> **依赖：** `spontaneous-crt-dual-gap-mobius.md`、`spontaneous-crt-quotient-source-scale.md`、`endpoint-lattice.md` §§16.34–16.38。
>
> **严格状态：**前一文件构造 positive full-`5^lambda` cross-determinant `E_Delta`，除去 `5^lambda` 后粗略落在 `(6,10)` natural-scale window。本文使用 `S_+/T` 的 exact quadratic form把该窗口压到 `(7.87,63/8)`。因此从上端最佳有理近似 `63/8` 提取出 canonical positive integer remainder `R_63=63B_Delta-8 Ehat_Delta`，其高度严格小于 parent scale的 `1/25`。更重要的是，exact `2`-adic gap valuations给 `v_2(R_63)=m+4`，其 primitive quotient恒为 `3 mod4`，所以这个缩短后的 remainder必产生一份 odd-inert parity。本文仍未证明该新 parity support与已有 pools完全分离，因此不关闭 A2。

---

## 1. normalized cross-determinant

沿用 positive full-depth cross determinant

\[
\mathscr E_\Delta
:=\Delta_-B_s-\Delta_+A_s,
\]

\[
5^\lambda\mid\mathscr E_\Delta,
\qquad
\widehat{\mathscr E}_\Delta
:=\frac{\mathscr E_\Delta}{5^\lambda}>0.
\]

定义 parent natural scale

\[
\boxed{
\mathscr B_\Delta
:=c_u^2D^2LK^2,}
\qquad T=L5^\lambda.
\tag{1.1}
\]

记

\[
\delta:=\frac CD,
\qquad
r:=3-\delta,
\qquad
\zeta:=\frac{a_3}{T}.
\]

已有

\[
0<\delta<\frac3{250},
\qquad
\frac{747}{250}<r<3,
\qquad
1<\zeta<\frac{251}{250}.
\tag{1.2}
\]

cross determinant可写成

\[
\mathscr E_\Delta
=\Gamma_\Delta B_s-2D\Delta_+,
\]

其中 exact

\[
\Gamma_\Delta
=2c_u^2DT(2K-12-2\zeta+\delta),
\]

\[
B_s=D(2K-10+\delta),
\]

\[
\Delta_+=c_u^2D\mathscr S_+.
\]

所以

\[
\boxed{
\frac{\widehat{\mathscr E}_\Delta}{\mathscr B_\Delta}
=2\frac{(2K-12-2\zeta+\delta)(2K-10+\delta)}{K^2}
-2\frac{\mathscr S_+/T}{K^2}.}
\tag{1.3}
\]

所有 factor-allocation scale已经消失。

---

## 2. exact expansion around `63/8`

前一 source-scale文件给

\[
\frac{\mathscr S_+}{T}
=
\frac{
\zeta^2K^2-2\mathcal L(r,\zeta)K+\mathcal C(r,\zeta)
}{(r+\zeta)^2}.
\]

代入 (1.3) 并整理：

\[
\boxed{
\frac{\widehat{\mathscr E}_\Delta}{\mathscr B_\Delta}
=
8-rac{2\zeta^2}{(r+\zeta)^2}
+\frac{C_1(r,\zeta)}K
+\frac{C_2(r,\zeta)}{K^2},}
\tag{2.1}
\]

其中

\[
\boxed{
C_1
=-4\frac{
2r^3+4r^2\zeta+9r^2+r\zeta^2+18r\zeta+9\zeta^2
}{(r+\zeta)^2},}
\tag{2.2}
\]

\[
\boxed{
C_2
=2\frac{
r^4+2r^3\zeta+9r^3+18r^2\zeta+26r^2
+9r\zeta^2+52r\zeta+26\zeta^2
}{(r+\zeta)^2}.}
\tag{2.3}
\]

在 box (1.2) 中直接粗估即可得到

\[
\boxed{-70<C_1<-40,\qquad0<C_2<130.}
\tag{2.4}
\]

---

## 3. strict upper bound `63/8`

因为 `r<3`、`zeta>1`：

\[
3\zeta>r,
\]
所以

\[
\frac\zeta{r+\zeta}>\frac14.
\]

因此 leading part严格满足

\[
8-rac{2\zeta^2}{(r+\zeta)^2}
<8-\frac18
=\frac{63}{8}.
\tag{3.1}
\]

由 (2.4)，只要 `K>4`：

\[
\frac{C_1}{K}+\frac{C_2}{K^2}
<-rac{40}{K}+rac{130}{K^2}<0.
\]

当前 `K>9*10^{11}`，故

\[
\boxed{
\frac{\widehat{\mathscr E}_\Delta}{\mathscr B_\Delta}
<\frac{63}{8}.}
\tag{3.2}
\]

---

## 4. strict lower bound `7.87`

由

\[
r>\frac{747}{250},
\qquad
\zeta<\frac{251}{250},
\]
有

\[
\frac\zeta{r+\zeta}<\frac{251}{998}.
\]

所以 leading part

\[
8-rac{2\zeta^2}{(r+\zeta)^2}
>
8-2\left(\frac{251}{998}\right)^2
>7.87349.
\tag{4.1}
\]

由 (2.4)：

\[
\frac{C_1}{K}+\frac{C_2}{K^2}
>-rac{70}{K}.
\]

而 `K>9*10^{11}`，故

\[
\boxed{
\frac{787}{100}=7.87
<
\frac{\widehat{\mathscr E}_\Delta}{\mathscr B_\Delta}.}
\tag{4.2}
\]

结合 (3.2)：

\[
\boxed{
\frac{787}{100}
<
\frac{\widehat{\mathscr E}_\Delta}{\mathscr B_\Delta}
<
\frac{63}{8}.}
\tag{4.3}
\]

---

## 5. canonical `63/8` remainder drops height by at least `25`

定义 ordinary integer

\[
\boxed{
\mathscr R_{63}
:=63\mathscr B_\Delta
-8\widehat{\mathscr E}_\Delta.}
\tag{5.1}
\]

由 (4.3)：

\[
\boxed{\mathscr R_{63}>0.}
\tag{5.2}
\]

下界 `Ehat/B>787/100` 又给

\[
\frac{\mathscr R_{63}}{\mathscr B_\Delta}
<63-8\cdot\frac{787}{100}
=\frac1{25}.
\]

所以

\[
\boxed{
0<\mathscr R_{63}
<\frac1{25}\mathscr B_\Delta.}
\tag{5.3}
\]

这是一个真正的 natural-representative descent：没有改变原 endpoint，只从 exact full-`5` synchronization中构造出一个至少短 `25` 倍的正整数。

---

## 6. exact two-adic depth of the cross determinant

已有

\[
\boxed{v_2(\Gamma_\Delta)=m+1,}
\tag{6.1}
\]

而 `B_s=2D(K-5)+C` 为 odd。

另一方面

\[
v_2(\Delta_+)=1,
\qquad
v_2(D)=m+t-1,
\qquad t\ge3.
\]

所以

\[
v_2(2D\Delta_+)=m+t+1\ge m+4.
\]

由

\[
\mathscr E_\Delta=\Gamma_\Delta B_s-2D\Delta_+
\]
第一项唯一最浅：

\[
\boxed{v_2(\mathscr E_\Delta)=m+1.}
\tag{6.2}
\]

`5^lambda` 为 odd，故

\[
\boxed{v_2(\widehat{\mathscr E}_\Delta)=m+1.}
\tag{6.3}
\]

---

## 7. exact two-adic depth of the short remainder

parent scale有

\[
\mathscr B_\Delta=c_u^2D^2LK^2.
\]

其中

\[
v_2(D)=m+t-1,
\quad v_2(L)=m,
\quad v_2(K)=1,
\quad c_u\text{ odd}.
\]

因此

\[
\boxed{v_2(\mathscr B_\Delta)=3m+2t.}
\tag{7.1}
\]

而

\[
v_2(8\widehat{\mathscr E}_\Delta)=m+4.
\]

因为 `m>=5,t>=3`：

\[
3m+2t>m+4.
\]

所以 (5.1) 中第二项唯一最浅：

\[
\boxed{v_2(\mathscr R_{63})=m+4.}
\tag{7.2}
\]

定义 primitive positive remainder

\[
\boxed{
\widehat{\mathscr R}_{63}
:=\frac{\mathscr R_{63}}{2^{m+4}}
\in\mathbf Z_{>0}\text{ odd}.}
\tag{7.3}
\]

---

## 8. primitive remainder is always `3 mod 4`

先读 `Ehat` 的 primitive unit。由 §6：

\[
\frac{\mathscr E_\Delta}{2^{m+1}}
\equiv
5^dc_u^2
\{g((2K-9)T-a_3)-H_0\}B_s
\pmod4.
\]

因为 `g` 被 `4` 整除：

\[
g((2K-9)T-a_3)-H_0
\equiv-H_0\pmod4.
\]

又 `D` 被 `4` 整除，所以

\[
B_s=2D(K-5)+C\equiv C\pmod4.
\]

而 source relation

\[
H_0=g(3T+a_3)-5^\lambda C
\]
给

\[
H_0\equiv-C\pmod4.
\]

由于 `5^d,c_u^2,5^lambda` 都为 `1 mod4`：

\[
\boxed{
\frac{\widehat{\mathscr E}_\Delta}{2^{m+1}}
\equiv(-H_0)C
\equiv C^2
\equiv1\pmod4.}
\tag{8.1}
\]

parent term `63B_Delta` 在除以 `2^{m+4}` 后仍被 `4` 整除，因为其二进深度远大于 `m+6`。所以从 (5.1)：

\[
\widehat{\mathscr R}_{63}
\equiv
-\frac{\widehat{\mathscr E}_\Delta}{2^{m+1}}
\equiv-1
\equiv3\pmod4.
\]

因此

\[
\boxed{
\widehat{\mathscr R}_{63}
>0,
\qquad
\widehat{\mathscr R}_{63}\equiv3\pmod4.}
\tag{8.2}
\]

所以它必含至少一枚 `3 mod4` prime到奇次。

---

## 9. current role

这是当前 additive CRT / Gaussian chain中第一条同时具有以下四点的 carrier：

1. 由 full `5^lambda` synchronization自然产生；
2. real height相对 parent natural scale严格下降至少 `25` 倍；
3. exact primitive `2`-depth为 `m+4`；
4. primitive quotient无条件为 positive `3 mod4`。

因此 `Rhat_63` 是一个新的短 odd-inert parity supplier。下一步最有价值的是研究它与原 `widehat T_2`、`P_Delta` 以及 source-common/target pools的 support overlap；若能证明至少一组 separation，就会把这份下降后的 parity升级成真正的新 distinct-prime cost。

A2 仍为 `待证`。

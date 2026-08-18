# A2 fixed `23` `eta=2` `c=2` 的 fixed-modulus natural-representative no-go

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-blowup-nogo.md`、`spontaneous-cq-canonical-defect-overlap.md`、`endpoint-lattice.md` §§5,13。
>
> **严格状态：**唯一 `v_23(c_Q)=2` high-2 类型 `(d,c_Q,k_h,slot)=(1,1587,1,+)` 具有 canonical `C mod23^4` orientation residue，同时 endpoint 给 `0<C<3D/250`。本文量化这两个条件的尺度，证明允许的 `C` 区间从最小合法长度开始就远长于 `23^4`。因此单独的 fixed `23^4` residue 无法排除任何 orientation；若要获得新 obstruction，必须与随高度增长的 `g,2^m,5^lambda,L_0` 或 Gaussian-center modulus 联立。

---

## 1. type-specific length lattice

当前类型满足

\[
(d,c_Q,k_h,\varepsilon)=(1,1587,1,+1),
\]

\[
M=2m-2,
\qquad
\lambda=m-1,
\qquad
M\equiv16\pmod{22}.
\tag{1.1}

因此

\[
2m-2\equiv16\pmod{22},
\]
即

\[
\boxed{m\equiv9\pmod{11}.}
\tag{1.2}

当前开放 endpoint 已有 `M>=11`，而 (1.1) 的最小非负 fixed-`23` length 是 `M=16`，故

\[
\boxed{m\ge9.}
\tag{1.3}

---

## 2. finite-defect denominator `D` 的指数下界

finite-defect normalization 为

\[
5^\lambda D=g10^m.
\]

由于 `lambda=m-1`：

\[
\boxed{D=5\cdot2^m g.}
\tag{2.1}

另一方面 `endpoint-lattice.md` 的 plus high-2 slot，在 `k_h=1` 时给

\[
\boxed{
\frac g{10^m}>
\frac{2389}{250}.}
\tag{2.2}

代入 (2.1)：

\[
D
>
5\cdot2^m\frac{2389}{250}10^m
=
\boxed{
\frac{2389}{50}\,20^m.}
\tag{2.3}

---

## 3. `C` 的允许区间远长于 `23^4`

危险 `(a,k)=(9,2)` endpoint 已有

\[
\boxed{0<C<\frac{3D}{250}.}
\tag{3.1}

由 (2.3)：

\[
\frac{3D}{250}
>
\frac{3\cdot2389}{12500}\,20^m.
\tag{3.2}

使用最小 `m=9`：

\[
\boxed{
\frac{3D}{250}
>
\frac{3\cdot2389}{12500}\,20^9
=293560320000.}
\tag{3.3}

而 canonical `23^2` square allocation只给固定模数

\[
23^{2c}=23^4=279841.
\tag{3.4}

因此从最小合法长度开始就有

\[
\boxed{
\frac{3D}{250}>23^4.}
\tag{3.5}

实际上两者相差超过一百万倍。

---

## 4. 任意 canonical orientation residue 都有区间代表

两种 orientation 分别要求

\[
C\equiv3D\pmod{23^4}
\tag{4.1-}

\]

或

\[
C\equiv
D\left(3+2a_3T^{-1}\right)
\pmod{23^4}.
\tag{4.1+}

无论右边是哪一个 residue class，取其模 `23^4` 的最小正代表 `r`；若 residue 为零则取 `r=23^4`。总有

\[
0<r\le23^4.
\]

由 (3.5)：

\[
0<r<\frac{3D}{250}.
\]

所以

\[
\boxed{
\text{每一个 fixed }23^4\text{ residue class}
\text{ 都至少有一个代表位于允许的 }C\text{ 区间。}}
\tag{4.2}

因此 canonical orientation residue与 `0<C<3D/250` 单独联立时不可能产生空性。

---

## 5. 更强的审计含义

本文给出的结论比“尚未找到矛盾”更强。对当前无界 type：

\[
\boxed{
C\bmod23^4
+0<C<3D/250
\text{ 在尺度上必然兼容。}}
\tag{5.1}

所以以下路线应停止：

1. 继续只提高 fixed `23` canonical residue的显式写法；
2. 只把 `C mod23^4` 与同一个固定小模数继续 CRT；
3. 期待 `C/D<3/250` 本身与 `23^4` residue冲突。

真正可能提供全局 pruning 的 modulus 必须随无界参数增长。当前规范候选是

\[
\boxed{
g,\quad2^m,\quad5^\lambda,\quad\mathfrak L_0=2c_u^2g^2}
\]

以及 `endpoint-lattice.md` 的 Gaussian center representative。下一步应把 canonical orientation label送入这些 growing-modulus natural representatives，而不是继续研究 fixed `23^4` 单独的 residue geometry。
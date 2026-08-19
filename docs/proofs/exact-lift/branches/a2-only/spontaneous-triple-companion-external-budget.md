# A2 `T^circ/J^circ/B^circ` external triple-reuse 的 short central budget

> **依赖：** `spontaneous-residual-parity-doubling.md`、`spontaneous-companion-common-parity-dichotomy.md`、`spontaneous-companion-external-tail-budget.md`、`spontaneous-height-companion-cross.md`、`source-discriminant.md`。
>
> **严格状态：**在 `D_H=1 mod4` 的危险 orientation 中，`T^circ,J^circ,B^circ` 三个 residual companion 都是 positive `3 mod4`。本文审计“一枚 generic external inert prime同时复用三份 parity”的最省-prime情形。令 `G_TJB=gcd(T^circ,J^circ,B^circ)`。对 genuine external prime `p|G_TJB`，`T/J` difference把完整 triple-common exponent送入 central factor `2K-9`，`J/B` difference把同一 exponent送入 `L_JB`。二者与 `B_W` 联立后，把 source ratio消成固定 `23`-discriminant finite-defect quadratic `F_23(C,D)=1204C^2-6396CD+6489D^2`。因此整个 generic external triple-common subproduct整除 `2K-9<20*10^M`，且每个 inert supplier满足 `(p/23)=-1`。本文不排除这些 simple central/defect roots，因此不关闭 A2。

---

## 1. triple common gcd

沿用 height-free positive odd companions

\[
T^\circ,\qquad J^\circ,\qquad B^\circ.
\]

定义

\[
\boxed{G_{TJB}:=\gcd(T^\circ,J^\circ,B^\circ).}
\tag{1.1}
\]

固定 genuine generic external inert prime `p`：

\[
p\mid G_{TJB},
\qquad
p\nmid W_q,
\tag{1.2}
\]

并保留标准 unit separation

\[
\boxed{p\nmid2\cdot3\cdot5\cdot Dgqfzc_uK\omega W_q.}
\tag{1.3}
\]

`spontaneous-companion-external-tail-budget.md` 已证明 external `J/B` common prime自动满足 `p∤omega`，所以 (1.3) 与该结论一致。

写

\[
t:=v_p(T^\circ),
\qquad
j:=v_p(J^\circ),
\qquad
b:=v_p(B^\circ),
\]

\[
\boxed{k:=v_p(G_{TJB})=\min(t,j,b)\ge1.}
\tag{1.4}
\]

---

## 2. `T/J` common depth enters the central factor

residual-parity difference为

\[
\boxed{
T^\circ-5^mJ^\circ
=-2^{m+1}B_0^2(2K-9)\omega W^\circ,}
\tag{2.1}
\]

其中 `B_0=c_ug`，`W^circ=W_q/D_H`。

在 current external prime上右端除 `2K-9` 外的所有 factors都是 units。左端两个 summands均被 `p^k` 整除，所以

\[
\boxed{p^k\mid2K-9.}
\tag{2.2}
\]

若 `t!=j`，则左边有唯一最浅项，因此

\[
\boxed{v_p(2K-9)=\min(t,j).}
\tag{2.3}
\]

但本文只需要 universal lower bound (2.2)。

令

\[
\boxed{H:=2K-9.}
\tag{2.4}
\]

---

## 3. `J/B` common depth enters the linear gate

`spontaneous-companion-common-parity-dichotomy.md` 已证明 generic external common exponent全部进入

\[
\boxed{L_{JB}:=DzK+fN_s,}
\tag{3.1}
\]

其中为避免与 decimal `10^M` 混淆，本文把 source/finite-defect integer记成

\[
\boxed{N_s:=3D-C.}
\tag{3.2}
\]

因此

\[
\boxed{p^k\mid L_{JB}.}
\tag{3.3}
\]

---

## 4. central root converts `B_W` into a `23` source quadratic

source height carrier为

\[
\mathscr B_W
=c_u^2(5K^2-36K+55)+z^2K^2.
\tag{4.1}
\]

用

\[
K=(H+9)/2
\]
直接展开，得到 exact identity

\[
\boxed{
4\mathscr B_W
=(5c_u^2+z^2)H^2
+18(c_u^2+z^2)H
+S_{23},}
\tag{4.2}
\]

其中

\[
\boxed{S_{23}:=81z^2-23c_u^2.}
\tag{4.3}
\]

external prime满足 `p∤W_q`，所以 `D_H=gcd(B_W,W_q)` 在 p 上没有 exponent，因而

\[
v_p(B^\circ)=v_p(B_W)=b\ge k.
\]

结合 (2.2),(4.2)：

\[
\boxed{p^k\mid S_{23}.}
\tag{4.4}
\]

所以 triple reuse自动进入一个 fixed `23` source orientation。

---

## 5. central + `L_JB` gives a finite-defect linear form

由 `H=2K-9`：

\[
\begin{aligned}
2L_{JB}-DzH
&=2DzK+2fN_s-Dz(2K-9)\\
&=9Dz+2fN_s.
\end{aligned}
\]

所以

\[
\boxed{R_{23}:=9Dz+2fN_s}
\tag{5.1}
\]

也满足

\[
\boxed{p^k\mid R_{23}.}
\tag{5.2}
\]

使用

\[
f=z+2c_u,
\qquad
N_s=3D-C,
\]
得到完全显式线性式

\[
\boxed{
R_{23}
=(15D-2C)z+(12D-4C)c_u.}
\tag{5.3}
\]

记

\[
A:=15D-2C,
\qquad
B:=12D-4C.
\tag{5.4}
\]

则

\[
R_{23}=Az+Bc_u.
\]

---

## 6. eliminate the source ratio

定义 conjugate linear form

\[
\boxed{\overline R_{23}:=Az-Bc_u.}
\tag{6.1}
\]

由 (4.3)：

\[
S_{23}=81z^2-23c_u^2.
\]

直接计算 exact eliminant：

\[
\boxed{
A^2S_{23}
-81R_{23}\overline R_{23}
=c_u^2F_{23}(C,D),}
\tag{6.2}
\]

其中

\[
\boxed{
F_{23}(C,D)
:=1204C^2-6396CD+6489D^2.}
\tag{6.3}
\]

由于 `p∤c_u`，结合 (4.4),(5.2)：

\[
\boxed{p^k\mid F_{23}(C,D).}
\tag{6.4}
\]

因此同一个 triple-common exponent被同时读取于

\[
\boxed{2K-9}
\quad\text{和}\quad
\boxed{F_{23}(C,D)}.
\]

---

## 7. the fixed `23` character

把 `F_23` 看成关于 `C` 的 quadratic：

\[
\operatorname{Disc}_C(F_{23})
=(-6396D)^2
-4\cdot1204\cdot6489D^2.
\]

精确化简：

\[
\boxed{
\operatorname{Disc}_C(F_{23})
=2^6 3^8\cdot23\,D^2.}
\tag{7.1}
\]

在 genuine prime `p∤2\cdot3\cdot23D` 上，若 `F_23(C,D)=0 mod p` 有 root，必要且充分的 character为

\[
\boxed{\left(\frac{23}{p}\right)=1.}
\tag{7.2}
\]

当前 supplier是 inert prime

\[
p\equiv3\pmod4,
\]
而

\[
23\equiv3\pmod4.
\]

由 quadratic reciprocity：

\[
\boxed{
\left(\frac{p}{23}\right)
=-\left(\frac{23}{p}\right)
=-1.}
\tag{7.3}
\]

所以 external triple-reuse supplier只能落在 mod-`23` quadratic nonresidue classes。

这是一条 fixed orientation；本文不把它重复计作 q-channel `-23` curvature 的独立 character，除非后续另有条件强迫相反 `(p/23)`。

---

## 8. global short central budget

令 `E_TJB^ext` 为 generic external triple-common primes，并定义

\[
\boxed{
G_{TJB}^{\rm ext}
:=\prod_{p\in E_{TJB}^{\rm ext}}
p^{v_p(G_{TJB})}.}
\tag{8.1}
\]

逐 prime由 (2.2)：

\[
\boxed{G_{TJB}^{\rm ext}\mid2K-9.}
\tag{8.2}
\]

令 decimal scale

\[
N_{10}:=10^M.
\]

endpoint有

\[
0<K<10N_{10}.
\]

故

\[
\boxed{
0<2K-9<20N_{10}.}
\tag{8.3}
\]

于是

\[
\boxed{
G_{TJB}^{\rm ext}<20\cdot10^M.}
\tag{8.4}
\]

同时由 (6.4)：

\[
\boxed{G_{TJB}^{\rm ext}\mid F_{23}(C,D)}
\tag{8.5}
\]

在 generic support上逐 prime成立。

所以一枚 external prime若想同时承担 `T^circ,J^circ,B^circ` 三份 odd parity，它不再只受三个大 carrier约束，而必须把完整 triple-common depth塞进一个只有 `M+2` 位量级的 central integer `2K-9`。

---

## 9. global allocation consequence

在 `D_H=1 mod4` orientation 中，三个 parent companions均为 positive `3 mod4`：

\[
T^\circ\equiv J^\circ\equiv B^\circ\equiv3\pmod4.
\]

如果 global parity试图用同一枚 generic external inert prime复用三份 odd parity，则该 prime必须属于 `G_TJB^ext`，所以同时满足：

\[
\boxed{p^{k}\mid2K-9,}
\]

\[
\boxed{p^{k}\mid F_{23}(C,D),}
\]

\[
\boxed{(p/23)=-1.}
\]

且所有这种 triple reuse的完整 common depth乘积满足

\[
\boxed{G_{TJB}^{\rm ext}<20\cdot10^M.}
\]

因此 triple parity reuse是一个昂贵、短-central、fixed-character branch，而不再是自由 generic prime allocation。

A2 仍为 `待证`。

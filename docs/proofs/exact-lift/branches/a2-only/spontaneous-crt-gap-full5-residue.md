# A2 additive CRT right gap 的 full-`5^lambda` residue

> **依赖：** `endpoint-lattice.md` §§16.36–16.38、`spontaneous-crt-quotient-source-scale.md`、`spontaneous-crt-gaussian-floorfree-carrier.md`。
>
> **严格状态：**`Delta_+=(Xi_+-Xi_C)/(2^m5^d)` 此前只知道 `v_2(Delta_+)=1`，未显式记录其剩余 `5`-进深度。本文使用 additive lift `Ttilde_2-(D-C)Gammatilde_Delta=g Delta_+`，把两项在完整 `5^lambda` 层正规化，得到 `Delta_+` 的显式 full-depth residue。特别地 `Delta_+` 是精确 `5`-进单位。floor-free Gaussian orientation carrier `P_Delta` 继承同一 `5^lambda` unit residue。因此 additive exact gap、Gaussian side与 Hensel 的完整 reflection `5`-深度首次位于同一 ordinary integer carrier上。本文不单独关闭 A2。

---

## 1. additive lift

沿用

\[
L:=2^m5^d,
\qquad
D=gL,
\qquad
T=10^m,
\qquad
m=\lambda+d,
\]

以及

\[
\nu_5:=\lambda-2d>0.
\]

`endpoint-lattice.md` (16.265) 已有 exact integer lift

\[
\boxed{
\widetilde{\mathcal T}_2
-(D-C)\widetilde\Gamma_\Delta
=g\Delta_+.}
\tag{1.1}
\]

其中

\[
\boxed{
\widetilde\Gamma_\Delta
=c_u^2\{g((2K-9)T-a_3)-H_0\}.}
\tag{1.2}
\]

并且

\[
H_0=g(3T+a_3)-5^\lambda C.
\tag{1.3}
\]

---

## 2. `Gammatilde_Delta` modulo `5^lambda`

由 (1.2),(1.3)：

\[
\begin{aligned}
\widetilde\Gamma_\Delta
&=c_u^2\{g((2K-12)T-2a_3)+5^\lambda C\}.
\end{aligned}
\]

因为

\[
v_5(T)=m=\lambda+d>\lambda,
\]
所以模 `5^lambda`：

\[
\boxed{
\widetilde\Gamma_\Delta
\equiv-2gc_u^2a_3
\pmod{5^\lambda}.}
\tag{2.1}
\]

---

## 3. explicit formula for `Ttilde_2`

`endpoint-lattice.md` (16.259) 为

\[
\mathcal T_2
=
\frac{
2b_2^2T\,[TK^2-(18T+4a_3)K+18a_3+55T]
-2Q^2N_0T^2
}
{2^{2M+2}5^{\nu_5}DL}.
\]

又

\[
\widetilde{\mathcal T}_2
:=\frac{\mathcal T_2}{2^{m+1}5^d}.
\]

使用

\[
b_2=2^{M+m+1}c_ug,
\qquad
Q=2^{M+1}Q_0,
\qquad
\nu_5+2d=\lambda,
\]
逐项约分，得到 exact formula

\[
\boxed{
\begin{aligned}
\widetilde{\mathcal T}_2
={}&Lc_u^2g^2
[TK^2-(18T+4a_3)K+18a_3+55T]\\
&-5^{\lambda+2d}Q_0^2N_0.
\end{aligned}}
\tag{3.1}
\]

模 `5^lambda` 时所有含 `T` 的项都消失，最后一项也消失。因此

\[
\boxed{
\widetilde{\mathcal T}_2
\equiv
Lc_u^2g^2a_3(18-4K)
\pmod{5^\lambda}.}
\tag{3.2}
\]

---

## 4. full-depth residue for `Delta_+`

把 (2.1),(3.2) 代入 (1.1)：

\[
\begin{aligned}
g\Delta_+
&\equiv
Lc_u^2g^2a_3(18-4K)
+2g c_u^2a_3(D-C)\\
&=gc_u^2a_3
[D(18-4K)+2D-2C]\\
&=gc_u^2a_3
[D(20-4K)-2C]
\pmod{5^\lambda}.
\end{aligned}
\]

当前 source split给

\[
\gcd(g,5)=1,
\]
所以可以消去 `g`：

\[
\boxed{
\Delta_+
\equiv
c_u^2a_3[D(20-4K)-2C]
\pmod{5^\lambda}.}
\tag{4.1}
\]

这比只模 `n_5=5^{lambda-d}` 更强整整 `d` 层。

---

## 5. height form

使用

\[
qW_q=DK-(3D-C),
\]
有

\[
D(20-4K)-2C
=2(4D+C-2qW_q).
\]

所以 (4.1) 等价于

\[
\boxed{
\Delta_+
\equiv
2c_u^2a_3(4D+C-2qW_q)
\pmod{5^\lambda}.}
\tag{5.1}
\]

这把 additive right gap的 full `5`-residue直接接回 reduced height numerator `W_q`。

---

## 6. `Delta_+` is exactly a `5`-adic unit

reflection 中 `d>=1`，故

\[
5\mid D.
\]

同时

\[
K=10P,
\qquad 5\mid K.
\]

由 primitive reduction / defect coprimality：

\[
5\nmid c_ua_3C.
\]

将 (4.1) 模 `5`：

\[
\boxed{
\Delta_+
\equiv-2c_u^2a_3C
\not\equiv0\pmod5.}
\tag{6.1}
\]

因此

\[
\boxed{v_5(\Delta_+)=0.}
\tag{6.2}
\]

所以三个 cofactor先约去公共 `5^d` 后，右 gap没有任何隐藏的额外 `5`-depth。

---

## 7. floor-free Gaussian carrier inherits the full residue

`spontaneous-crt-gaussian-floorfree-carrier.md` 定义

\[
\mathscr P_\Delta
=2^{A_G}\Delta_+
-5^{B_G}k_h^3(D^2-C^2),
\]

其中

\[
A_G=\frac{M+5\eta}{2}+8,
\qquad
B_G=3M-d-\eta-3.
\]

在 current low-`m` reflection cone，`m<=6M/11`，故

\[
B_G-\lambda
=4M-3m-3
>0.
\tag{7.1}
\]

所以

\[
5^\lambda\mid5^{B_G}k_h^3(D^2-C^2).
\]

由 (4.1)：

\[
\boxed{
\mathscr P_\Delta
\equiv
2^{A_G}c_u^2a_3[D(20-4K)-2C]
\pmod{5^\lambda}.}
\tag{7.2}
\]

等价地

\[
\boxed{
\mathscr P_\Delta
\equiv
2^{A_G+1}c_u^2a_3(4D+C-2qW_q)
\pmod{5^\lambda}.}
\tag{7.3}
\]

模 `5` 使用 (6.1)：

\[
\boxed{
\mathscr P_\Delta
\equiv
-2^{A_G+1}c_u^2a_3C
\not\equiv0\pmod5.}
\tag{7.4}
\]

所以

\[
\boxed{v_5(\mathscr P_\Delta)=0.}
\tag{7.5}
\]

现在 `P_Delta` 同时具有：

1. `sgn(P_Delta)=-epsilon`；
2. `P_Delta` 为 odd integer；
3. `P_Delta` 为 `5`-adic unit；
4. 模 `5^lambda` 的显式 residue (7.2)/(7.3)。

---

## 8. current interface

Hensel scalar `r_E` 的中心模数为

\[
n_5=5^{\lambda-d},
\]
而 (7.2) 已覆盖更深的 `5^lambda`。因此 `P_Delta` 与 centered Hensel kernel现在确实处在同一 `5`-adic tower，而非仅共享 endpoint parameters。

下一步可把

\[
gr_E\equiv c_+c_u\pmod{5^{\lambda-d}}
\]
代入 (7.2)，尝试把 `c_u^2` 换成 centered Hensel unit `r_E^2`；随后再与 `P_Delta z_E chi_E<0` 的符号律联立。若 natural representative被该 residue固定到错误符号，即可排除对应 Gaussian side。

A2 仍为 `待证`。

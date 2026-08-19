# A2 forced inert carrier 经 `R_63` 的 positive height descent

> **依赖：** `spontaneous-crt-dual-gap-remainder.md`、`endpoint-lattice.md` §§16.37–16.39。
>
> **严格状态：**前一文件从 dual-gap full-`5^lambda` synchronization构造 positive primitive `3 mod4` remainder `Rhat_63`。本文证明它不是与原核心 carrier `That_2` 平行的新对象：二者在完整 denominator modulus `g` 上满足 `That_2≡5^{nu_5}Rhat_63 mod g`。因此可定义 positive descended quotient `D_63=(That_2-5^{nu_5}Rhat_63)/g`。更强地，`5^{nu_5}Rhat_63` 小于原 `That_2` 的 `1/24`，而 `D_63` 有显式 positive quadratic form与窄 `(31/500,1/16)` normalized window。原 carrier与短 remainder若复用 prime，该 prime必须继续进入 `D_63`。这构成 nested support/height descent，但尚未证明可无限迭代回同一 decimal class，因此不关闭 A2。

---

## 1. notation

沿用

\[
\nu_5:=\lambda-2d>0,
\qquad
n_5:=5^{\lambda-d}=5^{\nu_5+d},
\]

\[
L=2^m5^d,
\qquad
D=gL,
\]

以及 additive lift

\[
\boxed{
\widetilde{\mathcal T}_2
-(D-C)\widetilde\Gamma_\Delta
=g\Delta_+.}
\tag{1.1}
\]

这里

\[
\widetilde{\mathcal T}_2=5^d\widehat{\mathcal T}_2,
\tag{1.2}
\]

\[
\widetilde\Gamma_\Delta
=c_u^2\{g((2K-9)T-a_3)-H_0\}.
\tag{1.3}
\]

定义 bracket

\[
\boxed{
B_\Delta
:=g((2K-9)T-a_3)-H_0.}
\tag{1.4}
\]

所以 `Gammatilde_Delta=c_u^2 B_Delta`。

---

## 2. cross determinant is itself an additive lift quotient

前一文件定义

\[
\mathscr E_\Delta
=\Gamma_\Delta B_s-2D\Delta_+,
\]

其中

\[
\Gamma_\Delta=2L\widetilde\Gamma_\Delta,
\qquad
B_s=2D(K-5)+C.
\]

由 (1.1)：

\[
2D\Delta_+
=2L\{
\widetilde{\mathcal T}_2-(D-C)\widetilde\Gamma_\Delta
\}.
\]

所以

\[
\begin{aligned}
\mathscr E_\Delta
&=2L\left[
\widetilde\Gamma_\Delta(B_s+D-C)
-\widetilde{\mathcal T}_2
\right]\\
&=2L\left[
D(2K-9)\widetilde\Gamma_\Delta
-\widetilde{\mathcal T}_2
\right].
\end{aligned}
\]

因此

\[
\boxed{
\mathscr E_\Delta
=2L\left[
D(2K-9)\widetilde\Gamma_\Delta
-\widetilde{\mathcal T}_2
\right].}
\tag{2.1}
\]

前一文件证明 `5^lambda|E_Delta`。因为

\[
\frac{2L}{5^\lambda}
=\frac{2^{m+1}}{n_5},
\]
得到

\[
\boxed{
\widehat{\mathscr E}_\Delta
=2^{m+1}\mathscr J_\Delta,}
\tag{2.2}
\]

其中 ordinary integer

\[
\boxed{
\mathscr J_\Delta
:=
\frac{
D(2K-9)\widetilde\Gamma_\Delta
-\widetilde{\mathcal T}_2
}{n_5}.}
\tag{2.3}
\]

这直接解释 `v_2(Ehat_Delta)=m+1`。

---

## 3. `J_Delta` has a pure square residue modulo `g`

先由 (1.1)：

\[
\widetilde{\mathcal T}_2
\equiv(D-C)\widetilde\Gamma_\Delta
\equiv-C\widetilde\Gamma_\Delta
\pmod g.
\tag{3.1}
\]

另一方面

\[
B_\Delta=g((2K-9)T-a_3)-H_0
\equiv-H_0\pmod g.
\]

source identity

\[
H_0=g(3T+a_3)-5^\lambda C
\]
给

\[
B_\Delta\equiv5^\lambda C\pmod g.
\]

因此

\[
\boxed{
\widetilde\Gamma_\Delta
\equiv c_u^25^\lambda C
\pmod g,}
\tag{3.2}
\]

\[
\boxed{
\widetilde{\mathcal T}_2
\equiv-c_u^25^\lambda C^2
\pmod g.}
\tag{3.3}
\]

在 (2.3) 中第一项含 `D`，故模 `g` 消失：

\[
n_5\mathscr J_\Delta
\equiv c_u^25^\lambda C^2
\pmod g.
\]

`5` 与 `g` 互素，所以消去 `n_5=5^{lambda-d}`：

\[
\boxed{
\mathscr J_\Delta
\equiv c_u^25^dC^2
\pmod g.}
\tag{3.4}
\]

---

## 4. short remainder modulo `g`

前一文件定义

\[
\widehat{\mathscr R}_{63}
:=\frac{
63\mathscr B_\Delta-8\widehat{\mathscr E}_\Delta
}{2^{m+4}},
\]

其中

\[
\mathscr B_\Delta=c_u^2D^2LK^2.
\]

由 (2.2)：

\[
\boxed{
\widehat{\mathscr R}_{63}
=
\frac{63\mathscr B_\Delta}{2^{m+4}}
-\mathscr J_\Delta.}
\tag{4.1}
\]

第一项为整数，并且含完整 factor `g`：确实

\[
\frac{\mathscr B_\Delta}{2^{m+4}g}
=
\frac{c_u^2gL^3K^2}{2^{m+4}}
\in\mathbf Z.
\]

因此由 (3.4)：

\[
\boxed{
\widehat{\mathscr R}_{63}
\equiv-c_u^25^dC^2
\pmod g.}
\tag{4.2}
\]

已有

\[
\gcd(c_uC,5g)=1.
\]

所以立即得到

\[
\boxed{
\gcd(\widehat{\mathscr R}_{63},g)=1.}
\tag{4.3}
\]

新 short `3 mod4` parity因此完全位于 denominator `g` support之外。

---

## 5. original carrier has the matching deeper residue

由 (1.2),(3.3)：

\[
5^d\widehat{\mathcal T}_2
\equiv-c_u^25^\lambda C^2
\pmod g.
\]

消去 `5^d`：

\[
\boxed{
\widehat{\mathcal T}_2
\equiv
-c_u^25^{\lambda-d}C^2
\pmod g.}
\tag{5.1}
\]

而

\[
\nu_5=\lambda-2d.
\]

把 (4.2) 乘 `5^{nu_5}`：

\[
5^{\nu_5}\widehat{\mathscr R}_{63}
\equiv
-c_u^25^{\lambda-d}C^2
\pmod g.
\]

所以

\[
\boxed{
\widehat{\mathcal T}_2
\equiv
5^{\nu_5}\widehat{\mathscr R}_{63}
\pmod g.}
\tag{5.2}
\]

这是 original forced inert carrier 与 short remainder之间的 exact denominator bridge。

---

## 6. define the descended positive quotient

由 (5.2) 定义 integer

\[
\boxed{
\mathscr D_{63}
:=
\frac{
\widehat{\mathcal T}_2
-5^{\nu_5}\widehat{\mathscr R}_{63}
}{g}.}
\tag{6.1}
\]

下面证明它严格为正，并给出 natural form。

---

## 7. exact closed form for `D_63`

由 (4.1)：

\[
\widehat{\mathscr R}_{63}=U_{63}-\mathscr J_\Delta,
\qquad
U_{63}:=\frac{63\mathscr B_\Delta}{2^{m+4}}.
\]

而 (2.3) 与 `n_5=5^{nu_5+d}` 给

\[
5^{\nu_5}\mathscr J_\Delta
=
\frac{D(2K-9)\widetilde\Gamma_\Delta}{5^d}
-\widehat{\mathcal T}_2.
\]

代入 (6.1) 后 `That_2` 完全消去：

\[
\widehat{\mathcal T}_2
-5^{\nu_5}\widehat{\mathscr R}_{63}
=
\frac{D(2K-9)\widetilde\Gamma_\Delta}{5^d}
-5^{\nu_5}U_{63}.
\]

利用

\[
D/5^d=g2^m,
\qquad
\widetilde\Gamma_\Delta=c_u^2B_\Delta,
\]
以及直接整理 `U_63` 的 powers，得到

\[
\boxed{
\mathscr D_{63}
=2^mc_u^2\mathscr F_{63},}
\tag{7.1}
\]

其中

\[
\boxed{
\mathscr F_{63}
:=(2K-9)B_\Delta
-\frac{63}{16}gTK^2.}
\tag{7.2}
\]

`gTK^2/16` 为整数，因为

\[
v_2(gTK^2)\ge(t-1)+m+2\ge9.
\]

---

## 8. `F_63` is positive and almost exactly `1/16` of the parent scale

写

\[
\delta=C/D,
\qquad
\zeta=a_3/T.
\]

有 exact

\[
\frac{B_\Delta}{gT}
=2K-12-2\zeta+\delta.
\]

因此

\[
\boxed{
\frac{\mathscr F_{63}}{gTK^2}
=
\frac1{16}
-rac{2(21+2\zeta-\delta)}K
+rac{9(12+2\zeta-\delta)}{K^2}.}
\tag{8.1}
\]

当前

\[
1<\zeta<251/250,
\qquad0<\delta<3/250,
\qquad K>9\cdot10^{11}.
\]

所以 correction的绝对量远小于 `10^{-9}`，并且线性负项主导正的 `K^{-2}` 项。安全地得到

\[
\boxed{
\frac{31}{500}
<
\frac{\mathscr F_{63}}{gTK^2}
<
\frac1{16}.}
\tag{8.2}
\]

结合 (7.1)：

\[
\boxed{
\frac{31}{500}
<
\frac{\mathscr D_{63}}
{2^mc_u^2gTK^2}
<
\frac1{16}.}
\tag{8.3}
\]

特别地

\[
\boxed{\mathscr D_{63}>0.}
\tag{8.4}
\]

此外 `B_Delta` 为 odd，`2K-9` 为 odd，而 `63gTK^2/16` 被 `4` 整除，因此 `F_63` 为 odd：

\[
\boxed{v_2(\mathscr D_{63})=m.}
\tag{8.5}
\]

---

## 9. the original carrier itself has a narrow natural window

为了比较 remainder relative size，先把 `That_2` 的 natural scale写清楚。由 §3 的 exact formula：

\[
\widehat{\mathcal T}_2
=2^mc_u^2g^2
[TK^2-(18T+4a_3)K+18a_3+55T]
-5^mQ_0^2N_0.
\]

定义

\[
\boxed{
\mathscr S_T:=2^mc_u^2g^2TK^2.}
\tag{9.1}
\]

令

\[
y:=\frac{10a_2}{N},
\qquad s=9+y.
\]

第二项相对主尺度精确为

\[
\boxed{
R_T(x,y)
:=\frac{Q^2N_0}{B^2K^2}
=
\frac{(x+2)^2(2025x^2+y^2)}
{100x^2(9+y)^2}.}
\tag{9.2}
\]

直接求导：

\[
\partial_xR_T
=
\frac{(x+2)(2025x^3-2y^2)}
{50x^3(y+9)^2}>0,
\]

\[
\partial_yR_T
=
-\frac{9(x+2)^2(225x^2-y)}
{50x^2(y+9)^3}<0
\]
在 endpoint box成立。因此 extremum在 corners：

\[
\boxed{
\frac{7497}{8000}
<R_T
<\frac{234947716}{250493929}.}
\tag{9.3}
\]

结合 `K>9*10^11` 的 negligible linear correction，得到

\[
\boxed{
\frac{31}{500}
<
\frac{\widehat{\mathcal T}_2}{\mathscr S_T}
<
\frac{63}{1000}.}
\tag{9.4}
\]

这也重新给出 `That_2>0` 的定量版本。

---

## 10. the residue is less than `1/24` of the original carrier

前一 remainder theorem给

\[
\widehat{\mathscr R}_{63}
<
\frac{\mathscr B_\Delta}{25\cdot2^{m+4}}.
\]

而 powers exact 满足

\[
\boxed{
\frac{5^{\nu_5}\mathscr B_\Delta}{2^{m+4}}
=\frac{\mathscr S_T}{16}.}
\tag{10.1}
\]

所以

\[
5^{\nu_5}\widehat{\mathscr R}_{63}
<\frac{\mathscr S_T}{400}.
\tag{10.2}
\]

用 (9.4) 的 lower bound：

\[
\frac{
5^{\nu_5}\widehat{\mathscr R}_{63}
}{\widehat{\mathcal T}_2}
<
\frac{1/400}{31/500}
=\frac5{124}
<\frac1{24}.
\]

所以

\[
\boxed{
0<5^{\nu_5}\widehat{\mathscr R}_{63}
<\frac1{24}\widehat{\mathcal T}_2.}
\tag{10.3}
\]

结合 (6.1)：

\[
\boxed{
\widehat{\mathcal T}_2
=5^{\nu_5}\widehat{\mathscr R}_{63}
+g\mathscr D_{63},}
\tag{10.4}
\]

其中两项均严格为正。

这是一条真正的 positive height descent decomposition。

---

## 11. nested support identity

由 (4.3)：

\[
\gcd(\widehat{\mathscr R}_{63},g)=1.
\]

从 (10.4)：

\[
\begin{aligned}
\gcd(\widehat{\mathcal T}_2,\widehat{\mathscr R}_{63})
&=
\gcd(g\mathscr D_{63},\widehat{\mathscr R}_{63})\\
&=
\boxed{
\gcd(\mathscr D_{63},\widehat{\mathscr R}_{63}).}
\end{aligned}
\tag{11.1}
\]

所以 original carrier 与 short remainder若复用任意 odd prime，该 prime必须继续进入 descended quotient `D_63`。

特别地，两者都是 positive `3 mod4` integers：

\[
\widehat{\mathcal T}_2\equiv3\pmod4,
\qquad
\widehat{\mathscr R}_{63}\equiv3\pmod4.
\]

因此它们的 odd-inert parity若试图共享 support，shared parity不能停在第一层；必须同时进入

\[
\boxed{
\widehat{\mathcal T}_2,
\quad
\widehat{\mathscr R}_{63},
\quad
\mathscr D_{63}.}
\tag{11.2}
\]

这就是 nested support descent。

---

## 12. current frontier

现在 original A2 inert carrier已被写成

\[
\boxed{
\widehat{\mathcal T}_2
=\underbrace{5^{\nu_5}\widehat{\mathscr R}_{63}}_{<\widehat T_2/24}
+\underbrace{g\mathscr D_{63}}_{>0}.}
\]

其中：

- `Rhat_63` 比其 parent natural scale短至少 `25` 倍，且为 `3 mod4`；
- `Rhat_63` 与 `g` 完全互素；
- `D_63` 相对 original scale少一整份 factor `g`，并有显式 positive quadratic form；
- any common prime of original/remainder must also divide `D_63`.

还不能称为 infinite descent，因为 `D_63` 尚未证明重新满足原 decimal/cofactor structural class。下一步最值得攻击的是

\[
\gcd(\mathscr D_{63},\widehat{\mathscr R}_{63}),
\]

若能把它压到 fixed/denominator support，就会强迫 original carrier和 short remainder使用不同 inert primes，从而给 global A2 parity一个真实 multiplicative surcharge。

A2 仍为 `待证`。

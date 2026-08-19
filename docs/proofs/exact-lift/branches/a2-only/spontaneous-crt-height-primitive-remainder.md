# A2 height descent remainder 的 exact `5^{2d}` primitive reduction

> **依赖：** `spontaneous-crt-height-remainder-descent.md`、`spontaneous-crt-dual-gap-remainder.md`。
>
> **严格状态：**前一 descent theorem构造 positive primitive-2 remainder `Rhat_63`，并得到 `That_2=5^{nu_5}Rhat_63+gD_63`。本文继续审计 `Rhat_63` 的 5-adic content，证明其深度精确为 `2d`。除去该 content 后得到 fully `(2,5)`-primitive positive `3 mod4` carrier `Rstar_63`，且 `gcd(Rstar_63,10g)=1`。由于 `nu_5+2d=lambda`，descent 自动升级为 `That_2=5^lambda Rstar_63+gD_63`；小余数承担的是完整 reflection `5^lambda` depth，并仍小于原 carrier的 `1/24`。本文尚未把 `Rstar_63` 重新识别为原 decimal structural class，因此不宣称 infinite descent或 A2 closure。

---

## 1. exact formula for `J_Delta`

前一 theorem定义

\[
\mathscr J_\Delta
=
\frac{
D(2K-9)\widetilde\Gamma_\Delta
-\widetilde{\mathcal T}_2
}{5^{\lambda-d}}.
\tag{1.1}
\]

使用

\[
D=gL,
\qquad
L=2^m5^d,
\]

\[
\widetilde\Gamma_\Delta
=c_u^2\{g((2K-12)T-2a_3)+5^\lambda C\},
\]

以及

\[
\widetilde{\mathcal T}_2
=Lc_u^2g^2
[TK^2-(18T+4a_3)K+18a_3+55T]
-5^{\lambda+2d}Q_0^2N_0,
\]
直接展开 numerator。

其中不含 `C` 的两个大 bracket发生精确消元：

\[
\boxed{
(2K-9)((2K-12)T-2a_3)
-
[TK^2-(18T+4a_3)K+18a_3+55T]
=T(3K^2-24K+53).}
\tag{1.2}
\]

因此除去 `5^{lambda-d}` 后得到 exact positive formula

\[
\boxed{
\begin{aligned}
\mathscr J_\Delta
=5^{2d}\Bigl[
&2^{2m}5^dc_u^2g^2(3K^2-24K+53)\\
&+2^mgc_u^2C(2K-9)\\
&+5^dQ_0^2N_0
\Bigr].
\end{aligned}}
\tag{1.3}
\]

---

## 2. exact `5`-depth of `J_Delta`

定义中括号为 `J_0`。当前

\[
5\nmid g c_u C Q_0N_0,
\qquad
K=10P,
\]
所以

\[
2K-9\equiv-9\equiv1\pmod5.
\]

(1.3) 中第一、第三项都含显式 `5^d`，而第二项为 unit。因此

\[
\boxed{
\mathscr J_0
\equiv2^mgc_u^2C
\not\equiv0\pmod5.}
\tag{2.1}
\]

故

\[
\boxed{v_5(\mathscr J_\Delta)=2d.}
\tag{2.2}
\]

---

## 3. `U_63` is much deeper at `5`

前一 theorem写

\[
\widehat{\mathscr R}_{63}
=U_{63}-\mathscr J_\Delta,
\]

\[
U_{63}
:=\frac{63c_u^2D^2LK^2}{2^{m+4}}.
\]

因为

\[
v_5(D)=d,
\qquad
v_5(L)=d,
\qquad
v_5(K)=1,
\]
有

\[
\boxed{v_5(U_{63})=3d+2.}
\tag{3.1}
\]

而 `d>=1`：

\[
3d+2>2d.
\]

由 (2.2)，两项 5-depth不同，所以不存在首层 cancellation：

\[
\boxed{v_5(\widehat{\mathscr R}_{63})=2d.}
\tag{3.2}
\]

---

## 4. fully primitive short remainder

定义

\[
\boxed{
\mathscr R_{63}^\star
:=
\frac{\widehat{\mathscr R}_{63}}{5^{2d}}.}
\tag{4.1}
\]

前一 theorem已有

\[
\widehat{\mathscr R}_{63}>0,
\qquad
\widehat{\mathscr R}_{63}\equiv3\pmod4,
\qquad
\gcd(\widehat{\mathscr R}_{63},g)=1.
\]

由于 `5^{2d}≡1 mod4`，结合 (3.2)：

\[
\boxed{
\mathscr R_{63}^\star>0,
\qquad
\mathscr R_{63}^\star\equiv3\pmod4,}
\tag{4.2}
\]

\[
\boxed{
\gcd(\mathscr R_{63}^\star,10g)=1.}
\tag{4.3}
\]

所以 `Rstar_63` 是真正的 fully `(2,5)`-primitive external odd-inert carrier。

模 `5` 还能从 (2.1) 读取：由于 `U_63/5^{2d}` 仍被 `5` 整除，

\[
\boxed{
\mathscr R_{63}^\star
\equiv
-2^mgc_u^2C
\pmod5.}
\tag{4.4}
\]

---

## 5. denominator residue after primitive reduction

前一 theorem有

\[
\widehat{\mathscr R}_{63}
\equiv-c_u^25^dC^2
\pmod g.
\]

代入 `Rhat=5^{2d}Rstar`，并消去一个 `5^d`：

\[
\boxed{
5^d\mathscr R_{63}^\star
\equiv-c_u^2C^2
\pmod g.}
\tag{5.1}
\]

因此

\[
\boxed{
5^\lambda\mathscr R_{63}^\star
\equiv
-c_u^25^{\lambda-d}C^2
\equiv
\widehat{\mathcal T}_2
\pmod g.}
\tag{5.2}
\]

---

## 6. descent upgrades from `5^{nu_5}` to full `5^lambda`

前一 theorem定义

\[
\mathscr D_{63}
=
\frac{
\widehat{\mathcal T}_2
-5^{\nu_5}\widehat{\mathscr R}_{63}
}{g}.
\]

因为

\[
\widehat{\mathscr R}_{63}=5^{2d}\mathscr R_{63}^\star,
\qquad
\nu_5+2d=\lambda,
\]
得到真正的 fully primitive descent：

\[
\boxed{
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g\mathscr D_{63}.}
\tag{6.1}
\]

三因子满足

\[
\widehat{\mathcal T}_2>0,
\qquad
\mathscr R_{63}^\star>0,
\qquad
\mathscr D_{63}>0.
\]

---

## 7. the full-`5^lambda` remainder is still under `1/24`

此前已有

\[
0<5^{\nu_5}\widehat{\mathscr R}_{63}
<\frac1{24}\widehat{\mathcal T}_2.
\]

左边正是

\[
5^{\nu_5+2d}\mathscr R_{63}^\star
=5^\lambda\mathscr R_{63}^\star.
\]

因此

\[
\boxed{
0<5^\lambda\mathscr R_{63}^\star
<\frac1{24}\widehat{\mathcal T}_2.}
\tag{7.1}
\]

等价地

\[
\boxed{
0<\mathscr R_{63}^\star
<\frac{
\widehat{\mathcal T}_2
}{24\cdot5^\lambda}.}
\tag{7.2}
\]

这是相对于 original forced inert carrier 的 full reflection-depth height drop。

---

## 8. nested support identity in fully primitive form

由 (4.3) 与 (6.1)：

\[
\begin{aligned}
\gcd(\widehat{\mathcal T}_2,\mathscr R_{63}^\star)
&=\gcd(g\mathscr D_{63},\mathscr R_{63}^\star)\\
&=\boxed{
\gcd(\mathscr D_{63},\mathscr R_{63}^\star).}
\end{aligned}
\tag{8.1}
\]

所以 original carrier 与 fully primitive short remainder若共享 odd prime，该 prime必须继续进入 descended quotient `D_63`。

而

\[
\widehat{\mathcal T}_2\equiv3\pmod4,
\qquad
\mathscr R_{63}^\star\equiv3\pmod4.
\]

因此 global parity要想用同一 inert prime复用两份 `3 mod4` orientation，必须支付一个三重 overlap：

\[
\boxed{
p\mid
\widehat{\mathcal T}_2,
\quad
p\mid\mathscr R_{63}^\star,
\quad
p\mid\mathscr D_{63}.}
\tag{8.2}
\]

---

## 9. current role

原 A2 核现在存在一个相当强的 strict descent package：

\[
\boxed{
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star+g\mathscr D_{63},}
\]

其中

- `Rstar_63` 是 positive、fully `(2,5)`-primitive、`3 mod4`；
- `gcd(Rstar_63,g)=1`；
- scaled remainder `<That_2/24`；
- any parity reuse with original forces entry into positive quotient `D_63`.

这已经比普通“存在另一个 inert carrier”强很多，但还不能称为 infinite descent：`Rstar_63` 尚未证明具有原 `That_2` 的 rational-root/cofactor origin，`D_63` 也尚未回到同一 coefficient plane。

下一步应优先研究 `gcd(Rstar_63,D_63)` 的 explicit gate，或证明 `Rstar_63` 的 inert prime无法属于原三类 prime-source中的任一 already-paid support。

A2 仍为 `待证`。

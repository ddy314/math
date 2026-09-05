# A2 outer-pair / descendant-common 的 external `Q_4` root splitter

> **依赖：** `outer-descendant-additive-lock.md`、`outer-cofactor-reuse-gate.md`、`endpoint-lattice.md` §§16.27–16.36、`crt-descent-ledger.md` 中 universal descendant cubic / projective depth reader / terminal character。
>
> **严格状态：**本文继续处理危险 `Z≡1 (mod4)` orientation 中，同一枚 genuine non-`3` inert prime 同时支付 `Xi_-`,`Xi_+` 且进入 descendant common gcd `G_Delta` 的情形。上一层已把这种 shared reuse 压到 `K=3`、`2K-9=0` 或 irreducible quartic `Q_4(K)=0`。本文证明 central branch 对 non-`3` prime 实际为空；generic `Q_4` 上 rational-root quartic 的四个根被刚化为 `2,3,4,2K-2zeta-9`。若真实根是第四根，则同一 prime 会同时进入三个 cofactor，继而通过 curvature bridge 与 `Dhat_63` 产生 genuine contradiction；若真实根撞 `2` 或 `4`，完整 resultant 只剩 split support，故 inert sector为空。最后 `r=3` 即 `p|C` 的中心 natural-representative collision 被 `Dhat_63` 再压成唯一 genuinely external fixed prime `p_C=24303427940647`。该 prime 通过 first-layer equations，但 `(-26/p_C)=+1`，因此不能沿同一 prime 进入 terminal overdepth。本文仍不排除 `p_C` 的 first-layer payment，也不宣称 A2 空。

---

## 1. additive lock 的三张 `K` sheet

沿用

\[
R_0(K,\zeta)=K^2-(18+4\zeta)K+18\zeta+55
\]

以及首一四次式

\[
\Phi_0(J)
=J(J+2\zeta)(K-J)^2-R_0(J+\zeta)^2.
\tag{1.1}
\]

若同一 genuine prime `p` 同时整除 `Xi_-`,`Xi_+` 且 `p|G_\Delta`，`outer-descendant-additive-lock.md` 已给

\[
\Phi_0(2)\equiv\Phi_0(4)\equiv0\pmod p.
\tag{1.2}
\]

记

\[
P_2:=\Phi_0(2),\qquad P_4:=\Phi_0(4),
\]

\[
H_{24}:=\frac{P_4-P_2}{4}
=4K\zeta^2+18K\zeta+26K-18\zeta^2-81\zeta-105.
\tag{1.3}
\]

exact resultant 为

\[
\boxed{
\operatorname{Res}_\zeta(P_2,H_{24})
=2(K-3)^2(2K-9)Q_4(K),}
\tag{1.4}
\]

其中

\[
\boxed{
Q_4(K)=676K^4-8004K^3+34801K^2-65868K+45964}
\tag{1.5}
\]

在 `Q[K]` 中不可约。

因此 non-`2` shared prime 必落在

\[
K=3,\qquad 2K-9=0,\qquad Q_4(K)=0
\tag{1.6}
\]

三类之一。

---

## 2. central factor 对 non-`3` prime 实际为空

把

\[
K=\frac92
\]

代回两个 outer equations：

\[
P_2=\frac{23\zeta^2+192\zeta+192}{4},
\]

\[
P_4=\frac{23\zeta^2+192\zeta+384}{4}.
\]

所以

\[
\boxed{P_4-P_2=48.}
\tag{2.1}
\]

故若 odd `p` 同时满足 `2K-9=0` 与 (1.2)，必有 `p|48`。在当前 non-`3` inert sector 不可能。

因此

\[
\boxed{2K-9=0\text{ 不是 genuine external shared-reuse branch}.}
\tag{2.2}
\]

---

## 3. `K=3` 是 root-collision sheet

在 `K=3`：

\[
P_2=-2(\zeta+3)(3\zeta^2+8\zeta+6),
\]

\[
P_4=-2(\zeta+3)(3\zeta^2+20\zeta+24).
\]

两式在 characteristic 非 `2,3` 的公共因子只有

\[
\boxed{\zeta+3.}
\tag{3.1}
\]

代入 `K=3,\zeta=-3`，完整 rational-root quartic 化为

\[
\boxed{
\Phi_0(r)=(r-4)(r-3)^2(r-2).}
\tag{3.2}
\]

所以 `K=3` 并非新的自由 external surface；真实 root 只能撞到 `2,3,4`，且 `r=3` 为双根。以下真正的 moving analysis只需处理 `Q_4=0`。

---

## 4. generic `Q_4` 上 `zeta` 只有一个线性 reader

对 `P_2,P_4` 关于 `zeta` 取 subresultant chain。最后一个正次数 subresultant 为

\[
64(2K-9)^2L_1(K,\zeta),
\]

其中

\[
\boxed{
\begin{aligned}
L_1={}&(18K^3-185K^2+612K-648)\zeta\\
&+26K^3-297K^2+1052K-1158.
\end{aligned}}
\tag{4.1}
\]

记 `zeta` 系数为 `A_1(K)`。其与 `Q_4` 的 resultant 为

\[
\boxed{
|\operatorname{Res}(Q_4,A_1)|
=2^{10}23^2 29^2 31^2.}
\tag{4.2}
\]

常数项的 resultant 为

\[
\boxed{
2^{15}\cdot13\cdot23\cdot29^2\cdot31^2.}
\tag{4.3}
\]

所以除 fixed `23,31`（以及 split `13,29`）外，generic `Q_4` root 上

\[
\boxed{\zeta=-B_1(K)/A_1(K)}
\tag{4.4}
\]

唯一确定。fixed `23/31` 在 checker 中保留为 coefficient-singular audit，不把它们混入 generic division。

---

## 5. `Q_4` 上第三个整数点自动成为 root

把 (4.4) 代入 `Phi_0(3)`，清分母后的 numerator 对 `Q_4(K)` 的余数严格为 `0`。因此：

\[
\boxed{Q_4=0,\ L_1=0\Longrightarrow \Phi_0(3)=0.}
\tag{5.1}
\]

而 `Phi_0(J)` 是首一四次式，其 `J^3` 系数给根和

\[
\sum r_i=2K-2\zeta.
\]

三个根已经是 `2,3,4`，故第四根必为

\[
\boxed{r_\star=2K-2\zeta-9.}
\tag{5.2}
\]

所以 generic `Q_4` shared-reuse 中，真实 rational root

\[
r=3-C/D
\]

只能满足

\[
\boxed{r\in\{2,3,4,r_\star\}\pmod p.}
\tag{5.3}
\]

这把原二维 modular freedom 压成四个 natural-root slots。

---

## 6. 真实根若等于第四根，则 genuine external 立即矛盾

若

\[
r=r_\star
\]

且与 `2,3,4` 均不同，则 `2,3,4` 全是 actual root 之外的三个整数根。因此同一 `p` 同时整除

\[
\Xi_-,\qquad\Xi_C,\qquad\Xi_+.
\tag{6.1}
\]

于是两个相邻 gap 都被 `p` 整除。`endpoint-lattice.md` §16.34 的 exact curvature identity为

\[
\Delta_--\Delta_+
=2^{m+1}5^dc_u^2B_\Delta,
\tag{6.2}
\]

其中

\[
B_\Delta=g((2K-9)T-a_3)-H_0.
\]

对 genuine external prime，`p∤2\cdot5c_u`，故 (6.1)–(6.2) 给

\[
\boxed{p\mid B_\Delta.}
\tag{6.3}
\]

另一方面 `p|G_\Delta` 给 `p|\widehat D_{63}`，而

\[
\widehat D_{63}
=c_u^2\left((2K-9)B_\Delta-\frac{63}{16}gTK^2\right).
\tag{6.4}
\]

若 `p` genuinely external，即

\[
p\nmid2\cdot3\cdot7\,c_ugTK,
\]

则 (6.3),(6.4) 强迫

\[
p\mid63,
\]

矛盾。因此：

\[
\boxed{r=r_\star\text{ 的 generic genuine external branch为空}.}
\tag{6.5}
\]

fixed `3,7` 与 coefficient-content cases仍由各自旧账本处理，不在这里重复收费。

---

## 7. `r=2` 与 `r=4` collision 没有 non-`3` inert support

若真实 root `r=2`，则

\[
p\mid D-C.
\]

而当前同一 prime还整除 `Xi_-`。因此 root `2` 在 mod `p` quartic 中必须至少为双根；在 (5.3) 中这意味着

\[
r_\star=2,
\qquad
\zeta=K-\frac{11}{2}.
\tag{7.1}
\]

将 (7.1) 代入 `P_2,P_4`，分别与 `Q_4` 对 `K` 求 resultant。任何共同 prime必须整除两个 resultants的 gcd，而 checker得到

\[
\boxed{
\gcd(R_2^{(2)},R_4^{(2)})
=2^{12}3^3\cdot137.}
\tag{7.2}
\]

其中

\[
137\equiv1\pmod4.
\]

所以 non-`3` inert prime不存在。

同理，若真实 root `r=4`，`p|D+C` 且 `p|Xi_+` 迫使

\[
r_\star=4,
\qquad
\zeta=K-\frac{13}{2}.
\tag{7.3}
\]

对应两个 resultants 的 gcd 为

\[
\boxed{
2^{24}3^3\cdot17,}
\tag{7.4}
\]

而 `17≡1 (mod4)`。因此：

\[
\boxed{r=2\text{ 或 }r=4\text{ 的 shared external inert branch全部为空}.}
\tag{7.5}
\]

这与旧 `floorfree-modulus-overlap` 中 `D-C,D+C` 两张 short carrier接口一致，但这里直接使用完整 additive-locked outer system，不需要额外高度估计。

---

## 8. 唯一剩余 root collision 是 `r=3`, 即 `p|C`

由 (5.3),(6.5),(7.5)，generic shared external prime只能满足

\[
\boxed{r=3\Longleftrightarrow p\mid C.}
\tag{8.1}
\]

现在把 `C=0` 代回 source identity

\[
H_0=g(3T+a_3)-5^\lambda C
\]
得到

\[
H_0\equiv g(3T+a_3)\pmod p.
\]

故

\[
B_\Delta
=g((2K-9)T-a_3)-H_0
\equiv2gT(K-6-\zeta).
\]

再代入 `p|\widehat D_{63}`，除去 genuine units `c_u,g,T`，得到新的线性 `zeta` gate

\[
\boxed{
K^2-64K\zeta-672K+288\zeta+1728=0.}
\tag{8.2}
\]

若 `2K-9` 为 unit，可写成

\[
\boxed{
\zeta=
\frac{K^2-672K+1728}{32(2K-9)}.}
\tag{8.3}
\]

把 (8.3) 分别代入 `P_2,P_4`，再各自与 `Q_4` 对 `K` 消元。两 resultant 的 gcd 完整分解为

\[
\boxed{
2^{18}\cdot7\cdot23^2\cdot24303427940647.}
\tag{8.4}
\]

记

\[
\boxed{p_C:=24303427940647.}
\tag{8.5}
\]

`p_C` 为素数且 `p_C≡3 (mod4)`。

`p=23` 对应 `2K-9=0` 的 central denominator，已由 §2 删除；`p=7` 落回 `K=3` fixed sheet。故 genuine external 中只剩

\[
\boxed{p=p_C.}
\tag{8.6}
\]

checker还给出真实 first-layer residue

\[
\boxed{
K_C=21805672591624,
\qquad
\zeta_C=9250192938088
\pmod{p_C},}
\tag{8.7}
\]

它确实同时满足 `Q_4,P_2,P_4,(8.2)`，并满足 universal descendant cubic `E_63=0`。所以这不是 resultant 的扩域伪根，不能在 first layer直接删除。

---

## 9. `p_C` 不能沿同一 prime进入 terminal overdepth

`p_C` 的 decimal order为

\[
\operatorname{ord}_{p_C}(10)=p_C-1,
\tag{9.1}
\]

故单纯 decimal orbit没有删掉它。

但旧 terminal-character theorem要求：若同一 terminal descendant label还要继续 quartic overdepth，则必须满足

\[
\left(\frac{-26}{p}\right)=-1.
\tag{9.2}
\]

而 checker精确给

\[
\boxed{
\left(\frac{-26}{p_C}\right)=+1.}
\tag{9.3}
\]

因此 `p_C` 即使承担 first-layer external common / shared outer payment，也不能沿**同一 prime**走到 terminal overdepth。它若要继续 recycling，必须在中途停止并把剩余 parity交给其它 support。

这已经把 genuine external shared-reuse 从 moving family 压成一个 fixed first-layer exception，并且该 exception没有 terminal self-recycling能力。

---

## 10. 当前 frontier

危险 `Z=1` 中，同一 non-`3` inert prime若想同时支付 `Xi_-`,`Xi_+` 并复用 `G_\Delta`：

1. source-common old pool 已由 `outer-descendant-additive-lock.md` 删除；
2. central `2K-9` branch为空；
3. generic `Q_4` 的 fourth-root branch为空；
4. `r=2,4` natural-root collision为空；
5. `r=3` 只剩 fixed `p_C=24303427940647`；
6. `p_C` 与 terminal overdepth character不兼容。

因此 shared-reuse 的真正剩余已经不是 unbounded external modular kernel，而是：

\[
\boxed{
\text{one fixed first-layer }p_C
+\text{its pre-terminal spill / parity handoff}.}
\]

本文没有证明该 handoff本身矛盾，所以 `A2` 仍为 `待证`。

---

## 11. verification

```bash
uv run python scripts/exact-lift/a2-only/research-checks/crt-descent/check_a2_outer_external_q4_root_split.py
```

# DD corrected terminal 的 source/carry `epsilon` cancellation 与 full source period

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-neighborhood-square-source-crt-2026-08-22.md`](dd-corrected-neighborhood-square-source-crt-2026-08-22.md)、[`dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md`](dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md)、[`dd-corrected-neighborhood-gap-fiber-entropy-2026-08-22.md`](dd-corrected-neighborhood-gap-fiber-entropy-2026-08-22.md)、[`dd-corrected-source-carry-sigma-overlap-2026-08-22.md`](dd-corrected-source-carry-sigma-overlap-2026-08-22.md)。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` terminal neighborhood）。**
>
> 前一 `source-carry-sigma-overlap` 文件允许 `a_3` 移动时只从候选差分读取 source period，因此留下
> \[
> D_\Sigma=(q_Q^2,\Sigma)
> \]
> 作为 apparent hard overlap。本文使用此前已经存在但没有同时代入的两个 exact parents，证明 `w` 可以先在整数恒等式中约掉；真正可能损失的只是 `epsilon=(c_3,\Sigma)`。随后 denominator valuation 证明
> \[
> \boxed{(q_Q,\varepsilon)=1.}
> \]
> 所以实际上完整 `q_Q^2` period在消去 `a_3` 后仍保留：
> \[
> \boxed{
> q_Q^2\mid
> g_0B10^dV A_{12}-XR_0.}
> \]
> 因而 `D_Sigma` 不再是开放 hard core。

---

## 1. 三条已经严格存在的 exact identity

沿用

\[
F:=5^T,
\qquad
X=2^HZ,
\qquad
Y=FU,
\qquad
V=X-Y,
\]

\[
\boxed{\Sigma:=X+Y=2FU+V.}
\tag{1.1}
\]

`core.md` §37 的 reduced-tail normalization为

\[
u=LQ_1=2FU,
\qquad
v=V,
\]

\[
\boxed{u+v=\varepsilon w=\Sigma,}
\qquad
\boxed{c_3=\varepsilon c.}
\tag{1.2}
\]

上一 square-source theorem定义

\[
S_Q:=LV\omega10^dA_{12}+a_3(LQ_1+2V)
\]

并已经严格证明

\[
\boxed{
S_Q=w\frac{H_{\rm sph}+y_3}{c}.}
\tag{Generic-Q-parent}
\]

以及

\[
\boxed{
q_Q^2\mid\frac{H_{\rm sph}+y_3}{c}.}
\tag{Square-source}
\]

另一方面 generic carry compatibility 已给

\[
\boxed{
g_0US_Q
=2\Sigma\left(
 g_0B10^dVA_{12}-XR_0
\right).}
\tag{Q-parent-carry}
\]

这些式子都在整个 corrected canonical funnel中成立，不需要 equality `q_c,C_L` normalization。

---

## 2. 先约掉 `w`，真正 overlap 只是 `epsilon`

由 `(Square-source)` 定义整数

\[
\boxed{
K_Q:=\frac{H_{\rm sph}+y_3}{c q_Q^2}
\in\mathbf Z_{>0}.}
\tag{2.1}
\]

于是 `(Generic-Q-parent)` 精确变成

\[
\boxed{S_Q=wq_Q^2K_Q.}
\tag{2.2}
\]

代入 `(Q-parent-carry)`，再使用 `Sigma=epsilon w`：

\[
 g_0U wq_Q^2K_Q
=2\varepsilon w
\left(g_0B10^dVA_{12}-XR_0\right).
\]

所有量为整数且 `w>0`，所以可以在**整数等式本身**中约去 `w`：

\[
\boxed{
 g_0U q_Q^2K_Q
=2\varepsilon
\left(g_0B10^dVA_{12}-XR_0\right).}
\tag{Epsilon-parent}
\]

因此 previous difference argument 中出现的 `Sigma` overlap是过度损失。真正需要审计的是

\[
\boxed{(q_Q,\varepsilon).}
\]

---

## 3. 核心 denominator lemma：`q_Q` 与 `epsilon` 互素

### 命题

\[
\boxed{(q_Q,\varepsilon)=1.}
\tag{Q-epsilon-coprime}
\]

### 证明

反设存在奇素数

\[
p\mid q_Q,
\qquad
p\mid\varepsilon.
\tag{3.1}
\]

`q_Q` 只含非十进制素数。上一 square-source theorem已经证明

\[
\boxed{(q_Q,V)=1,}
\]

所以

\[
p\nmid V.
\tag{3.2}
\]

而 `epsilon|(u+v)=Sigma`，故 `p|Sigma`。由

\[
\Sigma=u+V
\]

和 `(3.2)`，立即有

\[
p\nmid u.
\]

canonical `u=2*5^T U`，因此

\[
\boxed{p\nmid U.}
\tag{3.3}
\]

记

\[
s:=v_p(q)>0.
\]

由 `Q=Uq` 与 `(3.3)`：

\[
\boxed{v_p(Q)=s.}
\tag{3.4}
\]

又 canonical third-denominator factorization给

\[
b_3=BVq,
\]

其中 `B` 为 2,5-smooth，且 `p∤V`。故

\[
\boxed{v_p(b_3)=s.}
\tag{3.5}
\]

令

\[
e_1:=v_p(b_1),
\qquad
e_2:=v_p(b_2).
\]

因为

\[
Q=b_1 10^{m_2}+b_2
\]

且 `p∤10`，只需分两种情况。

### 3.1 若 `e_1 != e_2`

两项 valuation不同，所以

\[
s=\min(e_1,e_2).
\]

不妨 `e_1=s<e_2`。由 `(3.5)`：

\[
v_p(q_{\rm lcm})=e_2,
\]

所以

\[
v_p(c_3)=e_2-s.
\]

而

\[
g_*=\frac G{c_3},
\qquad
\widehat g=\frac{g_*}{V},
\]

且 `p∤V`。因此

\[
\begin{aligned}
v_p(\widehat g)
&=e_1+e_2-(e_2-s)\\
&=2s.
\end{aligned}
\tag{3.6}
\]

但 `q_Q` 的 local exponent定义为

\[
f_p=
\max\left(
 s-v_p(\widehat g)
 -\left\lceil\frac{v_p(H-y_3)}2\right\rceil
 -\left\lceil\frac{v_p(c)}2\right\rceil,
0\right).
\]

由 `(3.6)`：

\[
f_p\le\max(s-2s,0)=0,
\]

与 `p|q_Q` 矛盾。

### 3.2 若 `e_1=e_2=:E`

此时 `(3.4)` 给

\[
s\ge E.
\]

再由 `(3.5)`，三 denominator 的 p-depth为

\[
E,E,s.
\]

所以

\[
v_p(q_{\rm lcm})=s,
\qquad
v_p(c_3)=v_p(q_{\rm lcm}/b_3)=0.
\tag{3.7}
\]

但

\[
\varepsilon=(c_3,u+v)\mid c_3,
\]

故 `(3.7)` 给 `p∤epsilon`，再次与 `(3.1)` 矛盾。

两种情况都不可能，因此 `(Q-epsilon-coprime)` 得证。

---

## 4. full source-square fixed CRT

从 `(Epsilon-parent)`，左边显式被 `q_Q^2` 整除，所以

\[
q_Q^2
\mid
2\varepsilon
\left(g_0B10^dVA_{12}-XR_0\right).
\]

`q_Q` 为 odd rough integer，而 `(Q-epsilon-coprime)` 给

\[
(q_Q,2\varepsilon)=1.
\]

因此

\[
\boxed{
q_Q^2\mid
g_0B10^dVA_{12}-XR_0.}
\tag{Full-source-parent}
\]

还需检查 `A_12` coefficient。固定 `p|q_Q`：

- `p∤B10`，因为 `B` 2,5-smooth；
- `p∤V`，由 `Source-moving-transverse`；
- `p∤epsilon`，由本文命题；
- `R_0/g_0=La_0/(2*5^T epsilon)` 已约成最低项，右侧 denominator在 p 处为 unit，因此 `p∤g_0`。

故

\[
\boxed{(q_Q,g_0B10^dV)=1.}
\tag{4.1}
\]

于是得到真正 fixed 的 source congruence

\[
\boxed{
 g_0B10^dV A_{12}
\equiv XR_0
\pmod{q_Q^2}.}
\tag{Full-source-CRT}
\]

它与 old equality `Q-fixed` 具有完全相同的语义，但现在适用于整个 corrected terminal neighborhood，并且**不含 `a_3`**。

---

## 5. `D_Sigma` hard core 正式降级

前一文件从两个候选做差得到

\[
\frac{q_Q^2}{(q_Q^2,\Sigma)}\mid\Delta A_{12}.
\]

该结论本身仍正确，但不 sharp。本文的 `(Full-source-CRT)` 对同一 fixed gap fiber中的任意两个 candidates直接给

\[
\boxed{q_Q^2\mid\Delta A_{12}.}
\tag{5.1}
\]

所以

\[
\boxed{
D_\Sigma=(q_Q^2,\Sigma)
\text{ 不再造成 source-period loss。}}
\tag{Sigma-hard-superseded}
\]

`dd-corrected-source-carry-sigma-overlap-2026-08-22.md` 应保留为一次安全但非 sharp 的 intermediate audit；其“下一 hard core 是 `D_Sigma`”状态由本文替代。

---

## 6. 与 pair-max period 的 full transverse product

pair-max neighborhood theorem给 fixed residue

\[
A_{12}\equiv\rho_V\pmod{v_2},
\]

且

\[
\frac{\log_{10}v_2}{S}
\ge1-C_{\rm one}\delta-o(1),
\]

\[
C_{\rm one}=2.335049992773302\ldots.
\]

square-source theorem给

\[
\frac{\log_{10}q_Q}{S}
\ge z_*-\delta-o(1),
\qquad
z_*=0.308883577618031\ldots,
\]

并且

\[
(q_Q,v_2)=1.
\]

因此即使允许 `a_3` 通过 carry随 `A_12` 移动，两个 fixed periods仍是 exact transverse product

\[
\boxed{M_{QV}=q_Q^2v_2.}
\tag{6.1}
\]

以及

\[
\boxed{
\frac{\log_{10}M_{QV}}S
\ge
1.617767155236062\ldots
-4.335049992773302\ldots\delta-o(1).}
\tag{6.2}
\]

所以此前

\[
\boxed{
\delta_{\rm CRT}=0.142505197463905\ldots}
\]

的 fixed-fiber uniqueness threshold现在不再要求额外固定 `a_3`；固定 denominator/S-unit data、`R_0,g_0,a_2` 已足够。

---

## 7. numerator entropy coefficient 改善

`dd-corrected-neighborhood-gap-fiber-entropy-2026-08-22.md` 已证明

\[
\#\{(R_0,g_0)\}
\le10^{\delta S+o(S)},
\]

以及

\[
\#\{a_2\}
\le10^{\kappa_{\rm dig}\delta S+o(S)},
\]

\[
\kappa_{\rm dig}
=0.767009998554660\ldots.
\]

在

\[
\delta<\delta_{\rm CRT}
\]

时，本文 full source CRT + full pair-max CRT 对 fixed `(R_0,g_0,a_2)` 直接令 `A_12` 至多一个；随后 carry唯一恢复 `a_3`。

因此 fixed denominator/S-unit data 下：

\[
\boxed{
N_{\rm num}(S;\delta)
\le
10^{C_{\rm num}\delta S+o(S)},}
\tag{7.1}
\]

其中

\[
\boxed{
C_{\rm num}
=1+\kappa_{\rm dig}
=1.767009998554660\ldots.}
\tag{7.2}
\]

这把前一 gap-fiber 文件的

\[
4.102059991327962\ldots
\]

显著降到

\[
\boxed{1.767009998554660\ldots.}
\]

更一般地，不要求 `delta<delta_CRT` 时，每个 `(R_0,g_0,a_2)` fiber 的 `A_12` 数量至多

\[
10^{[(2+C_{\rm one})\delta-2z_*]_+S+o(S)},
\]

所以

\[
\boxed{
N_{\rm num}(S;\delta)
\le
10^{\left[
(1+\kappa_{\rm dig})\delta
+[(2+C_{\rm one})\delta-2z_*]_+
\right]S+o(S)}.}
\tag{7.3}
\]

---

## 8. 新的真正 frontier：denominator / S-unit entropy

经过本文，corrected terminal neighborhood 中 numerator side 已经没有正高度 same-prime hard core：

1. `q_Q^2` 是 fixed source period；
2. `v_2` 是 fixed pair-max period；
3. 二者互素；
4. `a_3` 的移动不会损失 source period；
5. gap fiber本身只有 `delta S+o(S)` entropy；
6. short suffix只有 `kappa_dig delta S+o(S)` entropy。

因此 strict-gap 的主障碍正式转成：

\[
\boxed{
\text{满足同一 corrected canonical phase 的 denominator/S-unit data 有多少？}}
\]

首选接口是已证明的 Farey slack identity

\[
\left|\frac ZU-\frac{5^T}{2^H}\right|
=\frac{10^{\sigma_SS+o(S)}}{U^2},
\qquad
\sigma_S\le\delta/\lambda_*+o(1),
\]

结合

\[
Q=Uq,
\qquad
b_3=BVq,
\qquad
V=v_1v_2,
\qquad
v_1=10^{O(\delta S)},
\]

去量化 denominator/S-unit fiber count。

---

## 9. 状态摘要

- **已严格完成：** exact `w` cancellation `(Epsilon-parent)`。
- **已严格完成：** denominator lemma `(q_Q,epsilon)=1`。
- **已严格完成：** `Full-source-parent` 与 fixed `Full-source-CRT`，允许 `a_3` 移动。
- **状态修正：** `D_Sigma` apparent hard overlap降级为非 sharp intermediate artifact。
- **已严格完成：** numerator entropy coefficient从 `4.1020599913...` 改善为 `1.7670099986...`（`delta<delta_CRT`）。
- **当前开放核心：** denominator/S-unit entropy；unique CRT lift的 Archimedean location；explicit strict slope gap；DD emptiness与有效绝对高度界。

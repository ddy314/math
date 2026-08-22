# DD corrected terminal neighborhood 的 full pair-max period

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)、[`dd-corrected-neighborhood-square-source-crt-2026-08-22.md`](dd-corrected-neighborhood-square-source-crt-2026-08-22.md)、[`good-genuine-ledger.md`](good-genuine-ledger.md) 中 `pairmax-fixed-a12-crt` 的 `Sphere-pay-global` identity，以及 [`core.md`](core.md) §§28, 37--38 的 canonical denominator / overlap normalization。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` terminal neighborhood；fixed-fiber statement）。**
>
> equality frontier 中的 `Pairmax-GCRT0` 过去只在 low denominator baseline 为 `o(S)` 后使用。本文保留该 baseline，证明对 quantitative one-channel core
> \[
> V=v_1v_2,
> \qquad
> \log_{10}v_2\ge(1-C_{\rm one}\delta)S-o(S),
> \]
> 每个 `p^h||v_2` 仍提供完整 rational period `p^h`，没有 `Cr` 型损失。与新 generic square-source period `q_Q^2` 联立后，在
> \[
> \delta<0.1425051974639\ldots
> \]
> 的 neighborhood 内，固定 canonical denominator/source/gap fiber 至多存在一个 `A_12`。

---

## 1. one-channel prime 的完整 denominator baseline

沿用 canonical denominator normal form

\[
 b_1=h_0v_1B_1,
 \qquad
 b_2=h_0v_2B_2,
 \qquad
 b_3=h_0v_1v_2B_3,
\]

且

\[
(B_1B_2B_3,v_1v_2)=1,
\qquad
(v_1,v_2)=1.
\tag{1.1}
\]

固定

\[
p^h\Vert v_2,
\qquad p\nmid10.
\]

令

\[
r:=v_p(h_0).
\]

则 exact denominator pattern 为

\[
\boxed{
 v_p(b_1)=r,
 \qquad
 v_p(b_2)=v_p(b_3)=r+h.}
\tag{1.2}
\]

对应 lcm 满足

\[
v_p(q_{\rm lcm})=r+h.
\tag{1.3}
\]

prefix denominator concat

\[
Q=b_1 10^{m_2}+b_2
\]

的两项 p-depth 分别为 `r` 与 `r+h`，所以

\[
\boxed{v_p(Q)=r.}
\tag{1.4}
\]

canonical phase中

\[
Q=Uq,
\qquad
G=\gamma V,
\qquad
\kappa=2\gamma5^TU,
\qquad
(U,V)=1.
\tag{1.5}
\]

因为 `p|V`，有 `p∤U`，故

\[
\boxed{v_p(q)=r.}
\tag{1.6}
\]

又

\[
v_p(G)=v_p(b_1b_2)=2r+h,
\qquad
v_p(V)=h,
\]

所以

\[
\boxed{v_p(\gamma)=2r.}
\tag{1.7}
\]

同时

\[
\boxed{v_p(\kappa)=2r.}
\tag{1.8}
\]

写

\[
X=2^HZ,
\qquad
Y=5^TU,
\qquad
V=X-Y,
\qquad
\Sigma=X+Y.
\]

`p|V` 且 `p∤XY`，故

\[
\boxed{p\nmid\Sigma.}
\tag{1.9}
\]

于是

\[
\kappa+G=\gamma\Sigma,
\qquad
\kappa+2G=2\gamma X,
\]

给

\[
\boxed{
 v_p(\kappa+G)=v_p(\kappa+2G)=2r.}
\tag{1.10}
\]

---

## 2. generic carry 本来就存在，不依赖 equality

`core.md` §37--38 写

\[
Q=\eta Q_1,
\qquad
u=LQ_1,
\qquad
v=V,
\qquad
u+v=\varepsilon w,
\]

其中这里用 `u` 代替上式的 `nu`：

\[
u=LQ_1=2\cdot5^TU,
\qquad
\varepsilon w=\Sigma.
\tag{2.1}
\]

primitive equations 已给

\[
 v\omega A_{12}10^d-a_3Q_1=wa_0.
\tag{2.2}
\]

又

\[
B=\frac{10^m}{2\cdot5^T}
=\frac{L\omega}{2\cdot5^T}.
\tag{2.3}
\]

因此

\[
\begin{aligned}
BVA_{12}10^d-Ua_3
&=\frac{L}{2\cdot5^T}
\left(v\omega A_{12}10^d-a_3Q_1\right)\\
&=\frac{Lwa_0}{2\cdot5^T}\\
&=\Sigma\frac{La_0}{2\cdot5^T\varepsilon}.
\end{aligned}
\tag{2.4}
\]

把正有理数约成最低项

\[
\boxed{
\frac{R_0}{g_0}
:=\frac{La_0}{2\cdot5^T\varepsilon},
\qquad
(R_0,g_0)=1.}
\tag{2.5}
\]

便得到 generic exact carry

\[
\boxed{
 g_0Ua_3
 =g_0B10^dVA_{12}-\Sigma R_0.}
\tag{Carry-generic}
\]

所以 equality 文献中的 `R_0,g_0` 并非 equality 才产生的对象；equality 只进一步证明它们的高度为 `o(S)`。

对当前 `p^h||v_2`，`c_3=q_lcm/b_3` 为 p-unit，故 overlap 中 `varepsilon,c` 都是 p-units；`L` 为 2,5-smooth，`a_3` 由 `(a_3,b_3)=1` 为 p-unit。由

\[
\lambda vH_0-a_3\varepsilon=La_0
\]

第一项含正 p-depth、第二项为 unit，故

\[
\boxed{p\nmid a_0.}
\tag{2.6}
\]

因此 `(2.5)` 立即给

\[
\boxed{p\nmid g_0R_0.}
\tag{2.7}
\]

结合 `(1.9)`：

\[
\boxed{p\nmid g_0UR_0\Sigma B10.}
\tag{2.8}
\]

---

## 3. `Sphere-pay-global` 在 baseline `r` 下的齐次 valuation

沿用 split-independent W-free carrier

\[
A_c:=Q(a_2b_1)^2,
\]

\[
\mathscr T:=
\frac{\kappa^2(\kappa+2G)}{10^m},
\]

\[
\Theta:=(\kappa+G)A_c\beta+\mathscr T a_3^2,
\tag{3.1}
\]

以及 exact identity

\[
\boxed{
10^mG^2\Theta
=\kappa\left[
\kappa(\kappa+2G)\mathcal S_{\rm raw}
+G^2(a_2b_1)^2b_3^2
\right],}
\tag{Sphere-pay-global}
\]

其中

\[
\mathcal S_{\rm raw}
=(a_2b_1)^2b_3^2+G^2a_3^2.
\]

当前 prime 上由 reducedness

\[
p\nmid a_2a_3.
\]

从 `(1.2),(1.4)`：

\[
\boxed{v_p(A_c)=3r.}
\tag{3.2}
\]

而 full denominator tail concat `beta=10^mQ+b_3` 的两项深度为 `r,r+h`，故

\[
\boxed{v_p(\beta)=r.}
\tag{3.3}
\]

由 `(1.7),(1.10)`：

\[
\boxed{v_p(\mathscr T)=6r.}
\tag{3.4}
\]

pair-max sphere theorem给 residual square-depth

\[
p^{2h}\mid y_2^2+y_3^2.
\]

而

\[
\mathcal S_{\rm raw}
=b_1^2\left(\frac{b_2b_3}{q_{\rm lcm}}\right)^2
(y_2^2+y_3^2).
\]

显式 baseline 深度为

\[
2r+2(r+h)=4r+2h,
\]

再加 residual `2h`，得到

\[
\boxed{v_p(\mathcal S_{\rm raw})\ge4r+4h.}
\tag{3.5}
\]

于是 `Sphere-pay-global` 右侧方括号两项都有至少

\[
8r+4h
\]

的 p-depth；外层 `kappa` 再给 `2r`。左侧 `G^2` 有 `4r+2h`，所以

\[
\boxed{v_p(\Theta)\ge6r+2h.}
\tag{Pairmax-theta-neighborhood}
\]

这正是 old `2h` square-depth 加上一份齐次 `6r` baseline。

---

## 4. carry-square 在除去 `6r` 后恢复 old shape

把 `(Carry-generic)` 平方并代入 `g_0^2U^2Theta`。定义 constant part

\[
\boxed{
H_{V,0}:=
 g_0^2U^2(\kappa+G)A_c\beta
 +\mathscr T\Sigma^2R_0^2.}
\tag{4.1}
\]

则 exact 地

\[
\boxed{
\begin{aligned}
g_0^2U^2\Theta
={}&H_{V,0}
-2\mathscr T g_0B10^dV\Sigma R_0A_{12}\\
&+\mathscr T g_0^2B^210^{2d}V^2A_{12}^2.
\end{aligned}}
\tag{Carry-square-neighborhood}
\]

在当前 `p^h||v_2`：

\[
v_p(g_0^2U^2\Theta)\ge6r+2h,
\]

\[
v_p\!\left(
2\mathscr T g_0B10^dV\Sigma R_0
\right)=6r+h,
\]

\[
v_p\!\left(
\mathscr T g_0^2B^210^{2d}V^2
\right)=6r+2h.
\]

因此右侧 constant part必满足

\[
\boxed{v_p(H_{V,0})\ge6r+h.}
\tag{4.2}
\]

定义 local integer quotient

\[
\boxed{M_p:=H_{V,0}/p^{6r+h}.}
\tag{4.3}
\]

将 `(Carry-square-neighborhood)` 除以 `p^{6r+h}` 后模 `p^h`，左侧与 quadratic term都消失，得到

\[
\boxed{
2\frac{\mathscr T}{p^{6r}}
 g_0B10^d
 \frac{V}{p^h}
 \Sigma R_0\,A_{12}
\equiv M_p
\pmod{p^h}.}
\tag{Pairmax-local-CRT}
\]

由 `(2.8),(3.4)` 与 `p^h||V`，coefficient 是 p-unit。因此每个 `p^h||v_2` 对 rational integer `A_12` 给出**完整 period `p^h`**。

这里没有 `r`-dependent period loss；low denominator baseline 只形成齐次 `6r`，在 second-layer extraction 前整体约掉。

---

## 5. 聚合得到完整 `v_2` fixed period

不同 `p^h||v_2` 互素。对固定 canonical denominator/source/gap fiber，`H_{V,0},r,g_0,R_0,a_2` 等数据固定，因此 `(Pairmax-local-CRT)` 通过普通 CRT 聚合成一个 fixed residue

\[
\boxed{
A_{12}\equiv\rho_V\pmod{v_2}.}
\tag{Pairmax-neighborhood-CRT}
\]

有效 period 恰为

\[
\boxed{v_2.}
\tag{Full-v2-period}
\]

quantitative one-channel theorem 已给

\[
\boxed{
\frac{\log_{10}v_2}{S}
\ge1-C_{\rm one}\delta-o(1),}
\]

其中

\[
\boxed{C_{\rm one}=2.335049992773302\ldots.}
\tag{5.1}
\]

---

## 6. 与 generic square-source period 联立

上一文件构造 `q_Q`，满足

\[
\boxed{
A_{12}\equiv\rho_Q\pmod{q_Q^2},}
\tag{6.1}
\]

\[
\boxed{
\frac{\log_{10}q_Q}{S}
\ge z_*-\delta-o(1),}
\qquad
z_*=0.308883577618031\ldots,
\tag{6.2}
\]

并且关键地

\[
\boxed{(q_Q,V)=1.}
\]

所以

\[
\boxed{(q_Q,v_2)=1.}
\tag{6.3}
\]

因此联合 period 是 exact product

\[
\boxed{M_{QV}:=q_Q^2v_2.}
\tag{6.4}
\]

由 `(5.1),(6.2)`：

\[
\boxed{
\frac{\log_{10}M_{QV}}S
\ge
1+2z_*-(2+C_{\rm one})\delta-o(1).}
\tag{6.5}
\]

即

\[
\boxed{
\frac{\log_{10}M_{QV}}S
\ge
1.617767155236062\ldots
-4.335049992773302\ldots\delta-o(1).}
\tag{6.6}
\]

---

## 7. 显式 fixed-fiber uniqueness neighborhood

在 `d_3`-dominant DD 中

\[
s_1+s_2\le2.
\]

而 `A_12=a_1 10^{n_2}+a_2` 恰有 `n_1+n_2` 位，因此

\[
0<A_{12}<10^{n_1+n_2}
\le10^{S+2}.
\tag{7.1}
\]

若

\[
1+2z_*-(2+C_{\rm one})\delta>1,
\]

即

\[
\boxed{
\delta<\delta_{\rm CRT}:=
\frac{2z_*}{2+C_{\rm one}}
=0.142505197463905\ldots,}
\tag{7.2}
\]

则存在 `epsilon(delta)>0`，使 sufficiently large `S` 时

\[
M_{QV}>10^{(1+\epsilon)S}>10^{S+2}.
\]

所以固定 canonical denominator/source/gap fiber内，若两个不同 `A_12` 同时满足 `(6.1)` 与 `(Pairmax-neighborhood-CRT)`，其差必须被 `M_QV` 整除，却绝对值小于 `M_QV`，矛盾。

因此：

\[
\boxed{
\delta<0.142505197463905\ldots
\Longrightarrow
\#\{A_{12}\text{ in a fixed canonical fiber}\}\le1.}
\tag{Neighborhood-A12-unique}
\]

这是旧 equality `Universal-A12-unique` 的显式 neighborhood 版本。

---

## 8. 这还没有给出 explicit slope gap

`Neighborhood-A12-unique` 是真正的新 uniqueness theorem，但仍不是 emptiness。原因是 fixed fiber 中包含的 denominator/source/gap data 本身仍可能随 `S` 移动；尤其：

- `q_Q` 的具体 prime-power分解依赖 sphere-gap allocation；
- `R_0/g_0` 虽有 generic exact definition，但在 `delta>0` 时不再是 `10^{o(S)}` slow data；
- Farey/Schmidt slack仍允许 `10^{sigma_S S+o(S)}` 级 projective fibers。

因此不能从“每 fiber 至多一个 `A_12`”直接推出 neighborhood 为空。

不过 strict-gap 目标现在进一步缩成：

\[
\boxed{
\text{控制 fixed fibers 的总数，或定位唯一 CRT lift 的 Archimedean digit shell。}}
\]

而 source-square 与 pair-max 两个 positive-height periods 已经全部完成，不再需要新的 leading-order CRT modulus。

---

## 9. 状态摘要

- **已严格完成：** generic carry `(Carry-generic)`，不依赖 equality。
- **已严格完成：** pair-max baseline valuation table `(1.2)--(3.4)`。
- **已严格完成：** `Pairmax-theta-neighborhood`，低 denominator baseline只贡献齐次 `6r`。
- **已严格完成：** local `Pairmax-local-CRT`，每个 `p^h||v_2` 保留完整 period `p^h`。
- **已严格完成：** aggregate `Full-v2-period`。
- **已严格完成：** `Neighborhood-A12-unique`，显式范围 `delta<0.142505197463905...`。
- **no-double-count：** `v_2` period来自已有 sphere-paid square-depth，只用于 residue/uniqueness，不作为新增 local height surplus。
- **仍待证：** fiber count / unique-lift location、explicit global slope gap、DD emptiness、effective absolute height bound。

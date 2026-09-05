# DD corrected terminal neighborhood 的 pair-max fixed CRT

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-neighborhood-square-source-crt-2026-08-22.md`](dd-corrected-neighborhood-square-source-crt-2026-08-22.md)、[`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)、[`good-genuine-ledger.md`](good-genuine-ledger.md#source-pairmax-fixed-a12-crt) 的 split-independent `Sphere-pay-global` identity、[`core.md`](core.md) §§37--38 的 primitive overlap normalization。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` terminal neighborhood；fixed primitive/source fiber）。**
>
> 旧 `Pairmax-GCRT0` 只在 equality frontier 中把低 denominator baseline 视为 `o(S)` 后写成模 `C_L` 的 fixed `A_12` residue。本文不删除该 baseline。对每个 quantitative one-channel prime
> \[
> p^h\Vert v_2
> \]
> 保留其低 prefix exponent `r`，证明所有 square/carry quantities具有统一 `6r` baseline；精确约掉后仍留下完整 `p^{2h}` square-depth，因此得到模 `p^h` 的 fixed linear `A_12` residue。聚合后 effective rational period正好是整个 `v_2`。

---

## 1. general carry 本来就在整个 canonical funnel 中成立

使用 `core.md` §37--38 的 overlap notation：

\[
Q=\eta Q_1,
\qquad
\tau=\eta v,
\qquad
u=LQ_1,
\qquad
\nu+v=\varepsilon w,
\]

以及

\[
\boxed{
v\omega A_{12}10^d-a_3Q_1=wa_0.}
\tag{1.1}
\]

canonical `t_2=1` phase识别

\[
\boxed{v=V,}
\qquad
\boxed{LQ_1=2\cdot5^TU,}
\qquad
\boxed{\varepsilon w=\Sigma:=2^HZ+5^TU.}
\tag{1.2}
\]

又

\[
10^m=L\omega,
\qquad
B:=\frac{10^m}{2\cdot5^T}
=\frac{L\omega}{2\cdot5^T}.
\tag{1.3}
\]

因此从 `(1.1)`：

\[
\begin{aligned}
BV10^dA_{12}-Ua_3
&=\frac{L}{2\cdot5^T}
\left(V\omega A_{12}10^d-a_3Q_1\right)\\
&=\frac{Lwa_0}{2\cdot5^T}\\
&=\Sigma\frac{La_0}{2\cdot5^T\varepsilon}.
\end{aligned}
\tag{1.4}
\]

把正有理数写成最低项

\[
\boxed{
\frac{La_0}{2\cdot5^T\varepsilon}
=\frac{R_0}{g_0},
\qquad
(R_0,g_0)=1.}
\tag{1.5}
\]

则 exact carry 为

\[
\boxed{
g_0Ua_3
=g_0B10^dVA_{12}-\Sigma R_0.}
\tag{Carry-general}
\]

所以 equality frontier中的 carry 不是新结构；equality 只进一步证明了 `g_0,R_0` 的 slow-height 性质。

还有一个有用解释。§38 给

\[
H_{\rm sph}-y_3=cLa_0,
\]

故

\[
\frac{R_0}{g_0}
=\frac{H_{\rm sph}-y_3}
{2\cdot5^T\varepsilon c}.
\tag{1.6}
\]

即 `R_0/g_0` 是 primitive sphere-gap quotient。

---

## 2. 固定一个 quantitative pair-max prime

固定

\[
\boxed{p^h\Vert v_2,\qquad p\nmid10.}
\tag{2.1}
\]

quantitative one-channel 使用 `(b_2,b_3)` pair-max orientation。写

\[
\boxed{
v_p(b_1)=r,}
\qquad
\boxed{
v_p(b_2)=v_p(b_3)=r+h.}
\tag{2.2}
\]

由

\[
Q=b_1 10^{m_2}+b_2
\]

两项 valuation 不等：

\[
\boxed{v_p(Q)=r.}
\tag{2.3}
\]

与上一文件相同，canonical reduced-tail quotient给

\[
\boxed{v_p(q)=r,\qquad p\nmid U.}
\tag{2.4}
\]

又

\[
G=\gamma V,
\qquad
v_p(G)=2r+h,
\qquad
v_p(V)=h,
\]

所以

\[
\boxed{v_p(\gamma)=2r.}
\tag{2.5}
\]

因 `kappa=gamma u` 且 `u=2*5^T U` 为 p-unit：

\[
\boxed{v_p(\kappa)=2r.}
\tag{2.6}
\]

并且

\[
\kappa+G=\gamma(u+V),
\qquad
\kappa+2G=\gamma(u+2V),
\]

括号均为 p-units，故

\[
\boxed{
v_p(\kappa+G)=v_p(\kappa+2G)=2r.}
\tag{2.7}
\]

---

## 3. raw sphere carrier 的 exact baseline + excess

令

\[
y:=a_2b_1,
\qquad
\mathcal S_{\rm raw}
:=y^2b_3^2+G^2a_3^2
=b_1^2\bigl[(a_2b_3)^2+(a_3b_2)^2\bigr].
\tag{3.1}
\]

reducedness给 `a_2,a_3` 为 p-units，因此

\[
v_p(y)=r.
\]

另一方面

\[
y_2=a_2\frac{q_{\rm lcm}}{b_2},
\qquad
y_3=a_3\frac{q_{\rm lcm}}{b_3}
\]

都是 p-units，而 pair-max sphere carrier给

\[
\boxed{p^{2h}\mid y_2^2+y_3^2.}
\tag{3.2}
\]

由于

\[
(a_2b_3)^2+(a_3b_2)^2
=\left(\frac{b_2b_3}{q_{\rm lcm}}\right)^2
(y_2^2+y_3^2),
\]

且

\[
v_p\left(\frac{b_2b_3}{q_{\rm lcm}}\right)=r+h,
\]

得到

\[
\boxed{v_p(\mathcal S_{\rm raw})\ge4r+4h.}
\tag{Sphere-raw-neighborhood}
\]

这里 `4r+2h` 是显式 denominator baseline，额外 `2h` 是 pair-max sphere square-depth。

---

## 4. `Sphere-pay-global` 给 `Theta` 的 `6r+2h` depth

定义

\[
T_3:=10^m,
\qquad
A_c:=Qy^2,
\]

\[
\mathscr T:=\frac{\kappa^2(\kappa+2G)}{T_3},
\]

\[
\boxed{
\Theta
:=(\kappa+G)A_c\beta+\mathscr T a_3^2.}
\tag{4.1}
\]

`pairmax-fixed-a12-crt.md` 已机械验证 split-independent exact identity

\[
\boxed{
T_3G^2\Theta
=\kappa\left[
\kappa(\kappa+2G)\mathcal S_{\rm raw}
+G^2y^2b_3^2
\right].}
\tag{Sphere-pay-global}
\]

由 `(2.3)--(2.7)`：

\[
v_p(A_c)=v_p(Q)+2v_p(y)=3r,
\]

而 denominator concat

\[
\beta=T_3Q+b_3
\]

的两项 valuations为 `r,r+h`，故

\[
\boxed{v_p(\beta)=r.}
\tag{4.2}
\]

于是 `Theta` 的两个显式 summands各自至少含 `p^{6r}`：

\[
v_p((\kappa+G)A_c\beta)=2r+3r+r=6r,
\]

\[
\boxed{v_p(\mathscr T)=6r.}
\tag{4.3}
\]

对 `Sphere-pay-global` 右端：

\[
v_p\left(\kappa(\kappa+2G)\mathcal S_{\rm raw}\right)
\ge8r+4h,
\]

\[
v_p(G^2y^2b_3^2)=8r+4h.
\]

外层 `kappa` 再贡献 `2r`；左边 `G^2` 显式贡献 `4r+2h`。因此

\[
\boxed{v_p(\Theta)\ge6r+2h.}
\tag{Theta-neighborhood}
\]

这正是旧 `2h` square-depth 加上一个统一 `6r` baseline。

---

## 5. target prime 上 `g_0,R_0,Sigma` 都是 units

在 pair-max prime上，`c_3=q_lcm/b_3` 为 p-unit，所以

\[
\varepsilon=(c_3,u+v)
\]

是 p-unit；`u=LQ_1` 为 p-unit，因此 `w=(u+v)/epsilon` 也是 p-unit。

从

\[
v\omega A_{12}10^d-a_3Q_1=wa_0
\]

看，第一项被 p 整除，第二项为 p-unit，故

\[
\boxed{p\nmid a_0.}
\tag{5.1}
\]

`L,2*5^T,epsilon` 都是 p-units，所以最低项定义 `(1.5)` 给

\[
\boxed{p\nmid g_0R_0.}
\tag{5.2}
\]

再由

\[
V=2^HZ-5^TU\equiv0\pmod p
\]

且 `U` 为 p-unit，可知 `X=2^HZ` 与 `Y=5^TU` 都是 p-units且 `X≡Y mod p`。因此

\[
\boxed{\Sigma=X+Y\equiv2Y\not\equiv0\pmod p.}
\tag{5.3}
\]

---

## 6. carry-square 在约掉 `6r` 后恢复旧 `r=0` ledger

将 `(Carry-general)` 平方并代入 `g_0^2U^2 Theta`，exact 地得到

\[
\begin{aligned}
g_0^2U^2\Theta
={}&H_{p,\rm raw}
-2\mathscr T g_0B10^dV\Sigma R_0A_{12}\\
&+\mathscr T g_0^2B^210^{2d}V^2A_{12}^2,
\end{aligned}
\tag{6.1}
\]

其中 constant part

\[
\boxed{
H_{p,\rm raw}
:=g_0^2U^2(\kappa+G)A_c\beta
+\mathscr T\Sigma^2R_0^2}
\tag{6.2}
\]

不显式含 `A_12`。

由 §§4--5：

\[
v_p(g_0^2U^2\Theta)\ge6r+2h,
\]

linear term的 coefficient depth恰为

\[
6r+h,
\]

quadratic term depth恰为

\[
6r+2h.
\]

而 `(6.2)` 的两个 summands各自至少含 `p^{6r}`。定义整数

\[
\boxed{
H_{p,0}:=\frac{H_{p,\rm raw}}{p^{6r}}.}
\tag{6.3}
\]

将 `(6.1)` 除以 `p^{6r}`。模 `p^h` 时 linear 与 quadratic 项消失，而左边被 `p^{2h}` 整除，因此

\[
\boxed{p^h\mid H_{p,0}.}
\tag{6.4}
\]

定义

\[
\boxed{M_p:=H_{p,0}/p^h\in\mathbf Z.}
\tag{6.5}
\]

再把除 `p^{6r}` 后的 `(6.1)` 整体除以 `p^h` 并模 `p^h`，得到

\[
\boxed{
2\frac{\mathscr T}{p^{6r}}
 g_0B10^d\frac{V}{p^h}\Sigma R_0\,A_{12}
\equiv M_p
\pmod{p^h}.}
\tag{Pairmax-p-CRT}
\]

由 `(4.3),(5.2),(5.3)` 与 `v_p(V)=h`，左侧 coefficient 为 p-unit。因此 `(Pairmax-p-CRT)` 对 `A_12` 给出完整 effective period `p^h`。

> `M_p` 依赖固定 primitive/source fiber中的 `R_0` 与其它 data，但不在该 fiber 内随待求 `A_12` 改变。本文的结论首先是 fixed-fiber uniqueness；它不宣称 `R_0` 在整个 neighborhood 只有 boundedly many values。

---

## 7. 聚合为完整 quantitative one-channel period

对

\[
v_2=\prod p^h
\]

的不同 target primes，`(Pairmax-p-CRT)` 各自给唯一 residue class modulo `p^h`。Chinese remainder theorem因此聚合成

\[
\boxed{A_{12}\equiv\rho_V\pmod{v_2}}
\tag{Pairmax-neighborhood-CRT}
\]

对固定 primitive/source fiber成立。

因此 equality statement

\[
\text{effective pair-max period}=C_L/10^{o(S)}
\]

在 corrected terminal neighborhood 中升级为

\[
\boxed{\text{effective pair-max period}=v_2}
\tag{Full-v2-period}
\]

而且无需删除低 baseline `r` 的 support。

quantitative one-channel theorem已经给出

\[
\boxed{
\frac{\log_{10}v_2}{S}
\ge1-C_{\rm one}\delta-o(1),
\qquad
C_{\rm one}=2.335049992773302\ldots.}
\tag{7.1}
\]

---

## 8. 与 generic source-square period 联立

上一文件构造 `q_Q` 并证明

\[
\boxed{\log_{10}q_Q/S\ge z_*-\delta-o(1),}
\]

\[
\boxed{(q_Q,v_2)=1,}
\]

以及 fixed source congruence modulo `q_Q^2`。

所以在同一个 fixed primitive/source fiber中，`A_12` 同时满足两个互素 periods：

\[
q_Q^2,
\qquad
v_2.
\]

联合 modulus为 exact product

\[
\boxed{M_{QV}:=q_Q^2v_2.}
\tag{8.1}
\]

且

\[
\boxed{
\frac{\log_{10}M_{QV}}S
\ge
1+2z_*-(2+C_{\rm one})\delta-o(1).}
\tag{8.2}
\]

即

\[
\boxed{
\frac{\log_{10}M_{QV}}S
\ge
1.617767155236062\ldots
-4.335049992773302\ldots\delta-o(1).}
\tag{8.3}
\]

---

## 9. 一个显式正宽度的 fixed-fiber uniqueness neighborhood

在 `d_3`-dominant DD 中

\[
s_1+s_2\le2.
\]

而

\[
A_{12}=a_1 10^{n_2}+a_2
\]

有至多 `n_1+n_2=S+s_1+s_2<=S+2` 位。因此任意两个合法 prefixes满足

\[
|A_{12}^{(1)}-A_{12}^{(2)}|<10^{S+2}.
\tag{9.1}
\]

若

\[
1+2z_*-(2+C_{\rm one})\delta>1,
\]

则 sufficiently large `S` 上 `M_QV>10^{S+2}`。阈值为

\[
\boxed{
\delta<\delta_{\rm CRT}
:=\frac{2z_*}{2+C_{\rm one}}
=0.142505197463905\ldots.}
\tag{9.2}
\]

于是得到：

\[
\boxed{
\delta<0.142505197463905\ldots
\Longrightarrow
\#\{A_{12}\text{ in a fixed primitive/source fiber}\}\le1
}
\tag{Neighborhood-fixed-fiber-unique}
\]

对 fixed `(n_2,a_2)` 同样把结论下推为 leading block `a_1` 至多一个。

这是 equality-only `Universal-A12-unique` 第一次被扩展到一个显式正宽度的 corrected terminal neighborhood。

---

## 10. 状态边界与下一目标

本文已经完成两个 period 的 neighborhood 移植，但 `Neighborhood-fixed-fiber-unique` 仍是 uniqueness，不是 emptiness，也还不是 explicit slope gap。原因是 fixed fiber 中包含

\[
R_0/g_0
=\frac{La_0}{2\cdot5^T\varepsilon},
\]

以及 `a_3` / primitive sphere data；本文没有证明这些 fiber 的总数为 subexponential。

下一步因此不再是继续增强 CRT modulus，而是量化 **fiber entropy**。最自然的两个接口是：

1. `(1.6)` 把 `R_0/g_0` 直接识别为 sphere-gap quotient；`Gap-augmented-defect` 已证明其 rough source只有 `O(delta S)` 高度；
2. generic source CRT 与 carry可以联立消去 `A_12`，把剩余 freedom推到 `a_3,R_0` 的一个低维 residue system。

如果能证明 terminal neighborhood 中 fixed-fiber 参数只有

\[
10^{C\delta S+o(S)}
\]

种，而 pair-max/source orientation再给一个独立 period超过这份 entropy，就可以把当前 uniqueness推进成 explicit slope gap或至少 exponential sparsity。

---

## 11. 状态摘要

- **已严格完成：** generic carry `Carry-general`。
- **已严格完成：** pair-max raw sphere depth `4r+4h`。
- **已严格完成：** `Theta-neighborhood`, depth `6r+2h`。
- **已严格完成：** 约掉 low baseline 后的 local `Pairmax-p-CRT`，effective period完整 `p^h`。
- **已严格完成：** aggregate `Pairmax-neighborhood-CRT`, effective period `v_2`。
- **已严格完成：** 与 `q_Q^2` 联立后，`delta<0.142505197463905...` 的 fixed-fiber `A_12/a_1` uniqueness neighborhood。
- **当前开放核心：** fixed primitive/source fiber 的 entropy；unique CRT representative 的 digit-shell exclusion；explicit strict slope gap；DD emptiness与有效绝对高度界。

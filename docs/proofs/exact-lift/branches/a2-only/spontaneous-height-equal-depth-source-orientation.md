# A2 moving height equal-depth 的 actual-carrier / source orientation law

> **依赖：** `spontaneous-height-angle-additive-norm-bridge.md`、`primitive-reduction.md`、`spontaneous-height-parity-ledger.md`、`source-discriminant.md`。
>
> **严格状态：**前一文件证明 moving height 的 unsaturated equal-depth extra lift 强迫 normalized `B_W/H_O` ratio为 `-square`。本文把 `H_O` 和 `B_W` 分别还原到实际 angle/additive primitive carriers，在 `p^h||W_q`、common depth `e<h` 上计算精确的一阶 resultant coefficient。利用 original sphere、`alpha=omega W_q`、`beta=omega S`、height square与 denominator ratio，最终把 equal-depth condition化成
> \[
> \left(\frac{(\Theta_{dec}/p^e)/(\mathcal O_+/p^e)}p\right)
> =\left(\frac{-\rho}p\right),
> \qquad \rho=q5^\lambda/c_u.
> \]
> 因而剩余 relative orientation 已直接接到真实 source ratio；不再含 `H_O`、`B_W` 或 auxiliary carrier。本文尚未从 sign-companion / source orbit独立固定左边或 `rho` 的 character，所以不关闭 equal-depth shell。

---

## 1. height prime 与原拼接 content

固定 genuine non-`3` inert endpoint-external height prime

\[
p^h\Vert W_q,
\qquad h\ge1,
\qquad p\equiv3\pmod4.
\tag{1.1}

允许 `p` 同时进入 `omega`；写

\[
w:=v_p(\omega)\ge0.
\]

primitive reduction 已给

\[
\boxed{
\alpha:=TK+a_3=\omega W_q,}
\tag{1.2}

\[
\boxed{
\beta:=TQ+b_3=\omega S,
\qquad \gcd(W_q,S)=1.}
\tag{1.3}

所以

\[
v_p(\alpha)=w+h,
\qquad
v_p(\beta)=w.
\tag{1.4}

原 exact sphere为

\[
\boxed{
B^2b_3^2\alpha^2
=\beta^2
\left(N_0b_3^2+B^2a_3^2\right).}
\tag{1.5}

external separation给 `p∤Bb_3S`，因此 (1.4)--(1.5) 精确推出

\[
\boxed{
v_p(N_0b_3^2+B^2a_3^2)=2h.}
\tag{1.6}

---

## 2. `alpha=0` height quadratic 在 mod `p^h` 内无损

定义 angle resultant使用的 quadratic

\[
\boxed{
\mathscr H_0
:=N_0b_3^2+B^2T^2K^2.}
\tag{2.1}

由 `a_3=alpha-TK`：

\[
\mathscr H_0-
(N_0b_3^2+B^2a_3^2)
=B^2(2\alpha TK-\alpha^2).
\tag{2.2}

右边至少有 `p^{h+w}`，而 (1.6) 有 `p^{2h}`。所以无条件有

\[
\boxed{p^h\mid\mathscr H_0.}
\tag{2.3}

这里不需要假设 `p∤omega`；即使 `omega` 带同 prime content，`p^h` height depth仍保留。

---

## 3. angle resultant 的一阶 coefficient

actual raw angle carrier为

\[
\boxed{
\mathcal O_+
=T\mathcal U_\Omega+2A^2Qb_3.}
\tag{3.1}

记

\[
L:=\mathcal O_+.
\]

由

\[
2A^2Qb_3=L-T\mathcal U_\Omega
\]
直接展开：

\[
\begin{aligned}
(2A^2Q)^2\mathscr H_0
={}&N_0(L-T\mathcal U_\Omega)^2
+4A^4Q^2B^2T^2K^2\\
={}&N_0L^2-2N_0T\mathcal U_\Omega L
+T^2\mathcal H_O.
\end{aligned}
\]
因此 exact identity为

\[
\boxed{
T^2\mathcal H_O
=(2A^2Q)^2\mathscr H_0
-N_0L^2
+2N_0T\mathcal U_\Omega L.}
\tag{3.2}

设 actual angle depth

\[
e:=v_p(L)<h.
\tag{3.3}

由 (2.3)，第一项比 `p^e` 更深；`L^2` 有深度 `2e>e`。故除以 `p^e` 并模 `p`：

\[
\boxed{
\frac{\mathcal H_O/p^e}{\mathcal O_+/p^e}
\equiv
\frac{2N_0\mathcal U_\Omega}{T}
\pmod p.}
\tag{3.4}

这是 height norm resultant 在 simple unsaturated root上的精确 derivative coefficient。

---

## 4. additive carrier 的一阶 coefficient

actual additive raw carrier为

\[
\boxed{
\Theta_{\rm dec}
=T\mathcal J_H
-2B^2(2K-9)\alpha.}
\tag{4.1}

若 common additive depth同样为 `e<h`，则第二项因 `v_p(alpha)>=h` 更深，所以

\[
\boxed{
\frac{\Theta_{\rm dec}}{p^e}
\equiv
T\frac{\mathcal J_H}{p^e}
\pmod p.}
\tag{4.2}

已有 height square bridge

\[
c_u^2\mathcal J_H
\equiv B^2\mathscr B_W
\pmod{W_q}.
\]
因此在 `e<h`：

\[
\boxed{
\frac{\Theta_{\rm dec}/p^e}{\mathscr B_W/p^e}
\equiv
T\left(\frac B{c_u}\right)^2
\pmod p.}
\tag{4.3}

angle 与 additive raw carriers都除以相同 primitive `2`-power
`2^{2M+m+2}`，所以它们的 normalized ratio与 primitive ratio完全相同。

---

## 5. `2 N_0 U_Omega` 的 character 精确等于 source `rho`

height square exact identity为

\[
\boxed{
b_3^2N_0+B^2a_3^2
=\left(\frac{BH_0}{g}\right)^2,}
\tag{5.1}

且 `H_0=c_uW_q`。模 `p|W_q`：

\[
\boxed{
N_0
\equiv-\left(\frac{Ba_3}{b_3}\right)^2
\pmod p.}
\tag{5.2}

所以

\[
\left(\frac{N_0}{p}\right)=-1.
\tag{5.3}

另一方面 actual angle first layer `O_+=0` 给

\[
T\mathcal U_\Omega
\equiv-2A^2Qb_3
\pmod p.
\]
因此

\[
2\mathcal U_\Omega
\equiv-\frac{4A^2Qb_3}{T}
\pmod p.
\tag{5.4}

source denominator ratio为

\[
\boxed{b_3z=Tc_uQ,}
\tag{5.5}

其中

\[
z=q5^\lambda,
\qquad
\rho:=\frac z{c_u}.
\tag{5.6}

由 (5.5)：

\[
\frac{Qb_3}{T}
=\frac{b_3^2z}{T^2c_u}.
\]
除显式 squares 后：

\[
\boxed{
\left(\frac{2\mathcal U_\Omega}{p}\right)
=\left(\frac{-\rho}{p}\right).}
\tag{5.7}

结合 (5.3)，因为 `p=3 mod4`：

\[
\boxed{
\left(\frac{2N_0\mathcal U_\Omega}{p}\right)
=\left(\frac{\rho}{p}\right).}
\tag{5.8}

`T` 只会在 (3.4) 中出现；稍后与 additive coefficient 的 `T` 精确相消，因此无需单独确定 `(T/p)`。

---

## 6. 把 `B_W/H_O` ratio换成 actual carrier ratio

由 (3.4) 与 (4.3)：

\[
\frac{\mathscr B_W/p^e}{\mathcal H_O/p^e}
\equiv
\frac{(\Theta_{\rm dec}/p^e)/(\mathcal O_+/p^e)}
{2N_0\mathcal U_\Omega}
\left(\frac{c_u}{B}\right)^2
\pmod p.
\tag{6.1}

这里两个 `T` 已经抵消。

所以 Legendre character为

\[
\boxed{
\left(
\frac{(\mathscr B_W/p^e)/(\mathcal H_O/p^e)}p
\right)
=
\left(
\frac{(\Theta_{\rm dec}/p^e)/(\mathcal O_+/p^e)}p
\right)
\left(\frac{\rho}{p}\right).}
\tag{6.2}

---

## 7. equal-depth extra lift的 source-orientation law

`spontaneous-height-angle-additive-norm-bridge.md` 已证明：若

\[
v_p(\mathscr B_W)=v_p(\mathcal H_O)=e<h
\]
且 auxiliary carrier `R_HO` 继续 extra lift，则

\[
\left(
\frac{(\mathscr B_W/p^e)/(\mathcal H_O/p^e)}p
\right)=-1.
\tag{7.1}

与 (6.2) 合并：

\[
\boxed{
\left(
\frac{(\Theta_{\rm dec}/p^e)/(\mathcal O_+/p^e)}p
\right)
=-\left(\frac{\rho}{p}\right).}
\tag{7.2}

因为 `(-1/p)=-1`，也可写成更对称的形式

\[
\boxed{
\left(
\frac{(\Theta_{\rm dec}/p^e)/(\mathcal O_+/p^e)}p
\right)
=
\left(\frac{-\rho}{p}\right).}
\tag{7.3}

这就是 moving-height equal-depth extra cancellation 的 actual-carrier / source orientation law。

---

## 8. updated frontier

现在 unsaturated moving height shell已经连续经历三次压缩：

1. singular bad-reduction tree 全部删除；
2. unequal-depth由 universal norm bridge精确同步；
3. equal-depth extra lift若发生，实际 angle/additive normalized ratio必须与 source ratio满足 (7.3)。

所以剩余问题不再需要 auxiliary `H_O/B_W` variables。规范目标是：

\[
\boxed{
\text{独立计算 actual sign pair / cross-sign sphere 对 }
(\Theta_{dec}/p^e)/(\mathcal O_+/p^e)
\text{ 的 character，}}
\]

或独立固定 `rho` 的 sign/quartic orientation。

若 sign-companion geometry给出的左侧 character与 `(7.3)` 相反，则整个 unsaturated equal-depth moving-height shell立即关闭。
# A2 resonance tail 的 coprime imbalance equation

> **依赖：** `spontaneous-height-equal-depth-tail-normalization.md`、`spontaneous-height-equal-depth-square-core.md`、`primitive-reduction.md`。
>
> **严格状态：**前一文件定义 canonical tail quotient `Lambda_tail=Lambda_dec/(omega Gamma)`，并证明 equal-depth target prime 上 `v_p(Lambda_tail)=rho_p`。本文把 `omega=Gamma omega^circ`、`W_q=Gamma W^circ` 代入，得到 exact reduced equation `Lambda_tail=2E_MNS omega^circ+TQ^2W^circ`，其中 `gcd(omega^circ,W^circ)=1`。利用 `gcd(W_q,2E_MNS)=1` 进一步证明全局 coprimality `gcd(Lambda_tail,W^circ)=1`。因此 reduced height numerator 的 residual prime support 与 resonance tail support 完全分离；equal-depth tail 只能通过两个 p-adic units 的线性 cancellation 产生。本文仍不能排除这种 cancellation，因此不关闭 A2。

---

## 1. square-core imbalance factors

沿用

\[
\Gamma:=\gcd(\omega,W_q),
\]
并定义

\[
\boxed{
\omega^\circ:=\frac\omega\Gamma,
\qquad
W^\circ:=\frac{W_q}{\Gamma}.}
\tag{1.1}
\]

于是

\[
\boxed{
\gcd(\omega^\circ,W^\circ)=1,}
\tag{1.2}
\]

以及

\[
\alpha
=\Gamma^2\omega^\circ W^\circ.
\tag{1.3}
\]

逐 prime 有

\[
v_p(\omega^\circ W^\circ)
=|v_p(\omega)-v_p(W_q)|.
\tag{1.4}
\]

因此 equal-depth target prime 不整除 `omega^circ W^circ`。

---

## 2. full-tail reader 除去 baseline gcd 后变成两项线性式

已有

\[
\Lambda_{\rm dec}
=2\beta\Delta_\omega+TQ^2\alpha,
\tag{2.1}
\]

以及

\[
\beta=\omega S,
\qquad
\Delta_\omega=E_MN\omega,
\qquad
\alpha=\omega W_q.
\tag{2.2}
\]

所以

\[
\begin{aligned}
\Lambda_{\rm dec}
&=2(\omega S)(E_MN\omega)
+TQ^2(\omega W_q)\\
&=\omega\left(
2E_MNS\omega+TQ^2W_q
\right).
\end{aligned}
\tag{2.3}
\]

前一文件证明

\[
\gcd(\alpha,\Lambda_{\rm dec})
=\omega\Gamma,
\]
所以

\[
\Lambda_{\rm tail}
:=\frac{\Lambda_{\rm dec}}{\omega\Gamma}.
\]

把

\[
\omega=\Gamma\omega^\circ,
\qquad
W_q=\Gamma W^\circ
\]
代入 (2.3)，得到 exact reduced equation：

\[
\boxed{
\Lambda_{\rm tail}
=2E_MNS\omega^\circ
+TQ^2W^\circ.}
\tag{2.4}
\]

它的两项都是正整数，因此

\[
\Lambda_{\rm tail}>0.
\]

---

## 3. equal-depth tail 是两个 global units 的纯 cancellation

固定 equal-depth target prime `p`。由定义：

\[
p\nmid\omega^\circ W^\circ.
\tag{3.1}
\]

并且 genuine height prime 与 `2E_MNSTQ` 分离，所以 (2.4) 的两个 summand 都是 p-adic units：

\[
v_p(2E_MNS\omega^\circ)=0,
\qquad
v_p(TQ^2W^\circ)=0.
\tag{3.2}
\]

另一方面前一文件给

\[
\boxed{v_p(\Lambda_{\rm tail})=\rho_p.}
\tag{3.3}
\]

所以

\[
\boxed{
\rho_p
=v_p\left(
2E_MNS\omega^\circ+TQ^2W^\circ
\right).}
\tag{3.4}
\]

这已经完全删除 baseline `h`：resonance tail 就是两个互素 global imbalance cofactors 的 unit cancellation depth。

---

## 4. tail quotient 与 residual height numerator 全局互素

`primitive-reduction.md` 与前一 normalization 已证明

\[
\boxed{
\gcd(W_q,2E_MNS)=1.}
\tag{4.1}
\]

因为 `W^circ|W_q`：

\[
\gcd(W^\circ,2E_MNS)=1.
\tag{4.2}
\]

现在对 (2.4) 模 `W^circ`：

\[
\Lambda_{\rm tail}
\equiv2E_MNS\omega^\circ
\pmod{W^\circ}.
\]

由 (1.2)、(4.2)，右侧与 `W^circ` 互素。因此

\[
\boxed{
\gcd(\Lambda_{\rm tail},W^\circ)=1.}
\tag{4.3}
\]

这是一个 global support separation，不只是对 equal-depth target pool 成立。

---

## 5. `W^circ` 也有纯 decimal gcd 读取器

前一 normalization 给

\[
\gcd(\alpha,\Lambda_{\rm dec})
=\omega\Gamma.
\]

而

\[
\alpha=\omega W_q.
\]

因此

\[
\boxed{
W^\circ
=\frac{W_q}{\Gamma}
=\frac{\alpha}{\gcd(\alpha,\Lambda_{\rm dec})}.}
\tag{5.1}
\]

所以 (4.3) 可完全改写为真实 decimal integers：

\[
\boxed{
\gcd\!\left(
\frac{\Lambda_{\rm dec}}{\gcd(\alpha,\Lambda_{\rm dec})},
\frac{\alpha}{\gcd(\alpha,\Lambda_{\rm dec})}
\right)=1.}
\tag{5.2}
\]

当然 (5.2) 也可视为 gcd 约去后的 tautological coprimality；真正的结构信息是 (2.4)：这两个 coprime quotients 恰好对应 resonance tail 与 reduced-height imbalance，而不是任意 gcd quotient。

---

## 6. `omega^circ` 的 pure-gcd recovery

已有

\[
\omega=\gcd(\alpha,\beta),
\qquad
\Gamma=
\frac{\gcd(\alpha,\Lambda_{\rm dec})}
{\gcd(\alpha,\beta)}.
\]

所以

\[
\boxed{
\omega^\circ
=\frac\omega\Gamma
=
\frac{\gcd(\alpha,\beta)^2}
{\gcd(\alpha,\Lambda_{\rm dec})}.}
\tag{6.1}
\]

于是 (2.4) 的两个 imbalance variables `omega^circ,W^circ` 都可以完全通过真实 decimal gcd data 恢复。

这说明 equal-depth tail 的剩余 unit equation不再依赖隐藏 source quotient：

\[
\boxed{
\Lambda_{\rm tail}
=2E_MNS\omega^\circ+TQ^2W^\circ,
\quad
\gcd(\omega^\circ,W^\circ)=1,}
\tag{6.2}
\]

其中所有量都有 canonical original-integer meaning。

---

## 7. 与 unequal-depth sector 的全局分离

由 (1.4)，若某 prime 满足

\[
v_p(\omega)\ne v_p(W_q),
\]
它会以深度

\[
|v_p(\omega)-v_p(W_q)|
\]
留在 `omega^circ W^circ`。

而 equal-depth target prime 满足

\[
p\nmid\omega^\circ W^\circ,
\]
其全部额外信息则进入 `Lambda_tail` 的 `rho_p`。

所以现在有真正的 canonical allocation：

\[
\boxed{
\begin{array}{c|c}
\text{sector}&\text{global carrier}\\ \hline
v_p(\omega)\ne v_p(W_q)&\omega^\circ W^\circ\\
v_p(\omega)=v_p(W_q)&\Gamma^2\\
\text{equal-depth extra resonance}&\Lambda_{\rm tail}
\end{array}}
\tag{7.1}
\]

并且 `Lambda_tail` 与 `W^circ` 已由 (4.3) 完全互素。

---

## 8. 当前 frontier

height/content overlap 已从最初的 moving source roots 压成三个 canonical integers：

\[
\boxed{
\Gamma,
\qquad
\omega^\circ W^\circ,
\qquad
\Lambda_{\rm tail}.}
\tag{8.1}
\]

其中：

- `Gamma^2` 承担 equal-depth baseline square core；
- `omega^circ W^circ` 承担所有 content/height imbalance；
- `Lambda_tail` 精确承担全部 extra resonance depth；
- `gcd(Lambda_tail,W^circ)=1` 已把 residual height support 与 tail support 全局分开。

下一步真正有机会关闭 equal-depth orbit 的方向是继续研究

\[
\gcd(\Lambda_{\rm tail},\Gamma),
\qquad
\gcd(\Lambda_{\rm tail},\omega^\circ),
\]

或把 reduced linear equation (2.4) 与 `C_alpha` 的小正 residue 联立。
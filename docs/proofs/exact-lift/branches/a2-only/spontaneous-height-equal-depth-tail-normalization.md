# A2 equal-depth resonance tail 的 canonical gcd normalization

> **依赖：** `spontaneous-height-equal-depth-tail-reader.md`、`spontaneous-height-equal-depth-square-core.md`、`primitive-reduction.md`。
>
> **严格状态：**`spontaneous-height-equal-depth-tail-reader.md` 已构造纯 decimal integer `Lambda_dec` 并证明 equal-depth target prime 上 `v_p(Lambda_dec)=2h+rho_p`。本文进一步证明 exact global gcd `gcd(alpha,Lambda_dec)=omega Gamma`，其中 `omega=gcd(alpha,beta)`、`Gamma=gcd(omega,W_q)`。因此 `Gamma` 可仅由真实 concatenated integers 恢复为 `gcd(alpha,Lambda_dec)/gcd(alpha,beta)`，无需 sphere height `H_0`；而 canonical quotient `Lambda_tail=Lambda_dec/gcd(alpha,Lambda_dec)` 在每个 equal-depth target prime 上的赋值恰为 `rho_p`。这把 baseline square depth 与 resonance tail 完全分层。本文不证明 tail quotient 没有 target prime，因此不关闭 A2。

---

## 1. 已有 primitive data

沿用

\[
\boxed{
\alpha=\omega W_q,
\qquad
\beta=\omega S,
\qquad
\gcd(W_q,S)=1.}
\tag{1.1}
\]

`primitive-reduction.md` 还证明

\[
\boxed{
W_q\text{ 为奇数},
\quad
5\nmid W_q,
\quad
\gcd(W_q,gc_Q)=1.}
\tag{1.2}
\]

令

\[
E_M=2^{M+1}c_Q,
\qquad
N=10^M,
\]
则 determinant 为

\[
\boxed{
\Delta_\omega=E_MN\omega.}
\tag{1.3}
\]

而 full-tail reader 是

\[
\boxed{
\Lambda_{\rm dec}
=2\beta\Delta_\omega+TQ^2\alpha.}
\tag{1.4}
\]

---

## 2. `W_q` 与 `2E_MNS` 完全互素

由

\[
E_M=2^{M+1}c_Q,
\qquad
N=2^M5^M,
\]
以及

\[
S=2^{M+m+1}gc_Q5^d,
\]
`2E_MNS` 的所有 prime support 都来自

\[
2,5,g,c_Q.
\]

结合 (1.2)：

\[
\boxed{
\gcd(W_q,2E_MNS)=1.}
\tag{2.1}
\]

这条全局 coprimality 是下面 exact gcd 的全部输入。

---

## 3. `gcd(alpha,Lambda_dec)` 精确等于 `omega Gamma`

由 (1.4) 模 `alpha`：

\[
\Lambda_{\rm dec}
\equiv2\beta\Delta_\omega
\pmod\alpha.
\]
因此

\[
\begin{aligned}
\gcd(\alpha,\Lambda_{\rm dec})
&=\gcd(\alpha,2\beta\Delta_\omega)\\
&=\gcd(\omega W_q,
2E_MNS\omega^2).
\end{aligned}
\tag{3.1}
\]

约出一份 `omega`：

\[
\gcd(\alpha,\Lambda_{\rm dec})
=\omega\,
\gcd(W_q,2E_MNS\omega).
\tag{3.2}
\]

由 (2.1)：

\[
\gcd(W_q,2E_MNS\omega)
=\gcd(W_q,\omega).
\]

定义

\[
\boxed{
\Gamma:=\gcd(\omega,W_q).}
\tag{3.3}
\]

于是得到 exact global identity

\[
\boxed{
\gcd(\alpha,\Lambda_{\rm dec})
=\omega\Gamma.}
\tag{3.4}
\]

这不是逐 target-prime 截断，而是所有 prime 同时成立的整数 gcd 等式。

---

## 4. square core 现在只靠 concatenated decimal integers 就能恢复

已有

\[
\boxed{\omega=\gcd(\alpha,\beta).}
\tag{4.1}
\]

把它代入 (3.4)：

\[
\boxed{
\Gamma
=
\frac{\gcd(\alpha,\Lambda_{\rm dec})}
{\gcd(\alpha,\beta)}.}
\tag{4.2}
\]

因此此前 square-core 文件的

\[
\Gamma=\gcd(\alpha,\beta,H_0)
\]
有了一个新的、完全不使用 sphere height 的读取器。

也就是说：

\[
\boxed{
\text{common square core }
\Gamma
\text{ 可由 }(\alpha,\beta,\Lambda_{\rm dec})
\text{ 三个真实 decimal integers 独立恢复}.}
\tag{4.3}
\]

这给后续纯 concatenation CRT 一个更干净的入口。

---

## 5. canonical tail quotient 精确删除 baseline depth

定义

\[
\boxed{
\Lambda_{\rm tail}
:=
\frac{\Lambda_{\rm dec}}
{\gcd(\alpha,\Lambda_{\rm dec})}
=
\frac{\Lambda_{\rm dec}}{\omega\Gamma}.}
\tag{5.1}
\]

固定 equal-depth target prime：

\[
v_p(\omega)=v_p(W_q)=h.
\]
因此

\[
\boxed{v_p(\Gamma)=h.}
\tag{5.2}
\]

full-tail reader 给

\[
\boxed{v_p(\Lambda_{\rm dec})=2h+\rho_p.}
\tag{5.3}
\]

所以从 (5.1)：

\[
\boxed{
v_p(\Lambda_{\rm tail})
=(2h+\rho_p)-h-h
=\rho_p.}
\tag{5.4}
\]

这是最干净的 tail normalization：

\[
\boxed{
\text{baseline }2h
\text{ 全部进入 }\gcd(\alpha,\Lambda_{\rm dec}),
\quad
\text{剩余赋值恰为 }\rho_p.}
\tag{5.5}
\]

因此 deep resonance `rho_p>=1` 等价于该 target prime 真正进入 `Lambda_tail`。

---

## 6. full tail product 直接整除 canonical quotient

令 `E_eq` 为 equal-depth oversaturation target pool，并定义

\[
\boxed{
R_\rho:=\prod_{p\in E_{\rm eq}}p^{\rho_p}.}
\tag{6.1}
\]

由 (5.4) 聚合：

\[
\boxed{
R_\rho\mid\Lambda_{\rm tail}.}
\tag{6.2}
\]

并且 target support 上是 exact：每个 `p in E_eq` 在 `Lambda_tail` 中恰出现 `rho_p` 次。

由 tail-reader 的 fixed window

\[
\Lambda_{\rm dec}<45T^2N^3
\]
有

\[
\boxed{
R_\rho
\le\Lambda_{\rm tail}
<
\frac{45T^2N^3}{\omega\Gamma}.}
\tag{6.3}
\]

相比原来的

\[
G_{\rm eq}^2R_\rho<45T^2N^3,
\]
(6.3) 的优点是 denominator `omega Gamma` 是一个 exact global gcd，而不是手工挑出的 target-prime product。

---

## 7. square/imbalance/tail 三层 canonical factorization

此前 square-core 文件给

\[
\alpha
=\Gamma^2\omega^\circ W^\circ,
\qquad
\gcd(\omega^\circ,W^\circ)=1.
\tag{7.1}
\]

本文则给

\[
\Lambda_{\rm dec}
=\omega\Gamma\Lambda_{\rm tail}.
\tag{7.2}
\]

所以 `alpha/Lambda_dec` 两个真实整数现在具有平行的 canonical decomposition：

\[
\boxed{
\begin{array}{c|c}
\alpha&\Gamma^2\cdot(\omega^\circ W^\circ)\\
\Lambda_{\rm dec}&\omega\Gamma\cdot\Lambda_{\rm tail}
\end{array}}
\tag{7.3}
\]

逐 equal-depth target prime：

- `Gamma^2` 读取 baseline `2h`；
- `omega^circ W^circ` 完全删除该 prime；
- `omega Gamma` 读取 `Lambda_dec` 中 baseline `2h`；
- `Lambda_tail` 精确读取剩余 `rho_p`。

因此前几轮的逐 prime depth ledger 已被提升为真正的 global gcd factorization。

---

## 8. 当前 frontier

现在 equal-depth resonance 的两个核心量都已 canonical 化：

\[
\boxed{
\Gamma
=
\frac{\gcd(\alpha,\Lambda_{\rm dec})}
{\gcd(\alpha,\beta)},
\qquad
\Lambda_{\rm tail}
=
\frac{\Lambda_{\rm dec}}
{\gcd(\alpha,\Lambda_{\rm dec})}.}
\tag{8.1}
\]

所以后续不再需要 source units `omega_0,W_0` 来描述剩余困难。

真正未关闭的对象已经压成：

\[
\boxed{
\text{一个短 square core }\Gamma^2\mid\alpha
\quad+\quad
\text{一个 pure decimal tail quotient }\Lambda_{\rm tail}.}
\tag{8.2}
\]

下一步最有价值的是研究 `Lambda_tail` 与 square-free imbalance cofactor `omega^circ W^circ`、顶部 defect `C_alpha` 或 prefix carriers 的 gcd。若能证明 target inert support 无法同时进入这些互补 natural quotients，就有机会真正关闭 equal-depth orbit。
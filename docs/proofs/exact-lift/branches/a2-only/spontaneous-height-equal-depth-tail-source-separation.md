# A2 resonance tail 与 imbalance support 的 source separation

> **依赖：** `spontaneous-height-equal-depth-tail-imbalance.md`、`source-discriminant.md`、`primitive-reduction.md`。
>
> **严格状态：**前一文件得到 `Lambda_tail=2E_MNS omega^circ+TQ^2W^circ` 与 `gcd(omega^circ,W^circ)=1`，并证明 `gcd(Lambda_tail,W^circ)=1`。本文进一步利用 source triangle `z=q5^lambda=g omega-c_u` 证明 `gcd(omega,q5)=1`，再结合 `alpha` 为奇数得到 `gcd(omega,2Tq)=1`。于是 `Lambda_tail` 与 `omega^circ` 的 overlap 精确等于 `gcd(c_Q^2,omega^circ)`，从而 `gcd(Lambda_tail,omega^circ W^circ)|c_Q^2`。因此除 `c_Q` support 外，resonance tail 与全部 content/height imbalance support 全局互素；当前 genuine height target primes 又与 `c_Q` 分离，所以 target tail 和 imbalance sector 已完全 prime-source 分开。本文不排除 tail primes 留在 square core `Gamma` 中，因此不关闭 A2。

---

## 1. `omega` 与 q-side source 完全互素

source triangle 为

\[
\boxed{
z=q5^\lambda=g\omega-c_u.}
\tag{1.1}
\]

并且已有

\[
\boxed{\gcd(\omega,c_u)=1.}
\tag{1.2}
\]

若某 prime `r` 同时整除 `omega` 与 `z`，则由 (1.1)

\[
c_u=g\omega-z
\]
也被 `r` 整除，与 (1.2) 矛盾。因此

\[
\boxed{\gcd(\omega,z)=1.}
\tag{1.3}
\]

因为

\[
z=q5^\lambda,
\qquad \lambda>0,
\]
所以

\[
\boxed{\gcd(\omega,q5)=1.}
\tag{1.4}
\]

---

## 2. `omega` 也是奇数

当前 denominator `b_3` 含非平凡 `2`-power，而

\[
\gcd(a_3,b_3)=1.
\]
所以 `a_3` 为奇数。

另一方面

\[
\alpha=TK+a_3,
\]
其中 `TK` 为偶数，因此

\[
\boxed{\alpha\text{ 为奇数}.}
\tag{2.1}
\]

又 `omega|alpha`，故

\[
\boxed{2\nmid\omega.}
\tag{2.2}
\]

结合 (1.4) 与 `T=2^m5^m`：

\[
\boxed{\gcd(\omega,Tq)=1.}
\tag{2.3}
\]

同样对 `omega^circ|omega`：

\[
\boxed{\gcd(\omega^\circ,Tq)=1.}
\tag{2.4}
\]

---

## 3. `TQ^2` 与 `omega^circ` 的 overlap 只来自 `c_Q`

由

\[
Q=2^{M+1}c_Qq,
\]
有

\[
TQ^2
=2^{m+2M+2}5^m c_Q^2q^2.
\]

使用 (2.4)：

\[
\boxed{
\gcd(TQ^2,\omega^\circ)
=\gcd(c_Q^2,\omega^\circ).}
\tag{3.1}
\]

因此任何 odd prime 同时进入 `TQ^2` 与 `omega^circ`，都必须来自 `c_Q` support。

---

## 4. tail 与 `omega^circ` 的 exact gcd

前一文件得到

\[
\boxed{
\Lambda_{\rm tail}
=2E_MNS\omega^\circ
+TQ^2W^\circ,}
\tag{4.1}
\]

以及

\[
\boxed{\gcd(\omega^\circ,W^\circ)=1.}
\tag{4.2}
\]

模 `omega^circ`：

\[
\Lambda_{\rm tail}
\equiv TQ^2W^\circ
\pmod{\omega^\circ}.
\]

由 (4.2)：

\[
\gcd(TQ^2W^\circ,\omega^\circ)
=\gcd(TQ^2,\omega^\circ).
\]

结合 (3.1)：

\[
\boxed{
\gcd(\Lambda_{\rm tail},\omega^\circ)
=\gcd(c_Q^2,\omega^\circ).}
\tag{4.3}
\]

这是 exact gcd identity，不只是 support inclusion。

---

## 5. tail 与整个 imbalance cofactor 的 overlap 只在 `c_Q`

前一文件已经证明

\[
\boxed{
\gcd(\Lambda_{\rm tail},W^\circ)=1.}
\tag{5.1}
\]

又

\[
\gcd(\omega^\circ,W^\circ)=1.
\]

所以

\[
\begin{aligned}
\gcd(
\Lambda_{\rm tail},
\omega^\circ W^\circ)
&=\gcd(\Lambda_{\rm tail},\omega^\circ)\\
&=\gcd(c_Q^2,\omega^\circ).
\end{aligned}
\]

即

\[
\boxed{
\gcd(
\Lambda_{\rm tail},
\omega^\circ W^\circ)
=\gcd(c_Q^2,\omega^\circ)
\mid c_Q^2.}
\tag{5.2}
\]

因此把 `c_Q` support 删除后：

\[
\boxed{
\operatorname{Supp}(\Lambda_{\rm tail})
\cap
\operatorname{Supp}(\omega^\circ W^\circ)
=\varnothing
\quad\text{outside }c_Q.}
\tag{5.3}
\]

---

## 6. 对 genuine equal-depth height target，separation 是完全的

`primitive-reduction.md` 已证明任何 genuine non-`3` height prime `p|W_q` 满足

\[
\boxed{p\nmid c_Q.}
\tag{6.1}
\]

因此对本文 equal-depth target prime：

\[
p\mid\Gamma,
\qquad
p\nmid\omega^\circ W^\circ c_Q.
\]

若 `rho_p>0`，则

\[
p\mid\Lambda_{\rm tail}.
\]

结合 (5.2)：该 prime 的 tail appearance 不可能来自 imbalance cofactor 的复用。

所以 canonical prime allocation 已变成：

\[
\boxed{
\begin{array}{c|c}
\text{mechanism}&\text{carrier}\ \hline
\text{unequal depth}&\omega^\circ W^\circ\\
\text{equal-depth baseline}&\Gamma^2\\
\text{equal-depth resonance tail}&\Lambda_{\rm tail}
\end{array}}
\tag{6.2}
\]

且最后一行与第一行对 genuine height primes 已完全 support-separated。

---

## 7. 当前剩余 overlap 被压到 `Gamma`

由 (5.2)，tail 与 imbalance sector 的 generic overlap 已经清空。

因此 equal-depth deep resonance 的 target primes若继续出现，只能来自它们本来就所在的 common square core：

\[
\boxed{
p\mid\Gamma
\quad\text{且}\quad
p^{\rho_p}\mid\Lambda_{\rm tail}.}
\tag{7.1}
\]

换句话说，真正尚未关闭的 gcd 已经压成单一对象

\[
\boxed{
\gcd(\Gamma,\Lambda_{\rm tail}).}
\tag{7.2}
\]

更高 `rho_p` 则对应该 gcd 在同一 prime 上的更深提升，直到超过 `v_p(\Gamma)` 后进入 higher tail powers。

下一步不再需要研究 `omega^circ W^circ` 与 tail 的 generic collision；应直接攻击 (7.2)，或把它与顶部小 defect `C_alpha` 的 square-modulus residue 联立。
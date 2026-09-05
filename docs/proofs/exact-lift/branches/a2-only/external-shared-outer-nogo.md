# A2 genuine external descendant-common prime 不能同时支付两个 outer cofactors

> **依赖：** [`outer-descendant-additive-lock.md`](outer-descendant-additive-lock.md)、`spontaneous-crt-pure-branch-defect.md`（历史正文已整合进 `crt-descent-ledger.md`）、`spontaneous-sphere-roots.md`（历史正文已整合进 `source-angle-ledger.md`）。
>
> **严格状态：**在危险 `Z≡1 (mod4)` orientation 中，`Xi_-`,`Xi_+` 都是 positive `3 mod4`、且都是 `3`-进单位，因此各自必须有 non-`3` inert supplier。此前已经排除 fixed `7/31/179` 与 source-common old pool 同时支付两边的可能。本文处理最后的 genuinely endpoint-external descendant-common kernel：若同一 genuine non-`3` inert prime `p` 同时满足 `p|G_Delta` 与 `p|Xi_-,Xi_+`，则 rational-root quartic 的真实第四根与 descendant defect reader 冲突，generic `K`-unit sector只剩 fixed `7`，而它落回 target boundary；唯一 `K=0` coefficient boundary为 fixed `11491`，其六个 algebraic sphere states全部不在真实 decimal orbit `<10>`。因此 genuine external shared reuse **为空**。本文的结论是“一个 descendant-common prime不能同时支付两个 outer parity”，尚不单独宣称 `A2=∅`。

---

## 1. additive lock 下的 rational-root quartic

沿用

\[
\zeta:=a_3/T,
\qquad
R_0(K,\zeta)
:=K^2-(18+4\zeta)K+18\zeta+55.
\tag{1.1}
\]

`outer-descendant-additive-lock.md` 已证明，任意 genuine odd descendant-common prime

\[
p\mid G_\Delta
\]

同时整除原 primitive additive carrier，因此 coefficient ratio 不再自由：

\[
\frac{Q^2N_0}{b_2^2}
\equiv R_0(K,\zeta)
\pmod p.
\tag{1.2}
\]

定义 locked rational-root polynomial

\[
\boxed{
\Phi(J)
:=J(J+2\zeta)(K-J)^2-R_0(J+\zeta)^2.}
\tag{1.3}
\]

若同一 prime还支付两个 outer cofactors，

\[
p\mid\Xi_-,
\qquad
p\mid\Xi_+,
\tag{1.4}
\]

则

\[
\boxed{\Phi(2)\equiv\Phi(4)\equiv0\pmod p.}
\tag{1.5}
\]

---

## 2. 两个 outer roots 自动给出完整四根分解

对 `Phi(J)` 关于

\[
(J-2)(J-4)
\]
做 exact polynomial division。checker验证商恰为

\[
\boxed{
(J-3)(J-2K+2\zeta+9).}
\tag{2.1}
\]

余式是 `J` 的一次式，而且有 exact interpolation identity

\[
2\operatorname{Rem}(J)
=(4-J)\Phi(2)+(J-2)\Phi(4).
\tag{2.2}
\]

因此在 (1.5) 下，任意 odd prime上都有

\[
\boxed{
\Phi(J)
\equiv
(J-2)(J-3)(J-4)
(J-2K+2\zeta+9)
\pmod p.}
\tag{2.3}
\]

真实 rational root为

\[
\boxed{J_{def}=3-C/D.}
\tag{2.4}
\]

对 genuinely external prime，`D-C,C,D+C` 都是 units；否则 prime已经回到 target old pool。因此

\[
J_{def}\not\equiv2,3,4\pmod p.
\tag{2.5}
\]

所以只能取第四根：

\[
3-C/D
\equiv2K-2\zeta-9
\pmod p.
\]

即

\[
\boxed{
\delta:=C/D
\equiv12+2\zeta-2K
\pmod p.}
\tag{2.6}
\]

这一步把 shared-outer 条件直接变成 top finite defect 的 natural-representative 线性锁。

---

## 3. descendant defect reader 与 outer defect lock 的差恰为 curvature term

历史 `spontaneous-crt-pure-branch-defect.md` 从 fully primitive descended quotient得到 universal identity

\[
\frac{\mathscr F_{63}}{gT}
=(2K-9)(2K-12-2\zeta+\delta)
-\frac{63}{16}K^2.
\tag{3.1}
\]

任意 noncentral descendant-common prime满足

\[
p\mid\mathscr F_{63},
\qquad
p\nmid2K-9,
\]
故

\[
\boxed{
\delta
\equiv12+2\zeta-2K
+\frac{63K^2}{16(2K-9)}
\pmod p.}
\tag{3.2}
\]

和 outer lock (2.6) 相减：

\[
\boxed{63K^2\equiv0\pmod p.}
\tag{3.3}
\]

这就是 genuine external shared-reuse 的主塌缩。

注意 central sheet必须单独处理，不能从 (3.2) 偷除 `2K-9`。

---

## 4. central `2K-9=0` 对 non-`3` odd prime没有真实 shared root

直接取

\[
K=9/2.
\]

checker得到

\[
\Phi(2)
=\frac{23\zeta^2+192\zeta+192}{4},
\]

\[
\Phi(4)
=\frac{23\zeta^2+192\zeta+384}{4}.
\]

所以

\[
\boxed{
\Phi(4)-\Phi(2)=48.}
\tag{4.1}
\]

若二者同时模 `p` 消失，则 `p|48`。因此对 non-`3` odd prime：

\[
\boxed{2K-9=0\text{ 的 elimination factor 没有真实 shared-outer root}.}
\tag{4.2}
\]

这说明 `outer-descendant-additive-lock.md` resultant 中的 central factor是 coefficient degeneration，而不是 genuine external escape。

---

## 5. `K` 为 unit 时只剩 fixed `7`，且它落回 target boundary

现在处于 noncentral sector并假设

\[
p\nmid K.
\]

由 (3.3)：

\[
p\mid63=3^2\cdot7.
\]

当前 `p` 是 non-`3` inert prime，所以

\[
\boxed{p=7.}
\tag{5.1}
\]

对整个 `F_7^2` 精确枚举 `(K,zeta)` 并只要求真实 outer equations

\[
\Phi(2)=\Phi(4)=0
\]
，checker得到唯一状态

\[
\boxed{(K,\zeta)=(3,4)=(3,-3)\pmod7.}
\tag{5.2}
\]

此时 (2.6) 给

\[
\boxed{\delta=C/D\equiv0\pmod7.}
\tag{5.3}
\]

即 `7|C`，它是 target boundary，而不是 genuinely external state。因此：

\[
\boxed{K\text{-unit genuine external shared reuse为空}.}
\tag{5.4}
\]

---

## 6. `K=0` coefficient boundary只剩 fixed `11491`

还必须单列

\[
p\mid K.
\tag{6.1}
\]

将 `K=0` 代入两个 outer equations并关于 `zeta` 求 resultant：

\[
\boxed{
|\operatorname{Res}_\zeta(\Phi(2),\Phi(4))|
=2^{10}3^6\cdot11491.}
\tag{6.2}
\]

其中

\[
\boxed{11491\text{ 为素数},\qquad11491\equiv3\pmod4.}
\tag{6.3}
\]

所以 non-`3` inert coefficient boundary唯一可能是

\[
\boxed{p=11491.}
\tag{6.4}
\]

在 `F_11491[zeta]` 中两个 outer polynomials的 gcd恰为

\[
\boxed{\zeta-743.}
\tag{6.5}
\]

故 first-layer state进一步固定为

\[
\boxed{K=0,\qquad\zeta=743\pmod{11491}.}
\tag{6.6}
\]

这里 `zeta` 非零，所以该点仍是 alpha-free candidate；不能仅凭 content separation删除。

---

## 7. fixed `11491` 的 sphere branches 全部错过 decimal orbit

对 genuine pure-spontaneous branch沿用

\[
\tau=10^{-M},
\qquad
s=9+y,
\qquad
K=s/\tau,
\qquad
\zeta=z_i/\tau.
\tag{7.1}
\]

由 `K=0` 且 `tau` 为 unit：

\[
\boxed{s=0,\qquad y=-9\pmod{11491}.}
\tag{7.2}
\]

两张 explicit sphere root `z_i(x,y)` 由 `spontaneous-sphere-roots.md` 给出。compact branch quadratic为

\[
55\tau^2+18(z_i-s)\tau+s^2-4sz_i-c=0,
\tag{7.3}
\]
其中

\[
c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.
\]

现在 `s=0`、`z_i=zeta*tau`，所以

\[
\boxed{
c=(55+18\zeta)\tau^2.}
\tag{7.4}
\]

对 fixed `p=11491,zeta=743,y=-9`，checker完整枚举两个 genuine sphere orientations。所有 branch-boundary denominator均保持 unit，且仅有六组代数状态：

\[
\boxed{
\begin{array}{c|c|c|c}
i&x&z_i&\tau\\ \hline
1&241&11030&4902\\
2&241&461&6589\\
1&4766&2557&653\\
2&4766&8934&10838\\
1&8871&6488&4169\\
2&8871&5003&7322
\end{array}}
\pmod{11491}.
\tag{7.5}
\]

但是

\[
\boxed{10^{766}\equiv1\pmod{11491}.}
\tag{7.6}
\]

任何真实 decimal phase

\[
\tau=10^{-M}
\]
必属于 `<10>`，因此必要地

\[
\tau^{766}=1.
\tag{7.7}
\]

对 (7.5) 的六个 `tau`，checker逐一验证

\[
\boxed{\tau^{766}\not\equiv1\pmod{11491}.}
\tag{7.8}
\]

所以 fixed `11491` 的全部代数 branch都不来自真实十进制长度。

因此

\[
\boxed{K=0\text{ genuine decimal external branch为空}.}
\tag{7.9}
\]

---

## 8. 结论：genuine external shared reuse 全部删除

§§4–7 覆盖 central、`K`-unit、`K=0` 三类：

\[
\boxed{
\begin{gathered}
p\ne3,\quad p\equiv3\pmod4,\\
p\mid G_\Delta,\quad
p\mid\Xi_-,\quad p\mid\Xi_+,\\
p\text{ genuinely endpoint-external}
\end{gathered}
\Longrightarrow\bot.}
\tag{8.1}
\]

结合此前 old-pool audits：

- fixed `7/31/179` 不能同时支付两个 outer cofactors；
- source-common shared reuse 已由 additive coefficient lock全部删除；
- 本文删除剩余 genuine external shared reuse。

因此现在可以严格说：

\[
\boxed{
\text{没有任何 descendant-common non-3 inert prime}
\text{ 能同时支付 }\Xi_-\text{ 与 }\Xi_+\text{ 两份 parity}.}
\tag{8.2}
\]

这会给后续 global product/parity allocation一个真正的 distinct-prime surcharge：如果某枚 common prime吸收 descendant odd parity，它至多同步支付一个 outer cofactor；另一个 outer cofactor仍要求 common support之外的 non-`3` inert supplier。

本文尚未证明这些被迫 distinct supports的总乘积一定超过全部 natural-representative heights，所以 `A2` 状态仍保持 `待证`。

---

## 9. verification

```bash
uv run python scripts/exact-lift/a2-only/research-checks/crt-descent/check_a2_external_shared_outer_nogo.py
```

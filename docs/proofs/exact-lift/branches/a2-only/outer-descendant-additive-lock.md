# A2 outer-pair / descendant-common 的 additive coefficient-ratio lock

> **依赖：** [`outer-cofactor-reuse-gate.md`](outer-cofactor-reuse-gate.md)；本分支新增的 additive/descendant gcd theorem
> \[
> \gcd(\widehat{\mathcal T}_2,\mathscr R_{63}^\star)
> =\gcd(\widehat{\mathcal T}_2,\widehat{\mathscr D}_{63})
> =G_\Delta;
> \]
> `endpoint-lattice.md` 的 primitive additive identity；source-common exact collision `18K-55=0`。
>
> **严格状态：**此前 shared outer supplier只通过 `F(2),F(4)` 交叉消去一个自由 coefficient ratio，得到 `G_pm(K,zeta)=0`。本文利用新的 gcd 接口补回遗漏的更强信息：任何 descendant-common prime都自动整除原 primitive additive carrier，因此 coefficient ratio 不再自由，而被固定为
> \[
> R_0=K^2-(18+4\zeta)K+18\zeta+55.
> \]
> 两个 outer values 因而必须同时满足 `Phi_2=Phi_4=0`。其 exact resultant只剩 `K=3`、central `2K-9=0` 与一个不可约 quartic `Q_4(K)`。再与 source-common line `18K-55=0` 相交后，全部 odd support只剩 split primes `13` 与 `1350049`；所以 genuine `3 mod4` source-common prime**不可能**同时支付两个 outer cofactors并复用 descendant common。上一文件 `source-common-outer-fixed-exception.md` 留下的巨大 `p_*` 因此被本文严格排除。本文仍未删除 genuinely endpoint-external common kernel，故 A2 仍为 `待证`。

---

## 1. descendant common 自动回到 original additive carrier

记

\[
G_\Delta:=\gcd(\mathscr R_{63}^\star,\widehat{\mathscr D}_{63}).
\]

新的 exact gcd interface 已证明

\[
\boxed{
\gcd(\widehat{\mathcal T}_2,\mathscr R_{63}^\star)
=
\gcd(\widehat{\mathcal T}_2,\widehat{\mathscr D}_{63})
=
G_\Delta.}
\tag{1.1}
\]

因此任何 prime

\[
p\mid G_\Delta
\]

都满足

\[
\boxed{p\mid\widehat{\mathcal T}_2.}
\tag{1.2}
\]

这正是此前 outer-pair / descendant compatibility 中没有使用的一层信息。

---

## 2. additive carrier 把 rational-root coefficient ratio 固定为 `R_0`

primitive additive identity可写成

\[
U^2 2^m\widehat{\mathcal T}_2
=
b_2^2F_0-TQ^2N_0,
\tag{2.1}
\]

其中 `U` 只含固定 `2`-power，而

\[
\boxed{
F_0
=T\left[K^2-(18+4\zeta)K+18\zeta+55\right],
\qquad
\zeta:=a_3/T.}
\tag{2.2}
\]

定义

\[
\boxed{R_0(K,\zeta):=K^2-(18+4\zeta)K+18\zeta+55.}
\tag{2.3}
\]

对 genuine odd prime `p|G_Delta`，相关 `2,T,b_2` 都是 `p`-进单位。由 (1.2),(2.1)：

\[
\boxed{
\frac{Q^2N_0}{b_2^2}
\equiv R_0(K,\zeta)
\pmod p.}
\tag{2.4}
\]

另一方面 rational-root quartic除去公共 `T^2` 后正是

\[
\Phi(J)
=J(J+2\zeta)(K-J)^2
-rac{Q^2N_0}{b_2^2}(J+\zeta)^2.
\tag{2.5}
\]

所以在 descendant-common prime上必须使用固定版本

\[
\boxed{
\Phi_0(J)
:=J(J+2\zeta)(K-J)^2-R_0(J+\zeta)^2.}
\tag{2.6}
\]

这比只从 `F(2)=F(4)=0` 交叉消掉 coefficient ratio严格更强。

---

## 3. shared outer supplier 必须同时满足两个显式 cubic/quadratic forms

若同一 genuine prime还同时支付两个 outer cofactors，

\[
p\mid\Xi_-,
\qquad
p\mid\Xi_+,
\tag{3.1}
\]

则

\[
\boxed{
\Phi_2:=\Phi_0(2)\equiv0,
\qquad
\Phi_4:=\Phi_0(4)\equiv0
\pmod p.}
\tag{3.2}
\]

直接展开：

\[
\boxed{
\begin{aligned}
\Phi_2={}&
-K^2\zeta^2+4K\zeta^3+34K\zeta^2+72K\zeta+56K\\
&-18\zeta^3-127\zeta^2-276\zeta-204,
\end{aligned}}
\tag{3.3}
\]

\[
\boxed{
\begin{aligned}
\Phi_4={}&
-K^2\zeta^2+4K\zeta^3+50K\zeta^2+144K\zeta+160K\\
&-18\zeta^3-199\zeta^2-600\zeta-624.
\end{aligned}}
\tag{3.4}
\]

两式之差除以 `4` 得较小的 quadratic-in-`zeta` gate

\[
\boxed{
H_{24}
=4K\zeta^2+18K\zeta+26K
-18\zeta^2-81\zeta-105.}
\tag{3.5}
\]

因此 shared outer + descendant common 必须满足

\[
\Phi_2=H_{24}=0.
\tag{3.6}
\]

---

## 4. exact elimination 只剩两个 linear sheets 与一个 quartic

对 (3.3),(3.5) 关于 `zeta` 求 resultant：

\[
\boxed{
\operatorname{Res}_\zeta(\Phi_2,H_{24})
=2(K-3)^2(2K-9)Q_4(K),}
\tag{4.1}
\]

其中

\[
\boxed{
Q_4(K)
=676K^4-8004K^3+34801K^2-65868K+45964.}
\tag{4.2}
\]

checker验证 `Q_4` 在 `Q[K]` 中不可约。

所以任意 genuine odd shared supplier都必须落在

\[
\boxed{
K\equiv3,
\quad
2K-9\equiv0,
\quad\text{或}\quad
Q_4(K)\equiv0
\pmod p.}
\tag{4.3}
\]

这把原先 irreducible degree-30 gate大幅压成一个 quartic加两个线性 sheet；下降来自 (1.1) 提供的 original-additive coefficient lock。

---

## 5. source-common line 与三个 additive-locked sheets 全部 inert-disjoint

source-common genuine support还满足

\[
\boxed{L_S:=18K-55\equiv0\pmod p.}
\tag{5.1}
\]

逐项相交。

### 5.1 `K=3`

\[
\boxed{
\operatorname{Res}_K(K-3,L_S)=-1.}
\tag{5.2}
\]

因此完全无公共 prime。

### 5.2 central `2K-9=0`

\[
\boxed{
\operatorname{Res}_K(2K-9,L_S)=52=2^2\cdot13.}
\tag{5.3}
\]

唯一 odd candidate `13` 满足

\[
13\equiv1\pmod4.
\tag{5.4}
\]

所以没有 inert prime。

### 5.3 quartic `Q_4=0`

\[
\boxed{
\operatorname{Res}_K(Q_4,L_S)
=21600784
=2^4\cdot1350049.}
\tag{5.5}
\]

而

\[
\boxed{1350049\text{ 为素数},\qquad1350049\equiv1\pmod4.}
\tag{5.6}
\]

因此 quartic intersection同样没有 `3 mod4` prime。

三类合并：

\[
\boxed{
\begin{gathered}
p\equiv3\pmod4,\quad
p\mid G_\Delta,\quad
p\mid\Xi_-,\Xi_+,\\
p\mid G_S^{\rm source}
\end{gathered}
\Longrightarrow\bot.}
\tag{5.7}
\]

即 genuine source-common descendant label不能同时给两个 outer cofactor parity付款。

---

## 6. weaker giant exception `p_*` 被 additive lock 删除

`source-common-outer-fixed-exception.md` 只把 source line、shared-outer free-ratio cubic与 universal descendant cubic联立，因此留下

\[
p_\star=740759498168792879433565547.
\]

该结论作为**较弱必要条件**没有代数错误，但缺少 (1.2)–(2.4) 的 coefficient-ratio lock。

在其真实 first-layer residue

\[
K\equiv55/18,
\qquad
\zeta\equiv121854543490110025177920950
\pmod{p_\star}
\]

直接代入：

\[
\boxed{
\Phi_2\not\equiv0\pmod{p_\star},
\qquad
\Phi_4\not\equiv0\pmod{p_\star}.}
\tag{6.1}
\]

所以

\[
\boxed{p_\star\text{ 被新的 additive lock 严格排除}.}
\tag{6.2}
\]

后续不得再把它列为活跃 frontier。

---

## 7. 更新后的 `Z=1` old-pool boundary

结合 fixed `7/31/179` 的 direct `F_p` outer-pair audit：

1. fixed height `7`、fixed target `31/179` 均不能同时支付 `Xi_-`,`Xi_+`；
2. source-common moving/fixed shared-reuse pool由本文全部删除；
3. 因而能让同一 prime同时支付两个 outer parities并复用 `G_Delta` 的 old-pool来源已经清空；
4. 剩余 shared-reuse 只能来自 genuinely endpoint-external descendant-common kernel，并必须落在 (4.3) 的 additive-locked `K=3 / central / Q_4` 三张 sheet上。

这显著收紧了 dangerous

\[
Z\equiv1\pmod4,
\qquad
G_\Delta\equiv3\pmod4
\]

逃逸口，但本文尚未排除第 4 项，因此不宣称 A2 全局关闭。

---

## 8. verification

```bash
uv run python scripts/exact-lift/a2-only/research-checks/crt-descent/check_a2_outer_descendant_additive_lock.py
```

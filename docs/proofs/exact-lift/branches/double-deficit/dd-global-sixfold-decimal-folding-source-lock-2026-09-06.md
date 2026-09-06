# DD global sixfold decimal folding 与 baseline-free source lock

> 日期：2026-09-06
>
> 依赖：global exact-lift integer bridge、DD prefix concat `Q=b_1 10^{m_2}+b_2`、[`dd-corrected-hard-source-split-2026-08-22.md`](dd-corrected-hard-source-split-2026-08-22.md)、[`dd-ultrahard-tail-root-sign-collapse-2026-08-22.md`](dd-ultrahard-tail-root-sign-collapse-2026-08-22.md)、[`dd-discriminant-root-dependency-audit-2026-08-22.md`](dd-discriminant-root-dependency-audit-2026-08-22.md) 的 safe global DD upper。
>
> **严格状态：已严格完成（universal folding identity + exact baseline-free ultra-hard source consequence）。**
>
> 本文给 corrected post-tail pure-source branch 一个此前缺失的、与 prefix `Q=b_1 10^{m_2}+b_2` 不同的 global decimal reader。它只使用原始 exact lift 和十进制 block concat，不使用 discriminant root、tail-root、Gaussian orientation 或已撤销的 `General-transfer-local`。
>
> 对任意整数 `k>=1`，若
> \[
> n=kS+e,
> \qquad S=m_1+m_2,
> \qquad e\ge0,
> \]
> 则有 universal block-folding congruence
> \[
> \boxed{
> q_{\rm lcm}A_{12}(-b_2)^k10^{km_1}10^e
> \equiv
> b_1^k\bigl(H_{\rm sph}b_3-q_{\rm lcm}a_3\bigr)
> \pmod Q.}
> \]
> 在 DD 高斜率 `6S<n<7S` 区域取 `k=6`，得到
> \[
> \boxed{
> Q\mid
> q_{\rm lcm}A_{12}b_2^6 10^{6m_1}10^{n-6S}
> -b_1^6\bigl(H_{\rm sph}b_3-q_{\rm lcm}a_3\bigr).}
> \]
> 因为 sixfold exponent为偶数，不再有 sign。
>
> 对 baseline-free ultra-hard source factor `X|Q`，已有 corrected ledger恰保证 folding coefficient在 `X` 上为 unit。因此只要 `X>10^{n-6S}`，上式就把短纯十进制幂 `10^{n-6S}` 从一个模类升级成 ordinary exact least-residue reconstruction。

---

## 1. exact-lift modulo `Q`

写 numerator / denominator concat

\[
\alpha=A_{12}10^n+a_3,
\qquad
\beta=Q10^m+b_3.
\]

整数球面 bridge 为

\[
\boxed{
q_{\rm lcm}\alpha=H_{\rm sph}\beta.}
\tag{1.1}
\]

把 concat 代入：

\[
q_{\rm lcm}A_{12}10^n+q_{\rm lcm}a_3
=H_{\rm sph}Q10^m+H_{\rm sph}b_3.
\]

定义 full-lift tail residual

\[
\boxed{
D_3:=H_{\rm sph}b_3-q_{\rm lcm}a_3.}
\tag{1.2}
\]

则 exact 地

\[
\boxed{
q_{\rm lcm}A_{12}10^n-D_3
=H_{\rm sph}Q10^m.}
\tag{1.3}
\]

因此

\[
\boxed{
q_{\rm lcm}A_{12}10^n\equiv D_3\pmod Q.}
\tag{Lift-Q}
\]

这就是第二个 global decimal parent；它来自 full exact lift，而不是 source-prefix valuation ledger。

---

## 2. universal block folding

DD prefix denominator concat为

\[
\boxed{Q=b_1 10^{m_2}+b_2.}
\tag{2.1}
\]

故

\[
\boxed{b_1 10^{m_2}\equiv-b_2\pmod Q.}
\tag{2.2}
\]

固定整数 `k>=1`，并假设

\[
\boxed{n=kS+e,\qquad e\ge0.}
\tag{2.3}
\]

其中

\[
S=m_1+m_2.
\]

把 `(Lift-Q)` 乘以 `b_1^k`：

\[
q_{\rm lcm}A_{12}b_1^k10^{k(m_1+m_2)+e}
\equiv b_1^kD_3\pmod Q.
\]

整理为

\[
q_{\rm lcm}A_{12}10^{km_1}10^e
\bigl(b_1 10^{m_2}\bigr)^k
\equiv b_1^kD_3\pmod Q.
\]

使用 `(2.2)`：

\[
\boxed{
q_{\rm lcm}A_{12}(-b_2)^k10^{km_1}10^e
\equiv
b_1^kD_3
\pmod Q.}
\tag{Block-folding-k}
\]

即

\[
\boxed{
Q\mid
q_{\rm lcm}A_{12}(-b_2)^k10^{km_1}10^e
-b_1^kD_3.}
\tag{2.4}
\]

这是纯 exact-lift / decimal-concat identity，对 canonical / Gaussian / resonance hypotheses均无依赖。

---

## 3. DD high-slope 的 sixfold specialization

当前 safe DD asymptotic upper为

\[
\limsup_{\rm DD}\frac nS
\le c_*
=6.308883577618\ldots<7.
\]

因此任何研究 frontier `>6` 的 sufficiently large subsequence都 eventually 满足

\[
\boxed{6S<n<7S.}
\tag{3.1}
\]

定义整数

\[
\boxed{e:=n-6S,\qquad 1\le e<S.}
\tag{3.2}
\]

在 `(Block-folding-k)` 取 `k=6`；由于 `(-b_2)^6=b_2^6`，得到

\[
\boxed{
q_{\rm lcm}A_{12}b_2^6 10^{6m_1}10^e
\equiv
b_1^6D_3
\pmod Q.}
\tag{Sixfold-folding}
\]

等价地：

\[
\boxed{
Q\mid
q_{\rm lcm}A_{12}b_2^6 10^{6m_1}10^e
-b_1^6(H_{\rm sph}b_3-q_{\rm lcm}a_3).}
\tag{Sixfold-divisibility}
\]

注意 `e=n-6S` 正是 `6.308883...` frontier 相对六倍 prefix scale留下的短 decimal exponent；其 equality-ray leading height为

\[
\frac eS\to c_*-6
=0.308883577618\ldots
=z_*.
\]

---

## 4. arbitrary source factor 的 residue lock

令

\[
X\mid Q
\]
为任意正整数，且满足

\[
\boxed{
(X,10q_{\rm lcm}A_{12}b_2)=1.}
\tag{4.1}
\]

则 sixfold leading coefficient

\[
C_6:=q_{\rm lcm}A_{12}b_2^6 10^{6m_1}
\]
在 modulo `X` 可逆。由 `(Sixfold-folding)`：

\[
\boxed{
10^e
\equiv
b_1^6D_3\,C_6^{-1}
\pmod X.}
\tag{Sixfold-source-residue}
\]

令

\[
\rho_X:=
\bigl[b_1^6D_3C_6^{-1}\bigr]_X
\in\{0,1,\ldots,X-1\}
\]
为 least nonnegative residue。

若进一步

\[
\boxed{0<10^e<X,}
\tag{4.2}
\]

则 ordinary representative唯一性直接给

\[
\boxed{10^e=\rho_X.}
\tag{Sixfold-source-lock}
\]

因此 full exact lift把大 source divisor `X` 转换成对短 pure decimal power `10^{n-6S}` 的 deterministic reconstruction。

这不是 candidate counting，也不需要 residue equidistribution。

---

## 5. exact baseline-free ultra-hard source 自动满足 unit hypothesis

[`dd-ultrahard-tail-root-sign-collapse-2026-08-22.md`](dd-ultrahard-tail-root-sign-collapse-2026-08-22.md) 的 baseline-free endpoint对每个 target prime给

\[
\boxed{
p\nmid10b_1b_2b_3,}
\]

\[
\boxed{p^c\Vert Q,\qquad c>0,}
\]

\[
\boxed{v_p(A_{12})=0,}
\]

以及

\[
\boxed{p\nmid q_{\rm lcm}.}
\]

所以若 `X` 是这些 exact baseline-free ultra-hard prime powers的任意乘积，则自动有

\[
\boxed{(X,10q_{\rm lcm}A_{12}b_2)=1.}
\tag{Ultra-hard-unit}
\]

因此该 branch 不需要为 `(4.1)` 再支付任何 exceptional mass；sixfold source residue对整个 exact baseline-free product同时成立。

---

## 6. full-height baseline-free source 的 ordinary lock

考虑一列 high-slope DD candidates及其 exact baseline-free ultra-hard source products `X=X(S)`，满足

\[
\boxed{
\log_{10}X=S-o(S).}
\tag{6.1}
\]

由 safe global DD upper：

\[
\frac nS\le c_*+o(1),
\]

所以

\[
\frac eS
=\frac nS-6
\le c_*-6+o(1)
=z_*+o(1).
\]

即

\[
\boxed{
\log_{10}10^e
\le(z_*+o(1))S,}
\tag{6.2}
\]

其中

\[
z_*=0.308883577618\ldots<1.
\]

另一方面 `(6.1)` 给

\[
\log_{10}X=(1-o(1))S.
\]

二者有固定 leading margin

\[
1-z_*
=0.691116422381969\ldots
=U_*>0.
\]

因此 sufficiently large `S` 时

\[
\boxed{0<10^e<X.}
\tag{6.3}
\]

结合 §5 的 unit hypothesis和 `(Sixfold-source-lock)`：

\[
\boxed{
10^{n-6S}
=
\left[
 b_1^6(H_{\rm sph}b_3-q_{\rm lcm}a_3)
 (q_{\rm lcm}A_{12}b_2^6 10^{6m_1})^{-1}
\right]_X.}
\tag{Full-height-sixfold-lock}
\]

所以 corrected post-tail ledger 中最危险的 **exact baseline-free full-height source core** 不再只是一个没有 reader 的 large divisor：full exact lift强迫它唯一读取一个只有 `z_*S+o(S)` 高度的 pure decimal power。

---

## 7. 与 corrected deep-hard `X_{H,D}` 的作用域边界

[`dd-corrected-hard-source-split-2026-08-22.md`](dd-corrected-hard-source-split-2026-08-22.md) 对一般 deep-hard source证明

\[
X_{H,D}Y_{H,D}\mid C_Q,
\]

并且若

\[
\log X_{H,D}=S-o(S),
\]

则 aggregate baseline `Y_{H,D}` 只有 `10^{o(S)}` 高度。

但

\[
Y_{H,D}=10^{o(S)}
\]
**并不自动意味着** `X_{H,D}` 含有一个 `10^{S-o(S)}` 高度的 exact baseline-zero subproduct：每个 target prime仍可能携带小但非零 local baseline。

因此本文的 full-height corollary严格只对：

\[
\boxed{
\text{exact baseline-free ultra-hard source product}}
\]

生效；不能未经新的 stripping theorem 就把 `(Full-height-sixfold-lock)` 宣称覆盖全部 `X_{H,D}`。

下一 quantitative post-tail target应是：把 `(Block-folding-k)` 与 corrected hard-source local ledger联合，构造一个 **baseline-stripped folding modulus**，证明 small aggregate `Y_{H,D}` 只造成 `o(S)` 的 modulus损失。若能做到，则 sixfold lock有望从 exact endpoint扩展到整个 dangerous deep-hard core。

---

## 8. 方法意义

此前 ultra-hard theorem已经证明 tail-root surviving sign精确退回 gap/tail-weight algebra，因此 local Hensel continuation不会给第二 source modulus。

本文提供的 `(Sixfold-folding)` 来自真正不同的 parent：

\[
\boxed{
\text{full exact lift }q_{\rm lcm}\alpha=H_{\rm sph}\beta
\quad+\quad
\text{prefix decimal concat}.}
\]

它没有重复 tail-root/discriminant source depth，并且直接作用于 decimal exponent `e=n-6S`。

因此 corrected post-tail pure-source branch现在具有一个真正 global deterministic reader：

\[
\boxed{
\text{full-height baseline-free source}
\Longrightarrow
\text{unique short decimal-power residue}.}
\]

这仍不是 contradiction：右侧 residue可能恰好是 `10^e`。下一步必须把该 exact residue与另一个 independent decimal/digit-shell condition联立，或先把 folding lock推广到 baseline-stripped `X_{H,D}` 后做 global location/counting。

---

## 9. 状态摘要

- **已严格完成：** universal `Block-folding-k` identity；
- **已严格完成：** DD `6S<n<7S` 的 `Sixfold-folding`；
- **已严格完成：** source factor residue `(Sixfold-source-residue)`；
- **已严格完成：** exact baseline-free ultra-hard support自动满足 coefficient-unit hypothesis；
- **已严格完成：** full-height exact baseline-free source `X=10^{S-o(S)}` 对 `10^{n-6S}` 的 ordinary least-residue lock；
- **仍待证：** baseline-stripped extension到一般 `X_{H,D}`；与第二 digit-shell reader联立后的 contradiction；post-tail/global DD slope improvement或 emptiness。

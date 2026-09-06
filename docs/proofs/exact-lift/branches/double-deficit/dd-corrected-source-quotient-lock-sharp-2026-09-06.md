# DD corrected source quotient `q` 的 direct `v_2` least-residue lock

> 日期：2026-09-06
>
> 依赖：[`dd-corrected-sunit-euclidean-lock-2026-09-06.md`](dd-corrected-sunit-euclidean-lock-2026-09-06.md)、[`dd-corrected-common-scale-ray-sharp-2026-09-06.md`](dd-corrected-common-scale-ray-sharp-2026-09-06.md)、[`dd-corrected-high-funnel-quantitative-defect-2026-08-22.md`](dd-corrected-high-funnel-quantitative-defect-2026-08-22.md)、[`dd-corrected-terminal-digit-polarization-2026-08-22.md`](dd-corrected-terminal-digit-polarization-2026-08-22.md)、[`dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md`](dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md)、[`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)、[`dd-corrected-terminal-rough-source-sharp-2026-08-22.md`](dd-corrected-terminal-rough-source-sharp-2026-08-22.md)、[`dd-corrected-gap-fiber-pairmax-rational-reconstruction-2026-08-22.md`](dd-corrected-gap-fiber-pairmax-rational-reconstruction-2026-08-22.md)。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` quantitative one-channel neighborhood 的显式子范围）。**
>
> 前一 `qZ` product lock先把 source variables压成一个小乘积。S-unit Euclidean lock现在允许更直接地处理 source quotient `q` 本身：固定 `(v_2,b_1)` 后，`v_1|b_1` 只有 divisor entropy；每个 `v_1` 给 `V=v_1v_2`，而 fixed `(H,T,V)` 已唯一恢复 `(U,Z)`。于是 prefix concat modulo `v_2` 直接给
> \[
> \boxed{Uq\equiv b_1 10^{m_2}\pmod{v_2}.}
> \]
> 本文用 shared-defect ledger证明
> \[
> \boxed{
> \frac1S\log_{10}\frac{v_2}{q}
> \ge U_*-\frac32\delta-o(1),}
> \]
> 因而在
> \[
> \boxed{
> \delta<\delta_q^{\sharp}:=\frac{2U_*}{3}
> =0.460744281587979\ldots}
> \]
> 内有 `0<q<v_2`，从而 `q` 是一个 ordinary least residue。结果：fixed `(v_2,b_1)` denominator/S-unit fiber 在该范围内只有 `10^{o(S)}` candidates；结合已有 numerator collapse，fixed-`v_2` full candidate count 的有效范围扩到 numerator 自身的阈值 `delta_UV=0.238062349248111...`。

---

## 1. exact modulo-`v_2` source line

canonical denominator identities为

\[
\boxed{Q=Uq,}
\qquad
\boxed{Q=b_1 10^{m_2}+b_2.}
\tag{1.1}

one-channel decomposition给

\[
V=v_1v_2,
\qquad v_2\mid b_2.
\tag{1.2}

因此

\[
\boxed{Uq\equiv b_1 10^{m_2}\pmod{v_2}.}
\tag{Source-line-v2}

canonical phase还有 `(U,V)=1`，故

\[
\boxed{(U,v_2)=1.}
\tag{1.3}

所以定义 least nonnegative residue

\[
\boxed{
\rho_q(U,b_1,m_2;v_2)
:=\left[U^{-1}b_1 10^{m_2}\right]_{v_2},
\qquad0\le\rho_q<v_2.}
\tag{1.4}

只要另外证明 `0<q<v_2`，就能把 `(Source-line-v2)` 升级为 exact equality `q=rho_q`。

---

## 2. uncoarsened `q` 与 `v_2`

令

\[
a:=\log_{10}2,
\qquad b:=1-a,
\]

\[
A:=\frac{2(1+2a)}3,
\qquad
U_*:=0.691116422381969\ldots,
\qquad
z_*:=1-U_*.
\]

仍写

\[
\delta:=c_*-\frac nS,
\qquad
\mu:=M_*-\frac mS.
\]

由 `Q=Uq` 与 `Q` 恰为 `S` 位整数，以及 uncoarsened `U` identity：

\[
\boxed{
\begin{aligned}
\frac{\log_{10}q}{S}-z_*
={}&-\frac{2b}{3}\mu
+aG_2+\frac{2b}{3}Q_5\\
&+\frac b3G_5+\frac b3N_5+R+o(1).}
\end{aligned}}
\tag{q-uncoarsened}

另一方面

\[
\frac{\log_{10}V}{S}
=1-aG_2-bG_5-R+o(1),
\]

且 `v_1|b_1`，所以

\[
\boxed{
\frac{\log_{10}v_2}{S}
\ge1-aG_2-bG_5-R-\frac{m_1}{S}-o(1).}
\tag{v2-via-m1}

保留 digit polarization 的 sharp intermediate：

\[
\boxed{
\begin{aligned}
\frac{m_1}{S}
\le{}&\frac\delta2
-\left(1-\frac b3\right)\mu
-\frac b3Q_5+rac b3G_5\\
&-\frac b6N_5+rac R2+o(1),
\end{aligned}}
\tag{m1-sharp}

以及

\[
\boxed{
aG_2\le\frac{m_1}{S}+aQ_2+o(1).}
\tag{G2-via-m1}

---

## 3. shared-defect comparison of `v_2/q`

从 `(v2-via-m1)-(q-uncoarsened)`：

\[
\begin{aligned}
\frac1S\log_{10}\frac{v_2}{q}-U_*
\ge{}&\frac{2b}{3}\mu
-2aG_2
-\frac{2b}{3}Q_5\\
&-\frac{4b}{3}G_5
-\frac b3N_5
-2R-\frac{m_1}{S}-o(1).
\end{aligned}
\tag{3.1}

用 `(G2-via-m1)`：

\[
-2aG_2
\ge-2\frac{m_1}{S}-2aQ_2-o(1).
\]

所以总共出现 `-3m_1/S`。代入 `(m1-sharp)` 后：

\[
\boxed{
\begin{aligned}
\frac1S\log_{10}\frac{v_2}{q}-U_*
\ge{}&-\frac32\delta
+\left(3-\frac b3\right)\mu
-2aQ_2\\
&+\frac b3Q_5
-\frac{7b}{3}G_5
+\frac b6N_5
-\frac72R-o(1).}
\tag{3.2}

现在使用 exact normalized identity

\[
\boxed{
A\mu
=\sigma_S+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)+2R+o(1).}
\tag{Mu-budget}

定义

\[
\boxed{
\eta:=\frac{3-b/3}{A}
=\frac{8+a}{2(1+2a)}
=2.590736314681693\ldots.}
\tag{3.3}

代入 `(3.2)`：

\[
\boxed{
\begin{aligned}
\frac1S\log_{10}\frac{v_2}{q}
\ge{}&U_*-\frac32\delta
+\eta\sigma_S\\
&+2a(\eta-1)Q_2+a\eta N_2\\
&+\frac b3(2\eta+1)Q_5
+\frac b3(4\eta-7)G_5\\
&+\frac b6(2\eta+1)N_5
+\left(2\eta-\frac72\right)R-o(1).}
\tag{v2-over-q-full}

数值上

\[
\eta=2.590736314681693\ldots>\frac74,
\]

所以

\[
4\eta-7>0,
\qquad
2\eta-\frac72>0,
\]

其余 coefficients显然也为正。故可以丢掉全部 correction：

\[
\boxed{
\frac1S\log_{10}\frac{v_2}{q}
\ge U_*-\frac32\delta-o(1).}
\tag{v2-over-q}

---

## 4. direct source-quotient lock threshold

若

\[
U_*-\frac32\delta>0,
\]

则 sufficiently large `S` 上

\[
0<q<v_2.
\]

定义

\[
\boxed{
\delta_q^{\sharp}
:=\frac{2U_*}{3}
=0.460744281587979\ldots.}
\tag{4.1}

于是

\[
\boxed{
\delta<\delta_q^{\sharp}
\Longrightarrow
q<v_2
\quad\text{eventually}.}
\tag{q-below-v2}

与 `(Source-line-v2)`、`(1.3)` 联立：

\[
\boxed{
q=\rho_q(U,b_1,m_2;v_2)
=\left[U^{-1}b_1 10^{m_2}\right]_{v_2}.}
\tag{q-residue-lock}

若 least residue为 `0`，该 fiber立即为空，因为 `q>0`。

---

## 5. fixed `(v_2,b_1)` denominator/S-unit fiber 只有 subexponential multiplicity

固定 digit/exponent layer以及

\[
(v_2,b_1).
\]

one-channel decomposition有

\[
v_1\mid b_1.
\]

因此 `v_1` 只有

\[
\tau(b_1)=10^{o(S)}
\]

种可能。对每个 `v_1`：

\[
\boxed{V=v_1v_2}
\]

唯一。

exponent coordinates `(H,T)` 在 fixed terminal window内只有 `S^{O(1)}=10^{o(S)}` 种。`dd-corrected-sunit-euclidean-lock-2026-09-06.md` 证明整个 one-channel neighborhood中 fixed `(H,T,V)` 后：

\[
\boxed{
Z=[2^{-H}V]_{5^T},
\qquad
U=\frac{2^HZ-V}{5^T}}
\]

至多唯一。

在本文范围 `delta<delta_q^sharp`，`q-residue-lock` 再唯一恢复 `q`。随后

\[
Q=Uq,
\qquad
b_2=Q-b_1 10^{m_2}
\]

唯一，并检查 positivity、digit length 与 `v_2|b_2`。通过后

\[
\gamma=\frac{b_1b_2}{V}
\]

唯一，而

\[
B=\frac{10^m}{2\cdot5^T},
\qquad
b_3=BVq
\]

也唯一恢复。

所以：

\[
\boxed{
N_{\rm den/SU}
\bigm|
(v_2,b_1)
=10^{o(S)}
\qquad(\delta<0.460744281587979\ldots).}
\tag{Fixed-v2-b1-direct-collapse}

这显著扩宽了早期依靠 `qZ<v_2` 所得到的 denominator reconstruction range。

---

## 6. fixed-`v_2` full candidate count扩到 numerator threshold

已有 quantitative digit polarization：

\[
\boxed{
m_1\le\kappa_{\rm dig}\delta S+o(S),
\qquad
\kappa_{\rm dig}=0.767009998554660\ldots.}
\tag{6.1}

因此 fixed `v_2` 时，所有可能 `b_1` 的最粗整数 count为

\[
10^{\kappa_{\rm dig}\delta S+o(S)}.
\]

对每个 `(v_2,b_1)`，本文 denominator multiplicity为 `10^{o(S)}`。另一方面 existing gap/pairmax/`U x v_2` numerator reconstruction证明：

\[
\boxed{
N_{\rm num}
\mid\text{fixed denominator/S-unit data}
=10^{o(S)}
\qquad
(\delta<\delta_{UV}),}
\]

其中

\[
\boxed{
\delta_{UV}=0.238062349248111\ldots.}
\]

而

\[
\delta_{UV}<\delta_q^{\sharp}.
\]

所以 fixed-`v_2` 的完整 Exact-Lift candidate count现在可以安全扩宽到 numerator 自身的 barrier：

\[
\boxed{
N_{\rm full}
\bigm|v_2
\le
10^{\kappa_{\rm dig}\delta S+o(S)}
\qquad
(\delta<0.238062349248111\ldots).}
\tag{Fixed-v2-full-to-UV}

旧 `qZ` product-lock threshold不再限制这条 fixed-core full-fiber conclusion。

---

## 7. 与 common-scale ray 的关系

common-scale theorem已经证明整个 one-channel neighborhood中，fixed phase/factor split的 denominator data只沿

\[
(b_1,b_2,b_3,q,\gamma)
=(\ell\bar b_1,\ell\bar b_2,\ell\bar b_3,
\ell\bar q,\ell^2\bar\gamma)
\]

移动。

本文的 direct `q` residue line与这个 common scale在 fixed primitive phase上是 homogeneous compatible的；不能把同一个 modulo `v_2` relation再次计作独立 height payer。本文真正的新作用是 **reconstruction order**：先由 `(v_2,b_1)` 的 divisor choices恢复 `V` 和 S-unit phase，再在 `q<v_2` 后把 source quotient从 residue class升级成 ordinary integer。

---

## 8. 状态与下一核心

当前 one-channel denominator reconstruction链已经达到：

- entire `delta<=1/2`：common-scale ray；
- entire `delta<=1/2`：fixed `(H,T,V)` phase uniqueness；
- `delta<0.460744281587979...`：fixed `(v_2,b_1)` denominator/S-unit fiber `10^{o(S)}`；
- `delta<0.238062349248111...`：fixed `v_2` full candidate fiber只有 short-head count `10^{kappa_dig delta S+o(S)}`。

因此 near-frontier positive-linear residual可以进一步集中为 **moving long core `v_2` 本身**；fixed long core后几乎全部其它 data都已降为 short-head / subexponential reconstruction。

这仍然没有给出 `v_2` 的 global movement bound或 strict slope gap。下一步必须让 `v_2` / `V` 与一个 independent decimal or numerator condition发生真正不相容，而不能继续重复使用 denominator concat与 S-unit等式的不同重写。

---

## 9. verification scope

配套机械审计：

```bash
uv run python scripts/exact-lift/double-deficit/research-checks/tail/check_dd_corrected_source_quotient_lock_sharp.py
```

脚本检查：

- `v2/q` shared-defect substitution的 symbolic cancellation；
- `eta` 与 `v2-over-q-full` 所有 correction coefficients的正性；
- threshold `delta_q^sharp=2U_*/3` 与 `delta_UV`、one-channel `1/2` 的数值顺序；
- toy exact data中 `q<v_2` 后 least-residue source lock。

有限 checks只核对 algebra/constants；渐近 theorem来自正文引用的 corrected inequalities。

---

## 10. 状态摘要

- **已严格完成：** `v2-over-q-full` 与 `v2-over-q`。
- **已严格完成：** direct `q-residue-lock` for `delta<0.460744281587979...`。
- **denominator reconstruction sharpen：** fixed `(v_2,b_1)` fiber在该范围内只有 `10^{o(S)}`。
- **full-candidate sharpen：** fixed-`v_2` count `10^{kappa_dig delta S+o(S)}` 扩到 `delta<delta_UV=0.238062349248111...`。
- **仍待证：** moving `v_2/V` 的 global elimination；explicit strict slope gap；DD emptiness；更低 post-tail / non-canonical dominant states 的统一 simultaneous height bound。

# DD corrected terminal 的 sharp `U v_2` period 与 numerator collapse

> 日期：2026-09-06
>
> 依赖：[`dd-corrected-denominator-product-lock-sharp-2026-09-06.md`](dd-corrected-denominator-product-lock-sharp-2026-09-06.md)、[`dd-corrected-common-scale-ray-sharp-2026-09-06.md`](dd-corrected-common-scale-ray-sharp-2026-09-06.md)、[`dd-corrected-carry-u-pairmax-crt-2026-08-22.md`](dd-corrected-carry-u-pairmax-crt-2026-08-22.md)、[`dd-corrected-pairmax-short-suffix-reader-2026-08-22.md`](dd-corrected-pairmax-short-suffix-reader-2026-08-22.md)、[`dd-corrected-gap-fiber-pairmax-rational-reconstruction-2026-08-22.md`](dd-corrected-gap-fiber-pairmax-rational-reconstruction-2026-08-22.md)。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` quantitative one-channel neighborhood）。**
>
> 本文把 2026-09-06 shared-defect sharpen 反馈到 numerator side。旧 `carry-U × pair-max` theorem 已严格给 exact transverse period
> \[
> M_{UV}=Uv_2,
> \qquad (U,v_2)=1,
> \]
> 但旧联合高度只得到
> \[
> \frac{\log(Uv_2)}S\ge 1+U_*-(2+3\log_{10}2)\delta-o(1),
> \]
> 从而 uniqueness threshold 为 `0.238062...`。
>
> 使用新的 `m_1-sharp + G_2-via-m_1` ledger，可把同一 period 的高度改进为
> \[
> \boxed{
> \frac{\log_{10}(Uv_2)}S
> \ge 1+U_*-\frac32\delta-o(1).}
> \]
> 因而 fixed `(R_0,g_0,a_2)` fiber 的 `A_12` uniqueness 扩大到
> \[
> \boxed{
> \delta<\delta_{UV}^{\sharp}
> :=\frac{2U_*}{3}
> =0.460744281587979\ldots.}
> \]
>
> 同时，2026-09-06 已证明
> \[
> \log v_2/S\ge1-\delta-o(1).
> \]
> 这把旧 short-suffix 与 gap-fiber 两个阈值分别从 `0.322366...`、`0.299845...` 扩展到整个 fixed `delta<1/2` one-channel neighborhood。最终：
> \[
> \boxed{
> N_{\rm num}(S;\delta)=10^{o(S)}
> \qquad
> (\delta<0.460744281587979\ldots)
> }
> \]
> 对 fixed denominator/S-unit data 成立。
>
> 这仍不是 DD emptiness；它把 canonical terminal 的正线性 numerator freedom在一个远宽于旧 `0.238...` 的 neighborhood 内完全消去，剩余瓶颈进一步集中到 denominator/S-unit primitive phase。

---

## 1. constants 与现有 exact periods

令

\[
a:=\log_{10}2,
\qquad b:=1-a,
\]

\[
A:=\frac{2(1+2a)}3,
\qquad
\lambda:=\frac{2+a}{1+2a},
\]

\[
U_*:=0.691116422381969\ldots,
\qquad
z_*:=1-U_*=0.308883577618031\ldots.
\]

固定

\[
\delta:=c_*-\frac nS,
\qquad
\mu:=M_*-\frac mS.
\]

`dd-corrected-carry-u-pairmax-crt-2026-08-22.md` 已严格证明：固定 denominator/S-unit data 与 `(R_0,g_0,a_2)` 后，`A_12` 同时满足

\[
A_{12}\equiv\rho_U\pmod U,
\qquad
A_{12}\equiv\rho_V\pmod{v_2},
\]

并且

\[
\boxed{(U,v_2)=1.}
\]

所以 exact combined period 为

\[
\boxed{M_{UV}=Uv_2.}
\tag{1.1}
\]

另一方面 `d_3`-dominant digit simplex 给

\[
\boxed{0<A_{12}<10^{S+2}.}
\tag{1.2}
\]

因此只要能够证明

\[
Uv_2>10^{S+2},
\]

fixed fiber 中 `A_12` 就至多一个。

---

## 2. `Uv_2` 的未粗化 shared-defect lower

`dd-corrected-common-scale-ray-sharp-2026-09-06.md` 已记录

\[
\boxed{
\frac{\log U}{S}-U_*
=
\frac{2b}{3}\mu
-aG_2
-\frac{2b}{3}Q_5
-\frac b3G_5
-\frac b3N_5
-R+o(1),}
\tag{2.1}
\]

以及

\[
\boxed{
\frac{\log V}{S}
=1-aG_2-bG_5-R+o(1).}
\tag{2.2}
\]

因为

\[
V=v_1v_2,
\qquad
v_1\mid b_1,
\qquad
b_1<10^{m_1},
\]

有

\[
\boxed{
\frac{\log v_2}{S}
\ge
\frac{\log V}{S}-\frac{m_1}{S}-o(1).}
\tag{2.3}
\]

同一 sharp ledger 还给

\[
\boxed{
\begin{aligned}
\frac{m_1}{S}
\le{}&\frac\delta2
-\left(1-\frac b3\right)\mu
-\frac b3Q_5
+\frac b3G_5\\
&-\frac b6N_5
+\frac R2+o(1),
\end{aligned}}
\tag{m1-sharp}
\]

以及

\[
\boxed{
aG_2\le\frac{m_1}{S}+aQ_2+o(1).}
\tag{G2-via-m1}
\]

由 `(2.1)--(2.3)`：

\[
\frac{\log(Uv_2)}S-(1+U_*)
\ge
\left(\frac{\log U}{S}-U_*\right)
+\left(\frac{\log V}{S}-1\right)
-\frac{m_1}{S}-o(1).
\tag{2.4}
\]

第一次代入 `(m1-sharp)`，再用 `(G2-via-m1)` 处理式中 `-2aG_2`，并第二次代入同一个 `(m1-sharp)`，精确整理得到

\[
\boxed{
\begin{aligned}
\frac{\log(Uv_2)}S-(1+U_*)
\ge{}&-\frac32\delta
+\left(3-\frac b3\right)\mu
-2aQ_2\\
&+\frac b3Q_5
-\frac{7b}{3}G_5
+\frac b6N_5
-\frac72R-o(1).
\end{aligned}}
\tag{Uv2-prebudget}
\]

这一步正是旧 `carry-U × pair-max` theorem 中缺失的 sharper reuse：旧证明使用了已经粗化的 `G_2` upper，因此让 `G_5,R` 再次支付了一整份额外 defect。

---

## 3. exact `mu` budget 后所有 correction 都非负

继续使用现行 exact normalized identity

\[
\boxed{
A\mu
=\sigma_S
+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)
+2R+o(1).}
\tag{Mu-budget}
\]

定义

\[
\boxed{
\eta:=\frac{3-b/3}{A}
=\frac{8+a}{2(1+2a)}
=2.590736314681693\ldots.}
\tag{3.1}
\]

将 `(Mu-budget)` 代入 `(Uv2-prebudget)`：

\[
\boxed{
\begin{aligned}
\frac{\log(Uv_2)}S
\ge{}&1+U_*-\frac32\delta
+\eta\sigma_S\\
&+2a(\eta-1)Q_2
+a\eta N_2\\
&+\frac{b(2\eta+1)}3Q_5
+\frac{b(4\eta-7)}3G_5\\
&+\frac{b(2\eta+1)}6N_5
+\left(2\eta-\frac72\right)R
-o(1).
\end{aligned}}
\tag{Uv2-sharp-full}
\]

因为

\[
\eta>\frac74,
\]

所有显示 correction coefficients 都严格为正。因此得到 universal lower：

\[
\boxed{
\frac{\log_{10}(Uv_2)}S
\ge1+U_*-\frac32\delta-o(1).}
\tag{Uv2-sharp}
\]

这与 2026-09-06 direct source-quotient lock 中出现的 `3/2` loss 来自同一个 shared-defect cancellation，但这里作用于不同的 exact period `Uv_2`。

---

## 4. `A_12` uniqueness threshold 扩展到 `0.460744...`

由 `(1.2)` 与 `(Uv2-sharp)`，若

\[
U_*-\frac32\delta>0,
\]

则 sufficiently large `S` 上

\[
Uv_2>10^{S+2}.
\]

定义

\[
\boxed{
\delta_{UV}^{\sharp}
:=\frac{2U_*}{3}
=0.460744281587979\ldots.}
\tag{4.1}
\]

于是

\[
\boxed{
\delta<\delta_{UV}^{\sharp}
\Longrightarrow
\#\{A_{12}\mid R_0,g_0,a_2,\text{fixed denominator/S-unit}\}
\le1.}
\tag{A12-sharp-unique}
\]

carry 再唯一恢复 `a_3`；固定 `(n_2,a_2)` 后 `A_12` 也唯一恢复 `a_1`。

旧 threshold

\[
0.238062349248111\ldots
\]

因此被严格替换为

\[
0.460744281587979\ldots.
\]

---

## 5. short suffix 在整个 one-channel neighborhood 内唯一

2026-09-06 sharp one-channel lower 为

\[
\boxed{
\frac{\log v_2}{S}\ge1-\delta-o(1).}
\tag{5.1}
\]

而 digit polarization 给

\[
\boxed{
\frac{n_2}{S}
\le\kappa_{\rm dig}\delta+o(1),
\qquad
\kappa_{\rm dig}:=\frac{2+a}{3}
=0.767009998554660\ldots.}
\tag{5.2}
\]

pair-max short-suffix theorem 已证明 fixed orientation `Omega` 下

\[
a_2\equiv\rho_{2,\Omega}\pmod{v_2}.
\]

若

\[
1-\delta>\kappa_{\rm dig}\delta,
\]

则 `v_2>10^{n_2}>a_2`，故每个 orientation fiber至多一个 `a_2`。

对应 threshold 为

\[
\boxed{
\delta<\delta_{a_2}^{\sharp}
:=\frac1{1+\kappa_{\rm dig}}
=0.565927754125872\ldots.}
\tag{5.3}
\]

现行 quantitative one-channel theorem 只使用 `delta<=1/2`。因此在它的整个严格内部 `delta<1/2`：

\[
\boxed{
\#\{a_2\mid\Omega,\text{fixed denominator/S-unit}\}\le1.}
\tag{a2-global-one-channel}
\]

orientation 数量仍只有

\[
2^{\omega(v_2)}=10^{o(S)}.
\]

---

## 6. gap fraction 在整个 `delta<1/2` one-channel neighborhood 内唯一

已有 gap rational reconstruction 对 fixed denominator/S-unit、orientation `Omega` 与 `a_2` 给

\[
\boxed{
v_2\mid
\Delta_{\rm gap}
:=R_0g_0'-R_0'g_0,}
\tag{6.1}
\]

且若两个 reduced fractions不同，则

\[
\boxed{
0<|\Delta_{\rm gap}|
\le10^{\delta S+o(S)}.}
\tag{6.2}
\]

利用新的 `(5.1)`，只要

\[
1-\delta>\delta,
\]

就有 sufficiently large `S`：

\[
v_2>|\Delta_{\rm gap}|,
\]

与 `(6.1)` 对非零 determinant 的整除矛盾。

所以

\[
\boxed{
\delta<\frac12
\Longrightarrow
\#\{(R_0,g_0)\mid\Omega,a_2,\text{fixed denominator/S-unit}\}
\le1.}
\tag{Gap-global-one-channel}
\]

旧 gap threshold

\[
0.299845580176277\ldots
\]

因此不再是当前 sharp one-channel proof tree 的有效 barrier。

---

## 7. full fixed-denominator numerator collapse

固定 denominator/S-unit data。对任意 fixed

\[
\delta<\delta_{UV}^{\sharp}
=0.460744281587979\ldots
<\frac12,
\]

依次有：

1. Gaussian orientation vectors 总数 `10^{o(S)}`；
2. 每个 orientation 下 `a_2` 至多一个，由 §5；
3. 每个 `(Omega,a_2)` 下 reduced gap fraction `(R_0,g_0)` 至多一个，由 §6；
4. 每个 `(R_0,g_0,a_2)` 下 `A_12` 至多一个，由 §4；
5. carry 唯一恢复 `a_3`，随后恢复 `a_1`。

因此：

\[
\boxed{
N_{\rm num}(S;\delta)
=10^{o(S)}
\qquad
\left(\delta<0.460744281587979\ldots\right)
}
\tag{Numerator-collapse-sharp}
\]

对 fixed denominator/S-unit data 成立。

这把旧 `Numerator-subexponential` 的范围

\[
\delta<0.238062349248111\ldots
\]

几乎扩大一倍。

---

## 8. source-square × pair-max 的同步 sharpen

虽然 §7 已由 `Uv_2` 给出更宽 numerator collapse，完整 source-square period也获得一个独立 consistency sharpen。

已有

\[
\frac{\log q_Q}{S}
\ge z_*-\delta-o(1),
\]

以及 `(5.1)`：

\[
\frac{\log v_2}{S}\ge1-\delta-o(1),
\qquad(q_Q,v_2)=1.
\]

故

\[
\boxed{
\frac{\log(q_Q^2v_2)}S
\ge1+2z_*-3\delta-o(1).}
\tag{8.1}
\]

其超过 `S`-height prefix window 的 threshold 为

\[
\boxed{
\delta<\delta_{QV}^{\sharp}
:=\frac{2z_*}{3}
=0.205922385078687\ldots.}
\tag{8.2}
\]

旧 source-square threshold `0.142505...` 因此同步升级，但它仍被更强的 `Uv_2` period覆盖。

---

## 9. 对 DD terminal bottleneck 的更新

在

\[
\boxed{
\delta<0.460744281587979\ldots
}
\]

中，fixed denominator/S-unit data 后已经没有任何 positive-linear numerator freedom。

结合 2026-09-06 denominator-side results：

- common-scale ray 在整个 `delta<=1/2` one-channel neighborhood 成立；
- fixed phase/factor split 后 denominator shape 唯一到 common scale；
- S-unit Euclidean lock 把 `(U,Z)` 读成单个 moving remainder `V` 的函数；
- direct source quotient lock 在 `delta<0.460744...` 中给 fixed `(v_2,b_1)` 的 `q` least-residue reconstruction；
- 本文把 numerator side也推到同一个 `0.460744...` barrier。

因此当前 corrected canonical terminal 的正线性 residual 可以更准确地概括成：

\[
\boxed{
\text{scale-quotiented moving S-unit remainder }V
\quad+\quad
\text{homogeneous common denominator scale }\ell.
}
\]

其中 `ell` 已不属于 projective shape；真正需要产生新不存在性输入的是 moving `V` / Farey-S-unit primitive phase。

本文没有证明该 phase不存在，也没有覆盖更低 post-tail / non-canonical dominant states。因此不宣称 DD 为空或已有 strict slope gap。

---

## 10. verification scope

配套机械审计：

```bash
uv run python scripts/exact-lift/double-deficit/research-checks/tail/check_dd_corrected_numerator_collapse_sharp.py
```

脚本检查：

- `(Uv2-prebudget)` 的 symbolic cancellation；
- `(Mu-budget)` 后 `Uv2-sharp-full` 的全部 correction coefficients为正；
- `delta_UV^sharp=2U_*/3`；
- `delta_a2^sharp=1/(1+kappa_dig)>1/2`；
- gap threshold sharpen为 `delta<1/2`；
- source-square × pair-max threshold `2z_*/3`。

机械检查只验证 algebra/constants；无界渐近 theorem 仍由正文引用的 exact CRT 与 corrected height inequalities承担。

---

## 11. 状态摘要

- **已严格完成：** `Uv2-sharp-full` 与 universal `Uv2-sharp`。
- **threshold sharpen：** `A_12` fixed-fiber uniqueness 从 `0.238062...` 扩到 `0.460744...`。
- **threshold sharpen：** short suffix `a_2` uniqueness 覆盖整个现行 `delta<1/2` one-channel neighborhood。
- **threshold sharpen：** gap-fraction uniqueness 覆盖整个现行 `delta<1/2` one-channel neighborhood。
- **full consequence：** fixed denominator/S-unit numerator family 在 `delta<0.460744281587979...` 中只有 `10^{o(S)}` candidates。
- **secondary sharpen：** `q_Q^2v_2` source/pairmax threshold 从 `0.142505...` 升到 `0.205922...`。
- **仍待证：** moving `V` / Farey-S-unit primitive phase exclusion；explicit strict slope gap；DD emptiness；post-tail / non-canonical dominant states 的统一控制。

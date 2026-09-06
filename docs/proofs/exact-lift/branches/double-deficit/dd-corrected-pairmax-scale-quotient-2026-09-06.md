# DD corrected terminal 的 pair-max-supported scale quotient 与 exact projective polarization

> 日期：2026-09-06
>
> 依赖：[`dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md`](dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md)、[`dd-corrected-denominator-product-lock-sharp-2026-09-06.md`](dd-corrected-denominator-product-lock-sharp-2026-09-06.md)、[`dd-corrected-common-scale-ray-sharp-2026-09-06.md`](dd-corrected-common-scale-ray-sharp-2026-09-06.md)、[`dd-corrected-numerator-collapse-sharp-2026-09-06.md`](dd-corrected-numerator-collapse-sharp-2026-09-06.md)。
>
> **严格状态：已严格完成（整个 corrected canonical `t_2=1` quantitative one-channel neighborhood；现行输入固定 `delta<=1/2`）。**
>
> quantitative pair-max prime `p^h||v_2` 上旧 theorem 一直保留一个 low denominator baseline `r`：
> \[
> v_p(b_1)=v_p(q)=r,
> \qquad
> v_p(b_2)=v_p(b_3)=r+h,
> \qquad
> v_p(\gamma)=2r.
> \]
> 本文证明这份 `r` 恰好是一份真实 common denominator scale，而不是 moving pair-max geometry 的一部分。把所有 `v_2`-supported baseline 聚合成
> \[
> \boxed{
> \ell_V:=\prod_{p^h\Vert v_2}p^{v_p(q)},}
> \]
> 并定义
> \[
> q_V:=q/\ell_V,
> \qquad
> b_i^{(V)}:=b_i/\ell_V,
> \qquad
> \gamma_V:=\gamma/\ell_V^2,
> \]
> 则：
> \[
> \boxed{(q_V,v_2)=(b_1^{(V)},v_2)=(\gamma_V,v_2)=1,}
> \]
> \[
> \boxed{v_2\mid b_2^{(V)},b_3^{(V)},}
> \]
> 且每个 `p^h||v_2` 上 denominator pattern 精确变成 `(0,h,h)`。
>
> 更重要的是，shared-defect digit/source formulas 给
> \[
> \boxed{
> \frac{\log_{10}q_V}{S}
> \ge z_*-\frac\delta2-o(1).}
> \]
> 因此 `q_V` 在整个 `delta<=1/2` one-channel neighborhood 中仍保持正线性高度。
>
> uniform scaling不改变 integer-sphere ghost coordinates；所以 quantitative `v_2` 本身满足 exact projective polarization
> \[
> \boxed{v_2\mid y_1,H_{\rm sph},}
> \qquad
> \boxed{(v_2,Z_0)=1,}
> \qquad
> \boxed{(v_2,y_1^2+y_2^2)=1.}
> \]
> 最后，scale-stripped denominator concat
> \[
> Uq_V=b_1^{(V)}10^{m_2}+b_2^{(V)}
> \]
> 与 `v_2|b_2^{(V)}` 给
> \[
> b_1^{(V)}\equiv Uq_V10^{-m_2}\pmod{v_2}.
> \]
> sharp `v_2` lower 与 short-head digit bound保证整个现行 one-channel 内 `0<b_1^{(V)}<v_2`，故
> \[
> \boxed{
> b_1^{(V)}=[Uq_V10^{-m_2}]_{v_2}.}
> \]
> 随后 `b_2^{(V)}` 与 `b_3^{(V)}=BVq_V` exact reconstruction。于是 fixed `(U,V,q_V,v_2)` 后，pair-max-supported scale quotient 的完整 denominator triple至多一个。

---

## 1. local pair-max baseline 本来就是 common scale

固定

\[
p^h\Vert v_2.
\]

`dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md` 已严格证明存在

\[
r:=v_p(b_1)\ge0
\]

使

\[
\boxed{
v_p(b_1)=r,}
\qquad
\boxed{
v_p(b_2)=v_p(b_3)=r+h,}
\tag{1.1}
\]

并且

\[
\boxed{v_p(q)=r,}
\tag{1.2}
\]

\[
\boxed{v_p(\gamma)=2r.}
\tag{1.3}
\]

同时 `v_p(V)=h`，所以 `p` 不进入 complementary factor `v_1=V/v_2`。

因此 `p^r` 同时整除

\[
b_1,b_2,b_3,q,
\]

而其平方 `p^{2r}` 整除 `gamma`。这正是 common-scale ray

\[
(b_1,b_2,b_3,q,\gamma)
\mapsto
(\ell b_1,\ell b_2,\ell b_3,\ell q,\ell^2\gamma)
\]

在该 prime 上的 valuation signature。

不同 `p^h||v_2` 互素，故可聚合定义

\[
\boxed{
\ell_V:=\prod_{p^h\Vert v_2}p^{r_p},
\qquad r_p:=v_p(q).}
\tag{1.4}
\]

由 `(1.1)--(1.3)`：

\[
\boxed{
\ell_V\mid(b_1,b_2,b_3,q),
\qquad
\ell_V^2\mid\gamma.}
\tag{1.5}
\]

---

## 2. canonical pair-max scale quotient

定义整数

\[
\boxed{
q_V:=q/\ell_V,}
\]

\[
\boxed{
b_i^{(V)}:=b_i/\ell_V,}
\qquad i=1,2,3,
\]

\[
\boxed{
\gamma_V:=\gamma/\ell_V^2.}
\tag{2.1}
\]

对任意 `p^h||v_2`，由 §1：

\[
\boxed{
v_p(q_V)=0,}
\]

\[
\boxed{
v_p(b_1^{(V)})=0,}
\]

\[
\boxed{
v_p(b_2^{(V)})=v_p(b_3^{(V)})=h,}
\]

\[
\boxed{
v_p(\gamma_V)=0.}
\tag{2.2}
\]

所以全局得到

\[
\boxed{(q_V,v_2)=1,}
\tag{2.3}
\]

\[
\boxed{(b_1^{(V)},v_2)=1,}
\tag{2.4}
\]

\[
\boxed{(\gamma_V,v_2)=1,}
\tag{2.5}
\]

\[
\boxed{v_2\mid b_2^{(V)},b_3^{(V)}.}
\tag{2.6}
\]

这把 frontier 中常用的 clean main-core pattern `(0,h,h)` 提升成整个 quantitative one-channel 的 **exact full-`v_2` pattern**；不需要删除 `10^{o(S)}` exceptional core。

---

## 3. stripping 不改变 ghost sphere coordinates

令

\[
q_{\rm lcm}=\operatorname{lcm}(b_1,b_2,b_3).
\]

因为 `ell_V` 同时整除三个 denominator blocks：

\[
\operatorname{lcm}(b_1^{(V)},b_2^{(V)},b_3^{(V)})
=\frac{q_{\rm lcm}}{\ell_V}.
\tag{3.1}
\]

原 ghost coordinates 为

\[
y_i=a_i\frac{q_{\rm lcm}}{b_i}.
\]

scale-stripped blocks给

\[
a_i\frac{q_{\rm lcm}/\ell_V}{b_i/\ell_V}
=a_i\frac{q_{\rm lcm}}{b_i}
=y_i.
\]

因此

\[
\boxed{y_i^{(V)}=y_i,}
\tag{Ghost-invariant}
\]

以及 sphere radius `H_sph` 也不变。

原 reducedness同时保持：若 `p|ell_V`，则 `p|b_i`；由 `(a_i,b_i)=1` 可知 `p∤a_i`。所以 `(a_i,b_i^{(V)})=1`。

这里并不宣称 `b_i^{(V)}` 仍具有原 `m_i` 位数；它是保留原 decimal weights 的 padded scale quotient，正如 common-scale-ray theorem 的 homogeneity解释。

---

## 4. full `v_2` 的 exact projective polarization

固定 `p^h||v_2`。由 `(2.2)` 与 reducedness：

\[
y_1=a_1\frac{q_{\rm lcm}/\ell_V}{b_1^{(V)}}
\]

至少含 `p^h`，而

\[
y_2,y_3
\]

都是 `p`-units。因此

\[
\boxed{p^h\mid y_1,}
\tag{4.1}
\]

\[
\boxed{p\nmid y_2y_3.}
\tag{4.2}
\]

pair-max orientation给

\[
p^{2h}\mid y_2^2+y_3^2.
\tag{4.3}
\]

sphere equation

\[
H_{\rm sph}^2=y_1^2+y_2^2+y_3^2
\]

于是

\[
p^{2h}\mid H_{\rm sph}^2,
\]

故

\[
\boxed{p^h\mid H_{\rm sph}.}
\tag{4.4}
\]

因为 `y_3` 是 p-unit：

\[
H_{\rm sph}+y_3\equiv y_3\not\equiv0\pmod p.
\]

primitive stereographic denominator exact formula为

\[
Z_0=\frac{H_{\rm sph}+y_3}
{((y_1,y_2),H_{\rm sph}+y_3)}.
\]

因此

\[
\boxed{p\nmid Z_0.}
\tag{4.5}
\]

同时

\[
y_1^2+y_2^2\equiv y_2^2\not\equiv0\pmod p,
\]

所以

\[
\boxed{p\nmid y_1^2+y_2^2.}
\tag{4.6}
\]

逐 prime 聚合：

\[
\boxed{v_2\mid y_1,H_{\rm sph},}
\tag{Projective-polarization-A}
\]

\[
\boxed{(v_2,Z_0)=1,}
\tag{Projective-polarization-B}
\]

\[
\boxed{(v_2,y_1^2+y_2^2)=1.}
\tag{Projective-polarization-C}
\]

所以 moving `v_2` 的 Gaussian orientation只能真正存在于 pair-max line `y_2+i y_3`；它不会传播到 primitive stereographic denominator或 numerator norm。

---

## 5. `q_V` 的 sharp positive-linear lower

由 `(1.5)`：

\[
\ell_V\mid b_1,
\]

故

\[
\boxed{\ell_V\le b_1<10^{m_1}.}
\tag{5.1}
\]

2026-09-06 sharp product-lock ledger给未粗化 source quotient identity

\[
\boxed{
\begin{aligned}
\frac{\log q}{S}-z_*
={}&-\frac{2b}{3}\mu
+aG_2
+\frac{2b}{3}Q_5\\
&+\frac b3G_5
+\frac b3N_5+R+o(1),
\end{aligned}}
\tag{5.2}
\]

以及 short-head upper

\[
\boxed{
\begin{aligned}
\frac{m_1}{S}
\le{}&\frac\delta2
-\left(1-\frac b3\right)\mu
-\frac b3Q_5
+\frac b3G_5\\
&-\frac b6N_5
+\frac R2+o(1).
\end{aligned}}
\tag{5.3}
\]

由 `q_V=q/ell_V` 与 `(5.1)`：

\[
\frac{\log q_V}{S}
\ge\frac{\log q}{S}-\frac{m_1}{S}-o(1).
\]

将 `(5.2),(5.3)` 相减，并使用 `b=1-a`：

\[
\boxed{
\begin{aligned}
\frac{\log q_V}{S}-z_*
\ge{}&-\frac\delta2
+a\mu+aG_2+bQ_5\\
&+\frac b2N_5+\frac R2-o(1).
\end{aligned}}
\tag{5.4}
\]

所有 correction 非负，因此

\[
\boxed{
\frac{\log_{10}q_V}{S}
\ge z_*-\frac\delta2-o(1).}
\tag{qV-sharp}
\]

在现行 `delta<=1/2` one-channel neighborhood 中：

\[
z_*-\frac14
=0.058883577618031\ldots>0.
\]

所以 `q_V` 在整个作用域内仍保持 exponential height；pair-max-supported scale stripping不会把 source quotient退化成 subexponential object。

---

## 6. scale-stripped denominator concat

因为 `ell_V|b_1,b_2,q`，从

\[
Uq=b_1 10^{m_2}+b_2
\]

整除 `ell_V` 得 exact padded-width identity

\[
\boxed{
Uq_V=b_1^{(V)}10^{m_2}+b_2^{(V)}.}
\tag{6.1}

由 `(2.6)`：

\[
b_2^{(V)}\equiv0\pmod{v_2}.
\]

且 `(U,v_2)=1`、`(10,v_2)=1`。所以

\[
\boxed{
b_1^{(V)}
\equiv Uq_V10^{-m_2}\pmod{v_2}.}
\tag{6.2}

### short head 比 `v_2` 小

显然

\[
0<b_1^{(V)}\le b_1<10^{m_1}.
\]

旧 digit polarization已经给

\[
\frac{m_1}{S}
\le\kappa_{\rm dig}\delta+o(1),
\qquad
\kappa_{\rm dig}=0.767009998554660\ldots,
\]

而 sharp one-channel lower为

\[
\frac{\log v_2}{S}\ge1-\delta-o(1).
\]

只要

\[
1-\delta>\kappa_{\rm dig}\delta,
\]

就有 `b_1^(V)<v_2`。阈值为

\[
\frac1{1+\kappa_{\rm dig}}
=0.565927754125872\ldots>rac12.
\]

故整个现行 fixed `delta<=1/2` one-channel neighborhood（在 endpoint 取 sufficiently large strict margin时可按 `delta<1/2` 使用）中：

\[
\boxed{0<b_1^{(V)}<v_2.}
\tag{6.3}

结合 `(6.2)`：

\[
\boxed{
b_1^{(V)}
=[Uq_V10^{-m_2}]_{v_2}.}
\tag{Short-head-least-residue}

因为 `(b_1^{(V)},v_2)=1`，该 least residue非零。

随后 `(6.1)` exact 恢复

\[
\boxed{
b_2^{(V)}
=Uq_V-b_1^{(V)}10^{m_2}.}
\tag{6.4}

第三 denominator factorization

\[
b_3=BVq
\]

整除 `ell_V` 给

\[
\boxed{b_3^{(V)}=BVq_V.}
\tag{6.5}

因此：

\[
\boxed{
\text{fixed }(U,V,q_V,v_2,m_2,B)
\Longrightarrow
(b_1^{(V)},b_2^{(V)},b_3^{(V)})
\text{ 至多一个}.}
\tag{Scale-stripped-den-reconstruction}

---

## 7. 与 full common-scale ray 的关系

`ell_V` 只剥离 support 在 `v_2` primes 上的 forced low baseline；它未必等于 full common-scale parameter `ell`。但 §1 已证明它本身就是一个 exact common-scale divisor：

\[
(b_1,b_2,b_3,q,\gamma)
=
(\ell_V b_1^{(V)},
 \ell_V b_2^{(V)},
 \ell_V b_3^{(V)},
 \ell_V q_V,
 \ell_V^2\gamma_V).
\]

full common-scale-ray theorem进一步说明，在 fixed S-unit phase / factor split 中其它 movable cofactor scale也只能继续沿同一个 homogeneous direction发生。

因此 denominator geometry可分成：

1. `v_2`-supported forced scale `ell_V`：本文 canonical 地从 local pair-max baselines读取；
2. scale-stripped shape `(b_i^(V),q_V,gamma_V)`：在 `v_2` support上 exact clean；
3. 可能的其它 common scale：仍是 homogeneous direction，不是新的 projective shape。

---

## 8. 方法边界与下一目标

本文没有制造新的 source CRT；`q_V` 是 denominator/source coordinate，不应与 square-source reader `q_Q` 混淆。特别地，不能因为 `(q_V,v_2)=1` 就声称存在 `q_V`-period 的 numerator congruence。

真正新增的是：

\[
\boxed{
\text{整个 quantitative one-channel 的 moving pair-max support
可 exact 归一化到 clean pattern }(0,h,h),}
\]

以及

\[
\boxed{
q_V=10^{(z_*-\delta/2)S+o(S)}\text{ 级、且 }(q_V,v_2)=1.}
\]

因此后续若要攻击 moving `V`，可以安全地在 scale-stripped chart 中工作：所有 `v_2` primes 都没有 low denominator/source baseline，任何新出现的 `v_2`-deep condition 都不能再归咎于 common scale `r`。

这为 quartic/global Gaussian orientation、raw decimal shell 与 moving-`V` compatibility提供了一个更干净的正宽度输入。

本文仍不证明 strict slope gap、DD emptiness，也不覆盖 post-tail / non-canonical dominant states。

---

## 9. verification scope

配套机械审计：

```bash
uv run python scripts/exact-lift/double-deficit/research-checks/tail/check_dd_corrected_pairmax_scale_quotient.py
```

脚本检查：

- local `(r,r+h,r+h)` strip 到 `(0,h,h)`；
- `q_V` / `gamma_V` 在 `v_2` support上成为 units；
- `q_V` sharp lower 的 symbolic cancellation；
- `1/(1+kappa_dig)>1/2`，故 short-head least-residue lock覆盖整个 strict one-channel interior。

有限 checks只核对代数与常数；渐近 theorem由正文引用的 corrected valuation/height inputs承担。

---

## 10. 状态摘要

- **已严格完成：** canonical `v_2`-supported scale `ell_V`。
- **已严格完成：** exact scale quotient `(q_V,b_i^(V),gamma_V)` 与 clean `(0,h,h)` pair-max pattern。
- **已严格完成：** full-`v_2` projective polarization `(v_2,Z_0)=1`、`(v_2,y_1^2+y_2^2)=1`、`v_2|y_1,H_sph`。
- **已严格完成：** `q_V` positive-linear lower `z_*-delta/2`。
- **已严格完成：** entire one-channel strict interior 的 stripped short-head least-residue reconstruction。
- **仍待证：** 一个真正独立于 existing sphere/source identities 的 global `v_2` orientation / decimal-shell incompatibility；strict slope gap；DD emptiness；post-tail / non-canonical closure。

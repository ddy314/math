# DD corrected one-channel 的 scale-free secondary Gaussian carrier

> 日期：2026-09-06
>
> 依赖：[`dd-corrected-gap-fiber-pairmax-rational-reconstruction-2026-08-22.md`](dd-corrected-gap-fiber-pairmax-rational-reconstruction-2026-08-22.md)、[`dd-corrected-pairmax-scale-quotient-2026-09-06.md`](dd-corrected-pairmax-scale-quotient-2026-09-06.md)、[`dd-corrected-high-funnel-quantitative-defect-2026-08-22.md`](dd-corrected-high-funnel-quantitative-defect-2026-08-22.md)、[`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)。
>
> **严格状态：已严格完成（整个现行 corrected quantitative one-channel neighborhood `delta<=1/2`）。**
>
> equality frontier 中存在 secondary Gaussian source line。本文证明其核心并非 equality-only：把 quantitative pair-max gap orientation 与 2026-09-06 的 `v_2`-supported common-scale quotient 联立，可在整个 corrected one-channel neighborhood 构造一个 exact scale-free chosen-orientation carrier：
>
> \[
> \boxed{
> \Pi_\Omega\mid
> g_0a_2v_1\,2^{m-2}q_V
> -iR_0\tau_2\,5^{2T-m},
> \qquad N(\Pi_\Omega)=v_2.
> }
> \]
>
> 其中
>
> \[
> q_V=q/\ell_V,
> \qquad
> \tau_2=\frac{b_2/\ell_V}{v_2},
> \]
>
> 且所有 `v_2` target primes 上 `q_V,v_1,tau_2,g_0,R_0,a_2` 都是 units。该 carrier 不新增 sphere-paid prime depth；它的价值是把 equality secondary orientation 正规化成 neighborhood-valid、完全剥离 pair-max common-scale baseline 的 Gaussian source coordinate。

---

## 1. quantitative pair-max gap line

固定

\[
p^h\Vert v_2.
\]

已有 pair-max orientation / gap reconstruction 给某个 Hensel root

\[
\iota_p^2\equiv-1\pmod{p^h}
\]

并严格满足

\[
\boxed{
 g_0a_2c_2
 \equiv
 2\cdot5^T\iota_pc_3R_0
 \pmod{p^h},
}
\tag{1.1}
\]

其中

\[
c_2=q_{\rm lcm}/b_2,
\qquad
c_3=q_{\rm lcm}/b_3,
\]

且

\[
\boxed{p\nmid c_2c_3g_0R_0a_2.}
\tag{1.2}
\]

---

## 2. scale quotient 把 `c_2/c_3` 精确改写成 `q_V`

由 [`dd-corrected-pairmax-scale-quotient-2026-09-06.md`](dd-corrected-pairmax-scale-quotient-2026-09-06.md)，定义 `v_2`-supported common scale

\[
\ell_V:=\prod_{p^h\Vert v_2}p^{v_p(q)},
\]

以及

\[
q_V:=q/\ell_V,
\qquad
b_i^{(V)}:=b_i/\ell_V.
\]

写

\[
\boxed{b_2^{(V)}=v_2\tau_2.}
\tag{2.1}
\]

exact third-denominator factorization给

\[
\boxed{b_3^{(V)}=BVq_V=Bv_1v_2q_V.}
\tag{2.2}
\]

另一方面

\[
c_2b_2=c_3b_3=q_{\rm lcm}.
\]

同时约去 common scale `ell_V` 与 `v_2`，得到 exact integer identity

\[
\boxed{c_2\tau_2=c_3Bv_1q_V.}
\tag{2.3}
\]

把 `(1.1)` 乘 `tau_2` 并代入 `(2.3)`：

\[
c_3g_0a_2Bv_1q_V
\equiv
2\cdot5^T\iota_pc_3R_0\tau_2
\pmod{p^h}.
\]

由 `(1.2)` 可约去 `c_3`：

\[
\boxed{
 g_0a_2Bv_1q_V
 \equiv
 2\cdot5^T\iota_pR_0\tau_2
 \pmod{p^h}.}
\tag{Scale-free-raw-p}
\]

这一步已经完全删除 target prime 的 lower baseline `r`。

---

## 3. 整个 `delta<=1/2` 中都有 `2T>m`

为了把 `(Scale-free-raw-p)` 化成 canonical secondary 形态，需要证明

\[
2T-m>0.
\]

5-resonance给

\[
\boxed{
\frac TS
=\frac{2M+2Q_5-2G_5+N_5}{3},}
\tag{3.1}
\]

所以

\[
\boxed{
\frac{2T-m}{S}
=\frac{M+4Q_5-4G_5+2N_5}{3}.}
\tag{3.2}
\]

令

\[
M_*:=\frac3A
=2.808883577618032\ldots,
\qquad
\mu:=M_*-M,
\]

其中

\[
A=\frac{2(1+2a)}3,
\qquad a=\log_{10}2.
\]

于是 `(3.2)` 的 numerator 为

\[
M_*-
\left(\mu+4G_5-4Q_5-2N_5\right).
\tag{3.3}
\]

`Mu-budget` 给

\[
A\mu
=\sigma_S+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)+2R+o(1),
\tag{3.4}
\]

而 quantitative defect 为

\[
\begin{aligned}
\delta\ge{}&
\lambda\sigma_S+2a\lambda Q_2+a\lambda N_2\\
&+\frac{2b(\lambda+1)}3Q_5
+\frac{2b(2\lambda-1)}3G_5\\
&+\frac{b(\lambda+1)}3N_5
+(2\lambda-1)R-o(1).
\end{aligned}
\tag{3.5}
\]

逐 variable 比较 `(3.3)--(3.5)` 中的 loss/cost ratio。最大值唯一由 `G_5` direction达到：

\[
\boxed{
C_T:=\frac{\lambda+1}{\lambda-1}
=5.58405934844036\ldots.}
\tag{3.6}
\]

因此

\[
\boxed{
\mu+4G_5-4Q_5-2N_5
\le C_T\delta+o(1).}
\tag{3.7}
\]

代回 `(3.2)`：

\[
\boxed{
\frac{2T-m}{S}
\ge
\frac{M_*-C_T\delta}{3}-o(1).}
\tag{Smooth-margin}
\]

数值上

\[
\boxed{
\frac{M_*}{C_T}
=0.503018217097309\ldots>rac12.}
\tag{3.8}
\]

所以对整个现行 one-channel 作用域

\[
\boxed{\delta\le\frac12,}
\]

sufficiently large `S` 上都有

\[
\boxed{2T>m.}
\tag{Secondary-smooth-positive}
\]

在最外沿 `delta=1/2` 仍有 normalized margin

\[
\frac{2T-m}{S}
\ge0.00561796779928\ldots-o(1).
\]

---

## 4. secondary normalization

canonical

\[
B=\frac{10^m}{2\cdot5^T}
=2^{m-1}5^{m-T}.
\]

`T<=m` 来自 `B` 的整数性，而 §3 给 `2T>m`。因此 `(Scale-free-raw-p)` 两边都有 common unit factor

\[
2\cdot5^{m-T}
\]

modulo `p^h`。由于 `p\nmid10`，可约去该 factor，得到

\[
\boxed{
 g_0a_2v_1\,2^{m-2}q_V
 \equiv
 \iota_pR_0\tau_2\,5^{2T-m}
 \pmod{p^h}.}
\tag{Scale-free-secondary-p}
\]

并且全部 coefficients在 `p` 上仍为 units。

---

## 5. 聚合 chosen Gaussian divisor

对所有

\[
p^h\Vert v_2
\]

固定一个 orientation vector

\[
\Omega=(\iota_p)_p.
\]

取与 `i -> iota_p` 对应的 chosen Gaussian prime power `pi_p^h`，并定义

\[
\boxed{
\Pi_\Omega:=\prod_{p^h\Vert v_2}\pi_p^h,
\qquad
N(\Pi_\Omega)=v_2.}
\tag{5.1}
\]

`(Scale-free-secondary-p)` 恰等价于

\[
\pi_p^h\mid
g_0a_2v_1\,2^{m-2}q_V
-iR_0\tau_2\,5^{2T-m}
\]

逐 prime-power成立。因此聚合得到

\[
\boxed{
\Pi_\Omega\mid
g_0a_2v_1\,2^{m-2}q_V
-iR_0\tau_2\,5^{2T-m}.}
\tag{Scale-free-secondary-Gaussian}
\]

定义 quotient

\[
\boxed{
\Delta_V
:=
\frac{
 g_0a_2v_1\,2^{m-2}q_V
-iR_0\tau_2\,5^{2T-m}
}{\Pi_\Omega}
\in\mathbf Z[i].}
\tag{5.2}
\]

这就是 corrected neighborhood 的 scale-free secondary Gaussian carrier。

---

## 6. ordinary `q_V` orientation reader

`q_V` 在所有 `v_2` target primes上为 unit。固定

\[
(v_2,\Omega,g_0,R_0,a_2,v_1,\tau_2,m,T)
\]

后，`(Scale-free-secondary-p)` 聚合成一个 fixed residue

\[
\boxed{q_V\equiv\rho_{q,\Omega}\pmod{v_2}.}
\tag{qV-orientation-residue}
\]

另一方面 `q_V<=q`。此前 direct source quotient theorem给

\[
q<v_2
\]

在

\[
\boxed{
\delta<\frac{2U_*}{3}
=0.460744281587979\ldots}
\tag{6.1}
\]

内成立。因此同一范围内：

\[
\boxed{0<q_V<v_2,}
\]

从而 `(qV-orientation-residue)` 直接升级为 ordinary least-residue recovery：

\[
\boxed{q_V=\rho_{q,\Omega}.}
\tag{qV-orientation-lock}
\]

这与 raw-prefix direct `q` lock 语义不同：后者固定 short denominator head；本文 fixed reader来自 Gaussian orientation + primitive gap/suffix/cofactor data。

---

## 7. no-double-count 与 equality secondary line

本文的 prime depth最终来自 pair-max sphere orientation；不能把 `Pi_Omega` 再作为一份独立 `v_2` height payer与已有 pair-max CRT相乘收费。

其真正新增内容是 **normalization / dependency structure**：

1. 旧 equality secondary source line具有一个 quantitative neighborhood ancestor；
2. pair-max lower baseline `r` 在 `q_V` chart 中完全消失；
3. Gaussian source coordinate可写成 neighborhood-valid exact divisor，而非 equality-only heuristic；
4. fixed orientation fiber 中 `q_V` 在 `delta<0.460744...` 可 ordinary reconstruction。

当 `delta->0` 时，`v_1,tau_2,g_0,R_0` 与其它 defect coefficients都只有 `10^{o(S)}` height，`q_V=q_c*10^{o(S)}`；因此 `(Scale-free-secondary-Gaussian)` 恢复旧 terminal secondary line的 leading geometry。本文不把这种恢复误计为新 frontier payer。

---

## 8. 当前意义

结合 full-`v_2` projective polarization：

\[
(v_2,Z_0)=1,
\qquad
(v_2,y_1^2+y_2^2)=1,
\]

说明 long core 的 chosen orientation只能通过 raw pair-max line或本文这类 scale-free source carrier被读取；它不会从 primitive stereographic geometry自动重现。

因此 corrected terminal 的 global orientation target可进一步规范为：

\[
\boxed{
(V,v_2,q_V,\Pi_\Omega,\Delta_V)
}
\]

加上由 S-unit Euclidean lock恢复的 `(U,Z)`。继续 strict-gap 攻击应研究 `Delta_V` 与 raw decimal prefix / Top-residue 的 genuinely global Archimedean compatibility，而不是继续增加同一 `p|v_2` 的 local norm/resultant。

---

## 9. 状态摘要

- **已严格完成：** scale-free raw pair-max/source congruence；
- **已严格完成：** `2T>m` 覆盖整个现行 `delta<=1/2` neighborhood；
- **已严格完成：** corrected scale-free secondary congruence；
- **已严格完成：** chosen Gaussian divisor `Pi_Omega | (...)`，`N(Pi_Omega)=v_2`；
- **已严格完成：** `delta<0.460744...` 中 fixed orientation fiber 的 ordinary `q_V` recovery；
- **不宣称：** 新 prime-depth payer、explicit strict gap、DD emptiness；
- **下一核心：** `Delta_V` 的 global Archimedean/digit-shell compatibility或 quartic/product-orientation invariant。

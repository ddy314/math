# DD corrected canonical terminal 的 global sparsity sharp extension

> 日期：2026-09-06
>
> 依赖：[`dd-corrected-terminal-denominator-sunit-entropy-2026-08-22.md`](dd-corrected-terminal-denominator-sunit-entropy-2026-08-22.md)、[`dd-corrected-common-scale-ray-sharp-2026-09-06.md`](dd-corrected-common-scale-ray-sharp-2026-09-06.md)、[`dd-corrected-numerator-collapse-sharp-2026-09-06.md`](dd-corrected-numerator-collapse-sharp-2026-09-06.md)。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` terminal neighborhood）。**
>
> 2026-08-22 的 global terminal sparsity theorem 在 fixed-denominator numerator uniqueness 处受阈值
> \[
> \delta_{UV}=0.238062349248111\ldots
> \]
> 限制。2026-09-06 的 shared-defect sharpen 已把 fixed denominator/S-unit 下的完整 numerator collapse 推到
> \[
> \boxed{
> \delta_{\rm num}^{\sharp}
> =\frac{2U_*}{3}
> =0.460744281587979\ldots.}
> \]
> 因而原有 denominator/S-unit global counting 可以无损接上新的 numerator theorem，把完整 candidate sparsity 的正宽度作用域几乎扩大一倍。

---

## 1. denominator/S-unit counting 不需要旧 numerator threshold

令

\[
a:=\log_{10}2,
\qquad
\lambda:=\frac{2+a}{1+2a}
=1.436294525872677\ldots,
\]

以及

\[
\delta':=c_*-\frac nS.
\]

固定常数 `delta_0` 并研究

\[
0\le\delta'\le\delta_0.
\]

旧 denominator/S-unit theorem 的 Farey/rough counting部分给

\[
N_{\rm den/SU}(S;\delta_0)
\le
10^{(\delta_0/\lambda)S+o(S)}.
\tag{1.1}
\]

这部分证明只使用 quantitative defect、Farey separation、rough-core/divisor assignment 与 exact denominator reconstruction；并不需要旧 numerator threshold `delta_UV`。

2026-09-06 common-scale ray sharpen还进一步把 candidate-specific denominator entropy 从

\[
\sigma_S+R
\]
压为

\[
\boxed{\sigma_S+\frac R2,}
\tag{1.2}
\]

因为 rough cofactor movement只沿 homogeneous common scale `ell`，且 `gamma=ell^2\bar\gamma`。

全局最坏 exponent仍由 `sigma_S` direction达到，所以 `(1.1)` 的 uniform coefficient `1/lambda` 不变；但 `(1.2)` 明确说明 rough `R` 不再是与 Farey slack等价昂贵的 projective coordinate。

---

## 2. fixed denominator/S-unit 的 numerator collapse 新阈值

2026-09-06 sharp numerator theorem证明 exact transverse `U × v_2` periods满足

\[
\boxed{
\frac{\log(Uv_2)}S
\ge
1+U_*-\frac32\delta'-o(1),}
\tag{2.1}
\]

其中

\[
U_*=0.691116422381969\ldots.
\]

所以当

\[
\boxed{
\delta'<\delta_{\rm num}^{\sharp}
:=\frac{2U_*}{3}
=0.460744281587979\ldots}
\tag{2.2}
\]

时，fixed denominator/S-unit data 下的完整 numerator family满足

\[
\boxed{
N_{\rm num}\le10^{o(S)}.}
\tag{2.3}
\]

同一 sharp chain 已把 short suffix 与 primitive gap fraction的旧 thresholds吸收；因此 `(2.3)` 是完整 numerator collapse，不再残留 `delta S` 级 gap entropy。

---

## 3. global terminal candidate count

固定任意

\[
\boxed{0\le\delta_0<\delta_{\rm num}^{\sharp}.}
\]

对每个 denominator/S-unit candidate，`(2.3)` 贡献至多 `10^{o(S)}` 个 numerator triples。乘上 `(1.1)`：

\[
\boxed{
N_{\rm term}(S;\delta_0)
\le
10^{(\delta_0/\lambda)S+o(S)}.}
\tag{Terminal-sparsity-sharp}
\]

数值为

\[
\boxed{
N_{\rm term}(S;\delta_0)
\le
10^{0.696236030972\,\delta_0 S+o(S)}
\qquad
(\delta_0<0.460744281587979\ldots).}
\tag{3.1}
\]

因此 2026-08-22 完整 candidate sparsity 的作用域从

\[
0.238062349248111\ldots
\]
提升到

\[
\boxed{0.460744281587979\ldots.}
\]

扩宽因子约为

\[
\boxed{1.935393\ldots.}
\]

---

## 4. equality shell

若沿一列 candidates 有

\[
\delta'\to0,
\]

则 `(Terminal-sparsity-sharp)` 恢复

\[
\boxed{N_{\rm term}(S)=10^{o(S)}}
\]

的 equality-scale sparsity。

配合 2026-09-06 的 structural reconstruction，现在这份 `10^{o(S)}` shell还具有更强解释：

- denominator projective cofactor只有一条 common-scale ray；
- fixed `(H,T,V)` 后 `(U,Z)` 唯一；
- full `v_2` 在 primitive stereographic coordinates中 exact invisible；
- fixed denominator/S-unit 后 numerator完全 subexponential；
- scale-free source `q_V` 具有 chosen Gaussian secondary carrier。

但这些仍然是 sparsity / reconstruction，而不是 deterministic digit-shell exclusion。

---

## 5. 方法边界

`(Terminal-sparsity-sharp)` 不能单独推出 strict slope gap。即使 `delta_0` 很小，右侧对 fixed positive `delta_0` 仍允许指数多个 candidates；在 `delta_0->0` 时得到 `10^{o(S)}` 也不能在没有额外 equidistribution / location theorem 的情况下推出 eventually empty。

因此安全结论仍是：

\[
\boxed{
\text{canonical terminal candidate space 在 }\delta<0.460744\ldots
\text{ 内已量化压缩到纯 Farey-scale exponent }\delta/\lambda.}
\]

下一步若要 strict gap，必须给 surviving shell 一个 deterministic Archimedean/digit-shell exclusion，或给 chosen Gaussian orientation一个 genuinely independent second parent。

---

## 6. 状态摘要

- **已严格完成：** global denominator/S-unit counting继续成立；
- **已严格完成：** common-scale ray将 candidate-specific rough entropy降为 `R/2`；
- **已严格完成：** full numerator collapse threshold提升至 `2U_*/3`；
- **新 global consequence：** full terminal sparsity bound扩展到 `delta<0.460744281587979...`；
- **不宣称：** explicit strict slope gap、DD emptiness、effective absolute height bound。

# DD corrected one-channel 的 full-`v_2` projective polarization

> 日期：2026-09-06
>
> 依赖：[`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)、[`dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md`](dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md)、[`dd-corrected-pairmax-scale-quotient-2026-09-06.md`](dd-corrected-pairmax-scale-quotient-2026-09-06.md)、[`../../global-framework.md`](../../global-framework.md) 的 canonical sphere recovery。
>
> **严格状态：已严格完成（整个 corrected quantitative one-channel neighborhood）。**
>
> 旧 frontier polarization 只在 equality ray 删除 `o(S)` exceptional denominator baseline 后证明 main pair-max core 不进入 primitive stereographic coordinates。本文观察到 quantitative one-channel 的 exact valuation pattern已经足以对整个 `v_2` 给出无 exceptional-core 版本：
>
> \[
> \boxed{v_2\mid y_1,H_{\rm sph},}
> \]
> \[
> \boxed{(v_2,H_{\rm sph}+y_3)=1,}
> \]
> \[
> \boxed{(v_2,Z_0)=1,}
> \]
> \[
> \boxed{(v_2,y_1^2+y_2^2)=1.}
> \]
>
> 所以 long pair-max core在 primitive stereographic numerator/denominator中 exact invisible；它只能保留在 pair-max line `y_2+i y_3` 的 chosen Gaussian orientation中。

---

## 1. local denominator pattern

固定

\[
p^h\Vert v_2.
\]

quantitative one-channel / pair-max theorem给

\[
\boxed{
v_p(b_1)=r,
\qquad
v_p(b_2)=v_p(b_3)=r+h.}
\tag{1.1}
\]

因为三 denominator 的最大 p-depth为 `r+h`，

\[
v_p(q_{\rm lcm})=r+h.
\tag{1.2}
\]

reducedness给 `p\nmid a_2a_3`，于是 canonical sphere coordinates

\[
y_i=a_i\frac{q_{\rm lcm}}{b_i}
\]
满足

\[
\boxed{v_p(y_1)=h+v_p(a_1)\ge h,}
\tag{1.3}
\]

\[
\boxed{v_p(y_2)=v_p(y_3)=0.}
\tag{1.4}
\]

注意这里不需要先 quotient common scale `r`；`r` 在 `q_{\rm lcm}/b_i` 中自动消失。

---

## 2. pair-max square depth强迫 `p^h\mid H_{\rm sph}`

one-channel pair-max sphere carrier给

\[
\boxed{p^{2h}\mid y_2^2+y_3^2.}
\tag{2.1}
\]

由 `(1.3)`：

\[
p^{2h}\mid y_1^2.
\]

sphere equation

\[
H_{\rm sph}^2=y_1^2+y_2^2+y_3^2
\]
因此给

\[
p^{2h}\mid H_{\rm sph}^2.
\]

所以

\[
\boxed{p^h\mid H_{\rm sph}.}
\tag{2.2}
\]

逐 prime-power 聚合：

\[
\boxed{v_2\mid y_1,H_{\rm sph}.}
\tag{2.3}
\]

---

## 3. `H_sph+y_3` 与 `v_2` exact coprime

由 `(1.4)`，`y_3` 为 p-unit；而 `(2.2)` 给 `p\mid H_{\rm sph}`。因此

\[
H_{\rm sph}+y_3\equiv y_3\not\equiv0\pmod p.
\]

故

\[
\boxed{p\nmid H_{\rm sph}+y_3.}
\tag{3.1}
\]

对全部 `p\mid v_2` 聚合：

\[
\boxed{(v_2,H_{\rm sph}+y_3)=1.}
\tag{3.2}
\]

primitive projective denominator exact formula为

\[
Z_0
=\frac{H_{\rm sph}+y_3}
{((y_1,y_2),H_{\rm sph}+y_3)}.
\]

其 numerator已经与 `v_2` 互素，所以立即有

\[
\boxed{(v_2,Z_0)=1.}
\tag{Full-v2-Z0-unit}
\]

---

## 4. primitive stereographic numerator同样看不到 `v_2`

由 `(1.3)--(1.4)`：

\[
y_1^2+y_2^2
\equiv y_2^2\not\equiv0\pmod p.
\]

所以

\[
\boxed{p\nmid y_1^2+y_2^2.}
\tag{4.1}
\]

聚合：

\[
\boxed{(v_2,y_1^2+y_2^2)=1.}
\tag{Full-v2-stereo-num-unit}
\]

若 `p=\pi\bar\pi`，则 `(4.1)` 等价于 `\pi,\bar\pi` 都不整除 Gaussian integer `y_1+i y_2`。结合 `(3.2)`，primitive stereographic coordinate

\[
z=\frac{y_1+i y_2}{H_{\rm sph}+y_3}
\]
在所有 `v_2` target primes上都是 Gaussian unit。

---

## 5. 与 pair-max orientation 的 exact polarization

另一方面 one-channel orientation恰好保留

\[
\Pi^2\mid y_2+i y_3,
\qquad N(\Pi)=v_2
\]
（逐 prime-power chosen orientation聚合）。

所以 corrected one-channel 的 long moving core具有 exact polarization：

\[
\boxed{
\begin{array}{c}
v_2\mid y_1,H_{\rm sph},\\
(v_2,H_{\rm sph}+y_3)=1,\\
(v_2,y_1^2+y_2^2)=1,\\
\Pi^2\mid y_2+i y_3,\quad N(\Pi)=v_2.
\end{array}}
\tag{Full-v2-polarization}
\]

它说明 `v_2` 的 chosen orientation不会自动传播到 primitive stereographic coordinate；任何试图获得第二个 independent `v_2` reader 的论证必须保留 raw pair-max line，或引入真正不同的 decimal/source parent family。

---

## 6. 与 scale quotient 的关系

[`dd-corrected-pairmax-scale-quotient-2026-09-06.md`](dd-corrected-pairmax-scale-quotient-2026-09-06.md) 证明 `v_2`-support 的 lower baseline `r` 正是 common scale的一部分，并可定义 scale-free source `q_V`。本文的 projective polarization甚至不依赖显式 quotient；这进一步确认 lower baseline并不是 projective/Gaussian的新 payer。

因此后续 global attack的最小 primitive state应写成

\[
\boxed{(V,v_2,q_V,\Pi)}
\]

加上由 S-unit Euclidean lock恢复的 `(U,Z)`，而不应再把 `v_2` 的 baseline `r`、`Z_0` 或 stereographic numerator当成新的独立 moving coordinates。

---

## 7. 状态摘要

- **已严格完成：** full quantitative `v_2\mid y_1,H_{\rm sph}`；
- **已严格完成：** `(v_2,H_{\rm sph}+y_3)=1`；
- **已严格完成：** `(v_2,Z_0)=1`；
- **已严格完成：** `(v_2,y_1^2+y_2^2)=1`；
- **解释：** long core仅在 pair-max Gaussian line保留 orientation，primitive stereographic geometry对其 exact transparent；
- **仍待证：** chosen `\Pi` 与 scale-free source/raw decimal prefix 的 genuinely global compatibility；explicit strict slope gap；DD emptiness。

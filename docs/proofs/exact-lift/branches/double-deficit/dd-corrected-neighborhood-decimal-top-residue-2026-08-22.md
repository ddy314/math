# DD corrected terminal neighborhood 的 decimal top-residue

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-terminal-neighborhood-geometry-2026-08-22.md`](dd-corrected-terminal-neighborhood-geometry-2026-08-22.md)、[`dd-corrected-neighborhood-gap-fiber-entropy-2026-08-22.md`](dd-corrected-neighborhood-gap-fiber-entropy-2026-08-22.md)、[`dd-corrected-carry-u-pairmax-crt-2026-08-22.md`](dd-corrected-carry-u-pairmax-crt-2026-08-22.md)、[`frontier.md`](frontier.md) 中 equality decimal remainder mechanism。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` terminal neighborhood；固定任意 `delta<3/4`）。**
>
> equality frontier 中已有 `0<R_dec<10^d` 与 exact `-1 carry`。本文证明该结构有很宽的 quantitative continuation：若
> \[
> \delta:=c_*-n/S<3/4,
> \]
> 则 sufficiently large `S` 上仍有
> \[
> \boxed{0<R_{\rm dec}<10^d,}
> \]
> 从而
> \[
> \boxed{\left\lfloor Ua_3/10^d\right\rfloor=BVA_{12}-1,}
> \]
> \[
> \boxed{Ua_3\bmod10^d=10^d-R_{\rm dec}.}
> \]
> 因而当前 `delta<0.238...` CRT neighborhood 全部处在同一个 exact top-residue cell 中。

---

## 1. generic remainder 本来就是 carry defect

primitive carry为

\[
\boxed{
Ua_3=B10^dVA_{12}-\frac\Sigma{g_0}R_0,}
\tag{1.1}
\]

其中上一文件已证明

\[
g_0\mid\Sigma.
\]

定义

\[
\boxed{
R_{\rm dec}:=
B10^dVA_{12}-Ua_3
=\frac\Sigma{g_0}R_0.}
\tag{1.2}
\]

所有量为正，所以

\[
\boxed{R_{\rm dec}>0.}
\tag{1.3}
\]

这不依赖 equality normalization。

---

## 2. `Sigma` 的统一 `2S+O(1)` upper

canonical phase有

\[
\kappa=2\gamma5^TU,
\qquad
G=\gamma V,
\]

故

\[
Y:=5^TU=\frac\kappa{2\gamma},
\qquad
X:=2^HZ=Y+V,
\]

\[
\Sigma=X+Y=2Y+V.
\tag{2.1}
\]

prefix decimal pinning给

\[
\frac{Q^2}{11}<\kappa<10Q^2,
\]

且 `Q<10^S`。因为 `gamma>=1`：

\[
Y<5Q^2<5\cdot10^{2S}.
\]

另一方面

\[
V\le G=b_1b_2<10^S.
\]

所以

\[
\Sigma=2Y+V
<10\cdot10^{2S}+10^S
<11\cdot10^{2S}
\]

for `S>=1`。因此

\[
\boxed{
\log_{10}\Sigma\le2S+O(1).}
\tag{Sigma-upper}
\]

这里甚至不需要 terminal-neighborhood stability。

---

## 3. gap quotient只损失 `delta S`

已有 exact gap ratio

\[
\frac{R_0}{g_0}
=\frac{H_{\rm sph}-y_3}{2\cdot5^Tc_3}>0.
\]

`dd-corrected-neighborhood-gap-fiber-entropy-2026-08-22.md` 证明

\[
\log_{10}(R_0g_0)\le\delta S+o(S).
\]

由于 `g_0>=1`：

\[
\boxed{
\log_{10}(R_0/g_0)
\le\log_{10}R_0
\le\delta S+o(S).}
\tag{Gap-ratio-upper}
\]

由 `(1.2)`、`(Sigma-upper)`：

\[
\boxed{
\log_{10}R_{\rm dec}
\le(2+\delta)S+o(S).}
\tag{Rdec-upper}
\]

---

## 4. third surplus gap 有 `3.5-delta` lower

quantitative terminal geometry已证明

\[
\boxed{
\frac dS\ge\frac72-\delta-o(1).}
\tag{d-lower}
\]

因此

\[
\log_{10}10^d
\ge(3.5-\delta)S-o(S).
\]

若固定

\[
\boxed{\delta<3/4,}
\tag{4.1}
\]

则

\[
3.5-\delta>2+\delta.
\]

存在正 margin

\[
1.5-2\delta>0.
\]

所以由 `(Rdec-upper)` 与 `(d-lower)`，sufficiently large `S` 上：

\[
\boxed{0<R_{\rm dec}<10^d.}
\tag{Decimal-cell-neighborhood}
\]

---

## 5. exact `-1 carry`

由定义

\[
Ua_3=BVA_{12}10^d-R_{\rm dec}.
\]

且 `(Decimal-cell-neighborhood)` 给

\[
0<R_{\rm dec}<10^d.
\]

因此

\[
Ua_3
=(BVA_{12}-1)10^d
+\left(10^d-R_{\rm dec}\right),
\]

其中

\[
0<10^d-R_{\rm dec}<10^d.
\]

故 exact 地

\[
\boxed{
\left\lfloor\frac{Ua_3}{10^d}\right\rfloor
=BVA_{12}-1.}
\tag{Carry-floor-neighborhood}
\]

以及

\[
\boxed{
Ua_3\bmod10^d
=10^d-R_{\rm dec}.}
\tag{Top-residue-neighborhood}
\]

相对 modulus 的 deficit满足

\[
\frac{R_{\rm dec}}{10^d}
\le
10^{-\left(\frac32-2\delta\right)S+o(S)}.
\tag{5.1}
\]

所以 top residue仍是 exponentially thin，只是 exponent margin从 equality 的 `3/2` 线性退化为

\[
\boxed{\frac32-2\delta.}
\tag{Top-margin}
\]

---

## 6. 与当前 CRT neighborhood 的兼容

carry-`U` × pair-max theorem 的 fixed-fiber uniqueness只需要

\[
\delta<0.238062349248111\ldots.
\]

该范围严格包含于 `delta<3/4`。因此当前全部 uniqueness neighborhood自动同时满足 exact top-residue：

\[
\boxed{
Ua_3\equiv-R_{\rm dec}\pmod{10^d},
\qquad
0<R_{\rm dec}
\le10^{(2+\delta)S+o(S)}.}
\]

由于 `(U,10)=1`，这也固定 `a_3 mod 10^d`：

\[
\boxed{
a_3\equiv-U^{-1}R_{\rm dec}\pmod{10^d}.}
\tag{a3-decimal-period}
\]

但本文不把 `10^d` 再当作与 carry 独立的 local modulus：它就是同一个 exact carry 的 Archimedean/decimal 坐标。

---

## 7. 下一接口

当前一个合法 candidate同时具有：

1. `A_12` 的 full `U` residue；
2. `A_12` 的 full `v_2` pair-max residue；
3. short `a_2` 的 oriented `v_2` residue；
4. `a_3` 的 top-decimal residue modulo `10^d`；
5. `R_dec/10^d` 的指数薄层宽度 `10^{-(3/2-2delta)S+o(S)}`。

local elimination大多会退回 carry/sphere identities；真正有希望的是研究 unique `Uv_2` lift对应的 `a_3` 是否能同时落入 `(Top-residue-neighborhood)` 的薄 Archimedean cell。

这是一个比 equality-only Top-residue更强的起点：薄层宽度现在对整个 fixed positive-width neighborhood都有显式控制。

---

## 8. 状态摘要

- **已严格完成：** generic positive `R_dec`。
- **已严格完成：** uniform `log Sigma<=2S+O(1)`。
- **已严格完成：** `log R_dec<=(2+delta)S+o(S)`。
- **已严格完成：** 对任意 fixed `delta<3/4`，`0<R_dec<10^d`。
- **已严格完成：** neighborhood exact `-1 carry` 与 `Top-residue-neighborhood`。
- **显式薄层 margin：** `(3/2-2delta)S`。
- **仍待证：** unique `Uv_2` lift 与 top-residue cell 的 Archimedean incompatibility；explicit strict slope gap；DD emptiness；effective absolute height bound。

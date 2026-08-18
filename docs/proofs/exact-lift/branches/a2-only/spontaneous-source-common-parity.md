# A2 source→common natural gate 的 primitive `3 mod 8` orientation

> **依赖：** `spontaneous-source-common-integer.md`、`spontaneous-source-prefix-simple.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文对 source→common natural integer `K_src(H,E,F)` 做精确 `2`-进本原化。利用真实 denominator defect并非任意，而满足 `b_2=E(F+H)=2^{M+m+1}c_ug`，证明 `v_2(K_src)=8`，且正奇 quotient `K_src/2^8` 恒为 `3 mod 8`。因此 source→common gate 自身也是一个全局 odd-inert parity carrier。本文不声称 `K_src` 的每个 inert divisor都是真正 source prime，也不据此关闭 A2。

---

## 1. natural integer gate

沿用

\[
F:=5^{M-1},
\qquad
E:=2^{M-1},
\qquad
M\ge11.
\]

真实 denominator defect为

\[
b_2=E(F+H).
\tag{1.1}
\]

`spontaneous-source-common-integer.md` 定义

\[
\boxed{
\begin{aligned}
\mathcal K_{\rm src}
={}&4400F^2(H+21F)^2\\
&+81EF\,\mathcal P_4(H,F)\\
&-810E^2(H+F)(99H+59F)\\
&\qquad\cdot(H^2+2HF+5F^2)(49H^2+58HF-191F^2),
\end{aligned}}
\tag{1.2}
\]

其中

\[
\boxed{
\mathcal P_4
=9401H^4+13684H^3F-175354H^2F^2
-418156HF^3-878519F^4.}
\tag{1.3}
\]

并有 positive scaling identity

\[
\boxed{
\mathcal K_{\rm src}
=10E^2F^6\,(10000\mathcal C_{\rm src}).}
\tag{1.4}
\]

真实 endpoint 已证明

\[
\mathcal C_{\rm src}>448,
\]
所以

\[
\boxed{\mathcal K_{\rm src}>0.}
\tag{1.5}
\]

---

## 2. `已严格完成`：真实 denominator normal form强迫 `v_2(H+F)>=3`

deep-even normal form同时给

\[
\boxed{
b_2=2^{M+m+1}c_ug.}
\tag{2.1}
\]

与 (1.1) 比较，并用 `E=2^{M-1}`：

\[
\boxed{
H+F=2^{m+2}c_ug.}
\tag{2.2}
\]

当前 third block至少有一位，故 `m>=1`。因此

\[
\boxed{8\mid H+F.}
\tag{2.3}
\]

`F` 为奇数，于是 `H` 也为奇数。

进一步：

\[
H+21F=(H+F)+20F.
\]
第一项被 `8` 整除，第二项满足 `v_2(20F)=2`，所以

\[
\boxed{v_2(H+21F)=2.}
\tag{2.4}
\]

写

\[
\boxed{H+21F=4L,\qquad L\text{ odd}.}
\tag{2.5}
\]

---

## 3. 第一项精确停在 `2^8`

由 (2.5)：

\[
4400F^2(H+21F)^2
=4400\cdot16F^2L^2
=2^8\cdot275F^2L^2.
\tag{3.1}
\]

因此第一项满足

\[
\boxed{v_2=8,}
\tag{3.2}
\]

且因为 odd square模 `8` 恒为 `1`：

\[
\boxed{
\frac{4400F^2(H+21F)^2}{2^8}
\equiv275\equiv3\pmod8.}
\tag{3.3}
\]

---

## 4. 第二、第三项在除 `2^8` 后都消失模 `8`

先看 `P_4`。因为 `H,F` 都奇，模 `2` 只有两个 odd coefficient项留下：

\[
\mathcal P_4
\equiv H^4-F^4
\equiv1-1
\equiv0\pmod2.
\tag{4.1}
\]

所以

\[
v_2(81EF\mathcal P_4)
\ge(M-1)+1
=M
\ge11.
\tag{4.2}
\]

从而

\[
\boxed{
2^{-8}(81EF\mathcal P_4)
\equiv0\pmod8.}
\tag{4.3}
\]

第三项的 coefficient `810` 具有 `v_2=1`，所以无论后面 product 的额外 parity如何：

\[
v_2(810E^2\cdot\text{product})
\ge1+2(M-1)
\ge21.
\tag{4.4}
\]

故

\[
\boxed{
2^{-8}(810E^2\cdot\text{product})
\equiv0\pmod8.}
\tag{4.5}
\]

---

## 5. `已严格完成`：primitive source-common gate 恒为 `3 mod 8`

综合 §§3–4：

\[
\boxed{v_2(\mathcal K_{\rm src})=8.}
\tag{5.1}
\]

定义

\[
\boxed{
\widehat{\mathcal K}_{\rm src}
:=\frac{\mathcal K_{\rm src}}{2^8}.}
\tag{5.2}
\]

则由 (1.5)、(3.3)、(4.3)、(4.5)：

\[
\boxed{
\widehat{\mathcal K}_{\rm src}>0,
\qquad
\widehat{\mathcal K}_{\rm src}\equiv3\pmod8.}
\tag{5.3}
\]

因此

\[
\boxed{
\sum_{p\equiv3\ (4)}
v_p(\widehat{\mathcal K}_{\rm src})
\equiv1\pmod2.}
\tag{5.4}
\]

也就是说 source→common natural gate自身强迫一份 odd inert parity。

---

## 6. 与已有两个 parity carriers 的关系

目前 dangerous endpoint中已经有

\[
\widehat{\mathcal O}_{\rm sp}>0,
\qquad
\widehat{\mathcal O}_{\rm sp}\equiv3\pmod4,
\]

\[
\widehat{\mathcal T}_2>0,
\qquad
\widehat{\mathcal T}_2\equiv3\pmod4.
\]

本文新增第三个 primitive integer：

\[
\boxed{
\widehat{\mathcal K}_{\rm src}>0,
\qquad
\widehat{\mathcal K}_{\rm src}\equiv3\pmod8.}
\tag{6.1}
\]

但必须保留逻辑边界：`K_src` 是 source slice 的 **gate integer**。一个任意 prime整除 `K_src` 并不自动意味着它同时整除 source integer `sigma` / `D_src`。只有再加入 source Hensel condition后，该 prime才成为真正 source→common carrier。

因此 (6.1) 不能单独推出 `G_sp` 的 parity；它提供的是新的全局自然整数，供后续研究

\[
\gcd(\widehat K_{\rm src},D_{\rm src}),
\qquad
\gcd(\widehat K_{\rm src},\sigma),
\]
或 source half-depth saturation时使用。

---

## 7. 更新后的 source frontier

结合 `spontaneous-source-depth-transfer.md`：

- `C_src` 精确读取 source common 的低于 `h` 的 additive depth；
- `K_src` 是 `C_src` 的真实整数 representative；
- `K_src/2^8` 自身为 positive `3 mod 8`；
- source base primary `p^{2h}` 仍为 even parity；
- 真正困难因此进一步集中为：`K_src` 的 odd inert parity 中，多少能与 source primary同步，以及 half-depth saturation后的 normalized blow-up。

这比继续做 source singular/discriminant hunting更接近 `G_sp` 的全局 parity，但尚未形成 closure。
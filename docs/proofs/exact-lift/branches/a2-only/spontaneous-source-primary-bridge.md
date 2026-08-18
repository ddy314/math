# A2 source primary 与 angle primitive carrier 的 exact integer bridge

> **依赖：** `spontaneous-prefix-eliminant.md`、`spontaneous-source-saturation-parity.md`、`spontaneous-source-prefix-simple.md`、`hensel.md`。
>
> **严格状态：**本文把 source Hensel linear form、source prefix half-depth `D_src` 与 spontaneous angle raw integer `O_sp` 放进同一条 exact integer identity。核心公式是
>
> \[
> 81\mathcal O_{\rm sp}=400T D_{\rm src}^2-81A^2\mathcal S_{\rm src}.
> \]
>
> 对 genuine non-`3` source prime，`v_p(S_src)=2h`，因此 source base `p^{2h}` 完整进入 angle carrier，且只有 `v_p(D_src)=h` 的 equal-depth cancellation能够产生 extra angle depth。这给 `spontaneous-source-saturation-parity.md` 一个更短的原始整数证明，并明确 extra depth 的唯一 algebraic来源。本文不排除该 equal-depth cancellation，也不关闭 A2。

---

## 1. 原始 decimal blocks

固定 reflection endpoint，记

\[
N:=10^M,
\qquad
T:=10^m,
\qquad
A:=a_2,
\qquad
B:=b_2,
\]

\[
Q:=B+2N.
\tag{1.1}
\]

`spontaneous-prefix-eliminant.md` 的 angle raw integer为

\[
\boxed{
\mathcal O_{\rm sp}
:=T\mathcal U_\Omega+2A^2Qb_3,}
\tag{1.2}
\]

其中

\[
\boxed{
\mathcal U_\Omega
=(45B^2-2AN)^2-A^2B(99B-4N).}
\tag{1.3}
\]

对 genuine odd prime，`O_sp` 与 `Omega_sp` / primitive `widehat(O)_sp` 只差固定 `2`-power和 odd units。

---

## 2. `已严格完成`：source Hensel line 的原始整数

source normalized variables为

\[
x=B/N,
\qquad
r_s=BT/b_3.
\]

因此

\[
\Phi_s=(99x-4)r_s-2x-4
\]
满足

\[
\begin{aligned}
Nb_3\Phi_s
&=TB(99B-4N)-2Bb_3-4Nb_3\\
&=TB(99B-4N)-2Qb_3.
\end{aligned}
\]

定义

\[
\boxed{
\mathcal S_{\rm src}
:=TB(99B-4N)-2Qb_3.}
\tag{2.1}
\]

则有 exact identity

\[
\boxed{
\mathcal S_{\rm src}=Nb_3\Phi_s.}
\tag{2.2}
\]

对 genuine source excess prime，`p` 与 `Nb_3` 分离，旧 source Hensel给

\[
p^{2h}\Vert\sigma,
\qquad
v_p(\Phi_s)=2h.
\]

所以

\[
\boxed{v_p(\mathcal S_{\rm src})=2h.}
\tag{2.3}
\]

这就是 source primary depth 的纯 integer representative。

---

## 3. source prefix defect正好是 angle square term

reflection 中

\[
A_0=9\cdot10^{M-1}=9N/10,
\qquad
C_0=9B/2,
\]

并定义

\[
D_{\rm src}:=C_0^2-A_0A.
\]

直接计算：

\[
D_{\rm src}
=\frac{81}{4}B^2-\frac9{10}AN.
\]

因此

\[
\boxed{
45B^2-2AN=\frac{20}{9}D_{\rm src}.}
\tag{3.1}
\]

这解释了 `U_Omega` 第一平方项为何正好测量 source half-depth，而不是一个新的独立 prefix polynomial。

---

## 4. `已严格完成`：angle raw integer 的 source bridge

从 (1.2)–(1.3)：

\[
\begin{aligned}
\mathcal O_{\rm sp}
={}&T(45B^2-2AN)^2\\
&-A^2\bigl[TB(99B-4N)-2Qb_3\bigr].
\end{aligned}
\]

使用 (2.1)：

\[
\boxed{
\mathcal O_{\rm sp}
=T(45B^2-2AN)^2-A^2\mathcal S_{\rm src}.}
\tag{4.1}
\]

再用 (3.1)，清去固定 denominator `9^2`：

\[
\boxed{
81\mathcal O_{\rm sp}
=400T D_{\rm src}^2-81A^2\mathcal S_{\rm src}.}
\tag{4.2}
\]

这是 source primary、prefix half-depth和 angle carrier之间的 exact integer bridge。

---

## 5. exact gcd / truncated valuation law

由 (4.2)，对任意 prime `p !=2,3,5` 且 `p∤AT`：

\[
\gcd(81\mathcal O_{\rm sp},\mathcal S_{\rm src})
=
\gcd(400T D_{\rm src}^2,\mathcal S_{\rm src})
\]
在 `p`-primary上给

\[
\boxed{
\min\{v_p(\mathcal O_{\rm sp}),v_p(\mathcal S_{\rm src})\}
=
\min\{2v_p(D_{\rm src}),v_p(\mathcal S_{\rm src})\}.}
\tag{5.1}
\]

现在固定 genuine source prime：

\[
v_p(\mathcal S_{\rm src})=2h,
\qquad
v_p(D_{\rm src})\ge h.
\]

于是

\[
\boxed{
\min\{v_p(\mathcal O_{\rm sp}),2h\}=2h.}
\tag{5.2}
\]

这直接恢复 source base primary完整进入 angle carrier的结论。

因为 primitive `widehat(O)_sp` 与 `O_sp` 只差固定 `2`-power，对 odd source prime同样有

\[
\boxed{
\min\{v_p(\widehat{\mathcal O}_{\rm sp}),2h\}=2h.}
\tag{5.3}
\]

---

## 6. extra angle depth 的唯一来源

bridge (4.2) 还给出更精确的 dichotomy。

### 6.1 strict half-depth

若

\[
v_p(D_{\rm src})>h,
\]
则第一平方项深度严格大于 `2h`，第二项精确为 `2h`。所以

\[
\boxed{
v_p(\widehat{\mathcal O}_{\rm sp})=2h.}
\tag{6.1}
\]

没有任何 extra angle depth。

### 6.2 equal-depth shell

只有

\[
\boxed{v_p(D_{\rm src})=h}
\tag{6.2}
\]
时两项都恰处在 `2h`，才可能继续 cancellation。

令

\[
D^\sharp:=D_{\rm src}/p^h,
\qquad
S^\sharp:=\mathcal S_{\rm src}/p^{2h}.
\]

则 extra lift至少一层的必要且充分 normalized condition为

\[
\boxed{
400T(D^\sharp)^2
\equiv81A^2S^\sharp\pmod p.}
\tag{6.3}
\]

这就是此前 `spontaneous-source-equal-depth.md` / `...-nogo.md` 的 normalized cancellation，用完全原始 decimal integers重写后的形式。

因此 source parity ledger可以规范分成

\[
\boxed{
2h\quad+\quad
v_p\!\left(400T(D^\sharp)^2-81A^2S^\sharp\right),}
\tag{6.4}
\]

第一部分严格偶数，第二部分才是真正 angle-over-source residual。

---

## 7. 对后续全局 parity 的意义

本文证明 source base depth之所以为偶，并不是抽象 Gaussian parity巧合，而来自 raw angle integer自身的

\[
\boxed{
\text{square prefix term}-\text{source primary term}.}
\]

结合 `spontaneous-source-depth-transfer.md`，现在 source primary在两侧的规范 ledger为：

\[
\boxed{
\begin{array}{c|c}
\text{angle side}&2h+\text{normalized equal-depth extra}\\
\text{additive/common side}&\min(v_p(C_{\rm src}),h)\text{ until half-depth saturation.}
\end{array}}
\]

因此后续真正未闭的 source parity不再是 base `p^{2h}`，而只有：

1. equal-depth angle extra；
2. `C_src` half-depth saturation后的 transverse allocation；
3. generic simple decimal-orbit synchronization。

继续追 source singular discriminant或 source-base Legendre character都不会增加信息。
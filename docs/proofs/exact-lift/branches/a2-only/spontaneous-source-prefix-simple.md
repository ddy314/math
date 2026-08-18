# A2 source common simple branch 的 prefix-`e` lift 与 resultant no-go

> **依赖：** `spontaneous-source-common-integer.md`、`hensel.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文把 source prefix integer `D_src` 精确写成真实 endpoint defects `(H,e,M)`。结论是：对 genuine non-`3` source prime，`D_src` 关于 numerator defect `e` 永远是 unit-slope linear Hensel equation，因此每个 `(H,M)` 与每个 source depth `p^h` 只对应唯一 `e mod p^h`。另一方面 source→common integer gate `K_src(H,E,F)` 完全不含 `e`，所以消去 `e` 不会产生新的 residual polynomial。本文明确把“继续做 `Res_e(D_src,K_src)`”降级为 no-go；真正剩余的是唯一 `e` residue 与真实窄窗的 natural-representative synchronization，而不是新的局部 singularity。本文不宣称 A2 全局关闭。

---

## 1. 真实 endpoint defects

沿用

\[
F:=5^{M-1},
\qquad
E:=2^{M-1},
\qquad
10^{M-1}=EF.
\]

最危险 reflection endpoint 中

\[
\boxed{b_2=10^{M-1}+2^{M-1}H=E(F+H),}
\tag{1.1}
\]

\[
\boxed{a_2=10^{M-1}-e=EF-e.}
\tag{1.2}
\]

并且真实窄窗为

\[
0<H<F/19,
\qquad
0<e<EF/250.
\tag{1.3}
\]

---

## 2. `已严格完成`：`D_src` 的 exact defect form

reflection 中 `a_1=9`，故

\[
A_0=9\cdot10^{M-1}=9EF,
\qquad
C_0=\frac{9b_2}{2}=\frac{9E(F+H)}2.
\]

source prefix integer为

\[
D_{\rm src}=C_0^2-A_0a_2.
\]

代入 (1.1)–(1.2)：

\[
\begin{aligned}
D_{\rm src}
&=\frac{81E^2(F+H)^2}{4}
-9EF(EF-e)\\
&=\frac{9E^2}{4}
\left[9(F+H)^2-4F^2\right]
+9EF e.
\end{aligned}
\]

因此

\[
\boxed{
D_{\rm src}
=
\frac{9E^2}{4}
(5F^2+18FH+9H^2)
+9EF e.}
\tag{2.1}
\]

因为当前 `M` 很大，`E` 被 `2` 高次整除，所以右边当然为整数；对 odd source prime则只需把 `4` 视为 unit。

这与 normalized identity

\[
D_{\rm src}
=9\cdot10^{2M-2}(225x^2-y)
\]
完全一致。

---

## 3. `已严格完成`：source half-depth 对 `e` 永远 simple

固定 genuine non-`3` source excess prime

\[
p\equiv3\pmod4,
\qquad p\ne3,5.
\]

source separation保证 `p` 不进入 decimal powers，因此

\[
\boxed{p\nmid 9EF.}
\tag{3.1}
\]

由 (2.1)：

\[
\boxed{
\frac{\partial D_{\rm src}}{\partial e}=9EF,}
\tag{3.2}
\]

在 `Z_p` 中为单位。因此无论 source half-depth `h` 多大，条件

\[
p^h\mid D_{\rm src}
\]
都等价于唯一线性 residue：

\[
\boxed{
4Fe
\equiv
-E(5F^2+18FH+9H^2)
\pmod{p^h}.}
\tag{3.3}
\]

因为 `4F` 为单位，对每个固定 `(H,E,F)`：

\[
\boxed{
\text{there is exactly one }e\pmod{p^h}
\text{ satisfying the source prefix depth}.}
\tag{3.4}
\]

所以 `D_src` 本身不可能产生 singular `e`-Hensel tree，也不存在第二个 `e` phase。

---

## 4. 与 source→common integer gate 的变量分离

`spontaneous-source-common-integer.md` 定义

\[
\mathcal K_{\rm src}(H,E,F),
\]
并证明 genuine source/common first layer 必须满足

\[
p\mid\mathcal K_{\rm src}(H,E,F).
\]

关键是

\[
\boxed{
\frac{\partial\mathcal K_{\rm src}}{\partial e}=0.}
\tag{4.1}
\]

也就是说两个条件的变量职责完全分离：

\[
\boxed{
\begin{array}{c|c}
\text{object}&\text{controls}\\ \hline
\mathcal K_{\rm src}&(H,M)\text{ common gate}\\
D_{\rm src}&e\text{ 的唯一 source residue}
\end{array}}
\tag{4.2}
\]

source local second-order correction `phi` 又已经由 angle extra-lift唯一决定。因此 simple source/common branch没有任何未命名局部 phase剩余。

---

## 5. `审计 / no-go`：消去 `e` 不会产生新的 residual

把 `D_src` 看成 `e` 的一次多项式，把 `K_src` 看成 `e` 的常数多项式。resultant定义立即给

\[
\boxed{
\operatorname{Res}_e
(D_{\rm src},\mathcal K_{\rm src})
=
\mathcal K_{\rm src}.}
\tag{5.1}
\]

至多差一个按 resultant convention 选择的单位幂；这里 `deg_e D_src=1`，所以恰好就是一份 `K_src`。

因此继续尝试

\[
\gcd(D_{\rm src},\mathcal K_{\rm src})
\]
的纯多项式消元，**不会**像 denominator `R_q/R_f` 那样掉出新的 simple residual。原因不是计算尚未做够，而是 `e` 只存在于一个 unit-slope linear equation中。

这条 no-go 必须保留，避免后续 agent 重复做一个注定退化的 resultant。

---

## 6. 真正剩余的是 natural representative

对 fixed `(p,h,H,M)`，(3.3) 给出唯一 residue

\[
e\equiv e_0\pmod{p^h}.
\]

但真实 decimal endpoint还要求

\[
\boxed{0<e<EF/250.}
\tag{6.1}
\]

因此 simple source/common branch是否真实存在，已经精确变成：

1. `(H,M)` 命中 common gate `K_src=0 mod p` 及其 simple lift；
2. source depth给出的唯一 `e mod p^h` 是否有 representative落进 (6.1)；
3. 同时满足其余 exact endpoint shell / additive depth。

这不是一个新的局部 algebraic-singularity 问题，而是 decimal-orbit / natural-representative synchronization。

---

## 7. 更新后的 source simple frontier

结合前两份 source 文件，现在 source-supported common channel可以规范写成

\[
\boxed{
\begin{array}{l}
\text{(i) }\mathcal K_{\rm src}(H,E,F)\equiv0\pmod p,\\
\text{(ii) }4Fe\equiv-E(5F^2+18FH+9H^2)\pmod{p^h},\\
\text{(iii) }0<H<F/19,\quad0<e<EF/250.
\end{array}}
\tag{7.1}
\]

其中：

- singular common gate 已审计并死亡；
- `(ii)` 对 `e` 唯一且 simple；
- local source angle correction也唯一；
- 所以剩下的全部自由都集中在 **simple `(H,M)` common orbit + natural representative**。

下一步若继续 source channel，应直接攻击 (7.1) 的 representative/orbit；不应再做 `e`-resultant、source singular-prime 或局部 Legendre stacking。
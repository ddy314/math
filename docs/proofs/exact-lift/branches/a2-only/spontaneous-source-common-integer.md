# A2 source→common gate 的自然整数代表与 singular audit

> **依赖：** `spontaneous-source-common-gate.md`、`spontaneous-source-saturation-parity.md`。
>
> **严格状态：**本文把 source→additive-common 的 normalized gate `C_src(x,tau)` 精确乘回真实 denominator defect `H` 与 decimal length `M`，得到一个整数 target `K_src(H,E,F)`。随后完整审计该 gate 作为 `(x,tau)` 平面曲线的 non-`3` inert singular bad reduction：唯一 genuine singular first-layer point出现在 `p=1746991`，但它不能提升到 `p^2`。因此 source→common gate 不存在 surviving singular Hensel tree；generic simple modular roots仍可能存在，所以本文不宣称 A2 全局关闭。

---

## 1. 回顾 source→common quadratic

沿用

\[
\boxed{
\begin{aligned}
\mathcal C_{\rm src}(x,\tau)
={}&440(x+2)^2\tau^2\\
&+81(9401x^4-2392x^3-1600x^2-64x-64)\tau\\
&-324x(99x-4)(25x^2+1)(49x^2-4x-2).
\end{aligned}}
\tag{1.1}
\]

在 genuine/noncentral source first-layer channel 中，

\[
\mathcal C_{\rm src}(x,10^{-M})\equiv0\pmod p
\]

是 source-supported angle root 进一步进入 additive common carrier 的必要且充分 first-layer gate。

真实 endpoint defect 为

\[
\boxed{x=\frac{1+u}{10},\qquad u=\frac{H}{5^{M-1}}.}
\tag{1.2}
\]

定义

\[
\boxed{F:=5^{M-1},\qquad E:=2^{M-1}.}
\tag{1.3}
\]

则

\[
u=H/F,\qquad 10^M=10EF,\qquad \tau=\frac1{10EF}.
\tag{1.4}
\]

---

## 2. `已严格完成`：defect gate 的整数化

`spontaneous-source-common-gate.md` 已有

\[
\boxed{
\begin{aligned}
10000\mathcal C_{\rm src}
={}&44000(u+21)^2\tau^2\\
&+81(9401u^4+13684u^3-175354u^2\\
&\qquad-418156u-878519)\tau\\
&-81(u+1)(99u+59)(u^2+2u+5)\\
&\qquad\cdot(49u^2+58u-191).
\end{aligned}}
\tag{2.1}
\]

把 (1.4) 代入并乘去所有 `2,5` denominator，得到

\[
\boxed{
10E^2F^6\,(10000\mathcal C_{\rm src})
=\mathcal K_{\rm src}(H,E,F),}
\tag{2.2}
\]

其中

\[
\boxed{
\begin{aligned}
\mathcal K_{\rm src}
={}&4400F^2(H+21F)^2\\
&+81EF\,\mathcal P_4(H,F)\\
&-810E^2(H+F)(99H+59F)\\
&\qquad\cdot(H^2+2HF+5F^2)
(49H^2+58HF-191F^2),
\end{aligned}}
\tag{2.3}
\]

且

\[
\boxed{
\begin{aligned}
\mathcal P_4(H,F):={}&9401H^4+13684H^3F-175354H^2F^2\\
&-418156HF^3-878519F^4.
\end{aligned}}
\tag{2.4}
\]

对 genuine source prime `p != 2,5`，`E,F` 均为 `p`-进单位，因此逐 prime-power 精确有

\[
\boxed{
v_p(\mathcal C_{\rm src})=v_p(\mathcal K_{\rm src}).}
\tag{2.5}
\]

特别地 source→common 条件现在有真正的整数自然代表：

\[
\boxed{p^k\mid\mathcal C_{\rm src}
\iff p^k\mid\mathcal K_{\rm src}.}
\tag{2.6}
\]

这一步没有引入新的 source/Hensel 变量；`K_src` 只依赖真实小缺口 `H` 与 decimal powers `E,F`。

---

## 3. genuine source units 在整数坐标中的对应

由

\[
x=\frac{H+F}{10F},
\]
有

\[
99x-4=\frac{99H+59F}{10F},
\tag{3.1}
\]

以及

\[
25x^2+1
=\frac{H^2+2HF+5F^2}{4F^2}.
\tag{3.2}
\]

因此旧 source separation

\[
p\nmid x(x+2)(99x-4)(25x^2+1)
\]
等价于 `K_src` 中前三类显式 defect factor均为单位。特别是整数化没有把已排除的 q/f/source boundary重新伪装成新因子。

---

# 第二部分：source→common gate 的 singular bad reduction

## 4. `tau`-discriminant

把 `C_src` 看成

\[
\mathcal C_{\rm src}=a(x)\tau^2+b(x)\tau+c(x),
\]
其中

\[
a(x)=440(x+2)^2.
\]

已有

\[
\boxed{
\operatorname{Disc}_\tau(\mathcal C_{\rm src})
=81\mathcal D_{\rm sc}(x),}
\tag{4.1}
\]

\[
\boxed{
\begin{aligned}
\mathcal D_{\rm sc}(x)={}&8012458881x^8-332013104x^7+1027170624x^6\\
&+111485312x^5+130846848x^4+25281536x^3\\
&+12020736x^2+888832x+331776.
\end{aligned}}
\tag{4.2}
\]

其 `x`-判别式精确分解为

\[
\boxed{
\begin{aligned}
\operatorname{Disc}_x(\mathcal D_{\rm sc})
={}&2^{96}3^55^4 11^4 101^{24}\cdot109\cdot233\\
&\cdot1746991\cdot405504443^2.
\end{aligned}}
\tag{4.3}
\]

因此除 `2,3,5` 与 `1 mod 4` primes外，full singular reduction只需审计

\[
\boxed{11,\quad1746991,\quad405504443.}
\tag{4.4}
\]

---

## 5. 为什么 repeated `tau` + repeated discriminant 正好控制 full singularity

当 `p` 不整除 `2a(x)` 时，若

\[
\mathcal C_{\rm src}=0,
\qquad
\partial_\tau\mathcal C_{\rm src}=0,
\]
则

\[
\tau=-\frac{b}{2a},
\qquad
\mathcal D_{\rm sc}=0.
\]

在这个 repeated root 上有 exact differential identity

\[
\boxed{
\mathcal D_{\rm sc}'
=-\frac{4a}{81}\,\partial_x\mathcal C_{\rm src}.}
\tag{5.1}
\]

所以在 `a` 为单位时：

\[
\boxed{
\mathcal C_{\rm src}
=\partial_\tau\mathcal C_{\rm src}
=\partial_x\mathcal C_{\rm src}=0
\iff
\mathcal D_{\rm sc}=\mathcal D_{\rm sc}'=0.}
\tag{5.2}
\]

因此 (4.3) 确实给出所有 generic full singular prime 的有限 bad set。

`p=11` 因 `440=0 mod 11` 需单独检查。

---

## 6. `p=11`：quadratic coefficient degeneration，但没有 finite singular point

模 `11`，

\[
a(x)\equiv0,
\]
而

\[
\boxed{
\partial_\tau\mathcal C_{\rm src}
\equiv
-5(x^2-5x-1)(x^2-2x-5)\pmod{11}.}
\tag{6.1}
\]

两个 quadratic 的判别式分别是 `7` 与 `2`，都不是模 `11` 的平方。因此

\[
\boxed{
\partial_\tau\mathcal C_{\rm src}\ne0
\quad\text{for every }x\in\mathbf F_{11}.}
\tag{6.2}
\]

故 `p=11` 没有 full singular point。它仍可能有 simple common states；本文只删除 singular tree。

---

## 7. `p=405504443`：repeated discriminant factor没有 `F_p` 根

精确计算

\[
\gcd(\mathcal D_{\rm sc},\mathcal D_{\rm sc}')
\equiv
x^2-63668219x+95115196
\pmod{405504443}.
\tag{7.1}
\]

该二次式判别式为

\[
345543957\pmod{405504443},
\]
且

\[
\left(\frac{345543957}{405504443}\right)=-1.
\tag{7.2}
\]

所以没有 `x in F_p` 的 repeated discriminant root，因而没有 finite full singular source→common state。

---

## 8. `p=1746991`：唯一 genuine singular first layer

此时

\[
\boxed{
\gcd(\mathcal D_{\rm sc},\mathcal D_{\rm sc}')
\equiv x+384338\pmod{1746991}.}
\tag{8.1}
\]

所以唯一 repeated `x` residue 为

\[
\boxed{x_0=1362653.}
\tag{8.2}
\]

由 repeated quadratic root

\[
\tau_0=-\frac{b(x_0)}{2a(x_0)}
\]
得到

\[
\boxed{\tau_0=807263\pmod{1746991}.}
\tag{8.3}
\]

直接代回：

\[
\mathcal C_{\rm src}(x_0,\tau_0)
\equiv
\partial_x\mathcal C_{\rm src}(x_0,\tau_0)
\equiv
\partial_\tau\mathcal C_{\rm src}(x_0,\tau_0)
\equiv0\pmod p.
\tag{8.4}
\]

同时 genuine units 为

\[
\boxed{
\begin{array}{c|c}
\text{factor}&\text{residue mod }p\\ \hline
x_0&1362653\\
x_0+2&1362655\\
99x_0-4&384336\\
25x_0^2+1&1554823\\
2(9+225x_0^2)-9\tau_0&1504546
\end{array}}
\tag{8.5}
\]

全部非零。因此它确实是 genuine/noncentral singular first-layer candidate，而不是旧 boundary。

---

## 9. `有限证书`：唯一 singular candidate不能提升到 `p^2`

取最小非负 representatives `(x_0,tau_0)`。exact integer value满足

\[
\boxed{
\frac{\mathcal C_{\rm src}(x_0,\tau_0)}p
\equiv1642591\not\equiv0\pmod p.}
\tag{9.1}
\]

另一方面 (8.4) 给

\[
p\mid\partial_x\mathcal C_{\rm src}(x_0,\tau_0),
\qquad
p\mid\partial_\tau\mathcal C_{\rm src}(x_0,\tau_0).
\]

对任意 lift

\[
x=x_0+pX,
\qquad
\tau=\tau_0+pT,
\]
Taylor 展开模 `p^2`：

\[
\mathcal C_{\rm src}(x,\tau)
\equiv
\mathcal C_{\rm src}(x_0,\tau_0)
+pX\partial_x\mathcal C_{\rm src}
+pT\partial_\tau\mathcal C_{\rm src}
\pmod{p^2}.
\]
后两项均自动被 `p^2` 整除，所以 (9.1) 无法被任何 `(X,T)` 修正：

\[
\boxed{
\text{the }1746991\text{ singular state has no }p^2\text{ lift}.}
\tag{9.2}
\]

---

## 10. 结论与新的 source→common frontier

综合 §§4–9：

\[
\boxed{
\text{source→common gate 在 genuine non-3 inert channel中不存在 surviving singular Hensel tree}.}
\tag{10.1}
\]

因此 source residual 的结构现在与 denominator common channel高度平行：

- source base primary depth `2h` 是偶数；
- source-local angle extra 是 simple 二阶 correction；
- source→additive-common 的外部 gate `C_src=0` 也没有 surviving singular tree；
- 真正剩余的只有 **simple modular roots of the integer gate `K_src` 与 decimal defect orbit `(H,E,F)` 的同步**。

下一步不应再做 singular-discriminant hunting。最有价值的是研究

\[
\gcd(D_{\rm src},\mathcal K_{\rm src})
\]

在 source primary depth `p^h|D_src` 下的截断赋值，或者把 `K_src` 与

\[
H+F=4c_u2^mg
\]
的 source-content separation 联立，寻找一个类似 denominator `R_q/R_f` 的 simple depth residual。
# A2 source→common 的 pure numerator/length eliminant

> **依赖：** `spontaneous-source-common-gate.md`、`spontaneous-source-prefix-simple.md`。
>
> **严格状态：**本文把 source first-layer square relation `225x^2=y` 与 source→common gate `C_src(x,tau)=0` 联立，完全消去 denominator phase `x`。resultant不是黑箱高次式，而精确写成 `E(y,tau)^2-14400 y O(y,tau)^2`。乘回真实 `A=a_2`、`S=10^{M-1}` 后得到整数 residual `R_src`; 在当前 endpoint中它严格为正且 `1 mod 8`。因此真正 source→common prime还必须命中一个只含 numerator defect `e` 与 decimal length `M` 的 pure-decimal gate。本文只给必要 projection与 parity，不声称其所有 modular roots都是真正 source primes，也不关闭 A2。

---

## 1. source square-root coordinate

source first layer为

\[
\boxed{225x^2-y=0.}
\tag{1.1}
\]

令

\[
\boxed{r:=15x,}
\qquad
\boxed{r^2=y.}
\tag{1.2}
\]

source→common gate沿用

\[
\begin{aligned}
\mathcal C_{\rm src}(x,\tau)
={}&440(x+2)^2\tau^2\\
&+81(9401x^4-2392x^3-1600x^2-64x-64)\tau\\
&-324x(99x-4)(25x^2+1)(49x^2-4x-2).
\end{aligned}
\tag{1.3}
\]

---

## 2. `已严格完成`：`C_src` 在 source square relation上只有 even/odd 两块

定义

\[
\boxed{
\begin{aligned}
\mathcal E(y,\tau):={}&
11000\tau^2y+9900000\tau^2\\
&+84609\tau y^2-3240000\tau y-29160000\tau\\
&-19404y^3-10836y^2+1474200y,
\end{aligned}}
\tag{2.1}
\]

以及

\[
\boxed{
\mathcal O(y,\tau):=
5500\tau^2-2691\tau y-16200\tau
+296y^2+1764y-8100.}
\tag{2.2}
\]

把 `x^2=y/225` 用于 (1.3) 的 even powers，而 odd powers提出一份 `x`，直接得到 exact identity

\[
\boxed{
5625\mathcal C_{\rm src}(x,\tau)
=\mathcal E(y,\tau)+120r\mathcal O(y,\tau),
\qquad r=15x,\ r^2=y.}
\tag{2.3}
\]

所以正负两个 source square-root branch只相差 `r` 的符号。

---

## 3. `已严格完成`：消去 `x` 后是单个平方差 residual

由 (2.3)：

\[
\boxed{
\mathcal R_{\rm src}^{(y)}(y,\tau)
:=\mathcal E(y,\tau)^2
-14400y\mathcal O(y,\tau)^2.}
\tag{3.1}
\]

直接 resultant计算给

\[
\boxed{
\operatorname{Res}_x
(225x^2-y,\mathcal C_{\rm src})
=2025^2\mathcal R_{\rm src}^{(y)}.}
\tag{3.2}
\]

因此对 genuine non-`3,5` source/common prime：

\[
\boxed{
p\mid\mathcal C_{\rm src},\quad p\mid225x^2-y
\Longrightarrow
p\mid\mathcal R_{\rm src}^{(y)}(y,\tau).}
\tag{3.3}
\]

这把 first-layer source→common 的必要条件从 `(x,y,tau)` 降成纯 `(y,tau)`。

展开 (3.1) 虽是 degree `(6,4)` polynomial，但 (3.1) 的平方差形式才是规范表达；不应以后把 expanded resultant当作新的黑箱对象。

---

## 4. 真实 numerator/length 的整数化

令

\[
\boxed{S:=10^{M-1},}
\qquad
\boxed{A:=a_2=S-e.}
\tag{4.1}
\]

则

\[
y=A/S,
\qquad
\tau=1/(10S).
\tag{4.2}
\]

定义

\[
\boxed{
\mathscr E:=10S^3\mathcal E(A/S,1/(10S)),}
\tag{4.3}
\]

\[
\boxed{
\mathscr O:=10S^2\mathcal O(A/S,1/(10S)).}
\tag{4.4}
\]

直接清分母得到

\[
\boxed{
\begin{aligned}
\mathscr E={}&-194040A^3-108360A^2S+84609A^2\\
&+14742000AS^2-3240000AS+1100A\\
&-29160000S^2+990000S,
\end{aligned}}
\tag{4.5}
\]

\[
\boxed{
\mathscr O=
2960A^2+17640AS-2691A
-81000S^2-16200S+550.}
\tag{4.6}
\]

于是定义 pure numerator/length integer residual

\[
\boxed{
\mathscr R_{\rm src}
:=\mathscr E^2-14400AS\mathscr O^2.}
\tag{4.7}
\]

并有 exact scaling

\[
\boxed{
\mathcal R_{\rm src}^{(y)}(A/S,1/(10S))
=\frac{\mathscr R_{\rm src}}{100S^6}.}
\tag{4.8}
\]

对 genuine odd prime `p!=5`，`S` 为单位，因此 (3.3) 可完全整数化为

\[
\boxed{p\mid\mathscr R_{\rm src}.}
\tag{4.9}
\]

---

## 5. defect form 与 `2`-进 orientation

把 `A=S-e` 代入：

\[
\boxed{
\begin{aligned}
\mathscr E={}&14439600S^3-13943160S^2e-32315391S^2\\
&-690480Se^2+3070782Se+991100S\\
&+194040e^3+84609e^2-1100e,
\end{aligned}}
\tag{5.1}
\]

\[
\boxed{
\mathscr O=
-60400S^2-23560Se-18891S
+2960e^2+2691e+550.}
\tag{5.2}
\]

当前 `M>=11`，所以

\[
2^{10}\mid S.
\tag{5.3}
\]

又 `A=a_2` 为奇数而 `S` 为偶数，故

\[
\boxed{e\text{ odd}.}
\tag{5.4}
\]

由 (5.1) 模 `8`，所有含 `S` 项消失；对 odd `e`：

\[
\mathscr E
\equiv194040e^3+84609e^2-1100e
\equiv0+1+4
\equiv5\pmod8.
\tag{5.5}
\]

由 (5.2) 模 `2`：

\[
\boxed{\mathscr O\equiv1\pmod2.}
\tag{5.6}
\]

而 `14400AS` 被 `2^6\cdot2^{10}` 整除，所以 (4.7) 给

\[
\boxed{
\mathscr R_{\rm src}
\equiv\mathscr E^2
\equiv1\pmod8.}
\tag{5.7}
\]

因此这个 pure numerator/length residual的 total inert valuation parity为偶数。

---

## 6. `已严格完成`：真实 endpoint 上 residual严格为正

真实 numerator window为

\[
249/250<y<1,
\qquad
0<\tau\le10^{-11}.
\tag{6.1}
\]

由 (2.1)：

\[
\mathcal E
\ge
\frac{249}{250}(1474200-10836-19404)
-(84609+3240000+29160000)10^{-11}.
\]
因此

\[
\boxed{\mathcal E>1.438\times10^6.}
\tag{6.2}
\]

而由 (2.2) 粗界

\[
|\mathcal O|
<296+1764+8100+(2691+16200)10^{-11}+5500\cdot10^{-22}
<10161.
\tag{6.3}
\]

故

\[
120\sqrt y\,|\mathcal O|
<120\cdot10161
<1.220\times10^6.
\tag{6.4}
\]

由 (6.2)–(6.4)：

\[
\mathcal E>120\sqrt y\,|\mathcal O|,
\]
所以

\[
\boxed{
\mathcal R_{\rm src}^{(y)}>0.}
\tag{6.5}
\]

再由正 scaling (4.8)：

\[
\boxed{\mathscr R_{\rm src}>0.}
\tag{6.6}
\]

综合 §§5–6：

\[
\boxed{
\mathscr R_{\rm src}>0,
\qquad
\mathscr R_{\rm src}\equiv1\pmod8.}
\tag{6.7}
\]

---

## 7. odd-valuation projection prime 自动看到 source square class

固定 odd prime

\[
p\nmid120AS.
\]

若

\[
v_p(\mathscr R_{\rm src})\text{ 为奇数},
\]
令

\[
a=v_p(\mathscr E),
\qquad b=v_p(\mathscr O).
\]

若 `a!=b`，(4.7) 两项深度不同，立即有

\[
v_p(\mathscr R_{\rm src})=2\min(a,b),
\]
为偶数，矛盾。因此 `a=b=k`。

除去 `p^{2k}` 后，odd residual valuation强迫

\[
\left(\frac{\mathscr E/p^k}{120\,\mathscr O/p^k}\right)^2
\equiv AS\pmod p.
\tag{7.1}
\]

所以

\[
\boxed{AS\text{ 是模 }p\text{ 的平方}.}
\tag{7.2}
\]

因为 `S^2` 是平方，等价于

\[
\boxed{y=A/S\text{ 是模 }p\text{ 的平方}.}
\tag{7.3}
\]

这说明 `R_src` 的 odd-valuation prime不会来自普通 nonsquare projection；它们自动落到 source square-root sheet。若 `E,O` 本身同时被 `p` 整除，则 first-layer两 sign branch同时接触；若至少一个为单位，则 (7.1) 唯一选择其中一个 sign branch。

但必须保留边界：实际 source prime还要满足真实 `Phi_s` / `sigma` Hensel condition。`R_src` 只消去了 `x`，没有消去 source structural orbit。因此 (7.3) 不能把 `R_src` 的所有 inert prime都直接计入 `G_sp`。

---

## 8. 新的 generic source simple frontier

真正 source→common prime现在有两套互补的 global gate：

1. denominator-defect representative
   \[
   \widehat K_{\rm src}=K_{\rm src}/2^8\equiv3\pmod8,
   \]
   只依赖 `(H,M)`；
2. numerator/length residual
   \[
   \mathscr R_{\rm src}\equiv1\pmod8,
   \]
   只依赖 `(e,M)`。

并且 `spontaneous-source-depth-transfer.md` 把 `C_src` depth精确转移到 additive/common depth直至 source half-depth `h`。

因此 generic source common 已从原来的多变量 Hensel系统压成：

\[
\boxed{
\begin{array}{l}
\text{source structural orbit }(\Phi_s,\sigma),\\
\widehat K_{\rm src}(H,M),\\
\mathscr R_{\rm src}(e,M),\\
\text{以及 half-depth saturation}. 
\end{array}}
\]

下一步若要真正关闭 source pool，最值得研究的是这两个相反 mod-8 orientation 的 natural integers在同一个 source primary上的 gcd/allocation；继续做单独的 singular discriminant已无新增信息。
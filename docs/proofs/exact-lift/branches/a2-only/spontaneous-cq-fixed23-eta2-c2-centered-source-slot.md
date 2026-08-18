# A2 fixed `23` `eta=2` `c=2` 的 centered source-divisor slot

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`、`endpoint-lattice.md` §§5,9,13。
>
> **严格状态：**source-only certificate 使用旧的 `19L_*<theta<20L_*`。本文利用当前唯一 type 的 exact high-2 equality，把 `G=g/T` 从 generic plus slot进一步压到 `9.619–9.653`，进而收紧真实 prefix ratio `x`。代回 endpoint 的精确 Hensel quotient ratio后，得到 centered remainder `varrho=20L_*-theta` 的统一窄窗 `L_*/4<varrho<L_*/2`，等价于 `19.5L_*<theta<19.75L_*`。因此 source divisor search 的相对宽度从约 `5.26%` 降至约 `1.28%`。

---

## 1. exact high-2 equation for `G`

当前 type 为

\[
(d,c_Q,k_h,\varepsilon)
=(1,1587,1,+1).
\]

定义

\[
G:=\frac gT,
\qquad
\mathcal H:=\frac{H_0}{gT}
=J+\zeta,
\qquad
\zeta:=\frac{a_3}{T}.
\]

high-2 equality为

\[
H_0+Y_2=\frac{g^2}{2},
\]
其中

\[
Y_2=5c_Qa_2.
\]
又

\[
a_2=y10^{M-1},
\qquad
T^2=10^{2m}=10^{M+2}
\]
因为 `eta=2`。所以

\[
\frac{Y_2}{gT}
=\frac{c_Qy}{200G}.
\]
将 high-2 equality除以 `gT`：

\[
\mathcal H+
\frac{c_Qy}{200G}
=\frac G2.
\]
于是

\[
\boxed{
G^2-2\mathcal HG-
\frac{1587}{100}y=0.}
\tag{1.1}

正根关于 `mathcal H,y` 都严格递增。

---

## 2. `G` 的 type-specific 窄窗

已有 endpoint bounds：

\[
\boxed{
\frac{997}{250}<\mathcal H<\frac{1001}{250},}
\tag{2.1}

\[
\boxed{
\frac{249}{250}<y<1.}
\tag{2.2}

令

\[
P(G;H,y):=G^2-2HG-\frac{1587}{100}y.
\]
在 lower corner直接计算：

\[
P\!\left(
\frac{9619}{1000};
\frac{997}{250},
\frac{249}{250}
\right)
=-\frac{2503}{10^6}<0.
\tag{2.3}

因为正根右侧 `P` 才变正，得到

\[
G>\frac{9619}{1000}.
\]

在 upper corner：

\[
P\!\left(
\frac{9653}{1000};
\frac{1001}{250},1
\right)
=\frac{1837}{200000}>0,
\tag{2.4}

故

\[
G<\frac{9653}{1000}.
\]

所以

\[
\boxed{
\frac{9619}{1000}
<G<
\frac{9653}{1000}.}
\tag{2.5}

---

## 3. exact `x`–`G`–`w` relation

沿用

\[
x:=\frac{b_2}{10^M},
\qquad
w:=\frac{b_3}{10^m}.
\]
reflection denominator ratio为

\[
\frac{b_3}{b_2}=\frac{5c_Q}{g}.
\]
因此

\[
\frac wx
=\frac{5c_Q}{g}\,10^{M-m}.
\]
当前

\[
M-m=\lambda-1,
\qquad
g=GT=G10^{\lambda+1},
\]
所以

\[
\boxed{
\frac wx=\frac{c_Q}{20G}.}
\tag{3.1}

即

\[
\boxed{x=\frac{20Gw}{1587}.}
\tag{3.2}

已有

\[
\frac{837}{1000}<w<\frac{843}{1000}.
\tag{3.3}

结合 (2.5)：

\[
\boxed{
x>x_-:=
\frac{20}{1587}
\frac{9619}{1000}
\frac{837}{1000},}
\tag{3.4}

\[
\boxed{
x<x_+:=
\frac{20}{1587}
\frac{9653}{1000}
\frac{843}{1000}.}
\tag{3.5}

数值上只是帮助阅读：

\[
0.10146<x<0.10256.
\]
证明本身只使用 (3.4)–(3.5) 的精确有理数。

---

## 4. centered Hensel remainder进入 `(1/4,1/2)`

endpoint §9 有 exact ratio

\[
\boxed{
\frac\theta{L_*}
=\frac{2+10^{-M}w}{x},}
\tag{4.1}

以及 centered variable

\[
\boxed{\varrho:=20L_*-\theta.}
\tag{4.2}

因此

\[
\frac\varrho{L_*}
=20-rac{2+10^{-M}w}{x}.
\tag{4.3}

### lower bound

当前 source-window proof 已有 `M>=104`；其实 `M>=16` 已经足够。使用 `w<1`、`x>x_->1/10`：

\[
\frac{10^{-M}w}{x}<10^{1-M}<\frac1{1000}.
\]
所以

\[
\frac\theta{L_*}
<\frac2{x_-}+\frac1{1000}.
\]
精确有理比较给

\[
\frac2{x_-}+\frac1{1000}
<\frac{79}{4}.
\tag{4.4}

故

\[
\boxed{\frac\varrho{L_*}>\frac14.}
\tag{4.5}

### upper bound

由 (4.1) 的 numerator严格大于 `2`，且 `x<x_+`：

\[
\frac\theta{L_*}>rac2{x_+}.
\]
精确比较给

\[
20-rac2{x_+}<\frac12.
\tag{4.6}

故

\[
\boxed{\frac\varrho{L_*}<\frac12.}
\tag{4.7}

综上：

\[
\boxed{
\frac14L_*<\varrho<\frac12L_*.}
\tag{4.8}

---

## 5. source divisor interval同步收紧

由

\[
\theta=20L_*-\varrho,
\]
(4.8) 等价于

\[
\boxed{
\frac{39}{2}L_*
<\theta<
\frac{79}{4}L_*.}
\tag{5.1}

也就是

\[
\boxed{19.5L_*<\theta<19.75L_*.}
\]

相对宽度为

\[
\frac{19.75-19.5}{19.5}
=\frac1{78}
\approx1.28\%.
\]

所以 source-only certificate 中原条件

\[
19L_*<\theta<20L_*
\]
可严格替换成 (5.1)。

仍保留旧本原性

\[
\gcd(\varrho,L_*)=1.
\tag{5.2}

因此真实 source divisor现在必须同时满足：

\[
\boxed{
\theta\mid\mathscr S_\lambda(c_u),
\quad
\theta\text{ odd},
\quad
\frac{39}{2}L_*<\theta<\frac{79}{4}L_*,
\quad
\gcd(20L_*-\theta,L_*)=1.}
\tag{5.3}

---

## 6. 更新后的 certificate

对固定 `(lambda,c_u)`，后续 finite source check应只搜索 (5.3) 的窄 divisor interval，再做 `a_3` CRT representative test。`19–20` 的旧 slot不应继续作为当前 type 的最终搜索窗口。

这仍不证明所有高度的 divisor interval为空；新增的是 type-specific 的严格 centered compression。
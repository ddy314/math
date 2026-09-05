# A1 minimal diagonal: third-digit window gives an ultra-thin one-sided gap shell

> 日期：2026-08-22。
>
> 依赖：`decimal-height-synchronization.md`、`sharp-positive-tail-window`、`diagonal.md`。
>
> 范围：minimal diagonal `k=g>=32` 的 surviving single-5 top edge。事实上本文实估计只使用 minimal-diagonal 显式前缀和真实第三分子窗口。

状态：**本文结论已严格完成；top edge 尚未整体关闭。**

---

## 1. exact real center

令

\[
T=10^k,
\qquad
\rho=\frac{b_3}{10^n},
\qquad
\Gamma=T(N_0-\rho).
\]

minimal diagonal 中

\[
G=b_1,
\qquad D=TQ,
\]

并定义

\[
N=a_1^2+(a_2G)^2.
\]

定义 exact real center

\[
\boxed{
\Gamma_0
:=T\left(D+N_0-\frac{GC}{\sqrt N}\right).
}
\tag{1}
\]

等价地，若

\[
\rho_0:=\frac{GC}{\sqrt N}-D,
\]

则

\[
\Gamma_0=T(N_0-\rho_0).
\]

定义

\[
\boxed{
F_0:=G^2C^2-N(D+\rho)^2.
}
\tag{2}
\]

由 `rho=N0-Gamma/T` 与 (1)，差平方精确给

\[
\boxed{
F_0
=\frac{\sqrt N}{T}(\Gamma-\Gamma_0)
\left(GC+\sqrt N(D+\rho)\right).
}
\tag{3}
\]

所以 `F0` 的符号恰等于 `Gamma-Gamma0` 的符号。

---

## 2. 第三 normalized numerator 的 exact quadratic

真实第三块的 normalized numerator 为

\[
\boxed{x:=\frac{a_3}{10^n},}
\]

且 digit window 给

\[
\boxed{\frac1{10}\le x<1.}
\tag{4}
\]

直接从 exact concatenation equation

\[
\left(\frac{C+x}{D+\rho}\right)^2
=\frac N{G^2}+\frac{x^2}{\rho^2}
\]

清分母并整理，得到

\[
\boxed{
F_0
=\frac{G^2D(D+2\rho)}{\rho^2}x^2
-2G^2Cx.
}
\tag{5}
\]

---

## 3. quadratic 的正项严格小于 `G^2 C`

sharp positive-tail window 给

\[
0<\Gamma<39.003,
\qquad
N_0\ge T/10,
\]

故当前 `T>=10^32` 时安全地有

\[
\boxed{\rho>T/11.}
\tag{6}
\]

minimal diagonal 显式前缀满足

\[
C>1000T^5.
\tag{7}
\]

又

\[
D<100T^3,
\qquad
D+2\rho<101T^3.
\tag{8}
\]

所以

\[
\frac{D(D+2\rho)}{\rho^2C}
<
\frac{(100T^3)(101T^3)}{(T/11)^2(1000T^5)}
=rac{1222.1}{T}<1.
\]

因此

\[
\boxed{
\frac{G^2D(D+2\rho)}{\rho^2}<G^2C.
}
\tag{9}
\]

---

## 4. `Gamma` 必在 `Gamma0` 左侧，且距离小于 `2/(9T)`

由 (4),(5),(9)：

\[
0<
\frac{G^2D(D+2\rho)}{\rho^2}x^2
<G^2Cx^2
<2G^2Cx.
\]

故

\[
\boxed{F_0<0}
\tag{10}
\]

并且

\[
\boxed{|F_0|<2G^2C.}
\tag{11}
\]

由 (3),(10)：

\[
\boxed{\Gamma<\Gamma_0.}
\tag{12}
\]

再由 (3),(11)，并仅用

\[
GC+\sqrt N(D+\rho)>GC,
\]

得到

\[
\Gamma_0-\Gamma
<\frac{2TG^2C}{\sqrt N\,GC}
=\frac{2TG}{\sqrt N}.
\tag{13}
\]

而

\[
N=a_1^2+(a_2G)^2>(a_2G)^2,
\]

所以

\[
\frac G{\sqrt N}<\frac1{a_2}.
\]

minimal diagonal 中

\[
a_2=10T^2-z>9T^2.
\]

代入 (13)：

\[
\boxed{
0<\Gamma_0-\Gamma
<\frac{2T}{a_2}
<\frac{2}{9T}.
}
\tag{14}
\]

---

## 5. consequence

此前 typewise continuous contact window 的宽度是绝对常数级。真实 third-numerator digit window 进一步把任何 top-edge candidate 压到 exact center `Gamma0` 左侧的

\[
\boxed{O(T^{-1})}
\]

薄壳：

\[
\boxed{
\Gamma_0-\frac{2}{9T}<\Gamma<\Gamma_0.
}
\]

当前 `k>=32` 时该宽度小于 `2.3e-33`。

下一步应把 `Gamma0` 的 minimal-diagonal 显式展开与

\[
\Gamma=\gamma/5^B
\]

的 exact 5-adic phase 联立；单独的“区间很窄”只给唯一性，不自动给空性，因此本文不声称 top edge 已关闭。
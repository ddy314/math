# DD corrected terminal 的 `m,d` neighborhood geometry

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-high-funnel-quantitative-defect-2026-08-22.md`](dd-corrected-high-funnel-quantitative-defect-2026-08-22.md)。
>
> **严格状态：已严格完成（corrected canonical high-funnel 的渐近 neighborhood consequence）。**

## 1. 基线

令

\[
a=\log_{10}2,
\qquad
A=\frac{2(1+2a)}3,
\qquad
\lambda=\frac{2+a}{1+2a},
\]

\[
c_*=2+3\lambda
=6.308883577618031\ldots,
\]

\[
M_*:=\frac3A
=2.808883577618031\ldots.
\]

定义 slope defect

\[
\boxed{\delta:=c_*-\mathcal N,\qquad \mathcal N=n/S.}
\]

上一文件给

\[
\delta\ge
\lambda\sigma_S
+c_{Q_2}Q_2+c_{N_2}N_2+c_{Q_5}Q_5+c_{G_5}G_5+c_{N_5}N_5+c_RR-o(1),
\tag{1.1}
\]

其中所有 coefficient 为正。

Schmidt budget deficit恰为

\[
3-AM
=\sigma_S
+2aQ_2+aN_2
+\frac{2b}{3}Q_5
+\frac{4b}{3}G_5
+\frac b3N_5
+2R,
\tag{1.2}
\]

其中 `b=1-a`。

## 2. coefficient-wise domination

逐项比较 `(1.2)` 与 `A*(1.1)`：

\[
A\lambda>1,
\]

\[
A(2a\lambda)\ge2a,
\qquad
A(a\lambda)\ge a,
\]

\[
A\frac{2b(\lambda+1)}3\ge\frac{2b}3,
\]

而对 `G_5` 与 `R` 恰有临界等号：

\[
\boxed{
A\frac{2b(2\lambda-1)}3=\frac{4b}3,
\qquad
A(2\lambda-1)=2.
}
\tag{2.1}
\]

因此由所有 variables 非负：

\[
\boxed{
3-AM\le A\delta+o(1).
}
\tag{2.2}
\]

另一方面 Schmidt budget本身给

\[
AM\le3+o(1).
\]

所以

\[
0\le M_*-M
=\frac{3-AM}{A}
\le\delta+o(1).
\]

即

\[
\boxed{
M_*-\delta-o(1)
\le M\le M_*+o(1).
}
\tag{M-window}
\]

## 3. `d/S` 被同一 `delta` 窗口锁住

令

\[
D:=d/S=\mathcal N-M.
\]

注意

\[
c_*-M_*=\frac72.
\]

写

\[
\mu:=M_*-M,
\qquad 0\le\mu\le\delta+o(1).
\]

于是

\[
D=(c_*-\delta)-(M_*-\mu)
=\frac72-\delta+\mu.
\]

故

\[
\boxed{
\frac72-\delta-o(1)
\le\frac dS
\le\frac72+o(1).
}
\tag{D-window}
\]

这比单纯的 equality rigidity 更强：若 slope 离 `c_*` 只有 `delta`，第三 numerator surplus 的 normalized 位置只能落在长度 `delta+o(1)` 的区间中。

## 4. `T/S` 的粗显式邻域

corrected resonance给

\[
\frac TS=\frac{2M+2Q_5-2G_5+N_5}{3}.
\]

terminal 值为

\[
T_*:=\frac{2M_*}{3}=1.872589051745354\ldots.
\]

利用上一文件逐项 bounds 与 `|M-M_*|<=delta+o(1)`，安全得到

\[
\boxed{
\left|\frac TS-T_*\right|
\le2.606\,\delta+o(1).
}
\tag{T-window}
\]

这里 `2.606` 只是方便使用的向上圆整常数，不声称最优。

## 5. 用途

`M-window` 与 `D-window` 允许把原本只在 exact equality sequence 中使用的 terminal estimates改写成 `delta`-neighborhood estimates：

- decimal tail length `m` 只有 `O(delta S)` 的相对自由度；
- surplus `d` 被锁在 `3.5S+O(delta S)`；
- 5-adic exponent `T` 也只有 `O(delta S)` 偏移。

若后续 Farey / Top-residue / Gaussian moving-core theorem能够在这些参数偏移 `O(delta S)` 时保持一个固定正 surplus，就可与 `(Quantitative-defect)` 闭合成 explicit slope gap。

## 6. 状态摘要

- **已严格完成：** `M-window`、`D-window`；`T-window` 的安全常数。
- **新目标：** 将 exact equality terminal 的 Farey / decimal remainder machinery量化到 `delta`-neighborhood。
- **未证明：** uniform positive `delta` gap、DD strict improvement、空性或有效绝对高度界。

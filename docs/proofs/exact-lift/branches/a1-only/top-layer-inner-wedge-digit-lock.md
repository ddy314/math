# A1 top layer: exact leading-decimal lock in the inner wedge

> 日期：2026-08-22。
>
> 依赖：`top-layer-inner-wedge-uniform-phase.md`。
>
> 范围：
> \[
> d=2,\qquad r=s=1,
> \]
> 令
> \[
> u:=2g-k,
> \qquad 1\le u\le g-1,
> \qquad
> H:=10^g,
> \qquad
> \tau:=10^{g-u}=H/10^u.
> \]

状态：**已严格完成。**

uniform phase theorem 给
\[
\boxed{
0<(J+1)\tau-\rho
<\frac{40\cdot10^u}{H^2}.
}
\tag{1}
以及 slope window
\[
\boxed{H/10\le\rho<H.}
\tag{2}

本文把原先的粗界 `J+1<1.1*10^u` 精确收紧成
\[
\boxed{10^{u-1}<J+1\le10^u.}
\tag{3}

---

## 1. lower decimal digit count

由 (1)：
\[
(J+1)\tau>\rho.
\]
再由 (2)：
\[
(J+1)\tau>H/10.
\]
代入 `tau=H/10^u`：
\[
J+1>10^{u-1}.
\]
这给 (3) 的下界。

---

## 2. upper decimal digit count

反设
\[
J+1\ge10^u+1.
\]
则
\[
(J+1)\tau
\ge H+\tau.
\]
而 `rho<H`，所以
\[
(J+1)\tau-\rho>\tau.
\tag{4}

在整个 inner wedge `u<=g-1` 中
\[
\tau=10^{g-u}\ge10.
\]
另一方面 (1) 的上界满足
\[
\frac{40\cdot10^u}{H^2}
=40\cdot10^{u-2g}
\le4\cdot10^{-g-1}<1.
\]
与 (4) 矛盾。

因此
\[
J+1\le10^u.
\]

---

## 3. interpretation

综上
\[
\boxed{10^{u-1}<J+1\le10^u.}
\]
所以 `J+1` 恰有 `u` 个十进制位。

而 (1) 还可写成
\[
\rho=(J+1)10^{g-u}+O(10^{u-2g}),
\]
因此 `J+1` 不是任意 moving residue；它就是第三尾斜率 `rho` 的 leading `u`-digit block。

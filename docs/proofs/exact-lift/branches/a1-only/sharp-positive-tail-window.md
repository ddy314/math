# A1 minimal diagonal: sharpened positive tail window

> 日期：2026-08-19。本文继续 `positive-tail-residual.md`，仍处于
> \[
> d=2,\qquad r=s=1,\qquad k=g\ge3.
> \]
> 记
> \[
> \rho=\frac{b_3}{10^\ell},\qquad N_0=j-10^k+1.
> \]

本文把旧的统一窗口

\[
5.09\,10^{-k}<N_0-\rho<50.45\,10^{-k}
\]

严格加强为

\[
\boxed{
15.09\,10^{-k}<N_0-\rho<39.003\,10^{-k}.
}
\tag{1}
\]

等价地，归一化 gap

\[
\Gamma_k:=10^k(N_0-\rho)
\]

必须满足

\[
\boxed{15.09<\Gamma_k<39.003.}
\tag{2}
\]

状态：**已严格完成。**

---

## 1. 输入

沿用前文记号

\[
\delta=10^{-k},\qquad \varepsilon=10^{-2k},
\]

\[
X=1+\sigma-\delta,\qquad 1.099<X<2,
\]

\[
c=5-z,
\qquad
(z,w)\in\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\}.
\]

已有精确关系

\[
10u=(50-5w\varepsilon)E-cw\varepsilon,
\tag{3}
\]

以及

\[
10u-X=\frac{N_0-\rho}{10^k}.
\tag{4}
\]

第一 positive source 已有双侧界

\[
0.02X-0.0121\varepsilon<S_1<0.02X+0.0504\varepsilon.
\tag{5}
\]

全 excess 为

\[
E=S_1+S_2+
\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
+\varepsilon^2\phi_1^2,
\tag{6}
\]

其中

\[
0<S_2<\varepsilon^2,
\qquad 0<\phi_1<0.434=\frac{217}{500},
\qquad \phi_2=\frac z{10}.
\tag{7}
\]

---

## 2. 类型相关曲率下界

函数

\[
f_z(x)=2x+\left(\frac z{10}\right)^2-x^2
\]

在 `0<x<1` 上严格递增。

### `z=1`

此时 `c=4` 且 `phi_1>0.4`，故

\[
f_1(\phi_1)>f_1(0.4)=0.65.
\tag{8}
\]

结合 (5)-(6) 中其余非负项：

\[
\boxed{E>0.02X+0.6379\varepsilon.}
\tag{9}
\]

### `z=3`

此时 `c=2` 且 `phi_1>0.2`，故

\[
f_3(\phi_1)>f_3(0.2)=0.45,
\]

从而

\[
\boxed{E>0.02X+0.4379\varepsilon.}
\tag{10}
\]

旧证明把 `cw<=16` 与曲率 `>0.45` 同时使用，但这两个最坏情况不能发生在同一类型；本文正是保留这点互斥信息。

---

## 3. 下界提高到 `15.09`

令

\[
a_z=
\begin{cases}
0.6379,&z=1,\\
0.4379,&z=3.
\end{cases}
\]

由 (3) 与 (9)-(10)：

\[
\begin{aligned}
10u-X
&>(50-5w\varepsilon)(0.02X+a_z\varepsilon)
-cw\varepsilon-X\\
&=\varepsilon
\left(
50a_z-cw-0.1wX-5wa_z\varepsilon
\right).
\end{aligned}
\tag{11}
\]

使用 `X<2` 与 `epsilon<=10^-6`，六类型的安全下界分别为：

| `(z,w)` | `(10u-X)/epsilon` 的严格下界 |
|---|---:|
| `(1,1)` | `>27.6949968` |
| `(1,2)` | `>23.4949936` |
| `(1,3)` | `>19.2949904` |
| `(1,4)` | `>15.0949872` |
| `(3,1)` | `>19.6949978` |
| `(3,2)` | `>17.4949956` |

因此统一有

\[
\boxed{10u-X>15.09\varepsilon.}
\tag{12}
\]

由 (4) 且 `epsilon=10^{-2k}`：

\[
\boxed{N_0-\rho>15.09\,10^{-k}.}
\tag{13}
\]

---

## 4. 曲率上界也按类型收紧

由于 `f_z` 在当前区间递增，并且 `phi_1<217/500`：

\[
f_1(\phi_1)
<2\frac{217}{500}+\frac1{100}
-\left(\frac{217}{500}\right)^2
=0.689644,
\tag{14}
\]

\[
f_3(\phi_1)
<2\frac{217}{500}+\frac9{100}
-\left(\frac{217}{500}\right)^2
=0.769644.
\tag{15}
\]

由 (5)-(7)：

\[
E<0.02X+A_z\varepsilon+1.189\varepsilon^2,
\tag{16}
\]

其中

\[
A_1=0.0504+0.689644=0.740044,
\]

\[
A_3=0.0504+0.769644=0.820044.
\]

---

## 5. 上界降低到 `39.003`

把 (16) 代入 (3)。在求上界时丢掉所有负 correction，可得

\[
\frac{10u-X}{\varepsilon}
<50A_z+50(1.189)\varepsilon-cw.
\tag{17}
\]

因 `epsilon<=10^-6`，六类型右侧最大值发生在 `(z,w)=(3,1)`：

\[
50(0.820044)+50(1.189)10^{-6}-2
=39.00225945
<39.003.
\tag{18}
\]

因此

\[
\boxed{10u-X<39.003\varepsilon,}
\tag{19}
\]

再由 (4)：

\[
\boxed{N_0-\rho<39.003\,10^{-k}.}
\tag{20}
\]

(13) 与 (20) 即给出主结论 (1)。

---

## 6. 对后续 finite-box / gap-desert 的意义

以后所有 minimal-diagonal fixed-layer certificate 都只需排除

\[
\boxed{15.09<10^k(\lceil\rho\rceil-\rho)<39.003.}
\tag{21}
\]

这里 `ceil(rho)=N_0` 由正号定理保证。

这个新窗口完全由连续几何与 prefix 类型信息推出，不使用任何 `k` 的有限枚举，因此可以直接作为全部 `k>=3` 的统一输入。
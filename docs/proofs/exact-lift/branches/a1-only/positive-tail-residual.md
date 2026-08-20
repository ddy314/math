# A1 minimal diagonal positive tail residual

> 日期：2026-08-19。本文继续 `near-integer-tail.md`。仍处于
> \[
> d=2,\qquad r=s=1,\qquad k=g\ge3.
> \]
> 记
> \[
> \rho=\frac{b_3}{10^\ell},\qquad
> N_0=j-10^k+1\in\mathbf Z.
> \]

本文把上一轮 near-integer 窗的符号彻底确定下来。核心结论是

\[
\boxed{
5.09\,10^{-k}
< N_0-\rho
<50.45\,10^{-k}.
}
\tag{1}
\]

因此 `rho` 永远严格位于整数 `N_0` 的左侧。特别地：

\[
\boxed{\text{minimal diagonal 的 saturated sector 在 }k\ge3\text{ 全部为空。}}
\tag{2}
\]

把误差乘回 `10^ell` 后，整数 residual

\[
 t=N_0 10^\ell-b_3
\]

满足

\[
\boxed{
5.09\,10^{\ell-k}<t<50.45\,10^{\ell-k}.
}
\tag{3}
\]

于是

\[
\boxed{\ell\le k-2\Longrightarrow\text{无候选},}
\tag{4}
\]

并且第一条可能的尾长边界 `ell=k-1` 精确只剩

\[
\boxed{t\in\{1,2,3,4,5\}.}
\tag{5}
\]

状态：**已严格完成。**

---

## 1. 输入与记号

沿用 `near-integer-tail.md`：

\[
\delta=10^{-k},\qquad
\varepsilon=10^{-2k}=\delta^2,
\]

\[
\sigma=\frac{\rho}{10^k}\in[0.1,1),
\qquad
u=\frac{j}{10^{k+1}},
\]

并定义

\[
\boxed{X=1+\sigma-\delta.}
\tag{6}
\]

minimal diagonal 的精确 gap/excess 关系为

\[
\boxed{
 u
=5E-\frac{w\varepsilon}{2}E
-\frac{cw\varepsilon}{10},
\qquad c=5-z\in\{4,2\}.
}
\tag{7}
\]

positive excess decomposition 写成

\[
E=S_1+S_2+
\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
+\varepsilon^2\phi_1^2,
\tag{8}
\]

其中 `S_2>=0`，而 `near-integer-tail.md` 已严格证明第一 source

\[
\boxed{
S_1>0.02X-0.0121\varepsilon.
}
\tag{9}
\]

上一轮为了得到双侧误差窗，没有使用曲率项的正下界。这里正是把它补回来。

---

## 2. 曲率项有统一的 `0.45 epsilon` 正供给

在 diagonal 中

\[
\phi_2=\frac z{10}
\]

且

\[
\phi_1=\frac{c+u}{10-w\varepsilon}.
\]

因为 `u>0`、`w epsilon>0`，有

\[
\phi_1>\frac c{10}.
\]

另一方面既有 half-gap kernel 给出

\[
\phi_1<0.434<1.
\]

对固定 `phi_2`，函数

\[
f(x)=2x+\phi_2^2-x^2
\]

在 `0<x<1` 上严格递增。

### `z=1`

此时

\[
c=4,\qquad \phi_2=0.1,\qquad \phi_1>0.4,
\]

故

\[
2\phi_1+\phi_2^2-\phi_1^2
>0.8+0.01-0.16
=0.65.
\]

### `z=3`

此时

\[
c=2,\qquad \phi_2=0.3,\qquad \phi_1>0.2,
\]

故

\[
2\phi_1+\phi_2^2-\phi_1^2
>0.4+0.09-0.04
=0.45.
\]

所以六个 prefix 类型统一满足

\[
\boxed{
2\phi_1+\phi_2^2-\phi_1^2>0.45.
}
\tag{10}
\]

结合 (8)、`S_2>=0`、最后一项非负以及 (9)：

\[
\boxed{
E>0.02X+0.4379\varepsilon.
}
\tag{11}
\]

这是决定 residual 符号的关键强化。

---

## 3. `10u-X` 严格为正

由精确式 (7)：

\[
10u=(50-5w\varepsilon)E-cw\varepsilon.
\]

因此

\[
10u-X
=(50-5w\varepsilon)E-cw\varepsilon-X.
\]

把 (11) 代入。由于 `50-5w epsilon>0`：

\[
\begin{aligned}
10u-X
&>(50-5w\varepsilon)
  (0.02X+0.4379\varepsilon)
  -cw\varepsilon-X\\
&=\varepsilon
\left(
21.895-cw-0.1wX-2.1895w\varepsilon
\right).
\end{aligned}
\tag{12}
\]

六类型中

\[
c\le4,\qquad w\le4,
\]

而

\[
X=1+\sigma-\delta<2.
\]

并且 `k>=3` 给出

\[
\varepsilon\le10^{-6}.
\]

故括号中的量严格大于

\[
21.895-16-0.8-2.1895\cdot4\cdot10^{-6}
>5.09.
\]

于是

\[
\boxed{
10u-X>5.09\varepsilon.
}
\tag{13}
\]

---

## 4. 转回原始 near-integer residual

由定义

\[
10u-X
=
\frac{j}{10^k}
-1
-\frac\rho{10^k}
+10^{-k}
=
\frac{N_0-\rho}{10^k}.
\]

所以 (13) 乘以 `10^k` 得

\[
\boxed{
N_0-\rho>5.09\,10^{-k}.
}
\tag{14}
\]

另一方面 `near-integer-tail.md` 已证明旧上界

\[
N_0-\rho<50.45\,10^{-k}.
\tag{15}
\]

合并即得到主结论 (1)：

\[
\boxed{
5.09\,10^{-k}
<N_0-\rho
<50.45\,10^{-k}.
}
\]

特别地

\[
\boxed{\rho<N_0.}
\tag{16}
\]

---

## 5. saturated sector 全部消失

saturated `L=1` 的定义是

\[
10^\ell\mid b_3.
\]

于是

\[
\rho=\frac{b_3}{10^\ell}\in\mathbf Z.
\]

同时 `N_0` 也是整数。

但对 `k>=3`，(1) 给出

\[
0<N_0-\rho<50.45\cdot10^{-3}<1.
\]

两个整数之差不可能严格落在 `(0,1)` 中。因此

\[
\boxed{
L=1\text{ 在 minimal diagonal }k\ge3\text{ 中为空。}
}
\tag{17}
\]

这比此前 `short-tail-saturation.md` 的“`ell<=k-2` 强制进入 saturated”更强：被强制进入的 saturated 状态本身已经不可能存在。

---

## 6. 整数 residual 的统一正窗

定义

\[
\boxed{
 t=N_0 10^\ell-b_3
=(N_0-\rho)10^\ell\in\mathbf Z.
}
\tag{18}
\]

由 (1)：

\[
\boxed{
5.09\,10^{\ell-k}
<t
<50.45\,10^{\ell-k}.
}
\tag{19}
\]

并且

\[
\boxed{t>0.}
\tag{20}
\]

### `ell<=k-2`

此时

\[
t<50.45\cdot10^{-2}=0.5045.
\]

与 `t` 为正整数矛盾。因此

\[
\boxed{
\ell\le k-2\Longrightarrow\text{无候选。}
}
\tag{21}
\]

所以任何剩余 candidate 必须满足

\[
\boxed{\ell\ge k-1.}
\tag{22}
\]

### `ell=k-1`

由 (19)：

\[
0.509<t<5.045.
\]

故

\[
\boxed{t\in\{1,2,3,4,5\}.}
\tag{23}
\]

### `ell=k`

同理：

\[
5.09<t<50.45,
\]

所以

\[
\boxed{t\in\{6,7,\ldots,50\}.}
\tag{24}
\]

这说明 genuinely-long tail 也不是完全连续的自由参数；每个固定 `ell-k` 都落在一个明确的有限 residual shell 中。

---

## 7. 对当前前沿的意义

结合 `k=1,2,3,4,5` 已有有限证书，当前无界 minimal diagonal 从此可以直接假设

\[
\boxed{k=g\ge6.}
\]

而第三尾同时满足

\[
\boxed{L>1,\qquad \ell\ge k-1,\qquad t>0.}
\]

第一条边界进一步只有

\[
\boxed{
ell=k-1,
\qquad
t\in\{1,2,3,4,5\}.
}
\]

因此下一步无需再研究 saturated short-tail；应直接攻击这五个 boundary residual，然后进入 `ell>=k` 的正 residual shells。
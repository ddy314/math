# A1 minimal diagonal: explicit rational phase shell of width three

> 日期：2026-08-22。
>
> 依赖：`deep-single5-topedge-ultrathin-gap.md`、`diagonal.md`。
>
> 范围：minimal diagonal `k=g>=32` 的 surviving single-5 top edge。

状态：**本文结论已严格完成；top edge 尚未整体关闭。**

---

## 1. minimal-diagonal 显式前缀

令

\[
T=10^k,
\qquad s_0:=\frac{N_0}{T},
\qquad \frac1{10}\le s_0<1.
\]

minimal diagonal 的显式式为

\[
G=10T^2-w,
\]

\[
Q=100T^2-(10w-1),
\qquad D=TQ,
\]

\[
a_2=10T^2-z,
\]

以及

\[
\boxed{
a_1
=100T^3+igl(10(5-z-w)+1\bigr)T+N_0-1.
}
\tag{1}
\]

于是

\[
C=10T^2a_1+a_2,
\qquad
N=a_1^2+(a_2G)^2.
\]

沿用

\[
\rho=N_0-\Gamma/T,
\]

\[
F_0(\Gamma):=G^2C^2-N(D+\rho)^2.
\]

`deep-single5-topedge-ultrathin-gap.md` 定义 exact real center

\[
\Gamma_0
=T\left(D+N_0-\frac{GC}{\sqrt N}\right),
\]

并已证明真实 candidate 满足

\[
\boxed{
0<\Gamma_0-\Gamma<\frac{2}{9T}.
}
\tag{2}
\]

---

## 2. 显式 rational 主中心

定义

\[
\boxed{
\Gamma_*
:=
\frac{
(15-z)s_0+10wz-50w-51z+390
}{10}.
}
\tag{3}
\]

也就是：

### `z=1`

\[
\boxed{
\Gamma_*=33.9-4w+1.4s_0.
}
\tag{4}
\]

### `z=3`

\[
\boxed{
\Gamma_*=23.7-2w+1.2s_0.
}
\tag{5}
\]

下面证明 `Gamma*` 位于 exact center `Gamma0` 的右侧，而且两者只差 `O(1/T)`。

---

## 3. exact expansion 在 `Gamma*` 处的首项

把 (1) 与 `N0=s0*T` 直接代入

\[
T^2F_0(\Gamma)
=T^2\left(G^2C^2-N(D+N_0-\Gamma/T)^2\right)
\]

并按 `T` 收集。

`T^12` 的系数精确为

\[
200000\left(
10\Gamma+s_0z-15s_0-10wz+50w+51z-390
\right).
\]

所以定义 (3) 正好令该最高项消失。

在 `Gamma=Gamma*` 时，下一项 `T^11` 的系数精确为

\[
\boxed{2\,000\,000-200\,000z.}
\tag{6}
\]

六类型中 `z in {1,3}`，故

\[
\boxed{
1\,400\,000
\le
2\,000\,000-200\,000z
\le
1\,800\,000.
}
\tag{7}
\]

其余各 `T^d`, `0<=d<=10`, 系数只含 `s0,z,w`。在安全盒

\[
0\le s_0\le1,
\qquad |z|\le3,
\qquad |w|\le4
\]

中，逐项三角估计可取以下统一绝对上界：

| degree `d` | coefficient absolute bound |
|---:|---:|
| 10 | 180,800,000 |
| 9 | 5,332,000 |
| 8 | 485,904,300 |
| 7 | 3,916,400 |
| 6 | 309,745,646 |
| 5 | 5,643,828 |
| 4 | 156,821,136 |
| 3 | 1,439,062 |
| 2 | 127,490,107 |
| 1 | 1,893,833 |
| 0 | 1,125,434 |

这些上界之和小于

\[
1.3\times10^9.
\]

因此写

\[
T^2F_0(\Gamma_*)
=(2\,000\,000-200\,000z)T^{11}+R,
\]

有

\[
\boxed{|R|<1.3\times10^9T^{10}.}
\tag{8}
\]

当前 `T>=10^32`，由 (7)-(8) 立即得到

\[
\boxed{F_0(\Gamma_*)>0}
\tag{9}
\]

以及安全上界

\[
\boxed{F_0(\Gamma_*)<2\times10^6T^9.}
\tag{10}
\]

---

## 4. `Gamma0<Gamma*` 且距离小于 `25/(9T)`

与 ultra-thin gap 文件相同，差平方恒等式给

\[
F_0(\Gamma_*)
=\frac{\sqrt N}{T}(\Gamma_*-\Gamma_0)
\left(GC+\sqrt N(D+\rho_*)\right),
\]

其中

\[
\rho_*:=N_0-\Gamma_*/T.
\]

由 (9)：

\[
\boxed{\Gamma_*>\Gamma_0.}
\tag{11}
\]

又

\[
\sqrt N>a_2G>81T^4,
\]

\[
GC>9000T^7,
\]

所以

\[
\sqrt N\,GC>729000T^{11}.
\]

由 (10)：

\[
0<\Gamma_*-\Gamma_0
<\frac{T(2\times10^6T^9)}{729000T^{11}}
<\frac{25}{9T}.
\tag{12}
\]

---

## 5. 宽度三的 rational phase shell

合并 (2),(11),(12)：

\[
0<\Gamma_* -\Gamma
=(\Gamma_*-\Gamma_0)+(\Gamma_0-\Gamma)
<\frac{25}{9T}+\frac{2}{9T}
=\frac3T.
\]

因此

\[
\boxed{
0<\Gamma_* -\Gamma<\frac3T.
}
\tag{13}
\]

乘以 `T`，并使用 `s0=N0/T`：

### `z=1`

\[
\boxed{
0<
\frac{14N_0+(339-40w)T}{10}
-T\Gamma
<3.
}
\tag{14}
\]

### `z=3`

\[
\boxed{
0<
\frac{12N_0+(237-20w)T}{10}
-T\Gamma
<3.
}
\tag{15}
\]

single-5 中

\[
\Gamma=\frac\gamma{5^B},
\]

故

\[
\boxed{
T\Gamma=\frac{2^k\gamma}{5^{B-k}}.
}
\tag{16}
\]

所以 (14)-(15) 是一个只含整数 `T,N0,gamma,k,B,z,w` 的绝对宽度 `3` rational phase condition。

---

## 6. integer remainder form

令

\[
d:=B-k\ge1.
\]

定义

\[
A_{z,w}:=
\begin{cases}
14N_0+(339-40w)T,&z=1,\\
12N_0+(237-20w)T,&z=3.
\end{cases}
\]

则 (14)-(16) 等价于存在正整数

\[
\boxed{
E:=5^dA_{z,w}-10\,2^k\gamma
}
\tag{17}
\]

满足

\[
\boxed{
0<E<30\,5^d.
}
\tag{18}
\]

这是真正的固定宽度相位 remainder。后续应把 (17)-(18) 与：

- gap identity；
- `gamma` 的 2/5-unit class；
- `N0` 的 local residue locks；
- top-edge `u|s+2*5^(B+2k)v`

联立。

注意 (18) 本身只给小余数，不自动给空性；本文不据此声称 top edge 已关闭。
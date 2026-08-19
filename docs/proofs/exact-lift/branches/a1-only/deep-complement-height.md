# A1 minimal diagonal: deep complement-quotient height bound

> 日期：2026-08-19。依赖 `gap-denominator-normal-form.md`、minimal-diagonal odd-prime supply 与 `deep-gap-valuation-normal-form.md`。
> 当前真正需要统一处理的范围已经可取 `k=g>=31`，因为 `k<=30` 有 fixed-layer certificates，而 central denominator 在全部 `k>=26` 上已由 `central-modular-exhaustion.md` 关闭。

本文给 deep denominator sector 一个新的全局高度约束。核心不是继续枚举 `(A,B)`，而是研究 odd-prime supply 的**补因子**

\[
M:=\frac{Qb_1}{h}\in\mathbf Z_{>0}.
\]

最终得到一个非常强的 rational-approximation necessary condition。特别地，在 double-deep `A,B>0` 中：

\[
\boxed{
2^{\min(A+e+\nu_2,3k)}
5^{\min(B+\nu_5,3k)}
<390100\,10^k,
}
\]

其中

\[
e=v_2(w),
\qquad\nu_2=v_2(N_0),
\qquad\nu_5=v_5(N_0).
\]

这把原来的无界二维 deep lattice 压入一个显式线性高度带。

状态：**已严格完成。**

---

## 1. general deep numerator identity

沿用 reduced normalized gap

\[
\Gamma_k=10^k(N_0-\rho)
=\frac{\gamma}{2^A5^B},
\qquad
15.09<\Gamma_k<39.003.
\]

记

\[
T=10^k,
\qquad
D=2^A5^B.
\]

若某一素数侧不 deep，则该侧可能仍在 `rho=h2^x5^y` 的分子中。定义

\[
\lambda_2=
\begin{cases}
0,&A>0,\\
k+x,&A=0,
\end{cases}
\qquad
\lambda_5=
\begin{cases}
0,&B>0,\\
k+y,&B=0,
\end{cases}
\]

以及

\[
\boxed{\lambda=2^{\lambda_2}5^{\lambda_5}.}
\]

由定义直接有

\[
D T(N_0-\rho)=\gamma,
\]

而

\[
D T\rho=h\lambda.
\]

所以

\[
\boxed{
DTN_0-\gamma=h\lambda.}
\tag{1}
\]

这是 central decimal equation 在任意 deep sector 中的统一替代式。

---

## 2. 引入 supply complement `M`

minimal-diagonal odd supply 给

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1,
\]

故至少有

\[
\boxed{h\mid Qb_1.}
\]

定义

\[
\boxed{M:=\frac{Qb_1}{h}\in\mathbf Z_{>0}.}
\tag{2}
\]

又

\[
Qb_1
=1000T^4+10(1-20w)T^2+C_0,
\qquad
C_0=w(10w-1).
\tag{3}
\]

由 (1)-(2)：

\[
MD(TN_0-\Gamma_k)
=M(DTN_0-\gamma)
=Mh\lambda
=Qb_1\lambda.
\]

所以定义

\[
\boxed{
\mu:=\frac{MD}{\lambda T^2}}
\tag{4}
\]

后，有精确恒等式

\[
\boxed{
\mu(TN_0-\Gamma_k)
=\frac{Qb_1}{T^2}.}
\tag{5}
\]

---

## 3. `mu` 永远落在固定区间 `(1000,10001)`

因为 `rho` 有 `k` 位且 `0<N_0-rho<1`，有

\[
\frac T{10}<N_0\le T.
\tag{6}
\]

首先证明下界。由 `N_0<=T`：

\[
1000T^2(TN_0-\Gamma_k)
\le1000T^2(T^2-\Gamma_k).
\]

而由 (3)：

\[
\begin{aligned}
Qb_1-1000T^2(T^2-\Gamma_k)
={}&\bigl(1000\Gamma_k+10(1-20w)\bigr)T^2+C_0.
\end{aligned}
\]

使用

\[
\Gamma_k>15.09,
\qquad w\le4,
\]

括号严格大于

\[
15090-790=14300.
\]

所以

\[
Qb_1>1000T^2(TN_0-\Gamma_k),
\]

结合 (5)：

\[
\boxed{\mu>1000.}
\tag{7}
\]

再证上界。由

\[
Qb_1<1000T^4
\]

以及

\[
TN_0-\Gamma_k>rac{T^2}{10}-39.003,
\]

得到

\[
\mu
<\frac{1000T^2}{T^2/10-39.003}
=\frac{10000}{1-390.03/T^2}.
\]

当前 `k>=31`，当然严格小于 `10001`；事实上 `k>=4` 已足够。因此

\[
\boxed{1000<\mu<10001.}
\tag{8}
\]

---

## 4. 得到 `O(T^-2)` 的超近有理逼近

把 (3) 代回 (5)：

\[
\mu TN_0-\mu\Gamma_k
=1000T^2+10(1-20w)+\frac{C_0}{T^2}.
\]

除以 `T^2`：

\[
\boxed{
\frac{MDN_0}{\lambda T^3}-1000
=
\frac{
\mu\Gamma_k+10(1-20w)+C_0/T^2
}{T^2}.}
\tag{9}
\]

由 (7) 与 `Gamma_k>15.09`，右侧分子严格为正：

\[
1000\cdot15.09-790>14300.
\]

另一方面由 (8)、`Gamma_k<39.003`：

\[
\mu\Gamma_k+10(1-20w)+C_0/T^2
<10001\cdot39.003+1
<390100.
\]

故

\[
\boxed{
0<
\frac{MDN_0}{\lambda T^3}-1000
<\frac{390100}{T^2}.}
\tag{10}
\]

---

## 5. reduced denominator 必须巨大

把左侧第一个有理数写成既约形式

\[
\frac{MDN_0}{\lambda T^3}=\frac ab,
\qquad\gcd(a,b)=1.
\]

因为它与整数 `1000` 的差非零，必有

\[
\left|\frac ab-1000\right|\ge\frac1b.
\]

结合 (10)：

\[
\boxed{
b>\frac{T^2}{390100}.}
\tag{11}
\]

现在计算这个 `b` 的 2/5 结构。

由于 `h` 与 `10` 互素，

\[
v_2(M)=v_2(Qb_1)=v_2(b_1)=e:=v_2(w),
\]

\[
v_5(M)=0.
\]

再记

\[
\nu_2=v_2(N_0),
\qquad
\nu_5=v_5(N_0).
\]

于是

\[
\boxed{
 b
=2^{(3k+\lambda_2-A-e-\nu_2)_+}
 5^{(3k+\lambda_5-B-\nu_5)_+}.}
\tag{12}
\]

因此 general deep sector 必须满足

\[
\boxed{
2^{(3k+\lambda_2-A-e-\nu_2)_+}
5^{(3k+\lambda_5-B-\nu_5)_+}
>
\frac{10^{2k}}{390100}.}
\tag{13}
\]

这是本文最通用的 complement-height inequality。

---

## 6. double-deep 的显式线性高度带

若

\[
A>0,
\qquad B>0,
\]

则

\[
\lambda_2=\lambda_5=0.
\]

把 (13) 等价地写成 cancellation 上界：

\[
\boxed{
2^{\min(A+e+\nu_2,3k)}
5^{\min(B+\nu_5,3k)}
<390100\,10^k.}
\tag{14}
\]

这已经改变了 `(A,B)` 可行区域的渐近斜率。

### 6.1 `5` 侧不可能达到 `3k`

若

\[
B+\nu_5\ge3k,
\]

则 (14) 左侧至少为 `5^(3k)`。但

\[
\frac{5^{3k}}{10^k}
=\left(\frac{125}{10}\right)^k
=12.5^k,
\]

对 `k>=31` 远大于 `390100`，矛盾。因此

\[
\boxed{B+\nu_5<3k.}
\tag{15}
\]

### 6.2 若 2 侧达到 `3k`，5 侧立刻变浅

若

\[
A+e+\nu_2\ge3k,
\]

由 (14)-(15)：

\[
2^{3k}5^{B+\nu_5}
<390100\,10^k.
\]

所以

\[
5^{B+\nu_5}
<390100\left(\frac54\right)^k.
\]

注意

\[
390100<5^8,
\qquad
\frac54<5^{0.139}.
\]

故得到简洁安全界

\[
\boxed{
B+\nu_5<8+0.139k.}
\tag{16}
\]

所以 extreme 2-deep 不可能同时伴随显著 5-deep。

### 6.3 未饱和区

若

\[
A+e+\nu_2<3k,
\]

则结合 (15)，(14) 直接变成

\[
\boxed{
2^{A+e+\nu_2}5^{B+\nu_5}
<390100\,10^k.}
\tag{17}
\]

这是一条真正的线性 logarithmic height bound，而不是此前 supply cap 的常数因子改进。

---

## 7. 当前意义

central denominator 已全部关闭，所以 minimal diagonal 的统一问题只剩 deep。

本文说明 deep 的 complement quotient 本身产生一个 `T^-2` 级别的 rational approximation；由于其分母只能来自 `2,5`，不能被任意深地约掉。

特别是 double-deep：

- `B+v_5(N_0)<3k`；
- 若 2 侧达到 `3k`，则 `B+v_5(N_0)<8+0.139k`；
- 其余区域满足 (17)。

下一步应把 (13)-(17) 与已有的 resonance parity、unit-square locks、Q-side orientation、primitive cross-corridor caps 联用。
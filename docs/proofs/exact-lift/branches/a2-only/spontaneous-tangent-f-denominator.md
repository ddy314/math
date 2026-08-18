# A2 repeated spontaneous 与真实 `f`-denominator line

> **依赖：** `spontaneous-angle.md`、`spontaneous-prefix-boundaries.md`、`spontaneous-tangent-decimal.md`。
>
> **严格状态：**本文处理一般 `p|f` 的 repeated spontaneous overlap，不假设 `Psi_f=0`。由真实 `f` denominator line 与 `Omega_sp=0` 先强迫 `Delta_0=0`，此时 sphere 降成唯一有限第三分子 orientation。加入 repeated tangent 后，整个系统降为两个 pure-prefix 方程 `Delta_0=G_f=0`，再消元得到一个显式八次式。本文完整审计该八次式的 inert singular bad primes，并证明所有 genuine singular candidate 都无法提升到 `p^2`。因此此 overlap 不存在新的 singular Hensel tree；但 generic simple roots 仍可能存在，所以本文不宣称该 denominator overlap 全局为空，也不宣称 A2 全局关闭。

---

## 1. `f` denominator line + `Omega_sp` 强迫 `Delta_0=0`

记

\[
F_f=r_s(x+2)+2x.
\]

若 genuine odd prime `p` 同时满足

\[
F_f\equiv0,
\qquad
\Omega_{\rm sp}\equiv0,
\]
且 `p∤x(x+2)`，则

\[
r_s\equiv-\frac{2x}{x+2}.
\tag{1.1}
\]

另一方面

\[
\Omega_{\rm sp}
=A_{\rm sp}r_s+2xy^2(x+2).
\]
代入 (1.1)：

\[
\Omega_{\rm sp}
=\frac{2x}{x+2}
\left[-A_{\rm sp}+y^2(x+2)^2\right].
\]

而 exact identity

\[
\boxed{
-A_{\rm sp}+y^2(x+2)^2
=-100x^2\Delta_0,
}
\tag{1.2}
\]
其中

\[
\Delta_0=2025x^2-18y-y^2.
\]
所以

\[
\boxed{
p\mid f,\ p\mid\Omega_{\rm sp}
\Longrightarrow
\Delta_0\equiv0\pmod p.}
\tag{1.3}
\]

这与旧 resultant `Res(F_f,Omega_sp)=-200x^3 Delta_0` 完全一致，但这里保留了 denominator root 本身。

---

## 2. 第三分母与 sphere 唯一 orientation 都显式化

`spontaneous-angle.md` 有

\[
r_s=\frac{x}{\bar w},
\qquad
\bar w:=\frac{b_3}{T10^M}.
\]
所以 (1.1) 给

\[
\boxed{
\bar w=-\frac{x+2}{2}.
}
\tag{2.1}
\]

令

\[
s=9+y,
\qquad
\bar\zeta=\frac{a_3}{T10^M}.
\]

exact sphere 为

\[
x^2\bar w^2(s+\bar\zeta)^2
=(x+2+\bar w)^2
\left(
\frac{2025x^2+y^2}{100}\bar w^2+x^2\bar\zeta^2
\right).
\tag{2.2}
\]

在 `Delta_0=0` 上

\[
2025x^2+y^2=2y(y+9)=2ys.
\tag{2.3}
\]

代入 (2.1)–(2.3) 并约去 genuine units，可得一次式

\[
x^2(s+2\bar\zeta)
=\frac{y(x+2)^2}{200}.
\]
因此唯一有限 sphere root 为

\[
\boxed{
\bar\zeta_f
=\frac{y(x+2)^2}{400x^2}-\frac{s}{2}.
}
\tag{2.4}
\]

这与 `spontaneous-prefix-boundaries.md` 的 `Delta_0=0` degree-drop 结论吻合：这里不存在第二个有限 orientation。

---

## 3. repeated tangent 唯一固定 decimal length residue

repeated branch derivative 为

\[
55\tau=9(s-\bar\zeta_f),
\qquad
\tau=10^{-M}.
\]
利用 (2.4)：

\[
\boxed{
\tau_f
=\frac9{55}
\left(
\frac{3s}{2}
-\frac{y(x+2)^2}{400x^2}
\right).
}
\tag{3.1}
\]

所以一般 `f`-denominator repeated overlap 不会固定 `K` 为常数；此前 `18K-29=0` 只属于额外 `Psi_f=0` 的更窄子通道。

---

## 4. `已严格完成`：repeated condition 在 `Delta_0=0` 上降成线性 `G_f`

把 (3.1) 代入统一 tangent

\[
\mathscr R_{\rm tan}
=495\tau^2-220s\tau+27s^2+9c,
\]
其中

\[
c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.
\]

清分母以后再对 `Delta_0` 做 Euclidean reduction，余式恰为 `243 G_f`，其中

\[
\boxed{
\begin{aligned}
G_f(x,y):={}&225x^2
(975627x^4+222616x^3+259848x^2+864x+432)\\
&-2(x+2)^2(27827x^2+108x+108)y.
\end{aligned}}
\tag{4.1}
\]

因此 genuine repeated `f`-denominator overlap 必满足

\[
\boxed{
\Delta_0(x,y)=0,
\qquad
G_f(x,y)=0.
}
\tag{4.2}
\]

这里 `G_f` 对 `y` 只有一次；third block、`r_s` 与 `tau` 都已经消失。

---

## 5. `已严格完成`：最终只剩一个八次 pure-prefix polynomial

直接对 (4.2) 消去 `y`：

\[
\boxed{
\operatorname{Res}_y(\Delta_0,G_f)
=-50625x^4\mathcal F_f(x),
}
\tag{5.1}
\]
其中

\[
\boxed{
\begin{aligned}
\mathcal F_f(x):={}&
951848043129x^8
+434380360464x^7
+560807241744x^6\\
&+134769639744x^5
+88351387616x^4
+5400711936x^3\\
&+2954700032x^2
+28892160x
+10416384.
\end{aligned}}
\tag{5.2}
\]

对 genuine `p∤3·5·x`：

\[
\boxed{
\Delta_0=G_f=0
\Longrightarrow
\mathcal F_f(x)=0\pmod p.}
\tag{5.3}
\]

所以一般 repeated `f`-denominator overlap 已从多变量 source system 降成单一 degree-8 prefix curve。

---

## 6. 真实 endpoint defect 上八次式严格为正

令真实 denominator defect

\[
u:=10x-1=\frac{H}{5^{M-1}},
\qquad0<u<\frac1{19}.
\tag{6.1}
\]

直接代入 `x=(1+u)/10`：

\[
10^8\mathcal F_f\left(\frac{1+u}{10}\right)
=\mathcal F_H(u),
\]
其中

\[
\boxed{
\begin{aligned}
\mathcal F_H(u)={}&
951848043129u^8
+11958587949672u^7\\
&+113139094614492u^6
+615777350903064u^5\\
&+2617235426677430u^4
+6748774195745624u^3\\
&+12182775750721052u^2
+12400944702783912u\\
&+5904991117326169.
\end{aligned}}
\tag{6.2}
\]

所有九个系数严格为正。因此

\[
\boxed{u>0\Longrightarrow\mathcal F_H(u)>0.}
\tag{6.3}
\]

所以 repeated `f`-overlap 完全没有 Archimedean root；任何 modular state 都是纯 `p`-adic wrapping。

---

## 7. `有限证书`：八次式 singular bad-prime set

八次式判别式精确分解为

\[
\boxed{
\begin{aligned}
\operatorname{disc}(\mathcal F_f)
={}&2^{136}3^{10}5^{20}11^4 17^4 23^6 43^2 101^8\\
&\cdot163\cdot673^2\cdot2521^2\cdot49663^2\cdot188359^2\\
&\cdot33719039\cdot118599997.
\end{aligned}}
\tag{7.1}
\]

限制到 non-`3` inert primes `p≡3 mod4`，只需审计

\[
\boxed{
11,23,43,163,49663,188359,33719039.}
\tag{7.2}
\]

逐个计算 `gcd(F_f,F_f')`：

- `p=11`：repeated roots 只有 `x=0,-1`（另一个二次因子无 `F_11` 根）；
- `p=23`：唯一 repeated root `x=-2`，为 denominator boundary；
- `p=43`：`gcd=1`，只是 leading-degree degeneration；
- `p=163`：唯一 repeated root `x=56`；
- `p=49663`：唯一 repeated root `x=41967`；
- `p=188359`：唯一 repeated root `x=28889`；
- `p=33719039`：唯一 repeated root `x=27256238`。

代回完整 system `Delta_0=G_f=0`：

\[
\boxed{
\begin{array}{c|c|c|c}
p&x&y&\text{状态}\\ \hline
11&0&0&x\text{ boundary}\\
11&10&9&\text{full singular candidate}\\
23&21&10,18&x+2=0\text{ boundary}\\
43&-&-&\text{no repeated root}\\
163&56&155&\text{full singular candidate}\\
49663&41967&-&\text{no }y\text{ solving full system}\\
188359&28889&-&\text{no }y\text{ solving full system}\\
33719039&27256238&16620484&\text{full singular candidate}
\end{array}}
\tag{7.3}
\]

三组 nonboundary full candidates 的 `x,x+2,y,s,d,A_sp,Nbar` 都为单位。

---

## 8. `有限证书`：三组 genuine singular candidate 全部无法升到 `p^2`

对

\[
F_1=\Delta_0,
\qquad
F_2=G_f
\]
在第一层解 `(x_0,y_0)` 写

\[
x=x_0+pX,
\qquad
y=y_0+pY.
\]

模 `p^2` 的必要条件是线性系统

\[
J(x_0,y_0)
\binom XY
\equiv
-\binom{F_1(x_0,y_0)/p}{F_2(x_0,y_0)/p}
\pmod p.
\tag{8.1}
\]

对三组 genuine singular candidate 做 exact modular row reduction，最后一零行的 augmented residue 分别为

\[
\boxed{
\begin{array}{c|c}
p&\kappa_p\\ \hline
11&10\\
163&148\\
33719039&30845985
\end{array}}
}
\tag{8.2}
\]

三者都非零，所以 (8.1) 均不相容：

\[
\boxed{
\text{三组 genuine singular first-layer state 均无 }p^2\text{ lift}.}
\tag{8.3}
\]

因此：

\[
\boxed{
\text{repeated spontaneous}\cap f\text{-denominator}
\text{ 中不存在 surviving singular Hensel tree}.}
\tag{8.4}
\]

注意这里消灭的是八次 reduced curve 的**进一步 singular branching**。`F_f(x)=0` 在其他 inert primes 上仍可能有 simple roots，所以不能把 (8.4) 写成整个 `f` overlap 为空。

---

## 9. 更新后的 denominator-overlap 核

一般 repeated spontaneous `f`-denominator overlap 现在规范化为

\[
\boxed{
\Delta_0=0,
\qquad
G_f=0,
\qquad
\mathcal F_f(x)=0.
}

并且：

- third block 与 source ratio 已完全消去；
- real endpoint 上 `F_H(u)>0`；
- 所有 inert singular bad primes 已审计；
- genuine singular candidates 全部不能升到 `p^2`。

所以后续若继续处理该 overlap，只需要研究 **simple modular roots of one fixed octic** 与真实 decimal defect orbit `u=H/5^{M-1}` 的同步；不应再做 singular-prime 或 curvature-character 枚举。

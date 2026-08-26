# A1 minimal diagonal: full contact-sign polynomial inside the finite `R` shell

> 日期：2026-08-27。依赖 `deep-2high-dual-slot-shell.md`、`deep-2high-contact-shell-coupling.md` 与 `deep-contact-sign-window.md`。当前统一 frontier `k>=32`。
>
> 本文把原 rational-contact square 的 leading-sign polynomial 重新代回 dual-shell 坐标。与旧 `Gamma` window 不同，这里同时消去 `Gamma` 与 prefix ratio `N_0/T`，得到只依赖 `(xi,y)` 的一元必要不等式；moderate 中 `xi=r`，故可直接作为 exact integer `(r,m)` slot certificate。

状态：**严格完成；附 exact C++ certificate。它是对原 contact-sign obstruction 的更精确使用，不与旧 contact lower window重复计数为独立条件。**

---

## 1. dual shell 先恢复 `N_0/T`

沿用

\[
f:=5^d,
\qquad
G:=2^cn_0,
\qquad
y:=R/f,
\]

以及

\[
\xi=2^{-\eta}5^{B+2\nu_5}r_{10}.
\]

直接由 master definitions：

\[
\begin{aligned}
fG\xi
&=5^{k+1-Y}2^{k+1+\eta+\nu_2}n_0
  \cdot2^{-\eta}5^{B+2\nu_5}r_{10}\\
&=2^{k+1+\nu_2}5^{k+1+\nu_5}n_0r_{10}\\
&=10TN_0r_{10},
\end{aligned}
\]

因为 `Y=B+nu_5`。所以

\[
\boxed{fG\xi=10TN_0r_{10}.}
\tag{1}
\]

另一方面 dual determinant 给

\[
y-z=\frac{2r_{10}}{fG},
\]

故

\[
\boxed{y-z=\frac{\xi}{5TN_0}.}
\tag{2}
\]

Möbius identity 又给

\[
y-z=\frac{y^2-1}{H+y},
\qquad
H=20b_1+1=200T^2-(20w-1).
\]

于是 prefix ratio

\[
s_0:=\frac{N_0}{T}
\]

被精确恢复为

\[
\boxed{
s_0=
\frac{\xi(H+y)}{5T^2(y^2-1)}.}
\tag{3}
\]

这一步不使用 contact square。

---

## 2. `Gamma` 也已是 `y` 的函数

`deep-2high-contact-shell-coupling.md` 已严格证明

\[
\boxed{
\Gamma
=\frac{\xi}{5}
\frac{y+20w-1-\dfrac{C_0}{5T^2}}
{y^2-1},}
\tag{4}
\]

其中

\[
C_0=w(10w-1).
\]

因此原 contact leading polynomial中的两个连续变量 `(s_0,Gamma)` 都可以同时消去。

---

## 3. contact leading polynomial

原 contact square 写成

\[
\mathcal R
=10000F_{z,w,\Gamma}(s_0)T^{10}+E_9,
\qquad
|E_9|\le101834561T^9,
\]

且 exact candidate 要求 `mathcal R>=0`。因此当前 `T>=10^32`：

\[
\boxed{
F_{z,w,\Gamma}(s_0)>-1.1\times10^{-28}.}
\tag{5}
\]

六类型统一写

\[
F=s_0^2-A_zs_0+200\Gamma-C_{z,w},
\tag{6}
\]

其中

\[
A_1=280,
\qquad A_3=240,
\]

以及

\[
\begin{array}{c|rrrrrr}
(z,w)&(1,1)&(1,2)&(1,3)&(1,4)&(3,1)&(3,2)\\ \hline
C_{z,w}&5980&5180&4380&3580&4340&3940.
\end{array}
\tag{7}
\]

---

## 4. 去掉 `T^{-2}` correction 后的一元主多项式

记

\[
a:=20w-1,
\qquad
X:=\frac{40\xi}{y^2-1}.
\]

由 (3)：

\[
s_0
=X+rac{\xi(y-a)}{5T^2(y^2-1)}.
\tag{8}
\]

而 (4) 给

\[
200\Gamma
=X\left(y+a-\frac{C_0}{5T^2}\right).
\tag{9}
\]

因此定义 shell main term

\[
\boxed{
P_{\xi,z,w}(y)
:=X^2+X(y+a-A_z)-C_{z,w}.}
\tag{10}
\]

则

\[
F=P_{\xi,z,w}(y)+\Delta_T.
\tag{11}
\]

在 full shell

\[
196000<\xi<15214000,
\qquad3780<y<78015,
\]

上直接使用粗界即有

\[
\boxed{|\Delta_T|<10^{-55}.}
\tag{12}
\]

相对 (5) 完全可忽略。

---

## 5. `P(y)` 在整个 shell 严格递减

写

\[
b:=a-A_z.
\]

六类型中

\[
-261\le b\le-201.
\]

又

\[
X=40\xi/(y^2-1)>0,
\qquad
X'=-\frac{2yX}{y^2-1}.
\]

所以

\[
P'(y)
=X\left[
1-\frac{2y(2X+y+b)}{y^2-1}
\right].
\]

`P'<0` 等价于

\[
y^2+2by+4Xy+1>0.
\]

而 `y>3780`、`b>=-261` 已使

\[
y^2+2by+1>0,
\]

故

\[
\boxed{P'_{\xi,z,w}(y)<0}
\tag{13}
\]

在整个 full shell 上严格成立。

---

## 6. exact integer leading-slot condition

令

\[
m=\lfloor y\rfloor.
\]

由于 `P` 递减：

\[
P(y)<P(m).
\]

若 `P(m)<0`，把 denominator 清掉：

\[
P(m)=
\frac{\mathcal P_{\xi,z,w}(m)}{(m^2-1)^2},
\]

其中纯整数 quartic numerator 为

\[
\boxed{
\begin{aligned}
\mathcal P_{\xi,z,w}(m)
={}&1600\xi^2\\
&+40\xi(m+20w-1-A_z)(m^2-1)\\
&-C_{z,w}(m^2-1)^2.
\end{aligned}}
\tag{14}
\]

当前 `m<=78014`，所以若 integer numerator 至少为 `-1`：

\[
P(m)\le-rac1{(78014^2-1)^2}
<-2.6\times10^{-20}.
\]

结合 (11)-(12)，这与 contact necessary bound (5) 相差八个数量级以上。

因此任何 exact candidate 必须满足完全整数化的条件

\[
\boxed{
\mathcal P_{\xi,z,w}(m)\ge0.}
\tag{15}
\]

无需 floating point，也无需枚举 `N_0` 或 `Gamma`。

---

## 7. moderate exact count

moderate 中

\[
\xi=r\in\mathbf Z.
\]

在修正后的

\[
2,603,440
\]

个 local-compatible `r` signatures 上，先应用现有 contact/remainder slot interval，再应用 (15)。exact checker 得：

\[
\boxed{
\begin{array}{c|r|r|r}
(z,w)&\text{old safe }(r,m)&\text{after (15)}&\text{retained}\\ \hline
(1,1)&1,881,136,022&1,822,151,927&96.8644\%\\
(1,2)&821,624,445&796,101,511&96.8936\%\\
(1,3)&1,060,138,361&1,029,160,856&97.0780\%\\
(1,4)&429,109,928&416,968,782&97.1706\%\\
(3,1)&15,361,714,596&15,335,559,940&99.8297\%\\
(3,2)&7,802,825,159&7,790,170,686&99.8378\%
\end{array}}
\tag{16}
\]

总计从

\[
27,356,548,511
\]

降到

\[
\boxed{27,190,113,702.}
\tag{17}
\]

额外删除

\[
\boxed{166,434,809}
\]

个 safe leading-slot pairs，约 `0.6084%`。

这不是数量级坍缩，但它第一次把原 contact leading sign **直接**写成 finite `(r,m)` 的 exact integer predicate。

---

## 8. dependency boundary

(15) 来自原 rational-contact square 的同一个 leading-sign obstruction；此前 typewise `Gamma_L` 只是在不知道 actual `s_0` 时取 `s_0=0.1` 得到的 uniform consequence。

所以：

- (15) 可以替代/加强旧 contact lower-window 在 finite shell 内的使用；
- 不能把 (15) 与旧 `Gamma_L` 当成统计独立的两个 obstruction；
- positive-tail upper window仍是独立输入。

附审计：

`scripts/exact-lift/a1-only/research-checks/deep-denominator/check_a1_deep_hl_full_contact_shell_slots.cpp`。

---

## 9. 下一接口

当前 moderate finite front 可按

\[
(r,m)
\]

先执行：

1. local 2/5 locks；
2. contact/remainder exact slot window；
3. integer quartic (15)；
4. whole-block `(alpha,beta)` partition；
5. prime-source periodic envelope；
6. 最后才进入 unbounded `d` divisor family。

不过 (17) 也说明，仅继续 sharpen continuous contact sign 很难关闭 tail。真正的下一关键仍是：把 dual-slot exact `q` form 与 contact-square `q^2/delta_C` lifting联立，得到对 lifted-block **routing** 或 supply denominator `G` 的新约束。
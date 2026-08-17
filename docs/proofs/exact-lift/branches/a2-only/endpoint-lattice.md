# A2 endpoint lattice continuation — 2026-08-17

> **适用范围：**延续已合并的 `phase-and-defect.md`、`phase-and-defect.md` 与 `phase-and-defect.md`。
> **严格状态：**本文给出新的 endpoint shell、defect remainder、height split 与 Gaussian-allocation 排除结果，但**不宣称 A2 全局关闭**。
> **审计原则：**本轮曾得到若干看起来很深的 `5`-进 endpoint congruence；完整代回 determinant / decimal-place 恒等式后发现其中若干只是旧系统的重写。本文把它们明确降级，不计作新的 obstruction。

---

## 1. 记号与 finite-defect 补余量

沿用 terminal A2：

\[
M=m_2,\qquad m=m_3,\qquad a=a_1\in\{5,7,9,11,13\},
\]

\[
x=\frac{b_2}{10^M},\qquad y=\frac{a_2}{10^{M-1}},\qquad
w=\frac{b_3}{10^m},\qquad \zeta=\frac{a_3}{10^m}.
\]

记 exact lift 的值为

\[
\mathcal R=\frac{a+y+10^{-M}\zeta}{2+x+10^{-M}w}.
\]

旧 finite-defect 正规形写成

\[
c_-^2X=kD+R,\qquad 0<R<D,
\]

并定义

\[
J_{\rm def}:=\frac{c_-^2X}{D}=k+\frac RD.
\]

本轮对低商状态更方便的变量是顶部补余量

\[
\boxed{C:=D-R},\qquad 0<C<D,
\]

以及

\[
j:=k+1,\qquad J_{\rm def}=j-\frac CD.
\]

---

# 第一部分：纯十进制 endpoint shell

## 2. `已严格完成`：`J_def` 的直接十进制恢复

第三坐标为

\[
r_3=\frac\zeta w.
\]

由旧 third-distance ratio 与拼接式直接消元，可得到

\[
\boxed{
J_{\rm def}=w(\mathcal R-r_3).
}
\tag{2.1}
\]

把拼接式代入，亦即

\[
\boxed{
J_{\rm def}
=\frac{w(a+y)-(2+x)\zeta}{2+x+10^{-M}w}.
}
\tag{2.2}
\]

这一步把 finite-defect 商从 factor-allocation 对象恢复成真实十进制变量。

另一方面球面关系为

\[
\mathcal R^2
=\frac{a^2}{4}+\frac{y^2}{100x^2}+\frac{\zeta^2}{w^2}.
\]

令

\[
S_a(x,y):=\frac{a^2}{4}+\frac{y^2}{100x^2}.
\]

由 \(w\mathcal R=J_{\rm def}+\zeta\) 得到精确 shell：

\[
\boxed{
J_{\rm def}(J_{\rm def}+2\zeta)
=w^2S_a(x,y).
}
\tag{2.3}
\]

因此 finite-defect 的整数带编号，本质上是一个纯四变量球面壳层条件。

---

## 3. `已严格完成`：消去 `w,zeta,M` 后的纯前缀 barrier

由拼接式和 (2.1)，

\[
(2+x)\mathcal R+10^{-M}J_{\rm def}=a+y.
\]

定义

\[
q_*:=1+\frac{J_{\rm def}}\zeta.
\]

因为 \(\zeta/w=\mathcal R/q_*\)，球面式化为

\[
\boxed{
(2+x)^2S_a(x,y)q_*^2
=
(a+y-10^{-M}J_{\rm def})^2(q_*^2-1).
}
\tag{3.1}
\]

由于右边系数满足

\[
0<a+y-10^{-M}J_{\rm def}<a+y,
\]

可定义

\[
\boxed{
q_0(x,y):=
\frac{a+y}{
\sqrt{(a+y)^2-(2+x)^2S_a(x,y)}}
}
\tag{3.2}
\]

并严格得到

\[
\boxed{q_*>q_0(x,y).}
\tag{3.3}
\]

若 defect 商为 \(k\)，则

\[
J_{\rm def}<k+1,\qquad \zeta>1,
\]

故

\[
q_*<k+2.
\]

于是得到纯前缀必要条件

\[
\boxed{q_0(x,y)<k+2.}
\tag{3.4}
\]

同时

\[
J_{\rm def}=\zeta(q_*-1)>q_0(x,y)-1,
\]

所以

\[
\boxed{
\frac RD>q_0(x,y)-(k+1).
}
\tag{3.5}
\]

这比仅通过 canonical angle 间接限制 \(R/D\) 更直接。

---

## 4. `已严格完成`：七个 finite-defect 状态全部进入固定余量带

把 (3.5) 与既有 core window 联立，再用 (2.3) 的粗上界，得到：

\[
\boxed{
\begin{array}{c|c|c}
a&k&R/D\\ \hline
5&1&\dfrac23<R/D<\dfrac{17}{20}\\[1mm]
7&2&\dfrac{31}{100}<R/D<\dfrac{31}{40}\\[1mm]
9&2&\dfrac{247}{250}<R/D<1\\[1mm]
9&3&0<R/D<\dfrac{18}{25}\\[1mm]
11&3&\dfrac{103}{125}<R/D<1\\[1mm]
11&4&0<R/D<\dfrac{17}{25}\\[1mm]
13&5&\dfrac9{100}<R/D<\dfrac{33}{50}
\end{array}}
\tag{4.1}
\]

其中 `a=5,7` 的新 lower bound 用精确 Sturm root count 验证 `q0(x,1)` 在完整 core interval 上分别严格大于 `8/3` 与 `331/100`；`a=9,11,13` 则在左端点直接得到

\[
q_0(1/10,1)^2=
\frac{8000}{503},\quad
\frac{256}{11},\quad
\frac{1600}{43}.
\]

上界只用

\[
J_{\rm def}<\sqrt{1+S_a(x,y)}-1
\]

与已有 digit window。

因此旧的七个 `k` 状态不再对应整个 `(0,D)`，而都落在固定的 remainder band 中。

---

# 第二部分：最危险 `(a,k)=(9,2)` 的 endpoint core

## 5. `已严格完成`：`x,y,zeta,w,C` 同时进入端点薄层

从此固定

\[
\boxed{a=9,\qquad k=2,\qquad j=3.}
\]

由 (4.1)，

\[
\boxed{0<C<\frac3{250}D.}
\tag{5.1}
\]

又因 `q0<4`，而在该 core 中

\[
\frac{\partial}{\partial x}\frac1{q_0^2}<0,
\qquad
\frac{\partial}{\partial y}\frac1{q_0^2}>0,
\]

所以 `q0` 对 `x` 严格增、对 `y` 严格减。两个精确端点为

\[
q_0(2/19,1)^2
=16+\frac1{564}>16,
\]

\[
q_0(1/10,249/250)^2
=16+\frac{258}{44237}>16.
\]

因此

\[
\boxed{
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1.
}
\tag{5.2}
\]

再由

\[
q_0(x,y)>\sqrt{\frac{8000}{503}},
\qquad J_{\rm def}<3,
\]

得到

\[
\boxed{
1<\zeta<
\frac3{\sqrt{8000/503}-1}
<\frac{251}{250}.
}
\tag{5.3}
\]

由 shell (2.3) 又有

\[
\boxed{
\frac{42}{\sqrt{2515}}<w<\frac{843}{1000}.
}
\tag{5.4}
\]

为后续整数化，定义四个真实十进制 endpoint defect：

\[
\boxed{
b_2=10^{M-1}+2^{M-1}H,}
\]

\[
\boxed{a_2=10^{M-1}-e,}
\]

\[
\boxed{a_3=10^m+h,}
\]

以及前述 `C=D-R`。由 (5.1)–(5.3)，

\[
\boxed{
0<H<\frac{5^{M-1}}{19},
\qquad
0<e<\frac{10^{M-1}}{250},
\qquad
0<h<\frac{10^m}{250},
\qquad
0<C<\frac{3D}{250}.
}
\tag{5.5}
\]

也就是说最危险状态已经变成四个同时很小的整数缺口 `(H,e,h,C)`。

---

## 6. `已严格完成`：第三坐标球面因子的统一短窗

primitive sphere 中沿用

\[
H_0-Y_3=5^Ec_-^2X,
\qquad
H_0+Y_3=c_+^2Y,
\]

以及第二坐标 `Y_2`。在当前 core，精确有

\[
\frac{H_0}{g10^m}=3+\zeta-\frac CD,
\qquad
\frac{Y_2}{g10^m}=\frac{yw}{10x},
\]

其中

\[
g=2^{t-1}\rho.
\]

由 (5.2)–(5.4)，

\[
\boxed{
\frac{99}{125}
<\frac{yw}{10x}
<\frac{843}{1000}.
}
\tag{6.1}
\]

所以两个正因子进入固定短窗：

\[
\boxed{
\frac{393}{125}
<\frac{H_0-Y_2}{g10^m}
<\frac{1607}{500},
}
\tag{6.2-}
\]

\[
\boxed{
\frac{2389}{500}
<\frac{H_0+Y_2}{g10^m}
<\frac{606}{125}.
}
\tag{6.2+}
\]

这两个区间会在后面的 `rho^2` square-side allocation 中提供 Archimedean 量化。

---

# 第三部分：新的整数接口

## 7. `已严格完成`：`J_def` 满足纯整数四次式，`C | F(j)`

令

\[
T=10^m,
\qquad
Q=2\cdot10^M+b_2,
\qquad
P=9\cdot10^{M-1}+a_2,
\]

\[
C_0=\frac{9b_2}{2},
\qquad
N_0=C_0^2+a_2^2.
\]

从 shell 与拼接 relation 消去 `w`，可得到

\[
\boxed{
F(J):=
 b_2^2T\,J(TJ+2a_3)(10P-J)^2
-Q^2N_0(TJ+a_3)^2=0
}
\tag{7.1}
\]

在 full finite-defect 状态中

\[
J=j-\frac CD,
\qquad \gcd(C,D)=1.
\]

把 `F(j-X)` 看作整数系数多项式，`X=C/D` 是其既约有理根。由 rational-root theorem，

\[
\boxed{C\mid F(j).}
\tag{7.2}
\]

特别地对当前 `j=3`，顶部补余量 `C` 必须整除一个完全由十进制 prefix 与 `a_3` 构成的显式整数。本文暂不把 (7.2) 宣称为 closure；它是后续与 prefix defect / Gaussian allocation 联立的新整数接口。

---

## 8. `已严格完成`：独立的线性 `2^m` phase

沿用 source split：

\[
U=5^{M-s},
\qquad E=\lambda+s,
\qquad d=m-E,
\]

\[
5^{M+\lambda}+c=g\theta,
\]

以及 finite-defect 补余量形式

\[
\alpha_0q=C_jD+C,
\qquad
\alpha_0c_u=gA_j-5^EC,
\]

其中

\[
A_j=a_3+j10^m,
\qquad
C_j=10P-j.
\]

与

\[
c_Qq=U+g2^mc_u
\]

一起消元，得到精确恒等式

\[
\boxed{
C\theta-UA_j
=
2^mc_u\left(
\alpha_0c_u-5^dc_QC_j
\right).
}
\tag{8.1}
\]

因此

\[
\boxed{
C\theta\equiv UA_j\pmod{2^mc_u},
}
\tag{8.2}
\]

特别地

\[
\boxed{
C\theta\equiv Ua_3\pmod{2^m}.
}
\tag{8.3}
\]

这条 phase 与旧 `2^{2t-1}` square-depth phase 来源不同；目前把它保留为严格 compatibility，不宣称它单独给出空性。

---

## 9. `已严格完成`：Hensel 商落入统一 `19–20` slot

定义

\[
L_*:=2^m5^Ec_u.
\]

由 Hensel 商

\[
5^Eq+c_u=g\omega,
\qquad
5^{M+\lambda}+c=g\theta,
\]

与

\[
c_Q\omega-\theta=L_*,
\]

可精确化为

\[
\boxed{
\frac\theta{L_*}
=\frac{2+10^{-M}w}{x},
}
\tag{9.1}
\]

\[
\boxed{
\frac{c_Q\omega}{L_*}
=\frac{x+2+10^{-M}w}{x}.
}
\tag{9.2}
\]

在 `(a,k)=(9,2)` endpoint core 中，`H>=1` 与 (5.2) 保证

\[
\boxed{
19L_*<\theta<20L_*,
}
\tag{9.3}
\]

\[
\boxed{
20L_*<c_Q\omega<21L_*.
}
\tag{9.4}
\]

所以存在唯一

\[
\boxed{\varrho:=20L_*-\theta}
\]

满足

\[
0<\varrho<L_*,
\qquad
\theta=20L_*-\varrho,
\qquad
c_Q\omega=21L_*-\varrho.
\]

又因为 `theta` 与 `2,5,c_u` 均互素，

\[
\boxed{\gcd(\varrho,L_*)=1.}
\tag{9.5}
\]

因此三个五进 channel 在这个 endpoint core 中共享同一个长度为 `L_*` 的 Hensel slot。

---

# 第四部分：真正产生 pruning 的 height split

## 10. `已严格完成`：high-`m` / low-`m` 二分

记

\[
u_0=c_u\rho,
\qquad
K_\rho:=2^{m+t-1}5^m.
\]

由 `x` 的定义有精确式

\[
\boxed{
\frac{u_0}{K_\rho}
=
\frac{2x}{4^t}\,
\frac{5^{M-s}}{20^m}.
}
\tag{10.1}
\]

由于 `x<2/19`、`t>=3`，若

\[
m>\frac{6M}{11},
\]

则 `20^6>5^11` 给出

\[
\boxed{
\frac{u_0}{K_\rho}<\frac1{304}.
}
\tag{10.2}
\]

另一方面旧 tail bound

\[
5^\lambda>3\cdot2^{M+1}>2^M
\]

与 `5^3<2^7` 给出

\[
\boxed{\lambda>\frac{3M}{7}.}
\tag{10.3}
\]

source channel `s>0` 满足

\[
m=\frac32(\lambda+s)>\frac{9M}{14}>\frac{6M}{11},
\]

因此它全部落入 (10.2) 的 small-source cone。

若

\[
m\le\frac{6M}{11},
\]

则 source channel 不可能发生，故

\[
\boxed{s=0,}
\]

只剩 balance / reflection，并有

\[
\boxed{
\frac{3M}{7}<\lambda\le m\le\frac{6M}{11}.
}
\tag{10.4}
\]

reflection 的

\[
d=m-\lambda
\]

进一步满足

\[
\boxed{0<d<\frac{9M}{77}.}
\tag{10.5}
\]

于是最危险核被切成两个性质完全不同的无界锥：

\[
\boxed{
\begin{array}{ll}
m>6M/11:&u_0/K_\rho<1/304,\\[1mm]
m\le6M/11:&s=0,\quad 3M/7<\lambda\le m.
\end{array}}
\tag{10.6}
\]

---

## 11. `已严格完成`：low-`m` cone 强迫深 `5`-进前缀范数

沿用旧高阶 tail certificate

\[
10^m\mid b_3^4\cdot4N_0.
\]

因为

\[
v_5(b_3)=m-\lambda,
\]

所以

\[
\boxed{v_5(N_0)\ge4\lambda-3m.}
\tag{11.1}
\]

在 low-`m` cone 中由 (10.4)：

\[
\boxed{v_5(N_0)>\frac{6M}{77}.}
\tag{11.2}
\]

reflection 还有旧五进同步的精确深度

\[
v_5(N_0)=3\lambda-2m,
\]

从而

\[
\boxed{
\text{reflection:}\quad
v_5(N_0)>\frac{15M}{77}.
}
\tag{11.3}
\]

balance 则有

\[
\boxed{
\text{balance:}\quad
v_5(N_0)\ge m=\lambda>\frac{3M}{7}.
}
\tag{11.4}
\]

因此 low-`m` cone 不是普通浅同余：`N_0=C_0^2+a_2^2` 必须承担随 `M` 线性增长的完整 `5`-进深度。

例如令

\[
\nu:=\left\lfloor\frac{6M}{77}\right\rfloor+1.
\]

因为 `s=0` 时 `C_0` 为 `5`-进单位，存在两种 `sqrt(-1)` phase 之一 `iota_nu` 使

\[
a_2\equiv\iota_\nu C_0\pmod{5^\nu}.
\]

代入 endpoint defects，得到

\[
\boxed{
e\equiv-9\cdot2^{M-2}\iota_\nu H\pmod{5^\nu}.}
\tag{11.5}
\]

这把两个真实 prefix defects `H,e` 直接绑在深 `5`-进两相位上。

---

## 12. `已严格完成`：low-`m` 中基础 square-depth 模数已经远大于 `C`

仍在 `s=0`。由

\[
5^{M-1}+H=2^{m+t+1}u_0
\]

定义最基础的 square-depth 尺度

\[
\mathfrak L_0:=2^{2t-1}u_0^2.
\]

`u_0` 可被完全消去：

\[
\boxed{
\mathfrak L_0
=\frac{(5^{M-1}+H)^2}{2^{2m+3}}.
}
\tag{12.1}
\]

另一方面

\[
D=\frac{(5^{M-1}+H)5^d}{4c_u},
\]

故

\[
\boxed{
\frac{\mathfrak L_0}{D}
=\frac{c_u(5^{M-1}+H)}{2^{2m+1}5^d}.
}
\tag{12.2}
\]

由

\[
m+d=2m-\lambda<\frac{51M}{77},
\qquad M\ge11,
\]

只用 `4^m<5^m` 就得到

\[
\boxed{\frac{\mathfrak L_0}{D}>\frac{25}{2}.}
\tag{12.3}
\]

结合 `C/D<3/250`：

\[
\boxed{\mathfrak L_0>1000C.}
\tag{12.4}
\]

这里仍需强调逻辑边界：`modulus >> C` 只提供极强 scale separation，不能单独推出 CRT representative 为空。后续还要控制其自然代表。

---

# 第五部分：`rho^2` Gaussian allocation 的 Archimedean 量化

## 13. `已严格完成`：二进高/低因子的赋值完全固定

primitive sphere 给出

\[
H_0^2-Y_2^2=Y_1^2+Y_3^2.
\]

在 deep-even terminal 中

\[
v_2(Y_3)=t-1,
\]

而 `Y_1` 的二进深度严格更高，所以

\[
\boxed{v_2(H_0^2-Y_2^2)=2t-2.}
\tag{13.1}
\]

`H_0,Y_2` 均为奇数，因此两个正因子

\[
H_0-Y_2,\qquad H_0+Y_2
\]

中恰有一个满足

\[
\boxed{v_2=1,}
\]

另一个满足

\[
\boxed{v_2=2t-3.}
\tag{13.2}
\]

称后者为 **high-2 factor**。

若 `rho^2` 被 square-side allocation 到 high-2 factor `F_h`，则存在正奇数 `k_h` 使

\[
\boxed{F_h=2^{2t-3}\rho^2k_h.}
\tag{13.3}
\]

因为

\[
2^{2t-3}\rho^2=\frac{g^2}{2},
\]

令

\[
G:=\frac g{10^m},
\]

并结合 (6.2±)，得到离散 Archimedean slots：

\[
\boxed{
G\in
\left(
\frac{786}{125k_h},
\frac{1607}{250k_h}
\right)
}
\tag{13.4-}
\]

或

\[
\boxed{
G\in
\left(
\frac{2389}{250k_h},
\frac{1212}{125k_h}
\right),
\qquad k_h\text{ odd}.
}
\tag{13.4+}
\]

这把 `rho^2` 的 Gaussian side choice 从纯素数分配提升成了一串彼此分离的实数槽。

任意一侧若只知道 `rho^2 | H_0±Y_2`，由 (6.2) 还得到粗高度界

\[
\boxed{
\rho<\frac{606}{125}\,2^{t-1}10^m.
}
\tag{13.5}
\]

而在 high-`m` small-source cone 中，若令

\[
n_\rho:=\frac{H_0\pm Y_2}{\rho^2},
\]

则 `n_rho` 为正偶数，并由 `rho<=u_0`、(10.2)、(6.2) 得到

\[
\boxed{n_\rho\ge956.}
\tag{13.6}
\]

所以 high-`m` source 方向中的 `rho^2` quotient 被强制推到很深的离散层。

---

## 14. `已严格完成`：low-`m` 中 high-2 allocation 迫使 `m` 接近 `M/2`

仍在 `s=0` low-`m` cone。若 `rho^2` 落到 high-2 factor，则由 (13.3) 与 (6.2) 得到

\[
2^t\rho<20\cdot10^m.
\]

再使用

\[
5^{M-1}+H=4c_u2^mg,
\]

和

\[
w=\frac{2^{M+1}c_Qc_u}{5^\lambda}<1,
\qquad \lambda\le m,
\]

可推出

\[
\boxed{m>\frac{M-2}{2}.}
\tag{14.1}
\]

所以

\[
\boxed{
m\le\frac{M-2}{2}
\Longrightarrow
\rho^2\text{ 不能进入 high-2 factor}.}
\tag{14.2}
\]

这已经把原本自由的 Gaussian side choice 在 low-`m` cone 的一大块区域中强制定向到 `v2=1` 的低因子。

---

## 15. `已严格完成`：reflection 精确中线 `M=2m` 的 high-2 分配全排除

现在进一步固定 reflection 且

\[
\boxed{M=2m.}
\]

记

\[
d=m-\lambda>0.
\]

由 `s=0` 的真实 denominator scale，

\[
\boxed{
G
=\frac{c_Q(1+H/5^{M-1})}{2w}\,5^{d-1}.
}
\tag{15.1}
\]

另一方面 high-2 allocation 必须满足 (13.4±)，特别有

\[
G<\frac{1212}{125}.
\]

由 `c_Q>=3`、`w<843/1000`，若 `d>=3`，(15.1) 的下界已经超过 `1212/125`，故

\[
\boxed{d\le2.}
\tag{15.2}
\]

### 15.1 `d=1`

此时

\[
G=\frac{c_Q(1+H/5^{M-1})}{2w}.
\]

`c_Q≡3 (mod 4)`、`5∤c_Q` 与 `G<1212/125` 只留下

\[
\boxed{c_Q\in\{3,7,11\}.}
\]

使用

\[
w<843/1000,
\qquad
w>837/1000,
\qquad
1<1+H/5^{M-1}<20/19,
\]

得到三个连续区间：

\[
\frac{1500}{843}<G<\frac{30000}{15903},
\]

\[
\frac{3500}{843}<G<\frac{70000}{15903},
\]

\[
\frac{5500}{843}<G<\frac{110000}{15903}.
\]

它们分别严格落在 (13.4±) 的相邻奇数 `k_h` slots 之间，因此都无交。

### 15.2 `d=2`

此时

\[
G=\frac{5c_Q(1+H/5^{M-1})}{2w}.
\]

`G<1212/125` 已经强迫

\[
\boxed{c_Q=3.}
\]

并有

\[
\frac{7500}{843}<G<\frac{150000}{15903}.
\]

该区间严格位于 `k_h=1` 的 low slot 上方、高 slot 下方；所有 `k_h>=3` slots 更低。因此同样无交。

综上：

\[
\boxed{
\text{reflection},\ a=9,k=2,\ M=2m
\Longrightarrow
\rho^2\text{ 不可能进入 high-2 factor}.
}
\tag{15.3}
\]

所以在这一整个可无界增长的精确中线子族中，`rho^2` 的 Gaussian side 被强制唯一：

\[
\boxed{\rho^2\text{ 只能进入 }v_2=1\text{ 的低因子}.}
\tag{15.4}
\]

这是本轮首次利用 endpoint 量化真正关闭一个无界 Gaussian-allocation 子族。

---

## 16. 固定 `eta=2m-M` 后的离散 lattice

对一般 reflection high-2 allocation，先由 (14.1) 得到

\[
2m-M>-2.
\]

因为左边是整数，暂时只有

\[
\eta:=2m-M\ge-1.
\]

若 `eta=-1`，则下面的真实 scale 退化为

\[
G=
\frac{c_Q(1+H/5^{M-1})}{w}5^d.
\]

利用 `c_Q>=3`、`d>=1`、`1+H/5^{M-1}>1` 与
`w<843/1000`，得到

\[
G>\frac{15\cdot1000}{843}
>\frac{1212}{125},
\]

这与 (13.4±) 的统一上界矛盾。因此严格得到

\[
\eta:=2m-M\ge0.
\]

真实 scale 为

\[
\boxed{
G
=\frac{c_Q(1+H/5^{M-1})}{w}
2^{-\eta-1}5^{d-\eta-1}.
}
\tag{16.1}
\]

与 (13.4±) 相等后，得到

\[
\boxed{
 c_Qk_h
=2^{\eta+2}5^{\eta+1-d}
\frac{s_\pm w}{1+H/5^{M-1}},
}
\tag{16.2}
\]

其中

\[
s_-\in(393/125,1607/500),
\qquad
s_+\in(2389/500,606/125).
\]

左边是奇整数，右边位于一个由 endpoint core 控制的窄实数带。对每个固定 `eta`，`d` 因 (16.1) 与 `G<1212/125` 自动只有有限多个可能值；前几层的粗 bound 为

\[
\eta=0:d\le2,
\quad
\eta=1:d\le3,
\quad
\eta=2:d\le4,
\quad
\eta=3:d\le6.
\]

### 16.1 `已严格完成`：`eta=1` 只剩十五个 slot 类型

在 `eta=1` 时，(16.1) 变成

\[
G=
\frac{c_Q(1+H/5^{M-1})}{w}
\frac{5^{d-2}}4.
\tag{16.3}
\]

若 `d>=4`，只用 `c_Q>=3` 与 `w<843/1000` 就有

\[
G>\frac{75\cdot1000}{4\cdot843}
>\frac{1212}{125},
\]

故不可能。若 `d=3`，则 `c_Q>=7` 时同样超过统一槽上界；而唯一还需看的 `c_Q=3` 满足

\[
\frac{3750}{843}<G<\frac{75000}{15903}.
\]

这个区间严格位于 `k_h=1` 的负号槽下方，同时位于所有
`k_h>=3` 槽的上方，所以也不相交。因此

\[
\boxed{\eta=1\Longrightarrow d\in\{1,2\}.}
\tag{16.4}
\]

再用

\[
c_Q\equiv3\pmod4,
\qquad 5\nmid c_Q,
\qquad k_h\text{ 为正奇数},
\]

以及 `837/1000<w<843/1000`、
`1<1+H/5^{M-1}<20/19`，逐个检查两个有界区间即可得到完整列表

\[
\boxed{
\begin{array}{c|c}
d& (c_Q,k_h,\text{slot})\\ \hline
1&(3,35,-),(3,51,+),(3,53,+),(7,15,-),\\
 &(7,23,+),(23,7,+),(31,5,+),(51,3,+),\\
 &(103,1,-),(107,1,-),(159,1,+),(163,1,+)\\[1mm]
2&(3,7,-),(7,3,-),(31,1,+).
\end{array}}
\tag{16.5}
\]

这里枚举的不是原问题候选，而只是由连续槽相交条件导出的十五个
`(d,c_Q,k_h,slot)` 类型；`M` 仍可无界增长。因此 (16.5) 是严格的
固定-`eta` 压缩，不是有限证书或 A2 空性。

### 16.2 `已严格完成`：拼接平面相关界把十五型降为十三型

上面的十五型只使用了彼此独立放宽的 `w`、prefix 与 sphere-factor
区间。现在恢复它们之间的精确相关性。记

\[
\chi:=1+\frac{H}{5^{M-1}}=10x,
\qquad
\mathcal H:=3+\zeta-\frac CD.
\]

由 endpoint 窗口，

\[
1<\chi<\frac{20}{19},
\qquad
\frac{997}{250}<\mathcal H<\frac{1001}{250}.
\tag{16.6}
\]

再令

\[
r:=\frac w\chi.
\]

两个 sphere factor 的精确归一化为

\[
s_\pm=\mathcal H\pm yr.
\]

在 `eta=1` 时把 (16.3) 与 `G=2s_\pm/k_h` 相等，得到

\[
\boxed{
K_{d,c_Q,k_h}
:=\frac{c_Qk_h5^{d-2}}8
=r(\mathcal H\pm yr).
}
\tag{16.7}
\]

对负号，右边在当前区间内对 `r`、`mathcal H` 单调增加，对 `y`
单调减少；因此

\[
K_-
<\frac{843}{1000}
\left(
\frac{1001}{250}
-\frac{249}{250}\frac{843}{1000}
\right)
=\frac{666891399}{250000000}
<\frac{107}{40}.
\tag{16.8}
\]

这排除 (16.5) 中的 `(d,c_Q,k_h,slot)=(1,107,1,-)`。

正号还可使用 exact concatenation plane。由

\[
(2+x)\mathcal R+10^{-M}J_{\rm def}=9+y,
\qquad
\mathcal H=w\mathcal R,
\]

得到

\[
r
=\mathcal H
\frac{2/\chi+1/10}
{9+y-10^{-M}J_{\rm def}}.
\tag{16.9}
\]

这里 `M>=11`、`J_def<3`。令

\[
a=\frac{21}{10},
\qquad
b=9-\frac3{10^{11}}.
\]

则

\[
r<\frac{1001}{250}\frac{a}{b+y}.
\]

函数

\[
\frac{a}{b+y}
\left(1+y\frac{a}{b+y}\right)
\]

在 `249/250<y<1` 上严格递增，故

\[
K_+
<
\left(\frac{1001}{250}\right)^2
\frac{a}{b+1}
\left(1+\frac{a}{b+1}\right)
<\frac{163}{40}.
\tag{16.10}
\]

这又排除 `(1,163,1,+)`。所以最终严格留下

\[
\boxed{
\begin{array}{c|c}
d& (c_Q,k_h,\text{slot})\\ \hline
1&(3,35,-),(3,51,+),(3,53,+),(7,15,-),\\
 &(7,23,+),(23,7,+),(31,5,+),(51,3,+),\\
 &(103,1,-),(159,1,+)\\[1mm]
2&(3,7,-),(7,3,-),(31,1,+).
\end{array}}
\tag{16.11}
\]

因此 `eta=1` 的 unbounded prefix family 已由十五个粗 slot 类型进一步
压成十三个相关类型。

### 16.3 `已严格完成`：prefix barrier 给出 `r>4/5`，只剩十一型

还可以把 §3 的纯前缀 barrier 送入 (16.7)。令

\[
\mathscr D(\chi,y)
:=(9+y)^2
-\left(2+\frac\chi{10}\right)^2
\left(\frac{81}{4}+\frac{y^2}{\chi^2}\right).
\]

因为 `J_def>q_0-1` 且 `zeta>1`，有

\[
\mathcal H>q_0
=\frac{9+y}{\sqrt{\mathscr D(\chi,y)}}.
\]

再由 (16.9) 中被减去的 `10^{-M}J_def` 为正，

\[
r>
\frac{2/\chi+1/10}
{\sqrt{\mathscr D(\chi,y)}}.
\tag{16.12}
\]

不等式 `r>4/5` 等价于下面的多项式在 endpoint rectangle 上为正：

\[
\begin{aligned}
\mathscr P(\chi,y)={}&
324\chi^4+12960\chi^3
-1584\chi^2y^2-28800\chi^2y+25\chi^2\\
&+640\chi y^2+1000\chi+6400y^2+10000.
\end{aligned}
\tag{16.13}
\]

在

\[
1\le\chi\le\frac{20}{19},
\qquad
\frac{249}{250}\le y\le1
\]

上直接求偏导可见 `mathscr P` 对两个变量都严格递减，而右上端点仍有

\[
\mathscr P\left(\frac{20}{19},1\right)
=\frac{160000}{130321}>0.
\]

所以严格得到

\[
\boxed{r>\frac45.}
\tag{16.14}
\]

结合 `mathcal H>997/250` 与 `y>249/250`，正号的 (16.7) 满足

\[
K_+
>\frac45
\left(
\frac{997}{250}
+\frac{249}{250}\frac45
\right)
=\frac{11962}{3125}
>\frac{153}{40}.
\tag{16.15}
\]

因此 `(1,3,51,+)` 与 `(1,51,3,+)` 两型也被排除。`eta=1`
最终只剩

\[
\boxed{
\begin{array}{c|c}
d& (c_Q,k_h,\text{slot})\\ \hline
1&(3,35,-),(3,53,+),(7,15,-),(7,23,+),\\
 &(23,7,+),(31,5,+),(103,1,-),(159,1,+)\\[1mm]
2&(3,7,-),(7,3,-),(31,1,+).
\end{array}}
\tag{16.16}
\]

这十一型只对应五个不同的相关高度：

\[
K_-\in\left\{\frac{103}{40},\frac{21}{8}\right\},
\qquad
K_+\in\left\{\frac{31}{8},\frac{159}{40},\frac{161}{40}\right\}.
\tag{16.17}
\]

### 16.4 `已严格完成`：Gaussian norm 的素数支持只留下五型

在 `s=0` reflection 中，primitive coordinates 还给出

\[
Y_1=g\frac{9b_3}{2},
\qquad
Y_3=ga_3.
\]

若 `rho^2` 进入 high-2 factor，写另一个低因子为 `2ell`，则

\[
\begin{aligned}
(H_0-Y_2)(H_0+Y_2)
&=g^2\left(\left(\frac{9b_3}{2}\right)^2+a_3^2\right)\\
&=2^{2t-2}\rho^2 k_h\ell.
\end{aligned}
\]

消去 `g^2=2^{2t-2}rho^2` 后得到

\[
\boxed{
k_h\ell
=\left(\frac{9b_3}{2}\right)^2+a_3^2.
}
\tag{16.18}
\]

特别地，`k_h` 必须整除右边的 primitive Gaussian norm。deep-even
中 `5\mid b_3`，而 `gcd(a_3,b_3)=1`，故

\[
\boxed{5\nmid k_h.}
\tag{16.19}
\]

再设 `p\equiv3 (mod 4)`、`p\ne3` 且 `p\mid k_h`。由二平方和的
局部定理，(16.18) 强迫

\[
p\mid\frac{9b_3}{2},
\qquad
p\mid a_3.
\]

因为 `p` 为奇数且 `p\ne3`，第一式推出 `p\mid b_3`，与
`gcd(a_3,b_3)=1` 矛盾。因此

\[
\boxed{
p\mid k_h, p\equiv3\pmod4
\Longrightarrow p=3.
}
\tag{16.20}
\]

把 (16.19)–(16.20) 施加到 (16.16)，含 `5`、`7` 或 `23` 的六型
全部排除，最终只剩

\[
\boxed{
\begin{array}{c|c}
d& (c_Q,k_h,\text{slot})\\ \hline
1&(3,53,+),(103,1,-),(159,1,+)\\[1mm]
2&(7,3,-),(31,1,+).
\end{array}}
\tag{16.21}
\]

对应的相关高度只有四个：

\[
K_-\in\left\{\frac{103}{40},\frac{21}{8}\right\},
\qquad
K_+\in\left\{\frac{31}{8},\frac{159}{40}\right\}.
\tag{16.22}
\]

这一步首次把 `eta=1` 的 Archimedean slot 与 Gaussian norm
的素数支持直接联立。最后的 `k_h=3` 还能严格推出一个特殊结构，但
**不能**仅凭整体本原性排除。若 `k_h=3`，则 (16.18) 右边作为二平方和
具有偶数 `3`-进赋值，故 `3\mid ell`。于是 `3` 同时整除 high-2 与
low-2 两个因子，即

\[
3\mid H_0-Y_2,
\qquad
3\mid H_0+Y_2.
\]

从而 `3\mid H_0,Y_2`；再由

\[
H_0^2-Y_2^2=Y_1^2+Y_3^2
\]

及 `-1` 在模 `3` 下非平方，得到 `3\mid Y_1,Y_3`。在唯一对应类型
`(d,c_Q,k_h,slot)=(2,7,3,-)` 中，这进一步给出

\[
\boxed{3\mid a_2,qquad 3\mid a_3,qquad 3\nmid b_2b_3.}
\tag{16.23}
\]

这里不能把 `H_0,Y_1,Y_2,Y_3` 自动视为整体本原：全局 primitive
recovery 只给逐坐标 gcd 恒等式，并不排除四坐标共享 `3`。同样，虽然
三个 numerator block 此时都被 `3` 整除，把它们同时除以 `3` 会使
第三分子的位数从 `m+1` 降到 `m`，不保持原 decimal coefficient
plane。因此“除以 `3` 下降到正常 chamber”也是无效的。

所以 `k_h=3` 类型仍保留在 (16.21)。另外三个 `k_h=1` 类型已经达到
high factor 的最小奇 quotient；剩余推进必须使用 exact factor
equality，而不能再从一般 slot 宽度获得额外下降。

### 16.5 `已严格完成`：剩余五型的 exact factor phase

对 (16.21) 中的三个 `k_h=1` 类型，high factor 与 low factor 分别为

\[
\frac{g^2}{2},
\qquad
2\mathscr N,
\qquad
\mathscr N:=\left(\frac{9b_3}{2}\right)^2+a_3^2.
\]

按正负 slot 解出 `Y_2`，得到

\[
Y_2=
\begin{cases}
g^2/4-\mathscr N,&+\text{ slot},\\
\mathscr N-g^2/4,&-\text{ slot}.
\end{cases}
\tag{16.24}
\]

另一方面

\[
Y_2=a_2c_Q5^d,
\qquad
c_Q5^d\mid\frac{9b_3}{2}.
\]

因此三个 `k_h=1` 类型都满足

\[
\boxed{
\left(\frac g{2a_3}\right)^2
\equiv1\pmod{c_Q5^d}.
}
\tag{16.25}
\]

这里 `g/2` 与 `a_3` 都是模数单位。对应的完整相位表为

\[
\begin{array}{c|c|c}
(d,c_Q,k_h)&c_Q5^d&g/(2a_3)\pmod{c_Q5^d}\\ \hline
(1,103,1)&515&1,104,411,514\\
(1,159,1)&795&1,211,266,319,476,529,584,794\\
(2,31,1)&775&1,249,526,774.
\end{array}
\tag{16.26}
\]

对剩下的 `(d,c_Q,k_h,slot)=(1,3,53,+)`，(16.18) 先给出

\[
53\mid\mathscr N.
\]

若 `53\mid c_u`，则 `53\mid b_3`，由既约性 `53\nmid a_3`，从而
`mathscr N` 模 `53` 非零，矛盾。因此

\[
\boxed{53\nmid c_u.}
\tag{16.27}
\]

并且 Gaussian phase 被固定为

\[
\boxed{
\frac{9b_3}{2a_3}
\equiv23\text{ 或 }30\pmod{53}.
}
\tag{16.28}
\]

再由 high/low factor 的精确值

\[
H_0+Y_2=\frac{53g^2}{2},
\qquad
H_0-Y_2=\frac{2\mathscr N}{53},
\]

可得第二条单位相位

\[
\boxed{
\left(\frac{53g}{2a_3}\right)^2
\equiv1\pmod{15}.
}
\tag{16.29}
\]

所以 `eta=1` 的五型已经不再是连续 slot 问题，而是 (16.25)–(16.29)
的有限 CRT phase 加上仍无界的 prefix/source 参数。下一步需要把这些
相位与 `Q_0=c_Qq_Q` 和 Hensel slot (9.3)–(9.5) 联立；单独列出相位
仍不能推出空性。

### 16.6 `失效/降级`：单靠粗 slot 不能统一排除所有 `eta`

原先希望直接证明 (16.2) 对每个 `eta>=0` 都没有整数带交点。这个目标若只使用本节已有的实数窗，则已经是假的。最小的明确见证为

\[
(\eta,d,c_Q,k_h,\text{slot})=(1,2,31,1,+).
\]

此时 (16.3) 给出

\[
\frac{7750}{843}
<G<
\frac{155000}{15903},
\]

而 `k_h=1` 的正号槽是

\[
\frac{2389}{250}<G<\frac{1212}{125}.
\]

两区间严格相交，因为

\[
\frac{7750}{843}<\frac{2389}{250},
\qquad
\frac{1212}{125}<\frac{155000}{15903}.
\]

所以后续不能再以“统一 slot exclusion”本身作为目标；必须把
`c_Q\mid Q_0`、source split、平方单边 allocation 的自然代表或
`C` 的 CRT phase 至少加入一项，才能继续排除 (16.21) 及更高 `eta`。

因此整个 reflection high-2 cone 已经被重写为离散 lattice

\[
\boxed{(\eta,d,c_Q,k_h)}
\]

上的窄整数带问题。`eta=0` 已由 §15 全部关闭，`eta=1` 已压成
(16.21) 的五个类型；但粗 slot 在 `eta>=1` 确有交点，不能单独闭环。

### 16.7 `已严格完成`：与 `eta` 无关的定向因子系统

固定任意 reflection high-2 allocation；本节不再固定 `eta`。令

\[
B:=c_Q5^d,
\qquad
\varepsilon\in\{-1,+1\},
\]

其中 \(\varepsilon\) 由 high-2 factor 的实际一侧定义：

\[
\boxed{
H_0+\varepsilon Y_2
=\frac{g^2k_h}{2}.
}
\tag{16.30}
\]

另一个因子必为 \(2\mathscr N/k_h\)。因此存在正奇数 \(\ell\) 满足

\[
\boxed{
k_h\ell=\mathscr N
=\left(\frac{9b_3}{2}\right)^2+a_3^2.
}
\tag{16.31}
\]

这里不需要固定任何 `eta`。因为 `B | b_3` 且
`gcd(a_3,b_3)=1`，立即有

\[
\gcd(\mathscr N,B)=1.
\]

结合 \(k_h\mid\mathscr N\) 得到统一互素性

\[
\boxed{\gcd(k_h,c_Q5^d)=1.}
\tag{16.32}
\]

这比只逐个排除 `k_h` 的某些素因子更直接：high quotient 与整个
第三分母的奇数块互素。

现在记 `c_Q=c_-c_+` 为 §13 中由第三坐标两因子决定的完整
prime-power allocation。reflection 中 \(E=\lambda\)，故

\[
H_0-Y_3=5^\lambda c_-^2X,
\qquad
H_0+Y_3=c_+^2Y,
\tag{16.33}
\]

且

\[
Y_2=a_2c_Q5^d,
\qquad
Y_3=ga_3.
\tag{16.34}
\]

由 source split 的互素性和 `s=0`，

\[
\gcd(g,c_Q5^d)=1.
\tag{16.35}
\]

定义偶整数

\[
\boxed{X_h:=\frac{k_hg}{2}.}
\tag{16.36}
\]

把 (16.30) 分别模 `5^d`、`c_-`、`c_+` 观察。因为
\(\lambda>d\)，(16.33) 给出

\[
H_0\equiv Y_3\pmod{5^d c_-},
\qquad
H_0\equiv-Y_3\pmod{c_+}.
\]

而 `Y_2` 被 `c_Q5^d` 整除。对 (16.30) 消去模数单位 `g`，得到
不含 `eta` 的**定向平方根锁**

\[
\boxed{
X_h\equiv a_3\pmod{5^dc_-},
\qquad
X_h\equiv-a_3\pmod{c_+}.
}
\tag{16.37}
\]

所以此前由

\[
\left(\frac{k_hg}{2a_3}\right)^2\equiv1\pmod{c_Q5^d}
\]

看起来产生的独立正负平方根，实际上已经被 `c_- / c_+`
square-side allocation 唯一定向；特别地，`5^d` 一侧永远取正根，
不是可逐层选择的相位。

由 (6.2±) 有 `X_h/T>393/125`，而 `a_3/T<251/250`，其中
`T=10^m`。故 `X_h>a_3`。于是存在正奇数 `r_-,r_+` 使

\[
\boxed{
X_h-a_3=c_-5^dr_-,
\qquad
X_h+a_3=c_+r_+.
}
\tag{16.38}
\]

相加、相减给出第一个完全离散的线性系统

\[
\boxed{
c_+r_+ + c_-5^dr_-=k_hg,
\qquad
c_+r_+ - c_-5^dr_-=2a_3.
}
\tag{16.39}
\]

另一方面，由 high/low 两因子的差，

\[
X_h^2-\mathscr N
=\varepsilon a_2Bk_h.
\]

结合 (16.38) 后可消去平方，得到

\[
\boxed{
r_-r_+
=\frac{81b_3^2}{4c_Q5^d}
+\varepsilon a_2k_h.
}
\tag{16.40}
\]

最后，把 (16.38) 直接代回 (16.30)、(16.33)。分别减去和加上
`Y_3=ga_3`，得到两个定向的 mixed-factor 等式：

\[
\boxed{
gr_- -\varepsilon a_2c_+
=5^{\lambda-d}c_-X,
}
\tag{16.41-}
\]

\[
\boxed{
gr_+ -\varepsilon a_2c_-5^d
=c_+Y.
}
\tag{16.41+}
\]

特别地，第一式给出随高度增长的统一相位

\[
\boxed{
gr_-\equiv\varepsilon a_2c_+
\pmod{5^{\lambda-d}}.
}
\tag{16.42}
\]

这条相位可以与 source 双 Hensel 直接合并，而不固定 `eta`。由

\[
g\omega=5^\lambda q+c_u,
\qquad
c_Q\omega-\theta=2^m5^\lambda c_u,
\]

在模 \(5^{\lambda-d}\) 下分别有
\(g\omega\equiv c_u\) 与 \(\theta\equiv c_Q\omega\)。因此
(16.42) 推出

\[
\boxed{
c_ur_-\equiv\varepsilon a_2c_+\omega
\pmod{5^{\lambda-d}},
}
\tag{16.43a}
\]

\[
\boxed{
c_-c_ur_-\equiv\varepsilon a_2\theta
\pmod{5^{\lambda-d}}.
}
\tag{16.43b}
\]

在当前 low-`m` reflection cone，§11 的精确范数深度为

\[
\nu_5:=v_5(N_0)=3\lambda-2m=\lambda-2d>0.
\]

取唯一两相位之一 `iota` 满足

\[
\iota^2\equiv-1\pmod{5^{\nu_5}},
\qquad
a_2\equiv\iota C_0\pmod{5^{\nu_5}}.
\]

又因

\[
C_0=\frac{9b_2}{2}
=9\cdot2^{M+m}c_ug,
\]

把 (16.43a) 降到模 \(5^{\nu_5}\)，再用
\(g\omega\equiv c_u\pmod{5^{\nu_5}}\) 并消去单位 \(c_u\)，得到纯
source/Gaussian 相位

\[
\boxed{
r_-
\equiv
\varepsilon\iota\,9\cdot2^{M+m}c_+c_u
\pmod{5^{\lambda-2d}}.
}
\tag{16.44}
\]

(16.44) 已经同时使用了 high/low exact equality、`c_Q` 的
square-side allocation、source Hensel 与深前缀范数；其中不再出现
任何固定层的相位表。

reflection 条件 `m=lambda+d <=3lambda/2` 说明

\[
\lambda-d=m-2d\ge\frac{\lambda}{2},
\]

所以 (16.42) 的深度随无界参数线性增长。它不是固定 `eta` 的有限
相位表，而是覆盖整个 reflection high-2 cone 的精确必要条件。

本节还没有证明 (16.31)、(16.39)–(16.44) 无解；严格的新边界是：
后续不应再枚举 `eta`，而应证明这个定向正奇数因子系统与 source
双 Hensel / prefix defect 不相容，或由它构造保持 decimal plane 的
下降。

### 16.8 `已严格完成`：统一 Gaussian norm transfer 与 extra-`d` alignment

(16.39)–(16.41) 还可以消去 `r_+` 和 `a_2`。具体地，用
(16.39) 的第一式把 `c_+r_+` 代入 (16.40)，再用 (16.41-) 消去
\(gr_- - \varepsilon a_2c_+\)，得到

\[
\boxed{
r_-^2+
\left(\frac{9b_3}{2c_-5^d}\right)^2
=k_h5^{\lambda-2d}X.
}
\tag{16.45}
\]

记

\[
\boxed{
R_3:=\frac{9b_3}{2c_-5^d}
=9\cdot2^{M+m}c_+c_u.
}
\tag{16.46}
\]

则 (16.45) 是完全不含 `eta` 的新 Gaussian norm。它还有近本原性：

\[
\boxed{\gcd(r_-,R_3)\mid9.}
\tag{16.47}
\]

证明如下。由 (16.38)，任何同时整除 `r_-` 与 `c_+` 的奇素数都同时
整除 `X_h-a_3` 与 `X_h+a_3`，因而整除 `a_3`；但 `c_+ | b_3`，这与
`gcd(a_3,b_3)=1` 矛盾。再设 `p | c_u` 且 `p | r_-`。由

\[
(H_0-Y_3)(H_0+Y_3)=Y_1^2+Y_2^2
\]

和 (16.33)–(16.34) 消去 `c_Q^2 5^{2d}`，得到

\[
\boxed{XY=\frac{N_0}{5^{\lambda-2d}}.}
\tag{16.48}
\]

由于 `p | c_u | b_2`、`gcd(a_2,b_2)=1`，有
\(N_0=C_0^2+a_2^2\not\equiv0\pmod p\)，所以 \(p\nmid X\)。同时
(16.32) 给出 \(p\nmid k_h\)。但 \(p\mid r_-,R_3\) 会由 (16.45) 推出
\(p\mid k_hX\)，矛盾。\(c_u\) 只含 \(1\bmod4\) 素数，故剩余公共素数只能
是显式系数 `9` 中的 `3`。若 `3 | c_+`，前一 `c_+` 论证又排除
`3 | r_-`；若 \(3\nmid c_+\)，则 `v_3(R_3)=2`。这就证明 (16.47)。

现在令

\[
\nu_5=\lambda-2d.
\]

由 `gcd(C,D)=1` 且 `5 | D`，有 \(5\nmid C\)；再由
`c_-^2X=3D-C`，可知 \(5\nmid X\)。结合 (16.32)，(16.45) 因而给出

\[
\boxed{v_5(r_-^2+R_3^2)=\nu_5.}
\tag{16.49}
\]

原 prefix norm 同样满足

\[
v_5(a_2^2+C_0^2)=\nu_5.
\]

(16.44) 正好说明两个 Gaussian 整数

\[
Z_r:=r_-+i\varepsilon R_3,
\qquad
Z_a:=a_2+iC_0
\]

在 \(5=(2+i)(2-i)\) 上把全部 \(\nu_5\) 深度分配到同一个 Gaussian
prime orientation。故存在
\(\pi_\iota\in\{2+i,2-i\}\) 使

\[
\boxed{
\mathcal R_5:=\frac{Z_r}{\pi_\iota^{\nu_5}},
\qquad
\mathcal A_5:=\frac{Z_a}{\pi_\iota^{\nu_5}}
\in\mathbb Z[i],
}
\tag{16.50}
\]

并且

\[
N(\mathcal R_5)=k_hX,
\qquad
N(\mathcal A_5)=XY.
\tag{16.51}
\]

更关键的是，两原向量的行列式可以由 (16.41-) 精确求出。利用

\[
\frac{C_0}{g}=9\cdot2^{M+m}c_u,
\qquad
R_3=\frac{C_0c_+}{g},
\]

得到

\[
\begin{aligned}
r_-C_0-\varepsilon a_2R_3
&=\frac{C_0}{g}
\left(gr_- -\varepsilon a_2c_+\right)\\
&=9\cdot2^{M+m}c_uc_-X\,5^{\lambda-d}.
\end{aligned}
\tag{16.52}
\]

右端除显式五次幂外为 `5`-进单位，所以

\[
\boxed{
v_5(r_-C_0-\varepsilon a_2R_3)
=\lambda-d=\nu_5+d.
}
\tag{16.53}
\]

同时除去 (16.50) 中共同的 Gaussian factor 会把有向面积除以
\(5^{\nu_5}\)。于是规范化后的两个 `5`-primitive Gaussian 向量满足

\[
\boxed{
v_5\!\left(
\operatorname{Im}
(\mathcal R_5\overline{\mathcal A_5})
\right)=d.
}
\tag{16.54}
\]

这不是把一个 exact-lift 解自动变成另一个十进制解；因此这里不把
(16.50) 冒充保持 coefficient plane 的无限下降。严格含义是：整个
reflection high-2 cone 已归一化为两条 `5`-primitive Gaussian 向量，
其范数由 (16.51) 控制，而它们的 projective 方向仍被迫额外对齐恰好
`d` 位。后续全局矛盾应从这条 extra-`d` alignment 的 Archimedean
高度下界，或从 source Hensel 对该 projective 类的禁止性得到。

### 16.9 `已严格完成`：互补 Gaussian norm 与精确 composition

前述 norm transfer 还有一个完全对称的同伴。定义

\[
\boxed{
R_1:=9\cdot2^{M+m}c_uc_-5^d
=\frac{9b_3}{2c_+}.
}
\tag{16.55}
\]

用 (16.39) 消去 `r_-`，并用 (16.41+) 消去
\(gr_+ - \varepsilon a_2c_-5^d\)，与 (16.45) 相同的计算给出

\[
\boxed{r_+^2+R_1^2=k_hY.}
\tag{16.56}
\]

同样有

\[
\boxed{\gcd(r_+,R_1)\mid9.}
\tag{16.57}
\]

其证明与 (16.47) 对称：`r_+` 与 `c_-5^d` 共享奇素数会同时整除
`X_h-a_3` 与 `X_h+a_3`；`c_u` 中的素数则由
\(XY=N_0/5^{\nu_5}\)、`gcd(a_2,b_2)=1` 和 (16.56) 排除。唯一未被
该论证排除的是显式系数 `9` 中的 `3`。

两条 norm transfer 并非互不相关。令 (16.50) 中的
\(\mathcal R_5,\mathcal A_5\) 保持不变。直接展开 Gaussian 乘积，并使用
(16.41±)、(16.48)，可得精确 composition identity

\[
\boxed{
\mathcal R_5\overline{\mathcal A_5}
=X\left(\varepsilon r_+-iR_1\right).
}
\tag{16.58}
\]

为核对实部，先有

\[
\begin{aligned}
g(r_-a_2+\varepsilon R_3C_0)
&=\varepsilon c_+(a_2^2+C_0^2)
+5^{\nu_5+d}a_2c_-X\\
&=5^{\nu_5}X
\left(\varepsilon c_+Y+5^da_2c_-\right)\\
&=5^{\nu_5}X\,\varepsilon gr_+,
\end{aligned}
\]

其中最后一步正是 (16.41+)。虚部则由 (16.52) 给出
\(-5^{\nu_5}XR_1\)。两者同时除以 \(5^{\nu_5}\) 即得 (16.58)。取范数
后 (16.56) 也立刻从 (16.51)、(16.58) 恢复。

所以任意 reflection high-2 候选必须同时提供两条近本原二平方表示

\[
\boxed{
r_-^2+R_3^2=k_h5^{\nu_5}X,
\qquad
r_+^2+R_1^2=k_hY,
}
\tag{16.59}
\]

并由同一个 Gaussian composition (16.58) 耦合。后续可以逐 Gaussian
prime 比较 `k_h` 在两条表示中的 orientation；这是一项统一的素因子
分配问题，不再是固定 `eta` 的整数槽枚举。

### 16.10 `已严格完成`：除 `3` 外的共同 Gaussian divisor 可整体消去

(16.58) 还允许使用 `Z[i]` 的唯一分解，而不需要枚举 `eta`。先注意

\[
\gcd(a_2,C_0)\mid9.
\tag{16.60}
\]

这是因为 `C_0=9b_2/2`、`a_2` 为奇数且 `gcd(a_2,b_2)=1`。除去
共同的 Gaussian `5`-factor 不改变任何 \(p\notin\{3,5\}\) 的逐坐标
本原性。因此 (16.47)、(16.57)、(16.60) 说明

\[
\mathcal A_5,
\quad
\mathcal R_5,
\quad
\varepsilon r_+-iR_1
\]

在每个 \(p\notin\{3,5\}\) 处都不可能同时被 `p` 的两个 Gaussian
orientation 整除。

写

\[
X_{(3)}:=\frac{X}{3^{v_3(X)}}.
\]

则存在 Gaussian 整数 `alpha_X` 满足

\[
\boxed{
N(\alpha_X)=X_{(3)},
\qquad
\alpha_X\mid\mathcal A_5,
\qquad
\alpha_X\mid\mathcal R_5.
}
\tag{16.61}
\]

证明只需逐个素数幂。设 `p^x || X_(3)`。若 `p=2` 或 `5`，由
所有当前因子均为奇数、`5`-primitive 可直接排除；若
\(p\equiv3\pmod4\)，\(p\mid N(\mathcal A_5)=XY\) 会迫使 `p` 同时整除
\(\mathcal A_5\) 两坐标，与 (16.60) 矛盾。因此

\[
p=1\pmod4,
\qquad
p=\pi\bar\pi
\]

在 \(\mathbb Z[i]\) 中分裂。由 `p`-本原性，\(N(\mathcal A_5)=XY\) 中的全部
`p` 次数都落在唯一一个 orientation；不妨该 orientation 为 `pi`。
于是

\[
v_\pi(\mathcal A_5)=v_p(X)+v_p(Y),
\qquad
v_\pi(\overline{\mathcal A_5})=0.
\]

对 composition (16.58) 取 `pi`-进赋值：右边显式含
`pi^{v_p(X)}`，故

\[
v_\pi(\mathcal R_5)\ge v_p(X).
\]

逐 `p` 相乘即构造出 (16.61)。所以所有非 `3` 的 `X`-部分都是真正
的共同 Gaussian divisor，而不只是两个范数中偶然出现的共同整数。

唯一剩余的 UFD cancellation 缺陷来自惰性素数 `3`，并且它的深度
绝对有界。事实上

\[
\boxed{v_3(N_0)\in\{0,2,4\}.}
\tag{16.62}
\]

若 \(3\nmid a_2\)，这是模 `3` 立即可见的；若 `v_3(a_2)=1`，则
`C_0^2` 至少含 `3^4` 而 `a_2^2` 恰含 `3^2`；若
\(v_3(a_2)\ge2\)，由 \(3\nmid b_2\)，除以 `3^4` 后
`(C_0/9)^2+(a_2/9)^2` 模 `3` 非零。因此只有 (16.62) 三种深度。
结合 (16.48)，

\[
v_3(X)+v_3(Y)\le4.
\tag{16.63}
\]

再设 `3 | k_h`。由 (16.32) 有 \(3\nmid c_Q\)，而 `c_u` 只含
`1 mod 4` 素数，故 (16.46)、(16.55) 中

\[
v_3(R_3)=v_3(R_1)=2.
\]

对任意整数 `z`，此时 `v_3(z^2+R_j^2)` 只能是 `0,2,4`。施加到
(16.45)、(16.56) 得到

\[
\boxed{
v_3(k_h)+v_3(X)\le4,
\qquad
v_3(k_h)+v_3(Y)\le4,
}
\tag{16.64}
\]

特别地

\[
\boxed{v_3(k_h)\le4.}
\tag{16.65}
\]

因此 composition 的无界 prime allocation 已严格分成两部分：

- `X_(3)` 的全部 split prime powers 可由 (16.61) 一次整体消去；
- 不能这样消去的 `3`-primary defect，其三个赋值
  `v_3(k_h),v_3(X),v_3(Y)` 都被绝对常数 `4` 控制。

这仍不是 decimal-plane-preserving descent，因为除去 `alpha_X` 后的
Gaussian 坐标未被证明重新对应合法十进制 blocks；但它把潜在失败
精确隔离在一个有界 `3`-primary obstruction，而不是任意无界素数库。

### 16.11 `已严格完成`：奇 `3`-primary defect 只有两个赋值通道

令

\[
e_3:=v_3(k_h),
\qquad
u_2:=v_3(a_2),
\qquad
u_3:=v_3(a_3).
\]

本节精确分类 `e_3` 为奇数的情形。由 (16.31)，`3 | k_h` 先迫使
\(3\mid\mathscr N\)。因为 `9b_3/2` 已含 `3^2`，而 (16.32) 给出
\(3\nmid b_3\)，所以

\[
u_3\ge1,
\qquad
v_3(\mathscr N)=
\begin{cases}
2,&u_3=1,\\
4,&u_3\ge2.
\end{cases}
\tag{16.66}
\]

high factor 与 low factor 的精确 `3`-进深度分别为

\[
v_3(H_0+\varepsilon Y_2)=e_3,
\qquad
v_3(H_0-\varepsilon Y_2)=v_3(\mathscr N)-e_3.
\tag{16.67}
\]

这里 \(3\nmid g\)：事实上 `e_3` 为奇数时，(16.67) 两边都含 `3`，
故 `3 | Y_2=a_2c_Q5^d`；再由 (16.32) 得 `3 | a_2`，于是
`gcd(a_2,b_2)=1` 排除 `3 | b_2`，而 `g | b_2`。因此

\[
3\nmid g,
\qquad
3\nmid b_2b_3.
\tag{16.68}
\]

若 (16.67) 的两个深度不同，则其差的一半
`Y_2` 的赋值恰为二者的最小值；若二者相同，则 `Y_2` 的赋值至少为
这个公共值。

先设 `u_3=1`。由 (16.66) 总深度为 `2`，奇数 `e_3` 只能等于 `1`，
两个因子深度同为 `1`，所以暂得 `u_2>=1`。但若 `u_2=1`，把球面式

\[
H_0^2=Y_1^2+Y_2^2+Y_3^2
\]

除以 `9` 后，`Y_1/3` 仍被 `3` 整除，而 `Y_2/3,Y_3/3` 都是单位；
右边模 `3` 等于 `2`，不可能为平方。因此

\[
u_3=1
\Longrightarrow
e_3=1,quad u_2\ge2.
\tag{16.69}
\]

再设 `u_3>=2`。此时 (16.66) 的总深度为 `4`，故
\(e_3\in\{1,3\}\)。high/low 深度为 `(1,3)` 或 `(3,1)`，不相等，
所以它们之差的一半恰含一个 `3`：

\[
u_3\ge2
\Longrightarrow
u_2=1,quad e_3\in\{1,3\}.
\tag{16.70}
\]

综上，奇 `3`-primary defect 只有两个互斥通道：

\[
\boxed{
e_3\text{ odd}
\Longrightarrow
\begin{cases}
u_3=1,\ e_3=1,\ u_2\ge2,\\
\text{or}\\
u_2=1,\ u_3\ge2,\ e_3\in\{1,3\}.
\end{cases}
}
\tag{16.71}
\]

还可把这一局部分类送回全局拼接平面。记原拼接分子、分母为
`alpha,beta`，球面 LCM 为 `q`，高度为 `H`。由 (16.68)，
\(3\nmid q\)。在 (16.69) 中，三个球面坐标的 `3`-进深度分别至少为
`(2,2,1)`；在 (16.70) 中则至少为 `(2,1,2)`。两种情形的最小深度
都唯一出现，所以

\[
\boxed{v_3(H)=1.}
\tag{16.72}
\]

另一方面，`a_1=9`，且 (16.71) 中 `a_2,a_3` 恰有一个只含一个
`3`；十进制幂是 `3`-进单位，故原拼接分子也满足

\[
\boxed{v_3(\alpha)=1.}
\tag{16.73}
\]

最后由整数平面 `qalpha=Hbeta` 得到

\[
\boxed{e_3\text{ odd}\Longrightarrow v_3(\beta)=0.}
\tag{16.74}
\]

所以未能被 (16.61) 整体消去的奇 `3` 缺陷不再是任意公共因子：它
只能处于 (16.71) 的两个通道，并且强制真实 denominator
concatenation 为 `3`-进单位。下一步需要把 (16.74) 与
`beta=2\cdot10^{M+m}+b_2 10^m+b_3` 的 source/Hensel 表达联立。

### 16.12 `已严格完成`：平衡转移一个 `3` 后得到完整共同 Gaussian divisor

§16.10 把 `X` 的非 `3` 部分整体消去，§16.11 分类了奇 `3` 通道。
事实上，在 Gaussian UFD 层面连这个奇性也可以统一处理。记

\[
x_3:=v_3(X),
\qquad
y_3:=v_3(Y),
\qquad
e_3:=v_3(k_h).
\]

由 (16.51) 与 (16.56)，三个近本原 Gaussian norm 分别为

\[
N(\mathcal A_5)=XY,
\qquad
N(\mathcal R_5)=k_hX,
\qquad
N(\varepsilon r_+-iR_1)=k_hY.
\]

因为 `3` 在 `Z[i]` 中惰性，每个 Gaussian norm 中的 `3`-进次数
必须为偶数。因此

\[
x_3+y_3\equiv e_3+x_3\equiv e_3+y_3\equiv0\pmod2,
\]

也即

\[
\boxed{x_3\equiv y_3\equiv e_3\pmod2.}
\tag{16.75}
\]

令

\[
\boxed{
\delta:=x_3\bmod2\in\{0,1\},
\qquad
X^\sharp:=3^\delta X.
}
\tag{16.76}
\]

则存在 Gaussian 整数 `alpha_X^sharp` 满足

\[
\boxed{
N(\alpha_X^\sharp)=X^\sharp,
\qquad
\alpha_X^\sharp\mid\mathcal A_5,
\qquad
\alpha_X^\sharp\mid\mathcal R_5.
}
\tag{16.77}
\]

对所有 \(p\ne3\) 的素数幂，构造与 (16.61) 完全相同。对 `p=3`，
取普通整数 Gaussian factor

\[
3^{(x_3+\delta)/2}.
\]

它的 norm 为 \(3^{x_3+\delta}\)。又由 (16.75)，当 `delta=1` 时
`y_3,e_3>=1`；故

\[
\frac{x_3+\delta}{2}
\le
\frac{x_3+y_3}{2},
\qquad
\frac{x_3+\delta}{2}
\le
\frac{x_3+e_3}{2}.
\]

右边分别是 \(\mathcal A_5,\mathcal R_5\) 两坐标的共同 `3`-进深度，
所以这个普通整数 factor 同时整除二者。与非 `3` 部分相乘即得
(16.77)。

于是存在 \(\mathcal B_5,\mathcal G_5\in\mathbb Z[i]\) 使

\[
\boxed{
\mathcal A_5=\alpha_X^\sharp\mathcal B_5,
\qquad
\mathcal R_5=\alpha_X^\sharp\mathcal G_5,
}
\tag{16.78}
\]

并且

\[
\boxed{
N(\mathcal B_5)=\frac{Y}{3^\delta},
\qquad
N(\mathcal G_5)=\frac{k_h}{3^\delta}.
}
\tag{16.79}
\]

把 (16.78) 代回 composition (16.58)，利用
\(N(\alpha_X^\sharp)=3^\delta X\) 并消去 `X`，进一步得到

\[
\boxed{
\varepsilon r_+-iR_1
=3^\delta\mathcal G_5\overline{\mathcal B_5}.
}
\tag{16.80}
\]

当 `delta=1` 时，(16.80) 同时重新推出 `3 | r_+,R_1`，与 §16.11
的奇通道完全一致。

因此，经过至多平衡转移一份 `3`，**所有** rational prime powers
都能在 `Z[i]` 中形成真正的共同 divisor；不再剩下无界或有界的 UFD
factor-allocation 障碍。当前唯一未完成的关键是：

\[
\boxed{
\text{证明 (16.78) 的共同因子约分必然保持原 decimal coefficient plane}
}
\]

并产生严格更小的合法 A2 候选；另一条可闭环的路线是直接从
(16.78)–(16.80) 与原平面的强制关系推出矛盾。必须强调：只证明
quotient **不**保持十进制平面并不能排除原候选，那只会使下降路线
失效。本文尚未得到 plane covariance 或直接矛盾，因此不提前宣称
无限下降。

### 16.13 `已严格完成`：共同因子约分后的纯 Gaussian Hensel kernel

共同 divisor (16.77) 可以从 source Hensel 兼容式中完全消去。先在
约分前定义

\[
Z_r=r_-+i\varepsilon R_3,
\qquad
Z_a=a_2+iC_0.
\]

由 (16.41-) 乘以 `omega`，再代入

\[
g\omega=5^\lambda q+c_u,
\qquad
\lambda=\nu_5+2d,
\]

实部精确给出

\[
c_ur_- -\varepsilon c_+\omega a_2
=5^{\nu_5+d}
\left(c_-X\omega-5^dqr_-\right).
\tag{16.81a}
\]

另一方面，由 `R_3=C_0c_+/g`，

\[
\begin{aligned}
c_uR_3-c_+\omega C_0
&=R_3(c_u-g\omega)\\
&=-5^\lambda qR_3\\
&=-5^{\nu_5+d}\,5^dqR_3.
\end{aligned}
\tag{16.81b}
\]

合并实虚部：

\[
\boxed{
c_uZ_r-\varepsilon c_+\omega Z_a
=5^{\nu_5+d}
\left(
c_-X\omega-5^dqr_-
-i\varepsilon5^dqR_3
\right).
}
\tag{16.82}
\]

按 (16.50) 取 \(\pi_\iota\) 使

\[
Z_r=\pi_\iota^{\nu_5}\mathcal R_5,
\qquad
Z_a=\pi_\iota^{\nu_5}\mathcal A_5.
\]

又

\[
5^{\nu_5+d}
=\pi_\iota^{\nu_5+d}\bar\pi_\iota^{\nu_5+d}.
\]

从 (16.82) 消去共同的 \(\pi_\iota^{\nu_5}\)，得到

\[
\pi_\iota^d\bar\pi_\iota^{\nu_5+d}
\mid
c_u\mathcal R_5
-\varepsilon c_+\omega\mathcal A_5.
\tag{16.83}
\]

最后代入 (16.78)。因为
\(N(\alpha_X^\sharp)=3^\delta X\) 与 `5` 互素，可在
\(\mathbb Z[i]\) 中消去 \(\alpha_X^\sharp\)，得到纯 quotient kernel

\[
\boxed{
\pi_\iota^d\bar\pi_\iota^{\nu_5+d}
\mid
c_u\mathcal G_5
-\varepsilon c_+\omega\mathcal B_5.
}
\tag{16.84}
\]

由于

\[
N\!\left(\pi_\iota^d\bar\pi_\iota^{\nu_5+d}\right)
=5^{\nu_5+2d}=5^\lambda,
\]

(16.84) 还给出完全标量化的必要条件

\[
\boxed{
5^\lambda
\mid
N\!\left(
c_u\mathcal G_5
-\varepsilon c_+\omega\mathcal B_5
\right).
}
\tag{16.85}
\]

利用 (16.79)–(16.80) 展开 norm，可写成

\[
\boxed{
5^\lambda
\mid
\frac{
c_u^2k_h+c_+^2\omega^2Y
-2c_uc_+\omega r_+
}{3^\delta}.
}
\tag{16.86}
\]

分子确实被 `3^delta` 整除，这是 (16.80) 的 norm/composition 直接
保证的整数性。

(16.84) 是当前 reflection high-2 cone 的核心统一式：其中已经没有
`X`、没有固定 `eta` 的分类，也没有未分配的 Gaussian prime powers；
只剩范数由 (16.79) 固定的 \(\mathcal B_5,\mathcal G_5\) 与 source
Hensel 商 `omega`。要闭环，需证明这个 Gaussian 线性式不可能达到
不对称深度 \((d,\nu_5+d)\)，或从达到该深度推出保持 decimal plane 的
严格降高。

这个线性式不可能为零。否则

\[
\mathcal G_5
=\varepsilon\frac{c_+\omega}{c_u}\mathcal B_5
\]

是实数倍关系，从而
\(\mathcal G_5\overline{\mathcal B_5}\) 为实数；但 (16.80) 的虚部是
\(-R_1/3^\delta\)，而 `R_1>0`。矛盾。因此 (16.85) 实际给出真高度下界

\[
\boxed{
N\!\left(
c_u\mathcal G_5
-\varepsilon c_+\omega\mathcal B_5
\right)
\ge5^\lambda.
}
\tag{16.87}
\]

由三角不等式和 (16.79)，还可写成

\[
\boxed{
5^{\lambda/2}
\le
c_u\sqrt{\frac{k_h}{3^\delta}}
+c_+\omega\sqrt{\frac{Y}{3^\delta}}.
}
\tag{16.88}
\]

(16.88) 目前尚未与 endpoint 上界形成反向矛盾，但它把下一步需要的
Archimedean 估计对象固定为一个非零 Gaussian Hensel 线性式，而不是
原始参数全集。

### 16.14 `已严格完成`：quotient 同余提升为精确商，低 orientation 恰为 `d`

(16.84) 还可以提升为精确因式分解。记

\[
\mathfrak K_5:=\pi_\iota^d\bar\pi_\iota^{\nu_5+d},
\qquad
\mathcal M_5:=
c_u\mathcal G_5-\varepsilon c_+\omega\mathcal B_5,
\]

以及

\[
\mathcal S_5:=
c_-X\omega-5^dq\left(r_-+i\varepsilon R_3\right).
\tag{16.89}
\]

把 (16.78) 直接代入 (16.82)，不是只得到整除关系，而是得到

\[
\boxed{
\alpha_X^\sharp\mathcal M_5
=\mathfrak K_5\mathcal S_5.
}
\tag{16.90}
\]

因为

\[
N(\alpha_X^\sharp)=3^\delta X,
\qquad 5\nmid X,
\]

故 \(\alpha_X^\sharp\) 与 \(\mathfrak K_5\) 在
\(\mathbf Z[i]\) 中互素。Gaussian Euclid 引理于是给出同一个
\(\mathcal W_5\in\mathbf Z[i]\)，使

\[
\boxed{
\mathcal M_5=\mathfrak K_5\mathcal W_5,
\qquad
\mathcal S_5=\alpha_X^\sharp\mathcal W_5.
}
\tag{16.91}
\]

所以 (16.84) 不是一个带未知余项的松同余；其 quotient 就是把
\(\mathcal S_5\) 除以已经确定的共同 Gaussian divisor 后所得的精确商。
取范数并使用 (16.45)，可把这个商的范数完全展开为

\[
\boxed{
N(\mathcal W_5)
=\frac{
c_-^2X\omega^2
-2\,5^dc_-\omega q r_-
+5^\lambda q^2k_h
}{3^\delta}.
}
\tag{16.92}
\]

特别地，(16.85) 的精确版本是

\[
\boxed{N(\mathcal M_5)=5^\lambda N(\mathcal W_5).}
\tag{16.93}
\]

还可以确定模数较短一侧的赋值没有任何隐藏增深。由 (16.80)，

\[
\begin{aligned}
\mathcal M_5\overline{\mathcal B_5}
&=
\frac{
\omega a_2c_-5^d
-\varepsilon5^\lambda q r_+
-i c_uR_1
}{3^\delta}.
\end{aligned}
\tag{16.94}
\]

这里 \(a_2,c_-,\omega,q,r_+,c_u\) 都是 `5`-进单位，而
\(v_5(R_1)=d<\lambda\)。所以 (16.94) 的实部和虚部都**恰好**含
\(5^d\)，除以 \(5^d\) 后两坐标均为 `5`-进单位。
另一方面 \(N(\mathcal B_5)=Y/3^\delta\) 也是 `5`-进单位。若
\(\pi_\iota\mid\mathcal W_5\)，则由

\[
\frac{
\mathcal M_5\overline{\mathcal B_5}
}{5^d}
=
\bar\pi_\iota^{\nu_5}
\mathcal W_5\overline{\mathcal B_5}
\]

及 \(\nu_5>0\)，右边会同时含
\(\pi_\iota\bar\pi_\iota=5\)，迫使两个坐标都被 `5` 整除，矛盾。
故

\[
\boxed{
v_{\pi_\iota}(\mathcal W_5)=0,
\qquad
v_{\pi_\iota}(\mathcal M_5)=d.
}
\tag{16.95}
\]

也就是说，(16.84) 中较短的 Gaussian orientation **精确**停在
`d`；任何额外的 `5`-进增深只能继续发生在
\(\bar\pi_\iota\) 一侧。因而不能把 (16.85) 当作一个随后还可在两侧
重复收费的 balanced Hensel 条件。

最后，使用 \(\theta\) 得到的表面同伴也不是第二条独立同余。定义

\[
\mathcal M_\theta
:=c_-c_u\mathcal G_5-\varepsilon\theta\mathcal B_5.
\]

由 \(c_Q=c_-c_+\) 与
\(c_Q\omega-\theta=2^m5^\lambda c_u\)，精确有

\[
\boxed{
\mathcal M_\theta-c_-\mathcal M_5
=\varepsilon2^m5^\lambda c_u\mathcal B_5.
}
\tag{16.96}
\]

右边的有理 `5`-幂 \(5^\lambda\) 已经同时包含
\(\mathfrak K_5\) 的两个 orientation。因此

\[
\mathfrak K_5\mid\mathcal M_\theta
\quad\Longleftrightarrow\quad
\mathfrak K_5\mid\mathcal M_5.
\tag{16.97}
\]

所以 `omega/theta` 两种写法只给同一个 quotient kernel；后续若要
闭环，必须加入真正独立的 decimal-plane 输入，不能把 (16.96) 再算作
第二个 Hensel obstruction。

### 16.15 `已严格完成`：原拼接平面给出 `C` 的精确自然代表

本节把前面一直隐含在 \(\alpha_0\) 中的原拼接平面显式恢复出来。
在当前 reflection 中，原分母拼接为

\[
\beta
=2\cdot10^{M+m}+b_2 10^m+b_3.
\]

利用

\[
b_2=2^{M+m+1}c_ug,
\qquad
b_3=2^{M+m+1}5^dc_Qc_u,
\]

以及

\[
g\theta=5^{M+\lambda}+c_Qc_u,
\qquad
c_Q\omega-\theta=2^m5^\lambda c_u,
\]

逐项提取公共因子，得到

\[
\boxed{
\beta
=2^{M+m+1}5^dg c_Q\omega.
}
\tag{16.98}
\]

相应的 LCM 为

\[
q_{\rm lcm}=b_2c_Q5^d=b_3g,
\]

故原平面 \(q_{\rm lcm}\alpha=H_0\beta\) 化为

\[
\omega H_0=c_u\alpha.
\]

又由 source split，\(\gcd(q,c_u)=1\)、\(5\nmid c_u\)，而
\(g\omega=5^\lambda q+c_u\)，所以
\(\gcd(\omega,c_u)=1\)。因此

\[
\boxed{
\omega\mid\alpha,
\qquad
\alpha_0:=\frac\alpha\omega\in\mathbf Z,
\qquad
H_0=c_u\alpha_0.
}
\tag{16.99}
\]

这也补全了 §8 中 \(\alpha_0\) 的原始含义：它不是额外自由参数，而是
真实 numerator concatenation 除以 Hensel 商后的整数商。

在当前 `j=3` endpoint 中，§8 的第二个线性式成为

\[
H_0=\alpha_0c_u=gA_3-5^\lambda C,
\qquad
A_3=a_3+3\cdot10^m.
\tag{16.100}
\]

再与 high-2 equality

\[
H_0+\varepsilon a_2c_Q5^d=\frac{g^2k_h}{2}
\]

联立，得到顶部小余量的精确自然代表公式

\[
\boxed{
5^\lambda C
=gA_3+\varepsilon a_2c_Q5^d-\frac{g^2k_h}{2}.
}
\tag{16.101}
\]

它把此前分开的三项——原 decimal plane、finite-defect 小余量与
Gaussian high/low equality——放进同一个整数等式。特别地，模 `g`
先有

\[
5^\lambda C\equiv\varepsilon a_2c_Q5^d\pmod g.
\]

再利用 \(5^\lambda q\equiv-c_u\pmod g\)、
\(c_Qq\equiv5^M\pmod g\) 与 \(\gcd(q,g)=1\)，得到

\[
\boxed{
c_uC\equiv-\varepsilon a_2 5^{M+d}\pmod g.
}
\tag{16.102}
\]

它与 §8 的独立二进相位

\[
\boxed{C\theta\equiv5^Ma_3\pmod{2^m}}
\tag{16.103}
\]

共同固定 `C` 在 `g`-方向和 decimal `2^m`-方向的自然代表。

最后，§12 的尺度在 reflection 中可写成

\[
\mathfrak L_0=2c_u^2g^2,
\qquad 0<C<\frac{\mathfrak L_0}{1000}.
\]

由于 \(5\nmid c_ug\)，(16.101) 等价于

\[
\boxed{
C=\operatorname{res}_{(0,\mathfrak L_0)}
\left(
5^{-\lambda}
\left[gA_3+\varepsilon a_2c_Q5^d-\frac{g^2k_h}{2}\right]
\right)
<\frac{\mathfrak L_0}{1000},
}
\tag{16.104}
\]

其中 \(5^{-\lambda}\) 表示模 \(\mathfrak L_0\) 的逆元，
`res` 表示唯一的 `0` 到 \(\mathfrak L_0\) 之间代表。

(16.104) 正面解决了“应当控制哪个自然代表”的定义问题，但尚未证明
该代表落在区间外。下一步真正需要的是给 (16.102)–(16.104) 的代表
建立统一下界；仅仅再次指出模数大于 `C`，仍然只能给唯一性，不能给
空性。

### 16.16 `已严格完成`：精确 quotient 的象限锁

(16.81a) 与 (16.89) 直接给出

\[
\boxed{
5^{\nu_5+d}\operatorname{Re}(\mathcal S_5)
=c_ur_- -\varepsilon c_+\omega a_2.
}
\tag{16.105}
\]

若 \(\varepsilon=-1\)，右边两项均正，所以
\(\operatorname{Re}(\mathcal S_5)>0\)。若
\(\varepsilon=+1\)，则由 (16.38)

\[
r_-<\frac{k_hg}{2c_-5^d}.
\tag{16.106}
\]

另一方面 (9.4) 给出

\[
c_+\omega a_2
>\frac{20\cdot2^m5^\lambda c_u a_2}{c_-}.
\]

故要证明 \(c_+\omega a_2>c_ur_-\)，只需证明

\[
40\cdot2^m5^{\lambda+d}a_2>k_hg.
\]

这里 \(\lambda+d=m\)，而 (6.2+) 与 high equality 给出

\[
\frac{k_hg}{2\cdot10^m}<\frac{606}{125}<5.
\]

所以 \(k_hg<10\cdot10^m<40a_2\cdot10^m\)，所需严格不等式成立。
因此两个符号统一满足

\[
\boxed{-\varepsilon\operatorname{Re}(\mathcal S_5)>0.}
\tag{16.107}
\]

虚坐标由定义精确为

\[
\boxed{
\operatorname{Im}(\mathcal S_5)
=-\varepsilon5^dqR_3,
}
\tag{16.108}
\]

故还有

\[
\boxed{-\varepsilon\operatorname{Im}(\mathcal S_5)>0.}
\tag{16.109}
\]

综上，

\[
\boxed{-\varepsilon\mathcal S_5
\text{ 位于严格第一象限}.}
\tag{16.110}
\]

事实上象限还能统一收窄成一个固定角楔。由 (16.106)、两个 slot 的
共同上界以及 (9.3)–(9.4)，有

\[
\frac{2^m5^\lambda c_u}{c_-}(20a_2-5)
<
\left|c_ur_- -\varepsilon c_+\omega a_2\right|
<
\frac{2^m5^\lambda c_u}{c_-}(21a_2+5).
\tag{16.111}
\]

另一方面

\[
5^{\nu_5+d}\left|\operatorname{Im}(\mathcal S_5)\right|
=5^\lambda qR_3,
\qquad
R_3=9\cdot2^{M+m}c_+c_u.
\]

故令

\[
\phi_S:=\arg(-\varepsilon\mathcal S_5)\in(0,\pi/2),
\]

则

\[
\frac{9\cdot2^Mc_Qq}{21a_2+5}
<\tan\phi_S<
\frac{9\cdot2^Mc_Qq}{20a_2-5}.
\tag{16.112}
\]

由

\[
c_Qq=5^M+2^mgc_u=5^M\left(1+\frac x2\right),
\qquad
x<\frac2{19},
\qquad
a_2>\frac{249}{250}10^{M-1},
\]

以及 \(a_2<10^{M-1}\)、\(M\ge11\)，两端可统一化为

\[
\boxed{4<\tan\phi_S<5.}
\tag{16.113}
\]

这个角楔相对于原 prefix Gaussian 向量的侧别也被精确固定。令

\[
\phi_a:=\arg(Z_a),
\qquad
Z_a=a_2+iC_0,
\qquad
\tan\phi_a=\frac{C_0}{a_2}.
\]

把 (16.105) 与
\(g\omega=5^\lambda q+c_u\)、
\(R_3=C_0c_+/g\) 联立，直接得到

\[
\begin{aligned}
&5^\lambda qR_3a_2
-C_0\left(c_+\omega a_2-\varepsilon c_ur_-\right)\\
&\qquad
=\varepsilon\frac{C_0c_u}{g}
\left(gr_--\varepsilon a_2c_+\right)\\
&\qquad
=\varepsilon\frac{C_0c_u}{g}
5^{\nu_5+d}c_-X.
\end{aligned}
\tag{16.114}
\]

左边正是比较 \(\tan\phi_S\) 与 \(C_0/a_2\) 的交叉乘积。因此

\[
\boxed{
\operatorname{sgn}(\phi_S-\phi_a)=\varepsilon.
}
\tag{16.115}
\]

等价地，原向量层面的有向面积为

\[
\boxed{
\operatorname{Im}
\left(
(-\varepsilon\mathcal S_5)\overline{Z_a}
\right)
=\varepsilon\frac{C_0c_uc_-X}{g}.
}
\tag{16.116}
\]

最后使用

\[
\mathcal S_5=\alpha_X^\sharp\mathcal W_5,
\qquad
Z_a=\pi_\iota^{\nu_5}\alpha_X^\sharp\mathcal B_5,
\qquad
N(\alpha_X^\sharp)=3^\delta X,
\]

可把 (16.116) 中的无界共同因子 `X` 完全约掉：

\[
\boxed{
\operatorname{Im}
\left(
\mathcal W_5
\bar\pi_\iota^{\nu_5}
\overline{\mathcal B_5}
\right)
=-\frac{C_0c_uc_-}{3^\delta g}
=-\frac{c_uR_1}{3^\delta5^d}.
}
\tag{16.117}
\]

(16.117) 也可由 (16.94) 除去精确的 \(5^d\) 直接恢复，因此这里不把
它误计为第二条独立 Hensel 条件。它的新用途是给同一个 quotient
kernel 一个清楚的 Archimedean 解释：约分后的
\(\mathcal W_5\) 与 \(\pi_\iota^{\nu_5}\mathcal B_5\) 不仅近共线，
其有向面积和位于 prefix angle 的哪一侧都已精确固定。

由于 \(\mathcal S_5=\alpha_X^\sharp\mathcal W_5\)，(16.110) 是共同
Gaussian divisor 与精确 Hensel quotient 之间的真正 Archimedean
orientation 条件，而 (16.113) 把它进一步压入
\((\arctan4,\arctan5)\) 的固定窄楔。它比 (16.92) 的无方向范数更强，
但尚未单独限制
\(\alpha_X^\sharp\) 的 canonical argument 到足以排除所有 split-prime
allocation；因此此处仍不把象限锁提升为下降或空性。

### 16.17 `已严格完成`：quotient kernel 的唯一中心 Gaussian 代表

精确商 (16.91) 还可以改写成一个真正的最小余数问题。令

\[
\mathcal V_5:=\pi_\iota^{\nu_5}\mathcal B_5.
\tag{16.118}
\]

因为

\[
\mathfrak K_5
=\pi_\iota^d\bar\pi_\iota^{\nu_5+d}
=5^d\bar\pi_\iota^{\nu_5},
\qquad
\nu_5+d=\lambda-d,
\]

把

\[
c_u\mathcal G_5-\varepsilon c_+\omega\mathcal B_5
=\mathfrak K_5\mathcal W_5
\]

乘以 \(\pi_\iota^{\nu_5}\)，得到

\[
\boxed{
5^{\lambda-d}\mathcal W_5
+\varepsilon c_+\omega\mathcal V_5
=c_u\pi_\iota^{\nu_5}\mathcal G_5.
}
\tag{16.119}
\]

右边的 Gaussian norm 为

\[
N\!\left(c_u\pi_\iota^{\nu_5}\mathcal G_5\right)
=\frac{c_u^2 5^{\nu_5}k_h}{3^\delta}.
\tag{16.120}
\]

这个余数相对于有理模数 \(5^{\lambda-d}\) 其实统一很小。先由
high slot 的共同上界

\[
\frac{k_hg}{2\cdot10^m}<5
\]

及

\[
x=\frac{2^{m+1}c_ug}{5^M},
\qquad
c_u=\frac{w5^\lambda}{2^{M+1}c_Q},
\qquad
x>\frac1{10},\quad w<1,\quad c_Q\ge3,
\]

得到

\[
\frac{c_u^2k_h}{5^\lambda}
<
\frac{25}{c_Q^3}
2^{2m-3M}5^{m-M+2\lambda}.
\tag{16.121}
\]

在 low-`m` cone 中 \(\lambda\le m\le6M/11\)，故

\[
2m-3M\le-\frac{21M}{11},
\qquad
m-M+2\lambda\le\frac{7M}{11}.
\]

再用 \(M\ge11\)，有

\[
\boxed{
\frac{c_u^2k_h}{5^\lambda}
<
\frac{25}{27}
\left(\frac{5^7}{2^{21}}\right)^{M/11}
\le
\frac{25}{27}\frac{5^7}{2^{21}}
<\frac1{25}.
}
\tag{16.122}
\]

而

\[
2(\lambda-d)=\lambda+\nu_5.
\]

把 (16.122) 代入 (16.120)，最终得到

\[
\boxed{
\left|
c_u\pi_\iota^{\nu_5}\mathcal G_5
\right|
<\frac{5^{\lambda-d}}5.
}
\tag{16.123}
\]

因此 (16.119) 说明

\[
\boxed{
c_u\pi_\iota^{\nu_5}\mathcal G_5
\equiv
\varepsilon c_+\omega\mathcal V_5
\pmod{5^{\lambda-d}\mathbf Z[i]}
}
\tag{16.124}
\]

右边的同余类在开圆盘

\[
|z|<\frac12 5^{\lambda-d}
\]

内只有这一个代表：若有两个，二者之差是非零
\(5^{\lambda-d}\mathbf Z[i]\) 向量，长度至少
\(5^{\lambda-d}\)，而两代表的距离严格小于该值。

所以当前 quotient-Hensel 核已经从“一个大模数整除”提升为：

\[
\boxed{
\text{范数由 }k_h/3^\delta\text{ 固定、方向含 }
\pi_\iota^{\nu_5}\text{ 的唯一中心 Gaussian 代表}.}
\tag{16.125}
\]

这仍不自动给出零代表；事实上右边非零，因为 \(k_h>0\)。要完成排除，
现在只需证明由 decimal plane / `C` 自然代表确定的同余类，其中心代表
不可能具有 (16.120) 的 norm 和 (16.117) 的有向面积。与固定 `eta`
枚举相比，这已经是覆盖整个 reflection high-2 cone 的统一二维格点目标。

### 16.18 `已严格完成`：中心代表给出唯一最近商与指数级方向锁

(16.119) 中的中心代表相对于主向量其实远小于 `1/5`。记

\[
n_5:=5^{\lambda-d},\qquad
s_5:=c_+\omega,\qquad
\mathcal E_5:=c_u\pi_\iota^{\nu_5}\mathcal G_5.
\tag{16.126}
\]

则 (16.119) 是

\[
\mathcal E_5=n_5\mathcal W_5+\varepsilon s_5\mathcal V_5.
\tag{16.127}
\]

先比较误差与主项。由 (16.30)、(6.2±)，

\[
\frac{k_hg}{2T}<5,
\qquad T=10^m.
\]

另一方面

\[
c_+^2Y=H_0+Y_3,
\qquad
\frac{H_0+Y_3}{gT}=J_{\rm def}+2\zeta>4,
\]

所以

\[
k_h<\frac{10T}{g},
\qquad
Y>\frac{4gT}{c_+^2},
\qquad
\sqrt{\frac{k_h}{Y}}
<\sqrt{\frac52}\frac{c_+}{g}.
\tag{16.128}
\]

因此

\[
\begin{aligned}
\eta_5
&:=\frac{|\mathcal E_5|}{s_5|\mathcal V_5|}
=\frac{c_u}{c_+\omega}\sqrt{\frac{k_h}{Y}}\\
&<\sqrt{\frac52}\frac{c_u}{g\omega}
<\sqrt{\frac52}\frac{c_u}{5^\lambda}\\
&=\sqrt{\frac52}\frac{w}{2^{M+1}c_Q}
<\frac1{7680}.
\end{aligned}
\tag{16.129}
\]

最后一步只用了

\[
g\omega=5^\lambda q+c_u,
\qquad q\ge1,\qquad
c_u=\frac{w5^\lambda}{2^{M+1}c_Q},
\]

以及 \(w<1\)、\(c_Q\ge3\)、\(M\ge11\) 和
\(\sqrt{5/2}<8/5\)。这比 (16.123) 的统一 `1/5` 半径强三个数量级，
而且随 `M` 指数下降。

特别地，若把 Gaussian 整数的实、虚坐标分别记为下标 `1,2`，则
(16.127) 与 \(|(\mathcal E_5)_j|<n_5/2\) 给出逐坐标的唯一最近整数公式

\[
\boxed{
(\mathcal W_5)_j
=-\operatorname{nint}
\left(\frac{\varepsilon s_5(\mathcal V_5)_j}{n_5}\right),
\qquad j=1,2,
}
\tag{16.130}
\]

其中 `nint` 是唯一最近整数；不会出现半整数 tie，因为实际余数严格小于
\(n_5/5\)。所以 \(\mathcal W_5\) 已不再是 quotient kernel 中可自由选择
的 Gaussian 参数，而是由 \(\mathcal V_5\) 逐坐标唯一确定。

方向也随之大幅收紧。由 (16.127)，

\[
-\varepsilon n_5\mathcal W_5
=s_5\mathcal V_5-\varepsilon\mathcal E_5.
\tag{16.131}
\]

令

\[
\phi_a=\arg Z_a,
\qquad
\phi_S=\arg(-\varepsilon\mathcal S_5).
\]

因为 \(Z_a=\alpha_X^\sharp\mathcal V_5\)、
\(\mathcal S_5=\alpha_X^\sharp\mathcal W_5\)，乘以共同非零 Gaussian
因子不改变两向量夹角。由 (16.129)、(16.131)，

\[
|\sin(\phi_S-\phi_a)|
\le\frac{\eta_5}{1-\eta_5}
<\frac1{7679}.
\tag{16.132}
\]

(16.113) 给出 \(0<\tan\phi_S<5\)，而 endpoint window 也给出

\[
\frac92\frac{b_2}{a_2}
=45\frac{x}{y}<5.
\]

故

\[
|\tan\phi_S-\tan\phi_a|
=\frac{|\sin(\phi_S-\phi_a)|}{\cos\phi_S\cos\phi_a}
<\frac{26}{7679}<\frac7{2000}.
\]

再与精确侧别 (16.115) 合并，得到

\[
\boxed{
0<\varepsilon
\left(
\tan\phi_S-\frac{C_0}{a_2}
\right)
<\frac7{2000}.
}
\tag{16.133}
\]

因此原先宽度为 `1` 的角楔已经压成贴着真实 decimal prefix slope、
宽度小于 `7/2000` 的单侧条带；同时 Gaussian quotient 本身由最近整数
公式 (16.130) 唯一恢复。这个结果仍不等于空性：一个唯一的最近商仍
可能存在。剩余闭环必须证明该确定商与 (16.101) 的 `C` 自然代表或
(16.117) 的精确非零面积不相容，而不能把“唯一”误写成“不存在”。

### 16.19 `已严格完成`：提升后 quotient angle 精确解码原 prefix 系数

上一节的 `7/2000` 只用了范数比较；利用 decimal concatenation，
角差还能精确化到随 \(a_2\) 消失的宽度。记

\[
\mathcal U:=\frac{Y_2}{gT},
\qquad
\mathcal K:=\frac{c_Q\omega}{2^m5^\lambda c_u}.
\tag{16.134}
\]

由

\[
X_h-a_3=c_-5^dr_-,
\qquad
\frac{X_h}{T}
=\frac{H_0+\varepsilon Y_2}{gT}
=J_{\rm def}+\zeta+\varepsilon\mathcal U,
\]

有

\[
r_-=\frac{T(J_{\rm def}+\varepsilon\mathcal U)}{c_-5^d}.
\]

将它代入 (16.105)，并使用 \(\lambda=\nu_5+2d\)，可把
\(-\varepsilon\mathcal S_5\) 的斜率写成

\[
\boxed{
\tan\phi_S
=
\frac{9\cdot2^Mc_Qq}
{\mathcal K a_2-\mathcal U-\varepsilon J_{\rm def}}.
}
\tag{16.135}
\]

现在发生两个精确的 decimal cancellation。由
\(b_2c_Q5^d=b_3g\)，

\[
C_0\mathcal U
=\frac{9b_2}{2}\frac{a_2c_Q5^d}{gT}
=\frac92wa_2.
\tag{16.136}
\]

另一方面，由 \(C_0/g=9\cdot2^{M+m}c_u\) 与
\(g\omega=5^\lambda q+c_u\)，

\[
\mathcal K C_0
=9\cdot2^Mc_Qq+\frac92w.
\tag{16.137}
\]

用 (16.136)–(16.137) 从 (16.135) 减去
\(\tan\phi_a=C_0/a_2\)，前两项完全抵消，留下

\[
\boxed{
\tan\phi_S-\frac{C_0}{a_2}
=
\frac{
\varepsilon C_0J_{\rm def}
}{
a_2(\mathcal K a_2-\mathcal U-\varepsilon J_{\rm def})
}.
}
\tag{16.138}
\]

这既重新推出 (16.115) 的侧别，也把 defect
\(J_{\rm def}=3-C/D\) 直接放入 quotient angle，而不经过任何
Gaussian prime 枚举。

由 Hensel slot 有 \(\mathcal K>20\)；同时
\(\mathcal U<843/1000\)、\(J_{\rm def}<3\) 且
\(C_0/a_2<5\)。所以 (16.138) 给出

\[
0<
\varepsilon
\left(
\tan\phi_S-\frac{C_0}{a_2}
\right)
<
\frac{15}{20a_2-4}
<
\frac1{a_2}.
\tag{16.139}
\]

最后一个严格不等式只用 \(a_2\ge1\)。于是提升后的 quotient
\(\mathcal S_5=\alpha_X^\sharp\mathcal W_5\) 的方向逐位恢复原 prefix
coefficient：

\[
\boxed{
\begin{array}{ll}
\varepsilon=+1:
&
C_0=\left\lfloor a_2\tan\phi_S\right\rfloor,
\\[1mm]
\varepsilon=-1:
&
C_0=\left\lceil a_2\tan\phi_S\right\rceil.
\end{array}
}
\tag{16.140}
\]

更离散地，若

\[
X_S:=\operatorname{Re}(-\varepsilon\mathcal S_5)>0,
\qquad
Y_S:=\operatorname{Im}(-\varepsilon\mathcal S_5)>0,
\]

则 (16.140) 等价于

\[
\boxed{
\begin{array}{ll}
\varepsilon=+1:
&
C_0X_S<a_2Y_S<(C_0+1)X_S,
\\[1mm]
\varepsilon=-1:
&
(C_0-1)X_S<a_2Y_S<C_0X_S.
\end{array}
}
\tag{16.141}
\]

因此原向量层面的 \(\mathcal S_5\) 方向由一个宽度恰为 \(1/a_2\)
的单侧 Farey strip 唯一解码出 \(C_0\)。但这里必须保留一个关键边界：
\(\mathcal S_5=\alpha_X^\sharp\mathcal W_5\) 仍含被约去的共同 Gaussian
因子；(16.140) 尚未证明裸 quotient \(\mathcal W_5\) 的绝对方向本身
恢复 \(C_0\)。所以它严格加强了原平面与 quotient lift 的兼容性，却
还没有建立 plane covariance、合法 A2 下降或空性。

### 16.20 `已严格完成`：角条带产生商恰为 `1` 的正 Euclidean split

(16.141) 中的两个正缺口还具有统一的相对大小。定义有向面积

\[
\Delta_S
:=
\varepsilon(a_2Y_S-C_0X_S)>0.
\tag{16.142}
\]

由 (16.138) 及 \(X_S>0\)，精确有

\[
\frac{\Delta_S}{X_S}
=
\frac{C_0J_{\rm def}}
{\mathcal K a_2-\mathcal U-\varepsilon J_{\rm def}}.
\tag{16.143}
\]

endpoint window 给出

\[
\frac{C_0}{a_2}=45\frac{x}{y}>\frac92,
\qquad
J_{\rm def}>\frac{747}{250},
\]

而 \(\mathcal K<21\)、\(J_{\rm def}<3\)。因为 \(a_2\ge4\)，

\[
\frac{\Delta_S}{X_S}
>
\frac{(9/2)(747/250)a_2}{21a_2+3}
>
\frac35.
\tag{16.144}
\]

反向使用 \(C_0/a_2<5\)、\(\mathcal K>20\)、
\(\mathcal U+J_{\rm def}<4\)，得到

\[
\frac{\Delta_S}{X_S}
<
\frac{15a_2}{20a_2-4}
<
\frac45.
\tag{16.145}
\]

所以

\[
\boxed{
\frac35
<
\frac{\Delta_S}{X_S}
<
\frac45.
}
\tag{16.146}
\]

令

\[
E_S:=X_S-\Delta_S.
\tag{16.147}
\]

则 Euclidean division 的商被完全固定为 `1`，并有

\[
\boxed{
X_S=\Delta_S+E_S,
\qquad
\frac14\Delta_S<E_S<\frac23\Delta_S.
}
\tag{16.148}
\]

两个符号下，\(E_S\) 都有直接的相邻整数解释：

\[
\boxed{
\begin{array}{ll}
\varepsilon=+1:
&
\Delta_S=a_2Y_S-C_0X_S,\quad
E_S=(C_0+1)X_S-a_2Y_S,
\\[1mm]
\varepsilon=-1:
&
\Delta_S=C_0X_S-a_2Y_S,\quad
E_S=a_2Y_S-(C_0-1)X_S.
\end{array}
}
\tag{16.149}
\]

因此 `1/a_2` Farey strip 不是只有“唯一 floor/ceiling”的定性信息；
它产生了一次统一、严格降小的正整数 Euclidean step。当前尚未证明
\(E_S\) 与 \(\Delta_S\) 重新组成满足 (16.59) 的 Gaussian norm，
也未证明它们落回原 decimal coefficient plane，所以这里仍不能把
(16.148) 宣称为 A2 无限下降。下一步的明确目标是验证或否定这两个
协变性；若成立，(16.148) 已提供严格下降量。

这里可以立即完成第一项审计。两个符号对应的整数线性变换分别为

\[
\binom{\Delta_S}{E_S}
=
\begin{cases}
\begin{pmatrix}
-C_0&a_2\\ C_0+1&-a_2
\end{pmatrix}
\binom{X_S}{Y_S},&\varepsilon=+1,\\[4mm]
\begin{pmatrix}
C_0&-a_2\\ 1-C_0&a_2
\end{pmatrix}
\binom{X_S}{Y_S},&\varepsilon=-1.
\end{cases}
\tag{16.150}
\]

两矩阵的 determinant 统一为

\[
\boxed{\det=-\varepsilon a_2.}
\tag{16.151}
\]

由于 \(a_2>1\)，它不是 \(\mathrm{GL}_2(\mathbf Z)\) 变换，更不是
Gaussian unit multiplication。因此 (16.148) 的正整数降小本身不保持
二平方 norm；把它直接称为 Gaussian descent 会是错误的。真正的
Gaussian Euclidean step 必须直接作用在
\((\mathcal W_5,\mathcal V_5)\) 上。

### 16.21 `已严格完成`：quotient pair 的首个 Gaussian Euclidean 商为纯实数

现在回到中心余数式 (16.127)。先证明 \(\mathcal V_5\) 相对于模数
\(n_5\) 足够大。由

\[
c_+^2Y=H_0+Y_3>4gT,
\qquad
c_+\le c_Q<
\frac{5^\lambda}{2^{M+1}c_u},
\]

以及

\[
g=\frac{x5^M}{2^{m+1}c_u},
\qquad T=2^m5^m,
\]

得到

\[
Y>
x\,2^{2M+3}c_u5^{M-\lambda+d}.
\tag{16.152}
\]

于是

\[
\frac{Y}{5^\lambda}
>
\frac{2^{2M+3}}{10}5^{M-2\lambda+d}
\ge
\frac{2^{2M+3}}{10}5^{1-M/11}
>1.
\tag{16.153}
\]

最后一个量在 \(M=11\) 时已大于 `1`，之后每增加一个 \(M\) 至少乘
\(4/5^{1/11}>1\)。因此

\[
N(\mathcal V_5)
=\frac{5^{\nu_5}Y}{3^\delta}
>
\frac{5^{\nu_5+\lambda}}3
=\frac{n_5^2}{3},
\]

即

\[
\boxed{
|\mathcal V_5|>\frac{n_5}{\sqrt3}>\frac{2n_5}{5}.
}
\tag{16.154}
\]

定义唯一最近整数

\[
\boxed{
Q_E:=
\operatorname{nint}\left(\frac{s_5}{n_5}\right)
\in\mathbf Z.
}
\tag{16.155}
\]

由于 \(n_5\) 为奇数，\(s_5/n_5\) 不可能是半整数，故最近整数唯一。
再令中心的有理余数

\[
r_E:=s_5-Q_En_5,
\qquad
|r_E|\le\frac{n_5-1}{2},
\tag{16.156}
\]

以及 Gaussian 余数

\[
\boxed{
\mathcal R_E:=
-\varepsilon\mathcal W_5-Q_E\mathcal V_5.
}
\tag{16.157}
\]

由 (16.127) 精确有

\[
n_5\mathcal R_E
=r_E\mathcal V_5-\varepsilon\mathcal E_5.
\tag{16.158}
\]

结合 (16.123)、(16.154)：

\[
\begin{aligned}
\frac{|\mathcal R_E|}{|\mathcal V_5|}
&\le
\frac{|r_E|}{n_5}
+
\frac{|\mathcal E_5|}{n_5|\mathcal V_5|}\\
&<
\frac{n_5-1}{2n_5}
+
\frac1{5|\mathcal V_5|}
<
\frac12.
\end{aligned}
\]

所以

\[
\boxed{
0<N(\mathcal R_E)<\frac14N(\mathcal V_5).
}
\tag{16.159}
\]

等价地，

\[
\left|
\frac{-\varepsilon\mathcal W_5}{\mathcal V_5}-Q_E
\right|<\frac12.
\]

任意另一个 Gaussian 整数与 \(Q_E\) 的距离至少为 `1`，故 \(Q_E\)
也是 \(-\varepsilon\mathcal W_5/\mathcal V_5\) 的唯一最近 Gaussian
整数；特别地，首个 Gaussian Euclidean 商没有虚部。

这里余数确实非零。由 (16.117)，

\[
\boxed{
\operatorname{Im}
\left(
\mathcal R_E\overline{\mathcal V_5}
\right)
=
\varepsilon\frac{c_uR_1}{3^\delta5^d}
\ne0,
}
\tag{16.160}
\]

因为减去实整数倍 \(Q_E\mathcal V_5\) 不改变 determinant。并且
\(\pi_\iota\mid\mathcal V_5\)、\(v_{\pi_\iota}(\mathcal W_5)=0\)，
故

\[
\boxed{v_{\pi_\iota}(\mathcal R_E)=0.}
\tag{16.161}
\]

因此 \(\mathcal R_E\) 是 canonical、非零、短 orientation 本原的
Gaussian Euclidean 余数，且 norm 至少下降四倍。这是真正作用在裸
quotient pair 上的严格下降，不再含 \(\alpha_X^\sharp\) 的绝对 argument。

它仍未单独关闭 reflection high-2：要形成 A2 无限下降，还必须证明
\((\mathcal R_E,\mathcal V_5)\) 或下一对 Euclidean pair 继续满足由
decimal concatenation 强制的 coefficient plane / Hensel 形状。
当前严格进展是已把“寻找某个 Gaussian 降高”缩成唯一的首商
\(Q_E\) 与余数 (16.157)，后续不再有 quotient-choice 自由度。

### 16.22 `已严格完成`：Gaussian 余数保持同一 Hensel 模数并降成唯一标量核

余数 (16.157) 不只具有较小 norm；把它乘回原不对称模数，可得到
完全同型的精确 Hensel 等式。由

\[
\mathfrak K_5\mathcal W_5
=c_u\mathcal G_5-\varepsilon s_5\mathcal B_5,
\qquad
\mathfrak K_5\mathcal V_5=n_5\mathcal B_5,
\]

以及 \(r_E=s_5-Q_En_5\)，直接算得

\[
\boxed{
\mathfrak K_5\mathcal R_E
=
r_E\mathcal B_5-\varepsilon c_u\mathcal G_5.
}
\tag{16.162}
\]

因此 Euclidean step 没有改变
\(\mathcal B_5,\mathcal G_5,\mathfrak K_5\)，只是把原大系数
\(s_5=c_+\omega\) 换成唯一中心整数 \(r_E\)。

这个中心整数必为 `5`-进单位。若 \(5\mid r_E\)，则 (16.162) 右边
第一项被 \(\pi_\iota\) 整除，而
\(5\nmid N(\mathcal G_5)=k_h/3^\delta\) 说明第二项不被
\(\pi_\iota\) 整除；这与左边含
\(\pi_\iota^d\)、\(d\ge1\) 矛盾。因此

\[
\boxed{5\nmid r_E.}
\tag{16.163}
\]

它还是中心区间内唯一满足 (16.162) 的整数。若另有
\(|r_E'|\le(n_5-1)/2\) 也满足同一整除式，则

\[
\mathfrak K_5\mid(r_E-r_E')\mathcal B_5.
\]

因 \(5\nmid N(\mathcal B_5)\)，可消去 \(\mathcal B_5\)。一个有理整数
被

\[
\mathfrak K_5
=\pi_\iota^d\bar\pi_\iota^{\nu_5+d}
\]

整除时，其两个 Gaussian orientation 赋值相等，故必须被
\(5^{\nu_5+d}=n_5\) 整除。但
\(|r_E-r_E'|<n_5\)，所以 \(r_E=r_E'\)。即

\[
\boxed{
r_E\text{ 是 }[-(n_5-1)/2,(n_5-1)/2]
\text{ 中唯一的 scalar Hensel representative}.
}
\tag{16.164}
\]

原 source Hensel 还给出它的两个等价自然余类：

\[
\boxed{
r_E\equiv c_+c_ug^{-1}\pmod{n_5},
\qquad
c_-r_E\equiv\theta\pmod{n_5}.
}
\tag{16.165}
\]

第一式来自 \(g\omega\equiv c_u\pmod{n_5}\)，第二式来自
\(c_Q\omega\equiv\theta\pmod{n_5}\)。

最后对 (16.162) 取 norm，并使用 (16.79)–(16.80)，得到纯一维二次核

\[
\boxed{
5^\lambda N(\mathcal R_E)
=
\frac{
Yr_E^2-2c_ur_+r_E+c_u^2k_h
}{3^\delta}.
}
\tag{16.166}
\]

左边二次式关于 \(r_E\) 的 discriminant 为

\[
\boxed{
-4c_u^2R_1^2,
}
\tag{16.167}
\]

因为 \(r_+^2+R_1^2=k_hY\)。所以 reflection high-2 的 Gaussian
quotient-choice 已严格降为：由 (16.165) 唯一固定的 `5`-进单位
\(r_E\)，必须使正定二次式 (16.166) 达到完整 \(5^\lambda\) 深度，
同时其 Gaussian 余数满足四倍 norm 下降 (16.159)。

这仍不是最终矛盾；但下一步已变成一个明确的一维任务：把
\(r_E\equiv c_-^{-1}\theta\pmod{n_5}\) 的唯一中心代表代入
(16.166)，证明所得正定值不可能具有要求的剩余 \(5^d\) 长
orientation，或证明它产生可迭代的 decimal-plane child。

### 16.23 `已严格完成`：十进制缺口进入第二层唯一中心奇代表

Hensel slot 的补余量 \(\varrho\) 可以完全用真实 denominator 缺口
\(H\) 表示。由

\[
2^{m+2}c_ug=5^{M-1}+H
\]

与

\[
\theta=\frac{5^{M+\lambda}+c_Qc_u}{g},
\qquad
\varrho=20L_*-\theta,
\]

直接得到

\[
\boxed{
g\varrho=5^{\lambda+1}H-c_Qc_u.
}
\tag{16.168}
\]

特别地，\(\varrho>0\) 等价于
\(5^{\lambda+1}H>c_Qc_u\)。另一方面
\(L_*=2^m5^dc_un_5\)，所以

\[
\theta=20L_*-\varrho\equiv-\varrho\pmod{n_5}.
\]

这说明 (16.165) 的第一层中心代表满足

\[
gc_-r_E\equiv c_Qc_u\pmod{n_5};
\]

其中 \(5^{\lambda+1}H\) 已含完整 \(n_5=5^{\lambda-d}\)，故十进制
\(H\)-项在第一层模数中确实消失。它没有真正丢失，而是进入精确提升商。
定义

\[
\boxed{
z_E:=
\frac{gr_E-c_+c_u}{n_5}\in\mathbf Z.
}
\tag{16.169}
\]

整数性就是 (16.165) 第一式。再把
\(c_-r_E+\varrho=n_5h_E\) 与 (16.168) 联立，得到

\[
c_-z_E
=gh_E-5^{d+1}H,
\]

因而

\[
\boxed{
c_-z_E\equiv-5^{d+1}H\pmod g.
}
\tag{16.170}
\]

这个提升商本身也是中心代表。先注意

\[
\frac{c_+c_u}{n_5}
\le\frac{c_Qc_u}{n_5}
=\frac{w5^d}{2^{M+1}}
<1.
\tag{16.171}
\]

最后一个不等式由 \(d<9M/77\) 与 \(5^9<2^{21}\) 给出：

\[
5^d<2^{7d/3}<2^{3M/11}<2^{M+1}.
\]

结合 \(|r_E|\le(n_5-1)/2\)，(16.169) 先给出

\[
|z_E|<\frac g2+1.
\]

因为 \(z_E\) 为整数，所以至多有 \(|z_E|\le g/2\)。端点也不可能：
\(5^{M-1}+H\) 被 \(2^{m+t+1}\) 整除，故 \(H\) 为奇数；而
\(g=2^{t-1}\rho\)、\(t\ge3\) 说明 \(g/2\) 为偶数。若
\(z_E=\pm g/2\)，则奇数 \(c_-\) 使
\(c_-z_E\equiv g/2\pmod g\) 为偶数，但 (16.170) 右边为奇数，矛盾。
因此

\[
\boxed{
-\frac g2<z_E<\frac g2,
\qquad
z_E\equiv-5^{d+1}Hc_-^{-1}\pmod g,
\qquad
z_E\text{ 为奇数},
\qquad
\gcd(z_E,g)=1.
}
\tag{16.172}
\]

最后一个互素性来自
\(H\equiv-5^{M-1}\pmod g\)：因 \(5\nmid g\)，有
\(\gcd(H,g)=1\)，再由 (16.170) 及
\(\gcd(5c_-,g)=1\) 即得。

由于 (16.170) 的余类不是端点类 \(g/2\)，开区间
\((-g/2,g/2)\) 中恰有它的一个代表；故 \(z_E\) 是由真实十进制
缺口 \(H\) 唯一固定的第二层中心奇代表。
反过来

\[
\boxed{
r_E=\frac{c_+c_u+n_5z_E}{g}.
}
\tag{16.173}
\]

所以当前标量核具有严格的两级 mixed-radix 结构：

\[
H
\xrightarrow{\ \bmod g\ }
z_E
\xrightarrow{\ \text{exact lift}\ }
r_E
\xrightarrow{\ (16.166)\ }
5^\lambda N(\mathcal R_E).
\tag{16.174}
\]

这是真正新增的 decimal 接口：第一层 `5`-进余类本身不看见 \(H\)，
但它的唯一提升商由 \(H\bmod g\) 完全决定。下一步应把 (16.173)
直接代入 (16.166)，而不是再次把 \(r_E\) 当作自由中心余数。

### 16.24 `已严格完成`：第二层中心代表给出 prefix-discriminant norm

现在执行 (16.173) 的代入。为避免分母，先把 (16.166) 的分子记为

\[
\mathcal Q_E(r)
:=
Yr^2-2c_ur_+r+c_u^2k_h.
\]

由 \(gr_E=c_+c_u+n_5z_E\)，有

\[
\begin{aligned}
g^2\mathcal Q_E(r_E)
={}&
Y(c_+c_u+n_5z_E)^2\\
&-2c_ur_+g(c_+c_u+n_5z_E)
+c_u^2k_hg^2.
\end{aligned}
\]

其中常数项利用

\[
gr_+-\varepsilon a_2c_-5^d=c_+Y,
\qquad
\frac{k_hg^2}{2}=H_0+\varepsilon Y_2,
\]

精确化为

\[
c_u^2
\left(
c_+^2Y-2c_+gr_++k_hg^2
\right)
=c_u^25^\lambda c_-^2X.
\]

线性项则化为

\[
2n_5c_u(c_+Y-gr_+)z_E
=-2\varepsilon n_5c_ua_2c_-5^dz_E.
\]

由于 \(n_5=5^{\lambda-d}\)、\(\nu_5=\lambda-2d\)，从两边消去
\(5^\lambda\)，得到

\[
\boxed{
3^\delta g^2N(\mathcal R_E)
=
5^{\nu_5}Yz_E^2
-2\varepsilon c_ua_2c_-z_E
+c_u^2c_-^2X.
}
\tag{16.175}
\]

这条二次式的 discriminant 为

\[
\begin{aligned}
\operatorname{disc}_{z_E}
&=
4c_u^2c_-^2
\left(a_2^2-5^{\nu_5}XY\right)\\
&=
\boxed{-4c_u^2c_-^2C_0^2},
\end{aligned}
\tag{16.176}
\]

因为 \(5^{\nu_5}XY=N_0=a_2^2+C_0^2\)。等价地，配方给出新的
Gaussian norm transfer：

\[
\boxed{
\left(
5^{\nu_5}Yz_E-\varepsilon c_ua_2c_-
\right)^2
+
\left(c_uc_-C_0\right)^2
=
3^\delta5^{\nu_5}g^2Y\,N(\mathcal R_E).
}
\tag{16.177}
\]

与 (16.166) 的 discriminant \(-4c_u^2R_1^2\) 相比，(16.177) 已把
第二坐标换成真实 prefix coefficient \(C_0\)，而 \(z_E\) 又由
\(H\bmod g\) 唯一确定；这是标量 Hensel 核与 decimal plane 的直接
二平方接口。

其完整二进公共层也可以严格约去。记

\[
U_E:=5^{\nu_5}Yz_E-\varepsilon c_ua_2c_-,
\qquad
V_E:=c_uc_-C_0.
\tag{16.178}
\]

由 \(C_0=9\cdot2^{M+m}c_ug\)，显然
\(2^{t-1}\mid V_E\)。右边 (16.177) 又被
\(g^2=2^{2t-2}\rho^2\) 整除。若
\(v_2(U_E)<t-1\)，则因 \(v_2(V_E)\ge t-1\)，二平方和左边的
二进赋值恰为 \(2v_2(U_E)<2t-2\)，矛盾。因此

\[
\boxed{2^{t-1}\mid U_E,\qquad 2^{t-1}\mid V_E.}
\tag{16.179}
\]

定义

\[
\widetilde U_E:=\frac{U_E}{2^{t-1}},
\qquad
\widetilde V_E:=\frac{V_E}{2^{t-1}},
\]

便得到去除完整 high-`2` common layer 的正规形

\[
\boxed{
\widetilde U_E^2+\widetilde V_E^2
=
3^\delta5^{\nu_5}\rho^2Y\,N(\mathcal R_E),
\qquad
\rho\mid\widetilde V_E.
}
\tag{16.180}
\]

其中第二个整除来自 \(g\mid C_0\)。事实上第一坐标也必含完整
\(\rho\)。模 \(\rho\) 使用

\[
H\equiv-5^{M-1},
\qquad
c_-z_E\equiv-5^{d+1}H\equiv5^{M+d},
\tag{16.181a}
\]

以及 (16.41+) 和 \(g\equiv0\pmod\rho\) 给出的

\[
c_+Y\equiv-\varepsilon a_2c_-5^d\pmod\rho.
\tag{16.181b}
\]

于是

\[
\begin{aligned}
c_Q U_E
&=5^{\nu_5}(c_+Y)(c_-z_E)
-\varepsilon c_ua_2c_-c_Q\\
&\equiv
-\varepsilon a_2c_-
\left(5^{M+\lambda}+c_Qc_u\right)
\equiv0\pmod\rho,
\end{aligned}
\tag{16.181}
\]

其中最后一步使用
\(5^{M+\lambda}+c_Qc_u=g\theta\)。由
\(\gcd(c_Q,\rho)=1\)，得到 \(\rho\mid U_E\)。结合 (16.179)：

\[
\boxed{g\mid U_E,\qquad g\mid V_E.}
\tag{16.182}
\]

令

\[
\widehat U_E:=\frac{U_E}{g},
\qquad
\widehat V_E:=\frac{V_E}{g},
\]

便可约去完整 \(g^2\)：

\[
\boxed{
\widehat U_E^2+\widehat V_E^2
=
3^\delta5^{\nu_5}Y\,N(\mathcal R_E).
}
\tag{16.183}
\]

这个约分还有精确 Gaussian 来源，因此不能被重复计算成新的独立
obstruction。将 (16.162) 乘以 \(\overline{\mathcal B_5}\)，使用
(16.80)，有

\[
3^\delta\mathfrak K_5
\mathcal R_E\overline{\mathcal B_5}
=
r_EY-c_ur_++i\varepsilon c_uR_1.
\]

另一方面由 (16.173)、(16.41+) 与
\(R_1=5^dC_0/g\)，

\[
g(r_EY-c_ur_+)=5^dU_E,
\qquad
gc_uR_1=5^dV_E.
\]

再用 \(\mathfrak K_5=5^d\bar\pi_\iota^{\nu_5}\)，得到

\[
\boxed{
\widehat U_E+i\varepsilon\widehat V_E
=
3^\delta
\bar\pi_\iota^{\nu_5}
\mathcal R_E\overline{\mathcal B_5}.
}
\tag{16.184}
\]

所以 §16.24 的严格结论是：第二层 decimal representative 强迫完整
\(g\)-common factor，且约分后恰为 canonical Euclidean remainder 与
\(\mathcal B_5\) 的 Gaussian composition。它解决了 \(\rho\) 的
split-prime allocation，但尚未把右边识别成新的合法 decimal blocks；
因此完整 \(g\)-约分是 plane-covariance 的必要进展，而不是已经闭环的
A2 descent。

### 16.25 `已严格完成`：第二层代表与顶部补余量进入同一整数核

第二层中心代表还可以与 §16.15 的顶部补余量 \(C\) 直接合并。由

\[
H\equiv-5^{M-1}\pmod g
\]

把 (16.170) 改写为

\[
c_-z_E\equiv5^{M+d}\pmod g.
\tag{16.185}
\]

另一方面 (16.102) 是

\[
c_uC\equiv-\varepsilon a_25^{M+d}\pmod g.
\]

消去同一个 \(5^{M+d}\)，得到新的 mixed decimal bridge

\[
\boxed{
c_uC+\varepsilon a_2c_-z_E\equiv0\pmod g.
}
\tag{16.186}
\]

定义其精确提升商

\[
\boxed{
\chi_E:=
\frac{c_uC+\varepsilon a_2c_-z_E}{g}
\in\mathbf Z.
}
\tag{16.187}
\]

现在回到第二层二次核 (16.175)。由

\[
\varepsilon a_2c_-z_E=g\chi_E-c_uC,
\qquad
c_-^2X=3D-C,
\]

可把其中两项合并成

\[
\boxed{
3^\delta g^2N(\mathcal R_E)
=
5^{\nu_5}Yz_E^2
-2c_ug\chi_E
+c_u^2(3D+C).
}
\tag{16.188}
\]

所以 reflection high-2 的剩余核现在由一个完全整数化的链控制：

\[
\boxed{
\begin{gathered}
z_E=\operatorname{cres}_g
\left(-5^{d+1}Hc_-^{-1}\right),
\qquad
\chi_E=\frac{c_uC+\varepsilon a_2c_-z_E}{g},\\
3^\delta g^2N(\mathcal R_E)
=5^{\nu_5}Yz_E^2-2c_ug\chi_E+c_u^2(3D+C).
\end{gathered}
}
\tag{16.189}
\]

这里 `cres` 表示已由 (16.172) 证明存在且唯一的中心代表。
(16.189) 首次把真实 denominator 缺口 \(H\)、顶部 defect \(C\)、
prefix norm factors 与 canonical Gaussian 余数放进同一个整数核。
但 (16.188) 仍由已有 exact-lift 等式推出，不能单独当作矛盾。
下一项真正独立的输入应是 §7 的 rational-root divisibility
\(C\mid F(3)\)；后续目标是用 (16.187) 消去 \(C\) 的模 \(g\)
自由度后，证明 \(F(3)/C\) 与 (16.188) 的正定高度不相容。

### 16.26 `已严格完成 / 降级`：canonical Gaussian child 不可能回到 A2 prefix window

完整 \(g\)-约分产生了严格更小的 Gaussian 向量，但它是否能作为同型
A2 child 必须由真实角度检验。先给 source ratio 一个统一上界：

\[
\begin{aligned}
\frac{c_uc_Q}{g}
&=
\frac wx\,c_u2^{m-M}5^{\lambda-M}\\
&<
\frac53\,2^{m-2M}5^{2\lambda-M}\\
&\le
\frac53\,2^{-16M/11}5^{M/11}
<\frac1{7000}.
\end{aligned}
\tag{16.190}
\]

第二步用了

\[
c_u=\frac{w5^\lambda}{2^{M+1}c_Q}
<\frac{5^\lambda}{3\cdot2^{M+1}},
\]

最后一步在 \(M=11\) 时化为
\(25/(3\cdot2^{16})<1/7000\)，之后按
\(5^{1/11}/2^{16/11}<1\) 递减。

由 (16.128) 及 \(c_+\le c_Q\)，

\[
c_u\sqrt{\frac{k_h}{Y}}
<
\sqrt{\frac52}\frac{c_uc_+}{g}
<
\frac1{4000}.
\tag{16.191}
\]

而 \(r_+^2+R_1^2=k_hY\)，故

\[
\boxed{
\frac{c_ur_+}{Y}<\frac1{4000},
\qquad
\frac{c_uR_1}{Y}<\frac1{4000}.
}
\tag{16.192}
\]

从 (16.184) 的实虚部也可直接写出

\[
\widehat U_E=\frac{r_EY-c_ur_+}{5^d},
\qquad
\widehat V_E=\frac{c_uR_1}{5^d}.
\tag{16.193}
\]

由 (16.163)，\(r_E\) 是非零整数，所以 \(|r_E|\ge1\)。结合
(16.192)：

\[
|r_EY-c_ur_+|
>
\frac{3999}{4000}Y.
\]

因此

\[
\boxed{
\left|
\frac{\widehat V_E}{\widehat U_E}
\right|
<\frac1{3999}.
}
\tag{16.194}
\]

另一方面任何合法 `(a,k)=(9,2)` A2 prefix 均满足

\[
\frac{C_0}{a_2}=45\frac xy>\frac92,
\qquad
\frac{C_0}{a_2}<5.
\]

乘以 Gaussian unit 只能交换两个坐标并改变符号，所以
(16.194) 对应的绝对斜率只能小于 \(1/3999\) 或大于 \(3999\)，绝不可能
落回 \((9/2,5)\)。于是

\[
\boxed{
\text{canonical child }
\widehat U_E+i\varepsilon\widehat V_E
\text{ 不可能是同型 A2 decimal prefix}.
}
\tag{16.195}
\]

这不是对原候选的矛盾，因为 exact lift 并未要求 Gaussian Euclidean
child 自动成为新十进制候选；它严格否定的是“用 (16.184) 直接迭代同型
下降”的路线。reflection high-2 的闭环因此必须使用 (16.189) 与
\(C\mid F(3)\) 的直接不相容，而不能再依赖 plane-preserving descent。

### 16.27 `已严格完成`：`C | F(3)` 的精确 `2/5` 正规化

§7 的整除条件还可以先剥去全部十进制素因子，而不作任何枚举。在
\(J=3\) 处，

\[
F(3)=
3b_2^2T(3T+2a_3)(10P-3)^2
-Q^2N_0(3T+a_3)^2.
\tag{16.196}
\]

先算精确二进赋值。由 deep-even 终端正规形，

\[
v_2(Q)=M+1,
\qquad
v_2(b_2)=M+m+t.
\]

又因 \(a_2,a_3\) 均为奇数，\(N_0=C_0^2+a_2^2\) 为奇数，
\(3T+a_3\) 为奇数，而

\[
v_2(3T+2a_3)=1,
\qquad
10P-3\equiv1\pmod2.
\]

因此 (16.196) 两项的二进赋值分别为

\[
2M+3m+2t+1
\quad\hbox{与}\quad
2M+2.
\]

前者严格更大，故不存在最低层抵消，并有

\[
\boxed{v_2(F(3))=2M+2.}
\tag{16.197}
\]

再算五进赋值。由 §16.7 的 source split，
\(b_2,Q,a_3\) 都是 \(5\)-进单位；同时
\(3T+2a_3\)、\(10P-3\)、\(3T+a_3\) 也都是 \(5\)-进单位。
reflection low-\(m\) 核中 §11 已给出

\[
v_5(N_0)=\nu_5=\lambda-2d,
\qquad
m=\lambda+d>\nu_5.
\]

所以 (16.196) 两项的五进赋值分别为 \(m\) 与 \(\nu_5\)，再次没有
最低层抵消：

\[
\boxed{v_5(F(3))=\nu_5.}
\tag{16.198}
\]

还需确定符号。对 \(0<J<10P\) 定义正函数

\[
\mathscr R(J):=
\frac{
b_2^2TJ(TJ+2a_3)(10P-J)^2
}{
Q^2N_0(TJ+a_3)^2
}.
\]

直接对数求导并约掉全部一次项，得到

\[
\boxed{
\frac{\mathscr R'(J)}{\mathscr R(J)}
=
\frac{2a_3^2}
{J(TJ+a_3)(TJ+2a_3)}
-\frac2{10P-J}.
}
\tag{16.199}
\]

在 \(J_{\rm def}\le J\le3\) 上，已有 \(a_3>T\)，故

\[
\frac{J(TJ+a_3)(TJ+2a_3)}{a_3^2}
<
3\cdot4\cdot5=60,
\]

而 \(10P-J>60\)。所以 \(\mathscr R'(J)>0\)。由
\(\mathscr R(J_{\rm def})=1\) 以及 \(J_{\rm def}<3\)，得到

\[
\boxed{F(3)>F(J_{\rm def})=0.}
\tag{16.200}
\]

最后，\(\gcd(C,D)=1\) 且 \(10\mid D\)，所以
\(\gcd(C,10)=1\)。结合 \(C\mid F(3)\)、(16.197)、(16.198) 与
(16.200)，可定义

\[
\boxed{
\Xi_C:=
\frac{F(3)}
{2^{2M+2}5^{\nu_5}C}
\in\mathbf Z_{>0},
\qquad
\gcd(\Xi_C,10)=1.
}
\tag{16.201}
\]

因此 rational-root 条件不再只是一个无符号整除式：剥去全部
\(2,5\)-primary content 与自然代表 \(C\) 后，剩下的是严格为正的
奇 \(5\)-进单位余因子。特别地，(16.198) 的五进深度与第二层
prefix norm 的精确深度 \(\nu_5\) 完全相同；任何进一步矛盾都必须
发生在 odd-prime support，而不能再向 \(2\) 或 \(5\) 重复收费。
下一步需把 \(\Xi_C\) 的奇素数支持与 (16.187)–(16.189) 的
\((z_E,\chi_E)\) 整数核联立。

### 16.28 `已严格完成`：奇余因子在整个 denominator 上只有一个平方类

(16.201) 的 \(\Xi_C\) 还能在模 \(D\) 下完全识别。令

\[
L:=2^m5^d,
\qquad D=gL.
\]

使用

\[
b_2=2^{M+m+1}c_ug,\qquad
Q=2^{M+1}c_Qq,\qquad
N_0=5^{\nu_5}XY,
\]

把 (16.196) 除以 \(2^{2M+2}5^{\nu_5}\)。由于
\(m-\nu_5=3d\)，得到

\[
\frac{F(3)}{2^{2M+2}5^{\nu_5}}
=
3c_u^2g^2L^3(3T+2a_3)(10P-3)^2
-c_Q^2q^2XY(3T+a_3)^2.
\tag{16.202}
\]

现在代入

\[
c_Q=c_-c_+,
\qquad
c_-^2X=3D-C.
\]

若记

\[
\mathscr A:=(3T+2a_3)(10P-3)^2,
\qquad
\mathscr B:=(3T+a_3)^2,
\]

则 (16.202) 与 \(F(3)/(2^{2M+2}5^{\nu_5})=C\Xi_C\)
精确化成

\[
\boxed{
C\!\left(\Xi_C-q^2c_+^2Y\mathscr B\right)
=
3D\!\left(
c_u^2gL^2\mathscr A-q^2c_+^2Y\mathscr B
\right).
}
\tag{16.203}
\]

因为 \(\gcd(C,D)=1\)，立刻有 denominator-wide residue

\[
\boxed{
\Xi_C
\equiv
q^2c_+^2Y(3T+a_3)^2
\pmod D.
}
\tag{16.204}
\]

特别地，\(Y,q,c_+,a_3\) 都是奇 \(5\)-进单位，且
\(T\equiv0\pmod{2^m5^d}\)，所以

\[
\boxed{
\Xi_C
\equiv
Y(qc_+a_3)^2
\pmod{2^m5^d}.
}
\tag{16.205}
\]

换言之，\(\Xi_C/Y\) 在 \(2^m\) 与 \(5^d\) 的单位群中都被强迫为
同一个显式平方类；尤其

\[
\Xi_C\equiv Y\pmod8.
\tag{16.206}
\]

模 \(g\) 的部分还可与 mixed bridge 对接。由 (16.41+) 与
(16.186)，

\[
c_+^2Y
\equiv-\varepsilon a_2c_Q5^d
\equiv c_uC
\pmod g.
\]

代回 (16.204)：

\[
\boxed{
\Xi_C
\equiv
c_uCq^2(3T+a_3)^2
\pmod g.
}
\tag{16.207}
\]

由于 \(C\) 在模 \(g\) 下可逆，(16.207) 等价于

\[
\boxed{
\Xi_CC^{-1}
\equiv
c_u\bigl(q(3T+a_3)\bigr)^2
\pmod g.
}
\tag{16.208}
\]

这已经把 §7 的独立 rational-root cofactor 接到了 source factor
\(c_u\)、prefix norm factor \(Y\) 和真实 denominator \(D\) 上。
但 (16.203) 也说明它仍是 exact root equation 的一次正规化；
仅凭“落在平方类”不能推出空性。新的闭环问题是：用
\(z_E,\chi_E\) 对 \(C\) 的中心代表限制，证明 (16.205) 与
(16.208) 所要求的两个平方类不能同时由同一个正整数 \(\Xi_C\)
实现。

### 16.29 `已严格完成`：相邻整数点同时产生两个互素的 `D`-尺度除数

只在 \(J=3\) 使用 rational-root theorem 会丢掉 denominator 一侧的
信息。令

\[
N:=3D-C=c_-^2X,
\qquad
s_j:=jD-N=(j-3)D+C.
\tag{16.209}
\]

因为 \(\gcd(N,D)=1\)，对每个整数 \(j\) 都有
\(\gcd(s_j,D)=1\)。把 \(F(N/D)=0\) 代入
\(D^4F((N+X)/D)\in\mathbf Z[X]\)，其常数项为零；在
\(X=s_j\) 处取值并消去与 \(s_j\) 互素的 \(D^4\)，得到

\[
\boxed{s_j\mid F(j).}
\tag{16.210}
\]

取根两侧的相邻整数 \(j=2,4\)，即

\[
s_2=-(D-C),
\qquad
s_4=D+C.
\]

§16.27 的 \(2,5\)-进赋值计算在这两点仍精确成立。事实上第二项
仍有赋值 \(2M+2\) 与 \(\nu_5\)，第一项的对应赋值都严格更高；
因此

\[
v_2(F(2))=v_2(F(4))=2M+2,
\qquad
v_5(F(2))=v_5(F(4))=\nu_5.
\tag{16.211}
\]

同一个对数导数公式 (16.199) 在 \(2\le J\le4\) 上仍为正，因为

\[
\frac{J(TJ+a_3)(TJ+2a_3)}{a_3^2}
<4\cdot5\cdot6=120<10P-J.
\]

而 \(2<J_{\rm def}<3<4\)，故

\[
F(2)<0<F(4).
\tag{16.212}
\]

于是存在两个新的正奇 \(5\)-进单位

\[
\boxed{
\Xi_-:=
\frac{-F(2)}
{2^{2M+2}5^{\nu_5}(D-C)}
\in\mathbf Z_{>0},
\qquad
\Xi_+:=
\frac{F(4)}
{2^{2M+2}5^{\nu_5}(D+C)}
\in\mathbf Z_{>0},
}
\tag{16.213}
\]

\[
\gcd(\Xi_-\Xi_+,10)=1.
\]

而且

\[
\gcd(D-C,D+C)
=\gcd(D-C,2C)=1,
\tag{16.214}
\]

因为 \(D\) 为偶数、\(C\) 为奇数且 \(\gcd(C,D)=1\)。所以
rational root 不仅要求小补余量 \(C\) 整除 \(F(3)\)，还同时要求
两个互素、都与 \(D\) 同阶的数 \(D-C,D+C\) 分别整除 \(F(2),F(4)\)。

这两个 cofactor 也继承 §16.28 的 denominator-wide 平方类。对
\(j\in\{2,4\}\) 记

\[
\mathscr A_j:=j(jT+2a_3)(10P-j)^2,
\qquad
\mathscr B_j:=(jT+a_3)^2.
\]

与 (16.202) 相同的正规化给出

\[
\frac{F(j)}{2^{2M+2}5^{\nu_5}}
=
c_u^2g^2L^3\mathscr A_j
-q^2c_+^2YN\mathscr B_j.
\]

代入 \(N=jD-s_j\)，再除以 \(s_j\)，可得

\[
\boxed{
\Xi_j
\equiv q^2c_+^2Y(jT+a_3)^2
\pmod D,
\qquad j=2,4,
}
\tag{16.215}
\]

其中 \(\Xi_2:=\Xi_-\)、\(\Xi_4:=\Xi_+\)。特别地

\[
\boxed{
\Xi_-\equiv\Xi_+\equiv
Y(qc_+a_3)^2
\pmod{2^m5^d}.
}
\tag{16.216}
\]

(16.213)–(16.216) 是比单独 \(C\mid F(3)\) 更强的三点
rational-root sieve：一个小除数与两个互素大除数必须共享同一个
denominator 平方类。它仍未自动给出矛盾，因为三个被除数随 prefix
增长；后续不能把它误称为有限枚举，而应寻找三 cofactor 的
resultant 或 reciprocity obstruction。

### 16.30 `已严格完成 / 审计`：mixed bridge 恢复 source coprimality 并锁定 `chi_E` 的符号

(16.186) 先恢复一组本原性。已有

\[
\gcd(C,g)=1,\qquad
\gcd(a_2,g)=1,\qquad
\gcd(c_-,g)=1,\qquad
\gcd(z_E,g)=1.
\tag{16.217}
\]

其中第二式来自 \(g\mid b_2\) 与 \(\gcd(a_2,b_2)=1\)，第三式来自
(16.35)，第四式来自 §16.23。故
\(-\varepsilon a_2c_-z_E\) 是模 \(g\) 的单位。由

\[
c_uC\equiv-\varepsilon a_2c_-z_E\pmod g
\]

及 \(C\) 也是模 \(g\) 的单位，得到

\[
\boxed{\gcd(c_u,g)=1.}
\tag{16.218}
\]

再由

\[
c_-z_E\equiv-5^{d+1}H\pmod g
\]

和 \(\gcd(5c_-z_E,g)=1\)，同时得到

\[
\boxed{\gcd(H,g)=1.}
\tag{16.219}
\]

结合旧 source split 的 \(\gcd(q,g)=1\)，(16.208) 还能把可能的
零因子通道精确隔离到 \(A_3=3T+a_3\)。若 \(p^e\Vert g\)，则

\[
\boxed{
\min\{v_p(\Xi_C),e\}
=
\min\{2v_p(A_3),e\}.
}
\tag{16.219a}
\]

事实上 (16.208) 右边除 \(A_3^2\) 外都是 \(p\)-进单位；若
\(2v_p(A_3)<e\)，同余两边有同一精确赋值，若
\(2v_p(A_3)\ge e\)，两边都在模 \(p^e\) 下为零。特别地，在
\(p\nmid A_3\) 的非饱和通道，\(\Xi_C\) 是单位并满足

\[
\boxed{
\left(\frac{\Xi_CC^{-1}}p\right)
=\left(\frac{c_u}p\right).
}
\tag{16.219b}
\]

所以不是所有零因子都自动消失；严格结论是它们只能来自
\(\gcd(A_3,g)\)，且在未饱和层总以偶赋值出现。

这里 (16.218) 也可直接由旧 source split 的
\(\gcd(c_u,\rho)=1\) 与 \(g=2^{t-1}\rho\) 得到，(16.219) 也可由
\(H\equiv-5^{M-1}\pmod g\) 得到；所以这两条 coprimality 是一致性
恢复，不另计作独立 obstruction。下面的实符号锁才是 mixed lift 新增的
Archimedean 信息。

\(\chi_E\) 的实符号也不再自由。由 §12 的精确尺度

\[
c_uD=\frac{(5^{M-1}+H)5^d}{4}
\]

以及 \(H<5^{M-1}/19\)、
\(a_2>(249/250)10^{M-1}\)，得到

\[
\frac{c_uD}{a_2}
<
\frac{1250}{4731}\frac{5^d}{2^{M-1}}
<\frac1{200}.
\tag{16.220}
\]

最后一步只需 \(5<2^3\)、\(d<9M/77\) 与 \(M\ge11\)：

\[
\frac{5^d}{2^{M-1}}
<2^{\,1-50M/77}<\frac1{64},
\]

再注意 \(1250/(4731\cdot64)<1/200\)。由 \(C/D<3/250\)，

\[
0<c_uC
<\frac{3c_uD}{250}
<\frac{3a_2}{50000}
<a_2.
\tag{16.221}
\]

而 \(z_E\) 是非零奇数，\(c_-\ge1\)，所以

\[
|\,\varepsilon a_2c_-z_E\,|
\ge a_2
>c_uC.
\]

从定义 \(g\chi_E=c_uC+\varepsilon a_2c_-z_E\) 可见大项不可能被
顶部补余量改变符号：

\[
\boxed{
\chi_E\ne0,
\qquad
\operatorname{sgn}(\chi_E)
=\operatorname{sgn}(\varepsilon z_E),
\qquad
\varepsilon z_E\chi_E>0.
}
\tag{16.222}
\]

更定量地，

\[
\boxed{
a_2c_-|z_E|-\frac{3c_uD}{250}
<
g|\chi_E|
<
a_2c_-|z_E|+\frac{3c_uD}{250}.
}
\tag{16.223}
\]

等价地，mixed lift 本身是一个统一的窄有理接触：

\[
\boxed{
\left|
\frac{g\chi_E}{\varepsilon a_2c_-z_E}-1
\right|
=
\frac{c_uC}{a_2c_-|z_E|}
<\frac3{50000}.
}
\tag{16.224}
\]

所以 \((z_E,\chi_E)\) 不是任意二维整数核：两坐标的象限由
\(\varepsilon\) 唯一锁定，且 \(\chi_E\) 是
\(\varepsilon a_2c_-z_E/g\) 的极窄相对扰动。结合 (16.218)，
三 cofactor 的下一 reciprocity 审计可以在 \(g\) 的每个非饱和奇素
因子上合法消去 \(c_u,C,z_E\)；唯一仍须单列的是
\(2v_p(A_3)\ge v_p(g)\) 的饱和通道。

### 16.31 `已严格完成`：消去中心代表后的 denominator character law

§16.28 的 cofactor residue 与 §16.25、§16.23 的两个中心同余可以
继续合并，而且 \(C,c_u,z_E,H\) 会全部消失。先由 (16.207) 与
(16.186)：

\[
\Xi_C
\equiv
-\varepsilon a_2c_-z_E
\bigl(q(3T+a_3)\bigr)^2
\pmod g.
\tag{16.225}
\]

再用

\[
c_-z_E\equiv-5^{d+1}H\pmod g,
\qquad
H\equiv-5^{M-1}\pmod g,
\]

得到纯 prefix/denominator character law

\[
\boxed{
\Xi_C
\equiv
-\varepsilon a_2\,5^{M+d}
\bigl(q(3T+a_3)\bigr)^2
\pmod g.
}
\tag{16.226}
\]

还可用 \(c_Qq\equiv5^M\pmod g\) 消去 \(q\)：

\[
\boxed{
c_Q^2\Xi_C
\equiv
-\varepsilon a_2\,5^{3M+d}(3T+a_3)^2
\pmod g.
}
\tag{16.227}
\]

这里 \(c_Q\) 与 \(g\) 互素，所以没有引入新的零因子。特别地，对
任意奇素数 \(p\mid g\) 且 \(p\nmid(3T+a_3)\)，

\[
\boxed{
\left(\frac{\Xi_C}{p}\right)
=
\left(
\frac{-\varepsilon a_2\,5^{M+d}}p
\right).
}
\tag{16.228}
\]

因此 §16.30 的非饱和 reciprocity channel 已不再含 Gaussian quotient、
source factor 或中心代表：它只读取
\(-\varepsilon a_2 5^{M+d}\) 在 \(g\) 的奇素因子上的二次特征。
另一方面 §16.28 仍给出

\[
\Xi_C\equiv Y(qc_+a_3)^2\pmod{2^m5^d}.
\tag{16.229}
\]

所以当前真正需要比较的两端已经变成

\[
\boxed{
\begin{array}{c}
\Xi_C/Y\text{ 在 }2^m5^d\text{ 上为平方},\\
\Xi_C/(-\varepsilon a_25^{M+d})
\text{ 在每个 }p\mid g,\ p\nmid A_3\text{ 处为平方}.
\end{array}
}
\tag{16.230}
\]

(16.230) 是明确的 reciprocity 接口，但尚不是矛盾：\(g\) 的 split
prime support 与 \(a_2,Y\) 的二次特征仍可能协调。下一步必须从
square-side factorization 或三 cofactor \(\Xi_-,\Xi_C,\Xi_+\) 的
共同 cubic quotient 中固定至少一个相反字符；仅重复 (16.226) 的
等价写法不会增加约束。

还必须保留一个边界：若 \(\rho=1\)，则 \(g=2^{t-1}\) 没有奇素因子，
(16.228) 为空陈述；若所有奇素因子又都落入
\(2v_p(A_3)\ge v_p(g)\) 的饱和层，character law 同样不能直接收费。
所以完整闭环必须同时处理 pure-\(2\) 与 odd-saturated 两个通道，不能
假设 \(g\) 自动提供可用的非饱和奇素数。

### 16.32 `已严格完成 / 失效降级`：提升到 `g^2` 不会产生新的二次特征

一个自然尝试是把 (16.204) 从模 \(g\) 提升到模 \(g^2\)，希望得到
第二个独立 character。精确正规化 (16.202) 说明这条路线实际上仍然
退化。记

\[
K:=q^2c_+^2Y,
\qquad
A_3:=3T+a_3.
\]

由于 (16.202) 的第一项被 \(g^2\) 整除，而
\(c_Q^2XY=c_+^2Y(3D-C)\)，有

\[
C\Xi_C
\equiv
K(C-3D)A_3^2
\pmod{g^2}.
\]

\(\gcd(C,g)=1\)，故

\[
\boxed{
\Xi_C
\equiv
Y(qc_+A_3)^2
\left(1-3DC^{-1}\right)
\pmod{g^2}.
}
\tag{16.231}
\]

现在逐个 prime power \(p^e\Vert g\) 检查最后的 principal unit。
若 \(p\) 为奇数，则 \(p^e\mid D\)，并且

\[
1-3DC^{-1}
\equiv
\left(1-\frac32DC^{-1}\right)^2
\pmod{p^{2e}},
\tag{16.232}
\]

因为平方展开的最后一项含 \(D^2\)，从而被 \(p^{2e}\) 整除。
若 \(p=2\)，写 \(e=v_2(g)=t-1\ge2\)。此时

\[
v_2(D)=e+m\ge3,
\]

所以 \(1-3DC^{-1}\equiv1\pmod8\)，它是每个
\(2^{2e}\) 单位群中的平方。于是：

\[
\boxed{
1-3DC^{-1}
\text{ 在模 }g^2\text{ 的每个 prime-power 分量上都是平方}.
}
\tag{16.233}
\]

特别地，在 \(\gcd(A_3,g)=1\) 的通道，(16.231) 只把
\(\Xi_C/Y\) 从模 \(g\) 的平方提升成模 \(g^2\) 的平方，并没有固定
任何相反 Legendre/Jacobi character。若 \(A_3\) 与 \(g\) 不互素，
先剥去 §16.30 已识别的偶赋值后，所有非饱和层仍得到同一结论。

所以“单纯把 rational-root congruence 再提升一层”不能关闭本核：
二阶修正 \(1-3DC^{-1}\) 自动落在 principal squares 中。这一 no-go
把后续目标进一步收紧为**非二次特征的信息**——例如三个 cubic
cofactor 的加性 resultant、符号/高度不等式，或饱和通道的精确
prime-power 大小；不能继续把同一平方类在 \(g,g^2,\ldots\) 上重复
收费。

### 16.33 `已严格完成`：三个 cofactor 是严格递增且严格凹的相邻值

§16.32 说明继续加深二次特征无效，因此转而保留三个 cofactor 的
加性信息。令

\[
r:=J_{\rm def}=\frac ND,
\qquad
K:=10P,
\]

\[
f(J):=J(TJ+2a_3)(K-J)^2,
\qquad
h(J):=(TJ+a_3)^2.
\]

写 \(A=b_2^2T>0\)、\(B=Q^2N_0>0\)，则

\[
F(J)=Af(J)-Bh(J),
\qquad
\frac BA=\frac{f(r)}{h(r)}.
\tag{16.234}
\]

先证明 \(F\) 在 \(2\le J\le4\) 上严格凸。令

\[
\mathscr E(J,r):=
h(r)f''(J)-f(r)h''(J).
\]

把它按 \(K\) 展开，二次首项恰为

\[
2Ta_3^2K^2.
\]

在

\[
2\le J\le4,\qquad 2<r<3,\qquad
T<a_3<\frac{251}{250}T<2T
\]

上，线性项所有可能的负贡献之和绝对值小于
\(2048T^3K\)，常数项的负贡献绝对值小于 \(1024T^3\)。
因此

\[
\mathscr E(J,r)
>
T^3(2K^2-2048K-1024)>0,
\tag{16.235}
\]

因为 \(K=10P>9\cdot10^{11}\)。由 (16.234)，

\[
\boxed{
F''(J)=\frac{A}{h(r)}\mathscr E(J,r)>0
\qquad(2\le J\le4).
}
\tag{16.236}
\]

同时 \(h'''=0\)，而直接求导给出

\[
F'''(J)
=12A(2JT-KT+a_3)<0,
\tag{16.237}
\]

因为 \(K>2J+a_3/T<10\)。所以 \(F\) 不仅严格凸，其曲率还严格
递减。

定义固定根 \(r\) 的 secant-slope 函数

\[
\mathscr H(J):=
\frac{F(J)-F(r)}{J-r}
=\frac{F(J)}{J-r}.
\]

积分表示

\[
\mathscr H(J)
=\int_0^1F'\!\left(r+t(J-r)\right)\,dt
\tag{16.238}
\]

给出

\[
\mathscr H'(J)
=\int_0^1tF''\!\left(r+t(J-r)\right)\,dt>0,
\]

\[
\mathscr H''(J)
=\int_0^1t^2F'''\!\left(r+t(J-r)\right)\,dt<0.
\tag{16.239}
\]

另一方面 \(s_j=D(j-r)\)，故 §16.27、§16.29 的三个正 cofactor
满足

\[
\Xi_j=
\frac{\mathscr H(j)}
{2^{2M+2}5^{\nu_5}D},
\qquad
j=2,3,4,
\]

其中 \(\Xi_2=\Xi_-\)、\(\Xi_3=\Xi_C\)、\(\Xi_4=\Xi_+\)。
由 (16.239)：

\[
\boxed{
0<\Xi_+-\Xi_C
<
\Xi_C-\Xi_-.
}
\tag{16.240}
\]

再由三者共享 (16.216) 的模 \(L=2^m5^d\) 余类，定义

\[
\Delta_-:=
\frac{\Xi_C-\Xi_-}{L},
\qquad
\Delta_+:=
\frac{\Xi_+-\Xi_C}{L}.
\]

它们不是任意有理数，而满足

\[
\boxed{
\Delta_-,\Delta_+\in\mathbf Z_{>0},
\qquad
\Delta_->\Delta_+,
\qquad
\Delta_-\ge2,\quad\Delta_+\ge1.
}
\tag{16.241}
\]

这是三点系统中第一条真正超出 quadratic character 的加性约束：
三个巨大 cofactor 位于同一 \(L\)-余类，严格递增，并且左间隔严格
大于右间隔。它仍未给出上界，故不能仅由
\(\Delta_-\ge2,\Delta_+\ge1\) 宣称矛盾；下一步应把
\(\Delta_--\Delta_+\) 写成 quotient cubic 的显式二阶差分，并与
\((z_E,\chi_E)\) 或 \(D\pm C\) 的大小联立。

### 16.34 `已严格完成`：cubic 二阶差分有精确的巨大正因子

§16.33 留下的
\(\Delta_--\Delta_+\) 可以完全展开，并不需要估计 cubic 的其余
系数。写

\[
F(J)=f_4J^4+f_3J^3+\cdots.
\]

由 (16.234) 的第一项直接读出

\[
f_4=b_2^2T^2,
\qquad
f_3=b_2^2T(2a_3-2KT).
\tag{16.242}
\]

因为 \(F(r)=0\)，secant polynomial
\(\mathscr H(J)=F(J)/(J-r)\) 的三次、二次系数分别为

\[
f_4,\qquad f_3+rf_4.
\]

任意 cubic \(uJ^3+vJ^2+\cdots\) 在 \(2,3,4\) 的中心二阶差分为
\(18u+2v\)。因此

\[
\begin{aligned}
2\mathscr H(3)-\mathscr H(2)-\mathscr H(4)
&=-2\bigl(f_3+(r+9)f_4\bigr)\\
&=
2b_2^2T^2
\left(2K-r-9-\frac{2a_3}{T}\right).
\end{aligned}
\tag{16.243}
\]

由 \(\Xi_j=\mathscr H(j)/(2^{2M+2}5^{\nu_5}D)\) 与
\(L=2^m5^d\)，(16.243) 给出

\[
\Delta_--\Delta_+
=
2^{2m+1}5^{m+d}c_u^2g
\left(
2K-r-9-\frac{2a_3}{T}
\right).
\tag{16.244}
\]

这里使用了

\[
b_2=2^{M+m+1}c_ug,
\qquad
\nu_5+2d=\lambda,
\qquad
\frac TL=5^\lambda.
\]

再代入 \(r=3-C/D\)、\(D=gL\)，并提取整数因子：

\[
\begin{aligned}
\Delta_--\Delta_+
&=
2^{m+1}5^dc_u^2
\left[
gT(2K-12)-2ga_3+5^\lambda C
\right]\\
&=
\boxed{
2^{m+1}5^dc_u^2
\left\{
g\bigl((2K-9)T-a_3\bigr)-H_0
\right\},
}
\end{aligned}
\tag{16.245}
\]

其中最后一步用了 (16.100)
\(H_0=g(3T+a_3)-5^\lambda C\)。

大括号严格为正。事实上

\[
\frac{H_0}{gT}
=3+\frac{a_3}{T}-\frac CD
<\frac{1001}{250},
\]

而 \(a_3/T<251/250\)，故

\[
g\bigl((2K-9)T-a_3\bigr)-H_0
>
gT(2K-15)>0.
\tag{16.246}
\]

于是三 cofactor 的凹性间隔不仅是两个相邻正整数：

\[
\boxed{
2^{m+1}5^dc_u^2
\mid
(\Delta_--\Delta_+),
\qquad
\Delta_--\Delta_+
>
2^{m+1}5^dc_u^2gT(2K-15).
}
\tag{16.247}
\]

这把第一条 non-character 信息提升为一个随 \(M,m\) 巨大增长的精确
additive curvature。它仍不单独矛盾，因为 \(\Delta_+\) 本身也随
prefix 增长；下一步应求 \(\Delta_+\) 的同尺度上界，或把
(16.245) 模 \(D-C,D+C\) 与 \(\chi_E\) 的窄有理接触联立。没有该
上界/模约束时，巨大可除性不能被误写成空性。

### 16.35 `已严格完成`：右间隔主导曲率，两个间隔之比落在 `(1,2)`

§16.34 所需的“同尺度上界”至少可以先在三个 cofactor 内部完成。
quotient cubic 的一次前向差为

\[
\mathscr H(4)-\mathscr H(3)
=f_2+(r+7)f_3+(r^2+7r+37)f_4.
\]

由 (16.234) 和 \(B/A=f(r)/h(r)\)，

\[
f_2
=A\left(
TK^2-4a_3K
-T^2\frac{f(r)}{h(r)}
\right),
\]

故

\[
\Delta_+
=
\frac{A\mathscr S_+}
{2^{2M+2}5^{\nu_5}DL},
\tag{16.248}
\]

其中

\[
\mathscr S_+
:=
TK^2-4a_3K
-T^2\frac{f(r)}{h(r)}
+(r+7)(2a_3-2KT)
+(r^2+7r+37)T.
\]

主二次项有统一下界。恒等式

\[
\frac{Tr(Tr+2a_3)}{(Tr+a_3)^2}
=1-\frac{a_3^2}{(Tr+a_3)^2}
<\frac{15}{16}
\]

来自 \(r<3\) 与 \(a_3>T\)。因此

\[
TK^2-T^2\frac{f(r)}{h(r)}
>
\frac1{16}TK^2.
\]

又 \(a_3<2T\)、\(r+7<10\)，其余可能为负的线性项总和大于
\(-28TK\)，最后一项为正。所以

\[
\boxed{
\mathscr S_+
>
T\left(\frac{K^2}{16}-28K\right).
}
\tag{16.249}
\]

另一方面 §16.34 的 curvature numerator 在除去相同正 denominator
前为

\[
2AT\left(2K-r-9-\frac{2a_3}{T}\right)
<4ATK.
\tag{16.250}
\]

由于 \(K>9\cdot10^{11}>512\)，

\[
T\left(\frac{K^2}{16}-28K\right)>4TK.
\]

比较 (16.248)–(16.250)，得到

\[
\boxed{
0<\Delta_--\Delta_+<\Delta_+,
\qquad
1<\frac{\Delta_-}{\Delta_+}<2.
}
\tag{16.251}
\]

特别地，(16.247) 也自动给出 \(\Delta_+\) 的同一巨大下界；但
(16.251) 说明 curvature 并不会大到吞掉右间隔，所以不能从“二阶差分
很大”直接制造符号矛盾。严格剩余目标变成：利用
\[
\Delta_-=\Delta_++(\Delta_--\Delta_+)
\]
中 (16.245) 已知的精确加数，证明右间隔 \(\Delta_+\) 的 prime support
或模 \(D\pm C\) 余类不允许该加法，而不是继续做纯实大小比较。

### 16.36 `已严格完成`：两个相邻间隔的二进深度都精确等于一层

三 cofactor 的模 \(D\) 公式还能给加性间隔一个精确二进结构。
由 (16.215)，

\[
\begin{aligned}
\Xi_+-\Xi_C
&\equiv
q^2c_+^2Y
\left[(4T+a_3)^2-(3T+a_3)^2\right]\\
&=
q^2c_+^2Y\,T(7T+2a_3)
\pmod D,
\end{aligned}
\tag{16.252}
\]

\[
\Xi_C-\Xi_-
\equiv
q^2c_+^2Y\,T(5T+2a_3)
\pmod D.
\tag{16.253}
\]

\(q,c_+,Y,a_3\) 均为奇数，且 \(m\ge1\)，所以

\[
v_2\!\left(T(7T+2a_3)\right)
=
v_2\!\left(T(5T+2a_3)\right)
=m+1.
\]

另一方面

\[
v_2(D)=m+v_2(g)=m+t-1\ge m+2.
\]

因此 (16.252)–(16.253) 的模数比右边的最低二进层至少再深一层，
不会发生提升抵消：

\[
\boxed{
v_2(\Xi_+-\Xi_C)
=
v_2(\Xi_C-\Xi_-)
=m+1.
}
\tag{16.254}
\]

除以 \(L=2^m5^d\) 后，

\[
\boxed{
v_2(\Delta_-)=v_2(\Delta_+)=1.
}
\tag{16.255}
\]

§16.34 的精确 curvature 还给出更深的差值。记 (16.245) 大括号为
\[
\mathscr B_\Delta
:=
g\bigl((2K-9)T-a_3\bigr)-H_0.
\]

第一项为偶数而 \(H_0\) 为奇数，故 \(\mathscr B_\Delta\) 为奇数。
模 \(5\) 又有

\[
\mathscr B_\Delta
\equiv-ga_3-ga_3
=-2ga_3\not\equiv0\pmod5.
\]

于是

\[
\boxed{
v_2(\Delta_--\Delta_+)=m+1,
\qquad
v_5(\Delta_--\Delta_+)=d.
}
\tag{16.256}
\]

等价地，存在奇数 \(u_-,u_+\) 使

\[
\Delta_-=2u_-,
\qquad
\Delta_+=2u_+,
\qquad
u_-\equiv u_+\pmod{2^m},
\qquad
v_2(u_--u_+)=m.
\tag{16.257}
\]

这为 §16.31 明确留下的 pure-\(2\) 通道补上了非平凡信息：
两个相邻 cofactor gap 除去公共 \(L\) 后都恰含一个 \(2\)，但它们的
差又额外含整整 \(m\) 层。该结构仍可实现，故不是矛盾；下一步要把
(16.257) 与 quotient cubic 的一次差显式式或 \(D\pm C\) 的奇除数
结构联立。

### 16.37 `已严格完成`：两个 gap 各有唯一的 `D\pm C` 大模数余类

现在把 §16.36 的 gap 真正送回两个互素大除数。由

\[
\frac{F(2)}{2^{2M+2}5^{\nu_5}}
=-(D-C)\Xi_-,
\quad
\frac{F(3)}{2^{2M+2}5^{\nu_5}}
=C\Xi_C,
\]

\[
\frac{F(4)}{2^{2M+2}5^{\nu_5}}
=(D+C)\Xi_+,
\]

以及

\[
\Xi_-=\Xi_C-L\Delta_-,
\qquad
\Xi_+=\Xi_C+L\Delta_+,
\]

中心 cofactor \(\Xi_C\) 在二阶差分中完全消去：

\[
\boxed{
\mathcal T_2
:=
\frac{F(4)-2F(3)+F(2)}
{2^{2M+2}5^{\nu_5}L}
=
(D+C)\Delta_+
+(D-C)\Delta_-.
}
\tag{16.258}
\]

左边确为整数，因为右边已经是整数。若需要完全不依赖 cofactor
记号的显式式，利用 §16.34 的 \(f_4,f_3,f_2\) 可写成

\[
\boxed{
\mathcal T_2
=
\frac{
2b_2^2T
\left[
TK^2-(18T+4a_3)K+18a_3+55T
\right]
-2Q^2N_0T^2
}{
2^{2M+2}5^{\nu_5}L
}.
}
\tag{16.259}
\]

由 \(\gcd(D-C,D+C)=1\)，且两个模数均为奇数并与 \(C\) 互素，
\(2C\) 在两边都可逆。把 (16.258) 分别模 \(D-C,D+C\)：

\[
\boxed{
\Delta_+
\equiv
(2C)^{-1}\mathcal T_2
\pmod{D-C},
}
\tag{16.260}
\]

\[
\boxed{
\Delta_-
\equiv
-(2C)^{-1}\mathcal T_2
\pmod{D+C}.
}
\tag{16.261}
\]

再代入 \(\Delta_-=\Delta_++\Gamma_\Delta\)，其中
\(\Gamma_\Delta\) 是 (16.245) 的显式正整数，得到对同一个
\(\Delta_+\) 的两条互素 CRT：

\[
\boxed{
\begin{aligned}
\Delta_+
&\equiv(2C)^{-1}\mathcal T_2
\pmod{D-C},\\
\Delta_+
&\equiv
-\Gamma_\Delta-(2C)^{-1}\mathcal T_2
\pmod{D+C}.
\end{aligned}
}
\tag{16.262}
\]

所以 \(\Delta_+\) 被唯一固定在模

\[
(D-C)(D+C)=D^2-C^2
\]

的一个余类中；\(\Delta_-\) 随后由精确加数
\(\Gamma_\Delta\) 恢复。这是 (16.245) 首次与两个 rational-root
大除数形成真正的 additive CRT，而不是再次比较平方类。

严格边界仍需说明：当前没有
\(\Delta_+<D^2-C^2\) 的上界，实际上粗尺度允许它远大于该模数；
所以“唯一 CRT 余类”仍不等于“唯一整数”或空性。下一步必须控制
\[
Q_\Delta:=
\left\lfloor\frac{\Delta_+}{D^2-C^2}\right\rfloor
\]
的高度/符号，或证明 (16.262) 的自然代表与
\(1<\Delta_-/\Delta_+<2\)、(16.256) 的精确赋值不相容。

### 16.38 `已严格完成`：additive CRT 产生无饱和缺陷的新 character

(16.258) 与 \(\Delta_-=\Delta_++\Gamma_\Delta\) 还能直接解出右
gap：

\[
\boxed{
2D\Delta_+
=
\mathcal T_2-(D-C)\Gamma_\Delta.
}
\tag{16.263}
\]

由 (16.256)，

\[
E_\Delta:=2^{m+1}5^d
\]

整除 \(\Gamma_\Delta\)。而 (16.263) 右边第一项
\(2D\Delta_+\) 也被 \(E_\Delta\) 整除，所以
\(E_\Delta\mid\mathcal T_2\)。定义

\[
\widetilde{\mathcal T}_2
:=\frac{\mathcal T_2}{E_\Delta},
\qquad
\widetilde\Gamma_\Delta
:=\frac{\Gamma_\Delta}{E_\Delta}
=c_u^2
\left\{
g((2K-9)T-a_3)-H_0
\right\}.
\tag{16.264}
\]

因为 \(2D/E_\Delta=g\)，(16.263) 变成新的精确整数 lift

\[
\boxed{
\widetilde{\mathcal T}_2
-(D-C)\widetilde\Gamma_\Delta
=g\Delta_+.
}
\tag{16.265}
\]

模 \(g\) 时，(16.100) 给出

\[
H_0\equiv-5^\lambda C\pmod g,
\]

所以

\[
\widetilde\Gamma_\Delta
\equiv c_u^25^\lambda C\pmod g.
\]

再用 \(D-C\equiv-C\pmod g\)，(16.265) 化为

\[
\boxed{
\widetilde{\mathcal T}_2
\equiv
-5^\lambda(c_uC)^2
\pmod g.
}
\tag{16.266}
\]

这条 character law 与 §16.31 有本质差别：右边不含
\(A_3=3T+a_3\)，所以没有 odd-saturated 通道。由
\(\gcd(5c_uC,g)=1\)，

\[
\boxed{
\gcd(\widetilde{\mathcal T}_2,g)=1,
\qquad
\left(\frac{\widetilde{\mathcal T}_2}{p}\right)
=
\left(\frac{-5^\lambda}{p}\right)
\quad
\text{对每个奇素数 }p\mid g.
}
\tag{16.267}
\]

也可用 mixed bridge 把平方根写成中心变量：

\[
c_uC\equiv-\varepsilon a_2c_-z_E\pmod g,
\]

故 (16.266) 等价于

\[
\widetilde{\mathcal T}_2
\equiv
-5^\lambda(a_2c_-z_E)^2
\pmod g.
\tag{16.268}
\]

因此三 cofactor 的 additive curvature 确实产出了一个新的、覆盖
\(g\) 全部奇素因子的无饱和 character；pure-\(2\) 的
\(\rho=1\) 仍是空 character 边界。当前尚缺的唯一一步是从
\(\widetilde{\mathcal T}_2\) 的显式式 (16.259) 独立证明相反二次
特征（或它在某个 \(p\mid\rho\) 上必为平方）。在得到该独立输入前，
(16.267) 仍是必要条件而非矛盾。

### 16.39 `已严格完成 / 后续降级`：additive cofactor 恒为 `3 mod 4`，并供应外部惰性素数

(16.266) 在二进分量上其实已经给出无条件信息。因为
\(t\ge3\)，有 \(4\mid g\)；而 \(5,c_u,C\) 均为奇数，所以

\[
\boxed{
\widetilde{\mathcal T}_2
\equiv
-5^\lambda(c_uC)^2
\equiv-1\equiv3\pmod4.
}
\tag{16.269}
\]

若 \(t\ge4\)，还可细化为

\[
\widetilde{\mathcal T}_2
\equiv
\begin{cases}
7\pmod8,&\lambda\text{ even},\\
3\pmod8,&\lambda\text{ odd}.
\end{cases}
\tag{16.270}
\]

由 (16.258)，\(\mathcal T_2>0\)，所以
\(\widetilde{\mathcal T}_2>0\)。因此它不可能是平方，也不可能是两个
整数平方之和；并且必存在奇素数 \(\ell\equiv3\pmod4\) 以奇次数
整除它。结合 (16.267) 的
\(\gcd(\widetilde{\mathcal T}_2,g)=1\)，该素数一定来自 denominator
之外：

\[
\boxed{
\exists\,\ell\equiv3\pmod4:
\quad
\ell\nmid g,
\qquad
v_\ell(\widetilde{\mathcal T}_2)\text{ odd}.
}
\tag{16.271}
\]

这补上了 pure-\(2\) 通道中原先为空的 character statement：
无论 \(\rho\) 是否为 \(1\)，三 cofactor 的 additive CRT 都强迫一个
新的外部 Gaussian-inert prime。它尚未立刻矛盾，因为当前没有证明
\(\widetilde{\mathcal T}_2\) 自身必须是 Gaussian norm；下一步最直接
的闭环目标因此变成：从 (16.259) 与原来的三条 norm composition
证明其全部 \(3\bmod4\) 素数赋值应为偶数。一旦建立，该 kernel 即
由 (16.269) 立即排除。

### 16.40 `已严格完成 / 降级`：显式式目前只是“尺度项减 Gaussian norm”

为了审计 §16.39 的最短闭环是否已经隐含成立，把 (16.259) 再按
deep-even 正规形完全约去。令

\[
\mathscr S_0
:=
TK^2-(18T+4a_3)K+18a_3+55T.
\]

由

\[
b_2=2^{M+m+1}c_ug,\quad
Q=2^{M+1}c_Qq,\quad
N_0=5^{\nu_5}XY,
\]

\[
\nu_5+2d=\lambda,\qquad m-d=\lambda,
\]

直接化简 (16.259) 与 (16.264)，得到

\[
\boxed{
\widetilde{\mathcal T}_2
=
Lc_u^2g^2\mathscr S_0
-
\bigl(c_Qq5^\lambda\bigr)^2XY.
}
\tag{16.272}
\]

第二项确实是一个 Gaussian norm：

\[
\bigl(c_Qq5^\lambda\bigr)^2XY
=
N\!\left(c_Qq5^\lambda\mathcal A_5\right).
\tag{16.273}
\]

但 (16.272) 是**差**而不是和，也没有出现控制两向量夹角的交叉项。
即使将来证明 \(L\mathscr S_0\) 本身是二平方和，“两个 Gaussian
norm 之差”仍不会自动成为 Gaussian norm。当前只能由
\(\widetilde{\mathcal T}_2>0\) 知道第一尺度项更大。

模 \(4\) 的现象也与此完全一致：第一项因 \(4\mid g\) 被 \(4\)
整除，而 (16.273) 是奇 Gaussian norm，故为 \(1\bmod4\)；其差正好
是 (16.269) 的 \(3\bmod4\)。因此不能把 (16.272) 的两个 norm-like
pieces 直接拼成所需的 norm 表示。

所以 §16.39 的候选闭环还需要一个真正新的 orientation identity，
形如

\[
Lc_u^2g^2\mathscr S_0
=N(Z_1),\qquad
N(Z_1)-N(Z_2)=N(Z_3),
\]

并给出相应的精确内积/正交关系；只有两项各自有 norm 解释不够。
在该交叉项出现前，“\(\widetilde{\mathcal T}_2\) 必为 Gaussian
norm”必须保持为待证，而不是从 (16.272) 直接宣称。

### 16.41 `已严格完成 / 降级`：additive CRT 商不是小商，而是至少 `5K`

§16.37 曾留下

\[
Q_\Delta=
\left\lfloor
\frac{\Delta_+}{D^2-C^2}
\right\rfloor.
\]

可以严格排除“它也许等于 \(0\) 或某个固定小整数”的希望。由
(16.248)–(16.249) 及

\[
\frac{b_2^2T^2}
{2^{2M+2}5^{\nu_5}DL}
=
2^{2m}5^{m+d}c_u^2g,
\]

有

\[
\Delta_+
>
2^{2m}5^{m+d}c_u^2g
\left(\frac{K^2}{16}-28K\right).
\tag{16.274}
\]

又 \(D=gL=g2^m5^d\)、\(D^2-C^2<D^2\)，故

\[
\frac{\Delta_+}{D^2-C^2}
>
\frac{c_u^25^\lambda}{g}
\left(\frac{K^2}{16}-28K\right).
\tag{16.275}
\]

high-2 slot (13.4±) 统一给出 \(g/T<1212/125<10\)，所以

\[
\frac{\Delta_+}{D^2-C^2}
>
\frac{c_u^2}{10\cdot2^m5^d}
\left(\frac{K^2}{16}-28K\right).
\tag{16.276}
\]

另一方面 \(m+d<51M/77\)，从而

\[
2^m5^d<10^{m+d}<10^{51M/77}.
\]

而 \(K=10P>9\cdot10^M\)、\(M\ge11\)，所以

\[
\frac{K}{2^m5^d}
>
9\cdot10^{26M/77}>1000.
\tag{16.277}
\]

最后 \(K>9\cdot10^{11}\) 给出

\[
\frac{K^2}{16}-28K>\frac{K^2}{17}.
\]

把它们代回 (16.276)，并用 \(c_u\ge1\)：

\[
\boxed{
\frac{\Delta_+}{D^2-C^2}
>
\frac{1000}{170}K
>5K,
\qquad
Q_\Delta\ge5K.
}
\tag{16.278}
\]

因此 additive CRT 的自然代表路线与早先 \(C\) 的小代表完全不同：
\(\Delta_+\) 至少跨过 \(5K\) 个完整的 \(D^2-C^2\) 周期。仅证明
CRT 唯一余类绝不可能关闭本核；必须研究这个随 prefix 无界增长的
商本身，或转回 §16.39 的外部惰性素数/orientation 缺口。

### 16.42 `已严格完成 / 审计`：once-normalized additive cofactor 接回 canonical discriminant

\(\widetilde{\mathcal T}_2\) 并非与旧判别平方完全无关。reflection
\(s=0\) 中，core 的 canonical discriminant coefficient 是

\[
K_0
=25\cdot2^{2(m+t)}u^2P^2-Q_0^2N_0.
\]

由

\[
u=c_u\rho,\qquad
g=2^{t-1}\rho,\qquad
Q_0=c_Qq,
\]

它精确化为

\[
\boxed{
K_0
=100\cdot2^{2m}c_u^2g^2P^2
-c_Q^2q^2N_0.
}
\tag{16.279}
\]

另一方面 \(K=10P\)。把 (16.272) 的 \(TK^2\) 主项与第二个 norm
合并，恰好得到

\[
Lc_u^2g^2TK^2
-
\bigl(c_Qq5^\lambda\bigr)^2XY
=5^{m+d}K_0.
\tag{16.280}
\]

这里用了 \(LT=2^{2m}5^{m+d}\)、
\(N_0=5^{\nu_5}XY\) 与
\(2\lambda-\nu_5=m+d\)。所以若定义

\[
\mathscr R_0
:=
-(18T+4a_3)K+18a_3+55T<0,
\]

则 once-normalized additive cofactor 的真实位置是

\[
\boxed{
\widetilde{\mathcal T}_2
=5^{m+d}K_0
+Lc_u^2g^2\mathscr R_0.
}
\tag{16.281}
\]

严格负号来自 \(K>9\cdot10^{11}\) 与 \(a_3<2T\)。结合
\(\widetilde{\mathcal T}_2>0\)，得到新的 canonical-discriminant
下界

\[
\boxed{
K_0
>
\left(\frac25\right)^m
c_u^2g^2
\left((18T+4a_3)K-18a_3-55T\right).
}
\tag{16.282}
\]

这项识别有两层审计意义：

1. §16.39 的外部惰性素数不是与旧判别式无关的全新自由对象；它位于
   \(5^{m+d}K_0\) 的一个显式负短移位上；
2. 但 (16.281) 仍是加法，不是因式分解。core 中
   \(5^\lambda(5^\lambda K_0-2cQ_0N_0)=Z^2\) 的平方条件尚未直接把
   这个短移位变成 Gaussian norm。

因此下一条最有希望的非重复路线，是把 canonical square \(Z^2\)
代入 (16.281)，审计负移位是否落入两个相邻平方之间；不能把
\(\widetilde{\mathcal T}_2\equiv3\bmod4\) 重新包装成旧 odd inert
excess 后重复收费。

### 16.43 `已严格完成 / 降级`：canonical square 代入后恰好恢复旧 odd inert excess

§16.42 建议把 canonical square 代入 (16.281)。完整代入表明，这不会
自动产生相邻平方矛盾，而是精确恢复 core §14.2 的
\(3\bmod4\) excess 机制。

canonical discriminant 为

\[
Z^2
=
5^\lambda
\left(
5^\lambda K_0-2cQ_0N_0
\right),
\qquad
Q_0=c_Qq,\quad c=c_Qc_u.
\tag{16.283}
\]

由右边可见 \(5^{\nu_5}\mid Z^2\)。写

\[
\nu_5=2h+\epsilon_5,
\qquad
\epsilon_5\in\{0,1\},
\qquad
Z_\nu:=\frac{Z}{5^{h+\epsilon_5}}\in\mathbf Z.
\]

则

\[
\frac{Z^2}{5^{\nu_5}}
=5^{\epsilon_5}Z_\nu^2.
\]

又因 \(m+d=\lambda+2d\) 与
\(\lambda-2d=\nu_5\)，从 (16.283) 解出

\[
\boxed{
5^{m+d}K_0
=
5^{\epsilon_5}Z_\nu^2
+2cQ_0N_0\,5^{2d}.
}
\tag{16.284}
\]

代回 (16.281)：

\[
\boxed{
\widetilde{\mathcal T}_2
=
5^{\epsilon_5}Z_\nu^2
+\mathscr J_\Delta,
}
\tag{16.285}
\]

其中

\[
\boxed{
\mathscr J_\Delta
:=
2cQ_0N_0\,5^{2d}
+Lc_u^2g^2\mathscr R_0.
}
\tag{16.286}
\]

\(K_0\) 为奇数，(16.283) 因而给出 \(Z\) 为奇数，所以
\(5^{\epsilon_5}Z_\nu^2\equiv1\pmod4\)。另一方面
\(c,Q_0,N_0\) 均为奇数，而 \(4\mid g\)，故

\[
\boxed{
\mathscr J_\Delta\equiv2\pmod4.
}
\tag{16.287}
\]

于是 (16.285) 重新得到

\[
\widetilde{\mathcal T}_2\equiv1+2\equiv3\pmod4,
\]

但没有得到 \(\widetilde{\mathcal T}_2\) 是平方或 Gaussian norm。
特别地，\(\mathscr J_\Delta\ne0\)，所以 canonical square 不会与
once-normalized additive cofactor 直接重合。

这说明 §16.39 的外部惰性素数供应不是可重复收费的第二个 inert
excess：代入 canonical square 后，它正是“平方 \(+\;2\bmod4\)
修正”所产生的旧 odd inert mechanism。若要继续这条路线，必须对
\(\mathscr J_\Delta\) 的 prime 来源作 core §14.2 的三分法
(denominator-prefix / source / spontaneous)，并在当前 endpoint
尺度上排除三类；单独使用 \(3\bmod4\) 已没有新信息。

### 16.44 `已严格完成 / 归一化修正`：真正的 \(2,5\)-本原 additive cofactor

§16.38 只除去了 \(\mathcal T_2\) 的共同因子
\(2^{m+1}5^d\)，但 (16.272) 还显示
\(\widetilde{\mathcal T}_2\) 本身含有第二份精确 \(5^d\)。事实上，

\[
\mathscr S_0
=TK^2-(18T+4a_3)K+18a_3+55T
\equiv18a_3\not\equiv0\pmod5,
\tag{16.288}
\]

因为 \(5\mid b_3\) 而 \(\gcd(a_3,b_3)=1\)。所以 (16.272) 第一项
的 \(5\)-进赋值恰为 \(d\)，而第二项的赋值恰为 \(2\lambda\)；
由 \(\lambda-2d=\nu_5\ge0\) 可知 \(2\lambda>d\)。因此

\[
\boxed{
v_5(\widetilde{\mathcal T}_2)=d.
}
\tag{16.289}
\]

应当把真正的 \(2,5\)-本原对象定义为

\[
\boxed{
\widehat{\mathcal T}_2
:=\frac{\widetilde{\mathcal T}_2}{5^d}
=\frac{\mathcal T_2}{2^{m+1}5^{2d}}.
}
\tag{16.290}
\]

除以 (16.272) 中的 \(5^d\)，得到整数显式式

\[
\boxed{
\widehat{\mathcal T}_2
=
2^mc_u^2g^2\mathscr S_0
-
(c_Qq)^2\,5^{\,2\lambda-d}XY.
}
\tag{16.291}
\]

它严格满足

\[
\boxed{
\widehat{\mathcal T}_2>0,\qquad
\gcd(\widehat{\mathcal T}_2,10g)=1,\qquad
\widehat{\mathcal T}_2\equiv3\pmod4.
}
\tag{16.292}
\]

这里正性来自 \(\widetilde{\mathcal T}_2>0\)；\(2,5\)-单位性来自
(16.289) 与 (16.269)；对 \(g\) 的互素性来自 (16.267)，因为
\(5\nmid g\)。同样把 (16.266) 除以模 \(g\) 的单位 \(5^d\)，可得

\[
\boxed{
\widehat{\mathcal T}_2
\equiv
-5^{\lambda-d}(c_uC)^2
\pmod g,
\qquad
\left(\frac{\widehat{\mathcal T}_2}{p}\right)
=
\left(\frac{-5^{\lambda-d}}p\right)
\quad(p\mid g,\ p\text{ odd}).
}
\tag{16.293}
\]

由于 \(5^d\equiv1\pmod4\)，§16.39 的外部惰性素数结论与
§16.43 的“平方 \(+\;2\bmod4\)”降级结论都原样传给
\(\widehat{\mathcal T}_2\)。本修正不制造新的 obstruction；它只把
后续 prime-source 分类的对象换成真正与 \(10g\) 互素的整数，避免把
必然存在的 \(5^d\) 错当成本原部分。

### 16.45 `已严格完成`：本原 cofactor 的 denominator/base-norm 接触由一个纯 numerator 多项式控制

(16.291) 还能给出不依赖二次特征的精确接触律。先记

\[
Q_0:=c_Qq.
\]

source split 给出
\(\gcd(c_u,Q_0g)=1\)。此外，若奇素数 \(p\mid c_ug\)，则
\(p\mid b_2\)，而 \(\gcd(a_2,b_2)=1\)，故

\[
N_0=C_0^2+a_2^2\not\equiv0\pmod p.
\]

由 \(N_0=5^{\nu_5}XY\) 且 \(5\nmid c_ug\)，得到

\[
\gcd(c_ug,XY)=1.
\tag{16.294}
\]

现在若 \(p\mid c_u\)，则 (16.291) 的第一项被 \(p\) 整除，而
第二项是 \(p\)-进单位；结合 (16.292) 已有的 \(g\)-互素性，

\[
\boxed{
\gcd(\widehat{\mathcal T}_2,c_ug)=1.
}
\tag{16.295}
\]

另一方面，\(2^mc_u^2g^2\) 是模 \(Q_0XY\) 的单位，而 (16.291)
第二项被 \(Q_0XY\) 整除。因此

\[
\widehat{\mathcal T}_2
\equiv
2^mc_u^2g^2\mathscr S_0
\pmod{Q_0XY},
\]

并得到精确 gcd identity

\[
\boxed{
\gcd(\widehat{\mathcal T}_2,Q_0XY)
=
\gcd(\mathscr S_0,Q_0XY).
}
\tag{16.296}
\]

更精确地，若 \(p^e\Vert Q_0XY\)，则 (16.291) 第二项至少被
\(p^e\) 整除，而第一项的系数为 \(p\)-进单位，所以

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),e\}
=
\min\{v_p(\mathscr S_0),e\}.
}
\tag{16.296a}
\]

这里 \(\mathscr S_0\) 只含 numerator blocks：

\[
\mathscr S_0
=T(K^2-6K+1)+(3T+a_3)(18-4K).
\tag{16.297}
\]

所以任取 §16.39 所迫出的
\(\ell\equiv3\pmod4\) 且
\(v_\ell(\widehat{\mathcal T}_2)\) 为奇数，已有严格二分：

1. 若 \(\ell\mid Q_0XY\)，则必有 \(\ell\mid\mathscr S_0\)，其
   denominator/base-norm 接触被同一个纯 numerator 整数控制；
2. 若 \(\ell\nmid Q_0XY\)，则它在当前 endpoint 因子库之外自发出现。

再结合 (16.295)，这种 \(\ell\) 永远不能来自 \(c_u\) 或 \(g\)。
而由 (16.50)、(16.60)，
\(XY=N(\mathcal A_5)\) 的两个 Gaussian 坐标除素数 \(3\) 外本原；
若 \(\ell\equiv3\pmod4\)、\(\ell\ne3\) 且 \(\ell\mid XY\)，则
\(\ell\) 必同时整除两坐标，矛盾。因此对任意非 \(3\) 的 inert
excess prime，上述第一类进一步收缩为

\[
\boxed{
\ell\ne3,\quad
\ell\mid Q_0XY
\quad\Longrightarrow\quad
\ell\mid\gcd(Q_0,\mathscr S_0).
}
\tag{16.298}
\]

于是当前只剩三个互不混淆的 endpoint 通道：固定异常素数 \(3\)；
同时接触 \(Q_0,\mathscr S_0\) 的非 \(3\) denominator prime；以及
不整除 \(Q_0XY\) 的 endpoint-external prime。
这一步把候选来源缩小了，但尚未关闭 core §14.2 的三类 excess：
\(Q_0\) 之外的 \(f\)、source-side \(\mathfrak n\) 尚未进入
(16.296)，而“\(\ell\mid\mathscr S_0\)”本身也不是矛盾。下一步需要
把 \(\mathscr S_0\) 与 prefix defect \(\Delta_{\rm pref}\) 或
source 双 Hensel 线性式求 resultant，而不能把 (16.296) 当作空性。

### 16.46 `已严格完成`：补齐 core denominator factor \(f\) 的接触律

core §12.7 的另一个 denominator factor 是

\[
f:=5^\lambda q+2c_u.
\]

由 source split，
\(\gcd(f,5c_u)=1\)，并且
\(\gcd(f,q)=1\)。在模 \(f\) 下有

\[
5^\lambda q\equiv-2c_u.
\]

把它代入未除第二份 \(5^d\) 的显式式 (16.272)，得到

\[
5^d\widehat{\mathcal T}_2
\equiv
c_u^2
\left(
2^m5^dg^2\mathscr S_0-4c_Q^2XY
\right)
\pmod f.
\tag{16.299}
\]

定义

\[
\boxed{
\mathscr R_f
:=
2^m5^dg^2\mathscr S_0-4c_Q^2XY.
}
\tag{16.300}
\]

由于 \(5^dc_u^2\) 是模 \(f\) 的单位，立刻得到

\[
\boxed{
\gcd(\widehat{\mathcal T}_2,f)
=
\gcd(\mathscr R_f,f).
}
\tag{16.301}
\]

并且若 \(p^e\Vert f\)，则同样有截断赋值恒等式

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),e\}
=
\min\{v_p(\mathscr R_f),e\}.
}
\tag{16.302}
\]

因此 core §14.2 的完整 denominator-prefix 因子 \(qf\) 在 endpoint
尺度上不再是未命名接触：

\[
\boxed{
\begin{aligned}
p\mid q,\ p\mid\widehat{\mathcal T}_2
&\Longrightarrow p\mid\mathscr S_0,\\
p\mid f,\ p\mid\widehat{\mathcal T}_2
&\Longrightarrow p\mid\mathscr R_f.
\end{aligned}
}
\tag{16.303}
\]

第一行来自 \(q\mid Q_0\) 与 (16.296)，第二行来自 (16.301)。
此外

\[
\mathscr R_f
\equiv-4c_Q^2XY\pmod{\mathscr S_0}.
\tag{16.304}
\]

所以若一个非 \(3\) 的 inert prime 同时接触
\(\mathscr S_0,\mathscr R_f\)，则 (16.50)、(16.60) 排除它整除
\(XY\)，从而它必须整除 \(c_Q\)。这把 denominator excess 精确压成
三个可审计的子通道：

\[
p\mid(q,\mathscr S_0),\qquad
p\mid(f,\mathscr R_f),\qquad
p\mid(c_Q,\mathscr S_0,\mathscr R_f),
\]

外加固定异常素数 \(3\)。这仍不是排除，因为尚无
\(\gcd(q,\mathscr S_0)=\gcd(f,\mathscr R_f)=1\)；但原来的抽象
“denominator-prefix excess”已被替换成两个显式整数接触问题。

### 16.47 `已严格完成`：固定异常素数 \(3\) 的精确一阶分类

§16.45–16.46 对非 \(3\) 的 inert prime 已去掉 \(XY\) 通道。剩余的
固定异常素数 \(3\) 也不是完全自由。首先 \(c_u\) 只含
\(1\bmod4\) 素数，所以 \(3\nmid c_u\)；并且

\[
C_0=\frac{9b_2}{2}\equiv0\pmod9.
\tag{16.305}
\]

若 \(3\mid g\)，(16.292) 已给出
\(3\nmid\widehat{\mathcal T}_2\)。以下设 \(3\nmid g\)。
由 \(T=10^m\)、\(K=10P\)、\(P=9\cdot10^{M-1}+a_2\)，有

\[
T\equiv1,\qquad K\equiv a_2\pmod3,
\]

所以 (16.288) 的更细模 \(3\) 形式是

\[
\boxed{
\mathscr S_0\equiv a_2^2-a_2a_3+1\pmod3.
}
\tag{16.306}
\]

若 \(3\mid a_2\)，则 (16.305) 给出 \(3\mid XY\)，而
(16.306) 给出 \(\mathscr S_0\equiv1\pmod3\)；从 (16.291) 立即
得到 \(3\nmid\widehat{\mathcal T}_2\)。因此只需考虑
\(3\nmid a_2\)，此时

\[
XY\equiv5^{-\nu_5}N_0
\equiv(-1)^{\nu_5}\pmod3.
\tag{16.307}
\]

若 \(3\nmid Q_0\)，把 (16.307) 代入 (16.291)，再用
\(\nu_5=m-3d\)，可得

\[
\widehat{\mathcal T}_2
\equiv
(-1)^m(\mathscr S_0-1)
\equiv
(-1)^m(1-a_2a_3)
\pmod3.
\tag{16.308}
\]

若 \(3\mid Q_0\)，则第二项消失，而 source split 保证
\(3\nmid g\)，故

\[
\widehat{\mathcal T}_2
\equiv(-1)^m\mathscr S_0
\equiv(-1)^m(-1-a_2a_3)
\pmod3.
\tag{16.309}
\]

综上，固定素数 \(3\) 能整除本原 additive cofactor 当且仅当

\[
\boxed{
\begin{array}{ll}
3\nmid gQ_0a_2
&\text{且 }a_2a_3\equiv1\pmod3,\\[2mm]
\text{或}\\[-1mm]
3\mid Q_0,\ 3\nmid a_2
&\text{且 }a_2a_3\equiv-1\pmod3.
\end{array}
}
\tag{16.310}
\]

特别地，只要这两个 digit residue 都不成立，§16.39 供应的奇次
inert prime 就必定不是 \(3\)，从而必须落入 §16.45–16.46 的显式
denominator 接触，或进入尚待与 \(\mathfrak n\) 对接的
endpoint-external 通道。式 (16.310) 只判定一阶可整除性；在允许
\(3\mid\widehat{\mathcal T}_2\) 的两个 residue 中，仍需进一步控制
\(v_3(\widehat{\mathcal T}_2)\) 的奇偶，不能把模 \(3\) 条件误写成
固定 \(3\) 已承担 odd excess。

### 16.48 `已严格完成 / 降级`：模 \(9\) 把固定 \(3\) 化成单一显式提升条件

在 (16.310) 允许 \(3\)-接触的两类中必有
\(3\nmid ga_2\)。由于 \(C_0\equiv0\pmod9\)，
\(N_0=5^{\nu_5}XY\) 给出

\[
XY\equiv5^{-\nu_5}a_2^2\pmod9.
\]

同时 \(10^m\equiv1\pmod9\) 且
\(K=10(9\cdot10^{M-1}+a_2)\equiv a_2\pmod9\)，故

\[
\mathscr S_0
\equiv a_2^2-4a_2a_3+1\pmod9.
\]

把两式代入 (16.291)，并使用
\[
2\lambda-d-\nu_5=\lambda+d=m,
\]
得到固定 \(3\) 的完整一阶提升式

\[
\boxed{
\widehat{\mathcal T}_2
\equiv
2^m(c_ug)^2
\left(a_2^2-4a_2a_3+1\right)
-5^mQ_0^2a_2^2
\pmod9.
}
\tag{16.311}
\]

因此在 (16.310) 的允许 residue 中：

\[
\boxed{
v_3(\widehat{\mathcal T}_2)=1
\iff
\text{(16.311) 的右边为 }3\text{ 或 }6\pmod9;
}
\tag{16.312}
\]

若右边为 \(0\bmod9\)，则只能推出
\(v_3(\widehat{\mathcal T}_2)\ge2\)。特别地，当 \(3\mid Q_0\) 时，
第二项已经被 \(9\) 整除，(16.312) 简化为

\[
v_3(\widehat{\mathcal T}_2)=1
\iff
a_2^2-4a_2a_3+1\not\equiv0\pmod9.
\tag{16.313}
\]

模 \(3\) 的允许条件并不自动固定 (16.311) 在模 \(9\) 下为
\(0,3,6\) 中哪一个；三种值都与当前的一阶 source-split residue
相容。因此“再看模 \(9\)”本身不会统一排除固定 \(3\)，但它把该通道
压成一个单一、可继续 Hensel 提升的显式式。若要证明 \(3\) 不承担
odd excess，下一步必须把 (16.311) 与 (16.101) 的 \(C\) 自然代表或
high quotient 的 \(k_h\)-allocation 联立，而不能只重复
\(a_2a_3\bmod3\)。

### 16.49 `已严格完成`：denominator 接触引出判别数 \(-23\) 的新 character

对 §16.45 中接触 \(Q_0\) 的非 \(3\) denominator inert prime，
(16.296) 强迫 \(p\mid\mathscr S_0\)。把 \(\mathscr S_0\) 看成
\(K\) 的二次式：

\[
\mathscr S_0
=
TK^2-(18T+4a_3)K+18a_3+55T.
\]

其判别式不是另一个 \(-1\)-Gaussian norm，而是

\[
\boxed{
\operatorname{disc}_K(\mathscr S_0)
=
8\mathscr R_{23},
\qquad
\mathscr R_{23}:=
2a_3^2+9Ta_3+13T^2.
}
\tag{16.314}
\]

这里

\[
\boxed{
\mathscr R_{23}
=2(a_3+2T)^2+(a_3+2T)T+3T^2
}
\tag{16.315}
\]

是判别数 \(1-4\cdot2\cdot3=-23\) 的正定二元二次型。因为当前
\(p\equiv3\pmod4\) 且 \(p\nmid10\)，\(T\) 是模 \(p\) 的单位。
若 \(p\mid\mathscr S_0\) 但 \(p\nmid\mathscr R_{23}\)，二次式在
模 \(p\) 下有根迫使

\[
\boxed{
\left(\frac{\mathscr R_{23}}p\right)
=
\left(\frac2p\right).
}
\tag{16.316}
\]

这与 §16.38 的 \((-5^{\lambda-d}/p)\) character 来源不同：它来自
纯 numerator curvature 的 \(-23\) 判别式，而不是把旧 odd inert
excess 再写一次。

剩余的 double-root 通道同样可精确描述。若
\(p\mid\mathscr R_{23}\)，则

\[
\boxed{
K\equiv9+2a_3T^{-1}\pmod p.
}
\tag{16.317}
\]

并且由 (16.315)，对 \(p\ne23\) 有
\[
\left(\frac{-23}p\right)=1.
\]
若再用 \(p\equiv3\pmod4\) 与二次互反律，则

\[
\boxed{
\left(\frac p{23}\right)=1
\qquad(p\ne23).
}
\tag{16.318}
\]

所以非 \(3\) 的 \(Q_0\)-denominator excess 现在分成两个严格算术
通道：

1. simple-root：同时满足 \(p\mid Q_0\) 与 (16.316) 的
   \(-23\) form character；
2. double-root：满足 (16.317)，且除 ramified prime \(23\) 外，
   \(p\bmod23\) 必为二次剩余。

这仍未给出空性，因为 \(Q_0\) 尚无与 \(-23\) form 相反的统一
character。真正的新闭环目标是：从
\(Q_0=5^M+2^mgc_u\) 计算
\(\mathscr S_0\) 对 \(q\) 的 resultant，看它是否强迫与
(16.316)/(16.318) 相反的 \(23\)-进分裂类型。\(f\)-channel 必须
另行使用 \(\mathscr R_f\)，如下节。

### 16.50 `已严格完成`：\(f\)-channel 也有独立的 curvature discriminant

对 \(p\mid f\) 的 denominator 接触，正确的二次式不是
\(\mathscr S_0\)，而是 (16.300) 的
\[
\mathscr R_f
=A_f\mathscr S_0-4c_Q^2XY,
\qquad
A_f:=2^m5^dg^2.
\]

由 \(f=5^\lambda q+2c_u=g\omega+c_u\) 与
\(\gcd(c_u,g)=1\)，有
\[
\gcd(f,10g)=1.
\]
所以对任意 \(p\mid f\)，\(\mathscr R_f\) 关于 \(K\) 的首项系数
\(A_fT\) 是模 \(p\) 的单位。直接计算判别式：

\[
\boxed{
\operatorname{disc}_K(\mathscr R_f)
=
8A_f\mathscr R_{23,f},
\qquad
\mathscr R_{23,f}
:=
A_f\mathscr R_{23}+2Tc_Q^2XY.
}
\tag{16.319}
\]

因此若 \(p\equiv3\pmod4\)、\(p\mid(f,\mathscr R_f)\)，且
\(p\nmid\mathscr R_{23,f}\)，则

\[
\boxed{
\left(\frac{\mathscr R_{23,f}}p\right)
=
\left(\frac2p\right)^{m+3}
\left(\frac5p\right)^d.
}
\tag{16.320}
\]

若 \(p\mid\mathscr R_{23,f}\)，则二次式只有一个重根，仍严格满足

\[
\boxed{
K\equiv9+2a_3T^{-1}\pmod p.
}
\tag{16.321}
\]

于是 \(q\)-channel 与 \(f\)-channel 已分别具有 (16.316) 和
(16.320) 两条 curvature character；两者的右边一般不同，不能再合并
成一个模 \(4\) 叙述。当前尚缺的是证明同一个 odd inert excess prime
必须同时经历两条 channel，或从 core factor allocation 推出某一条
右边与其已知 source character 相反。在这条分配桥建立前，
(16.316)/(16.320) 是严格必要条件而不是矛盾。

### 16.51 `已严格完成 / 审计`：所有 curvature character 来自一个全局平方配方

§16.49–16.50 的判别式还可以在整数层一次性配方。定义正整数

\[
\boxed{
\mathscr C_{23}
:=
2c_u^2g^2\mathscr R_{23}
+5^{\,m+2\lambda-d}Q_0^2XY.
}
\tag{16.322}
\]

直接展开 (16.291) 与 (16.314)，得到

\[
\boxed{
\left[
c_ug(TK-9T-2a_3)
\right]^2
=
\mathscr C_{23}
+5^m\widehat{\mathcal T}_2.
}
\tag{16.323}
\]

事实上 \(K\)-二次项与一次项完全抵消，剩余常数恰为

\[
(9T+2a_3)^2-T(18a_3+55T)
=2\mathscr R_{23}.
\]

等价地，\(\widehat{\mathcal T}_2\) 关于 \(K\) 的完整判别式为

\[
\boxed{
\operatorname{disc}_K(\widehat{\mathcal T}_2)
=
\left(2^{m+1}c_ug\right)^2\mathscr C_{23}.
}
\tag{16.324}
\]

因此若 \(p\mid\widehat{\mathcal T}_2\)，(16.323) 自动给出
\[
\mathscr C_{23}
\equiv
\left[c_ug(TK-9T-2a_3)\right]^2
\pmod p.
\tag{16.325}
\]

特别地，当 \(p\mid Q_0\) 时，(16.322) 的第二项消失，
(16.325) 正好退化成 (16.316)；\(f\)-channel 的 (16.320) 也是同一
二次多项式在模 \(f\) 下换用 (16.299) 后的判别式投影。

这给出必须保留的逻辑边界：

- 判别数 \(-23\) 的 form 确实是新的显式算术对象；
- 但仅由“\(p\) 整除相应二次式”推出其判别式为平方，是
  (16.323) 的 principal-square shadow，不能单独计作第二个
  obstruction；
- 真正可能闭环的输入必须独立地固定
  \((\mathscr C_{23}/p)\)、\((\mathscr R_{23}/p)\) 或
  \((\mathscr R_{23,f}/p)\) 的相反 character，例如来自 source
  Gaussian allocation 或 prefix defect，而不是再次使用同一个
  quadratic root。

同时 (16.323) 给出严格正 gap
\[
0<\mathscr C_{23}
<
\left[c_ug(TK-9T-2a_3)\right]^2,
\]
但当前没有证明 \(\mathscr C_{23}\) 本身为平方，所以它还不是相邻平方
矛盾。下一步应研究 \(\mathscr C_{23}\) 的独立 norm/source
表示；若无法得到，curvature-discriminant 路线必须继续降级。

### 16.52 `已严格完成 / 审计`：companion 是 \(-23\) norm 加深五进 Gaussian norm

(16.322) 的 companion 还有一个跨二次域的精确分解。由
\(\lambda=m-d\)，第二项的五进指数化为

\[
m+2\lambda-d=3\lambda.
\]

另一方面令

\[
U_{23}:=c_ug\left(2a_3+\frac{9T}{2}\right),
\qquad
V_{23}:=c_ug\frac{T}{2}.
\]

则 (16.315) 直接给出

\[
\boxed{
\mathscr C_{23}
=
U_{23}^2+23V_{23}^2
+5^{3\lambda}Q_0^2XY.
}
\tag{16.326}
\]

第一部分是 \(\mathbf Q(\sqrt{-23})\) 的整数 norm，第二部分则是
深五进倍数乘以 Gaussian norm \(XY\)。这说明 companion 确实连接了
\(-23\) 与 \(-1\) 两个二次域，但“两个不同域的 norm 之和”并不自动
是任一域的 norm。

其容易取得的局部信息仍全部退化为 principal square。reflection 中
\[
\nu_5=3\lambda-2m\ge0,
\]
所以 \(3\lambda\ge2m\)；又 \(v_5(V_{23})=m\)。因此

\[
\boxed{
\mathscr C_{23}\equiv U_{23}^2\pmod{5^{2m}}.
}
\tag{16.327}
\]

在二进端，\(4\mid g\)，而
\(N_0\equiv a_2^2\equiv1\pmod8\)。由
\(N_0=5^{\nu_5}XY\) 与
\(3\lambda+\nu_5=6\lambda-2m\) 为偶数，得到

\[
\boxed{
\mathscr C_{23}\equiv1\pmod8.
}
\tag{16.328}
\]

故 \(\mathscr C_{23}\) 在 \(\mathbf Z_2\) 中为平方，并在
\(\mathbf Z_5\) 中至少贴近平方到深度 \(2m\)。这排除了“只用
\(2,5\)-进局部非平方关闭 (16.323)”的路线。若 companion 能产生
矛盾，只能来自某个 odd prime 的独立 \(-23\)/Gaussian orientation，
或来自 (16.323) 的 Archimedean 相邻平方控制。

### 16.53 `已严格完成`：companion 与 canonical square 产生两个正的 shifted factors

令 core §12.8 的 canonical square 写成

\[
\mathcal A^2-Z^2
=
5^\lambda Q_0N_0(5^\lambda Q_0+2c).
\tag{16.329}
\]

这里必须恢复 core §13 在“去掉共同五进部分”中省略的 content。
由
\[
v_5\!\left((\mathcal A-Z)(\mathcal A+Z)\right)
=\lambda+\nu_5=2(\lambda-d),
\]
而
\[
v_5(2\mathcal A)=\lambda+1>\lambda-d,
\]
两因子的 \(5\)-进赋值不能不同，故必各等于 \(\lambda-d\)。结合
square-side allocation，精确式是

\[
\boxed{
\mathcal A-Z=5^{\lambda-d}fc_-^2X,
\qquad
\mathcal A+Z=5^{\lambda-d}qc_+^2Y.
}
\tag{16.329a}
\]

在 reflection 中
\[
u=c_u\rho,\qquad g=2^{t-1}\rho,\qquad K=10P,
\]
所以

\[
\boxed{
5^d\mathcal A=Tc_ugK.
}
\tag{16.330}
\]

定义

\[
\mathscr E_{23}:=c_ug(9T+2a_3),
\qquad
\mathscr W_{23}:=c_ug(TK-9T-2a_3).
\]

于是

\[
\mathscr W_{23}=5^d\mathcal A-\mathscr E_{23}.
\tag{16.331}
\]

因此有精确 shifted factorization

\[
\boxed{
\begin{aligned}
\mathscr V_-
&:=\mathscr W_{23}-5^dZ
=5^\lambda fc_-^2X-\mathscr E_{23},\\
\mathscr V_+
&:=\mathscr W_{23}+5^dZ
=5^\lambda qc_+^2Y-\mathscr E_{23}.
\end{aligned}
}
\tag{16.332}
\]

两因子的正性并非假设。先对 \(\mathscr V_-\) 证明。由
\[
c_-^2X=D J_{\rm def},\qquad
J_{\rm def}>3-\frac3{250}=\frac{747}{250},
\]
以及 \(\lambda+d=m\)，有
\[
\mathscr V_-
=gT\left\{
fJ_{\rm def}
-c_u\left(9+\frac{2a_3}{T}\right)
\right\}.
\]
故结合 \(a_3<251T/250\)，只需比较 \(f/c_u\)。
而
\[
f>5^\lambda q>\frac{5^{M+\lambda}}{c_Q},
\qquad
c_Qc_u<\frac{5^\lambda}{2^{M+1}}
\]
分别来自 \(Q_0=c_Qq>5^M\) 与 \(w<1\)。故

\[
\boxed{
\frac{f}{c_u}
>
2^{M+1}5^M
\ge2^{12}5^{11}.
}
\tag{16.333}
\]

这里仅用了 \(M\ge11\)。另一方面
\[
\frac{9T+2a_3}{T}<\frac{1376}{125}.
\]
结合 \(747/250\cdot2^{12}5^{11}>1376/125\)，严格得到

\[
\boxed{\mathscr V_->0.}
\tag{16.334}
\]

又 \(Z>0\)，所以 \(\mathscr V_+>\mathscr V_->0\)。因此

\[
\boxed{
0<\mathscr V_-<\mathscr V_+,\qquad
\mathscr V_-\mathscr V_+
=\mathscr W_{23}^2-5^{2d}Z^2.
}
\tag{16.335}
\]

这两个 shifted factors 还是奇 \(5\)-进单位。因为
\(4\mid g\)，\(\mathscr W_{23}\) 被 \(4\) 整除，而 \(Z\) 为奇数；
又模 \(5\) 时
\[
\mathscr W_{23}\equiv-2c_uga_3\not\equiv0\pmod5.
\]
并且对任意 \(p\mid c_ug\)，(16.294)、source split 与
\(f=g\omega+c_u\) 表明 (16.332) 的第一项在模 \(p\) 下为单位。
故

\[
\boxed{
\gcd(\mathscr V_-\mathscr V_+,10c_ug)=1.
}
\tag{16.336}
\]

(16.332) 是此前缺少的显式 factor-allocation 接口：同一个短移位
\(\mathscr E_{23}\) 分别作用于 \(f c_-^2X\) 与 \(q c_+^2Y\)，而不再
只看抽象判别式。不过它尚未自行矛盾；下一步必须控制
\(\gcd(\mathscr V_-,\mathscr V_+)\) 或证明其中的
\(3\bmod4\) 因子与 \(c_-/c_+\) Gaussian orientation 不相容。

### 16.54 `已严格完成`：shifted factors 的 denominator 接触压成一个第三块线性整数

把共同短移位写成

\[
\mathscr E_{23}=2c_ug\mathscr L_{23},
\qquad
\boxed{
\mathscr L_{23}:=\frac{9T}{2}+a_3.
}
\tag{16.337}
\]

由于 \(a_3\) 为奇 \(5\)-进单位、\(m\ge2\)，
\(\mathscr L_{23}\) 是奇 \(5\)-进单位，并且

\[
\boxed{
\frac{11}{2}T
<
\mathscr L_{23}
<
\frac{688}{125}T,
\qquad
\gcd(\mathscr L_{23},10)=1.
}
\tag{16.338}
\]

现在 (16.332) 在各自的 denominator factor 下直接退化。因为
\(\gcd(f,2c_ug)=1\) 与 \(\gcd(q,2c_ug)=1\)，有

\[
\boxed{
\gcd(\mathscr V_-,f)
=
\gcd(\mathscr L_{23},f),
\qquad
\gcd(\mathscr V_+,q)
=
\gcd(\mathscr L_{23},q).
}
\tag{16.339}
\]

所以 shifted factor 与 \(q,f\) 的同侧接触不再依赖大二次式
\(\mathscr S_0,\mathscr R_f\)，而完全由长度约 \(5.5T\) 的第三块
线性整数 \(\mathscr L_{23}\) 控制。

两 shifted factors 的共同部分也有精确描述。由
\[
\mathscr V_+-\mathscr V_-=2\cdot5^dZ,
\qquad
\mathscr V_++\mathscr V_-=2\mathscr W_{23},
\]
再用 (16.336) 排除 \(2,5,c_ug\)，得到

\[
\boxed{
\gcd(\mathscr V_-,\mathscr V_+)
=
\gcd(\mathscr W_{23},Z)
=
\gcd(TK-9T-2a_3,Z).
}
\tag{16.340}
\]

最后一式中 \(\gcd(Z,c_ug)=1\)：若 \(p\mid c_ugZ\)，则
\(\mathscr W_{23}\equiv0\pmod p\) 会使
\(\mathscr V_\pm\equiv0\pmod p\)，与 (16.336) 矛盾。

因此新的 factor pair 只剩两个明确的 gcd kernel：

1. 同侧 denominator kernel
   \(\gcd(\mathscr L_{23},qf)\)；
2. 两侧共同 kernel
   \(\gcd(TK-9T-2a_3,Z)\)。

若能证明二者都只含 \(1\bmod4\) 素数（或其中 \(3\bmod4\) 赋值为
偶数），则 (16.335) 的 \(3\bmod4\) factor 必须落在单侧
Gaussian allocation 上，可继续与 \(c_-^2X/c_+^2Y\) 对撞。
当前尚未证明这两个 gcd 的 inert part 为空。

### 16.55 `已严格完成`：共同 kernel 消去 canonical square root

(16.340) 的第二个 kernel 仍含平方根 \(Z\)，但可以把它消去而不做
有限枚举。定义

\[
\boxed{
\mathscr D_Z
:=
\mathscr E_{23}^2
-5^{m+d}Q_0N_0(5^\lambda Q_0+2c).
}
\tag{16.341}
\]

由 canonical difference of squares
\[
\mathcal A^2-Z^2
=5^\lambda Q_0N_0(5^\lambda Q_0+2c)
\]
和 \(\mathscr E_{23}=5^d\mathcal A-\mathscr W_{23}\)，直接得到

\[
\boxed{
\mathscr D_Z
=
5^{2d}Z^2
-\mathscr W_{23}
\left(\mathscr E_{23}+5^d\mathcal A\right).
}
\tag{16.342}
\]

因此若奇素数 \(p^e\Vert\mathscr W_{23}\)，则

\[
\boxed{
\min\{v_p(\mathscr D_Z),e\}
=
\min\{2v_p(Z),e\}.
}
\tag{16.343}
\]

这里 \(p\ne5\)，因为
\(\mathscr W_{23}=c_ug(TK-9T-2a_3)\) 的最后一因子为奇
\(5\)-进单位。特别地，

\[
\boxed{
p\mid\gcd(\mathscr W_{23},Z)
\iff
p\mid\gcd(\mathscr W_{23},\mathscr D_Z).
}
\tag{16.344}
\]

所以 (16.340) 的共同因子支持完全等价于两个显式整数
\[
TK-9T-2a_3,
\qquad
\mathscr D_Z
\]
的 gcd；canonical square root 已被消去。式 (16.343) 还说明共同
接触在未饱和层总以 \(Z\)-侧偶赋值进入，真正可能产生 odd inert
excess 的只能是 \(\mathscr W_{23}\)-饱和层。下一步应证明该饱和层
与 (16.101) 的小 \(C\) 代表不相容，或给出
\(\gcd(TK-9T-2a_3,\mathscr D_Z)\) 的固定 resultant 上界。

### 16.56 `已严格完成`：共同-kernel 的全部 denominator 接触自动是平方深度

(16.341) 在 \(qf\) 上还能完全化简。因为

\[
Q_0=c_Qq,\qquad
5^\lambda Q_0+2c=c_Qf,
\]

有

\[
\boxed{
\mathscr D_Z
=
\mathscr E_{23}^2
-5^{m+d}c_Q^2qfN_0.
}
\tag{16.345}
\]

又 \(\gcd(q,f)=1\) 且
\(\gcd(2c_ug,qf)=1\)，所以模 \(qf\) 时

\[
\mathscr D_Z
\equiv
\mathscr E_{23}^2
\equiv
(2c_ug)^2\mathscr L_{23}^2
\pmod{qf}.
\]

因此得到精确 gcd 与逐素数赋值律

\[
\boxed{
\gcd(\mathscr D_Z,qf)
=
\gcd(\mathscr L_{23}^2,qf),
}
\tag{16.346}
\]

\[
\boxed{
p^e\Vert qf
\Longrightarrow
\min\{v_p(\mathscr D_Z),e\}
=
\min\{2v_p(\mathscr L_{23}),e\}.
}
\tag{16.347}
\]

这说明 (16.339) 的 denominator contact 与 (16.344) 的共同-factor
kernel 并非两套独立现象：在 \(qf\) 的所有未饱和层，
\(\mathscr D_Z\) 的接触赋值严格为偶数。故 denominator prime 若要
承担 odd inert excess，只能满足

\[
\boxed{
p^e\Vert qf,\qquad
p^e\mid\mathscr L_{23},
}
\tag{16.348}
\]

即完整 denominator prime power 已在长度约 \(5.5T\) 的第三块线性
整数中饱和。当前缺口因而从一般 prime contact 缩成 saturation：
需要证明 \(q\) 或 \(f\) 的任何 \(3\bmod4\) 完整素数幂都不能整除
\(\mathscr L_{23}\)，或证明饱和后 (16.332) 的剩余赋值仍为偶数。
有限检查固定 \(m,M\) 不能替代这一无界 prime-power 命题。

### 16.57 `已严格完成`：模 \(4\) 把 inert carrier 分成固定 \(3\) 与 denominator \(q\)

source split 在模 \(4\) 下先给出一个此前未显式记录的定向。因为
\[
Q_0=c_Qq=5^M+2^mgc_u\equiv1\pmod4,
\qquad
c_Q\equiv3\pmod4,
\]
所以

\[
\boxed{
q\equiv3\pmod4,
\qquad
f=5^\lambda q+2c_u\equiv1\pmod4.
}
\tag{16.349}
\]

另一方面 \(\mathcal A\equiv0\pmod4\)、\(Z\) 为奇数，故由
(16.329)

\[
5^{\lambda-d}fc_-^2X=\mathcal A-Z\equiv-Z\pmod4,
\qquad
5^{\lambda-d}qc_+^2Y=\mathcal A+Z\equiv Z\pmod4.
\]

代入 (16.349)，得到

\[
\boxed{
X\equiv Y\equiv-Z\pmod4.
}
\tag{16.350}
\]

这也与 \(XY=N(\mathcal A_5)\equiv1\pmod4\) 一致。由
(16.50)、(16.60)，\(XY\) 中除固定素数 \(3\) 外没有
\(3\bmod4\) 素因子，所以 (16.350) 给出严格二分：

\[
\boxed{
\begin{array}{ll}
Z\equiv1\pmod4
&\Longrightarrow
v_3(X)\equiv v_3(Y)\equiv1\pmod2,\\[1mm]
Z\equiv3\pmod4
&\Longrightarrow
v_3(X)\equiv v_3(Y)\equiv0\pmod2.
\end{array}
}
\tag{16.351}
\]

同时 \(\mathscr E_{23}\equiv0\pmod4\)，所以 (16.332) 给出
\[
\mathscr V_-\equiv-Z,\qquad
\mathscr V_+\equiv Z\pmod4.
\]
因此：

1. \(Z\equiv1\pmod4\) 时，\(3\bmod4\) shifted factor 是
   \(\mathscr V_-\)，而基础 Gaussian factors \(X,Y\) 都由固定
   素数 \(3\) 承担奇 parity；
2. \(Z\equiv3\pmod4\) 时，\(3\bmod4\) shifted factor 是
   \(\mathscr V_+\)，\(X,Y\) 的 inert parity 都为偶数，基础
   \(3\bmod4\) 载体只能来自 \(q\equiv3\pmod4\)。

这把 §16.47 的固定 \(3\) 通道与 §16.56 的 denominator saturation
通道分成了两个全局 orientation，而非任意混合。剩余闭环也相应分成：
排除 \(Z\equiv1\) 时 \(3\) 在 \(X,Y\) 两侧同时为奇的 balanced
transfer；以及排除 \(Z\equiv3\) 时 \(q\) 的 inert primary part
在 \(\mathscr L_{23}\) 中饱和。

### 16.58 `已严格完成`：\(Z\equiv1\) 时固定 \(3\) 不能承担 additive-cofactor excess

§16.12 定义
\[
\delta:=v_3(X)\bmod2
\]
并证明
\[
v_3(X)\equiv v_3(Y)\equiv v_3(k_h)\pmod2.
\]
与 (16.351) 合并，得到

\[
\boxed{
\delta=1\iff Z\equiv1\pmod4,
\qquad
\delta=0\iff Z\equiv3\pmod4.
}
\tag{16.352}
\]

若 \(Z\equiv1\pmod4\)，则 \(\delta=1\)，故
\(e_3=v_3(k_h)\) 为奇数。§16.11 的完整分类随即适用：

\[
\boxed{
\begin{cases}
v_3(a_3)=1,\quad v_3(a_2)\ge2,\\
\text{或}\\
v_3(a_2)=1,\quad v_3(a_3)\ge2,
\end{cases}
\qquad
v_3(\beta)=0.
}
\tag{16.353}
\]

特别地 \(3\mid a_2\)。但 §16.47 已证明
\[
3\mid a_2
\Longrightarrow
3\nmid\widehat{\mathcal T}_2.
\]
所以

\[
\boxed{
Z\equiv1\pmod4
\Longrightarrow
3\nmid\widehat{\mathcal T}_2.
}
\tag{16.354}
\]

这消除了一个潜在混淆：在 \(Z\equiv1\) orientation 中，固定素数
\(3\) 确实同时以奇 parity 出现在 \(X,Y,k_h\) 中，但它**不能**
同时承担 §16.44 的 additive-cofactor odd inert excess。后者必由
某个 \(\ell\ne3\) 承担，因而必须进入
§16.45–16.46 的显式 denominator contact，或进入真正的
endpoint-external/source 通道。

在 \(Z\equiv3\pmod4\) orientation 中，\(\delta=0\)，基础
Gaussian factors 的 inert parity 为偶，而 \(q\equiv3\pmod4\)
承担 denominator carrier；固定 \(3\) 是否另外整除
\(\widehat{\mathcal T}_2\) 仍由 (16.310)–(16.313) 判定。

### 16.59 `已严格完成`：\(Z\equiv1\) orientation 的 shifted pair 恰共享一份 \(3\)

继续设 \(Z\equiv1\pmod4\)。由 (16.353)，\(a_2,a_3\) 都被 \(3\)
整除，且恰有一个的 \(3\)-进赋值为 \(1\)。由于
\[
P=9\cdot10^{M-1}+a_2,\qquad K=10P,
\]
逐两种通道检查可得

\[
\boxed{
v_3(TK-9T-2a_3)=1.
}
\tag{16.355}
\]

事实上，若 \(v_3(a_3)=1\)，前两项至少被 \(9\) 整除而最后一项
恰含一个 \(3\)；若 \(v_3(a_2)=1\)，则 \(v_3(K)=1\)，其余两项
至少被 \(9\) 整除。

另一方面 \(C_0\) 被 \(9\) 整除，故 \(3\mid a_2\) 推出
\(9\mid N_0\)；同时 \(3\mid K\)。由 (16.279) 有
\(9\mid K_0\)，再代入 canonical square (16.283)，得到

\[
\boxed{3\mid Z.}
\tag{16.356}
\]

§16.11 还给出 \(3\nmid c_ug\)。所以 (16.355)–(16.356) 与
(16.340) 合并后，

\[
\boxed{
v_3\!\left(\gcd(\mathscr V_-,\mathscr V_+)\right)=1.
}
\tag{16.357}
\]

也就是说 shifted pair 恰共享一份普通 Gaussian inert factor \(3\)，
不多不少。定义
\[
\mathscr V_-^{(3)}:=\frac{\mathscr V_-}{3},
\qquad
\mathscr V_+^{(3)}:=\frac{\mathscr V_+}{3}.
\]
则

\[
\boxed{
3\nmid\gcd(\mathscr V_-^{(3)},\mathscr V_+^{(3)}),
\qquad
\mathscr V_-^{(3)}\equiv1,\quad
\mathscr V_+^{(3)}\equiv3\pmod4.
}
\tag{16.358}
\]

所以 §16.12 的“平衡转移一份 \(3\)”在新的 canonical shifted
factorization 中有完全对应：约去唯一公共 \(3\) 后，
\(3\bmod4\) orientation 固定转移到 plus side。尚缺的是排除
\(\mathscr V_+^{(3)}\) 中可能残留的额外 \(3\)-primary depth，或把
其非 \(3\) inert prime 强制送入 (16.339)/(16.348) 的 denominator
saturation。

### 16.60 `已严格完成`：denominator saturation 等价于两个显式 source/digit Hensel targets

§16.56 剩下的条件是某个完整 prime power
\(p^e\Vert qf\) 整除 \(\mathscr L_{23}\)。它还能按 \(q/f\) 两侧
分别消去 denominator 变量。

先设 \(p^e\mid q\) 且 \(p^e\mid\mathscr L_{23}\)。由

\[
c_Qq=5^M+2^mgc_u,
\qquad
2\mathscr L_{23}=9T+2a_3,
\]

分别得到
\[
2^mgc_u\equiv-5^M,
\qquad
2a_3\equiv-9\cdot2^m5^m
\pmod{p^e}.
\]
相乘消去 \(2^m\)：

\[
\boxed{
p^e\mid q,\ p^e\mid\mathscr L_{23}
\Longrightarrow
p^e\mid
\left(2a_3gc_u-9\cdot5^{M+m}\right).
}
\tag{16.359}
\]

再设 \(p^e\mid f\) 且 \(p^e\mid\mathscr L_{23}\)。由
\[
c_Qf=5^\lambda Q_0+2c
=5^{M+\lambda}+2^m5^\lambda gc_u+2c
\]
并乘以 \(9\cdot5^d\)，使用
\(\lambda+d=m\) 与
\(9T\equiv-2a_3\pmod{p^e}\)，得到

\[
\boxed{
p^e\mid f,\ p^e\mid\mathscr L_{23}
\Longrightarrow
p^e\mid
\left(
2a_3gc_u
-9\cdot5^{M+m}
-18c5^d
\right).
}
\tag{16.360}
\]

因此定义两个整数

\[
\boxed{
\mathscr H_q:=2a_3gc_u-9\cdot5^{M+m},
\qquad
\mathscr H_f:=\mathscr H_q-18c5^d,
}
\tag{16.361}
\]

则所有非 \(3\) denominator odd-excess 候选已压成

\[
\boxed{
p^e\Vert q,\ p^e\mid\mathscr H_q
\quad\text{或}\quad
p^e\Vert f,\ p^e\mid\mathscr H_f.
}
\tag{16.362}
\]

这两条是完整 prime-power Hensel targets，不是仅模 \(p\) 的
character。它们的差固定为
\[
\mathscr H_q-\mathscr H_f=18c5^d.
\]
对不整除 \(3c\) 的 inert prime，两 target 不可能同时接触；这与
\(\gcd(q,f)=1\) 一致。剩余任务是利用
\(5^{M-1}+H=4c_u2^mg\) 和 \(C\) 的自然代表把
\(\gcd(q,\mathscr H_q)\)、\(\gcd(f,\mathscr H_f)\) 压到
不含完整 \(3\bmod4\) prime power。当前还没有这样的全局 gcd 上界。

### 16.61 `已严格完成`：Hensel targets 接回真实 denominator 缺口 \(H\)

(16.361) 仍含 \(g c_u\)，但 §12 的真实 denominator defect 给出

\[
4c_u2^mg=5^{M-1}+H.
\]

乘以 \(2^{m+1}\) 后，两个 target 精确化为

\[
\boxed{
\begin{aligned}
\mathscr G_q
&:=2^{m+1}\mathscr H_q
=5^{M-1}(a_3-90T)+a_3H,\\
\mathscr G_f
&:=2^{m+1}\mathscr H_f
=\mathscr G_q-18\cdot2^{m+1}c5^d.
\end{aligned}
}
\tag{16.363}
\]

因为 \(p\) 为奇素数，(16.362) 完全等价于

\[
\boxed{
p^e\Vert q,\ p^e\mid\mathscr G_q
\quad\text{或}\quad
p^e\Vert f,\ p^e\mid\mathscr G_f.
}
\tag{16.364}
\]

这已把 saturation 接回真实小缺口 \(H\)，没有新增自由变量。其
Archimedean 位置也被固定。由
\[
1<\frac{a_3}{T}<\frac{251}{250},
\qquad
0<\frac{H}{5^{M-1}}<\frac1{19},
\]
得到

\[
\boxed{
\frac{42248}{475}
<
\frac{-\mathscr G_q}{5^{M-1}T}
<
89.
}
\tag{16.365}
\]

而由
\[
w=\frac{2^{M+1}c}{5^\lambda}
\]
可把两 target 的差写成

\[
\boxed{
\frac{\mathscr G_q-\mathscr G_f}{5^{M-1}T}
=
\frac{18w}{2^M5^{M-1}}.
}
\tag{16.366}
\]

所以 \(\mathscr G_q,\mathscr G_f\) 都是负整数，位于同一个宽度小于
\(1/10\) 的固定 significand band，并且二者相对距离随 \(M\)
指数消失。这个结果排除了把 saturation target 当作小余数的希望：
它们的高度约为 \(89\cdot5^{M-1}T\)。下一步需要的是
\(p\)-进/decimal resultant，而非 Archimedean “模数大于 target”
论证。

### 16.62 `已严格完成`：\(q\)-saturation 在 rational-root 四次式中产生二倍 prime-power 深度

考虑 (16.364) 的 \(q\)-channel，并令非 \(3\) inert prime 满足
\[
p^e\Vert q,\qquad p^e\mid\mathscr L_{23}.
\]
写
\[
N:=DJ_{\rm def}=3D-C=c_-^2X.
\]
因为 \(p\mid q\) 而 \(\gcd(q,10c_ug)=1\)，\(D,b_2,T\) 都是
\(p\)-进单位；又 \(p\ne3\) 时 \(p\nmid N_0\)，否则
\(p\mid C_0^2+a_2^2\) 会迫使 \(p\mid C_0,a_2\)，与 (16.60) 的
Gaussian 本原性矛盾。

把 rational-root 方程 \(F(J_{\rm def})=0\) 清去 \(D\) 的单位，
并使用 \(p^e\mid Q\)，得到

\[
\boxed{
v_p(N)
+v_p(TN+2a_3D)
+2v_p(KD-N)
\ge2e.
}
\tag{16.367}
\]

而 saturation 给出
\[
2a_3\equiv-9T\pmod{p^e},
\]
所以在深度 \(e\) 内第二因子就是
\[
TN+2a_3D\equiv T(N-9D)\pmod{p^e}.
\tag{16.368}
\]

三个实际因子
\[
N,\qquad TN+2a_3D,\qquad KD-N
\]
在模 \(p\) 下两两同时为零时，分别会迫使
\(p\mid2a_3\)、\(p\mid K\)、\(p\mid K-9\)。saturation 已给出
\(2a_3\equiv-9T\not\equiv0\pmod p\)。因此若
\[
p\nmid K(K-9),
\]
则其中至多一个被 \(p\) 整除，(16.367) 强迫严格三分：

\[
\boxed{
\begin{array}{ll}
p\mid N
&\Longrightarrow p^{2e}\mid N,\\[1mm]
p\mid TN+2a_3D
&\Longrightarrow p^{2e}\mid TN+2a_3D,\\[1mm]
p\mid KD-N
&\Longrightarrow p^e\mid KD-N.
\end{array}
}
\tag{16.369}
\]

若再有 \(p\nmid c_Q\)，则 \(p\nmid c_-X=N\)，第一行自动排除。
所以 generic \(q\)-saturation 只剩

\[
\boxed{
\begin{aligned}
p^e&\mid(6D+C),\\
p^{2e}&\mid\bigl(D(3T+2a_3)-TC\bigr),
\end{aligned}
\quad\text{或}\quad
p^e\mid((K-3)D+C),
}
\tag{16.370}
\]

外加 \(p\mid c_QK(K-9)\) 的显式 overlap/exceptional 通道。
这里第一支获得了相对于 denominator prime power 的**二倍深度**；
它是新的 Hensel amplification，而非模 \(p\) character。尚需用
\(0<C<3D/250\) 与 \(D=g2^m5^d\) 对 (16.370) 作无界高度排除；
当前单凭相对大小仍不足，因为 \(p^e\) 可以是 \(q\) 的小 primary
factor。

### 16.63 `已严格完成`：三分支的精确赋值与 middle branch 的高阶 quotient kernel

(16.367) 实际上来自一个整数等式，而不只是单向整除。设

\[
a_p:=v_p(c_Q),\qquad n_p:=v_p(c_Qq)=a_p+e.
\tag{16.371}
\]

由于 \(Q=2^{M+1}c_Qq\)，有 \(v_p(Q)=n_p\)。在当前非 \(3\)
inert channel，\(b_2,T,D,N_0\) 都是 \(p\)-进单位；特别地，
把 (7.1) 在 \(J=N/D\) 处清分母后，左右两边的赋值给出精确预算

\[
\begin{aligned}
&v_p(N)+v_p(TN+2a_3D)+2v_p(KD-N)\\
&\qquad=2n_p+2v_p(TN+a_3D).
\end{aligned}
\tag{16.372}
\]

这使 (16.369) 的三支分别得到更强结论。

首先若 \(p\mid N\)，则 saturation 给出

\[
TN+2a_3D\equiv-9TD\not\equiv0,\qquad
TN+a_3D\equiv-\frac92TD\not\equiv0\pmod p.
\]

若再有 \(p\nmid K\)，则 \(KD-N\) 也是单位，所以 (16.372) 强迫
\(v_p(N)=2n_p\)。但 \(N=c_-^2X\)，而非 \(3\) inert prime
不能整除 \(X\)；若 \(p\mid N\)，完整 square-side allocation 又给出
\(v_p(N)=2a_p\)。这与 \(n_p=a_p+e\)、\(e>0\) 矛盾。因此

\[
\boxed{p\mid N\quad\Longrightarrow\quad p\mid K.}
\tag{16.373}
\]

也就是说初步分流中的 \(c_Q\)-overlap 本身还不够；第一支只能进入
更窄的 \(c_Q\)-且-\(K\) overlap。

其次考虑 (16.370) 的 middle branch，并假设 \(p\nmid K-9\)。此时

\[
N\equiv9D,\qquad
TN+a_3D\equiv\frac92TD,\qquad
KD-N\equiv(K-9)D
\pmod p,
\]

三者都是单位。因此 (16.372) 不仅给出下界，而给出精确深度

\[
\boxed{
v_p\!\left(D(3T+2a_3)-TC\right)=2n_p=2(a_p+e).
}
\tag{16.374}
\]

把这条深度写成规范 Hensel 商。由 saturation 与 middle branch，
以下两个数都是正整数：

\[
s_p:=\frac{2a_3+9T}{p^e},
\qquad
r_p:=\frac{6D+C}{p^e}.
\tag{16.375}
\]

而恒等式

\[
D(3T+2a_3)-TC
=p^e(Ds_p-Tr_p)
\tag{16.376}
\]

与 \(D=g2^m5^d\)、\(T=2^m5^m\)、\(\lambda=m-d\) 给出

\[
\boxed{
v_p\!\left(gs_p-5^\lambda r_p\right)
=e+2a_p.
}
\tag{16.377}
\]

这里是**精确赋值**，不是只有模 \(p^e\) 的同余。特别地，当
\(p\mid c_Q\) 时，每一份 \(c_Q\)-overlap 都在二阶商中额外贡献
两层深度；先前把它仅列作“例外”会丢失这部分信息。

最后，若 \(p\mid KD-N\)，并且

\[
p\nmid K(K-9)(2K-9),
\]

则 \(N\)、\(TN+2a_3D\)、\(TN+a_3D\) 都是单位；(16.372) 给出

\[
\boxed{v_p(KD-N)=n_p=a_p+e.}
\tag{16.378}
\]

故 third branch 同样必须吸收整个 \(c_Qq\) 的 \(p\)-primary
深度，而不只是 \(q\) 中的 \(p^e\)。当前尚未排除 (16.377)、
(16.378) 以及 \(p\mid K(K-9)(2K-9)\) 的结构例外；但
\(q\)-saturation 已从粗略的三条 lower bound 提升成精确的
prime-power budget，下一步可以对这些显式线性因子作 resultant，
而不再猜测额外赋值来自何处。

### 16.64 `已严格完成`：精确赋值预算固定三个 residual unit character

精确预算还能在除去全部 \(p\)-幂后保留一条新的单位层信息。这里使用
清分母后的完整等式

\[
\boxed{
b_2^2TN(TN+2a_3D)(KD-N)^2
=Q^2N_0D^2(TN+a_3D)^2.
}
\tag{16.379}
\]

它与 (16.372) 相比没有丢掉剩余单位的平方类。

在第一支中，(16.373) 已知 \(p\mid K\)。此时 (16.372) 还精确给出

\[
v_p(N)=2a_p,\qquad v_p(KD-N)=e.
\tag{16.380}
\]

把 (16.379) 除去两边的 \(p^{2n_p}\)，再模 \(p\) 取 Legendre
character。因为

\[
\frac{N}{p^{2a_p}}\equiv(\text{square})X,\qquad
TN+2a_3D\equiv-9TD,\qquad
N_0=5^{\nu_5}XY,
\]

所有显式平方消去后得到

\[
\boxed{
\left(\frac{-D}{p}\right)
=\left(\frac{5^{\nu_5}Y}{p}\right)
\qquad(p\mid N,\ p\mid K).
}
\tag{16.381}
\]

在 middle branch，记

\[
\overline M_p
:=\frac{D(3T+2a_3)-TC}{p^{2n_p}}.
\tag{16.382}
\]

由 (16.374)，它是 \(p\)-进单位。又

\[
N\equiv9D,\qquad KD-N\equiv(K-9)D\pmod p.
\]

在 (16.379) 中消去平方后有

\[
\left(\frac{TD\,\overline M_p}{p}\right)
=\left(\frac{N_0}{p}\right).
\]

利用 \(N_0=5^{\nu_5}XY\)、
\(TD=g2^{2m}5^{m+d}\) 与
\(\nu_5=m-3d\)，所有 \(5\)-幂之差为 \(-4d\)，从而

\[
\boxed{
\left(\frac{\overline M_p}{p}\right)
=\left(\frac{gXY}{p}\right).
}
\tag{16.383}
\]

这条 character 读取的是除去完整 \(p^{2(a_p+e)}\) 后的真正
Hensel leading unit；它不等同于此前只看未归一化 middle factor
的模 \(p\) 条件。

最后在 third branch 的 generic 条件
\(p\nmid K(K-9)(2K-9)\) 下，(16.378) 允许把
\((KD-N)/p^{n_p}\) 的平方完全约掉。由

\[
N\equiv KD,\qquad
TN+2a_3D\equiv TD(K-9)\pmod p
\]

得到

\[
\boxed{
\left(\frac{K(K-9)}p\right)
=\left(\frac{5^{\nu_5}XY}p\right).
}
\tag{16.384}
\]

所以 \(q\)-saturation 的三个残余对象现已全部固定：第一支只能在
\(c_Q\)-且-\(K\) overlap 中满足 (16.381)，middle branch 必须满足
精确 quotient character (16.383)，third branch 必须满足
(16.384)。这些仍是必要条件而不是空性结论；但后续 reciprocity
比较必须作用在这些**约尽完整 prime power 的 leading units**上，
不能再把未正规化因子当成独立 character。

### 16.65 `已严格完成`：carrier 条件把所有 generic 例外压到固定素数 \(11,23\)

若上述 saturation prime 真正来自 \(q\)-侧 additive cofactor，
§16.46 还给出 \(p\mid\mathscr S_0\)。这一条件与
\(p^e\mid\mathscr L_{23}\) 之间有一个此前未使用的精确 resultant。
把

\[
u_{23}:=2a_3+9T=2\mathscr L_{23}
\]

代入 (16.288) 中

\[
\mathscr S_0
=TK^2-(18T+4a_3)K+18a_3+55T,
\]

直接得到

\[
\boxed{
\mathscr S_0
=T(K^2-26)-(2K-9)u_{23}.
}
\tag{16.385}
\]

因此对 \(p^e\mid\mathscr L_{23}\) 有完整 prime-power 同余

\[
\boxed{
\mathscr S_0\equiv T(K^2-26)\pmod{p^e}.
}
\tag{16.386}
\]

特别地，只要 \(p\mid\mathscr S_0\)，由于 \(p\nmid T\)，就必须
满足

\[
\boxed{
K^2\equiv26\pmod p,\qquad
\left(\frac{26}{p}\right)=1.
}
\tag{16.387}
\]

这条二次剩余条件不是额外假设，而是 denominator saturation 与
additive-cofactor contact 的一次显式 resultant。它立即清理
§16.63 的结构例外：

\[
\begin{array}{rcll}
p\mid K
&\Longrightarrow&p\mid26,&\text{不可能，因为 }p\equiv3\pmod4,\ p\ne2,13;\\
p\mid K-9
&\Longrightarrow&p\mid(9^2-26)=55,&\text{故只能 }p=11;\\
p\mid2K-9
&\Longrightarrow&p\mid(9^2-4\cdot26)=-23,&\text{故只能 }p=23.
\end{array}
\tag{16.388}
\]

于是第一 valuation branch 对真正的非 \(3\) \(q\)-carrier **完全
消失**：由 (16.373) 它需要 \(p\mid K\)，而 (16.387) 排除这一点。
其余两支变为

\[
\boxed{
\begin{array}{ll}
\text{middle:}&
v_p(gs_p-5^\lambda r_p)=e+2a_p
\quad(p\ne11),\\[1mm]
\text{third:}&
v_p(KD-N)=a_p+e
\quad(p\ne11,23).
\end{array}}
\tag{16.389}
\]

这里 \(11\) 只对应 \(K\equiv9\pmod{11}\) 的一个 root，\(23\) 只
对应 \(2K\equiv9\pmod{23}\) 的一个 root；另一 root 仍落在 generic
公式中。故原来的无界 exceptional set
\(p\mid c_QK(K-9)(2K-9)\) 已严格缩成两个固定 ramified primes
\(11,23\)，加上 middle/third 两条精确赋值核。当前尚需分别排除
这两个固定素数的无限 Hensel 深度，并在 generic primes 上把
(16.383)/(16.384) 与 (16.387) 联立成相反 character 或高度矛盾。

### 16.66 `已严格完成`：odd carrier 等价于 \(\sqrt{26}\) 的奇深接近或单一阈值抵消

(16.385) 还能区分 carrier 的真正赋值来源。记

\[
h_p:=v_p(u_{23})\ge e,\qquad
\sigma_p:=v_p(\mathscr S_0),\qquad
\tau_p:=v_p(\widehat{\mathcal T}_2).
\tag{16.390}
\]

由 (16.291)，第二项的 \(p\)-进赋值精确为 \(2n_p\)，第一项的
赋值精确为 \(\sigma_p\)。因此

\[
\boxed{
\begin{array}{ll}
\sigma_p<2n_p&\Longrightarrow\tau_p=\sigma_p,\\
\sigma_p>2n_p&\Longrightarrow\tau_p=2n_p,\\
\sigma_p=2n_p&\Longrightarrow\tau_p\ge2n_p,
\end{array}}
\tag{16.391}
\]

其中最后一行是唯一可能发生高阶 cancellation 的阈值。因为
\(2n_p\) 为偶数，若 \(\tau_p\) 为奇数，则只有两种可能：

\[
\boxed{
\begin{array}{ll}
\text{I.}&\sigma_p=\tau_p<2n_p\text{ 且二者为奇数};\\
\text{II.}&\sigma_p=2n_p<\tau_p\text{ 且}\tau_p\text{ 为奇数}.
\end{array}}
\tag{16.392}
\]

现在把 \(\sigma_p\) 接回 \(K^2-26\)。令

\[
b_p:=v_p(2K-9).
\]

(16.385) 的两个加数分别有赋值
\(v_p(K^2-26)\) 与 \(b_p+h_p\)，因为 \(T\) 是单位。故

\[
\boxed{
\begin{aligned}
\sigma_p<b_p+h_p
&\Longrightarrow v_p(K^2-26)=\sigma_p,\\
\sigma_p>b_p+h_p
&\Longrightarrow v_p(K^2-26)=b_p+h_p,\\
\sigma_p=b_p+h_p
&\Longrightarrow v_p(K^2-26)\ge b_p+h_p.
\end{aligned}}
\tag{16.393}
\]

对 \(p\ne23\)，(16.388) 给出 \(b_p=0\)。于是 carrier 类型 I 若
\(\tau_p<h_p\)，就精确等价于

\[
\boxed{
v_p(K^2-26)=\tau_p
<\min\{h_p,2n_p\},\qquad \tau_p\text{ 为奇数}.
}
\tag{16.394}
\]

若 \(\sigma_p\ge h_p\)，则 (16.393) 至少强迫
\(p^{h_p}\mid K^2-26\)，之后唯一剩余自由是 (16.385) 两个
正规化加数在深度 \(h_p\) 的 cancellation。由于
\(p\nmid2K\)（由 \(K^2\equiv26\) 且 \(p\ne2,13\)），
\(K^2-26\) 的每个模 \(p\) 根都由 Hensel lemma 唯一提升；这里没有
分叉成指数多个 phase。

因此 generic \(q\)-carrier 的 odd depth 已被完整压成三个明确对象：

1. \(K\) 到唯一 \(p\)-进根 \(\sqrt{26}\) 的奇数距离 (16.394)；
2. \(\sigma_p=h_p\) 时 (16.385) 的一次 normalized cancellation；
3. \(\sigma_p=2n_p\) 时 (16.291) 的一次 normalized cancellation。

\(p=23\) 只改变第一阈值为 \(b_p+h_p\)，并不产生新的自由相位。
这仍未证明三类为空；但它排除了“饱和后还可能在任意许多层任意
跳跃”的情况。剩余证明必须对上述两个明确阈值作 resultant，或把
唯一 \(\sqrt{26}\) Hensel root 与 decimal prefix \(K=10P\)、
\(q\mid Q_0\) 联立。

### 16.67 `已严格完成`：\(q/f\) saturation 在 \(K^2-26\) 上分离，交集恰落入 \(c_Q\)-overlap

同一个 resultant 也能处理 \(f\)-侧，而两侧的结论严格不同。若
非 \(3\) inert prime 是 \(q\)-侧 carrier，则
\(p\mid\mathscr S_0\)，(16.387) 已给出

\[
K^2-26\equiv0\pmod p.
\tag{16.395q}
\]

若它是 \(f\)-侧 carrier，则 §16.46 给出
\(p\mid\mathscr R_f\)。在 saturation 下，(16.386) 与

\[
\mathscr R_f
=2^m5^dg^2\mathscr S_0-4c_Q^2XY,\qquad
N_0=5^{\nu_5}XY
\]

给出

\[
2^{2m}5^{m+d+\nu_5}g^2(K^2-26)
\equiv4c_Q^2N_0\pmod p.
\]

因为 \(m+d+\nu_5=2(m-d)=2\lambda\)，这恰好化成

\[
\boxed{
K^2-26
\equiv
\left(\frac{2c_Q}{2^m5^\lambda g}\right)^2N_0
\pmod p.
}
\tag{16.395f}
\]

若 \(p\nmid c_Q\)，右边是 \(p\)-进单位，故 generic \(f\)-侧严格满足

\[
\boxed{
p\nmid K^2-26,\qquad
\left(\frac{K^2-26}{p}\right)
=\left(\frac{N_0}{p}\right).
}
\tag{16.396}
\]

若 \(p\mid c_Q\)，同一个 (16.395f) 反而退化成
\(K^2\equiv26\pmod p\)；这正是 §16.46 已隔离的
\(c_Q\)-overlap，而不是 generic \(f\)-channel。因此在
\(p\nmid c_Q\) 外部，\(q/f\) 两侧不是同一局部条件的改名：
\(q\)-side 正好落在 \(K^2-26\) 的零点，\(f\)-side 则被强迫落在
一个由 prefix Gaussian norm \(N_0\) 固定的**非零**平方类；两类的
交集只能进入显式 \(c_Q\)-overlap。

\(q\)-side 的零点还能直接接到原 prefix 向量。精确恒等式

\[
K-\frac92Q=10a_2-C_0
\tag{16.397}
\]

说明 \(p\mid q\) 时 \(K\equiv10a_2-C_0\pmod p\)。令

\[
J_{101}:=10C_0+a_2.
\]

二平方恒等式

\[
(10a_2-C_0)^2+(10C_0+a_2)^2
=101(C_0^2+a_2^2)=101N_0
\tag{16.398}
\]

与 (16.395q) 联立，得到新的 prefix bridge

\[
\boxed{J_{101}^2\equiv101N_0-26\pmod p.}
\tag{16.399}
\]

因而每个 \(q\)-carrier 除了在二次域中分裂 \(26\)，还必须使
\(101N_0-26\) 为平方（或为零）。(16.399) 目前仍未与
middle/third residual characters 形成矛盾；但它首次把
\(\sqrt{26}\) Hensel root 接回真实 prefix Gaussian vector，而不是
停留在孤立的 \(K\)-多项式上。下一步应比较 (16.383)/(16.384)、
(16.399) 与 \(N_0=5^{\nu_5}XY\) 的 square-side allocation。

### 16.68 `已严格完成`：\(f\)-side 也只有一个显式 Hensel 阈值

(16.395f) 还可提升为不丢高阶项的整数恒等式。定义

\[
R_\lambda:=2^m5^\lambda g,
\]

\[
\boxed{
\Phi_f
:=R_\lambda^2(K^2-26)-4c_Q^2N_0.
}
\tag{16.400}
\]

把 (16.385) 代入 \(\mathscr R_f\)，再乘以 \(5^{\nu_5}\)，并使用
\[
m+d+\nu_5=2\lambda,
\]
得到

\[
\boxed{
5^{\nu_5}\mathscr R_f
=\Phi_f
-2^m5^{d+\nu_5}g^2(2K-9)u_{23}.
}
\tag{16.401}
\]

这不是模 \(p\) 的近似，而是精确整数等式。对
\(p^e\Vert f\)、\(p^e\mid\mathscr L_{23}\) 的非 \(3\) inert
prime，已有 \(p\nmid5g\)。仍记
\[
h_p=v_p(u_{23})\ge e,\qquad b_p=v_p(2K-9),
\]
并令
\[
\phi_p:=v_p(\Phi_f),\qquad
\rho_p:=v_p(\mathscr R_f).
\]
则 (16.401) 的修正项赋值精确为 \(b_p+h_p\)，故

\[
\boxed{
\begin{aligned}
\rho_p<b_p+h_p
&\Longrightarrow \phi_p=\rho_p,\\
\rho_p>b_p+h_p
&\Longrightarrow \phi_p=b_p+h_p,\\
\rho_p=b_p+h_p
&\Longrightarrow \phi_p\ge b_p+h_p.
\end{aligned}}
\tag{16.402}
\]

因此 \(f\)-side 的高阶接触也没有任意多套来源：

1. 在阈值 \(b_p+h_p\) 以下，它就是单个显式 resultant
   \(\Phi_f\) 的真实赋值；
2. 高于阈值时，只可能来自 (16.401) 两个正规化加数的一次
   cancellation。

当 \(p\nmid c_Q\) 时，\(\Phi_f\equiv0\pmod p\) 正是
(16.395f) 的非零 norm class；当 \(p\mid c_Q\) 时，
\(\Phi_f\equiv R_\lambda^2(K^2-26)\pmod p\)，重新落回
\(\sqrt{26}\) root。故 \(c_Q\)-overlap 是 \(q/f\) 两种局部型的
唯一交界，而不是第三种未命名机制。

当前尚缺的是把 \(\Phi_f\) 的赋值与 \(f=5^\lambda q+2c_u\) 的
完整 \(p^e\) 深度作独立 resultant；但 \(f\)-channel 现在也已压成
一个显式主 resultant 加一个显式阈值 cancellation，与
§16.66 的 \(q\)-channel 结构完全平行。

### 16.69 `已严格完成`：\(f\)-saturation 的完整 denominator 深度等价于纯 prefix resultant

(16.400) 仍含 source 变量 \(c_Q,g\)，但在 \(f\)-saturation 内可以
全部消去。定义纯 prefix 整数

\[
\boxed{
\Psi_f
:=b_2^2(K^2-26)-Q^2N_0.
}
\tag{16.403}
\]

先由
\[
Q=2^{M+1}Q_0,\qquad
b_2=2^{M+m+1}c_ug
\]
得到
\[
\frac{Q}{b_2}=\frac{Q_0}{2^mc_ug}.
\]
另一方面 \(p^e\mid f=5^\lambda q+2c_u\)，乘以 \(c_Q\) 后给出
\[
5^\lambda Q_0+2c_Qc_u\equiv0\pmod{p^e}.
\]
所以在完整深度 \(e\) 上

\[
\boxed{
\frac{2c_Q}{R_\lambda}
\equiv-\frac{Q}{b_2}\pmod{p^e}.
}
\tag{16.404}
\]

这里 \(R_\lambda,b_2\) 都是 \(p\)-进单位。再由
\(p^e\mid u_{23}\)，(16.401) 给出

\[
5^{\nu_5}\mathscr R_f\equiv\Phi_f\pmod{p^e}.
\tag{16.405}
\]

把 (16.404) 的平方代入 \(R_\lambda^{-2}\Phi_f\)，得到

\[
R_\lambda^{-2}\Phi_f
\equiv
K^2-26-\left(\frac Q{b_2}\right)^2N_0
=b_2^{-2}\Psi_f
\pmod{p^e}.
\tag{16.406}
\]

所有被乘除的量都是 \(p\)-进单位，故 (16.405)–(16.406) 给出
逐 prime-power 的截断赋值恒等式

\[
\boxed{
\min\{v_p(\mathscr R_f),e\}
=\min\{v_p(\Psi_f),e\}.
}
\tag{16.407}
\]

结合 §16.46，
\[
\min\{v_p(\widehat{\mathcal T}_2),e\}
=\min\{v_p(\mathscr R_f),e\},
\]
于是还可直接写成

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),e\}
=\min\{v_p(\Psi_f),e\}
\qquad(p^e\Vert f,\ p^e\mid\mathscr L_{23}).
}
\tag{16.408}
\]

所以在完整 denominator 深度以内，\(f\)-carrier 已不再依赖
\(c_Q,g,q,u_{23}\)：它完全由前两块的
\((b_2,Q,K,N_0)\) 决定。

这个 resultant 还是严格正整数。写
\[
x=\frac{b_2}{10^M},\qquad y=\frac{a_2}{10^{M-1}},
\qquad
S_9(x,y)=\frac{81}{4}+\frac{y^2}{100x^2}.
\]
则

\[
\frac{\Psi_f}{b_2^2Q^2}
=
\frac{(9+y)^2}{(2+x)^2}
-S_9(x,y)-\frac{26}{Q^2}.
\tag{16.409}
\]

由当前 endpoint core 的 \(q_0(x,y)<4\)，前两项之差严格大于
\((9+y)^2/[16(2+x)^2]\)。再用
\[
y>\frac{249}{250},\qquad x<\frac2{19},\qquad Q>10^{11},
\]
其下界大于 \(1\)，而 \(26/Q^2<1\)。因此

\[
\boxed{\Psi_f>0.}
\tag{16.410}
\]

(16.407)–(16.410) 把 \(f\)-side 的无界 gcd 问题改写成了一个正的
纯 prefix resultant 问题。尚缺证明
\(\gcd(f,\Psi_f)\) 的 inert primary part 不会在
\(\mathscr L_{23}\) 中饱和；但后续不再需要同时追踪
\(\mathscr R_f,\Phi_f\) 与 source variables 三套表示。

### 16.70 `已严格完成`：两个 denominator channels 统一降为两个纯 prefix gcd

\(q\)-side 也有与 (16.408) 完全平行、而且更短的截断赋值律。
若 \(p^e\Vert q\) 且 \(p^e\mid\mathscr L_{23}\)，则 (16.386) 给出

\[
\min\{v_p(\mathscr S_0),e\}
=\min\{v_p(K^2-26),e\}.
\tag{16.411}
\]

另一方面 §16.45 已有

\[
\min\{v_p(\widehat{\mathcal T}_2),e\}
=\min\{v_p(\mathscr S_0),e\}.
\]

所以

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),e\}
=\min\{v_p(K^2-26),e\}
\qquad(p^e\Vert q,\ p^e\mid\mathscr L_{23}).
}
\tag{16.412q}
\]

与 (16.408) 并列，完整的非 \(3\) denominator reduction 现在是

\[
\boxed{
\begin{array}{rcl}
p^e\Vert q
&\Longrightarrow&
\min\{v_p(\widehat{\mathcal T}_2),e\}
=\min\{v_p(K^2-26),e\},\\[1mm]
p^e\Vert f
&\Longrightarrow&
\min\{v_p(\widehat{\mathcal T}_2),e\}
=\min\{v_p(\Psi_f),e\},
\end{array}
}
\tag{16.412}
\]

其中两行都在 saturation
\(p^e\mid\mathscr L_{23}\) 假设下成立。于是 denominator odd
excess 的无界核心不再是
\(\mathscr S_0,\mathscr R_f,\mathscr D_Z,\mathscr G_q,\mathscr G_f\)
五套看似不同的 gcd，而是恰好两个纯 prefix gcd：

\[
\boxed{
\gcd(q,K^2-26),
\qquad
\gcd(f,\Psi_f).
}
\tag{16.413}
\]

\(\mathscr L_{23}\) 的作用只剩确认完整 denominator prime power
已经饱和；一旦饱和，奇偶深度由 (16.412) 的两个 prefix resultant
唯一读取。特别地：

* 若 \(q\)-carrier 的 odd depth 小于 \(e\)，它就是
  \(v_p(K^2-26)\) 的同一个奇数；
* 若 \(f\)-carrier 的 odd depth 小于 \(e\)，它就是
  \(v_p(\Psi_f)\) 的同一个奇数；
* 只有达到 \(e\) 之后的 parity 仍需 higher lift，不能由截断等式
  单独决定。

这把下一全局命题精确化为：证明所有满足
\(p^e\mid\mathscr L_{23}\) 的非 \(3\) inert primary factors，在
\(\gcd(q,K^2-26)\) 与 \(\gcd(f,\Psi_f)\) 中都不能留下奇 excess；
固定 \(11,23\) 与 \(c_Q\)-overlap 包含在这两个 gcd 内，不再需要
另立无界“例外素数集”。

### 16.71 `已严格完成`：canonical factor allocation 预先选定 \(q\)-carrier 的 third branch

§16.62–16.64 从 rational-root 四次式本身得到三分，但对真正的
\(q\)-carrier，canonical difference of squares 还会预先选定其中
一支。恢复 §16.53 的完整五进 content，有

\[
\mathcal A-Z=5^{\lambda-d}fN,
\qquad
\mathcal A+Z=5^{\lambda-d}qc_+^2Y,
\tag{16.414}
\]

其中
\[
N=c_-^2X,\qquad
5^d\mathcal A=Tc_ugK.
\]
后式等价于

\[
\mathcal A=2^m5^\lambda c_ugK.
\tag{16.415}
\]

现在令非 \(3\) inert prime \(p\mid q\)。由 (16.414) 的 plus
factor，
\[
Z\equiv-\mathcal A\pmod p,
\]
所以 minus factor 给出
\[
2\mathcal A\equiv5^{\lambda-d}fN\pmod p.
\]
又因
\[
f=5^\lambda q+2c_u\equiv2c_u\pmod p,
\]
把 (16.415) 代入并消去单位
\(2c_u5^{\lambda-d}\)，得到

\[
\boxed{N\equiv DK\pmod p.}
\tag{16.416}
\]

因此每个 \(q\)-side denominator prime 在进入 rational-root
方程以前，就已经由 canonical square-side allocation 指定为
\(KD-N\) branch。对真正 carrier 再用 (16.387)：
\[
K^2\equiv26\pmod p,
\]
可知 \(p\nmid K\)，从而 \(N\) 也是单位。于是第一 branch 完全
不可能；middle branch 只有在
\[
KD-N\equiv0,\qquad N-9D\equiv0\pmod p
\]
同时成立时才出现，也就是
\[
K\equiv9\pmod p.
\]
结合 \(K^2\equiv26\) 得到

\[
\boxed{
\text{middle/third overlap 只能是 }p=11,\ K\equiv9\pmod{11}.
}
\tag{16.417}
\]

所以对 \(p\ne11,23\) 的 \(q\)-carrier，(16.378) 无条件适用：

\[
\boxed{
v_p(KD-N)=n_p=a_p+e
\qquad(p\ne11,23).
}
\tag{16.418}
\]

而且 (16.384) 的 residual-unit character 也是唯一 generic
character；(16.377) 的 middle quotient 不再是一个需要全局排除的
generic branch。

两个固定点的预算也可精确保留。若
\(p=11,\ K\equiv9\pmod{11}\)，则 middle 与 third 同时接触，而
\(TN+a_3D\) 仍为单位，所以 (16.372) 变成

\[
\boxed{
v_{11}(TN+2a_3D)+2v_{11}(KD-N)=2n_{11}.
}
\tag{16.419}
\]

若 \(p=23,\ 2K\equiv9\pmod{23}\)，则 middle factor 是单位，
但右边的 \(TN+a_3D\) 可以获得额外深度；此时

\[
\boxed{
v_{23}(KD-N)
=n_{23}+v_{23}(TN+a_3D).
}
\tag{16.420}
\]

\(p=11\) 的另一个 \(\sqrt{26}\) root 与 \(p=23\) 的另一个 root
仍满足 generic (16.418)。至此 \(q\)-carrier 的 rational-root
分流已从“三条无界分支”严格降成：

1. 一个 generic third branch (16.418)；
2. 一个固定 \(11\)-进双因子预算 (16.419)；
3. 一个固定 \(23\)-进右侧增深预算 (16.420)。

下一步不应再尝试排除 generic middle branch；它已被 canonical
allocation 消去。真正剩余的是将 (16.418) 的 normalized third
unit 与 prefix gcd \(\gcd(q,K^2-26)\) 联立，以及单独关闭
(16.419)–(16.420) 的两条固定 Hensel lifts。

### 16.72 `已严格完成`：third branch 实际全局提升为 \(q\mid KD-N\) 与正加性 quotient

(16.416) 不只是逐素数的模 \(p\) 现象。由 (16.414) 的两个精确
factor equality，

\[
\begin{aligned}
2\mathcal A
&=(\mathcal A-Z)+(\mathcal A+Z)\\
&=5^{\lambda-d}\left(fN+qc_+^2Y\right).
\end{aligned}
\tag{16.421}
\]

再代入
\[
f=5^\lambda q+2c_u,\qquad
\mathcal A=c_u5^{\lambda-d}DK,
\]
并约去 \(5^{\lambda-d}\)，得到

\[
\boxed{
2c_u(DK-N)
=q\left(c_+^2Y+5^\lambda N\right).
}
\tag{16.422}
\]

由于 \(\gcd(q,2c_u)=1\)，立刻有全局整除

\[
\boxed{q\mid DK-N.}
\tag{16.423}
\]

定义

\[
\boxed{
W_q:=\frac{DK-N}{q}\in\mathbf Z_{>0}.
}
\tag{16.424}
\]

正性来自 \(K>9\cdot10^{11}\) 与 \(N/D=J_{\rm def}<3\)。而 (16.422)
化成不含 \(Z,\mathcal A,f\) 的正加性 quotient：

\[
\boxed{
2c_uW_q
=c_+^2Y+5^\lambda c_-^2X.
}
\tag{16.425}
\]

这说明 rational-root 的 third factor 并不是在 carrier prime 出现后
才偶然接触 \(q\)：完整的 \(q\) 早已由 canonical square-side
allocation 全局嵌入 \(KD-N\)。§16.71 的 valuation 结论现在可写成

\[
\boxed{
v_p(W_q)=v_p(c_Q)
\qquad
\left(
\begin{array}{c}
p^e\Vert q,\ p^e\mid\mathscr L_{23},\\
p\text{ 为 }q\text{-carrier},\ p\ne11,23
\end{array}
\right).
}
\tag{16.426}
\]

特别地，在 \(p\nmid c_Q\) 的 generic carrier 层，
\(W_q\) 是 \(p\)-进单位；全部 \(q\)-深度已经由定义 (16.424)
精确约尽。固定 \(11,23\) 的额外预算则描述 \(W_q\) 是否还获得
超出 \(c_Q\) 的深度。

还有一个无条件的模 \(4\) orientation。因为 \(4\mid D\)、\(K\) 为
偶数、\(N\equiv-Z\pmod4\) 且 \(q\equiv3\pmod4\)，有

\[
\boxed{
W_q\equiv3Z\pmod4.
}
\tag{16.427}
\]

所以
\[
Z\equiv3\Longrightarrow W_q\equiv1\pmod4,\qquad
Z\equiv1\Longrightarrow W_q\equiv3\pmod4.
\]
后一 orientation 的 \(W_q\) 自身必须含一个 odd inert prime；
是否能证明该 prime 必回到
\(\gcd(q,K^2-26)\) 而不能来自 \(c_+^2Y+5^\lambda c_-^2X\) 的
外部加法，是现在比 generic middle branch 更精确的剩余问题。

### 16.73 `已严格完成`：\(W_q\) 的非 \(3\) inert prime 被锁到 \(H_0\) 且固定 prefix-norm character

(16.425) 对 \(W_q\) 的 endpoint-external inert prime 还有两条
独立后果。设
\[
r\ne3,\qquad r\equiv3\pmod4,\qquad r\mid W_q.
\]
§16.45 已证明这种 \(r\) 不能整除 \(XY,c_u,g\)。它也不能整除
\(c_Q\)：若 \(r\mid c_+\)，则 (16.425) 模 \(r\) 后只剩
\(5^\lambda c_-^2X\)，是单位；若 \(r\mid c_-\)，则只剩
\(c_+^2Y\)，同样是单位。故

\[
\boxed{\gcd(r,c_Qc_u gXY)=1.}
\tag{16.428}
\]

现在对 (16.425) 模 \(r\) 取 character：

\[
c_+^2Y\equiv-5^\lambda c_-^2X\pmod r.
\]

约去平方并用 \(N_0=5^{\nu_5}XY\)，得到

\[
\begin{aligned}
\left(\frac{N_0}{r}\right)
&=
\left(\frac{5^{\nu_5}XY}{r}\right)\\
&=
\left(\frac{-5^{\nu_5+\lambda}}r\right)
=\left(\frac{-1}{r}\right)=-1,
\end{aligned}
\]

因为
\[
\nu_5+\lambda=2(\lambda-d)
\]
为偶数。因此

\[
\boxed{
r\mid W_q,\ r\ne3,\ r\equiv3\pmod4
\Longrightarrow
\left(\frac{N_0}{r}\right)=-1.
}
\tag{16.429}
\]

另一方面，把 \(q^2\) 从清分母后的 rational-root 等式 (16.379)
中用 (16.424) 精确约去，得到

\[
b_2^2TN(TN+2a_3D)W_q^2
=2^{2M+2}c_Q^2N_0D^2(TN+a_3D)^2.
\tag{16.430}
\]

由 (16.428)，除 \(W_q\) 外的
\(b_2,T,N,c_Q,N_0,D\) 都是 \(r\)-进单位。等式右边强迫
\(r\mid TN+a_3D\)。这又保证 \(r\nmid a_3\)：否则
\(r\mid TN\)，与 \(N\) 为单位矛盾。于是

\[
TN+2a_3D\equiv a_3D\not\equiv0\pmod r.
\]

比较 (16.430) 两边的精确赋值，得到

\[
\boxed{
v_r(W_q)=v_r(TN+a_3D).
}
\tag{16.431}
\]

最后，\(N=3D-C\) 与 (16.100) 给出整数恒等式

\[
\begin{aligned}
TN+a_3D
&=D(3T+a_3)-TC\\
&=2^m5^d\left(g(3T+a_3)-5^\lambda C\right)\\
&=2^m5^dH_0.
\end{aligned}
\tag{16.432}
\]

所以 (16.431) 精确化为

\[
\boxed{
v_r(W_q)=v_r(H_0).
}
\tag{16.433}
\]

这关闭了一个此前未命名的 prime-source 自由度：\(W_q\) 的每个
非 \(3\) inert prime 都不是“自发”出现，而是以完全相同的深度来自
真实 sphere height \(H_0\)，并同时满足 prefix norm nonresidue
(16.429)。剩余 endpoint-external 命题已经变成明确的
\[
r\mid H_0,\qquad
\left(\frac{N_0}{r}\right)=-1
\]
通道；下一步必须用 sphere/high-factor equality 排除它，或证明其
赋值在 \(W_q\) 中总为偶数。

---

# 第六部分：审计后降级的漂亮恒等式

## 17. `失效/降级`：source / reflection 的若干深 `5`-进 endpoint congruence

本轮中曾得到过若干形如

\[
5^r\mid\text{linear form}(H,e,h,C,\ldots)
\]

的深五进式。它们在局部展开时看起来像新的 mixed-radix obstruction。

完整把

\[
\omega C=qA_j-BC_j,
\]

Hensel slot、source split 与

\[
C_j=10P-j
\]

代回后，可以看出其中 source 版本直接因式分解出已知 `5^d`，而 reflection 版本中的低位项与 `C_j` 的 decimal tail 精确抵消；剩余项因十进制高位自动含目标 `5`-幂。

因此这些式子属于

\[
\boxed{
\text{determinant/source split + decimal place 的重写}
}
\]

而不是新的独立 obstruction。

本文明确保留这一 no-go，后续不得把这些 congruence 再计作额外稀疏性或“第二条独立 Hensel 条件”。真正有 pruning power 的新增输入是：

1. endpoint shell / `q0` barrier；
2. `C/D`、`x,y,zeta,w` 的真实窄窗；
3. high/low-`m` 高度二分；
4. low-`m` 的深 `v5(N0)`；
5. `rho^2` high/low `2`-adic factor 量化与 slot exclusion。

---

# 18. 当前严格边界与下一步

本文没有关闭整个 A2。当前新的最具体核心为：

### high-`m` cone

\[
m>6M/11,
\qquad
u_0/K_\rho<1/304,
\]

若 `rho^2` 进入任一 sphere factor，则 quotient 至少达到 `956` 层。下一步应把这个 deep quotient 与 `c_u^2, c_Q^2` 的 square-side allocation 同时送入 Gaussian rectangle。

### low-`m` cone

\[
s=0,
\qquad
3M/7<\lambda\le m\le6M/11,
\]

并有

\[
v_5(N_0)>6M/77,
\qquad
\mathfrak L_0>1000C.
\]

其中 reflection 更强到

\[
v_5(N_0)>15M/77.
\]

`rho^2` 的 high-2 side 已在

\[
m\le(M-2)/2
\]

全部排除，并在精确中线

\[
M=2m
\]

的 reflection 子族再次全部排除。

因此下一步不再回到固定 `eta` 的 slot 枚举。统一 quotient 已被提升为
精确商 (16.91)，其短 orientation 恰停在 `d`，而 `theta` 同伴与
`omega` 核严格相关；(16.126)–(16.133) 又把 quotient 变成逐坐标唯一
最近商，而 (16.134)–(16.141) 把提升后 quotient 与原 prefix 的方向锁
精确加强到宽度 `1/a_2`，并从 `mathcal S_5` slope 唯一恢复原
prefix 系数 `C_0`；(16.142)–(16.149) 又把该条带化为商恰为 `1`、
余量严格下降的正 Euclidean split。裸 quotient 仍缺共同因子的绝对
argument，且该实线性 split 的 determinant 为 `-epsilon a_2`，不能
保持 Gaussian norm；但 (16.152)–(16.161) 已在裸
`(W_5,V_5)` 上构造出纯实唯一首商和 norm 至少下降四倍的 canonical
Gaussian 余数；(16.162)–(16.167) 又把同一模数下的剩余条件降成唯一
中心标量 `r_E` 与正定二次核。该余数尚未证明保持 decimal plane，
标量二次核也尚未排除；(16.168)–(16.174) 进一步证明其精确提升商
`z_E` 是由真实缺口 `H` 模 `g` 唯一确定的中心奇代表；
(16.175)–(16.180) 则把它送入 discriminant 为
`-4c_u^2c_-^2C_0^2` 的 prefix norm；(16.181)–(16.184) 进一步约去
完整 `g`，并识别为 `R_E overline(B_5)` 的精确 composition。
(16.185)–(16.189) 最后把 `H` 的中心代表与顶部 `C` 代表接入同一
整数核；尚待加入独立的 `C divides F(3)`。
(16.190)–(16.195) 同时证明 canonical Gaussian child 的斜率远离 A2
prefix window，故同型下降路线严格降级。
(16.196)–(16.201) 又把独立的 rational-root 条件正规化为正奇
\(5\)-进单位
\[
\Xi_C=\frac{F(3)}{2^{2M+2}5^{\nu_5}C};
\]
所以剩余闭环只能来自这个 odd-prime cofactor 与
\((z_E,\chi_E)\) 核的不相容，不能再依赖 \(2,5\)-进深度本身。
(16.202)–(16.208) 进一步证明 \(\Xi_C/Y\) 在
\(2^m5^d\) 上是显式平方，并把 \(\Xi_CC^{-1}\) 模 \(g\) 的平方类
固定为 \(c_u\)；这把奇余因子接入完整 denominator，但尚未排除该
平方类。
(16.209)–(16.216) 再从相邻整数点得到互素的 \(D-C,D+C\) 两个
\(D\)-尺度除数及正奇 cofactor \(\Xi_-,\Xi_+\)；三者在
\(2^m5^d\) 上共享同一个 \(Y\)-平方类。当前可行的直接路线因而是
三 cofactor 的 resultant / reciprocity 排除，而不是扩大 defect
枚举。
(16.217)–(16.223) 进一步证明 \(c_u,H\) 均与 \(g\) 互素，并锁定
\(\operatorname{sgn}\chi_E=\operatorname{sgn}(\varepsilon z_E)\)；
所以 mixed kernel 没有象限自由度，零因子则被隔离到
\(3T+a_3\) 的饱和通道。
(16.225)–(16.230) 最终消去 \(C,c_u,z_E,H,q\) 的平方类自由度，
把非饱和奇素通道压成
\[
\left(\frac{\Xi_C}{p}\right)
=\left(\frac{-\varepsilon a_25^{M+d}}p\right)
\quad(p\mid g,\ p\nmid3T+a_3).
\]
剩余工作是从另一侧固定相反字符，而不是继续展开同一个中心同余。
(16.231)–(16.233) 审计表明模 \(g^2\) 的二阶修正自动是 principal
square；因此普通 quadratic-character 提升路线严格降级，下一输入
必须超出二次特征。
(16.234)–(16.241) 随后从 \(F''>0>F'''\) 得到三 cofactor 的首条
加性约束：
\[
0<\Xi_+-\Xi_C<\Xi_C-\Xi_-,
\qquad
L\mid(\Xi_+-\Xi_C),(\Xi_C-\Xi_-).
\]
这为 cubic 二阶差分提供了严格符号与整数尺度。
(16.242)–(16.247) 进一步把该二阶差分精确化为
\[
\Delta_--\Delta_+
=2^{m+1}5^dc_u^2
\{g((2K-9)T-a_3)-H_0\},
\]
从而含巨大正因子 \(2^{m+1}5^dc_u^2\)；尚缺同尺度上界或新的模约束。
(16.248)–(16.251) 给出内部尺度比较
\[
0<\Delta_--\Delta_+<\Delta_+,
\qquad1<\Delta_-/\Delta_+<2;
\]
故纯实曲率大小不会自行矛盾，下一步必须使用加法的 prime support 或
\(D\pm C\) 余类。
(16.252)–(16.257) 进一步固定
\[
v_2(\Delta_-)=v_2(\Delta_+)=1,
\qquad
v_2(\Delta_--\Delta_+)=m+1,
\quad
v_5(\Delta_--\Delta_+)=d.
\]
所以 pure-\(2\) fallback 也已进入精确的相邻-gap 核。
(16.258)–(16.262) 最后把两个 gap 接回互素大模数：
\(\Delta_+\) 落入模 \(D^2-C^2\) 的唯一显式 CRT 类，
\(\Delta_-=\Delta_++\Gamma_\Delta\)。尚缺对 CRT 商
\(Q_\Delta\) 的全局控制。
(16.263)–(16.268) 进一步从 additive CRT 抽出无饱和 character：
\[
\widetilde{\mathcal T}_2
\equiv-5^\lambda(c_uC)^2\pmod g,
\qquad
\left(\frac{\widetilde{\mathcal T}_2}{p}\right)
=\left(\frac{-5^\lambda}{p}\right)
\quad(p\mid g,\ p\text{ odd}).
\]
这已覆盖所有 odd prime channels；尚缺显式式另一侧的相反 character。
(16.269)–(16.271) 又在二进端无条件得到
\[
\widetilde{\mathcal T}_2\equiv3\pmod4,
\]
故它必须含一个不整除 \(g\) 的 \(3\bmod4\) 惰性素数到奇次。当前最短
闭环目标是证明显式式 (16.259) 应为 Gaussian norm。
(16.272)–(16.273) 的审计说明当前显式式只是“尺度项减 Gaussian
norm”，并无所需交叉项；所以 norm 识别仍是真缺口，不能从两项各自
norm-like 直接推出。
(16.274)–(16.278) 同时证明 additive CRT 商满足
\[
Q_\Delta\ge5K;
\]
所以它不是可由小自然代表排除的有限层，而是新的无界高度。CRT 路线
若继续，必须控制该大商的结构。
(16.279)–(16.282) 还把 once-normalized additive cofactor 接回
canonical discriminant：
\[
\widetilde{\mathcal T}_2
=5^{m+d}K_0+Lc_u^2g^2\mathscr R_0,
\qquad\mathscr R_0<0.
\]
下一候选闭环是将 canonical square 代入并做相邻平方 gap，而不是重复
odd inert excess。
(16.283)–(16.287) 的完整代入审计表明
\[
\widetilde{\mathcal T}_2
=5^{\epsilon_5}Z_\nu^2+\mathscr J_\Delta,
\qquad
\mathscr J_\Delta\equiv2\pmod4;
\]
这恰好恢复旧 odd inert excess，并不自动给相邻平方矛盾。后续必须
排除 \(\mathscr J_\Delta\) 的三类 prime 来源。
(16.288)–(16.293) 修正了归一化：严格有
\[
v_5(\widetilde{\mathcal T}_2)=d,\qquad
\widehat{\mathcal T}_2
=\mathcal T_2/(2^{m+1}5^{2d}),
\]
且
\[
\gcd(\widehat{\mathcal T}_2,10c_ug)=1,\qquad
\widehat{\mathcal T}_2\equiv3\pmod4.
\]
因此后续 prime-source 分析必须作用在
\(\widehat{\mathcal T}_2\)，不能把必然的 \(5^d\) 留在所谓本原
对象中。
(16.294)–(16.304) 进一步给出完整 denominator 接触律
\[
\gcd(\widehat{\mathcal T}_2,Q_0XY)
=\gcd(\mathscr S_0,Q_0XY),\qquad
\gcd(\widehat{\mathcal T}_2,f)
=\gcd(\mathscr R_f,f).
\]
非 \(3\) 的 inert prime 不能整除 \(XY,c_u,g\)，所以 \(qf\) excess
只剩 \((q,\mathscr S_0)\)、\((f,\mathscr R_f)\) 与
\(c_Q\)-overlap 三个显式通道。
(16.305)–(16.310) 又把固定异常素数 \(3\) 的一阶接触完全分类：
只有两类由 \(3\mid Q_0\) 与 \(a_2a_3\bmod3\) 决定的 digit residue
能够出现；允许类中的 \(3\)-进赋值奇偶仍待证明。
(16.311)–(16.313) 把允许的固定 \(3\) 通道继续提升到单一模 \(9\)
条件；当前一阶数据允许 \(0,3,6\bmod9\) 三种 lift，所以更高
\(3\)-进奇偶必须与 \(C\) 或 \(k_h\)-allocation 联立。
(16.314)–(16.321) 给非 \(3\) denominator channel 一个不同于旧
Gaussian character 的新输入：
\[
\operatorname{disc}_K(\mathscr S_0)=8\mathscr R_{23},
\qquad
\operatorname{disc}_K(\mathscr R_f)=8A_f\mathscr R_{23,f},
\]
其中 \(\mathscr R_{23}\) 是判别数 \(-23\) 的二元型。simple/double
root 分别产生 (16.316)、(16.318)、(16.320) 的分裂约束；尚缺把
它们与 source allocation 接成相反 character。
(16.322)–(16.325) 的完整配方进一步给出
\[
\left[c_ug(TK-9T-2a_3)\right]^2
=\mathscr C_{23}+5^m\widehat{\mathcal T}_2.
\]
因此上述 curvature character 都是同一 principal-square identity
的投影，不能作为第二个独立 obstruction；真正缺口是
\(\mathscr C_{23}\) 的独立 source/norm character。
(16.326)–(16.328) 又把 companion 精确写成
\[
\mathscr C_{23}
=U_{23}^2+23V_{23}^2+5^{3\lambda}Q_0^2XY,
\]
并证明它模 \(5^{2m}\) 与模 \(8\) 都是 principal square；所以
\(2,5\)-进局部非平方路线也已降级。
(16.329)–(16.340) 把 companion 与 canonical \(Z\) 联立成正
shifted pair：
\[
\mathscr V_-=5^\lambda fc_-^2X-\mathscr E_{23},
\qquad
\mathscr V_+=5^\lambda qc_+^2Y-\mathscr E_{23}.
\]
同侧 \(q,f\) 接触完全由
\(\mathscr L_{23}=9T/2+a_3\) 控制，两因子的公共部分则为
\(\gcd(TK-9T-2a_3,Z)\)。
(16.341)–(16.348) 消去 \(Z\) 并证明
\[
\gcd(\mathscr D_Z,qf)=\gcd(\mathscr L_{23}^2,qf);
\]
所以所有未饱和 denominator contact 都是偶赋值，odd excess 只剩
\(p^e\Vert qf,\ p^e\mid\mathscr L_{23}\) 的完整 prime-power
saturation。
(16.349)–(16.354) 再给出全局 orientation
\[
q\equiv3,\quad f\equiv1,\quad X\equiv Y\equiv-Z\pmod4.
\]
\(Z\equiv1\) 对应固定 \(3\) balanced transfer，且此时
\(3\nmid\widehat{\mathcal T}_2\)；\(Z\equiv3\) 对应 denominator
\(q\) carrier。
(16.355)–(16.358) 进一步证明 \(Z\equiv1\) 时 shifted pair 恰共享
一份 \(3\)，约去后 plus side 固定为 \(3\bmod4\)。尚缺控制其额外
\(3\)-primary depth 或把非 \(3\) inert prime 送入上述 saturation。
(16.359)–(16.366) 最后把 saturation 写成完整 prime-power targets
\[
p^e\Vert q,\ p^e\mid\mathscr G_q
\quad\text{或}\quad
p^e\Vert f,\ p^e\mid\mathscr G_f,
\]
其中 \(\mathscr G_q,\mathscr G_f\) 只含 \(a_3,H\) 与已知 source
尺度，并位于约 \(-89\cdot5^{M-1}T\) 的同一窄 significand band。
它们不是小余数；剩余闭环需要真正的无界 gcd/resultant。
(16.367)–(16.370) 在 generic \(q\)-saturation 中进一步利用
rational-root 四次式，把一支提升到 \(p^{2e}\) 深度：
\[
p^e\mid(6D+C),\qquad
p^{2e}\mid D(3T+2a_3)-TC,
\]
另一支为 \(p^e\mid(K-3)D+C\)，例外集中在
\(p\mid c_QK(K-9)\)。尚缺把该二倍深度转成统一高度矛盾。
(16.371)–(16.384) 随后把粗 lower bound 提升为 rational-root
等式的精确 prime-power budget，并识别约尽完整 \(p\)-幂后的
residual-unit characters。
(16.385)–(16.394) 用
\[
\mathscr S_0=T(K^2-26)-(2K-9)(2a_3+9T)
\]
把真正 \(q\)-carrier 强迫到 \(K^2\equiv26\pmod p\)，第一
valuation branch 因而消失，无界例外缩成固定 \(11,23\)；odd depth
只可能来自 \(\sqrt{26}\) 的奇深 Hensel 接近或两个明确阈值抵消。
(16.395)–(16.410) 又证明 generic \(f\)-carrier 取互补非零局部型，
并将完整 \(f\)-深度降成正的纯 prefix resultant
\[
\Psi_f=b_2^2(K^2-26)-Q^2N_0>0.
\]
(16.411)–(16.413) 因而把两个 denominator saturation channels
统一为
\[
\gcd(q,K^2-26),\qquad \gcd(f,\Psi_f).
\]
(16.414)–(16.427) 进一步使用 canonical factor allocation，证明
generic middle branch 实际不存在，并在整数层得到
\[
q\mid DK-N,\qquad
2c_u(DK-N)/q=c_+^2Y+5^\lambda c_-^2X.
\]
除固定 \(11,23\) 外，唯一 rational-root branch 满足
\(v_p(KD-N)=v_p(c_Qq)\)。
(16.428)–(16.433) 最后把 quotient \((DK-N)/q\) 的每个非 \(3\)
inert prime 以完全相同深度锁到真实 sphere height \(H_0\)，并固定
\((N_0/r)=-1\)。当前无界核心已经精确缩成两个 pure-prefix gcd、
固定 \(11,23\) lifts 与这个 sphere-height channel；这些仍未全部
排除。
真正新增的
decimal-plane 接口是 (16.101)–(16.104) 对小补余量 `C` 的自然代表公式。
要关闭本 cone，必须继续恢复完整尺度与 `a_2,C`，并证明这个确定商与
`C` 代表或精确非零面积不相容，或由此产生保持原十进制平面的严格降高。

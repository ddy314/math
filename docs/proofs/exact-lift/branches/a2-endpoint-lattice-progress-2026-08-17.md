# A2 endpoint lattice continuation — 2026-08-17

> **适用范围：**延续已合并的 `a2-decimal-ellipse-phase.md`、`a2-ellipse-to-defect-window.md` 与 `a2-low-defect-angle-squeeze.md`。  
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

对一般 reflection high-2 allocation，令

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

因此整个 reflection high-2 cone 已经被重写为离散 lattice

\[
\boxed{(\eta,d,c_Q,k_h)}
\]

上的窄整数带问题。`eta=0` 已由 §15 全部关闭；下一步应寻找对 `eta` 统一的 slot exclusion，而不是逐层无限枚举。

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

因此下一步最值得攻击的是 (16.2) 的统一 `eta`-slot lattice：若能证明所有 `eta>=0` 都无整数带交点，就会把 reflection 的 `rho^2` side choice 全局定向；再与 `c_Q^2/c_u^2` allocation 和小补余量 `C` 联立，才有希望把“唯一 representative”升级为真正空性。

# DD frontier: allocation, rational contact and terminal audits

> 本文件是按数学依赖整合的规范编辑入口。每个来源笔记只在本文件中保留一次；来源边界、原状态和公式正文均保留，避免日期文件之间形成平行副本。

## 整合顺序

`dd-projective-angular-allocation-2026-08-16.md` → `dd-rational-contact-frontier.md` → `dd-frontier-five-adic-forcing-2026-08-16.md` → `dd-frontier-five-adic-baseline-2026-08-16.md` → `dd-frontier-one-channel-second-order-2026-08-16.md` → `dd-frontier-decimal-remainder-2026-08-16.md` → `dd-frontier-continuation-2026-08-16.md` → `dd-good-slot-capacity-2026-08-16.md`

---

## 1. DD projective angular allocation — 2026-08-16

> 整合来源：`dd-projective-angular-allocation-2026-08-16.md`。以下正文保留该来源的原始证明状态和审计边界。

> 本文接续 [`core.md`](core.md) §§56--61，对一般 DD 的 projective denominator / 5-adic allocation 做进一步精确化。
> 本文结论不要求进入 `6.308883...` frontier；它们是在原 §57--61 假设和符号下的严格局部算术结论。
>
> **状态边界：**本文关闭的是“5-adic angular depth 可以再次支付 projective denominator / 两条 carrier contact”的重复支付通道；它本身还不是 DD 全局空性。

---

### 1. 基线

沿用 overlap 参数化

\[
Q=\eta Q_1,
\qquad
\tau=\eta v,
\qquad
(LQ_1,v)=1,
\qquad
(L,\eta)=1.
\]

无 \(E_D\) eliminant 为

\[
\Xi
=(LQ+\tau)^2(LQ+2\tau)^2
(10^{2k}+10^{2d}).
\tag{1.1}
\]

若两个独立 carrier residual 同时满足

\[
5^h\mid\mathcal E_{12},
\qquad
5^h\mid\mathcal E_{13},
\]

则已有

\[
\boxed{
h\le2v_5(Z_0)+v_5(\Xi).}
\tag{1.2}
\]

projective point 写成

\[
z=\frac{X_0+iY_0}{Z_0},
\]

并令

\[
g=(y_1,y_2),
\qquad r_5=v_5(g).
\]

已有 exact formula

\[
\boxed{
Z_0=\frac{H+y_3}{(g,H+y_3)}.
}
\tag{1.3}
\]

同时

\[
(H-y_3)(H+y_3)=y_1^2+y_2^2.
\tag{1.4}
\]

---

### 2. 当 \(5\mid L\) 时两个 moving factors 都是 5-adic units

设

\[
\ell_5:=v_5(L)>0.
\]

由

\[
(L,\eta)=1
\]

得到

\[
v_5(\eta)=0.
\]

又由

\[
(LQ_1,v)=1
\]

得到

\[
v_5(v)=0.
\]

于是

\[
LQ+\tau
=\eta(LQ_1+v),
\]

\[
LQ+2\tau
=\eta(LQ_1+2v).
\]

模 \(5\) 有

\[
LQ_1+v\equiv v\not\equiv0,
\]

\[
LQ_1+2v\equiv2v\not\equiv0.
\]

故

\[
\boxed{
v_5(LQ+\tau)=v_5(LQ+2\tau)=0.}
\tag{2.1}
\]

因此 `(1.1)` 在 5-adic place 的 valuation 完全退化为 decimal baseline：

\[
\boxed{
v_5(\Xi)=v_5(10^{2k}+10^{2d}).}
\tag{2.2}
\]

而直接分情况 \(k<d,k>d,k=d\) 得到

\[
\boxed{
v_5(10^{2k}+10^{2d})=2\min(k,d).}
\tag{2.3}
\]

所以

\[
\boxed{v_5(\Xi)=2\min(k,d).}
\tag{Moving-unit}
\]

**结论：**当 \(5\mid L\) 时，§56 中列出的两个单侧 moving factors 在 5-adic place 完全不能支付任何额外深度。

---

### 3. 一个 odd-prime two-factor lemma

令 \(p\) 为奇素数，\(A,B\in\mathbf Z\)，并记

\[
s=\min(v_p(A),v_p(B)).
\]

若

\[
v_p(A-B)>s,
\]

则

\[
\boxed{v_p(A+B)=s.}
\tag{3.1}
\]

证明：写

\[
A=p^sA_0,
\qquad
B=p^sB_0,
\]

至少一个 \(A_0,B_0\) 为 unit。由

\[
p\mid A_0-B_0
\]

可知二者事实上都是 units 且

\[
A_0\equiv B_0\not\equiv0\pmod p.
\]

因为 \(p\ne2\)，

\[
A_0+B_0\equiv2A_0\not\equiv0\pmod p.
\]

故 (3.1) 成立。

---

### 4. 5-adic angular depth 不会进入 \(Z_0\)

令

\[
s_5:=\min(v_5(H),v_5(y_3)).
\]

sphere gap 为

\[
H-y_3=La,
\]

故

\[
v_5(H-y_3)=\ell_5+v_5(a).
\tag{4.1}
\]

真正的 angular case 正是 gap depth 超过共同 multiplicative scale 的情况，即

\[
\ell_5+v_5(a)>s_5.
\tag{4.2}
\]

对 `(3.1)` 取

\[
A=H,
\qquad B=y_3,
\qquad p=5,
\]

由 `(4.2)` 得

\[
\boxed{v_5(H+y_3)=s_5.}
\tag{4.3}
\]

再由 `(1.3)`：

\[
\begin{aligned}
v_5(Z_0)
&=v_5(H+y_3)
-
\min(r_5,v_5(H+y_3))\\
&=s_5-\min(r_5,s_5).
\end{aligned}
\]

所以

\[
\boxed{
v_5(Z_0)=\max(0,s_5-r_5).}
\tag{Angular-Z0-collapse}
\]

右边只测量 \(H,y_3\) 的 common multiplicative scale 相对于 \((y_1,y_2)\) common scale 的差；它**完全不含** primitive Gaussian angular depth

\[
\omega_5=v_5(X^2+Y^2).
\]

这比旧的

\[
v_5(Z_0)=\max(0,r_5+\omega_5-v_5(La))
\]

更清楚地说明了支付结构：一旦 \(5\)-adic sphere gap 已经深过共同尺度，angular depth 在因子化

\[
(H-y_3)(H+y_3)
\]

中全部进入第一因子 \(H-y_3\)，不会再出现在 complementary projective denominator 中。

换言之：

\[
\boxed{
\text{5-adic angular depth}
\not\longrightarrow Z_0
\quad\text{(after common-scale baseline is separated).}
}
\tag{4.4}
\]

---

### 5. 与 bottom-edge exclusion 合并

旧 §60 已证明，若 primitive prefix angle 有正 5-adic depth

\[
\omega_5>0,
\]

则

\[
\boxed{v_5(U_{12}^{\rm prim})=0.}
\tag{5.1}
\]

因此 primitive bottom carrier edge 不接收 angular depth。

同时 determinant ultrametric theorem 对

\[
\theta_{12},\theta_{13},\theta_{23}
\]

要求三个 valuation 中两个最小值相等。删去 decimal forced baseline 后，由 `(5.1)` 有

\[
v_5(\theta_{12})=0.
\]

于是必有

\[
\boxed{
\min(v_5(\theta_{13}),v_5(\theta_{23}))=0.
}
\tag{5.2}
\]

所以 angular depth至多进入一条上侧 carrier edge；它不可能同时进入两条独立 carrier residual。

---

### 6. angular depth 对 simultaneous carrier contact 的零贡献

将 `(Moving-unit)` 与 `(Angular-Z0-collapse)` 代入无 \(E_D\) bound `(1.2)`：

\[
\boxed{
h
\le
2\max(0,s_5-r_5)
+2\min(k,d).}
\tag{6.1}
\]

右端只包含：

1. common-scale discrepancy \(s_5-r_5\)；
2. explicit decimal baseline \(2\min(k,d)\)。

**primitive angular depth \(\omega_5\) 完全消失。**

因此得到严格 allocation lemma：

\[
\boxed{
\begin{array}{c}
5\mid L,\quad
v_5(H-y_3)>\min(v_5(H),v_5(y_3)),\quad
\omega_5>0\\[2mm]
\Longrightarrow\\[2mm]
\text{任何两条独立 carrier residual 的共同 5-depth，}\
\text{扣除 decimal/common-scale baseline 后都不能由 }\omega_5\text{ 支付。}
\end{array}
}
\tag{Angular-no-double-pay}
\]

结合 `(5.2)`，angular depth 既不能进入 bottom edge，也不能进入 projective denominator，也不能进入 simultaneous upper-edge contact。

---

### 7. 对一般 5-adic allocation 的更新

旧 §61 将 \(v_5(L)\) 分成：

- common-scale / multiplicative；
- genuine angular。

现在第二支可以进一步精确化：

#### genuine angular excess

若某一正线性深度确实由

\[
\omega_5=v_5(X^2+Y^2)
\]

承担，那么这份深度只能作为 **sphere-gap angular depth** 存在；它不能再次支付：

- \(Z_0\)；
- primitive bottom edge；
- 两条独立 carrier residual；
- \((LQ+\tau)/\eta\) 或 \((LQ+2\tau)/\eta\) 的 5-depth。

所以凡是后续论证能够证明“同一正线性 excess 必须再出现于任意上述第二通道”，genuine-angular branch 会立即矛盾。

这将一般 projective/common-scale allocation 的开放部分进一步压缩到：

\[
\boxed{
\text{common multiplicative scale}
\quad\cup\quad
\text{至多一条 single-edge angular contact}.
}
\]

真正尚未关闭的是前者，以及如何从 global DD carrier/tail system 强迫 angular excess 必须发生第二次独立接触。

---

## 2. DD frontier：rational contact、Bad/Good 分解与 cofactor 临界系统

> 整合来源：`dd-rational-contact-frontier.md`。以下正文保留该来源的原始证明状态和审计边界。

> 状态：本文是 [`core.md`](core.md) terminal frontier 的后续证明记录。
> 除明确标成 `待证` 或 `失效/降级` 的项目外，下面的恒等式和条件蕴含都只在假想
> \(n_3/S\to6.308883577618\ldots\) 的 frontier sequence 上使用。
> **它们不是 DD 全局空性，也不给出有效绝对 \(S\) 上界。**
>
> 本文统一采用
> \[
> A=s\theta q_c,\qquad b=5^T\widetilde r,
> \qquad R_+=b+A,\qquad R_-=b-A.
> \]
> 因而 \(D_+=(V,R_+)\) 对应固定点 \((-1,-1,-1)\)，
> \(D_-=(V,R_-)\) 对应固定点 \((1,1,1)\)。
> 这一约定贯穿全文，避免旧草稿中 `+/-` 同时表示“加法符号”和“固定点符号”的混淆。

### 1. 已有 terminal 基线

本文直接依赖 `core.md` 已建立的 terminal normalization：

\[
X=2^HZ,\qquad Y=5^TU,\qquad V=X-Y=C_0s,
\]

\[
(U,V)=(U,Z)=(V,Z)=1,
\qquad (UVZ,10)=1,
\]

\[
V=C_Lv_0,
\qquad
\log C_L=S+o(S),
\qquad
\log v_0=o(S),
\]

\[
q_c=10^{z_*S+o(S)},
\qquad
z_*=0.308883577618\ldots,
\]

\[
2^{m_2}=10^{(\log_{10}2)S+o(S)},
\qquad
\delta_*=z_* -\log_{10}2
=0.007853581954\ldots.
\]

pair-max Gaussian core 选择 orientation

\[
N(\Pi)=C_L,
\qquad
\Pi^2\mid y_2+i y_3.
\]

secondary Gaussian line 为

\[
\Pi\mid A_*2^{m-2}q_c-iB_*5^{2T-m},
\]

其中

\[
A_*=g_0a_2\theta s,
\qquad
B_*=\widetilde rR_0.
\]

定义

\[
\Delta_1=
\frac{A_*2^{m-2}q_c-iB_*5^{2T-m}}{\Pi},
\]

则

\[
C_LN(\Delta_1)
=A_*^22^{2m-4}q_c^2+B_*^25^{4T-2m},
\]

\[
\log|\Delta_1|
=0.654441788809\ldots S+o(S),
\]

\[
\log N(\Delta_1)
=1.308883577618\ldots S+o(S).
\]

clean source identity 为

\[
VA_0-5^TR_0=q_c^2L_{\rm clean},
\]

且

\[
\log L_{\rm clean}=5.691116422\ldots S+o(S),
\qquad
\log(C_L,L_{\rm clean})=o(S).
\]

已有 hidden square / prefix norm：

\[
(C_LP_1)^2+P_0^2
=4\widetilde r^{\,2}5^TR_0L_{\rm clean},
\qquad
P_0=g_0a_2B\theta s.
\]

这些都是本文输入，不重复计费。

---

### 2. general overlap skeleton 精确退化为 terminal phase

**状态：`已严格完成`（frontier 条件蕴含）。**

一般 DD reduced-tail overlap 写成

\[
t=(10^mQ,b_3),
\qquad
u=\frac{10^mQ}{t},
\qquad
v=\frac{b_3}{t},
\qquad
(u,v)=1.
\]

这里的第二个变量统一记作 \(u\)，即

\[
u=\frac{10^mQ}{t}.
\]

terminal 上

\[
Q=J(s\widetilde w10^{m_2}+C_0\widetilde r)
=JUq_c\theta,
\]

\[
b_3=BJC_0q_c\theta s,
\qquad
\frac{10^m}{B}=2\cdot5^T.
\]

又因为

\[
\gcd(2\cdot5^TU,C_0s)=1,
\]

所以

\[
\boxed{t=BJq_c\theta,}
\]

\[
\boxed{u=2\cdot5^TU,\qquad v=C_0s=V,}
\]

\[
\boxed{u+v=2^HZ+5^TU=X+Y.}
\]

因此 general primitive overlap、terminal S-unit phase 与 sphere bridge 是同一对象的三个坐标图，不能当三份独立约束。

---

### 3. denominator-only quotient \(R_2\) 与 Farey entropy collapse

**状态：`已严格完成`（frontier 条件蕴含）。**

由 decimal prefix 与 phase 联立得到

\[
\boxed{
R_2=
\frac{5^T\widetilde r+A}{2^{m_2}}
\in\mathbf Z_{>0},
}
\]

\[
\boxed{
UR_2
=\widetilde r2^{H-m_2}Z+s^2\widetilde w5^{m_2},
}
\tag{R2-1}
\]

\[
\boxed{
q_c\theta2^{H-m_2}Z
-s\widetilde w5^{T+m_2}
=C_0R_2.
}
\tag{R2-2}
\]

frontier 高度为

\[
\log R_2
=1.007853581954\ldots S+o(S),
\]

\[
v_5(R_2)=0,
\qquad
v_2(R_2)=o(S),
\]

\[
\log\operatorname{core}_{10}(R_2)
=1.007853581954\ldots S+o(S).
\]

从 `(R2-1)`：

\[
\frac ZU
=
\frac{R_2}{\widetilde r2^{H-m_2}}
-
\frac{s^2\widetilde w5^{m_2}}
{\widetilde r2^{H-m_2}U}.
\]

令

\[
u_*=0.691116422382\ldots,
\qquad
U=10^{u_*S+o(S)}.
\]

沿第一次 source residue

\[
A\equiv-b\pmod{2^{m_2}}
\]

产生的所有 lift，\(Z/U\) 被压进宽度

\[
10^{-2u_*S+o(S)}
\]

的 Farey cell；分母为该尺度的不同 reduced fractions 的最小间距也在
\(10^{-2u_*S+o(S)}\) 尺度。因此

\[
\boxed{\#\{Z/U\}=10^{o(S)}.}
\]

固定 \(Z/U\) 又固定 \(R_2\)，从而固定最后 source lift。当前最强计数结论为

\[
\boxed{N_{\rm frontier}(S)=10^{o(S)}.}
\]

这仍然只是 subexponential count，不是 emptiness。

---

### 4. rational cross-resultant

**状态：`已严格完成`。**

令

\[
a=s\theta,
\qquad
A=aq_c,
\qquad
b=5^T\widetilde r.
\]

clean source 写成

\[
F(q)=L_{\rm clean}q^2+5^TR_0,
\qquad
F(q_c)=VA_0.
\]

而 \(R_2\) 来自

\[
G(q)=aq+b,
\qquad
G(q_c)=2^{m_2}R_2.
\]

resultant 为

\[
\operatorname{Res}_q(F,G)
=5^T\mathscr R_{\rm cross},
\]

其中

\[
\boxed{
\mathscr R_{\rm cross}
=a^2R_0+
\widetilde r^{\,2}5^TL_{\rm clean}.
}
\tag{RCross}
\]

对

\[
D_R=(V,R_2)
\]

有

\[
\boxed{D_R\mid\mathscr R_{\rm cross}.}
\]

而且

\[
\boxed{
\log\mathscr R_{\rm cross}=7S+o(S),
}
\]

\[
\boxed{
\log\operatorname{core}_{10}(\mathscr R_{\rm cross})
=7S+o(S),
}
\]

\[
\boxed{
\log(\mathscr R_{\rm cross},L_{\rm clean})=o(S).
}
\]

所以这是一个几乎完全 rough、并与旧 clean-source rough core 渐近互素的 \(7S\)-height 整数。

#### 4.1 cross-resultant cofactor 的固定 \(5S\) gap

写

\[
D=D_R,
\qquad
V=De,
\qquad
R_2=Df,
\qquad
\mathscr R_{\rm cross}=DK.
\]

则

\[
\boxed{
q_c^2K
=\widetilde r^{\,2}5^TeA_0
+2^{m_2}R_0f(A-b).
}
\tag{CR9}
\]

亦即

\[
\boxed{
\widetilde r^{\,2}5^TeA_0-q_c^2K
=2^{m_2}R_0f(b-A)>0.
}
\]

若

\[
\eta=\frac{\log D}{S},
\]

则两主项高度均为

\[
(7.617767155236-\eta)S+o(S),
\]

correction 高度只有

\[
(2.617767155236-\eta)S+o(S).
\]

因此 gap 精确为

\[
\boxed{5S+o(S),}
\]

且与 \(\eta\) 无关。

#### 4.2 与 near-axis norm 的审计

置

\[
C_*:=\frac{g_0a_2B}{2},
\qquad
N_{\rm ax}:=C_*^2+R_0^2.
\]

prefix norm 给出

\[
\boxed{
R_0\mathscr R_{\rm cross}
-a^2N_{\rm ax}
=\left(\frac{C_LP_1}{2}\right)^2.
}
\tag{Hidden-cross}
\]

所以不能把 \((N_{\rm ax},\mathscr R_{\rm cross})\) 当独立 gcd obstruction；它正被 hidden square 支付。

---

### 5. rational sign channels 与 \(C_L\) 分解

**状态：`已严格完成`。**

定义

\[
\boxed{R_+=b+A=2^{m_2}R_2,\qquad R_-=b-A,}
\]

\[
\boxed{D_+=(V,R_+),\qquad D_-=(V,R_-).}
\]

由于

\[
(R_+,R_-)\mid2A,2b,
\]

而 \((C_L,q_c)=1\) 且 coefficient overlaps 只有 \(10^{o(S)}\)，得到

\[
\boxed{(D_+,D_-)=10^{o(S)}.}
\]

cross-resultant 还满足

\[
\boxed{
q_c^2\mathscr R_{\rm cross}
=\widetilde r^{\,2}5^TVA_0-R_0R_+R_-.
}
\]

因此 main prime-power 高度上

\[
\boxed{
(C_L,\mathscr R_{\rm cross})
=D_+D_-\cdot10^{o(S)}.
}
\]

定义

\[
\boxed{
C_G=
\frac{C_L}{(C_L,\mathscr R_{\rm cross})},
}
\]

则

\[
\boxed{C_L=D_+D_-C_G\cdot10^{o(S)}.}
\]

于是 terminal moving core 被分成：

1. **full rational-contact branch**：\(D_+D_-=C_L^{1-o(1)}\)；
2. **genuine-Gaussian branch**：\(C_G=10^{\varepsilon S+o(S)}\) 对某个 \(\varepsilon>0\)。

#### 5.1 sign 同时固定 Gaussian orientation

在 \(D_+\) 上 \(A\equiv-b\)，secondary line specialization 给

\[
\boxed{\Pi_+\mid C_*+iR_0,\qquad N(\Pi_+)=D_+.}
\]

在 \(D_-\) 上 \(A\equiv b\)，得到

\[
\boxed{\Pi_-\mid C_*-iR_0,\qquad N(\Pi_-)=D_-.}
\]

所以 rational sign 不只是 rational residue；它还固定 pair-max Gaussian orientation。

---

### 6. sign-Farey reduction

**状态：`已严格完成`。**

令

\[
c=\widetilde r5^{T-m_2}U,
\qquad
d=s^2\widetilde w2^{m_2},
\]

\[
\boxed{J_+=c+d,\qquad J_-=c-d.}
\]

D1 直接给

\[
\boxed{UR_+-5^{m_2}J_+=V\widetilde r,}
\tag{SF+}
\]

\[
\boxed{UR_--5^{m_2}J_-=-V\widetilde r.}
\tag{SF-}
\]

因此

\[
\boxed{D_+\mid J_+,\qquad D_-\mid J_-.}
\]

写

\[
R_\pm=D_\pm h_\pm,
\qquad
J_\pm=D_\pm j_\pm.
\]

在 full rational-contact branch 中令

\[
E=D_+D_-,
\qquad
V=Ee_0,
\qquad
\log e_0=o(S).
\]

则

\[
\boxed{
Uh_+-5^{m_2}j_+=D_-e_0\widetilde r,
}
\tag{SF-red+}
\]

\[
\boxed{
Uh_--5^{m_2}j_-=-D_+e_0\widetilde r.
}
\tag{SF-red-}
\]

两个 reduced endpoints 满足

\[
\boxed{
j_-h_+-j_+h_-
=2e_0\widetilde r^{\,2}5^{T-m_2}.}
\tag{SF-det}
\]

在 full rational branch 中右端 rough core 只有 \(10^{o(S)}\)；但这个 determinant 本身不能自动接收 Bad Gaussian orientation，见第 17 节。

#### 6.1 contact 深度几乎处处是 full depth

若 \(p^h\Vert C_L\)，记 \(t_p\) 为它进入 \(D_+D_-\) 的 rational-contact depth。因为

\[
\log(D_+D_-)=\log C_L+o(S),
\]

所以

\[
\sum_{p^h\Vert C_L}(h-t_p)\log p=o(S).
\]

因此除去 \(10^{o(S)}\) prime mass 后

\[
\boxed{t_p=h.}
\]

full rational branch 的主质量是完整 prime-power contact，不是大量浅 contact 的总和。

---

### 7. 固定 rational-contact 曲面

**状态：`已严格完成`。**

定义

\[
\boxed{
x=\frac Ab,\qquad y=\frac cd,
\qquad
z=\frac{\widetilde r2^HZ}{s^2\widetilde w10^{m_2}}.}
\]

由 D1：

\[
xy
=1+
\frac{C_0\widetilde r}{s\widetilde w10^{m_2}},
\]

由 phase：

\[
z
=y+
\frac{C_0\widetilde r}{s\widetilde w10^{m_2}}.
\]

消去 remainder：

\[
\boxed{z=xy+y-1,\qquad z+1=y(x+1).}
\tag{Surface}
\]

几何意义：

- \(D_-\)：\(A\equiv b\)、\(c\equiv d\)，所以
  \[
  (x,y,z)\equiv(1,1,1);
  \]
- \(D_+\)：\(A\equiv-b\)、\(c\equiv-d\)，所以
  \[
  (x,y,z)\equiv(-1,-1,-1).
  \]

rational-contact branch 因而是固定曲面上对两个固定点的高阶 p-adic contact。

---

### 8. first-order contact 的高度预算精确饱和

**状态：`已严格完成`（frontier 高度计算）。**

令 \(S_0=\{\infty,2,5\}\)。terminal moving coefficients 的 outside-\(S_0\) 高度只有 \(o(S)\)。

\[
\boxed{
h_{\bar S_0}(x)
=0.308883577618\ldots S+o(S),}
\]

\[
\boxed{
h_{\bar S_0}(y)
=0.691116422382\ldots S+o(S).}
\]

故

\[
\boxed{
h_{\bar S_0}(x)+h_{\bar S_0}(y)=S+o(S).}
\tag{Height-critical}
\]

而 full rational-contact branch 正好满足

\[
\boxed{\log(D_+D_-)=S+o(S).}
\]

因此 first-order rational contact 已经把两个 rational variables 的全部 prime-to-\(\{2,5\}\) height budget 用满。

结论不是“Subspace theorem 失效”，而是：**普通 first-order GCD / Ridout / fixed-target Subspace 型估计在 leading order 只能达到临界等号，不能自动给严格线性矛盾。**

---

### 9. standalone blow-up / tangent condition 的审计

**状态：`失效/降级`。**

rational contact 与 terminal Gaussian double root 联立后，确实可在每个固定点构造 oriented 二阶 tangent condition；但把两 sign 统一后，它仍被 hidden square 吃掉。

令

\[
M=\widetilde r^{\,2}5^TL_{\rm clean},
\qquad
S_0^{\rm ax}=C_*-iR_0,
\]

并定义

\[
\Gamma=\Pi_-\overline{\Pi_+}.
\]

由第 5.1 节

\[
\Gamma\mid S_0^{\rm ax}.
\]

两个 sign 的二阶 condition 可统一成

\[
\Gamma^2\mid Q,
\qquad
Q=2C_*a^2+i(M-a^2R_0).
\]

但 hidden square 精确给出

\[
\boxed{
R_0Q
=i\left(
 aS_0^{\rm ax}-\frac{iC_LP_1}{2}
\right)
\left(
 aS_0^{\rm ax}+\frac{iC_LP_1}{2}
\right).
}
\tag{Tangent-collapse}
\]

因为 \(\Gamma\mid S_0^{\rm ax}\) 且 \(\Gamma\mid C_L\)，两因子自动各含一份 \(\Gamma\)。所以 \(\Gamma^2\mid Q\) 不是第二份独立 height。

---

### 10. denominator-transformed Gaussian quotient

**状态：定义与恒等式 `已严格完成`；若只做同-prime norm resultant 则 `失效/降级`。**

令

\[
e=m+m_2-2T>0.
\]

定义

\[
L_U
=g_0a_2s^2\widetilde w
2^{m+m_2-2}5^e
-i\widetilde rR_0U,
\]

\[
\Pi\mid L_U,
\qquad
\Delta_U=L_U/\Pi.
\]

frontier 上

\[
\boxed{
\log|\Delta_U|
=0.691116422382\ldots S+o(S),}
\]

\[
\boxed{
\log N(\Delta_U)
=1.382232844764\ldots S+o(S).}
\]

相应 Z-side quotient \(\Delta_Z\) 满足

\[
\boxed{
2^{m_2}\Delta_Z-5^T\Delta_U
=-i\widetilde rR_0s\frac{C_0}{C_L}\bar\Pi.
}
\tag{UZ-transfer}
\]

同时

\[
\boxed{
U\Delta_1-5^{2T-m}\Delta_U
=g_0a_2s\widetilde r2^{m-2}
\frac{C_0}{C_L}\bar\Pi.
}
\tag{U1-transfer}
\]

D1/R22 与 secondary line 的最自然 same-prime resultants 都精确退回 \(N(\Delta_1)\)，而 \(\Delta_U,\Delta_Z\) 的 cross determinant 只产生 \((C_0/C_L)\bar\Pi\)。所以“再造 Gaussian quotient 后直接取 norm/resultant”不增加 rank。

真正留下的新信息是 repeat / non-repeat orientation allocation。

---

### 11. Bad/Good 分解

**状态：定义及必要条件 `已严格完成`；最终 closure `待证`。**

对 \(D_+\)、\(D_-\) 的 main oriented prime-power，第一份 \(\Pi_\pm\) 已经从 \(L_U\) 中除去。

定义 \(B_\pm\) 为那些在 quotient \(\Delta_U\) 中**同一 orientation 再次出现**的 prime-power 部分，令

\[
G_\pm=D_\pm/B_\pm.
\]

则

\[
\log(B_+B_-)+\log(G_+G_-)=S+o(S).
\]

故至少发生一个：

\[
\boxed{
\log(B_+B_-)
\ge\frac12S-o(S)
}
\tag{Bad}
\]

或

\[
\boxed{
\log(G_+G_-)
\ge\frac12S-o(S).
}
\tag{Good}
\]

#### 11.1 single-slot orientation allocation

由 `(U1-transfer)`、`(UZ-transfer)`，除去 \(C_0/C_L\) 等 \(10^{o(S)}\) overlap 后：

\[
\boxed{
\Pi_B\mid\Delta_U
\Longrightarrow
(\Pi_B,\Delta_1)_{\mathbf Z[i]}
=(\Pi_B,\Delta_Z)_{\mathbf Z[i]}
=1
}
\]

按 main oriented prime mass 理解。

所以 Bad mass 一旦重新进入 \(\Delta_U\)，就不能同 orientation 再进入 \(\Delta_1\) 或 \(\Delta_Z\)。这是真正的 **single-slot allocation**，但单独还不是容量矛盾。

---

### 12. full rational-contact cofactor Lorentz system

**状态：`已严格完成`。这是目前 rational branch 的核心新结构。**

定义

\[
\boxed{
H_R=h_+h_-
=\frac{b^2-A^2}{E},}
\]

\[
\boxed{
H_J=j_+j_-
=\frac{c^2-d^2}{E},}
\]

\[
\boxed{
S_c=\frac{bc-Ad}{E},}
\]

\[
\boxed{
T_c=e_0\widetilde r^{\,2}5^{T-m_2}.}
\]

Brahmagupta/Lorentz 恒等式：

\[
\boxed{
S_c^2-H_RH_J=T_c^2.
}
\tag{CF1}
\]

由 `(SF-red+)`、`(SF-red-)` 消元：

\[
\boxed{
5^{m_2}H_J-US_c=e_0\widetilde r\,d,
}
\tag{CF2}
\]

\[
\boxed{
5^{m_2}S_c-UH_R=e_0\widetilde r\,A.
}
\tag{CF3}
\]

等价地

\[
\boxed{
\begin{pmatrix}
H_R&S_c\\
S_c&H_J
\end{pmatrix}
\binom{U}{-5^{m_2}}
=-e_0\widetilde r
\binom{A}{d}.
}
\tag{CF-matrix}
\]

矩阵行列式为 \(-T_c^2\)。取 adjugate：

\[
\boxed{
H_JA-S_cd
=e_0\widetilde r^{\,3}5^{2(T-m_2)}U,
}
\tag{CF4}
\]

\[
\boxed{
S_cA-H_Rd
=e_0\widetilde r^{\,3}5^{2T-m_2}.
}
\tag{CF5}
\]

#### 12.1 exact \(2S\) cancellation

frontier 高度：

\[
\log H_R=1.617767155236\ldots S+o(S),
\]

\[
\log H_J=1.602059991328\ldots S+o(S),
\]

\[
\log S_c=1.609913573282\ldots S+o(S),
\]

\[
\log T_c=0.609913573282\ldots S+o(S).
\]

于是 `(CF1)` 两主平方项高度为

\[
3.219827146564\ldots S+o(S),
\]

而差 \(T_c^2\) 只有

\[
1.219827146564\ldots S+o(S).
\]

`(CF2)` 两主项高度均为

\[
2.301029995664\ldots S+o(S),
\]

右端只有

\[
0.301029995664\ldots S+o(S).
\]

`(CF3)` 两主项高度均为

\[
2.308883577618\ldots S+o(S),
\]

右端只有

\[
0.308883577618\ldots S+o(S).
\]

因此两条都是精确 \(2S+o(S)\) cancellation，且两个 residual exponent 之差正是

\[
\boxed{\delta_*=0.007853581954\ldots.}
\]

#### 12.2 generic real + 5-adic proximity 又精确临界

`(CF2)` 提供 real place 的 \(2S\) proximity，而 `(CF4)` 的

\[
5^{2(T-m_2)}
\]

提供

\[
1.219827146564\ldots S
\]

的 5-adic depth。两者相加恰为

\[
3.219827146564\ldots S
=2\log S_c+o(S).
\]

所以 generic Ridout/Subspace 型 height inequality 在 cofactor 层仍精确达到临界等号。最终 closure 必须使用 Bad/Good 的第三信息。

---

### 13. Bad repeat 的精确 quotient / numerator / digital / concat 投影

**状态：`已严格完成`。**

#### 13.1 quotient residual

对 \(D_+\) contact，\(A\equiv-b\)、\(c\equiv-d\)。令

\[
N_{\rm ax}=C_*^2+R_0^2,
\qquad
n_+=N_{\rm ax}/D_+.
\]

把 \(N(L_U)\) 在该 root 处精确一阶展开：

\[
\boxed{
B_+\mid d n_+-2R_0^2j_+.
}
\tag{Bad-local+}
\]

在 \(D_-\) contact 同理：

\[
\boxed{
B_-\mid d n_-+2R_0^2j_-.
}
\tag{Bad-local-}
\]

#### 13.2 numerator reconstruction projection

把 `(Bad-local+)`、`(Bad-local-)` 与 pair-max square / clean-source quotient 联立，消去 \(n_\pm\)：

\[
\boxed{
B_+\mid UA_0-2R_0,
}
\tag{Bad-num+}
\]

\[
\boxed{
B_-\mid UA_0+2R_0.
}
\tag{Bad-num-}
\]

#### 13.3 digital Gaussian projection

exact reconstruction 为

\[
UA_0+R_0=g_0B10^dA_{12}.
\]

对 \(D_+\)，`(Bad-num+)` 给

\[
g_0B10^dA_{12}\equiv3R_0,
\]

配合

\[
\Pi_+\mid C_*+iR_0
\]

得到

\[
\boxed{
\Pi_{B,+}
\mid3a_2+2i10^dA_{12}.
}
\tag{Bad-G+}
\]

对 \(D_-\)，`(Bad-num-)` 给

\[
g_0B10^dA_{12}\equiv-R_0,
\]

配合

\[
\Pi_-\mid C_*-iR_0
\]

得到

\[
\boxed{
\Pi_{B,-}
\mid a_2+2i10^dA_{12}.
}
\tag{Bad-G-}
\]

取范数：

\[
\boxed{
B_+\mid9a_2^2+4\,10^{2d}A_{12}^2,
}
\]

\[
\boxed{
B_-\mid a_2^2+4\,10^{2d}A_{12}^2.
}
\]

两个 digital Gaussian carriers 的差只有 \(2a_2\)。main pair-max primes 不整除 \(a_2\)，故两侧 Bad carrier 只有 \(10^{o(S)}\) overlap。

令

\[
Y=2\,10^dA_{12}.
\]

则

\[
(a_2+iY)(3a_2+iY)
=(2a_2+iY)^2-a_2^2.
\]

这是来自 decimal prefix 的 near-square Gaussian factorization；它不同于 sphere hidden square。

#### 13.4 full concat numerator projection

terminal exact identities：

\[
g_0(\alpha-a_3)=2\cdot5^T(UA_0+R_0),
\]

\[
VA_0-g_0a_3=2\cdot5^TR_0.
\]

在 \(D_\pm\mid V\) 上消去 \(g_0\) 后等价于

\[
R_0\alpha+UA_0a_3\equiv0\pmod{D_\pm}.
\]

所以 `(Bad-num+)`、`(Bad-num-)` 分别给

\[
\boxed{
B_+\mid\alpha+2a_3
=A_{12}10^{n_3}+3a_3,
}
\tag{Bad-concat+}
\]

\[
\boxed{
B_-\mid\alpha-2a_3
=A_{12}10^{n_3}-a_3.
}
\tag{Bad-concat-}
\]

同一 Bad prime mass 因而同时出现在 denominator quotient、prefix digital Gaussian carrier 和 full concat numerator residue 三个坐标图中。

---

### 14. Bad 的 cofactor projection

**状态：`已严格完成`。**

在 full rational branch 定义

\[
\boxed{
N_c=\frac{N_{\rm ax}}{E}.
}
\]

因为

\[
n_+=D_-N_c,
\qquad
n_-=D_+N_c,
\]

且由 `(SF-det)`

\[
j_+h_-=S_c-T_c,
\qquad
j_-h_+=S_c+T_c,
\]

把 `(Bad-local+)` 乘 \(h_-\)，并用

\[
R_-\equiv2b\pmod{D_+},
\]

得到

\[
\boxed{
B_+\mid
bdN_c-R_0^2S_c+R_0^2T_c.
}
\tag{Bad-CF+}
\]

同理

\[
\boxed{
B_-\mid
bdN_c+R_0^2S_c+R_0^2T_c.
}
\tag{Bad-CF-}
\]

统一为

\[
\boxed{
B_\sigma\mid
bdN_c-\sigma R_0^2S_c+R_0^2T_c,
\qquad
\sigma\in\{+1,-1\}.
}
\tag{Bad-CF}
\]

这里 \(\sigma\) 明确表示 channel label \(D_\sigma\)。

这是当前 Bad branch 最重要的 transfer：\(\Delta_U,q_c,A_0,A_{12},\Pi\) 都从 congruence 中消失，只剩 cofactor 坐标

\[
(N_c,S_c,T_c).
\]

---

### 15. 现成的 \(N_c\) elimination

**状态：`已严格完成`；与 `(Bad-CF)` 的最终联合消元 `待证`。**

secondary norm：

\[
C_LN(\Delta_1)
=g_0^2a_2^22^{2m-4}A^2
+\widetilde r^{\,2}R_0^25^{4T-2m}.
\]

而

\[
EH_R=b^2-A^2,
\qquad
EN_c=C_*^2+R_0^2.
\]

消去 \(A^2\)：

\[
\boxed{
\widetilde r^{\,2}5^{4T-2m}N_c
-g_0^2a_2^22^{2m-4}H_R
=
\frac{C_L}{E}N(\Delta_1).
}
\tag{Nc-elim}
\]

左侧两个主项高度都为

\[
3.308883577618\ldots S+o(S),
\]

右端只有

\[
1.308883577618\ldots S+o(S).
\]

所以 `(Nc-elim)` 本身又是精确 \(2S+o(S)\) cancellation。

下一步不是再制造 quotient，而是：

1. 用 `(Nc-elim)` 从 `(Bad-CF)` 消掉 \(N_c\)；
2. 保留 \(B_\sigma\) 的 oriented prime-power divisibility；
3. 用第 11.1 节 single-slot allocation 阻止同一 Bad mass 被 \(N(\Delta_1)\) 再次支付；
4. 争取把第三 linear proximity 完全落到 \((H_R,S_c,T_c)\) 上。

若能做到，`(CF1)`--`(CF5)` 已经精确 critical，任何额外正线性的 Bad modulus 都将成为真正 surplus。

---

### 16. source/projective 独立性审计

**状态：`已严格完成`，主要用于防止重复计费。**

primitive quadratic root \((\mu,\nu)\)、\(\Delta_1\)、recovery gcd 与 projective source quotient 在 terminal 上有精确互相恢复关系：

\[
\log\mu
=0.654441788809\ldots S+o(S),
\]

\[
\log\nu
=1.154441788809\ldots S+o(S),
\]

而 recovery common factor 只有 \(o(S)\) rough height。

从 prefix norm 主 rough divisor 抽出 source Gaussian factor \(\Lambda_{\rm src}\) 后，得到

\[
K_{\rm src}
=\frac{X_0+iY_0}{\Lambda_{\rm src}},
\qquad
\log|K_{\rm src}|
=0.654441788809\ldots S+o(S),
\]

\[
\log\operatorname{core}_{10}N(K_{\rm src})=o(S).
\]

另一方面

\[
\log\operatorname{core}_{10}N(\Delta_1)
=1.308883577618\ldots S+o(S),
\]

所以

\[
\boxed{
\log N\bigl(
\gcd_{\mathbf Z[i]}(K_{\rm src},\Delta_1)
\bigr)=o(S).
}
\]

这是一个真实的 transverse coprimality；但 \((\mu,\nu),K_{\rm src},\Delta_1\) 本身并不是三份独立 terminal entropy。

---

### 17. 已严格判死或降级的路线

这一节必须保留，防止后续 agent 重开死路。

#### 17.1 standalone blow-up tangent：`失效/降级`

见 `(Tangent-collapse)`。二阶 oriented contact 被 hidden square 自动提供，不能当第二份 local height。

#### 17.2 cross-resultant 与 near-axis norm 直接 gcd：`失效/降级`

见 `(Hidden-cross)`。两者差精确等于 \((C_LP_1/2)^2\)，不是独立 targets。

#### 17.3 D1/R22 与 secondary line 的同-prime resultant：`失效/降级`

最自然的 U-side、Z-side resultants 都精确退回 secondary norm；\(\Delta_U,\Delta_Z\) 的 cross determinant 只由 \((C_0/C_L)\bar\Pi\) 支付。

#### 17.4 `Bad -> bottom determinant` bridge：`失效/降级`

曾尝试证明 digital Gaussian Bad carrier 会强迫

\[
B_\sigma\mid j_-h_+-j_+h_-.
\]

这不能由 primitive carrier tetrahedron 推出。main \(C_L\)-prime 上已有

\[
v_p(\Delta_{12})=v_p(\Delta_{13})=0.
\]

carrier tetrahedron 只给 determinant valuation 的 ultrametric order type，不会凭空把 Bad orientation 送到底边。

#### 17.5 \(t_p+b_p\le h_p\)：`失效/降级`

full rational branch 已经几乎处处有 \(t_p=h_p\)。Bad repeat 是除去完整 \(p^{h_p}\) contact 后在 Gaussian quotient 中产生的新 cancellation，并不由 \(h_p-t_p\) 支付。

#### 17.6 单靠 \(C_0\) 与 digital norm 的 gcd：`失效/降级`

Bad primes 本来就在 \(C_L\mid C_0\) 主 core 中。reconstruction 只把 \(A_{12}\) 固定为 p-adic residue，并不禁止

\[
4\,10^{2d}A_{12}^2+c_\sigma a_2^2
\equiv0\pmod{p^r}.
\]

不能从 reducedness 直接推出这个 gcd 只有 \(10^{o(S)}\)。

#### 17.7 模 \(A_0\) 的“小 gcd 强迫小误差整除”：`失效/降级`

从

\[
A_0\mid q_c^2K-E
\]

与 \((A_0,q_c^2K)\) 小，不能推出 \(A_0/g\mid E\)。正确的 rational-spacing 分析说明 small gcd 允许更细 spacing；需要的是 large common divisor。

#### 17.8 generic first-order GCD / Subspace / Ridout closure：`失效/降级`

`(Height-critical)` 与第 12.2 节都显示 leading-order budget 精确饱和。继续套同类型 generic theorem 只能再次得到临界等号。

#### 17.9 first-order hyperbolic determinants：`失效/降级`

\[
\begin{pmatrix}b&A\\c&d\end{pmatrix}
\]

的 \(R_\pm,J_\pm\) 一阶代数满足 Brahmagupta/Plücker 恒等式，所有自然 cross determinants 最终退回 `(SF-det)`。这个 first-order \(2\times2\) algebra 已闭合。

---

### 18. 当前精确分支图

#### 18.1 genuine-Gaussian branch

若

\[
\boxed{C_G=10^{\varepsilon S+o(S)}}
\]

对某个 \(\varepsilon>0\)，则这些 main primes 不满足 \(A\equiv\pm b\)。所有 rational denominator-contact resultants 在它们处为单位。

这支需要真正新的 Gaussian/projective same-prime elimination；本文尚未关闭。

#### 18.2 full rational-contact branch

若

\[
\boxed{D_+D_-=C_L^{1-o(1)},}
\]

则先进入 exact critical cofactor system `(CF1)`--`(CF5)`，再分：

##### Bad

\[
\log(B_+B_-)
\ge\frac12S-o(S).
\]

大 prime mass 同时满足：

- denominator repeat `(Bad-local+)` / `(Bad-local-)`；
- numerator reconstruction `(Bad-num+)` / `(Bad-num-)`；
- digital Gaussian `(Bad-G+)` / `(Bad-G-)`；
- full concat `(Bad-concat+)` / `(Bad-concat-)`；
- cofactor third linear form `(Bad-CF)`。

当前首选 closure 是 `(Bad-CF)+(Nc-elim)+single-slot orientation`。

##### Good

\[
\log(G_+G_-)
\ge\frac12S-o(S).
\]

至少半个 \(C_L\)-height 在 full rational contact 后与 \(N(\Delta_U)\) 横截。这一支不能再靠 first-order rational contact 收费；应直接追踪 \(N(\Delta_U)\) rough core 的来源，并与 \((C_L,L_{\rm clean})=10^{o(S)}\)、source/projective transversality 联立。

---

### 19. 当前首选证明任务

**状态：`待证`。**

下一次工作不要再扩对象。首选目标固定为：

#### 19.1 Bad branch

从

\[
B_\sigma\mid
bdN_c-\sigma R_0^2S_c+R_0^2T_c
\]

和

\[
\widetilde r^{\,2}5^{4T-2m}N_c
-g_0^2a_2^22^{2m-4}H_R
=
\frac{C_L}{E}N(\Delta_1)
\]

消掉 \(N_c\)，但**不要先取 norm 丢掉 orientation**。

成功标准是得到只含

\[
H_R,\quad S_c,\quad T_c
\]

与 \(o(S)\)-height coefficients 的第三 linear form，并证明 Bad modulus 的正线性高度不能由 \(N(\Delta_1)\) 再次支付。

目标必须是可逐行核验的严格 surplus，例如

\[
0<|\Theta|<M\le|\Theta|,
\]

或

\[
\log M\ge cS+o(S),
\qquad
\log|\Theta|<(c-\varepsilon)S+o(S).
\]

#### 19.2 若 Bad 消元再次退化

若上述消元精确回到 `(CF1)`--`(CF5)` 或 hidden square，立即停止在 rational first-order algebra 中继续造 eliminant，转向 genuine-Gaussian branch。

---

### 20. 状态总表

- **`已严格完成`（仅 frontier 条件蕴含）**：general overlap 精确退化、\(R_2\) matrix、Farey subexponential compression、rational cross-resultant、sign-channel 分解、full-depth rational contact、fixed surface、critical height budget、cofactor Lorentz system `(CF1)`--`(CF5)`、Bad 的 quotient/numerator/digital/concat/cofactor 多重投影、`(Nc-elim)`、single-slot orientation allocation、source/projective transversality audit。
- **`失效/降级`**：standalone tangent/blow-up、cross-resultant 与 near-axis norm 直接 gcd、U/Z-side same-prime resultants、Bad 到 bottom determinant、\(t+b\le h\)、单靠 \(C_0\)-digital norm gcd、错误的模 \(A_0\) small-gcd argument、generic first-order GCD/Subspace/Ridout、继续挖 first-order hyperbolic determinants。
- **`待证`**：Bad 的 \(N_c\) oriented elimination、Good 的 transverse rough-core closure、genuine-Gaussian branch 的 uniform same-prime elimination。
- **全局状态不变**：DD 尚未证明为空；当前最强全局渐近结论仍为
  \[
  \limsup_{\rm DD}\frac{n_3}{S}
  \le6.308883577618\ldots,
  \]
  其阈值依赖 Schmidt Subspace Theorem 且非有效；本文新增的所有 \(o(S)\) 与 rational-contact 结论都只在假想 frontier sequence 上使用。

---

## 3. DD frontier 5-adic factor allocation — 2026-08-16

> 整合来源：`dd-frontier-five-adic-forcing-2026-08-16.md`。以下正文保留该来源的原始证明状态和审计边界。

> 本文接续 [`frontier.md`](frontier.md)，并专门回到假想
> \[
> \frac{n_3}{S}\to6.308883577618\ldots
> \]
> 的 terminal frontier。
>
> **修正说明：**早期版本曾把 \(H-y_3\) 超出 \((H,y_3)\) common scale 的深度直接判成 primitive Gaussian angular depth。该跳步不成立，因为
> \(y_1,y_2\) 自身还可能携带大的共同 ghost scale。本文保留正确的 factor-asymmetry 结论，并把最终状态改写成 exact `common-ghost + angular` 分配。
>
> **状态边界：**本文不关闭 DD frontier；它精确限制 5-adic 深度可以藏在哪里。

---

### 1. terminal 5-adic data

沿用 terminal overlap：

\[
b_3=BJC_0q_c\theta s,
\qquad
\frac{10^m}{B}=2\cdot5^T.
\tag{1.1}
\]

frontier 比例为

\[
\frac mS\to2.808883577618\ldots,
\]

\[
\frac TS\to1.872589051745\ldots,
\]

\[
m_1+m_2=S.
\tag{1.2}
\]

sphere bridge 已给出

\[
\boxed{H-y_3=2\cdot5^T\rho_0,}
\tag{1.3}
\]

其中

\[
\log\rho_0=o(S).
\]

因此

\[
\boxed{v_5(H-y_3)=T+o(S).}
\tag{1.4}
\]

---

### 2. 第三分母自身已经含有 \(5^{m-T}\)

由 `(1.1)`：

\[
B=\frac{10^m}{2\cdot5^T}
=2^{m-1}5^{m-T}.
\]

所以

\[
\boxed{v_5(b_3)\ge m-T.}
\tag{2.1}
\]

记

\[
e_i=v_5(b_i),
\qquad
E=\max(e_1,e_2,e_3).
\]

全局定义

\[
q=\operatorname{lcm}(b_1,b_2,b_3)
\]

给出

\[
\boxed{v_5(q/b_3)=E-e_3.}
\tag{2.2}
\]

sufficiently large frontier 上 `(2.1)` 给 \(e_3>0\)，又

\[
(a_3,b_3)=1,
\]

故

\[
v_5(a_3)=0.
\]

因此

\[
y_3=a_3\frac q{b_3}
\]

满足

\[
\boxed{v_5(y_3)=E-e_3.}
\tag{2.3}
\]

---

### 3. prefix digit length 给 \(y_3\) 的 5-depth 一个严格线性上界

对 \(i=1,2\)，因为

\[
1\le b_i<10^{m_i},
\]

若 \(5^{e_i}\mid b_i\)，则

\[
5^{e_i}<10^{m_i},
\]

故

\[
\boxed{e_i<\frac{m_i}{\log_{10}5}.}
\tag{3.1}
\]

又

\[
m_1+m_2=S,
\]

所以

\[
\boxed{
\max(e_1,e_2)
<\frac{S}{\log_{10}5}.
}
\tag{3.2}
\]

由 `(2.2)` 和 `(2.1)`：

\[
\begin{aligned}
E-e_3
&\le
\max\left(
0,
\max(e_1,e_2)-e_3
\right)\\
&<
\max\left(
0,
\frac{S}{\log_{10}5}-(m-T)
\right).
\end{aligned}
\]

因此

\[
\boxed{
\frac{v_5(y_3)}S
\le
\frac1{\log_{10}5}
-\frac mS+\frac TS+o(1).
}
\tag{3.3}
\]

代入 frontier 极限：

\[
\frac1{\log_{10}5}
=1.430676558073\ldots,
\]

得到

\[
\boxed{
\limsup\frac{v_5(y_3)}S
\le
0.494382032200\ldots.
}
\tag{3.4}
\]

令

\[
s_5=\min(v_5(H),v_5(y_3)).
\]

则

\[
\boxed{
\limsup\frac{s_5}{S}
\le0.494382032200\ldots.
}
\tag{3.5}
\]

---

### 4. sphere 两因子的 5-adic valuation 被完全定向

由 `(1.4)` 与 `(3.5)`：

\[
\boxed{
\frac{v_5(H-y_3)-s_5}{S}
\ge
1.378207019545\ldots-o(1).
}
\tag{4.1}
\]

所以 sufficiently large frontier 上

\[
\boxed{v_5(H-y_3)>s_5.}
\tag{4.2}
\]

对奇素数 \(5\) 使用 elementary two-factor lemma：若

\[
s=\min(v_5(A),v_5(B)),
\qquad
v_5(A-B)>s,
\]

则

\[
v_5(A+B)=s.
\]

取

\[
A=H,
\qquad B=y_3,
\]

得到

\[
\boxed{v_5(H+y_3)=s_5.}
\tag{4.3}
\]

因此

\[
\boxed{
v_5(y_1^2+y_2^2)
=T+s_5+o(S).}
\tag{4.4}
\]

这里必须强调：`(4.4)` 只规定总二平方和 valuation；它尚未区分 \(y_1,y_2\) 的共同 ghost scale 与 primitive angle。

---

### 5. 正确的 `common-ghost + angular` 分解

写

\[
g=(y_1,y_2),
\qquad
y_1=gX,
\qquad
y_2=gY,
\qquad(X,Y)=1.
\]

定义

\[
r_5=v_5(g),
\qquad
\omega_5=v_5(X^2+Y^2).
\]

则 `(4.4)` 精确给出

\[
\boxed{
2r_5+\omega_5
=T+s_5+o(S).
}
\tag{5.1}
\]

所以 frontier 的主 5-adic budget 只能分配到两个槽：

1. `common-ghost`：\(2r_5\)；
2. `primitive angular`：\(\omega_5\)。

原先从 `(4.1)` 直接推出 \(\omega_5\) 线性大的论证是错误的，因为 \(r_5\) 也可以是线性大的。

---

### 6. projective denominator 对 angular 深度仍然零收费

projective denominator 的 exact formula 为

\[
Z_0=\frac{H+y_3}{(g,H+y_3)}.
\]

由 `(4.3)`：

\[
\boxed{
v_5(Z_0)
=s_5-\min(r_5,s_5)
=\max(0,s_5-r_5).}
\tag{6.1}
\]

这条式子仍然是一个真实的新简化：\(v_5(Z_0)\) **完全不含** \(\omega_5\)。

所以无论 `(5.1)` 中 angular slot 占多少，primitive angular depth 都不能再被 \(Z_0\) 重复支付。

特别地：

- 若 \(r_5\ge s_5\)，则
  \[
  \boxed{v_5(Z_0)=0;}
  \]
- 若 \(r_5<s_5\)，则
  \[
  v_5(Z_0)=s_5-r_5
  \le0.494382032200\ldots S+o(S).
  \]

---

### 7. 与 angular/bottom exclusion 合并后的正确状态

[`frontier.md`](frontier.md) 的 conditional angular conclusions 保持有效：若

\[
\omega_5>0,
\]

则 primitive bottom carrier edge 不接收该 angular depth；determinant ultrametric 又阻止它同时进入两条 independent upper carrier edges；且当 \(5\mid L\) 时两个 normalized tail moving factors 都是 5-adic units。

因此当前 frontier 5-adic 状态应写成：

\[
\boxed{
2r_5+\omega_5=T+s_5+o(S),
\qquad
s_5\le0.494382032200\ldots S+o(S),
}
\]

其中：

- \(\omega_5\) 不能再次支付 \(Z_0\) 或 simultaneous carrier contact；
- 尚未关闭的主要逃逸是线性大的 common-ghost scale \(r_5\)，以及 angular depth 只停留在单一允许槽中的情形。

换言之，frontier 的 5-adic 问题已经从“common scale / angular / projective / moving factor 多槽混合”压成了：

\[
\boxed{
\text{common ghost scale }r_5
\quad\cup\quad
\text{single-slot angular remainder }\omega_5.
}
\]

下一步应优先把 \(r_5\) 用 denominator overlap \(g_*\)、primitive recovery 与 reducedness 精确参数化；若能证明 \(r_5\) 的线性部分必须进入已被 pair-max / carrier 使用的同一 denominator slot，就会产生真正的 capacity surplus。

---

## 4. DD frontier primitive 5-adic baseline — 2026-08-16

> 整合来源：`dd-frontier-five-adic-baseline-2026-08-16.md`。以下正文保留该来源的原始证明状态和审计边界。

> 本文继续 [`frontier.md`](frontier.md) 修正后的 `common-ghost + angular` 分解。
> 适用范围是同一个假想 \(6.308883577618\ldots\) terminal frontier，并采用其规范化取向
> \[
> (m_1,m_2;n_1,n_2)
> =(o(S),S-o(S);S-o(S),o(S)).
> \]
>
> **核心结论：**frontier 的 primitive \(5\)-adic angular depth在 leading order 上由 denominator 的 \(5\)-adic exponent pattern完全决定，并不是新的独立 entropy。

---

### 1. denominator 与 numerator 的 small side

记

\[
e_i=v_5(b_i),
\qquad
E=\max(e_1,e_2,e_3).
\]

frontier digit shape 给

\[
m_1=o(S),
\qquad
n_2=o(S).
\]

因此

\[
\boxed{e_1=o(S),}
\tag{1.1}
\]

并且

\[
\boxed{v_5(a_2)=o(S).}
\tag{1.2}
\]

terminal overlap 为

\[
t=(10^mQ,b_3),
\qquad
u=\frac{10^mQ}{t}=2\cdot5^TU,
\qquad
v=\frac{b_3}{t}=V,
\]

其中 \(U,V\) 为 5-adic units。故

\[
v_5(b_3)=v_5(t)
=m+v_5(Q)-T.
\]

terminal slow-data normalization 给

\[
v_5(Q)=o(S),
\]

所以

\[
\boxed{e_3=m-T+o(S).}
\tag{1.3}
\]

frontier 比例还满足

\[
\boxed{3T=2m+o(S),}
\tag{1.4}
\]

因为

\[
\frac mS\to2.808883577618\ldots,
\qquad
\frac TS\to1.872589051745\ldots.
\]

---

### 2. \(s_5\) 实际上等于第三 ghost 的 denominator deficit

全局

\[
q=\operatorname{lcm}(b_1,b_2,b_3)
\]

给

\[
y_i=a_i\frac q{b_i}.
\]

由于 sufficiently large frontier 上 \(e_3>0\)，reducedness 给

\[
v_5(a_3)=0.
\]

所以

\[
\boxed{v_5(y_3)=E-e_3.}
\tag{2.1}
\]

前一文件已证明

\[
v_5(H-y_3)>v_5(y_3)
\]

对 sufficiently large frontier 成立。因此

\[
H=y_3+(H-y_3)
\]

直接给

\[
\boxed{v_5(H)=v_5(y_3)=E-e_3.}
\tag{2.2}
\]

故

\[
\boxed{s_5:=\min(v_5(H),v_5(y_3))=E-e_3.}
\tag{2.3}
\]

这里没有剩余误差。

---

### 3. common ghost scale \(r_5\) 的 leading formula

令

\[
g=(y_1,y_2),
\qquad
r_5=v_5(g).
\]

由

\[
v_5(y_1)=E-e_1+v_5(a_1),
\]

\[
v_5(y_2)=E-e_2+v_5(a_2),
\]

以及 `(1.1)`--`(1.2)`：

\[
v_5(y_1)\ge E-o(S),
\]

\[
v_5(y_2)=E-e_2+o(S).
\]

因为 \(e_2\ge0\)，两式取最小得到

\[
\boxed{r_5=E-e_2+o(S).}
\tag{3.1}
\]

这说明 common ghost scale 也不是独立变量；leading order 上它就是总 \(5\)-进 denominator maximum 相对第二分母的 deficit。

---

### 4. primitive angular depth 的 denominator-only formula

写

\[
y_1=gX,
\qquad
y_2=gY,
\qquad(X,Y)=1,
\]

并令

\[
\omega_5=v_5(X^2+Y^2).
\]

前一文件已得

\[
2r_5+\omega_5=T+s_5+o(S).
\tag{4.1}
\]

代入 `(2.3)` 与 `(3.1)`：

\[
2(E-e_2)+\omega_5
=T+(E-e_3)+o(S),
\]

所以

\[
\boxed{
\omega_5
=T-E+2e_2-e_3+o(S).
}
\tag{4.2}
\]

因为 `(1.1)` 给 \(e_1=o(S)\)，leading order 上

\[
E=\max(e_2,e_3)+o(S).
\]

分两种情况。

#### 4.1 tail 5-max：\(e_2\le e_3+o(S)\)

此时 \(E=e_3+o(S)\)，故

\[
\omega_5
=T+2e_2-2e_3+o(S).
\]

由 `(1.3)`--`(1.4)`：

\[
T-2e_3
=T-2(m-T)+o(S)
=3T-2m+o(S)
=o(S).
\]

因此

\[
\boxed{\omega_5=2e_2+o(S).}
\tag{4.3}
\]

#### 4.2 prefix 5-max：\(e_2\ge e_3+o(S)\)

此时 \(E=e_2+o(S)\)，故

\[
\omega_5
=T+e_2-e_3+o(S).
\]

而

\[
T-e_3
=T-(m-T)+o(S)
=2T-m+o(S).
\]

由 \(3T=2m+o(S)\)：

\[
2T-m=m-T+o(S)=e_3+o(S).
\]

所以

\[
\boxed{\omega_5=e_2+e_3+o(S).}
\tag{4.4}
\]

统一得到

\[
\boxed{
\omega_5
=e_2+\min(e_2,e_3)+o(S).
}
\tag{5-adic-baseline}
\]

---

### 5. 解释：primitive angle 已被 denominator baseline 完全支付

右端

\[
e_2+\min(e_2,e_3)
\]

只依赖 \((b_2,b_3)\) 的 5-adic exponent pattern。它可以写成

\[
\boxed{
\omega_5
=v_5(b_2)+v_5((b_2,b_3))+o(S).
}
\tag{5.1}
\]

所以 terminal frontier 的 primitive Gaussian angle 虽然可能具有正线性深度，但它在 leading order 上**没有独立算术自由度**：每一份深度都已经由 denominator 5-adic baseline 预先决定。

这解释了此前多个 5-adic / projective 尝试为何不断达到临界等号：

\[
\boxed{
\text{frontier 5-adic angle}
=\text{denominator baseline}+o(S).
}
\]

因此后续若要关闭 terminal frontier，不应再把 \(\omega_5\) 当成一份可额外收费的 height。

---

### 6. 与 projective no-double-pay 的最终合并

虽然 \(\omega_5\) 没有独立 entropy，前两份 continuation 仍给出重要的“不重复计费”信息：

- \(\omega_5\) 不进入 \(Z_0\)；
- \(\omega_5>0\) 时 primitive bottom carrier 不接收同一份 angular depth；
- angular depth 不能同时进入两条 independent upper carrier edges；
- normalized tail moving factors在 \(5\mid L\) 时都是 5-adic units。

现在这些结论应解释为：**denominator 已经支付的 5-adic baseline 不能再被 projective/carrier 层重复使用。**

所以 terminal frontier 剩余的真正正线性未决对象继续是 odd split-prime moving core \(C_L\) 及其 digit-shell compatibility，而不是 5-adic angular entropy。

---

## 5. DD frontier one-channel collapse 与二阶 \(A_{12}\) CRT — 2026-08-16

> 整合来源：`dd-frontier-one-channel-second-order-2026-08-16.md`。以下正文保留该来源的原始证明状态和审计边界。

> 本文接续 terminal frontier、rational-contact frontier 与 Good continuation。
> 适用范围为假想
> \[
> \frac{n_3}{S}\to6.308883577618\ldots
> \]
> 的无界 DD frontier sequence；第 4 节以后进一步进入 full rational-contact main branch。
>
> **核心推进：**
> 1. frontier 的 moving pair-max rough mass 在 leading order 上只剩 \(b_2\)-\(b_3\) 单一通道；
> 2. 将旧 §67 只记录“存在”的 \(A_{12}\bmod q_c^2\) 与 \(A_{12}\bmod C_L\) 两条线性同余显式恢复；
> 3. 说明 \(C_L\)-侧信息确实只在除去第一份 Gaussian rational-contact core 后出现，是一个真正的二阶 quotient residue。

---

### 1. moving pair-max core 的单通道坍缩

一般 DD 的 reduced-tail moving odd core 写作

\[
V=v_1v_2
\]

（这里删去旧记号中所有 \(2,5\)-part；terminal normalization 已有 \((V,10)=1\)），其中：

- \(v_1\) 对应 pair-max \((b_1,b_3)\)；
- \(v_2\) 对应 pair-max \((b_2,b_3)\)。

canonical denominator normal form 给

\[
b_1=h\,v_1B_1,
\qquad
b_2=h\,v_2B_2,
\qquad
b_3=h\,v_1v_2B_3,
\tag{1.1}
\]

且 \((B_1B_2B_3,v_1v_2)=1\)。

frontier digit shape 为

\[
(m_1,m_2;n_1,n_2)
=(o(S),S-o(S);S-o(S),o(S)).
\tag{1.2}
\]

因此

\[
b_1<10^{m_1}=10^{o(S)}.
\]

由 \(v_1\mid b_1\)：

\[
\boxed{\log v_1=o(S).}
\tag{1.3}
\]

另一方面 terminal phase 给

\[
V=C_Lv_0,
\qquad
\log C_L=S+o(S),
\qquad
\log v_0=o(S).
\tag{1.4}
\]

所以

\[
\boxed{\log v_2=S+o(S).}
\tag{1.5}
\]

换言之，删去 norm \(10^{o(S)}\) 的 exceptional core 后，整个 moving pair-max core 都在 \((b_2,b_3)\) channel：

\[
\boxed{v_2=C_L\cdot10^{o(S)}.}
\tag{One-channel}
\]

特别地，因为 \(m_2=S+o(S)\)，

\[
\boxed{b_2=C_L\cdot10^{o(S)}}
\tag{1.6}
\]

按 logarithmic height 理解。

对应 sphere divisibilities 统一为

\[
\boxed{C_L\mid H_{\rm sph},\ y_1}
\tag{1.7}
\]

以及 oriented pair-max

\[
\boxed{\Pi^2\mid y_2+i y_3,\qquad N(\Pi)=C_L}
\tag{1.8}
\]

均只差 norm \(10^{o(S)}\) 的 exceptional core。

**结论：**frontier 后续无需继续保留两个指数级 pair-max channels；\(b_1\)-\(b_3\) 一侧只有 subexponential mass。

---

### 2. 一个 exact numerator bridge

沿用

\[
X=2^HZ,
\qquad
Y=5^TU,
\qquad
V=X-Y,
\qquad
\Sigma:=X+Y.
\]

已有 exact reconstruction

\[
UA_0+R_0=g_0B10^dA_{12},
\tag{2.1}
\]

以及前一 continuation 得到

\[
\boxed{g_0\alpha=\Sigma A_0.}
\tag{2.2}
\]

其中

\[
\alpha=A_{12}10^{n_3}+a_3,
\qquad
n_3=m+d,
\]

并且

\[
\frac{10^m}{B}=2\cdot5^T.
\tag{2.3}
\]

将 `(2.2)` 代入 `(2.1)`：

\[
\begin{aligned}
\Sigma R_0
&=g_0\left(
B10^d\Sigma A_{12}-U\alpha
\right)\\
&=g_0\left[
\bigl(B10^d\Sigma-U10^{m+d}\bigr)A_{12}-Ua_3
\right].
\end{aligned}
\]

由

\[
\Sigma-2\cdot5^TU=V
\]

及 `(2.3)`：

\[
B10^d\Sigma-U10^{m+d}
=B10^dV.
\]

因此得到 exact identity

\[
\boxed{
\Sigma R_0
=g_0\bigl(B10^dVA_{12}-Ua_3\bigr).
}
\tag{R0-A12}
\]

这是后续两个 CRT residues 的共同起点。

---

### 3. 显式恢复 \(A_{12}\bmod q_c^2\)

clean source 为

\[
VA_0-5^TR_0=q_c^2L_{\rm clean}.
\tag{3.1}
\]

乘以 \(\Sigma\)，再用 `(2.2)` 与 `(R0-A12)`：

\[
\begin{aligned}
\Sigma q_c^2L_{\rm clean}
&=g_0V\alpha
-g_0 5^T(B10^dVA_{12}-Ua_3)\\
&=g_0\left[
V(10^{m+d}-5^TB10^d)A_{12}
+(V+5^TU)a_3
\right].
\end{aligned}
\]

由

\[
10^m=2\cdot5^TB,
\qquad
V+5^TU=X,
\]

得到

\[
\boxed{
\Sigma q_c^2L_{\rm clean}
=g_0\bigl(
5^TB10^dVA_{12}+Xa_3
\bigr).
}
\tag{QCRT-exact}
\]

因此在删去 \((q_c,g_0BVa_3)=10^{o(S)}\) 的 coefficient overlap 后，得到有效线性同余

\[
\boxed{
5^TB10^dV\,A_{12}
\equiv-Xa_3
\pmod{q_c^2/10^{o(S)}}.
}
\tag{QCRT}
\]

其有效模量高度为

\[
\boxed{
2\log q_c
=0.617767155236\ldots S+o(S).
}
\tag{3.2}
\]

这就是旧 §67 中未显式写出的第一条 residue。

---

### 4. 为什么一阶模 \(C_L\) 看不到 \(A_{12}\)

`(R0-A12)` 中

\[
C_L\mid V.
\]

所以直接模 \(C_L\) 时，\(A_{12}\) 的 coefficient 整体消失：

\[
\Sigma R_0
\equiv-g_0Ua_3
\pmod{C_L}.
\tag{4.1}
\]

因此任何只停留在 rational first-order reconstruction 的尝试，都不可能得到 \(A_{12}\bmod C_L\)。

这解释了旧 §67 的第二条 congruence 为什么必须来自 **除去第一份 pair-max / rational-contact core 之后的 quotient level**。

---

### 5. 显式恢复二阶 Gaussian \(C_L\)-residue

进入 full rational-contact branch。令

\[
E=D_+D_-,
\qquad
V=Ee_0,
\]

并取

\[
\Gamma:=\Pi_+\overline{\Pi_-},
\qquad
N(\Gamma)=E.
\tag{5.1}
\]

axis factorization 为

\[
C_*+iR_0=\Gamma\overline K,
\tag{5.2+}
\]

\[
C_*-iR_0=\overline\Gamma K,
\tag{5.2-}
\]

其中

\[
C_*:=\frac{g_0a_2B}{2}.
\]

将 `(R0-A12)` 代入 `(5.2+)` 并乘以 \(\Sigma\)：

\[
\Sigma\Gamma\overline K
=
\Sigma C_*
-i g_0Ua_3
+i g_0B10^dV A_{12}.
\]

使用

\[
V=Ee_0=N(\Gamma)e_0
=\Gamma\overline\Gamma e_0,
\]

得到

\[
\Sigma C_*-i g_0Ua_3
=\Gamma\left(
\Sigma\overline K
-i g_0B10^de_0\overline\Gamma A_{12}
\right).
\]

因此

\[
\boxed{
M_+:=
\frac{\Sigma C_*-i g_0Ua_3}{\Gamma}
\in\mathbf Z[i].
}
\tag{5.3+}
\]

并且

\[
\boxed{
\Sigma\overline K-M_+
=i g_0B10^de_0\overline\Gamma A_{12}.
}
\tag{A12-second+}
\]

完全对称地：

\[
\boxed{
M_-:=
\frac{\Sigma C_*+i g_0Ua_3}{\overline\Gamma}
\in\mathbf Z[i],
}
\tag{5.3-}
\]

\[
\boxed{
\Sigma K-M_-
=-i g_0B10^de_0\Gamma A_{12}.
}
\tag{A12-second-}
\]

这两式是 **exact second-order quotient identities**。

---

### 6. 第二条 \(A_{12}\) residue 的有效 rational modulus

从 `(A12-second+)` 模 \(\Gamma\)：

\[
\boxed{
 i g_0B10^de_0\overline\Gamma A_{12}
\equiv
\Sigma\overline K-M_+
\pmod\Gamma.
}
\tag{GCRT+}
\]

main mass 上：

\[
N\gcd_{\mathbf Z[i]}(\Gamma,\overline\Gamma)
=10^{o(S)},
\]

并且 coefficient overlap

\[
N\gcd_{\mathbf Z[i]}
(\Gamma,g_0B10^de_0\Sigma)
=10^{o(S)}.
\]

因此 `(GCRT+)` 对 rational integer \(A_{12}\) 给出的有效 period 为

\[
\boxed{
E/10^{o(S)}
=10^{S+o(S)}.
}
\tag{6.1}
\]

理由是：删去 conjugate exceptional core 后，映射

\[
\mathbf Z\longrightarrow\mathbf Z[i]/(\Gamma)
\]

的 kernel 为

\[
(N\Gamma)=(E).
\]

所以旧 §67 所称的“模 \(C_L\) 线性同余”可以更精确地表述成 `(GCRT+)`：它来自第一次 rational/Gaussian core 除法后的 second-order quotient residue。

---

### 7. §67 的 \(1.617767\ldots S\) 联合模量由此完全显式化

`(QCRT)` 的有效高度为

\[
0.617767155236\ldots S+o(S),
\]

`(GCRT+)` 的有效高度为

\[
S+o(S).
\]

又有

\[
(q_c,C_L)=1,
\]

且 full rational 中 \(E=C_L\cdot10^{o(S)}\)。故两个 effective periods 只有 \(10^{o(S)}\) overlap。

因此联合 modulus 高度为

\[
\boxed{
1.617767155236\ldots S+o(S).
}
\tag{7.1}
\]

而

\[
\log A_{12}=S+o(S).
\]

从而重新严格得到

\[
\boxed{\#\{A_{12}\}\le1}
\]

对固定 terminal denominator-tail / axis data成立。

与旧文相比，新的内容是两个 residue 的 **显式 exact parents** `(QCRT-exact)` 与 `(A12-second+)` 已经写出。

---

### 8. 新的状态边界

这次展开同时证明了一个重要 no-go：

\[
\boxed{
\text{任何 first-order }C_L\text{ elimination 都看不到 }A_{12};
}
\]

因为它的 coefficient 必然带 \(V\)，见 `(4.1)`。

真正的 \(A_{12}\bmod C_L\) 信息只在除去第一份 \(\Gamma\) 后出现。

因此下一步若要把“至多一个 \(A_{12}\)”升级为 emptiness，目标已经非常具体：

> 对 `(QCRT)` 与 `(GCRT+)` 的唯一 CRT lift 做 **digit-shell location**，证明该 lift 无法落入
> \[
> 10^{S+o(S)-1}\le A_{12}<10^{S+o(S)}
> \]
> 的合法十进制窗口，或者证明 `(GCRT+)` 的 Gaussian phase 与 `(QCRT)` 的 rational residue 在 full rational Good / genuine-Gaussian 两支中不兼容。

继续制造 first-order resultant 不会触及这个问题。

---

## 6. DD frontier decimal remainder collapse — 2026-08-16

> 整合来源：`dd-frontier-decimal-remainder-2026-08-16.md`。以下正文保留该来源的原始证明状态和审计边界。

> 接续 [`frontier.md`](frontier.md)。
> 适用范围为假想 \(6.308883577618\ldots\) terminal frontier。
>
> **核心结论：**terminal numerator reconstruction 中一个原本只按高度观察的巨大 cancellation，实际上落入严格的单个十进制 remainder cell：
> \[
> 0<R_{\rm dec}<10^d.
> \]
> 因而产生 exact `-1 carry` 恒等式。

---

### 1. exact defect

沿用

\[
X=2^HZ,
\qquad
Y=5^TU,
\qquad
V=X-Y,
\qquad
\Sigma=X+Y.
\]

前一文件已经严格得到

\[
\boxed{
\Sigma R_0
=g_0\bigl(B10^dVA_{12}-Ua_3\bigr).
}
\tag{1.1}
\]

定义

\[
\boxed{
R_{\rm dec}:=
B10^dVA_{12}-Ua_3.
}
\tag{1.2}
\]

则

\[
\boxed{
R_{\rm dec}=\frac{\Sigma R_0}{g_0}.
}
\tag{1.3}
\]

所有量均为正，terminal normalization 中 \(R_0>0\)，故

\[
\boxed{R_{\rm dec}>0.}
\tag{1.4}
\]

---

### 2. 关键尺度：\(R_0\) 只有 subexponential height

secondary Gaussian coefficient 在 terminal 中写成

\[
B_*:=\widetilde rR_0,
\]

且已有

\[
\log|B_*|=o(S).
\]

由于 \(\widetilde r\in\mathbf Z_{>0}\)，得到

\[
\boxed{\log R_0=o(S).}
\tag{2.1}
\]

同样 \(g_0\ge1\)，所以 `(1.3)` 给

\[
\log R_{\rm dec}
\le
\log\Sigma+o(S).
\]

frontier phase 中

\[
\log\Sigma=2S+o(S),
\]

故

\[
\boxed{
\log R_{\rm dec}
\le2S+o(S).
}
\tag{2.2}
\]

另一方面

\[
\frac dS\to3.5.
\]

因此 sufficiently large frontier 上

\[
\boxed{
0<R_{\rm dec}<10^d.
}
\tag{Decimal-cell}
\]

这里存在 \(1.5S-o(S)\) 的严格指数余量。

---

### 3. reducedness 保证余数非零

terminal third denominator 含有大 \(2,5\)-smooth factor；特别是 sufficiently large frontier 上

\[
10\mid b_3.
\]

由

\[
(a_3,b_3)=1
\]

得到

\[
(a_3,10)=1.
\]

又

\[
(U,10)=1,
\]

所以

\[
\boxed{(Ua_3,10)=1.}
\tag{3.1}
\]

因此

\[
Ua_3\not\equiv0\pmod{10^d}.
\]

写 Euclidean division

\[
Ua_3=K10^d+r,
\qquad
1\le r<10^d.
\tag{3.2}
\]

---

### 4. exact `-1 carry`

由 `(1.2)`：

\[
R_{\rm dec}
=BVA_{12}10^d-(K10^d+r)
=(BVA_{12}-K)10^d-r.
\]

结合

\[
0<R_{\rm dec}<10^d,
\qquad
1\le r<10^d,
\]

唯一可能是

\[
\boxed{BVA_{12}-K=1.}
\tag{4.1}
\]

并且

\[
\boxed{R_{\rm dec}=10^d-r.}
\tag{4.2}
\]

所以得到新的 exact digit-carry identity：

\[
\boxed{
\left\lfloor\frac{Ua_3}{10^d}\right\rfloor
=BVA_{12}-1.
}
\tag{Carry-floor}
\]

等价地

\[
\boxed{
BVA_{12}
=\left\lceil\frac{Ua_3}{10^d}\right\rceil.
}
\tag{Carry-ceil}
\]

以及

\[
\boxed{
Ua_3
=(BVA_{12}-1)10^d
+\bigl(10^d-R_{\rm dec}\bigr).
}
\tag{4.3}
\]

这比仅仅知道

\[
B10^dVA_{12}=Ua_3+10^{2S+o(S)}
\]

强得多：cancellation 已经被定位到唯一 decimal carry cell。

---

### 5. 与 primitive determinant 的 exact 对接

全局 DD determinant 为

\[
E
=b_3A_{12}10^d-a_3Q.
\tag{5.1}
\]

terminal normalization 有

\[
Q=JUq_c\theta,
\]

\[
b_3=BJVq_c\theta.
\]

因此

\[
\begin{aligned}
E
&=Jq_c\theta
\bigl(BVA_{12}10^d-Ua_3\bigr)\\
&=Jq_c\theta R_{\rm dec}.
\end{aligned}
\]

故得到

\[
\boxed{
E=Jq_c\theta R_{\rm dec}.
}
\tag{Det-remainder}
\]

再用 `(1.3)`：

\[
\boxed{
E
=Jq_c\theta\frac{\Sigma R_0}{g_0}.
}
\tag{5.2}
\]

所以 terminal primitive determinant 的最后 defect 并不是新的自由整数；它等于 clean source rough factor \(q_c\) 乘上一个严格位于单 decimal cell 内的 remainder。

---

### 6. 新的结构性含义

`(Carry-floor)` 把 frontier numerator 约束改写成：

\[
\boxed{
\text{一个真实乘积 }Ua_3
\text{ 的前 }(n_3+\log U-d)\text{ 位，}
\text{恰好等于 }BVA_{12}-1.
}
\]

同时低 \(d\) 位的 complement 为

\[
R_{\rm dec}
=10^d-(Ua_3\bmod10^d)
=10^{2S+o(S)},
\]

因此低 \(d\)-digit residue 实际位于 interval 顶端：

\[
\boxed{
Ua_3\bmod10^d
=10^d-10^{2S+o(S)}.
}
\tag{Top-residue}
\]

相对整个 \(10^d\) 模长，它距离上端只有

\[
10^{-1.5S+o(S)}
\]

的比例。

这已经是一个真正的 `CRT remainder window`：任何后续独立的 \(2\)-adic / \(5\)-adic / Gaussian residue 若能把 \(Ua_3\bmod10^d\) 排除在该顶端薄层之外，就会直接关闭 terminal frontier。

---

### 7. 当前下一击

后续不应再把 `(1.1)` 当作普通 height cancellation。首选目标改成：

1. 将 `Top-residue` 分别投影到 \(2^d\)、\(5^d\)；
2. 使用 \((a_3,b_3)=1\)、\((U,10)=1\) 与 terminal source phase 确定 \(Ua_3\) 的 inverse class；
3. 与 pair-max / second-order \(A_{12}\) CRT 对齐；
4. 争取证明唯一 residue class 到 \(10^d\) 上端的距离至少为 \(10^{(2+\varepsilon)S}\)，与实际 \(10^{2S+o(S)}\) 冲突。

这条路线有真实的 \(1.5S\) remainder margin，和此前多个 leading-order critical equalities不同。

---

## 7. DD frontier continuation：Good closure audit、orientation reconstruction 与双 lattice sheet

> 整合来源：`dd-frontier-continuation-2026-08-16.md`。以下正文保留该来源的原始证明状态和审计边界。

> **研究日期：2026-08-16**
> **适用范围：**仅针对假想满足
> \[
> \frac{n_3}{S}\to6.308883577618\ldots
> \]
> 的 DD frontier sequence。
> **状态边界：**本文记录 `frontier.md` 之后的新推进与 no-go 审计。本文**不证明 DD 全局空性**，也不给出有效绝对的 \(S\) 上界。
> **阅读约定：**若本文与 `frontier.md` 中“Bad 尚待关闭”等旧状态冲突，以本文的更新状态为准；但所有结论仍只在 frontier 条件下使用。

---

### 1. 基线与符号

沿用 rational-contact frontier 的 terminal normalization：

\[
X=2^HZ,\qquad Y=5^TU,\qquad V=X-Y=C_0s,
\]

\[
V=C_Lv_0,\qquad
\log C_L=S+o(S),\qquad
\log v_0=o(S),
\]

\[
q_c=10^{z_*S+o(S)},
\qquad
z_*=0.308883577618\ldots,
\]

以及 oriented pair-max Gaussian core

\[
N(\Pi)=C_L,
\qquad
\Pi^2\mid y_2+i y_3.
\]

仍记

\[
A=s\theta q_c,
\qquad
b=5^T\widetilde r,
\]

\[
C_*:=\frac{g_0a_2B}{2},
\qquad
N_{\rm ax}=C_*^2+R_0^2,
\]

\[
P_0=g_0a_2B\theta s,
\]

以及 hidden square / clean source：

\[
\boxed{
(C_LP_1)^2+P_0^2
=4\widetilde r^{\,2}5^TR_0L_{\rm clean},
}
\tag{HS}
\]

\[
\boxed{
VA_0-5^TR_0=q_c^2L_{\rm clean}.
}
\tag{CS}
\]

secondary Gaussian numerator记为

\[
\mathcal G_1
=g_0a_2\theta s\,2^{m-2}q_c
-i\widetilde rR_0\,5^{2T-m}
=\Pi\Delta_1.
\]

另有 denominator-transformed quotient

\[
L_U=\Pi\Delta_U.
\]

---

## 第一部分：full rational-contact 中 Bad 的关闭与 Good 正规形

### 2. Bad branch 的更新状态：已关闭

旧稿将 full rational-contact 分成 Bad/Good：Bad 表示在 \(L_U\) 已除去第一份 selected orientation 后，\(\Delta_U\) 又出现同 orientation repeat。

本轮首先完成了 conjugate-orientation exclusion。对 main oriented core，若 selected prime 为 \(\pi^h\Vert\Pi\)，则

\[
\bar\pi^r\mid\Delta_U
\]

会迫使相同 rational prime-power 进入 \(R_0\)，再由 clean source 进入 \(L_{\rm clean}\)。结合

\[
\log(C_L,L_{\rm clean})=o(S)
\]

得到

\[
\boxed{
\log N\gcd_{\mathbf Z[i]}(\bar\Pi,\Delta_U)=o(S).
}
\tag{2.1}
\]

同理，借助 U1-transfer 可以把 \(\Delta_1\) 的 conjugate overlap 转移到 \(\Delta_U\)，得到

\[
\boxed{
\log N\gcd_{\mathbf Z[i]}(\bar\Pi,\Delta_1)=o(S).
}
\tag{2.2}
\]

因此 single-slot allocation 可以真正排除 \(N(\Delta_1)\) 对 Bad main mass 的重复支付。

将 `Bad-CF` 与 `Nc-elim` 联立，并移除只由 \(N(\Delta_1)\) 支付的次指数异常部分，可得 oriented tangent congruences

\[
\boxed{
B_+^{\flat}\mid d h_+ + b j_+,
}
\tag{2.3+}
\]

\[
\boxed{
B_-^{\flat}\mid b j_- - d h_-.
}
\tag{2.3-}
\]

这里 \(B_\pm^{\flat}\) 与原 Bad mass 只差 \(10^{o(S)}\) 的 exceptional core。

再使用 sign-Farey exact identities 与

\[
\boxed{
Ac-bd=ET_c,
\qquad
T_c=e_0\widetilde r^{\,2}5^{T-m_2},
}
\tag{2.4}
\]

可把 (2.3±) 的 main oriented prime-power 继续压入 \(T_c\) 的 rough core。由于

\[
\log\operatorname{core}_{10}(T_c)=o(S),
\]

Bad 不可能承载正线性质量。因此

\[
\boxed{
\log(B_+B_-)=o(S).
}
\tag{Bad-closed}
\]

故 full rational-contact 在 leading order 上是纯 Good：

\[
\boxed{
\log(G_+G_-)=S+o(S).
}
\tag{Good-main}
\]

> **状态：**`Bad` 在 full rational-contact frontier 上关闭；这不是 DD 全局关闭。

---

### 3. Good 的 Gaussian square-Plücker 正规形

设

\[
\alpha_1=g_0a_2\,2^{m-2},
\qquad
\beta_1=\widetilde r5^{2T-m}.
\]

则由 \(10^m/B=2\cdot5^T\) 有

\[
\boxed{\alpha_1b=\beta_1C_*.}
\tag{3.1}
\]

并且

\[
\boxed{
5^{T-m_2}L_U=C_*d-iR_0c.
}
\tag{3.2}
\]

将 rational main core 写成

\[
\Pi_R=\Pi_+\Pi_-,
\qquad
N(\Pi_R)=D_+D_-=C_L\cdot10^{o(S)},
\]

并定义去掉 \(C_L/(D_+D_-)\) exceptional factor 的 quotients

\[
\widehat\Delta_1=\mathcal G_1/\Pi_R,
\qquad
\widehat\Delta_U=L_U/\Pi_R.
\]

令

\[
S_-=C_*-iR_0,
\qquad
S_+=C_*+iR_0.
\]

由 sign-fixed Gaussian orientation 可写

\[
\boxed{
S_-=\Pi_-\overline{\Pi_+}K,
\qquad
S_+=\Pi_+\overline{\Pi_-}\,\overline K,
}
\tag{3.3}
\]

且

\[
\boxed{N(K)=N_c.}
\tag{3.4}
\]

由

\[
S_-R_+-S_+R_-=2(C_*A-iR_0b)
\]

与 (3.1)，得到

\[
\boxed{
2\,5^{m-T}\widehat\Delta_1
=
\overline{\Pi_+}^{\,2}K h_+
-
\overline{\Pi_-}^{\,2}\overline K h_-.
}
\tag{G1}
\]

类似地由

\[
S_-J_+-S_+J_-=2(C_*d-iR_0c)
\]

与 (3.2)，得到

\[
\boxed{
2\,5^{T-m_2}\widehat\Delta_U
=
\overline{\Pi_+}^{\,2}K j_+
-
\overline{\Pi_-}^{\,2}\overline K j_-.
}
\tag{G2}
\]

利用

\[
j_-h_+-j_+h_-=2T_c,
\]

以及

\[
e=m+m_2-2T>0,
\]

反解二维系统：

\[
\boxed{
e_0\widetilde r^{\,2}\overline{\Pi_+}^{\,2}K
=5^e j_-\widehat\Delta_1-h_-\widehat\Delta_U,
}
\tag{Good-square+}
\]

\[
\boxed{
e_0\widetilde r^{\,2}\overline{\Pi_-}^{\,2}\overline K
=5^e j_+\widehat\Delta_1-h_+\widehat\Delta_U.
}
\tag{Good-square-}
\]

这给出 Good 的一侧 square-depth CRT，但直接做 norm / ordinary linear combination 会精确退回 sign-Farey determinant，不能重复计费。

---

### 4. Good repeat 的本质：radius excess

对 main prime-power

\[
p^h\Vert C_L,
\qquad
p=\pi\bar\pi,
\qquad
\pi^h\Vert\Pi,
\]

原始 cross-determinant 满足

\[
\boxed{
\Delta\Pi
=g_0\bigl((y_2+i y_3)-iH_{\rm sph}\bigr),
}
\tag{4.1}
\]

而 \(\Delta\) 与 \(\Delta_1\) 只差 main \(C_L\)-unit 与 \(10^{o(S)}\) exceptional factor。

定义 radius excess

\[
a_p=v_p(H_{\rm sph})-h.
\]

因为

\[
v_\pi(y_2+i y_3)\ge2h,
\]

可得截断 valuation identity

\[
\boxed{
\min\{v_\pi(\Delta_1),h\}
=
\min\{v_p(H_{\rm sph})-h,h\}.
}
\tag{4.2}
\]

又由 sphere bridge

\[
g_0H_{\rm sph}=C_Lv_0\lambda A_0
\]

得到，在 main mass 上

\[
\boxed{
\min\{v_\pi(\Delta_1),h\}
=
\min\{v_p(A_0),h\}.
}
\tag{4.3}
\]

因此

\[
\boxed{
\text{secondary repeat}
\Longleftrightarrow
\text{radius repeat }(C_L,A_0)
}
\tag{Radius=Secondary}
\]

按逐深度、忽略 \(10^{o(S)}\) coefficient overlaps 的意义成立。

---

## 第二部分：pair-max Gaussian local algebra 的闭包审计

### 5. derivative Gaussian integer 唯一重构 orientation

定义

\[
\boxed{
D_{\rm der}
:=2\widetilde rL_{\rm clean}q_c-iP_0.
}
\tag{5.1}
\]

由 hidden square 与 clean source：

\[
\begin{aligned}
N(D_{\rm der})
&=4\widetilde r^{\,2}L_{\rm clean}^2q_c^2+P_0^2\\
&=4\widetilde r^{\,2}L_{\rm clean}
(q_c^2L_{\rm clean}+5^TR_0)
-(C_LP_1)^2,
\end{aligned}
\]

故

\[
\boxed{
N(D_{\rm der})
=C_L\Bigl(
4\widetilde r^{\,2}L_{\rm clean}v_0A_0
-C_LP_1^2
\Bigr).
}
\tag{5.2}
\]

main \(C_L\)-primes 均为 split odd primes，且 coefficient overlaps 只有 \(10^{o(S)}\)。因此对 almost all main prime-powers，\(D_{\rm der}\) 的两个 Gaussian orientations 中恰有一个以完整深度 \(h\) 出现。于是

\[
\boxed{
\Pi
\sim
\gcd_{\mathbf Z[i]}(C_L,D_{\rm der})
}
\tag{5.3}
\]

差一个 Gaussian unit 与 norm \(10^{o(S)}\) 的 exceptional factor。

**结论：**一旦 rational terminal data 与 \(C_L\) 固定，\(\Pi\) 的逐素数 orientation 没有指数级自由度；\(\Pi\) 是可重构对象，而不是最终独立 entropy。

---

### 6. derivative line 自动恢复 secondary line

有 exact identity

\[
\boxed{
P_0D_{\rm der}
-2\widetilde rL_{\rm clean}
\bigl(P_0q_c-2i\widetilde r5^TR_0\bigr)
=i(C_LP_1)^2.
}
\tag{6.1}
\]

后一个 Gaussian integer只差 smooth/main-unit scalar 就是 secondary numerator。因此

\[
\Pi\mid D_{\rm der}
\Longrightarrow
\Pi\mid\mathcal G_1.
\]

同时令

\[
F_\pm
=D_{\rm der}\pm C_LP_1,
\]

则 \(\Pi\mid F_+,F_-\)，并且二者乘积恢复 pair-max Gaussian double root。

因此 local chain

\[
\boxed{
\text{hidden square}
\Longrightarrow
\text{unique derivative orientation}
\Longrightarrow
\text{secondary line}
\Longrightarrow
\Pi^2\mid y_2+i y_3
}
\tag{6.2}
\]

在 main mass 上自动闭合。

---

### 7. 正确的 Newton second-order resultant 仍然退化

令 derivative root 的一阶 \(p\)-adic \(\sqrt{-1}\) approximation 为

\[
t=\frac{2\widetilde rL_{\rm clean}q_c}{P_0}.
\]

对其做真正 Newton/Hensel 二阶 lift，并与 pair-max root

\[
-\frac{y_2}{y_3}
\pmod{p^{2h}}
\]

比较。完全展开后得到

\[
\boxed{
\Theta_{\rm Newton}
=C_L^2
\left[
4\widetilde r^{\,2}L_{\rm clean}v_0^2A_0^2
-
P_1^2(3q_c^2L_{\rm clean}+5^TR_0)
\right].
}
\tag{7.1}
\]

因此 pair-max 的 \(2h\) 深度在正确的 second-order resultant 中天然带一整份 \(C_L^2\)。

> **No-go：**在已有 \(2h\) pair-max depth 内继续构造同素数 Hensel resultant，不会制造新的正线性 surplus。

---

### 8. derivative repeat、secondary repeat、radius repeat 等价

由 (6.1) 除去一份 \(\Pi\)，对 \(r\le h\)：

\[
\boxed{
\pi^r\mid D_{\rm der}/\Pi
\iff
\pi^r\mid\Delta_1.
}
\tag{8.1}
\]

而由 (5.2)：

\[
\boxed{
\pi^r\mid D_{\rm der}/\Pi
\iff
p^r\mid A_0
}
\tag{8.2}
\]

在 main coefficient-unit mass 上成立。

故再次得到

\[
\boxed{
\text{derivative repeat}
=
\text{secondary repeat}
=
\text{radius repeat}.
}
\tag{8.3}
\]

这说明 Good 的 secondary-repeat 子支不是新的 Gaussian mechanism。

---

## 第三部分：near-square 的完全展开与 no-go

### 9. normalized near-square 的两个因子其实就是旧 source channels

写 normalized discriminant

\[
M^2-Z_{\rm disc}^2=R,
\]

并令

\[
t=M-Z_{\rm disc}>0.
\]

由全局 primitive recovery 与 terminal S-unit phase，将 \(\kappa,\mu,\nu,G_0\) 完整代回，可以把小因子精确化成

\[
\boxed{
M-Z_{\rm disc}
=
\frac{J^2\widetilde w\widetilde rR_0}{g_0}
2^{H-m+3}5^{2T-m}Z.
}
\tag{9.1}
\]

因此

\[
\boxed{
\operatorname{core}_{10}(M-Z_{\rm disc})
=Z\cdot10^{o(S)}.
}
\tag{9.2}
\]

另一因子同样可完全展开：

\[
\boxed{
M+Z_{\rm disc}
=
\frac{4J^2\widetilde w\widetilde r5^T
L_{\rm clean}q_c^2U}{Bg_0}.
}
\tag{9.3}
\]

所以判别平方根本身为

\[
\boxed{
Z_{\rm disc}
=
\frac{2J^2\widetilde w\widetilde r5^T}{Bg_0}
\left(
L_{\rm clean}q_c^2U
-R_0\,2^HZ
\right).
}
\tag{9.4}
\]

两因子相加给

\[
\boxed{
Bg_0sC_0A_{12}10^d
=L_{\rm clean}q_c^2U+R_0\,2^HZ.
}
\tag{9.5}
\]

再代入 clean source 与 \(2^HZ=5^TU+V\)，(9.5) 精确退回 numerator reconstruction

\[
UA_0+R_0=g_0B10^dA_{12}.
\]

> **No-go：**near-square 的小 CRT square-root representative 并非新的 random phase；其 rough core 就是已有 \(Z\)-channel，而大因子是已有 \(q_c^2U\)-channel。完整 \(2/5\)-adic phase 只是在重构旧 terminal data。

---

## 第四部分：两个 exact rank-2 lattice sheets

### 10. denominator triangle

定义三列

\[
v_1=
\binom{2^{m_2}}{5^T},
\qquad
v_2=
\binom{\widetilde r}{R_2},
\qquad
v_3=
\binom{U}{2^{H-m_2}Z}.
\]

则三个 \(2\times2\) minors 恰好为

\[
\boxed{
\det(v_1,v_2)=s\theta q_c,
}
\tag{10.1}
\]

\[
\boxed{
\det(v_1,v_3)=V=sC_0,
}
\tag{10.2}
\]

\[
\boxed{
\det(v_2,v_3)=-s^2\widetilde w5^{m_2}.
}
\tag{10.3}
\]

因此 terminal denominator/source chain 可包装为

\[
\boxed{
\mathcal D=
\begin{pmatrix}
2^{m_2}&\widetilde r&U\\
5^T&R_2&2^{H-m_2}Z
\end{pmatrix}.
}
\tag{D-Triangle}
\]

Plücker relation 的两个坐标分别恢复

\[
\theta q_cU=C_0\widetilde r+s\widetilde w10^{m_2},
\]

\[
\theta q_c2^{H-m_2}Z=C_0R_2+s\widetilde w5^{T+m_2}.
\]

所以这不是额外约束，而是 terminal denominator chain 的最小 rank-2 线性代数封装。

---

### 11. \(\delta_*\) 是 denominator triangle 的 projective thickness

定义三个 slope

\[
\lambda_1=\frac{5^T}{2^{m_2}},
\qquad
\lambda_2=\frac{R_2}{\widetilde r},
\qquad
\lambda_3=\frac{2^{H-m_2}Z}{U}.
\]

由 (10.1)--(10.3)：

\[
\lambda_2-\lambda_1
=
\frac{s\theta q_c}{2^{m_2}\widetilde r},
\]

\[
\lambda_2-\lambda_3
=
\frac{s^2\widetilde w5^{m_2}}{\widetilde rU},
\]

\[
\lambda_3-\lambda_1
=
\frac{V}{2^{m_2}U}.
\]

三个 slope 自身均具有

\[
\log_{10}\lambda_i
=1.007853581954\ldots S+o(S),
\]

而三个绝对差均位于

\[
10^{\delta_*S+o(S)},
\qquad
\boxed{
\delta_*=0.007853581954\ldots.
}
\tag{11.1}
\]

换言之，三点相对距离都是 \(10^{-S+o(S)}\)。此前最后 source-lift 中反复出现的 \(\delta_*S\) entropy，几何上正是这张 denominator projective triangle 的厚度。

进一步，三列 projective heights 与三个 minors 的 leading heights 恰好使 adelic product-formula budget达到临界等号。因此 denominator triangle 单独不能再由 fixed-target Subspace/Ridout 类型估计收费。

---

### 12. source / numerator triangle

定义

\[
w_1=
\binom{5^T}{V},
\qquad
w_2=
\binom{A_0}{R_0},
\qquad
w_3=
\binom{1}{-U}.
\]

三个 minors 为

\[
\boxed{
\det(w_1,w_2)
=5^TR_0-VA_0
=-q_c^2L_{\rm clean},
}
\tag{12.1}
\]

\[
\boxed{
\det(w_1,w_3)
=-(5^TU+V)
=-2^HZ,
}
\tag{12.2}
\]

\[
\boxed{
\det(w_2,w_3)
=-(UA_0+R_0)
=-g_0B10^dA_{12}.
}
\tag{12.3}
\]

因此第二张 exact sheet 为

\[
\boxed{
\mathcal S=
\begin{pmatrix}
5^T&A_0&1\\
V&R_0&-U
\end{pmatrix}.
}
\tag{S-Triangle}
\]

它同时包装 clean source、S-unit phase 与 numerator reconstruction。

---

### 13. 两张 sheet 的自然 mixed direction 在 main \(C_L\) 上横截

将 denominator sheet 的两行与 source sheet 的第二行组成

\[
\mathscr M=
\begin{pmatrix}
2^{m_2}&\widetilde r&U\\
5^T&R_2&2^{H-m_2}Z\\
V&R_0&-U
\end{pmatrix}.
\]

直接展开，并使用 denominator minors，得到

\[
\boxed{
\det\mathscr M
=-\left[
V(s^2\widetilde w5^{m_2}+R_0)
+Us\theta q_c
\right].
}
\tag{13.1}
\]

再用

\[
s\theta q_cU
=\widetilde rV+s^2\widetilde w10^{m_2},
\]

得到

\[
\boxed{
\det\mathscr M
=-\left[
V(s^2\widetilde w5^{m_2}+R_0+\widetilde r)
+s^2\widetilde w10^{m_2}
\right].
}
\tag{13.2}
\]

由于

\[
C_L\mid V,
\qquad
(C_L,10)=1,
\]

故模 \(C_L\)：

\[
\det\mathscr M
\equiv
-s^2\widetilde w10^{m_2}
\pmod{C_L}.
\]

而 main \(C_L\)-mass 与 \(s\widetilde w\) 的 overlap 只有 \(10^{o(S)}\)。因此

\[
\boxed{
\log\gcd\!\left(C_L,\det\mathscr M\right)=o(S).
}
\tag{Mixed-transverse}
\]

这给出一个真正的新 transverse lemma：

> denominator pair-max main core 不会自动传播到最自然的 source lattice direction；两张 terminal sheet 在 main \(C_L\) 上是横截的。

因此不能再把“第二张 source sheet 也会收到同一份 \(C_L\)-deep contact”作为潜在 closure 机制。

---

## 第五部分：orientation entropy 与 counting 的进一步坍缩

### 14. fixed \(C_L\) 后不再需要预先固定 \(\Pi\)

由 derivative reconstruction，对 main \(p^h\Vert C_L\)：

\[
\iota_p
\equiv
\frac{2\widetilde rL_{\rm clean}q_c}{P_0}
\pmod{p^h}.
\]

利用 clean source

\[
q_c^2L_{\rm clean}\equiv-5^TR_0\pmod{p^h},
\]

得到

\[
\boxed{
\iota_p
\equiv
-\frac{2\widetilde r5^TR_0}{P_0q_c}
\pmod{p^h}.
}
\tag{14.1}
\]

将

\[
P_0=g_0a_2B\theta s
\]

代入后，除只由 exponent mode 决定的 smooth factor外，orientation 由

\[
\frac{\xi}{q_c},
\qquad
\xi=\frac{\widetilde rR_0}{g_0a_2\theta s},
\qquad
h(\xi)=o(S),
\]

决定。

若固定 \(C_L\) 与同一个 subexponential terminal-data fiber，存在两个 source lifts \(q_1,q_2\)，按每个 prime 的 orientation 是否相同将 \(C_L\) 分成 \(C_-C_+=C_L\cdot10^{o(S)}\)。则

\[
C_-\mid \xi_1q_2-\xi_2q_1,
\qquad
C_+\mid \xi_1q_2+\xi_2q_1.
\]

右边两个整数的高度各至多

\[
z_*S+o(S)=0.308883577618\ldots S+o(S).
\]

若二者均非零，则

\[
S+o(S)
\le
0.617767155236\ldots S+o(S),
\]

矛盾。因此在固定 slow-data fiber 中必有

\[
\xi_1q_2=\xi_2q_1.
\]

特别地若 \(\xi_1=\xi_2\)，则

\[
\boxed{q_1=q_2.}
\tag{14.2}
\]

故旧的

\[
(C_L,\Pi)\text{ fixed}\Rightarrow q_c\text{ unique}
\]

可加强为：

\[
\boxed{
C_L\text{ fixed + subexponential terminal data fixed}
\Rightarrow q_c\text{ unique}.
}
\tag{14.3}
\]

Gaussian orientation entropy 已经被 derivative gcd 重构吸收。

---

### 15. full rational-contact 的 moving-core counting 可降到 subexponential

full rational-contact 上定义

\[
\Gamma=\Pi_+\overline{\Pi_-}.
\]

sign-fixed axis orientation 给

\[
\Gamma\mid C_*+iR_0,
\qquad
N(\Gamma)=D_+D_-=C_L\cdot10^{o(S)}.
\]

frontier 上 \(a_2,g_0,R_0\) 只有 subexponential height，而 exponent mode \((m,T)\) 在尺度 \(S\) 上只有 polynomially many choices。因此

\[
\#\{C_*+iR_0\}=10^{o(S)}.
\]

对每个这样的 Gaussian integer，Gaussian divisor count 由普通整数 divisor bound 给出

\[
\tau_{\mathbf Z[i]}(C_*+iR_0)=10^{o(S)}.
\]

所以 full rational-contact 中

\[
\boxed{
\#\{(C_L,\Pi)\}=10^{o(S)}.
}
\tag{15.1}
\]

结合 fixed-core source-lift uniqueness，得到该子支的候选计数仍为

\[
\boxed{N_{\rm full\ rational}(S)=10^{o(S)}.}
\tag{15.2}
\]

这消除了指数级 entropy，但**仍不是 eventual emptiness**。

---

## 第六部分：已严格判死 / 降级的新路线

### 16.1 三 Gaussian quotients 再做 projective determinant

\(\Delta_1,\Delta_U,\Delta_Z\) 的三条 pairwise determinant 在 Archimedean 与 finite places 上都精确饱和 product formula；第三个 quotient 不增加 projective rank。其 closure payer 是 \(R_2\)。

**状态：`失效/降级`。**

### 16.2 pair-max second-order Newton resultant

正确 Newton lift result 为 (7.1)，天然含 \(C_L^2\)。

**状态：`失效/降级`。**

### 16.3 source Gaussian factor / quartic reciprocity

将 prefix Gaussian vector按 source factorization写成 \(\Lambda_{\rm src}K_{\rm src}\) 后，试图把 derivative line视为 \(\Pi\) 与 \(\Lambda_{\rm src}\) 的新 reciprocity condition。完整代入后 \(\Lambda_{\rm src}\) 整体可约出，条件退回 hidden-square 的两个一次因子。

**状态：`失效/降级`。**

### 16.4 near-square 的“小 CRT root”

由 (9.1)--(9.5)，小因子的 rough core就是 \(Z\)，大因子就是 \(q_c^2U\) source channel；完整 phase退回 numerator reconstruction。

**状态：`失效/降级`。**

### 16.5 denominator lattice 的 Minkowski shortest vector

\(\mathcal D\) 的 row lattice 面积为 \(10^{S+o(S)}\)，因此存在 \(10^{S/2+o(S)}\) 级短向量。但 row operation 不保持原 decimal carrier 语义，且其法向量 modulo \(C_L\) 给出的 slope 与 pair-max Gaussian \(\sqrt{-1}\) orientation 相差一个正线性 source scaling。

因此不能把 shortest vector 偷换成 \((\Re\Pi,\Im\Pi)\) 并构造下降。

**状态：`失效/降级`。**

### 16.6 两张 lattice sheet 自动共享 main \(C_L\) contact

`Mixed-transverse` 明确给出相反结论：自然 mixed determinant 与 \(C_L\) 的 gcd 只有 \(10^{o(S)}\)。

**状态：`失效/降级`。**

---

## 第七部分：当前真正剩余的 frontier

### 17. 局部 Gaussian algebra 已基本闭包

本轮得到的核心认识是：

\[
\boxed{
\text{pair-max }C_L^2\mid y_2^2+y_3^2
\text{ 的局部二阶 Gaussian algebra已被 hidden square 完全支付。}
}
\]

orientation 可以从 \(D_{\rm der}\) 唯一重构；secondary line、second-order Hensel 与 radius repeat 都是同一局部 algebra 的不同投影。

因此后续不应继续寻找“第三层同素数 Hensel resultant”。

---

### 18. full rational-contact Good 的剩余问题

Bad 已关闭，full rational-contact 的 main mass进入 Good。此前 Good-square 系统给出 conjugate orientation 的 square-depth CRT，但所有 ordinary norm / determinant 会退回 sign-Farey / hidden-square critical geometry。

`Mixed-transverse` 又说明自然 source sheet不能接收同一份 main \(C_L\) contact。

因此 full rational Good 的剩余质量只能藏在已经 critical 的 cofactor/Plücker sheet 中。下一步应当做**容量分配**而非再造 quotient：

1. 将 radius-repeat、next-repeat、carrier-repeat 等槽按逐素数 depth统一分配；
2. 使用 Bad closure 与 `Mixed-transverse` 排除已知槽；
3. 证明剩余 main mass只能进入 cofactor system 的唯一 slot；
4. 对该 slot 寻找独立于 `(CF1)`--`(CF5)` 的 strict height bound。

---

### 19. genuine-Gaussian 的剩余问题

若

\[
C_G=10^{\varepsilon S+o(S)},
\qquad \varepsilon>0,
\]

则这些 main primes 不满足 rational sign degeneration。local pair-max orientation仍可由 derivative Gaussian gcd 重构，但 rational-contact cofactor sheet不存在。

此时真正剩余的是一个**全局 split-prime / digit-shell 问题**：

\[
V=2^HZ-5^TU=C_Lv_0
\]

为何不能让正线性高度长期集中在 \(p\equiv1\pmod4\) 的 denominator pair-max primes，同时满足 denominator triangle、source triangle 与 decimal reconstruction？

这已经不是局部 \(\sqrt{-1}\) Hensel 问题。

---

### 20. 当前严格状态摘要

截至本 continuation：

\[
\boxed{
\begin{array}{l}
\text{full rational Bad：关闭；}\\
\text{Good square-Pl\ddot ucker 正规形：已得；}\\
\text{secondary repeat = radius repeat：已得；}\\
\text{pair-max orientation：由 derivative gcd 唯一重构；}\\
\text{second-order Newton：证明退化；}\\
\text{near-square / 2,5-CRT：证明退化；}\\
\text{denominator triangle：已建立并解释 }\delta_*;\\
\text{source triangle：已建立；}\\
\text{两 sheet 的自然 mixed direction：main-}C_L\text{ 横截；}\\
\text{full rational moving-core entropy：降为 }10^{o(S)};\\
\text{DD frontier emptiness：仍未证明。}
\end{array}
}
\]

最重要的方法论修正是：

\[
\boxed{
\text{停止继续堆同素数 Gaussian resultant；
下一阶段必须做全局 slot capacity / split-prime digit-shell。}
}
\]

---

## 8. DD Good slot capacity frontier — 2026-08-16

> 整合来源：`dd-good-slot-capacity-2026-08-16.md`。以下正文保留该来源的原始证明状态和审计边界。

> 本文接续 [`frontier.md`](frontier.md)。
> 适用范围始终是一个假想满足
> \[
> \frac{n_3}{S}\to6.308883577618\ldots
> \]
> 的 DD frontier sequence，并进一步处于 full rational-contact Good 主质量。
> 本文中的 `main prime-power` 均默认删去 coefficient overlap、conjugate overlap、Bad mass 等总高度为 \(o(S)\) 的 exceptional core。
>
> **状态边界：**本文给出新的严格 frontier 条件蕴含和 no-go 审计；它仍不证明 DD 全局空性。

---

### 1. 基线

沿用

\[
A=s\theta q_c,
\qquad
b=5^T\widetilde r,
\]

\[
c=\widetilde r5^{T-m_2}U,
\qquad
d=s^2\widetilde w2^{m_2},
\]

\[
R_\pm=b\pm A=D_\pm h_\pm,
\qquad
J_\pm=c\pm d=D_\pm j_\pm,
\]

\[
E=D_+D_-,
\qquad V=Ee_0,
\]

以及 cofactor system

\[
H_R=h_+h_-,
\qquad H_J=j_+j_-,
\]

\[
S_c=\frac{bc-Ad}{E},
\qquad
T_c=e_0\widetilde r^{\,2}5^{T-m_2},
\]

\[
S_c^2-H_RH_J=T_c^2.
\tag{CF1}
\]

axis norm 记为

\[
C_*:=\frac{g_0a_2B}{2},
\qquad
N_{\rm ax}=C_*^2+R_0^2,
\qquad
N_c=\frac{N_{\rm ax}}E.
\]

Good square-Plücker 系统使用

\[
S_-=\Pi_-\overline{\Pi_+}K,
\qquad
S_+=\Pi_+\overline{\Pi_-}\,\overline K,
\qquad
N(K)=N_c,
\]

以及

\[
2\,5^{m-T}\widehat\Delta_1
=
\overline{\Pi_+}^{\,2}K h_+
-
\overline{\Pi_-}^{\,2}\overline K h_-,
\tag{G1}
\]

\[
2\,5^{T-m_2}\widehat\Delta_U
=
\overline{\Pi_+}^{\,2}K j_+
-
\overline{\Pi_-}^{\,2}\overline K j_-.
\tag{G2}
\]

最新 continuation 已证明

\[
\log(B_+B_-)=o(S),
\]

且 selected / conjugate orientation 在 \(\Delta_U\) 中的重复总质量均为 \(o(S)\)。

---

### 2. 一个此前未单独写出的 \(\Delta_U\)-norm cofactor identity

已有精确式

\[
5^{T-m_2}L_U=C_*d-iR_0c,
\qquad
L_U=\Pi\Delta_U.
\]

取范数：

\[
C_L5^{2(T-m_2)}N(\Delta_U)
=C_*^2d^2+R_0^2c^2.
\]

另一方面

\[
C_*^2+R_0^2=EN_c,
\qquad
c^2-d^2=EH_J.
\]

所以右端可以完全改写为

\[
\begin{aligned}
C_*^2d^2+R_0^2c^2
&=(C_*^2+R_0^2)d^2+R_0^2(c^2-d^2)\\
&=E(d^2N_c+R_0^2H_J).
\end{aligned}
\]

因此得到精确恒等式

\[
\boxed{
d^2N_c+R_0^2H_J
=
\frac{C_L}{E}
5^{2(T-m_2)}N(\Delta_U).
}
\tag{NcU-elim}
\]

它与已有

\[
\boxed{
\widetilde r^{\,2}5^{4T-2m}N_c
-g_0^2a_2^22^{2m-4}H_R
=
\frac{C_L}{E}N(\Delta_1)
}
\tag{Nc1-elim}
\]

形成一对：前者控制 \((N_c,H_J)\)，后者控制 \((N_c,H_R)\)。

#### Good 的 rational norm 形式

Bad 已关闭，同时 conjugate overlap 已是 \(o(S)\)，故 full rational Good 主质量满足

\[
\boxed{
\log\gcd(C_L,N(\Delta_U))=o(S).
}
\tag{Good-norm}
\]

由 `(NcU-elim)`，删去 \(C_L/E\) 与 coefficient exceptional core 后等价地有

\[
\boxed{
\log\gcd
\bigl(C_L,d^2N_c+R_0^2H_J\bigr)
=o(S).
}
\tag{Good-cofactor-unit}
\]

所以 Good 可以完全翻译为 cofactor 层的一条 **unit condition**，而不必继续携带 \(\Delta_U\)。

---

### 3. main prime 的精确 slot theorem

只写 \(D_+\)；\(D_-\) 完全共轭对称。

固定 main

\[
p^h\Vert D_+,
\qquad
p=\pi\bar\pi,
\qquad
\pi^h\Vert\Pi_+.
\]

删去 exceptional core 后

\[
p\nmid2T_c,
\qquad
p\nmid h_-j_-,
\]

并且 Good / conjugate exclusion 给

\[
v_\pi(\widehat\Delta_U)
=v_{\bar\pi}(\widehat\Delta_U)=0.
\]

定义四个非负深度

\[
r:=v_p(h_+),
\qquad
j:=v_p(j_+),
\]

\[
k:=v_\pi(K),
\qquad
\bar k:=v_{\bar\pi}(K).
\]

#### 3.1 rational endpoint repeat 互斥

由

\[
j_-h_+-j_+h_-=2T_c
\]

且右端为 \(p\)-unit，立刻得到

\[
\boxed{\min(r,j)=0.}
\tag{Slot-RJ}
\]

也就是说，同一 main prime 不可能同时在 \(R_+\) 与 \(J_+\) 的 reduced cofactor 中继续获得正深度。

#### 3.2 Good 强迫 \(K\) 只可能使用 conjugate orientation

在 `(G2)` 的 \(\bar\pi\)-valuation 上：

- 第一项含 \(\overline{\Pi_+}^{\,2}\)，故 valuation 至少 \(2h\)；
- 第二项的 valuation 为 \(k\)，因为 \(j_-\) 与 \(\overline{\Pi_-}\) 都是 \(p\)-unit；
- 左端是 \(\bar\pi\)-unit。

故必有

\[
\boxed{k=0.}
\tag{K-orientation}
\]

于是 main \(p\)-part若进入 \(K\)，只能进入 \(\bar\pi\)-orientation。

特别地

\[
\boxed{v_p(N_c)=\bar k.}
\tag{Nc-slot}
\]

再看 `(G2)` 的 selected \(\pi\)-valuation。两项 valuation 分别为

\[
j,\qquad \bar k.
\]

左端为 unit，因此

\[
\boxed{\min(j,\bar k)=0.}
\tag{Slot-JK}
\]

也就是说，`next-J` 与 axis/carrier repeat 同样逐素数互斥。

综合 `(Slot-RJ)` 与 `(Slot-JK)`：

\[
\boxed{
j>0\Longrightarrow r=\bar k=0.}
\tag{J-isolated}
\]

而 \(r\) 与 \(\bar k\) 可以同时为正。

---

### 4. radius repeat 的精确分解

令

\[
a:=v_\pi(\widehat\Delta_1).
\]

conjugate overlap exclusion 说明它同时也是 main rational depth

\[
a=v_p(N(\Delta_1)).
\]

由 `(G1)` 在 selected \(\pi\) 上，两项 valuation 正好是

\[
r,\qquad\bar k.
\]

因此：

- 若 \(r<\bar k\)，则 \(a=r\)；
- 若 \(\bar k<r\)，则 \(a=\bar k\)；
- 若 \(r=\bar k\)，还可能发生进一步 unit cancellation。

统一写成

\[
\boxed{
a=\min(r,\bar k)+\varepsilon_p,}
\tag{Radius-split}
\]

其中

\[
\varepsilon_p\ge0
\]

且

\[
\boxed{
\varepsilon_p>0
\Longrightarrow r=\bar k.
}
\tag{Pure-equal}
\]

特别地，当

\[
r=\bar k=0,
\qquad
\varepsilon_p>0,
\]

radius repeat 完全来自 `(G1)` 中两个 \(p\)-units 的高阶 cancellation；本文称之为

\[
\boxed{\text{pure-radius slot}.}
\]

这正是简单 slot-counting 无法删掉的通道。

注意 `J-isolated` 并不禁止 pure-radius：若 \(j>0\)，则 \(r=\bar k=0\)，此时 `(G1)` 仍可能出现 \(\varepsilon_p>0\)。

---

### 5. 同一结论的纯 rational cofactor 版本

`(Nc1-elim)` 在 main \(p\) 上所有显式 coefficient 都是 units。结合

\[
v_p(N_c)=\bar k,
\qquad
v_p(H_R)=r,
\]

可把 `(Radius-split)` 完全写成

\[
\boxed{
v_p(N(\Delta_1))
=
v_p\!\left(
\widetilde r^{\,2}5^{4T-2m}N_c
-g_0^2a_2^22^{2m-4}H_R
\right).
}
\tag{Radius-rational}
\]

而 Good 则由 `(NcU-elim)` 给出

\[
\boxed{
p\nmid d^2N_c+R_0^2H_J.}
\tag{Good-rational-local}
\]

因此 Good 的 local algebra 已经可以完全压缩成三个 cofactor slots

\[
H_R,\qquad H_J,\qquad N_c
\]

和一条 equal-depth cancellation `(Radius-rational)`。

这一步不再需要新 Gaussian quotient。

---

### 6. radius repeat 等价于完整拼接分子 repeat

已有 terminal exact identities

\[
g_0(\alpha-a_3)
=2\cdot5^T(UA_0+R_0),
\tag{6.1}
\]

\[
VA_0-g_0a_3
=2\cdot5^TR_0.
\tag{6.2}
\]

由 (6.2)

\[
g_0a_3=VA_0-2\cdot5^TR_0.
\]

代入 (6.1)：

\[
\begin{aligned}
g_0\alpha
&=VA_0+2\cdot5^TUA_0\\
&=(V+2\cdot5^TU)A_0.
\end{aligned}
\]

而

\[
V=2^HZ-5^TU,
\]

故得到新的 exact bridge

\[
\boxed{
g_0\alpha=(2^HZ+5^TU)A_0.}
\tag{Concat-radius}
\]

对 main \(p^h\Vert C_L\)：

\[
p\mid V,
\qquad
(U,V)=(Z,V)=1,
\qquad p\ne2,5.
\]

所以若 \(p\mid2^HZ+5^TU\)，则它同时整除和与差，从而整除 \(2^{H+1}Z\)，矛盾。故

\[
p\nmid2^HZ+5^TU.
\]

再删去 \(p\mid g_0\) 的 exceptional core，有

\[
\boxed{v_p(A_0)=v_p(\alpha).}
\tag{Radius=Concat}
\]

与 continuation 中

\[
v_p(A_0)=v_\pi(\Delta_1)
\]

合并：

\[
\boxed{
\text{secondary/radius repeat}
\Longleftrightarrow
\text{full concatenated numerator }\alpha\text{ repeat}
}
\tag{Secondary=Radius=Concat}
\]

逐 main prime-depth 成立。

这把 pure-radius 从“神秘 Gaussian cancellation”重新翻译成了十进制 digit-shell 问题。

---

### 7. radius 的 digital Gaussian carrier

令

\[
Y:=2\,10^dA_{12}.
\]

numerator reconstruction

\[
UA_0+R_0=g_0B10^dA_{12}
\tag{7.1}
\]

在 radius prime \(p\mid A_0\) 上给

\[
R_0\equiv g_0B10^dA_{12}\pmod{p^a}.
\]

#### \(D_+\) channel

由

\[
\Pi_+\mid C_*+iR_0,
\qquad
C_*=\frac{g_0a_2B}{2},
\]

消去公共 unit 得

\[
\boxed{
\Pi_{R,+}\mid a_2+iY.
}
\tag{Radius-G+}
\]

#### \(D_-\) channel

同理

\[
\boxed{
\Pi_{R,-}\mid a_2-iY.
}
\tag{Radius-G-}
\]

若将两 sign 统一定向为

\[
\Gamma_R:=\Pi_{R,+}\overline{\Pi_{R,-}},
\]

则

\[
\boxed{
\Gamma_R\mid a_2+iY.
}
\tag{Radius-digital}
\]

这是 pure-radius 的自然 decimal Gaussian carrier。

---

### 8. radius digital carrier 与 axis carrier 的直接 resultant 仍然退化

full rational axis carrier 为

\[
\Gamma:=\Pi_+\overline{\Pi_-}\mid C_*+iR_0.
\]

若同一 radius subcore 同时进入 `(Radius-digital)`，最自然的 \(2\times2\) determinant 是

\[
C_*Y-R_0a_2.
\]

利用

\[
C_*Y
=
\frac{g_0a_2B}{2}\cdot2\,10^dA_{12}
=a_2g_0B10^dA_{12}
\]

与 (7.1)，得到

\[
\boxed{
C_*Y-R_0a_2
=a_2UA_0.
}
\tag{Radius-resultant-collapse}
\]

右端恰好重新含有 radius payer \(A_0\)。

所以“axis Gaussian carrier + radius digital Gaussian carrier 直接取 determinant”不会产生新独立模量；它只把 `(Radius=Concat)` 换了一种写法。

**状态：`失效/降级`。**

---

### 9. 为什么简单的总容量相加关不掉 Good

当前三个 cofactor 的 frontier Archimedean heights 为

\[
\log H_R
=1.617767155236\ldots S+o(S),
\]

\[
\log H_J
=1.602059991328\ldots S+o(S),
\]

而

\[
N_c=\frac{C_*^2+R_0^2}{E}
\]

具有约 \(2S\) 的尺度。

同时

\[
\log N(\Delta_1)
=1.308883577618\ldots S+o(S).
\]

因此每个单独 slot 都有能力承载一个 \(S\)-级 main divisor。互斥关系

\[
\min(r,j)=0,
\qquad
\min(j,\bar k)=0
\]

虽然真实，但仅靠这些容量上界仍得不到

\[
\text{总容量}<S.
\]

尤其 pure-radius 只消耗 \(N(\Delta_1)\) 的 residual capacity，而该 residual height 本身大于 \(S\)。

所以 continuation §18 中的 “slot capacity” 必须理解为：

> 先做逐素数 mutually-exclusive allocation，再对最后留下的 equal-depth / pure-radius slot 寻找 **新的 digit-shell strict bound**。

不能把它简化成对 \(H_R,H_J,N_c,N(\Delta_1)\) 的普通高度求和。

---

### 10. 当前严格压缩后的 Good frontier

截至本文，full rational Good 可以重写成以下有限类型的 local network：

1. `next-R`：\(p\mid H_R\)；
2. `next-J`：\(p\mid H_J\)；
3. `axis/carrier`：\(p\mid N_c\)，且只能取与 selected \(\Pi\) 相反的 Gaussian orientation；
4. `radius overlap`：由 \(\min(v_p(H_R),v_p(N_c))\) 自动支付；
5. `pure-radius`：\(H_R,N_c\) 均为 units（或 equal-depth 已抽掉 baseline）后，`(Nc1-elim)` 的 unit-unit cancellation；它等价于 \(p\mid\alpha\)。

并且：

\[
\boxed{
\text{next-J 与 next-R / axis-repeat 逐素数互斥；}
}
\]

\[
\boxed{
\text{Good 同时要求 }p\nmid d^2N_c+R_0^2H_J;
}
\]

\[
\boxed{
\text{pure-radius 的最后新信息位于完整拼接分子 }\alpha\text{ 的 digit shell。}
}
\]

因此 full rational Good 的真正未决核已经从“若干未定义 slots”缩成：

\[
\boxed{
\text{equal-depth }(H_R,N_c)
\text{ cancellation}
\;\cup\;
\text{pure numerator-shell contact }(C_L,\alpha).
}
\]

下一步若继续 full rational Good，首选目标应是一个 **primitive digit-shell lemma**：证明 main pair-max modulus 在已经满足 rational sign contact 与 `(Good-cofactor-unit)` 后，不可能再以正线性高度进入 \(\alpha\) 或 equal-depth residual。

若这个 lemma 只能再次退回 `(Concat-radius)` / hidden square / `(CF1)`--`(CF5)`，则 full rational Good 的局部代数已经真正闭包，应停止继续造 local resultant，转向 genuine-Gaussian split-prime/digit-shell branch。

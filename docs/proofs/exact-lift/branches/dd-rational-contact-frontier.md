# DD frontier：rational contact、Bad/Good 分解与 cofactor 临界系统

> 状态：本文是 [`double-deficit.md`](double-deficit.md) terminal frontier 的后续证明记录。
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

## 1. 已有 terminal 基线

本文直接依赖 `double-deficit.md` 已建立的 terminal normalization：

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

## 2. general overlap skeleton 精确退化为 terminal phase

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

## 3. denominator-only quotient \(R_2\) 与 Farey entropy collapse

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

## 4. rational cross-resultant

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

### 4.1 cross-resultant cofactor 的固定 \(5S\) gap

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

### 4.2 与 near-axis norm 的审计

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

## 5. rational sign channels 与 \(C_L\) 分解

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

### 5.1 sign 同时固定 Gaussian orientation

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

## 6. sign-Farey reduction

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

### 6.1 contact 深度几乎处处是 full depth

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

## 7. 固定 rational-contact 曲面

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

## 8. first-order contact 的高度预算精确饱和

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

## 9. standalone blow-up / tangent condition 的审计

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

## 10. denominator-transformed Gaussian quotient

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

## 11. Bad/Good 分解

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

### 11.1 single-slot orientation allocation

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

## 12. full rational-contact cofactor Lorentz system

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

### 12.1 exact \(2S\) cancellation

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

### 12.2 generic real + 5-adic proximity 又精确临界

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

## 13. Bad repeat 的精确 quotient / numerator / digital / concat 投影

**状态：`已严格完成`。**

### 13.1 quotient residual

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

### 13.2 numerator reconstruction projection

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

### 13.3 digital Gaussian projection

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

### 13.4 full concat numerator projection

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

## 14. Bad 的 cofactor projection

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

## 15. 现成的 \(N_c\) elimination

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

## 16. source/projective 独立性审计

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

## 17. 已严格判死或降级的路线

这一节必须保留，防止后续 agent 重开死路。

### 17.1 standalone blow-up tangent：`失效/降级`

见 `(Tangent-collapse)`。二阶 oriented contact 被 hidden square 自动提供，不能当第二份 local height。

### 17.2 cross-resultant 与 near-axis norm 直接 gcd：`失效/降级`

见 `(Hidden-cross)`。两者差精确等于 \((C_LP_1/2)^2\)，不是独立 targets。

### 17.3 D1/R22 与 secondary line 的同-prime resultant：`失效/降级`

最自然的 U-side、Z-side resultants 都精确退回 secondary norm；\(\Delta_U,\Delta_Z\) 的 cross determinant 只由 \((C_0/C_L)\bar\Pi\) 支付。

### 17.4 `Bad -> bottom determinant` bridge：`失效/降级`

曾尝试证明 digital Gaussian Bad carrier 会强迫

\[
B_\sigma\mid j_-h_+-j_+h_-.
\]

这不能由 primitive carrier tetrahedron 推出。main \(C_L\)-prime 上已有

\[
v_p(\Delta_{12})=v_p(\Delta_{13})=0.
\]

carrier tetrahedron 只给 determinant valuation 的 ultrametric order type，不会凭空把 Bad orientation 送到底边。

### 17.5 \(t_p+b_p\le h_p\)：`失效/降级`

full rational branch 已经几乎处处有 \(t_p=h_p\)。Bad repeat 是除去完整 \(p^{h_p}\) contact 后在 Gaussian quotient 中产生的新 cancellation，并不由 \(h_p-t_p\) 支付。

### 17.6 单靠 \(C_0\) 与 digital norm 的 gcd：`失效/降级`

Bad primes 本来就在 \(C_L\mid C_0\) 主 core 中。reconstruction 只把 \(A_{12}\) 固定为 p-adic residue，并不禁止

\[
4\,10^{2d}A_{12}^2+c_\sigma a_2^2
\equiv0\pmod{p^r}.
\]

不能从 reducedness 直接推出这个 gcd 只有 \(10^{o(S)}\)。

### 17.7 模 \(A_0\) 的“小 gcd 强迫小误差整除”：`失效/降级`

从

\[
A_0\mid q_c^2K-E
\]

与 \((A_0,q_c^2K)\) 小，不能推出 \(A_0/g\mid E\)。正确的 rational-spacing 分析说明 small gcd 允许更细 spacing；需要的是 large common divisor。

### 17.8 generic first-order GCD / Subspace / Ridout closure：`失效/降级`

`(Height-critical)` 与第 12.2 节都显示 leading-order budget 精确饱和。继续套同类型 generic theorem 只能再次得到临界等号。

### 17.9 first-order hyperbolic determinants：`失效/降级`

\[
\begin{pmatrix}b&A\\c&d\end{pmatrix}
\]

的 \(R_\pm,J_\pm\) 一阶代数满足 Brahmagupta/Plücker 恒等式，所有自然 cross determinants 最终退回 `(SF-det)`。这个 first-order \(2\times2\) algebra 已闭合。

---

## 18. 当前精确分支图

### 18.1 genuine-Gaussian branch

若

\[
\boxed{C_G=10^{\varepsilon S+o(S)}}
\]

对某个 \(\varepsilon>0\)，则这些 main primes 不满足 \(A\equiv\pm b\)。所有 rational denominator-contact resultants 在它们处为单位。

这支需要真正新的 Gaussian/projective same-prime elimination；本文尚未关闭。

### 18.2 full rational-contact branch

若

\[
\boxed{D_+D_-=C_L^{1-o(1)},}
\]

则先进入 exact critical cofactor system `(CF1)`--`(CF5)`，再分：

#### Bad

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

#### Good

\[
\log(G_+G_-)
\ge\frac12S-o(S).
\]

至少半个 \(C_L\)-height 在 full rational contact 后与 \(N(\Delta_U)\) 横截。这一支不能再靠 first-order rational contact 收费；应直接追踪 \(N(\Delta_U)\) rough core 的来源，并与 \((C_L,L_{\rm clean})=10^{o(S)}\)、source/projective transversality 联立。

---

## 19. 当前首选证明任务

**状态：`待证`。**

下一次工作不要再扩对象。首选目标固定为：

### 19.1 Bad branch

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

### 19.2 若 Bad 消元再次退化

若上述消元精确回到 `(CF1)`--`(CF5)` 或 hidden square，立即停止在 rational first-order algebra 中继续造 eliminant，转向 genuine-Gaussian branch。

---

## 20. 状态总表

- **`已严格完成`（仅 frontier 条件蕴含）**：general overlap 精确退化、\(R_2\) matrix、Farey subexponential compression、rational cross-resultant、sign-channel 分解、full-depth rational contact、fixed surface、critical height budget、cofactor Lorentz system `(CF1)`--`(CF5)`、Bad 的 quotient/numerator/digital/concat/cofactor 多重投影、`(Nc-elim)`、single-slot orientation allocation、source/projective transversality audit。
- **`失效/降级`**：standalone tangent/blow-up、cross-resultant 与 near-axis norm 直接 gcd、U/Z-side same-prime resultants、Bad 到 bottom determinant、\(t+b\le h\)、单靠 \(C_0\)-digital norm gcd、错误的模 \(A_0\) small-gcd argument、generic first-order GCD/Subspace/Ridout、继续挖 first-order hyperbolic determinants。
- **`待证`**：Bad 的 \(N_c\) oriented elimination、Good 的 transverse rough-core closure、genuine-Gaussian branch 的 uniform same-prime elimination。
- **全局状态不变**：DD 尚未证明为空；当前最强全局渐近结论仍为
  \[
  \limsup_{\rm DD}\frac{n_3}{S}
  \le6.308883577618\ldots,
  \]
  其阈值依赖 Schmidt Subspace Theorem 且非有效；本文新增的所有 \(o(S)\) 与 rational-contact 结论都只在假想 frontier sequence 上使用。

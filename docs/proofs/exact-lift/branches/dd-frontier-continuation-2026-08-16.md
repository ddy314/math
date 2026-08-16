# DD frontier continuation：Good closure audit、orientation reconstruction 与双 lattice sheet

> **研究日期：2026-08-16**  
> **适用范围：**仅针对假想满足
> \[
> \frac{n_3}{S}\to6.308883577618\ldots
> \]
> 的 DD frontier sequence。  
> **状态边界：**本文记录 `dd-rational-contact-frontier.md` 之后的新推进与 no-go 审计。本文**不证明 DD 全局空性**，也不给出有效绝对的 \(S\) 上界。  
> **阅读约定：**若本文与 `dd-rational-contact-frontier.md` 中“Bad 尚待关闭”等旧状态冲突，以本文的更新状态为准；但所有结论仍只在 frontier 条件下使用。

---

## 1. 基线与符号

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

# 第一部分：full rational-contact 中 Bad 的关闭与 Good 正规形

## 2. Bad branch 的更新状态：已关闭

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

## 3. Good 的 Gaussian square-Plücker 正规形

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

## 4. Good repeat 的本质：radius excess

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

# 第二部分：pair-max Gaussian local algebra 的闭包审计

## 5. derivative Gaussian integer 唯一重构 orientation

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

## 6. derivative line 自动恢复 secondary line

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

## 7. 正确的 Newton second-order resultant 仍然退化

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

## 8. derivative repeat、secondary repeat、radius repeat 等价

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

# 第三部分：near-square 的完全展开与 no-go

## 9. normalized near-square 的两个因子其实就是旧 source channels

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

# 第四部分：两个 exact rank-2 lattice sheets

## 10. denominator triangle

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

## 11. \(\delta_*\) 是 denominator triangle 的 projective thickness

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

## 12. source / numerator triangle

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

## 13. 两张 sheet 的自然 mixed direction 在 main \(C_L\) 上横截

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

# 第五部分：orientation entropy 与 counting 的进一步坍缩

## 14. fixed \(C_L\) 后不再需要预先固定 \(\Pi\)

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

## 15. full rational-contact 的 moving-core counting 可降到 subexponential

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

# 第六部分：已严格判死 / 降级的新路线

## 16.1 三 Gaussian quotients 再做 projective determinant

\(\Delta_1,\Delta_U,\Delta_Z\) 的三条 pairwise determinant 在 Archimedean 与 finite places 上都精确饱和 product formula；第三个 quotient 不增加 projective rank。其 closure payer 是 \(R_2\)。

**状态：`失效/降级`。**

## 16.2 pair-max second-order Newton resultant

正确 Newton lift result 为 (7.1)，天然含 \(C_L^2\)。

**状态：`失效/降级`。**

## 16.3 source Gaussian factor / quartic reciprocity

将 prefix Gaussian vector按 source factorization写成 \(\Lambda_{\rm src}K_{\rm src}\) 后，试图把 derivative line视为 \(\Pi\) 与 \(\Lambda_{\rm src}\) 的新 reciprocity condition。完整代入后 \(\Lambda_{\rm src}\) 整体可约出，条件退回 hidden-square 的两个一次因子。

**状态：`失效/降级`。**

## 16.4 near-square 的“小 CRT root”

由 (9.1)--(9.5)，小因子的 rough core就是 \(Z\)，大因子就是 \(q_c^2U\) source channel；完整 phase退回 numerator reconstruction。

**状态：`失效/降级`。**

## 16.5 denominator lattice 的 Minkowski shortest vector

\(\mathcal D\) 的 row lattice 面积为 \(10^{S+o(S)}\)，因此存在 \(10^{S/2+o(S)}\) 级短向量。但 row operation 不保持原 decimal carrier 语义，且其法向量 modulo \(C_L\) 给出的 slope 与 pair-max Gaussian \(\sqrt{-1}\) orientation 相差一个正线性 source scaling。

因此不能把 shortest vector 偷换成 \((\Re\Pi,\Im\Pi)\) 并构造下降。

**状态：`失效/降级`。**

## 16.6 两张 lattice sheet 自动共享 main \(C_L\) contact

`Mixed-transverse` 明确给出相反结论：自然 mixed determinant 与 \(C_L\) 的 gcd 只有 \(10^{o(S)}\)。

**状态：`失效/降级`。**

---

# 第七部分：当前真正剩余的 frontier

## 17. 局部 Gaussian algebra 已基本闭包

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

## 18. full rational-contact Good 的剩余问题

Bad 已关闭，full rational-contact 的 main mass进入 Good。此前 Good-square 系统给出 conjugate orientation 的 square-depth CRT，但所有 ordinary norm / determinant 会退回 sign-Farey / hidden-square critical geometry。

`Mixed-transverse` 又说明自然 source sheet不能接收同一份 main \(C_L\) contact。

因此 full rational Good 的剩余质量只能藏在已经 critical 的 cofactor/Plücker sheet 中。下一步应当做**容量分配**而非再造 quotient：

1. 将 radius-repeat、next-repeat、carrier-repeat 等槽按逐素数 depth统一分配；
2. 使用 Bad closure 与 `Mixed-transverse` 排除已知槽；
3. 证明剩余 main mass只能进入 cofactor system 的唯一 slot；
4. 对该 slot 寻找独立于 `(CF1)`--`(CF5)` 的 strict height bound。

---

## 19. genuine-Gaussian 的剩余问题

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

## 20. 当前严格状态摘要

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

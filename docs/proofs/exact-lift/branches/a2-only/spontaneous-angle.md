# A2 spontaneous-angle master polynomial

> **依赖：** `core.md` §§14.1–15、`phase-and-defect.md` §§1.1–1.6、`height-cofactor.md`、`decimal-prefix-bridge.md`。
>
> **严格状态：**本文补上旧 §14.2-III 一直缺失的“第二 angle polynomial”。它把 `E_1` 的 spontaneous contact 变成关于 source-normalized ratio 的一个显式一次式，并用三个小 resultant 精确恢复 source / q-side / f-side 的旧边界。另给出 `\widehat{\mathcal T}_2` 的全局 pure-decimal carrier polynomial。本文仍**不宣称 A2 全局关闭**。

---

## 1. 避免 `z` 重名的统一记号

当前只处理 reflection endpoint，故

\[
a_1=9,\qquad \sigma_5=0,\qquad E_5=\lambda.
\]

沿用

\[
M=m_2,\qquad T=10^m,
\]

\[
x=\frac{b_2}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}}.
\]

`phase-and-defect.md` 原来把 source-normalized ratio 也记为 `z`；而后续 `source-discriminant.md` 已用 `z=q5^\lambda`。为避免混淆，本文把前者改记为

\[
\boxed{
r_s:=\frac{5^\lambda D_0}{c_Q}.}
\tag{1.1}
\]

于是 phase Hensel 线为

\[
\boxed{
\Phi_s(x,r_s)
=(99x-4)r_s-2x-4.
}
\tag{1.2}
\]

并有

\[
q=\frac{U(x+2)}{2c_Q},
\qquad
f=\frac{U}{2D_0}\bigl(r_s(x+2)+2x\bigr),
\qquad U=5^M.
\tag{1.3}
\]

令

\[
\Sigma=c_Q^2qf,
\qquad
\mathfrak n=2c_u\sigma
\tag{1.4}
\]

为 core §14.2 的 denominator/source 两个尺度。`phase-and-defect.md` 已证明

\[
\boxed{
\frac{\mathfrak n}{\Sigma}
=
\frac{x\Phi_s(x,r_s)}
{(x+2)\bigl(r_s(x+2)+2x\bigr)}.
}
\tag{1.5}
\]

---

## 2. `已严格完成`：`E_1` 恰由一个一次 angle polynomial 控制

`hensel.md` 恢复的旧第二层精确式是

\[
\boxed{
E_1=5^\lambda L_0^2-\mathfrak n a_2^2.
}
\tag{2.1}
\]

在当前 `a_1=9` endpoint，

\[
L_0=-U10^{M-1}(225x^2-y),
\qquad
a_2=y10^{M-1}.
\tag{2.2}
\]

另一方面由 (1.3)，

\[
\Sigma
=
\frac{c_QU^2}{4D_0}
(x+2)\bigl(r_s(x+2)+2x\bigr).
\tag{2.3}
\]

所以

\[
\frac{5^\lambda L_0^2}{\Sigma a_2^2}
=
\frac{4r_s(225x^2-y)^2}
{y^2(x+2)\bigl(r_s(x+2)+2x\bigr)}.
\tag{2.4}
\]

与 (1.5) 相减，得到真正缺失的 spontaneous angle polynomial：

\[
\boxed{
\Omega_{\rm sp}(x,y,r_s)
:=
4r_s(225x^2-y)^2
-xy^2\Phi_s(x,r_s).
}
\tag{2.5}
\]

并且不是只有模素数关系，而是精确有理恒等式

\[
\boxed{
\frac{E_1}{\Sigma a_2^2}
=
\frac{\Omega_{\rm sp}}
{y^2(x+2)\bigl(r_s(x+2)+2x\bigr)}.
}
\tag{2.6}
\]

因此对于与 `2,3,5,c_Q,q,f,\mathfrak n,\mathcal N_0` 分离的 genuine non-`3` spontaneous inert prime，`a_2` 也是单位，故

\[
\boxed{
p\mid E_1\iff p\mid\Omega_{\rm sp}.}
\tag{2.7}
\]

这补上了 `hensel.md` 末尾“为 spontaneous angle excess 寻找第二个角度多项式”的开放项。

---

## 3. `已严格完成`：spontaneous root 是唯一的一次 Hensel root

写

\[
d_s:=225x^2-y.
\]

(2.5) 关于 `r_s` 只有一次：

\[
\boxed{
\Omega_{\rm sp}
=A_{\rm sp}(x,y)r_s
+2xy^2(x+2),
}
\tag{3.1}
\]

其中

\[
\boxed{
A_{\rm sp}(x,y)
=4d_s^2-xy^2(99x-4).
}
\tag{3.2}
\]

在真正 spontaneous prime 上若
`p\nmid2xy(x+2)`，则 `p\mid\Omega_sp` 自动强迫 `A_sp` 为单位；否则常数项也必须为零，矛盾。因此

\[
\boxed{
r_s\equiv
-\frac{2xy^2(x+2)}{A_{\rm sp}(x,y)}
\pmod p.}
\tag{3.3}
\]

所以 spontaneous channel 不是新的高维 Hensel 树：在第一层分离假设下，它只有一个 source-ratio root，之后的 prime-power lift 也是唯一的一维 lift，除非另有固定 bad-reduction prime 使分离条件失效。

---

## 4. `已严格完成`：真实 endpoint window 中 `Omega_sp` 严格远离零

当前危险 endpoint 已有

\[
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1,
\qquad r_s>0.
\tag{4.1}
\]

因此

\[
d_s=225x^2-y>\frac94-1=\frac54.
\]

同时 `x(99x-4)` 在该区间递增，所以

\[
xy^2(99x-4)
<x(99x-4)
<\frac{244}{361}.
\]

故

\[
\boxed{
A_{\rm sp}
>\frac{25}{4}-\frac{244}{361}
=\frac{8049}{1444}>5.
}
\tag{4.2}
\]

从而

\[
\boxed{
\Omega_{\rm sp}
>\frac{8049}{1444}r_s>0.
}
\tag{4.3}
\]

结合 (2.6)，还重新得到一个严格的 endpoint 实数结论：

\[
\boxed{E_1>0.}
\tag{4.4}
\]

注意这不是模 `p` 排除；它的用途是说明 spontaneous congruence 的真实一次根在实轴上位于负侧，而实际 `r_s` 为正。若要把该符号错位升级成空性，仍需要 prime-power modulus / natural representative 的高度输入。

---

## 5. `已严格完成`：三个小 resultant 把旧 prime-source 图接成一张图

定义归一化 prefix defect

\[
\boxed{
\Delta_0(x,y)
:=2025x^2-18y-y^2
=\frac{\Delta_{\rm pref}}{10^{2M-2}}.
}
\tag{5.1}
\]

### 5.1 source line

直接对 `r_s` 求 resultant：

\[
\boxed{
\operatorname{Res}_{r_s}
(\Phi_s,\Omega_{\rm sp})
=
8(x+2)(225x^2-y)^2.
}
\tag{5.2}
\]

因此 source Hensel line 与 spontaneous line 的交点，在与 q-side 分离后只能回到

\[
225x^2-y,
\]

也就是 `hensel.md` 的 `D_src/L_0` 半深度 contact。没有第四种 source/spontaneous overlap。

### 5.2 f-side denominator line

令

\[
F_f:=r_s(x+2)+2x.
\]

则

\[
\boxed{
\operatorname{Res}_{r_s}
(F_f,\Omega_{\rm sp})
=-200x^3\Delta_0(x,y).
}
\tag{5.3}
\]

所以 f-denominator 与 spontaneous angle 的交点恰好就是旧 prefix-defect contact。

### 5.3 q-side denominator line

q-side 在 scale-free 坐标中由 `x+2=0` 表示。直接代入：

\[
\boxed{
\Omega_{\rm sp}(-2,y,r_s)
=400r_s\Delta_0(-2,y).
}
\tag{5.4}
\]

所以 q-side 同样只回到同一个 `Delta_pref`。

综上，旧 §14.2 的三类来源现在不是三套散乱条件：

\[
\boxed{
\begin{array}{ccl}
\text{source}&\longleftrightarrow&\Phi_s,\\
\text{denominator}&\longleftrightarrow&x+2\text{ 或 }F_f,\\
\text{spontaneous}&\longleftrightarrow&\Omega_{\rm sp},
\end{array}}
\]

而它们两两相交时只产生既有的 `D_src` 或 `Delta_pref`，没有新的未命名 prime pool。

---

## 6. `已严格完成 / 审计`：与 external double-root 的 resultant 只恢复 `sqrt(55)` gate

`source-discriminant.md` 使用的 source ratio

\[
r=\frac{5^\lambda2^mg}{c_Q}
\]

与本文 `r_s` 相同，因为 reflection 中 `D_0=2^mg`。external double-root 的 discriminant line 因而是

\[
\boxed{
\Gamma_W(x,r_s)
:=55r_s^2(x+2)^2-49x^2.
}
\tag{6.1}
\]

记 `A_sp` 如 (3.2)。消去 `r_s` 得

\[
\boxed{
\operatorname{Res}_{r_s}
(\Omega_{\rm sp},\Gamma_W)
=
x^2\left[
220y^4(x+2)^4-49A_{\rm sp}^2
\right].
}
\tag{6.2}
\]

所以在所有相关量均为单位时，再次得到

\[
\left(\frac{55}{p}\right)=1.
\]

这与 `source-discriminant.md` 的 double-root character 相同，因而 (6.2) **不应被重复收费成第二个 quadratic obstruction**。它的真正价值是：spontaneous/external overlap 现在也有了一个明确的二变量 resultant，可与 prefix/length 条件继续消元。

---

## 7. `已严格完成`：所有 odd cofactor carrier 都有一个 pure-decimal 二次接口

`endpoint-lattice.md` 的

\[
\widehat{\mathcal T}_2
=
2^mc_u^2g^2\mathscr S_0
-Q_0^2 5^{2\lambda-d}XY
\]

可完全乘回原始 decimal blocks。利用

\[
b_2=2^{M+m+1}c_ug,
\qquad
Q=2^{M+1}Q_0,
\qquad
N_0=5^{\lambda-2d}XY,
\qquad
m=\lambda+d,
\]

得到

\[
\boxed{
\Theta_{\rm dec}
:=b_2^2\mathscr S_0-TQ^2N_0
=2^{2M+m+2}\widehat{\mathcal T}_2.
}
\tag{7.1}
\]

所以 `\widehat{T}_2` 的**全部奇素数支持**，不仅 common-height / denominator 子通道，都等价于纯 decimal quadratic

\[
\Theta_{\rm dec}(K)\equiv0.
\]

又因为

\[
\mathscr S_0
=T(K^2-26)-(2K-9)(2a_3+9T),
\]

以及

\[
\Psi_f=b_2^2(K^2-26)-Q^2N_0,
\]

有

\[
\boxed{
\Theta_{\rm dec}
=T\Psi_f
-b_2^2(2K-9)(2a_3+9T).
}
\tag{7.2}
\]

若再写

\[
\alpha=TK+a_3,
\qquad
F_W(K)=5K^2-36K+55,
\]

则

\[
2a_3+9T=2\alpha-T(2K-9)
\]

给出第二种精确形态

\[
\boxed{
\Theta_{\rm dec}
=T\Phi_H
-2b_2^2(2K-9)\alpha,
}
\tag{7.3}
\]

其中

\[
\boxed{
\Phi_H
:=b_2^2F_W(K)-Q^2N_0.
}
\tag{7.4}
\]

因此任意 odd carrier 与 concatenated numerator `alpha` 的公共部分已经被单个 pure-prefix polynomial `Phi_H` 控制。结合

\[
\alpha=\omega W_q,
\]

common-`alpha` channel 随后严格分成 `W_q` height 与 `omega` content 两类；而真正 `p\nmid\alpha` 的 carrier 才是必须继续由 `Omega_sp / Theta_dec` 联立处理的 pure spontaneous angle channel。

---

## 8. 更新后的开放核

本轮没有证明 spontaneous channel 为空，但把旧的“未知第二角度多项式”问题改写为下面两个明确的一次/二次对象：

\[
\boxed{
\Omega_{\rm sp}(x,y,r_s)=0,
\qquad
\Theta_{\rm dec}(K)=0.
}
\]

并且：

1. `Omega_sp` 与 source line 的 resultant 只回到 `D_src`；
2. 与 q/f denominator line 的 resultant 只回到 `Delta_pref`；
3. 与 external double-root 的 resultant 只回到既有 `sqrt(55)` gate；
4. `Theta_dec` 覆盖 `widehat(T)_2` 的全部 odd support，消除了“只分析 common-height prime 是否遗漏真正 spontaneous carrier”的记号缺口。

下一步真正值得做的是：把 `Omega_sp` 与 `Theta_dec` 通过 third-block exact plane / finite-defect shell 消去 `r_s,a_3`，而不是继续添加 Legendre character。
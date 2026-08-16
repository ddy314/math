# `A_2` source excess closure

> 分支：`agent/a2-hensel-resultant-progress`  
> 状态：**`u`-side / `rho`-supported source inert excess 已严格关闭。**  
> 依赖：[`a2-only.md` §§12.5, 14–15](a2-only.md)，[`a2-hensel-resultant-progress.md`](a2-hensel-resultant-progress.md)。

本文把 source resultant collapse 与 Gaussian rectangle 合并，排除由 `u`-side 残余因子 `rho` 承载的全部 \(3\bmod4\) source excess。

## 1. Source inert prime 必落在 `rho`

`a2-only.md` §12.5 有唯一互素 source split

\[
u=5^{\sigma_5}c_u\rho,
\]

且

\[
p\mid c_u\Longrightarrow p\equiv1\pmod4.
\]

因此若奇素数

\[
p\equiv3\pmod4
\]

来自 \(u\)-side，则它既不可能来自纯五次幂，也不可能进入 \(c_u\)，只能满足

\[
\boxed{p\mid\rho.}
\]

由

\[
D_0=2^{m_3+t-1}\rho,
\qquad
H_s=D_0c_u
\]

立即得到

\[
\boxed{p\mid H_s.}
\]

---

## 2. Resultant 因子就是 Gaussian 正交误差

§14 定义

\[
L_0=U_5a_2-10H_sC_0.
\]

固定斜率

\[
U_5C_0=10H_sA_0
\]

结合

\[
\frac{C_0}{A_0}=5x,
\qquad
x=\frac{b_2}{10^{m_2}},
\qquad
y=\frac{a_2}{10^{m_2-1}}
\]

给出

\[
H_s=\frac{U_5x}{2},
\qquad
C_0=5a_1x\,10^{m_2-1}.
\]

故

\[
\begin{aligned}
L_0
&=U_5y10^{m_2-1}
-10\frac{U_5x}{2}\cdot5a_1x10^{m_2-1}\\
&=U_5 10^{m_2-1}(y-25a_1x^2).
\end{aligned}
\]

即

\[
\boxed{
L_0=-U_5 10^{m_2-1}(25a_1x^2-y).
}
\]

对 source inert prime \(p\equiv3\pmod4\)，有 \(p\ne2,5\)，因此 \(U_5 10^{m_2-1}\) 是 \(p\)-进单位。

由前一文件的 resultant collapse，若

\[
p^{2h}\Vert\sigma,
\qquad
v_p(\Psi_{a_1})\ge h,
\]

则

\[
v_p(25a_1x^2-y)\ge h.
\]

从而

\[
\boxed{v_p(L_0)\ge h\ge1.}
\]

特别地

\[
\boxed{p\mid L_0.}
\]

---

## 3. Gaussian rectangle 给出矛盾

§14 还有

\[
M_0=10H_sP.
\]

由于 \(p\mid H_s\)，得到

\[
\boxed{p\mid M_0.}
\]

Gaussian rectangle 恒等式为

\[
L_0^2+M_0^2
=(U_5^2+100H_s^2)\mathcal N_0.
\]

左端被 \(p\) 整除；而 \(p\mid H_s\) 且 \(p\nmid U_5\)，所以

\[
U_5^2+100H_s^2\equiv U_5^2\not\equiv0\pmod p.
\]

于是

\[
\boxed{p\mid\mathcal N_0.}
\]

现在

\[
\mathcal N_0=C_0^2+a_2^2,
\qquad
C_0=\frac{a_1b_2}{2}.
\]

又因为 \(p\mid\rho\mid u\) 且

\[
b_2=2^{m_2+m_3+t}u,
\]

有

\[
p\mid b_2
\Longrightarrow
p\mid C_0.
\]

因此 \(p\mid\mathcal N_0\) 化为

\[
a_2^2\equiv0\pmod p,
\]

即

\[
p\mid a_2.
\]

这与第二块既约性

\[
\gcd(a_2,b_2)=1
\]

矛盾。

故得到：

\[
\boxed{
\text{不存在任何由 }\rho\text{ 承载的 source inert excess.}
}
\]

---

## 4. 对 §14.2 三分法的影响

若 `a2-only.md` §14.2 中的“source excess”严格指 §12.5 的 `u`-side source pool，则上面的论证已经关闭整个第 II 类：

\[
\boxed{
\text{II. Source excess}=\varnothing.
}
\]

现有主文件使用了未在统一符号表中登记的 \(\mathfrak n\) 和 \(u_0\)。因此在把“第 II 类全部关闭”同步回主状态之前，需要先核对这两个旧符号是否确实只是 `rho`-side/source-norm 的旧记号；若它们还包含额外 source pool，则上面的定理已经关闭其中全部 `rho`-supported 部分，而额外部分必须单独定义后再审计。

这个符号核对是证明语义问题，不能靠猜测跳过。

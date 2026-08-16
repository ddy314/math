# `A_2` source-excess audit after resultant collapse

> 分支：`agent/a2-hensel-resultant-progress`  
> 状态：**上一版“source inert prime 必落在 `rho`”的归类失效；resultant 与 `L_0` 恒等式保留为严格结论。**  
> 依赖：[`a2-only.md` §§12.5, 14–15](a2-only.md)，[`a2-hensel-resultant-progress.md`](a2-hensel-resultant-progress.md)。

## 1. `失效/降级`：不能把 source excess 认成 `rho`-supported prime

旧记号核对给出

\[
u_0=\frac{u}{5^{\sigma_5}}=c_u\rho.
\]

而 `a2-only.md` §14.2 对真正的 source excess 明确记录了分离条件

\[
p\nmid q_Q f c_Q u_0.
\]

因此 source excess prime 特别满足

\[
\boxed{p\nmid\rho.}
\]

所以“\(p\equiv3\pmod4\) 来自 `u`-side，故 \(p\mid\rho\)”并不是 §14.2 的 source excess；它只是另一种 `u`-supported inert prime 情形。上一版据此宣称“第 II 类 source excess 已关闭”的结论撤回，不得使用。

---

## 2. `已严格完成`：resultant 因子等于 Gaussian 正交误差

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

因此前一文件的 resultant collapse

\[
v_p(25a_1x^2-y)\ge h
\]

与旧 source-Hensel 记号完全等价于

\[
\boxed{v_p(L_0)\ge h}
\]

（因为 source inert prime \(p\ne2,5\)，而 \(U_5 10^{m_2-1}\) 是 \(p\)-进单位）。

这不是新矛盾，但它识别出了双 Hensel 系统真正测量的几何量：第二个 Hensel 多项式的消元结果恰好是 Gaussian rectangle 的正交误差 \(L_0\)。

---

## 3. 旧 source-excess 赋值结构的正确恢复

旧 A2 研究记录还给出第二层的精确形态

\[
\boxed{
E_1=5^{E_5}L_0^2-\mathfrak n a_2^2,
}
\]

其中 \(\mathfrak n\) 是 §14.2 所称的 source-side 二平方尺度。

对 source inert prime，若

\[
p^{2h}\Vert\mathfrak n,
\qquad
\alpha=v_p(a_2),
\]

则 source excess 的临界接触要求

\[
\boxed{
v_p(L_0)=h+\alpha}
\]

并进一步研究

\[
v_p\!\left(5^{E_5}L_0^2-\mathfrak n a_2^2\right)
\]

在两项具有相同基础深度 \(2h+2\alpha\) 后还能否产生正奇数额外赋值。

因此 resultant collapse 的真正作用是：它没有直接关闭 source excess，而是把此前的“\(2h:h\) 双 Hensel”重新解释成对 \(L_0\) 的精确半深度接触。下一步必须研究两个归一化单位之间的残余角度消去，不能再把 `rho` 混入这里。

---

## 4. 保留的辅助恒等式

定义

\[
D_{\rm src}=C_0^2-A_0a_2.
\]

则

\[
D_{\rm src}
=a_1 10^{2m_2-2}(25a_1x^2-y),
\]

并且

\[
\Delta_{\rm pref}=D_{\rm src}-a_2P,
\qquad
\mathcal N_0=D_{\rm src}+a_2P.
\]

所以

\[
\boxed{
2D_{\rm src}=\Delta_{\rm pref}+\mathcal N_0,
\qquad
2a_2P=\mathcal N_0-\Delta_{\rm pref}.
}
\]

这组恒等式后续可用于把 source contact 与 prefix-defect / denominator contact 放在同一前缀坐标中比较。

---

## 5. 当前结论

本文件现只保留以下严格进展：

1. resultant factor 与 \(L_0\) 是同一个量；
2. source excess 的旧赋值模型应恢复为
   \[
   E_1=5^{E_5}L_0^2-\mathfrak n a_2^2,
   \quad
   v_p(\mathfrak n)=2h,
   \quad
   v_p(L_0)=h+v_p(a_2);
   \]
3. `rho`-supported inert prime 论证不属于真正的 source excess，不能用于关闭 §14.2-II。

因此第 II 类仍待证，但其剩余问题已被压到**归一化单位的奇阶 cancellation**，而不再是原来的二维 \((\Phi,\Psi)\) 接触。

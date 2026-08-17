# A2 source Hensel and excess audit

> 本文件是按数学依赖整合的规范编辑入口。每个来源笔记只在本文件中保留一次；来源边界、原状态和公式正文均保留，避免日期文件之间形成平行副本。

## 整合顺序

`a2-hensel-resultant-progress.md` → `a2-source-excess-closure.md`

---

## 1. `A_2` source Hensel resultant continuation

> 整合来源：`a2-hensel-resultant-progress.md`。以下正文保留该来源的原始证明状态和审计边界。

> 分支：`agent/a2-hensel-resultant-progress`
> 状态：**部分已严格完成；`A_2` 全局空性仍待证。**
> 依赖：[`core.md` §15](core.md#15-a_2-的-source-双-hensel-系统)。

本文只处理 `A_2` deep-even 终端通道中的 source 双 Hensel 接触。它不把有限诊断提升为全局结论，也不宣称 `A_2` 已关闭。

### 1. 双 Hensel 系统

沿用主分支文件的归一化变量

\[
x=\frac{b_2}{10^{m_2}},\qquad
 y=\frac{a_2}{10^{m_2-1}},\qquad
 z=\frac{5^{E_5}D_0}{c_Q},
\]

以及

\[
\Phi(x,z)=(99x-4)z-2x-4,
\]

\[
\Psi_{a_1}(y,z)=400a_1(z+1)^2-y(99z-2)^2.
\]

对 source inert prime

\[
p\equiv3\pmod4,
\qquad p^{2h}\Vert\sigma,
\]

已有

\[
v_p(\Phi)=2h,
\qquad
v_p(\Psi_{a_1})\ge h.
\]

这里对有理数使用通常的扩张赋值；由于 \(p\ne2,5\)，十进制归一化分母均为 \(p\)-进单位。

---

### 2. `已严格完成`：resultant 完全塌缩

令

\[
A=99x-4,
\qquad
B=2x+4,
\]

则

\[
\Phi=Az-B.
\]

#### 命题 2.1

有精确恒等式

\[
\boxed{
\operatorname{Res}_z(\Phi,\Psi_{a_1})
=163216\,(25a_1x^2-y)
=16\cdot101^2(25a_1x^2-y).
}
\]

#### 证明

\(\Phi\) 关于 \(z\) 为一次式。其根为

\[
r=\frac BA=\frac{2x+4}{99x-4}.
\]

直接计算

\[
r+1
=\frac{B+A}{A}
=\frac{101x}{A},
\]

以及

\[
99r-2
=\frac{99B-2A}{A}
=\frac{404}{A}
=\frac{4\cdot101}{A}.
\]

故

\[
A^2\Psi_{a_1}(y,r)
=400a_1(101x)^2-y\,404^2
=163216(25a_1x^2-y).
\]

因为一次多项式 \(Az-B\) 与二次多项式 \(\Psi\) 的 resultant 等于 \(A^2\Psi(B/A)\)，命题成立。\(\square\)

还存在无需除法的 Bézout 形式

\[
\boxed{
A^2\Psi_{a_1}
-163216(25a_1x^2-y)
=\Phi\,\mathcal Q,
}
\]

其中

\[
\begin{aligned}
\mathcal Q={}&39600a_1xz+80000a_1x-1600a_1z-1600a_1\\
&-970299xyz+19602xy+39204yz-40788y.
\end{aligned}
\]

因此这一消元完全发生在整数系数多项式环中。

---

### 3. `已严格完成`：source `2h:h` 接触降为纯前缀接触

#### 命题 3.1

设 \(p\equiv3\pmod4\) 为 §1 的 source inert prime。则

\[
\boxed{
v_p(25a_1x^2-y)\ge h.}
\]

#### 证明

首先 \(p\nmid A=99x-4\)。否则由 \(p\mid\Phi=Az-B\) 得 \(p\mid B\)，从而

\[
p\mid 99B-2A=404=4\cdot101.
\]

但 \(p\) 是 \(3\bmod4\) 奇素数，而 \(101\equiv1\pmod4\)，矛盾。

又

\[
163216=2^4\cdot101^2
\]

对这样的 \(p\) 也是单位。把 Bézout 恒等式取 \(p\)-进赋值：左侧第一项 \(A^2\Psi\) 至少被 \(p^h\) 整除，右侧的 \(\Phi\mathcal Q\) 至少被 \(p^{2h}\) 整除，因此

\[
p^h\mid 163216(25a_1x^2-y).
\]

常数为 \(p\)-进单位，故结论成立。\(\square\)

这把原来的二维接触

\[
v_p(\Phi)=2h,
\qquad
v_p(\Psi_{a_1})\ge h
\]

严格压缩为一个与 \(z\) 无关的前缀条件。

---

### 4. `已严格完成`：整数前缀接触量

定义

\[
\boxed{
D_{\rm src}=C_0^2-A_0a_2,
}
\]

其中

\[
A_0=a_1 10^{m_2-1},
\qquad
C_0=\frac{a_1b_2}{2}.
\]

直接代入 \(x,y\) 得

\[
\boxed{
D_{\rm src}
=a_1 10^{2m_2-2}(25a_1x^2-y).
}
\]

所以对任意满足 \(p\nmid a_1\) 的 source inert prime，命题 3.1 给出

\[
\boxed{p^h\mid D_{\rm src}.}
\]

此外，一旦 \(p\mid D_{\rm src}\) 且 \(p\nmid a_1\)，有

\[
C_0^2\equiv A_0a_2\pmod p.
\]

于是 prefix defect 与前两块奇范数满足

\[
\Delta_{\rm pref}
=C_0^2-2A_0a_2-a_2^2
\equiv-a_2(A_0+a_2)
=-a_2P\pmod p,
\]

\[
\mathcal N_0=C_0^2+a_2^2
\equiv a_2(A_0+a_2)
=a_2P\pmod p.
\]

故得到新的耦合恒等式

\[
\boxed{
\Delta_{\rm pref}\equiv-\mathcal N_0\pmod p.
}
\]

这个同余把原先相互分开的 source Hensel 接触与 §14.1 的 prefix defect 接到同一个前缀整数上。

---

### 5. `已严格完成`：source 线性式与 \(\Phi\) 的精确比例

由主分支中的固定斜率

\[
U_5C_0=10H_sA_0
\]

以及

\[
\frac{C_0}{A_0}=5x
\]

可得

\[
\boxed{U_5x=2H_s=2D_0c_u.}
\]

再把

\[
z=\frac{5^{E_5}D_0}{c_Q}
\]

代入

\[
2\sigma
=c_uD_0(99\,5^{E_5}D_0-2c_Q)
-2U_5(5^{E_5}D_0+c_Q),
\]

并用 \(D_0c_u=U_5x/2\) 化简，得到

\[
\boxed{
4\sigma=U_5c_Q\Phi(x,z).
}
\]

因此只要 source prime 与 \(U_5c_Q\) 分离，原来的

\[
v_p(\Phi)=2h
\]

就是 \(v_p(\sigma)=2h\) 的精确重写；没有额外的隐藏 Hensel 自由度。

---

### 6. 实数侧：resultant 因子不会趋于零

由 `core.md` §12.9 的 core windows 与 \(y<1\)：

- \(a_1=5\) 时 \(x>27/250\)，所以
  \[
  25a_1x^2-y>125(27/250)^2-1=0.458>0;
  \]
- \(a_1\in\{7,9,11,13\}\) 时 \(x\ge1/10\)，所以
  \[
  25a_1x^2-y>\frac{a_1}{4}-1\ge\frac34>0.
  \]

故统一有

\[
\boxed{25a_1x^2-y>0.458.}
\]

这说明 source resultant 的实根退化完全被排除；若要关闭 source excess，余下任务只可能是证明强制的 \(p^h\) 模数超过这个前缀整数的可用高度，或利用其与 \(\Delta_{\rm pref},\mathcal N_0\) 的新耦合制造局部矛盾。

---

### 7. 当前证明边界

本文件新增的严格结果是：

\[
\boxed{
\text{source }2h:h\text{ 双 Hensel}
\Longrightarrow
p^h\mid(25a_1x^2-y)
}
\]

以及对应的整数前缀量 \(D_{\rm src}\)、prefix-defect 耦合和精确比例式 \(4\sigma=U_5c_Q\Phi\)。

它们**尚未**单独排除 source excess；denominator-prefix excess 与 spontaneous angle excess 也仍需处理。因此 `A_2` 目前不能标记为关闭。

下一步的严格目标已经缩小为：

1. 对 source excess，比较 \(p^h\) 与 \(D_{\rm src}\) 的高度，或证明 \(D_{\rm src}\) 接触与 source/\(\mathcal N_0\) 分离条件不相容；
2. 对 denominator-prefix excess，把 \(\gcd(q_Qf,E_1)=\gcd(q_Qf,\Delta_{\rm pref})\) 与同一前缀量做消元；
3. 对 spontaneous angle excess，寻找不经过 source/denominator 的第二个角度多项式，再做同型 resultant。

---

## 2. `A_2` source-excess audit after resultant collapse

> 整合来源：`a2-source-excess-closure.md`。以下正文保留该来源的原始证明状态和审计边界。

> 分支：`agent/a2-hensel-resultant-progress`
> 状态：**上一版“source inert prime 必落在 `rho`”的归类失效；resultant 与 `L_0` 恒等式保留为严格结论。**
> 依赖：[`core.md` §§12.5, 14–15](core.md)，[`hensel.md`](hensel.md)。

### 1. `失效/降级`：不能把 source excess 认成 `rho`-supported prime

旧记号核对给出

\[
u_0=\frac{u}{5^{\sigma_5}}=c_u\rho.
\]

而 `core.md` §14.2 对真正的 source excess 明确记录了分离条件

\[
p\nmid q_Q f c_Q u_0.
\]

因此 source excess prime 特别满足

\[
\boxed{p\nmid\rho.}
\]

所以“\(p\equiv3\pmod4\) 来自 `u`-side，故 \(p\mid\rho\)”并不是 §14.2 的 source excess；它只是另一种 `u`-supported inert prime 情形。上一版据此宣称“第 II 类 source excess 已关闭”的结论撤回，不得使用。

---

### 2. `已严格完成`：resultant 因子等于 Gaussian 正交误差

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

### 3. 旧 source-excess 赋值结构的正确恢复

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

### 4. 保留的辅助恒等式

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

### 5. 当前结论

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

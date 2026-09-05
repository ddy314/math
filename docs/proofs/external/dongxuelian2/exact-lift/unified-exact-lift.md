# 三项十进制拼接平方和问题：Strict Layer Unified Exact Lift Campaign

**文件名：** `strict_layer_unified_exact_lift_campaign.md`  
**本轮等级：** **SGR-2B — UNIFICATION + NEW COUPLING**  
**范围：** 只统一 SGR-1 的 primitive-core / finite-fibre 框架与既有 Exact-Lift 框架；不单独深攻 \(A_2\)、DD、\(A_1\)，不启动新的 Pell / \(S\)-unit / Vieta jumping 路线。

---

# 0. Executive Summary

本轮得到的统一结论是：

\[
\boxed{
\text{Exact integer sphere + exact recovery}
\Longleftrightarrow
\text{primitive sphere core + coprime scale}.
}

为避免 Exact-Lift 中前两分母拼接 \(Q\) 与 primitive sphere 的第四坐标冲突，全文把 primitive core 写成

\[
\mathcal P=(P_1,P_2,P_3,Q_0),
\]

而把 Exact-Lift 的前两分母拼接写成

\[
Q_{12}=b_1 10^{m_2}+b_2.
\]

两套主变量严格对应为

\[
\boxed{
q=V,\qquad y_i=UP_i,\qquad H=UQ_0.
}
\]

其中

\[
P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1,
\]

\[
\gcd(U,V)=1,
\qquad
g_i=\gcd(V,P_i),
\qquad
a_i=\frac{UP_i}{g_i},
\qquad
b_i=\frac{V}{g_i}.
\]

Exact-Lift 的三个 carrier chamber

\[
A_2\text{-only},\qquad DD,\qquad A_1\text{-only}
\]

不是 primitive core 的三种算术类型，而是由

\[
s_i=n_i-m_i
\]

决定的真实 decimal carrier/profile 状态。完整 SGR state 决定 carrier chamber，但 chamber 不能反向恢复 primitive core、gcd profile、carry bits 或 decimal depth。

两套“二次门”也不是同一个方程：

- SGR 的二次式
  \[
  F_\Sigma(T)=0,\qquad T=10^{\ell(V)}
  \]
  控制 **decimal depth**；
- Exact-Lift 的统一 gap quadratic 控制 \([\mu:\nu]\)；
- Exact-Lift 的 primitive tail quadratic 控制第三尾有理根 \(z_3\)。

它们是对同一 exact candidate 的不同消元投影，因此属于：

\[
\boxed{
\text{compatible but nonredundant gates}.
}

但二者可以进一步严格耦合。固定 primitive core 与完整 SGR state \(\Sigma\) 后，Exact-Lift 判别平方可化成

\[
\mathscr P_\Sigma(T)=Z^2,
\qquad
\deg_T\mathscr P_\Sigma\le6.
\]

将它模 SGR 二次式约化后，可写成

\[
Z_*^2=A_\Sigma T+B_\Sigma.
\]

若 SGR 二次式为

\[
f_2T^2+f_1T+f_0=0
\]

且 \(f_2A_\Sigma\neq0\)，消去 \(T\) 得

\[
\boxed{f_2X^2+
(f_1A_\Sigma-2f_2B_\Sigma)X
+
\bigl(
f_2B_\Sigma^2-f_1A_\Sigma B_\Sigma+f_0A_\Sigma^2
\bigr)
=0,
\quad
X=Z_*^2.}
\tag{UC}
\]

这是一条新的 **primitive-state resultant coupling**。它是“两旧门同时成立”的严格消元后果，不能夸大成比二者联立更强的新定理，但它把原来分散的两个约束压成了一个可直接研究 square-spacing、divisibility 与 moving-core growth 的对象。

SGR-1 的 fixed-core finite-fibre theorem 进一步说明：

\[
\boxed{
\text{固定 primitive core}
\Longrightarrow
\text{只有有限多个 strict decimal lifts}.
}

故任何无穷 strict-layer 候选序列都必须满足

\[
\boxed{
Q_0\to\infty.
}

这对 \(A_2\)、DD、\(A_1\) 同时成立。原来三个 chamber 中看似独立的“长尾逃逸”因此都不能发生在固定 primitive sphere direction 上；整个 strict layer 的真正无界源被统一为 **moving primitive core**。

本轮后的顶层 frontier 可以压成一个独立终端义务：

\[
\boxed{
\textbf{Moving Primitive-Core Uniform Termination}.
}

其内部有两个必须同时满足、但不应误写为两个分别必须关闭的 terminal lemmas 的信息通道：

1. SGR depth + Exact discriminant 的 algebraic/square coupling；
2. Exact tail / gcd / \(2,5\)-adic actual-lift recovery。

因此本轮等级为

\[
\boxed{\textbf{SGR-2B — UNIFICATION + NEW COUPLING}.}
\]

本轮没有证明 strict layer empty，也没有关闭 \(A_2\)、DD、\(A_1\) 中任何一个旧局部分支。

---

# 1. 证据等级与来源审计

全文使用以下等级：

- **PROVED**：本文给出完整证明，或回查到已有严格证明正文；
- **DERIVED FROM PROVED RESULTS**：由已证结论直接推出；
- **COMPUTATIONAL EVIDENCE**：仅计算证据；
- **HEURISTIC**：结构性启发，不作为定理；
- **OPEN OBLIGATION**：仍需证明。

本轮实际使用的 Exact-Lift 关键链包括：

\[
q=\operatorname{lcm}(b_i),
\qquad y_i=\frac{a_iq}{b_i},
\qquad y_1^2+y_2^2+y_3^2=H^2,
\]

\[
\gcd(q,y_i)=\frac q{b_i},
\]

统一 gap quadratic、判别平方、primitive tail quadratic、以及

\[
10^\ell\mid\kappa^2(\kappa+2G).
\]

这些关键等价、整除与恢复步骤均沿既有 Exact-Lift 证明链回查，而不是仅把 synthesis 的摘要陈述当作证明。

primitive normalization 的关键恢复步骤也回查到早期 primitive-sphere 正文与审计后的基础定理：特别是

\[
V=\operatorname{lcm}(b_1,b_2,b_3)
\]

及最小公共分母的 primitive recovery。

### 关于 SGR-1 正文可见性的限制

本轮 File Library 检索没有重新暴露 `strict_layer_global_reduction_campaign.md` 的完整正文。项目当前冻结的 SGR-1 输入为：

\[
\boxed{
\text{fixed primitive core}\Longrightarrow\text{finite decimal fibre},
}

以及每个完整 finite state 上的 exact depth gate

\[
\boxed{
F_{2,\Sigma}T^2+F_{1,\Sigma}T+F_{0,\Sigma}=0,
\qquad
T=10^{\ell(V)}.
}
\]

SGR-1 还给出了 core-height 对 \(\ell(U),\ell(V)\) 的显式线性界；这些常数不参与本轮新 coupling 的证明，因此本文不把它们作为新结果重新证明。

为了避免依赖不可见正文中的代数细节，第 4 节从已经回查到的 primitive-profile master equation 重新推导了 **固定完整 state 上的二次 depth gate**。需要区分：

- “每个固定 state 至多两个 depth roots”由本文重新推导；
- “固定 primitive core 只有有限多个完整 states”继承 SGR-1 的 finite-state theorem。

这一区分避免把 finite-fibre 结论循环地建立在未经证明的“\(r\) 只有有限种”上。

---

# 2. 精确变量字典

## 2.1 SGR primitive normalization

取

\[
\boxed{P_1^2+P_2^2+P_3^2=Q_0^2,
\qquad
\gcd(P_1,P_2,P_3,Q_0)=1.}
\tag{2.1}

令

\[
\boxed{\gcd(U,V)=1,}
\]

\[
\boxed{g_i=\gcd(V,P_i),
\qquad
C_i=\frac{P_i}{g_i}.}
\tag{2.2}

则 strict candidate 的既约块恢复为

\[
\boxed{a_i=UC_i=\frac{UP_i}{g_i},
\qquad
b_i=\frac{V}{g_i}.}
\tag{2.3}

---

## 2.2 SGR \(\Rightarrow\) Exact-Lift

### 定理 2.1 — \(V\) 恰为分母最小公倍数

**PROVED.**

\[
\boxed{\operatorname{lcm}(b_1,b_2,b_3)=V.}
\tag{2.4}

任取素数 \(p\) 且 \(p^e\parallel V\)。若 \(p\mid P_1,P_2,P_3\)，则由球面方程可得 \(p\mid Q_0\)，与 primitive 性矛盾。故至少存在一个 \(j\) 使 \(p\nmid P_j\)，于是 \(v_p(g_j)=0\)，所以 \(v_p(b_j)=e\)。因此 \(V\) 的每个完整素幂都出现在至少一个 \(b_j\) 中，而所有 \(b_i\mid V\)，故 lcm 等于 \(V\)。

Exact-Lift 定义
\[
q=\operatorname{lcm}(b_i),\qquad y_i=\frac{a_iq}{b_i}.
\]
于是
\[
\boxed{q=V,\qquad y_i=UP_i,\qquad H=UQ_0.}
\tag{2.6}

---

## 2.3 Exact-Lift \(\Rightarrow\) SGR

从 Exact-Lift 出发定义
\[
U=\gcd(y_1,y_2,y_3,H),\quad P_i=y_i/U,\quad Q_0=H/U,\quad V=q.
\]
利用 primitive recovery
\[
\gcd(q,y_i)=q/b_i
\]
可证明 \(\gcd(U,V)=1\)，并恢复
\[
g_i=\gcd(V,P_i)=V/b_i,
\qquad b_i=V/g_i,
\qquad a_i=UP_i/g_i.
\]
因此两套 primitive normalization 完全双向一致。

---

# 3. 两套 reduction 的逻辑关系

primitive normalization 可以由 Exact-Lift 直接推出；fixed-core finite fibre 则还必须使用 fixed core 的有限 gcd profiles、carry states、decimal concatenation master equation、depth gate 以及 SGR-1 的 scale-gap finite-state theorem。

三个 carrier chamber 精确翻译为
\[
A_2:\ \delta_3>0,\ \delta_2+\delta_3\le0,
\]
\[
DD:\ \delta_3>0,\ \delta_2+\delta_3>0,
\]
\[
A_1:\ \delta_3\le0,\ \delta_2+\delta_3>0.
\]
完整 SGR state 决定 chamber，反向不成立。正确层级是共同 primitive core 上分出 SGR depth gate 与 Exact block/tail arithmetic 两条非冗余通道。

---

# 4. SGR depth quadratic 的自包含重推

固定 primitive core，令
\[
L_g=\operatorname{lcm}(g_1,g_2,g_3),\qquad h_i=L_g/g_i.
\]
primitive-profile master equation 为
\[
P_1h_1 10^{n_2+n_3}+P_2h_2 10^{n_3}+P_3h_3
=Q_0(h_1 10^{m_2+m_3}+h_2 10^{m_3}+h_3).
\]

记 \(u=\ell(U),v=\ell(V),T=10^v\)，由 multiplication carry bits
\[
n_i=u+\lambda_i-1+\varepsilon_i,
\]
\[
m_i=v-\gamma_i+1-\eta_i,
\]
可把主方程写成
\[
F_{2,\Sigma}T^2+F_{1,\Sigma}T+F_{0,\Sigma}=0,
\]
且
\[
F_{0,\Sigma}=h_3(P_3-Q_0)<0.
\]
清分母后得到整数二次式
\[
f_2T^2+f_1T+f_0=0,
\qquad f_0\ne0.
\]
因此固定完整 state 至多两个 decimal depths。

---

# 5. Exact-Lift 翻译到 primitive-profile 坐标

令
\[
R=V/L_g,
\qquad b_i=Rh_i,
\qquad a_i=UC_i.
\]
定义
\[
\widehat Q=h_1 10^{m_2}+h_2,
\qquad \widehat G=h_1h_2,
\]
\[
\widehat{\mathcal N}=(C_1h_2)^2+(C_2h_1)^2.
\]
则
\[
Q_{12}=R\widehat Q,
\quad G=R^2\widehat G,
\quad \mathcal N_{12}=U^2R^2\widehat{\mathcal N}.
\]
三个 chamber 统一有
\[
C=U\widehat C,
\qquad D=R\widehat D.
\]
同时
\[
\widetilde\kappa=10^{m_3}\widehat Q\widehat G,
\qquad
\kappa=R^2\widetilde\kappa/h_3,
\]
以及
\[
\widehat K=\widehat G^2\widehat C^2-\widehat D^2\widehat{\mathcal N},
\qquad
K_{C,D}=U^2R^4\widehat K.
\]

---

# 6. Exact-Lift 两类二次门与统一判别平方

统一 gap quadratic：
\[
D(\kappa+2G)\mu^2-2G\kappa C\mu\nu+
\kappa D\mathcal N_{12}\nu^2=0.
\]
判别平方：
\[
\kappa(\kappa K_{C,D}-2GD^2\mathcal N_{12})=W^2.
\]
primitive tail quadratic：
\[
-\kappa(\kappa+2G)z_3^2+2G^2LCz_3+\mathcal C_3=0,
\]
并保留统一 tail certificate
\[
10^\ell\mid\kappa^2(\kappa+2G).
\]

---

# 7. Exact discriminant square 化为 \(T\)-多项式平方门

尺度分解给出
\[
Z^2=
\widetilde\kappa(
\widetilde\kappa\widehat K-
2h_3\widehat G\widehat D^2\widehat{\mathcal N}).
\]
固定 state 后，\(\widehat Q,\widehat C,\widehat D\) 对 \(T\) 次数至多 1，\(\widehat K\) 至多 2，\(\widetilde\kappa\) 至多 2，所以
\[
\boxed{\mathscr P_\Sigma(T)=Z^2,
\qquad \deg\mathscr P_\Sigma\le6.}
\]
清分母并乘平方后可取 \(\mathscr P_\Sigma^*\in\mathbb Z[T]\)。

---

# 8. 两套“二次门”的关系

SGR gate 的未知量是 decimal depth \(T\)；Exact gap quadratic 的未知对象是 \([\mu:\nu]\)；Exact tail quadratic 的未知量是 \(z_3\)。三者来自不同消元方向，属于同一候选上的非冗余 gates，不能互相替代。

---

# 9. 新 coupling

把 SGR depth gate 写成
\[
F(T)=f_2T^2+f_1T+f_0=0,
\qquad f_0\ne0,
\]
把 Exact square gate 模 \(F\) 约化成
\[
Z_*^2=AT+B.
\]
令 \(X=Z_*^2\)。若 \(f_2A\ne0\)，消去 \(T\) 得
\[
\boxed{
\Phi_\Sigma(X)=f_2X^2+(f_1A-2f_2B)X+
(f_2B^2-f_1AB+f_0A^2)=0,
}
\]
且 \(X\) 必须是整数完全平方。

退化情形必须保留：若 \(f_2=0\) 则 depth 唯一或 state 为空；若 \(A=0\) 则检查固定 \(B\) 是否为平方；若 \(A=B=0\)，这一层 discriminant elimination 不提供额外状态约束，但 actual tail recovery 仍保留。

resultant 判别式本身为平方不提供新信息；真正有内容的是 \(X\) 自身必须是平方，以及 actual-lift arithmetic recovery。

---

# 10. Actual-lift arithmetic channel

由 tail certificate 与 primitive profile 尺度分解可得，对 \(p\in\{2,5\}\)：
\[
\ell\le
6v_p(R)+2v_p(\widetilde\kappa)+
v_p(\widetilde\kappa+2h_3\widehat G)-3v_p(h_3).
\]
因此 normalized discriminant square 虽可消除 \(U,R\)，actual tail divisibility 仍保留真实 scale 的 \(2,5\)-进信息。

---

# 11. fixed core finite fibre 的影响

继承 SGR-1：固定 primitive core 只有有限 strict decimal lifts。因此任意无限 strict candidate 序列必有
\[
\boxed{Q_0\to\infty.}
\]
这同时作用于 A2、DD、A1：固定 primitive sphere direction 上的“长尾无限逃逸”都不可能发生。真正的 top-level infinity 是 moving primitive core，而不是某一个 tail 参数独立发散。

---

# 12. Unified Strict Exact Lift datum 与 frontier

一个真实 strict candidate 必须同时满足：

1. SGR depth gate \(F_\Sigma(T)=0\)；
2. Exact normalized square gate \(P_\Sigma(T)=Z^2\)，或一般情形下的 \(\Phi_\Sigma(Z_*^2)=0\)；
3. actual-lift arithmetic recovery，包括
   \[
   10^\ell\mid\kappa^2(\kappa+2G),
   \]
   \[
   \nu\mid D(\kappa+2G),\qquad
   \mu\mid\kappa D\mathcal N_{12},
   \]
   primitive recovery gcd、digit windows、positivity、逐项既约和 exact reconstruction。

顶层义务可统一表述为
\[
\boxed{\textbf{Moving Primitive-Core Uniform Termination}.}
\]
即不存在 \(Q_0\to\infty\) 的 primitive cores 与相容 states，使上述三组 gates 同时成立。

---

# 13. 结果分级

## PROVED

- primitive normalization 与 Exact integer sphere + primitive recovery 双向桥；
- \(q=V,y_i=UP_i,H=UQ_0\)；
- 固定 full SGR state 的 quadratic depth gate；
- Exact square gate 的 degree-6 \(T\)-polynomial form；
- resultant coupling 含退化情形；
- tail certificate 的 primitive-profile \(2/5\)-adic capacity form。

## DERIVED FROM PROVED RESULTS

- fixed-core finite fibre 同时作用于 A2/DD/A1；
- infinite strict candidates \(\Rightarrow Q_0\to\infty\)；
- fixed-core long-tail escape 被排除；
- top-level unboundedness 统一为 moving primitive core termination。

## HEURISTIC

near-square、near-S-unit、double-Hensel、square-spacing 可能是 moving-core termination 的不同局部投影。

## OPEN

\[
\boxed{\textbf{Moving Primitive-Core Uniform Termination}.}
\]

---

# 14. 下一轮两个 terminal targets

1. **Moving-Core Resultant Square Obstruction**：研究 \(\Phi_\Sigma(X)=0, X=Z^2, Q_0\to\infty\)，寻找 uniform square-spacing、coefficient gcd、root separation、height inequality 或 resultant divisibility obstruction。
2. **Moving-Core \(2/5\)-Adic Capacity Coupling**：把 tail divisibility 的 valuation capacity 与 depth root \(T=10^{\ell(V)}\) 和 primitive core height \(Q_0\) 联立，尝试同时阻止正确 decimal depth、足够 2/5-adic capacity 与 Exact discriminant square。

---

# 15. 最终裁决

\[
\boxed{\textbf{SGR-2B — UNIFICATION + NEW COUPLING}.}
\]

本轮没有证明 Strict Layer Empty。resultant 的价值是消除重复框架并把两个旧条件组织为一个更适合统一终止研究的 state-level algebraic object；它没有被夸大为比原联立条件逻辑上更强的新定理。

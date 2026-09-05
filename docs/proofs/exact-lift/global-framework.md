# 全局统一框架

本文件给出三块十进制拼接 Exact Lift 的当前规范公共框架。历史长稿仍保存在 `archive/`；这里仅保留经现行分支审计仍有效、且三个异常分支共同使用的结构。主不存在性命题与 A2/DD/A1 三分支状态均由 `status.md` 和各分支 README 决定。

# 3. 整数球面提升与 canonical recovery

对三个正既约有理数

\[
r_i=\frac{a_i}{b_i},\qquad \gcd(a_i,b_i)=1,
\]

令

\[
\boxed{q=\operatorname{lcm}(b_1,b_2,b_3)},
\qquad
\boxed{y_i=\frac{qa_i}{b_i}}.
\]

若 exact lift 成立，则存在正整数 \(H\) 使

\[
\boxed{y_1^2+y_2^2+y_3^2=H^2},
\qquad
\boxed{q\alpha=H\beta},
\]

其中 \(\alpha,\beta\) 为完整 numerator / denominator decimal words。

逐坐标有精确恢复恒等式

\[
\boxed{\gcd(q,y_i)=\frac q{b_i}}.
\]

因此令

\[
d_i=\gcd(q,y_i),
\]

即可唯一恢复

\[
\boxed{a_i=\frac{y_i}{d_i},\qquad b_i=\frac q{d_i}}.
\]

所以完整候选可放在 canonical spine

\[
\boxed{(y_1,y_2,y_3,q)}
\]

上理解。给定该 spine 后，\(H\)、六个 reduced blocks、digit lengths、valuations 与后续 Exact-Lift coefficient data 都是确定性投影。Gap root、tail root、判别平方根符号、Hensel/Gaussian 标签若只是这些数据的消元表示，不能重复计作新的 original-candidate freedom。

注意：\(q=\operatorname{lcm}(b_i)\) 不自动保证 \((y_1,y_2,y_3,H)\) 整体本原；需要 primitive core 时必须显式再除公共 content。

---

# 4. 前两块公共对象与 carrier coefficients

统一定义

\[
\boxed{Q=b_1 10^{m_2}+b_2},
\qquad
\boxed{G=b_1b_2},
\]

\[
\boxed{\mathcal N_{12}=(a_1b_2)^2+(a_2b_1)^2=G^2(r_1^2+r_2^2)}.
\]

三个异常分支使用统一 coefficient pair \((C,D)\)：

\[
(C,D)=
\begin{cases}
\left(a_1 10^{m_2}+10a_2,\ Q\right),&A_2,\\[0.4em]
\left(10^{m_2+k_{12}}a_1+10^{d_3}a_2,\ Q\right),&DD,\\[0.4em]
\left(10^{g+k_{12}+m_2}a_1+a_2,\ 10^gQ\right),&A_1.
\end{cases}
\]

DD 中

\[
d_3=s_3>0,\qquad k_{12}=s_2+s_3>0,
\]

A1 中

\[
g=-s_3\ge0,\qquad k_{12}=s_2+s_3\ge1.
\]

这些定义只是把三个 carrier chamber 的 decimal coefficient plane 写入同一语言，不改变分支状态。

---

# 5. 第三尾正规化与 denominator–decimal trace

定义有效尾长

\[
\ell=
\begin{cases}
m_3,&A_2,DD,\\m_3-g,&A_1,
\end{cases}
\]

以及

\[
\boxed{\delta_3=\gcd(10^\ell,b_3)},
\qquad
\boxed{L=\frac{10^\ell}{\delta_3}},
\qquad
\boxed{\tau=\frac{b_3}{\delta_3}},
\]

故

\[
\gcd(L,\tau)=1.
\]

第三分子的相应 tail normalization 只在其定义域内使用；不能从 \(\delta_3\) 的 denominator gcd 无条件推出 \(\delta_3\mid a_3\)。涉及 primitive tail numerator 的公式必须引用对应分支已经建立的 exact-recovery 定义。

Denominator recovery 与 decimal completion 真正需要共享的 denominator-side trace 可以写成

\[
\boxed{T_{\rm blk}=(b_1,b_2,b_3,10^\ell)},
\]

或等价的 segmented word 形式

\[
\boxed{T_{\rm word}=(\beta,10^{m_2},10^{m_3},10^\ell)}.
\]

给定该 trace，\(q,Q,G,\delta_3,L,\tau\) 以及全部 denominator-only valuation/gcd data 都是确定性函数。这个接口只减少重复状态，不关闭任何分支。

A1 的 historical saturated `L=1` 子支已经在 A1 后续工作中排除；它不再是当前 A1 frontier。当前 A1 权威前沿见 `branches/a1-only/README.md`。

---

# 6. 三分支统一尾权 \(\kappa\)

三个分支的尾权可以统一写成同一个 branch-free 恒等式：

\[
\boxed{\kappa=\frac{10^{m_3}QG}{b_3}\in\mathbf Z_{>0}}.
\]

证明只是把各分支原定义代回：

- A2/DD 有 \(\ell=m_3\)，故 \(L/\tau=10^{m_3}/b_3\)；
- A1 有 \(\ell=m_3-g\)，故 \(10^gL/\tau=10^{m_3}/b_3\)。

因此旧的两种写法

\[
\kappa=\frac{LQG}{\tau}\quad(A_2,DD),
\qquad
\kappa=\frac{10^gLQG}{\tau}\quad(A_1)
\]

只是同一恒等式的 chamber-specific 展开。

公共窗口仍为

\[
\boxed{QG<\kappa\le10QG}.
\]

这个统一式是本次外部整合后正式采纳的公共简化；它不依赖任何 DD closure 假设。

---

# 7. Gap quadratic 与判别平方

令统一 gap 参数满足

\[
G(\mathcal R-r_3)=\frac\mu\nu,
\qquad \gcd(\mu,\nu)=1.
\]

三个异常分支都得到

\[
\boxed{
D(\kappa+2G)\mu^2
-2G\kappa C\mu\nu
+\kappa D\mathcal N_{12}\nu^2=0.
}
\]

于是必要整除为

\[
\boxed{\nu\mid D(\kappa+2G)},
\qquad
\boxed{\mu\mid\kappa D\mathcal N_{12}}.
\]

定义

\[
\boxed{K_{C,D}=G^2C^2-D^2\mathcal N_{12}}.
\]

存在有理 gap root 的必要条件是

\[
\boxed{
\kappa\bigl(\kappa K_{C,D}-2GD^2\mathcal N_{12}\bigr)=W^2
}
\]

对某个整数 \(W\)。

这类 quadratic / discriminant 条件是 exact candidate 的投影证书。若在某个更完整的 recovery chart 中它们由同一 exact reconstruction 自动推出，就不能作为额外独立 obstruction 再次收费；具体独立性由对应分支 dependency audit 决定。

定义

\[
G_0=\gcd(\mathcal N_{12}\nu^2-\mu^2,2G\mu\nu).
\]

已有公共结果

\[
\boxed{G_0\mid2G\mathcal N_{12}},
\]

所以 recovery 中出现的额外 gcd 不能充当完全独立的无界素数储存池。

---

# 8. Tail quadratic 与 denominator-tail certificate

在各分支已经建立相应 primitive-tail recovery 的定义域内，可得到统一 tail quadratic 与有理根整除。其最稳定、跨分支可直接使用的 denominator-side 结论是

\[
\boxed{10^\ell\mid\kappa^2(\kappa+2G)}.
\]

由于第 6 节的 branch-free \(\kappa\) 公式，这个 certificate 的 denominator side 完全由

\[
(b_1,b_2,b_3,10^\ell)
\]

决定。

令

\[
S_{12}=m_1+m_2.
\]

由

\[
Q,G<10^{S_{12}}
\]

以及 \(QG<\kappa\le10QG\)，得到公共粗尾长锥

\[
\boxed{\ell\le6S_{12}+3}.
\]

于是 A2/DD 有

\[
\boxed{m_3\le6S_{12}+3},
\]

A1 有

\[
\boxed{m_3-g\le6S_{12}+3}.
\]

这些只是 prefix-uniform 高度约束，不是全局空性。

---

# 9. Vieta / prime-flow 工具的使用边界

Gap/tail quadratic 常可产生 Vieta conjugate、cross-difference、prime-power allocation 或 quadratic-residue 条件。这些工具在局部算术上有效，但必须区分：

1. 共轭根是否仍对应正的 original decimal block；
2. 变换后是否保持逐块既约；
3. 是否保持同一 decimal coefficient plane / carrier chamber；
4. prime-flow 条件是否只是原 quadratic 的等价投影。

本仓库早期曾多次把“有 companion root / Gaussian flip 改变尺度”误当成合法 descent。现行审计已经确认：没有证明上述保持性时，Vieta/Gaussian 变换只能作为局部 factorization 工具，不能迭代成全局下降。

A1 的外部 word-recovery 审计还提供了一个重要反例原则：即使 sphere、tail、Gaussian、reducedness 的多个投影同时成立，只要没有强制 **同一个真实 first-two decimal cut**，仍可留下无穷 ambient pseudo-family。因此后续 prime-flow 结论必须回接真实 word realization。

---

# 10. Denominator prime graph

对任意素数 \(p\)，记

\[
e_i=v_p(b_i),\qquad E=\max(e_1,e_2,e_3).
\]

逐坐标 recovery

\[
v_p(\gcd(q,y_i))=E-e_i
\]

把 denominator exponent pattern 精确送入整数球面。

对于奇素数 \(p\ne2,5\)，若最大赋值只在一块出现，则 complementary denominator relation 强迫另外两块的 \(p\)-进指数相等；pair-max 情形结合二平方和局部条件，会对 \(p\bmod4\) 产生严格限制。所有更细的 unique-max / pair-max 结论必须引用相应分支的已审计 lemma，不能从这张 skeleton 自动外推全局关闭。

对 \(p=2\)，整数球面与 primitive recovery 给出强 parity/exponent pattern；现行分支文档中的 2-adic locks 是对该 skeleton 的进一步专门化。

因此 denominator prime graph 的作用是组织 prime supply 与 recovery depth，不是单独的 contradiction theorem。

---

# 11. Gaussian 整数结构与当前边界

整数球面有

\[
y_1^2+y_2^2=(H-y_3)(H+y_3),
\]

同时在 \(\mathbf Z[i]\) 中

\[
y_1^2+y_2^2=(y_1+iy_2)(y_1-iy_2).
\]

这给出 Gaussian factor matching、split/inert prime allocation、norm squareclass 与局部容量约束。三个分支的大量严格中间结果都建立在这一接口上。

必须保留的全局边界是：

\[
\boxed{\text{Gaussian flip 一般不保持原 decimal coefficient plane。}}
\]

所以 Gaussian normalization 可以用于局部因子归约、source orientation、prime allocation 和 certificate；除非额外证明变换后的点仍满足 original exact-lift word equations、digit cells 与 reducedness，否则不能称为合法 descent。

当前完整证明仍必须回到三条权威分支：A2、DD、A1。任何外部或历史报告中的 `CLOSED` 标签都需要先通过当前 `status.md` 与分支 README 的 coverage 审计。

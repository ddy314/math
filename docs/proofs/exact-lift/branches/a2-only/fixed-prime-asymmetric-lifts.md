# A2 fixed-prime asymmetric lift continuation

> **依赖：** [`primitive-reduction.md`](primitive-reduction.md) §§5–10；[`auxiliary-reductions-ledger.md`](auxiliary-reductions-ledger.md) 中整合来源 `fixed-denominator-height-angle.md`；[`source-angle-ledger.md`](source-angle-ledger.md) 中整合来源 `spontaneous-denominator-depth-matrix.md`。
>
> **严格状态：**本文接续历史账本已经得到的 fixed `7,23,43` shallow pool。本文新增的是：当 saturated denominator 与 angle/common 两个方向都继续到第二层时，五个 genuine first-layer template 的所有合法 continuation 都被压成两条唯一的 asymmetric Hensel 轨道；其中没有继续加深的 height/additive 对象恰好只有一层。本文仍**不宣称 A2 全局关闭**。

---

## 1. 先对齐历史来源：`7,23,43` 与五个 first-layer template 已经存在于账本

`primitive-reduction.md` §10 从当前 canonical 链独立恢复了

\[
q\text{-height}:p=23,
\qquad
f\text{-height}:p\in\{7,43\},
\]

以及

\[
\min\left\{
 v_p(\text{denominator}),
 v_p(W_q),
 v_p(\widehat{\mathcal T}_2)
\right\}=1.
\tag{1.1}
\]

这一固定素数结论与机械归并进 `auxiliary-reductions-ledger.md` 的历史来源
`fixed-denominator-height-angle.md` 一致。后者还已经加入 angle/common 条件并完成 first-layer 枚举；因此本文不把下面五个模板重新计作新结论：

\[
\boxed{
\begin{array}{c|c|c}
p&\text{genuine first-layer state}&M\text{ class}\\ \hline
23&(x,y,\tau)=(-2,18,6)&16\pmod{22}\\
23&(x,y,\tau)=(-2,10,17)&5\pmod{22}\\
7&(x,y,\tau)=(4,6,1)&0\pmod6\\
43&(x,y,\tau)=(5,37,15)&10\pmod{21}\\
43&(x,y,\tau)=(18,33,38)&8\pmod{21}
\end{array}}
\tag{1.2}
\]

这里

\[
\tau:=10^{-M}\pmod{p^k}
\]

是 decimal length unit；它与下文的 valuation depth 无关。

历史账本已经证明五个模板均 Jacobian nonsingular，而且 first-layer decimal-compatible。真正剩余的问题是 (1.1) 之后的**非对称高阶分配**。

---

## 2. denominator/additive depth 的最终规范对象

`spontaneous-denominator-depth-matrix.md` 已把完整 saturation 内的 additive depth 压成两个 pure-prefix quadratic。

q-side：

\[
\boxed{P_q(K):=K^2-26,}
\tag{2.1q}
\]

并且若 \(p^e\Vert q\)、\(p^e\mid\mathscr L_{23}\)，则

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),e\}
=
\min\{v_p(P_q(K)),e\}.}
\tag{2.2q}
\]

f-side：

\[
\boxed{P_f(K):=3K^2-36K+26,}
\tag{2.1f}
\]

并且若 \(p^e\Vert f\)、\(p^e\mid\mathscr L_{23}\)，则

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),e\}
=
\min\{v_p(P_f(K)),e\}.}
\tag{2.2f}
\]

angle/common depth 在 q/f 两侧都由同一个 prefix defect读取：

\[
\boxed{
\Delta_0:=2025x^2-18y-y^2.}
\tag{2.3}
\]

因此 fixed-prime continuation 不再需要 source ratio、curvature character 或第三块 Gaussian Hensel root；只需研究

\[
\boxed{
\text{denominator depth},\quad
v_p(\Delta_0),\quad
v_p(W_q),\quad
v_p(P_q/P_f).}
\tag{2.4}
\]

---

# 第一部分：q-side fixed `23`

## 3. q-side 的三个局部方程

在 q-line 上 `x=-2`。令

\[
s:=y+9.
\]

固定 `23` 的 three-way first-layer center 可由三个整数多项式读取：

\[
D_q:=8100-18y-y^2,
\tag{3.1}
\]

\[
H_q:=2(y+9)-9\tau,
\tag{3.2}
\]

\[
A_q:=(y+9)^2-26\tau^2.
\tag{3.3}
\]

其中：

- `D_q=0` 是 angle/common；
- `H_q=0` 是 height+saturation center `2K-9=0` 乘上 decimal unit；
- `A_q=0` 是 additive root `P_q(K)=0` 乘上 `tau^2`。

历史 first-layer 模板正是

\[
(y,\tau)=(18,6),(10,17)\pmod{23}.
\tag{3.4}
\]

由 (1.1)，若 denominator 已进入第二层，就不能同时让 `H_q,A_q` 都进入第二层。于是只存在两个合法方向：

\[
(D_q,H_q)\text{ deep},\quad A_q\text{ shallow},
\]

或

\[
(D_q,A_q)\text{ deep},\quad H_q\text{ shallow}.
\]

---

## 4. `已严格完成`：两个 `23` 模板各有恰两条 asymmetric `23^2` continuation

对两个 first-layer 点分别计算上述两个 `2x2` Jacobian。四个 determinant 为

\[
3,12,20,12\pmod{23},
\tag{4.1}
\]

全部为单位。因此每个方向都有唯一 Hensel lift 到 `23^2`，并继续唯一提升到所有更高层。

精确的第二层结果为：

\[
\boxed{
\begin{array}{c|c|c|c|c}
(y,\tau)\bmod23&\text{deep pair}&(y,\tau)\bmod529
&\text{shallow}/23\bmod23&M\bmod506\\ \hline
(18,6)&D_q,H_q&(156,213)&A_q/23=14&236\\
(18,6)&D_q,A_q&(156,75)&H_q/23=8&302\\
(10,17)&D_q,H_q&(355,316)&A_q/23=14&489\\
(10,17)&D_q,A_q&(355,454)&H_q/23=15&49
\end{array}}
\tag{4.2}
\]

四个 shallow normalized residues 都非零。因此：

\[
\boxed{
\begin{array}{ll}
D_q,H_q\text{ 深到第二层}
&\Longrightarrow v_{23}(P_q(K))=1,\\[1mm]
D_q,P_q(K)\text{ 深到第二层}
&\Longrightarrow v_{23}(W_q)=1.
\end{array}}
\tag{4.3}
\]

这不只是在 `23^2` 上的一次偶然失败。因为深系统的 Jacobian 是 `23`-进单位，后续沿其唯一 Hensel branch 移动时，已经非零的 shallow quotient 模 `23` 保持不变；所以 shallow 对象在整条 branch 上都**精确只有一层**。

---

# 第二部分：f-side fixed `7,43`

## 5. f-side 的四个局部方程

令

\[
s:=y+9.
\]

使用历史 f-common 三方程的整数版本：

\[
D_f:=2025x^2-18y-y^2,
\tag{5.1}
\]

\[
L_f:=200x^2(s-9\tau)-y(x+2)^2,
\tag{5.2}
\]

并加入

\[
H_f:=2s-9\tau,
\tag{5.3}
\]

\[
A_f:=3s^2-36s\tau+26\tau^2.
\tag{5.4}
\]

这里：

- `D_f,L_f` 是 angle/common + saturated denominator sphere；
- `H_f` 读取 height center；
- `A_f=tau^2 P_f(K)` 读取 additive depth。

历史 genuine first-layer states 为

\[
(4,6,1)\pmod7,
\tag{5.5a}
\]

\[
(5,37,15),(18,33,38)\pmod{43}.
\tag{5.5b}
\]

若 denominator 与 angle/common 都继续到第二层，则合法的两个非对称系统只能是

\[
(D_f,L_f,H_f)\text{ deep},\quad A_f\text{ shallow},
\tag{5.6H}
\]

或

\[
(D_f,L_f,A_f)\text{ deep},\quad H_f\text{ shallow}.
\tag{5.6A}
\]

---

## 6. `已严格完成`：`p=7` 的两条唯一 asymmetric continuation

在 first-layer 点 `(4,6,1)` 上，两个 `3x3` Jacobian determinant 分别为

\[
4,3\pmod7,
\tag{6.1}
\]

均为单位。唯一第二层 lifts 为

\[
\boxed{
\begin{array}{c|c|c|c}
\text{deep system}&(x,y,\tau)\bmod49
&\text{shallow}/7\bmod7&M\bmod42\\ \hline
D_f,L_f,H_f&(39,48,29)&A_f/7=5&18\\
D_f,L_f,A_f&(25,34,22)&H_f/7=5&24
\end{array}}
\tag{6.2}
\]

所以 denominator+angle 已深时：

\[
\boxed{
\text{height deep}\Longrightarrow\text{additive exact depth }1,
}
\tag{6.3H}
\]

\[
\boxed{
\text{additive deep}\Longrightarrow\text{height exact depth }1.
}
\tag{6.3A}
\]

---

## 7. `已严格完成`：`p=43` 的四条唯一 asymmetric continuation

对两个 first-layer templates，height-deep / additive-deep Jacobian determinants 分别为

\[
(4,31),\qquad(3,3)\pmod{43},
\tag{7.1}
\]

全部为单位。四条唯一第二层轨道为

\[
\boxed{
\begin{array}{c|c|c|c|c}
(x,y,\tau)\bmod43&\text{deep system}&(x,y,\tau)\bmod1849
&\text{shallow}/43\bmod43&M\bmod903\\ \hline
(5,37,15)&D_f,L_f,H_f&(1252,424,918)&A_f/43=4&640\\
(5,37,15)&D_f,L_f,A_f&(1295,1327,359)&H_f/43=30&787\\
(18,33,38)&D_f,L_f,H_f&(1738,1065,855)&A_f/43=10&575\\
(18,33,38)&D_f,L_f,A_f&(1007,76,683)&H_f/43=33&92
\end{array}}
\tag{7.2}
\]

四个 shallow normalized residues 全部为单位。因此与 `p=7` 一样，选定哪一个对象继续加深以后，另一个对象会沿整条唯一 Hensel branch 永久停在精确第一层。

---

# 第三部分：decimal orbit 审计

## 8. `已严格完成 / 降级`：更高 `p^k` 的纯 decimal membership 不会关闭这些 branch

第二层的 decimal orders 为

\[
\operatorname{ord}_{49}(10)=42,
\qquad
\operatorname{ord}_{529}(10)=506,
\qquad
\operatorname{ord}_{1849}(10)=903.
\tag{8.1}
\]

并且有精确一阶主单位：

\[
10^6\equiv1+7\pmod{49},
\tag{8.2a}
\]

\[
10^{22}\equiv1+8\cdot23\pmod{529},
\tag{8.2b}
\]

\[
10^{21}\equiv1+12\cdot43\pmod{1849}.
\tag{8.2c}
\]

三个系数 `1,8,12` 分别是模 `7,23,43` 的单位。因此 LTE / 主单位群给出

\[
\boxed{
\operatorname{ord}_{7^k}(10)=6\cdot7^{k-1},
}
\tag{8.3a}
\]

\[
\boxed{
\operatorname{ord}_{23^k}(10)=22\cdot23^{k-1},
}
\tag{8.3b}
\]

\[
\boxed{
\operatorname{ord}_{43^k}(10)=21\cdot43^{k-1}.
}
\tag{8.3c}
\]

对 `7,23`，`10` 生成全部单位群；对 `43`，它在 Teichmuller 部分保持 index `2`，但 `10^{21}` 已生成完整 principal-unit direction。由于两个 first-layer `43` templates 的 `tau=15,38` 本来就在 `<10>` 中，所以一旦进入其唯一 Hensel branch，继续提高 `43^k` 只会唯一细化指数 `M`，不会产生新的 subgroup obstruction。

因此：

\[
\boxed{
\text{继续机械检查 }\tau\in\langle10\rangle\pmod{p^k}
\text{ 不会排除上述 asymmetric branches}.}
\tag{8.4}
\]

这是一个重要 no-go：后续必须加入与 decimal length 独立的第二个全局条件。

---

## 9. `已严格完成`：fixed denominator-height-angle pool 的完整二阶状态图

结合历史 first-layer 枚举、共同深度定理与 §§4–8，可把 fixed `7,23,43` pool 在第二层后的状态写成：

\[
\boxed{
\begin{array}{c}
\text{first-layer fixed template}\\
\Downarrow\\
\text{若 denominator depth}=1\text{ 或 angle depth}=1:\text{ 离开 common-deep sector};\\[1mm]
\text{否则 denominator,angle 均}\ge2\\
\Downarrow\\
\begin{cases}
\text{唯一 height-deep Hensel branch，additive depth}=1,\\
\text{唯一 additive-deep Hensel branch，height depth}=1.
\end{cases}
\end{array}}
\tag{9.1}
\]

特别地，在 `denominator>=2` 且 `angle>=2` 的 sector 中，已经**没有**：

- 三对象共同的二阶节点；
- 多分叉的 Hensel tree；
- 新的 singular prime；
- 更高 decimal subgroup gate。

只剩两条一维、唯一的 asymmetric `p`-进轨道。

因此 fixed-prime 部分真正尚未处理的自由度被压到两类：

1. `denominator depth = 1` 或 `angle/common depth = 1` 后，prime 从 fixed common sector 退出并进入 global parity ledger；
2. 在两条 unique asymmetric deep branch 上，需要一个**独立于 decimal membership 的全局量**来决定这份固定浅层 correction 是否能与其他 odd-inert carriers 配对。

这比“分别继续追 `7,23,43` 的任意 Hensel 深度”更精确，也避免重复研究已经被 simple Jacobian 和主单位群完全刚性化的局部树。

---

## 10. 验证

```bash
uv run python scripts/exact-lift/a2-only/check_a2_fixed_prime_asymmetric_lifts.py
```

脚本逐项核对：

- 五个历史 first-layer templates 的 reduction；
- 两套 deep-system Jacobian 的非奇异性；
- 十条 asymmetric `p^2` lifts；
- complementary shallow residual 的 exact depth `1`；
- 第二层 decimal exponent classes；
- `7,23,43` 的 principal-unit order growth。

这些核对只验证本文列出的代数与局部 Hensel 结论；A2 的无界 deep-even 核仍未全局关闭。

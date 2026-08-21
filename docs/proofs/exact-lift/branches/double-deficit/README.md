# `double-deficit`（DD）分支

这是 DD 的**当前权威状态入口**。2026-08-22 的 discriminant-root audit 发现：若把 unified integer discriminant root 与 §18 的 reduced root `L Xi` 直接认同，会漏掉一个真实 normalization factor。由此产生的一批旧 5-adic high-funnel 状态标签必须降级。

历史账本继续保留原推导与原状态文字，作为依赖审计记录；**若账本中的状态与本 README 或 2026-08-22 correction notes 冲突，以本 README / correction notes 为准。**

## 1. 当前安全主结论

DD 尚未证明为空，也没有 effective absolute height bound。

当前安全的全局渐近结论仍为

\[
\boxed{
\limsup_{\rm DD}\frac{n_3}{S_{12}}
\le 6.308883577618\ldots
}
\]

该阈值使用 Schmidt Subspace Theorem，因此非有效。

2026-08-22 已对 corrected canonical `t_2=1` double-resonant high funnel 独立重证同一个常数：令

\[
a=\log_{10}2,
\]

则

\[
\boxed{
\limsup\frac nS
\le
\frac{8+7a}{1+2a}
=6.308883577618031\ldots
}
\]

而 equality closure 强迫

\[
Q_5,G_5,N_5,R\to0,
\qquad
\frac mS\to2.808883577618\ldots,
\qquad
\frac dS\to\frac72.
\]

因此旧 `6.308883...` terminal geometry 仍是真正的 extremal geometry；目前没有正确证明把 `<=` 升级为严格 `<`。

主修正文：

- [`dd-discriminant-root-dependency-audit-2026-08-22.md`](dd-discriminant-root-dependency-audit-2026-08-22.md)：错误 normalization 的依赖审计与撤销表。
- [`dd-corrected-high-funnel-schmidt-2026-08-22.md`](dd-corrected-high-funnel-schmidt-2026-08-22.md)：corrected high-funnel 的独立 Schmidt + exact-small-factor 证明，恢复 `6.308883...`。
- [`dd-z0-charged-first-2026-08-21.md`](dd-z0-charged-first-2026-08-21.md)：post-tail `X_Q` 的 charged-first local allocation；其使用范围必须按 discriminant-root audit 后的依赖重新读取。

## 2. 2026-08-22 后明确撤销 / 降级的旧结论

以下旧结论**不得再作为覆盖整个 canonical funnel 的 theorem 引用**：

1. `frontier-five-adic-closure` 对 equality frontier 的旧 valuation-mismatch closure；所以旧
   \[
   \limsup n/S<6.308883577618\ldots
   \]
   当前撤销，退回 `<=`。

2. `high-funnel-five-adic-dichotomy` 的 exhaustive
   \[
   \text{Defect-heavy}\cup\text{Tail-short}
   \]
   branch partition。旧 proof 的 valuation mismatch 来自错误的 discriminant-root normalization。

3. 旧
   \[
   3v_5(\Xi)=5q_5+4g_5+n_5-m
   \]
   (`Xi-slack`)。

4. 从上述链推出的 generic `denominator-max-lock`：
   \[
   b_3\text{ 非 5-adic maximum}\Longrightarrow n<6S+O(1),
   \]
   以及把所有 remaining states 强制到
   \[
   B_5=q_5+2g_5,
   \qquad
   m=2q_5+4g_5+n_5.
   \]

5. 因此历史文件 `high-funnel-tail-short-schmidt-upgrade.md` 中“各旧 sheets 穷尽 canonical funnel，从而 whole sector `<=6`”的合并结论也降级。其 LP 在**额外 Tail-short 条件成立时**仍可作为条件计算读取，但 Tail-short 已不再由正确的 5-adic dichotomy 自动覆盖 complementary states。

6. `Final-5` 仍可作为额外条件 sheet 使用；不得再把它描述为 remaining high funnel 的必然终态。

## 3. corrected 5-adic local ledger

在 corrected discriminant normalization 下，令

\[
E_5:=\max_i v_5(b_i),
\qquad
B_5:=v_5(b_3),
\qquad
q_5:=v_5(Q).
\]

在相应 `B_5<m` high-funnel discriminant-separation region，正确的 `Xi` depth 为

\[
\boxed{
v_5(\Xi)=q_5+E_5-B_5.
}
\]

若 `b_3` 恰为 5-adic maximum，则

\[
\boxed{v_5(\Xi)=q_5.}
\]

结合

\[
\Xi=|\mathcal M-C_0a|,
\qquad
C_0=QL+2\tau,
\]

及 decimal depth，可在对应作用域内得到

\[
\boxed{
v_5(a)=q_5+E_5-B_5.
}
\]

所以

\[
\boxed{
v_5(H-y_3)=T+(E_5-B_5).
}
\]

另一方面 overlap-normalized factor

\[
\widehat g=\gamma/c_3
\]

满足

\[
v_5(\widehat g)=g_5-(E_5-B_5).
\]

两者精确抵消 denominator-max deficit：

\[
\boxed{
v_5\bigl((H-y_3)\widehat g\bigr)=T+g_5.
}
\]

这是 corrected high-funnel small-factor lower bound 的核心接口。

## 4. corrected canonical high-funnel Schmidt proof

canonical `t_2=1` phase 保留 exact identities

\[
\kappa=2\gamma5^TU,
\qquad
\kappa+2G=2\gamma2^HZ,
\qquad
2^HZ-5^TU=V.
\]

fixed-target Schmidt 仍给

\[
\log U+\log Z\ge S-o(S).
\]

结合 decimal pinning 与 2/5 resonance，可独立恢复安全 budget

\[
\boxed{
\frac{2(1+2a)}3M
+2aQ_2+aN_2
+\frac{1-a}{3}(2Q_5+4G_5+N_5)
+2R
\le3.
}
\]

同时 exact

\[
F_-=2^{H+1}Z(H-y_3)\widehat g
\]

与上一节的 corrected 5-adic cancellation 给新的 whole-funnel small-factor inequality。两式具有一个直接 dual certificate，得到

\[
\boxed{
\limsup\frac nS
\le
\frac{8+7\log_{10}2}{1+2\log_{10}2}.
}
\]

因此以后研究 strict gap 时，不再使用旧 `Five-dichotomy / Xi-slack / Final-5 exhaustion`；直接以这套 corrected inequalities 为 baseline。

## 5. 当前 strict-gap terminal frontier

若存在 sequence 逼近

\[
\frac nS\to6.308883577618\ldots,
\]

corrected dual equality 强迫所有 5-adic/rough defects饱和到旧 terminal ray。真正剩余的正线性 entropy 仍是 odd split-prime moving core

\[
V=C_Lv_0,
\qquad
\log C_L=S+o(S),
\qquad
\log v_0=o(S).
\]

因此 [`frontier.md`](frontier.md) 中与 odd moving core、rational contact、Gaussian orientation、Bad/Good、Lorentz cofactor system 有关的**条件恒等式与 no-double-pay audit**继续作为 strict-gap 工具使用；但其中凡声称 equality frontier 已由旧 5-adic mismatch 排除的文字均视为历史状态，已被本 README supersede。

当前 terminal branch 图：

### A. full rational-contact

\[
D_+D_-=C_L^{1-o(1)}.
\]

已有 critical cofactor Lorentz system `(CF1)`--`(CF5)`，以及 Bad/Good 分解。

Bad branch 当前首选对象是 oriented quotient-level elimination；不得先取 norm 丢掉 Gaussian orientation。

### B. genuine-Gaussian

\[
C_G=10^{\varepsilon S+o(S)}
\]

对某个 `epsilon>0`。这一支仍需新的 same-prime Gaussian/projective elimination。

### C. Good rational-contact

至少半个 `C_L` 高度在 full rational contact 后不重复进入 chosen Gaussian quotient。需要追踪 transverse rough core，而不能继续使用 first-order rational GCD/Ridout，因为 leading-order height 已精确临界。

## 6. post-tail / non-canonical dominant line

细粒度研究仍保存在：

- [`tail-allocation-ledger.md`](tail-allocation-ledger.md)
- [`high-funnel-ledger.md`](high-funnel-ledger.md)
- [`good-genuine-ledger.md`](good-genuine-ledger.md)

注意：这些是**历史研究账本**，内部来源块保留当时状态，不能仅凭局部标题中的 `已严格完成` 判定当前可引用性。涉及 unified discriminant root、`W=LXi`、5-adic mismatch、Five-dichotomy、Xi-slack、denominator-max exhaustion 的任何结论，必须先经过 [`dd-discriminant-root-dependency-audit-2026-08-22.md`](dd-discriminant-root-dependency-audit-2026-08-22.md)。

post-tail charged-first 仍提供一个独立的 denominator-source factor-allocation视角，但在继续向 global slope 喂回之前，需要逐项确认它所调用的 local transfer 没有通过旧 discriminant-root identity 间接依赖失效链。

## 7. 已判死 / 不应重开的路线

在 terminal frontier 中，下列方向已有 no-double-pay / hidden-square audit，不应重复投入：

- standalone tangent / blow-up；
- cross-resultant 与 near-axis norm 直接 gcd；
- U/Z side same-prime norm resultants；
- Bad 直接桥接 bottom determinant；
- `t_p+b_p<=h_p`；
- 单靠 `C_0` 与 digital norm gcd；
- 模 `A_0` 的 small-gcd argument；
- generic first-order GCD / Subspace / Ridout closure；
- first-order hyperbolic `2x2` determinant mining。

这些方向要么精确退回 hidden square / existing norm，要么 leading-order height 恰好临界。

## 8. 当前优先任务

1. 完成 Bad branch 中 quotient-level oriented elimination，并核验它是否只是已有 `U1-transfer` 的 Lorentz-coordinate 改写。
2. 若等价，正式把 `Bad-CF + Nc-elim` 作为独立 closure 路线降级，立即转 genuine-Gaussian branch。
3. 若不等价，保留 chosen orientation，尝试得到第三个真正有正线性 surplus 的 proximity。
4. 随后处理 Good rational-contact 的 transverse rough core。
5. 再把 strict-gap terminal 结论反馈给 post-tail / non-canonical global branch partition。

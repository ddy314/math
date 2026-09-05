# 2026-09-06 外部成果整合审计

审计对象：`dongxuelian2/three-term-decimal-concatenation-square-sum`，来源 `master` 提交 `2cfa389f1d4ced90653101e6c92ee8dfe85b5535`。

本文件按本仓库 `AGENTS.md` / `CONTRIBUTING.md` 的证明标准裁决外部成果。原则是：保留可复用的严格局部结论和负面知识；有限计算不外推；旧 coverage 不自动继承；原作者的状态标签不具有本仓库的权威性。

## 1. 总体裁决

来源仓库本身仍明确记录“global problem open”。其基础 T1–T18、critical-G 若干子定理、Exact-Lift recovery 接口和 A1 backward 结构有较高复用价值；来源后期的 `SGR-9A — DD CLOSED` 则依赖一条与本仓库现行 DD 前沿不一致的冻结覆盖链，不能升级本仓库 DD 状态。

因此当前权威状态保持：

\[
\boxed{A_2\text{ 待证},\qquad DD\text{ 待证},\qquad A_1\text{ 待证}.}
\]

## 2. 采纳：common-denominator canonicalization

来源 T1/T3 与本仓库 `global-framework.md` 的 `q,y_i,H` 语言一致。令

\[
q=\operatorname{lcm}(b_1,b_2,b_3),\qquad y_i=qa_i/b_i.
\]

已有

\[
y_1^2+y_2^2+y_3^2=H^2,
\qquad
\gcd(q,y_i)=q/b_i.
\]

所以完整 reduced blocks 可由 canonical spine

\[
\boxed{(y_1,y_2,y_3,q)}
\]

唯一恢复：

\[
d_i=\gcd(y_i,q),\qquad a_i=y_i/d_i,\qquad b_i=q/d_i.
\]

这不是新的不存在性定理，但可安全采纳为 dependency discipline：gap root、tail root、判别平方根、Hensel/Gaussian 标签若只是该 spine 的投影，就不能重复计作独立 candidate freedom。

## 3. 采纳：branch-free 尾权恒等式

来源 denominator–decimal interface 把三分支尾权统一为

\[
\boxed{\kappa=\frac{10^{m_3}QG}{b_3}}.
\]

它与本仓库现有公式严格等价。

- A2/DD：`ell=m3`，故 `L/tau=10^m3/b3`；
- A1：`ell=m3-g`，而 `10^g L/tau=10^m3/b3`。

因此该恒等式不依赖任何来源仓库的 DD closure 假设，可以作为三分支统一记号直接使用。相应 denominator-tail certificate

\[
10^\ell\mid\kappa^2(\kappa+2G)
\]

的 denominator side 只读取 segmented denominator word 与 effective tail scale。

## 4. 采纳：denominator–decimal shared trace

来源给出等价接口

\[
T_{\rm blk}=(b_1,b_2,b_3,10^\ell),
\]

\[
T_{\rm word}=(\beta,10^{m_2},10^{m_3},10^\ell).
\]

其中 `beta` 为完整 denominator word。两者互相唯一恢复，并决定 `q,Q,G`、第三尾 gcd split 与 denominator-only valuation data。

本仓库采纳其**语义结论**：denominator recovery 与 decimal completion 之间不要重复携带 `delta_3,L,tau,kappa` 等确定性投影。该接口没有关闭任何 A2/DD/A1 分支。

## 5. 保留：基础 T1–T18 与审计修正

外部 `foundations/theorem-index.md` 作为补充定理索引保留。特别是外部 `audit-response.md` 对 T10、T12、T18 给出了独立补证，并主动降级了带覆盖缺口的 E1/E6 等程序结果。

裁决：这些材料可作为额外证明来源，但不替换本仓库的 `problem-and-carrier.md` / `global-framework.md`。机器辅助结论必须保留其原有边界。

## 6. 保留但隔离：critical G 模板

PR6、GD1、GA1-1、GE2-1、GALMB-3 均保留在 `external/dongxuelian2/templates/g/`。它们的 `A1`/`A2` 标签属于来源 critical-G 模板内部命名，不能仅因名称相同就映射成本仓库 Exact-Lift 的 A1/A2 全分支状态。

裁决：作为 scoped lemma / reduction 使用；不改变三分支权威状态。

## 7. DD SGR-9 的逐链审计

SGR-9 的局部 quotient-overload 证明在其 top-DD 假设下闭合。设 `S=m1+m2`、`m=m3`，冻结条件包含

\[
10S+11\le n_3\le11S+3,\qquad d_3\le5S,
\]

从而

\[
m\ge5S+11.
\]

借助 SGR-8 orientation、第三块既约性和 double 5-adic resonance，来源得到

\[
v_5(N)+2m+2v_5(Q)\le9S+9,
\]

故

\[
2m\le9S+9.
\]

与 `m>=5S+11` 矛盾。这个**条件定理**可保留。

问题发生在最后一步“所有 DD candidate 都已被此前链条压入该 top state”。本仓库当前 DD 入口仍明确保留 `n_3/S<6.308883...` 下的 post-tail / non-canonical dominant states，以及 projective/gap、bottom/common-numerator、residual split-Gaussian payer 的 simultaneous height 问题。它们没有被 `n_3>=10S+11` 覆盖。

因此本仓库裁决为：

\[
\boxed{\text{SGR-9 关闭 frozen top-DD 子域；不证明当前 DD 全局为空。}}
\]

来源文件改名为 `dd-top-quotient-overload.md`，避免文件名继续暗示全局 closure。

## 8. A1 backward 成果的作用域修复

来源 `post-DD` 文档先用 `DD=empty` 推出 strict layer 只剩 A1；该全局前提不被本仓库采纳。但其后 A1-only 内部的 word-recovery / oriented word-gap 推导可脱离 DD 使用。

安全保留的局部内容整理到 `external/dongxuelian2/a1/word-recovery-interface.md`：固定 A1 denominator trace 后，完整 numerator word 与真实 decimal cut 必须共同满足 weighted prefix norm；经 denominator-kernel quotient 和 tail deflation 可得到 A1 自身的 oriented gap 与 near-coprime odd-prime allocation。它不关闭 A1。

## 9. 明确拒绝或删除的内容

本次清理不保留下列 staging 冗余稿：

- 外部 `exact-lift-research-synthesis-2026-08-10.md`：与本仓库已有不可变 archive 大面积重复，且后期已有更精确专题替代；
- 外部 `initial-route.md`：早期 strict-layer 总路线，被 theorem index + unified exact-lift + 后续专题覆盖；
- 外部 `exact-lift/status.md`：来源状态快照容易与本仓库权威 `status.md` 混淆；
- `post-dd-a1-frontier.md`：前半依赖未采纳的全局 DD closure；其中可复用 A1 局部结论已单独抽取。

历史失败路线中具有反重复价值的内容（例如 projected phase endogenous / supply-phase route 无独立信息）继续保留，不视为垃圾。

## 10. 当前使用规则

1. 主线状态只看本目录 `status.md` 和三个分支入口。
2. external 文件必须先看来源根 `README.md` 的审计等级。
3. `source status=PROVED/CLOSED` 只表示来源仓库的状态；本仓库的采纳等级以本审计为准。
4. finite computation、fixed-prefix finiteness、CRT uniqueness、projected discriminant/Hensel 条件均不得无条件升级为 global emptiness。
5. 后续若要把外部 scoped lemma 写入分支主线，应给出与当前 branch hypotheses 的显式变量字典和 coverage proof。

# Backward denominator–decimal recovery interface（curated import）

来源：`dongxuelian2/three-term-decimal-concatenation-square-sum@2cfa389f1d4ced90653101e6c92ee8dfe85b5535`，原稿 `research/exact-lift/backward/backward-denominator-decimal-interface.md`。

来源状态：cleaned denominator recovery 与 decimal completion 之间的 **explicit lossless pairwise interface theorem**。本仓库采纳其接口语义和 branch-free `kappa` 恒等式；它不关闭任何 A2/DD/A1 分支。

令
\[
\Lambda=\operatorname{lcm}(b_1,b_2,b_3),\qquad M_i=10^{m_i},\qquad S=10^\ell,
\]
完整 denominator word 为
\[
B=b_1M_2M_3+b_2M_3+b_3.
\]
共享 trace 有两个等价 normal form：
\[
\boxed{T_{\rm blk}=(b_1,b_2,b_3,S)},
\]
\[
\boxed{T_{\rm word}=(B,M_2,M_3,S)}.
\]
word form 通过 decimal cuts 唯一恢复三个 denominator blocks；block form 通过真实 digit lengths 恢复 word 与 cuts。二者都不携带 numerator/sphere information。

第三尾 tuple 由 `(b3,S)` 确定：
\[
\eta_3=\gcd(S,b_3),\qquad
\mathcal L=S/\eta_3,\qquad
\tau=b_3/\eta_3.
\]
同一 trace 还确定
\[
\Lambda,\quad d_i=\Lambda/b_i,\quad Q=b_1M_2+b_2,\quad G=b_1b_2,
\]
以及 denominator-only valuation/gcd/prime-support views。

最直接可纳入本仓库统一记号的恒等式是
\[
\boxed{\kappa=\frac{M_3QG}{b_3}=\frac{10^{m_3}QG}{b_3}}.
\]
它同时覆盖 A2、DD 和 A1。故 denominator-tail certificate
\[
\boxed{S\mid\kappa^2(\kappa+2G)}
\]
的 denominator side 是纯 trace predicate；不需要 gap root、`C,D,N12` 或 tail numerator。

在清除此前误混入 denominator block 的 algebraic/root data 后，来源证明 joint denominator/decimal compatibility 恰是两 semantic blocks 在该 trace 上的 fibre product。换言之，真正 cross-synchronization 只需
\[
\boxed{\text{same segmented denominator word}+\text{same effective tail scale}}.
\]

来源还给出 infinite fibre 与逐分量 collision，说明该 trace 真正遗忘了 numerator/sphere direction，不是把完整 candidate 偷偷编码成另一组变量。

Chamber-specific distinction：DD 中 `S=M3`，所以该 pairwise interface 可降为 denominator triple；A1 中 `S=10^{n3}`，需要额外传递 effective tail scale。**这只是接口差异，不蕴含 DD 已关闭，也不蕴含 strict layer 只剩 A1。**

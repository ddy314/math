# A1 backward word-recovery interface（curated import）

来源：`dongxuelian2/three-term-decimal-concatenation-square-sum@2cfa389f1d4ced90653101e6c92ee8dfe85b5535`，主要抽取自 `research/a1/backward/backward-a1-word-recovery-architecture.md` 与其 post-DD 前置稿。

本文件只保留 **A1-only 内部可独立使用** 的结论；不使用来源的 `DD=empty -> strict only A1` 外推。因此它不能关闭本仓库 A1。

## 1. Fixed denominator trace

在 A1 中令

\[
g=m_3-n_3\ge0,\qquad S=10^{n_3},
\]

\[
Q=b_1 10^{m_2}+b_2,\qquad G=b_1b_2,\qquad D=10^gQ,
\]

并固定

\[
\boxed{T=(b_1,b_2,b_3,S)}.
\]

则 denominator word

\[
\mathbf B=SD+b_3
\]

及 `m_i,Q,G,g,D`、tail gcd split 和 denominator-side `kappa` 都由 `T` 确定。

完整 numerator word 写成

\[
\mathbf A=SP+a_3,
\]

其中

\[
a_3=\mathbf A\bmod S,\qquad P=\lfloor\mathbf A/S\rfloor.
\]

对 first-two decimal cut `n`：

\[
a_1=\lfloor P/10^n\rfloor,\qquad a_2=P\bmod10^n.
\]

定义 weighted prefix norm

\[
F_n=b_2^2a_1^2+b_1^2a_2^2.
\]

任何真实 A1 candidate 必须满足 exact word-recovery equation

\[
\boxed{
F_n=G^2\left[\left(\frac{\mathbf A}{\mathbf B}\right)^2-\left(\frac{a_3}{b_3}\right)^2\right].
}
\tag{A1-WR}
\]

并同时满足真实 digit windows 与逐块 `gcd(a_i,b_i)=1`。这条 formulation 的主要价值是强制 norm 使用**同一个真实 decimal cut**；来源给出的显式 pseudo-family 说明，如果忘掉这一 cut，即使保留 sphere/norm/tail/Gaussian/reducedness 的大量投影，也会留下无穷伪解。

## 2. Denominator-kernel quotient

令

\[
\Lambda=\operatorname{lcm}(b_1,b_2,b_3),\qquad
\Gamma=\gcd(\mathbf B,\Lambda),\qquad E=\mathbf B/\Gamma.
\]

来源在其 strict foundation 中证明 `E|A-word`。写

\[
\mathbf A=EW,\qquad \mathbf B=E\Gamma.
\]

于是 global concatenation ratio 降为

\[
\mathbf A/\mathbf B=W/\Gamma.
\]

这是安全的 normalization：它只移除 denominator word 强制的 common multiplier，不创造新的候选自由度。

## 3. A1 自身的 oriented word-gap

令

\[
h=\gcd(W,\Gamma),\qquad W=hu,\quad\Gamma=hv,\qquad\gcd(u,v)=1.
\]

来源由 A1 word identity 本身得到

\[
\boxed{J_-:=b_3u-a_3v=S\varepsilon>0},
\]

以及

\[
Nv^2b_3^2=G^2J_-J_+,
\qquad J_+=b_3u+a_3v,
\]

这里的 minus orientation 来自 A1 的 exact word geometry，不借用 DD 的 source orientation。

进一步写

\[
\eta=\gcd(S,b_3),\qquad S=\eta\mathcal L,\qquad b_3=\eta\tau,\qquad\gcd(\mathcal L,\tau)=1.
\]

由第三块既约性与 `J_-=S epsilon` 有 `eta|v`。令 `v=eta vbar`，得到

\[
\boxed{\tau u-a_3\bar v=\mathcal L\varepsilon>0},
\]

\[
\boxed{N\eta^2\bar v^2\tau^2=G^2(\tau u-a_3\bar v)(\tau u+a_3\bar v)}.
\]

## 4. Odd-prime cross-content

定义

\[
c_a=\gcd(a_3,u),\qquad c_\tau=\gcd(\tau,\bar v),
\]

并约去这两个 cross-content 后，来源得到 normalized factors `Z_-`,`Z_+` 满足

\[
\boxed{\gcd(Z_-,Z_+)\mid2}.
\]

因此 odd-prime allocation 在两 gap factors 之间是 complementary 的；residual decimal-prime depth `mathcal L` 不能被 `c_tau` 吸收。

把 prefix norm 的 common content 同时约去后，来源进一步得到每个 `p=3 mod 4` 在 `Z_-`、`Z_+` 中的赋值均为偶数，因此两个 normalized gap factors 各自满足 sum-of-two-squares 的必要 prime-class 条件。

## 5. 审计等级

- 上述 fixed-trace、quotient、oriented-gap 与 gcd/squareclass 公式：作为 **scoped structural lemmas** 保留；它们只在 A1 hypotheses 下使用。
- 来源关于 legal cut fibre `<=2` 的结论依赖另一份 exact-root-pair / discrete-convexity 证明链；本次没有把该完整链迁入，因此这里只作为来源记录，不把它用于本仓库任何 closure。
- 来源明确构造了忘掉 actual decimal cut 后的无限 pseudo-family，这项 negative knowledge 被采纳：未来不能用只看 projected prime/Gaussian/tail gates 的系统代替真实 word-cut synchronization。
- **A1 仍待证。**

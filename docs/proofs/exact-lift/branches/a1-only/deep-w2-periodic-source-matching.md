# A1 minimal diagonal: periodic source matching for `w=2`

> 日期：2026-08-27。依赖 `deep-2high-coefficient-source-minima.md` 与 `deep-w2-coefficient-source-conflict.md`。当前统一 frontier `k>=32`。
>
> 本文只加强 `w=2` 的 complement-source lower bound。核心新增条件是：`b_1` 与 `Q` 两侧选出的负模四 source prime 不仅必须不同，还必须能够在同一个 `k` 上同时出现。

状态：**严格完成；附 exact residue-cycle checker。**

---

## 1. source residue classes

`w=2` 时

\[
b_1(k)=10^{2k+1}-2,
\qquad
Q(k)=10^{2k+2}-19.
\]

对任意 `p\equiv3\pmod4` 且 `p\nmid10`，记

\[
o_p:=\operatorname{ord}_p(10).
\]

定义两个 exact source class sets

\[
\mathcal C_b(p)
:=\{a\bmod o_p:\ p\mid10^{2a+1}-2\},
\]

\[
\mathcal C_Q(p)
:=\{a\bmod o_p:\ p\mid10^{2a+2}-19\}.
\]

于是

\[
p\mid b_1(k)
\Longleftrightarrow
k\bmod o_p\in\mathcal C_b(p),
\]

\[
p\mid Q(k)
\Longleftrightarrow
k\bmod o_p\in\mathcal C_Q(p).
\]

前几个 `b_1` source：

\[
\begin{array}{c|c|c}
p&o_p&\mathcal C_b(p)\\ \hline
19&18&\{8,17\}\\
31&15&\{10\}\\
59&58&\{12,41\}\\
71&35&\{14\}\\
131&130&\{41,106\}\\
151&75&\{17\}
\end{array}
\tag{1}
\]

前几个 `Q` source：

\[
\begin{array}{c|c|c}
q&o_q&\mathcal C_Q(q)\\ \hline
3&1&\{0\}\\
31&15&\{12\}\\
59&58&\{10,39\}\\
67&33&\{22\}\\
71&35&\{26\}\\
107&53&\{23\}
\end{array}
\tag{2}
\]

这些表只来自一个完整 multiplicative-order period 的 exact enumeration。

---

## 2. simultaneous-source compatibility

设 `p` 是实际 candidate 中留在 `u/2` 的一个 `3 mod 4` odd source prime，`q` 是留在 `v` 的一个 `3 mod 4` odd source prime。

已有 cross-coprimality 给

\[
p\nmid\alpha,
\qquad
q\nmid\beta.
\tag{3}
\]

又因为

\[
\gcd(b_1,Q)=1,
\]

必有

\[
\boxed{p\ne q.}
\tag{4}
\]

更重要的是，两者来自同一个实际 `k`，所以必须存在

\[
a\in\mathcal C_b(p),
\qquad
b\in\mathcal C_Q(q)
\]

满足 generalized CRT compatibility

\[
\boxed{
a\equiv b
\pmod{\gcd(o_p,o_q)}.}
\tag{5}
\]

若 (5) 对所有 residue pair 都失败，则 `(p,q)` 即使分别能在两个序列中出现，也绝不可能同时成为同一个 candidate 的 source pair。

---

## 3. periodic matching lower bound

定义

\[
\boxed{
J_2^{\rm per}(\alpha,\beta)
:=2\min pq,
}
\tag{6}
\]

其中 minimum 遍历满足以下全部条件的 source pairs：

1. `p\in\mathcal P_b(2)`；
2. `q\in\mathcal P_Q(2)`；
3. `p\nmid\alpha`；
4. `q\nmid\beta`；
5. `p\ne q`；
6. `(p,q)` 满足 (5) 的 simultaneous-`k` compatibility。

实际 candidate 自身提供至少一个这样的 pair，因此 minimum 有定义，并且

\[
\boxed{M=uv\ge J_2^{\rm per}(\alpha,\beta).}
\tag{7}
\]

旧 `J_2(\alpha,\beta)` 只使用条件 1--5；所以恒有

\[
\boxed{J_2^{\rm per}\ge J_2.}
\tag{8}
\]

---

## 4. `3|beta` 的新统一加强

假设

\[
3\mid\beta.
\]

则 `Q`-side source `3` 被 coefficient absorption 排除，最小剩余 Q-source 是 `31`。

若 `19\nmid\alpha`，独立大小排序首先会尝试

\[
(p,q)=(19,31).
\]

但

\[
\mathcal C_b(19)=\{8,17\}\pmod{18},
\]

两者都满足

\[
k\equiv2\pmod3,
\]

而

\[
\mathcal C_Q(31)=\{12\}\pmod{15}
\]

要求

\[
k\equiv0\pmod3.
\]

由于

\[
\gcd(18,15)=3,
\]

这两个 source 不能同时出现。

`(31,31)` 又被 (4) 排除。下一最小可兼容 pair 是

\[
(p,q)=(19,59).
\]

这里

\[
\gcd(18,58)=2,
\]

而两边 residue sets 都同时含偶、奇 residue，因此 generalized CRT compatible。

故无论 `alpha` 是否吸收 19，都有统一下界

\[
\boxed{3\mid\beta\Longrightarrow M\ge2\cdot19\cdot59=2242.}
\tag{9}
\]

若 `19\mid\alpha`，`p=19` 也被排除，于是最小兼容 pair 变成

\[
(31,59),
\]

得到更强的旧层级

\[
\boxed{3\mid\beta,\ 19\mid\alpha
\Longrightarrow M\ge3658.}
\tag{10}
\]

---

## 5. denominator cap 立即更新

由 complement height

\[
\mu=MD/T^2<10001,
\]

所以 (9) 给

\[
\boxed{
3\mid\beta
\Longrightarrow
\frac D{T^2}<\frac{10001}{2242}
<4.461.}
\tag{11}
\]

相比旧的 independent bound

\[
M\ge1178,
\qquad D/T^2<9,
\]

这里约再缩小一半。

若再有 `19|alpha`：

\[
\boxed{
\frac D{T^2}<\frac{10001}{3658}<2.735.}
\tag{12}
\]

---

## 6. 更深 coefficient absorption 的周期层级

同一 checker 还给出一些可直接复用的 exact examples：

\[
\boxed{
\begin{array}{c|c|c|c}
\alpha\text{ absorbs}&\beta\text{ absorbs}
&J_2^{\rm per}&\text{first compatible pair}\\ \hline
1&1&114&(19,3)\\
1&3&2242&(19,59)\\
19&1&186&(31,3)\\
19&3&3658&(31,59)\\
19\cdot31&3&3658&(59,31)\\
19&3\cdot31&3658&(31,59)\\
19\cdot31&3\cdot31&7906&(59,67)\\
1&3\cdot31\cdot59&2698&(19,71)\\
19&3\cdot31\cdot59&4154&(31,67)
\end{array}}
\tag{13}
\]

最后两行展示了真正的 periodic effect：即使 `p\ne q`，最小的 distinct source pair 仍可能因 shared order residue 冲突而被排除。

例如 `beta` 吸收 `3,31,59` 时，最小 Q-source 是 67；但 `(19,67)` 不兼容，因为

\[
\gcd(18,33)=3,
\]

`b`-side 19 要求 `k=2 mod 3`，而 Q-side 67 要求 `k=1 mod 3`。因此若 `19\nmid\alpha`，最小兼容 pair 跳到 `(19,71)`。

---

## 7. certificate boundary

本文没有假设 factorization of `b_1` 或 `Q` 可整体控制。证明只使用：

- 实际 `u/2\equiv3 mod4` 必提供至少一个 `3 mod4` odd source prime；
- 实际 `v\equiv3 mod4` 必提供至少一个同类 source prime；
- cross-coprimality 排除 coefficient-absorbed sources；
- `gcd(b_1,Q)=1` 排除同一 prime；
- 同一 `k` 必满足两个 exact residue cycles 的 generalized CRT compatibility。

因此 (7) 是 full 2-high master 上的严格 necessary lower bound；moderate 与 `E_2` 都可使用。

附审计：

`scripts/exact-lift/a1-only/research-checks/deep-denominator/check_a1_deep_w2_periodic_source_matching.py`。

---

## 8. moderate one-exponent interface

`w=2` 的 coefficient source hierarchy 现在应使用

\[
J_2^{\rm per}(\alpha,\beta)
\]

而不是只使用 independent first-source minima 或 distinctness-only `J_2`。

在 moderate HL 中

\[
a_2=v_2(r),
\qquad a_5=v_5(r),
\qquad k=d+Y-1,
\]

并且精确有

\[
\boxed{
\frac D{T^2}
=2^{3-a_2}5^{2-a_5-2d}
=\frac{200r_{10}}{r\,25^d}.}
\tag{14}
\]

因此 (7) 与 complement height 等价给出必要条件

\[
\boxed{
25^d>
\frac{200J_2^{\rm per}(\alpha,\beta)r_{10}}
{10001r}.}
\tag{15}
\]

所以 source cap 在 one-exponent family 中的正确作用是：给 fixed coefficient cell 一个显式 lower bound on `d`，而不是删除整个 unbounded coefficient partition。因为 `D/T^2` 随 `d` 按 `25^{-d}` 下降，任何固定 finite `J_2^{per}` 最终都会满足 cap。

要获得真正的 tail control，需要继续保留 source 的 `k`-residue 信息，而不是只保留其全局 minimum。`deep-w2-periodic-source-envelope.md` 正是这一 refinement：它构造 `J_3(k)`，再令 `k=d+Y-1` 得到直接的 `d`-periodic sieve。
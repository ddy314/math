# A1 minimal diagonal: periodic `w=2, 3|beta` source lower envelope

> 日期：2026-08-27。依赖 `deep-w2-periodic-source-matching.md`。当前统一 frontier `k>=32`。
>
> 本文把 pairwise compatibility 进一步组织成一个真正依赖 `k mod L` 的 periodic lower envelope。只假设 `w=2` 与 `3|beta`；`alpha` 或 `beta` 吸收更多 source primes 只会加强本文的下界。

状态：**严格完成；附 exact period checker。**

---

## 1. 使用的 finite source prefix

`b_1=10^{2k+1}-2` 的前四个 `3 mod 4` source primes：

\[
19,31,59,71,
\]

其下一个 source prime 是

\[
131.
\]

`Q=10^{2k+2}-19` 在 `3|beta` 时 source `3` 被 cross-coprimality 排除；随后前四个可见 Q-source primes：

\[
31,59,67,71,
\]

其下一个 source prime 是

\[
107.
\]

对应 order：

\[
18,15,58,35,
\]

与

\[
15,58,33,35.
\]

故所有这些 small-source occurrence pattern 的公共 period 为

\[
\boxed{
L=\operatorname{lcm}(18,15,58,35,33)=200970.}
\tag{1}
\]

---

## 2. residue-wise safe lower envelope

对每个 `k mod L`：

- 列出实际能整除 `b_1(k)` 的 known sources `19,31,59,71`；
- 列出实际能整除 `Q(k)` 的 known sources `31,59,67,71`；
- 若 actual negative source 不在已列出的 `b` primes 中，则它至少为 131；
- 若 actual negative Q-source 不在已列出的 Q primes 中，则它至少为 107；
- 两侧 actual source 还必须不同，因为 `gcd(b_1,Q)=1`。

令 `J_3(k)` 为按这些规则得到的最小安全值 `2pq`。则任何

\[
w=2,\qquad3\mid\beta
\]

candidate 都满足

\[
\boxed{M=uv\ge J_3(k).}
\tag{2}
\]

注意这里把 unknown larger source 仅替换成 lower sentinel `131` 或 `107`；因此即使 sentinel 本身在该 residue 不整除母体，也只会把 lower bound 取得更小，不会误删真实 candidate。

---

## 3. exact period distribution

完整枚举一个 period `0<=k<L`，`J_3(k)` 只取 16 个值：

\[
\boxed{
\begin{array}{r|r|r}
J_3&\#\{k\bmod L\}&\text{比例}\\ \hline
2242&770&0.3831\%\\
2698&616&0.3065\%\\
3658&924&0.4598\%\\
4066&20944&10.4215\%\\
4154&1176&0.5852\%\\
6634&11760&5.8516\%\\
7906&168&0.0836\%\\
8122&12936&6.4368\%\\
8378&346&0.1722\%\\
9514&162&0.0806\%\\
12626&4898&2.4372\%\\
15194&4590&2.2839\%\\
15458&5060&2.5178\%\\
17554&4374&2.1764\%\\
18602&4590&2.2839\%\\
28034&127656&63.5199\%
\end{array}}
\tag{3}
\]

总数精确为

\[
\sum  \# =200970=L.
\]

因此：

\[
\boxed{99.3103\%\text{ of residues have }J_3\ge3658,}
\tag{4}
\]

\[
\boxed{88.4291\%\text{ have }J_3\ge4154,}
\tag{5}
\]

\[
\boxed{81.9923\%\text{ have }J_3\ge7906,}
\tag{6}
\]

\[
\boxed{63.5199\%\text{ have }J_3=28034.}
\tag{7}
\]

最弱值 `2242` 只出现在 770 个 residue，即整个 period 的约 `0.38%`。

---

## 4. denominator envelope

complement height 给

\[
\mu=MD/T^2<10001.
\]

因此 residue-wise：

\[
\boxed{
\frac D{T^2}<\frac{10001}{J_3(k)}.}
\tag{8}
\]

例如占 63.52% 的最大 lower-envelope cells 上：

\[
\boxed{
M\ge28034
\Longrightarrow
D/T^2<10001/28034<0.357.}
\tag{9}
\]

这比统一 `3|beta` cap `D/T^2<4.461` 强超过一个数量级。

---

## 5. moderate one-exponent 中变成 `d`-periodic sieve

moderate HL 写

\[
a_2=v_2(r),
\qquad a_5=v_5(r),
\qquad
k=d+Y-1.
\]

精确有

\[
\boxed{
\frac D{T^2}
=2^{3-a_2}5^{2-a_5-2d}
=\frac{200r_{10}}{r\,25^d}.}
\tag{10}
\]

因此 (8) 等价于必要条件

\[
\boxed{
2^{3-a_2}5^{2-a_5-2d}
<\frac{10001}{J_3(d+Y-1)}.}
\tag{11}
\]

或者

\[
\boxed{
25^d>
\frac{200J_3(d+Y-1)r_{10}}{10001r}.}
\tag{12}
\]

所以 fixed moderate cell `(r,Y,alpha,beta)` 若有 `3|beta`，可以在进入 divisor test 前先对 `d mod 200970` 使用 (11)。

这个条件不会关闭整个 unbounded tail：左侧随 `d` 指数增长，故任何固定 finite source envelope 最终都会被满足。它的正确用途是删除低 `d` 与建立 residue-dependent denominator height，而不是宣称删除整个 coefficient partition。

---

## 6. 一个最小层例子

若

\[
a_2=0,
\qquad a_5=1,
\]

则

\[
D/T^2=8\cdot5^{1-2d}.
\]

在 `J_3=28034` 的 residue 上，`d=1` 会给

\[
D/T^2=8/5=1.6,
\]

但 (9) 要求 `<0.357`，故这些 residue 上

\[
\boxed{d\ge2.}
\]

类似地可对每个 finite `(a_2,a_5,Y)` cell 直接用 exact integer arithmetic 计算首个 admissible `d`。

---

## 7. dependency boundary

`J_3(k)` 只使用 prime-source / whole-block 信息：

- exact divisibility cycles of finitely many small source primes；
- cross-coprimality；
- `gcd(b_1,Q)=1`；
- next-source lower sentinels 131 与 107。

它与 contact-square `q^2` lifting、5-adic Hensel lock、normalized `R` shell 均不是同一个条件的重复写法，因此可以作为独立 prime-source sieve 与这些结构联立。

附审计：

`scripts/exact-lift/a1-only/research-checks/deep-denominator/check_a1_deep_w2_periodic_source_envelope.py`。

---

## 8. 下一接口

下一步有两条可并行推进的路线：

1. moderate：把 `J_3(d+Y-1)` 与已经有限化的 `(r,m)` contact-shell slots 联合，优先清理 small `d`；
2. full master：把 dual-slot exact form
   \[
   q=\frac{(m+1)G+e'}{2\beta}
   \]
   代入 contact-square `q^2/delta_C` lifting，寻找对 supply denominator `G` 的真正新 resultant bound。

第二条才有机会控制 unbounded tail；本文的 finite source envelope 本身不声称完成该步骤。
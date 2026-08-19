# A2 equal-depth resonance 的 target-prefix ladder 与 fixed `7` exception

> **依赖：** `spontaneous-height-equal-depth-tail-gcd-ladder.md`、`spontaneous-height-equal-depth-decimal-pair.md`、`spontaneous-height-equal-depth-tail-normalization.md`、`primitive-reduction.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文把上一层 canonical resonance ladder 再与真正的 omega-height target selector 联立。对每个 genuine non-`3` equal-depth oversaturation target，fixed quadratic `P_{omega H}(K)=6K^2-36K+55` 的 p-depth恰为 `h=v_p(W_q)=v_p(omega)`；而在当前 endpoint，它本身只是一个恰有 `2M+3` 位的 pure-prefix positive integer。因此所有 target baseline prime powers 的乘积统一装入同一个短 prefix carrier。再把 `P_{omega H}` 与 `qW_q=DK-N` 消去 `K`，得到 source-prefix resultant `R_PD=55D^2-36DN+6N^2`。若 target resonance 真正满足 `rho_p>=1`，则除固定素数 `7` 外有 `v_p(R_PD)=h` 精确等号；`R_PD` 可能比 baseline 多一层的全部 moving prime 被 exact Bezout identity 压成唯一 fixed exception `p=7`。本文不排除 `p=7`，也不宣称 A2 closure。

---

## 1. target setting

固定当前 genuine non-`3` inert equal-depth omega-height oversaturation target prime `p`。写

\[
\boxed{
v_p(\omega)=v_p(W_q)=h\ge1.}
\tag{1.1}
\]

沿用

\[
\boxed{
\mathcal P_{\omega H}(K)
:=6K^2-36K+55.}
\tag{1.2}
\]

`spontaneous-height-equal-depth-decimal-pair.md` 已从 `B_W` oversaturation 精确得到

\[
\boxed{
v_p(\mathcal P_{\omega H}(K))=h.}
\tag{1.3}
\]

另一方面

\[
\boxed{qW_q=DK-N,}
\tag{1.4}
\]

且当前 genuine height prime 与 `qD` 分离，因此

\[
\boxed{
v_p(DK-N)=h.}
\tag{1.5}
\]

记

\[
U:=DK-N=qW_q.
\tag{1.6}
\]

于是 target baseline 已同时落在一个 quadratic value 与一个 linear value 上：

\[
\boxed{
p^h\Vert \mathcal P_{\omega H}(K),
\qquad
p^h\Vert U.}
\tag{1.7}
\]

---

## 2. `P_{omega H}(K)` 是一个只有 `2M+3` 位的 pure-prefix carrier

当前 endpoint 写

\[
N=10^M,
\qquad
\frac{249}{250}<y:=\frac{10a_2}{N}<1,
\]

所以

\[
\frac KN=9+y
\]
满足

\[
\boxed{
\frac{2499}{250}<\frac KN<10.}
\tag{2.1}
\]

又 `M>=11`。因此

\[
\frac{\mathcal P_{\omega H}(K)}{N^2}
=6\left(\frac KN\right)^2
-\frac{36}{N}\frac KN
+\frac{55}{N^2}.
\tag{2.2}
\]

下界使用 `K/N>2499/250`、`K/N<10` 与 `N>=10^11`：

\[
\frac{\mathcal P_{\omega H}(K)}{N^2}
>
6\left(\frac{2499}{250}\right)^2
-\frac{360}{10^{11}}
>599.
\tag{2.3}
\]

上界则由 `K<10N` 且 `K>=1`：

\[
6K^2<600N^2,
\qquad
-36K+55<0,
\]
所以

\[
\boxed{
599N^2
<\mathcal P_{\omega H}(K)
<600N^2.}
\tag{2.4}
\]

因此

\[
\boxed{
\mathcal P_{\omega H}(K)
\text{ 恰有 }2M+3\text{ 个十进制数字}.}
\tag{2.5}
\]

这比此前 `J_H/H_pref` 的 `4M+1` 位 carrier 更短；它直接读取 target baseline `h`，但不读取 resonance tail `rho_p`。

---

## 3. 所有 equal-depth oversaturation targets 的 baseline product 共享同一短 carrier

令 `E_tar` 为当前所有 genuine non-`3` equal-depth omega-height oversaturation target primes。对每个

\[
p\in E_{\rm tar}
\]
写

\[
h_p:=v_p(\omega)=v_p(W_q).
\]

定义

\[
\boxed{
G_{\rm tar}:=
\prod_{p\in E_{\rm tar}}p^{h_p}.}
\tag{3.1}
\]

由 (1.3)，不同 target primes 的对应 prime powers 全部整除同一个 `P_{omega H}(K)`：

\[
\boxed{
G_{\rm tar}\mid\mathcal P_{\omega H}(K).}
\tag{3.2}
\]

而且 target support 上是 exact baseline depth：

\[
\boxed{
v_p(\mathcal P_{\omega H}(K))=h_p.}
\tag{3.3}
\]

结合 (2.4)：

\[
\boxed{
G_{\rm tar}<600\cdot10^{2M}.}
\tag{3.4}
\]

等价地

\[
\boxed{
\sum_{p\in E_{\rm tar}}h_p\log p
<\log600+2M\log10.}
\tag{3.5}
\]

这是一个只依赖 `M` 的 target-baseline global budget；第三块长度 `m` 已完全消失。

---

## 4. target-specific gcd ladder 可以直接用 `P_{omega H}` 代替 `Gamma`

上一层定义了 canonical full-tail quotient

\[
\Lambda_{\rm tail},
\]

并对 equal-depth target prime证明

\[
\boxed{v_p(\Lambda_{\rm tail})=\rho_p.}
\tag{4.1}
\]

对 `k>=1` 定义纯 prefix target ladder

\[
\boxed{
T_k
:=\gcd\!\left(
\mathcal P_{\omega H}(K)^k,
\Lambda_{\rm tail}
\right).}
\tag{4.2}
\]

则对每个真正 target prime，由 (1.3)、(4.1)：

\[
\boxed{
v_p(T_k)=\min(kh_p,\rho_p).}
\tag{4.3}
\]

所以 target 的完整 resonance tail 可以在一个 `2M+3` 位 pure-prefix base 上逐层读取。

必须审计：`T_k` 可能还含有并非 omega-height oversaturation target 的其它 common primes，因此 (4.3) 只对真实 target support 给出 exact valuation；本文不把 `T_k` 的全部 support 误称为 target set。

---

## 5. 消去 `K`：一个 source-prefix resultant

由

\[
U=DK-N
\]
定义

\[
\boxed{
\mathscr R_{PD}
:=55D^2-36DN+6N^2.}
\tag{5.1}
\]

直接展开 `D^2 P_{omega H}(K)`：

\[
\boxed{
D^2\mathcal P_{\omega H}(K)
=
\mathscr R_{PD}
+(12N-36D)U
+6U^2.}
\tag{5.2}
\]

所以由 (1.7)：

\[
\boxed{p^h\mid\mathscr R_{PD}.}
\tag{5.3}
\]

也就是说 target baseline `h` 还必须由一个完全不含 `K,omega,W_q,a_3,b_3` 的 source-prefix quadratic 承担。

模 `p` 看 (5.1)，因为 `p\nmid N`：

\[
55\left(\frac DN\right)^2
-36\frac DN+6\equiv0\pmod p.
\tag{5.4}
\]

其 discriminant 仍为

\[
36^2-4\cdot55\cdot6=-24,
\]
所以这里的 first-layer quadratic character仍只是已有 `sqrt(-6)` orbit 的重写；本文不把它计作新的 Legendre obstruction。

---

## 6. deep resonance 把 `R_PD/p^h` 压成一个线性 factor

现在进一步假设

\[
\boxed{\rho_p\ge1.}
\tag{6.1}
\]

`spontaneous-height-equal-depth-decimal-pair.md` 定义

\[
R_+=D\mathcal P_{\omega H}(K)-KU
\tag{6.2}
\]

并证明 deep resonance 时

\[
\boxed{p^{h+1}\mid R_+.}
\tag{6.3}
\]

写

\[
\mathcal P_{\omega H}(K)=p^hP_0,
\qquad
U=p^hU_0,
\qquad
p\nmid P_0U_0.
\tag{6.4}
\]

由 (6.2)–(6.3) 除以 `p^h`：

\[
\boxed{DP_0\equiv KU_0\pmod p.}
\tag{6.5}
\]

另一方面 `U=DK-N` 且 `p|U`，所以

\[
\boxed{DK\equiv N\pmod p.}
\tag{6.6}
\]

将 (5.2) 除以 `p^h` 并模 `p`，`U^2/p^h` 因 `h>=1` 消失：

\[
\frac{\mathscr R_{PD}}{p^h}
\equiv
D^2P_0-(12N-36D)U_0
\pmod p.
\]

再用 (6.5)、(6.6)：

\[
D^2P_0
\equiv DKU_0
\equiv NU_0
\pmod p.
\]

因此得到关键 next-layer identity：

\[
\boxed{
\frac{\mathscr R_{PD}}{p^h}
\equiv
(36D-11N)U_0
\pmod p.}
\tag{6.7}
\]

由于 `U_0` 为 p-unit：

\[
\boxed{
v_p(\mathscr R_{PD})>h
\Longleftrightarrow
p\mid(36D-11N)
\qquad(\rho_p\ge1).}
\tag{6.8}
\]

所以 moving deep resonance 若想让 source-prefix resultant 继续超过 baseline depth，已经被压到一个单独的线性 source ratio。

---

## 7. 线性 exceptional overlap 只能是固定素数 `7`

`R_PD` 与 `36D-11N` 有 exact Bezout identity

\[
\boxed{
1296\mathscr R_{PD}
-(1980D-691N)(36D-11N)
=175N^2.}
\tag{7.1}
\]

直接展开即可验证。

若 genuine target prime满足

\[
p\mid\mathscr R_{PD},
\qquad
p\mid(36D-11N),
\]
则由 `p\nmid6N` 和 (7.1)：

\[
p\mid175=5^2\cdot7.
\]

当前 prime 非 `5`，因此

\[
\boxed{p=7.}
\tag{7.2}
\]

结合 (6.8)：

\[
\boxed{
\rho_p\ge1,\ p\ne7
\Longrightarrow
v_p(\mathscr R_{PD})=h.}
\tag{7.3}
\]

这是一条新的 exact-depth statement：所有 moving deep target primes 在 `R_PD` 上都只能支付 baseline `h`，唯一可能让该 resultant继续 Hensel 加深的 prime 被固定为 `7`。

---

## 8. `p=7` 的固定局部形状

本文不排除 `p=7`，但其 first-layer residue 已完全固定。

若

\[
7\mid(36D-11N),
\]
则

\[
\boxed{D\equiv4N\pmod7.}
\tag{8.1}
\]

又 `U=DK-N` 被 `7` 整除，所以

\[
4K-1\equiv0\pmod7,
\]
即

\[
\boxed{K\equiv2\pmod7.}
\tag{8.2}
\]

而

\[
\mathcal P_{\omega H}(2)
=24-72+55=7,
\]
所以这与 `P_{omega H}` 的 simple `7`-root完全一致。

因此 fixed `7` branch 是一个真正的 simple local orbit，不能仅凭 first-order resultant排除；若后续需要关闭它，应单独使用更高 `7`-adic digit、source allocation 或 endpoint size，而不能把 (7.2) 误写成矛盾。

---

## 9. 当前 target frontier

现在 equal-depth omega-height target 已有三层 canonical reader：

\[
\boxed{
\begin{array}{c|c|c}
\text{层}&\text{carrier}&\text{target p-depth}\\ \hline
\text{baseline prefix}
&\mathcal P_{\omega H}(K)
&h\\
\text{full resonance tail}
&\Lambda_{\rm tail}
&\rho_p\\
\text{source-prefix check}
&\mathscr R_{PD}
&h\quad(p\ne7,\ \rho_p\ge1).
\end{array}}
\tag{9.1}
\]

其中 `P_{omega H}` 只有 `2M+3` 位，并统一容纳所有 target baseline prime powers；`Lambda_tail` 读取全部 tail；`R_PD` 则证明除 fixed `7` 外 deep target 的 source-prefix resultant不能继续超过 baseline。

下一步最有价值的攻击点已经变成：

1. 单独处理 fixed `7` orbit；
2. 对 `p!=7`，把两个 exact-baseline carriers `P_{omega H}` 与 `R_PD` 的 unit quotients联立 `Lambda_tail`，尝试产生第二个不再属于 `sqrt(-6)` shadow 的线性/Archimedean约束；
3. 或利用 global bound `G_tar<600*10^{2M}` 与 `Lambda_tail` 的 full-tail budget证明 target weighted product过饱和。

A2 仍为 `待证`。
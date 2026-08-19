# A2 equal-depth fixed `7/2671` exceptions 的二阶横截性

> **依赖：** `spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-equal-depth-triple-orientation.md`、`spontaneous-height-equal-depth-fixed7-hensel.md`。
>
> **严格状态：**前面的 next-depth 审计留下两个 fixed exceptions：`p=7` 控制 source-prefix resultant `R_PD` 是否能超过 baseline，`p=2671` 控制 source/third orientation carrier `L_D3` 是否能超过 baseline。本文证明两例中的“quadratic target root”与“exceptional linear root”都只在 first layer 相交：相应 Bezout 常数在 fixed prime 上恰有赋值 `1`，所以两个 simple Hensel branches 不可能同时提升到 `p^2`。显式地，`7` 的两个 lifts 为 `32` 与 `18 mod 49`，`2671` 的两个 lifts 为 `2825391` 与 `5707400 mod 2671^2`。因此 fixed exceptions 本身不产生新的 singular/unbounded Hensel tree；任何更高 extra depth 必须来自 normalized companion cancellation。本文仍不排除这种 cancellation，因此不关闭 A2。

---

## 1. fixed `7` 的两个 first-layer equations

记

\[
R_{PD}:=55D^2-36DN+6N^2,
\]

\[
F_7:=36D-11N.
\]

此前已证明：若 deep equal-depth target 使

\[
v_7(R_{PD})>h,
\]
则必须进入 fixed branch

\[
\boxed{7\mid R_{PD},\qquad 7\mid F_7.}
\tag{1.1}
\]

并且

\[
D\equiv4N\pmod7.
\tag{1.2}
\]

已有 exact Bezout identity

\[
\boxed{
1296R_{PD}
-(1980D-691N)F_7
=175N^2.}
\tag{1.3}
\]

由于 genuine target 满足 `7\nmid N`，右端赋值为

\[
\boxed{v_7(175N^2)=1.}
\tag{1.4}
\]

在 `D=4N mod 7` 上，另一个 coefficient 为

\[
1980D-691N
\equiv(1980\cdot4-691)N
\equiv5N\not\equiv0\pmod7.
\tag{1.5}
\]

而 `1296` 也是 `7`-进单位。

所以若 `R_PD` 与 `F_7` 都被 `49` 整除，则 (1.3) 左端被 `49` 整除，与 (1.4) 矛盾。因此

\[
\boxed{
\min\{v_7(R_{PD}),v_7(F_7)\}=1
\qquad\text{在 fixed-7 first-layer intersection 上}.}
\tag{1.6}
\]

特别地，真正 extra-resultant branch有 `v_7(R_PD)>h>=1`，故

\[
\boxed{v_7(F_7)=1.}
\tag{1.7}
\]

也就是说 `F_7` 的 exceptional linear root永远只贡献第一层；`R_PD` 若继续深化，不是因为同一个 linear root继续 Hensel 跟随。

---

## 2. fixed `7` 两个 Hensel roots 在 `49` 上显式分离

写 unit ratio

\[
d:=D/N.
\]

`R_PD=0` 化为

\[
\boxed{55d^2-36d+6=0.}
\tag{2.1}
\]

fixed first root是

\[
d\equiv4\pmod7.
\]

其 derivative

\[
110d-36
\]
在 `d=4` 时为 unit，因此唯一 Hensel lift。直接计算：

\[
\boxed{d\equiv32\pmod{49}.}
\tag{2.2}
\]

另一方面 linear exception

\[
36d-11=0
\]
的唯一 lift为

\[
\boxed{d\equiv18\pmod{49}.}
\tag{2.3}
\]

显然

\[
32\not\equiv18\pmod{49}.
\]

所以：

\[
\boxed{
R_{PD}=0\text{ 与 }F_7=0
\text{ 的两个 simple 7-adic branches只在 mod }7\text{ 相交}.}
\tag{2.4}
\]

---

## 3. fixed `2671` 的 exact Bezout同样只有一层

令

\[
p_*:=2671,
\]

\[
P:=6K^2-36K+55,
\qquad
F_*:=5K-36.
\]

triple-orientation 文件证明，若 `L_D3` 想超过 target baseline，则唯一可能先满足

\[
\boxed{p_*\mid P,\qquad p_*\mid F_*.}
\tag{3.1}
\]

其共同 first root为

\[
\boxed{K\equiv2144\pmod{2671}.}
\tag{3.2}
\]

exact Bezout为

\[
\boxed{
25P-(30K+36)F_*=2671.}
\tag{3.3}
\]

右端有精确赋值

\[
\boxed{v_{2671}(2671)=1.}
\tag{3.4}
\]

在 `K=2144 mod 2671` 上

\[
30K+36\equiv252\not\equiv0\pmod{2671},
\tag{3.5}
\]

且 `25` 也是 unit。因此完全同理：

\[
\boxed{
\min\{v_{2671}(P),v_{2671}(F_*)\}=1.}
\tag{3.6}
\]

对 target baseline

\[
h:=v_{2671}(P),
\]
立刻得到 dichotomy：

\[
\boxed{
 h\ge2
 \Longrightarrow
 v_{2671}(F_*)=1,}
\tag{3.7}
\]

以及

\[
\boxed{
 v_{2671}(F_*)\ge2
 \Longrightarrow
 h=1.}
\tag{3.8}
\]

所以 linear orientation exception 与 target quadratic baseline不可能同时具有二阶深度。

---

## 4. fixed `2671` 的两个 `p^2` lifts 也显式不同

`P'(K)=12K-36`，在 (3.2) 为 `2671`-进 unit，因此 `P=0` 的 root唯一提升。

计算得到

\[
\boxed{
K_P\equiv2825391\pmod{2671^2}.}
\tag{4.1}
\]

而 linear root `5K-36=0` 的唯一提升为

\[
\boxed{
K_F\equiv5707400\pmod{2671^2}.}
\tag{4.2}
\]

两者都回到

\[
2144\pmod{2671},
\]
但

\[
\boxed{K_P\not\equiv K_F\pmod{2671^2}.}
\tag{4.3}
\]

事实上

\[
\frac{K_P-K_F}{2671}
\equiv1592\not\equiv0\pmod{2671}.
\tag{4.4}
\]

这与 Bezout valuation (3.6) 完全一致。

---

## 5. normalized first digits被 Bezout精确固定

`2671` 例还可以读取两个 root branches分离后的 first normalized digit。

若沿 target quadratic Hensel branch

\[
P\equiv0\pmod{2671^2},
\]
则把 (3.3) 除以 `2671` 并模 `2671`：

\[
-(30K+36)\frac{F_*}{2671}\equiv1\pmod{2671}.
\]

在 first root上 `30K+36=252`，所以

\[
\boxed{
\frac{F_*}{2671}
\equiv-252^{-1}
\equiv2618\pmod{2671}.}
\tag{5.1}
\]

相反，若沿 linear branch

\[
F_*\equiv0\pmod{2671^2},
\]
则

\[
25\frac P{2671}\equiv1\pmod{2671},
\]
即

\[
\boxed{
\frac P{2671}\equiv25^{-1}\equiv2030\pmod{2671}.}
\tag{5.2}
\]

所以二阶分叉不仅存在，而且两个 normalized transverse digits 都是固定 nonzero units。

---

## 6. 对 fixed exceptions 的正确解释

此前 `7` 与 `2671` 被称为 fixed exceptions，是因为普通 first-layer next-depth argument在这些 primes上失去 unit coefficient。

本文说明它们都**不是** singular Hensel exceptions：

\[
\boxed{
\text{quadratic target root与 exceptional linear root均为 simple，且只在 first layer相交}.}
\tag{6.1}
\]

因此：

- fixed `7` 中，`F_7` 在真正 extra-resultant branch上精确只有一层；
- fixed `2671` 中，若 target baseline `h>=2`，`F_*` 也精确只有一层；若 `F_*` 自己继续深化，则 target baseline只能是 `h=1`；
- 任意更高 companion depth必须来自 `R_+`、`U`、`alpha` 等 normalized terms之间的 cancellation，而不能解释成 exceptional root本身继续跟随。

这把两个 fixed branches从“可能的额外 Hensel tree”降级为“first-layer transverse collision + higher normalized cancellation”。

---

## 7. 当前 fixed-prime frontier

fixed exceptions现在具有统一结构：

\[
\boxed{
\begin{array}{c|c|c|c}
 p&\text{quadratic carrier}&\text{linear exception}&\text{intersection depth}\\ \hline
7&R_{PD}&36D-11N&1\\
2671&P&5K-36&1
\end{array}}
\tag{7.1}
\]

所以后续不应继续机械提升这两个 linear roots。真正的新目标应是对它们的 normalized cancellation构造 natural corrected carrier，或者把这种 cancellation与 `Lambda_tail` 的 exact resonance depth联立。

A2 仍为 `待证`。

# A2 source actual/conjugate gate 与 numerator residual 的 exact bridge

> **依赖：** `spontaneous-source-common-parity.md`、`spontaneous-source-numerator-length.md`、`spontaneous-source-sheet-collision.md`、`spontaneous-source-prefix-simple.md`。
>
> **严格状态：**本文把 source actual gate `K_src(H,E,F)`、共轭 square-sheet gate `K_src(-H-2F,E,F)` 与 pure numerator/length residual `R_src(e,M)` 放进同一个 integer congruence modulo source prefix linear form。对 source half-depth `p^h|D_src`，得到截断赋值律 `v(R_src)=v(K)+v(K^vee)`（截断到 `h`）。因此不发生 sheet collision时，`R_src` 与真实 `K_src/C_src` 读取完全相同的 half-depth；额外 valuation只能来自已经被固定 quartic控制的 conjugate-sheet collision。本文不排除 simple collision roots，也不宣称 A2 closure。

---

## 1. actual 与 conjugate denominator defects

沿用

\[
F=5^{M-1},
\qquad
E=2^{M-1},
\qquad
S=EF=10^{M-1},
\]

\[
x=\frac{H+F}{10F}.
\tag{1.1}
\]

定义 actual source-common natural gate

\[
\boxed{K:=\mathcal K_{\rm src}(H,E,F).}
\tag{1.2}
\]

source square relation的共轭 sheet是 `x -> -x`。保持 `E,F` 不变时，唯一对应的 defect substitution为

\[
\frac{H^\vee+F}{10F}
=-\frac{H+F}{10F},
\]
即

\[
\boxed{H^\vee=-H-2F.}
\tag{1.3}
\]

因此定义

\[
\boxed{
K^\vee
:=\mathcal K_{\rm src}(-H-2F,E,F).}
\tag{1.4}
\]

由 `K_src` 的 scaling identity：

\[
\boxed{
K=100000E^2F^6\mathcal C_{\rm src}(x,\tau),}
\tag{1.5}
\]

\[
\boxed{
K^\vee=100000E^2F^6\mathcal C_{\rm src}(-x,\tau),}
\tag{1.6}
\]

其中

\[
\tau=(10EF)^{-1}.
\]

---

## 2. source prefix equation 的 primitive linear form

`spontaneous-source-prefix-simple.md` 已有

\[
D_{\rm src}
=\frac{9E^2}{4}(5F^2+18FH+9H^2)+9EF e.
\]

提出固定 `9E/4`，定义 primitive linear form

\[
\boxed{
D_{\rm lin}
:=E(5F^2+18FH+9H^2)+4Fe.}
\tag{2.1}
\]

则

\[
\boxed{
D_{\rm src}=\frac{9E}{4}D_{\rm lin}.}
\tag{2.2}
\]

对 genuine non-`3` source prime，`9E/4` 是 unit，因此

\[
\boxed{v_p(D_{\rm lin})=v_p(D_{\rm src}).}
\tag{2.3}
\]

---

## 3. normalized product identity

`spontaneous-source-sheet-collision.md` 已证明在 quotient ring

\[
225x^2-y=0
\]
中：

\[
\boxed{
\mathcal R_{\rm src}^{(y)}
=5625^2\mathcal C_{\rm src}(x,\tau)
\mathcal C_{\rm src}(-x,\tau).}
\tag{3.1}
\]

而 source prefix relation正是

\[
225x^2-y
=\frac{D_{\rm src}}{9S^2}
=\frac{D_{\rm lin}}{4FS}.
\tag{3.2}
\]

同时 pure numerator integer residual满足

\[
\boxed{
\mathcal R_{\rm src}^{(y)}
=\frac{\mathscr R_{\rm src}}{100S^6}.}
\tag{3.3}
\]

所以乘回所有 `2,3,5,E,F` scales后，(3.1) 在整数多项式环中产生一个 modulo `D_lin` 的 exact product bridge。

---

## 4. `已严格完成`：integer congruence

把 (1.5)–(1.6)、(3.3) 代入 (3.1)；使用

\[
\frac{10^8}{5625^2}=\frac{256}{81},
\]
得到 source slice上的 equality

\[
81E^2KK^\vee=256F^6\mathscr R_{\rm src}.
\]

由于 source slice由 linear equation `D_lin=0` 定义，这等价于 polynomial congruence

\[
\boxed{
81E^2KK^\vee
\equiv
256F^6\mathscr R_{\rm src}
\pmod{D_{\rm lin}}.}
\tag{4.1}
\]

也就是说存在

\[
\mathcal L_{\rm conj}\in\mathbf Z[H,e,E,F]
\]
使

\[
81E^2KK^\vee
-256F^6\mathscr R_{\rm src}
=D_{\rm lin}\mathcal L_{\rm conj}.
\tag{4.2}
\]

`check_a2_spontaneous_source_conjugate_bridge.py` 对完整 expanded integers直接做 exact polynomial division验证 (4.2)，无需记录 90-term quotient本身。

---

## 5. source half-depth 下的截断 valuation law

固定 genuine source prime，且

\[
p^h\mid D_{\rm src}.
\]

由 (2.3)：

\[
p^h\mid D_{\rm lin}.
\]

又

\[
p\nmid2\cdot3\cdot5EF,
\]
所以 (4.1) 模 `p^h` 是两个 unit multiples 的 congruence：

\[
KK^\vee
\equiv u\,\mathscr R_{\rm src}
\pmod{p^h},
\qquad u\in\mathbf Z_p^\times.
\tag{5.1}
\]

因此逐 prime-power精确有

\[
\boxed{
\min\{v_p(\mathscr R_{\rm src}),h\}
=
\min\{v_p(K)+v_p(K^\vee),h\}.}
\tag{5.2}
\]

这不是只在 first layer成立，而是 source prefix half-depth内的完整 truncated law。

---

## 6. generic 单-sheet时 `R_src` 与 actual common gate完全同步

若共轭 gate为 unit：

\[
p\nmid K^\vee,
\tag{6.1}
\]
则 (5.2) 立即简化为

\[
\boxed{
\min\{v_p(\mathscr R_{\rm src}),h\}
=
\min\{v_p(K),h\}.}
\tag{6.2}
\]

对 genuine odd source prime，`K` 与 `C_src`只差 `2,5,E,F` units，因此

\[
\boxed{
\min\{v_p(\mathscr R_{\rm src}),h\}
=
\min\{v_p(\mathcal C_{\rm src}),h\}.}
\tag{6.3}
\]

再与 `spontaneous-source-depth-transfer.md` 合并：

\[
\boxed{
\min\{v_p(\mathscr R_{\rm src}),h\}
=
\min\{v_p(\widehat{\mathcal T}_2),h\}
=
\min\{v_p(G_{\rm sp}),h\}}
\tag{6.4}
\]

在 generic noncollision source primary上成立。

所以 pure numerator/length residual不再只是一个 necessary resultant：它精确读取真实 common depth，直到 source half-depth。

---

## 7. 唯一 correction：conjugate sheet collision

若

\[
p\mid K^\vee
\]
且 actual gate也命中，则两个 source square sheets同时 contact。`spontaneous-source-sheet-collision.md` 已证明这等价于

\[
\mathcal E=\mathcal O=0
\]
并被固定 quartic

\[
\mathcal Q_{\rm sheet}(y)=0
\]
控制。

而该 collision locus：

- 真实 endpoint interval无 Archimedean root；
- genuine non-`3` inert singular Hensel tree为空；
- 剩余只能是 simple fixed-quartic synchronization。

因此 (5.2) 中 `v_p(K^vee)` 是**唯一**可能使 `R_src` 比 actual `C_src` 多收 depth 的 correction；它不携带新的 source ratio或奇异分叉。

---

## 8. 与两个 mod-8 orientations 的关系

已有

\[
\widehat K_{\rm src}=K/2^8\equiv3\pmod8,
\]
而

\[
\mathscr R_{\rm src}\equiv1\pmod8.
\]

(4.1) 解释了两者为何并不矛盾：`R_src` 是 actual gate和共轭 gate的 source-sheet norm，而不是 actual gate本身。

形式上，在 source slice上：

\[
\boxed{
\text{numerator/length norm}
\sim
\text{actual gate}\times\text{conjugate gate}.}
\tag{8.1}
\]

所以 `1 mod 8` orientation正是两张 sheet parity合并后的结果。若要从全局 parity进一步逼 actual source common prime，必须控制 conjugate sheet 的 inert allocation；本文已经把这一 correction压到固定 simple quartic，避免把整个 `R_src` 错误地直接等同于 `K_src`。

---

## 9. 更新后的 source common ledger

source pool现在可以用四个对象完整记账：

\[
\boxed{
\begin{array}{c|c}
\mathcal S_{\rm src}&\text{source primary depth }2h\\
D_{\rm lin}&\text{source prefix half-depth }h\\
K&\text{actual source→common gate}\\
K^\vee&\text{conjugate-sheet correction}\\
\mathscr R_{\rm src}&\text{actual×conjugate numerator norm}
\end{array}}
\]

并有三条 exact depth bridge：

\[
81\mathcal O_{\rm sp}=400TD_{\rm src}^2-81A^2\mathcal S_{\rm src},
\]

\[
\min(v_p(\widehat T_2),h)=\min(v_p(K),h),
\]

\[
\min(v_p(\mathscr R_{\rm src}),h)=\min(v_p(K)+v_p(K^\vee),h).
\]

这已经把 source local algebra基本封装完成。真正开放项只剩 simple actual/conjugate decimal orbit和 global inert parity allocation。
# A2 source→common 的共轭 square-sheet collision

> **依赖：** `spontaneous-source-numerator-length.md`、`spontaneous-source-common-gate.md`。
>
> **严格状态：**source first layer满足 `r^2=y`，真实 sheet为 `r=15x`。`spontaneous-source-numerator-length.md` 把 `C_src` 分成 `E+120rO`，因此 pure numerator/length residual正是两个共轭 source sheets 的乘积。本文审计两个 sheet同时命中 `C_src=0` 的 collision locus：它降成一个固定 quartic；在真实 numerator interval没有实根，且 genuine non-`3` inert singular Hensel tree为空。simple modular sheet-collisions仍可能存在，因此本文不宣称 A2 closure。

---

## 1. 两个 source square sheets

source first-layer relation为

\[
225x^2=y.
\]

令

\[
\boxed{r:=15x,\qquad r^2=y.}
\tag{1.1}
\]

已有 exact even/odd decomposition

\[
\boxed{
5625\mathcal C_{\rm src}(x,\tau)
=\mathcal E(y,\tau)+120r\mathcal O(y,\tau),}
\tag{1.2}
\]

其中

\[
\begin{aligned}
\mathcal E={}&11000\tau^2y+9900000\tau^2
+84609\tau y^2-3240000\tau y-29160000\tau\\
&-19404y^3-10836y^2+1474200y,
\end{aligned}
\tag{1.3}
\]

\[
\mathcal O=
5500\tau^2-2691\tau y-16200\tau
+296y^2+1764y-8100.
\tag{1.4}
\]

在共轭 sheet `r -> -r`，即 `x -> -x`：

\[
\boxed{
5625\mathcal C_{\rm src}(-x,\tau)
=\mathcal E-120r\mathcal O.}
\tag{1.5}
\]

所以

\[
\boxed{
\mathcal R_{\rm src}^{(y)}
=5625^2\mathcal C_{\rm src}(x,\tau)
\mathcal C_{\rm src}(-x,\tau)
}
\tag{1.6}
\]

在 quotient ring `225x^2-y=0` 中精确成立。这就是此前

\[
\mathcal R_{\rm src}^{(y)}=\mathcal E^2-14400y\mathcal O^2
\]
的几何意义。

---

## 2. 双-sheet collision 等价于 `E=O=0`

对 genuine odd source prime，`2,3,5,r` 都是单位。若同时

\[
p\mid C_{\rm src}(x,\tau),
\qquad
p\mid C_{\rm src}(-x,\tau),
\]
则由 (1.2)、(1.5)：

\[
\boxed{
p\mid\mathcal E,\qquad p\mid\mathcal O.}
\tag{2.1}
\]

反向也显然成立。因此两个 square sheets 的 first-layer collision精确由 `(E,O)` 的平面交控制。

---

## 3. `已严格完成`：collision消成一个固定 quartic

对 `tau` 求 resultant：

\[
\boxed{
\operatorname{Res}_{\tau}(\mathcal E,\mathcal O)
=-550000(y+9)^2\mathcal Q_{\rm sheet}(y),}
\tag{3.1}
\]

其中

\[
\boxed{
\begin{aligned}
\mathcal Q_{\rm sheet}(y)
={}&2461063649y^4+234628417800y^3\\
&+4390818840000y^2+17723448000000y\\
&-144342000000000.
\end{aligned}}
\tag{3.2}
\]

反向消去 `y` 也得到固定 decimal-length quartic：

\[
\boxed{
\operatorname{Res}_{y}(\mathcal E,\mathcal O)
=-1000000\tau^2\mathcal Q_{\tau}(\tau),}
\tag{3.3}
\]

\[
\boxed{
\begin{aligned}
\mathcal Q_{\tau}(	au)
={}&7444717538225\tau^4
+119322760549410\tau^3\\
&+292869540803250\tau^2
+743568561885024\tau\\
&-87085495164087.
\end{aligned}}
\tag{3.4}
\]

所以双-sheet collision没有新的 source ratio自由度；它是固定 `(y,tau)` algebraic intersection。

---

## 4. `y=-9` 因子不属于 genuine non-3 inert decimal collision

在 `y=-9`：

\[
\boxed{
\mathcal E=81\tau(121000\tau+84609),}
\tag{4.1}
\]

\[
\boxed{
\mathcal O=11\tau(500\tau+729).}
\tag{4.2}
\]

两个非零线性 factors 的 resultant为

\[
\boxed{45904500=2^2\cdot3^2\cdot5^3\cdot101^2.}
\tag{4.3}
\]

因此对 genuine non-`3` inert prime，两个式子共同为零只能来自

\[
\tau=0,
\]
但真实

\[
\tau=10^{-M}
\]
永远是单位。故 (3.1) 的 `(y+9)^2` 是非 decimal boundary，不属于本文的真实 collision。

---

## 5. 真实 endpoint interval 没有 Archimedean collision

真实 numerator phase满足

\[
249/250<y<1.
\]

`Q_sheet` 在正半轴严格递增，因为 derivative的全部 coefficient为正：

\[
\mathcal Q_{\rm sheet}'(y)>0
\qquad(y>0).
\tag{5.1}
\]

而

\[
\boxed{
\mathcal Q_{\rm sheet}(1)=-121990643678551<0.}
\tag{5.2}
\]

因此整个真实 interval上

\[
\boxed{
\mathcal Q_{\rm sheet}(y)<0.}
\tag{5.3}
\]

没有实数 sheet collision；任何 collision只能来自 modular wrapping。

---

## 6. singular bad-prime set

quartic的整数判别式为

\[
\boxed{
\operatorname{Disc}(\mathcal Q_{\rm sheet})
= -2^{32}3^{32}5^{25}101^7\cdot113\cdot7437536446892971.}
\tag{6.1}
\]

其中

\[
113\equiv1\pmod4,
\qquad
101\equiv1\pmod4,
\]
且

\[
\boxed{7437536446892971\equiv3\pmod4}
\tag{6.2}
\]
为素数。

另外 quartic leading coefficient

\[
2461063649=11^2\cdot1609\cdot12641,
\]
其中 `1609,12641` 都为 `1 mod4`。resultant content `550000` 还含一份 `11`。

所以 genuine non-`3` inert singular/degree-drop audit只需

\[
\boxed{p=11,\qquad p=7437536446892971.}
\tag{6.3}
\]

---

## 7. `p=11`：唯一 singular point是 `tau=0` boundary

完整枚举 `F_11^2` 中 `(E,O)=(0,0)` 得

\[
\boxed{
(y,\tau,J)=
(2,0,0),\quad(3,3,6),\quad(5,9,1),}
\tag{7.1}
\]

其中

\[
J:=\det\frac{\partial(\mathcal E,\mathcal O)}{\partial(y,\tau)}.
\]

唯一 singular intersection `(2,0)` 满足 `tau=0`，不是 decimal phase；其余两点 Jacobian均为单位。因此

\[
\boxed{p=11\text{ 没有 genuine singular sheet-collision branch}.}
\tag{7.2}
\]

simple `11` collision states本身没有被本文排除。

---

## 8. 大 inert singular prime不能升到 `p^2`

令

\[
\boxed{p=7437536446892971.}
\]

此时

\[
\gcd(\mathcal Q_{\rm sheet},\mathcal Q_{\rm sheet}')
=y+2367909658823161
\pmod p,
\]
所以唯一 repeated `y` residue为

\[
\boxed{y_0=5069626788069810.}
\tag{8.1}
\]

代回 `(E,O)`，共同 `tau` root唯一：

\[
\boxed{\tau_0=1327194327136915.}
\tag{8.2}
\]

这是 finite unit state，并且 `y_0` 本身是模 `p` 的平方，所以不能靠 source square-sheet condition直接排除。

在该点，Jacobian两行模 `p` 为

\[
(4769546899604225,\ 5300490912652323),
\]

\[
(2429430622649786,\ 4767246607889802).
\tag{8.3}
\]

第二行是第一行的

\[
\lambda=6415545761503029
\]
倍，因此 rank为 `1`。

取最小非负 representatives，normalized carries为

\[
\frac{\mathcal E(y_0,\tau_0)}p
\equiv1149464242486028,
\]

\[
\frac{\mathcal O(y_0,\tau_0)}p
\equiv2576181903398455
\pmod p.
\tag{8.4}
\]

若存在 `p^2` lift，增广线性化必须满足同一 row relation。但 compatibility residual为

\[
\boxed{
\lambda\cdot1149464242486028
-2576181903398455
\equiv762004648349653\not\equiv0\pmod p.}
\tag{8.5}
\]

因此

\[
\boxed{
\text{该唯一 genuine singular sheet collision无 }p^2\text{ lift}.}
\tag{8.6}
\]

---

## 9. 结论：共轭 sheet只留下 simple fixed-quartic synchronization

综合 §§6–8：

\[
\boxed{
\text{source conjugate-sheet collision不存在 surviving singular Hensel tree}.}
\tag{9.1}
\]

所以对 genuine source prime，如果

\[
p\nmid\mathcal Q_{\rm sheet}(y),
\]
共轭 gate `C_src(-x,tau)` 为单位，于是由 (1.6)：

\[
\boxed{
v_p(\mathcal R_{\rm src}^{(y)})
=v_p(\mathcal C_{\rm src}(x,\tau)).}
\tag{9.2}
\]

若命中 `Q_sheet`，则两张 source square sheets同时接触；本文证明它最多沿 simple fixed-quartic Hensel synchronization传播，不会产生新的 singular branching。

因此 numerator/length residual `R_src` 与真实 source-common gate `C_src` 的 valuation差异已经被局限到一个固定 simple collision locus。后续 parity ledger可以把它单独列为 `sheet-collision correction`，而无需再次引入 source ratio或第三块变量。
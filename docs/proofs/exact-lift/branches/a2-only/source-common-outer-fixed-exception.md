# A2 source-common / outer-pair / descendant-common reuse 塌缩到唯一 fixed prime

> **依赖：** [`outer-cofactor-reuse-gate.md`](outer-cofactor-reuse-gate.md)；`spontaneous-source-parity-common-gcd.md`、`spontaneous-source-parity-collision-gate.md`（历史正文已整合进 source/auxiliary ledgers）；`spontaneous-crt-universal-descendant-cubic.md`（整合于 `crt-descent-ledger.md`）。
>
> **严格状态：**危险 `Z≡1 (mod4)` orientation 中，两个 outer rational-root cofactors `Xi_-,Xi_+` 各自都需要 non-`3` inert supplier。若同一 genuine source-common prime还试图同时支付这两个 outer parity并复用 descendant common pair，则 source-common linear sheet `18K-55=0`、outer-pair cubic `G_pm=0` 与 universal descendant cubic `E_63=0` 必须同时成立。本文把三个 moving 条件完全消元：全部非 `3` inert support塌成唯一 fixed prime
> \[
> p_\star=740759498168792879433565547.
> \]
> 该 prime 在 `F_{p_*}` 中确有真实公共 `zeta` 根，并同时通过 source-square character `(55/p_*)=1` 与旧 terminal character `(-26/p_*)=-1`，因此本文**不排除**该 fixed exception；A2 仍为 `待证`。

---

## 1. source-common 把 `K` 固定到一张线性 sheet

source parity 的两个 primitive carriers 满足 exact identity

\[
55\mathscr B_W-K^2\mathscr D_W
=c_u^2(18K-55)^2.
\tag{1.1}
\]

对 genuine common prime

\[
p\mid\mathscr B_W,
\qquad
p\mid\mathscr D_W,
\qquad
p\nmid55Kc_u,
\tag{1.2}
\]

因此

\[
\boxed{18K-55\equiv0\pmod p.}
\tag{1.3}
\]

即

\[
\boxed{K\equiv\frac{55}{18}\pmod p.}
\tag{1.4}
\]

这正是 canonical source-common old pool 的 moving linear sheet。

---

## 2. 同一 prime 支付两个 outer cofactors 时必须命中 `G_pm`

`outer-cofactor-reuse-gate.md` 已证明，若 genuine non-`3` inert prime 同时满足

\[
p\mid\Xi_-,
\qquad
p\mid\Xi_+,
\tag{2.1}
\]

则令

\[
\zeta:=a_3/T,
\]

必有

\[
\boxed{\mathcal G_{\pm}(K,\zeta)\equiv0\pmod p,}
\tag{2.2}
\]

其中

\[
\boxed{
\begin{aligned}
\mathcal G_{\pm}(K,\zeta):={}&
-K^2\zeta^3-3K^2\zeta^2
+12K\zeta^3+60K\zeta^2\\
&+96K\zeta+64K
-28\zeta^3-156\zeta^2-288\zeta-192.
\end{aligned}}
\tag{2.3}
\]

把 source line (1.4) 代入并清分母，得到 primitive cubic

\[
\boxed{
G_S(\zeta)
=217\zeta^3+219\zeta^2-1728\zeta-1152.}
\tag{2.4}
\]

所以 source-common + shared outer reuse 已经不再含 `K` 自由度。

---

## 3. 再复用 descendant common 后只剩一个 fixed resultant

若同一 prime 同时还属于 fully primitive descendant common support，则 universal descendant compatibility 给

\[
\boxed{\mathcal E_{63}(K,\zeta)\equiv0\pmod p.}
\tag{3.1}
\]

沿用 canonical cubic

\[
\begin{aligned}
\mathcal E_{63}={}&
98304U^3A_0\zeta^3
-1024U^2B_2\zeta^2\\
&+32UL_KB_1\zeta-L_K^2B_0,
\end{aligned}
\tag{3.2}
\]

其中

\[
U=2K-9,
\qquad
L_K=K^2-576K+1296,
\]

\[
A_0=5K^2+144K-324,
\]

\[
B_2=381K^4-78048K^3-277520K^2+2392704K-3074112,
\]

\[
B_1=189K^4-126720K^3+132784K^2+1359360K-2218752,
\]

\[
B_0=63K^4-54432K^3+136672K^2+239616K-539136.
\]

代入 `K=55/18` 后清分母得到另一个 primitive cubic

\[
\boxed{
\begin{aligned}
E_S(\zeta)={}&
-472107612503015424\zeta^3\\
&+5728570300274245632\zeta^2\\
&-21821587044824975616\zeta\\
&+19816509935574590969.
\end{aligned}}
\tag{3.3}
\]

现在对 (2.4),(3.3) 关于 `zeta` 求 exact resultant：

\[
\boxed{
\begin{aligned}
R_S
&:=\left|\operatorname{Res}_\zeta(G_S,E_S)\right|\\
&=377519852626542769621117894805749147492566419200897716610331068879.
\end{aligned}}
\tag{3.4}
\]

其完整平方自由分解为

\[
\boxed{
\begin{aligned}
R_S={}&41\cdot64217\cdot72238473017\\
&\cdot2679539349324345019093\\
&\cdot740759498168792879433565547.
\end{aligned}}
\tag{3.5}
\]

五个因子均为素数，且模 `4` 分别为

\[
1,1,1,1,3.
\tag{3.6}
\]

因此 genuine inert prime 的可能性被严格压成唯一一枚：

\[
\boxed{
p=p_\star:=740759498168792879433565547.}
\tag{3.7}
\]

这不是“大素数大概不可能”的高度启发，而是完整 exact resultant 的 prime-support classification。

---

## 4. `p_*` 是真实 `F_p` 交点，不是扩域伪根

像 fixed `7` 的 degree-30 eliminant 所示，`p|resultant` 本身不能保证真实 decimal residue `zeta∈F_p` 存在。因此必须直接算

\[
\gcd_{\mathbf F_{p_\star}[\zeta]}(G_S,E_S).
\]

checker 得到一次 gcd

\[
\boxed{
\gcd(G_S,E_S)
=\zeta-121854543490110025177920950
\quad\text{in }\mathbf F_{p_\star}[\zeta].}
\tag{4.1}
\]

所以确有真实 first-layer residue

\[
\boxed{
\zeta_\star
=121854543490110025177920950
\pmod{p_\star}.}
\tag{4.2}
\]

因此不能像 fixed `7` outer-pair shadow那样通过 `F_p` root audit直接删除它。

---

## 5. 已知 source / terminal characters 也没有杀掉它

source common 本身还必须满足

\[
\mathscr D_W=55z^2-49c_u^2\equiv0\pmod p.
\]

在 genuine sector `p∤c_u`，因此必要条件为

\[
\boxed{\left(\frac{55}{p}\right)=1.}
\tag{5.1}
\]

对 `p_*` 直接计算：

\[
\boxed{\left(\frac{55}{p_\star}\right)=1.}
\tag{5.2}
\]

所以 source-square character兼容。

历史 terminal descendant overdepth 还留下固定 character

\[
\left(\frac{-26}{p}\right)=-1.
\tag{5.3}
\]

而

\[
\boxed{\left(\frac{-26}{p_\star}\right)=-1.}
\tag{5.4}
\]

它同样兼容。故这里不能靠重复已有 quadratic character宣布矛盾。

---

## 6. fixed intersection 是 first-layer transverse，但仍未空

(3.5) 中 `p_*` 只出现一次：

\[
\boxed{v_{p_\star}(R_S)=1.}
\tag{6.1}
\]

因此在 exact source sheet `18K-55=0` 上，两个 reduced cubics `G_S,E_S` 不可能同时形成一个自由的共同二阶 Hensel tree；若 source line 自身也提升到相应深度，则至少一张 cubic 必停在第一层。

这很有用，但还不能删除 `p_*` 的**一层** odd common payment；而 parity账恰恰允许 squarefree first layer。因此本文严格保留

\[
\boxed{p_\star\text{ 为唯一 source-common shared-reuse fixed exception}.}
\tag{6.2}
\]

---

## 7. 更新后的 `Z=1` old-pool frontier

结合 `outer-cofactor-reuse-gate.md`：

1. fixed height `7` 与 fixed targets `31/179` 都不能同时支付 `Xi_-`,`Xi_+` 两边；
2. source-common moving family若同时支付两边并复用 descendant common，已完全塌成唯一 fixed prime `p_*`；
3. `p_*` 通过当前 source/terminal quadratic characters，尚需新的 decimal/Hensel 或 natural-representative input；
4. 除 `p_*` 外，真正仍未分类的是 genuinely endpoint-external descendant-common kernel。

所以 old-pool 的 shared-reuse 问题已经从

\[
\text{fixed }7/31/179+\text{moving source-common family}
\]

压成

\[
\boxed{\text{single fixed }p_\star+\text{genuine external common kernel}.}
\]

A2 仍为 `待证`。

---

## 8. verification

```bash
uv run python scripts/exact-lift/a2-only/research-checks/crt-descent/check_a2_source_common_outer_fixed_exception.py
```

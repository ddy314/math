# A2 fixed `7` extra-depth target 的 two-orbit Hensel rigidity

> **依赖：** `spontaneous-height-equal-depth-fixed7-audit.md`、`spontaneous-height-equal-depth-target-ladder.md`。
>
> **严格状态：**前一 fixed-7 audit把 extra-resultant branch压成 `M≡1,5 (mod 6)` 与四个 mod-`7` states。本文证明这些 states 全部为 simple Hensel roots：exceptional quadratic root `K≡2 (mod 7)` 唯一提升；`U=DK-N` 随后唯一确定 `D mod 7^h`，prefix identity唯一确定 `A mod 7^h`；而每个 surviving phase 的两个 `B mod 7` roots 对 pure-prefix height polynomial 的导数均为 `7`-进单位，因此各自唯一提升到任意 `7^h`。所以对每个允许的长度相位与 fixed baseline depth `h`，prefix target只剩两条 canonical 7-adic orbits，而不是指数增长的 residue tree。本文不证明两条 orbits 不存在，不关闭 A2。

---

## 1. exceptional `K` root 是 simple

沿用

\[
\mathcal P_{\omega H}(K)=6K^2-36K+55.
\]

fixed-7 extra-depth branch已经强迫

\[
\boxed{K\equiv2\pmod7.}
\tag{1.1}
\]

导数为

\[
\mathcal P'_{\omega H}(K)=12K-36.
\]

在 `K=2`：

\[
\boxed{
\mathcal P'_{\omega H}(2)
=-12\equiv2\not\equiv0\pmod7.}
\tag{1.2}
\]

所以 `K≡2` 是 simple root。

由 Hensel lemma，对每个

\[
r\ge1
\]
存在唯一 residue

\[
\boxed{\kappa_r\pmod{7^r}}
\tag{1.3}
\]
满足

\[
\kappa_r\equiv2\pmod7,
\qquad
\mathcal P_{\omega H}(\kappa_r)\equiv0\pmod{7^r}.
\tag{1.4}
\]

例如第一层提升为

\[
\boxed{\kappa_2\equiv23\pmod{49}.}
\tag{1.5}
\]

若 target baseline depth为

\[
v_7(\mathcal P_{\omega H}(K))=h,
\]
则必有

\[
\boxed{K\equiv\kappa_h\pmod{7^h},}
\tag{1.6}
\]

且 exact depth `h` 进一步要求 `K` 不落入下一层 root class `kappa_{h+1} mod 7^{h+1}`。

---

## 2. `D` 与 `A` 随 `K` 唯一恢复

目标还有

\[
U=DK-N=qW_q,
\qquad
v_7(U)=h.
\]

由于 `K≡2 (mod 7)` 是 unit：

\[
DK\equiv N\pmod{7^h}
\]
唯一给出

\[
\boxed{
D\equiv NK^{-1}\pmod{7^h}.}
\tag{2.1}
\]

在 `h=1` 时恢复前一文件的

\[
D\equiv4N\pmod7.
\]

在 `h=2`、`K≡23 (mod 49)` 时

\[
23^{-1}\equiv32\pmod{49},
\]
所以

\[
\boxed{D\equiv32N\pmod{49}.}
\tag{2.2}
\]

原 prefix identity

\[
K=9N+10A
\]
中 `10` 对 `7` 为 unit，因此

\[
\boxed{
A\equiv(K-9N)10^{-1}\pmod{7^h}.}
\tag{2.3}
\]

所以给定真实 `M` 与 baseline depth `h`，`K,D,A mod 7^h` 全部不再分支。

---

## 3. `B` 的 target equation

定义

\[
\boxed{
F_h(B)
:=B^2K^2+(B+2N)^2
\left[\left(\frac{9B}{2}\right)^2+A^2\right].}
\tag{3.1}
\]

这就是

\[
\mathscr H_{\omega H}^{\rm pref}
\]
作为 `B` 的 polynomial。

真正 target 满足

\[
v_7(\mathscr H_{\omega H}^{\rm pref})=h,
\]
故至少

\[
F_h(B)\equiv0\pmod{7^h}.
\tag{3.2}
\]

其 coefficients中的 `N,K,A` 按 §§1–2 已在每层唯一确定。

---

## 4. 四个 mod-`7` roots 全部 simple

前一 finite audit得到：

### `M≡1 (mod 6)`

\[
N\equiv3,
\quad A\equiv1,
\quad B\equiv2,4\pmod7.
\]

对应的 mod-`7` polynomial为

\[
F(B)
=(B-2)(B+3)(B^2-3B+1).
\]

直接求导得到

\[
\boxed{
F'(2)\equiv2,
\qquad
F'(4)\equiv3
\pmod7.}
\tag{4.1}
\]

### `M≡5 (mod 6)`

\[
N\equiv5,
\quad A\equiv2,
\quad B\equiv1,3\pmod7,
\]

且

\[
F(B)
=(B-3)(B-1)(B^2+3B-2).
\]

有

\[
\boxed{
F'(1)\equiv3,
\qquad
F'(3)\equiv4
\pmod7.}
\tag{4.2}
\]

所以四个 surviving roots 全部满足

\[
\boxed{7\nmid F'(B_0).}
\tag{4.3}
\]

---

## 5. 每个 phase 只有两条唯一 `7`-adic B-orbits

由 (4.3) 与 Hensel lemma，每个 mod-`7` root都唯一提升到任意

\[
7^r,
\qquad r\ge1.
\]

因此：

### `M≡1 (mod 6)`

存在唯一两条 compatible residue chains

\[
\boxed{
B_{2,r}\equiv2\pmod7,
\qquad
B_{4,r}\equiv4\pmod7,}
\tag{5.1}
\]

满足

\[
F_h(B_{2,r})\equiv
F_h(B_{4,r})\equiv0\pmod{7^r}.
\]

### `M≡5 (mod 6)`

同样只有

\[
\boxed{
B_{1,r}\equiv1\pmod7,
\qquad
B_{3,r}\equiv3\pmod7.}
\tag{5.2}
\]

两条 compatible chains。

因此对 fixed real length `M` 和 baseline depth `h`：

\[
\boxed{
\text{fixed-7 extra-depth prefix target至多有两条 }7\text{-adic residue orbits}.}
\tag{5.3}
\]

这里的“至多”保留 exact valuation `h`、真实 digit window及其它 source 条件可能继续删除某条 orbit 的可能性。

---

## 6. mod `49` sanity check

`K` 的 exceptional lift为

\[
K\equiv23\pmod{49}.
\]

逐真实 `M mod 42` 相位代入 `N=10^M mod 49`、由 (2.3) 恢复 `A` 后，每个满足

\[
M\equiv1,5\pmod6
\]
的相位确实恰好出现两个 admissible `B mod 49` roots；其它 phase 没有从 mod-`7` elimination中复活。

这一有限检查只作为 Hensel uniqueness 的 sanity certificate；一般 `7^h` 结论来自 simple-root theorem，而非枚举。

---

## 7. fixed-7 frontier

fixed `7` extra-depth target现在具有 deterministic prefix pipeline：

\[
\boxed{
M
\Longrightarrow
N=10^M
\Longrightarrow
K=\kappa_h
\Longrightarrow
D,A
\Longrightarrow
\text{两条 }B\text{-Hensel orbits}.}
\tag{7.1}
\]

所以 fixed `7` branch 已不再有 moving residue-tree complexity。真正剩余的自由是：

1. 两条 simple orbit中是否有一条能同时满足 full tail condition
   \[
   v_7(\Lambda_{\rm tail})=\rho_7>0;
   \]
2. exact valuation `v_7(P)=h`、`v_7(H_pref)=h` 后的下一 digit是否与 residual companion oversaturation兼容；
3. 真实 decimal endpoint interval是否最终排除某条 lifted orbit。

后续若继续 fixed `7`，应该直接沿这两条 Hensel chains计算 normalized next-digit equations，而无需再枚举全部 residues。

A2 仍为 `待证`。
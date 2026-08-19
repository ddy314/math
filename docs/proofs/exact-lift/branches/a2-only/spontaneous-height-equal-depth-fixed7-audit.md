# A2 equal-depth target 的 fixed `7` residue audit

> **依赖：** `spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-oversaturation-depth-ledger.md`、`spontaneous-height-content-oversaturation.md`、`endpoint-lattice.md`。
>
> **严格状态：**前一 target-ladder 文件证明：若 deep equal-depth target `p` 使 source-prefix resultant `R_PD` 的 p-depth超过 baseline `h`，则唯一可能是 `p=7`，并且必须有 `D≡4N`、`K≡2 (mod 7)`。本文把真正 target 还必须满足的 pure-prefix height congruence `H_pref=B^2K^2+Q^2N_0≡0 (mod 7)` 代回原始 decimal definitions，完整枚举 `M mod 6` 的六个 `N=10^M mod 7` 相位。结果只有 `M≡1,5 (mod 6)` 存活，每个相位只剩两个 `B mod 7` residue；其余四个长度相位严格排除 fixed-7 extra-depth orbit。本文是有限模 `7` 局部证书，不排除两个 surviving phases，也不关闭 A2。

---

## 1. fixed `7` extra-depth setting

沿用前一文件的唯一 exceptional branch：

\[
\boxed{p=7,}
\tag{1.1}
\]

并且

\[
\boxed{
D\equiv4N\pmod7,
\qquad
K\equiv2\pmod7.}
\tag{1.2}
\]

这里

\[
N=10^M.
\]

由于 `10≡3 (mod 7)`：

\[
\boxed{N\equiv3^M\pmod7,}
\tag{1.3}
\]

所以只需检查 `M mod 6`。

---

## 2. `K≡2` 唯一确定 `A=a_2 mod 7`

原 prefix 定义为

\[
\boxed{K=9N+10A.}
\tag{2.1}
\]

模 `7` 有 `9≡2`、`10≡3`，所以 fixed-7 branch满足

\[
2N+3A\equiv2\pmod7.
\]

因为 `3^{-1}≡5 (mod 7)`：

\[
\boxed{
A\equiv3(1-N)\pmod7.}
\tag{2.2}
\]

因此一旦 `M mod 6` 固定，`N mod 7` 与 `A mod 7` 都不再自由。

---

## 3. target height gate 模 `7` 变成一个一元 quartic

真正的 equal-depth omega-height target 已由 parent 文件证明

\[
v_7(\mathscr H_{\omega H}^{\rm pref})=h\ge1,
\]
其中

\[
\boxed{
\mathscr H_{\omega H}^{\rm pref}
=B^2K^2+Q^2N_0,}
\tag{3.1}
\]

\[
Q=B+2N,
\qquad
N_0=\left(\frac{9B}{2}\right)^2+A^2.
\tag{3.2}
\]

因此必有

\[
\boxed{B^2K^2+Q^2N_0\equiv0\pmod7.}
\tag{3.3}
\]

当前 genuine height prime 与 `BQN_0` 分离，所以还必须保留

\[
\boxed{7\nmid BQN_0.}
\tag{3.4}
\]

在模 `7` 下，`K≡2`，而

\[
\frac92\equiv1\pmod7
\]
（因为 `2^{-1}≡4`）。所以

\[
N_0\equiv B^2+A^2\pmod7.
\tag{3.5}
\]

于是 height gate 化为

\[
\boxed{
F_{N,A}(B)
:=4B^2+(B+2N)^2(B^2+A^2)
\equiv0\pmod7.}
\tag{3.6}
\]

其中 `A` 已由 (2.2) 唯一决定。

---

## 4. 六个 `M mod 6` 相位的完整表

逐个代入

\[
N=3^M\pmod7,
\qquad
A=3(1-N)\pmod7,
\]
并只保留满足 (3.4) 的 `B`：

\[
\boxed{
\begin{array}{c|c|c|c}
M\bmod6 & N\bmod7 & A\bmod7 & \text{admissible }B\bmod7\\ \hline
0&1&0&\varnothing\\
1&3&1&\{2,4\}\\
2&2&4&\varnothing\\
3&6&6&\varnothing\\
4&4&5&\varnothing\\
5&5&2&\{1,3\}
\end{array}}
\tag{4.1}
\]

所以 fixed `7` extra-depth target 必须满足

\[
\boxed{M\equiv1\text{ 或 }5\pmod6.}
\tag{4.2}
\]

其它四个长度相位

\[
\boxed{M\equiv0,2,3,4\pmod6}
\tag{4.3}
\]

已严格排除该 orbit。

---

## 5. surviving residues 的完整局部数据

对两个 surviving phases，把 `Q` 与 `N_0` 也列出：

### `M≡1 (mod 6)`

此时

\[
N\equiv3,
\qquad
A\equiv1.
\]

两个解分别为

\[
\boxed{
(B,Q,N_0)\equiv(2,1,5),\ (4,3,3)\pmod7.}
\tag{5.1}
\]

### `M≡5 (mod 6)`

此时

\[
N\equiv5,
\qquad
A\equiv2.
\]

两个解分别为

\[
\boxed{
(B,Q,N_0)\equiv(1,4,5),\ (3,6,6)\pmod7.}
\tag{5.2}
\]

所有显示的 `B,Q,N_0` 都是 `7`-进单位，符合 genuine target separation。

另外四个 `N_0` residue

\[
5,3,5,6
\]
均为模 `7` 非平方，这与已有 height character

\[
\left(\frac{N_0}{7}\right)=-1
\]
一致；因此该 character在这里没有进一步删除 surviving states，不能重复收费。

---

## 6. quartic factor audit

在两个 surviving phases，(3.6) 的 quartic分别分解为

\[
\boxed{
M\equiv1:\quad
F(B)
=(B-2)(B+3)(B^2-3B+1)
\pmod7,}
\tag{6.1}
\]

\[
\boxed{
M\equiv5:\quad
F(B)
=(B-3)(B-1)(B^2+3B-2)
\pmod7.}
\tag{6.2}
\]

两个 quadratic factors 在模 `7` 均不产生额外 admissible root；真正 surviving roots正是 (4.1) 中四个 linear residues。

这说明 fixed `7` extra-depth orbit 已经降成四个 simple local states，而不是一个未解析 quartic branch。

---

## 7. 当前 fixed-7 frontier

综合 target-ladder 与本文：

\[
\boxed{
\begin{gathered}
\rho_7\ge1,
\quad
v_7(\mathscr R_{PD})>h
\\
\Longrightarrow
K\equiv2,
\quad
D\equiv4N\pmod7,
\\
M\equiv1,5\pmod6,
\\
(B,Q,N_0)\text{ 仅有 (5.1)、(5.2) 四个 residue states.}
\end{gathered}}
\tag{7.1}
\]

因此 fixed `7` 的 extra-resultant branch 已从无限长度族缩成两个 `M mod 6` phase、四个 mod-`7` states。

下一步若继续攻击 `7`，应提升这四个 simple states到 `mod 49`，并与

\[
v_7(\mathcal P_{\omega H}(K))=h,
\qquad
v_7(\Lambda_{\rm tail})=\rho_7
\]
的 gcd ladder联立；普通模 `7` quadratic character已无额外信息。

A2 仍为 `待证`。
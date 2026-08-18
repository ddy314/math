# A2 pure-spontaneous 固定 `p=11` 审计

> **依赖：** `spontaneous-prefix-boundaries.md`、`spontaneous-sphere-roots.md`、`spontaneous-single-branch-syzygy.md`。
>
> **严格状态：**`11` 在两个 prefix quadratic 的 resultant/subresultant 常数中出现，但 sphere 几何证明它并不是 branch-collision 的真实例外。对真实 decimal 相位 `tau=10^{-M}=±1 (mod 11)` 做完整第一层审计后，恰留下 12 个 genuine noncentral 状态，而且 12 个全部为 simple roots。因此 `11` 不能被局部排除，但在**实际 decimal 第一层**没有 singular state。这里不宣称任意抽象 `tau∈F_11` 都不存在 noncentral repeated root。本文仍**不宣称 A2 全局关闭**。

---

## 1. `11` 不是 branch-collision 例外

`spontaneous-prefix-branch-audit.md` 的 subresultant 含系数

\[
198000=2^4\cdot3^2\cdot5^3\cdot11,
\]
所以仅从该 subresultant 在模 `11` 下不能继续推出 branch 二分。但 sphere 几何本身没有这一问题。

若

\[
\Delta_0\ne0,
\]
两个 finite sphere roots 满足

\[
\bar\zeta_2-\bar\zeta_1
=\frac{9(225x^2-y)A_-A_{\rm sp}}
{200x^2y^3(x+2)^2\Delta_0}.
\tag{1.1}

在 genuine pure-spontaneous channel 中

\[
11\nmid xy(x+2)(225x^2-y)A_{\rm sp},
\]
而 `A_-=0` 已证明会强迫 concatenated numerator/denominator 双零，即退出 `p∤alpha` pure channel。因此

\[
\boxed{p=11,\ \Delta_0\ne0\Longrightarrow
\text{两个 admissible finite sphere roots 仍严格不同。}}
\tag{1.2}

若

\[
\Delta_0=0,
\]
`spontaneous-prefix-boundaries.md` 已证明 sphere 恰降为一次式，只有一个 finite root。

因此：

\[
\boxed{
p=11\text{ 不会因为 subresultant 的 coefficient }11
\text{ 制造真实 two-branch collision。}}
\tag{1.3}

resultant 中的 coefficient `11` 只是清分母/正规化层的坏系数，不能被解释成第二个 sphere orientation 合并。

---

## 2. `审计修正`：抽象 `F_11` repeated-root 不能从 syzygy 直接排除

compact branch 为

\[
\mathscr L(\tau)
=55\tau^2+18(z-s)\tau+s^2-4sz-c.
\]

模 `11` 后二次首项消失：

\[
\mathscr L'(\tau)
=110\tau+18(z-s)
\equiv7(z-s).
\tag{2.1}

所以 abstract repeated condition 只先给

\[
z\equiv s\pmod{11}.
\tag{2.2}

`spontaneous-single-branch-syzygy.md` 的 discriminant identity

\[
405x^2\mathscr D
=20x^2(81z+29s)^2+11C_*
\]
在模 `11` 下与 (2.2) 相容，并不会额外强迫

\[
9\tau=2s.
\]

因此旧的过强说法

\[
\text{“任意 }p=11\text{ repeated root 必 central”}
\]
撤回，不得使用。

本文真正需要的不是任意 abstract `tau`，而是原问题的真实 decimal phase；它只有两个 residue，下一节直接完整检查。

---

## 3. 真实 decimal length 在模 `11` 只有两个第一层相位

因为

\[
10\equiv-1\pmod{11},
\]
所以

\[
\boxed{
\tau=10^{-M}\equiv(-1)^M\in\{1,10\}\pmod{11}.}
\tag{3.1}

因此 fixed `11` 的真实第一层可以完整有限审计，而不需要扫描任意 `tau`。

对每个

\[
\tau\in\{1,10\},
\quad x,y\in\mathbf F_{11}^\times,
\]
逐项要求：

- `x+2`、`225x^2-y`、`A_sp` 为单位；
- normalized `N_0=2025x^2+y^2` 为单位；
- `Omega_sp` 唯一恢复的 `bar w` 为单位；
- q/f/source 三个分离量均为单位；
- `2(9+y)-9tau` 非零（noncentral）；
- `Theta` 恢复 `bar zeta`；
- exact sphere 成立；
- concatenated numerator `9+y+bar zeta` 非零。

完整枚举只剩 12 个状态。

---

## 4. `有限证书`：12 个 genuine noncentral `11`-states

按

\[
(\tau,x,y,\bar w,\bar\zeta)
\]
列出：

\[
\boxed{
\begin{array}{c|ccccc}
&\tau&x&y&\bar w&\bar\zeta\\ \hline
1&1&1&2&7&8\\
2&1&5&2&3&9\\
3&1&7&9&5&5\\
4&1&8&6&7&3\\
5&1&10&10&7&2\\
6&10&1&2&7&3\\
7&10&2&6&3&5\\
8&10&4&7&2&2\\
9&10&4&9&3&10\\
10&10&5&2&3&2\\
11&10&6&10&6&7\\
12&10&7&4&5&8
\end{array}}
\tag{4.1}

这些点全部满足 genuine denominator/source/base-norm separation，且

\[
\Delta_0A_-C_*\ne0\pmod{11}.
\tag{4.2}

所以没有一个靠 prefix-defect degree drop、common-`alpha` 或 central kernel 偷渡。

每个状态恰命中一个 finite sphere orientation；不存在双 branch。

---

## 5. `已严格完成`：真实 12 个状态全部 simple

compact branch derivative 为

\[
\mathscr L'(\tau)
=110\tau+18(z-s).
\]
在 `p=11` 下就是

\[
7(z-s).
\]

对 (4.1) 十二点依次得到

\[
\boxed{
1,8,8,4,2,10,7,1,10,3,4,9
\pmod{11}.}
\tag{5.1}

全部非零。因此：

\[
\boxed{
\text{真实 decimal 第一层的 12 个 genuine }11\text{-states 全部 simple。}}
\tag{5.2}

这才是 fixed `11` 的严格 singularity 结论：**实际相位上没有 repeated state**。它不推广到任意抽象 `tau∈F_11`。

---

## 6. `已严格完成 / 降级`：decimal exponent orbit 本身也不会自动杀掉 `11`

\[
10^2=100=1+9\cdot11,
\]
其中 `9` 是 `11`-进单位。因此

\[
\boxed{
\operatorname{ord}_{11^k}(10)
=2\cdot11^{k-1}
\qquad(k\ge1).
}
\tag{6.1}

所以 `tau=±1 (mod 11)` 的 decimal exponent classes 都有完整的一维 `11`-进 lift。第一层 simple 并不意味着完整 `(x,y)` 状态自动提升，但也说明“继续只升 exponent”不会制造空性；还需要真实 prefix variables 的 lift条件。

---

## 7. 更新后的 fixed-11 结论

`11` 应当从“可能的 branch-collision bad coefficient”重新分类为：

\[
\boxed{
\text{fixed local carrier with 12 genuine simple first-layer templates}.}
\]

严格来说：

- no two-branch collision；
- 对真实 `tau=±1`，没有 repeated state；
- 12 genuine noncentral first-layer states survive；
- decimal exponent residue classes本身可继续提升。

所以 `11` 尚未关闭，但后续不应再把 resultant coefficient `11` 当成 branch singularity。真正剩余问题是把这 12 个 template 与

\[
b_2=10^{M-1}+2^{M-1}H,
\qquad
a_2=10^{M-1}-e
\]
的真实 defect lift 联立。

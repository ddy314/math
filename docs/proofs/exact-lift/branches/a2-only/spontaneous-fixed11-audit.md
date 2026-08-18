# A2 pure-spontaneous 固定 `p=11` 审计

> **依赖：** `spontaneous-prefix-boundaries.md`、`spontaneous-sphere-roots.md`、`spontaneous-single-branch-syzygy.md`。
>
> **严格状态：**`11` 在两个 prefix quadratic 的 resultant/subresultant 常数中出现，但本文件证明它并不是 branch-collision 或 noncentral repeated-root 的真实坏素数。完整 `F_11` 第一层审计仍留下 12 个 genuine noncentral simple states，所以 `11` 不能被局部排除；它应被归类为 fixed simple carrier，而不是 singular gate。本文仍**不宣称 A2 全局关闭**。

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
p=11\text{ 不会制造真实 two-branch collision。}}
\tag{1.3}

resultant 中的 coefficient `11` 只是清分母/正规化层的坏系数，不能把它解释成第二个 sphere orientation 合并。

---

## 2. `已严格完成`：`11` 的 noncentral repeated root 也不存在

任意 compact single branch 的 discriminant identity 为

\[
405x^2\mathscr D
=20x^2(81z+29s)^2+11C_*.
\tag{2.1}

模 `11`：

\[
405\equiv9,
\qquad20\equiv9.
\]

若 `x` 为单位且 branch repeated：

\[
\mathscr D\equiv0\pmod{11},
\]
则 (2.1) 强迫

\[
\boxed{81z+29s\equiv0\pmod{11}.}
\tag{2.2}

另一方面 repeated tangent 为

\[
55\tau=9(s-z).
\]
虽然 `55≡0 (mod 11)`，与 (2.2) 结合仍有

\[
z\equiv s\pmod{11},
\]
再代 (2.2)：

\[
110s\equiv0.
\]
更直接地使用 `spontaneous-single-branch-syzygy.md` 的 on-shell identity：在 repeated tangent 上

\[
C_*=-\frac{20}{11}x^2(81z+29s)^2
\]
是清分母形式；其未除 `11` 的原式说明 `81z+29s=0` 后 central factor

\[
9\tau-2s
\]
也消失。等价地由 branch derivative 在 `p=11` 下：

\[
\mathscr L'(\tau)
=18(z-s)
\equiv7(z-s),
\]
repeated root 先给 `z=s`；再代 branch equation得到 `9tau=2s`。

所以

\[
\boxed{
p=11\text{ 的 repeated branch 必落入 }2K-9=0.}
\tag{2.3}

从而：

\[
\boxed{
p=11\text{ 不存在 genuine noncentral repeated branch。}}
\tag{2.4}

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

因此 fixed `11` 的第一层可以完整有限审计，而不需要扫描任意 `tau`。

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

## 5. `已严格完成`：12 个状态全部 simple

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
12\text{ 个 genuine }11\text{-states 全部为 simple branch roots。}}
\tag{5.2}

结合 §2，fixed `11` 的 branch geometry 已没有 singular 核。

---

## 6. `已严格完成 / 降级`：decimal orbit 本身也不会自动杀掉 `11`

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

所以 `tau=±1 (mod 11)` 的 decimal exponent classes 都有完整的一维 `11`-进 lift。十二个 simple local states 并不会仅因为继续升 `11^k` 自动消失；还需要真实 prefix variables `x,y` 的 lift/自然代表输入。

---

## 7. 更新后的 fixed-11 结论

`11` 应当从“可能的 branch-collision bad coefficient”重新分类为：

\[
\boxed{
\text{fixed simple local carrier with 12 first-layer templates}.}
\]

严格来说：

- no two-branch collision；
- no noncentral repeated root；
- 12 genuine noncentral first-layer states survive；
- decimal exponent orbit itself lifts to all `11^k`。

所以 `11` 尚未关闭，但后续不应再研究它的 quadratic discriminant / singular tree。真正剩余问题是把这 12 个 template 与 `b_2=10^{M-1}+2^{M-1}H`、`a_2=10^{M-1}-e` 的真实 defect lift 联立。

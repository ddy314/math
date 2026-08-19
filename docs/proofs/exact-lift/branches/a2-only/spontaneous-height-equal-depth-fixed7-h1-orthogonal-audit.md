# A2 fixed `7`, `K=4`, baseline `h=1` 的 orthogonal 低层 residue compression

> **依赖：** `spontaneous-height-equal-depth-orthogonal-decimal-norm.md`、`spontaneous-height-equal-depth-fixed-second-layer-squeeze.md`、`spontaneous-height-equal-depth-tropical-balance.md`。
>
> **严格状态：**本文补齐 fixed `7` 的另一张 quadratic root。对 `K=4 mod7`, `h=1` 的 orthogonal exception，deep `R_+` 先强迫 `D/N` 的第一提升 digit 与 `K` 同步；若 `L_perp` 再获得第二个 extra digit，则 `D/N` 的下一 digit也被唯一决定。此时 `E_+` 想超过最小 deep depth `3`，必须命中一个由 `K mod49` 唯一决定的 normalized numerator unit `a=alpha/(49T) mod7`。六个 exact-h=1 classes中，`K=46 mod49` 会要求 `a=0`，与 `v_7(alpha)=2` 冲突，故直接删除；其余五类各只剩一个 `a mod7`。本文不排除这五个 residue states 的更高 lift，因此不关闭 A2。

---

## 1. local normalization

固定

\[
p=7,
\qquad
h=v_7(P)=v_7(U)=1,
\]
并处在 orthogonal exceptional root

\[
\boxed{K\equiv4\pmod7.}
\tag{1.1}
\]

沿用

\[
P=6K^2-36K+55,
\qquad
U=DK-N,
\]

\[
R_+=DP-KU,
\]

以及

\[
L_\perp=(55D-18N)\alpha+3TR_++T(53-15K)U.
\tag{1.2}
\]

因为 `7∤NT`，定义

\[
\boxed{d:=D/N\in\mathbf Z_7^\times.}
\tag{1.3}
\]

`U=0 mod7` 与 `K=4 mod7` 给

\[
\boxed{d\equiv2\pmod7.}
\tag{1.4}
\]

写

\[
\boxed{K=4+7k+49k_2,\qquad d=2+7\ell+49\ell_2.}
\tag{1.5}
\]

又 equal depth `h=1` 给

\[
v_7(\alpha)=2.
\]
所以定义 unit

\[
\boxed{a:=\frac{\alpha}{49T}\in\mathbf Z_7^\times.}
\tag{1.6}
\]

后文只使用它模 `7` 的 residue。

---

## 2. first normalized digits

由 `K=4+7k+49k_2` 直接展开：

\[
\boxed{\frac P7\equiv1+5k\pmod7.}
\tag{2.1}
\]

并且

\[
\boxed{\frac{U}{7N}\equiv1+2k+4\ell\pmod7.}
\tag{2.2}
\]

由

\[
\frac{R_+}{N}=dP-K(dK-1)
\]
得到

\[
\boxed{\frac{R_+}{7N}\equiv5+2k+5\ell\pmod7.}
\tag{2.3}
\]

---

## 3. deep `R_+` 唯一同步 first lift

当前 deep resonance要求

\[
\boxed{v_7(R_+)\ge2.}
\tag{3.1}
\]

由 (2.3)：

\[
5+2k+5\ell\equiv0\pmod7.
\]
因为 `5^{-1}=3 mod7`：

\[
\boxed{\ell\equiv k+6\pmod7.}
\tag{3.2}
\]

代回 (2.2)：

\[
\frac{U}{7N}
\equiv1+2k+4(k+6)
\equiv4+6k.
\]
而

\[
2\frac P7
\equiv2+10k
\equiv2+3k.
\]
两者都恰在

\[
k\equiv4\pmod7
\]
时消失。事实上 `P/7=0` 也由 (2.1) 给同一条件。因此：

\[
\boxed{
v_7(P)=v_7(U)=1
\Longleftrightarrow
k\not\equiv4\pmod7.}
\tag{3.3}
\]

`k=4` 即

\[
K\equiv32\pmod{49},
\]
是 `P=0` 的 quadratic Hensel lift，属于 `h>=2` 而非本文低 baseline。

---

## 4. orthogonal second extra digit 唯一决定 `D/N` 的下一位

现在进一步要求

\[
\boxed{v_7(L_\perp)\ge3.}
\tag{4.1}
\]

把 (1.5)、(1.6) 与 (3.2) 代入 exact identity (1.2)，除以 `49NT` 后模 `7`，得到

\[
\boxed{
\frac{L_\perp}{49NT}
\equiv
 a+k^2+6k+6k_2+\ell_2
\pmod7.}
\tag{4.2}
\]

所以 (4.1) 唯一强迫

\[
\boxed{
\ell_2
\equiv
k_2+k-k^2-a
\pmod7.}
\tag{4.3}
\]

这说明 orthogonal exception一旦再多一层，source ratio的第二 lift digit不再自由。

---

## 5. `E_+` deeper 的唯一 numerator-unit condition

在 (3.2) 下直接展开

\[
\boxed{
\frac{R_+}{49N}
\equiv
3k+2k_2+5\ell_2+6
\pmod7.}
\tag{5.1}
\]

再代入 (4.3)，`k_2` 完全消失：

\[
\boxed{
\frac{R_+}{49N}
\equiv
2a+2k^2+k-1
\pmod7.}
\tag{5.2}
\]

由于

\[
E_+=E_M\omega R_+,
\qquad v_7(E_M\omega)=1,
\]
所以

\[
\boxed{
v_7(E_+)\ge4
\Longleftrightarrow
2a+2k^2+k-1\equiv0\pmod7.}
\tag{5.3}
\]

等价地

\[
\boxed{
a\equiv-k^2+3k+4\pmod7.}
\tag{5.4}
\]

因此给定 `K mod49` 后，只有唯一一个 normalized numerator unit `a mod7` 能让 `E_+` 再继续一层。

---

## 6. complete low-baseline table

exact `h=1` 排除 `k=4`，所以六个 admissible `k` 与 `K mod49` 为

\[
\boxed{
\begin{array}{c|c|c}
k&K\bmod49&\text{若 }v_7(E_+)\ge4\text{ 所需 }a\\ \hline
0&4&4\\
1&11&6\\
2&18&6\\
3&25&4\\
5&39&1\\
6&46&0
\end{array}}
\tag{6.1}
\]

但 `a` 由 (1.6) 是 `7`-进单位，因此

\[
\boxed{a\not\equiv0\pmod7.}
\tag{6.2}
\]

所以最后一行严格不可能：

\[
\boxed{
K\equiv46\pmod{49},\quad v_7(L_\perp)\ge3
\Longrightarrow
v_7(E_+)=3.}
\tag{6.3}
\]

其余五个 classes若要 `E_+` deeper，也各自只剩表 (6.1) 中唯一 `a`。

---

## 7. tropical consequence

若某个 surviving class确实满足

\[
v_7(E_+)\ge4,
\]
则 `spontaneous-height-equal-depth-tropical-balance.md` 的 universal `h=1` squeeze 给

\[
\boxed{
\min\{r_B,\rho_7\}=1.}
\tag{7.1}
\]

所以这些 low-baseline states仍不可能同时承担第二层 `B_W` residual与第二层 full resonance tail。

---

## 8. fixed-7 low-baseline frontier after both roots

fixed `7`, `h=1` 的两个 roots现在均已离散化：

- `K=2 mod7` / `R_PD` exception：若 `R_PD` 有第二个 extra digit，六个 `K mod49` classes中只有 `K=9` 能让 `E_+` deeper；
- `K=4 mod7` / `L_perp` exception：若 `L_perp` 有第二个 extra digit，六个 exact-h=1 classes中 `K=46` 被直接删除，其余五类各只允许唯一 `alpha/(49T) mod7` residue使 `E_+` deeper。

因此 fixed `7` 的低 baseline已从连续三项 cancellation降成有限 first/second normalized templates。后续若继续 `7`，应把这些模板与 `Lambda_tail` 的 first normalized unit或 `B_W` residual unit联立，而不再扫描全部 `7`-adic roots。

A2 仍为 `待证`。

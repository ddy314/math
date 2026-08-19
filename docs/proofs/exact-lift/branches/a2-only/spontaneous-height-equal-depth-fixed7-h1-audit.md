# A2 fixed `7`, `K=2`, baseline `h=1` 的低层 residue compression

> **依赖：** `spontaneous-height-equal-depth-fixed-second-layer-squeeze.md`、`spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-equal-depth-decimal-pair.md`。
>
> **严格状态：**上一层 second-layer squeeze 对 `h>=2` 已把 fixed exceptions 压到最浅 `E_+` depth；唯一未覆盖的是 `h=1` 时 `R_+`、`F_7U`、`U^2` 同时可能落在第二层。本文对最危险的 fixed `7`, `K=2` extra-resultant root做完整低层展开。deep condition先唯一强迫 `D/N=32 mod49`；若 `R_PD` 还要超过一层，则进一步唯一强迫 `D/N=179 mod343`。在该状态下六个 exact-`h=1` 的 `K mod49` classes中，只有 `K=9 mod49` 能让 `E_+` 超过最小 deep depth `3`；其余五类全部精确 `v_7(E_+)=3`。本文不排除 `K=9 mod49` 的继续 lift，也不处理 fixed-7 的另一根 `K=4`，因此不关闭 A2。

---

## 1. unit-normalized source variables

固定

\[
p=7,
\qquad
h=v_7(P)=v_7(U)=1,
\]
并处在 fixed extra-resultant root

\[
\boxed{K\equiv2\pmod7.}
\tag{1.1}
\]

这里

\[
P=6K^2-36K+55,
\qquad
U=DK-N,
\]

\[
R_+=DP-KU,
\qquad
R_{PD}=55D^2-36DN+6N^2.
\]

因为 `7∤N`，可在 `Z_7` 中定义 unit ratio

\[
\boxed{d:=D/N.}
\tag{1.2}
\]

于是

\[
\frac UN=dK-1,
\tag{1.3}
\]

\[
\frac{R_+}{N}
=dP-K(dK-1),
\tag{1.4}
\]

\[
\frac{R_{PD}}{N^2}
=55d^2-36d+6.
\tag{1.5}
\]

fixed root `K=2` 与 `U=0 mod7` 给

\[
\boxed{d\equiv4\pmod7.}
\tag{1.6}
\]

写

\[
\boxed{K=2+7k,\qquad d=4+7\ell.}
\tag{1.7}
\]

---

## 2. first normalized digits

直接展开并除以 `7`：

\[
P
=7\left(1-12k+42k^2\right),
\]
所以

\[
\boxed{\frac P7\equiv1+2k\pmod7.}
\tag{2.1}
\]

又

\[
dK-1
=7\left(1+4k+2\ell+7k\ell\right),
\]
故

\[
\boxed{
\frac{U}{7N}
\equiv1+4k+2\ell\pmod7.}
\tag{2.2}
\]

对 `R_+`，由 (1.4) 展开得到

\[
\boxed{
\frac{R_+}{7N}
\equiv2+3\ell\pmod7.}
\tag{2.3}
\]

注意 (2.3) 中 `k` 完全消失。这是 low-baseline branch 的第一个 rigidity。

---

## 3. deep resonance 唯一决定 `D/N mod49`

当前 genuine deep target满足

\[
\boxed{v_7(R_+)\ge2.}
\tag{3.1}
\]

由 (2.3)：

\[
2+3\ell\equiv0\pmod7,
\]
所以

\[
\boxed{\ell\equiv4\pmod7.}
\tag{3.2}
\]

于是

\[
\boxed{d=D/N\equiv32\pmod{49}.}
\tag{3.3}
\]

这恰好与 fixed-7 quadratic Hensel root一致，但这里它不是额外假设，而是由 `h=1 + deep R_+` 直接恢复。

把 `ell=4` 代回 (2.2)：

\[
\frac{U}{7N}
\equiv2+4k
=2(1+2k)
\pmod7.
\]
结合 (2.1)：

\[
\boxed{
\frac{U}{7N}
\equiv2\frac P7
\pmod7.}
\tag{3.4}
\]

因此

\[
\boxed{
v_7(P)=v_7(U)=1
\Longleftrightarrow
k\not\equiv3\pmod7.}
\tag{3.5}
\]

`k=3` 正是 `K=23 mod49` 的 quadratic lift，会把 baseline提升到 `h>=2`，所以必须从当前 `h=1` case删除。

---

## 4. 若 `R_PD` 再多一层，则 `D/N mod343` 也唯一

现在进一步假设 fixed resultant 不只达到 `h+1=2` 层，而是

\[
\boxed{v_7(R_{PD})\ge3.}
\tag{4.1}
\]

由 (3.3) 写

\[
\boxed{d=32+49j.}
\tag{4.2}
\]

代入 (1.5)，除以 `49` 后模 `7`：

\[
\boxed{
\frac{R_{PD}}{49N^2}
\equiv6+5j\pmod7.}
\tag{4.3}
\]

所以 (4.1) 强迫

\[
6+5j\equiv0\pmod7,
\]
即

\[
\boxed{j\equiv3\pmod7.}
\tag{4.4}
\]

因此

\[
\boxed{
D/N\equiv179\pmod{343}.}
\tag{4.5}
\]

所以 fixed-7 `h=1` branch若想让 `R_PD` 出现第二个 extra digit，source ratio 到 `7^3` 已经完全无自由。

---

## 5. `E_+` 的 next depth只剩一个 `K mod49` class

在 (4.5) 下，把

\[
K=2+7k+49k_2
\]
代入 (1.4)。直接展开后，`k_2` 在下一 residue 中消失，并得到

\[
\boxed{
\frac{R_+}{49N}
\equiv
6k^2+4k+4
=6(k-1)(k-3)
\pmod7.}
\tag{5.1}
\]

由当前 exact baseline (3.5)，`k=3` 已被排除。因此：

\[
\boxed{
v_7(R_+)\ge3
\Longleftrightarrow
k\equiv1\pmod7.}
\tag{5.2}
\]

而

\[
E_+=E_M\omega R_+,
\qquad
v_7(E_M\omega)=h=1,
\]
所以

\[
\boxed{
v_7(E_+)\ge4
\Longleftrightarrow
k\equiv1\pmod7.}
\tag{5.3}
\]

也就是

\[
\boxed{
v_7(E_+)\ge4
\Longleftrightarrow
K\equiv9\pmod{49}.}
\tag{5.4}
\]

所有其它 exact-`h=1` classes都满足

\[
\boxed{v_7(E_+)=3.}
\tag{5.5}
\]

---

## 6. 完整 `K mod49` table

`K=2+7k` 且 `k!=3`，所以六个 admissible classes为

\[
\boxed{
K\equiv2,9,16,30,37,44\pmod{49}.}
\tag{6.1}
\]

在 `v_7(R_PD)>=3` 下：

\[
\boxed{
\begin{array}{c|c|c}
K\bmod49&k\bmod7&v_7(E_+)\\ \hline
2&0&3\\
9&1&\ge4\\
16&2&3\\
30&4&3\\
37&5&3\\
44&6&3
\end{array}}
\tag{6.2}
\]

因此最危险的 low-baseline triple cancellation从六个 local states再压成唯一 `K=9 mod49` state。

---

## 7. current low-baseline frontier

fixed `7`, root `K=2` 现在严格分成：

1. `v_7(R_PD)=2`：只有一个 extra digit；
2. `v_7(R_PD)>=3` 且 `K!=9 mod49`：
   \[
   D/N=179\pmod{343},
   \qquad v_7(E_+)=3;
   \]
3. 唯一还能同时让 `R_PD` 与 `E_+` 继续深化的 state：
   \[
   \boxed{D/N\equiv179\pmod{343},\qquad K\equiv9\pmod{49}.}
   \]

后续若继续 fixed-7 low baseline，应该只追最后这一条 state与 `Lambda_tail` / `B_W` residual的 next digit，不再枚举其它 `K mod49` classes。

本文不处理 `K=4` orthogonal exception或 fixed `2671,h=1`；A2 仍为 `待证`。

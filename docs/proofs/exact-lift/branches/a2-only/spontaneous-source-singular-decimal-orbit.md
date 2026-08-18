# A2 source→common singular projection 的 decimal-orbit 排除

> **依赖：** `spontaneous-source-common-integer.md`、`spontaneous-source-singular-resolution.md`。
>
> **严格状态：**projected source→common gate 的唯一 genuine non-`3` inert singular algebraic point位于 `p=1746991`、`tau=807263 mod p`。本文证明该 `tau` 根本不属于 `10` 在 `F_p^×` 中生成的子群，因此不存在任何 decimal length `M` 使 `tau=10^{-M}`。所以无论 abstract transverse blow-up 是否存在，真实十进制 endpoint 永远不会进入该 singular point。结合其余 bad primes 的 finite-root audit，真实 A2 source→common singular sector因此全部关闭；剩余仅为 generic simple roots。本文仍不关闭整个 A2。

---

## 1. 唯一 algebraic singular point

`spontaneous-source-common-integer.md` 已证明：source→common first-layer gate

\[
\mathcal C_{\rm src}(x,\tau)=0
\]

在 genuine non-`3` inert primes上的 projected singular bad set只有

\[
11,\quad1746991,\quad405504443.
\]

其中：

- `p=11` 没有 finite singular point；
- `p=405504443` 的 repeated discriminant factor在 `F_p` 无根；
- 唯一 finite genuine singular point是

\[
\boxed{
p=1746991,\qquad
x_0=1362653,\qquad
\tau_0=807263.}
\tag{1.1}
\]

此前 transverse audit研究的是这个 algebraic point附近的 abstract `p`-adic geometry。真实 endpoint还必须额外满足 decimal orbit：

\[
\boxed{\tau=10^{-M}.}
\tag{1.2}
\]

---

## 2. `已严格完成`：`10` 的模 `p` 阶

精确计算：

\[
\boxed{
\operatorname{ord}_{1746991}(10)=174699.}
\tag{2.1}
\]

并且

\[
\boxed{
174699=3^2\cdot7\cdot47\cdot59.}
\tag{2.2}
\]

注意

\[
p-1=1746990=10\cdot174699,
\]
所以 `10` 只生成 `F_p^×` 的 index-`10` 子群。

所有真实 decimal phase

\[
10^{-M}
\]
当然都属于该子群，因此必要条件为

\[
\boxed{
\tau^{174699}=1\pmod p.}
\tag{2.3}
\]

---

## 3. singular `tau_0` 不在 decimal subgroup

直接 modular exponentiation：

\[
\boxed{
807263^{174699}
\equiv119562
\not\equiv1
\pmod{1746991}.}
\tag{3.1}
\]

因此

\[
\boxed{
807263\notin\langle10\rangle\subset\mathbf F_p^\times.}
\tag{3.2}
\]

等价地，不存在任何整数 `M` 满足

\[
\boxed{
10^{-M}\equiv807263\pmod{1746991}.}
\tag{3.3}
\]

所以 (1.1) 虽然是 source→common algebraic surface 的 genuine singular residue，却不是**十进制 length orbit**上的 residue。

---

## 4. 与 corrected transverse audit 的关系

`spontaneous-source-common-integer.md` 修正了旧 checker 的 `p`-adic carry，并得到 abstract transverse 结论：

- `h>=2` 无 full source/common lift；
- `h=1` 二阶 equation 有两个 normalized transverse roots
  \[
  D=\pm16651.
  \]

`spontaneous-source-singular-resolution.md` 又证明这两个 blow-up roots都是 simple。

这些结论描述的是**如果允许 tau 固定在 algebraic residue `807263`**时的局部几何。本文 (3.3) 说明真实 decimal endpoint根本到不了这个 base point，所以两个 abstract `h=1` branches也无需继续与真实 `(H,e)` 做同步：

\[
\boxed{
\text{decimal orbit exclusion occurs before transverse lifting.}}
\tag{4.1}
\]

因此 carry 修正仍必须保留——它纠正了局部数学事实；但对最终 A2 pruning，decimal-orbit lemma更强。

---

## 5. source→common singular sector 全部关闭

三个 projected bad primes逐一归纳：

\[
\boxed{
\begin{array}{c|c}
p&\text{status}\\ \hline
11&\partial_\tau C_{src}\text{ 无 }F_{11}\text{ 零点}\\
405504443&\text{repeated }D_{sc}\text{ factor无 }F_p\text{ 根}\\
1746991&\tau_0\notin\langle10\rangle
\end{array}}
\tag{5.1}
\]

所以：

\[
\boxed{
\text{真实 decimal A2 source→common channel不存在 singular first-layer state}.}
\tag{5.2}
\]

这比“没有 surviving singular Hensel tree”更强：真正 endpoint连 singular tree的根节点都不存在。

---

## 6. 更新后的 source frontier

source-supported common channel现在只剩

\[
\boxed{\text{generic simple roots of }\mathcal K_{src}(H,E,F)}
\]

与：

\[
4Fe\equiv-E(5F^2+18FH+9H^2)\pmod{p^h},
\]

以及真实窄窗

\[
0<H<F/19,
\qquad
0<e<EF/250
\]

的同步。

因此后续 source 工作不应再审计 singular primes，包括 `1746991`；最有价值的是 generic simple root 的 decimal/natural-representative closure。
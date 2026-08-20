# A2 fixed `23` `eta=2` `c=2` 的 full canonical `a_3` CRT representative

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-a3-crt-representative.md`、`spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`、`spontaneous-cq-canonical-defect-overlap.md`。
>
> **严格状态：**此前 third numerator CRT只使用 `2^m` binary root 与 `5^(lambda-1)` Gaussian root，得到 modulus `T/25`，真实 digit window占其 `1/10`。本文加入 canonical square allocation 对 `a_3 mod c_Q` 的 exact directed root。当前 `c_Q=1587=3*23^2` 与 decimal moduli互素，因此 full CRT modulus提升为 `1587*T/25`，而窗口宽度不变，故候选必须落在完整 CRT cell 的前 `1/15870`。固定 pure-23 orientation 后，剩余 3-primary allocation只有两个选择，所以每个 source divisor / Gaussian phase至多检查两个 full representatives。

---

## 1. current canonical divisor choices

当前

\[
\boxed{c_Q=1587=3\cdot23^2.}
\tag{1.1}

canonical allocation满足

\[
c_Q=c_-c_+,
\]
且每个 prime power完整分配到唯一一侧。因此

\[
\boxed{
(c_-,c_+)\in
\{(1,1587),(3,529),(529,3),(1587,1)\}.}
\tag{1.2}

pure fixed-`23` orientation进一步将其二分：

### `23^2|c_-`

\[
\boxed{c_-\in\{529,1587\}.}
\tag{1.3-}

### `23^2|c_+`

\[
\boxed{c_-\in\{1,3\}.}
\tag{1.3+}

也就是说 fixed `23` orientation选定后，只剩 `3`-primary factor在同侧或对侧的二元选择。

---

## 2. directed factor system唯一固定 `a_3 mod c_Q`

当前 `d=1,k_h=1` 的 endpoint directed factors为

\[
\boxed{
\frac g2-a_3=5c_-r_-,}
\tag{2.1-}

\[
\boxed{
\frac g2+a_3=c_+r_+.}
\tag{2.1+}

因为 `g` 被 `4` 整除，`g/2` 为整数；又 `5` 与 `c_Q` 互素。因此

\[
\boxed{
a_3\equiv\frac g2\pmod{c_-},}
\tag{2.2-}

\[
\boxed{
a_3\equiv-\frac g2\pmod{c_+}.}
\tag{2.2+}

并且

\[
\gcd(c_-,c_+)=1.
\]
所以对每个完整 canonical allocation `(c_-,c_+)`，CRT唯一确定

\[
\boxed{
a_{3,(Q)}\pmod{c_Q}.}
\tag{2.3}

这个 residue包含此前 pure-23 marker之外的 `3`-primary side choice。

---

## 3. three-way coprime CRT

前一文件已经得到：

1. 唯一 binary root
   \[
   a_{3,(2)}\pmod{2^m};
   \]
2. 固定 Gaussian orientation后的唯一 long-5 root
   \[
   a_{3,(5)}\pmod{5^{\lambda-1}}.
   \]

现在再加入 (2.3)。三个模数

\[
2^m,
\qquad
5^{\lambda-1},
\qquad
c_Q=1587
\]
两两互素。因此完整 CRT modulus 为

\[
\boxed{
\mathfrak M_3^\sharp
:=c_Q2^m5^{\lambda-1}.}
\tag{3.1}

由 `m=lambda+1` 和 `T=10^m`：

\[
2^m5^{\lambda-1}=\frac T{25}.
\]
故

\[
\boxed{
\mathfrak M_3^\sharp
=1587\frac T{25}.}
\tag{3.2}

固定 source divisor `theta`、Gaussian orientation与 canonical allocation后，三条 residue唯一给

\[
\boxed{
R_{3,\sharp}^{\rm CRT}
\in[0,\mathfrak M_3^\sharp).}
\tag{3.3}

---

## 4. digit window只占 full CRT cell 的 `1/15870`

真实 third-numerator window为

\[
T<a_3<T+\frac T{250}.
\tag{4.1}

full modulus不再整除 `T`，所以定义 shifted representative

\[
\boxed{
H_{3,\sharp}
:=\operatorname{res}_{[0,\mathfrak M_3^\sharp)}
\left(R_{3,\sharp}^{\rm CRT}-T\right).}
\tag{4.2}

若真实 `a_3` 存在，则

\[
a_3=T+h,
\qquad0<h<T/250,
\]
从而 `h` 与 (4.2) 同余。因为 interval长度远小于 modulus，必须有

\[
\boxed{
0<H_{3,\sharp}<\frac T{250}.}
\tag{4.3}

而由 (3.2)：

\[
\frac T{250}
=rac{\mathfrak M_3^\sharp}{1587\cdot10}.
\]
所以 exact representative test 是

\[
\boxed{
0<H_{3,\sharp}
<\frac{\mathfrak M_3^\sharp}{15870}.}
\tag{4.4}

反过来若 (4.4) 成立，则该 CRT class在 digit interval中唯一可能的整数就是

\[
\boxed{a_3=T+H_{3,\sharp}.}
\tag{4.5}

因此 candidate cell比例从旧 two-way CRT 的

\[
\frac1{10}
\]
收紧到

\[
\boxed{\frac1{15870}.}
\tag{4.6}

---

## 5. fixed `23` orientation后的候选数

source-only divisor certificate已经把 `(lambda,c_u,theta)` 固定后 `g` 唯一恢复；Gaussian phase最多两种。

对一个已经选定的 pure-23 canonical orientation：

- 若 `23^2|c_-`，只需检查 `c_-=529,1587`；
- 若 `23^2|c_+`，只需检查 `c_-=1,3`。

所以固定 source divisor与 Gaussian orientation后，full canonical level最多两个 shifted representatives `H_{3,#}`。

每一个必须通过极窄 test (4.4)。

---

## 6. post-CRT reconstruction

若某个 full representative通过 (4.4)，则 `a_3` 已被 exact 恢复。随后无需再搜索其它 continuous third-block variable：

\[
g=\frac{5^{3\lambda}+1587c_u}{\theta},
\]

\[
b_3=2^{3\lambda+2}\cdot5\cdot1587c_u,
\]

\[
a_3=T+H_{3,\sharp}.
\]

接着可由 exact quadratic identity恢复

\[
\boxed{
a_2
=\frac{g^2-4a_3^2-81b_3^2}{20\cdot1587}.}
\tag{6.1}

并检查 prefix digit window、primitive gcd 与 finite-defect `C`。因此 full CRT通过后也只剩确定性验证，没有新的整数枚举。

---

## 7. updated source certificate

对最后的 `(1,1587,1,+)` type，规范 finite certificate应按以下顺序：

1. `lambda=8 mod11` 与 source-content window枚举 `c_u`；
2. 在 centered `19.5–19.75 L_*` interval 中找满足 `theta mod23^3` filter 的奇 divisor；
3. 恢复 `g`；
4. 对至多两个 Gaussian orientations和两个 compatible `3`-allocations计算 full `a_3` CRT；
5. 只保留
   \[
   H_{3,\sharp}/\mathfrak M_3^\sharp<1/15870;
   \]
6. 用 (6.1) 等 exact formulas做最终确定性审计。

与原始无界连续搜索相比，third numerator的 geometric freedom现在被压缩成极小的 canonical CRT cell。无界 closure剩余任务是证明这些 full representatives统一无法进入该 cell，或把进入情况进一步同步到已知 odd-depth classes。
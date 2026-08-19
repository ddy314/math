# A2 equal-depth dual short carriers 的 mod-24 双字符 parity ledger

> **依赖：** `spontaneous-height-equal-depth-dual-short-carriers.md`、`spontaneous-height-equal-depth-four-sheet-split.md`。
>
> **严格状态：**此前已经证明 prefix carrier `P=6K^2-36K+55` 与真实 third carrier `R_3=6(a_3+3T)^2+T^2` 都是短的 primitive odd-inert parity suppliers，并且 `gcd(P,R_3)` 精确分成 numerator/conjugate 两张互素 sheets。本文把这一 pair 从 `mod 4` 提升到 `mod 24`：`P/5` 与 `R_3/2` 都恒为 `11 mod 24`。任何非 `2,3,5` 公共 prime 都落在 `1,5,7,11 mod 24` 的 Klein 四群，因此约去完整公共 gcd 后两个 residual 不仅 `mod 4` 相同，而且 `mod 24` 完全相同。本文同时审计：该双字符 parity 只控制两张 sheet 的乘积类，不能单独固定 target numerator sheet 的 residue class，所以它本身不是 A2 closure。

---

## 1. 记号

沿用

\[
P:=6K^2-36K+55,
\]

\[
R_3:=6(a_3+3T)^2+T^2,
\]

\[
\alpha=TK+a_3,
\qquad
L_3=T(K-6)-a_3.
\]

当前 endpoint 中

- `K=10r`，其中 `r` 为奇数；
- `m>=5`，故 `T=10^m`；
- `a_3` 为奇数；
- primitive reduction 给 `5\nmid a_3`。

此前已有 exact identity

\[
\boxed{T^2P-R_3=6\alpha L_3}
\tag{1.1}
\]

以及 exact coprime sheet split

\[
\boxed{
G_{P3}:=\gcd(P,R_3)
=G_-G_+,}
\tag{1.2}
\]

其中

\[
\boxed{
G_-:=\gcd(P,\alpha),
\qquad
G_+:=\gcd(P,L_3),
\qquad
\gcd(G_-,G_+)=1.}
\tag{1.3}
\]

真正 equal-depth target 只进入 `G_-` numerator sheet。

---

## 2. prefix primitive carrier 恒为 `11 mod 24`

因为 `K=10r` 且 `r` 为奇数，

\[
K\equiv2\pmod4.
\]

所以 `K^2` 被 `4` 整除，而更精确地

\[
6K^2\equiv0\pmod{24}.
\]

同时 `K` 为偶数，故

\[
36K\equiv0\pmod{24}.
\]

于是

\[
\boxed{P\equiv55\equiv7\pmod{24}.}
\tag{2.1}
\]

`K` 被 `10` 整除，因此 `P` 被 `5` 整除。由于 `5` 在 `mod 24` 下可逆且

\[
5^{-1}\equiv5\pmod{24},
\]
得到

\[
\boxed{\frac P5\equiv7\cdot5\equiv11\pmod{24}.}
\tag{2.2}
\]

这里不声称 `v_5(P)=1`；即使 `P` 还含更高 `5`-primary，(2.2) 仍是严格整数同余。

---

## 3. third primitive carrier 也恒为 `11 mod 24`

当 `m>=5` 时

\[
T=10^m\equiv16\pmod{48}.
\tag{3.1}
\]

因此

\[
3T\equiv0\pmod{48},
\qquad
T^2\equiv16\pmod{48}.
\]

`a_3` 为奇数，所以任意奇数平方满足

\[
a_3^2\equiv1\pmod8.
\]

乘以 `6` 后该信息正好提升为

\[
6a_3^2\equiv6\pmod{48}.
\]

于是

\[
\begin{aligned}
R_3
&=6(a_3+3T)^2+T^2\\
&\equiv6a_3^2+16\\
&\equiv22\pmod{48}.
\end{aligned}
\]

所以

\[
\boxed{R_3\equiv22\pmod{48},}
\tag{3.2}
\]

并可合法除以 `2` 得

\[
\boxed{\frac{R_3}{2}\equiv11\pmod{24}.}
\tag{3.3}
\]

因此两个 short primitive carriers 具有完全相同的 `mod 24` orientation：

\[
\boxed{
\frac P5\equiv\frac{R_3}{2}\equiv11\pmod{24}.}
\tag{3.4}
\]

---

## 4. 公共 prime 只能来自四个 `sqrt(-6)` classes

先注意

\[
\gcd(G_{P3},30)=1.
\tag{4.1}
\]

`2,3` 不整除 `P`；而 `5\nmid R_3`，因为 `T\equiv0 (mod 5)` 且 `5\nmid a_3` 给

\[
R_3\equiv6a_3^2\not\equiv0\pmod5.
\]

固定 odd prime

\[
p\mid G_{P3}.
\]

则 `p|P` 且 `p\ne2,3`。由

\[
P=6(K-3)^2+1
\]
有

\[
(6(K-3))^2\equiv-6\pmod p.
\]

所以

\[
\boxed{\left(\frac{-6}{p}\right)=1.}
\tag{4.2}
\]

对 `p\nmid6`，这等价于

\[
\boxed{p\equiv1,5,7,11\pmod{24}.}
\tag{4.3}
\]

记

\[
\mathcal H_{24}:=\{1,5,7,11\}\subset(\mathbb Z/24\mathbb Z)^\times.
\]

它是 Klein 四群，且每个元素都满足

\[
u^{-1}=u\pmod{24}.
\tag{4.4}
\]

因为 `G_{P3}` 的每个 prime factor都在这些 classes中，

\[
\boxed{G_{P3}\bmod24\in\mathcal H_{24}.}
\tag{4.5}
\]

---

## 5. 约去完整 common gcd 后，两边 residual 的 `mod 24` 完全相同

定义

\[
\boxed{
P^{\rm res}:=\frac{P}{5G_{P3}},
\qquad
R_3^{\rm res}:=\frac{R_3}{2G_{P3}}.}
\tag{5.1}
\]

因为 `G_{P3}` 是完整 gcd，且固定 primes `2,5` 不共享，

\[
\boxed{\gcd(P^{\rm res},R_3^{\rm res})=1.}
\tag{5.2}
\]

由 (3.4)、(4.4)：

\[
\boxed{
P^{\rm res}
\equiv
R_3^{\rm res}
\equiv
11G_{P3}
\pmod{24}.}
\tag{5.3}
\]

所以完整 residue table 是

\[
\boxed{
\begin{array}{c|c|c}
G_{P3}\bmod24
&P^{\rm res}\bmod24
&R_3^{\rm res}\bmod24\\ \hline
1&11&11\\
5&7&7\\
7&5&5\\
11&1&1
\end{array}}
\tag{5.4}
\]

这是此前 `mod 4` parity pair 的严格增强。

---

## 6. 两个独立 binary characters 同时复制

表 (5.4) 同时编码两个 parity bits。

### 6.1 `3 mod 4` inert parity

两 residual 都为 `3 mod 4` 当且仅当

\[
G_{P3}\equiv1\pmod4.
\]

所以

\[
\boxed{
G_{P3}\equiv1\pmod4
\Longrightarrow
P^{\rm res}\equiv R_3^{\rm res}\equiv3\pmod4.}
\tag{6.1}
\]

由于两 residual 互素，它们各自必须携带一份 odd total `3 mod 4` prime parity，而且不能复用同一 prime。

### 6.2 `mod 3` nonresidue parity

两 residual 都为 `2 mod 3` 当且仅当

\[
G_{P3}\equiv1\pmod3.
\]

所以

\[
\boxed{
G_{P3}\equiv1\pmod3
\Longrightarrow
P^{\rm res}\equiv R_3^{\rm res}\equiv2\pmod3.}
\tag{6.2}
\]

因此同一个 common gcd 还决定是否复制第二份 `mod 3` nonresidue parity。

特别地：

- `G_{P3}=1 mod24`：两个 parity bits 同时复制；
- `G_{P3}=5 mod24`：只复制 odd-inert bit；
- `G_{P3}=7 mod24`：只复制 mod-3 bit；
- `G_{P3}=11 mod24`：两 bit 都由 common gcd 吸收，两个 residual 均 `1 mod24`。

---

## 7. 与 exact numerator/conjugate sheet split 联立

已有

\[
G_{P3}=G_-G_+,
\qquad
\gcd(G_-,G_+)=1,
\]

其中 target baseline primes只进入

\[
G_-:=\gcd(P,\alpha).
\]

由于 `G_-`、`G_+` 的 prime factors同样来自 `H_24`，

\[
G_-\bmod24,\ G_+\bmod24\in\mathcal H_{24}.
\tag{7.1}
\]

但 (5.4) 只固定乘积

\[
\boxed{G_-G_+=G_{P3}\pmod{24}.}
\tag{7.2}
\]

它**不固定** `G_-` 或 `G_+` 单独属于哪一个 class。

例如 `G_{P3}=11 mod24` 可以由

\[
(1,11),\ (11,1),\ (5,7),\ (7,5)
\]
四种 ordered sheet classes产生。

所以：

\[
\boxed{
\text{dual-short mod-24 parity 本身不能把某个 parity bit强制指派给 target numerator sheet }G_-.}
\tag{7.3}
\]

这是一条重要 no-double-count 审计。后续若要从 global parity 真正关闭 target，必须再加入一个能区分 `G_-` 与 `G_+` 的 independent orientation / additive input；不能只凭两个 short carriers都是 `11 mod24` 就宣称 target sheet承担奇 parity。

---

## 8. 当前 parity frontier

现在 dual-short pair 的 global arithmetic 被压成：

\[
\boxed{
\frac P5\equiv\frac{R_3}{2}\equiv11\pmod{24},}
\]

\[
\boxed{
G_{P3}=G_-G_+,\quad \gcd(G_-,G_+)=1,}
\]

\[
\boxed{
P^{\rm res}\equiv R_3^{\rm res}\equiv11G_{P3}\pmod{24}.}
\]

因此 common gcd 是否吸收/复制两个 parity bits 已完全确定；尚未确定的唯一离散自由是这两个 bits 在 numerator/conjugate 两张 common sheets之间的分配。

这说明下一步最有价值的输入应来自：

1. 能区分 `alpha` 与 `L_3` 的第二个 natural carrier；或
2. fixed `7/2671` 的 higher-depth Bezout；或
3. `Sigma_geom` 与 residual parity carrier之间的独立 additive relation。

本文不关闭 A2。

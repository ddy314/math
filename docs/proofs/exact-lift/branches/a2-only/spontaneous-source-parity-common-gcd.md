# A2 source parity 的 canonical common gcd 与 square-root depth

> **依赖：** `source-discriminant.md`、`spontaneous-source-parity-collision-gate.md`、`spontaneous-source-parity-reuse-depth.md`。
>
> **严格状态：**`B_W` 与 `D_W/2` 都是 positive primitive `3 mod 4` source parity carriers。本文用完整 common gcd `G_S=gcd(B_W,D_W/2)` 统一此前的 separate/reused supplier讨论：约掉 `G_S` 后两个 coprime residual具有完全相同的 mod-4 orientation。若 `G_S=1 mod4`，两 residual各自必须携带独立 odd-inert parity；若 `G_S=3 mod4`，common gcd吸收 parity。进一步，exact square collision证明每个 genuine common prime的 gcd exponent `k` 至少以 `ceil(k/2)` 深度进入短 linear carrier `18K-55`；因此整个 generic common gcd的 square-root depth受 `<180N` 控制。本文仍保留 fixed `3,5,11` exceptions并不证明 residual primes不存在，故不关闭 A2。

---

## 1. two primitive source parity carriers

已有

\[
\boxed{\mathscr B_W\equiv7\pmod8,}
\tag{1.1}

所以

\[
\boxed{\mathscr B_W\equiv3\pmod4.}
\tag{1.2}

source discriminant满足

\[
\mathscr D_W\equiv6\pmod8,
\]
因此

\[
\boxed{\frac{\mathscr D_W}{2}\equiv3\pmod4.}
\tag{1.3}

两者均为 positive odd integers。

---

## 2. canonical common gcd and residuals

定义

\[
\boxed{
G_S:=\gcd\!\left(\mathscr B_W,\frac{\mathscr D_W}{2}\right).}
\tag{2.1}

由于 `B_W` 为 odd，也有

\[
G_S=\gcd(\mathscr B_W,\mathscr D_W).
\]

定义 coprime residuals

\[
\boxed{B_S:=\frac{\mathscr B_W}{G_S},}
\qquad
\boxed{D_S:=\frac{\mathscr D_W}{2G_S}.}
\tag{2.2}

显然

\[
\boxed{\gcd(B_S,D_S)=1.}
\tag{2.3}

由 (1.2),(1.3)，`G_S` 为 odd，因此模 `4` 可逆，并有

\[
\boxed{
B_S\equiv D_S\equiv3G_S^{-1}\pmod4.}
\tag{2.4}

---

## 3. canonical source parity doubling

若

\[
\boxed{G_S\equiv1\pmod4,}
\]
则 (2.4) 给

\[
\boxed{B_S\equiv D_S\equiv3\pmod4.}
\tag{3.1}

因为 `B_S,D_S` positive、odd、coprime，它们各自都必须含至少一枚 `3 mod4` prime到奇次，而且两枚 suppliers必不同。因此：

\[
\boxed{
G_S\equiv1\pmod4
\Longrightarrow
\text{source residual parity至少需要两枚 distinct inert primes}.}
\tag{3.2}

若

\[
\boxed{G_S\equiv3\pmod4,}
\]
则

\[
\boxed{B_S\equiv D_S\equiv1\pmod4.}
\tag{3.3}

此时两份 source odd parity已被 common gcd整体吸收；residuals不再被 mod-4 强迫各自生成 inert prime。

所以此前“separate / reused”讨论现在有 canonical integer formulation，而不需要先人为选择 supplier primes。

---

## 4. common-prime depth from the square collision

已有 exact identity

\[
\boxed{
55\mathscr B_W-K^2\mathscr D_W
=c_u^2L_S^2,}
\qquad
L_S:=18K-55.
\tag{4.1}

固定 odd common prime `r`，并假设 genuine unit separation

\[
\boxed{r\nmid55Kc_u.}
\tag{4.2}

写

\[
a:=v_r(\mathscr B_W),
\qquad
d:=v_r(\mathscr D_W),
\]

\[
\boxed{k:=v_r(G_S)=\min(a,d),}
\qquad
\ell:=v_r(L_S).
\tag{4.3}

### unequal source depths

若

\[
a\ne d,
\]
则 (4.1) 左端赋值精确为 `k`。右端赋值为 `2ell`，所以

\[
\boxed{k=2\ell.}
\tag{4.4}

特别地 `k` 自动为偶数，并且

\[
\boxed{\ell=k/2.}
\tag{4.5}

### equal source depths

若

\[
a=d=k,
\]
左端两个 summands等深，故

\[
v_r(55B_W-K^2D_W)\ge k.
\]

由 (4.1)：

\[
2\ell\ge k.
\]
所以

\[
\boxed{\ell\ge\left\lceil\frac k2\right\rceil.}
\tag{4.6}

综合两类：

\[
\boxed{
v_r(18K-55)
\ge\left\lceil\frac{v_r(G_S)}2\right\rceil}
\tag{4.7}

对每个 genuine unit-separated common prime成立。

---

## 5. global square-root-depth product

令 `E_S^gen` 为 `G_S` 的 genuine odd common prime support中满足 (4.2) 的 primes。定义

\[
\boxed{
H_S^{\rm gen}
:=\prod_{r\in E_S^{\rm gen}}
r^{\lceil v_r(G_S)/2\rceil}.}
\tag{5.1}

逐 prime由 (4.7)：

\[
\boxed{H_S^{\rm gen}\mid18K-55.}
\tag{5.2}

endpoint有

\[
0<K<10N,
\]
故

\[
\boxed{0<18K-55<180N.}
\tag{5.3}

因此

\[
\boxed{H_S^{\rm gen}<180N.}
\tag{5.4}

这对 common gcd的**全部 generic depth**收费，而不只对 odd/odd reused exponents收费。

---

## 6. squarefree form

令

\[
G_S^{\rm gen}:=\prod_{r\in E_S^{\rm gen}}r^{v_r(G_S)},
\]

以及 odd-exponent radical

\[
\boxed{
R_S^{\rm odd}
:=\prod_{\substack{r\in E_S^{\rm gen}\\v_r(G_S)\text{ odd}}}r.}
\tag{6.1}

则按 exponent逐项有

\[
\boxed{(H_S^{\rm gen})^2=G_S^{\rm gen}R_S^{\rm odd}.}
\tag{6.2}

所以 (5.4) 等价给

\[
\boxed{
G_S^{\rm gen}R_S^{\rm odd}
<(180N)^2.}
\tag{6.3}

若 `G_S≡3 mod4` 的奇 parity由 generic common support承担，则 `R_S^odd` 中至少含一枚 `3 mod4` prime。

---

## 7. fixed exceptions

(4.2) 故意保留固定 bad support。由 source-discriminant 的 gcd audit：

- `r|c_u` 的 nontrivial overlap只可能来自 `5,11`；
- `r=3` 为 source-discriminant fixed parity gate；
- `r|K` 与 (4.1) 的 common genuine root除固定 `5,11` 外不发生。

所以真正没有纳入 `H_S^gen` 的只是有限固定 small-prime bookkeeping；不存在额外 moving common family被隐藏。

---

## 8. relation to serial pool

serial-first target primes属于 `omega` support，而 source-discriminant满足

\[
\gcd(D_W,\omega)\mid6.
\]

因此 non-`3` serial pool与 `G_S^gen` support分离。

现在 source side可同时使用：

1. canonical parity dichotomy `G_S mod4`；
2. generic common-gcd square-root budget
   \[
   H_S^{gen}<180N;
   \]
3. serial/double pool的独立 weighted budget。

这为后续 global product allocation提供了不重复计数的两个 canonical sectors。

A2 仍为 `待证`。

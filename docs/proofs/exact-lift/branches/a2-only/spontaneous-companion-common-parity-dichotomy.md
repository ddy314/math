# A2 `J^circ/B^circ` companion parity 的 canonical common-gcd dichotomy

> **依赖：** `spontaneous-height-resultant-parity.md`、`spontaneous-height-companion-cross.md`、`spontaneous-height-content-oversaturation.md`、`spontaneous-height-equal-depth-target-selector.md`。
>
> **严格状态：**`J^circ` 与 `B^circ` 是约去完整 height gcd `D_H` 后的两个 positive companion residual。本文用 `G_JB=gcd(J^circ,B^circ)` 统一审计它们的 odd-inert parity：当 parent orientation 为 `3 mod4` 时，`G_JB=1 mod4` 强迫两份 parity落在两个互素 residual 中；`G_JB=3 mod4` 则 common gcd本身承担 parity。进一步，common gcd中的 genuine external prime，其完整 gcd exponent全部进入 linear gate `L_JB=DzK+fN`；若 common prime同时 height-supported，则进入既有 omega-content oversaturation / target hierarchy。因此 equal-depth target并非由 companion parity无条件强制，但任何不进入 target 的 parity分配都必须走“两个分离 residual primes”或“external linear-depth”两类明确替代成本。本文不排除这些替代分支，因此不关闭 A2。

---

## 1. parent companions and their common gcd

沿用

\[
D_H
=\gcd(\widehat{\mathcal J}_H,W_q)
=\gcd(\mathscr B_W,W_q),
\]

\[
\boxed{
J^\circ:=\widehat{\mathcal J}_H/D_H,
\qquad
B^\circ:=\mathscr B_W/D_H.}
\tag{1.1}
\]

已有

\[
\widehat{\mathcal J}_H>0,
\qquad
\widehat{\mathcal J}_H\equiv3\pmod4,
\]

\[
\mathscr B_W>0,
\qquad
\mathscr B_W\equiv7\pmod8
\equiv3\pmod4.
\]

`D_H` 为 positive odd integer，所以

\[
\boxed{
J^\circ\equiv B^\circ
\equiv3D_H^{-1}\pmod4.}
\tag{1.2}
\]

定义完整 residual common gcd

\[
\boxed{G_{JB}:=\gcd(J^\circ,B^\circ).}
\tag{1.3}
\]

再定义 coprime residuals

\[
\boxed{
J_1:=J^\circ/G_{JB},
\qquad
B_1:=B^\circ/G_{JB}.}
\tag{1.4}
\]

于是

\[
\boxed{\gcd(J_1,B_1)=1.}
\tag{1.5}
\]

并且

\[
\boxed{
J_1\equiv B_1
\equiv3(D_HG_{JB})^{-1}\pmod4.}
\tag{1.6}
\]

---

## 2. complete mod-4 table

因为 `D_H,G_JB` 都为 odd，只需看两者的 `1/3 mod4` classes：

\[
\boxed{
\begin{array}{c|c|c}
D_H\bmod4&G_{JB}\bmod4&J_1\equiv B_1\pmod4\\ \hline
1&1&3\\
1&3&1\\
3&1&1\\
3&3&3
\end{array}}
\tag{2.1}
\]

因此 residual pair需要两份 independent odd-inert parity，当且仅当

\[
\boxed{G_{JB}\equiv D_H\pmod4.}
\tag{2.2}
\]

此时

\[
\boxed{J_1\equiv B_1\equiv3\pmod4,}
\tag{2.3}
\]

而 `J_1,B_1` positive、odd、coprime，所以它们各自至少含一枚 `3 mod4` prime到奇次，且两枚 suppliers必不同。

特别地，在此前最常用的 parity-doubling orientation

\[
\boxed{D_H\equiv1\pmod4,}
\]
有最简单的二分：

\[
\boxed{
G_{JB}\equiv1\pmod4
\Longrightarrow
J_1,B_1\equiv3\pmod4,}
\tag{2.4}
\]

即 common gcd不吸收 parity，必须生成两枚不同 residual inert suppliers；而

\[
\boxed{
G_{JB}\equiv3\pmod4}
\tag{2.5}
\]
意味着 common gcd本身含 odd total inert parity。

所以 companion parity并不无条件强迫 `G_JB` 非平凡；`G_JB=1` 完全允许，但代价是两份分离 parity。

---

## 3. common parity splits into external or height-supported support

若 `G_JB` 本身承担 odd inert parity，则至少有一枚 genuine inert prime

\[
p\mid G_{JB}.
\]

该 common prime有两类：

### 3.1 external common prime

若

\[
\boxed{p\nmid W_q,}
\tag{3.1}
\]

则它不属于 height-supported oversaturation。`spontaneous-height-companion-cross.md` 给出 genuine external linear gate

\[
\boxed{L_{JB}:=DzK+fN\equiv0\pmod p.}
\tag{3.2}
\]

### 3.2 height-supported common prime

若

\[
\boxed{p\mid W_q,}
\tag{3.3}
\]

则由于 `p|B^circ,J^circ`，完整 height exponent被 `D_H` 吃掉后 companion仍继续加深。`spontaneous-height-content-oversaturation.md` 已证明

\[
\boxed{p\mid\omega,}
\tag{3.4}
\]

并进入 fixed target quadratic

\[
\boxed{
P_{\omega H}(K)
=6K^2-36K+55
\equiv0\pmod p.}
\tag{3.5}
\]

随后才继续按 `e=v_p(omega)` 与 `h=v_p(W_q)` 分成 unequal-depth / equal-depth，equal-depth deep resonance再由 `Sigma_deep`,`Sigma_first`,`Sigma_second` 等 canonical selectors读取。

所以：

\[
\boxed{
\text{common companion parity}
\Longrightarrow
\text{external linear orbit}
\ \text{或}\
\text{height-supported omega/target orbit}.}
\tag{3.6}
\]

---

## 4. external common gcd pays its full depth to `L_JB`

现在固定 genuine external common prime，并假设标准 separation

\[
\boxed{p\nmid qzW^\circ,}
\qquad
W^\circ:=W_q/D_H.
\tag{4.1}
\]

写

\[
j:=v_p(J^\circ),
\qquad
b:=v_p(B^\circ),
\]

\[
\boxed{k:=v_p(G_{JB})=\min(j,b)\ge1.}
\tag{4.2}
\]

已有 exact difference

\[
5^{2d}J^\circ
-(2^mg)^2 5^{2d}B^\circ
=q^2W^\circ\,\mathcal B_p,
\tag{4.3}
\]

其中 bracket满足 exact relation

\[
\boxed{q\mathcal B_p=-zL_{JB}.}
\tag{4.4}
\]

在 (4.1) 下，`q,z,W^circ` 都是 p-adic units，两个左侧 coefficients也是 units。因此：

- 左边两个 summands均被 `p^k` 整除；
- 故其差至少有 depth `k`；
- (4.3),(4.4) 立即给
  \[
  \boxed{v_p(L_{JB})\ge k.}
  \tag{4.5}
  \]

若

\[
\boxed{j\ne b,}
\tag{4.6}
\]

左边有唯一最浅 summand，所以

\[
\boxed{v_p(L_{JB})=k.}
\tag{4.7}
\]

只有 equal companion depths `j=b` 时，linear gate本身才可能继续发生额外 cancellation。

因此 external common gcd不是免费的 support reuse：

\[
\boxed{
\text{每一份 external }G_{JB}\text{ depth都必须由 }L_{JB}\text{ 支付}.}
\tag{4.8}
\]

---

## 5. global parity trichotomy in the dangerous parent orientation

固定

\[
\boxed{D_H\equiv1\pmod4,}
\tag{5.1}
\]

于是 parent companions

\[
J^\circ\equiv B^\circ\equiv3\pmod4.
\]

现在 global companion parity严格只有三种实现方式：

### A. split residual parity

若

\[
G_{JB}\equiv1\pmod4,
\]
则 `J_1,B_1` positive coprime `3 mod4`，所以必须出现两枚不同 inert residual primes。

### B. common external parity

若 `G_JB≡3 mod4` 且承担其 odd parity的 common inert prime不在 `W_q` support，则该 prime进入 external linear gate `L_JB`，并按 §4 支付完整 common depth。

### C. common height-supported parity

若 common inert supplier同时位于 `W_q` support，则它进入 `omega` oversaturation / target hierarchy；equal-depth deep subbranch才进一步进入 `Sigma_deep` 与 serial selectors。

因此：

\[
\boxed{
\text{companion parity}
\Longrightarrow
\begin{cases}
\text{two distinct residual suppliers},\\
\text{external common linear-depth supplier},\\
\text{height-supported omega/target supplier}.
\end{cases}}
\tag{5.2}
\]

这给 global proof一个严格替代关系：**不能假设 target pool必然存在；但不进入 target，就必须支付另外两种明确且可继续量化的 prime成本。**

---

## 6. relation to complete source/target separation

最新 `spontaneous-source-target-support-separation.md` 已把 source-common genuine support与整个 equal-depth target support完全分离。

因此若 case C 最终进入 equal-depth target/serial sector，同时 source parity又调用 genuine source-common pool，则二者成本可以严格叠加，不存在 fixed `11` 复用。

而 case A/B 则给出 target-free alternatives，必须分别从 residual-prime multiplicity或 `L_JB` natural/decimal depth继续攻击。

所以当前正确的 global frontier不是“证明 target一定存在”，而是关闭 trichotomy (5.2) 的三条成本分支。

A2 仍为 `待证`。

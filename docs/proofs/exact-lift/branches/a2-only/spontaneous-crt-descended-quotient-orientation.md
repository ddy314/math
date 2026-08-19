# A2 descended quotient `Dhat_63` 的 parity orientation 与 denominator gate

> **依赖：** `spontaneous-crt-height-remainder-descent.md`、`spontaneous-crt-height-primitive-remainder.md`、`endpoint-lattice.md` 的 `W_q mod 4` orientation 与 mixed coprimality。
>
> **严格状态：**positive descent `That_2=5^lambda Rstar_63+gD_63` 中，`D_63` 仍含显式 `2^m`。本文除去它，定义 positive odd primitive quotient `Dhat_63=D_63/2^m=c_u^2F_63`。其 mod-4 orientation精确等于 `3Z`，所以在危险 `Z=1 mod4` orientation中它本身也是 positive `3 mod4` inert carrier。另一方面它与 denominator `g` 的全部 common support精确等于 central gate `gcd(2K-9,g)`；因此 descended parity不能自由回落到 denominator support。本文不排除 central gate本身，因此不关闭 A2。

---

## 1. primitive descended quotient

前一 descent theorem给

\[
\boxed{
\mathscr D_{63}=2^m c_u^2\mathscr F_{63}>0,}
\tag{1.1}
\]

其中

\[
\boxed{
\mathscr F_{63}
=(2K-9)B_\Delta-\frac{63}{16}gTK^2,}
\tag{1.2}
\]

\[
\boxed{
B_\Delta:=g((2K-9)T-a_3)-H_0.}
\tag{1.3}
\]

`F_63` 已证明为 odd，因此定义

\[
\boxed{
\widehat{\mathscr D}_{63}
:=\frac{\mathscr D_{63}}{2^m}
=c_u^2\mathscr F_{63}
\in\mathbf Z_{>0}\text{ odd}.}
\tag{1.4}
\]

---

## 2. mod-4 orientation

因为

\[
g=2^{t-1}\rho,
\qquad t\ge3,
\]
有

\[
g\equiv0\pmod4.
\]

所以由 (1.3)：

\[
B_\Delta\equiv-H_0\pmod4.
\tag{2.1}
\]

source relation为

\[
H_0=g(3T+a_3)-5^\lambda C.
\]

第一项被 `4` 整除，而 `5^lambda≡1 mod4`，故

\[
\boxed{H_0\equiv-C\pmod4,}
\tag{2.2}
\]

于是

\[
\boxed{B_\Delta\equiv C\pmod4.}
\tag{2.3}
\]

又 `K=10P`，所以 `2K` 被 `4` 整除：

\[
\boxed{2K-9\equiv3\pmod4.}
\tag{2.4}
\]

第二项

\[
\frac{63}{16}gTK^2
\]
在当前 `m>=5,t>=3` 下仍被 `4` 整除。因此

\[
\boxed{
\mathscr F_{63}\equiv3C\pmod4.}
\tag{2.5}
\]

`c_u` 只含 `1 mod4` primes，所以 `c_u^2≡1 mod4`：

\[
\boxed{
\widehat{\mathscr D}_{63}
\equiv3C\pmod4.}
\tag{2.6}
\]

---

## 3. identify `C mod 4` with the old `Z` orientation

已有

\[
H_0=c_uW_q,
\qquad
W_q\equiv3Z\pmod4.
\tag{3.1}
\]

又 `c_u≡1 mod4`，所以

\[
H_0\equiv3Z\pmod4.
\tag{3.2}
\]

与 (2.2) 的 `H_0≡-C≡3C mod4` 比较：

\[
3Z\equiv3C\pmod4.
\]

消去 `3`：

\[
\boxed{C\equiv Z\pmod4.}
\tag{3.3}
\]

代回 (2.6)：

\[
\boxed{
\widehat{\mathscr D}_{63}
\equiv3Z\pmod4.}
\tag{3.4}
\]

特别地在最危险 orientation

\[
\boxed{Z\equiv1\pmod4}
\]
时：

\[
\boxed{
\widehat{\mathscr D}_{63}>0,
\qquad
\widehat{\mathscr D}_{63}\equiv3\pmod4.}
\tag{3.5}
\]

所以 original `That_2`、fully primitive remainder `Rstar_63` 与 descended primitive quotient `Dhat_63` 在该 orientation中都需要 odd-inert parity。

---

## 4. denominator overlap is exactly the central gate

模 `g`，由 (1.3) 与 source relation：

\[
B_\Delta
\equiv-H_0
\equiv5^\lambda C
\pmod g.
\tag{4.1}
\]

(1.2) 第二项显式含 `g`，所以

\[
\boxed{
\mathscr F_{63}
\equiv5^\lambda C(2K-9)
\pmod g.}
\tag{4.2}
\]

mixed/source coprimality已有

\[
\gcd(5c_uC,g)=1.
\tag{4.3}
\]

由于 `Dhat_63=c_u^2F_63`：

\[
\boxed{
\gcd(\widehat{\mathscr D}_{63},g)
=\gcd(2K-9,g).}
\tag{4.4}
\]

所以 descended quotient若想把其 inert parity落回 denominator `g` support，只能通过唯一 central linear gate

\[
\boxed{2K-9.}
\tag{4.5}
\]

不存在 generic denominator reuse。

---

## 5. relation to the nested descent

fully primitive positive descent为

\[
\boxed{
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g\,2^m\widehat{\mathscr D}_{63}.}
\tag{5.1}
\]

其中

\[
\widehat{\mathcal T}_2\equiv3\pmod4,
\qquad
\mathscr R_{63}^\star\equiv3\pmod4,
\qquad
\gcd(\mathscr R_{63}^\star,10g)=1.
\]

在 `Z=1 mod4` 时再加 (3.5)，得到三层 positive `3 mod4` package：

\[
\boxed{
\widehat{\mathcal T}_2,
\quad
\mathscr R_{63}^\star,
\quad
\widehat{\mathscr D}_{63}
\text{ 均为 positive }3\bmod4.}
\tag{5.2}
\]

若 parity试图复用同一 prime，则 parent theorem已经要求该 prime同时进入 `Rstar_63,Dhat_63`；本文又说明若它还位于 denominator support，就必须进入 `2K-9` central gate。

---

## 6. current role

本文没有排除 `gcd(2K-9,g)`。它把 descended quotient的 denominator overlap精确压回仓库已经反复出现的 central sheet。

因此后续 nested descent的 support审计只需区分：

1. central `2K-9` support；
2. genuine external support。

尤其在 `Z=1 mod4` orientation，若能进一步证明 `Rstar_63/Dhat_63` 的 common inert supplier不能进入 central sheet，就会强制原 carrier、short remainder与 descended quotient至少使用两枚不同 inert primes。

A2 仍为 `待证`。

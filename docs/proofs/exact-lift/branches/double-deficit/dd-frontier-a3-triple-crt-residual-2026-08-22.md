# DD frontier: `a_3` 的 triple CRT 与 `rho_*` residual lift

> 日期：2026-08-22
>
> 作用域：假想满足
> \[
> n/S\to6.308883577618\ldots
> \]
> 的 terminal one-channel frontier，固定 denominator/source/orientation fiber，并删除总高度 `o(S)` 的 coefficient exceptional core。
>
> 本文是 **CRT / counting lemma**。其中 pair-max `C_L^2` period来自已有 sphere-paid Gaussian depth，因此绝不能再作为一份独立 p-adic height charge。本文只利用它定位 decimal variable `a_3`。

## 1. 三个作用在 `a_3` 上的 fixed periods

### 1.1 decimal `10^d` period

exact decimal remainder已有

\[
Ua_3=BVA_{12}10^d-R_{\rm dec},
\qquad
R_{\rm dec}=\frac{\Sigma R_0}{g_0},
\]

所以

\[
\boxed{
Ua_3\equiv-R_{\rm dec}\pmod{10^d}.}
\tag{D-period}
\]

terminal phase满足 `(U,10)=1`，故这对 rational integer `a_3` 给出一个固定模 `10^d` residue。

frontier 上

\[
\boxed{d/S\to7/2.}
\tag{1.1}
\]

### 1.2 clean-source `q_c^2` period

clean source与 numerator reconstruction给

\[
\boxed{
g_0a_3+5^TR_0=q_c^2L_{\rm clean}.}
\tag{Clean-a3}
\]

因此

\[
\boxed{
g_0a_3\equiv-5^TR_0\pmod{q_c^2}.}
\tag{Q-period}
\]

删去 `gcd(g_0,q_c)` 的 `10^{o(S)}` exceptional core后，有效 period高度为

\[
\boxed{
2\log q_c
=0.617767155236\ldots S+o(S).}
\tag{1.2}
\]

### 1.3 pair-max `C_L^2` rational period

对 main

\[
p^h\Vert C_L,
\qquad p=\pi\bar\pi,
\]

固定 chosen orientation，使

\[
\pi^{2h}\mid y_2+i y_3.
\]

写

\[
\beta_2=\frac{q_{\rm lcm}}{b_2},
\qquad
\beta_3=\frac{q_{\rm lcm}}{b_3}.
\]

在 pair-max support 上 `beta_2,beta_3` 都是 `p`-units，所以

\[
\boxed{
\pi^{2h}\mid a_2\beta_2+i a_3\beta_3.}
\tag{PM-a3}
\]

若两个 rational integers `a_3,a_3'` 在固定其余 data 与同一 orientation 下均满足 `(PM-a3)`，相减：

\[
\pi^{2h}\mid i\beta_3(a_3-a_3').
\]

因 `beta_3` 是 unit：

\[
\pi^{2h}\mid a_3-a_3'.
\]

但差是 rational integer。取 Gaussian conjugate同时得到

\[
\bar\pi^{2h}\mid a_3-a_3'.
\]

而 `(pi,bar pi)=1`，故

\[
\boxed{p^{2h}\mid a_3-a_3'.}
\tag{PM-rational-period-p}
\]

聚合 main core：

\[
\boxed{
C_L^2/10^{o(S)}
\text{ 是 }a_3\text{ 的 fixed rational period}.}
\tag{CL2-period}
\]

再次强调：这是 **period information**；`C_L^2` 本身就是 sphere pair-max depth，不得再计作独立 height payer。

## 2. 联合 period

terminal 有

\[
(C_L,q_c)=10^{o(S)},
\]

并且 `C_L` 是 odd non-decimal moving core。`q_c` 的 decimal overlap也只进入 slow/ex\-ceptional data；按 effective-period意义，三个 periods 的 lcm满足

\[
\boxed{
M_{a_3}
=
10^d C_L^2 q_c^2/10^{o(S)}.
}
\tag{Triple-period}

因此

\[
\begin{aligned}
\frac{\log M_{a_3}}S
&\to
\frac72+2+2z_*\\
&=5.5+0.617767155236\ldots\\
&=\boxed{6.117767155236\ldots},
\end{aligned}
\tag{2.1}
\]

其中

\[
z_*=0.308883577618\ldots.
\]

而

\[
\boxed{
\log a_3=n+O(1)
=(6+z_*)S+o(S).
}
\tag{2.2}
\]

所以固定 fiber中 `a_3` 的剩余 lift数至多

\[
10^{\rho_*S+o(S)},
\]

其中

\[
\boxed{
\rho_*
=(6+z_*)-(5.5+2z_*)
=\frac12-z_*.
}
\tag{rho-def}

数值为

\[
\boxed{
\rho_*=0.191116422382\ldots.}
\tag{rho-value}
\]

于是

\[
\boxed{
\#\{a_3\text{ in a fixed terminal orientation fiber}\}
\le10^{0.191116422382\ldots S+o(S)}.
}
\tag{a3-count}
\]

## 3. `rho_*` 的 Gaussian 意义

因为

\[
N(\Pi)=C_L=10^{S+o(S)},
\]

有

\[
\log|\Pi|=\frac12S+o(S).
\]

所以

\[
\boxed{
\rho_*S
=\log|\Pi|-\log q_c+o(S).}
\tag{rho-Gaussian}
\]

另一方面 terminal source heights满足

\[
\log U=(1-z_*)S+o(S),
\]

故也有

\[
\boxed{
\rho_*S
=\log U-\log|\Pi|+o(S).}
\tag{rho-geomean}
\]

即

\[
|\Pi|
\]

在 leading height上正处于 `q_c` 与 `U` 的几何中点：

\[
2\log|\Pi|
=\log U+\log q_c+o(S)=S+o(S).
\]

这解释了 residual constant为什么不是一个杂乱的 LP 数值；它正是 terminal moving Gaussian scale相对 source factor的最后不平衡。

## 4. no-double-count audit

`CL2-period` 与已有 `Pairmax-GCRT0` 并非两份独立 arithmetic height。

把 pair-max `a_3` residue代入 exact carry

\[
g_0Ua_3
=g_0B10^dVA_{12}-\Sigma R_0,
\]

其中 `V=C_Lv_0` 已经显式提供一层 `C_L`。从 `C_L^2` depth除去这层后，留下的正好是作用于 `A_{12}` 的 `C_L` second-order period；这就是 `Pairmax-GCRT0` 的来源。

同理，`Q-period` 与 `Q-fixed` 通过同一 carry互相转换。

因此不能把

- `a_3` 的 `C_L^2,q_c^2` periods，和
- `A_{12}` 的 `C_L,q_c^2` periods

同时当成四份独立 modulus 再相乘。

本文只提供一个新的 **`a_3`-coordinate view**。

## 5. 当前真正的 location target

`a_3` triple CRT仍留下

\[
10^{\rho_*S+o(S)},
\qquad
\rho_*=0.191116422382\ldots,
\]

个可能 lifts；所以它本身不关闭 frontier。

下一步若沿此坐标继续，必须寻找一条真正独立、effective height超过 `rho_*S` 的 global condition，或直接证明 CRT 的 canonical representative不进入合法 `n`-digit window。

由于

\[
\rho_*S
=\log(|\Pi|/q_c)+o(S),
\]

最自然的 normalized target是 source/orientation quotient scale

\[
\boxed{|\Pi|/q_c=10^{\rho_*S+o(S)}.}
\]

但 `Pi/q_c` 一般不是 Gaussian integer；后续若使用它，必须通过一个 genuine integral quotient/lattice construction实现，不能把实数高度差误当整除。

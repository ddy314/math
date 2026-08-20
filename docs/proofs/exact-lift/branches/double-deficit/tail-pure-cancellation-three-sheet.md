# DD baseline-free primitive `Q` cancellation 的 three-sheet split

> **依赖：** [`tail-rough-cq-excess.md`](tail-rough-cq-excess.md)、
> `global-framework.md` 的 unified quadratic 与 primitive recovery。
>
> **严格状态：** `已严格完成（baseline-free rough cancellation primes）`。
>
> `tail-rough-cq-excess.md` 说明真正最坏的 post-tail loss发生在 denominator baseline
> 很小的 primitive `Q` cancellation。本文处理最纯的 local sheet：
> \[
> p\nmid10b_1b_2b_3,
> \qquad p^c\Vert Q,
> \qquad c>0.
> \]
> 此时 `p^c||kappa`、`p` 不整除 `G(kappa+G)(kappa+2G)`。
> primitive recovery先强迫
> \[
> \boxed{
> v_p(\nu)=0,
> \qquad
> v_p(G_0)=v_p(\mu)=:\rho,
> \qquad
> \rho\le v_p(\mathcal N_{12}).}
> \]
> 再把 unified quadratic除去 forced `p^c` 后，三个 term的 valuations为
> \[
> \boxed{
> 2\rho,\qquad
> \rho+t,\qquad
> c+n,
> }
> \]
> 其中
> \[
> t=v_p(C),\qquad n=v_p(\mathcal N_{12}).
> \]
> 因此只可能落入三种 pair-min sheets。特别地 `rho=0` 强制 `t=0`，并产生
> 一个深度 `c+n` 的 unit--unit Hensel relation。

---

## 1. baseline-free cancellation hypothesis

固定 odd prime

\[
p\nmid10
\]

并假设

\[
\boxed{
p\nmid b_1b_2b_3,}
\qquad
\boxed{p^c\Vert Q,\quad c>0.}
\tag{1.1}

这正是 `tail-rough-cq-excess.md` 中 `E=j=0` 的最坏 sheet。

因为

\[
G=b_1b_2,
\]

有

\[
\boxed{p\nmid G.}
\tag{1.2}

而 gcd-normal tail weight

\[
\kappa b_3=10^mQG
\]

在 `p` 处给

\[
\boxed{p^c\Vert\kappa.}
\tag{1.3}

因此

\[
p\nmid(\kappa+G)(\kappa+2G).
\tag{1.4}

写

\[
Q=p^cQ_0,
\qquad
\kappa=p^c\kappa_0,
\]

其中 `Q_0,kappa_0` 为 `p`-units。

---

## 2. primitive recovery 先锁死 `nu` 与 `G_0`

primitive recovery为

\[
\boxed{10^mQG_0=2\kappa\mu\nu.}
\tag{2.1}

因为 `p` 不整除 `10` 且 `(1.1),(1.3)` 给

\[
v_p(Q)=v_p(\kappa)=c,
\]

所以

\[
\boxed{v_p(G_0)=v_p(\mu)+v_p(\nu).}
\tag{2.2}

记

\[
r:=v_p(\mu),
\qquad
s:=v_p(\nu).
\]

由 `(mu,nu)=1`：

\[
\min(r,s)=0.
\]

又

\[
G_0=\gcd(
\mathcal N_{12}\nu^2-\mu^2,
2G\mu\nu).
\]

若 `s>0`，则 `r=0`，第一参数

\[
\mathcal N_{12}\nu^2-\mu^2
\]

模 `p` 等于 `-mu^2`，是 unit；于是 `v_p(G_0)=0`，与 `(2.2)` 的
`v_p(G_0)=s>0` 矛盾。

故

\[
\boxed{s=0.}
\tag{2.3}

令

\[
\boxed{\rho:=r=v_p(\mu)=v_p(G_0).}
\tag{2.4}

若 `rho>0`，因为 `nu` 为 unit、`mu^2` 至少含 `p^{2rho}`，要使

\[
p^\rho\mid
\mathcal N_{12}\nu^2-\mu^2
\]

必须有

\[
\boxed{v_p(\mathcal N_{12})\ge\rho.}
\tag{2.5}

`rho=0` 时该式当然仍以非负形式成立。因此统一记

\[
\boxed{n:=v_p(\mathcal N_{12})\ge\rho.}
\tag{2.6}

---

## 3. unified quadratic 的三项 valuation

DD unified quadratic为

\[
Q(\kappa+2G)\mu^2
-2G\kappa C\mu\nu
+\kappa Q\mathcal N_{12}\nu^2
=0.
\tag{3.1}

代入

\[
Q=p^cQ_0,
\qquad
\kappa=p^c\kappa_0
\]

并除以 `p^c`：

\[
\boxed{
Q_0(\kappa+2G)\mu^2
-2G\kappa_0C\mu\nu
+p^c\kappa_0Q_0\mathcal N_{12}\nu^2
=0.
}
\tag{3.2}

记

\[
\boxed{t:=v_p(C).}
\]

由 `(1.2),(1.4)`、`Q_0,kappa_0,nu` 都是 units，三个 term的 valuations
精确为

\[
\boxed{
A=2\rho,
\qquad
B=\rho+t,
\qquad
D=c+n.}
\tag{3.3}

三个整数和为零，因此 ultrametric 必要条件是

\[
\boxed{
\min(A,B,D)
\text{ 至少出现两次}.}
\tag{3.4}

---

## 4. canonical three-sheet partition

由 `(3.3),(3.4)` 只可能有以下三类（允许 triple tie落在交界）：

### AB sheet

\[
A=B\le D.
\]

等价于

\[
\boxed{t=\rho,}
\qquad
\boxed{c+n\ge2\rho.}
\tag{AB}

若严格

\[
c+n>2\rho,
\]

则前两项除去 `p^{2rho}` 后是 units，并必须发生额外深度

\[
\boxed{c+n-2\rho}
\]

的 unit--unit cancellation。

### AD sheet

\[
A=D\le B.
\]

即

\[
\boxed{c+n=2\rho,}
\qquad
\boxed{t\ge\rho.}
\tag{AD}

这里 source cancellation被 `N_12 / mu` 的 norm depth直接吸收。

### BD sheet

\[
B=D\le A.
\]

即

\[
\boxed{\rho+t=c+n,}
\qquad
\boxed{t\le\rho.}
\tag{BD}

结合 `n>=rho`：

\[
\boxed{c\le t\le\rho,}
\qquad
\boxed{n=\rho+t-c.}
\tag{4.1}

这时第二、第三项承担最低层 cancellation。

因此 baseline-free `Q` cancellation不再是一个无结构的 prime-power condition，而是
一个有限 three-sheet Hensel partition。

---

## 5. `rho=0` 是纯 unit-Hensel sheet

若

\[
\rho=0,
\]

则 `n>=0` 且 `c>0`，所以

\[
D=c+n>0,
\qquad
A=0.
\]

为使最小 valuation至少出现两次，必须

\[
B=t=0.
\]

因此

\[
\boxed{p\nmid C\mu\nu G_0.}
\tag{5.1}

`(3.2)` 的第三项恰有 valuation `c+n`，故前两 unit terms的和也恰有同一
valuation：

\[
\boxed{
v_p\!\left(
Q_0(\kappa+2G)\mu^2
-2G\kappa_0C\mu\nu
\right)=c+n.}
\tag{5.2}

约去 unit `mu`，得到 deep Hensel relation

\[
\boxed{
Q_0(\kappa+2G)\mu
\equiv
2G\kappa_0C\nu
\pmod{p^{c+n}}.
}
\tag{Unit-Hensel}

特别地它至少有原 source cancellation 的完整深度 `c`。

---

## 6. `rho>0` 的 norm/Hensel hybrid

若 `rho>0`，已有

\[
\rho\le n.
\]

所以 source cancellation `c` 必须以以下方式之一被支付：

1. `AD/BD` sheet中直接进入 `N_12` / gap norm depth；
2. `AB` sheet中 `C` 本身承担 baseline `rho`，剩余
   \[
   c+n-2\rho
   \]
   （若为正）再次成为 normalized unit--unit Hensel depth。

例如若

\[
c>\rho,
\]

则 `AB` sheet的 residual Hensel depth至少

\[
(c-\rho)+(n-\rho),
\]

而 `AD` sheet只有在 `c<=rho` 时才可能满足 `c+n=2rho`。

因此正线性 `c` 无法完全隐藏在一个匿名 gcd 中：它要么进入 explicit norm
`N_12`，要么重新出现为 coefficient Hensel contact。

---

## 7. 下一接口

对当前 post-tail side-branch reoptimization，真正最坏的是 `rho=0` 的
`Unit-Hensel` sheet，因为它没有先支付任何 prefix norm depth。

其 congruence的系数并非独立：

\[
\frac{\kappa_0}{Q_0}
=\frac{10^mG}{b_3}
\]

是 exact rational quantity。因此下一步应：

- 把 `(Unit-Hensel)` 用 tail recovery消去 `kappa_0/Q_0`；
- 判断它是否退化为已有 coefficient plane identity；
- 若不退化，构造 canonical source Hensel carrier并与 denominator concat
  \(B_1 10^{m_2}+B_2\) 做 cross-resultant。

---

## 8. 状态摘要

- **`已严格完成`**：`nu`-unit lock、`rho<=v_p(N_12)`、three-sheet valuation partition、
  `Unit-Hensel`。
- **`结构压缩`**：baseline-free `X_Q` prime只剩 norm sheet或 explicit unit-Hensel sheet。
- **`待证`**：`Unit-Hensel` 是否退化；若不退化则 source cross-carrier；由此控制
  `X_Q` height并完成 global post-tail reoptimization。

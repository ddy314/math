# A2 descendant balance saturation 的 third-order coefficient 与 fixed degree-148 gate

> **依赖：** `spontaneous-crt-descendant-second-order-gcd-ladder.md`、`spontaneous-crt-descendant-quartic-tail-hierarchy.md`、`spontaneous-crt-descendant-balance-tail.md`。
>
> **严格状态：**finite quartic hierarchy 已把 generic same-prime recycling 的真正 moving frontier推进到 first balance `rho=h` 且 second tail至少吞下一个 baseline `sigma>=h`。本文审计 strict branch `sigma>h`：此时 linear+quadratic block已严格深于 `3h`，若 actual remainder还要越过 `3h`，cubic homogeneous coefficient必须模 `p` 消失。first-order recycling已把 parent ratio唯一固定为 `chi_geom=-2G_>/(81G_<)`；在此 ratio上，cubic coefficient的 primitive numerator是 degree-20 polynomial `S_3(K,zeta)`。与 universal cubic消去 `zeta` 后只剩 central `(2K-9)^3`、旧 descendant-height gate `G_D(K)^2`，以及一个 irreducible degree-148 pure-K gate `P_148(K)`。所以 generic noncentral、non-height moving branch中，`sigma>h` 的 third-order overdepth只能命中 fixed `P_148`；真正未固定化的 third-order resonance进一步缩成 exact saturation `sigma=h`。本文不排除 `P_148` 的 modular roots，因此不关闭 A2。

---

## 1. cubic homogeneous coefficient

沿用 parent coordinates

\[
X=5^\lambda\mathscr R_{63}^\star,
\qquad
Y=g2^m\widehat{\mathscr D}_{63},
\]

以及

\[
\chi:=X/Y.
\]

finite quartic hierarchy 已证明 exact cubic block为

\[
\boxed{
M^{(3)}
=s_L^3
\frac{8192\,\mathcal H_3(X,Y;K,\zeta)}
{5^5 11^5K^2},}
\tag{1.1}
\]

其中 `H_3` 对 `(X,Y)` 齐次三次，`zeta` 次数2，共24项。

除去 `Y^3`，定义 ratio coefficient

\[
\mathcal Q_3(K,\zeta;\chi)
:=\mathcal H_3(\chi,1;K,\zeta).
\tag{1.2}
\]

first-order same-prime recycling在 equal parent depth上已唯一固定

\[
\boxed{
\chi_{geom}
=-\frac{2\mathcal G_>}{81\mathcal G_<}.}
\tag{1.3}
\]

---

## 2. primitive numerator at the geometric balance

将 (1.3) 代入 (1.2)。exact simplification给

\[
\boxed{
\mathcal Q_3(K,\zeta;\chi_{geom})
=
\frac{2^{13}\,\mathcal S_3(K,\zeta)}
{81K^2\mathcal G_<^3}.}
\tag{2.1}
\]

这里 `S_3` 取 primitive integer normalization，checker给

\[
\boxed{
\deg_{total}\mathcal S_3=20,
\qquad
\deg_\zeta\mathcal S_3=19,}
\tag{2.2}
\]

\[
\boxed{
\#\operatorname{supp}(\mathcal S_3)=230.}
\tag{2.3}
\]

所以 third-order normalization没有产生新的 denominator sheet；denominator只有 genuine unit `K` 与 first-order gate `G_<` 的三次方。

---

## 3. eliminate `zeta`: one new degree-148 gate

与 universal descendant cubic

\[
\mathcal E_{63}(K,\zeta)=0
\]

对 `zeta` 求 exact resultant。得到

\[
\boxed{
\operatorname{Res}_{\zeta}
(\mathcal E_{63},\mathcal S_3)
=
2^{174}3^{10}
(2K-9)^3
G_D(K)^2
P_{148}(K),}
\tag{3.1}
\]

其中

\[
G_D(K)=11K^2-240K+432,
\]

而

\[
\boxed{
\deg P_{148}=148,}
\tag{3.2}
\]

\[
\boxed{
P_{148}\text{ 在 }\mathbf Q[K]\text{ 中不可约},}
\tag{3.3}
\]

并且 `P_148` 恰有149个 nonzero coefficients。

因此排除 central `2K-9` 与旧 height/descendant gate `G_D` 后：

\[
\boxed{
\mathcal E_{63}=\mathcal S_3=0
\Longrightarrow
P_{148}(K)=0.}
\tag{3.4}
\]

正文不抄写149项大多项式；checker从 exact cubic block与 `chi_geom` canonical 重建并验证 factorization、degree与 irreducibility。

---

## 4. no real third-order degeneration

定义 projective form

\[
\boxed{
\mathcal S_3^{proj}(r,u)
:=r^{20}\mathcal S_3(1/r,u/r).}
\tag{4.1}
\]

exact audit给

\[
\deg_r=20,
\qquad
\deg_u=19,
\qquad
\#\operatorname{supp}=230.
\]

真实 endpoint包含于粗 box

\[
0<r<10^{-3},
\qquad
0<u<10^{-3}.
\]

将 (4.1) 搬到 unit square并转 tensor Bernstein basis，共

\[
21\cdot20=420
\]
个 exact rational coefficients。checker验证全部严格为负；极值为

\[
\boxed{
\min b_{ij}
=
-\frac{110643494138140653988416850451597394424139780430491531767088006331095359222500626733242735149107}
{29103830456733703613281250000000000000000000000000},}
\tag{4.2}
\]

\[
\boxed{
\max b_{ij}
=-2741384670235465948046260545341682788232526505<0.}
\tag{4.3}
\]

所以

\[
\boxed{\mathcal S_3(K,\zeta)<0}
\tag{4.4}
\]

在整个真实 dangerous endpoint成立。`P_148` branch没有 real third-order cancellation point；任何 surviving root只能来自 p-adic wrapping。

---

## 5. depth consequence

固定 genuine common prime，记

\[
h=v_p(G_\Delta),
\qquad
\rho=v_p(B_{63}),
\qquad
\sigma=v_p(C_{63}^{(2)}).
\]

当前 generic equal-parent moving branch已被前层压到

\[
\rho=h.
\]

若进一步

\[
\boxed{\sigma>h,}
\tag{5.1}
\]

second-order ladder给

\[
v_p(M^{(1)}+M^{(2)})
=2h+\sigma>3h.
\]

而 cubic block normally具有 baseline `3h`。因此若 actual remainder还满足

\[
\boxed{v_p(M)>3h,}
\tag{5.2}
\]

cubic coefficient必须模 `p` 消失。在 first recycling ratio已固定为 `chi_geom` 后，就是

\[
\mathcal S_3(K,\zeta)\equiv0\pmod p.
\]

结合 universal cubic与 §3：

\[
\boxed{
\rho=h,
\quad
\sigma>h,
\quad
v_p(M)>3h
\Longrightarrow
p\mid P_{148}(K),}
\tag{5.3}
\]

在 genuine noncentral、non-`G_D` sector成立。

所以 strict second-tail overdepth再次被一个 fixed irreducible pure-K gate固定化。

---

## 6. revised generic third-order frontier

目前 generic moving same-prime branch可进一步收缩：

- `rho<h`：first ladder exact；
- `rho>h` 且越过 `2h`：进入 fixed `P_110`；
- `rho=h, sigma<h`：second ladder exact；
- `rho=h, sigma>h` 且越过 `3h`：进入 fixed `P_148`；
- 所以真正仍保留未固定 normalized third-order resonance的 moving branch只剩
  \[
  \boxed{\rho=h,\qquad\sigma=h.}
  \tag{6.1}
  \]

下一步应直接在 `rho=sigma=h` 上读取 third tail `C_63^(3)` 的 exact saturation；不应继续扩大 `P_148` 的 ordinary discriminant分析。

A2 仍为 `待证`。

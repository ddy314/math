# A2 equal-depth target 的 triple `sqrt(-6)` orientation 与 fixed `2671`

> **依赖：** `spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-equal-depth-dual-short-carriers.md`、`spontaneous-height-equal-depth-decimal-pair.md`。
>
> **严格状态：**本文把 prefix quadratic `P`、source-prefix resultant `R_PD` 与真实 third carrier `R_3` 统一写成同一个 `sqrt(-6)` norm orbit，并识别真正 equal-depth numerator sheet在 source 与 third 两侧采取同一反向 orientation。由此构造 cross-orientation linear carrier `L_D3=55TD-36TN-6Na_3`。在 deep resonance `rho_p>=1` 下，所有 genuine moving target primes 都满足 `v_p(L_D3)=h`；若 `L_D3` 想超过 baseline `h`，exact Bezout 强迫唯一 fixed prime `p=2671`。因此 moving deep target 的两个独立 next-depth directions现已分别只留下 fixed `7`（source-prefix）与 fixed `2671`（source-vs-third orientation）两个例外。本文不排除 fixed `2671`，不关闭 A2。

---

## 1. 三个 `sqrt(-6)` carriers

沿用

\[
\boxed{P:=6K^2-36K+55=6(K-3)^2+1.}
\tag{1.1}
\]

source-prefix resultant 为

\[
\boxed{R_{PD}:=55D^2-36DN+6N^2.}
\tag{1.2}
\]

直接配方：

\[
\boxed{
55R_{PD}=(55D-18N)^2+6N^2.}
\tag{1.3}
\]

真实 third carrier 为

\[
\boxed{R_3:=6(a_3+3T)^2+T^2.}
\tag{1.4}
\]

所以三个 target conditions 都在同一个 quadratic extension `sqrt(-6)` 中。

定义对应的 normalized square roots

\[
\boxed{
X_P:=6(K-3),
\qquad
X_D:=\frac{55D-18N}{N},
\qquad
X_3:=6\frac{a_3+3T}{T}.}
\tag{1.5}
\]

对 genuine target prime `p`，`N,T` 都是 p-units。

由 `p|P`：

\[
X_P^2\equiv-6\pmod p.
\tag{1.6}
\]

由 `p|R_PD`：

\[
X_D^2\equiv-6\pmod p.
\tag{1.7}
\]

由 `p|R_3`：

\[
X_3^2\equiv-6\pmod p.
\tag{1.8}
\]

---

## 2. source-prefix root 与 prefix root 取反 orientation

真正 target 还有

\[
U:=DK-N=qW_q,
\qquad p^h\Vert U,
\]

所以 first layer

\[
DK\equiv N\pmod p.
\tag{2.1}
\]

于是

\[
\frac DN\equiv K^{-1}\pmod p.
\]

利用 `P(K)=0 mod p`：

\[
6K^2-36K+55\equiv0,
\]
故

\[
55-18K
\equiv18K-6K^2
=-6K(K-3).
\]

除以 unit `K`：

\[
\boxed{
X_D
=\frac{55D-18N}{N}
\equiv-6(K-3)
=-X_P
\pmod p.}
\tag{2.2}
\]

所以 source-prefix resultant选择的是 `P` root 的反向 `sqrt(-6)` orientation。

---

## 3. numerator sheet 的 third root也取反 orientation

真正 equal-depth target满足

\[
p\mid\alpha,
\qquad
\alpha=TK+a_3.
\]

因此

\[
\frac{a_3}{T}\equiv-K\pmod p.
\]

于是

\[
\boxed{
X_3
=6\left(\frac{a_3}{T}+3\right)
\equiv-6(K-3)
=-X_P
\pmod p.}
\tag{3.1}
\]

所以 numerator sheet 上

\[
\boxed{X_D\equiv X_3\equiv-X_P\pmod p.}
\tag{3.2}
\]

与 `spontaneous-height-equal-depth-dual-short-carriers.md` 的 exact sheet split一致：conjugate sheet `L_3=0` 会取 `X_3=+X_P`，而真正 target 的 `alpha=0` sheet取反向 root。

---

## 4. source 与 third orientation 的自然线性差

由 (3.2)，定义 integer cross carrier

\[
\boxed{
\begin{aligned}
\mathcal L_{D3}
&:=TN(X_D-X_3)\\
&=T(55D-18N)-6N(a_3+3T)\\
&=55TD-36TN-6Na_3.
\end{aligned}}
\tag{4.1}
\]

每个 genuine equal-depth target first layer都满足

\[
p\mid\mathcal L_{D3}.
\]

但 deep resonance允许我们精确读取它的下一层。

---

## 5. `L_D3` 与 deep companion 的 exact identity

沿用

\[
R_+:=DP-KU,
\qquad
U=DK-N,
\]

以及

\[
\alpha=TK+a_3.
\]

直接展开得到

\[
\boxed{
\mathcal L_{D3}
=TR_+ +T(36-5K)U-6N\alpha.}
\tag{5.1}
\]

固定 deep equal-depth target：

\[
v_p(P)=h,
\qquad
v_p(U)=h,
\qquad
v_p(\alpha)=2h,
\qquad
\rho_p\ge1.
\]

`spontaneous-height-equal-depth-decimal-pair.md` 已证明

\[
\boxed{v_p(R_+)\ge h+1.}
\tag{5.2}
\]

写

\[
U=p^hU_0,
\qquad p\nmid U_0.
\]

将 (5.1) 除以 `p^h` 并模 `p`。第一项由 (5.2) 消失，第三项因 `2h>=h+1` 也消失，所以

\[
\boxed{
\frac{\mathcal L_{D3}}{p^h}
\equiv
T(36-5K)U_0
\pmod p.}
\tag{5.3}
\]

由于 `T,U_0` 为 p-units：

\[
\boxed{
 v_p(\mathcal L_{D3})>h
 \Longleftrightarrow
 5K-36\equiv0\pmod p
 \qquad(\rho_p\ge1).}
\tag{5.4}
\]

所以 source-vs-third orientation想继续超过 baseline，只可能撞一个新的线性 K-exception。

---

## 6. linear exception 唯一固定为 `2671`

`P` 与 `5K-36` 有 exact Bezout identity

\[
\boxed{
25P-(30K+36)(5K-36)=2671.}
\tag{6.1}
\]

直接展开即可验证。

若 genuine target prime同时满足

\[
p\mid P,
\qquad
p\mid5K-36,
\]
则

\[
p\mid2671.
\]

而

\[
\boxed{2671\text{ 是素数},
\qquad2671\equiv7\pmod{24}.}
\tag{6.2}
\]

因此该 fixed prime确实落在允许的 inert class 中，不能靠 first-layer character排除。

结合 (5.4)：

\[
\boxed{
\rho_p\ge1,
\quad p\ne2671
\Longrightarrow
v_p(\mathcal L_{D3})=h.}
\tag{6.3}
\]

这与 target-ladder 的

\[
\rho_p\ge1,\ p\ne7
\Longrightarrow
v_p(R_{PD})=h
\]

是两个不同的 next-depth directions：

- `7` 控制 source-prefix resultant是否超过 baseline；
- `2671` 控制 source root与真实 third root的 orientation差是否超过 baseline。

---

## 7. fixed `2671` 的 first-layer residue

若进入唯一 exception：

\[
5K-36\equiv0\pmod{2671}.
\]

因为 `5^{-1}\equiv2137 (mod 2671)`：

\[
\boxed{K\equiv2144\pmod{2671}.}
\tag{7.1}
\]

由 `U=DK-N`：

\[
\boxed{D\equiv NK^{-1}\pmod{2671}.}
\tag{7.2}
\]

由 numerator sheet：

\[
\boxed{a_3\equiv-TK\pmod{2671}.}
\tag{7.3}
\]

本文暂不枚举 `M mod ord_{2671}(10)` 或 prefix `B` roots；这应作为 fixed-prime orbit单独处理，而不是把 (6.2) 误写成矛盾。

---

## 8. 当前 triple-orientation frontier

moving deep target现在有四个互补 reader：

\[
\boxed{
\begin{array}{c|c}
\text{carrier}&\text{target depth}\\ \hline
P&h\\
R_3&h\\
R_{PD}&h\quad(p\ne7)\\
\mathcal L_{D3}&h\quad(p\ne2671).
\end{array}}
\tag{8.1}
\]

full resonance tail仍由

\[
v_p(\Lambda_{\rm tail})=\rho_p
\]

精确读取。

因此所有 moving `p\notin\{7,2671\}` deep targets在 prefix、third、source-prefix、cross-orientation四个自然整数上都只能保持 baseline `h`；额外 resonance depth只能留在 canonical tail quotient中，不能再伪装成这些 companion carriers的额外 p-depth。

下一步最自然的是：

1. 单独压 fixed `2671` 的 length/prefix Hensel orbit；
2. 对 moving `p\notin\{7,2671\}`，利用四个 exact-baseline readers与 `Lambda_tail` 的 excess depth做 product/CRT separation；
3. 检查 `7` 与 `2671` 是否可能同时进入同一 global parity allocation。

A2 仍为 `待证`。

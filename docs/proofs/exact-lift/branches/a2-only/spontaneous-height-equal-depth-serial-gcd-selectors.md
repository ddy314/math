# A2 serial strict resonance 的 canonical gcd selectors

> **依赖：** `spontaneous-height-equal-depth-serial-tropical-bridge.md`、`spontaneous-height-equal-depth-middle-near-pair.md`、`spontaneous-height-equal-depth-tail-normalization.md`、`spontaneous-height-equal-depth-geometric-selector.md`。
>
> **严格状态：**本文把 serial bridge 剩下的 two-node higher cancellation完全改写成 ordinary integer gcd ladders，不再预枚举 target primes。first-node relevant strict branch由两个 `Omega`-ladder quotients选择；second-node 的“`c_p=rho_p` 且 `r_+>rho_p`”则由单个 two-level gcd quotient自动选择，连 equal-depth 条件都无需单独写。二者交集精确对应唯一的 double-serial danger `r_B=h<c_p=rho_p<r_+`。本文把剩余局部机制 canonical 化，但不证明这些 selectors 为 `1`，因此不关闭 A2。

---

## 1. canonical residual readers

沿用 middle near-pair

\[
C_+=C_{BE},
\qquad
C_-=A_P\beta-b_3P,
\]

并定义

\[
\boxed{G_C:=\gcd(C_+,C_-),}
\tag{1.1}
\]

\[
\boxed{C_{\rm tail}:=\frac{C_+}{G_C}.}
\tag{1.2}
\]

对 genuine deep equal-depth target，middle near-pair 已证明

\[
v_p(C_+)=h+c_p,
\qquad
v_p(C_-)=h.
\]

因此

\[
\boxed{v_p(G_C)=h,}
\tag{1.3}
\]

\[
\boxed{v_p(C_{\rm tail})=c_p.}
\tag{1.4}
\]

full-tail normalization 已有 canonical quotient

\[
\Lambda_{\rm tail}
:=\frac{\Lambda_{\rm dec}}{\gcd(\alpha,\Lambda_{\rm dec})},
\]
并在 equal-depth target 上精确满足

\[
\boxed{v_p(\Lambda_{\rm tail})=\rho_p.}
\tag{1.5}
\]

最后定义 baseline common carrier

\[
\boxed{\Omega:=\gcd(P,\beta).}
\tag{1.6}
\]

因为 target 上

\[
v_p(P)=v_p(\beta)=h,
\]
故

\[
\boxed{v_p(\Omega)=h.}
\tag{1.7}
\]

所以 `(Omega,C_tail,Lambda_tail)` 分别给出

\[
\boxed{h,\ c_p,\ \rho_p}
\]
三个完全 canonical 的 local depth readers。

---

## 2. first-node depth-over-baseline ladder

对任意正整数 `X` 定义相对于 `Omega` 的二级 quotient

\[
\boxed{
\mathcal R_\Omega(X)
:=
\frac{\gcd(\Omega^2,X)}{\gcd(\Omega,X)}.}
\tag{2.1}
\]

分母总整除分子，因为 `Omega|Omega^2`。

若 target 上

\[
v_p(\Omega)=h,
\qquad
v_p(X)=x,
\]
则

\[
\boxed{
v_p(\mathcal R_\Omega(X))
=\min(2h,x)-\min(h,x).}
\tag{2.2}
\]

因此

\[
\boxed{
p\mid\mathcal R_\Omega(X)
\Longleftrightarrow
x>h.}
\tag{2.3}
\]

应用于两个 residual readers：

\[
\boxed{
R_C:=\mathcal R_\Omega(C_{\rm tail}),}
\tag{2.4}
\]

\[
\boxed{
R_\Lambda:=\mathcal R_\Omega(\Lambda_{\rm tail}).}
\tag{2.5}
\]

于是 target 上

\[
\boxed{p\mid R_C\Longleftrightarrow c_p>h,}
\tag{2.6}
\]

\[
\boxed{p\mid R_\Lambda\Longleftrightarrow \rho_p>h.}
\tag{2.7}
\]

---

## 3. canonical first-node strict selector

沿用此前 geometric deep-target selector `Sigma_geom`。定义

\[
\boxed{
\Sigma_{\rm first}
:=\gcd(\Sigma_{\rm geom},R_C,R_\Lambda).}
\tag{3.1}
\]

在 genuine deep target sector 中：

\[
\boxed{
p\mid\Sigma_{\rm first}
\Longleftrightarrow
c_p>h,\quad\rho_p>h.}
\tag{3.2}
\]

serial first-node law 又说明 `c_p>h` 只能发生在

\[
\boxed{r_B=h.}
\tag{3.3}
\]

而 `c_p,rho_p>h` 使 second-node minimum本身已大于 `h`，所以

\[
\boxed{r_+>h.}
\tag{3.4}
\]

因此 `Sigma_first` 在当前 genuine sector精确选择此前的 first-node relevant strict mechanism：

\[
\boxed{
r_B=h<\rho_p,\quad r_+>h}
\]
以及其中可能进一步满足 `c_p=rho_p` 的更深 subcase。

更规范地说，它选择

\[
\boxed{r_B=h,\quad c_p>h,\quad\rho_p>h.}
\tag{3.5}
\]

---

## 4. second-node common core

定义两个 residual readers 的 common core

\[
\boxed{
G_2:=\gcd(C_{\rm tail},\Lambda_{\rm tail}).}
\tag{4.1}
\]

在 target 上令

\[
s:=\min(c_p,\rho_p).
\]
则

\[
\boxed{v_p(G_2)=s.}
\tag{4.2}
\]

不需要预先判断 `c_p=rho_p`；`G_2` 只记录两者的公共最浅层。

---

## 5. second-node strict ladder

定义

\[
\boxed{
A_1:=\gcd(\Omega^2G_2,\ F_{\rm dec}E_+),}
\tag{5.1}
\]

\[
\boxed{
A_2:=\gcd(\Omega^2G_2^2,\ F_{\rm dec}E_+),}
\tag{5.2}
\]

以及 quotient

\[
\boxed{
R_{\rm second}:=\frac{A_2}{A_1}.}
\tag{5.3}
\]

因为 `G_2|G_2^2`，有

\[
\Omega^2G_2\mid\Omega^2G_2^2,
\]
故 `A_1|A_2`，所以 (5.3) 是整数。

在 genuine target 上 `F_dec` 是 unit，并且

\[
v_p(E_+)=2h+r_+.
\]

所以

\[
v_p(A_1)
=\min(2h+s,2h+r_+).
\]

serial law 给

\[
r_+\ge s,
\]
故

\[
\boxed{v_p(A_1)=2h+s.}
\tag{5.4}
\]

同理

\[
v_p(A_2)
=2h+\min(2s,r_+).
\]

因此

\[
\boxed{
v_p(R_{\rm second})
=\min(2s,r_+)-s
=\min(s,r_+-s).}
\tag{5.5}
\]

这是 second-node strictness 的 canonical valuation formula。

---

## 6. equal-depth condition is detected automatically

若

\[
c_p\ne\rho_p,
\]
serial second-node law给唯一 minimum：

\[
r_+=s.
\]

代入 (5.5)：

\[
\boxed{v_p(R_{\rm second})=0.}
\tag{6.1}
\]

若

\[
c_p=\rho_p=s,
\]
则：

- 若没有 strict cancellation，`r_+=s`，仍有 `v_p(R_second)=0`；
- 若发生 strict cancellation，`r_+>s`，则
  \[
  \boxed{v_p(R_{\rm second})=\min(s,r_+-s)>0.}
  \tag{6.2}
  \]

所以在 genuine deep target sector：

\[
\boxed{
p\mid R_{\rm second}
\Longleftrightarrow
c_p=\rho_p=:s,\quad r_+>s.}
\tag{6.3}
\]

这是最重要的点：一个 ordinary gcd quotient自动同时检测了

1. second-node 两 residual depths相等；
2. actual sum sheet发生 strict-extra。

无需 factorization，也无需把 `c_p=rho_p` 当作额外负条件手工检查。

---

## 7. canonical second-node selector

定义

\[
\boxed{
\Sigma_{\rm second}
:=\gcd(\Sigma_{\rm geom},R_{\rm second}).}
\tag{7.1}
\]

则在 current genuine deep target sector：

\[
\boxed{
p\mid\Sigma_{\rm second}
\Longleftrightarrow
c_p=\rho_p,\quad r_+>\rho_p.}
\tag{7.2}
\]

所以 serial bridge 的第二个 remaining mechanism现在也被一个 canonical integer selector完全恢复。

---

## 8. double-serial selector

最后定义

\[
\boxed{
\Sigma_{\rm double}
:=\gcd(\Sigma_{\rm first},\Sigma_{\rm second}).}
\tag{8.1}
\]

若 genuine target prime进入该 gcd，则同时有

\[
c_p>h,
\qquad
\rho_p>h,
\]
以及

\[
c_p=\rho_p,
\qquad
r_+>\rho_p.
\]

所以精确得到

\[
\boxed{
r_B=h<c_p=\rho_p<r_+.}
\tag{8.2}
\]

反过来任何满足 (8.2) 的 genuine deep target都进入 `Sigma_double`。

因此：

\[
\boxed{
p\mid\Sigma_{\rm double}
\Longleftrightarrow
r_B=h<c_p=\rho_p<r_+.}
\tag{8.3}
\]

这就是 serial hierarchy 中唯一“两级都 extra”的最危险 orbit。

---

## 9. current canonical frontier

剩余 equal-depth local danger现在可完全由三个普通整数描述：

\[
\boxed{
\Sigma_{\rm first},\qquad
\Sigma_{\rm second},\qquad
\Sigma_{\rm double}.}
\]

其中：

- `Sigma_first`：第一节点超过 baseline，同时 tail也超过 baseline；
- `Sigma_second`：第二节点 equal-depth 后 actual sheet strict-extra；
- `Sigma_double`：唯一双级 serial extra，满足
  \[
  r_B=h<c_p=\rho_p<r_+.
  \]

后续无需继续 prime-by-prime 分类旧四种 tie。最值得攻击的是 `Sigma_double` 的全局高度/奇素数 parity；若它为空，则两个 serial nodes不能同时无界深化。

A2 仍为 `待证`。

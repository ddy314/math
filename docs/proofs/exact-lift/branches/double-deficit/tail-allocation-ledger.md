# double-deficit Tail Allocation Ledger

> 本文件是细粒度研究记录的机械归并账本。各来源的标题、正文和证明状态原样保留；账本中的局部闭合、有限证书或降级路线均不表示该分支或主不存在性命题已经关闭。

## 来源索引

- [`tail-hard-source-derivative-sheet.md`](#source-tail-hard-source-derivative-sheet)
- [`tail-pure-cancellation-hensel-nogo.md`](#source-tail-pure-cancellation-hensel-nogo)
- [`tail-pure-cancellation-three-sheet.md`](#source-tail-pure-cancellation-three-sheet)
- [`tail-root-decimal-phase-lock.md`](#source-tail-root-decimal-phase-lock)
- [`tail-root-kappa-plus-g-crt-nogo.md`](#source-tail-root-kappa-plus-g-crt-nogo)
- [`tail-rough-angular-source-transfer.md`](#source-tail-rough-angular-source-transfer)
- [`tail-rough-bottom-angular-cyclotomic-split.md`](#source-tail-rough-bottom-angular-cyclotomic-split)
- [`tail-rough-bottom-small-factor-charge.md`](#source-tail-rough-bottom-small-factor-charge)
- [`tail-rough-canonical-payer-decomposition.md`](#source-tail-rough-canonical-payer-decomposition)
- [`tail-rough-cq-excess.md`](#source-tail-rough-cq-excess)
- [`tail-rough-d0-allocation.md`](#source-tail-rough-d0-allocation)
- [`tail-rough-gaussian-payer-split.md`](#source-tail-rough-gaussian-payer-split)
- [`tail-rough-general-transfer.md`](#source-tail-rough-general-transfer)
- [`tail-rough-projective-bottom-two-payer.md`](#source-tail-rough-projective-bottom-two-payer)
- [`tail-rough-third-angular-absorption.md`](#source-tail-rough-third-angular-absorption)
- [`tail-rough-z0-only-frontier.md`](#source-tail-rough-z0-only-frontier)
- [`tail-source-cancellation-transfer.md`](#source-tail-source-cancellation-transfer)

<a id="source-tail-hard-source-derivative-sheet"></a>

> 整合来源：`tail-hard-source-derivative-sheet.md`

# DD baseline-free `Q` cancellation 的 hard derivative sheet

> **依赖：** [`gcd-normal-exact-small-factor.md`](good-genuine-ledger.md#source-gcd-normal-exact-small-factor)、
> [`tail-pure-cancellation-three-sheet.md`](tail-allocation-ledger.md#source-tail-pure-cancellation-three-sheet)、
> `core.md` §17–18 的 DD gap discriminant `W=L Xi`。
>
> **严格状态：** `已严格完成（baseline-free rough cancellation primes）`。
>
> general exact small-factor normalization自动给出 universal square-core
> \[
> \boxed{LaG_0=2c_3\mu^2.}
> \]
> 在 baseline-free `p^c||Q` sheet中，`L,c_3` 都是 `p`-units，因此
> \[
> v_p(a)=v_p(\mu)=v_p(G_0)=:\rho.
> \]
> 将其与 three-sheet valuation ledger联立后，所有 source depth `c` 除一个
> sub-sheet外都有显式 payer。唯一真正 hard 的情况为
> \[
> \boxed{c>\rho,\qquad v_p(C)=\rho.}
> \]
> 此时
> \[
> \boxed{v_p(W)=v_p(\Xi)=c+\rho.}
> \]
> 而 DD §17 中的长记号其实满足 exact simplification
> \[
> \boxed{\mathcal M=q_{\rm lcm}C.}
> \]
> 因此 hard source prime最终等价于一个 normalized derivative congruence：
> \[
> \boxed{
> v_p(q_{\rm lcm}C-C_0a)=c+\rho,
> \quad
> v_p(C)=v_p(a)=\rho.
> }
> \]

---

## 1. universal gap square-core 不需要 `t_2=1`

`gcd-normal-exact-small-factor.md` 已证明

\[
\boxed{
F_-=L(u+2v)\,a\frac{g_*}{v},}
\tag{1.1}

其中 `L=r` 是 gcd-normal smooth tail factor。

另一方面 near-square definition为

\[
\boxed{
F_-=\frac{2(\kappa+2G)\mu^2}{G_0}.}
\tag{1.2}

使用

\[
\kappa+2G=\gamma(u+2v),
\qquad
\frac{g_*}{v}=\frac\gamma{c_3},
\]

比较 `(1.1),(1.2)` 并约去正因子 `gamma(u+2v)`：

\[
\boxed{
LaG_0=2c_3\mu^2.}
\tag{Gap-square-general}

这是整个 gcd-normal DD tail的 exact identity。

若再写

\[
c_3=\varepsilon c_0,
\qquad
a=c_0a_0,
\]

则也可化为

\[
\boxed{La_0G_0=2\varepsilon\mu^2.}
\tag{1.3}

canonical `t_2=1` 文件中的

\[
5^Ta_0G_0=s\varepsilon\mu^2
\]

只是使用 `L=2*5^T/s` 后的 specialization。

---

## 2. baseline-free prime 下 gap depth = `rho`

固定

\[
p\nmid10b_1b_2b_3,
\qquad p^c\Vert Q,
\quad c>0.
\]

`tail-pure-cancellation-three-sheet.md` 已证明

\[
v_p(\nu)=0,
\qquad
v_p(G_0)=v_p(\mu)=:\rho,
\qquad
v_p(\mathcal N_{12})=:n\ge\rho.
\tag{2.1}

这里 denominator 在 `p` 处全为 units，所以

\[
p\nmid c_3=q_{\rm lcm}/b_3.
\]

而 `L` 是 2,5-smooth，故 `p` 不整除 `L`。

对 `(Gap-square-general)` 取 `p`-valuation：

\[
v_p(a)+\rho=2\rho.
\]

因此

\[
\boxed{v_p(a)=\rho.}
\tag{Gap-rho}

---

## 3. three-sheet 中哪些已经支付 source depth

沿用前一文件

\[
t:=v_p(C),
\]

三个 divided-quadratic term valuations为

\[
2\rho,\qquad \rho+t,\qquad c+n.
\]

### 3.1 若 `rho>=c`

此时 source cancellation depth `c` 已经不超过 gap/norm depth `rho`。
从 height allocation角度，它已由

\[
\mu,\quad G_0,\quad a,\quad \mathcal N_{12}
\]

中的现有 `rho` baseline承担，不再是 unpaid `X_Q` excess。

### 3.2 `BD` sheet

`BD` 条件为

\[
\rho+t=c+n,
\qquad t\le\rho.
\]

由 `n>=rho` 得

\[
c\le t.
\]

所以

\[
\boxed{t\ge c.}
\]

原 source depth完整进入 numerator coefficient `C`。

### 3.3 `AD` sheet

`AD` 有

\[
c+n=2\rho.
\]

结合 `n>=rho`：

\[
\boxed{c\le\rho.}
\]

因此同样已经被 gap/norm baseline支付。

故若 source depth仍有真正 unpaid部分，只能在 `AB` sheet 且

\[
\boxed{c>\rho.}
\tag{Hard-condition}

`AB` 又强制

\[
\boxed{t=\rho.}
\tag{3.1}

这就是唯一 hard sub-sheet。

---

## 4. hard `AB` sheet 的 unified discriminant depth

写

\[
Q=p^cQ_0,
\qquad
\kappa=p^c\kappa_0,
\]

其中 `Q_0,kappa_0` 为 units。

unified discriminant为

\[
W^2
=\kappa\left(
\kappa K_{C,Q}-2GQ^2\mathcal N_{12}
\right),
\]

\[
K_{C,Q}=G^2C^2-Q^2\mathcal N_{12}.
\]

在 hard sheet

\[
v_p(C)=\rho,
\qquad c>\rho,
\qquad n\ge\rho.
\]

因此

\[
v_p(G^2C^2)=2\rho,
\]

而

\[
v_p(Q^2\mathcal N_{12})=2c+n>2\rho.
\]

所以

\[
\boxed{v_p(K_{C,Q})=2\rho.}
\tag{4.1}

discriminant inner bracket两项 valuations为

\[
c+2\rho,
\qquad
2c+n.
\]

其差

\[
(2c+n)-(c+2\rho)
=c+n-2\rho
>0
\]

因为 `c>rho`、`n>=rho`。

所以没有 inner cancellation：

\[
v_p\left(
\kappa K_{C,Q}-2GQ^2\mathcal N_{12}
\right)
=c+2\rho.
\]

最终

\[
\boxed{v_p(W^2)=2c+2\rho,}
\]

即

\[
\boxed{v_p(W)=c+\rho.}
\tag{W-hard}

---

## 5. `mathcal M` 的 exact simplification

DD gap quadratic使用

\[
\mathcal M
=10^d\left(10^{n_2}b_1y_1+b_2y_2\right).
\]

整数球面 ghost definitions为

\[
y_1=a_1q_{\rm lcm}/b_1,
\qquad
y_2=a_2q_{\rm lcm}/b_2.
\]

所以

\[
\begin{aligned}
\mathcal M
&=10^dq_{\rm lcm}
\left(a_1 10^{n_2}+a_2\right)\\
&=q_{\rm lcm}\,10^dA_{12}.
\end{aligned}
\]

而 DD coefficient正是

\[
C=10^dA_{12}.
\]

因此

\[
\boxed{\mathcal M=q_{\rm lcm}C.}
\tag{M-simple}

这条 identity此前被 ghost notation遮住，但完全是 exact algebra。

---

## 6. hard derivative congruence

DD §18 有

\[
\boxed{W=L\Xi,}
\qquad
\boxed{\Xi=|\mathcal M-C_0a|,}
\]

其中

\[
C_0=QL+2\tau.
\]

baseline-free prime满足 `p` 不整除 `L`。又 `Q` 含 `p^c` 而 `tau` 为
`p`-unit，所以

\[
\boxed{p\nmid C_0.}
\tag{6.1}

由 `(W-hard)`：

\[
\boxed{v_p(\Xi)=c+\rho.}
\tag{6.2}

使用 `(M-simple)`：

\[
\boxed{
 v_p(q_{\rm lcm}C-C_0a)=c+\rho.}
\tag{Derivative-hard}

由于 denominator在 `p` 处全为 units：

\[
p\nmid q_{\rm lcm}C_0.
\]

并且

\[
v_p(C)=v_p(a)=\rho.
\]

所以两项各自恰有 baseline depth `rho`，再发生完整额外 `c` 层 cancellation。

若定义

\[
C^{\circ}:=C/p^\rho,
\qquad
a^{\circ}:=a/p^\rho,
\]

则二者均为 `p`-units，并有

\[
\boxed{
q_{\rm lcm}C^{\circ}
\equiv
C_0a^{\circ}
\pmod{p^c}.}
\tag{Derivative-Hensel}

这才是 baseline-free source cancellation经过所有已有 payer剥离后留下的真正
normalized second contact。

---

## 7. 当前 source-cancellation frontier

一个 hard source prime现在必须**同时**满足两条深度 `c` 条件：

1. denominator prefix concat：
   \[
   p^c\mid Q=b_1 10^{m_2}+b_2;
   \]
2. normalized gap derivative：
   \[
   q_{\rm lcm}C^{\circ}
   \equiv C_0a^{\circ}\pmod{p^c}.
   \]

第二条不再等同于前一文件已经判死的 sphere complementary Hensel；它来自 unified
**discriminant derivative** `W=L Xi`，并在 hard `AB` sheet上有 exact extra depth
`c`。

下一步的正确任务是审计这两条 contact之间的 resultant：

- 若消元精确退回 coefficient plane / gap quadratic，则正式 no-go；
- 若产生一个 independent short integer，则 `X_Q` height终于可以被收费。

---

## 8. 状态摘要

- **`已严格完成`**：universal `Gap-square-general`、`Gap-rho`、hard sheet唯一性、
  `W-hard`、`M-simple`、`Derivative-Hensel`。
- **`结构压缩`**：baseline-free post-tail loss只剩 denominator concat + normalized
  discriminant derivative 的 simultaneous depth。
- **`待证`**：两 contact resultant / no-go；`X_Q` global height；post-tail branch
  reoptimization；DD global explicit slope / absolute height。

---

<a id="source-tail-pure-cancellation-hensel-nogo"></a>

> 整合来源：`tail-pure-cancellation-hensel-nogo.md`

# DD baseline-free `Q`-cancellation Hensel 的 sphere-collapse no-go

> **依赖：** [`tail-pure-cancellation-three-sheet.md`](tail-allocation-ledger.md#source-tail-pure-cancellation-three-sheet)、
> exact lift、unified gap definition与 sphere factorization。
>
> **严格状态：** `已严格完成（no-go audit）`。
>
> 前一文件把 baseline-free `p^c||Q` 的 unified quadratic压成 three-sheet Hensel
> partition。本文证明：其中看似最有希望的 deep unit-Hensel并不是独立 obstruction。
> 存在 exact identity
> \[
> \boxed{
> b_3(\kappa+2G)\mu
> -2\cdot10^mG^2C\nu
> =
> -10^mQG^2(\mathcal R+r_3)\nu,
> }
> \]
> 其中 DD coefficient `C=10^dA_12`。
> 因此所谓 Hensel depth精确等于 sphere complementary factor
> `R+r_3` 的已有深度。three-sheet ledger正确，但不能作为第二份独立高度收费。

---

## 1. DD coefficient `C` 就是前缀 numerator concat

统一 framework 在 DD 中定义

\[
C=10^{m_2+k_{12}}a_1+10^da_2.
\]

由于

\[
k_{12}=s_2+d,
\qquad
m_2+s_2=n_2,
\]

有

\[
m_2+k_{12}=n_2+d.
\]

所以

\[
\boxed{
C=10^d(a_1 10^{n_2}+a_2)
=10^dA_{12}.}
\tag{1.1}

因此

\[
\boxed{10^mC=10^{m+d}A_{12}=10^{n_3}A_{12}.}
\tag{1.2}

而完整 numerator concat为

\[
\boxed{\alpha=10^mC+a_3.}
\tag{1.3}

---

## 2. 先恢复一个 exact gap/concat identity

gap parameter定义

\[
\boxed{
\frac\mu\nu=G(\mathcal R-r_3).}
\tag{2.1}

乘 `b_3`：

\[
\frac{b_3\mu}{\nu}
=G(b_3\mathcal R-a_3).
\]

因此由 `(1.3)`：

\[
\begin{aligned}
\frac{b_3\mu}{\nu}-10^mGC
&=G(b_3\mathcal R-a_3-10^mC)\\
&=G(b_3\mathcal R-\alpha).
\end{aligned}
\]

exact lift给

\[
\mathcal R=\alpha/\beta,
\qquad
\beta=10^mQ+b_3.
\]

所以

\[
b_3\mathcal R-\alpha
=\alpha\left(\frac{b_3}{\beta}-1\right)
=-10^mQ\mathcal R.
\]

于是得到

\[
\boxed{
 b_3\mu-10^mGC\nu
=-10^mGQ\mathcal R\nu.
}
\tag{Gap-concat-parent}

---

## 3. `Unit-Hensel` parent精确等于 complementary sphere factor

考虑前一文件中出现的 linear combination

\[
\mathcal U
:=
 b_3(\kappa+2G)\mu
-2\cdot10^mG^2C\nu.
\]

展开第一项：

\[
\begin{aligned}
\mathcal U
&=b_3\kappa\mu
+2G(b_3\mu-10^mGC\nu).
\end{aligned}
\]

由 tail weight

\[
\boxed{b_3\kappa=10^mQG}
\tag{3.1}

以及 `(Gap-concat-parent)`：

\[
\begin{aligned}
\mathcal U
&=10^mQG\mu
-2\cdot10^mG^2Q\mathcal R\nu\\
&=10^mQG\nu
\left(\frac\mu\nu-2G\mathcal R\right).
\end{aligned}
\]

使用 `(2.1)`：

\[
\frac\mu\nu-2G\mathcal R
=G(\mathcal R-r_3)-2G\mathcal R
=-G(\mathcal R+r_3).
\]

故

\[
\boxed{
\mathcal U
=-10^mQG^2(\mathcal R+r_3)\nu.
}
\tag{Sphere-parent}

这是 exact rational identity；左边为整数，所以右边当然也是同一整数。

---

## 4. baseline-free prime 下 Hensel depth完全由 sphere 支付

回到

\[
p\nmid10b_1b_2b_3,
\qquad p^c\Vert Q,
\]

并沿用前一文件

\[
\rho=v_p(\mu)=v_p(G_0),
\qquad
v_p(\nu)=0,
\qquad
n=v_p(\mathcal N_{12})\ge\rho.
\]

因为 `p` 不整除 `G`，`(2.1)` 给

\[
\boxed{v_p(\mathcal R-r_3)=\rho.}
\tag{4.1}

sphere identity为

\[
(\mathcal R-r_3)(\mathcal R+r_3)
=r_1^2+r_2^2
=\frac{\mathcal N_{12}}{G^2}.
\]

所以

\[
\boxed{
v_p(\mathcal R+r_3)=n-\rho.}
\tag{4.2}

由 `(Sphere-parent)` 且 `nu,G` 为 units：

\[
\boxed{
v_p(\mathcal U)=c+n-\rho.}
\tag{4.3}

而前一文件 divided quadratic中的前两项有共同 `mu` factor；乘回 `mu`
后其和的 valuation为

\[
\rho+(c+n-\rho)=\boxed{c+n},
\]

正好等于第三项 forced valuation。

因此 three-sheet 中出现的 deep cancellation没有新增任何 `p`-adic height：

\[
\boxed{
\text{source }c
+\text{ complementary sphere depth }(n-\rho)
}
\]

已经精确解释全部 Hensel深度。

---

## 5. `rho=0` 的 unit-Hensel完全退化

尤其在最危险的

\[
\rho=0
\]

sheet：

\[
v_p(\mathcal R-r_3)=0,
\qquad
v_p(\mathcal R+r_3)=n.
\]

前一文件的

\[
Q_0(\kappa+2G)\mu
\equiv2G\kappa_0C\nu
\pmod{p^{c+n}}
\]

经 `kappa_0 b_3=10^mQ_0G` 清分母后，正是 `(Sphere-parent)` 模
`p^{c+n}` 的重写。

所以：

\[
\boxed{
\text{`Unit-Hensel` 不是独立 source carrier.}
}
\tag{Unit-Hensel-nogo}

不能把它与 sphere factorization再次相加收费。

---

## 6. 对 three-sheet 文件的正确定位

`tail-pure-cancellation-three-sheet.md` 的 valuation partition仍然严格正确：它准确描述
unified quadratic的 local tropical geometry。

但其用途应降级为：

- `AB/AD/BD` 是 sphere/gap depth在 quadratic 三项中的不同投影；
- 它们可以帮助 bookkeeping；
- **不能**被当作控制 primitive `Q` cancellation overflow `X_Q` 的第二份独立
Hensel obstruction。

因此 `X_Q` 的真正下一攻击必须来自 quadratic/sphere 之外的独立结构，例如：

1. full decimal concat / exact lift 的另一线性 carrier；
2. Gaussian orientation 不变量；
3. source cancellation prime的全局 product/parity；
4. 新的 Subspace/Ridout 输入。

---

## 7. 状态摘要

- **`已严格完成`**：`Gap-concat-parent`、`Sphere-parent`、valuation collapse。
- **`失效/降级`**：把 baseline-free `Unit-Hensel` 视为独立 obstruction或高度 payer。
- **`待证`**：真正独立的 `X_Q` source-cancellation control；post-tail global branch
reoptimization；DD absolute height / emptiness。

---

<a id="source-tail-pure-cancellation-three-sheet"></a>

> 整合来源：`tail-pure-cancellation-three-sheet.md`

# DD baseline-free primitive `Q` cancellation 的 three-sheet split

> **依赖：** [`tail-rough-cq-excess.md`](tail-allocation-ledger.md#source-tail-rough-cq-excess)、
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

---

<a id="source-tail-root-decimal-phase-lock"></a>

> 整合来源：`tail-root-decimal-phase-lock.md`

# DD tail-root × decimal remainder 的 2-adic phase lock

> **依赖：** [`genuine-tail-root-orientation-lock.md`](good-genuine-ledger.md#source-genuine-tail-root-orientation-lock) 的 global `Tail-root-original`、`frontier.md` 的 terminal primitive overlap / exact decimal remainder / prefix polarization、[`pairmax-fixed-a12-crt.md`](good-genuine-ledger.md#source-pairmax-fixed-a12-crt) 使用的 one-channel unit ledger。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。将 exact top residue 与 tail-root linearization 联立，可消去 `A_12,a_3`，得到模 `10^d` 的 W-only congruence
> \[
> \mathscr T R_0+\eta g_0U\gamma W\equiv0\pmod{10^d}.
> \]
> 对其做 2-adic valuation，并与 unified discriminant 的 2-adic valuation比较，严格推出
> \[
> H=2m+o(S),
> \qquad
> v_2(W)=m+o(S).
> \]
> 再由 `X=2^HZ` 与 `log X=2S+o(S)` 得
> \[
> \log Z=z_*S+o(S),
> \qquad z_*=0.308883577618\ldots,
> \]
> 恰与 `q_c` 的 frontier height相同。
>
> 本文仍不单独关闭 terminal frontier，但新增一个此前未显式记录的 source-height lock。

---

## 1. tail-root 与 decimal carry 消去 prefix

统一 tail-root original identity为

\[
\boxed{
\mathscr T a_3
=\kappa G^2 10^dA_{12}
+\eta(\kappa+G)W,
}
\tag{1.1}

其中

\[
\mathscr T
=\frac{\kappa^2(\kappa+2G)}{10^m}.
\tag{1.2}

exact carry为

\[
\boxed{
g_0Ua_3
=g_0B10^dVA_{12}-\Sigma R_0.}
\tag{1.3}

把 `(1.1)` 乘 `g_0U`，模 `10^d`：

\[
g_0U\mathscr T a_3
\equiv
\eta g_0U(\kappa+G)W
\pmod{10^d}.
\tag{1.4}

把 `(1.3)` 乘 `mathscr T`，同样模 `10^d`：

\[
g_0U\mathscr T a_3
\equiv
-\mathscr T\Sigma R_0
\pmod{10^d}.
\tag{1.5}

因此

\[
\mathscr T\Sigma R_0
+\eta g_0U(\kappa+G)W
\equiv0\pmod{10^d}.
\tag{1.6}

terminal primitive overlap给

\[
\boxed{\kappa+G=\gamma\Sigma.}
\tag{1.7}

又 `Sigma` 是 10-adic unit：

- `V=X-Y` 为 odd；
- `Y=5^TU` 为 odd；
- 因此 `X=V+Y` 为 even；
- `Sigma=X+Y` 为 odd；
- 模 `5`，`Sigma≡X` 且 `X` 为 5-unit。

所以

\[
(\Sigma,10)=1.
\]

可从 `(1.6)` 在模 `10^d` 中约去 `Sigma`：

\[
\boxed{
\mathscr T R_0
+\eta g_0U\gamma W
\equiv0\pmod{10^d}.}
\tag{Tail-decimal}

---

## 2. terminal 2-adic primitive overlap

写

\[
F:=5^T.
\]

terminal overlap为

\[
\boxed{
\kappa=2\gamma FU,
\qquad
G=\gamma V,
\qquad
\kappa+2G=2\gamma X,
}
\tag{2.1}

其中

\[
(UVZ,10)=1,
\qquad
X=2^HZ.
\]

令

\[
g_2:=v_2(\gamma).
\]

则

\[
\boxed{v_2(\kappa)=1+g_2,}
\tag{2.2}

\[
\boxed{v_2(G)=g_2,}
\tag{2.3}

\[
\boxed{v_2(\kappa+2G)=1+g_2+H.}
\tag{2.4}

所以

\[
\boxed{
v_2(\mathscr T)
=H-m+3+3g_2.}
\tag{2.5}

one-channel asymptotic还给

\[
\log\gamma=o(S),
\]

因为

\[
G=\gamma V,
\quad
\log G=S+o(S),
\quad
\log V=S+o(S).
\]

故

\[
\boxed{g_2=o(S).}
\tag{2.6}

同时

\[
\log g_0=\log R_0=o(S),
\qquad
v_2(U)=0.
\tag{2.7}

---

## 3. `Q` 与 `N_12` 的 2-depth 都只有 `o(S)`

prefix polarization给

\[
m_1=o(S),
\qquad
n_2=o(S),
\qquad
m_2=S+o(S).
\]

one-channel给

\[
b_2=C_L\cdot10^{o(S)}
\]

按 logarithmic height理解，而 `C_L` 为 odd prime-to-10 main core。因此

\[
\boxed{v_2(b_1)=v_2(b_2)=v_2(a_2)=o(S).}
\tag{3.1}

### 3.1 `Q`

\[
Q=b_1 10^{m_2}+b_2.
\]

第一项的 2-depth为

\[
m_2+v_2(b_1)=S+o(S),
\]

第二项只有 `o(S)`；sufficiently large frontier上两者 valuation不同，所以

\[
\boxed{v_2(Q)=v_2(b_2)=o(S).}
\tag{3.2}

### 3.2 `N_12`

写

\[
x=a_1b_2,
\qquad
y=a_2b_1,
\qquad
\mathcal N_{12}=x^2+y^2.
\]

由 `(3.1)` 与 `n_2,m_1=o(S)`：

\[
\boxed{v_2(y)=o(S).}
\]

对任意整数 `x,y` 有 elementary sum-of-two-squares valuation：

\[
v_2(x^2+y^2)
\le2\min(v_2(x),v_2(y))+1.
\]

故

\[
\boxed{v_2(\mathcal N_{12})=o(S).}
\tag{3.3}

---

## 4. unified discriminant 精确给 `v_2(W)=H/2+o(S)`

DD discriminant identity为

\[
\boxed{
W^2
=(\kappa G\mathscr C)^2
-Q^2\mathcal N_{12}\kappa(\kappa+2G),
}
\tag{4.1}

其中 DD coefficient

\[
\boxed{\mathscr C=10^dA_{12}.}
\tag{4.2}

第一项 2-depth至少为

\[
\begin{aligned}
v_2((\kappa G\mathscr C)^2)
&\ge2\bigl[(1+g_2)+g_2+d\bigr]\\
&=2d+2+4g_2\\
&=7S+o(S),
\end{aligned}
\tag{4.3}

因为 frontier

\[
\boxed{d=3.5S+o(S).}
\tag{4.4}

第二项利用 §§2--3：

\[
\begin{aligned}
v_2(Q^2\mathcal N_{12}\kappa(\kappa+2G))
&=2v_2(Q)+v_2(\mathcal N_{12})\\
&\quad +(1+g_2)+(1+g_2+H)\\
&=\boxed{H+o(S).}
\end{aligned}
\tag{4.5}

另一方面

\[
X=2^HZ>0,
\qquad
X<\Sigma,
\]

且 decimal remainder analysis已经给

\[
\log\Sigma=2S+o(S).
\]

因为 `Z>=1`：

\[
H\log_{10}2
\le2S+o(S),
\]

即

\[
\boxed{
H\le\frac{2}{\log_{10}2}S+o(S)
=6.643856189774\ldots S+o(S).}
\tag{4.6}

所以 `(4.5)` 与 `(4.3)` 存在严格线性 gap：

\[
H+o(S)<7S+o(S).
\]

两项 2-adic valuations最终不同；对整数差，valuation等于较小者。因此

\[
2v_2(W)=H+o(S),
\]

即

\[
\boxed{v_2(W)=\frac H2+o(S).}
\tag{W2}

---

## 5. `Tail-decimal` 强迫两项 2-depth相等

对 `(Tail-decimal)` 两项记

\[
r:=v_2(\mathscr T R_0),
\qquad
s:=v_2(g_0U\gamma W).
\]

由 `(2.5)`--`(2.7)`：

\[
\boxed{r=H-m+o(S).}
\tag{5.1}

由 `(W2)`：

\[
\boxed{s=\frac H2+o(S).}
\tag{5.2}

而 `(Tail-decimal)` 要求

\[
2^d\mid \mathscr T R_0+\eta g_0U\gamma W.
\]

先排除

\[
\min(r,s)\ge d.
\]

若成立，则特别有

\[
s\ge d,
\]

故

\[
\frac H2\ge3.5S-o(S),
\]

即

\[
H\ge7S-o(S),
\]

与 `(4.6)` 矛盾。

因此

\[
\boxed{\min(r,s)<d.}
\tag{5.3}

若 `r!=s`，则 two-adic valuation of the sum等于 `min(r,s)<d`，又与 `2^d` divisibility矛盾。

所以必须

\[
\boxed{r=s.}
\tag{5.4}

代入 `(5.1)`--`(5.2)`：

\[
H-m=\frac H2+o(S).
\]

因此

\[
\boxed{H=2m+o(S).}
\tag{H-lock}

并由 `(W2)`：

\[
\boxed{v_2(W)=m+o(S).}
\tag{W2-lock}

---

## 6. `Z` 与 `q_c` 高度精确对齐

由

\[
\Sigma=X+Y,
\qquad
V=X-Y,
\]

有

\[
X=\frac{\Sigma+V}{2}.
\]

frontier

\[
\log\Sigma=2S+o(S),
\qquad
\log V=S+o(S),
\]

所以

\[
\boxed{\log X=2S+o(S).}
\tag{6.1}

又

\[
X=2^HZ,
\]

故

\[
\log Z
=2S-H\log_{10}2+o(S).
\]

使用 `(H-lock)` 与

\[
\frac mS\to2.808883577618\ldots:
\]

\[
\begin{aligned}
\frac{\log Z}{S}
&=2-2(2.808883577618\ldots)\log_{10}2+o(1)\\
&=\boxed{0.308883577618\ldots+o(1).}
\end{aligned}
\]

所以

\[
\boxed{
\log Z=z_*S+o(S),
\qquad
z_*=0.308883577618\ldots.}
\tag{Z-lock}

而已有

\[
\log q_c=z_*S+o(S).
\]

因此得到新的 exact leading-height symmetry：

\[
\boxed{
\log Z=\log q_c+o(S).}
\tag{Z-qc-lock}

---

## 7. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`Tail-decimal`、`v_2(Q)=o(S)`、`v_2(N_12)=o(S)`、`W2`、`H-lock`、`W2-lock`、`Z-lock`。
- **`新 frontier 约束`**：`H=2m+o(S)` 与 `log Z=log q_c+o(S)`。
- **`待证`**：利用 `Z/q_c` 同高度与 denominator/source orientation 构造新的 strict source relation；5-adic projection的剩余 unit phase；DD frontier emptiness。

---

<a id="source-tail-root-kappa-plus-g-crt-nogo"></a>

> 整合来源：`tail-root-kappa-plus-g-crt-nogo.md`

# DD tail-root `kappa+G` fixed-CRT route 的 exact collapse

> **依赖：** [`genuine-tail-root-orientation-lock.md`](good-genuine-ledger.md#source-genuine-tail-root-orientation-lock) 的 `Tail-root-original`、`frontier.md` 的 exact carry 与 terminal primitive overlap。
>
> **严格状态：** `失效/降级（已严格证明退化）`。将 tail-root linear identity 与 decimal carry联立，表面上会产生一个模 `kappa+G` 的 fixed `A_12` congruence。由于 `kappa+G` 具有约 `QG` 尺度，这看起来像一个潜在第三大 period。本文证明 terminal primitive overlap使其 coefficient **精确含整个 `kappa+G`**：
> \[
> \mathscr T BV-U\kappa G^2
> =U\kappa G(\kappa+G).
> \]
> 因此该 congruence 中 `A_12` 项模 `kappa+G` 恒为零，只剩旧 common-factor condition；effective `A_12` period 为零。

---

## 1. candidate congruence

沿用

\[
D:=10^d,
\qquad F:=5^T,
\qquad T_3:=10^{m_3}.
\]

全局 tail-root linear identity为

\[
\boxed{
\mathscr T a_3
=\kappa G^2D A_{12}
+\eta(\kappa+G)W,
}
\tag{1.1}

其中

\[
\boxed{
\mathscr T
=\frac{\kappa^2(\kappa+2G)}{T_3}.
}
\tag{1.2}

exact carry为

\[
\boxed{
g_0Ua_3
=g_0BDVA_{12}-\Sigma R_0.}
\tag{1.3}

把 `(1.3)` 代入 `(1.1)` 并乘 `g_0U`：

\[
\mathscr T(g_0BDVA_{12}-\Sigma R_0)
=g_0U\kappa G^2DA_{12}
+\eta g_0U(\kappa+G)W.
\]

整理：

\[
\boxed{
g_0D(\mathscr T BV-U\kappa G^2)A_{12}
-\mathscr T\Sigma R_0
=\eta g_0U(\kappa+G)W.}
\tag{Candidate-exact}

所以形式上有

\[
\boxed{
g_0D(\mathscr T BV-U\kappa G^2)A_{12}
\equiv\mathscr T\Sigma R_0
\pmod{\kappa+G}.}
\tag{Candidate-CRT}

---

## 2. coefficient 的第一层化简

terminal smooth relation为

\[
\boxed{\frac{T_3}{B}=2F.}
\tag{2.1}

因此

\[
\begin{aligned}
\mathscr T BV-U\kappa G^2
&=\frac{\kappa^2(\kappa+2G)}{T_3}BV
-U\kappa G^2\\
&=\frac{\kappa}{2F}
\left[\kappa(\kappa+2G)V-2FUG^2\right].
\end{aligned}
\tag{2.2}

又

\[
\Sigma=V+2FU.
\]

故括号可写成

\[
\begin{aligned}
\kappa(\kappa+2G)V-2FUG^2
&=V\left[\kappa(\kappa+2G)+G^2\right]-G^2\Sigma\\
&=\boxed{V(\kappa+G)^2-G^2\Sigma}.
\end{aligned}
\tag{2.3}

所以

\[
\boxed{
\mathscr T BV-U\kappa G^2
=\frac{\kappa}{2F}
\left[V(\kappa+G)^2-G^2\Sigma\right].}
\tag{2.4}

仅看这一步，似乎 `kappa+G` 还可能留下大 period；terminal primitive overlap会把它完全消掉。

---

## 3. terminal primitive overlap

frontier 已有

\[
\gamma=(\kappa,G),
\qquad
\kappa=\gamma u,
\qquad
G=\gamma v,
\qquad
(u,v)=1,
\]

并在 terminal primitive overlap 中精确识别

\[
\boxed{u=2FU,\qquad v=V.}
\tag{3.1}

因此

\[
\boxed{
\kappa=2\gamma FU,
\qquad
G=\gamma V.}
\tag{3.2}

特别地

\[
\boxed{
\kappa+G
=\gamma(2FU+V)
=\gamma\Sigma.}
\tag{KplusG}

同理还顺带有

\[
\boxed{
\kappa+2G
=2\gamma(FU+V)
=2\gamma X,}
\tag{Kplus2G}

因为 `X=FU+V`。

这两式说明 unified tail factors本身就是 terminal S-unit phase的缩放，不是新的独立 moving moduli。

---

## 4. candidate coefficient 精确含整个 modulus

把 `(3.2)` 与 `(KplusG)` 代入 `(2.4)`。更直接地，从 `(2.2)`：

\[
\begin{aligned}
\frac{\kappa^2(\kappa+2G)}{T_3}BV
&=\kappa\frac{\kappa}{2F}(\kappa+2G)V\\
&=\kappa(\gamma U)(\kappa+2G)V\\
&=U\kappa G(\kappa+2G),
\end{aligned}
\]

因为

\[
\frac\kappa{2F}=\gamma U,
\qquad
\gamma V=G.
\]

所以

\[
\begin{aligned}
\mathscr T BV-U\kappa G^2
&=U\kappa G(\kappa+2G)-U\kappa G^2\\
&=\boxed{U\kappa G(\kappa+G).}
\end{aligned}
\tag{Coefficient-collapse}

这是 exact integer identity。

因此 `(Candidate-exact)` 其实为

\[
\boxed{
g_0DU\kappa G(\kappa+G)A_{12}
-\mathscr T\Sigma R_0
=\eta g_0U(\kappa+G)W.}
\tag{4.1}

模 `kappa+G` 后，`A_12` 项完全消失：

\[
\boxed{
\mathscr T\Sigma R_0
\equiv0\pmod{\kappa+G}.}
\tag{4.2}

所以 `(Candidate-CRT)` 对 `A_12` 的 effective period正好为

\[
\boxed{1.}
\tag{Zero-period}

---

## 5. 剩余 divisibility 只是 common-factor condition

由 `(KplusG)`：

\[
\kappa+G=\gamma\Sigma.
\]

于是 `(4.2)` 约去显式 `Sigma` 后只要求

\[
\boxed{\gamma\mid\mathscr T R_0}
\tag{5.1}

在相应 integer quotient意义下成立。

这不再含 `A_12`，只能作为已有 terminal common-factor ledger 的一部分；不能与 `C_L` / `q_c^2` CRT再叠加成第三 decimal period。

---

## 6. 方法含义

此前最诱人的第三 fixed modulus候选有：

\[
\kappa+G\asymp QG.
\]

若只看 `Tail-root-original` 与 carry，它似乎会给一个很大的 `A_12` period。但 exact terminal identification

\[
\kappa+G=\gamma\Sigma
\]

和 `(Coefficient-collapse)` 说明：

\[
\boxed{
\text{`kappa+G` 的全部 moving modulus
已经位于 coefficient 中；}
\text{它对 decimal prefix没有剩余 period。}}
\]

所以后续不得把 `(Candidate-CRT)` 计作第三 independent residue。

同时 `(KplusG)/(Kplus2G)` 解释了这个退化为何是结构性的：`kappa+G` 与 `kappa+2G` 分别就是 S-unit sum `Sigma` 与 `2X` 的 `gamma`-倍数。

---

## 7. 状态摘要

- **`已严格完成`**：`Candidate-exact`、coefficient 两级化简、`kappa+G=gamma Sigma`、`kappa+2G=2gamma X`、`Coefficient-collapse`。
- **`失效/降级`**：把 `kappa+G` 当作第三 fixed `A_12` period；其 effective prefix period为零。
- **`待证`**：split-independent `C_L q_c^2` unique lift的 Archimedean location；真正独立第三 residue若存在；DD frontier emptiness。

---

<a id="source-tail-rough-angular-source-transfer"></a>

> 整合来源：`tail-rough-angular-source-transfer.md`

# DD rough Gaussian payer 的 source-to-numerator orientation transfer

> **依赖：** [`tail-rough-gaussian-payer-split.md`](tail-allocation-ledger.md#source-tail-rough-gaussian-payer-split)、
> [`tail-rough-general-transfer.md`](tail-allocation-ledger.md#source-tail-rough-general-transfer)。
>
> **严格状态：** `已严格完成（整个 `X_Q` odd rough support）`。
>
> 上一文件把 post-tail rough loss写成
> \[
> X_Q\mid
> \operatorname{core}_{10}(C)^2
> \operatorname{core}_{10}(N_{\rm ang})
> \operatorname{core}_{10}(Z_0a),
> \]
> 其中 `N_ang` 已是 primitive split-Gaussian norm，但仍含 primitive denominator
> blocks `B_1,B_2`。本文利用 source cancellation本身把这份 orientation继续转移到
> 一个**纯 numerator norm**。
>
> 令
> \[
> g_n=(a_1,a_2),
> \qquad \bar a_i=a_i/g_n,
> \]
> 并定义
> \[
> \boxed{
> N_{\rm num}
> :=(\bar a_1 10^{m_2})^2+\bar a_2^2.
> }
> \]
> 则逐 `p|X_Q` 的 source/angular contact给同向 Gaussian transfer，最终得到
> \[
> \boxed{
> X_Q\mid
> \operatorname{core}_{10}(C)^2\,
> \operatorname{core}_{10}(N_{\rm num})\,
> \operatorname{core}_{10}(Z_0a).
> }
> \tag{Numerator-transfer}
> \]
> 此外若
> \[
> A^\circ:=A_{12}/g_n
> =\bar a_1 10^{n_2}+\bar a_2,
> \]
> 则 numerator coefficient与 Gaussian norm的 rough overlap受一个纯 decimal
> cyclotomic factor控制：
> \[
> \boxed{
> \operatorname{core}_{10}\gcd(A^\circ,N_{\rm num})
> \mid 10^{2|s_2|}+1,
> \qquad s_2=n_2-m_2.
> }
> \tag{Cyclotomic-overlap}
> \]
> 因而 `C` 与 `N_num` 也不是两个完全自由的 rough pools。

---

## 1. cross numerator common gcd 恰是 `(a_1,a_2)`

沿用
\[
b_i=h_{12}B_i,
\qquad(B_1,B_2)=1.
\]
定义
\[
X=a_1B_2,
\qquad Y=a_2B_1.
\]
上一文件写
\[
g_A=(X,Y).
\]
本文先证明
\[
\boxed{g_A=g_n:=(a_1,a_2).}
\tag{1.1}

显然 `g_n|g_A`。反过来，固定 prime `p|g_A`。若 `p` 不同时整除
`a_1,a_2`，则从
\[
p|a_1B_2,\qquad p|a_2B_1
\]
只能落入以下三种可能之一：

1. `p|B_1,B_2`，与 `(B_1,B_2)=1` 矛盾；
2. `p|a_1,B_1`，与 reducedness `(a_1,b_1)=1` 矛盾；
3. `p|a_2,B_2`，与 reducedness `(a_2,b_2)=1` 矛盾。

故必有 `p|min(a_1,a_2)`，并且逐 exponent同样成立。于是 `(1.1)` 成立。

因此
\[
\boxed{
N_{\rm ang}
=(\bar a_1B_2)^2+(\bar a_2B_1)^2,
}
\tag{1.2}
且两坐标互素。

---

## 2. source cancellation 给 exact Gaussian linear identity

primitive denominator concat为
\[
C_Q=B_1 10^{m_2}+B_2.
\]
定义两个 Gaussian integers
\[
\boxed{
Z_{\rm ang}:=\bar a_1B_2+i\bar a_2B_1,
}
\tag{2.1}
\]
\[
\boxed{
Z_{\rm num}:=-\bar a_1 10^{m_2}+i\bar a_2.
}
\tag{2.2}
\]
则直接展开得到
\[
\boxed{
Z_{\rm ang}-B_1Z_{\rm num}
=\bar a_1 C_Q.
}
\tag{Source-angular-linear}

其 norms分别为
\[
N(Z_{\rm ang})=N_{\rm ang},
\]
\[
\boxed{
N(Z_{\rm num})=N_{\rm num}
=(\bar a_1 10^{m_2})^2+\bar a_2^2.
}
\tag{2.3}

由于 `(\bar a_1,\bar a_2)=1`，`N_num` 的 odd non-decimal prime support同样全部是
`1 mod 4` split primes。

---

## 3. same-orientation transfer

固定
\[
p\mid X_Q.
\]
前一文件已证明
\[
p\nmid10B_1B_2.
\tag{3.1}
\]
写
\[
c=v_p(C_Q)>0,
\qquad
\omega=v_p(N_{\rm ang}).
\]
若 `omega=0` 本节无事可做。以下设 `omega>0`。

因为 `Z_ang` 的两个实坐标互素，`p|N_ang` 强迫
\[
p\equiv1\pmod4.
\]
在 `Z[i]` 中写
\[
p=\pi\bar\pi.
\]
primitive 性保证 `pi` 与 `bar pi` 不可能同时整除 `Z_ang`；故交换共轭后唯一有
\[
\boxed{\pi^\omega\mid Z_{\rm ang}.}
\tag{3.2}

另一方面 `p^c|C_Q` 作为 rational integer意味着
\[
\pi^c\bar\pi^c\mid C_Q.
\]
`(3.1)` 还给 `B_1` 为 `pi`-unit。把 `(Source-angular-linear)` 模
`pi^min(c,omega)` 观察：
\[
\boxed{
\pi^{\min(c,\omega)}\mid Z_{\rm num}.
}
\tag{Orientation-transfer}

因此取 norm：
\[
\boxed{
v_p(N_{\rm num})\ge\min(c,\omega).}
\tag{3.3}

这里保存的是同一 Gaussian orientation，而不只是 ordinary norm divisibility。

---

## 4. 消去 `N_ang` payer

固定 `p|X_Q`，记
\[
x=v_p(X_Q),
\quad t=v_p(C),
\quad g=v_p(g_n),
\quad \omega=v_p(N_{\rm ang}),
\quad r=v_p(R_3^{\rm den}),
\]
\[
u=v_p(N_{\rm num}).
\]
由上一文件：
\[
\boxed{x\le\max(t,2g+\omega,r),}
\tag{4.1}
\]
并且
\[
\boxed{g\le t.}
\tag{4.2}
又由 `x_p<=c` 显然有
\[
\boxed{x\le c.}
\tag{4.3}

我们证明
\[
\boxed{x\le2t+r+u.}
\tag{4.4}

若 `(4.1)` 的最大值由 `t` 或 `r` 支付，则显然成立。
只需考虑
\[
x\le2g+\omega.
\]
若已经 `x<=2t+r` 也结束。否则
\[
x>2t+r\ge2g,
\]
故
\[
\omega\ge x-2g>0.
\]
由 `(3.3),(4.3)`：
\[
u\ge\min(c,\omega)
\ge x-2g.
\]
所以
\[
2t+r+u
\ge2t+r+x-2g
\ge x.
\]
证明 `(4.4)`。

逐 prime相乘，并注意 `X_Q` 只含 odd non-decimal primes：
\[
\boxed{
X_Q\mid
\operatorname{core}_{10}(C)^2
\operatorname{core}_{10}(R_3^{\rm den})
\operatorname{core}_{10}(N_{\rm num}).
}
\tag{4.5}

再用
\[
\operatorname{core}_{10}(R_3^{\rm den})\mid Z_0a
\]
得到
\[
\boxed{
X_Q\mid
\operatorname{core}_{10}(C)^2
\operatorname{core}_{10}(N_{\rm num})
\operatorname{core}_{10}(Z_0a).
}
\tag{Numerator-transfer}

这样 denominator-dependent `N_ang` 已从最终 payer list中消失。

---

## 5. coefficient / numerator norm overlap只来自 `10^{2|s_2|}+1`

定义
\[
\boxed{
A^\circ:=A_{12}/g_n
=\bar a_1 10^{n_2}+\bar a_2.
}
\tag{5.1}
因为 `g_n|(a_1,a_2)`，这是整数；且
\[
(A^\circ,\bar a_1)=1
\tag{5.2}
\]
由 `(\bar a_1,\bar a_2)=1` 立即成立。

模 `A^circ` 有
\[
\bar a_2\equiv-\bar a_1 10^{n_2}.
\]
因此
\[
\begin{aligned}
N_{\rm num}
&=\bar a_1^2 10^{2m_2}+\bar a_2^2\\
&\equiv
\bar a_1^2
\left(10^{2m_2}+10^{2n_2}\right)
\pmod{A^\circ}.
\end{aligned}
\tag{5.3}

固定 `p\nmid10` 且
\[
p^r\mid(A^\circ,N_{\rm num}).
\]
由 `(5.2)` 有 `p\nmid\bar a_1`，所以 `(5.3)` 给
\[
p^r\mid10^{2m_2}+10^{2n_2}.
\]
抽掉 `10^{2min(m_2,n_2)}` 这个 `p`-unit：
\[
\boxed{
p^r\mid10^{2|n_2-m_2|}+1.}
\]
而
\[
s_2=n_2-m_2.
\]
逐 rough primes相乘得到
\[
\boxed{
\operatorname{core}_{10}\gcd(A^\circ,N_{\rm num})
\mid10^{2|s_2|}+1.
}
\tag{Cyclotomic-overlap}

这说明 numerator coefficient `C=10^dg_nA^circ` 与 `N_num` 的 primitive
concat部分若想同时支付同一 rough prime，其共同深度必须进入一个完全显式的 decimal
cyclotomic carrier。

---

## 6. 当前 side-branch payer list

post-tail rough loss现在有
\[
\boxed{
X_Q\mid
\operatorname{core}_{10}(C)^2
\operatorname{core}_{10}(N_{\rm num})
\operatorname{core}_{10}(Z_0a),
}
\]
其中：

1. `C=10^dA_12` 的 rough part来自普通 numerator prefix concat；
2. `N_num=(bar a_1 10^{m_2})^2+bar a_2^2` 是纯 numerator primitive Gaussian norm；
3. `Z_0a` 是 projective denominator / sphere gap；
4. `A^circ` 与 `N_num` 的 rough overlap被 `10^(2|s_2|)+1` 控制。

所以 non-canonical dominant branch reoptimization已经从 denominator source gcd问题转成
**三个 numerator/projective carriers及其 overlap**。特别地 split-Gaussian orientation现在有一个
不含 denominator blocks 的 canonical reader `Z_num`。

---

## 7. 状态摘要

- **`已严格完成`**：`g_A=g_n`、`Source-angular-linear`、same-orientation transfer。
- **`已严格完成`**：`Numerator-transfer`。
- **`已严格完成`**：`Cyclotomic-overlap`。
- **`结构压缩`**：独立 Gaussian payer已变成纯 numerator norm `N_num`，其与 primitive
  numerator concat的 rough overlap由 explicit `10^(2|s_2|)+1` 支付。
- **`待证`**：`N_num` 与 projective carrier的 simultaneous orientation；把三个 payer的
  height喂回 second-Schmidt inequality；完成 non-canonical dominant branch reoptimization；
  DD global explicit `<=6` / absolute height。

---

<a id="source-tail-rough-bottom-angular-cyclotomic-split"></a>

> 整合来源：`tail-rough-bottom-angular-cyclotomic-split.md`

# DD residual bottom / Gaussian-angular payer 的 cyclotomic sheet split

> **依赖：** [`tail-rough-canonical-payer-decomposition.md`](tail-allocation-ledger.md#source-tail-rough-canonical-payer-decomposition)、
> [`tail-rough-third-angular-absorption.md`](tail-allocation-ledger.md#source-tail-rough-third-angular-absorption)、
> [`tail-rough-angular-source-transfer.md`](tail-allocation-ledger.md#source-tail-rough-angular-source-transfer)。
>
> **严格状态：** `已严格完成（整个 `X_Q` odd rough support）`。
>
> 前两步已经把 post-tail hard loss写成 projective layer、bottom layer、common numerator
> layer与 residual Gaussian layer。本文进一步抽掉 bottom 与 Gaussian 的共同 primitive
> numerator depth。最终得到 exact exponent-layer factorization
> \[
> \boxed{
> X_Q=X_P\,X_C\,D_{BA}^{\,2}\,B_0A_0,
> }
> \tag{Cyclotomic-normal-form}
> \]
> 其中
> \[
> \boxed{X_P\mid\operatorname{core}_{10}(Z_0a),}
> \]
> \[
> \boxed{X_C\mid\operatorname{core}_{10}(a_1,a_2)^2,}
> \]
> \[
> \boxed{D_{BA}\mid10^{2|s_2|}+1,}
> \]
> 并且
> \[
> \boxed{(B_0,A_0)=1.}
> \]
> `B_0` 是 primitive bottom-only leftover，`A_0` 是 residual split-Gaussian-only
> leftover。也就是说，bottom 与 Gaussian 若在同一 rough prime上同时线性深，重叠部分
> 必须由显式 decimal cyclotomic carrier支付；除掉这部分后二者 prime support互斥。

---

## 1. 从 third-angular absorption后的 local layers开始

对每个
\[
p^x\Vert X_Q
\]
`tail-rough-canonical-payer-decomposition.md` 给
\[
x=e_3+e_B+e_G+e_A.
\]
`tail-rough-third-angular-absorption.md` 又把 `r>0` support上的 `e_3+e_A`
合并进 projective reader。记
\[
e_P:=e_3+e_{A,3},
\]
其中 `e_{A,3}=e_A` 当 `r>0`，否则为 0；并记 residual angular
\[
e_{A,0}:=e_A-e_{A,3}.
\]
于是逐 prime
\[
\boxed{x=e_P+e_B+e_G+e_{A,0}.}
\tag{1.1}
且
\[
\boxed{p^{e_P}\mid Z_0a.}
\tag{1.2}
此外
\[
e_{A,0}>0\Longrightarrow r=0.
\tag{1.3}

---

## 2. bottom depth中先抽一份 common numerator scale

令
\[
g_n=(a_1,a_2),
\qquad g:=v_p(g_n).
\]
定义 primitive numerator concat
\[
A^\circ=A_{12}/g_n.
\]
因为 `p` 不整除 10：
\[
\boxed{
v_p(C)=v_p(A_{12})=g+v_p(A^\circ).}
\tag{2.1}

bottom layer满足
\[
e_B\le v_p(C).
\]
定义
\[
\boxed{e_{B,g}:=\min(e_B,g),}
\tag{2.2}
\]
\[
\boxed{e_B^\circ:=e_B-e_{B,g}.}
\tag{2.3}
显然
\[
\boxed{e_B^\circ\le v_p(A^\circ).}
\tag{2.4}

另一方面原 common layer有
\[
e_G\le g.
\]
所以定义总 common-square layer
\[
\boxed{e_C:=e_{B,g}+e_G,}
\tag{2.5}
立刻有
\[
\boxed{e_C\le2g.}
\tag{2.6}

逐 prime将 `(1.1)` 重写为
\[
\boxed{x=e_P+e_C+e_B^\circ+e_{A,0}.}
\tag{2.7}

---

## 3. primitive bottom / angular overlap进入 cyclotomic carrier

`tail-rough-angular-source-transfer.md` 已证明
\[
\boxed{
\operatorname{core}_{10}\gcd(A^\circ,N_{\rm num})
\mid10^{2|s_2|}+1.
}
\tag{3.1}
其中
\[
N_{\rm num}
=(\bar a_1 10^{m_2})^2+\bar a_2^2.
\]

residual angular layer满足
\[
\boxed{e_{A,0}\le v_p(N_{\rm num}).}
\tag{3.2}
结合 `(2.4)`，定义 local overlap
\[
\boxed{d_p:=\min(e_B^\circ,e_{A,0}).}
\tag{3.3}
则
\[
d_p\le v_p(A^\circ),
\qquad d_p\le v_p(N_{\rm num}),
\]
所以由 `(3.1)`：
\[
\boxed{
p^{d_p}\mid10^{2|s_2|}+1.}
\tag{Cyclotomic-local}

定义剩余单侧 layers
\[
\boxed{b_p:=e_B^\circ-d_p,}
\qquad
\boxed{a_p:=e_{A,0}-d_p.}
\tag{3.4}
由 `d_p=min(...)`：
\[
\boxed{\min(a_p,b_p)=0.}
\tag{3.5}
这就是 bottom / angular 的 two-sheet residue：抽掉 cyclotomic overlap后，每个 prime只能留在一侧。

---

## 4. global canonical factors

定义
\[
X_P:=\prod_{p|X_Q}p^{e_P(p)},
\]
\[
X_C:=\prod_{p|X_Q}p^{e_C(p)},
\]
\[
D_{BA}:=\prod_{p|X_Q}p^{d_p},
\]
\[
B_0:=\prod_{p|X_Q}p^{b_p},
\qquad
A_0:=\prod_{p|X_Q}p^{a_p}.
\]
由 `(2.7)` 与 `(3.4)`：
\[
\boxed{
X_Q=X_PX_CD_{BA}^2B_0A_0.
}
\tag{Cyclotomic-normal-form}

各 payer满足：

### projective/gap
由 third-angular absorption：
\[
\boxed{X_P\mid\operatorname{core}_{10}(Z_0a).}
\tag{4.1}

### common numerator square
由 `(2.6)`：
\[
\boxed{X_C\mid\operatorname{core}_{10}(g_n)^2.}
\tag{4.2}

### bottom/angular overlap
由 `(Cyclotomic-local)`：
\[
\boxed{D_{BA}\mid10^{2|s_2|}+1.}
\tag{4.3}
（`D_BA` 本身无 2、5 primes，因此不必再取 `core_10`。）

### one-sided residuals
由定义：
\[
\boxed{B_0\mid\operatorname{core}_{10}(A^\circ),}
\tag{4.4}
\[
\boxed{A_0\mid\operatorname{core}_{10}(N_{\rm num}).}
\tag{4.5}
并由 `(3.5)`：
\[
\boxed{(B_0,A_0)=1.}
\tag{4.6}

此外原 bottom reader仍给
\[
B_0\mid X_B\mid C_{12}\mid R_{12}
\]
在对应 exponent layers上的整除，因此 `B_0` 保留 genuine bottom-carrier语义；`A_0`
保留 numerator Gaussian orientation语义。

---

## 5. 基本 height caps

这一步还未完成 final LP，但已经给几条无条件 cap。

### common numerator
因为
\[
g_n\le\min(a_1,a_2),
\]
且 DD `d`-dominant surplus simplex有
\[
n_1+n_2=S+s_1+s_2\le S+2,
\]
所以
\[
\boxed{
\log_{10}X_C
\le2\log_{10}g_n
\le S+O(1).
}
\tag{5.1}

### primitive bottom
\[
B_0\mid A^\circ,
\]
且
\[
A^\circ=A_{12}/g_n<10^{n_1+n_2}/g_n,
\]
故
\[
\boxed{
\log_{10}B_0
\le S-\log_{10}g_n+O(1).
}
\tag{5.2}

同时 `B_0` 还是 bottom reader `R_12` 的 divisor。

### cyclotomic overlap
\[
\boxed{
\log_{10}D_{BA}
\le2|s_2|+O(1).
}
\tag{5.3}

### residual Gaussian
`A_0|N_num`，而
\[
N_{\rm num}
=(\bar a_1 10^{m_2})^2+\bar a_2^2,
\]
所以其 height由纯 numerator digit shape控制；后续应与 `(B_0,A_0)=1` 和 projective
layer联立，而不是把 `log N_num` 全额当独立 loss。

---

## 6. 对 branch reoptimization 的意义

第二次 Schmidt要求 rough mass约为 `S`。经过当前链条：
\[
\text{anonymous }X_Q
\rightsquigarrow
X_P\,X_C\,D_{BA}^2\,B_0A_0,
\]
其中：

- `X_P` 是单一 projective/gap reader；
- `X_C` 是 numerator common square，最多由前两 numerator共同位数支付；
- bottom / Gaussian simultaneous same-prime depth已被显式 cyclotomic integer
  `10^{2|s_2|}+1` 抽掉；
- 剩余 `B_0,A_0` **互素**，分别落在 bottom 与 Gaussian sheets。

因此下一 LP 不再需要给 `C_Q` 一个自由 `S` 高度。真正未知只剩：

1. `X_P` 的 global height；
2. coprime one-sided leftovers `B_0,A_0` 能否同时线性大；
3. `s_2` cyclotomic budget与 surplus simplex如何联立。

---

## 7. 状态摘要

- **`已严格完成`**：bottom common/primitive split、`Cyclotomic-local`。
- **`已严格完成`**：`Cyclotomic-normal-form`、`(B_0,A_0)=1`。
- **`结构压缩`**：post-tail hard rough loss被压成 projective、common-square、explicit cyclotomic 与两个互素 one-sided sheets。
- **`待证`**：`X_P/B_0/A_0` simultaneous height；post-tail branch reoptimization；DD global explicit `<=6` / absolute height。

---

<a id="source-tail-rough-bottom-small-factor-charge"></a>

> 整合来源：`tail-rough-bottom-small-factor-charge.md`

# DD post-tail bottom payer 的 exact small-factor charge

> **依赖：** [`tail-rough-projective-bottom-two-payer.md`](tail-allocation-ledger.md#source-tail-rough-projective-bottom-two-payer)、
> `core.md` 的 decimal determinant `E` 与 universal identity
> \[
> F_-Q(\kappa+G)=E\kappa(\kappa+2G).
> \]
>
> **严格状态：** `已严格完成（整个 `X_B` support）`。
>
> two-payer theorem写
> \[
> X_Q=X_PX_B,
> \qquad
> X_P\mid Z_0a,
> \qquad
> X_B\mid C_{12}:=(A_{12},Q).
> \]
> 本文证明 bottom payer `X_B` 其实已经被真实 small factor `F_-` 支付，并且带一整份
> prefix denominator product `G=b_1b_2` 的折扣：
> \[
> \boxed{X_BG<F_-.}
> \tag{Bottom-charge}
> \]
> 因 `m_1+m_2=S`，
> \[
> \boxed{
> \log_{10}X_B
> <\log_{10}F_- -S+O(1).
> }
> \tag{Bottom-height-charge}
> \]
> 因而 post-tail second-Schmidt loss中 `X_B` 不再是一份自由 `S`-height；真正尚未
> 直接收费的只剩 projective/gap payer `X_P`。

---

## 1. `C_12` 自动整除真实 decimal determinant

DD decimal determinant为
\[
\boxed{
E=b_3A_{12}10^d-a_3Q>0.
}
\tag{1.1}
定义
\[
C_{12}:=(A_{12},Q).
\]
两项都显然被 `C_12` 整除，所以
\[
\boxed{C_{12}\mid E.}
\tag{1.2}

two-payer theorem已有
\[
X_B\mid\operatorname{core}_{10}(C_{12}),
\]
故特别地
\[
\boxed{X_B\mid E.}
\tag{1.3}

---

## 2. universal identity把 `E G` 严格放进 `F_-`

`core.md` 的 universal identity是
\[
\boxed{
F_-Q(\kappa+G)=E\kappa(\kappa+2G).
}
\tag{2.1}
所有量均为正整数。整理：
\[
\boxed{
\frac{EG}{F_-}
=
\frac{QG}{\kappa}
\frac{\kappa+G}{\kappa+2G}.
}
\tag{2.2}

DD unified tail window严格有
\[
\boxed{QG<\kappa.}
\tag{2.3}
同时 `G>0` 给
\[
\boxed{\kappa+G<\kappa+2G.}
\tag{2.4}
所以 `(2.2)` 的两个因子都严格小于 1：
\[
\boxed{EG<F_-.}
\tag{2.5}

结合 `(1.3)` 与正整数性：
\[
X_BG\le EG<F_-.
\]
即
\[
\boxed{X_BG<F_-.}
\tag{Bottom-charge}

注意这不是 ordinary size guess，而是 exact universal identity + tail interval 的直接推论。

---

## 3. 一整份 `S` 的 Archimedean 折扣

`b_i` 分别有 `m_i` 位，所以
\[
10^{m_i-1}\le b_i<10^{m_i}.
\]
而
\[
m_1+m_2=S.
\]
因此
\[
\boxed{
10^{S-2}\le G=b_1b_2<10^S.
}
\tag{3.1}

由 `Bottom-charge`：
\[
\log_{10}X_B
<\log_{10}F_- -\log_{10}G.
\]
使用 `(3.1)`：
\[
\boxed{
\log_{10}X_B
<\log_{10}F_- -S+2.
}
\tag{Bottom-height-charge}

所以任何 linearly large bottom source loss都必须先让 `F_-` 比它多承担约一整份 `S`
高度。

---

## 4. 与第二次 Schmidt 的自举

`tail-rough-cq-excess.md` 已有 second fixed-target Schmidt：
\[
\boxed{
\log R_x+\log(g_*/v)
\ge S-\log X_Q-o(S),
}
\tag{4.1}
其中 `R_x` 与 `g_*/v` 都是真实 `F_-` factors。
因此安全地
\[
\boxed{
\log F_-
\ge S-\log X_Q-o(S).
}
\tag{4.2}

使用 two-payer
\[
X_Q=X_PX_B
\]
与 `Bottom-height-charge`：
\[
\begin{aligned}
\log F_-
&\ge S-\log X_P-\log X_B-o(S)\\
&>S-\log X_P-
(\log F_- -S+O(1))-o(S).
\end{aligned}
\]
所以
\[
\boxed{
2\log F_-+\log X_P
\ge2S-o(S).
}
\tag{Bootstrap}

等价地
\[
\boxed{
\log F_-
\ge S-\frac12\log X_P-o(S).
}
\tag{Bootstrap-F}

这说明 bottom loss已经从 Schmidt budget中消去；代价只是 projective loss `log X_P`
的系数被减半。

---

## 5. 当前 branch-reoptimization frontier

post-tail hard rough mass经历
\[
C_Q\to X_Q\to(X_P,X_B)
\]
后，`X_B` 又由 `Bottom-charge` 进入真实 small factor。因此当前唯一未直接收费的量是
\[
\boxed{X_P\mid Z_0a.}
\]
并且它只以半权重出现在 bootstrap lower bound：
\[
\log F_-
\ge S-\frac12\log X_P-o(S).
\]

下一步只需对 projective/gap payer建立统一 height cap，或把 `X_P` 的一部分再次送进
`F_-` / carrier-circle。无需再对 denominator source cancellation或 bottom layer做新的 rough
Schmidt。

---

## 6. 状态摘要

- **`已严格完成`**：`C_12|E`、`EG<F_-`、`Bottom-charge`。
- **`已严格完成`**：`Bottom-height-charge`、second-Schmidt `Bootstrap`。
- **`结构压缩`**：post-tail reoptimization唯一尚未直接收费的 hard loss为 projective/gap `X_P`。
- **`待证`**：projective payer `X_P` height / further charge；non-canonical branch reoptimization；DD global explicit `<=6` / absolute height。

---

<a id="source-tail-rough-canonical-payer-decomposition"></a>

> 整合来源：`tail-rough-canonical-payer-decomposition.md`

# DD post-tail rough overflow 的 canonical four-payer decomposition

> **依赖：** [`tail-rough-general-transfer.md`](tail-allocation-ledger.md#source-tail-rough-general-transfer)、
> [`tail-rough-angular-source-transfer.md`](tail-allocation-ledger.md#source-tail-rough-angular-source-transfer)、
> [`high-funnel-qz-bottom-orientation-correction.md`](high-funnel-ledger.md#source-high-funnel-qz-bottom-orientation-correction)。
>
> **严格状态：** `已严格完成（整个 `X_Q` odd rough support）`。
>
> 之前的结果已经证明 `X_Q` 的每个 prime-power只能由 denominator third-excess、
> numerator coefficient/common-square、或 split-Gaussian angle支付。本文把这种“max payer”
> 改写成一个**逐 exponent 的 canonical decomposition**。
>
> 对每个
> \[
> p^x\Vert X_Q
> \]
> 定义四段深度：
> \[
> e_3=\min(x,r),
> \]
> \[
> e_B=\min(x-e_3,t),
> \]
> \[
> e_G=\min(x-e_3-e_B,g),
> \]
> \[
> e_A=x-e_3-e_B-e_G,
> \]
> 其中
> \[
> r=v_p(R_3^{\rm den}),\quad
> t=v_p(C),\quad
> g=v_p((a_1,a_2)).
> \]
> 则 `e_A` 自动满足
> \[
> \boxed{e_A\le v_p(N_{\rm num}).}
> \]
> 因此存在 canonical integers
> \[
> \boxed{X_Q=X_3X_BX_GX_A}
> \]
> （四者不要求 pairwise coprime；同一 prime 的不同 exponent layers可落入不同 payer），且
> \[
> \boxed{
> X_3\mid\operatorname{core}_{10}(R_3^{\rm den})\mid Z_0a,
> }
> \]
> \[
> \boxed{
> X_B\mid\operatorname{core}_{10}(C_{12})\mid\operatorname{core}_{10}(R_{12}),
> }
> \]
> \[
> \boxed{X_G\mid\operatorname{core}_{10}(a_1,a_2),}
> \]
> \[
> \boxed{X_A\mid\operatorname{core}_{10}(N_{\rm num}).}
> \]
> 这里
> \[
> C_{12}=(A_{12},Q),
> \]
> 而 `R_12` 是 orientation-uniform primitive bottom determinant reader。
>
> 这把 second-Schmidt 的 loss从一个匿名整数 `X_Q` 变成四条可分别收费的
> **projective / bottom / common-numerator / Gaussian-angular** carrier layers。

---

## 1. local data

固定
\[
p^x\Vert X_Q.
\]
`tail-rough-general-transfer.md` 与随后 Gaussian split使用：
\[
t:=v_p(C),
\qquad
r:=v_p(R_3^{\rm den}),
\]
\[
g:=v_p(g_n),
\qquad g_n=(a_1,a_2),
\]
\[
\omega:=v_p(N_{\rm ang}),
\qquad
u:=v_p(N_{\rm num}).
\]

在 `X_Q` support上
\[
\boxed{g\le t,}
\tag{1.1}
\]
且
\[
\boxed{
x\le\max(t,2g+\omega,r).}
\tag{1.2}

另一方面若 `omega>0`，`tail-rough-angular-source-transfer.md` 的同向 Gaussian transfer给
\[
\boxed{
\nu\ge\min(c,\omega),
}
\tag{1.3}
\]
其中
\[
c=v_p(C_Q),
\]
并且 `X_Q|C_Q` 给
\[
\boxed{x\le c.}
\tag{1.4}

---

## 2. canonical sequential allocation

定义
\[
\boxed{e_3:=\min(x,r).}
\tag{2.1}
\]
令
\[
x_1=x-e_3.
\]
再定义
\[
\boxed{e_B:=\min(x_1,t),}
\tag{2.2}
\]
\[
x_2=x_1-e_B.
\]
再定义
\[
\boxed{e_G:=\min(x_2,g),}
\tag{2.3}
\]
以及最后 remainder
\[
\boxed{e_A:=x_2-e_G.}
\tag{2.4}
显然
\[
\boxed{x=e_3+e_B+e_G+e_A.}
\tag{2.5}

前三段分别自动满足
\[
e_3\le r,
\qquad e_B\le t,
\qquad e_G\le g.
\]
唯一需要证明的是
\[
e_A\le\nu.
\]

---

## 3. angular remainder 必被 `N_num` 支付

若
\[
e_A=0,
\]
无事可证。以下设
\[
e_A>0.
\]
这意味着在 sequential allocation 后仍有 depth，因而
\[
\boxed{x>r+t+g.}
\tag{3.1}
特别地
\[
x>r,\qquad x>t.
\]
所以 `(1.2)` 的最大值只能由
\[
2g+\omega
\]
支付：
\[
\boxed{x\le2g+\omega.}
\tag{3.2}
由于 `t>=g`，从 `(3.1)` 还有
\[
x>t+g\ge2g,
\]
所以
\[
\omega>0.
\]
由 `(3.2)`：
\[
\boxed{\omega\ge x-2g.}
\tag{3.3}

另一方面 `(1.3),(1.4)` 给
\[
\nu\ge\min(c,\omega).
\]
因为 `c>=x`，而 `(3.3)` 给 `omega>=x-2g`：
\[
\boxed{\nu\ge x-2g.}
\tag{3.4}

最后由定义，`e_A>0` 时前三段都已达到各自容量：
\[
e_3=r,\qquad e_B=t,\qquad e_G=g.
\]
故
\[
e_A=x-r-t-g.
\]
而
\[
r+t-g\ge0
\]
因为 `t>=g`。所以
\[
\begin{aligned}
e_A
&=x-r-t-g\\
&\le x-2g\\
&\le\nu.
\end{aligned}
\]
证明
\[
\boxed{e_A\le v_p(N_{\rm num}).}
\tag{Angular-remainder}

---

## 4. global four-payer integers

对每个 `p|X_Q` 取上述四个 exponents，定义
\[
\boxed{X_3:=\prod_{p|X_Q}p^{e_3(p)},}
\]
\[
\boxed{X_B:=\prod_{p|X_Q}p^{e_B(p)},}
\]
\[
\boxed{X_G:=\prod_{p|X_Q}p^{e_G(p)},}
\]
\[
\boxed{X_A:=\prod_{p|X_Q}p^{e_A(p)}.}
\]
由 `(2.5)`：
\[
\boxed{X_Q=X_3X_BX_GX_A.}
\tag{Four-payer-product}

注意这些 integers 的 prime supports可以重叠，因为这里刻意分解的是**同一 prime 的
valuation layers**，不是做 coprime support partition。

逐定义立即有
\[
\boxed{X_3\mid\operatorname{core}_{10}(R_3^{\rm den}),}
\tag{4.1}
\]
\[
\boxed{X_G\mid\operatorname{core}_{10}(g_n),}
\tag{4.2}
\]
\[
\boxed{X_A\mid\operatorname{core}_{10}(N_{\rm num}).}
\tag{4.3}

下一节处理 `X_B`。

---

## 5. coefficient layer 自动进入 bottom carrier

固定 `p|X_B`。有
\[
e_B\le t=v_p(C).
\]
DD coefficient
\[
C=10^dA_{12}
\]
且 `p` 不整除 10，所以
\[
\boxed{e_B\le v_p(A_{12}).}
\tag{5.1}

另一方面
\[
e_B\le x\le c=v_p(C_Q),
\]
而
\[
Q=(b_1,b_2)C_Q,
\]
故
\[
\boxed{e_B\le v_p(Q).}
\tag{5.2}

因此
\[
\boxed{
p^{e_B}\mid C_{12}:=(A_{12},Q).}
\tag{5.3}
逐 prime相乘：
\[
\boxed{X_B\mid\operatorname{core}_{10}(C_{12}).}
\tag{5.4}

`high-funnel-qz-bottom-orientation-correction.md` 已证明，不论 `k-d` 正负，
orientation-uniform bottom reader
\[
R_{12}:=\Delta_{12}/10^{\min(k,d)}
\]
均满足
\[
\boxed{C_{12}\mid R_{12}.}
\tag{5.5}
所以
\[
\boxed{X_B\mid\operatorname{core}_{10}(R_{12}).}
\tag{Bottom-reader}

因此 coefficient payer不是一个普通 height pool；它必同时制造 genuine bottom-carrier depth。

---

## 6. third layer进入 projective/gap

已有 general projective allocation：
\[
\boxed{
\operatorname{core}_{10}(R_3^{\rm den})\mid Z_0a.
}
\]
结合 `(4.1)`：
\[
\boxed{X_3\mid\operatorname{core}_{10}(Z_0a).}
\tag{Projective-reader}

所以 four payer 的四条 canonical readers为
\[
\boxed{
\begin{array}{c|c}
\text{layer}&\text{reader}\\ \hline
X_3&Z_0a\\
X_B&C_{12}\mid R_{12}\\
X_G&(a_1,a_2)\\
X_A&N_{\rm num}
\end{array}}
\tag{Reader-table}

---

## 7. height form

由 exact product decomposition：
\[
\boxed{
\log X_Q
=\log X_3+\log X_B+\log X_G+\log X_A.
}
\]
并且安全有
\[
\boxed{
\log X_Q
\le
\log\operatorname{core}_{10}(Z_0a)
+\log\operatorname{core}_{10}(C_{12})
+\log\operatorname{core}_{10}(a_1,a_2)
+\log\operatorname{core}_{10}(N_{\rm num}).
}
\tag{Height-four-payer}

这比一个单独 `X_Q|product` 更适合后续 LP：每一份 valuation depth都只出现一次，且
`X_B` 已经带有 bottom-carrier语义，`X_A` 已带同向 Gaussian orientation。

---

## 8. 当前 branch-reoptimization frontier

post-tail source cancellation的 local complexity已经被压成四个 reader：

1. **projective/gap** `Z_0a`；
2. **bottom carrier** `R_12`；
3. **common numerator scale** `(a_1,a_2)`；
4. **pure numerator split-Gaussian angle** `N_num`。

因此下一步不应再做 ordinary denominator gcd allocation。真正目标变成：

- 用 carrier tetrahedron / circle eliminant限制 `X_B` 与 `X_3` 同时线性大；
- 用 numerator digit shell / cyclotomic overlap限制 `X_B` 与 `X_A`；
- common numerator `X_G` 的总高度最多由前两 numerator 的共同位数支付。

如果能证明这四个 layer总高度严格小于 `S` 的 Schmidt loss threshold，就可完成
non-canonical dominant side branch reoptimization，并有希望把全 DD explicit limsup推到 `<=6`。

---

## 9. 状态摘要

- **`已严格完成`**：canonical exponent allocation、`Angular-remainder`。
- **`已严格完成`**：`Four-payer-product`。
- **`已严格完成`**：`Bottom-reader` / `Projective-reader` / `Reader-table`。
- **`结构压缩`**：`X_Q` 已从单一匿名 loss变成四条可分别用不同算术机制收费的 carrier layers。
- **`待证`**：four-payer simultaneous height bound；non-canonical dominant branch reoptimization；DD global explicit `<=6` / absolute height。

---

<a id="source-tail-rough-cq-excess"></a>

> 整合来源：`tail-rough-cq-excess.md`

# DD tail rough core 的 primitive `Q`-cancellation overflow

> **依赖：** [`tail-rough-d0-allocation.md`](tail-allocation-ledger.md#source-tail-rough-d0-allocation)、
> [`gcd-normal-exact-small-factor.md`](good-genuine-ledger.md#source-gcd-normal-exact-small-factor)。
>
> **严格状态：** `已严格完成（non-decimal `d_0` support）`。
>
> 上一文件把第二次 Schmidt 的剩余 rough pool粗略压到
> \[
> C_Q=Q/(b_1,b_2).
> \]
> 本文继续逐 prime剥掉已经由 actual overlap `g_*/v` 支付的 denominator baseline。
> 对 `p` 不整除 10 且 `p|d_0`，写
> \[
> v_p(b_1)=v_p(b_2)=E,
> \qquad v_p(b_3)=j,
> \qquad c=v_p(C_Q).
> \]
> 则
> \[
> v_p(d_0)=E+c-j,
> \]
> 而未被 `g_*/v` 支付的精确 overflow为
> \[
> \boxed{
> x_p=
> \max\bigl(c-j-\min(E,j),0\bigr).
> }
> \]
> 因而真正的 hard rough pool不是整个 `C_Q`，而是 primitive concat cancellation
> 超过 `j+min(E,j)` denominator baseline后的部分。

---

## 1. local ledger

固定

\[
p\nmid10,\qquad p\mid d_0.
\]

`tail-rough-d0-allocation.md` 已证明

\[
\boxed{v_p(b_1)=v_p(b_2)=E.}
\tag{1.1}

记

\[
j:=v_p(b_3),
\qquad
c:=v_p(C_Q),
\qquad
h:=v_p(d_0).
\]

由

\[
Q=(b_1,b_2)C_Q
\]

以及 gcd-normal tail ledger

\[
v_p(Q)=h+j,
\]

得到

\[
\boxed{h=E+c-j>0.}
\tag{1.2}

---

## 2. actual overlap payer 的 exact depth

仍有

\[
\frac{g_*}{v}=\frac\gamma{c_3}.
\]

在当前 prime：

\[
v_p(\gamma)=2E,
\]

而

\[
v_p(c_3)=\max(E,j)-j.
\]

所以

\[
\boxed{
o:=v_p(g_*/v)
=2E-\max(E,j)+j.}
\tag{2.1}

分情况：

\[
\boxed{
o=
\begin{cases}
E+j,&E\ge j,\\
2E,&j>E.
\end{cases}}
\tag{2.2}

`o` 是已经真实出现在

\[
F_-=r(u+2v)\,a(g_*/v)
\]

中的 payer，不应再次记为 loss。

---

## 3. unpaid depth 的闭式

定义 local unpaid depth

\[
\boxed{x:=\max(h-o,0).}
\tag{3.1}

若 `E>=j`：

\[
h-o=(E+c-j)-(E+j)=c-2j.
\]

而 `min(E,j)=j`，所以

\[
x=\max(c-j-\min(E,j),0).
\]

若 `j>E`：

\[
h-o=(E+c-j)-2E=c-j-E,
\]

且 `min(E,j)=E`，得到同一式。

因此统一有

\[
\boxed{
 x_p
=\max\bigl(c-j-\min(E,j),0\bigr).
}
\tag{CQ-excess-local}

特别地：

- `E=j=0` 时
  \[
  x_p=c,
  \]
  整个 `C_Q` cancellation都是 hard excess；
- `E>0` 或 `j>0` 时，至少 `j+min(E,j)` 层 cancellation被 denominator
  baseline / actual overlap吸收；
- 若
  \[
  c\le j+\min(E,j),
  \]
  则该 prime对第二次 Schmidt不留下任何 unpaid `d_0` rough depth。

---

## 4. canonical excess integer

令

\[
D_{0,\rm rough}:=\operatorname{core}_{10}(d_0).
\]

逐 `p|D_{0,rough}` 定义

\[
X_Q:=\prod_{p\mid D_{0,\rm rough}}p^{x_p}.
\tag{4.1}

则从 `x_p=max(h-o,0)` 立即得到

\[
\boxed{
D_{0,\rm rough}
\mid
\frac{g_*}{v}\,X_Q.
}
\tag{4.2}

且

\[
\boxed{X_Q\mid C_Q.}
\tag{4.3}

所以 `tail-rough-d0-allocation.md` 的 coarse payer

\[
D_{0,\rm rough}\mid(g_*/v)C_Q
\]

可以严格加强成 `(4.2)`。

---

## 5. 第二次 Schmidt 的真正 loss

令

\[
R_x:=\operatorname{core}_{10}\bigl((u+2v)/(u,2)\bigr).
\]

第二次 Schmidt theorem给

\[
\log R_x+\log D_{0,\rm rough}\ge S-o(S).
\]

而 `R_x` 与 `g_*/v` 都已经进入 actual `F_-`。使用 `(4.2)`：

\[
\boxed{
\log R_x+\log(g_*/v)
\ge
S-\log X_Q-o(S).
}
\tag{5.1}

因此 post-tail branch reoptimization 唯一真正需要继续收费的是

\[
\boxed{X_Q,}
\]

而不是 `d_0` 或 `C_Q` 全体。

`X_Q` 的 primewise 定义说明它只由**超过 denominator baseline 的 primitive
prefix concat cancellation**组成。

---

## 6. prime-flow interpretation

对 `p|X_Q` 必有

\[
c>j+\min(E,j).
\]

因此 `Q/h_{12}` 在 `p` 处发生的 cancellation depth不仅超过第三 denominator
深度 `j`，还超过 prefix/tail 可共同支付的 `min(E,j)`。

在最危险的 baseline-free 情形

\[
E=j=0,
\]

这就是纯粹的

\[
B_1 10^{m_2}+B_2\equiv0\pmod{p^c}
\]

型 source cancellation；它与旧 canonical `U`-prime channel完全一致。

所以非-canonical side branches若携带显著 denominator common depth，`X_Q` 会自动
小于原 `C_Q`；真正可能保持正线性 loss的只剩接近 baseline-free 的 source
cancellation sheet。

---

## 7. 状态摘要

- **`已严格完成`**：`CQ-excess-local`、canonical `X_Q`、
  `D0_rough | (g_*/v) X_Q`。
- **`结构压缩`**：second-Schmidt post-tail loss只剩 primitive cancellation overflow
  `X_Q`。
- **`待证`**：对 `X_Q` 建立 source/Gaussian cancellation height bound；用其完成
  side-branch reoptimization并判断 global `6.215109...` 升级；DD absolute height。

---

<a id="source-tail-rough-d0-allocation"></a>

> 整合来源：`tail-rough-d0-allocation.md`

# DD 第二次 Schmidt rough core 的 `d_0` allocation

> **依赖：** [`gcd-normal-exact-small-factor.md`](good-genuine-ledger.md#source-gcd-normal-exact-small-factor)、
> `global-framework.md` 的 denominator prime graph、`core.md` 的 gcd-normal form。
>
> **严格状态：** `已严格完成（整个 DD gcd-normal tail 的 non-decimal support）`。
>
> general exact small-factor normalization 已说明，第二次 Schmidt rough product中
> `x=(u+2v)/delta` 一侧已经进入 `F_-`；唯一尚未定位的是
> \[
> \operatorname{core}_{10}(d_0),
> \qquad d_0=(u,Q).
> \]
> 本文证明：任何 `p` 不整除 10 且 `p|d_0`，前两 denominator 在 `p` 处必须
> **equal valuation**。令
> \[
> h_{12}=(b_1,b_2),\qquad C_Q:=Q/h_{12},
> \]
> 则
> \[
> \boxed{
> \operatorname{core}_{10}(d_0)^2
> \mid
> \gamma C_Q^2,
> }
> \]
> 并且更贴近 small factor地有
> \[
> \boxed{
> \operatorname{core}_{10}(d_0)
> \mid
> \frac{g_*}{v}\,C_Q.
> }
> \]
> 因而第二次 Schmidt尚未被 `F_-` 支付的唯一 rough pool缩成 primitive
> prefix-concat cancellation factor `C_Q`。

---

## 1. 固定一个 `d_0` rough prime

沿用 gcd-normal notation：

\[
\kappa=\gamma u,\qquad G=\gamma v,\qquad(u,v)=1,
\]

\[
d_0=(u,Q),\qquad u=d_0r,\qquad Q=d_0q,\qquad(r,q)=1,
\]

且 `r|10^m`。

固定

\[
p\nmid10,\qquad p\mid d_0.
\]

记

\[
h:=v_p(d_0)>0,
\qquad j:=v_p(q),
\]

以及 denominator valuations

\[
e_i:=v_p(b_i),\qquad i=1,2,3.
\]

由 `gcd-normal-exact-small-factor.md` 的 tail recovery

\[
b_3=v\frac{10^m}{r}q.
\]

因为 `p|u` 且 `(u,v)=1`：

\[
p\nmid v.
\]

又 `p` 不整除 `10r`，所以

\[
\boxed{e_3=j.}
\tag{1.1}

而

\[
\boxed{v_p(Q)=h+j.}
\tag{1.2}

同时 `p|u`、`p` 不整除 `v` 意味着

\[
v_p(\kappa)>v_p(G),
\]

故

\[
\boxed{v_p(\gamma)=v_p(G)=e_1+e_2.}
\tag{1.3}

---

## 2. 前两 denominator 必须 equal valuation

反设

\[
e_1\ne e_2.
\]

由于 `p` 不整除 10，二项

\[
Q=b_1 10^{m_2}+b_2
\]

的两个 summands valuation不同，因此没有 cancellation：

\[
\boxed{v_p(Q)=\min(e_1,e_2).}
\tag{2.1}

结合 `(1.2)`：

\[
\min(e_1,e_2)=h+j>j=e_3.
\tag{2.2}

所以三个 denominator valuations中，较大的那个 prefix exponent是**唯一最大值**。

但 denominator prime graph 的 odd-prime unique-max rule证明：若某一块唯一取得最大值，
另外两块的 `p`-adic exponents必须相等。

例如若 `e_1>e_2`，必须

\[
e_2=e_3=j,
\]

这与 `(2.2)` 的 `e_2=h+j>j` 矛盾。另一方向相同。

因此

\[
\boxed{e_1=e_2=:E.}
\tag{Equal-prefix}

这说明每个 `d_0` rough prime都是

\[
\boxed{\text{equal-prefix denominator depth + genuine }Q\text{-cancellation}}
\]

类型，而不是 arbitrary denominator imbalance prime。

---

## 3. primitive concat cancellation depth

定义

\[
\boxed{h_{12}:=(b_1,b_2),}
\qquad
\boxed{C_Q:=Q/h_{12}.}
\tag{3.1}

在当前 `p`：

\[
v_p(h_{12})=E.
\]

由 `(1.2)`：

\[
\boxed{
v_p(C_Q)=h+j-E.}
\tag{3.2}

右端自动非负，因为 equal valuations至少强制 `p^E|Q`。

由 `(1.3)` 与 `(Equal-prefix)`：

\[
\boxed{v_p(\gamma)=2E.}
\tag{3.3}

于是

\[
\begin{aligned}
v_p(\gamma C_Q^2)
&=2E+2(h+j-E)\\
&=2h+2j\\
&\ge2h.
\end{aligned}
\]

所以对每个 `p|core_10(d_0)`：

\[
2v_p(d_0)
\le v_p(\gamma C_Q^2).
\]

逐素数相乘得到

\[
\boxed{
\operatorname{core}_{10}(d_0)^2
\mid
\gamma C_Q^2.
}
\tag{d0-square-allocation}

---

## 4. 把 `gamma` payer换成 actual small-factor overlap

`core.md` 的 denominator overlap满足

\[
\boxed{g_*=G/c_3,}
\]

而 `G=gamma v`，所以

\[
\boxed{
\frac{g_*}{v}=\frac\gamma{c_3}.}
\tag{4.1}

需要比较 `c_3=q_lcm/b_3` 的 `p`-depth。

当前

\[
e_1=e_2=E,\qquad e_3=j.
\]

因此

\[
\boxed{v_p(c_3)=\max(E,j)-j.}
\tag{4.2}

从而

\[
v_p(g_*/v)
=2E-\max(E,j)+j.
\tag{4.3}

与 `(3.2)` 相加。若 `E>=j`：

\[
(E+j)+(h+j-E)=h+2j\ge h.
\]

若 `j>E`：

\[
2E+(h+j-E)=h+E+j\ge h.
\]

所以统一有

\[
\boxed{
v_p(d_0)
\le
v_p(g_*/v)+v_p(C_Q).}
\tag{4.4}

逐 rough primes相乘：

\[
\boxed{
\operatorname{core}_{10}(d_0)
\mid
\frac{g_*}{v}\,C_Q.
}
\tag{d0-F-payer}

这里 `g_*/v` 已经是
`gcd-normal-exact-small-factor.md` 中 actual normalized small-factor quotient

\[
F_-=r(u+2v)\,a(g_*/v)
\]

的一部分。因此第二次 Schmidt的 `d_0` rough height中，只有被 `C_Q` 支付的部分
没有同时自动出现在 `F_-`。

---

## 5. 与第二次 Schmidt rough product 联立

第二次 fixed-target Schmidt theorem使用

\[
\delta=(u,u+2v)=(u,2)\in\{1,2\},
\]

\[
x=(u+2v)/\delta,\qquad y=u/\delta.
\]

因为 `r` 是 2,5-smooth，

\[
\boxed{
\operatorname{core}_{10}(y)
=\operatorname{core}_{10}(d_0).
}
\tag{5.1}

而 `x`-side rough core完整整除 `u+2v`，已由 exact small factor支付。

Schmidt 给

\[
\log_{10}\operatorname{core}_{10}(x)
+
\log_{10}\operatorname{core}_{10}(d_0)
\ge S-o(S).
\tag{5.2}

使用 `(d0-F-payer)`：若记

\[
C_h:=\log_{10}C_Q,
\]

则除 `C_Q` 这一份 cancellation height外，`(5.2)` 强迫的 rough mass都已经
进入 actual factor

\[
(u+2v)(g_*/v)\mid F_-/r a
\]

的对应部分。

因此 post-tail side-branch reoptimization真正剩余的单一 rough pool是

\[
\boxed{C_Q=Q/(b_1,b_2).}
\]

而不是 `d_0`、`q-Z gcd` 或另一个匿名 rough gcd。

---

## 6. `C_Q` 的算术意义

写

\[
b_1=h_{12}B_1,\qquad b_2=h_{12}B_2,\qquad(B_1,B_2)=1.
\]

则

\[
\boxed{
C_Q=B_1 10^{m_2}+B_2.
}
\tag{6.1}

所以 `C_Q` 是**primitive prefix denominator concat cancellation carrier**。

对 `p|d_0` 的 rough support，`p` 不可能来自 unequal denominator valuations；它只能来自
`B_1 10^{m_2}+B_2` 的 genuine p-adic cancellation。

这正对应旧 canonical prime-flow 中 `U`-type cancellation primes的全局版本。

---

## 7. 状态摘要

- **`已严格完成`**：`Equal-prefix`、`d0-square-allocation`、`d0-F-payer`。
- **`结构压缩`**：第二次 Schmidt rough product中，除 actual `F_-` 已支付的
  `x`-core 与 overlap payer外，只剩 primitive concat cancellation `C_Q`。
- **`待证`**：对 `C_Q` 建立 global height / Gaussian split / source cancellation
  charge；完成 post-tail 非 canonical branches reoptimization；DD global explicit slope / absolute height。

---

<a id="source-tail-rough-gaussian-payer-split"></a>

> 整合来源：`tail-rough-gaussian-payer-split.md`

# DD post-tail rough payer 的 common / Gaussian-angular split

> **依赖：** [`tail-rough-general-transfer.md`](tail-allocation-ledger.md#source-tail-rough-general-transfer)、
> `core.md` 的 prefix two-square norm 与 stereographic projective denominator。
>
> **严格状态：** `已严格完成（整个 `X_Q` odd rough support）`。
>
> `tail-rough-general-transfer.md` 已把第二次 Schmidt 剩余 overflow `X_Q`
> 压到三个 payer：
> \[
> C,\qquad
> N_0:=\frac{\mathcal N_{12}}{(b_1,b_2)^2},\qquad
> Z_0a.
> \]
> 本文继续把 `N_0` 中并不独立的 common numerator square剥掉。写
> \[
> b_i=h_{12}B_i,\qquad h_{12}=(b_1,b_2),\qquad(B_1,B_2)=1,
> \]
> \[
> X=a_1B_2,\qquad Y=a_2B_1,\qquad
> g_A=(X,Y),
> \]
> \[
> \boxed{
> N_{\rm ang}:=\frac{N_0}{g_A^2}
> =\left(\frac X{g_A}\right)^2+
> \left(\frac Y{g_A}\right)^2.
> }
> \]
> 则 `N_ang` 是 primitive sum of two squares；所以所有 odd prime divisor
> `p|N_ang` 都满足
> \[
> \boxed{p\equiv1\pmod4.}
> \]
> 更重要的是，在 `X_Q` 的 prime support上有
> \[
> v_p(g_A)\le v_p(C),
> \]
> 因而 general transfer 可全局加强成 product allocation
> \[
> \boxed{
> X_Q\mid
> \operatorname{core}_{10}(C)^2\,
> \operatorname{core}_{10}(N_{\rm ang})\,
> \operatorname{core}_{10}(Z_0a).
> }
> \tag{Angular-transfer}
> \]
> 于是 post-tail source loss中真正独立的 Gaussian payer只剩
> **split-prime angular norm** `N_ang`；`3 mod 4` rough primes不能藏在一个新的
> two-square norm pool里。

---

## 1. primitive prefix denominator blocks

令
\[
\boxed{h_{12}:=(b_1,b_2),}
\]
并写
\[
\boxed{b_1=h_{12}B_1,\qquad b_2=h_{12}B_2,}
\qquad(B_1,B_2)=1.
\tag{1.1}
\]
则 primitive denominator concat为
\[
\boxed{
C_Q=\frac Q{h_{12}}
=B_1 10^{m_2}+B_2.
}
\tag{1.2}

同时
\[
\begin{aligned}
N_0
&:=\frac{\mathcal N_{12}}{h_{12}^2}\\
&=(a_1B_2)^2+(a_2B_1)^2.
\end{aligned}
\tag{1.3}

沿用记号
\[
X:=a_1B_2,
\qquad
Y:=a_2B_1.
\]

---

## 2. `X_Q` prime不整除 primitive denominator blocks

固定
\[
p\mid X_Q.
\]
由 `tail-rough-cq-excess.md`：
\[
X_Q\mid C_Q,
\]
所以
\[
p\mid C_Q=B_1 10^{m_2}+B_2.
\tag{2.1}
\]
又 `p` 属于 `core_10(d_0)`，因此
\[
p\nmid10.
\]

若 `p|B_1`，由 `(2.1)` 会有 `p|B_2`，与 `(B_1,B_2)=1` 矛盾。
反向相同。因此
\[
\boxed{p\nmid B_1B_2.}
\tag{XQ-den-unit}

这一步非常关键：在真正需要支付的 `X_Q` support 上，`N_0` 的 common
`p`-depth只能来自 numerator `a_1,a_2`，不能再次来自 denominator baseline。

---

## 3. common numerator scale已被 `C` 支付

定义
\[
\boxed{g_A:=(X,Y)=(a_1B_2,a_2B_1).}
\tag{3.1}

固定 `p|X_Q`。由 `(XQ-den-unit)`：
\[
\boxed{
v_p(g_A)=\min(v_p(a_1),v_p(a_2)).
}
\tag{3.2}

DD numerator coefficient满足
\[
C=10^dA_{12},
\qquad
A_{12}=a_1 10^{n_2}+a_2.
\]
由于 `p` 不整除 10：
\[
v_p(C)=v_p(A_{12}).
\]
二项和总有
\[
v_p(A_{12})
\ge\min(v_p(a_1),v_p(a_2)).
\]
所以
\[
\boxed{
v_p(g_A)\le v_p(C)
\qquad(p\mid X_Q).
}
\tag{Common-paid}

因此 `N_0` 中平方 common factor `g_A^2` 的每一层，在 `X_Q` support 上都可由
`C^2` 支付。

---

## 4. 剩余 norm 是 genuine primitive Gaussian angle

定义
\[
\boxed{
N_{\rm ang}:=\frac{N_0}{g_A^2}.
}
\tag{4.1}
令
\[
X_0=X/g_A,
\qquad
Y_0=Y/g_A.
\]
则
\[
(X_0,Y_0)=1,
\]
且
\[
\boxed{N_{\rm ang}=X_0^2+Y_0^2.}
\tag{4.2}

固定 odd prime
\[
p\equiv3\pmod4.
\]
若 `p|N_ang`，则
\[
X_0^2+Y_0^2\equiv0\pmod p.
\]
因为 `-1` 在 `F_p` 中不是平方，唯一可能是
\[
p|X_0,\qquad p|Y_0,
\]
与 `(X_0,Y_0)=1` 矛盾。因此
\[
\boxed{
p\mid N_{\rm ang},\ p\text{ odd}
\Longrightarrow p\equiv1\pmod4.}
\tag{Angular-split}

特别地，对 `p=3 mod 4` 有 exact local valuation
\[
v_p(N_0)=2v_p(g_A)\le2v_p(C).
\tag{4.3}

所以 inert rough prime在 general transfer中若看似由 `N_0` 支付，其实只是
numerator common square的另一张投影，并不是独立 Gaussian payer。

---

## 5. 从 general transfer 得到 angular product allocation

`tail-rough-general-transfer.md` 对每个 `p|X_Q` 给
\[
 x_p\le
 \max\Bigl(
 v_p(C),
 v_p(N_0),
 v_p(R_3^{\rm den})
 \Bigr).
\tag{5.1}

写
\[
g_p:=v_p(g_A),
\qquad
\omega_p:=v_p(N_{\rm ang}),
\qquad
r_p:=v_p(R_3^{\rm den}).
\]
则
\[
v_p(N_0)=2g_p+\omega_p.
\]
由 `(Common-paid)`：
\[
g_p\le v_p(C)=:t_p.
\]
所以 `(5.1)` 安全推出
\[
\begin{aligned}
x_p
&\le\max(t_p,2g_p+\omega_p,r_p)\\
&\le2t_p+\omega_p+r_p.
\end{aligned}
\tag{5.2}

逐 `X_Q` prime相乘：
\[
\boxed{
X_Q
\mid
\operatorname{core}_{10}(C)^2\,
\operatorname{core}_{10}(N_{\rm ang})\,
\operatorname{core}_{10}(R_3^{\rm den}).
}
\tag{5.3}

这里使用 product 而非虚假的互素分配；三个 payer可以共享 prime，`(5.3)` 只是一条
逐 prime exponent inequality。

---

## 6. third-exclusive payer继续进入 projective/gap

`tail-rough-general-transfer.md` / 既有 projective ledger 已证明
\[
\boxed{
\operatorname{core}_{10}(R_3^{\rm den})\mid Z_0a.
}
\tag{6.1}

代入 `(5.3)`：
\[
\boxed{
X_Q
\mid
\operatorname{core}_{10}(C)^2\,
\operatorname{core}_{10}(N_{\rm ang})\,
\operatorname{core}_{10}(Z_0a).
}
\tag{Angular-transfer}

高度上安全得到
\[
\boxed{
\log X_Q
\le
2\log\operatorname{core}_{10}(C)
+\log\operatorname{core}_{10}(N_{\rm ang})
+\log\operatorname{core}_{10}(Z_0a).
}
\tag{6.2}

后续优化不能把这些高度视为独立而任意重复收费；本文的价值是**support 类型分离**：
`N_ang` 的所有 odd rough support均为 Gaussian split primes。

---

## 7. inert / split rough source 的 canonical interpretation

把 `X_Q` 的 odd support按模 4 分成
\[
X_Q=X_Q^{(+)}X_Q^{(-)},
\]
其中
\[
p|X_Q^{(+)}\Rightarrow p\equiv1\pmod4,
\]
\[
p|X_Q^{(-)}\Rightarrow p\equiv3\pmod4.
\]
（两个整数当然互素。）

对 inert part，由 `(4.3)` 与 general transfer可直接写成
\[
\boxed{
X_Q^{(-)}
\mid
\operatorname{lcm}\!\left(
\operatorname{core}_{10}(C)^2,
\operatorname{core}_{10}(R_3^{\rm den})
\right),
}
\tag{Inert-transfer}

进而
\[
\boxed{
X_Q^{(-)}
\mid
\operatorname{lcm}\!\left(
\operatorname{core}_{10}(C)^2,
\operatorname{core}_{10}(Z_0a)
\right).
}
\tag{Inert-projective}

所以 `3 mod 4` rough source完全不需要新的 Gaussian norm pool。

真正需要继续研究的只有 split part `X_Q^(+)`：当它没有被 `C` 或 `Z_0a`
支付时，`N_ang` 给出一个 primitive Gaussian orientation condition。

---

## 8. 当前 post-tail frontier

第二次 Schmidt的 hard loss已经经历：
\[
C_Q
\to X_Q
\to(C,N_0,Z_0a)
\to(C,N_{\rm ang},Z_0a),
\]
且最后一个新 norm满足
\[
\boxed{
\text{odd support}(N_{\rm ang})
\subset\{p:p\equiv1\pmod4\}.
}
\]

因此 side-branch reoptimization的下一步不再是 generic source cancellation：

1. inert rough mass只能进入 numerator coefficient `C` 或 projective/gap `Z_0a`；
2. 只有 split rough mass能进入 genuine Gaussian angular payer `N_ang`；
3. 应把 split `N_ang` 与 existing Gaussian carrier / determinant orientation 联立，而不是继续做普通 gcd height。

---

## 9. 状态摘要

- **`已严格完成`**：`XQ-den-unit`、`Common-paid`、`Angular-split`。
- **`已严格完成`**：`Angular-transfer` 与 `Inert-projective`。
- **`结构压缩`**：`N_0` 的独立 rough payer只剩 primitive split-Gaussian angle `N_ang`。
- **`待证`**：split `N_ang` 的 orientation / carrier charge；`C` 与 `Z_0a` 的 independent excess height；non-canonical dominant branch reoptimization；DD global explicit `<=6` / absolute height。

---

<a id="source-tail-rough-general-transfer"></a>

> 整合来源：`tail-rough-general-transfer.md`

# DD general rough `Q`-cancellation 的三 payer transfer

> **依赖：** [`tail-rough-cq-excess.md`](tail-allocation-ledger.md#source-tail-rough-cq-excess)、[`tail-source-cancellation-transfer.md`](tail-allocation-ledger.md#source-tail-source-cancellation-transfer)、[`tail-hard-source-derivative-sheet.md`](tail-allocation-ledger.md#source-tail-hard-source-derivative-sheet)、`global-framework.md` 的 unified quadratic / primitive recovery，以及 `core.md` 的 DD gap quadratic 与 projective denominator formula。
>
> **严格状态：** `已严格完成（整个 gcd-normal DD tail 的 odd non-decimal `d_0` support）`。
>
> `tail-rough-cq-excess.md` 对每个 `p|core_10(d_0)` 写
> \[
> v_p(b_1)=v_p(b_2)=E,
> \qquad v_p(b_3)=j,
> \qquad c=v_p(C_Q),
> \]
> 并定义真正未被 denominator overlap 支付的 primitive concat overflow
> \[
> x_p=\max\bigl(c-j-\min(E,j),0\bigr).
> \]
> 本文证明该 overflow 不可能继续悬空。令
> \[
> h_{12}=(b_1,b_2),
> \qquad N_0:=\mathcal N_{12}/h_{12}^2,
> \]
> \[
> R_3^{\rm den}:=
> \frac{b_3}{(b_3,\operatorname{lcm}(b_1,b_2))}.
> \]
> 则逐 prime 有
> \[
> \boxed{
> x_p\le
> \max\Bigl(
> v_p(C),
> v_p(N_0),
> v_p(R_3^{\rm den})
> \Bigr).
> }
> \tag{General-transfer-local}
> \]
> 因而若 `X_Q` 是 `tail-rough-cq-excess.md` 的 canonical overflow integer，
> \[
> \boxed{
> X_Q\mid
> \operatorname{lcm}\!\left(
> \operatorname{core}_{10}(C),
> \operatorname{core}_{10}(N_0),
> \operatorname{core}_{10}(R_3^{\rm den})
> \right).
> }
> \tag{General-transfer-global}
> \]
> 再用 projective denominator 的逐 prime identity，第三 payer 可继续送入 `Z_0 a`：
> \[
> \boxed{
> X_Q\mid
> \operatorname{lcm}\!\left(
> \operatorname{core}_{10}(C),
> \operatorname{core}_{10}(N_0),
> \operatorname{core}_{10}(Z_0a)
> \right).
> }
> \tag{General-transfer-projective}
> \]
> 因此 post-tail 第二次 Schmidt 的唯一 rough loss已从匿名 denominator cancellation
> 压成三个明确 numerator/projective payer。

---

## 1. local denominator ledger

固定 odd prime
\[
p\nmid10,
\qquad p\mid d_0.
\]
`tail-rough-d0-allocation.md` 已证明前两 denominator 必须 equal valuation：
\[
\boxed{v_p(b_1)=v_p(b_2)=E.}
\tag{1.1}
\]
写
\[
j:=v_p(b_3),
\qquad c:=v_p(C_Q),
\qquad C_Q=Q/(b_1,b_2).
\]
则
\[
\boxed{v_p(Q)=E+c.}
\tag{1.2}
\]
而 `tail-rough-cq-excess.md` 给
\[
\boxed{x:=x_p=\max(c-j-\min(E,j),0).}
\tag{1.3}
\]
以下只需处理 `x>0`。

令
\[
M:=\max(E,j),
\qquad
\delta:=M-j=(E-j)_+.
\]
由 tail weight
\[
\kappa b_3=10^mQG,
\qquad v_p(G)=2E,
\]
得到
\[
\boxed{v_p(\kappa)=3E+c-j>2E.}
\tag{1.4}
\]
所以 `p` 为奇素数时
\[
\boxed{
 v_p(\kappa+G)
 =v_p(\kappa+2G)
 =2E.
}
\tag{1.5}

此外 `L|10^m`，故 `p` 不整除 `L`。若
\[
C_0=QL+2\tau,
\]
则 `v_p(QL)=E+c>j=v_p(\tau)`，于是
\[
\boxed{v_p(C_0)=j.}
\tag{1.6}

整数球面 lcm denominator记为 `q_lcm`。显然
\[
v_p(q_{\rm lcm})=M.
\tag{1.7}
\]
DD §17 的 exact simplification为
\[
\boxed{\mathcal M=q_{\rm lcm}C,}
\tag{1.8}
\]
故若
\[
t:=v_p(C),
\]
则
\[
\boxed{v_p(\mathcal M)=M+t.}
\tag{1.9}

最后
\[
\mathcal N_{12}=h_{12}^2N_0,
\qquad v_p(h_{12})=E,
\]
所以记
\[
\boxed{n_0:=v_p(N_0),}
\qquad
v_p(\mathcal N_{12})=2E+n_0.
\tag{1.10}

---

## 2. 反设 overflow 没有任何三 payer

反设
\[
\boxed{
x>t,\qquad x>n_0,\qquad x>(j-E)_+.}
\tag{2.1}
\]
我们将推出矛盾。

记
\[
A:=v_p(a),
\qquad r:=v_p(\mu),
\qquad s:=v_p(\nu),
\qquad g_0:=v_p(G_0).
\]
由
\[
\frac\mu\nu
=G(\mathcal R-r_3)
=\frac{GLa}{q_{\rm lcm}}
\]
得到
\[
\boxed{r-s=2E+A-M.}
\tag{2.2}
\]
由 primitive recovery
\[
10^mQG_0=2\kappa\mu\nu
\]
得到
\[
\boxed{g_0=2E-j+r+s.}
\tag{2.3}
\]
而 universal gap square-core
\[
LaG_0=2c_3\mu^2,
\qquad c_3=q_{\rm lcm}/b_3
\]
在当前 prime给
\[
\boxed{A+g_0=\delta+2r.}
\tag{2.4}
\]
这些关系与 `(2.2),(2.3)` 一致，并用于下面的 valuation case split。

---

## 3. gap quadratic 强制 `A=t+delta`

DD gap quadratic为
\[
\boxed{
C_0a^2-2\mathcal Ma+Q\frac{\mathcal S_{12}}L=0.
}
\tag{3.1}
\]
其中
\[
\mathcal S_{12}=y_1^2+y_2^2
=\left(\frac{q_{\rm lcm}}G\right)^2\mathcal N_{12}.
\]
因此三项 valuations为
\[
\boxed{
G_1=j+2A,
\qquad
G_2=M+t+A,
\qquad
G_3=c-E+2M+n_0.
}
\tag{3.2}
\]
三个整数和为零，所以最低 valuation至少出现两次。

### 3.1 `E>=j`

此时 `M=E`, `delta=E-j`，且 `(2.2)` 给
\[
r=E+A,\qquad s=0.
\]
由 `(2.3)`：
\[
g_0=3E-j+A.
\]
考察
\[
G_0\mid \mathcal N_{12}\nu^2-\mu^2.
\]
若 `A<delta`，则 `2v_p(mu)=2E+2A<g_0`。要使差仍被 `p^{g_0}` 整除，只可能两项先在更低层同 valuation，即
\[
n_0=2A.
\]
但 `(2.1)` 给 `x>2A`。此时
\[
G_3-G_1=E+c-j>0,
\]
故第三项严格更深，必须 `G_1=G_2`，即 `A=t+delta>=delta`，矛盾。

所以 `A>=delta`。此时若 `2E+n_0<g_0`，它不可能与 `2E+2A` 在同一较低层相消，因为
\[
2A\ge A+delta=g_0-2E.
\]
因此必有
\[
\boxed{n_0\ge A+delta.}
\tag{3.3}
\]
于是
\[
G_3-G_1
=E+c-j+n_0-2A
\ge x+2E-A>0,
\]
其中使用 `c=x+2j` 与 `x>n_0>=A`。同理
\[
G_3-G_2
=c+n_0-t-A
\ge x+E+j-t>0.
\]
所以第三项严格更深，必有
\[
\boxed{A=t+delta.}
\tag{3.4}

### 3.2 `j>E`

此时 `M=j`, `delta=0`，且 `(2.1)` 的第三个不等式给
\[
x>j-E.
\]
由于
\[
x=c-j-E,
\]
可得
\[
\boxed{c>2j.}
\tag{3.5}

由 `(2.2)`：
\[
r-s=2E+A-j.
\]
若右端非正，结合 `(2.3)` 的 `g_0>=0` 可知只能有 `A=0`（边界 `j=2E` 也同样给 `A=0`）。此时 `G_3>G_1=j`，最低层要求 `G_1=G_2`，故 `t=0=A`。

下面设右端为正。则
\[
r=2E+A-j,
\qquad s=0,
\qquad
 g_0=A+4E-2j.
\]
并且 `G_0|N_12 nu^2-mu^2` 迫使
\[
\boxed{n_0\ge A+2E-2j.}
\tag{3.6}
\]
（右端若为负则该不等式当然自动成立）。

若 `A<t`，则 `G_1<G_2`，最低层只能要求 `G_1=G_3`。这给
\[
n_0=2A-c+E-j.
\]
与 `(3.6)` 比较：
\[
A\ge c+E-j=x+2E,
\]
但 `A<t<x`，矛盾。

若 `A>t`，同理 `G_2<G_1`，只能 `G_2=G_3`，从而
\[
n_0=t+A-c+E-j.
\]
再与 `(3.6)` 比较得到
\[
t\ge c+E-j=x+2E,
\]
与 `t<x` 矛盾。

因此唯一可能为
\[
\boxed{A=t.}
\tag{3.7}

综上两种 denominator order统一得到
\[
\boxed{A=t+delta.}
\tag{Gap-baseline-lock}

---

## 4. 第三 gap term 必须严格更深

将 `A=t+delta` 代回 `(3.2)`：
\[
G_1=G_2=M+t+A.
\]
定义
\[
\boxed{
\Delta:=G_3-G_1
=c+j-E+n_0-2t.
}
\tag{4.1}

最低 valuation至少出现两次，所以 `Delta>=0`。事实上 `Delta=0` 也不可能。

若 `E>=j`，由 `(3.3)` 与 `A=t+delta`：
\[
n_0\ge t+2delta.
\]
于是
\[
\Delta
\ge x+E+j-t>0.
\]

若 `j>E` 且 `t=0`，显然 `Delta>0`。若 `t>0`，由 `(3.6)`：
\[
n_0\ge t+2E-2j.
\]
若反设 `Delta=0`，则
\[
t\ge c+E-j=x+2E,
\]
再次与 `t<x` 矛盾。

因此统一有
\[
\boxed{\Delta>0.}
\tag{Gap-extra}

gap quadratic因而给一条 genuine extra contact：
\[
\boxed{
v_p(C_0a-2\mathcal M)=M+t+\Delta.}
\tag{Gap-contact-general}

---

## 5. unified discriminant 给 derivative contact

统一判别核
\[
K_{C,Q}=G^2C^2-Q^2\mathcal N_{12}
\]
的两项 valuation分别为
\[
4E+2t,
\qquad
4E+2c+n_0.
\]
由 `c>x>t`，第二项严格更深，所以
\[
\boxed{v_p(K_{C,Q})=4E+2t.}
\tag{5.1}

unified discriminant为
\[
W^2
=\kappa\left(
\kappa K_{C,Q}-2GQ^2\mathcal N_{12}
\right).
\]
括号中两项 valuation差恰为
\[
\begin{aligned}
&\bigl(6E+2c+n_0\bigr)
-\bigl(7E+c-j+2t\bigr)\\
&=c+j-E+n_0-2t
=\Delta>0.
\end{aligned}
\]
故无 inner cancellation，并得到
\[
\boxed{v_p(W)=5E+c-j+t.}
\tag{W-general}

DD §18 有同一个判别根
\[
W=L\Xi,
\qquad
\Xi=\mathcal M-C_0a
\]
（绝对值不影响 valuation），且 `p` 不整除 `L`。另一方面
\[
v_p(\mathcal M)=M+t,
\]
而由 `Gap-baseline-lock`
\[
v_p(C_0a)=j+A=j+t+delta=M+t.
\]
所以 derivative extra depth为
\[
\boxed{
D_{\rm der}
:=v_p(\Xi)-(M+t)
=5E+c-j-M.
}
\tag{5.2}

---

## 6. derivative 与 gap 两 contacts 强迫 `D_der=0`

若
\[
D_{\rm der}>0,
\]
则 `(5.2)` 给
\[
\mathcal M\equiv C_0a
\pmod{p^{M+t+1}}.
\]
而 `(Gap-contact-general)` 与 `Delta>0` 给
\[
2\mathcal M\equiv C_0a
\pmod{p^{M+t+1}}.
\]
两式相减：
\[
p^{M+t+1}\mid\mathcal M.
\]
但 `(1.9)` 精确给
\[
v_p(\mathcal M)=M+t,
\]
矛盾。因此必须
\[
\boxed{D_{\rm der}=0.}
\tag{6.1}

现在解 `(5.2)`。

若 `E>=j`，则 `M=E`，所以
\[
D_{\rm der}=4E+c-j>0,
\]
与 `(6.1)` 矛盾。

若 `j>E`，则 `M=j`，故
\[
5E+c-2j=0,
\]
即
\[
\boxed{c=2j-5E.}
\tag{6.2}
\]
于是
\[
x=c-j-E=j-6E.
\]
但
\[
j-6E\le j-E=(j-E)_+,
\]
又与反设 `(2.1)` 的 `x>(j-E)_+` 矛盾。

所以反设不可能，证明
\[
\boxed{
 x_p\le
 \max\Bigl(v_p(C),v_p(N_0),v_p(R_3^{\rm den})\Bigr).
}
\]

---

## 7. 全局整数形式

对 `p|X_Q`，`tail-rough-d0-allocation.md` 已给 equal-prefix ledger，所以
\[
v_p(R_3^{\rm den})=(j-E)_+.
\]
`General-transfer-local` 因而说明
\[
v_p(X_Q)
\le
v_p\!\left(\operatorname{lcm}(C,N_0,R_3^{\rm den})\right).
\]
而 `X_Q` 只含 odd non-decimal primes，所以可安全抽掉 2、5 smooth part：
\[
\boxed{
X_Q\mid
\operatorname{lcm}\!\left(
\operatorname{core}_{10}(C),
\operatorname{core}_{10}(N_0),
\operatorname{core}_{10}(R_3^{\rm den})
\right).
}
\]

其中
\[
N_0=\frac{\mathcal N_{12}}{(b_1,b_2)^2}
\in\mathbf Z_{>0}.
\]
这严格推广了 `tail-source-cancellation-transfer.md` 的 baseline-free theorem；当
`E=j=0` 时，`R_3^{den}` 为 `p`-unit、`N_0=N_12`、`x_p=c`，恰恢复
\[
c\le\max(v_p(C),v_p(N_{12})).
\]

---

## 8. third payer 继续进入 projective/gap system

`R_3^{den}` 的 non-decimal prime `p^r` 使 `y_1,y_2` 同时至少含 `p^r`，因此
\[
\operatorname{core}_{10}(R_3^{den})\mid g_y:=\gcd(y_1,y_2).
\]
`core.md` 的 stereographic denominator formula
\[
v_p(Z_0)=\max(0,v_p(g_y)+\omega_p-v_p(a))
\]
立即给
\[
\boxed{
\operatorname{core}_{10}(R_3^{den})\mid Z_0a.
}
\tag{8.1}

所以最终有
\[
\boxed{
X_Q\mid
\operatorname{lcm}\!\left(
\operatorname{core}_{10}(C),
\operatorname{core}_{10}(N_0),
\operatorname{core}_{10}(Z_0a)
\right).
}
\tag{8.2}

这一步本身不宣称三个 payer 独立，也不把其高度机械相加；它只是 canonical
prime-power allocation。后续优化必须继续按 `lcm` / sheet allocation避免 double-count。

---

## 9. 对 post-tail branch reoptimization 的意义

`tail-rough-cq-excess.md` 已有第二次 Schmidt rough lower
\[
\log R_x+\log(g_*/v)
\ge S-\log X_Q-o(S),
\]
其中左边两项已真实进入 exact small factor。

本文把唯一 loss `X_Q` 完全改写为
\[
\boxed{
\text{prefix numerator rough }C
\ \cup\ 
\text{primitive Gaussian norm }N_0
\ \cup\ 
\text{projective/gap }Z_0a.
}
\]
因此 non-canonical side branches 的剩余困难不再是 denominator source cancellation
本身，而是这三类 numerator/projective payer能否同时承载正线性 rough height。

这正是下一步可与 carrier-circle / Gaussian angle / digit-shell height联立的接口。

---

## 10. 状态摘要

- **`已严格完成`**：`General-transfer-local/global/projective`。
- **`已严格完成`**：baseline-free `Source-transfer-local` 被本文严格包含为特例。
- **`结构压缩`**：post-tail second-Schmidt 的唯一 rough loss `X_Q` 被完全转移到
  `C / N_0 / Z_0a` 三 payer。
- **`待证`**：三 payer 的 independent excess height；完成 non-canonical dominant
  branch reoptimization，决定能否把全 DD explicit limsup升级到 `<=6`；absolute height / emptiness。

---

<a id="source-tail-rough-projective-bottom-two-payer"></a>

> 整合来源：`tail-rough-projective-bottom-two-payer.md`

# DD post-tail rough loss 的 projective / bottom two-payer collapse

> **依赖：** [`tail-rough-canonical-payer-decomposition.md`](tail-allocation-ledger.md#source-tail-rough-canonical-payer-decomposition)、
> [`tail-rough-third-angular-absorption.md`](tail-allocation-ledger.md#source-tail-rough-third-angular-absorption)、
> `core.md` 的 stereographic projective denominator formula。
>
> **严格状态：** `已严格完成（整个 `X_Q` odd rough support）`。
>
> canonical four-payer decomposition写
> \[
> x=e_3+e_B+e_G+e_A
> \]
> primewise。本文证明 projective/gap reader `Z_0a` 不只支付 third-exclusive `e_3`：
> 它自动同时支付 denominator-induced ghost common depth、numerator common depth与 primitive
> Gaussian angular depth。因此
> \[
> \boxed{
> e_3+e_G+e_A\le v_p(Z_0a).
> }
> \tag{Projective-absorb-all}
> \]
> 对每个 `p|X_Q` 成立。
>
> 定义
> \[
> e_P:=e_3+e_G+e_A.
> \]
> 全局得到最终 two-payer normal form
> \[
> \boxed{X_Q=X_PX_B,}
> \]
> \[
> \boxed{X_P\mid\operatorname{core}_{10}(Z_0a),}
> \]
> \[
> \boxed{X_B\mid\operatorname{core}_{10}(C_{12})\mid\operatorname{core}_{10}(R_{12}).}
> \]
> 因而 second-Schmidt 的唯一 rough loss不再需要独立的 Gaussian/common-numerator height
> pool：最终只剩 **projective/gap sheet** 与 **bottom-carrier sheet**。

---

## 1. local denominator / numerator data

固定
\[
p^x\Vert X_Q,
\qquad p\nmid10.
\]
`tail-rough-d0-allocation.md` 已证明
\[
\boxed{v_p(b_1)=v_p(b_2)=E.}
\tag{1.1}
写
\[
j:=v_p(b_3),
\qquad
M:=\max(E,j),
\]
并定义 third-exclusive depth
\[
\boxed{r:=(j-E)_+=M-E.}
\tag{1.2}
这正是
\[
v_p(R_3^{\rm den})=r.
\]

令 numerator valuations
\[
A_i:=v_p(a_i),
\]
以及 common numerator depth
\[
\boxed{g:=\min(A_1,A_2)=v_p(a_1,a_2).}
\tag{1.3}
`tail-rough-angular-source-transfer.md` 已证明在 `X_Q` support上这也等于
cross numerator common scale `g_A` 的 p-depth。

因为 `q_lcm` 的 p-depth为 `M`：
\[
y_i=a_iq_{\rm lcm}/b_i
\]
给
\[
v_p(y_1)=A_1+r,
\qquad
v_p(y_2)=A_2+r.
\]
因此 ghost common scale
\[
g_y=(y_1,y_2)
\]
满足
\[
\boxed{v_p(g_y)=r+g.}
\tag{Ghost-common}

---

## 2. primitive ghost angular depth就是 `N_ang`

写
\[
y_1=p^{r+g}Y_1,
\qquad
 y_2=p^{r+g}Y_2,
\]
其中 `(Y_1,Y_2)` 至少一项为 p-unit。

又写
\[
b_i=p^EB_i,
\qquad p\nmid B_1B_2,
\]
后者来自 `p|X_Q|C_Q=B_1 10^{m_2}+B_2` 与 `(B_1,B_2)=1`。

令
\[
\bar a_i=a_i/(a_1,a_2).
\]
则 p-adically `(Y_1,Y_2)` 与
\[
(\bar a_1B_2,\bar a_2B_1)
\]
只差共同 p-unit scale。因此
\[
\boxed{
\omega:=v_p(N_{\rm ang})
=v_p(Y_1^2+Y_2^2),
}
\tag{Angular=ghost-general}
其中
\[
N_{\rm ang}
=(\bar a_1B_2)^2+(\bar a_2B_1)^2.
\]

所以
\[
\boxed{
v_p(y_1^2+y_2^2)=2(r+g)+\omega.}
\tag{2.1}

---

## 3. stereographic denominator直接吸收 common + angle

DD sphere factorization：
\[
(H-y_3)(H+y_3)=y_1^2+y_2^2.
\]
gap normalization：
\[
H-y_3=La.
\]
当前 `p∤10` 且 `L|10^m`，故
\[
p\nmid L,
\qquad
\alpha:=v_p(La)=v_p(a).
\]

`core.md` 的 exact projective denominator formula为
\[
\boxed{
v_p(Z_0)=
\max(0,v_p(g_y)+\omega-\alpha).
}
\tag{3.1}
使用 `(Ghost-common)`：
\[
\boxed{
v_p(Z_0)=
\max(0,r+g+\omega-v_p(a)).
}
\tag{3.2}
因此
\[
\begin{aligned}
v_p(Z_0a)
&=v_p(a)+v_p(Z_0)\\
&=\max(v_p(a),r+g+\omega).
\end{aligned}
\]
特别地
\[
\boxed{
v_p(Z_0a)\ge r+g+\omega.}
\tag{Projective-capacity}

这条式子同时包含上一文件 third-angular two-sheet theorem；后者是 `g=0,r>0`
时的显式 sphere-sheet展开。

---

## 4. canonical angular remainder总有 `e_A<=omega`

`tail-rough-canonical-payer-decomposition.md` 定义
\[
e_3=\min(x,r),
\]
随后按顺序定义 `e_B,e_G,e_A`，并有
\[
e_G\le g.
\]
显然
\[
\boxed{e_3\le r,
\qquad e_G\le g.}
\tag{4.1}
唯一需要重新确认的是
\[
e_A\le\omega.
\]

若 `e_A=0` 无事可证。设 `e_A>0`。这意味着前三层不足以支付 `x`，所以它们
都达到容量：
\[
e_3=r,
\qquad e_B=t,
\qquad e_G=g,
\]
其中
\[
t:=v_p(C).
\]
于是
\[
\boxed{x>r+t+g.}
\tag{4.2}

`tail-rough-gaussian-payer-split.md` 的 general transfer refinement给
\[
\boxed{x\le\max(t,2g+\omega,r).}
\tag{4.3}
由于 `(4.2)` 特别给 `x>t,r`，只能
\[
x\le2g+\omega.
\]
而 `g<=t`，故
\[
\begin{aligned}
e_A
&=x-r-t-g\\
&\le2g+\omega-r-t-g\\
&=\omega-(r+t-g)\\
&\le\omega.
\end{aligned}
\]
所以
\[
\boxed{e_A\le\omega.}
\tag{Angular-capacity}

---

## 5. 三个 non-bottom layers一次性进入 `Z_0a`

由 `(4.1)` 与 `(Angular-capacity)`：
\[
 e_3+e_G+e_A
\le r+g+\omega.
\]
再由 `(Projective-capacity)`：
\[
\boxed{
 e_3+e_G+e_A
\le v_p(Z_0a).
}
\tag{Projective-absorb-all}

定义
\[
\boxed{e_P:=e_3+e_G+e_A.}
\tag{5.1}
则逐 prime有
\[
p^{e_P}\mid Z_0a.
\]

剩余唯一 layer就是 `e_B`，且
\[
x=e_P+e_B.
\tag{5.2}

---

## 6. global two-payer factorization

定义
\[
\boxed{X_P:=\prod_{p|X_Q}p^{e_P(p)},}
\]
\[
\boxed{X_B:=\prod_{p|X_Q}p^{e_B(p)}.}
\]
由 `(5.2)`：
\[
\boxed{X_Q=X_PX_B.}
\tag{Two-payer-product}

`Projective-absorb-all` 给
\[
\boxed{X_P\mid\operatorname{core}_{10}(Z_0a).}
\tag{Projective-payer}

而 canonical payer decomposition已证明
\[
\boxed{X_B\mid\operatorname{core}_{10}(C_{12}),}
\qquad
C_{12}=(A_{12},Q),
\]
并由 orientation-uniform bottom identity
\[
\boxed{C_{12}\mid R_{12}}
\]
得到
\[
\boxed{X_B\mid\operatorname{core}_{10}(R_{12}).}
\tag{Bottom-payer}

所以最终：
\[
\boxed{
X_Q=X_PX_B,
\quad
X_P\mid Z_0a,
\quad
X_B\mid C_{12}\mid R_{12}.
}
\tag{Two-payer-normal-form}

---

## 7. 对此前 payer files 的重新定位

这条 theorem严格加强前几步：

- `tail-rough-gaussian-payer-split.md` 的 `N_ang` 仍提供 primitive angular reader，但其
  height不再需要单独计入最终 `X_Q` budget；
- `tail-rough-angular-source-transfer.md` 的 `N_num` orientation与 cyclotomic overlap仍是
  bottom/angular local structure，但不是最终必需的第三 height pool；
- `tail-rough-third-angular-absorption.md` 是本文在 `r>0,g=0` 子情形的更显式
  sphere two-sheet版本；
- `tail-rough-bottom-angular-cyclotomic-split.md` 仍是正确的细分，但 two-payer theorem
  对最终 height accounting更强。

因此 branch reoptimization 的 hard loss已从
\[
C_Q\to X_Q\to\text{four/five payers}
\]
进一步压成
\[
\boxed{
X_Q\rightsquigarrow
\text{projective/gap }(Z_0a)
+\text{ bottom }(C_{12},R_{12}).
}

---

## 8. 下一步

第二次 Schmidt已有
\[
\log R_x+\log(g_*/v)
\ge S-\log X_Q-o(S),
\]
而 `R_x` 与 `g_*/v` 都是真实 `F_-` factors。
现在唯一 loss为
\[
\log X_P+\log X_B,
\]
并有两个 concrete readers：
\[
X_P\mid Z_0a,
\qquad
X_B\mid R_{12}.
\]

下一任务因此非常明确：

1. 对 simultaneous projective/bottom depth建立 carrier-circle / determinant-tetrahedron
   eliminant；或
2. 证明两者任一达到正线性 `S` 高度时，已有 small-factor / digit-shell budget自动付费。

一旦 `log X_P+log X_B` 能得到比自由 `S` 更小的统一上界，就可把第二次 Schmidt
真正转成新的 explicit global slope，并继续冲击 DD `<=6`。

---

## 9. 状态摘要

- **`已严格完成`**：`Ghost-common`、`Angular=ghost-general`、`Projective-capacity`。
- **`已严格完成`**：`e_A<=omega` 与 `Projective-absorb-all`。
- **`已严格完成`**：`Two-payer-product / payer / normal-form`。
- **`结构压缩`**：post-tail rough loss最终只剩 projective/gap 与 bottom 两条 carrier边。
- **`待证`**：projective-bottom simultaneous eliminant / height；non-canonical branch reoptimization；DD global explicit `<=6` / absolute height。

---

<a id="source-tail-rough-third-angular-absorption"></a>

> 整合来源：`tail-rough-third-angular-absorption.md`

# DD third-exclusive / Gaussian-angular layers 的 sphere two-sheet absorption

> **依赖：** [`tail-rough-canonical-payer-decomposition.md`](tail-allocation-ledger.md#source-tail-rough-canonical-payer-decomposition)、
> [`tail-rough-angular-source-transfer.md`](tail-allocation-ledger.md#source-tail-rough-angular-source-transfer)、`core.md` 的
> integer sphere 与 stereographic denominator formula。
>
> **严格状态：** `已严格完成（`X_Q` support 中所有 third-exclusive primes）`。
>
> four-payer decomposition此前把同一 rough prime的 depth分为
> \[
> e_3+e_B+e_G+e_A.
> \]
> 本文证明：只要 third-exclusive capacity
> \[
> r:=v_p(R_3^{\rm den})>0,
> \]
> 同一个 prime上的 `e_3` 与 `e_A` 其实不需要两个 reader。integer sphere把
> third common scale与 primitive Gaussian angular depth锁在同一个二-sheet factorization里：
> \[
> \boxed{v_p(Z_0a)\ge r+\omega,}
> \qquad
> \omega:=v_p(N_{\rm ang}).
> \tag{Sphere-absorb}
> \]
> 而 canonical allocation在 `e_A>0` 时自动有
> \[
> e_3\le r,
> \qquad e_A\le\omega.
> \]
> 因此
> \[
> \boxed{p^{e_3+e_A}\mid Z_0a.}
> \tag{Layer-absorb-local}
> \]
>
> 结果：`X_A` 只有在 `R_3^{den}` 为 p-unit 的 primes上才需要继续作为独立
> numerator-Gaussian reader；所有与 third-exclusive denominator 共存的 angular depth都已
> 被 projective/gap sheet吸收。

---

## 1. third-exclusive prime 的 denominator / ghost ledger

固定
\[
p\mid X_Q,
\qquad p\nmid10,
\]
并假设
\[
\boxed{r:=v_p(R_3^{\rm den})>0.}
\tag{1.1}

`tail-rough-d0-allocation.md` 已给
\[
v_p(b_1)=v_p(b_2)=E.
\]
由 `R_3^{den}` 定义：
\[
\boxed{v_p(b_3)=j=E+r>E.}
\tag{1.2}
所以 `b_3` 是 p-adic unique maximum。

因为每个 `a_i/b_i` reduced：
\[
\boxed{p\nmid a_1a_2a_3.}
\tag{1.3}
整数球面 lcm denominator `q_lcm` 的 p-depth为 `j`，故
\[
y_i=a_iq_{\rm lcm}/b_i
\]
满足
\[
\boxed{
v_p(y_1)=v_p(y_2)=r,
\qquad v_p(y_3)=0.
}
\tag{1.4}

球面方程
\[
H^2=y_1^2+y_2^2+y_3^2
\]
模 `p` 于是给
\[
H^2\equiv y_3^2\not\equiv0\pmod p,
\]
所以
\[
\boxed{v_p(H)=0.}
\tag{1.5}

令
\[
g_y=(y_1,y_2).
\]
由 `(1.4)`：
\[
\boxed{v_p(g_y)=r.}
\tag{1.6}

---

## 2. primitive ghost angular depth就是 `N_ang`

写
\[
y_1=p^rY_1,
\qquad y_2=p^rY_2,
\]
其中 `Y_1,Y_2` 为 p-units。

另一方面
\[
b_i=p^EB_i\quad(i=1,2),
\qquad p\nmid B_1B_2.
\]
由于
\[
\frac{Y_1}{Y_2}
=rac{y_1}{y_2}
=rac{a_1b_2}{a_2b_1}
=rac{a_1B_2}{a_2B_1},
\]
存在 p-adic unit `lambda_p` 使
\[
(Y_1,Y_2)=\lambda_p(a_1B_2,a_2B_1)
\]
在 `Z_p^2` 中只差共同 unit scale。

而 `(1.3)` 与 `p∤B_1B_2` 给
\[
p\nmid(a_1,a_2),
\]
故在该 prime
\[
v_p(g_n)=0,
\qquad g_n=(a_1,a_2).
\]
所以
\[
N_{\rm ang}
=(\bar a_1B_2)^2+(\bar a_2B_1)^2
\]
的 p-depth正是 primitive ghost norm depth：
\[
\boxed{
\omega:=v_p(N_{\rm ang})
=v_p(Y_1^2+Y_2^2).
}
\tag{Angular=ghost}

因此
\[
\boxed{
v_p(y_1^2+y_2^2)=2r+\omega.}
\tag{2.1}

---

## 3. sphere factorization只有两个 sheets

integer sphere给
\[
(H-y_3)(H+y_3)=y_1^2+y_2^2.
\]
由 `(1.5)` 与 `v_p(y_3)=0`，`H,y_3` 都是 p-units。对 odd prime `p`：
\[
\boxed{
\min(v_p(H-y_3),v_p(H+y_3))=0,
}
\tag{3.1}
因为若两者同时被 p 整除，则 p同时整除 `2H,2y_3`，矛盾。

结合 `(2.1)`：
\[
\boxed{
\{v_p(H-y_3),v_p(H+y_3)\}
=\{0,2r+\omega\}.
}
\tag{Sphere-two-sheet}

DD gap normalization为
\[
H-y_3=La.
\]
当前 `p∤10` 且 `L|10^m`，故 `p∤L`。因此
\[
\boxed{v_p(a)=v_p(H-y_3).}
\tag{3.2}

所以两 sheets显式为：

### Gap sheet
\[
\boxed{
v_p(a)=2r+\omega,
\qquad v_p(H+y_3)=0.}
\tag{G}

### Complementary sheet
\[
\boxed{
v_p(a)=0,
\qquad v_p(H+y_3)=2r+\omega.}
\tag{C}

---

## 4. projective denominator 精确读取 complementary sheet

`core.md` 的 stereographic denominator为
\[
\boxed{
Z_0=\frac{H+y_3}{(g_y,H+y_3)}.
}
\tag{4.1}

在 Gap sheet，`H+y_3` 为 p-unit：
\[
v_p(Z_0)=0,
\]
故
\[
\boxed{v_p(Z_0a)=2r+\omega.}
\tag{4.2}

在 Complementary sheet：
\[
v_p(H+y_3)=2r+\omega,
\qquad v_p(g_y)=r,
\]
于是
\[
\boxed{v_p(Z_0)=r+\omega,}
\tag{4.3}
并因 `v_p(a)=0`：
\[
\boxed{v_p(Z_0a)=r+\omega.}
\tag{4.4}

两者统一：
\[
\boxed{
v_p(Z_0a)\ge r+\omega.
}
\tag{Sphere-absorb}

注意这比旧 general payer
\[
p^r\mid Z_0a
\]
多读出了整份 primitive Gaussian angular depth `omega`。

---

## 5. 吸收 canonical `e_3+e_A` layers

`tail-rough-canonical-payer-decomposition.md` 定义
\[
e_3=\min(x,r),
\]
然后顺序支付 `e_B,e_G,e_A`。
显然
\[
\boxed{e_3\le r.}
\tag{5.1}

当前 `r>0` 意味着 `j>E`；由 reducedness已在 §2 得到
\[
g=v_p(g_n)=0.
\tag{5.2}
因此 `e_G=0`。

若 `e_A=0`，直接由 `(Sphere-absorb)` 得
\[
e_3\le r\le v_p(Z_0a).
\]

下面设 `e_A>0`。sequential definition意味着
\[
x>r+t,
\]
其中 `t=v_p(C)`。general transfer在 `g=0` 时为
\[
x\le\max(t,\omega,r).
\]
因为 `x>t,r`，只能有
\[
\boxed{x\le\omega.}
\tag{5.3}
所以当然
\[
\boxed{e_A\le x\le\omega.}
\tag{5.4}

由 `(5.1),(5.4)`：
\[
e_3+e_A\le r+\omega.
\]
再用 `(Sphere-absorb)`：
\[
\boxed{
e_3+e_A\le v_p(Z_0a).
}
\tag{Layer-absorb-local}

---

## 6. global absorbed / residual angular split

把 `X_A` 按 `R_3^{den}` support分成 exponent layers：
\[
X_A=X_{A,3}X_{A,0},
\]
其中 `X_{A,3}` 收集所有 `r>0` primes上的 `e_A`，`X_{A,0}` 收集
`r=0` primes上的 `e_A`。

同样 `X_3` 全部只在 `r>0` support。逐 prime `(Layer-absorb-local)` 相乘得到
\[
\boxed{
X_3X_{A,3}\mid\operatorname{core}_{10}(Z_0a).
}
\tag{Global-absorb}

而 residual angular payer
\[
\boxed{X_{A,0}\mid\operatorname{core}_{10}(N_{\rm num})}
\tag{Residual-angular}
仍严格成立。

因此 four-payer decomposition可重写为
\[
\boxed{
X_Q
=(X_3X_{A,3})\,X_B\,X_G\,X_{A,0},
}
\]
其中第一括号已经是单一 projective/gap reader。

更重要的是：真正还需要独立 Gaussian orientation的 `X_{A,0}` 只支撑在
\[
\boxed{v_p(R_3^{\rm den})=0}
\]
的 primes上。也就是说 **third-exclusive denominator 与 Gaussian angular excess
不能形成两个独立 height pools**。

---

## 7. 当前 side-branch frontier

post-tail rough loss现在只剩三类真正不同机制：

1. **projective/gap combined layer**
   \[
   X_P:=X_3X_{A,3}\mid Z_0a;
   \]
2. **bottom/common numerator layers**
   \[
   X_B\mid C_{12}\mid R_{12},
   \qquad
   X_G\mid(a_1,a_2);
   \]
3. **residual split-Gaussian layer**
   \[
   X_{A,0}\mid N_{\rm num},
   \qquad R_3^{\rm den}\text{ is p-unit on its support}.
   \]

这比原 four-payer表少了一份可能重复计算的 `third + angular` height。
下一步应专门研究 residual `X_{A,0}` 与 bottom `X_B` / coefficient `A^circ` 的
cyclotomic overlap，以及 projective layer `X_P` 的 global height。

---

## 8. 状态摘要

- **`已严格完成`**：`Angular=ghost`、`Sphere-two-sheet`、`Sphere-absorb`。
- **`已严格完成`**：canonical `e_3+e_A` local absorption与 `Global-absorb`。
- **`结构压缩`**：third-exclusive denominator depth与同-prime Gaussian angular depth不再是独立 payer；residual Gaussian payer只存在于 `R_3^{den}`-unit support。
- **`待证`**：residual `X_{A,0}` / bottom `X_B` simultaneous height；projective layer `X_P` height；non-canonical dominant branch reoptimization；DD global explicit `<=6` / absolute height。

---

<a id="source-tail-rough-z0-only-frontier"></a>

> 整合来源：`tail-rough-z0-only-frontier.md`

# DD post-tail rough loss 的 `Z_0`-only frontier

> **依赖：** [`tail-rough-projective-bottom-two-payer.md`](tail-allocation-ledger.md#source-tail-rough-projective-bottom-two-payer)、
> [`tail-rough-bottom-small-factor-charge.md`](tail-allocation-ledger.md#source-tail-rough-bottom-small-factor-charge)、
> `gcd-normal-exact-small-factor.md`。
>
> **严格状态：** `已严格完成（整个 post-tail `X_Q` support）`。
>
> two-payer theorem给
> \[
> X_Q=X_PX_B,
> \qquad X_P\mid Z_0a,
> \qquad X_B\mid C_{12}.
> \]
> 本文把 projective product继续分成 sphere-gap 与 true projective denominator：
> \[
> X_P=X_aX_Z,
> \qquad X_a\mid a,
> \qquad X_Z\mid Z_0.
> \]
> exact small factor不仅支付 `X_B`，也支付 gap payer，并且两者各带一整份 prefix
> denominator height：
> \[
> \boxed{X_BG<F_-,}
> \qquad
> \boxed{X_aQ<F_-.}
> \]
> 因而 second-Schmidt 可自举为
> \[
> \boxed{
> 3\log F_-+\log X_Z\ge3S-o(S),
> }
> \tag{Triple-bootstrap}
> \]
> 即
> \[
> \boxed{
> \log F_-
> \ge S-\frac13\log X_Z-o(S).
> }
> \tag{Z0-bootstrap}
> \]
> 而 `X_Z` 同时仍是 `X_Q` 的 factor，所以
> \[
> \boxed{X_Z\mid\gcd(C_Q,Z_0).}
> \tag{Z0-only-loss}
> \]
> post-tail branch reoptimization因此只剩一个真正未收费对象：primitive denominator source
> concat `C_Q` 与 stereographic denominator `Z_0` 的 rough gcd。

---

## 1. projective payer 的 gap / denominator exponent split

`tail-rough-projective-bottom-two-payer.md` 对每个
\[
p^e\Vert X_P
\]
给
\[
e\le v_p(Z_0a)=v_p(Z_0)+v_p(a).
\]
定义 sequential split
\[
\boxed{e_a:=\min(e,v_p(a)),}
\tag{1.1}
\[
\boxed{e_Z:=e-e_a.}
\tag{1.2}
则自动有
\[
e_Z\le v_p(Z_0).
\]

全局定义
\[
\boxed{X_a:=\prod p^{e_a(p)},}
\qquad
\boxed{X_Z:=\prod p^{e_Z(p)}.}
\]
于是
\[
\boxed{X_P=X_aX_Z,}
\tag{1.3}
\[
\boxed{X_a\mid\operatorname{core}_{10}(a),}
\qquad
\boxed{X_Z\mid\operatorname{core}_{10}(Z_0).}
\tag{1.4}

结合 two-payer：
\[
\boxed{X_Q=X_aX_ZX_B.}
\tag{1.5}

---

## 2. gap payer同样带一整份 `S` discount

`gcd-normal-exact-small-factor.md` 的 exact factorization为
\[
\boxed{
F_-=a\,g_*\,L\frac{LQ+2\tau}{\tau}.
}
\tag{2.1}

unified tail weight给
\[
\frac\tau L=\frac{QG}{\kappa}.
\]
而严格 tail window
\[
QG<\kappa
\]
意味着
\[
\boxed{L/\tau>1.}
\tag{2.2}

所以从 `(2.1)`：
\[
\frac{F_-}{a}
=g_*L\frac{LQ+2\tau}{\tau}
>g_*L\frac{LQ}{\tau}
=g_*LQ\frac L\tau.
\]
其中 `g_*>=1`, `L>=1`, `L/tau>1`，故
\[
\boxed{aQ<F_-.}
\tag{Gap-charge}

由 `X_a|a`：
\[
\boxed{X_aQ<F_-.}
\tag{2.3}

ordinary denominator concat
\[
Q=b_1 10^{m_2}+b_2
\]
恰有 `S=m_1+m_2` 位，所以
\[
\boxed{10^{S-1}\le Q<10^S.}
\tag{2.4}
因此
\[
\boxed{
\log X_a<\log F_- -S+1.
}
\tag{Gap-height-charge}

---

## 3. bottom payer已有同样 discount

`tail-rough-bottom-small-factor-charge.md` 已严格证明
\[
\boxed{X_BG<F_-,}
\]
且
\[
10^{S-2}\le G<10^S.
\]
因此
\[
\boxed{
\log X_B<\log F_- -S+2.
}
\tag{Bottom-height-charge}

---

## 4. second-Schmidt 的 triple bootstrap

`tail-rough-cq-excess.md` 已有
\[
\boxed{
\log F_-
\ge S-\log X_Q-o(S).
}
\tag{4.1}
使用 `(1.5)`：
\[
\log F_-
\ge S-\log X_a-\log X_Z-\log X_B-o(S).
\]
再用 `Gap-height-charge` 与 `Bottom-height-charge`：
\[
\begin{aligned}
\log F_-
&\ge S-
(\log F_- -S+O(1))
-\log X_Z\\
&\qquad-
(\log F_- -S+O(1))-o(S).
\end{aligned}
\]
所以
\[
\boxed{
3\log F_-+\log X_Z
\ge3S-o(S).
}
\tag{Triple-bootstrap}

等价地
\[
\boxed{
\log F_-
\ge S-\frac13\log X_Z-o(S).
}
\tag{Z0-bootstrap}

由于 `X_Z|X_Q|C_Q` 且 `X_Z|Z_0`：
\[
\boxed{X_Z\mid\gcd(C_Q,Z_0).}
\tag{Z0-only-loss}

粗略使用 `C_Q<Q<10^S` 已给
\[
\log X_Z\le S+O(1),
\]
所以无条件还有
\[
\boxed{
\log F_-\ge\frac23S-o(S).
}
\tag{Two-thirds-F}
这已排除 post-tail small factor退化到 subexponential height，但尚不足以单独完成 full side-branch LP。

---

## 5. 当前唯一 hard object

现在 rough-source chain为
\[
C_Q
\to X_Q
\to(X_P,X_B)
\to(X_a,X_Z,X_B)
\to\boxed{X_Z=(C_Q,Z_0)\text{ 的一部分}}.
\]

其中：

- `X_a` 已由 exact gap factor带 `Q~10^S` 收费；
- `X_B` 已由 decimal determinant / universal identity带 `G~10^S` 收费；
- common numerator与 Gaussian angular depth都已在 projective theorem中吸收到 `Z_0a`；
- 唯一还没获得额外 `S` discount的是 `X_Z|gcd(C_Q,Z_0)`。

因此下一步不应再做 generic source gcd、Gaussian norm或 bottom determinant allocation。真正目标只有：

\[
\boxed{
\text{控制 primitive denominator concat }C_Q
\text{ 与 stereographic denominator }Z_0
\text{ 的 common rough height。}
}

可行接口包括 coefficient circle的 homogeneous equation、projective denominator exact valuation
formula，以及 `C_Q=B_1 10^{m_2}+B_2` 的 source root。

---

## 6. 状态摘要

- **`已严格完成`**：projective `X_a/X_Z` split。
- **`已严格完成`**：`Gap-charge` 与 `Gap-height-charge`。
- **`已严格完成`**：`Triple-bootstrap`、`Two-thirds-F`。
- **`结构压缩`**：post-tail branch reoptimization只剩 `X_Z|gcd(C_Q,Z_0)`。
- **`待证`**：`C_Q-Z_0` common rough height；non-canonical dominant branch reoptimization；DD global explicit `<=6` / absolute height。

---

<a id="source-tail-source-cancellation-transfer"></a>

> 整合来源：`tail-source-cancellation-transfer.md`

# DD baseline-free source cancellation 的 numerator transfer theorem

> **依赖：** [`tail-pure-cancellation-three-sheet.md`](tail-allocation-ledger.md#source-tail-pure-cancellation-three-sheet)、
> [`tail-hard-source-derivative-sheet.md`](tail-allocation-ledger.md#source-tail-hard-source-derivative-sheet)、
> DD gap quadratic。
>
> **严格状态：** `已严格完成（baseline-free odd rough primes）`。
>
> 固定
> \[
> p\nmid10b_1b_2b_3,
> \qquad p^c\Vert Q,\quad c>0.
> \]
> 则 source cancellation depth不可能悬空：
> \[
> \boxed{
> c\le
> \max\bigl(v_p(C),v_p(\mathcal N_{12})\bigr).
> }
> \]
> 换言之，完整 prime-power `p^c` 必须进入 numerator coefficient `C` 或 prefix
> Gaussian norm `N_12` 的至少一侧。证明的关键是：three-sheet中唯一可能未支付的
> hard `AB` sheet同时要求
> \[
> M\equiv C_0a\pmod{p^{c+\rho}}
> \]
> 与
> \[
> 2M\equiv C_0a\pmod{p^c}.
> \]
> 因为 hard sheet有 `rho<c`，两式模 `p^c` 相减便强迫 `p^c|M`，与
> `v_p(M)=rho` 矛盾。

---

## 1. 已知 local ledger

沿用 baseline-free hypotheses：

\[
p\nmid10b_1b_2b_3,
\qquad p^c\Vert Q,\quad c>0.
\]

前序文件已经证明：

\[
v_p(\nu)=0,
\qquad
v_p(\mu)=v_p(G_0)=v_p(a)=:\rho,
\]

\[
n:=v_p(\mathcal N_{12})\ge\rho,
\]

并记

\[
t:=v_p(C).
\]

unified quadratic的 divided term valuations为

\[
2\rho,\qquad \rho+t,\qquad c+n,
\]

所以只能位于 `AB/AD/BD` three-sheet。

---

## 2. 若 `n>=c` 或 `t>=c` 已完成支付

目标是证明

\[
c\le\max(t,n).
\]

若

\[
n\ge c
\]

或

\[
t\ge c
\]

已经结束。因此只需反设

\[
\boxed{n<c,\qquad t<c.}
\tag{2.1}

因为

\[
\rho\le n,
\]

于是

\[
\boxed{\rho<c.}
\tag{2.2}

---

## 3. `AD` 与 `BD` 在反设下自动消失

`AD` sheet要求

\[
c+n=2\rho.
\]

但 `n>=rho` 立刻给

\[
c\le\rho,
\]

与 `(2.2)` 矛盾。

`BD` sheet要求

\[
\rho+t=c+n,
\qquad t\le\rho.
\]

结合 `n>=rho` 得

\[
c\le t,
\]

与 `(2.1)` 的 `t<c` 矛盾。

所以反设下只能进入

\[
\boxed{AB\text{ sheet}.}
\tag{3.1}

`AB` 给

\[
\boxed{t=\rho,}
\qquad
c+n\ge2\rho.
\]

由于 `c>rho`、`n>=rho`，事实上

\[
\boxed{c+n>2\rho.}
\tag{3.2}

这正是 `tail-hard-source-derivative-sheet.md` 的 hard sub-sheet。

---

## 4. discriminant derivative要求 `M=C_0a`

hard derivative文件已证明，在 `(3.1),(3.2)` 下

\[
\boxed{v_p(W)=v_p(\Xi)=c+\rho,}
\]

其中

\[
\Xi=|\mathcal M-C_0a|.
\]

并且

\[
\mathcal M=q_{\rm lcm}C.
\]

简记

\[
\boxed{M:=\mathcal M.}
\]

baseline-free denominator意味着 `q_lcm` 为 `p`-unit；`t=rho` 给

\[
\boxed{v_p(M)=\rho.}
\tag{4.1}

又 `C_0=QL+2tau` 是 `p`-unit，而 `v_p(a)=rho`。所以

\[
\boxed{v_p(C_0a)=\rho.}
\tag{4.2}

`v_p(M-C_0a)=c+rho` 因而等价于 normalized derivative contact

\[
\boxed{
M\equiv C_0a
\pmod{p^{c+\rho}}.
}
\tag{Derivative-contact}

特别地当然也有

\[
M\equiv C_0a\pmod{p^c}.
\tag{4.3}

---

## 5. gap quadratic要求 `2M=C_0a` 模 `p^c`

DD gap quadratic为

\[
\boxed{
C_0a^2-2Ma+Q\frac{\mathcal S_{12}}L=0.
}
\tag{5.1}

baseline-free `p` 下 `L` 为 unit，并且

\[
v_p(\mathcal S_{12})=v_p(\mathcal N_{12})=n,
\]

因为 `q_lcm/G` 为 `p`-unit。

三项 valuations分别为：

\[
2\rho,
\qquad
2\rho,
\qquad
c+n.
\]

由 `(3.2)`：

\[
c+n>2\rho.
\]

所以前两项必须单独相消到第三项的深度：

\[
v_p(C_0a^2-2Ma)=c+n.
\]

约去 `a` 的 `rho` 层：

\[
\boxed{
v_p(C_0a-2M)=c+n-\rho.}
\tag{5.2}

而 `n>=rho`，故

\[
c+n-\rho\ge c.
\]

因此严格得到

\[
\boxed{
2M\equiv C_0a
\pmod{p^c}.}
\tag{Gap-contact}

注意这里**不能**一般加强为模 `p^{c+rho}`；前一版本曾把这一步写强，现已修正。
本文的矛盾只需要模 `p^c`。

---

## 6. 两 contacts 对 odd prime 不相容

将 `Derivative-contact` 降到模 `p^c`，与 `Gap-contact` 相减：

\[
M\equiv0\pmod{p^c}.
\]

但 `(4.1)` 给

\[
v_p(M)=\rho<c.
\]

矛盾。

因此反设 `(2.1)` 不成立，证明

\[
\boxed{
 c\le\max(t,n)
 =\max\bigl(v_p(C),v_p(\mathcal N_{12})\bigr).
}
\tag{Source-transfer-local}

---

## 7. prime-power transfer 的整数形式

定义 baseline-free source cancellation part

\[
X_{Q,0}
:=
\prod_{\substack{p\nmid10b_1b_2b_3\\p^c\Vert Q}}
 p^c.
\]

对每个 prime，`Source-transfer-local` 说明其完整 exponent `c` 被
`C` 或 `N_12` 的最大 exponent覆盖。因此

\[
\boxed{
X_{Q,0}
\mid
\operatorname{lcm}(C,\mathcal N_{12}).
}
\tag{Source-transfer-global}

特别地

\[
\log X_{Q,0}
\le
\log C+\log\mathcal N_{12},
\]

但后续做 height optimization时应使用 `lcm` / primewise max，而不是把两边高度
机械相加造成 double-count。

---

## 8. 含义与下一步

这条 theorem第一次把 denominator-prefix 的 pure cancellation depth转移到 numerator-side
两个明确 carrier：

\[
\boxed{C\quad\text{or}\quad\mathcal N_{12}.}
\]

其中：

- `C=10^dA_12` 是 DD weighted prefix numerator coefficient；
- `N_12` 是 prefix Gaussian norm。

因此 `tail-rough-cq-excess.md` 的最坏 `E=j=0` pool已经不再是匿名 source gcd。

下一步有两条：

1. 将一般 `E,j>0` 的 normalized overflow `x_p` 约去 denominator baseline后归约到本文，
   争取证明整个 `X_Q` 都进入 normalized `C/N_12`；
2. 在 height层面审计 `C` 的 forced decimal `10^d` 与 `N_12` 的 common/angle depth，
   避免把已有 digit baseline重复收费。

---

## 9. 状态摘要

- **`已严格完成`**：hard derivative sheet为空；`Source-transfer-local/global`。
- **`结构压缩`**：baseline-free primitive denominator cancellation完整转入 numerator
  coefficient或 prefix Gaussian norm。
- **`待证`**：一般 baseline normalized transfer；`C/N_12` 的 independent excess高度；
  post-tail branch reoptimization；DD global explicit slope / absolute height。

---

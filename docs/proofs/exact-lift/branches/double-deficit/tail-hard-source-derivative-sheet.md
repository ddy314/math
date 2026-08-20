# DD baseline-free `Q` cancellation 的 hard derivative sheet

> **依赖：** [`gcd-normal-exact-small-factor.md`](gcd-normal-exact-small-factor.md)、
> [`tail-pure-cancellation-three-sheet.md`](tail-pure-cancellation-three-sheet.md)、
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

# A2 `Rstar_63/D_63` overlap 的 resultant no-go

> **依赖：** `spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-height-remainder-descent.md`。
>
> **严格状态：**fully primitive short remainder `Rstar_63` 与 descended quotient `D_63` 的 common prime正是 original/remainder parity reuse的唯一剩余 overlap。本文审计两个最自然的 elimination方向。对 top defect `C` 的 linear resultant精确退化为 `(2K-9)That_2`，在 common branch上完全自动；对 `K` 的 resultant虽产生一个新 quadratic discriminant，但其唯一 nonsquare-looking factor `H_63` 在 `That_2=0` 上精确退化为 `c_u^2g^2(TK-9T-2a_3)^2`。因此 ordinary resultant/Legendre路线没有新的 generic obstruction；只有两个显式 singular gates `TK-9T-2a_3` 与 `1270B^2-Q^2N_0` 值得继续。本文是 no-go + singular reduction，不关闭 A2。

---

## 1. cleared overlap equations

令

\[
A_m:=2^m,
\qquad
V_d:=5^d,
\qquad
P_\lambda:=5^\lambda,
\]
所以

\[
T=A_mV_dP_\lambda.
\]

将 descended primitive quadratic `F_63` 清掉 denominator `16`：

\[
\boxed{
\begin{aligned}
F_{63}^{(16)}:={}&
16(2K-9)
\{g((2K-12)T-2a_3)+P_\lambda C\}\\
&-63gTK^2.
\end{aligned}}
\tag{1.1}
\]

对 genuine overlap prime `p∤2c_u`：

\[
p\mid\mathscr D_{63}
\Longleftrightarrow
p\mid F_{63}^{(16)}.
\]

另一方面 fully primitive remainder的 exact formula由 parent expansion给

\[
\boxed{
\begin{aligned}
16\mathscr R_{63}^\star
={}&A_m^2V_dc_u^2g^2
(15K^2+384K-848)\\
&-16A_mgc_u^2C(2K-9)\\
&-16V_dQ_0^2N_0.
\end{aligned}}
\tag{1.2}
\]

记右边为 `R_63^(16)`。

所以 genuine common support满足

\[
F_{63}^{(16)}=R_{63}^{(16)}=0\pmod p.
\]

---

## 2. eliminating `C` exactly recovers the original carrier

两式对 `C` 都是一次式。直接求 resultant并使用 `T=A_mV_dP_lambda`：

\[
\boxed{
\operatorname{Res}_C(
F_{63}^{(16)},R_{63}^{(16)}
)
=256(2K-9)\widehat{\mathcal T}_2.}
\tag{2.1}
\]

这里

\[
\boxed{
\begin{aligned}
\widehat{\mathcal T}_2
={}&A_mc_u^2g^2
[TK^2-(18T+4a_3)K+18a_3+55T]\\
&-5^mQ_0^2N_0.
\end{aligned}}
\tag{2.2}
\]

但是 parent descent已经证明

\[
p\mid\mathscr R_{63}^\star,\quad
p\mid\mathscr D_{63}
\Longrightarrow
p\mid\widehat{\mathcal T}_2.
\]

所以 (2.1) 对 noncentral `p∤2K-9` 不增加任何条件；central `2K-9` 也已是旧 additive overlap gate。

因此：

\[
\boxed{
C\text{-resultant is an exact syzygy, not a new obstruction}.}
\tag{2.3}
\]

---

## 3. eliminating `K` gives only a quadratic in `C`

反过来对 `K` 求 resultant。除去显式 unit/content factor

\[
256A_m^2g^2V_d^2,
\]
剩余是关于 `C` 的 quadratic `R_C(C)`。

无需记录其冗长 coefficients；真正决定 generic root character的是 discriminant。直接 factor得到

\[
\boxed{
\begin{aligned}
\operatorname{Disc}_C(R_C)
={}&4096P_\lambda^2c_u^2
\left(
1270A_m^2c_u^2g^2-N_0Q_0^2
\right)^2\\
&\cdot\mathscr H_{63},
\end{aligned}}
\tag{3.1}
\]

其中

\[
\boxed{
\mathscr H_{63}
:=
c_u^2g^2(26T^2+18Ta_3+4a_3^2)
+5^{2m}Q_0^2N_0.}
\tag{3.2}
\]

所以除 fixed/content factors外，表面上唯一可能产生 independent quadratic character的是 `H_63`。

---

## 4. `H_63` becomes an exact square on the original carrier

在任何 genuine common prime上已有

\[
\widehat{\mathcal T}_2\equiv0\pmod p.
\]

由 (2.2)：

\[
5^mQ_0^2N_0
\equiv
A_mc_u^2g^2
[TK^2-(18T+4a_3)K+18a_3+55T]
\pmod p.
\]

再乘 `5^m`，并使用

\[
A_m5^m=T:
\]

\[
5^{2m}Q_0^2N_0
\equiv
Tc_u^2g^2
[TK^2-(18T+4a_3)K+18a_3+55T]
\pmod p.
\tag{4.1}
\]

代入 (3.2)：

\[
\begin{aligned}
\mathscr H_{63}
\equiv c_u^2g^2\{&
26T^2+18Ta_3+4a_3^2\\
&+T[TK^2-(18T+4a_3)K+18a_3+55T]
\}.
\end{aligned}
\]

大括号精确平方：

\[
\boxed{
26T^2+18Ta_3+4a_3^2
+T[TK^2-(18T+4a_3)K+18a_3+55T]
=(TK-9T-2a_3)^2.}
\tag{4.2}
\]

因此

\[
\boxed{
\mathscr H_{63}
\equiv
c_u^2g^2(TK-9T-2a_3)^2
\pmod p.}
\tag{4.3}
\]

在 `p∤c_ug` generic sector，这就是显式平方。

故 (3.1) 的整个 discriminant在 generic overlap上自动为平方：

\[
\boxed{
\text{ordinary }K\text{-resultant Legendre test adds no new generic obstruction}.}
\tag{4.4}
\]

---

## 5. only two singular gates remain

`K`-resultant quadratic出现 repeated root只可能来自 discriminant factors。

除固定 `2,5,c_u` 外，真正需要单列的是：

### A. third/central gate

\[
\boxed{TK-9T-2a_3\equiv0\pmod p.}
\tag{5.1}
\]

这正是此前 source/shifted-pair analysis中已经出现的 central third-block linear form。

### B. pure-prefix gate

另一个 square factor为

\[
1270A_m^2c_u^2g^2-N_0Q_0^2.
\]

使用

\[
A_m c_ug=\frac{B}{2^{M+1}},
\qquad
Q_0=\frac{Q}{2^{M+1}},
\]
乘回公共 denominator得到 pure-prefix integer

\[
\boxed{
\mathscr F_{1270}
:=1270B^2-Q^2N_0.}
\tag{5.2}
\]

所以第二个 singular branch只是

\[
\boxed{p\mid\mathscr F_{1270}.}
\tag{5.3}
\]

真实 endpoint中 `Q^2N_0` 为 `O(N^4)` 而 `1270B^2` 仅 `O(N^2)`，故 `F_1270<0` 对大 `M` 明显远离 real zero；但 simple p-adic roots仍可能存在，不能仅凭符号排除。

---

## 6. revised overlap frontier

因此 `Rstar_63/D_63` common support的 generic quadratic elimination已经审计完毕：

1. 消 `C` 只回到 original `That_2`；
2. 消 `K` 的 apparent new discriminant在 `That_2=0` 上自动成为平方；
3. 剩余 singular support只在
   \[
   TK-9T-2a_3
   \]
   与
   \[
   1270B^2-Q^2N_0
   \]
   两张显式低维 gate。

所以下一步不应继续叠 ordinary resultants/Legendre symbols。最有价值的是审计 `F_1270` 与 original prime-source三类的 support交集，或者利用 `Rstar_63<That_2/(24*5^lambda)` 的 height drop做 multiplicative budget。

A2 仍为 `待证`。

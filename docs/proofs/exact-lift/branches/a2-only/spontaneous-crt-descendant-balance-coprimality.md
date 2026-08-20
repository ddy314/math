# A2 parent-balance tail 的 coprime coordinates、`1/23` gap 与 cross-gate reuse

> **依赖：** `spontaneous-crt-descendant-balance-tail.md`、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descended-quotient-orientation.md`。
>
> **严格状态：**canonical balance tail使用 parent summands `X=5^lambda Rstar_63`、`Y=g2^m Dhat_63`。本文证明它们的完整 gcd恰为 `G_Delta`：`Rstar` 已与 `10g` 互素，而 `Dhat` 模5是显式 unit。故除去 common baseline后得到互素正整数 coordinates `Xbar,Ybar`。old short-remainder height drop立即给 `0<Xbar/Ybar<1/23`，与 recycling geometric ratio `<-1` 形成超过1的 real gap。balance tail进一步写成 `81 Xbar A_< + 2 Ybar A_>` 的正两项和；互素性给 exact cross-gcd identities，说明 tail prime若回流到某个 parent residual coordinate，必须命中另一侧 fixed gate。本文仍不排除完全 external tail prime或 p-adic balance wrapping，因此不关闭 A2。

---

## 1. `Dhat_63` is a `5`-adic unit

已有

\[
\widehat{\mathscr D}_{63}=c_u^2\mathscr F_{63},
\]

\[
\mathscr F_{63}
=(2K-9)B_\Delta-rac{63}{16}gTK^2,
\]

\[
B_\Delta=g((2K-9)T-a_3)-H_0.
\]

当前

\[
K\equiv0\pmod5,
\qquad T\equiv0\pmod5,
\]
所以

\[
2K-9\equiv1\pmod5,
\]
且 `F_63` 的第二项模5消失。

source relation

\[
H_0=g(3T+a_3)-5^\lambda C
\]
给

\[
H_0\equiv ga_3\pmod5.
\]

因此

\[
B_\Delta
\equiv-ga_3-H_0
\equiv-2ga_3\pmod5,
\]
从而

\[
\boxed{
\widehat{\mathscr D}_{63}
\equiv-2c_u^2ga_3\not\equiv0\pmod5.}
\tag{1.1}

这里 `5∤c_ug` 由 source/mixed coprimality，`5∤a_3` 由 `5|b_3` 与 `(a_3,b_3)=1`。

所以

\[
\boxed{\gcd(\widehat D_{63},5)=1.}
\tag{1.2}

---

## 2. the full parent gcd is exactly `G_Delta`

定义

\[
X=5^\lambda Rstar,
\qquad
Y=g2^mDhat.
\]

已有

\[
\gcd(Rstar,10g)=1,
\]
所以

\[
\gcd(Rstar,g2^m)=1.
\]

由 (1.2)：

\[
\gcd(Dhat,5^\lambda)=1.
\]

同时 source coprimality给 `gcd(5,g)=1`。因此任意 common prime of `X,Y` 必同时来自 `Rstar,Dhat`；反向显然成立。于是

\[
\boxed{
\gcd(X,Y)
=\gcd(Rstar,Dhat)
=G_\Delta.}
\tag{2.1}

定义 reduced parent coordinates

\[
\boxed{
\bar X:=X/G_\Delta,
\qquad
\bar Y:=Y/G_\Delta.}
\tag{2.2}

则

\[
\boxed{
\bar X,\bar Y\in\mathbf Z_{>0},
\qquad
\gcd(\bar X,\bar Y)=1.}
\tag{2.3}

`Xbar` 为 odd，而 `Ybar` 保留 parent 2-power scale。

---

## 3. exact `1/23` real balance window

short remainder descent已有严格 height drop

\[
\boxed{
0<X=5^\lambda Rstar
<\frac1{24}\widehat T_2.}
\tag{3.1}

而

\[
\widehat T_2=X+Y.
\]

所以

\[
24X<X+Y
\Longrightarrow
23X<Y.
\]

因此

\[
\boxed{
0<\frac XY<\frac1{23}.}
\tag{3.2}

除去共同正因子不改变 ratio：

\[
\boxed{
0<\frac{\bar X}{\bar Y}<\frac1{23}.}
\tag{3.3}

这就是 equal-depth parent unit的真实 Archimedean代表。

上一 balance-tail theorem则证明 recycling需要的纯几何 ratio满足

\[
\boxed{
\chi_{geom}
=-\frac{2\mathfrak G_>}{81\mathfrak G_<}
<-1.}
\tag{3.4}

所以

\[
\boxed{
\frac{\bar X}{\bar Y}-\chi_{geom}>1.}
\tag{3.5}

real balance gap不只是异号，而是统一超过1。

---

## 4. balance tail is a positive coprime two-summand form

定义 positive fixed gates

\[
\boxed{A_<:=-\mathfrak G_< >0,}
\qquad
\boxed{A_>:=-\mathfrak G_> >0.}
\tag{4.1}

balance-tail definition化为

\[
\boxed{
\mathscr B_{63}
=81\bar X A_<+2\bar Y A_>.}
\tag{4.2}

所以其正性完全显式，不依赖 cancellation estimate。

结合 (3.4)：

\[
\mathscr B_{63}
=81\bar YA_<
\left(
\frac{\bar X}{\bar Y}-\chi_{geom}
\right).
\tag{4.3}

由 (3.5) 还得到严格 lower bound

\[
\boxed{
\mathscr B_{63}>81\bar Y A_<.}
\tag{4.4}

---

## 5. exact cross-gcd identities

由 (4.2) 与 `gcd(Xbar,Ybar)=1`：

\[
\begin{aligned}
\gcd(\mathscr B_{63},\bar X)
&=\gcd(2\bar YA_>,\bar X)\\
&=\gcd(A_>,\bar X),
\end{aligned}
\]
因为 `Xbar` 为 odd。因此

\[
\boxed{
\gcd(\mathscr B_{63},\bar X)
=\gcd(A_>,\bar X).}
\tag{5.1}

同理

\[
\begin{aligned}
\gcd(\mathscr B_{63},\bar Y)
&=\gcd(81\bar XA_<,\bar Y)\\
&=\boxed{
\gcd(81A_<,\bar Y).}
\end{aligned}
\tag{5.2}

所以对 non-`3` odd prime：

\[
\boxed{
p\mid\mathscr B_{63},\ p\mid\bar X
\Longrightarrow p\mid A_>,}
\tag{5.3}

\[
\boxed{
p\mid\mathscr B_{63},\ p\mid\bar Y,\ p\ne3
\Longrightarrow p\mid A_<.}
\tag{5.4}

tail若回流到某一 residual parent coordinate，必须支付**另一侧** unequal-depth fixed gate。

---

## 6. support trichotomy for balance-tail primes

任意 genuine non-`3` odd prime `r|B_63` 现在只有三种位置：

1. `r|Xbar`：由 (5.3) 同时 `r|A_>`；
2. `r|Ybar`：由 (5.4) 同时 `r|A_<`；
3. `r∤Xbar Ybar`：真正的 parent-external balance-tail prime。

由于 `Xbar,Ybar` 已互素，不存在第四种同时回流两边的 residual support。

特别地 same-prime recycling prime本身在 equal baseline除去 `G_Delta` 后属于第三类：它不再整除 `Xbar,Ybar`，却通过 p-adic ratio `chi_p=chi_geom` 整除 `B_63`。

---

## 7. updated frontier

canonical balance tail现在同时具有：

- positive integer form；
- exact parent baseline removal；
- coprime parent coordinates；
- real ratio window `(0,1/23)` vs geometric `<-1`；
- residual parent reuse的 cross-gate identities。

所以后续若要关闭 balance-tail odd parity，最自然的分类已经变成：

- cross-gate reuse (`A_<`/`A_>` fixed algebraic support)；
- genuine parent-external tail；
- equal-baseline same-prime p-adic balance wrapping。

A2 仍为 `待证`。

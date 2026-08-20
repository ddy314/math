# A2 fixed `23` `eta=2` `c=2` 的 `3`-primary angle exclusion

> **依赖：** `spontaneous-cq-fixed23-eta2-slots.md`、`spontaneous-angle-pair-q0-depth.md`、`primitive-reduction.md`。
>
> **严格状态：**唯一 `c=2` type 的 `c_Q=1587=3*23^2` 含一个奇指数 `3`-primary。此前 pure-`c_Q` generic depth law始终排除 `p=3`，所以这一因子必须单独审计。本文直接在真实 primitive angle integers上计算模 `3`，证明 `3` 根本不整除任一 angle sign。故 `3` 不进入 angle/additive common gcd，也不能作为该 type 的 inert odd-depth supplier。

---

## 1. primitive separation先给 `3 not divide a_2`

当前 reflection 有

\[
N_0=\left(\frac{9b_2}{2}\right)^2+a_2^2
=5^{\lambda-2}XY.
\tag{1.1}

canonical primitive separation给

\[
\gcd(XY,c_Q)=1.
\]
由于

\[
3\mid c_Q,
\qquad
3\ne5,
\]
得到

\[
3\nmid N_0.
\tag{1.2}

第一平方项显然被 `3^2` 整除，所以模 `3`：

\[
N_0\equiv a_2^2\pmod3.
\]
因此

\[
\boxed{3\nmid a_2.}
\tag{1.3}

记

\[
A:=a_2,
\qquad
B:=b_2,
\qquad
N:=10^M.
\]
于是 `A,N,T=10^m` 都是 `3`-进 units。

---

## 2. `Q`-contact固定 `B mod3`

当前

\[
Q=B+2N=2^{M+1}c_Qq.
\]
因为 `3|c_Q`：

\[
Q\equiv0\pmod3.
\]
故

\[
B\equiv-2N\equiv N\pmod3.
\tag{2.1}

特别地

\[
3\nmid B.
\]

---

## 3. exact angle core在模 `3` 下是 unit

真实 angle core为

\[
\mathcal U_\Omega
=(45B^2-2AN)^2
-A^2B(99B-4N).
\tag{3.1}

模 `3`：

\[
45\equiv99\equiv0,
\qquad
4\equiv1.
\]
所以

\[
\begin{aligned}
\mathcal U_\Omega
&\equiv
(-2AN)^2
-A^2B(-4N)\\
&\equiv
A^2N^2+A^2BN\\
&=A^2N(N+B)
\pmod3.
\end{aligned}
\tag{3.2}

由 (2.1)：

\[
N+B\equiv2N\equiv-N\pmod3.
\]
因此

\[
\boxed{
\mathcal U_\Omega
\equiv-A^2N^2
\not\equiv0
\pmod3.}
\tag{3.3}

---

## 4. 两个 angle signs 都是 `3`-进 units

真实 sign-pair angle integers为

\[
\mathcal O_\pm
=T\mathcal U_\Omega
\pm2A^2Qb_3.
\tag{4.1}

第二项含 `Q`，故被 `3` 整除。于是

\[
\mathcal O_\pm
\equiv T\mathcal U_\Omega
\pmod3.
\]
由 `3 not divide T` 与 (3.3)：

\[
\boxed{
3\nmid\mathcal O_+,
\qquad
3\nmid\mathcal O_-.}
\tag{4.2}

primitive normalization只除去 `2`-power，所以同样有

\[
\boxed{
3\nmid\widehat{\mathcal O}_+,
\qquad
3\nmid\widehat{\mathcal O}_-.}
\tag{4.3}

---

## 5. common gcd 中完全没有 `3`

无论 additive side 的 `3`-adic行为怎样，angle side已经是 unit。因此对任意包含 angle integer的 common gcd，特别是当前

\[
G_{\rm sp}
=\gcd(\widehat{\mathcal O}_+,\widehat{\mathcal T}_2),
\]
都有

\[
\boxed{v_3(G_{\rm sp})=0.}
\tag{5.1}

所以

\[
\boxed{
 c_Q=3\cdot23^2
\text{ 中的 odd }3\text{-primary 不贡献任何 common parity}.}
\tag{5.2}

这也说明 generic pure-`c_Q` 分析排除 `p=3` 没有遗漏一个潜在 closure shortcut；在最后的 `c=2` type中，真正开放的 pure-`c_Q` inert common prime仍是 fixed `23`。

---

## 6. 对 frontier 的影响

该 type 的 denominator square content从 mod-4 角度看含一个 `3`，但它在 angle primitive carrier中完全消失。因此后续 parity ledger不能使用 `c_Q=3 mod4` 本身推断 common gcd 的 parity。

剩余工作仍是：

1. fixed `23` 的 actual common depth；
2. source divisor / full canonical `a_3` representative；
3. reconstruction 后其它 residual prime pools的审计。

本文把唯一特殊 `p=3` loophole严格关闭。
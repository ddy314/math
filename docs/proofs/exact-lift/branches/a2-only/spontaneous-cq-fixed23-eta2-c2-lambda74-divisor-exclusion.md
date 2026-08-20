# A2 fixed `23` `eta=2` `c=2` 的 `lambda=74, c_u=3917` source-divisor exclusion

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-source-window.md`、`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md`、`spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`。
>
> **严格状态：**source window 在 `lambda=74` 留下 `c_u in {3917,3929}`。本文对 `c_u=3917` 的 source integer 做完整可验证分解。合法 centered source divisor `theta` 必须落在一个 80 位窄区间；而 source integer 的因子结构恰好分成一个 114 位素数与总乘积仅 42 位的其余因子。任何 divisor 因而要么过小、要么过大，centered interval 中没有 divisor。故 `(lambda,c_u)=(74,3917)` arithmetic source state 被严格排除。本文不处理同高度的 `c_u=3929`。

---

## 1. centered divisor requirement

当前唯一 `c=2` type 满足

\[
M=2\lambda,
\qquad
m=\lambda+1,
\qquad
c_Q=1587.
\]

source product为

\[
\boxed{
\mathscr S_\lambda(c_u)
=5^{3\lambda}+1587c_u
=g\theta.}
\tag{1.1}

并定义

\[
L_*:=2^{\lambda+1}5^\lambda c_u.
\tag{1.2}

`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md` 已把真实 divisor window收紧为

\[
\boxed{
\frac{39}{2}L_*<\theta<\frac{79}{4}L_*.}
\tag{1.3}

此外 `theta` 必须为正奇 divisor of `S_lambda(c_u)`。

本文固定

\[
\boxed{\lambda=74,\qquad c_u=3917.}
\tag{1.4}

此时

\[
L_*=2^{75}5^{74}\cdot3917
=\boxed{783400000000000000000000000000000000000000000000000000000000000000000000000000}.
\tag{1.5}

所以 (1.3) 的整数范围为

\[
\boxed{
15276300000000000000000000000000000000000000000000000000000000000000000000000000
<\theta
}
\tag{1.6a}

和

\[
\boxed{
\theta<
15472150000000000000000000000000000000000000000000000000000000000000000000000000.}
\tag{1.6b}

也就是说任何合法 `theta` 必为一个 80 位整数。

---

## 2. source integer 的完整分解

直接整数计算得到

\[
\boxed{
\begin{aligned}
\mathscr S_{74}(3917)
={}&2^8\cdot7\cdot149
\cdot1660311777398843\\
&\cdot755010757548746032247\\
&\cdot P_{114},
\end{aligned}}
\tag{2.1}

其中

\[
\boxed{
P_{114}
=443275675908365257356310830167221246577649755270106234437033874498268569377246437010851938887432890877364857937953
}
\tag{2.2}

为素数。

其余全部因子的总乘积为

\[
\boxed{
S_{\rm small}
:=2^8\cdot7\cdot149
\cdot1660311777398843
\cdot755010757548746032247
=334708746929231021723648971080910156928768.}
\tag{2.3}

这是一个 42 位整数。

checker 使用 exact multiplication 与 `sympy.isprime` 分别验证 (2.1) 和 (2.2)；因此这里不是依赖未证实的 probable-factor heuristic。

---

## 3. divisor gap

任取正 divisor

\[
d\mid\mathscr S_{74}(3917).
\]

因为 `P_114` 在 (2.1) 中指数为 `1`，只有两种情况。

### 3.1 `P_114 not divide d`

则

\[
d\mid S_{\rm small},
\]
所以

\[
\boxed{d\le S_{\rm small}.}
\tag{3.1}

而 exact comparison给

\[
\boxed{
S_{\rm small}
<\frac{39}{2}L_*.}
\tag{3.2}

故 `d` 太小，不能满足 centered window。

### 3.2 `P_114 | d`

则

\[
d\ge P_{114}.
\]
exact comparison给

\[
\boxed{
P_{114}
>\frac{79}{4}L_*.}
\tag{3.3}

所以 `d` 又太大。

综上，source integer中没有 divisor跨入 (1.3)：

\[
\boxed{
\operatorname{Div}(\mathscr S_{74}(3917))
\cap
\left(\frac{39}{2}L_*,\frac{79}{4}L_*\right)
=\varnothing.}
\tag{3.4}

---

## 4. arithmetic-state exclusion

source-only certificate要求真实 state 至少先提供一个 odd divisor

\[
\theta\mid\mathscr S_{74}(3917)
\]
满足 centered interval (1.3)。式 (3.4) 已在进入 `a_3` CRT、Gaussian orientation、canonical `3`-allocation之前否定这个必要条件。

因此得到严格排除：

\[
\boxed{
(\lambda,c_u)=(74,3917)
\Longrightarrow
\text{no arithmetic state in the final }c=2\text{ type}.}
\tag{4.1}

特别地，该 state 不再只是在 fixed-23 parity ledger中被标为 `d_23=1`；它从完整 arithmetic candidate set中消失。

---

## 5. 更新后的 `lambda=74` frontier

`spontaneous-cq-fixed23-eta2-c2-source-window.md` 原来给

\[
\lambda=74:\qquad c_u\in\{3917,3929\}.
\]

本文删除第一项，所以

\[
\boxed{
\lambda=74\Longrightarrow c_u=3929
}
\tag{5.1}

是该高度唯一仍需审计的 source content。

`c_u=3929` 的 source integer虽已有多个小因子，但剩余 127 位部分仍为合数；本文没有完整分解它，因此不对该 state 作越界结论。后续可继续 source divisor factor certificate，或绕过完整 factorization直接使用 full centered `a_3` map / natural representative。
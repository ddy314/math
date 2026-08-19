# A2 fixed `23` `eta=2` `c=2` 的 `lambda=52, c_u=29` source-divisor exclusion

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-source-window.md`、`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md`、`spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`。
>
> **严格状态：**source window 在最低允许高度 `lambda=52` 只留下 `c_u=29`。本文对 source integer 做完整可验证分解。centered source divisor `theta` 必须落在一个 56 位窄区间；而 source integer 的因子结构分成一个 72 位素数与总乘积仅 38 位的其余因子。任何 divisor 因而必定过小或过大。故 `(lambda,c_u)=(52,29)` 从完整 arithmetic candidate set 中严格排除。

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

source product 为

\[
\boxed{
\mathscr S_\lambda(c_u)
=5^{3\lambda}+1587c_u
=g\theta.}
\tag{1.1}
\]

并定义

\[
L_*:=2^{\lambda+1}5^\lambda c_u.
\tag{1.2}
\]

`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md` 已证明真实 source divisor 必须满足

\[
\boxed{
\frac{39}{2}L_*<\theta<\frac{79}{4}L_*.
}
\tag{1.3}

本文固定

\[
\boxed{\lambda=52,\qquad c_u=29.}
\tag{1.4}

此时

\[
L_*=580000000000000000000000000000000000000000000000000000.
\tag{1.5}

所以 centered interval 为

\[
\boxed{
11310000000000000000000000000000000000000000000000000000
<\theta
}
\tag{1.6a}

和

\[
\boxed{
\theta<
11455000000000000000000000000000000000000000000000000000.
}
\tag{1.6b}

任何合法 `theta` 因而必须是 56 位整数。

---

## 2. source integer 的完整分解

直接 exact integer factorization 得到

\[
\boxed{
\begin{aligned}
\mathscr S_{52}(29)
={}&2^3\cdot311\cdot1013\cdot1540787\\
&\cdot4691120092228268769101767\\
&\cdot P_{72},
\end{aligned}}
\tag{2.1}

其中

\[
\boxed{
P_{72}
=600954647989450344901853769984896357520599617802323154990245217256098773
}
\tag{2.2}

为素数。

除去 `P_72` 后，其余全部因子的总乘积为

\[
\boxed{
S_{\rm small}
=18217088908728795407321637435454176376.
}
\tag{2.3}

checker 使用 exact multiplication 与 `sympy.isprime` 验证 (2.1)–(2.2)。

---

## 3. divisor gap

任取正 divisor

\[
d\mid\mathscr S_{52}(29).
\]

因为 `P_72` 在完整分解中指数为 `1`，分两种情况。

### 3.1 `P_72` 不整除 `d`

此时

\[
d\mid S_{\rm small},
\]
所以

\[
d\le S_{\rm small}.
\]

而 exact comparison 给

\[
\boxed{
S_{\rm small}<\frac{39}{2}L_*.
}
\tag{3.1}

故 `d` 太小，不能进入 centered interval。

### 3.2 `P_72` 整除 `d`

此时

\[
d\ge P_{72}.
\]

而

\[
\boxed{
P_{72}>\frac{79}{4}L_*.
}
\tag{3.2}

故 `d` 又太大。

因此

\[
\boxed{
\operatorname{Div}(\mathscr S_{52}(29))
\cap
\left(\frac{39}{2}L_*,\frac{79}{4}L_*\right)
=\varnothing.}
\tag{3.3}

该结论比 `theta` 必须为 odd 更强：事实上 source integer 根本没有任何正 divisor 落入窗口。

---

## 4. arithmetic-state exclusion

source-only certificate要求真实 state 至少先存在

\[
\theta\mid\mathscr S_{52}(29)
\]
满足 centered interval。式 (3.3) 已否定这一必要条件，所以无需进入 Gaussian orientation、full `a_3` CRT 或 deterministic reconstruction。

因此

\[
\boxed{
(\lambda,c_u)=(52,29)
\Longrightarrow
\text{no arithmetic state in the final }c=2\text{ type}.}
\tag{4.1}

于是最后 `c=2` type 的最低实际 arithmetic height 已从 `lambda=52` 提升到至少

\[
\boxed{\lambda\ge63.}
\tag{4.2}

这里 (4.2) 是 arithmetic candidate 的高度下界；它不同于此前只针对 fixed-`23` common depth 的 source-content hierarchy。
# A2 fixed `7` omega-content / descendant central branch 的 finite Hensel audit

> **依赖：** `spontaneous-crt-omega-content-descent.md`、`spontaneous-omega-content-common.md`、`spontaneous-omega-biquadratic.md`。
>
> **严格状态：**omega-content/descendant overlap的 central denominator `2K-9=0` 只可能在 fixed non-3 prime `7` 出现。本文把 content angle gate、additive content gate与 central equation在 `F_7` 中完整枚举，只剩两组 genuine unit states；两点 Jacobian均非零，因此各自只有唯一 Hensel lift。fixed `7` central exception存在局部 branches，但没有 singular tree。本文是 finite/local rigidity，不是 global exclusion，也不关闭 A2。

---

## 1. normalized content system

沿用 omega-content normalized variables

\[
x=B/N,
\qquad y=10A/N,
\qquad \tau=N^{-1}=10^{-M}.
\]

content angle gate为

\[
\boxed{
F(x,y):=
202500x^4-(101x^2+4x+4)y^2-1800x^2y.}
\tag{1.1}

additive content gate为

\[
\boxed{
\begin{aligned}
G(x,y,\tau):={}&
100x^2[5(y+9)^2-36(y+9)\tau+55\tau^2]\\
&-(x+2)^2(2025x^2+y^2).
\end{aligned}}
\tag{1.2}

而

\[
K=N(9+y)=\frac{9+y}{\tau}.
\]

central descendant branch为

\[
2K-9\equiv0\pmod7.
\]

清去 unit `tau` 后定义

\[
\boxed{C_7(x,y,\tau):=2(y+9)-9\tau.}
\tag{1.3}

所以 fixed-7 local system为

\[
\boxed{F=G=C_7=0\quad\text{in }\mathbf F_7.}
\tag{1.4}

---

## 2. complete finite enumeration

枚举

\[
\tau\in\mathbf F_7^\times,
\qquad
x\in\mathbf F_7^\times,
\qquad
y\in\mathbf F_7
\]
并排除 q-boundary `x=-2`，得到恰好两组：

\[
\boxed{
(\tau,x,y)=(4,1,2),
\qquad
(5,4,3)
\pmod7.}
\tag{2.1}

两组都满足 `x(x+2) !=0`，故不是 denominator boundary。

source collision sheet为

\[
y=225x^2.
\]

模 `7` 有 `225=1`，而两点分别满足

\[
2\ne1^2,
\qquad
3\ne4^2=2.
\]

因此

\[
\boxed{\text{两点都不在 source sheet}.}
\tag{2.2}

结合 alpha-supported sheet uniqueness，它们是真正 omega-content states，而不是 height/source collision的重命名。

---

## 3. decimal length phases

因为

\[
\tau=10^{-M}\pmod7,
\qquad10\equiv3\pmod7,
\]
且

\[
\operatorname{ord}_7(10)=6,
\]
直接查六相位：

\[
\boxed{
\tau=4\Longleftrightarrow M\equiv2\pmod6,}
\tag{3.1}

\[
\boxed{
\tau=5\Longleftrightarrow M\equiv1\pmod6.}
\tag{3.2}

所以 central fixed-7 content/descent branch只存在于

\[
\boxed{M\equiv1\text{ or }2\pmod6.}
\tag{3.3}

注意这与此前 fixed-7 equal-depth target的 `M≡1 or5 mod6` 是不同局部 branch，不可混为同一 orbit。

---

## 4. both states are nonsingular

对三方程

\[
(F,G,C_7)
\]
关于

\[
(x,y,\tau)
\]
取 Jacobian determinant。

在两点分别得到

\[
\boxed{
\det J(1,2,4)\equiv1\pmod7,}
\tag{4.1}

\[
\boxed{
\det J(4,3,5)\equiv5\pmod7.}
\tag{4.2}

全部非零。因此 multivariate Hensel lemma给：

\[
\boxed{
\text{每个 first-layer state至多有一条 compatible }7\text{-adic lift}.}
\tag{4.3}

所以 fixed7 central omega-content/descent exception不是 singular Hensel tree，也不会在每层产生指数多个 residue choices。

---

## 5. current role

omega-content/descendant common branch现在分为：

1. noncentral simple branch：`C/D` 由 `K` 唯一确定，并进入 positive natural carrier `H_{omega Delta}`；
2. central branch：仅 fixed `7`，且只剩本文两条 simple Hensel orbits。

本文没有证明这两条 `7`-adic decimal exponent orbit最终不命中真实 integer candidate；机械继续提升 `7^k` 只会唯一固定更细相位，不能当作空性。

A2 仍为 `待证`。

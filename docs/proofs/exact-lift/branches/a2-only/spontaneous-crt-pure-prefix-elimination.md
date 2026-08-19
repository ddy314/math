# A2 pure-spontaneous / descendant common kernel 的最终 pure-prefix elimination

> **依赖：** `spontaneous-single-branch.md`、`spontaneous-sphere-roots.md`、`spontaneous-crt-universal-descendant-cubic.md`。
>
> **严格状态：**generic pure-spontaneous common prime已选定唯一 sphere branch `z_i(x,y)`，并满足 compact quadratic `L_i(tau)=0`。本文把 universal descendant cubic `E_63(K,zeta)=0` 代入 `K=s/tau,zeta=z_i/tau`，乘 `tau^8` 后对 `L_i` 做 exact Euclidean division。degree-8 compatibility modulo branch quadratic只剩一次 remainder `A_63 tau+B_63`；因此 generic coefficient branch中 decimal phase `tau=10^{-M}` 被唯一恢复。继续取 resultant可完全消去 `tau`，得到 degree-16 universal carrier `X_63(s,z,c)`；代入 `z_i(x,y),c(x,y)` 后成为只含 `(x,y)` 的 pure-prefix necessary condition。至此 third numerator、finite defect、prefix norm ratio和 decimal phase均已从 descendant common kernel消去。本文尚未证明 branch-specific pure-prefix carrier无有限域根，因此不关闭 A2。

---

## 1. compact branch quadratic

记

\[
s:=9+y,
\]

以及任一已选 sphere orientation

\[
z:=z_i(x,y),
\qquad i\in\{1,2\}.
\]

再定义

\[
\boxed{
c:=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.}
\tag{1.1}

`spontaneous-single-branch.md` 已证明 generic branch equation就是

\[
\boxed{
L_z(\tau)
:=55\tau^2+18(z-s)\tau+s^2-4sz-c=0.}
\tag{1.2}

这里

\[
\tau=10^{-M},
\qquad
K=s/\tau,
\qquad
\zeta=z/\tau.
\tag{1.3}

所有 sphere-root denominator在 genuine pure-spontaneous channel中均为 unit。

---

## 2. substitute the universal descendant cubic

前一文件构造 universal cubic

\[
\mathcal E_{63}(K,\zeta).
\]

定义

\[
\boxed{
\widetilde E_{63}(\tau;s,z)
:=\tau^8
\mathcal E_{63}(s/\tau,z/\tau).}
\tag{2.1}

因为 `E_63` 对 `K` 总次数最多 `8`，对 `zeta` 次数 `3`，(2.1) 是 genuine integer polynomial in `tau,s,z`，且

\[
\boxed{\deg_\tau \widetilde E_{63}=8.}
\tag{2.2}

现在在 polynomial ring

\[
\mathbf Z[s,z,c][\tau]
\]
中对 monic-up-to-unit quadratic `L_z` 做 Euclidean reduction。为避免除 `55` 引入无关 rational content，允许先在 `Q[s,z,c][tau]` 取余再清 primitive denominator。

exact computation给

\[
\boxed{
\widetilde E_{63}
\equiv
A_{63}(s,z,c)\tau+B_{63}(s,z,c)
\pmod{L_z}.}
\tag{2.3}

primitive normalization可选到

\[
\boxed{
\deg A_{63}=7,
\qquad A_{63}\text{ 有 }20\text{ 个 nonzero terms},}
\tag{2.4}

\[
\boxed{
\deg B_{63}=8,
\qquad B_{63}\text{ 有 }24\text{ 个 nonzero terms}.}
\tag{2.5}

完整 coefficients由 checker从 `E_63,L_z` 直接重建；正文不手抄机械大整数。

---

## 3. generic descendant branch uniquely recovers the decimal phase

若 genuine pure-spontaneous prime同时满足 branch equation与 descendant compatibility：

\[
L_z(\tau)\equiv0,
\qquad
\widetilde E_{63}(\tau;s,z)\equiv0
\pmod p,
\]
则由 (2.3)：

\[
\boxed{
A_{63}\tau+B_{63}\equiv0\pmod p.}
\tag{3.1}

若

\[
A_{63}\not\equiv0\pmod p,
\]
则 decimal phase不再是 free Hensel coordinate：

\[
\boxed{
\tau\equiv-B_{63}A_{63}^{-1}\pmod p.}
\tag{3.2}

所以在 generic coefficient branch中

\[
\boxed{
(x,y,i)
\Longrightarrow z_i
\Longrightarrow \tau
\Longrightarrow C/D}
\tag{3.3}

整个 first-layer local state已由 pure prefix branch唯一恢复。

若 `A_63=0`，common root还必须 `B_63=0`；这是新的 coefficient-singular subbranch，需单列，不能偷偷除去。

---

## 4. eliminate `tau` completely

对 quadratic (1.2) 与 linear remainder (3.1) 取 resultant。若写

\[
A:=A_{63},
\qquad B:=B_{63},
\]
则直接代 `tau=-B/A` 可得 universal formula

\[
\boxed{
\mathcal X_{63}(s,z,c)
:=55B^2
-18(z-s)AB
+(s^2-4sz-c)A^2.}
\tag{4.1}

任何 common root，无论 `A` 是否为零，都必须满足

\[
\boxed{\mathcal X_{63}\equiv0\pmod p.}
\tag{4.2}

exact coefficient audit给：未 primitive 化的 (4.1) 的全部 coefficient gcd恰为

\[
\boxed{5^7 11^7.}
\tag{4.3}

除去该固定 content后定义 primitive

\[
\boxed{
\mathcal X_{63}^{\rm prim}
:=\frac{\mathcal X_{63}}{5^7 11^7}.}
\tag{4.4}

它满足

\[
\boxed{
\deg\mathcal X_{63}^{\rm prim}=16,}
\tag{4.5}

并且 expanded support只有

\[
\boxed{59\text{ 个 nonzero monomials}.}
\tag{4.6}

当前 genuine pure-spontaneous prime已经排除 fixed coefficient primes `5,11`，所以 primitive normalization不丢任何 relevant root。

---

## 5. substitute the two rational sphere roots: pure prefix only

对每个 branch

\[
z=z_i(x,y),
\]
以及 (1.1) 的

\[
c=c(x,y),
\]
代入 (4.4)。清去 sphere-root denominator后定义 branch-specific primitive numerator

\[
\boxed{
\mathcal X_{63,i}^{\rm pref}(x,y)
:=
\operatorname{primnum}
\mathcal X_{63}^{\rm prim}
(s=9+y,z=z_i(x,y),c=c(x,y)).}
\tag{5.1}

于是 generic pure-spontaneous/descendant common prime必须满足

\[
\boxed{
\mathcal X_{63,i}^{\rm pref}(x,y)
\equiv0\pmod p}
\tag{5.2}

对它实际选择的唯一 branch `i`。

这是真正的 final local elimination：

\[
\boxed{
(a_3,b_3,C/D,\tau,Q^2N_0/B^2)
}
\]
全部不再出现在必要条件中，只剩

\[
\boxed{(x,y)\text{ 的 pure-prefix curve}.}
\tag{5.3}

---

## 6. relation to previous branch eliminants

旧 `Q_i(tau;x,y)=0` 单独允许一维 simple p-adic root family，因为 `tau` 仍是 decimal phase。

本文新增 `E_63=0` 后：

1. `E_63` modulo `Q_i/L_i` 只剩 linear remainder；
2. generic `tau` 被唯一恢复；
3. resultant `X_63` 进一步彻底消掉 `tau`。

因此 external descendant common kernel已从

\[
\text{single quadratic branch in }\tau
\]
下降成

\[
\boxed{\text{single pure-prefix algebraic curve in }(x,y).}
\]

这与旧 two-branch resultant `A_- C_*` 不同：本文没有让 `Q_1,Q_2` 同时消失，而是在**每个 branch内部**加入 descendant compatibility并消去 decimal phase。

---

## 7. proof boundary and next target

本文是结构性降维，不声称 degree-16 prefix carrier没有 finite-field roots。

下一步应分别对

\[
\mathcal X_{63,1}^{pref},
\qquad
\mathcal X_{63,2}^{pref}
\]
做：

- source line `d=225x^2-y` resultant；
- prefix norm defect `Delta_0` resultant；
- external discriminant `E_W` resultant；
- 或与 decimal relation `x=B/N,y=10A/N` 的 natural representative高度联立。

尤其应先检查 branch-specific numerator是否因回旧 `A_-`, `C_*`, `A_sp`；若只是旧 collision kernel，应明确降级。若出现新的 primitive factor，则它就是当前 alpha-free external common parity最直接的 pure-prefix obstruction。

A2 仍为 `待证`。

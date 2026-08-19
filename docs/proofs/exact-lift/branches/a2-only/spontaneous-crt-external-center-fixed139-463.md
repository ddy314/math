# A2 external discriminant-zero center 与 descendant common 的 fixed `139/463` orbits

> **依赖：** `external-secant-center.md`、`length-orbit.md`、`spontaneous-crt-universal-descendant-cubic.md`、`spontaneous-crt-height-descent-overlap.md`。
>
> **严格状态：**universal descendant cubic限制到 external discriminant-zero center `K=55/18, zeta=-55/18` 后，genuine external character只留下 fixed `139,463`。本文把这两枚 prime代回 `length-orbit.md` 的 fully coupled三方程，并与真实 decimal multiplicative orbit联立。`139` 留一组 genuine state，`463` 留两组；三点 full Jacobian均非零，且 `10` 的 exponent direction在相应 order上都非-Wieferich，所以每组至多一条唯一 p-adic decimal lift。它们与此前 height/source-common/descendant triple-overlap 的 fixed set `{139,463}` 完全一致，不构成新的第四 prime-source。本文不排除这三条 simple orbits，因此不关闭 A2。

---

## 1. universal cubic reduces the external center to `139,463`

external discriminant-zero common center给

\[
\boxed{
K_*=\frac{55}{18},
\qquad
\zeta_*=-\frac{55}{18}.}
\tag{1.1}

所以

\[
\alpha=T(K_*+\zeta_*)=0.
\]

universal descendant cubic在 `alpha=0`, 即 `zeta=-K`, 上因成

\[
\boxed{
\mathcal E_{63}(K,-K)
=-9G_D(K)^2Q_4(K),}
\tag{1.2}

其中

\[
G_D(K)=11K^2-240K+432,
\]

\[
Q_4(K)=5055K^4-44640K^3-91424K^2+612864K-539136.
\]

代入 `K=55/18`：

\[
\boxed{
G_D(55/18)
=-\frac{64357}{324}
=-\frac{139\cdot463}{324},}
\tag{1.3}

\[
\boxed{
Q_4(55/18)
=-\frac{12349325707}{34992}
=-\frac{257\cdot48051851}{34992}.}
\tag{1.4}

fully coupled external prime还必须满足

\[
p\equiv3\pmod4,
\qquad
\left(\frac{55}{p}\right)=1.
\tag{1.5}

四个 odd numerator primes中：

- `139,463` 均为 `3 mod4` 且 `(55/p)=1`；
- `257` 为 `1 mod4`；
- `48051851` 为 `3 mod4`，但 `(55/p)=-1`。

因此

\[
\boxed{
\text{external center}\cap\text{descendant common}
\subseteq\{139,463\}.}
\tag{1.6}

---

## 2. fully coupled finite-field equations

`length-orbit.md` 使用

\[
\boxed{s=36\cdot10^{M-1},}
\qquad
Y_s=11-9s,
\tag{2.1}

以及 external prefix root

\[
y=Y_s/s.
\tag{2.2}

三个 fully coupled equations为

\[
\boxed{
\mathcal N_{sp}(s,x)
=(x+2)^2(2025s^2x^2+Y_s^2)+10780x^2,}
\tag{2.3}

\[
\boxed{
\begin{aligned}
\mathcal O_{sp}(s,x,r_s)={}&
r_s[4(225sx^2+9s-11)^2\\
&\qquad-xY_s^2(99x-4)]
+2xY_s^2(x+2),
\end{aligned}}
\tag{2.4}

\[
\boxed{
\mathcal G_{sp}(x,r_s)
=55r_s^2(x+2)^2-49x^2.}
\tag{2.5}

当前 fixed-prime audit只保留满足

\[
\mathcal N_{sp}=\mathcal O_{sp}=\mathcal G_{sp}=0
\]
且 `s` 位于真实 decimal orbit `36<10>` 的 unit states。

---

## 3. `p=139`: exactly one genuine state

模 `139`：

\[
\operatorname{ord}_{139}(10)=46.
\]

遍历完整 decimal orbit

\[
s=36\cdot10^{M-1}
\]
并对每个 orbit point解 (2.3)--(2.5)，只得到

\[
\boxed{
(s,x,y,r_s)=(94,124,34,41)
\pmod{139}.}
\tag{3.1}

对应 exponent phase为

\[
\boxed{M\equiv44\pmod{46}.}
\tag{3.2}

它满足全部 genuine separation：

\[
x(x+2)y\ne0,
\]

\[
\boxed{
\Phi_s=(99x-4)r_s-2x-4
\equiv137\ne0\pmod{139},}
\tag{3.3}

\[
\boxed{
r_s(x+2)+2x\equiv132\ne0\pmod{139}.}
\tag{3.4}

所以既不是 source Hensel line，也不是 f-denominator boundary。

---

## 4. `p=463`: exactly two genuine states

模 `463`：

\[
\operatorname{ord}_{463}(10)=154.
\]

完整 decimal-orbit枚举只留下两组：

\[
\boxed{
(s,x,y,r_s)=(141,299,349,458),}
\tag{4.1}

\[
\boxed{
(s,x,y,r_s)=(172,328,376,416)
\pmod{463}.}
\tag{4.2}

对应

\[
\boxed{M\equiv140\pmod{154},}
\tag{4.3}

\[
\boxed{M\equiv147\pmod{154}.}
\tag{4.4}

两组均 genuine：

第一组

\[
\boxed{
\Phi_s\equiv36,
\qquad
r_s(x+2)+2x\equiv19
\pmod{463},}
\tag{4.5}

第二组

\[
\boxed{
\Phi_s\equiv318,
\qquad
r_s(x+2)+2x\equiv425
\pmod{463}.}
\tag{4.6}

全部为 units。

---

## 5. all three states are simple in the full system

对

\[
(\mathcal N_{sp},\mathcal O_{sp},\mathcal G_{sp})
\]
关于 `(s,x,r_s)` 的 Jacobian determinant，三点分别为

\[
\boxed{111\pmod{139},}
\tag{5.1}

\[
\boxed{397,\qquad159\pmod{463}.}
\tag{5.2}

全部非零。因此 multivariate Hensel lemma给：

\[
\boxed{
\text{每个 finite-field state至多有一条 compatible }p\text{-adic lift}.}
\tag{5.3}

不存在 external-center descendant singular tree。

---

## 6. decimal exponent direction is also simple

直接计算：

\[
\boxed{
10^{46}
\equiv1+43\cdot139
\pmod{139^2},}
\tag{6.1}

\[
\boxed{
10^{154}
\equiv1+217\cdot463
\pmod{463^2}.}
\tag{6.2}

`43,217` 都是相应 prime的 units，所以

\[
v_{139}(10^{46}-1)=1,
\qquad
v_{463}(10^{154}-1)=1.
\]

因此每个 simple state与 decimal exponent orbit联立后仍只有唯一 exponent lift：

\[
\boxed{
139:\ 1\text{ 条 unique decimal-Hensel orbit},}
\tag{6.3}

\[
\boxed{
463:\ 2\text{ 条 unique decimal-Hensel orbits}.}
\tag{6.4}

继续机械提升 `p^k` 只会刚性化这些 branches，不会自动制造局部空性。

---

## 7. these are exactly the known triple-overlap labels

`spontaneous-crt-height-descent-overlap.md` 已独立证明：若 descendant common prime同时属于 sphere-height 与 source-common support，则

\[
\boxed{p\in\{139,463\}.}
\tag{7.1}

external discriminant-zero center本身含 source-common center

\[
18K-55=0,
\]
并处于 `alpha=0` 的 content/height decomposition。

因此本文 surviving `139/463` states并不是新的第四类 descendant-common prime-source；它们正是既有 fixed triple-overlap labels的 actual fully-coupled local realizations。

所以 global common-parity ledger中不应把

\[
\text{external center }139/463
\]
与

\[
\text{height/source-common overlap }139/463
\]
重复计数。

---

## 8. current role

external discriminant-zero center + descendant common已从 moving prime问题压成：

\[
\boxed{
1\text{ 条 }139\text{-adic simple orbit}
+2\text{ 条 }463\text{-adic simple orbits}.}
\]

它们没有被 local finite-field compatibility排除，但也没有任何 local branching自由。

下一步若继续该 fixed center，应把三条 unique lifts接到 finite-defect centered representative或 descent height bound；继续只做 Hensel lift属于机械刚性化。

A2 仍为 `待证`。

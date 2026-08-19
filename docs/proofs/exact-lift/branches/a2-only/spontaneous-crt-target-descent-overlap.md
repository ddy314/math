# A2 equal-depth target 与 height-descent overlap 只剩 fixed `31/179`

> **依赖：** `spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descended-quotient-orientation.md`、`spontaneous-crt-descent-overlap-nogo.md`、`spontaneous-crt-f1270-source-audit.md`、`spontaneous-crt-l9-singular-audit.md`、equal-depth target chain。
>
> **严格状态：**本文直接把 equal-depth target relations代入 descended primitive quotient `Dhat_63`，得到一个只含 `K` 的 quadratic `G_D=11K^2-240K+432`。它与 target quadratic `P=6K^2-36K+55` 的 resultant仅为 `31*179*269`；target inert class排除 `269`，所以任何 target/descent reuse只剩 fixed `31,179`。fully primitive remainder `Rstar_63` 给同一 fixed set。更强地，`31,179` 在 resultant中只出现一层，所以 target baseline `h>=2` 时 `Dhat_63` 在该 prime上精确只有一层。结合此前两个 singular-gate audit，`31/179` 与所有 target singular candidates完全错开，因此 target/descent reuse只发生在 generic simple branch。本文尚未排除 `h=1` 的 fixed `31/179` first-layer cancellation，因此不关闭 A2。

---

## 1. exact target decomposition of the descended quotient

fully primitive descent中

\[
\widehat{\mathscr D}_{63}
=c_u^2\mathscr F_{63},
\]

\[
\mathscr F_{63}
=(2K-9)B_\Delta-\frac{63}{16}gTK^2,
\]

\[
B_\Delta=g((2K-9)T-a_3)-H_0.
\]

使用 exact concatenation

\[
\alpha=TK+a_3
\]
把 `a_3=alpha-TK` 代入：

\[
B_\Delta
=3gT(K-3)-g\alpha-H_0.
\tag{1.1}
\]

所以

\[
\begin{aligned}
16\mathscr F_{63}
={}&48gT(2K-9)(K-3)
-63gTK^2\\
&-16(2K-9)(g\alpha+H_0).
\end{aligned}
\]

前两项的 quadratic恰好因成

\[
48(2K-9)(K-3)-63K^2
=3(11K^2-240K+432).
\]

定义

\[
\boxed{G_D(K):=11K^2-240K+432.}
\tag{1.2}
\]

得到 exact identity

\[
\boxed{
16\mathscr F_{63}
=3gT G_D(K)
-16(2K-9)(g\alpha+H_0).}
\tag{1.3}

---

## 2. equal-depth target first layer

真正 equal-depth target满足

\[
v_p(\omega)=v_p(W_q)=h\ge1,
\]

\[
\alpha=\omega W_q,
\qquad
H_0=c_uW_q.
\]

所以

\[
\boxed{v_p(\alpha)=2h,\qquad v_p(H_0)=h.}
\tag{2.1}
\]

`p` 与 `gc_uT` 分离，因此两 summands深度不同：

\[
\boxed{v_p(g\alpha+H_0)=h.}
\tag{2.2}
\]

若 target prime还满足

\[
p\mid\widehat{\mathscr D}_{63},
\]
则由 (1.3)，模 `p` 的 error消失，得到

\[
\boxed{p\mid G_D(K).}
\tag{2.3}
\]

---

## 3. target resultant leaves only `31,179,269`

目标 prefix quadratic为

\[
\boxed{P(K)=6K^2-36K+55.}
\tag{3.1}
\]

直接 resultant：

\[
\boxed{
\operatorname{Res}_K(P,G_D)
=1492681
=31\cdot179\cdot269.}
\tag{3.2}
\]

所有 genuine target inert primes满足

\[
p\equiv7\text{ or }11\pmod{24}.
\]

而

\[
31\equiv7,
\qquad179\equiv11,
\qquad269\equiv5
\pmod{24}.
\]

所以

\[
\boxed{
\operatorname{Supp}_{\rm target}^{\rm gen}
\cap
\operatorname{Supp}(\widehat{\mathscr D}_{63})
\subseteq\{31,179\}.}
\tag{3.3}
\]

两 fixed roots唯一为

\[
\boxed{
K\equiv9\pmod{31},
\qquad
K\equiv71\pmod{179}.}
\tag{3.4}
\]

---

## 4. the fully primitive remainder gives the same fixed set

fully primitive remainder满足 exact formula

\[
\begin{aligned}
16\mathscr R_{63}^\star
={}&2^{2m}5^dc_u^2g^2
(15K^2+384K-848)\\
&-16\cdot2^mgc_u^2C(2K-9)\\
&-16\cdot5^dQ_0^2N_0.
\end{aligned}
\tag{4.1}
\]

在 target上：

\[
\alpha\equiv0
\Longrightarrow
a_3\equiv-TK,
\tag{4.2}
\]

\[
qW_q=DK-(3D-C)\equiv0
\Longrightarrow
C\equiv D(3-K),
\tag{4.3}
\]

而 original carrier `That_2=0` 与 (4.2)、`P=0` 给

\[
\boxed{
Q_0^2N_0
\equiv-2^{2m}c_u^2g^2K^2
\pmod p.}
\tag{4.4}
\]

代入 (4.1)：

\[
\boxed{
16\mathscr R_{63}^\star
\equiv
2^{2m}5^dc_u^2g^2
G_R(K)
\pmod p,}
\tag{4.5}
\]

其中

\[
\boxed{G_R(K):=63K^2+144K-416.}
\tag{4.6}
\]

resultant：

\[
\boxed{
\operatorname{Res}_K(P,G_R)
=13434129
=3^2\cdot31\cdot179\cdot269.}
\tag{4.7}
\]

因此 target与 `Rstar_63` 的 genuine inert overlap同样只可能是

\[
\boxed{31,179.}
\tag{4.8}
\]

对应 common K roots仍是 (3.4)。

事实上

\[
\boxed{G_R=16P-3G_D,}
\tag{4.9}
\]

所以两个 fixed-set resultants是同一 descent relation的不同投影。

---

## 5. transverse depth: high-baseline target can enter `Dhat_63` only once

(3.2) 中 `31,179,269` 全部只出现 exponent `1`。resultant Bezout identity因此给：在任一 fixed common root，

\[
\boxed{
\min\{v_p(P),v_p(G_D)\}=1.}
\tag{5.1}
\]

目标 baseline已有 exact

\[
\boxed{v_p(P)=h.}
\tag{5.2}
\]

所以若

\[
h\ge2,
\]
则

\[
\boxed{v_p(G_D)=1.}
\tag{5.3}
\]

另一方面由 (2.2)，(1.3) 的 error term

\[
16(2K-9)(g\alpha+H_0)
\]
在 `31/179` 上具有 exact depth `h`；两个 fixed states中

\[
2K-9\not\equiv0\pmod p.
\]

当 `h>=2`，main term `3gTG_D` 的 depth为 `1`，唯一最浅。因此

\[
\boxed{
 v_p(\mathscr F_{63})=1,
 \qquad
 v_p(\widehat{\mathscr D}_{63})=1
 \quad(p=31,179;\ h\ge2).}
\tag{5.4}

所以 deep target baseline不能在 descended quotient里继续携带同样的无界深度。

---

## 6. singular locus is completely disjoint from the target reuse candidates

此前两个 singular audit给：

\[
\boxed{
L_9\text{ target branch}:\ \varnothing,}
\tag{6.1}
\]

\[
\boxed{
F_{1270}\text{ target branch}:\ \{7,79,107,199\}.}
\tag{6.2}
\]

本文的 actual descent target reuse candidates为

\[
\boxed{\{31,179\}.}
\tag{6.3}
\]

三集合互不相交。因此

\[
\boxed{
\text{任何 genuine target/descent reuse 都位于 generic simple }K\text{-resultant branch}.}
\tag{6.4}
\]

不存在 target supplier藏进 descent singular Hensel tree的可能。

---

## 7. current frontier

original/short-remainder parity若试图复用 equal-depth target prime，现在只剩两个 fixed first-layer candidates：

\[
31,\quad179.
\]

若 target baseline `h>=2`，它们在 `Dhat_63` 中又只能精确出现一层。

唯一尚未精确关闭的是 `h=1` 时 fixed `31/179` 的 next-digit cancellation：此时 (1.3) 的 main/error 两项都只有一层，可能继续抵消。若需要彻底禁止 target reuse，下一步可只审这两个 fixed prime的 mod-`p^2` normalized equation，不再需要任何 moving-prime分析。

A2 仍为 `待证`。

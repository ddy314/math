# A2 descendant common support 的 universal `(K,zeta)` cubic

> **依赖：** `endpoint-lattice.md` 的 exact rational-root quartic、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-pure-branch-defect.md`、`spontaneous-prefix-eliminant.md`。
>
> **严格状态：**descendant common condition先唯一恢复 finite-defect root `r=J_def`；original additive carrier再唯一恢复 prefix ratio `Q^2N_0/B^2`。本文把二者代回 exact rational-root quartic，消去 `C,D,B,Q,N_0`，得到一个只依赖真实 prefix integer `K` 与 third phase `zeta=a_3/T` 的 universal cubic `E_63(K,zeta)`。其 zeta-discriminant完全因子化：除一个新的 degree-8 kernel `H_8(K)` 外，其余 singular factors都是已知 central/descendant gates且以平方出现。对 generic pure-spontaneous branch，这给 `Q_i=0` 之外真正的第二个独立 compatibility equation。本文尚未完成 branchwise resultant，因此不关闭 A2。

---

## 1. normalized rational-root equation

exact rational-root polynomial为

\[
F(J)=
B^2T\,J(TJ+2a_3)(K-J)^2
-Q^2N_0(TJ+a_3)^2.
\]

令

\[
\boxed{\zeta:=a_3/T,}
\qquad
\boxed{R:=Q^2N_0/B^2.}
\]

除去 genuine units `B^2T^2`，root `r=J_def` 满足

\[
\boxed{
\Phi(r)
:=r(r+2\zeta)(K-r)^2
-R(r+\zeta)^2=0.}
\tag{1.1}

这里

\[
r=3-C/D.
\]

---

## 2. additive carrier eliminates `R`

height/additive identity为

\[
\widehat{\mathcal T}_2=0
\Longleftrightarrow
T\mathcal J_H
-2B^2(2K-9)\alpha=0
\pmod p,
\]

其中

\[
\mathcal J_H
=B^2(5K^2-36K+55)-Q^2N_0,
\]

\[
\alpha=T(K+\zeta).
\]

对 descendant common prime，`p|Rstar,Dhat` 由 positive descent自动给

\[
p\mid\widehat{\mathcal T}_2.
\]

除去 `B^2T`：

\[
5K^2-36K+55-R
-2(2K-9)(K+\zeta)=0.
\]

所以

\[
\boxed{
R
=K^2-(18+4\zeta)K+18\zeta+55.}
\tag{2.1}

这一步已经把 prefix norm ratio从 rational-root equation中完全移除。

---

## 3. descendant equation eliminates `r`

`spontaneous-crt-pure-branch-defect.md` 的 universal descendant equation为

\[
(2K-9)(2K-9-2\zeta-r)
=\frac{63}{16}K^2.
\tag{3.1}

在 noncentral sector

\[
2K-9\not\equiv0\pmod p
\]
可唯一解出

\[
\boxed{
 r
=
\frac{
K^2-64K\zeta-576K+288\zeta+1296
}
{16(2K-9)}.}
\tag{3.2}

所以 descendant common prime同时把 rational-root中的两个 auxiliary quantities `R,r` 都降成 `(K,zeta)` 的有理函数。

---

## 4. substitute into `Phi`: universal cubic

将 (2.1),(3.2) 代入 (1.1)。清去 denominator

\[
65536(2K-9)^4
\]
后定义 primitive numerator

\[
\boxed{\mathcal E_{63}(K,\zeta).}
\tag{4.1}

为方便审计，记

\[
U:=2K-9,
\qquad
L:=K^2-576K+1296,
\]

并定义四个小 coefficient polynomials

\[
A:=5K^2+144K-324,
\]

\[
B_2:=381K^4-78048K^3-277520K^2+2392704K-3074112,
\]

\[
B_1:=189K^4-126720K^3+132784K^2+1359360K-2218752,
\]

\[
B_0:=63K^4-54432K^3+136672K^2+239616K-539136.
\]

则完整 cubic具有高度因子化的系数：

\[
\boxed{
\begin{aligned}
\mathcal E_{63}(K,\zeta)
={}&98304U^3A\,\zeta^3\\
&-1024U^2B_2\,\zeta^2\\
&+32ULB_1\,\zeta\\
&-L^2B_0.
\end{aligned}}
\tag{4.2}

因此每个 genuine noncentral descendant common prime都满足

\[
\boxed{\mathcal E_{63}(K,\zeta)\equiv0\pmod p.}
\tag{4.3}

这是完全独立于 `C,D,B,Q,N_0` 的 universal third/prefix carrier。

---

## 5. cubic discriminant factorization

直接对 `zeta` 求 discriminant。定义

\[
\boxed{
\begin{aligned}
H_8(K):={}&
28539K^8-33511968K^7+7112503200K^6\\
&+135023040000K^5-985065366784K^4\\
&+1911068393472K^3-377731358720K^2\\
&-2065729978368K+1344988053504.
\end{aligned}}
\tag{5.1}

则

\[
\boxed{
\begin{aligned}
\operatorname{Disc}_{\zeta}(\mathcal E_{63})
={}&-2^{34}3^2
(2K-9)^{10}\\
&\cdot(K^2-576K+1296)^2\\
&\cdot(11K^2-240K+432)^2\\
&\cdot H_8(K).
\end{aligned}}
\tag{5.2}

所以 ordinary repeated-root locus分成：

1. central gate `2K-9`；
2. quadratic gate `L=K^2-576K+1296`；
3. known descendant-height quadratic `G_D=11K^2-240K+432`；
4. genuinely new singular kernel `H_8`。

前三项全部以偶 exponent进入 discriminant，不能再次当 independent Legendre obstruction收费。

---

## 6. the new `L` gate itself has fixed-7 discriminant

\[
L=K^2-576K+1296
\]
的 discriminant为

\[
\boxed{
576^2-4\cdot1296
=326592
=216^2\cdot7.}
\tag{6.1}

所以 generic inert prime `p!=7` 若进入 `L=0`，必须满足

\[
\boxed{\left(\frac7p\right)=1.}
\tag{6.2}

因为 `7,p=3 mod4`，互反律等价于

\[
\boxed{\left(\frac p7\right)=-1.}
\tag{6.3}

这只是 singular-gate orientation，不自动排除 moving prime；ramified `7` 需另行审计。

---

## 7. consistency on `alpha=0`

作为结构审计，把

\[
\alpha=0
\Longrightarrow
\zeta=-K
\]
代入 universal cubic。精确因子化为

\[
\boxed{
\mathcal E_{63}(K,-K)
=-9G_D(K)^2\,Q_4(K),}
\tag{7.1}

其中

\[
\boxed{
Q_4(K)
=5055K^4-44640K^3-91424K^2+612864K-539136.}
\tag{7.2}

所以此前 target/height analysis中反复出现的 `G_D(K)=0` 正是 universal cubic 在 alpha-supported sector中的 double factor；这验证本文的降维与既有 target/height结果一致。

剩余 quartic `Q_4` 对应其它 alpha-supported content possibility，不应与 `G_D^2` 重复计数。

---

## 8. pure-spontaneous branch now has two independent equations

在 genuine alpha-free、noncentral pure-spontaneous sector，已有唯一 branch

\[
\mathcal Q_i(\tau;x,y)=0,
\qquad i\in\{1,2\},
\]
以及

\[
K=\frac{9+y}{\tau},
\qquad
\zeta=\frac{z_i(x,y)}{\tau}.
\]

本文再给第二条 independent compatibility：

\[
\boxed{
\mathcal E_{63}\!\left(
\frac{9+y}{\tau},
\frac{z_i(x,y)}{\tau}
\right)=0.}
\tag{8.1}

所以 remaining external kernel已从“一个可自由 simple-Hensel 的 quadratic branch”升级成两方程交集：

\[
\boxed{
\mathcal Q_i=0
\quad\cap\quad
\mathcal E_{63}=0.}
\tag{8.2}

而 `C/D` 又由前一文件唯一恢复。即 third numerator、finite defect、prefix norm ratio都不再是自由变量。

下一步最直接的是对每个 `i` 在 sphere-root quotient ring中求 (8.2) 的 branchwise resultant，审计是否塌成 fixed primes/短 decimal carrier。若 resultant再次只回到 `A_-`, `C_*` 等旧 collision，应明确降级；若出现新 pure-prefix factor，则它就是当前最有希望的 global external obstruction。

A2 仍为 `待证`。

# A2 descendant same-prime recycling 的 canonical parent-balance tail

> **依赖：** `spontaneous-crt-descendant-unequal-parent-depth.md`、`spontaneous-crt-descendant-linear-depth-reader.md`、`spontaneous-crt-descendant-transport-resonance.md`。
>
> **严格状态：**前一文件按 `a=v_p(Rstar_63)`、`b=v_p(Dhat_63)` 分出两条 unequal-depth coefficient gates；equal depth仍保留一个 normalized parent unit。本文把三种情况重新齐次化。令 parent 两个正 summands为 `X=5^lambda Rstar_63`、`Y=g2^m Dhat_63`，则 projective/additive error与 descendant error满足 exact linear identities `L=s_L(X+Y)`、`F=K^2s_LY`。代入 transported error再减 Euclidean quotient后，一阶 remainder恰为共同 unit乘 `81X G_<+2Y G_>`。因此除去 canonical common baseline `G_Delta` 后得到 positive integer tail `B_63`，其 p-support精确等价于 same-prime linear-remainder overdepth。equal depth时 resonance unit被唯一固定为 `chi=-2G_>/(81G_<)`；真实 endpoint上该几何 ratio严格小于 `-1`。若 parent自身先发生 `chi=-1` cancellation，再要求 child recycling，其 collision resultant恰回到 central / old singular / `H_2,H_10` tangent gates。于是 generic parent-cancelled equal-depth branch不能继续 recycling。本文仍未排除 `chi=chi_geom` 的 p-adic wrapping，因此不关闭 A2。

---

## 1. homogeneous parent coordinates

fully primitive parent descent写成

\[
\boxed{
\widehat{\mathcal T}_2=X+Y,}
\tag{1.1}

其中定义两个 positive integers

\[
\boxed{X:=5^\lambda\mathscr R_{63}^\star,}
\tag{1.2}

\[
\boxed{Y:=g2^m\widehat{\mathscr D}_{63}.}
\tag{1.3}

记

\[
G_\Delta=\gcd(\mathscr R_{63}^\star,
                  \widehat{\mathscr D}_{63}).
\]

因为 `Rstar_63` 与 `10g` 互素，`G_Delta` 与 parent scale `5g2` 互素。因此

\[
\boxed{G_\Delta\mid X,\qquad G_\Delta\mid Y.}
\tag{1.4}

---

## 2. exact errors in terms of `X,Y`

前一 depth theorem给

\[
L
=\frac{2^{2M+2}}{5^mB^2K^2}\widehat T_2.
\]

定义 p-unit/rational scale

\[
\boxed{s_L:=\frac{2^{2M+2}}{5^mB^2K^2}.}
\tag{2.1}

由 (1.1)：

\[
\boxed{L=s_L(X+Y).}
\tag{2.2}

另一方面

\[
F=\frac{\widehat D_{63}}{c_u^2gT}.
\]

直接使用

\[
B^2=2^{2M+2m+2}c_u^2g^2,
\qquad
T=2^m5^m
\]
可验证

\[
\boxed{F=K^2s_LY.}
\tag{2.3}

这两个 identities是 exact，不是只在某个 valuation case成立。

---

## 3. first-order remainder is one homogeneous parent form

transported error的一阶部分为

\[
C_{tr}
\left[
\frac{\Phi_J}{U}F
-K^2(J+\zeta)^2L
\right],
\]
其中

\[
C_{tr}=\frac{65536U^4}{K^8},
\qquad U=2K-9.
\]

Euclidean remainder为

\[
M=E-Q L.
\]

把 (2.2),(2.3) 代入，得到一阶式

\[
M^{(1)}
=s_L\left[
X(C_<-Q_0)+Y(C_>-Q_0)
\right],
\tag{3.1}

其中 `C_<,C_>,Q_0` 正是 unequal-depth文件的 coefficient functions。

该文件定义 primitive integer gates

\[
\mathcal G_<,\qquad\mathcal G_>,
\]
并且 checker给 exact raw normalizations

\[
\boxed{
C_<-Q_0
=\frac{5184}{5^711^7K^6}\mathcal G_<,}
\tag{3.2}

\[
\boxed{
C_>-Q_0
=\frac{128}{5^711^7K^6}\mathcal G_>.}
\tag{3.3}

因为

\[
5184=64\cdot81,
\qquad
128=64\cdot2,
\]
有

\[
\boxed{
M^{(1)}
=\frac{64s_L}{5^711^7K^6}
\left(81X\mathcal G_<+2Y\mathcal G_>\right).}
\tag{3.4}

所有被除 scale在 genuine non-`3`, non-`5,11`, noncentral external prime上均为 units。

---

## 4. clear the third-block denominator

`G_<,G_>` 为 total-degree-6 polynomials in `(K,zeta)`，而

\[
\zeta=a_3/T.
\]

定义 ordinary integer gates

\[
\boxed{
\mathfrak G_<
:=T^6\mathcal G_<(K,a_3/T),}
\tag{4.1}

\[
\boxed{
\mathfrak G_>
:=T^6\mathcal G_>(K,a_3/T).}
\tag{4.2}

`T` 是 genuine p-unit，所以 valuation/support不变。

前一文件 projective Bernstein audit等价于真实 endpoint上

\[
\boxed{
\mathfrak G_<<0,
\qquad
\mathfrak G_><0.}
\tag{4.3}

---

## 5. canonical positive balance tail

定义 homogeneous resonance numerator

\[
\boxed{
\mathscr H_{bal}
:=81X\mathfrak G_<+2Y\mathfrak G_>.}
\tag{5.1}

由 (1.4)：

\[
G_\Delta\mid\mathscr H_{bal}.
\]

又由 `X,Y>0` 与 (4.3)：

\[
\boxed{\mathscr H_{bal}<0.}
\tag{5.2}

因此定义 canonical positive integer

\[
\boxed{
\mathscr B_{63}
:=-\frac{\mathscr H_{bal}}{G_\Delta}
\in\mathbf Z_{>0}.}
\tag{5.3}

这就是 parent-balance tail。

---

## 6. exact support equivalence with same-prime recycling

固定 genuine common prime `p`，写

\[
k=v_p(G_\Delta),
\]

\[
X=p^kX_0,
\qquad
Y=p^kY_0,
\]
其中至少一个 `X_0,Y_0` 为 unit。

所有 transported higher-order terms对 parent errors的总次数至少2，所以至少含 `p^(2k)`。由 (3.4)，再用 `k>=1`：

\[
\boxed{
\frac{M}{p^k}
\equiv
u_p\left(
81X_0\mathfrak G_<
+2Y_0\mathfrak G_>
\right)
\pmod p,}
\tag{6.1}

其中 `nu_p` 为显式 p-unit。

而 (5.3) 除去的 `G_Delta` 在 p 上恰为 `p^k`。因此

\[
\boxed{
p\mid\mathscr B_{63}
\Longleftrightarrow
v_p(M)>k.}
\tag{6.2}

这在当前 genuine regular sector是 exact support selector：same-prime linear-tail recycling不再需要预先按 `a<b,a=b,b<a` 分类。

---

## 7. previous depth cases are the projective limits

若

\[
a=v_p(Rstar)<b=v_p(Dhat),
\]
则模 p

\[
X_0\ne0,\qquad Y_0=0.
\]
(6.1) 恢复

\[
\boxed{\mathfrak G_<\equiv0.}
\tag{7.1}

若

\[
b<a,
\]
则

\[
X_0=0,\qquad Y_0\ne0,
\]
恢复

\[
\boxed{\mathfrak G_>\equiv0.}
\tag{7.2}

所以两个 degree-48 unequal-depth gates只是 homogeneous parent line在 `0` 与 `infinity` 两个 projective endpoints。

---

## 8. equal depth: a canonical parent-balance unit

现在令

\[
a=b=h.
\]
则 `X_0,Y_0` 都是 units。定义

\[
\boxed{
\chi_p:=X_0/Y_0
=\frac{5^\lambda Rstar/p^h}
       {g2^mDhat/p^h}.}
\tag{8.1}

parent sum满足

\[
\frac{\widehat T_2}{p^h}
=Y_0(1+\chi_p).
\]
所以

\[
\boxed{
v_p(\widehat T_2)>h
\Longleftrightarrow
\chi_p\equiv-1\pmod p.}
\tag{8.2}

如果 parent没有额外 cancellation，即 `chi_p!=-1`，same-prime recycling由 (6.1) 唯一锁定：

\[
\boxed{
\chi_p
=-\frac{2\mathfrak G_>}
        {81\mathfrak G_<}
\pmod p.}
\tag{8.3}

因此 equal-depth中最后的 residual unit自由已压成一个 canonical parent-balance unit。

---

## 9. the geometric balance lies strictly below `-1` on the real endpoint

projective gates都为负。进一步定义

\[
\mathfrak H_{-1}
:=81\mathfrak G_<-2\mathfrak G_>.
\]

在 projective `(r,u)` box `[0,10^-3]^2` 上，exact Bernstein audit给全部49个 coefficients严格为正；最小值为

\[
\boxed{
\frac{24267959613723206789529}{6250000000}>0.}
\tag{9.1}

所以真实 endpoint上

\[
\boxed{81\mathfrak G_<-2\mathfrak G_> >0.}
\tag{9.2}

由于 denominator `81G_<` 为负，(8.3) 的 real geometric value满足

\[
\boxed{
\chi_{geom}
:=-\frac{2\mathfrak G_>}{81\mathfrak G_<}
<-1.}
\tag{9.3}

而真实 parent ratio

\[
X/Y>0.
\]
所以 equal-depth recycling也没有 real balance point；只能依赖 p-adic wrapping。

---

## 10. parent cancellation plus child recycling is exactly the tangent collision

若 parent先有额外 cancellation，则

\[
\chi_p=-1.
\]

若同时要求 child recycling，(8.3) 强迫

\[
\boxed{
81\mathfrak G_<-2\mathfrak G_>\equiv0\pmod p.}
\tag{10.1}

乘/除 `T^6` 不改变 genuine p-support。对 primitive `(K,zeta)` polynomial

\[
81\mathcal G_<-2\mathcal G_>
\]
与 universal cubic消去 `zeta`，exact resultant为

\[
\boxed{
\begin{aligned}
&2^{43}3^2(2K-9)^{13}
(K^2-576K+1296)^2\\
&\qquad\cdot G_D(K)^2H_2(K)H_{10}(K),
\end{aligned}}
\tag{10.2}

差一个无关整体正负号。

这与 `spontaneous-crt-descendant-transport-resonance.md` 的 rational-root tangent resultant完全相同。

因此在排除 central / old zero-root / alpha-height / `H_2,H_10` tangent gates后：

\[
\boxed{
\chi_p=-1
\Longrightarrow
p\nmid\mathscr B_{63}.}
\tag{10.3}

也就是说 generic parent-cancelled equal-depth branch**不能继续 same-prime recycling**。

---

## 11. revised final generic bottleneck

same-prime recycling的 parent-depth自由现在已完全 canonical 化：

- unequal depths：fixed projective endpoint gates `G_<,G_>`；
- equal depth + parent cancellation `chi=-1`：只在已知 tangent factor set中重合；
- genuine remaining generic branch：
  \[
  \boxed{
  a=b=h,
  \quad\chi_p\ne-1,
  \quad\chi_p=\chi_{geom}< -1\text{ (real)}
  }
  \]
  通过 p-adic wrapping实现。

而所有 same-prime recycling support统一由 positive canonical integer `B_63` 读取。

下一步最窄目标已经变成：为 `B_63` 建立 height / primitive parity，或把 `chi_p=chi_geom` 与 parent positive ratio的 natural representative做 prime-power budget。

A2 仍为 `待证`。

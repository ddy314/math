# A2 descendant-only external common depth 的 projective reader 与 resonance tail

> **依赖：** `spontaneous-crt-descendant-projective-integer.md`、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descended-quotient-orientation.md`、`endpoint-lattice.md` 的 exact rational-root equation。
>
> **严格状态：**上一文件构造 positive canonical integer `P_63`，但只记录 support。本文证明 descendant common gcd 的完整 baseline exponent逐 prime都进入 `P_63`。核心是把 universal cubic恢复成 exact rational-root polynomial `Phi(J,R)` 在 additive approximation `R_0` 与 descendant approximation `J_0` 上的值：`Phi(J_0,R_0)=E_63/[65536(2K-9)^4]`，而 `R_0-R` 正比于 projective branch error `L_proj`，`J_0-J` 正比于 descendant error `F_Delta`。因此 common depth `k` 同时进入 `L_proj,E_proj`，继而进入 projective resultant与 `P_63`。本文还给 resultant 的 exact local identity，证明在 coefficient/repeated-root singular gates之外，额外 projective depth只能来自一次 equal-depth normalized cancellation。于是若 pure external common product本身承担 odd parity，`P_63^circ≡1 mod8` 会强迫一份额外 inert tail；同一 prime若想重复支付，必须进入该 resonance tail。本文仍未排除 resonance tail，因此不关闭 A2。

---

## 1. common baseline depth

固定 genuine alpha-free、noncentral descendant-only external prime `p`。写

\[
a_p:=v_p(\mathscr R_{63}^\star),
\qquad
b_p:=v_p(\widehat{\mathscr D}_{63}),
\]

\[
\boxed{k_p:=\min(a_p,b_p)\ge1.}
\tag{1.1}

fully primitive descent为

\[
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.
\]

在 genuine external sector `p∤10g`，所以

\[
\boxed{v_p(\widehat{\mathcal T}_2)\ge k_p.}
\tag{1.2}

若 `a_p!=b_p`，两项深度不同，甚至有

\[
\boxed{v_p(\widehat{\mathcal T}_2)=k_p.}
\tag{1.3}

只有 equal descendant depth `a_p=b_p` 时，parent descent本身才可能继续 cancellation。

---

## 2. exact rational-root error coordinates

令真实 finite-defect root为

\[
J:=3-C/D,
\]
并记

\[
\zeta:=a_3/T,
\qquad
R:=Q^2N_0/B^2.
\]

exact rational-root equation为

\[
\boxed{
\Phi(J,R)
:=J(J+2\zeta)(K-J)^2
-R(J+\zeta)^2
=0.}
\tag{2.1}

additive carrier对应的 zero approximation为

\[
\boxed{
R_0
:=K^2-(18+4\zeta)K+18\zeta+55.}
\tag{2.2}

projective variables

\[
r=1/K,
\qquad
u=\zeta/K,
\qquad
v=R/K^2
\]
下

\[
\mathscr L_{\rm proj}
=55r^2+18(u-1)r+1-4u-v.
\]

直接乘回 `K^2`：

\[
\boxed{
R_0-R=K^2\mathscr L_{\rm proj}.}
\tag{2.3}

另一方面定义 descendant residual

\[
\boxed{
F_\Delta
:=(2K-9)(2K-9-J-2\zeta)
-\frac{63}{16}K^2.}
\tag{2.4}

由

\[
\widehat{\mathscr D}_{63}
=c_u^2gT\,F_\Delta
\]
在 genuine sector `p∤c_ugT` 得

\[
\boxed{v_p(F_\Delta)=b_p\ge k_p.}
\tag{2.5}

令

\[
\boxed{
J_0
:=\frac{K^2-64K\zeta-576K+288\zeta+1296}
{16(2K-9)}.}
\tag{2.6}

从 (2.4) 直接解出

\[
\boxed{
J_0-J=\frac{F_\Delta}{2K-9}.}
\tag{2.7}

所以 additive 与 descendant 两个 approximation errors都至少有 `k_p` 层。

---

## 3. universal cubic is exactly the transported rational-root error

`spontaneous-crt-universal-descendant-cubic.md` 定义 `E_63(K,zeta)`。直接代入 (2.2),(2.6) 并清分母，得到 exact identity

\[
\boxed{
\Phi(J_0,R_0)
=
\frac{\mathcal E_{63}(K,\zeta)}
{65536(2K-9)^4}.}
\tag{3.1}

因为真实 `Phi(J,R)=0`，而

\[
J_0=J+F_\Delta/(2K-9),
\]

\[
R_0=R+K^2\mathscr L_{\rm proj},
\]
所以

\[
\Phi(J_0,R_0)-\Phi(J,R)
\]
是关于两个 error variables

\[
F_\Delta,
\qquad
\mathscr L_{\rm proj}
\]
的 polynomial，且没有 constant term。所有清分母只使用 `2K-9`，在 noncentral genuine sector为 unit。

因此只要

\[
v_p(F_\Delta)\ge k_p,
\qquad
v_p(\mathscr L_{\rm proj})\ge k_p,
\]
就有

\[
\boxed{v_p(\mathcal E_{63})\ge k_p.}
\tag{3.2}

而 (1.2) 与 `Theta_dec=B^2TK^2 L_proj`、primitive normalization只差 `2,5` units，给

\[
\boxed{v_p(\mathscr L_{\rm proj})\ge k_p.}
\tag{3.3}

故 (3.2) 无条件适用于当前 generic descendant common prime。

---

## 4. move the depth into the projective resultant

在 actual projective point

\[
r=1/K,
\qquad
u=\zeta/K,
\qquad
v=R/K^2,
\]
定义

\[
\mathscr E_{\rm proj}(r,u)
=r^8\mathcal E_{63}(1/r,u/r).
\]

`p∤K`，所以由 (3.2)

\[
\boxed{v_p(\mathscr E_{\rm proj})\ge k_p.}
\tag{4.1}

将 `E_proj` 对 quadratic `L_proj` 做 Euclidean division：

\[
\boxed{
\mathscr E_{\rm proj}
=Q_{63}\mathscr L_{\rm proj}
+M_{63},}
\tag{4.2}

\[
\boxed{M_{63}=A_{63}^{\rm proj}r+B_{63}^{\rm proj}.}
\tag{4.3}

division denominator只含 `55=5*11`；当前 genuine branch排除 `5,11`。由 (3.3),(4.1)：

\[
\boxed{v_p(M_{63})\ge k_p.}
\tag{4.4}

projective resultant `X_63^proj` 除 fixed content `5^7 11^7` 外，正是 `L_proj` 与 `M_63` 的 resultant。因此

\[
\boxed{v_p(\mathscr X_{63}^{\rm proj})\ge k_p.}
\tag{4.5}

最后 canonical integer clearing

\[
\mathscr P_{63}
=(TK)^8(B^2K^2)^8
\mathscr X_{63}^{\rm proj}(a_3/(TK),Q^2N_0/(B^2K^2))
\]
只乘 genuine p-units，故

\[
\boxed{v_p(\mathscr P_{63})\ge k_p.}
\tag{4.6}

---

## 5. global full-baseline divisibility

令 `E_pure` 为当前 genuine alpha-free noncentral descendant-only external primes，并定义 baseline common product

\[
\boxed{
G_\Delta^{\rm pure}
:=\prod_{p\in E_{pure}}p^{k_p}.}
\tag{5.1}

逐 prime由 (4.6)：

\[
\boxed{G_\Delta^{\rm pure}\mid\mathscr P_{63}.}
\tag{5.2}

由于 `G_pure` 为 odd，而上一文件证明

\[
v_2(\mathscr P_{63})=16M+8m+58,
\]
定义 positive odd primitive carrier

\[
\boxed{
\mathscr P_{63}^\circ
:=\frac{\mathscr P_{63}}{2^{16M+8m+58}}.}
\tag{5.3}

则仍有完整 baseline divisibility

\[
\boxed{G_\Delta^{\rm pure}\mid\mathscr P_{63}^\circ.}
\tag{5.4}

---

## 6. exact local resultant identity and the only generic overdepth mechanism

写 projective quadratic

\[
L(r)=55r^2+br+c,
\]
其中

\[
b=18(u-1),
\qquad
c=1-4u-v,
\]
以及 linear remainder

\[
M(r)=Ar+B.
\]

其 raw resultant为

\[
X=55B^2-bAB+cA^2.
\]

对任意 evaluation point `r` 有 exact identity

\[
\boxed{
X
=A^2L(r)-A L'(r)M(r)+55M(r)^2.}
\tag{6.1}

固定 prime满足 coefficient/repeated-root separation

\[
\boxed{p\nmid A L'(r).}
\tag{6.2}

记

\[
\ell:=v_p(L(r)),
\qquad
\mu:=v_p(M(r)).
\]

若

\[
\ell<\mu,
\]
则 (6.1) 唯一最低项是 `A^2L`：

\[
\boxed{v_p(X)=\ell.}
\tag{6.3}

若

\[
\mu<\ell,
\]
唯一最低项是 `-AL'M`：

\[
\boxed{v_p(X)=\mu.}
\tag{6.4}

所以

\[
\boxed{
\ell\ne\mu
\Longrightarrow
v_p(X)=\min(\ell,\mu).}
\tag{6.5}

额外 projective depth只能发生在

\[
\boxed{\ell=\mu=:h.}
\tag{6.6}

此时写

\[
L=p^hL_0,
\qquad
M=p^hM_0,
\]
其中 `L_0,M_0` 为 units。除以 `p^h` 后，`55M^2` 至少还含 `p^h`，所以 extra depth iff

\[
\boxed{
A L_0-L'(r)M_0\equiv0\pmod p.}
\tag{6.7}

因此 generic same-prime overdepth不是任意现象，而是一条明确的 equal-depth normalized resonance。

若 `p|A`，进入已单列的 coefficient-singular `H_4/H_24`；若 `p|L'`，进入 `spontaneous-single-branch.md` 的 repeated-root tangent。本文不把这两类算作 generic resonance。

---

## 7. parity consequence of the full baseline reader

上一文件证明

\[
\boxed{
\mathscr P_{63}^\circ>0,
\qquad
\mathscr P_{63}^\circ\equiv1\pmod8.}
\tag{7.1}

定义 projective tail

\[
\boxed{
\mathscr T_{63}^{\rm proj}
:=\frac{\mathscr P_{63}^\circ}{G_\Delta^{\rm pure}}.}
\tag{7.2}

若 pure external common product本身承担 odd inert parity，即

\[
G_\Delta^{\rm pure}\equiv3\pmod4,
\]
则由 (7.1)

\[
\boxed{
\mathscr T_{63}^{\rm proj}\equiv3\pmod4.}
\tag{7.3}

所以 common baseline若想吸收一份 descendant odd parity，canonical projective carrier中自动出现另一份 odd-inert valuation **超过 baseline common product**。

这份 tail可以由另一枚 inert prime承担；若仍想由同一个 common label重复承担，则必须有

\[
\boxed{v_p(\mathscr P_{63})>k_p,}
\tag{7.4}

并进入 §6 的 projective overdepth mechanism（或 coefficient/repeated-root singular gates）。

---

## 8. updated closure target

pure descendant external common escape现在不再只是一个任意 common gcd：

1. full baseline depth由 `P_63` 读取；
2. `P_63^circ` 为 positive `1 mod8`；
3. common product若为 `3 mod4`，其 quotient自动再产生 `3 mod4` tail；
4. same-prime tail recycling只剩：
   - generic equal-depth resonance (6.7)；
   - coefficient singular `H_4/H_24`；
   - repeated-root tangent。

因此下一步最窄的 generic closure target已经变成排除或收费 (6.7) 的 normalized equal-depth resonance，而不是继续扩张 prime-source 分类。

A2 仍为 `待证`。

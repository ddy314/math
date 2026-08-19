# A2 source common depth 的 fully-decimal square gate

> **依赖：** `spontaneous-source-parity-decimal-gcd.md`、`spontaneous-source-parity-common-gcd.md`。
>
> **严格状态：**本文把 source square collision也完全乘回 decimal plane：`55B_dec-K^2D_dec=b_3^2(18K-55)^2`。随后定义 `G_free=G_dec/gcd(G_dec,b_3^2)`，证明对所有与 `c_u` 分离的 genuine common primes，它精确恢复 source common gcd `G_S` 的局部 exponent；巨大 denominator square scale自动被 `b_3^2` gcd删掉。因此 source common depth和 linear square-root surcharge均可由真实 decimal integers canonical 读取，只剩 fixed `5/11` 的 `c_u` overlap需单列。本文不证明 `G_free=1`，故不关闭 A2。

---

## 1. decimal square collision

已有

\[
B_{\rm dec}=L^2\mathscr B_W,
\qquad
D_{\rm dec}=L^2\mathscr D_W,
\qquad
L=b_3/c_u.
\]

source square collision为

\[
55\mathscr B_W-K^2\mathscr D_W
=c_u^2(18K-55)^2.
\]

乘以 `L^2`，并使用 `L^2c_u^2=b_3^2`：

\[
\boxed{
55B_{\rm dec}-K^2D_{\rm dec}
=b_3^2(18K-55)^2.}
\tag{1.1}

全部量均为真实 decimal/prefix integers。

---

## 2. decimal common gcd contains one known square scale

定义

\[
G_{\rm dec}
:=\gcd\!\left(B_{\rm dec},D_{\rm dec}/2\right).
\]

已有精确式

\[
\boxed{G_{\rm dec}=L^2G_S,}
\tag{2.1}

其中

\[
G_S=\gcd(B_W,D_W/2).
\]

所以 `G_dec` 中的 huge denominator/source common factor `L^2` 完全是已知 square scale。

---

## 3. remove the square scale by one ordinary gcd

定义

\[
\boxed{
G_{\rm free}
:=\frac{G_{\rm dec}}{\gcd(G_{\rm dec},b_3^2)}.}
\tag{3.1}

这是整数。

固定 odd common prime `r`，并假设

\[
\boxed{r\nmid c_u.}
\tag{3.2}

写

\[
\ell:=v_r(L)=v_r(b_3),
\]

\[
k:=v_r(G_S).
\]

由 (2.1)：

\[
\boxed{v_r(G_{\rm dec})=2\ell+k.}
\tag{3.3}

而 (3.2) 下

\[
\boxed{v_r(b_3^2)=2\ell.}
\tag{3.4}

所以

\[
v_r(\gcd(G_{\rm dec},b_3^2))=2\ell,
\]
并得到

\[
\boxed{v_r(G_{\rm free})=k=v_r(G_S).}
\tag{3.5}

因此 `G_free` 在整个 genuine `c_u`-free common sector精确恢复 source common-gcd depth。

---

## 4. fixed `c_u` exceptions are finite

source discriminant gcd audit已有

\[
\gcd(D_W,c_u)\mid55.
\]

所以 odd common prime若违反 (3.2)，只能来自

\[
\boxed{5,11.}
\tag{4.1}

这些是固定 small-prime bookkeeping，不构成新的 moving support。

因此除 `5/11` 外：

\[
\boxed{
\operatorname{Supp}(G_{\rm free})
=\operatorname{Supp}(G_S),}
\tag{4.2}

且所有 local exponents完全相同。

---

## 5. decimal form of the square-root depth law

source common-gcd theorem证明，对 genuine unit common prime

\[
v_r(18K-55)
\ge\left\lceil\frac{v_r(G_S)}2\right\rceil.
\]

使用 (3.5)，可完全改写为

\[
\boxed{
 v_r(18K-55)
\ge\left\lceil\frac{v_r(G_{\rm free})}{2}\right\rceil}
\tag{5.1}

对所有 odd `r notin {5,11}` 且属于 genuine common sector成立。

所以 source common depth的 canonical decimal pipeline现在是

\[
\boxed{
(B_{\rm dec},D_{\rm dec},b_3)
\longrightarrow G_{\rm dec}
\longrightarrow G_{\rm free}
\longrightarrow18K-55.}
\tag{5.2}

不再需要显式恢复 `z,c_u,B_W,D_W`。

---

## 6. parity classification also stays decimal

前文定义

\[
B_{\rm src}^\circ=B_{\rm dec}/G_{\rm dec},
\qquad
D_{\rm src}^\circ=D_{\rm dec}/(2G_{\rm dec}).
\]

它们是 coprime odd integers且具有同一 mod-4 orientation。

所以 source side现在完全由以下原整数派生对象控制：

\[
\boxed{
G_{\rm free},\quad
B_{\rm src}^\circ,\quad
D_{\rm src}^\circ,\quad
18K-55.}
\]

- `G_free` 读 common depth；
- 两 residual quotients读 parity是否被 common gcd吸收；
- `18K-55` 支付 common depth的 square-root height。

---

## 7. current role

这一步把 source parity/common-depth ledger从 source coordinates彻底迁回 decimal plane。后续若做 global gcd ladder、parity allocation或 product-height比较，都可以只操作真实 decimal integers。

唯一需要保留的 source-side exception只是固定 `5/11`，而不是 moving prime family。

A2 仍为 `待证`。

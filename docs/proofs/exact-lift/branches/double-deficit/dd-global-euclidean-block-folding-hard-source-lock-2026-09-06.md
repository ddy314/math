# DD global Euclidean block-folding hard-source lock

> 日期：2026-09-06
>
> 依赖：[`dd-global-sixfold-primitive-hard-source-lock-2026-09-06.md`](dd-global-sixfold-primitive-hard-source-lock-2026-09-06.md)、[`dd-corrected-hard-source-split-2026-08-22.md`](dd-corrected-hard-source-split-2026-08-22.md)。
>
> **严格状态：已严格完成（universal primitive block folding + entire corrected odd non-decimal hard sheet）。**
>
> sixfold reader并非最自然的 decimal normalization。primitive denominator prefix
>
> \[
> C_Q=u_1 10^{m_2}+u_2,
> \qquad (u_1,u_2)=1
> \]
>
> 允许直接把 exponent `n` 按 block length `m_2` 做 Euclidean reduction。令
>
> \[
> k:=\left\lfloor\frac n{m_2}\right\rfloor,
> \qquad
> r_n:=n-km_2,
> \qquad 0\le r_n<m_2.
> \]
>
> 则 full exact lift给一个 target为**最短纯 decimal power** `10^{r_n}` 的 source congruence。对 corrected hard primes，其 coefficient/right-side common depth仍恰为 `M+t`，与 `k` 无关，因此 residual hard modulus仍精确为
>
> \[
> \boxed{\mathfrak C_{\rm E}=X_HT_HN_HJ_H.}
> \]
>
> 相较 sixfold failure charge `log mathfrak C_6 <= n-6S`，Euclidean folding sharpen 为
>
> \[
> \boxed{\log\mathfrak C_{\rm E}\le r_n<m_2}
> \]
>
> whenever ordinary lock fails.

---

## 1. primitive prefix

令

\[
 d_B:=(b_1,b_2),
 \qquad
 u_1:=b_1/d_B,
 \qquad
 u_2:=b_2/d_B.
\]

则

\[
\boxed{C_Q:=Q/d_B=u_1 10^{m_2}+u_2,}
\tag{1.1}
\]

且 `(u_1,u_2)=1`。对任何 `p|C_Q`, `p\nmid10`：

\[
\boxed{p\nmid u_1u_2.}
\tag{1.2}
\]

full exact lift modulo `C_Q|Q` 为

\[
\boxed{
q_{\rm lcm}A_{12}10^n\equiv D_3\pmod{C_Q},
}
\tag{1.3}
\]

其中

\[
D_3:=H_{\rm sph}b_3-q_{\rm lcm}a_3.
\]

---

## 2. arbitrary block folding

对任意整数

\[
0\le k\le\left\lfloor\frac n{m_2}\right\rfloor
\]

把 `(1.3)` 乘 `u_1^k`。由 `(1.1)`：

\[
u_1 10^{m_2}\equiv-u_2\pmod{C_Q},
\]

所以

\[
u_1^k10^{km_2}\equiv(-u_2)^k\pmod{C_Q}.
\]

写

\[
n=km_2+r_k,
\qquad r_k:=n-km_2\ge0.
\]

得到 exact family

\[
\boxed{
C_Q\mid
q_{\rm lcm}A_{12}(-u_2)^k10^{r_k}
-u_1^kD_3.}
\tag{Block-fold-k}
\]

其中 sixfold primitive theorem只是选择某个特定 `k` 后再把 `r_k` 改写成 `6m_1+(n-6S)` 的版本。

---

## 3. Euclidean-optimal exponent

取

\[
\boxed{k_E:=\left\lfloor\frac n{m_2}\right\rfloor,}
\]

\[
\boxed{r_n:=n-k_E m_2.}
\]

则 Euclidean division严格给

\[
\boxed{0\le r_n<m_2.}
\tag{Euclidean-range}
\]

对应的 optimal folding 为

\[
\boxed{
C_Q\mid
C_E10^{r_n}-D_E,}
\tag{Euclidean-fold}
\]

其中

\[
\boxed{
C_E:=q_{\rm lcm}A_{12}(-u_2)^{k_E},
\qquad
D_E:=u_1^{k_E}D_3.}
\tag{3.1}
\]

注意 coefficient中已经没有额外 `10^{km_1}`；所有 decimal exponent都集中在最短 target `10^{r_n}` 中。

---

## 4. universal gcd stripping

定义

\[
\boxed{g_E:=(C_Q,C_E),}
\]

\[
\boxed{Q_E:=C_Q/g_E.}
\]

由 `(Euclidean-fold)` 自动有 `g_E|D_E`。令

\[
\overline C_E=C_E/g_E,
\qquad
\overline D_E=D_E/g_E.
\]

则

\[
\boxed{
Q_E\mid\overline C_E10^{r_n}-\overline D_E,
\qquad
(Q_E,\overline C_E)=1.}
\tag{Euclidean-gcd-stripped}
\]

所以

\[
\boxed{
10^{r_n}\equiv
\overline D_E\overline C_E^{-1}\pmod{Q_E}.}
\tag{Euclidean-residue}
\]

若

\[
\boxed{10^{r_n}<Q_E,}
\]

则直接得到 ordinary exact lock

\[
\boxed{
10^{r_n}
=[\overline D_E\overline C_E^{-1}]_{Q_E}.}
\tag{Euclidean-lock}
\]

---

## 5. hard source local depth 与 `k` 无关

固定 corrected odd non-decimal hard prime。使用记号

\[
E=v_p(b_1)=v_p(b_2),
\quad j=v_p(b_3),
\quad M=\max(E,j),
\]

\[
t=v_p(A_{12}),
\quad n_0=v_p(N_0),
\quad c=v_p(C_Q),
\quad h>0.
\]

corrected hard ledger为

\[
\boxed{c=h+2t+n_0+M+j.}
\tag{5.1}
\]

primitive prefix给 `p\nmid u_1u_2`，而

\[
v_p(q_{\rm lcm})=M.
\]

因此对**任意** `k`：

\[
\boxed{v_p(C_E)=M+t.}
\tag{5.2}
\]

hard gap baseline又给

\[
D_3=b_3La,
\qquad
v_p(D_3)=M+t.
\]

故

\[
\boxed{v_p(D_E)=M+t.}
\tag{5.3}
\]

于是 Euclidean folding逐 hard prime精确 stripping `M+t` 后，剩余 modulus depth为

\[
\boxed{
 c-(M+t)=h+t+n_0+j>0.}
\tag{5.4}
\]

与 `k` 完全无关。

---

## 6. global hard modulus

定义 hard-support products

\[
X_H:=\prod p^h,
\quad
T_H:=\prod p^t,
\quad
N_H:=\prod p^{n_0},
\quad
J_H:=\prod p^j.
\]

逐 prime `(5.4)` 给

\[
\boxed{
\mathfrak C_E
:=\prod_{p\mid X_H}p^{h+t+n_0+j}
=X_HT_HN_HJ_H.}
\tag{Hard-Euclidean-modulus}
\]

并存在 hard-stripped coefficients `\widehat C_E,\widehat D_E` 满足

\[
\boxed{
\mathfrak C_E\mid
\widehat C_E10^{r_n}-\widehat D_E,}
\]

\[
\boxed{
(\widehat C_E,\mathfrak C_E)
=(\widehat D_E,\mathfrak C_E)=1.}
\tag{6.1}
\]

因此

\[
\boxed{
10^{r_n}\equiv
\widehat D_E\widehat C_E^{-1}\pmod{\mathfrak C_E}.}
\tag{Hard-Euclidean-residue}
\]

---

## 7. sharpened ordinary-lock / failure dichotomy

若

\[
\log_{10}\mathfrak C_E>r_n,
\]

则

\[
\boxed{
10^{r_n}
=[\widehat D_E\widehat C_E^{-1}]_{\mathfrak C_E}.}
\tag{Hard-Euclidean-lock}
\]

若 ordinary criterion失败，则

\[
\boxed{
\log_{10}(X_HT_HN_HJ_H)
\le r_n.}
\tag{Euclidean-failure-charge}
\]

而 Euclidean range给

\[
\boxed{r_n<m_2.}
\tag{7.1}
\]

所以无条件有

\[
\boxed{
\text{failure branch}
\Longrightarrow
\log(X_HT_HN_HJ_H)<m_2.}
\tag{7.2}
\]

这严格 sharpen sixfold failure bound

\[
\log(X_HT_HN_HJ_H)\le n-6S
\]

whenever `r_n<n-6S`; 即使两者次序相反，Euclidean reader仍是同一 block-fold family中 exponent最短的 canonical representative。

---

## 8. neighboring foldings没有第二独立 reader

`k` 与 `k+1` 两条 `(Block-fold-k)` 由

\[
u_1 10^{m_2}\equiv-u_2\pmod{C_Q}
\]

可逆互相转换（在 odd non-decimal source support上 `u_1,u_2,10` 都是 units）。因此不能把不同 `k` 的 foldings当成独立 moduli重复收费。

Euclidean choice的价值是**最短 exponent normalization**，不是制造第二 parent。

---

## 9. 当前意义

corrected hard-source obstruction现在可以统一写成：

\[
\boxed{
\mathfrak C_E=X_HT_HN_HJ_H
}
\]

要么 ordinary读取一个长度 `<m_2` 的纯十进制幂 `10^{r_n}`，要么其全部 hard/source+baseline height被 `r_n` 直接控制。

因此 post-tail 下一步应把 `(Euclidean-failure-charge)` 喂回 corrected second-Schmidt bootstrap；ordinary-lock branch若要排除，则必须引入与 prefix block folding不同的第二 global decimal parent或 multiplicative-order/Archimedean input。

---

## 10. 状态摘要

- **已严格完成：** arbitrary primitive block folding；
- **已严格完成：** Euclidean-optimal remainder `0<=r_n<m_2`；
- **已严格完成：** universal gcd stripping；
- **已严格完成：** hard source residual depth `h+t+n_0+j` 与 folding index无关；
- **已严格完成：** global modulus `X_HT_HN_HJ_H`；
- **已严格完成：** sharpened ordinary-lock/failure-charge dichotomy；
- **no-go：** neighboring `k` foldings不是 independent readers；
- **未证明：** ordinary-lock branch impossible、post-tail global strict gap、DD emptiness。

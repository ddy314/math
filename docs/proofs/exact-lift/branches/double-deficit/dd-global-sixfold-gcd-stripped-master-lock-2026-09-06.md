# DD global sixfold gcd-stripped master lock

> 日期：2026-09-06
>
> 依赖：[`dd-global-sixfold-decimal-folding-source-lock-2026-09-06.md`](dd-global-sixfold-decimal-folding-source-lock-2026-09-06.md)、[`dd-corrected-hard-source-split-2026-08-22.md`](dd-corrected-hard-source-split-2026-08-22.md)。
>
> **严格状态：已严格完成（universal gcd-stripped lock + full-height deep-hard consequence）。**
>
> sixfold folding可用一个 canonical gcd normalization统一处理所有 coefficient baseline。无需预先把 source primes分成 exact baseline-free / good / bad：对任何 high-slope DD candidate定义
> \[
> C_6:=q_{\rm lcm}A_{12}b_2^6 10^{6m_1},
> \qquad
> D_6:=b_1^6(H_{\rm sph}b_3-q_{\rm lcm}a_3),
> \]
> \[
> g_6:=(Q,C_6),
> \qquad
> Q_6:=Q/g_6.
> \]
> 则 universal sixfold identity自动给
> \[
> \boxed{
> Q_6\mid
> \frac{C_6}{g_6}10^{n-6S}
> -\frac{D_6}{g_6},
> \qquad
> \left(Q_6,\frac{C_6}{g_6}\right)=1.}
> \]
> 因而只要 `Q_6>10^{n-6S}`，就得到 ordinary exact reconstruction。
>
> corrected deep-hard full-height regime中，已有 source/baseline tradeoff进一步强迫
> \[
> \boxed{g_6=10^{o(S)},\qquad Q_6=10^{S-o(S)}.}
> \]
> 所以整个 dangerous full-height deep-hard branch自动进入该 ordinary lock。本文给前一 primewise stripping theorem一个更简洁、更 canonical 的 master formulation。

---

## 1. sixfold input

在 `6S<n<7S` 中令

\[
\boxed{e:=n-6S.}
\]

前一 theorem证明

\[
\boxed{Q\mid C_6 10^e-D_6,}
\tag{Sixfold}
\]

其中

\[
\boxed{
C_6=q_{\rm lcm}A_{12}b_2^6 10^{6m_1},}
\tag{1.1}
\]

\[
\boxed{
D_6=b_1^6D_3,
\qquad
D_3=H_{\rm sph}b_3-q_{\rm lcm}a_3.}
\tag{1.2}
\]

所有量均为整数。

---

## 2. universal gcd stripping lemma

定义

\[
\boxed{g_6:=(Q,C_6).}
\tag{2.1}
\]

因为

\[
g_6\mid Q,
\qquad
g_6\mid C_6,
\]

而 `(Sixfold)` 给

\[
g_6\mid C_6 10^e-D_6,
\]

所以

\[
\boxed{g_6\mid D_6.}
\tag{2.2}
\]

因此可定义

\[
\boxed{
Q_6:=Q/g_6,
\qquad
\overline C_6:=C_6/g_6,
\qquad
\overline D_6:=D_6/g_6.}
\tag{2.3}
\]

将 `(Sixfold)` 除以 `g_6`：

\[
\boxed{
Q_6\mid\overline C_6 10^e-\overline D_6.}
\tag{Gcd-stripped-sixfold}
\]

逐 prime比较 exponent即可得到 elementary but crucial fact：

\[
\boxed{(Q_6,\overline C_6)=1.}
\tag{Coefficient-unit}
\]

确实，若

\[
v_p(Q)=u,
\qquad
v_p(C_6)=v,
\]
则 `g_6` 删除 `min(u,v)` 层；余下 exponents分别为

\[
(u-v)_+,
\qquad
(v-u)_+,
\]
不可能同时为正。

于是对**任意** high-slope DD candidate都有 canonical fixed residue

\[
\boxed{
10^e
\equiv
\overline D_6\,\overline C_6^{-1}
\pmod{Q_6}.}
\tag{Master-residue}
\]

这不需要 canonical one-channel、Gaussian splitting、source genericity或 baseline-free hypothesis。

---

## 3. ordinary representative criterion

令

\[
\rho_6:=
[\overline D_6\overline C_6^{-1}]_{Q_6}
\in\{0,1,\ldots,Q_6-1\}.
\]

若

\[
\boxed{0<10^e<Q_6,}
\tag{3.1}
\]

则 `(Master-residue)` 立即升级为

\[
\boxed{10^e=\rho_6.}
\tag{Master-lock}
\]

所以问题完全被压到一个 gcd height：

\[
\boxed{
\text{控制 }g_6=(Q,C_6)\text{ 的高度}
\Longrightarrow
\text{控制 sixfold decimal-power location}.}
\]

---

## 4. dangerous deep-hard source 强迫 `g_6` subexponential

现在进入 corrected deep-hard regime，并假设

\[
\boxed{\log_{10}X_{H,D}=S-o(S).}
\tag{4.1}
\]

因为

\[
X_{H,D}\mid C_Q\mid Q,
\]
且 `Q` 是 `S`-digit prefix denominator：

\[
10^{S-1}\le Q<10^S,
\]
故

\[
\boxed{
\log_{10}(Q/X_{H,D})=o(S).}
\tag{4.2}
\]

对 `X_{H,D}` support上的 prime，沿 corrected notation：

\[
E=v_p(b_1)=v_p(b_2),
\quad
j=v_p(b_3),
\quad
M=\max(E,j),
\quad
t=v_p(A_{12}).
\]

lcm denominator给

\[
v_p(q_{\rm lcm})=M.
\]

因此

\[
\boxed{v_p(C_6)=M+t+6E.}
\tag{4.3}
\]

定义 aggregate baseline products

\[
M_H:=\prod p^M,
\qquad
T_H:=\prod p^t,
\qquad
E_H:=\prod p^E.
\]

full-height deep-hard tradeoff已经证明

\[
\boxed{
\log M_H,
\log T_H=o(S),}
\tag{4.4}
\]
且 `E<=M` 给

\[
\boxed{E_H\mid M_H,\qquad\log E_H=o(S).}
\tag{4.5}
\]

所以 restricted gcd

\[
g_X:=(X_{H,D},C_6)
\]
满足

\[
\boxed{
g_X\mid M_HT_HE_H^6,}
\tag{4.6}
\]
从而

\[
\boxed{\log g_X=o(S).}
\tag{4.7}
\]

---

## 5. outside-source gcd 只能落在 `Q/X_HD`

这里使用一个 elementary divisor inequality。若

\[
X\mid Q,
\]
则对任意 `C`：

\[
\boxed{
\frac{(Q,C)}{(X,C)}\mid\frac QX.}
\tag{5.1}
\]

逐 prime证明：令 exponents为 `q>=x` 与 `c`，左侧 exponent为

\[
\min(q,c)-\min(x,c)
\le q-x.
\]

应用于

\[
X=X_{H,D},
\qquad C=C_6,
\]
得到

\[
\boxed{
\frac{g_6}{g_X}\mid\frac{Q}{X_{H,D}}.}
\tag{5.2}
\]

所以由 `(4.2)`、`(4.7)`：

\[
\boxed{\log_{10}g_6=o(S).}
\tag{Gcd-small}
\]

这一步把 primewise good/bad stripping统一成一个全局 gcd statement。

---

## 6. master modulus 保留 full height

由定义

\[
Q_6=Q/g_6.
\]

又

\[
\log Q=S+O(1),
\qquad
\log g_6=o(S),
\]
故

\[
\boxed{
\log_{10}Q_6=S-o(S).}
\tag{Master-full-height}
\]

safe global DD upper给

\[
\frac eS=\frac nS-6
\le z_*+o(1),
\qquad
z_*=0.308883577618\ldots<1.
\]

因此

\[
\log 10^e\le(z_*+o(1))S,
\]
而

\[
\log Q_6=(1-o(1))S.
\]

leading margin仍为

\[
1-z_*=U_*=0.691116422381969\ldots.
\]

于是 sufficiently large `S`：

\[
\boxed{0<10^e<Q_6.}
\tag{6.1}
\]

代入 `(Master-lock)`：

\[
\boxed{
10^{n-6S}
=
\left[
\frac{D_6}{g_6}
\left(\frac{C_6}{g_6}\right)^{-1}
\right]_{Q/g_6}.}
\tag{Deep-hard-master-lock}
\]

所以 full-height corrected deep-hard branch的 large source obstruction已经可以完全用 canonical gcd `g_6` 表述，而不需要选择 prime subsets。

---

## 7. 与 primewise stripping theorem 的关系

[`dd-global-sixfold-baseline-stripped-deephard-lock-2026-09-06.md`](dd-global-sixfold-baseline-stripped-deephard-lock-2026-09-06.md) 给出 finer local information：

\[
r_p=h+t+n_0+j-5E,
\]
以及在 `r_p>0` support上

\[
v_p(D_3)=M+t.
\]

本文不取代这些 local conclusions；它把 ordinary reconstruction所需的 global modulus canonical 化成

\[
\boxed{Q_6=Q/(Q,C_6).}
\]

primewise theorem解释 **为什么** dangerous source上这个 gcd小；master theorem则说明后续 global work只需研究一个自然对象 `g_6`，无需人为 split support。

---

## 8. no-double-count audit for `D_3`

在 hard sheet中

\[
D_3=b_3(H_{\rm sph}-y_3)=b_3La.
\]

对 odd non-decimal target prime，`L` 为 `2/5`-smooth，所以

\[
v_p(D_3)=j+v_p(a).
\]

corrected hard-sheet gap baseline为

\[
v_p(a)=t+(E-j)_+.
\]

于是

\[
\boxed{
v_p(D_3)
=j+t+(E-j)_+
=t+\max(E,j)
=M+t.}
\tag{8.1}
\]

这与 primewise sixfold stripping在 good support强迫的 `v_p(D_3)=M+t` **完全相同**。

因此该 local residual depth不是新 payer；sixfold attack真正新增的是 global coefficient-unit decimal-power residue，而不是再次向 gap baseline收费。

---

## 9. 当前攻击面

master theorem把 full-height post-tail pure-source branch压成：

\[
\boxed{
Q_6=10^{S-o(S)},
\qquad
(C_6/g_6,Q_6)=1,
\qquad
10^{n-6S}\text{ 是一个 fixed ordinary residue mod }Q_6.}
\]

下一步真正有价值的输入必须改变这份 residue的 global location，例如：

1. 对同一 `Q_6` 构造第二个 independent pure-power reader；
2. 对 `Q_6` 的 source primes证明足以限制 `ord_p(10)` 的 global order theorem；
3. 把 `(Master-lock)` 作为 exponentially small remainder输入 moving-target/Subspace/Ridout 型 argument；
4. 从 another full exact-lift block folding得到不由 prefix relation重构的不同 exponent phase。

仅重新展开 `D_3=b_3La` 或 tail-root sign不会产生第二 height；这些已经由 §8 与现有 ultra-hard no-go审计封死。

---

## 10. 状态摘要

- **已严格完成：** universal gcd stripping `g_6=(Q,C_6)`；
- **已严格完成：** canonical coefficient-unit modulus `Q_6=Q/g_6`；
- **已严格完成：** full-height deep-hard regime `g_6=10^{o(S)}`；
- **已严格完成：** `Q_6=10^{S-o(S)}` 与 ordinary `10^{n-6S}` master lock；
- **已严格完成：** `D_3` local depth与旧 gap baseline完全同源的 no-double-count audit；
- **仍待证：** second independent reader / order or Archimedean obstruction；post-tail strict slope gap；DD emptiness。

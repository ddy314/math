# A2 source-common / height-descent overlap 的 square-root depth theorem

> **依赖：** `spontaneous-crt-source-descent-overlap.md`、`spontaneous-source-parity-common-gcd.md`、`spontaneous-crt-height-primitive-remainder.md`。
>
> **严格状态：**上一文件只对 source-common/descent-common 的 support radical给出双短-carrier约束。本文利用 `F63^(16)` 与 source collision sheet之间的 exact Bezout identity，把完整 common gcd 的一半深度也收费到同一两个短 carrier。若 `k_r` 是某 genuine prime在 source common gcd、`Rstar_63`、`Dhat_63` 三者中的共同深度，则 `r^{ceil(k_r/2)}` 同时整除 `18K-55` 与 `H_S63`。因此整个 common gcd满足 square-root-depth product bound，而不仅是 squarefree radical bound。本文不证明该 common gcd为空，因此不关闭 A2。

---

## 1. common-depth notation

沿用 source common gcd 的 genuine unit-separated部分

\[
G_S^{\rm gen}
=
\prod_{r\in E_S^{\rm gen}}r^{s_r},
\qquad
s_r:=v_r(G_S).
\tag{1.1}
\]

旧 source square-collision theorem 已证明

\[
\boxed{
v_r(18K-55)
\ge
\left\lceil\frac{s_r}{2}\right\rceil.}
\tag{1.2}
\]

现在同时考虑 fully primitive descended pair

\[
\mathscr R_{63}^\star,
\qquad
\widehat{\mathscr D}_{63}.
\]

对每个 genuine source-common prime定义三重 common depth

\[
\boxed{
k_r
:=
\min\!\left\{
 s_r,
 v_r(\mathscr R_{63}^\star),
 v_r(\widehat{\mathscr D}_{63})
\right\}.}
\tag{1.3}
\]

只有 `k_r>=1` 的 prime真正属于 source-common/descent-common overlap。

定义完整 common factor

\[
\boxed{
G_{SD}
:=
\prod_{r\in E_S^{\rm gen}}r^{k_r}.}
\tag{1.4}
\]

---

## 2. exact Bezout between descendant equation and source sheet

上一文件定义

\[
\boxed{
\mathscr H_{S63}
=102383gT-29952ga_3+14976C5^\lambda.}
\tag{2.1}
\]

以及 cleared descended equation

\[
\boxed{
\begin{aligned}
F_{63}^{(16)}={}&
16(2K-9)
\{g((2K-12)T-2a_3)+5^\lambda C\}\\
&-63gTK^2.
\end{aligned}}
\tag{2.2}
\]

resultant `Res_K(F63^(16),18K-55)=-H_S63` 事实上来自一个更强的 exact polynomial Bezout：

\[
\boxed{
324F_{63}^{(16)}+\mathscr H_{S63}
=(18K-55)\mathscr Q_{S63},}
\tag{2.3}
\]

其中

\[
\boxed{
\mathscr Q_{S63}
:=576C5^\lambda
+18KgT
-12041gT
-1152ga_3.}
\tag{2.4}
\]

直接展开即可验证。

---

## 3. each common prime pays half its depth into `H_S63`

固定 `r` 满足 `k_r>=1`。由定义

\[
v_r(\widehat{\mathscr D}_{63})\ge k_r.
\]

`Dhat_63` 与 `F63^(16)` 只差 genuine `r`-units / fixed powers of `2,c_u`，所以

\[
\boxed{v_r(F_{63}^{(16)})\ge k_r.}
\tag{3.1}
\]

另一方面由 (1.2)，并因 `s_r>=k_r`：

\[
\boxed{
v_r(18K-55)
\ge
\left\lceil\frac{s_r}{2}\right\rceil
\ge
\left\lceil\frac{k_r}{2}\right\rceil.}
\tag{3.2}
\]

令

\[
t_r:=\left\lceil\frac{k_r}{2}\right\rceil.
\]

在 Bezout (2.3) 中：

- `324F63^(16)` 至少有 `k_r>=t_r` 层；
- `(18K-55)Q_S63` 至少有 `t_r` 层。

所以二者之差 `H_S63` 也至少有 `t_r` 层：

\[
\boxed{
v_r(\mathscr H_{S63})
\ge
\left\lceil\frac{k_r}{2}\right\rceil.}
\tag{3.3}
\]

这把上一文件的 first-layer support statement升级为完整 square-root-depth收费。

---

## 4. global square-root-depth product divides both short carriers

定义

\[
\boxed{
H_{SD}
:=
\prod_{r\in E_S^{\rm gen}}
 r^{\lceil k_r/2\rceil}.}
\tag{4.1}
\]

逐 prime由 (3.2),(3.3)：

\[
\boxed{H_{SD}\mid18K-55,}
\tag{4.2}
\]

\[
\boxed{H_{SD}\mid\mathscr H_{S63}.}
\tag{4.3}
\]

而 endpoint bounds为

\[
0<18K-55<180N,
\]

\[
0<\mathscr H_{S63}
<\frac{9076339}{125}gT.
\]

因此

\[
\boxed{
H_{SD}
<
\min\!\left\{
180N,
\frac{9076339}{125}gT
\right\}.}
\tag{4.4}
\]

所以 source/descent common gcd的完整深度不能任意堆积在 descendant internal syzygy中；至少一半深度必须同时由两个独立尺度的短 natural representatives承担。

---

## 5. exact square-root bookkeeping identity

定义 common gcd 中 odd-exponent radical

\[
\boxed{
R_{SD}^{\rm odd}
:=
\prod_{\substack{r\in E_S^{\rm gen}\\k_r\text{ odd}}}r.}
\tag{5.1}
\]

逐 exponent 有

\[
2\left\lceil\frac{k_r}{2}\right\rceil
=
k_r+(k_r\bmod2).
\]

所以

\[
\boxed{
H_{SD}^2
=G_{SD}\,R_{SD}^{\rm odd}.}
\tag{5.2}
\]

结合 (4.4)：

\[
\boxed{
G_{SD}R_{SD}^{\rm odd}
<(180N)^2,}
\tag{5.3}
\]

并且同时有

\[
\boxed{
G_{SD}R_{SD}^{\rm odd}
<\left(\frac{9076339}{125}gT\right)^2.}
\tag{5.4}
\]

注意这不是说 `G_SD` 本身整除两个短 carrier；整除的是其 canonical square-root-depth lift `H_SD`。本文严格保留这一差别。

---

## 6. relation to target overlap

source-common genuine support与 entire equal-depth target support已经有 complete separation：

\[
\operatorname{Supp}_{\rm gen}(G_S)
\cap
\operatorname{Supp}_{\rm gen}(G_{\rm tar})
=\varnothing.
\tag{6.1}
\]

所以新 common factor `G_SD` 与此前 fixed target/descent common factor

\[
G_{TD}\mid31\cdot179
\]
在 genuine support上互素：

\[
\boxed{\gcd(G_{SD},G_{TD})=1.}
\tag{6.2}
\]

因此 target reuse 与 source-common reuse可在 global product/parity ledger中独立收费，不存在同一 genuine prime被两套 overlap账本重复计算的问题。

---

## 7. revised descendant-overlap frontier

当前 `Rstar_63/Dhat_63` common support的两大 old-source channels都已有 canonical计价：

1. target overlap：固定 squarefree
   \[
   G_{TD}\mid5549;
   \]
2. source-common overlap：完整 common depth通过
   \[
   H_{SD}^2=G_{SD}R_{SD}^{odd},
   \qquad
   H_{SD}\mid\gcd(18K-55,H_{S63})
   \]
   收费。

且两者 genuine support互素。

下一步若做 global parity，应把 `G_TD` 与 `G_SD` 从 descendant common gcd中分开，再审计仍未归属 target/source-common 的 residual common parity。若 residual common part为空，则在 `Z=1 mod4` 的 parity-doubling分支会真正迫使两枚不同 generic inert primes。

A2 仍为 `待证`。

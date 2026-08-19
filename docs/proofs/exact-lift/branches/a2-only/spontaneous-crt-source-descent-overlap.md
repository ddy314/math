# A2 source-common 与 height-descent common support 的短 carrier

> **依赖：** `spontaneous-source-parity-common-gcd.md`、`spontaneous-source-parity-collision-gate.md`、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descent-overlap-nogo.md`。
>
> **严格状态：**source parity 的 genuine reused prime必须进入 `18K-55`；height-descent parity若由同一 prime在 `Rstar_63,Dhat_63` 中复用，则该 prime也进入 cleared descendant equation `F63^(16)`。本文直接消去 `K`，resultant退化成一个只有 third/source 尺度的正线性 carrier `H_S63`。所以 source-common/descent common support不能自由复用：每个 genuine common prime必须同时进入 `18K-55` 与 `H_S63`。此外 fixed `13` 被严格排除。本文尚未证明这两个短 carrier互素，因此不关闭 A2。

---

## 1. two common-support equations

source common gcd 的 genuine unit-separated prime `r` 满足

\[
\boxed{r\mid18K-55.}
\tag{1.1}
\]

这是 exact square collision

\[
55\mathscr B_W-K^2\mathscr D_W
=c_u^2(18K-55)^2
\]
的直接结果。

另一方面 fully primitive height descent中

\[
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.
\]

若同一个 genuine prime同时进入

\[
r\mid\mathscr R_{63}^\star,
\qquad
r\mid\widehat{\mathscr D}_{63},
\tag{1.2}
\]
则 descended quotient的 cleared equation为

\[
\boxed{
\begin{aligned}
F_{63}^{(16)}:={}&
16(2K-9)
\{g((2K-12)T-2a_3)+5^\lambda C\}\\
&-63gTK^2,
\end{aligned}}
\tag{1.3}
\]
且

\[
\boxed{r\mid F_{63}^{(16)}.}
\tag{1.4}
\]

由

\[
\gcd(\mathscr R_{63}^\star,10g)=1
\]
还自动有

\[
\boxed{r\nmid10g.}
\tag{1.5}
\]

---

## 2. eliminate `K`: a short mixed source carrier

直接对 (1.3) 与 `18K-55` 求 resultant：

\[
\boxed{
\operatorname{Res}_K(F_{63}^{(16)},18K-55)
=-\mathscr H_{S63},}
\tag{2.1}
\]

其中

\[
\boxed{
\mathscr H_{S63}
:=102383\,gT
-29952\,g a_3
+14976\,C5^\lambda.}
\tag{2.2}
\]

因此任意 genuine source-common/descent-common prime满足

\[
\boxed{
r\mid\mathscr H_{S63}.}
\tag{2.3}
\]

所以 common support被同时装入两个短整数：

\[
\boxed{
r\mid\gcd(18K-55,\mathscr H_{S63}).}
\tag{2.4}
\]

这里没有 quadratic character，也没有 resultant degree增长；`K` 被线性 source sheet完全消掉。

---

## 3. `H_S63` is positive and short

写 endpoint normalized variables

\[
\zeta:=\frac{a_3}{T},
\qquad
\delta:=\frac CD.
\]

由

\[
gT=D5^\lambda
\]
可把 (2.2) 除以 `gT`：

\[
\boxed{
\frac{\mathscr H_{S63}}{gT}
=102383-29952\zeta+14976\delta.}
\tag{3.1}
\]

当前 dangerous endpoint给

\[
1<\zeta<\frac{251}{250},
\qquad
0<\delta<\frac3{250}.
\]

所以

\[
\boxed{
\frac{9038899}{125}
<\frac{\mathscr H_{S63}}{gT}
<\frac{9076339}{125}.}
\tag{3.2}
\]

即

\[
\boxed{
72311.192\,gT
<\mathscr H_{S63}
<72610.712\,gT.}
\tag{3.3}
\]

特别地 `H_S63` 是严格正的 natural representative，而不是只有模 `r` 意义的形式。

source sheet本身还有

\[
0<18K-55<180N.
\tag{3.4}
\]

因此 source/descent common support同时受一个 `N`-scale linear carrier和一个 `gT`-scale mixed carrier控制。

---

## 4. fixed `13` is impossible

系数分解为

\[
\boxed{
14976=2^7\cdot3^2\cdot13,}
\tag{4.1}
\]

\[
29952=2\cdot14976,
\]

\[
\boxed{102383=43\cdot2381.}
\tag{4.2}
\]

模 `13`：

\[
14976\equiv29952\equiv0,
\qquad
102383\equiv8\not\equiv0.
\]

若 `r=13` 同时进入 (2.3)，则

\[
0\equiv\mathscr H_{S63}
\equiv8gT\pmod{13}.
\]

但 descendant common prime由 (1.5) 与 `13\nmid10` 满足 `13\nmid g`，同时 `13\nmid T`。矛盾。

所以

\[
\boxed{13\notin
\operatorname{Supp}_{\rm gen}
(\text{source-common}\cap\text{descent-common}).}
\tag{4.3}
\]

这也意味着旧 source collision sheet与 additive central sheet的唯一 odd common prime `13` 不能充当新的 descent parity reuse通道。

---

## 5. support radical budget

令 `E_SD` 为 genuine source-common primes中同时进入 `Rstar_63,Dhat_63` 的 support，并定义 squarefree radical

\[
\boxed{R_{SD}:=\prod_{r\in E_{SD}}r.}
\tag{5.1}
\]

由 (2.4)：

\[
\boxed{
R_{SD}\mid\gcd(18K-55,\mathscr H_{S63}).}
\tag{5.2}
\]

因此

\[
\boxed{
R_{SD}<180N,}
\tag{5.3}
\]

并同时

\[
\boxed{
R_{SD}<\frac{9076339}{125}gT.}
\tag{5.4}
\]

(5.3) 对 support radical已经很短；若要对 source common gcd的完整 exponent收费，仍应使用既有 square-root-depth product `H_S^gen|18K-55`，本文不把 radical bound误写成 full-depth bound。

---

## 6. current source/descent frontier

现在 descended common parity与两个主要旧 prime-source pools的 overlap都已被压缩：

- equal-depth target pool：只剩 fixed squarefree `G_TD|31*179`；
- source-common pool：必须进入
  \[
  \gcd(18K-55,\mathscr H_{S63}),
  \]
  且 fixed `13` 不可能。

所以一个 target-free descendant common inert supplier若还想复用 source parity，必须支付两个独立短 natural carriers，而不能只依靠 `Rstar/Dhat` 的 internal syzygy。

下一步最有价值的是把 `H_S63` 与 source discriminant `D_W` / source triangle联立，继续压缩 fixed coefficient primes `43,2381` 与 generic source root；或在 global parity ledger中先除去 `R_SD`，研究剩余 descendant pair是否仍强迫 distinct inert support。

A2 仍为 `待证`。

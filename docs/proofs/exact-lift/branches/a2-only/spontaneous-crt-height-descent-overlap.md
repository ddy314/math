# A2 sphere-height / descendant common overlap 的 fixed-`67` orientation

> **依赖：** `primitive-reduction.md`、`spontaneous-height-equal-depth-target-selector.md`、`spontaneous-residual-parity-doubling.md`、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-target-descent-overlap.md`。
>
> **严格状态：**每个 non-3 inert divisor of `W_q` 已被锁到真实 height `H_0`。本文进一步要求该 prime进入 fully primitive descendant common gcd。`alpha,H_0` 同时消失后，descended quotient强迫固定 quadratic `G_D=11K^2-240K+432`；original carrier又强迫该 prime进入 `J_H`，因此回流到 canonical height gcd `D_H=gcd(B_W,W_q)`。消去 `K` 后得到 source quartic `H_67`，其 square completion只含 fixed discriminant `67`。generic height/descent common inert prime必须满足 `(67/r)=1`，而 ramified `r=67` 因要求一个非平方 `63` 成为 `(z/c_u)^2` 被严格排除。若再与 source-common sheet相交，resultant只剩 fixed `139,463`。本文仍允许满足 fixed-67 orientation的 moving height primes，因此不关闭 A2。

---

## 1. height prime entering descendant common support

固定 odd prime

\[
r\ne3,
\qquad
r\equiv3\pmod4,
\qquad
r\mid W_q,
\]
并假设它还进入 descendant common gcd

\[
G_\Delta
=
\gcd(\mathscr R_{63}^\star,
     \widehat{\mathscr D}_{63}).
\]

已有 height theorem 给

\[
\boxed{
r\nmid c_Qc_ugXY,}
\tag{1.1}

\[
\boxed{
v_r(W_q)=v_r(H_0),}
\tag{1.2}

\[
\boxed{
\left(\frac{N_0}{r}\right)=-1.}
\tag{1.3}

因为

\[
\alpha=\omega W_q,
\qquad
H_0=c_uW_q,
\]
立刻有

\[
\boxed{r\mid\alpha,\qquad r\mid H_0.}
\tag{1.4}

---

## 2. descendant equation forces `G_D(K)=0`

fully primitive descended quotient满足 exact identity

\[
\boxed{
16\mathscr F_{63}
=3gT G_D(K)
-16(2K-9)(g\alpha+H_0),}
\tag{2.1}

其中

\[
\boxed{G_D(K)=11K^2-240K+432.}
\tag{2.2}

`Dhat_63=c_u^2 F_63`，且由 (1.1) `r∤3c_ugT`。使用 (1.4)：

\[
\boxed{r\mid\widehat{\mathscr D}_{63}
\Longrightarrow
G_D(K)\equiv0\pmod r.}
\tag{2.3}

所以 every height/descent common prime被送进同一固定 K-quadratic。

它的 discriminant为

\[
\boxed{
\operatorname{Disc}(G_D)
=38592
=24^2\cdot67.}
\tag{2.4}

---

## 3. original carrier sends the same prime back to the canonical height gcd

height-free additive identity为

\[
\boxed{
\widehat{\mathcal T}_2
=5^m\widehat{\mathcal J}_H
-2^{m+1}B_0^2(2K-9)\alpha,}
\tag{3.1}

其中 `B_0=c_ug`。

若 `r|G_Delta`，positive descent说明

\[
r\mid\widehat{\mathcal T}_2.
\]

再用 (1.4)，(3.1) 模 `r` 化为

\[
0\equiv5^m\widehat{\mathcal J}_H.
\]

所以

\[
\boxed{r\mid\widehat{\mathcal J}_H.}
\tag{3.2}

而已有 canonical height gcd identity

\[
\boxed{
D_H
:=\gcd(\widehat{\mathcal J}_H,W_q)
=\gcd(\mathscr B_W,W_q).}
\tag{3.3}

结合 `r|W_q`：

\[
\boxed{r\mid\mathscr B_W.}
\tag{3.4}

所以 height/descent common prime不是新的自由 source label；它自动落入既有 height gcd `D_H`。

---

## 4. eliminate `K`: the source quartic `H_67`

source companion为

\[
\boxed{
\mathscr B_W
=c_u^2(5K^2-36K+55)+z^2K^2.}
\tag{4.1}

由 (1.1)，`c_u` 为 r-unit。

先注意 `z` 也不能在 genuine inert common root上为零。若 `r|z`，(4.1) 与 (3.4) 会给

\[
5K^2-36K+55\equiv0.
\]

但

\[
\boxed{
\operatorname{Res}_K(
G_D,
5K^2-36K+55)
=527017
=17\cdot29\cdot1069,}
\tag{4.2}

三个 odd prime全部为 `1 mod4`。所以 inert r不可能来自 `z=0`。

因此可定义 r-unit

\[
v:=z/c_u.
\]

将 (4.1) 除以 `c_u^2`，与 `G_D=0` 对 K 消元：

\[
\boxed{
186624v^4+779040v^2+527017
\equiv0\pmod r.}
\tag{4.3}

乘回 `c_u^4`，定义 ordinary positive source carrier

\[
\boxed{
\mathscr H_{67}
:=186624z^4
+779040z^2c_u^2
+527017c_u^4.}
\tag{4.4}

于是

\[
\boxed{r\mid\mathscr H_{67}.}
\tag{4.5}

---

## 5. exact square completion and fixed-67 orientation

(4.4) 有精确 completion：

\[
\boxed{
9\mathscr H_{67}
=
(1296z^2+2705c_u^2)^2
-67(196c_u^2)^2.}
\tag{5.1}

验证只需展开；系数恒等式为

\[
2705^2-67\cdot196^2
=9\cdot527017.
\]

对 `r\ne67`，由 (4.5)、`r∤3c_u`：

\[
\left(
\frac{1296z^2+2705c_u^2}{196c_u^2}
\right)^2
\equiv67\pmod r.
\]

所以

\[
\boxed{
\left(\frac{67}{r}\right)=1.}
\tag{5.2}

由于

\[
67\equiv r\equiv3\pmod4,
\]
quadratic reciprocity给

\[
\boxed{
\left(\frac r{67}\right)=-1.}
\tag{5.3}

因此 every generic height/descent common inert prime都被固定到 mod-67 nonresidue orientation。

---

## 6. ramified prime `67` is impossible

若 `r=67`，(5.1) 与 `H_67=0` 给

\[
1296z^2+2705c_u^2\equiv0\pmod{67}.
\]

因 `c_u` 为 unit：

\[
\boxed{
(z/c_u)^2
\equiv-2705\cdot1296^{-1}
\equiv63\pmod{67}.}
\tag{6.1}

但直接 Euler criterion / quadratic-residue table给

\[
\boxed{
\left(\frac{63}{67}\right)=-1.}
\tag{6.2}

左边 `(z/c_u)^2` 必为平方，矛盾。因此

\[
\boxed{67\notin\operatorname{Supp}(G_\Delta)
\quad\text{through the height channel}.}
\tag{6.3}

所以 fixed discriminant prime本身没有 singular Hensel branch。

---

## 7. triple overlap with source-common is only fixed `139,463`

若同一 height/descent common prime还属于 source common gcd，已有 collision sheet

\[
18K-55\equiv0\pmod r.
\]

与 (2.2) resultant：

\[
\boxed{
\operatorname{Res}_K(G_D,18K-55)
=-64357
=-139\cdot463.}
\tag{7.1}

因此 genuine triple overlap满足

\[
\boxed{
r\in\{139,463\}.}
\tag{7.2}

两个 fixed primes都为 `3 mod4`；对应 K states唯一：

\[
\boxed{
K\equiv88\pmod{139},
\qquad
K\equiv286\pmod{463}.}
\tag{7.3}

所以 source-common与 height-common 两类 old source label若同时试图承担 descendant common parity，不存在 moving intersection。

---

## 8. revised height/common frontier

height/descent common support现在满足三层规范约束：

1. canonical gcd:
   \[
   r\mid D_H=\gcd(B_W,W_q);
   \]
2. fixed K quadratic:
   \[
   G_D(K)\equiv0;
   \]
3. source quartic / character:
   \[
   r\mid H_{67},
   \qquad
   (r/67)=-1,
   \qquad r\ne67.
   \]

若再进入 source-common pool，只剩 fixed `139,463`。

因此 descendant common parity的 remaining height source已经不再是任意 `W_q` prime；它必须同时通过 canonical height gcd和 fixed-67 orientation。尚缺的是排除满足这些条件的 moving height prime，或证明其 common exponent parity不能使 `G_Delta≡3 mod4`。

A2 仍为 `待证`。

# A2 target 的 source/third four-sheet split

> **依赖：** `spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-equal-depth-dual-short-carriers.md`、`spontaneous-height-equal-depth-triple-orientation.md`。
>
> **严格状态：**本文识别 source-prefix resultant 与 prefix quadratic之间和 third carrier完全平行的 exact two-sheet factorization。`D^2P-R_PD=6UL_D`，其中 target source sheet `U=DK-N=qW_q`，conjugate source sheet `L_D=D(K-6)+N`；在 genuine non-`2,3,5` common sector，两条 sheet互斥。与 third-side 的 `T^2P-R_3=6 alpha L_3` 联立后，任何同时进入三个 norm carriers `P,R_PD,R_3` 的 genuine prime唯一落入四个 source/third sheet pairs之一。真正 equal-depth target被 canonical 地锁在 `(alpha,U)` sheet；其它三格是 conjugate collisions。本文完成 root-sheet allocation，不排除 target sheet本身，因此不关闭 A2。

---

## 1. source-prefix identity本身已经因式分解

沿用

\[
P=6K^2-36K+55,
\qquad
U=DK-N,
\]

\[
R_{PD}=55D^2-36DN+6N^2.
\]

`spontaneous-height-equal-depth-target-ladder.md` 给出的 identity为

\[
D^2P
=R_{PD}+(12N-36D)U+6U^2.
\]

右侧 correction可以直接因式分解：

\[
(12N-36D)U+6U^2
=6U(U+2N-6D).
\]

而

\[
U+2N-6D
=DK-N+2N-6D
=D(K-6)+N.
\]

定义 source conjugate sheet

\[
\boxed{L_D:=D(K-6)+N.}
\tag{1.1}
\]

于是得到完全对称于 third carrier 的 exact identity：

\[
\boxed{D^2P-R_{PD}=6U L_D.}
\tag{1.2}
\]

与 third-side

\[
\boxed{T^2P-R_3=6\alpha L_3,}
\qquad
L_3=T(K-6)-a_3,
\tag{1.3}
\]

形成一对平行 sheet factorizations。

---

## 2. source 两条 sheet 在 genuine common sector互斥

两条 source linear forms满足

\[
\boxed{U+L_D=2D(K-3).}
\tag{2.1}
\]

而

\[
P=6(K-3)^2+1
\]
给

\[
\boxed{\gcd(P,K-3)=1.}
\tag{2.2}
\]

固定 odd prime

\[
p\nmid6DN,
\qquad p\mid P.
\]

若 `p|U,L_D`，则由 (2.1) 强迫 `p|K-3`，与 (2.2) 矛盾。因此

\[
\boxed{
p\mid P
\Longrightarrow
p\text{ 不可能同时进入 }U,L_D
\quad(p\nmid6D).}
\tag{2.3}
\]

另一方面若 `p|P,R_PD`，由 (1.2) 且 `p\nmid6D`：

\[
p\mid U L_D.
\]
结合 (2.3)：

\[
\boxed{
p\mid P,R_{PD}
\Longrightarrow
\text{恰有一条 }U=0\text{ 或 }L_D=0\pmod p.}
\tag{2.4}
\]

所以 source-prefix common root不是一个模糊 quadratic collision，而是两个明确互斥的 Hensel sheets。

---

## 3. source sheet 的 `sqrt(-6)` orientation

定义

\[
X_P=6(K-3),
\qquad
X_D=\frac{55D-18N}{N}.
\]

若取 target source sheet

\[
U=DK-N\equiv0\pmod p,
\]
则前一文件已证明

\[
\boxed{X_D\equiv-X_P\pmod p.}
\tag{3.1}
\]

若改取 conjugate source sheet

\[
L_D=D(K-6)+N\equiv0\pmod p,
\]
则

\[
\frac DN\equiv-\frac1{K-6}\pmod p.
\]
于是

\[
X_D
\equiv-\frac{55}{K-6}-18
=\frac{53-18K}{K-6}.
\]

而使用 `P=0`：

\[
6(K-3)(K-6)
=6K^2-54K+108
\equiv53-18K.
\]

所以

\[
\boxed{L_D=0\Longrightarrow X_D\equiv+X_P\pmod p.}
\tag{3.2}
\]

因此 source 两 sheets 正好就是 `sqrt(-6)` 的 `-/+` 两个 orientations。

---

## 4. third 两 sheets 同样是 `-/+` orientations

`spontaneous-height-equal-depth-dual-short-carriers.md` 已有

\[
\alpha=TK+a_3,
\qquad
L_3=T(K-6)-a_3.
\]

定义

\[
X_3=6\frac{a_3+3T}{T}.
\]

若

\[
\alpha\equiv0\pmod p,
\]
则 `a_3/T=-K`，故

\[
\boxed{X_3\equiv-X_P\pmod p.}
\tag{4.1}
\]

若

\[
L_3\equiv0\pmod p,
\]
则 `a_3/T=K-6`，故

\[
\boxed{X_3\equiv+X_P\pmod p.}
\tag{4.2}
\]

所以 source 与 third 两侧都具有同一 canonical sign convention：

\[
\boxed{
\begin{array}{c|c}
\text{sheet}&\sqrt{-6}\text{ orientation}\\ \hline
U&-\\
L_D&+\\
\alpha&-\\
L_3&+
\end{array}}
\tag{4.3}
\]

---

## 5. 三个 norm carriers 的 four-sheet partition

固定 genuine prime

\[
p\nmid30DN,
\]
并假设

\[
p\mid P,
\qquad
p\mid R_{PD},
\qquad
p\mid R_3.
\]

source two-sheet split (2.4) 给唯一选择

\[
U\quad\text{or}\quad L_D,
\]

third two-sheet split给唯一选择

\[
\alpha\quad\text{or}\quad L_3.
\]

因此 `p` 唯一落入四格之一：

\[
\boxed{
\begin{array}{c|c|c}
&\text{third }- &\text{third }+\\ \hline
\text{source }-&(U,\alpha)&(U,L_3)\\
\text{source }+&(L_D,\alpha)&(L_D,L_3)
\end{array}}
\tag{5.1}
\]

其中 diagonal 两格 orientation相同，off-diagonal 两格 orientation相反。

`spontaneous-height-equal-depth-triple-orientation.md` 的 cross carrier

\[
\mathcal L_{D3}=TN(X_D-X_3)
\]

正好在两个 diagonal sheets 上 first-layer 消失；它的 fixed `2671` next-depth exception是在真正 target diagonal `(U,alpha)` 上继续审计 normalized depth所得。

---

## 6. 真正 equal-depth target 被锁在 `(U,alpha)` sheet

对 genuine equal-depth omega-height target：

\[
U=qW_q,
\qquad
v_p(U)=h\ge1,
\]

以及

\[
\alpha=\omega W_q,
\qquad
v_p(\alpha)=2h.
\]

所以它必在

\[
\boxed{(U,\alpha)}
\tag{6.1}
\]

这一格。

而 source/third conjugates满足

\[
\boxed{p\nmid L_D L_3.}
\tag{6.2}
\]

因此后续研究 target无需再携带另外三种 root signs；它们是明确的 non-target sheet collisions。

此外 target-ladder给

\[
v_p(P)=v_p(R_{PD})=h
\quad(p\ne7,\ \rho_p\ge1),
\]

dual-short文件给

\[
v_p(R_3)=h.
\]

所以 moving target `p\ne7` 在三个 norm carriers上都以同一 baseline depth `h` 进入同一个 `(-,-)` sheet。

---

## 7. canonical sheet selectors

定义两个普通整数 gcd：

\[
\boxed{G_{P,U}:=\gcd(P,U),}
\tag{7.1}
\]

\[
\boxed{G_{P,\alpha}:=\gcd(P,\alpha).}
\tag{7.2}
\]

对真正 equal-depth target：

\[
\boxed{
v_p(G_{P,U})=h,
\qquad
v_p(G_{P,\alpha})=h.}
\tag{7.3}
\]

所以 target baseline可以进一步写成 fully integer intersection

\[
\boxed{G_{--}:=\gcd(P,U,\alpha).}
\tag{7.4}
\]

并在 target support上精确读取 `h`。

`G_{--}` 本身可能含不满足 residual oversaturation / equal-depth resonance 的额外 primes，因此它是 sheet selector而不是完整 target selector。完整 deep target仍需与 `G_JB`、`Lambda_tail` 等 canonical gates联立。

---

## 8. 当前 four-sheet frontier

三个 `sqrt(-6)` norm carriers 的 moving root ambiguity现在已经全部离散化：

\[
\boxed{
P
\rightsquigarrow
\begin{cases}
U\text{ or }L_D,\\
\alpha\text{ or }L_3,
\end{cases}}
\]

而真正 target固定为

\[
\boxed{U=0,\qquad\alpha=0}
\]

的 double-minus sheet。

所以 moving `p\notin\{7,2671\}` 的剩余困难不再包含 quadratic root sign选择；prefix/source/third orientation全部已经固定。剩余自由只在：

1. baseline 后的 p-adic unit digits；
2. `Lambda_tail` 的 excess depth `rho_p`；
3. global product / parity allocation。

下一步应把 `G_{--}` 与 `Sigma_deep` 合成 fully canonical double-minus target carrier，并检查其 primitive parity / height是否足以承担 global odd-inert excess。

A2 仍为 `待证`。

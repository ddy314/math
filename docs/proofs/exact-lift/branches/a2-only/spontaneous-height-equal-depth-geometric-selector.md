# A2 deep equal-depth target 的 geometric carrier selector

> **依赖：** `spontaneous-height-equal-depth-target-selector.md`、`spontaneous-height-equal-depth-four-sheet-split.md`、`spontaneous-height-equal-depth-triple-orientation.md`、`spontaneous-height-equal-depth-tail-gcd-ladder.md`。
>
> **严格状态：**本文用 four-sheet geometry进一步简化 deep-target selector。对 genuine non-`2,3,5` sector，`P=R_PD=0` 只允许 source 的 `U`/`L_D` 两个 orientations；`alpha=0` 固定 third 为 minus orientation，而 `L_D3=0` 强迫 source 与 third orientation一致，因此自动选择 target source sheet `U=0`。再与 residual companion carrier `G_JB` 和 canonical tail quotient `Lambda_tail` 取 gcd，得到 `Sigma_geom=gcd(G_JB,P,R_PD,alpha,L_D3,Lambda_tail)`。在当前 genuine denominator-separated sector，它无需显式输入 `Gamma` 或人工 prime list即可选择 residual oversaturation + double-minus source/third sheet + equal-depth deep resonance。本文仍需 inert congruence filter，不宣称 A2 closure。

---

## 1. 已有 four-sheet geometry

沿用

\[
P=6K^2-36K+55,
\]

\[
R_{PD}=55D^2-36DN+6N^2,
\]

\[
\alpha=TK+a_3,
\]

以及 cross-orientation carrier

\[
\mathcal L_{D3}=55TD-36TN-6Na_3.
\]

`spontaneous-height-equal-depth-four-sheet-split.md` 已证明：对 genuine prime

\[
p\nmid30DN,
\qquad p\mid P,R_{PD},
\]

source root唯一落在

\[
U:=DK-N=0
\]

或

\[
L_D:=D(K-6)+N=0
\]

两条互斥 sheets之一；其 `sqrt(-6)` orientations分别为

\[
U:\ -,
\qquad
L_D:\ +.
\tag{1.1}
\]

third side同理：

\[
\alpha:\ -,
\qquad
L_3:=T(K-6)-a_3:\ +.
\tag{1.2}
\]

而

\[
\boxed{
\mathcal L_{D3}=TN(X_D-X_3)}
\tag{1.3}
\]

正是 source/third normalized roots之差。

---

## 2. `P,R_PD,alpha,L_D3` 自动选择 double-minus sheet

固定 genuine prime满足

\[
\boxed{
p\mid P,
\quad p\mid R_{PD},
\quad p\mid\alpha,
\quad p\mid\mathcal L_{D3}.}
\tag{2.1}
\]

由 `p|alpha`，third side被固定为 minus orientation：

\[
\boxed{X_3\equiv-X_P\pmod p.}
\tag{2.2}
\]

由 `p|P,R_PD`，source side只有两种可能：

\[
X_D\equiv-X_P
\quad\text{或}\quad
X_D\equiv+X_P.
\tag{2.3}
\]

又 `p|L_D3` 与 (1.3) 给

\[
X_D\equiv X_3\pmod p.
\]

结合 (2.2)：

\[
\boxed{X_D\equiv-X_P.}
\tag{2.4}
\]

因此 source 不能是 plus sheet `L_D=0`，必须是

\[
\boxed{U=DK-N\equiv0\pmod p.}
\tag{2.5}
\]

所以四个自然 carriers `P,R_PD,alpha,L_D3` 已经在 first layer自动选择真正 target 的 double-minus geometry：

\[
\boxed{(U,\alpha).}
\tag{2.6}
\]

这一步不需要显式把 `U` 放进 gcd selector。

---

## 3. double-minus sheet + `Lambda_tail` 自动恢复 equal depth

由 (2.5) 和

\[
U=qW_q,
\]
当前 genuine denominator separation `p\nmid q` 给

\[
\boxed{p\mid W_q.}
\tag{3.1}
\]

写

\[
e=v_p(\omega),
\qquad
h=v_p(W_q)\ge1.
\]

`spontaneous-height-equal-depth-tail-gcd-ladder.md` 在当前 genuine coefficient-separated sector证明

\[
 v_p(\Lambda_{\rm tail})
 =
 \begin{cases}
 0,&e\ne h,\\
 \rho_p,&e=h.
 \end{cases}
\tag{3.2}
\]

这里允许 `e=0<h`：此时仍落在第一行，tail 是 p-unit。

因此若在 double-minus sheet上再有

\[
p\mid\Lambda_{\rm tail},
\]
则必有

\[
\boxed{e=h\ge1,
\qquad\rho_p>0.}
\tag{3.3}
\]

所以 `Gamma=gcd(omega,W_q)` 虽然仍是有用的 square-core reader，却不再是**定义 deep target support**所必需的 selector input。

---

## 4. residual oversaturation carrier

沿用

\[
D_H
=\gcd(\widehat{\mathcal J}_H,W_q)
=\gcd(\mathscr B_W,W_q),
\]

\[
J^\circ=\widehat{\mathcal J}_H/D_H,
\qquad
B^\circ=\mathscr B_W/D_H,
\]

以及

\[
\boxed{G_{JB}:=\gcd(J^\circ,B^\circ).}
\tag{4.1}
\]

因此

\[
p\mid G_{JB}
\]

精确表示完整 height gcd约去后两个 companions仍继续共享 `p`。

---

## 5. geometric deep-target selector

定义普通整数

\[
\boxed{
\Sigma_{\rm geom}
:=\gcd(
G_{JB},
P,
R_{PD},
\alpha,
\mathcal L_{D3},
\Lambda_{\rm tail}
).}
\tag{5.1}
\]

固定当前 genuine non-`3` denominator-separated prime `p`。

若

\[
p\mid\Sigma_{\rm geom},
\]
则：

1. `p|G_JB`：residual `J^circ/B^circ` oversaturation；
2. `p|P,R_PD,alpha,L_D3`：由 §2 自动进入 double-minus `(U,alpha)` sheet；
3. `p|U`：故 `p|W_q`；
4. `p|Lambda_tail`：由 §3 强迫 `e=h` 且 `rho_p>0`。

所以

\[
\boxed{
 p\mid\Sigma_{\rm geom}
 \Longrightarrow
 \begin{cases}
 p\mid J^\circ,B^\circ,\\
 p\mid U,\alpha,\\
 v_p(\omega)=v_p(W_q)\ge1,\\
 \rho_p>0.
 \end{cases}}
\tag{5.2}
\]

反过来，真正 deep equal-depth residual target满足上述所有条件，并且 target-ladder / dual-short / triple-orientation文件分别给

\[
p\mid P,R_{PD},\alpha,\mathcal L_{D3},\Lambda_{\rm tail},G_{JB}.
\]

因此在该 genuine sector有 support equivalence：

\[
\boxed{
 p\mid\Sigma_{\rm geom}
 \Longleftrightarrow
 p\text{ 是 deep equal-depth residual double-minus target prime},}
\tag{5.3}
\]

这里尚未编码 `p≡3 mod4` / inertness；split common primes也会被 selector看见。

---

## 6. target p-depth of the geometric selector

对真正 target写

\[
h=v_p(\omega)=v_p(W_q),
\qquad
r_{JB}:=v_p(G_{JB})\ge1.
\]

已有

\[
v_p(P)=h,
\qquad
v_p(\alpha)=2h,
\qquad
v_p(\Lambda_{\rm tail})=\rho_p.
\]

对 moving primes：

\[
v_p(R_{PD})=h\quad(p\ne7),
\]

\[
v_p(\mathcal L_{D3})=h\quad(p\ne2671).
\]

但即使 `p=7` 或 `2671`，`P` 本身仍只有 exact depth `h`。所以统一有

\[
\boxed{
 v_p(\Sigma_{\rm geom})
 =\min\{r_{JB},h,\rho_p\}.}
\tag{6.1}
\]

也就是说 fixed `7/2671` 的 companion extra-depth不会人为放大 selector；prefix carrier `P` 自动把 selector截回真实 baseline `h`。

---

## 7. 与旧 `Sigma_deep` 的关系

旧 selector为

\[
\Sigma_{\rm deep}
=\gcd(G_{JB},\Gamma,\Lambda_{\rm tail}).
\]

它通过 `Gamma` 选择 common equal-depth sector。

新 selector改用 four-sheet geometry：

\[
P,R_{PD},\alpha,\mathcal L_{D3}
\Longrightarrow U\text{ sheet},
\]

再由

\[
U+\Lambda_{\rm tail}
\Longrightarrow e=h,\rho_p>0.
\]

所以 `Sigma_geom` 是一个独立的 geometric realization：它把 equal-depth source/third orientation显式编码进 natural carriers，而不是先调用 square-core gcd。

两个 selector可互相审计，但本文不把它们的形式差异当作新的 obstruction。

---

## 8. 当前 frontier

现在 deep target有两种 fully canonical描述：

\[
\boxed{
\Sigma_{\rm deep}
=\gcd(G_{JB},\Gamma,\Lambda_{\rm tail}),}
\]

以及

\[
\boxed{
\Sigma_{\rm geom}
=\gcd(G_{JB},P,R_{PD},\alpha,\mathcal L_{D3},\Lambda_{\rm tail}).}
\]

后者的优势是直接暴露四个 natural carriers：prefix、source-prefix、true numerator、source/third orientation。

因此下一步可不再逐 prime追踪 root signs，而直接研究

\[
\boxed{\operatorname{Supp}_{3\bmod4}(\Sigma_{\rm geom})}
\]

的 primitive parity 与高度；或者比较 `Sigma_geom` 与 `Sigma_deep` 的 inert parts，寻找一个完全 global 的 parity mismatch。

A2 仍为 `待证`。

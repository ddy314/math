# A2 deep equal-depth oversaturation 的 canonical target selector

> **依赖：** `spontaneous-height-companion-cross.md`、`spontaneous-height-equal-depth-tail-gcd-ladder.md`、`spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-resultant-parity.md`。
>
> **严格状态：**前面的论证已经分别 canonical 化了三件事：`J_H/B_W` 在完整 height gcd 之后是否继续共享 prime、`omega/W_q` 是否为 equal-depth common prime、以及该 equal-depth prime 是否具有 `rho_p>0` 的 resonance tail。本文把三层合成一个普通整数 gcd `Sigma_deep=gcd(G_JB,Gamma,Lambda_tail)`。在当前 genuine non-`3` denominator-separated sector，`p|Sigma_deep` 当且仅当 `p` 同时是 residual `J^circ/B^circ` common prime、equal-depth `omega/W_q` common prime、且 resonance tail 为正。因此 deep equal-depth omega-height oversaturation support 不再需要预先列 prime 集合即可定义。本文只给 support selector；split primes 或其它非目标 sector仍需按既有 genuine/inert 条件过滤，不宣称 A2 closure。

---

## 1. residual companion common carrier

已有全局 height gcd

\[
\boxed{
D_H
:=\gcd(\widehat{\mathcal J}_H,W_q)
=\gcd(\mathscr B_W,W_q).}
\tag{1.1}
\]

定义 height-free companions

\[
\boxed{
J^\circ:=\frac{\widehat{\mathcal J}_H}{D_H},
\qquad
B^\circ:=\frac{\mathscr B_W}{D_H}.}
\tag{1.2}
\]

再定义

\[
\boxed{
G_{JB}:=\gcd(J^\circ,B^\circ).}
\tag{1.3}
\]

于是对任意 odd prime：

\[
\boxed{
p\mid G_{JB}
\Longleftrightarrow
p\mid J^\circ\ \text{且}\ p\mid B^\circ.}
\tag{1.4}
\]

所以 `G_JB` 正是“完整 height part 已约掉以后，两个 companions仍然复用同一 prime”的 canonical integer carrier。

---

## 2. equal-depth common square carrier

此前 square-core / tail-normalization 文件定义

\[
\boxed{
\Gamma:=\gcd(\omega,W_q).}
\tag{2.1}
\]

逐 common prime写

\[
e=v_p(\omega),
\qquad
h=v_p(W_q).
\]

则

\[
v_p(\Gamma)=\min(e,h).
\tag{2.2}
\]

同时 canonical tail quotient为

\[
\boxed{
\Lambda_{\rm tail}
=\frac{\Lambda_{\rm dec}}
{\gcd(\alpha,\Lambda_{\rm dec})}.}
\tag{2.3}
\]

`spontaneous-height-equal-depth-tail-gcd-ladder.md` 已在当前 genuine non-`3` denominator-separated common-prime sector证明

\[
\boxed{
 v_p(\Lambda_{\rm tail})
 =
 \begin{cases}
 0,&e\ne h,\\[1mm]
 \rho_p,&e=h.
 \end{cases}}
\tag{2.4}
\]

因此

\[
\boxed{
p\mid\gcd(\Gamma,\Lambda_{\rm tail})
\Longleftrightarrow
e=h\ge1\ \text{且}\ \rho_p>0}
\tag{2.5}
\]

在该 genuine sector成立。

---

## 3. 三层合并成一个 ordinary gcd

定义

\[
\boxed{
\Sigma_{\rm deep}
:=\gcd(
G_{JB},
\Gamma,
\Lambda_{\rm tail}
).}
\tag{3.1}
\]

固定当前 genuine non-`3` denominator-separated common prime `p`。

若

\[
p\mid\Sigma_{\rm deep},
\]
则：

1. `p|G_JB`，故完整 height gcd 约去后仍有
   \[
   p\mid J^\circ,
   \qquad
   p\mid B^\circ;
   \]
2. `p|Gamma`，故 `p` 同时进入 `omega,W_q`；
3. `p|Lambda_tail`，结合 (2.4) 强迫
   \[
   e=h,
   \qquad
   \rho_p>0.
   \]

反过来，若 `p` 满足

\[
p\mid J^\circ,
\quad
p\mid B^\circ,
\quad
e=h\ge1,
\quad
\rho_p>0,
\]
则显然

\[
p\mid G_{JB},
\quad
p\mid\Gamma,
\quad
p\mid\Lambda_{\rm tail},
\]
所以

\[
p\mid\Sigma_{\rm deep}.
\]

因此得到 exact support equivalence：

\[
\boxed{
 p\mid\Sigma_{\rm deep}
 \Longleftrightarrow
 \begin{cases}
 p\mid J^\circ,\ B^\circ,\\
 v_p(\omega)=v_p(W_q)\ge1,\\
 \rho_p>0,
 \end{cases}}
\tag{3.2}
\]

对当前 genuine non-`3` denominator-separated common-prime sector成立。

---

## 4. inert omega-height targets 现在只是 `Sigma_deep` 的一个 filtered support

本文的 `Sigma_deep` 本身不编码 quadratic inertness。真正当前 parity target 还要求

\[
p\equiv3\pmod4,
\]
以及 parent omega-height analysis给出的

\[
\boxed{p\equiv7\text{ 或 }11\pmod{24}.}
\tag{4.1}
\]

所以真正 deep equal-depth inert oversaturation target support 可以理解为

\[
\boxed{
\operatorname{Supp}(\Sigma_{\rm deep})
\cap
\{p:p\equiv7,11\pmod{24}\},}
\tag{4.2}
\]

并继续排除仓库中已经单列的 fixed / denominator / central exceptions。

重要的是：prime set 现在只是 `Sigma_deep` 的 support filter，而不再是定义 resonance branch 所必需的外部数据。

---

## 5. selected target 自动进入短 prefix quadratic

`spontaneous-height-equal-depth-target-ladder.md` 已证明：对真正 equal-depth omega-height oversaturation target，

\[
\boxed{
v_p(\mathcal P_{\omega H}(K))=h,}
\tag{5.1}
\]
其中

\[
\mathcal P_{\omega H}(K)
=6K^2-36K+55
\]
并且

\[
\boxed{
599N^2
<\mathcal P_{\omega H}(K)
<600N^2.}
\tag{5.2}
\]

所以每个 inert target prime `p|Sigma_deep` 在通过既有 omega-height target 条件后，其 baseline `p^h` 都由一个恰有 `2M+3` 位的 pure-prefix integer精确读取。

因此可以定义无需 prime list 的 candidate prefix selector

\[
\boxed{
G_{\rm pref}
:=\gcd(
\Gamma,
\mathcal P_{\omega H}(K)
).}
\tag{5.3}
\]

对每个真正 selected target：

\[
\boxed{v_p(G_{\rm pref})=h.}
\tag{5.4}
\]

`G_pref` 可能含有不满足 residual companion condition的额外 prime，因此 (5.4) 是 target-support exactness，而不是 converse characterization。

---

## 6. deep target ladder 的 fully canonical pipeline

现在无需预先 factorization或手工 prime pool即可写出：

\[
\boxed{
\begin{aligned}
D_H
&=\gcd(\widehat{\mathcal J}_H,W_q),\\
G_{JB}
&=\gcd(\widehat{\mathcal J}_H/D_H,
        \mathscr B_W/D_H),\\
\Gamma
&=\gcd(\omega,W_q),\\
\Lambda_{\rm tail}
&=\Lambda_{\rm dec}/\gcd(\alpha,\Lambda_{\rm dec}),\\
\Sigma_{\rm deep}
&=\gcd(G_{JB},\Gamma,\Lambda_{\rm tail}),\\
G_{\rm pref}
&=\gcd(\Gamma,\mathcal P_{\omega H}(K)).
\end{aligned}}
\tag{6.1}
\]

在 genuine inert target sector，`Sigma_deep` 选择 deep equal-depth residual overlap support，而 `G_pref` 为这些 selected targets 读取完整 baseline `h`。

这把此前的逻辑

\[
\text{residual overlap}
+\text{equal depth}
+\text{deep unit resonance}
+\text{target quadratic}
\]

压成了一组 ordinary integer gcds。

---

## 7. 当前 frontier

现在真正需要关闭的 moving object不再是一个人工定义的 prime family，而是 canonical integer

\[
\boxed{\Sigma_{\rm deep}.}
\tag{7.1}
\]

对其 genuine inert support：

- baseline depth由 `G_pref` / `P_{omega H}` 的 `2M+3` 位窗口控制；
- full resonance depth由 `Lambda_tail` 控制；
- source-prefix resultant `R_PD` 已证明除 fixed `7` 外只能保持 baseline `h`；
- fixed `7` extra-depth branch已进一步压成 `M≡1,5 (mod 6)` 的四个 mod-`7` states。

所以后续最直接的 closure target是证明

\[
\boxed{
\operatorname{Supp}_{\rm inert}(\Sigma_{\rm deep})
=\varnothing,}
\tag{7.2}
\]

或至少证明其 weighted product不足以承担 global odd-inert parity。

A2 仍为 `待证`。
# A2 equal-depth target 的 orthogonal decimal norm 与 fixed-exception complementarity

> **依赖：** `spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-equal-depth-triple-orientation.md`、`spontaneous-height-equal-depth-fixed-exception-transversality.md`、`spontaneous-height-equal-depth-dual-short-carriers.md`、`spontaneous-height-equal-depth-decimal-pair.md`。
>
> **严格状态：**本文把 source-prefix resultant `R_PD`、source/third cross orientation `L_D3` 与它的正交 companion 全部乘回真实 decimal concatenations。得到三个完全 source-free 的 natural integers，并证明它们满足一个 exact positive binary-norm identity。新的 orthogonal carrier 在所有 genuine deep equal-depth targets 上除 fixed `7` 的另一根外都精确读取 baseline；在 `p=7` 时，它与 `R_PD` 的 extra-depth root 恰好互补：`K=2` 只让 `R_PD` 加深，`K=4` 只让 orthogonal carrier 加深，二者不能同时坏。fixed `2671` 则只有 parallel cross carrier加深，另外两条仍精确 baseline。本文完成 fixed-exception 的三方向分流，但不排除 normalized higher cancellation，因此不关闭 A2。

---

## 1. decimal scaling

沿用

\[
\alpha=TK+a_3,\qquad
\beta=TQ+b_3,
\]

以及 exact determinant

\[
\Delta:=\Delta_\omega=Kb_3-Qa_3=E_MN\omega.
\]

记

\[
\boxed{c:=E_M\omega=\frac{\Delta}{N}.}
\tag{1.1}
\]

`Delta/N` 是整数。由

\[
\beta=E_MD\omega,
\qquad
U:=DK-N=qW_q,
\]
和 `E_+=E_M omega R_+`，有四条 exact decimalization：

\[
\boxed{cD=\beta,\qquad cN=\Delta,\qquad cU=Q\alpha,\qquad cR_+=E_+.}
\tag{1.2}
\]

其中第三条也可直接从

\[
K\beta-\Delta=Q\alpha
\]
看出。

对 genuine equal-depth target

\[
v_p(\omega)=v_p(W_q)=h\ge1,
\]
当前 denominator separation 给 `p∤E_MN`，因此

\[
\boxed{v_p(c)=h.}
\tag{1.3}
\]

---

## 2. source-prefix resultant 的完全 decimal 版本

定义

\[
R_{PD}:=55D^2-36DN+6N^2.
\]

把 (1.2) 直接代入，得到

\[
\boxed{
\Xi_{PD}
:=55\beta^2-36\beta\Delta+6\Delta^2
=c^2R_{PD}.}
\tag{2.1}
\]

它还具有正定形式

\[
\boxed{
\Xi_{PD}
=\beta^2+6(\Delta-3\beta)^2>0.}
\tag{2.2}
\]

以及

\[
\boxed{
55\Xi_{PD}
=(55\beta-18\Delta)^2+6\Delta^2.}
\tag{2.3}
\]

因此 target 上

\[
\boxed{
v_p(\Xi_{PD})=2h+v_p(R_{PD}).}
\tag{2.4}
\]

此前 target-ladder 已证明 deep resonance 中

\[
p\ne7\Longrightarrow v_p(R_{PD})=h.
\]
所以

\[
\boxed{
p\ne7\Longrightarrow v_p(\Xi_{PD})=3h.}
\tag{2.5}
\]

而 fixed `7` extra-resultant root会使 `v_7(Xi_PD)>3h`。

---

## 3. parallel cross carrier 的完全 decimal 版本

沿用

\[
L_{D3}
=T(55D-18N)-6N(a_3+3T).
\]

定义

\[
\boxed{
\Xi_{\parallel}
:=55T\beta-36T\Delta-6a_3\Delta.}
\tag{3.1}
\]

利用 (1.2)：

\[
\begin{aligned}
\Xi_{\parallel}
&=c\left[T(55D-18N)-6N(a_3+3T)\right]\\
&=cL_{D3}.
\end{aligned}
\]

所以

\[
\boxed{
\Xi_{\parallel}=cL_{D3},
\qquad
v_p(\Xi_{\parallel})=h+v_p(L_{D3}).}
\tag{3.2}
\]

`spontaneous-height-equal-depth-triple-orientation.md` 给

\[
p\ne2671\Longrightarrow v_p(L_{D3})=h.
\]
因此

\[
\boxed{
p\ne2671\Longrightarrow v_p(\Xi_{\parallel})=2h.}
\tag{3.3}
\]

fixed `2671` orientation exception 则满足

\[
\boxed{v_{2671}(\Xi_{\parallel})>2h.}
\tag{3.4}
\]

另由 decimal-pair identity `E_+=cR_+`、`cU=Qalpha` 可写成完全等价的 corrected form

\[
\boxed{
\Xi_{\parallel}
=T\left(E_+-(5K-36)Q\alpha\right)-6\Delta\alpha.}
\tag{3.5}
\]

这说明 fixed `2671` 的 normalized cancellation可以完全在真实 decimal integers中读取。

---

## 4. 新的 orthogonal cross carrier

令

\[
A_D:=55D-18N,
\qquad
u_3:=a_3+3T.
\]

`L_D3` 是

\[
L_{D3}=TA_D-6N\nu_3.
\]

定义其 binary norm 的正交 companion

\[
\boxed{
L_\perp:=A_D\nu_3+NT.}
\tag{4.1}
\]

乘以 `c` 后定义 pure decimal integer

\[
\boxed{
\Xi_\perp
:=(55\beta-18\Delta)(a_3+3T)+\Delta T.}
\tag{4.2}
\]

由 (1.2) 立刻有

\[
\boxed{
\Xi_\perp=cL_\perp.}
\tag{4.3}
\]

所以 target 上

\[
\boxed{
v_p(\Xi_\perp)=h+v_p(L_\perp).}
\tag{4.4}
\]

---

## 5. `L_perp` 的 deep next-layer formula

把

\[
a_3=\alpha-TK,
\qquad
U=DK-N,
\qquad
R_+=DP-KU,
\]

其中

\[
P=6K^2-36K+55,
\]
代入 (4.1)，直接展开得到

\[
\boxed{
L_\perp
=(55D-18N)\alpha
+3TR_+
+T(53-15K)U.}
\tag{5.1}
\]

固定 deep equal-depth target。已有

\[
v_p(\alpha)=2h,
\qquad
v_p(R_+)\ge h+1,
\qquad
v_p(U)=h.
\tag{5.2}
\]

且 `55D-18N` 是 p-unit：若 `p` 同时整除它与 `R_PD`，由

\[
55R_{PD}=(55D-18N)^2+6N^2
\]
和 `p∤6N` 得矛盾。

写

\[
U=p^hU_0,
\qquad p\nmid U_0.
\]

将 (5.1) 除以 `p^h` 并模 `p`，前两项消失，得到

\[
\boxed{
\frac{L_\perp}{p^h}
\equiv
T(53-15K)U_0
\pmod p.}
\tag{5.3}
\]

因此

\[
\boxed{
v_p(L_\perp)>h
\Longleftrightarrow
15K-53\equiv0\pmod p.}
\tag{5.4}
\]

---

## 6. orthogonal extra-depth 只有 fixed `7`，而且是 `P` 的另一根

`P` 与 `15K-53` 有 exact Bezout identity

\[
\boxed{
75P+(74-30K)(15K-53)=203=7\cdot29.}
\tag{6.1}
\]

因此若 genuine target prime同时满足

\[
p\mid P,
\qquad
p\mid15K-53,
\]
则

\[
p\mid203.
\]

当前 genuine inert target 满足

\[
p\equiv7\text{ 或 }11\pmod{24}.
\]
`29≡5 mod24` 不属于 genuine inert class，所以只剩

\[
\boxed{p=7.}
\tag{6.2}
\]

于是

\[
\boxed{
p\ne7\Longrightarrow v_p(L_\perp)=h}
\tag{6.3}
\]

以及纯 decimal 版本

\[
\boxed{
p\ne7\Longrightarrow v_p(\Xi_\perp)=2h.}
\tag{6.4}
\]

模 `7`，quadratic `P` 恰有两根

\[
\boxed{K\equiv2,4\pmod7.}
\tag{6.5}
\]

而

\[
15K-53\equiv K-4\pmod7,
\]
所以 orthogonal extra-depth精确选择

\[
\boxed{K\equiv4\pmod7.}
\tag{6.6}
\]

另一方面 target-ladder 的 fixed-7 `R_PD` exception满足

\[
36D-11N\equiv0\pmod7.
\]
配合 `DK≡N mod7`，它等价于

\[
36-11K\equiv0\pmod7,
\]
即

\[
\boxed{K\equiv2\pmod7.}
\tag{6.7}
\]

所以 fixed `7` 的两个 extra directions正好命中 `P` 的两张不同 simple roots。

---

## 7. fixed `7` 的 complementarity theorem

由 §§2、6：

### root `K=2 mod 7`

\[
\boxed{
v_7(R_{PD})>h,
\qquad
v_7(L_\perp)=h.}
\tag{7.1}
\]

对应 decimal depths

\[
\boxed{
v_7(\Xi_{PD})>3h,
\qquad
v_7(\Xi_\perp)=2h.}
\tag{7.2}
\]

### root `K=4 mod 7`

此时 `R_PD` 的 exceptional linear coefficient为 unit，所以

\[
\boxed{
v_7(R_{PD})=h,
\qquad
v_7(L_\perp)>h.}
\tag{7.3}
\]

对应

\[
\boxed{
v_7(\Xi_{PD})=3h,
\qquad
v_7(\Xi_\perp)>2h.}
\tag{7.4}
\]

因此无条件得到

\[
\boxed{
\min\{v_7(R_{PD}),v_7(L_\perp)\}=h.}
\tag{7.5}
\]

换句话说，fixed `7` 不可能同时让 source-prefix norm 与 orthogonal cross direction超过 baseline；两个“坏方向”被两张不同 roots彻底拆开。

---

## 8. exact decimal norm identity

由

\[
55R_{PD}=A_D^2+6N^2,
\qquad
R_3=T^2+6\nu_3^2,
\]
二次型 Lagrange identity给

\[
\boxed{
55R_{PD}R_3
=L_{D3}^2+6L_\perp^2.}
\tag{8.1}
\]

乘以 `c^2`，再使用 §§2--4 的 decimalization：

\[
\boxed{
55\Xi_{PD}R_3
=\Xi_{\parallel}^2+6\Xi_\perp^2.}
\tag{8.2}
\]

这是一个完全由真实 decimal concatenations / prefix integers构成的 positive binary norm identity。

---

## 9. 三方向 exact-depth table

对 genuine deep equal-depth target，三个 decimal directions现在有：

\[
\boxed{
\begin{array}{c|c|c|c}
\text{prime sector}
&v_p(\Xi_{PD})
&v_p(\Xi_{\parallel})
&v_p(\Xi_\perp)\\ \hline
p\notin\{7,2671\}
&3h&2h&2h\\
7,\ K\equiv2
&>3h&2h&2h\\
7,\ K\equiv4
&3h&2h&>2h\\
2671
&3h&>2h&2h
\end{array}}
\tag{9.1}
\]

其中 fixed `2671` 行使用 `2671≠7`，所以 `Xi_PD` 与 `Xi_perp` 都仍是 exact baseline。

这张表说明：

\[
\boxed{
\text{任何 genuine deep target 至多只有一个 orthogonal natural direction能超过 baseline。}}
\tag{9.2}
\]

moving sector三个方向全部 exact；fixed `7` 的两个 roots分别把 extra depth送入 `Xi_PD` 或 `Xi_perp`；fixed `2671` 只把 extra depth送入 `Xi_parallel`。

---

## 10. 当前 frontier

fixed exceptions现在已经被统一为同一个 decimal norm plane：

\[
55\Xi_{PD}R_3
=\Xi_{\parallel}^2+6\Xi_\perp^2.
\]

所以后续不再需要分别把 `7`、`2671` 当成孤立 resultant accident。真正剩余的是：

1. `p=7,K=2` 时 `Xi_parallel` 与 `Xi_perp` 两个 exact-baseline squares为何能在 (8.2) 中继续 cancellation；
2. `p=7,K=4` 时 orthogonal extra-depth `Xi_perp` 的 normalized cancellation；
3. `p=2671` 时 parallel extra-depth `Xi_parallel` 与 canonical full tail `Lambda_tail` 的关系；
4. moving `p∉{7,2671}` 时三方向全部 exact，因此所有 excess仍只能留在 `Lambda_tail` / residual companion sector。

A2 仍为 `待证`。

# A2 equal-depth tropical balance 的 fully-decimal identity

> **依赖：** `spontaneous-height-equal-depth-tropical-balance.md`、`spontaneous-height-equal-depth-tail-reader.md`、`spontaneous-height-equal-depth-decimal-pair.md`、`source-discriminant.md`。
>
> **严格状态：**此前 tropical law仍通过 source Bezout中的 `B_W,z,f,D,g omega,L_JB` 证明。本文把三项全部乘回真实 decimal plane。定义 `B_dec=b_3^2(5K^2-36K+55)+T^2Q^2K^2`，它在 genuine target 上精确读取 `h+r_B`；随后把 source Bezout 改写成只含 `E_+`,`B_dec`,`Lambda_dec`, `alpha/beta/Delta` 等真实整数的 exact identity。该 identity 的三项深度精确为 `2h+r_B,3h,2h+rho_p`，所以 tropical minimum law与所有 tie sectors现在完全 source-free。本文只自然化 tie cancellation，不排除 tie 本身，因此不关闭 A2。

---

## 1. source ratios 的 decimal realizations

沿用

\[
\alpha=TK+a_3,
\qquad
\beta=TQ+b_3,
\qquad
\Delta=Kb_3-Qa_3.
\]

令

\[
c:=E_M\omega=\frac{\Delta}{N}.
\]

已有

\[
\boxed{cD=\beta,\qquad cR_+=E_+.}
\tag{1.1}
\]

`source-discriminant.md` 与 full-tail reader给

\[
\boxed{b_3z=Tc_uQ,}
\tag{1.2}
\]

\[
\boxed{b_3(g\omega)=c_u\beta.}
\tag{1.3}
\]

写

\[
A_H:=g\omega,
\qquad
f=A_H+c_u.
\]

由 (1.3)：

\[
b_3f
=b_3A_H+b_3c_u
=c_u(\beta+b_3).
\]
而

\[
\beta+b_3=TQ+2b_3.
\]
所以定义

\[
\boxed{F_{\rm dec}:=TQ+2b_3}
\tag{1.4}
\]
后有

\[
\boxed{b_3f=c_uF_{\rm dec}.}
\tag{1.5}
\]

在 genuine target prime上 `p∤b_3c_uf`，因此

\[
\boxed{p\nmid F_{\rm dec}.}
\tag{1.6}
\]

---

## 2. `B_W` 的 pure-decimal exact reader

沿用

\[
F_H(K):=5K^2-36K+55.
\]

source height companion为

\[
B_W=c_u^2F_H(K)+z^2K^2.
\tag{2.1}
\]

定义完全由真实 decimal quantities组成的正整数

\[
\boxed{
B_{\rm dec}
:=b_3^2F_H(K)+T^2Q^2K^2.}
\tag{2.2}
\]

由 (1.2)：

\[
b_3^2z^2=c_u^2T^2Q^2.
\]
因此

\[
\boxed{
b_3^2B_W=c_u^2B_{\rm dec}.}
\tag{2.3}
\]

当前 genuine target 与 `b_3c_u` 分离，所以若

\[
v_p(B_W)=h+r_B,
\]
则

\[
\boxed{v_p(B_{\rm dec})=h+r_B.}
\tag{2.4}
\]

这给 `r_B` 一个不再含 source quotient 的 exact natural reader。

---

## 3. full tail 的 decimal reader

沿用

\[
\boxed{
\Lambda_{\rm dec}
=2\beta\Delta+TQ^2\alpha.}
\tag{3.1}
\]

full-tail 文件已证明

\[
\boxed{
b_3cL_{JB}=c_u\Lambda_{\rm dec},}
\tag{3.2}
\]

以及 equal-depth target上

\[
\boxed{v_p(\Lambda_{\rm dec})=2h+\rho_p.}
\tag{3.3}
\]

---

## 4. source Bezout 的 complete decimalization

原 exact Bezout 为

\[
\boxed{
c_u^2fR_+
=DfB_W-DzA_H^2K^2+Kc_u^2L_{JB}.}
\tag{4.1}
\]

现在逐项使用 §§1--3。

由

\[
D=\beta/c,
\qquad
R_+=E_+/c,
\]

\[
f=c_uF_{\rm dec}/b_3,
\qquad
z=c_uTQ/b_3,
\]

\[
A_H=c_u\beta/b_3,
\]

\[
B_W=c_u^2B_{\rm dec}/b_3^2,
\qquad
L_{JB}=c_u\Lambda_{\rm dec}/(b_3c),
\]
代入 (4.1)。乘去共同 denominator并约掉 `c_u^3`，得到：

\[
\boxed{
 b_3^2F_{\rm dec}E_+
 =
 \beta F_{\rm dec}B_{\rm dec}
 -\beta^3TQK^2
 +Kb_3^2\Lambda_{\rm dec}.}
\tag{4.2}
\]

所有量均为原 decimal/prefix 整数；source variables

\[
D,z,f,c_u,g\omega,L_{JB},B_W
\]
已全部从最终 identity中消失。

---

## 5. four exact depth readers in one equation

固定 genuine deep equal-depth target：

\[
v_p(\omega)=v_p(W_q)=h,
\]

\[
v_p(B_W)=h+r_B,
\qquad
v_p(L_{JB})=h+\rho_p,
\]
并定义

\[
r_+=v_p(E_+)-2h.
\]

已有

\[
\boxed{v_p(\beta)=h,}
\tag{5.1}
\]

\[
\boxed{v_p(B_{\rm dec})=h+r_B,}
\tag{5.2}
\]

\[
\boxed{v_p(\Lambda_{\rm dec})=2h+\rho_p,}
\tag{5.3}
\]

\[
\boxed{v_p(E_+)=2h+r_+.}
\tag{5.4}
\]

而 genuine separation给

\[
p\nmid b_3F_{\rm dec}TQK.
\tag{5.5}
\]

因此 (4.2) 的 LHS 与三个 RHS terms赋值精确为

\[
\boxed{
\begin{array}{c|c}
\text{term}&p\text{-depth}\\ \hline
b_3^2F_{\rm dec}E_+&2h+r_+\\
\beta F_{\rm dec}B_{\rm dec}&2h+r_B\\
-\beta^3TQK^2&3h\\
Kb_3^2\Lambda_{\rm dec}&2h+\rho_p.
\end{array}}
\tag{5.6}

提出共同 `p^{2h}` 后，整个 tropical ledger就是四个 natural integers的 residual depth equation：

\[
\boxed{r_+\quad\leftrightarrow\quad r_B,\ h,\ \rho_p.}
\tag{5.7}

---

## 6. fully-decimal tropical law

由 (5.6)，令

\[
m_*:=\min\{r_B,h,\rho_p\}.
\]

立刻重新得到

\[
\boxed{r_+\ge m_*.}
\tag{6.1}
\]

若 minimum 唯一，则 RHS有唯一最浅 natural term，因此

\[
\boxed{r_+=m_*.}
\tag{6.2}
\]

若

\[
r_+>m_*,
\]
则至少两个 RHS natural terms必须在 depth `2h+m_*` 上发生 normalized cancellation。

所以此前 source-level tropical law现在可以完全改写为：

\[
\boxed{
\text{extra }E_+\text{ depth只可能来自 }
\beta B_{\rm dec},\ \beta^3,\ \Lambda_{\rm dec}
\text{ 三个 decimal channels的 minimum tie}.}
\tag{6.3}

---

## 7. the three pair-tie normalized equations

(4.2) 还给后续 tie audit一个 canonical starting point。只记录 strict-extra 所需的 first normalized congruence；不在本文宣称它们矛盾。

### `r_B=h<rho_p`

第一、第二 RHS terms同深，tail term更深。若 `r_+>h`，则

\[
\boxed{
\beta_0F_{\rm dec}B_0
\equiv
\beta_0^3TQK^2
\pmod p,}
\tag{7.1}
\]
其中

\[
\beta_0:=\beta/p^h,
\qquad
B_0:=B_{\rm dec}/p^{2h}.
\]

即

\[
\boxed{
F_{\rm dec}B_0
\equiv
\beta_0^2TQK^2
\pmod p.}
\tag{7.2}
\]

### `r_B=\rho_p<h`

square-content term更深。若 `r_+>r_B`，则

\[
\boxed{
\beta_0F_{\rm dec}B_0
+Kb_3^2\Lambda_0
\equiv0\pmod p,}
\tag{7.3}
\]
其中

\[
B_0:=B_{\rm dec}/p^{h+r_B},
\qquad
\Lambda_0:=\Lambda_{\rm dec}/p^{2h+\rho_p}.
\]

### `h=\rho_p<r_B`

`B_dec` term更深。若 `r_+>h`，则

\[
\boxed{
-\beta_0^3TQK^2
+Kb_3^2\Lambda_0
\equiv0\pmod p.}
\tag{7.4}

即

\[
\boxed{
b_3^2\Lambda_0
\equiv
\beta_0^3TQK
\pmod p.}
\tag{7.5}

triple tie

\[
r_B=h=\rho_p
\]
则三项同时保留。

这些 congruences 是下一层真正值得审计的 normalized unit conditions；如果其中某条被证明只是已有 exact identity的投影，应明确降级，而不能重复计作 obstruction。

---

## 8. current tie frontier

现在 equal-depth resonance的所有 depth变量都有 canonical decimal readers：

\[
\boxed{
\begin{array}{c|c}
\text{depth}&\text{reader}\\ \hline
h&\beta\text{ 或 }\Delta\\
r_B&B_{\rm dec}\\
\rho_p&\Lambda_{\rm dec}\text{ / }\Lambda_{\rm tail}\\
r_+&E_+.
\end{array}}
\tag{8.1}

因此后续不必再回到 projective source units追 `R_+` cancellation。唯一剩余的 unbounded local mechanism就是 §§7 的 pair/triple minimum ties。

A2 仍为 `待证`。

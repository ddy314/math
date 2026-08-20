# A2 descendant-only external depth 的 shorter linear-remainder carrier

> **依赖：** `spontaneous-crt-descendant-projective-depth-reader.md`、`spontaneous-crt-descendant-projective-integer.md`。
>
> **严格状态：**projective depth theorem用 resultant integer `P_63` 读取完整 descendant common baseline，但 `P_63` 的 clearing scale为 `R^8Y^8`。本文回到 universal cubic对 branch quadratic的 Euclidean remainder `M_63=A r+B` 本身。清去固定 `5^7 11^7` denominator后，`A#` 在真实 projective box严格为正、`B#` 严格为负；因 `r=1/K` 极小，`M_63` 真实值严格为负。统一清 `u,v` denominator只需 `R^7Y^4`，得到更短 ordinary integer `M_63^int`。它同样读取完整 common baseline，且 `v_2(M_63^int)=8M+7m+33`。取 positive carrier `H_M63=-M_63^int` 后 primitive part总为 `1 mod4`：`m` 偶时 `5 mod8`，`m` 奇时 `1 mod8`。因此 pure external common product若自身为 `3 mod4`，从这个更短 carrier中约去 baseline后仍强迫一份 `3 mod4` tail。本文尚未排除 linear-remainder overdepth，因此不关闭 A2。

---

## 1. integer-normalized projective remainder

沿用 projective Euclidean division

\[
\mathscr E_{\rm proj}
=Q_{63}\mathscr L_{\rm proj}
+M_{63},
\]

\[
\boxed{M_{63}=A(u,v)r+B(u,v),}
\tag{1.1}

其中

\[
r=1/K,
\qquad
u=a_3/(TK),
\qquad
v=Q^2N_0/(B^2K^2).
\]

exact coefficient audit给

\[
\deg_v A=3,
\qquad
\deg_v B=4,
\]

\[
\deg_u A=\deg_u B=7,
\]

且二者 coefficient denominator的共同固定尺度为

\[
\boxed{D_0:=5^7 11^7.}
\tag{1.2}

定义 integer polynomials

\[
\boxed{A^\#:=D_0A,\qquad B^\#:=D_0B.}
\tag{1.3}

它们分别有 `20` 与 `24` 个 monomials。

---

## 2. exact sign on the actual projective box

真实 box仍为

\[
0<u<1/1000,
\qquad
937/1000<v<939/1000.
\]

对 `A#`,`B#` 分别做 exact rational tensor-Bernstein audit，得到

\[
\boxed{
\frac{186871147561988154254304}{15625}
<A^\#
<
\frac{5744925543296429255273134446887094}
{476837158203125}.}
\tag{2.1}

特别地

\[
\boxed{A^\#>0.}
\tag{2.2}

对 `B#`：

\[
\boxed{
-\frac{82743358059276934923729}{1953125}
<B^\#
<
-\frac{18219304842663055778170041164244}
{476837158203125}<0.}
\tag{2.3}

这里右端是离零最近的 upper bound。

而实际 `K>9*10^11`，本文甚至只用极弱的

\[
K>1000.
\]

两端 exact difference为

\[
\boxed{
-\sup B^\#-\frac{\sup A^\#}{1000}
=
\frac{6237189649683313261448453358678453}
{238418579101562500}>0.}
\tag{2.4}

因此

\[
\boxed{
\frac{A^\#}{K}+B^\#<0.}
\tag{2.5}

即 normalized linear remainder在整个真实 dangerous endpoint严格为负。

---

## 3. clear only the necessary denominators

继续记

\[
R:=TK,
\qquad
X:=Q^2N_0,
\qquad
Y:=B^2K^2.
\]

由于 `deg_u<=7, deg_v<=4`，定义 ordinary integer

\[
\boxed{
\begin{aligned}
\mathscr M_{63}^{\rm int}
:=R^7Y^4\Bigl[&
A^\#(a_3/R,X/Y)\\
&+K B^\#(a_3/R,X/Y)
\Bigr].
\end{aligned}}
\tag{3.1}

它只有 `20+24` 个 composite input terms，清分母尺度仅为

\[
R^7Y^4,
\]
明显短于 projective resultant reader的 `R^8Y^8`。

由 (1.1),(1.3)：

\[
\boxed{
\mathscr M_{63}^{\rm int}
=D_0 K R^7Y^4\,M_{63}.}
\tag{3.2}

在 genuine external sector，`D_0 KRY` 全为 p-units，所以

\[
\boxed{
v_p(\mathscr M_{63}^{\rm int})=v_p(M_{63}).}
\tag{3.3}

前一 depth theorem已有 `v_p(M_63)>=k_p`，故

\[
\boxed{v_p(\mathscr M_{63}^{\rm int})\ge k_p.}
\tag{3.4}

由 (2.5) 与 positive clearing：

\[
\boxed{\mathscr M_{63}^{\rm int}<0.}
\tag{3.5}

定义 positive carrier

\[
\boxed{H_{M63}:=-\mathscr M_{63}^{\rm int}>0.}
\tag{3.6}

---

## 4. exact binary ledger

已有

\[
v_2(a_3)=0,
\qquad
v_2(R)=m+1,
\]

\[
v_2(X)=2M+2,
\qquad
v_2(Y)=2M+2m+2t+2.
\]

对 `A#` monomial `a_ij u^i v^j`，(3.1) 中相应 term depth为

\[
v_2(a_{ij})+(7-i)(m+1)+j(2M+2)+(4-j)(2M+2m+2t+2).
\]

`B#` monomial还多一个 `K`，所以再加 `1`。

抽出公共

\[
7(m+1)+4(2M+2),
\]
后，extra depths分别为

\[
\epsilon^A_{ij}
=v_2(a_{ij})-i(m+1)+(4-j)(2m+2t),
\tag{4.1}

\[
\epsilon^B_{ij}
=v_2(b_{ij})+1-i(m+1)+(4-j)(2m+2t).
\tag{4.2}

checker验证所有 support上的 `m,t` slopes非负，所以最小值在 `(m,t)=(5,3)` 读取。

唯一 minimum来自 `K B#` 的

\[
(i,j)=(0,4)
\]
项，其 coefficient为

\[
\boxed{
b_{0,4}
=2^{17}3^{12}5^3 11^3 13.}
\tag{4.3}

它给

\[
\boxed{\epsilon^B_{0,4}=18.}
\tag{4.4}

第二浅层已经是 `21`，所以不存在 first-layer cancellation。

因此

\[
\boxed{
 v_2(\mathscr M_{63}^{\rm int})
=7(m+1)+4(2M+2)+18
=8M+7m+33.}
\tag{4.5}

---

## 5. signed and positive primitive orientations

除去 (4.5) 后只剩 dominant `(0,4)` term。记

\[
k_0:=K/2\quad\text{odd}.
\]

有

\[
R/2^{m+1}=5^m k_0.
\]

因此 signed primitive unit为

\[
\begin{aligned}
\frac{\mathscr M_{63}^{\rm int}}{2^{8M+7m+33}}
&\equiv
\frac{b_{0,4}}{2^{17}}
\,k_0\,(5^m k_0)^7
\left(\frac X{2^{2M+2}}\right)^4\\
&\equiv3\cdot5^m\pmod8,
\end{aligned}
\tag{5.1}

因为 `k_0^8≡1`、odd fourth power也为 `1 mod8`。

所以

\[
\boxed{
\frac{\mathscr M_{63}^{\rm int}}{2^{8M+7m+33}}
\equiv
\begin{cases}
3\pmod8,&m\text{ even},\\
7\pmod8,&m\text{ odd}.
\end{cases}}
\tag{5.2}

但正 carrier为相反数。定义

\[
\boxed{
H_{M63}^\circ
:=\frac{H_{M63}}{2^{8M+7m+33}}.}
\tag{5.3}

则

\[
\boxed{
H_{M63}^\circ
\equiv
\begin{cases}
5\pmod8,&m\text{ even},\\
1\pmod8,&m\text{ odd}.
\end{cases}}
\tag{5.4}

特别地无条件

\[
\boxed{H_{M63}^\circ\equiv1\pmod4.}
\tag{5.5}

---

## 6. full common baseline and parity tail

定义 genuine descendant-only external baseline product

\[
G_\Delta^{\rm pure}
=\prod p^{k_p}.
\]

由 (3.4)：

\[
\boxed{G_\Delta^{\rm pure}\mid H_{M63}^\circ.}
\tag{6.1}

若该 pure external common product承担 odd parity：

\[
G_\Delta^{\rm pure}\equiv3\pmod4,
\]
则 (5.5) 强迫

\[
\boxed{
\frac{H_{M63}^\circ}{G_\Delta^{\rm pure}}
\equiv3\pmod4.}
\tag{6.2}

所以从更短的 linear-remainder carrier中也会产生一份 baseline之外的 odd-inert tail。

同一 prime若想再次承担该 tail，就必须满足

\[
\boxed{v_p(M_{63})>k_p.}
\tag{6.3}

因此下一步无需继续使用更大的 `P_63`：generic same-prime recycling的最短 target已经变成 linear remainder的 overdepth。

---

## 7. updated frontier

new external ledger现在有两层 reader：

- `P_63`：resultant reader，结构最 canonical；
- `H_M63`：linear-remainder reader，scale更短，完整读取同一 baseline。

`H_M63^circ≡1 mod4` 意味着 common product若为 `3 mod4`，必留下另一份 odd tail。故 generic closure可以进一步集中为：

\[
\boxed{v_p(M_{63})>k_p}
\]
的 same-prime overdepth是否可能无限发生。

A2 仍为 `待证`。

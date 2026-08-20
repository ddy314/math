# A2 descendant projective Euclidean quotient gate 的 parity charge 与 overdepth split

> **依赖：** `spontaneous-crt-descendant-linear-depth-reader.md`、`spontaneous-crt-descendant-projective-depth-reader.md`。
>
> **严格状态：**generic same-prime recycling 现在只需理解 linear remainder `M_63=E_proj-Q_63 L_proj` 是否比 common baseline 更深。本文先隔离 Euclidean quotient `Q_63`：清去固定 `5^7 11^7` denominator后得到 degree-6、50项的 integer projective polynomial `Q#`，它在真实 `(r,u,v)` box严格为正。清回 decimal blocks得到 positive ordinary integer `Q_63^int`，完整二进 depth为 `6M+6m+29`，primitive unit恒为 `3 mod8`。因此 quotient-singular prime并非免费 exception；该 gate自身携带 odd-inert parity。另一方面 valuation split说明 `p|Q_63` 本身不会制造 baseline-level cancellation：若 `v_p(Q_63)>0`，linear remainder overdepth必先要求 upstream `E_proj` 已 overdeep。于是 generic closure可继续集中到 upstream transported-error resonance。本文仍未排除该 resonance，因此不关闭 A2。

---

## 1. projective Euclidean quotient

沿用 exact division

\[
\boxed{
\mathscr E_{\rm proj}
=\mathscr Q_{63}\mathscr L_{\rm proj}
+\mathscr M_{63}.}
\tag{1.1}

其中

\[
\mathscr L_{\rm proj}
=55r^2+18(u-1)r+1-4u-v,
\]

\[
\mathscr M_{63}=A(u,v)r+B(u,v).
\]

Euclidean quotient满足

\[
\boxed{
\deg_r\mathscr Q_{63}=6,
\quad
\deg_u\mathscr Q_{63}=6,
\quad
\deg_v\mathscr Q_{63}=3,}
\tag{1.2}

\[
\boxed{
\deg_{\rm total}\mathscr Q_{63}=6,
\qquad
\#\operatorname{supp}(\mathscr Q_{63})=50.}
\tag{1.3}

全部 rational coefficient的共同 denominator仍恰为

\[
\boxed{D_0=5^7 11^7.}
\tag{1.4}

定义 integer projective quotient

\[
\boxed{
\mathscr Q_{63}^\#:=D_0\mathscr Q_{63}
\in\mathbf Z[r,u,v].}
\tag{1.5}

---

## 2. exact positivity on the real endpoint box

实际变量满足更强窗口，但本文只使用宽松 rational box

\[
\boxed{
0<r<\frac1{1000},
\qquad
0<u<\frac1{1000},
\qquad
\frac{937}{1000}<v<\frac{939}{1000}.}
\tag{2.1}

把 `Q#` 仿射搬到 unit cube，并转成 tensor Bernstein basis。其 bidegrees为 `(6,6,3)`，所以共有

\[
7\cdot7\cdot4=196
\]
个 exact rational Bernstein coefficients。checker验证全部严格为正，且

\[
\boxed{
\min b_{ijk}
=
\frac{10423408247410155008672}{15625}>0,}
\tag{2.2}

\[
\boxed{
\max b_{ijk}
=
\frac{10299944552027210611196952289529}
{15258789062500}.}
\tag{2.3}

因此真实 dangerous endpoint上

\[
\boxed{\mathscr Q_{63}^\#>0.}
\tag{2.4}

---

## 3. clear to an ordinary integer

继续用

\[
R:=TK,
\qquad
X:=Q^2N_0,
\qquad
Y:=B^2K^2,
\]
并注意

\[
r=1/K=T/R,
\qquad
u=a_3/R,
\qquad
v=X/Y.
\]

因为 `deg_(r,u)<=6`、`deg_v<=3`，定义 compact ordinary integer

\[
\boxed{
\mathscr Q_{63}^{\rm int}
:=R^6Y^3
\mathscr Q_{63}^\#(T/R,a_3/R,X/Y).}
\tag{3.1}

它仍只有50个 composite monomials。由 (2.4) 及 `R,Y>0`：

\[
\boxed{\mathscr Q_{63}^{\rm int}>0.}
\tag{3.2}

对 genuine external prime `p\nmid5\cdot11RY`：

\[
\boxed{
v_p(\mathscr Q_{63}^{\rm int})
=v_p(\mathscr Q_{63}).}
\tag{3.3}

所以 quotient-singular support也有 canonical ordinary integer reader。

---

## 4. exact 2-adic depth

若 `Q#` 中 monomial为

\[
q_{abj}r^au^bv^j,
\]
则清回 (3.1) 后对应

\[
q_{abj}T^a a_3^bR^{6-a-b}X^jY^{3-j}.
\]

已有

\[
v_2(T)=m,
\quad
v_2(a_3)=0,
\quad
v_2(R)=m+1,
\]

\[
v_2(X)=2M+2,
\quad
v_2(Y)=2M+2m+2t+2.
\]

checker对全部50项审计。唯一最低项为

\[
\boxed{(a,b,j)=(0,0,3),}
\tag{4.1}

其 coefficient为

\[
\boxed{
q_{003}
=150659459039232000
=2^{17}3^{12}5^3 11^3 13.}
\tag{4.2}

对应 depth

\[
17+6(m+1)+3(2M+2)
=6M+6m+29.
\]

所有其它项相对该层的 `m,t` slopes均非负；在最小 `(m,t)=(5,3)` 已至少再深3层。因此

\[
\boxed{
v_2(\mathscr Q_{63}^{\rm int})
=6M+6m+29.}
\tag{4.3}

---

## 5. positive primitive orientation is `3 mod 8`

除去完整二进 content，模8只剩 (4.1) 项：

\[
\frac{\mathscr Q_{63}^{\rm int}}
{2^{6M+6m+29}}
\equiv
\frac{q_{003}}{2^{17}}
\left(\frac R{2^{m+1}}\right)^6
\left(\frac X{2^{2M+2}}\right)^3
\pmod8.
\]

第一 factor满足

\[
q_{003}/2^{17}\equiv3\pmod8.
\]

又 `R/2^(m+1)` 为 odd，故六次幂为 `1 mod8`。同时

\[
X/2^{2M+2}=Q_0^2N_0.
\]

`Q_0` 为 odd，所以 `Q_0^2≡1 mod8`；而 `A=a_2` 为 odd、`B/2` 被4整除，故

\[
N_0=(9B/2)^2+A^2\equiv1\pmod8.
\]

因此

\[
\boxed{
\mathscr Q_{63}^{\rm int}/2^{6M+6m+29}
\equiv3\pmod8.}
\tag{5.1}

结合 (3.2)，这是 positive primitive `3 mod8` carrier。故 quotient-singular gate自身必带一份 odd-inert parity。

---

## 6. quotient valuation does not create baseline cancellation by itself

固定 descendant-only common prime，记

\[
k=k_p,
\quad
q=v_p(\mathscr Q_{63}),
\quad
\ell=v_p(\mathscr L_{\rm proj}),
\]

\[
e=v_p(\mathscr E_{\rm proj}),
\quad
\mu=v_p(\mathscr M_{63}).
\]

已有

\[
\ell,e,\mu\ge k.
\]

由 exact division (1.1)：

\[
\mathscr M_{63}
=\mathscr E_{\rm proj}
-\mathscr Q_{63}\mathscr L_{\rm proj}.
\tag{6.1}

### `q>0`

此时

\[
q+\ell>k.
\]

若 `e=k`，两项 depth不同，故

\[
\boxed{\mu=k.}
\tag{6.2}

所以

\[
\boxed{q>0,\ \mu>k\Longrightarrow e>k.}
\tag{6.3}

quotient singularity本身不会制造 baseline overdepth；它只能伴随 upstream `E_proj` 已 overdeep。

### `q=0`

若

\[
e\ne\ell,
\]
则两项 depth不同：

\[
\boxed{\mu=\min(e,\ell).}
\tag{6.4}

因此 `mu>k` 只可能来自：

1. `min(e,ell)>k`；或
2. `e=ell=k`，并发生 normalized cancellation
   \[
   \boxed{
   E_0\equiv Q_0L_0\pmod p.}
   \tag{6.5}
   \]

这里 `E=p^kE_0`、`L=p^kL_0`、`Q=Q_0`，三者 normalized units。

---

## 7. revised overdepth frontier

same-prime linear-tail recycling现在只有三类输入：

1. upstream transported error本身已 overdeep：`e>k`；
2. generic unit-quotient equal-depth resonance (6.5)；
3. quotient-singular gate `p|Q_63`，但该 gate自身由 positive primitive `3 mod8` integer收费，而且仍需 `e>k` 才能让 `M_63` overdeep。

所以 quotient factor已经从“潜在第三种自由 cancellation source”降成一个带独立 parity surcharge的显式 gate。下一步应直接分析 `e=v_p(E_proj)>k` 的 transported-error条件。

A2 仍为 `待证`。

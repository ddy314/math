# DD `q-Z` two-sheet 的 reader collapse 与 balanced payer theorem

> **依赖：** [`high-funnel-qz-two-sheet-split.md`](high-funnel-qz-two-sheet-split.md)、
> `core.md` 的 primitive determinant ladder / overlap parameterization / carrier-circle
> eliminant。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
>
> 上一文件把未由 `gamma` square-root baseline 支付的 `D_{qZ}=gcd(q,Z)`
> excess 分成 gap / complementary 两个 sheets。本文继续证明：
>
> 1. `E_exc` 只是 sphere-gap quotient `a` 的同一 p-adic reader；
> 2. bottom carrier excess只是 prefix concat gcd `(A_12,Q)` 的同一 reader；
> 3. 因而真正 canonical sheet selector 是 `a / A_12`，不是 `E / Delta_12`；
> 4. 得到 balanced payer
>    \[
>    \boxed{D_{qZ}^2\mid\gamma\,a\,(A_{12},Q)\,Z_0;}
>    \]
> 5. `q-Z` prime本身恰好就是 carrier-circle eliminant 的单侧 moving-factor
>    ramification prime，因此直接套 two-residual eliminant不会产生独立高度收益。

---

## 1. 记号

沿用上一文件：

\[
D_{qZ}=(q,Z),
\qquad
D_{qZ}=D_{\rm base}D_{\rm ex},
\]

\[
D_{\rm gap}=(D_{\rm ex},E_{\rm exc}),
\qquad
D_{\rm comp}=D_{\rm ex}/D_{\rm gap},
\]

其中

\[
E_{\rm exc}=\frac{E}{(E,Q)},
\qquad
\Theta_{12}=\frac{\Delta_{12}}{(b_1,b_2)}.
\]

对任意

\[
p^e\Vert D_{\rm ex},\qquad e>0,
\]

上一文件已经证明 denominator pattern 必为

\[
e_1=e_2=M<e_3=r=M+c,
\qquad c>0,
\qquad e\le c,
\]

且 sphere只有 gap / complementary 两个 signs。

---

## 2. `a` 与 `A_12` 才是 primary sheet selectors

### 2.1 gap sheet

上一文件有

\[
p^e\mid A_{12}10^{n_3}+2a_3.
\]

因为 `p|b_3` 且 `(a_3,b_3)=1`：

\[
p\nmid a_3.
\]

所以模 `p`：

\[
A_{12}10^{n_3}\equiv-2a_3\not\equiv0.
\]

于是

\[
\boxed{v_p(A_{12})=0.}
\tag{2.1}

同时 gap factor满足

\[
v_p(H_{\rm sph}-y_3)\ge2c.
\]

对 `p\nmid10`，`L` 是 p-unit；由

\[
H_{\rm sph}-y_3=La
\]

得到

\[
\boxed{v_p(a)\ge2c\ge2e.}
\tag{2.2}

### 2.2 complementary sheet

这里

\[
p^e\mid A_{12},
\]

而

\[
v_p(H_{\rm sph}-y_3)=0.
\]

仍因 `p\nmid L`：

\[
\boxed{v_p(a)=0.}
\tag{2.3}

所以对 `D_ex` support，两个 primary readers严格互斥：

\[
\boxed{
\begin{array}{c|cc}
&v_p(a)&v_p(A_{12})\\ \hline
\text{gap}&\ge2e&0\\
\text{complementary}&0&\ge e
\end{array}}
\tag{Primary-sheets}

于是完全整数化地：

\[
\boxed{
D_{\rm gap}=(D_{\rm ex},a),
\qquad
D_{\rm comp}=(D_{\rm ex},A_{12}).}
\tag{2.4}

特别地

\[
\boxed{D_{\rm ex}\mid aA_{12},}
\tag{2.5}

\[
\boxed{(D_{\rm ex},a,A_{12})=1.}
\tag{2.6}

这才是 `q-Z` excess 的 canonical source/prefix two-sheet split。

---

## 3. gap sheet 的 `E_exc` 完全塌回 `a`

`core.md` 的 primitive determinant ladder定义

\[
D_{\rm sph}:=(H_{\rm sph},q_{\rm lcm}),
\qquad
C_{\rm concat}:=(\alpha,\beta),
\]

\[
E'=E/C_{\rm concat},
\]

并有 exact identity

\[
\boxed{D_{\rm sph}E'=\tau a.}
\tag{3.1}

固定 `p|D_ex`。第三分母在 p 处 unique maximum，故 `y_3` 与
`H_sph` 都是 p-units；因此

\[
v_p(D_{\rm sph})=0.
\tag{3.2}

上一文件 §4 已同时证明完整 numerator concat `alpha` 为 p-unit，而完整
`beta` 具有 depth `r`，所以

\[
v_p(C_{\rm concat})=0.
\tag{3.3}

又 `p\nmid10`，故

\[
v_p(\tau)=v_p(b_3)=r.
\tag{3.4}

由 `(3.1)`：

\[
\boxed{v_p(E)=r+v_p(a).}
\tag{3.5}

由于 `v_p(Q)=r`：

\[
\boxed{v_p(E_{\rm exc})=v_p(a).}
\tag{E-a-same-reader}

所以在 `D_ex` support上：

\[
\boxed{(D_{\rm ex},E_{\rm exc})=(D_{\rm ex},a).}
\tag{3.6}

上一文件中“gap sheet 的 E 变深”并不是第二份 carrier obstruction；它只是
primitive determinant ladder 对同一个 sphere gap `a` 的重读。

---

## 4. complementary sheet 的 bottom depth塌回 prefix concat gcd

定义

\[
\boxed{C_{12}:=(A_{12},Q).}
\tag{4.1}

complementary sheet中

\[
p^e\mid A_{12}
\]

且 `p^e|D_ex|q|Q`，所以

\[
\boxed{p^e\mid C_{12}.}
\tag{4.2}

而 gap sheet中 `A_12` 是 p-unit，因此

\[
\boxed{v_p(C_{12})=0.}
\tag{4.3}

故

\[
\boxed{
D_{\rm comp}=(D_{\rm ex},C_{12}).}
\tag{4.4}

另一方面 exact bottom identities为

\[
\frac{\Delta_{12}}{10^d}
=Qa_1 10^{s_2}-b_1A_{12},
\tag{4.5}

\[
\frac{-10^{m_2}\Delta_{12}}{10^d}
=Qa_2-b_2A_{12}.
\tag{4.6}

所以普通 gcd `C_12` 自动满足

\[
\boxed{C_{12}\mid\Delta_{12}/10^d.}
\tag{4.7}

因此 complementary sheet 的 bottom-carrier excess本质上是 prefix concat
numerator/denominator common factor的 determinant reader；它同样不是凭空出现的第二个
independent source。

---

## 5. balanced payer theorem

上一文件已证明：

\[
D_{\rm base}^2\mid\gamma,
\]

\[
D_{\rm gap}^2\mid a,
\]

以及 complementary sheet 上

\[
D_{\rm comp}\mid Z_0.
\]

本文又有

\[
D_{\rm comp}\mid C_{12}.
\]

所以

\[
\boxed{D_{\rm comp}^2\mid C_{12}Z_0.}
\tag{5.1}

逐 prime exponent 相加得到新的全局 balanced payer：

\[
\boxed{
D_{qZ}^{\,2}
\mid
\gamma\,a\,C_{12}\,Z_0.}
\tag{qZ-balanced-payer}

即

\[
\boxed{
D_{qZ}^{\,2}
\mid
\gamma\,a\,(A_{12},Q)\,Z_0.}
\tag{5.2}

因此

\[
\boxed{
\log_{10}D_{qZ}
\le
\frac12\left(
\log_{10}\gamma
+\log_{10}a
+\log_{10}C_{12}
+\log_{10}Z_0
\right).}
\tag{5.3}

在 d-dominant funnel中

\[
n_1+n_2=S+s_1+s_2\le S+2,
\]

所以

\[
A_{12}<10^{S+2},
\qquad Q<10^S,
\]

特别地

\[
\boxed{C_{12}<10^S.}
\tag{5.4}

这使 `(5.3)` 比单纯使用未知 `Z_0^2` 更适合后续 height optimization。

还可用 complementary sheet 的 bottom reader得到另一版本：

\[
\boxed{
D_{qZ}^{\,2}
\mid
\gamma\,a\,C_{12}\,|\Theta_{12}|,}
\tag{5.5}

因为 gap primes由 `a` 支付两份，而 complementary primes分别由
`C_12` 与 `Theta_12` 各支付一份。

---

## 6. balanced sharpened `L_Z` height

已有

\[
L_Z=
\frac{2^{H+2}5^TZ}
{(2^{H+2}5^TZ,q)}
\mid F_-.
\]

记

\[
a_2=\log_{10}2,
\qquad a_5=\log_{10}5.
\]

利用 `(5.3)`：

\[
\boxed{
\begin{aligned}
\log_{10}F_-
\ge{}&a_2H+a_5T+\log_{10}Z
-a_2\mathfrak q-a_5q_5\\
&-\frac12\log_{10}\gamma
-\frac12\log_{10}a
-\frac12\log_{10}C_{12}
-\frac12\log_{10}Z_0
+O(1).
\end{aligned}}
\tag{LZ-balanced-height}

并且可粗化

\[
-\frac12\log C_{12}\ge-\frac12S+O(1).
\]

这是一条新的可用于 LP / stability 重算的严格输入。

---

## 7. 为什么 carrier-circle eliminant 对 `q-Z` prime天然 ramified

`core.md` 的 overlap parameterization写成

\[
\eta=(Q,\tau),
\qquad Q=\eta Q_1,
\qquad \tau=\eta v,
\]

并有

\[
\boxed{u=LQ_1.}
\tag{7.1}

在 `t_2=1` S-unit phase：

\[
u=2\cdot5^TU,
\qquad v=V.
\]

所以两个 normalized moving factors精确为

\[
\boxed{
LQ_1+2v
=u+2v
=2^{H+1}Z,}
\tag{7.2}

\[
\boxed{
LQ_1+v
=u+v
=5^TU+2^HZ.}
\tag{7.3}

固定 `p|D_qZ`。因为 `p|Z` 且 `p\nmid U`：

\[
\boxed{v_p(LQ_1+v)=0,}
\tag{7.4}

\[
\boxed{v_p(LQ_1+2v)=v_p(Z).}
\tag{7.5}

而无 `E_D` circle eliminant 的 normalized moving part正包含

\[
(LQ_1+v)^2(LQ_1+2v)^2.
\]

所以它在 `q-Z` support上自动携带

\[
\boxed{2v_p(Z)}
\tag{7.6}

的单侧 ramification depth。

因此即使额外构造出两条 residual 的共同 `p^h` contact，`h<=...+v_p(Xi)`
中的 moving-factor term也已经可以直接由同一个 `Z` 支付。换言之：

\[
\boxed{
\text{raw carrier-circle eliminant 对 `q-Z` primes 是结构性饱和的。}}
\tag{Circle-qZ-nogo}

这和上一文件证明的“两个 carrier readers本来就不会自动同时深”相互独立；
两点共同说明继续沿 raw circle resultant磨 `q-Z` gcd不会得到新的线性高度。

---

## 8. 新的真实 frontier

`q-Z` bottleneck现在被压成：

\[
\boxed{
D_{\rm ex}
\rightsquigarrow
\begin{cases}
D_{\rm gap}:& D_{\rm gap}^2\mid a,\\
D_{\rm comp}:& D_{\rm comp}\mid C_{12},\ Z_0,\ \Theta_{12},
\end{cases}}
\]

并且两 sheets 在 prime support上互斥。

其中：

- gap 的 `E_exc` 已证明只是 `a` 的重复 reader；
- complementary 的 bottom carrier已证明至少包含 prefix concat gcd `C_12` 的重复 reader；
- raw carrier-circle eliminant又被 `Z` moving factor结构性 ramification饱和。

因此下一步不应再尝试 local same-prime resultant。真正可能产生新高度的接口只剩：

1. 对 `C_12=(A_12,Q)` 建立 prefix-uniform gcd / digit-shell bound；
2. 将 `aZ_0` 用 sphere/projective exact factorization重写，和 scale-free allocation比较；
3. 把 balanced `L_Z` height与 Schmidt / defect-aware stability重新做 LP。

DD 全局仍为 `待证`。
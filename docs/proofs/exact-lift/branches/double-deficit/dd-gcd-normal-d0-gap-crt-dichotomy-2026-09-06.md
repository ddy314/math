# DD gcd-normal `d_0` source-gap CRT 与 large-gap multiplicative dichotomy

> 日期：2026-09-06
>
> 依赖：[`good-genuine-ledger.md`](good-genuine-ledger.md) 中 `gcd-normal-exact-small-factor`、[`tail-allocation-ledger.md`](tail-allocation-ledger.md) 中 `tail-rough-d0-allocation` / `tail-rough-cq-excess`、[`dd-corrected-hard-source-split-2026-08-22.md`](dd-corrected-hard-source-split-2026-08-22.md)。
>
> **严格状态：已严格完成（整个 DD gcd-normal tail；local source sharpening 对 odd non-decimal `d_0` support）。**
>
> 本文不使用 unified discriminant root、不使用 suspended `General-transfer-local`，也不使用 canonical `t_2=1`。核心是把 gcd-normal tail recovery 与 DD gap exact identity直接联立。得到两个此前未显式利用的结果：
>
> 1. reduced denominator core `v` **全局整除 sphere height** `H_sph`；
> 2. gap quotient `a` 同时被两个互素 moduli `d_0` 与 `v` 读取。
>
> 因而 `a` 要么是 modulo `d_0v` 的 ordinary exact CRT lift，要么 `a>=d_0v` 并强迫
>
> \[
> \boxed{F_->Q^2v^3,}
> \]
>
> 比 universal `F_->Qv^2` 多一整份 `Qv`。
>
> 此外，`d_0`-reader 在 odd source prime上做 coefficient stripping后留下的 local modulus exponent为
>
> \[
> \boxed{r_p^{(d_0)}=(c-t-(j-E)_+)_+,}
> \]
>
> 比此前 `C_Q` Euclidean modulus `(c-max(E,j)-t)_+` 恰好恢复了 prefix-common depth `E`。在 corrected split 上，这个新 modulus自动覆盖全部 `X_N X_H` residual。

---

## 1. gcd-normal exact data

写

\[
\kappa=\gamma u,
\qquad
G=\gamma v,
\qquad
(u,v)=1,
\]

并令

\[
d_0=(u,Q),
\qquad
u=d_0L,
\qquad
Q=d_0q,
\qquad
(L,q)=1.
\tag{1.1}
\]

这里使用 `gcd-normal-exact-small-factor` 已证明的 exact identification：其旧记号 `r` 就是 DD tail normalization 的 `L`。同时

\[
\boxed{\tau=vq,}
\tag{1.2}
\]

\[
\boxed{(d_0,v)=1,\qquad(L,v)=1.}
\tag{1.3}
\]

令

\[
\omega:=(10^m,b_3)=10^m/L,
\]

以及

\[
c_3:=q_{\rm lcm}/b_3.
\]

由 tail recovery

\[
b_3=v\omega q,
\]

故

\[
\boxed{q_{\rm lcm}=v\omega q c_3.}
\tag{1.4}
\]

注意 `omega` 是 `{2,5}`-smooth，但一般**不是**纯 `10` 次幂。后续 decimal phase shifting只能抽取其中的完整 `10`-power `10^{v_{10}(omega)}`；剩余 one-sided `2`/`5` factor必须保留在 coefficient 中。

---

## 2. source-gap exact identity直接给 `v | H_sph`

DD gap exact identity为

\[
\boxed{
\mathcal M=q_{\rm lcm}A_{12}10^d
=QH_{\rm sph}+\tau a.
}
\tag{2.1}
\]

代入 `(1.1)--(1.4)`：

\[
v\omega q c_3A_{12}10^d
=d_0qH_{\rm sph}+vqa.
\]

约去正整数 `q`：

\[
\boxed{
v\omega c_3A_{12}10^d
=d_0H_{\rm sph}+va.
}
\tag{2.2}
\]

右边说明

\[
v\mid d_0H_{\rm sph}.
\]

由 `(d_0,v)=1`：

\[
\boxed{v\mid H_{\rm sph}.}
\tag{v-H}
\]

定义

\[
\boxed{H_{\rm sph}=vH_0,\qquad H_0\in\mathbf Z_{>0}.}
\tag{2.3}
\]

把 `(2.3)` 代回 `(2.2)` 并约去 `v`：

\[
\boxed{
\omega c_3A_{12}10^d
=a+d_0H_0.
}
\tag{D0-parent}
\]

因此得到第一个 source residue：

\[
\boxed{
 a\equiv \omega c_3A_{12}10^d\pmod{d_0}.
}
\tag{D0-residue}
\]

---

## 3. sphere gap给互素 `v`-residue

因为

\[
y_3=a_3\frac{q_{\rm lcm}}{b_3}=a_3c_3,
\]

而 DD gap normalization为

\[
H_{\rm sph}-y_3=La,
\]

结合 `H_sph=vH_0`：

\[
\boxed{
vH_0=a_3c_3+La.}
\tag{V-parent}
\]

模 `v`：

\[
\boxed{La\equiv-a_3c_3\pmod v.}
\tag{V-residue}
\]

由 `(L,v)=1`：

\[
\boxed{
a\equiv-a_3c_3L^{-1}\pmod v.}
\tag{V-residue-unit}
\]

又 `(d_0,v)=1`，所以 `(D0-residue)` 与 `(V-residue-unit)` 由 CRT 唯一确定一个

\[
\boxed{\rho_a\in[0,d_0v)}
\tag{3.1}
\]

满足

\[
\boxed{a\equiv\rho_a\pmod{d_0v}.}
\tag{Gap-CRT}
\]

这是两个**不同 coprime moduli** 对同一个 gap quotient 的 exact global reconstruction；本文不把它们当两份 p-adic height payer，只使用其 CRT location。

---

## 4. small-gap / large-gap 二分

### 4.1 small-gap branch

若

\[
\boxed{0<a<d_0v,}
\tag{4.1}
\]

则 `(Gap-CRT)` 立即升级成 ordinary exact lift：

\[
\boxed{a=\rho_a.}
\tag{Gap-CRT-lock}
\]

特别地，若 computed residue `rho_a=0`，则与 `a>0` 矛盾，该 fiber为空。

### 4.2 large-gap branch

若

\[
\boxed{a\ge d_0v,}
\tag{4.2}
\]

exact small-factor normalization为

\[
\boxed{
F_-=L(u+2v)\,a\frac{g_*}{v},
\qquad \frac{g_*}{v}\in\mathbf Z_{>0}.
}
\tag{4.3}
\]

由 `u=d_0L`、`a>=d_0v`：

\[
F_-
\ge L(u+2v)d_0v
=uv(u+2v)
>u^2v.
\tag{4.4}
\]

而 gcd-normal tail window给

\[
\boxed{Q<u/v\le10Q,}
\tag{4.5}
\]

所以 `u>Qv`。代入 `(4.4)`：

\[
\boxed{F_->Q^2v^3.}
\tag{Large-gap-Fminus}
\]

这严格强于 universal multiplicative lower

\[
F_->Qv^2.
\]

---

## 5. large-gap height consequence

由 decimal lengths

\[
Q\ge10^{S-1},
\qquad
G\ge10^{S-2},
\]

且

\[
v=G/\gamma,
\]

记

\[
\Gamma:=\frac{\log_{10}\gamma}{S}.
\]

则 `(Large-gap-Fminus)` 给

\[
\boxed{
\frac{\log_{10}F_-}{S}
\ge5-3\Gamma-o(1).
}
\tag{5.1}
\]

与 d-dominant Archimedean upper

\[
\log_{10}F_-<4S+2m-n+O(1)
\]

联立：

\[
\boxed{
\frac nS
\le-1+2\frac mS+3\Gamma+o(1).
}
\tag{Large-gap-slope}
\]

旧 universal multiplicative lower只给

\[
\frac nS\le1+2\frac mS+2\Gamma+o(1).
\]

二者目标差为

\[
(-1+2M+3\Gamma)-(1+2M+2\Gamma)=\Gamma-2.
\]

而 `gamma|G`，故 `Gamma<=1+o(1)`。所以在 large-gap branch，本文的新 slope inequality具有至少约一整份 normalized `S` 的严格余量。

---

## 6. odd `d_0` source 的 coefficient-stripped modulus

现在回到 second-Schmidt odd non-decimal support。固定

\[
p\nmid10,
\qquad p\mid d_0.
\]

沿用 `tail-rough-d0-allocation` 的 notation：

\[
E=v_p(b_1)=v_p(b_2),
\quad
j=v_p(b_3),
\quad
c=v_p(C_Q),
\]

其中

\[
C_Q=Q/(b_1,b_2).
\]

并令

\[
t=v_p(A_{12}).
\]

旧 exact ledger给

\[
\boxed{v_p(d_0)=E+c-j,}
\tag{6.1}
\]

以及

\[
\boxed{v_p(c_3)=(E-j)_+.}
\tag{6.2}
\]

因为 `p` 为 non-decimal prime，`omega` 是 p-unit。故 `(D0-parent)` 左侧 coefficient

\[
\omega c_3A_{12}
\]

在 p 处深度为

\[
\boxed{s_p=(E-j)_++t.}
\tag{6.3}
\]

定义 stripping 后的 residual exponent

\[
\boxed{
r_p^{(d_0)}
:=\bigl(v_p(d_0)-s_p\bigr)_+.
}
\tag{6.4}
\]

代入 `(6.1),(6.3)`：

\[
\boxed{
r_p^{(d_0)}
=\bigl(c-t-(j-E)_+\bigr)_+.
}
\tag{D0-local-depth}
\]

若 `r_p^(d0)>0`，则 `s_p<v_p(d_0)`；由 `(D0-parent)` 的 unit `10^d` 可知两边要能相差 `p^{v_p(d0)}`，必有

\[
\boxed{v_p(a)=s_p.}
\tag{6.5}
\]

所以除去 `p^{s_p}` 后确实留下一个 coefficient/right-side 都为 p-unit 的模 `p^{r_p^(d0)}` source residue。

同时

\[
r_p^{(d_0)}\le c,
\]

故全局 modulus

\[
\boxed{
D_{d_0}:=\prod_{p\mid\operatorname{core}_{10}(d_0)}p^{r_p^{(d_0)}}
}
\tag{6.6}
\]

满足

\[
\boxed{D_{d_0}\mid C_Q.}
\tag{6.7}
\]

这点非常重要：虽然 reader源自更大的 `d_0`，stripping 后留下的有效 source modulus仍落回 primitive prefix modulus `C_Q`，所以可以继续合法使用 prefix block folding。

---

## 7. 相比旧 `C_Q` Euclidean modulus精确恢复 `E` 层

旧 Euclidean coefficient stripping在同一 prime给

\[
\boxed{
r_p^{(E)}=(c-\max(E,j)-t)_+.}
\tag{7.1}
\]

而

\[
\max(E,j)=E+(j-E)_+.
\]

所以在取 positive part之前：

\[
\boxed{
 c-t-(j-E)_+
=
\bigl(c-\max(E,j)-t\bigr)+E.
}
\tag{7.2}
\]

因此

\[
\boxed{r_p^{(d_0)}\ge r_p^{(E)}.}
\tag{7.3}
\]

新 `d_0` reader恰好把旧 `C_Q` coefficient中被 `q_lcm` denominator maximum吞掉的 prefix-common depth `E` 恢复进 source modulus。

---

## 8. corrected split 中 `D_{d_0}` 覆盖全部 `X_N X_H`

使用 `dd-corrected-hard-source-split` notation。

### 8.1 hard support `h>0`

hard ledger为

\[
\boxed{c=h+2t+n_0+M+j,\qquad M=\max(E,j).}
\tag{8.1}
\]

若 `E>=j`：

\[
r_p^{(d_0)}=c-t
=h+t+n_0+E+j
\ge h+n_0.
\]

若 `j>E`：

\[
\begin{aligned}
r_p^{(d_0)}
&=c-t-(j-E)\\
&=h+t+n_0+j+E\\
&\ge h+n_0.
\end{aligned}
\]

所以所有 hard source + hard prefix-norm exponent都进入 `D_d0`。

### 8.2 soft prefix-norm support `e_N>0,h=0`

corrected split定义本身给

\[
e_B=t,
\qquad e_a=\alpha,
\]

以及

\[
x=t+\alpha+e_N+e_3.
\tag{8.2}
\]

若 `j>E`，由 source-excess identity

\[
c=x+j+E
\]

得到

\[
\begin{aligned}
r_p^{(d_0)}
&=c-t-(j-E)\\
&=\alpha+e_N+e_3+2E\\
&\ge e_N.
\end{aligned}
\]

若 `E>=j`，则 `e_3=0` 且

\[
c=x+2j,
\]

故

\[
\begin{aligned}
r_p^{(d_0)}
&=c-t\\
&=\alpha+e_N+2j\\
&\ge e_N.
\end{aligned}
\]

因此全局严格有

\[
\boxed{X_NX_H\mid D_{d_0}.}
\tag{D0-covers-NH}
\]

这是相对旧 Euclidean modulus的主要结构升级：不再留下 `X_{N,D}|(b_1,b_2)` 的 denominator-common escape。

---

## 9. decimal circular normalization 的正确边界

因为 `D_d0|C_Q`，在 `D_d0` 上 primitive prefix relation

\[
u_1 10^{m_2}\equiv-u_2
\]

仍可用于 exponent folding，且 `u_1,u_2` 为 target units。

但必须注意：`omega` 只保证 `{2,5}`-smooth，不保证是纯 `10` 次幂。定义

\[
c_{10}^{(d_0)}:=v_{10}(\omega c_3A_{12}),
\qquad
s_{10}^{(d_0)}:=v_{10}(a),
\]

其中

\[
v_{10}(N):=\min(v_2(N),v_5(N)).
\]

只有这两份完整 decimal powers可向 exponent搬移；其余 one-sided smooth part保留在 unit coefficient中。

因此和前一 circular theorem完全相同的离散 interval argument给一个 normalized exponent

\[
\boxed{r_{d_0,\rm circ}\ge0}
\]

满足

\[
\boxed{
r_{d_0,\rm circ}
\le
\max\left(
0,
\left\lfloor
\frac{m_2-c_{10}^{(d_0)}-s_{10}^{(d_0)}}2
\right\rfloor
\right)
\le\frac{m_2}{2}.
}
\tag{D0-circular-range}
\]

并存在 target-unit coefficients `A_d,B_d` 使

\[
\boxed{
D_{d_0}\mid A_d10^{r_{d_0,\rm circ}}-B_d,
\qquad
(A_dB_d,D_{d_0})=1.
}
\tag{D0-circular-reader}
\]

所以若

\[
D_{d_0}>10^{r_{d_0,\rm circ}},
\]

则得到 ordinary exact source-phase lock；若 ordinary criterion失败，则由 `(D0-covers-NH)`：

\[
\boxed{
X_NX_H
\le D_{d_0}
\le10^{r_{d_0,\rm circ}}.
}
\tag{D0-failure}
\]

结合现有 corrected third-gap bootstrap

\[
3\log F_-+\log(X_NX_H)\ge3S-o(S)
\]

得到

\[
\boxed{
\log F_-
\ge S-\frac13r_{d_0,\rm circ}-o(S).
}
\tag{D0-failure-Fminus}
\]

由于 `r_d0,circ<=m2/2<=S/2`，粗化为 `5S/6-o(S)`。这**不取代**前一 `7S/8` circular-failure lower；后者通过保留并再收费 denominator gcd 得到更强的 worst-case constant。本文 d0-reader的主要价值是：

1. source modulus更大；
2. `X_NX_H` 无 denominator-common escape；
3. ordinary-lock branch更容易触发；
4. 和 coprime `v`-residue一起直接控制 gap quotient `a`。

不能把同一 prefix-common `E` 同时当成新 modulus surplus与额外 independent height payer重复收费。

---

## 10. 状态摘要

- **已严格完成：** `v|H_sph`、`D0-parent`、`V-parent`；
- **已严格完成：** coprime `d_0 × v` gap CRT；
- **已严格完成：** `a<d_0v` ordinary gap reconstruction；
- **已严格完成：** `a>=d_0v => F_->Q^2v^3` 与 slope consequence；
- **已严格完成：** odd-source stripped depth `r_p^(d0)=(c-t-(j-E)_+)_+`；
- **已严格完成：** `D_d0|C_Q` 且 `X_NX_H|D_d0`；
- **已严格完成：** decimal circular normalization只移动完整 `10`-powers，`r_d0,circ<=m2/2`；
- **边界：** `D0-failure-Fminus` 的 universal constant弱于现有 `7/8` failure lower，不能重复收费；本 theorem的新增收益集中在 enlarged ordinary modulus 与 gap CRT dichotomy；
- **未证明：** small-gap CRT lift不可能、ordinary d0 circular lock不可能、post-tail 全局 strict gap、DD emptiness。

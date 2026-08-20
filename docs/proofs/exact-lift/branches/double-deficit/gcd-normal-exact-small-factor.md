# DD gcd-normal tail 的 universal exact small-factor normalization

> **依赖：** `core.md` 的 gcd-normal form、tail recovery、§35 exact small-factor factorization、
> 通用恒等式 `F_-Q(kappa+G)=E kappa(kappa+2G)`。
>
> **严格状态：** `已严格完成（整个 DD gcd-normal tail）`。
>
> 此前 `high-funnel-exact-small-factor-normalization.md` 在 canonical `t_2=1`
> S-unit phase中证明了一个 exact factorization。本文证明，其核心其实不依赖
> `t_2=1`：对一般 gcd-normal form
> \[
> \kappa=\gamma u,\qquad G=\gamma v,\qquad(u,v)=1,
> \]
> 令
> \[
> d_0=(u,Q),\qquad u=d_0r,\qquad Q=d_0q,\qquad(r,q)=1,
> \]
> 则
> \[
> \boxed{L=r,\qquad\tau=vq,\qquad\eta=(Q,\tau)=q,}
> \]
> 且 `q|E`。最终
> \[
> \boxed{
> F_-=r(u+2v)R,\qquad
> R=a\frac{g_*}{v}\in\mathbf Z_{>0},
> }
> \]
> 即
> \[
> \boxed{
> F_-=a\frac{g_*}{v}\,r(u+2v).
> }
> \]

---

## 1. gcd-normal form

写

\[
\boxed{
\kappa=\gamma u,\qquad
G=\gamma v,\qquad
(u,v)=1.
}
\tag{1.1}

再令

\[
\boxed{
d_0=(u,Q),}
\qquad
\boxed{u=d_0r,\qquad Q=d_0q,}
\tag{1.2}

则

\[
\boxed{(r,q)=1,\qquad r\mid10^m.}
\tag{1.3}

`core.md` 的 tail recovery为

\[
\boxed{b_3=vt,\qquad ut=10^mQ.}
\tag{1.4}

---

## 2. tail normalization 精确等于 reduced pair

把 `(1.2)` 代入 `(1.4)`：

\[
d_0rt=10^md_0q.
\]

约去 `d_0`：

\[
\boxed{rt=10^mq.}
\tag{2.1}

由 `(r,q)=1` 与 `r|10^m`：

\[
\boxed{
t=\frac{10^m}{r}q.}
\tag{2.2}

又 `(u,v)=1` 且 `r|u`，所以

\[
(r,v)=1.
\]

因此

\[
\begin{aligned}
\omega
&=(10^m,b_3)\\
&=\left(10^m,
 v\frac{10^m}{r}q\right)\\
&=\frac{10^m}{r}(r,vq)\\
&=\frac{10^m}{r}.
\end{aligned}
\]

故 DD tail normalization

\[
L=10^m/\omega,\qquad\tau=b_3/\omega
\]

精确化为

\[
\boxed{L=r,\qquad\tau=vq.}
\tag{Tail-general}

此外 `(u,v)=1` 还给 `(d_0,v)=1`。于是

\[
\eta=(Q,\tau)
=(d_0q,vq)
=q(d_0,v)
=\boxed q.
\tag{2.3}

所以 overlap parameterization 中的 `eta` 正是 gcd-normal reduced source factor `q`。

---

## 3. reduced source factor整除 decimal determinant

DD determinant为

\[
\boxed{E=b_3A_{12}10^d-a_3Q.}
\tag{3.1}

由 `(Tail-general)`：

\[
b_3=\omega vq,\qquad Q=d_0q.
\]

两项都含 `q`，故

\[
\boxed{q\mid E.}
\tag{3.2}

定义

\[
\boxed{E_0:=E/q\in\mathbf Z_{>0}.}
\tag{3.3}

---

## 4. universal identity 的 exact cancellation

通用恒等式为

\[
\boxed{
F_-Q(\kappa+G)=E\kappa(\kappa+2G).
}
\tag{4.1}

代入

\[
Q=d_0q,
\quad
\kappa=\gamma u,
\quad
G=\gamma v,
\quad
u=d_0r,
\quad
E=qE_0:
\]

\[
F_-d_0q\,\gamma(u+v)
=qE_0\,\gamma d_0r\,\gamma(u+2v).
\]

约去 `d_0 q gamma`：

\[
\boxed{
F_-(u+v)=E_0\gamma r(u+2v).
}
\tag{4.2}

因为 `(u,v)=1`：

\[
(u+v,r)=1
\]

（`r|u`），并且

\[
(u+v,u+2v)=(u+v,v)=1.
\]

所以

\[
\boxed{(u+v,r(u+2v))=1.}
\tag{4.3}

由 `(4.2)`：

\[
\boxed{u+v\mid E_0\gamma.}
\tag{4.4}

定义

\[
\boxed{
R:=\frac{E_0\gamma}{u+v}\in\mathbf Z_{>0}.
}
\tag{4.5}

则

\[
\boxed{F_-=r(u+2v)R.}
\tag{4.6}

---

## 5. 与 §35 exact factorization 对齐

`core.md` §35 已有

\[
\boxed{
F_-=a\,g_*
\frac{L(LQ+2\tau)}{\tau}.
}
\tag{5.1}

使用

\[
L=r,\qquad Q=d_0q,\qquad\tau=vq,
\]

有

\[
LQ+2\tau
=rd_0q+2vq
=q(u+2v).
\]

故

\[
\begin{aligned}
F_-
&=a g_*
\frac{r\,q(u+2v)}{vq}\\
&=\boxed{
a\frac{g_*}{v}\,r(u+2v).
}
\end{aligned}
\tag{5.2}

比较 `(4.6)` 与 `(5.2)`：

\[
\boxed{
R=a\frac{g_*}{v}.}
\tag{R-general}

§37 overlap 参数化本来就给

\[
g_*=vc\lambda r_*,
\]

所以

\[
R=ac\lambda r_*
\]

确为正整数。

最终 universal normalization：

\[
\boxed{
F_-=r(u+2v)
\;a\frac{g_*}{v}.
}
\tag{Exact-Fminus-general}

---

## 6. 与 canonical `t_2=1` 文件的关系

在 `t_2=1` S-unit phase中，后续 source notation写

\[
u=2\cdot5^TU,\qquad v=V,\qquad Q=Uq_{\rm src}.
\]

由于 source `q_src` 与本文 reduced `q` 可差一个 `2,5`-smooth gcd，
`high-funnel-exact-small-factor-normalization.md` 专门完成了记号审计并得到

\[
r=\frac{2\cdot5^T}{(2\cdot5^T,q_{\rm src})}.
\]

本文说明那个结果只是 `(Exact-Fminus-general)` 在 canonical S-unit coordinates
中的展开，而不是 `t_2=1` 特有现象。

---

## 7. 对 post-tail branch reoptimization 的接口

第二次 Schmidt tail collapse研究

\[
x=\frac{\kappa+2G}{(\kappa,\kappa+2G)},
\qquad
y=\frac\kappa{(\kappa,\kappa+2G)}.
\]

在 gcd-normal variables 中，令

\[
\delta=(u,u+2v)=(u,2)\in\{1,2\}.
\]

则

\[
\boxed{
x=(u+2v)/\delta,\qquad y=u/\delta.}
\tag{7.1}

而 `(Exact-Fminus-general)` 已经把整个 `u+2v` 与 smooth quotient `r`
放入 small factor `F_-`。

因此第二次 Schmidt 强迫的 rough height

\[
\operatorname{core}_{10}(x)\operatorname{core}_{10}(y)
\]

中，`x`-side rough core已经是 `F_-` 的真实整数因子；剩余困难只在
`y`-side rough core，即 `d_0` 的 non-decimal part如何被其它 payer支付。

这把 post-tail side-branch reoptimization 的真正 bottleneck精确定位为

\[
\boxed{
\operatorname{core}_{10}(d_0),
}

而不是重新逐个处理 `F_-` 的所有 2/5-adic位置。

---

## 8. 状态摘要

- **`已严格完成`**：`Tail-general`、`eta=q`、`q|E`、`R-general`、
  `Exact-Fminus-general`。
- **`结构压缩`**：第二次 Schmidt 的 `x`-side rough core已经自动进入 `F_-`；
  post-tail 旁支只需追 `core_10(d_0)` 的支付。
- **`待证`**：`core_10(d_0)` 的 denominator/overlap allocation；据此重算非
  canonical dominant branches并决定是否能把 `6.215109...` 升级为全 DD explicit limsup。

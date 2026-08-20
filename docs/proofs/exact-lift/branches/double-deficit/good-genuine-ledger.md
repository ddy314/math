# double-deficit Good Genuine Ledger

> 本文件是细粒度研究记录的机械归并账本。各来源的标题、正文和证明状态原样保留；账本中的局部闭合、有限证书或降级路线均不表示该分支或主不存在性命题已经关闭。

## 来源索引

- [`frontier-five-adic-closure.md`](#source-frontier-five-adic-closure)
- [`gcd-normal-exact-small-factor.md`](#source-gcd-normal-exact-small-factor)
- [`genuine-a12-fixed-crt.md`](#source-genuine-a12-fixed-crt)
- [`genuine-a12-second-order-crt.md`](#source-genuine-a12-second-order-crt)
- [`genuine-denominator-cleared-carrier.md`](#source-genuine-denominator-cleared-carrier)
- [`genuine-discriminant-carrier.md`](#source-genuine-discriminant-carrier)
- [`genuine-discriminant-cross-audit.md`](#source-genuine-discriminant-cross-audit)
- [`genuine-elliptic-collapse.md`](#source-genuine-elliptic-collapse)
- [`genuine-full-concat-carrier.md`](#source-genuine-full-concat-carrier)
- [`genuine-full-concat-hensel.md`](#source-genuine-full-concat-hensel)
- [`genuine-large-core-crt.md`](#source-genuine-large-core-crt)
- [`genuine-tail-root-orientation-lock.md`](#source-genuine-tail-root-orientation-lock)
- [`good-axis-normalization.md`](#source-good-axis-normalization)
- [`good-excess-gcd-ladder.md`](#source-good-excess-gcd-ladder)
- [`good-prefix-crt-location-audit.md`](#source-good-prefix-crt-location-audit)
- [`good-prefix-polarization.md`](#source-good-prefix-polarization)
- [`good-radius-excess.md`](#source-good-radius-excess)
- [`good-short-residue-audit.md`](#source-good-short-residue-audit)
- [`mixed-rational-good-extension.md`](#source-mixed-rational-good-extension)
- [`pairmax-fixed-a12-crt.md`](#source-pairmax-fixed-a12-crt)
- [`pure-common-five-squareclass-nogo.md`](#source-pure-common-five-squareclass-nogo)

<a id="source-frontier-five-adic-closure"></a>

> 整合来源：`frontier-five-adic-closure.md`

# DD `6.308883577618...` frontier 的 5-adic tail-root closure

> **依赖：** [`tail-root-decimal-phase-lock.md`](tail-allocation-ledger.md#source-tail-root-decimal-phase-lock) 的 exact `Tail-decimal` congruence、`core.md` §18 的 DD 判别根整除 `W=L Xi`、`global-framework.md` §7 的统一判别根、`notation.md` 的统一 `W` 记号、`frontier.md` 的 5-adic baseline 与 terminal primitive overlap。
>
> **严格状态：** `已严格完成（frontier contradiction）`。本文证明：不存在满足
> \[
> \frac{n_3}{S}\to6.308883577618\ldots
> \]
> 的无界 DD terminal frontier sequence。
>
> 核心只有一个 valuation mismatch。exact tail-root / decimal congruence要求
> \[
> 5^d\mid \mathscr T R_0+\eta g_0U\gamma W.
> \]
> frontier 上第一项的 5-depth只有
> \[
> \frac T2+o(S)=0.936294525872\ldots S+o(S),
> \]
> 而 DD §18 的同一个 unified discriminant root满足 `W=L Xi`，故第二项至少有
> \[
> T+o(S)=1.872589051745\ldots S+o(S)
> \]
> 的 5-depth。两项深度严格不同，所以和的 5-depth等于较小者，无法达到
> \[
> d=3.5S+o(S).
> \]
> 矛盾。
>
> 这关闭的是旧的 extremal asymptotic frontier，不等于 DD 全局空性；它把原先的非有效 `limsup <= 6.308883...` 加强为：若 DD 有无界序列，则其 `limsup` 严格小于该常数，但本文不给出显式新 gap。

---

## 1. 先审计 `W`：DD §18 与 unified discriminant 使用同一个根

`global-framework.md` §7 在三分支统一框架中定义

\[
\boxed{
\kappa\left(
\kappa K_{C,D}-2GD^2\mathcal N_{12}
\right)=W^2
}
\tag{Unified-W}

并称 `W` 为统一判别平方根。

随后 `core.md` 的 DD §18 直接使用同一符号：

\[
\boxed{LJ=W^2,}
\tag{1.1}

并进一步证明

\[
\boxed{W=L\Xi,\qquad J=L\Xi^2,}
\tag{DD-W-div}

其中

\[
\Xi=|\mathcal M-C_0a|\in\mathbf Z.
\]

这里不存在局部的 `W:=...` 重新定义。`notation.md` 的全局统一表同样只登记一个

\[
W=\text{统一判别平方根}.
\]

而这些结构化文件由同一原总稿机械迁移，明确要求保持原公式与符号含义。因此本文后续使用

\[
\boxed{L\mid W}
\tag{1.2}

作用于 `(Unified-W)` 的同一整数根。

> 这一节专门记录符号作用域审计，避免把历史草稿中的同名字母误认为同一对象。当前仓库的 canonical notation 对这里没有歧义。

---

## 2. exact tail-root / decimal congruence

`tail-root-decimal-phase-lock.md` 已从 unified tail-root linearization 与 exact carry得到

\[
\boxed{
\mathscr T R_0
+\eta g_0U\gamma W
\equiv0\pmod{10^d},
}
\tag{Tail-decimal}

其中

\[
\boxed{
\mathscr T
=\frac{\kappa^2(\kappa+2G)}{10^m},
}
\tag{2.1}

\[
\eta\in\{\pm1\},
\]

且 terminal primitive overlap为

\[
\boxed{
\kappa=2\gamma5^TU,
\qquad
G=\gamma V,
\qquad
\kappa+2G=2\gamma X.
}
\tag{2.2}

这里

\[
(UVZ,10)=1,
\qquad
X=2^HZ.
\]

所以特别地

\[
v_5(U)=v_5(V)=v_5(X)=0.
\tag{2.3}

---

## 3. frontier 的 5-adic baseline

frontier 5-adic baseline 已证明第三分母的精确 leading depth

\[
\boxed{
e_3:=v_5(b_3)=m-T+o(S).}
\tag{3.1}

而 DD tail normalization定义

\[
\delta_3=(10^m,b_3),
\qquad
L=10^m/\delta_3.
\]

由于

\[
T/S\to1.872589051745\ldots>0,
\]

有

\[
e_3<m
\]

for sufficiently large frontier，于是

\[
v_5(\delta_3)=e_3.
\]

因此

\[
\boxed{
 v_5(L)
 =m-e_3
 =T+o(S).
}
\tag{L5}

由 `(DD-W-div)`：

\[
\boxed{
v_5(W)\ge T+o(S).}
\tag{W5-lower}

注意这里只需要下界；`Xi` 是否再含额外 5-depth无关紧要。

---

## 4. `mathscr T` 的 5-depth只有 `T/2`

令

\[
g_5:=v_5(\gamma).
\]

由 `(2.2)` 与 `(2.3)`：

\[
\boxed{v_5(\kappa)=T+g_5,}
\tag{4.1}

\[
\boxed{v_5(\kappa+2G)=g_5.}
\tag{4.2}

所以从 `(2.1)`：

\[
\boxed{
v_5(\mathscr T)
=2T-m+3g_5.
}
\tag{4.3}

terminal primitive overlap还有

\[
G=\gamma V.
\]

one-channel frontier中

\[
\log G=S+o(S),
\qquad
\log V=S+o(S),
\]

故

\[
\boxed{\log\gamma=o(S),\qquad g_5=o(S).}
\tag{4.4}

frontier ratio同时满足

\[
\boxed{3T=2m+o(S).}
\tag{4.5}

因此

\[
2T-m=\frac T2+o(S),
\]

最终

\[
\boxed{
v_5(\mathscr T)=\frac T2+o(S).}
\tag{T5}

又

\[
\log R_0=o(S),
\]

所以

\[
\boxed{
v_5(\mathscr T R_0)=\frac T2+o(S).}
\tag{First-depth}

数值上：

\[
\frac{T}{2S}
=0.936294525872\ldots+o(1).
\]

---

## 5. 第二项至少有 `T` 深度

第二项为

\[
\eta g_0U\gamma W.
\]

其中

\[
\log g_0=o(S),
\qquad
v_5(U)=0,
\qquad
g_5=o(S).
\]

由 `(W5-lower)`：

\[
\boxed{
v_5(\eta g_0U\gamma W)
\ge T+o(S).}
\tag{Second-depth}

数值上：

\[
\frac TS
=1.872589051745\ldots+o(1).
\]

因此 `(First-depth)` 与 `(Second-depth)` 有正线性差：

\[
v_5(\eta g_0U\gamma W)
-v_5(\mathscr T R_0)
\ge\frac T2+o(S)>0
\]

for sufficiently large frontier。

---

## 6. 两项 valuation 不等，和只能取较浅深度

对任意 prime `p`，若

\[
v_p(A)\ne v_p(B),
\]

则

\[
v_p(A+B)=\min(v_p(A),v_p(B)).
\]

应用于 `(Tail-decimal)` 的两个 5-adic terms，得到

\[
\boxed{
v_5\left(
\mathscr T R_0+\eta g_0U\gamma W
\right)
=\frac T2+o(S).}
\tag{6.1}

但 `(Tail-decimal)` 要求

\[
5^d\mid
\mathscr T R_0+\eta g_0U\gamma W,
\]

所以必须

\[
d\le\frac T2+o(S).
\tag{6.2}

frontier 却有

\[
\boxed{d=3.5S+o(S),}
\tag{6.3}

而

\[
\boxed{
\frac T2
=0.936294525872\ldots S+o(S).}
\tag{6.4}

显然

\[
3.5>0.936294525872\ldots.
\]

矛盾。

因此：

\[
\boxed{
\text{不存在无界 DD sequence 满足 }
\frac{n_3}{S}\to6.308883577618\ldots.
}
\tag{Frontier-closed}

---

## 7. 对全局 limsup 的严格含义

此前已有依赖经典 Schmidt Subspace Theorem 的非有效结论

\[
\limsup_{\rm DD}\frac{n_3}{S}
\le6.308883577618\ldots.
\]

若存在无界 DD solutions 且其 limsup 恰等于右端，则按 limsup 定义可选取一个子序列满足

\[
\frac{n_3}{S}\to6.308883577618\ldots,
\]

与 `(Frontier-closed)` 矛盾。

所以严格得到：

\[
\boxed{
\text{若 DD solutions 在 }S\text{ 上无界，则 }
\limsup_{\rm DD}\frac{n_3}{S}
<6.308883577618\ldots.
}
\tag{Strict-limsup}

这里的严格 gap **非有效且本文不给出数值 epsilon**。因此不能把它改写成某个未经证明的显式

\[
n_3\le(6.308883577618-\varepsilon)S+C.
\]

若 DD solutions 实际在 `S` 上有界，则当然转入有限问题，但本文也没有给出该绝对界。

---

## 8. 方法边界与下一 frontier

本文关闭了过去数轮工作的 extremal terminal frontier。以下结论需要同时更新：

1. `6.308883577618...` 不再是一个可实现的 asymptotic equality frontier；
2. full-rational / genuine / mixed 在该 equality frontier上的所有 slot / CRT continuation现在应视为**对假想极限结构的结构定理与 no-go 记录**，而非当前最外层开放 frontier；
3. `pairmax-fixed-a12-crt.md` 的 universal fixed-fiber uniqueness仍然严格成立在该假想 frontier假设下，但由于 frontier本身已被排除，它主要保留为可迁移机制；
4. 下一步不能继续只在 equality frontier内部增加 local lemmas，而应回到 Schmidt upper-bound proof 前一层，寻找能把本次 5-adic mismatch量化为一个邻域排除，从而得到显式改善，或处理新的较低 asymptotic frontier。

---

## 9. 状态摘要

- **`已严格完成（frontier contradiction）`**：`L5`、`W5-lower`、`T5`、two-term 5-adic mismatch、`Frontier-closed`。
- **`已严格完成（非有效严格加强）`**：若 DD 有无界 solutions，则 `limsup n_3/S < 6.308883577618...`。
- **`失效/降级`**：继续把 `6.308883...` equality frontier当作可实现候选层。
- **`待证`**：把 mismatch 扩成定量邻域排除；新的 lower frontier；DD 全局空性或有效绝对高度界。

---

<a id="source-gcd-normal-exact-small-factor"></a>

> 整合来源：`gcd-normal-exact-small-factor.md`

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

---

<a id="source-genuine-a12-fixed-crt"></a>

> 整合来源：`genuine-a12-fixed-crt.md`

# DD genuine-Gaussian 的 W-free fixed `A_12` CRT

> **依赖：** [`genuine-elliptic-collapse.md`](good-genuine-ledger.md#source-genuine-elliptic-collapse)、[`genuine-a12-second-order-crt.md`](good-genuine-ledger.md#source-genuine-a12-second-order-crt)、`frontier.md` 的 exact carry。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。上一文件从 `Psi_G` 直接读取了模 `C_G` 的 `A_12` period，但 coefficient / quotient仍含 discriminant root `W`。本文进一步使用已经证明 sphere-paid 的 W-free carrier
> \[
> \Theta=(\kappa+G)A_c\beta+\mathscr T a_3^2,
> \qquad C_G^2\mid\Theta,
> \]
> 再代入 exact carry。由于 `V=C_G e_G`，平方展开中的 `A_12^2` 项自动含 `C_G^2`，线性项恰含一层 `C_G`。除去一层后得到一个 coefficients 完全独立于 `A_12,a_3,W` 的 fixed linear CRT：
> \[
> 2\mathscr T g_0B10^d e_G\Sigma R_0 A_{12}
> \equiv M_{G,0}\pmod{C_G}.
> \]
>
> 这是真正适合与 `q_c^2` / rational-contact periods 做跨分支 CRT 的 genuine decimal reader。

---

## 1. W-free surviving carrier

沿用

\[
A_c=Qa_2^2b_1^2,
\]

\[
\mathscr T
=\frac{\kappa^2(\kappa+2G)}{10^{m_3}},
\]

以及 orientation-locked genuine main core `C_G`。

`genuine-elliptic-collapse.md` 定义

\[
\boxed{
\Theta
=(\kappa+G)A_c\beta+\mathscr T a_3^2
}
\tag{1.1}

并证明

\[
\boxed{C_G^2\mid\Theta.}
\tag{1.2}

虽然该 square-depth由 sphere carrier支付，仍可用于 decimal-variable extraction。

---

## 2. exact carry 的平方展开

exact carry为

\[
\boxed{
g_0Ua_3
=g_0B10^dVA_{12}-\Sigma R_0.
}
\tag{2.1}

平方得到

\[
\begin{aligned}
g_0^2U^2a_3^2
&=g_0^2B^2 10^{2d}V^2A_{12}^2
-2g_0B10^dV\Sigma R_0A_{12}
+\Sigma^2R_0^2.
\end{aligned}
\tag{2.2}

将 `(2.2)` 代入 `g_0^2U^2 Theta`：

\[
\begin{aligned}
g_0^2U^2\Theta
={}&g_0^2U^2(\kappa+G)A_c\beta
+\mathscr T\Sigma^2R_0^2\\
&-2\mathscr T g_0B10^dV\Sigma R_0A_{12}\\
&+\mathscr T g_0^2B^2 10^{2d}V^2A_{12}^2.
\end{aligned}
\tag{2.3}

定义 constant part

\[
\boxed{
H_{G,0}
:=g_0^2U^2(\kappa+G)A_c\beta
+\mathscr T\Sigma^2R_0^2.
}
\tag{2.4}

注意 `H_{G,0}` 只依赖 denominator/source/prefix-small data 与 `kappa`；它不含

\[
A_{12},\quad a_3,\quad W.
\]

---

## 3. constant part 自动含第一层 `C_G`

写

\[
\boxed{V=C_Ge_G.}
\tag{3.1}

由 `(1.2)`：

\[
C_G^2\mid g_0^2U^2\Theta.
\]

在 `(2.3)` 中：

- linear `A_12` 项含显式 `V`，故至少含一层 `C_G`；
- quadratic `A_12^2` 项含 `V^2`，故至少含两层 `C_G`。

因此模 `C_G` 观察 `(2.3)`，只能剩 constant part；故

\[
\boxed{C_G\mid H_{G,0}.}
\tag{3.2}

定义整数

\[
\boxed{
M_{G,0}
:=\frac{H_{G,0}}{C_G}.
}
\tag{3.3}

---

## 4. 除去第一层后得到 fixed linear `A_12` residue

把 `(2.3)` 除以 `C_G`，使用 `(3.1)`：

\[
\begin{aligned}
\frac{g_0^2U^2\Theta}{C_G}
={}&M_{G,0}
-2\mathscr T g_0B10^d e_G\Sigma R_0A_{12}\\
&+C_G\,\mathscr T g_0^2B^2 10^{2d}e_G^2A_{12}^2.
\end{aligned}
\tag{4.1}

左边仍被 `C_G` 整除，最后一项也显式被 `C_G` 整除。因此模 `C_G` 得到

\[
\boxed{
2\mathscr T g_0B10^d e_G\Sigma R_0A_{12}
\equiv M_{G,0}
\pmod{C_G}.
}
\tag{GCRT-G0}

这就是 W-free fixed genuine CRT。

与上一文件 `(GCRT-G)` 相比，新式的关键改进是：

\[
\boxed{
M_{G,0}\text{ 与 coefficient 都不含 }A_{12},a_3,W.
}
\tag{4.2}

所以它可在固定 denominator/source fiber 中真正作为一个不随待求 prefix 变化的 period 使用。

---

## 5. effective period 精确为 `C_G`

固定

\[
p^h\Vert C_G.
\]

main unit ledger给

\[
p\nmid g_0B10R_0e_G.
\]

还需检查 `mathscr T` 与 `Sigma`。

### 5.1 `mathscr T` 是 target p-unit

`genuine-tail-root-orientation-lock.md` 的 exact identity为

\[
\mathscr T a_3
=\kappa G^2C_{\rm DD}+\eta(\kappa+G)W.
\]

模 `p`：

\[
\mathscr T a_3
\equiv\eta\kappa W\not\equiv0\pmod p,
\]

因为 `a_3,kappa,W` 都是 p-units。因此

\[
\boxed{p\nmid\mathscr T.}
\tag{5.1}

### 5.2 `Sigma` 是 target p-unit

由

\[
V=X-Y\equiv0\pmod p,
\]

且 `X,Y` 为 p-units，

\[
\Sigma=X+Y\equiv2Y\not\equiv0\pmod p
\]

（`p` 为 odd main split prime）。故

\[
\boxed{p\nmid\Sigma.}
\tag{5.2}

综上 `(GCRT-G0)` 的 `A_12` coefficient在每个 main target prime上都是 unit。因此

\[
\boxed{
\text{effective period of `(GCRT-G0)`}
=C_G/10^{o(S)}.
}
\tag{5.3}

---

## 6. 与 sphere-pay no-go 的兼容性

`Theta` 的 `C_G^2` depth 已被 `Sphere-pay-identity` 证明完全由 original sphere carrier支付。

本文没有把它重新解释成一份新的 p-adic height。做的只是：

\[
\boxed{
\text{在同一已知 square-depth内，利用 }V=C_Ge_G
\text{ 把 second layer 读取成 fixed decimal residue。}
}

这和 A2 / full-rational 中“同一 depth 可以作为 CRT period，但不能重复计入 height surplus”完全一致。

---

## 7. 下一步接口

现在 genuine main core提供一个固定 period

\[
C_G,
\]

而 rational-contact core已有 second-order period

\[
E=D_+D_-.
\]

rational/genuine split满足

\[
EC_G=C_L\cdot10^{o(S)}.
\]

因此下一步应证明 partial rational `GCRT+` 在 `E` 未占满 `C_L` 时仍保持 effective period `E`，然后与 `(GCRT-G0)` 合并成 split-independent `C_L` period。

---

## 8. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：W-free carry square expansion、`C_G|H_{G,0}`、fixed `GCRT-G0`、`mathscr T/Sigma` unit audit、effective period `C_G`。
- **`失效/降级`**：把 fixed period `C_G` 当作 sphere carrier之外的新 height obstruction。
- **`待证`**：partial-rational GCRT extension；hybrid full-`C_L` decimal period；unique lift location；DD frontier emptiness。

---

<a id="source-genuine-a12-second-order-crt"></a>

> 整合来源：`genuine-a12-second-order-crt.md`

# DD genuine-Gaussian 的 second-order `A_12` residue

> **依赖：** [`genuine-tail-root-orientation-lock.md`](good-genuine-ledger.md#source-genuine-tail-root-orientation-lock)、[`genuine-full-concat-carrier.md`](good-genuine-ledger.md#source-genuine-full-concat-carrier)、`frontier.md` 的 exact decimal remainder identity。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。前两文件已经证明 genuine main core只有一个 surviving elliptic orientation，并有
> \[
> C_G^2\mid A_c\beta+\eta Wa_3,
> \qquad A_c=Qa_2^2b_1^2.
> \]
> 本文不再尝试把该 square-depth当成独立 height；`genuine-elliptic-collapse.md` 已证明它由 sphere carrier支付。本文改做 **digit extraction**：把 exact carry 中 `a_3` 对 `A_12` 的一次依赖代入，利用 `V` 只贡献一层 `C_G`，从 square-depth quotient 中得到一个有效模 `C_G` 的线性 `A_12` residue。
>
> 这给 genuine branch 一个与 full-rational `GCRT+` 平行的 second-order decimal period。

---

## 1. surviving genuine carrier

orientation lock 后记 genuine main core为

\[
\boxed{C_G=C_{\rm ell}}
\]

（以下均默认删除 `10^{o(S)}` exceptional overlap）。

全局 tail-root sign为

\[
\eta\in\{\pm1\}.
\]

定义

\[
A_c:=Qa_2^2b_1^2.
\]

surviving full-concat carrier为

\[
\boxed{
\Psi_G
:=A_c\beta+\eta Wa_3,
\qquad
C_G^2\mid\Psi_G.
}
\tag{1.1}

main unit ledger给

\[
\boxed{
(C_G,g_0UB10W)=1
}
\tag{1.2}

按 main prime-power理解；`2,5` 与 coefficient overlaps均已进入 exceptional core。

---

## 2. exact decimal carry

沿用

\[
X=2^HZ,
\qquad
Y=5^TU,
\qquad
V=X-Y,
\qquad
\Sigma=X+Y.
\]

frontier decimal remainder文件已经证明

\[
\boxed{
\Sigma R_0
=g_0\bigl(B10^dVA_{12}-Ua_3\bigr).
}
\tag{Carry-exact}

等价地

\[
\boxed{
g_0Ua_3
=g_0B10^dVA_{12}-\Sigma R_0.
}
\tag{2.1}

同时

\[
V=C_Lv_0.
\]

对 genuine main core定义

\[
\boxed{e_G:=\frac{V}{C_G}.}
\tag{2.2}

因为 `C_G` 使用每个 target rational prime的完整 `p^h` main depth，而 `V/C_L=v_0` 与 main core只有 `10^{o(S)}` overlap，所以删除 exceptional core后

\[
\boxed{(C_G,e_G)=1.}
\tag{2.3}

这条 unit condition保证下面的 `A_12` coefficient不会丢失 genuine period。

---

## 3. 把 carry 代入 genuine square carrier

将 `(1.1)` 乘以 `g_0U`：

\[
g_0U\Psi_G
=g_0UA_c\beta+\eta Wg_0Ua_3.
\]

代入 `(2.1)`：

\[
\begin{aligned}
g_0U\Psi_G
&=g_0UA_c\beta
+\eta W\left(
 g_0B10^dVA_{12}-\Sigma R_0
\right)\\
&=\left(
 g_0UA_c\beta-\eta W\Sigma R_0
\right)
+\eta g_0B10^dWVA_{12}.
\end{aligned}
\tag{3.1}

定义 first quotient numerator

\[
\boxed{
H_G
:=g_0UA_c\beta-\eta W\Sigma R_0.
}
\tag{3.2}

于是

\[
\boxed{
g_0U\Psi_G=H_G+\eta g_0B10^dWVA_{12}.}
\tag{3.3}

---

## 4. `H_G` 自动含第一层 `C_G`

由

\[
C_G^2\mid\Psi_G
\]

知左边 `(3.3)` 被 `C_G^2` 整除。

另一方面

\[
V=C_Ge_G,
\]

所以 `(3.3)` 的第二项至少被 `C_G` 整除。因此

\[
\boxed{C_G\mid H_G.}
\tag{4.1}

定义整数

\[
\boxed{
M_G:=\frac{H_G}{C_G}
=\frac{g_0UA_c\beta-\eta W\Sigma R_0}{C_G}.
}
\tag{4.2}

将 `(3.3)` 除以 `C_G`：

\[
\frac{g_0U\Psi_G}{C_G}
=M_G
+\eta g_0B10^dW e_G A_{12}.
\tag{4.3}

左边仍被 `C_G` 整除，因为原 `Psi_G` 有 square depth。因此得到 genuine second-order residue：

\[
\boxed{
\eta g_0B10^dW e_G A_{12}
\equiv-M_G
\pmod{C_G}.
}
\tag{GCRT-G}

这是 exact ordinary-integer congruence。

---

## 5. effective period 正好是 `C_G`

固定 genuine main

\[
p^h\Vert C_G.
\]

main unit ledger与 `(2.3)` 给

\[
p\nmid \eta g_0B10^dW e_G.
\]

因此 `(GCRT-G)` 对 `A_12` 的有效 `p`-period正好是

\[
p^h.
\]

聚合所有 genuine main prime-powers：

\[
\boxed{
\text{effective rational period of `(GCRT-G)`}
=C_G/10^{o(S)}.
}
\tag{5.1}

所以 genuine square-depth的两层在 decimal extraction 中具有清楚分工：

1. 第一层 `C_G` 被 `V=C_G e_G` 自动支付；
2. 第二层留下一个真正作用于 `A_12` 的模 `C_G` linear residue。

注意这只是 **period / counting information**。它不与 `genuine-elliptic-collapse.md` 冲突：后者说明该 depth不是新的独立 p-adic height；本文只是利用同一 depth读取 decimal variable。

---

## 6. 与 full-rational `GCRT+` 的平行性

full-rational rational-contact core `E=D_+D_-` 已有 second-order Gaussian quotient identity，给 `A_12` 一个有效 period

\[
E/10^{o(S)}.
\]

本文给 genuine complement一个平行 period

\[
C_G/10^{o(S)}.
\]

而 terminal rational/genuine split满足

\[
\boxed{
E\,C_G=C_L\cdot10^{o(S)},
\qquad
(E,C_G)=10^{o(S)}.
}
\tag{6.1}

所以两类 second-order decimal readers正好覆盖整个 moving pair-max main core。

下一文件可据此把 partial-rational `GCRT+` 与 `(GCRT-G)` 拼成一个 **split-independent full-`C_L` A_12 period**。

---

## 7. no-double-count 边界

必须区分两件事：

- `genuine-elliptic-collapse.md`：证明 `C_G^2|Psi_G` 的 p-adic depth由 sphere carrier支付，不能再算作一份新的 height surplus；
- 本文：在已存在的 square-depth中读取 `A_12` 的 second-order residue，得到 period `C_G`。

因此本文允许用于：

- CRT uniqueness；
- candidate counting；
- digit-shell location。

但不能把 `C_G` period再当作 sphere carrier之外的额外 modulus height来证明同一局部矛盾。

---

## 8. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`H_G` first-layer divisibility、integer quotient `M_G`、genuine second-order `GCRT-G`、effective period `C_G`。
- **`失效/降级`**：把 `GCRT-G` 当作 sphere square-depth之外的新 p-adic收费。
- **`待证`**：rational/genuine hybrid `C_L`-period CRT；unique lift 的 Archimedean location；DD frontier emptiness。

---

<a id="source-genuine-denominator-cleared-carrier"></a>

> 整合来源：`genuine-denominator-cleared-carrier.md`

# DD genuine-Gaussian cross carrier 的 denominator-cleared digit form

> **依赖：** [`genuine-discriminant-carrier.md`](good-genuine-ledger.md#source-genuine-discriminant-carrier)、[`genuine-discriminant-cross-audit.md`](good-genuine-ledger.md#source-genuine-discriminant-cross-audit)。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文把 ghost-coordinate cross determinants
> \[
> \Omega y_2\pm Wy_3
> \]
> 清回原始 `a_i,b_i`。由于 genuine pair-max prime在 `b2,b3,q` 中的深度分别为 `h,h,h`，原来的 square-depth contact在 denominator-cleared integer 中变成 cube-depth divisibility：
> \[
> C_\sigma^3
> \mid
> Q a_2^2b_1b_3(\kappa+G)\pm W a_3b_2.
> \]
> 其中恰有一份 `C_sigma` 是显式 denominator baseline；除去它后仍保留两份 genuine p-adic cancellation depth。
>
> 本文仍不提供 Archimedean saving；它的用途是把 genuine-Gaussian 下一步对象从 ghost coordinates 改写成原始 digit/denominator integer。

---

## 1. ghost cross determinants

沿用

\[
\Omega=Q(a_2b_1)(\kappa+G),
\]

以及 orientation split

\[
C_G^{\rm main}=C_{\rm same}C_{\rm opp}.
\]

已有

\[
\boxed{
C_{\rm same}^2
\mid
\Theta_{\rm same}
:=\Omega y_2-Wy_3,
}
\tag{1.1}
\]

\[
\boxed{
C_{\rm opp}^2
\mid
\Theta_{\rm opp}
:=\Omega y_2+Wy_3.
}
\tag{1.2}
\]

且

\[
\Theta_{\rm same}\ne0,
\qquad
\Theta_{\rm opp}>0
\]

对 sufficiently large frontier成立。

---

## 2. 清除 ghost denominator

由整数球面提升

\[
y_2=a_2\frac q{b_2},
\qquad
y_3=a_3\frac q{b_3}.
\]

所以 exact 地有

\[
\begin{aligned}
b_2b_3\Theta_{\rm same}
&=b_2b_3\left(
\Omega a_2\frac q{b_2}
-Wa_3\frac q{b_3}
\right)\\
&=q\left(
\Omega a_2b_3-Wa_3b_2
\right),
\end{aligned}
\]

以及

\[
\begin{aligned}
b_2b_3\Theta_{\rm opp}
&=q\left(
\Omega a_2b_3+Wa_3b_2
\right).
\end{aligned}
\]

定义原始整数

\[
\boxed{
\Phi_{\rm same}
:=\Omega a_2b_3-Wa_3b_2,
}
\tag{2.1}
\]

\[
\boxed{
\Phi_{\rm opp}
:=\Omega a_2b_3+Wa_3b_2.
}
\tag{2.2}
\]

则

\[
\boxed{
b_2b_3\Theta_\sigma=q\Phi_\sigma}
\tag{Clear}
\]

对 `sigma=same,opp` 同时成立。

再代入 `Omega`：

\[
\boxed{
\Phi_{\rm same}
=Q a_2^2b_1b_3(\kappa+G)-Wa_3b_2,
}
\tag{Digit-same}
\]

\[
\boxed{
\Phi_{\rm opp}
=Q a_2^2b_1b_3(\kappa+G)+Wa_3b_2.
}
\tag{Digit-opp}
\]

这些量只含原始 numerator/denominator blocks 与统一 global objects，不再含 `y2,y3`。

---

## 3. pair-max valuation bookkeeping

固定

\[
p^h\Vert C_\sigma.
\]

one-channel main prime满足

\[
\boxed{
v_p(b_2)=v_p(b_3)=h,}
\tag{3.1}
\]

并且 `p` 在 `b2,b3` 已达到 lcm 的最大深度，而 `p∤b1`，故

\[
\boxed{v_p(q)=h.}
\tag{3.2}
\]

由前一文件

\[
v_p(\Theta_\sigma)\ge2h.
\]

对 `(Clear)` 取 valuation：

\[
2h+v_p(\Theta_\sigma)
=h+v_p(\Phi_\sigma).
\]

因此

\[
\boxed{
v_p(\Phi_\sigma)\ge3h.}
\tag{3.3}
\]

聚合：

\[
\boxed{
C_{\rm same}^{\,3}\mid\Phi_{\rm same},
\qquad
C_{\rm opp}^{\,3}\mid\Phi_{\rm opp}.
}
\tag{Cube-depth}
\]

这就是 denominator-clearing 带来的 cube-depth form。

---

## 4. 三层中只有一层是显式 denominator baseline

对 `p^h|C_sigma` 写

\[
b_2=p^h b_2^\circ,
\qquad
b_3=p^h b_3^\circ,
\qquad
p\nmid b_2^\circ b_3^\circ.
\]

于是

\[
\Phi_{\rm same}
=p^h\left[
Q a_2^2b_1b_3^\circ(\kappa+G)
-Wa_3b_2^\circ
\right],
\tag{4.1}
\]

\[
\Phi_{\rm opp}
=p^h\left[
Q a_2^2b_1b_3^\circ(\kappa+G)
+Wa_3b_2^\circ
\right].
\tag{4.2}
\]

前一文件的 unit ledger 给

\[
p\nmid Q a_2b_1(\kappa+G)Wa_3,
\]

所以方括号中的两个 summands 都是 p-units。

而 `(3.3)` 说明方括号整体仍满足

\[
\boxed{
p^{2h}\mid[\cdots].}
\tag{4.3}
\]

因此 cube-depth 的结构恰为：

\[
\boxed{
\underbrace{p^h}_{\text{shared denominator baseline}}
\times
\underbrace{p^{2h}}_{\text{genuine unit-unit cancellation}}.
}
\tag{4.4}
\]

所以不能把三份 depth 全部当成新 obstruction；但也不能把 `(Cube-depth)` 说成纯粹由 `b2,b3` baseline 自动产生。扣掉一份后仍有真实 square-depth residue。

---

## 5. orientation-free digit product

由 two sign channels：

\[
C_{\rm same}^3C_{\rm opp}^3
\mid
\Phi_{\rm same}\Phi_{\rm opp}.
\]

故

\[
\boxed{
(C_G^{\rm main})^3
\mid
\bigl[Q a_2^2b_1b_3(\kappa+G)\bigr]^2
-
(Wa_3b_2)^2.
}
\tag{Digit-product}
\]

这是一条完全不需要预先固定 Gaussian orientation 的 original-integer statement。

不过它的 raw Archimedean 高度仍然很大；前一文件的 `9S` transverse ratio 在 denominator clearing 后保持不变。

---

## 6. real-size audit保持不变

两个 digit terms 的比值为

\[
\frac{Q a_2^2b_1b_3(\kappa+G)}{Wa_3b_2}
=\frac{\Omega y_2}{Wy_3},
\]

因为

\[
\frac{b_3a_2}{b_2a_3}
=\frac{y_2}{y_3}.
\]

所以前一文件直接给

\[
\boxed{
\frac{Q a_2^2b_1b_3(\kappa+G)}{Wa_3b_2}
=10^{-9S+o(S)}.
}
\tag{6.1}

因此

\[
\Phi_{\rm same}
=-Wa_3b_2\left(1-10^{-9S+o(S)}\right),
\]

\[
\Phi_{\rm opp}
=Wa_3b_2\left(1+10^{-9S+o(S)}\right).
\]

raw digit integer同样没有 Archimedean cancellation。

---

## 7. genuine branch 的更新目标

经过 denominator clearing，genuine branch 的 square-depth p-adic cancellation已经有一个完全 original-integer 的载体：

\[
\boxed{
C_\sigma^2
\mid
\frac{\Phi_\sigma}{C_\sigma}
}
\]

其中除法为整数，且 target prime上的两个 summands 在抽掉 `C_sigma` baseline 后都是 units。

下一步真正有价值的问题变成：

> `Phi_sigma/C_sigma` 是否存在由 terminal source / decimal structure 强迫的进一步大公共因子，使得除掉它以后剩余 cofactor 的 Archimedean height严格小于 `2 log C_sigma`？

若没有这种 factorization，单靠 cube-depth本身不能关闭 genuine branch。

---

## 8. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`Clear`、`Digit-same/opp`、pair-max `v_p(q)=h`、`Cube-depth`、baseline/cancellation `1+2` depth split、orientation-free `Digit-product`。
- **`失效/降级`**：把 cube-depth 三层全部当成新收费；用 raw `Phi_same/opp` height直接关闭 genuine core。
- **`待证`**：`Phi_sigma/C_sigma` 的 source/digit factorization与 normalized cofactor height；genuine-Gaussian closure；DD 全局空性。

---

<a id="source-genuine-discriminant-carrier"></a>

> 整合来源：`genuine-discriminant-carrier.md`

# DD genuine-Gaussian 的 discriminant square carrier

> **依赖：** [`global-framework.md`](../../global-framework.md) 的统一 `Q,G,N_12,kappa,W` 判别平方；[`frontier.md`](frontier.md) 的 one-channel pair-max reduction 与 genuine-Gaussian branch。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文第一次离开 full-rational `A≡±b` sheet，直接处理 genuine-Gaussian main core。对每个 one-channel pair-max prime-power `p^h`，统一判别平方本身会产生第二个 depth `2h` 的 sum-of-two-squares carrier：
> \[
> p^{2h}\mid W^2+\Omega^2,
> \qquad
> \Omega:=Q(a_2b_1)(\kappa+G).
> \]
> 该 carrier 不使用 rational sign degeneration。进一步与原 pair-max carrier比较 orientation，可把 genuine core 分成 same/opposite 两类，并得到两个 **square-depth rational cross determinants**。
>
> 本文不证明这些 determinants 足够短，因此不关闭 genuine-Gaussian branch；但它把此前“需要新的 Gaussian/projective same-prime elimination”具体化成一个可核验的二 carrier orientation problem。

---

## 1. one-channel genuine main prime 的本原数据

统一前两块对象为

\[
Q=b_1 10^{m_2}+b_2,
\qquad
G=b_1b_2,
\tag{1.1}
\]

\[
\mathcal N_{12}
=(a_1b_2)^2+(a_2b_1)^2.
\tag{1.2}
\]

为避免与 moving core `C_G` 混淆，把 unified DD coefficient 记为

\[
\boxed{
\mathscr C
:=10^{m_2+k_{12}}a_1+10^{d_3}a_2.
}
\tag{1.3}
\]

DD 中

\[
\boxed{
\kappa=\frac{10^{m_3}QG}{b_3}\in\mathbf Z.
}
\tag{1.4}
\]

固定 genuine-Gaussian main prime-power

\[
p^h\Vert C_G^{\rm main}.
\]

one-channel pair-max normalization 删除 all-three/common 与另一 pair channel 的 `o(S)` exceptional core 后，恰有

\[
\boxed{
v_p(b_2)=v_p(b_3)=h,
\qquad p\nmid b_1,
\qquad p\ne2,5.}
\tag{1.5}
\]

由 reducedness：

\[
\boxed{p\nmid a_2a_3.}
\tag{1.6}
\]

于是

\[
Q\equiv b_1 10^{m_2}\not\equiv0\pmod p,
\]

故

\[
\boxed{v_p(Q)=0.}
\tag{1.7}
\]

同时

\[
\boxed{v_p(G)=h.}
\tag{1.8}
\]

由 `(1.2)`：

\[
\mathcal N_{12}
\equiv(a_2b_1)^2\not\equiv0\pmod p,
\]

因此

\[
\boxed{v_p(\mathcal N_{12})=0.}
\tag{1.9}
\]

最后由 `(1.4)`：

\[
v_p(\kappa)
=v_p(G)-v_p(b_3)=h-h=0,
\]

所以

\[
\boxed{p\nmid\kappa(\kappa+2G).}
\tag{1.10}
\]

这组 unit facts 全部不使用 rational contact。

---

## 2. 两个自然平方近似都精确到 `p^(2h)`

定义

\[
x:=a_1b_2,
\qquad
y:=a_2b_1.
\tag{2.1}
\]

则

\[
\mathcal N_{12}=x^2+y^2.
\]

由 `p^h|b_2`：

\[
\boxed{
\mathcal N_{12}\equiv y^2\pmod{p^{2h}}.}
\tag{2.2}
\]

另一方面

\[
\kappa(\kappa+2G)
=\kappa^2+2\kappa G,
\]

而

\[
(\kappa+G)^2
=\kappa^2+2\kappa G+G^2.
\]

由 `p^h|G`：

\[
\boxed{
\kappa(\kappa+2G)
\equiv(\kappa+G)^2
\pmod{p^{2h}}.}
\tag{2.3}
\]

甚至两者乘积的误差也可 exact 展开：

\[
\begin{aligned}
&\mathcal N_{12}\kappa(\kappa+2G)
-y^2(\kappa+G)^2\\
&\qquad=
\boxed{
x^2\kappa(\kappa+2G)-y^2G^2.}
\end{aligned}
\tag{2.4}
\]

右端两项都被 `p^(2h)` 整除，因此

\[
\boxed{
\mathcal N_{12}\kappa(\kappa+2G)
\equiv
(a_2b_1)^2(\kappa+G)^2
\pmod{p^{2h}}.}
\tag{Square-approx}
\]

---

## 3. 判别平方产生新的 depth-`2h` sum-of-two-squares carrier

统一判别平方在 DD (`D=Q`) 中为

\[
W^2
=\kappa\bigl(
\kappa(G^2\mathscr C^2-Q^2\mathcal N_{12})
-2GQ^2\mathcal N_{12}
\bigr).
\]

整理：

\[
\boxed{
W^2
+Q^2\mathcal N_{12}\kappa(\kappa+2G)
=(\kappa G\mathscr C)^2.
}
\tag{Disc-square}
\]

定义全局整数

\[
\boxed{
\Omega
:=Q(a_2b_1)(\kappa+G).
}
\tag{3.1}
\]

由 `(Square-approx)`：

\[
Q^2\mathcal N_{12}\kappa(\kappa+2G)
\equiv\Omega^2\pmod{p^{2h}}.
\]

而 `(1.8)` 给

\[
p^{2h}\mid(\kappa G\mathscr C)^2.
\]

代入 `(Disc-square)`：

\[
\boxed{
p^{2h}\mid W^2+\Omega^2.}
\tag{Disc-carrier-local}
\]

聚合 genuine main prime-powers：

\[
\boxed{
(C_G^{\rm main})^2
\mid W^2+\Omega^2.
}
\tag{Disc-carrier-global}
\]

这里没有出现 `A±b`、`D_±`、`R_±` 或 full-rational cofactor sheet，因此该 carrier genuine branch 也可用。

---

## 4. carrier 在 genuine main core 上是 primitive 的

由 §§1：

\[
p\nmid Q(a_2b_1)(\kappa+G),
\]

所以

\[
\boxed{p\nmid\Omega.}
\tag{4.1}
\]

若 `p|W`，由 `(Disc-carrier-local)` 模 `p` 会得到

\[
\Omega^2\equiv0\pmod p,
\]

矛盾。因此

\[
\boxed{p\nmid W\Omega.}
\tag{4.2}
\]

于是 `-1` 在每个 genuine main prime 上为 quadratic residue；特别地

\[
\boxed{p\equiv1\pmod4.}
\tag{4.3}
\]

更重要的是，`W+iOmega` 的 `p`-norm depth `2h` 不可能同时分给 conjugate 两侧：若 `pi` 与 `bar pi` 都整除 `W+iOmega`，则 `p` 同时整除 `W` 与 `Omega`，与 `(4.2)` 冲突。

因此对每个 `p^h` 存在唯一 orientation（差一个 Gaussian unit）使

\[
\pi_p^{2h}\mid W+i\Omega.
\]

聚合得到一个 oriented Gaussian factor

\[
\boxed{
N(\Pi_{\rm disc})=C_G^{\rm main},
\qquad
\Pi_{\rm disc}^{\,2}\mid W+i\Omega.
}
\tag{Disc-Gaussian}
\]

所以统一判别平方现在自身也是 pair-max orientation 的一个 reader。

---

## 5. 与原 pair-max orientation 比较

原 pair-max core给出另一个 oriented factor

\[
\boxed{
N(\Pi_{\rm sph})=C_G^{\rm main},
\qquad
\Pi_{\rm sph}^{\,2}\mid y_2+i y_3.
}
\tag{Sphere-Gaussian}
\]

对每个 genuine main `p^h`，比较 `Pi_disc` 与 `Pi_sph` 的 local orientation。

定义：

- `same`：两者选择同一个 `pi_p`；
- `opposite`：一个选择 `pi_p`，另一个选择 `bar pi_p`。

相应把 genuine core 分成互素（差 `10^{o(S)}` exceptional overlap）的两个 rational divisors

\[
\boxed{
C_G^{\rm main}=C_{\rm same}C_{\rm opp}.}
\tag{5.1}
\]

---

## 6. same orientation 给 square-depth difference determinant

若 `p^h|C_same`，则

\[
\pi_p^{2h}\mid y_2+i y_3,
\qquad
\pi_p^{2h}\mid W+i\Omega.
\]

考虑 Gaussian linear combination：

\[
\Omega(y_2+i y_3)-y_3(W+i\Omega)
=\Omega y_2-Wy_3.
\]

右边是 rational integer，却被 `pi_p^(2h)` 整除。对 rational integer，`v_pi=v_p`，故

\[
p^{2h}\mid\Omega y_2-Wy_3.
\]

聚合：

\[
\boxed{
C_{\rm same}^{\,2}
\mid
\Theta_{\rm same},
\qquad
\Theta_{\rm same}:=\Omega y_2-Wy_3.
}
\tag{Same-det}
\]

`Theta_same` 可能为零；若为零，则得到 exact slope lock

\[
\boxed{
\frac W\Omega=\frac{y_2}{y_3}.}
\tag{Same-zero}
\]

这需要后续单独审计。

---

## 7. opposite orientation 给 square-depth positive determinant

若 `p^h|C_opp`，取 `Pi_sph` 的 orientation 为 `pi_p`，则 discriminant carrier在同一 `pi_p` 上表现为

\[
\pi_p^{2h}\mid W-i\Omega.
\]

于是

\[
\Omega(y_2+i y_3)+y_3(W-i\Omega)
=\Omega y_2+Wy_3.
\]

故

\[
p^{2h}\mid\Omega y_2+Wy_3.
\]

聚合：

\[
\boxed{
C_{\rm opp}^{\,2}
\mid
\Theta_{\rm opp},
\qquad
\Theta_{\rm opp}:=\Omega y_2+Wy_3.
}
\tag{Opp-det}
\]

所有 terminal quantities 为正，所以

\[
\boxed{\Theta_{\rm opp}>0.}
\tag{7.1}
\]

因此 opposite orientation 不存在 zero-determinant 逃逸；它必须真实支付一个 positive rational integer 的 square-depth divisibility。

---

## 8. orientation-free product form

由 `(Same-det)` 与 `(Opp-det)`：

\[
C_{\rm same}^2C_{\rm opp}^2
\mid
\Theta_{\rm same}\Theta_{\rm opp}.
\]

结合 `(5.1)`：

\[
\boxed{
(C_G^{\rm main})^2
\mid
(\Omega y_2)^2-(Wy_3)^2.
}
\tag{Cross-product}
\]

这条 product form 不需要预先固定每个 prime 的 orientation。

但目前不能仅凭其 Archimedean size关闭 genuine branch：`W,Omega,y_2,y_3` 的 raw heights 很大，普通 capacity bound 仍可能容纳 `2 log C_G`。

因此 `(Cross-product)` 的价值主要是：把 genuine-Gaussian 的同素数问题从抽象“另找一个 Gaussian eliminant”压成两个 explicit rational integers `Theta_same,Theta_opp`。

---

## 9. 当前新的 genuine-Gaussian frontier

现在 genuine branch 至少具有两套 independent-looking Gaussian carriers：

\[
\Pi_{\rm sph}^{\,2}\mid y_2+i y_3,
\]

\[
\Pi_{\rm disc}^{\,2}\mid W+i\Omega,
\qquad
\Omega=Q(a_2b_1)(\kappa+G).
\]

比较 orientations 后：

\[
\boxed{
C_{\rm same}^{\,2}\mid\Omega y_2-Wy_3,
\qquad
C_{\rm opp}^{\,2}\mid\Omega y_2+Wy_3.
}
\tag{9.1}
\]

下一步不应立刻取 norm 再做 generic height sum；应该分别研究：

1. `same` 的 zero case `(Same-zero)` 是否会精确退回已有 projective/source relation；
2. `same` 非零时，`Theta_same` 是否有 hidden small factor / cancellation；
3. `opposite` 中 `Theta_opp>0`，能否在除去 explicit smooth/source factors 后得到严格小于 `2 log C_opp` 的 core height；
4. 若两 determinant 都只是 primitive carrier tetrahedron 的旧 edges，则把该等价关系明确写出并继续寻找真正 global digit carrier。

---

## 10. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：genuine main prime 上 `Q,N_12,kappa,kappa+2G` 为 units；`N_12` 与 `kappa(kappa+2G)` 的 `p^(2h)` natural square approximations；`Disc-carrier-global`；primitive discriminant Gaussian orientation；same/opposite orientation split；`Same-det`、`Opp-det` 与 orientation-free `Cross-product`。
- **`有限证书`**：可用脚本机械检查 `(2.4)`、`Disc-square` 重排和两个 Gaussian cross combinations。
- **`待证`**：`Same-zero` audit；两个 cross determinant 的 normalized core height；genuine-Gaussian closure；DD 全局空性。

---

<a id="source-genuine-discriminant-cross-audit"></a>

> 整合来源：`genuine-discriminant-cross-audit.md`

# DD genuine-Gaussian discriminant cross determinant 的 Archimedean audit

> **依赖：** [`genuine-discriminant-carrier.md`](good-genuine-ledger.md#source-genuine-discriminant-carrier)、[`good-prefix-polarization.md`](good-genuine-ledger.md#source-good-prefix-polarization) 与 [`frontier.md`](frontier.md) 的 terminal constants。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。上一文件给出
> \[
> C_{\rm same}^2\mid\Omega y_2-Wy_3,
> \qquad
> C_{\rm opp}^2\mid\Omega y_2+Wy_3.
> \]
> 本文计算两项的真实 Archimedean 比例。结果是
> \[
> \frac{\Omega y_2}{Wy_3}=10^{-9S+o(S)}.
> \]
> 因而 `same` determinant 对 sufficiently large frontier 永不为零，且 `same/opp` 两个 determinant 都由 `Wy3` 主导，没有任何正线性 Archimedean cancellation。于是“新 discriminant carrier + 原 sphere carrier直接取 raw cross determinant”不能靠高度小性关闭 genuine branch。
>
> 这不否定新 carrier 的 p-adic 信息；它说明下一步必须先从 `Theta_same/Theta_opp` 中抽出 genuinely small source/digit cofactor，不能直接使用 raw determinant 高度。

---

## 1. terminal digit polarization

沿用

\[
S=m_1+m_2.
\]

prefix polarization 已给

\[
\boxed{
(n_1,m_1,n_2,m_2)
=(S,0,0,S)+o(S).
}
\tag{1.1}
\]

因此按 base-10 logarithmic height：

\[
\boxed{
\log a_1=S+o(S),
\qquad
\log b_2=S+o(S),
}
\tag{1.2}
\]

\[
\boxed{
\log a_2=o(S),
\qquad
\log b_1=o(S).
}
\tag{1.3}
\]

这里及下文 `log` 均按 `log_10` 理解；改变固定底数只会整体缩放常数。

由

\[
Q=b_1 10^{m_2}+b_2,
\qquad
G=b_1b_2,
\]

两项均为正，得到

\[
\boxed{
\log Q=S+o(S),
\qquad
\log G=S+o(S).
}
\tag{1.4}

---

## 2. `kappa` 的高度恰为 `2S`

统一 tail weight 满足固定窗口

\[
QG<\kappa\le10QG.
\]

结合 `(1.4)`：

\[
\boxed{
\log\kappa=2S+o(S).
}
\tag{2.1}

而

\[
\frac G\kappa<\frac1Q=10^{-S+o(S)},
\]

所以

\[
\boxed{
\log(\kappa+G)=2S+o(S),
\qquad
\frac{\kappa+G}{\kappa}=1+10^{-S+o(S)}.
}
\tag{2.2}

---

## 3. DD coefficient `mathscr C` 的高度为 `4.5S`

frontier constants 为

\[
\frac{n_3}{S}	o6.308883577618\ldots,
\qquad
\frac{m_3}{S}	o2.808883577618\ldots.
\]

因此

\[
\boxed{d_3=n_3-m_3=3.5S+o(S).}
\tag{3.1}

又由

\[
s_2=n_2-m_2=-S+o(S),
\]

得到

\[
\boxed{k_{12}=s_2+d_3=2.5S+o(S).}
\tag{3.2}

DD unified coefficient 为

\[
\mathscr C
=10^{m_2+k_{12}}a_1+10^{d_3}a_2.
\]

第一项高度：

\[
(m_2+k_{12})+\log a_1
=(S+2.5S+S)+o(S)
=4.5S+o(S).
\]

第二项只有

\[
d_3+\log a_2
=3.5S+o(S).
\]

两项为正，因此不存在 cancellation，且

\[
\boxed{
\log\mathscr C=4.5S+o(S).}
\tag{3.3}

---

## 4. `N_12` 与 discriminant correction 的高度

写

\[
x=a_1b_2,
\qquad
y=a_2b_1.
\]

由 §1：

\[
\log x=2S+o(S),
\qquad
\log y=o(S).
\]

故

\[
\mathcal N_{12}=x^2+y^2
\]

满足

\[
\boxed{
\log\mathcal N_{12}=4S+o(S).
}
\tag{4.1}

定义 discriminant 主平方尺度

\[
M_{\rm disc}:=\kappa G\mathscr C.
\]

由 `(1.4)`、`(2.1)`、`(3.3)`：

\[
\boxed{
\log M_{\rm disc}=7.5S+o(S),
\qquad
\log M_{\rm disc}^2=15S+o(S).
}
\tag{4.2}

而 correction

\[
R_{\rm disc}
:=Q^2\mathcal N_{12}\kappa(\kappa+2G)
\]

满足

\[
\boxed{
\log R_{\rm disc}
=(2+4+2+2)S+o(S)
=10S+o(S).
}
\tag{4.3}

所以

\[
\boxed{
\frac{R_{\rm disc}}{M_{\rm disc}^2}
=10^{-5S+o(S)}.
}
\tag{4.4}

由 exact discriminant identity

\[
W^2=M_{\rm disc}^2-R_{\rm disc},
\]

得到 sufficiently large frontier 上 `W>0`，并且

\[
\boxed{
\frac W{M_{\rm disc}}
=1+O(10^{-5S+o(S)}),
\qquad
\log W=7.5S+o(S).
}
\tag{W-height}

这里第一式的 `O` 只表达实数相对误差的指数尺度；证明来自

\[
\sqrt{1-t}=1+O(t)
\qquad(t\to0^+).
\]

---

## 5. discriminant carrier 的第二坐标只有 `3S`

上一文件定义

\[
\Omega=Q(a_2b_1)(\kappa+G).
\]

由 `(1.3)`、`(1.4)`、`(2.2)`：

\[
\boxed{
\log\Omega=3S+o(S).
}
\tag{5.1}

于是

\[
\boxed{
\log\frac W\Omega=4.5S+o(S).
}
\tag{5.2}

也就是说，在实平面上 `W+iOmega` 极度接近 real axis；其 slope 只有

\[
\frac\Omega W=10^{-4.5S+o(S)}.
\]

---

## 6. sphere carrier 的 slope 恰好朝相反尺度

因为

\[
y_i=a_i\frac q{b_i},
\]

公共 `q` 消去：

\[
\frac{y_2}{y_3}
=\frac{a_2/b_2}{a_3/b_3}.
\tag{6.1}

由 digit lengths：

\[
\log\frac{a_2}{b_2}
=n_2-m_2+O(1)
=-S+o(S),
\]

而

\[
\log\frac{a_3}{b_3}
=n_3-m_3+O(1)
=d_3+O(1)
=3.5S+o(S).
\]

所以

\[
\boxed{
\log\frac{y_2}{y_3}
=-4.5S+o(S).
}
\tag{Sphere-slope}

即原 sphere carrier `y2+i y3` 极度接近 imaginary axis：

\[
\frac{y_2}{y_3}=10^{-4.5S+o(S)}.
\]

---

## 7. cross determinant 中小项比大项低 `9S`

结合 `(5.2)` 与 `(Sphere-slope)`：

\[
\begin{aligned}
\log\frac{\Omega y_2}{W y_3}
&=\log\frac\Omega W+\log\frac{y_2}{y_3}\\
&=-4.5S-4.5S+o(S).
\end{aligned}
\]

因此

\[
\boxed{
\rho_S
:=\frac{\Omega y_2}{W y_3}
=10^{-9S+o(S)}.
}
\tag{Cross-ratio}

特别地 sufficiently large frontier 上

\[
0<\rho_S<1.
\tag{7.1}

于是 same determinant

\[
\Theta_{\rm same}
=\Omega y_2-Wy_3
=-Wy_3(1-\rho_S)
\]

严格非零，并满足

\[
\boxed{
|\Theta_{\rm same}|
=Wy_3\bigl(1-10^{-9S+o(S)}\bigr).
}
\tag{Same-size}

所以前一文件留下的 exact slope escape

\[
\Theta_{\rm same}=0
\]

在 sufficiently large frontier 上完全排除：

\[
\boxed{
\Theta_{\rm same}\ne0.
}
\tag{Same-zero-closed}

同理

\[
\Theta_{\rm opp}
=\Omega y_2+Wy_3
=Wy_3(1+\rho_S),
\]

故

\[
\boxed{
\Theta_{\rm opp}
=Wy_3\bigl(1+10^{-9S+o(S)}\bigr)>0.
}
\tag{Opp-size}

---

## 8. raw cross determinant 没有 Archimedean saving

由 §7：

\[
\boxed{
\log|\Theta_{\rm same}|
=
\log\Theta_{\rm opp}
=
\log W+\log y_3+o(S).
}
\tag{8.1}

而每个 genuine main prime上，由上一文件的 primitive unit facts：

\[
p\nmid W,
\qquad
p\nmid y_3.
\]

第二条因为

\[
y_3=a_3(q/b_3),
\]

且 `p` 在 `b3` 已达到 lcm max depth、`p∤a3`。

因此 `C_G` 的 square-depth divisibility

\[
C_{\rm same}^2\mid\Theta_{\rm same},
\qquad
C_{\rm opp}^2\mid\Theta_{\rm opp}
\]

确实来自两个 p-adic units 的 deep cancellation；但在 Archimedean place，两个 terms 的大小差了 `9S`，完全没有相应 cancellation。

所以：

\[
\boxed{
\text{直接用 raw }\Theta_{\rm same/opp}\text{ 的绝对高度，}
\text{不会产生 genuine core 的 strict small-determinant bound。}
}
\tag{Raw-cross-nogo}

**状态：`失效/降级`，针对 raw determinant height 路线。**

---

## 9. 新 carrier 仍然留下什么

虽然 raw cross determinant 不短，上一文件的新 p-adic结构仍然真实：

\[
C_{\rm same}^2\mid\Theta_{\rm same}\ne0,
\qquad
C_{\rm opp}^2\mid\Theta_{\rm opp}>0.
\]

本文进一步说明这两条 divisibility 都发生在 **Archimedean-transverse** 情形：

\[
\frac{\Omega/W}{y_3/y_2}
=10^{-9S+o(S)}.
\]

因此若要利用它们，下一步只能寻找 `Theta_same/opp` 的 exact factorization / normalized quotient，证明主导的 `Wy3` 部分由已知 source factors抽掉后只剩短 cofactor。

若完整展开再次退回 primitive carrier determinants、projective source quotient或原 discriminant identity，则这个 discriminant carrier也只能作为 orientation reader保留，不能关闭 genuine branch。

---

## 10. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`log Q=log G=S+o(S)`、`log kappa=2S+o(S)`、`log mathscr C=4.5S+o(S)`、`log N12=4S+o(S)`、`log W=7.5S+o(S)`、`log Omega=3S+o(S)`、sphere/discriminant slope asymptotics、`Cross-ratio=10^{-9S+o(S)}`、`Same-zero-closed`。
- **`失效/降级`**：用 raw `Theta_same/Theta_opp` Archimedean height直接关闭 genuine core。
- **`待证`**：两个 cross determinant 的 exact normalized factorization；是否能剥出短 cofactor；genuine-Gaussian closure；DD 全局空性。

---

<a id="source-genuine-elliptic-collapse"></a>

> 整合来源：`genuine-elliptic-collapse.md`

# DD genuine-Gaussian surviving elliptic second lift 的 sphere-pay collapse

> **依赖：** [`genuine-tail-root-orientation-lock.md`](good-genuine-ledger.md#source-genuine-tail-root-orientation-lock)、[`genuine-full-concat-carrier.md`](good-genuine-ledger.md#source-genuine-full-concat-carrier)。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。orientation lock 已证明 genuine main core 只保留一个全局 relative orientation，且其 sign 满足
> \[
> \epsilon_\sigma\eta=+1.
> \]
> 本文继续审计 surviving full-concat square-depth。消去 `W` 后得到 W-free carrier
> \[
> \Theta
> =(\kappa+G)Q(a_2b_1)^2\beta+\mathscr T a_3^2.
> \]
> 随后证明一个 exact identity：`Theta` 的全部 `C_G^2` depth 已由原 pair-max sphere norm 的 `2h` excess 加上显式 denominator baseline支付。因此 discriminant/full-concat second lift在 surviving elliptic class 上不构成第二份独立 obstruction。
>
> 结论：本轮 discriminant carrier 的真正新增信息只有 **global orientation lock**；其 surviving square-depth 是 sphere carrier 的重写。

---

## 1. surviving elliptic sign

沿用全局 tail-root sign

\[
\eta\in\{\pm1\}
\]

以及

\[
\epsilon_{\rm same}=-1,
\qquad
\epsilon_{\rm opp}=+1.
\]

前一文件证明 genuine main primes 必须满足

\[
\boxed{\epsilon_\sigma\eta=+1.}
\tag{1.1}

因此 surviving class 的 sign 实际满足

\[
\boxed{\epsilon_\sigma=\eta.}
\tag{1.2}

以下记其 main core 为

\[
C_{\rm ell}=C_G^{\rm main}\cdot10^{o(S)}.
\]

为了避免与 denominator core 混淆，继续把统一 DD coefficient 写成

\[
C_{\rm DD}=10^{d_3}A_{12}.
\]

---

## 2. 从 full-concat carrier 消去 `W`

定义

\[
y:=a_2b_1,
\qquad
A_c:=Qy^2.
\]

surviving full-concat carrier 为

\[
\boxed{
\Psi_{\rm ell}
=A_c\beta+\eta Wa_3,
\qquad
C_{\rm ell}^2\mid\Psi_{\rm ell}.
}
\tag{2.1}

而 tail-root original identity 为

\[
\boxed{
\mathscr T a_3
=\kappa G^2C_{\rm DD}
+\eta(\kappa+G)W,
}
\tag{2.2}

其中

\[
\mathscr T
=\frac{\kappa^2(\kappa+2G)}{10^{m_3}}.
\]

由 `(2.2)`：

\[
\eta(\kappa+G)W
=\mathscr T a_3-\kappa G^2C_{\rm DD}.
\]

乘 `(2.1)` 以 `kappa+G`：

\[
\begin{aligned}
(\kappa+G)\Psi_{\rm ell}
&=(\kappa+G)A_c\beta
+\eta(\kappa+G)Wa_3\\
&=(\kappa+G)A_c\beta
+\mathscr T a_3^2
-\kappa G^2C_{\rm DD}a_3.
\end{aligned}
\]

定义 W-free integer

\[
\boxed{
\Theta
:=(\kappa+G)A_c\beta
+\mathscr T a_3^2.
}
\tag{Theta-def}

于是有 exact relation

\[
\boxed{
\Theta
=(\kappa+G)\Psi_{\rm ell}
+\kappa G^2C_{\rm DD}a_3.
}
\tag{Theta-from-Psi}

由于

\[
C_{\rm ell}^2\mid\Psi_{\rm ell},
\qquad
C_{\rm ell}^2\mid G^2,
\]

立刻有

\[
\boxed{C_{\rm ell}^2\mid\Theta.}
\tag{2.3}

但这一步还不能说明 `Theta` 是独立 obstruction；下面做 no-double-count 审计。

---

## 3. 定义 original-integer sphere norm carrier

令

\[
\boxed{
\mathcal S_{\rm raw}
:=y^2b_3^2+G^2a_3^2.
}
\tag{3.1}

使用

\[
y=a_2b_1,
\qquad
G=b_1b_2,
\]

可写成

\[
\boxed{
\mathcal S_{\rm raw}
=b_1^2\left[(a_2b_3)^2+(a_3b_2)^2\right].
}
\tag{3.2}

它就是 `(y_2,y_3)` sphere norm 清除 pair-max denominator 后的 original-integer 版本。

固定

\[
p^h\Vert C_{\rm ell}.
\]

写

\[
b_2=p^hb_{2,p},
\qquad
b_3=p^hb_{3,p}.
\]

前一文件的 `(Sphere-normalized)` 给

\[
p^{2h}\mid
a_2^2b_{3,p}^2+a_3^2b_{2,p}^2.
\]

因此 `(3.2)` 给

\[
\boxed{p^{4h}\mid\mathcal S_{\rm raw}.}
\tag{Sphere-raw-4h}

这里前 `2h` 是 `b_2,b_3` shared denominator baseline，后 `2h` 是 pair-max Gaussian square-depth。

---

## 4. `Theta` 与 sphere norm 的 exact identity

记

\[
T_3:=10^{m_3}.
\]

使用

\[
\beta=T_3Q+b_3,
\tag{4.1}
\]

\[
\kappa b_3=T_3QG,
\tag{4.2}
\]

以及

\[
\mathscr T=\frac{\kappa^2(\kappa+2G)}{T_3},
\]

从 `(Theta-def)` 直接展开：

\[
\Theta
=(\kappa+G)Qy^2(T_3Q+b_3)
+\frac{\kappa^2(\kappa+2G)}{T_3}a_3^2.
\tag{4.3}

乘以 `T_3 G^2`，并用 `(4.2)` 消去 `T_3QG`：

\[
\begin{aligned}
T_3G^2\Theta
&=\kappa^2(\kappa+G)^2y^2b_3^2/\kappa
+\kappa^2(\kappa+2G)G^2a_3^2\\
&=\kappa\Bigl[
(\kappa+G)^2y^2b_3^2
+\kappa(\kappa+2G)G^2a_3^2
\Bigr].
\end{aligned}
\]

使用

\[
(\kappa+G)^2
=\kappa(\kappa+2G)+G^2,
\]

得到精确恒等式

\[
\boxed{
T_3G^2\Theta
=\kappa\left[
\kappa(\kappa+2G)\mathcal S_{\rm raw}
+G^2y^2b_3^2
\right].
}
\tag{Sphere-pay-identity}

这是本文的核心 no-double-count identity。

---

## 5. `Theta` 的 `2h` 深度全部由 sphere carrier 支付

固定 `p^h||C_ell`。main ledger 给

\[
p\nmid T_3\kappa y.
\]

同时

\[
v_p(G)=v_p(b_3)=h.
\]

由 `(Sphere-raw-4h)`：

\[
v_p(\mathcal S_{\rm raw})\ge4h.
\]

而第二项显然有

\[
v_p(G^2y^2b_3^2)=4h.
\]

所以 `(Sphere-pay-identity)` 的右端满足

\[
v_p(\text{RHS})\ge4h.
\]

左端的显式 `G^2` 已支付恰好 `2h`：

\[
v_p(T_3G^2\Theta)=2h+v_p(\Theta).
\]

因此仅由 sphere norm 与 denominator baseline 就已经推出

\[
\boxed{v_p(\Theta)\ge2h.}
\tag{Sphere-pays-Theta}

这与 `(2.3)` 完全相同。

所以：

\[
\boxed{
C_{\rm ell}^2\mid\Theta
\text{ 并不是 discriminant/full-concat 提供的第二份独立 square depth；}
\text{它已经被原 sphere square-depth精确支付。}
}
\tag{Elliptic-collapse}

---

## 6. 对 two-layer Hensel 的含义

此前 genuine two-layer ledger 写成

\[
R_\sigma=C_\sigma K_\sigma,
\qquad
v_p(R_\sigma)=h,
\]

以及

\[
C_\sigma\mid K_\sigma+A_c\frac{b_3}{C_\sigma}.
\]

orientation lock 后只剩 `ell` class。

`Theta-from-Psi` 与 `Sphere-pay-identity` 说明：如果试图用 tail-root identity 消去 `K_ell` 中的 `W`，second lift最终会落回 `mathcal S_raw` 的 sphere norm；不会产生一个新的 `<C_ell` natural representative。

因此此前的 closure target

\[
\text{“从 }K_\sigma\text{ 的 source residue 提取独立短代表”}
\]

在当前 discriminant/tail-root algebra 内已经完成审计：

\[
\boxed{
\text{它只能恢复 sphere-paid elliptic depth。}
}
\tag{K-route-nogo}

**状态：`失效/降级`。**

---

## 7. genuine branch 的更新 frontier

经过最近几层：

1. discriminant square carrier存在；
2. raw cross determinant没有 Archimedean saving；
3. denominator-cleared / full-concat carrier存在；
4. two-layer Hensel存在；
5. tail-root linearization把 relative orientation 锁成全局唯一 class；
6. wrong hyperbolic class严格矛盾；
7. surviving elliptic second lift由 sphere square-depth完全支付。

因此同-prime discriminant/tail-root algebra 已经闭合到：

\[
\boxed{
\text{orientation reader only, no independent positive-linear depth.}
}
\]

真正未解决的 genuine-Gaussian 问题重新变得清楚：

> 为什么一个正线性高度的 one-channel pair-max core 能长期由 split primes `p≡1 mod4` 承担，同时满足 denominator/source digit shells？

接下来不应继续从 `W,Omega,K_sigma` 造同素数 eliminant；应转向 **global split-prime / digit-shell distribution**，尤其利用现在已经没有 relative-orientation entropy这一点。

---

## 8. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：W-free `Theta`、`Theta-from-Psi`、original `mathcal S_raw`、`Sphere-pay-identity`、`Sphere-pays-Theta`。
- **`失效/降级`**：orientation lock 后继续从 `K_sigma/W` algebra寻找第二份 square-depth或 short representative；surviving elliptic second lift 已被 sphere carrier支付。
- **`待证`**：global split-prime / digit-shell distribution；genuine-Gaussian closure；DD 全局空性。

---

<a id="source-genuine-full-concat-carrier"></a>

> 整合来源：`genuine-full-concat-carrier.md`

# DD genuine-Gaussian 的 full-concat square-depth carrier

> **依赖：** [`genuine-denominator-cleared-carrier.md`](good-genuine-ledger.md#source-genuine-denominator-cleared-carrier) 与全局 exact lift `q alpha=H beta`。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。上一文件的 cube-depth original-integer carrier在除去一份 shared-denominator baseline 后可进一步精确识别：其中的大 denominator expression
> \[
> 10^{m_3}Q+b_3
> \]
> 正是完整拼接分母 `beta`。因此 genuine branch 得到一个非常简洁的 square-depth full-concat carrier：
> \[
> C_\sigma^2
> \mid
> Q a_2^2b_1^2\beta\pm Wa_3.
> \]
> 这把 genuine same-prime cancellation 直接放到 `(beta,a3)` digit shell 上。再利用 `q alpha=H beta`，同一 carrier可无损推到 `(alpha,a3)` numerator shell。
>
> 本文不证明该 carrier 高度足够小；它完成的是 genuine branch 从 Gaussian ghost orientation 到真实 concatenated integers 的桥接。

---

## 1. denominator-cleared carrier 的进一步因式分解

上一文件定义

\[
\Phi_\sigma
=Q a_2^2b_1b_3(\kappa+G)
\pm Wa_3b_2,
\]

并证明

\[
\boxed{C_\sigma^3\mid\Phi_\sigma}
\tag{1.1}
\]

对 `sigma=same,opp` 成立；其中符号约定为

\[
\Phi_{\rm same}
=Q a_2^2b_1b_3(\kappa+G)-Wa_3b_2,
\]

\[
\Phi_{\rm opp}
=Q a_2^2b_1b_3(\kappa+G)+Wa_3b_2.
\]

利用 DD tail weight

\[
\kappa=\frac{10^{m_3}QG}{b_3},
\qquad
G=b_1b_2,
\]

有

\[
\begin{aligned}
Q a_2^2b_1b_3(\kappa+G)
&=Q a_2^2b_1b_3
\left(
\frac{10^{m_3}Qb_1b_2}{b_3}+b_1b_2
\right)\\
&=Q a_2^2b_1^2b_2
\left(10^{m_3}Q+b_3\right).
\end{aligned}
\tag{1.2}

所以

\[
\boxed{
\Phi_\sigma
=b_2\left[
Q a_2^2b_1^2(10^{m_3}Q+b_3)
\pm Wa_3
\right].
}
\tag{1.3}

---

## 2. 括号中的 denominator quantity 就是 `beta`

完整 denominator concatenation 为

\[
\beta
=b_1 10^{m_2+m_3}+b_2 10^{m_3}+b_3.
\]

而

\[
Q=b_1 10^{m_2}+b_2.
\]

因此 exact 地

\[
\boxed{
\beta=10^{m_3}Q+b_3.
}
\tag{Beta-tail}

把它代入 `(1.3)`，定义

\[
\boxed{
\Psi_{\rm same}
:=Q a_2^2b_1^2\beta-Wa_3,
}
\tag{2.1}

\[
\boxed{
\Psi_{\rm opp}
:=Q a_2^2b_1^2\beta+Wa_3.
}
\tag{2.2}

则得到 exact factorization

\[
\boxed{
\Phi_\sigma=b_2\Psi_\sigma.
}
\tag{Phi-Psi}

---

## 3. cube-depth 减去 denominator baseline 后正好剩 square depth

固定

\[
p^h\Vert C_\sigma.
\]

one-channel main prime满足

\[
v_p(b_2)=h.
\]

由 `(1.1)` 与 `(Phi-Psi)`：

\[
h+v_p(\Psi_\sigma)
=v_p(\Phi_\sigma)
\ge3h.
\]

因此

\[
\boxed{v_p(\Psi_\sigma)\ge2h.}
\tag{3.1}

聚合：

\[
\boxed{
C_{\rm same}^2
\mid
Q a_2^2b_1^2\beta-Wa_3,
}
\tag{Concat-same}

\[
\boxed{
C_{\rm opp}^2
\mid
Q a_2^2b_1^2\beta+Wa_3.
}
\tag{Concat-opp}

这就是 genuine-Gaussian 的 full-denominator square-depth carrier。

---

## 4. 两个 summands 在 target prime 上都是 units

main genuine prime有

\[
p\nmid Q a_2b_1Wa_3.
\]

还需要检查 `beta`。

因为

\[
p^h\mid b_2,b_3,
\qquad
p\nmid b_1 10,
\]

所以

\[
\beta
=b_1 10^{m_2+m_3}
+b_2 10^{m_3}
+b_3
\equiv
b_1 10^{m_2+m_3}
ot\equiv0\pmod p.
\]

故

\[
\boxed{p\nmid\beta.}
\tag{Beta-unit}

因此 `(Concat-same/opp)` 的 `2h` 深度完全来自两个 p-units 的 cancellation；没有剩余 denominator factor藏在括号中。

这比 cube-depth 形式更规范：

\[
\boxed{
\underbrace{C_\sigma}_{b_2\text{ baseline}}
\times
\underbrace{C_\sigma^2}_{\Psi_\sigma\text{ primitive cancellation}}
}
\]

已经精确分开。

---

## 5. orientation-free full-concat product

两 sign cores 互素且

\[
C_G^{\rm main}=C_{\rm same}C_{\rm opp}
\]

差 `10^{o(S)}` exceptional core。因此

\[
\boxed{
(C_G^{\rm main})^2
\mid
\bigl(Q a_2^2b_1^2\beta\bigr)^2
-(Wa_3)^2.
}
\tag{Concat-product}

它完全使用 original integers 与统一 discriminant root `W`，不再出现 sphere ghosts或 Gaussian orientation choice。

---

## 6. exact lift 把 denominator carrier 推到 numerator shell

全局 exact lift 给

\[
\boxed{q\alpha=H\beta.}
\tag{6.1}

固定 sign core `C_sigma`。pair-max main prime在 `q` 与 `H` 中至少各含完整 `C_sigma` depth，因此定义整数

\[
q_\sigma:=\frac q{C_\sigma},
\qquad
H_\sigma:=\frac H{C_\sigma}.
\tag{6.2}

由 `(6.1)`：

\[
q_\sigma\alpha=H_\sigma\beta.
\tag{6.3}

将 `Psi_sigma` 乘以 `H_sigma`：

\[
\begin{aligned}
H_\sigma\Psi_\sigma
&=Q a_2^2b_1^2H_\sigma\beta
\pm H_\sigma W a_3\\
&=q_\sigma Q a_2^2b_1^2\alpha
\pm H_\sigma W a_3.
\end{aligned}
\]

由于

\[
C_\sigma^2\mid\Psi_\sigma,
\]

得到 numerator-shell version

\[
\boxed{
C_\sigma^2
\mid
q_\sigma Q a_2^2b_1^2\alpha
\pm H_\sigma W a_3.
}
\tag{Numerator-carrier}

注意乘 `H_sigma` 可能在个别 prime 上增加额外深度；本文只使用安全的 lower bound `C_sigma^2`，不把该额外深度计作新的 obstruction。

---

## 7. target prime 上 `alpha` repeat 与 sphere-height excess完全相同

固定

\[
p^h\Vert C_\sigma.
\]

由于 pair-max channel 在 `q` 中已达到深度 `h`：

\[
v_p(q)=h.
\]

而 `(Beta-unit)` 给

\[
v_p(\beta)=0.
\]

从

\[
q\alpha=H\beta
\]

得到 exact valuation identity：

\[
\boxed{
v_p(\alpha)=v_p(H)-h.}
\tag{Alpha-height-excess}

同时

\[
v_p(q_\sigma)=0,
\qquad
v_p(H_\sigma)=v_p(\alpha).
\tag{7.1}

因此 `(Numerator-carrier)` 中两个 summands 自带完全相同的 `alpha` baseline：若

\[
e_p:=v_p(\alpha),
\]

则

\[
\boxed{
\begin{aligned}
v_p(q_\sigma Q a_2^2b_1^2\alpha)&=e_p,\\
v_p(H_\sigma W a_3)&=e_p.
\end{aligned}}
\tag{7.2}

所以把共同 `p^{e_p}` 抽掉后，仍需承担原 `Psi_sigma` 的完整 `2h` unit cancellation。

换言之，exact-lift push 不会凭空支付 genuine square-depth；它只是把同一 p-adic phase从 `(beta,a3)` 坐标图搬到 `(alpha,a3)` 坐标图。

---

## 8. 与 full-rational `G_exc` 的区别

full-rational Good 中，最后困难被压成

\[
(C_N,A_N)=G_{\rm exc}
\]

的一份 **额外 numerator depth**。

这里 genuine-Gaussian carrier 的结构不同：即使

\[
v_p(\alpha)=0,
\]

仍有

\[
p^{2h}\mid\Psi_\sigma
\]

的 primitive unit-unit cancellation。因此 genuine branch 的 square-depth contact不是由 numerator repeat 才出现；它已经存在于 `(beta,a3,W)` phase 本身。

这说明 genuine branch 确实需要与 full-rational `G_exc` 不同的 closure mechanism。

---

## 9. 新 frontier

目前 genuine branch 已从抽象 orientation 走到两个 exact original-integer forms：

\[
\boxed{
C_\sigma^2
\mid
Q a_2^2b_1^2\beta\pm Wa_3,
}
\tag{9.1}

以及

\[
\boxed{
C_\sigma^2
\mid
q_\sigma Q a_2^2b_1^2\alpha
\pm H_\sigma W a_3.
}
\tag{9.2}

前者是 **full denominator concat carrier**，后者是 **full numerator concat carrier**。

两式是同一 p-adic phase 的 exact-lift 两个坐标图，不能重复收费；但它们提供了一个干净接口，可继续与十进制 shell

\[
\alpha=A_{12}10^{n_3}+a_3,
\qquad
\beta=Q10^{m_3}+b_3
\]

联立。

下一步最有价值的是：把 `(9.1)` 中的 `beta=Q10^m+b3` 和 `a3` 做 Euclidean/digit remainder normalization，看看 `C_sigma^2` 是否强迫一个短于 `2 log C_sigma` 的 remainder；若该 remainder又完整退回 discriminant identity，则记录 no-go。

---

## 10. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`Phi_sigma=b2 Psi_sigma`；`Beta-tail`；primitive `Concat-same/opp`；`Beta-unit`；orientation-free `Concat-product`；exact-lift `Numerator-carrier`；`Alpha-height-excess`。
- **`失效/降级`**：把 denominator carrier与 numerator carrier当成两份独立 p-adic收费。
- **`待证`**：`Psi_sigma` 的 decimal remainder normalization；genuine-Gaussian closure；DD 全局空性。

---

<a id="source-genuine-full-concat-hensel"></a>

> 整合来源：`genuine-full-concat-hensel.md`

# DD genuine-Gaussian full-concat carrier 的两层 Hensel 分解

> **依赖：** [`genuine-full-concat-carrier.md`](good-genuine-ledger.md#source-genuine-full-concat-carrier) 与 terminal factorization
> \[
> b_3=BJC_0q_c\theta s,
> \qquad
> C_0s=C_Lv_0.
> \]
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。上一文件给
> \[
> C_\sigma^2\mid
> Q a_2^2b_1^2\beta\pm Wa_3.
> \]
> 本文利用 `beta=Q10^{m_3}+b_3` 将这份 square depth 分成两个连续层：第一层作用于
> \[
> R_\sigma=Q^2a_2^2b_1^2 10^{m_3}\pm Wa_3,
> \]
> 且对每个 target `p^h` 有 **exact depth** `v_p(R_sigma)=h`；除去这一层后，第二 quotient 与 `b_3/C_sigma` 再发生至少 `h` 深度的 unit-unit cancellation。
>
> 这给 genuine branch 一个真正的 two-level Hensel ledger，并把第二层显式接到 `q_c` source factor上。

---

## 1. 统一 sign 记号

定义

\[
\boxed{A_c:=Q a_2^2b_1^2.}
\tag{1.1}

对 `sigma=same,opp` 取符号

\[
\epsilon_{\rm same}=-1,
\qquad
\epsilon_{\rm opp}=+1.
\]

上一文件的 carrier 统一写成

\[
\boxed{
\Psi_\sigma
=A_c\beta+\epsilon_\sigma Wa_3,
\qquad
C_\sigma^2\mid\Psi_\sigma.
}
\tag{1.2}

利用

\[
\beta=Q10^{m_3}+b_3,
\]

定义 first-layer integer

\[
\boxed{
R_\sigma
:=A_cQ10^{m_3}+\epsilon_\sigma Wa_3
=Q^2a_2^2b_1^2 10^{m_3}
+\epsilon_\sigma Wa_3.
}
\tag{1.3}

则 exact 地

\[
\boxed{
\Psi_\sigma=R_\sigma+A_cb_3.
}
\tag{Layer-decomp}

---

## 2. 第一层：`C_sigma | R_sigma`

因为

\[
C_\sigma\mid b_3
\]

且

\[
C_\sigma^2\mid\Psi_\sigma,
\]

从 `(Layer-decomp)` 模 `C_sigma` 立刻得到

\[
\boxed{C_\sigma\mid R_\sigma.}
\tag{Hensel-1}

因此定义整数 quotient

\[
\boxed{
K_\sigma:=\frac{R_\sigma}{C_\sigma}.
}
\tag{2.1}

同时定义

\[
\boxed{
b_{3,\sigma}:=\frac{b_3}{C_\sigma}.}
\tag{2.2}

将 `(Layer-decomp)` 除以 `C_sigma`：

\[
\boxed{
\frac{\Psi_\sigma}{C_\sigma}
=K_\sigma+A_cb_{3,\sigma}.
}
\tag{2.3}

---

## 3. 第二层：`C_sigma | K_sigma+A_c b_{3,sigma}`

由

\[
C_\sigma^2\mid\Psi_\sigma
\]

和 `(2.3)`：

\[
\boxed{
C_\sigma
\mid
K_\sigma+A_cb_{3,\sigma}.
}
\tag{Hensel-2}

这就是 square-depth carrier 的第二层 quotient congruence。

它与第一层的变量不同：

- 第一层把 `Wa3` 与 pure decimal term `A_c Q 10^m` 对齐；
- 第二层把第一层 quotient `K_sigma` 与 denominator tail `A_c b3/C_sigma` 对齐。

---

## 4. 第一层深度事实上恰好是 `h`

固定

\[
p^h\Vert C_\sigma.
\]

main unit ledger 给

\[
p\nmid A_c.
\]

并且

\[
v_p(b_3)=h,
\]

所以

\[
\boxed{p\nmid b_{3,\sigma}.}
\tag{4.1}

因此

\[
A_cb_{3,\sigma}
\]

是 p-unit。

由 `(Hensel-2)`：

\[
K_\sigma+A_cb_{3,\sigma}
\equiv0\pmod p.
\]

若 `p|K_sigma`，左边模 `p` 会等于非零 unit `A_cb_{3,sigma}`，矛盾。故

\[
\boxed{p\nmid K_\sigma.}
\tag{K-unit}

由于

\[
R_\sigma=C_\sigma K_\sigma,
\]

得到精确赋值：

\[
\boxed{
v_p(R_\sigma)=h.
}
\tag{Hensel-1-exact}

所以 genuine square-depth 不可能全部堆在第一层；第一层只拿走恰好一份 `h`。

---

## 5. 第二层至少再承担完整 `h`

由

\[
\Psi_\sigma
=C_\sigma\left(K_\sigma+A_cb_{3,\sigma}\right)
\]

以及

\[
v_p(\Psi_\sigma)\ge2h,
\]

立刻得到

\[
\boxed{
v_p\left(K_\sigma+A_cb_{3,\sigma}\right)\ge h.}
\tag{Hensel-2-depth}

而 §4 已证明两项都是 p-units：

\[
\boxed{
p\nmid K_\sigma A_cb_{3,\sigma}.}
\tag{5.1}

因此第二层是 genuine unit-unit cancellation，不含第一层的 denominator baseline。

整个 local depth ledger 为

\[
\boxed{
\begin{array}{c|c}
\text{层}&\text{target depth}\\ \hline
R_\sigma=C_\sigma K_\sigma&h\ \text{(exact)}\\
K_\sigma+A_cb_{3,\sigma}&\ge h.
\end{array}}
\tag{Two-layer-ledger}

---

## 6. 第二层显式含 `q_c` source factor

terminal factorization 为

\[
b_3=BJC_0q_c\theta s,
\]

而

\[
C_0s=C_Lv_0.
\]

故

\[
\boxed{
b_3=BJq_c\theta C_Lv_0.}
\tag{6.1}

因为

\[
C_\sigma\mid C_L,
\]

定义

\[
C_{\rm co,\sigma}:=\frac{C_L}{C_\sigma}.
\]

则

\[
\boxed{
b_{3,\sigma}
=BJq_c\theta v_0 C_{\rm co,\sigma}.}
\tag{6.2}

代入 `(Hensel-2)`：

\[
\boxed{
C_\sigma
\mid
K_\sigma
+A_c BJq_c\theta v_0 C_{\rm co,\sigma}.
}
\tag{Source-Hensel-2}

这就是 genuine branch 到 clean source core `q_c` 的第一个 explicit second-layer interface。

注意

\[
(C_\sigma,q_c)=1
\]

沿用 main `C_L` 与 clean source 的 asymptotic coprimality（删除 `o(S)` overlap）。所以第二项中的 `q_c` 不支付 `C_sigma` depth；它只控制 moving residue 的 source shape。

---

## 7. 也可消去 `J q_c theta`

terminal overlap还有

\[
Q=JUq_c\theta.
\]

所以

\[
Jq_c\theta=\frac QU.
\]

并且 `U` 整除 `Q` 于当前 terminal identity 中。于是 `(6.2)` 还可写成

\[
\boxed{
b_{3,\sigma}
=Bv_0 C_{\rm co,\sigma}\frac QU.}
\tag{7.1}

相应第二层为

\[
\boxed{
C_\sigma
\mid
K_\sigma
+A_c Bv_0 C_{\rm co,\sigma}\frac QU.
}
\tag{Source-Hensel-2b}

两种写法用途不同：

- `(Source-Hensel-2)` 显式保留 clean core `q_c`；
- `(Source-Hensel-2b)` 把它换成 denominator prefix `Q` 与 S-unit cofactor `U`。

二者是同一 identity，不能重复计费。

---

## 8. 第一层也是一个纯 digit/discriminant congruence

`Hensel-1` 展开为

\[
\boxed{
C_\sigma
\mid
Q^2a_2^2b_1^2 10^{m_3}
+\epsilon_\sigma Wa_3.
}
\tag{Digit-Hensel-1}

所有 coefficient 在 target prime 上均为 units。因此第一层给出一个 canonical root：

\[
\boxed{
Wa_3
\equiv
-\epsilon_\sigma Q^2a_2^2b_1^2 10^{m_3}
\pmod{C_\sigma}.
}
\tag{8.1}

其 lifting quotient就是 `K_sigma`；第二层再要求 `K_sigma` 命中明确的 denominator/source residue。

这把 genuine branch真正改写成了：

\[
\boxed{
\text{一个 first digit root}
\quad+\quad
\text{一个 source-controlled second lift}.}
\tag{8.2}

---

## 9. 当前最具体的 closure target

现有 p-adic 信息已经不再模糊：

\[
R_\sigma=C_\sigma K_\sigma,
\qquad
p\nmid K_\sigma,
\]

\[
C_\sigma
\mid
K_\sigma+A_cBJq_c\theta v_0C_{\rm co,\sigma}.
\]

所以要关闭 genuine branch，最自然的新目标是证明 second-lift quotient `K_sigma` 无法同时满足：

1. 它来自 exact first-layer digit integer
   \[
   K_\sigma
   =\frac{Q^2a_2^2b_1^2 10^{m_3}+\epsilon_\sigma Wa_3}{C_\sigma};
   \]
2. 它在模 `C_sigma` 下等于一个显式 `q_c`-source residue；
3. `K_sigma` 对 target primes 为 unit；
4. `C_sigma` 与 `q_c` 只有 subexponential overlap。

若能从 `K_sigma` 抽出一个 `<C_sigma` 的 natural representative，即可真正获得 strict surplus。若完整代入只重构 discriminant identity / `b3` factorization，则记录该 second-layer route 的 no-go。

---

## 10. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`Layer-decomp`、`Hensel-1`、`Hensel-2`、`K-unit`、`Hensel-1-exact`、second-layer full depth、`Source-Hensel-2` 与 `Source-Hensel-2b`。
- **`失效/降级`**：把两种 source 写法当两份独立 congruence。
- **`待证`**：second-lift quotient `K_sigma` 的 natural short representative / strict height bound；genuine-Gaussian closure；DD 全局空性。

---

<a id="source-genuine-large-core-crt"></a>

> 整合来源：`genuine-large-core-crt.md`

# DD genuine-large core 的 fixed `q_c^2 × C_G` prefix CRT

> **依赖：** [`genuine-a12-fixed-crt.md`](good-genuine-ledger.md#source-genuine-a12-fixed-crt)、[`good-prefix-crt-location-audit.md`](good-genuine-ledger.md#source-good-prefix-crt-location-audit) 的 Q-side exact parent、frontier constants。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文把两个 coefficients 不含 `A_12,a_3,W` 的 fixed decimal periods联立：
>
> 1. clean-source Q-side period `q_c^2`；
> 2. orientation-locked genuine period `C_G`。
>
> 因 `q_c` 与 pair-max core渐近互素，联合 period 高度为
> \[
> (2z_*+c)S+o(S),
> \qquad c:=\frac{\log C_G}{S}.
> \]
> 当
> \[
> c>1-2z_*=0.382232844764\ldots
> \]
> 时，它严格超过 `A_12` 的 `S+o(S)` digit window，因此在固定 denominator/source/small-prefix fiber中 `A_12` 至多一个。
>
> 本文是 counting/uniqueness 结果，不证明该唯一 candidate不存在。

---

## 1. fixed Q-side `A_12` congruence

记

\[
D:=10^d,
\qquad
F:=5^T,
\]

\[
X=2^HZ,
\qquad
\Sigma=X+FU,
\qquad
V=X-FU.
\]

已有 exact identities

\[
\Sigma R_0
=g_0(BDVA_{12}-Ua_3),
\tag{1.1}
\]

以及

\[
q_c^2L_{\rm clean}
=g_0a_3+FR_0.
\tag{1.2}
\]

由 `(1.1)`：

\[
g_0BDVA_{12}
=\Sigma R_0+g_0Ua_3.
\]

用 `(1.2)` 消去 `g_0a_3`：

\[
\begin{aligned}
g_0BDVA_{12}
&=\Sigma R_0+U(q_c^2L_{\rm clean}-FR_0)\\
&=(\Sigma-UF)R_0+Uq_c^2L_{\rm clean}\\
&=XR_0+Uq_c^2L_{\rm clean}.
\end{aligned}
\]

因此得到 exact parent

\[
\boxed{
g_0BDVA_{12}-XR_0
=Uq_c^2L_{\rm clean}.}
\tag{Q-fixed-exact}

模 `q_c^2`：

\[
\boxed{
g_0BDV A_{12}
\equiv XR_0
\pmod{q_c^2}.}
\tag{Q-fixed}

删去 coefficient exceptional core后，`A_12` coefficient与 `q_c` 互素，所以 effective period为

\[
\boxed{q_c^2/10^{o(S)}.}
\tag{1.3}

frontier 给

\[
\log q_c
=z_*S+o(S),
\qquad
z_*=0.308883577618\ldots,
\]

故

\[
\boxed{
\log(q_c^2)
=0.617767155236\ldots S+o(S).
}
\tag{1.4}

---

## 2. fixed genuine `A_12` congruence

`genuine-a12-fixed-crt.md` 已证明

\[
\boxed{
2\mathscr T g_0BD e_G\Sigma R_0 A_{12}
\equiv M_{G,0}
\pmod{C_G},
}
\tag{G-fixed}

其中

\[
e_G=V/C_G
\]

且 coefficient在 genuine main support上为 unit。因此 effective period为

\[
\boxed{C_G/10^{o(S)}.}
\tag{2.1}

重要的是 `(G-fixed)` 的 coefficient与 `M_{G,0}` 都不含

\[
A_{12},\quad a_3,\quad W.
\]

所以 `(Q-fixed)` 与 `(G-fixed)` 可以在同一个 fixed denominator/source/small-prefix fiber中真正作为两个固定 residue classes联立，而不是 moving-root congruences。

---

## 3. 两个 periods 渐近互素

terminal source separation给

\[
\boxed{(q_c,C_L)=10^{o(S)}}
\]

按 gcd height理解。

又

\[
C_G\mid C_L.
\]

所以

\[
\boxed{(q_c^2,C_G)=10^{o(S)}.}
\tag{3.1}

因此两个 fixed congruences的联合 effective period为

\[
\boxed{
M_G^{\rm CRT}
=\frac{q_c^2C_G}{10^{o(S)}}.
}
\tag{3.2}

---

## 4. genuine mass parameter 与 threshold

定义 genuine main-height ratio

\[
\boxed{
c:=\frac{\log C_G}{S}.}
\tag{4.1}

则

\[
\log M_G^{\rm CRT}
=(2z_*+c)S+o(S).
\tag{4.2}

prefix polarization 已证明

\[
\boxed{\log A_{12}=S+o(S).}
\tag{4.3}

因此若

\[
2z_*+c>1,
\]

联合 period严格大于合法 `A_12` 窗口。

阈值为

\[
\boxed{
c>1-2z_*}
\tag{4.4}

即

\[
\boxed{
c>0.382232844764\ldots.}
\tag{Genuine-CRT-threshold}

---

## 5. uniqueness lemma

固定一个 terminal denominator/source/small-prefix fiber，使 `(Q-fixed)` 与 `(G-fixed)` 的所有 coefficients、right-hand residues、`q_c,C_G` 固定。

若存在两个不同合法 prefixes

\[
A_{12}^{(1)}\ne A_{12}^{(2)}
\]

同时满足两个 congruences，则其差被联合 period整除：

\[
M_G^{\rm CRT}
\mid
A_{12}^{(1)}-A_{12}^{(2)}.
\]

另一方面 digit window给

\[
|A_{12}^{(1)}-A_{12}^{(2)}|
<10^{S+o(S)}.
\]

当 `(Genuine-CRT-threshold)` 成立时：

\[
M_G^{\rm CRT}
=10^{(2z_*+c)S+o(S)}
>10^{S+o(S)}
\]

for sufficiently large `S`，矛盾。

所以：

\[
\boxed{
 c>0.382232844764\ldots
 \Longrightarrow
 \#\{A_{12}\text{ in a fixed genuine fiber}\}\le1.
}
\tag{Large-genuine-uniqueness}

---

## 6. leading-block version

prefix polarization还有

\[
A_{12}=10^{n_2}a_1+a_2,
\qquad
n_2=o(S),
\qquad
\log a_2=o(S).
\]

固定 small suffix data `(n_2,a_2)` 后，`A_12` 与 `a_1` 是 injective affine correspondence。因此同样有

\[
\boxed{
 c>0.382232844764\ldots
 \Longrightarrow
 \#\{a_1\text{ in the fixed fiber}\}\le1.
}
\tag{Large-genuine-a1}

这把此前只在 full-rational Q/G CRT 中得到的 prefix uniqueness扩展到 genuine core足够大的 sector。

---

## 7. threshold 以下意味着 rational-contact mass 至少 `2z_*`

rational/genuine main split满足

\[
\log(D_+D_-)+\log C_G
=S+o(S).
\]

若 genuine sector未达到 `(Genuine-CRT-threshold)`，即

\[
c\le1-2z_*+o(1),
\]

则 rational-contact mass至少为

\[
\boxed{
\frac{\log(D_+D_-)}S
\ge2z_*+o(1)
=0.617767155236\ldots+o(1).
}
\tag{Rational-mass-floor}

所以 terminal frontier被进一步切成：

1. **large-genuine sector**
   \[
   c>0.382232844764\ldots,
   \]
   fixed fiber中 `A_12/a_1` 至多一个；
2. **rational-heavy sector**
   \[
   \log(D_+D_-)
   \ge0.617767155236\ldots S+o(S).
   \]

第二支仍待把 partial rational-contact mass与已有 Good/Bad/cofactor machinery重新做容量账本。

---

## 8. no-double-count 边界

联合 period大于 digit window只给

\[
\#\{A_{12}\}\le1,
\]

不自动给

\[
\#\{A_{12}\}=0.
\]

而 genuine period `C_G` 的 p-adic depth已知由 sphere carrier支付；本文只把它用作 CRT period，不增加 local height surplus。

下一步有两个互补方向：

- 对 large-genuine sector研究唯一 CRT lift 的 Archimedean location；
- 对 rational-heavy sector把 `0.617767...S` 的 contact mass重新代入 partial Good/Bad capacity ledger，争取得到严格 mass inequality。

---

## 9. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：fixed Q-side `A_12` congruence、fixed genuine `A_12` congruence、联合 period、threshold `c>0.382232844764...`、large-genuine fixed-fiber uniqueness、complementary rational mass floor。
- **`有限/计数结论`**：上述 uniqueness 只在 fixed terminal fiber中使用，不是 eventual emptiness。
- **`待证`**：large-genuine unique-lift location；rational-heavy partial-contact capacity；genuine / DD frontier emptiness。

---

<a id="source-genuine-tail-root-orientation-lock"></a>

> 整合来源：`genuine-tail-root-orientation-lock.md`

# DD genuine-Gaussian 的 tail-root 线性化与全局 orientation lock

> **依赖：** [`global-framework.md`](../../global-framework.md) 的统一判别平方与 primitive tail quadratic、[`genuine-full-concat-hensel.md`](good-genuine-ledger.md#source-genuine-full-concat-hensel) 的 first-layer Hensel、以及 frontier pair-max square-depth
> \[
> \Pi_{\rm sph}^2\mid y_2+i y_3.
> \]
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文首先把 primitive tail quadratic 的判别式完全化成统一 discriminant root `W`，得到一个此前未显式使用的全局线性恒等式
> \[
> \mathscr T a_3
> =\kappa G^2C_{\rm DD}+\eta(\kappa+G)W,
> \qquad \eta\in\{\pm1\},
> \]
> 其中
> \[
> \mathscr T=\frac{\kappa^2(\kappa+2G)}{10^{m_3}}\in\mathbf Z.
> \]
> 然后把它与 genuine first-layer Hensel 联立，证明 `same/opp` relative Gaussian orientation 在 main core 上不能逐 prime 自由选择：全局 tail-root sign `eta` 唯一决定 surviving orientation；另一 orientation 的 main mass 为零（恢复 exceptional core 后只有 `10^{o(S)}`）。
>
> 本文不关闭 genuine-Gaussian branch；它消除的是 relative-orientation entropy。

---

## 1. primitive tail quadratic 与记号

统一框架中 DD 的 coefficient pair 写为

\[
(C,D)=(C_{\rm DD},Q),
\]

其中

\[
C_{\rm DD}=10^{d_3}A_{12}.
\]

令

\[
10^{m_3}=\delta_3L,
\qquad
b_3=\delta_3\tau,
\qquad
z_3=\frac{a_3}{\delta_3}.
\]

这里 `z_3` 只作为 rational root 使用，不要求 `delta_3|a_3`。

primitive tail quadratic 为

\[
-\kappa(\kappa+2G)z_3^2
+2G^2LC_{\rm DD}z_3
+\mathcal C_3
=0,
\tag{1.1}
\]

其中

\[
\mathcal C_3
=G^2L^2C_{\rm DD}^2
-\mathcal N_{12}(LQ+\tau)^2.
\tag{1.2}
\]

同时 tail-weight identity 为

\[
\boxed{\kappa\tau=LQG.}
\tag{Tail-weight}
\]

统一 discriminant square 为

\[
\boxed{
W^2
=\kappa^2G^2C_{\rm DD}^2
-\kappa Q^2\mathcal N_{12}(\kappa+2G).
}
\tag{Disc-W}
\]

---

## 2. tail quadratic 的判别式正好由 `W` 给出

把 `(1.1)` 视为关于 `z_3` 的二次式。其判别式为

\[
\begin{aligned}
\Delta_z
&=4G^4L^2C_{\rm DD}^2
+4\kappa(\kappa+2G)\mathcal C_3\\
&=4\Bigl[
G^2L^2C_{\rm DD}^2(\kappa+G)^2
-\kappa(\kappa+2G)\mathcal N_{12}(LQ+\tau)^2
\Bigr].
\end{aligned}
\tag{2.1}

由 `(Tail-weight)`：

\[
LQ+\tau
=LQ\frac{\kappa+G}{\kappa}.
\tag{2.2}
\]

代入 (2.1)：

\[
\begin{aligned}
\Delta_z
&=
\frac{4L^2(\kappa+G)^2}{\kappa^2}
\Bigl[
\kappa^2G^2C_{\rm DD}^2
-\kappa Q^2\mathcal N_{12}(\kappa+2G)
\Bigr]\\
&=
\boxed{
\left(
\frac{2L(\kappa+G)}{\kappa}W
\right)^2}.
\end{aligned}
\tag{Tail-discriminant}
\]

因此 actual rational root `z_3` 必满足某个全局固定符号

\[
\boxed{\eta\in\{\pm1\}}
\]

使

\[
\boxed{
\kappa^2(\kappa+2G)z_3
=L\Bigl[
\kappa G^2C_{\rm DD}
+\eta(\kappa+G)W
\Bigr].
}
\tag{Tail-root-linear}
\]

这个 `eta` 是由 actual tail root 一次性决定的全局符号，不随 prime 改变。

---

## 3. 消去 `delta_3`：得到 original-integer 线性恒等式

统一 denominator-tail certificate 已证明

\[
10^{m_3}\mid\kappa^2(\kappa+2G).
\]

定义

\[
\boxed{
\mathscr T
:=\frac{\kappa^2(\kappa+2G)}{10^{m_3}}
\in\mathbf Z_{>0}.
}
\tag{3.1}

由

\[
z_3=\frac{a_3}{\delta_3},
\qquad
10^{m_3}=\delta_3L,
\]

把 `(Tail-root-linear)` 乘 `delta_3`，得到完全 original-integer 的恒等式

\[
\boxed{
\mathscr T a_3
=\kappa G^2C_{\rm DD}
+\eta(\kappa+G)W.
}
\tag{Tail-root-original}

这条式子是后面 orientation lock 的核心。

---

## 4. pair-max main prime 上自动得到 square-depth tail-root congruence

固定 one-channel pair-max main prime-power

\[
p^h\Vert C_L^{\rm main}.
\]

删除 coefficient exceptional core 后：

\[
p\ne2,5,
\qquad
p^h\Vert b_2,
\qquad
p^h\Vert b_3,
\qquad
p\nmid b_1Qa_2a_3.
\tag{4.1}

又有

\[
G=b_1b_2,
\]

故

\[
p^h\Vert G.
\tag{4.2}

由

\[
\kappa b_3=10^{m_3}QG
\tag{4.3}
\]

把 `p^h` 从 `b_3,G` 两边同时约掉，可见

\[
\boxed{p\nmid\kappa.}
\tag{4.4}

于是

\[
p\nmid\kappa+G.
\]

`(Tail-root-original)` 中

\[
p^{2h}\mid G^2,
\]

所以得到

\[
\boxed{
p^{2h}
\mid
\mathscr T a_3
-\eta(\kappa+G)W.
}
\tag{Tail-root-p2h}

聚合 main pair-max core，可写成

\[
\boxed{
(C_L^{\rm main})^2
\mid
\mathscr T a_3
-\eta(\kappa+G)W
}
\tag{Tail-root-core}

按删除 `10^{o(S)}` exceptional core 后理解。

---

## 5. 与 genuine first-layer Hensel 联立

沿用

\[
A_c=Qa_2^2b_1^2,
\]

并对

\[
\sigma\in\{\mathrm{same},\mathrm{opp}\}
\]

定义

\[
\epsilon_{\rm same}=-1,
\qquad
\epsilon_{\rm opp}=+1.
\tag{5.1}

`genuine-full-concat-hensel.md` 已证明，对

\[
p^h\Vert C_\sigma
\]

有 first-layer congruence

\[
\boxed{
Q^2a_2^2b_1^2 10^{m_3}
+\epsilon_\sigma Wa_3
\equiv0
\pmod{p^h}.
}
\tag{H1}

记

\[
y:=a_2b_1.
\]

将 `(H1)` 乘以 `eta(kappa+G)`，再用 `(Tail-root-p2h)` 的模 `p^h` 版本消掉 `W`，然后乘 `eta 10^{m_3}`，得到

\[
(\kappa+G)Q^2y^2 10^{2m_3}
+\epsilon_\sigma\eta\,
\kappa^2(\kappa+2G)a_3^2
\equiv0
\pmod{p^h}.
\tag{5.2}

写

\[
b_2=p^h b_{2,p},
\qquad
b_3=p^h b_{3,p},
\qquad
G=p^hG_p,
\]

其中

\[
G_p=b_1b_{2,p}.
\tag{5.3}

由 `(4.3)`：

\[
\boxed{
\kappa b_{3,p}
=10^{m_3}QG_p.
}
\tag{5.4}

把 `(5.4)` 代入 `(5.2)`，乘 p-unit `G_p^2` 并约去 `kappa^2`，再用

\[
\kappa+G\equiv\kappa+2G\equiv\kappa
\pmod{p^h},
\]

得到

\[
y^2b_{3,p}^2
+\epsilon_\sigma\eta\,G_p^2a_3^2
\equiv0
\pmod{p^h}.
\]

由 `y=a_2b_1`、`G_p=b_1b_{2,p}` 且 `p\nmid b_1`：

\[
\boxed{
a_2^2b_{3,p}^2
+\epsilon_\sigma\eta\,
a_3^2b_{2,p}^2
\equiv0
\pmod{p^h}.
}
\tag{Normalized-contact}

这是 tail-root 与 discriminant first lift 联立后的 normalized last-two-fractions contact。

---

## 6. sphere square-depth 已经给 normalized elliptic sum 深度 `2h`

pair-max sphere orientation 给

\[
\Pi_{\rm sph}^2\mid y_2+i y_3.
\]

在当前 rational prime `p^h` 上，因此

\[
\boxed{p^{2h}\mid y_2^2+y_3^2.}
\tag{6.1}

又因为

\[
q=p^hq_p,
\qquad
b_2=p^hb_{2,p},
\qquad
b_3=p^hb_{3,p},
\]

且 `q_p,b_{2,p},b_{3,p}` 都是 p-units，

\[
y_2=a_2\frac{q_p}{b_{2,p}},
\qquad
y_3=a_3\frac{q_p}{b_{3,p}}.
\]

乘以 p-unit

\[
\left(\frac{b_{2,p}b_{3,p}}{q_p}\right)^2
\]

不会改变 p-adic valuation，因此

\[
\boxed{
p^{2h}
\mid
a_2^2b_{3,p}^2+a_3^2b_{2,p}^2.
}
\tag{Sphere-normalized}

---

## 7. hyperbolic relative sign 不可能出现

若

\[
\epsilon_\sigma\eta=-1,
\]

则 `(Normalized-contact)` 给

\[
p^h
\mid
a_2^2b_{3,p}^2-a_3^2b_{2,p}^2.
\tag{7.1}

而 `(Sphere-normalized)` 甚至给更强的

\[
p^{2h}
\mid
a_2^2b_{3,p}^2+a_3^2b_{2,p}^2.
\tag{7.2}

特别地两式都模 `p^h` 为零。相加得到

\[
p^h\mid2a_2^2b_{3,p}^2.
\]

但

\[
p\nmid2a_2b_{3,p}
\]

由 main reducedness / unit ledger 保证，矛盾。

因此每个 genuine main prime都必须满足

\[
\boxed{
\epsilon_\sigma\eta=+1.
}
\tag{Orientation-lock-local}

---

## 8. 全局 orientation lock

`eta` 是 actual tail root 决定的一个**全局固定 sign**，而

\[
\epsilon_{\rm same}=-1,
\qquad
\epsilon_{\rm opp}=+1.
\]

所以 `(Orientation-lock-local)` 立刻给出：

- 若
  \[
  \eta=+1,
  \]
  则 genuine main primes 只能进入 `opp`；
- 若
  \[
  \eta=-1,
  \]
  则 genuine main primes 只能进入 `same`。

因此 relative Gaussian orientation 不再有逐 prime 的二元自由度。记 surviving class 为

\[
C_{\rm ell},
\]

wrong-sign class 为

\[
C_{\rm hyp}.
\]

则在 main core 上严格有

\[
\boxed{C_{\rm hyp}=1,}
\tag{8.1}

而恢复此前删除的 exceptional core 后：

\[
\boxed{
\log C_{\rm hyp}=o(S),
\qquad
C_{\rm ell}=C_G\cdot10^{o(S)}
}
\tag{Genuine-orientation-lock}

按 logarithmic main-height 理解。

这是真正的 entropy reduction：genuine branch 的 discriminant orientation 由一个 global tail-root sign 唯一决定。

---

## 9. 方法边界

surviving sign 满足

\[
\epsilon_\sigma\eta=+1,
\]

所以 `(Normalized-contact)` 退化成

\[
a_2^2b_{3,p}^2+a_3^2b_{2,p}^2
\equiv0\pmod{p^h},
\]

而 sphere carrier 已经给同一 quantity 更深的 `p^{2h}` divisibility。因此 surviving first-layer normalized contact本身不能作为第二份独立 height。

换言之：

\[
\boxed{
\text{tail-root linearization 的新作用是锁 orientation，}
\text{不是在 surviving elliptic class 上再次收费。}
}
\tag{No-double-pay}

下一步必须审计 second-layer `p^{2h}` full-concat cancellation 在 orientation lock 后是否也完全由 sphere square-depth支付。

---

## 10. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`Tail-discriminant`、`Tail-root-linear`、`Tail-root-original`、pair-max `Tail-root-p2h`、`Normalized-contact`、hyperbolic sign contradiction、global `Genuine-orientation-lock`。
- **`失效/降级`**：把 surviving elliptic first-layer contact当作 sphere carrier之外的新 obstruction。
- **`待证`**：orientation lock 后 second-layer square-depth是否完全 sphere-paid；genuine split-prime / digit-shell closure；DD 全局空性。

---

<a id="source-good-axis-normalization"></a>

> 整合来源：`good-axis-normalization.md`

# DD full-rational Good 的 axis-normalized excess 与三重 reader

> **依赖：** [`frontier.md`](frontier.md) 的 `Radius-split`、`Radius=Concat`、`Nc-slot`、`Nc1-elim`、`Concat-radius` 与 full rational axis factorization；以及 [`good-radius-excess.md`](good-genuine-ledger.md#source-good-radius-excess) 的 canonical `G_exc`。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文仍只处理假想
> \[
> \frac{n_3}{S}\to6.308883577618\ldots
> \]
> 的 full rational-contact Good 主质量，并默认删除总高度为 `o(S)` 的 coefficient / conjugate / Bad exceptional core。
>
> 本文完成三件事：
>
> 1. 证明 pure excess 的局部深度可只用 `alpha` 与 axis quotient `N_c` 读取：
>    \[
>    \varepsilon_p=\max(v_p(\alpha)-v_p(N_c),0).
>    \]
> 2. 将上一文件的 `G_exc` 改写成只含 `C_L,N_c,alpha` 的 canonical gcd；`H_R` 从 excess reader 中完全消失。
> 3. 构造一个由 axis Gaussian carrier 与最后两块 numerator 形成的 exact companion pair，并证明其 gcd quotient 在每个 main prime 上精确读取 `epsilon_p`。与 `N(Delta_1)` tail 一起得到三条等价 reader。
>
> 本文不证明 `G_exc` 为 subexponential，也不关闭 full rational Good。

---

## 1. 局部账本：`epsilon_p` 其实只是 `alpha` 超过 `N_c` 的深度

固定 main prime-power

\[
p^h\Vert C_L^{\rm main}.
\]

记

\[
r:=v_p(H_R),
\qquad
n:=v_p(N_c),
\qquad
a:=v_p(A_0)=v_p(\alpha).
\tag{1.1}
\]

最后一个等号使用 `Radius=Concat`；main coefficient-unit 条件保证

\[
p\nmid g_0(2^HZ+5^TU).
\]

`Radius-split` 给出

\[
\boxed{
a=\min(r,n)+\varepsilon_p,}
\tag{1.2}
\]

其中

\[
\varepsilon_p\ge0,
\qquad
\boxed{
\varepsilon_p>0\Longrightarrow r=n.
}
\tag{1.3}
\]

于是可以完全消去 `r`。

### 命题 1.1

对每个 main prime：

\[
\boxed{
\varepsilon_p
=\max(a-n,0)
=\max(v_p(\alpha)-v_p(N_c),0).
}
\tag{Axis-excess-local}
\]

### 证明

若 `epsilon_p=0`，则由 `(1.2)`

\[
a=\min(r,n)\le n,
\]

所以

\[
\max(a-n,0)=0=\varepsilon_p.
\]

若 `epsilon_p>0`，由 `(1.3)` 有 `r=n`，再由 `(1.2)`：

\[
a=n+\varepsilon_p,
\]

所以

\[
\max(a-n,0)=\varepsilon_p.
\]

证毕。

这说明此前写成

\[
\text{equal-depth }(H_R,N_c)
\text{ cancellation}
\]

的最后 tail，在真正扣除旧 payer 后只依赖：

\[
\boxed{
\text{concatenated numerator }\alpha
\quad\text{相对于 axis quotient }N_c\text{ 的正深度差。}
}
\]

---

## 2. `G_exc` 的 axis-normalized decimal gcd

令

\[
\boxed{
C_N
:=
\frac{C_L^{\rm main}}
{\gcd(C_L^{\rm main},N_c)},
}
\tag{2.1}
\]

以及真正的 decimal quotient

\[
\boxed{
A_N
:=
\frac{\alpha}{\gcd(\alpha,N_c)}.
}
\tag{2.2}
\]

对 `p^h || C_L^{main}`：

\[
v_p(C_N)=\max(h-n,0),
\tag{2.3}
\]

而命题 1.1 给

\[
\boxed{v_p(A_N)=\varepsilon_p.}
\tag{2.4}
\]

上一文件定义的 excess depth 为

\[
x_p
=\min(h,a)-\min(h,r,n).
\tag{2.5}
\]

如果 `epsilon_p=0`，则 `a=min(r,n)`，故 `x_p=0`。

如果 `epsilon_p>0`，则 `r=n`、`a=n+epsilon_p`，于是

\[
\begin{aligned}
x_p
&=\min(h,n+\varepsilon_p)-\min(h,n)\\
&=\min\bigl(\max(h-n,0),\varepsilon_p\bigr).
\end{aligned}
\tag{2.6}
\]

因此得到新的 exact reader：

\[
\boxed{
G_{\rm exc}
=\gcd(C_N,A_N)
}
\tag{Axis-decimal-gcd}
\]

按 `C_L^{main}` 的逐 prime-depth 精确成立。

换言之，`G_exc` 不再需要显式写成

\[
\frac{\gcd(C_L^{\rm main},\alpha)}
{\gcd(C_L^{\rm main},H_R,N_c)};
\]

它可以直接解释为：

\[
\boxed{
\text{未被 }N_c\text{ 支付的 main core}
\quad\cap\quad
\text{未被 }N_c\text{ 支付的真实 numerator}.}
\tag{2.7}
\]

这一步把 `H_R` 从 primitive excess 的定义中完全删掉。

---

## 3. canonical imbalance：core residual 与 numerator tail 逐素数只留一边

定义

\[
\boxed{
C_{\rm free}:=\frac{C_N}{G_{\rm exc}},
\qquad
A_{\rm tail}:=\frac{A_N}{G_{\rm exc}}.
}
\tag{3.1}
\]

由 `G_exc=gcd(C_N,A_N)` 立即有

\[
\boxed{
\gcd(C_{\rm free},A_{\rm tail})=1
}
\tag{Axis-imbalance}
\]

在 main core 上严格成立。

逐 prime 看，若 `epsilon_p>0`：

\[
v_p(C_N)=\max(h-n,0),
\qquad
v_p(A_N)=\varepsilon_p.
\]

抽掉最小值 `x_p` 后，只能剩下其中一边：

\[
\boxed{
\begin{array}{c|c|c}
\varepsilon_p<h-n
& p\mid C_{\rm free}
& p\nmid A_{\rm tail}\\
\varepsilon_p=h-n
& p\nmid C_{\rm free}A_{\rm tail}
& \\
\varepsilon_p>h-n
& p\nmid C_{\rm free}
& p\mid A_{\rm tail}.
\end{array}}
\tag{3.2}
\]

因此 `G_exc` 之后的 residual 不是两个仍然纠缠的 slots；它是一个真正的 **denominator-vs-numerator imbalance**。

---

## 4. 最后两块 numerator 自带一个 full-core Gaussian carrier

定义 full rational axis carrier

\[
\boxed{
Z_{\rm ax}:=C_*+iR_0,
\qquad
C_*:=\frac{g_0a_2B}{2}.
}
\tag{4.1}
\]

并沿用统一 orientation

\[
\Gamma:=\Pi_+\overline{\Pi_-},
\qquad
N(\Gamma)=E=D_+D_-.
\tag{4.2}
\]

full rational sign factorization 已给

\[
\boxed{\Gamma\mid Z_{\rm ax}.}
\tag{4.3}
\]

定义只使用最后两块 numerator 与 decimal tail 的 Gaussian integer

\[
\boxed{
Z_{23}
:=2a_3+i10^m a_2.
}
\tag{4.4}
\]

使用 exact bridge

\[
VA_0-g_0a_3=2\cdot5^TR_0
\tag{4.5}
\]

和

\[
10^m=2B5^T,
\tag{4.6}
\]

直接展开：

\[
\begin{aligned}
g_0Z_{23}
&=2g_0a_3+i g_0a_2 10^m\\
&=2VA_0-4\cdot5^TR_0
+4i5^TC_*\\
&=\boxed{
2VA_0+4i5^T(C_*+iR_0)}.
\end{aligned}
\tag{Tail-axis}
\]

因为

\[
E\mid V,
\qquad
\Gamma\mid Z_{\rm ax},
\]

且 main core 与 `g_0` 只有 `o(S)` overlap，所以

\[
\boxed{
\Gamma\mid Z_{23}
}
\tag{Two-block-carrier}
\]

在 full rational main orientation 上成立。

这是一条新的 terminal projection：pair-max rational-contact orientation 已经可以仅从

\[
2a_3+i10^m a_2
\]

读取；不需要 `A_{12}` 或 `Y=2\,10^dA_{12}`。

取范数还得到必要条件

\[
\boxed{
E\mid4a_3^2+10^{2m}a_2^2
}
\tag{4.7}
\]

按 main prime mass 理解。

> **审计边界：**`Two-block-carrier` 本身是 full-depth baseline，不应把它当成 `G_exc` 的第二次收费。真正的 excess 必须在除去 axis/common depth后读取。

---

## 5. axis / two-block carrier 的 exact companion pair

考虑 Gaussian product

\[
Z_{\rm ax}\overline{Z_{23}}
=(C_*+iR_0)(2a_3-i10^m a_2).
\]

定义其实部、虚部：

\[
\boxed{
\mathcal T_+
:=2C_*a_3+R_0 10^m a_2,
}
\tag{5.1}
\]

\[
\boxed{
\mathcal T_-
:=2R_0a_3-C_*10^m a_2.
}
\tag{5.2}
\]

### 5.1 `T_+` 精确等于 `V A_0` 通道

利用 `(4.5)`、`C_*=g_0a_2B/2` 与 `10^m=2B5^T`：

\[
\begin{aligned}
\mathcal T_+
&=g_0a_2Ba_3
+2B5^TR_0a_2\\
&=Ba_2(g_0a_3+2\cdot5^TR_0)\\
&=\boxed{Ba_2VA_0.}
\end{aligned}
\tag{Tplus}
\]

### 5.2 `T_-` 精确等于 `A_0/N_c` difference

由同一组恒等式：

\[
\begin{aligned}
g_0\mathcal T_-
&=2g_0R_0a_3-g_0C_*10^m a_2\\
&=2VR_0A_0
-4\cdot5^TR_0^2
-4\cdot5^TC_*^2.
\end{aligned}
\]

又有

\[
C_*^2+R_0^2=EN_c,
\qquad
V=Ee_0,
\]

所以

\[
\boxed{
g_0\mathcal T_-
=2E\bigl(e_0R_0A_0-2\cdot5^TN_c\bigr).}
\tag{Tminus}
\]

因此 `T_+` 与 `T_-` 是一个 exact companion pair：前者读取 `A_0`，后者比较 `A_0` 与 axis quotient `N_c`。

---

## 6. companion gcd quotient 精确读取 `epsilon_p`

定义

\[
\boxed{
\Lambda_{\rm ax}
:=
\frac{\mathcal T_+}
{\gcd(\mathcal T_+,\mathcal T_-)}.
}
\tag{6.1}
\]

若 `T_-<0`，gcd 取 `|T_-|`；这不影响任何赋值。对 main prime，`B,a_2,e_0,R_0,g_0,2,5` 都是 units。

由 `(Tplus)`：

\[
\boxed{v_p(\mathcal T_+)=h+a.}
\tag{6.2}
\]

由 `(Tminus)`，括号内两项的深度分别为 `a` 与 `n`。

### 情形一：`epsilon_p=0`

此时

\[
a=\min(r,n)\le n.
\]

若 `a<n`，则

\[
v_p(\mathcal T_-)=h+a.
\]

若 `a=n`，两项可能继续 cancellation，但至少有

\[
v_p(\mathcal T_-)\ge h+a.
\]

因为 `T_+` 的深度恰为 `h+a`，两种情况下都有

\[
v_p\gcd(\mathcal T_+,\mathcal T_-)=h+a,
\]

故

\[
v_p(\Lambda_{\rm ax})=0.
\tag{6.3}
\]

### 情形二：`epsilon_p>0`

由 `(1.3)`：

\[
r=n,
\qquad
a=n+\varepsilon_p>n.
\]

于是 `(Tminus)` 中两项深度不等，较浅项为 `N_c`：

\[
\boxed{v_p(\mathcal T_-)=h+n.}
\tag{6.4}
\]

因此

\[
\begin{aligned}
v_p(\Lambda_{\rm ax})
&=(h+n+\varepsilon_p)-(h+n)\\
&=\varepsilon_p.
\end{aligned}
\]

统一得到：

\[
\boxed{
v_p(\Lambda_{\rm ax})=\varepsilon_p}
\tag{Axis-tail-reader}
\]

对每个 main prime 精确成立。

所以 `Lambda_ax` 是一个 canonical **pure excess tail quotient**：full pair-max depth `h` 与 axis baseline `min(a,n)` 都已经被 ordinary gcd 自动删掉，只留下真正的 unit-unit excess。

---

## 7. `N(Delta_1)` 也给出同一个 tail reader

定义

\[
\boxed{
D_1
:=
\gcd\bigl(N(\Delta_1),H_R,N_c\bigr),
}
\tag{7.1}
\]

以及

\[
\boxed{
\Lambda_1
:=
\frac{N(\Delta_1)}{D_1}.
}
\tag{7.2}
\]

对 main prime，`Radius-split` 给

\[
v_p(N(\Delta_1))=\min(r,n)+\varepsilon_p.
\]

因此

\[
v_p(D_1)=\min(r,n),
\]

从而

\[
\boxed{v_p(\Lambda_1)=\varepsilon_p.}
\tag{Norm-tail-reader}
\]

这说明 cofactor norm tail、axis companion tail 与 decimal numerator tail 三者在 main support 上读取的是**同一个**深度函数 `epsilon_p`。

---

## 8. 三重 canonical gcd ladder

综合 §§2、6、7：

\[
v_p(A_N)
=v_p(\Lambda_{\rm ax})
=v_p(\Lambda_1)
=\varepsilon_p.
\tag{8.1}
\]

而

\[
v_p(C_N)=\max(h-n,0).
\]

所以同一个 `G_exc` 有三条完全等价的 reader：

\[
\boxed{
G_{\rm exc}
=\gcd(C_N,A_N)
=\gcd(C_N,\Lambda_{\rm ax})
=\gcd(C_N,\Lambda_1)
}
\tag{Gcd-ladder}
\]

按 `C_L^{main}` 的 prime-depth 精确成立。

这张 ladder 的三个坐标具有不同语义：

1. `A_N`：真实 concatenated numerator 的 axis-normalized quotient；
2. `Lambda_ax`：最后两块 Gaussian carrier 与 axis carrier 的 companion gcd quotient；
3. `Lambda_1`：secondary norm `N(Delta_1)` 去掉 `(H_R,N_c)` baseline 后的 quotient。

于是 pure excess 已从一条局部 cancellation 改写成一个 **同一 denominator residual `C_N` 与三个 natural tail readers 的公共 gcd**。

---

## 9. no-double-count 审计：raw `Z_23` 只读取 baseline

`Two-block-carrier` 给

\[
\Gamma\mid Z_{23}
\]

对整个 full rational main core成立，而不需要 `epsilon_p>0`。

所以后续不能把

\[
C_L\mid N(Z_{23})
\]

再次算作 pure excess 的独立模量。

真正的新 tail 位于

\[
\Lambda_{\rm ax}
=\mathcal T_+/\gcd(\mathcal T_+,\mathcal T_-),
\]

即先把 full axis / pair-max common depth自动删掉后剩下的 quotient。

同理，`Lambda_1` 必须先除以

\[
D_1=\gcd(N(\Delta_1),H_R,N_c)
\]

才能作为 excess reader；直接使用整个 `N(Delta_1)` 会重复计算 radius baseline。

---

## 10. 当前更新后的 primitive digit-shell 目标

上一文件把目标写成证明

\[
\log G_{\rm exc}=o(S).
\]

本文把可用输入进一步正规化为

\[
\boxed{
\begin{gathered}
C_N=\frac{C_L^{\rm main}}{(C_L^{\rm main},N_c)},\\[1mm]
A_N=\frac{\alpha}{(\alpha,N_c)},\\[1mm]
\Lambda_{\rm ax}
=\frac{\mathcal T_+}{(\mathcal T_+,\mathcal T_-)},\\[1mm]
\Lambda_1
=\frac{N(\Delta_1)}{(N(\Delta_1),H_R,N_c)},\\[1mm]
G_{\rm exc}
=(C_N,A_N)
=(C_N,\Lambda_{\rm ax})
=(C_N,\Lambda_1).
\end{gathered}}
\tag{10.1}
\]

因此下一条真正有价值的 strict lemma 已经可以表述得更窄：

> **Axis-normalized digit-shell separation（待证）**：证明 `C_N` 的正线性 main mass不能同时进入 `A_N` 与任一 independent normalized tail reader；或者证明 `A_N`、`Lambda_ax`、`Lambda_1` 在除去已知 common algebra 后的共同 main support只有 `10^{o(S)}`。

如果继续消元后只恢复 `(Tail-axis)`、`(Tplus)`、`(Tminus)` 或 `Nc1-elim`，则属于同一 local algebra 的重写，不得重复计费。

---

## 11. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`epsilon_p=max(v_p(alpha)-v_p(N_c),0)`；`G_exc=(C_N,A_N)`；canonical denominator/numerator imbalance；two-block full Gaussian carrier `Gamma | 2a_3+i10^m a_2`；exact companion pair `(Tplus)/(Tminus)`；`v_p(Lambda_ax)=epsilon_p`；`v_p(Lambda_1)=epsilon_p`；三重 gcd ladder `(Gcd-ladder)`。
- **`失效/降级`**：把 raw `Z_23` 的 full `C_L` divisibility 当作 excess surplus；未先删除 `(H_R,N_c)` baseline 就直接对 `N(Delta_1)` 收费。
- **`待证`**：axis-normalized digit-shell separation；`log G_exc=o(S)`；full rational Good emptiness；genuine-Gaussian split-prime / digit-shell closure；DD 全局空性与有效绝对高度界。

---

<a id="source-good-excess-gcd-ladder"></a>

> 整合来源：`good-excess-gcd-ladder.md`

# DD full-rational Good 的 canonical excess gcd ladder

> **依赖：** [`good-axis-normalization.md`](good-genuine-ledger.md#source-good-axis-normalization)。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文不增加新的 local resultant；它把上一文件得到的 axis-normalized depth
> \[
> c_p:=\max(h_p-v_p(N_c),0),
> \qquad
> \varepsilon_p:=\max(v_p(\alpha)-v_p(N_c),0)
> \]
> 提升成无需预先枚举 prime list 的 ordinary-integer gcd ladder。
>
> 核心结论：`G_exc` 是该 ladder 的第一层；稳定层读取 `C_N` support 上的完整 `epsilon_p`，而第一层之后的两个 residual 分别是 **unpaid denominator depth** 与 **numerator overflow**，逐 prime 永不同时出现。本文同时证明 `A_N`、`Lambda_ax`、`Lambda_1` 三条 ladder 在 main support 上完全相同，因此三者不能被误算成三份独立 obstruction。

---

## 1. 三个 tail reader 的共同局部深度

沿用

\[
C_N
=\frac{C_L^{\rm main}}
{(C_L^{\rm main},N_c)},
\]

\[
A_N
=\frac{\alpha}{(\alpha,N_c)},
\]

\[
\Lambda_{\rm ax}
=\frac{\mathcal T_+}{(\mathcal T_+,\mathcal T_-)},
\]

\[
\Lambda_1
=\frac{N(\Delta_1)}
{(N(\Delta_1),H_R,N_c)}.
\]

固定

\[
p^h\Vert C_L^{\rm main},
\qquad
n=v_p(N_c).
\]

定义

\[
\boxed{c_p:=v_p(C_N)=\max(h-n,0).}
\tag{1.1}
\]

上一文件已经证明

\[
\boxed{
v_p(A_N)
=v_p(\Lambda_{\rm ax})
=v_p(\Lambda_1)
=\varepsilon_p.}
\tag{1.2}
\]

其中

\[
\boxed{
\varepsilon_p
=\max(v_p(\alpha)-n,0).}
\tag{1.3}
\]

因此 main support 上的 primitive excess 已完全压成一对非负整数

\[
(c_p,\varepsilon_p).
\]

---

## 2. `G_exc` 是 ladder 的第一层

对任意 reader

\[
R\in\{A_N,\Lambda_{\rm ax},\Lambda_1\}
\]

定义

\[
\boxed{D_1(R):=\gcd(C_N,R).}
\tag{2.1}
\]

逐 prime：

\[
v_p(D_1(R))
=\min(c_p,\varepsilon_p).
\]

上一文件已识别该深度为 `x_p`，所以

\[
\boxed{
D_1(A_N)
=D_1(\Lambda_{\rm ax})
=D_1(\Lambda_1)
=G_{\rm exc}
}
\tag{2.2}
\]

按 `C_L^{main}` 的 prime-primary part 精确成立。

这里若三个普通 gcd 在 exceptional / non-main support 上还含其它因子，不把这些额外因子并入 `G_exc`；本文所有等号均指 main-primary projection，与前两文件约定一致。

---

## 3. `C_N^k` ladder 逐层读取完整 excess tail

对整数

\[
k\ge1
\]

和任一 reader `R` 定义

\[
\boxed{
D_k(R):=\gcd(C_N^k,R).
}
\tag{3.1}
\]

则

\[
\boxed{
v_p(D_k(R))
=\min(kc_p,\varepsilon_p).}
\tag{3.2}
\]

因此三条 ladder 的 main-primary part 对每个 `k` 都完全相同：

\[
\boxed{
D_k(A_N)^{\rm main}
=D_k(\Lambda_{\rm ax})^{\rm main}
=D_k(\Lambda_1)^{\rm main}.}
\tag{Reader-ladder-equality}
\]

这给出一个不需要 prime factorization 才能定义的 excess-depth reader。

---

## 4. successive quotient 读取第 `k` 个 core-height block

令

\[
\boxed{
E_k(R):=\frac{D_{k+1}(R)}{D_k(R)}.
}
\tag{4.1}
\]

由于 `D_k|D_{k+1}`，这是正整数。

逐 main prime：

\[
\boxed{
v_p(E_k(R))
=\min((k+1)c_p,\varepsilon_p)
-\min(kc_p,\varepsilon_p).}
\tag{4.2}
\]

所以：

- 若 `epsilon_p<=k c_p`，第 `k` 层以后不再出现该 prime；
- 若 `k c_p<epsilon_p<(k+1)c_p`，本层读取剩余 `epsilon_p-kc_p`；
- 若 `epsilon_p>=(k+1)c_p`，本层再读取完整一个 `c_p` block。

这把“excess 比剩余 main core 还深多少”变成普通 gcd successive quotients。

---

## 5. 稳定层与 full `C_N`-supported tail

对固定整数 reader `R`，存在有限 `k_0`，使得对所有 `k>=k_0`：

\[
D_k(R)=D_{k_0}(R)
\]

在 `C_N` support 上稳定。

记 main-primary 稳定值为

\[
\boxed{D_\infty.}
\tag{5.1}
\]

则

\[
\boxed{
v_p(D_\infty)=
\begin{cases}
\varepsilon_p,&c_p>0,\\
0,&c_p=0.
\end{cases}}
\tag{5.2}
\]

因此 `D_infty` 精确读取：**仍有未被 `N_c` 吃掉的 main denominator depth的 primes 上，完整的 numerator excess tail。**

如果 `n>=h`，则 `c_p=0`；即使 `alpha` 还有更深 p-depth，它也已不属于可用于关闭 main `C_L` 的 unpaid core，故不会进入 ladder。

---

## 6. 第一层之后的 canonical deficit / overflow 分解

第一层为

\[
G_{\rm exc}=D_1.
\]

定义 denominator residual

\[
\boxed{
C_{\rm rem}:=\frac{C_N}{G_{\rm exc}},}
\tag{6.1}
\]

以及 full supported tail 相对第一层的 overflow

\[
\boxed{
R_{\rm over}:=\frac{D_\infty}{G_{\rm exc}}.}
\tag{6.2}
\]

逐 prime：

\[
\boxed{
v_p(C_{\rm rem})
=\max(c_p-\varepsilon_p,0),}
\tag{6.3}
\]

\[
\boxed{
v_p(R_{\rm over})
=\max(\varepsilon_p-c_p,0).}
\tag{6.4}
\]

因此

\[
\boxed{
\gcd(C_{\rm rem},R_{\rm over})=1
}
\tag{Deficit-overflow-separation}
\]

在 main support 上严格成立。

这给出最终三分：

\[
\boxed{
\begin{array}{c|c}
\varepsilon_p<c_p
&\text{留下 unpaid denominator deficit }c_p-\varepsilon_p\\
\varepsilon_p=c_p
&\text{该 prime 在第一层恰好完全匹配}\\
\varepsilon_p>c_p
&\text{留下 numerator overflow }\varepsilon_p-c_p.
\end{array}}
\tag{6.5}
\]

其中 numerator overflow 已经超出原 `C_N` 可支付的 main depth，不能再拿来重复计算 `C_L` closure。

---

## 7. 三条 reader 不能当三份独立 obstruction

`Reader-ladder-equality` 是一个必须保留的 no-double-count 审计。

虽然

\[
A_N,
\qquad
\Lambda_{\rm ax},
\qquad
\Lambda_1
\]

分别来自：

- 真实 concatenated numerator；
- axis/two-block Gaussian companion；
- secondary norm quotient；

但在 main core 上它们的 p-depth函数都恒等于同一个

\[
\varepsilon_p=\max(v_p(\alpha)-v_p(N_c),0).
\]

所以：

\[
\boxed{
\text{三条 reader 是同一 pure excess tail 的不同坐标图，}
\text{不是三份可相加的 height。}}
\tag{Reader-no-triple-pay}
\]

特别地，单纯证明

\[
G_{\rm exc}\mid A_N,
\quad
G_{\rm exc}\mid\Lambda_{\rm ax},
\quad
G_{\rm exc}\mid\Lambda_1
\]

不能产生三倍 modulus surplus。

---

## 8. 真正剩下的 independent interface：small `R_0` remainder

虽然三条 tail reader 本身不独立，numerator reconstruction 仍给出一个不同性质的 **Archimedean-small remainder**：

\[
\boxed{
UA_0+R_0=g_0B10^dA_{12},
\qquad
\log R_0=o(S).}
\tag{8.1}
\]

令

\[
A_0^\circ:=\frac{A_0}{(A_0,N_c)}.
\tag{8.2}
\]

由命题 1.1，main prime 上

\[
v_p(A_0^\circ)=\varepsilon_p.
\]

所以所有 ladder target primes 同时满足

\[
\boxed{
g_0B10^dA_{12}\equiv R_0
\pmod{A_0^\circ_{\rm target}}.}
\tag{Small-remainder}
\]

这里右边只有 `10^{o(S)}` 高度；这与前三个 reader 的“同一 valuation shadow”不同，是后续 digit-shell separation 真正应该利用的接口。

但是 `(Small-remainder)` 单独还不能推出空性：模数的逆元可把小 `R_0` 映射到任意合法 `A_{12}` residue。必须再与一个不由 numerator reconstruction 重构的独立 residue/size condition 联立。

---

## 9. 当前 frontier

现在 full rational Good 的 pure excess 可用一条完全 canonical pipeline描述：

\[
\boxed{
\begin{aligned}
C_N&=C_L^{\rm main}/(C_L^{\rm main},N_c),\\
A_N&=\alpha/(\alpha,N_c),\\
D_k&=\gcd(C_N^k,A_N),\\
G_{\rm exc}&=D_1,\\
D_\infty&=\text{stable }C_N\text{-supported tail},\\
C_{\rm rem}&=C_N/G_{\rm exc},\\
R_{\rm over}&=D_\infty/G_{\rm exc},\\
(C_{\rm rem},R_{\rm over})&=1.
\end{aligned}}
\tag{9.1}
\]

`Lambda_ax` 与 `Lambda_1` 给相同 ladder，因此只作为交叉审计保留。

下一条真正可能推进 closure 的命题应直接针对 `(Small-remainder)`：寻找 `A_0^circ_target` 上第二个独立、同样具有短 natural representative 的 residue。若只能再次推出 `Tail-axis`、`Radius-resultant-collapse`、`Nc1-elim` 或 clean-source 的同一 reconstruction，则应判为重复投影。

---

## 10. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`C_N^k` excess gcd ladder；`D_1=G_exc`；stable `D_infty`；canonical deficit/overflow separation；三条 reader ladder 在 main support 上相同；`R_0` small-remainder interface。
- **`失效/降级`**：把 `A_N/Lambda_ax/Lambda_1` 三条 reader 当作三份独立 height；把 `R_over` 再计入原 `C_N` 的可支付深度。
- **`待证`**：第二个 independent short residue；axis-normalized digit-shell separation；`log G_exc=o(S)` 或其它 strict bound；full rational Good emptiness；genuine-Gaussian closure；DD 全局空性。

---

<a id="source-good-prefix-crt-location-audit"></a>

> 整合来源：`good-prefix-crt-location-audit.md`

# DD full-rational Good 的 prefix CRT location audit

> **依赖：** [`good-prefix-polarization.md`](good-genuine-ledger.md#source-good-prefix-polarization) 与 [`frontier.md`](frontier.md) 的 `R0-A12`、clean source、`QCRT-exact`、axis factorization、`A12-second+`。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文审计上一文件留下的唯一 leading-block residue `a_1` 的 Archimedean location。结论是：`Prefix-QCRT` 与 `Prefix-GCRT` 都是真实且联合 period 超过 `a_1` 窗口的 congruence，但它们的 natural exact representatives 完全由已有 numerator reconstruction / clean-source / axis factorization重构；两条 prefix residual 之间还有一个 exact compatibility identity，其差值正是 `U q_c^2 L_clean`。因此现有 full-rational parent identities 本身不能把“至多一个 `a_1`”升级为 emptiness。
>
> 这封闭的是 **full-rational Good 中继续展开现有 Q/G CRT parents 以寻找短自然代表** 的路线；它不证明 `a_1` 不存在，也不关闭 DD。

---

## 1. 基线与 prefix 变量

沿用

\[
A_{12}=10^{n_2}a_1+a_2.
\]

为简洁记

\[
t:=10^{n_2},
\qquad
D:=10^d,
\qquad
F:=5^T.
\tag{1.1}
\]

并保留

\[
X=2^HZ,
\qquad
\Sigma=X+FU,
\qquad
V=X-FU.
\tag{1.2}
\]

因此

\[
\boxed{\Sigma-X=FU.}
\tag{1.3}
\]

numerator reconstruction 的 terminal form 为

\[
\boxed{
\Sigma R_0
=g_0(BDVA_{12}-Ua_3).
}
\tag{R0-A12}
\]

而 clean source 与 `a_3` bridge 分别为

\[
VA_0-FR_0=q_c^2L_{\rm clean},
\tag{1.4}
\]

\[
g_0a_3=VA_0-2FR_0.
\tag{1.5}
\]

两式相减立刻得到

\[
\boxed{
q_c^2L_{\rm clean}=g_0a_3+FR_0.
}
\tag{Source-a3}
\]

这条 exact identity 是下面 location audit 的关键。

---

## 2. Prefix-QCRT 的 natural representative

将

\[
A_{12}=ta_1+a_2
\]

代入 `(R0-A12)`：

\[
\begin{aligned}
g_0BDVt a_1
&=\Sigma R_0+g_0Ua_3-g_0BDVa_2.
\end{aligned}
\tag{2.1}
\]

定义 Q-side natural residual

\[
\boxed{
H_Q:=XR_0-g_0BDVa_2.
}
\tag{2.2}
\]

由于

\[
C_*:=\frac{g_0a_2B}{2},
\]

还可写成

\[
\boxed{
H_Q=XR_0-2DVC_*.
}
\tag{2.3}
\]

从 `(2.1)` 减去 `(2.2)`，使用 `(1.3)`：

\[
\begin{aligned}
g_0BDVt a_1-H_Q
&=(\Sigma-X)R_0+g_0Ua_3\\
&=U(FR_0+g_0a_3).
\end{aligned}
\]

最后用 `(Source-a3)`：

\[
\boxed{
g_0BDVt a_1-H_Q
=Uq_c^2L_{\rm clean}.}
\tag{Prefix-Q-exact}
\]

因此模 `q_c^2`：

\[
\boxed{
g_0BDVt a_1
\equiv
XR_0-2DVC_*
\pmod{q_c^2}.}
\tag{Prefix-Q-natural}
\]

删去 coefficient exceptional core 后，这就是上一文件的 `Prefix-QCRT`。

关键是 `(Prefix-Q-exact)` 已经精确告诉我们这个 residue 的 natural parent：它与真正的 `a_1` 项之间相差

\[
Uq_c^2L_{\rm clean},
\]

即已有 clean-source quotient 的整数倍。

所以若仅使用

- `R0-A12`；
- `Source-a3`；
- `QCRT-exact`

继续化简 `Prefix-QCRT`，不会产生一个独立短代表；所有 rearrangement 都只是 `(Prefix-Q-exact)` 的重写。

**状态：`失效/降级`，若把 `H_Q` 当作新的 independent short residue。**

---

## 3. Prefix-GCRT 的 exact parent同样完全显式

full rational-contact 中取

\[
\Gamma:=\Pi_+\overline{\Pi_-},
\qquad
N(\Gamma)=E,
\qquad
V=Ee_0,
\tag{3.1}
\]

以及 axis factorization

\[
\boxed{
C_*+iR_0=\Gamma\overline K.
}
\tag{3.2}
\]

已有

\[
\boxed{
M_+
:=
\frac{\Sigma C_*-ig_0Ua_3}{\Gamma}
\in\mathbf Z[i],
}
\tag{3.3}
\]

和 exact second-order identity

\[
\boxed{
\Sigma\overline K-M_+
=ig_0BDe_0\overline\Gamma A_{12}.
}
\tag{A12-second+}
\]

代入

\[
A_{12}=ta_1+a_2
\]

并定义 suffix-deleted Gaussian residual

\[
\boxed{
H_G
:=
\Sigma\overline K-M_+
-ig_0BDe_0\overline\Gamma a_2.
}
\tag{3.4}
\]

则直接得到

\[
\boxed{
H_G
=ig_0BDe_0\overline\Gamma t a_1.
}
\tag{Prefix-G-exact}
\]

模 `Gamma` 后正是 `Prefix-GCRT` 的 parent。

这里同样没有 hidden Archimedean saving：`H_G` 作为 natural exact representative 本身就等于 `a_1` 主项乘上完整 Gaussian coefficient。只有在模 `Gamma` 以后它才成为 residue class；仅靠 `(A12-second+)` 与 axis factorization不能把该 class 的最小代表压短。

---

## 4. 两条 prefix residual 的 exact compatibility

由于

\[
V=E e_0
=\Gamma\overline\Gamma e_0,
\]

从 `(Prefix-G-exact)` 得

\[
-i\Gamma H_G
=g_0BDVt a_1.
\tag{4.1}
\]

与 `(Prefix-Q-exact)` 联立，立即得到

\[
\boxed{
-i\Gamma H_G-H_Q
=Uq_c^2L_{\rm clean}.}
\tag{Prefix-QG-compat}
\]

这条 identity 很重要，因为它区分了两种“独立性”：

1. **period 独立性**：`q_c^2` 与 rational kernel `E=N(\Gamma)` 的 overlap 只有 `10^{o(S)}`，所以 `QCRT+GCRT` 的联合 period 确实达到
   \[
   10^{1.617767155236\ldots S+o(S)};
   \]
   因而 fixed slow data 下 `a_1` 至多一个。
2. **natural-representative 独立性**：`(Prefix-QG-compat)` 显示两条 exact parent residual 并非两个自由的短整数；它们之间的差恰由已有 clean source `Uq_c^2L_clean` 支付。

所以不能从“两个 periods 几乎互素”直接推成“两个 natural short representatives 独立”。

---

## 5. `QCRT-exact` 本身也可由同一两条 parent 恢复

已有 QCRT exact parent：

\[
\Sigma q_c^2L_{\rm clean}
=g_0(FBDVA_{12}+Xa_3).
\tag{5.1}
\]

将 `(Source-a3)` 代入左边：

\[
\Sigma(g_0a_3+FR_0)
=g_0(FBDVA_{12}+Xa_3).
\]

移项并使用

\[
\Sigma-X=FU
\]

后，约去 `F`，得到

\[
\Sigma R_0
=g_0(BDVA_{12}-Ua_3),
\]

正是 `(R0-A12)`。

因此：

\[
\boxed{
\text{`QCRT-exact`}
\Longleftrightarrow
\text{`R0-A12` + `Source-a3`}
}
\tag{Q-parent-equivalence}
\]

在当前 terminal identities 下成立。

这进一步说明 Q-side location不能从自己的 exact parent 中再榨出独立的 Archimedean约束。

---

## 6. G-side exact parent同样只是 axis quotient后的 reconstruction

由 `(3.2)`：

\[
\overline K=\frac{C_*+iR_0}{\Gamma}.
\]

把它和 `(3.3)` 代入 `(3.4)`：

\[
\begin{aligned}
\Gamma H_G
&=\Sigma(C_*+iR_0)
-(\Sigma C_*-ig_0Ua_3)
-i g_0BD e_0\Gamma\overline\Gamma a_2\\
&=i\left(
\Sigma R_0+g_0Ua_3-g_0BDVa_2
\right).
\end{aligned}
\]

由 `(2.1)`：

\[
\boxed{
\Gamma H_G
=i g_0BDVt a_1.
}
\tag{6.1}
\]

正好恢复 `(Prefix-G-exact)`。

所以 G-side 所谓 second-order parent，是把同一 numerator reconstruction 先沿 axis Gaussian factor `Gamma` 做一次 quotient 后再读取；它在 p-adic period 上是真实的新层，但 exact Archimedean representative 没有脱离 reconstruction algebra。

---

## 7. full-rational prefix location 的 no-go 边界

现在可以严格记录：

\[
\boxed{
\begin{array}{l}
\text{Prefix-QCRT natural parent}
\;\leftrightarrow\;
\text{reconstruction + clean source},\\[1mm]
\text{Prefix-GCRT natural parent}
\;\leftrightarrow\;
\text{axis quotient of the same reconstruction},\\[1mm]
-i\Gamma H_G-H_Q
=Uq_c^2L_{\rm clean}.
\end{array}}
\tag{7.1}
\]

所以已有 parents 足以给出：

\[
\boxed{\#\{a_1\}\le1}
\]

但不足以给出：

\[
\boxed{\#\{a_1\}=0.}
\]

任何声称从 `H_Q,H_G` 的“同时短”直接得到矛盾的证明，都必须先提供一个**不来自** `R0-A12` / `Source-a3` / axis factorization 的独立 Archimedean bound；否则会由 `(Prefix-QG-compat)` 重复计算同一 source payer。

**状态：当前 full-rational Q/G parent algebra 的 location route `失效/降级`。**

---

## 8. 方法切换

此前 continuation 已多次证明：

- first-order rational determinants critical；
- local higher Gaussian resultants退回 hidden square；
- short-residue local candidates退回 `C_L` carry / `N(Delta_1)` / axis baseline；
- 本文又证明 Q/G unique-lift 的 natural representatives退回 reconstruction / clean source。

因此 full-rational Good 的已知 local + prefix algebra 在当前变量系统下已经形成闭包。后续若没有真正外部的 Archimedean digit theorem，不应继续制造同一组 parent identities 的 eliminant。

下一主攻方向改为 frontier 中仍独立开放的

\[
\boxed{
\text{genuine-Gaussian split-prime / digit-shell branch}.}
\]

那里正线性 main core 不满足 rational sign degeneration，因而不会自动落回本文件的 Q/G rational-contact parent sheet。

---

## 9. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`Source-a3`；`Prefix-Q-exact`；`Prefix-G-exact`；`Prefix-QG-compat`；`Q-parent-equivalence`；G-parent reconstruction audit。
- **`失效/降级`**：从现有 Q/G exact parents内部寻找第二个 independent short natural representative；把 period independence误当 natural-representative independence。
- **`待证`**：外部 Archimedean digit-window theorem 若存在；genuine-Gaussian split-prime / digit-shell closure；DD 全局空性。

---

<a id="source-good-prefix-polarization"></a>

> 整合来源：`good-prefix-polarization.md`

# DD full-rational Good 的 prefix polarization 与 leading-block CRT

> **依赖：** [`frontier.md`](frontier.md) 的 one-channel reduction、full-rational moving-core counting、`QCRT` / `GCRT+`，以及统一符号中
> \[
> A_{12}=a_1 10^{n_2}+a_2,
> \qquad S=m_1+m_2.
> \]
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文不新增 local Gaussian resultant；它把已有 `A12` 唯一 CRT lift 的十进制结构进一步定位到第一 numerator block `a1`。
>
> 核心结论是：full-rational frontier 已强迫前两块发生极端互补极化
> \[
> (n_1,m_1,n_2,m_2)
> =
> (S,0,0,S)+o(S),
> \]
> 因而 `A12` 的 suffix `a2` 只有 subexponential 位长。把 suffix 条件
> \[
> A_{12}\equiv a_2\pmod{10^{n_2}}
> \]
> 加到 `QCRT+GCRT+` 上只增加 `o(S)` 的 effective modulus，不能凭 modulus 高度本身把“至多一个”升级为 emptiness。另一方面，两条 CRT 可等价地下推为 `a1` 的 residue，联合有效 period 仍为
> \[
> 10^{1.617767155236\ldots S+o(S)},
> \]
> 而 `a1` 只有 `S+o(S)` 位，因此真正未决的 digit-shell 已缩成 **唯一 leading-block residue 的 Archimedean location**。

---

## 1. 已有 frontier 输入

沿用

\[
S=m_1+m_2.
\tag{1.1}
\]

one-channel reduction 已证明

\[
\boxed{m_2=S+o(S),}
\tag{1.2}
\]

并且

\[
b_2=C_L\cdot10^{o(S)}
\]

按 logarithmic height理解。

full-rational moving-core counting 的输入中已经使用并证明：

\[
\boxed{
\log a_2=o(S),
\qquad
\log g_0=o(S),
\qquad
\log R_0=o(S).
}
\tag{1.3}
\]

另一方面 second-order `A12` CRT 段给出

\[
\boxed{\log A_{12}=S+o(S).}
\tag{1.4}
\]

统一定义为

\[
\boxed{
A_{12}=a_1 10^{n_2}+a_2,
}
\tag{1.5}
\]

其中 `n_i` 是 `a_i` 的十进制位数。

---

## 2. 第二 numerator block 只有 `o(S)` 位

因为 `a_2` 是正整数且

\[
\log a_2=o(S),
\]

其十进制位数满足

\[
\boxed{n_2=o(S).}
\tag{2.1}
\]

这里 `log` 取何固定底数不影响 `o(S)` 结论。

所以 `A12` 的低位 suffix 模量只有

\[
\boxed{10^{n_2}=10^{o(S)}.}
\tag{2.2}
\]

这已经说明：任何仅仅把

\[
A_{12}\equiv a_2\pmod{10^{n_2}}
\]

当作第三个 CRT period 的方案，在 leading order 上只能增加 `o(S)` 模高。

---

## 3. 第一 numerator block 占满整个 `S` 尺度

由 `(1.5)`，`A12` 的十进制位数精确为

\[
n_1+n_2.
\]

因此

\[
\log A_{12}=n_1+n_2+O(1).
\tag{3.1}
\]

结合 `(1.4)` 与 `(2.1)`：

\[
\boxed{n_1=S+o(S).}
\tag{3.2}
\]

于是 numerator prefix 的全部正线性 digit entropy 都在第一块 `a1`，而 `a2` 只是 subexponential suffix。

---

## 4. denominator 两块发生完全相反的极化

由

\[
S=m_1+m_2
\]

与 `(1.2)`：

\[
\boxed{m_1=o(S).}
\tag{4.1}
\]

因此前两块的 digit-length profile 为

\[
\boxed{
\begin{array}{c|cc}
&\text{numerator digits}&\text{denominator digits}\\ \hline
1& S+o(S)&o(S)\\
2& o(S)&S+o(S).
\end{array}}
\tag{Block-polarization}
\]

等价地，对 surplus

\[
s_i=n_i-m_i
\]

有

\[
\boxed{
s_1=S+o(S),
\qquad
s_2=-S+o(S).
}
\tag{4.2}
\]

这与 DD 的 `d_3`-dominant surplus simplex 相容：前两块的正、负 surplus 在 leading order 精确互相抵消。

这个极化此前散落在 one-channel counting 的输入中；本文把它显式提升为后续 digit-shell 的规范 frontier 数据。

---

## 5. suffix CRT 不增加正线性 modulus surplus

已有两条 `A12` residues：

1. rational `QCRT`，有效 period
   \[
   M_Q=q_c^2/10^{o(S)},
   \qquad
   \log M_Q
   =0.617767155236\ldots S+o(S);
   \]
2. Gaussian `GCRT+` 对 rational integer `A12` 的有效 period
   \[
   M_G=E/10^{o(S)},
   \qquad
   \log M_G=S+o(S).
   \]

并且

\[
(M_Q,M_G)=10^{o(S)}.
\]

所以联合 effective period 为

\[
\boxed{
M_{QG}
=10^{1.617767155236\ldots S+o(S)}.
}
\tag{5.1}
\]

现在再加入 exact decimal suffix

\[
A_{12}\equiv a_2\pmod{10^{n_2}}.
\tag{5.2}
\]

main `M_QM_G` 与 `10` 的 overlap 已被 coefficient exceptional core 删除，而

\[
\log 10^{n_2}=o(S).
\]

故三者的联合 modulus 仍只有

\[
\boxed{
\log\operatorname{lcm}(M_Q,M_G,10^{n_2})
=1.617767155236\ldots S+o(S).
}
\tag{Suffix-no-surplus}
\]

因此 suffix condition 不能靠“再加一个 decimal modulus”产生新的正线性 surplus。

**状态：`失效/降级`**，若把 `10^{n_2}` 当成第三份 leading-order CRT height。

---

## 6. 两条 CRT 可直接下推到 `a1`

虽然 suffix 模高很小，它可以把变量从 `A12` 换成真正的 leading block `a1`。

由

\[
A_{12}=10^{n_2}a_1+a_2
\]

代入 `QCRT`：

\[
K_Q(10^{n_2}a_1+a_2)
\equiv R_Q
\pmod{M_Q},
\tag{6.1}
\]

其中

\[
K_Q=5^TB10^dV
\]

而 `R_Q=-Xa_3`；删除既有 coefficient exceptional core 后，`K_Q10^{n_2}` 是 `M_Q`-unit。因此得到唯一的

\[
\boxed{
a_1\equiv\rho_Q\pmod{M_Q}.}
\tag{Prefix-QCRT}
\]

同理，将

\[
A_{12}=10^{n_2}a_1+a_2
\]

代入 Gaussian congruence `GCRT+`：

\[
i g_0B10^de_0\overline\Gamma
(10^{n_2}a_1+a_2)
\equiv
\Sigma\overline K-M_+
\pmod\Gamma.
\tag{6.2}
\]

因为 `10` 与 main `Gamma` 互素，乘上 `10^{n_2}` 不改变从 rational integers 到 `Z[i]/(Gamma)` 的 kernel；删除 coefficient exceptional core 后得到

\[
\boxed{
a_1\equiv\rho_G\pmod{M_G}}
\tag{Prefix-GCRT}
\]

的 rational effective period 描述。

所以 `QCRT+GCRT+` 的联合 residue 可以完全转写为 `a1` 的 residue，且 period 高度不变：

\[
\boxed{
\log M_{\rm pref}
=1.617767155236\ldots S+o(S).
}
\tag{6.3}
\]

---

## 7. `a1` 也至多只有一个 candidate

由 `(3.2)`：

\[
\log a_1=S+o(S).
\]

而

\[
\log M_{\rm pref}
=1.617767155236\ldots S+o(S).
\]

因此 sufficiently large frontier 上

\[
0<a_1<M_{\rm pref}.
\]

所以 fixed terminal denominator-tail / axis data 与 fixed slow suffix `a2` 下：

\[
\boxed{\#\{a_1\}\le1.}
\tag{Prefix-unique}
\]

这与旧的 `#\{A12\}\le1` 在计数上等价，但语义更强：

\[
\boxed{
\text{唯一 CRT lift 的全部正线性十进制自由度都在 leading block }a_1.
}
\tag{Leading-block-location}
\]

`a2` 只改变该 residue 的 `10^{o(S)}` 级 slow-data fiber。

---

## 8. 第一 denominator block 也只能提供 `o(S)` 的附加筛选

由 `(4.1)`：

\[
\log b_1=o(S).
\]

因此 reducedness

\[
(a_1,b_1)=1
\]

以及任何只使用 `b1` 的 fixed congruence / divisor condition，最多贡献 `o(S)` 的 modulus / entropy。

所以在 leading order 上，不能期待用

- `A12` 的短 suffix `a2`；
- 第一 denominator block `b1`；
- 或它们的有限组合

给现有 `1.617767...S` CRT 再增加一份正线性 modulus surplus。

真正需要的是 **location**：证明 `(Prefix-QCRT)+(Prefix-GCRT)` 指定的唯一 residue `rho_pref` 不落在合法 `n1=S+o(S)` digit interval，或与一个来自大尺度对象的独立 sign / order / interval condition 冲突。

---

## 9. 更新后的 full-rational digit-shell target

经过本文，旧目标

\[
\text{“定位唯一 }A_{12}\text{ CRT lift”}
\]

可进一步收紧为

\[
\boxed{
\text{定位唯一 leading numerator block }a_1
\text{ 的 CRT residue。}
}
\tag{9.1}
\]

可用数据分成：

- **large-period arithmetic**：`QCRT + GCRT+`，总有效高度 `1.617767...S`；
- **slow suffix data**：`a2,n2,b1,m1,g0,R0,...=10^{o(S)}`；
- **合法 interval**：`a1` 必须是恰有 `n1=S+o(S)` 位的正整数；
- **reducedness**：`(a1,b1)=1`，但 `b1` 只有 subexponential height。

因此下一步若继续 full-rational Good，不应再增加 suffix modulus；应直接研究 `rho_pref` 的 Archimedean representative / sign / digit interval。

若该 representative 完整展开后再次只等价于 `R0-A12`、carry 或 clean-source reconstruction，则 full-rational digit-shell 的 algebraic elimination也已闭包，应转 genuine-Gaussian branch。

---

## 10. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`n2=o(S)`、`n1=S+o(S)`、`m1=o(S)`、`m2=S+o(S)` 的 block polarization；suffix modulus 只有 `10^{o(S)}`；`QCRT/GCRT+` 可无损下推为 `a1` residues；`a1` 至多一个 candidate。
- **`失效/降级`**：把 `A12≡a2 (mod 10^{n2})` 或 `b1`-based conditions 当作新的正线性 CRT height。
- **`待证`**：唯一 prefix residue 的合法 digit-window exclusion；`log G_exc=o(S)`；full rational Good emptiness；genuine-Gaussian closure；DD 全局空性。

---

<a id="source-good-radius-excess"></a>

> 整合来源：`good-radius-excess.md`

# DD full-rational Good 的 canonical radius-excess

> **依赖：** [`frontier.md`](frontier.md) 中 continuation 的 `Radius-split`、`Secondary=Radius=Concat`、`Slot-RJ`、`Slot-JK`、`Nc1-elim`、`Good-cofactor-unit` 与 decimal remainder/carry 恒等式。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文只处理假想
> \[
> \frac{n_3}{S}\to 6.308883577618\ldots
> \]
> 的 full rational-contact Good 主质量。本文证明：此前末端看似分开的 **equal-depth radius cancellation** 与 **pure-radius cancellation**，在扣除 `gcd(C_L,H_R,N_c)` 的共同深度后其实是同一个 normalized unit-unit excess。由此得到一个 canonical 全局 excess 模数 `G_exc`，并证明 baseline 与 `H_J` 主槽逐素数分离。本文还记录一个 exact decimal no-go：把 `Top-residue` 与 `alpha` 直接相加消元只会精确退回 numerator reconstruction。
>
> 本文不证明 DD frontier emptiness，也不处理 genuine-Gaussian 主支。

---

## 1. main prime 的现有局部账本

沿用 `frontier.md` 的 full rational-contact Good 约定。删去 coefficient overlap、conjugate overlap、Bad mass 等总高度为 `o(S)` 的 exceptional core 后，固定一个 main prime-power

\[
p^h\Vert C_L,
\qquad p=\pi\bar\pi,
\]

并按对应 sign channel 选择

\[
\pi^h\Vert\Pi.
\]

记

\[
r_p:=v_p(H_R),
\qquad
n_p:=v_p(N_c),
\qquad
j_p:=v_p(H_J).
\tag{1.1}
\]

`frontier.md` 的 slot theorem 给出，在所选 channel 上

\[
\boxed{
\min(r_p,j_p)=0,
\qquad
\min(j_p,n_p)=0.
}
\tag{1.2}
\]

这里第二式使用了

\[
n_p=v_p(N_c)=\bar k
\]

与 `Slot-JK`；另一 sign channel 完全对称。

另一方面，`Radius-split` 给出

\[
\boxed{
a_p^{\rm raw}=\min(r_p,n_p)+\varepsilon_p,}
\tag{1.3}
\]

其中

\[
\varepsilon_p\ge0,
\qquad
\boxed{
\varepsilon_p>0\Longrightarrow r_p=n_p.}
\tag{1.4}
\]

而 `Secondary=Radius=Concat` 把同一 main depth 识别为真实拼接分子

\[
\alpha=A_{12}10^{n_3}+a_3
\]

中的深度。因此在 main `C_L` 可见范围内可写成

\[
\boxed{
\min\{h,v_p(\alpha)\}
=
\min\{h,a_p^{\rm raw}\}.
}
\tag{1.5}
\]

本文只使用 `(1.2)`--`(1.5)`，不重新构造任何 Gaussian quotient。

---

## 2. canonical baseline / excess 分解

定义截断的 radius depth

\[
\boxed{
a_p:=\min\{h,v_p(\alpha)\},}
\tag{2.1}
\]

共同 cofactor baseline

\[
\boxed{
b_p:=\min\{h,r_p,n_p\},}
\tag{2.2}
\]

以及 excess depth

\[
\boxed{
x_p:=a_p-b_p.}
\tag{2.3}
\]

由 `(1.3)`--`(1.5)`，

\[
a_p
=
\min\{h,\min(r_p,n_p)+\varepsilon_p\}
\ge
\min\{h,r_p,n_p\}
=b_p.
\]

故

\[
\boxed{x_p\ge0.}
\tag{2.4}
\]

于是每个 main prime 的 radius depth 被 canonical 地分成

\[
\boxed{
\text{radius depth}
=
\text{common }(H_R,N_c)\text{ baseline}
+
\text{excess}.
}
\tag{2.5}
\]

这里没有人为选择 payer；`b_p` 由三个整数 `C_L,H_R,N_c` 的 gcd 唯一确定。

---

## 3. 核心引理：任何正 excess 在正规化后都是 pure-radius

### 命题 3.1

若

\[
\boxed{x_p>0,}
\tag{3.1}
\]

则必有

\[
\boxed{
r_p=n_p=b_p<h.}
\tag{3.2}
\]

因此除去共同因子 `p^{b_p}` 后，`H_R` 与 `N_c` 两个 cofactor 都成为 `p`-unit；剩余的 main radius depth只能来自 `Nc1-elim` 两个 unit 项之间的 cancellation。

### 证明

若

\[
r_p\ne n_p,
\]

则由 `(1.4)` 的逆否命题

\[
\varepsilon_p=0.
\]

于是

\[
a_p
=
\min\{h,\min(r_p,n_p)\}
=b_p,
\]

与 `x_p>0` 矛盾。因此

\[
r_p=n_p=:t.
\tag{3.3}
\]

若

\[
t\ge h,
\]

则

\[
b_p=h
\]

且由 `a_p\le h` 再次得到 `x_p=0`，矛盾。故

\[
t<h.
\]

于是

\[
b_p=t=r_p=n_p<h,
\]

即得 `(3.2)`。

现在使用

\[
\widetilde r^{\,2}5^{4T-2m}N_c
-g_0^2a_2^22^{2m-4}H_R
=
\frac{C_L}{E}N(\Delta_1).
\tag{Nc1-elim}
\]

在 main coefficient-unit regime 中，两项显式 coefficient 与 `C_L/E` 的相关 overlap 已删入 exceptional core。由 `(3.2)` 可从左侧两项共同提出恰好 `p^{b_p}`；提出后两个剩余项都是 `p`-units。其后仍存在的 `p`-depth就是 unit-unit cancellation depth，而 main `C_L` 能看到的剩余部分恰为 `x_p`。

故 `(3.1)` 下没有第二种 normalized mechanism。证毕。

---

## 4. equal-depth 与 pure-radius 的假分叉消失

旧 slot ledger 将最后的困难写成两类：

1. `r_p=n_p>0` 后继续发生 equal-depth cancellation；
2. `r_p=n_p=0` 时发生 pure-radius cancellation。

命题 3.1 表明，这一区分只发生在**扣除 common baseline 之前**。

若第一类产生真正的 main excess，则

\[
r_p=n_p=b_p<h.
\]

除以 `p^{b_p}` 后立刻变为

\[
v_p(H_R/p^{b_p})
=
v_p(N_c/p^{b_p})
=0,
\]

而 excess 仍由两个 units 的差产生。

第二类只是 `b_p=0` 的同一情况。

因此得到：

\[
\boxed{
\text{equal-depth excess}
\quad\text{与}\quad
\text{pure-radius}
\quad\text{在 canonical baseline normalization 后是同一 local slot。}
}
\tag{Pure-excess-local}
\]

这将 `frontier.md` 末端的

\[
\text{equal-depth }(H_R,N_c)\text{ cancellation}
\;\cup\;
\text{pure numerator-shell contact}
\]

压成一个单一对象：**normalized pure excess**。

---

## 5. 全局 canonical excess 模数

令 `C_L^{\rm main}` 表示删去上述 `o(S)` exceptional prime-power 后的 main divisor：

\[
C_L^{\rm main}
:=
\prod_{p^h\Vert C_L,\ p\in\mathcal P_{\rm main}}p^h,
\qquad
\log\frac{C_L}{C_L^{\rm main}}=o(S).
\tag{5.1}
\]

定义真实 radius modulus

\[
\boxed{
G_{\rm rad}
:=
\gcd(C_L^{\rm main},\alpha),}
\tag{5.2}
\]

共同 baseline

\[
\boxed{
G_{\rm base}
:=
\gcd(C_L^{\rm main},H_R,N_c),}
\tag{5.3}
\]

以及 quotient

\[
\boxed{
G_{\rm exc}
:=
\frac{G_{\rm rad}}{G_{\rm base}}.
}
\tag{5.4}
\]

由第 2 节逐素数有 `b_p<=a_p`，故 `(5.4)` 确为正整数，而且

\[
\boxed{
G_{\rm rad}=G_{\rm base}G_{\rm exc}.}
\tag{5.5}
\]

更精确地，

\[
v_p(G_{\rm base})=b_p,
\qquad
v_p(G_{\rm exc})=x_p.
\tag{5.6}
\]

因此命题 3.1 立即全局化为

\[
\boxed{
\gcd\!\left(
G_{\rm exc},
\frac{H_R}{G_{\rm base}}
\right)=1,
\qquad
\gcd\!\left(
G_{\rm exc},
\frac{N_c}{G_{\rm base}}
\right)=1.
}
\tag{Pure-excess-global}
\]

同时

\[
\boxed{
G_{\rm exc}
\mid
\frac{\alpha}{G_{\rm base}}.
}
\tag{5.7}
\]

所以 `G_exc` 是一个完全由已有 terminal integers 定义的 **primitive digit-shell modulus**：它整除真实拼接 numerator，但已经与 normalized `H_R`、`N_c` 两个旧 payer 都互素。

这正是后续 strict digit-shell lemma 应当作用的对象。

---

## 6. baseline 与 `next-J` 主槽严格分离

由 `(1.2)`：如果

\[
b_p>0,
\]

则

\[
r_p>0,
\qquad n_p>0.
\]

于是 `Slot-RJ` 与 `Slot-JK` 都强迫

\[
j_p=0.
\]

因此

\[
\boxed{
\gcd(G_{\rm base},H_J)=1
}
\tag{Baseline-J-separation}
\]

在 `C_L^{\rm main}` 上逐素数严格成立。

把 exceptional core 放回去时，这可写为高度形式

\[
\boxed{
\log\gcd(G_{\rm base}^{\rm full},H_J)=o(S),
}
\tag{6.1}
\]

其中 `G_base^{full}` 表示未预先删 exceptional prime-power 的对应 gcd。

这说明 common `(H_R,N_c)` payer 与 `next-J` payer 不能支付同一份 main prime mass。

---

## 7. `Good-cofactor-unit` 在两个基础 slot 上是自动的

Good 已被翻译成

\[
\boxed{
p\nmid d^2N_c+R_0^2H_J}
\tag{7.1}
\]

对每个 main prime 成立。

在 coefficient-unit convention 下：

- 若 `p|G_base`，则 `p|N_c` 且第 6 节给 `p\nmid H_J`，所以 `(7.1)` 模 `p` 退化为非零的 `R_0^2H_J`；
- 若 `j_p>0`，则 `(1.2)` 给 `n_p=0`，所以 `(7.1)` 模 `p` 退化为非零的 `d^2N_c`。

因此 `Good-cofactor-unit` 对这两个 mutually-exclusive 基础槽本身不提供新的正线性 height 收费。

这解释了为什么仅把 `NcU-elim` 再与 slot capacity 相加仍会达到临界：真正可能携带新信息的是已经除掉 baseline 后的 `G_exc`，而不是 `(7.1)` 本身。

> **状态：**这一节是 no-go / allocation 审计，不是 closure。

---

## 8. `Top-residue + alpha` 的直接消元精确退回 numerator reconstruction

这一节记录另一个容易重复尝试的方向。

定义

\[
\Sigma:=2^HZ+5^TU,
\qquad
V:=2^HZ-5^TU,
\]

以及

\[
R_{\rm dec}
:=B10^dVA_{12}-Ua_3.
\tag{8.1}
\]

已有

\[
\boxed{
R_{\rm dec}=\frac{\Sigma R_0}{g_0},
}
\tag{8.2}
\]

和

\[
\boxed{
g_0\alpha=\Sigma A_0.}
\tag{8.3}
\]

又因为

\[
n_3=m+d,
\qquad
\alpha=A_{12}10^{m+d}+a_3,
\]

以及 terminal phase

\[
10^m=2B5^T,
\]

直接计算：

\[
\begin{aligned}
R_{\rm dec}+U\alpha
&=B10^dVA_{12}-Ua_3
+U(A_{12}10^{m+d}+a_3)\\
&=B10^dA_{12}
\left(V+\frac{U10^m}{B}\right)\\
&=B10^dA_{12}(V+2\cdot5^TU)\\
&=\boxed{B10^dA_{12}\Sigma}.
\end{aligned}
\tag{8.4}
\]

将 `(8.2)`、`(8.3)` 代入 `(8.4)`：

\[
\frac{\Sigma}{g_0}(R_0+UA_0)
=B10^dA_{12}\Sigma.
\]

因为 `Sigma>0`，约去后恰得

\[
\boxed{
UA_0+R_0=g_0B10^dA_{12},
}
\tag{8.5}
\]

即已有 numerator reconstruction。

因此：

\[
\boxed{
\text{把 }Top\text{-residue 与 }\alpha\text{-repeat 通过 }R_{\rm dec}+U\alpha
\text{ 直接联立，不产生独立 congruence。}
}
\tag{Decimal-alpha-no-go}
\]

`Top-residue` 本身仍然是严格的 thin decimal window；这里只排除最直接的线性消元方式。若后续利用该 window，必须引入一个不由 `(8.2)`--`(8.5)` 重构的 primitive residue / size input。

---

## 9. 更新后的 Good radius frontier

本文把 Good 的 radius 侧整理成以下 canonical 图：

\[
\boxed{
G_{\rm rad}
=
G_{\rm base}G_{\rm exc},
}
\]

其中

\[
G_{\rm base}
=
\gcd(C_L^{\rm main},H_R,N_c)
\]

是已经由两个 cofactor payer 共同承担的 baseline，并与 `H_J` main slot 分离；真正未支付的 radius 信息全部进入

\[
\boxed{
G_{\rm exc}
=\frac{\gcd(C_L^{\rm main},\alpha)}
{\gcd(C_L^{\rm main},H_R,N_c)}.
}
\tag{9.1}
\]

对每个

\[
p\mid G_{\rm exc},
\]

在除去 `G_base` 后都有

\[
H_R/G_{\rm base},
\qquad
N_c/G_{\rm base}
\]

为 `p`-units；所以旧的 equal-depth excess 与 pure-radius 已经统一成一个 pure unit-unit cancellation。

因此 Good radius 的下一条合理目标可固定为：

> **Primitive excess digit-shell lemma（待证）**：证明在 full rational-contact Good frontier 上
> \[
> \log G_{\rm exc}=o(S),
> \]
> 或给出一个严格更强的界，使 `G_exc` 无法承载任何所需的正线性 main mass。

这个目标应直接使用 `G_exc | alpha/G_base` 的真实十进制位置，同时保持

\[
\gcd\!\left(G_{\rm exc},H_R/G_{\rm base}\right)
=
\gcd\!\left(G_{\rm exc},N_c/G_{\rm base}\right)=1.
\]

继续区分 “equal-depth excess” 与 “pure-radius” 已没有数学收益；继续把 `Top-residue` 与 `alpha` 做 `(8.4)` 型一阶消元也只会回到旧 reconstruction。

---

## 10. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：main radius depth 的 canonical `baseline + excess` 分解；`x_p>0 => r_p=n_p=b_p<h`；equal-depth excess 在 baseline normalization 后等价于 pure-radius；全局 `G_rad=G_base G_exc`；`G_exc` 与 normalized `H_R,N_c` 互素；`G_base` 与 `H_J` main slot 分离；`Decimal-alpha-no-go` exact identity。
- **`失效/降级`**：试图仅靠 `Good-cofactor-unit` 对 baseline / next-J 槽再次收费；通过 `R_dec+U alpha` 直接把 `Top-residue` 与 radius repeat 做线性消元。
- **`待证`**：primitive excess digit-shell lemma；full rational Good 的最终 emptiness；genuine-Gaussian split-prime / digit-shell closure；DD 全局空性与有效绝对高度界。

---

<a id="source-good-short-residue-audit"></a>

> 整合来源：`good-short-residue-audit.md`

# DD full-rational Good 的 short-residue audit 与 overflow 二次分层

> **依赖：** [`frontier.md`](frontier.md) 的 `CS` / `HS` / `R0-A12` / `Top-residue` / `Radius-resultant-collapse` / `Nc1-elim`，以及 [`good-axis-normalization.md`](good-genuine-ledger.md#source-good-axis-normalization)、[`good-excess-gcd-ladder.md`](good-genuine-ledger.md#source-good-excess-gcd-ladder)。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文继续只处理假想
> \[
> \frac{n_3}{S}\to 6.308883577618\ldots
> \]
> 的 full rational-contact Good 主质量，并删除总高度为 `o(S)` 的 coefficient / conjugate / Bad exceptional core。
>
> 本文做两件事：
>
> 1. 审计上一文件留下的“第二个 independent short residue”候选，证明三个最自然的局部候选分别退回 full rational carry、旧 `Delta_1` norm、旧 axis baseline，不能重复收费；
> 2. 将上一文件的 numerator overflow 再分成 **axis-reuse** 与 **deep overflow**，从而证明 `G_exc` 是 normalized numerator tail 中唯一真正面向尚未支付 `C_N` 深度的第一层。
>
> 本文仍不证明 `log G_exc=o(S)`，不关闭 full rational Good，也不关闭 DD。

---

## 1. 记号

令

\[
C:=C_L^{\rm main}.
\]

固定 main prime-power

\[
p^h\Vert C,
\qquad
n:=v_p(N_c).
\]

对 pure-excess 活跃 prime，沿用

\[
a:=v_p(A_0)=v_p(\alpha)=n+\varepsilon_p,
\qquad
\varepsilon_p>0.
\tag{1.1}
\]

并定义

\[
c_p:=\max(h-n,0),
\qquad
x_p:=\min(c_p,\varepsilon_p).
\tag{1.2}
\]

上一文件的 canonical objects 为

\[
G_{\rm ax}:=(C,N_c),
\qquad
C_N:=\frac{C}{G_{\rm ax}},
\tag{1.3}
\]

\[
A_N:=\frac{\alpha}{(\alpha,N_c)},
\tag{1.4}
\]

以及

\[
G_{\rm exc}:=(C_N,A_N).
\tag{1.5}
\]

逐 prime 有

\[
v_p(C_N)=c_p,
\qquad
v_p(A_N)=\varepsilon_p,
\qquad
v_p(G_{\rm exc})=x_p.
\tag{1.6}
\]

在真正的 `G_exc` target 上必有 `c_p>0`，故

\[
n<h.
\tag{1.7}
\]

---

## 2. `Top-residue` 在 main core 上不是第二条 residue

定义

\[
R_{\rm dec}
:=B10^dVA_{12}-Ua_3.
\tag{2.1}
\]

于是 exact identity 本身就是

\[
\boxed{
Ua_3+R_{\rm dec}
=B10^dVA_{12}.
}
\tag{2.2}
\]

由于

\[
C\mid V,
\]

立刻有

\[
\boxed{
Ua_3\equiv -R_{\rm dec}\pmod C.
}
\tag{2.3}
\]

因此当然也有

\[
Ua_3\equiv -R_{\rm dec}\pmod{G_{\rm exc}}.
\tag{2.4}
\]

另一方面 `Top-residue` 只是同一个 exact carry 在 decimal modulus 上的投影：

\[
Ua_3\equiv -R_{\rm dec}\pmod{10^d}.
\tag{2.5}
\]

所以若试图把 `(2.5)` 再投影到 `G_exc`，得到的不是第二个 p-adic residue；`(2.3)` 已经在完整 `C` 上给出了同一个 representative，而且它完全不需要 `alpha` repeat。

这可以用一个 exact compatibility identity写得更明显。由

\[
g_0B10^dA_{12}=UA_0+R_0,
\tag{2.6}
\]

以及

\[
g_0R_{\rm dec}=\Sigma R_0,
\qquad
\Sigma=V+2\cdot5^TU,
\tag{2.7}
\]

有

\[
\begin{aligned}
g_0(Ua_3+R_{\rm dec})
&=g_0B10^dVA_{12}\\
&=V(UA_0+R_0).
\end{aligned}
\tag{2.8}
\]

而使用

\[
g_0a_3=VA_0-2\cdot5^TR_0
\tag{2.9}
\]

展开左边也精确得到同一式。

所以：

\[
\boxed{
\text{`Top-residue` 的 main-}C\text{ 投影就是已有 }V\text{-contact，}
\text{不是 `G_exc` 的第二条 independent residue。}
}
\tag{Top-main-nogo}
\]

**状态：`失效/降级`。**

---

## 3. clean-source 的 square lift 确实存在

clean source 为

\[
\boxed{
VA_0=q_c^2L_{\rm clean}+5^TR_0.
}
\tag{CS'}
\]

由于 `G_exc|C|V`，又因为 `G_exc|A_N` 且 main target 上 `v_p(A_0)=n+epsilon_p>=x_p`，所以

\[
G_{\rm exc}\mid A_0.
\]

因此

\[
\boxed{
G_{\rm exc}^2
\mid
q_c^2L_{\rm clean}+5^TR_0.
}
\tag{Square-source}
\]

这是一条真实的 square-modulus congruence。注意这里的平方不是 Hensel 猜测，而只是来自两个独立整数因子

\[
G_{\rm exc}\mid V,
\qquad
G_{\rm exc}\mid A_0.
\]

在删除 clean-source exceptional core 后还可写成 unit synchronization

\[
q_c^2L_{\rm clean}
\equiv-5^TR_0
\pmod{G_{\rm exc}^2},
\tag{3.1}
\]

其中 target primes 不进入 `q_c L_clean R_0`。

看上去这很像新的 second-order short residue；下一节证明它仍然是旧 secondary norm 的投影。

---

## 4. `(Square-source)+HS` 精确退回 `Delta_1` norm

hidden square 为

\[
\boxed{
(C_LP_1)^2+P_0^2
=4\widetilde r^{\,2}5^TR_0L_{\rm clean},
}
\tag{HS}
\]

其中

\[
P_0=g_0a_2B\theta s.
\tag{4.1}
\]

因为 `G_exc|C_L`，模 `G_exc^2` 时 `(C_LP_1)^2` 消失。将 `(HS)` 乘以 `q_c^2`，再使用 `(Square-source)`，得到

\[
\boxed{
G_{\rm exc}^2
\mid
(q_cP_0)^2
+4\widetilde r^{\,2}5^{2T}R_0^2.
}
\tag{4.2}
\]

现在检查右边是不是新的 integer。

secondary Gaussian numerator 为

\[
\mathcal G_1
=g_0a_2\theta s\,2^{m-2}q_c
-i\widetilde rR_0\,5^{2T-m}
=\Pi\Delta_1,
\tag{4.3}
\]

而 terminal identity

\[
B=2^{m-1}5^{m-T}
\tag{4.4}
\]

给出

\[
\boxed{
2\,5^{m-T}\mathcal G_1
=q_cP_0-2i\widetilde r5^TR_0.
}
\tag{4.5}
\]

取范数：

\[
\boxed{
(q_cP_0)^2
+4\widetilde r^{\,2}5^{2T}R_0^2
=
4\,5^{2(m-T)}N(\mathcal G_1).
}
\tag{4.6}
\]

又因为

\[
\mathcal G_1=\Pi\Delta_1,
\qquad
N(\Pi)=C_L,
\]

故

\[
\boxed{
(q_cP_0)^2
+4\widetilde r^{\,2}5^{2T}R_0^2
=
4\,5^{2(m-T)}C_LN(\Delta_1).
}
\tag{Square-collapse}
\]

所以 `(4.2)` 并没有制造新的 second-order obstruction；它精确就是旧 `Delta_1` norm 的 smooth rescaling。

逐 target prime 也能直接看见这一点：

\[
v_p\bigl(N(\Delta_1)\bigr)=a=n+\varepsilon_p,
\]

于是 `(Square-collapse)` 右边的 p-depth 为

\[
h+a.
\]

而

\[
2x_p\le h+a
\]

只是

\[
x_p\le h,
\qquad
x_p\le a
\]

的直接和。因此 `G_exc^2` 的 divisibility 已完全被旧 `(C_L,N(Delta_1))` payer 覆盖。

结论：

\[
\boxed{
\text{clean-source square lift + hidden square}
\Longrightarrow
\text{旧 }\Delta_1\text{ norm，不能重复收费。}
}
\tag{Square-nogo}
\]

**状态：`失效/降级`。**

---

## 5. axis / radius-digital 的正交 companion 也只会回收 axis baseline

令

\[
Z_{\rm ax}:=C_*+iR_0,
\qquad
C_*:=\frac{g_0a_2B}{2},
\]

以及 radius digital carrier

\[
W:=a_2+iY,
\qquad
Y:=2\,10^dA_{12}.
\tag{5.1}
\]

考虑

\[
Z_{\rm ax}\overline W
=\mathcal D-i\mathcal I,
\tag{5.2}
\]

其中

\[
\boxed{
\mathcal I:=C_*Y-R_0a_2=a_2UA_0
}
\tag{5.3}
\]

正是 `Radius-resultant-collapse`，而正交坐标为

\[
\boxed{
\mathcal D:=C_*a_2+R_0Y.
}
\tag{5.4}
\]

利用 numerator reconstruction：

\[
10^dA_{12}
=\frac{UA_0+R_0}{g_0B},
\]

可得 exact identity

\[
\boxed{
g_0B\mathcal D
=2\bigl(EN_c+UR_0A_0\bigr),
}
\tag{Dot-exact}
\]

其中

\[
E=D_+D_-=C\cdot10^{o(S)}
\]

在 main primary depth 上等同于 `C`。

固定 pure-excess main prime，`a=n+epsilon_p`。由于 `g_0,B,U,R_0,a_2` 都是 p-units：

\[
v_p(\mathcal I)=n+\varepsilon_p.
\tag{5.5}
\]

`(Dot-exact)` 的两项深度分别为

\[
h+n,
\qquad
n+\varepsilon_p.
\]

若 `epsilon_p!=h`，较浅项唯一；若 `epsilon_p=h`，`mathcal D` 可能继续 cancellation，但 `mathcal I` 的深度恰为 `n+h`。因此无论 equal case 是否继续提升：

\[
\boxed{
v_p\bigl((\mathcal D,\mathcal I)\bigr)
=n+\min(h,\varepsilon_p).
}
\tag{Dot-gcd-depth}
\]

抽掉 common axis depth `n` 后，正交 companion 读取的只是

\[
\min(h,\varepsilon_p).
\]

定义 full-core first layer

\[
\boxed{
G_{\rm full}:=(C,A_N).
}
\tag{5.6}
\]

则

\[
\boxed{
v_p(G_{\rm full})=\min(h,\varepsilon_p).}
\tag{5.7}
\]

所以 `(Dot-gcd-depth)` 的 normalized content 恰好就是 `G_full`。

---

## 6. `G_full/G_exc` 全部由旧 axis baseline 支付

因为

\[
C_N=C/(C,N_c),
\]

有

\[
G_{\rm exc}=(C_N,A_N)\mid(C,A_N)=G_{\rm full}.
\]

定义

\[
\boxed{
G_{\rm reuse}
:=\frac{G_{\rm full}}{G_{\rm exc}}.
}
\tag{6.1}
\]

逐 prime：

\[
v_p(G_{\rm reuse})
=
\min(h,\varepsilon_p)
-
\min((h-n)_+,\varepsilon_p).
\tag{6.2}
\]

一个直接的 valuation inequality 给出

\[
\boxed{
0\le v_p(G_{\rm reuse})\le\min(h,n).
}
\tag{6.3}
\]

而

\[
v_p(G_{\rm ax})=v_p((C,N_c))=\min(h,n).
\]

故全局 main-primary 意义下：

\[
\boxed{
G_{\rm reuse}\mid G_{\rm ax}.
}
\tag{Axis-reuse}
\]

这说明把 `C_N` 换回完整 `C` 后多看到的 numerator overlap，没有产生任何新 unpaid mass；它全部落回已经被 `N_c` 占用的 axis baseline。

所以 axis/radius-digital 的 orthogonal coordinate虽然给出真实 gcd，但新增部分只是旧 payer：

\[
\boxed{
G_{\rm full}
=G_{\rm exc}\,G_{\rm reuse},
\qquad
G_{\rm reuse}\mid(C,N_c).
}
\tag{Full-vs-excess}
\]

**状态：新增结构 `已严格完成`；把 `G_reuse` 再计作 obstruction 属于 `失效/降级`。**

---

## 7. 上一文件的 `R_over` 可再拆成 axis-reuse + deep overflow

上一文件定义 `C_N^k` ladder 的 stable target tail `D_infty`，其 active main prime 上满足

\[
v_p(D_\infty)=\varepsilon_p.
\tag{7.1}
\]

并定义

\[
R_{\rm over}:=\frac{D_\infty}{G_{\rm exc}},
\]

所以

\[
v_p(R_{\rm over})
=\max(\varepsilon_p-c_p,0).
\tag{7.2}
\]

现在定义 full-core deep overflow

\[
\boxed{
R_{\rm deep}
:=\frac{D_\infty}{G_{\rm full}}.
}
\tag{7.3}
\]

因为 `c_p>0` 的 active support 上 `h>0`，有

\[
\boxed{
v_p(R_{\rm deep})
=\max(\varepsilon_p-h,0).
}
\tag{7.4}
\]

由定义立刻得到 exact factorization：

\[
\boxed{
R_{\rm over}
=G_{\rm reuse}\,R_{\rm deep}
}
\tag{Overflow-split}
\]

按 active main-primary part成立。

逐 prime 看得更清楚。令

\[
c=h-n>0.
\]

则：

\[
\boxed{
\begin{array}{c|c|c|c}
\varepsilon\le c
&G_{\rm exc}:\varepsilon
&G_{\rm reuse}:0
&R_{\rm deep}:0\\
 c<\varepsilon\le h
&G_{\rm exc}:c
&G_{\rm reuse}:\varepsilon-c
&R_{\rm deep}:0\\
 \varepsilon>h
&G_{\rm exc}:c
&G_{\rm reuse}:n
&R_{\rm deep}:\varepsilon-h.
\end{array}}
\tag{7.5}
\]

所以此前统称的 numerator overflow 实际包含两种完全不同的东西：

1. `G_reuse`：仍位于 full `C` 的可用 prime-power 深度以内，但这部分恰好被旧 axis baseline `(C,N_c)` 支付；
2. `R_deep`：已经超过整个 full `C` depth，属于同 support 上的 genuinely deep numerator tail，不能再拿来覆盖任何额外 `C`-depth。

因此：

\[
\boxed{
\text{normalized numerator tail 中唯一真正面向 unpaid }C_N
\text{ 第一层的对象就是 }G_{\rm exc}.}
\tag{Unique-unpaid-layer}
\]

这不是 `G_exc` 的小高度结论，但它封死了“从 overflow 再找一份可支付 `C_L` 的局部质量”的可能性。

---

## 8. nested gcd ladders

上一文件使用

\[
D_k^{(N)}:=\gcd(C_N^k,A_N).
\]

本文再定义 full-core ladder

\[
\boxed{
D_k^{(C)}:=\gcd(C^k,A_N).
}
\tag{8.1}
\]

逐 prime：

\[
v_p(D_k^{(C)})
=\min(kh,\varepsilon_p).
\tag{8.2}
\]

第一层为

\[
D_1^{(C)}=G_{\rm full}
=G_{\rm exc}G_{\rm reuse},
\]

而 stable layer 读取 `C` support 上完整 `epsilon_p`。在 `C_N` active support 上，两个 ladders 的 stable value一致，第一层之差恰为 `G_reuse`。

因此现在有 canonical nested picture：

\[
\boxed{
\begin{array}{c}
C_N\subset C,\\[1mm]
D_1^{(N)}=G_{\rm exc},\\[1mm]
D_1^{(C)}=G_{\rm exc}G_{\rm reuse},\\[1mm]
G_{\rm reuse}\mid(C,N_c),\\[1mm]
D_\infty/G_{\rm exc}
=G_{\rm reuse}R_{\rm deep}.
\end{array}}
\tag{Nested-ladders}
\]

这把 unpaid core、axis baseline 与 beyond-core overflow 三种深度完全分开。

---

## 9. 本轮 no-double-count 总结

当前最自然的三个“第二 short residue / second local payer”候选已经全部审计：

### 9.1 `Top-residue`

\[
Ua_3\equiv-R_{\rm dec}\pmod{G_{\rm exc}}
\]

只是

\[
C\mid Ua_3+R_{\rm dec}
\]

的弱化；full rational contact 已经提供它。

### 9.2 clean-source square lift

\[
G_{\rm exc}^2
\mid q_c^2L_{\rm clean}+5^TR_0
\]

与 hidden square联立后精确成为

\[
4\,5^{2(m-T)}C_LN(\Delta_1),
\]

即旧 secondary norm。

### 9.3 axis/radius-digital orthogonal companion

抽掉 common axis depth后读取

\[
G_{\rm full}=(C,A_N),
\]

但

\[
G_{\rm full}/G_{\rm exc}
\mid(C,N_c),
\]

新增部分全部是旧 axis payer。

因此：

\[
\boxed{
\text{full-rational Good 的现有 local Gaussian / carry / source algebra}
\text{没有再产生第二份 unpaid }G_{\rm exc}\text{ modulus。}
}
\tag{Local-closure-audit}
\]

这比“几条尝试失败”更强：它给出了失败对象各自精确退回的 canonical payer。

---

## 10. 更新后的 frontier

full rational Good 现在可以压成：

\[
\boxed{
\begin{gathered}
C_N=C/(C,N_c),\\
A_N=\alpha/(\alpha,N_c),\\
G_{\rm exc}=(C_N,A_N),\\
G_{\rm full}=(C,A_N)
=G_{\rm exc}G_{\rm reuse},\\
G_{\rm reuse}\mid(C,N_c),\\
R_{\rm over}=G_{\rm reuse}R_{\rm deep}.
\end{gathered}}
\tag{10.1}
\]

其中：

- `G_exc` 是唯一尚未被旧 axis payer覆盖、并且仍位于 unpaid denominator depth 内的 numerator contact；
- `G_reuse` 只是旧 `(C,N_c)` baseline 的重用；
- `R_deep` 已超过 full `C` prime-power depth，不能给 `C` closure 再支付一层；
- `Top-residue`、clean-source square lift、orthogonal digital companion 均已证明不能提供第二份独立 local modulus。

因此 full-rational Good 若继续推进，下一步不应再造同素数 local resultant。真正剩余的路线只剩两类：

1. 对已有 `QCRT + GCRT+` 唯一 `A_{12}` lift 做 **global digit-shell location / exclusion**；
2. 若该 location 仍只重构 carry/source algebra，则离开 full-rational local sheet，转向 genuine-Gaussian split-prime / digit-shell branch。

---

## 11. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`Top-residue` main projection no-go；`G_exc^2` clean-source square lift；其与 hidden square 精确退回 scaled `N(Delta_1)`；axis/radius digital orthogonal companion；`G_full/G_exc | (C,N_c)`；`R_over=G_reuse R_deep`；nested `C_N^k` / `C^k` gcd ladders。
- **`失效/降级`**：把 `Top-residue` 当 `G_exc` 第二 p-adic residue；把 clean-source square lift当第二个 local norm；把 `G_reuse` 当新的 unpaid modulus。
- **`待证`**：`log G_exc=o(S)` 或其它 strict digit-shell bound；`QCRT+GCRT+` 唯一 lift 的合法 digit-window exclusion；full rational Good emptiness；genuine-Gaussian closure；DD 全局空性与有效绝对高度界。

---

<a id="source-mixed-rational-good-extension"></a>

> 整合来源：`mixed-rational-good-extension.md`

# DD mixed frontier：partial rational core 的 Bad closure 与 Good normalization

> **依赖：** `frontier.md` 的 rational/genuine split、Bad elimination、Good slot theorem；[`good-radius-excess.md`](good-genuine-ledger.md#source-good-radius-excess)、[`good-axis-normalization.md`](good-genuine-ledger.md#source-good-axis-normalization)。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。旧 continuation 最终在 full rational-contact 情形 `E=D_+D_-=C_L^{1-o(1)}` 中关闭 Bad，并发展 Good slot / excess normalization。本文审计证明：Bad closure 的 local prime-support argument实际上不要求 `E` 占满 `C_L`。对任意 mixed split
> \[
> E\cdot C_G=C_L\cdot10^{o(S)},
> \]
> partial rational-contact main prime仍无法由 `e_0=V/E` 中的 genuine complement支付，因为它们是不同 prime support。因此 Bad 在 partial rational core中仍只有 `10^{o(S)}` mass；剩余 rational-contact main mass全部进入 Good。
>
> 同时，Good 的 local slot theorem、axis-normalized excess与 gcd ladder只依赖 target prime上的 unit ledger，故可将原 full-rational `C_L` 无损替换为 partial rational core `E`。

---

## 1. mixed rational/genuine split

沿用

\[
R_+=b+A,
\qquad
R_-=b-A,
\]

\[
D_+=(V,R_+),
\qquad
D_-=(V,R_-).
\]

定义 rational-contact main core

\[
\boxed{E:=D_+D_-}
\tag{1.1}

并定义 genuine complement

\[
\boxed{C_G:=\frac{C_L}{E}}
\tag{1.2}

均按删除 `10^{o(S)}` coefficient / sign-overlap exceptional core后理解。

已有 split 给

\[
\boxed{
EC_G=C_L\cdot10^{o(S)},
\qquad
(E,C_G)=10^{o(S)}.
}
\tag{1.3}

写

\[
\boxed{V=Ee_0.}
\tag{1.4}

由于

\[
V=C_Lv_0,
\]

有

\[
e_0=C_Gv_0\cdot10^{o(S)}.
\tag{1.5}

关键点：虽然 `e_0` 的**高度**在 mixed branch可以是正线性的，但对任一 main prime

\[
p^h\Vert E
\]

删除 `(E,v_0)` exceptional overlap后仍有

\[
\boxed{p\nmid e_0.}
\tag{1.6}

不同 genuine primes不会支付这个 rational prime的 same-prime divisibility。

---

## 2. Bad tangent elimination 不使用 `e_0=o(S)` 直到最后一步

旧 Bad elimination 对 `D_+` / `D_-` 的 main Bad subcores给出 oriented tangent congruences

\[
\boxed{
B_+^{\flat}\mid d h_+ + b j_+,
}
\tag{2.1+}

\[
\boxed{
B_-^{\flat}\mid b j_- - d h_-.
}
\tag{2.1-}

其中 `B_sigma^flat` 与 Bad main mass只差 `10^{o(S)}` exceptional core。

再利用 sign-Farey identities 与

\[
Ac-bd=ET_c,
\]

旧证明把同一个 oriented Bad prime-power继续压入

\[
\boxed{
T_c=e_0\widetilde r^{\,2}5^{T-m_2}.
}
\tag{2.2}

这一步是逐 prime 的 divisibility statement；并没有使用

\[
\log e_0=o(S).
\]

full-rational 旧稿只在最后用 `e_0=o(S)` 把 Bad 总质量判成 `o(S)`。

---

## 3. mixed split 中同一个 Bad prime仍不能进入 `T_c`

固定 main Bad prime

\[
p^h\Vert B_\sigma^{\flat}\mid E.
\]

由 `(1.6)`：

\[
p\nmid e_0.
\]

main coefficient-unit ledger还给

\[
p\nmid\widetilde r5.
\]

因此

\[
\boxed{p\nmid T_c.}
\tag{3.1}

但 Bad elimination要求该 same prime进入 `(2.2)`，矛盾。

所以删除 exceptional core后没有 main Bad prime：

\[
\boxed{B_+^{\flat}=B_-^{\flat}=1.}
\tag{3.2}

恢复 exceptional factors：

\[
\boxed{
\log(B_+B_-)=o(S)
}
\tag{Partial-Bad-closed}

对**任意** rational/genuine mixed split成立。

这比旧状态更强：Bad closure不是 full-rational 专属结论。

---

## 4. partial rational-contact main mass 因而几乎全是 Good

令 rational-contact main mass分解为

\[
E=B_R G_R
\]

其中 `B_R` 为 Bad、`G_R` 为 Good，忽略 `10^{o(S)}` overlap。

由 `(Partial-Bad-closed)`：

\[
\boxed{
G_R=E\cdot10^{o(S)}.
}
\tag{Partial-Good-main}

因此以后 mixed branch中的 rational-contact prime可直接按 Good local ledger处理；无需再保留正线性 Bad 子支。

---

## 5. Good slot theorem 对 partial `E` 原样成立

在每个

\[
p^h\Vert E^{\rm main}
\]

上，sign contact仍使用完整 prime-power depth。写

\[
R_\pm=D_\pm h_\pm,
\qquad
J_\pm=D_\pm j_\pm,
\]

\[
H_R=h_+h_-,
\qquad
H_J=j_+j_-.
\]

axis norm满足

\[
C_*^2+R_0^2=EN_c
\tag{5.1}

定义 integer `N_c`。

Good selected/conjugate exclusion的证明逐 prime使用：

- target `p` 在 `E` 中的完整 contact depth；
- `p\nmid e_0`；
- coefficient units；
- Bad / conjugate exceptional exclusion。

这些条件在 §3 后的 partial main core全部保留。因此原 slot theorem仍成立：若

\[
r_p=v_p(H_R),
\quad
j_p=v_p(H_J),
\quad
n_p=v_p(N_c),
\]

则

\[
\boxed{\min(r_p,j_p)=0,}
\tag{Slot-RJ-partial}

\[
\boxed{\min(j_p,n_p)=0.}
\tag{Slot-JN-partial}

radius split同样为

\[
\boxed{
a_p=\min(r_p,n_p)+\varepsilon_p,}
\tag{Radius-partial}

\[
\boxed{
\varepsilon_p>0\Longrightarrow r_p=n_p.
}
\tag{Equal-partial}

其中

\[
a_p=v_p(A_0)=v_p(\alpha)
\]

沿用 `Radius=Concat`。

---

## 6. axis-normalized excess 公式也不需要 `E=C_L`

`good-axis-normalization.md` 的局部证明只使用 `(Radius-partial)` 与 `(Equal-partial)`，故立即得到

\[
\boxed{
\varepsilon_p
=\max(v_p(\alpha)-v_p(N_c),0).
}
\tag{6.1}

所以对 partial rational core定义

\[
\boxed{
E_N:=\frac{E}{(E,N_c)},
}
\tag{6.2}

\[
\boxed{
A_N:=\frac{\alpha}{(\alpha,N_c)}.
}
\tag{6.3}

则逐 `p^h||E`：

\[
v_p(E_N)=\max(h-v_p(N_c),0),
\]

\[
v_p(A_N)=\varepsilon_p.
\]

定义 partial rational excess

\[
\boxed{
G_{\rm exc}^{(R)}
:=\gcd(E_N,A_N).
}
\tag{6.4}

它正是旧 full-rational `G_exc` 在 mixed split中的自然替代。

---

## 7. gcd ladder 原样延伸

对

\[
k\ge1
\]

定义

\[
\boxed{
D_k^{(R)}:=\gcd(E_N^k,A_N).
}
\tag{7.1}

则逐 main rational prime：

\[
\boxed{
v_p(D_k^{(R)})
=\min\left(
k\max(h-v_p(N_c),0),
\varepsilon_p
\right).
}
\tag{7.2}

第一层为

\[
\boxed{D_1^{(R)}=G_{\rm exc}^{(R)}.}
\tag{7.3}

稳定层、denominator deficit / numerator overflow separation与旧 `good-excess-gcd-ladder.md` 完全相同，只需将

\[
C_N\rightsquigarrow E_N.
\]

所以 mixed frontier 的 rational Good困难仍可 canonical 化，而无需 full-rational 假设。

---

## 8. 与 large-genuine threshold 的合并

`genuine-large-core-crt.md` 已证明：若

\[
c:=\frac{\log C_G}{S}
>0.382232844764\ldots,
\]

则 fixed genuine fiber中 `A_12` 至多一个。

其补集满足

\[
\frac{\log E}{S}
\ge0.617767155236\ldots+o(1).
\]

本文说明该 rational-heavy mass并不会分散到 Bad；它几乎全部进入 Good：

\[
\boxed{
\frac{\log G_R}{S}
\ge0.617767155236\ldots+o(1).
}
\tag{8.1}

因此 large-genuine threshold以下的真正未决核已经压成：

\[
\boxed{
\text{至少 }0.617767155236\ldots S
\text{ 的 partial-rational Good core}
}
\]

加上至多 `0.382232844764...S` 的 orientation-locked genuine complement。

下一步可以直接对这个 quantitative mixed Good core重做 axis/excess mass ledger；不需要再考虑 Bad。

---

## 9. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：partial rational Bad closure、partial Good main reduction、slot theorem extension、axis-normalized excess公式、partial `E_N/A_N/G_exc^(R)` 与 gcd ladder。
- **`有限/结构结论`**：large-genuine threshold以下 rational Good mass至少 `0.617767155236...S`。
- **`待证`**：partial Good quantitative mass allocation；`G_exc^(R)` strict digit-shell bound；mixed/genuine frontier emptiness；DD 全局空性。

---

<a id="source-pairmax-fixed-a12-crt"></a>

> 整合来源：`pairmax-fixed-a12-crt.md`

# DD one-channel pair-max 的 split-independent fixed `A_12` CRT

> **依赖：** `frontier.md` 的 one-channel pair-max reduction、sphere carrier、exact carry；[`genuine-elliptic-collapse.md`](good-genuine-ledger.md#source-genuine-elliptic-collapse) 中的 `Sphere-pay-identity`；[`genuine-a12-fixed-crt.md`](good-genuine-ledger.md#source-genuine-a12-fixed-crt) 的 carry-square extraction 模板。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。此前 W-free carrier
> \[
> \Theta=(\kappa+G)Q(a_2b_1)^2\beta+\mathscr T a_3^2
> \]
> 是在 genuine orientation audit 中发现的，但其 `Sphere-pay-identity` 实际只依赖 one-channel pair-max sphere depth，完全不使用 rational/genuine split。本文因此将其全局化到整个 main `C_L`，证明
> \[
> (C_L^{\rm main})^2\mid\Theta.
> \]
> 再代入 exact decimal carry，得到一个 coefficients 固定、effective period为整个 `C_L` 的线性 `A_12` congruence。与 clean-source `q_c^2` period 联立后，**任意 terminal frontier fixed fiber** 中 `A_12` / `a_1` 都至多一个；此前 `c>0.382232...` 的 large-genuine threshold因此降级为被本文统一结论覆盖的中间分支结果。
>
> 本文仍只给 uniqueness/counting，不证明唯一 candidate 不存在。

---

## 1. 全 main pair-max 的共同 unit ledger

one-channel reduction已经把 moving pair-max main core全部放入 `(b_2,b_3)` channel。固定

\[
p^h\Vert C_L^{\rm main}.
\]

删除 all-three/common、coefficient 与 rough overlaps 的 `10^{o(S)}` exceptional core后：

\[
\boxed{
v_p(b_2)=v_p(b_3)=v_p(q)=h,}
\tag{1.1}

\[
\boxed{p\nmid b_1a_2a_3Q10.}
\tag{1.2}

写

\[
G=b_1b_2,
\qquad y:=a_2b_1.
\]

则

\[
\boxed{v_p(G)=h,\qquad p\nmid y.}
\tag{1.3}

这些结论对 rational-contact / genuine 两类 main prime完全相同。

---

## 2. original sphere norm 在每个 main prime上有 `4h` 深度

定义

\[
\boxed{
\mathcal S_{\rm raw}
:=y^2b_3^2+G^2a_3^2
=b_1^2\left[(a_2b_3)^2+(a_3b_2)^2\right].
}
\tag{2.1}

pair-max Gaussian sphere carrier给

\[
\Pi^2\mid y_2+i y_3,
\qquad N(\Pi)=C_L.
\]

对当前 `p^h`，清除

\[
y_2=a_2q/b_2,
\qquad
y_3=a_3q/b_3
\]

中的 p-unit quotient后，得到 normalized square-depth

\[
p^{2h}\mid
 a_2^2(b_3/p^h)^2
+a_3^2(b_2/p^h)^2.
\]

重新乘回 shared denominator baseline `p^{2h}`：

\[
\boxed{p^{4h}\mid\mathcal S_{\rm raw}.}
\tag{Sphere-raw-global}

因此

\[
\boxed{(C_L^{\rm main})^4\mid\mathcal S_{\rm raw}}
\tag{2.2}

按 main-primary depth理解。

---

## 3. W-free `Theta` 的 sphere-pay identity本来就是 split-independent

定义

\[
T_3:=10^{m_3},
\qquad
A_c:=Qy^2,
\]

\[
\boxed{
\mathscr T:=\frac{\kappa^2(\kappa+2G)}{T_3}\in\mathbf Z_{>0},
}
\tag{3.1}

以及

\[
\boxed{
\Theta
:=(\kappa+G)A_c\beta+\mathscr T a_3^2.
}
\tag{3.2}

`genuine-elliptic-collapse.md` 已机械验证 exact identity

\[
\boxed{
T_3G^2\Theta
=\kappa\left[
\kappa(\kappa+2G)\mathcal S_{\rm raw}
+G^2y^2b_3^2
\right].
}
\tag{Sphere-pay-global}

它的推导只使用

\[
\beta=T_3Q+b_3,
\qquad
\kappa b_3=T_3QG,
\]

以及

\[
(\kappa+G)^2=\kappa(\kappa+2G)+G^2.
\]

**没有使用**：

- `A≡±b`；
- `D_±`；
- rational-contact；
- genuine complement；
- same/opp orientation。

所以 `(Sphere-pay-global)` 对整个 one-channel main core都成立。

---

## 4. 全局得到 `C_L^2 | Theta`

固定 `p^h||C_L^{main}`。

由 `(Sphere-raw-global)`：

\[
v_p(\mathcal S_{\rm raw})\ge4h.
\]

第二项显然满足

\[
v_p(G^2y^2b_3^2)=4h.
\]

同时 main unit ledger给

\[
p\nmid T_3\kappa.
\]

所以 `(Sphere-pay-global)` 右端至少有 `4h` 深度，而左端显式 `G^2` 含恰好 `2h`。故

\[
\boxed{v_p(\Theta)\ge2h.}
\tag{4.1}

聚合全部 main prime-powers：

\[
\boxed{
(C_L^{\rm main})^2\mid\Theta.
}
\tag{Pairmax-Theta}

这是真正 split-independent 的 W-free square-depth carrier。

注意它完全由 sphere carrier支付；本文仍不把该 depth算作新的 local height surplus。

---

## 5. exact carry平方展开

沿用

\[
V=C_Lv_0,
\tag{5.1}

以及 exact carry

\[
\boxed{
g_0Ua_3
=g_0B10^dVA_{12}-\Sigma R_0.}
\tag{Carry}

把 `(Carry)` 平方：

\[
\begin{aligned}
g_0^2U^2a_3^2
={}&g_0^2B^210^{2d}V^2A_{12}^2\\
&-2g_0B10^dV\Sigma R_0A_{12}
+\Sigma^2R_0^2.
\end{aligned}
\tag{5.2}

代入 `g_0^2U^2 Theta`：

\[
\begin{aligned}
g_0^2U^2\Theta
={}&H_{L,0}
-2\mathscr T g_0B10^dV\Sigma R_0A_{12}\\
&+\mathscr T g_0^2B^210^{2d}V^2A_{12}^2,
\end{aligned}
\tag{5.3}

其中定义 split-independent constant part

\[
\boxed{
H_{L,0}
:=g_0^2U^2(\kappa+G)A_c\beta
+\mathscr T\Sigma^2R_0^2.
}
\tag{5.4}

`H_{L,0}` 不含

\[
A_{12},\quad a_3,\quad W,
\]

也不依赖 rational/genuine orientation split。

---

## 6. 第一层 `C_L` 自动进入 constant part

由 `(Pairmax-Theta)`：

\[
(C_L^{\rm main})^2
\mid g_0^2U^2\Theta
\]

（删去 `g_0U` coefficient overlap）。

在 `(5.3)` 中：

- linear term含 `V=C_Lv_0`，故至少一层 `C_L`；
- quadratic term含 `V^2`，故至少两层 `C_L`。

所以模 `C_L` 只剩 constant part：

\[
\boxed{C_L^{\rm main}\mid H_{L,0}.}
\tag{6.1}

定义 integer quotient

\[
\boxed{
M_{L,0}:=\frac{H_{L,0}}{C_L^{\rm main}}.
}
\tag{6.2}

为简洁，下文把删除 exceptional core后的 `C_L^{main}` 仍写作 `C_L`。

---

## 7. split-independent fixed `C_L` residue

把 `(5.3)` 除以 `C_L`，使用

\[
V=C_Lv_0.
\]

得到

\[
\begin{aligned}
\frac{g_0^2U^2\Theta}{C_L}
={}&M_{L,0}
-2\mathscr T g_0B10^d v_0\Sigma R_0A_{12}\\
&+C_L\mathscr T g_0^2B^210^{2d}v_0^2A_{12}^2.
\end{aligned}
\tag{7.1}

左边仍被 `C_L` 整除；最后一项显式含 `C_L`。因此：

\[
\boxed{
2\mathscr T g_0B10^d v_0\Sigma R_0A_{12}
\equiv M_{L,0}
\pmod{C_L}.
}
\tag{Pairmax-GCRT0}

这就是整个 moving pair-max core上的 fixed decimal reader。

---

## 8. effective period 为完整 `C_L`

对 main `p^h||C_L`，需审计 coefficient

\[
2\mathscr T g_0B10^d v_0\Sigma R_0.
\]

main setup已经删除

\[
p\mid2\cdot5\cdot g_0BR_0v_0
\]

的 `10^{o(S)}` exceptional core。

另外：

### 8.1 `Sigma` 是 p-unit

由

\[
V=X-Y\equiv0\pmod p
\]

且 `X,Y` 为 p-units，

\[
\Sigma=X+Y\equiv2Y\not\equiv0\pmod p.
\]

故

\[
p\nmid\Sigma.
\tag{8.1}

### 8.2 `mathscr T` 是 p-unit

统一 tail-root linearization给

\[
\mathscr T a_3
=\kappa G^2C_{\rm DD}+\eta(\kappa+G)W.
\]

main p上 `G≡0`，而 `a_3,\kappa,W` 为 units，所以

\[
\mathscr T a_3
\equiv\eta\kappa W\not\equiv0\pmod p.
\]

故

\[
p\nmid\mathscr T.
\tag{8.2}

因此 `(Pairmax-GCRT0)` 的 effective period为

\[
\boxed{C_L/10^{o(S)}}.
\tag{8.3}

---

## 9. 与 fixed `q_c^2` residue 联立

clean-source exact identity已经给

\[
\boxed{
g_0B10^dVA_{12}-XR_0
=Uq_c^2L_{\rm clean}.}
\tag{9.1}

所以

\[
\boxed{
g_0B10^dVA_{12}
\equiv XR_0\pmod{q_c^2}.}
\tag{Q-fixed}

其 effective period为

\[
q_c^2/10^{o(S)}.
\]

同时

\[
(C_L,q_c)=10^{o(S)}.
\]

故 `(Pairmax-GCRT0)` 与 `(Q-fixed)` 的联合 period为

\[
\boxed{
M_{\rm pairmax}
=\frac{C_Lq_c^2}{10^{o(S)}}.
}
\tag{9.2}

frontier heights：

\[
\log C_L=S+o(S),
\]

\[
\log q_c=z_*S+o(S),
\qquad
z_*=0.308883577618\ldots.
\]

所以

\[
\boxed{
\log M_{\rm pairmax}
=1.617767155236\ldots S+o(S).
}
\tag{Full-period-height}

---

## 10. universal fixed-fiber prefix uniqueness

prefix polarization给

\[
\boxed{\log A_{12}=S+o(S).}
\]

固定 terminal denominator/source/small-prefix fiber，使两个 congruences的 coefficients、RHS、`C_L,q_c` 固定。

若有两个不同合法

\[
A_{12}^{(1)}\ne A_{12}^{(2)}
\]

同时满足 `(Pairmax-GCRT0)` 与 `(Q-fixed)`，则

\[
M_{\rm pairmax}
\mid A_{12}^{(1)}-A_{12}^{(2)}.
\]

但

\[
|A_{12}^{(1)}-A_{12}^{(2)}|
<10^{S+o(S)},
\]

而

\[
M_{\rm pairmax}
=10^{1.617767155236\ldots S+o(S)}.
\]

sufficiently large `S` 矛盾。因此：

\[
\boxed{
\#\{A_{12}\text{ in any fixed terminal frontier fiber}\}\le1.
}
\tag{Universal-A12-unique}

固定 subexponential suffix `(n_2,a_2)` 后同样有

\[
\boxed{
\#\{a_1\text{ in the fixed fiber}\}\le1.
}
\tag{Universal-a1-unique}

这不再需要 rational/genuine split或 genuine-mass threshold。

---

## 11. 对此前分支结果的更新

本文说明以下中间状态需要降级：

1. `genuine-large-core-crt.md` 的 threshold
   \[
   c>0.382232844764\ldots
   \]
   仍是正确 sufficient condition，但已被 `Universal-A12-unique` 全面覆盖；不再是当前 frontier 的真实分支边界。
2. full-rational `GCRT+` 的 period仍是正确局部 reader，但不再需要靠 rational contact才能获得 `C_L`-级 second-order decimal period；`Pairmax-GCRT0` 已统一覆盖整个 one-channel core。
3. rational/genuine mixed split仍可用于其他 cofactor/slot 分析，但 **prefix uniqueness 不再依赖该 split**。

---

## 12. no-double-count 与未解决部分

`Pairmax-GCRT0` 的 `C_L` period来自 sphere-paid `Theta` depth。因此它可用于：

- CRT uniqueness；
- candidate counting；
- digit-shell location。

不能把 `C_L` 再当作 sphere square-depth之外的新 local height surplus。

本文仍没有证明唯一 CRT lift不落入合法 decimal window。因此 DD frontier emptiness依然开放。

真正下一步已压成：

> 对 split-independent 联合 CRT
> \[
> A_{12}\pmod{C_Lq_c^2}
> \]
> 的唯一 lift做 Archimedean digit-window location，或者构造一个不由 sphere/carry/clean-source parents重构的第三 fixed residue。

---

## 13. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：global `Sphere-raw-4h`、split-independent `C_L^2|Theta`、fixed `Pairmax-GCRT0`、effective period `C_L`、与 `q_c^2` 联合 period `1.617767155236...S`、universal fixed-fiber `A_12/a_1` uniqueness。
- **`失效/降级`**：将 `c>0.382232844764...` 当作当前必要分支阈值；认为只有 full-rational / large-genuine 才有 `C_L`-级 prefix period。
- **`有限/计数结论`**：universal uniqueness仍不是 emptiness。
- **`待证`**：unique CRT lift的 Archimedean location；独立第三 fixed residue若存在；DD frontier emptiness与全局 DD closure。

---

<a id="source-pure-common-five-squareclass-nogo"></a>

> 整合来源：`pure-common-five-squareclass-nogo.md`

# DD pure common-scale 的 5-adic square-class no-go

> **依赖：** [`high-funnel-two-adic-balance.md`](high-funnel-ledger.md#source-high-funnel-two-adic-balance)、
> [`high-funnel-denominator-max-lock.md`](high-funnel-ledger.md#source-high-funnel-denominator-max-lock) 与
> `core.md` 的 overlap parameterization / scale-free quadratic。
>
> **严格状态：** `已严格完成（pure-common conditional audit）`。
> 本文不关闭 pure common-scale branch；它证明一个重要方法边界：
> scale-free quadratic 在该 branch 中产生的看似深达 `5^{2g_5}` 的 Hensel
> 条件，约去 forced common scale 后只剩一个普通 5-adic unit square class。
> 因而继续增加同一个 5-adic Hensel 深度不会产生正线性高度障碍。

---

## 1. pure common-scale ledger

假设 `Final-5-lock` 落在 endpoint

\[
\boxed{
q_5=n_5=0,
\qquad
m=4g,
\qquad
T=2g,
}
\tag{Pure}

其中 `g:=g_5>0`。

`high-funnel-two-adic-balance.md` 已证明 denominator 5-depth 必为

\[
\boxed{
v_5(b_1)=g,
\qquad
v_5(b_2)=0,
\qquad
v_5(b_3)=2g.
}
\tag{1.1}

令

\[
\omega=(10^m,b_3),
\qquad
L=10^m/\omega.
\]

于是

\[
\boxed{v_5(\omega)=v_5(L)=2g.}
\tag{1.2}

在 overlap 参数化

\[
Q=\eta Q_1,
\qquad
\tau=\eta v,
\qquad
u=LQ_1,
\]

\[
D=vc\lambda,
\qquad
C=\lambda w,
\qquad
g_*=vc\lambda r
\]

中，`q_5=0` 和 `tau` 为 5-unit 给

\[
\eta,Q_1,v\ \text{均为 5-units}.
\]

又 `v_5(H_sph)=0`，所以 `D=(H_sph,q_lcm)` 为 5-unit；因此

\[
\boxed{v_5(c)=v_5(\lambda)=v_5(w)=0.}
\tag{1.3}

`a=ca_0` 且 pure branch有 `v_5(a)=0`，故

\[
\boxed{v_5(a_0)=0.}
\tag{1.4}

最后 denominator overlap 在 5 处为

\[
v_5(g_*)=g,
\]

所以由 `g_*=vc lambda r`：

\[
\boxed{v_5(r)=g.}
\tag{1.5}

定义 5-units

\[
L'=L/5^{2g},
\qquad
r'=r/5^g,
\qquad
\omega'=\omega/5^{2g}.
\]

---

## 2. 清分母后的 scale-free quadratic

`core.md` 的 scale-free quadratic为

\[
\begin{aligned}
0={}&
L c^4\lambda^2r^2w(LQ_1+2v)x^2\\
&-2L c^4\lambda^2r^2v(LQ_1+v)A_{12}10^d x\\
&+\eta^2\mathcal N_{12}Q_1w,
\end{aligned}
\tag{SFQ}

其中

\[
x=a_0/\omega.
\]

乘 `omega^2` 后，三项的 5-depth分别为

\[
4g,
\qquad
d+6g,
\qquad
4g.
\]

所以除以 `5^{4g}w` 后得到

\[
\boxed{
L'c^4\lambda^2r'^2(LQ_1+2v)a_0^2
+\eta^2\mathcal N_{12}Q_1\omega'^2
\equiv0
\pmod{5^{d+2g}}.
}
\tag{2.1}

这确实是一个很深的 two-unit cancellation；但下面说明其深度本身没有新信息。

---

## 3. prefix norm 在 `5^{2g}` 下退化成一个平方

写

\[
X=a_1b_2,
\qquad
Y=a_2b_1,
\qquad
\mathcal N_{12}=X^2+Y^2.
\]

由 `(1.1)` 与 reducedness：

\[
v_5(X)=0,
\qquad
v_5(Y)\ge g.
\]

因此

\[
\boxed{
\mathcal N_{12}\equiv X^2\pmod{5^{2g}}.
}
\tag{3.1}

将 `(2.1)` 降到模 `5^{2g}` 并使用 `(3.1)`，所有出现的分母都是
5-units，于是

\[
\boxed{
-\frac{Q_1}{L'(LQ_1+2v)}
\in
\left((\mathbf Z/5^{2g}\mathbf Z)^\times\right)^2.
}
\tag{3.2}

更显式地，右边的一个平方根由

\[
\frac{c^2\lambda r'a_0}{\eta X\omega'}
\]

给出（符号和选取不影响 square class）。

---

## 4. square class 精确化成 `UV`

S-unit phase有

\[
LQ_1=u=2\cdot5^TU,
\qquad
v=V,
\qquad
T=2g.
\]

所以

\[
\boxed{L'Q_1=2U.}
\tag{4.1}

并且

\[
LQ_1+2v
=2(5^TU+V)
=2^{H+1}Z.
\tag{4.2}

由 `(4.1)`–`(4.2)`：

\[
-\frac{Q_1}{L'(LQ_1+2v)}
=
-\frac{Q_1^2}{2^{H+2}UZ}.
\tag{4.3}

`Q_1^2` 是平方，而 `-1` 在 `Z_5` 中也是平方；`2^{H+2}` 与
`2^H` 只差平方因子 `4`。故 `(3.2)` 等价于

\[
\boxed{
2^HUZ
\in
\left((\mathbf Z/5^{2g}\mathbf Z)^\times\right)^2.
}
\tag{4.4}

但 phase equation

\[
2^HZ=5^{2g}U+V
\]

模 `5^{2g}` 给

\[
2^HZ\equiv V\pmod{5^{2g}}.
\]

最终得到最简形式

\[
\boxed{
UV
\in
\left((\mathbf Z/5^{2g}\mathbf Z)^\times\right)^2.
}
\tag{UV-square}

---

## 5. 为什么这没有线性高度收益

对奇素数 `p`，一个 `p`-adic unit是模 `p^k` 的平方，当且仅当它模 `p`
是平方；任意非零平方根随后由普通 Hensel lemma唯一提升。

所以 `(UV-square)` 的全部深度条件严格等价于

\[
\boxed{
UV\text{ 是模 }5\text{ 的 quadratic residue}.
}
\tag{UV-mod5}

因此 `2g` 即使随 `S` 线性增长，也不会产生 `2g` 份独立约束。它只保留
一个 square-class bit。

这正是 common-scale branch 与 genuine angular branch 的差别：前者的深
5-adic denominator可以被一个 unit square root自动吸收，继续做 same-prime
Hensel lifting不会得到新的 Archimedean 费用。

---

## 6. 方法边界

- **`已严格完成`**：`(2.1)`、`(UV-square)`、`(UV-mod5)`。
- **`失效/降级`**：把 pure common-scale 的 `5^{2g}` Hensel 深度本身视作线性高度 obstruction。
- **`待证`**：把 `UV` 的 square class 与 moving split-prime orientation / `q,Z` rough allocation 联立；或从另一个独立 carrier得到第二个不兼容的 square class。

所以 pure common-scale 的下一步应该是跨 prime 或跨 carrier，而不是继续提高同一个 5-adic lifting 阶数。

---

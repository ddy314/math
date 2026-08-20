# DD `6.308883577618...` frontier 的 5-adic tail-root closure

> **依赖：** [`tail-root-decimal-phase-lock.md`](tail-root-decimal-phase-lock.md) 的 exact `Tail-decimal` congruence、`core.md` §18 的 DD 判别根整除 `W=L Xi`、`global-framework.md` §7 的统一判别根、`notation.md` 的统一 `W` 记号、`frontier.md` 的 5-adic baseline 与 terminal primitive overlap。
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

# DD baseline-free source cancellation 的 numerator transfer theorem

> **依赖：** [`tail-pure-cancellation-three-sheet.md`](tail-pure-cancellation-three-sheet.md)、
> [`tail-hard-source-derivative-sheet.md`](tail-hard-source-derivative-sheet.md)、
> DD gap quadratic。
>
> **严格状态：** `已严格完成（baseline-free odd rough primes）`。
>
> 固定
> \[
> p\nmid10b_1b_2b_3,
> \qquad p^c\Vert Q,\quad c>0.
> \]
> 则 source cancellation depth不可能悬空：
> \[
> \boxed{
> c\le
> \max\bigl(v_p(C),v_p(\mathcal N_{12})\bigr).
> }
> \]
> 换言之，完整 prime-power `p^c` 必须进入 numerator coefficient `C` 或 prefix
> Gaussian norm `N_12` 的至少一侧。证明的关键是：three-sheet中唯一可能未支付的
> hard `AB` sheet会同时要求
> \[
> M\equiv C_0a
> \quad\text{与}\quad
> 2M\equiv C_0a
> \pmod{p^{c+\rho}},
> \]
> 对 odd `p` 直接矛盾。

---

## 1. 已知 local ledger

沿用 baseline-free hypotheses：

\[
p\nmid10b_1b_2b_3,
\qquad p^c\Vert Q,\quad c>0.
\]

前序文件已经证明：

\[
v_p(\nu)=0,
\qquad
v_p(\mu)=v_p(G_0)=v_p(a)=:\rho,
\]

\[
n:=v_p(\mathcal N_{12})\ge\rho,
\]

并记

\[
t:=v_p(C).
\]

unified quadratic的 divided term valuations为

\[
2\rho,\qquad \rho+t,\qquad c+n,
\]

所以只能位于 `AB/AD/BD` three-sheet。

---

## 2. 若 `n>=c` 或 `t>=c` 已完成支付

目标是证明

\[
c\le\max(t,n).
\]

若

\[
n\ge c
\]

或

\[
t\ge c
\]

已经结束。因此只需反设

\[
\boxed{n<c,\qquad t<c.}
\tag{2.1}

因为

\[
\rho\le n,
\]

于是

\[
\boxed{\rho<c.}
\tag{2.2}

---

## 3. `AD` 与 `BD` 在反设下自动消失

`AD` sheet要求

\[
c+n=2\rho.
\]

但 `n>=rho` 立刻给

\[
c\le\rho,
\]

与 `(2.2)` 矛盾。

`BD` sheet要求

\[
\rho+t=c+n,
\qquad t\le\rho.
\]

结合 `n>=rho` 得

\[
c\le t,
\]

与 `(2.1)` 的 `t<c` 矛盾。

所以反设下只能进入

\[
\boxed{AB\text{ sheet}.}
\tag{3.1}

`AB` 给

\[
\boxed{t=\rho,}
\qquad
c+n\ge2\rho.
\]

由于 `c>rho`、`n>=rho`，事实上

\[
\boxed{c+n>2\rho.}
\tag{3.2}

这正是 `tail-hard-source-derivative-sheet.md` 的 hard sub-sheet。

---

## 4. discriminant derivative要求 `M=C_0a`

hard derivative文件已证明，在 `(3.1),(3.2)` 下

\[
\boxed{v_p(W)=v_p(\Xi)=c+\rho,}
\]

其中

\[
\Xi=|\mathcal M-C_0a|.
\]

并且

\[
\mathcal M=q_{\rm lcm}C.
\]

简记

\[
\boxed{M:=\mathcal M.}
\]

baseline-free denominator意味着 `q_lcm` 为 `p`-unit；`t=rho` 给

\[
\boxed{v_p(M)=\rho.}
\tag{4.1}

又 `C_0=QL+2tau` 是 `p`-unit，而 `v_p(a)=rho`。所以

\[
\boxed{v_p(C_0a)=\rho.}
\tag{4.2}

`v_p(M-C_0a)=c+rho` 因而等价于 normalized derivative contact

\[
\boxed{
M\equiv C_0a
\pmod{p^{c+\rho}}.
}
\tag{Derivative-contact}

---

## 5. gap quadratic要求 `2M=C_0a`

DD gap quadratic为

\[
\boxed{
C_0a^2-2Ma+Q\frac{\mathcal S_{12}}L=0.
}
\tag{5.1}

baseline-free `p` 下 `L` 为 unit，并且

\[
v_p(\mathcal S_{12})=v_p(\mathcal N_{12})=n,
\]

因为 `q_lcm/G` 为 `p`-unit。

三项 valuations分别为：

\[
2\rho,
\qquad
2\rho,
\qquad
c+n.
\]

由 `(3.2)`：

\[
c+n>2\rho.
\]

所以前两项必须单独相消到第三项的深度：

\[
v_p(C_0a^2-2Ma)=c+n.
\]

约去 `a` 的 `rho` 层：

\[
\boxed{
v_p(C_0a-2M)=c+n-\rho.}
\tag{5.2}

而 `n>=rho`，故

\[
c+n-\rho\ge c.
\]

乘回 baseline `p^rho` 的记号，至少得到

\[
\boxed{
2M\equiv C_0a
\pmod{p^{c+\rho}}}
\tag{Gap-contact}

当 `n>rho` 时实际深度更高；这里只需要 `c+rho`。

---

## 6. 两 contacts 对 odd prime 不相容

`Derivative-contact` 与 `Gap-contact` 相减：

\[
M\equiv0\pmod{p^{c+\rho}}.
\]

但 `(4.1)` 给

\[
v_p(M)=\rho<c+\rho.
\]

矛盾。

因此反设 `(2.1)` 不成立，证明

\[
\boxed{
 c\le\max(t,n)
 =\max\bigl(v_p(C),v_p(\mathcal N_{12})\bigr).
}
\tag{Source-transfer-local}

---

## 7. prime-power transfer 的整数形式

定义 baseline-free source cancellation part

\[
X_{Q,0}
:=
\prod_{\substack{p\nmid10b_1b_2b_3\\p^c\Vert Q}}
 p^c.
\]

对每个 prime，`Source-transfer-local` 说明其完整 exponent `c` 被
`C` 或 `N_12` 的最大 exponent覆盖。因此

\[
\boxed{
X_{Q,0}
\mid
\operatorname{lcm}(C,\mathcal N_{12}).
}
\tag{Source-transfer-global}

特别地

\[
\log X_{Q,0}
\le
\log C+\log\mathcal N_{12},
\]

但后续做 height optimization时应使用 `lcm` / primewise max，而不是把两边高度
机械相加造成 double-count。

---

## 8. 含义与下一步

这条 theorem第一次把 denominator-prefix 的 pure cancellation depth转移到 numerator-side
两个明确 carrier：

\[
\boxed{C\quad\text{or}\quad\mathcal N_{12}.}
\]

其中：

- `C=10^dA_12` 是 DD weighted prefix numerator coefficient；
- `N_12` 是 prefix Gaussian norm。

因此 `tail-rough-cq-excess.md` 的最坏 `E=j=0` pool已经不再是匿名 source gcd。

下一步有两条：

1. 将一般 `E,j>0` 的 normalized overflow `x_p` 约去 denominator baseline后归约到本文，
   争取证明整个 `X_Q` 都进入 normalized `C/N_12`；
2. 在 height层面审计 `C` 的 forced decimal `10^d` 与 `N_12` 的 common/angle depth，
   避免把已有 digit baseline重复收费。

---

## 9. 状态摘要

- **`已严格完成`**：hard derivative sheet为空；`Source-transfer-local/global`。
- **`结构压缩`**：baseline-free primitive denominator cancellation完整转入 numerator
  coefficient或 prefix Gaussian norm。
- **`待证`**：一般 baseline normalized transfer；`C/N_12` 的 independent excess高度；
  post-tail branch reoptimization；DD global explicit slope / absolute height。

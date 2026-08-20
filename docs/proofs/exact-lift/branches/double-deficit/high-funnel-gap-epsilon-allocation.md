# DD gap square-core 的 `epsilon / lambda / G_0` support allocation

> **依赖：** [`high-funnel-gap-square-core.md`](high-funnel-gap-square-core.md)、
> `core.md` §37–38 的 overlap 参数化与 primitive system、exact-lift primitive reduction。
>
> **严格状态：** `已严格完成（rough support；pure-common specialization 为全整数结论）`。
>
> 本文把
> \[
> 5^Ta_0G_0=s\varepsilon\mu^2
> \]
> 中 `a_0` 与 `epsilon` 的 common support定位到 `lambda`。
> 对任意 `p` 不整除 10：
> \[
> \boxed{
> v_p((a_0,\varepsilon))\le v_p(\lambda).
> }
> \]
> 在 pure common / `mathfrak q=0` sheet中，`a_0,epsilon` 都是 10-units；令
> \[
> d=(a_0,\varepsilon),\qquad a_0=dA,\qquad\varepsilon=dE,
> \]
> 则
> \[
> \boxed{d\mid\lambda,\qquad E\mid G_0,\qquad
> A(G_0/E)=\left(\mu/5^{g_5}\right)^2.}
> \]
> 因而 pure common 的 gap squarefree support只剩 `lambda` 与 `G_0` 两个 payer。

---

## 1. overlap primitive system

沿用 `core.md` §37–38：

\[
\eta=(Q,\tau),
\qquad
Q=\eta Q_1,
\qquad
\tau=\eta V,
\]

\[
u=LQ_1,
\qquad
(u,V)=1,
\]

以及

\[
\varepsilon=(c_3,u+V),
\qquad
c_3=\varepsilon c,
\qquad
u+V=\varepsilon w.
\]

进一步

\[
D=Vc\lambda,
\qquad
C=\lambda w,
\]

\[
a=ca_0.
\]

primitive system 中第二条精确方程为

\[
\boxed{
\lambda VH_0-a_3\varepsilon
=La_0.
}
\tag{P2}

exact-lift primitive denominator还满足

\[
\boxed{
q_0=\frac{\omega\eta\varepsilon}{\lambda},
\qquad
(H_0,q_0)=1.
}
\tag{1.1}

---

## 2. `p|epsilon` 自动避开 `LQ_1V`

固定 prime

\[
p\nmid10,
\qquad
p\mid\varepsilon.
\]

因为

\[
\varepsilon\mid u+V,
\qquad
(u,V)=1,
\]

有

\[
\boxed{p\nmid uV.}
\tag{2.1}

而 `u=LQ_1` 且 `L` 为 10-smooth，所以

\[
\boxed{p\nmid LQ_1V.}
\tag{2.2}

特别地 `V` 是 `p`-unit。

---

## 3. `gcd(a_0,epsilon)` 的 full depth必须进入 `lambda`

记

\[
A:=v_p(a_0),
\qquad
E:=v_p(\varepsilon),
\qquad
L_\lambda:=v_p(\lambda),
\qquad
H_p:=v_p(H_0),
\]

并令

\[
\boxed{t:=\min(A,E).}
\tag{3.1}

在 `(P2)` 中：

- `a_3 epsilon` 被 `p^E` 整除，因而至少被 `p^t` 整除；
- `L a_0` 因 `p` 不整除 `L`，其 valuation为 `A>=t`。

所以第一项也必须满足

\[
p^t\mid\lambda V H_0.
\]

由 `(2.2)` 中 `p` 不整除 `V`：

\[
\boxed{L_\lambda+H_p\ge t.}
\tag{3.2}

反设

\[
L_\lambda<t.
\]

则 `(3.2)` 强迫

\[
H_p>0.
\tag{3.3}

但 `p` 不整除 `omega`，而 `(1.1)` 给

\[
v_p(q_0)
=v_p(\eta)+E-L_\lambda.
\]

由于

\[
E\ge t>L_\lambda,
\]

必有

\[
v_p(q_0)>0.
\]

这与 `(3.3)` 和

\[
(H_0,q_0)=1
\]

矛盾。

所以

\[
\boxed{
\min(v_p(a_0),v_p(\varepsilon))
\le v_p(\lambda)
\qquad(p\nmid10).
}
\tag{Common-to-lambda}

逐素数相乘：

\[
\boxed{
\operatorname{core}_{10}\bigl((a_0,\varepsilon)\bigr)
\mid\lambda.
}
\tag{3.4}

这是 full prime-power depth，而不只是 radical support。

---

## 4. pure common sheet 中 common gcd 本身是 10-unit

现在进入 `Final-5-lock` 的 pure common / LP worst face：

\[
q_5=n_5=0,
\qquad
m=4g_5,
\qquad
T=2g_5,
\qquad
\mathfrak q=0.
\]

`high-funnel-two-adic-balance.md` 给

\[
v_2(a)=0,
\]

且 overlap 参数 `c,epsilon` 为二进单位；pure common 的 5-adic ledger又给

\[
v_5(a)=v_5(c_3)=0,
\]

所以

\[
\boxed{(a_0\varepsilon,10)=1.}
\tag{4.1}

因此若定义

\[
\boxed{d:=(a_0,\varepsilon),}
\tag{4.2}

则 `(3.4)` 直接成为完整整数整除

\[
\boxed{d\mid\lambda.}
\tag{4.3}

---

## 5. exclusive `epsilon` support必须进入 `G_0`

`high-funnel-gap-square-core.md` 在 pure common上给

\[
\boxed{
 a_0G_0
=\varepsilon\mu_0^2,
\qquad
\mu_0:=\frac{\mu}{5^{g_5}}\in\mathbf Z,
}
\tag{5.1}

其中 `mu_0` 为 5-unit。

写

\[
\boxed{
a_0=dA,\qquad\varepsilon=dE,\qquad(A,E)=1.}
\tag{5.2}

把 `(5.2)` 代入 `(5.1)` 并约去 `d`：

\[
\boxed{A G_0=E\mu_0^2.}
\tag{5.3}

因为 `(A,E)=1`：

\[
\boxed{E\mid G_0.}
\tag{E-to-G0}

令

\[
G_1:=G_0/E.
\]

则 `(5.3)` 进一步化为

\[
\boxed{A G_1=\mu_0^2.}
\tag{Residual-square}

所以 pure common 的 `epsilon` 被 canonical 地分成：

- common part `d`：完整进入 `lambda`；
- exclusive part `E`：完整进入 `G_0`。

特别地

\[
\boxed{\varepsilon=dE\mid\lambda G_0.}
\tag{5.4}

---

## 6. gap squarefree support也只剩两个 payer

由

\[
a_0=dA,
\qquad d\mid\lambda,
\]

以及 `(Residual-square)`：

若 prime `p` 在 `A` 中以奇次出现，则它必须在 `G_1` 中也以奇次出现。
因此

\[
\boxed{
\operatorname{rad}(\operatorname{sqfree}(a_0))
\mid
\operatorname{rad}(\lambda G_0).
}
\tag{Gap-two-payer}

这比上一文件的 generic

\[
\operatorname{rad}(\operatorname{sqfree}(a_0))
\mid\operatorname{rad}(5s\varepsilon G_0)
\]

在 pure common sheet上更强：`epsilon` 本身已经被吸收到 `lambda G_0`。

---

## 7. 方法边界与下一接口

现在 pure common / `mathfrak q=0` 的 gap squarefree问题只剩：

\[
\boxed{\lambda\quad\text{与}\quad G_0.}
\]

其中：

- `lambda` 同时进入 sphere common scale `D=Vc lambda` 与 concat gcd
  `C=lambda w`；
- `G_0|2G N_12`，是 primitive recovery gcd；
- `a_0/d` 与 `G_0/E` 的乘积是一个**完全平方**。

下一步应该审计 `gcd(lambda,G_0)` 与 `G_0` 在 prefix norm / denominator overlap
中的 prime-flow；若两者不能同时携带正线性 squarefree height，则 pure common
`2-short` 会进一步有限化。

---

## 8. 状态摘要

- **`已严格完成`**：`Common-to-lambda` full-depth lemma。
- **`已严格完成（pure common）`**：`d|lambda`、`E|G_0`、
  `A(G_0/E)=mu_0^2`、`epsilon|lambda G_0`。
- **`结构压缩`**：pure common gap squarefree support只剩 `lambda/G_0` 两 payer。
- **`待证`**：`gcd(lambda,G_0)` 与两 payer simultaneous height；
  `Final-5 + 2-short`；sector-to-global reoptimization；DD global closure。

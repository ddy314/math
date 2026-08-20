# DD 第二次 Schmidt rough core 的 `d_0` allocation

> **依赖：** [`gcd-normal-exact-small-factor.md`](gcd-normal-exact-small-factor.md)、
> `global-framework.md` 的 denominator prime graph、`core.md` 的 gcd-normal form。
>
> **严格状态：** `已严格完成（整个 DD gcd-normal tail 的 non-decimal support）`。
>
> general exact small-factor normalization 已说明，第二次 Schmidt rough product中
> `x=(u+2v)/delta` 一侧已经进入 `F_-`；唯一尚未定位的是
> \[
> \operatorname{core}_{10}(d_0),
> \qquad d_0=(u,Q).
> \]
> 本文证明：任何 `p` 不整除 10 且 `p|d_0`，前两 denominator 在 `p` 处必须
> **equal valuation**。令
> \[
> h_{12}=(b_1,b_2),\qquad C_Q:=Q/h_{12},
> \]
> 则
> \[
> \boxed{
> \operatorname{core}_{10}(d_0)^2
> \mid
> \gamma C_Q^2,
> }
> \]
> 并且更贴近 small factor地有
> \[
> \boxed{
> \operatorname{core}_{10}(d_0)
> \mid
> \frac{g_*}{v}\,C_Q.
> }
> \]
> 因而第二次 Schmidt尚未被 `F_-` 支付的唯一 rough pool缩成 primitive
> prefix-concat cancellation factor `C_Q`。

---

## 1. 固定一个 `d_0` rough prime

沿用 gcd-normal notation：

\[
\kappa=\gamma u,\qquad G=\gamma v,\qquad(u,v)=1,
\]

\[
d_0=(u,Q),\qquad u=d_0r,\qquad Q=d_0q,\qquad(r,q)=1,
\]

且 `r|10^m`。

固定

\[
p\nmid10,\qquad p\mid d_0.
\]

记

\[
h:=v_p(d_0)>0,
\qquad j:=v_p(q),
\]

以及 denominator valuations

\[
e_i:=v_p(b_i),\qquad i=1,2,3.
\]

由 `gcd-normal-exact-small-factor.md` 的 tail recovery

\[
b_3=v\frac{10^m}{r}q.
\]

因为 `p|u` 且 `(u,v)=1`：

\[
p\nmid v.
\]

又 `p` 不整除 `10r`，所以

\[
\boxed{e_3=j.}
\tag{1.1}

而

\[
\boxed{v_p(Q)=h+j.}
\tag{1.2}

同时 `p|u`、`p` 不整除 `v` 意味着

\[
v_p(\kappa)>v_p(G),
\]

故

\[
\boxed{v_p(\gamma)=v_p(G)=e_1+e_2.}
\tag{1.3}

---

## 2. 前两 denominator 必须 equal valuation

反设

\[
e_1\ne e_2.
\]

由于 `p` 不整除 10，二项

\[
Q=b_1 10^{m_2}+b_2
\]

的两个 summands valuation不同，因此没有 cancellation：

\[
\boxed{v_p(Q)=\min(e_1,e_2).}
\tag{2.1}

结合 `(1.2)`：

\[
\min(e_1,e_2)=h+j>j=e_3.
\tag{2.2}

所以三个 denominator valuations中，较大的那个 prefix exponent是**唯一最大值**。

但 denominator prime graph 的 odd-prime unique-max rule证明：若某一块唯一取得最大值，
另外两块的 `p`-adic exponents必须相等。

例如若 `e_1>e_2`，必须

\[
e_2=e_3=j,
\]

这与 `(2.2)` 的 `e_2=h+j>j` 矛盾。另一方向相同。

因此

\[
\boxed{e_1=e_2=:E.}
\tag{Equal-prefix}

这说明每个 `d_0` rough prime都是

\[
\boxed{\text{equal-prefix denominator depth + genuine }Q\text{-cancellation}}
\]

类型，而不是 arbitrary denominator imbalance prime。

---

## 3. primitive concat cancellation depth

定义

\[
\boxed{h_{12}:=(b_1,b_2),}
\qquad
\boxed{C_Q:=Q/h_{12}.}
\tag{3.1}

在当前 `p`：

\[
v_p(h_{12})=E.
\]

由 `(1.2)`：

\[
\boxed{
v_p(C_Q)=h+j-E.}
\tag{3.2}

右端自动非负，因为 equal valuations至少强制 `p^E|Q`。

由 `(1.3)` 与 `(Equal-prefix)`：

\[
\boxed{v_p(\gamma)=2E.}
\tag{3.3}

于是

\[
\begin{aligned}
v_p(\gamma C_Q^2)
&=2E+2(h+j-E)\\
&=2h+2j\\
&\ge2h.
\end{aligned}
\]

所以对每个 `p|core_10(d_0)`：

\[
2v_p(d_0)
\le v_p(\gamma C_Q^2).
\]

逐素数相乘得到

\[
\boxed{
\operatorname{core}_{10}(d_0)^2
\mid
\gamma C_Q^2.
}
\tag{d0-square-allocation}

---

## 4. 把 `gamma` payer换成 actual small-factor overlap

`core.md` 的 denominator overlap满足

\[
\boxed{g_*=G/c_3,}
\]

而 `G=gamma v`，所以

\[
\boxed{
\frac{g_*}{v}=\frac\gamma{c_3}.}
\tag{4.1}

需要比较 `c_3=q_lcm/b_3` 的 `p`-depth。

当前

\[
e_1=e_2=E,\qquad e_3=j.
\]

因此

\[
\boxed{v_p(c_3)=\max(E,j)-j.}
\tag{4.2}

从而

\[
v_p(g_*/v)
=2E-\max(E,j)+j.
\tag{4.3}

与 `(3.2)` 相加。若 `E>=j`：

\[
(E+j)+(h+j-E)=h+2j\ge h.
\]

若 `j>E`：

\[
2E+(h+j-E)=h+E+j\ge h.
\]

所以统一有

\[
\boxed{
v_p(d_0)
\le
v_p(g_*/v)+v_p(C_Q).}
\tag{4.4}

逐 rough primes相乘：

\[
\boxed{
\operatorname{core}_{10}(d_0)
\mid
\frac{g_*}{v}\,C_Q.
}
\tag{d0-F-payer}

这里 `g_*/v` 已经是
`gcd-normal-exact-small-factor.md` 中 actual normalized small-factor quotient

\[
F_-=r(u+2v)\,a(g_*/v)
\]

的一部分。因此第二次 Schmidt的 `d_0` rough height中，只有被 `C_Q` 支付的部分
没有同时自动出现在 `F_-`。

---

## 5. 与第二次 Schmidt rough product 联立

第二次 fixed-target Schmidt theorem使用

\[
\delta=(u,u+2v)=(u,2)\in\{1,2\},
\]

\[
x=(u+2v)/\delta,\qquad y=u/\delta.
\]

因为 `r` 是 2,5-smooth，

\[
\boxed{
\operatorname{core}_{10}(y)
=\operatorname{core}_{10}(d_0).
}
\tag{5.1}

而 `x`-side rough core完整整除 `u+2v`，已由 exact small factor支付。

Schmidt 给

\[
\log_{10}\operatorname{core}_{10}(x)
+
\log_{10}\operatorname{core}_{10}(d_0)
\ge S-o(S).
\tag{5.2}

使用 `(d0-F-payer)`：若记

\[
C_h:=\log_{10}C_Q,
\]

则除 `C_Q` 这一份 cancellation height外，`(5.2)` 强迫的 rough mass都已经
进入 actual factor

\[
(u+2v)(g_*/v)\mid F_-/r a
\]

的对应部分。

因此 post-tail side-branch reoptimization真正剩余的单一 rough pool是

\[
\boxed{C_Q=Q/(b_1,b_2).}
\]

而不是 `d_0`、`q-Z gcd` 或另一个匿名 rough gcd。

---

## 6. `C_Q` 的算术意义

写

\[
b_1=h_{12}B_1,\qquad b_2=h_{12}B_2,\qquad(B_1,B_2)=1.
\]

则

\[
\boxed{
C_Q=B_1 10^{m_2}+B_2.
}
\tag{6.1}

所以 `C_Q` 是**primitive prefix denominator concat cancellation carrier**。

对 `p|d_0` 的 rough support，`p` 不可能来自 unequal denominator valuations；它只能来自
`B_1 10^{m_2}+B_2` 的 genuine p-adic cancellation。

这正对应旧 canonical prime-flow 中 `U`-type cancellation primes的全局版本。

---

## 7. 状态摘要

- **`已严格完成`**：`Equal-prefix`、`d0-square-allocation`、`d0-F-payer`。
- **`结构压缩`**：第二次 Schmidt rough product中，除 actual `F_-` 已支付的
  `x`-core 与 overlap payer外，只剩 primitive concat cancellation `C_Q`。
- **`待证`**：对 `C_Q` 建立 global height / Gaussian split / source cancellation
  charge；完成 post-tail 非 canonical branches reoptimization；DD global explicit slope / absolute height。

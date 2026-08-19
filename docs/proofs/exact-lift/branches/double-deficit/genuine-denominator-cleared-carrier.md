# DD genuine-Gaussian cross carrier 的 denominator-cleared digit form

> **依赖：** [`genuine-discriminant-carrier.md`](genuine-discriminant-carrier.md)、[`genuine-discriminant-cross-audit.md`](genuine-discriminant-cross-audit.md)。
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

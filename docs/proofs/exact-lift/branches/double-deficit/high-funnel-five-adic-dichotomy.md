# DD slope `>7` S-unit funnel 的 exact 5-adic tail-root dichotomy

> **依赖：** `core.md` §§9–16 的 high-funnel 5-resonance、`global-framework.md` 的 unified tail-root discriminant、`core.md` §18 的 `W=L Xi`。
>
> **严格状态：** `已严格完成`（适用于旧证明中所有进入 slope `>7` 唯一 S-unit funnel 的 DD 候选；不要求逼近 `6.308883...` equality frontier）。本文把 frontier 5-adic closure推广成一个 exact finite-height dichotomy。
>
> 记
> \[
> B_5=v_5(b_3),\quad
> q_5=v_5(Q),\quad
> g_5=v_5(G),\quad
> n_5=v_5(\mathcal N_{12}).
> \]
> 则 high-funnel 候选必须满足至少一个：
> \[
> \boxed{m\le5q_5+4g_5+n_5}
> \tag{Defect-heavy}
> \]
> 或
> \[
> \boxed{3d\le m+4q_5+5g_5+2n_5.}
> \tag{Tail-short}
> \]
>
> 因此若 prefix/common 5-adic defects都只有 `o(S)`，自动有 `3d<=m+o(S)`；这立即排除旧 extremal frontier，并把下一阶段问题压成“defect-heavy branch vs short-tail branch”。

---

## 1. high-funnel 5-adic baseline

旧 `core.md` 已证明，任何渐近 slope `>7` 的 DD 候选最终都进入唯一 funnel，并满足

\[
\boxed{5\mid b_3,\qquad k_5>g_5,}
\tag{1.1}

以及 exact 5-resonance

\[
\boxed{
3k_5=2m+2q_5+g_5+n_5,
}
\tag{5-res}

其中

\[
k_5=v_5(\kappa).
\]

由 exact tail weight

\[
\kappa b_3=10^mQG
\]

取 5-adic valuation：

\[
\boxed{
k_5=m+q_5+g_5-B_5.}
\tag{1.2}

把 `(1.2)` 与 `(5-res)` 联立：

\[
\boxed{
3B_5=m+q_5+2g_5-n_5.
}
\tag{B5-formula}

---

## 2. tail-root 自身已经给模 `5^d` 的两项同余

DD unified tail-root original identity是

\[
\boxed{
\mathscr T a_3
=\kappa G^2 10^dA_{12}
+\eta(\kappa+G)W,
}
\tag{2.1}

其中

\[
\boxed{
\mathscr T=\frac{\kappa^2(\kappa+2G)}{10^m}.
}
\tag{2.2}

模 `5^d` 直接得到

\[
\boxed{
\mathscr T a_3
\equiv
\eta(\kappa+G)W
\pmod{5^d}.}
\tag{Tail-5}

因为 `5|b_3` 且 `(a_3,b_3)=1`：

\[
\boxed{v_5(a_3)=0.}
\tag{2.3}

这说明 carry / terminal `R_0` 并不是 5-adic mismatch 的必要输入。

---

## 3. 左边的 exact 5-depth

由

\[
k_5>g_5
\]

且 `5` 为奇素数：

\[
\boxed{v_5(\kappa+2G)=g_5.}
\tag{3.1}

因此

\[
\boxed{
 r:=v_5(\mathscr T a_3)
=2k_5+g_5-m.
}
\tag{3.2}

用 `(1.2)`：

\[
\boxed{
 r=m+2q_5+3g_5-2B_5.
}
\tag{3.3}

也可用 resonance `(5-res)` 消掉 `k_5`：

\[
\boxed{
3r=m+4q_5+5g_5+2n_5.
}
\tag{r-res}

---

## 4. 当 denominator 5-depth 足够大时，右边严格更深

DD §18 的 unified discriminant root满足

\[
\boxed{W=L\Xi,\qquad\Xi\in\mathbf Z.}
\tag{4.1}

这里

\[
L=\frac{10^m}{(10^m,b_3)}.
\]

若

\[
\boxed{B_5>2q_5+2g_5,}
\tag{4.2}

则由 `(B5-formula)` 等价地有

\[
\boxed{m>5q_5+4g_5+n_5.}
\tag{4.3}

特别地 `(4.3)` 保证 `B_5<m`，故

\[
\boxed{v_5(L)=m-B_5.}
\tag{4.4}

于是

\[
v_5(W)\ge m-B_5.
\]

又因为 `k_5>g_5`：

\[
\boxed{v_5(\kappa+G)=g_5.}
\tag{4.5}

所以右边

\[
s:=v_5((\kappa+G)W)
\]

满足

\[
\boxed{s\ge m+g_5-B_5.}
\tag{4.6}

与 `(3.3)` 比较：

\[
\begin{aligned}
s-r
&\ge
(m+g_5-B_5)
-(m+2q_5+3g_5-2B_5)\\
&=\boxed{B_5-2q_5-2g_5}>0.
\end{aligned}
\tag{4.7}

因此在 `(4.2)` 分支，`Tail-5` 两项 valuation严格不同，较浅项一定是左边：

\[
\boxed{
v_5\bigl(\mathscr T a_3-\eta(\kappa+G)W\bigr)=r.
}
\tag{4.8}

但该差被 `5^d` 整除，所以

\[
\boxed{d\le r.}
\tag{4.9}

再代入 `(r-res)`：

\[
\boxed{
3d\le m+4q_5+5g_5+2n_5.
}
\tag{Tail-short}

---

## 5. 另一分支就是 defect-heavy inequality

若 `(4.2)` 不成立：

\[
B_5\le2q_5+2g_5.
\]

利用 `(B5-formula)`：

\[
m+q_5+2g_5-n_5
\le6q_5+6g_5.
\]

所以

\[
\boxed{
m\le5q_5+4g_5+n_5.}
\tag{Defect-heavy}

因此 high-funnel 中每个候选都必须落入

\[
\boxed{
\text{`Defect-heavy`}
\quad\cup\quad
\text{`Tail-short`}.
}
\tag{Five-dichotomy}

这是 exact finite-height dichotomy，没有 `o(S)`。

---

## 6. extremal frontier 是其直接推论

旧 `6.308883...` frontier满足

\[
\frac mS\to2.808883577618\ldots,
\qquad
\frac dS\to3.5,
\]

以及 prefix polarization / one-channel：

\[
q_5=o(S),
\qquad
g_5=o(S),
\qquad
n_5=o(S).
\]

于是 `Defect-heavy` 不可能，因为其右边为 `o(S)` 而 `m` 为正线性。

`Tail-short` 则退化为

\[
3d\le m+o(S),
\]

即

\[
10.5S+o(S)
\le2.808883577618\ldots S+o(S),
\]

同样不可能。

所以 `frontier-five-adic-closure.md` 的矛盾也可由本文更一般的 dichotomy直接恢复。

---

## 7. 下一步：把 defect-heavy 支喂回 stability inequality

旧 stability inequality有

\[
n<c_*S+C_*-\Pi,
\]

其中 `Pi` 的每个 defect coefficient严格为正。

`Five-dichotomy` 表明：任何试图保持大 `m,d` 的 high-funnel candidate，都必须让

\[
q_5,\quad g_5,\quad n_5
\]

至少一个获得正线性高度。

因此下一步不再需要假设精确 equality frontier；真正目标是从旧 stability derivation恢复 `q_5,g_5,n_5` 在 `Pi` 中的显式 coefficients，并与

\[
\text{`Defect-heavy` / `Tail-short`}
\]

做线性规划，从而给出新的显式 asymptotic slope。

---

## 8. 状态摘要

- **`已严格完成（high-funnel）`**：`B5-formula`、`r-res`、5-adic two-term comparison、`Five-dichotomy`。
- **`已严格完成` 的推论**：extremal `6.308883...` frontier为空。
- **`待证`**：恢复 stability defect `Pi` 的显式系数并求新的最优 slope；DD 全局空性 / effective absolute height bound。

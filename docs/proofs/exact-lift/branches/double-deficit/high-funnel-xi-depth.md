# DD high-funnel `Defect-heavy` slack 的 canonical `Xi`-depth

> **依赖：** [`high-funnel-five-adic-dichotomy.md`](high-funnel-five-adic-dichotomy.md)、[`high-funnel-defect-optimization.md`](high-funnel-defect-optimization.md)、`global-framework.md` 的 unified discriminant、`core.md` §18 的 `W=L Xi`。
>
> **严格状态：** `已严格完成（asymptotic high-funnel）`。本文继续拆 `Defect-heavy`
> \[
> m\le5q_5+4g_5+n_5.
> \]
> 先证明若第三分母的 5-depth `B_5=v_5(b_3)` 满足 `B_5>=m`，则 defect-aware stability 立即给 slope `<=6`。所以任何仍可能承载 slope `>6` 的 defect-heavy 无界序列最终必须有 `B_5<m`。
>
> 在 `B_5<m` 且 slope `>7` 的唯一 funnel中，global tail bound `limsup m/S<=5` 保证 `d>q_5`，从而 unified discriminant 的两项 5-adic valuation严格分离。于是
> \[
> v_5(W)=2k_5-m.
> \]
> 再用 `W=L Xi` 精确得到
> \[
> \boxed{
> 3v_5(\Xi)=5q_5+4g_5+n_5-m.
> }
> \]
> 因此 `Defect-heavy` 不再是三个散乱 defect 的任意组合：它的全部 slack正好集中到 DD §18 的单一判别 quotient `Xi=|mathcal M-C_0a|` 的 5-adic 深度。

---

## 1. high-funnel exact identities

沿用

\[
B_5=v_5(b_3),
\quad q_5=v_5(Q),
\quad g_5=v_5(G),
\quad n_5=v_5(\mathcal N_{12}),
\quad k_5=v_5(\kappa).
\]

high-funnel 5-resonance与 tail weight给

\[
\boxed{3k_5=2m+2q_5+g_5+n_5,}
\tag{1.1}

\[
\boxed{k_5=m+q_5+g_5-B_5.}
\tag{1.2}

所以

\[
\boxed{3B_5=m+q_5+2g_5-n_5.}
\tag{1.3}

---

## 2. `B_5>=m` 支自动只有 slope `<=6`

若

\[
B_5\ge m,
\]

由 `(1.3)`：

\[
3m\le m+q_5+2g_5-n_5,
\]

即

\[
\boxed{2m+n_5\le q_5+2g_5.}
\tag{2.1}

特别地

\[
m\le\frac12q_5+g_5-rac12n_5.
\]

而显然

\[
\frac12q_5+g_5-rac12n_5
\le2q_5+g_5+n_5
\]

对非负 `q_5,g_5,n_5` 成立。因此

\[
\boxed{m\le2q_5+g_5+n_5.}
\tag{2.2}

`high-funnel-defect-optimization.md` 的 defect-aware stability为

\[
n<6S+\frac{2b}{3}m
-2a\mathfrak q-a\mathfrak n
-\frac{2b}{3}(2q_5+g_5+n_5)
+O(1),
\]

其中 `a,b>0`。丢掉非正的 2-adic defect项，并使用 `(2.2)`：

\[
\boxed{n<6S+O(1).}
\tag{BgeM-six}

所以任何无界 sequence 若满足

\[
\limsup n/S>6,
\]

则 sufficiently far out 必有

\[
\boxed{B_5<m.}
\tag{2.3}

特别地，当前 slope `>7` funnel 的真正 defect-heavy 难支必在 `B_5<m`。

---

## 3. discriminant 两项在 `B_5<m` 高锥中严格分离

DD unified discriminant为

\[
\boxed{
W^2
=(\kappa G C_{\rm DD})^2
-Q^2\mathcal N_{12}\kappa(\kappa+2G),
}
\tag{3.1}

其中

\[
C_{\rm DD}=10^dA_{12}.
\]

记

\[
a_5:=v_5(A_{12})\ge0.
\]

high-funnel有 `k_5>g_5`，故

\[
v_5(\kappa+2G)=g_5.
\]

第一项 valuation为

\[
R_1=2(k_5+g_5+d+a_5).
\tag{3.2}

第二项 valuation为

\[
R_2=2q_5+n_5+k_5+g_5.
\tag{3.3}

用 `(1.1)` 消去 `n_5`：

\[
\boxed{R_2=4k_5-2m.}
\tag{3.4}

两者之差：

\[
\begin{aligned}
R_1-R_2
&=2(k_5+g_5+d+a_5)-(4k_5-2m)\\
&=2(m+g_5+d+a_5-k_5)\\
&=\boxed{2(d+a_5+B_5-q_5)},
\end{aligned}
\tag{3.5}

其中最后一步用了 `(1.2)`。

现在只考虑 slope `>7` 的无界 sequence。旧 Schmidt tail result已有

\[
\limsup m/S\le5.
\]

而 `n/S>7+o(1)`，故

\[
d=n-m>2S-o(S).
\]

另一方面 `Q<10^S` 给

\[
q_5\log_{10}5<S,
\]

即

\[
q_5<\log_5(10)S=1.430676\ldots S.
\]

因此 eventually

\[
\boxed{d>q_5.}
\tag{3.6}

由 `a_5,B_5>=0`，(3.5) 严格为正。所以 discriminant 两项 5-depth不同，差的 valuation等于较浅的第二项：

\[
2v_5(W)=R_2=4k_5-2m.
\]

因此

\[
\boxed{v_5(W)=2k_5-m.}
\tag{W5-exact}

---

## 4. `W=L Xi` 把全部 defect slack 收进 `Xi`

`B_5<m` 时

\[
L=\frac{10^m}{(10^m,b_3)}
\]

满足

\[
\boxed{v_5(L)=m-B_5.}
\tag{4.1}

而 DD §18 有同一个 unified discriminant root的精确 factorization

\[
\boxed{W=L\Xi,}
\qquad
\Xi=|\mathcal M-C_0a|\in\mathbf Z.
\tag{4.2}

所以 `(W5-exact)` 给

\[
\begin{aligned}
v_5(\Xi)
&=(2k_5-m)-(m-B_5)\\
&=2k_5-2m+B_5.
\end{aligned}
\tag{4.3}

用 `(1.2)`：

\[
\boxed{v_5(\Xi)=2q_5+2g_5-B_5.}
\tag{4.4}

再用 `(1.3)` 消掉 `B_5`：

\[
\begin{aligned}
3v_5(\Xi)
&=6q_5+6g_5-(m+q_5+2g_5-n_5)\\
&=\boxed{5q_5+4g_5+n_5-m.}
\end{aligned}
\tag{Xi-slack}

这就是 defect-heavy slack 的 canonical factorization。

---

## 5. branch condition 等价于 `Xi` 的非负深度

因为 `Xi` 是整数，当然

\[
v_5(\Xi)\ge0.
\]

`(Xi-slack)` 因而重新给出

\[
m\le5q_5+4g_5+n_5,
\]

也就是 `Defect-heavy`。

但新的内容是方向相反也已识别：

\[
\boxed{
5q_5+4g_5+n_5-m
=3v_5(\Xi).
}
\]

所以大 slope想躲进 defect-heavy时，不能任意把 deficit分散给 `q_5,g_5,n_5`；三者的组合必须恰好形成一个真实整数 `Xi` 的 5-adic depth。

这给下一步提供唯一目标：

> 对
> \[
> \Xi=|\mathcal M-C_0a|
> \]
> 建立独立的 Archimedean / reducedness / carrier 上界，或证明正线性 `v_5(Xi)` 必须再次进入已关闭的 5-adic angular / source channel。

---

## 6. 当前 high-funnel 压缩

`high-funnel-defect-optimization.md` 已证明 Tail-short branch

\[
\limsup n/S\le6.215109404735\ldots.
\]

本文又证明 `B_5>=m` branch只有 slope `<=6`。

所以任何可能保持

\[
\limsup n/S>6.215109404735\ldots
\]

的 double-resonant `t_2=1` high-funnel sequence，最终必须满足：

\[
\boxed{
B_5<m,
\qquad
v_5(\Xi)=\frac{5q_5+4g_5+n_5-m}{3}>0
}
\]

（若最后等于零则恰在 Tail-short/Defect-heavy 边界，可由闭包处理）。

真正未决对象因此已经从四个 valuation变量压成：

\[
\boxed{\text{positive-linear 5-adic depth of the single integer }\Xi.}
\]

---

## 7. 状态摘要

- **`已严格完成`**：`B_5>=m => n<6S+O(1)`；`B_5<m` high-slope discriminant valuation；`Xi-slack`。
- **`结构压缩`**：remaining defect-heavy slack equals `3 v_5(Xi)` exactly.
- **`待证`**：positive-linear `v_5(Xi)` exclusion or strict bound；new global numerical limsup；DD global emptiness/effective height bound。

# DD `Final-5-lock` 上的 `2-balanced` sector collapse

> **依赖：** [`high-funnel-exact-small-factor-normalization.md`](high-funnel-exact-small-factor-normalization.md)、
> [`high-funnel-two-adic-balance.md`](high-funnel-two-adic-balance.md)、
> [`high-funnel-denominator-max-lock.md`](high-funnel-denominator-max-lock.md)、
> `core.md` 的 `Q/G` constant window、small-factor Archimedean upper bound与固定目标 Schmidt Subspace Theorem。
>
> **严格状态：** `已严格完成（conditional canonical t_2=1 / Final-5 sector）`。
> 本文不是新的全 DD numerical limsup；它关闭 `Final-5-lock` 中的
> `2-balanced` sheet 到
> \[
> \boxed{
> \limsup\frac nS
> \le
> \frac{13+10\log_{10}2}{2(1+\log_{10}2)}
> =6.152932680260\ldots.
> }
> \]
> 因而在当前 canonical sector 内，任何试图保持 slope
> `>6.215109404735...` 的 remaining sequence只能进入 `2-short`。

---

## 1. 归一化变量

记

\[
a:=\log_{10}2,
\qquad
b:=\log_{10}5=1-a.
\]

对无界 sequence 除以 `S`，记

\[
M:=\frac mS,
\qquad
Q_5:=\frac{q_5}{S},
\qquad
G_5:=\frac{g_5}{S},
\qquad
N_5:=\frac{n_5}{S},
\]

\[
Q_2:=\frac{\mathfrak q}{S},
\qquad
N_2:=\frac{\mathfrak n}{S},
\qquad
G_2:=\frac{\mathfrak g}{S},
\]

并记

\[
G_0:=\frac{\log_{10}\gamma_0}{S},
\]

其中

\[
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0,
\qquad
(\gamma_0,10)=1.
\]

`Final-5-lock` 给

\[
\boxed{M=2Q_5+4G_5+N_5.}
\tag{1.1}

因此

\[
\boxed{G_5\le\frac M4.}
\tag{1.2}

同时

\[
T=m-2g_5,
\]

故

\[
\frac TS=M-2G_5.
\tag{1.3}

---

## 2. defect-aware Schmidt budget

`high-funnel-two-adic-balance.md` 已在 `Final-5-lock` 上证明

\[
\boxed{
(1+a)M+2aQ_2+aN_2+2G_0\le3+o(1).
}
\tag{Schmidt-budget}

这里已经使用固定目标 Schmidt Subspace Theorem

\[
\liminf\frac{\log U+\log Z}{S}\ge1.
\]

后续只把 `(Schmidt-budget)` 作为一个已经完成的非有效 asymptotic 输入。

---

## 3. exact small-factor normalization 在 `Final-5` 上的最小高度

新 exact normalization 为

\[
F_-=
\frac{2^{H+2}5^TZ}{s}
\;a_{\rm gap}\frac{g_*}{V},
\qquad
s=(2\cdot5^T,q).
\tag{3.1}

为避免与常数 `a=log10 2` 混淆，本文把 sphere-gap quotient写成
`a_gap`。

`Final-5-lock` 给

\[
v_5(a_{\rm gap})=q_5.
\tag{3.2}

又因 `b_3` 为 5-adic maximum，`c_3=q_lcm/b_3` 在 5 处为 unit，而

\[
g_*=G/c_3,
\qquad
V\text{ 为 5-unit},
\]

所以

\[
\boxed{v_5(g_*/V)=g_5.}
\tag{3.3}

同时 `(1.1)` 与 `(1.3)` 给

\[
T=2q_5+2g_5+n_5\ge q_5.
\]

因此

\[
v_5(s)=q_5.
\tag{3.4}

所以 `(3.1)` 的 net 5-adic contribution至少为

\[
T-q_5+(q_5+g_5)=T+g_5=m-g_5.
\]

更方便地，令

\[
U_h:=\frac{\log_{10}U}{S}.
\]

S-unit phase

\[
2^HZ=5^TU+V
\]

与 tail window给

\[
\frac{H\log_{10}2+\log_{10}Z}{S}
=b\frac TS+U_h+o(1).
\tag{3.5}

于是从 `(3.1)`–`(3.4)`：

\[
\boxed{
\frac{\log_{10}F_-}{S}
\ge
b(2M-3G_5)+U_h+o(1).
}
\tag{F-lower}

另一方面 canonical `d`-dominant small-factor upper bound为

\[
\log_{10}F_-<4S+2m-n+O(1).
\]

故若

\[
C:=\limsup\frac nS,
\]

则沿相应子序列

\[
\boxed{
C\le4+2aM+3bG_5-U_h.
}
\tag{F-slope}

---

## 4. `U` 的 exact height identity

`Q` 是前两 denominator 的十进制拼接，因此

\[
\log_{10}Q=S+O(1).
\]

而 `Q/G` 位于固定常数窗口

\[
1<Q/G\le11,
\]

所以

\[
\log_{10}G=S+O(1).
\]

又

\[
\kappa=2\gamma5^TU,
\]

且

\[
QG<\kappa\le10QG.
\]

因此

\[
\frac{\log_{10}\kappa}{S}=2+o(1).
\]

展开 `kappa`：

\[
\boxed{
U_h
=2-aG_2-G_0-b(M-G_5)+o(1).
}
\tag{U-height}

将 `(U-height)` 代入 `(F-slope)`：

\[
\boxed{
C
\le
2+(1+a)M+2bG_5+aG_2+G_0+o(1).
}
\tag{4.1}

---

## 5. `2-balanced` 把 `G_2` 锁死

`high-funnel-two-adic-balance.md` 的第二支是

\[
2\mathfrak g=m+\mathfrak q+\ell-2,
\]

其中 `ell` 只有 `0/1`，故归一化后

\[
\boxed{2G_2=M+Q_2+o(1).}
\tag{2-balanced}

代入 `(4.1)`：

\[
\begin{aligned}
C
&\le
2+(1+a)M+2bG_5
+\frac a2(M+Q_2)+G_0+o(1)\\
&=2+\left(1+\frac{3a}{2}\right)M
+2bG_5+\frac a2Q_2+G_0+o(1).
\end{aligned}
\tag{5.1}

由 `(1.2)`：

\[
2bG_5\le\frac b2M.
\]

而

\[
1+\frac{3a}{2}+\frac b2
=\frac32+a.
\]

所以

\[
\boxed{
C
\le
2+\left(\frac32+a\right)M
+\frac a2Q_2+G_0+o(1).
}
\tag{5.2}

---

## 6. 一行 dual certificate

`(Schmidt-budget)` 是

\[
(1+a)M+2aQ_2+aN_2+2G_0\le3+o(1).
\]

对 budget 中各变量，`(5.2)` 的收益/成本比分别为

\[
\frac{\frac32+a}{1+a},
\qquad
\frac{a/2}{2a}=\frac14,
\qquad
0,
\qquad
\frac12.
\]

而

\[
\frac{\frac32+a}{1+a}>\frac12>\frac14.
\]

所以线性目标的最大值在全部 budget送给 `M` 时取得。严格地，将
`(Schmidt-budget)` 乘

\[
\lambda:=\frac{\frac32+a}{1+a}
\]

即可支配 `(5.2)` 中 `M,Q_2,G_0` 的全部正系数；`N_2` 系数本来为零。
因此

\[
\boxed{
C
\le
2+3\frac{\frac32+a}{1+a}.
}
\tag{6.1}

化简：

\[
\boxed{
C
\le
\frac{13+10a}{2(1+a)}.
}
\tag{6.2}

代入

\[
a=\log_{10}2
\]

得到

\[
\boxed{
C
\le
6.152932680260\ldots.
}
\tag{2-balanced-slope}

---

## 7. 对当前 branch picture 的含义

此前 `high-funnel-defect-optimization.md` 已把 `Tail-short` sector压到

\[
6.215109404735\ldots.
\]

而当前 `Final-5-lock` 是继续研究任何企图高于这一常数的 canonical
`Defect-heavy` sequence。现在其中的 `2-balanced` sheet又满足

\[
6.152932680260\ldots
<6.215109404735\ldots.
\]

因此：

\[
\boxed{
\text{在当前 canonical sector 中，若 }
\limsup n/S>6.215109404735\ldots,
\text{ 则 eventually 必在 `2-short`。}
}
\tag{Remaining-2-short}

这里仍不声称所有 slope `>6.215...` 的 DD sequence自动进入该 canonical
funnel；原 funnel 的全局作用域必须按 `core.md` 的既有分类读取。

---

## 8. 状态摘要

- **`已严格完成（sector）`**：`F-lower`、`U-height`、`2-balanced` dual bound。
- **`显式 sector bound`**：`2-balanced <= 6.152932680260...`。
- **`结构压缩`**：`Final-5` 中高于 `6.215109...` 的 remaining sheet只剩 `2-short`。
- **`待证`**：`Final-5 + 2-short`；将 sector-level improvement重新接回全 DD 分类；有效全局 slope / DD 空性。

# DD double-resonant high funnel 的 defect-aware stability 与 `6.215109...` tail-short bound

> **依赖：** [`high-funnel-five-adic-dichotomy.md`](high-funnel-five-adic-dichotomy.md)、`core.md` 的 `t_2=1` 二进 resonance、五进 resonance、`F_-` small-factor 上界与两个 multiplicative height bounds。
>
> **严格状态：** `已严格完成`（适用于旧证明中的 `b_3` 二进独大、`t_2=1`、2/5 双 resonance S-unit funnel）。本文重新展开旧 stability calculation，不再把 `q_5,g_5,n_5` 惩罚粗化掉。
>
> 得到两项新结果：
>
> 1. defect-aware stability
>    \[
>    n<6S+\frac{2b}{3}m
>    -2a\mathfrak q-a\mathfrak n
>    -\frac{2b}{3}(2q_5+g_5+n_5)
>    +5+2a,
>    \]
>    其中 `a=log10 2`, `b=log10 5`；
> 2. 在新 5-adic dichotomy 的 `Tail-short` 支，线性优化给显式
>    \[
>    \boxed{
>    \limsup\frac nS
>    \le
>    \frac{28}{3+5\log_{10}2}
>    =6.215109404735\ldots.}
>    \]
>
> 因而 double-resonant funnel 中任何 asymptotic slope 高于 `6.215109...` 的候选都必须进入 `Defect-heavy` 支
> \[
> m\le5q_5+4g_5+n_5.
> \]
> 本文没有关闭该 defect-heavy 支，因此不是新的全 DD numerical limsup bound。

---

## 1. 记号

令

\[
a:=\log_{10}2,
\qquad
b:=\log_{10}5=1-a.
\]

二进记号：

\[
\mathfrak q=v_2(Q),
\qquad
\mathfrak g=v_2(G),
\qquad
\mathfrak n=v_2(\mathcal N_{12}),
\]

\[
\mathfrak f=v_2(\kappa+2G).
\]

五进记号：

\[
q_5=v_5(Q),
\quad
g_5=v_5(G),
\quad
n_5=v_5(\mathcal N_{12}),
\quad
k_5=v_5(\kappa).
\]

定义

\[
\boxed{
\mathscr A_5:=2q_5+g_5+n_5.
}
\tag{1.1}

在本文 funnel 中：

\[
\boxed{
\mathfrak f+\mathfrak g+3
=2m+2\mathfrak q+\mathfrak n
}
\tag{2-res}

以及

\[
\boxed{
3k_5=2m+\mathscr A_5.
}
\tag{5-res}

此外 `t_2=1` 的 S-unit normalization给

\[
v_2(\kappa)=\mathfrak g+1.
\tag{1.2}

---

## 2. 保留 defects 的 `F_-` 乘法高度下界

旧 local valuation table在当前 funnel给

\[
\boxed{v_2(F_-)=\mathfrak f+1,}
\tag{2.1}

\[
\boxed{v_5(F_-)=k_5.}
\tag{2.2}

所以

\[
\log_{10}F_-
\ge a(\mathfrak f+1)+bk_5.
\tag{2.3}

由 `(2-res)`：

\[
\mathfrak f+1
=2m+2\mathfrak q+\mathfrak n-\mathfrak g-2.
\]

于是

\[
\begin{aligned}
\log_{10}F_-
\ge{}&
2am+2a\mathfrak q+a\mathfrak n
-a\mathfrak g-2a+bk_5.
\end{aligned}
\tag{2.4}

另一方面

\[
2^{\mathfrak g+1}5^{k_5}\mid\kappa
\]

且 decimal pinning给

\[
\kappa<10QG<10^{2S+1}.
\]

因此

\[
a(\mathfrak g+1)+bk_5<2S+1,
\]

即

\[
-a\mathfrak g
>-2S-1+a+bk_5.
\tag{2.5}

把 `(2.5)` 代入 `(2.4)`：

\[
\log_{10}F_-
>
2am+2a\mathfrak q+a\mathfrak n
-2S-1-a+2bk_5.
\]

再由 `(5-res)`：

\[
2bk_5
=\frac{4b}{3}m+\frac{2b}{3}\mathscr A_5.
\]

故得到 defect-aware lower bound

\[
\boxed{
\log_{10}F_-
>
\left(2a+\frac{4b}{3}\right)m
-2S-1-a
+2a\mathfrak q+a\mathfrak n
+\frac{2b}{3}\mathscr A_5.
}
\tag{Fminus-defect-lower}

旧正文使用的

\[
\log F_->\left(2a+\frac43b\right)m-2S-1-a
\]

正是把最后三项全部丢掉后的弱化版。

---

## 3. defect-aware stability inequality

在 `d`-dominant high funnel，旧 small-factor ratio给

\[
F_-
<2\cdot10^{2S+s+D_s+2m-n+4},
\]

而

\[
s=s_1+s_2\le2,
\qquad
D_s=|s_1-s_2|\le2S-2.
\]

所以

\[
\boxed{
\log_{10}F_-
<4S+2m-n+4+a.
}
\tag{Fminus-upper}

将 `(Fminus-defect-lower)` 与 `(Fminus-upper)` 比较：

\[
\begin{aligned}
n
<{}&6S
+\left[2-2a-\frac{4b}{3}\right]m\\
&-2a\mathfrak q-a\mathfrak n
-\frac{2b}{3}\mathscr A_5
+5+2a.
\end{aligned}
\]

因为

\[
2-2a-\frac{4b}{3}=\frac{2b}{3},
\]

得到

\[
\boxed{
n
<6S+\frac{2b}{3}m
-2a\mathfrak q-a\mathfrak n
-\frac{2b}{3}\mathscr A_5
+5+2a.
}
\tag{Defect-stability}

这就是 handoff 中 `Pi` 对当前关键 defects 的显式恢复。

---

## 4. 重新推导 general combined-height constraint

本节只使用两个普遍 height bounds，不依赖任何固定最高整数层。

首先

\[
2^{\mathfrak g+1}5^{k_5}<\kappa<10^{2S+1},
\]

即

\[
a(\mathfrak g+1)+bk_5<2S+1.
\tag{4.1}

其次

\[
2^{\mathfrak f}<\kappa+2G<11\cdot10^{2S},
\]

所以

\[
a\mathfrak f<2S+c,
\qquad
c:=\log_{10}11.
\tag{4.2}

把 `(2-res)`、`(5-res)` 代入 `(4.1)+(4.2)`，`mathfrak g` 精确消去，得到

\[
\boxed{
\frac{2(1+2a)}{3}m
+2a\mathfrak q+a\mathfrak n
+\frac b3\mathscr A_5
<4S+1+c+2a.
}
\tag{Combined-height}

因此旧 top-layer 文本中的 combined-height 其实是整个 `t_2=1` double-resonant funnel 的通用 inequality；后续只是在最高层中把它用于有限尺寸压缩。

---

## 5. Tail-short branch 的 slope inequality

`high-funnel-five-adic-dichotomy.md` 的 Tail-short branch满足

\[
\boxed{
3d\le m+4q_5+5g_5+2n_5.
}
\tag{5.1}

同时该 branch对应

\[
\boxed{
m>5q_5+4g_5+n_5.}
\tag{5.2}

令 normalized variables

\[
M=\frac mS,
\quad
Q_5=\frac{q_5}{S},
\quad
G_5=\frac{g_5}{S},
\quad
N_5=\frac{n_5}{S}.
\]

忽略 `O(1/S)`，从 `(5.1)`：

\[
\frac nS
=\frac{m+d}{S}
\le
\frac43M
+\frac43Q_5
+\frac53G_5
+\frac23N_5.
\tag{5.3}

从 `(Combined-height)` 丢掉非负二进 defects：

\[
\boxed{
A M
+\frac b3(2Q_5+G_5+N_5)
\le4,
}
\tag{5.4}

其中

\[
\boxed{A:=\frac{2(1+2a)}3.}
\]

而 `(5.2)` 在 limsup optimization 中可闭包为

\[
\boxed{-M+5Q_5+4G_5+N_5\le0.}
\tag{5.5}

---

## 6. LP 有闭式 dual certificate

目标线性型记为

\[
\mathcal L
=\frac43M
+\frac43Q_5
+\frac53G_5
+\frac23N_5.
\]

取两个非负系数

\[
\boxed{
\lambda=\frac{7}{5a+3},
\qquad
\mu=\frac{2(4a+1)}{3(5a+3)}.
}
\tag{6.1}

将 `(5.4)` 乘 `lambda`，将 `(5.5)` 乘 `mu` 并相加。

对 `M,G_5` 的系数恰好分别等于目标中的

\[
\frac43,\qquad\frac53.
\]

对 `Q_5`，组合系数比目标多

\[
\boxed{
\frac{2(a+2)}{5a+3}>0.
}
\tag{6.2}

对 `N_5`，组合系数比目标多

\[
\boxed{
\frac{1-3a}{5a+3}>0,
}
\tag{6.3}

其中最后一步使用

\[
a=\log_{10}2<\frac13
\]

（等价于 `2^3<10`）。

因此所有 normalized variables非负时：

\[
\mathcal L
\le4\lambda
=\boxed{
\frac{28}{5a+3}}.
\tag{6.4}

于是 Tail-short branch严格得到

\[
\boxed{
\limsup
\frac nS
\le
\frac{28}{3+5\log_{10}2}
=6.215109404735\ldots.
}
\tag{Tail-short-slope}

LP 的极值闭包位于

\[
Q_5=N_5=0,
\qquad
M=4G_5,
\]

即恰在 `Tail-short / Defect-heavy` 分界上；这与 dual certificate一致。

---

## 7. 新的 high-funnel branch picture

所以 double-resonant `t_2=1` funnel现在分成：

### A. Tail-short

\[
m>5q_5+4g_5+n_5
\]

则

\[
\boxed{
\limsup n/S\le6.215109404735\ldots.}
\]

### B. Defect-heavy

\[
\boxed{m\le5q_5+4g_5+n_5.}
\]

本文尚未给出小于 `6.308883...` 的显式 bound。

因此任何企图在这个 funnel 中保持 slope

\[
>6.215109404735\ldots
\]

的无界 sequence都必须让 `q_5,g_5,n_5` 中至少一部分承担正线性 defect。

这正是下一轮应与 Schmidt / denominator prime-flow 联立的唯一剩余支。

---

## 8. 状态摘要

- **`已严格完成`**：`Fminus-defect-lower`、`Defect-stability`、general `Combined-height`、Tail-short LP dual certificate。
- **`显式 asymptotic bound`（sector only）**：Tail-short double-resonant funnel `limsup n/S <= 6.215109404735...`。
- **`待证`**：Defect-heavy funnel；将其与 Subspace / prime-flow 联立；新的全 DD explicit limsup；DD 全局空性。

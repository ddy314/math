# DD Tail-short 的 recovered-Schmidt upgrade 与 canonical sector `<=6`

> **依赖：** [`high-funnel-five-adic-dichotomy.md`](high-funnel-five-adic-dichotomy.md)、
> [`high-funnel-defect-optimization.md`](high-funnel-defect-optimization.md)、
> [`high-funnel-two-adic-balance.md`](high-funnel-two-adic-balance.md)、
> [`high-funnel-xi-depth.md`](high-funnel-xi-depth.md)、
> [`high-funnel-denominator-max-lock.md`](high-funnel-denominator-max-lock.md)、
> [`high-funnel-final5-sphere-c3-collapse.md`](high-funnel-final5-sphere-c3-collapse.md)。
>
> **严格状态：** `已严格完成（canonical t_2=1 double-resonant sector）`。
>
> `high-funnel-defect-optimization.md` 的旧 Tail-short bound
> \[
> 6.215109404735\ldots
> \]
> 使用的是早期 `Combined-height <=4S`。随后
> `high-funnel-two-adic-balance.md` 已对同一个 canonical S-unit funnel恢复更强的
> Schmidt defect budget，右端是 `3S`，并且 5-adic common-scale coefficient也从
> `g_5` 加强为 `4g_5`。
>
> 把新的 budget重新代回原 Tail-short LP，得到闭式 dual certificate：
> \[
> \boxed{
> \limsup_{\rm Tail\text{-}short}\frac nS
> \le
> \frac6{1+\log_{10}2}
> =4.611730721041\ldots.}
> \]
>
> 再与其它 canonical branches 合并：
>
> - `B_5>=m` defect-heavy：`<=6`；
> - `b_3` 非 5-adic maximum：`<=6`；
> - `Final-5`：`<=5.805865360520...`；
> - Tail-short：本文 `<=4.611730721041...`。
>
> 因而整个 canonical `t_2=1` double-resonant sector严格得到
> \[
> \boxed{
> \limsup\frac nS\le6.}
> \]
>
> 这仍是 sector theorem：最初把一般 DD candidate压进该 canonical S-unit funnel
> 的分类有自己的作用域。本文不把 `<=6` 无条件外推为全 DD numerical limsup。

---

## 1. 旧 Tail-short 的两条线性约束

记

\[
a:=\log_{10}2,
\qquad
b:=\log_{10}5=1-a.
\]

归一化：

\[
M=m/S,
\quad Q= q_5/S,
\quad G=g_5/S,
\quad N=n_5/S,
\]

并记目标 slope

\[
\mathcal N=\limsup n/S.
\]

`high-funnel-five-adic-dichotomy.md` 的 Tail-short branch满足

\[
3d\le m+4q_5+5g_5+2n_5.
\]

所以

\[
\boxed{
\mathcal N
\le
\frac43M+rac43Q+rac53G+rac23N.}
\tag{Tail-objective}

同一 branch由 strict inequality

\[
m>5q_5+4g_5+n_5
\]

在 limsup closure中给

\[
\boxed{-M+5Q+4G+N\le0.}
\tag{Tail-branch}

这些正是旧 `6.215109...` LP 使用的两条输入。

---

## 2. 用 recovered Schmidt budget替换旧 Combined-height

`high-funnel-two-adic-balance.md` 已对整个 canonical `t_2=1`
double-resonant S-unit funnel严格证明

\[
\begin{aligned}
&\frac{2(1+2a)}3m
+2a\mathfrak q+a\mathfrak n\\
&\qquad
+\frac b3(2q_5+4g_5+n_5)
+2\log_{10}\gamma_0
\le3S+o(S).
\end{aligned}
\tag{Subspace-defect}

所有省略项都非负，所以 normalized 后安全得到

\[
\boxed{
A M
+\frac{2b}{3}Q
+\frac{4b}{3}G
+\frac b3N
\le3,}
\tag{New-height}

其中

\[
\boxed{A:=\frac{2(1+2a)}3.}
\]

相比旧 Tail-short 文件使用的

\[
A M+\frac b3(2Q+G+N)\le4,
\]

`(New-height)` 同时更换了右端与 `G` coefficient，因此必须重新做 LP；
不能继续沿用 `6.215109...`。

---

## 3. 闭式 dual certificate

目标线性型：

\[
\mathcal L
:=\frac43M+rac43Q+rac53G+rac23N.
\]

取

\[
\boxed{
\lambda:=\frac2{1+a},
\qquad
\mu:=\frac{4a}{3(1+a)}.}
\tag{3.1}

二者均为正数。

把 `(New-height)` 乘 `lambda`，把 `(Tail-branch)` 乘 `mu` 后相加。

### M coefficient

\[
\lambda A-\mu
=\frac43.
\tag{3.2}

### N coefficient

\[
\lambda\frac b3+\mu
=\frac23.
\tag{3.3}

### Q coefficient

\[
\lambda\frac{2b}{3}+5\mu
=\frac43+\boxed{\frac{4a}{1+a}}
>\frac43.
\tag{3.4}

### G coefficient

\[
\lambda\frac{4b}{3}+4\mu
=\frac83
=\frac53+1
>\frac53.
\tag{3.5}

因为 `M,Q,G,N>=0`，组合左边逐项 dominate目标 `mathcal L`。右边只有
`(New-height)` 贡献：

\[
\mathcal L
\le3\lambda
=\boxed{\frac6{1+a}}.
\]

于是

\[
\boxed{
\limsup_{\rm Tail\text{-}short}\frac nS
\le
\frac6{1+\log_{10}2}.}
\tag{Tail-4611}

数值：

\[
\boxed{4.611730721041\ldots.}
\]

这个 dual certificate没有数值 LP 黑箱，也没有使用 sphere-c3 payer；它只是在
旧 Tail-short algebra上补上后来已经严格恢复的 stronger Schmidt budget。

---

## 4. extremal closure的形状（仅审计）

上述 dual中 Q/G coefficients有严格 slack；若有 sequence逼近
`6/(1+a)`，必须有

\[
Q\to0,
\qquad G\to0.
\]

M、N 两个系数恰好 tight，而 `(Tail-branch)` 与 `(New-height)` 也必须饱和，
所以

\[
N=M+o(1),
\]

\[
(A+b/3)M=3+o(1).
\]

但

\[
A+b/3=1+a,
\]

故

\[
\boxed{
M=N\to\frac3{1+a}.}
\tag{4.1}

这只记录 LP equality geometry，不声称该 ray真实存在。

---

## 5. canonical branch tree 合并为 `<=6`

现在回顾 exact 5-adic branch tree。

### 5.1 Tail-short

本文：

\[
\boxed{\limsup n/S\le4.611730721041\ldots.}
\]

### 5.2 Defect-heavy 且 `B_5>=m`

`high-funnel-xi-depth.md` 已证明

\[
\boxed{n<6S+O(1),}
\]

故 limsup `<=6`。

### 5.3 `b_3` 不是 5-adic maximum

`high-funnel-denominator-max-lock.md` 已证明

\[
\boxed{n<6S+O(1),}
\]

故 limsup `<=6`。

### 5.4 剩余 Final-5

`high-funnel-final5-sphere-c3-collapse.md` 已证明

\[
\boxed{
\limsup n/S
\le5.805865360520\ldots<6.}
\]

以上分支穷尽 canonical `t_2=1` double-resonant sector，所以：

\[
\boxed{
\limsup_{\rm canonical\ t_2=1\ double\text{-}resonant}
\frac nS\le6.}
\tag{Canonical-six}

---

## 6. 与旧 `6.215109...` 文件的关系

`high-funnel-defect-optimization.md` 的 algebra和 dual certificate在其使用的
`Combined-height` 输入下都是正确的，因此文件本身不是“错误证明”。

但在后来的 `Subspace-defect` 已经严格建立后，`6.215109...` 不再是当前最强
Tail-short bound，应降级为**历史中间 bound**。

当前 canonical branch tree应以本文的

\[
\boxed{\text{Tail-short }\le4.611730721041...}
\]

和

\[
\boxed{\text{whole canonical sector }\le6}
\]

为准。

---

## 7. 当前边界

这个 `<=6` 仍不能自动升级成全 DD `limsup<=6`，因为 `core.md` 中最初把
任意 candidate压入 canonical `t_2=1` double-resonant funnel的分类只在其规定的
高锥作用域中成立。旧全局 `6.308883...` proof后来还使用了全 DD tail collapse、
non-dominant `<=6` 与其它 dominant state分类。

下一步必须回到那一层 branch partition，逐个检查所有**未进入 canonical funnel**的
剩余 dominant states是否已经有 `<=6`，或把当前 stronger Schmidt/sphere payer迁移过去。
只有完成这一步才能严谨地宣称新的全 DD explicit `limsup<=6`。

---

## 8. 状态摘要

- **`已严格完成（Tail-short sector）`**：
  \[
  \limsup n/S\le6/(1+\log_{10}2)=4.611730721041... .
  \]
- **`已严格完成（canonical sector）`**：
  \[
  \limsup n/S\le6.
  \]
- **`失效/降级`**：`6.215109...` 作为当前 Tail-short frontier；它只保留为旧
  Combined-height 下的历史中间 bound。
- **`待证`**：把未进入 canonical funnel 的其它 DD dominant states统一审计到
  `<=6`，从而决定全 DD 是否可升级到 explicit `limsup<=6`。
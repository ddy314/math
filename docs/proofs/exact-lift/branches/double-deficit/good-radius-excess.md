# DD full-rational Good 的 canonical radius-excess

> **依赖：** [`frontier.md`](frontier.md) 中 continuation 的 `Radius-split`、`Secondary=Radius=Concat`、`Slot-RJ`、`Slot-JK`、`Nc1-elim`、`Good-cofactor-unit` 与 decimal remainder/carry 恒等式。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文只处理假想
> \[
> \frac{n_3}{S}\to 6.308883577618\ldots
> \]
> 的 full rational-contact Good 主质量。本文证明：此前末端看似分开的 **equal-depth radius cancellation** 与 **pure-radius cancellation**，在扣除 `gcd(C_L,H_R,N_c)` 的共同深度后其实是同一个 normalized unit-unit excess。由此得到一个 canonical 全局 excess 模数 `G_exc`，并证明 baseline 与 `H_J` 主槽逐素数分离。本文还记录一个 exact decimal no-go：把 `Top-residue` 与 `alpha` 直接相加消元只会精确退回 numerator reconstruction。
>
> 本文不证明 DD frontier emptiness，也不处理 genuine-Gaussian 主支。

---

## 1. main prime 的现有局部账本

沿用 `frontier.md` 的 full rational-contact Good 约定。删去 coefficient overlap、conjugate overlap、Bad mass 等总高度为 `o(S)` 的 exceptional core 后，固定一个 main prime-power

\[
p^h\Vert C_L,
\qquad p=\pi\bar\pi,
\]

并按对应 sign channel 选择

\[
\pi^h\Vert\Pi.
\]

记

\[
r_p:=v_p(H_R),
\qquad
n_p:=v_p(N_c),
\qquad
j_p:=v_p(H_J).
\tag{1.1}
\]

`frontier.md` 的 slot theorem 给出，在所选 channel 上

\[
\boxed{
\min(r_p,j_p)=0,
\qquad
\min(j_p,n_p)=0.
}
\tag{1.2}
\]

这里第二式使用了

\[
n_p=v_p(N_c)=\bar k
\]

与 `Slot-JK`；另一 sign channel 完全对称。

另一方面，`Radius-split` 给出

\[
\boxed{
a_p^{\rm raw}=\min(r_p,n_p)+\varepsilon_p,}
\tag{1.3}
\]

其中

\[
\varepsilon_p\ge0,
\qquad
\boxed{
\varepsilon_p>0\Longrightarrow r_p=n_p.}
\tag{1.4}
\]

而 `Secondary=Radius=Concat` 把同一 main depth 识别为真实拼接分子

\[
\alpha=A_{12}10^{n_3}+a_3
\]

中的深度。因此在 main `C_L` 可见范围内可写成

\[
\boxed{
\min\{h,v_p(\alpha)\}
=
\min\{h,a_p^{\rm raw}\}.
}
\tag{1.5}
\]

本文只使用 `(1.2)`--`(1.5)`，不重新构造任何 Gaussian quotient。

---

## 2. canonical baseline / excess 分解

定义截断的 radius depth

\[
\boxed{
a_p:=\min\{h,v_p(\alpha)\},}
\tag{2.1}
\]

共同 cofactor baseline

\[
\boxed{
b_p:=\min\{h,r_p,n_p\},}
\tag{2.2}
\]

以及 excess depth

\[
\boxed{
x_p:=a_p-b_p.}
\tag{2.3}
\]

由 `(1.3)`--`(1.5)`，

\[
a_p
=
\min\{h,\min(r_p,n_p)+\varepsilon_p\}
\ge
\min\{h,r_p,n_p\}
=b_p.
\]

故

\[
\boxed{x_p\ge0.}
\tag{2.4}
\]

于是每个 main prime 的 radius depth 被 canonical 地分成

\[
\boxed{
\text{radius depth}
=
\text{common }(H_R,N_c)\text{ baseline}
+
\text{excess}.
}
\tag{2.5}
\]

这里没有人为选择 payer；`b_p` 由三个整数 `C_L,H_R,N_c` 的 gcd 唯一确定。

---

## 3. 核心引理：任何正 excess 在正规化后都是 pure-radius

### 命题 3.1

若

\[
\boxed{x_p>0,}
\tag{3.1}
\]

则必有

\[
\boxed{
r_p=n_p=b_p<h.}
\tag{3.2}
\]

因此除去共同因子 `p^{b_p}` 后，`H_R` 与 `N_c` 两个 cofactor 都成为 `p`-unit；剩余的 main radius depth只能来自 `Nc1-elim` 两个 unit 项之间的 cancellation。

### 证明

若

\[
r_p\ne n_p,
\]

则由 `(1.4)` 的逆否命题

\[
\varepsilon_p=0.
\]

于是

\[
a_p
=
\min\{h,\min(r_p,n_p)\}
=b_p,
\]

与 `x_p>0` 矛盾。因此

\[
r_p=n_p=:t.
\tag{3.3}
\]

若

\[
t\ge h,
\]

则

\[
b_p=h
\]

且由 `a_p\le h` 再次得到 `x_p=0`，矛盾。故

\[
t<h.
\]

于是

\[
b_p=t=r_p=n_p<h,
\]

即得 `(3.2)`。

现在使用

\[
\widetilde r^{\,2}5^{4T-2m}N_c
-g_0^2a_2^22^{2m-4}H_R
=
\frac{C_L}{E}N(\Delta_1).
\tag{Nc1-elim}
\]

在 main coefficient-unit regime 中，两项显式 coefficient 与 `C_L/E` 的相关 overlap 已删入 exceptional core。由 `(3.2)` 可从左侧两项共同提出恰好 `p^{b_p}`；提出后两个剩余项都是 `p`-units。其后仍存在的 `p`-depth就是 unit-unit cancellation depth，而 main `C_L` 能看到的剩余部分恰为 `x_p`。

故 `(3.1)` 下没有第二种 normalized mechanism。证毕。

---

## 4. equal-depth 与 pure-radius 的假分叉消失

旧 slot ledger 将最后的困难写成两类：

1. `r_p=n_p>0` 后继续发生 equal-depth cancellation；
2. `r_p=n_p=0` 时发生 pure-radius cancellation。

命题 3.1 表明，这一区分只发生在**扣除 common baseline 之前**。

若第一类产生真正的 main excess，则

\[
r_p=n_p=b_p<h.
\]

除以 `p^{b_p}` 后立刻变为

\[
v_p(H_R/p^{b_p})
=
v_p(N_c/p^{b_p})
=0,
\]

而 excess 仍由两个 units 的差产生。

第二类只是 `b_p=0` 的同一情况。

因此得到：

\[
\boxed{
\text{equal-depth excess}
\quad\text{与}\quad
\text{pure-radius}
\quad\text{在 canonical baseline normalization 后是同一 local slot。}
}
\tag{Pure-excess-local}
\]

这将 `frontier.md` 末端的

\[
\text{equal-depth }(H_R,N_c)\text{ cancellation}
\;\cup\;
\text{pure numerator-shell contact}
\]

压成一个单一对象：**normalized pure excess**。

---

## 5. 全局 canonical excess 模数

令 `C_L^{\rm main}` 表示删去上述 `o(S)` exceptional prime-power 后的 main divisor：

\[
C_L^{\rm main}
:=
\prod_{p^h\Vert C_L,\ p\in\mathcal P_{\rm main}}p^h,
\qquad
\log\frac{C_L}{C_L^{\rm main}}=o(S).
\tag{5.1}
\]

定义真实 radius modulus

\[
\boxed{
G_{\rm rad}
:=
\gcd(C_L^{\rm main},\alpha),}
\tag{5.2}
\]

共同 baseline

\[
\boxed{
G_{\rm base}
:=
\gcd(C_L^{\rm main},H_R,N_c),}
\tag{5.3}
\]

以及 quotient

\[
\boxed{
G_{\rm exc}
:=
\frac{G_{\rm rad}}{G_{\rm base}}.
}
\tag{5.4}
\]

由第 2 节逐素数有 `b_p<=a_p`，故 `(5.4)` 确为正整数，而且

\[
\boxed{
G_{\rm rad}=G_{\rm base}G_{\rm exc}.}
\tag{5.5}
\]

更精确地，

\[
v_p(G_{\rm base})=b_p,
\qquad
v_p(G_{\rm exc})=x_p.
\tag{5.6}
\]

因此命题 3.1 立即全局化为

\[
\boxed{
\gcd\!\left(
G_{\rm exc},
\frac{H_R}{G_{\rm base}}
\right)=1,
\qquad
\gcd\!\left(
G_{\rm exc},
\frac{N_c}{G_{\rm base}}
\right)=1.
}
\tag{Pure-excess-global}
\]

同时

\[
\boxed{
G_{\rm exc}
\mid
\frac{\alpha}{G_{\rm base}}.
}
\tag{5.7}
\]

所以 `G_exc` 是一个完全由已有 terminal integers 定义的 **primitive digit-shell modulus**：它整除真实拼接 numerator，但已经与 normalized `H_R`、`N_c` 两个旧 payer 都互素。

这正是后续 strict digit-shell lemma 应当作用的对象。

---

## 6. baseline 与 `next-J` 主槽严格分离

由 `(1.2)`：如果

\[
b_p>0,
\]

则

\[
r_p>0,
\qquad n_p>0.
\]

于是 `Slot-RJ` 与 `Slot-JK` 都强迫

\[
j_p=0.
\]

因此

\[
\boxed{
\gcd(G_{\rm base},H_J)=1
}
\tag{Baseline-J-separation}
\]

在 `C_L^{\rm main}` 上逐素数严格成立。

把 exceptional core 放回去时，这可写为高度形式

\[
\boxed{
\log\gcd(G_{\rm base}^{\rm full},H_J)=o(S),
}
\tag{6.1}
\]

其中 `G_base^{full}` 表示未预先删 exceptional prime-power 的对应 gcd。

这说明 common `(H_R,N_c)` payer 与 `next-J` payer 不能支付同一份 main prime mass。

---

## 7. `Good-cofactor-unit` 在两个基础 slot 上是自动的

Good 已被翻译成

\[
\boxed{
p\nmid d^2N_c+R_0^2H_J}
\tag{7.1}
\]

对每个 main prime 成立。

在 coefficient-unit convention 下：

- 若 `p|G_base`，则 `p|N_c` 且第 6 节给 `p\nmid H_J`，所以 `(7.1)` 模 `p` 退化为非零的 `R_0^2H_J`；
- 若 `j_p>0`，则 `(1.2)` 给 `n_p=0`，所以 `(7.1)` 模 `p` 退化为非零的 `d^2N_c`。

因此 `Good-cofactor-unit` 对这两个 mutually-exclusive 基础槽本身不提供新的正线性 height 收费。

这解释了为什么仅把 `NcU-elim` 再与 slot capacity 相加仍会达到临界：真正可能携带新信息的是已经除掉 baseline 后的 `G_exc`，而不是 `(7.1)` 本身。

> **状态：**这一节是 no-go / allocation 审计，不是 closure。

---

## 8. `Top-residue + alpha` 的直接消元精确退回 numerator reconstruction

这一节记录另一个容易重复尝试的方向。

定义

\[
\Sigma:=2^HZ+5^TU,
\qquad
V:=2^HZ-5^TU,
\]

以及

\[
R_{\rm dec}
:=B10^dVA_{12}-Ua_3.
\tag{8.1}
\]

已有

\[
\boxed{
R_{\rm dec}=\frac{\Sigma R_0}{g_0},
}
\tag{8.2}
\]

和

\[
\boxed{
g_0\alpha=\Sigma A_0.}
\tag{8.3}
\]

又因为

\[
n_3=m+d,
\qquad
\alpha=A_{12}10^{m+d}+a_3,
\]

以及 terminal phase

\[
10^m=2B5^T,
\]

直接计算：

\[
\begin{aligned}
R_{\rm dec}+U\alpha
&=B10^dVA_{12}-Ua_3
+U(A_{12}10^{m+d}+a_3)\\
&=B10^dA_{12}
\left(V+\frac{U10^m}{B}\right)\\
&=B10^dA_{12}(V+2\cdot5^TU)\\
&=\boxed{B10^dA_{12}\Sigma}.
\end{aligned}
\tag{8.4}
\]

将 `(8.2)`、`(8.3)` 代入 `(8.4)`：

\[
\frac{\Sigma}{g_0}(R_0+UA_0)
=B10^dA_{12}\Sigma.
\]

因为 `Sigma>0`，约去后恰得

\[
\boxed{
UA_0+R_0=g_0B10^dA_{12},
}
\tag{8.5}
\]

即已有 numerator reconstruction。

因此：

\[
\boxed{
\text{把 }Top\text{-residue 与 }\alpha\text{-repeat 通过 }R_{\rm dec}+U\alpha
\text{ 直接联立，不产生独立 congruence。}
}
\tag{Decimal-alpha-no-go}
\]

`Top-residue` 本身仍然是严格的 thin decimal window；这里只排除最直接的线性消元方式。若后续利用该 window，必须引入一个不由 `(8.2)`--`(8.5)` 重构的 primitive residue / size input。

---

## 9. 更新后的 Good radius frontier

本文把 Good 的 radius 侧整理成以下 canonical 图：

\[
\boxed{
G_{\rm rad}
=
G_{\rm base}G_{\rm exc},
}
\]

其中

\[
G_{\rm base}
=
\gcd(C_L^{\rm main},H_R,N_c)
\]

是已经由两个 cofactor payer 共同承担的 baseline，并与 `H_J` main slot 分离；真正未支付的 radius 信息全部进入

\[
\boxed{
G_{\rm exc}
=\frac{\gcd(C_L^{\rm main},\alpha)}
{\gcd(C_L^{\rm main},H_R,N_c)}.
}
\tag{9.1}
\]

对每个

\[
p\mid G_{\rm exc},
\]

在除去 `G_base` 后都有

\[
H_R/G_{\rm base},
\qquad
N_c/G_{\rm base}
\]

为 `p`-units；所以旧的 equal-depth excess 与 pure-radius 已经统一成一个 pure unit-unit cancellation。

因此 Good radius 的下一条合理目标可固定为：

> **Primitive excess digit-shell lemma（待证）**：证明在 full rational-contact Good frontier 上
> \[
> \log G_{\rm exc}=o(S),
> \]
> 或给出一个严格更强的界，使 `G_exc` 无法承载任何所需的正线性 main mass。

这个目标应直接使用 `G_exc | alpha/G_base` 的真实十进制位置，同时保持

\[
\gcd\!\left(G_{\rm exc},H_R/G_{\rm base}\right)
=
\gcd\!\left(G_{\rm exc},N_c/G_{\rm base}\right)=1.
\]

继续区分 “equal-depth excess” 与 “pure-radius” 已没有数学收益；继续把 `Top-residue` 与 `alpha` 做 `(8.4)` 型一阶消元也只会回到旧 reconstruction。

---

## 10. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：main radius depth 的 canonical `baseline + excess` 分解；`x_p>0 => r_p=n_p=b_p<h`；equal-depth excess 在 baseline normalization 后等价于 pure-radius；全局 `G_rad=G_base G_exc`；`G_exc` 与 normalized `H_R,N_c` 互素；`G_base` 与 `H_J` main slot 分离；`Decimal-alpha-no-go` exact identity。
- **`失效/降级`**：试图仅靠 `Good-cofactor-unit` 对 baseline / next-J 槽再次收费；通过 `R_dec+U alpha` 直接把 `Top-residue` 与 radius repeat 做线性消元。
- **`待证`**：primitive excess digit-shell lemma；full rational Good 的最终 emptiness；genuine-Gaussian split-prime / digit-shell closure；DD 全局空性与有效绝对高度界。

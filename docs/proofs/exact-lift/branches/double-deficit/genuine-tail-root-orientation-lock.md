# DD genuine-Gaussian 的 tail-root 线性化与全局 orientation lock

> **依赖：** [`global-framework.md`](../../global-framework.md) 的统一判别平方与 primitive tail quadratic、[`genuine-full-concat-hensel.md`](genuine-full-concat-hensel.md) 的 first-layer Hensel、以及 frontier pair-max square-depth
> \[
> \Pi_{\rm sph}^2\mid y_2+i y_3.
> \]
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文首先把 primitive tail quadratic 的判别式完全化成统一 discriminant root `W`，得到一个此前未显式使用的全局线性恒等式
> \[
> \mathscr T a_3
> =\kappa G^2C_{\rm DD}+\eta(\kappa+G)W,
> \qquad \eta\in\{\pm1\},
> \]
> 其中
> \[
> \mathscr T=\frac{\kappa^2(\kappa+2G)}{10^{m_3}}\in\mathbf Z.
> \]
> 然后把它与 genuine first-layer Hensel 联立，证明 `same/opp` relative Gaussian orientation 在 main core 上不能逐 prime 自由选择：全局 tail-root sign `eta` 唯一决定 surviving orientation；另一 orientation 的 main mass 为零（恢复 exceptional core 后只有 `10^{o(S)}`）。
>
> 本文不关闭 genuine-Gaussian branch；它消除的是 relative-orientation entropy。

---

## 1. primitive tail quadratic 与记号

统一框架中 DD 的 coefficient pair 写为

\[
(C,D)=(C_{\rm DD},Q),
\]

其中

\[
C_{\rm DD}=10^{d_3}A_{12}.
\]

令

\[
10^{m_3}=\delta_3L,
\qquad
b_3=\delta_3\tau,
\qquad
z_3=\frac{a_3}{\delta_3}.
\]

这里 `z_3` 只作为 rational root 使用，不要求 `delta_3|a_3`。

primitive tail quadratic 为

\[
-\kappa(\kappa+2G)z_3^2
+2G^2LC_{\rm DD}z_3
+\mathcal C_3
=0,
\tag{1.1}
\]

其中

\[
\mathcal C_3
=G^2L^2C_{\rm DD}^2
-\mathcal N_{12}(LQ+\tau)^2.
\tag{1.2}
\]

同时 tail-weight identity 为

\[
\boxed{\kappa\tau=LQG.}
\tag{Tail-weight}
\]

统一 discriminant square 为

\[
\boxed{
W^2
=\kappa^2G^2C_{\rm DD}^2
-\kappa Q^2\mathcal N_{12}(\kappa+2G).
}
\tag{Disc-W}
\]

---

## 2. tail quadratic 的判别式正好由 `W` 给出

把 `(1.1)` 视为关于 `z_3` 的二次式。其判别式为

\[
\begin{aligned}
\Delta_z
&=4G^4L^2C_{\rm DD}^2
+4\kappa(\kappa+2G)\mathcal C_3\\
&=4\Bigl[
G^2L^2C_{\rm DD}^2(\kappa+G)^2
-\kappa(\kappa+2G)\mathcal N_{12}(LQ+\tau)^2
\Bigr].
\end{aligned}
\tag{2.1}

由 `(Tail-weight)`：

\[
LQ+\tau
=LQ\frac{\kappa+G}{\kappa}.
\tag{2.2}
\]

代入 (2.1)：

\[
\begin{aligned}
\Delta_z
&=
\frac{4L^2(\kappa+G)^2}{\kappa^2}
\Bigl[
\kappa^2G^2C_{\rm DD}^2
-\kappa Q^2\mathcal N_{12}(\kappa+2G)
\Bigr]\\
&=
\boxed{
\left(
\frac{2L(\kappa+G)}{\kappa}W
\right)^2}.
\end{aligned}
\tag{Tail-discriminant}
\]

因此 actual rational root `z_3` 必满足某个全局固定符号

\[
\boxed{\eta\in\{\pm1\}}
\]

使

\[
\boxed{
\kappa^2(\kappa+2G)z_3
=L\Bigl[
\kappa G^2C_{\rm DD}
+\eta(\kappa+G)W
\Bigr].
}
\tag{Tail-root-linear}
\]

这个 `eta` 是由 actual tail root 一次性决定的全局符号，不随 prime 改变。

---

## 3. 消去 `delta_3`：得到 original-integer 线性恒等式

统一 denominator-tail certificate 已证明

\[
10^{m_3}\mid\kappa^2(\kappa+2G).
\]

定义

\[
\boxed{
\mathscr T
:=\frac{\kappa^2(\kappa+2G)}{10^{m_3}}
\in\mathbf Z_{>0}.
}
\tag{3.1}

由

\[
z_3=\frac{a_3}{\delta_3},
\qquad
10^{m_3}=\delta_3L,
\]

把 `(Tail-root-linear)` 乘 `delta_3`，得到完全 original-integer 的恒等式

\[
\boxed{
\mathscr T a_3
=\kappa G^2C_{\rm DD}
+\eta(\kappa+G)W.
}
\tag{Tail-root-original}

这条式子是后面 orientation lock 的核心。

---

## 4. pair-max main prime 上自动得到 square-depth tail-root congruence

固定 one-channel pair-max main prime-power

\[
p^h\Vert C_L^{\rm main}.
\]

删除 coefficient exceptional core 后：

\[
p\ne2,5,
\qquad
p^h\Vert b_2,
\qquad
p^h\Vert b_3,
\qquad
p\nmid b_1Qa_2a_3.
\tag{4.1}

又有

\[
G=b_1b_2,
\]

故

\[
p^h\Vert G.
\tag{4.2}

由

\[
\kappa b_3=10^{m_3}QG
\tag{4.3}
\]

把 `p^h` 从 `b_3,G` 两边同时约掉，可见

\[
\boxed{p\nmid\kappa.}
\tag{4.4}

于是

\[
p\nmid\kappa+G.
\]

`(Tail-root-original)` 中

\[
p^{2h}\mid G^2,
\]

所以得到

\[
\boxed{
p^{2h}
\mid
\mathscr T a_3
-\eta(\kappa+G)W.
}
\tag{Tail-root-p2h}

聚合 main pair-max core，可写成

\[
\boxed{
(C_L^{\rm main})^2
\mid
\mathscr T a_3
-\eta(\kappa+G)W
}
\tag{Tail-root-core}

按删除 `10^{o(S)}` exceptional core 后理解。

---

## 5. 与 genuine first-layer Hensel 联立

沿用

\[
A_c=Qa_2^2b_1^2,
\]

并对

\[
\sigma\in\{\mathrm{same},\mathrm{opp}\}
\]

定义

\[
\epsilon_{\rm same}=-1,
\qquad
\epsilon_{\rm opp}=+1.
\tag{5.1}

`genuine-full-concat-hensel.md` 已证明，对

\[
p^h\Vert C_\sigma
\]

有 first-layer congruence

\[
\boxed{
Q^2a_2^2b_1^2 10^{m_3}
+\epsilon_\sigma Wa_3
\equiv0
\pmod{p^h}.
}
\tag{H1}

记

\[
y:=a_2b_1.
\]

将 `(H1)` 乘以 `eta(kappa+G)`，再用 `(Tail-root-p2h)` 的模 `p^h` 版本消掉 `W`，然后乘 `eta 10^{m_3}`，得到

\[
(\kappa+G)Q^2y^2 10^{2m_3}
+\epsilon_\sigma\eta\,
\kappa^2(\kappa+2G)a_3^2
\equiv0
\pmod{p^h}.
\tag{5.2}

写

\[
b_2=p^h b_{2,p},
\qquad
b_3=p^h b_{3,p},
\qquad
G=p^hG_p,
\]

其中

\[
G_p=b_1b_{2,p}.
\tag{5.3}

由 `(4.3)`：

\[
\boxed{
\kappa b_{3,p}
=10^{m_3}QG_p.
}
\tag{5.4}

把 `(5.4)` 代入 `(5.2)`，乘 p-unit `G_p^2` 并约去 `kappa^2`，再用

\[
\kappa+G\equiv\kappa+2G\equiv\kappa
\pmod{p^h},
\]

得到

\[
y^2b_{3,p}^2
+\epsilon_\sigma\eta\,G_p^2a_3^2
\equiv0
\pmod{p^h}.
\]

由 `y=a_2b_1`、`G_p=b_1b_{2,p}` 且 `p\nmid b_1`：

\[
\boxed{
a_2^2b_{3,p}^2
+\epsilon_\sigma\eta\,
a_3^2b_{2,p}^2
\equiv0
\pmod{p^h}.
}
\tag{Normalized-contact}

这是 tail-root 与 discriminant first lift 联立后的 normalized last-two-fractions contact。

---

## 6. sphere square-depth 已经给 normalized elliptic sum 深度 `2h`

pair-max sphere orientation 给

\[
\Pi_{\rm sph}^2\mid y_2+i y_3.
\]

在当前 rational prime `p^h` 上，因此

\[
\boxed{p^{2h}\mid y_2^2+y_3^2.}
\tag{6.1}

又因为

\[
q=p^hq_p,
\qquad
b_2=p^hb_{2,p},
\qquad
b_3=p^hb_{3,p},
\]

且 `q_p,b_{2,p},b_{3,p}` 都是 p-units，

\[
y_2=a_2\frac{q_p}{b_{2,p}},
\qquad
y_3=a_3\frac{q_p}{b_{3,p}}.
\]

乘以 p-unit

\[
\left(\frac{b_{2,p}b_{3,p}}{q_p}\right)^2
\]

不会改变 p-adic valuation，因此

\[
\boxed{
p^{2h}
\mid
a_2^2b_{3,p}^2+a_3^2b_{2,p}^2.
}
\tag{Sphere-normalized}

---

## 7. hyperbolic relative sign 不可能出现

若

\[
\epsilon_\sigma\eta=-1,
\]

则 `(Normalized-contact)` 给

\[
p^h
\mid
a_2^2b_{3,p}^2-a_3^2b_{2,p}^2.
\tag{7.1}

而 `(Sphere-normalized)` 甚至给更强的

\[
p^{2h}
\mid
a_2^2b_{3,p}^2+a_3^2b_{2,p}^2.
\tag{7.2}

特别地两式都模 `p^h` 为零。相加得到

\[
p^h\mid2a_2^2b_{3,p}^2.
\]

但

\[
p\nmid2a_2b_{3,p}
\]

由 main reducedness / unit ledger 保证，矛盾。

因此每个 genuine main prime都必须满足

\[
\boxed{
\epsilon_\sigma\eta=+1.
}
\tag{Orientation-lock-local}

---

## 8. 全局 orientation lock

`eta` 是 actual tail root 决定的一个**全局固定 sign**，而

\[
\epsilon_{\rm same}=-1,
\qquad
\epsilon_{\rm opp}=+1.
\]

所以 `(Orientation-lock-local)` 立刻给出：

- 若
  \[
  \eta=+1,
  \]
  则 genuine main primes 只能进入 `opp`；
- 若
  \[
  \eta=-1,
  \]
  则 genuine main primes 只能进入 `same`。

因此 relative Gaussian orientation 不再有逐 prime 的二元自由度。记 surviving class 为

\[
C_{\rm ell},
\]

wrong-sign class 为

\[
C_{\rm hyp}.
\]

则在 main core 上严格有

\[
\boxed{C_{\rm hyp}=1,}
\tag{8.1}

而恢复此前删除的 exceptional core 后：

\[
\boxed{
\log C_{\rm hyp}=o(S),
\qquad
C_{\rm ell}=C_G\cdot10^{o(S)}
}
\tag{Genuine-orientation-lock}

按 logarithmic main-height 理解。

这是真正的 entropy reduction：genuine branch 的 discriminant orientation 由一个 global tail-root sign 唯一决定。

---

## 9. 方法边界

surviving sign 满足

\[
\epsilon_\sigma\eta=+1,
\]

所以 `(Normalized-contact)` 退化成

\[
a_2^2b_{3,p}^2+a_3^2b_{2,p}^2
\equiv0\pmod{p^h},
\]

而 sphere carrier 已经给同一 quantity 更深的 `p^{2h}` divisibility。因此 surviving first-layer normalized contact本身不能作为第二份独立 height。

换言之：

\[
\boxed{
\text{tail-root linearization 的新作用是锁 orientation，}
\text{不是在 surviving elliptic class 上再次收费。}
}
\tag{No-double-pay}

下一步必须审计 second-layer `p^{2h}` full-concat cancellation 在 orientation lock 后是否也完全由 sphere square-depth支付。

---

## 10. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`Tail-discriminant`、`Tail-root-linear`、`Tail-root-original`、pair-max `Tail-root-p2h`、`Normalized-contact`、hyperbolic sign contradiction、global `Genuine-orientation-lock`。
- **`失效/降级`**：把 surviving elliptic first-layer contact当作 sphere carrier之外的新 obstruction。
- **`待证`**：orientation lock 后 second-layer square-depth是否完全 sphere-paid；genuine split-prime / digit-shell closure；DD 全局空性。

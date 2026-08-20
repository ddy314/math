# double-deficit High Funnel Ledger

> 本文件是细粒度研究记录的机械归并账本。各来源的标题、正文和证明状态原样保留；账本中的局部闭合、有限证书或降级路线均不表示该分支或主不存在性命题已经关闭。

## 来源索引

- [`high-funnel-625-rigidity.md`](#source-high-funnel-625-rigidity)
- [`high-funnel-defect-optimization.md`](#source-high-funnel-defect-optimization)
- [`high-funnel-denominator-max-lock.md`](#source-high-funnel-denominator-max-lock)
- [`high-funnel-exact-small-factor-normalization.md`](#source-high-funnel-exact-small-factor-normalization)
- [`high-funnel-final-five-collapse.md`](#source-high-funnel-final-five-collapse)
- [`high-funnel-final5-sphere-c3-collapse.md`](#source-high-funnel-final5-sphere-c3-collapse)
- [`high-funnel-final5-two-adic-optimization.md`](#source-high-funnel-final5-two-adic-optimization)
- [`high-funnel-five-adic-dichotomy.md`](#source-high-funnel-five-adic-dichotomy)
- [`high-funnel-fminus-sunit-factorization.md`](#source-high-funnel-fminus-sunit-factorization)
- [`high-funnel-gap-depth.md`](#source-high-funnel-gap-depth)
- [`high-funnel-gap-epsilon-allocation.md`](#source-high-funnel-gap-epsilon-allocation)
- [`high-funnel-gap-square-core.md`](#source-high-funnel-gap-square-core)
- [`high-funnel-qz-bottom-orientation-correction.md`](#source-high-funnel-qz-bottom-orientation-correction)
- [`high-funnel-qz-gcd-allocation.md`](#source-high-funnel-qz-gcd-allocation)
- [`high-funnel-qz-projective-allocation.md`](#source-high-funnel-qz-projective-allocation)
- [`high-funnel-qz-sheet-reader-collapse.md`](#source-high-funnel-qz-sheet-reader-collapse)
- [`high-funnel-qz-two-sheet-split.md`](#source-high-funnel-qz-two-sheet-split)
- [`high-funnel-recovery-squarefree-lock.md`](#source-high-funnel-recovery-squarefree-lock)
- [`high-funnel-square-identities-audit.md`](#source-high-funnel-square-identities-audit)
- [`high-funnel-tail-short-schmidt-upgrade.md`](#source-high-funnel-tail-short-schmidt-upgrade)
- [`high-funnel-two-adic-balance.md`](#source-high-funnel-two-adic-balance)
- [`high-funnel-two-balanced-collapse.md`](#source-high-funnel-two-balanced-collapse)
- [`high-funnel-xi-depth.md`](#source-high-funnel-xi-depth)

<a id="source-high-funnel-625-rigidity"></a>

> 整合来源：`high-funnel-625-rigidity.md`

# DD `Final-5` 的 `25/4` equality-ray rigidity

> **依赖：** [`high-funnel-final5-two-adic-optimization.md`](high-funnel-ledger.md#source-high-funnel-final5-two-adic-optimization)、
> [`high-funnel-fminus-sunit-factorization.md`](high-funnel-ledger.md#source-high-funnel-fminus-sunit-factorization)、
> `core.md` 的 digit/surplus upper、S-unit pinning、overlap parameterization。
>
> **严格状态：** `已严格完成（conditional equality-ray structure）`。
>
> 本文不证明存在 slope `25/4` 的 DD sequence。相反，假设 canonical
> `Final-5 / 2-balanced` sector 中存在无界 sequence满足
> \[
> \frac nS\to\frac{25}{4},
> \]
> 则上一文件证明中的每个非负 defect都必须趋零，系统被锁到唯一比例模型。
>
> 主要结论：令 `a=log10 2`，则
> \[
> \boxed{
> \frac mS\to\frac3{1+a},
> \qquad
> \frac TS\to\frac{3}{2(1+a)},
> \qquad
> \frac{\log_{10}\gamma}{S}\to\frac34,}
> \]
> \[
> \boxed{
> \frac{\log_{10}U}{S}\to\frac{11a-1}{4(1+a)},
> \quad
> \frac{\log_{10}Z}{S}
> =\frac{\log_{10}q}{S}
> \to\frac{5-7a}{4(1+a)},
> \quad
> \frac{\log_{10}V}{S}\to\frac14.}
> \]
> 并且 prefix digit orientation唯一为
> \[
> \boxed{
> (m_1,m_2;n_1,n_2)
> =(S,o(S);o(S),S)+o(S).}
> \]
> 此外 sphere-gap quotient满足 `log a_gap=o(S)`；因此 `25/4` 若可实现，
> 也只能沿一个新的 terminal ray，而不是一片正维 defect region。

---

## 1. equality迫使所有 defect terms消失

沿用上一文件 normalized variables

\[
M,Q_5,G_5,N_5,Q_2,G_2,N_2,R.
\]

`2-balanced` bound为

\[
\begin{aligned}
\mathcal N
\le{}&
\frac{11}{2}+\frac{1+a}{4}M
-\frac{3a}{2}Q_2-\frac a2N_2\\
&-\frac{3b}{2}Q_5-\frac{3b}{4}N_5,
\end{aligned}
\tag{1.1}

其中 `b=1-a`，而

\[
(1+a)M+2aQ_2+aN_2+2R\le3.
\tag{1.2}

假设

\[
\mathcal N\to25/4.
\]

因为 `(1.1)` 的最终 `25/4` 来自

\[
M\le\frac3{1+a}
\]

并且所有显示的 defect coefficients都严格为负，所以必须有

\[
\boxed{
M\to M_*:=\frac3{1+a},}
\tag{1.3}

\[
\boxed{
Q_2,N_2,Q_5,N_5,R\to0.}
\tag{1.4}

这里箭头表示 normalized quantities 沿该 sequence趋于相应极限。

`Final-5` 有

\[
M=2Q_5+4G_5+N_5,
\]

所以

\[
\boxed{
G_5\to\frac{M_*}{4}
=\frac{3}{4(1+a)}.}
\tag{1.5}

又

\[
T/S=M-2G_5,
\]

故

\[
\boxed{
\frac TS\to\frac{M_*}{2}
=\frac{3}{2(1+a)}.}
\tag{1.6}

`2-balanced` 给

\[
2G_2=M+Q_2+o(1),
\]

于是

\[
\boxed{
G_2\to\frac{M_*}{2}
=\frac{3}{2(1+a)}.}
\tag{1.7}

---

## 2. `gamma` 的高度恰为 `3/4 S`

写

\[
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0,
\qquad
R=\frac{\log_{10}\gamma_0}{S}\to0.
\]

所以

\[
\frac{\log_{10}\gamma}{S}
\to aG_2+bG_5.
\]

代入 `(1.5)`、`(1.7)`：

\[
\begin{aligned}
aG_2+bG_5
&=\frac{M_*}{4}(2a+b)\\
&=\frac{M_*}{4}(1+a)\\
&=\boxed{\frac34}.
\end{aligned}
\tag{Gamma-3/4}

因此 denominator gcd-normal form

\[
G=\gamma V
\]

中 `gamma` 承担恰 `3S/4` 的 decimal height。

---

## 3. S-unit heights全部唯一确定

2-resonance给 S-unit exponent

\[
\frac HS
=2M+2Q_2+N_2-2G_2+o(1).
\]

由 `(1.3)`、`(1.4)`、`(1.7)`：

\[
\boxed{
\frac HS\to M_*=rac3{1+a}.}
\tag{3.1}

又

\[
\kappa=2\gamma5^TU
\]

与 decimal pinning `log10 kappa=2S+O(1)` 给

\[
\frac{\log_{10}U}{S}
\to
2-\frac34-b\frac{M_*}{2}.
\]

化简：

\[
\boxed{
U_*:=\lim\frac{\log_{10}U}{S}
=\frac{11a-1}{4(1+a)}
=0.444134639479\ldots.}
\tag{U-height}

同理

\[
\kappa+2G=2\gamma2^HZ,
\]

其 decimal height同样为 `2S+O(1)`，故

\[
\boxed{
Z_*:=\lim\frac{\log_{10}Z}{S}
=2-\frac34-aM_*
=\frac{5-7a}{4(1+a)}
=0.555865360521\ldots.}
\tag{Z-height}

而

\[
U_*+Z_*=1,
\]

所以 Schmidt lower bound也必须恰好在边界上饱和。

由于 `Q=Uq` 且 `Q` 是 S-digit denominator concat：

\[
\boxed{
\frac{\log_{10}q}{S}
\to1-U_*=Z_*.}
\tag{q-height}

另外 `G=b_1b_2` 的 decimal height为 `S+O(1)`，所以

\[
\boxed{
\frac{\log_{10}V}{S}
=1-\frac34+o(1)
\to\frac14.}
\tag{V-height}

最终

\[
\boxed{
\log_{10}(5^TU)
=\log_{10}(2^HZ)
=\frac54S+o(S).}
\tag{XY-height}

---

## 4. third-block 与 denominator smooth depths

`Final-5` 给

\[
B_5=q_5+2g_5,
\]

所以

\[
\boxed{
\frac{B_5}{S}	o\frac{M_*}{2}.}
\tag{4.1}

二进 `t_2=1` denominator lock为

\[
\mathfrak B=m+\mathfrak q-1,
\]

所以

\[
\boxed{
\frac{\mathfrak B}{S}	o M_*.}
\tag{4.2}

而 prefix product `G=b_1b_2` 的 2/5-depth分别为

\[
\boxed{
\frac{v_2(G)}S\to\frac{M_*}{2},
\qquad
\frac{v_5(G)}S\to\frac{M_*}{4}.}
\tag{4.3}

因此在 leading order上，`b_3` 的两种 decimal-prime depth都正好是
prefix product对应 depth的两倍：

\[
\frac{v_2(b_3)}S
\to2\frac{v_2(G)}S,
\qquad
\frac{v_5(b_3)}S
\to2\frac{v_5(G)}S.
\tag{4.4}

---

## 5. equality强迫 prefix digit polarization

`Z-defect-stability` 仍使用了旧 exact upper

\[
F_-<2\cdot10^{2S+s+D_s+2m-n+O(1)}
\]

以及

\[
s+D_s\le2S.
\]

若 `n/S->25/4` 达到本文上界，则该 coarse digit inequality不能损失正线性高度；
因此

\[
\boxed{\frac{s+D_s}{S}\to2.}
\tag{5.1}

但

\[
s=s_1+s_2\le2=O(1),
\]

而

\[
s+D_s=2\max(s_1,s_2).
\]

所以除交换 `1,2` 外：

\[
\frac{s_1}{S}\to1,
\qquad
\frac{s_2}{S}\to-1.
\]

由

\[
m_1+m_2=S,
\qquad
n_i=m_i+s_i>0,
\]

只能有两种 asymptotic orientations：

\[
(m_1,m_2;n_1,n_2)
=(o(S),S;S,o(S))+o(S)
\tag{5.2A}
\]

或

\[
(m_1,m_2;n_1,n_2)
=(S,o(S);o(S),S)+o(S).
\tag{5.2B}

下一节用 `q_5=o(S)` 排除第一种。

---

## 6. 5-adic valuation固定 digit orientation

写

\[
e_i:=v_5(b_i).
\]

由 `(1.5)`：

\[
\frac{e_1+e_2}{S}
=\frac{g_5}{S}
\to\frac{M_*}{4}>0.
\tag{6.1}

若取 orientation `(5.2A)`，则 `b_1` 只有 `o(S)` 位，所以

\[
\frac{e_1}{S}\to0,
\]

从而

\[
\frac{e_2}{S}\to\frac{M_*}{4}.
\]

但

\[
Q=b_1 10^{m_2}+b_2.
\]

第一项的 5-depth满足

\[
\frac{v_5(b_1 10^{m_2})}{S}
=\frac{e_1+m_2}{S}\to1,
\]

而第二项 depth趋于 `M_*/4<1`。两项 depth严格分离，所以

\[
\frac{q_5}{S}
=\frac{v_5(Q)}S
\to\frac{M_*}{4}>0,
\]

与 equality必要条件 `Q_5->0` 矛盾。

因此只能有

\[
\boxed{
(m_1,m_2;n_1,n_2)
=(S,o(S);o(S),S)+o(S).}
\tag{Prefix-625}

于是长 denominator block为 `b_1`，短 denominator block为 `b_2`；特别地

\[
\frac{v_5(b_2)}S\to0,
\qquad
\frac{v_5(b_1)}S\to\frac{M_*}{4}.
\tag{6.2}

同理由 `Q_2->0` 与 2-adic height得到

\[
\frac{v_2(b_2)}S\to0,
\qquad
\frac{v_2(b_1)}S\to\frac{M_*}{2}.
\tag{6.3}

---

## 7. gap quotient 与 `c_3` 都变成次指数

从 exact factorization：

\[
F_-=2^{H+1}Z(H_{\rm sph}-y_3)\widehat g.
\]

Final-5 smooth baseline已经抽出

\[
2^{\mathfrak f+1}5^{k_5}Z.
\]

定义剩余正整数 quotient

\[
\boxed{
\mathfrak R_F
:=\frac{F_-}{2^{\mathfrak f+1}5^{k_5}Z}.}
\tag{7.1}

由 exact factors：

\[
\mathfrak R_F
=
\frac{H_{\rm sph}-y_3}{2\cdot5^T}
\cdot
\frac{\widehat g}{2^{\mathfrak g}5^{g_5}}.
\tag{7.2}

两个因子均为正整数：

- `v_2(H_sph-y_3)=1`、`v_5(H_sph-y_3)=T`；
- `c_3` 在 2、5 处均为 unit，所以
  `v_2(widehat g)=mathfrak g`、`v_5(widehat g)=g_5`。

要达到 `(1.1)` 的最终 equality，`Z-smooth-lower` 与 `F_-` upper之间不能
再损失正线性高度。因此

\[
\boxed{
\log_{10}\mathfrak R_F=o(S).}
\tag{7.3}

因为 `(7.2)` 是两个正整数乘积，分别都有

\[
\boxed{
\log_{10}\frac{H_{\rm sph}-y_3}{2\cdot5^T}=o(S),}
\tag{7.4}

\[
\boxed{
\log_{10}\frac{\widehat g}{2^{\mathfrak g}5^{g_5}}=o(S).}
\tag{7.5}

sphere gap又有

\[
H_{\rm sph}-y_3=La,
\]

且 `L` 只有 2、5 因子；`v_5(a)=q_5=o(S)`，`v_2(a)=O(1)`。
因此 `(7.4)` 推出

\[
\boxed{\log_{10}a=o(S).}
\tag{a-slow}

另一方面

\[
\widehat g=\gamma/c_3
\]

且 equality已有 `log gamma_0=o(S)`。因为 `c_3` 是 2、5-unit并整除
`gamma` 的 non-decimal part，所以

\[
\boxed{\log_{10}c_3=o(S).}
\tag{c3-slow}

---

## 8. denominator overlap几乎占满 prefix lcm

由

\[
g_*=G/c_3
\]

和 `log G=S+O(1)`、`c_3=10^{o(S)}`：

\[
\boxed{\log_{10}g_*=S+o(S).}
\tag{8.1}

但

\[
g_*=(b_1,b_2)(\operatorname{lcm}(b_1,b_2),b_3).
\]

`Prefix-625` 给 `b_2=10^{o(S)}`，故

\[
\log(b_1,b_2)=o(S).
\]

于是

\[
\boxed{
\log_{10}(\operatorname{lcm}(b_1,b_2),b_3)
=S+o(S).}
\tag{8.2}

也就是说：若 `25/4` equality ray存在，长 prefix denominator `b_1`
几乎全部 prime-power content都必须重新出现在第三分母 `b_3` 中。

这把下一步问题压成一个很窄的 denominator-overlap terminal geometry。

---

## 9. reduced `q` / overlap `eta` 的 exact Final-5 identity

在 overlap parameterization：

\[
Q=\eta Q_1,
\qquad
u=LQ_1,
\]

而 `t_2=1`：

\[
u=2\cdot5^TU,
\qquad Q=Uq.
\]

所以

\[
L\frac{Uq}{\eta}=2\cdot5^TU.
\]

约去 `U`：

\[
\boxed{
q=\eta\frac{2\cdot5^T}{L}.}
\tag{9.1}

在 Final-5 中

\[
v_5(L)=m-B_5=T-q_5,
\]

且

\[
v_2(L)=\ell\in\{0,1\}.
\]

因为 `L` 仅含 2、5：

\[
\boxed{L=2^\ell5^{T-q_5}.}
\tag{9.2}

因此

\[
\boxed{
q=\eta\,2^{1-\ell}5^{q_5}.}
\tag{q-eta}

特别地 `Z` 为 10-unit，所以

\[
\boxed{(q,Z)=(\eta,Z).}
\tag{9.3}

在 `25/4` equality ray上 `q_5=o(S)`，故由 `(q-height)`：

\[
\boxed{
\frac{\log_{10}\eta}{S}
\to Z_*
=\frac{5-7a}{4(1+a)}.}
\tag{eta-height}

这说明旧 `q-Z` bottleneck在新的 equality ray上精确变成

\[
\boxed{\gcd(\eta,Z)}
\]

的 compatibility，而不是一个额外未命名 rough factor。

---

## 10. 当前 `25/4` terminal frontier

假想 equality sequence必须同时满足：

\[
\boxed{
\begin{gathered}
M=M_*+o(1),\quad
G_5=M_*/4+o(1),\quad
G_2=T/S=M_*/2+o(1),\\
\log\gamma/S=3/4+o(1),\quad
\log V/S=1/4+o(1),\\
\log U/S=(11a-1)/(4(1+a))+o(1),\\
\log q/S=\log Z/S=\log\eta/S
=(5-7a)/(4(1+a))+o(1),\\
(m_1,m_2;n_1,n_2)=(S,o(S);o(S),S)+o(S),\\
\log a=o(S),\quad\log c_3=o(S),\quad\log g_*=S+o(S).
\end{gathered}}
\tag{625-terminal}

所以 `25/4` 已经和旧 `6.308883...` 一样，收缩成一个唯一 terminal
geometry。本文尚未排除该 ray；下一步应优先利用：

1. `b_1` 与 `b_3` 的 almost-full denominator overlap `(8.2)`；
2. `q=eta*2^{1-ell}5^{q5}` 与 `log eta=log Z+o(S)`；
3. sphere gap quotient `a=10^{o(S)}`；
4. pure-common 5-adic square-class condition与 2-balanced exact equality。

---

## 11. 状态摘要

- **`已严格完成（conditional rigidity）`**：`25/4` equality若存在，则所有
  normalized ratios由 `(625-terminal)` 唯一确定。
- **`已严格完成`**：equality digit orientation唯一为
  `(S,o;o,S)`，不是仅“交换前两块”。
- **`已严格完成`**：`a,c_3` 次指数，prefix lcm 与 `b_3` almost-full overlap。
- **`已严格完成`**：Final-5 exact `q-eta` identity与 `(q,Z)=(eta,Z)`。
- **`待证`**：排除 `25/4` equality ray，或将其量化为显式 `<25/4`；
  DD 全局仍未关闭。

---

<a id="source-high-funnel-defect-optimization"></a>

> 整合来源：`high-funnel-defect-optimization.md`

# DD double-resonant high funnel 的 defect-aware stability 与 `6.215109...` tail-short bound

> **依赖：** [`high-funnel-five-adic-dichotomy.md`](high-funnel-ledger.md#source-high-funnel-five-adic-dichotomy)、`core.md` 的 `t_2=1` 二进 resonance、五进 resonance、`F_-` small-factor 上界与两个 multiplicative height bounds。
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

---

<a id="source-high-funnel-denominator-max-lock"></a>

> 整合来源：`high-funnel-denominator-max-lock.md`

# DD remaining high funnel 的 5-adic denominator-max lock

> **依赖：** [`high-funnel-gap-depth.md`](high-funnel-ledger.md#source-high-funnel-gap-depth)、`core.md` 的 integer lift / denominator valuations、`high-funnel-defect-optimization.md` 的 defect-aware stability。
>
> **严格状态：** `已严格完成（remaining high-funnel）`。本文把 slope `>6.215109404735...` 的最后 `Defect-heavy` 候选按第三分母是否承担最大 5-adic denominator depth 分开。
>
> 结论：若 `b_3` 不是 5-adic maximum，则 defect-aware stability 立刻给 `n<6S+O(1)`；因此真正剩余的高 slope支必须满足 `b_3` 为 5-adic maximum。此时 sphere common scale在 `(H,y_3)` 端为零，并且所有 valuation被锁成
> \[
> \boxed{
> B_5=q_5+2g_5,
> \qquad
> m=2q_5+4g_5+n_5,
> \qquad
> v_5(a)=v_5(\Xi)=q_5.
> }
> \]
> 进一步 `T:=k_5-g_5=m-2g_5`，且 `v_5(H-y_3)=T`。

---

## 1. denominator 5-adic maximum 与 ghost coordinates

记

\[
e_i:=v_5(b_i),
\qquad
B_5:=v_5(b_3),
\]

\[
\boxed{E_5:=\max(e_1,e_2,B_5).}
\tag{1.1}

因为

\[
q_{\rm lcm}=\operatorname{lcm}(b_1,b_2,b_3),
\]

有

\[
v_5(q_{\rm lcm})=E_5.
\]

而

\[
y_i=a_i\frac{q_{\rm lcm}}{b_i}.
\]

high funnel已有 `5|b_3`，故 reducedness给

\[
v_5(a_3)=0.
\]

因此

\[
\boxed{v_5(y_3)=E_5-B_5.}
\tag{1.2}

另外

\[
G=b_1b_2,
\]

所以

\[
\boxed{e_1+e_2=g_5.}
\tag{1.3}

---

## 2. sphere factorization 的 exact 5-depth balance

令

\[
D_5:=v_5(H-y_3),
\qquad
s_5:=\min(v_5(H),v_5(y_3)).
\]

`high-funnel-gap-depth.md` 已证明在 remaining branch

\[
\boxed{D_5=m+2q_5+2g_5-2B_5.}
\tag{2.1}

而

\[
s_5\le v_5(y_3)=E_5-B_5.
\]

由 `(1.3)`，

\[
E_5\le\max(B_5,g_5),
\]

所以

\[
\boxed{s_5\le\max(0,g_5-B_5).}
\tag{2.2}

又 `B_5<m`。若 `g_5<=B_5`，则 `s_5=0<D_5`。若 `g_5>B_5`：

\[
D_5-(g_5-B_5)
=m+2q_5+g_5-B_5>0.
\]

因此统一有

\[
\boxed{D_5>s_5.}
\tag{2.3}

5 为奇素数。odd-prime two-factor lemma应用于 `H,y_3` 给

\[
\boxed{v_5(H+y_3)=s_5.}
\tag{2.4}

sphere identity

\[
(H-y_3)(H+y_3)=y_1^2+y_2^2
\]

于是

\[
\boxed{v_5(y_1^2+y_2^2)=D_5+s_5.}
\tag{2.5}

另一方面

\[
y_1^2+y_2^2
=\left(\frac{q_{\rm lcm}}G\right)^2\mathcal N_{12}.
\]

故

\[
\boxed{
D_5+s_5
=2(E_5-g_5)+n_5.
}
\tag{Sphere5-balance}

---

## 3. 若 `b_3` 不是 maximum，则 slope <= 6

设

\[
E_5>B_5.
\]

由 `(1.3)`：

\[
E_5\le g_5.
\]

所以 `Sphere5-balance` 的右边不超过 `n_5`：

\[
D_5+s_5\le n_5.
\]

从而

\[
\boxed{D_5\le n_5.}
\tag{3.1}

用 `(2.1)` 与 high-funnel exact relation

\[
3B_5=m+q_5+2g_5-n_5
\]

消去 `B_5`，得到

\[
\boxed{3D_5=m+4q_5+2g_5+2n_5.}
\tag{3.2}

结合 `D_5<=n_5`：

\[
\boxed{m+4q_5+2g_5\le n_5.}
\tag{3.3}

特别地

\[
2q_5+g_5+n_5\ge m.
\]

而 defect-aware stability给

\[
n<6S+\frac{2b}{3}m
-\frac{2b}{3}(2q_5+g_5+n_5)
-2a\mathfrak q-a\mathfrak n
+O(1).
\]

所以

\[
\boxed{n<6S+O(1).}
\tag{Nonmax-six}

因此任何 remaining sequence若满足 slope `>6.215109...`，最终必须有

\[
\boxed{E_5=B_5.}
\tag{B3-max}

---

## 4. `b_3` maximum 时 `H,y_3` 都是 5-units

由 `(B3-max)` 与 `(1.2)`：

\[
\boxed{v_5(y_3)=0.}
\]

而 `D_5>0`，即

\[
5\mid H-y_3.
\]

所以

\[
H\equiv y_3\not\equiv0\pmod5,
\]

故

\[
\boxed{v_5(H)=0,\qquad s_5=0.}
\tag{4.1}

`Sphere5-balance` 因而化成

\[
\boxed{D_5=2(B_5-g_5)+n_5.}
\tag{4.2}

---

## 5. 解出全部 5-adic variables

一方面 `(2.1)`：

\[
D_5=m+2q_5+2g_5-2B_5.
\tag{5.1}

与 `(4.2)` 比较：

\[
m+2q_5+2g_5-2B_5
=2B_5-2g_5+n_5.
\]

所以

\[
\boxed{m=4B_5-2q_5-4g_5+n_5.}
\tag{5.2}

另一方面 high-funnel resonance给

\[
\boxed{m=3B_5-q_5-2g_5+n_5.}
\tag{5.3}

两式相减：

\[
\boxed{B_5=q_5+2g_5.}
\tag{B-lock}

代回 `(5.3)`：

\[
\boxed{m=2q_5+4g_5+n_5.}
\tag{m-lock}

`high-funnel-gap-depth.md` 已有

\[
3v_5(a)=5q_5+4g_5+n_5-m.
\]

使用 `(m-lock)`：

\[
\boxed{v_5(a)=q_5.}
\tag{a-lock}

而 `v_5(a)=v_5(Xi)`，故

\[
\boxed{v_5(\Xi)=q_5.}
\tag{Xi-lock}

---

## 6. S-unit exponent 与 gap depth也同步锁定

由 tail weight

\[
k_5=m+q_5+g_5-B_5.
\]

使用 `(B-lock)`：

\[
\boxed{k_5=m-g_5.}
\tag{6.1}

定义 high-funnel 5-adic S-unit exponent

\[
\boxed{T:=k_5-g_5.}
\]

于是

\[
\boxed{T=m-2g_5.}
\tag{T-lock}

再由 `(4.2)` 和 `(B-lock)`：

\[
D_5
=2q_5+2g_5+n_5.
\]

而 `(m-lock)` 给

\[
m-2g_5=2q_5+2g_5+n_5.
\]

所以

\[
\boxed{v_5(H-y_3)=D_5=T.}
\tag{Gap-T-lock}

这与旧 extremal terminal 的 `v_5(H-y_3)=T+o(S)` 现象一致，但本文是在 remaining high-funnel branch中由 exact denominator-max ledger重新得到。

---

## 7. 最终 remaining branch 的形状

任何 double-resonant high-funnel sequence若试图保持

\[
\limsup n/S>6.215109404735\ldots,
\]

最终必须同时满足：

\[
\boxed{
\begin{gathered}
B_5=E_5=q_5+2g_5,\\
m=2q_5+4g_5+n_5,\\
v_5(a)=v_5(\Xi)=q_5,\\
T=m-2g_5,\\
v_5(H-y_3)=T,\\
v_5(H)=v_5(y_3)=0.
\end{gathered}}
\tag{Final-5-lock}

这已经不再是 generic defect-heavy region，而是一条非常刚性的 5-adic sheet。

特别地 LP 的 pure common-scale extremizer `q_5=n_5=0` 会退化成

\[
\boxed{
B_5=2g_5,
\qquad
m=4g_5,
\qquad
T=2g_5,
\qquad
v_5(a)=0.
}
\tag{Pure-common}

下一步应专门分析这一类 denominator exponent pattern，而不再对 `q_5,g_5,n_5` 做自由 LP。

---

## 8. 状态摘要

- **`已严格完成`**：`Sphere5-balance`、non-max `b_3` branch `n<6S+O(1)`、`B-lock`、`m-lock`、`a/Xi-lock`、`T/Gap-lock`。
- **`结构压缩`**：remaining slope `>6.215109...` high funnel lies on `Final-5-lock`.
- **`待证`**：pure/common-scale denominator pattern；new global numerical limsup；DD global closure/effective height bound。

---

<a id="source-high-funnel-exact-small-factor-normalization"></a>

> 整合来源：`high-funnel-exact-small-factor-normalization.md`

# DD canonical `t_2=1` funnel 的 exact small-factor normalization

> **依赖：** `core.md` §27.33 的 gcd-normal form、`t_2=1` S-unit phase、通用恒等式
> \(F_-Q(\kappa+G)=E\kappa(\kappa+2G)\)、§35 的 exact small-factor factorization、§37 的 overlap 参数化。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
>
> 本文修正一个容易混淆的记号点：§6 gcd-normal form 的 reduced quotient 与后续
> `Q=Uq` 中的 source factor `q` 并不必然相同；两者只差一个 `2,5`-smooth gcd。
> 正确拆分后，旧 terminal 工作中看似需要研究的 `gcd(q,Z)` 可以从 exact
> small-factor identity 中完全消去。最终得到
> \[
> \boxed{
> F_-=
> \frac{2^{H+2}5^TZ}{(2\cdot5^T,q)}
> \;a\frac{g_*}{V}.
> }
> \]
> 特别地 `Z` 是 10-unit，因此
> \[
> \boxed{Z\mid F_-.}
> \]

---

## 1. 区分两个 `q`

gcd-normal form 先写

\[
\kappa=\gamma u,
\qquad
G=\gamma v,
\qquad
(u,v)=1,
\]

并定义

\[
d_0=(u,Q),
\qquad
u=d_0r,
\qquad
Q=d_0q_{\rm red},
\qquad
(r,q_{\rm red})=1,
\]

其中

\[
r\mid10^m.
\]

在 canonical `t_2=1` S-unit phase 中，另一方面写

\[
\boxed{
u=2\cdot5^TU,\qquad v=V,}
\tag{1.1}
\]

\[
\boxed{Q=Uq,}
\tag{1.2}
\]

并有

\[
(UV,10)=1,
\qquad
(U,V)=1.
\]

这里 `(1.2)` 中的 `q` 不应未经审计地与 `q_red` 认同。令

\[
\boxed{r_0:=2\cdot5^T,}
\qquad
\boxed{s:=(r_0,q).}
\tag{1.3}

则

\[
(u,Q)
=(r_0U,Uq)
=U(r_0,q)
=Us.
\]

所以真正的 gcd-normal reduced pair 为

\[
\boxed{
r=\frac{r_0}{s},
\qquad
q_{\rm red}=\frac q s.
}
\tag{1.4}

特别地

\[
(r,q_{\rm red})=1.
\]

这正是此前直接从 `Q=Uq` 推断 `(q,10)=1` 的错误所在：只有
`q_red` 与 `r` 互素；source factor `q` 自己可以携带被 `s` 记录的
`2,5`-depth。

---

## 2. tail recovery 精确给出 `L` 与 `tau`

原 gcd-normal tail recovery 为

\[
\boxed{b_3=vt,\qquad ut=10^mQ.}
\tag{2.1}

代入 `(1.1)`、`(1.2)`：

\[
r_0Ut=10^mUq,
\]

约去 `U`：

\[
\boxed{r_0t=10^mq.}
\tag{2.2}

使用 `(1.4)`：

\[
rt=10^mq_{\rm red}.
\]

因为 `(r,q_red)=1` 且 `r|10^m`，有

\[
\boxed{
t=\frac{10^m}{r}\,q_{\rm red}.}
\tag{2.3}

现在 `b_3=Vt`，而 `(r,V)=1` 来自 `(u,v)=1`。于是

\[
\begin{aligned}
\omega
&=(10^m,b_3)\\
&=\left(10^m,
V\frac{10^m}{r}q_{\rm red}\right)\\
&=\frac{10^m}{r}
\,(r,Vq_{\rm red})\\
&=\frac{10^m}{r}.
\end{aligned}
\]

因此 DD tail normalization

\[
L=\frac{10^m}{\omega},
\qquad
\tau=\frac{b_3}{\omega}
\]

精确化成

\[
\boxed{
L=r=\frac{2\cdot5^T}{s},
\qquad
\tau=q_{\rm red}V=\frac q sV.
}
\tag{Tail-reduced}

这里没有渐近误差。

---

## 3. reduced source factor自动整除真实 decimal determinant

DD determinant 为

\[
\boxed{
E=b_3A_{12}10^d-a_3Q.
}
\tag{3.1}

由 `(Tail-reduced)`：

\[
b_3=\omega q_{\rm red}V,
\qquad
Q=Usq_{\rm red}.
\]

所以

\[
\boxed{q_{\rm red}\mid E.}
\tag{3.2}

定义

\[
\boxed{
E_0:=\frac{E}{q_{\rm red}}
=\omega VA_{12}10^d-a_3Us.
}
\tag{3.3}

这一步是 exact integer cancellation；不能把它错误加强为 `q|E`，因为
`s` 未必为 1。

---

## 4. universal identity 中的 rough `q` 层全部约掉

令

\[
\boxed{X:=2^HZ,\qquad Y:=5^TU.}
\tag{4.1}

S-unit phase 为

\[
X-Y=V.
\]

于是

\[
u=2Y,
\qquad
u+v=X+Y,
\qquad
u+2v=2X.
\]

通用恒等式

\[
F_-Q(\kappa+G)=E\kappa(\kappa+2G)
\]

在

\[
Q=Uq,
\quad
\kappa=2\gamma5^TU,
\quad
G=\gamma V
\]

下化为

\[
\boxed{
F_-q(X+Y)
=4E\gamma\,2^H5^TZ.
}
\tag{4.2}

使用

\[
q=sq_{\rm red},
\qquad
E=q_{\rm red}E_0,
\]

约去 `q_red`：

\[
\boxed{
F_-s(X+Y)
=4E_0\gamma\,2^H5^TZ.
}
\tag{4.3}

注意 `q-Z` 的所有 non-decimal common prime已经不再出现在 `(4.3)` 左边的
source factor中；唯一留下的是 `s|(2*5^T)` 的 decimal smooth overlap。

---

## 5. `X+Y` 与 smooth--`Z` carrier互素

由 `(UV,10)=1`，`U,V` 都是奇数且为 5-units；所以

\[
5^TU+V
\]

为偶数，从而 `H>=1`。

若某个 odd prime `p|U,Z`，则由

\[
2^HZ-5^TU=V
\]

强迫 `p|V`，与 `(U,V)=1` 矛盾。因此

\[
\boxed{(U,Z)=1.}
\tag{5.1}

故

\[
(X,Y)=1.
\]

于是

\[
(X+Y,X)=1.
\]

又 `X+Y` 为奇数；若 `T>0`，则

\[
X+Y\equiv X\not\equiv0\pmod5,
\]

而 `T=0` 时没有 5-factor需要处理。因此统一有

\[
\boxed{
(X+Y,\,2^{H+2}5^TZ)=1.
}
\tag{5.2}

从 `(4.3)` 与 `(5.2)`：

\[
\boxed{X+Y\mid E_0\gamma.}
\tag{5.3}

定义正整数

\[
\boxed{
R:=\frac{E_0\gamma}{X+Y}>0.
}
\tag{5.4}

则 `(4.3)` 给

\[
\boxed{
F_-
=\frac{2^{H+2}5^TZ}{s}\,R.
}
\tag{5.5}

因为 `s|2*5^T`，右侧 smooth coefficient是整数。

特别地 `Z` 为 10-unit，因此

\[
\boxed{Z\mid F_-.}
\tag{Z-divides-Fminus}

这条结论完全没有 `gcd(q,Z)` 损失。

---

## 6. `R` 精确等于 sphere-gap × normalized overlap

`core.md` §35 的 exact factorization 为

\[
\boxed{
F_-
=a\,g_*
\frac{L(LQ+2\tau)}{\tau}.
}
\tag{6.1}

使用 `(Tail-reduced)`：

\[
L=\frac{2\cdot5^T}{s},
\qquad
Q=Usq_{\rm red},
\qquad
\tau=q_{\rm red}V.
\]

于是

\[
\begin{aligned}
LQ+2\tau
&=2\cdot5^TUq_{\rm red}+2q_{\rm red}V\\
&=2q_{\rm red}(5^TU+V)\\
&=2q_{\rm red}X.
\end{aligned}
\tag{6.2}

代回 `(6.1)`：

\[
\begin{aligned}
F_-
&=a g_*
\frac{L\,2q_{\rm red}X}{q_{\rm red}V}\\
&=\frac{2a g_*LX}{V}\\
&=\frac{2^{H+2}5^TZ}{s}
\;a\frac{g_*}{V}.
\end{aligned}
\tag{6.3}

§37 overlap 参数化写

\[
g_*=vc\lambda r_*,
\]

其中这里的 reduced tail denominator `v` 正是当前 `V`。因此

\[
\boxed{V\mid g_*.}
\tag{6.4}

比较 `(5.5)` 与 `(6.3)`，得到 canonical normalized quotient

\[
\boxed{
R=a\frac{g_*}{V}\in\mathbf Z_{>0}.
}
\tag{R-exact}

最终 exact small-factor normalization 为

\[
\boxed{
F_-=
\frac{2^{H+2}5^TZ}{(2\cdot5^T,q)}
\;a\frac{g_*}{V}.
}
\tag{Exact-Fminus-t2}

---

## 7. height 形式

取十进制对数，`(Exact-Fminus-t2)` 给

\[
\boxed{
\log_{10}F_-
=(H+2)\log_{10}2
+T\log_{10}5
+\log_{10}Z
-\log_{10}s
+\log_{10}a
+\log_{10}\frac{g_*}{V}.
}
\tag{7.1}

又

\[
2^HZ=5^TU+V
=5^TU\left(1+\frac{V}{5^TU}\right),
\]

所以

\[
\boxed{
\begin{aligned}
\log_{10}F_-
={}&2T\log_{10}5+\log_{10}U\\
&+\log_{10}\left(1+\frac{V}{5^TU}\right)
+2\log_{10}2\\
&-\log_{10}s
+\log_{10}a
+\log_{10}\frac{g_*}{V}.
\end{aligned}}
\tag{7.2}

这把旧 stability 中被压缩的 payer完整暴露为：

- forced S-unit baseline `2T log 5 + log U`；
- smooth overlap loss `log s`；
- sphere-gap quotient `a`；
- normalized denominator overlap `g_*/V`。

其中不再出现 `gcd(q,Z)`。

---

## 8. 与旧 `q-Z` allocation 的关系

`high-funnel-qz-gcd-allocation.md` 与
`high-funnel-qz-projective-allocation.md` 中的 divisibility ledger本身仍然成立；
但它们把 `gcd(q,Z)` 当作 `L_Z|F_-` 中的 potential height loss继续分配给
`gamma / R_3^den / Z_0 / a`。

`(Exact-Fminus-t2)` 更强：在同一个 canonical `t_2=1` funnel 中，经过
正确区分 `q` 与 `q_red` 后，full 10-unit `Z` 已经无条件整除 `F_-`。
因此这些 `q-Z` payer files 应降级为**正确但被更强 exact normalization 覆盖的中间账本**，不再是当前 bottleneck。

下一目标应改为研究

\[
\boxed{a\,g_*/V}
\]

的 Archimedean height / prime allocation，而不是继续尝试从
`p|gcd(q,Z)` 推出两条 carrier residual 的传播。

---

## 9. 状态摘要

- **`已严格完成`**：`Tail-reduced`、`q_red|E`、rough-`q` cancellation、
  `Z|F_-`、`R-exact`、`Exact-Fminus-t2`。
- **`失效/降级`**：把 `q-Z gcd` 当作 canonical `t_2=1` funnel 的真实
  small-factor height bottleneck；以及从 `Q=Uq` 未经审计地推断 `(q,10)=1`。
- **`待证`**：对 `a(g_*/V)` 建立新的 global charge；由 `(7.2)` 恢复更强的
  defect-aware stability；DD 全局空性 / effective height bound。

---

<a id="source-high-funnel-final-five-collapse"></a>

> 整合来源：`high-funnel-final-five-collapse.md`

# DD `Final-5-lock` 的 full smooth-overlap collapse

> **依赖：** [`high-funnel-exact-small-factor-normalization.md`](high-funnel-ledger.md#source-high-funnel-exact-small-factor-normalization)、
> [`high-funnel-two-adic-balance.md`](high-funnel-ledger.md#source-high-funnel-two-adic-balance) 的 shallow-gap 与 Schmidt budget、
> [`high-funnel-denominator-max-lock.md`](high-funnel-ledger.md#source-high-funnel-denominator-max-lock) 的 `Final-5-lock`、
> [`high-funnel-defect-optimization.md`](high-funnel-ledger.md#source-high-funnel-defect-optimization) 的 `Tail-short` bound、
> `core.md` 的 `d`-dominant small-factor upper bound与 `Q/G` constant window。
>
> **严格状态：** `已严格完成（canonical double-resonant t_2=1 funnel）`。
>
> 关键修正：exact small-factor normalization 中，除 5-adic charge 外还存在一份此前
> sector LP 未收费的完整二进 overlap
> \[
> v_2\!\left(\frac{a(g_*/V)}{s}\right)=\mathfrak g,
> \qquad s=(2\cdot5^T,q).
> \]
> 把这项保留后，`Final-5-lock` 的整个剩余 sector满足
> \[
> \boxed{
> \limsup\frac nS
> \le
> 2+3\frac{\frac32+\frac12\log_{10}2}{1+\log_{10}2}
> =5.805865360520\ldots.
> }
> \]
> 因而此前 `>6.215109...` 的 Defect-heavy remaining sheet为空。
> 结合 `Tail-short <= 6.215109404735...`，得到 canonical double-resonant
> `t_2=1` funnel 的显式 sector bound
> \[
> \boxed{
> \limsup\frac nS
> \le
> \frac{28}{3+5\log_{10}2}
> =6.215109404735\ldots.
> }
> \]
> 本文不自动把该 sector bound外推成新的全 DD numerical limsup；全局分类作用域仍按
> `core.md` 读取。

---

## 1. 记号与 `Final-5-lock`

令

\[
a_2:=\log_{10}2,
\qquad
b_5:=\log_{10}5=1-a_2.
\]

为避免和 sphere-gap quotient `a` 混淆，本文把两个对数常数写成
`a_2,b_5`。

对无界 sequence 归一化：

\[
M=\frac mS,
\quad Q_5=\frac{q_5}{S},
\quad G_5=\frac{g_5}{S},
\quad N_5=\frac{n_5}{S},
\]

\[
Q_2=\frac{\mathfrak q}{S},
\quad G_2=\frac{\mathfrak g}{S},
\quad N_2=\frac{\mathfrak n}{S},
\quad
G_0^{\rm rough}=\frac{\log_{10}\gamma_0}{S}.
\]

`Final-5-lock` 给

\[
\boxed{
M=2Q_5+4G_5+N_5,
}
\tag{1.1}

以及

\[
\boxed{
T/S=M-2G_5.
}
\tag{1.2}

因此

\[
\boxed{G_5\le M/4.}
\tag{1.3}

---

## 2. exact small factor 的 2/5-adic full charge

`high-funnel-exact-small-factor-normalization.md` 已证明

\[
\boxed{
F_-=
\frac{2^{H+2}5^TZ}{s}
\;a\frac{g_*}{V},
\qquad
s=(2\cdot5^T,q).
}
\tag{2.1}

这里 source factor由 `Q=Uq` 定义，且 `(UV,10)=1`，所以

\[
v_2(q)=\mathfrak q,
\qquad
v_5(q)=q_5.
\tag{2.2}

### 2.1 五进净深度

`Final-5-lock` 给

\[
v_5(a)=q_5,
\qquad
v_5(g_*/V)=g_5.
\tag{2.3}

又

\[
T=2q_5+2g_5+n_5\ge q_5,
\]

所以

\[
v_5(s)=q_5.
\tag{2.4}

因此 `(2.1)` 中 5-adic 总贡献为

\[
\boxed{
T-q_5+q_5+g_5=T+g_5.
}
\tag{2.5}

### 2.2 二进净深度

`high-funnel-two-adic-balance.md` 的 shallow-gap theorem给

\[
v_2(a)=
\begin{cases}
0,&\mathfrak q=0,\\
1,&\mathfrak q\ge1.
\end{cases}
\tag{2.6}

另一方面

\[
v_2(s)=\min(1,\mathfrak q),
\tag{2.7}

所以

\[
\boxed{v_2(a)=v_2(s).}
\tag{2.8}

`b_3` 是二进 unique maximum；因此 `c_3=q_lcm/b_3` 为二进单位，而

\[
\frac{g_*}{V}=\frac\gamma{c_3},
\qquad V\text{ odd}.
\]

故

\[
\boxed{v_2(g_*/V)=\mathfrak g.}
\tag{2.9}

于是 `(2.1)` 中 smooth quotient在强制 `2^{H+2}` 之外还有完整

\[
\boxed{\mathfrak g}
\]

层：

\[
\boxed{
 v_2\!\left(\frac{a(g_*/V)}s\right)=\mathfrak g.
}
\tag{2-full-charge}

这正是此前 `2-balanced` sector estimate 中被保守丢掉的一项。

---

## 3. sharpened `F_-` lower bound

令

\[
U_h:=\frac{\log_{10}U}{S},
\qquad
Z_h:=\frac{\log_{10}Z}{S}.
\]

S-unit phase

\[
2^HZ=5^TU+V
\]

与 tail window给

\[
a_2\frac HS+Z_h
=b_5\frac TS+U_h+o(1).
\tag{3.1}

由 `(2.1)`、`(2.5)`、`(2-full-charge)`：

\[
\begin{aligned}
\frac{\log_{10}F_-}{S}
&\ge
 a_2\left(\frac HS+G_2\right)
+b_5\left(\frac TS+G_5\right)
+Z_h+o(1)\\
&=
2b_5\frac TS+b_5G_5+U_h+a_2G_2+o(1).
\end{aligned}
\]

使用 `T/S=M-2G_5`：

\[
\boxed{
\frac{\log_{10}F_-}{S}
\ge
2b_5M-3b_5G_5+U_h+a_2G_2+o(1).
}
\tag{F-lower-full}

---

## 4. 与 Archimedean small-factor upper bound 联立

canonical `d`-dominant funnel 的旧 small-factor ratio给

\[
\boxed{
\log_{10}F_-<4S+2m-n+O(1).
}
\tag{4.1}

若沿子序列

\[
C_*:=\limsup n/S,
\]

则 `(F-lower-full)` 与 `(4.1)` 给

\[
\boxed{
C_*
\le
4+2a_2M+3b_5G_5-U_h-a_2G_2.
}
\tag{4.2}

---

## 5. `U-height` 中的二进 overlap精确抵消

`Q` 为 `S` 位十进制拼接，且

\[
1<Q/G\le11.
\]

所以

\[
\log_{10}Q=S+O(1),
\qquad
\log_{10}G=S+O(1).
\]

又

\[
QG<\kappa\le10QG,
\]

故

\[
\frac{\log_{10}\kappa}{S}=2+o(1).
\]

写

\[
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0,
\qquad
(\gamma_0,10)=1,
\]

以及

\[
\kappa=2\gamma5^TU.
\]

得到 exact asymptotic height identity

\[
\boxed{
U_h
=2-a_2G_2-G_0^{\rm rough}
-b_5(M-G_5)+o(1).
}
\tag{U-height}

代回 `(4.2)`，`a_2G_2` **精确抵消**：

\[
\boxed{
C_*
\le
2+(1+a_2)M+2b_5G_5+G_0^{\rm rough}+o(1).
}
\tag{5.1}

这不是重复计费；`(F-lower-full)` 的 `+a_2G_2` 来自 actual divisor
`g_*/V`，而 `(U-height)` 的 `-a_2G_2` 来自从 `kappa` 中剥去 `gamma` 后
`U` 的余因子高度。两者由两个 exact identities分别读取同一份 factor allocation。

---

## 6. Final-5 + Schmidt budget 的 dual bound

由 `(1.3)`：

\[
2b_5G_5\le\frac{b_5}{2}M.
\]

所以 `(5.1)` 给

\[
\boxed{
C_*
\le
2+\left(\frac32+\frac{a_2}{2}\right)M
+G_0^{\rm rough}+o(1).
}
\tag{6.1}

`high-funnel-two-adic-balance.md` 已在 `Final-5-lock` 上证明

\[
\boxed{
(1+a_2)M
+2a_2Q_2+a_2N_2+2G_0^{\rm rough}
\le3+o(1).
}
\tag{Schmidt-budget}

定义

\[
\lambda_*:=
\frac{\frac32+\frac{a_2}{2}}{1+a_2}.
\]

因为

\[
\lambda_*>rac12,
\]

将 `(Schmidt-budget)` 乘 `lambda_*` 后，其 `M` coefficient与 `(6.1)`
恰好相等，而 `G_0^{rough}` coefficient至少为 1；`Q_2,N_2` 只增加非负
slack。因此

\[
\boxed{
C_*
\le
2+3\lambda_*.
}
\tag{6.2}

即

\[
\boxed{
C_*
\le
2+3\frac{\frac32+\frac12\log_{10}2}
{1+\log_{10}2}
=5.805865360520\ldots.
}
\tag{Final5-collapse}

---

## 7. 与 five-adic dichotomy 合并

`high-funnel-five-adic-dichotomy.md` 把 canonical high funnel分成：

### Tail-short

`high-funnel-defect-optimization.md` 已证明

\[
\boxed{
\limsup\frac nS
\le
\frac{28}{3+5\log_{10}2}
=6.215109404735\ldots.
}
\]

### Defect-heavy

若它试图保持 slope `>6.215109...`，
`high-funnel-denominator-max-lock.md` 会把它压入 `Final-5-lock`。
但本文证明整个 `Final-5-lock` 只有

\[
5.805865360520\ldots
<6.215109404735\ldots.
\]

矛盾。

因此 canonical double-resonant `t_2=1` funnel整体满足 sector bound

\[
\boxed{
\limsup\frac nS
\le
\frac{28}{3+5\log_{10}2}
=6.215109404735\ldots.
}
\tag{Canonical-funnel-bound}

---

## 8. 状态与作用域

- **`已严格完成（sector）`**：full 2-adic overlap charge、`F-lower-full`、
  `Final5-collapse`。
- **`已严格完成（canonical funnel）`**：结合 five-adic dichotomy，得到
  `t_2=1` double-resonant canonical funnel `limsup <= 6.215109404735...`。
- **`失效/降级`**：把 `2-balanced` 视为 Final-5 的唯一可收费二进子支；
  `high-funnel-two-balanced-collapse.md` 仍正确，但已被本文更强的整个
  `Final-5` collapse覆盖。
- **`待证`**：把 sector-level `6.215109...` 与 `core.md` 全 DD 分类的其余
  asymptotic branches重新优化，判断是否得到新的**全 DD**显式 limsup；DD 空性/
  effective absolute height bound仍开放。

---

<a id="source-high-funnel-final5-sphere-c3-collapse"></a>

> 整合来源：`high-funnel-final5-sphere-c3-collapse.md`

# DD `Final-5` 的 sphere–`c_3` collapse

> **依赖：** [`high-funnel-denominator-max-lock.md`](high-funnel-ledger.md#source-high-funnel-denominator-max-lock)、
> [`high-funnel-two-adic-balance.md`](high-funnel-ledger.md#source-high-funnel-two-adic-balance)、
> [`high-funnel-fminus-sunit-factorization.md`](high-funnel-ledger.md#source-high-funnel-fminus-sunit-factorization)、
> `core.md` 的 integer sphere、overlap parameterization 与 d-dominant digit/surplus bounds。
>
> **严格状态：** `已严格完成（canonical Final-5 sector）`。
>
> 本文给出一个比此前 `25/4` 更强、而且不需要接近任何 equality ray 的
> Archimedean payer。令
> \[
> c_3:=\frac{q_{\rm lcm}}{b_3}.
> \]
> 则 sphere factorization直接给
> \[
> \boxed{
> c_3>
> \frac{L\,a_3\,G^2}{b_3^2\mathcal N_{12}}.}
> \]
> 在 `Final-5` 中 `c_3` 是 10-unit，且 exact overlap factorization给
> `c_3|gamma_0`。与 `Subspace-Final5` 联立后得到
> \[
> \boxed{
> \limsup_{\rm Final\text{-}5}\frac nS
> \le
> \frac72+\frac3{1+\log_{10}2}
> =5.805865360520\ldots.}
> \]
>
> 因为 `Final-5` 原本只是在排除 `Tail-short`、non-max 等支以后，为研究
> slope `>6.215109404735...` 而留下的最后支，所以这个上界在原 branch tree
> 中直接形成矛盾：**不存在 slope `>6.215109...` 的 Final-5 sequence。**
> 因而 canonical `t_2=1` double-resonant funnel 的显式最坏支重新变成
> Tail-short：
> \[
> \boxed{
> \limsup_{\rm canonical\ t_2=1\ double\text{-}resonant}
> \frac nS
> \le6.215109404735\ldots.}
> \]
> 这仍是 sector conclusion，不在本文中外推为全 DD numerical limsup。

---

## 1. sphere 中 `c_3` 的 exact lower payer

令整数球面 lcm denominator为

\[
q_{\rm lcm}=\operatorname{lcm}(b_1,b_2,b_3),
\]

并定义

\[
\boxed{c_3:=q_{\rm lcm}/b_3.}
\tag{1.1}

于是

\[
y_3=a_3c_3.
\tag{1.2}

又

\[
y_1^2+y_2^2
=\left(\frac{q_{\rm lcm}}G\right)^2\mathcal N_{12}
=\left(\frac{b_3c_3}{G}\right)^2\mathcal N_{12}.
\tag{1.3}

sphere gap normalization为

\[
H_{\rm sph}-y_3=La,
\qquad a\in\mathbf Z_{>0}.
\tag{1.4}

所以

\[
La(H_{\rm sph}+y_3)
=\frac{b_3^2c_3^2}{G^2}\mathcal N_{12}.
\tag{1.5}

因为

\[
a\ge1,
\qquad
H_{\rm sph}+y_3>y_3=a_3c_3,
\]

由 `(1.5)` 严格得到

\[
L a_3c_3
<\frac{b_3^2c_3^2}{G^2}\mathcal N_{12}.
\]

约去正数 `c_3`：

\[
\boxed{
 c_3>
 \frac{L\,a_3\,G^2}{b_3^2\mathcal N_{12}}.}
\tag{Sphere-c3}

这条式子不使用 `25/4` equality、`q-Z` gcd 或 Gaussian orientation。

---

## 2. d-dominant digit heights

当前 canonical high funnel在 d-dominant sector，已有

\[
s_1+s_2\le2,
\qquad
s_i=n_i-m_i,
\qquad
S=m_1+m_2.
\]

第三 numerator `a_3` 有 `n=m+d` 位，所以

\[
\boxed{a_3\ge10^{n-1}.}
\tag{2.1}

前两 denominator均非空：

\[
b_i\ge10^{m_i-1},
\]

故

\[
\boxed{G=b_1b_2\ge10^{S-2}.}
\tag{2.2}

第三 denominator有 `m` 位：

\[
\boxed{b_3<10^m.}
\tag{2.3}

对 prefix norm

\[
\mathcal N_{12}
=(a_1b_2)^2+(a_2b_1)^2
\]

有

\[
n_1+m_2=S+s_1,
\qquad
n_2+m_1=S+s_2.
\]

而 d-dominant surplus simplex给

\[
\max(s_1,s_2)\le S.
\]

所以两个 cross products均小于 `10^{2S}`，从而

\[
\boxed{
\mathcal N_{12}<2\cdot10^{4S}.}
\tag{2.4}

把 `(2.1)`--`(2.4)` 代入 `(Sphere-c3)`：

\[
\boxed{
\log_{10}c_3
\ge
n-2m-2S+\log_{10}L-O(1).}
\tag{c3-height-lower}

这里 `O(1)` 是绝对常数；例如可取吸收 `1+4+log10 2` 的固定常数。

---

## 3. Final-5 中 `c_3` 必须由 rough overlap `gamma_0` 支付

`Final-5` 已证明：

1. `b_3` 是二进 unique maximum；
2. `b_3` 是五进 maximum。

因此 lcm quotient `c_3=q_lcm/b_3` 在 2、5 两处都是 unit：

\[
\boxed{(c_3,10)=1.}
\tag{3.1}

另一方面 `high-funnel-fminus-sunit-factorization.md` 从 overlap parameterization
严格得到

\[
\widehat g=\frac\gamma{c_3}\in\mathbf Z_{>0}.
\]

所以

\[
\boxed{c_3\mid\gamma.}
\tag{3.2}

写

\[
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0,
\qquad
(\gamma_0,10)=1.
\]

由 `(3.1)`、`(3.2)`：

\[
\boxed{c_3\mid\gamma_0.}
\tag{3.3}

因此

\[
\boxed{
\log_{10}c_3\le\log_{10}\gamma_0.}
\tag{c3-rough-pay}

这一步很重要：sphere要求的 `c_3` height不能偷偷塞回 2/5 smooth baseline，
只能由真正的 non-decimal overlap `gamma_0` 支付。

---

## 4. Final-5 中 `L` 的 exact leading height

记

\[
q_5=v_5(Q),
\quad g_5=v_5(G),
\quad n_5=v_5(\mathcal N_{12}),
\quad B_5=v_5(b_3).
\]

`Final-5-lock` 为

\[
\boxed{
B_5=q_5+2g_5,}
\tag{4.1}

\[
\boxed{
m=2q_5+4g_5+n_5.}
\tag{4.2}

又

\[
L=10^m/(10^m,b_3).
\]

在 2 处 `v_2(L)=ell in {0,1}`，故其 normalized contribution为 `o(S)`。
在 5 处，由 `(4.1)`、`(4.2)`：

\[
\begin{aligned}
v_5(L)
&=m-B_5\\
&=q_5+2g_5+n_5\\
&=\boxed{\frac{m+n_5}{2}}.
\end{aligned}
\tag{4.3}

因此若

\[
M=m/S,
\qquad N_5=n_5/S,
\qquad b=\log_{10}5,
\]

则

\[
\boxed{
\frac{\log_{10}L}{S}
=\frac b2(M+N_5)+o(1).}
\tag{L-height}

---

## 5. sphere payer转成 slope inequality

记

\[
\mathcal N:=\limsup\frac nS,
\qquad
R:=\limsup\frac{\log_{10}\gamma_0}{S}.
\]

沿实现 limsup 的子序列使用 `(c3-height-lower)`、`(c3-rough-pay)` 与
`(L-height)`：

\[
\boxed{
\mathcal N
\le
2+2M-rac b2(M+N_5)+R.}
\tag{Sphere-Final5}

这是本文第一条新的 asymptotic height inequality。

---

## 6. 与 `Subspace-Final5` 精确合并

`high-funnel-two-adic-balance.md` 已经严格得到

\[
\boxed{
(1+a)M+2aQ_2+aN_2+2R\le3,}
\tag{Subspace-Final5}

其中

\[
a=\log_{10}2,
\qquad b=1-a,
\]

\[
Q_2=\mathfrak q/S,
\qquad
N_2=\mathfrak n/S.
\]

因此

\[
R\le
\frac{3-(1+a)M-2aQ_2-aN_2}{2}.
\]

代入 `(Sphere-Final5)`：

\[
\begin{aligned}
\mathcal N
\le{}&
2+2M-rac b2(M+N_5)\\
&+\frac{3-(1+a)M-2aQ_2-aN_2}{2}.
\end{aligned}
\]

因为 `b=1-a`，M coefficient精确化简：

\[
2-\frac b2-\frac{1+a}{2}=1.
\]

所以

\[
\boxed{
\mathcal N
\le
\frac72+M
-aQ_2-rac a2N_2-rac b2N_5.}
\tag{Final5-collapse-defect}

特别地

\[
\boxed{
\mathcal N\le\frac72+M.}
\tag{6.1}

而 `Subspace-Final5` 丢掉非负 defects给

\[
\boxed{M\le\frac3{1+a}.}
\tag{6.2}

最终：

\[
\boxed{
\mathcal N
\le
\frac72+\frac3{1+a}.}
\tag{Final5-bound}

数值为

\[
\boxed{
\frac72+\frac3{1+\log_{10}2}
=5.805865360520\ldots.}
\]

---

## 7. 对 `Final-5` branch tree 的含义

`high-funnel-defect-optimization.md` 已把 Tail-short sector压到

\[
\boxed{
\limsup n/S\le6.215109404735\ldots.}
\]

随后 `high-funnel-xi-depth.md`、`high-funnel-denominator-max-lock.md` 只在
企图保持更高 slope的剩余 `Defect-heavy` 中继续分析，并最终压到
`Final-5`。

现在 `(Final5-bound)` 却给

\[
5.805865360520\ldots
<6.215109404735\ldots.
\]

所以：

\[
\boxed{
\text{不存在任何无界 sequence 既进入 Final-5，
又保持 slope }>6.215109404735\ldots.}
\tag{Final5-high-empty}

因此原 high-funnel branch tree中：

- Tail-short：`<=6.215109...`；
- `B_5>=m` defect-heavy：`<=6`；
- `b_3` 非 5-adic maximum：`<=6`；
- Final-5：本文 `<=5.805865...`。

故 canonical `t_2=1` double-resonant sector整体得到

\[
\boxed{
\limsup\frac nS
\le6.215109404735\ldots.}
\tag{Canonical-6215}

这个显式 sector bound目前由 Tail-short控制。

---

## 8. 对旧 `25/4` 文件的状态更新

`high-funnel-final5-two-adic-optimization.md` 的

\[
2\text{-short}\le6.137703...,
\qquad
2\text{-balanced}\le6.25
\]

仍是严格的 conditional inequalities；但它们已被本文更强的
`Final5-bound` 统一覆盖。

`high-funnel-625-rigidity.md` 描述的 `25/4` equality ray因此成为一个
**已被更强 sphere–c3 payer排除的假想中间 terminal geometry**。其结构恒等式仍可保留作为审计记录，但不得再列为开放 frontier。

---

## 9. 状态摘要

- **`已严格完成（Final-5 sector）`**：`Sphere-c3`、`c3|gamma0`、
  `Sphere-Final5`、`Final5-collapse-defect`。
- **`已严格完成（显式 sector bound）`**：
  \[
  \limsup_{\rm Final\text{-}5}n/S
  \le5.805865360520\ldots.
  \]
- **`已严格完成（canonical funnel）`**：当前 branch tree合并后
  \[
  \limsup_{\rm canonical\ t_2=1\ double\text{-}resonant}n/S
  \le6.215109404735\ldots.
  \]
- **`失效/降级`**：把 `25/4` equality ray继续当作开放 terminal target。
- **`待证`**：把其他 DD states量化到同一显式常数以下，或给出更强的全 DD
  numerical limsup / absolute-height contradiction。

---

<a id="source-high-funnel-final5-two-adic-optimization"></a>

> 整合来源：`high-funnel-final5-two-adic-optimization.md`

# DD `Final-5` 的 `Z`-enhanced stability 与二进两格优化

> **依赖：** [`high-funnel-fminus-sunit-factorization.md`](high-funnel-ledger.md#source-high-funnel-fminus-sunit-factorization)、
> [`high-funnel-defect-optimization.md`](high-funnel-ledger.md#source-high-funnel-defect-optimization)、
> [`high-funnel-denominator-max-lock.md`](high-funnel-ledger.md#source-high-funnel-denominator-max-lock)、
> [`high-funnel-two-adic-balance.md`](high-funnel-ledger.md#source-high-funnel-two-adic-balance)。
>
> **严格状态：** `已严格完成（canonical t_2=1 double-resonant sector）`。
>
> 本文把 exact factorization
> \[
> F_-=2^{H+1}Z(H_{\rm sph}-y_3)\widehat g
> \]
> 中旧 smooth-valuation proof 丢掉的 rough factor `Z` 保留下来，得到
> `Z`-enhanced defect stability。与 `Final-5-lock` 和二进
> `2-short / 2-balanced` 二分联立后：
>
> \[
> \boxed{
> \text{2-short:}\quad
> \limsup\frac nS
> \le
> \frac{5(5+11\log_{10}2)}
> {4(1+\log_{10}2)^2}
> =6.137703685012\ldots}
> \]
>
> \[
> \boxed{
> \text{2-balanced:}\quad
> \limsup\frac nS\le\frac{25}{4}=6.25.}
> \]
>
> 因而整个 `Final-5` sheet满足
> \[
> \boxed{
> \limsup_{\rm Final\text{-}5}\frac nS\le6.25.}
> \]
>
> 结合此前 Tail-short `<=6.215109...`、5-adic/non-max branches `<=6`，
> canonical `t_2=1` double-resonant sector整体得到显式 `<=6.25`。
> **这不是全 DD bound**：旧 funnel 的结构入口有自己的作用域；本文不把 sector
> 结论外推到其他 DD states。

---

## 1. normalized variables

令

\[
a:=\log_{10}2,
\qquad
b:=\log_{10}5=1-a.
\]

沿无界 sequence 取 normalized limsup variables：

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
G_2:=\frac{\mathfrak g}{S},
\qquad
N_2:=\frac{\mathfrak n}{S}.
\]

写

\[
\gamma
=2^{\mathfrak g}5^{g_5}\gamma_0,
\qquad
(\gamma_0,10)=1,
\]

并记 rough overlap height

\[
\boxed{R:=\limsup\frac{\log_{10}\gamma_0}{S}\ge0.}
\tag{1.1}

总 slope记为

\[
\boxed{\mathcal N:=\limsup\frac nS.}
\]

以下所有 `<=` 均是沿 subsequence 去掉 `O(1/S)` 后的 asymptotic inequality。

---

## 2. exact factorization把旧 smooth lower加强一个 `log Z`

`high-funnel-fminus-sunit-factorization.md` 已证明

\[
\boxed{
F_-
=2^{H+1}Z(H_{\rm sph}-y_3)\widehat g,
\qquad
\widehat g=\gamma/c_3.}
\tag{2.1}

在当前 canonical funnel：

- `b_3` 是二进 unique maximum，所以 `c_3=q_lcm/b_3` 是 2-unit；
- `Final-5` 中 `b_3` 是 5-adic maximum，所以 `c_3` 是 5-unit；
- `v_2(H_sph-y_3)=1`；
- `v_5(H_sph-y_3)=T`；
- `v_2(gamma)=mathfrak g`、`v_5(gamma)=g_5`。

因此

\[
v_2(\widehat g)=\mathfrak g,
\qquad
v_5(\widehat g)=g_5.
\]

而 `t_2=1` 给

\[
v_2(\kappa+2G)=\mathfrak f=\mathfrak g+H+1,
\]

`Final-5` 给

\[
k_5=T+g_5.
\]

所以 `(2.1)` 直接给比旧 local valuation lower更强的整除：

\[
\boxed{
2^{\mathfrak f+1}5^{k_5}Z\mid F_-.}
\tag{2.2}

于是

\[
\boxed{
\log_{10}F_-
\ge
 a(\mathfrak f+1)+bk_5+\log_{10}Z.}
\tag{Z-smooth-lower}

`high-funnel-defect-optimization.md` 的旧推导从
`a(f+1)+bk_5` 出发。逐行保留新增的 `+log Z`，其余 algebra不变，得到

\[
\boxed{
\begin{aligned}
\mathcal N
\le{}&6+\frac{2b}{3}M
-2aQ_2-aN_2\\
&-\frac{2b}{3}(2Q_5+G_5+N_5)
-Z_* ,
\end{aligned}}
\tag{Z-defect-stability}

其中

\[
Z_*:=\liminf\frac{\log_{10}Z}{S}.
\]

这就是旧 defect stability 在 `Final-5` 上新增的一份 genuine rough `Z` charge。

---

## 3. 用 S-unit pinning消去 `Z_*`

`t_2=1` phase有

\[
\kappa+2G=2\gamma\,2^HZ.
\]

又由 decimal pinning `Q^2/11<kappa<10Q^2` 与 `Q/G` 的常数窗口：

\[
\log_{10}(\kappa+2G)=2S+O(1).
\]

二进 resonance给

\[
\frac HS
=2M+2Q_2+N_2-2G_2+o(1).
\tag{3.1}

而

\[
\frac{\log_{10}\gamma}{S}
=aG_2+bG_5+R+o(1).
\]

所以

\[
\boxed{
Z_*
=2-a(2M+2Q_2+N_2-2G_2)
-aG_2-bG_5-R.}
\tag{3.2}

把 `(3.2)` 代回 `(Z-defect-stability)`，`Q_2,N_2` 精确消去，得到

\[
\mathcal N
\le
4+\left(2a+\frac{2b}{3}\right)M
-aG_2+bG_5+R
-\frac{2b}{3}(2Q_5+G_5+N_5).
\tag{3.3}

`Final-5-lock` 为

\[
\boxed{M=2Q_5+4G_5+N_5.}
\tag{Final5-M}

消去 `G_5` 后：

\[
\boxed{
\mathcal N
\le
4+\frac{5a+3}{4}M
-aG_2+R
-\frac{3b}{2}Q_5
-\frac{3b}{4}N_5.}
\tag{Final5-Zstab}

特别地丢掉最后两个非正项仍有安全弱化

\[
\boxed{
\mathcal N
\le
4+\frac{5a+3}{4}M-aG_2+R.}
\tag{3.4}

---

## 4. Schmidt budget

`high-funnel-two-adic-balance.md` 已在 `Final-5` 上严格恢复

\[
\boxed{
(1+a)M+2aQ_2+aN_2+2R\le3.}
\tag{Subspace-Final5}

因此特别地

\[
\boxed{M\le\frac3{1+a}.}
\tag{Mmax}

这个 bound 与旧 extremal `M=2.8088...` 不同；它是当前 `Final-5`
新 sheet上的 defect-aware budget。

---

## 5. `2-short`：凸组合消去 `G_2`

`2-short` exact branch为

\[
d\le m+2\mathfrak q+\mathfrak n+\mathfrak g+O(1),
\]

所以 normalized：

\[
\boxed{
\mathcal N
\le2M+2Q_2+N_2+G_2.}
\tag{2-short-N}

取 `(3.4)` 的权

\[
\frac1{1+a}
\]

与 `(2-short-N)` 的权

\[
\frac a{1+a}.
\]

两式右端的 `G_2` coefficient恰好抵消：

\[
-\frac{a}{1+a}G_2
+\frac{a}{1+a}G_2=0.
\]

得到

\[
\begin{aligned}
\mathcal N
\le{}&
\frac4{1+a}
+\frac{13a+3}{4(1+a)}M\\
&+\frac{2aQ_2+aN_2+R}{1+a}.
\end{aligned}
\tag{5.1}

而 `(Subspace-Final5)` 给

\[
2aQ_2+aN_2+R
\le3-(1+a)M,
\]

因为 `R>=0` 且原式有 `2R`。所以

\[
\boxed{
\mathcal N
\le
\frac7{1+a}
+\frac{9a-1}{4(1+a)}M.}
\tag{5.2}

注意

\[
9a-1>0
\]

（甚至 `a>1/9` 已足够）。故用 `(Mmax)`：

\[
\begin{aligned}
\mathcal N
&\le
\frac7{1+a}
+\frac{3(9a-1)}{4(1+a)^2}\\
&=
\boxed{
\frac{5(5+11a)}{4(1+a)^2}}.
\end{aligned}
\tag{2-short-bound}

数值为

\[
\boxed{
\mathcal N
\le6.137703685012\ldots.}
\]

这比此前 Tail-short sector 的 `6.215109...` 还低。

---

## 6. `2-balanced`：直接代入 Schmidt budget

`2-balanced` exact equality为

\[
2\mathfrak g=m+\mathfrak q+\ell-2,
\]

其中 `ell in {0,1}`。归一化后

\[
\boxed{2G_2=M+Q_2.}
\tag{6.1}

把 `(6.1)` 代入完整 `(Final5-Zstab)`：

\[
\begin{aligned}
\mathcal N
\le{}&
4+\frac{3(1+a)}4M
-\frac a2Q_2+R\\
&-\frac{3b}{2}Q_5
-\frac{3b}{4}N_5.
\end{aligned}
\tag{6.2}

由 `(Subspace-Final5)`：

\[
R
\le
\frac{3-(1+a)M-2aQ_2-aN_2}{2}.
\]

代入 `(6.2)`：

\[
\boxed{
\begin{aligned}
\mathcal N
\le{}&
\frac{11}{2}+\frac{1+a}{4}M
-\frac{3a}{2}Q_2-\frac a2N_2\\
&-\frac{3b}{2}Q_5-\frac{3b}{4}N_5.
\end{aligned}}
\tag{6.3}

丢掉所有非正 defect项，再用 `(Mmax)`：

\[
\boxed{
\mathcal N
\le
\frac{11}{2}+\frac34
=\frac{25}{4}=6.25.}
\tag{2-balanced-bound}

该常数是 exact rational number，不是数值 LP 猜测。

---

## 7. `Final-5` 与 canonical funnel 的新 sector bound

`high-funnel-two-adic-balance.md` 已证明 `2-short / 2-balanced` 穷尽
当前 canonical `Final-5` sheet。因此

\[
\boxed{
\limsup_{\rm Final\text{-}5}\frac nS
\le\max(6.137703685012\ldots,6.25)
=6.25.}
\tag{Final5-625}

再回到此前 5-adic branch tree：

- Tail-short：
  \[
  \limsup n/S\le6.215109404735\ldots;
  \]
- defect-heavy 且 `B_5>=m`：`<=6`；
- `b_3` 非 5-adic maximum：`<=6`；
- 剩余 `Final-5`：本文 `<=6.25`。

所以在这些 structural hypotheses 定义的 canonical `t_2=1`
double-resonant sector中：

\[
\boxed{
\limsup\frac nS\le6.25.}
\tag{Canonical-sector-625}

**作用域再次强调：**最早把 arbitrary high candidate压入该 canonical funnel的
分类有自己的 slope/sector前提。`(Canonical-sector-625)` 是对该 algebraic sector
的显式改进，不是对所有 DD states 的无条件 `limsup<=6.25`。

---

## 8. 状态摘要

- **`已严格完成（sector）`**：`Z-defect-stability`、`Final5-Zstab`。
- **`已严格完成（sector）`**：`2-short <= 6.137703685012...` 的闭式凸组合证书。
- **`已严格完成（sector）`**：`2-balanced <= 25/4`。
- **`已严格完成（sector）`**：`Final-5 <= 6.25`，canonical `t_2=1`
  double-resonant sector `<=6.25`。
- **`待证`**：把其他 DD states统一降到同一显式常数以下，或直接给 DD
  absolute height / emptiness；不能把本文件的 sector bound外推成全局结论。

---

<a id="source-high-funnel-five-adic-dichotomy"></a>

> 整合来源：`high-funnel-five-adic-dichotomy.md`

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

---

<a id="source-high-funnel-fminus-sunit-factorization"></a>

> 整合来源：`high-funnel-fminus-sunit-factorization.md`

# DD `t_2=1` 的 exact `F_-` S-unit factorization

> **依赖：** `core.md` §§31–38 的 denominator overlap / primitive determinant ladder /
> overlap parameterization，以及 `core.md` §11 的 `t_2=1` S-unit phase；
> [`high-funnel-denominator-max-lock.md`](high-funnel-ledger.md#source-high-funnel-denominator-max-lock) 仅用于
>最后的 `Final-5` 推论。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
>
> `core.md` §35.1 已经明确警告：不能把 `g_*` 当作一份独立的额外高度惩罚。
>本文不这样做；而是把 `g_*` 与 overlap parameterization **精确消去**。得到
>
> \[
> \boxed{
> F_-
> =2^{H+1}Z\,(H_{\rm sph}-y_3)\,\widehat g,
> \qquad
> \widehat g:=\frac{g_*}{V}\in\mathbf Z_{>0}.}
> \]
>
> 在 `Final-5-lock`
> \[
> v_5(H_{\rm sph}-y_3)=T
> \]
> 上立即得到无 `gcd(q,Z)` loss 的整除：
> \[
> \boxed{2^{H+1}5^TZ\mid F_-.}
> \]
>
> 这是一条严格新接口，但单独与粗 `F_-` 上界联立只给约 `6.805865...`
> 的 conditional sector bound；本文明确不把它误报为新的全 DD slope。

---

## 1. 已有 exact small-factor factorization

`core.md` §35 已有

\[
\boxed{
F_-
=a\,g_*
\frac{L(LQ+2\tau)}{\tau}.}
\tag{1.1}

其中 sphere gap 为

\[
\boxed{H_{\rm sph}-y_3=La.}
\tag{1.2}

`core.md` §35.1 的修正指出：不能从 `(1.1)` 中把 `g_*` 直接再当成
一份 independent height，因为 `(H_sph-y_3)g_*` 与 denominator overlap存在
exact cancellation。本文后续只做代数恒等变换，不作这种重复收费。

---

## 2. overlap parameterization 精确抽掉 `V`

`core.md` §37 定义

\[
\eta=(Q,\tau),
\qquad Q=\eta Q_1,
\qquad \tau=\eta v,
\]

\[
u=LQ_1,
\qquad (u,v)=1.
\]

继续有

\[
\boxed{g_*=vc\lambda r.}
\tag{2.1}

因此

\[
\boxed{
\widehat g:=\frac{g_*}{v}=c\lambda r\in\mathbf Z_{>0}.}
\tag{2.2}

把 `(2.1)` 代回 `(1.1)`：

\[
\begin{aligned}
F_-
&=a(vc\lambda r)
\frac{L\,\eta(LQ_1+2v)}{\eta v}\\
&=a(c\lambda r)L(LQ_1+2v).
\end{aligned}
\]

所以一般 overlap-normalized form为

\[
\boxed{
F_-=a\widehat g L(u+2v).}
\tag{2.3}

利用 `(1.2)`：

\[
\boxed{
F_-=(H_{\rm sph}-y_3)\widehat g\,(u+2v).}
\tag{2.4}

这是 §35.1 所要求的正确 normalized use：`v` 已经从 `g_*` 与
`tau` 中 exact cancel，不会被再计一次。

---

## 3. 进入 `t_2=1` S-unit phase

canonical `t_2=1` funnel写成

\[
\boxed{
u=2\cdot5^TU,
\qquad v=V,}
\tag{3.1}

以及

\[
\boxed{5^TU+V=2^HZ,}
\qquad (UVZ,10)=1.
\tag{3.2}

于是

\[
\begin{aligned}
u+2v
&=2\cdot5^TU+2V\\
&=2(5^TU+V)\\
&=\boxed{2^{H+1}Z}.
\end{aligned}
\tag{3.3}

而 `(2.1)` 此时给

\[
\boxed{V\mid g_*,
\qquad
\widehat g=\frac{g_*}{V}.}
\tag{3.4}

将 `(3.3)` 代入 `(2.4)`：

\[
\boxed{
F_-
=2^{H+1}Z\,(H_{\rm sph}-y_3)\widehat g.}
\tag{Fminus-Sunit}

这是本文主恒等式。

---

## 4. `widehat g` 与 `gamma/c_3`

`core.md` §37 还给出

\[
c_3=\varepsilon c,
\]

\[
\boxed{G=\varepsilon vc^2\lambda r.}
\tag{4.1}

另一方面 gcd-normal form为

\[
G=\gamma v.
\tag{4.2}

比较 `(4.1)`、`(4.2)`：

\[
\boxed{
\gamma=\varepsilon c^2\lambda r.}
\tag{4.3}

而

\[
\widehat g=c\lambda r.
\]

因此

\[
\boxed{
\widehat g=\frac\gamma{\varepsilon c}
=\frac\gamma{c_3}.}
\tag{4.4}

这与早期恒等式

\[
g_*=G/c_3
\]

完全一致，因为 `G=gamma V`。

所以 `(Fminus-Sunit)` 也可以写成

\[
\boxed{
F_-
=2^{H+1}Z\,(H_{\rm sph}-y_3)\frac\gamma{c_3}.}
\tag{4.5}

但后续高度估计若使用 `(4.5)`，必须把 `gamma/c_3` 作为一个整体；
不能把 `gamma` 单独视作额外独立收益。

---

## 5. Final-5 的无损 smooth/S-unit divisor

`high-funnel-denominator-max-lock.md` 已严格证明 remaining `Final-5` sheet满足

\[
\boxed{v_5(H_{\rm sph}-y_3)=T.}
\tag{5.1}

因此

\[
5^T\mid H_{\rm sph}-y_3.
\]

由 `(Fminus-Sunit)` 且 `widehat g` 为正整数：

\[
\boxed{
2^{H+1}5^TZ\mid F_-.}
\tag{Final5-Fdiv}

注意该整除式完全不含

\[
(q,Z),
\]

所以它比从一般 large-divisor

\[
u(u+2v)\mid F_-Q
\]

再约 `Q=Uq` 得到的 `L_Z|F_-` 更直接；后者的 `q-Z` gcd loss在
`Final-5` 的此条 exact factorization中并不存在。

这**不使** `high-funnel-qz-*` 文件失效：那些文件仍给整个 canonical funnel的
rough-factor allocation和 two-sheet structure；这里只说明在 `Final-5` 的
`F_-` 高度问题上有一条更强的专用 divisor。

---

## 6. 直接高度下界

记

\[
a_2:=\log_{10}2,
\qquad a_5:=\log_{10}5.
\]

由 `(Final5-Fdiv)`：

\[
\boxed{
\log_{10}F_-
\ge
(H+1)a_2+Ta_5+\log_{10}Z.}
\tag{6.1}

S-unit phase `(3.2)` 还给

\[
H a_2+\log_{10}Z
=
Ta_5+\log_{10}U
+\log_{10}\left(1+\frac{V}{5^TU}\right).
\tag{6.2}

而 tail window中

\[
\frac1{5Q}\le\frac{V}{5^TU}<\frac2Q,
\]

所以最后一项是 `O(10^{-S})`，特别是 `O(1)`。因此

\[
\boxed{
\log_{10}F_-
\ge
2Ta_5+\log_{10}U+O(1).}
\tag{6.3}

也可用

\[
\kappa=2\gamma5^TU,
\qquad
Q^2/11<\kappa<10Q^2,
\]

以及 `Q` 为 S-digit denominator concat得到

\[
Ta_5+\log_{10}U+\log_{10}\gamma
=2S+O(1),
\]

故

\[
\boxed{
\log_{10}F_-
\ge
2S+Ta_5-\log_{10}\gamma+O(1).}
\tag{6.4}

`(6.4)` 只是 `(6.1)` 的另一种 bookkeeping；不能把 `-log gamma` 与
`widehat g=gamma/c_3` 再独立收费，否则会重复计算 overlap。

---

## 7. 与粗 `F_-` 上界单独联立的边界

`high-funnel-defect-optimization.md` 的通用 d-dominant small-factor上界为

\[
\boxed{
\log_{10}F_-
<4S+2m-n+O(1).}
\tag{7.1}

单独将 `(6.1)` / `(6.4)` 与 `(7.1)` 联立，并加入 Final-5、2-adic resonance、
Schmidt `log U+log Z>=S-o(S)` 等已知线性约束，得到的 relaxed LP optimum仍约为

\[
\boxed{6.805865\ldots}
\]

（机械脚本记录该数值诊断）。它高于已有全局非有效 strict bound

\[
\limsup n/S<6.308883577618\ldots.
\]

因此：

\[
\boxed{
\text{`Final5-Fdiv` 是严格新结构，但不能单独宣称新的全局 slope。}}
\]

真正有价值的下一步是回到产生 `c_*=7.745178...` 与 Schmidt
`6.308883...` 的完整 stability inequality，在其中保留 `(Fminus-Sunit)` 所暴露的
S-unit / gap项，而不是继续使用 `(7.1)` 的粗 upper/lower pair。

---

## 8. 状态摘要

- **`已严格完成`**：`Fminus-Sunit`、`widehat g=g_*/V=gamma/c_3`、
  `Final5-Fdiv`。
- **`审计完成`**：使用 normalized `widehat g` 不违反 `core.md` §35.1；
  裸 `g_*` 仍不得作为 independent height重复收费。
- **`结构结论`**：Final-5 的 `F_-` height不需要先控制 `gcd(q,Z)`。
- **`待证`**：把 exact factorization嵌回完整 stability derivation，恢复显式更强
  defect inequality；新的 effective global slope或 DD 空性。

---

<a id="source-high-funnel-gap-depth"></a>

> 整合来源：`high-funnel-gap-depth.md`

# DD high-funnel `Defect-heavy` = sphere-gap extra 5-depth

> **依赖：** [`high-funnel-xi-depth.md`](high-funnel-ledger.md#source-high-funnel-xi-depth)、`core.md` §§17–18 的 gap normalization、high-funnel tail weight与 5-resonance。
>
> **严格状态：** `已严格完成（remaining high-funnel）`。上一文件证明，在仍可能承载 slope `>6.215109...` 的 `B_5<m` defect-heavy branch 中
> \[
> 3v_5(\Xi)=5q_5+4g_5+n_5-m.
> \]
> 本文恢复 DD §18 中 `Xi=|mathcal M-C_0a|` 的显式 quadratic coefficient
> \[
> C_0=QL+2\tau,
> \]
> 并证明该 `C_0` 在当前 5-adic funnel上是 unit，而 `mathcal M` 自动含 `5^d`。由于 remaining non-Tail-short branch满足 `v_5(Xi)<d`，得到
> \[
> \boxed{v_5(a)=v_5(\Xi)}.
> \]
> 因此最后 defect slack精确等于 sphere gap `H-y_3=La` 中 `a` 承担的额外 5-depth。

---

## 1. 恢复 §18 的 quadratic coefficient `C_0`

DD §17 有

\[
\mathcal G=\mathcal M-QH,
\qquad Q=A+B,
\]

以及

\[
\mathcal G=\tau a,
\qquad
H=\frac12\left(La+\frac{\mathcal S_{12}}{La}\right).
\]

代入：

\[
\mathcal M
-\frac Q2\left(La+\frac{\mathcal S_{12}}{La}\right)
=\tau a.
\]

乘 `2La` 并除以 `L`：

\[
\boxed{
(QL+2\tau)a^2
-2\mathcal M a
+Q\frac{\mathcal S_{12}}L
=0.
}
\tag{1.1}

因为 `La|mathcal S_12`，最后一项为整数。

定义

\[
\boxed{C_0:=QL+2\tau.}
\tag{C0}

对实际根 `a`，二次式的 half-discriminant满足

\[
\begin{aligned}
\mathcal M^2-C_0Q\frac{\mathcal S_{12}}L
&=(\mathcal M-C_0a)^2.
\end{aligned}
\]

所以 §18 的

\[
\Xi=|\mathcal M-C_0a|
\]

正好对应 `(C0)`；这里没有未定义自由 coefficient。

---

## 2. `C_0` 可用 tail weight完全化简

exact tail weight为

\[
\boxed{\kappa\tau=LQG.}
\tag{2.1}

因此

\[
\begin{aligned}
C_0
&=QL+2\tau\\
&=LQ\left(1+\frac{2G}{\kappa}\right)\\
&=\boxed{
LQ\frac{\kappa+2G}{\kappa}}.
\end{aligned}
\tag{2.2}

当前 high funnel满足

\[
k_5:=v_5(\kappa)>g_5:=v_5(G),
\]

故

\[
v_5(\kappa+2G)=g_5.
\]

又在 remaining branch

\[
B_5:=v_5(b_3)<m,
\]

所以

\[
v_5(L)=m-B_5.
\]

因此

\[
\begin{aligned}
v_5(C_0)
&=(m-B_5)+q_5+g_5-k_5.
\end{aligned}
\]

而 tail weight valuation给

\[
k_5=m+q_5+g_5-B_5.
\]

故精确得到

\[
\boxed{v_5(C_0)=0.}
\tag{C0-unit}

---

## 3. `mathcal M` 自动含完整 decimal `5^d`

DD §17 定义

\[
\mathcal M
=10^{k_{12}}Ay_1+10^dBy_2,
\]

其中

\[
A=10^{m_2}b_1,
\qquad
B=b_2,
\qquad
k_{12}=s_2+d.
\]

由于

\[
s_2+m_2=n_2,
\]

第一 coefficient 为

\[
10^{k_{12}}A
=10^{s_2+d+m_2}b_1
=10^{n_2+d}b_1.
\]

所以

\[
\boxed{
\mathcal M
=10^d\left(10^{n_2}b_1y_1+b_2y_2\right).
}
\tag{M-decimal}

特别地

\[
\boxed{v_5(\mathcal M)\ge d.}
\tag{M5}

---

## 4. remaining high slope保证 `v_5(Xi)<d`

上一文件记

\[
x:=v_5(\Xi)
=2q_5+2g_5-B_5.
\tag{4.1}

而 `high-funnel-five-adic-dichotomy.md` 中

\[
r:=v_5(\mathscr T)
=m+2q_5+3g_5-2B_5.
\tag{4.2}

两者之差为

\[
\boxed{r-x=m+g_5-B_5>0}
\tag{4.3}

因为 `B_5<m`。

`high-funnel-defect-optimization.md` 已经把 `Tail-short` branch压到

\[
\limsup n/S\le6.215109404735\ldots.
\]

所以只研究任何假想满足更高 slope 的 remaining sequence。它不能满足 Tail-short inequality `d<=r`；eventually 必有

\[
\boxed{d>r.}
\tag{4.4}

结合 `(4.3)`：

\[
\boxed{x<r<d.}
\tag{4.5}

---

## 5. `Xi` depth 就是 `a` depth

由定义

\[
\Xi=|\mathcal M-C_0a|.
\]

现在：

\[
v_5(\mathcal M)\ge d>x,
\]

而 `(C0-unit)` 给

\[
v_5(C_0)=0.
\]

若 `v_5(a)\ne x`，两项 valuation不同，则差的 valuation等于较小者；结合第一项深度 `>x`，唯一可能是

\[
v_5(a)=x.
\]

更直接地模 `5^{x+1}` 观察即可。因此

\[
\boxed{v_5(a)=v_5(\Xi).}
\tag{Gap-Xi}

使用 `high-funnel-xi-depth.md`：

\[
\boxed{
3v_5(a)
=5q_5+4g_5+n_5-m.
}
\tag{Gap-slack}

---

## 6. sphere gap 的新解释

DD gap normalization为

\[
\boxed{H-y_3=La.}
\tag{6.1}

所以

\[
v_5(H-y_3)
=v_5(L)+v_5(a)
=(m-B_5)+x.
\]

由 `(4.1)`：

\[
\boxed{
v_5(H-y_3)
=m+2q_5+2g_5-2B_5.
}
\tag{Gap5}

而 `(4.2)` 给

\[
\boxed{
v_5(H-y_3)=r-g_5.}
\tag{6.2}

因此 `Defect-heavy` 的额外 slack具有非常具体的几何意义：

- `L` 支付 forced denominator/decimal baseline `m-B_5`；
- `a` 支付额外
  \[
  x=v_5(a)=\frac{5q_5+4g_5+n_5-m}{3};
  \]
- 这正是 sphere gap的 extra 5-depth。

于是高 slope最后未决核已经重新接回仓库已有的 5-adic allocation language：

\[
\boxed{
\text{positive-linear `Defect-heavy`}
\Longleftrightarrow
\text{positive-linear extra 5-depth in the sphere-gap quotient }a.
}

---

## 7. 下一接口

`frontier.md` / projective-angular allocation已经证明：一旦 sphere-gap 5-depth超过 common multiplicative scale，genuine angular part不能再次支付 projective denominator、bottom edge或两条 simultaneous carrier contacts。

本文因此把下一任务固定为：

1. 将 `v_5(a)` 与 `s_5=min(v_5(H),v_5(y_3))`、`r_5=v_5((y_1,y_2))` 做 exact common-scale / angular 分解；
2. 若 `v_5(a)` 主要是 angular，调用现有 no-double-pay 迫使矛盾；
3. 若主要是 common scale，则把该 scale送回 denominator prime-flow，争取由 reducedness / prefix height收费。

---

## 8. 状态摘要

- **`已严格完成`**：`C0=QL+2tau`、`C0-unit`、`M-decimal`、`Gap-Xi`、`Gap-slack`、`Gap5`。
- **`结构压缩`**：remaining high-funnel defect-heavy slack = extra 5-depth of sphere-gap quotient `a`.
- **`待证`**：common-scale vs angular allocation of `v_5(a)`；new global numerical limsup；DD global closure。

---

<a id="source-high-funnel-gap-epsilon-allocation"></a>

> 整合来源：`high-funnel-gap-epsilon-allocation.md`

# DD gap square-core 的 `epsilon / lambda / G_0` support allocation

> **依赖：** [`high-funnel-gap-square-core.md`](high-funnel-ledger.md#source-high-funnel-gap-square-core)、
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

---

<a id="source-high-funnel-gap-square-core"></a>

> 整合来源：`high-funnel-gap-square-core.md`

# DD canonical `t_2=1` funnel 的 gap square-core identity

> **依赖：** [`high-funnel-exact-small-factor-normalization.md`](high-funnel-ledger.md#source-high-funnel-exact-small-factor-normalization)、
> `core.md` 的 `F_-` 定义、overlap 参数化与 `G_0|2G N_12`。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
>
> exact small-factor quotient
> \[
> R=a\frac{g_*}{V}
> \]
> 与
> \[
> F_-=\frac{2(\kappa+2G)\mu^2}{G_0}
> \]
> 可以完全对齐。最终得到
> \[
> \boxed{
> a_0 5^T G_0=s\varepsilon\mu^2,
> \qquad
> s=(2\cdot5^T,q),
> }
> \]
> 其中 `c_3=epsilon c`、`a=ca_0`。
> 因此 `a_0 5^T G_0/(s epsilon)` 是一个**整数完全平方**。

---

## 1. 从 `F_-` 的二次式定义读取同一个 quotient

统一 near-square factors 中

\[
\boxed{
F_-=
\frac{2(\kappa+2G)\mu^2}{G_0}.
}
\tag{1.1}

在 `t_2=1` phase：

\[
\kappa+2G
=\gamma(u+2v)
=2\gamma\,2^HZ.
\]

所以

\[
\boxed{
F_-
=2^{H+2}Z\frac{\gamma\mu^2}{G_0}.
}
\tag{1.2}

另一方面 `high-funnel-exact-small-factor-normalization.md` 已证明

\[
\boxed{
F_-=
\frac{2^{H+2}5^TZ}{s}
\;a\frac{g_*}{V},
\qquad
s=(2\cdot5^T,q).
}
\tag{1.3}

约去共同正因子 `2^{H+2} Z`：

\[
\boxed{
\frac{\gamma\mu^2}{G_0}
=
\frac{5^T}{s}
\;a\frac{g_*}{V}.
}
\tag{1.4}

交叉相乘：

\[
\boxed{
sV\gamma\mu^2
=5^Ta g_*G_0.
}
\tag{1.5}

---

## 2. `gamma` 精确消失

denominator overlap 定义给

\[
\boxed{g_*=G/c_3.}
\tag{2.1}

而 gcd-normal form为

\[
\boxed{G=\gamma V.}
\tag{2.2}

所以

\[
\boxed{
\frac{g_*}{V}=\frac{\gamma}{c_3}.
}
\tag{2.3}

把 `(2.3)` 直接代入 `(1.4)`，约去 `gamma`：

\[
\frac{\mu^2}{G_0}
=
\frac{5^T}{s}\frac{a}{c_3}.
\]

因此标准形式为

\[
\boxed{
5^T a G_0=s c_3\mu^2.
}
\tag{Gap-square-raw}

---

## 3. primitive gap 形式

overlap 参数化还有

\[
\boxed{c_3=\varepsilon c,}
\qquad
\boxed{a=ca_0.}
\tag{3.1}

代入 `(Gap-square-raw)` 并约去 `c>0`：

\[
\boxed{
5^T a_0G_0
=s\varepsilon\mu^2.
}
\tag{Gap-square-core}

于是

\[
\boxed{
\frac{5^Ta_0G_0}{s\varepsilon}
=\mu^2
\in\mathbf Z_{>0}^2.
}
\tag{3.2}

特别地

\[
\boxed{s\varepsilon\mid5^Ta_0G_0.}
\tag{3.3}

并且对任意 prime `p`：

\[
v_p(a_0)+T\mathbf 1_{p=5}+v_p(G_0)
-v_p(s)-v_p(\varepsilon)
\]

必须是非负偶数。

---

## 4. squarefree-support consequence

若 prime `p` 不整除

\[
5s\varepsilon G_0,
\]

则 `(Gap-square-core)` 在 `p` 处给

\[
\boxed{v_p(a_0)=2v_p(\mu),}
\]

所以 `v_p(a_0)` 必为偶数。

因此 `a_0` 的 squarefree kernel没有新的自由 prime support：

\[
\boxed{
\operatorname{rad}(\operatorname{sqfree}(a_0))
\mid
\operatorname{rad}(5s\varepsilon G_0).
}
\tag{Squarefree-support}

这里 `sqfree(a_0)` 表示 `a_0` 的平方自由核；该结论只控制 prime support，
不把它误计成新的线性高度。

---

## 5. pure common-scale specialization

在 `Final-5-lock` 的 pure common mode：

\[
q_5=n_5=0,
\qquad
m=4g_5,
\qquad
T=2g_5.
\]

若同时位于 LP 的 2-adic worst face `mathfrak q=0`，则 source factor `q` 是
10-unit，因此

\[
\boxed{s=1.}
\]

`b_3` 为 5-adic maximum，故 `c_3=q_lcm/b_3` 为 5-unit；于是
`epsilon,c` 均为 5-units。`v_5(a)=0` 给 `a_0` 为 5-unit，而 high-funnel
recovery ledger给

\[
v_5(G_0)=n_5=0,
\qquad
v_5(\mu)=g_5.
\]

因此 `(Gap-square-core)` 除以 `5^{2g_5}` 后得到

\[
\boxed{
 a_0G_0
=\varepsilon
\left(\frac{\mu}{5^{g_5}}\right)^2.
}
\tag{Pure-gap-square}

这比单纯的 5-adic square-class Hensel 更强：它是一个**全局整数 square-core equation**。

---

## 6. 方法边界

`(Gap-square-core)` 本身还没有关闭 pure common-scale branch，因为
`G_0` 与 `epsilon` 可以携带补偿 squarefree support。

但它把下一问题从“继续做更深的 5-adic unit lifting”改写成一个明确的全局
factor-allocation 问题：

1. `G_0|2G N_12`，所以 recovery gcd 的 prime support受前缀 norm控制；
2. `epsilon=(c_3,u+v)`，所以另一份 squarefree support来自 denominator/projective overlap；
3. 除这两个载体外，`a_0` 的所有 prime exponent都必须为偶数。

下一步应研究 `G_0` 与 `epsilon` 的 common/exclusive support，或从
`Pure-gap-square` 构造一个 normalized squarefree divisor并与 digit/sphere
height联立。

---

## 7. 状态摘要

- **`已严格完成`**：`Gap-square-raw`、`Gap-square-core`、squarefree-support。
- **`结构压缩`**：pure common 的 gap quotient被压成 `a_0 G_0 = epsilon * square`。
- **`待证`**：`G_0 / epsilon` 的 squarefree allocation；`Final-5 + 2-short`；
  sector-to-global reoptimization；DD 全局空性。

---

<a id="source-high-funnel-qz-bottom-orientation-correction"></a>

> 整合来源：`high-funnel-qz-bottom-orientation-correction.md`

# DD `q-Z` bottom reader 的 orientation-uniform 修正

> **依赖：** [`high-funnel-qz-two-sheet-split.md`](high-funnel-ledger.md#source-high-funnel-qz-two-sheet-split)、
> [`high-funnel-qz-sheet-reader-collapse.md`](high-funnel-ledger.md#source-high-funnel-qz-sheet-reader-collapse)。
>
> **严格状态：** `已严格完成（技术修正）`。
>
> 前两文件在 complementary-sheet bottom identity 的展示中写了
> `Delta_12/10^d`。该写法只在 `k>=d`（即 `s_2=k-d>=0`）时是整数式。
> DD 中 `k-d` 可以为负，因此 canonical integer reader必须改用
> \[
> h:=\min(k,d),\qquad
> R_{12}:=\Delta_{12}/10^h.
> \]
> 本文给出两种 orientation 的 exact identity，并验证前两文件使用的
> p-adic depth结论、`C_12|bottom-reader` 与 balanced payer theorem 全部保持不变。

---

## 1. bottom determinant

沿用

\[
\Delta_{12}
=a_1 10^k b_2-a_2 10^d b_1,
\]

以及

\[
Q=b_1 10^{m_2}+b_2,
\qquad
A_{12}=a_1 10^{n_2}+a_2.
\]

DD 参数满足

\[
\boxed{k-d=n_2-m_2.}
\tag{1.1}

令

\[
\boxed{h:=\min(k,d),
\qquad R_{12}:=\Delta_{12}/10^h\in\mathbf Z.}
\tag{1.2}

---

## 2. `k>=d` orientation

若

\[
k\ge d,
\qquad t:=k-d=n_2-m_2\ge0,
\]

则

\[
R_{12}=a_1 10^t b_2-a_2b_1.
\]

直接展开：

\[
\begin{aligned}
Qa_1 10^t-b_1A_{12}
&=(b_1 10^{m_2}+b_2)a_1 10^t
-b_1(a_1 10^{m_2+t}+a_2)\\
&=a_1 10^t b_2-a_2b_1.
\end{aligned}
\]

所以

\[
\boxed{
R_{12}=Qa_1 10^{k-d}-b_1A_{12}
\qquad(k\ge d).}
\tag{2.1}

这正是前两文件所使用的 orientation。

---

## 3. `k<d` orientation

若

\[
k<d,
\qquad t:=d-k=m_2-n_2>0,
\]

则

\[
R_{12}=a_1b_2-a_2 10^t b_1.
\]

因为

\[
10^tA_{12}
=a_1 10^{n_2+t}+a_2 10^t
=a_1 10^{m_2}+a_2 10^t,
\]

有

\[
\begin{aligned}
Qa_1-b_1 10^tA_{12}
&=(b_1 10^{m_2}+b_2)a_1
-b_1(a_1 10^{m_2}+a_2 10^t)\\
&=a_1b_2-a_2 10^t b_1.
\end{aligned}
\]

因此

\[
\boxed{
R_{12}=Qa_1-b_1 10^{d-k}A_{12}
\qquad(k<d).}
\tag{3.1}

---

## 4. prefix concat gcd 对两个 orientations 都进入 bottom reader

定义

\[
C_{12}:=(A_{12},Q).
\]

无论 `(2.1)` 还是 `(3.1)`，右边都是 `Q` 的整数倍减去 `A_12` 的整数倍。
所以统一有

\[
\boxed{C_{12}\mid R_{12}.}
\tag{4.1}

特别地，前文件 complementary sheet 上的

\[
D_{\rm comp}\mid C_{12}
\]

仍然推出

\[
\boxed{D_{\rm comp}\mid R_{12}.}
\tag{4.2}

因为所有 `D_ex` primes 都满足 `p\nmid10`，

\[
v_p(R_{12})=v_p(\Delta_{12}).
\]

所以原来的 bottom-depth statement 应理解为

\[
\boxed{
v_p(R_{12})\ge M+e}
\]

或除去 denominator common baseline后

\[
\boxed{v_p(\Theta_{12})\ge e,}
\]

其数值内容完全不变。

---

## 5. gap-sheet 的 Pluecker unit结论也不受 orientation影响

`high-funnel-qz-two-sheet-split.md` 的 gap proof 使用的是 raw determinants

\[
\Delta_{12},\Delta_{13},\Delta_{23}
\]

的 Pluecker identity与 nested carry：

\[
E=10^{m_2}\Delta_{13}+\Delta_{23},
\]

\[
b_1\Delta_{23}-b_2\Delta_{13}+b_3\Delta_{12}=0.
\]

该推导没有除以 `10^d`，因此本来就同时覆盖 `k>=d` 与 `k<d`。
所以

\[
\boxed{
\text{gap sheet}\Longrightarrow
v_p(\Delta_{12})=M
}
\]

以及

\[
v_p(\Theta_{12})=0
\]

无需任何修改。

---

## 6. 对 balanced payer theorem 的影响

balanced payer只使用

\[
D_{\rm comp}\mid C_{12},
\qquad
D_{\rm comp}\mid Z_0,
\]

以及

\[
D_{\rm gap}^2\mid a.
\]

这些结论均与 `k-d` 的符号无关。因此

\[
\boxed{
D_{qZ}^2\mid\gamma\,a\,C_{12}\,Z_0
}
\]

保持严格成立。

同理使用 bottom reader 的版本应写成

\[
\boxed{
D_{qZ}^2
\mid
\gamma\,a\,C_{12}\,|R_{12}|_{\rm nd},
}
\]

其中在 `D_ex` 的 non-decimal support上，`R_12` 与此前的 raw/decimal-normalized
bottom determinant具有相同 p-adic depth；如果继续使用 `Theta_12`，则仍按
\[
\Theta_{12}=\Delta_{12}/(b_1,b_2)
\]
读取 denominator baseline 后的 excess。

---

## 7. 状态摘要

- **修正：**不能全局把 bottom integer reader写成 `Delta_12/10^d`；canonical
  reader是 `Delta_12/10^{min(k,d)}`。
- **保持不变：**two-sheet split、gap bottom-unit、complementary bottom-excess、
  `D_comp|(A_12,Q)`、balanced payer theorem。
- **后续规范：**凡需要普通整数整除时统一使用 `R_12`；只做 `p\nmid10`
  valuation 时可直接使用 raw `Delta_12`，因为 decimal powers都是 p-units。

---

<a id="source-high-funnel-qz-gcd-allocation"></a>

> 整合来源：`high-funnel-qz-gcd-allocation.md`

# DD high-funnel 的 `q-Z` gcd allocation

> **依赖：** `core.md` 的 gcd-normal form、`t_2=1` S-unit phase、denominator
> prime graph 与 carrier large-divisor identity；
> [`high-funnel-two-adic-balance.md`](high-funnel-ledger.md#source-high-funnel-two-adic-balance) 只作为后续接口。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
> 本文不假设 `gcd(q,Z)=10^{o(S)}`。相反，它把这个 gcd 的每个 prime-power
> 深度精确分配到两个已有 payer：denominator overlap `gamma` 与第三分母相对
> prefix lcm 的 unique-max excess。

---

## 1. 从 `u(u+2v)|F_-Q` 抽出 `Z`-divisor

`core.md` 的 gcd-normal form为

\[
\kappa=\gamma u,
\qquad
G=\gamma v,
\qquad
(u,v)=1,
\]

并已有通用整除

\[
\boxed{u(u+2v)\mid F_-Q.}
\tag{1.1}

在 `t_2=1` S-unit phase：

\[
u=2\cdot5^TU,
\qquad
v=V,
\qquad
Q=Uq,
\]

\[
5^TU+V=2^HZ.
\]

所以

\[
u+2v=2(5^TU+V)=2^{H+1}Z.
\]

又 `(UV,10)=1`、`(U,V)=1`。若某个 odd prime `p|U,Z`，phase equation
模 `p` 会强迫 `p|V`，矛盾；因此

\[
\boxed{(U,2\cdot5Z)=1.}
\tag{1.2}

将 `(1.1)` 写成

\[
2^{H+2}5^T UZ\mid F_-Uq
\]

并用 `(1.2)` 约掉 `U`：

\[
\boxed{
2^{H+2}5^TZ\mid F_-q.
}
\tag{Z-divisor-product}

因此 canonical large divisor

\[
\boxed{
L_Z:=
\frac{2^{H+2}5^TZ}
{\gcd(2^{H+2}5^TZ,q)}
\mid F_-.
}
\tag{LZ}

旧 terminal 工作把 bottleneck指向 `gcd(q,Z)`；`(LZ)` 说明同一个
bottleneck其实已经存在于整个 canonical `t_2=1` funnel。

---

## 2. `q-Z` common prime 自动避开 `U,V`

定义

\[
\boxed{D_{qZ}:=\gcd(q,Z).}
\tag{2.1}

因为 `Z` 为 10-unit，`D_{qZ}` 也是 10-unit。

固定

\[
p\mid D_{qZ},
\qquad p\nmid10.
\]

由 `p|Z` 与 phase equation：

- 若 `p|U`，则 `p|V`，与 `(U,V)=1` 矛盾；
- 若 `p|V`，则 `p|U`，同样矛盾。

所以

\[
\boxed{p\nmid UV.}
\tag{2.2}

因此

\[
v_p(Q)=v_p(q),
\qquad
v_p(G)=v_p(\gamma),
\]

且

\[
v_p(\kappa)=v_p(\gamma),
\]

因为 `u=2*5^T U` 也是 `p`-unit。

---

## 3. denominator valuation ledger

写

\[
e_i:=v_p(b_i),
\qquad
r:=v_p(q)=v_p(Q).
\]

由 tail weight

\[
\kappa b_3=10^mQG
\]

和 §2：

\[
v_p(\gamma)+e_3
=r+v_p(\gamma),
\]

所以

\[
\boxed{e_3=r.}
\tag{3.1}

同时

\[
\boxed{v_p(\gamma)=e_1+e_2.}
\tag{3.2}

令

\[
M:=\max(e_1,e_2),
\qquad
m_0:=\min(e_1,e_2).
\]

由于

\[
Q=b_1 10^{m_2}+b_2,
\qquad p\nmid10,
\]

有标准二项赋值二分：

- 若 `e_1 != e_2`，则
  \[
  r=m_0;
  \]
- 若 `e_1=e_2=M`，则
  \[
  r\ge M,
  \]
  超出的 `r-M` 正是 prefix denominator concat 的额外 `p`-adic cancellation。

---

## 4. 第三分母 unique-max excess

定义

\[
\boxed{
R_3^{\rm den}:=
\frac{b_3}{\gcd(b_3,\operatorname{lcm}(b_1,b_2))}.
}
\tag{4.1}

于是

\[
\boxed{
v_p(R_3^{\rm den})=\max(r-M,0).}
\tag{4.2}

我们现在证明

\[
\boxed{
2r\le v_p(\gamma)+2v_p(R_3^{\rm den}).
}
\tag{4.3}

若 `r<=M`：

- `e_1 != e_2` 时 `r=m_0`，故
  \[
  2r=2m_0\le M+m_0=e_1+e_2=v_p(\gamma);
  \]
- `e_1=e_2=M` 时 `r<=M` 与 `r>=M` 合起来给 `r=M`，于是
  \[
  2r=2M=v_p(\gamma).
  \]

若 `r>M`，则必有 `e_1=e_2=M`，所以

\[
v_p(\gamma)=2M,
\qquad
v_p(R_3^{\rm den})=r-M,
\]

从而

\[
2r=2M+2(r-M)
=v_p(\gamma)+2v_p(R_3^{\rm den}).
\]

因此 `(4.3)` 对所有 `p|D_qZ` 成立。

---

## 5. 全局 gcd allocation

对

\[
s_p:=v_p(D_{qZ})\le r
\]

由 `(4.3)`：

\[
2s_p
\le
v_p(\gamma)+2v_p(R_3^{\rm den}).
\]

逐素数相乘，得到 exact integer divisibility

\[
\boxed{
D_{qZ}^{\,2}
\mid
\gamma\,(R_3^{\rm den})^2.
}
\tag{qZ-allocation}

因此

\[
\boxed{
\log D_{qZ}
\le
\frac12\log\gamma
+
\log R_3^{\rm den}.
}
\tag{5.1}

这不是一个假设的 gcd-smallness，而是一条无条件 payer decomposition。

还可以定义 canonical paid/excess split

\[
D_{\gamma}:=\gcd(D_{qZ}^2,\gamma),
\qquad
D_{3}:=D_{qZ}^2/D_{\gamma}.
\]

则

\[
\boxed{D_3\mid(R_3^{\rm den})^2.}
\tag{5.2}

所以 `q-Z` overlap不能凭空消失：未被 `gamma` 支付的部分只能进入第三
分母 unique-max excess。

---

## 6. third-excess 进入 ghost common scale

令整数球面 ghost common scale

\[
\boxed{g_y:=\gcd(y_1,y_2).}
\]

固定 `p|R_3^{den}`，写

\[
c:=v_p(R_3^{\rm den})=e_3-\max(e_1,e_2)>0.
\]

此时 lcm denominator 的 `p`-depth为 `e_3`，所以

\[
v_p(y_i)=e_3-e_i\ge c
\qquad(i=1,2).
\]

故

\[
\boxed{
\operatorname{core}_{10}(R_3^{\rm den})\mid g_y.
}
\tag{ghost-pay}

这里取 `core_10` 只是为了与 `(qZ-allocation)` 的 non-decimal support
一致；2、5 的 depth另有独立账本。

因此 `(qZ-allocation)` 的第二个 payer并非新自由池，它正是 projective
系统中已经出现的 ghost common scale。

---

## 7. `L_Z` 的 height form

因为 `Z` 是 10-unit，

\[
\gcd(2^{H+2}5^TZ,q)
\mid
2^{\mathfrak q}5^{q_5}D_{qZ}.
\]

所以 `(LZ)` 与 `(5.1)` 给

\[
\boxed{
\begin{aligned}
\log_{10}F_-
\ge{}&aH+bT+\log_{10}Z\\
&-a\mathfrak q-bq_5
-\frac12\log_{10}\gamma
-\log_{10}R_3^{\rm den}
+O(1).
\end{aligned}}
\tag{LZ-height}

这条式子把最后的 `q-Z` loss完全暴露成两个具体 payer：`gamma` 与
`R_3^{den}`。

如果后续证明 `R_3^{den}` 只有 subexponential height，则
`Subspace-defect` 中的 `gamma` 费用会立刻使 `(LZ-height)` 产生新的
线性余量；若 `R_3^{den}` 有正线性高度，则 `(ghost-pay)` 把问题转入
projective common-scale / carrier-tetrahedron branch。

---

## 8. 当前边界

- **`已严格完成`**：`Z-divisor-product`、`L_Z|F_-`、
  `qZ-allocation`、`ghost-pay`、`LZ-height`。
- **`结构压缩`**：`gcd(q,Z)` 的全部高度只能由 denominator overlap
  `gamma` 或 third-exclusive ghost common scale支付。
- **`待证`**：对 `R_3^{den}` / `g_y` 建立 projective carrier收费；把
  `(LZ-height)` 与 `Subspace-defect` 联立成新的 explicit slope，或得到
  absolute-height contradiction。

---

<a id="source-high-funnel-qz-projective-allocation"></a>

> 整合来源：`high-funnel-qz-projective-allocation.md`

# DD `q-Z` gcd 的 projective / gap allocation

> **依赖：** [`high-funnel-qz-gcd-allocation.md`](high-funnel-ledger.md#source-high-funnel-qz-gcd-allocation)
> 与 `core.md` 的 stereographic projective denominator formula。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
> 本文继续消去上一文件中的临时 payer `R_3^{den}`：其 non-decimal
> prime-power 深度必须进一步进入 projective denominator `Z_0` 或 sphere-gap
> quotient `a`。因此 `gcd(q,Z)` 的全部 rough height最终只有三个 payer：
> `gamma`、`Z_0`、`a`。

---

## 1. 已有 denominator allocation

上一文件定义

\[
D_{qZ}=\gcd(q,Z),
\]

\[
R_3^{\rm den}
=
\frac{b_3}{\gcd(b_3,\operatorname{lcm}(b_1,b_2))},
\]

并严格证明

\[
\boxed{
D_{qZ}^2
\mid
\gamma(R_3^{\rm den})^2.
}
\tag{1.1}

同时若

\[
g_y:=\gcd(y_1,y_2),
\]

则

\[
\boxed{
\operatorname{core}_{10}(R_3^{\rm den})\mid g_y.
}
\tag{1.2}

由于 `D_qZ` 本身为 10-unit，后续只需处理 `(R_3^{den})` 的
non-decimal support。

---

## 2. projective denominator 的 exact local formula

把 ghost pair写成

\[
y_1=g_yX,
\qquad
y_2=g_yY,
\qquad
(X,Y)=1.
\]

令

\[
\omega_p:=v_p(X^2+Y^2),
\qquad
r_p:=v_p(g_y),
\]

并记 sphere gap

\[
H_{\rm sph}-y_3=La.
\]

最低项 stereographic denominator满足 `core.md` 的 exact valuation formula

\[
\boxed{
v_p(Z_0)
=
\max(0,r_p+\omega_p-\alpha_p),
}
\tag{2.1}

其中

\[
\alpha_p:=v_p(La).
\]

固定本文关心的 odd non-decimal prime `p`。因为 `L|10^m`，

\[
\boxed{v_p(L)=0,\qquad \alpha_p=v_p(a).}
\tag{2.2}

---

## 3. third-excess 必进 `Z_0` 或 `a`

固定

\[
p^c\Vert\operatorname{core}_{10}(R_3^{\rm den}).
\]

由上一文件的 ghost allocation：

\[
\boxed{r_p\ge c.}
\tag{3.1}

现在分 `(2.1)` 的两种情况。

若

\[
r_p+\omega_p\le v_p(a),
\]

则 `v_p(Z_0)=0`，但

\[
v_p(a)\ge r_p+\omega_p\ge c.
\]

若

\[
r_p+\omega_p>v_p(a),
\]

则

\[
\begin{aligned}
v_p(Z_0)+v_p(a)
&=r_p+\omega_p\\
&\ge r_p\\
&\ge c.
\end{aligned}
\]

所以无论哪种情况都有

\[
\boxed{
c\le v_p(Z_0)+v_p(a).}
\tag{3.2}

逐素数相乘：

\[
\boxed{
\operatorname{core}_{10}(R_3^{\rm den})\mid Z_0a.
}
\tag{R3-projective-pay}

这说明 third denominator unique-max excess并不是第四个独立 rough pool；
它已经被 projective/gap system完全吸收。

---

## 4. `q-Z` gcd 的三 payer theorem

`D_qZ` 为 10-unit，所以 `(1.1)` 中只有 `R_3^{den}` 的 non-decimal part
会参与 `D_qZ` 的 prime exponents。由 `(R3-projective-pay)`：

\[
\boxed{
D_{qZ}^2
\mid
\gamma Z_0^2a^2.
}
\tag{qZ-three-payer}

因此高度上

\[
\boxed{
\log D_{qZ}
\le
\frac12\log\gamma
+
\log Z_0
+
\log a.
}
\tag{4.1}

这个结论没有假设三者互素，也没有把同一 prime强行分给唯一 payer；
它是逐 prime exponent inequality 的精确全局乘积版本。

---

## 5. 回代 `L_Z|F_-`

上一文件已有

\[
L_Z=
\frac{2^{H+2}5^TZ}
{\gcd(2^{H+2}5^TZ,q)}
\mid F_-.
\]

因为 `Z` 为 10-unit：

\[
\gcd(2^{H+2}5^TZ,q)
\mid
2^{\mathfrak q}5^{q_5}D_{qZ}.
\]

结合 `(4.1)`，得到无需 `R_3^{den}` 的 height form：

\[
\boxed{
\begin{aligned}
\log_{10}F_-
\ge{}&aH+bT+\log_{10}Z\\
&-a\mathfrak q-bq_5
-\frac12\log_{10}\gamma\\
&-\log_{10}Z_0-\log_{10}a
+O(1).
\end{aligned}}
\tag{Projective-LZ-height}

所以 `q-Z` overlap 想吃掉 `Z`-divisor，只剩三种付款方式：

1. denominator overlap `gamma`；
2. stereographic projective denominator `Z_0`；
3. sphere-gap quotient `a`。

前者已经进入 `Subspace-defect`；后两者正是 carrier-circle / projective
allocation line中的 canonical variables。

---

## 6. 与 common/angular split 的关系

projective formula还给

\[
v_p(Z_0)=\max(0,r_p+\omega_p-v_p(a)).
\]

所以 `(qZ-three-payer)` 并没有把同一份 ghost depth重复收费：

- 当 gap depth `v_p(a)` 足够大时，`Z_0` 自动下降；
- 当 gap depth不足时，剩余 common/angle depth才进入 `Z_0`。

特别地，在 decimal prime `5` 的 angular branch中已有

\[
\omega_5>0
\Longrightarrow
v_5(U_{12}^{\rm prim})=0,
\]

而 `D_qZ` 本身不含 5。因此本文的 rough gcd allocation与已有
5-adic angular/bottom exclusion是互补而非重复的。

---

## 7. 当前边界

- **`已严格完成`**：`R3-projective-pay`、`qZ-three-payer`、
  `Projective-LZ-height`。
- **`结构压缩`**：`gcd(q,Z)` 不再需要独立 gcd-smallness 假设；其高度
  被完全归入 `gamma / Z_0 / a`。
- **`待证`**：证明 `Z_0` 与 `a` 的正线性高度不能同时支付
  `(Projective-LZ-height)` 所需 loss；最自然接口是无 `E_D` carrier-circle
  eliminant与 primitive determinant ladder。

---

<a id="source-high-funnel-qz-sheet-reader-collapse"></a>

> 整合来源：`high-funnel-qz-sheet-reader-collapse.md`

# DD `q-Z` two-sheet 的 reader collapse 与 balanced payer theorem

> **依赖：** [`high-funnel-qz-two-sheet-split.md`](high-funnel-ledger.md#source-high-funnel-qz-two-sheet-split)、
> `core.md` 的 primitive determinant ladder / overlap parameterization / carrier-circle
> eliminant。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
>
> 上一文件把未由 `gamma` square-root baseline 支付的 `D_{qZ}=gcd(q,Z)`
> excess 分成 gap / complementary 两个 sheets。本文继续证明：
>
> 1. `E_exc` 只是 sphere-gap quotient `a` 的同一 p-adic reader；
> 2. bottom carrier excess只是 prefix concat gcd `(A_12,Q)` 的同一 reader；
> 3. 因而真正 canonical sheet selector 是 `a / A_12`，不是 `E / Delta_12`；
> 4. 得到 balanced payer
>    \[
>    \boxed{D_{qZ}^2\mid\gamma\,a\,(A_{12},Q)\,Z_0;}
>    \]
> 5. `q-Z` prime本身恰好就是 carrier-circle eliminant 的单侧 moving-factor
>    ramification prime，因此直接套 two-residual eliminant不会产生独立高度收益。

---

## 1. 记号

沿用上一文件：

\[
D_{qZ}=(q,Z),
\qquad
D_{qZ}=D_{\rm base}D_{\rm ex},
\]

\[
D_{\rm gap}=(D_{\rm ex},E_{\rm exc}),
\qquad
D_{\rm comp}=D_{\rm ex}/D_{\rm gap},
\]

其中

\[
E_{\rm exc}=\frac{E}{(E,Q)},
\qquad
\Theta_{12}=\frac{\Delta_{12}}{(b_1,b_2)}.
\]

对任意

\[
p^e\Vert D_{\rm ex},\qquad e>0,
\]

上一文件已经证明 denominator pattern 必为

\[
e_1=e_2=M<e_3=r=M+c,
\qquad c>0,
\qquad e\le c,
\]

且 sphere只有 gap / complementary 两个 signs。

---

## 2. `a` 与 `A_12` 才是 primary sheet selectors

### 2.1 gap sheet

上一文件有

\[
p^e\mid A_{12}10^{n_3}+2a_3.
\]

因为 `p|b_3` 且 `(a_3,b_3)=1`：

\[
p\nmid a_3.
\]

所以模 `p`：

\[
A_{12}10^{n_3}\equiv-2a_3\not\equiv0.
\]

于是

\[
\boxed{v_p(A_{12})=0.}
\tag{2.1}

同时 gap factor满足

\[
v_p(H_{\rm sph}-y_3)\ge2c.
\]

对 `p\nmid10`，`L` 是 p-unit；由

\[
H_{\rm sph}-y_3=La
\]

得到

\[
\boxed{v_p(a)\ge2c\ge2e.}
\tag{2.2}

### 2.2 complementary sheet

这里

\[
p^e\mid A_{12},
\]

而

\[
v_p(H_{\rm sph}-y_3)=0.
\]

仍因 `p\nmid L`：

\[
\boxed{v_p(a)=0.}
\tag{2.3}

所以对 `D_ex` support，两个 primary readers严格互斥：

\[
\boxed{
\begin{array}{c|cc}
&v_p(a)&v_p(A_{12})\\ \hline
\text{gap}&\ge2e&0\\
\text{complementary}&0&\ge e
\end{array}}
\tag{Primary-sheets}

于是完全整数化地：

\[
\boxed{
D_{\rm gap}=(D_{\rm ex},a),
\qquad
D_{\rm comp}=(D_{\rm ex},A_{12}).}
\tag{2.4}

特别地

\[
\boxed{D_{\rm ex}\mid aA_{12},}
\tag{2.5}

\[
\boxed{(D_{\rm ex},a,A_{12})=1.}
\tag{2.6}

这才是 `q-Z` excess 的 canonical source/prefix two-sheet split。

---

## 3. gap sheet 的 `E_exc` 完全塌回 `a`

`core.md` 的 primitive determinant ladder定义

\[
D_{\rm sph}:=(H_{\rm sph},q_{\rm lcm}),
\qquad
C_{\rm concat}:=(\alpha,\beta),
\]

\[
E'=E/C_{\rm concat},
\]

并有 exact identity

\[
\boxed{D_{\rm sph}E'=\tau a.}
\tag{3.1}

固定 `p|D_ex`。第三分母在 p 处 unique maximum，故 `y_3` 与
`H_sph` 都是 p-units；因此

\[
v_p(D_{\rm sph})=0.
\tag{3.2}

上一文件 §4 已同时证明完整 numerator concat `alpha` 为 p-unit，而完整
`beta` 具有 depth `r`，所以

\[
v_p(C_{\rm concat})=0.
\tag{3.3}

又 `p\nmid10`，故

\[
v_p(\tau)=v_p(b_3)=r.
\tag{3.4}

由 `(3.1)`：

\[
\boxed{v_p(E)=r+v_p(a).}
\tag{3.5}

由于 `v_p(Q)=r`：

\[
\boxed{v_p(E_{\rm exc})=v_p(a).}
\tag{E-a-same-reader}

所以在 `D_ex` support上：

\[
\boxed{(D_{\rm ex},E_{\rm exc})=(D_{\rm ex},a).}
\tag{3.6}

上一文件中“gap sheet 的 E 变深”并不是第二份 carrier obstruction；它只是
primitive determinant ladder 对同一个 sphere gap `a` 的重读。

---

## 4. complementary sheet 的 bottom depth塌回 prefix concat gcd

定义

\[
\boxed{C_{12}:=(A_{12},Q).}
\tag{4.1}

complementary sheet中

\[
p^e\mid A_{12}
\]

且 `p^e|D_ex|q|Q`，所以

\[
\boxed{p^e\mid C_{12}.}
\tag{4.2}

而 gap sheet中 `A_12` 是 p-unit，因此

\[
\boxed{v_p(C_{12})=0.}
\tag{4.3}

故

\[
\boxed{
D_{\rm comp}=(D_{\rm ex},C_{12}).}
\tag{4.4}

另一方面 exact bottom identities为

\[
\frac{\Delta_{12}}{10^d}
=Qa_1 10^{s_2}-b_1A_{12},
\tag{4.5}

\[
\frac{-10^{m_2}\Delta_{12}}{10^d}
=Qa_2-b_2A_{12}.
\tag{4.6}

所以普通 gcd `C_12` 自动满足

\[
\boxed{C_{12}\mid\Delta_{12}/10^d.}
\tag{4.7}

因此 complementary sheet 的 bottom-carrier excess本质上是 prefix concat
numerator/denominator common factor的 determinant reader；它同样不是凭空出现的第二个
independent source。

---

## 5. balanced payer theorem

上一文件已证明：

\[
D_{\rm base}^2\mid\gamma,
\]

\[
D_{\rm gap}^2\mid a,
\]

以及 complementary sheet 上

\[
D_{\rm comp}\mid Z_0.
\]

本文又有

\[
D_{\rm comp}\mid C_{12}.
\]

所以

\[
\boxed{D_{\rm comp}^2\mid C_{12}Z_0.}
\tag{5.1}

逐 prime exponent 相加得到新的全局 balanced payer：

\[
\boxed{
D_{qZ}^{\,2}
\mid
\gamma\,a\,C_{12}\,Z_0.}
\tag{qZ-balanced-payer}

即

\[
\boxed{
D_{qZ}^{\,2}
\mid
\gamma\,a\,(A_{12},Q)\,Z_0.}
\tag{5.2}

因此

\[
\boxed{
\log_{10}D_{qZ}
\le
\frac12\left(
\log_{10}\gamma
+\log_{10}a
+\log_{10}C_{12}
+\log_{10}Z_0
\right).}
\tag{5.3}

在 d-dominant funnel中

\[
n_1+n_2=S+s_1+s_2\le S+2,
\]

所以

\[
A_{12}<10^{S+2},
\qquad Q<10^S,
\]

特别地

\[
\boxed{C_{12}<10^S.}
\tag{5.4}

这使 `(5.3)` 比单纯使用未知 `Z_0^2` 更适合后续 height optimization。

还可用 complementary sheet 的 bottom reader得到另一版本：

\[
\boxed{
D_{qZ}^{\,2}
\mid
\gamma\,a\,C_{12}\,|\Theta_{12}|,}
\tag{5.5}

因为 gap primes由 `a` 支付两份，而 complementary primes分别由
`C_12` 与 `Theta_12` 各支付一份。

---

## 6. balanced sharpened `L_Z` height

已有

\[
L_Z=
\frac{2^{H+2}5^TZ}
{(2^{H+2}5^TZ,q)}
\mid F_-.
\]

记

\[
a_2=\log_{10}2,
\qquad a_5=\log_{10}5.
\]

利用 `(5.3)`：

\[
\boxed{
\begin{aligned}
\log_{10}F_-
\ge{}&a_2H+a_5T+\log_{10}Z
-a_2\mathfrak q-a_5q_5\\
&-\frac12\log_{10}\gamma
-\frac12\log_{10}a
-\frac12\log_{10}C_{12}
-\frac12\log_{10}Z_0
+O(1).
\end{aligned}}
\tag{LZ-balanced-height}

并且可粗化

\[
-\frac12\log C_{12}\ge-\frac12S+O(1).
\]

这是一条新的可用于 LP / stability 重算的严格输入。

---

## 7. 为什么 carrier-circle eliminant 对 `q-Z` prime天然 ramified

`core.md` 的 overlap parameterization写成

\[
\eta=(Q,\tau),
\qquad Q=\eta Q_1,
\qquad \tau=\eta v,
\]

并有

\[
\boxed{u=LQ_1.}
\tag{7.1}

在 `t_2=1` S-unit phase：

\[
u=2\cdot5^TU,
\qquad v=V.
\]

所以两个 normalized moving factors精确为

\[
\boxed{
LQ_1+2v
=u+2v
=2^{H+1}Z,}
\tag{7.2}

\[
\boxed{
LQ_1+v
=u+v
=5^TU+2^HZ.}
\tag{7.3}

固定 `p|D_qZ`。因为 `p|Z` 且 `p\nmid U`：

\[
\boxed{v_p(LQ_1+v)=0,}
\tag{7.4}

\[
\boxed{v_p(LQ_1+2v)=v_p(Z).}
\tag{7.5}

而无 `E_D` circle eliminant 的 normalized moving part正包含

\[
(LQ_1+v)^2(LQ_1+2v)^2.
\]

所以它在 `q-Z` support上自动携带

\[
\boxed{2v_p(Z)}
\tag{7.6}

的单侧 ramification depth。

因此即使额外构造出两条 residual 的共同 `p^h` contact，`h<=...+v_p(Xi)`
中的 moving-factor term也已经可以直接由同一个 `Z` 支付。换言之：

\[
\boxed{
\text{raw carrier-circle eliminant 对 `q-Z` primes 是结构性饱和的。}}
\tag{Circle-qZ-nogo}

这和上一文件证明的“两个 carrier readers本来就不会自动同时深”相互独立；
两点共同说明继续沿 raw circle resultant磨 `q-Z` gcd不会得到新的线性高度。

---

## 8. 新的真实 frontier

`q-Z` bottleneck现在被压成：

\[
\boxed{
D_{\rm ex}
\rightsquigarrow
\begin{cases}
D_{\rm gap}:& D_{\rm gap}^2\mid a,\\
D_{\rm comp}:& D_{\rm comp}\mid C_{12},\ Z_0,\ \Theta_{12},
\end{cases}}
\]

并且两 sheets 在 prime support上互斥。

其中：

- gap 的 `E_exc` 已证明只是 `a` 的重复 reader；
- complementary 的 bottom carrier已证明至少包含 prefix concat gcd `C_12` 的重复 reader；
- raw carrier-circle eliminant又被 `Z` moving factor结构性 ramification饱和。

因此下一步不应再尝试 local same-prime resultant。真正可能产生新高度的接口只剩：

1. 对 `C_12=(A_12,Q)` 建立 prefix-uniform gcd / digit-shell bound；
2. 将 `aZ_0` 用 sphere/projective exact factorization重写，和 scale-free allocation比较；
3. 把 balanced `L_Z` height与 Schmidt / defect-aware stability重新做 LP。

DD 全局仍为 `待证`。

---

<a id="source-high-funnel-qz-two-sheet-split"></a>

> 整合来源：`high-funnel-qz-two-sheet-split.md`

# DD high-funnel 的 `q-Z` excess two-sheet split

> **依赖：** [`high-funnel-qz-gcd-allocation.md`](high-funnel-ledger.md#source-high-funnel-qz-gcd-allocation)、
> [`high-funnel-qz-projective-allocation.md`](high-funnel-ledger.md#source-high-funnel-qz-projective-allocation)、
> `core.md` 的 `t_2=1` S-unit phase、integer sphere / exact lift、nested carry、
> Plücker 关系与 projective denominator 公式。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
>
> 本文处理 `D_{qZ}=gcd(q,Z)` 中没有被 denominator-overlap `gamma` 的
> square-root baseline 支付的部分。结论不是“该 excess 自动进入两条独立
> carrier residual”；恰恰相反，它有一个精确 two-sheet split：
>
> - **gap sheet**：excess 进入 sphere gap 与 decimal determinant `E`，而
>   bottom carrier 没有 excess；
> - **complementary sheet**：`E` 只有 baseline，而 bottom carrier获得全部
>   excess，并且同一 prime 同时进入 projective denominator `Z_0`。
>
> 作为全局推论，旧 payer bound
> \[
> D_{qZ}^2\mid \gamma Z_0^2a^2
> \]
> 可严格加强为
> \[
> \boxed{D_{qZ}^2\mid \gamma a Z_0^2.}
> \]

---

## 1. canonical excess modulus

在 `t_2=1` funnel 中：

\[
\kappa=\gamma u,\qquad G=\gamma V,
\qquad u=2\cdot5^TU,
\qquad Q=Uq,
\]

\[
2^HZ=5^TU+V,
\qquad (UVZ,10)=1,
\qquad (U,V)=1.
\]

沿用

\[
D_{qZ}:=(q,Z).
\]

因为 `Z` 是 10-unit，`D_{qZ}` 也只含 `p\nmid10` 的素数。

定义 `gamma` 的 non-decimal square-root part

\[
\boxed{
\Gamma_{1/2}
:=\prod_{p\nmid10}p^{\lfloor v_p(\gamma)/2\rfloor}.
}
\tag{1.1}

于是

\[
\Gamma_{1/2}^2\mid\gamma.
\]

把 `q-Z` gcd 分成

\[
\boxed{
D_{\rm base}:=(D_{qZ},\Gamma_{1/2}),
\qquad
D_{\rm ex}:=D_{qZ}/D_{\rm base}.
}
\tag{1.2}

`D_base` 是可以直接由 `gamma` 的平方深度支付的部分；真正需要继续追踪的
是 `D_ex`。

---

## 2. `D_ex` prime 必然是第三分母 unique-max

固定

\[
p^e\Vert D_{\rm ex},\qquad e>0.
\]

写

\[
r:=v_p(q)=v_p(Q),
\qquad z:=v_p(Z),
\qquad d_p:=v_p(D_{qZ})=\min(r,z),
\]

以及 denominator valuations

\[
e_i:=v_p(b_i).
\]

`high-funnel-qz-gcd-allocation.md` 已证明：

\[
p\nmid UV,
\qquad e_3=r,
\qquad v_p(\gamma)=e_1+e_2.
\tag{2.1}

若 `e_1\ne e_2`，二项赋值给

\[
r=\min(e_1,e_2),
\]

从而

\[
\left\lfloor\frac{v_p(\gamma)}2\right\rfloor
\ge r\ge d_p,
\]

与 `e>0` 矛盾。

因此必有

\[
\boxed{e_1=e_2=:M.}
\tag{2.2}

此时

\[
v_p(\gamma)=2M.
\]

如果 `r=M`，仍有 `d_p<=M`，不会进入 `D_ex`。故必有

\[
\boxed{r=M+c,\qquad c>0.}
\tag{2.3}

并且

\[
\boxed{e=d_p-M>0,\qquad e\le c,\qquad z\ge M+e.}
\tag{2.4}

所以每个 `D_ex` prime 都具有唯一 denominator pattern

\[
\boxed{e_1=e_2=M<e_3=M+c.}
\tag{Third-exclusive}

---

## 3. 两条 denominator Hensel relations

写

\[
b_1=p^MB_1,\qquad
b_2=p^MB_2,\qquad
b_3=p^{M+c}B_3,
\]

\[
Q=p^{M+c}Q_0,
\]

其中 `B_1,B_2,B_3,Q_0` 都是 `p`-units。

由

\[
Q=b_1 10^{m_2}+b_2
\]

得到 prefix cancellation

\[
\boxed{
B_1 10^{m_2}+B_2=p^cQ_0.
}
\tag{3.1}

另一方面

\[
\kappa+2G
=G\frac{10^mQ+2b_3}{b_3}.
\]

而 S-unit phase 给

\[
v_p(\kappa+2G)
=v_p(\gamma)+v_p(Z)
=2M+z.
\]

所以

\[
\boxed{
v_p(10^mQ+2b_3)=M+c+z=r+z.}
\tag{3.2}

除去 `p^r`：

\[
\boxed{
10^mQ_0+2B_3\equiv0\pmod{p^z}.}
\tag{Tail-sign}

令完整 denominator concat

\[
\beta=10^mQ+b_3
=p^r\beta_0,
\qquad
\beta_0:=10^mQ_0+B_3.
\]

由 `(Tail-sign)`：

\[
\boxed{
\beta_0\equiv-B_3\pmod{p^z},
\qquad p\nmid\beta_0.}
\tag{3.3}

---

## 4. sphere 强迫唯一的两条 sign sheets

记整数球面半径为 `H_sph`，避免与 S-unit exponent `H` 混淆。

由于第三分母在 `p` 处唯一最大，lcm denominator 的 `p`-depth为 `r`。
于是

\[
p^c\mid y_1,y_2,
\qquad p\nmid y_3.
\]

sphere equation

\[
H_{\rm sph}^2-y_3^2=y_1^2+y_2^2
\]

说明 `H_sph` 也是 `p`-unit，并且

\[
v_p(y_1^2+y_2^2)\ge2c.
\]

因为 `p` 为奇素数且 `y_3` 为 unit，

\[
(H_{\rm sph}-y_3,\ H_{\rm sph}+y_3)
\]

不可能同时被 `p` 整除。因此恰有一条深：

\[
\boxed{
\begin{array}{ll}
\text{gap sheet:}&
 v_p(H_{\rm sph}-y_3)\ge2c,
 \quad v_p(H_{\rm sph}+y_3)=0,\\[1mm]
\text{complementary sheet:}&
 v_p(H_{\rm sph}+y_3)\ge2c,
 \quad v_p(H_{\rm sph}-y_3)=0.
\end{array}}
\tag{Sphere-sheets}

现在令完整 numerator concat

\[
\alpha=A_{12}10^{n_3}+a_3,
\qquad n_3=m+d.
\]

写 lcm denominator 为

\[
q_{\rm lcm}=p^rq_0,
\qquad p\nmid q_0.
\]

exact lift 与第三 ghost coordinate给

\[
q_0\alpha=H_{\rm sph}\beta_0,
\qquad
y_3=a_3\frac{q_0}{B_3}.
\]

所以

\[
\frac{H_{\rm sph}}{y_3}
=\frac{\alpha B_3}{a_3\beta_0}
\equiv-\frac\alpha{a_3}
\pmod{p^z}.
\tag{4.1}

由 `(2.4)` 有 `e<=c` 且 `z>=e`。结合 `(Sphere-sheets)`：

### gap sheet

\[
H_{\rm sph}/y_3\equiv1\pmod{p^e},
\]

故

\[
\boxed{
p^e\mid\alpha+a_3
=A_{12}10^{n_3}+2a_3.}
\tag{Gap-num}

### complementary sheet

\[
H_{\rm sph}/y_3\equiv-1\pmod{p^e},
\]

故

\[
\boxed{
p^e\mid\alpha-a_3=A_{12}10^{n_3}.}
\]

因为 `p\nmid10`：

\[
\boxed{p^e\mid A_{12}.}
\tag{Comp-num}

这就是 `q-Z` excess 的 numerator two-sheet selector。

---

## 5. gap sheet：`E` 深、bottom carrier 恰为 baseline

DD decimal determinant为

\[
\boxed{E=b_3A_{12}10^d-a_3Q.}
\tag{5.1}

由 `(Gap-num)` 与 `n_3=m+d`：

\[
A_{12}10^d
\equiv-2a_3 10^{-m}
\pmod{p^e}.
\tag{5.2}

由 `(Tail-sign)`：

\[
Q_0\equiv-2B_3 10^{-m}\pmod{p^e}.
\tag{5.3}

代入 `(5.1)`：

\[
\boxed{v_p(E)\ge r+e.}
\tag{Gap-E}

下面证明 bottom carrier没有获得同一 excess。

定义三个 raw carrier determinants：

\[
\Delta_{12}
=a_1 10^k b_2-a_2 10^d b_1,
\]

\[
\Delta_{13}
=a_1 10^k b_3-a_3b_1,
\qquad
\Delta_{23}
=a_2 10^d b_3-a_3b_2,
\]

其中

\[
k=s_2+d,
\qquad n_2=m_2+s_2.
\]

由于 `r>M` 且 `p\mid b_3` 强迫 `p\nmid a_3`：

\[
\boxed{v_p(\Delta_{13})=v_p(\Delta_{23})=M.}
\tag{5.4}

写

\[
\Delta_{13}=p^MD_{13},
\qquad
\Delta_{23}=p^MD_{23},
\]

其中 `D_13,D_23` 为 units。

nested carry 是 exact identity

\[
\boxed{E=10^{m_2}\Delta_{13}+\Delta_{23}.}
\tag{5.5}

由 `(Gap-E)`：

\[
10^{m_2}D_{13}+D_{23}=p^{c+e}W_p
\tag{5.6}

对某个整数 `W_p`。

同时 Plücker 关系

\[
b_1\Delta_{23}-b_2\Delta_{13}+b_3\Delta_{12}=0
\]

除去 `p^{2M}`，并使用 `(3.1)` 与 `(5.6)`，得到

\[
B_3\frac{\Delta_{12}}{p^M}
=Q_0D_{13}-p^eB_1W_p.
\tag{5.7}

右边模 `p` 等于 unit `Q_0D_13`，故

\[
\boxed{v_p(\Delta_{12})=M.}
\tag{Gap-bottom-baseline}

令

\[
d_{12}:=(b_1,b_2),
\qquad
\Theta_{12}:=\Delta_{12}/d_{12}.
\]

因为当前 `v_p(d_12)=M`：

\[
\boxed{v_p(\Theta_{12})=0.}
\tag{Gap-Theta-unit}

所以 gap sheet 的 excess只进入 `E`，不会再次进入 bottom carrier。

---

## 6. complementary sheet：`E` 恰为 baseline、bottom carrier变深

由 `(Comp-num)`：

\[
p^e\mid A_{12},
\qquad e>0.
\]

在 `(5.1)` 除去 `p^r` 后，第一项仍被 `p` 整除，而
`a_3Q_0` 是 unit。因此

\[
\boxed{v_p(E)=r.}
\tag{Comp-E-baseline}

另一方面有 exact bottom identity

\[
\boxed{
\frac{\Delta_{12}}{10^d}
=Qa_1 10^{s_2}-b_1A_{12}.}
\tag{6.1}

第一项的 `p`-depth至少为 `r>=M+e`，第二项至少为 `M+e`，所以

\[
\boxed{v_p(\Delta_{12})\ge M+e.}
\]

即

\[
\boxed{v_p(\Theta_{12})\ge e.}
\tag{Comp-bottom-excess}

因此 complementary sheet 与 gap sheet恰好相反：bottom carrier获得全部
`D_ex` depth，而 `E` 没有任何 excess。

---

## 7. canonical integer sheet selectors

定义 normalized decimal-determinant excess reader

\[
\boxed{
E_{\rm exc}
:=\frac{E}{(E,Q)}.}
\tag{7.1}

对每个 `p^e||D_ex`：

\[
\boxed{
\begin{array}{c|cc}
&v_p(E_{\rm exc})&v_p(\Theta_{12})\\ \hline
\text{gap sheet}&\ge e&0\\
\text{complementary sheet}&0&\ge e
\end{array}}
\tag{7.2}

于是可完全整数化地定义

\[
\boxed{
D_{\rm gap}:=(D_{\rm ex},E_{\rm exc}),
\qquad
D_{\rm comp}:=D_{\rm ex}/D_{\rm gap}.}
\tag{7.3}

逐素数由 `(7.2)` 得

\[
\boxed{(D_{\rm gap},D_{\rm comp})=1,}
\tag{7.4}

\[
\boxed{D_{\rm gap}\mid E_{\rm exc},}
\tag{7.5}

\[
\boxed{D_{\rm comp}\mid\Theta_{12},}
\tag{7.6}

以及 no-double-contact：

\[
\boxed{(D_{\rm ex},E_{\rm exc},\Theta_{12})=1.}
\tag{7.7}

特别地

\[
\boxed{D_{\rm ex}\mid E_{\rm exc}\Theta_{12}}
\tag{Two-sheet-product}

但 `D_ex` 的同一个 prime不可能同时由这两个 carrier reader支付。

这正式说明：从 `p|q,Z` 直接跳到“两条独立 carrier residual 同时深”是错误路线。

---

## 8. sphere/projective payer也随 sheet 锁定

### gap sheet

这里

\[
v_p(H_{\rm sph}-y_3)\ge2c.
\]

对 `p\nmid10`，tail quotient `L` 没有 `p`-part，而

\[
H_{\rm sph}-y_3=La.
\]

所以

\[
v_p(a)\ge2c\ge2e.
\]

因此

\[
\boxed{D_{\rm gap}^2\mid a.}
\tag{Gap-a-pay}

### complementary sheet

令

\[
g_y:=(y_1,y_2),
\qquad \rho:=v_p(g_y)\ge c.
\]

写 primitive sum depth

\[
v_p(y_1^2+y_2^2)=2\rho+\omega_p.
\]

complementary sheet中全部深度进入 `H_sph+y_3`，故

\[
v_p(H_{\rm sph}+y_3)=2\rho+\omega_p.
\]

projective denominator已有 exact formula

\[
Z_0=\frac{H_{\rm sph}+y_3}{(g_y,H_{\rm sph}+y_3)}.
\]

所以

\[
v_p(Z_0)=\rho+\omega_p\ge c\ge e.
\]

因此

\[
\boxed{D_{\rm comp}\mid Z_0.}
\tag{Comp-Z0-pay}

---

## 9. `q-Z` payer theorem 的严格加强

由定义

\[
D_{qZ}=D_{\rm base}D_{\rm ex}
=D_{\rm base}D_{\rm gap}D_{\rm comp}.
\]

又

\[
D_{\rm base}^2\mid\Gamma_{1/2}^2\mid\gamma,
\]

并由 `(Gap-a-pay)`、`(Comp-Z0-pay)`：

\[
D_{\rm gap}^2D_{\rm comp}^2
\mid aZ_0^2.
\]

逐素数相加 exponent 得到

\[
\boxed{
D_{qZ}^{\,2}\mid\gamma\,a\,Z_0^2.}
\tag{qZ-three-payer-sharp}

因此高度形式严格加强为

\[
\boxed{
\log_{10}D_{qZ}
\le
\frac12\log_{10}\gamma
+\frac12\log_{10}a
+\log_{10}Z_0.}
\tag{9.1}

相比旧 `gamma Z_0^2 a^2`，sphere-gap payer 的 coefficient 从 `1` 降为
`1/2`。

---

## 10. sharpened `L_Z` height

`high-funnel-qz-gcd-allocation.md` 已有

\[
L_Z=
\frac{2^{H+2}5^TZ}
{(2^{H+2}5^TZ,q)}
\mid F_-.
\]

记

\[
a_2:=\log_{10}2,
\qquad a_5:=\log_{10}5.
\]

因为 `Z` 为 10-unit：

\[
\log_{10}(2^{H+2}5^TZ,q)
\le
a_2\mathfrak q+a_5q_5+\log_{10}D_{qZ}+O(1).
\]

使用 `(9.1)`：

\[
\boxed{
\begin{aligned}
\log_{10}F_-
\ge{}&a_2H+a_5T+\log_{10}Z
-a_2\mathfrak q-a_5q_5\\
&-\frac12\log_{10}\gamma
-\frac12\log_{10}a
-\log_{10}Z_0
+O(1).
\end{aligned}}
\tag{LZ-height-sharp}

所以未来的 global height optimization 不再需要把 `q-Z` gcd作为一个未知
loss；它只剩三个明确 payer，而且 sphere-gap payer已经按真实 square depth只收费
半份。

---

## 11. 当前边界

本文同时给出一个正面结构结论和一个重要 no-go：

1. **正面：** `q-Z` excess 被 canonical 地分成 `gap / complementary` 两个
   Hensel sheets，并得到 sharpened three-payer theorem
   \[
   D_{qZ}^2\mid\gamma aZ_0^2.
   \]
2. **no-go：** `q-Z` excess **不会**自动制造两条独立 carrier residual 的共同
   深度；在同一 prime上，`E_exc` 与 `Theta_12` 两个 reader严格互斥。

因此下一步不能无条件套 `core.md` §56 的 two-residual circle eliminant。真正应分别攻击：

- `gap sheet`：`D_gap^2|a` 与 primitive determinant ladder / `E_exc` 的兼容；
- `complementary sheet`：`D_comp|Z_0` 且 `D_comp|Theta_12` 的 projective-bottom
  simultaneous contact。

DD 全局仍为 `待证`。

---

<a id="source-high-funnel-recovery-squarefree-lock"></a>

> 整合来源：`high-funnel-recovery-squarefree-lock.md`

# DD canonical `t_2=1` recovery gcd 的 squarefree lock

> **依赖：** `core.md` 的 gap 定义、overlap 参数化、primitive recovery
> \(10^mQG_0=2\kappa\mu\nu\)，以及
> [`high-funnel-exact-small-factor-normalization.md`](high-funnel-ledger.md#source-high-funnel-exact-small-factor-normalization)
> 中对 source `q` / reduced `q_red` 的严格区分。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
>
> 本文显式恢复 reduced gap ratio `mu/nu`，并得到
> \[
> \boxed{
> h^2G_0=2\varepsilon^3Lc^4r_*^2a_0,
> }
> \]
> 其中
> \[
> h=(\varepsilon Lc^2r_*a_0,q_0).
> \]
> 因而
> \[
> \boxed{
> \operatorname{sqf}(G_0)
> =\operatorname{sqf}(2\varepsilon La_0).
> }
> \]
> pure common sheet上更化为
> \[
> \boxed{
> \operatorname{sqf}(G_0)=\operatorname{sqf}(\varepsilon a_0).
> }

---

## 1. gap ratio 的显式分数

整数球面提升给

\[
\mathcal R=H/q_{\rm lcm},
\qquad
r_3=y_3/q_{\rm lcm}.
\]

因此

\[
\mathcal R-r_3
=\frac{H-y_3}{q_{\rm lcm}}
=\frac{La}{q_{\rm lcm}}.
\]

unified quadratic中定义

\[
\boxed{
G(\mathcal R-r_3)=\frac\mu\nu,
\qquad (\mu,\nu)=1.
}
\tag{1.1}

primitive exact-lift parameterization为

\[
q_{\rm lcm}=Dq_0,
\qquad
D=Vc\lambda,
\]

而 overlap 参数化给

\[
G=\varepsilon Vc^2\lambda r_*,
\qquad
a=ca_0.
\]

所以

\[
\begin{aligned}
G(\mathcal R-r_3)
&=\frac{GLa}{Dq_0}\\
&=\frac{\varepsilon Vc^2\lambda r_*\,Lca_0}
{Vc\lambda q_0}\\
&=\boxed{
\frac{\varepsilon Lc^2r_*a_0}{q_0}.}
\end{aligned}
\tag{Gap-ratio-explicit}

定义

\[
\boxed{
N_\mu:=\varepsilon Lc^2r_*a_0,
\qquad
h:=(N_\mu,q_0).
}
\tag{1.2}

由于 `(1.1)` 已是最低项：

\[
\boxed{
\mu=\frac{N_\mu}{h},
\qquad
\nu=\frac{q_0}{h}.}
\tag{mu-nu-explicit}

---

## 2. canonical `t_2=1` 的 auxiliary identities

令

\[
r_0:=2\cdot5^T,
\qquad
s:=(r_0,q),
\]

其中 `Q=Uq` 是 S-unit phase 的 source factor。

`high-funnel-exact-small-factor-normalization.md` 已证明 gcd-normal reduced pair为

\[
L=\frac{r_0}{s},
\qquad
q_{\rm red}=\frac qs.
\]

另一方面 overlap 参数化有

\[
u=LQ_1,
\qquad Q=\eta Q_1,
\]

而 `t_2=1` 给

\[
u=r_0U,
\qquad Q=Uq.
\]

因此

\[
Q_1=sU,
\]

从而

\[
\boxed{q=s\eta,\qquad q_{\rm red}=\eta.}
\tag{2.1}

并且

\[
\boxed{\tau=\eta V.}
\]

此外

\[
G=\gamma V
=\varepsilon Vc^2\lambda r_*
\]

给

\[
\boxed{\gamma=\varepsilon c^2\lambda r_*.}
\tag{2.2}

primitive denominator参数为

\[
\boxed{q_0=\frac{\omega\eta\varepsilon}{\lambda}.}
\tag{2.3}

---

## 3. primitive recovery 把 `G_0` 完全展开

统一 primitive recovery为

\[
\boxed{
10^mQG_0=2\kappa\mu\nu.}
\tag{3.1}

在 canonical phase：

\[
Q=Us\eta,
\qquad
\kappa=\gamma r_0U.
\]

代入 `(3.1)` 并约去 `U`：

\[
10^ms\eta G_0
=2\gamma r_0\mu\nu.
\]

又

\[
\omega=10^m/L=10^ms/r_0,
\]

所以

\[
\boxed{
\omega\eta G_0=2\gamma\mu\nu.}
\tag{3.2}

使用 `(mu-nu-explicit)`：

\[
\mu\nu
=\frac{N_\mu q_0}{h^2}.
\]

再代入

\[
N_\mu=\varepsilon Lc^2r_*a_0,
\quad
q_0=\frac{\omega\eta\varepsilon}{\lambda},
\quad
\gamma=\varepsilon c^2\lambda r_*.
\]

则 `(3.2)` 右侧为

\[
\frac{
2\omega\eta\varepsilon^3Lc^4r_*^2a_0
}{h^2}.
\]

约去 `omega eta`，得到 exact identity

\[
\boxed{
 h^2G_0
=2\varepsilon^3Lc^4r_*^2a_0.
}
\tag{Recovery-square}

---

## 4. squarefree kernel 被完全锁死

对正整数 `N`，记 `sqf(N)` 为删去全部偶次 prime exponent后的平方自由核。

`(Recovery-square)` 两边相差的因子

\[
h^2,\quad c^4,\quad r_*^2
\]

全部是完全平方；而 `epsilon^3` 与 `epsilon` 的 prime-exponent parity相同。
因此逐素数 parity完全相等：

\[
\boxed{
\operatorname{sqf}(G_0)
=\operatorname{sqf}(2\varepsilon La_0).
}
\tag{G0-squarefree-lock}

这不是只有 radical inclusion，而是 squarefree kernel本身的精确相等。

---

## 5. pure common specialization

在 pure common / `mathfrak q=0` endpoint：

\[
q_5=n_5=0,
\quad m=4g_5,
\quad T=2g_5,
\quad s=1.
\]

所以

\[
L=2\cdot5^{2g_5}.
\]

于是

\[
2L=4\cdot5^{2g_5}
=(2\cdot5^{g_5})^2
\]

是完全平方。

`(G0-squarefree-lock)` 因而退化成

\[
\boxed{
\operatorname{sqf}(G_0)
=\operatorname{sqf}(\varepsilon a_0).
}
\tag{Pure-G0-squarefree}

这与 `high-funnel-gap-square-core.md` 的

\[
a_0G_0=\varepsilon\mu_0^2
\]

相容；本文进一步说明这种相容性来自 recovery 的 exact gcd normalization，
不是偶然的 5-adic parity coincidence。

---

## 6. 方法边界

本文把 `G_0` 的**平方自由 support**完全锁死，但没有给 `G_0` 的平方部分高度上界。
所以它不会单独关闭 pure common branch。

真正剩余自由从

\[
\text{arbitrary prime support of }G_0
\]

缩成

\[
\boxed{\text{square depth / Archimedean height inside a fixed support parity pattern}.}
\]

这提示后续不要继续做 radical chasing；应改为：

1. 控制 `h=(N_mu,q_0)` 的高度，或
2. 用 `(Recovery-square)` 比较 `G_0` 与 `epsilon,L,c,r_*,a_0` 的实际大小，或
3. 把 `mu=N_mu/h` 的平方高度送回 `F_-` / digit shell。

---

## 7. 状态摘要

- **`已严格完成`**：`Gap-ratio-explicit`、`mu-nu-explicit`、`q_red=eta`、
  `Recovery-square`、`G0-squarefree-lock`。
- **`结构压缩`**：pure common 中 `G_0` 不再有自由 squarefree support；只剩平方深度/高度。
- **`待证`**：`h` 的 height、`G_0` square depth、全 DD branch reoptimization、DD global closure。

---

<a id="source-high-funnel-square-identities-audit"></a>

> 整合来源：`high-funnel-square-identities-audit.md`

# DD gap/recovery square identities 的 no-double-pay 审计

> **依赖：** [`high-funnel-gap-square-core.md`](high-funnel-ledger.md#source-high-funnel-gap-square-core)、
> [`high-funnel-recovery-squarefree-lock.md`](high-funnel-ledger.md#source-high-funnel-recovery-squarefree-lock)、
> `global-framework.md` 的 `G_0|2G N_12`。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
>
> 两条看似不同的平方结构
> \[
> 5^Ta_0G_0=s\varepsilon\mu^2
> \]
> 与
> \[
> h^2G_0=2\varepsilon^3Lc^4r_*^2a_0
> \]
> **不是两份独立高度**。结合
> \[
> L=2\cdot5^T/s
> \]
> 后，它们恰好退化为 `mu=N_mu/h` 的定义平方。
>
> 真正可从第二式继续提取的新信息来自全局 recovery gcd bound
> `G_0|2G N_12`，它给出新的 exact divisor
> \[
> \boxed{
> \varepsilon^2Lc^2r_*a_0
> \mid
> V\lambda\mathcal N_{12}h^2,
> }
> \]
> 等价地
> \[
> \boxed{
> \mu^2
> \mid
> V\lambda Lc^2r_*a_0\mathcal N_{12}.
> }
> \]

---

## 1. 两条 square identity

已有

\[
\boxed{
5^Ta_0G_0=s\varepsilon\mu^2,
}
\tag{Gap-square}

以及

\[
\boxed{
h^2G_0=2\varepsilon^3Lc^4r_*^2a_0.}
\tag{Recovery-square}

这里

\[
N_\mu=\varepsilon Lc^2r_*a_0,
\qquad
h=(N_\mu,q_0),
\qquad
\mu=N_\mu/h,
\]

且 canonical `t_2=1` normalization给

\[
\boxed{L=\frac{2\cdot5^T}{s}.}
\tag{1.1}

---

## 2. 两式联立只恢复 `h mu = N_mu`

把 `(Recovery-square)` 中的 `G_0` 代入 `(Gap-square)`：

\[
5^Ta_0
\frac{2\varepsilon^3Lc^4r_*^2a_0}{h^2}
=s\varepsilon\mu^2.
\]

由 `(1.1)`，

\[
2\cdot5^T=sL.
\]

所以

\[
\frac{s\varepsilon^3L^2c^4r_*^2a_0^2}{h^2}
=s\varepsilon\mu^2.
\]

约去 `s epsilon`：

\[
\left(
\frac{\varepsilon Lc^2r_*a_0}{h}
\right)^2
=\mu^2.
\]

所有量均为正，因此

\[
\boxed{
h\mu=\varepsilon Lc^2r_*a_0=N_\mu.}
\tag{2.1}

这正是 `mu=N_mu/h` 的定义，不是新的 obstruction。

因此禁止如下 double-count：

> 不能把 `Gap-square` 与 `Recovery-square` 的 squarefree / square-depth
> 看成两份独立约束再相加高度。

它们是同一 primitive recovery algebra 的两个 reader。

---

## 3. 真正的新输入：`G_0|2G N_12`

全局 primitive recovery 已证明

\[
\boxed{G_0\mid2G\mathcal N_{12}.}
\tag{3.1}

而 overlap 参数化给

\[
\boxed{G=\varepsilon Vc^2\lambda r_*.}
\tag{3.2}

令

\[
K:=\frac{2G\mathcal N_{12}}{G_0}\in\mathbf Z_{>0}.
\]

将 `(Recovery-square)` 与 `(3.2)` 代入：

\[
\begin{aligned}
K
&=
\frac{2\varepsilon Vc^2\lambda r_*\mathcal N_{12}}
{2\varepsilon^3Lc^4r_*^2a_0/h^2}\\
&=
\boxed{
\frac{V\lambda\mathcal N_{12}h^2}
{\varepsilon^2Lc^2r_*a_0}.}
\end{aligned}
\tag{3.3}

因为 `K` 是整数，得到 exact divisor

\[
\boxed{
\varepsilon^2Lc^2r_*a_0
\mid
V\lambda\mathcal N_{12}h^2.
}
\tag{Recovery-divisor-h}

---

## 4. 等价的 `mu^2` divisor

由 `(2.1)`：

\[
h^2\mu^2
=\varepsilon^2L^2c^4r_*^2a_0^2.
\]

将 `(3.3)` 中的 `h^2` 改写，也可得到

\[
K
=
\frac{V\lambda Lc^2r_*a_0\mathcal N_{12}}{\mu^2}.
\]

因此

\[
\boxed{
\mu^2
\mid
V\lambda Lc^2r_*a_0\mathcal N_{12}.
}
\tag{Recovery-divisor-mu}

这条比 squarefree-kernel parity强：它控制的是 `mu` 的**完整平方深度**。

---

## 5. primewise allocation

对任意 prime `p`，令 `v_p` 简写为 valuation。`Recovery-divisor-mu` 给

\[
\boxed{
2v_p(\mu)
\le
v_p(V)+v_p(\lambda)+v_p(L)
+2v_p(c)+v_p(r_*)+v_p(a_0)+v_p(\mathcal N_{12}).
}
\tag{5.1}

所以任何 `mu` 的正线性 square depth必须由以下真实 payer承担：

- moving imbalance `V`；
- primitive common scale `lambda`；
- decimal smooth tail `L`；
- overlap common factor `c^2 r_*`；
- gap quotient `a_0`；
- prefix Gaussian norm `N_12`。

但本文不把这些 payer视为相互独立；它们之间仍有 overlap 参数化与
scale-free quadratic 的关系，下一步必须继续做 no-double-pay。

---

## 6. pure common 的 5-adic consistency

在 pure common sheet：

\[
T=2g_5,
\quad v_5(\mu)=g_5,
\quad v_5(V)=v_5(a_0)=v_5(\mathcal N_{12})=0.
\]

`Recovery-divisor-mu` 的 5-adic 左边为 `2g_5`，而 `L` 本身已经恰有

\[
v_5(L)=2g_5.
\]

所以该 prime 上 divisor完全由 forced decimal baseline `L` 支付，没有额外
5-adic contradiction。这再次说明 pure common 的真正下一自由度不是继续做
same-prime 5-adic lifting，而是 rough/square-height allocation。

---

## 7. 状态摘要

- **`已严格完成`**：square-identities no-double-pay、`Recovery-divisor-h`、
  `Recovery-divisor-mu`。
- **`失效/降级`**：把 `Gap-square` 与 `Recovery-square` 当两条独立 square
  obstruction进行高度相加。
- **`待证`**：rough prime 下 `mu^2` payer 的进一步互斥；post-tail side-branch
  reoptimization；DD global explicit slope / absolute height。

---

<a id="source-high-funnel-tail-short-schmidt-upgrade"></a>

> 整合来源：`high-funnel-tail-short-schmidt-upgrade.md`

# DD Tail-short 的 recovered-Schmidt upgrade 与 canonical sector `<=6`

> **依赖：** [`high-funnel-five-adic-dichotomy.md`](high-funnel-ledger.md#source-high-funnel-five-adic-dichotomy)、
> [`high-funnel-defect-optimization.md`](high-funnel-ledger.md#source-high-funnel-defect-optimization)、
> [`high-funnel-two-adic-balance.md`](high-funnel-ledger.md#source-high-funnel-two-adic-balance)、
> [`high-funnel-xi-depth.md`](high-funnel-ledger.md#source-high-funnel-xi-depth)、
> [`high-funnel-denominator-max-lock.md`](high-funnel-ledger.md#source-high-funnel-denominator-max-lock)、
> [`high-funnel-final5-sphere-c3-collapse.md`](high-funnel-ledger.md#source-high-funnel-final5-sphere-c3-collapse)。
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

---

<a id="source-high-funnel-two-adic-balance"></a>

> 整合来源：`high-funnel-two-adic-balance.md`

# DD high-funnel 的 2-adic shallow-gap 与 tail-root balance

> **依赖：** `core.md` 的 `t_2=1` S-unit funnel、overlap 参数化与 scale-free quadratic，
> [`high-funnel-denominator-max-lock.md`](high-funnel-ledger.md#source-high-funnel-denominator-max-lock) 的 `Final-5-lock`，以及固定目标 Schmidt Subspace Theorem。
>
> **严格状态：** `已严格完成（canonical t_2=1 double-resonant funnel）`。
> 本文不声称新的全 DD 数值 `limsup`。新增的核心是两个 exact finite-height 结论：
>
> 1. 在 `b_3` 二进 unique maximum、`t_2=1` 的 canonical funnel 中，sphere gap 必为二进浅因子
>    \[
>    \boxed{v_2(H_{\rm sph}-y_3)=1.}
>    \]
> 2. unified tail-root 的二进投影给 exact dichotomy
>    \[
>    \boxed{
>    d\le m+2\mathfrak q+\mathfrak n+\mathfrak g-1
>    }
>    \tag{2-short}
>    \]
>    或
>    \[
>    \boxed{
>    2\mathfrak g=m+\mathfrak q+\ell-2.
>    }
>    \tag{2-balanced}
>    \]
>
> 其中
> \(\mathfrak q=v_2(Q)\)、\(\mathfrak g=v_2(G)\)、
> \(\mathfrak n=v_2(\mathcal N_{12})\)，且
> \[
> \ell=v_2(L)=\begin{cases}1,&\mathfrak q=0,\\0,&\mathfrak q\ge1.\end{cases}
> \]
>
> 在 `Final-5-lock` 上，本文还恢复一个 defect-aware Schmidt budget
> \[
> \boxed{
> (1+a)m+2a\mathfrak q+a\mathfrak n+2\log_{10}\gamma_0
> \le3S+o(S),
> }
> \]
> 其中 \(a=\log_{10}2\)，
> \(\gamma=2^{\mathfrak g}5^{g_5}\gamma_0\)、\((\gamma_0,10)=1\)。
> 这些公式是后续处理 pure/common-scale sheet 的新接口。

---

## 1. 2-adic denominator baseline

仍在旧证明已经严格压出的 canonical funnel：

\[
5\text{-resonance}
+ b_3\text{ 二进 unique maximum}
+t_2=1
+2\text{-resonance}.
\]

记

\[
\mathfrak B:=v_2(b_3),\qquad
\mathfrak q:=v_2(Q),\qquad
\mathfrak g:=v_2(G),\qquad
\mathfrak n:=v_2(\mathcal N_{12}).
\]

`t_2=1` 的定义给

\[
\boxed{v_2(\kappa)=\mathfrak g+1.}
\tag{1.1}
\]

由 tail weight

\[
\kappa b_3=10^mQG
\]

取二进赋值：

\[
\boxed{
\mathfrak B=m+\mathfrak q-1.
}
\tag{B2}

因为 `b_3` 是二进 unique maximum，整数球面中的第三坐标是唯一二进单位坐标；因此

\[
\boxed{v_2(y_3)=v_2(H_{\rm sph})=0.}
\tag{1.2}

令

\[
\omega=(10^m,b_3),\qquad L=10^m/\omega.
\]

由 `(B2)`：

\[
\boxed{
\ell:=v_2(L)
=\begin{cases}
1,&\mathfrak q=0,\\
0,&\mathfrak q\ge1.
\end{cases}}
\tag{ell}

确实，`q=0` 时 `mathfrak B=m-1`，否则 `mathfrak B>=m`。

---

## 2. overlap 参数在 2 处的精确账本

使用 `core.md` 的 overlap 参数：

\[
\eta=(Q,\tau),\quad Q=\eta Q_1,\quad \tau=\eta v,
\]

\[
u=LQ_1,\qquad (LQ_1,v)=1,
\]

以及

\[
D=vc\lambda,\quad C=\lambda w,\quad
g_*=vc\lambda r,
\]

\[
G=\varepsilon vc^2\lambda r.
\]

在当前 funnel 中

\[
u=2\cdot5^TU,\qquad v=V,\qquad (UV,10)=1.
\]

所以

\[
\boxed{v_2(u)=1,\qquad v_2(v)=0.}
\tag{2.1}

由 `u=LQ_1` 与 `(ell)`：

\[
\boxed{v_2(Q_1)=1-\ell.}
\tag{2.2}

又

\[
v_2(\eta)=\mathfrak q-v_2(Q_1)
=\boxed{\mathfrak q-1+\ell.}
\tag{2.3}

`b_3` 二进 unique maximum 时，denominator overlap
\[
g_*=(b_1,b_2)(\operatorname{lcm}(b_1,b_2),b_3)
\]
在 2 处恰恢复 prefix 总深度：

\[
\boxed{v_2(g_*)=\mathfrak g.}
\tag{2.4}

另一方面 `v,c,lambda` 都是二进单位，因此

\[
\boxed{v_2(r)=\mathfrak g.}
\tag{2.5}

最后，

\[
u+v=5^TU+V=2^HZ
\]

且 `epsilon,w` 为二进单位；所以

\[
\boxed{v_2(LQ_1+v)=H,}
\tag{2.6}

\[
LQ_1+2v=2(5^TU+V)=2^{H+1}Z,
\]

故

\[
\boxed{v_2(LQ_1+2v)=H+1.}
\tag{2.7}

---

## 3. sphere 的两个二进因子只能有一个浅因子

令

\[
D_-:=v_2(H_{\rm sph}-y_3).
\]

由 `(1.2)`，`H_sph,y_3` 都是奇数，因此 `H_sph-y_3` 与
`H_sph+y_3` 中恰有一个的二进赋值为 1。

另一方面

\[
y_1^2+y_2^2
=\left(\frac{q_{\rm lcm}}G\right)^2\mathcal N_{12}.
\]

因为 `b_3` 是二进 unique maximum，

\[
v_2(q_{\rm lcm})=\mathfrak B,
\]

所以

\[
\boxed{
R:=v_2(y_1^2+y_2^2)
=2(\mathfrak B-\mathfrak g)+\mathfrak n.
}
\tag{3.1}

sphere factorization

\[
(H_{\rm sph}-y_3)(H_{\rm sph}+y_3)=y_1^2+y_2^2
\]

于是

\[
\boxed{D_-\in\{1,R-1\}.}
\tag{3.2}

又 `H_sph-y_3=La`，所以若记

\[
A_2:=v_2(a),
\]

则

\[
\boxed{D_-=\ell+A_2.}
\tag{3.3}

---

## 4. scale-free quadratic 排除 deep-gap orientation

`core.md` 的 scale-free quadratic 为

\[
\begin{aligned}
0={}&
L c^4\lambda^2r^2w(LQ_1+2v)x^2\\
&-2L c^4\lambda^2r^2v(LQ_1+v)A_{12}10^d x\\
&+\eta^2\mathcal N_{12}Q_1w,
\end{aligned}
\tag{SFQ}
\]

其中

\[
x=\frac{a_0}{\omega},\qquad a=ca_0.
\]

在当前二进位置，`c` 为二进单位，所以

\[
v_2(a_0)=A_2.
\]

而

\[
v_2(\omega)=m-\ell,
\]

故

\[
v_2(x)=A_2-m+\ell.
\tag{4.1}

令 `(SFQ)` 三项赋值依次为 `V_1,V_2,V_3`。使用 §2 的账本及
2-resonance

\[
\boxed{
\mathfrak f+\mathfrak g+3
=2m+2\mathfrak q+\mathfrak n,
}
\tag{2-res}

并且

\[
\mathfrak f=v_2(\kappa+2G)=\mathfrak g+H+1,
\]

可逐项化简为

\[
\boxed{
V_1=2\mathfrak q+\mathfrak n+3\ell-3+2A_2,
}
\tag{4.2}

\[
\boxed{
V_3=2\mathfrak q+\mathfrak n-1+\ell,
}
\tag{4.3}

以及

\[
\boxed{
V_2=d-m+1+2\ell+2\mathfrak g+v_2(A_{12})+A_2.
}
\tag{4.4}

所以

\[
\boxed{V_1-V_3=2(D_--1).}
\tag{4.5}

反设 sphere gap 取深因子：

\[
D_-=R-1>1.
\]

由 `(B2)`、`(3.1)`、`(3.3)` 代回 `(4.4)-(4.3)`，所有 valuation
变量精确消去，得到

\[
\boxed{
V_2-V_3=d+m-1+v_2(A_{12})>0.
}
\tag{4.6}

同时 `(4.5)` 给 `V_1>V_3`。因此 `(SFQ)` 中第三项是唯一最浅项，
三个整数/有理数项不可能相加为零，矛盾。

故只剩浅因子：

\[
\boxed{v_2(H_{\rm sph}-y_3)=1.}
\tag{Shallow-gap}

结合 `(3.3)`：

\[
\boxed{
v_2(a)=1-\ell
=\begin{cases}
0,&\mathfrak q=0,\\
1,&\mathfrak q\ge1.
\end{cases}}
\tag{a2-lock}

这是 exact finite-height conclusion，不使用任何 asymptotic equality ray。

---

## 5. tail-root 的 2-adic exact dichotomy

unified tail-root identity为

\[
\boxed{
\mathscr T a_3
=\kappa G^2 10^dA_{12}
+\eta_0(\kappa+G)W,
}
\tag{5.1}

其中

\[
\mathscr T=\frac{\kappa^2(\kappa+2G)}{10^m},
\qquad \eta_0\in\{\pm1\}.
\]

模 `2^d`：

\[
\boxed{
\mathscr T a_3
\equiv
\eta_0(\kappa+G)W
\pmod{2^d}.}
\tag{Tail-2}

因为 `b_3` 偶且 `(a_3,b_3)=1`，`a_3` 为奇数。

由 `(1.1)`、`(2-res)`：

\[
\boxed{
r_2:=v_2(\mathscr T a_3)
=m+2\mathfrak q+\mathfrak n+\mathfrak g-1.
}
\tag{r2}

现在使用

\[
\Xi=|\mathcal M-C_0a|,
\qquad W=L\Xi,
\]

以及

\[
C_0=LQ\frac{\kappa+2G}{\kappa}.
\]

由 `(a2-lock)` 可得

\[
\boxed{
A:=v_2(C_0a)
=2m+3\mathfrak q+\mathfrak n-2\mathfrak g-3.
}
\tag{5.2}

又 `high-funnel-gap-depth.md` 中的 decimal factorization实际上同时给

\[
\mathcal M=10^d(10^{n_2}b_1y_1+b_2y_2),
\]

所以

\[
\boxed{v_2(\mathcal M)\ge d.}
\tag{5.3}

因此：

- 若 `A<d`，则 `v_2(Xi)=A`；
- 若 `A>=d`，则 `v_2(Xi)>=d`。

并且 `t_2=1` 给 `v_2(kappa+G)=mathfrak g`。

若 `d<=r_2`，直接得到第一支

\[
\boxed{d\le m+2\mathfrak q+\mathfrak n+\mathfrak g-1.}
\tag{2-short}

现在设 `d>r_2`。`Tail-2` 要求右边也有恰好 `r_2<d` 的 valuation；
故不可能处在 `A>=d`，只能 `A<d`，而且

\[
r_2
=\mathfrak g+\ell+A.
\]

代入 `(r2)` 与 `(5.2)`：

\[
\boxed{2\mathfrak g=m+\mathfrak q+\ell-2.}
\tag{2-balanced}

因此 `(2-short)` 与 `(2-balanced)` 穷尽当前 funnel。

---

## 6. Schmidt lower bound 的 defect-aware 重写

写 gcd-normal form

\[
\kappa=\gamma u,\qquad G=\gamma v,
\]

以及 `t_2=1` S-unit phase

\[
u=2\cdot5^TU,\qquad v=V,
\]

\[
5^TU+V=2^HZ.
\]

再写

\[
\boxed{
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0,
\qquad (\gamma_0,10)=1.
}
\tag{6.1}

由 decimal pinning

\[
\log_{10}\kappa=2S+O(1),
\qquad
\log_{10}(\kappa+2G)=2S+O(1).
\]

而

\[
\kappa=2\gamma5^TU,
\]

\[
\kappa+2G=2\gamma2^HZ.
\]

所以

\[
\begin{aligned}
\log_{10}U+\log_{10}Z
={}&4S-2\log_{10}\gamma-aH-bT+O(1),
\end{aligned}
\tag{6.2}

其中常数 `-2a` 已吸收到 `O(1)`。

二进 resonance给

\[
H=2m+2\mathfrak q+\mathfrak n-2\mathfrak g-4,
\tag{6.3}

五进 resonance给

\[
3T=2m+2q_5-2g_5+n_5.
\tag{6.4}

将 `(6.1)`–`(6.4)` 代回 `(6.2)`，`mathfrak g` 完全消去，得到

\[
\boxed{
\begin{aligned}
\log_{10}U+\log_{10}Z
={}&4S
-\frac{2(1+2a)}3m\\
&-(2a\mathfrak q+a\mathfrak n)
-\frac b3(2q_5+4g_5+n_5)\\
&-2\log_{10}\gamma_0+O(1).
\end{aligned}}
\tag{UZ-exact-height}

旧固定目标 Schmidt Subspace Theorem 对整个该 S-unit funnel给

\[
\liminf\frac{\log_{10}U+\log_{10}Z}{S}\ge1.
\]

因此任何无界 sequence 满足

\[
\boxed{
\frac{2(1+2a)}3m
+2a\mathfrak q+a\mathfrak n
+\frac b3(2q_5+4g_5+n_5)
+2\log_{10}\gamma_0
\le3S+o(S).
}
\tag{Subspace-defect}

在 [`high-funnel-denominator-max-lock.md`](high-funnel-ledger.md#source-high-funnel-denominator-max-lock) 的
`Final-5-lock`

\[
m=2q_5+4g_5+n_5
\]

上，它进一步化成

\[
\boxed{
(1+a)m
+2a\mathfrak q+a\mathfrak n
+2\log_{10}\gamma_0
\le3S+o(S).
}
\tag{Subspace-Final5}

这比此前只保留 multiplicative height 的 `Combined-height` 在该 sheet 上更强。

---

## 7. `Final-5` 上的两个 sector diagnostics

以下只是当前 sheet 的显式诊断，不替代仓库已经更强的全局非有效
`limsup < 6.308883...`。

### 7.1 整个 `Final-5` sheet 的粗 bound

由 small-factor upper 与 exact

\[
v_2(F_-)=\mathfrak f+1,\qquad v_5(F_-)=k_5=m-g_5
\]

可直接得到

\[
\boxed{
n
<4S+b m
-2a\mathfrak q-a\mathfrak n
+a\mathfrak g+b g_5+O(1).
}
\tag{Raw-F}

又 `G=gamma V` 且 `V>=1`，故

\[
\boxed{
a\mathfrak g+b g_5+\log_{10}\gamma_0\le S+O(1).}
\tag{Gamma-height}

代入 `(Raw-F)`：

\[
n<5S+b m-2a\mathfrak q-a\mathfrak n-\log_{10}\gamma_0+O(1).
\]

再用 `(Subspace-Final5)`，丢掉非负 defect，得到

\[
\boxed{
\limsup_{\rm Final5}\frac nS
\le
5+\frac{3b}{1+a}
=
\frac{8+2a}{1+a}
=6.611730721041\ldots.
}
\tag{Final5-coarse}

这个数值高于已有全 DD strict limsup bound，因此它的意义是
`Final-5` sheet 的内部收费结构，不是新的全局常数。

### 7.2 `2-balanced` sector

由 `(2-balanced)`：

\[
\mathfrak g=\frac12m+\frac12\mathfrak q+O(1).
\]

代回 `(Raw-F)`：

\[
n
<4S+\left(1-\frac a2\right)m
-\frac{3a}{2}\mathfrak q-a\mathfrak n
+b g_5+O(1).
\]

`Final-5-lock` 给

\[
4g_5\le m.
\]

所以

\[
n
<4S+rac{5-3a}{4}m+O(1)
\]

（继续丢掉非正 defect）。再用 `(Subspace-Final5)`：

\[
\boxed{
\limsup_{\rm Final5,\,2-balanced}
\frac nS
\le
4+\frac{3(5-3a)}{4(1+a)}
=
\frac{31+7a}{4(1+a)}
=6.361730721041\ldots.
}
\tag{Balanced-sector}

同样，这个 sector 数值仍高于仓库已有的全局 strict `6.308883...`，
所以不能被宣传为新的 DD 全局 bound。

---

## 8. pure common-scale endpoint 的额外 exact shape

`Final-5-lock` 的 LP endpoint为

\[
q_5=n_5=0,\qquad m=4g_5,\qquad T=2g_5.
\]

此时 `Q=b_1 10^{m_2}+b_2` 是 5-unit，而

\[
v_5(b_1)+v_5(b_2)=g_5.
\]

因为第一项 `b_1 10^{m_2}` 具有正 5-depth（若 `g_5>0`），要使 `Q`
为 5-unit，必须

\[
\boxed{v_5(b_1)=g_5,\qquad v_5(b_2)=0.}
\tag{Pure-denominator5}

从 reduced-tail identities

\[
u=2\cdot5^TU,\qquad Q=Uq,\qquad ut=10^mQ,\qquad b_3=Vt
\]

还得到 exact

\[
\boxed{
b_3=2^{m-1}5^{m-T}qV.}
\tag{b3-reduced}

因为 `b_3` 恰有 `m` 位：

\[
10^{m-1}\le b_3<10^m.
\]

除以 `(b3-reduced)` 的 smooth factor可得

\[
\boxed{
bT+a-1\le\log_{10}(qV)<bT+a.}
\tag{qV-window}

特别地 pure common-scale 中

\[
\boxed{
\log_{10}(qV)=\frac b2m+O(1).
}
\tag{Pure-qV}

这说明剩余 rough denominator freedom并非任意；`qV` 本身被锁在一个固定高度窗口。

---

## 9. 当前边界

本文新增的 `Shallow-gap` 与 `2-short/2-balanced` 是 exact finite-height
结构。它们把最后 high-funnel sheet 的二进自由度压成了两个明确状态。

目前还不能据此宣布 DD closure，也不能给出低于既有 global strict
`6.308883...` 的显式常数。下一步应优先处理：

1. `2-short` 中 `q,V,gamma_0` 的 rough-height allocation；
2. `2-balanced` 中 pure common-scale 的 deep 5-adic unit cancellation；
3. 将 `(qV-window)` 与 `u(u+2v)|F_-Q` 的大除数连接，寻找不能由 `q` 支付的 `Z`-rough mass。

---

<a id="source-high-funnel-two-balanced-collapse"></a>

> 整合来源：`high-funnel-two-balanced-collapse.md`

# DD `Final-5-lock` 上的 `2-balanced` sector collapse

> **依赖：** [`high-funnel-exact-small-factor-normalization.md`](high-funnel-ledger.md#source-high-funnel-exact-small-factor-normalization)、
> [`high-funnel-two-adic-balance.md`](high-funnel-ledger.md#source-high-funnel-two-adic-balance)、
> [`high-funnel-denominator-max-lock.md`](high-funnel-ledger.md#source-high-funnel-denominator-max-lock)、
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

---

<a id="source-high-funnel-xi-depth"></a>

> 整合来源：`high-funnel-xi-depth.md`

# DD high-funnel `Defect-heavy` slack 的 canonical `Xi`-depth

> **依赖：** [`high-funnel-five-adic-dichotomy.md`](high-funnel-ledger.md#source-high-funnel-five-adic-dichotomy)、[`high-funnel-defect-optimization.md`](high-funnel-ledger.md#source-high-funnel-defect-optimization)、`global-framework.md` 的 unified discriminant、`core.md` §18 的 `W=L Xi`。
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

---

# DD `Final-5` 的 `25/4` equality-ray rigidity

> **依赖：** [`high-funnel-final5-two-adic-optimization.md`](high-funnel-final5-two-adic-optimization.md)、
> [`high-funnel-fminus-sunit-factorization.md`](high-funnel-fminus-sunit-factorization.md)、
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
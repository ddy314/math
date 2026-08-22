# DD corrected terminal neighborhood 的 square-source CRT

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-high-funnel-quantitative-defect-2026-08-22.md`](dd-corrected-high-funnel-quantitative-defect-2026-08-22.md)、[`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)、[`dd-corrected-terminal-rough-source-sharp-2026-08-22.md`](dd-corrected-terminal-rough-source-sharp-2026-08-22.md)、[`core.md`](core.md) §§31, 37--38 的 denominator overlap / primitive normalization。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` terminal neighborhood）。**
>
> 本文补上此前 sharp rough-source theorem 留下的核心代数桥。构造一个整个 canonical neighborhood 中都存在的 rough integer `q_Q`，证明：
>
> \[
> \boxed{\log_{10}q_Q\ge(z_*-\delta)S-o(S),}
> \]
>
> \[
> \boxed{q_Q^2\mid
> Lv\omega10^dA_{12}+a_3(LQ_1+2v),}
> \]
>
> 且 `(q_Q,v)=1`。因此 `q_Q^2` 本身就是一个 coefficients fixed、对 `A_12` 系数可逆的 neighborhood-valid source period。它不再依赖 equality-only `q_c` normalization。

---

## 1. canonical source quotient 与 normalized overlap

沿用 canonical `t_2=1` phase

\[
\kappa=2\gamma5^TU,
\qquad
Q=Uq,
\qquad
G=\gamma V,
\qquad
(UV,10)=1,
\qquad
(U,V)=1.
\tag{1.1}
\]

统一尾权

\[
\kappa=\frac{10^mQG}{b_3}
\]

给出上一文件的 exact third-denominator factorization

\[
\boxed{b_3=BVq,}
\qquad
\boxed{B:=\frac{10^m}{2\cdot5^T}.}
\tag{1.2}
\]

另一方面 general denominator overlap 定义

\[
g_*=(b_1,b_2)(\operatorname{lcm}(b_1,b_2),b_3),
\]

并令

\[
c_3=\frac{q_{\rm lcm}}{b_3}.
\]

`core.md` §31 给

\[
\boxed{g_*=\frac G{c_3}.}
\tag{1.3}
\]

因为 `G=gamma V`，定义 normalized overlap

\[
\boxed{\widehat g:=\frac{g_*}{V}=\frac\gamma{c_3}\in\mathbf Z_{>0}.}
\tag{1.4}
\]

`core.md` §37 的 overlap parameterization 进一步写

\[
\boxed{g_*=vc\lambda r,}
\tag{1.5}
\]

而 canonical reduced-tail variable `v` 正是 `V`，故

\[
\boxed{\widehat g=c\lambda r,}
\qquad
\boxed{c\mid\widehat g.}
\tag{1.6}
\]

这里的 `lambda` 是 §37 的整数 overlap parameter；它与 quantitative defect 中的实常数 `lambda=(2+log10 2)/(1+2log10 2)` 不是同一个局部符号。本文在涉及 quantitative constant 时一律写 `lambda_*`。

---

## 2. generic sphere-source identity

整数球面给

\[
(H_{\rm sph}-y_3)(H_{\rm sph}+y_3)
=y_1^2+y_2^2.
\tag{2.1}
\]

而

\[
y_i=a_i\frac{q_{\rm lcm}}{b_i}
\]

故

\[
y_1^2+y_2^2
=\left(\frac{q_{\rm lcm}}G\right)^2\mathcal N_{12}.
\tag{2.2}
\]

由 `(1.3)`：

\[
\frac{q_{\rm lcm}}G=\frac{b_3}{g_*}.
\]

再代入 `(1.2)` 与 `(1.4)`：

\[
\frac{b_3}{g_*}
=\frac{BVq}{V\widehat g}
=\frac{Bq}{\widehat g}.
\]

所以得到 exact identity

\[
\boxed{
\widehat g^{\,2}
(H_{\rm sph}-y_3)(H_{\rm sph}+y_3)
=B^2q^2\mathcal N_{12}.
}
\tag{Sphere-source}
\]

这条式子只使用 canonical funnel、denominator overlap 和整数球面；没有使用 equality terminal `q_c,C_L,R_0,L_clean`。

---

## 3. 逐素数 square-source extraction

固定任意 `p\nmid10`，记

\[
s_p:=v_p(q),
\qquad
h_p:=v_p(\widehat g),
\]

\[
a_p:=v_p(H_{\rm sph}-y_3),
\qquad
n_p:=v_p(\mathcal N_{12}),
\qquad
c_p:=v_p(c).
\]

由 `(Sphere-source)`：

\[
\boxed{
v_p(H_{\rm sph}+y_3)
=2s_p+n_p-2h_p-a_p.}
\tag{3.1}
\]

定义

\[
\boxed{
f_p:=
\max\left(
 s_p-h_p-\left\lceil\frac{a_p}{2}\right\rceil
       -\left\lceil\frac{c_p}{2}\right\rceil,
 0
\right).}
\tag{3.2}
\]

以及 rough square-source reader

\[
\boxed{q_Q:=\prod_{p\nmid10}p^{f_p}.}
\tag{3.3}
\]

若 `f_p>0`，则

\[
\begin{aligned}
2f_p
&\le
2s_p-2h_p
-2\left\lceil\frac{a_p}{2}\right\rceil
-2\left\lceil\frac{c_p}{2}\right\rceil\\
&\le2s_p-2h_p-a_p-c_p\\
&\le v_p(H_{\rm sph}+y_3)-c_p,
\end{aligned}
\]

其中最后一步使用 `n_p>=0` 与 `(3.1)`。因此

\[
\boxed{q_Q^2\mid\frac{H_{\rm sph}+y_3}{c}.}
\tag{Square-source}
\]

这就是此前缺失的 neighborhood square-source theorem。

---

## 4. `q_Q` 与 moving core `V` 严格互素

固定 `p\mid V`, `p\nmid10`。general moving-prime theorem 给 denominator pair-max pattern。以 `(b_2,b_3)` pair-max 为例，写

\[
v_p(b_1)=r<E=v_p(b_2)=v_p(b_3).
\]

由于

\[
Q=b_1 10^{m_2}+b_2
\]

两项 p-depth 分别为 `r,E`，故

\[
v_p(Q)=r.
\]

又

\[
t=(10^mQ,b_3)
\]

在 `p` 处深度也是 `r`，所以 reduced-tail numerator `u=10^mQ/t` 为 p-unit。canonical `u=2*5^T U` 因而给 `p\nmid U`，故

\[
\boxed{s_p=v_p(q)=r.}
\tag{4.1}
\]

另一方面

\[
v_p(G)=E+r,
\qquad
v_p(V)=E-r,
\]

所以由 `G=gamma V`：

\[
v_p(\gamma)=2r.
\]

此时 `c_3=q_lcm/b_3` 为 p-unit，因此

\[
\boxed{h_p=v_p(\widehat g)=2r.}
\tag{4.2}
\]

于是 `(3.2)` 中

\[
s_p-h_p=r-2r\le0,
\]

所以 `f_p=0`。另一 pair-max orientation 完全相同。

因此

\[
\boxed{(q_Q,V)=1.}
\tag{Source-moving-transverse}
\]

特别地，由 quantitative one-channel 的 `v_2|V`：

\[
\boxed{(q_Q,v_2)=1.}
\tag{4.3}
\]

这比此前只知道 `gcd(q_rough,v_2)|b_1` 更强；square-source extraction 自动删除了所有 moving pair-max overlap。

---

## 5. `q_Q^2` 直接产生 generic fixed `A_12` congruence

使用 `core.md` §37--38 的 overlap parameterization：

\[
Q=\eta Q_1,
\qquad
\tau=\eta v,
\qquad
u=LQ_1,
\qquad
u+v=\varepsilon w,
\]

\[
c_3=\varepsilon c.
\tag{5.1}
\]

primitive system 为

\[
\boxed{
\omega\varepsilon A_{12}10^d
-\lambda Q_1H_0=a_0,
}
\tag{5.2}
\]

\[
\boxed{
\lambda vH_0-a_3\varepsilon=La_0.
}
\tag{5.3}
\]

并已有 elimination

\[
\boxed{
v\omega A_{12}10^d-a_3Q_1=wa_0.}
\tag{5.4}
\]

sphere scale satisfies

\[
H_{\rm sph}=DH_0=vc\lambda H_0,
\]

而

\[
y_3=a_3\frac{q_{\rm lcm}}{b_3}=a_3c_3=a_3\varepsilon c.
\]

故由 `(5.3)`：

\[
\begin{aligned}
\frac{H_{\rm sph}+y_3}{c}
&=\lambda vH_0+a_3\varepsilon\\
&=La_0+2a_3\varepsilon.
\end{aligned}
\tag{5.5}
\]

乘以 `w`，使用 `(5.4)` 与

\[
\varepsilon w=LQ_1+v,
\]

得到 exact parent

\[
\boxed{
w\frac{H_{\rm sph}+y_3}{c}
=Lv\omega A_{12}10^d
+a_3(LQ_1+2v).}
\tag{Generic-Q-parent}
\]

由 `(Square-source)`：

\[
\boxed{
q_Q^2\mid
Lv\omega A_{12}10^d
+a_3(LQ_1+2v).}
\tag{5.6}
\]

又 `q_Q` 只含非十进制素数，`L,omega,10` 都是 2/5-smooth；而 `(q_Q,v)=1`。因此 `A_12` coefficient 是模 `q_Q^2` 的 unit：

\[
\boxed{
Lv\omega10^d A_{12}
\equiv
-a_3(LQ_1+2v)
\pmod{q_Q^2}.}
\tag{Generic-QCRT}
\]

这是 equality `q_c^2` QCRT 的 neighborhood-valid 替代，而且不需要预先识别 `q/q_c=J theta`。

---

## 6. rough gap 本身进入 quantitative defect

令

\[
\boxed{
P_{\rm gap}:=
\frac1S\log_{10}\operatorname{core}_{10}(H_{\rm sph}-y_3).}
\tag{6.1}
\]

corrected exact small-factor factorization为

\[
F_-=2^{H+1}Z(H_{\rm sph}-y_3)\widehat g.
\tag{6.2}
\]

`dd-corrected-high-funnel-schmidt-2026-08-22.md` 中的 lower bound只读取了 sphere gap 的 forced 5-adic baseline，而把其它正因子丢掉。保留 `(6.1)` 的 rough part 后，同一推导把 `Corrected-stability` 的右端再减去 `P_gap`。

因此 `dd-corrected-high-funnel-quantitative-defect-2026-08-22.md` 的最终 defect inequality可加强为

\[
\boxed{
\begin{aligned}
\delta\ge{}&
\lambda_*\sigma_S
+2a\lambda_*Q_2+a\lambda_*N_2\\
&+\frac{2b(\lambda_*+1)}3Q_5
+\frac{2b(2\lambda_*-1)}3G_5\\
&+\frac{b(\lambda_*+1)}3N_5
+(2\lambda_*-1)R
+P_{\rm gap}
-o(1),
\end{aligned}}
\tag{Gap-augmented-defect}
\]

其中

\[
a=\log_{10}2,
\qquad b=1-a,
\qquad
\lambda_*:=\frac{2+a}{1+2a}.
\]

特别地

\[
\boxed{P_{\rm gap}\le\delta+o(1).}
\tag{6.3}
\]

---

## 7. `q_Q` 的 sharp neighborhood height

上一 sharp rough-source theorem在优化前给

\[
\begin{aligned}
\frac{\log q_{\rm rough}}S-z_*
={}&-\frac{2b}{3}\mu
-aQ_2-\frac b3Q_5\\
&+\frac b3G_5+\frac b3N_5+aG_2+R+o(1),
\end{aligned}
\tag{7.1}
\]

其中

\[
\mu=M_*-M.
\]

由 `(3.2)`，使用

\[
\left\lceil\frac{k}{2}\right\rceil\le k
\quad(k\in\mathbf Z_{\ge0}),
\]

得到 logarithmic lower

\[
\log q_Q
\ge
\log q_{\rm rough}
-\log\operatorname{core}_{10}(\widehat g)
-\log\operatorname{core}_{10}(H_{\rm sph}-y_3)
-\log\operatorname{core}_{10}(c).
\tag{7.2}
\]

因为

\[
\widehat g=\gamma/c_3,
\qquad c\mid\widehat g,
\]

故

\[
\frac1S\log\operatorname{core}_{10}(\widehat g)\le R,
\qquad
\frac1S\log\operatorname{core}_{10}(c)\le R.
\tag{7.3}
\]

`(7.1)` 中原有 `+R`，所以代入 `(7.2)--(7.3)` 后，安全 loss 为

\[
\mathcal L_Q
:=\frac{2b}{3}\mu+aQ_2+\frac b3Q_5+R+P_{\rm gap}.
\tag{7.4}
\]

Schmidt exact slack identity给

\[
A\mu
=\sigma_S+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)+2R+o(1),
\]

其中

\[
A=\frac{2(1+2a)}3.
\tag{7.5}
\]

把 `(7.5)` 代入 `(7.4)`。相对于 `(Gap-augmented-defect)`，各 variable 的 loss/cost ratio分别为

\[
\begin{array}{c|c}
\sigma_S&0.3037639690\ldots\\
Q_2&0.6518819845\ldots\\
N_2&0.3037639690\ldots\\
Q_5&0.3843108934\ldots\\
G_5&0.4659800029\ldots\\
N_5&0.1790811912\ldots\\
R&1\\
P_{\rm gap}&1
\end{array}
\]

最大值恰为 `1`。所有变量共用同一份 defect budget，故

\[
\boxed{\mathcal L_Q\le\delta+o(1).}
\tag{7.6}
\]

最终：

\[
\boxed{
\frac{\log_{10}q_Q}{S}
\ge z_*-\delta-o(1),
\qquad
z_*=0.308883577618031\ldots.}
\tag{Square-source-height}
\]

这条 coefficient `1` 已把 overlap、sphere-gap rough part 与 source smooth loss统一计入；不能再分别把同一份 defect budget重复相加。

---

## 8. 与 quantitative one-channel 的联合容量

quantitative one-channel theorem给

\[
\frac{\log_{10}v_2}{S}
\ge1-C_{\rm one}\delta-o(1),
\]

\[
C_{\rm one}=2.335049992773302\ldots.
\tag{8.1}
\]

由 `(4.3)`：

\[
(q_Q,v_2)=1.
\]

因此两个 periods 的 lcm 不再损失任何 source/pair-max overlap：

\[
\boxed{
\frac1S\log_{10}(q_Q^2v_2)
\ge
1+2z_*-(2+C_{\rm one})\delta-o(1).}
\tag{8.2}
\]

即

\[
\boxed{
\frac1S\log_{10}(q_Q^2v_2)
\ge
1.617767155236062\ldots
-4.335049992773302\ldots\delta-o(1).}
\tag{8.3}
\]

纯高度上，该联合 modulus严格超过一个 `S`-height prefix window，只要

\[
\boxed{
\delta<
\frac{2z_*}{2+C_{\rm one}}
=0.142505197464\ldots.}
\tag{8.4}
\]

`(8.4)` 仍不是 slope gap theorem，因为第二个 `v_2` period 还需要把 equality frontier 的 `Pairmax-GCRT0` 逐项移植到 quantitative neighborhood。但此前最关键的 source-square bridge已经在本文完成。

---

## 9. 状态摘要

- **已严格完成：** `Sphere-source`。
- **已严格完成：** canonical rough square reader `q_Q` 与 `Square-source`。
- **已严格完成：** `Source-moving-transverse`，故 `q_Q` 与整个 moving core `V` 互素。
- **已严格完成：** generic exact parent `Generic-Q-parent` 与 fixed source period `Generic-QCRT`。
- **已严格完成：** `Gap-augmented-defect`。
- **已严格完成：** `Square-source-height`, coefficient `1`。
- **capacity：** source-square × one-channel pair-max 的潜在联合 period可保持超 `S` 高度到 `delta<0.142505197464...`。
- **下一核心：** 将 split-independent `Pairmax-GCRT0` 从 equality `C_L` normalization移植到 quantitative one-channel `v_2`，并精确审计其 coefficient exceptional mass。
- **仍未证明：** explicit global slope gap、DD emptiness、effective absolute height bound。

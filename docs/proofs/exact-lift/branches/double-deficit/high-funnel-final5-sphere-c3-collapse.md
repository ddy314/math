# DD `Final-5` 的 sphere–`c_3` collapse

> **依赖：** [`high-funnel-denominator-max-lock.md`](high-funnel-denominator-max-lock.md)、
> [`high-funnel-two-adic-balance.md`](high-funnel-two-adic-balance.md)、
> [`high-funnel-fminus-sunit-factorization.md`](high-funnel-fminus-sunit-factorization.md)、
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
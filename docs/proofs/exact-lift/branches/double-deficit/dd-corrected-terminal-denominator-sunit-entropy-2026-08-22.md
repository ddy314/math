# DD corrected terminal 的 denominator / S-unit entropy bound

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-schmidt-farey-slack-2026-08-22.md`](dd-corrected-schmidt-farey-slack-2026-08-22.md)、[`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)、[`dd-corrected-terminal-rough-source-sharp-2026-08-22.md`](dd-corrected-terminal-rough-source-sharp-2026-08-22.md)、[`dd-corrected-gap-fiber-pairmax-rational-reconstruction-2026-08-22.md`](dd-corrected-gap-fiber-pairmax-rational-reconstruction-2026-08-22.md)。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` terminal neighborhood 的 quantitative counting consequence）。**
>
> 前一 gap-fiber theorem 已把 fixed denominator/S-unit data 上的 numerator entropy 压到
> \[
> 10^{[C_{UV}\delta-U_*]_+S+o(S)}
> \]
> （并在 `delta<delta_UV` 时压到 `10^{o(S)}`）。本文处理当时留下的 denominator/S-unit family 本身。
>
> 关键点是：不能把 `gamma` 的整个 logarithmic height 当作 candidate entropy。写
> \[
> \gamma=2^{\mathfrak g}5^{g_5}\gamma_0,
> \]
> 则 `2,5` 两个指数只有多项式多种选择；真正指数级移动只来自 rough core `gamma_0`，其 entropy 是 `R S`。另一方面
> \[
> G=b_1b_2=\gamma V,
> \qquad
> V=v_1v_2,
> \qquad
> v_i\mid b_i,
> \]
> 说明固定 `V,gamma` 后，`b_1,b_2` 的剩余选择只是 `V` 与 `gamma` 的 divisor assignments，因此统一只有 `10^{o(S)}` 种。
>
> 最终 denominator/S-unit family 的正线性 entropy 只剩
> \[
> \boxed{\sigma_S+R,}
> \]
> 而 quantitative defect 同时收费
> \[
> \delta\ge\lambda\sigma_S+(2\lambda-1)R-o(1).
> \]
> 由于 `2lambda-1>lambda`，得到
> \[
> \boxed{\sigma_S+R\le\delta/\lambda+o(1).}
> \]

---

## 1. 记号与 slope window

令

\[
a:=\log_{10}2,
\qquad
\lambda:=\frac{2+a}{1+2a}
=1.436294525872677\ldots,
\]

\[
c_*:=2+3\lambda
=6.308883577618031\ldots.
\]

对单个 candidate 写

\[
\delta':=c_*-\frac nS\ge0.
\]

为便于做统一计数，固定一个常数 `delta_0`，考虑 terminal window

\[
\boxed{0\le\delta'\le\delta_0.}
\tag{1.1}
\]

下文所有 `o(S)` 对 fixed `delta_0` 一致理解。

Schmidt/Farey slack 为 `sigma_S`，rough overlap height 为

\[
R:=\frac1S\log_{10}\gamma_0,
\qquad
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0,
\qquad
(\gamma_0,10)=1.
\]

quantitative defect theorem 给

\[
\boxed{
\delta'
\ge
\lambda\sigma_S
+(2\lambda-1)R
+\text{其它非负 charged terms}
-o(1).}
\tag{1.2}

并且

\[
2\lambda-1
=1.872589051745354\ldots
>\lambda.
\tag{1.3}

因此立即有

\[
\boxed{
\sigma_S+R
\le\frac{\delta'}{\lambda}+o(1)
\le\frac{\delta_0}{\lambda}+o(1).}
\tag{Shared-entropy-budget}

其中

\[
\boxed{
\frac1\lambda
=\frac{1+2a}{2+a}
=0.696236030971719\ldots.}
\tag{1.4}

---

## 2. Farey side 只支付 `sigma_S S`

canonical S-unit equation为

\[
\boxed{2^HZ-5^TU=V,}
\tag{2.1}

且

\[
(U,Z)=1.
\]

`dd-corrected-schmidt-farey-slack-2026-08-22.md` 已证明

\[
\left|\frac ZU-\frac{5^T}{2^H}\right|
=
\frac{10^{\sigma_SS+o(S)}}{U^2}.
\tag{2.2}

因此在 fixed smooth/exponent fiber 中，Farey separation 给 projective rational candidates

\[
\boxed{
N_{UZ}
\le10^{\sigma_SS+o(S)}.}
\tag{2.3}

这里保留 candidate-specific `sigma_S`，而不先粗化成 `delta_0/lambda`。

`H,T` 以及 terminal 中所有 digit lengths / valuation exponents 都是 `O(S)` 的非负整数；固定有限个这类坐标只产生

\[
S^{O(1)}=10^{o(S)}
\]

个 combinatorial/exponent fibers。若 `sigma_S` 在 window 内移动，可按宽 `1/S` 的区间分层；层数仍为 `S^{O(1)}`，不会改变正线性 exponent。

所以 Farey/projective side 的全部正线性 counting cost 就是

\[
\boxed{\sigma_SS.}
\tag{2.4}

---

## 3. `gamma` 的 candidate entropy 只有 rough part `R S`

写

\[
\boxed{
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0.}
\tag{3.1}

对 fixed `S,delta_0`，terminal normalized valuation bounds保证

\[
\mathfrak g,g_5=O(S).
\]

所以 smooth exponents `(mathfrak g,g_5)` 只有 `S^{O(1)}` 种。

固定一个 `R`-layer 后，

\[
1\le\gamma_0\le10^{RS+o(S)},
\]

故最粗的整数计数已经给

\[
\boxed{
N_{\gamma}
\le10^{RS+o(S)}.}
\tag{3.2}

特别地，不应使用

\[
10^{(\log\gamma) }
\]

去枚举 `gamma`：其中 `2^{mathfrak g}` 与 `5^{g_5}` 的巨大数值高度来自两个指数坐标，而不是指数多种独立整数选择。

---

## 4. 固定 `V,gamma` 后 denominator factorization 只有 `10^{o(S)}` 种

quantitative one-channel decomposition给 exact

\[
\boxed{V=v_1v_2,}
\tag{4.1}

其中

\[
v_1\mid b_1,
\qquad
v_2\mid b_2.
\]

又 canonical denominator product 为

\[
\boxed{G=b_1b_2=\gamma V.}
\tag{4.2}

定义整数

\[
t_1:=b_1/v_1,
\qquad
t_2:=b_2/v_2.
\]

由 `(4.1)--(4.2)` exact 地得到

\[
\boxed{t_1t_2=\gamma.}
\tag{4.3}

因此固定 `V,gamma` 后，所有可能的 `(b_1,b_2)` 都来自

\[
v_1v_2=V,
\qquad
t_1t_2=\gamma,
\]

再令

\[
\boxed{b_1=v_1t_1,
\qquad b_2=v_2t_2.}
\tag{4.4}

ordered factor assignments 的数目至多

\[
\tau(V)\tau(\gamma).
\]

terminal heights 给

\[
\log V,\log\gamma=O(S).
\]

由标准 divisor bound

\[
\log\tau(N)=O\left(\frac{\log N}{\log\log N}\right)
=o(S)
\qquad(N\le10^{O(S)}),
\]

所以统一有

\[
\boxed{
\tau(V)\tau(\gamma)=10^{o(S)}.}
\tag{4.5}

这一步同时吸收了：

- small/large channel 的 prime assignment；
- `b_2/v_2` 的 cofactor freedom；
- `b_1/v_1` 的 cofactor freedom。

它们不再各自支付 `O(delta S)` 的 raw interval entropy。

---

## 5. 其余 denominator/source data 随后被 exact reconstruction 固定

固定 digit lengths，特别是 `m_2` 后，prefix concat 为

\[
\boxed{Q=b_1 10^{m_2}+b_2.}
\tag{5.1}

canonical phase又有

\[
\boxed{Q=Uq.}
\tag{5.2}

所以固定 `(U,b_1,b_2,m_2)` 后：

- 若 `U` 不整除 `Q`，该 factor assignment 不合法；
- 若整除，则
  \[
  \boxed{q=Q/U}
  \]
  唯一。

同时

\[
\boxed{B=\frac{10^m}{2\cdot5^T}}
\tag{5.3}

由 `(m,T)` 唯一，而 exact third-denominator factorization

\[
\boxed{b_3=BVq}
\tag{5.4}

进一步唯一恢复 `b_3`。

因此在 fixed combinatorial/exponent fiber 中：

1. Farey candidate `(U,Z)` 决定
   \[
   V=2^HZ-5^TU;
   \]
2. `gamma_0` 与 smooth exponents决定 `gamma`；
3. `(V,gamma)` 只有 `10^{o(S)}` 个 factor assignments；
4. 每个 assignment 之后 `b_1,b_2,Q,q,B,b_3` 全部由 exact formulas 决定或被 integrality/digit-length test 淘汰。

所以 denominator/S-unit data 本身没有其它 positive-linear candidate entropy。

---

## 6. denominator / S-unit family 的总 entropy bound

由 §§2--5，在一个 fixed `(sigma_S,R)` layer 内：

\[
N_{\rm den/SU}
\le
10^{(\sigma_S+R)S+o(S)}.
\tag{6.1}

再用 `(Shared-entropy-budget)`：

\[
\boxed{
N_{\rm den/SU}(S;\delta_0)
\le
10^{(\delta_0/\lambda)S+o(S)}.}
\tag{Den-SU-entropy}

数值即

\[
\boxed{
N_{\rm den/SU}(S;\delta_0)
\le
10^{0.696236030972\,\delta_0 S+o(S)}.}
\tag{6.2}

这比逐项把 `gamma`、`v_1`、`b_2/v_2` 的 raw height 都当成独立 entropy 的估计严格更强；关键改进来自 **smooth valuation coordinates 只按指数枚举** 与 **factor assignment 只花 divisor entropy**。

---

## 7. 与 gap-lattice numerator theorem 合并

前一 theorem 在

\[
\delta_0<\delta_{\rm gap}
=0.299845580176277\ldots
\]

时，对 fixed denominator/S-unit data 给

\[
N_{\rm num}
\le
10^{[C_{UV}\delta_0-U_*]_+S+o(S)},
\tag{7.1}

其中

\[
C_{UV}=2+3a
=2.903089986991944\ldots,
\]

\[
U_*=0.691116422381969\ldots.
\]

乘上 `(Den-SU-entropy)`，得到整个 corrected canonical terminal window 的 quantitative candidate count：

\[
\boxed{
N_{\rm term}(S;\delta_0)
\le
10^{\left[
\frac{\delta_0}{\lambda}
+[C_{UV}\delta_0-U_*]_+
\right]S+o(S)}
\qquad(\delta_0<\delta_{\rm gap}).}
\tag{Terminal-global-count}

特别地

\[
\delta_{UV}
:=\frac{U_*}{C_{UV}}
=0.238062349248111\ldots
<\delta_{\rm gap},
\]

所以在整个 `U × v_2` uniqueness neighborhood 中：

\[
\boxed{
N_{\rm term}(S;\delta_0)
\le
10^{(\delta_0/\lambda)S+o(S)}
=
10^{0.696236030972\,\delta_0S+o(S)}
\qquad(\delta_0<\delta_{UV}).}
\tag{Terminal-near-frontier-sparsity}

当 `delta_0 -> 0` 时恢复

\[
\boxed{N_{\rm term}(S;\delta_0)=10^{o(S)}}
\]

的 frontier-scale sparsity；现在还得到一个显式正宽度 quantitative continuation。

---

## 8. 这仍不是 strict slope gap

`Terminal-global-count` 是全局 candidate sparsity，不是 emptiness theorem。

即使 exponent

\[
\frac{\delta_0}{\lambda}
\]

很小，只要 `delta_0>0`，它仍允许指数多 candidates。当前还缺一个真正独立的 Archimedean/digit-shell exclusion，把这些 surviving denominator/S-unit candidates 与

\[
Ua_3\bmod10^d=10^d-R_{\rm dec}
\]

的 exponentially thin top-residue cell 做不相容比较。

因此安全结论是：

\[
\boxed{
\text{terminal denominator/S-unit entropy 已量化闭合到 }\delta/\lambda;
\text{ 下一核心是 surviving global candidates 的 digit-shell exclusion。}
}
\]

不据此宣称

\[
\limsup n/S<c_*,
\]

也不宣称 DD emptiness 或 effective absolute height bound。

---

## 9. verification scope

配套有限审计脚本：

```bash
uv run python scripts/exact-lift/double-deficit/research-checks/tail/check_dd_corrected_terminal_denominator_sunit_entropy.py
```

脚本检查：

- `lambda`, `1/lambda`, `delta_UV`, `delta_gap` 的数值关系；
- shared budget
  \[
  \lambda\sigma+(2\lambda-1)R\le\delta
  \Longrightarrow
  \sigma+R\le\delta/\lambda;
  \]
- toy integer models 中
  \[
  V=v_1v_2,\quad\gamma=t_1t_2,
  \quad b_i=v_it_i
  \]
  精确重构 `b_1b_2=gamma V`；
- `Terminal-global-count` 的 exponent bookkeeping。

有限枚举只做 algebra/constant sanity check；无界 counting theorem 来自正文的 Farey separation、shared defect budget 与标准 divisor bound。

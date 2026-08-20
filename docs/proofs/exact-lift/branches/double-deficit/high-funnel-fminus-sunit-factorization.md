# DD `t_2=1` 的 exact `F_-` S-unit factorization

> **依赖：** `core.md` §§31–38 的 denominator overlap / primitive determinant ladder /
> overlap parameterization，以及 `core.md` §11 的 `t_2=1` S-unit phase；
> [`high-funnel-denominator-max-lock.md`](high-funnel-denominator-max-lock.md) 仅用于
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
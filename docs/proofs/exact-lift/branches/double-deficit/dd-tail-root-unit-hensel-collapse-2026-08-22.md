# DD corrected tail-root unit-Hensel 的 exact gap collapse

> 日期：2026-08-22
>
> 作用域：DD canonical high-funnel / terminal 中使用 unified tail-root linearization 的区域。
> 本文依赖 `dd-discriminant-root-dependency-audit-2026-08-22.md` 的判别根 normalization 修正。
>
> **状态：已严格完成（no-go / no-double-pay）。**
> 结论是：旧 valuation mismatch 被修正后留下的 equal-depth 5-adic unit cancellation，并不是新的 Hensel 约束；把正确的 signed unified root 代回后，它精确退化为 basic gap / decimal-determinant identity。

## 1. 两个根与 signed normalization

记

\[
q_\ell:=\operatorname{lcm}(b_1,b_2,b_3).
\]

DD gap root 使用

\[
\Xi=Qy_3-\tau a,
\]

而 corrected unified discriminant root 满足

\[
|\widetilde W|
=\frac{\kappa G}{q_\ell}|\Xi|.
\]

把实际 tail root 所选择的 sign 吸收到 root 中，定义 signed root

\[
\boxed{
\widetilde W_{\rm s}
:=\frac{\kappa G}{q_\ell}\Xi.
}
\tag{1.1}
\]

若历史文件使用 `eta * widetilde W`，则 `(1.1)` 就是把该 actual sign 合并后的同一整数。

## 2. tail-root linearization

统一 tail-root identity 写成

\[
\boxed{
\mathscr T a_3
=\kappa G^2 C
+(\kappa+G)\widetilde W_{\rm s},
}
\tag{2.1}
\]

其中

\[
\mathscr T
=\frac{\kappa^2(\kappa+2G)}{10^m},
\qquad
C=10^dA_{12}.
\]

又有

\[
y_3=a_3\frac{q_\ell}{b_3},
\qquad
\kappa b_3=10^mQG.
\tag{2.2}
\]

将 `(1.1)` 与 `Xi=Qy_3-tau a` 代入 `(2.1)`：

\[
\frac{\kappa^2(\kappa+2G)}{10^m}a_3
=
\kappa G^2C
+\frac{\kappa G(\kappa+G)}{q_\ell}
\left(
Q a_3\frac{q_\ell}{b_3}-\tau a
\right).
\]

使用

\[
\frac Q{b_3}=\frac\kappa{10^mG},
\]

右边第一份 `a3` 项化成

\[
\frac{\kappa^2(\kappa+G)}{10^m}a_3.
\]

两边相减后恰得

\[
\frac{\kappa^2G}{10^m}a_3
-\kappa G^2C
=-\frac{\kappa G(\kappa+G)}{q_\ell}\tau a.
\]

除去 `kappa G`：

\[
\frac\kappa{10^m}a_3-GC
=-\frac{\kappa+G}{q_\ell}\tau a.
\]

再用

\[
\frac\kappa{10^m}=\frac{QG}{b_3}
\]

得到

\[
G\left(C-\frac{Qa_3}{b_3}\right)
=\frac{\kappa+G}{q_\ell}\tau a.
\]

定义 decimal determinant

\[
\boxed{E:=b_3C-Qa_3.}
\]

于是

\[
\frac{GE}{b_3}
=\frac{\kappa+G}{q_\ell}\tau a.
\tag{2.3}
\]

完整 denominator concat 为

\[
\beta:=10^mQ+b_3.
\]

由 `kappa b3=10^m QG`：

\[
\beta
=b_3\left(\frac\kappa G+1\right)
=\frac{b_3(\kappa+G)}G.
\]

因此 `(2.3)` 精确等价于

\[
\boxed{
E=\frac{\beta\tau a}{q_\ell}.
}
\tag{Tail-root-collapse}
\]

## 3. `(Tail-root-collapse)` 本来就是 exact lift

全拼接 numerator / denominator 为

\[
\alpha=10^{n_3}A_{12}+a_3,
\qquad
\beta=10^mQ+b_3,
\qquad n_3=m+d.
\]

exact lift 给

\[
H=\frac{q_\ell\alpha}{\beta},
\qquad
y_3=\frac{q_\ell a_3}{b_3}.
\]

所以

\[
\begin{aligned}
H-y_3
&=q_\ell\left(\frac\alpha\beta-\frac{a_3}{b_3}\right)\\
&=q_\ell\frac{b_3\alpha-a_3\beta}{\beta b_3}\\
&=q_\ell\frac{10^m(b_3C-Qa_3)}{\beta b_3}\\
&=q_\ell\frac{10^mE}{\beta b_3}.
\end{aligned}
\tag{3.1}
\]

另一方面 DD gap normalization 是

\[
H-y_3=La,
\qquad
L=\frac{10^m}{\omega},
\qquad
b_3=\omega\tau.
\]

将其代入 `(3.1)` 并约去 `10^m/omega`：

\[
\boxed{
E=\frac{\beta\tau a}{q_\ell},
}
\]

与 `(Tail-root-collapse)` 完全相同。

## 4. 对 corrected 5-adic high funnel 的含义

`dd-discriminant-root-dependency-audit-2026-08-22.md` 已证明，旧 Five-dichotomy 使用的 valuation mismatch 消失；tail-root 两侧在 5-adic place 精确同深。

在提出共同 5-depth 后，确实会留下一个很深的 unit-unit congruence。但本文说明：

\[
\boxed{
\text{该 unit-Hensel congruence 的全部深度}
=\text{basic gap/determinant identity 的 5-adic 投影}.
}
\]

因此不能把它再次用于：

- 排除 corrected equality frontier；
- 对 `q_c` / source-lift index 额外收费；
- 恢复旧 `Five-dichotomy`；
- 构造独立的 third Hensel phase。

任何后续 strict-gap proof 必须使用不由

\[
H-y_3=La,
\qquad
E=b_3C-Qa_3,
\qquad
q_\ell\alpha=H\beta
\]

恢复的全局结构。

## 5. 状态摘要

- **已严格完成：** signed normalization 下 `(Tail-root-collapse)` 的逐行推导；其与 exact lift gap identity 的等价。
- **no-go：** corrected equal-depth tail-root unit cancellation 不是独立 source constraint。
- **仍待证：** corrected `6.308883...` equality terminal 的 strict gap；moving split-prime core `C_L/Pi` 与 decimal/source structure 的真正全局兼容性；DD 空性与有效绝对高度界。

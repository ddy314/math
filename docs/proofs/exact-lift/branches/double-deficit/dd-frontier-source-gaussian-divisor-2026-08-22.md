# DD frontier: source Gaussian carrier 的 exact smooth collapse

> 日期：2026-08-22
>
> 作用域：假想 corrected `6.308883...` terminal one-channel frontier。
>
> **状态：已严格完成（no-go / normalization audit）。**
>
> 本文修正本文件早先版本的一处解释：由 derivative orientation 与 clean source 投影得到的 `source Gaussian carrier` 并不是新的 Gaussian reader。它与已有 secondary Gaussian numerator **精确相差一个纯 `2/5`-smooth scalar和一个 Gaussian unit**。因此此前从它导出的 fixed-`q_c` divisor counting 与 source-lift separation 不能作为独立 entropy reduction 再收费；它们只是 secondary line 的重写。

## 1. 两条已有 Gaussian 线

已有 derivative Gaussian integer

\[
D_{\rm der}
=2\widetilde rL_{\rm clean}q_c-iP_0,
\qquad
\Pi\mid D_{\rm der},
\qquad N(\Pi)=C_L.
\tag{1.1}
\]

clean source为

\[
q_c^2L_{\rm clean}=VA_0-5^TR_0,
\qquad V=C_Lv_0.
\tag{1.2}
\]

另一方面 terminal secondary Gaussian numerator为

\[
\boxed{
\mathcal G_1
=A_*2^{m-2}q_c
-i\widetilde rR_0\,5^{2T-m}
=\Pi\Delta_1.
}
\tag{Secondary}
\]

其中

\[
A_*=g_0a_2\theta s,
\qquad
P_0=A_*B,
\tag{1.3}
\]

且 terminal decimal normalization给

\[
\boxed{
B=\frac{10^m}{2\cdot5^T}
=2^{m-1}5^{m-T}.
}
\tag{1.4}
\]

## 2. derivative + clean source 的 source projection

将 `(1.1)` 乘以 `q_c`，使用 `(1.2)`：

\[
\begin{aligned}
q_cD_{\rm der}
&=2\widetilde r q_c^2L_{\rm clean}-iP_0q_c\\
&=2\widetilde rC_Lv_0A_0
-\bigl(2\widetilde r5^TR_0+iP_0q_c\bigr).
\end{aligned}
\]

因为 `Pi|C_L`，得到

\[
\Pi\mid\mathcal S_{\rm src},
\qquad
\boxed{
\mathcal S_{\rm src}
:=2\widetilde r5^TR_0+iP_0q_c.
}
\tag{Source-Gaussian}
\]

这一步本身严格正确。

## 3. exact smooth-collapse identity

使用 `(1.3)--(1.4)`：

\[
P_0q_c
=A_*2^{m-1}5^{m-T}q_c.
\]

因此

\[
\begin{aligned}
i\,2\,5^{m-T}\mathcal G_1
&=iA_*2^{m-1}5^{m-T}q_c
+2\widetilde rR_0 5^T\\
&=iP_0q_c+2\widetilde r5^TR_0.
\end{aligned}
\]

于是得到精确恒等式

\[
\boxed{
\mathcal S_{\rm src}
=i\,2\,5^{m-T}\mathcal G_1
=i\,2\,5^{m-T}\Pi\Delta_1.
}
\tag{Smooth-collapse}
\]

这不是 leading-order 近似，也没有 exceptional core：它是 exact identity。

所以 `(Source-Gaussian)` 没有提供新的 oriented divisibility；它只是 `(Secondary)` 乘以 rational smooth scalar `2*5^{m-T}` 后旋转 `i`。

## 4. norm parent 也只是同一 identity 的平方

取 norm：

\[
\boxed{
N(\mathcal S_{\rm src})
=4\,5^{2(m-T)}C_LN(\Delta_1).
}
\tag{4.1}
\]

此前由 hidden square + clean source得到的表达

\[
N(\mathcal S_{\rm src})
=C_L\left(
4\widetilde r^{\,2}5^TR_0v_0A_0
-C_L(q_cP_1)^2
\right)
\tag{4.2}
\]

因此也只是 `(4.1)` 的另一坐标表示。特别地，括号内整数精确等于

\[
\boxed{
4\,5^{2(m-T)}N(\Delta_1).
}
\tag{4.3}
\]

所以这里不存在新的 deep cancellation invariant。

## 5. 撤销早先版本的 counting interpretation

早先版本曾据

\[
\Pi\mid\mathcal S_{\rm src}
\]

声称：固定 `q_c` 与 slow data 后，`(C_L,Pi)` 只能从一个新的 fixed Gaussian integer 的 divisors 中选择，并进一步讨论不同 source lifts 的 common-core separation。

`(Smooth-collapse)` 说明这些 statement 若作为集合论陈述仍可由 `mathcal S_src` 写出，但它们与已有

\[
\Pi\mid\mathcal G_1
\]

**完全等价**，没有新增约束、没有新增 counting rank，也没有新增 source-lift restriction。

因此以下用途全部撤销：

1. 把 `S_src` 当成独立于 secondary line 的 fixed-`q_c` Gaussian reader；
2. 把由 `S(q_1)-S(q_2)` 得到的 pairwise core separation当成新的 source-lift entropy reduction；
3. 把 `C_L|N(S_src)` 当成 hidden square / secondary norm 之外的另一份 arithmetic information。

## 6. 当前边界

本次 audit 给出一个明确 no-go：

\[
\boxed{
\text{derivative orientation}
+\text{clean source}
\longrightarrow
\mathcal S_{\rm src}
}
\]

不会生成新的 Gaussian direction；它精确回到 secondary numerator `G_1`。

所以 strict-gap 工作不应再沿 `D_der + clean source` 制造 source Gaussian carrier。真正仍可能产生新信息的接口必须改变至少一个 parent family，例如：

- raw decimal prefix denominator relation与 moving pair-max orientation；
- 跨不同 split primes 的 global distribution；
- 一个不由 `Delta_1 / hidden square / projective Z_0` 生成的 genuinely new lattice determinant。

当前全局状态不变：

\[
\boxed{
\limsup_{\rm DD}\frac{n_3}{S}
\le6.308883577618\ldots
}
\]

strict gap 与 DD 空性仍待证。

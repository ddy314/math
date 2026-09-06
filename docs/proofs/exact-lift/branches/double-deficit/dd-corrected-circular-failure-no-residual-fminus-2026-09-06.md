# DD corrected circular-lock failure：no-residual `F_-` lower

> 日期：2026-09-06
>
> 依赖：[`dd-global-circular-decimal-phase-hard-source-lock-2026-09-06.md`](dd-global-circular-decimal-phase-hard-source-lock-2026-09-06.md)、[`dd-corrected-euclidean-failure-denominator-gcd-bootstrap-2026-09-06.md`](dd-corrected-euclidean-failure-denominator-gcd-bootstrap-2026-09-06.md)、[`dd-corrected-euclidean-failure-no-residual-fminus-2026-09-06.md`](dd-corrected-euclidean-failure-no-residual-fminus-2026-09-06.md)。
>
> **严格状态：已严格完成（corrected post-tail odd non-decimal source；circular ordinary-lock failure branch）。**
>
> Euclidean failure continuation已经证明：universal source modulus覆盖全部 hard source与 soft prefix-norm，唯一可能逃出的 soft exponent进入 denominator common gcd `d_B=(b_1,b_2)`；再由 exact overlap factorization把 `d_B` 也收费进 `F_-`，得到
> \[
> 4\log F_-\ge4S-r_n-o(S).
> \]
>
> 本文把 Euclidean exponent `r_n<m_2` 替换成前一 theorem 的 circular phase
> \[
> r_{\rm circ}\le m_2/2.
> \]
> 关键不是重新做 payer allocation，而是证明 circular normalization使用的 universal odd source modulus与 Euclidean theorem在每个 rough prime上有**完全相同的 exponent**
> \[
> r_E=(c-M-t)_+.
> \]
> 因而整个 hard+soft coverage可原样迁移，得到
> \[
> \boxed{
> 4\log_{10}F_-
> \ge4S-r_{\rm circ}-o(S).
> }
> \]
> 特别地
> \[
> \boxed{
> \log_{10}F_-\ge\frac78S-o(S).
> }
> \]
> failure side至此只剩一个显式 decimal phase `r_circ`，没有匿名 source/norm/projective/denominator-gcd payer。

---

## 1. universal circular source modulus

沿用 primitive source prefix

\[
C_Q=u_1 10^{m_2}+u_2.
\]

对任意 odd non-decimal source prime `p|C_Q` 写

\[
E=v_p(b_1)=v_p(b_2),
\quad j=v_p(b_3),
\quad M=\max(E,j),
\]

\[
t=v_p(A_{12}),
\quad c=v_p(C_Q).
\]

`dd-global-circular-decimal-phase-hard-source-lock` 从 gap-normalized parent

\[
q_{\rm lcm}A_{12}10^d\equiv\tau a
\]

出发。左侧 coefficient在 `p` 处的 depth为

\[
\boxed{v_p(q_{\rm lcm}A_{12})=M+t.}
\tag{1.1}
\]

所有 decimal shifts与 primitive-prefix foldings只乘除 `10,u_1,u_2`，它们在 odd source support上均为 units。因此 gcd-stripped effective source exponent对**任意** odd source prime都是

\[
\boxed{
r_E=(c-M-t)_+.}
\tag{1.2}
\]

这与 Euclidean theorem §1 的 universal modulus exponent完全相同。

定义 rough circular modulus

\[
\boxed{
Q_{\rm circ}:=
\prod_{p\mid X_Q}p^{(c_p-M_p-t_p)_+},
}
\tag{1.3}
\]

其中 product只遍历 corrected `X_Q` 的 odd non-decimal support。

前一 circular theorem的 phase normalization因此可同时在 `Q_circ` 上完成：存在整数 units `A_circ,B_circ` 使

\[
\boxed{
Q_{\rm circ}\mid
A_{\rm circ}10^{r_{\rm circ}}-B_{\rm circ},
\qquad
(A_{\rm circ}B_{\rm circ},Q_{\rm circ})=1.
}
\tag{Circular-universal-reader}
\]

---

## 2. ordinary-lock / failure dichotomy on the universal modulus

若

\[
Q_{\rm circ}>10^{r_{\rm circ}},
\]

则

\[
\boxed{
10^{r_{\rm circ}}
=[B_{\rm circ}A_{\rm circ}^{-1}]_{Q_{\rm circ}}.
}
\tag{2.1}
\]

本文研究其 complementary failure branch：

\[
\boxed{
Q_{\rm circ}\le10^{r_{\rm circ}}.
}
\tag{Circular-failure}
\]

---

## 3. previous hard+soft coverage survives unchanged

[`dd-corrected-euclidean-failure-denominator-gcd-bootstrap-2026-09-06.md`](dd-corrected-euclidean-failure-denominator-gcd-bootstrap-2026-09-06.md) 的 local proof只使用 universal exponent

\[
r_E=(c-M-t)_+.
\]

它证明：

1. hard support上 `h+n_0<=r_E`；
2. soft `e_N>0` 且 `j>E` 时 `e_N<=r_E`；
3. soft `e_N>0` 且 `E>=j` 时未被 `r_E` 覆盖的 exponent满足
   \[
   e_{N,D}\le E;
   \]
4. 因而存在整数 `Y_E,X_{N,D}` 满足
   \[
   \boxed{X_NX_H=Y_EX_{N,D},}
   \tag{3.1}
   \]
   \[
   \boxed{Y_E\mid Q_{\rm circ},}
   \tag{3.2}
   \]
   \[
   \boxed{X_{N,D}\mid\operatorname{core}_{10}(d_B),
   \qquad d_B=(b_1,b_2).}
   \tag{3.3}
   \]

这里 `(3.2)` 可以把旧 `Q_E` 直接替换为 `Q_circ`，因为二者在 relevant odd source support的 local exponent同为 `(1.2)`；没有新增或删除 valuation layer。

由 `(Circular-failure)`：

\[
\boxed{Y_E\le10^{r_{\rm circ}}.}
\tag{3.4}

于是

\[
\boxed{
X_NX_H
\le10^{r_{\rm circ}}\operatorname{core}_{10}(d_B).
}
\tag{3.5}

---

## 4. third/gap layer已经 exact paid

前一 corrected continuation已经从 exact small-factor normalization安全得到

\[
\boxed{X_aX_3Q<F_-.}
\tag{4.1}

结合 bottom charge与 original second-Schmidt，得到 corrected third-gap bootstrap

\[
\boxed{
3\log_{10}F_-+\log_{10}(X_NX_H)
\ge3S-o(S).
}
\tag{4.2}

代入 `(3.5)`：

\[
\boxed{
3\log_{10}F_-+\log_{10}\operatorname{core}_{10}(d_B)
\ge3S-r_{\rm circ}-o(S).
}
\tag{4.3}

弱化为 raw gcd：

\[
\boxed{
3\log_{10}F_-+\log_{10}d_B
\ge3S-r_{\rm circ}-o(S).
}
\tag{4.4}

---

## 5. denominator common gcd也进入 `F_-`

exact denominator overlap为

\[
g_*=(b_1,b_2)\,(
\operatorname{lcm}(b_1,b_2),b_3),
\]

故

\[
\boxed{d_B\mid g_*.}
\tag{5.1}

safe exact small-factor normalization给

\[
F_-=a g_*L\frac{LQ+2\tau}{\tau},
\qquad0<\tau<L.
\]

因此

\[
\boxed{d_BQ<F_-.}
\tag{5.2}

而 `Q` 是 `S`-digit prefix：

\[
10^{S-1}\le Q<10^S.
\]

所以

\[
\boxed{
\log_{10}d_B
\le\log_{10}F_- -S+O(1).
}
\tag{5.3}

代入 `(4.4)`：

\[
\boxed{
4\log_{10}F_-
\ge4S-r_{\rm circ}-o(S).
}
\tag{Circular-no-residual}

即

\[
\boxed{
\log_{10}F_-
\ge S-\frac{r_{\rm circ}}4-o(S).
}
\tag{5.4}

---

## 6. universal `7/8` lower

前一 circular theorem严格证明

\[
0\le r_{\rm circ}\le\left\lfloor\frac{m_2}{2}\right\rfloor.
\]

又

\[
m_2\le S.
\]

所以

\[
\boxed{
\frac{r_{\rm circ}}4\le\frac S8.
}
\]

代入 `(5.4)`：

\[
\boxed{
\log_{10}F_-
\ge\frac78S-o(S).
}
\tag{Seven-eighths}

更精细地，若

\[
c_{10}=v_{10}(q_{\rm lcm}A_{12}),
\qquad
s_{10}=v_{10}(\tau a),
\]

则

\[
r_{\rm circ}
\le
\max\!\left(0,
\left\lfloor\frac{m_2-c_{10}-s_{10}}2\right\rfloor
\right),
\]

故 `(5.4)`保留 coefficient/right-side smooth mass的全部改善；不必先粗化成 `7/8`。

特别地若

\[
c_{10}+s_{10}\ge m_2-1,
\]

则 `r_circ=0`，failure branch直接给

\[
\boxed{
\log_{10}F_-\ge S-o(S).
}
\tag{Smooth-saturated-failure}

---

## 7. proof-status boundary

本文关闭的是**circular ordinary-lock failure branch的 payer accounting**：

\[
\boxed{
\text{failure}
\Longrightarrow
\log F_-\ge S-r_{\rm circ}/4-o(S)
\ge7S/8-o(S).
}
\]

它没有证明 ordinary circular lock不可能。ordinary branch仍可能包含无界 candidates，除非另一个 independent global parent、deterministic digit-location theorem或 moving-target argument排除它。

因此本文不推出 `DD=empty`，也暂不推出新的 global explicit slope常数。

---

## 8. 状态摘要

- **已严格完成：** universal circular modulus local exponent `r_E=(c-M-t)_+`；
- **已严格完成：** Euclidean hard+soft coverage原样迁移到 `Q_circ`；
- **已严格完成：** circular failure只留下 `d_B`；
- **已严格完成：** exact `d_BQ<F_-` 删除最后 denominator gcd；
- **主结论：** `4 log F_- >= 4S-r_circ-o(S)`；
- **universal consequence：** `log F_- >= 7S/8-o(S)`；
- **仍待证：** ordinary circular lock branch、corrected non-canonical global LP、DD strict gap/emptiness。

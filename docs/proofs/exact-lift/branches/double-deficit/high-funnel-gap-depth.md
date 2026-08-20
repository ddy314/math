# DD high-funnel `Defect-heavy` = sphere-gap extra 5-depth

> **依赖：** [`high-funnel-xi-depth.md`](high-funnel-xi-depth.md)、`core.md` §§17–18 的 gap normalization、high-funnel tail weight与 5-resonance。
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

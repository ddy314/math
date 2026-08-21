# DD post-tail correction：general-transfer 的判别根 normalization 错位

> **依赖：** [`core.md`](core.md) §17–18 的 DD gap normalization / discriminant、
> [`tail-allocation-ledger.md`](tail-allocation-ledger.md) 中 `tail-pure-cancellation-three-sheet`、
> `tail-pure-cancellation-hensel-nogo` 与 `tail-rough-general-transfer`。
>
> **严格状态：** `已严格完成（错误定位与 corrected hard-sheet identity）`。
>
> **影响：** `tail-hard-source-derivative-sheet` 的 `W-hard / Derivative-hard`，以及
> `tail-rough-general-transfer` §5–6 用它关闭 hard sheet 的步骤失效。
> 因而 `General-transfer-local`
> \[
> x_p\le\max(v_p(C),v_p(N_0),v_p(R_3^{\rm den}))
> \]
> 当前 **不能视为已证**。依赖它获得“全部 `X_Q` support”穷尽性的后续 payer / Gaussian
> 文件必须暂时按 **conditional-on-transfer** 使用；这些文件中的独立 exact identities并不因此
> 自动失效。

---

## 1. 两个判别根必须分开记号

DD §17–18 使用
\[
H-y_3=La,
\qquad
\mathcal M-QH=\tau a,
\]
并令
\[
\boxed{C_0=LQ+2\tau.}
\tag{1.1}

其 gap quadratic 为
\[
\boxed{
C_0a^2-2\mathcal Ma+Q\frac{\mathcal S_{12}}L=0,
}
\tag{Gap-Q}
其中
\[
\mathcal S_{12}=y_1^2+y_2^2.
\]

§18 的整数为
\[
\boxed{
\Xi=\mathcal M-C_0a,
\qquad
W_{\rm gap}=L\Xi
}
\tag{1.2}
（绝对值对以下 valuation 无影响）。

另一方面 `tail-rough-general-transfer` §5 使用的 unified quadratic discriminant 为
\[
\boxed{
\widetilde W^2
=
\kappa\bigl(\kappa K_{C,Q}-2GQ^2\mathcal N_{12}\bigr),
}
\tag{1.3}
其中
\[
K_{C,Q}=G^2C^2-Q^2\mathcal N_{12}.
\]
等价地
\[
\boxed{
\widetilde W^2
=
(\kappa GC)^2
-
\kappa(\kappa+2G)Q^2\mathcal N_{12}.
}
\tag{Unified-W}

旧 proof 把 `(Unified-W)` 的正根与 `(1.2)` 中的 `W_gap` 直接认成同一个整数。
这一步不成立。

---

## 2. `Xi` 的两个 exact simplification

由
\[
\mathcal M=QH+\tau a
\]
立即有
\[
\begin{aligned}
\Xi
&=QH+\tau a-(LQ+2\tau)a\\
&=Q(H-La)-\tau a\\
&=\boxed{Qy_3-\tau a.}
\end{aligned}
\tag{Xi-linear}

另一方面把 `(Gap-Q)` 代入平方展开：
\[
\begin{aligned}
\Xi^2
&=(\mathcal M-C_0a)^2\\
&=\mathcal M^2-2C_0\mathcal Ma+C_0^2a^2\\
&=\boxed{
\mathcal M^2
-C_0Q\frac{\mathcal S_{12}}L.
}
\end{aligned}
\tag{Xi-square}

这两式只使用 §17 的 exact DD algebra。

---

## 3. unified root 与 gap root 的 exact normalization

整数球面 ghost definitions 给
\[
\mathcal M=qC,
\qquad
\mathcal S_{12}
=\left(\frac qG\right)^2\mathcal N_{12}.
\]
因此 `(Xi-square)` 化为
\[
\boxed{
\Xi^2
=q^2\left(
C^2-
\frac{C_0Q\mathcal N_{12}}{LG^2}
\right).
}
\tag{3.1}

又由 tail weight
\[
\kappa b_3=10^{m_3}QG,
\qquad
b_3=\omega\tau,
\qquad
10^{m_3}=\omega L,
\]
得到
\[
\boxed{\kappa\tau=LQG.}
\tag{3.2}

所以
\[
\begin{aligned}
\frac{\kappa(\kappa+2G)Q^2}{\kappa^2G^2}
&=\frac{(\kappa+2G)Q^2}{\kappa G^2}\\
&=\frac{Q^2}{G^2}\left(1+\frac{2\tau}{LQ}\right)\\
&=\frac{C_0Q}{LG^2}.
\end{aligned}
\]
代回 `(Unified-W)`：
\[
\boxed{
\widetilde W^2
=(\kappa G)^2
\left(
C^2-
\frac{C_0Q\mathcal N_{12}}{LG^2}
\right).
}
\tag{3.3}

与 `(3.1)` 比较得到本文核心 correction：
\[
\boxed{
\widetilde W^2
=\left(\frac{\kappa G}{q}\right)^2\Xi^2.
}
\tag{Unified-vs-gap}

取正根：
\[
\boxed{
\widetilde W
=\frac{\kappa G}{q}\,|\Xi|.
}
\tag{3.4}

而 §18 的 root 是
\[
W_{\rm gap}=L\Xi.
\]
两者之间存在显式 normalization ratio
\[
\boxed{
\frac{\widetilde W}{|W_{\rm gap}|}
=\frac{\kappa G}{qL}.
}
\tag{3.5}

因此旧 general-transfer 中从 `v_p(\widetilde W)` 直接读取
`v_p(\Xi)` 的步骤遗漏了整份 `v_p(\kappa G/q)`。

---

## 4. hard-sheet 上 `Xi` 的正确 valuation

沿用 `tail-rough-general-transfer` 的 local notation：
\[
E=v_p(b_1)=v_p(b_2),
\quad j=v_p(b_3),
\quad M=\max(E,j),
\]
\[
c=v_p(C_Q),
\quad t=v_p(C),
\quad n_0=v_p(N_0).
\]

在该文件的 contradiction hypothesis
\[
\boxed{
x>t,\qquad x>n_0,\qquad x>(j-E)_+}
\tag{Hard-H}
下，其 §1–4（不使用 unified discriminant）得到
\[
\boxed{A:=v_p(a)=t+(E-j)_+,}
\tag{4.1}
以及
\[
\boxed{
\Delta
:=c+j-E+n_0-2t>0.
}
\tag{4.2}

并有
\[
v_p(\mathcal M)=M+t.
\]

现在直接使用 `(Xi-square)`。因为
\[
v_p(C_0)=j,
\qquad
v_p(Q)=E+c,
\]
以及
\[
\mathcal S_{12}
=\left(\frac qG\right)^2\mathcal N_{12}
\]
给
\[
v_p(\mathcal S_{12})=2M-2E+n_0,
\]
所以第二项 valuation 为
\[
\begin{aligned}
v_p\left(C_0Q\frac{\mathcal S_{12}}L\right)
&=j+(E+c)+(2M-2E+n_0)\\
&=2M+c+j-E+n_0\\
&=2(M+t)+\Delta.
\end{aligned}
\]
严格大于
\[
v_p(\mathcal M^2)=2(M+t).
\]
故不存在 cancellation：
\[
\boxed{
v_p(\Xi)=M+t.
}
\tag{Xi-hard-correct}

这也可从 `(Xi-linear)` 直接理解：hard sheet 上 `tau*a` 正好携带 baseline
`M+t`，而 `Qy_3` 更深。

---

## 5. 旧 `W-general` 的“大深度”来自 normalization factor

`tail-rough-general-transfer` §5 对 `(Unified-W)` 的 valuation 计算本身给
\[
\boxed{
v_p(\widetilde W)=5E+c-j+t.
}
\tag{5.1}

这与 `(Xi-hard-correct)` 完全相容。事实上
\[
v_p(\kappa)=3E+c-j,
\qquad
v_p(G)=2E,
\qquad
v_p(q)=M,
\]
所以
\[
\begin{aligned}
v_p(\kappa G/q)+v_p(\Xi)
&=(5E+c-j-M)+(M+t)\\
&=5E+c-j+t,
\end{aligned}
\]
恰为 `(5.1)`。

因此旧 proof 看到的所谓 derivative extra depth
\[
5E+c-j-M
\]
完全等于
\[
\boxed{v_p(\kappa G/q),}
\]
是显式 normalization depth，不是 `Xi` 中的额外 Hensel cancellation。

---

## 6. gap 的“extra contact”同样没有独立 source height

`tail-rough-general-transfer` §4 还得到
\[
v_p(C_0a-2\mathcal M)=M+t+\Delta.
\]
这条 valuation 本身正确，但 exact algebra 给
\[
\begin{aligned}
C_0a-2\mathcal M
&=(LQ+2\tau)a-2(QH+\tau a)\\
&=Q(La-2H)\\
&=\boxed{-Q(H+y_3).}
\end{aligned}
\tag{Gap-contact-collapse}

所以其额外深度已经显式含有 source factor `Q` 与 complementary sphere factor；
这与 `tail-pure-cancellation-hensel-nogo` 的 `Sphere-parent` no-double-count 结论一致。

不能把该 contact 与 `Q` cancellation 再次相加收费。

---

## 7. `General-transfer-local` 的正确状态

旧 proof 的最终 contradiction 需要同时使用：
\[
\mathcal M\equiv C_0a\pmod{p^{M+t+1}}
\]
和
\[
2\mathcal M\equiv C_0a\pmod{p^{M+t+1}}.
\]
第一条来自错误的 `v_p(Xi)>M+t`。

corrected `(Xi-hard-correct)` 恰给
\[
v_p(\mathcal M-C_0a)=M+t,
\]
所以该 congruence不存在。第二条只是 `(Gap-contact-collapse)` 的 sphere/source投影。

因此 contradiction 消失，`(Hard-H)` 目前仍是一个合法 local sheet。

故：
\[
\boxed{
\text{`General-transfer-local` 当前降级为待证；旧证明无效。}
}
\tag{Transfer-suspended}

特别是 baseline-free 纯 unit sheet
\[
E=j=t=n_0=A=0,
\qquad c=x>0,
\]
在 valuation ledger 上完全一致：
\[
G_1=G_2=0<G_3=c,
\]
其 deep cancellation正是 `tail-pure-cancellation-hensel-nogo` 已识别的 sphere-paid
unit-Hensel，不产生第二份 local payer。

---

## 8. downstream 影响边界

下列结论因依赖 `General-transfer-local` 的**穷尽性**，暂时不能继续标记为“整个 `X_Q` support
已关闭”：

1. `tail-rough-gaussian-payer-split` 的 exhaustive angular transfer；
2. `tail-rough-angular-source-transfer` 的 exhaustive numerator transfer；
3. `tail-rough-canonical-payer-decomposition`；
4. `tail-rough-projective-bottom-two-payer`；
5. `tail-rough-z0-only-frontier`；
6. 本分支新文件 `dd-z0-charged-first-*`、`dd-third-excess-collapse-*`、
   `dd-gaussian-overlap-stripped-*`、`dd-gaussian-oriented-transversality-*`、
   `dd-gaussian-deep-core-*` 的 **global/exhaustive status**。

这些文件中只依赖各自显式 local hypotheses 的 algebraic lemmas仍可保留。例如：

- source/angular Gaussian linear identities；
- cyclotomic orientation identity；
- bottom determinant exact identity；
- 在已经确认进入 Gaussian residual sheet之后的 local valuation formulas；
- source-square/deep 的 conditional height tradeoff。

它们现在应读作：
\[
\boxed{
\text{conditional structural theorems, not an exhaustive global transfer.}
}
\]

---

## 9. corrected frontier

post-tail second-Schmidt 的真正未付 rough object必须重新写成两部分：

\[
\boxed{
X_Q
\rightsquigarrow
\text{existing explicit payer sheets}
\quad+\quad
\text{hard source-cancellation sheet }X_H.
}
\]

`X_H` 的 local defining condition正是 `(Hard-H)`：source overflow比 coefficient、prefix norm
与 third denominator excess都深。

在该 sheet 上已有严格结构：

\[
A=t+(E-j)_+,
\]
\[
G_1=G_2<G_3,
\]
\[
v_p(\Xi)=M+t,
\]
以及 exact no-double-count
\[
C_0a-2\mathcal M=-Q(H+y_3).
\]

所以继续攻击 `X_H` 不能再靠同一个 gap quadratic / unified discriminant制造第二份 local height。
正确接口应来自它们之外的独立结构：full decimal concat、global source product、Gaussian orientation
（若另有来源强迫）或新的 fixed-target/Subspace input。

---

## 10. 状态摘要

- **`已严格完成`**：`Xi-linear`、`Xi-square`、`Unified-vs-gap`、`Xi-hard-correct`。
- **`已严格完成`**：旧 `W-general` 的额外 valuation 被精确识别为 `v_p(kappa G/q)` normalization。
- **`已严格完成`**：`Gap-contact-collapse` 与 existing Unit-Hensel no-go 一致。
- **`纠正`**：`W-hard / Derivative-hard` 失效；`General-transfer-local` 的旧 proof 失效。
- **`待证`**：hard source product `X_H` 的独立 global control；重做 post-tail side-branch reoptimization；DD global explicit `<=6` / absolute height。

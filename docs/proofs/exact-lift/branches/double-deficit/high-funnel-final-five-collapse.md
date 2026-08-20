# DD `Final-5-lock` 的 full smooth-overlap collapse

> **依赖：** [`high-funnel-exact-small-factor-normalization.md`](high-funnel-exact-small-factor-normalization.md)、
> [`high-funnel-two-adic-balance.md`](high-funnel-two-adic-balance.md) 的 shallow-gap 与 Schmidt budget、
> [`high-funnel-denominator-max-lock.md`](high-funnel-denominator-max-lock.md) 的 `Final-5-lock`、
> [`high-funnel-defect-optimization.md`](high-funnel-defect-optimization.md) 的 `Tail-short` bound、
> `core.md` 的 `d`-dominant small-factor upper bound与 `Q/G` constant window。
>
> **严格状态：** `已严格完成（canonical double-resonant t_2=1 funnel）`。
>
> 关键修正：exact small-factor normalization 中，除 5-adic charge 外还存在一份此前
> sector LP 未收费的完整二进 overlap
> \[
> v_2\!\left(\frac{a(g_*/V)}{s}\right)=\mathfrak g,
> \qquad s=(2\cdot5^T,q).
> \]
> 把这项保留后，`Final-5-lock` 的整个剩余 sector满足
> \[
> \boxed{
> \limsup\frac nS
> \le
> 2+3\frac{\frac32+\frac12\log_{10}2}{1+\log_{10}2}
> =5.805865360520\ldots.
> }
> \]
> 因而此前 `>6.215109...` 的 Defect-heavy remaining sheet为空。
> 结合 `Tail-short <= 6.215109404735...`，得到 canonical double-resonant
> `t_2=1` funnel 的显式 sector bound
> \[
> \boxed{
> \limsup\frac nS
> \le
> \frac{28}{3+5\log_{10}2}
> =6.215109404735\ldots.
> }
> \]
> 本文不自动把该 sector bound外推成新的全 DD numerical limsup；全局分类作用域仍按
> `core.md` 读取。

---

## 1. 记号与 `Final-5-lock`

令

\[
a_2:=\log_{10}2,
\qquad
b_5:=\log_{10}5=1-a_2.
\]

为避免和 sphere-gap quotient `a` 混淆，本文把两个对数常数写成
`a_2,b_5`。

对无界 sequence 归一化：

\[
M=\frac mS,
\quad Q_5=\frac{q_5}{S},
\quad G_5=\frac{g_5}{S},
\quad N_5=\frac{n_5}{S},
\]

\[
Q_2=\frac{\mathfrak q}{S},
\quad G_2=\frac{\mathfrak g}{S},
\quad N_2=\frac{\mathfrak n}{S},
\quad
G_0^{\rm rough}=\frac{\log_{10}\gamma_0}{S}.
\]

`Final-5-lock` 给

\[
\boxed{
M=2Q_5+4G_5+N_5,
}
\tag{1.1}

以及

\[
\boxed{
T/S=M-2G_5.
}
\tag{1.2}

因此

\[
\boxed{G_5\le M/4.}
\tag{1.3}

---

## 2. exact small factor 的 2/5-adic full charge

`high-funnel-exact-small-factor-normalization.md` 已证明

\[
\boxed{
F_-=
\frac{2^{H+2}5^TZ}{s}
\;a\frac{g_*}{V},
\qquad
s=(2\cdot5^T,q).
}
\tag{2.1}

这里 source factor由 `Q=Uq` 定义，且 `(UV,10)=1`，所以

\[
v_2(q)=\mathfrak q,
\qquad
v_5(q)=q_5.
\tag{2.2}

### 2.1 五进净深度

`Final-5-lock` 给

\[
v_5(a)=q_5,
\qquad
v_5(g_*/V)=g_5.
\tag{2.3}

又

\[
T=2q_5+2g_5+n_5\ge q_5,
\]

所以

\[
v_5(s)=q_5.
\tag{2.4}

因此 `(2.1)` 中 5-adic 总贡献为

\[
\boxed{
T-q_5+q_5+g_5=T+g_5.
}
\tag{2.5}

### 2.2 二进净深度

`high-funnel-two-adic-balance.md` 的 shallow-gap theorem给

\[
v_2(a)=
\begin{cases}
0,&\mathfrak q=0,\\
1,&\mathfrak q\ge1.
\end{cases}
\tag{2.6}

另一方面

\[
v_2(s)=\min(1,\mathfrak q),
\tag{2.7}

所以

\[
\boxed{v_2(a)=v_2(s).}
\tag{2.8}

`b_3` 是二进 unique maximum；因此 `c_3=q_lcm/b_3` 为二进单位，而

\[
\frac{g_*}{V}=\frac\gamma{c_3},
\qquad V\text{ odd}.
\]

故

\[
\boxed{v_2(g_*/V)=\mathfrak g.}
\tag{2.9}

于是 `(2.1)` 中 smooth quotient在强制 `2^{H+2}` 之外还有完整

\[
\boxed{\mathfrak g}
\]

层：

\[
\boxed{
 v_2\!\left(\frac{a(g_*/V)}s\right)=\mathfrak g.
}
\tag{2-full-charge}

这正是此前 `2-balanced` sector estimate 中被保守丢掉的一项。

---

## 3. sharpened `F_-` lower bound

令

\[
U_h:=\frac{\log_{10}U}{S},
\qquad
Z_h:=\frac{\log_{10}Z}{S}.
\]

S-unit phase

\[
2^HZ=5^TU+V
\]

与 tail window给

\[
a_2\frac HS+Z_h
=b_5\frac TS+U_h+o(1).
\tag{3.1}

由 `(2.1)`、`(2.5)`、`(2-full-charge)`：

\[
\begin{aligned}
\frac{\log_{10}F_-}{S}
&\ge
 a_2\left(\frac HS+G_2\right)
+b_5\left(\frac TS+G_5\right)
+Z_h+o(1)\\
&=
2b_5\frac TS+b_5G_5+U_h+a_2G_2+o(1).
\end{aligned}
\]

使用 `T/S=M-2G_5`：

\[
\boxed{
\frac{\log_{10}F_-}{S}
\ge
2b_5M-3b_5G_5+U_h+a_2G_2+o(1).
}
\tag{F-lower-full}

---

## 4. 与 Archimedean small-factor upper bound 联立

canonical `d`-dominant funnel 的旧 small-factor ratio给

\[
\boxed{
\log_{10}F_-<4S+2m-n+O(1).
}
\tag{4.1}

若沿子序列

\[
C_*:=\limsup n/S,
\]

则 `(F-lower-full)` 与 `(4.1)` 给

\[
\boxed{
C_*
\le
4+2a_2M+3b_5G_5-U_h-a_2G_2.
}
\tag{4.2}

---

## 5. `U-height` 中的二进 overlap精确抵消

`Q` 为 `S` 位十进制拼接，且

\[
1<Q/G\le11.
\]

所以

\[
\log_{10}Q=S+O(1),
\qquad
\log_{10}G=S+O(1).
\]

又

\[
QG<\kappa\le10QG,
\]

故

\[
\frac{\log_{10}\kappa}{S}=2+o(1).
\]

写

\[
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0,
\qquad
(\gamma_0,10)=1,
\]

以及

\[
\kappa=2\gamma5^TU.
\]

得到 exact asymptotic height identity

\[
\boxed{
U_h
=2-a_2G_2-G_0^{\rm rough}
-b_5(M-G_5)+o(1).
}
\tag{U-height}

代回 `(4.2)`，`a_2G_2` **精确抵消**：

\[
\boxed{
C_*
\le
2+(1+a_2)M+2b_5G_5+G_0^{\rm rough}+o(1).
}
\tag{5.1}

这不是重复计费；`(F-lower-full)` 的 `+a_2G_2` 来自 actual divisor
`g_*/V`，而 `(U-height)` 的 `-a_2G_2` 来自从 `kappa` 中剥去 `gamma` 后
`U` 的余因子高度。两者由两个 exact identities分别读取同一份 factor allocation。

---

## 6. Final-5 + Schmidt budget 的 dual bound

由 `(1.3)`：

\[
2b_5G_5\le\frac{b_5}{2}M.
\]

所以 `(5.1)` 给

\[
\boxed{
C_*
\le
2+\left(\frac32+\frac{a_2}{2}\right)M
+G_0^{\rm rough}+o(1).
}
\tag{6.1}

`high-funnel-two-adic-balance.md` 已在 `Final-5-lock` 上证明

\[
\boxed{
(1+a_2)M
+2a_2Q_2+a_2N_2+2G_0^{\rm rough}
\le3+o(1).
}
\tag{Schmidt-budget}

定义

\[
\lambda_*:=
\frac{\frac32+\frac{a_2}{2}}{1+a_2}.
\]

因为

\[
\lambda_*>rac12,
\]

将 `(Schmidt-budget)` 乘 `lambda_*` 后，其 `M` coefficient与 `(6.1)`
恰好相等，而 `G_0^{rough}` coefficient至少为 1；`Q_2,N_2` 只增加非负
slack。因此

\[
\boxed{
C_*
\le
2+3\lambda_*.
}
\tag{6.2}

即

\[
\boxed{
C_*
\le
2+3\frac{\frac32+\frac12\log_{10}2}
{1+\log_{10}2}
=5.805865360520\ldots.
}
\tag{Final5-collapse}

---

## 7. 与 five-adic dichotomy 合并

`high-funnel-five-adic-dichotomy.md` 把 canonical high funnel分成：

### Tail-short

`high-funnel-defect-optimization.md` 已证明

\[
\boxed{
\limsup\frac nS
\le
\frac{28}{3+5\log_{10}2}
=6.215109404735\ldots.
}
\]

### Defect-heavy

若它试图保持 slope `>6.215109...`，
`high-funnel-denominator-max-lock.md` 会把它压入 `Final-5-lock`。
但本文证明整个 `Final-5-lock` 只有

\[
5.805865360520\ldots
<6.215109404735\ldots.
\]

矛盾。

因此 canonical double-resonant `t_2=1` funnel整体满足 sector bound

\[
\boxed{
\limsup\frac nS
\le
\frac{28}{3+5\log_{10}2}
=6.215109404735\ldots.
}
\tag{Canonical-funnel-bound}

---

## 8. 状态与作用域

- **`已严格完成（sector）`**：full 2-adic overlap charge、`F-lower-full`、
  `Final5-collapse`。
- **`已严格完成（canonical funnel）`**：结合 five-adic dichotomy，得到
  `t_2=1` double-resonant canonical funnel `limsup <= 6.215109404735...`。
- **`失效/降级`**：把 `2-balanced` 视为 Final-5 的唯一可收费二进子支；
  `high-funnel-two-balanced-collapse.md` 仍正确，但已被本文更强的整个
  `Final-5` collapse覆盖。
- **`待证`**：把 sector-level `6.215109...` 与 `core.md` 全 DD 分类的其余
  asymptotic branches重新优化，判断是否得到新的**全 DD**显式 limsup；DD 空性/
  effective absolute height bound仍开放。

# DD remaining high funnel 的 5-adic denominator-max lock

> **依赖：** [`high-funnel-gap-depth.md`](high-funnel-gap-depth.md)、`core.md` 的 integer lift / denominator valuations、`high-funnel-defect-optimization.md` 的 defect-aware stability。
>
> **严格状态：** `已严格完成（remaining high-funnel）`。本文把 slope `>6.215109404735...` 的最后 `Defect-heavy` 候选按第三分母是否承担最大 5-adic denominator depth 分开。
>
> 结论：若 `b_3` 不是 5-adic maximum，则 defect-aware stability 立刻给 `n<6S+O(1)`；因此真正剩余的高 slope支必须满足 `b_3` 为 5-adic maximum。此时 sphere common scale在 `(H,y_3)` 端为零，并且所有 valuation被锁成
> \[
> \boxed{
> B_5=q_5+2g_5,
> \qquad
> m=2q_5+4g_5+n_5,
> \qquad
> v_5(a)=v_5(\Xi)=q_5.
> }
> \]
> 进一步 `T:=k_5-g_5=m-2g_5`，且 `v_5(H-y_3)=T`。

---

## 1. denominator 5-adic maximum 与 ghost coordinates

记

\[
e_i:=v_5(b_i),
\qquad
B_5:=v_5(b_3),
\]

\[
\boxed{E_5:=\max(e_1,e_2,B_5).}
\tag{1.1}

因为

\[
q_{\rm lcm}=\operatorname{lcm}(b_1,b_2,b_3),
\]

有

\[
v_5(q_{\rm lcm})=E_5.
\]

而

\[
y_i=a_i\frac{q_{\rm lcm}}{b_i}.
\]

high funnel已有 `5|b_3`，故 reducedness给

\[
v_5(a_3)=0.
\]

因此

\[
\boxed{v_5(y_3)=E_5-B_5.}
\tag{1.2}

另外

\[
G=b_1b_2,
\]

所以

\[
\boxed{e_1+e_2=g_5.}
\tag{1.3}

---

## 2. sphere factorization 的 exact 5-depth balance

令

\[
D_5:=v_5(H-y_3),
\qquad
s_5:=\min(v_5(H),v_5(y_3)).
\]

`high-funnel-gap-depth.md` 已证明在 remaining branch

\[
\boxed{D_5=m+2q_5+2g_5-2B_5.}
\tag{2.1}

而

\[
s_5\le v_5(y_3)=E_5-B_5.
\]

由 `(1.3)`，

\[
E_5\le\max(B_5,g_5),
\]

所以

\[
\boxed{s_5\le\max(0,g_5-B_5).}
\tag{2.2}

又 `B_5<m`。若 `g_5<=B_5`，则 `s_5=0<D_5`。若 `g_5>B_5`：

\[
D_5-(g_5-B_5)
=m+2q_5+g_5-B_5>0.
\]

因此统一有

\[
\boxed{D_5>s_5.}
\tag{2.3}

5 为奇素数。odd-prime two-factor lemma应用于 `H,y_3` 给

\[
\boxed{v_5(H+y_3)=s_5.}
\tag{2.4}

sphere identity

\[
(H-y_3)(H+y_3)=y_1^2+y_2^2
\]

于是

\[
\boxed{v_5(y_1^2+y_2^2)=D_5+s_5.}
\tag{2.5}

另一方面

\[
y_1^2+y_2^2
=\left(\frac{q_{\rm lcm}}G\right)^2\mathcal N_{12}.
\]

故

\[
\boxed{
D_5+s_5
=2(E_5-g_5)+n_5.
}
\tag{Sphere5-balance}

---

## 3. 若 `b_3` 不是 maximum，则 slope <= 6

设

\[
E_5>B_5.
\]

由 `(1.3)`：

\[
E_5\le g_5.
\]

所以 `Sphere5-balance` 的右边不超过 `n_5`：

\[
D_5+s_5\le n_5.
\]

从而

\[
\boxed{D_5\le n_5.}
\tag{3.1}

用 `(2.1)` 与 high-funnel exact relation

\[
3B_5=m+q_5+2g_5-n_5
\]

消去 `B_5`，得到

\[
\boxed{3D_5=m+4q_5+2g_5+2n_5.}
\tag{3.2}

结合 `D_5<=n_5`：

\[
\boxed{m+4q_5+2g_5\le n_5.}
\tag{3.3}

特别地

\[
2q_5+g_5+n_5\ge m.
\]

而 defect-aware stability给

\[
n<6S+\frac{2b}{3}m
-\frac{2b}{3}(2q_5+g_5+n_5)
-2a\mathfrak q-a\mathfrak n
+O(1).
\]

所以

\[
\boxed{n<6S+O(1).}
\tag{Nonmax-six}

因此任何 remaining sequence若满足 slope `>6.215109...`，最终必须有

\[
\boxed{E_5=B_5.}
\tag{B3-max}

---

## 4. `b_3` maximum 时 `H,y_3` 都是 5-units

由 `(B3-max)` 与 `(1.2)`：

\[
\boxed{v_5(y_3)=0.}
\]

而 `D_5>0`，即

\[
5\mid H-y_3.
\]

所以

\[
H\equiv y_3\not\equiv0\pmod5,
\]

故

\[
\boxed{v_5(H)=0,\qquad s_5=0.}
\tag{4.1}

`Sphere5-balance` 因而化成

\[
\boxed{D_5=2(B_5-g_5)+n_5.}
\tag{4.2}

---

## 5. 解出全部 5-adic variables

一方面 `(2.1)`：

\[
D_5=m+2q_5+2g_5-2B_5.
\tag{5.1}

与 `(4.2)` 比较：

\[
m+2q_5+2g_5-2B_5
=2B_5-2g_5+n_5.
\]

所以

\[
\boxed{m=4B_5-2q_5-4g_5+n_5.}
\tag{5.2}

另一方面 high-funnel resonance给

\[
\boxed{m=3B_5-q_5-2g_5+n_5.}
\tag{5.3}

两式相减：

\[
\boxed{B_5=q_5+2g_5.}
\tag{B-lock}

代回 `(5.3)`：

\[
\boxed{m=2q_5+4g_5+n_5.}
\tag{m-lock}

`high-funnel-gap-depth.md` 已有

\[
3v_5(a)=5q_5+4g_5+n_5-m.
\]

使用 `(m-lock)`：

\[
\boxed{v_5(a)=q_5.}
\tag{a-lock}

而 `v_5(a)=v_5(Xi)`，故

\[
\boxed{v_5(\Xi)=q_5.}
\tag{Xi-lock}

---

## 6. S-unit exponent 与 gap depth也同步锁定

由 tail weight

\[
k_5=m+q_5+g_5-B_5.
\]

使用 `(B-lock)`：

\[
\boxed{k_5=m-g_5.}
\tag{6.1}

定义 high-funnel 5-adic S-unit exponent

\[
\boxed{T:=k_5-g_5.}
\]

于是

\[
\boxed{T=m-2g_5.}
\tag{T-lock}

再由 `(4.2)` 和 `(B-lock)`：

\[
D_5
=2q_5+2g_5+n_5.
\]

而 `(m-lock)` 给

\[
m-2g_5=2q_5+2g_5+n_5.
\]

所以

\[
\boxed{v_5(H-y_3)=D_5=T.}
\tag{Gap-T-lock}

这与旧 extremal terminal 的 `v_5(H-y_3)=T+o(S)` 现象一致，但本文是在 remaining high-funnel branch中由 exact denominator-max ledger重新得到。

---

## 7. 最终 remaining branch 的形状

任何 double-resonant high-funnel sequence若试图保持

\[
\limsup n/S>6.215109404735\ldots,
\]

最终必须同时满足：

\[
\boxed{
\begin{gathered}
B_5=E_5=q_5+2g_5,\\
m=2q_5+4g_5+n_5,\\
v_5(a)=v_5(\Xi)=q_5,\\
T=m-2g_5,\\
v_5(H-y_3)=T,\\
v_5(H)=v_5(y_3)=0.
\end{gathered}}
\tag{Final-5-lock}

这已经不再是 generic defect-heavy region，而是一条非常刚性的 5-adic sheet。

特别地 LP 的 pure common-scale extremizer `q_5=n_5=0` 会退化成

\[
\boxed{
B_5=2g_5,
\qquad
m=4g_5,
\qquad
T=2g_5,
\qquad
v_5(a)=0.
}
\tag{Pure-common}

下一步应专门分析这一类 denominator exponent pattern，而不再对 `q_5,g_5,n_5` 做自由 LP。

---

## 8. 状态摘要

- **`已严格完成`**：`Sphere5-balance`、non-max `b_3` branch `n<6S+O(1)`、`B-lock`、`m-lock`、`a/Xi-lock`、`T/Gap-lock`。
- **`结构压缩`**：remaining slope `>6.215109...` high funnel lies on `Final-5-lock`.
- **`待证`**：pure/common-scale denominator pattern；new global numerical limsup；DD global closure/effective height bound。

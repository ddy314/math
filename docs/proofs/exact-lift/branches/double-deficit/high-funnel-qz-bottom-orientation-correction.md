# DD `q-Z` bottom reader 的 orientation-uniform 修正

> **依赖：** [`high-funnel-qz-two-sheet-split.md`](high-funnel-qz-two-sheet-split.md)、
> [`high-funnel-qz-sheet-reader-collapse.md`](high-funnel-qz-sheet-reader-collapse.md)。
>
> **严格状态：** `已严格完成（技术修正）`。
>
> 前两文件在 complementary-sheet bottom identity 的展示中写了
> `Delta_12/10^d`。该写法只在 `k>=d`（即 `s_2=k-d>=0`）时是整数式。
> DD 中 `k-d` 可以为负，因此 canonical integer reader必须改用
> \[
> h:=\min(k,d),\qquad
> R_{12}:=\Delta_{12}/10^h.
> \]
> 本文给出两种 orientation 的 exact identity，并验证前两文件使用的
> p-adic depth结论、`C_12|bottom-reader` 与 balanced payer theorem 全部保持不变。

---

## 1. bottom determinant

沿用

\[
\Delta_{12}
=a_1 10^k b_2-a_2 10^d b_1,
\]

以及

\[
Q=b_1 10^{m_2}+b_2,
\qquad
A_{12}=a_1 10^{n_2}+a_2.
\]

DD 参数满足

\[
\boxed{k-d=n_2-m_2.}
\tag{1.1}

令

\[
\boxed{h:=\min(k,d),
\qquad R_{12}:=\Delta_{12}/10^h\in\mathbf Z.}
\tag{1.2}

---

## 2. `k>=d` orientation

若

\[
k\ge d,
\qquad t:=k-d=n_2-m_2\ge0,
\]

则

\[
R_{12}=a_1 10^t b_2-a_2b_1.
\]

直接展开：

\[
\begin{aligned}
Qa_1 10^t-b_1A_{12}
&=(b_1 10^{m_2}+b_2)a_1 10^t
-b_1(a_1 10^{m_2+t}+a_2)\\
&=a_1 10^t b_2-a_2b_1.
\end{aligned}
\]

所以

\[
\boxed{
R_{12}=Qa_1 10^{k-d}-b_1A_{12}
\qquad(k\ge d).}
\tag{2.1}

这正是前两文件所使用的 orientation。

---

## 3. `k<d` orientation

若

\[
k<d,
\qquad t:=d-k=m_2-n_2>0,
\]

则

\[
R_{12}=a_1b_2-a_2 10^t b_1.
\]

因为

\[
10^tA_{12}
=a_1 10^{n_2+t}+a_2 10^t
=a_1 10^{m_2}+a_2 10^t,
\]

有

\[
\begin{aligned}
Qa_1-b_1 10^tA_{12}
&=(b_1 10^{m_2}+b_2)a_1
-b_1(a_1 10^{m_2}+a_2 10^t)\\
&=a_1b_2-a_2 10^t b_1.
\end{aligned}
\]

因此

\[
\boxed{
R_{12}=Qa_1-b_1 10^{d-k}A_{12}
\qquad(k<d).}
\tag{3.1}

---

## 4. prefix concat gcd 对两个 orientations 都进入 bottom reader

定义

\[
C_{12}:=(A_{12},Q).
\]

无论 `(2.1)` 还是 `(3.1)`，右边都是 `Q` 的整数倍减去 `A_12` 的整数倍。
所以统一有

\[
\boxed{C_{12}\mid R_{12}.}
\tag{4.1}

特别地，前文件 complementary sheet 上的

\[
D_{\rm comp}\mid C_{12}
\]

仍然推出

\[
\boxed{D_{\rm comp}\mid R_{12}.}
\tag{4.2}

因为所有 `D_ex` primes 都满足 `p\nmid10`，

\[
v_p(R_{12})=v_p(\Delta_{12}).
\]

所以原来的 bottom-depth statement 应理解为

\[
\boxed{
v_p(R_{12})\ge M+e}
\]

或除去 denominator common baseline后

\[
\boxed{v_p(\Theta_{12})\ge e,}
\]

其数值内容完全不变。

---

## 5. gap-sheet 的 Pluecker unit结论也不受 orientation影响

`high-funnel-qz-two-sheet-split.md` 的 gap proof 使用的是 raw determinants

\[
\Delta_{12},\Delta_{13},\Delta_{23}
\]

的 Pluecker identity与 nested carry：

\[
E=10^{m_2}\Delta_{13}+\Delta_{23},
\]

\[
b_1\Delta_{23}-b_2\Delta_{13}+b_3\Delta_{12}=0.
\]

该推导没有除以 `10^d`，因此本来就同时覆盖 `k>=d` 与 `k<d`。
所以

\[
\boxed{
\text{gap sheet}\Longrightarrow
v_p(\Delta_{12})=M
}
\]

以及

\[
v_p(\Theta_{12})=0
\]

无需任何修改。

---

## 6. 对 balanced payer theorem 的影响

balanced payer只使用

\[
D_{\rm comp}\mid C_{12},
\qquad
D_{\rm comp}\mid Z_0,
\]

以及

\[
D_{\rm gap}^2\mid a.
\]

这些结论均与 `k-d` 的符号无关。因此

\[
\boxed{
D_{qZ}^2\mid\gamma\,a\,C_{12}\,Z_0
}
\]

保持严格成立。

同理使用 bottom reader 的版本应写成

\[
\boxed{
D_{qZ}^2
\mid
\gamma\,a\,C_{12}\,|R_{12}|_{\rm nd},
}
\]

其中在 `D_ex` 的 non-decimal support上，`R_12` 与此前的 raw/decimal-normalized
bottom determinant具有相同 p-adic depth；如果继续使用 `Theta_12`，则仍按
\[
\Theta_{12}=\Delta_{12}/(b_1,b_2)
\]
读取 denominator baseline 后的 excess。

---

## 7. 状态摘要

- **修正：**不能全局把 bottom integer reader写成 `Delta_12/10^d`；canonical
  reader是 `Delta_12/10^{min(k,d)}`。
- **保持不变：**two-sheet split、gap bottom-unit、complementary bottom-excess、
  `D_comp|(A_12,Q)`、balanced payer theorem。
- **后续规范：**凡需要普通整数整除时统一使用 `R_12`；只做 `p\nmid10`
  valuation 时可直接使用 raw `Delta_12`，因为 decimal powers都是 p-units。
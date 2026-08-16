# DD frontier decimal remainder collapse — 2026-08-16

> 接续 [`dd-frontier-one-channel-second-order-2026-08-16.md`](dd-frontier-one-channel-second-order-2026-08-16.md)。
> 适用范围为假想 \(6.308883577618\ldots\) terminal frontier。
>
> **核心结论：**terminal numerator reconstruction 中一个原本只按高度观察的巨大 cancellation，实际上落入严格的单个十进制 remainder cell：
> \[
> 0<R_{\rm dec}<10^d.
> \]
> 因而产生 exact `-1 carry` 恒等式。

---

## 1. exact defect

沿用

\[
X=2^HZ,
\qquad
Y=5^TU,
\qquad
V=X-Y,
\qquad
\Sigma=X+Y.
\]

前一文件已经严格得到

\[
\boxed{
\Sigma R_0
=g_0\bigl(B10^dVA_{12}-Ua_3\bigr).
}
\tag{1.1}
\]

定义

\[
\boxed{
R_{\rm dec}:=
B10^dVA_{12}-Ua_3.
}
\tag{1.2}
\]

则

\[
\boxed{
R_{\rm dec}=\frac{\Sigma R_0}{g_0}.
}
\tag{1.3}
\]

所有量均为正，terminal normalization 中 \(R_0>0\)，故

\[
\boxed{R_{\rm dec}>0.}
\tag{1.4}
\]

---

## 2. 关键尺度：\(R_0\) 只有 subexponential height

secondary Gaussian coefficient 在 terminal 中写成

\[
B_*:=\widetilde rR_0,
\]

且已有

\[
\log|B_*|=o(S).
\]

由于 \(\widetilde r\in\mathbf Z_{>0}\)，得到

\[
\boxed{\log R_0=o(S).}
\tag{2.1}
\]

同样 \(g_0\ge1\)，所以 `(1.3)` 给

\[
\log R_{\rm dec}
\le
\log\Sigma+o(S).
\]

frontier phase 中

\[
\log\Sigma=2S+o(S),
\]

故

\[
\boxed{
\log R_{\rm dec}
\le2S+o(S).
}
\tag{2.2}
\]

另一方面

\[
\frac dS\to3.5.
\]

因此 sufficiently large frontier 上

\[
\boxed{
0<R_{\rm dec}<10^d.
}
\tag{Decimal-cell}
\]

这里存在 \(1.5S-o(S)\) 的严格指数余量。

---

## 3. reducedness 保证余数非零

terminal third denominator 含有大 \(2,5\)-smooth factor；特别是 sufficiently large frontier 上

\[
10\mid b_3.
\]

由

\[
(a_3,b_3)=1
\]

得到

\[
(a_3,10)=1.
\]

又

\[
(U,10)=1,
\]

所以

\[
\boxed{(Ua_3,10)=1.}
\tag{3.1}
\]

因此

\[
Ua_3\not\equiv0\pmod{10^d}.
\]

写 Euclidean division

\[
Ua_3=K10^d+r,
\qquad
1\le r<10^d.
\tag{3.2}
\]

---

## 4. exact `-1 carry`

由 `(1.2)`：

\[
R_{\rm dec}
=BVA_{12}10^d-(K10^d+r)
=(BVA_{12}-K)10^d-r.
\]

结合

\[
0<R_{\rm dec}<10^d,
\qquad
1\le r<10^d,
\]

唯一可能是

\[
\boxed{BVA_{12}-K=1.}
\tag{4.1}
\]

并且

\[
\boxed{R_{\rm dec}=10^d-r.}
\tag{4.2}
\]

所以得到新的 exact digit-carry identity：

\[
\boxed{
\left\lfloor\frac{Ua_3}{10^d}\right\rfloor
=BVA_{12}-1.
}
\tag{Carry-floor}
\]

等价地

\[
\boxed{
BVA_{12}
=\left\lceil\frac{Ua_3}{10^d}\right\rceil.
}
\tag{Carry-ceil}
\]

以及

\[
\boxed{
Ua_3
=(BVA_{12}-1)10^d
+\bigl(10^d-R_{\rm dec}\bigr).
}
\tag{4.3}
\]

这比仅仅知道

\[
B10^dVA_{12}=Ua_3+10^{2S+o(S)}
\]

强得多：cancellation 已经被定位到唯一 decimal carry cell。

---

## 5. 与 primitive determinant 的 exact 对接

全局 DD determinant 为

\[
E
=b_3A_{12}10^d-a_3Q.
\tag{5.1}
\]

terminal normalization 有

\[
Q=JUq_c\theta,
\]

\[
b_3=BJVq_c\theta.
\]

因此

\[
\begin{aligned}
E
&=Jq_c\theta
\bigl(BVA_{12}10^d-Ua_3\bigr)\\
&=Jq_c\theta R_{\rm dec}.
\end{aligned}
\]

故得到

\[
\boxed{
E=Jq_c\theta R_{\rm dec}.
}
\tag{Det-remainder}
\]

再用 `(1.3)`：

\[
\boxed{
E
=Jq_c\theta\frac{\Sigma R_0}{g_0}.
}
\tag{5.2}
\]

所以 terminal primitive determinant 的最后 defect 并不是新的自由整数；它等于 clean source rough factor \(q_c\) 乘上一个严格位于单 decimal cell 内的 remainder。

---

## 6. 新的结构性含义

`(Carry-floor)` 把 frontier numerator 约束改写成：

\[
\boxed{
\text{一个真实乘积 }Ua_3
\text{ 的前 }(n_3+\log U-d)\text{ 位，}
\text{恰好等于 }BVA_{12}-1.
}
\]

同时低 \(d\) 位的 complement 为

\[
R_{\rm dec}
=10^d-(Ua_3\bmod10^d)
=10^{2S+o(S)},
\]

因此低 \(d\)-digit residue 实际位于 interval 顶端：

\[
\boxed{
Ua_3\bmod10^d
=10^d-10^{2S+o(S)}.
}
\tag{Top-residue}
\]

相对整个 \(10^d\) 模长，它距离上端只有

\[
10^{-1.5S+o(S)}
\]

的比例。

这已经是一个真正的 `CRT remainder window`：任何后续独立的 \(2\)-adic / \(5\)-adic / Gaussian residue 若能把 \(Ua_3\bmod10^d\) 排除在该顶端薄层之外，就会直接关闭 terminal frontier。

---

## 7. 当前下一击

后续不应再把 `(1.1)` 当作普通 height cancellation。首选目标改成：

1. 将 `Top-residue` 分别投影到 \(2^d\)、\(5^d\)；
2. 使用 \((a_3,b_3)=1\)、\((U,10)=1\) 与 terminal source phase 确定 \(Ua_3\) 的 inverse class；
3. 与 pair-max / second-order \(A_{12}\) CRT 对齐；
4. 争取证明唯一 residue class 到 \(10^d\) 上端的距离至少为 \(10^{(2+\varepsilon)S}\)，与实际 \(10^{2S+o(S)}\) 冲突。

这条路线有真实的 \(1.5S\) remainder margin，和此前多个 leading-order critical equalities不同。

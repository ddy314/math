# DD frontier one-channel collapse 与二阶 \(A_{12}\) CRT — 2026-08-16

> 本文接续 terminal frontier、rational-contact frontier 与 Good continuation。
> 适用范围为假想
> \[
> \frac{n_3}{S}\to6.308883577618\ldots
> \]
> 的无界 DD frontier sequence；第 4 节以后进一步进入 full rational-contact main branch。
>
> **核心推进：**
> 1. frontier 的 moving pair-max rough mass 在 leading order 上只剩 \(b_2\)-\(b_3\) 单一通道；
> 2. 将旧 §67 只记录“存在”的 \(A_{12}\bmod q_c^2\) 与 \(A_{12}\bmod C_L\) 两条线性同余显式恢复；
> 3. 说明 \(C_L\)-侧信息确实只在除去第一份 Gaussian rational-contact core 后出现，是一个真正的二阶 quotient residue。

---

## 1. moving pair-max core 的单通道坍缩

一般 DD 的 reduced-tail moving odd core 写作

\[
V=v_1v_2
\]

（这里删去旧记号中所有 \(2,5\)-part；terminal normalization 已有 \((V,10)=1\)），其中：

- \(v_1\) 对应 pair-max \((b_1,b_3)\)；
- \(v_2\) 对应 pair-max \((b_2,b_3)\)。

canonical denominator normal form 给

\[
b_1=h\,v_1B_1,
\qquad
b_2=h\,v_2B_2,
\qquad
b_3=h\,v_1v_2B_3,
\tag{1.1}
\]

且 \((B_1B_2B_3,v_1v_2)=1\)。

frontier digit shape 为

\[
(m_1,m_2;n_1,n_2)
=(o(S),S-o(S);S-o(S),o(S)).
\tag{1.2}
\]

因此

\[
b_1<10^{m_1}=10^{o(S)}.
\]

由 \(v_1\mid b_1\)：

\[
\boxed{\log v_1=o(S).}
\tag{1.3}
\]

另一方面 terminal phase 给

\[
V=C_Lv_0,
\qquad
\log C_L=S+o(S),
\qquad
\log v_0=o(S).
\tag{1.4}
\]

所以

\[
\boxed{\log v_2=S+o(S).}
\tag{1.5}
\]

换言之，删去 norm \(10^{o(S)}\) 的 exceptional core 后，整个 moving pair-max core 都在 \((b_2,b_3)\) channel：

\[
\boxed{v_2=C_L\cdot10^{o(S)}.}
\tag{One-channel}
\]

特别地，因为 \(m_2=S+o(S)\)，

\[
\boxed{b_2=C_L\cdot10^{o(S)}}
\tag{1.6}
\]

按 logarithmic height 理解。

对应 sphere divisibilities 统一为

\[
\boxed{C_L\mid H_{\rm sph},\ y_1}
\tag{1.7}
\]

以及 oriented pair-max

\[
\boxed{\Pi^2\mid y_2+i y_3,\qquad N(\Pi)=C_L}
\tag{1.8}
\]

均只差 norm \(10^{o(S)}\) 的 exceptional core。

**结论：**frontier 后续无需继续保留两个指数级 pair-max channels；\(b_1\)-\(b_3\) 一侧只有 subexponential mass。

---

## 2. 一个 exact numerator bridge

沿用

\[
X=2^HZ,
\qquad
Y=5^TU,
\qquad
V=X-Y,
\qquad
\Sigma:=X+Y.
\]

已有 exact reconstruction

\[
UA_0+R_0=g_0B10^dA_{12},
\tag{2.1}
\]

以及前一 continuation 得到

\[
\boxed{g_0\alpha=\Sigma A_0.}
\tag{2.2}
\]

其中

\[
\alpha=A_{12}10^{n_3}+a_3,
\qquad
n_3=m+d,
\]

并且

\[
\frac{10^m}{B}=2\cdot5^T.
\tag{2.3}
\]

将 `(2.2)` 代入 `(2.1)`：

\[
\begin{aligned}
\Sigma R_0
&=g_0\left(
B10^d\Sigma A_{12}-U\alpha
\right)\\
&=g_0\left[
\bigl(B10^d\Sigma-U10^{m+d}\bigr)A_{12}-Ua_3
\right].
\end{aligned}
\]

由

\[
\Sigma-2\cdot5^TU=V
\]

及 `(2.3)`：

\[
B10^d\Sigma-U10^{m+d}
=B10^dV.
\]

因此得到 exact identity

\[
\boxed{
\Sigma R_0
=g_0\bigl(B10^dVA_{12}-Ua_3\bigr).
}
\tag{R0-A12}
\]

这是后续两个 CRT residues 的共同起点。

---

## 3. 显式恢复 \(A_{12}\bmod q_c^2\)

clean source 为

\[
VA_0-5^TR_0=q_c^2L_{\rm clean}.
\tag{3.1}
\]

乘以 \(\Sigma\)，再用 `(2.2)` 与 `(R0-A12)`：

\[
\begin{aligned}
\Sigma q_c^2L_{\rm clean}
&=g_0V\alpha
-g_0 5^T(B10^dVA_{12}-Ua_3)\\
&=g_0\left[
V(10^{m+d}-5^TB10^d)A_{12}
+(V+5^TU)a_3
\right].
\end{aligned}
\]

由

\[
10^m=2\cdot5^TB,
\qquad
V+5^TU=X,
\]

得到

\[
\boxed{
\Sigma q_c^2L_{\rm clean}
=g_0\bigl(
5^TB10^dVA_{12}+Xa_3
\bigr).
}
\tag{QCRT-exact}
\]

因此在删去 \((q_c,g_0BVa_3)=10^{o(S)}\) 的 coefficient overlap 后，得到有效线性同余

\[
\boxed{
5^TB10^dV\,A_{12}
\equiv-Xa_3
\pmod{q_c^2/10^{o(S)}}.
}
\tag{QCRT}
\]

其有效模量高度为

\[
\boxed{
2\log q_c
=0.617767155236\ldots S+o(S).
}
\tag{3.2}
\]

这就是旧 §67 中未显式写出的第一条 residue。

---

## 4. 为什么一阶模 \(C_L\) 看不到 \(A_{12}\)

`(R0-A12)` 中

\[
C_L\mid V.
\]

所以直接模 \(C_L\) 时，\(A_{12}\) 的 coefficient 整体消失：

\[
\Sigma R_0
\equiv-g_0Ua_3
\pmod{C_L}.
\tag{4.1}
\]

因此任何只停留在 rational first-order reconstruction 的尝试，都不可能得到 \(A_{12}\bmod C_L\)。

这解释了旧 §67 的第二条 congruence 为什么必须来自 **除去第一份 pair-max / rational-contact core 之后的 quotient level**。

---

## 5. 显式恢复二阶 Gaussian \(C_L\)-residue

进入 full rational-contact branch。令

\[
E=D_+D_-,
\qquad
V=Ee_0,
\]

并取

\[
\Gamma:=\Pi_+\overline{\Pi_-},
\qquad
N(\Gamma)=E.
\tag{5.1}
\]

axis factorization 为

\[
C_*+iR_0=\Gamma\overline K,
\tag{5.2+}
\]

\[
C_*-iR_0=\overline\Gamma K,
\tag{5.2-}
\]

其中

\[
C_*:=\frac{g_0a_2B}{2}.
\]

将 `(R0-A12)` 代入 `(5.2+)` 并乘以 \(\Sigma\)：

\[
\Sigma\Gamma\overline K
=
\Sigma C_*
-i g_0Ua_3
+i g_0B10^dV A_{12}.
\]

使用

\[
V=Ee_0=N(\Gamma)e_0
=\Gamma\overline\Gamma e_0,
\]

得到

\[
\Sigma C_*-i g_0Ua_3
=\Gamma\left(
\Sigma\overline K
-i g_0B10^de_0\overline\Gamma A_{12}
\right).
\]

因此

\[
\boxed{
M_+:=
\frac{\Sigma C_*-i g_0Ua_3}{\Gamma}
\in\mathbf Z[i].
}
\tag{5.3+}
\]

并且

\[
\boxed{
\Sigma\overline K-M_+
=i g_0B10^de_0\overline\Gamma A_{12}.
}
\tag{A12-second+}
\]

完全对称地：

\[
\boxed{
M_-:=
\frac{\Sigma C_*+i g_0Ua_3}{\overline\Gamma}
\in\mathbf Z[i],
}
\tag{5.3-}
\]

\[
\boxed{
\Sigma K-M_-
=-i g_0B10^de_0\Gamma A_{12}.
}
\tag{A12-second-}
\]

这两式是 **exact second-order quotient identities**。

---

## 6. 第二条 \(A_{12}\) residue 的有效 rational modulus

从 `(A12-second+)` 模 \(\Gamma\)：

\[
\boxed{
 i g_0B10^de_0\overline\Gamma A_{12}
\equiv
\Sigma\overline K-M_+
\pmod\Gamma.
}
\tag{GCRT+}
\]

main mass 上：

\[
N\gcd_{\mathbf Z[i]}(\Gamma,\overline\Gamma)
=10^{o(S)},
\]

并且 coefficient overlap

\[
N\gcd_{\mathbf Z[i]}
(\Gamma,g_0B10^de_0\Sigma)
=10^{o(S)}.
\]

因此 `(GCRT+)` 对 rational integer \(A_{12}\) 给出的有效 period 为

\[
\boxed{
E/10^{o(S)}
=10^{S+o(S)}.
}
\tag{6.1}
\]

理由是：删去 conjugate exceptional core 后，映射

\[
\mathbf Z\longrightarrow\mathbf Z[i]/(\Gamma)
\]

的 kernel 为

\[
(N\Gamma)=(E).
\]

所以旧 §67 所称的“模 \(C_L\) 线性同余”可以更精确地表述成 `(GCRT+)`：它来自第一次 rational/Gaussian core 除法后的 second-order quotient residue。

---

## 7. §67 的 \(1.617767\ldots S\) 联合模量由此完全显式化

`(QCRT)` 的有效高度为

\[
0.617767155236\ldots S+o(S),
\]

`(GCRT+)` 的有效高度为

\[
S+o(S).
\]

又有

\[
(q_c,C_L)=1,
\]

且 full rational 中 \(E=C_L\cdot10^{o(S)}\)。故两个 effective periods 只有 \(10^{o(S)}\) overlap。

因此联合 modulus 高度为

\[
\boxed{
1.617767155236\ldots S+o(S).
}
\tag{7.1}
\]

而

\[
\log A_{12}=S+o(S).
\]

从而重新严格得到

\[
\boxed{\#\{A_{12}\}\le1}
\]

对固定 terminal denominator-tail / axis data成立。

与旧文相比，新的内容是两个 residue 的 **显式 exact parents** `(QCRT-exact)` 与 `(A12-second+)` 已经写出。

---

## 8. 新的状态边界

这次展开同时证明了一个重要 no-go：

\[
\boxed{
\text{任何 first-order }C_L\text{ elimination 都看不到 }A_{12};
}
\]

因为它的 coefficient 必然带 \(V\)，见 `(4.1)`。

真正的 \(A_{12}\bmod C_L\) 信息只在除去第一份 \(\Gamma\) 后出现。

因此下一步若要把“至多一个 \(A_{12}\)”升级为 emptiness，目标已经非常具体：

> 对 `(QCRT)` 与 `(GCRT+)` 的唯一 CRT lift 做 **digit-shell location**，证明该 lift 无法落入
> \[
> 10^{S+o(S)-1}\le A_{12}<10^{S+o(S)}
> \]
> 的合法十进制窗口，或者证明 `(GCRT+)` 的 Gaussian phase 与 `(QCRT)` 的 rational residue 在 full rational Good / genuine-Gaussian 两支中不兼容。

继续制造 first-order resultant 不会触及这个问题。

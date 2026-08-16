# A1 second-repunit 5-adic saturation dichotomy — 2026-08-16

本文继续 second-repunit edge，并与
`a1-repunit-lower-endpoint-5adic-closure-2026-08-16.md` 联立。

当前已有

\[
\boxed{
 b_3=10^{\ell-1}+f,
\qquad f>0,
}
\]

以及

\[
0<f<\frac18\,10^{\ell-2k}.
\]

本文证明五进通道只有两个极端选择：

\[
\boxed{
\begin{array}{ll}
\text{5-unsaturated:}&v_5(10^{m_1}-b_1)=k-1,\\[0.4em]
\text{5-saturated:}&\ell>6.643856\ldots\,k+0.678071\ldots.
\end{array}}
\]

本文结论均为 **已严格完成**。

---

## 1. 记号

保持 second-repunit edge：

\[
g=0,
\qquad
n_2=2k,
\]

\[
a_2=10^{2k}-1,
\qquad
b_2=10^{k-1}.
\]

所以

\[
\boxed{v_5(b_2)=k-1.}
\tag{1}
\]

写

\[
\boxed{s=\ell-2k>0.}
\]

第三分母已经证明不能等于十进制下端点，因此

\[
\boxed{b_3=10^{\ell-1}+f,\qquad f>0.}
\tag{2}
\]

并有端点上界

\[
\boxed{f<\frac18\,10^s.}
\tag{3}
\]

---

# 2. 5-unsaturated 时第一分母指数被锁死

先设

\[
\boxed{e_3:=v_5(b_3)<\ell.}
\tag{4}
\]

安全五进 unsaturated sieve 已证明此时最大赋值形状只能是：

1. third unique max；
2. triple tie；
3. prefix pair-max。

由 (1)，逐种看：

### third unique max

\[
e_3>e_1=e_2,
\]

故

\[
e_1=e_2=k-1;
\]

### triple tie

\[
e_1=e_2=e_3,
\]

故仍然

\[
e_1=k-1;
\]

### prefix pair-max

\[
e_1=e_2>e_3,
\]

所以同样

\[
e_1=e_2=k-1.
\]

因此无论是哪一种允许形状：

\[
\boxed{v_5(b_1)=k-1.}
\tag{5}
\]

写最高层 normal form

\[
\boxed{b_1=10^{m_1}-d,\qquad d\ge1.}
\]

因为 `m_1>k`，模 `5^k` 立即得到

\[
\boxed{v_5(d)=k-1.}
\tag{6}
\]

所以 5-unsaturated side 的第一分母 deficit 始终携带精确增长的 `5^{k-1}`。

---

# 3. 5-saturated 强迫第三 excess 极大

现在设

\[
\boxed{v_5(b_3)\ge\ell.}
\tag{7}
\]

基项

\[
10^{\ell-1}
\]

的五进赋值恰为

\[
\ell-1.
\]

由

\[
b_3=10^{\ell-1}+f
\]

要使和的赋值至少为 `\ell`，两项首先必须具有相同的最低五进赋值。因此

\[
\boxed{v_5(f)=\ell-1.}
\tag{8}
\]

特别地

\[
\boxed{f\ge5^{\ell-1}.}
\tag{9}
\]

与端点上界 (3) 联立：

\[
5^{\ell-1}
<\frac18\,10^s.
\tag{10}
\]

代入

\[
\ell=2k+s.
\]

取常用对数：

\[
(2k+s-1)\log_{10}5
<s-\log_{10}8.
\]

利用

\[
1-\log_{10}5=\log_{10}2
\]

整理得

\[
\boxed{
 s>
\frac{2\log_{10}5}{\log_{10}2}k
+
\frac{\log_{10}8-\log_{10}5}{\log_{10}2}.
}
\]

即

\[
\boxed{
 s>
2\log_2 5\,k+3-\log_2 5.
}
\tag{11}
\]

数值上

\[
\boxed{
 s>4.643856189\ldots\,k+0.678071905\ldots.
}
\tag{12}
\]

因此

\[
\boxed{
\ell=2k+s
>6.643856189\ldots\,k+0.678071905\ldots.
}
\tag{13}
\]

---

# 4. 最终五进二选一

second-repunit edge 的任意剩余候选必须满足以下之一：

### 5-unsaturated

\[
\boxed{
v_5(10^{m_1}-b_1)=k-1.
}
\]

### 5-saturated

\[
\boxed{
\ell>6.643856189\ldots\,k+0.678071905\ldots.
}
\]

所以在任何第三尾斜率显著低于 `6.64` 的潜在无界族中，都自动进入第一种状态，第一块十进制 deficit 的五进深度被精确锁为 `k-1`。

这给后续 p-adic exact-polynomial 分析提供了一个无界参数随 `k` 线性增长的固定 valuation 输入。
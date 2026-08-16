# A1 second-repunit minimal-third 2/5 sieve — 2026-08-16

本文继续 second-repunit edge：

\[
\boxed{
 g=0,
\quad n_2=2k,
\quad a_2=10^{2k}-1,
\quad b_2=10^{k-1},
\quad m_1\ge4k+1.
}
\]

前文已证明

\[
\ell\ge2k+1.
\]

本文专门分析最小第三尾边界

\[
\boxed{\ell=2k+1.}
\]

核心结论：

\[
\boxed{
 b_3=10^{2k},
\quad
 a_3=10^{2k+1}-h,
\quad
 h\in\{1,3,7,9,11\},
}
\]

并且

\[
\boxed{v_5(b_1)=k-1.}
\]

若写 `b_1=10^{m_1}-d_1`，则更有

\[
\boxed{v_5(d_1)=k-1.}
\]

本文结论均为 **已严格完成**。

---

## 1. 旧 third-edge 常数核

由 `a1-top-layer-third-block-edge-2026-08-16.md`，若

\[
\ell=2k+1,
\]

则第三块只能写成

\[
\boxed{
 a_3=10^{2k+1}-h,
\qquad1\le h\le11,
}
\tag{1}
\]

\[
\boxed{
 b_3=10^{2k}+f,
\qquad f\in\{0,1\}.
}
\tag{2}
\]

下面用安全 `2/5`-adic 定理进一步筛掉大部分类型。

---

# 2. `f=1` 与安全二进最大定理矛盾

先假设

\[
f=1.
\]

则

\[
b_3=10^{2k}+1
\]

为奇数，所以

\[
\boxed{e_3:=v_2(b_3)=0<\ell.}
\tag{3}
\]

安全二进 dichotomy 已证明：若 `e_3<\ell`，第三块必须取得唯一二进最大值：

\[
\boxed{e_3>v_2(b_1),v_2(b_2).}
\tag{4}
\]

### 若 `k\ge2`

本边缘

\[
b_2=10^{k-1},
\]

所以

\[
v_2(b_2)=k-1\ge1>e_3,
\]

与 (4) 直接矛盾。

### 若 `k=1`

此时

\[
b_2=1,
\qquad v_2(b_2)=0=e_3.
\]

若 `b_1` 为奇数，则三个 denominator 的二进最大值都为 `0`，违反整数球面已经证明的“最大二进指数唯一取得”。

若 `b_1` 为偶数，则二进最大值位于前缀，而安全 dichotomy 强迫

\[
e_3\ge\ell,
\]

仍与 `e_3=0<\ell` 矛盾。

所以所有 `k\ge1` 都有

\[
\boxed{f\ne1.}
\]

因此

\[
\boxed{f=0,
\qquad b_3=10^{2k}.}
\tag{5}

---

# 3. 五进 unsaturated 强迫第三块 unique max

由 (5)：

\[
\boxed{v_5(b_3)=2k.}
\tag{6}

另一方面

\[
\ell=2k+1,
\]

故

\[
\boxed{v_5(b_3)<\ell.}
\tag{7}

即当前处于五进 unsaturated side。

第二块满足

\[
b_2=10^{k-1},
\]

所以

\[
\boxed{v_5(b_2)=k-1<2k.}
\tag{8}

安全五进 unsaturated sieve 已证明，允许的最大指数形状只有：

1. third unique max；
2. triple tie；
3. prefix pair-max。

但 (6)、(8) 立即排除 triple tie 与 prefix pair-max：第二块指数已经严格低于第三块。

因此当前只能是

\[
\boxed{
 v_5(b_3)=2k
>
v_5(b_1)=v_5(b_2).
}
\tag{9}

odd denominator prime graph 中 unique max 强迫另外两块指数相等，于是由 (8)：

\[
\boxed{v_5(b_1)=k-1.}
\tag{10}

---

# 4. 第三分子的 constant core 缩成五类

由 (1)、(5)：

\[
a_3=10^{2k+1}-h,
\qquad
b_3=10^{2k}.
\]

原问题要求

\[
\gcd(a_3,b_3)=1.
\]

而 `b_3` 的全部素因子只有 `2,5`。模 `2`、模 `5`：

\[
a_3\equiv-h.
\]

所以必须

\[
\boxed{\gcd(h,10)=1.}
\tag{11}

在

\[
1\le h\le11
\]

中只剩

\[
\boxed{h\in\{1,3,7,9,11\}.}
\tag{12}

因此最小第三边界从原来的 `22` 个 `(h,f)` 类型缩成恰好 `5` 个 `h` 类型。

---

# 5. 第一分母 deficit 必须精确携带 `5^{k-1}`

最高层 normal form 写成

\[
\boxed{b_1=10^{m_1}-d_1,}
\qquad d_1\ge1.
\tag{13}

这里

\[
m_1\ge4k+1>k.
\]

所以

\[
5^k\mid10^{m_1}.
\]

由 (13) 模 `5^k`：

\[
b_1\equiv-d_1\pmod{5^k}.
\]

而 (10) 给出

\[
v_5(b_1)=k-1.
\]

因此 `b_1` 模 `5^k` 恰被 `5^{k-1}` 整除而不被 `5^k` 整除。相同性质必须由 `-d_1` 承担：

\[
\boxed{v_5(d_1)=k-1.}
\tag{14}

这是一个很强的 moving-prefix arithmetic constraint：第一分母虽然靠近十进制上端点，但它与 `10^{m_1}` 的 deficit 本身必须含有精确深度 `5^{k-1}`。

---

# 6. 二进侧的同时约束

当前

\[
b_3=10^{2k}
\]

还满足

\[
v_2(b_3)=2k<\ell=2k+1.
\]

安全二进 dichotomy 因而强迫第三块也是唯一二进最大：

\[
\boxed{
 v_2(b_1)<2k,
\qquad
v_2(b_2)=k-1<2k.
}
\tag{15}

由于 `m_1>2k`，从

\[
b_1=10^{m_1}-d_1
\]

模 `2^{2k}` 同样得到

\[
\boxed{v_2(d_1)=v_2(b_1)<2k.}
\tag{16}

所以当前 prefix deficit `d_1` 同时满足

\[
\boxed{
v_5(d_1)=k-1,
\qquad
v_2(d_1)<2k.
}
\]

---

# 7. 当前最小第三边界核心

second-repunit edge 上若

\[
\ell=2k+1,
\]

则所有候选已经被压成：

\[
\boxed{
 b_3=10^{2k},
\quad
 a_3=10^{2k+1}-h,
\quad
h\in\{1,3,7,9,11\},
}
\]

以及第一块 deficit 的精确局部条件

\[
\boxed{
v_5(10^{m_1}-b_1)=k-1.
}
\]

所以这条最小第三边界不再含任意第三块 mantissa；第三块只剩五个固定 `h`，而第一块 offset 被迫携带增长中的 `5^{k-1}` 深度。

下一步可把这一精确 `5`-进 deficit 与 repunit escape polynomial 的 leading factor

\[
L=-5RS+100Rf+10Rh+10Sd+Se
\]

联立，继续压缩 `m_1-4k` 的逃逸方向。
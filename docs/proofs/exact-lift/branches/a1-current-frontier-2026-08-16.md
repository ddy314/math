# A1 current frontier — 2026-08-16

本文只汇总 `A_1` 当前严格证明边界，作为后续继续研究的入口。详细推导见同目录各专门文件。

---

## 1. 全局结构已经压成四个位数层

A1 条件：

\[
s_3\le0,
\qquad
s_2+s_3>0.
\]

记

\[
g=-s_3\ge0,
\qquad
k=s_2+s_3\ge1.
\]

已经严格证明

\[
\boxed{\ell=n_3,}
\]

以及无任何低尺度例外的全局位数带

\[
\boxed{
 g-1\le s_1\le g+2.
}
\]

所以 A1 只剩

\[
\boxed{s_1-g\in\{-1,0,1,2\}.}
\]

---

## 2. 第三块 fixed-prefix 无界性已经关闭

直接从原拼接式建立 rational-contact：

\[
R=\frac{P+\theta r_3}{1+\theta},
\qquad
\frac1{10Q}\le\theta<\frac1Q.
\]

安全整数平方证书：

\[
W^2=T^2K-2Tb_3DN.
\]

安全 denominator certificate：

\[
\boxed{b_3\mid T^2D^2G.}
\]

结合 `2/5` resonance、同向非 resonance、两个 cross corridors 与
`\gcd(a_3,b_3)=1`，得到：

\[
\boxed{
\text{任意固定前两块下，A1 第三块候选集合有限。}
}
\]

这不等于全局 A1 空性；移动前缀仍无界。

---

## 3. 旧第三分子正规化已被安全替代

旧公共框架的

\[
z_3=a_3/\delta_3,
\qquad
\delta_3=\gcd(10^\ell,b_3)
\]

不能在 `\delta_3>1` 时作为无条件整数正规化，因为

\[
\gcd(a_3,b_3)=1.
\]

当前 A1 只使用安全 gap：

\[
10^\ell E=b_3U,
\]

\[
U=LA,
\qquad
E=\tau A,
\]

以及

\[
LA(H+y_3)=y_1^2+y_2^2.
\]

安全 Vieta 因子对：

\[
\boxed{
(TGC-W)(TGC+W)=TDN(TD+2b_3).
}
\]

---

## 4. Odd prime flow 已基本分类

对任意

\[
p\equiv3\pmod4,
\]

第三分母完整 prime power 满足

\[
\boxed{v_p(b_3)\le v_p(Q).}
\]

对任意奇素数 `p\ne5`，若

\[
v_p(b_3)>v_p(Q),
\]

则只能有

\[
p\equiv1\pmod4
\]

且为 prefix--third pair-max。

若指数差为 `d`，该异常满足深度 `2d` 的 `\sqrt{-1}` Hensel 锁；其赋值 ledger 已精确化为

\[
v_p(N)=2e,
\quad
v_p(K)=4e,
\quad
v_p(V)=2e,
\quad
v_p(F_-)=v_p(F_+)=2e,
\]

并有

\[
\boxed{v_p(H)=d+v_p(\alpha).}
\]

---

## 5. 安全 `2/5` 通道

### 二进

若前缀 denominator 取得二进最大，则

\[
\boxed{v_2(b_3)\ge\ell.}
\]

若

\[
v_2(b_3)<\ell,
\]

则第三块必须 unique max，并有显式 `\ell` 上界：

\[
\ell\le
\begin{cases}
3e_3-2M-1,&e_1\ne e_2,\\
3e_3-2M,&e_1=e_2.
\end{cases}
\]

### 五进

若

\[
v_5(b_3)<\ell,
\]

最大指数形状只剩：

1. third unique max；
2. triple tie；
3. prefix pair-max。

其余 prefix unique-max 与 prefix--third pair-max 已排除。

---

# 6. 最高层 `s_1=g+2`

最高层具有极端十进制 normal form，并已证明

\[
\boxed{m_1\ge2k,
\qquad n_2\ge2k.}
\]

双边界

\[
m_1=n_2=2k
\]

为空。

第一边界

\[
m_1=2k
\]

已经整条关闭。

第二边界

\[
n_2=2k
\]

只剩 second-repunit edge：

\[
\boxed{
 g=0,
\quad
 a_2=10^{2k}-1,
\quad
 b_2=10^{k-1}.
}
\]

---

# 7. Second-repunit edge 的当前压缩

已经证明

\[
\boxed{m_1\ge4k+1.}
\]

第三块满足

\[
\boxed{\ell\ge2k+2.}
\]

更强地，第三分母不能处于任意 lower decimal endpoint：

\[
\boxed{b_3\ne10^{\ell-1}.}
\]

写

\[
b_3=10^{\ell-1}+f,
\qquad f>0,
\]

则安全二进结构强迫

\[
\boxed{2^k\mid f.}
\]

因此

\[
\boxed{
10^{\ell-2k}>8\cdot2^k,
}
\]

即

\[
\boxed{
\ell>2.301029995\ldots\,k+0.903089986\ldots.
}
\]

同时 exact-polynomial Cauchy bound 给出整体 escape cone：

\[
\boxed{
 m_1\ge5k-3
\quad\text{或}\quad
\ell\ge3k-3.
}
\]

五进还有更强二选一：

\[
\boxed{
\begin{array}{ll}
5\text{-unsaturated}:&v_5(10^{m_1}-b_1)=k-1,\\[0.4em]
5\text{-saturated}:&\ell>6.643856189\ldots\,k+0.678071905\ldots.
\end{array}}
\]

所以在任何 moderate-tail 候选中，第一分母 deficit 都携带精确增长的 `5^{k-1}`。

---

## 8. 已关闭的最高层有限边界核

第一 slope-2 repunit edge：全空。

`slope-4` 第一块与最小第三尾的双边界：全空。

此前最小第三尾 `\ell=2k+1`：现已作为更一般的 `b_3=10^{\ell-1}` 5-adic closure 的特例被覆盖。

对应符号/有限证书：

- `scripts/check_a1_slope4_double_boundary.py`；
- `scripts/check_a1_repunit_escape_cone.py`；
- `scripts/check_a1_minimal_third_5adic.py`；
- `scripts/check_a1_repunit_lower_endpoint_5adic.py`。

这些脚本只验证已经数学有限化的常数类型或符号 coefficient/monomial ledger，不枚举无界 `k` 代替证明。

---

# 9. 真正剩余核心

目前尚未证明 A1 全局为空。

剩余大块为：

### (A) 三个较低位数层

\[
\boxed{s_1-g\in\{-1,0,1\}.}
\]

它们没有最高层那种四端点同时逼近 1 的特殊结构，需要更多依赖整数球面、safe Vieta 与 prime flow。

### (B) 最高层严格内部锥

\[
s_1=g+2,
\qquad
m_1>2k,
\qquad
n_2>2k,
\]

其中 second-repunit edge 只是最外边缘之一；严格内部仍未全闭。

### (C) second-repunit escape region

即同时满足最新斜率与 `2/5` 局部约束的远端区域。

后续研究应优先寻找跨位数层的整数/局部不变量，而不是继续依赖 fixed-prefix finite 枚举。
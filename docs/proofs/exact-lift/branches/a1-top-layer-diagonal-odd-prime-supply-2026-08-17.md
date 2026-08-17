# A1 top-layer minimal diagonal odd-prime supply — 2026-08-17

本文在 minimal diagonal

\[
d=2,\qquad r=s=1,\qquad k=g
\]

中，把 universal denominator certificate 的粗供给

\[
h\mid Q^2G
\]

与 denominator prime graph 联用，得到更强的奇素数结构。

这里

\[
b_2=1,
\qquad
G=b_1,
\qquad
Q=10b_1+1,
\]

所以

\[
\gcd(Q,b_1)=1.
\]

令

\[
b_3=h2^u5^v,
\qquad
\gcd(h,10)=1.
\]

本文证明：

1. 对 `p|Q` 的奇素数 `p!=5`，
   \[
   \boxed{v_p(b_3)\le v_p(Q)};
   \]
2. 若 `p^e||b_1`、`p!=2,5`，则
   \[
   \boxed{v_p(b_3)\in\{0,e\}};
   \]
   且 `v_p(b_3)=e` 只有在
   \[
   \boxed{p\equiv1\pmod4}
   \]
   时可能。

因此 `h` 的 `Q` 侧指数不再来自 `Q^2`，而 `b_1` 侧只允许整块选择 `1 mod 4` 素因子。

本文结论均为 **已严格完成**。

---

## 1. denominator prime graph 的两条输入

对奇素数

\[
p\ne2,5
\]

记

\[
e_i=v_p(b_i).
\]

全局 denominator prime graph 已证明：

### unique max

若某一块唯一取得最大赋值，则另外两块的 `p`-进指数必须相等；同时对应的 complementary denominator concatenation 被该最大 `p` 次幂整除。

### pair max

若最大赋值恰由两块取得，则必须

\[
\boxed{p\equiv1\pmod4.}
\]

本文只在 `b_2=1` 的 minimal diagonal 中专门化这两条结论。

---

## 2. `p|Q` 时第三分母指数至多来自一个 `Q`

设

\[
p\mid Q,
\qquad p\ne2,5.
\]

因为

\[
\gcd(Q,b_1)=1,
\qquad b_2=1,
\]

所以

\[
e_1=e_2=0.
\]

若

\[
e_3=v_p(b_3)>0,
\]

则第三块唯一取得最大赋值。

unique-max complementary concatenation 正是前两分母拼接

\[
b_1 10^{m_2}+b_2=10b_1+1=Q.
\]

因此

\[
p^{e_3}\mid Q.
\]

即

\[
\boxed{v_p(b_3)\le v_p(Q).}
\tag{1}
\]

所以 universal certificate 中 `Q^2` 给出的两倍指数在这里被 prime graph 收紧为单个 `Q` 的指数。

---

## 3. `p|b_1` 时只有 `0/e` 两种状态

现在设

\[
p^e\Vert b_1,
\qquad e>0,
\qquad p\ne2,5.
\]

因为

\[
\gcd(Q,b_1)=1,
\qquad b_2=1,
\]

有

\[
e_2=0.
\]

令

\[
f=v_p(b_3).
\]

### 情形 `0<f<e`

此时第一块唯一取得最大赋值 `e`。

unique-max 定理要求另外两块指数相等：

\[
e_2=f.
\]

但 `e_2=0` 而 `f>0`，矛盾。

### 情形 `f>e`

此时第三块唯一取得最大赋值 `f`。

unique-max 定理要求另外两块指数相等：

\[
e=e_2=0,
\]

再次矛盾。

因此只可能

\[
\boxed{f=0\quad\text{或}\quad f=e.}
\tag{2}
\]

若

\[
f=e,
\]

最大赋值恰由第一、第三块 pair-max 取得，所以 denominator prime graph 强迫

\[
\boxed{p\equiv1\pmod4.}
\tag{3}
\]

因此若

\[
p\equiv3\pmod4,
\]

则必有

\[
\boxed{v_p(b_3)=0.}
\tag{4}
\]

---

## 4. `h` 的精确供给形状

分解

\[
b_1
=2^{e_2}
\prod_{p\equiv1(4)}p^{e_p}
\prod_{q\equiv3(4)}q^{f_q},
\]

其中这里只列奇素数部分，`p,q!=5`。

定义

\[
\boxed{
B_+
:=
\prod_{p\equiv1(4),\ p^{e_p}\Vert b_1}
p^{e_p}.
}
\tag{5}
\]

注意 `B_+` 的每个 prime-power block 在 `b_3` 中只能整块出现或完全不出现。

另一方面 `Q` 侧允许任意普通因子

\[
q\mid Q
\]

（再自动去掉 `2,5`，而此处 `Q=10b_1+1` 本身已与 `10` 互素）。

所以存在

\[
q\mid Q
\]

以及 `B_+` 的一个 block-selector

\[
s=\prod_{p\in I}p^{e_p}
\]

使

\[
\boxed{h=qs.}
\tag{6}
\]

特别地有粗整除

\[
\boxed{h\mid QB_+,}
\tag{7}
\]

但 (6) 比普通“`h` 是 `QB_+` 的任意因子”更强，因为 `B_+` 一侧不允许降低某个已选 prime-power block 的指数。

---

## 5. `k=3` 的供给数量

当

\[
k=g=3,
\qquad r=s=1,
\]

四种 `w` 的 `b_1,Q` 分解为：

### `w=1`

\[
b_1=9999999=3^2\cdot239\cdot4649,
\]

其中只有

\[
4649\equiv1\pmod4.
\]

所以 `b_1` 侧只有 `2` 个 block-selector。

又

\[
Q=99999991=7\cdot13\cdot769\cdot1429,
\]

有 `16` 个普通因子。

故

\[
\boxed{\#h=32.}
\]

### `w=2`

\[
b_1=9999998=2\cdot4999999,
\]

且

\[
4999999\equiv3\pmod4,
\]

所以 `b_1` 侧没有可选奇块。

\[
Q=99999981=3^3\cdot3703703,
\]

有 `8` 个因子，因此

\[
\boxed{\#h=8.}
\]

### `w=3`

\[
b_1=9999997=7\cdot1428571,
\]

两个奇素因子均为 `3 mod 4`，所以 `b_1` 侧没有可选块。

\[
Q=99999971
\]

为素数，故

\[
\boxed{\#h=2.}
\]

### `w=4`

\[
b_1=9999996=2^2\cdot3\cdot191\cdot4363,
\]

三个奇素因子均为 `3 mod 4`，仍无 `b_1` 侧可选块。

\[
Q=99999961=179^2\cdot3121,
\]

有 `6` 个因子，所以

\[
\boxed{\#h=6.}
\]

因此 `k=3` 的 odd-prime supply 每个 prefix 只需考虑

\[
\boxed{32,8,2,6}
\]

种 `h`（按 `w=1,2,3,4`）。

---

## 6. 当前意义

minimal diagonal 的尾部供给已从 universal

\[
h\mid Q^2G
\]

收紧成 denominator-prime-graph 正规形 (6)。

对后续有限证书，这会显著减少状态数；对无界证明，它说明：

- `Q` 侧奇素数最多以原指数进入第三分母；
- `b_1` 侧只有 `1 mod 4` 素数能够流向第三分母，而且必须以完整 exponent block 流动；
- `3 mod 4` 的 `b_1` 素因子完全与第三分母隔离。

这是一条真正连接 moving prefix factorization 与第三 denominator prime supply 的接口。

# A1 minimal diagonal, valuation lock and finite certificates

> 本文件是按数学依赖整合的规范编辑入口。每个来源笔记只在本文件中保留一次；来源边界、原状态和公式正文均保留，避免日期文件之间形成平行副本。

## 整合顺序

`a1-top-layer-minimal-diagonal-2026-08-17.md` → `a1-top-layer-diagonal-valuation-normal-form-2026-08-17.md` → `a1-top-layer-diagonal-odd-prime-supply-2026-08-17.md` → `a1-top-layer-diagonal-significand-lock-2026-08-17.md` → `a1-top-layer-diagonal-sharp-significand-lock-2026-08-17.md` → `a1-top-layer-diagonal-k1-certificate-2026-08-17.md` → `a1-top-layer-diagonal-k2-certificate-2026-08-17.md` → `a1-discriminant-square-audit-2026-08-17.md`

---

## 1. A1 top-layer minimal-surplus diagonal kernel — 2026-08-17

> 整合来源：`a1-top-layer-minimal-diagonal-2026-08-17.md`。以下正文保留该来源的原始证明状态和审计边界。

本文研究最高层最小双 surplus

\[
r=s=1,
\qquad g\ge1
\]

中的 diagonal 区域

\[
\boxed{k=g.}
\]

在这一条线上，自然 carrier-gap 尺度恰好退化成常数 `10`。结合 half-gap shell，可把真实 rational gap 的整数部分完全锁死为 `5`，进而得到一个新的十进制余量参数 `j`。

核心结论（`k\ge2`）：

\[
\boxed{
U_1=(5-z)10^{k+1}+j,
\qquad
0\le j<\frac{17}{5}10^k,
}
\]

以及

\[
\boxed{
x=(5-z-w)10^{k+1}+j.}
\]

本文结论均为 **已严格完成**；`k=g=1` 保留为明确有限的小尺度例外。

---

### 1. diagonal 基本形状

`r=s=1` 已给出

\[
b_1=10^{2k+1}-w,
\]

\[
a_2=10^{2k+1}-z,
\]

\[
(z,w)
\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\}.
\]

当

\[
g=k
\]

时

\[
m_2=k-g+1=1,
\]

故

\[
\boxed{b_2=1.}
\tag{1}
\]

共同十进制中心为

\[
\boxed{M=10^{2k+1}.}
\]

自然 gap 尺度变成

\[
\boxed{
H_0=10^{g+1-k}=10.
}
\tag{2}
\]

---

### 2. half-gap shell 直接锁死 gap 的整数部分

令

\[
D_0=10^kr_1-r_2.
\]

half-gap sharpening 给出

\[
\frac12
<\frac{D_0}{10}
<\frac{267}{500}.
\]

所以

\[
\boxed{
5<D_0<\frac{267}{50}=5.34.
}
\tag{3}
\]

由于 `b_2=1`，residue kernel 给出

\[
D_0
=10^k\frac{U_1}{b_1}+U_2.
\]

而 `s=1,y=0` 时

\[
U_2=z.
\]

故

\[
\boxed{
D_0
=10^k\frac{U_1}{b_1}+z.
}
\tag{4}
\]

又 determinant

\[
\Delta=10^kb_2U_1+b_1U_2
\]

在这里化为

\[
\boxed{
\Delta=10^kU_1+b_1z.
}
\tag{5}
\]

并且

\[
D_0=\frac\Delta{b_1}.
\]

由 (3)：

\[
5b_1<\Delta<\frac{267}{50}b_1.
\]

因此存在唯一正整数 `J` 使

\[
\boxed{
\Delta=5b_1+J,
\qquad
0<J<\frac{17}{50}b_1.
}
\tag{6}
\]

---

### 3. `J` 的十进制同余

把 (5) 代入 (6)：

\[
10^kU_1+b_1z
=5b_1+J.
\]

于是

\[
\boxed{
J=10^kU_1-(5-z)b_1.
}
\tag{7}
\]

令

\[
c=5-z.
\]

因为

\[
z\in\{1,3\},
\]

所以

\[
\boxed{c\in\{4,2\}.}
\tag{8}
\]

再代入

\[
b_1=10^{2k+1}-w:
\]

\[
J
=10^kU_1-c10^{2k+1}+cw.
\]

因此

\[
\boxed{
J=cw+10^k
\left(U_1-c10^{k+1}\right).
}
\tag{9}
\]

---

### 4. `k\ge2` 时得到新的非负整数 `j`

定义

\[
\boxed{
j=U_1-c10^{k+1}.}
\tag{10}
\]

则 (9) 为

\[
\boxed{J=cw+10^kj.}
\tag{11}
\]

六类型中

\[
cw\le4\cdot4=16.
\]

若

\[
k\ge2,
\]

则

\[
cw<10^k.
\]

因为 `J>0` 且 `J\equiv cw\pmod{10^k}`，其最小正代表就是 `cw`，所以

\[
\boxed{j\ge0.}
\tag{12}
\]

由 (6)：

\[
10^kj
<J
<\frac{17}{50}b_1
<\frac{17}{50}10^{2k+1}.
\]

故

\[
\boxed{
0\le j<\frac{17}{5}10^k.
}
\tag{13}
\]

所以

\[
\boxed{
U_1=c10^{k+1}+j
=(5-z)10^{k+1}+j.
}
\tag{14}
\]

---

### 5. 第一分子 offset `x` 也得到块分解

在 diagonal 中 `g=k`，且 `r=1`，所以

\[
U_1=x+10^{k+1}w.
\]

结合 (14)：

\[
x+10^{k+1}w
=(5-z)10^{k+1}+j.
\]

因此

\[
\boxed{
 x=(5-z-w)10^{k+1}+j.
}
\tag{15}
\]

六类型中 `5-z-w` 总是非负：

| `z` | `w` | `5-z-w` |
|---:|---:|---:|
| 1 | 1 | 3 |
| 1 | 2 | 2 |
| 1 | 3 | 1 |
| 1 | 4 | 0 |
| 3 | 1 | 1 |
| 3 | 2 | 0 |

所以 diagonal 第一分子 offset 只允许六个固定主块，外加

\[
0\le j<0.34\cdot10^{k+1}.
\]

---

### 6. 原四整数在 diagonal 中的最终形状

对 `k=g\ge2`、`r=s=1`，六类型统一写成

\[
\boxed{
b_1=10^{2k+1}-w,}
\]

\[
\boxed{b_2=1,}
\]

\[
\boxed{a_2=10^{2k+1}-z,}
\]

\[
\boxed{
 a_1
=10^{3k+2}
+(5-z-w)10^{k+1}
+j,
}
\]

其中

\[
(z,w)
\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\},
\]

\[
\boxed{0\le j<\frac{17}{5}10^k.}
\]

因此 diagonal 边界已经从两个长整数自由度降为：

- 一个整数 `k\ge2`；
- 6 个绝对类型；
- 一个只有 `k+1` 位尺度、且前 `~70%` 区间被删除的余量 `j`。

---

### 7. `k=g=1` 小尺度例外

当

\[
k=g=1,
\]

有

\[
10^k=10,
\]

而某些类型的 `cw` 可达到 `12` 或 `16`，因此从 `J>0` 不能自动推出本文定义的 `j\ge0`。

这是一个**明确有限的单个 `(k,g)` 切片**，应单独做精确有限检查；它不影响 `k=g\ge2` 的无界 diagonal reduction。

---

### 8. 后续接口

在 diagonal 中第三分母正规化还有额外简化。令

\[
\sigma=\frac{b_3}{10^{m_3}}
\in[0.1,1).
\]

因为 `g=k`，有

\[
\boxed{
\frac\theta\lambda
=\frac\rho{10^k}
=\sigma.
}
\]

所以 positive excess decomposition 中 prefix-contact 与 third-contact 两个 source 只差一个第三分母 significand `sigma`。

下一步应把 `(k;z,w;j;\sigma)` 代回 excess decomposition 与 safe integer-gap identity，优先关闭 `k\ge2` diagonal；`k=1` 则作为有限切片独立核验。

---

## 2. A1 top-layer minimal diagonal valuation normal form — 2026-08-17

> 整合来源：`a1-top-layer-diagonal-valuation-normal-form-2026-08-17.md`。以下正文保留该来源的原始证明状态和审计边界。

本文继续最小双 surplus diagonal，并结合 `k=g=1,2` 两个有限证书，把剩余无界部分统一置于

\[
\boxed{k=g\ge3.}
\]

在这一范围，六个 `(z,w)` 类型的 `2/5`-进前缀结构完全稳定，两个 primitive cross-corridor 上界都精确退化成同一个整数 `k`。

核心结论：

\[
\boxed{v_5(K)=0,}
\]

\[
\boxed{v_2(K)=2v_2(w),}
\]

以及

\[
\boxed{X_0=Y_0=k.}
\]

本文结论均为 **已严格完成**。

---

### 1. minimal diagonal 数据

当前范围为

\[
d=2,
\qquad r=s=1,
\qquad k=g\ge3.
\]

因此

\[
\boxed{b_2=1,}
\]

\[
\boxed{b_1=10^{2k+1}-w,}
\]

\[
\boxed{a_2=10^{2k+1}-z,}
\]

其中

\[
(z,w)
\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\}.
\]

又

\[
Q=10b_1+1,
\qquad
G=b_1,
\qquad
D=10^kQ.
\]

第二分子位数为

\[
n_2=2k+1,
\]

所以

\[
C=a_1 10^{2k+1}+a_2.
\]

---

### 2. `Q,C,G` 的 `2/5` 赋值

因为

\[
Q=10b_1+1,
\]

立即有

\[
\boxed{v_2(Q)=v_5(Q)=0.}
\tag{1}
\]

又 `a_2` 的末位为 `9` 或 `7`，而第一项 `a_1 10^{2k+1}` 同时被 `2,5` 整除，因此

\[
C\equiv a_2\pmod{10}.
\]

所以

\[
\boxed{v_2(C)=v_5(C)=0.}
\tag{2}
\]

对

\[
G=b_1=10^{2k+1}-w,
\]

六类型中 `1\le w\le4`。由于

\[
v_2(10^{2k+1})=2k+1>v_2(w),
\]

有

\[
\boxed{v_2(G)=v_2(w)\in\{0,1,2\}.}
\tag{3}
\]

同时 `w` 不被 `5` 整除，故

\[
\boxed{v_5(G)=0.}
\tag{4}
\]

由 (1)：

\[
\boxed{v_2(D)=v_5(D)=k.}
\tag{5}
\]

---

### 3. `N` 的二进结构

这里

\[
N=a_1^2+(a_2b_1)^2.
\]

若 `w` 为偶数，则 `b_1` 为偶数。原问题有

\[
\gcd(a_1,b_1)=1,
\]

所以 `a_1` 必为奇数，而第二项为偶平方。因此

\[
\boxed{w\text{ 偶}\Longrightarrow v_2(N)=0.}
\tag{6}
\]

若 `w` 为奇数，则 `b_1,a_2` 均为奇数。

- `a_1` 偶时，`N` 为奇数；
- `a_1` 奇时，两项均为 `1 mod 4`，所以
  \[
  N\equiv2\pmod4.
  \]

因此全局有

\[
\boxed{v_2(N)\in\{0,1\}.}
\tag{7}
\]

---

### 4. `K` 的五进赋值恒为零

定义

\[
K=G^2C^2-D^2N.
\]

由 (2)、(4)：

\[
v_5(G^2C^2)=0.
\]

而由 (5)：

\[
v_5(D^2N)\ge2k\ge6.
\]

两项赋值不同，所以

\[
\boxed{v_5(K)=0.}
\tag{8}
\]

---

### 5. `K` 的二进赋值等于 `2v_2(w)`

令

\[
e=v_2(w)=v_2(G)\in\{0,1,2\}.
\]

由 (2)：

\[
v_2(G^2C^2)=2e\le4.
\]

另一方面由 (5)、(7)：

\[
v_2(D^2N)=2k+v_2(N)\ge6.
\]

因此仍是严格不同赋值，低侧由第一项唯一承担：

\[
\boxed{v_2(K)=2e=2v_2(w).}
\tag{9}
\]

所以六类型只有

\[
v_2(K)=
\begin{cases}
0,&w=1,3,\\
2,&w=2,\\
4,&w=4.
\end{cases}
\]

这里 `k\ge3` 很重要；`k=2,w=4` 时两个主项可能在同一二进深度相遇，因此已经被单独的有限证书处理。

---

### 6. resonance lines

normalized tail 写成

\[
\rho=h2^x5^y.
\]

二进 resonance line 为

\[
x_*
=v_2(K)-\left(1+v_2(D)+v_2(N)\right).
\]

所以

\[
\boxed{
 x_*=2v_2(w)-1-k-v_2(N).
}
\tag{10}
\]

五进 resonance line 为

\[
y_*
=v_5(K)-v_5(D)-v_5(N),
\]

故

\[
\boxed{
 y_*=-k-v_5(N).
}
\tag{11}
\]

---

### 7. 两个 primitive cross-corridor cap 都等于 `k`

旧 primitive cross-corridor 公式为

\[
X_0=
\max\left(
0,
 d_2,
 d_2+\frac{k_2}{2}-g_2-c_2,
 d_2+g_2-\frac{k_2}{2}
\right),
\]

其中

\[
d_2=k,
\quad
k_2=2e,
\quad
g_2=e,
\quad c_2=0.
\]

所以后两项都恰为 `k`：

\[
d_2+\frac{k_2}{2}-g_2-c_2=k+e-e=k,
\]

\[
d_2+g_2-\frac{k_2}{2}=k+e-e=k.
\]

因此

\[
\boxed{X_0=k.}
\tag{12}
\]

五进同理：

\[
d_5=k,
\quad k_5=0,
\quad g_5=c_5=0,
\]

故

\[
\boxed{Y_0=k.}
\tag{13}
\]

---

### 8. 当前意义

minimal diagonal 的六个 prefix 类型虽然在十进制外形上不同，但 `2/5`-进 tail geometry 在 `k\ge3` 已经统一成：

\[
\boxed{
X_0=Y_0=k,
}
\]

配合 resonance lines

\[
x_*=2v_2(w)-1-k-v_2(N),
\]

\[
y_*=-k-v_5(N).
\]

所以：

- `2+5-` cross corridor 中一旦 `x>k` 就不可能；
- `2-5+` cross corridor 中一旦 `y>k` 就不可能；
- 五进前缀没有任何隐藏的 `5`-adic supply，因为 `v_5(K)=0`；
- 二进前缀只由绝对小常数 `w` 的赋值决定。

这为把 diagonal significand lock 与 tail resonance/cross-corridor 系统直接耦合提供了统一入口。

---

## 3. A1 top-layer minimal diagonal odd-prime supply — 2026-08-17

> 整合来源：`a1-top-layer-diagonal-odd-prime-supply-2026-08-17.md`。以下正文保留该来源的原始证明状态和审计边界。

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

### 1. denominator prime graph 的两条输入

对奇素数

\[
p\ne2,5
\]

记

\[
e_i=v_p(b_i).
\]

全局 denominator prime graph 已证明：

#### unique max

若某一块唯一取得最大赋值，则另外两块的 `p`-进指数必须相等；同时对应的 complementary denominator concatenation 被该最大 `p` 次幂整除。

#### pair max

若最大赋值恰由两块取得，则必须

\[
\boxed{p\equiv1\pmod4.}
\]

本文只在 `b_2=1` 的 minimal diagonal 中专门化这两条结论。

---

### 2. `p|Q` 时第三分母指数至多来自一个 `Q`

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

### 3. `p|b_1` 时只有 `0/e` 两种状态

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

#### 情形 `0<f<e`

此时第一块唯一取得最大赋值 `e`。

unique-max 定理要求另外两块指数相等：

\[
e_2=f.
\]

但 `e_2=0` 而 `f>0`，矛盾。

#### 情形 `f>e`

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

### 4. `h` 的精确供给形状

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

### 5. `k=3` 的供给数量

当

\[
k=g=3,
\qquad r=s=1,
\]

四种 `w` 的 `b_1,Q` 分解为：

#### `w=1`

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

#### `w=2`

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

#### `w=3`

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

#### `w=4`

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

### 6. 当前意义

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

---

## 4. A1 top-layer diagonal significand lock — 2026-08-17

> 整合来源：`a1-top-layer-diagonal-significand-lock-2026-08-17.md`。以下正文保留该来源的原始证明状态和审计边界。

本文继续 `diagonal.md`，仍处于

\[
d=2,
\qquad
r=s=1,
\qquad
k=g\ge2.
\]

上一文件得到

\[
U_1=(5-z)10^{k+1}+j,
\qquad
0\le j<\frac{17}{5}10^k.
\]

本文把 positive excess decomposition 与 diagonal identity

\[
\frac\theta\lambda
=\frac{b_3}{10^{m_3}}
\]

结合，证明 prefix remainder `j` 与第三分母的十进制 significand 被直接锁在一起。

定义

\[
\boxed{
 u=\frac{j}{10^{k+1}},
}
\]

\[
\boxed{
 \sigma=\frac{b_3}{10^{m_3}}\in[0.1,1).
}
\]

核心结论：

\[
\boxed{
0.098+0.099\sigma
<u
<0.101+0.101\sigma.
}
\]

因此

\[
\boxed{
\left|
\frac{j}{10^k}-(1+\sigma)
\right|<0.03.
}
\]

本文结论均为 **已严格完成**。

---

### 1. diagonal 中 `phi_1` 的精确 `u` 表达

令

\[
c=5-z\in\{4,2\}.
\]

由上一文件

\[
U_1=c10^{k+1}+j
=10^{k+1}(c+u).
\]

又

\[
b_1=10^{2k+1}-w.
\]

在 diagonal 中自然 gap 尺度是 `10`，所以

\[
\phi_1
=\frac{10^kU_1/b_1}{10}
=\frac{10^{k-1}U_1}{b_1}.
\]

代入后除以 `10^{2k}`：

\[
\boxed{
\phi_1
=\frac{c+u}{10-w\varepsilon},
}
\tag{1}
\]

其中

\[
\varepsilon=10^{-2k}.
\]

而

\[
\phi_2=\frac z{10}.
\]

因此总 normalized gap

\[
\Phi:=\phi_1+\phi_2
\]

满足

\[
2\Phi-1
=2\frac{c+u}{10-w\varepsilon}+
rac z5-1.
\]

因为 `c=5-z`，整理为

\[
\boxed{
2\Phi-1
=\frac{10u+cw\varepsilon}
{5(10-w\varepsilon)}.
}
\tag{2}
\]

等价地

\[
\boxed{
 u
=5(2\Phi-1)
-\frac{w\varepsilon}{2}(2\Phi-1)
-\frac{cw\varepsilon}{10}.
}
\tag{3}

---

### 2. `lambda/epsilon` 在 diagonal 中几乎精确为 `1/100`

最小边界中

\[
\lambda=\frac1{10b_1+1}.
\]

所以

\[
\frac\lambda\varepsilon
=\frac1{100-(10w-1)\varepsilon}.
\]

六类型有 `w\le4`，并且 `k\ge2` 给出

\[
\varepsilon\le10^{-4}.
\]

因此

\[
\boxed{
\frac1{100}
<\frac\lambda\varepsilon
<0.010001.
}
\tag{4}
\]

---

### 3. 第三 contact 比例就是第三分母 significand

写

\[
\rho=\frac{b_3}{10^\ell}.
\]

由于 diagonal 中

\[
g=k,
\qquad
m_3=k+\ell,
\]

有

\[
\frac\rho{10^k}
=\frac{b_3}{10^{k+\ell}}
=\frac{b_3}{10^{m_3}}
=\sigma.
\]

而最小边界满足

\[
\frac\theta\lambda=\frac\rho{10^k}.
\]

所以

\[
\boxed{
\theta=\sigma\lambda.
}
\tag{5}
\]

这是 diagonal 中 prefix-contact 与 third-contact 的精确比例。

---

### 4. positive excess 的下界

沿用正项分解

\[
\begin{aligned}
E:=2\Phi-1
={}&
\frac{\mathfrak h}{M\varepsilon}
\left(1+\varepsilon\phi_1+\frac RM\right)\\
&+\frac{(r_3/M)^2}{\varepsilon}
+\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
+\varepsilon^2\phi_1^2.
\end{aligned}
\tag{6}
\]

其中

\[
\frac{\mathfrak h}{M}
=\lambda A+\theta B,
\]

\[
A=(1+\varepsilon\phi_1)
-10^{-k}(1-\varepsilon\phi_2),
\]

\[
B=\frac RM-\frac{r_3}{M}.
\]

因为 `k\ge2`：

\[
10^{-k}\le0.01,
\]

故

\[
\boxed{A>0.99.}
\tag{7}
\]

又

\[
\frac RM>\frac{r_2}{M}=1-\varepsilon\phi_2
\ge1-0.3\cdot10^{-4}>0.99997.
\]

最高层还有

\[
\frac{r_3}{M}<10^{-3k}\le10^{-6},
\]

所以

\[
\boxed{B>0.9999.}
\tag{8}
\]

结合 (4)、(5)、(7)、(8)：

\[
\frac{\mathfrak h}{M\varepsilon}
>
0.01(0.99+0.9999\sigma).
\tag{9}
\]

此外

\[
1+\varepsilon\phi_1+R/M
>1+0.99997>1.9999.
\]

因此只保留 (6) 第一正项即可得到

\[
\boxed{
E
>0.01979+0.01997\sigma.
}
\tag{10}
\]

---

### 5. positive excess 的上界

half-gap kernel 给出

\[
\phi_1<0.434,
\qquad
\phi_2\le0.3.
\]

故

\[
1+\varepsilon\phi_1<1.000044.
\]

于是

\[
A<1.000044,
\qquad
B<1.000044.
\]

由 (4)、(5)：

\[
\frac{\mathfrak h}{M\varepsilon}
<0.010001\cdot1.000044(1+\sigma).
\]

又

\[
1+\varepsilon\phi_1+R/M<2.000088.
\]

所以第一 source 小于

\[
0.020013(1+\sigma).
\tag{11}
\]

第三半径满足

\[
\frac{(r_3/M)^2}{\varepsilon}
<10^{-4k}
\le10^{-8}.
\tag{12}
\]

曲率项满足

\[
\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
<10^{-4}(0.868+0.09)
<0.000096,
\tag{13}
\]

以及

\[
\varepsilon^2\phi_1^2<2\cdot10^{-9}.
\tag{14}
\]

故

\[
\boxed{
E
<0.020013(1+\sigma)+0.000097.
}
\tag{15}
\]

---

### 6. 转回 `u`

由精确式 (3)：

\[
u
=5E
-\frac{w\varepsilon}{2}E
-\frac{cw\varepsilon}{10}.
\]

#### 下界

由 (10)：

\[
5E>0.09895+0.09985\sigma.
\]

又六类型中

\[
w,c\le4,
\qquad
\varepsilon\le10^{-4},
\qquad
E<0.041,
\]

所以两个减项之和小于 `0.00017`。于是

\[
\boxed{
 u>0.098+0.099\sigma.
}
\tag{16}
\]

#### 上界

从 (3) 直接丢掉两个负项并用 (15)：

\[
u<5E
<0.100065(1+\sigma)+0.000485.
\]

因此

\[
\boxed{
 u<0.101+0.101\sigma.
}
\tag{17}
\]

合并 (16)–(17)：

\[
\boxed{
0.098+0.099\sigma
<u
<0.101+0.101\sigma.
}
\tag{18}
\]

---

### 7. 十进制 significand lock

因为

\[
u=\frac{j}{10^{k+1}},
\]

把 (18) 与

\[
0.1(1+\sigma)
\]

比较：

下侧误差最多

\[
0.1(1+\sigma)-(0.098+0.099\sigma)
=0.002+0.001\sigma<0.003,
\]

上侧误差最多

\[
(0.101+0.101\sigma)-0.1(1+\sigma)
=0.001+0.001\sigma<0.002.
\]

所以

\[
\boxed{
\left|
 u-\frac{1+\sigma}{10}
\right|<0.003.
}
\tag{19}
\]

乘以 `10`：

\[
\boxed{
\left|
\frac{j}{10^k}-(1+\sigma)
\right|<0.03.
}
\tag{20}
\]

最后代回

\[
\sigma=\frac{b_3}{10^{m_3}}:
\]

\[
\boxed{
\left|
\frac{j}{10^k}
-
1
-
\frac{b_3}{10^{m_3}}
\right|<0.03.
}
\tag{21}
\]

这是一条直接连接 moving prefix 与第三分母 leading decimal 的约束。

---

### 8. `j` 的位数被锁定

由 `sigma>=0.1` 和 (18)：

\[
u>0.098+0.0099=0.1079.
\]

由 `sigma<1`：

\[
u<0.101+0.101=0.202.
\]

所以

\[
1.079
<\frac{j}{10^k}
<2.02.
\]

因此

\[
\boxed{j\text{ 恰有 }k+1\text{ 位}.}
\tag{22}
\]

若

\[
\frac j{10^k}\ge2,
\]

则由 (20)

\[
1+\sigma>1.97,
\]

所以

\[
\boxed{
 j\text{ 以 }2\text{ 开头}
\Longrightarrow
\sigma>0.97.
}
\tag{23}
\]

除第三分母 significand 已经落在最顶部 `3%` 的情形外，`j` 必须以十进制数字 `1` 开头。

---

### 9. 当前意义

minimal diagonal kernel 现在具有直接的 prefix-tail 数字锁：

\[
\frac j{10^k}-1
\approx
\frac{b_3}{10^{m_3}}
\]

误差严格小于 `0.03`。

这说明第三分母的 leading decimal 已不再只通过抽象 `theta` 进入证明；它与 prefix remainder `j` 的 leading decimal 发生直接耦合。

下一步应把该 significand lock 与：

- `b_3\mid10^{2m_3}Q^2G`；
- `2/5` resonance/cross-corridor 赋值；
- `j` 在六 `(z,w)` 类型中的同余；

联用，尝试把 `0.03` 窗继续压到单个 leading-prefix 或产生模矛盾。

---

## 5. A1 top-layer diagonal sharp significand lock for `k>=3` — 2026-08-17

> 整合来源：`a1-top-layer-diagonal-sharp-significand-lock-2026-08-17.md`。以下正文保留该来源的原始证明状态和审计边界。

本文结合 `k=g=1,2` 两个有限证书，从此只研究 minimal diagonal 的无界部分

\[
\boxed{k=g\ge3.}
\]

上一版 significand lock 为

\[
\left|
\frac j{10^k}
-
1
-
\frac{b_3}{10^{m_3}}
\right|<0.03.
\]

利用 `k>=3` 后

\[
10^{-k}\le10^{-3},
\qquad
\varepsilon=10^{-2k}\le10^{-6},
\]

positive excess decomposition 中的误差可以再压两个数量级。

令

\[
\boxed{
\sigma=\frac{b_3}{10^{m_3}}\in[0.1,1),
}
\]

\[
\boxed{
 u=\frac{j}{10^{k+1}}.
}
\]

本文证明

\[
\boxed{
0.09989+0.09999\sigma
<u
<0.100005+0.100001\sigma.
}
\tag{1}
\]

因此

\[
\boxed{
\left|
\frac j{10^k}-(1+\sigma)
\right|<0.0012.
}
\tag{2}
\]

本文结论均为 **已严格完成**。

---

### 1. 输入

仍沿用 minimal diagonal 的

\[
\phi_1,
\qquad
\phi_2=\frac z{10}\le0.3,
\qquad
\varepsilon=10^{-2k},
\]

以及正项 excess

\[
E:=2(\phi_1+\phi_2)-1.
\]

`top-layer.md` 给出

\[
\begin{aligned}
E
={}&
\frac{\mathfrak h}{M\varepsilon}
\left(1+\varepsilon\phi_1+\frac RM\right)\\
&+\frac{(r_3/M)^2}{\varepsilon}
+\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
+\varepsilon^2\phi_1^2.
\end{aligned}
\tag{3}
\]

其中

\[
\frac{\mathfrak h}{M}
=\lambda A+\theta B,
\]

\[
A=(1+\varepsilon\phi_1)-10^{-k}(1-\varepsilon\phi_2),
\]

\[
B=\frac RM-\frac{r_3}{M}.
\]

在 diagonal 中

\[
\boxed{\theta=\sigma\lambda.}
\tag{4}
\]

而六类型始终有

\[
0<\phi_1<0.434.
\]

---

### 2. `lambda/epsilon` 的六位精度

minimal diagonal 有

\[
\frac\lambda\varepsilon
=
\frac1{100-(10w-1)\varepsilon},
\qquad w\le4.
\]

当 `k>=3` 时

\[
\varepsilon\le10^{-6},
\]

故

\[
100-(10w-1)\varepsilon
\ge100-39\cdot10^{-6}.
\]

于是

\[
\boxed{
0.01
<\frac\lambda\varepsilon
<0.010000004.
}
\tag{5}
\]

---

### 3. `A,B` 的统一上下界

因为

\[
10^{-k}\le0.001,
\]

有

\[
\boxed{A>1-10^{-k}\ge0.999.}
\tag{6}
\]

又

\[
A<1+\varepsilon\phi_1<1.000000434.
\tag{7}
\]

对 `B`，由

\[
R>r_2=M(1-\varepsilon\phi_2)
\]

和最高层

\[
\frac{r_3}{M}<10^{-3k}\le10^{-9}
\]

得到

\[
B
>1-0.3\varepsilon-10^{-3k}
>0.9999996.
\tag{8}
\]

另一方面

\[
B<\frac RM<\frac{10^kr_1}{M}
=1+\varepsilon\phi_1
<1.000000434.
\tag{9}
\]

---

### 4. 第一 positive source 的精确夹逼

由 (4)–(9)：

\[
\frac{\mathfrak h}{M\varepsilon}
=
\frac\lambda\varepsilon(A+\sigma B).
\]

下侧：

\[
\boxed{
\frac{\mathfrak h}{M\varepsilon}
>0.01(0.999+0.9999996\sigma).
}
\tag{10}
\]

上侧：

\[
\boxed{
\frac{\mathfrak h}{M\varepsilon}
<0.010000004\cdot1.000000434(1+\sigma).
}
\tag{11}
\]

同时

\[
1+\varepsilon\phi_1+R/M
>2-\varepsilon\phi_2
>1.9999997,
\tag{12}
\]

以及

\[
1+\varepsilon\phi_1+R/M
<2(1+\varepsilon\phi_1)
<2.000000868.
\tag{13}
\]

因此 (3) 第一 source 满足一个几乎精确的

\[
0.02(1+\sigma)
\]

比例。

---

### 5. 其余 source 总量小于 `10^{-6}` 量级

第三半径：

\[
\frac{(r_3/M)^2}{\varepsilon}
<10^{-4k}
\le10^{-12}.
\tag{14}
\]

曲率：

\[
2\phi_1+\phi_2^2-\phi_1^2
<2(0.434)+0.3^2
=0.958.
\]

所以

\[
\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
<0.958\cdot10^{-6},
\tag{15}
\]

并且

\[
\varepsilon^2\phi_1^2<2\cdot10^{-13}.
\tag{16}
\]

---

### 6. 从 excess 转回 `u`

minimal diagonal 的精确关系为

\[
\boxed{
 u
=5E
-\frac{w\varepsilon}{2}E
-\frac{(5-z)w\varepsilon}{10}.
}
\tag{17}
\]

由 half-gap 上界 `E<0.068`、`w<=4`、`5-z<=4`，当 `epsilon<=10^-6` 时两个减项总和小于

\[
1.74\cdot10^{-6}.
\tag{18}
\]

把 (10)–(16) 代入 (3)，再代入 (17)，采用安全十进制粗化即可得到

\[
\boxed{
 u>0.09989+0.09999\sigma,
}
\tag{19}
\]

以及

\[
\boxed{
 u<0.100005+0.100001\sigma.
}
\tag{20}
\]

这就是 (1)。

---

### 7. sharpened significand lock

目标中心为

\[
\frac{1+\sigma}{10}
=0.1+0.1\sigma.
\]

由 (19)：

\[
\frac{1+\sigma}{10}-u
<0.00011+0.00001\sigma
<0.00012.
\]

由 (20)：

\[
u-\frac{1+\sigma}{10}
<0.000005+0.000001\sigma
<0.000006.
\]

因此统一有

\[
\boxed{
\left|
 u-\frac{1+\sigma}{10}
\right|<0.00012.
}
\tag{21}
\]

乘以 `10`：

\[
\boxed{
\left|
\frac j{10^k}-(1+\sigma)
\right|<0.0012.
}
\tag{22}
\]

即

\[
\boxed{
\left|
\frac j{10^k}
-1
-\frac{b_3}{10^{m_3}}
\right|<0.0012.
}
\tag{23}
\]

---

### 8. 全局 `j` 窗进一步缩窄

由

\[
0.1\le\sigma<1
\]

和 (19)–(20)：

\[
u>0.09989+0.009999=0.109889,
\]

\[
u<0.100005+0.100001=0.200006.
\]

因此

\[
\boxed{
1.09889
<\frac j{10^k}
<2.00006.
}
\tag{24}
\]

与早先的

\[
1.079<j/10^k<2.02
\]

相比，两侧都明显收紧。

特别地 `j` 若达到或超过

\[
2\cdot10^k,
\]

则 (22) 强迫

\[
\sigma>0.9988.
\]

所以 `j` 以十进制数字 `2` 开头的尾部已被压到第三分母 significand 的最顶部 `0.12%`。

---

### 9. 当前意义

在 minimal diagonal 的全部无界范围 `k=g>=3` 中，moving prefix remainder `j` 与第三分母 significand `sigma` 已经在 `1.2×10^-3` 的绝对误差内同步。

配合 valuation normal form

\[
X_0=Y_0=k,
\]

下一步可以把 `(j,sigma)` 的数字锁直接叠加到 `rho=h2^x5^y` 的 resonance / cross-corridor 几何中，尝试获得对 `k` 本身的统一矛盾。

---

## 6. A1 top-layer diagonal `k=g=1` finite certificate — 2026-08-17

> 整合来源：`a1-top-layer-diagonal-k1-certificate-2026-08-17.md`。以下正文保留该来源的原始证明状态和审计边界。

本文关闭最高层最小双 surplus diagonal 的小尺度切片

\[
\boxed{d=2,\qquad r=s=1,\qquad k=g=1.}
\]

结论：

\[
\boxed{\text{该切片为空。}}
\]

验证脚本：

```bash
uv run python scripts/exact-lift/a1-only/check_a1_top_diag_k1.py --jobs 4
```

状态：**有限证书**。

---

### 1. 完备 prefix box

minimal-surplus theorem 已把 `(z,w)` 限成六类型

\[
(z,w)\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\}.
\]

这里

\[
b_1=10^3-w,
\qquad b_2=1,
\qquad a_2=10^3-z,
\]

并写

\[
U_1=x+100w,
\qquad a_1=10^5+x.
\]

因为 diagonal 自然 gap 尺度仍为 `10`，half-gap sharpening 直接给出

\[
\boxed{
z=1:\quad \frac25<\frac{U_1}{b_1}<\frac{217}{500},}
\]

\[
\boxed{
z=3:\quad \frac15<\frac{U_1}{b_1}<\frac{117}{500}.}
\]

所以每个六类型的 `U_1` 都落在一个显式有限整数区间。再施加

\[
x\ge0,
\qquad \gcd(a_1,b_1)=1,
\qquad K>0,
\]

恰好剩下

\[
\boxed{79}
\]

个 admissible prefixes。

这里没有使用 `k\ge2` 时的 `j\ge0` 推导，因此完整覆盖之前特意保留的 `k=g=1` 小尺度例外。

---

### 2. 第三尾有限盒

后续 tail 证书与
[`diagonal.md`](diagonal.md)
完全使用同一条严格链：

1. universal denominator certificate 给出第三分母 `2/5`-free 部分
   \[
   h\mid Q^2G;
   \]
2. 写
   \[
   \rho=h2^x5^y;
   \]
3. 此处 `g=1`，所以 decade strip 为
   \[
   1\le\rho<10;
   \]
4. `2/5` resonance lines 与 primitive cross-corridor 上界给出完备有限 `(x,y)` 盒；
5. 对每个 partial state `(P,S,theta)` 精确检查
   \[
   \Xi=P^2-(1+2\theta)S
   \]
   是否为非负有理平方；
6. 若平方通过，再恢复两个 `r_3` 根、检查位数/正规化并直接复核原始拼接平方恒等式。

所有运算使用整数和 `Fraction`，没有浮点判等。

---

### 3. 精确结果

| `(z,w)` | prefixes | exact `(h,x,y)` states | rational-square states |
|---|---:|---:|---:|
| `(1,1)` | 14 | 31302 | 0 |
| `(1,2)` | 11 | 10473 | 0 |
| `(1,3)` | 21 | 19585 | 0 |
| `(1,4)` | 6 | 6692 | 0 |
| `(3,1)` | 15 | 33533 | 0 |
| `(3,2)` | 12 | 11430 | 0 |
| **总计** | **79** | **113015** | **0** |

因此

\[
\boxed{
 d=2,\ r=s=1,\ k=g=1
\text{ 为空。}
}

预期脚本摘要：

```text
prefixes=79
tail_states=113015
rational_square_contacts=0
positive_r3_roots=0
exact_hits=0
CERTIFICATE OK: k=g=1, r=s=1 diagonal slice is empty.
```

---

### 4. 对无界 diagonal 的意义

结合 `k=g=2` 证书，最小双 surplus diagonal 现在已经严格排除

\[
\boxed{k=g\in\{1,2\}.}
\]

所以尚未关闭的无界 diagonal 可以无条件进入

\[
\boxed{k=g\ge3.}
\]

在这一范围

\[
\varepsilon=10^{-2k}\le10^{-6},
\]

因此 positive excess decomposition 中曲率项与 third-radius 项比此前的通用 `k\ge2` 估计再小至少两个数量级。后续应直接利用这一点强化 diagonal significand lock。

---

## 7. A1 top-layer diagonal `k=g=2` finite certificate — 2026-08-17

> 整合来源：`a1-top-layer-diagonal-k2-certificate-2026-08-17.md`。以下正文保留该来源的原始证明状态和审计边界。

本文关闭最高层最小双 surplus diagonal 中的完整切片

\[
\boxed{
d=2,
\qquad r=s=1,
\qquad k=g=2.
}
\]

结论：

\[
\boxed{
\text{该切片不存在 exact-lift 候选。}
}
\]

证明由前序无界理论给出的**完备有限盒**与精确有理数证书组成。验证脚本：

```bash
uv run python scripts/exact-lift/a1-only/check_a1_top_diag_k2.py --jobs 4
```

脚本只使用整数、`fractions.Fraction`、整数平方根与 `sympy.factorint`；没有浮点判等或数值容差。

状态：**有限证书**。它关闭的是明确有界的 `k=g=2,r=s=1,d=2` 切片，不代表整个 A1 或整个 diagonal 已关闭。

---

### 1. 前缀集合为什么是完备的

沿用 minimal diagonal kernel。这里

\[
k=g=2,
\qquad r=s=1.
\]

因此

\[
\boxed{b_2=1,}
\]

\[
\boxed{b_1=10^5-w,}
\]

\[
\boxed{a_2=10^5-z,}
\]

而绝对六类型为

\[
\boxed{
(z,w)
\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\}.
}
\tag{1}
\]

又由 diagonal integerization，令

\[
c=5-z,
\]

则

\[
\boxed{
a_1=10^8+(c-w)10^3+j.}
\tag{2}
\]

`diagonal.md` 已严格证明

\[
1.079<\frac j{10^2}<2.02.
\]

因为 `j` 为整数，所以精确等价于

\[
\boxed{108\le j\le201.}
\tag{3}
\]

因此原始四个 prefix 整数已经落入 `6×94` 个显式候选。

再施加原问题的

\[
\gcd(a_1,b_1)=1
\]

以及 exact contact 的必要条件

\[
K=G^2C^2-D^2N>0,
\]

得到恰好

\[
\boxed{333}
\]

个 admissible prefixes。

这一步没有枚举任意经验高度；(1) 与 (3) 都来自前序严格无界压缩。

---

### 2. 每个第三分母的非 `2,5` 部分都有完备有限来源

写

\[
b_3=h2^u5^v,
\qquad
\gcd(h,10)=1.
\]

A1 universal denominator certificate 已证明

\[
b_3\mid10^{2m_3}Q^2G.
\]

因此

\[
\boxed{h\mid Q^2G.}
\tag{4}
\]

更精确地，`h` 必须整除 `Q^2G` 的 `2,5`-free 部分。

脚本对每个 prefix 精确分解该整数，并枚举它的**全部正因子**作为 `h`。

所以 odd-prime supply 没有遗漏。

---

### 3. 用 `(x,y)` 参数化全部 `2/5` 尾状态

令

\[
T=10^\ell,
\qquad
\rho=\frac{b_3}{T}.
\]

写

\[
\boxed{
\rho=h2^x5^y,
\qquad
x=u-\ell,
\quad
y=v-\ell.
}
\tag{5}
\]

由于 `g=2`，第三分母位数窗严格等价于

\[
\boxed{10\le\rho<100.}
\tag{6}
\]

对固定 prefix，normalized square identity 为

\[
V^2=K-2\rho DN.
\tag{7}
\]

令

\[
k_p=v_p(K),
\qquad
d_p=v_p(D),
\qquad n_p=v_p(N).
\]

则 resonance lines 为

\[
\boxed{
x_*=k_2-(1+d_2+n_2),}
\tag{8}
\]

\[
\boxed{
y_*=k_5-(d_5+n_5).}
\tag{9}

---

### 4. 为什么 `(x,y)` 的枚举盒覆盖全部整数点

前序文件
`rational-contact.md`
已经证明：

#### `2+5-` cross corridor

若

\[
x>x_*,\qquad y<y_*,
\]

且 `k_2` 为偶数，则

\[
\boxed{
x\le X_0,}
\]

其中

\[
\boxed{
X_0=
\max\left(
0,
 d_2,
 d_2+\frac{k_2}{2}-v_2(G)-v_2(C),
 d_2+v_2(G)-\frac{k_2}{2}
\right).
}
\tag{10}
\]

若 `k_2` 为奇数，则严格 `x>x_*` 的 K-dominant 一侧不可能产生平方，因为 `v_2(V^2)=k_2` 为奇数。

#### `2-5+` cross corridor

若

\[
x<x_*,\qquad y>y_*,
\]

且 `k_5` 为偶数，则

\[
\boxed{
y\le Y_0,}
\]

其中

\[
\boxed{
Y_0=
\max\left(
0,
 d_5,
 d_5+\frac{k_5}{2}-v_5(G)-v_5(C),
 d_5+v_5(G)-\frac{k_5}{2}
\right).
}
\tag{11}
\]

`k_5` 为奇数时同理，严格 high side 不可能是平方。

现在结合 decade strip (6)：

- `++` 区域中 `y\ge y_*`，故 `rho<100` 给 `x` 上界；
- `--` 区域中 `y\le y_*`，故 `rho\ge10` 给 `x` 下界；
- 两条 cross corridor 分别由 (10)、(11) 截断 high coordinate；
- `x=x_*` 或 `y=y_*` 的 resonance 线上，(6) 自动把另一个坐标限制到有限区间。

脚本中的 `finite_xy_box()` 正是把这四种情况取最坏端点后合并成一个保守矩形，再逐点用 (6) 和 sector 条件精确过滤。

因此它覆盖每一个可能的整数 `(x,y)`；有限盒不是经验截断。

---

### 5. partial-data rational-contact square sieve 是完备必要条件

对每个完整 prefix、`h,x,y`，`rho` 因而 `theta=rho/D` 已经固定。

记

\[
P=\frac CD,
\qquad
S=\frac N{G^2}.
\]

在尚未构造 `r_3` 时，rational-contact quadratic 的判别核

\[
\boxed{
\Xi=P^2-(1+2\theta)S
}
\tag{12}
\]

若存在有理 `r_3`，则 `Xi` 必须是非负有理平方。

这正是 `diagonal.md` 中保留的合法用途：

- 在完整 exact candidate 上不能把 square property 重复算成额外方程；
- 在这里只固定 partial data `(P,S,theta)`、尚未恢复 `r_3`，所以它是完备的必要筛选器。

脚本把 `Xi` 写成 `Fraction`，分别对分子、分母做整数平方根测试。

没有模素数近似，也没有浮点平方判断。

---

### 6. 若平方通过，脚本仍会完整恢复并复核原式

虽然本切片最终没有任何 square state，脚本仍实现了完整恢复路径。

若

\[
\Xi=z_0^2,
\]

则枚举二次式两个根

\[
\boxed{
 r_3
=
\frac{
\theta P\pm(1+\theta)z_0
}{1+2\theta}.
}
\tag{13}
\]

对每个正的既约根

\[
r_3=\frac{a_3}{b_3},
\]

令

\[
\ell=\operatorname{digits}(a_3).
\]

再严格检查

\[
\operatorname{digits}(b_3)=g+\ell,
\]

\[
\frac{b_3}{10^\ell}=\rho,
\]

最后直接以 `Fraction` 检查原始拼接平方恒等式。

因此证书即使未来某个中间 square sieve 出现命中，也不会把“必要条件通过”误写成 exact lift。

---

### 7. 精确计算结果

完整 prefix 分布与尾状态数如下：

| `(z,w)` | admissible prefixes | exact `(h,x,y)` states | rational-square states |
|---|---:|---:|---:|
| `(1,1)` | 62 | 908281 | 0 |
| `(1,2)` | 47 | 63262 | 0 |
| `(1,3)` | 88 | 645343 | 0 |
| `(1,4)` | 29 | 33235 | 0 |
| `(3,1)` | 60 | 879010 | 0 |
| `(3,2)` | 47 | 63262 | 0 |
| **总计** | **333** | **2592393** | **0** |

所以甚至在恢复 `r_3` 之前已经得到

\[
\boxed{
\text{rational-square contact states}=0.
}
\]

因此

\[
\boxed{
 d=2,\ r=s=1,\ k=g=2
\text{ 整个切片为空。}
}
\tag{14}

---

### 8. 脚本的预期终端摘要

运行

```bash
uv run python scripts/exact-lift/a1-only/check_a1_top_diag_k2.py --jobs 4
```

预期最终摘要包含

```text
prefixes=333
tail_states=2592393
rational_square_contacts=0
positive_r3_roots=0
exact_hits=0
CERTIFICATE OK: k=g=2, r=s=1 diagonal slice is empty.
```

脚本内部还断言 prefix 数、总状态数和 square 命中数，避免未来修改静默改变证书范围。

---

### 9. 严格证明边界

本证书只关闭

\[
\boxed{k=g=2,\quad r=s=1,\quad d=2.}
\]

它没有证明：

- `k=g\ge3` 的整个 diagonal 为空；
- `k=g=1` 小切片为空；
- `r>1` 或 `s>1` 的最高层为空；
- `d=1,0,-1` 三层为空；
- A1 全局为空。

它的意义在于：minimal diagonal 的第一个真正无界参数值已经通过前序理论压成一个可审计的完整有限证书，并且结果为零候选。

---

## 8. A1 rational-contact discriminant audit — 2026-08-17

> 整合来源：`a1-discriminant-square-audit-2026-08-17.md`。以下正文保留该来源的原始证明状态和审计边界。

本文审计 A1 新框架中反复出现的判别平方

\[
\Xi=P^2-(1+2\theta)S,
\qquad
S=r_1^2+r_2^2.
\]

结论很重要：**在完整 exact-contact 系统中，`Xi` 为有理平方并不是额外独立障碍；它是 contact 恒等式与球面方程的代数重写。**

这不使由其清分母得到的整数恒等式失效；那些恒等式仍可用于赋值、整除和 prime-flow bookkeeping。需要修正的是证明解释：不能再把“`Xi` 是平方”本身当成一条独立于 exact contact 的新筛选器。

本文结论为 **已严格完成 / 审计澄清**。

---

### 1. 完整 contact 系统

A1 rational-contact 坐标满足

\[
\boxed{
P-R=\theta(R-r),
}
\tag{1}
\]

其中

\[
r=r_3,
\qquad
R^2=S+r^2.
\tag{2}
\]

所以

\[
\boxed{
P=R+\theta(R-r).
}
\tag{3}
\]

---

### 2. 判别核精确平方化

代入 (3)：

\[
\begin{aligned}
\Xi
&=P^2-(1+2\theta)S\\
&=\left(R+\theta(R-r)\right)^2
 -(1+2\theta)(R^2-r^2).
\end{aligned}
\]

展开：

\[
\begin{aligned}
\Xi
={}&R^2+2\theta R(R-r)+\theta^2(R-r)^2\\
&-R^2+r^2-2\theta(R^2-r^2).
\end{aligned}
\]

注意

\[
R(R-r)-(R^2-r^2)
=R(R-r)-(R-r)(R+r)
=-r(R-r).
\]

因此

\[
\Xi
=r^2-2\theta r(R-r)+\theta^2(R-r)^2,
\]

即

\[
\boxed{
\Xi
=\left(r-\theta(R-r)\right)^2.
}
\tag{4}
\]

所以只要完整 exact contact (1) 与球面 (2) 成立，`Xi` 自动就是有理平方，因为 `r,theta,R` 在 exact lift 下均为有理数。

---

### 3. 与二次根公式的关系

此前把 `r` 看成未知量时，从

\[
R=\frac{P+\theta r}{1+\theta}
\]

与

\[
R^2=S+r^2
\]

消去 `R`，得到关于 `r` 的二次式，并把

\[
\Xi=P^2-(1+2\theta)S
\]

识别为判别核。

这个步骤作为**反向构造测试**仍然完全正确：如果只固定 `(P,S,theta)`，想问是否存在有理 `r`，那么 `Xi` 必须为有理平方。

但一旦已经假设存在完整 exact-lift 候选 `(R,r)` 并满足 contact，(4) 说明这个平方条件不再提供第二条独立方程。

因此后续应区分：

- **prefix/tail partial data sieve**：固定部分数据、尚未构造 `r` 时，平方判别仍可用于筛选；
- **full exact-candidate deduction**：已经使用完整 contact 与球面后，不能再把同一个平方性质重复计作独立约束。

---

### 4. 整数平方证书仍然有效，但应理解为整数化恒等式

此前定义

\[
T=10^\ell,
\qquad
D=10^gQ,
\qquad
K=G^2C^2-D^2N,
\]

并得到

\[
\boxed{
W^2=T^2K-2Tb_3DN.
}
\tag{5}
\]

式 (5) 仍然是 exact lift 的严格必要整数恒等式。

根据 (4)，其平方根可以理解为 contact residual 的清分母：

\[
\sqrt\Xi
=\left|r-\theta(R-r)\right|.
\]

因此 (5) 的价值在于：

1. 把有理 contact residual 强制整数化；
2. 允许对 `2,5` 赋值进行严格比较；
3. 与 denominator certificate、prime supply 和 fixed-prefix tail reduction 联用；
4. 在只给定 partial data 时作为有效的平方筛选。

它的价值**不应**表述为“在完整 contact 之外又多出一个神秘平方障碍”。

---

### 5. 对现有 A1 证明树的影响

#### 保持有效

以下已经完成的 A1 结果不依赖“平方条件独立”这一解释，因此保持有效：

- rational-contact 恒等式；
- universal integer-square identity 本身；
- denominator divisibility certificate；
- `2/5` 赋值分层；
- resonance/cross-corridor fixed-prefix finite 结论；
- safe integer-gap recovery；
- moving-prefix contact window 中直接由 `P>R`、digit window 得到的 `K` 不等式；
- 2026-08-17 的全局四层定理与最高层 endpoint/residue kernel。

#### 需要避免的表述

后续不得使用以下逻辑：

\[
\text{full contact + sphere}
\Longrightarrow
\Xi\text{ square}
\]

然后把 `Xi square` 再当成与前两者独立的第三条方程进行维数计数或“额外稀疏性”论证。

---

### 6. 当前研究意义

这次审计把 A1 的真正独立输入进一步厘清：

\[
\boxed{
\text{decimal contact}
+\text{sphere/rationality}
+\text{primitive denominator structure}
+\text{digit geometry}
}
\]

其中平方证书属于前两者的整数化接口。

因此 moving-prefix 的下一步应继续使用：

- endpoint/residue kernel；
- `gcd(U_i,b_i)=1`；
- denominator prime graph；
- safe integer-gap divisibility；
- `2/5` 整数赋值；

而不把判别平方本身重复计算成新的独立约束。

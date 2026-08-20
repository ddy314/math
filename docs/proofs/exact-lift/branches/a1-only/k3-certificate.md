# A1 minimal diagonal `k=g=3` finite certificate

> 日期：2026-08-19。本文关闭 `A_1` 最高层 minimal diagonal 的第三个完整切片
> \[
> d=2,\qquad r=s=1,\qquad k=g=3.
> \]
> 它依赖 `diagonal.md` 的 valuation / odd-prime supply / cross-corridor 定理，以及 `near-integer-tail.md` 新得到的 near-integer tail lock。

结论：

\[
\boxed{
 d=2,\ r=s=1,\ k=g=3
\text{ 整个切片为空。}
}
\]

状态：**有限证书 / 严格完成。**

验证脚本：

```bash
uv run python scripts/exact-lift/a1-only/check_a1_top_diag_k3.py
```

---

## 1. near-integer theorem 把 `j` 精确缩成 901 个整数

`near-integer-tail.md` 已证明，对全部 `k=g\ge3` minimal diagonal，令

\[
N=j-10^k+1\in\mathbb Z,
\qquad
\rho=\frac{b_3}{10^\ell},
\]

则

\[
\boxed{
N-0.0505<\rho<N+0.0175.
}
\tag{1}
\]

另一方面第三分母位数窗精确给出

\[
10^{k-1}\le\rho<10^k.
\tag{2}
\]

由 (1)–(2)，因为 `N` 是整数：

\[
N>10^{k-1}-0.0175
\Longrightarrow
N\ge10^{k-1},
\]

以及

\[
N<10^k+0.0505
\Longrightarrow
N\le10^k.
\]

所以一般地有新的整数窗

\[
\boxed{
10^{k-1}\le N\le10^k,
}
\tag{3}
\]

等价于

\[
\boxed{
11\cdot10^{k-1}-1
\le j\le
2\cdot10^k-1.
}
\tag{4}
\]

专门取 `k=3`：

\[
\boxed{1099\le j\le1999.}
\tag{5}
\]

因此此前 sharp significand lock 留下的连续实窗口在这一层被转成恰好 `901` 个整数值。

---

## 2. 完整 prefix box

minimal diagonal 六类型为

\[
(z,w)
\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\}.
\]

在 `k=g=3`：

\[
\boxed{b_2=1,}
\]

\[
\boxed{b_1=10^7-w,}
\]

\[
\boxed{a_2=10^7-z,}
\]

\[
\boxed{
 a_1
=10^{11}
+(5-z-w)10^4+j.
}
\tag{6}
\]

脚本枚举 (5) 中所有 `j`，并保留原问题必要条件

\[
\gcd(a_1,b_1)=1.
\tag{7}
\]

再定义

\[
Q=10b_1+1,
\qquad
G=b_1,
\]

\[
C=a_1 10^7+a_2,
\]

\[
\mathcal N=a_1^2+(a_2b_1)^2,
\]

\[
D=10^3Q,
\]

以及

\[
\boxed{
K=G^2C^2-D^2\mathcal N.
}
\tag{8}
\]

exact contact 必有 `P>R>\sqrt S`，所以还必须

\[
\boxed{K>0.}
\tag{9}
\]

施加 (7)、(9) 后，完整 prefix 数为：

| `(z,w)` | admissible prefixes |
|---|---:|
| `(1,1)` | 598 |
| `(1,2)` | 451 |
| `(1,3)` | 773 |
| `(1,4)` | 300 |
| `(3,1)` | 597 |
| `(3,2)` | 451 |
| **总计** | **3170** |

这里没有经验截断；(5) 已经覆盖全部可能 `j`。

---

## 3. odd-prime supply 只有 `32,8,2,6` 种

写 normalized tail

\[
\rho=h2^x5^y,
\qquad
\gcd(h,10)=1.
\]

`diagonal.md` 已证明 minimal diagonal 的强化 odd-prime supply：

- `Q` 侧每个奇素数至多按其在 `Q` 中的原指数进入；
- `b_1` 侧只有 `1 mod 4` 的奇 prime-power block 可以进入，并且必须整块选择。

因此 `h` 不需要枚举 universal certificate 中的 `Q^2G` 全部因子。

对 `k=3`，四种 `w` 的完整供给数已经严格化为

\[
\boxed{
\#h=
32,8,2,6
\quad
(w=1,2,3,4).
}
\tag{10}
\]

脚本重新精确分解 `b_1,Q` 并按该 block-selector 规则构造全部 `h`，同时断言数量恰为 (10)。

---

## 4. `2/5` 几何在这一层完全显式

对 `k=g=3`，`diagonal.md` 的 valuation normal form 给出

\[
\boxed{v_5(K)=0,}
\]

\[
\boxed{v_2(K)=2v_2(w),}
\]

\[
\boxed{X_0=Y_0=3.}
\tag{11}
\]

脚本对 3170 个 prefixes 逐个重新计算这些赋值并断言 (11)。

令

\[
n_2=v_2(\mathcal N),
\qquad
n_5=v_5(\mathcal N).
\]

resonance lines 是

\[
\boxed{
x_*=2v_2(w)-4-n_2,}
\tag{12}
\]

\[
\boxed{
y_*=-3-n_5.}
\tag{13}
\]

第三尾 decade strip 为

\[
\boxed{100\le h2^x5^y<1000.}
\tag{14}
\]

与既有 cross-corridor theorem 联用：

- `2+5-` corridor 中若 `x>x_*`、`y<y_*`，则 `x\le3`；
- `2-5+` corridor 中若 `x<x_*`、`y>y_*`，则 `y\le3`；
- `++`、`--` 和 resonance 线上，(14) 与另一坐标的 resonance bound 自动给出有限端点。

因此对每个 `(prefix,h)` 都存在一个**由定理推出的完备有限 `(x,y)` 矩形**。脚本先生成该矩形，再逐点用 (14) 和 sector 条件过滤。

---

## 5. near-integer theorem 把所有 tail states 压到 230 个

对每个 prefix 定义

\[
N=j-999.
\]

由 (1)，任何 exact lift 都必须满足

\[
\boxed{
N-0.0505
< h2^x5^y
<N+0.0175.
}
\tag{15}
\]

脚本以 `Fraction` 精确检查 (15)，没有浮点比较。

在完整 odd-prime supply、完备 `(x,y)` box、decade strip 和 (15) 联合过滤后，3170 个 prefixes 总共只留下：

| `(z,w)` | prefixes | surviving exact tail states |
|---|---:|---:|
| `(1,1)` | 598 | 58 |
| `(1,2)` | 451 | 38 |
| `(1,3)` | 773 | 23 |
| `(1,4)` | 300 | 12 |
| `(3,1)` | 597 | 61 |
| `(3,2)` | 451 | 38 |
| **总计** | **3170** | **230** |

这里的 `230` 不是抽样；它是所有已证明必要条件下的完整剩余状态数。

---

## 6. 230 个状态全部死在 partial-data rational square sieve

对每个剩余 `(prefix,h,x,y)`，`rho` 已固定，故

\[
\theta=\frac\rho D
\]

也固定。

记

\[
P=\frac CD,
\qquad
S=\frac{\mathcal N}{G^2}.
\]

此时第三分数 `r_3` 尚未构造，所以 discriminant audit 明确允许使用 partial-data 必要条件

\[
\boxed{
\Xi=P^2-(1+2\theta)S
\text{ 必须是非负有理平方。}
}
\tag{16}
\]

脚本用既约 `Fraction` 表示 `Xi`，分别对分子、分母做整数平方根检查。

精确结果为

\[
\boxed{
\text{rational-square states}=0.
}
\tag{17}
\]

分类型结果全部为零：

| `(z,w)` | surviving tail states | rational-square states |
|---|---:|---:|
| `(1,1)` | 58 | 0 |
| `(1,2)` | 38 | 0 |
| `(1,3)` | 23 | 0 |
| `(1,4)` | 12 | 0 |
| `(3,1)` | 61 | 0 |
| `(3,2)` | 38 | 0 |
| **总计** | **230** | **0** |

因此没有任何状态能够构造有理 `r_3`，从而不可能存在 exact lift。

故

\[
\boxed{
 d=2,\ r=s=1,\ k=g=3
\text{ 为空。}
}
\tag{18}
\]

---

## 7. 证书的严格边界

本文只关闭

\[
\boxed{k=g=3,\quad r=s=1,\quad d=2.}
\]

结合此前 `k=1,2` 两个证书，minimal diagonal 现在已经严格排除

\[
\boxed{k=g\in\{1,2,3\}.}
\]

因此该 diagonal 的真正无界前沿推进到

\[
\boxed{k=g\ge4.}
\]

`near-integer-tail.md` 的常数窗口对全部 `k\ge3` 成立，所以 `k\ge4` 时误差实际上进一步缩小十倍：

\[
-0.0017425
<j-10^k-\rho+1
<0.005045.
\]

下一阶段应优先利用这个更薄的窗口与 `rho=h2^x5^y` 的约分母结构，尝试把 `k\ge4` 从逐层 finite certificate 转成统一矛盾。

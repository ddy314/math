# A1-only Finite Layer Certificates Ledger

> 本文件是细粒度研究记录的机械归并账本。各来源的标题、正文和证明状态原样保留；账本中的局部闭合、有限证书或降级路线均不表示该分支或主不存在性命题已经关闭。

## 来源索引

- [`k24-k25-uniform-certificates.md`](#source-k24-k25-uniform-certificates)
- [`k26-k30-uniform-certificates.md`](#source-k26-k30-uniform-certificates)
- [`k3-certificate.md`](#source-k3-certificate)
- [`k31-uniform-certificate.md`](#source-k31-uniform-certificate)
- [`k4-k5-certificates.md`](#source-k4-k5-certificates)
- [`k6-ell6-certificate.md`](#source-k6-ell6-certificate)
- [`k6-ell7-certificate.md`](#source-k6-ell7-certificate)
- [`k6-first-boundary-certificate.md`](#source-k6-first-boundary-certificate)
- [`k6-uniform-tail-certificate.md`](#source-k6-uniform-tail-certificate)
- [`uniform-layer-finite-box.md`](#source-uniform-layer-finite-box)

<a id="source-k24-k25-uniform-certificates"></a>

> 整合来源：`k24-k25-uniform-certificates.md`

# A1 minimal diagonal: uniform certificates for `k=24,25`

> 日期：2026-08-19。本文继续 `uniform-layer-finite-box.md`。

固定层统一证书继续关闭

\[
\boxed{k=g=24,25.}
\]

因此结合此前 `k=1,...,23`：

\[
\boxed{
1\le k=g\le25
\Longrightarrow
\text{minimal diagonal empty}.
}
\tag{1}
\]

状态：**已由 exact integer/rational certificate 严格复核。**

---

## 1. `k=24`

完整 odd-prime supply 数量按 `w=1,2,3,4` 为

\[
\boxed{(256,256,32,64).}
\]

5-adic/root-lifting 与 2-adic floor 给出

\[
\underline x_*=-26,
\qquad
\underline y_*=-59.
\]

cross-corridor + decade 推出的 theorem-derived exponent box 为

\[
\boxed{
-298\le x\le216,
\qquad
-114\le y\le45.
}
\]

完整 decade state 数为

\[
\boxed{188712.}
\]

在旧的更宽窗口

\[
5.09<10^{24}(\lceil\rho\rceil-\rho)<50.45
\]

中命中数为

\[
\boxed{0.}
\]

因此当然也没有状态落入新 sharpened window

\[
15.09<10^{24}(\lceil\rho\rceil-\rho)<39.003.
\]

---

## 2. `k=25`

完整 odd-prime supply 数量为

\[
\boxed{(2048,48,16,512).}
\]

valuation floors：

\[
\underline x_*=-27,
\qquad
\underline y_*=-61.
\]

exponent box：

\[
\boxed{
-316\le x\le224,
\qquad
-122\le y\le47.
}
\]

完整 decade state 数为

\[
\boxed{796197.}
\]

同样在旧宽窗口中

\[
\boxed{\text{gap hits}=0.}
\]

所以 `k=g=25` 为空。

---

## 3. 新前沿

当前 minimal diagonal 已严格关闭

\[
\boxed{1\le k=g\le25.}
\]

因此首个未关闭固定层推进到

\[
\boxed{k=g\ge26.}
\]

但从证明结构上看，下一步优先级已经不再是继续逐层 factor `b_1,Q`。`sharp-positive-tail-window.md` 与 `gap-denominator-normal-form.md` 已把统一 gap-desert 问题压成：

1. central denominator 的 24 个固定整数 `Gamma=16,...,39`；
2. `a>k` 或 `b>k` 的 deep-denominator sector。

其中 central sector 已完全消去自由 exponent pair，是下一步最值得优先攻击的统一算术核心。

---

## 4. 可复核脚本

脚本：

`check_a1_top_diag_uniform_layers_24_25.py`

它复用 `check_a1_top_diag_uniform_layers.py` 的完整 fixed-layer machinery，并刻意检查旧的更宽 gap window；因此 `0` 命中对 sharpened window 是更强的有限证书。

---

<a id="source-k26-k30-uniform-certificates"></a>

> 整合来源：`k26-k30-uniform-certificates.md`

# A1 minimal diagonal: uniform fixed-layer certificates `k=26..30`

> 日期：2026-08-19。依赖 `uniform-layer-finite-box.md` 与 `uniform-2adic-prefix.md`。

本文继续 generic fixed-`k` finite-box certificate，把此前 `k<=25` 的有限层前沿推进到

\[
\boxed{k=g=26,27,28,29,30.}
\]

每一层都重新：

1. 精确 factor `b_1=10^{2k+1}-w` 与 `Q=10b_1+1`；
2. 构造完整 minimal-diagonal odd-prime supply `H_{k,w}`；
3. 用 `p`-adic root lifting 求 prefix 的 exact valuation floor；
4. 由 cross-corridor + decade 推出 theorem-derived finite exponent box；
5. 对盒内每个 exact rational state 检查旧的、更宽的 one-sided near-integer window
   \[
   5.09\,10^{-k}<\lceil\rho\rceil-\rho<50.45\,10^{-k}.
   \]

所有层的命中数均为 `0`。由于新 sharpened window `[15.09,39.003]` 严格包含于旧窗口，这些证书自动也是当前理论的更强有限排除。

状态：**已严格完成；附带脚本可精确复核。**

---

## 1. 结果总表

`H counts` 按 `w=1,2,3,4` 排列。

| `k` | `H counts` | `x* floor` | `y* floor` | exponent box `(xmin,xmax;ymin,ymax)` | decade states | wide-gap hits |
|---:|---|---:|---:|---|---:|---:|
| 26 | `(128,24,32,256)` | `-28` | `-66` | `(-329,239;-126,49)` | `146,580` | `0` |
| 27 | `(12288,160,32,512)` | `-29` | `-67` | `(-339,245;-130,51)` | `4,238,867` | `0` |
| 28 | `(256,768,16,64)` | `-30` | `-70` | `(-330,255;-126,52)` | `390,688` | `0` |
| 29 | `(64,96,128,256)` | `-31` | `-72` | `(-343,263;-131,54)` | `196,277` | `0` |
| 30 | `(32768,128,64,64)` | `-32` | `-75` | `(-378,273;-145,56)` | `11,672,944` | `0` |

因此

\[
\boxed{
26\le k=g\le30
\Longrightarrow
\text{minimal diagonal empty}.}
\tag{1}
\]

结合旧证书：

\[
\boxed{
1\le k=g\le30
\Longrightarrow
\text{minimal diagonal empty}.}
\tag{2}
\]

首个尚未由 fixed-layer certificate 关闭的层推进到

\[
\boxed{k=g\ge31.}
\tag{3}
\]

---

## 2. `2`-adic floor 与统一闭式一致

`uniform-2adic-prefix.md` 已证明对所有 `k>=3`

\[
\underline x_*(k)=-k-2.
\]

上表五层依次得到

\[
-28,-29,-30,-31,-32,
\]

与闭式完全一致。因此这些层真正需要 root lifting 的只有 `5`-adic prefix depth。

各层六类型的 `max v_5(N)` 为：

\[
\begin{array}{c|c}
k&((1,1),(1,2),(1,3),(1,4),(3,1),(3,2))\\ \hline
26&(37,37,37,40,37,38)\\
27&(39,38,40,39,40,39)\\
28&(40,41,40,42,40,40)\\
29&(42,43,42,41,42,42)\\
30&(45,43,43,43,43,43)
\end{array}
\]

因此

\[
\underline y_*(k)=-k-\max v_5(N)
\]

正好给表中的 `-66,-67,-70,-72,-75`。

---

## 3. `k=30` 的大 supply 不改变证书性质

`k=30,w=1` 的完整 odd-prime supply 达到

\[
|H_{30,1}|=32768.
\]

因此该层 decade state 数上升到一千一百余万。实际复核可把 `h` supply 分块并行；每个 worker 使用相同的 exact integer/rational inequalities，最终只对互不相交的 `h` 子集计数再求和。

这只是计算调度，不引入概率步骤，也不改变 certificate：总计

\[
\boxed{11,672,944}
\]

个 decade states 全部被检查，wide-gap hit 总数严格为

\[
\boxed0.
\]

---

## 4. 与 uniform central/deep 证明线的关系

这些 fixed-layer certificates 是保险线，不取代当前 `k`-uniform 的 central/deep 攻击。

当前统一理论已经把所有 `k>=26` 分成：

- central denominator：有限 type-gap + finite `U` generalized Pell families；
- deep denominator：valuation/resonance lattice + unit-square + directed Q-side supply。

本文的作用是把真正可能需要统一理论处理的首层从 `26` 再推到 `31`，并为后续任何全局高度界提供更宽的已验证基区间。

---

## 5. 可复核脚本

脚本：

`../../../../../scripts/exact-lift/a1-only/check_a1_top_diag_uniform_layers_26_30.py`

它复用 `check_a1_top_diag_uniform_layers.py` 中的 exact supply、root-lifting、box 与 rational-gap routines，并对上表 metadata 与 `0` hit 逐层断言。

---

<a id="source-k3-certificate"></a>

> 整合来源：`k3-certificate.md`

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

---

<a id="source-k31-uniform-certificate"></a>

> 整合来源：`k31-uniform-certificate.md`

# A1 minimal diagonal: exact `k=g=31` uniform certificate

> 日期：2026-08-20。依赖 `uniform-layer-finite-box.md`。本证书继续使用旧的更宽 near-integer window，因此比当前 sharpened window 更强。

本文关闭

\[
\boxed{k=g=31.}
\]

状态：**已严格完成。**

---

## 1. 完整 factorization

令

\[
b_1=10^{63}-w,
\qquad
Q=10^{64}-(10w-1).
\]

四个 `w` 的完整 factorization 已全部获得并做素性确认。此前最后的缺口是 `w=4` 的 Q-side；现在有

\[
\boxed{
10^{64}-39
=7^2\cdot34673\cdot
7675984356934380436832851\cdot
766793494003346313676638849083843.
}
\tag{1}
\]

最后两个大因子均为素数。

由完整 odd-prime supply theorem 得到四个 `w` 的 `h` 数量

\[
\boxed{(|H_1|,|H_2|,|H_3|,|H_4|)=(16384,96,16,96).}
\tag{2}
\]

---

## 2. valuation floors 与 finite box

对六类型用 exact p-adic root lifting 计算 prefix `N` 的最大赋值：

\[
\begin{array}{c|cc}
(z,w)&\max v_2(N)&\max v_5(N)\\ \hline
(1,1)&1&45\\
(1,2)&3&44\\
(1,3)&1&44\\
(1,4)&5&45\\
(3,1)&1&44\\
(3,2)&3&47
\end{array}
\]

所以 global resonance floors 为

\[
\boxed{\underline x_*=-33,\qquad \underline y_*=-78.}
\tag{3}
\]

结合 decade 与 primitive cross-corridor，`uniform-layer-finite-box.md` 的一般公式给出

\[
\boxed{
-321\le x\le284,
\qquad
-120\le y\le58.
}
\tag{4}
\]

这是与 `ell` 无关的完整 finite search box。

---

## 3. exact decade scan

脚本

`check_a1_top_diag_uniform_layer_31.py`

枚举全部合法 `h`，对每个 `x` 精确恢复 decade 中至多两个 `y`，并应用两个 cross-corridor necessary conditions。

落入

\[
10^{30}\le\rho<10^{31}
\]

的状态数按 `w` 为

\[
\boxed{
\begin{array}{c|r}
w&\text{decade states}\\ \hline
1&6,066,806\\
2&36,304\\
3&6,277\\
4&37,285
\end{array}}
\]

总计

\[
\boxed{6,146,672.}
\tag{5}
\]

---

## 4. 仍检查旧的更宽 gap window

当前理论只要求排除

\[
15.09<10^{31}(\lceil\rho\rceil-\rho)<39.003.
\]

为保持与 `k=6..30` 保险证书一致，本层仍检查旧的更宽区间

\[
\boxed{
5.09<10^{31}(\lceil\rho\rceil-\rho)<50.45.
}
\tag{6}
\]

所有 `6,146,672` 个 decade states 中：

\[
\boxed{\text{near hits}=0.}
\tag{7}
\]

因此 sharpened window 当然也没有 candidate。

---

## 5. 结论

结合旧证书 `k<=30`：

\[
\boxed{1\le k=g\le31\Longrightarrow\text{empty}.}
\tag{8}
\]

所以 fixed-layer 保险线的首个未关闭层现在推进到

\[
\boxed{k=g=32.}
\]

这与统一 deep 理论独立：central 已对所有 `k>=26` 关闭，而 deep 统一证明仍继续处理 `k>=32` 的无限尾。

---

<a id="source-k4-k5-certificates"></a>

> 整合来源：`k4-k5-certificates.md`

# A1 minimal diagonal `k=g=4,5` finite certificates

> 日期：2026-08-19。本文继续 `k3-certificate.md` 的严格有限证书方法，关闭
> \[
> d=2,\qquad r=s=1,\qquad k=g\in\{4,5\}.
> \]
> 两层均使用 `near-integer-tail.md` 的 **k-dependent** 误差，而不是固定的 `k=3` 粗窗口。

结论：

\[
\boxed{
 d=2,\ r=s=1,\ k=g=4
\text{ 为空},
}
\]

\[
\boxed{
 d=2,\ r=s=1,\ k=g=5
\text{ 为空}.
}
\]

状态：**有限证书 / 严格完成。**

验证脚本：

```bash
uv run python scripts/exact-lift/a1-only/check_a1_top_diag_k45.py
```

---

## 1. 统一输入

对任意 `k=g\ge3`，令

\[
N_0=j-10^k+1\in\mathbb Z,
\qquad
\rho=\frac{b_3}{10^\ell}.
\]

near-integer theorem 的未粗化版本为

\[
\boxed{
-17.425\,10^{-k}
<N_0-\rho
<50.45\,10^{-k}.
}
\tag{1}
\]

第三尾 decade strip 为

\[
\boxed{
10^{k-1}\le\rho<10^k.
}
\tag{2}
\]

由整数性得到完整 `j` 窗

\[
\boxed{
11\cdot10^{k-1}-1
\le j\le
2\cdot10^k-1.
}
\tag{3}
\]

minimal diagonal 的六个 prefix 类型仍为

\[
(z,w)
\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\},
\]

并且

\[
b_2=1,
\qquad
b_1=10^{2k+1}-w,
\qquad
a_2=10^{2k+1}-z,
\]

\[
\boxed{
 a_1
=10^{3k+2}
+(5-z-w)10^{k+1}+j.
}
\tag{4}
\]

与 `k=3` 证书完全相同，枚举 (3) 中全部整数 `j` 后只保留原问题必要条件

\[
\gcd(a_1,b_1)=1,
\qquad
K>0.
\tag{5}
\]

---

## 2. tail supply 与 `(x,y)` box 仍然完备

定义

\[
Q=10b_1+1,
\qquad
G=b_1,
\]

\[
C=a_1 10^{2k+1}+a_2,
\]

\[
\mathcal N=a_1^2+(a_2b_1)^2,
\qquad
D=10^kQ,
\]

\[
K=G^2C^2-D^2\mathcal N.
\]

`diagonal.md` 已对全部 `k\ge3` 证明

\[
\boxed{v_5(K)=0,}
\]

\[
\boxed{v_2(K)=2v_2(w),}
\]

以及

\[
\boxed{X_0=Y_0=k.}
\tag{6}
\]

脚本在两个层级的每个 admissible prefix 上重新计算并断言这些等式。

odd-prime supply 仍使用强化 prime-graph 版本：若

\[
\rho=h2^x5^y,
\qquad\gcd(h,10)=1,
\]

则 `Q` 侧只能取普通因子，`b_1` 侧只能整块选择 `1 mod 4` 的奇 prime-power blocks。脚本精确分解 `Q,b_1` 并构造全部 `h`。

对固定 `(prefix,h)`，由 resonance lines、(6) 与 decade strip (2) 构造 theorem-derived finite `(x,y)` box；没有经验 exponent cutoff。

最后用 (1) 的当前 `k` 精确窗口过滤 `rho`，并对剩余 partial data 使用合法的 rational-square 必要条件

\[
\boxed{
\Xi=P^2-(1+2\theta)S
\text{ 必须是非负有理平方},
}
\tag{7}
\]

其中

\[
P=\frac CD,
\qquad
S=\frac{\mathcal N}{G^2},
\qquad
\theta=\frac\rho D.
\]

所有计算使用整数与 `Fraction`。

---

## 3. `k=g=4` 完整结果

此时

\[
10^3\le N_0\le10^4,
\]

故

\[
10999\le j\le19999.
\]

near-integer 窗使用未粗化的

\[
\boxed{
-0.0017425
<N_0-\rho
<0.005045.
}
\tag{8}
\]

四种 `w` 的完整 odd-prime supply 数为

\[
\boxed{
\#h=24,48,32,16
\quad(w=1,2,3,4).
}
\tag{9}
\]

完整计算结果：

| `(z,w)` | admissible prefixes | surviving tail states | rational-square states |
|---|---:|---:|---:|
| `(1,1)` | 5839 | 37 | 0 |
| `(1,2)` | 4494 | 66 | 0 |
| `(1,3)` | 8868 | 65 | 0 |
| `(1,4)` | 3001 | 25 | 0 |
| `(3,1)` | 5838 | 38 | 0 |
| `(3,2)` | 4495 | 66 | 0 |
| **总计** | **32535** | **297** | **0** |

因此

\[
\boxed{k=g=4\text{ minimal diagonal 为空}.}
\tag{10}
\]

---

## 4. `k=g=5` 完整结果

此时

\[
10^4\le N_0\le10^5,
\]

故

\[
109999\le j\le199999.
\]

near-integer 窗进一步缩成

\[
\boxed{
-0.00017425
<N_0-\rho
<0.0005045.
}
\tag{11}
\]

四种 `w` 的完整 odd-prime supply 数为

\[
\boxed{
\#h=16,24,32,16
\quad(w=1,2,3,4).
}
\tag{12}
\]

完整计算结果：

| `(z,w)` | admissible prefixes | surviving tail states | rational-square states |
|---|---:|---:|---:|
| `(1,1)` | 59997 | 30 | 0 |
| `(1,2)` | 43449 | 110 | 0 |
| `(1,3)` | 84707 | 151 | 0 |
| `(1,4)` | 27691 | 34 | 0 |
| `(3,1)` | 59997 | 28 | 0 |
| `(3,2)` | 43449 | 112 | 0 |
| **总计** | **319290** | **465** | **0** |

因此

\[
\boxed{k=g=5\text{ minimal diagonal 为空}.}
\tag{13}
\]

---

## 5. 当前前沿

结合原有 `k=1,2`、本文之前新增的 `k=3` 与本文件：

\[
\boxed{
 k=g\in\{1,2,3,4,5\}
\text{ 的 minimal diagonal 全部为空。}
}
\tag{14}
\]

所以该 diagonal 的无界前沿推进为

\[
\boxed{k=g\ge6.}
\tag{15}
\]

有限证书本身不替代统一证明。不过数值结构已经非常明确：随着 `k` 增大，prefix 数按十倍量级增长，但 near-integer theorem 把真正进入平方筛选的 tail states 继续压在几百个量级。这说明下一步最值得抽取的是 **为什么这些 near-integer S-unit states 统一无法满足 rational-square contact**，而不是机械地逐个继续增加 `k`。

---

<a id="source-k6-ell6-certificate"></a>

> 整合来源：`k6-ell6-certificate.md`

# A1 minimal diagonal `k=g=6, ell=6` residual-shell certificate

> 日期：2026-08-19。
> 本文继续 `k6-first-boundary-certificate.md`，关闭下一条 tail shell
> \[
> \boxed{
> d=2,\quad r=s=1,\quad k=g=6,\quad \ell=6.
> }
> \]

结论：

\[
\boxed{\text{该 shell 为空。}}
\]

验证脚本：

```bash
uv run python scripts/exact-lift/a1-only/check_a1_top_diag_k6_ell6.py
```

状态：**有限 divisor-congruence 证书。**

---

## 1. residual 窗只有 `6,...,50`

`positive-tail-residual.md` 给出

\[
5.09\,10^{\ell-k}<t<50.45\,10^{\ell-k}.
\]

当前

\[
\ell=k=6,
\]

所以

\[
5.09<t<50.45.
\]

因此

\[
\boxed{t\in\{6,7,\ldots,50\}.}
\tag{1}
\]

---

## 2. 整个 shell 都属于 regular residual regime

对 `6<=t<=50`：

\[
v_2(t)\le5<6,
\]

\[
v_5(t)\le2<6.
\]

因此 `residual-shell-supply.md` 对全部 45 个 residual 都适用。

令

\[
a_t=2^{v_2(t)}5^{v_5(t)},
\qquad
\widehat t=t/a_t.
\]

任何 exact candidate 都必须满足

\[
\boxed{b_3=a_t h,}
\tag{2}
\]

其中 `h` 属于完整 odd-prime supply，并且

\[
\boxed{
\frac{10^6}{a_t}\mid h+\widehat t.
}
\tag{3}
\]

一旦通过，prefix integer 唯一恢复为

\[
\boxed{
N_0=\frac{a_t(h+\widehat t)}{10^6}.
}
\tag{4}
\]

再要求

\[
10^5\le N_0<10^6.
\]

---

## 3. 完整 supply

与 `k6-first-boundary-certificate.md` 相同，`k=6` 四种 `w` 的 odd-prime supply 数为：

| `w` | `#h` |
|---:|---:|
| `1` | `64` |
| `2` | `32` |
| `3` | `2` |
| `4` | `8` |

这些集合已包含所有可能的 Q-side divisor 和所有允许的 `b_1` 侧 `1 mod4` whole prime-power block selectors。

---

## 4. 精确结果

脚本对每个

\[
w\in\{1,2,3,4\},
\qquad
6\le t\le50,
\qquad
h\in\mathcal H_{6,w}
\]

检查 (3) 与 `N_0` 位数条件。

结果：

| `w` | shell hits |
|---:|---:|
| `1` | `0` |
| `2` | `0` |
| `3` | `0` |
| `4` | `0` |
| **总计** | **0** |

因此 even before 使用 `z`、prefix coprimality、`K>0` 或 rational-square sieve，必要 divisor-congruence 超集已经为空。

所以

\[
\boxed{
 d=2,\ r=s=1,\ k=g=6,\ \ell=6
\text{ 为空。}
}
\tag{5}

---

## 5. `k=6` 当前剩余前沿

positive residual theorem 已经排除

\[
\ell\le4.
\]

第一 boundary certificate 排除

\[
\ell=5.
\]

本文再排除

\[
\ell=6.
\]

因此任何尚存的 `k=g=6` candidate 必须满足

\[
\boxed{\ell\ge7.}
\tag{6}
\]

从 `ell=7` 开始，residual 窗为

\[
50.9<t<504.5,
\]

即 `t=51,...,504`。其中大多数 residual 仍满足 regular-shell 条件；只有少量具有 `v_2(t)>=7` 或 `v_5(t)>=7` 的 deep-2/5 residual 需要单独处理。下一步可以把 `ell=7` 分成 regular 与 deep-2/5 两部分继续压缩。

---

<a id="source-k6-ell7-certificate"></a>

> 整合来源：`k6-ell7-certificate.md`

# A1 minimal diagonal `k=g=6, ell=7` residual-shell certificate

> 日期：2026-08-19。
> 本文继续关闭 `k=g=6` 的下一条 tail shell：
> \[
> \boxed{d=2,\quad r=s=1,\quad k=g=6,\quad \ell=7.}
> \]

结论：

\[
\boxed{\text{该 shell 为空。}}
\]

验证脚本：

```bash
uv run python scripts/exact-lift/a1-only/check_a1_top_diag_k6_ell7.py
```

状态：**regular/deep-2 分裂后的有限 divisor-congruence 证书。**

---

## 1. residual 窗

positive residual theorem 给出

\[
5.09\,10^{\ell-k}<t<50.45\,10^{\ell-k}.
\]

当前 `ell-k=1`，所以

\[
50.9<t<504.5.
\]

因此

\[
\boxed{t\in\{51,52,\ldots,504\}.}
\tag{1}
\]

共 `454` 个 residual。

---

## 2. regular 与 deep residual 的精确分裂

`residual-shell-supply.md` 的 regular 条件是

\[
v_2(t)<7,
\qquad
v_5(t)<7.
\]

在区间 (1) 中，`5^7=78125` 已远大于上界，所以没有 deep-5 residual。

满足 `v_2(t)>=7` 的只有

\[
\boxed{t\in\{128,256,384\}.}
\tag{2}
\]

因此：

- regular residual：其余 `451` 个；
- deep-2 residual：恰好 `128,256,384` 三个。

---

## 3. 451 个 regular residual 全部零命中

对 regular `t`，令

\[
a_t=2^{v_2(t)}5^{v_5(t)},
\qquad
\widehat t=t/a_t.
\]

任何候选必须满足

\[
b_3=a_t h,
\]

以及

\[
\boxed{
\frac{10^7}{a_t}\mid h+\widehat t.
}
\tag{3}
\]

其中 `h` 属于 `k=6` 的完整 odd-prime supply：

| `w` | `#h` |
|---:|---:|
| `1` | `64` |
| `2` | `32` |
| `3` | `2` |
| `4` | `8` |

脚本枚举全部 regular `(w,t,h)`，再由

\[
N_0=\frac{a_t(h+\widehat t)}{10^7}
\]

恢复 prefix integer 并检查

\[
10^5\le N_0<10^6.
\]

结果：

\[
\boxed{\text{regular hits}=0.}
\tag{4}
\]

---

## 4. 三个 deep-2 residual 也全部零命中

现在取

\[
t\in\{128,256,384\}.
\]

三者都满足

\[
v_5(t)=0.
\]

而

\[
b_3=N_0 10^7-t.
\]

第一项被 `5^7` 整除，第二项不被 `5` 整除，所以

\[
\boxed{v_5(b_3)=0.}
\tag{5}
\]

因此第三分母只能写成

\[
\boxed{b_3=h2^u,\qquad u\ge0,}
\tag{6}
\]

其中 `h` 仍来自同一个有限 odd-prime supply。

当前

\[
m_3=k+\ell=13,
\]

所以

\[
10^{12}\le b_3<10^{13}.
\]

对固定 `h`，满足

\[
10^{12}\le h2^u<10^{13}
\]

的整数 `u` 只有有限几个。脚本逐一检查

\[
10^7\mid h2^u+t
\]

并恢复

\[
N_0=\frac{h2^u+t}{10^7}.
\]

结果：

\[
\boxed{\text{deep-2 hits}=0.}
\tag{7}
\]

---

## 5. 结论

regular 与 deep-2 两部分共同覆盖 (1) 的全部 `454` 个 residual，因此

\[
\boxed{
 d=2,\ r=s=1,\ k=g=6,\ \ell=7
\text{ 为空。}
}
\tag{8}

注意本证书仍然没有使用 rational-square sieve；denominator prime supply、positive residual 和十进制恢复已经足够。

---

## 6. `k=6` 当前前沿

已有：

\[
\ell\le4\quad\text{全局排除},
\]

\[
\ell=5\quad\text{boundary certificate 排除},
\]

\[
\ell=6\quad\text{regular shell certificate 排除},
\]

\[
\ell=7\quad\text{本文排除}.
\]

所以 `k=g=6` 的剩余候选现在可以无条件假设

\[
\boxed{\ell\ge8.}
\]

下一层 `ell=8` 的 residual 窗为

\[
509<t<5045,
\]

即

\[
t\in\{510,\ldots,5044\}.
\]

同样可以分成 regular 与少量 deep-2/5 residual，再使用有限 `h` supply 推进。

---

<a id="source-k6-first-boundary-certificate"></a>

> 整合来源：`k6-first-boundary-certificate.md`

# A1 minimal diagonal `k=g=6` first-boundary certificate

> 日期：2026-08-19。
> 本文关闭当前首个未完成层中的第一条尾长边界
> \[
> \boxed{
> d=2,\quad r=s=1,\quad k=g=6,\quad \ell=k-1=5.
> }
> \]

结论：

\[
\boxed{\text{该 boundary 为空。}}
\]

验证脚本：

```bash
uv run python scripts/exact-lift/a1-only/check_a1_top_diag_k6_boundary.py
```

状态：**有限 divisor-congruence 证书。**

---

## 1. 不再枚举 prefix 区间

`positive-tail-residual.md` 已证明第一 boundary 只有

\[
t\in\{1,2,3,4,5\}.
\]

`boundary-residual-2adic.md` 又把 even-`w` 类型收紧为

\[
w=2\Longrightarrow t=3,
\]

\[
w=4\Longrightarrow t=1.
\]

因此需要检查的 residual 集合为

\[
\begin{array}{c|c}
w&t\\
\hline
1&1,2,3,4,5\\
2&3\\
3&1,2,3,4,5\\
4&1
\end{array}
\]

另一方面 `boundary-decimal-supply.md` 已证明：令

\[
a_t=2^{v_2(t)}5^{v_5(t)},
\qquad
\widehat t=t/a_t,
\]

则

\[
b_3=a_t h
\]

且必须

\[
\boxed{
\frac{10^{k-1}}{a_t}\mid h+\widehat t.
}
\tag{1}
\]

一旦 `h` 固定，prefix integer 由

\[
\boxed{
N_0=\frac{a_t(h+\widehat t)}{10^{k-1}}
}
\tag{2}
\]

唯一恢复。

所以本证书根本不扫描

\[
10^5\le N_0<10^6
\]

的九十万个整数；只需枚举 denominator prime graph 给出的有限 `h` supply。

---

## 2. `k=6` 的完整 odd-prime supply 数量

这里

\[
b_1=10^{13}-w,
\qquad
Q=10b_1+1.
\]

对每个 `w`，脚本精确分解 `b_1,Q`，构造

\[
h=q\,s,
\]

其中

\[
q\mid Q
\]

而 `s` 是 `b_1` 中 `1 mod4` odd prime-power blocks 的 whole-block selector。

得到完整 supply 数：

| `w` | `#h` |
|---:|---:|
| `1` | `64` |
| `2` | `32` |
| `3` | `2` |
| `4` | `8` |

脚本把这些数量写成断言，因此未来若因子分解或 supply 实现被修改，会立即报错。

---

## 3. decimal congruence 检查结果

对 §1 中每个允许的 `(w,t)`，逐个 `h` 检查 (1)，并在通过时再恢复 (2) 并检查

\[
10^5\le N_0<10^6.
\]

结果为：

| `w` | `t` | divisor-congruence hits |
|---:|---:|---:|
| `1` | `1` | `0` |
| `1` | `2` | `0` |
| `1` | `3` | `0` |
| `1` | `4` | `0` |
| `1` | `5` | `0` |
| `2` | `3` | `0` |
| `3` | `1` | `0` |
| `3` | `2` | `0` |
| `3` | `3` | `0` |
| `3` | `4` | `0` |
| `3` | `5` | `0` |
| `4` | `1` | `0` |

因此

\[
\boxed{
\text{total divisor-congruence hits}=0.
}
\tag{3}
\]

注意这里甚至没有使用：

- `z`；
- `gcd(a_1,b_1)=1`；
- `K>0`；
- partial-data rational-square sieve；
- `boundary-prime-sieve.md` 的 mod `3/7/11` 条件。

也就是说，一个更宽的 necessary-condition 超集已经为空，所以完整 exact-lift boundary 必然为空。

---

## 4. 证书完备性

完整性来自三条已经证明的 reduction：

1. positive residual theorem 保证 `ell=5` 时只有 `t=1,...,5`；
2. 2-adic boundary theorem 对 `w=2,4` 删除其余 residual；
3. odd-prime supply theorem 保证任何候选的 `h` 必在脚本枚举的有限 supply 中。

对固定 `(h,t)`，式

\[
b_3=a_th=N_0 10^5-t
\]

又唯一决定 `N_0`。因此没有遗漏任何连续变量或 exponent lattice。

于是严格得到

\[
\boxed{
 d=2,\ r=s=1,\ k=g=6,\ \ell=5
\text{ 为空。}
}
\tag{4}

---

## 5. 对 `k=6` 剩余部分的意义

这还没有关闭整个 `k=g=6` diagonal，因为仍需处理

\[
\boxed{\ell\ge6.}
\]

但 `ell<=4` 已由 positive residual theorem 全局排除，`ell=5` 又由本文证书排除。因此 `k=6` 现在可以无条件进入

\[
\boxed{\ell\ge k=6.}
\]

并且 `ell=6` 时 residual 只有

\[
\boxed{t\in\{6,7,\ldots,50\}.}
\]

下一步应把同一个 decimal-supply reduction 推到 `ell=k`：对每个 `t=6,...,50`，先剥离其 `2/5` 部分，再用有限 `h` supply 检查

\[
\frac{10^k}{a_t}\mid h+\widehat t.
\]

这有可能在不调用 rational-square sieve 的情况下继续关闭 `k=6` 的下一层 tail shell。

---

<a id="source-k6-uniform-tail-certificate"></a>

> 整合来源：`k6-uniform-tail-certificate.md`

# A1 minimal diagonal: uniform `k=g=6` tail certificate

> 日期：2026-08-19。本文把此前逐层推进到 `ell>=8` 的 `k=6` tail 改写成一个与 `ell` 无关的统一有限证书，并关闭整个 `k=g=6` minimal diagonal。

当前范围：

\[
d=2,\qquad r=s=1,\qquad k=g=6.
\]

结论：

\[
\boxed{k=g=6\text{ minimal diagonal is empty}.}
\]

状态：**已严格完成，并有精确整数/有理数脚本复核。**

---

## 1. 已有输入

写

\[
\rho=\frac{b_3}{10^\ell}=h2^x5^y,
\qquad \gcd(h,10)=1.
\]

odd-prime supply theorem 给出：对固定 `w`，`h` 只能属于有限集合 `H_{6,w}`；其大小为

\[
|H_{6,1}|=64,\quad |H_{6,2}|=32,\quad |H_{6,3}|=2,\quad |H_{6,4}|=8.
\]

第三分母位数给出

\[
10^5\le \rho<10^6.
\tag{1}
\]

positive residual theorem 又给出。令

\[
N_0=j-10^6+1\in\mathbf Z,
\]

则

\[
\boxed{
5.09\cdot10^{-6}
<N_0-\rho
<50.45\cdot10^{-6}.
}
\tag{2}
\]

因此任何 candidate 的 `rho` 都必须从下方落在某个整数 `N_0` 的极窄单侧邻域内。

minimal-diagonal valuation normal form 还给出

\[
X_0=Y_0=6,
\]

以及 resonance thresholds

\[
x_*=2v_2(w)-1-6-v_2(N),
\qquad
y_*=-6-v_5(N).
\tag{3}
\]

cross-corridor exclusion 为

\[
x>x_*,\ y<y_*,\ x>6\Longrightarrow\bot,
\tag{4}
\]

\[
x<x_*,\ y>y_*,\ y>6\Longrightarrow\bot.
\tag{5}
\]

---

## 2. 对全部 moving prefix 审计 `v_2(N),v_5(N)`

由 near-integer decade，可能的整数中心只需取

\[
10^5\le N_0\le10^6.
\]

对六个 `(z,w)` 类型，把

\[
j=N_0+10^6-1,
\]

代入

\[
a_1=10^{20}+(5-z-w)10^7+j,
\]

\[
b_1=10^{13}-w,
\qquad
a_2=10^{13}-z,
\]

\[
N=a_1^2+(a_2b_1)^2.
\]

对整个整数区间做精确有限审计。得到：

| `(z,w)` | `max v2(N)` | `max v5(N)` |
|---|---:|---:|
| `(1,1)` | 1 | 9 |
| `(1,2)` | 3 | 8 |
| `(1,3)` | 1 | 8 |
| `(1,4)` | 5 | 9 |
| `(3,1)` | 1 | 8 |
| `(3,2)` | 3 | 9 |

代回 (3)，六类型统一满足

\[
\boxed{x_*\ge-8,}
\qquad
\boxed{y_*\ge-15.}
\tag{6}
\]

注意这里扫描的是全部 `N_0`，没有先施加 `gcd(a_1,b_1)=1` 或 `K>0`；因此得到的是 admissible prefixes 的安全超集上界。

---

## 3. cross-corridor 把无限指数平面压成有限盒

由 (4)、(6)：若

\[
x>6,\qquad y<-15,
\]

则必有 `x>x_*`、`y<y_*`，故 impossible。因此

\[
\boxed{x>6\Longrightarrow y\ge-15.}
\tag{7}
\]

同理由 (5)：

\[
\boxed{y>6\Longrightarrow x\ge-8.}
\tag{8}
\]

现在利用 decade (1) 和 finite `h` supply 把每个坐标都封住。

令

\[
H_{\max}=\max_{w,h\in H_{6,w}}h
=1406469760899873417721519.
\]

### `x` 的上界

若 `x<=6` 已有界；若 `x>6`，由 (7) 有 `y>=-15`，并且 `h>=1`，所以

\[
\rho\ge2^x5^{-15}<10^6.
\]

精确比较幂得到

\[
\boxed{x\le54.}
\tag{9}
\]

### `x` 的下界

若 `x>=-8` 已有界；若 `x<-8`，由 (8) 的逆否形式在允许区中只能有 `y<=6`。于是

\[
10^5\le\rho\le H_{\max}2^x5^6.
\]

精确比较给出

\[
\boxed{x\ge-77.}
\tag{10}
\]

### `y` 的上界

若 `y>6`，由 (8) 有 `x>=-8`，故

\[
\rho\ge2^{-8}5^y<10^6,
\]

从而

\[
\boxed{y\le12.}
\tag{11}
\]

### `y` 的下界

若 `y<-15`，由 (7) 的允许区形式只能有 `x<=6`。于是

\[
10^5\le\rho\le H_{\max}2^65^y,
\]

精确比较得到

\[
\boxed{y\ge-29.}
\tag{12}
\]

因此任何 `k=6` candidate 都落入统一有限盒

\[
\boxed{
-77\le x\le54,
\qquad
-29\le y\le12.
}
\tag{13}
\]

这里已经完全消除了第三块位数 `ell`。

---

## 4. 完整 finite supply + near-integer certificate

对每个

\[
w\in\{1,2,3,4\},
\quad h\in H_{6,w},
\quad -77\le x\le54,
\quad -29\le y\le12,
\]

先施加两个 universal cross-corridor exclusion

\[
(x>6\ \&\ y<-15)
\quad\text{or}\quad
(y>6\ \&\ x<-8),
\]

再用精确有理数计算

\[
\rho=h2^x5^y.
\]

落入 decade (1) 的状态总数为

\[
\boxed{8679.}
\]

对每个这样的 `rho`，整数中心被唯一确定为

\[
N_0=\lceil\rho\rceil.
\]

最后检查单侧 gap (2)。结果：

\[
\boxed{
\#\{\text{near-integer hits}\}=0.
}
\tag{14}
\]

因此不存在任何满足所有必要条件的 `rho`，无论 `ell` 取何值。

于是得到

\[
\boxed{k=g=6\text{ 整个 minimal diagonal 为空}.}
\]

---

## 5. 意义

此前的 `ell=5,6,7` shell certificates 仍然是正确的局部证书，但现在被本结果统一覆盖。

更重要的是，本证明展示了新的无界层策略：

1. 对固定 `k` 先在全部整数中心上审计 `v_2(N),v_5(N)`；
2. 用 resonance + cross-corridor 得到 `x_*,y_*` 的统一下界；
3. 用 finite odd-prime supply 与 decade window 把 `(x,y)` 压成有限盒；
4. 最后只检查 one-sided near-integer gap。

这条路线不再枚举第三块位数 `ell`，因此适合继续攻击 `k>=7`。

---

<a id="source-uniform-layer-finite-box"></a>

> 整合来源：`uniform-layer-finite-box.md`

# A1 minimal diagonal: generic fixed-`k` finite-box theorem

> 日期：2026-08-19。本文把 `k=6` 的统一 tail certificate 抽象成任意固定 `k>=6` 的证明模板，并用它精确关闭 `k=6,...,23`。

当前范围：

\[
d=2,\qquad r=s=1,\qquad k=g\ge6.
\]

核心结论有两层。

第一层是结构定理：**对任意固定 `k`，第三块位数 `ell` 可以完全从搜索中消失，所有 candidate 都落入一个显式有限 `(h,x,y)` 盒。**

第二层是精确证书：对

\[
\boxed{6\le k\le23}
\]

所得有限盒全部没有通过 one-sided near-integer gap 的状态，因此

\[
\boxed{k=g=6,7,\ldots,23\text{ 全部为空}.}
\]

状态：**结构定理严格完成；`k=6..23` 由精确整数/有理数脚本严格复核。**

---

## 1. 固定 `k` 的输入

写

\[
\rho=\frac{b_3}{10^\ell}=h2^x5^y,
\qquad \gcd(h,10)=1.
\]

odd-prime supply theorem 给出有限集合

\[
h\in\mathcal H_{k,w},
\]

其中

\[
h=q\,s,\qquad q\mid Q,
\]

而 `s` 是 `b_1` 中所有 `1 mod 4` odd prime-power blocks 的 whole-block selector。

因此固定 `(k,w)` 后 `h` 的可能值有限，并与 `ell` 无关。

第三分母位数给出 decade

\[
\boxed{10^{k-1}\le\rho<10^k.}
\tag{1}
\]

positive-tail residual theorem 给出整数中心

\[
N_0=j-10^k+1
\]

以及严格单侧窗口

\[
\boxed{
5.09\,10^{-k}<N_0-\rho<50.45\,10^{-k}.
}
\tag{2}
\]

minimal-diagonal valuation normal form 给出

\[
X_0=Y_0=k,
\]

\[
x_*=2v_2(w)-1-k-v_2(N),
\qquad
y_*=-k-v_5(N).
\tag{3}
\]

cross-corridor exclusions 为

\[
x>x_*,\ y<y_*,\ x>k\Longrightarrow\bot,
\tag{4}
\]

\[
x<x_*,\ y>y_*,\ y>k\Longrightarrow\bot.
\tag{5}
\]

---

## 2. 不扫描整个 prefix 区间：用 `p`-adic root lifting 求 valuation maxima

由 (1)-(2)，可能的整数中心只需考虑

\[
10^{k-1}\le N_0\le10^k.
\tag{6}
\]

固定 `(k,z,w)` 后，写

\[
a_1=N_0+A_{k,z,w},
\qquad B_{k,z,w}=a_2b_1.
\]

则

\[
N=(N_0+A_{k,z,w})^2+B_{k,z,w}^2.
\tag{7}
\]

要找

\[
M_p(k,z,w)=\max_{N_0\text{ satisfying }(6)}v_p(N),
\qquad p\in\{2,5\},
\]

无需枚举 `9*10^(k-1)` 个整数中心。

从模 `p` 的根开始，把每个根 `r mod p^e` 提升为

\[
r+d p^e,\qquad d=0,\ldots,p-1,
\]

只保留满足

\[
N(r)\equiv0\pmod{p^{e+1}}
\]

且对应同余类与区间 (6) 有交的 lift。若某一级再无 lift，则前一级就是精确最大 valuation。

这是有限、精确的整数运算，并且复杂度只随实际 valuation 深度增长，而不随 prefix 区间长度指数增长。

定义六类型上的统一下界

\[
\underline x_*(k)
:=\min_{z,w,N_0}x_*,
\]

\[
\underline y_*(k)
:=\min_{z,w,N_0}y_*.
\tag{8}
\]

由 root-lifting 得到的 `M_2,M_5` 可精确计算这两个整数。

---

## 3. cross-corridor 自动给出两个全局禁象限

因为 `underline x_*`、`underline y_*` 不大于任何具体 prefix 的 `x_*,y_*`，由 (4)-(5) 立即得到安全的全局结论：

\[
\boxed{
x>k,\ y<\underline y_*(k)\Longrightarrow\bot,
}
\tag{9}
\]

\[
\boxed{
y>k,\ x<\underline x_*(k)\Longrightarrow\bot.
}
\tag{10}
\]

这两条已经足够把无界指数平面压成有限盒。

---

## 4. finite `h` supply + decade 给出显式有限 `(x,y)` box

令

\[
H_k:=\max_{w,h\in\mathcal H_{k,w}}h.
\]

### `x` 上界

若 `x>k`，由 (9) 必有

\[
y\ge\underline y_*(k).
\]

又 `h>=1`，故由 (1)

\[
2^x5^{\underline y_*(k)}<10^k.
\]

这给一个显式有限上界 `x<=X_max(k)`。

### `x` 下界

若 `x<underline x_*(k)`，由 (10) 必有 `y<=k`。于是

\[
10^{k-1}\le H_k2^x5^k,
\]

给出有限下界 `x>=X_min(k)`。

### `y` 上界

若 `y>k`，由 (10) 有 `x>=underline x_*(k)`，所以

\[
2^{\underline x_*(k)}5^y<10^k,
\]

得到 `y<=Y_max(k)`。

### `y` 下界

若 `y<underline y_*(k)`，由 (9) 的允许区形式有 `x<=k`，故

\[
10^{k-1}\le H_k2^k5^y,
\]

得到 `y>=Y_min(k)`。

因此对每个固定 `k>=6`：

\[
\boxed{
X_{\min}(k)\le x\le X_{\max}(k),
\qquad
Y_{\min}(k)\le y\le Y_{\max}(k).
}
\tag{11}
\]

这个盒与 `ell` 完全无关。

所以原先的第三尾无界问题已经严格转化为：

1. 有限 `h` supply；
2. 有限 `(x,y)` box；
3. exact rational `rho=h2^x5^y`；
4. decade (1)；
5. one-sided gap (2)。

---

## 5. `k=6..23` 的精确 certificate

`check_a1_top_diag_uniform_layers.py` 对每个 `k`：

1. 精确 factor `b_1,Q` 并构造完整 `H_{k,w}`；
2. 用 root lifting 求六类型的 exact `v_2(N),v_5(N)` maxima；
3. 推出 `underline x_*,underline y_*` 与 theorem-derived exponent box；
4. 只枚举落入 decade 的 exact rational states；
5. 检查 (2)。

结果如下。`H counts` 按 `w=1,2,3,4` 排列。

| `k` | `H counts` | `x* floor` | `y* floor` | exponent box `(xmin,xmax;ymin,ymax)` | decade states | gap hits |
|---:|---|---:|---:|---|---:|---:|
| 6 | `(64,32,2,8)` | -8 | -15 | `(-77,54;-29,12)` | 8,679 | 0 |
| 7 | `(128,12,128,32)` | -9 | -19 | `(-81,67;-31,13)` | 27,644 | 0 |
| 8 | `(128,24,16,256)` | -10 | -22 | `(-111,77;-43,15)` | 46,489 | 0 |
| 9 | `(16,192,32,8)` | -11 | -23 | `(-112,83;-43,17)` | 29,096 | 0 |
| 10 | `(128,24,32,24)` | -12 | -25 | `(-132,91;-51,19)` | 26,685 | 0 |
| 11 | `(32,48,48,8)` | -13 | -28 | `(-122,101;-46,21)` | 18,958 | 0 |
| 12 | `(3072,96,4,32)` | -14 | -32 | `(-157,114;-60,23)` | 497,994 | 0 |
| 13 | `(256,192,512,16)` | -15 | -32 | `(-173,117;-67,25)` | 161,213 | 0 |
| 14 | `(256,96,128,16)` | -16 | -36 | `(-178,130;-68,26)` | 86,637 | 0 |
| 15 | `(64,128,16,32)` | -17 | -39 | `(-194,140;-75,28)` | 45,800 | 0 |
| 16 | `(32,48,128,32)` | -18 | -41 | `(-209,148;-81,30)` | 50,952 | 0 |
| 17 | `(128,24,64,256)` | -19 | -43 | `(-218,156;-84,32)` | 103,730 | 0 |
| 18 | `(4096,20,32,128)` | -20 | -44 | `(-230,161;-89,34)` | 944,083 | 0 |
| 19 | `(1024,384,16,8)` | -21 | -49 | `(-237,176;-91,36)` | 335,288 | 0 |
| 20 | `(32,48,64,64)` | -22 | -50 | `(-255,182;-98,38)` | 54,299 | 0 |
| 21 | `(1024,32,256,64)` | -23 | -54 | `(-247,195;-94,39)` | 366,660 | 0 |
| 22 | `(4096,192,32,256)` | -24 | -55 | `(-280,200;-108,41)` | 1,225,045 | 0 |
| 23 | `(128,96,128,256)` | -25 | -58 | `(-292,211;-112,43)` | 177,478 | 0 |

因此严格得到

\[
\boxed{
6\le k=g\le23
\Longrightarrow
\text{minimal diagonal empty}.
}
\tag{12}
\]

结合旧 `k=1..5` certificates：

\[
\boxed{
1\le k=g\le23
\Longrightarrow
\text{minimal diagonal empty}.
}
\tag{13}
\]

---

## 6. 新的无界前沿

minimal diagonal 当前真正的首个未关闭层已经推进到

\[
\boxed{k=g\ge24.}
\]

更重要的是，未来固定层已经不需要枚举 `ell`、`j` 或完整 prefix box。计算规模由 `H_{k,w}` 的 divisor supply 和一个线性尺度的 exponent box 决定。

`k=6..23` 的数据还显示一个明显现象：允许 states 到最近整数的归一化距离

\[
10^k(\lceil\rho\rceil-\rho)
\]

在理论目标窗口 `[5.09,50.45]` 附近形成稳定空带。把这个“gap desert”提升成 `k`-uniform 的算术命题，是下一步比继续增加有限层更值得优先尝试的方向。

---

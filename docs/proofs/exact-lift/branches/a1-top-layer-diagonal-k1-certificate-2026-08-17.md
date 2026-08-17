# A1 top-layer diagonal `k=g=1` finite certificate — 2026-08-17

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
uv run python scripts/check_a1_top_diag_k1.py --jobs 4
```

状态：**有限证书**。

---

## 1. 完备 prefix box

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

## 2. 第三尾有限盒

后续 tail 证书与
[`a1-top-layer-diagonal-k2-certificate-2026-08-17.md`](a1-top-layer-diagonal-k2-certificate-2026-08-17.md)
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

## 3. 精确结果

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

## 4. 对无界 diagonal 的意义

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

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

# A1 top-layer diagonal `k=g=2` finite certificate — 2026-08-17

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
uv run python scripts/check_a1_top_diag_k2.py --jobs 4
```

脚本只使用整数、`fractions.Fraction`、整数平方根与 `sympy.factorint`；没有浮点判等或数值容差。

状态：**有限证书**。它关闭的是明确有界的 `k=g=2,r=s=1,d=2` 切片，不代表整个 A1 或整个 diagonal 已关闭。

---

## 1. 前缀集合为什么是完备的

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

`a1-top-layer-diagonal-significand-lock-2026-08-17.md` 已严格证明

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

## 2. 每个第三分母的非 `2,5` 部分都有完备有限来源

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

## 3. 用 `(x,y)` 参数化全部 `2/5` 尾状态

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

## 4. 为什么 `(x,y)` 的枚举盒覆盖全部整数点

前序文件
`a1-cross-corridor-primitive-collapse-2026-08-16.md`
已经证明：

### `2+5-` cross corridor

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

### `2-5+` cross corridor

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

## 5. partial-data rational-contact square sieve 是完备必要条件

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

这正是 `a1-discriminant-square-audit-2026-08-17.md` 中保留的合法用途：

- 在完整 exact candidate 上不能把 square property 重复算成额外方程；
- 在这里只固定 partial data `(P,S,theta)`、尚未恢复 `r_3`，所以它是完备的必要筛选器。

脚本把 `Xi` 写成 `Fraction`，分别对分子、分母做整数平方根测试。

没有模素数近似，也没有浮点平方判断。

---

## 6. 若平方通过，脚本仍会完整恢复并复核原式

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

## 7. 精确计算结果

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

## 8. 脚本的预期终端摘要

运行

```bash
uv run python scripts/check_a1_top_diag_k2.py --jobs 4
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

## 9. 严格证明边界

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

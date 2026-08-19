# `A_1`-only 分支

这是 `A_1` 分支的唯一规范编辑入口。内容按“统一框架 → moving-prefix/top layer → minimal diagonal”组织，避免把连续推进误读成互相独立的证明。

## 阅读顺序

1. [`core.md`](core.md)：原 §§28–31，以及 2026-08-16/17 的分支状态和审计边界。
2. [`rational-contact.md`](rational-contact.md)：rational-contact 主框架、safe integer-gap recovery、universal denominator funnel、resonance 和 cross-corridor 收缩。
3. [`top-layer.md`](top-layer.md)：moving-prefix 四层压缩、`d=2` endpoint/residue/half-gap kernel、positive excess decomposition 和 minimal-surplus 的 off-diagonal 分裂。
4. [`diagonal.md`](diagonal.md)：`k=g` minimal diagonal 的余量、2/5 valuation、奇素数供给、significand lock、`k=1,2` 有限证书和判别平方审计。
5. [`near-integer-tail.md`](near-integer-tail.md)：保留 `10^{-k}` 的二阶误差，把 `rho=b_3/10^ell` 压到整数 `j-10^k+1` 的 `O(10^{-k})` 邻域。
6. [`positive-tail-residual.md`](positive-tail-residual.md)：补回正曲率供给，严格得到
   \[
   5.09\,10^{-k}<j-10^k-\rho+1<50.45\,10^{-k}.
   \]
   因此 saturated sector 在 `k>=3` 全部为空，`ell<=k-2` 也全部为空。
7. [`boundary-residual-2adic.md`](boundary-residual-2adic.md)：在第一 non-saturated boundary 上做模 `32/64` 的整数平方核压缩。
8. [`boundary-prime-sieve.md`](boundary-prime-sieve.md)：把 denominator prime supply 改写成 residual/prefix 的禁同余类。
9. [`boundary-decimal-supply.md`](boundary-decimal-supply.md)：把第一 boundary 反向化成 finite `h` supply + decimal congruence。
10. [`residual-shell-supply.md`](residual-shell-supply.md)：把 divisor-congruence reduction 推广到 regular residual shells。
11. [`k3-certificate.md`](k3-certificate.md)：完整关闭 `k=g=3`。
12. [`k4-k5-certificates.md`](k4-k5-certificates.md)：完整关闭 `k=g=4,5`。
13. [`k6-first-boundary-certificate.md`](k6-first-boundary-certificate.md)、[`k6-ell6-certificate.md`](k6-ell6-certificate.md)、[`k6-ell7-certificate.md`](k6-ell7-certificate.md)：早期逐 `ell` 推进 `k=6` 的局部证书；现已被统一证书覆盖。
14. [`k6-uniform-tail-certificate.md`](k6-uniform-tail-certificate.md)：首次完全消去第三块位数 `ell`，用 valuation maxima + cross-corridor + finite odd-prime supply 把整个 `k=6` 压成有限 `(h,x,y)` 盒，并得到 0 near-integer hits。
15. [`uniform-layer-finite-box.md`](uniform-layer-finite-box.md)：把 `k=6` 方法推广到任意固定 `k>=6`；用 `p`-adic root lifting 求 prefix valuation maxima，再构造 theorem-derived exponent box。精确证书已关闭 `k=6,...,23`。
16. [`short-tail-saturation.md`](short-tail-saturation.md)：保留 positive-sign theorem 之前的中间整数化记录；其中 saturated short-tail 已被后续结果完全取代。

## 当前状态

本分支仍为 `待证`，但 minimal diagonal 的有限层前沿已经大幅推进。

旧证书关闭

\[
k=g=1,2,3,4,5.
\]

新的 uniform fixed-layer certificate 又严格关闭

\[
\boxed{k=g=6,7,\ldots,23.}
\]

因此当前已严格得到

\[
\boxed{
1\le k=g\le23
\Longrightarrow
\text{minimal diagonal empty}.
}
\]

minimal diagonal 的首个未关闭层已经推进到

\[
\boxed{k=g\ge24.}
\]

### 单侧 near-integer 刚性

对全部 `k>=3`，写

\[
\rho=\frac{b_3}{10^\ell},
\qquad
N_0=j-10^k+1,
\]

则

\[
\boxed{
5.09\,10^{-k}
<N_0-\rho
<50.45\,10^{-k}.
}
\]

因此

\[
\rho<N_0,
\qquad
L>1,
\qquad
\ell\ge k-1.
\]

### 新的固定层统一策略

写

\[
\rho=h2^x5^y,
\qquad h\in\mathcal H_{k,w}.
\]

`h` 来自 finite odd-prime supply，与 `ell` 无关。

对固定 `k`，把

\[
N=(N_0+A)^2+B^2
\]

在 `N_0\in[10^{k-1},10^k]` 上做模 `2^e,5^e` root lifting，可以精确得到所有 prefix 的 `v_2(N),v_5(N)` maxima，而无需扫描整个 prefix 区间。

结合

\[
X_0=Y_0=k,
\]

以及 resonance/cross-corridor，得到两个全局禁象限，并进一步由

\[
10^{k-1}\le h2^x5^y<10^k
\]

推出一个与 `ell` 完全无关的有限 exponent box

\[
X_{\min}(k)\le x\le X_{\max}(k),
\qquad
Y_{\min}(k)\le y\le Y_{\max}(k).
\]

于是每个固定 `k` 的整个第三尾都一次性变成 finite exact rational search，不再需要逐 `ell` 推进。

`k=6..23` 的全部这些 finite boxes 中，one-sided near-integer window 的命中数均为 0。

### 下一步

当前最值得推进的方向已经从“继续机械增加 `ell` shell”变成两条：

1. 继续把 generic fixed-layer certificate 推到 `k>=24`，作为快速严格证书；
2. 更重要地，从 `k=6..23` 的数据中证明一个 `k`-uniform 的 **gap desert**：允许的 `rho=h2^x5^y` 到最近上方整数的归一化距离
   \[
   10^k(\lceil\rho\rceil-\rho)
   \]
   在目标区间
   \[
   5.09<\cdot<50.45
   \]
   附近持续为空。如果能把这个现象提升为统一算术定理，就有机会一次关闭全部 `k>=24` diagonal。

`d=1,0,-1` 等其他 A1 无界核心仍待处理。判别平方审计继续有效：完整 contact 系统中的平方恒等式不能重复当作独立障碍。

## 可复核脚本

分支专用脚本位于 [`scripts/exact-lift/a1-only/`](../../../../../scripts/exact-lift/a1-only/)。主要包括：

- `check_a1_top_diag_k1.py`、`check_a1_top_diag_k2.py`、`check_a1_top_diag_k3.py`：`k=1,2,3`；
- `check_a1_top_diag_k45.py`：`k=4,5`；
- `check_a1_top_diag_k6_boundary.py`、`check_a1_top_diag_k6_ell6.py`、`check_a1_top_diag_k6_ell7.py`：早期 `k=6` 局部 shell 证书；
- `check_a1_top_diag_k6_uniform_tail.py`：整个 `k=6` 的统一 tail 证书；
- `check_a1_top_diag_uniform_layers.py`：generic `k=6..23` fixed-layer certificate；
- `check_a1_near_integer_tail_constants.py`：精确有理数复核 near-integer 常数。
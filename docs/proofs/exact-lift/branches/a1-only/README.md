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
7. [`boundary-residual-2adic.md`](boundary-residual-2adic.md)：在 `k>=6, ell=k-1` 把整数平方核模 `32/64`；`w=2` 只剩 `t=3`，`w=4` 只剩 `t=1`。
8. [`boundary-prime-sieve.md`](boundary-prime-sieve.md)：把 denominator prime supply 改写成 `N_0` 的禁同余类；`11` 是六类型共同永久缺失素数，`w!=2` 还有 mod `3` sieve。
9. [`boundary-decimal-supply.md`](boundary-decimal-supply.md)：证明第一 boundary 可反向枚举有限 `h` supply，并用 `10^{k-1}/a_t | h+hat t` 唯一恢复 `N_0`。
10. [`residual-shell-supply.md`](residual-shell-supply.md)：把 divisor-congruence reduction 推广到所有满足 `v_2(t),v_5(t)<ell` 的 regular residual shells；特别地 `ell=k` 全层自动 regular。
11. [`k3-certificate.md`](k3-certificate.md)：完整关闭 `k=g=3`。
12. [`k4-k5-certificates.md`](k4-k5-certificates.md)：完整关闭 `k=g=4,5`。
13. [`k6-first-boundary-certificate.md`](k6-first-boundary-certificate.md)：关闭 `k=g=6, ell=5`，完整 finite `h` supply 的 decimal congruence 命中数为 `0`。
14. [`k6-ell6-certificate.md`](k6-ell6-certificate.md)：关闭 `k=g=6, ell=6`；`t=6,...,50` 的完整 regular shell supply 为 `0` 命中。
15. [`k6-ell7-certificate.md`](k6-ell7-certificate.md)：关闭 `k=g=6, ell=7`；451 个 regular residual 与三个 deep-2 residual `128,256,384` 分别做有限 supply / `h2^u` 恢复，全部 `0` 命中。
16. [`short-tail-saturation.md`](short-tail-saturation.md)：保留 positive-sign theorem 之前的中间整数化记录；其中 saturated short-tail 已被后续结果完全取代。

## 当前状态

本分支仍为 `待证`。minimal diagonal 已严格关闭

\[
\boxed{k=g\in\{1,2,3,4,5\}.}
\]

因此全局无界前沿仍为

\[
\boxed{k=g\ge6.}
\]

但当前首层 `k=6` 已经被沿第三尾继续推进。

对全部 `k>=3`，第三尾满足单侧 near-integer 刚性

\[
\boxed{
5.09\,10^{-k}
<j-10^k-\rho+1
<50.45\,10^{-k}.
}
\]

定义

\[
N_0=j-10^k+1,
\qquad
 t=(N_0-\rho)10^\ell
=N_0 10^\ell-b_3.
\]

则

\[
\boxed{t\in\mathbf Z_{>0}},
\]

\[
\boxed{5.09\,10^{\ell-k}<t<50.45\,10^{\ell-k},}
\]

并且

\[
\boxed{L>1,\qquad \ell\ge k-1.}
\]

regular residual 进一步满足

\[
\boxed{b_3=a_t h,}
\]

\[
\boxed{
\frac{10^\ell}{a_t}\mid h+\widehat t,
\qquad
N_0=\frac{a_t(h+\widehat t)}{10^\ell}.}
\]

所以大量长尾已经从旧 `(x,y)` lattice 变成有限 divisor-congruence problem；只有 `v_2(t)>=ell` 或 `v_5(t)>=ell` 的 deep residual 需要额外 cancellation 分析。

### `k=6` 当前状态

positive residual theorem 排除

\[
\ell\le4.
\]

三个 finite supply certificates 又依次排除

\[
\ell=5,6,7.
\]

因此任何尚存的 `k=g=6` candidate 都可以无条件假设

\[
\boxed{\ell\ge8.}
\]

下一层 `ell=8` 的 residual 窗为

\[
509<t<5045,
\]

即

\[
\boxed{t\in\{510,\ldots,5044\}.}
\]

下一步继续把这一层分成 regular 与 deep-2/5 residual。这里的关键进展已经很清楚：`k=6` 的尾长并没有形成新的无界二维格点，而是在逐层变成有限的 decimal-supply 证书。

`d=1,0,-1` 等其他 A1 无界核心仍待处理。判别平方审计继续有效：完整 contact 系统中的平方恒等式不能重复当作独立障碍。

## 可复核脚本

分支专用脚本位于 [`scripts/exact-lift/a1-only/`](../../../../../scripts/exact-lift/a1-only/)。其中：

- `check_a1_top_diag_k1.py`、`check_a1_top_diag_k2.py`、`check_a1_top_diag_k3.py` 给出 `k=1,2,3` 的完整证书；
- `check_a1_top_diag_k45.py` 同时复核 `k=4,5`；
- `check_a1_top_diag_k6_boundary.py` 复核 `k=6, ell=5`；
- `check_a1_top_diag_k6_ell6.py` 复核 `k=6, ell=6`；
- `check_a1_top_diag_k6_ell7.py` 复核 `k=6, ell=7`；
- `check_a1_near_integer_tail_constants.py` 用精确有理数复核 near-integer 常数。
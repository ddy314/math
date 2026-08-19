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
9. [`boundary-decimal-supply.md`](boundary-decimal-supply.md)：证明第一 boundary 可反向枚举有限 `h` supply，并用
   \[
   10^{k-1}/a_t\mid h+\widehat t
   \]
   唯一恢复 `N_0`。
10. [`residual-shell-supply.md`](residual-shell-supply.md)：把上述 divisor-congruence reduction 推广到所有满足 `v_2(t),v_5(t)<ell` 的 regular residual shells；特别地 `ell=k` 全层自动 regular。
11. [`k3-certificate.md`](k3-certificate.md)：完整关闭 `k=g=3`。
12. [`k4-k5-certificates.md`](k4-k5-certificates.md)：完整关闭 `k=g=4,5`。
13. [`k6-first-boundary-certificate.md`](k6-first-boundary-certificate.md)：对 `k=g=6, ell=5` 的完整 finite `h` supply 做 decimal congruence certificate，命中数为 `0`。
14. [`k6-ell6-certificate.md`](k6-ell6-certificate.md)：继续关闭 `k=g=6, ell=6`；`t=6,...,50` 的完整 regular shell supply 同样 `0` 命中。
15. [`short-tail-saturation.md`](short-tail-saturation.md)：保留 positive-sign theorem 之前的中间整数化记录；其中 saturated short-tail 已被后续结果完全取代。

## 当前状态

本分支仍为 `待证`。minimal diagonal 已严格关闭

\[
\boxed{k=g\in\{1,2,3,4,5\}.}
\]

因此全局无界前沿为

\[
\boxed{k=g\ge6.}
\]

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
\boxed{5.09\,10^{\ell-k}<t<50.45\,10^{\ell-k}.}
\]

并且

\[
\boxed{L>1,\qquad \ell\ge k-1.}
\]

第一 boundary 为

\[
\ell=k-1,
\qquad
t\in\{1,2,3,4,5\},
\]

且当前 `k>=6` 有

\[
\boxed{
w=2\Longrightarrow t=3,
\qquad
w=4\Longrightarrow t=1.}
\]

regular residual 进一步满足

\[
\boxed{
b_3=a_t h,}
\]

\[
\boxed{
\frac{10^\ell}{a_t}\mid h+\widehat t,
\qquad
N_0=\frac{a_t(h+\widehat t)}{10^\ell},
}
\]

所以大量长尾已经从 `(x,y)` lattice 变成有限 divisor-congruence problem。

### `k=6` 当前状态

positive residual theorem 排除

\[
\ell\le4.
\]

有限 supply 证书又排除

\[
\ell=5,6.
\]

因此 `k=g=6` 尚存候选可无条件假设

\[
\boxed{\ell\ge7.}
\]

`ell=7` 时

\[
50.9<t<504.5,
\]

即

\[
t\in\{51,\ldots,504\}.
\]

这一层大多数 residual 仍是 regular；只有少数满足 `v_2(t)>=7` 或 `v_5(t)>=7` 的 deep-2/5 residual 需要单独处理。下一步优先把 `ell=7` 分成 regular / deep-2/5 两块继续推进，而无需恢复旧的二维无限搜索。

`d=1,0,-1` 等其他 A1 无界核心仍待处理。判别平方审计继续有效：完整 contact 系统中的平方恒等式不能重复当作独立障碍。

## 可复核脚本

分支专用脚本位于 [`scripts/exact-lift/a1-only/`](../../../../../scripts/exact-lift/a1-only/)。其中：

- `check_a1_top_diag_k1.py`、`check_a1_top_diag_k2.py`、`check_a1_top_diag_k3.py` 给出 `k=1,2,3` 的完整证书；
- `check_a1_top_diag_k45.py` 同时复核 `k=4,5`；
- `check_a1_top_diag_k6_boundary.py` 复核 `k=6, ell=5` boundary；
- `check_a1_top_diag_k6_ell6.py` 复核 `k=6, ell=6` shell；
- `check_a1_near_integer_tail_constants.py` 用精确有理数复核 near-integer 常数。
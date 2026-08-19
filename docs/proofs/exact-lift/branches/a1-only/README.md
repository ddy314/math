# `A_1`-only 分支

这是 `A_1` 分支的唯一规范编辑入口。内容按“统一框架 → moving-prefix/top layer → minimal diagonal”组织。

## 阅读顺序

1. [`core.md`](core.md)：A1 主框架与审计边界。
2. [`rational-contact.md`](rational-contact.md)：rational-contact、integer-gap、universal denominator funnel、resonance、cross-corridor。
3. [`top-layer.md`](top-layer.md)：moving-prefix 四层压缩、`d=2` endpoint kernel、positive excess 与 minimal-surplus 分裂。
4. [`diagonal.md`](diagonal.md)：`k=g` minimal diagonal、valuation normal form、odd-prime supply、早期有限证书。
5. [`near-integer-tail.md`](near-integer-tail.md)：把 `rho=b_3/10^ell` 压到明确整数 `N_0=j-10^k+1` 的 `O(10^-k)` 邻域。
6. [`positive-tail-residual.md`](positive-tail-residual.md)：确定 gap 的正号，排除 saturated sector 与 `ell<=k-2`。
7. [`sharp-positive-tail-window.md`](sharp-positive-tail-window.md)：把统一窗口严格加强为
   \[
   \boxed{15.09\,10^{-k}<N_0-\rho<39.003\,10^{-k}.}
   \]
8. [`uniform-2adic-prefix.md`](uniform-2adic-prefix.md)：证明 `2`-进 prefix 不需要 root lifting；全局精确 floor 为
   \[
   \boxed{\underline x_*(k)=-k-2.}
   \]
9. [`gap-denominator-normal-form.md`](gap-denominator-normal-form.md)：按 reduced denominator 分裂 gap desert；central sector 只剩固定 `Gamma=16,...,39`，剩余无界性进入 deep-denominator sector。
10. [`central-gap-2adic.md`](central-gap-2adic.md)：central sector 的整数平方核模 `64/256`；把 `144` 个 type-gap 组合压成 `48` 个。
11. [`central-gap-sign-collapse.md`](central-gap-sign-collapse.md)：展开整数平方核最高阶项，统一排除其中 `18` 个负号组合；central core 只剩 `30` 个。
12. [`boundary-residual-2adic.md`](boundary-residual-2adic.md)、[`boundary-prime-sieve.md`](boundary-prime-sieve.md)、[`boundary-decimal-supply.md`](boundary-decimal-supply.md)、[`residual-shell-supply.md`](residual-shell-supply.md)：早期 residual-shell / decimal-supply 压缩。
13. [`k3-certificate.md`](k3-certificate.md)、[`k4-k5-certificates.md`](k4-k5-certificates.md)：关闭 `k=3,4,5`。
14. [`k6-first-boundary-certificate.md`](k6-first-boundary-certificate.md)、[`k6-ell6-certificate.md`](k6-ell6-certificate.md)、[`k6-ell7-certificate.md`](k6-ell7-certificate.md)：早期逐 `ell` 的 `k=6` 局部证书，现已被统一证书覆盖。
15. [`k6-uniform-tail-certificate.md`](k6-uniform-tail-certificate.md)：首次消去 `ell`，整个 `k=6` 一次性关闭。
16. [`uniform-layer-finite-box.md`](uniform-layer-finite-box.md)：generic fixed-`k` finite-box theorem；关闭 `k=6,...,23`。
17. [`k24-k25-uniform-certificates.md`](k24-k25-uniform-certificates.md)：继续关闭 `k=24,25`。
18. [`short-tail-saturation.md`](short-tail-saturation.md)：保留 positive-sign theorem 之前的中间记录；其 saturated 分支已被后续结果完全排除。

## 当前状态

A1 整体仍为 `待证`，但 minimal diagonal 已严格关闭

\[
\boxed{1\le k=g\le25.}
\]

因此首个未关闭 fixed layer 为

\[
\boxed{k=g\ge26.}
\]

### 统一 near-integer 输入

对全部 `k>=3`：

\[
\boxed{
15.09\,10^{-k}
<N_0-\rho
<39.003\,10^{-k}.}
\]

故

\[
\rho<N_0,
\qquad L>1,
\qquad \ell\ge k-1,
\]

且归一化 gap

\[
\Gamma_k:=10^k(N_0-\rho)
\]

必须满足

\[
\boxed{15.09<\Gamma_k<39.003.}
\]

### 2-adic prefix 已完全解析

对合法 prefix：

\[
w\text{ even}\Longrightarrow v_2(N)=0,
\]

\[
w\text{ odd}\Longrightarrow v_2(N)\le1.
\]

因此

\[
\boxed{\underline x_*(k)=-k-2}
\]

对所有 `k>=3` 都是闭式。fixed-layer certificate 今后只真正需要处理 `5`-adic valuation floor。

### reduced-denominator 分裂

写既约

\[
\rho=\frac nd,
\qquad d=2^a5^b,
\qquad r=N_0d-n.
\]

则

\[
\gcd(r,d)=1,
\qquad
\Gamma_k=\frac{10^k r}{d},
\]

以及

\[
\boxed{d>10^k/39.003.}
\]

若 `d|10^k`，则 `Gamma_k` 为整数，精确只有

\[
\boxed{\Gamma\in\{16,17,\ldots,39\}.}
\]

并且

\[
\boxed{x=-k+v_2(\Gamma),\qquad y=-k+v_5(\Gamma),}
\]

\[
\boxed{
2^{v_2(\Gamma)}5^{v_5(\Gamma)}h
=N_0 10^k-\Gamma.}
\]

若 `d` 不整除 `10^k`，则真正进入 deep sector：

\[
\boxed{a>k\quad\text{或}\quad b>k.}
\]

### central sector 已压到 30 个 type-gap 组合

最初 central sector 有六个 prefix 类型乘 24 个 gap：`144` 个组合。

`central-gap-2adic.md` 利用 representation-independent 整数平方核

\[
R=K-2(10^k\rho)Q\mathcal N
\]

模 `64/256`，把它压成 `48` 个：

- `(1,1),(1,3),(3,1)`：只剩偶数 `Gamma=16,18,...,38`；
- `(1,2),(3,2)`：只剩 `Gamma in {16,22,30,32,38}`；
- `(1,4)`：只剩 `Gamma in {24,26}`。

随后 `central-gap-sign-collapse.md` 写

\[
T=10^k,\qquad s=N_0/T\in[0.1,1]
\]

并展开

\[
R=10000F_{z,w,\Gamma}(s)T^{10}+O(T^9).
\]

低阶项有统一精确界，而 `T>=10^6` 时首项符号已支配。由此再杀掉 18 个组合，central core 当前只剩

\[
\boxed{30}
\]

个：

| `(z,w)` | remaining `Gamma` |
|---|---|
| `(1,1)` | `32,34,36,38` |
| `(1,3)` | `24,26,28,30,32,34,36,38` |
| `(3,1)` | `22,24,26,28,30,32,34,36,38` |
| `(1,2)` | `30,32,38` |
| `(3,2)` | `22,30,32,38` |
| `(1,4)` | `24,26` |

其中 `(3,1,Gamma=22)` 还必须满足

\[
\boxed{N_0<0.251\,10^k.}
\]

### fixed-layer 证书

`uniform-layer-finite-box.md` 已把每个固定 `k` 的整个第三尾压成 finite `(h,x,y)` box，与 `ell` 无关。当前严格关闭

\[
\boxed{k=6,7,\ldots,25.}
\]

其中最新两层：

- `k=24`：188712 decade states，旧宽 gap window 命中 `0`；
- `k=25`：796197 decade states，旧宽 gap window 命中 `0`。

结合 `k=1..5` 旧证书即得到 `1<=k<=25` 全部为空。

## 下一步

现在最值得推进的两个统一核心是：

1. **central 30-combination core**：在 `R>0` 且 2-adic 局部平方尚可的 30 个固定组合上，把
   \[
   c_\Gamma h=N_0 10^k-\Gamma,
   \qquad h=q s,
   \]
   与 `q|Q`、whole-block selector，以及完整平方条件联用；
2. **deep denominator sector**：利用 `a>k` 或 `b>k` 的方向性，与 typewise resonance/cross-corridor 尤其 even-`w` 的强 `x_*` threshold 联用。

如果这两块统一关闭，minimal diagonal 的全部 `k>=26` 会一次消失，无需继续逐层 factor certificate。

`d=1,0,-1` 等其他 A1 无界核心仍待处理。判别平方审计继续有效：完整 contact 系统中的平方恒等式不能重复当作独立障碍。

## 可复核脚本

分支专用脚本位于 [`scripts/exact-lift/a1-only/`](../../../../../scripts/exact-lift/a1-only/)。主要包括：

- `check_a1_top_diag_k1.py`、`check_a1_top_diag_k2.py`、`check_a1_top_diag_k3.py`；
- `check_a1_top_diag_k45.py`；
- `check_a1_top_diag_k6_uniform_tail.py`；
- `check_a1_top_diag_uniform_layers.py`：`k=6..23`；
- `check_a1_top_diag_uniform_layers_24_25.py`：`k=24,25`；
- `check_a1_near_integer_tail_constants.py`；
- `check_a1_sharp_positive_tail_constants.py`；
- `check_a1_central_gap_2adic.py`；
- `check_a1_central_gap_sign.py`。
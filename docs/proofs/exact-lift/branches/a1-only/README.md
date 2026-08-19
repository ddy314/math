# `A_1`-only 分支

这是 `A_1` 分支的唯一规范编辑入口。内容按“统一框架 → moving-prefix/top layer → minimal diagonal”组织。

## 阅读顺序

1. [`core.md`](core.md)：A1 主框架与审计边界。
2. [`rational-contact.md`](rational-contact.md)：rational-contact、integer-gap、universal denominator funnel、resonance、cross-corridor。
3. [`top-layer.md`](top-layer.md)：moving-prefix 四层压缩、`d=2` endpoint kernel、positive excess 与 minimal-surplus 分裂。
4. [`diagonal.md`](diagonal.md)：`k=g` minimal diagonal、valuation normal form、odd-prime supply、早期有限证书。
5. [`near-integer-tail.md`](near-integer-tail.md)：把 `rho=b_3/10^ell` 压到明确整数 `N_0=j-10^k+1` 的 `O(10^-k)` 邻域。
6. [`positive-tail-residual.md`](positive-tail-residual.md)：确定 gap 的正号，排除 saturated sector 与 `ell<=k-2`。
7. [`sharp-positive-tail-window.md`](sharp-positive-tail-window.md)：利用六类型互斥的曲率/`cw` 信息，把统一窗口严格加强为
   \[
   \boxed{15.09\,10^{-k}<N_0-\rho<39.003\,10^{-k}.}
   \]
8. [`uniform-2adic-prefix.md`](uniform-2adic-prefix.md)：证明 `2`-进 prefix 不需要 root lifting；全局精确 floor 为
   \[
   \boxed{\underline x_*(k)=-k-2.}
   \]
9. [`gap-denominator-normal-form.md`](gap-denominator-normal-form.md)：把 gap desert 按 reduced denominator 分裂；central sector 只剩固定 `Gamma=16,...,39` 这 24 个整数，剩余无界性全部进入 deep-denominator sector。
10. [`boundary-residual-2adic.md`](boundary-residual-2adic.md)、[`boundary-prime-sieve.md`](boundary-prime-sieve.md)、[`boundary-decimal-supply.md`](boundary-decimal-supply.md)、[`residual-shell-supply.md`](residual-shell-supply.md)：早期 residual-shell / decimal-supply 压缩。
11. [`k3-certificate.md`](k3-certificate.md)、[`k4-k5-certificates.md`](k4-k5-certificates.md)：关闭 `k=3,4,5`。
12. [`k6-first-boundary-certificate.md`](k6-first-boundary-certificate.md)、[`k6-ell6-certificate.md`](k6-ell6-certificate.md)、[`k6-ell7-certificate.md`](k6-ell7-certificate.md)：早期逐 `ell` 的 `k=6` 局部证书，现已被统一证书覆盖。
13. [`k6-uniform-tail-certificate.md`](k6-uniform-tail-certificate.md)：首次消去 `ell`，整个 `k=6` 一次性关闭。
14. [`uniform-layer-finite-box.md`](uniform-layer-finite-box.md)：generic fixed-`k` finite-box theorem；关闭 `k=6,...,23`。
15. [`k24-k25-uniform-certificates.md`](k24-k25-uniform-certificates.md)：继续关闭 `k=24,25`。
16. [`short-tail-saturation.md`](short-tail-saturation.md)：保留 positive-sign theorem 之前的中间记录；其 saturated 分支已被后续结果完全排除。

## 当前状态

A1 整体仍为 `待证`，但 minimal diagonal 已严格关闭

\[
\boxed{
1\le k=g\le25.
}
\]

因此首个未关闭 fixed layer 已推进到

\[
\boxed{k=g\ge26.}
\]

### 当前统一 near-integer 输入

对全部 `k>=3`，写

\[
\rho=\frac{b_3}{10^\ell},
\qquad
N_0=j-10^k+1,
\]

则现在有

\[
\boxed{
15.09\,10^{-k}
<N_0-\rho
<39.003\,10^{-k}.
}
\]

所以

\[
\rho<N_0,
\qquad
L>1,
\qquad
\ell\ge k-1.
\]

归一化 gap

\[
\Gamma_k:=10^k(N_0-\rho)
\]

必须满足

\[
\boxed{15.09<\Gamma_k<39.003.}
\]

### 2-adic 部分已完全解析

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

对所有 `k>=3` 都是显式闭式。generic fixed-layer certificate 今后只真正需要处理 `5`-adic valuation floor。

### reduced-denominator 分裂

写既约

\[
\rho=\frac nd,
\qquad d=2^a5^b,
\]

并令

\[
r=N_0d-n.
\]

则

\[
\gcd(r,d)=1,
\qquad
\Gamma_k=\frac{10^k r}{d}.
\]

sharp window 首先给出

\[
\boxed{d>10^k/39.003.}
\]

若 `d|10^k`，则 `Gamma_k` 必为整数，精确只剩

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
=N_0 10^k-\Gamma.
}
\]

所以 central-denominator sector 已彻底消掉自由 `(x,y)`；真正剩余的统一无界问题只有

\[
\boxed{a>k\quad\text{或}\quad b>k}
\]

的 deep-denominator sector。

### fixed-layer 证书

`uniform-layer-finite-box.md` 已把每个固定 `k` 的整个第三尾压成 finite `(h,x,y)` box，与 `ell` 无关。原证书关闭 `k=6..23`，最新扩展又关闭

\[
\boxed{k=24,25.}
\]

其中：

- `k=24`：`H counts=(256,256,32,64)`，box `(-298,216;-114,45)`，188712 decade states，gap hits `0`；
- `k=25`：`H counts=(2048,48,16,512)`，box `(-316,224;-122,47)`，796197 decade states，gap hits `0`。

这两个证书刻意检查旧的更宽窗口 `[5.09,50.45]`，因此对 sharpened `[15.09,39.003]` 是更强的有限排除。

## 下一步

现在不应优先继续机械 factor `k=26,27,...`。更值得推进的是统一 gap-desert 的两个子问题：

1. **central sector**：只剩 24 个固定 `Gamma=16,...,39`，把
   \[
   c_\Gamma h=N_0 10^k-\Gamma
   \]
   与 `h=q s`、`q|Q`、whole-block selector 联用，争取一次排除全部 `k`；
2. **deep sector**：利用 `a>k` 或 `b>k` 的方向性，与 typewise resonance/cross-corridor 尤其 even-`w` 的强 `x_*` threshold 联用。

如果这两块都能统一关闭，minimal diagonal 的全部 `k>=26` 就会一次消失，而无需继续逐层证书。

`d=1,0,-1` 等其他 A1 无界核心仍待处理。判别平方审计继续有效：完整 contact 系统中的平方恒等式不能重复当作独立障碍。

## 可复核脚本

分支专用脚本位于 [`scripts/exact-lift/a1-only/`](../../../../../scripts/exact-lift/a1-only/)。主要包括：

- `check_a1_top_diag_k1.py`、`check_a1_top_diag_k2.py`、`check_a1_top_diag_k3.py`；
- `check_a1_top_diag_k45.py`；
- `check_a1_top_diag_k6_uniform_tail.py`；
- `check_a1_top_diag_uniform_layers.py`：`k=6..23`；
- `check_a1_top_diag_uniform_layers_24_25.py`：`k=24,25`；
- `check_a1_near_integer_tail_constants.py`：旧 near-integer 常数审计；
- `check_a1_sharp_positive_tail_constants.py`：新 `[15.09,39.003]` 常数审计。
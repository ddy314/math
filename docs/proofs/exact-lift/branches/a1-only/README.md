# `A_1`-only 分支

这是 `A_1` 分支的唯一规范编辑入口。内容按“统一框架 → moving-prefix/top layer → minimal diagonal”组织，避免把连续推进误读成互相独立的证明。

## 阅读顺序

1. [`core.md`](core.md)：原 §§28–31，以及 2026-08-16/17 的分支状态和审计边界。
2. [`rational-contact.md`](rational-contact.md)：rational-contact 主框架、safe integer-gap recovery、universal denominator funnel、resonance 和 cross-corridor 收缩。
3. [`top-layer.md`](top-layer.md)：moving-prefix 四层压缩、`d=2` endpoint/residue/half-gap kernel、positive excess decomposition 和 minimal-surplus 的 off-diagonal 分裂。
4. [`diagonal.md`](diagonal.md)：`k=g` minimal diagonal 的余量、2/5 valuation、奇素数供给、significand lock、`k=1,2` 有限证书和判别平方审计。
5. [`near-integer-tail.md`](near-integer-tail.md)：在 `k=g\ge3` 保留 `10^{-k}` 的二阶误差，证明 `\rho=b_3/10^\ell` 被压到整数 `j-10^k+1` 的 `O(10^{-k})` 邻域；进一步得到第三分母 prefix/tail 分界处的 decimal collapse。
6. [`k3-certificate.md`](k3-certificate.md)：完整枚举 `k=g=3`；3170 个 prefixes 最终只剩 230 个 tail states，全部无法通过 partial-data rational-square 必要条件，因此该层为空。
7. [`k4-k5-certificates.md`](k4-k5-certificates.md)：使用未粗化的 k-dependent near-integer 窗继续关闭 `k=g=4,5`；两层分别只剩 297、465 个 tail states，平方命中均为 0。
8. [`short-tail-saturation.md`](short-tail-saturation.md)：把 near-integer 误差乘回 `10^\ell` 后整数化；证明 `\ell\le k-2` 全部强制进入 saturated `10^\ell\mid b_3` 分支，non-saturated 必有 `\ell\ge k-1`，且边界 `\ell=k-1` 只剩六个非零 residual 与六个显式 `(x,y)` patterns。

## 当前状态

本分支仍为 `待证`。全局四层定理、`d=2` 的 endpoint kernel 等均按各自范围成立；minimal diagonal 已严格关闭

\[
\boxed{k=g\in\{1,2,3,4,5\}.}
\]

因此其无界前沿已经推进到

\[
\boxed{k=g\ge6.}
\]

对全部 `k\ge3`，第三尾满足 near-integer 刚性

\[
-17.425\,10^{-k}
<j-10^k-\rho+1
<50.45\,10^{-k}.
\]

同时第三块位数已经出现结构性分裂：

\[
\boxed{
\ell\le k-2\Longrightarrow L=1,
\qquad
L>1\Longrightarrow\ell\ge k-1.
}
\]

在第一条 non-saturated 边界 `\ell=k-1` 上只剩 `t\in\{-1,1,2,3,4,5\}` 六个 residual。下一阶段的重点已经很明确：从 `k=3,4,5` 的零平方证书中抽取一个 prefix-uniform 的 near-integer S-unit / rational-square 矛盾，避免继续机械增加有限层；并分别处理 saturated short-tail、`\ell=k-1` 六模式和 `\ell\ge k` genuinely-long tail。`d=1,0,-1` 等无界核心仍待处理。

判别平方审计继续有效：完整 contact 系统中的平方恒等式不能重复当作独立障碍。

## 可复核脚本

分支专用脚本位于 [`scripts/exact-lift/a1-only/`](../../../../../scripts/exact-lift/a1-only/)。其中：

- `check_a1_top_diag_k1.py`、`check_a1_top_diag_k2.py`、`check_a1_top_diag_k3.py` 给出 `k=1,2,3` 的完整证书；
- `check_a1_top_diag_k45.py` 同时复核 `k=4,5` 两层；
- `check_a1_near_integer_tail_constants.py` 只用精确有理数复核 near-integer lemma 中的安全十进制常数。

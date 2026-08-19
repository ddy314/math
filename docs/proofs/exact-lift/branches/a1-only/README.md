# `A_1`-only 分支

这是 `A_1` 分支的唯一规范编辑入口。内容按“统一框架 → moving-prefix/top layer → minimal diagonal”组织，避免把连续推进误读成互相独立的证明。

## 阅读顺序

1. [`core.md`](core.md)：原 §§28–31，以及 2026-08-16/17 的分支状态和审计边界。
2. [`rational-contact.md`](rational-contact.md)：rational-contact 主框架、safe integer-gap recovery、universal denominator funnel、resonance 和 cross-corridor 收缩。
3. [`top-layer.md`](top-layer.md)：moving-prefix 四层压缩、`d=2` endpoint/residue/half-gap kernel、positive excess decomposition 和 minimal-surplus 的 off-diagonal 分裂。
4. [`diagonal.md`](diagonal.md)：`k=g` minimal diagonal 的余量、2/5 valuation、奇素数供给、significand lock、`k=1,2` 有限证书和判别平方审计。
5. [`near-integer-tail.md`](near-integer-tail.md)：保留 `10^{-k}` 的二阶误差，把 `rho=b_3/10^ell` 压到整数 `j-10^k+1` 的 `O(10^{-k})` 邻域。
6. [`positive-tail-residual.md`](positive-tail-residual.md)：补回被旧估计丢弃的正曲率供给，严格确定 near-integer residual 的符号：
   \[
   5.09\,10^{-k}<j-10^k-\rho+1<50.45\,10^{-k}.
   \]
   由此 saturated sector 在 `k>=3` 全部为空，`ell<=k-2` 全部为空，且 `ell=k-1` 只剩 `t=1,2,3,4,5`。
7. [`boundary-residual-2adic.md`](boundary-residual-2adic.md)：在当前前沿 `k>=6, ell=k-1` 上把整数平方核模 `32/64`；`w=2` 只剩 `t=3`，`w=4` 只剩 `t=1`，奇 `w` 的奇 residual 强迫 `N_0` 偶。
8. [`k3-certificate.md`](k3-certificate.md)：完整枚举 `k=g=3`；3170 个 prefixes 最终只剩 230 个 tail states，全部无法通过 partial-data rational-square 必要条件，因此该层为空。
9. [`k4-k5-certificates.md`](k4-k5-certificates.md)：使用 k-dependent near-integer 窗继续关闭 `k=g=4,5`；两层分别只剩 297、465 个 tail states，平方命中均为 0。
10. [`short-tail-saturation.md`](short-tail-saturation.md)：记录 positive-sign theorem 之前得到的中间整数化步骤。其“short tail 进入 saturated”结论已被 `positive-tail-residual.md` 严格加强为“short tail 为空”。

## 当前状态

本分支仍为 `待证`。全局四层定理、`d=2` 的 endpoint kernel 等均按各自范围成立；minimal diagonal 已严格关闭

\[
\boxed{k=g\in\{1,2,3,4,5\}.}
\]

因此无界前沿为

\[
\boxed{k=g\ge6.}
\]

对全部 `k>=3`，第三尾现在满足更强的**单侧 near-integer 刚性**

\[
\boxed{
5.09\,10^{-k}
<j-10^k-\rho+1
<50.45\,10^{-k}.
}
\]

所以

\[
\boxed{
rho<j-10^k+1,
\qquad
L>1,
\qquad
\ell\ge k-1.
}
\]

此前需要单独研究的 saturated short-tail 已经整个消失。定义

\[
t=(j-10^k+1)10^\ell-b_3\in\mathbf Z,
\]

则

\[
5.09\,10^{\ell-k}<t<50.45\,10^{\ell-k}.
\]

第一条可能的尾长边界因此精确为

\[
\boxed{
\ell=k-1,
\qquad
t\in\{1,2,3,4,5\}.
}
\]

在当前 `k>=6` 前沿，二进平方核进一步给出：

\[
\boxed{
w=2\Longrightarrow t=3,
\qquad
w=4\Longrightarrow t=1.}
\]

其中

\[
(z,w)=(1,2):\ N_0\equiv0,2\pmod8,
\]

\[
(z,w)=(3,2):\ N_0\equiv4,6\pmod8.
\]

对奇 `w`，`t=1,3,5` 时必须 `N_0` 为偶数。

所以 minimal diagonal 当前真正剩余的结构已经分成两块：

1. `ell=k-1` 的五 residual boundary，其中 even-`w` 类型已几乎刚化；
2. `ell>=k` 的正 residual shells，例如 `ell=k` 时只有 `t=6,...,50`。

下一阶段优先把第一 boundary 的 fixed residual 与 denominator prime supply / whole-block selector 联用；这里已经没有原先的二维 `(x,y)` 无界自由度。随后再把同样的 residual 方法推广到 `ell>=k`。`d=1,0,-1` 等其他 A1 无界核心仍待处理。

判别平方审计继续有效：完整 contact 系统中的平方恒等式不能重复当作独立障碍。

## 可复核脚本

分支专用脚本位于 [`scripts/exact-lift/a1-only/`](../../../../../scripts/exact-lift/a1-only/)。其中：

- `check_a1_top_diag_k1.py`、`check_a1_top_diag_k2.py`、`check_a1_top_diag_k3.py` 给出 `k=1,2,3` 的完整证书；
- `check_a1_top_diag_k45.py` 同时复核 `k=4,5` 两层；
- `check_a1_near_integer_tail_constants.py` 用精确有理数复核 near-integer lemma 中的安全十进制常数。
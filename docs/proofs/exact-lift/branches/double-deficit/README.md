# `double-deficit`（DD）分支

这是 DD 分支的唯一规范编辑入口。主干与 frontier 后续分开保存，但 frontier 的日期笔记已经合并成一个按依赖排列的文件，不再维护多个相互重叠的 frontier 副本。

## 阅读顺序

1. [`core.md`](core.md)：原 §§17–27 及 `# 27.33` 后续合并进展，包含 DD 的统一正规化、有限证书和全局未闭合核心。
2. [`frontier.md`](frontier.md)：从一般 projective/angular allocation 到假想 `6.308883577618...` frontier 的 rational contact、5-adic allocation、单通道/十进制 remainder、Good closure 和 slot-capacity 审计。
3. [`good-radius-excess.md`](good-radius-excess.md)：接续 full rational-contact Good 的最新 slot ledger，把 equal-depth excess 与 pure-radius 在 common-baseline normalization 后统一为 canonical `G_exc`，并记录 `Top-residue + alpha` 直接消元退回 numerator reconstruction 的 exact no-go。
4. [`good-axis-normalization.md`](good-axis-normalization.md)：进一步证明 `epsilon_p=max(v_p(alpha)-v_p(N_c),0)`，把 `H_R` 从 primitive excess reader 中删掉；构造 two-block Gaussian carrier、axis companion pair，并把同一 `G_exc` 写成 decimal numerator、axis companion 与 `N(Delta_1)` 三条 canonical gcd reader。

## 当前状态

DD 仍为 `待证`。主干中的相对界、Schmidt 的非有效渐近界和已关闭的有限切片都保持原状态；`frontier.md`、`good-radius-excess.md` 与 `good-axis-normalization.md` 的结论只在假想 frontier sequence 条件下成立，不能推出 DD 全局空性或有效绝对高度界。

full rational-contact frontier 中 Bad 主质量已经关闭；Good 的 radius 侧先压成

\[
G_{\rm rad}=G_{\rm base}G_{\rm exc},
\qquad
G_{\rm base}=\gcd(C_L^{\rm main},H_R,N_c),
\]

随后 primitive excess 又可用 axis-normalized quotient 写成

\[
C_N=\frac{C_L^{\rm main}}{(C_L^{\rm main},N_c)},
\qquad
A_N=\frac{\alpha}{(\alpha,N_c)},
\qquad
\boxed{G_{\rm exc}=(C_N,A_N)}.
\]

同一个 `G_exc` 还可由 axis companion tail 和 `N(Delta_1)` normalized tail 读取。真正尚待新的 digit-shell 输入控制的是这份 axis-normalized common support；genuine-Gaussian split-prime / digit-shell 主支仍未关闭。

## 可复核脚本

DD 的有限证书与机械恒等式脚本位于 [`scripts/exact-lift/double-deficit/`](../../../../../scripts/exact-lift/double-deficit/)。

- `check_dd_good_radius_excess.py`：检查 baseline/excess 赋值账本、slot separation 与 decimal-alpha exact identity。
- `check_dd_good_axis_normalization.py`：检查 `epsilon_p` 的 axis-normalized 赋值公式、`G_exc` gcd 深度、two-block/axis companion exact identities 与三重 tail reader 的机械账本。

这些脚本只认证正文声明的有限赋值逻辑与恒等式，不承担 DD emptiness 的证明。

# `double-deficit`（DD）分支

这是 DD 分支的唯一规范编辑入口。主干与 frontier 后续分开保存，但 frontier 的日期笔记已经合并成一个按依赖排列的文件，不再维护多个相互重叠的 frontier 副本。

## 阅读顺序

1. [`core.md`](core.md)：原 §§17–27 及 `# 27.33` 后续合并进展，包含 DD 的统一正规化、有限证书和全局未闭合核心。
2. [`frontier.md`](frontier.md)：从一般 projective/angular allocation 到假想 `6.308883577618...` frontier 的 rational contact、5-adic allocation、单通道/十进制 remainder、Good closure 和 slot-capacity 审计。
3. [`good-radius-excess.md`](good-radius-excess.md)：接续 full rational-contact Good 的最新 slot ledger，把 equal-depth excess 与 pure-radius 在 common-baseline normalization 后统一为 canonical `G_exc`，并记录 `Top-residue + alpha` 直接消元退回 numerator reconstruction 的 exact no-go。
4. [`good-axis-normalization.md`](good-axis-normalization.md)：证明 `epsilon_p=max(v_p(alpha)-v_p(N_c),0)`，把 `H_R` 从 primitive excess reader 中删掉；构造 two-block Gaussian carrier、axis companion pair，并把同一 `G_exc` 写成 decimal numerator、axis companion 与 `N(Delta_1)` 三条 canonical gcd reader。
5. [`good-excess-gcd-ladder.md`](good-excess-gcd-ladder.md)：把 axis-normalized excess 提升为 `C_N^k` ordinary-gcd ladder；第一层就是 `G_exc`，稳定层读取完整 supported tail，并把 residual 精确分成 mutually-exclusive denominator deficit / numerator overflow。该文件同时证明三条 reader 只是同一 tail 的不同坐标图，不能重复计费。
6. [`good-short-residue-audit.md`](good-short-residue-audit.md)：审计第二 short-residue 的最自然局部候选。`Top-residue` 的 main 投影退回完整 `C_L` carry residue；clean-source 的 `G_exc^2` square lift 与 hidden square 联立后精确退回 scaled `C_L N(Delta_1)`；axis/radius-digital 正交 companion 多出的 overlap 全部由旧 `(C_L,N_c)` baseline 支付。并把上一文件的 numerator overflow 再拆成 `axis-reuse × deep-overflow`。

## 当前状态

DD 仍为 `待证`。主干中的相对界、Schmidt 的非有效渐近界和已关闭的有限切片都保持原状态；上述 Good continuation 文件的结论只在假想 frontier sequence 条件下成立，不能推出 DD 全局空性或有效绝对高度界。

full rational-contact frontier 中 Bad 主质量已经关闭；Good 的 radius 侧先压成

\[
G_{\rm rad}=G_{\rm base}G_{\rm exc},
\qquad
G_{\rm base}=\gcd(C_L^{\rm main},H_R,N_c),
\]

随后 primitive excess 可用 axis-normalized quotient写成

\[
C_N=\frac{C_L^{\rm main}}{(C_L^{\rm main},N_c)},
\qquad
A_N=\frac{\alpha}{(\alpha,N_c)},
\qquad
\boxed{G_{\rm exc}=(C_N,A_N)}.
\]

令

\[
D_k=(C_N^k,A_N),
\]

可不预先枚举 primes 地恢复 `C_N` support 上完整 excess tail。最新审计进一步定义

\[
G_{\rm full}:=(C_L^{\rm main},A_N)
=G_{\rm exc}G_{\rm reuse},
\qquad
G_{\rm reuse}\mid(C_L^{\rm main},N_c),
\]

并把旧 overflow 精确分成

\[
R_{\rm over}=G_{\rm reuse}R_{\rm deep}.
\]

所以 `G_exc` 是 normalized numerator tail 中唯一仍面向 **unpaid** `C_N` depth 的第一层；`G_reuse` 只是旧 axis payer，`R_deep` 已超过整个 full `C_L` prime-power depth。

同时，本地最自然的第二 short-residue 路线已经三次精确退化：carry 投影回 full `C_L`、square clean-source 投影回 `N(Delta_1)`、orthogonal digital overlap 投影回 axis baseline。因此 full-rational Good 下一步应直接做已有 `QCRT + GCRT+` 唯一 `A_{12}` lift 的 **global digit-shell location / exclusion**；若仍只重构 carry/source algebra，则转向 genuine-Gaussian split-prime / digit-shell 主支。

## 可复核脚本

DD 的有限证书与机械恒等式脚本位于 [`scripts/exact-lift/double-deficit/`](../../../../../scripts/exact-lift/double-deficit/)。

- `check_dd_good_radius_excess.py`：检查 baseline/excess 赋值账本、slot separation 与 decimal-alpha exact identity。
- `check_dd_good_axis_normalization.py`：检查 `epsilon_p` 的 axis-normalized 赋值公式、`G_exc` gcd 深度、two-block/axis companion exact identities 与三重 tail reader 的机械账本。
- `check_dd_good_excess_gcd_ladder.py`：检查 `C_N^k` ladder、successive quotient、stable tail 与 deficit/overflow separation。
- `check_dd_good_short_residue_audit.py`：检查 nested `C_N/C` 赋值账本、`G_reuse` axis-baseline bound、overflow 二次分层、orthogonal dot identity 与 secondary-norm scaling collapse。

这些脚本只认证正文声明的有限赋值逻辑与恒等式，不承担 DD emptiness 的证明。

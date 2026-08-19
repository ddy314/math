# `double-deficit`（DD）分支

这是 DD 分支的唯一规范编辑入口。主干与 frontier 后续分开保存，但 frontier 的日期笔记已经合并成一个按依赖排列的文件，不再维护多个相互重叠的 frontier 副本。

## 阅读顺序

1. [`core.md`](core.md)：原 §§17–27 及 `# 27.33` 后续合并进展，包含 DD 的统一正规化、有限证书和全局未闭合核心。
2. [`frontier.md`](frontier.md)：从一般 projective/angular allocation 到假想 `6.308883577618...` frontier 的 rational contact、5-adic allocation、单通道/十进制 remainder、Good closure 和 slot-capacity 审计。
3. [`good-radius-excess.md`](good-radius-excess.md)：接续 full rational-contact Good 的 slot ledger，把 equal-depth excess 与 pure-radius 在 common-baseline normalization 后统一为 canonical `G_exc`，并记录 `Top-residue + alpha` 直接消元退回 numerator reconstruction 的 exact no-go。
4. [`good-axis-normalization.md`](good-axis-normalization.md)：证明 `epsilon_p=max(v_p(alpha)-v_p(N_c),0)`，把 `H_R` 从 primitive excess reader 中删掉；构造 two-block Gaussian carrier、axis companion pair，并把同一 `G_exc` 写成 decimal numerator、axis companion 与 `N(Delta_1)` 三条 canonical gcd reader。
5. [`good-excess-gcd-ladder.md`](good-excess-gcd-ladder.md)：把 axis-normalized excess 提升为 `C_N^k` ordinary-gcd ladder；第一层就是 `G_exc`，稳定层读取完整 supported tail，并把 residual 精确分成 mutually-exclusive denominator deficit / numerator overflow。该文件同时证明三条 reader 只是同一 tail 的不同坐标图，不能重复计费。
6. [`good-short-residue-audit.md`](good-short-residue-audit.md)：审计第二 short-residue 的最自然局部候选。`Top-residue` 的 main 投影退回完整 `C_L` carry residue；clean-source 的 `G_exc^2` square lift 与 hidden square 联立后精确退回 scaled `C_L N(Delta_1)`；axis/radius-digital 正交 companion 多出的 overlap 全部由旧 `(C_L,N_c)` baseline 支付。并把 numerator overflow 再拆成 `axis-reuse × deep-overflow`。
7. [`good-prefix-polarization.md`](good-prefix-polarization.md)：把现有 `QCRT + GCRT+` 的唯一 `A_12` lift定位到 leading numerator block `a_1`。证明 `(n_1,m_1,n_2,m_2)=(S,0,0,S)+o(S)`；`a_2` suffix 与 `b_1` 都只有 subexponential 规模，不能增加正线性 CRT 高度；两条大 period residues 可无损下推为 `a_1` residue。
8. [`good-prefix-crt-location-audit.md`](good-prefix-crt-location-audit.md)：审计唯一 `a_1` lift 的 natural representative。证明 `Prefix-QCRT` 精确退回 reconstruction + clean source，`Prefix-GCRT` 是同一 reconstruction 经 axis quotient 后的投影，并有 `-i Gamma H_G-H_Q=U q_c^2 L_clean`。因此 period independence 仍给 uniqueness，但现有 parents 本身不给独立 Archimedean location；full-rational Q/G parent algebra 的 location 路线降级。
9. [`genuine-discriminant-carrier.md`](genuine-discriminant-carrier.md)：切到 genuine-Gaussian branch。由统一判别平方构造不依赖 `A≡±b` 的第二个 square-depth Gaussian carrier
   \[
   (C_G^{\rm main})^2\mid W^2+\Omega^2,
   \qquad \Omega=Q(a_2b_1)(\kappa+G),
   \]
   并与原 `Pi_sph^2|y_2+i y_3` 比较 orientation，得到 `same/opp` 两个 square-depth rational cross determinants。
10. [`genuine-discriminant-cross-audit.md`](genuine-discriminant-cross-audit.md)：计算两个 Gaussian carriers 的实数 slope，得到 `Omega y_2/(W y_3)=10^{-9S+o(S)}`。因此 `same` zero case 在 sufficiently large frontier 上关闭，但两个 raw cross determinant 都由 `W y_3` 主导，没有 Archimedean cancellation；直接 small-determinant 高度路线降级。
11. [`genuine-denominator-cleared-carrier.md`](genuine-denominator-cleared-carrier.md)：把 ghost cross determinant 清回 original integers，得到
   \[
   C_{\rm same}^3\mid Q a_2^2b_1b_3(\kappa+G)-Wa_3b_2,
   \]
   \[
   C_{\rm opp}^3\mid Q a_2^2b_1b_3(\kappa+G)+Wa_3b_2.
   \]
   cube-depth 中一层是 shared-denominator baseline，剩余两层仍是 genuine unit-unit cancellation。下一对象因此变成 normalized digit carrier `Phi_sigma/C_sigma`。

## 当前状态

DD 仍为 `待证`。主干中的相对界、Schmidt 的非有效渐近界和已关闭的有限切片都保持原状态；上述 continuation 文件的结论只在假想 frontier sequence 条件下成立，不能推出 DD 全局空性或有效绝对高度界。

### full rational-contact Good

Bad 主质量已经关闭。Good 的 primitive excess 可写为

\[
C_N=\frac{C_L^{\rm main}}{(C_L^{\rm main},N_c)},
\qquad
A_N=\frac{\alpha}{(\alpha,N_c)},
\qquad
\boxed{G_{\rm exc}=(C_N,A_N)}.
\]

`C_N^k` gcd ladder恢复完整 excess tail；进一步

\[
G_{\rm full}:=(C_L^{\rm main},A_N)
=G_{\rm exc}G_{\rm reuse},
\qquad
G_{\rm reuse}\mid(C_L^{\rm main},N_c),
\]

\[
R_{\rm over}=G_{\rm reuse}R_{\rm deep}.
\]

所以 `G_exc` 是 normalized numerator tail 中唯一面向 unpaid `C_N` depth 的第一层。现有 local short-residue 候选分别精确退回 carry、`N(Delta_1)` 与 axis baseline。

prefix digit-shell 进一步极化为

\[
\boxed{(n_1,m_1,n_2,m_2)=(S,0,0,S)+o(S)}.
\]

`QCRT + GCRT+` 将 `a_1` 锁成至多一个 candidate，但 natural representatives 满足

\[
\boxed{-i\Gamma H_G-H_Q=Uq_c^2L_{\rm clean}},
\]

故当前 Q/G parent algebra 内部没有第二个 independent short representative。除非引入真正外部的 Archimedean digit theorem，full-rational Good 不再继续堆同一组 eliminants。

### genuine-Gaussian

对 genuine main core，统一判别平方给

\[
\boxed{(C_G^{\rm main})^2\mid W^2+\Omega^2},
\qquad
\Omega=Q(a_2b_1)(\kappa+G),
\]

从而得到 discriminant Gaussian orientation `Pi_disc`。与 sphere orientation 比较后：

\[
C_{\rm same}^2\mid\Omega y_2-Wy_3,
\qquad
C_{\rm opp}^2\mid\Omega y_2+Wy_3.
\]

实数侧

\[
\frac{\Omega y_2}{Wy_3}=10^{-9S+o(S)},
\]

所以 `same` 的 zero escape 已关闭，raw determinants 也已证明没有 Archimedean saving。

清除 ghost denominators 后得到 original-integer cube-depth carriers

\[
\boxed{
C_\sigma^3\mid
\Phi_\sigma,
\qquad
\Phi_\sigma
=Q a_2^2b_1b_3(\kappa+G)
\pm Wa_3b_2.
}
\]

其中一层 `C_sigma` 是显式 shared-denominator baseline；真正待利用的是

\[
\boxed{C_\sigma^2\mid \Phi_\sigma/C_\sigma}
\]

的 normalized square-depth cancellation。下一步应寻找 `Phi_sigma/C_sigma` 的 exact source/digit factorization；若无法剥出大已知 factor 将 cofactor 高度压到 `<2 log C_sigma`，这条 discriminant carrier也只能保留为 orientation reader。

## 可复核脚本

DD 的有限证书与机械恒等式脚本位于 [`scripts/exact-lift/double-deficit/`](../../../../../scripts/exact-lift/double-deficit/)。

- `check_dd_good_radius_excess.py`：检查 baseline/excess 赋值账本、slot separation 与 decimal-alpha exact identity。
- `check_dd_good_axis_normalization.py`：检查 `epsilon_p` axis-normalized 公式、`G_exc` gcd 深度、two-block/axis companion identities 与三重 tail reader。
- `check_dd_good_excess_gcd_ladder.py`：检查 `C_N^k` ladder、successive quotient、stable tail 与 deficit/overflow separation。
- `check_dd_good_short_residue_audit.py`：检查 nested `C_N/C` 账本、`G_reuse` axis-baseline bound、overflow 二次分层、orthogonal dot identity 与 secondary-norm scaling collapse。
- `check_dd_good_prefix_polarization.py`：检查 `A_12` block digit-count、suffix 到 leading block 的 affine residue pushdown，以及 `2z_*+1=1.617767155236...`。
- `check_dd_good_prefix_crt_location_audit.py`：检查 `Prefix-Q-exact`、Q parent equivalence 与 Q/G residual compatibility。
- `check_dd_genuine_discriminant_carrier.py`：检查 discriminant square approximation、判别式重排与 same/opp Gaussian cross combinations。
- `check_dd_genuine_discriminant_cross_audit.py`：检查 genuine carrier 的 leading-height ledger、frontier digit constants 与 `-9S` cross-ratio。
- `check_dd_genuine_denominator_cleared_carrier.py`：检查 ghost-to-digit clearing identity、cube-depth valuation ledger 与 digit carrier expansion。

这些脚本只认证正文声明的有限赋值逻辑、常数账本与恒等式，不承担 DD emptiness 的证明。

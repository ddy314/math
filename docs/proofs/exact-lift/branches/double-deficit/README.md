# `double-deficit`（DD）分支

本文件是 DD 的规范导航入口。DD 当前仍为 **待证**。旧 equality frontier、多个高层和 canonical double-resonant 子域已经严格关闭或显著压缩；更低的 post-tail / non-canonical dominant states 仍缺少 projective/gap、bottom/common-numerator 与 residual split-Gaussian payer 的统一高度控制。

外部 `dongxuelian2` 的 SGR-9 只在其 frozen top-DD hypotheses 下给出 5-adic quotient-overload 矛盾；本仓库没有把它升级成 `DD=empty`。见 [`../../integration-audit-2026-09-06.md`](../../integration-audit-2026-09-06.md)。

## 规范主线与账本

先读 [`core.md`](core.md) 和 [`frontier.md`](frontier.md)。细粒度历史/continuation 分别归并在 [`good-genuine-ledger.md`](good-genuine-ledger.md)、[`high-funnel-ledger.md`](high-funnel-ledger.md)、[`tail-allocation-ledger.md`](tail-allocation-ledger.md)。

2026-08-21/22 后续 standalone 文档含有尚未完全归并进三本 ledger 的独有推导，因此继续保留并在下方完整索引。文件名中的 `collapse/closure` 均只按其显式假设生效。

## 2026-08-21 Gaussian / z0 continuation

- [`dd-gaussian-deep-core-2026-08-21.md`](dd-gaussian-deep-core-2026-08-21.md)
- [`dd-gaussian-oriented-transversality-2026-08-21.md`](dd-gaussian-oriented-transversality-2026-08-21.md)
- [`dd-gaussian-overlap-stripped-2026-08-21.md`](dd-gaussian-overlap-stripped-2026-08-21.md)
- [`dd-third-excess-collapse-2026-08-21.md`](dd-third-excess-collapse-2026-08-21.md)
- [`dd-z0-charged-first-2026-08-21.md`](dd-z0-charged-first-2026-08-21.md)

## 2026-08-22 corrected terminal / neighborhood chain

- [`dd-corrected-carry-u-pairmax-crt-2026-08-22.md`](dd-corrected-carry-u-pairmax-crt-2026-08-22.md)
- [`dd-corrected-gap-fiber-pairmax-rational-reconstruction-2026-08-22.md`](dd-corrected-gap-fiber-pairmax-rational-reconstruction-2026-08-22.md)
- [`dd-corrected-hard-source-split-2026-08-22.md`](dd-corrected-hard-source-split-2026-08-22.md)
- [`dd-corrected-high-funnel-quantitative-defect-2026-08-22.md`](dd-corrected-high-funnel-quantitative-defect-2026-08-22.md)
- [`dd-corrected-high-funnel-schmidt-2026-08-22.md`](dd-corrected-high-funnel-schmidt-2026-08-22.md)
- [`dd-corrected-neighborhood-decimal-top-residue-2026-08-22.md`](dd-corrected-neighborhood-decimal-top-residue-2026-08-22.md)
- [`dd-corrected-neighborhood-gap-fiber-entropy-2026-08-22.md`](dd-corrected-neighborhood-gap-fiber-entropy-2026-08-22.md)
- [`dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md`](dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md)
- [`dd-corrected-neighborhood-square-source-crt-2026-08-22.md`](dd-corrected-neighborhood-square-source-crt-2026-08-22.md)
- [`dd-corrected-pairmax-short-suffix-reader-2026-08-22.md`](dd-corrected-pairmax-short-suffix-reader-2026-08-22.md)
- [`dd-corrected-schmidt-farey-slack-2026-08-22.md`](dd-corrected-schmidt-farey-slack-2026-08-22.md)
- [`dd-corrected-source-carry-epsilon-cancellation-2026-08-22.md`](dd-corrected-source-carry-epsilon-cancellation-2026-08-22.md)
- [`dd-corrected-source-carry-sigma-overlap-2026-08-22.md`](dd-corrected-source-carry-sigma-overlap-2026-08-22.md)
- [`dd-corrected-terminal-denominator-sunit-entropy-2026-08-22.md`](dd-corrected-terminal-denominator-sunit-entropy-2026-08-22.md)
- [`dd-corrected-terminal-digit-polarization-2026-08-22.md`](dd-corrected-terminal-digit-polarization-2026-08-22.md)
- [`dd-corrected-terminal-neighborhood-geometry-2026-08-22.md`](dd-corrected-terminal-neighborhood-geometry-2026-08-22.md)
- [`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)
- [`dd-corrected-terminal-rough-source-neighborhood-2026-08-22.md`](dd-corrected-terminal-rough-source-neighborhood-2026-08-22.md)
- [`dd-corrected-terminal-rough-source-sharp-2026-08-22.md`](dd-corrected-terminal-rough-source-sharp-2026-08-22.md)
- [`dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md`](dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md)

## 2026-09-06 denominator-side attack

- [`dd-corrected-denominator-product-lock-2026-09-06.md`](dd-corrected-denominator-product-lock-2026-09-06.md)
- [`dd-corrected-common-scale-ray-2026-09-06.md`](dd-corrected-common-scale-ray-2026-09-06.md)

第一步在 corrected canonical `t_2=1` terminal neighborhood 的显式范围

\[
\delta<\delta_{qZ}=0.075150109396892\ldots
\]

内，将 denominator concat、S-unit phase 与 long pair-max core 联立，证明

\[
2^HqZ\equiv5^Tb_1 10^{m_2}\pmod{v_2},
\qquad 0<qZ<v_2,
\]

从而 `qZ` 被 `v_2` 的 least residue **精确唯一恢复**。固定 `v_2,b_1` 与 valuation/exponent layer 后，`(q,Z)`、`v_1`、`U,Q,b_2,gamma,b_3` 全部只剩 divisor entropy / exact reconstruction；接上已有 numerator collapse 后，fixed-`v_2` 的完整 Exact-Lift candidate family 满足

\[
N_{\rm full}\mid v_2
\le10^{0.767009998555\,\delta S+o(S)}.
\]

第二步在更宽范围

\[
\delta<\delta_{\rm ray}=0.156961684731344\ldots
\]

内，把

\[
b_1=v_1\tau_1,
\qquad b_2=v_2\tau_2,
\qquad Q=Uq
\]

的 cofactor compatibility写成 modulo `U` 的 projective line。两个 cofactor candidates 强迫

\[
U\mid \tau_2\tau_1'-\tau_2'\tau_1,
\]

而 determinant height严格小于 `U`，故 fixed S-unit phase / `V=v_1v_2` factor split 中 `tau_2/tau_1` 至多一个。进一步 exact reconstruction给

\[
\boxed{
(b_1,b_2,b_3,q,\gamma)
=(\ell\bar b_1,\ell\bar b_2,\ell\bar b_3,
\ell\bar q,\ell^2\bar\gamma).}
\]

因此 rough `gamma` 的 movable part被降级为 common denominator scale，而不再是第二个独立 projective shape。candidate-specific denominator/S-unit entropy相应从 `sigma_S+R` sharpen 为

\[
\boxed{\sigma_S+R/2.}
\]

uniform `delta/lambda` 最坏系数暂时未改善，因为最坏方向现在集中到 Farey/projective slack `sigma_S`。在两条 theorem 的公共 neighborhood 内，上一结果所说的 `short decimal head b_1` 也进一步被识别为 common-scale coordinate；真正的 denominator projective residual只剩 Farey/S-unit phase与 `V` 的 divisor split。

这些结论仍不是 DD emptiness 或 strict slope gap。当前 terminal 主攻目标已经从 arbitrary `v_2/gamma` movement进一步收缩为 **scale-quotiented Farey/projective primitive shape exclusion**；rough common scale本身是 Exact-Lift 的齐次方向，不能再被当作独立几何 payer 重复收费。

## Frontier continuation

- [`dd-discriminant-root-dependency-audit-2026-08-22.md`](dd-discriminant-root-dependency-audit-2026-08-22.md)
- [`dd-frontier-a3-triple-crt-residual-2026-08-22.md`](dd-frontier-a3-triple-crt-residual-2026-08-22.md)
- [`dd-frontier-genuine-radius-pairmax-collapse-2026-08-22.md`](dd-frontier-genuine-radius-pairmax-collapse-2026-08-22.md)
- [`dd-frontier-good-digit-shell-local-closure-2026-08-22.md`](dd-frontier-good-digit-shell-local-closure-2026-08-22.md)
- [`dd-frontier-phase-normalized-secondary-norm-2026-08-22.md`](dd-frontier-phase-normalized-secondary-norm-2026-08-22.md)
- [`dd-frontier-projective-source-pairmax-polarization-2026-08-22.md`](dd-frontier-projective-source-pairmax-polarization-2026-08-22.md)
- [`dd-frontier-qz-complementary-collapse-2026-08-22.md`](dd-frontier-qz-complementary-collapse-2026-08-22.md)
- [`dd-frontier-secondary-quadratic-reciprocity-2026-08-22.md`](dd-frontier-secondary-quadratic-reciprocity-2026-08-22.md)
- [`dd-frontier-source-core-projective-denominator-2026-08-22.md`](dd-frontier-source-core-projective-denominator-2026-08-22.md)
- [`dd-frontier-source-gaussian-divisor-2026-08-22.md`](dd-frontier-source-gaussian-divisor-2026-08-22.md)
- [`dd-frontier-source-orientation-euclidean-quotient-2026-08-22.md`](dd-frontier-source-orientation-euclidean-quotient-2026-08-22.md)

## Additional post-tail / root continuation

- [`dd-gcd-normal-multiplicative-fminus-lower-2026-08-22.md`](dd-gcd-normal-multiplicative-fminus-lower-2026-08-22.md)
- [`dd-general-transfer-correction-2026-08-22.md`](dd-general-transfer-correction-2026-08-22.md)
- [`dd-good-digit-shell-rational-collapse-2026-08-22.md`](dd-good-digit-shell-rational-collapse-2026-08-22.md)
- [`dd-hard-source-determinant-gap-charge-2026-08-22.md`](dd-hard-source-determinant-gap-charge-2026-08-22.md)
- [`dd-tail-root-unit-hensel-collapse-2026-08-22.md`](dd-tail-root-unit-hensel-collapse-2026-08-22.md)
- [`dd-ultrahard-tail-root-sign-collapse-2026-08-22.md`](dd-ultrahard-tail-root-sign-collapse-2026-08-22.md)
- [`tail-rough-angular-coefficient-stripped.md`](tail-rough-angular-coefficient-stripped.md)
- [`tail-rough-z0-angular-only-collapse.md`](tail-rough-z0-angular-only-collapse.md)
- [`tail-rough-z0-two-sheet-collapse.md`](tail-rough-z0-two-sheet-collapse.md)

## 当前边界

现行 DD 已知的 equality/frontier/subsector 关闭结论必须保留作用域。2026-09-06 的 denominator-side attack 已把 corrected terminal 的一个显式 neighborhood 中 fixed phase/factor split 的 denominator data压成唯一 common-scale ray，并把 rough-`gamma` entropy从独立 projective freedom降级为 homogeneous scale；更小的 `delta<0.07515...` neighborhood 还具有 `qZ` ordinary product lock。当前 terminal 真正的 uniform worst case已向 scale-quotiented Farey/projective `sigma_S` sector集中。更低锥与 post-tail / non-canonical payer 的共同高度控制仍然开放；subexponential counting、单一 CRT phase、fixed-target Schmidt 或某个 local collapse 都不能单独推出 DD 全局为空。

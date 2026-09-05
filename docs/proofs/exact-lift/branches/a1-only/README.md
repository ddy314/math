# `A_1`-only 分支

本文件是 A1 的规范导航入口。A1 当前仍为 **待证**。已严格关闭 fixed layers `1<=k=g<=31`，central denominator 在 `k>=26` 时为空；因此尚存 minimal-diagonal candidate 必须满足 `k=g>=32` 并进入 deep denominator。后续工作又关闭了若干 minimal-diagonal / top-layer 子域，但不能据此把整个 A1 标记为空。

## 规范主线与账本

先读 [`core.md`](core.md)、[`rational-contact.md`](rational-contact.md)、[`top-layer.md`](top-layer.md)、[`diagonal.md`](diagonal.md)。细粒度来源归并在 [`boundary-and-tail-ledger.md`](boundary-and-tail-ledger.md)、[`central-denominator-ledger.md`](central-denominator-ledger.md)、[`deep-denominator-ledger.md`](deep-denominator-ledger.md)、[`finite-layer-certificates-ledger.md`](finite-layer-certificates-ledger.md)。

`global-*`、`deep-*`、`top-layer-*` 与 `w1-*` 文件是前一轮多分支整合后仍含独有推导的 standalone continuation，因此保留并在下方完整索引。文件名中的 `closure/collapse` 只作用于其显式 hypotheses。

## 全局 / minimal-diagonal continuation

- [`decimal-height-synchronization.md`](decimal-height-synchronization.md)
- [`global-squarefree-terminal.md`](global-squarefree-terminal.md)
- [`global-terminal-bridge.md`](global-terminal-bridge.md)
- [`minimal-diagonal-closure.md`](minimal-diagonal-closure.md)
- [`deep-hl-local-signature-count-correction.md`](deep-hl-local-signature-count-correction.md)

## Double-deep 2-high / W2 continuation

- [`deep-2high-coefficient-source-minima.md`](deep-2high-coefficient-source-minima.md)
- [`deep-2high-contact-shell-coupling.md`](deep-2high-contact-shell-coupling.md)
- [`deep-2high-contact-shell-full-sign.md`](deep-2high-contact-shell-full-sign.md)
- [`deep-2high-decimal-height-collapse.md`](deep-2high-decimal-height-collapse.md)
- [`deep-2high-dual-slot-inverse-lock.md`](deep-2high-dual-slot-inverse-lock.md)
- [`deep-2high-dual-slot-shell.md`](deep-2high-dual-slot-shell.md)
- [`deep-2high-normalized-complement-shell.md`](deep-2high-normalized-complement-shell.md)
- [`deep-w2-coefficient-source-conflict.md`](deep-w2-coefficient-source-conflict.md)
- [`deep-w2-periodic-source-envelope.md`](deep-w2-periodic-source-envelope.md)
- [`deep-w2-periodic-source-matching.md`](deep-w2-periodic-source-matching.md)

## Single-deep continuation

- [`deep-single2-decimal-height-collapse.md`](deep-single2-decimal-height-collapse.md)
- [`deep-single5-decimal-height-collapse.md`](deep-single5-decimal-height-collapse.md)
- [`deep-single5-lowedge-small-supply-collapse.md`](deep-single5-lowedge-small-supply-collapse.md)
- [`deep-single5-lowedge-sphere-lock.md`](deep-single5-lowedge-sphere-lock.md)
- [`deep-single5-topedge-2resonance-certificate.md`](deep-single5-topedge-2resonance-certificate.md)
- [`deep-single5-topedge-common-quotient.md`](deep-single5-topedge-common-quotient.md)
- [`deep-single5-topedge-contact-descaling.md`](deep-single5-topedge-contact-descaling.md)
- [`deep-single5-topedge-decimal-factor-pair.md`](deep-single5-topedge-decimal-factor-pair.md)
- [`deep-single5-topedge-finite-height.md`](deep-single5-topedge-finite-height.md)
- [`deep-single5-topedge-fullsign-lock.md`](deep-single5-topedge-fullsign-lock.md)
- [`deep-single5-topedge-geB-phase-certificate.md`](deep-single5-topedge-geB-phase-certificate.md)
- [`deep-single5-topedge-high5-phase-certificate.md`](deep-single5-topedge-high5-phase-certificate.md)
- [`deep-single5-topedge-odd-cancellation.md`](deep-single5-topedge-odd-cancellation.md)
- [`deep-single5-topedge-oriented-root-factors.md`](deep-single5-topedge-oriented-root-factors.md)
- [`deep-single5-topedge-rational-phase-shell.md`](deep-single5-topedge-rational-phase-shell.md)
- [`deep-single5-topedge-real-sign-orientation.md`](deep-single5-topedge-real-sign-orientation.md)
- [`deep-single5-topedge-root-selection.md`](deep-single5-topedge-root-selection.md)
- [`deep-single5-topedge-strictlow-phase-certificate.md`](deep-single5-topedge-strictlow-phase-certificate.md)
- [`deep-single5-topedge-supply-compression.md`](deep-single5-topedge-supply-compression.md)
- [`deep-single5-topedge-u2-collapse.md`](deep-single5-topedge-u2-collapse.md)
- [`deep-single5-topedge-ultrathin-gap.md`](deep-single5-topedge-ultrathin-gap.md)

## Top-layer continuation

- [`top-layer-final-corridor-certificate.md`](top-layer-final-corridor-certificate.md)
- [`top-layer-final-corridor-reduction.md`](top-layer-final-corridor-reduction.md)
- [`top-layer-inner-wedge-digit-lock.md`](top-layer-inner-wedge-digit-lock.md)
- [`top-layer-inner-wedge-mixed-collapse.md`](top-layer-inner-wedge-mixed-collapse.md)
- [`top-layer-inner-wedge-pure2-collapse.md`](top-layer-inner-wedge-pure2-collapse.md)
- [`top-layer-inner-wedge-pure5-collapse.md`](top-layer-inner-wedge-pure5-collapse.md)
- [`top-layer-inner-wedge-stable-closure.md`](top-layer-inner-wedge-stable-closure.md)
- [`top-layer-inner-wedge-uniform-phase.md`](top-layer-inner-wedge-uniform-phase.md)
- [`top-layer-k2g-closure.md`](top-layer-k2g-closure.md)
- [`top-layer-k2g-gap-smallL-collapse.md`](top-layer-k2g-gap-smallL-collapse.md)
- [`top-layer-k2g-prime-shape-collapse.md`](top-layer-k2g-prime-shape-collapse.md)
- [`top-layer-k2g-pure5-finite-collapse.md`](top-layer-k2g-pure5-finite-collapse.md)
- [`top-layer-k2g-pure5-odd-orientation.md`](top-layer-k2g-pure5-odd-orientation.md)
- [`top-layer-k2g-pure5-positive-root-orientation.md`](top-layer-k2g-pure5-positive-root-orientation.md)
- [`top-layer-k2g-pure5-real-phase-shell.md`](top-layer-k2g-pure5-real-phase-shell.md)
- [`top-layer-k2gm1-closure.md`](top-layer-k2gm1-closure.md)
- [`top-layer-k2gm1-mixed-collapse.md`](top-layer-k2gm1-mixed-collapse.md)
- [`top-layer-k2gm1-pure2-collapse.md`](top-layer-k2gm1-pure2-collapse.md)
- [`top-layer-k2gm1-pure5-collapse.md`](top-layer-k2gm1-pure5-collapse.md)
- [`top-layer-k2gm2-closure.md`](top-layer-k2gm2-closure.md)
- [`top-layer-k2gm2-mixed-collapse.md`](top-layer-k2gm2-mixed-collapse.md)
- [`top-layer-k2gm2-pure2-collapse.md`](top-layer-k2gm2-pure2-collapse.md)
- [`top-layer-k2gm2-pure5-collapse.md`](top-layer-k2gm2-pure5-collapse.md)
- [`top-layer-k2gm2-tail-center.md`](top-layer-k2gm2-tail-center.md)
- [`top-layer-k2gminus1-tail-center.md`](top-layer-k2gminus1-tail-center.md)
- [`top-layer-minimal-offdiagonal-J-compression.md`](top-layer-minimal-offdiagonal-J-compression.md)
- [`top-layer-minimal-offdiagonal-far-collapse.md`](top-layer-minimal-offdiagonal-far-collapse.md)
- [`top-layer-minimal-surplus-closure.md`](top-layer-minimal-surplus-closure.md)
- [`top-layer-post-minimal-surplus-frontier.md`](top-layer-post-minimal-surplus-frontier.md)
- [`top-layer-r1-joint-halfgap-collapse.md`](top-layer-r1-joint-halfgap-collapse.md)
- [`top-layer-s1-far-lowr-collapse.md`](top-layer-s1-far-lowr-collapse.md)
- [`top-layer-s1-far-radius-phase.md`](top-layer-s1-far-radius-phase.md)
- [`top-layer-uniform-offdiagonal-tail-center.md`](top-layer-uniform-offdiagonal-tail-center.md)

## W1 continuation

- [`w1-fixed-pair-descent.md`](w1-fixed-pair-descent.md)
- [`w1-global-complement-minimum.md`](w1-global-complement-minimum.md)

## 当前边界

A1 的历史 saturated `L=1` 支已经退出前沿。当前阅读时优先以 `k>=32` deep-denominator 与后续 standalone continuation 为准；任何有限 certificate、fixed pair descent 或 minimal-diagonal closure 都不能自动覆盖 moving-prefix / 非 minimal-diagonal 的完整 A1。

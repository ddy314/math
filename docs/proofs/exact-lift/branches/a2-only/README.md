# `A_2`-only 分支

本文件是 A2 的规范导航入口。A2 当前仍为 **待证**：大量 source / endpoint / Gaussian / CRT / fixed-prime 通道已经严格压缩或降级，但 `m_2>=11` 的 deep-even 无界核心及剩余 fixed-prime、prefix-gcd、sphere-height 通道尚未统一排除。

## 规范主线

推荐先读 [`core.md`](core.md)、[`phase-and-defect.md`](phase-and-defect.md)、[`hensel.md`](hensel.md)、[`endpoint-lattice.md`](endpoint-lattice.md)、[`prime-source.md`](prime-source.md)、[`primitive-reduction.md`](primitive-reduction.md)。五本细粒度账本为 [`auxiliary-reductions-ledger.md`](auxiliary-reductions-ledger.md)、[`source-angle-ledger.md`](source-angle-ledger.md)、[`crt-descent-ledger.md`](crt-descent-ledger.md)、[`height-ledger.md`](height-ledger.md)、[`fixed23-and-cq-ledger.md`](fixed23-and-cq-ledger.md)。

所有“collapse / closure”只按文件写明的 hypotheses 生效；它们不能仅凭文件名升级为 A2 全局空性。

## 独立 continuation manifest

以下文件保留独有的后续推导，因此继续作为顶层可审计节点；每个节点都必须从本 README 直接可达。

- [`additive-descendant-gcd-interface.md`](additive-descendant-gcd-interface.md)
- [`descendant-f-gd-bridge.md`](descendant-f-gd-bridge.md)
- [`endpoint-five-point-cofactors.md`](endpoint-five-point-cofactors.md)
- [`external-shared-outer-fixed-templates.md`](external-shared-outer-fixed-templates.md)
- [`external-shared-outer-nogo.md`](external-shared-outer-nogo.md)
- [`fixed-prime-asymmetric-lifts.md`](fixed-prime-asymmetric-lifts.md)
- [`fixed-prime-descendant-transversality.md`](fixed-prime-descendant-transversality.md)
- [`fixed-target-serial-dichotomy.md`](fixed-target-serial-dichotomy.md)
- [`fixed199-angle-residual.md`](fixed199-angle-residual.md)
- [`fixed3-exception-collapse.md`](fixed3-exception-collapse.md)
- [`fixed3-f-contact-orientation.md`](fixed3-f-contact-orientation.md)
- [`fixed3-terminal-spill.md`](fixed3-terminal-spill.md)
- [`outer-cofactor-reuse-gate.md`](outer-cofactor-reuse-gate.md)
- [`outer-descendant-additive-lock.md`](outer-descendant-additive-lock.md)
- [`outer-external-q4-root-split.md`](outer-external-q4-root-split.md)
- [`source-common-outer-fixed-exception.md`](source-common-outer-fixed-exception.md)
- [`target-common-parity-surcharge.md`](target-common-parity-surcharge.md)

## 当前边界

现有结果已经把许多看似独立的高阶 Hensel / quadratic-character / Gaussian-child 条件识别为既有 exact identities 的投影，后续不得重复收费。当前真正需要的新输入仍应同时控制 moving coefficient、真实 decimal window 与剩余 odd-prime/source channels；有限枚举、单个 fixed-prime closure 或局部 descendant transversality 均不能代替全局无界证明。

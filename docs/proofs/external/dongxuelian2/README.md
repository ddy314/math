# dongxuelian2 外部研究整合

来源：`dongxuelian2/three-term-decimal-concatenation-square-sum`，`master` 提交 `2cfa389f1d4ced90653101e6c92ee8dfe85b5535`（2026-08-27）。

本目录是**经过筛选的外部 corpus**。来源仓库的顶层 `STATUS.md` 本身仍声明全局问题 open；本仓库进一步按现行 Exact-Lift 分支重新审计。权威裁决见 [`../../exact-lift/integration-audit-2026-09-06.md`](../../exact-lift/integration-audit-2026-09-06.md)。

## 审计等级

### 可直接复用 / 已采纳语义

- [`foundations/theorem-index.md`](foundations/theorem-index.md)：T1–T18 与 scoped 分支定理索引；机器结果保持原证据等级。
- [`exact-lift/audit-response.md`](exact-lift/audit-response.md)：T10/T12/T18 补证，以及对 E1/E6 等程序覆盖缺口的降级。
- [`exact-lift/unified-exact-lift.md`](exact-lift/unified-exact-lift.md)：primitive-core 与 Exact-Lift 的结构耦合；不作为 closure。
- [`exact-lift/backward/canonical-dependency-skeleton.md`](exact-lift/backward/canonical-dependency-skeleton.md)：canonical recovery spine 与反重复依赖规则。
- [`exact-lift/backward/denominator-decimal-interface.md`](exact-lift/backward/denominator-decimal-interface.md)：segmented denominator word + effective tail scale 接口；其中 branch-free `kappa` 恒等式已纳入本仓库审计结论。
- [`a1/word-recovery-interface.md`](a1/word-recovery-interface.md)：从来源 post-DD / backward A1 稿中抽出的 A1-only 局部 word-gap 结构；不依赖 DD 全局为空。

### Scoped critical-G 结果

- [`templates/g/core/primitive-core-pr6.md`](templates/g/core/primitive-core-pr6.md)：PR6 结构 reduction，G 整体仍 open。
- [`templates/g/core/zero-remainder-closure-gd1.md`](templates/g/core/zero-remainder-closure-gd1.md)：只关闭 `T-Jb2=0` normal sublayer。
- [`templates/g/a1/unit-determinant-resolution-ga1.md`](templates/g/a1/unit-determinant-resolution-ga1.md)：来源 critical-G 的 `gamma=1,A1` 交分支。
- [`templates/g/a2/exceptional-binary-resolution-ge2.md`](templates/g/a2/exceptional-binary-resolution-ge2.md)：来源 critical-G 的异常二进室。
- [`templates/g/a2/low-phi-multiblock-galmb3.md`](templates/g/a2/low-phi-multiblock-galmb3.md)：低 `phi` 多块递归；移动模数问题仍 open。

这些 `A1/A2` 名称属于来源 critical-G 模板，不能按名字直接升级本仓库 Exact-Lift A1/A2 分支。

### DD 条件/历史工具

- [`denominator-structure/dd-post-deflation.md`](denominator-structure/dd-post-deflation.md)：post-deflation residual supply，作为结构中间件保留。
- [`denominator-structure/dd-supply-phase-audit.md`](denominator-structure/dd-supply-phase-audit.md)：证明 projected phase 是 endogenous 的负面知识，防止重复收费。
- [`denominator-structure/dd-orientation-recovery.md`](denominator-structure/dd-orientation-recovery.md)：只在来源冻结 top-DD 子域上的 orientation recovery。
- [`denominator-structure/dd-top-quotient-overload.md`](denominator-structure/dd-top-quotient-overload.md)：SGR-9 的 5-adic quotient-overload 条件矛盾；本仓库**不采纳其 `DD=empty` 全局外推**。

## 已清理的冗余导入

未保留来源的 broad 8 月 10 日 synthesis、早期 `initial-route`、来源 `status` 快照和 `post-DD-A1` 总稿。前两者与现有 archive/后期专题重复；状态快照会与本仓库权威状态混淆；post-DD 稿中可用的 A1 局部结构已抽入独立文件。

## 使用边界

任何 external 结论进入主分支前都必须重新证明其 hypotheses 覆盖本仓库当前分支状态。尤其禁止从“来源后期写着 CLOSED”推断本仓库同名分支已关闭。

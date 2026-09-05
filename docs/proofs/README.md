# 证明资料

本仓库的权威研究入口是 [三块十进制拼接 Exact Lift](exact-lift/README.md)。主不存在性命题仍未完成证明。

## 权威主线

`exact-lift/` 保存原问题、统一框架、三个异常分支、严格状态、依赖图和历史快照。日常判断证明状态时按以下顺序读取：

1. [`exact-lift/status.md`](exact-lift/status.md)；
2. 对应分支入口：[`A2`](exact-lift/branches/a2-only/README.md)、[`DD`](exact-lift/branches/double-deficit/README.md)、[`A1`](exact-lift/branches/a1-only/README.md)；
3. 规范专题与按依赖归并的 ledger；
4. [`exact-lift/integration-audit-2026-09-06.md`](exact-lift/integration-audit-2026-09-06.md) 记录外部成果进入主线前的最新审计。

`exact-lift/archive/` 只保存迁移前不可变快照，不作为新的编辑入口。

## 外部研究

[`external/`](external/README.md) 保存经过筛选的外部证明材料。外部目录中的 `source status` 只描述来源仓库自己的判断；本仓库是否采纳、降级或拒绝，由对应来源的审计索引决定。

当前已审计来源：[`dongxuelian2/three-term-decimal-concatenation-square-sum`](external/dongxuelian2/README.md)。

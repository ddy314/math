# 三块十进制拼接 Exact Lift

本目录是当前仓库的**权威主证明树**。原始 2026-08-10 总稿保存在 `archive/`；结构化文件和三个分支入口承载当前结论。

## 当前严格状态（2026-09-06）

主不存在性命题仍为 **待证**。三个异常分支均未被本仓库的现行依赖链全局关闭：

- **A2：待证。** `m_2>=11` 的 deep-even 无界核及剩余 fixed-`11,23` / prefix-gcd / sphere-height 通道尚未统一排除。
- **DD：待证。** equality frontier、若干高层和 canonical `t_2=1` double-resonant funnel 已大量收缩，但 post-tail / non-canonical dominant states 仍缺少统一的 simultaneous height bound。
- **A1：待证。** fixed layers `1<=k=g<=31` 与 central denominator 已关闭；任何尚存 minimal-diagonal candidate 必须进入 `k=g>=32` 的 deep denominator，当前核心是统一 `2`-high / `5`-low master branch。

外部来源 `dongxuelian2` 的 SGR-9 在其**冻结 top-DD 前提**下给出正确的 5-adic quotient-overload 矛盾；本仓库审计确认该旧覆盖链没有包含现行 DD 的全部低层/post-tail states，因此**不采纳 `DD=∅` 的全局升级**。完整裁决见 [2026-09-06 外部整合审计](integration-audit-2026-09-06.md)。

## 阅读顺序

1. [`problem-and-carrier.md`](problem-and-carrier.md)：原问题、正权平均与 A2/DD/A1 三分支穷尽。
2. [`global-framework.md`](global-framework.md)：整数球面、primitive recovery、统一尾正规化、判别式和 denominator prime graph。
3. [`status.md`](status.md)：权威严格状态、历史错误路线和当前优先级。
4. 分支入口：[`A2`](branches/a2-only/README.md)、[`DD`](branches/double-deficit/README.md)、[`A1`](branches/a1-only/README.md)。
5. [`dependency-map.md`](dependency-map.md) 与 [`conclusion.md`](conclusion.md)：跨分支依赖和当前结论。
6. [`integration-audit-2026-09-06.md`](integration-audit-2026-09-06.md)：外部成果与主线的作用域核对。

## 外部材料的使用规则

已筛选的外部成果位于 [`../external/dongxuelian2/`](../external/dongxuelian2/README.md)。其中可直接复用的内容包括 common-denominator canonicalization、denominator–decimal interface、若干 scoped critical-G 定理，以及 A1 backward word-gap 结构；它们只有在本审计明确写为“采纳”时才进入主线语义。

尤其禁止：把来源仓库的 `DD CLOSED`、`strict only A1`、有限证书或旧 strict-layer 覆盖表直接改写成本仓库的全局状态。

## 维护规则

新增结果遵循“命题 → 假设/作用域 → 推导或证书 → 依赖 → 状态 → 验证/开放缺口”。分支细节写入对应规范专题或 ledger，并同步分支 README；顶层 README 只保留导航和权威状态，避免再次膨胀成逐日研究流水账。

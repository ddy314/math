# 仓库研究规则

## 目标与事实边界

本仓库研究三块十进制拼接 Exact Lift。首要产物是可审计、连续的数学证明稿。主不存在性命题仍为待证；A2、DD、A1 三个完整分支未全部关闭。

依次读取 README.md、PROOF.md 的公共系统、相关分支及 RESEARCH.md 对应路线。CHECKS.md 说明计算覆盖。历史原文仅用来查来源，不承担现行导航或新的编辑位置。

## 唯一位置

- PROOF.md 是现行定义、引理、定理和证明的唯一正文。用稳定命题 ID，直接写完整假设和推导。
- RESEARCH.md 是未完成路线、允许见证、撤回论证和剩余系统的唯一记录。用稳定 route ID，不以日期命名新的数学笔记。
- registry/claims.json 登记命题的四种状态、依赖、scope、checks、来源范围。registry/checks.json 登记稳定核对入口。
- checks/common、checks/a2、checks/dd、checks/a1 保存现行核对代码。添加计算必须链接到具体命题或路线，解释是否覆盖无界参数。
- history/2026-10-01-sources.zip 原样保全迁移前 621 个文件；history/sources.json 保留每个文件及 ledger 记录的哈希。后续不得改写这份快照；历史错误在 RESEARCH.md 注明。

2026-10-01 的用户要求是整体重写和统一组织；旧分支 README、日期专题及巨型 ledger 路径已退出现行结构。不得重新生成它们。

## 状态与证明

仅使用：已严格完成、有限证书、待证、失效/降级。明确区分定理的完整作用域、必要条件、条件唯一性、精确有限计算、允许投影和猜想。

禁止以下外推：

- 固定前缀有限推出全部前缀的并集有限。
- 没有全局参数界的有限枚举推出无界为空。
- 渐近排除推出有效绝对 cutoff 或排除 finite exceptions。
- 同源 Hensel、norm、radius 或消元投影重复计入独立预算。
- Gaussian flip / Vieta root 未证明原 word cut、尺度、正性、既约和位数保持就成为合法下降。
- 结构检查或脚本 PASS 成为整分支关闭。

A2 必须保留 actual 减向 transport 和 fixed-3 8/12 更正。DD 必须使用非循环 joint count。A1 必须保留正确的 lambda·10^(−g)·r2 尺度；LK17G 撤回状态不变。

## 修改和验证

先检查 git status --short 与相关 diff，保留已有工作。不要提交环境、缓存、临时二进制、大规模输出。

Python 优先使用 uv，依赖保持 uv.lock 同步；新增依赖用 uv add。精确枚举可使用 C++，须说明整数宽度与独立检查。一次性实验放在 /tmp；通过审计的结果再接入主稿。

```bash
uv sync --locked
uv run python main.py check
uv run python main.py verify <对应核对ID>
uv run python -m unittest discover -s tests
git diff --check
```

新定理依次处理：明确命题和范围 → 完整证明 → 登记状态与依赖 → 接入对应路线 → 记录证书边界 → 运行相关验证。修改任何源摘要或来源映射须保留迁移证据。

不另开平行 agent，除非用户明确要求。交付说明实际改动、验证以及仍未证明的核心，不把重组说成新数学定理。

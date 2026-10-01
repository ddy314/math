# 不可变来源库

`2026-10-01-sources.zip` 是整体重写前的完整源码快照，包含 **621 个文件**；已逐文件核对 SHA-256。它包含 GitHub 同步后的内容及当时本地未提交的研究成果，不含 `.git`、`.venv`、缓存或计算产物。原有两份 archive 也保存在包内，字节未改。

现行证明唯一入口是 [PROOF.md](../PROOF.md)，研究路线唯一入口是 [RESEARCH.md](../RESEARCH.md)。来源包不自动赋予任何数学结论当前有效状态。

[sources.json](sources.json) 记录文件 ID、原路径、字节数、哈希、路线归属、现行命题使用位置，另将巨型 ledger 的 **342 条**来源边界分别登记。文件的原状态用 `original_status_mentions` 原样记录，避免整理时冒充重新证明或静默降级旧结果。

```bash
uv run python main.py list sources --route a2-fixed3
uv run python main.py source search 'LK17G'
uv run python main.py source show SRC-0001
```

`source show` 只读并验证来源哈希，不在仓库重建日期笔记。`source extract` 需要明确目录，保全的老脚本可在临时目录复跑。证书的现行入口已迁到 `checks/`；旧算法仅作为来源，不与现行代码平行维护。

原路径和来源名保留历史命名；现行稿已按问题及依赖重新编号。公式没有因改写标题而变更。检测到的排版损坏修复单独列在 `normalizations` 中。

[重写复核记录](rewrite-verification.json) 保存本次全部 38 个模式的退出码、源码哈希、输出摘要与校验值。12 项迁移测试另核对唯一命题位置、依赖、来源完整性以及算术和公式保留。它不宣称三分支已关闭。

来源行号以 `main.py source show` 的视图为准（Python `str.splitlines()`）；旧文本中的 form-feed 损坏字符也分行，原 bytes 完整保存在来源包中。

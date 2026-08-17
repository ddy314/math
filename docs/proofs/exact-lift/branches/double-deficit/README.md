# `double-deficit`（DD）分支

这是 DD 分支的唯一规范编辑入口。主干与 frontier 后续分开保存，但 frontier 的日期笔记已经合并成一个按依赖排列的文件，不再维护多个相互重叠的 frontier 副本。

## 阅读顺序

1. [`core.md`](core.md)：原 §§17–27 及 `# 27.33` 后续合并进展，包含 DD 的统一正规化、有限证书和全局未闭合核心。
2. [`frontier.md`](frontier.md)：从一般 projective/angular allocation 到假想 `6.308883577618...` frontier 的 rational contact、5-adic allocation、单通道/十进制 remainder、Good closure 和 slot-capacity 审计。

## 当前状态

DD 仍为 `待证`。主干中的相对界、Schmidt 的非有效渐近界和已关闭的有限切片都保持原状态；`frontier.md` 的结论只在假想 frontier sequence 条件下成立，不能推出 DD 全局空性或有效绝对高度界。

## 可复核脚本

DD 的有限证书脚本位于 [`scripts/exact-lift/double-deficit/`](../../../../../scripts/exact-lift/double-deficit/)。每个脚本只覆盖正文明确给出的有限层或机械恒等式。

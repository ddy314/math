# 修改与核对规范

每项数学结果只有一个现行正文位置。修改 PROOF.md 中最具体的命题；试探、反例投影和失败推导写入 RESEARCH.md 对应 route。日期可以记在 Git 提交中，不再成为文件组织单位。

## 命题条目

```text
稳定 ID 与标题
状态：已严格完成 / 有限证书 / 待证 / 失效/降级
范围：全部变量的取值和额外假设
依赖：具体命题 ID
结论：必要条件、完整子域空性或剩余系统
证明：从依赖出发的完整推导
计算：参数界、核对 ID、输出、是否覆盖无界参数
来源：历史 SRC ID 与行号；新原创推导说明新增部分
边界：未覆盖的参数或推理缺口
```

同步更新 registry/claims.json；依赖须无环，待证/撤回条目不能为“已严格完成”提供未证明的前提。历史原命题自称的状态仅是来源信息，不能越过现行审计。结构验证会检查登记表、正文锚点、check 覆盖和历史哈希；不会自动判定证明正确。

## 核对代码

计算入口以 registry/checks.json 为准；CHECKS.md 解释 scope 与模式。需要更改运行模式时同步两个位置，并核对相关主稿命题。证书输出留在 /tmp，命题中记录可复算的计数和边界，不提交大输出。

```bash
uv run python main.py check
uv run python main.py verify <id>
uv run python -m unittest discover -s tests
uv run python -m compileall -q main.py repository.py checks tests
git diff --check
```

只有路径或注释变化时，检查 import/runpy 路径和算术 AST 保持，再跑相关核对。改变数学内容时重新证明实际假设与边界；有限回归不能替代无界论证。

## 来源与复查

```bash
uv run python main.py list sources --route a1-denominators
uv run python main.py source show SRC-0001
uv run python main.py source search '精确身份'
```

621 个旧文件全部保存在单个不可变来源包；ledger 的每条来源有独立记录 ID。原文无需再次复制到新专题。现行命题的提取范围、逐段哈希和符号修复在 history/sources.json 与 registry/claims.json 中记录。

环境版本与锁文件保留原值，因为它们承担复现契约。整理不更改数值范围、证书算法或既有未提交成果。提交前用 git diff 核对最终树；推送、合并和重写 Git 历史遵循用户授权。

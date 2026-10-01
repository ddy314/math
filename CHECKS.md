# 统一核对目录

所有命令从仓库根目录运行：`uv run python main.py verify <id>`。计算只承担下表写明的角色，主稿给完备假设与参数界。`quick` 是较短的核对集合；`full` 包含完整的大枚举与独立 reader。两种集合都不是通用数学证明器。

源码迁移保持精确系数、界和搜索算法；只调整 import、runpy 和路径。环境依赖与锁文件保留。临时编译、可执行文件和运行日志不进入仓库。

```bash
uv run python main.py list checks
uv run python main.py verify --group quick
uv run python main.py verify a1-e4
uv run python main.py verify --group full
```

## common

| ID | 集合 | 覆盖与角色 | 命题 |
|---|---|---|---|
| `norm-mod9` | quick | 符号 norm 恒等式；702 模九类，144 排除、558 允许。 | [C05](PROOF.md#c05), [C06](PROOF.md#c06) |
| `all-single-digits` | full | 26,836,101 行；三个一位分母；全部分子高度归约。 | [C10](PROOF.md#c10) |
| `all-single-digits-factored` | full | 同一覆盖的 factored reader。 | [C10](PROOF.md#c10) |
| `suffix-tail-one` | quick | 后两分母一位，n3=1；45,015 行。 | [C09](PROOF.md#c09) |
| `suffix-tail-one-factored` | quick | 尾一位 factored reader；45,015 行。 | [C09](PROOF.md#c09) |

## a2

| ID | 集合 | 覆盖与角色 | 命题 |
|---|---|---|---|
| `a2-fixed3-exceptions` | quick | a3 深 central 的 depth 12 与 eta=1 矛盾。 | [A2-08](PROOF.md#a2-08) |
| `a2-fixed3-depths` | quick | actual sphere/plane 的 depth 8/12；不是旧 6/10。 | [A2-07](PROOF.md#a2-07) |
| `a2-contact-slots` | quick | eta=2 的八个正 slot；不是完整十进制候选枚举。 | [A2-08](PROOF.md#a2-08) |
| `a2-contact-orientation` | quick | 实际 A3、共同支持及 source 3/7 字层。 | [A2-09](PROOF.md#a2-09) |
| `a2-outer-root` | quick | pC 共深度一层与实际减向 terminal 条件。 | [A2-06](PROOF.md#a2-06) |
| `a2-outer-exception` | quick | 固定素数的递归 Lucas 素性证书。 | [A2-06](PROOF.md#a2-06) |
| `a2-quartic` | quick | 四阶完整符号展开、真实 parent box 与二进初项。 | [A2-05](PROOF.md#a2-05) |
| `a2-terminal-character` | quick | strict terminal 必要条件 (26/p)=+1。 | [A2-05](PROOF.md#a2-05) |
| `a2-third-order` | quick | 三阶系数、固定 gate 与实数符号。 | [A2-05](PROOF.md#a2-05) |

## dd

| ID | 集合 | 覆盖与角色 | 命题 |
|---|---|---|---|
| `dd-unit-prefix` | quick | 单位前缀一位尾的完整同余排除。 | [C07](PROOF.md#c07) |
| `dd-single-digits` | full | 独立三个一位分母 DD 证书。 | [C10](PROOF.md#c10) |
| `dd-third-two` | quick | third-two-dominant 的长前缀 extension；7020 行。 | [DD-03](PROOF.md#dd-03) |
| `dd-suffix` | full | 后两分母一位的 DD 完整末端；3759479 行。 | [C09](PROOF.md#c09) |
| `dd-suffix-factored` | full | 同覆盖的 factored reader。 | [C09](PROOF.md#c09) |
| `dd-eight-tail` | full | m2=2,b3=8 完整证书，无长度预筛 103548188 行。 | [DD-04](PROOF.md#dd-04) |
| `dd-eight-tail-factored` | full | 八尾的 factored reader，同一完整覆盖。 | [DD-04](PROOF.md#dd-04) |
| `dd-four-tail` | quick | b3=4 到 b3=8 的合法整尺度转移。 | [DD-04](PROOF.md#dd-04) |
| `dd-gap-crt` | quick | 原 parents、共享预算、ordinary CRT 与 unique-five-tail。 | [DD-05](PROOF.md#dd-05), [DD-06](PROOF.md#dd-06), [DD-07](PROOF.md#dd-07) |
| `dd-gap-reconstruction` | quick | 条件有理恢复 period；不证明 joint family 为空。 | [DD-B02](PROOF.md#dd-b02), [DD-08](PROOF.md#dd-08) |
| `dd-numerator-count` | quick | 非循环 period、原 norm 与 selected sheets 投影。 | [DD-08](PROOF.md#dd-08), [DD-09](PROOF.md#dd-09) |
| `dd-denominator-entropy` | quick | denominator/S-unit entropy；不含旧循环 full-candidate 合并。 | [DD-08](PROOF.md#dd-08) |
| `dd-global-sparsity` | quick | fixed delta0<1/2 同预算 global exponent。 | [DD-08](PROOF.md#dd-08) |
| `cpp-suffix` | full | 独立 C++ DD standard；3759479 行。 | [C09](PROOF.md#c09) |
| `cpp-suffix-factored` | full | 独立 C++ DD factored；3759479 行。 | [C09](PROOF.md#c09) |
| `cpp-tail-one` | full | 独立 C++ n3=1 standard；45015 行。 | [C09](PROOF.md#c09) |
| `cpp-tail-one-factored` | full | 独立 C++ n3=1 factored；45015 行。 | [C09](PROOF.md#c09) |

## a1

| ID | 集合 | 覆盖与角色 | 命题 |
|---|---|---|---|
| `a1-kernels` | quick | 恒等式、深度三分裂及真实 product 条件。 | [A1-K01](PROOF.md#a1-k01), [A1-K02](PROOF.md#a1-k02), [A1-K03](PROOF.md#a1-k03), [A1-K04](PROOF.md#a1-k04), [A1-K05](PROOF.md#a1-k05), [A1-K06](PROOF.md#a1-k06) |
| `a1-e2` | quick | g=0,e=2 balanced-tail；5050 prefix / 219101 J。 | [A1-F02](PROOF.md#a1-f02) |
| `a1-e4` | full | C++ 枚举 262115848 J，Python 独立复核 1377 筛后候选。 | [A1-F04](PROOF.md#a1-f04) |
| `a1-first-strict` | quick | g=1,delta=2；2566 prefix / 30923 J，平方投影仍无法恢复合法根。 | [A1-F12](PROOF.md#a1-f12) |
| `a1-unit-prefix` | quick | g=0,b1=b2=1 balanced-tail；855 prefix / 161 J。 | [A1-F12](PROOF.md#a1-f12) |
| `a1-joint-surplus` | quick | JS 恒等式和精确不等式；有界样例不承担无界证明。 | [A1-04](PROOF.md#a1-04), [A1-05](PROOF.md#a1-05) |
| `cpp-a1-e4` | full | 独立完整 e4 C++ certificate；Python wrapper 另复核筛后候选。 | [A1-F04](PROOF.md#a1-f04) |

## 范围与结果

后两分母一位的 Python/C++ 两 reader 分別核对 45,015 与 3,759,479 行，原解为零。八尾两位第二分母证书不使用长度预筛时为每 reader 103,548,188 行；默认必要 norm 预筛模式覆盖同一子域并减少枚举行数，两者不能混记。

A1 e4 的 262,115,848 个合法 J 经精确余类 sieve 留 1377 个投影，Python 独立重算它们的原 discriminant。g1 首 strict 证书保留一个 square projection，而两根都不能恢复合法正尾；输出原解零。

本次重写后全部 38 个模式已重新运行通过，覆盖计数与基线一致；[复核记录](history/rewrite-verification.json) 保存源码与输出哈希，完整日志仍在临时验证目录。数学范围仍以 PROOF.md 为准。A2/DD 的符号 identities 与玩具 residue checks 不属于一般 Exact Lift 穷尽枚举。

## 修改核对入口

命令和模式的机器来源是 [checks.json](registry/checks.json)。每个入口链接到具体现行命题；原文件 ID 与迁移后源码哈希同表保留。添加新核对应先写清主稿或研究目标，再登记入口，禁止重建层层 research-checks/日期脚本树。

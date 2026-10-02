# 统一核对目录

所有命令从仓库根目录运行：`uv run python main.py verify <id>`。计算只承担下表写明的角色，主稿给完备假设与参数界。`quick` 是较短的核对集合；`full` 包含完整的大枚举与独立 reader。两种集合都不是通用数学证明器。

原源码迁移保持精确系数、界和搜索算法；只调整 import、runpy 和路径。后续新核对按稳定命题登记，注明新增来源。环境依赖与锁文件保留。临时编译、可执行文件和运行日志不进入仓库。

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
| `a2-first-block` | quick | 第一块界、严格实数窗、奇尾恢复、归一化尾长及既约素数过滤；G10 相对界 `m3≤10m2`、五进单位时 `m3≤3m2`。外部子空间定理不由脚本证明。 | [A2-G01](PROOF.md#a2-g01), [A2-G02](PROOF.md#a2-g02), [A2-G03](PROOF.md#a2-g03), [A2-G06](PROOF.md#a2-g06), [A2-G07](PROOF.md#a2-g07), [A2-G09](PROOF.md#a2-g09), [A2-G10](PROOF.md#a2-g10), [A2-F01](PROOF.md#a2-f01), [A2-F02](PROOF.md#a2-f02) |
| `a2-binary-chambers` | quick | 二进主导与两个 sphere gap；五进尾主导、纯五次幂尾商及 source 锁；固定尾长界与联合 gap。有限模式不是原候选穷尽。 | [A2-G04](PROOF.md#a2-g04), [A2-G05](PROOF.md#a2-g05), [A2-G08](PROOF.md#a2-g08) |
| `a2-nondecimal-support` | quick | 非十进制共同支持、原 `k+cU` 素幂锁与半径整除；符号恒等式、1,314 个有限分母投影和素数平方类。无界证明在 G11，投影不是原解枚举。 | [A2-G11](PROOF.md#a2-g11) |
| `a2-decimal-divisor` | quick | 六种分母形状和 560 个恒等式投影；显式指数界的有理常数核对，模 `2^27` 唯一指数类的三种整数 reader，以及 `E=2..8`。完整无界排除还依赖主稿中明示的 Bugeaud 定理。 | [A2-G12](PROOF.md#a2-g12) |
| `a2-decimal-rays` | quick | 完整 4 行一位首部、35 行两位首部及 1,197 个恒等式投影；16 个固定系数的有效界和模 `2^27` 三种整数 reader；两族原式的模 5/8 障碍。完整空性与唯一必要族归约在主稿，剩余族仍待证。 | [A2-G13](PROOF.md#a2-g13)、[A2-G14](PROOF.md#a2-g14) |
| `a2-decimal-ray-residual` | quick | 原恢复、消元与平方和商恒等式；有效整数窗口，四个完整指数周期。`E=4..12` 的九个奇深素因子；`E=3` 的 612 个 gap 行和独立 39,999 个原分子行。保留 `E=13` 的平方和允许投影。 | [A2-G15](PROOF.md#a2-g15)、[A2-F09](PROOF.md#a2-f09) |
| `a2-rational-recovery` | quick | G16 的有理圆恒等式、`r=24` 严格实数弧、`E=13` 精确非整数见证、denominator norm 因式分解及双变量整数恢复同余；不证明整数系统为空。 | [A2-G16](PROOF.md#a2-g16) |
| `a2-one-digit-tail` | quick | 一位尾的全部 11,544 个奇尾标签；原整数性及平方类的完整指数周期，任意精度 Python。 | [A2-F01](PROOF.md#a2-f01) |
| `a2-one-digit-tail-cpp` | quick | 同一完整标签覆盖，独立展开系数与反向周期传播；128 位整数，可用 `--ubsan`。 | [A2-F01](PROOF.md#a2-f01) |
| `a2-two-digit-tail` | full | 全部两位尾：独立重算 47,432,488 个标签总数、复核全部 250 个周期筛后标签、3,366 个有界原二次式。 | [A2-F02](PROOF.md#a2-f02) |
| `a2-two-digit-tail-cpp` | full | 同一完整周期标签；原既约性和二进 primitive recovery；128 位整数，可用 `--ubsan`。 | [A2-F02](PROOF.md#a2-f02) |
| `a2-short-prefix-even` | full | 三至五位偶尾两个有界二进类；114/1,814/23,306 个分母组合，共 272,158,962 个原二次式；五位尾 C++ 任意精度与独立 Python 全行核对，零合法根。 | [A2-G08](PROOF.md#a2-g08), [A2-F03](PROOF.md#a2-f03) |
| `a2-short-prefix-even-six` | full | 六位偶尾同两个有界类；270,385 个分母组合、29,740,339,198 个原二次式。C++ 全枚举；Python 独立审计全部 297,935 条系数、区间行数和三个非整数投影，未做第二遍全行扫描。 | [A2-F03](PROOF.md#a2-f03) |
| `a2-three-digit-five` | full | 三位尾且第二分母含 5；容斥重算 120,626,568 标签，完整循环轨道复核 4 个筛后标签，另 100 个有界原二次式。 | [A2-F04](PROOF.md#a2-f04) |
| `a2-three-digit-five-cpp` | full | 同一完整周期部分，独立因式/展开 reader；128 位整数，可用 `--ubsan`。 | [A2-F04](PROOF.md#a2-f04) |
| `a2-fixed-prefix` | quick | 固定原前缀有效尾长界；全部 `m2=2`，102 前缀、`m3≤20`、12,025 原尾二次式，两 reader 全行比较，零平方判别式。 | [A2-G10](PROOF.md#a2-g10), [A2-F05](PROOF.md#a2-f05) |
| `a2-fixed-prefix-three` | quick | 全部 `m2=3`；11,993 前缀、有效尾界 30、55,508 原尾二次式，两 reader 逐行核对。 | [A2-G10](PROOF.md#a2-g10), [A2-F06](PROOF.md#a2-f06) |
| `a2-fixed-prefix-four` | full | 全部 `m2=4`；1,229,008 前缀、有效尾界 40、7,448,321 原尾二次式，两 reader 全行独立判别式核对。 | [A2-G10](PROOF.md#a2-g10)、[A2-F06](PROOF.md#a2-f06) |
| `a2-three-tail-five` | full | 三位尾且尾分母含 5；五进单位前缀的 2,990,309,248 标签与 117 个独立完整轨道复核。 | [A2-F07](PROOF.md#a2-f07) |
| `a2-three-odd-coprime` | quick | 整个三位奇尾且后两分母互素子域；476,207 完整标签，两个 C++ reader/UBSan 与独立 Python 全几何、整数轨道、25,683 周期标签核对。 | [A2-F08](PROOF.md#a2-f08) |
| `a2-three-odd-inventory` | quick | 三位奇尾五进单位的非互素完整必要标签清单；真共同支持约 25.59 亿、完全共同支持约 776.70 亿。只是允许投影，不证明空性。 | [A2-G11](PROOF.md#a2-g11) |
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

后两分母一位的 Python/C++ 两 reader 分别核对 45,015 与 3,759,479 行，原解为零。八尾两位第二分母证书不使用长度预筛时为每 reader 103,548,188 行；默认必要 norm 预筛模式覆盖同一子域并减少枚举行数，两者不能混记。

A1 e4 的 262,115,848 个合法 J 经精确余类 sieve 留 1377 个投影，Python 独立重算它们的原 discriminant。g1 首 strict 证书保留一个 square projection，而两根都不能恢复合法正尾；输出原解零。

本次重写后的原 38 个模式已重新运行通过，覆盖计数与基线一致；[复核记录](history/rewrite-verification.json) 保存当时源码与输出哈希，完整日志仍在临时验证目录。新增 A2 核对覆盖 G01–G12 的恒等式、常数与赋值分支，以及 F01–F08 的完整周期和原方程证书，不改写该迁移记录。新增 18 个 A2 模式均已有与当前源码及依赖哈希一致的通过报告；完整 quick 集合与 13 个仓库测试也通过。数学范围仍以 PROOF.md 为准。A2/DD 的符号 identities 与玩具 residue checks 不属于一般 Exact Lift 穷尽枚举。

## 修改核对入口

命令和模式的机器来源是 [checks.json](registry/checks.json)。每个入口链接到具体现行命题；原文件 ID 与迁移后源码哈希同表保留。共享头文件和本地 reader 依赖也须登记 `dependencies`；结构检查及运行报告核对它们的哈希。添加新核对应先写清主稿或研究目标，再登记入口，禁止重建层层 research-checks/日期脚本树。

本次新增 `a2-rational-recovery` 已以精确有理算术和 SymPy 恒等式独立运行通过；它核对 G16 的代数接口，不承担无界整数空性证明。

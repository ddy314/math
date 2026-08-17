# 仓库脚本

分支专用脚本按 `scripts/exact-lift/{a2-only,double-deficit,a1-only}/` 归档，避免与共享的 `proof_tree.py` 及其他分支证书混在同一层。除标准库外，使用到的 SymPy/NumPy 等依赖均由 `uv.lock` 管理，优先通过 `uv run` 调用。

## 分支脚本入口

- `scripts/exact-lift/a2-only/`：A2 source-Hensel、decimal ellipse 和 endpoint-lattice 校验。
- `scripts/exact-lift/double-deficit/`：DD 第 27.10–27.33 节的符号核对与有限证书；下方保留每个证书的边界说明。
- `scripts/exact-lift/a1-only/`：A1 `k=g=1,2` minimal-diagonal 有限证书。

例如：

```bash
uv run python scripts/exact-lift/a2-only/check_a2_151.py
uv run python scripts/exact-lift/a1-only/check_a1_top_diag_k1.py --jobs 4
```

## `proof_tree.py`

检查证明树的必需文件、一级章节、内部 Markdown 链接和当前开放状态：

```bash
uv run python scripts/proof_tree.py check
```

列出结构化证明文件及行数：

```bash
uv run python scripts/proof_tree.py list
```

这个检查器只验证仓库结构和文档一致性，不验证数学推导。

## `check_dd_2710.py`

机械核对 DD 第 27.10 节中 primitive recovery 的三条符号消元，以及
五进入口与两个高度上界之间的单调余量：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2710.py
```

它不验证第 27.10 节所依赖的数学假设，也不是 DD 分支的有限证书。

## `check_dd_2711.py`

机械核对 DD 第 27.11 节中的加权 resonance 消元、粗有理高度比较和
最高整数层的 \(\Xi<20\) residue 列表：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2711.py
```

它不验证正文假设，也不枚举 DD 候选。

## `check_dd_2712.py`

机械核对 DD 第 27.12 节使用的整数幂对数证书、残余
\((S,m_3)\) 列表和两个最终高度比较：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2712.py
```

它不枚举原问题候选，也不代替正文的无界推导。

## `check_dd_2713.py`

机械核对 DD 第 27.13 节中 `t_2 >= 2` 子锥的模 \(3\) residue、
最高剩余层 \(n_3=8S+4\) 的有理参数压缩、\((S,m_3)=(8,32)\)
的直接整数赋值矛盾，以及最后十个尺寸的赋值—余因子区间证书：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2713.py
```

它不枚举原问题的分子、分母；最终循环只穷尽正文严格导出的 225 个
赋值元组及其有界十进制余因子，构成 \(n_3=8S+4\) 这一明确有界层
的有限证书，不覆盖更低的无界区域。

## `check_dd_2714.py`

机械核对 DD 第 27.14 节中 \(n_3=8S+3\) 与 \(n_3=8S+2\) 两层的
有理尺寸核、精确整数赋值盒和一般 \(G<10^S\) 余因子区间证书：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2714.py
```

两层分别覆盖 32、59 个尺寸及 2677、14095 个必要赋值元组。证书
排除的是这两个先经无界符号推导压成有限盒的明确层，不覆盖更低层。

## `check_dd_2715.py`

机械核对 DD 第 27.15 节中 \(n_3=8S+1,\ S\ge4\) 的尺寸核、48808
个赋值元组及唯一余因子幸存者，并验证它最终固定
\((b_1,b_2)=(768,97)\)、\((s_1,s_2)=(-2,4)\) 后，near-square
判别式模 \(3\) 为非平方：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2715.py
```

该证书本身不处理同一层的 \(S=2,3\)；这两个入口边界由下一节的
独立有限证书处理。

## `check_dd_2716.py`

有限核对 DD 第 27.16 节中 \(n_3=8S+1\) 的两个入口边界
\(S=2,3\)。脚本先穷尽统一尾权除数区间，再施加二进位置与 resonance、
五进三分支、全部有界前缀、squarefree gap 和统一判别平方：

~~~bash
uv run python scripts/exact-lift/double-deficit/check_dd_2716.py
~~~

两个尺寸分别从 618、39710 个 denominator-tail 元组缩到 75、5116
个，再只留下 114、27 个满足二进与五进条件的 tail-prefix 组合；
squarefree gap 最终留下 2、8 个判别式，精确整数平方根检查验证十个
均非平方。该证书只覆盖 \(S=2,3,n_3=8S+1\)，不覆盖
\(n_3\le8S\) 的更低无界区域。

## `check_dd_2717.py`

核对 DD 第 27.17 节在新边界 \(n_3=8S\) 上的入口分解：脚本验证
\(t_2=1,S\ge11\) 的 70 个有理尺寸、51828 个必要赋值行，并用
floor-sum 与对 \(2,5\) 的容斥精确计算余因子循环剩余类区间：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2717.py
```

模计数器先与 1000 个随机小盒的直接枚举对照，全部尺寸最终有零个
余因子幸存者。脚本还核对 \(t_2\ge2\) 等号层的八个常数核赋值表。
它不枚举原始 DD 分子、分母，也不关闭这八个无界前缀族或
\(2\le S\le10\) 的入口下有限 \(S\)-列表；后者不能仅因 \(S\)
固定就视为完整有限候选盒。

## `check_dd_2718.py`

机械核对 DD 第 27.18 节关闭八个入口上常数核时使用的赋值表、
\(F_-/10^{2S}\) 的 18300 个 \((c,\rho)\) 赋值行计数、gcd 上界与最终统一
常数比较：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2718.py
```

脚本不证明正文中由两个 \(\mu/\nu\) 公式导出的精确整除，也不枚举
原始 DD 块。\(S\ge11\) 的无界排除来自正文的整除式两侧分别按
\(10^{2S}\) 与 \(10^S\) 增长；脚本只复核其中的常数算术。

## `check_dd_2719.py`

有限核对 DD 第 27.19 节在 \(4\le S\le10,n_3=8S\) 中的
\(b_3\)-二进主导、\(t_2=1\)、唯一五进正规形子支。56 个尺寸的
97693 个赋值行先由同步 \(F_-\) 因子界压到 3121 行，再由余因子
区间与真实 denominator factorization 压到唯一尾核；该核由模 3
near-square 矛盾排除：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2719.py
```

脚本不枚举 numerators，也不覆盖普通入口下 resonance、
\(5\nmid b_3\) 或 \(\Delta_5^\pm\)。

## `check_dd_2720.py`

有限核对 DD 第 27.20 节在同一个唯一五进正规形中尚未由无界论证
覆盖的 \(t_2\ge2,S=4,5,6\) 分母块。三个尺寸分别检查 129600、
1296000、12960000 个有序真实分母块；固定赋值预算、尾区间与
\(F_-\) 大除数条件后均无幸存者：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2720.py
```

脚本不枚举 numerators；它与第 27.18 节的 \(S\ge7\) 无界论证合并，
只关闭 \(4\le S\le10\) 的 \(b_3\)-二进主导唯一五进正规形，不关闭
其他五进状态或二进位置。

## `check_dd_2721.py`

机械核对 DD 第 27.21 节把 \(n_3=8S\) 等号层压到 \(S=2,3\)
时使用的整数幂比较、五进单位尾乘数界和三个最终二进剩余类：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2721.py
```

正文先在 \(5\mid b_3\) 时恢复 \(e_5=q_5\)，逐一排除 resonance 与
\(\Delta_5^\pm\)；在 \(5\nmid b_3\) 时则把尾权压成
\(2\cdot5^{3S}\) 并由二进 resonance 同余排除。脚本只复核常数算术，
不替代这些无界符号推导。

## `check_dd_2722.py`

有限核对 DD 第 27.22 节留下的两个等号尺寸
\(S=2,3,n_3=8S\)。脚本先只用强制 \(m_3\) 范围与 primitive
denominator-tail 整除关闭 non-dominant 扇区，不枚举其可能无界的
prefix surplus；dominant 扇区再由 \(n_1+n_2\le S+2\) 得到真实有限
前缀盒，并施加二进位置、两素数三状态、既约性、squarefree gap 与
统一判别式：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2722.py
```

两个尺寸的 dominant tail 核分别有 1527、72092 行；最终精确检查
703、38633 个非负判别式，全部非平方。squarefree gap 的大乘积用
多 limb 整数比较避免 `int64` 溢出。该证书与第 27.21 节合并后
关闭整个 \(n_3=8S\) 层并给出 \(n_3\le8S-1\)，但不覆盖这一界以下
仍可无界增长的 DD 区域。

## `check_dd_2723.py`

机械核对 DD 第 27.23 节对 non-dominant 锥和 \(8S-1\) 层的进一步
压缩：脚本穷尽唯一尚未由无界论证或既有尾表覆盖的
\(S=4,m_3=27\) denominator-tail 层，并验证它为空；随后核对五进入口
幂比较、\(t_2\ge2\) 的 19、9、0 个常数核与统一大除数常数，以及
\(t_2=1\) 的有理尺寸窗口、valuation 盒与精确 floor-sum 余因子证书：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2723.py
```

它支持正文的全局 \(m_3\le6S+2\)、non-dominant
\(n_3\le7S+2\)，以及
\(n_3=8S-1\Rightarrow S\le17\)。其中 \(t_2=1\) 部分覆盖 45 个
尺寸、15525 个 valuation rows，并得到零余因子幸存者。最后一个结论
只把最高层变成完整有限盒；脚本没有穷尽该盒，不能称为 \(8S-1\)
层空性证书。

## `check_dd_2724.py`

有限核对 DD 第 27.24 节中 \(n_3=8S-1\) 的两个最小尺寸
\(S=2,3\)。脚本复用第 27.22 节的完整 denominator-tail、二进位置、
两素数三状态、精确多 limb squarefree gap 与统一判别式框架：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2724.py
```

两个 dominant 尾核分别有 2665、126669 行；最终检查 24396、
1582338 个非负判别式，全部非平方。该证书只把最高层进一步缩到
\(4\le S\le17\)，不覆盖这些剩余尺寸或 \(n_3\le8S-2\) 的无界区域。

## `check_dd_2725.py`

有限核对 DD 第 27.25 节中 \(S=4,n_3=31,m_3=11\) 的完整切片。
squarefree gap 先把位数压成两个极端有序形状，其中一个由严格大小界
直接排除；脚本对另一个形状逐项生成开口向上二次不等式的全部正整数
区间，并施加二进位置、两素数三状态、既约性与统一判别式：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2725.py
```

相关的 382086 个 tail rows 最终产生 694825 个非负大整数判别式，
全部非平方。二次区间算法先与 2000 个随机小盒直接枚举对照。该证书
只排除这个单一尾长，不关闭整个 \(S=4\) 尺寸。

## `check_dd_2726.py`

有限核对同一尺寸的 \(m_3=12\) 完整切片。严格位数估计留下三个
有序 prefix 形状；精确二次区间与两素数三状态把 613218 个相关
tail rows 产生的候选压成 138352740 个 valuation-tail 判别式：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2726.py
```

脚本先用模
\(2882880=2^6\cdot3^2\cdot5\cdot7\cdot11\cdot13\) 的完整平方剩余表
作必要过滤，再对 10987773 个幸存判别式使用 Python 大整数
`math.isqrt`；全部非平方。该有限证书与上一脚本合并只得到
\(S=4,n_3=31\Rightarrow m_3\ge13\)，不覆盖更高尾长、其他尺寸或
\(n_3\le8S-2\) 的无界区域。

## `check_dd_2727.py`

有限核对 DD 第 27.26 节中 \(S=4,n_3=31,m_3=13\) 的完整切片。
粗 squarefree-gap 位数盒有十种有序形状，其中三种由统一严格大小界
直接排除；其余七种复用精确二次区间、两素数三状态、模平方表与统一
判别式引擎：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2727.py
```

551649 个相关 tail rows 产生 5088309 个 valuation-tail 判别式；模
2882880 的完整平方剩余表留下 714489 个，最终 Python 大整数
`math.isqrt` 检查全部非平方。与前两层合并先得到
\(S=4,n_3=31\Rightarrow m_3\ge14\)；下一脚本继续处理 \(m_3=14\)。

## `check_dd_2728.py`

有限核对 DD 第 27.27 节中 \(S=4,n_3=31,m_3=14\) 的完整切片。
十六种粗位数形状中三种由严格大小界直接排除；其余十三种复用同一
套精确二次区间、两素数三状态、模平方表与统一判别式引擎：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2728.py
```

379935 个相关 tail rows 产生 1077887 个 valuation-tail 判别式；模
2882880 的完整平方剩余表留下 99342 个，最终 Python 大整数
`math.isqrt` 检查全部非平方。与前三层合并先得到
\(S=4,n_3=31\Rightarrow m_3\ge15\)；下一组证书继续处理全部剩余
尾长。

## `check_dd_2729.cpp` 与 `check_dd_2729.py`

关闭 DD 第 27.28 节中 \(S=4,n_3=31\) 的全部剩余尾层。C++ 主证书
覆盖 \(m_3=15,\ldots,21\)，用精确 \(2\)-进、\(5\)-进剩余树流式
生成三状态候选，并逐项复验既约性、严格 squarefree gap、模平方表与
`boost::multiprecision::cpp_int` 统一判别式。它固定断言七层的
位数形状、二进位置和全部计数：

```bash
g++ -O3 -DNDEBUG -std=c++20 -fopenmp \
  scripts/exact-lift/double-deficit/check_dd_2729.cpp -o /tmp/check_dd_2729_cpp
/tmp/check_dd_2729_cpp --self-check --m3-min 15 --m3-max 21 \
  --expect-baseline
```

七层的精确平方判别式计数均为零。`--self-check` 把开口向上二次
区间、两素数剩余树与多精度整数平方根和直接枚举或精确输入交叉
核验；C++ 基线故意不使用 Python 中可选的四角凸性、valuation box
或通用 \(L_F\) 前筛，因此计数是稳定的未过滤全量基线。

Python 脚本的高尾模式逐项穷尽 \(m_3=22,\ldots,26\) 的 primitive
denominator-tail divisor tree，并断言五层 tail 核都为空：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2729.py --empty-high-only
```

不带参数时，Python 实现还可独立复核 \(m_3=15,\ldots,21\)，并使用
严格四角凸性、valuation-height box 与通用 \(F_-\) 大除数作前置
过滤。对 \(m_3=15,20,21\)，还可关闭这些可选前筛并逐项核对 C++
记录的未过滤基线：

```bash
uv run python scripts/exact-lift/double-deficit/check_dd_2729.py --m3 15 --unfiltered
uv run python scripts/exact-lift/double-deficit/check_dd_2729.py --m3 20 --unfiltered
uv run python scripts/exact-lift/double-deficit/check_dd_2729.py --m3 21 --unfiltered
```

主证书与高尾证书合并只关闭 \(S=4,n_3=31\) 这个明确有界的
尺寸；最高层的 \(5\le S\le17\) 及 \(n_3\le8S-2\) 的无界区域仍待证。

## `check_dd_2730.cpp`

有限核对 DD 第 27.29 节中 \(S=5,n_3=39\) 的高尾层。程序对
\(m_3=22,\ldots,26\) 穷尽四个有序分母位数拆分的 324000 个真实
分母对，复用精确二次区间与两素数剩余树，并用
`unsigned __int128` 保存可能超过 64 位的 \(\mathcal N_{12}\)，最终
转为 `boost::multiprecision::cpp_int` 检查统一判别式：

```bash
g++ -O3 -DNDEBUG -std=c++20 -fopenmp \
  scripts/exact-lift/double-deficit/check_dd_2730.cpp -o /tmp/check_dd_2730_cpp
/tmp/check_dd_2730_cpp --self-check --expect-baseline --threads 12
```

五层分别有 136692、23052、3742、401、35 个 primitive tail rows，
最终精确平方判别式均为零。相同命令还一次性核对
\(m_3=27,\ldots,32\) 的 divisor tree，并固定断言六层 primitive tail
核都为空。128 位剩余树及 128 位到多精度整数的转换均有独立随机
小盒自检。

因此与下一脚本合并前，这个明确有界的尺寸先缩到
\(14\le m_3\le21\)、\(18\le d_3\le25\)。程序没有关闭这些最低
八个尾长，也不覆盖其余最高层尺寸或更低的无界 DD 区域。

## `check_dd_2731.cpp`

有限核对 DD 第 27.30 节中 \(S=5,n_3=39,m_3=14\) 的完整切片。
严格位数盒只留下 \((m_1,m_2;n_1,n_2)=(4,1;1,6)\)。完整 primitive
tail 核先由四角凸性、valuation height box、通用 \(L_F\) 大除数与
分母单位性赋值盒逐级压缩，再用第 27.29 节的 128 位两素数剩余树
复验所有前缀：

```bash
g++ -O3 -DNDEBUG -std=c++20 -fopenmp \
  scripts/exact-lift/double-deficit/check_dd_2731.cpp -o /tmp/check_dd_2731_cpp
/tmp/check_dd_2731_cpp --self-check --threads 12 --expect-baseline
```

6207930 个 primitive tail rows 中 5828153 个进入状态核；四角、
valuation box、\(L_F\)、二进单位性盒、五进单位性盒依次留下
1378380、1123254、8495、611、75 行。最终 49 个 denominator pairs
产生 7930779 个 squarefree-gap 前缀，但完整两素数三状态交集为空。
所以与下一脚本合并前，这个尺寸只剩 \(15\le m_3\le21\)、
\(18\le d_3\le24\)。
这仍不关闭整个 \(S=5\) 尺寸或 DD 分支。

## `check_dd_2732.cpp`

有限核对 DD 第 27.31 节中 \(S=5,n_3=39,m_3=15\) 的完整切片。
严格位数核固定为三个形状；程序对每个形状分别应用 128 位四角
gap、shape-specific valuation height box、通用 \(L_F\) 大除数与
二/五进 denominator-unit reachable box，再把全部幸存前缀送入原始
两素数状态和多精度判别式：

```bash
g++ -O3 -DNDEBUG -std=c++20 -fopenmp \
  -Wall -Wextra -Wconversion -Wshadow \
  scripts/exact-lift/double-deficit/check_dd_2732.cpp -o /tmp/check_dd_2732_cpp
/tmp/check_dd_2732_cpp --self-check --threads 12 --expect-baseline
```

三个形状在全部必要过滤后分别剩 1404、17、5499 条 primitive
tails；精确判别式平方数均为零。程序固定断言位数形状、各过滤阶段、
位置和全部前缀计数，并随机抽查 denominator-unit 过滤从不删除实际
满足原状态的前缀。与前两份证书合并后，这个尺寸只剩
\(16\le m_3\le21\)、\(18\le d_3\le23\)，仍未关闭整个 \(S=5\)
尺寸或 DD 分支。

## `check_dd_2733.cpp`

有限核对 DD 第 27.32 节中 \(S=5,n_3=39,m_3=16\) 的完整切片。
程序固定断言 10 个粗形状、3 个 size-killed 与 7 个严格幸存形状；
逐形状执行 128 位四角 gap、shape-specific valuation height、\(L_F\)
与二/五进 denominator-unit 必要过滤，再完整复验原状态和多精度判别式：

```bash
g++ -O3 -DNDEBUG -std=c++20 -fopenmp \
  -Wall -Wextra -Wconversion -Wshadow \
  scripts/exact-lift/double-deficit/check_dd_2733.cpp -o /tmp/check_dd_2733_cpp
/tmp/check_dd_2733_cpp --self-check --threads 12 --expect-baseline
```

七形状五进过滤后共有 113002 条 primitive tails、23656 个非空
shape--denominator jobs；141826212 个 valuation-tail pairs 经多精度
精确检查没有平方判别式。与前三份 S=5 证书合并后，该尺寸只剩
\(17\le m_3\le21\)、\(18\le d_3\le22\)。这仍不关闭整个 \(S=5\)
尺寸或 DD 分支。

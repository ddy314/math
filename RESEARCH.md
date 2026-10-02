# 研究路线与审计记录

本文件按数学目标组织研究，不按实验日期排列。现行已采纳的命题只在 [PROOF.md](PROOF.md) 中证明。下面区分严格归约、尚待证明的联合系统、失败推断和历史证据；所有历史文件均能通过路线 ID 检索。

主不存在性命题、A2、DD、A1 完整空性均为 **待证**。任何候选计数、局部 Hensel lift、norm 允许点或固定前缀有限性都不改变这一事实。

<a id="common-model"></a>
## 原方程与必要投影

路线 `common-model` · 状态：**已严格完成**。原十进制 cut、整数球面与分母投影；投影允许点不是解。

公共对象从原 `alpha,beta` 出发。整数球面必须同时满足原 coefficient plane；局部变换不能只保留 sphere。当前 denominator norm 的惯性素数偶深度、模九过滤及二进深度都是必要投影。允许的 `(1,1,4) mod9` 等类不能作为原解。

Gaussian flip / Vieta root 的旧 descent 企图没有证明真实十进制 cut、尺度、正性与逐块既约的同时保持，不能继续作为主不存在性的依赖。

现行命题：[C01](PROOF.md#c01)、[C02](PROOF.md#c02)、[C03](PROOF.md#c03)、[C04](PROOF.md#c04)、[C05](PROOF.md#c05)、[C06](PROOF.md#c06)、[C07](PROOF.md#c07)、[C08](PROOF.md#c08)

历史证据：`uv run python main.py list sources --route common-model`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="common-certificates"></a>
## 有高度归约的完整子域证书

路线 `common-certificates` · 状态：**有限证书**。一位后缀等明示子域；每项先证明全部参数界。

后两分母一位：C09 给全部参数界后，尾一位与 DD 两片分别有 45,015 和 3,759,479 个 quadratic rows；每种 reader 总覆盖 3,804,494 行。第一分母起初任意，三个分子起初任意。

这类证书闭合完整明示子域；三个一位分母的独立 26,836,101 行证书是校核，不是新增无界参数上界。一般多位分母仍保留。

现行命题：[C09](PROOF.md#c09)、[C10](PROOF.md#c10)

历史证据：`uv run python main.py list sources --route common-certificates`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="a2-core"></a>
## 相邻边界与 deep-even 参数核

路线 `a2-core` · 状态：**待证**。全部 A2 的原式余核；旧 deep-even chart 只覆盖明示子片。

现行原候选已同时满足：

- 第一块是 G01 的 13 种，`b1=1,a1=1..8` 或 `b1=2,a1∈{5,7,9,11,13}`。
- `m2≥5,m3≥3`：F01/F02 关闭整个一、两位尾；F05/F06 关闭整个两至四位第二分母。
- `b2∤b1·10^m2`：G12 关闭相反条件下的完整无界子域，包含所有第二分母为十进制幂的情形。
- 第二分母不能只有一位有效数字；若只有两位有效数字，则必须是 G14/F09 的唯一必要族 `b1=1,a1=2,b2=24·10^(2E−1),b3=8·10^(3E−1),E≥13`，从而 `m2≥27,m3≥39`。
- `m3≤10m2`。后两分母不含 5 时还有 `m3≤v5(S)≤3m2`，`S=(a1·b2)²+(b1·a2)²`；G10 给每个固定原前两块的可计算尾长界。
- 三位尾须 `5∤b2b3`、`125|S`。若三位尾为奇尾，还须 `c=gcd(b2,b3)>1`；这是 F04/F07/F08 的完整范围，没有排除其它原候选。

奇尾由 G02/G06 限为 `b1=1,a1=4,m3=3,4` 或 `b1=1,a1=8,m3=3..6`，保留主稿分类表中的分子赋值条件。G03 证明整个奇尾原候选集合有限，G09 证明任意固定尾长的全 A2 原候选集合有限；两者均不给有效前缀界，有限例外尚未排除。全 A2 若有无限候选，其无限部分只能在越来越长的偶尾中；不能把固定系列的有限并集外推到无限多个系列。

偶尾的二进分类见 G04，五进尾主导与 source 桥梁见 G05。F03 排除三至六位偶尾的两个完整有界类：第二分母二进主导，或尾主导且 `v2(b2)≥v2(b1)+m2`。这些尾长的余核只在 ordinary 二进类；七位及更长尾仍保留上述主导类。ordinary 的明示二进/五进减 gap 冲突类已由 G08 排除，二进加 gap、五进单位及五进等深加 gap 仍保留。五进两个单位相加不必进位，不能套用二进论证。

G11 给完整非十进制支持：共同素幂必须同深，共同素数均为 `1 mod4`；尾剩余非十进制部分整除 `k+cU`。固定前缀的支持唯一分解为 `C=CM·CQ`，其中 `CM` 为 `M0` 的完整 unitary 因子，`CQ|Q0`，两者互素。三位奇尾五进单位时，`c` 因此是 `b3` 的 unitary divisor。完全共同支持 `c=b3` 仍允许；真因子类的周期试算尚未形成完整证书。原半径还给 `H=b3·alpha/(k+cU)` 为整数，奇尾五进单位时 `ell=(k+cU)/(b3/c)` 整除原 `alpha`，并恰为 `gcd(alpha,beta)`；半径既约分母为 `b2·b3/c²`。这个精确 height 接口仍只约束原候选，第二分子须满足相应剩余类与既约恢复。

`a2-three-odd-inventory` 独立清点三位奇尾五进单位的完整必要标签：`1<c<b3` 为 78 个分母支持、5,782,874 个 `(b3,c,k)` 标签、2,559,479,281 个带尾分子的标签；`c=b3` 为 44 个分母支持、117,120,640 个标签、77,670,247,200 个带尾分子的标签。它们都是允许投影计数，不是原候选数；非互素周期试算在本轮时间上限内未完成并已停止，阶段日志不承担完整证书。

G12 将 `b2∣b1·10^m2` 归约为六种分母形状，用 `q=b3` 的整数半径大小排除五进加 gap，再由原 word 的二进加 gap 排除所有剩余。唯一指数末端 `v2(7·25^E+1)=3E` 先由 Bugeaud (2002) Theorem 2 得到有效绝对界 `E<10^6`，再由完整模 `2^27` 余类和七个小指数排除。这一子域已关闭；外部定理的适用参数写在主稿，不能把同一界用于系数随前缀变化的普通系统。

G13 完整排除一位有效数字的第二分母。G14 将两位有效数字的第二分母归约为唯一必要族；二进加 gap 的 16 个固定系数都有明示 `E<10^6` 和完整周期证书，双减 gap 的两个 `r=12` 中间族分别被模 5 非平方和模 8 单位矛盾排除。不能只核对赋值而跳过这些单位约束。固定系数上界仍不能直接用于任意多位首部。

G14 剩余族的原整数恢复、消元二次式及其完整推导现在统一在 [G15](PROOF.md#a2-g15)。写 `z=10^E`，原解须有 `24z²/25<N<z²`、`z³≤a<21z³/20`、`5z<k<174z/31`，并保留逐块既约性；`k` 的素因子全部是 `1 mod4`。消元二次式必须恢复原整数 `a`，不能只找有理点或平方判别式就当成原解。

G15 的平方和商恒等式进一步要求 `S_E=816·100^E−31` 的每个 `3 mod4` 素因子偶深。模 `p,p²` 的四个完整周期给无界排除；例如 `E=6 mod9` 必须进一步满足 `E=96 mod171`。进入更深类仍可能有奇数赋值，不能当成通过全部范数约束。这里没有声称对所有模数都局部可解。

[F09](PROOF.md#a2-f09) 已完整排除 `E=3..12`：`E=4..12` 各有经完整试除验证的奇深素因子；`E=3` 通过平方和障碍，但在 612 个 gap 整数与独立 39,999 个原第二分子的两个完整窗口中均无平方判别式。该范围归约来自 G14/G15，不把有限计算外推到无界为空。

当前第一个保留指数是 `E=13`。它有精确允许投影 `816·100^13−31=83674539967313²+273127390353400²`。G16 证明在这一族的严格实数窗口内，分母 norm 条件已经是有理松弛可行性的充要条件，并实际恢复出一个 `E=13` 的有理非整数 word/sphere 点；因此继续只在有理数域强化同一消元/范数路线不能排除这一允许类。G16 同时把原解精确等价为两个整数未知量 `(N,k)` 的系统，第三分子及其既约性自动恢复。下一步应直接证明该整数系统对全部保留 `E≥13` 无点，或从整数局部条件得到新的全参数有效界。

全 A2 现在有两个清晰的整数前沿：两位有效数字的 `E≥13` 族须排除 G16 的双变量整数系统；至少三位有效数字的普通第二分母仍需联合原整数性、真实位数与逐块既约性。G07 的既约素数锁、G10 的 gap 高度及 G11 的支持锁都来自同一个 word/sphere 系统。G12 继续排除其中整除十进制权重的部分。仅合并同源局部模数、枚举有限个指数或证明渐近稀疏都不能关闭无界余核。

历史记录曾称 `b1=1` 已排除并把所有候选送入 deep-even，但仍缺连续证据；当前不采用这个结论。严格实数 prefix 窗本身允许 `(4/1,8/11,10/9)`，其原拼接比值 `4810/1119` 不等于欧氏长度，所以只是允许投影。G05 现已补齐第二分母二进主导时的初始 source 桥梁；`b1=2` 的此类进入 A2-01 chart，尾分母二进主导仍须独立处理。deep-even 的 `m2≥11` 联合整数系统尚未排除。

现行命题：[A2-G01](PROOF.md#a2-g01)、[A2-G02](PROOF.md#a2-g02)、[A2-G03](PROOF.md#a2-g03)、[A2-G04](PROOF.md#a2-g04)、[A2-G05](PROOF.md#a2-g05)、[A2-G06](PROOF.md#a2-g06)、[A2-G07](PROOF.md#a2-g07)、[A2-G08](PROOF.md#a2-g08)、[A2-G09](PROOF.md#a2-g09)、[A2-G10](PROOF.md#a2-g10)、[A2-G11](PROOF.md#a2-g11)、[A2-G12](PROOF.md#a2-g12)、[A2-G13](PROOF.md#a2-g13)、[A2-G14](PROOF.md#a2-g14)、[A2-G15](PROOF.md#a2-g15)、[A2-G16](PROOF.md#a2-g16)、[A2-F01](PROOF.md#a2-f01)、[A2-F02](PROOF.md#a2-f02)、[A2-F03](PROOF.md#a2-f03)、[A2-F04](PROOF.md#a2-f04)、[A2-F05](PROOF.md#a2-f05)、[A2-F06](PROOF.md#a2-f06)、[A2-F07](PROOF.md#a2-f07)、[A2-F08](PROOF.md#a2-f08)、[A2-F09](PROOF.md#a2-f09)、[A2-01](PROOF.md#a2-01)

历史证据：`uv run python main.py list sources --route a2-core`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="a2-endpoint"></a>
## 真实端点、source 与 prefix-gcd

路线 `a2-endpoint` · 状态：**待证**。移动前缀、原 numerator 与 sphere-height 的联合兼容。

保留 source linear Hensel、prefix resultant、真实 ellipse/window 和 denominator/height gcd 的路线。首批 finite-defect slots 不穷尽全部 eta；更深 endpoint lattice 与 moving prefix 仍需和原 sphere/word 联立。

下一结果必须控制真实长度、numerator remainder 和原既约恢复，或给出可审计的新绝对参数界；一个固定 prime 的刚性轨道不足。

现行命题：[A2-02](PROOF.md#a2-02)、[A2-03](PROOF.md#a2-03)

历史证据：`uv run python main.py list sources --route a2-endpoint`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="a2-transport"></a>
## 实际减向的有限四阶递推

路线 `a2-transport` · 状态：**待证**。terminal pool 外的供应与高阶饱和。

A2-05 采用 `F=U(J0−J),L=(R0−R)/K²` 的实际减向。四阶 `H4=26[27(X+Y)]^4−[55Y]^4`，strict terminal 必须 `(26/p)=+1`。有限 hierarchy 的各层属于同一 M，不能各算独立预算。

`pC=24303427940647` 的 H2/H3/H4 units、character 与第二层 lift 把四对象共同深度压到 1；进一步 recycling 只允许 exact triple saturation。该边界没有排除所有 deeper recycling。

现行命题：[A2-05](PROOF.md#a2-05)、[A2-06](PROOF.md#a2-06)

历史证据：`uv run python main.py list sources --route a2-transport`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="a2-fixed3"></a>
## fixed 3 与真实 contact

路线 `a2-fixed3` · 状态：**待证**。eta=2 的八型及更深 source cancellation。

当前严格初项是 a2-shallow f-unit depth 8 和全部 a3-shallow depth 12。odd spill 仍可来自 a2-shallow f-contact。eta=1 contact 已排除；eta=2 正 e3=1 只余八型：

| d | (cQ,kh) |
|---|---|
| 1 | (7,219),(31,51),(511,3),(523,3),(527,3),(539,3) |
| 2 | (103,3),(107,3) |

这张表不是全十进制候选集。更深 zero sheet 的 parity 仍需原 source 限制。

现行命题：[A2-07](PROOF.md#a2-07)、[A2-08](PROOF.md#a2-08)

历史证据：`uv run python main.py list sources --route a2-fixed3`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="a2-shared-primes"></a>
## 同源素数交集与 shared 7

路线 `a2-shared-primes` · 状态：**待证**。局部无限 lift 与全局 divisor / remainder / sphere。

A2-09 给实际 A3 支持、共同 saturation 的单层 11 上界及 q/GDelta 的 43/109 边界。实际 A3WqGDelta saturation 的 Bezout 常数为 `3^10·7·12569471`，不提供新的 independent budget。

source/height/descendant/outer 联立，eta=2 shared-7 剩 (31,51)、(527,3)，m=2 mod3；source chart 可无限 7-adic lift。真实 N3 上还存在 odd depth 3 的边界，故 7 可以承担 parity。不能误写成“shared 7 永远偶深”。

两型整数核有 `g|5^(3m−3)+cQ cu`。设 `B=5cQ,L=Bω+10cuT,E=ωg²kh/2−9cuT10^M`，则 `E−La2=cu a3`，`L>30cuT`，`1<a3/T<251/250`。因此 a2 是唯一 floor 代表，余数 `0<R<cuT/250,cu|R,a3=T+R/cu`。即使 `v2(g)=2` 分别给 m≥68/80，下界仍不成为绝对上界；divisor/remainder/sphere 兼容待证。

现行命题：[A2-04](PROOF.md#a2-04)、[A2-09](PROOF.md#a2-09)

历史证据：`uv run python main.py list sources --route a2-shared-primes`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="a2-height"></a>
## 相位、长度与高度预算

路线 `a2-height` · 状态：**待证**。需原十进制窗口的独立约束；局部刚性不足。

source Hensel、height Hensel 和 norm reciprocity 往往是同一原式的投影。继续追逐固定 quadratic characters 或机械 p-adic 加深只会得到唯一 exponent orbit；不能自动累积独立高度付款。

同一个 fixed target 的非有效序列定理必须保留作用域；移动 coefficient 的联合参数需要额外原约束。

现行命题：按相关主稿分支及来源审计，不设平行定理正文。

历史证据：`uv run python main.py list sources --route a2-height`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="a2-retired"></a>
## 撤回的加向 transport 与下降

路线 `a2-retired` · 状态：**失效/降级**。plus hierarchy、旧 6/10 初项、未保持 coefficient plane 的下降。

**失效/降级：旧加向 transport。** 实际 parent 与 Euclidean 项采用真实减向，旧代码却在近似点上加向。不能把它当成无关符号约定。相反 character 和依赖旧 sign 的 higher-order 链退出当前证明。

**失效/降级：旧 fixed-3 depths 6/10。** 正确 H2 的 source substitution 使旧 leading forms 为零；当前已经从真实 sphere/plane 重建 8/12。旧章节只在来源包里保留，不再作为定理。

**失效/降级：未保持 coefficient plane 的 Gaussian child。** 未证明其重新回到原 A2 decimal window 和逐块既约，不作为合法 descent。

现行命题：按相关主稿分支及来源审计，不设平行定理正文。

历史证据：`uv run python main.py list sources --route a2-retired`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="dd-model"></a>
## gcd-normal 原始 gap 系统

路线 `dd-model` · 状态：**待证**。普通 small gap 与 full-concat 同源 determinant。

DD-05 的 exact `v|H_sph` 与两个互素 d0/v readers 是真实原 parents。a<d0v 时 ordinary CRT 唯一；a≥d0v 时强迫 F−>Q²v³。两 readers 消去 H0 恰返回旧 source-gap determinant，不产生第二个 independent budget。

一位第三分母有 v=1 和 b3|10Q，仍没有关闭一般前缀的 ordinary 兼容族。

现行命题：[DD-01](PROOF.md#dd-01)、[DD-B02](PROOF.md#dd-b02)、[DD-05](PROOF.md#dd-05)

历史证据：`uv run python main.py list sources --route dd-model`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="dd-tail"></a>
## 低层尾分母与完整有限末端

路线 `dd-tail` · 状态：**有限证书**。逐项限定后缀、位数和赋值；不覆盖一般多位分母。

C09 排除后两分母一位的整个 DD 层。DD-04 另外排除 m2=2,b3=8 和 b3=4、n3≥2、n2+n3>3 的完整子层：八尾五个 denominator states、无长度预筛每种 reader 103,548,188 行；四尾通过合法整尺度转移。

DD-03 关闭一位偶尾 third-two-dominant；DD-07 关闭 unique-five-tail 且 m2≤2。未覆盖其它多位尾、prefix-two-dominant、五进 prefix 及 m2≥3；这些都不能由子层证书外推。

现行命题：[DD-02](PROOF.md#dd-02)、[DD-03](PROOF.md#dd-03)、[DD-04](PROOF.md#dd-04)、[DD-07](PROOF.md#dd-07)

历史证据：`uv run python main.py list sources --route dd-tail`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="dd-terminal"></a>
## corrected canonical terminal

路线 `dd-terminal` · 状态：**待证**。Z=1 mod4 的 ordinary small-gap 无界 joint family。

canonical t2=1,delta≤1/2 的无界序列最终 a<d0v，Z=3 mod4 的无界序列亦排除。但两个结果非有效，保留有限例外，不能据此启动一个声称覆盖全局的有限搜索。

真正余核是 Z=1 mod4 的 ordinary small-gap、joint suffix/gap/moving orientation/scale-free source。需要原 full-concat 的第二个独立 parent 或真正 oriented deterministic location。

现行命题：[DD-B01](PROOF.md#dd-b01)、[DD-06](PROOF.md#dd-06)、[DD-10](PROOF.md#dd-10)

历史证据：`uv run python main.py list sources --route dd-terminal`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="dd-entropy"></a>
## 共享预算与非循环稀疏计数

路线 `dd-entropy` · 状态：**已严格完成**。fixed delta0<1/2 的 sparse bound；稀疏不推出空。

安全枚举先固定 denominator/S-units/lengths，枚举 a2，再读取 gap 与 selected sheets，恢复 prefix。保留 `N_num≤10^(n2+o(S))`。与 denominator entropy 共用同一预算得

```math
N_{\rm term}(S;\delta_0)\le10^{(\delta_0/\lambda)S+o(S)},
\quad \delta_0<1/2,\quad\lambda=1.436294525872677\ldots.
```

这是已采纳的 sparse bound。指数正、参数无界，计数稀疏不推出空。

现行命题：[DD-08](PROOF.md#dd-08)

历史证据：`uv run python main.py list sources --route dd-entropy`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="dd-orientation"></a>
## chosen Gaussian sheets 与独立性

路线 `dd-orientation` · 状态：**待证**。移动 orientation；不能重复支付原 sphere/word。

完整 ordinary gap/word 字典已在 DD-09 统一。source-square 与 pair-max 两条 chosen sheets 的有效 period 必须保留 orientation。惯性 U/Z source prime 的 denominator norm 偶深度可由原 baseline 自动满足。

norm 只在指定 cyclotomic overlap 上有非零投影；其它 target primes 两 sheets 都为 units。W-free rationalization 有 JV>qV,KV>qV 的结构 no-go，删掉 orientation 不成为 second parent。

现行命题：[DD-09](PROOF.md#dd-09)

历史证据：`uv run python main.py list sources --route dd-orientation`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="dd-decimal"></a>
## noncanonical decimal / circular 成功支

路线 `dd-decimal` · 状态：**待证**。ordinary circular-lock 成功支与完整 moving-target control。

folding→Euclidean→合法完整十次幂 phase shifting 给 circular 半径界；failure-side 支付 F− 的下界。ordinary circular-lock 成功支仍需要额外原 full-concat/moving-target 约束。

omega 是 2/5 smooth，通常不是纯 10 次幂；只能抽出共同的完整 10-power，不能把 one-sided content 删除。

现行命题：按相关主稿分支及来源审计，不设平行定理正文。

历史证据：`uv run python main.py list sources --route dd-decimal`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="dd-retired"></a>
## 撤回的 root transfer 与循环计数

路线 `dd-retired` · 状态：**失效/降级**。fixed-denominator 联合 subexponential 与无条件 General-transfer。

**失效/降级：fixed-denominator Nnum=10^o(S)。** fixed gap 下 suffix 唯一、fixed suffix 下 gap 唯一，是互相条件化的两条陈述；不能串联为 joint family 唯一。当前采用先枚举 a2 的非循环修复，保留短 suffix entropy。

**失效/降级：unified discriminant root / General-transfer。** 原来源的条件与 root identification 不足，不能无条件作为一般 DD 的依赖。外部 SGR-9 只覆盖 frozen top-DD hypotheses。

**独立性审计。** 同源 Hensel、Gaussian norm 和 radius rewrite 仍只有原来的预算；循环/平方投影不增加独立 payer。

现行命题：按相关主稿分支及来源审计，不设平行定理正文。

历史证据：`uv run python main.py list sources --route dd-retired`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="a1-contact"></a>
## 原始 rational contact 与四层

路线 `a1-contact` · 状态：**待证**。固定前缀有限，前缀的并集仍无界。

A1 原系统为 `R=(P+theta r3)/(1+theta)`，其中 `P=C/(10^gQ)`，`1/(10Q)≤theta<1/Q`。固定 prefix 的 tail 可有限，但前缀并集无界。

四层 d=s1−g∈{−1,0,1,2} 已建立。P 的正确式是 `(1−lambda)10^k r1+lambda 10^(−g)r2`；低层不能套最高层 endpoint 半 gap。

现行命题：[A1-01](PROOF.md#a1-01)、[A1-02](PROOF.md#a1-02)

历史证据：`uv run python main.py list sources --route a1-contact`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="a1-top"></a>
## 最高层稳定区与放大边界

路线 `a1-top` · 状态：**待证**。低 radius significand、contact endpoint 和更深 surplus。

A1-04 的统一稳定区 N≤min(4g,2k) 由原 JS 整数 0<K<1 关闭，不是有限枚举。首 radius 壳的上 u 和首 contact 壁的低 u 已关闭，低 radius u、更深 amplified corridor、contact 上 u 仍保留。

contact endpoint 经真实 word/sphere 给 2/5 深度三分裂和相对盒，例如 m3<9g 或 m3<18g；这些依赖假设的相对界不提供 g 的全局上界。原投影兼容点和允许模九类应作为边界见证保留。

现行命题：[A1-03](PROOF.md#a1-03)、[A1-04](PROOF.md#a1-04)、[A1-05](PROOF.md#a1-05)

历史证据：`uv run python main.py list sources --route a1-top`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="a1-denominators"></a>
## balanced 深度与真实 numerator recovery

路线 `a1-denominators` · 状态：**待证**。一般 units、非 balanced 分母及高偶数纯等前缀。

balanced 指 v2(bi)=v5(bi)，unit 因子无界。g=0/1 的 unequal-prefix-depth 被排除；equal-prefix 的 delta>g、delta<g、delta=g 需分别使用真实 word 最浅项。delta=g+1 的 product 是 1/9 mod20，其它指定 strict 范围才是 11/19。

纯等前缀 balanced-tail 的完整供给是 j|10^(e+1)+1。g=0 奇数 e 排除后，e=2/4 证书闭合；现在余偶数 e≥6。g=1 首 strict delta=2 排除后，余偶数 e≥4、delta≥3。一般 units、非 balanced 分母、其它 g 仍无界。

原 gap recovery 保留 `a3=M[jZa1−(C+j)J]+F0V`。分母 (100,100,110000) 的 norm 是二平方和，但没有分子；该投影点被 e=2 真实 recovery 证书排除。

现行命题：[A1-K01](PROOF.md#a1-k01)、[A1-K02](PROOF.md#a1-k02)、[A1-K03](PROOF.md#a1-k03)、[A1-K04](PROOF.md#a1-k04)、[A1-K05](PROOF.md#a1-k05)、[A1-K06](PROOF.md#a1-k06)、[A1-K07](PROOF.md#a1-k07)、[A1-K08](PROOF.md#a1-k08)、[A1-K09](PROOF.md#a1-k09)

历史证据：`uv run python main.py list sources --route a1-denominators`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="a1-finite"></a>
## 固定层的完整证书

路线 `a1-finite` · 状态：**有限证书**。每份证书按实际假设审计；不拼成全局盒。

e=2：5050 prefix、219101 J，0 square；e=4：828814 prefix、262115848 J，1377 sieve survivors、0 square/root。e=4 Python 对每个 surviving projection 独立核对原 discriminant，C++ 保留整数宽度论证。

g=1,delta=2 的正确范围是 d=0,k≤7；d=1,k≤9。2566 prefix、30923 J 中有一个平方投影，两根分别非整数或 a3<0，不能把 square projection 叫原解。g=0 单位 prefix balanced-tail 为 855 prefix、161 J、0 square。

其它历史 fixed-layer 证书仅按原假设保全；没有重新把这些 bounded slices 组合成一个无界定理。

现行命题：[A1-F02](PROOF.md#a1-f02)、[A1-F04](PROOF.md#a1-f04)、[A1-F12](PROOF.md#a1-f12)

历史证据：`uv run python main.py list sources --route a1-finite`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="a1-moving"></a>
## moving-prefix / 深分母的剩余路线

路线 `a1-moving` · 状态：**待证**。joint source、word cut 与真实 integer gap。

moving-prefix、deep-denominator、source/word matching 的历史路线归入这里。minimal-diagonal 和 fixed-pair closure 不覆盖完整 A1；旧 k≥32 前沿只是历史阶段，后续子域结论按各自范围采纳。

下一步仍需联合控制真实前缀 cut、整数 gap、第三块位数/既约以及尚未关闭的 amplified 区域。每个 fixed prefix 有限不能给所有 prefixes 的统一绝对上界。

现行命题：按相关主稿分支及来源审计，不设平行定理正文。

历史证据：`uv run python main.py list sources --route a1-moving`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="a1-retired"></a>
## 撤回的尺度推广与漏条件

路线 `a1-retired` · 状态：**失效/降级**。LK17G、错误 recovery 符号、旧 r=1 漏 k≥g。

**失效/降级：LK17G 一般 g 的 d=1 角点。** 旧 Ptilde 漏掉第二项 10^(−g)，其正余量和后续预算不能用在 actual P。正确角点余量为

```math
\xi P^*-r_2^*=
\frac{10Z[2E-10^g(E+1)]+10E+1+1/E-10^{-g}}{Q+1}.
```

例如 g=e=1,k=3 为负；这反驳旧证明步骤，没有构造原 Exact Lift。g=0 的 LK17 仍有效，all-g d=2 只用正确正主项而不依赖 LK17G。

**失效/降级：错误 numerator recovery 符号。** 将 `[jZa1−(C+j)J]` 写反后推出的“整 d=1 关闭”和“d=0,k≥e+1”撤回。

**失效/降级：旧 r=1 缺 k≥g。** 旧 N=s 的 phase 上界缺条件；统一 JS 稳定区已经独立重建，不依赖漏条件范围。

现行命题：按相关主稿分支及来源审计，不设平行定理正文。

历史证据：`uv run python main.py list sources --route a1-retired`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="external-audit"></a>
## 外部材料的适用范围审计

路线 `external-audit` · 状态：**待证**。来源自身状态与本仓库采纳状态分开；frozen top-DD 不覆盖 DD。

来源仓库的 source status 不等于本仓库采纳状态。外部 proof fragments、integration audits 和 source certificates 均保留原 bytes。被采纳的公共 simplification 接入 C03；其它结果的 frozen chamber、word cut 与 orientation 假设不能删除。

SGR-9 只覆盖 frozen top-DD，不能升级成一般 DD 闭合。未保持真实 first-two decimal cut 的 ambient pseudo-family 同时满足多个投影，也仍不是原候选。

现行命题：按相关主稿分支及来源审计，不设平行定理正文。

历史证据：`uv run python main.py list sources --route external-audit`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

<a id="repository-history"></a>
## 环境与迁移记录

路线 `repository-history` · 状态：**已严格完成**。仅保存源码和组织沿革，不是数学证明。

2026-10-01 整体重写建立单一证明稿、单一路线记录和统一核对入口。原 196 个 Exact Lift Markdown、394 个核对源码及其它环境/外部材料全部按 bytes 保全；现行源码保留 26 个 Python 算术核对和 2 个 C++ 源文件。

重新组织不等于逐项重新证明历史材料。未进入当前命题链的原结果保留 original status、路线归属和完整源码，供按目标复查；不静默把它们改写为错误，也不让其旧 closure 名称覆盖当前主状态。

现行命题：按相关主稿分支及来源审计，不设平行定理正文。

历史证据：`uv run python main.py list sources --route repository-history`。记录按来源文件或 ledger 源条目检索，原状态与哈希保留。

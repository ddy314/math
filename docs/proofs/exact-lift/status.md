# 严格证明状态与后续工作

本文件对应原总稿 §§32–39，是 agent 判断证明状态的权威入口。

## 状态边界

当前严格状态是：主不存在性命题尚未完成证明；三个异常分支均有大量严格局部结论，但 `A_2`、DD、`A_1` 都仍有未闭合的无界核心。

## 2026-08-13 DD 合并状态

本节覆盖下方由 2026-08-10 原总稿机械拆分出的 DD 旧状态。完整命题、假设、推导与逻辑修正见
[double-deficit.md §27.33](branches/double-deficit.md#2733-2026-08-13-后续合并进展)。

- **`已严格完成`**：§27.33 的解析与局部算术推导证明 `n_3=8S_12-1` 整层为空，故 `n_3<=8S_12-2`；同时有 prefix-uniform 解析锥 `n_3<31S_12/4+6581/960`，以及 11 个固定 surplus modes。
- **`有限证书`**：`S_12=5,n_3=39,m_3=17,...,21` 的精确 Hensel--CRT / 判别平方证书为空，与已有的 `m_3=14,15,16,22,...,32` 证书合并后关闭整个该尺寸。
- **`已严格完成`（依赖经典外部定理，阈值非有效）**：固定目标 Schmidt Subspace Theorem 给出 `limsup m_3/S_12<=5` 与 `limsup_DD n_3/S_12<=6.308883577618...`。这些是渐近结论，不给出可计算的绝对 `S_12` 上界。
- **`已严格完成`（frontier 条件蕴含）**：若存在逼近 `6.308883...` frontier 的无界 DD 序列，则其位数比例、S-unit phase、rough cofactors 和 denominator imbalance 被压到唯一渐近形状；固定 moving Gaussian core `(C_L,Pi)` 后，`A_0`、`A_12` 与最后的 `q_c/R_2` lift 至多唯一。这些结论只在假想 frontier sequence 上使用。
- **`失效/降级`**：`g_*` 不是独立高度惩罚；terminal Pell-like cancellation 只是 prefix norm 的重写；继续单素数 Hensel、ordinary quadratic character 或重复 fixed-target Subspace Theorem 都不能当作新闭合步骤。
- **`待证`**：DD 全局空性、有效绝对界 `S_12<=S_0`、moving pair-max Gaussian core 的 uniform elimination，以及一般 projective/common-scale 与 5-adic angular allocation 仍未完成。

## 维护规则

这里的清单必须与三个分支文件同步。新增局部结论时，要说明它属于 `已严格完成`、`有限证书`、`待证` 或 `失效/降级` 哪一类。有限切片不能自动提升为 prefix-uniform 的全局结论。

## 研究优先级

原总稿建议的优先级是 DD 中低层 → `A_2` deep-even 的 resultant/Hensel 接触 → `A_1` saturated 的 coefficient-plane invariant。具体命题、公式和开放缺口见本文件的拆分正文。

> 迁移说明：以下正文由原始总稿机械拆分，公式和证明状态不作数学改写。
# 32. 早期“完整证明”为什么不能作为最终证明

研究过程中曾经形成过一版形式上已经把三个分支全部“关闭”的预印本框架。严格审计后发现，其中承担全局不存在性作用的若干步骤没有真正建立。

这些问题已经明确撤回，不能继续作为证明依据。

## 32.1 “完全共享分母结构已关闭”曾被无证明引用

如果每个素数在三个分母中的最高赋值都至少出现两次，可以严格得到

\[
b_1=q_0c_2c_3,
\]

\[
b_2=q_0c_1c_3,
\]

\[
b_3=q_0c_1c_2,
\]

其中 \(c_1,c_2,c_3\) 两两互素。

这个分解本身正确。

错误在于曾经从这里直接跳到“完全共享分母分支已经排除”。  
分解定理只描述结构，并没有自动导出与 exact balance 的矛盾。

后续研究通过更细 denominator prime graph、局部高斯匹配和分支正规化替代了这个未经证明的“总关闭”。

---

## 32.2 有限证书不能替代无界下降

早期 \(A_2\) 证明中曾经存在这样的逻辑：

1. 用计算排除一个有限盒子；
2. 宣称更高位候选会“下降”回该盒子；
3. 因而全局排除。

问题在于第 2 步没有给出保持以下所有性质的严格映射：

- 正性；
- 既约性；
- exact balance；
- 整数球面；
- 十进制位数；
- 同一 carrier 分支。

后续真正证明的 Gaussian flip 又不保持原十进制 coefficient plane，因此无法补上这条缺口。

现在有限证书只被用于已经先有严格参数上界的有限切片。

---

## 32.3 DD 中“素数同时进入 gap 与二平方和所以矛盾”不成立

曾经尝试认为某个独占最高素幂同时进入

\[
H-y_3
\]

和

\[
y_1^2+y_2^2
\]

会与二平方定理冲突。

这是错误的。

二平方定理对

\[
p\equiv3\pmod4
\]

只要求它在二平方和中的总赋值为偶数，并不禁止它同时整除一个因子 \(H-y_3\)。

因此 DD 后来必须转向更精细的：

- unique-max denominator graph；
- \(e_1=e_2<e_3\)；
- exact \(p\)-adic capacity；
- near-square；
- resonance；
- near-\(S\)-unit。

---

## 32.4 \(A_1\) 中“两个 gap 尺度不相容”的文字论证不够

早期 \(A_1\) 终端论证曾使用：

- 远 gap；
- 第二个独立 gap；
- cyclotomic kernel；
- 尺度不相容；

但没有给出一个可以逐行核验的矛盾，例如

\[
v_p(X)\ge A
\quad\text{且}\quad
v_p(X)\le A-1,
\]

或

\[
0<T<M\le T.
\]

因此该“terminal incompatibility”没有成立。

后续真正可靠的结果是薄环、尾商斜率、统一 tail quadratic、saturated tail bound 与 denominator-only 奇素数锁。

---

# 33. 后来被严格判死或降级的证明路线

## 33.1 \(A_2\to A_1\) 的 Vieta jumping

关于第三坐标的二次方程确实有 companion root。

但在相邻 \(A_2\) 中可以证明 companion 第三坐标全局为负。

做符号反射后虽然得到更小的正坐标

\[
\widehat r_3<r_3,
\]

甚至有精确差值

\[
r_3-\widehat r_3
=
\frac{
20GP
}{
Q(\kappa+2G)
},
\]

但反射后的点不再满足原十进制 coefficient plane。

所以没有合法的

\[
\text{正根}\to\text{更小正根}
\]

Vieta jumping。

---

## 33.2 反复 Gaussian flip

对 \(L>1\)，flip 确实把球面因子中的 \(L\) 从一侧移到另一侧。

然而十进制平面系数会多出 \(L\)，因此一次 flip 后就离开原族。

对 saturated \(L=1\)，flip 又退化为 projective identity。

所以两个极端都无法形成传统无限下降。

---

## 33.3 Source-only Legendre/Jacobi 全局乘积

曾经尝试把所有 source prime 的二次剩余条件相乘，希望得到全局 \(-1\)。

严格整理后发现各项之间存在结构性抵消，最终只得到

\[
\boxed{
1=1.
}
\]

这说明 source-only quadratic character 没有利用到真正关键的十进制相位信息。

---

## 33.4 Generic \(u_0,c_u,\rho\) 二次剩余追逐

大量模素数条件在已知 Gaussian norm / source split 下自动满足。

继续逐个做 Legendre symbol 只会重复已有局部 norm 条件，不能控制十进制 coefficient plane。

因此该路线被降级。

---

## 33.5 “模数大于区间”只给唯一性，不给空性

如果一个变量 \(R\) 满足 CRT 且

\[
0<R<D,
\]

而模数 \(M>D\)，只能推出区间内至多有一个候选。

这只是

\[
\boxed{
\text{at most one},
}
\]

因此无法推出

\[
\boxed{
\text{zero}.
}
\]

真正还需要证明唯一代表不能满足 Gaussian divisor、窄实数窗口或平方条件。

---

## 33.6 普通 class group / genus / Hasse norm

外部系数本身已经满足大量全局 norm 条件。

单独使用 genus theory 或普通 Hasse norm obstruction 没有直接抓住十进制 coefficient plane。

class group 中某个小 ideal class 也可能被 source-side prime 补偿。

因此这些工具目前只可能作为辅助，不适合做主路线。

---

## 33.7 Scalar descent

曾经构造过一个线性变换 \(\mathcal M\)，但它满足

\[
\mathcal M^2=-\mathfrak d I.
\]

也就是说两步变换只回到原向量的标量倍数。

这种结构属于有限阶/projective 对称，无法形成无限下降。

---

## 33.8 错误的 odd-inert 推断

曾一度从

\[
E_1+\mathcal K
=
R_*(A_0^2+C_0^2)
\]

以及某个 \(p\equiv3\pmod4\) 在 \(E_1\) 中奇次出现，直接推断

\[
p\mid a_1.
\]

这是无效的，因为赋值可能出现类似

\[
3+1=4
\]

的普通加法抵消。

因此曾经由此得到的“某些 core 已全局关闭”“所有 odd inert prime 必来自固定 core”等说法已经撤回。

真正留下来的结构是 odd inert excess 三分法与 source 双 Hensel 接触。

---

# 34. 有限计算在完整证明中的正确角色

有限计算目前有三种用途。

### 34.1 验证严格有界切片

例如 \(A_2\) deep-even 中

\[
m_2\le10
\]

已经可以用纯整数模平方证书排除。

只要候选范围本身先由严格数学推导得到，这类计算可以成为证明的一部分。

### 34.2 诊断无界参数空间的实际稀疏程度

例如更高 \(m_2\) 层的 denominator recovery 过滤，可以告诉我们哪些理论约束最有杀伤力，从而决定下一步该证明哪个统一引理。

这类结果是研究导航，不应写成全局定理。

### 34.3 为最终有限余项提供证书

最理想的全局证明不一定需要纯手工排除所有小参数。

如果能够先证明

\[
S_{12}\le S_0
\]

或

\[
m_2\le M_0,
\]

那么剩余有限范围完全可以由可复核的整数程序关闭。

因此目标不应执着于“完全不用计算”，而应要求：

\[
\boxed{
\text{无限族必须先被理论上统一压成有限族。}
}
\]

---

# 35. “固定前缀有限”与“全局空”之间的逻辑门槛

这是整个项目中最重要的方法论教训之一。

在 \(A_2\) 中，固定前两块后第三块可以被平方判别和 recovery 压成有限集合。

在 DD 中，固定 ghost \((y_1,y_2)\) 后

\[
La\mid y_1^2+y_2^2
\]

使第三坐标只有有限候选。

在 \(A_1\) 中也存在相同的逐纤维有限化。

但如果前缀参数

\[
m_2,\ a_2,\ b_2
\]

或 ghost

\[
y_1,y_2
\]

仍然无界，那么

\[
\bigcup_{\text{所有前缀}}
\text{有限候选集}
\]

仍可能是无限集合。

因此以下推理是无效的：

\[
\forall P,\quad
\#F(P)<\infty
\quad\Longrightarrow\quad
\bigcup_PF(P)
\text{ 有限}.
\]

真正需要的是某种 **prefix-uniform** 结论：

\[
\boxed{
\text{统一高度上界、统一矛盾、或保持原问题族的严格下降。}
}
\]

目前主定理仍开放，正是因为这最后一层还没有完全建立。

---

# 36. 当前严格证明状态

截至本文整理时，可以可靠写成以下状态。

## 36.1 已严格完成

1. exact lift 的十进制正权平均重写；
2. carrier 原理；
3. 正常位数区域排除；
4. 三异常分支穷尽；
5. 整数球面提升；
6. primitive recovery；
7. denominator prime graph 的主要全局结构；
8. 第三块公共尾商正规化；
9. 统一整数尾权 \(\kappa\)；
10. 统一二次式和平方判别式；
11. primitive tail quadratic；
12. \(10^\ell\mid\kappa^2(\kappa+2G)\)；
13. 三分支线性 denominator-tail cone；
14. 完整高斯共轭匹配的局部结构；
15. 高斯 flip 不保持十进制 coefficient plane；
16. \(A_2\) 相邻边界区
    \[
    (s_2,s_3)=(-1,1);
    \]
17. \(A_2\) deep-even 终端通道；
18. \(a_1=3\) 全局排除；
19. \(A_2\) 的 source split、Hensel 商、五进同步与 factor allocation；
20. \(A_2\) 的 prefix defect、odd inert excess 与 source 双 Hensel 系统；
21. \(A_2\) 的有限切片
    \[
    m_2\le10
    \]
    排除；
22. DD 的公共商正规化；
23. DD 的 surplus simplex；
24. DD 的 near-square gap；
25. DD 的
    \[
    d_3\le5S_{12};
    \]
26. DD 顶部 \(2/5\)-adic 双 resonance；
27. DD near-\(S\)-unit 化；
28. DD 极端 denominator 不对称；
29. DD 最大 denominator-tail 层排除；
30. DD 拼接行列式 gap 的精确赋值恒等式；
31. DD 双 resonance 终端尖角
    \[
    10S_{12}+11\le n_3\le11S_{12}+3
    \]
    的全排除；
32. DD 的五进正规形先给出中间上界
    \[
    n_3
    <
    \left(5+3\log_5 10\right)S_{12}
    +\frac32\log_5 10;
    \]
33. DD 中高层的奇偶锁 \(10\mid b_3\)、唯一五进正规形与超深五进单位抵消；
34. DD 中高层的二进非 resonance 锁 \(\Delta_2>0\) 与三条二进正规形；
35. DD 二进主导项锁
    \[
    v_2(\kappa)=v_2(G)+1
    \]
    及整个单五进 resonance 中高层的排除；
36. DD 此前的全局相对界
    \[
    n_3\le8S_{12};
    \]
37. DD 阈值以下的上层
    \[
    n_3\ge(5+2\log_5 10)S_{12}+\log_5 10
    \]
    被压成唯一五进 resonance 正规形或 \(\Delta_5>0\)；
38. DD 五进入口以上的整个 \(\Delta_5>0\) 支已经排除；其中
    \[
    v_5(\kappa)=v_5(G)
    \]
    由 \(v_5(\kappa+2G)\) 的高度排除，而
    \(v_5(\kappa)>v_5(G)\) 由 primitive recovery 强制
    \(v_5(F_-)=v_5(\kappa)>n_3\) 后排除；
39. DD 上层 resonance 的加权赋值惩罚
    \[
    n_3
    <8S+6+\log_{10}2-\log_{10}\Xi,
    \qquad
    \Xi\ge2,
    \]
    以及最高整数层 \(\Xi\in\{2,16\}\) 的终端正规形；
40. DD 最高整数层
    \[
    n_3=8S_{12}+5
    \]
    已按三个二进位置全部排除；\(t_2=1\) 最终只需关闭
    \((S,m_3)=(4,17),(5,21)\) 两个严格推出的尺寸，均由
    \(\kappa>10QG\) 矛盾排除；
41. DD 入口以上、\(b_3\) 二进主导且 \(t_2\ge2\) 的无界
    resonance 子锥满足
    \[
    n_3\le8S_{12};
    \]
    当前最高剩余层 \(n_3=8S_{12}+4\) 因而只能落入 \(t_2=1\)，
    先压成十个 \((S,m_3)\) 尺寸及统一极端前缀位数形状，再由
    225 个赋值元组及其有界余因子区间的有限证书全部排除；
42. DD 的一般余因子区间证书不再依赖极端位数形状，并连续排除
    \[
    n_3=8S_{12}+3,\qquad n_3=8S_{12}+2;
    \]
    两层分别压成 32、59 个尺寸和 2677、14095 个赋值元组，所有
    余因子区间均无幸存者；
43. DD 的 \(n_3=8S_{12}+1\) 层已经全部排除：\(S\ge4\) 的
    86 个尺寸和 48808 个赋值元组只留下 \((S,m_3)=(5,16)\)
    的一个余因子，它固定 \((b_1,b_2)=(768,97)\) 后使
    near-square 判别式模 \(3\) 为非平方；\(S=2,3\) 则由严格
    分扇区归约压成 618、39710 个 denominator-tail 元组，最终
    2、8 个统一判别式均由有限证书验证为非平方；
44. DD 新边界 \(n_3=8S_{12}\) 的入口上部分已经分解：
    \(S\ge11,t_2=1\) 被压成 70 个尺寸和 51828 个赋值行，精确
    floor-sum 余因子证书没有幸存者；\(t_2\ge2\) 则严格强制
    \[
    m_3=3S,\quad d_3=5S,\quad
    \kappa=10^{2S}c,\quad1\le c\le8,
    \]
    并有极端前缀位数形状与 \(10^{S-3}\mid b_3\)。后者仍是八个
    无界族，不是八个有限候选；
45. 上述八个无界核也已由 \(F_-=10^{2S}\rho\)、\(0<\rho<20000\)
    和精确大除数
    \[
    \frac{c10^{2S}+2G}{\gcd(c10^{2S},G)}\mid\rho Q
    \]
    全部排除。八核固定赋值给出
    \(\gcd(c10^{2S},G)/c\le128\)，使整除式两侧的
    \(10^{2S}\) 与 \(10^S\) 增长率矛盾。因此
    \(n_3=8S\Rightarrow S\le10\)，并且 \(S\ge11\) 时
    \(n_3\le8S-1\)；
46. 在 \(4\le S\le10,n_3=8S\) 的 \(b_3\)-二进主导、
    \(t_2=1\)、唯一五进正规形子支中，56 个尺寸的 97693 个赋值行
    先压到 3121 个同步 \(F_-\) 行和 113 个余因子对；真实分母分解
    只剩 \((b_1,b_2)=(768,97)\) 的一个尾核，并由 near-square
    模 3 非平方排除；
47. 同一唯一五进正规形的 \(t_2\ge2\) 子支在 \(S\ge7\) 已由大除数
    无界矛盾排除；\(S=4,5,6\) 的 129600、1296000、12960000 个
    有序真实分母块也在局部预算、尾区间与大除数条件后没有幸存者。
    因此该五进正规形在 \(4\le S\le10\) 的 \(b_3\)-二进主导位置
    全空；其他入口下五进状态仍待证；
48. DD 的整个 \(n_3=8S\)、\(S\ge4\) 等号层已经排除：若
    \(5\mid b_3\)，位数下界自动恢复 \(e_5=q_5\)，resonance、
    \(\Delta_5<0\)、\(\Delta_5>0\) 三态分别由唯一正规形、高度与
    primitive recovery 排除；若 \(5\nmid b_3\)，尾权强制
    \(\kappa=2\cdot5^{3S}\)，最终三个二进剩余类均超过真实
    \(G\) 上界。因此
    \[
    n_3=8S\Longrightarrow S\in\{2,3\},
    \qquad
    S\ge4\Longrightarrow n_3\le8S-1;
    \]
49. DD 的剩余 \(S=2,3,n_3=8S\) 等号层也已关闭。non-dominant
    扇区分别强迫 \(m_3\ge14,21\)，但 primitive denominator-tail
    核在 \(m_3=10,17\) 后已经为空，因此无需枚举无界 prefix
    surplus。dominant 扇区的 1527、72092 个 tail rows 经二进位置、
    两素数三状态、既约性与 squarefree gap 后，分别只需检查 703、
    38633 个统一判别式；精确整数平方根证书验证全部非平方。因此
    \[
    n_3=8S_{12}\text{ 整层为空},
    \qquad
    n_3\le8S_{12}-1;
    \]
50. DD 的 denominator-tail 界已对全部 \(S\ge2\) 加强为
    \(m_3\le6S+2\)，从而 non-dominant 扇区统一满足
    \(n_3\le7S+2\)。新的最高允许层 \(n_3=8S-1\) 因而全部
    dominant；在 \(S\ge18\) 的五进 resonance 区，\(t_2\ge2\)
    被压成 19、9、0 个常数核并由大除数矛盾排除，\(t_2=1\) 则压成
    45 个尺寸、15525 个 valuation rows，并由 floor-sum 余因子证书
    全部排除。因此
    \[
    n_3=8S-1\Longrightarrow S\le17,
    \]
    该层已经成为真正有限的原问题切片，但其最终空性仍待核验；
51. DD 的 \(n_3=8S-1\) 层中 \(S=2,3\) 两个最小尺寸已经由有限
    证书排除：dominant 尾核分别有 2665、126669 行，全部有界前缀
    经二进位置、两素数三状态、既约性与 squarefree gap 后产生
    24396、1582338 个非负统一判别式，精确整数平方根检查全部非平方。
    因此在处理下一个尺寸以前，最高层先缩为
    \[
    n_3=8S-1,\qquad4\le S\le17;
    \]
52. 对任意 DD 候选，\(F_-\)、primitive recovery 与正拼接 gap
    还给出不依赖 resonance 的精确大除数
    \[
    \frac{\mathfrak L_F}{\gcd(\mathfrak L_F,Q)}\mid F_-,
    \qquad
    \mathfrak L_F=
    \frac{\kappa(\kappa+2G)}
    {\gcd(\kappa(\kappa+2G),\kappa+G)}.
    \]
    在最高层的 \(S=4\) 切片中，squarefree gap 先把最低尾长
    \(m_3=11,12,13,14\) 压成 1、3、7、13 个有序位数形状；四个完整
    有限证书最终检查 694825、10987773、714489、99342 个大整数
    判别式幸存者，全部非平方。
    余下 \(m_3=15,\ldots,21\) 由流式 C++ 精确枚举检查
    14150484、9828、8792、112243、70、1887、0 个 valuation-tail
    判别式，最终整数平方数都为零；\(m_3=22,\ldots,26\) 的 primitive
    denominator-tail 核逐层为空。因此
    \[
    S=4,\quad n_3=31\Longrightarrow\text{无 DD 候选},
    \]
    当前最高层只剩
    \[
    n_3=8S-1,\qquad5\le S\le17.
    \]
    这仍是明确有界的有限证书，不关闭更低无界层；
53. DD 最高层的 \(S=5,n_3=39\) 尺寸中，完整流式证书先排除
    \(m_3=22,\ldots,26\)：五层的 136692、23052、3742、401、35 个
    primitive tail rows 最终没有平方判别式；\(m_3=27,\ldots,32\)
    的 primitive denominator-tail 核逐层为空。第 27.30 节又证明
    \(m_3=14\) 的唯一位数形状在四角、valuation box、通用
    \(F_-\) 大除数与二/五进单位性盒后只剩 75 条 primitive tails；
    全部 7930779 个 squarefree-gap 前缀都不满足完整两素数三状态。
    第 27.31 节再以三个严格位数形状的完整流式证书排除 \(m_3=15\)：
    五类必要过滤后分别剩 1404、17、5499 条 primitive tails，所有
    多精度精确判别式仍无平方。第 27.32 节同样排除 \(m_3=16\) 的
    七个严格位数形状：141826212 个 valuation-tail pairs 最终没有
    精确平方判别式。因此这个尺寸只剩
    \[
    17\le m_3\le21,
    \qquad18\le d_3\le22.
    \]
    这仍是明确有界的有限证书，没有关闭整个 \(S=5\) 尺寸；
54. \(A_1\) saturated 支的 denominator-only 尾长界；
55. \(A_1\) saturated 非十进制奇素数只能来自 \(G\) 且为 \(1\bmod4\)。

---

## 36.2 尚未完成

\[
\boxed{
A_2\text{-only 尚未全局关闭}.
}
\]

\[
\boxed{
DD 尚未全局关闭.
}
\]

\[
\boxed{
A_1\text{-only 尚未全局关闭.
}
\]

因此

\[
\boxed{
\text{主不存在性定理尚未完成证明}.
}
\]

---

# 37. 三个分支的剩余核心

## 37.1 \(A_2\)

真正开放的是

\[
\boxed{
m_2\ge11
}
\]

下 deep-even 终端系统的统一空性。

局部素数追逐已经基本耗尽，继续方向应集中在：

\[
\boxed{
\text{source 双 Hensel}
+
\text{十进制窄窗口}
}
\]

以及

\[
\boxed{
\text{Gaussian ellipse}
+
\text{真实 }2/5\text{-adic phase}.
}
\]

---

## 37.2 DD

原先的双 resonance 顶部

\[
10S_{12}+11
\le n_3\le
11S_{12}+3
\]

已经排除；其下方原本可能只发生五进 resonance 的整个中高层

\[
d_3=\max(s_1,s_2,d_3),
\qquad
n_3\ge9S_{12}+2
\]

也已由二进主导项与球面差分排除。继续把五进入口以上的
primitive recovery 代回 \(F_-\) 后，整个 \(\Delta_5>0\) 支也被排除；再保留 resonance 正规形中的完整前缀赋值并恢复 \(F_-\) 上界的精确常数后，先得到中间上界

\[
\boxed{
n_3\le8S_{12}.
}
\]

但 DD 仍未全局关闭：\(d_3\) 非 dominant 扇区与五进 resonance 阈值下的 dominant 扇区仍可随 \(S_{12}\) 无界增长。后一区域的上层

\[
n_3\ge
(5+2\log_5 10)S_{12}
+\log_5 10
\]

已进一步只剩唯一五进 resonance 正规形；\(\Delta_5<0\) 与
\(\Delta_5>0\) 均已排除。

入口以上唯一可随 \(S\) 无界的二进主导 \(t_2\ge2\) 子锥还满足加权界

\[
n_3
<8S+6+\log_{10}2-\log_{10}\Xi,
\qquad
\Xi\ge2.
\]

此前可能达到的整数层 \(n_3=8S+5\) 已进一步按三个二进位置全部排除；其中 \(t_2=1\) 只退化到

\[
(S,m_3)=(4,17),(5,21),
\]

并由两处 resonance 的整数高度预算直接排除。

进一步保留加权 \(m_3\) 界中的 \(\Xi\) 后，入口以上的
\(t_2\ge2\) 子锥实际上整体满足

\[
n_3\le8S.
\]

因此新最高层 \(n_3=8S+4\) 只能来自 \(t_2=1\)。未粗化的
small-factor 比例把该层压成统一的极端位数形状，并只留下

\[
\begin{aligned}
(S,m_3)\in\{&
(3,13),(4,16),(5,19),(5,20),\\
&(6,23),(6,24),(7,27),(7,28),(8,31),(9,36)
\}.
\end{aligned}
\]

对这些尺寸继续保留
\(v_2(\kappa)=v_2(G)+1\)、\(v_5(\kappa)=k_5\) 的精确余因子后，
combined-height 只留下 225 个赋值元组；每个元组要求一个显式短区间
包含指定奇数倍的 \(2^h\)，而有限整数证书验证所有区间均为空。因此
\[
n_3=8S_{12}+4
\]
已经严格排除。该有限证书只关闭这个先经符号推导有界化的层，不覆盖
更低的无界区域。

把同一余因子方法改用一般界 \(G<10^S\) 后，不再需要极端位数形状。
层 \(n_3=8S+3\) 与 \(n_3=8S+2\) 分别被压成 32、59 个尺寸及
2677、14095 个赋值元组；对应的一般余因子区间证书仍无幸存者。因此

\[
n_3=8S_{12}+3,\qquad n_3=8S_{12}+2
\]

也已严格排除；在这一阶段界为 \(n_3\le8S_{12}+1\)。这些有限证书只覆盖
已经由符号不等式给出 \(S\) 上界的两个明确层。

对新最高层 \(n_3=8S_{12}+1\)，\(S\ge4\) 的入口以上部分也已
排除：一般余因子证书在 86 个尺寸、48808 个赋值元组中只留下
\((S,m_3)=(5,16)\)；它进一步固定
\((b_1,b_2)=(768,97)\)、\((s_1,s_2)=(-2,4)\)，并使 near-square
判别式满足 \(Y^2\equiv2\pmod3\)，矛盾。对入口另一侧的 \(S=2,3\)，
非 \(d_3\)-dominant 扇区先由改进界 \(n_3\le7S+3\) 压到唯一
\(S=2,m_3=15\) 取等锥，并被统一尾整除直接排除。dominant 部分的
denominator-tail 核分别有 618、39710 个元组；二进位置与强制
resonance、五进三分支和全部有界前缀把它们压到 114、27 个
tail-prefix 组合，squarefree gap 最终只剩 2、8 个统一判别式。
有限证书以精确整数平方根验证十个判别式均非平方。因此整个
\(n_3=8S_{12}+1\) 层已排除，并在这一阶段给出全局相对界
\[
\boxed{n_3\le8S_{12}.}
\]

这一有限证书只覆盖两个已由 \(S=2,3\) 固定的入口边界，不覆盖
\(n_3\le8S\) 的无界区域。

在新的等号层 \(n_3=8S\) 上，第 27.17 节已经进一步处理入口上的
\(S\ge11\) 部分。非 \(b_3\) 二进主导位置被严格排除；\(t_2=1\)
被压成 70 个尺寸和 51828 个赋值行，并由精确模计数证明余因子幸存数
为零。\(t_2\ge2\) 则被严格压成

\[
m_3=3S,\qquad d_3=5S,
\]

统一极端前缀位数形状，以及

\[
\kappa=10^{2S}c,
\qquad c\in\{1,2,3,4,5,6,7,8\},
\qquad 10^{S-3}\mid b_3.
\]

第 27.18 节又恢复

\[
F_-=10^{2S}\rho,
\qquad0<\rho<20000,
\]

并从 \(F_-\)、primitive recovery 与拼接 gap 的两个
\(\mu/\nu\) 表达式导出

\[
\frac{c10^{2S}+2G}{\gcd(c10^{2S},G)}\mid\rho Q.
\]

八核的固定 \(2,5\)-赋值给出
\(\gcd(c10^{2S},G)/c\le128\)，所以该整除要求
\(10^S<2560000\)，与 \(S\ge11\) 矛盾。故八个无界核已经全部
关闭，并有

\[
n_3=8S\Longrightarrow S\le10,
\qquad
S\ge11\Longrightarrow n_3\le8S-1.
\]

在这一中间阶段，全局统一界仍是 \(n_3\le8S\)：这里只把等号层压到
有限 \(S\)-列表，并未自动得到完整有限候选盒；而 \(n_3<8S\) 仍可
随 \(S\) 无界增长。

在该小切片中，第 27.19–27.20 节又关闭了
\(4\le S\le10\) 的 \(b_3\)-二进主导、唯一五进正规形：
\(t_2=1\) 由 56 个尺寸、97693 个赋值行、113 个余因子对与唯一
模 3 尾核的有限证书排除；\(t_2\ge2\) 在 \(S\ge7\) 由无界
大除数矛盾排除，在 \(S=4,5,6\) 由真实分母块有限证书排除。

第 27.21 节随后关闭了这些剩余状态。对 \(S\ge4\)，dominant 位数
下界在 \(5\mid b_3\) 时自动恢复 \(e_5=q_5\)，从而五进
resonance、\(\Delta_5<0\) 与 \(\Delta_5>0\) 分别由唯一正规形、
单因子高度和 primitive recovery 排除。\(5\nmid b_3\) 时，尾权只
可能为 \(2\cdot5^{3S}\)；\(S\ge7\) 直接违反尾高度，\(S=4,5,6\)
则要求一个超过真实 \(G\) 上界的二进剩余类。因此

\[
n_3=8S\Longrightarrow S\in\{2,3\},
\qquad
S\ge4\Longrightarrow n_3\le8S-1.
\]

第 27.22 节没有把这两个固定 \(S\) 直接当成完整有限盒。它先证明
non-dominant 扇区强迫 \(m_3\ge14,21\)，再用 denominator-tail
整除核在 \(m_3=10,17\) 后为空来排除，完全不截断无界 prefix
surplus。dominant 扇区才由 \(s_1+s_2\le2\) 有限化；1527、72092 个
tail rows 最终产生 703、38633 个非负统一判别式，精确整数平方根
检查全部非平方。因此当前严格相对界是

\[
\boxed{n_3\le8S_{12}-1.}
\]

第 27.23 节又把 denominator-tail 界统一加强为 \(m_3\le6S+2\)，
故 non-dominant 扇区现在满足 \(n_3\le7S+2\)。在最高允许层
\(n_3=8S-1\)，\(S=2,3\) 的 non-dominant 尾核也直接为空，所以
整层全部 dominant。五进入口以上的 \(S\ge18\) 只剩 resonance；
其中 \(t_2\ge2\) 的 28 个常数核被统一大除数排除，\(t_2=1\) 的
45 个尺寸、15525 个 valuation rows 则由精确 floor-sum 余因子证书
排除。于是

\[
\boxed{
n_3=8S-1\Longrightarrow
d_3=\max(s_1,s_2,d_3),\quad S\le17.
}
\]

第 27.24 节又对其中 \(S=2,3\) 作了完整有限核验。2665、126669 个
dominant tail rows 最终只需检查 24396、1582338 个非负统一判别式，
精确整数平方根证书全部非平方。因此当前最高层只剩

\[
\boxed{n_3=8S-1\Longrightarrow4\le S\le17.}
\]

第 27.25–27.28 节建立了一个不要求 resonance 或五进入口的通用
\(F_-\) 大除数，并逐尾长关闭下一个尺寸。对 \(S=4,n_3=31\)，
最低四个尾长 \(m_3=11,12,13,14\) 的 squarefree gap 分别只允许
1、3、7、13 个有序位数形状；二进位置、两素数三状态、精确二次区间
枚举与统一判别式证书最终没有平方。余下 \(m_3=15,\ldots,21\)
由固定全量计数的 C++ 流式精确证书排除；\(m_3=22,\ldots,26\)
的 primitive denominator-tail 核为空。因此当前严格结论已加强为

\[
\boxed{
S=4,\quad n_3=31
\Longrightarrow
\text{无 DD 候选},
\qquad
n_3=8S-1\Longrightarrow5\le S\le17.
}
\]

这仍不是 DD 空性，因为最高层的 \(5\le S\le17\) 与更低层都尚未
关闭，后者还可随 \(S\) 无界增长。

第 27.29–27.32 节又处理下一个尺寸的高尾与最低三个尾层。在
\(S=5,n_3=39\) 中，
\(m_3=22,\ldots,26\) 的完整 128 位流式前缀证书没有平方判别式，
\(m_3=27,\ldots,32\) 的 primitive tail 核为空；\(m_3=14\) 的唯一
位数形状则由 75 条 primitive-tail 小核与完整两素数状态证书排除；
\(m_3=15,16\) 的三个与七个严格位数形状也由完整多精度判别式证书排除。
故该尺寸当前只剩

\[
\boxed{17\le m_3\le21,\qquad18\le d_3\le22.}
\]

这同样没有改变 DD 更低层的无界性。当前在最高层应先继续关闭
\(S=5\) 的其余五个尾长，再推进 \(6\le S\le17\)，并同时在更低层
寻找可送入

\[
(\mathcal R-r_3)(\mathcal R+r_3)
=
\frac{\mathcal N_{12}}{G^2}
\]

的唯一主导项；目标仍是绝对高度界或直接矛盾。

---

## 37.3 \(A_1\)

有效尾长已经受

\[
\ell\le3(m_1+m_2)+1
\]

控制。

真正最危险的是 saturated \(L=1\) 中可能继续无界的 decimal shift

\[
\boxed{
g.
}
\]

Gaussian descent 在这里完全失效。

需要寻找一个新的 coefficient-plane invariant 或直接的 decimal-shift 高度界。

---

# 38. 推荐的全局攻关顺序

## 第一优先级：关闭五进 resonance 阈值以下的 DD

第 27 节已经关闭双 resonance 顶部及其下方整个单五进 resonance 带，
并把当前最高层 \(n_3=8S-1\) 压成 \(5\le S\le17\) 的 dominant
有限盒。
下一步需同时面对这个有限盒，以及

\[
n_3\le8S_{12}-1
\]

内更低的两个无界区域：non-dominant 扇区
\(n_3\le7S+2\)，以及尚未达到五进 resonance 强制阈值的 dominant
扇区；后一区域仍可能自发发生 resonance。

建议把全部力量放在

\[
\mathcal N_{12}
=
X_0^2+\varepsilon^2
\]

的 near-square 结构与

\[
\kappa(
\kappa K_{C,D}
-
2GQ^2\mathcal N_{12}
)
=
W^2
\]

之间。

具体应尝试：

1. 从最高层的 \(5\le S\le17\) 继续使用精确二次区间、两素数状态、
   通用 \(F_-\) 大除数与统一判别式，避免直接枚举不可行的十进制
   全盒；
2. 对五进入口以下的 resonance、\(\Delta_5>0\) 与 \(\Delta_5<0\) 分别做 \(\kappa\) 相对 \(G\) 的超距分类；入口以上只保留 resonance；
3. 把每一类中 \(\mathcal R-r_3\) 与 \(2r_3\) 的赋值差写成显式线性式，寻找像第 27.5 节那样唯一主导的球面因子；
4. 对 \(n_3\le8S-2\) 中仍可无界增长的真实块继续保留
   \(Q,G,\mathcal N_{12}\) 与 short
   numerator block，给出
   \[
   |\varepsilon|/X_0
   \]
   的指数级上界；
5. 把判别核围绕 \(\mathcal N_{12}=X_0^2\) 展开，并寻找最近的候选整数平方中心 \(W_0^2\)；
6. 证明真实值与 \(W_0^2\) 的非零偏差小于相邻平方间距；
7. 如果最终只得到
   \[
   S_{12}\le S_0,
   \]
   则用有限证书关闭剩余层。

near-square 路线仍可用来给 \(E\) 或 \(F_-\) 提供绝对值上界，但不应再以已排除的 resonance 带为目标。新的主线是用

\[
\frac{\mu}{\nu}
=
\frac{E\kappa^2}{10^{m_3}Q^2(\kappa+G)}
\]

控制非 resonance 时 \(F_-\) 与 \(F_+\) 的赋值差，并每次与

\[
\kappa^3(\kappa+2G)<10^{8S_{12}+4}
\]

的统一高度上界重新比较。

---

## 第二优先级：\(A_2\) 的 resultant / Hensel 接触

对

\[
\Phi(x,z)
=
(99x-4)z-2x-4
\]

和

\[
\Psi_{a_1}(y,z)
=
400a_1(z+1)^2
-y(99z-2)^2
\]

计算

\[
\operatorname{Res}_z(\Phi,\Psi_{a_1}).
\]

由于 \(\Phi\) 对 \(z\) 线性，可以直接代入

\[
z=\frac{2x+4}{99x-4}
\]

得到显式的

\[
\Theta_{a_1}(x,y).
\]

合法 source odd excess 要求某个 inert prime 同时满足

\[
p^{2h}\mid\Phi,
\qquad
p^h\mid\Psi_{a_1}.
\]

预期可转化为

\[
p^h
\mid
\Theta_{a_1}(x,y).
\]

下一步应研究：

- \(\Theta_{a_1}\) 的因子分解；
- repeated-root/discriminant；
- 与固定 core \(a_1\) 的 gcd；
- 是否只有有限小素数允许高阶 Hensel 接触；
- \(p^{2h}\) 与十进制区间长度之间的 rational reconstruction 矛盾。

如果能证明所有高阶接触都来自固定有限素数集，\(A_2\) 就可能进一步压成有限状态。

---

## 第三优先级：\(A_1\) saturated 的 coefficient-plane invariant

这里不应继续尝试 Gaussian flip。

更合理的方向是找一个直接依赖

\[
10^g
\]

与前两块系数的整数对象，例如：

- determinant；
- cross-ratio 型有理不变量；
- 二次型 discriminant；
- 两个线性平面之间的格指数；
- 对 \(2,5\)-进高度同时敏感的 resultant。

目标是证明当 \(g\) 变大时，该对象一方面必须被 \(10^g\) 深度整除，另一方面绝对值增长速度又小于 \(10^g\)，从而出现

\[
0<|X|<10^g
\quad\text{且}\quad
10^g\mid X
\]

的直接矛盾。

这会比在 saturated 支中继续寻找“下降”自然得多。

---

# 39. 最终主定理需要的最小新成果集合

目前不需要重新发明前面所有局部代数。

一个完整证明最少需要以下三类新结果。

### Lemma DD — 中低层的统一高度界

双 resonance 顶部已排除。剩余需证明的是：对单 resonance 和非 resonance 区域建立

\[
S_{12}\le S_0,
\]

或者直接得到与 gap-valuation 恒等式不相容的赋值/高度矛盾。

### Lemma A2 — deep-even uniform obstruction

证明

\[
m_2\ge11
\]

时 source Hensel / Gaussian ellipse / decimal window 无法兼容，或者得到统一 \(m_2\) 上界。

### Lemma A1 — saturated decimal-shift bound

证明 saturated \(L=1\) 中

\[
g\le g_0(m_1,m_2)
\]

并最终与现有 tail bound 合并成全局有限性，或者直接产生矛盾。

若三条都得到统一有限上界，最后的有限区域可以由严格整数证书完全关闭。

---

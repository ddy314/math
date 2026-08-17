# 严格证明状态与后续工作

本文件对应原总稿 §§32–39，是 agent 判断证明状态的权威入口。

## 状态边界

当前严格状态是：主不存在性命题尚未完成证明；三个异常分支均有大量严格局部结论，但 `A_2`、DD、`A_1` 都仍有未闭合的无界核心。

## 2026-08-13 DD 合并状态

本节覆盖下方由 2026-08-10 原总稿机械拆分出的 DD 旧状态。完整命题、假设、推导与逻辑修正见
[DD 主干 §27.33](branches/double-deficit/core.md#2733-2026-08-13-后续合并进展)。

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

最新 endpoint-lattice 推进在最危险 `(a,k)=(9,2)` reflection high-2
子族中严格得到：`eta=2m-M=-1,0` 均不可能，`eta=1` 只剩五个
`(d,c_Q,k_h,slot)` 类型。这里仍须保留两条状态边界：

- **`已严格完成`**：固定 `eta=1` 的连续槽相交分类先成为有限十五型，
  exact concatenation 相关界排除 `(107,1,-)` 与 `(163,1,+)`，随后
  `q_0` barrier 给出的 `r>4/5` 又排除两个 `K_+=153/40` 类型，
  Gaussian norm 的素数支持再排除所有含 `5`、`7`、`23`
  的类型；
- **`失效/降级`**：唯一的 `k_h=3` 类型虽强迫四个 sphere 坐标共享
  `3`，但 LCM sphere 不自动整体本原；同时除以 `3` 会改变第三块位数，
  不能构成保持 decimal plane 的下降；
- **`失效/降级`**：粗 slot 本身不能对所有 `eta` 给出空性，
  `(eta,d,c_Q,k_h,slot)=(1,2,31,1,+)` 的两个必要实区间严格相交。

因此下一步必须把这五型与 `c_Q\mid Q_0`、source split、平方单边
allocation 的自然代表或 `C` 的 CRT phase 联立。三个 `k_h=1` 类型
现已分别压到模 `515,795,775` 的有限平方根相位；`k_h=53` 类型则有
模 `53` 的两个 Gaussian 相位及 `53\nmid c_u`。这些仍不是 A2 关闭。

为避免把主线退化成逐层枚举，最新的 `eta`-uniform 推进进一步令

\[
X_h=\frac{k_hg}{2},
\qquad c_Q=c_-c_+,
\]

并对整个 reflection high-2 cone 严格得到

\[
\gcd(k_h,c_Q5^d)=1,
\qquad
5^dc_-\mid X_h-a_3,
\qquad
c_+\mid X_h+a_3.
\]

因此模 `c_Q5^d` 的平方根符号不是独立自由度，而由原
square-side allocation 唯一定向；特别地 `5^d` 恒取正根。定义相应
正奇数 `r_-,r_+` 后，还得到 exact linear/product system 以及

\[
gr_-\equiv\varepsilon a_2c_+
\pmod{5^{\lambda-d}},
\qquad
\lambda-d\ge\lambda/2.
\]

进一步与 source 双 Hensel 及
`v_5(N_0)=lambda-2d` 的两相位合并，已消去 `g,omega,theta`，得到

\[
r_-\equiv
\varepsilon\iota\,9\cdot2^{M+m}c_+c_u
\pmod{5^{\lambda-2d}},
\qquad
\iota^2\equiv-1.
\]

同一系统还严格给出新的近本原 Gaussian norm transfer

\[
r_-^2+
\left(9\cdot2^{M+m}c_+c_u\right)^2
=k_h5^{\lambda-2d}X,
\qquad
\gcd(r_-,9\cdot2^{M+m}c_+c_u)\mid9.
\]

把它与 prefix norm 同时除去同 orientation 的
`(2 plus or minus i)^{lambda-2d}` 后，两条 `5`-primitive Gaussian
向量的交叉行列式仍满足精确深度

\[
v_5\!\left(
\operatorname{Im}(\mathcal R_5\overline{\mathcal A_5})
\right)=d.
\]

此外还存在互补的近本原表示与精确 Gaussian composition：

\[
r_+^2+
\left(9\cdot2^{M+m}c_uc_-5^d\right)^2
=k_hY,
\]

\[
\mathcal R_5\overline{\mathcal A_5}
=X\left(
\varepsilon r_+-i\,9\cdot2^{M+m}c_uc_-5^d
\right).
\]

这把剩余核进一步变成同一 `k_h` 在两条互补近本原二平方表示中的
Gaussian prime orientation 兼容问题。

对精确 composition 使用 `Z[i]` 唯一分解后，进一步严格得到：令
`X_(3)=X/3^{v_3(X)}`，则存在

\[
N(\alpha_X)=X_{(3)},
\qquad
\alpha_X\mid\mathcal A_5,
\qquad
\alpha_X\mid\mathcal R_5.
\]

也就是说 `X` 的全部非 `3` 部分是真正可整体消去的共同 Gaussian
divisor。唯一例外的 `3`-primary defect 满足

\[
v_3(X)+v_3(Y)\le4,
\qquad
v_3(k_h)\le4.
\]

这尚未证明约分后的坐标回到原 decimal coefficient plane，但已经
排除“任意新奇素数形成无界 obstruction”的可能。

对唯一的奇 `3`-primary defect 还可作完整赋值分类。写
`e_3=v_3(k_h)`，则

\[
e_3\text{ 为奇数}
\Longrightarrow
\begin{cases}
v_3(a_3)=1,\ e_3=1,\ v_3(a_2)\ge2,\\
\text{or}\\
v_3(a_2)=1,\ v_3(a_3)\ge2,\ e_3\in\{1,3\}.
\end{cases}
\]

两通道都进一步强迫

\[
v_3(H)=v_3(\alpha)=1,
\qquad
v_3(\beta)=0.
\]

因此奇 `3` 缺陷已被压到两个明确通道，并必须与真实 denominator
concatenation 的模 `3` source/Hensel 表达兼容。

进一步地，`3` 的奇性也可以在 Gaussian UFD 内统一吸收。由三条 norm
恒等式，

\[
v_3(X)\equiv v_3(Y)\equiv v_3(k_h)\pmod2.
\]

令 `delta` 为这一公共奇偶性，则存在完整共同 Gaussian divisor

\[
N(\alpha_X^\sharp)=3^\delta X,
\qquad
\alpha_X^\sharp\mid\mathcal A_5,\mathcal R_5,
\]

约去后满足

\[
N(\mathcal B_5)=Y/3^\delta,
\qquad
N(\mathcal G_5)=k_h/3^\delta,
\]

\[
\varepsilon r_+-iR_1
=3^\delta\mathcal G_5\overline{\mathcal B_5}.
\]

所以当前已不存在独立的 Gaussian prime-allocation 障碍；真正缺口是
证明共同因子约分必然保持原 decimal coefficient plane，并把它升级
为严格降低高度且仍合法的 A2 descent；另一条可行路线是直接从
quotient 与原平面的强制关系推出矛盾。仅证明 quotient 不保持平面
不能排除原候选。

把完整共同 divisor 从 source Hensel 兼容式中消去后，进一步得到不含
`X`、不含固定 `eta` 分类的纯 Gaussian quotient kernel：

\[
\pi_\iota^d\bar\pi_\iota^{\lambda-d}
\mid
c_u\mathcal G_5
-\varepsilon c_+\omega\mathcal B_5,
\]

其中

\[
N(\mathcal B_5)=Y/3^\delta,
\qquad
N(\mathcal G_5)=k_h/3^\delta.
\]

Gaussian 模数的 norm 恰为 `5^lambda`，故相应线性式的 norm 必须被
`5^lambda` 整除；由精确 composition 的非零虚部，该线性式不可能为
零，所以其 norm 实际至少为 `5^lambda`。进一步审计表明该整除来自
同一个 Gaussian 商的精确分解；短 orientation 的赋值恰为 `d`，任何
额外增深只能留在长 orientation，而 `theta` 写法与 `omega` 核严格
线性相关，并不提供第二条独立 Hensel 条件。

原拼接平面还给出

\[
\omega\mid\alpha,
\qquad H_0=c_u(\alpha/\omega),
\]

并把 endpoint 小余量固定为

\[
5^\lambda C
=g(a_3+3\cdot10^m)
+\varepsilon a_2c_Q5^d
-\frac{g^2k_h}{2}.
\]

所以当前可审计的直接闭环目标已变成：证明这个唯一自然代表不能落在
`0<C<mathfrak L_0/1000`，或由精确 quotient 构造合法降高；不能再对
`omega/theta` 两种写法重复收费。

Archimedean 侧也不再只有一个无方向 norm bound。预约分商
`S_5=alpha_X^sharp W_5` 满足

\[
4<\tan\arg(-\varepsilon\mathcal S_5)<5,
\]

并且相对 prefix 向量 `Z_a=a_2+iC_0` 的侧别恰由 `epsilon` 决定。
约掉共同 `X` 后还有精确面积式

\[
\operatorname{Im}
\left(
\mathcal W_5\bar\pi_\iota^{\nu_5}
\overline{\mathcal B_5}
\right)
=-\frac{c_uR_1}{3^\delta5^d}.
\]

因此下一步所需的不是再做粗角度估计，而是证明这个固定窄楔与精确
面积不允许任何 canonical split-prime argument，或由其恢复合法下降。

同一精确商还能写成有理 Gaussian 格上的中心余数：

\[
5^{\lambda-d}\mathcal W_5
+\varepsilon c_+\omega
\pi_\iota^{\nu_5}\mathcal B_5
=c_u\pi_\iota^{\nu_5}\mathcal G_5.
\]

low-`m` 高度锥统一给出

\[
\frac{c_u^2k_h}{5^\lambda}<\frac1{25},
\qquad
\left|c_u\pi_\iota^{\nu_5}\mathcal G_5\right|
<\frac15 5^{\lambda-d}.
\]

故右端是相应同余类在半径 \(5^{\lambda-d}/2\) 圆盘内的唯一代表。
主缺口因而进一步缩成：排除这个唯一中心代表同时具有既定 norm、
有向面积与 `C` 自然代表；这仍只关闭到 reflection high-2 kernel，
不是 A2 全局空性。

中心代表与主向量之比还满足统一指数界

\[
\frac{
|c_u\pi_\iota^{\nu_5}\mathcal G_5|
}{
c_+\omega|\pi_\iota^{\nu_5}\mathcal B_5|
}
<\frac1{7680}.
\]

因此 quotient 的两个坐标都是唯一最近整数商；其方向不再只落在
`4<tan(phi_S)<5`，而是满足

\[
0<\varepsilon
\left(
\tan\phi_S-\frac{C_0}{a_2}
\right)
<\frac7{2000}.
\]

这把剩余对象压成贴着真实 decimal prefix slope 的确定单侧格点条带，
但“唯一最近商”仍不等于“不存在”；必须继续接入 `C` 自然代表或精确
面积才能得到矛盾。

进一步把 quotient slope 按 \(J_{\rm def}\) 展开后，两项 decimal
contribution 精确抵消，并得到

\[
\tan\phi_S-\frac{C_0}{a_2}
=
\frac{
\varepsilon C_0J_{\rm def}
}{
a_2(\mathcal K a_2-\mathcal U-\varepsilon J_{\rm def})
}.
\]

因此实际方向锁是

\[
0<\varepsilon
\left(
\tan\phi_S-\frac{C_0}{a_2}
\right)
<\frac1{a_2}.
\]

于是 `epsilon=+1` 时 \(C_0=\lfloor a_2\tan\phi_S\rfloor\)，
`epsilon=-1` 时 \(C_0=\lceil a_2\tan\phi_S\rceil\)。这说明提升后
quotient \(\mathcal S_5=\alpha_X^\sharp\mathcal W_5\) 的方向可唯一恢复
原 prefix 系数。它仍含共同 Gaussian factor；裸 quotient 的绝对
argument、完整尺度、\(a_2\) 与顶部补余量 \(C\) 尚未同步恢复。

同一精确式还把有向面积
\(\Delta_S=\varepsilon(a_2Y_S-C_0X_S)\) 锁入

\[
\frac35<\frac{\Delta_S}{X_S}<\frac45.
\]

因此 \(X_S=\Delta_S+E_S\) 的 Euclidean 商恰为 `1`，且
\(\Delta_S/4<E_S<2\Delta_S/3\)。这给出严格更小的正整数余量，但尚未
证明该余量保持 Gaussian norm 与 decimal plane，故还不是合法下降。

进一步审计表明，该实线性 split 的变换 determinant 为
\(-\varepsilon a_2\)，所以它确实不保持二平方 norm。改在裸
quotient pair 上做 Gaussian 除法，则首商被唯一固定为纯实整数

\[
Q_E=\operatorname{nint}
\left(\frac{c_+\omega}{5^{\lambda-d}}\right).
\]

对应非零余数
\(\mathcal R_E=-\varepsilon\mathcal W_5-Q_E\mathcal V_5\) 满足

\[
0<N(\mathcal R_E)<\frac14N(\mathcal V_5),
\qquad
v_{\pi_\iota}(\mathcal R_E)=0.
\]

这是严格的 canonical Gaussian norm descent；尚缺的是证明该余数继续
满足 decimal coefficient plane / Hensel 形状，才能迭代为 A2 下降。

乘回同一不对称模数后还有

\[
\mathfrak K_5\mathcal R_E
=r_E\mathcal B_5-\varepsilon c_u\mathcal G_5,
\]

其中 \(r_E\) 是中心区间内唯一的 scalar Hensel representative，
\(5\nmid r_E\)，并满足

\[
r_E\equiv c_-^{-1}\theta\pmod{5^{\lambda-d}}.
\]

取 norm 后得到一维正定二次核

\[
5^\lambda N(\mathcal R_E)
=
\frac{Yr_E^2-2c_ur_+r_E+c_u^2k_h}{3^\delta},
\]

其 discriminant 恰为 \(-4c_u^2R_1^2\)。因此下一直接目标是排除该
唯一中心代表达到剩余长 orientation，而不再处理二维 Gaussian
quotient-choice。

继续展开 Hensel slot 得到

\[
g\varrho=5^{\lambda+1}H-c_Qc_u.
\]

第一层 \(r_E\) 余类中的 \(H\) 项被模 \(5^{\lambda-d}\) 消去，但提升商

\[
z_E=\frac{gr_E-c_+c_u}{5^{\lambda-d}}
\]

满足

\[
-\frac g2<z_E<\frac g2,
\qquad
c_-z_E\equiv-5^{d+1}H\pmod g,
\]

并且是唯一中心奇代表。代入一维核后得到

\[
3^\delta g^2N(\mathcal R_E)
=5^{\nu_5}Yz_E^2
-2\varepsilon c_ua_2c_-z_E+c_u^2c_-^2X,
\]

其 discriminant 恰为 \(-4c_u^2c_-^2C_0^2\)。对应二平方表示的两个
坐标均被完整 \(g\) 整除；约分后精确等于
\[
3^\delta\bar\pi_\iota^{\nu_5}
\mathcal R_E\overline{\mathcal B_5}.
\]
所以 `H,a_2,C_0` 已进入同一个正规化 Gaussian 向量，但该向量仍未
证明对应合法 decimal child。

第二层代表还与顶部补余量满足

\[
c_uC+\varepsilon a_2c_-z_E\equiv0\pmod g,
\qquad
\chi_E=\frac{c_uC+\varepsilon a_2c_-z_E}{g}\in\mathbf Z,
\]

并给出 `(z_E,chi_E)` 的完全整数正定核。另一方面，完整
`g`-约分所得 canonical Gaussian child 的绝对斜率小于
`1/3999`（乘 unit 后则大于 `3999`），不可能回到
`(9/2,5)` 的 A2 prefix window；因此直接同型下降路线已严格降级，
不能把 Gaussian norm 下降本身当作 A2 空性。

独立的 rational-root 条件现已剥去全部十进制素因子：

\[
\Xi_C=
\frac{F(3)}{2^{2M+2}5^{\nu_5}C}
\in\mathbf Z_{>0},
\qquad
\gcd(\Xi_C,10)=1.
\]

它在完整 denominator 上满足

\[
\Xi_C\equiv q^2c_+^2Y(3T+a_3)^2\pmod D,
\]

所以 `Xi_C/Y` 在 `2^m5^d` 上是显式平方类。把同一
rational root 在相邻整数点平移，还得到

\[
D-C\mid F(2),
\qquad
D+C\mid F(4),
\qquad
\gcd(D-C,D+C)=1,
\]

以及正奇 `5`-进单位 cofactor `Xi_-,Xi_+`；三者模
`2^m5^d` 共享同一个 `Y`-平方类。这是严格的无界必要条件，
不是有限证书。当前最具体的直接缺口是从三个 odd-prime cofactor 的
resultant/reciprocity 与 `(z_E,chi_E)` 中心代表推出矛盾。

此外 mixed bridge 重新恢复旧 source coprimality，并严格新增符号锁

\[
\gcd(c_uH,g)=1,
\qquad
\operatorname{sgn}\chi_E=\operatorname{sgn}(\varepsilon z_E),
\qquad
\left|
\frac{g\chi_E}{\varepsilon a_2c_-z_E}-1
\right|<\frac3{50000}.
\]

其中 coprimality 与旧 source split 一致，不重复计作 obstruction；新
结论是该中心核的象限自由度消失。模 \(p^e\Vert g\) 时还有

\[
\min\{v_p(\Xi_C),e\}
=\min\{2v_p(3T+a_3),e\},
\]

所以零因子只剩 \(3T+a_3\) 的饱和通道；窄有理接触本身尚未形成矛盾。
在非饱和奇素数 \(p\mid g\) 上，继续消去
\(C,c_u,z_E,H,q\) 后有

\[
\left(\frac{\Xi_C}{p}\right)
=\left(\frac{-\varepsilon a_25^{M+d}}p\right).
\]

这把下一步精确化为：从 \(2^m5^d\) 的 \(Y\)-平方类或
\(\Xi_-,\Xi_+\) 的共同 cubic quotient 固定相反字符。
但把同一 congruence 提升到模 \(g^2\) 后，精确修正为

\[
\Xi_C\equiv
Y(qc_+(3T+a_3))^2(1-3DC^{-1})\pmod{g^2},
\]

而 \(1-3DC^{-1}\) 在 \(g^2\) 的每个 prime-power 分量上自动为平方。
所以普通 quadratic-character 提升路线已严格降级；下一输入必须是
非二次特征的加性 resultant、符号/高度或饱和层大小。

三点 secant cubic 已提供第一条这样的加性信息。定义

\[
\Delta_-=\frac{\Xi_C-\Xi_-}{2^m5^d},
\qquad
\Delta_+=\frac{\Xi_+-\Xi_C}{2^m5^d},
\]

则严格有

\[
1<\frac{\Delta_-}{\Delta_+}<2,
\qquad
v_2(\Delta_-)=v_2(\Delta_+)=1,
\]

\[
\Delta_--\Delta_+
=2^{m+1}5^dc_u^2
\{g((20P-9)T-a_3)-H_0\},
\]

\[
v_2(\Delta_--\Delta_+)=m+1,
\qquad
v_5(\Delta_--\Delta_+)=d.
\]

这已覆盖 pure-\(2\) fallback 的精确相邻-gap 结构，但尚未证明该加法
与 \(D-C,D+C\) 的奇除数不相容。
进一步取 \(F(2),F(3),F(4)\) 的中心二阶差分后，\(\Delta_+\) 已由两条
互素 congruence 唯一固定在模 \(D^2-C^2\) 的显式 CRT 类中；
\(\Delta_-=\Delta_++\Gamma_\Delta\)。当前剩余自由度因此缩成 CRT 商
\[
Q_\Delta=\left\lfloor\frac{\Delta_+}{D^2-C^2}\right\rfloor,
\]
但尚无它的全局上界。

同时，中心二阶差分先除去 \(2^{m+1}5^d\) 得到
\(\widetilde{\mathcal T}_2\)，但显式式进一步给出精确赋值
\(v_5(\widetilde{\mathcal T}_2)=d\)。真正的 \(2,5\)-本原正整数为
\[
\widehat{\mathcal T}_2
=\frac{\mathcal T_2}{2^{m+1}5^{2d}},
\]
严格满足

\[
\widehat{\mathcal T}_2
\equiv-5^{\lambda-d}(c_uC)^2\pmod g,
\qquad
\widehat{\mathcal T}_2\equiv3\pmod4,
\qquad
\gcd(\widehat{\mathcal T}_2,10c_ug)=1.
\]

所以它必供应一个不整除 \(g\) 的 \(3\bmod4\) 惰性素数到奇次。但完整
代入 canonical square 后得到
\[
5^d\widehat{\mathcal T}_2
=5^{\epsilon_5}Z_\nu^2+\mathscr J_\Delta,
\qquad \mathscr J_\Delta\equiv2\pmod4,
\]
这恰好恢复旧 odd inert excess，而非第二个独立 obstruction。后续必须
排除其 denominator-prefix、source、spontaneous 三类来源。
进一步化简显示
\[
\widehat{\mathcal T}_2
=2^mc_u^2g^2\mathscr S_0
-(c_Qq)^2 5^{2\lambda-d}XY,
\]
所以当前只有“尺度项减 norm”，没有把差变成 norm 所需的内积/正交
恒等式；该漂亮路线已审计到一个明确而真实的 orientation 缺口。
新的接触律
\[
\gcd(\widehat{\mathcal T}_2,Q_0XY)
=\gcd(\mathscr S_0,Q_0XY),
\qquad
\gcd(\widehat{\mathcal T}_2,f)
=\gcd(\mathscr R_f,f)
\]
已把 \(qf\) denominator excess 压成两个显式 gcd 问题；非 \(3\)
inert prime 不能来自 \(XY,c_u,g\)。固定素数 \(3\) 的一阶出现条件
也已由 (16.310) 精确分类，但允许 residue 中的赋值奇偶仍待控制。
对非 \(3\) denominator prime，\(\mathscr S_0\) 的
\(K\)-判别式进一步识别为判别数 \(-23\) 的二元型：
\[
\operatorname{disc}_K(\mathscr S_0)=8\mathscr R_{23}.
\]
\(q\)-channel 因而满足 (16.316)/(16.318) 的 \(23\)-分裂约束，
\(f\)-channel 满足独立的 (16.320) curvature character。它们仍只是
必要条件；(16.323) 的完整平方配方进一步证明这些局部 character
都是同一 principal-square identity 的投影，尚未取得与 source
allocation 相反的独立 character。
companion 还满足
\[
\mathscr C_{23}
=U_{23}^2+23V_{23}^2+5^{3\lambda}Q_0^2XY,
\quad
\mathscr C_{23}\equiv U_{23}^2\pmod{5^{2m}},
\quad
\mathscr C_{23}\equiv1\pmod8.
\]
因此纯 \(2,5\)-进局部非平方路线同样已降级。
进一步与 canonical \(Z\) 联立产生两个严格正 shifted factors
\[
\mathscr V_-=5^\lambda fc_-^2X-\mathscr E_{23},
\qquad
\mathscr V_+=5^\lambda qc_+^2Y-\mathscr E_{23}.
\]
它们的 \(q,f\) 同侧接触由
\(\mathscr L_{23}=9T/2+a_3\) 控制，共同因子由
\(\gcd(TK-9T-2a_3,Z)\) 控制。消去 \(Z\) 后证明 \(qf\) 的所有
未饱和接触赋值为偶数，所以 denominator odd excess 只剩
\[
p^e\Vert qf,\qquad p^e\mid\mathscr L_{23}
\]
的完整 prime-power saturation。
同时 \(q\equiv3,f\equiv1\pmod4\) 把 orientation 分成固定 \(3\)
balanced transfer 与 denominator \(q\) carrier；在前一支中
\(\mathscr V_\pm\) 恰共享一份 \(3\)，且
\(3\nmid\widehat{\mathcal T}_2\)。
剩余 saturation 已进一步接回真实缺口 \(H\)：
\[
\mathscr G_q=5^{M-1}(a_3-90T)+a_3H,\qquad
\mathscr G_f=\mathscr G_q-18\cdot2^{m+1}c5^d,
\]
候选必须满足完整 \(p^e\Vert q\) 整除 \(\mathscr G_q\)，或完整
\(p^e\Vert f\) 整除 \(\mathscr G_f\)。两 target 位于约
\(-89\cdot5^{M-1}T\) 的同一窄 significand band；尚缺无界
prime-power gcd/resultant 排除。
generic \(q\)-saturation 还由 rational-root 四次式放大为
\[
p^e\mid(6D+C),\quad
p^{2e}\mid\bigl(D(3T+2a_3)-TC\bigr),
\]
或 \(p^e\mid((K-3)D+C)\)。按
\(n_p=v_p(c_Qq)=v_p(c_Q)+e\) 精确计价后，middle branch 的
正规商恰有深度 \(e+2v_p(c_Q)\)，third branch 吸收完整 \(n_p\)。
对真正接触 \(\mathscr S_0\) 的 \(q\)-carrier，又有
\[
\mathscr S_0=T(K^2-26)-(2K-9)(2a_3+9T),
\qquad K^2\equiv26\pmod p.
\]
故第一 valuation branch 完全排除，无界 exceptional set 缩成固定
素数 \(11,23\)。尚未排除这两个固定素数的无限 Hensel lift，也尚未
从 middle/third residual unit character 得到最终矛盾。
在 \(p\nmid c_Q\) 的 generic 层，\(f\)-侧 saturation 则满足互补的非零局部型
\[
K^2-26\equiv
\left(\frac{2c_Q}{2^m5^\lambda g}\right)^2N_0\not\equiv0\pmod p,
\]
\(p\mid c_Q\) 时它退化回 \(K^2\equiv26\)，恰为已隔离的 overlap；
而 \(q\)-侧根另有
\(J_{101}^2\equiv101N_0-26\pmod p\) 的 prefix Gaussian bridge。
这些是新的严格必要条件，仍未合成为空性证明。
canonical factor allocation 又强迫每个 \(q\)-carrier 满足
\(N\equiv DK\pmod p\)，从而 generic middle branch 完全删除。
对 \(p\ne11,23\)，唯一剩余 rational-root branch 精确满足
\(v_p(KD-N)=v_p(c_Qq)\)；\(11\) 与 \(23\) 分别只剩一条固定的
双因子预算和右侧增深预算。
整数层进一步有
\[
q\mid DK-N,\qquad
2c_u(DK-N)/q=c_+^2Y+5^\lambda c_-^2X.
\]
在 saturation 内，\(q/f\) 两侧的截断赋值已分别降为纯 prefix
resultants \(K^2-26\) 与
\(\Psi_f=b_2^2(K^2-26)-Q^2N_0>0\)。此外
\((DK-N)/q\) 的每个非 \(3\) inert prime 都以相同深度整除
\(H_0\)，并满足 \((N_0/r)=-1\)。这三个明确通道尚未全部排除。
同时 \(Q_\Delta\ge5K\)，故 CRT 商不是可由固定有限层排除的小参数。

当前数学核心已经转为证明这个覆盖所有 `eta` 的定向因子系统与
source 双 Hensel / prefix defect 不相容，或从中构造保持十进制
coefficient plane 的下降；尚未得到该最终矛盾。

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

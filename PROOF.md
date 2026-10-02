# 三块十进制拼接 Exact Lift：规范证明稿

主不存在性命题：**待证**。`A2`、`DD`、`A1` 三个完整异常分支仍未全部关闭。

本稿从原问题顺次建立公共系统，再进入三个分支。每个命题的状态、作用域、依赖和证书只在该命题下定义；研究路线和撤回记录集中在 [RESEARCH.md](RESEARCH.md)。历史原文不是现行证明依赖。

四种状态使用同一含义：**已严格完成**表示明确作用域内的已采纳定理或必要归约；**有限证书**表示先有完备参数界、再由精确有限计算闭合明示子域；**待证**表示仍有逻辑缺口；**失效/降级**只用于研究审计。结构检查和符号回归不代替数学论证。

全局符号仅在公共章节统一。A2 的 `K,zeta`、DD 的 `a,d0,v`、A1 的 `k,g,d` 都是其所在分支的局部符号；进入新分支重新定义，禁止跨分支同名代入。

历史标签如 `(LK19)`、`(JS24)` 只标识本节公式；稳定命题编号是 `Cxx`、`A2-xx`、`DD-xx`、`A1-xx`。逐段原文的范围和 SHA-256 存于 [命题登记表](registry/claims.json)，可用 `main.py source` 核对。

## 阅读顺序

- [公共系统](#common)：C01–C10。
- [A2 分支](#a2)：无条件 first-block 归约、奇尾有限系列、deep-even source、actual transport、fixed 3。
- [DD 分支](#dd)：原 gap、低层证书、canonical 预算与 orientation。
- [A1 分支](#a1)：contact、四层、最高层和低层整数 recovery。
- [剩余目标](#remaining)：三分支与主目标。

<a id="common"></a>
## 公共系统

<a id="c01"></a>
### C01　原问题、carrier 与三个穷尽分支

**状态：已严格完成。** 所有正既约整数块；只把主目标归约为三个异常分支。

依赖：定义与正权平均。

核对：正文推导；本次重写未为此项另增枚举。

<a id="c01-detail-src-0202-8-1"></a>
#### 基本数据

对 \(i=1,2,3\)，令

```math
r_i=\frac{a_i}{b_i}>0,
\qquad
\gcd(a_i,b_i)=1,
```

其中 \(a_i,b_i\) 均为无前导零的正整数。

统一记

```math
n_i=\operatorname{digits}(a_i),
\qquad
m_i=\operatorname{digits}(b_i),
```

以及分子、分母位数差

```math
\boxed{s_i=n_i-m_i.}
```

三个分子与三个分母的十进制拼接分别为

```math
\boxed{
\alpha
=
a_1 10^{n_2+n_3}
+a_2 10^{n_3}
+a_3,
}
```

```math
\boxed{
\beta
=
b_1 10^{m_2+m_3}
+b_2 10^{m_3}
+b_3.
}
```

目标命题是

```math
\boxed{
\text{不存在正既约有理数三元组使 }
\frac{\alpha}{\beta}
=
\sqrt{r_1^2+r_2^2+r_3^2}.
}
```

本文把右侧欧氏长度统一记为

```math
\boxed{
\mathcal R
:=
\sqrt{r_1^2+r_2^2+r_3^2}.
}
```

---

<a id="c01-detail-src-0202-8-2"></a>
#### 十进制权重与 carrier 放大因子

定义三个分母位置权重

```math
B_1=10^{m_2+m_3},
\qquad
B_2=10^{m_3},
\qquad
B_3=1,
```

以及正权

```math
w_i=B_i b_i.
```

定义十进制放大因子

```math
\Lambda_1=10^{s_2+s_3},
\qquad
\Lambda_2=10^{s_3},
\qquad
\Lambda_3=1.
```

则拼接式恒等地写成

```math
\alpha
=
\sum_{i=1}^3 w_i\Lambda_i r_i,
\qquad
\beta
=
\sum_{i=1}^3w_i.
```

因此 exact lift 等式等价于

```math
\boxed{
\mathcal R
=
\frac{
w_1\Lambda_1r_1
+w_2\Lambda_2r_2
+w_3r_3
}{
w_1+w_2+w_3
}.
}
```

右端是三个数

```math
\Lambda_1r_1,\qquad
\Lambda_2r_2,\qquad
r_3
```

的严格正权平均。

由于

```math
\mathcal R>r_i
```

对所有 \(i\) 都成立，第三坐标

```math
\Lambda_3r_3=r_3
```

永远不可能达到 \(\mathcal R\)。因此若 exact lift 存在，第一、第二坐标至少有一个必须满足

```math
\Lambda_i r_i\ge \mathcal R.
```

这就是整个分支理论的 carrier 原理。

---

<a id="c01-detail-src-0202-8-3"></a>
#### Carrier 几何与三个异常分支

如果

```math
s_3\le0,
\qquad
s_2+s_3\le0,
```

则

```math
\Lambda_1\le1,
\qquad
\Lambda_2\le1.
```

于是

```math
\Lambda_1r_1<\mathcal R,\qquad
\Lambda_2r_2<\mathcal R,\qquad
r_3<\mathcal R,
```

三个正权平均项全部小于 \(\mathcal R\)，矛盾。

因此正常位数区域被严格排除。

所有可能候选恰好处于以下三个异常 chamber：

| 分支 | 位数条件 | 可能承担 carrier 的坐标 |
|---|---|---|
| \(A_2\)-only | \(s_3>0,\ s_2+s_3\le0\) | 第二坐标 |
| double-deficit（DD） | \(s_3>0,\ s_2+s_3>0\) | 第一、第二坐标 |
| \(A_1\)-only | \(s_3\le0,\ s_2+s_3>0\) | 第一坐标 |

所以主命题已经严格化为：

```math
\boxed{
\text{分别证明 }A_2\text{-only、DD、}A_1\text{-only 三个分支均为空。}
}
```


来源：`SRC-0202:8–211`。原文保全，当前论证以本节为准。

<a id="c02"></a>
### C02　整数球面与逐坐标唯一恢复

**状态：已严格完成。** q=lcm(bi)，sphere 与原 word 同时成立；全体球面不等于原解。

依赖：[C01](#c01)

核对：正文推导；本次重写未为此项另增枚举。

对三个正既约有理数

```math
r_i=\frac{a_i}{b_i},\qquad \gcd(a_i,b_i)=1,
```

令

```math
\boxed{q=\operatorname{lcm}(b_1,b_2,b_3)},
\qquad
\boxed{y_i=\frac{qa_i}{b_i}}.
```

若 exact lift 成立，则存在正整数 \(H\) 使

```math
\boxed{y_1^2+y_2^2+y_3^2=H^2},
\qquad
\boxed{q\alpha=H\beta},
```

其中 \(\alpha,\beta\) 为完整 numerator / denominator decimal words。

逐坐标有精确恢复恒等式

```math
\boxed{\gcd(q,y_i)=\frac q{b_i}}.
```

因此令

```math
d_i=\gcd(q,y_i),
```

即可唯一恢复

```math
\boxed{a_i=\frac{y_i}{d_i},\qquad b_i=\frac q{d_i}}.
```

所以完整候选可放在 canonical spine

```math
\boxed{(y_1,y_2,y_3,q)}
```

上理解。给定该 spine 后，\(H\)、六个 reduced blocks、digit lengths、valuations 与后续 Exact-Lift coefficient data 都是确定性投影。Gap root、tail root、判别平方根符号、Hensel/Gaussian 标签若只是这些数据的消元表示，不能重复计作新的 original-candidate freedom。

注意：\(q=\operatorname{lcm}(b_i)\) 不自动保证 \((y_1,y_2,y_3,H)\) 整体本原；需要 primitive core 时必须显式再除公共 content。


来源：`SRC-0199:7–57`。原文保全，当前论证以本节为准。

<a id="c03"></a>
### C03　公共 prefix、gap 与 tail 必要系统

**状态：已严格完成。** 只在相应 primitive-tail recovery 定义域使用；相对高度界不提供绝对上界。

依赖：[C02](#c02)

核对：正文推导；本次重写未为此项另增枚举。

统一定义

```math
\boxed{Q=b_1 10^{m_2}+b_2},
\qquad
\boxed{G=b_1b_2},
```

```math
\boxed{\mathcal N_{12}=(a_1b_2)^2+(a_2b_1)^2=G^2(r_1^2+r_2^2)}.
```

三个异常分支使用统一 coefficient pair \((C,D)\)：

```math
(C,D)=
\begin{cases}
\left(a_1 10^{m_2}+10a_2,\ Q\right),&A_2,\\[0.4em]
\left(10^{m_2+k_{12}}a_1+10^{d_3}a_2,\ Q\right),&DD,\\[0.4em]
\left(10^{g+k_{12}+m_2}a_1+a_2,\ 10^gQ\right),&A_1.
\end{cases}
```

DD 中

```math
d_3=s_3>0,\qquad k_{12}=s_2+s_3>0,
```

A1 中

```math
g=-s_3\ge0,\qquad k_{12}=s_2+s_3\ge1.
```

这些定义只是把三个 carrier chamber 的 decimal coefficient plane 写入同一语言，不改变分支状态。

---

<a id="c03-detail-src-0199-63-1"></a>
#### 第三尾正规化与 denominator–decimal trace

定义有效尾长

```math
\ell=
\begin{cases}
m_3,&A_2,DD,\\m_3-g,&A_1,
\end{cases}
```

以及

```math
\boxed{\delta_3=\gcd(10^\ell,b_3)},
\qquad
\boxed{L=\frac{10^\ell}{\delta_3}},
\qquad
\boxed{\tau=\frac{b_3}{\delta_3}},
```

故

```math
\gcd(L,\tau)=1.
```

第三分子的相应 tail normalization 只在其定义域内使用；不能从 \(\delta_3\) 的 denominator gcd 无条件推出 \(\delta_3\mid a_3\)。涉及 primitive tail numerator 的公式必须引用对应分支已经建立的 exact-recovery 定义。

Denominator recovery 与 decimal completion 真正需要共享的 denominator-side trace 可以写成

```math
\boxed{T_{\rm blk}=(b_1,b_2,b_3,10^\ell)},
```

或等价的 segmented word 形式

```math
\boxed{T_{\rm word}=(\beta,10^{m_2},10^{m_3},10^\ell)}.
```

给定该 trace，\(q,Q,G,\delta_3,L,\tau\) 以及全部 denominator-only valuation/gcd data 都是确定性函数。这个接口只减少重复状态，不关闭任何分支。

A1 的 historical saturated `L=1` 子支已经在 A1 后续工作中排除；它不再是当前 A1 frontier。当前 A1 权威前沿见 `branches/a1-only/README.md`。

---

<a id="c03-detail-src-0199-63-2"></a>
#### 三分支统一尾权 \(\kappa\)

三个分支的尾权可以统一写成同一个 branch-free 恒等式：

```math
\boxed{\kappa=\frac{10^{m_3}QG}{b_3}\in\mathbf Z_{>0}}.
```

证明只是把各分支原定义代回：

- A2/DD 有 \(\ell=m_3\)，故 \(L/\tau=10^{m_3}/b_3\)；
- A1 有 \(\ell=m_3-g\)，故 \(10^gL/\tau=10^{m_3}/b_3\)。

因此旧的两种写法

```math
\kappa=\frac{LQG}{\tau}\quad(A_2,DD),
\qquad
\kappa=\frac{10^gLQG}{\tau}\quad(A_1)
```

只是同一恒等式的 chamber-specific 展开。

公共窗口仍为

```math
\boxed{QG<\kappa\le10QG}.
```

这个统一式是本次外部整合后正式采纳的公共简化；它不依赖任何 DD closure 假设。

---

<a id="c03-detail-src-0199-63-3"></a>
#### Gap quadratic 与判别平方

令统一 gap 参数满足

```math
G(\mathcal R-r_3)=\frac\mu\nu,
\qquad \gcd(\mu,\nu)=1.
```

三个异常分支都得到

```math
\boxed{
D(\kappa+2G)\mu^2
-2G\kappa C\mu\nu
+\kappa D\mathcal N_{12}\nu^2=0.
}
```

于是必要整除为

```math
\boxed{\nu\mid D(\kappa+2G)},
\qquad
\boxed{\mu\mid\kappa D\mathcal N_{12}}.
```

定义

```math
\boxed{K_{C,D}=G^2C^2-D^2\mathcal N_{12}}.
```

存在有理 gap root 的必要条件是

```math
\boxed{
\kappa\bigl(\kappa K_{C,D}-2GD^2\mathcal N_{12}\bigr)=W^2
}
```

对某个整数 \(W\)。

这类 quadratic / discriminant 条件是 exact candidate 的投影证书。若在某个更完整的 recovery chart 中它们由同一 exact reconstruction 自动推出，就不能作为额外独立 obstruction 再次收费；具体独立性由对应分支 dependency audit 决定。

定义

```math
G_0=\gcd(\mathcal N_{12}\nu^2-\mu^2,2G\mu\nu).
```

已有公共结果

```math
\boxed{G_0\mid2G\mathcal N_{12}},
```

所以 recovery 中出现的额外 gcd 不能充当完全独立的无界素数储存池。

---

<a id="c03-detail-src-0199-63-4"></a>
#### Tail quadratic 与 denominator-tail certificate

在各分支已经建立相应 primitive-tail recovery 的定义域内，可得到统一 tail quadratic 与有理根整除。其最稳定、跨分支可直接使用的 denominator-side 结论是

```math
\boxed{10^\ell\mid\kappa^2(\kappa+2G)}.
```

由于第 6 节的 branch-free \(\kappa\) 公式，这个 certificate 的 denominator side 完全由

```math
(b_1,b_2,b_3,10^\ell)
```

决定。

令

```math
S_{12}=m_1+m_2.
```

由

```math
Q,G<10^{S_{12}}
```

以及 \(QG<\kappa\le10QG\)，得到公共粗尾长锥

```math
\boxed{\ell\le6S_{12}+3}.
```

于是 A2/DD 有

```math
\boxed{m_3\le6S_{12}+3},
```

A1 有

```math
\boxed{m_3-g\le6S_{12}+3}.
```

这些只是 prefix-uniform 高度约束，不是全局空性。

---


来源：`SRC-0199:63–291`。原文保全，当前论证以本节为准。

<a id="c04"></a>
### C04　完整素幂 denominator complement

**状态：已严格完成。** 任意分母、位数及既约分子。

依赖：[C02](#c02)

核对：正文推导；本次重写未为此项另增枚举。

<a id="c04-detail-src-0199-681-1"></a>
#### Denominator recovery 的完整素幂整除

**状态：已严格完成（必要条件）。** 令

```math
C_1=b_2 10^{m_3}+b_3,\quad
C_2=b_1 10^{m_2+m_3}+b_3,\quad
C_3=(b_1 10^{m_2}+b_2)10^{m_3}.
```

任意原 exact lift 必满足

```math
\boxed{b_i\mid\operatorname{lcm}(b_j,b_k,C_i)
\quad(\{i,j,k\}=\{1,2,3\}).}
```

逐素数证明：若 `ei>max(ej,ek)`，则该 sphere 坐标独占分母最大深度，
其 `yi` 为单位而另外两个为 `p` 的倍数，所以 `H²=yi²!=0 modp`，
`H` 为单位。原 word 给 `vp(beta)=ei+vp(alpha)>=ei`；
`beta-Ci` 是该分母乘十进制整数权重，亦含完整 `p^ei`，故
`vp(Ci)>=ei`。若最大值未独占，则其他分母已承载所需深度。
因此整除保留每个素数幂，不仅是 radical 支持。

特别地

```math
\boxed{b_1\mid\operatorname{lcm}(b_2,b_3,b_2 10^{m_3}+b_3).}
```

右端由最后两个分母确定，因而固定这两个分母后，第一分母的候选
可有效穷尽。对 `1<=b2,b3<=9`，粗界为 `b1<=9*9*99=8019`。
这不是无界后缀的统一上界。`C2,C3` 还含相应分母的位数，不能
照搬第一分母的有效有限性到全部三分母的并集。

对于 `p∤10`，第三项还给 tail 非十进制部分的深度界
`v_p(b3)<=max(v_p(b1),v_p(b2),v_p(Q))`。
这些整除均来自同一原 sphere/word，不构成额外高度预算。

---


来源：`SRC-0199:681–720`。原文保全，当前论证以本节为准。

<a id="c05"></a>
### C05　原 coefficient plane 的 norm 与二进分母条件

**状态：已严格完成。** 任意共同 content；D-norm 和正二进最大深度必要条件。

依赖：[C02](#c02)

核对：`norm-mod9`

对任意素数 \(p\)，记

```math
e_i=v_p(b_i),\qquad E=\max(e_1,e_2,e_3).
```

逐坐标 recovery

```math
v_p(\gcd(q,y_i))=E-e_i
```

把 denominator exponent pattern 精确送入整数球面。

对于奇素数 \(p\ne2,5\)，若最大赋值只在一块出现，则 complementary denominator relation 强迫另外两块的 \(p\)-进指数相等；pair-max 情形结合二平方和局部条件，会对 \(p\bmod4\) 产生严格限制。所有更细的 unique-max / pair-max 结论必须引用相应分支的已审计 lemma，不能从这张 skeleton 自动外推全局关闭。

对 \(p=2\)，必须区分 \(E_2=\max_i v_2(b_i)>0\) 与三个分母全奇。
若 \(E_2>0\)，在达到最大值的坐标上，既约性保证 \(a_i\) 为奇数，
故至少一个 \(y_i\) 为奇数。整数球面模 \(4\) 给出 \(H\) 为奇数，
且三个 \(y_i\) 中恰有一个奇数。因此

```math
\boxed{E_2>0\Longrightarrow\max_i v_2(b_i)\text{ 必须唯一取得}.}
```

若 \(E_2=0\)，不能直接断言 \(H\) 为奇数，也不能断言最大值唯一。
例如全偶球面坐标不被模 \(4\) 排除。DD 已在
[core.md §27.7](#c09) 单独处理全奇分母锥。
这项本地范围修正不声称找到了 exact-lift 反例。现行分支文档中的
2-adic locks 仍须在各自假设下使用。

若 `E2>=2`，模八还给出一个 denominator-only 必要条件：另外两块中
深度恰为 `E2-1` 的分母数量必须为偶数（零或二）。这些深度为正，
既约性使对应分子为奇数，故其 `yi²=4 mod8`；更浅分母的坐标平方
为零，最大深度坐标与 `H` 的奇平方都为一。因此单独一块相差一层
会给 `1=1+4 mod8`，矛盾。`E2=1` 时其他分子的奇偶自由，不能只数
分母。DD 对一位偶尾的完整应用见
[third-2-dominant 低层排除](RESEARCH.md#dd-model)（原始记录 SRC-0122）。

原 word equation 还给出一个更直接的接口：若 `b3` 为奇数，则完整
`beta=Q*10^m3+b3` 为奇数。假如 `E2>0`，上面的 sphere 条件使 `H`
为奇数，而 `q alpha` 为偶数，违反 `q alpha=H beta`。因此
```math
\boxed{b_3\text{ 奇}\Longrightarrow b_1,b_2,b_3\text{ 全奇}.}
```
这里仍不推断全奇分母下的 `H` 奇偶；它只排除奇尾分母与偶前缀分母
同时出现的无界状态。

因此 denominator prime graph 的作用是组织 prime supply 与 recovery depth，不是单独的 contradiction theorem。


<a id="c05-detail-src-0199-451-1"></a>
#### 原始 coefficient plane 的分母 norm 阻碍

**状态：已严格完成（跨分支必要条件与无界剩余类排除）。** 本节不要求
三个分母有相同三进赋值。仍使用原始六个十进制块，定义
```math
(t_1,t_2,t_3)
=(b_1 10^{n_2+n_3},b_2 10^{n_3},b_3),\qquad D=\beta,
```
```math
\boxed{\Delta_{\rm dec}=t_1^2+t_2^2+t_3^2-D^2.}
```
这里 `Delta_dec` 由三个分母和六块的位数决定，不含分子的数值。
若 exact lift 成立，则
```math
\boxed{\Delta_{\rm dec}\ge0,\qquad
\Delta_{\rm dec}\text{ 是两个有理平方之和}.}
\tag{D-norm}
```
特别地，若 `Delta_dec!=0`，每个 `p=3 mod4` 的赋值都必须为偶数。
这是一条原 sphere/word equation 的必要投影，不是额外独立的高度预算。

<a id="c05-detail-src-0199-451-2"></a>
#### 精确 Gaussian identity

依赖 §3，原 word equation 可以写成
```math
DH=t_1y_1+t_2y_2+t_3y_3.
```
令 `s=H+y3>0`，以及
```math
G_{\rm dec}=(D+t_3)(y_1+iy_2)-(t_1+it_2)s.
```
直接展开得到恒等式
```math
\begin{aligned}
N(G_{\rm dec})-\Delta_{\rm dec}s^2
={}&-(D+t_3)^2(H^2-y_1^2-y_2^2-y_3^2)\\
&+2(D+t_3)s(DH-t_1y_1-t_2y_2-t_3y_3).
\end{aligned}
\tag{D-norm-identity}
```
两括号由 sphere 与原 coefficient plane 同时为零。因此
`Delta_dec=N(G_dec/s)`，证明 (D-norm)，包括 `Delta_dec=0` 的情形。
对 `p=3 mod4`，两个整数平方之和若被 `p` 整除，则两个整数都被 `p`
整除；除尽共同 `p` content 后，该和的赋值为零。清除有理分母只改变
偶数赋值，故非零有理 norm 的 `p` 赋值必为偶数。

<a id="c05-detail-src-0199-451-3"></a>
#### 任意共同三进 content 下的模九排除

令
```math
j=\min_i v_3(b_i),\qquad c_i=b_i/3^j.
```
至少一个 `ci` 为三进单位。所有十进制权重为 `1 mod9`，所以
```math
\frac{\Delta_{\rm dec}}{3^{2j}}
\equiv\sum_i c_i^2-\left(\sum_i c_i\right)^2
=-2(c_1c_2+c_1c_3+c_2c_3)\pmod9.
```
若 pair sum 为 `3` 或 `6 mod9`，右侧恰被三整除而不被九整除，
故 `v3(Delta_dec)=2j+1`，与 (D-norm) 矛盾。因此得到无界排除
```math
\boxed{c_1c_2+c_1c_3+c_2c_3\equiv3\text{ 或 }6\pmod9
\Longrightarrow\varnothing.}
\tag{D9-general}
```
这覆盖任意分子、任意位数和任意三个分母的三进赋值差。
例如 `ci=(1,3,3) mod9` 已被排除，超出 §10.1 的共同赋值范围。
当 `ci` 同为单位且同模三符号时，`sum ci=0 mod3`，此条件恰与
§10.1 的 (D9) 相同；`(1,1,4) mod9` 是允许类，不能误报为空。

同一核对脚本穷尽 702 个至少含一个三进单位的模九系数类，144 类
因 (D9-general) 被排除；其余 558 类在本原 sphere/plane 模九投影上
有允许点。这些允许点不证明有原 exact-lift 解。脚本另以符号展开核对
(D-norm-identity)。对其他 inert primes 的偶赋值要求仍只是一条必要条件，
本节没有从它推出任一完整分支关闭。


来源：`SRC-0199:310–360`；`SRC-0199:451–528`。原文保全，当前论证以本节为准。

<a id="c06"></a>
### C06　模九无界排除及十进制幂分母推论

**状态：已严格完成。** 共同三进单位与一般 pair-sum 3/6 阻碍；允许类仍不是解。

依赖：[C05](#c05)

核对：`norm-mod9`

<a id="c06-detail-src-0199-363-1"></a>
#### 同三进赋值分母的模九阻碍

**状态：已严格完成（跨分支必要条件与无界子域排除）。** 假设
```math
v_3(b_1)=v_3(b_2)=v_3(b_3)=E\ge0,\qquad
c_i:=b_i/3^E\equiv c\pmod3\quad(i=1,2,3),
```
其中选取 `c=1` 或 `c=-1`。若原 exact lift 成立，则必须有
```math
\boxed{c_1^2+c_2^2+c_3^2\equiv0\pmod9,}
\qquad
\boxed{c_1+c_2+c_3\equiv6c\pmod9.}
\tag{D9}
```
两条件在上述同剩余类假设下等价。因此违反 (D9) 的整个分母子域为空，
无论三个分子和六个块的位数如何增长。它不覆盖不同三进赋值或不同
`c_i mod3` 的状态，也不证明通过 (D9) 的状态存在。

<a id="c06-detail-src-0199-363-2"></a>
#### 固定十进制权重上的三进正规化

依赖 §3 的 canonical sphere 和原始 word equation。令
```math
q=3^E q',\qquad q'=\operatorname{lcm}(c_1,c_2,c_3),
\qquad y_i=q'a_i/c_i.
```
把 `q alpha=H beta` 除以 `3^E` 得到精确线性式
```math
\sum_i c_i X_i y_i=H\sum_i c_i Y_i,
```
其中 `(X_1,X_2,X_3)=(10^{n_2+n_3},10^{n_3},1)`，
`(Y_1,Y_2,Y_3)=(10^{m_2+m_3},10^{m_3},1)`。

取 `t=min(v3(y1),v3(y2),v3(y3),v3(H))`，令 `z_i=y_i/3^t`、`h=H/3^t`。
球面与这条**固定权重**线性式都可同时除以 `3^t`；这里不声称
正规化后的坐标仍恢复原十进制块，也不构造 decimal descent。
于是至少一个 `(z1,z2,z3,h)` 是三进单位，并有
```math
\sum_i z_i^2=h^2,\qquad
\sum_i c_i z_i\equiv h\sum_i c_i\pmod9,
\tag{D9-spine}
```
因为所有 `X_i,Y_i` 均为 `1 mod9`。

若 `3 not|h`，球面模三说明恰有一个 `z_i` 为单位；线性式模三却要求
`sum z_i=0`，矛盾。因此 `3|h`。球面模三与三进本原性随后说明
三个 `z_i` 都为单位；它们的和为零又强迫三者同为 `sigma mod3`，
其中 `sigma=1` 或 `sigma=-1`。

写
```math
z_i=\sigma+3t_i,\qquad c_i=c+3u_i.
```
球面模九给出
```math
3+6\sigma\sum_i t_i\equiv0\pmod9,
\qquad\sum_i t_i\equiv\sigma\pmod3.
```
另一方面 `3|h` 且 `3|sum c_i`，所以 (D9-spine) 的右端为零模九。
代回左端并除以三，得到
```math
c\sigma+c\sum_i t_i+\sigma\sum_i u_i\equiv0\pmod3,
\qquad\sum_i u_i\equiv c\pmod3.
```
因此 `sum c_i=3c+3 sum u_i=6c mod9`，且
`sum c_i^2=3+6c sum u_i=0 mod9`，证明 (D9)。

**推论。** 若 `c_1=c_2=c_3`，则 `sum c_i^2=3c_1^2 not=0 mod9`，
故所有等分母候选为空。这重新在公共框架中给出了等分母排除，
同时把它扩展到许多不相等的分母；它不借用外部 DD closure 前提。
更一般，若 `c1,c2,c3` 具有同一模九单位剩余类，也同样为空。
因此对任意正整数 `b` 与非负整数 `e1,e2,e3`，整个
`(b1,b2,b3)=(b*10^e1,b*10^e2,b*10^e3)` 十进制分母射线均被排除；
特别地三个分母都是十进制幂的状态已全部关闭，不留 equal-prefix 例外。

<a id="c06-detail-src-0199-363-3"></a>
#### 有限局部证书与边界

证书命令与覆盖见 [统一核对目录](CHECKS.md)。

 核对：穷尽模九的 540 个三进本原球面剩余类，以及 54 个
`c_i` 为单位且同模三符号的有序分母剩余类；其中 36 类没有满足线性式
的本原点，18 类只在这个局部投影上允许点。脚本还核对 (D9) 两种
写法等价与等分母推论。有限证书只核对完整模九投影；上面的无界
排除来自对任意原候选的严格约化，不是把有界整数枚举外推。


来源：`SRC-0199:363–449`。原文保全，当前论证以本节为准。

<a id="c07"></a>
### C07　单位前缀与一位尾分母排除

**状态：已严格完成。** b1=b2=1，1≤b3≤9，全部正分子。

依赖：[C05](#c05)、[C04](#c04)

核对：`dd-unit-prefix`

<a id="c07-detail-src-0199-529-1"></a>
#### 单位前缀分母与一位第三分母全部排除

**状态：已严格完成（整个无界分母子域）。** 假设
```math
\boxed{b_1=b_2=1,\qquad1\le b_3\le9.}
```
对任意正整数 `a1,a2,a3` 及任意三分子位数，均不存在原 exact lift。
本节没有限制分子的高度，也不依赖有界搜索。

由 §3，`q=b3`，故
```math
(y_1,y_2,y_3)=(b_3a_1,b_3a_2,a_3),\qquad
H^2=y_1^2+y_2^2+y_3^2,\qquad b_3\alpha=H(110+b_3),
```
其中 `H` 是正整数，`gcd(a3,b3)=1`。按第三分母作穷尽分支：

1. `b3=1`：三个分母相等，由 §10.1 排除。
2. `b3=3,6,9`：取 `p=3`；`b3=7`：取 `p=7`。球面模 `p` 给
   `H²=a3²!=0 modp`，所以 `H` 是 `p`-unit；但 `110+b3` 也是
   `p`-unit，而 `b3 alpha` 被 `p` 整除。整数 word equation 矛盾。
3. `b3=2,4,6,8`：既约性使 `a3` 奇，球面使 `H` 奇，原分子 word
   `alpha=A12*10^n3+a3` 也奇。若 `v2(b3)=1`，`110+b3` 被四整除；
   若 `v2(b3)>=2`，`110+b3` 恰含一个二。两种情况都使 word equation
   的两端二进赋值不同。与上一项重叠的 `b3=6` 不影响穷尽性。
4. `b3=5`：word equation 给 `H=alpha/23`，故
   `H=2a3 mod5`，因为 `alpha=a3 mod5`。球面却给 `H²=a3² mod5`。
   于是 `4a3²=a3² mod5`，与 `5 not|a3` 矛盾。

这些情形覆盖全部一位正分母，证明命题。DD 中 `m3=1,n3>1` 的
单位前缀 slice 是本节的一个完整推论，见
[DD 低层记录](#dd-02)。它不覆盖一般前缀分母，
也不把 DD、A2 或 A1 任何完整分支提升为已关闭。


来源：`SRC-0199:529–562`。原文保全，当前论证以本节为准。

<a id="c08"></a>
### C08　一位尾分母的 prefix 整除

**状态：已严格完成。** b3≤9；一般位数上 b3|10Q，unique-five-tail 的单位范围逐项保留。

依赖：[C04](#c04)

核对：正文推导；本次重写未为此项另增枚举。

<a id="c08-detail-src-0199-648-1"></a>
#### 一位第三分母的无界 prefix 整除

**状态：已严格完成（必要条件，不是该子域空性）。** 令
`Q=b1*10^m2+b2`。不论三个分子位数及分支为何，只要 `1<=b3<=9`，
原 exact lift 必满足

```math
\boxed{b_3\mid10Q.}
```

这里两个前缀分母可任意大。依赖 §3 的 `q alpha=beta H`、整数球面，
以及 §10 已证明的正二进最大分母深度唯一性。证明如下。
若结论失败，取素数 `p` 满足
`e3=v_p(b3)>t=v_p(10Q)`。因 `beta=10Q+b3`，`v_p(beta)=t`。
原 word equation 给 `v_p(R)=v_p(alpha)-t>=-t`。

- `p=5` 不可能：一位 `b3` 的五进深度至多一，而 `10Q` 至少含一个五。
- `p=2` 时，正最大深度 `E=max_i v2(bi)>=e3` 唯一取得，球面中仅一个
  `yi` 为奇数，故 `H` 奇、`v2(R)=-E<=-e3<-t`，矛盾。
- 其余可能只有 `p=3,7`，均为 inert prime。三个分母不能同时达到最大
  深度 `E`：若同时达到，则 `e3=E` 且 `v_p(Q)>=E`，与 `e3>t` 矛盾。
  因此球面最浅层至多有两个单位坐标。一个单位平方不会为零；两个
  单位平方之和也不会在 `p=3 mod4` 上为零。所以 `H` 为单位，
  `v_p(R)=-E<=-e3<-t`，仍矛盾。

穷尽一位分母的素因子即得结论。DD 中此条件等价于 gcd-normal
`v=b3/gcd(10Q,b3)=1`，其真实恢复字典见
[一位 tail 的 v=1 reader](#dd-06)。
它关闭的是违反该整除的整个无界前缀状态；通过整除者仍须满足原
分子 word、球面、位数与既约性，不能因此称整个一位 tail 分支为空。


来源：`SRC-0199:648–679`。原文保全，当前论证以本节为准。

<a id="c09"></a>
### C09　后两分母一位的完整子域

**状态：有限证书。** b1 任意、b2,b3≤9、三个正分子任意；全部参数归约后有限末端。

依赖：[C01](#c01)、[C04](#c04)、[C05](#c05)、[C08](#c08)

核对：`suffix-tail-one`、`suffix-tail-one-factored`、`dd-suffix`、`dd-suffix-factored`、`cpp-tail-one`、`cpp-tail-one-factored`、`cpp-suffix`、`cpp-suffix-factored`

本命题将尾分子一位与至少两位两片接在同一个 denominator projection 后。后面的 DD 原变量只用于 n3≥2 的证明。

<a id="c09-detail-src-0199-724-1"></a>
#### 后两分母为一位的完整子域

**状态：有限证书（先证明全部高度归约，完整覆盖指定子域）。**
任意 `b1>=1`、`1<=b2,b3<=9` 和任意正既约分子均不可能给出原
exact lift。第一分母与三个分子没有预设搜索上界。本节合并
`n3>=2` 的 [DD 完整证书](#dd-03)
与以下 `n3=1` 证书；不覆盖多位第二或第三分母。

<a id="c09-detail-src-0199-724-2"></a>
#### 分母投影与其必要条件

此时 `m2=m3=1`，`Q=10b1+b2`、`D=100b1+10b2+b3`。
§10.6 的完整素幂整除先给
`b1|lcm(b2,b3,10b2+b3)`，共 **994** 个分母三元组，最大第一分母
为 `6408`。再应用以下来自原 word/sphere 的必要条件：

1. §10.5 的 `b3|10Q`。
2. 正二进最大深度 `E` 唯一；`E>0` 时尾分母必须偶，尾分子既约
   为奇，从而 `v2(D)=E`。若 `E>=2`，其他分母中恰有一个深度为
   `E-1` 会在 sphere 模八产生 `H²=5 mod8`，必须排除。
3. 任一素数的最大深度独占时，或 inert prime 的最大深度只由两个
   分母取得时，最浅 sphere 层不能为零，故 `vp(D)>=E`。
4. §10.2 的分母 norm：剥去共同三进深度后，三个单位化分母的
   pair-product sum 不得为 `3/6 mod9`。
5. 若 `b3=5` 且 `5∤b1b2`，则 `Q=4 mod5`。确实，写 `q=5q0`，
   原 word 给 `q0*a3=(2Q+1)H mod5`，sphere 给
   `H²=(q0*a3)² mod5`；单位平方消去得 `(2Q+1)²=1 mod5`。
   `Q=b2!=0 mod5` 排除 `Q=0`，只余 `Q=4`。这里没有使用仅适用于
   `n3>=2` 的更强模二十五条件。

这些条件适用于任意分子位数。其完整投影正好留下 **19** 个三元组：

```text
(11,1,1) (5,1,5) (15,1,5) (7,2,8) (33,3,3)
(5,5,1) (15,5,1) (85,5,1) (255,5,1) (265,5,3)
(1,5,5) (11,5,5) (55,5,5) (40,5,6) (280,5,6)
(1,6,8) (15,7,5) (77,7,7) (99,9,9)
```

它们只是必要条件投影，尚未判为原解。DD 的模二十五投影恰好留下
同一列表；完整子域结论仍须以下分子重构证书。

<a id="c09-detail-src-0199-724-3"></a>
#### `n3=1` 的全部分子高度归约

固定上述分母，令 `q=lcm(b1,b2,b3)`、`X=10^n2`；尾分子
`1<=a3<=9`。若 `n2>=2`，原拼接与三角不等式给

```math
\frac{10Xa_1}{D}<R<\frac{a_1}{b_1}+\frac{X}{b_2}+\frac9{b_3},
\qquad
a_1< F(X):=\frac{X/b_2+9/b_3}{10X/D-1/b_1}.
```

`D/b1<=199`，所以 `X>=100` 时分母严格正。`F(X)` 的导数严格负，
故 `a1<=A1=ceil(F(100))-1`，在这 19 组中 `A1<=823`。
整数 sphere 中 `H-(q/b2)a2` 为正整数，因而

```math
a_2<\frac{qb_2}{2}
\left[\left(\frac{A_1}{b_1}\right)^2+
      \left(\frac9{b_3}\right)^2\right].
```

取严格整数上界后，全部 19 组都满足 `n2<=5`。程序针对实际 `X`
再取 `ceil(F(X))-1`，枚举 `a1,a3` 并恢复所有正整数 `a2`。
若 `n2=1`，仅枚举 `1<=a2,a3<=9`，直接恢复**全部**正整数 `a1`，
不对它作高度截断。两片均从原式
`q² alpha²=D² sum((q/bi ai)²)` 生成二次方程；标准和 factored
reader 穷尽所有正整数根，包括二次项为零的线性退化，并检查实际
位数、既约性和原方程。

<a id="c09-detail-src-0199-724-4"></a>
#### 精确证书与独立核对

证书命令与覆盖见 [统一核对目录](CHECKS.md)。

`n3=1` 的两种 Python reader 各核对 **45,015** 行，`n3>=2` 的两种
reader 各核对 **3,759,479** 行，均为零个原解。独立 C++ 程序重新
生成全部分母、精确有理边界和二次方程，两种判别式逐组得到相同
计数。C++ 使用有溢出检查的 256 位整数，所有判别式在正文归约盒
中小于 `2^190`；超出算术范围会直接报错。所有原生 `uint64` 边界
乘式的粗上界为 `70,701,190,630,418,880<2^56`。本子域二次项不会
退化：恢复 `a3` 时 `D>b3`；恢复 `a2` 时 `D` 末位非零而
`10^n3*b2` 末位为零；尾一位的两个恢复则分别有 `D>10b2`、
`D>100b1`。C++ 对此直接断言，Python 另具通用线性退化处理。
完整 UBSan 四模式复算没有诊断。单次标准或 factored
覆盖合计 **3,804,494** 行。

这里的有限计算闭合来自已证明的全部参数归约，绝不把截断搜索
当作无界证明。三个完整异常分支仍有多位分母的无界核心。

---


<a id="c09-detail-src-0122-3232-1"></a>
#### 最后两个分母均一位、第一分母无界的完整 DD 层关闭

**状态：已严格完成（无界 denominator 归约 + 全局 numerator bounds +
精确有限证书）。** 本节完整关闭

```math
\boxed{1\le b_2,b_3\le9,\qquad b_1\ge1,\qquad n_3>m_3=1.}
\tag{Last-two-single-digit-DD-domain}
```

全部分子与第一分母最初无界。因 `m_2=m_3=1,n_2>=1,n_3>=2`，
`k_12=n_2+n_3-2>0` 自动成立。本节扩大 §27.7.3 的作用域，不使用
canonical、frozen top-DD 或任何渐近高度预算。`n_3=1`、两位以上的
第二或第三分母不属于本结论。

**公开 first-denominator divisor bound。** 对任意完整 Exact-Lift
候选（不限本节的 denominator digit lengths），令

```math
\beta=b_1 10^{m_2+m_3}+C,\qquad C=b_2 10^{m_3}+b_3.
```

对每个素数 `p`，写 `e_i=v_p(b_i)`、`c=v_p(C)`。若
`e_1>max(e_2,e_3,c)`，第一分数独占最高 denominator depth，sphere
给 `v_p(R)=-e_1`；而 `v_p(b_1 10^{m_2+m_3})>=e_1>c`，故
`v_p(beta)=c<e_1`，原 word `R=alpha/beta` 给 `v_p(R)>=-c`，矛盾。
因此逐 prime power合并得到

```math
\boxed{b_1\mid\operatorname{lcm}(b_2,b_3,b_2 10^{m_3}+b_3).}
\tag{Public-first-denominator-divisor-bound}
```

这个是 denominator-only necessary condition，对三个分支统一成立，
既不是独立 height payer，也不直接关闭一般分母族。本节 `m_2=m_3=1`
时，它将任意 `b_1` 完整归约为

```math
b_1\mid\operatorname{lcm}(b_2,b_3,10b_2+b_3).
```

遍历九乘九个 `(b_2,b_3)` 的全部 positive divisors，得到 `994` 个
triples，最大 `b_1=6408`。这是有证明 bound之后的完整有限 denominator
表，仍需 numerator height归约才能关闭原候选。

**确定性 denominator filters。** 对每个 divisor triple令
`Q=10b_1+b_2,D=10Q+b_3`，依次只使用以下 necessary conditions：

1. [gcd-normal §11](#dd-06)
   的公开一位尾条件 `b_3|10Q`。
2. §27.7 的 positive二进 max唯一；奇尾时两个前缀必须奇，偶尾时
   reduced `a_3` 与 numerator word奇，故 `v_2(D)=max_i v_2(b_i)`。
3. §27.7.4 的 `E_2>=2` 时不能恰有一个 denominator位于 `E_2-1`。
   `E_2=1` 不套用这个 denominator计数。
4. 对每个 `p|lcm(b_i)`，若最高 denominator depth `E_p` 唯一，sphere
   给 `v_p(R)=-E_p`；若恰两个坐标取得最高且 `p=3 mod4`，其 leading
   unit squares不能抵消，仍给同样结论。因此这两类都必须
   `v_p(D)>=E_p`。其它 multiple-max状态不按这个条件擅自排除。
5. [原 denominator norm](#c06)
   的 min-three-content条件：令 `r=min_i v_3(b_i)`、`c_i=b_i/3^r`。
   因所有 decimal weights模九为一，
   `Delta_dec/3^(2r)=-2(c_1c_2+c_2c_3+c_3c_1) mod9`。若 pair sum为
   `3` 或 `6 mod9`，则 `v_3(Delta_dec)=2r+1` 为奇数，违反非零
   rational Gaussian norm，故排除。这不要求三个 `c_i` 同 mod3。
6. [gcd-normal §11.1](#dd-07)
   的 `b_3=5,5∤b_1b_2,n_3>=2 => Q=24 mod25`。

完整确定性 projection留下下面十九个 triples。没有对 denominator
允许状态作 emptiness推断，也不依赖其它低层 slice已经关闭；下一步对
全部十九个状态统一作 numerator归约和精确证书。

**高 tail 归约。** 固定一个 triple，写
`q=lcm(b_i),X=10^(n_2),Y=10^(n_3)`。原 parents为

```math
q\mathscr A=DH,\quad H^2=\sum_i(q a_i/b_i)^2,\quad
\mathscr A=a_1XY+a_2Y+a_3.
\tag{Last-two-single-digit-original-parents}
```

令 `N=min{j>=2:10^j b_2>D}`、`Y_0=10^N`。对 `n_3>=N`，严格
triangle `R<sum_i a_i/b_i` 给

```math
a_1(XY-D/b_1)+a_2(Y-D/b_2)<a_3(D/b_3-1)<YD/b_3.
```

这里 `Y-D/b_2>0`，故

```math
\boxed{a_1\left(X-\frac D{b_1Y}\right)<\frac D{b_3}.}
\tag{Last-two-digit-high-tail-triangle}
```

分母 `X-D/(b_1Y)` 为正：`Y>=Y_0>D/b_2` 且 `b_2<=9,b_1>=1`，
故 `D/(b_1Y)<9<X`。于是 `a_1>=1` 先给完整 `X` bound
`X<D/b_3+D/(b_1Y_0)`。令 `J_h` 为满足该 strict bound的最大
`n_2`，则 `a_2<=10^(J_h)-1`；令

```math
A_h=\left\lceil\frac{D/b_3}{10-D/(b_1Y_0)}\right\rceil-1.
```

对所有高 tail `a_1<=A_h`。Integer sphere的 `H-y_3>=1`、
`H+y_3>2y_3` 再给

```math
a_3<\frac{b_3q}{2}
\left((A_h/b_1)^2+((10^{J_h}-1)/b_2)^2\right)=:B_h.
\tag{Last-two-digit-high-tail-sphere-bound}
```

取 `floor_strict(B_h)=ceil(B_h)-1` 的实际 digit length作 `K_h`，则
`N<=n_3<=K_h`。在有限 certificate中，对每个实际 `X,Y` 还用
`a_1<(D/b_3)/(X-D/(b_1Y))`，避免将同一个 uniform `A_h` 无必要地
复制到所有 `n_2`。这只是tightening已证明的 bound，不增加筛除假设。

**短 tail 归约。** 对每个 `n_3=2,...,N-1` 固定 `Y=10^(n_3)`，从
原 word lower与实际 triangle得到

```math
\boxed{a_1<\frac{X/b_2+(Y-1)/b_3}{XY/D-1/b_1}=:B_1(X,Y).}
\tag{Last-two-digit-short-tail-triangle}
```

分母对 `X>=10,Y>=100` 始终为正，因为
`D/b_1=100+(10b_2+b_3)/b_1<=199<1000<=XY`。`B_1` 随 `X` 严格
递减，其导数的 numerator为
`-1/(b_1b_2)-Y(Y-1)/(Db_3)<0`。因此
`A_Y=ceil(B_1(10,Y))-1` 给全部 `n_2` 的 uniform `a_1` bound。
Integer sphere的 `H-y_2>=1` 再给

```math
a_2<\frac{b_2q}{2}\left((A_Y/b_1)^2+((Y-1)/b_3)^2\right)=:B_Y.
\tag{Last-two-digit-short-tail-sphere-bound}
```

`floor_strict(B_Y)` 的 digit length给 `J_Y`，故 `1<=n_2<=J_Y`。
在 certificate中每个实际 `X` 继续使用 `floor_strict(B_1(X,Y))`。
这完成所有十九个 triple、所有 `n_3>=2` 与所有原始 numerator lengths
的完整归约；没有任意设置的 first-numerator cutoff。

**参数盒与 exact certificate。** 下表的高盒记为 `(J_h,K_h,A_h)`；
短盒记为 `n_3:(J_Y,A_Y)`。所有 caps由上述 exact rational expressions
计算，`--show-bounds` 还输出完整 `a_2/a_3` integer caps。

| `(b_1,b_2,b_3)` | `N` | 高盒 | 短盒 | quadratic rows |
|---|---:|---|---|---:|
| `(11,1,1)` | 4 | `(3,7,111)` | `2:(5,134); 3:(7,113)` | 134406 |
| `(5,1,5)` | 3 | `(2,6,10)` | `2:(4,17)` | 2592 |
| `(15,1,5)` | 4 | `(2,6,30)` | `2:(4,50); 3:(6,32)` | 22788 |
| `(7,2,8)` | 3 | `(1,4,9)` | `2:(4,14)` | 1070 |
| `(33,3,3)` | 4 | `(3,7,111)` | `2:(5,134); 3:(7,113)` | 61848 |
| `(5,5,1)` | 3 | `(2,4,55)` | `2:(6,62)` | 6590 |
| `(15,5,1)` | 3 | `(3,6,156)` | `2:(6,174)` | 17920 |
| `(85,5,1)` | 4 | `(3,7,855)` | `2:(7,960); 3:(9,864)` | 797290 |
| `(255,5,1)` | 4 | `(4,9,2557)` | `2:(7,2868); 3:(9,2583)` | 1726988 |
| `(265,5,3)` | 4 | `(3,8,885)` | `2:(7,1032); 3:(9,898)` | 636680 |
| `(1,5,5)` | 2 | `(1,3,3)` | — | 48 |
| `(11,5,5)` | 3 | `(2,5,23)` | `2:(5,28)` | 3528 |
| `(55,5,5)` | 4 | `(3,7,111)` | `2:(5,134); 3:(7,113)` | 88344 |
| `(40,5,6)` | 3 | `(2,6,68)` | `2:(5,83)` | 2910 |
| `(280,5,6)` | 4 | `(3,9,468)` | `2:(6,576); 3:(8,477)` | 91110 |
| `(1,6,8)` | 2 | `(1,3,2)` | — | 12 |
| `(15,7,5)` | 3 | `(2,5,31)` | `2:(6,37)` | 3102 |
| `(77,7,7)` | 4 | `(3,7,111)` | `2:(5,134); 3:(7,113)` | 100405 |
| `(99,9,9)` | 4 | `(3,7,111)` | `2:(5,134); 3:(7,113)` | 61848 |

使用 §27.7.3 从原 `qmathscr A=DH` 与 sphere直接消元所得的 exact
quadratic reader。高盒枚举 `a_1,a_2`、重构 `a_3`；短盒枚举
`a_1,a_3`、重构 `a_2`，两盒都核对实际 digit interval与全部
reducedness。Unknown `a_3` 的 leading coefficient非零，因为 `D>b_3`；
unknown `a_2` 的 leading coefficient非零，因为 `D` 的末位非零，不能
等于 `10^(n_3)b_2`。

两个独立 discriminant readers均对全部十九个状态给
`3,759,479` 个 quadratic rows、零个 exact解。Numerator证书不再加
额外 norm/length预筛；denominator投影的每一项已在上文证明为 necessary。

证书命令与覆盖见 [统一核对目录](CHECKS.md)。

独立 C++ certificate重新生成 `994` 个 divisor triples、十九个 states与
全部 exact rational bounds。它使用 checked 256-bit整数；在上表更粗的
uniform boxes中，高盒 `K<2^55,W<2^151`，discriminant `4D^2W<2^183`，
短盒更小，故统一 `<2^190` 的保守界确保全部运算处于所选整数宽度内。
Python standard / factored与独立 C++ standard / factored四次运行的
各状态 row counts完全一致，均总计 `3,759,479` 行、零个 exact解。

证书命令与覆盖见 [统一核对目录](CHECKS.md)。

因此 `(Last-two-single-digit-DD-domain)` 整层为空。这里有限证书有明确的
全局 denominator / numerator归约承担无界覆盖；不能将有限程序空表
直接外推到两位以上的第二或第三分母，DD全局分支仍开放。


来源：`SRC-0199:724–824`；`SRC-0122:3232–3437`。原文保全，当前论证以本节为准。

<a id="c10"></a>
### C10　三个一位分母的独立复核

**状态：有限证书。** b1,b2,b3≤9；作为 C09 的子域推论及独立 reader 验证。

依赖：[C09](#c09)

核对：`all-single-digits`、`all-single-digits-factored`、`dd-single-digits`

<a id="c10-detail-src-0199-564-1"></a>
#### 三个一位分母的完整高度归约与有限证书

**状态：有限证书（经证明的高度归约覆盖整个指定分母子域）。**
对任意正既约分子，若 `1<=b1,b2,b3<=9`，则原 exact lift 不存在。
这里分子的高度没有作为输入假设；以下推导先覆盖全部分子位数，
再进行有限精确计算。一般的多位分母仍不在结论中。

依赖 §3 的整数球面与原 word equation。令
`q=lcm(b1,b2,b3)<=729`、`ci=q/bi`、`D=100b1+10b2+b3<=999`，
以及 `X=10^n2,Y=10^n3`。若有原解，则

```math
\alpha=(a_1X+a_2)Y+a_3,
\qquad q\alpha=DH,
\qquad H^2=\sum_i(c_i a_i)^2,\quad H\in\mathbf Z_{>0}.
```

三个比值均正，故严格三角界给 `alpha<D(a1+a2+a3)`。
另对任一坐标 `yi=ci ai`，正整数 `H-yi>=1` 给出统一 gap 界

```math
a_i<\frac{q b_i}{2}\sum_{j\ne i}(a_j/b_j)^2.
\tag{SD-gap}
```

这是因为 `sum_{j!=i} yj²=(H-yi)(H+yi)>2yi`。
以下五个互不重叠的情形覆盖全部正整数 `n2,n3`。

| 位数情形 | 有限枚举的已知分子 | 精确重构的分子 |
| --- | --- | --- |
| `3<=n3<=8,n2=1,2` | `1<=a1<=110`，`a2` 为 `n2` 位 | `a3` |
| `n3=2,2<=n2<=8` | `1<=a1<=22,10<=a3<=99` | `a2` |
| `n3=2,n2=1` | `1<=a2<=9,10<=a3<=99` | 任意高度的 `a1` |
| `n3=1,3<=n2<=8` | `1<=a1<=111,1<=a3<=9` | `a2` |
| `n3=1,n2=1,2` | `a2` 为 `n2` 位，`1<=a3<=9` | 任意高度的 `a1` |

**第一行的无界归约。** 当 `n3>=3`，`Y>=1000>D`。三角界改写为
`a1(XY-D)<(D-Y)a2+(D-1)a3<(D-1)Y`，所以
`a1(X-D/Y)<D-1<=998`。`X>=1000` 时左侧至少 `999.001`，矛盾；
因此 `n2<=2,a2<=99`。又 `X-D/Y>=9.001`，故
`a1<998/9.001<111`。由 (SD-gap)，
`a3<6561*(110²+99²)/2<10^8`，所以 `n3<=8`。

**第二行的无界归约。** 当 `n3=2,n2>=2`，三角界给
`a1<999(X+99)/(100X-999)`。右侧随 `X` 递减，在 `X=100` 时为
`198801/9001<23`，故 `a1<=22`。再由 (SD-gap)，
`a2<6561*(22²+99²)/2<10^8`，故 `n2<=8`。

**第四行的无界归约。** 当 `n3=1,n2>=3`，同理
`a1<999(X+9)/(10X-999)`。在 `X>=1000` 上右侧递减且不超过
`1007991/9001<112`，故 `a1<=111`。由 (SD-gap)，
`a2<6561*(111²+9²)/2<10^8`，故 `n2<=8`。
其余两行只枚举已知的短分子，不截断第一分子的高度。

**精确整数二次重构。** 固定一行中的两个已知分子后，记未知分子为
`x`、其 word coefficient 为 `Cx`、其 sphere coefficient 为 `cx`，
并写 `alpha=Cx*x+K`、其余 sphere 平方和为 `S`。原方程恰为

```math
A x^2+B x+C=0,
\quad A=q^2 C_x^2-D^2 c_x^2,\quad
B=2q^2 C_xK,\quad C=q^2K^2-D^2S.
```

脚本用标准整数判别式 `B²-4AC` 穷尽所有正整数根，逐个检查实际
位数、既约性与原方程。`A=0` 时按 `B>0` 的线性方程处理，不跳过
退化情形。另一 reader 独立使用恒等式
`B²-4AC=4D²(q² cx² K²+A S)`；两种 reader 都使用整数平方根，
没有浮点容差，也不依赖模类或 norm 预筛。

证书命令与覆盖见 [统一核对目录](CHECKS.md)。

两次运行均覆盖 **26,836,101** 个既约已知分子二次重构行，五行计数
依次为 `20,104,038 / 4,258,548 / 259,380 / 1,927,530 / 286,605`，
原解数均为 **0**。`n3>=2` 的前三行另由
[DD 专用证书](RESEARCH.md#dd-model)（原始记录 SRC-0122）
独立核对。这一完整有限证书只关闭指定的一位分母子域；它没有给
多位分母统一上界，不能由此推出三个异常分支已关闭。


来源：`SRC-0199:564–647`。原文保全，当前论证以本节为准。

<a id="a2"></a>
## A2 分支

<a id="a2-g01"></a>
### A2-G01　全部 A2 的第一块绝对界与第三比值窗

**状态：已严格完成。** 全部原始正既约 A2 候选，不要求 deep-even、特殊 source 或分母赋值。

依赖：[C01](#c01)

核对：`a2-first-block` 核对配方、导数和严格常数；无界归约由下面的证明给出。

#### 相邻位数边界

A2 中令 \(k=s_3\ge1\) 且 \(s_2\le-k\)。位数窗给出

```math
r_2<10^{s_2+1}\le10^{1-k},\qquad r_3>10^{k-1}.
```

第一 carrier 不超过 \(r_1<\mathcal R\)，第二 carrier 因而必须严格超过
\(\mathcal R\)：\(10^k r_2>\mathcal R>r_3\)。左侧小于 10，右侧大于
\(10^{k-1}\)，所以 \(k\ge2\) 不可能。若 \(k=1,s_2\le-2\)，第二
carrier 小于 1，而 \(r_3>1\)，也矛盾。因此

```math
\boxed{s_3=1,\qquad s_2=-1,\qquad m_2\ge2.}
```

#### 原式给出的严格 prefix 不等式

本节暂记 \(A=a_1,B=b_1,T=10^{m_2},U=10^{m_3}\)，以及

```math
x=\frac{b_2}{T},\qquad z=r_2,\qquad w=r_3,\qquad
\varepsilon=\frac{b_3}{TU}.
```

位数窗是 \(1/10\le x<1\)、\(xz=a_2/T<1/10\)、\(w>1\)，从而
\(0<z<1\)。把原拼接等式除以 \(TU\) 得到

```math
(B+x+\varepsilon)\mathcal R=A+10xz+\varepsilon w,
\qquad \mathcal R=\sqrt{(A/B)^2+z^2+w^2}.
```

由于 \(\mathcal R>w\)，这里保留了一个严格余量：

```math
\boxed{(B+x)\mathcal R=A+10xz-\varepsilon(\mathcal R-w)<A+10xz.}
\tag{A2-prefix-strict}
```

#### 第一分母只能为 1 或 2

Cauchy 不等式作用于 \((A/B,\sqrt{z^2+w^2})\) 和
\((B,\sqrt{x(2B+x)})\)，给出

```math
A+\sqrt{x(2B+x)}\sqrt{z^2+w^2}\le(B+x)\mathcal R<A+10xz.
```

平方并除以 \(xz^2>0\)，再用 \(w/z>10x\)，得到

```math
(2B+x)(1+100x^2)<100x,
\qquad 2B+x<\frac{100x}{1+100x^2}\le5.
```

最后一步等价于 \((10x-1)^2\ge0\)。由于 \(x\ge1/10\)，
\(B<49/20\)，故正整数 \(B\) 只能为 1 或 2。

#### 第一分子的上界

由 (A2-prefix-strict) 有 \(B\mathcal R-A<x(10z-\mathcal R)\)。左侧正，
所以 \(10z-\mathcal R>0\)。再用 \(x<1/(10z)\)，得到

```math
\left(B+\frac1{10z}\right)\sqrt{A^2/B^2+1+z^2}
<\left(B+\frac1{10z}\right)\mathcal R<A+1.
\tag{A2-numerator-cap}
```

令 \(c_0=A^2/B^2+1\)。左侧作为 \(z\) 的函数，其导数为

```math
\frac{Bz-c_0/(10z^2)}{\sqrt{c_0+z^2}}.
```

若 \(c_0\ge10B\)，此函数在 \(0<z\le1\) 上递减，因而必要条件为

```math
(B+1/10)^2(A^2/B^2+2)<(A+1)^2.
```

对 \(B=1,A\ge9\)，这要求 \(21A^2-200A+142<0\)，但该多项式在
\(A=9\) 等于 43，且其后严格递增，矛盾。对 \(B=2,A\ge15\)，
这要求 \(41A^2-800A+3128<0\)，但在 \(A=15\) 等于 353，且其后
严格递增，也矛盾。两段所用的 \(c_0\ge10B\) 均已满足。
因此 \(B=1\) 时 \(1\le A\le8\)，\(B=2\) 时 \(A\le14\)；
后者由既约性只允许奇数 \(A\le13\)。

#### 排除 \(B=2,A=1,3\)

若 \(A=1\)，(A2-prefix-strict) 给出
\(\mathcal R<(1+10xz)/(2+x)<20/21<1\)，与 \(w>1\) 矛盾。

若 \(A=3\)，(A2-numerator-cap) 要求
\((2+1/(10z))\mathcal R<4\)。另一方面

```math
\mathcal R^2>13/4+z^2>(7/4+z/5)^2,
```

因为两个平方之差为 \((384z^2-280z+75)/400\)，首项正、判别式负。
此外 \((16z^2-20z+7)/(40z)>0\)，所以

```math
\left(2+\frac1{10z}\right)\mathcal R
>\frac72+\frac1{50}+\frac{2z}{5}+\frac7{40z}
>\frac72+\frac1{50}+\frac12=\frac{201}{50}>4,
```

矛盾。至此得到全部 A2 的无条件第一块分类：

```math
\boxed{(b_1,a_1)\in
\{(1,1),(1,2),\ldots,(1,8)\}
\ \cup\ \{(2,5),(2,7),(2,9),(2,11),(2,13)\}.}
\tag{A2-first-block}
```

#### 第三比值与尾分母窗

令 \(y=10xz\in(0,1)\)。由 (A2-prefix-strict)，
\(w^2<F=(A+y)^2/(B+x)^2-A^2/B^2-y^2/(100x^2)\)。完整配方为

```math
F=-\frac{x(2B+x)}{B^2(B+x)^2}
\left(A-\frac{B^2y}{x(2B+x)}\right)^2
+y^2 f_B(x),\qquad
f_B(x)=\frac1{x(2B+x)}-\frac1{100x^2}.
```

因此 \(f_B(x)>0\)，且 \(w^2<F\le y^2 f_B(x)<f_B(x)\)。对
\(B=1,2\)，

```math
f_B'(x)=-\frac{-4B^2+96Bx+99x^2}{50x^3(2B+x)^2}<0
\qquad(x\ge1/10).
```

分子在此区间递增，并在 \(x=1/10\) 为正。于是

```math
\boxed{
b_1=1:\quad 1<r_3<\sqrt{79/21}<2,\quad b_3>10^{m_3}/2;
}
```

```math
\boxed{
b_1=2:\quad 1<r_3<\sqrt{59/41}<6/5,\quad b_3>5\cdot10^{m_3}/6.
}
```

#### 保留第一分子的更窄实数窗

上述配方对所有第一分子统一取界。若保留 \(A\)，还能直接使用
\(0<y<1\)。对允许的 13 个第一块，\(100(A+1)>(10B+1)^2\)。
若 \(1/(B+x)^2-1/(100x^2)\ge0\)，则 \(\partial F/\partial y>0\)；
若此系数为负，在 \(y\le1\) 上其最小导数仍满足

```math
\frac{\partial F}{\partial y}\ge
\frac{2(A+1)}{(B+x)^2}-\frac1{50x^2}>0,
```

最后一步使用 \((B+x)/x\le10B+1\)。因而

```math
\boxed{w^2<F(A,x,1)=\frac{(A+1)^2}{(B+x)^2}-\frac{A^2}{B^2}-\frac1{100x^2}.}
```

关于 \(x>0\) 的导数只有一个零点
\(x_*=B/\{[100(A+1)^2]^{1/3}-1\}\)，左侧为正、右侧为负。
故全正轴上的最大值是

```math
\frac{\bigl((A+1)^{2/3}-100^{-1/3}\bigr)^3-A^2}{B^2}.
```

若 \(100(A+1)^2>(10B+1)^3\)，则 \(x_*<1/10\)，在合法区间
\(x\ge1/10\) 上函数严格递减。此条件覆盖 \(B=1,A\ge3\) 和
\(B=2,A\ge9\)。特别地，四个奇尾第一分子给出

```math
\boxed{
A=2:\quad w^2<5/2;\qquad
A=4:\quad w^2<443/121;\qquad
A=6:\quad w^2<423/121;\qquad
A=8:\quad w^2<235/121.
}
```

\(A=2\) 的有理界来自最大值式：
\(9^{1/3}<2081/1000\)、\(100^{-1/3}>215/1000\)，因此两者差小于
\(933/500\)，且 \((933/500)^3<13/2\)。其余三项直接代入
\(x=1/10\)。同样有

```math
\boxed{
(B,A)=(1,1):\ w^2<8/5;\qquad
(B,A)=(2,5):\ w^2<9/8;\qquad
(B,A)=(2,7):\ w^2<4/3.
}
```

具体地，\(4^{1/3}<1588/1000\)，两根差小于 \(1373/1000\)，其立方
小于 \(13/5\)；\(36^{1/3}<3302/1000\)，两根差小于 \(3087/1000\)，
其立方小于 \(59/2\)；\(64^{1/3}=4\)，两根差小于 \(757/200\)，
其立方小于 \(163/3\)。分别代入上面的最大值式即得三项有理界。
这些是严格必要界，固定尾标签也可据此作全指数排除。

若固定标签使 \(x(T)=x_0+\rho/T\)、\(x_0,\rho>0\)，则对
\(B=1,A\ge3\) 可用
\(L=\max(1/10,x_0)\) 得 \(w^2<F(A,L,1)\)。对 \(A=2\)，若
\(x_0\ge3/25\)，同样可用 \(w^2<F(2,x_0,1)\)，因为
\((28/3)^3<900\) 使导数在 \(x\ge3/25\) 上为负；其它标签保留
上面的 \(5/2\) 界。\(A=1,B=1\) 在 \(x_0\ge1/5\) 上也可直接使用
\(F(1,x_0,1)\)，因为 \(6^3<400\)；其它标签保留 \(8/5\) 界。
不满足这些必要界的标签在任意 \(m_2\) 下均无解，
不是仅在某个最大指数前无解。

尾分母窗使用 \(a_3\ge10^{m_3}\)。本节没有排除分母 1，也没有把
分母 2 的全部状态送入 deep-even chart。来源：从原等式重新推导；
历史 first-block 摘要只供比对，不是本证明的前提。

<a id="a2-g02"></a>
### A2-G02　奇尾分母的绝对尾长界与有限系列恢复

**状态：已严格完成。** 全部 A2 且 \(b_3\) 为奇数；本项给有限系列标签，不提供 \(m_2\) 上界。

依赖：[A2-G01](#a2-g01)、[C02](#c02)、[C04](#c04)、[C05](#c05)

核对：`a2-first-block` 核对模四、平方和赋值及原式恢复恒等式。

#### 奇尾强迫偶分子与至多六位尾

由 C05，奇数 \(b_3\) 强迫三个分母全奇。由 A2-G01，\(b_1=1\)，
\(1\le A=a_1\le8\)。C02 的 \(q\) 亦为奇数，记
\(y_1=qA,y_2=qa_2/b_2,y_3=qa_3/b_3\)。原 word 模二给
\(H\equiv y_3\pmod2\)，故

```math
y_1^2+y_2^2=H^2-y_3^2\equiv0\pmod4.
```

两个平方只有同时为偶数才能和为零模四。因此 \(A,a_2\) 都为偶数，
\(A\in\{2,4,6,8\}\)。令 \(v=v_2(A)\in\{1,2,3\}\)，
\(t=v_2(a_2)\ge1\)。两个偶平方的赋值为

```math
v_2(y_1^2+y_2^2)=
\begin{cases}2\min(v,t),&v\ne t,\\2v+1,&v=t,
\end{cases}
\qquad\le2v+1.
```

令 \(T=10^{m_2},U=10^{m_3},Q=T+b_2\)。原式还精确给出

```math
\beta(H-y_3)=U\{q(AT+10a_2)-Qy_3\}.
```

右侧括号是整数，\(\beta\) 为奇数，所以 \(v_2(H-y_3)\ge m_3\)。
且 \(H+y_3\) 为偶数，从而

```math
m_3+1\le v_2((H-y_3)(H+y_3))\le2v+1,
\qquad\boxed{m_3\le2v_2(A)\le6.}
```

具体为 \(A=2,6\) 时 \(m_3\le2\)，\(A=4\) 时 \(m_3\le4\)，
\(A=8\) 时 \(m_3\le6\)。这覆盖任意 \(m_2\)，无需先固定前缀。

#### 所有尾块与分母线性系列只有有限个标签

现在 \(U\le10^6\)，\(U/2<b_3<U\)，且
\(U\le a_3<2b_3\)、\(\gcd(a_3,b_3)=1\)。故 \((A,m_3,b_3,a_3)\)
取值确实有限。令 \(c=\gcd(b_2,b_3)\)。C04 给
\(b_2\mid\operatorname{lcm}(b_3,TU+b_3)\)，所以逐素数有
\(b_2/c\mid TU+b_3\)。定义正整数

```math
k=\frac{c(TU+b_3)}{b_2},\qquad
\boxed{b_2=\frac{c(UT+b_3)}{k}}.
```

\(c\mid b_3\)，而 \(b_2/T=x\in[1/10,1)\)、\(T\ge100\)、\(b_3<U\)
给出严格、有效的标签界

```math
\boxed{cU<k<\frac{101}{10}cU.}
```

因此 \((A,m_3,b_3,a_3,c,k)\) 是一个可穷尽的有限集合；剩余无界
参数是 \(T=10^{m_2},m_2\ge2\)，不是任意移动的两块分母。

还须保留一个原始奇偶约束：\(c,b_2,b_3\) 都为奇数，\(UT\) 为偶数，
所以 \(kb_2=c(UT+b_3)\) 强迫 **\(k\) 为奇数**。因此
\(\Lambda=k+cU\) 为奇数，而 \(10cU\) 为偶数。

#### 原 numerator 的完整恢复方程

对固定标签记 \(B(T)=c(UT+b_3)/k\)、\(\Lambda=k+cU\)。由分母恒等式

```math
\beta=(T+B(T))U+b_3=\frac{B(T)\Lambda}{c}
```

和 \(c\alpha=AkB(T)+10cUa_2+c(a_3-Ab_3)\)，原等式等价于

```math
\boxed{
\Lambda^2\{(A^2+a_3^2/b_3^2)B(T)^2+a_2^2\}
=[AkB(T)+10cUa_2+c(a_3-Ab_3)]^2.
}
\tag{A2-odd-tail-recovery}
```

这里保留全部原块：\(B(T)\) 必须为奇整数，满足
\(T/10\le B(T)<T\)、\(\gcd(B(T),b_3)=c\)；\(a_2\) 必须为偶整数，
满足 \(T/100\le a_2<T/10\)、\(\gcd(a_2,B(T))=1\)。尾标签仍须满足
上述位数、既约性和 \(m_3\le2v_2(A)\)。在这些条件下，两边平方
等式的正根恰给原 \(\alpha/\beta\)，所以恢复是原候选的等价描述，
没有另换 coefficient plane。

清除固定分母后，这是系数为 \(T\) 的整数多项式、关于 \(a_2\)
次数恰为二的方程。二次项 \(\Lambda^2-100c^2U^2\) 是奇数，故非零。
每个标签和每个 \(m_2\) 至多两个 \(a_2\) 根，不存在自由 numerator 线。

本节给绝对尾长界和完整的有限系列归约，**没有给 \(m_2\) 绝对界**。
下面 A2-G03 将证明这些系列的非有效有限性；有限枚举指数仍不能
代替全部有限例外的排除。来源：由本稿公共命题及 A2-G01 新推导。

<a id="a2-g03"></a>
### A2-G03　整个奇尾 A2 的非有效有限性

**状态：已严格完成。** 所有 A2 且 \(b_3\) 为奇数的原候选总数有限；不宣称为空，不给有效的 \(m_2\) cutoff。

依赖：[A2-G02](#a2-g02)；外部输入是 Schlickewei 的 p-adic Subspace Theorem。

核对：`a2-first-block` 核对奇数标签与非零判别式；外部定理及以下无界论证不由脚本证明。

#### 明示的外部定理与一个固定二次式引理

使用下列形式的 p-adic Subspace Theorem：有限素点集包含无穷点，
每个点上的三条线性型具有代数系数且线性无关。对任意固定正数
\(C,\delta\)，使各点线性型绝对值乘积不超过
\(C\|\mathbf x\|^{-\delta}\) 的本原整数三维向量，落在有限多个
真有理线性子空间中。准确版本见
[Evertse, Theorem 1.1, pp. 1–2](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf)；
原作者的研究文献见
[Schlickewei, 1992, §1](https://www.numdam.org/item/CM_1992__82_3_245_0.pdf)。
这里只调用定性有限子空间结论，不使用任何高度或指数有效界。

**本节引理。** 固定 \(P(X)=p_2X^2+p_1X+p_0\in\mathbf Z[X]\)，
\(p_2>0\)，且 \(p_1^2-4p_2p_0\ne0\)。那么使
\(P(10^m)=Y^2\)、\(Y\in\mathbf Z\)、\(m\ge0\) 的指数只有有限个。

证明：取非负 \(Y\)，记 \(T=10^m\)、\(\alpha=\sqrt{p_2}>0\)、
\(\gamma=p_1/(2\alpha)\)。固定系数的展开给

```math
Y=\alpha T+\gamma+O(T^{-1}).
```

对本原向量 \(\mathbf x=(Y,T,1)\)，无穷点采用三条线性型
\(X_1-\alpha X_2-\gamma X_3,X_2,X_3\)；在 2 和 5 两点都采用
\(X_1,X_2,X_3\)。各组三型均线性无关，且

```math
\begin{aligned}
\prod_{v\in\{\infty,2,5\}}\prod_{i=1}^3|L_{i,v}(\mathbf x)|_v
&=|Y-\alpha T-\gamma|\,T\,|YT|_2|YT|_5\\
&\le |Y-\alpha T-\gamma|\,T\,|T|_2|T|_5
=O(T^{-1}),
\end{aligned}
```

其中 \(|T|_2|T|_5=T^{-1}\)，\(\|\mathbf x\|\asymp T\)。故充分大
的解满足外部定理（例如取 \(\delta=1/2\)），落在有限个真有理子空间。
每个子空间有非零有理关系 \(uY+vT+w=0\)。若 \(u=0\)，至多固定
一个 \(T\)，或无解；若 \(u\ne0\)，代入 \(Y^2=P(T)\) 后得到

```math
P(T)-\left(-\frac{vT+w}{u}\right)^2=0.
```

这不是零多项式，否则 \(P\) 是有理线性式的平方，判别式为零，
违反假设。因此每个子空间至多容纳两个 \(T\)。有限子空间的并集
只有有限个指数，初始有限指数也不改变结论。引理得证。

#### 固定奇尾系列没有无限退化支

使用 A2-G02 的固定标签，暂记 \(B=B(T)\)、\(w=a_3/b_3\)，以及

```math
u=10cU,\quad \Lambda=k+cU,\quad h=\Lambda^2-u^2,\quad
C=A^2+w^2>0,\quad j=c(a_3-Ab_3).
```

由于 \(A\ge2\)、\(w<2\)，有 \(j<0\)。又由 A2-G02，\(\Lambda\) 奇、
\(u\) 偶，因此 **\(h\) 为奇数，特别地非零**。原恢复方程写成

```math
F(N,B)=\Lambda^2(CB^2+N^2)-(AkB+uN+j)^2=0,\qquad N=a_2.
```

其 \(N\)-判别式及内部二次式为

```math
\operatorname{disc}_N F=4\Lambda^2 P(B),\qquad
P(B)=(AkB+j)^2-hCB^2,
```

```math
\operatorname{disc}_B P=4hCj^2.
```

有理根 \(N\) 强迫 \(P(B)\) 是有理平方；
又 \(B(T)=c(UT+b_3)/k\) 的斜率非零，若 \(P\) 为二次式，则
\(P(B(T))\) 的判别式也非零。取固定正整数 \(D\) 清除全部系数
分母，使 \(D^2P(B(T))\in\mathbf Z[T]\)。在原候选上它是整数的
有理平方，因而是整数平方。若其首项正，本节引理给有限个 \(m_2\)；
若首项负，实数正性已只允许有限个 \(T\)。

若 \(P\) 的二次项恰为零，则
\(P(B)=j(2AkB+j)<0\)，因为原分母系列给
\(AkB+j=c(AUT+a_3)>0\)，又 \(AkB>0\)。此情形没有原候选。
由于 \(h=0\) 已被奇偶性排除，上述分析穷尽全部原候选标签。

A2-G02 的标签集合实际有限，每个标签的指数及对应 numerator
根又有限，故**整个奇尾 A2 原候选集合有限**。这是有限个系列的并集，
没有把任意多个固定前缀的有限性外推到全体前缀。

外部定理未提供所需子空间的可计算位置；本证明因此不给所有系列
统一的有效指数上界，也未穷尽有限例外。奇尾空性、偶尾 A2 和主命题
仍为待证。来源：本稿新应用；外部输入仅为上面明示的 Subspace Theorem。

<a id="a2-g04"></a>
### A2-G04　偶尾的二进主导分类与两个球面 gap 分支

**状态：已严格完成。** 全部 A2 且 \(b_3\) 为偶数；给出无界参数上的必要分类，不宣称任一剩余类为空。

依赖：[A2-G01](#a2-g01)、[C02](#c02)、[C05](#c05)

核对：`a2-binary-chambers` 核对原 word-gap 恒等式、有限赋值模式和两个 sphere gap 分支；有限样例不是原候选穷尽。

#### 唯一最大深度只能来自第二或第三分母

记 \(A=a_1,B=b_1\in\{1,2\}\)、\(T=10^{m_2},U=10^{m_3}\)，其中
\(m_2\ge2,m_3\ge1\)。定义

```math
e=v_2(B)\in\{0,1\},\quad f=v_2(b_2),\quad g=v_2(b_3)\ge1,
\quad Q=BT+b_2,\quad d=v_2(Q),\quad E=\max(e,f,g).
```

第三块既约且分母为偶，故 \(a_3\) 为奇数，原 \(\alpha\) 也为奇数。
C05 给 \(E\) 唯一取得且 \(H\) 奇。由 \(q\alpha=H\beta\) 得
\(v_2(\beta)=E\)。第一分母不能独占最大值：若 \(e=0\)，则
\(g\ge1>e\)；若 \(e=1\)，则 \(g\ge e\)。因此恰有下面两类。

#### 第二分母主导：原 deep-even 二进形态的严格来源

设 \(f>\max(e,g)\)。在 \(\beta=QU+b_3\) 中，若两项赋值不同，
其和的赋值为较小者，不可能等于 \(f>g\)。故必须
\(d+m_3=g\)，并在相同赋值层抵消至 \(f\)。

若 \(f<e+m_2\)，则 \(d=f\)；若 \(f=e+m_2\)，则
\(d\ge f+1\)。两种情形都给 \(d+m_3>f>g\)，矛盾。因而

```math
\boxed{f>e+m_2,\qquad d=e+m_2,\qquad g=e+m_2+m_3.}
```

这里 \(g\ge3\)，故 \(f\ge4\)，且第一分母深度 \(e<f-1\)。若
\(g=f-1\)，另外两分母恰有一块深度为 \(E-1\)，违反 C05 的模八条件。
所以实际上

```math
\boxed{f\ge g+2=e+m_2+m_3+2.}
```

写 \(b_2=2^f u,b_3=2^g v\)，其中 \(u,v\) 奇，则

```math
\begin{array}{c|c|c}
B&b_3&b_2\\\hline
1&2^{m_2+m_3}v&2^{m_2+m_3+t}u,\ t\ge2\\
2&2^{m_2+m_3+1}v&2^{m_2+m_3+t}u,\ t\ge3.
\end{array}
```

第二行正是 A2-01 使用的二进形态。此处只证明这一形态的适用来源：
它覆盖 \(B=2\) 且第二分母二进主导的全部原候选，不自动补出后续
纯五次幂尾商或其它 source 归一化条件；\(B=1\) 的第一行也未被排除。

#### 第三分母主导：保留减 gap 与加 gap 两个分支

现在设 \(g>\max(e,f)\)。由 \(v_2(QU+b_3)=g\)，必须

```math
\boxed{g<d+m_3.}
```

因为 \(d+m_3<g\) 时和的赋值更小，等于 \(g\) 时两个奇单位相加
反而至少升一层。C02 给 \(y_3=qa_3/b_3\) 奇，另外两个坐标为偶。
令

```math
C_0=AT+10a_2,\qquad
p_1=g-e+v_2(A),\qquad p_2=g-f+v_2(a_2),
```

```math
\sigma=v_2(y_1^2+y_2^2)=
\begin{cases}2\min(p_1,p_2),&p_1\ne p_2,\\2p_1+1,&p_1=p_2.
\end{cases}
```

最后一式在相等赋值时使用两个奇平方之和恰为 \(2\pmod8\)。
原 word 精确给

```math
\boxed{\beta(H-y_3)=U(qC_0-Qy_3).}
```

先设 \(d\le g\)。因 \(C_0\) 偶，\(v_2(qC_0)\ge g+1>d\)，而
\(v_2(Qy_3)=d\)，括号赋值恰为 \(d\)。于是

```math
\boxed{\delta:=v_2(H-y_3)=m_3+d-g\ge1.}
```

由球面 \((H-y_3)(H+y_3)=y_1^2+y_2^2\)，分成两个互斥且穷尽的情形：

```math
\boxed{
\begin{array}{ll}
\delta\ge2:&v_2(H+y_3)=1,\quad \sigma=m_3+d-g+1;\\
\delta=1:&v_2(H+y_3)=\sigma-1\ge2.
\end{array}}
```

证明这一步只需 \(H,y_3\) 均奇：若其差被 4 整除，其和等于
\(2y_3\pmod4\)，恰有一层；若其差恰有一层，则其和被 4 整除。
第二行不能丢弃，也不能把两个 gap 的深度同时按减 gap 计算。

#### 第三分母主导的 source 抵消层

余下 \(d\ge g+1\)。若 \(f\ne e+m_2\)，则
\(d=\min(f,e+m_2)\le f<g\)，矛盾。因此

```math
\boxed{f=e+m_2.}
```

此时 \(f\ge2\)，既约性使 \(a_2\) 为奇数。
\(AT\) 至少含 \(2^2\)，而 \(10a_2\) 恰含一层，所以
\(v_2(C_0)=1\)。同时
\(p_2=g-f<p_1=g-e+v_2(A)\)，故 \(\sigma=2(g-f)\)。

若 \(d>g+1\)，括号 \(qC_0-Qy_3\) 的赋值恰为 \(g+1\)，得到
\(v_2(H-y_3)=m_3+1\ge2\)。加 gap 恰一层，因而

```math
\boxed{d>g+1\ \Longrightarrow\ m_3+2=2(g-f).}
```

若 \(d=g+1\)，两个括号项赋值相同，抵消后至少为 \(g+2\)，所以
\(v_2(H-y_3)\ge m_3+2\)，加 gap 仍恰一层，得到

```math
\boxed{d=g+1\ \Longrightarrow\ m_3+3\le2(g-f).}
```

上述分类保留原 \(Q,\alpha,\beta,q,H,y_i\)，覆盖全部偶尾 A2。
它没有排除尾分母主导，也没有提供任何全局位数上界。来源：本稿由
公共球面和原拼接式新推导；有限赋值回归只审计这些等式的算术实现。

<a id="a2-g05"></a>
### A2-G05　五进尾主导与二进前缀主导的完整尾商归约

**状态：已严格完成。** 全部 A2 的五进主导位置；第二分母二进主导类的纯五次幂尾商、Hensel 锁和互素 source 分解。均为必要归约，未证明为空。

依赖：[A2-G01](#a2-g01)、[A2-G04](#a2-g04)、[C02](#c02)、[C03](#c03)、[C04](#c04)

核对：`a2-binary-chambers` 核对模五平方类、有限分母投影和尾商恢复恒等式。无界覆盖由以下证明给出。

#### 正五进最大深度必须由尾分母唯一取得

仍记 \(B=b_1\in\{1,2\}\)、\(T=10^{m_2},U=10^{m_3}\)，其中
\(m_2\ge2,m_3\ge1\)。设 \(F=v_5(b_2),J=v_5(b_3)\)，第一分母为
五进单位。本节证明

```math
\boxed{(F,J)=(0,0)\quad\text{或}\quad J>F.}
```

若 \(F>0,J=0\)，第二分母唯一最深，球面使 \(H\) 为五进单位，
但 \(\beta=QU+b_3\) 为五进单位；\(q\alpha=H\beta\) 左端至少有
\(F\) 层，右端零层，矛盾。

若 \(F=J>0\)，令 \(s=m_2+m_3\)。位数给 \(b_2b_3<10^s\)，故
不能 \(F\ge s\)，否则 \(b_2b_3\ge25^s>10^s\)。于是 \(F<s\)。
当 \(F<m_2\) 时 \(v_5(Q)=F\)；等于 \(m_2\) 时
\(v_5(Q)\ge m_2+1\)；大于 \(m_2\) 时 \(v_5(Q)=m_2\)。三个情形
都给 \(v_5(QU)>F\)，所以 \(v_5(\beta)=F\)。原 \(a_3\) 及
\(\alpha\) 为五进单位，word 因而给 \(H\) 为单位。
然而 \(y_1=0\pmod5\)，\(y_2,y_3\) 均为单位；两个非零平方
之和模五属于 \(\{0,2,3\}\)，不能等于单位平方 \(\{1,4\}\)。矛盾。

最后设 \(F>J>0\)。此时第二分母唯一最深，\(H,\alpha\) 都为单位，
故 \(v_5(\beta)=F\)。与 A2-G04 的二进前缀主导推导同样比较两项：
要从 \(QU+b_3\) 得到比 \(J\) 更高的赋值，必须
\(v_5(Q)+m_3=J\)。若 \(F\le m_2\)，则 \(v_5(Q)\ge F\)，
不可能；因此 \(F>m_2\)，\(v_5(Q)=m_2\)，于是

```math
J=m_2+m_3=s,\qquad F\ge s+1.
```

但这强迫 \(b_2b_3\ge5^{2s+1}>10^s\)，再次违反位数窗。
以上穷尽所有 \(F\ge J\) 且 \(F>0\) 的情形，结论得证。
特别地，奇尾分母不一定为五进单位；此结论没有把奇尾与五进单位混同。

#### 第二分母二进主导自动给纯五次幂尾商

现在处于 A2-G04 的第二分母二进主导类。记
\(e=v_2(B)\)，并写

```math
b_2=2^{m_2+m_3+t}u,\qquad
b_3=2^{e+m_2+m_3}v,\qquad u,v\text{ 奇},\qquad t-e\ge2.
```

令 \(J=v_5(b_3)\)。若 \(J\ge m_3\)，则
\(b_3\ge2^{e+m_2+m_3}5^{m_3}=2^{e+m_2}U>U\)，矛盾。
因此定义

```math
\lambda=m_3-J\in\{1,\ldots,m_3\},\qquad
c=\frac{b_3}{2^{e+m_2+m_3}5^J},\qquad \gcd(c,10)=1.
```

在 C03 的分母尾规范化 \(\delta_3=\gcd(U,b_3),L=U/\delta_3,
\tau=b_3/\delta_3\) 中，已直接得到

```math
\boxed{\delta_3=2^{m_3}5^J,\qquad L=5^\lambda,
\qquad \tau=2^{e+m_2}c.}
```

这是原分母 gcd 的计算，没有对尾分子作未经证明的除法。
第三分母的真实 significand 为

```math
\frac{b_3}{U}=\frac{2^{e+m_2}c}{5^\lambda}.
```

令 \(\gamma_1=1/2,\gamma_2=5/6\)。A2-G01 的更强尾窗给

```math
\boxed{\frac{\gamma_B5^\lambda}{2^{e+m_2}}<c<
\frac{5^\lambda}{2^{e+m_2}}.}
```

#### Hensel 锁与互素 source 分配仍来自原 word

记 \(r=t-e\ge2\)，则

```math
Q=2^{e+m_2}Q_0,\qquad
Q_0=5^{m_2}+2^{m_3+r}u\quad\text{为奇数},
```

```math
\beta=2^{e+m_2+m_3}5^J
\{5^{m_2+\lambda}+c+2^{m_3+r}5^\lambda u\}.
```

A2-G04 已给 \(v_2(\beta)=m_2+m_3+t\)，故括号的赋值恰为 \(r\)。
最后一项的赋值为 \(m_3+r>r\)，所以

```math
\boxed{r=v_2(5^{m_2+\lambda}+c).}
```

由 \(r\ge2\) 与 \(5^h=1\pmod4\) 得 \(c=3\pmod4\)，特别地
\(c\ge3\)。上方尾窗立即给

```math
\boxed{5^\lambda>3\,2^{e+m_2}.}
```

对任意 \(p\mid c\)，有 \(p\ne2,5\)。C04 的第三分母整除给
\(v_p(c)\le\max(v_p(u),v_p(Q_0))\)。又

```math
\gcd(u,Q_0)=\gcd(u,5^{m_2}),
```

故没有一个 \(p\mid c\) 同时出现在 \(u,Q_0\)。完整素数幂因此唯一分配为

```math
\boxed{c=c_Qc_u,\qquad c_Q\mid Q_0,\quad c_u\mid u,
\quad\gcd(c_Q,c_u)=1.}
```

这里 \(c_u=\gcd(c,u)\)，\(c_Q=c/c_u\)；不是独立选取两个新标签。
当 \(B=2\) 时 \(e=1,r=t-1\)，所得 \(L,\tau,Q_0,c_Q,c_u\) 和
Hensel 锁与 A2-01 的初始 chart 一致，适用范围已明确是第二分母
二进主导类。\(B=1\) 则有 \(e=0,r=t\) 的相应原式归约。
尾分母二进主导仍须单独处理；本节不使全部 A2 落入该 chart，也不
使 source、norm 与 sphere 的同源约束变成独立预算。来源：本稿新推导。

<a id="a2-g06"></a>
### A2-G06　奇尾分子的最低二进层与精确尾长分类

**状态：已严格完成。** 全部奇尾 A2；第三分子严格独占三个分子的最低二进层，并给出 \(m_3\ge2\) 的精确必要分类。

依赖：[A2-G02](#a2-g02)、[C02](#c02)

核对：`a2-first-block` 核对两平方赋值公式及分类表的有限参数回归；无界覆盖来自本节证明。

在 A2-G02 的三个奇分母情形，记
\(v=v_2(A)\in\{1,2,3\}\)、\(t=v_2(a_2)\ge1\)、\(j=v_2(a_3)\)。
本节首先证明

```math
\boxed{0\le j<\min(v,t).}
```

令 \(d=\min(v,t,j)\)。原拼接式 \(\alpha=U(AT+10a_2)+a_3\) 中，
前两项分别至少含 \(2^{d+3}\)、\(2^{d+2}\)，因为 \(m_2\ge2,m_3\ge1\)。
\(q,\beta\) 均奇，所以 \(v_2(H)=v_2(\alpha)\)。若 \(j>d\)，
则 \(H/2^d\) 为偶；而 \(y_1/2^d,y_2/2^d\) 至少一项奇、
\(y_3/2^d\) 偶。平方和模四为 1 或 2，不可能等于该偶数的平方。
故 \(j=d\)。此时 \(\alpha/2^j\) 奇，\(H/2^j\) 奇；若 \(v=j\)
或 \(t=j\)，球面除以 \(2^{2j}\) 后至少两项奇，其平方和为 2 或 3
模四，再次矛盾。于是最低层只由第三分子取得。

现在只为计算赋值而记
\(A'=A/2^j,a_2'=a_2/2^j,a_3'=a_3/2^j,H'=H/2^j,y_i'=y_i/2^j\)。
保留原 \(m_2,m_3,T,U,Q,\alpha,\beta\) 的系数，不声称这是位数
不变的新候选。\(A',a_2'\) 偶，\(a_3',H',y_3'\) 奇，原 gap 恒等式给

```math
\beta(H'-y_3')=U\{q(A'T+10a_2')-Qy_3'\}.
```

右侧括号是偶数减奇数，恰为奇数。因此
\(v_2(H'-y_3')=m_3\)。若 \(m_3\ge2\)，另一个 gap 恰有一层，得到

```math
\boxed{
m_3+1=\begin{cases}
2\min(v-j,t-j),&v\ne t,\\
2(v-j)+1,&v=t.
\end{cases}}
```

这里的两个平方赋值公式与 A2-G02 相同，但先除去了原分子的共同
二进层，因此得到等式而非粗上界。代入 \(v=1,2,3\) 给全部允许形态：

| \(A\) | \(j=v_2(a_3)\) | \(t=v_2(a_2)\) | \(m_3\) |
|---|---:|---:|---:|
| 2、6 | 0 | 1 | 2 |
| 4 | 0 | 2 | 4 |
| 4 | 0 | \(t\ge3\) | 3 |
| 4 | 1 | 2 | 2 |
| 8 | 0 | 2 | 3 |
| 8 | 0 | 3 | 6 |
| 8 | 0 | \(t\ge4\) | 5 |
| 8 | 1 | 3 | 4 |
| 8 | 1 | \(t\ge4\) | 3 |
| 8 | 2 | 3 | 2 |

若 \(m_3=1\)，则 \(v_2(H'+y_3')\ge2\)，只有不等式
\(2\min(v-j,t-j)+[v=t]\ge3\)，不能套用上面的尾长等式。
该完整一位尾子层由 A2-F01 排除。上表是原候选的必要形态；其中
\(m_3=2\) 各行又已由 A2-F02 排除，实际剩余只保留更长尾。
该表不是解的存在性声明。来源：本稿新推导。

<a id="a2-g07"></a>
### A2-G07　奇尾系列中恢复分子与分母的既约素数排除

**状态：已严格完成。** A2-G02 的任意固定奇尾标签；给出原恢复二次式和逐块既约性共同产生的必要素数过滤。

依赖：[A2-G02](#a2-g02)

核对：`a2-first-block` 核对恢复式在被整除分母上的退化恒等式。

沿用 \(A,b=b_3,a=a_3,c,k,U=10^{m_3}\)，令
\(\Lambda=k+cU,u=10cU,h=\Lambda^2-u^2\)，以及
\(B=b_2=c(UT+b)/k\)、\(N=a_2\)、\(j=c(a-Ab)\)。原恢复二次式为

```math
\Lambda^2\{(A^2+a^2/b^2)B^2+N^2\}-(AkB+uN+j)^2=0.
```

设素数 \(p\nmid10kb\)，且 \(p\mid a-Ab\)、\(p\nmid h\)。因为
\(c\mid b\)，所有分母在模 \(p\) 上可逆。如果 \(p\mid UT+b\)，
则 \(p\mid B\) 且 \(j=0\pmod p\)。恢复式模 \(p\) 恰成为
\(hN^2=0\)，于是 \(p\mid N\)，违反 \(\gcd(N,B)=1\)。所以

```math
\boxed{p\nmid10kb,\quad p\mid a-Ab,\quad p\nmid h
\quad\Longrightarrow\quad UT+b\not\equiv0\pmod p.}
```

这是原分子根的既约恢复约束。仅检查恢复式的判别式为平方，会容许
\(N\) 与 \(B\) 同时被 \(p\) 整除的根，因此会漏掉此项过滤；两者仍
来自同一原系统，不能计为两个独立高度预算。

例如两位奇尾标签 \((A,b,a,c,k)=(4,89,134,89,85987)\) 有
\(a-Ab=-222\)，\(h\ne0\pmod3\)，\(3\nmid10kb\)。但所有
\(T=10^{m_2},m_2\ge2\) 都使 \(100T+89=0\pmod3\)。该标签因此
在全部指数上被原既约性排除；它不是原候选的允许见证。来源：本稿新推导。

<a id="a2-g08"></a>
### A2-G08　固定偶尾长的有效前缀界与 ordinary 联合赋值排除

**状态：已严格完成。** 全部偶尾 A2 的两个有界二进类，以及明示的
ordinary 二进/五进联合子类。其余 ordinary 类仍允许无界 \(m_2\)。

依赖：[A2-G04](#a2-g04)、[A2-G05](#a2-g05)、[C02](#c02)

核对：`a2-short-prefix-even` 核对整数界和有界类证书；无界结论由下列
赋值证明给出，有限样例不承担无界覆盖。

记 \(m=m_3,U=10^m,e=v_2(B),f=v_2(b_2),g=v_2(b_3)\)，定义精确整数

```math
G(m)=\max\{g\ge0:2^g\le10^m-1\},\qquad
H(m)=\max\{h\ge0:3\cdot2^h<5^m\}.
```

若第二分母二进主导，A2-G05 给某个 \(1\le\lambda\le m\) 满足
\(3\cdot2^{e+m_2}<5^\lambda\le5^m\)，故

```math
\boxed{f>g\quad\Longrightarrow\quad m_2\le H(m)-e.}
```

若尾分母二进主导且 \(f\ge e+m_2\)，则 \(f\ge2\)，第一分母的
深度 \(e\le1<f\)。若 \(g=f+1\)，唯一一个非主导分母在 \(g-1\)
层，违反 C05 的模八必要条件。因此 \(g\ge f+2\)，位数给
\(g\le G(m)\)，从而

```math
\boxed{g>\max(e,f),\ f\ge e+m_2
\quad\Longrightarrow\quad m_2\le G(m)-e-2.}
```

固定 \(m\) 后这两个类都有可计算的绝对前缀界；A2-G01 再给固定的
13 个第一块、严格尾窗，故可直接穷尽原方程。没有对余下类外推此界。

#### ordinary 类的二进减 gap 与加 gap

上述两类之外，必须 \(g>\max(e,f)\) 且 \(f<e+m_2\)，所以
\(d=v_2(B10^{m_2}+b_2)=f\)。记 \(D=g-f>0\)。A2-G04 的减 gap
深度恰为 \(\delta=m-D\ge1\)，保留其两个 sphere 分支。

若 \(f>e\)，逐块既约使 \(a_2\) 奇；两个非尾坐标的赋值满足
\(p_2=D<p_1\)，故 \(\sigma=2D\)。于是

```math
\boxed{
\begin{array}{ll}
\delta\ge2:&m=3D-1;\\
\delta=1:&m=D+1,\quad D\ge2.
\end{array}}
```

第二行的 \(D\ge2\) 来自 \(v_2(H+y_3)=2D-1\ge2\)。若
\(f=e=1\)，则 \(B=2,A,a_2\) 均奇，\(p_1=p_2=D\)，得到

```math
\boxed{
\delta\ge2\Rightarrow m=3D,\qquad
\delta=1\Rightarrow m=D+1.}
```

\(f=e=0\) 的情形继续保留 A2-G04 中含分子赋值的 \(\sigma\) 公式，
不能套用上面两式。特别是加 gap 深分支没有被删除。

#### 正五进 ordinary 层及一个无界联合空类

这一段实际上对全部 A2 有效。设 \(F=v_5(b_2)>0\)、
\(F<m_2\)。A2-G05 给 \(J=v_5(b_3)>F\)，故尾坐标唯一为五进
单位，其余两坐标被 5 整除，\(H\) 为单位。第三块既约使
\(a_3,\alpha\) 都为单位，原 word 因此强迫 \(v_5(\beta)=J\)。
因 \(v_5(Q)=F\)，比较 \(QU+b_3\) 给 \(J\le m+F\)。
这里等深的两个五进单位相加可以仍为单位；不能照搬二进的必然进位。

若 \(J<m+F\)，把 word 除以 \(5^J\) 后模 5，得
\(H\equiv y_3\pmod5\)，因此 \(H+y_3\) 为单位。球面中
\(v_5(y_2)=J-F<v_5(y_1)\)，没有同层抵消，所以

```math
v_5(H-y_3)=v_5(y_1^2+y_2^2)=2(J-F).
```

原减 gap 的括号 \(q(AT+10a_2)-Qy_3\) 的赋值恰为 \(F\)：
\(a_2\) 为五进单位，第一项至少 \(J+1\) 层，第二项恰 \(F\) 层。
因而 \(v_5(H-y_3)=m+F-J\)，联立得到

```math
\boxed{0<F<m_2,\ J<m+F\quad\Longrightarrow\quad m=3(J-F).}
```

若 \(J=m+F\)，同一 gap 给 \(v_5(H-y_3)=0\)。球面仍给
\(v_5(y_1^2+y_2^2)=2(J-F)=2m\)，故完整保留另一分支：

```math
\boxed{J=m+F\quad\Longrightarrow\quad
v_5(H+y_3)=2m,\quad H\equiv-y_3\pmod5,\quad5^F<2^m.}
```

最后的不等式直接来自 \(5^{m+F}\le b_3<10^m\)。这不是合法原解的
构造，也没有把这一五进加 gap 分支排除。

与二进 ordinary 减 gap 联立，立即排除以下完整无界子类：

```math
\boxed{f>e,\ f<e+m_2,\ 0<F<m_2,\ J<m+F,\ \delta\ge2
\quad\Longrightarrow\quad\text{无原候选}.}
```

因为它同时要求 \(m\equiv2\pmod3\) 和 \(m\equiv0\pmod3\)。
两条结论均来自同一原 word/sphere，只用于联合必要条件，不记为
独立预算。若 \(F\ge m_2\)，也只有必要界
\(m_2\le F<J\le\max\{j:5^j\le U-1\}\)，没有自动排除。

#### 第二分母五进单位时的尾深度界

若 \(F=0,J>0\)，则 \(Q\) 为五进单位，尾坐标唯一为单位。
与上段相同，\(H,\alpha\) 为单位，原 word 给 \(v_5(\beta)=J\)，
所以 \(J\le m\)。原减 gap 的括号赋值为零，故
\(v_5(H-y_3)=m-J\)。若 \(J<m\)，\(H\equiv y_3\pmod5\)，加
 gap 为单位，而另两个 sphere 坐标均至少含 \(J\) 层，得到

```math
\boxed{F=0,\ 0<J<m\quad\Longrightarrow\quad m\ge3J.}
```

更准确地，此时
\(v_5(A^2b_2^2+B^2a_2^2)=m-3J\ge0\)。若 \(J=m\)，减 gap
为单位，必须保留深的加 gap，不能沿用 \(m\ge3J\)。所以三位尾在
\(F=0\) 时仅允许 \(J\in\{0,1,3\}\)；\(J=2,4\) 全部排除。
结合 F04 后，三位尾的全部原候选都必须满足这个条件。

来源：本稿由 G04/G05 新推导。固定尾长有效界不成为全部尾长的
全局界；ordinary 的加 gap 深分支、五进单位类和低二进第二分母
继续留在 RESEARCH.md。

<a id="a2-g09"></a>
### A2-G09　任意固定尾长的整个 A2 非有效有限性

**状态：已严格完成。** 对每个固定正整数 \(m_3\)，整个 A2 的原候选
总数有限；同样，对每个固定 \(M\)，\(m_3\le M\) 的原候选总数有限。
不证明这些集合为空，不提供可计算的统一 \(m_2\) 上界，也不把所有
尾长的无限并集说成有限。

依赖：[A2-G01](#a2-g01)、[A2-G02](#a2-g02)、[A2-G03](#a2-g03)、[C04](#c04)

核对：`a2-first-block` 核对任意首分母的原恢复式、判别式、零二次项
和线性式奇偶拆分。外部子空间定理继续只按 G03 的明示版本使用。

固定 \(m=m_3,U=10^m\)。G01 给全部 13 个第一块 \((A,B)\)，以及
\(U/2<b=b_3<U\)、\(U\le a=a_3<2b\)（\(B=2\) 时用更强的窗口）。
所以 \((A,B,b,a)\) 有限。\(B=1\) 时显然 \(B\mid b\)；\(B=2\)
时 G02 排除了奇尾，故同样 \(B\mid b\)。C04 于是给
\(b_2\mid\operatorname{lcm}(b,B10^{m_2}U+b)\)。令
\(c=\gcd(b_2,b)\)，逐素数得 \(b_2/c\mid B10^{m_2}U+b\)。因此

```math
T=10^{m_2},\quad k=\frac{c(BUT+b)}{b_2}\in\mathbf Z_{>0},\quad
M(T)=b_2=\frac{c(BUT+b)}k,\quad
BcU<k<(10B+1/10)cU.
```

\(c\mid b\)，标签 \((A,B,b,a,c,k)\) 的集合确实有限。仍保留全部
原整数性、位数、既约性和 \(c\) 的实际含义，没有放宽后再声称等价。

记

```math
\Lambda=k+cU,\quad u=10cU,\quad h=\Lambda^2-u^2,\quad
C=A^2+B^2a^2/b^2>0,\quad j=c(Ba-Ab).
```

与 F02 相同的原式恒等变形给

```math
\Lambda^2\{CM(T)^2+B^2N^2\}
=[AkM(T)+uBN+j]^2,\qquad N=a_2.
```

这里没有使用奇尾的 \(h\) 奇性。改为直接证明两个退化不可能：

1. 若 \(h=0\)，因正数 \(\Lambda=u\)，有 \(k=9cU\)，而分母
   系列强迫 \(9Ub_2=BTU+b\)，故 \(U\mid b\)，违反 \(0<b<U\)。
   此标签没有原候选。
2. \(j\ne0\)。若 \(B=1,A=1\)，有 \(a/b>1=A/B\)，所以 \(j>0\)；
   若 \(B=1,A\ge2\)，有 \(a/b<2\le A/B\)，所以 \(j<0\)；
   若 \(B=2\)，有 \(a/b<6/5<A/B\)，仍 \(j<0\)。

因此关于 \(N\) 的二次项 \(hB^2\) 非零，每个固定指数至多两个根。
原有理根强迫

```math
P(M)=(AkM+j)^2-hCM^2
```

为有理平方；它关于 \(M\) 的判别式是 \(4hCj^2\ne0\)。
若其二次项非零，代入非零斜率的 \(M(T)\) 并以固定整数平方清除
系数分母，得到判别式非零的整数二次式 \(\widetilde P(T)\)。
在原候选上它是整数有理平方，因而是整数平方。首项负时只有有限
个正 \(T\)；首项正时由 G03 的固定二次式引理，指数有限。

剩下二次项为零的情形，
\(P(M)=j(2AkM+j)\)，且

```math
AkM+j=cB(AUT+a)>0,\qquad AkM>0.
```

若 \(j<0\)，\(P(M)<0\)，无原候选。若 \(j>0\)，代入 \(M(T)\)
得到正斜率的线性式，且常数项

```math
P(M(0))=j(2Acb+j)=c^2[(Ba)^2-(Ab)^2]>0.
```

取固定整数平方清分母，得到 \(\ell T+d\)，\(\ell,d\) 为正整数。
对指数拆成 \(m_2=2n+\varepsilon\)、\(\varepsilon\in\{0,1\}\)，其
整数平方条件变为

```math
\ell\,10^\varepsilon(10^n)^2+d=Y^2.
```

这也是 G03 的二次式引理：首项正且判别式
\(-4\ell10^\varepsilon d\ne0\)。两个奇偶系列各只有有限个指数。
因此偶尾特有的零二次项也没有无限自由支。

全部有限标签、每标签有限指数、每指数至多两个 \(N\) 的并集有限，
结论得证。对固定 \(M\)，再取 \(m_3=1,\ldots,M\) 的有限并集。
若整个 A2 存在无限多个原候选，则尾长必无界；由 G03 奇尾总数
有限，其无限部分只能出现在越来越长的偶尾。

来源：G03 非有效有限性方法向任意固定尾长的新扩展；新增审计是
\(h=0\) 的原整数性排除、\(j\ne0\) 和正线性退化的奇偶拆分。
没有产生任何有效绝对 cutoff，也没有排除有限例外。

<a id="a2-g10"></a>
### A2-G10　固定前两块的有效尾长界

**状态：已严格完成。** 全部 A2 的每个固定原前两块有可计算的
\(m_3\) 上界；故每个固定 \(m_2\) 的原候选集合可有效穷尽。
不把所有 \(m_2\) 的无限并集说成有限，不宣称整个 A2 为空。

依赖：[A2-G01](#a2-g01)、[A2-G02](#a2-g02)、[A2-G04](#a2-g04)、[A2-G05](#a2-g05)、[C02](#c02)、[C04](#c04)

核对：`a2-fixed-prefix`、`a2-first-block`；整数阈值、原尾恢复判别式
及统一相对界的符号/常数审计。无界覆盖由下列
完整 gap 分裂给出，不依赖枚举猜测的 cutoff。

固定 \((A,B,N,M)=(a_1,b_1,a_2,b_2)\)、\(T=10^{m_2}\)，定义

```math
Q=BT+M,\quad C_0=AT+10N,\quad
D_0=(BM)^2,\quad S=(AM)^2+(BN)^2,
```

```math
e=v_2(B),\quad f=v_2(M),\quad F=v_5(M),\quad
 d_p=v_p(Q),\ c_p=v_p(C_0),\ \kappa_p=v_p(S)-v_p(D_0)
\quad(p=2,5).
```

\(c_2,c_5\ge1\)。令 \(L\) 为 \(\operatorname{lcm}(B,M,Q)\)
去掉全部 2、5 因子的正整数部分。C04 给任何原尾

```math
b_3=2^g5^JC,\qquad C\mid L,\qquad U=10^m,\quad m=m_3,
\qquad \frac12<\frac{b_3}{U}<1.
```

若对应素数由尾分母唯一主导，则
\(v_p(y_1^2+y_2^2)=2v_p(b_3)+\kappa_p\)，因为
\(q^2(r_1^2+r_2^2)=q^2S/D_0\)。所有 \(\kappa_p,d_p,c_p,L\)
均由固定前两块精确计算。

#### 二进的三个有效分裂

奇尾先由 G02 给 \(m\le6\)。偶尾第二分母主导时，G04 给
\(g=d_2+m\)、\(f\ge g+2\)，所以 \(m\le f-d_2-2\)。

现在尾分母二进主导。若 \(g+c_2\le d_2\)，原减 gap 括号至少
\(g+c_2\) 层，因而
\(v_2(H-y_3)\ge m+c_2\ge2\)，加 gap 恰一层。球面给
\(2g+\kappa_2\ge m+c_2+1\)，且 \(g\le d_2-c_2\)，所以

```math
m\le2d_2+\kappa_2-3c_2-1.
```

若 \(g+c_2>d_2\)，括号恰 \(d_2\) 层，减 gap 的深度为
\(\delta_2=m+d_2-g\ge1\)。两个互斥分支为

```math
\begin{array}{ll}
\delta_2\ge2:&3g=m+d_2+1-\kappa_2;\\
\delta_2=1:&g=m+d_2-1.
\end{array}
```

第一式用球面深度 \(2g+\kappa_2=\delta_2+1\)；第二式保留深加 gap。

#### 五进的三个有效分裂

G05 给 \((F,J)=(0,0)\) 或 \(J>F\)。\(J=0\) 后面直接用尾位数窗。
设 \(J>F\)，此时 \(H,y_3,\alpha\) 为五进单位，word 强迫
\(v_5(\beta)=J\)，所以 \(J\le m+d_5\)。

若 \(J+c_5\le d_5\)，减 gap 深度至少 \(m+c_5\ge2\)，加 gap 为
单位，球面给 \(2J+\kappa_5\ge m+c_5\)，故

```math
m\le2d_5+\kappa_5-3c_5.
```

若 \(J+c_5>d_5\)，减 gap 深度为 \(\delta_5=m+d_5-J\ge0\)，得

```math
\begin{array}{ll}
\delta_5\ge1:&3J=m+d_5-\kappa_5;\\
\delta_5=0:&J=m+d_5.
\end{array}
```

第一行中 \(H\equiv y_3\pmod5\)，加 gap 为单位；第二行中减 gap
为单位，保留深加 gap，没有照搬二进单位相加必进位的结论。

#### 两个深加 gap 不能同时发生

若二进、五进都进入上述第二行，则

```math
\frac{b_3}{U}=C\,2^{d_2-1}5^{d_5}.
```

若 \(d_2\ge1\)，此值至少 1；若 \(d_2=0,d_5\ge1\)，至少 \(5/2\)；
若 \(d_2=d_5=0\)，\(C=1\) 时恰为 \(1/2\)，而奇数 \(C\ge3\)
时至少 \(3/2\)。全部违反严格尾窗。这排除完整的联合加 gap 子类，
不是将两套来自同一 word/sphere 的条件计为独立预算。

二进减 gap 分支的 \(g=(m+d_2+1-\kappa_2)/3\) 与
\(J\le m+d_5,C\le L\) 联立，尾窗给

```math
2^{2m}<L^3\,2^{d_2+4-\kappa_2}5^{3d_5}.
```

二进加 gap 分支若 \(J>0\)，五进临界类已有界，余下只能进入五进
减 gap，于是

```math
5^{2m}<L^3\,2^{3d_2}5^{d_5-\kappa_5}.
```

若 \(J=0\)，直接有 \(5^m<L2^{d_2}\)。右侧都是固定、可计算的
正有理数；负指数也按精确有理数处理。

定义 \(E(b,t,X)=\max\{m\ge0:b^{tm}<X\}\)，空集取 \(-1\)。完整
有效上界是下列七个整数的最大值：

```math
\boxed{\max\left\{
6,\ f-d_2-2,\ 2d_2+\kappa_2-3c_2-1,\ 2d_5+\kappa_5-3c_5,
E(2,2,L^3 2^{d_2+4-\kappa_2}5^{3d_5}),
E(5,2,L^3 2^{3d_2}5^{d_5-\kappa_5}),
E(5,1,L2^{d_2})\right\}.}
```

以上覆盖奇尾、第二分母二进主导、两个素数临界类及全部剩余 gap
组合。固定 \(m_2\) 后，G01 的 13 个第一块及原 \(N,M\) 位数窗给
有限个前缀，取上述界的有限最大值即可。再用
\(C\mid L,g\le\max(e,f,d_2+m),J\le\max(F,d_5+m)\) 的 C04 完整
支持界穷尽尾分母，原尾分子从原二次式恢复，因此是有效有限性。

#### 对所有前缀统一的相对尾长界

上述有效界还给全部 A2 的必要条件

```math
\boxed{m_3\le10m_2.}
```

这里第一块仍是 G01 的 13 种；令 \(n=m_2\ge2,T=10^n\)。G01 的
配方给 \(F(A,B,x,y)\le y^2 f_B(x)\)，其中
\(f_B(x)=1/[x(2B+x)]-1/(100x^2)\)。原尾比值大于 1，且
\(x=M/T\ge1/10,0<y=10N/T<1\)，所以 \(f_B(x)>1\)。
\(f_B'(x)\) 的分子为 \(4B^2-96Bx-99x^2\)，在
\(B\in\{1,2\},x\ge1/10\) 时严格为负。又有

```math
f_1(2/5)=47/48<1,\qquad
f_2(37/200)=1145200/1145853<1.
```

于是 \(B=1\) 时 \(M<2T/5\)，\(B=2\) 时 \(M<37T/200\)。
因此分别有 \(MQ<14T^2/25\)、\(MQ<16169T^2/40000\)，都小于
\(T^2\)。写 \(M_0=M/(2^f5^F),Q_0=Q/(2^{d_2}5^{d_5})\)，则
\(L\le M_0Q_0\)。因为 \(S\) 是正整数，
\(\kappa_2\ge-2(e+f),\kappa_5\ge-2F\)，两个减 gap 阈值满足

```math
\begin{aligned}
L^3 2^{d_2+4-\kappa_2}5^{3d_5}
&\le\frac{16\,2^{2e}M^3Q^3}{2^{f+2d_2}5^{3F}}
\le16B^2(MQ)^3<K_B T^6,\\
L^3 2^{3d_2}5^{d_5-\kappa_5}
&\le\frac{M^3Q^3}{2^{3f}5^{F+2d_5}}
\le(MQ)^3<T^6,
\end{aligned}
```

其中

```math
K_1=16(14/25)^3=43904/15625<4,\qquad
K_2=64(16169/40000)^3=4227167754809/10^{12}<2^{42}/10^{12}.
```

二进临界类 \(g\le d_2-c_2\) 时，\(J\le m+d_5\) 与尾窗直接给
\(2^m<2L2^{d_2-c_2}5^{d_5}\le MQ<T^2\)。五进临界类
\(J\le d_5-c_5\) 时，尾二进主导的 G04 给
\(g\le m+d_2-1\)，因此
\(5^m<L2^{d_2}5^{d_5-c_5}\le MQ<T^2\)。二进加 gap 且
\(J=0\) 时同样有 \(5^m<L2^{d_2}\le MQ<T^2\)。奇尾仍为
\(m\le6\)；第二分母二进主导有 \(m\le f-d_2-2\)，故
\(2^m<T\)。这些类及两个减 gap 已穷尽全部允许组合。

若 \(m\ge10n+1\)，令 \(\rho=2^{20}/10^6>1\)，则
\(2^{2m}\ge4\rho^nT^6\)。当 \(B=1\)，这大于 \(4T^6>K_1T^6\)；
当 \(B=2,n\ge2\)，这至少为 \(4\rho^2T^6=2^{42}T^6/10^{12}
>K_2T^6\)。五的对应幂更大，故两个减 gap 均矛盾。另有
\(2^m\ge2\cdot2^{10n}>2T^3>T^2\)，也排除两个临界类及
五进单位尾类；奇尾与第二分母主导的界同样不可能。于是
\(m\le10n\)。这是一条覆盖无界 \(n\) 的相对界，未给 \(n\) 的
绝对上界，不能据此称候选总集合有限。

#### 后两分母五进单位时的更强界

若 \(F=J=0\)，则 \(M,b_3,B,\beta,q\) 都是五进单位，其中
\(q=\operatorname{lcm}(B,M,b_3)\)、\(H=q\alpha/\beta\)、
\(y_3=qa_3/b_3\) 均为五进整数。原 word 给

```math
H-y_3=\frac{qU(b_3C_0-Qa_3)}{\beta b_3},
```

所以 \(v_5(H-y_3)\ge m\)；\(H+y_3\) 为五进整数，球面恒等式给

```math
\boxed{m\le v_5(S)=v_5((AM)^2+(BN)^2).}
```

这一步不要求 \(H,y_3\) 是单位，不要求两个五进单位相加进位，
也不将同源 word/sphere 条件重复计为预算。原 word 是前缀比值
\(C_0/Q\) 与 \(a_3/b_3\) 的正权平均，而半径 \(R>a_3/b_3\)，
故 \(C_0/Q>R>A/B\)。交叉相乘得

```math
\boxed{AM<10BN.}
```

于是 \(S<101B^2N^2<101B^2T^2/100\le101T^2/25<5T^2\)。若
\(m\ge3n+1\)，则 \(5^m\ge5\cdot125^n>5\cdot100^n=5T^2>S\)，
与 \(5^m\mid S\) 矛盾。因此进一步有

```math
\boxed{F=J=0\quad\Longrightarrow\quad m_3\le3m_2.}
```

特别是 F04/F07 后的三位尾余核必须 \(125\mid S\)。此同源必要
条件可以过滤原前缀，但尚未排除所有满足该同余的前缀。

来源：固定原前缀的两个 gap 与完整非十进制分母支持的新联合归约。
没有转换原 word cut、没有候选下降；\(m_2\) 的无限并集仍待处理。

<a id="a2-g11"></a>
### A2-G11　非十进制共同支持与原标签锁

**状态：已严格完成。** 全部 A2。后两分母共有的非 2、5 素幂
必须同深，且素数为 \(1\pmod4\)；尾分母其余非十进制部分整除
原标签的 \(k+cU\)。这些只是原候选的必要条件。

依赖：[A2-G01](#a2-g01)、[A2-G02](#a2-g02)、[C02](#c02)、[C04](#c04)

核对：`a2-nondecimal-support`；原标签恒等式、1,314 个有界完整
denominator-complement 投影及小素数平方类。无界覆盖由以下证明
给出，投影计数不是 Exact Lift 穷尽枚举。

仍用 \(B\in\{1,2\},T=10^{m_2},U=10^{m_3},M=b_2,b=b_3\)。
设 \(p\ne2,5\) 同时整除 \(M,b\)，记两深度 \(f_p,g_p>0\)。
\(BTU+b\) 与 \((BT+M)U\) 都是 \(p\)-单位。C04 的第二、第三
分母完整整除分别给 \(f_p\le g_p\) 与 \(g_p\le f_p\)，故

```math
\boxed{v_p(M)=v_p(b).}
```

此时 \(\beta=(BT+M)U+b\) 也是 \(p\)-单位。对
\(q=\operatorname{lcm}(B,M,b)\)，\(v_p(q)=f_p=g_p\)；
\(H=q\alpha/\beta\) 与 \(y_1=qA/B\) 都含 \(p\)，而原逐块既约
保证 \(y_2=qN/M,y_3=qa/b\) 都为单位。整数球面模 \(p\) 给
\(y_2^2+y_3^2=0\)，故 \(-1\) 为模 \(p\) 的平方。于是

```math
\boxed{p\mid\gcd(M,b),\ p\ne2,5\quad\Longrightarrow\quad p\equiv1\pmod4.}
```

令 \(c=\gcd(M,b)\)，\(c_*\) 为 \(c\) 去掉全部 2、5 的部分，
\(b_*\) 为 \(b\) 的相应部分。上面的同深结论意味着每个非十进制
素幂或完整进入 \(c_*\)，或完全不进入；所以

```math
\boxed{c_*\mid b_*,\quad\gcd(c_*,b_*/c_*)=1,\quad
\text{每个 }p\mid c_*\text{ 均为 }1\pmod4.}
```

G02 在 \(B=2\) 时排除了奇尾，因此全部原候选都有 \(B\mid b\)。
C04 给 \(M\mid\operatorname{lcm}(b,BTU+b)\)，从而
\(M/c\mid BTU+b\)，定义原整数标签
\(k=c(BTU+b)/M\)。设 \(b_0=b_*/c_*\)。对每个 \(p\mid b_0\)，
\(v_p(M)=0\)，C04 的第三整除给 \(p^{v_p(b_0)}\mid BT+M\)。
又有原恒等式

```math
k(BT+M)=B(k+cU)T+cb.
```

\(B,T\) 是模 \(b_0\) 的单位，\(b_0\mid b\)，故得到完整素幂锁

```math
\boxed{b_0\mid k+cU.}
```

它与球面判别式、原整数性仍属于同一原 word/sphere 系统，没有
产生独立高度预算。尤其奇尾且 \(5\nmid b\) 时，\(c\) 是 \(b\)
的 unitary divisor，且共同素数全为 \(1\pmod4\)；即使满足这些
限制，仍必须恢复原第二分子和既约性，不能把标签允许点视为原解。

原半径整性还把该支持锁接回原分子拼接。因为 \(B\mid b\)，
\(q=Mb/c\)，而原分母标签给 \(\beta=(k+cU)M/c\)。C02 的整数
半径因此为

```math
\boxed{H=\frac{b\alpha}{k+cU}\in\mathbf Z,\qquad k+cU\mid b\alpha.}
```

特别在奇尾且 \(5\nmid b\) 时，G02 给 \(B=1\) 及两个后分母奇；
C04 的 \(M\mid\operatorname{lcm}(b,UT+b)\) 又给 \(5\nmid M\)，
因为右端两个数都是五进单位。因此 \(c,b/c,k\) 都为十进制单位，
G11 同深结论及 \(UT+b\) 在共同素数上为单位给
\(\gcd(k,c)=1\)，故 \(\gcd(k+cU,c)=1\)。写
\(b=c b_0,k+cU=b_0\ell\)，则

```math
\boxed{\ell\mid\alpha=ATU+10UN+a,\qquad
N\equiv-(ATU+a)(10U)^{-1}\pmod\ell.}
```

这里 \(\ell\) 也是十进制单位；模逆存在。给出的只是原第二分子的
一个剩余类，未宣称该类有合法位数与既约恢复，也未把半径整性作为
独立预算。完全共同支持 \(c=b\) 时仍有 \(\ell=k+bU\mid\alpha\)，
所以该剩余类不能从证书中删去。

奇尾五进单位时，上述 word 因子还是**精确**的拼接 gcd。令
\(V=M/c,b_0=b/c\)。同深结论给 \(\gcd(V,b)=1\)，且
\(\gcd(c,b_0)=1\)，故 \(q=cVb_0\)。对任何 \(p\mid q\)：

- 若 \(p\mid c\)，原 \(\beta\) 为单位，故
  \(v_p(H)=v_p(q)+v_p(\alpha)\ge v_p(q)=v_p(c)\)。
- 若 \(p\mid Vb_0\)，该素数只出现在一个后分母中，那个 sphere
  坐标为单位，另外两个含 \(p\)，所以 \(H^2\) 为单位，\(H\) 也为单位。

这里所有素数均不为 2、5，首分母为 1；两类穷尽 \(q\) 的支持，
并在第一类保留了完整素幂。因此

```math
\gcd(H,q)=c,\qquad
\operatorname{den}_{\rm reduced}(R)=q/c=Vb_0.
```

又 \(\beta=(k+cU)V=b_0\ell V\)。原 \(R=\alpha/\beta\) 的既约
分母恰为 \(Vb_0\)，故

```math
\boxed{\gcd(\alpha,\beta)=\ell=\frac{k+cU}{b/c},\qquad
\gcd(\alpha/\ell,Vb_0)=1.}
```

这给原 word 的完整约分因子，没有变更三个块的 cut 或逐块既约性。
它仍是原候选必须满足的条件，不提供 \(m_2\) 的绝对界，也不排除
\(c=b\) 的完全共同支持类。

固定原前两块时，G10 的 \(M_0,Q_0\) 还满足
\(\gcd(M_0,Q_0)=1\)：任何共有素数不为 2、5，却会整除
\(Q-M=BT\)，矛盾。因此非十进制支持不是两个重叠预算，而有唯一分解

```math
L=M_0Q_0,\qquad C=C_M C_Q,\quad
C_M\mid M_0,\ C_Q\mid Q_0,\quad\gcd(C_M,C_Q)=1.
```

具体取 \(C_M=\gcd(C,M_0)\)，\(C_Q=C/C_M\)。同深结论强迫
\(C_M\) 的每个素幂都是 \(M_0\) 中的完整素幂，所以
\(\gcd(C_M,M_0/C_M)=1\)，且其素数全为 \(1\pmod4\)。
\(C_Q\) 仍是 \(Q_0\) 的任意因子，没有排除其更深或不完全幂次。
这是完整必要支持分解；满足该分解的分母仍不一定有原分子恢复。

来源：原 denominator complement 与整数球面的联合支持推导。

<a id="a2-g12"></a>
### A2-G12　第二分母整除第一十进制权重的整个子域为空

**状态：已严格完成。** 全部 A2 且 \(b_2\mid b_1 10^{m_2}\)；前缀、
尾长和分子都不设搜索上限。特别包含任意 \(b_2=10^t\)、\(t\ge1\)。
这是 A2 的一个完整无界子域，不是 A2 整分支。

依赖：[A2-G01](#a2-g01)、[A2-G04](#a2-g04)、[A2-G05](#a2-g05)、
[C02](#c02)、[C04](#c04)、[C05](#c05)、[A2-F05](#a2-f05)、[A2-F06](#a2-f06)

核对：`a2-decimal-divisor`。整数恒等式、六种分母形状、常数的有理
界、一个模 \(2^{27}\) 的完整循环类及七个小指数；外部显式定理
和下面的无界推导承担全范围覆盖。

#### 六种分母形状与共同整数半径

记 \(B=b_1,A=a_1,N=a_2,M=b_2,n=m_2,T=10^n\)，并记
\(m=m_3,U=10^m,a=a_3,b=b_3\)。F05/F06 已关闭 \(n=2,3,4\)，
所以只需证明 \(n\ge5\)。设

```math
K=BT/M\in\mathbf Z_{>0},\qquad x=M/T=B/K.
```

G01 给 \(B\in\{1,2\}\)、\(x\ge1/10\)，且递减函数
\(f_B(x)=1/[x(2B+x)]-1/(100x^2)>1\)。因为
\(f_1(2/5)=47/48<1\)、\(f_2(1/5)=79/84<1\)，分别有
\(K>5/2\) 或 \(K>10\)，并总有 \(K\le10B\)。又 \(K\mid BT\)，
所以 \(K\) 只含 2、5。全部可能形状如下；\(f=v_2(M),F=v_5(M)\)，
\(r_p=v_p(K+1)\)，\(W=(K+1)/(2^{r_2}5^{r_5})\)。

| \(B\) | \(K\) | \(M/T\) | \(f\) | \(F\) | \(r_2\) | \(r_5\) | \(W\) |
|---|---|---|---|---|---|---|---|
| 1 | 4 | 1/4 | \(n-2\) | \(n\) | 0 | 1 | 1 |
| 1 | 5 | 1/5 | \(n\) | \(n-1\) | 1 | 0 | 3 |
| 1 | 8 | 1/8 | \(n-3\) | \(n\) | 0 | 0 | 9 |
| 1 | 10 | 1/10 | \(n-1\) | \(n-1\) | 0 | 0 | 11 |
| 2 | 16 | 1/8 | \(n-3\) | \(n\) | 0 | 0 | 17 |
| 2 | 20 | 1/10 | \(n-1\) | \(n-1\) | 0 | 0 | 21 |

各行均有 \(f>v_2(B),F>0\)。奇尾被 C05 排除；若第二分母二进
主导，G04 要求 \(f\ge v_2(B)+n+m+2\)，与表中 \(f\le n\)
矛盾。因此尾分母二进主导。写

```math
g=v_2(b)=f+D,\quad J=v_5(b)=F+E.
```

C05 的模八条件给 \(D\ge2\)，G05 给 \(E\ge1\)。由于 \(M\)
只含 2、5，故 \(M\mid b\)，并有

```math
q=\operatorname{lcm}(B,M,b)=b,\qquad m\ge n\ge5,\qquad
b=M2^D5^E C,\quad C\mid W.
```

最后一个完整素幂整除来自 C04：尾的非十进制部分整除
\(Q=BT+M=M(K+1)\) 的非十进制部分 \(W\)。原半径整数是
\(H=b\mathcal R\)，第三球面坐标就是 \(a\)。G01 的严格前缀窗
给 \(\mathcal R<9\)、\(a/b<2\)，从而

```math
0<H+a<11b<11\cdot10^m. \tag{A2-divisor-radius}
```

#### 五进加 gap 排除与两个剩余减 gap

令 \(C_0=AT+10N\)。逐块既约给 \(v_2(C_0)=v_5(C_0)=1\)，
因为 \(n\ge5\) 且 \(N\) 为十进制单位。原 word 精确给

```math
\beta(H-a)=U(bC_0-Qa),\qquad \beta=QU+b.
```

\(H,a\) 都是二进、五进单位：前者来自两个素数上尾坐标唯一最浅
的整数球面，后者来自 \(\gcd(a,b)=1\)。原 word 随即给
\(v_2(\beta)=g,v_5(\beta)=J\)。由于
\(g+1>f+r_2\)、\(J+1>F+r_5\)，括号中的第二项在这两个素数上
严格较浅，故

```math
v_2(H-a)=m+r_2-D,\qquad v_5(H-a)=m+r_5-E.
```

又 \(y_1=Ab/B,y_2=Nb/M\)，在两个素数上 \(y_2\) 都严格较浅，
所以

```math
v_2(y_1^2+y_2^2)=2D,\qquad v_5(y_1^2+y_2^2)=2E.
```

若 \(v_5(H-a)=0\)，则 \(E=m+r_5\ge m\)，球面给
\(5^{2m}\mid H+a\)。这与 (A2-divisor-radius) 矛盾，因为
\((5/2)^m\ge(5/2)^5>11\)。因此五进必在减 gap 上，且

```math
m=3E-r_5. \tag{A2-divisor-five}
```

二进则完整保留两种情况：

```math
\begin{array}{ll}
v_2(H-a)\ge2:&m=3D-r_2-1,\quad v_2(H+a)=1;\\
v_2(H-a)=1:&D=m+r_2-1,\quad v_2(H+a)=2D-1.
\end{array}
```

第一种与 (A2-divisor-five) 联立要求
\(3(D-E)=r_2+1-r_5\)。表中仅 \((B,K)=(1,4)\) 允许此式，且
\(D=E,C=1\)。但此时 \(b=M10^E\)、\(m=3E-1\)，严格尾窗
\(1/2<b/U<1\) 要求 \(2<10^{n+1-2E}<4\)，整数十进制幂不可能
满足。因此全部六行只能进入二进加 gap。

#### 原 word 的加 gap 整数锁

设 \(d=W/C\)。把二进加 gap 的 \(D=m+r_2-1\) 和五进关系代入，
得到没有改变原 cut 的恒等式

```math
\frac\beta b=1+2d25^E=:L,\qquad
L(H+a)=C_0U+2(1+d25^E)a. \tag{A2-divisor-plus-word}
```

\(L\) 为奇数，第一项的二进赋值恰为 \(m+1\)，而左侧的赋值是
\(2D-1=2m+2r_2-3>m+1\)，这里使用 \(m\ge5\)。两项必须先同深
再抵消，故必要条件为

```math
\boxed{v_2(1+d25^E)=m.} \tag{A2-divisor-exponent-lock}
```

六行的 \(d\) 全部属于 \(\{1,3,7,9,11,17,21\}\)。由于
\(25^E\equiv1\pmod8\)，\(d=1,9,17,21\) 时左侧为 1，
\(d=3,11\) 时为 2，均与 \(m\ge5\) 矛盾。唯一剩余是
\((B,K,C,d)=(2,20,3,7)\)，此时 \(r_5=0,m=3E\)，故 \(E\ge2\)
且必须 \(v_2(7\cdot25^E+1)=3E\)。下面的有效引理排除此式。

#### 显式指数引理与完整余类证书

对每个整数 \(E\ge2\)，都有

```math
\boxed{v_2(7\cdot25^E+1)<3E.} \tag{A2-divisor-exponent-lemma}
```

这里使用明确的外部输入：Y. Bugeaud，
[Linear Forms in two m-adic Logarithms and Applications to Diophantine Problems](https://doi.org/10.1023/A:1015825809661)，
Compositio Mathematica 132 (2002), 137–158，Theorem 2（p. 140）。
取原定理中的 \(m=8,g=1,\mu=4\)，
\((x_1/y_1,x_2/y_2)=(25,-1/7)\)、\((b_1,b_2)=(E,1)\)，
\((A_1,A_2)=(25,8)\)。两者都是二进单位，其减 1 的赋值均为 3；
因此 H1、H2 均成立，且 \(\gcd(8,E,1)=1\)。\(\Lambda=25^E+1/7\ne0\)。
采用不要求乘法独立性的常数 \(c_1(4)=66.8\)，定理给出

```math
v_8(\Lambda)\le
\frac{66.8\log25\log8}{(\log8)^4}
\left(\max\left\{\log\left(\frac E{\log8}+\frac1{\log25}\right)
+\log\log8+0.64,\ 4\log8\right\}\right)^2.
```

全用自然对数。注意 \(v_8(\Lambda)=\lfloor v_2(7\cdot25^E+1)/3\rfloor\)，
不能把两个赋值直接当成相等。利用 \(2<\log8<3\)、
\(1<\log25<4\)、\(\log\log8<2\)，可保守放宽为

```math
v_2(7\cdot25^E+1)
<128\max\{\log(E+1)+3,12\}^2+3.
```

若左侧至少为 \(3E\)，则 \(E<10^6\)：在 \(E=10^6\) 处，
\(9<\log(E+1)<14\)，上界小于 \(128\cdot17^2+3=36995<3\cdot10^6\)；
之后最大值始终取对数项，\((\log(E+1)+3)^2/E\) 与 \(3/E\) 都严格递减。
因此这个上界是已经证明的绝对界，不是自行选择的枚举截止点。

另一方面，由 \(v_2(25^{2^s}-1)=s+3\)，25 在模 \(2^{27}\)
下的阶恰为 \(2^{24}\)。一次精确模幂计算给

```math
7\cdot25^{11278491}+1\equiv0\pmod{2^{27}}.
```

故所有满足该同余的指数恰为
\(E\equiv11278491\pmod{16777216}\)。若 \(E\ge9\) 且
\(v_2(7\cdot25^E+1)\ge3E\)，就必须属于该类；它在
\(0\le E<10^6\) 中没有代表。余下 \(E=2,\ldots,8\) 的赋值依次为
\(3,6,3,4,3,5,3\)，都小于 \(3E\)，引理得证。
模幂由二进快速幂、逐位提升和截断二项式三种整数 reader 核对；
截断取 \(25^r=(1+24)^r\)，第 9 项起均被 \(2^{27}\) 整除。

这排除了最后的原整数锁，完成整个 \(b_2\mid b_1 10^{m_2}\) 子域。
证明未给一般第二分母的绝对界；含非十进制素因子，或二进/五进
深度超过 \(b_1 10^{m_2}\) 对应深度的第二分母，仍须另行处理。

来源：本稿从原 word/sphere 联立的新推导；外部显式定理按上文
参数使用，有限模核对只在有效界和完整周期证明之后承担剩余排除。


<a id="a2-g13"></a>
### A2-G13　第二分母只有一位有效数字的整个子域为空

**状态：已严格完成。** 全部 A2 且 \(b_2=r10^t\)，其中
\(1\le r\le9\)、\(t\ge0\)；前缀分子和尾长均不设上限。

依赖：[A2-G01](#a2-g01)、[A2-G04](#a2-g04)、[A2-G05](#a2-g05)、[A2-G11](#a2-g11)、[A2-G12](#a2-g12)、[C02](#c02)、[C05](#c05)、[A2-F05](#a2-f05)、[A2-F06](#a2-f06)

核对：`a2-decimal-rays`；下面的证明覆盖任意 \(t,m_3\)。

沿用 G12 的 \(A,B,N,M,n,T,a,b,m,U\) 记号。A2 有 \(n\ge2\)，
F05/F06 排除 \(n\le4\)，故 \(n=t+1\ge5\)。G01 的
\(M/T<2/5\)（\(B=1\)）和 \(M/T<1/5\)（\(B=2\)）只允许
\((B,r)=(1,1),(1,2),(1,3),(2,1)\)。除 \((1,3)\) 外均已由 G12
排除。只需考虑

```math
B=1,\quad M=3\cdot10^t,\quad Q=T+M=13\cdot10^t,\quad t\ge4.
```

G04/C05 排除奇尾和第二分母二进主导，G05 给五进尾主导。
写 \(v_2(b)=t+D,v_5(b)=t+E\)，则 \(D\ge2,E\ge1\)。
G11 排除共同素数 3，尾的剩余支持整除 13，故

```math
b=10^t2^D5^E C,\quad C\in\{1,13\},\quad
q=3b,\quad H=q\mathcal R,\quad y_3=3a,\quad m\ge5.
```

令 \(C_0=AT+10N\)。既约性给 \(v_2(C_0)=v_5(C_0)=1\)。
原 word 与整数球面给

```math
\beta(H-3a)=3U(bC_0-Qa),\qquad
v_2(H-3a)=m-D,\quad v_5(H-3a)=m-E,
```

以及 \(v_2(y_1^2+y_2^2)=2D,v_5(y_1^2+y_2^2)=2E\)。若五进
走加 gap，则 \(E=m\)、\(25^m\mid H+3a\)，与
\(0<H+3a<33b<33\cdot10^m\)、\((5/2)^5>33\) 矛盾。
所以 \(m=3E\)。二进减 gap 要求 \(m=3D-1\)，不可能；二进
只能走加 gap，\(D=m-1\)、\(v_2(H+3a)=2m-3\)。

设 \(d=13/C\in\{1,13\}\)。此时

```math
L=\beta/b=1+2d25^E,\qquad
L(H+3a)=3C_0U+6(1+d25^E)a.
```

右侧两项的二进赋值分别为 \(m+1\ge6\) 和 2，因为
\(d\equiv1\pmod4\)、\(a\) 为奇数。左侧为 \(2m-3\ge7\)，
矛盾。至此所有一位有效数字的第二分母均被排除。

来源：G12 的原 word 加 gap 方法，结合 G11 的共同素数限制；
此项不使用新的指数估计或有限长度枚举。


<a id="a2-g14"></a>
### A2-G14　两位有效数字第二分母的唯一必要族

**状态：已严格完成。** 全部 A2 且 \(b_2=r10^t\)、
\(10\le r\le99\)、\(10\nmid r\)、\(t\ge0\)。若原解存在，
必须落在下列唯一一族，其中 \(E\) 是整数且 \(E\ge3\)。
表只给必要参数，不断言其中存在原解。

| \(b_1\) | \(a_1\) | \(b_2\) | \(b_3\) | \((m_2,m_3)\) |
|---|---|---|---|---|
| 1 | 2 | \(24\cdot10^{2E-1}\) | \((4/5)10^{3E}\) | \((2E+1,3E)\) |

因此这一范围内全部 \(b_1=2\)，以及 \(b_1=1,(a_1,r)\ne(2,24)\)
的完整无界子域为空。这一族的原分子恢复仍为待证，不能把分类写成
整个两位有效数字子域为空，更不能写成整个 A2 关闭。

依赖：[A2-G01](#a2-g01)、[A2-G04](#a2-g04)、[A2-G05](#a2-g05)、[A2-G11](#a2-g11)、[A2-G12](#a2-g12)、[C02](#c02)、[C05](#c05)、[A2-F01](#a2-f01)、[A2-F02](#a2-f02)、[A2-F03](#a2-f03)、[A2-F05](#a2-f05)、[A2-F06](#a2-f06)

核对：`a2-decimal-rays`；完整有限首部表、精确有理窗口、16 个固定
系数的有效指数界及完整模周期。\(t,E\) 均由下面的解析推导处理，
不设试算 cutoff。

#### 固定首部与整数 gap

沿用 G12 记号。短前缀由 F05/F06 排除，故 \(n=t+2\ge5,t\ge3\)；
F01/F02 给 \(m\ge3\)。设

```math
u=v_2(r),\quad v=v_5(r),\quad r_0=r/(2^u5^v),\quad Q_* =100B+r,
\quad r_p=v_p(Q_*)-v_p(r),\quad W=Q_*/(2^{v_2(Q_*)}5^{v_5(Q_*)}).
```

G01 只允许 \(B=1,r=11,\ldots,39\) 或
\(B=2,r=11,\ldots,18\)，始终删去 \(10\mid r\)。其中 \(r=19,B=2\)
由 \(f_2(19/100)<1\) 排除。这个 35 行整数表满足
\(-3\le r_2\le5\)、\(r_5\in\{0,1\}\)，且 \(r_5=1\) 只在
\((B,r)=(1,25)\) 出现。\(r_2>2\) 只在 \((1,28)\) 出现，此时
\(r_2=5\)。这些是固定首部的完整表，不枚举任意长的第二分母。

记 \(f=t+u,F=t+v,e=v_2(B)\)。奇尾被 C05 排除；若第二分母二进
主导，则 G04 给 \(m\le u-e-4\le1\)，与 \(m\ge3\) 矛盾。
所以 \(g=v_2(b)=f+D\)，且 C05 给 \(D\ge2\)；G05 给
\(J=v_5(b)=F+E,E\ge1\)。G11 的完整支持分解给

```math
b=10^t2^{u+D}5^{v+E}C_M C_Q,\quad
C_M\mid r_0,\quad \gcd(C_M,r_0/C_M)=1,\quad
p\mid C_M\Longrightarrow p\equiv1\pmod4,\quad C_Q\mid W.
```

令 \(V=r_0/C_M\)。因 \(\gcd(r_0,W)=1\)，有
\(q=Vb,H=q\mathcal R,y_3=Va\)。特别地

```math
b\ge20\cdot10^t,\quad m\ge t+2\ge5,\qquad
0<H+y_3<11Vb<429\cdot10^m. \tag{A2-rays-height}
```

\(N\) 与 10 互素，故 \(C_0=AT+10N\) 的二进、五进赋值都是 1。
\(H,y_3,V\) 都是二进、五进单位。由于 \(E+1>r_5\)，原 word
\(\beta(H-y_3)=VU(bC_0-Qa)\) 给
\(v_5(H-y_3)=m+r_5-E\)，球面余项的五进赋值为 \(2E\)。
若走五进加 gap，就有 \(E=m+r_5\ge m\) 及
\(25^m\mid H+y_3\)。当 \(m\ge7\) 时，这与 (A2-rays-height)
及 \((5/2)^7>429\) 矛盾；当 \(m\le6\) 时，
\(b\ge4\cdot10^t5^m\) 和 \(b<10^m\) 要求
\(2^m>4\cdot10^t\ge4000\)，也不可能。因此

```math
m=3E-r_5. \tag{A2-rays-five}
```

二进临界情形 \(D+1\le r_2\) 只可能在 \((B,r)=(1,28)\)。
此时 \(D\le4,f=n\)，G04 的 \(d_2\ge g+1\) 公式给 \(m\le5\)，
从而被 F03 排除。其余均有 \(D+1>r_2\)，故

```math
v_2(H-y_3)=m+r_2-D,\qquad v_2(y_1^2+y_2^2)=2D.
```

二进减 gap 给 \(m=3D-r_2-1\)；二进加 gap 给
\(D=m+r_2-1\)、\(v_2(H+y_3)=2D-1\)。

#### 双减 gap 的首部分类与单位障碍

双减要求 \(3(D-E)=r_2+1-r_5\)。35 行首部中恰有下面五行满足
右侧被 3 整除；它们都强迫 \(C_M=1\)。设
\(z=(r_2+1-r_5)/3\)，则

```math
\frac bU=\kappa10^{t-2E+r_5},\qquad
\kappa=2^{u+z}5^v C_Q.
```

| \((B,r)\) | \((r_2,r_5)\) | 全部 \(C_Q\) | 全部 \(\kappa\) | \(1/2<b/U<1\) 允许的比值 |
|---|---|---|---|---|
| \((1,12)\) | \((2,0)\) | 1,7 | 8,56 | \(4/5,14/25\) |
| \((1,24)\) | \((-1,0)\) | 1,31 | 8,248 | \(4/5\) |
| \((1,25)\) | \((0,1)\) | 1 | 25 | 无 |
| \((1,28)\) | \((5,0)\) | 1 | 16 | 无 |
| \((2,16)\) | \((-1,0)\) | 1,3,9,27 | 16,48,144,432 | 无 |

每个 \(\kappa\) 除以唯一使其落在 \([1/10,1)\) 的十进制幂即可
核对此表；无需枚举无界指数。最后三个允许比值分别给
\(t=2E-1,2E-2,2E-1\)。再将

```math
\frac1{(b/U)^2}<\frac{(A+1)^2}{(B+r/100)^2}
-\frac{A^2}{B^2}-\frac1{100(r/100)^2}
```

代入 G01 的有限第一块集合，恰得 \(A=2,\ldots,6\)、\(A=4\)、
\(A=2\)。\(E\le1\) 违反 \(t\ge3\)；\(E=2\) 时第二行违反
\(t\ge3\)，第一、三行均有 \(m=6,f\ge n\)，被 F03 排除。
所以这三个中间族统一要求 \(E\ge3\)。

两种 \(r=12\) 的情形还被 gap 的单位部分排除，不能只核对赋值。
写 \(z=10^E\)。第一种有 \(M=(6/5)z^2,b=(4/5)z^3\)，
\(q=3b\)。已知的二进、五进减 gap 给
\(H-3a=2z^2k\)，其中 \(k\) 是整数且与 10 互素。原 word 与球面
分别精确化为

```math
(14z^2+1)k=15Az^3+15Nz-21a,\qquad
k(H+3a)=\frac{72}{25}A^2z^4+2N^2.
```

模 5 下 \(k\equiv-a\)、\(H+3a\equiv a\)，故
\(-a^2\equiv2N^2\pmod5\)。但 \(N,a\) 都是五进单位，这要求
\((N/a)^2\equiv2\pmod5\)，不可能。

第二种有 \(M=(3/25)z^2,b=(14/25)z^3\)、\(q=3b\)，仍可写
\(H-3a=2z^2k\)、\(\gcd(k,10)=1\)。这次两个精确式是

```math
(1+2z^2)k=\frac32Az^3+15Nz-3a,\qquad
k(3a+z^2k)=\frac{441}{625}A^2z^4+49N^2.
```

因为 \(E\ge3\)，模 8 下第一式给 \(k\equiv-3a\)，第二式
给 \(3ka\equiv N^2\)。\(N,a\) 均为奇数，所以左侧为
\(-9a^2\equiv7\)，右侧为 1，矛盾。因此双减 gap 只余定理中的
\(r=24,A=2\) 一族。

#### 二进加 gap 的统一原 word 锁

现在只处理二进加 gap。令 \(d=W/C_Q\)，利用 (A2-rays-five) 得

```math
L=C_M+2d25^E=C_M\beta/b,\qquad LH=r_0\alpha,
```

从而保留原 cut 的精确恒等式是

```math
L(H+Va)=r_0 C_0U+2V(C_M+d25^E)a. \tag{A2-rays-plus}
```

先设 \(m\ge7\)。第一项赋值为 \(m+1\)，左侧为
\(2m+2r_2-3\ge5\)。若 \(C_M+d\not\equiv0\pmod8\)，第二项
赋值至多 3，直接矛盾。反之，完整支持表只给下表的 16 对
\((C_M,d)\)，且它们都满足 \(r_5=0,r_2\ge-1\)。因此左侧
赋值严格超过 \(m+1\)，两项须先同深，必要条件为

```math
v_2(C_M+d25^E)=m=3E,\qquad E\ge3. \tag{A2-rays-exponent-lock}
```

下表全部排除此条件。表中 \(R\) 是唯一满足
\(C_M+d25^R\equiv0\pmod{2^{27}}\) 的模 \(2^{24}\) 指数代表。

| \(C_M\) | \(d\) | \(R\) | \(C_M\) | \(d\) | \(R\) |
|---|---|---|---|---|---|
| 1 | 7 | 11278491 | 1 | 111 | 4080162 |
| 1 | 23 | 9812409 | 1 | 39 | 9107639 |
| 17 | 39 | 9988485 | 1 | 119 | 10397645 |
| 1 | 31 | 7123260 | 1 | 63 | 6779384 |
| 13 | 3 | 3170470 | 1 | 127 | 6463984 |
| 29 | 43 | 1037599 | 29 | 3 | 10147948 |
| 13 | 139 | 8546749 | 1 | 71 | 5210195 |
| 17 | 31 | 8004106 | 17 | 7 | 12159337 |

使用 G12 已列明的 Bugeaud Theorem 2，这次取
\((\alpha_1,\alpha_2)=(25,-C_M/d)\)、\((b_1,b_2)=(E,1)\)、
\(A_1=25,A_2=\max\{8,C_M,d\}\)，仍取 \(m=8,g=1,\mu=4\)。
表中两系数互素，且都是奇数；\(v_2(\alpha_1-1)=3\)、
\(v_2(\alpha_2-1)=v_2(C_M+d)\ge3\)，故 H1、H2 成立。
\(\Lambda=25^E+C_M/d>0\)。由 \(2<\log8\)、\(\log25<4\)、
\(\log A_2<5\) 和 \(3(66.8)4(5)/2^4<256\)，得到

```math
v_2(C_M+d25^E)<256\max\{\log(E+1)+3,12\}^2+3.
```

若左侧至少为 \(3E\)，则 \(E<10^6\)：端点上界小于
\(256\cdot17^2+3=73987<3\cdot10^6\)，其后与 \(E\) 的比值
严格递减，理由同 G12。对 \(E\ge9\)，必要同余的全部代表由
上表给出，而它们均大于 \(10^6\)。\(E=3,\ldots,8\) 的每一
赋值也都严格小于 \(3E\)。模幂、逐位提升、截断二项式分别核对
16 个根；LTE 给周期恰为 \(2^{24}\)，所以这是完整余类证书。
两个小指数 \(E=1,2\) 不在这里的结论中，也没有被遗漏为反例。

最后考虑 \(m\le6\)。F03 先排除 \(f\ge e+n\)，其余首部
都满足 \(r_2=0\)。\(r_5=1\) 的唯一首部 \((1,25)\) 已由 G12
排除；故 (A2-rays-five) 和 \(m\ge5\) 强迫 \(m=6,E=2,D=5\)。
于是

```math
b=800\cdot10^t2^u5^v C_M C_Q<10^6
```

要求 \(t=3,u=v=0,C_M=C_Q=1\)。此时 \(d=100B+r\)，是区间
\([111,139]\) 或 \([211,218]\) 内的奇数。由 (A2-rays-plus)
仍须 \(v_2(1+625d)=6\)，这等价于 \(d\equiv47\pmod{128}\)，
两个区间都不包含该类，矛盾。二进加 gap 至此全部排除，完成
定理的唯一必要族归约。

来源：原 word/sphere 与 G11 的完整支持；固定系数指数式使用
G12 引用的 Bugeaud 显式定理。未对剩余族的原分子恢复作空性外推。


<a id="a2-g15"></a>
### A2-G15　两位有效数字余核的平方和障碍与整数恢复窗

**状态：已严格完成。** G14 唯一未排除族的无界必要条件；不证明
该族为空。设 \(E\ge3,z=10^E\)。若它有原解，则

```math
S_E=816\cdot100^E-31
```

是两个有理数的平方和；特别是每个 \(p\equiv3\pmod4\) 都满足
\(v_p(S_E)\equiv0\pmod2\)。原整数还必须满足下面的恢复系统和
严格窗口；所有素因子都为 \(1\pmod4\) 的整数 \(k\) 处于
\(5z<k<(174/31)z\)。

依赖：[A2-G01](#a2-g01)、[A2-G14](#a2-g14)、[C02](#c02)

核对：`a2-decimal-ray-residual`；符号恒等式、有理端点和四个素数
的完整指数周期。无界必要性由本节证明，不由有限指数试算承担。

#### 原整数恢复与有效窗口

G14 中的记号在这里具体为

```math
A=2,\quad B=1,\quad T=10z^2,\quad M=\frac{12}{5}z^2,
\quad U=z^3,\quad b=\frac45z^3,\quad q=3b.
```

第二、第三分子记为 \(N,a\)。原条件给
\(z^2/10\le N<z^2\)、\(U\le a<2b\)、
\(\gcd(N,M)=\gcd(a,b)=1\)。整数半径 \(H=q\mathcal R\)
满足 \(H>3a\)。G14 的双减 gap 给
\(v_2(H-3a)=2E-1,v_5(H-3a)=2E\)，所以

```math
H-3a=\frac{z^2}{2}k,\qquad k\in\mathbf Z_{>0},\quad \gcd(k,10)=1.
```

代入原 word 和球面分别得到

```math
\left(1+\frac{31}{2}z^2\right)k=120z^3+60Nz-93a, \tag{A2-ray24-word}
```

```math
k\left(3a+\frac{z^2}{4}k\right)=\frac{576}{25}z^4+N^2. \tag{A2-ray24-sphere}
```

这些式子没有改变原 cut。反过来，若整数 \(N,a,k\) 满足两式、
上述原范围和既约性，则 \(H=3a+z^2k/2>0\) 满足原 word/sphere，
因而恢复这个族的原解。只保留消元二次式则不具有这个充分性。

令 \(s=N/z^2\)。G01 的严格 prefix 窗是

```math
\left(\frac ab\right)^2<F(s)
:=\frac{625(2+s)^2}{961}-4-\frac{25s^2}{144}.
```

\(F'(s)=2500/961+(65975/69192)s>0\)，而
\(F(24/25)=36956/24025<25/16\)。因为 \(a\ge U\) 给
\(a/b\ge5/4\)，所以 \(N>(24/25)z^2\)。又

```math
\left(\frac aU\right)^2<\frac{16}{25}F(1)
=\frac{232439}{216225}<\frac{441}{400},
```

故 \(a<(21/20)U\)。若 \(k\le5z\)，则 (A2-ray24-sphere)
左侧小于 \(5z((63/20)z^3+(5/4)z^3)=22z^4\)，右侧大于
\((576/25)z^4>22z^4\)，矛盾。另一方面，用 \(N<z^2,a\ge z^3\)
代入 (A2-ray24-word) 得 \((1+31z^2/2)k<87z^3\)。因此

```math
\boxed{\frac{24}{25}z^2<N<z^2,\qquad
z^3\le a<\frac{21}{20}z^3,\qquad 5z<k<\frac{174}{31}z.} \tag{A2-ray24-window}
```

此外 (A2-ray24-sphere) 右侧为
\(N^2+(24z^2/5)^2\)，两个坐标互素，因为 \(24z^2/5=2M\)
且 \(\gcd(N,2M)=1\)。任何 \(p\equiv3\pmod4\) 都不可能整除
这一个原始平方和：否则 \(-1\) 为模 \(p\) 的平方，或 \(p\)
同时整除两个坐标，均矛盾。\(k\) 为奇数，故其每个素因子都是
\(1\pmod4\)，特别地 \(k\equiv1\pmod4\)。

#### 只含指数的平方和必要条件

消去 \(a\) 给必要二次式

```math
P(N,k,z):=31N^2-60zNk+\left(1+\frac{31}{4}z^2\right)k^2
-120z^3k+\frac{17856}{25}z^4=0.
```

定义全部为整数的

```math
\Delta=2639z^2-124,\quad S=816z^2-31,\quad
X=31N-30zk,\quad Y=\Delta k+7440z^3,\quad V=\frac{2976}{5}z^2.
```

直接配方得到

```math
Y^2-4\Delta X^2=V^2 S.
```

利用 \(\Delta=4S-625z^2\)，这又等价于

```math
\boxed{Y^2+(50zX)^2=S\bigl(V^2+(4X)^2\bigr).} \tag{A2-ray24-norm}
```

\(V>0\)，因此

```math
S=\left|\frac{Y+50zX\,i}{V+4X\,i}\right|^2
```

是两个有理数的平方和。这只是原式的范数恒等式，不是 Gaussian
变换后的合法下降，也没有生成新的原 word。

若 \(p\equiv3\pmod4\)，任意非零整数平方和的 \(p\)-赋值都是
偶数：当它被 \(p\) 整除时，两坐标必须都被 \(p\) 整除，反复
除去 \(p^2\) 即得结论。对 (A2-ray24-norm) 两侧取赋值，两个
平方和的赋值相减，便得到 \(v_p(S)\) 为偶数。允许公因子，
无需假定两边平方和是原始的。

#### 四个完整指数周期给出的无界排除

下面 \(d_p,d_{p^2}\) 分别是 100 在模 \(p,p^2\) 下的精确阶；
\(r_p,r_{p^2}\) 是方程 \(816\cdot100^E\equiv31\) 的唯一指数类。

| \(p\) | \(d_p\) | \(r_p\) | \(d_{p^2}\) | \(r_{p^2}\) |
|---|---|---|---|---|
| 19 | 9 | 6 | 171 | 96 |
| 71 | 35 | 9 | 2485 | 1549 |
| 79 | 13 | 9 | 1027 | 815 |
| 139 | 23 | 5 | 3197 | 189 |

每行均为素数 \(p\equiv3\pmod4\)。模幂给表中根，精确阶给
唯一性，逐项完整周期核对给独立验证。若
\(E\equiv r_p\pmod{d_p}\) 而
\(E\not\equiv r_{p^2}\pmod{d_{p^2}}\)，则 \(v_p(S_E)=1\)，
与上面的偶深条件矛盾。因而每行排除整个无限指数类的相应部分。
进入 \(r_{p^2}\) 类只代表此轮未排除，不证明赋值一定为偶数。

这个障碍也不是原解的充分条件。例如

```math
816\cdot100^{13}-31=83674539967313^2+273127390353400^2.
```

所以不能由平方和障碍单独排除 \(E=13\)，更不能由已排除的
若干指数外推所有 \(E\)。G15 本身到此为止；A2-G16 将这一允许
投影提升为严格窗口内的有理非整数见证，并把原整数恢复压成双变量
充要系统，但仍未证明该整数系统为空。

来源：G14 剩余族的原 word/sphere 精确消元及平方和赋值；不增加
外部定理，也不把同源恒等式重复计为独立预算。


<a id="a2-g16"></a>
### A2-G16　有理系数平面的范数充要性与 r=24 的双向整数恢复

**状态：已严格完成。** 对全部 A2，固定原分母与十进制权重后，原
word/sphere 的有理松弛在非空严格实数弧上恰由 C05 的分母 norm
控制；它不排除整数候选。对 G14/G15 的 `r=24` 余核，进一步把原解
精确等价为两个整数未知量 `(N,k)` 的系统，并给出 `E=13` 的严格窗口
内有理但非整数见证。该见证不是原 Exact Lift 解，本项也不证明该族为空。

依赖：[C01](#c01)、[C02](#c02)、[C05](#c05)、[A2-G01](#a2-g01)、[A2-G14](#a2-g14)、[A2-G15](#a2-g15)

核对：`a2-rational-recovery`；精确有理算术核对 `E=13` 见证、原数值
word/sphere、重新约分后的真实 decimal cuts，以及全部符号恒等式、
严格实数弧公式和模 3/31/10 的恢复同余。无界充要性来自下面的证明，
不是由有限指数试算外推。

#### 原系数平面的统一有理圆

设固定有理系数 `t1,t2,t3,beta`，其中 `beta+t3>0`，并记

```math
\Delta=t_1^2+t_2^2+t_3^2-\beta^2,
\qquad C=\beta+t_3.
```

考虑齐次 word/sphere 系统

```math
R^2=r_1^2+r_2^2+r_3^2,
\qquad \beta R=t_1r_1+t_2r_2+t_3r_3. \tag{A2-rat-plane}
```

若非零解存在，则 `R+r3!=0`：否则球面给 `r1=r2=0`，再由
`C>0` 与平面式得到全零。于是可定义

```math
x=\frac{r_1}{R+r_3},\qquad y=\frac{r_2}{R+r_3}.
```

球面给 `(R-r3)/(R+r3)=x^2+y^2`。将平面式除以 `R+r3` 并配方，
恰得

```math
\boxed{(Cx-t_1)^2+(Cy-t_2)^2=\Delta.} \tag{A2-rat-circle}
```

因此有理非零解必使 `Delta` 为两个有理平方之和。反过来，若
`rho,sigma` 为有理数且 `rho^2+sigma^2=Delta`，取

```math
x=\frac{t_1+\rho}{C},\qquad y=\frac{t_2+\sigma}{C},
```

```math
R_0=\frac{1+x^2+y^2}{2},\quad r_{1,0}=x,\quad r_{2,0}=y,
\quad r_{3,0}=\frac{1-x^2-y^2}{2},
```

直接代入即可恢复 (A2-rat-plane) 的有理解。若需固定
`r1=A/B>0`，在 `x>0` 的目标弧上再乘正有理尺度 `A/(Bx)` 即可。

一旦圆有一个有理点 `(rho0,sigma0)`，全部有理点由

```math
\rho(t)=\frac{\rho_0(1-t^2)-2\sigma_0t}{1+t^2},\qquad
\sigma(t)=\frac{\sigma_0(1-t^2)+2\rho_0t}{1+t^2},\quad t\in\mathbf Q
```

参数化并在实圆上稠密。因此，对固定第一坐标的任意非空**严格**
实数可行弧，窗口内存在有理解当且仅当 `Delta` 是两个有理平方之和。
严格开弧假设不可删；这里没有声称 norm 对任意指定闭窗口都充分。

对 A2，写

```math
A=a_1,\ B=b_1,\ T=10^{m_2},\ U=10^{m_3},\ M=b_2,\ b=b_3.
```

G01 已给 `s2=-1,s3=1`，原系数为

```math
(t_1,t_2,t_3)=(BTU,10MU,b),\qquad \beta=(BT+M)U+b.
```

合法 A2 实数候选不可能有 `Delta<0`，因为 (A2-rat-plane) 与
Cauchy 矛盾；`Delta=0` 时 Cauchy 必取等号，`r` 与 `t` 成正比，
于是

```math
r_3=\frac{Ab}{B^2TU}<\frac{A}{B^2T}\le\frac8{100}<1,
```

又与 `r3>1` 矛盾。因此全部原 A2 候选都在 `Delta>0` 的圆情形。
这证明了一个路线边界：在已经存在严格实数弧的地方，只在有理数域
继续消元或寻找“无有理点”阻碍，与 C05 的 norm 条件等价；真正剩余
障碍必须保留原整数性、逐块既约性和真实 decimal cuts。

#### r=24 余核的所有指数都有严格实数可行弧

沿用 G14/G15，设 `E>=3,z=10^E`，并固定

```math
A=2,\quad B=1,\quad T=10z^2,\quad M=\frac{12}{5}z^2,
\quad U=z^3,\quad b=\frac45z^3.
```

对应 denominator norm 直接展开为

```math
\boxed{\Delta_{\rm dec}
=\frac{16}{25}z^8(816z^2-31)
=\left(\frac45z^4\right)^2S_z,\qquad S_z=816z^2-31.}
\tag{A2-ray24-den-norm}
```

所以 G15 的 `S_z` 平方和障碍正是 C05 分母 norm 除去一个有理平方，
两者不是独立 obstruction。

为证明严格实数弧确实存在，固定 `N=(49/50)z^2`，写 `a=vz^3`。
原拼接比值为

```math
R_z(v)=\frac{5((20+10\cdot49/50)z^2+v)}{2(31z^2+2)}.
```

令

```math
F_z(v)=R_z(v)^2-4-\left(\frac{49}{120}\right)^2
-\left(\frac{5v}{4}\right)^2.
```

精确计算得到

```math
F_z(1)=\frac{640139z^4-4866124z^2-240004}
{14400(31z^2+2)^2}>0,
```

```math
F_z(21/20)=-\frac{6304669z^4+19535596z^2+960016}
{57600(31z^2+2)^2}<0,
```

以及

```math
F_z'(v)=-\frac{5z^2(4805vz^2+620v-596)}
{8(31z^2+2)^2}<0
```

对 `z>=1000,1<=v<=21/20` 成立。故每个 `E>=3` 都有唯一
`v in (1,21/20)` 使原数值 word/sphere 成立；导数非零又给
`N/z^2=49/50` 附近的非空严格实数开弧。由 G15 的 word 恢复

```math
\frac{k}{z}=\frac{120+60\cdot49/50-93v}{31/2+1/z^2}
```

在该矩形内严格落入 `(5,174/31)`。于是对每个 `E>=3`，固定这组
分母后存在满足 G15 严格 `N,a,k` 窗口的**有理松弛**，当且仅当

```math
\boxed{816\cdot100^E-31\text{ 是两个有理数的平方和}.}
\tag{A2-ray24-rational-iff}
```

这里允许 `N,a,k` 为有理数；它不是原整数块问题。

#### E=13 的精确非整数见证

G15 已有

```math
816\cdot100^{13}-31
=83674539967313^2+273127390353400^2.
```

取该圆上的有理旋转参数 `t=-4/9`。记旋转后的两坐标为 `rho,sigma`，
并令

```math
D=2639z^2-124,\qquad V=\frac{2976}{5}z^2,
```

```math
X=\frac{\sigma V}{50z-4\rho},\qquad Y=\rho V-4\sigma X,
```

```math
k=\frac{Y-7440z^3}{D},\qquad
N=\frac{X+30zk}{31},\qquad
 a=\frac{120z^3+60Nz-(1+31z^2/2)k}{93}.
```

`a2-rational-recovery` 以精确分数核对这些公式及原 word/sphere。
归一化数值约为

```text
N/z^2 = 0.9677704730727729...
k/z   = 5.482219320744378...
a/z^3 = 1.0009874076648226...
```

三者均严格位于 G15 窗口，但 `N,k,a` 均非整数。将 `N/M` 与 `a/b`
真正约分后，实际块的位数差变为 `s2=s3=0`；按约分后的整数块重新
十进制拼接，原等式不成立。因此这个见证只证明平方和允许投影确实
可在严格实数窗口中提升为有理 word/sphere 点，不能升级成原反例。

#### 两个整数未知量的原解充要系统

继续令

```math
P(N,k,z)=31N^2-60zNk+\left(1+\frac{31}{4}z^2\right)k^2
-120z^3k+\frac{17856}{25}z^4,
```

```math
L=120z^3+60Nz-\left(1+\frac{31}{2}z^2\right)k.
```

则 G14/G15 的 `r=24` 族有原整数解，当且仅当存在整数 `N,k` 满足

```math
\boxed{
\begin{gathered}
P(N,k,z)=0,\qquad \gcd(N,30)=1,\qquad \gcd(k,310)=1,\\
\frac{24}{25}z^2<N<z^2,\qquad
5z<k<\frac{174}{31}z,\\
93z^3\le L<\frac{1953}{20}z^3.
\end{gathered}}
\tag{A2-ray24-integer-iff}
```

必要性方面，G15 已给原整数 `k`、word/sphere 两式及窗口。原第二块
既约给 `gcd(N,30)=1`。G15 的原始平方和
`N^2+(24z^2/5)^2` 两坐标互素，所以任何 `3 mod4` 素数不整除它；
由 sphere 式中特别取 `p=31` 可得 `31 not| k`。合并
`gcd(k,10)=1` 即得 `gcd(k,310)=1`。消去 `a` 正是 `P=0`，且
`L=93a` 给最后窗口。

充分性方面，假设整数 `N,k` 满足该盒。因 `z=10^E=1 mod3`，有

```math
1+\frac{31}{2}z^2\equiv0\pmod3,
```

故 `3|L`。模 31 时，清除固定分母后有

```math
P\equiv k(k+2zN+4z^3)\pmod{31},
\qquad L\equiv-(k+2zN+4z^3)\pmod{31}.
```

`31 not|k` 与 `P=0` 因而给 `31|L`，所以

```math
\boxed{93\mid L,\qquad a=L/93\in\mathbf Z.}
```

又在模 2、5 下 `L=-k`，故 `a` 为 2、5 单位；而
`b=(4/5)z^3` 只含 2、5，得到 `gcd(a,b)=1`。同理
`M=(12/5)z^2` 只含 2、3、5，`gcd(N,30)=1` 正好恢复
`gcd(N,M)=1`。窗口给正确原位数

```math
\operatorname{digits}(N)=2E,\quad \operatorname{digits}(M)=2E+1,
```

```math
\operatorname{digits}(a)=3E+1,\quad \operatorname{digits}(b)=3E.
```

最后有恒等式

```math
k\left(3\frac L{93}+\frac{z^2}{4}k\right)
-\frac{576}{25}z^4-N^2=-\frac{P(N,k,z)}{31}.
```

故 `P=0` 恢复 G15 的 sphere 式；定义 `H=3a+z^2k/2>0`，word 式
也由 `L=93a` 直接恢复，于是 `beta H=q alpha` 与整数球面同时成立，
返回原 Exact Lift 等式。这里没有改变 decimal cuts，也不再需要额外
搜索第三分子。

因此，G14/F09 的两位有效数字余核已经被压成
(A2-ray24-integer-iff) 这个双变量整数系统。**尚未证明的是该系统对
所有保留 `E>=13` 无整数点。** 同时，至少三位有效数字的普通第二分母
余核仍独立存在，所以本项不能解释为整个 A2 已关闭。

来源：C05 的原 denominator norm、G14/G15 的原 word/sphere 与本节
有理圆反向参数化、严格实数弧和整数恢复同余。所有条件来自同一原
系统，不把 norm、消元式和恢复式重复计作独立预算。

<a id="a2-f01"></a>
### A2-F01　第三分母一位的整个 A2 子层为空

**状态：有限证书。** 全部 A2 且 \(m_3=1\)，第一、第二块及 \(m_2\)
起初无界；偶尾由解析证明排除，奇尾归约为有限标签上的完整指数周期证书。

依赖：[A2-G02](#a2-g02)、[A2-G04](#a2-g04)、[A2-G05](#a2-g05)、[C04](#c04)

核对：`a2-one-digit-tail`、`a2-one-digit-tail-cpp`；任意精度 Python 和独立展开系数的 C++ reader 均排除全部 11,544 个奇尾标签，不设 \(m_2\) cutoff。

#### 偶尾无需枚举

若第二分母二进主导，A2-G05 的 \(1\le\lambda\le m_3=1\) 给
\(5^\lambda=5\)，但同时要求
\(5^\lambda>3\,2^{e+m_2}\ge12\)，矛盾。

若第三分母二进主导，A2-G04 的 \(g<d+m_3=d+1\) 给 \(d\ge g\)。
由于 \(g>f\)，在 \(Q=BT+b_2\) 中只有 \(f=e+m_2\) 的等深抵消
能够使 \(d\ge g\)；赋值不等时 \(d=\min(f,e+m_2)\le f<g\)。
一位尾分母有 \(g\le3\)，而 \(f=e+m_2\ge2\)、\(g>f\)，因此
唯一可能是 \(B=1,m_2=2,f=2,g=3\)。此时另外两分母中恰有第二
分母处于 \(E-1=2\) 层，违反 C05 已用于 A2-G04 的模八必要条件。
故全部偶尾一位子层为空。

#### 奇尾的完整标签界与原式平方必要条件

由 A2-G02，\(B=1,A\in\{2,4,6,8\}\)，且
\(5<b=b_3<10\) 为奇数，所以 \(b\in\{7,9\}\)。记 \(a=a_3\)，则
\(10\le a<2b\)、\(\gcd(a,b)=1\)；\(c\mid b\)；标签 \(k\) 奇且

```math
10c<k<101c,\qquad b_2=\frac{c(10T+b)}{k},\quad T=10^{m_2},\quad m_2\ge2.
```

还可以严格去掉 \(\gcd(k,10b)>1\) 的标签。C04 给
\(b_2\mid\operatorname{lcm}(b,10T+b)\)。对 \(p\mid b\)，因
\(p\ne2,5\) 且 \(p\nmid10T+b\)，有 \(v_p(b_2)\le v_p(b)\)，
于是 \(v_p(c)=v_p(b_2)\)，在 \(k=c(10T+b)/b_2\) 中完全抵消。
此外 \(b,10T+b\) 均为五进单位，所以 \(b_2,k\) 亦为五进单位；
\(k\) 奇已在 A2-G02 证明。故

```math
\boxed{\gcd(k,10b)=1,\qquad \gcd(k,c)=1,\qquad k\mid10T+b.}
```

这些有限范围恰有 11,544 个 \((A,b,a,c,k)\) 标签；保留了一些不满足
其它更强必要条件的标签，因而是原候选的超集。

记 \(\Lambda=k+10c,u=100c,h=\Lambda^2-u^2\ne0\)。A2-G02 的
关于 \(N=a_2\) 的恢复二次式有
\(P(B)=(AkB+c(a-Ab))^2-h(A^2+a^2/b^2)B^2\)，且有理根强迫
\(P(B)\) 为有理平方。代入 \(B=b_2=c(10T+b)/k\)，并乘
\((kb/c)^2\)，得到整数平方的必要条件

```math
\boxed{
W^2=k^2b^2(10AT+a)^2-h(A^2b^2+a^2)(10T+b)^2.
}
\tag{A2-one-tail-square}
```

右侧是整数，有理平方根必为整数。该式仍由原恢复二次式导出，
没有给辅助平方根自由度，也不将它当作充分条件。

#### 有限周期如何覆盖全部指数

令 \(n=m_2-2\ge0\)。对每个标签，\(\gcd(k,10)=1\)，所以
\(T=100\cdot10^n\pmod k\) 是一个完整纯周期。必要整除
\(k\mid10T+b\) 给允许的 \(n\) 模该周期的集合。
对每个奇素数 \(3\le p\le241,p\ne5\)，同样读取
\(100\cdot10^n\pmod p\) 的完整周期，并保留使上式右端为平方类
（含零）的 \(n\) 剩余类。所有周期都由乘十回到首项来确定，
没有用预设的最大指数。

若同一非负整数 \(n\) 同时满足周期 \(r_i,r_j\) 的约束，其两个
剩余类必在 \(\gcd(r_i,r_j)\) 上一致。因此可以反复删除没有相容
剩余类的状态。每次删除都只排除不可能属于共同指数的类；状态总数
有限，过程终止。若任一周期集合变空，就严格排除该标签的所有指数。
反过来，非空状态不声称原候选存在；本证书只使用变空的充分排除。

两个 reader 的完整结果相同：

| 排除原因 | 标签数 |
|---|---:|
| \(b_2\) 整数性周期为空 | 7,080 |
| 某一素数平方类周期为空 | 4,226 |
| 多个指数周期相容传播后为空 | 238 |
| 合计 | 11,544 |
| 未覆盖标签 | 0 |

Python 直接计算因式形式，使用任意精度整数；C++ 独立展开成
\(p_2T^2+p_1T+p_0\)，用反向次序传播周期约束。
C++ 全部多项式计算使用有符号 128 位整数：\(k<909,c\le9,b\le9,
A\le8,a\le17,T\bmod p<241\) 给中间绝对值小于 \(2^{70}\)。
两者均不构造周期的巨型乘积；逐周期长度小于 909。
UBSan 复核也通过。以上完整有限证书排除全部奇尾，结合前面的偶尾
证明，得到整个 \(m_3=1\) A2 子层为空。

该结果覆盖任意前缀位数，却只固定第三分母一位；它没有关闭
\(m_3\ge2\)、全部奇尾或整个 A2。来源：本稿新归约与两个独立精确 reader。

<a id="a2-f02"></a>
### A2-F02　第三分母两位的整个 A2 子层为空

**状态：有限证书。** 全部 A2 且 \(m_3=2\)；第一、第二块及 \(m_2\)
起初无界。完整周期标签覆盖与有界 source 的原二次式证书共同排除。

依赖：[A2-G01](#a2-g01)、[A2-G04](#a2-g04)、[A2-G05](#a2-g05)、[A2-G06](#a2-g06)、[A2-G07](#a2-g07)、[C04](#c04)

核对：`a2-two-digit-tail`、`a2-two-digit-tail-cpp`。C++ 覆盖 47,432,488
个完整周期标签；Python 独立复核全部 250 个筛后标签及 3,366 个有界
原方程二次式。两个 reader 不设指数 cutoff。

#### 偶尾的完整分裂：两个周期类和一个有界 source

设 \(U=100,T=10^{m_2},B=b_1\in\{1,2\},A=a_1\)，继续使用
\(e=v_2(B),f=v_2(b_2),g=v_2(b_3),d=v_2(BT+b_2)\)。

第二分母二进主导时，A2-G05 给 \(1\le\lambda\le2\) 和
\(5^\lambda>3\,2^{e+m_2}\)。故 \(\lambda=2\)，\(e+m_2\le3\)，
且 \(J=v_5(b_3)=0\)。由 \(b_3=2^{e+m_2+2}c\)、\(c=3\pmod4\)、
\(50<b_3<100\)，\(e+m_2=2\) 没有合法 \(c\)，而
\(e+m_2=3\) 只有 \(c=3,b_3=96\)。当 \(B=1,m_2=3\)，Hensel 锁
给 \(r=v_2(5^5+3)=3\)，于是 \(v_2(b_2)=8\)，位数窗只留
\(b_2=256,768\)。当 \(B=2,m_2=2\)，则
\(r=v_2(5^4+3)=2\)，强迫 \(b_2\ge128>10^{m_2}\)，故为空。

第三分母二进主导时，A2-G04 给 \(g<d+2\)，即 \(d\ge g-1\)。
若 \(f\ne e+m_2\)，则 \(d=\min(f,e+m_2)\le f<g\)，故
\(d=f=g-1\)。当 \(g\ge2\)，C05 的模八条件要求第一分母也在
\(g-1\) 层；于是 \(e=f=1,g=2,B=2\)。当 \(g=1\)，必须单列
\(e=f=0,B=1\)，不能使用只适用于 \(E\ge2\) 的分母计数规则。
因此无界 ordinary 类恰为

```math
\boxed{
\begin{array}{c|c|c}
B&v_2(b_2)&b_3\\\hline
1&0&54,58,62,66,70,74,78,82,86,90,94,98\\
2&1&84,92.
\end{array}}
```

第二行使用 \(b_3>5U/6\)。其 \(b_3=84\) 又被
\(a_3\ge101\)、\(a_3/b_3<6/5\) 直接排除；证书保留该空尾窗以审计
覆盖，而不删除其来源。

余下 \(f=e+m_2\)。因为 \(f\ge2\)，若 \(g=f+1\)，第二分母是
唯一处于 \(E-1\) 层者，违反模八。因此 \(g\ge e+m_2+2\)。两位
分母的 \(g\le6\) 给 \(m_2\le4-e\)。结合真实尾窗，source 状态只有

```math
(B,m_2,b_3)\in
\{(1,2,64),(1,2,80),(1,2,96),(1,3,64),(1,3,96),(1,4,64),(2,2,96)\}.
```

至此所有偶尾均进入 ordinary 周期类，或明示有界 source，或上面的
两个前缀主导状态；没有遗漏 \(g=1\) 的分子奇偶自由情形。

#### 三个周期类的有限完整标签

奇尾由 A2-G06 的 \(m_3=2\) 行归约为 \(B=1\)，以及
\((A,v_2(a_3))=(2,0),(6,0),(4,1),(8,2)\)。所有周期类中
\(B\mid b_3\)，故 C04 给
\(b_2\mid\operatorname{lcm}(b_3,BTU+b_3)\)。令
\(b=b_3,a=a_3,c=\gcd(b_2,b)\)，得到

```math
\boxed{k=\frac{c(BUT+b)}{b_2}\in\mathbf Z_{>0},\qquad
b_2=\frac{c(BUT+b)}k,\qquad
BcU<k<(10B+1/10)cU.}
```

标签范围还包括 \(c\mid b\)、\(\gcd(a,b)=1\)、原三位尾分子窗口，
以及下面的完整分母深度约束。记 \(J=v_5(b)\)、
\(b_0=b/(2^{v_2(b)}5^J)\)。因 \(b<100\)，\(J\le2<m_2+2\)，
所以 \(v_5(BTU+b)=J\)。A2-G05 给 \(v_5(b_2)<J\)（\(J>0\) 时），
故 \(v_5(c)<J\)，并且 \(v_5(k)=J\)。\(J=0\) 时这些量均为零。
对每个 \(p\mid b_0\)，C04 给 \(v_p(b_2)\le v_p(b)\)，从 \(k\)
定义中消去后得 \(\gcd(k,b_0)=1\)。二进深度如下：

| 周期类 | \(v_2(c)\) | \(v_2(k)\) | 完整标签数 |
|---|---:|---:|---:|
| 奇尾、\(B=1\) | 0 | 0 | 33,683,610 |
| 偶尾 ordinary、\(B=1,g=1\) | 0 | 1 | 13,541,128 |
| 偶尾 ordinary、\(B=2,g=2\) | 1 | 2 | 207,750 |
| 合计 | | | 47,432,488 |

上述 \(v_2(k)\) 直接由
\(v_2(k)=v_2(c)+v_2(BTU+b)-v_2(b_2)\) 得到。这些标签是原候选
的超集，未把仅通过必要过滤的点当作原解。

#### 原平方恢复、既约性和完整指数周期

令 \(\Lambda=k+cU,u=10cU,h=\Lambda^2-u^2\ne0\)。三类的
\(v_2(\Lambda)\) 都小于 \(v_2(u)\)，故 \(h\) 非零。仍记
\(M=b_2,N=a_2\)。原 word 精确给

```math
\beta=M\Lambda/c,\qquad
cB\alpha=AkM+10cBU N+c(Ba-Ab).
```

与球面联立的恢复式为

```math
\Lambda^2\{(A^2+B^2a^2/b^2)M^2+B^2N^2\}
=[AkM+10cBU N+c(Ba-Ab)]^2.
```

有理根的判别式因此强迫整数平方必要条件

```math
\boxed{
W^2=k^2B^2b^2(AUT+a)^2-h(A^2b^2+B^2a^2)(BUT+b)^2.
}
\tag{A2-two-tail-square}
```

同时，A2-G07 的证明在乘 \(B^2\) 后同样适用：若
\(p\nmid10kb\)、\(p\mid Ba-Ab\)、\(p\nmid h\)，则
\(BUT+b\ne0\pmod p\)，否则恢复二次式强迫 \(p\mid N,M\)。
此项只读取原根的既约性，不增加独立预算。

去掉 \(k\) 的 2/5 部分后，余下 \(K\) 与 \(10c\) 互素；2/5 部分已
由上表的深度支付。因此整数性等价于
\(K\mid BUT+b\)。\(T=100\cdot10^n,n=m_2-2\ge0\) 在模 \(K\)
上是纯周期。C++ 以完整乘法阶和 baby-step/giant-step 读取这个周期
的唯一允许指数类或证明没有允许类；算法完整扫描生成子群，非随机
搜索。所有单位模数 \(K\le500\) 的全部单位目标另由直接循环轨道
核对这个算法。Python 对筛后标签重新使用直接完整轨道，不调用该算法。

其它素数上的平方类周期按 A2-F01 的相容传播处理。第一次使用
\(3\le p\le241,p\ne5\)；第二次对筛后标签使用
\(3\le p\le397,p\ne5\) 及原既约性过滤。A2-G01 的严格实数窗在
周期之前排除全部指数下几何不可能的标签。两个 reader 的覆盖为

| 周期类 | 全指数实数窗 | 整数性周期 | 单素数平方类 | 联合周期 | 首轮剩余 |
|---|---:|---:|---:|---:|---:|
| 奇尾 | 26,862,513 | 4,985,137 | 1,529,143 | 306,627 | 190 |
| 偶尾 \(B=1\) | 11,091,013 | 1,715,977 | 657,938 | 76,140 | 60 |
| 偶尾 \(B=2\) | 108,030 | 77,064 | 22,331 | 325 | 0 |

独立展开系数的 reader 首轮同样给 250 个标签。任意精度 Python
逐一读取完整轨道，249 个由第二轮周期/既约性排除；唯一剩余标签为
\((B,A,b,a,c,k)=(1,6,74,109,37,34054)\)，下面用原恢复式关闭。

#### 唯一剩余周期标签的解析二进末端

对该标签清除原恢复方程的固定分母，将关于 \((N,T)\) 的六个整数
系数共同除以 content \(87616=2^6\cdot37^2\)。所得 primitive
二次式的系数（按 \(N^2,NT,N,T^2,T,1\)）是

```math
\begin{aligned}
(&4085282209855041,\ -119069622000300000,\ -21630981330054500,\\
 &10829959500030625,\ 55916663430145825,\ 24312354841938084).
\end{aligned}
```

若 \(m_2\ge6\)，\(T=0\pmod{64}\)，primitive 恢复式模 64 成为

```math
N^2+28N+36=0\pmod{64},\qquad (N+14)^2=32\pmod{64}.
```

平方不可能恰有五层二进赋值，因此无解。若 \(2\le m_2\le5\)，
\(c(100T+74)\) 除以 \(k=34054\) 的余数依次为
\(32198,24906,20094,6028\)，都非零，第二分母根本不是整数。
这里使用有证明的有限低指数和全体高指数分裂，不是搜索到某个
最大指数后外推空性。C++ 与 Python 分别检查 primitive 系数和全部
64 个剩余类，均排除该标签。

#### 有界偶尾 source 的原方程核对

上面七个 source 状态通过
\(b_2\mid\operatorname{lcm}(B,b_3,BTU+b_3)\)、原位数及
\(v_2(b_2)=e+m_2\) 只给 16 个分母组合。加上两个前缀主导状态，
共 18 个。对每个组合枚举全部第一块和原三位既约尾分子；关于
\(N=a_2\) 直接使用原平方等式的二次式。若
\(D=(Bb_2b_3)^2,L=ATU+a_3\)，三个系数为

```math
\begin{aligned}
c_2&=\beta^2(Bb_3)^2-(10U)^2D,\\
c_1&=-2L(10U)D,\\
c_0&=\beta^2\{(Ab_2b_3)^2+(a_3Bb_2)^2\}-L^2D.
\end{aligned}
```

\(c_2\ne0\)：否则正 \(\beta=10Ub_2\)，使
\(b_3=U(9b_2-BT)\)，违反 \(0<b_3<U\)。任意精度 Python 完整读取
3,366 个二次式，零个平方判别式，因而不存在整数第二分子根。

至此奇尾、偶尾 ordinary、偶尾 source 及前缀主导都已穷尽排除。
C++ 多项式运算使用有符号 128 位整数，明示范围
\(k<100000,c,b<100,A\le13,B\le2,a<200,T\bmod p<397\) 给中间量
绝对值小于 \(2^{100}\)；UBSan 复核通过。Python 对全部筛后标签、
完整标签总数和有界原二次式独立使用任意精度整数核对。
因此**整个两位尾 A2 子层为空**，但 \(m_3\ge3\) 和整个 A2 仍待证。
来源：本稿新归约与精确有限周期/原方程证书。

<a id="a2-f03"></a>
### A2-F03　三至六位偶尾的两个有界二进类为空

**状态：有限证书。** A2、\(m_3\in\{3,4,5,6\}\)、\(b_3\) 偶，且
第二分母二进主导，或尾分母二进主导且
\(v_2(b_2)\ge v_2(b_1)+m_2\)。覆盖这两个类的任意前缀；不关闭整个
三至六位尾，不覆盖其余 ordinary 类。

依赖：[A2-G01](#a2-g01)、[A2-G04](#a2-g04)、[A2-G05](#a2-g05)、[A2-G08](#a2-g08)、[C04](#c04)

核对：`a2-short-prefix-even`、`a2-short-prefix-even-six`。三、四位尾
用两个独立 reader 全行核对；五位尾用任意精度 C++ 和独立 Python
全行 sphere 判别式核对；六位尾用同一 C++ 完整枚举及 Python 的
完整系数、行数和平方投影审计，未重复用 Python 扫描约 297 亿行。

G08 的有效界对 \(m_3=3,4,5,6\) 分别给
\((G,H)=(9,5),(13,7),(16,10),(19,12)\)。第二分母主导时
\(m_2\le H-e,g=e+m_2+m_3,f\ge g+2\)；尾分母主导且
\(f\ge e+m_2\) 时 \(m_2\le G-e-2,g\ge f+2\)。所以枚举的
\(m_2\) 集合完整而有限。G01 给 13 个第一块及严格尾窗。

对每个 \((B,m_2,b_3)\)，C04 必要条件是

```math
b_2\mid\operatorname{lcm}(B,b_3,B10^{m_2+m_3}+b_3).
```

取全部正因子，保留第二分母原位数、上述二进主导条件、
\(v_2(\beta)=\max(e,f,g)\) 和 G05 的五进主导条件，得到完整必要
超集。对每个第一分子 \(A\)，令 \(x=b_2/T\)，G01 的严格实数窗为

```math
\frac{a_3^2}{b_3^2}<F(A,B,x,1)
=\frac{(A+1)^2}{(B+x)^2}-\frac{A^2}{B^2}-\frac1{100x^2}.
```

枚举原尾分子 \(U\le a_3<2b_3\)（\(B=2\) 时用更强的
\(a_3<6b_3/5\)），保留 \(\gcd(a_3,b_3)=1\)。几何端点以有理数
和整数平方根实现，没有浮点舍入。

对每行记 \(M=b_2,b=b_3,a=a_3,L=ATU+a,D=(BMb)^2\)。直接由原
word/sphere 清分母得到第二分子 \(N=a_2\) 的二次式：

```math
\begin{aligned}
c_2&=\beta^2(Bb)^2-(10U)^2D,\\
c_1&=-2L(10U)D,\\
c_0&=\beta^2[(AMb)^2+(aBM)^2]-L^2D.
\end{aligned}
```

\(c_2\ne0\)：否则正数开方给 \(\beta=10UM\)，于是
\(b=U(9M-BT)\)，违反 \(0<b<U\)。因此完整整数平方判别式和
两根恢复足以判定该行全部原 \(N\)。恢复后仍须满足
\(T/100\le N<T/10\)、\(\gcd(N,M)=1\)。独立 reader 取
\(q=\operatorname{lcm}(B,M,b)\)，从
\(\beta^2\sum y_i^2=(q\alpha)^2\) 展开；每行系数恰相差
\((BMb/q)^2\)，并核对判别式多项式及全部平方投影的有理根。

| \(m_3\) | 分母组合（第二分母主导） | 原二次式 | 第二分母主导行 | 尾高深度行 | 平方投影 | 合法根 |
|---|---:|---:|---:|---:|---:|---:|
| 3 | 114（8） | 16,067 | 643 | 15,424 | 1 | 0 |
| 4 | 1,814（22） | 2,202,520 | 38,013 | 2,164,507 | 1 | 0 |
| 5 | 23,306（85） | 269,940,375 | 607,105 | 269,333,270 | 1 | 0 |
| 6 | 270,385（333） | 29,740,339,198 | 17,325,104 | 29,723,014,094 | 3 | 0 |

六个平方投影并未删除。\(m_3=3\) 时唯一投影
\((A,B,m_2,M,a,b)=(3,1,2,12,1203,944)\)，两根为
\(-5082927/9499,639189/87143\)；\(m_3=4\) 时唯一投影
\((1,1,2,12,11289,9440)\)，两根为
\(-1522007/8142,11877067/1220002\)。\(m_3=5\) 时唯一投影为
\((3,1,2,12,146301,85760)\)，两根
\(-216114849/406288,21054729/2126848\)。六位尾的三个投影为

| \((A,B,m_2,M,a,b)\) | 两根 |
|---|---|
| `(3,1,2,20,1172147,859600)` | `−31836130/303009`、`24631090680270/2418859254511` |
| `(5,1,2,12,1527307,970400)` | `−3535031726607/3964153141`、`343879/35177` |
| `(5,1,2,12,1259143,980480)` | `−4993344665/5600992`、`4352938185/495730688` |

全部均不是整数，因此没有原第二分子。由已证前缀界和完整有限覆盖，上述明示两个类为空。

五、六位尾 C++ 使用 Boost `cpp_int` 任意精度整数。令

```math
Q(a)=B^4b^4(ATU+a)^2-c_2(A^2b^2+B^2a^2),
\qquad \Delta_N=4\beta^2M^2Q(a).
```

所以原判别式为平方恰当且仅当 \(Q(a)\) 为整数平方。模数
\(64,63,11,13,17,19,23,31\) 的平方类只作必要过滤；所有通过者再
用精确整数平方根及原两根恢复。Python 独立容斥重算全部行数，
并从 lcm-sphere 的二次式重算关于 \(a\) 的判别式多项式，逐行检查
全部 269,940,375 个判别式，得到同一个平方投影及同一对有理根。
六位尾对全部 297,935 条活跃系数记录，独立以 lcm-sphere 在
`a=0,1,2` 的值恢复判别式二次多项式，与 C++ 的 product 多项式
逐系数一致；因为次数至多二，等式覆盖每条记录的全部尾分子。
Python 用互素区间容斥独立核对全部行数，每条记录的计数也在 C++
中逐行重算；三个平方投影再独立恢复原根。六位尾的平方类筛选循环
没有第二套全枚举，其审计边界明确限于上述系数、计数与投影。

六位尾的 `T,M<10^17` 和总计数小于 `2^64`；`a,b<2·10^6`，
仅循环索引用 32/64 位整数，全部多项式及平方根使用任意精度整数。
临时二进制、行表和日志不进入仓库。

来源：G08 新有效界后的原方程精确证书。未对尾长 \(\ge7\)、奇尾或
\(f<e+m_2\) 的 ordinary 偶尾作外推。

<a id="a2-f04"></a>
### A2-F04　三位尾且第二分母含 5 的整个 A2 子域为空

**状态：有限证书。** 全部 A2、\(m_3=3\)、\(v_5(b_2)>0\)，包括
奇尾和偶尾、任意 \(m_2\)。不排除第二分母为五进单位的其余三位尾。

依赖：[A2-G01](#a2-g01)、[A2-G04](#a2-g04)、[A2-G05](#a2-g05)、[A2-G06](#a2-g06)、[A2-G08](#a2-g08)、[A2-F03](#a2-f03)、[C04](#c04)

核对：`a2-three-digit-five`、`a2-three-digit-five-cpp`。完整周期标签
120,626,568 个；Python 用互素区间容斥独立重算总数，用完整循环
轨道复核全部四个筛后标签，另以两个原式 reader 排除 100 个有界例外。

#### 完整分裂及分母标签

固定 \(U=1000,F=v_5(b_2)>0,J=v_5(b_3)\)。G05 给 \(J>F\)，位数
给 \(J\le4\)，因而 \(1\le F\le3\)。若 \(F<m_2\)，G08 五进
两个 gap 强迫 \(J-F=1\) 或 \(J-F=3\)。其它情形只有
\(J-F=2,m_2\le F\)，下文单独完整处理。

奇尾由 G06 的 \(m_3=3\) 行给 \(B=1\)，以及
\((A,v_2(a_3))=(4,0),(8,0),(8,1)\)。

偶尾的第二分母主导和 \(f\ge e+m_2\) 类已经由 F03 排除，所以
只余 G08 ordinary。若 \(B=1,f=0\)，\(g<m_3\)，因此 \(g=1,2\)；
若 \(B=1,f>0\)，二进减 gap 的 \(m_3=3D-1\) 不可能，只能加 gap
\(D=2\)，即 \(g=f+2\)。若 \(B=2,f=0\)，第一分子奇，
\(p_1=g-1<p_2\)，故 \(\sigma=2(g-1)\)；\(g<3\) 且 \(g>1\)
强迫 \(g=2,\delta=1\)，加 gap 却只有一层，违反 G04。若
\(B=2,f=1\)，G08 给 \(g=2,3\)；若 \(B=2,f\ge2\)，则
\(g=f+2\ge4\)，且 \(J\ge2\)，所以 \(400\mid b_3\)，严格窗
\(2500/3<b_3<1000\) 中没有 400 的倍数。因此偶尾完整形态是

```math
\begin{array}{c|c}
B& (f,g)\\\hline
1&(0,1),(0,2),\ \text{或 } f\ge1,g=f+2;\\
2&(1,2),(1,3).
\end{array}
```

统一记 \(b=b_3,a=a_3,c=\gcd(b_2,b)\)。与 F02 一样，C04 给

```math
b_2=\frac{c(BUT+b)}k,\quad BcU<k<(10B+1/10)cU,\quad c\mid b.
```

由于 \(J\le4<m_2+3\)，首项 \(BUT\) 的五进深度更高，故
\(v_5(BUT+b)=J\)、\(v_5(c)=F<J\)、\(v_5(k)=J\)。各 ordinary
二进形态则给 \(v_2(c)=f,v_2(k)=g\)；奇尾时两者皆零。
对 \(b_0=b/(2^g5^J)\)，C04 又给 \(\gcd(k,b_0)=1\)。
\(c\le b/5<200\)，所以 \(k<2,010,000\)，标签确实有限且范围有效。
对每个标签仍保留原尾位数、既约性、G01 严格实数窗。

#### 完整周期与原恢复根既约性

原二次式的整数平方必要条件仍为

```math
W^2=k^2B^2b^2(AUT+a)^2-h(A^2b^2+B^2a^2)(BUT+b)^2,\qquad
h=(k+cU)^2-(10cU)^2.
```

上面的二进形态均使 \(v_2(k+cU)<v_2(10cU)\)，所以 \(h\ne0\)。
设 \(K=k/(2^{v_2(k)}5^J)\)；\(\gcd(K,10bc)=1\)，原分母整数性
必要条件是 \(BUT+b=0\pmod K\)。\(T=100\cdot10^n,n\ge0\)，在
\(K\) 及各素数模数上的完整指数周期均可有限计算。低指数的额外
二进原整数性要求只会进一步缩小超集，未用它错误过滤原候选。

同时，若 \(p\nmid10kb\)、\(p\mid Ba-Ab\)、\(p\nmid h\)，则原
候选必须 \(BUT+b\ne0\pmod p\)：否则恢复式在 \(b_2=0\pmod p\)
上给 \(hB^2a_2^2=0\)，与逐块既约性矛盾。此过滤读取同一个原
恢复根，不重复计入独立预算。

C++ 的首轮采用所有 \(3\le p\le397,p\ne5\) 的平方类及上述既约
条件，完整周期之间按公共 period 的 gcd 传播必要余类。空余类集合
即可排除全部无界指数，没有指数 cutoff。

| 首分母 | 完整标签 | 实数窗排除 | 整数周期排除 | 平方/既约周期排除 | 首轮剩余 |
|---|---:|---:|---:|---:|---:|
| 1 | 119,936,428 | 102,091,229 | 12,846,601 | 4,998,594 | 4 |
| 2 | 690,140 | 370,166 | 200,379 | 119,595 | 0 |

首轮四个标签按 \((B,A,b,a,c,k)\) 为
\((1,4,725,1009,145,1149275)\)、\((1,2,850,1311,85,581650)\)、
\((1,5,850,1523,85,783550)\)、\((1,4,925,1033,185,1431725)\)。
扩大到 \(p\le499\) 的同一完整周期条件后全被排除。Python 使用
任意精度因式形式、直接循环轨道，独立复核这四个标签；总数用
\(k=2^g5^Jz,\gcd(z,10b_0)=1\) 的区间容斥独立重算。
C++ 可切换展开多项式 reader；在上述有限标签界内，所有带符号
128 位中间整数小于 \(2^{124}\)，可用 `--ubsan` 复核。

#### \(J-F=2\) 的全部有界例外

\(J=3,F=1\) 要求 \(m_2\le1\)，已不在 A2；唯一剩余为
\(J=4,F=2,m_2=2,b=625\)，必为奇尾、\(B=1\)。\(A=8\) 被
G01 的 \(w^2<235/121\) 排除，因为 \(w\ge1000/625=8/5\)；因此
\(A=4\)。C04 使二位 \(b_2\) 是
\(\operatorname{lcm}(625,100625)=100625=5^4\cdot7\cdot23\) 的因子，
且五进深度为 2，所以仅 \(b_2=25\)。枚举全部
\(1000\le a_3<1250\)、\(a_3\) 奇、\(5\nmid a_3\)，恰为 100 行；
F03 的两个原二次式 reader 均给非平方判别式。没有第二分子根。

以上覆盖全部分裂，故明示子域为空。来源：G08 联合赋值后的新完整
周期证书；没有对 \(v_5(b_2)=0\) 或其它尾长作外推。

<a id="a2-f05"></a>
### A2-F05　第二分母两位的整个 A2 子层为空

**状态：有限证书。** 全部 A2 且 \(m_2=2\)，任意第三块位数及第一块；
不是固定尾长的截断枚举。\(m_2\ge3\) 仍未全部排除。

依赖：[A2-G01](#a2-g01)、[A2-G02](#a2-g02)、[A2-G04](#a2-g04)、[A2-G05](#a2-g05)、[A2-G10](#a2-g10)、[C04](#c04)

核对：`a2-fixed-prefix`。任意精度整数；每行原 product 二次式与
独立 lcm-sphere 判别式完全比较。

固定 \(T=100\)，全部第一块为 G01 的 13 种，\(10\le M=b_2<100\)、
\(1\le N=a_2<10\)、\(\gcd(N,M)=1\)。G01 的严格前缀实数窗要求

```math
D=C_0^2D_0-Q^2S>Q^2D_0,
```

因为 \(a_3^2/b_3^2>1\)，且其严格上界为
\(C_0^2/Q^2-S/D_0=D/(Q^2D_0)\)。完整枚举恰留下 **102 个前缀**。
G10 对它们的有效界最大为 **\(m_3\le20\)**，最大值来自
\((A,B,N,M)=(7,2,9,13)\)。没有截断超过已证界的指数。

对每个前缀、\(1\le m_3\le\) 该前缀的 G10 界，取全部
\(C\mid L\)、\(0\le g\le\max(e,f,d_2+m_3)\)、
\(0\le J\le\max(F,d_5+m_3)\)，恢复 \(b=2^g5^JC\)。保留 G01 严格
尾窗、G02 的奇尾原奇偶、G04/C05 的二进唯一最大及模八条件、
\(v_2(\beta)=\max(e,f,g)\)、G05 的五进主导及
\(v_5(\beta)=J\)（\(J>F\) 时），还有 C04 的完整第二分母整除。
它们只缩小必要超集，不把允许点当成原候选。

不枚举巨大尾分子区间。以 \(a=a_3\)、\(U=10^{m_3}\)、
\(\beta=QU+b\)，原方程关于 \(a\) 的整数二次式为

```math
\begin{aligned}
c_2&=D_0(\beta^2-b^2)>0,\\
c_1&=-2C_0Ub^2D_0,\\
c_0&=\beta^2b^2S-C_0^2U^2b^2D_0,
\end{aligned}
```

```math
\boxed{c_1^2-4c_2c_0
=4(BM\beta b)^2 W,\qquad W=U(UD-2QbS).}
```

原有理根因此强迫 \(W\) 为整数平方。另一 reader 以
\(q=\operatorname{lcm}(B,M,b)\)、固定 \(y_1=qA/B,y_2=qN/M\)，直接
展开 \(\beta^2[y_1^2+y_2^2+(qa/b)^2]=q^2(C_0U+a)^2\)，逐行重算
原判别式并与因式形式比较，保留正确的平方缩放因子。

完整支持枚举留下 **12,025 行**，全部 \(W>0\)，两 reader 都给零
平方判别式。因此连有理尾分子也无法恢复，更不可能有满足原位数
和既约性的整数尾分子。由 G10 的完整有效尾长界，本子层为空。

来源：G10 后的新完整原方程证书；不向其它 \(m_2\) 外推。

<a id="a2-f06"></a>
### A2-F06　第二分母三、四位的整个 A2 子层为空

**状态：有限证书。** 全部 A2 且 \(m_2\in\{3,4\}\)，任意尾长与第一块；
\(m_2\ge5\) 仍未全部排除。

依赖：[A2-G01](#a2-g01)、[A2-G02](#a2-g02)、[A2-G04](#a2-g04)、[A2-G05](#a2-g05)、[A2-G10](#a2-g10)、[C04](#c04)

核对：`a2-fixed-prefix-three`、`a2-fixed-prefix-four`。与 F05 同一个
原方程入口，两个 reader
逐行核对；任意精度整数，无指数截断。

对 \(T=10^{m_2}\)，取全部原位数窗
\(T/10\le M<T,T/100\le N<T/10\)、\(\gcd(N,M)=1\) 及 G01 的
13 个第一块。与 F05 相同的严格实数窗留下以下完整前缀集合：

| \(m_2\) | 前缀数 | G10 最大有效尾长 | 尾二次式 |
|---|---:|---:|---:|
| 3 | 11,993 | 30 | 55,508 |
| 4 | 1,229,008 | 40 | 7,448,321 |

枚举支持不扫描巨大尾区间。G10 的完整二进分裂允许
\(g=0,d_2+m,m+d_2-1\)，或整数
\(g=(m+d_2+1-\kappa_2)/3\)，或临界整数
\(\max(e,f)<g\le d_2-c_2\)。五进允许 \(J=0,m+d_5\)，或整数
\(J=(m+d_5-\kappa_5)/3\)，或临界整数 \(F<J\le d_5-c_5\)。
取各列表的并集、去重并保留非负整数；每个 \(C\mid L\) 恢复
\(b_3=2^g5^JC\)。所有原候选都由 G10 落入这些支持，额外允许点
只扩大必要超集。

保留与 F05 相同的原尾窗、完整 denominator complement、二进/五进
主导及 word 深度。剩余尾二次式数见表，全部 \(W>0\)。
使用 F05 的原判别式恒等式和独立 lcm-sphere 展开，逐行都给非平方
判别式，故没有有理或整数尾根。完整有效界后，此子层为空。

来源：G10 后的三、四位完整前缀子层证书，不外推到更长第二分母。

<a id="a2-f07"></a>
### A2-F07　三位尾且尾分母含 5 的整个 A2 子域为空

**状态：有限证书。** 全部 A2、\(m_3=3\)、\(5\mid b_3\)，任意前缀。
结合 F04，三位尾的其余原候选必须 \(5\nmid b_2b_3\)。

依赖：[A2-G01](#a2-g01)、[A2-G04](#a2-g04)、[A2-G05](#a2-g05)、[A2-G06](#a2-g06)、[A2-G08](#a2-g08)、[A2-F03](#a2-f03)、[A2-F04](#a2-f04)、[C04](#c04)

核对：`a2-three-tail-five`。完整周期部分 2,990,309,248 个标签；Python
以互素区间容斥独立重算覆盖，完整循环轨道复核全部 117 个首轮剩余。

若 \(F=v_5(b_2)>0\)，已由 F04 排除。设 \(F=0,J=v_5(b_3)>0\)，
G08 给 \(J=1,3\)。F03 排除了偶尾的第二分母主导与高前缀深度类；
余下 ordinary 中 \(B=1\) 允许 \((f,g)=(0,1),(0,2)\) 或
\(f\ge1,g=f+2\)。\(B=2,f=0\) 同 F04 的二进 gap 矛盾；
\(f=1\) 允许 \(g=2,3\)，\(f>1\) 允许 \(g=f+2\)。此次 \(J=1\)，
后一个首分母 2 类必须保留，不能沿用 F04 的 \(J\ge2\) 位数排除。
奇尾仍为 G06 的 \((A,v_2(a_3))=(4,0),(8,0),(8,1)\)。

沿 F04 定义 \(c=\gcd(b_2,b_3)\)、\(b=b_3,a=a_3\) 及
\(b_2=c(BUT+b)/k\)。标签范围相同，但现在
\(v_5(c)=0,v_5(k)=J\)、\(v_2(c)=f,v_2(k)=g\)，
\(\gcd(k,b_0)=1\)。因为 \(J\le3<m_2+3\)，这些五进赋值覆盖全部
无界指数。\(B=1\) 时 \(c\le199\)；\(B=2\) 时上述二进形态再给
\(c\le99\)。因此仍 \(k<2,010,000\)，带符号 128 位中间数界
\(2^{124}\) 不变。

使用 F04 的原平方恢复、既约根过滤、完整整数周期和所有
\(p\le397,p\ne5\) 的平方类：

| 首分母 | 全标签 | 实数窗排除 | 整数周期排除 | 平方/既约周期排除 | 首轮剩余 |
|---|---:|---:|---:|---:|---:|
| 1 | 2,966,809,178 | 2,535,544,392 | 321,793,054 | 109,471,615 | 117 |
| 2 | 23,500,070 | 10,277,559 | 10,250,306 | 2,972,205 | 0 |

独立 Python 的完整轨道及 \(p\le499\) 同一原条件排除 113 个，
余下四个 \((B,A,b,a,c,k)\) 为
\((1,4,865,1311,173,1705505)\)、\((1,4,905,1289,181,1485415)\)、
\((1,4,915,1319,61,513355)\)、\((1,4,965,1573,193,1729435)\)。
扩大到 \(p\le601\) 后全被排除；没有指数 cutoff。完整分裂及有限
周期证书关闭明示子域，其余三位尾仍保留。

来源：五进单位第二分母、正五进尾主导的完整周期新证书；没有对
\(5\nmid b_2b_3\) 或其它尾长外推。

<a id="a2-f08"></a>
### A2-F08　三位奇尾且后两分母互素的整个 A2 子域为空

**状态：有限证书。** 全部 A2、\(m_3=3,b_3\) 奇、
\(\gcd(b_2,b_3)=1\)，任意第二块位数。非互素奇尾仍保留。

依赖：[A2-G01](#a2-g01)、[A2-G02](#a2-g02)、[A2-G05](#a2-g05)、[A2-G06](#a2-g06)、[A2-G07](#a2-g07)、[A2-G11](#a2-g11)、[A2-F07](#a2-f07)、[C04](#c04)

核对：`a2-three-odd-coprime`。完整 476,207 个标签，C++ 因式/展开
两个 reader 与 UBSan；任意精度 Python 重算全部几何、整数性轨道，
并对全部 25,683 个剩余标签逐一检查完整素数周期。

若 \(5\mid b_3\)，已由 F07 排除。其余设 \(5\nmid b_3\)，G05
强迫 \(5\nmid b_2\)。G02 给 \(B=1\)、两个后分母全奇；G06 在
三位尾时只允许 \(A=4,8\)。设 \(b=b_3,a=a_3,U=1000\)，则完整
标签为

```math
501\le b<1000,\quad \gcd(b,10)=1,\quad c=1,\quad
1000<k<10100,\quad\gcd(k,10b)=1,\quad b\mid k+1000.
```

最后一式来自 G11 的完整支持锁，而非新的指数 cutoff。G06 要求
\(A=4\) 时 \(a\) 奇，\(A=8\) 时 \(v_2(a)\le1\)；仍保留
\(1000\le a<2b,\gcd(a,b)=1\)。共有 982 个 \((b,k)\) 标签，
带尾分子与第一块后共有 476,207 个标签。原分母始终恢复为
\(M=(1000T+b)/k,T=10^{m_2}\)。

G01 的严格实数窗按 \(x\ge\max(1000/k,1/10)\) 排除 407,864 个
标签；对 \(A=4,8\) 该几何函数关于 \(x\) 严格递减，使用端点只是
必要超集。C++ 按尾分子平方的单调上界划分区间，Python 独立逐个
尾分子计算精确有理数窗；两者计数相同。原整数性对全部
\(T=100\cdot10^n,n\ge0\) 的完整模 \(k\) 轨道，再排除 42,660 个。
余下 25,683 个全部由 \(3\le p\le397,p\ne5\) 的原恢复平方类
及 G07 既约性条件排除。指数类按 F01/F02 的完整周期相容传播；
不是只枚举有限多个 \(m_2\)。

Python 用直接循环轨道代替 C++ 的乘法阶/离散对数恢复，并在每个
剩余标签上重算原恢复多项式。C++ 因式与展开式两套 reader 的覆盖
均为 `476207 / 407864 / 42660 / 25683 / 0`；有符号 128 位中间量
由 \(c=1,k<10100,a<2000,b<1000,A\le8,U=1000\) 界为小于
\(2^{100}\)，UBSan 通过，Python 使用任意精度整数。

因此本明示完整子域为空；未对 \(c>1\) 或更长奇尾外推。
来源：G11 原支持锁接完整周期与独立 reader 的新原方程证书。

<a id="a2-f09"></a>
### A2-F09　一至两位有效数字第二分母的有界长度子域为空

**状态：有限证书。** 全部 A2 且 \(b_2=r10^t\)、
\(1\le r\le99\)、\(10\nmid r\)、\(t\ge0\)，并满足
\(m_2\le26\) 或 \(m_3\le38\)。另一块长度不设额外搜索界。
本项不排除 \(m_2\ge27,m_3\ge39\) 的 G14 余族。

依赖：[A2-G13](#a2-g13)、[A2-G14](#a2-g14)、[A2-G15](#a2-g15)

核对：`a2-decimal-ray-residual`；九个确切奇深素因子，以及
\(E=3\) 的 612 个 gap 整数和独立的 39,999 个原第二分子。
Python 整数无固定位宽；两个 reader 均逐行精确判平方，不用浮点。

G13/G14 已将这个完整范围归约为唯一族
\(m_2=2E+1,m_3=3E,E\ge3\)。所述长度条件任一个成立都强迫
\(3\le E\le12\)。对 \(E=4,\ldots,12\)，下表给出
\(S_E=816\cdot100^E-31\) 的素因子 \(p\equiv3\pmod4\)，且
\(p\mid S_E,p^2\nmid S_E\)，从而被 G15 排除。

| \(E\) | \(p\) | \(E\) | \(p\) | \(E\) | \(p\) |
|---|---|---|---|---|---|
| 4 | 1811 | 5 | 139 | 6 | 19 |
| 7 | 25391 | 8 | 3823 | 9 | 71 |
| 10 | 361617239 | 11 | 7757594443 | 12 | 431 |

这些素数全部由直到整数平方根的试除验证；整除和不被平方整除
由精确模幂核对，不依赖未完成的大整数分解。

剩下 \(E=3,z=1000\) 确实通过 G15 的平方和障碍，例如
\(815999969=7712^2+27505^2\)，所以必须回到原整数恢复。
(A2-ray24-window) 给完整有限窗口

```math
5001\le k\le5612,\qquad 960001\le N\le999999.
```

第一个 reader 把 \(P(N,k,1000)=0\) 看成 \(N\) 的二次式，其判别式为

```math
\mathscr D_k=(2639z^2-124)k^2+14880z^3k-\frac{2214144}{25}z^4.
```

612 个 \(k\) 的判别式均不是整数平方。这里甚至没有预先使用
\(\gcd(k,10)=1\) 或 \(k\equiv1\pmod4\) 来删行。

第二个 reader 独立从原拼接系数出发。对全部 39,999 个 \(N\)，
令 \(C_0=2T+10N,\beta=(T+M)U+b\)，则原 \(a\) 的二次式为

```math
\mathsf A a^2+\mathsf B a+\mathsf C=0,
```

其中

```math
\mathsf A=M^2(\beta^2-b^2),\qquad
\mathsf B=-2M^2b^2 C_0U,\qquad
\mathsf C=\beta^2b^2(4M^2+N^2)-M^2b^2 C_0^2U^2.
```

全部判别式也都不是整数平方，第二次完整排除 \(E=3\)。
因此所述有界长度子域为空；任意剩余两位有效数字候选必须满足
\(E\ge13,m_2\ge27,m_3\ge39\)。这不是对无界指数的枚举结论。

来源：G15 的全参数窗口与奇深素因子障碍，再做明示有限范围的
两个独立变量 reader；\(E\ge13\) 的恢复系统留在 a2-core。


<a id="a2-01"></a>
### A2-01　相邻边界与明确 deep-even 子片

**状态：已严格完成。** 相邻位数边界无条件成立；deep-even 后续在 b1=2、a1∈{5,7,9,11,13} 等明确 chart 假设下使用。

依赖：[A2-G01](#a2-g01)、[A2-G05](#a2-g05)、[C03](#c03)

核对：正文推导；本次重写未为此项另增枚举。

相邻边界及全部 first-block 绝对界已经在 [A2-G01](#a2-g01) 从原式
证明。这里只使用其结论，不再复制该证明。

下面单独进入 b1=2、a1∈{5,7,9,11,13} 的 deep-even 子片。这些是后续
source/endpoint chart 的明确假设。旧基线记录曾称其它 first-block 状态
已排除，但可见入口仅给“ordered Cauchy + 窗口”的摘要。A2-G01 已重新
证明 b1≤2 和 b1=2 的五个 a1；A2-G04–G05 已把 b1=2 且第二分母
二进主导的原候选严格送入以下尾商和 source 形态。b1=1 的排除与
第三分母二进主导仍缺证明，故不把旧摘要重新写成全部 A2 的无条件
deep-even 归约。原声明的状态原样保全，剩余系统列于 RESEARCH.md
的 a2-core。后面的条件化 source 证明只在其明示 chart 中使用。


<a id="a2-01-detail-src-0095-118-1"></a>
#### Deep-even 终端通道

从这里开始仍统一使用全局位数 \(m_2,m_3\)，避免旧稿中 \(M,m\) 的重复记号。

最后危险通道具有

```math
\boxed{
b_2
=
2^{m_2+m_3+t}u,
}
```

```math
\boxed{
b_3
=
2^{m_2+m_3+1}b_{3,0},
}
```

其中

```math
u,\ b_{3,0}
```

均为奇数，且

```math
\boxed{
t\ge3.
}
```

前两分母拼接满足

```math
Q
=
2\cdot10^{m_2}+b_2
=
2^{m_2+1}Q_0,
```

其中

```math
\boxed{
Q_0
=
5^{m_2}
+
2^{m_3+t-1}u.
}
```

第三块正规化尾商被强迫为纯五次幂

```math
\boxed{
L=5^\lambda,
}
```

并且

```math
\boxed{
5^\lambda>2^{m_2+1}.
}
```

将

```math
b_3=\delta_3 b'
```

进一步去二后写成

```math
\boxed{
b'=2^{m_2+1}c.
}
```

于是 \(c\) 为奇数，并处在十倍窗口

```math
\boxed{
\frac{5^\lambda}{10\cdot2^{m_2+1}}
\le c
<
\frac{5^\lambda}{2^{m_2+1}}.
}
```

---

<a id="a2-01-detail-src-0095-118-2"></a>
#### 二进 Hensel 锁

deep-even 通道中的二进抵消深度没有独立自由度，其值由

```math
5^{m_2+\lambda}+c
```

唯一决定：

```math
\boxed{
t
=
1+
v_2(5^{m_2+\lambda}+c).
}
```

因为 \(t\ge3\)，得到

```math
5^{m_2+\lambda}+c
\equiv0\pmod4.
```

而

```math
5^k\equiv1\pmod4,
```

所以

```math
\boxed{
c\equiv3\pmod4.
}
```

于是 \(c\ge3\)，并可把尾商下界加强为

```math
\boxed{
5^\lambda>3\cdot2^{m_2+1}.
}
```

这一结果把二进深度与五进尾商精确耦合起来。

---

<a id="a2-01-detail-src-0095-118-3"></a>
#### \(c=c_Qc_u\) 的来源分解

统一记

```math
\sigma_5=v_5(u).
```

按 \(c\) 的素因子究竟来自前缀 \(Q_0\) 还是来自 \(u\)，存在唯一互素分解

```math
\boxed{
c=c_Qc_u,
}
```

并进一步写成

```math
\boxed{
Q_0
=
5^{\sigma_5}c_Qq_Q,
}
```

```math
\boxed{
u
=
5^{\sigma_5}c_u\rho.
}
```

满足

```math
\gcd(c_Qq_Q,c_u\rho)=1,
```

```math
\gcd(c_Q,c_u)=1,
```

```math
\gcd(c_u,\rho)=1.
```

由二平方局部条件，

```math
p\mid c_u
\Longrightarrow
p\equiv1\pmod4.
```

因此

```math
c_u\equiv1\pmod4.
```

结合

```math
c\equiv3\pmod4
```

得到

```math
\boxed{
c_Q\equiv3\pmod4.
}
```

这一步把原先混杂的“尾分母素数”分成两个来源完全不同的算术库：

- \(c_Q\)：来自 denominator-prefix；
- \(c_u\)：来自 source \(u\)，且只含 \(1\bmod4\) 奇素数。

---

<a id="a2-01-detail-src-0095-118-4"></a>
#### 五进统一参数与三条通道

定义

```math
\boxed{
E_5=\lambda+\sigma_5.
}
```

为了描述 \(5\)-进同步，统一使用

```math
d_5=m_3-E_5,
```

```math
r_5=2E_5-m_3,
```

```math
\nu_5=3E_5-2m_3.
```

满足

```math
2d_5+\nu_5=E_5,
```

```math
r_5+d_5=E_5,
```

```math
E_5+\nu_5=2r_5.
```

合法候选只能处于三条五进通道：

<a id="a2-01-detail-src-0095-118-5"></a>
#### 通道 I：\(\sigma_5>0\)

```math
\boxed{
m_3=\frac32E_5,
}
```

并且 \(E_5\) 必须为偶数。

<a id="a2-01-detail-src-0095-118-6"></a>
#### 通道 II：reflection

```math
\sigma_5=0,
\qquad
\lambda<m_3\le\frac32\lambda.
```

此时

```math
\boxed{
\nu_5=3\lambda-2m_3.
}
```

<a id="a2-01-detail-src-0095-118-7"></a>
#### 通道 III：balance

```math
\sigma_5=0,
\qquad
\lambda=m_3.
```

该支中 \(5\)-进范数至少达到尾长深度，并存在更细的 gap 分类。

这三条通道说明 \(m_3,\lambda,v_5(u)\) 不能独立增长。

---

<a id="a2-01-detail-src-0095-118-8"></a>
#### Hensel 商与 \(\rho\) 的恢复

定义

```math
\boxed{
f=5^{E_5}q_Q+2c_u.
}
```

存在奇整数 \(\omega,\theta\) 使

```math
\boxed{
5^{E_5}q_Q+c_u
=
2^{t-1}\rho\omega,
}
```

```math
\boxed{
5^{m_2+\lambda}+c
=
2^{t-1}\rho\theta.
}
```

二式相减整理得到

```math
\boxed{
c_Q\omega-\theta
=
2^{m_3}5^{E_5}c_u.
}
```

并且

```math
\boxed{
\gcd(\omega,\theta)=1.
}
```

于是

```math
\boxed{
2^{t-1}\rho
=
\gcd(
5^{E_5}q_Q+c_u,\,
5^{m_2+\lambda}+c
).
}
```

因此

```math
\boxed{
\rho
=
\frac{
\gcd(
5^{E_5}q_Q+c_u,\,
5^{m_2+\lambda}+c
)
}{
2^{t-1}
}.
}
```

也就是说 \(\rho\) 同样失去了独立自由度。

---

<a id="a2-01-detail-src-0095-118-9"></a>
#### 完全去二的平方判别式

定义

```math
A_0=a_1 10^{m_2-1},
\qquad
P=A_0+a_2,
```

以及

```math
C_0=\frac{a_1b_2}{2}.
```

定义 deep-even 前两块奇范数

```math
\boxed{
\mathcal N_0=C_0^2+a_2^2.
}
```

它与全局 \(\mathcal N_{12}\) 的关系是

```math
\mathcal N_{12}=4\mathcal N_0
```

因为此时 \(b_1=2\)。

定义

```math
K_0
=
25\cdot2^{2(m_3+t)}u^2P^2
-
Q_0^2\mathcal N_0.
```

判别平方可写成

```math
\boxed{
5^\lambda
\left(
5^\lambda K_0
-
2cQ_0\mathcal N_0
\right)
=
Z^2.
}
```

再令

```math
\boxed{
\mathcal A
=
5^{\lambda+1}2^{m_3+t}uP,
}
```

则完全等价于差平方系统

```math
\boxed{
\mathcal A^2-Z^2
=
5^\lambda Q_0\mathcal N_0
\left(
5^\lambda Q_0+2c
\right).
}
```

所以存在正奇数因子 \(U_-,U_+\) 满足

```math
\boxed{
U_-U_+
=
5^\lambda Q_0\mathcal N_0
(5^\lambda Q_0+2c),
}
```

```math
\boxed{
U_-+U_+
=
2\mathcal A.
}
```

这把 \(A_2\) 的无界问题从混合二进/五进/高斯结构压成了一个纯奇数的“乘积已知 + 和已知”的差平方因子分配问题。

---

<a id="a2-01-detail-src-0095-118-10"></a>
#### 实数十进制窗口

定义

```math
x=\frac{b_2}{10^{m_2}},
\qquad
y=\frac{a_2}{10^{m_2-1}},
\qquad
w=\frac{b_3}{10^{m_3}}.
```

已经得到 core-specific 的严格窗口：

```math
\boxed{
\begin{array}{c|c}
a_1&x\\ \hline
5&27/250<x<3/16\\
7&1/10\le x<7/40\\
9&1/10\le x<3/20\\
11&1/10\le x<1/8\\
13&1/10\le x<11/100
\end{array}
}
```

第二分子被压在其十进制区间顶部：

```math
\boxed{
\begin{array}{c|c}
a_1&y\\ \hline
5&y>0.93\\
7&y>0.84\\
9&y>0.83\\
11&y>0.88\\
13&y>0.95
\end{array}
}
```

第三分母被压在其位数区间顶部：

```math
\boxed{
\begin{array}{c|c}
a_1&w\\ \hline
5&w>20/21\\
7&w>7/8\\
9&w>5/6\\
11&w>5/6\\
13&w>10/11
\end{array}
}
```

而第三分子则被压在其位数区间底部。

这种“第二分子接近上端、第二分母接近下端、第三分母接近上端、第三分子接近下端”的反向挤压，是 \(A_2\) 终端系统中非常重要的实几何刚性。

---

<a id="a2-01-detail-src-0095-118-11"></a>
#### \(A_2\) 的 factor allocation

对差平方两因子做最简分母恢复后，可写

```math
U_-=f\xi,
\qquad
U_+=q_Q\upsilon,
```

并有

```math
\boxed{
\xi\upsilon
=
5^{E_5}c_Q^2\mathcal N_0.
}
```

同时

```math
\boxed{
\upsilon-5^{E_5}\xi
=
2^t5^{2E_5-m_3}\rho a_3.
}
```

若

```math
p^e\Vert c_Q,
```

则该完整素数幂不能分散到两边，必须全部进入 \(\xi\) 或全部进入 \(\upsilon\)。

因此存在唯一互素分解

```math
\boxed{
c_Q=c_-c_+,
\qquad
\gcd(c_-,c_+)=1,
}
```

使去掉共同五进部分后

```math
\boxed{
\xi=c_-^2X,
\qquad
\upsilon=c_+^2Y.
}
```

这叫做 \(c_Q\) 的 square-side allocation。

同类分析也可以对 \(\rho\) 做平方单边分配。

于是原本每个素数幂都有很多组合方式的 factor allocation，被压缩为每个完整 prime power 的二元选择。

---

<a id="a2-01-detail-src-0095-118-12"></a>
#### \(A_2\) 的 Gaussian rectangle 与 prefix defect

这一阶段的目的，是进一步研究差平方终端式中必然出现的 \(3\bmod4\) 奇素数。

定义 source-side 量

```math
U_5=5^{m_2-\sigma_5},
```

以及

```math
D_0=2^{m_3+t-1}\rho,
```

```math
H_s=D_0c_u.
```

由 source split 有

```math
\boxed{
c_Qq_Q=U_5+H_s.
}
```

固定十进制斜率满足

```math
\boxed{
U_5C_0=10H_sA_0.
}
```

定义正交误差

```math
\boxed{
L_0
=
U_5a_2-10H_sC_0.
}
```

实数窗口可以严格证明

```math
\boxed{
L_0<0.
}
```

同时

```math
\boxed{
\gcd(L_0,a_2)
=
\gcd(a_2,5a_1).
}
```

所以能够同时进入 \(L_0\) 与 \(a_2\) 的 \(3\bmod4\) 素数只能来自固定 core 的小素数。

再定义

```math
M_0=U_5C_0+10H_sa_2.
```

由固定斜率，

```math
\boxed{
M_0=10H_sP.
}
```

于是有 Gaussian 乘法恒等式

```math
\boxed{
L_0+iM_0
=
(U_5+10iH_s)(a_2+iC_0).
}
```

因此

```math
\boxed{
L_0^2+M_0^2
=
(U_5^2+100H_s^2)\mathcal N_0.
}
```

这一结构把“十进制固定斜率”直接嵌入高斯整数乘法。

---

<a id="a2-01-detail-src-0095-118-13"></a>
#### Prefix defect

定义

```math
\boxed{
\Delta_{\rm pref}
=
A_0^2+C_0^2-P^2.
}
```

展开为

```math
\Delta_{\rm pref}
=
C_0^2-2A_0a_2-a_2^2.
```

这是纯粹由第一、第二块决定的整数。

第二层 surplus \(E_1\) 可以精确写成

```math
\boxed{
E_1
=
R_*\Delta_{\rm pref}
+
\Sigma a_2^2,
}
```

其中

```math
R_*=100\,5^{E_5}H_s^2
```

而 \(\Sigma\) 是 denominator/source 乘积因子。

关键 gcd 关系是

```math
\boxed{
\gcd(q_Qf,E_1)
=
\gcd(q_Qf,\Delta_{\rm pref}).
}
```

这意味着所有 denominator-side 对 \(E_1\) 的接触，都被同一个纯前缀整数 \(\Delta_{\rm pref}\) 控制。

还得到

```math
\boxed{
\Delta_{\rm pref}\equiv7\pmod8.
}
```

对

```math
a_1=9,11,13
```

可以进一步证明

```math
\boxed{
\Delta_{\rm pref}>0.
}
```

---

<a id="a2-01-detail-src-0095-118-14"></a>
#### Odd inert excess

第二层结构给出

```math
E_1\equiv3\pmod4.
```

另一方面，相关 source norm 与 \(\mathcal N_0\) 中 \(3\bmod4\) 素数的赋值受到二平方和奇偶约束。

因此必然存在某个

```math
p\equiv3\pmod4
```

使第二层产生一个正奇数的“额外赋值”。

统一称其为

```math
\boxed{
\text{odd inert excess}.
}
```

这里描述的是一类机制，并不指定某个固定素数：某个 inert prime 在第二层乘积中比基础二平方赋值多出奇数深度。

当前分析把它分成三类来源：

<a id="a2-01-detail-src-0095-118-15"></a>
#### I. Denominator-prefix excess

```math
p\mid q_Qf.
```

这类接触完全受

```math
\Delta_{\rm pref}
```

控制。

<a id="a2-01-detail-src-0095-118-16"></a>
#### II. Source excess

```math
p\mid \mathfrak n
```

其中 \(\mathfrak n\) 是 source-side 二平方尺度。

这类 prime 与 denominator 已经证明完全分离：

```math
p\nmid q_Qfc_Qu_0.
```

它们的 odd excess 只能通过一种高阶 Hensel 角接触产生。

<a id="a2-01-detail-src-0095-118-17"></a>
#### III. Spontaneous angle excess

```math
p\nmid \mathfrak n q_Qf\mathcal N_0,
\qquad
p\mid E_1.
```

这类 prime 原先不属于 source 或 denominator，只在第二层角度条件中自发出现，目前最难统一排除。

---

<a id="a2-01-detail-src-0095-118-18"></a>
#### \(A_2\) 的 source 双 Hensel 系统

对 source inert prime，可以把原来的复杂二次表达式线性化。

定义

```math
L_+=5^{E_5}D_0+c_Q,
```

```math
L_-=99\,5^{E_5}D_0-2c_Q.
```

source 参数 \(\sigma\) 满足

```math
\boxed{
2\sigma
=
c_uD_0L_-
-
2U_5L_+.
}
```

因此 \(\sigma\) 对纯五次幂

```math
U_5=5^{m_2-\sigma_5}
```

是线性的。

若

```math
p^{2h}\Vert\sigma,
\qquad
p\equiv3\pmod4,
```

则 \(U_5\) 必须以精确深度 \(2h\) 贴近一个显式有理 Hensel 根。

为了与十进制窗口结合，引入归一化变量

```math
x=\frac{b_2}{10^{m_2}},
\qquad
y=\frac{a_2}{10^{m_2-1}},
```

以及一个 source-normalized 变量

```math
z=\frac{5^{E_5}D_0}{c_Q}.
```

其实际实数意义可化为

```math
z=\frac{b_2}{w},
```

而 \(w=b_3/10^{m_3}\) 已经被压在接近 \(1\) 的窄窗口中。

定义第一个 Hensel 多项式

```math
\boxed{
\Phi(x,z)
=
(99x-4)z-2x-4.
}
```

若

```math
p^{2h}\Vert\sigma,
```

则

```math
\boxed{
v_p(\Phi(x,z))=2h.
}
```

于是

```math
z
\equiv
\frac{2x+4}{99x-4}
\pmod{p^{2h}}.
```

再定义第二个 Hensel 多项式

```math
\boxed{
\Psi_{a_1}(y,z)
=
400a_1(z+1)^2
-y(99z-2)^2.
}
```

source odd excess 若存在，还必须满足

```math
\boxed{
v_p(\Psi_{a_1}(y,z))\ge h.
}
```

因此 source odd excess 被压缩为非常特殊的

```math
\boxed{
2h:h
}
```

双 Hensel 接触：

```math
\boxed{
v_p(\Phi)=2h,
\qquad
v_p(\Psi_{a_1})\ge h.
}
```

而 \(x,y,z\) 同时受到窄十进制实数窗口约束。

这已经远强于普通的 Legendre/Jacobi 二次剩余条件。

---


来源：`SRC-0095:118–1141`。原文保全，当前论证以本节为准。

<a id="a2-02"></a>
### A2-02　实数 phase、prefix defect 与真实余数窗

**状态：已严格完成。** deep-even 的既有参数 chart；保留真实 coefficient plane。

依赖：[A2-01](#a2-01)

核对：正文推导；本次重写未为此项另增枚举。

<a id="a2-02-detail-src-0115-26-1"></a>
#### 记号

沿用 terminal A2：

```math
M=m_2,\qquad m=m_3,\qquad a=a_1\in\{5,7,9,11,13\},
```

```math
x=\frac{b_2}{10^M},\qquad y=\frac{a_2}{10^{M-1}},\qquad w=\frac{b_3}{10^m}.
```

source split：

```math
U=5^{M-\sigma_5},\quad D_0=2^{m+t-1}\rho,\quad H_s=D_0c_u,
```

```math
c_Qq=U+H_s,\qquad Ux=2H_s.
```

定义

```math
E=E_5,\qquad z=\frac{5^ED_0}{c_Q},
```

```math
\Phi(x,z)=(99x-4)z-2x-4,
```

```math
f=5^Eq+2c_u,\qquad \Sigma=c_Q^2qf,
```

以及 source norm scale

```math
n=2c_u\sigma.
```

canonical discriminant / Gaussian companion 使用

```math
A=10H_s5^dP,
```

```math
A^2-T^2=\Sigma\mathcal N,
\qquad
T^2+J^2=n\mathcal N.
```

同时

```math
J=-5^dL_0>0,
\qquad
L_0=-U10^{M-1}(25ax^2-y).
```

---

<a id="a2-02-detail-src-0115-26-2"></a>
#### `已严格完成`：第三块实尺度给出精确的 source normalized `z`

由 deep-even 第三分母正规形

```math
b_3=2^{m+M+1}5^{m-\lambda}c,
\qquad c=c_Qc_u,
```

有

```math
w=\frac{b_3}{10^m}
=\frac{2^{M+1}c_Qc_u}{5^\lambda}.
```

另一方面

```math
D_0=\frac{Ux}{2c_u}=\frac{5^{M-\sigma_5}x}{2c_u}.
```

因此

```math
\begin{aligned}
z
&=\frac{5^{\lambda+\sigma_5}D_0}{c_Q}\\
&=\frac{5^{M+\lambda}x}{2c_uc_Q}\\
&=\frac{10^M x}{w}.
\end{aligned}
```

即

```math
\boxed{z=\frac{10^Mx}{w}=\frac{b_2}{w}.}
```

所以 \(z\) 不是新的无界自由尺度；一旦 \((M,b_2,b_3)\) 固定，它由真实十进制 phase 精确确定。

---

<a id="a2-02-detail-src-0115-26-3"></a>
#### `已严格完成`：`n/Sigma` 的完全尺度消去

由前一研究文件的精确恒等式

```math
4\sigma=Uc_Q\Phi(x,z)
```

以及

```math
c_u=\frac{Ux}{2D_0}
```

得到

```math
n=2c_u\sigma
=\frac{U^2xc_Q}{4D_0}\Phi(x,z).
```

另一方面

```math
q=\frac{U(x+2)}{2c_Q}.
```

又

```math
\begin{aligned}
f
&=5^Eq+2c_u\\
&=\frac{U}{2D_0}\left(z(x+2)+2x\right).
\end{aligned}
```

因此

```math
\Sigma=c_Q^2qf
=\frac{c_QU^2}{4D_0}(x+2)\left(z(x+2)+2x\right).
```

两式相除：

```math
\boxed{
\frac n\Sigma
=
\frac{x\Phi(x,z)}{(x+2)(z(x+2)+2x)}.
}
\tag{3.1}
```

所有 \(U,D_0,c_Q,c_u,q,f\) 尺度全部消失。

再用恒等式

```math
x\Phi(x,z)+(x+2)(z(x+2)+2x)
=4z(25x^2+1),
```

可把 (3.1) 写成

```math
\boxed{
\frac n\Sigma
=
\frac{x(99x-4)}{(x+2)^2}
-
\frac{8x(25x^2+1)}{(x+2)^2\bigl(z(x+2)+2x\bigr)}.
}
\tag{3.2}
```

因 terminal window 中 \(x>0,z>0\)，第二项严格为正。故

```math
\boxed{
0<\frac n\Sigma
<r_0(x):=\frac{x(99x-4)}{(x+2)^2}.
}
\tag{3.3}
```

这里正性来自 \(n,\Sigma>0\)。特别地，它还重新推出

```math
\Phi(x,z)>0.
```

由于 \(z=10^Mx/w\)，(3.2) 的误差是显式 \(O(10^{-M})\)；也就是说 source/denominator 比例被真实第二块十进制 phase 指数级贴近于单变量曲线 \(r_0(x)\)。

---

<a id="a2-02-detail-src-0115-26-4"></a>
#### `已严格完成`：Gaussian angle 完全进入 `(x,y)` 窗口

由

```math
J=-5^dL_0
=5^dU10^{M-1}(25ax^2-y)
```

和

```math
A=10H_s5^dP,
\qquad H_s=\frac{Ux}{2},
\qquad P=10^{M-1}(a+y),
```

得到精确无尺度比值

```math
\boxed{
\frac JA
=\frac{25ax^2-y}{5x(a+y)}.
}
\tag{4.1}
```

记

```math
r=\frac n\Sigma,\qquad
\tau=\frac TA,\qquad
\jmath=\frac JA.
```

由

```math
T^2+J^2=n\mathcal N,
\qquad
A^2-T^2=\Sigma\mathcal N
```

相除得到

```math
r=\frac{\tau^2+\jmath^2}{1-\tau^2},
```

从而

```math
\boxed{
\tau^2=\frac{r-\jmath^2}{1+r}.
}
\tag{4.2}
```

结合 \(r<r_0(x)\)，并注意右端关于 \(r\) 严格递增，得到

```math
\boxed{
\left(\frac TA\right)^2
<
H_a(x,y)
:=
\frac{r_0(x)-\left(\frac{25ax^2-y}{5x(a+y)}\right)^2}
{1+r_0(x)}.
}
\tag{4.3}
```

在全部合法 core window 中已有 \(25ax^2-y>0\)。直接求导可见

```math
\frac{\partial}{\partial y}
\frac{25ax^2-y}{5x(a+y)}
<0,
```

故 \(H_a(x,y)\) 关于 \(y\) 递增。由于 \(y<1\)，

```math
H_a(x,y)<H_a(x,1).
```

而后者惊人地化成

```math
\boxed{
H_a(x,1)
=-\frac{
25a^2x^4+100a^2x^3-(200a+99)x^2+4x+4
}{100x^2(a+1)^2}.
}
\tag{4.4}
```

并有

```math
\boxed{
\frac{d}{dx}H_a(x,1)
=-\frac{(x+2)(25a^2x^3-2)}{50x^3(a+1)^2}.
}
\tag{4.5}
```

因此每个 core 的最大值只有一个可能内临界点；不存在复杂的二维连续优化。

---

<a id="a2-02-detail-src-0115-26-5"></a>
#### `已严格完成`：五个 core 的显式 angle cap

在 `core.md` 的严格实窗口上，(4.4)–(4.5) 给出：

```math
\boxed{
\begin{array}{c|c}
a&T/A\\ \hline
5&<3/8\\
7&<31/100\\
9&<13/50\\
11&<21/100\\
13&<1/6
\end{array}}
\tag{5.1}
```

说明：对 \(a=5,7\)，唯一临界点由 \(25a^2x^3=2\) 给出；对 \(a=9,11,13\)，该临界点已经落在合法 \(x\)-窗口左侧，所以最大值在 \(x=1/10\) 端点。附带 checker 使用精确有理 Sturm root count 验证对应阈值多项式在整个闭区间无零点且为正，因此 (5.1) 不依赖浮点数。

---

<a id="a2-02-detail-src-0115-26-6"></a>
#### `已严格完成`：Gaussian divisor 必须处于窄乘法窗

canonical mixed signs 给出

```math
fZ=A-T,
\qquad
qW=A+T.
```

因此

```math
\frac{fZ}{qW}=\frac{1-T/A}{1+T/A}.
```

由 (5.1) 得到严格下界：

```math
\boxed{
\begin{array}{c|c}
a&\displaystyle \frac{fZ}{qW}\\ \hline
5&>5/11\\
7&>69/131\\
9&>37/63\\
11&>79/121\\
13&>5/7
\end{array}}
\tag{6.1}
```

同时 \(T>0\) 给出

```math
\frac{fZ}{qW}<1.
```

也就是说合法 Gaussian allocation 不允许两个 mixed-sign 因子发生任意大的乘法失衡。特别是高 core 越大，窗口越窄：\(a=13\) 时

```math
\boxed{
\frac57<\frac{fZ}{qW}<1.
}
```

若再代入

```math
Z=c_-^2X,\qquad W=c_+^2Y,\qquad XY=\mathcal N,
```

则每一种 \(c_Q=c_-c_+\) 的平方单边 allocation 都必须满足

```math
\boxed{
\eta_a
<
\frac{f c_-^2X}{q c_+^2Y}
<1,
}
\tag{6.2}
```

其中 \(\eta_a\) 为 (6.1) 左栏对应常数。

这正是后续把连续 ellipse 与离散 \(c_Q\)-allocation、\(q/f\) singular lift、2/5-adic phase 联立所需的 multiplicative window。

---

<a id="a2-02-detail-src-0115-26-7"></a>
#### 证明边界

本节严格完成的是：

1. \(z\) 与真实 decimal phase 的精确恢复；
2. \(n/\Sigma\) 的完全 scale-free 化；
3. \(J/A\) 的完全 scale-free 化；
4. 五个 core 的显式 \(T/A\) 上界；
5. 因而得到 Gaussian mixed-sign factors 的 core-dependent 窄乘法窗。

这些结论排除了“Gaussian divisor 可以任意失衡”的剩余自由度，但尚未单独证明所有离散 allocation 均不落入 (6.2)。下一步必须把 (6.2) 与已有的平方单边 allocation、finite defect / CRT 唯一代表直接联立；继续单独追 source prime 不会增加约束。

---

<a id="a2-02-detail-src-0115-26-8"></a>
#### `A_2` ellipse-to-defect remainder window


> 分支：`agent/a2-hensel-resultant-progress`
> 状态：**严格结构推进；连续 canonical ellipse 已直接限制 finite-defect 余量。**
> 依赖：[`phase-and-defect.md`](#a2-02) 与旧 terminal factor / finite-defect 正规形。

本文把 canonical signed-square angle 的新实数窄窗与旧 finite-defect

```math
c_-^2X=kD+R,\qquad 0<R<D
```

直接联立。所得结论第一次把连续 ellipse 约束变成 \(R/D\) 的显式下界。

---

<a id="a2-02-detail-src-0115-26-9"></a>
#### 两套第三坐标因子的精确对应

terminal factor system 有

```math
H_0-Y_3=5^E c_-^2X,
\qquad
H_0+Y_3=c_+^2Y.
\tag{1.1}
```

finite-defect 记号满足

```math
5^ED=g10^m,
\qquad
J_{\rm def}:=\frac{c_-^2X}{D}=k+\frac RD.
\tag{1.2}
```

于是

```math
H_0-Y_3=g10^mJ_{\rm def}.
```

旧 k-free 恒等式又给出

```math
H_0=g(a_3+10^mJ_{\rm def}),
```

故

```math
\boxed{
\frac{H_0-Y_3}{H_0+Y_3}
=
\frac{J_{\rm def}}{J_{\rm def}+2\zeta},
\qquad
\zeta:=\frac{a_3}{10^m}.
}
\tag{1.3}
```

真实第三分子窗口给出

```math
1<\zeta<
\begin{cases}
21/20,&a=5,\\
8/7,&a=7,\\
6/5,&a=9,11,\\
11/10,&a=13.
\end{cases}
\tag{1.4}
```

其中左端严格：若 \(a_3=10^m\)，则 \(a_3\) 为偶数，而 terminal deep-even 的 \(b_3\) 也是偶数，违背 \(\gcd(a_3,b_3)=1\)。

---

<a id="a2-02-detail-src-0115-26-10"></a>
#### Canonical mixed-sign ratio 与 sphere ratio 的校正因子

canonical discriminant factorization 写成

```math
fZ=A-T,
\qquad
qW=A+T,
```

且

```math
Z=c_-^2X,
\qquad
W=c_+^2Y.
```

所以

```math
\frac{fZ}{qW}
=
\frac{f}{5^Eq}
\frac{H_0-Y_3}{H_0+Y_3}.
\tag{2.1}
```

这里不能把两种 ratio 直接认成同一个量；差别正是 \(f/(5^Eq)\)。

由 source normalization

```math
q=\frac{U(x+2)}{2c_Q},
```

```math
f=\frac{U}{2D_0}\bigl(z(x+2)+2x\bigr),
```

以及

```math
z=\frac{10^Mx}{w},
```

得到

```math
\boxed{
\vartheta:=\frac{5^Eq}{f}
=
\frac{z(x+2)}{z(x+2)+2x}
=
\frac{10^M(x+2)}{10^M(x+2)+2w}.
}
\tag{2.2}
```

因为 \(x>0\) 且 \(0<w<1\)，

```math
\boxed{
\vartheta>
rac{10^M}{10^M+1}.
}
\tag{2.3}
```

在当前开放范围 \(M\ge11\) 中统一有

```math
\boxed{
\vartheta>
artheta_{11}:=
rac{10^{11}}{10^{11}+1}.
}
\tag{2.4}
```

这说明 canonical ratio 到 sphere ratio 的校正只有十进制指数级小量。

---

<a id="a2-02-detail-src-0115-26-11"></a>
#### `已严格完成`：finite-defect 商的 core-dependent 下界

前一文件得到

```math
\frac{fZ}{qW}>\eta_a,
```

其中

```math
\eta_5=\frac5{11},\qquad
\eta_7=\frac{69}{131},\qquad
\eta_9=\frac{37}{63},\qquad
\eta_{11}=\frac{79}{121},\qquad
\eta_{13}=\frac57.
\tag{3.1}
```

由 (2.1)–(2.4)，

```math
\frac{H_0-Y_3}{H_0+Y_3}
>\eta_a\vartheta_{11}.
```

再代入 (1.3)，得到

```math
\boxed{
J_{\rm def}
>
\frac{2\eta_a\vartheta_{11}}
{1-\eta_a\vartheta_{11}}\,\zeta.
}
\tag{3.2}
```

因为 \(\zeta>1\)，可去掉第三分子的连续参数：

```math
\boxed{
J_{\rm def}>C_a,
}
\tag{3.3}
```

其中精确常数为

```math
\begin{array}{c|c|c}
a&C_a&\text{数值}\ \hline
5&\dfrac{10^{12}}{600000000011}&1.666666666636\ldots\\[2mm]
7&\dfrac{600000000000}{269565217397}&2.225806451565\ldots\\[2mm]
9&\dfrac{7400000000000}{2600000000063}&2.846153846084\ldots\\[2mm]
11&\dfrac{15800000000000}{4200000000121}&3.761904761796\ldots\\[2mm]
13&\dfrac{10^{12}}{200000000007}&4.999999999825\ldots
\end{array}
\tag{3.4}
```

---

<a id="a2-02-detail-src-0115-26-12"></a>
#### `已严格完成`：七个 defect 状态中的四个获得真余量下界

由于

```math
J_{\rm def}=k+\frac RD,
\qquad 0<\frac RD<1,
```

旧 defect 状态为

```math
k\in
\begin{cases}
\{1\},&a=5,\\
\{2\},&a=7,\\
\{2,3\},&a=9,\\
\{3,4\},&a=11,\\
\{5\},&a=13.
\end{cases}
```

(3.3) 对低商状态给出：

```math
\boxed{
\begin{array}{c|c|c}
a&k& R/D\ \hline
5&1&>33/50\\
7&2&>11/50\\
9&2&>21/25\\
11&3&>19/25
\end{array}}
\tag{4.1}
```

这些是故意取弱后的干净有理界；均严格弱于 (3.4) 的精确值，因此无需浮点判断。

特别是两个此前仍有整段 \((0,D)\) 自由度的状态被压到顶端薄层：

```math
\boxed{
a=9,\ k=2\Longrightarrow \frac RD>\frac{21}{25},}
```

```math
\boxed{
a=11,\ k=3\Longrightarrow \frac RD>\frac{19}{25}.}
```

也就是说相应 CRT 唯一代表若存在，只能落在区间最后的 \(16\%\) 或 \(24\%\)。

对 \((a,k)=(9,3),(11,4),(13,5)\)，当前 lower angle cap 尚不足以超过商的整数基线，因此本节不宣称新余量下界。

---

<a id="a2-02-detail-src-0115-26-13"></a>
#### 与统一平方深度 CRT 的直接组合

固定 core、\(k\)、二进相位以及 \(c_Q,\rho\) 的平方单边分配后，已有统一模数

```math
\mathfrak L
=2^{2t-1}c_u\rho^2\operatorname{lcm}(q,c_Q^2),
```

使 \(R\) 落在模 \(\mathfrak L\) 的至多一个兼容类。

在平衡支已有 \(\mathfrak L>D\)，所以 \(0<R<D\) 中至多一个代表。现在 (4.1) 进一步要求这个唯一代表还必须落在

```math
\left(\frac{33}{50}D,D\right),
\quad
\left(\frac{11}{50}D,D\right),
\quad
\left(\frac{21}{25}D,D\right),
\quad
\left(\frac{19}{25}D,D\right)
```

之一（依 core / defect 而定）。

研究目标见 [路线记录](RESEARCH.md)。

---

<a id="a2-02-detail-src-0115-26-14"></a>
#### 当前证明边界

本文新增的是严格的 bridge

```math
\boxed{
\text{decimal ellipse angle}
\Longrightarrow
\text{sphere distance ratio}
\Longrightarrow
J_{\rm def}=k+R/D
\Longrightarrow
\text{CRT remainder interval}.
}
```

它没有单独关闭全部 A2，但已把连续几何约束真正送入最后的离散 CRT representative，而不是停留在独立的实数估计。

---


来源：`SRC-0115:26–776`。原文保全，当前论证以本节为准。

<a id="a2-03"></a>
### A2-03　端点整数、high/low m 与首个有限 slot

**状态：已严格完成。** 明确 finite-defect 状态；high-2 allocation 中线排除及相对长度约束。

依赖：[A2-02](#a2-02)

核对：正文推导；本次重写未为此项另增枚举。

<a id="a2-03-detail-src-0099-9-1"></a>
#### 记号与 finite-defect 补余量

沿用 terminal A2：

```math
M=m_2,\qquad m=m_3,\qquad a=a_1\in\{5,7,9,11,13\},
```

```math
x=\frac{b_2}{10^M},\qquad y=\frac{a_2}{10^{M-1}},\qquad
w=\frac{b_3}{10^m},\qquad \zeta=\frac{a_3}{10^m}.
```

记 exact lift 的值为

```math
\mathcal R=\frac{a+y+10^{-M}\zeta}{2+x+10^{-M}w}.
```

旧 finite-defect 正规形写成

```math
c_-^2X=kD+R,\qquad 0<R<D,
```

并定义

```math
J_{\rm def}:=\frac{c_-^2X}{D}=k+\frac RD.
```

本轮对低商状态更方便的变量是顶部补余量

```math
\boxed{C:=D-R},\qquad 0<C<D,
```

以及

```math
j:=k+1,\qquad J_{\rm def}=j-\frac CD.
```

---

<a id="a2-03-detail-src-0099-9-2"></a>
#### 第一部分：纯十进制 endpoint shell

<a id="a2-03-detail-src-0099-9-3"></a>
#### `已严格完成`：`J_def` 的直接十进制恢复

第三坐标为

```math
r_3=\frac\zeta w.
```

由旧 third-distance ratio 与拼接式直接消元，可得到

```math
\boxed{
J_{\rm def}=w(\mathcal R-r_3).
}
\tag{2.1}
```

把拼接式代入，亦即

```math
\boxed{
J_{\rm def}
=\frac{w(a+y)-(2+x)\zeta}{2+x+10^{-M}w}.
}
\tag{2.2}
```

这一步把 finite-defect 商从 factor-allocation 对象恢复成真实十进制变量。

另一方面球面关系为

```math
\mathcal R^2
=\frac{a^2}{4}+\frac{y^2}{100x^2}+\frac{\zeta^2}{w^2}.
```

令

```math
S_a(x,y):=\frac{a^2}{4}+\frac{y^2}{100x^2}.
```

由 \(w\mathcal R=J_{\rm def}+\zeta\) 得到精确 shell：

```math
\boxed{
J_{\rm def}(J_{\rm def}+2\zeta)
=w^2S_a(x,y).
}
\tag{2.3}
```

因此 finite-defect 的整数带编号，本质上是一个纯四变量球面壳层条件。

---

<a id="a2-03-detail-src-0099-9-4"></a>
#### `已严格完成`：消去 `w,zeta,M` 后的纯前缀 barrier

由拼接式和 (2.1)，

```math
(2+x)\mathcal R+10^{-M}J_{\rm def}=a+y.
```

定义

```math
q_*:=1+\frac{J_{\rm def}}\zeta.
```

因为 \(\zeta/w=\mathcal R/q_*\)，球面式化为

```math
\boxed{
(2+x)^2S_a(x,y)q_*^2
=
(a+y-10^{-M}J_{\rm def})^2(q_*^2-1).
}
\tag{3.1}
```

由于右边系数满足

```math
0<a+y-10^{-M}J_{\rm def}<a+y,
```

可定义

```math
\boxed{
q_0(x,y):=
\frac{a+y}{
\sqrt{(a+y)^2-(2+x)^2S_a(x,y)}}
}
\tag{3.2}
```

并严格得到

```math
\boxed{q_*>q_0(x,y).}
\tag{3.3}
```

若 defect 商为 \(k\)，则

```math
J_{\rm def}<k+1,\qquad \zeta>1,
```

故

```math
q_*<k+2.
```

于是得到纯前缀必要条件

```math
\boxed{q_0(x,y)<k+2.}
\tag{3.4}
```

同时

```math
J_{\rm def}=\zeta(q_*-1)>q_0(x,y)-1,
```

所以

```math
\boxed{
\frac RD>q_0(x,y)-(k+1).
}
\tag{3.5}
```

这比仅通过 canonical angle 间接限制 \(R/D\) 更直接。

---

<a id="a2-03-detail-src-0099-9-5"></a>
#### `已严格完成`：七个 finite-defect 状态全部进入固定余量带

把 (3.5) 与既有 core window 联立，再用 (2.3) 的粗上界，得到：

```math
\boxed{
\begin{array}{c|c|c}
a&k&R/D\\ \hline
5&1&\dfrac23<R/D<\dfrac{17}{20}\\[1mm]
7&2&\dfrac{31}{100}<R/D<\dfrac{31}{40}\\[1mm]
9&2&\dfrac{247}{250}<R/D<1\\[1mm]
9&3&0<R/D<\dfrac{18}{25}\\[1mm]
11&3&\dfrac{103}{125}<R/D<1\\[1mm]
11&4&0<R/D<\dfrac{17}{25}\\[1mm]
13&5&\dfrac9{100}<R/D<\dfrac{33}{50}
\end{array}}
\tag{4.1}
```

其中 `a=5,7` 的新 lower bound 用精确 Sturm root count 验证 `q0(x,1)` 在完整 core interval 上分别严格大于 `8/3` 与 `331/100`；`a=9,11,13` 则在左端点直接得到

```math
q_0(1/10,1)^2=
\frac{8000}{503},\quad
\frac{256}{11},\quad
\frac{1600}{43}.
```

上界只用

```math
J_{\rm def}<\sqrt{1+S_a(x,y)}-1
```

与已有 digit window。

因此旧的七个 `k` 状态不再对应整个 `(0,D)`，而都落在固定的 remainder band 中。

---

<a id="a2-03-detail-src-0099-9-6"></a>
#### 第二部分：最危险 `(a,k)=(9,2)` 的 endpoint core

<a id="a2-03-detail-src-0099-9-7"></a>
#### `已严格完成`：`x,y,zeta,w,C` 同时进入端点薄层

从此固定

```math
\boxed{a=9,\qquad k=2,\qquad j=3.}
```

由 (4.1)，

```math
\boxed{0<C<\frac3{250}D.}
\tag{5.1}
```

又因 `q0<4`，而在该 core 中

```math
\frac{\partial}{\partial x}\frac1{q_0^2}<0,
\qquad
\frac{\partial}{\partial y}\frac1{q_0^2}>0,
```

所以 `q0` 对 `x` 严格增、对 `y` 严格减。两个精确端点为

```math
q_0(2/19,1)^2
=16+\frac1{564}>16,
```

```math
q_0(1/10,249/250)^2
=16+\frac{258}{44237}>16.
```

因此

```math
\boxed{
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1.
}
\tag{5.2}
```

再由

```math
q_0(x,y)>\sqrt{\frac{8000}{503}},
\qquad J_{\rm def}<3,
```

得到

```math
\boxed{
1<\zeta<
\frac3{\sqrt{8000/503}-1}
<\frac{251}{250}.
}
\tag{5.3}
```

由 shell (2.3) 又有

```math
\boxed{
\frac{42}{\sqrt{2515}}<w<\frac{843}{1000}.
}
\tag{5.4}
```

为后续整数化，定义四个真实十进制 endpoint defect：

```math
\boxed{
b_2=10^{M-1}+2^{M-1}H,}
```

```math
\boxed{a_2=10^{M-1}-e,}
```

```math
\boxed{a_3=10^m+h,}
```

以及前述 `C=D-R`。由 (5.1)–(5.3)，

```math
\boxed{
0<H<\frac{5^{M-1}}{19},
\qquad
0<e<\frac{10^{M-1}}{250},
\qquad
0<h<\frac{10^m}{250},
\qquad
0<C<\frac{3D}{250}.
}
\tag{5.5}
```

也就是说最危险状态已经变成四个同时很小的整数缺口 `(H,e,h,C)`。

---

<a id="a2-03-detail-src-0099-9-8"></a>
#### `已严格完成`：第三坐标球面因子的统一短窗

primitive sphere 中沿用

```math
H_0-Y_3=5^Ec_-^2X,
\qquad
H_0+Y_3=c_+^2Y,
```

以及第二坐标 `Y_2`。在当前 core，精确有

```math
\frac{H_0}{g10^m}=3+\zeta-\frac CD,
\qquad
\frac{Y_2}{g10^m}=\frac{yw}{10x},
```

其中

```math
g=2^{t-1}\rho.
```

由 (5.2)–(5.4)，

```math
\boxed{
\frac{99}{125}
<\frac{yw}{10x}
<\frac{843}{1000}.
}
\tag{6.1}
```

所以两个正因子进入固定短窗：

```math
\boxed{
\frac{393}{125}
<\frac{H_0-Y_2}{g10^m}
<\frac{1607}{500},
}
\tag{6.2-}
```

```math
\boxed{
\frac{2389}{500}
<\frac{H_0+Y_2}{g10^m}
<\frac{606}{125}.
}
\tag{6.2+}
```

这两个区间会在后面的 `rho^2` square-side allocation 中提供 Archimedean 量化。

---

<a id="a2-03-detail-src-0099-9-9"></a>
#### 第三部分：新的整数接口

<a id="a2-03-detail-src-0099-9-10"></a>
#### `已严格完成`：`J_def` 满足纯整数四次式，`C | F(j)`

令

```math
T=10^m,
\qquad
Q=2\cdot10^M+b_2,
\qquad
P=9\cdot10^{M-1}+a_2,
```

```math
C_0=\frac{9b_2}{2},
\qquad
N_0=C_0^2+a_2^2.
```

从 shell 与拼接 relation 消去 `w`，可得到

```math
\boxed{
F(J):=
 b_2^2T\,J(TJ+2a_3)(10P-J)^2
-Q^2N_0(TJ+a_3)^2=0
}
\tag{7.1}
```

在 full finite-defect 状态中

```math
J=j-\frac CD,
\qquad \gcd(C,D)=1.
```

把 `F(j-X)` 看作整数系数多项式，`X=C/D` 是其既约有理根。由 rational-root theorem，

```math
\boxed{C\mid F(j).}
\tag{7.2}
```

特别地对当前 `j=3`，顶部补余量 `C` 必须整除一个完全由十进制 prefix 与 `a_3` 构成的显式整数。本文暂不把 (7.2) 宣称为 closure；它是后续与 prefix defect / Gaussian allocation 联立的新整数接口。

---

<a id="a2-03-detail-src-0099-9-11"></a>
#### `已严格完成`：独立的线性 `2^m` phase

沿用 source split：

```math
U=5^{M-s},
\qquad E=\lambda+s,
\qquad d=m-E,
```

```math
5^{M+\lambda}+c=g\theta,
```

以及 finite-defect 补余量形式

```math
\alpha_0q=C_jD+C,
\qquad
\alpha_0c_u=gA_j-5^EC,
```

其中

```math
A_j=a_3+j10^m,
\qquad
C_j=10P-j.
```

与

```math
c_Qq=U+g2^mc_u
```

一起消元，得到精确恒等式

```math
\boxed{
C\theta-UA_j
=
2^mc_u\left(
\alpha_0c_u-5^dc_QC_j
\right).
}
\tag{8.1}
```

因此

```math
\boxed{
C\theta\equiv UA_j\pmod{2^mc_u},
}
\tag{8.2}
```

特别地

```math
\boxed{
C\theta\equiv Ua_3\pmod{2^m}.
}
\tag{8.3}
```

这条 phase 与旧 `2^{2t-1}` square-depth phase 来源不同；目前把它保留为严格 compatibility，不宣称它单独给出空性。

---

<a id="a2-03-detail-src-0099-9-12"></a>
#### `已严格完成`：Hensel 商落入统一 `19–20` slot

定义

```math
L_*:=2^m5^Ec_u.
```

由 Hensel 商

```math
5^Eq+c_u=g\omega,
\qquad
5^{M+\lambda}+c=g\theta,
```

与

```math
c_Q\omega-\theta=L_*,
```

可精确化为

```math
\boxed{
\frac\theta{L_*}
=\frac{2+10^{-M}w}{x},
}
\tag{9.1}
```

```math
\boxed{
\frac{c_Q\omega}{L_*}
=\frac{x+2+10^{-M}w}{x}.
}
\tag{9.2}
```

在 `(a,k)=(9,2)` endpoint core 中，`H>=1` 与 (5.2) 保证

```math
\boxed{
19L_*<\theta<20L_*,
}
\tag{9.3}
```

```math
\boxed{
20L_*<c_Q\omega<21L_*.
}
\tag{9.4}
```

所以存在唯一

```math
\boxed{\varrho:=20L_*-\theta}
```

满足

```math
0<\varrho<L_*,
\qquad
\theta=20L_*-\varrho,
\qquad
c_Q\omega=21L_*-\varrho.
```

又因为 `theta` 与 `2,5,c_u` 均互素，

```math
\boxed{\gcd(\varrho,L_*)=1.}
\tag{9.5}
```

因此三个五进 channel 在这个 endpoint core 中共享同一个长度为 `L_*` 的 Hensel slot。

---

<a id="a2-03-detail-src-0099-9-13"></a>
#### 第四部分：真正产生 pruning 的 height split

<a id="a2-03-detail-src-0099-9-14"></a>
#### `已严格完成`：high-`m` / low-`m` 二分

记

```math
u_0=c_u\rho,
\qquad
K_\rho:=2^{m+t-1}5^m.
```

由 `x` 的定义有精确式

```math
\boxed{
\frac{u_0}{K_\rho}
=
\frac{2x}{4^t}\,
\frac{5^{M-s}}{20^m}.
}
\tag{10.1}
```

由于 `x<2/19`、`t>=3`，若

```math
m>\frac{6M}{11},
```

则 `20^6>5^11` 给出

```math
\boxed{
\frac{u_0}{K_\rho}<\frac1{304}.
}
\tag{10.2}
```

另一方面旧 tail bound

```math
5^\lambda>3\cdot2^{M+1}>2^M
```

与 `5^3<2^7` 给出

```math
\boxed{\lambda>\frac{3M}{7}.}
\tag{10.3}
```

source channel `s>0` 满足

```math
m=\frac32(\lambda+s)>\frac{9M}{14}>\frac{6M}{11},
```

因此它全部落入 (10.2) 的 small-source cone。

若

```math
m\le\frac{6M}{11},
```

则 source channel 不可能发生，故

```math
\boxed{s=0,}
```

只剩 balance / reflection，并有

```math
\boxed{
\frac{3M}{7}<\lambda\le m\le\frac{6M}{11}.
}
\tag{10.4}
```

reflection 的

```math
d=m-\lambda
```

进一步满足

```math
\boxed{0<d<\frac{9M}{77}.}
\tag{10.5}
```

于是最危险核被切成两个性质完全不同的无界锥：

```math
\boxed{
\begin{array}{ll}
m>6M/11:&u_0/K_\rho<1/304,\\[1mm]
m\le6M/11:&s=0,\quad 3M/7<\lambda\le m.
\end{array}}
\tag{10.6}
```

---

<a id="a2-03-detail-src-0099-9-15"></a>
#### `已严格完成`：low-`m` cone 强迫深 `5`-进前缀范数

沿用旧高阶 tail certificate

```math
10^m\mid b_3^4\cdot4N_0.
```

因为

```math
v_5(b_3)=m-\lambda,
```

所以

```math
\boxed{v_5(N_0)\ge4\lambda-3m.}
\tag{11.1}
```

在 low-`m` cone 中由 (10.4)：

```math
\boxed{v_5(N_0)>\frac{6M}{77}.}
\tag{11.2}
```

reflection 还有旧五进同步的精确深度

```math
v_5(N_0)=3\lambda-2m,
```

从而

```math
\boxed{
\text{reflection:}\quad
v_5(N_0)>\frac{15M}{77}.
}
\tag{11.3}
```

balance 则有

```math
\boxed{
\text{balance:}\quad
v_5(N_0)\ge m=\lambda>\frac{3M}{7}.
}
\tag{11.4}
```

因此 low-`m` cone 不是普通浅同余：`N_0=C_0^2+a_2^2` 必须承担随 `M` 线性增长的完整 `5`-进深度。

例如令

```math
\nu:=\left\lfloor\frac{6M}{77}\right\rfloor+1.
```

因为 `s=0` 时 `C_0` 为 `5`-进单位，存在两种 `sqrt(-1)` phase 之一 `iota_nu` 使

```math
a_2\equiv\iota_\nu C_0\pmod{5^\nu}.
```

代入 endpoint defects，得到

```math
\boxed{
e\equiv-9\cdot2^{M-2}\iota_\nu H\pmod{5^\nu}.}
\tag{11.5}
```

这把两个真实 prefix defects `H,e` 直接绑在深 `5`-进两相位上。

---

<a id="a2-03-detail-src-0099-9-16"></a>
#### `已严格完成`：low-`m` 中基础 square-depth 模数已经远大于 `C`

仍在 `s=0`。由

```math
5^{M-1}+H=2^{m+t+1}u_0
```

定义最基础的 square-depth 尺度

```math
\mathfrak L_0:=2^{2t-1}u_0^2.
```

`u_0` 可被完全消去：

```math
\boxed{
\mathfrak L_0
=\frac{(5^{M-1}+H)^2}{2^{2m+3}}.
}
\tag{12.1}
```

另一方面

```math
D=\frac{(5^{M-1}+H)5^d}{4c_u},
```

故

```math
\boxed{
\frac{\mathfrak L_0}{D}
=\frac{c_u(5^{M-1}+H)}{2^{2m+1}5^d}.
}
\tag{12.2}
```

由

```math
m+d=2m-\lambda<\frac{51M}{77},
\qquad M\ge11,
```

只用 `4^m<5^m` 就得到

```math
\boxed{\frac{\mathfrak L_0}{D}>\frac{25}{2}.}
\tag{12.3}
```

结合 `C/D<3/250`：

```math
\boxed{\mathfrak L_0>1000C.}
\tag{12.4}
```

这里仍需强调逻辑边界：`modulus >> C` 只提供极强 scale separation，不能单独推出 CRT representative 为空。后续还要控制其自然代表。

---

<a id="a2-03-detail-src-0099-9-17"></a>
#### 第五部分：`rho^2` Gaussian allocation 的 Archimedean 量化

<a id="a2-03-detail-src-0099-9-18"></a>
#### `已严格完成`：二进高/低因子的赋值完全固定

primitive sphere 给出

```math
H_0^2-Y_2^2=Y_1^2+Y_3^2.
```

在 deep-even terminal 中

```math
v_2(Y_3)=t-1,
```

而 `Y_1` 的二进深度严格更高，所以

```math
\boxed{v_2(H_0^2-Y_2^2)=2t-2.}
\tag{13.1}
```

`H_0,Y_2` 均为奇数，因此两个正因子

```math
H_0-Y_2,\qquad H_0+Y_2
```

中恰有一个满足

```math
\boxed{v_2=1,}
```

另一个满足

```math
\boxed{v_2=2t-3.}
\tag{13.2}
```

称后者为 **high-2 factor**。

若 `rho^2` 被 square-side allocation 到 high-2 factor `F_h`，则存在正奇数 `k_h` 使

```math
\boxed{F_h=2^{2t-3}\rho^2k_h.}
\tag{13.3}
```

因为

```math
2^{2t-3}\rho^2=\frac{g^2}{2},
```

令

```math
G:=\frac g{10^m},
```

并结合 (6.2±)，得到离散 Archimedean slots：

```math
\boxed{
G\in
\left(
\frac{786}{125k_h},
\frac{1607}{250k_h}
\right)
}
\tag{13.4-}
```

或

```math
\boxed{
G\in
\left(
\frac{2389}{250k_h},
\frac{1212}{125k_h}
\right),
\qquad k_h\text{ odd}.
}
\tag{13.4+}
```

这把 `rho^2` 的 Gaussian side choice 从纯素数分配提升成了一串彼此分离的实数槽。

任意一侧若只知道 `rho^2 | H_0±Y_2`，由 (6.2) 还得到粗高度界

```math
\boxed{
\rho<\frac{606}{125}\,2^{t-1}10^m.
}
\tag{13.5}
```

而在 high-`m` small-source cone 中，若令

```math
n_\rho:=\frac{H_0\pm Y_2}{\rho^2},
```

则 `n_rho` 为正偶数，并由 `rho<=u_0`、(10.2)、(6.2) 得到

```math
\boxed{n_\rho\ge956.}
\tag{13.6}
```

所以 high-`m` source 方向中的 `rho^2` quotient 被强制推到很深的离散层。

---

<a id="a2-03-detail-src-0099-9-19"></a>
#### `已严格完成`：low-`m` 中 high-2 allocation 迫使 `m` 接近 `M/2`

仍在 `s=0` low-`m` cone。若 `rho^2` 落到 high-2 factor，则由 (13.3) 与 (6.2) 得到

```math
2^t\rho<20\cdot10^m.
```

再使用

```math
5^{M-1}+H=4c_u2^mg,
```

和

```math
w=\frac{2^{M+1}c_Qc_u}{5^\lambda}<1,
\qquad \lambda\le m,
```

可推出

```math
\boxed{m>\frac{M-2}{2}.}
\tag{14.1}
```

所以

```math
\boxed{
m\le\frac{M-2}{2}
\Longrightarrow
\rho^2\text{ 不能进入 high-2 factor}.}
\tag{14.2}
```

这已经把原本自由的 Gaussian side choice 在 low-`m` cone 的一大块区域中强制定向到 `v2=1` 的低因子。

---

<a id="a2-03-detail-src-0099-9-20"></a>
#### `已严格完成`：reflection 精确中线 `M=2m` 的 high-2 分配全排除

现在进一步固定 reflection 且

```math
\boxed{M=2m.}
```

记

```math
d=m-\lambda>0.
```

由 `s=0` 的真实 denominator scale，

```math
\boxed{
G
=\frac{c_Q(1+H/5^{M-1})}{2w}\,5^{d-1}.
}
\tag{15.1}
```

另一方面 high-2 allocation 必须满足 (13.4±)，特别有

```math
G<\frac{1212}{125}.
```

由 `c_Q>=3`、`w<843/1000`，若 `d>=3`，(15.1) 的下界已经超过 `1212/125`，故

```math
\boxed{d\le2.}
\tag{15.2}
```

<a id="a2-03-detail-src-0099-9-21"></a>
#### `d=1`

此时

```math
G=\frac{c_Q(1+H/5^{M-1})}{2w}.
```

`c_Q≡3 (mod 4)`、`5∤c_Q` 与 `G<1212/125` 只留下

```math
\boxed{c_Q\in\{3,7,11\}.}
```

使用

```math
w<843/1000,
\qquad
w>837/1000,
\qquad
1<1+H/5^{M-1}<20/19,
```

得到三个连续区间：

```math
\frac{1500}{843}<G<\frac{30000}{15903},
```

```math
\frac{3500}{843}<G<\frac{70000}{15903},
```

```math
\frac{5500}{843}<G<\frac{110000}{15903}.
```

它们分别严格落在 (13.4±) 的相邻奇数 `k_h` slots 之间，因此都无交。

<a id="a2-03-detail-src-0099-9-22"></a>
#### `d=2`

此时

```math
G=\frac{5c_Q(1+H/5^{M-1})}{2w}.
```

`G<1212/125` 已经强迫

```math
\boxed{c_Q=3.}
```

并有

```math
\frac{7500}{843}<G<\frac{150000}{15903}.
```

该区间严格位于 `k_h=1` 的 low slot 上方、高 slot 下方；所有 `k_h>=3` slots 更低。因此同样无交。

综上：

```math
\boxed{
\text{reflection},\ a=9,k=2,\ M=2m
\Longrightarrow
\rho^2\text{ 不可能进入 high-2 factor}.
}
\tag{15.3}
```

所以在这一整个可无界增长的精确中线子族中，`rho^2` 的 Gaussian side 被强制唯一：

```math
\boxed{\rho^2\text{ 只能进入 }v_2=1\text{ 的低因子}.}
\tag{15.4}
```

这是本轮首次利用 endpoint 量化真正关闭一个无界 Gaussian-allocation 子族。

---


来源：`SRC-0099:9–1142`。原文保全，当前论证以本节为准。

<a id="a2-04"></a>
### A2-04　primitive source 支持、共同 gcd 与预算边界

**状态：已严格完成。** 既有 q/f/height 交集定理；同源 shadow 不构成第二份预算。

依赖：[A2-02](#a2-02)

核对：正文推导；本次重写未为此项另增枚举。

<a id="a2-04-detail-src-0117-9-1"></a>
#### `已严格完成`：`W_q` 与 sphere height 之间存在全局整数恒等式

§16.72 已得到

```math
2c_uW_q=c_+^2Y+5^\lambda c_-^2X.
\tag{1.1}
```

而 reflection 的 canonical factor allocation 早已有

```math
H_0-Y_3=5^\lambda c_-^2X,
\qquad
H_0+Y_3=c_+^2Y.
\tag{1.2}
```

把 (1.2) 两式相加：

```math
2H_0=c_+^2Y+5^\lambda c_-^2X.
```

与 (1.1) 比较，得到此前只在逐素数层出现、但实际上更强的全局恒等式

```math
\boxed{H_0=c_uW_q.}
\tag{1.3}
```

因此 §16.73 的

```math
v_r(W_q)=v_r(H_0)
```

对任何 `r\nmid c_u` 都只是 (1.3) 的逐素数投影；并不需要再次从 rational-root equation 逐素数恢复。

---

<a id="a2-04-detail-src-0117-9-2"></a>
#### `已严格完成`：`W_q` 就是旧 Hensel quotient `alpha_0`，也是 `gcd(alpha,H_0)`

§16.15 已从真实 concatenation plane 得到

```math
\alpha=\omega\alpha_0,
\qquad
H_0=c_u\alpha_0,
\qquad
\gcd(\omega,c_u)=1.
\tag{2.1}
```

与 (1.3) 比较立刻有

```math
\boxed{W_q=\alpha_0.}
\tag{2.2}
```

所以

```math
\boxed{
\alpha=\omega W_q,
\qquad
H_0=c_uW_q.
}
\tag{2.3}
```

由于 `gcd(omega,c_u)=1`，

```math
\boxed{W_q=\gcd(\alpha,H_0).}
\tag{2.4}
```

这给 `W_q` 一个完全 canonical 的含义：它不是 rational-root 后来新出现的自由 quotient，而是**原拼接分子与整数球面高度的最大公因子**。

当前 endpoint 为 `a_1=9`，第二分子有 `M-1` 位、第三分子有 `m+1` 位。令

```math
T=10^m,
\qquad
P=9\cdot10^{M-1}+a_2,
\qquad
K=10P,
```

则原拼接分子精确为

```math
\alpha
=9\cdot10^{M+m}+a_2\cdot10^{m+1}+a_3
=TK+a_3.
\tag{2.5}
```

故还可写成

```math
\boxed{TK+a_3=\omega W_q.}
\tag{2.6}
```

---

<a id="a2-04-detail-src-0117-9-3"></a>
#### `已严格完成`：`omega` 是拼接分子/分母的完整 gcd，`W_q` 是 reduced numerator

§16.15 的 LCM 为

```math
q_{\rm lcm}=b_2c_Q5^d=b_3g,
```

且原整数平面在约去公共尺度后给出

```math
q_{\rm lcm}\omega=c_u\beta.
\tag{3.1}
```

定义

```math
S:=\frac{q_{\rm lcm}}{c_u}.
\tag{3.2}
```

reflection 中

```math
b_2=2^{M+m+1}c_ug,
```

所以

```math
\boxed{S=2^{M+m+1}gc_Q5^d.}
\tag{3.3}
```

接下来证明

```math
\boxed{\gcd(W_q,S)=1.}
\tag{3.4}
```

逐个 prime source 检查即可：

1. §16.72 已给 `W_q mod 4`，故 `W_q` 为奇数；
2. (1.1) 模 `5` 时第二项消失，而 `c_u,c_+,Y` 都是 `5`-进单位，故 `5\nmid W_q`；
3. §16.30 有 `gcd(H_0,g)=1`，结合 (1.3) 得 `gcd(W_q,g)=1`；
4. 若 `p\mid c_+`，由 `H_0+Y_3=c_+^2Y` 得 `H_0\equiv-Y_3 (mod p)`；若 `p\mid c_-`，则由另一式得 `H_0\equiv Y_3 (mod p)`。因为 `c_Q\mid b_3`、`gcd(a_3,b_3)=1` 且 `gcd(g,c_Q)=1`，两种情形都有 `p\nmid Y_3=ga_3`。故 `gcd(H_0,c_Q)=1`，再由 (1.3) 得 `gcd(W_q,c_Q)=1`。

这证明 (3.4)。

由 (3.1) 有

```math
\beta=S\omega.
\tag{3.5}
```

结合 `alpha=omega W_q` 与 (3.4)：

```math
\boxed{
\gcd(\alpha,\beta)=\omega.
}
\tag{3.6}
```

所以原十进制拼接分数的最低项表示被完全识别：

```math
\boxed{
\frac{\alpha}{\beta}
=\frac{W_q}{S},
\qquad
\gcd(W_q,S)=1.
}
\tag{3.7}
```

同时由

```math
H_0=c_uW_q,
\qquad
q_{\rm lcm}=c_uS
```
还得到对 sphere lift 的对称 primitive recovery：

```math
\boxed{
\gcd(H_0,q_{\rm lcm})=c_u.
}
\tag{3.8}
```

因此四个此前分散的量其实是两个最简分数的同一套 gcd 数据：

```math
\boxed{
\omega=\gcd(\alpha,\beta),
\qquad
c_u=\gcd(H_0,q_{\rm lcm}),
\qquad
W_q=\frac{\alpha}{\omega}=\frac{H_0}{c_u}.
}
\tag{3.9}
```

---

<a id="a2-04-detail-src-0117-9-4"></a>
#### `已严格完成 / 审计降级`：height channel 的 `N_0` 非剩余 character 是自动 shadow

设

```math
r\ne3,
\qquad
r\equiv3\pmod4,
\qquad
r\mid W_q.
\tag{4.1}
```

由 (1.3)，`r\mid H_0`。§16.73 已证明这种 `r` 与 `5gc_QXY` 互素；也可从 §16.45 的本原性逐项恢复。

把 (1.2) 相乘并模 `r`：

```math
(H_0-Y_3)(H_0+Y_3)
=5^\lambda c_Q^2XY.
```

因为 `H_0\equiv0 (mod r)`、`Y_3=ga_3`，

```math
-g^2a_3^2
\equiv
5^\lambda c_Q^2XY
\pmod r.
\tag{4.2}
```

又

```math
N_0=5^{\nu_5}XY,
\qquad
\nu_5-\lambda=-2d,
```
故

```math
\boxed{
N_0
\equiv
-\left(
\frac{ga_3}{c_Q5^d}
\right)^2
\pmod r.
}
\tag{4.3}
```

由于 `r=3 mod 4`，`-1` 为非平方，于是

```math
\boxed{
\left(\frac{N_0}{r}\right)=-1.
}
\tag{4.4}
```

因此 `prime-source.md` 与 §16.73 中记录的 height character (4.4) **不是独立 obstruction**：一旦 `r\mid W_q`，它已经由 canonical factor equality 自动推出。

后续不得再把

```math
r\mid H_0
\quad\text{和}\quad
\left(\frac{N_0}{r}\right)=-1
```

当作两条独立局部条件收费。真正新增的 global input 必须来自 `W_q` 作为 reduced numerator 的十进制/prime-flow 结构，或来自它与 `widehat{T}_2` excess carrier 的进一步连接。

---

<a id="a2-04-detail-src-0117-9-5"></a>
#### `已严格完成`：任意 saturation-height 交集都强迫 `2K-9=0`

设非 `3` inert prime `p` 同时满足

```math
p\mid W_q,
\qquad
p\mid\mathscr L_{23}.
\tag{5.1}
```

第二式等价于

```math
2a_3+9T\equiv0\pmod p.
\tag{5.2}
```

另一方面由 (2.6)，`p\mid W_q` 给出

```math
TK+a_3\equiv0\pmod p.
\tag{5.3}
```

当前 `p\nmid10`，故 `T` 是单位。把 (5.2) 代入 (5.3)：

```math
K-\frac92\equiv0\pmod p.
```

即

```math
\boxed{2K-9\equiv0\pmod p.}
\tag{5.4}
```

这是 denominator saturation 与 sphere-height/reduced-numerator channel 的**统一交集 resultant**；它不依赖 `q/f` 侧别。

---

<a id="a2-04-detail-src-0117-9-6"></a>
#### `已严格完成`：q-carrier 与 height channel 的交集只可能是 special `23`

若 (5.1) 中的 `p` 同时还是 q-side additive carrier，则 §16.67 给出

```math
K^2\equiv26\pmod p.
\tag{6.1}
```

而 (5.4) 给出 `K=9/2`，故

```math
\frac{81}{4}\equiv26\pmod p,
```
即

```math
p\mid(104-81)=23.
```

因此

```math
\boxed{
q\text{-carrier}\cap\text{height channel}
\Longrightarrow p=23.
}
\tag{6.2}
```

这把 `prime-source.md` 的 special `23` 重新解释为：它不是随意出现的 fixed exception，而是 **q-side saturation 与 reduced-numerator height channel 的唯一可能交点**。

这一结论还清理了 generic `c_Q` overlap。对 `p\ne11,23` 的 q-carrier，§16.72/16.73 已有

```math
v_p(W_q)=v_p(c_Q).
\tag{6.3}
```

但 (3.4) 已证明 `gcd(W_q,c_Q)=1`，所以

```math
\boxed{
v_p(W_q)=v_p(c_Q)=0
\qquad(p\ne11,23,\ p\text{ q-carrier}).}
\tag{6.4}
```

因此 generic q-carrier 的 `c_Q` overlap 实际全部消失。唯一 `c_Q`-overlap 是 `prime-source.md` 已识别的 special `11`，而该点满足 `11\nmid W_q`；special `23` 则满足 `23\nmid c_Q`。

所以 q-side 的 prime-source 图现在是严格三分：

```math
\boxed{
\begin{array}{ll}
\text{generic }p\ne11,23:& p\nmid c_QW_q,\\
\text{special }11:& 11\mid c_+,\ 11\nmid W_q,\\
\text{special }23:& 23\nmid c_Q,\ \text{且它是唯一可能的 height overlap}.
\end{array}}
\tag{6.5}
```

---

<a id="a2-04-detail-src-0117-9-7"></a>
#### `已严格完成`：f-carrier 若进入 height channel，必须满足两条独立 reciprocity 签名

现在设 `p` 是 f-side saturation carrier，并同时满足 `p\mid W_q`。由 (3.4) 有 `p\nmid c_Q`，所以 §16.67 的 generic f-side law 适用：

```math
K^2-26
\equiv
\left(\frac{2c_Q}{2^m5^\lambda g}\right)^2N_0
\pmod p.
\tag{7.1}
```

由 (5.4)，`K=9/2`，故

```math
K^2-26=-\frac{23}{4}.
```

再用 (4.4)：

```math
\left(\frac{-23}{p}\right)
=
\left(\frac{N_0}{p}\right)
=-1.
\tag{7.2}
```

对 `p=3 mod 4`，二次互反律给出

```math
\left(\frac{-23}{p}\right)
=
\left(\frac p{23}\right).
```

所以

```math
\boxed{\left(\frac p{23}\right)=-1.}
\tag{7.3}
```

特别地 `p\ne23`。

还可以把 §16.50 的 curvature character 化成另一个固定签名。saturation 下

```math
a_3\equiv-\frac92T\pmod p,
```
故

```math
\mathscr R_{23}
=2a_3^2+9Ta_3+13T^2
\equiv13T^2\pmod p.
\tag{7.4}
```

另一方面由 (4.2)

```math
XY
\equiv
-\frac{g^2a_3^2}{5^\lambda c_Q^2}
\equiv
-\frac{81}{4}\frac{g^2T^2}{5^\lambda c_Q^2}
\pmod p.
\tag{7.5}
```

在

```math
\mathscr R_{23,f}
=2^m5^dg^2\mathscr R_{23}+2Tc_Q^2XY
```
中使用

```math
2^m5^d=\frac{T}{5^\lambda}
```
得到

```math
\boxed{
\mathscr R_{23,f}
\equiv
-\frac{55}{2}\frac{g^2T^3}{5^\lambda}
\pmod p.
}
\tag{7.6}
```

若 `p\mid\mathscr R_{23,f}`，因右侧所有其他量均为单位，只可能 `p=11`。但 §16.50 的 double-root law 此时给出

```math
K\equiv9+2a_3T^{-1}\equiv0\pmod{11},
```
而 (5.4) 给出 `K=9/2\not\equiv0 (mod 11)`，矛盾。因此

```math
\boxed{p\ne11,23,\qquad p\nmid\mathscr R_{23,f}.}
\tag{7.7}
```

于是 §16.50 的 simple-root curvature character 必须成立：

```math
\left(\frac{\mathscr R_{23,f}}p\right)
=
\left(\frac2p\right)^{m+3}
\left(\frac5p\right)^d.
\tag{7.8}
```

把 (7.6) 代入，使用 `T=2^m5^m` 与 `d=m-\lambda`。两边相除后全部 `m,lambda,d` 指数消去，恰剩

```math
\boxed{\left(\frac{-55}{p}\right)=1.}
\tag{7.9}
```

对于 `p=3 mod 4`，再次用二次互反律：

```math
\boxed{
\left(\frac p5\right)
\left(\frac p{11}\right)=1.
}
\tag{7.10}
```

因此 f-side saturation 与 height channel 若相交，必须同时满足

```math
\boxed{
\begin{gathered}
p\equiv3\pmod4,
\qquad p\notin\{3,5,11,23\},\\
2K\equiv9\pmod p,\\
\left(\frac p{23}\right)=-1,
\qquad
\left(\frac p5\right)
\left(\frac p{11}\right)=1.
\end{gathered}}
\tag{7.11}
```

这没有把 f-height intersection 全部排空，但已经把它从“任意 endpoint-external inert prime”压成一个固定的三二次域 reciprocity signature。

---

<a id="a2-04-detail-src-0117-9-8"></a>
#### `已严格完成`：去掉 balanced `3` 后，`W_q` 的 non-`3` inert parity 总体为偶

§16.57、16.58 给出

```math
W_q\equiv3Z\pmod4,
\qquad
\delta=1\iff Z\equiv1\pmod4,
\qquad
\delta=0\iff Z\equiv3\pmod4.
\tag{8.1}
```

当 `delta=1` 时，§16.11 还给出 `v_3(H_0)=1`；`3\nmid c_u`，所以由 (1.3)

```math
v_3(W_q)=1.
\tag{8.2}
```

定义

```math
W_q^{\rm prim}:=\frac{W_q}{3^\delta}.
\tag{8.3}
```

若 `delta=0`，(8.1) 直接给 `W_q\equiv1 (mod 4)`；若 `delta=1`，则 `W_q\equiv3 (mod 4)` 且恰约去一份 `3`。两种情形统一得到

```math
\boxed{W_q^{\rm prim}\equiv1\pmod4.}
\tag{8.4}
```

因此 `W_q` 中除 balanced `3` 以外的所有 `3 mod 4` 素数，其**奇赋值 carrier 的总数必为偶数**：

```math
\boxed{
\sum_{\substack{r\ne3\\r\equiv3\ (4)}}v_r(W_q)
\equiv0\pmod2.
}
\tag{8.5}
```

这里的和只需按模 `2` 理解。它不能推出每个 `v_r(W_q)` 都为偶数，但它说明任何 non-`3` height odd carrier 都不能作为唯一的未配对 inert source 出现。

---

<a id="a2-04-detail-src-0117-9-9"></a>
#### 更新后的逻辑边界

本轮最重要的审计结论是：此前把 height channel 写成

```math
r\mid H_0,
\qquad
\left(\frac{N_0}{r}\right)=-1
```

会让它看起来像“两条条件”。严格地说，第二条只是第一条通过 canonical factor equality 的 quadratic shadow。真正的新结构是

```math
\boxed{W_q=\gcd(\alpha,H_0)}
```

以及 saturation-height 交集律

```math
\boxed{p\mid W_q,\ p\mid\mathscr L_{23}\Longrightarrow2K-9\equiv0\pmod p.}
```

由此：

1. q-side 与 height 的交集只可能是 `23`；
2. generic q-carrier 的 `c_Q` overlap 全部消失；
3. f-side 与 height 的交集必须满足 (7.11) 的固定 reciprocity signature；
4. height character `(N_0/r)=-1` 不得重复计作独立 obstruction；
5. non-`3` height odd carriers 在 `W_q/3^delta` 中必须成总体偶 parity。

研究目标见 [路线记录](RESEARCH.md)。

- 把 `W_q` 作为**最低项拼接分子的 reduced numerator**，与 `widehat{\mathcal T}_2` 的 endpoint-external excess prime 建立逐 prime-power 的赋值桥；
- 对仍可能存在的 f-height intersection，把 (7.11) 与纯 prefix resultant `Psi_f` 的完整 `p^e` 深度联立，尝试把三个二次域 signature 提升成一个真正的 Hensel/resultant 矛盾。

---

<a id="a2-04-detail-src-0117-9-10"></a>
#### `已严格完成`：f-height intersection 精确塌缩到固定素数 `7,43`，且不存在共同二阶深接触

§9 的第二个后续方向可以直接推进一步。仍设 `p` 是非 `3` 的 inert f-side saturation carrier，并且

```math
p\mid W_q.
\tag{10.1}
```

由 (3.4)，`p\nmid c_Q`，因此 generic f-side law (7.1) 可用。关键是这里不再只取 Legendre symbol，而保留 (4.3) 的**完整剩余类**。

先把 canonical factor equality (1.2) 相乘：

```math
H_0^2-g^2a_3^2=5^\lambda c_Q^2XY.
```

由于

```math
N_0=5^{\nu_5}XY,
\qquad
\nu_5-\lambda=-2d,
```
实际存在精确有理恒等式

```math
\boxed{
N_0=
\left(\frac{H_0}{c_Q5^d}\right)^2
-
\left(\frac{ga_3}{c_Q5^d}\right)^2.
}
\tag{10.2}
```

在当前 `p` 上所有分母都是 `p`-进单位，而 `H_0=c_uW_q`，故 (10.2) 模 `p` 正好恢复

```math
N_0\equiv-
\left(\frac{ga_3}{c_Q5^d}\right)^2
\pmod p.
\tag{10.3}
```

把 (10.3) **直接**代入 f-side law (7.1)，并用 `lambda+d=m`：

```math
\begin{aligned}
K^2-26
&\equiv
-\left(
\frac{2c_Q}{2^m5^\lambda g}
\frac{ga_3}{c_Q5^d}
\right)^2\\
&=-\left(\frac{2a_3}{T}\right)^2
\pmod p.
\end{aligned}
\tag{10.4}
```

另一方面 saturation `p\mid\mathscr L_{23}` 给出

```math
\frac{2a_3}{T}\equiv-9\pmod p,
\tag{10.5}
```

而 height/saturation intersection (5.4) 给出

```math
K\equiv\frac92\pmod p.
\tag{10.6}
```

于是 (10.4) 的两边分别变成

```math
K^2-26\equiv-\frac{23}{4},
\qquad
-\left(\frac{2a_3}{T}\right)^2\equiv-81.
```

故

```math
\boxed{301\equiv0\pmod p.}
\tag{10.7}
```

因为

```math
301=7\cdot43,
```
得到严格固定素数塌缩

```math
\boxed{
p\in\{7,43\}.}
\tag{10.8}
```

这比 (7.11) 强得多：旧的三二次域 signature 只给 residue class 条件，而 (10.8) 把整个无界 f-height prime support 压成两个固定素数。两者确实都满足 (7.11)，所以这里仍不是空性；验证脚本也显式检查了这一点。

还可以把同一计算提升到 prime-power 深度。写

```math
e:=v_p(f),
\qquad
h:=v_p(W_q)=v_p(H_0),
\qquad
\tau:=v_p(\widehat{\mathcal T}_2),
\tag{10.9}
```

并假设完整 saturation

```math
p^e\mid\mathscr L_{23}.
\tag{10.10}
```

由 §16.69 的截断赋值律，令

```math
s:=\min\{\tau,e\},
```
则

```math
p^s\mid\Psi_f.
\tag{10.11}
```

同时 `f=g\omega+c_u`，且 `p\mid f`、`p\nmid gc_u`，所以 `p\nmid\omega`。由 `alpha=omega W_q` 得

```math
v_p(\alpha)=h.
\tag{10.12}
```

又

```math
\alpha-\mathscr L_{23}
=T\left(K-\frac92\right),
```
故在

```math
t:=\min\{s,h\}=\min\{\tau,e,h\}
\tag{10.13}
```

的深度上有

```math
K\equiv\frac92\pmod{p^t},
\qquad
\frac{2a_3}{T}\equiv-9\pmod{p^t}.
\tag{10.14}
```

另一方面 (10.2) 给出

```math
N_0\equiv-
\left(\frac{ga_3}{c_Q5^d}\right)^2
\pmod{p^{2h}},
\tag{10.15}
```

而 §16.69 的 `Psi_f` 同余与 `p^e\mid f` 把 (7.1) 同样提升到模 `p^s`。因此在共同深度 `t` 上，(10.4)–(10.7) 原样成立，得到

```math
\boxed{p^t\mid301.}
\tag{10.16}
```

但 `301=7\cdot43` 在两个剩余素数上都只有一次赋值，所以

```math
\boxed{
\min\left\{
 v_p(\widehat{\mathcal T}_2),
 v_p(f),
 v_p(W_q)
\right\}=1.
}
\tag{10.17}
```

这给出真正的 Hensel transversality：f-denominator saturation、height/reduced-numerator 深度和 odd-excess 深度**不能三者同时进入二阶**。特别地：

- 若 `v_p(f)>=2` 且 `v_p(W_q)>=2`，则必有 `v_p(widehat{T}_2)=1`；
- 若 odd excess 深度与 height 深度都至少为 `2`，则 `v_p(f)=1`；
- 若 odd excess 深度与 denominator 深度都至少为 `2`，则 `v_p(W_q)=1`。

因此 f-height intersection 的剩余核心已经从“任意素数、任意 Hensel 深度”压成固定 `7/43` 的**一阶横截或单侧浅层**问题。下一步应分别审计 `p=7` 与 `p=43` 的唯一 Hensel 轨道，并尝试与 `W_q^{\rm prim}\equiv1 (mod 4)` 的配对约束及 prefix digit phase 联立；不能再把 (7.11) 当作无界 prime family 处理。


来源：`SRC-0117:9–848`。原文保全，当前论证以本节为准。

<a id="a2-05"></a>
### A2-05　实际减向四阶 transport 与 terminal character

**状态：已严格完成。** 实际 F=U(J0−J)、L=(R0−R)/K²；strict terminal 条件 (26/p)=+1。

依赖：[A2-02](#a2-02)

核对：`a2-quartic`、`a2-third-order`、`a2-terminal-character`

采用真实四次多项式

```math
\Phi(J,R)=J(J+2\zeta)(K-J)^2-R(J+\zeta)^2,\quad U=2K-9,
```

```math
R_0=K^2-(18+4\zeta)K+18\zeta+55,\quad
J_0=\frac{K^2-64K\zeta-576K+288\zeta+1296}{16U}.
```

原 source 平面给 `Phi(J,R)=0`，实际正 parent 定义为

```math
F=U(J_0-J),\qquad L=(R_0-R)/K^2.
```

为完整写出 Euclidean 项，令

```math
\begin{aligned}
L_K&=K^2-576K+1296,\quad A_0=5K^2+144K-324,\\
B_2&=381K^4-78048K^3-277520K^2+2392704K-3074112,\\
B_1&=189K^4-126720K^3+132784K^2+1359360K-2218752,\\
B_0&=63K^4-54432K^3+136672K^2+239616K-539136,\\
E_{63}&=98304U^3A_0\zeta^3-1024U^2B_2\zeta^2
 +32UL_KB_1\zeta-L_K^2B_0.
\end{aligned}
```

把 `r=1/K,u=zeta/K` 代入，`Q(r,u,v)` 是多项式
`r^8 E63(1/r,u/r)` 除以 `55r²+18(u−1)r+1−4u−v` 的 Euclidean 商。
使用 `v=R0/K²−L`，定义

```math
\begin{aligned}
E_{\rm proj}&=\frac{65536U^4}{K^8}
 \{\Phi(J_0,R_0)-\Phi(J_0-F/U,R_0-K^2L)\},\\
M&=E_{\rm proj}-Q(1/K,\zeta/K,R_0/K^2-L)L.
\end{aligned}
```

这是完整定义；不把近似点与真实点交换后沿加向 transport。
`M` 总次数为四，全部 `(F,L)` 次数对恰为
`(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(0,3),(4,0),(0,4)`。
令 `F=K²sY,L=s(X+Y)`，按 `s` 次数取 `Hrat_j`。各层的分母和 content 为

| j | 分母 | numerator content |
|---|---|---|
| 1 | `5^7 11^7 K^6` | 64 |
| 2 | `5^5 11^6 K^4` | 256 |
| 3 | `5^5 11^5 K^2` | 8192 |
| 4 | `5^4 11^4` | 65536 |

去掉这些显式分母与正 content 后定义整数多项式 `H_j`。这一定义同时
固定下面 fixed-3 计算中的 `H2,H3`，不会在另一文件里更换符号。
四阶层精确为

```math
\boxed{\mathcal H_4=26[27(X+Y)]^4-[55Y]^4.}
```

当 inert `p` 不在清分母的 bad support、两原 parent 的共同深度为 `h`，
前三层均饱和且实际 terminal 层深度严格超过 `4h` 时，去 content 后
`H4=0 mod p`。严格 terminal sector 的 `Y` 与 `27(X+Y)` 为单位，故

```math
26=\left(\frac{55Y}{27(X+Y)}\right)^4\pmod p.
```

因此必须 `(26/p)=+1`。`p=3 mod4` 时非零四次幂集合与平方集合相同，
所以在这些非退化假设下这是精确的 character gate。它不是全 pool 的空性。

每一层若未达到下一饱和阈值，就由该层的非零初项决定深度；若达到阈值，
才移入下一层。次数四保证递推在第四层停止，但 terminal 的额外 cancellation
深度仍可变化。所有层都是同一个 `M` 的展开，不能各算一个独立 parent。

在实际 parent box `0≤1/K≤1/1000,0≤zeta/K≤1/1000,0≤X/Y≤1/23`，
有界矩形上的 Bernstein 系数逐项给 `H1<0,H2<0,H3>0`；三阶的最小
Bernstein 系数为 `77742383923>0`。清分母的上下界使四阶 remainder
不足以改变所需实数符号。这里的计算是有限个有理系数对整个矩形的证明，
不是在矩形中有限抽样。

物理二进类型 `X` 为奇数、`v2(Y)=m+t−1` 时，三阶唯一浅项是
`−8800610472 X³ zeta²`，其系数为 `−2³3⁸·107·1567`。
逐项比较斜率后，正 primitive 的 `N3=3 mod4`；四阶唯一浅项是
`2·3^12·13 X⁴`，同样解析给物理 positive primitive 的 orientation。
此范围不能推广到任意两个 odd parents。完整系数表与逐项比较由
`a2-quartic` 从上述定义独立生成和核对。


<a id="a2-06"></a>
### A2-06　固定 outer 例外与 terminal recycling

**状态：已严格完成。** pC 的共同深度一层及 exact triple-saturation 边界；不推出整个 pool 独立。

依赖：[A2-04](#a2-04)、[A2-05](#a2-05)

核对：`a2-outer-root`、`a2-outer-exception`

<a id="a2-06-detail-src-0114-457-1"></a>
#### actual transport 方向审计与严格 terminal 条件

本节以 [`crt-descent-ledger.md` 的方向审计](RESEARCH.md#a2-transport)（原始记录 SRC-0096）
为准。真实 root 与 ratio 满足
```math
J=J_0-F_\Delta/(2K-9),\qquad R=R_0-K^2\mathscr L_{\rm proj}.
```
因此 actual transport 是 `Phi(J0,R0)-Phi(J0-F/U,R0-K²L)`。
旧 high-order checker 在 approximation 上用了加向；它给出的
`26[27(X_d+Y_d)]^4+[55Y_d]^4` 与 character `(26/p)=-1`
均为 **失效/降级**。旧本专题引用 `(-26/p)=-1` 虽恰匹配 actual
符号，却不能由旧 ledger 的加号四阶系数证明。本轮从 exact 原式重新建立
```math
\boxed{\mathcal H_4=26[27(X_d+Y_d)]^4-[55Y_d]^4,}
```
故 strict-lower-block terminal overdepth 必须满足
```math
\boxed{\left(\frac{26}{p}\right)=+1,
\qquad\left(\frac{-26}{p}\right)=-1.}
\tag{9.4}
```
而精确核对给 `p_C` 的 `(26/p_C)=-1`，所以该 **strict sector** 为空。
这不删除 lower block 恰为 `4h` 的 boundary cancellation。

此外 `ord_{p_C}(10)=p_C-1`，单纯 decimal orbit 仍不能排除 first-layer payment。

<a id="a2-06-detail-src-0114-457-2"></a>
#### `已严格完成`：四对象在 `p_C` 上的共同深度恰为一层

在 §§4–8 的 genuine external `Q_4 / r=3` 子支，定义

```math
t_C:=\min\{v_{p_C}(\Xi_-),v_{p_C}(\Xi_+),
                 v_{p_C}(G_\Delta),v_{p_C}(C)\}.
\tag{9.5}
```

上述 first-layer 假设已经保证 `t_C>=1`。若 `t_C>=2`，additive gcd
interface 将 coefficient lock 提升到模 `p_C^2`；`D`、`T`、`b_2`
均为单位，而 `p_C^2|C` 将真实 root 提升为 `r=3 mod p_C^2`。
因此 (8.2) 和两个 outer equations 都必须同时在模 `p_C^2` 上消失。

在 (8.7) 的 first-layer 点，`(P_2,P_4)` 关于 `(K,zeta)` 的 Jacobian
determinant 精确为

```math
\boxed{3212002394182\not\equiv0\pmod{p_C}.}
\tag{9.6}
```

其唯一二阶 lift 写为
`K=K_C+p_C u,zeta=zeta_C+p_C v`，则

```math
\boxed{(u,v)=(17757405664989,19804620386067)\pmod{p_C}.}
\tag{9.7}
```

直接代入 (8.2) 的左边 `F_{D,C=0}`，得到

```math
\boxed{
\frac{F_{D,C=0}}{p_C}
\equiv2979046557878\not\equiv0\pmod{p_C}.}
\tag{9.8}
```

所以不存在三方程共同的二阶 lift，严格得到

```math
\boxed{t_C=1.}
\tag{9.9}
```

也可由 (8.4) 中 `p_C` 的 resultant exponent 恰为 `1` 得到同一
截断。此结论不保证四个 individual valuations 全部为 `1`；它只保证
至少一个对象停止在第一层，不能据此删除 first-layer payment。

<a id="a2-06-detail-src-0114-457-3"></a>
#### `已严格完成`：实际 parent ratio 排除 strict-lower-block terminal sector

采用 [`crt-descent-ledger.md` 的 balance-tail](RESEARCH.md#a2-transport)（原始记录 SRC-0096）
和 finite quartic hierarchy 的记号

```math
X=5^\lambda\mathscr R_{63}^\star,
\qquad Y=g2^m\widehat{\mathscr D}_{63},
\qquad h=v_{p_C}(G_\Delta)\ge1.
\tag{9.10}
```

在 (8.7) 的固定 residue，first-order 两个 coefficient gates 给出

```math
\boxed{
\mathcal G_<\equiv9320260449125,
\qquad
\mathcal G_>\equiv13624230293838
\pmod{p_C}.}
\tag{9.11}
```

两者均为单位。因此 unequal parent depth 的两条 linear-tail recycling
路线上，唯一最低系数不会消失；若继续 same-prime recycling，必须进入
equal parent depth `v_{p_C}(X)=v_{p_C}(Y)=h`。写
`X=p_C^h X_0,Y=p_C^h Y_0`，first balance 使唯一 ratio 为

```math
\boxed{
\frac{X_0}{Y_0}
\equiv\chi_{geom}
:=-\frac{2\mathcal G_>}{81\mathcal G_<}
\equiv5130679962854\pmod{p_C}.}
\tag{9.12}
```

把该实际 ratio 代入 quartic coefficient，而不只检查 character，得到

```math
\boxed{
\mathcal H_4(\chi_{geom},1)
=26[27(\chi_{geom}+1)]^4-55^4
\equiv16192417895792\not\equiv0\pmod{p_C}.}
\tag{9.13}
```

故在该 first-recycling 子支上 `v_{p_C}(M^{(4)})=4h`。
若进一步满足 terminal-character theorem 的明确假设

```math
v_{p_C}(M^{(1)}+M^{(2)}+M^{(3)})>4h,
\tag{9.14}
```

则最低层只有 quartic block，严格得到

```math
\boxed{v_{p_C}(M)=4h.}
\tag{9.15}
```

于是 **(9.14) 下的** terminal overdepth `v_{p_C}(M)>4h` 被排除。
这是独立于旧反号论证的实际 coefficient 排除，适用于任意 `h>=1`。
若 lower block 的深度恰为 `4h`，它仍可与 quartic block 发生 normalized
cancellation；(9.13) 不排除这一 boundary regime，也不关闭全 A2。

<a id="a2-06-detail-src-0114-457-4"></a>
#### `已严格完成`：`p_C` 若继续 terminal recycling，只能 exact triple saturation

同一 canonical reconstruction 还给出实际 parent ratio 上的其它
primitive homogeneous coefficients：

```math
\boxed{
\begin{array}{c|rrrr}
n&1&2&3&4\\\hline
\mathcal H_n(\chi_{geom},1)\bmod p_C
&0&2328839710684&18611479848870&16192417895792
\end{array}}
\tag{9.16}
```

其中 `H_1` 的零点正是 first balance，后三项均为单位。采用
finite quartic hierarchy 的 ordinary tail depths

```math
\rho=v_{p_C}(B_{63}),\quad
\sigma=v_{p_C}(C_{63}^{(2)}),\quad
\tau=v_{p_C}(C_{63}^{(3)}).
\tag{9.17}
```

则任意 same-prime common label 的 terminal overdepth 都必须满足

```math
\boxed{v_{p_C}(M)>4h\Longrightarrow\rho=\sigma=\tau=h.}
\tag{9.18}
```

证明逐层使用 exact hierarchy 的最低赋值：`rho<h` 时已经停在
`h+rho<2h`；`rho>h` 时 quadratic block 的单位独占 `2h`。
因此越过 `2h` 只能 `rho=h`。进入该子支后，`sigma<h` 时停在
`2h+sigma<3h`，`sigma>h` 时 cubic 单位独占 `3h`；故越过 `3h`
只能 `sigma=h`。再以 quartic 单位重复一步，越过 `4h` 只能 `tau=h`。
各显示 rational scales 在 `p_C` 上都是单位，故无隐藏 content 修正。

所以该 fixed exception 无法使用 strict `P_110`、`P_148` 或 strict
quartic coefficient-zero sector 来继续；全部 deeper recycling 被压到
三个 exact baseline collisions。依赖
[`crt-descent-ledger.md` 的 third-order parity spill](RESEARCH.md#a2-transport)（原始记录 SRC-0096），
在 (9.18) 下第三阶 parent 的深度恰为 `4h`，是偶数。因此 `p_C` 对
该 parent 的 odd-inert parity 中性；第三阶 positive carrier 仍需
terminal recycling pool 之外的 supplier。这里不能直接说该 supplier
与所有其它 old/external pools 都不同。尤其正确 transport 已撤回旧 generic fixed-`3` depth `6/10`，故 fixed `3` 仍是可能补给；其全局排除仍为 `待证`。

---


<a id="a2-06-detail-src-0119-21-1"></a>
#### 较弱 elimination 留下的 fixed prime

令

```math
\zeta=a_3/T,
\qquad
K\equiv55/18
```

来自 source-common line。把 shared-outer free-ratio gate代入得到

```math
G_S(\zeta)=217\zeta^3+219\zeta^2-1728\zeta-1152.
```

把 universal descendant cubic在同一 `K=55/18` 上清分母得到 primitive cubic `E_S(\zeta)`。checker 验证

```math
\begin{aligned}
\left|\operatorname{Res}_\zeta(G_S,E_S)\right|
={}&41\cdot64217\cdot72238473017\\
&\cdot2679539349324345019093\\
&\cdot740759498168792879433565547.
\end{aligned}
```

前四枚 prime 都是 `1 mod4`，唯一 inert factor 是 `p_*`。并且

```math
\gcd_{\mathbf F_{p_*}[\zeta]}(G_S,E_S)
=
\zeta-121854543490110025177920950,
```

所以它确实是该**较弱系统**的真实 first-layer `F_p` 交点，而非扩域伪根。

 素性审计：checker 为这五个 factors 加入完整 Lucas `n-1`
证书，41 个非基节点全部递归到素数 `2`。每个节点精确核对 `n-1`
的完整因子乘积、`a^(n-1)=1 mod n`，以及对每个已证明素因子 `q`
都有 `gcd(a^((n-1)/q)-1,n)=1`。于是任何 `n` 的素因子都必须承载
阶 `n-1`，只能等于 `n`，给出无条件素性证明。
两枚大于 `2^64` 的顶层 factors 分别使用 witness `a=6` 与 `a=2`；
其 `n-1` 因子表及全依赖链在 checker 内固定保存。这里的完整
prime-support 结论不再依赖单独的 probable-prime 检查。

此外 checker 记录

```math
\left(\frac{55}{p_*}\right)=1,
\qquad
\left(\frac{-26}{p_*}\right)=-1,
```

两条均兼容 actual source/strict-terminal characters。 的
[方向审计](RESEARCH.md#a2-transport)（原始记录 SRC-0096） 证明实际四阶系数
为 `26[27(X_d+Y_d)]^4-[55Y_d]^4`，其 strict terminal 条件是
`(26/p)=+1`，等价 `(-26/p)=-1`。旧加号 compact form 导致的相反条件
失效；这里不靠 character 删除 `p_*`。整个 `p_*` shared-reuse candidate
仍由下节的 additive lock 独立排除。

---

<a id="a2-06-detail-src-0119-21-2"></a>
#### 后续 additive lock 为什么删除 `p_*`

较弱系统漏掉了一条后来才显式接上的信息：若 prime 属于 descendant common gcd `G_Delta`，新的 gcd theorem 同时强迫

```math
p\mid\widehat{\mathcal T}_2.
```

于是 rational-root quartic 中原本被交叉消掉的 coefficient ratio 实际必须满足

```math
\frac{Q^2N_0}{b_2^2}
\equiv
R_0(K,\zeta)
:=K^2-(18+4\zeta)K+18\zeta+55
\pmod p.
```

因此 shared outer supplier必须满足更强的

```math
\Phi_0(2)=\Phi_0(4)=0.
```

[`outer-descendant-additive-lock.md`](RESEARCH.md#a2-transport)（原始记录 SRC-0113） 对这两个式子完成 exact elimination，并证明再与 `18K-55=0` 相交后 odd primes 只剩

```math
13,\qquad1350049,
```

且两者都为 `1 mod4`。所以

```math
\boxed{
\text{genuine source-common shared outer/descendant inert pool}=\varnothing.
}
```

特别地，在旧 `p_*` residue上直接有

```math
\Phi_0(2)\not\equiv0,
\qquad
\Phi_0(4)\not\equiv0
\pmod{p_*}.
```

故 `p_*` 已严格删除，不再属于当前 A2 frontier。

---


来源：`SRC-0114:457–650`；`SRC-0119:21–134`。原文保全，当前论证以本节为准。

<a id="a2-07"></a>
### A2-07　fixed 3 的实际 depth 8/12

**状态：已严格完成。** 真实 source/sphere/plane；a2-shallow f-unit 与全部 a3-shallow，包含更深 central。

依赖：[A2-05](#a2-05)

核对：`a2-fixed3-depths`

<a id="a2-07-detail-src-0109-19-1"></a>
#### endpoint fixed-`3` dichotomy

在 `Z≡1 mod4` orientation，`endpoint-lattice.md` 已证明

```math
\boxed{
\begin{cases}
v_3(a_3)=1,\quad v_3(a_2)\ge2,\\
\text{or}\\
v_3(a_2)=1,\quad v_3(a_3)\ge2,
\end{cases}}
\tag{1.1}
```

同时

```math
3\nmid g,
\qquad
3\nmid c_u,
\qquad
3\nmid c_Q,
\qquad
3\nmid\beta.
\tag{1.2}
```

而 `primitive-reduction.md` 给

```math
\alpha=\omega W_q,
\qquad
H_0=c_uW_q,
\qquad
\beta=S\omega,
\tag{1.3}
```

其中 `3∤S` 于当前 odd-`3` channels 成立。因此

```math
\boxed{3\nmid\omega.}
\tag{1.4}
```

又由 (1.1)，原拼接分子

```math
\alpha=TK+a_3
```

恰含一个 `3`，所以

```math
\boxed{v_3(W_q)=v_3(H_0)=1.}
\tag{1.5}
```

此外 `endpoint-lattice.md` §16.58 已给

```math
\boxed{3\nmid\widehat{\mathcal T}_2.}
\tag{1.6}
```

---

<a id="a2-07-detail-src-0109-19-2"></a>
#### descendant parent 与一个新的 exact source identity

为避免与 endpoint Gaussian factors `X,Y` 混淆，本节把 descendant parent coordinates 记为

```math
\boxed{
X_d:=5^\lambda\mathscr R_{63}^\star,
\qquad
Y_d:=g2^m\widehat{\mathscr D}_{63}.}
\tag{2.1}
```

则

```math
\widehat{\mathcal T}_2=X_d+Y_d.
\tag{2.2}
```

历史 descended quotient formula 是

```math
\widehat{\mathscr D}_{63}
=c_u^2\mathscr F_{63},
\tag{2.3}
```

```math
\mathscr F_{63}
=(2K-9)B_\Delta
-\frac{63}{16}gTK^2,
\tag{2.4}
```

其中

```math
B_\Delta=g((2K-9)T-a_3)-H_0.
\tag{2.5}
```

利用

```math
H_0=c_u\frac{TK+a_3}{\omega},
\qquad
f=g\omega+c_u,
```

可得到本文使用的 exact identity：

```math
\boxed{
\omega B_\Delta
=f((2K-9)T-a_3)
-3c_u(K-3)T.}
\tag{2.6}
```

证明只是展开：

```math
\begin{aligned}
\omega B_\Delta
&=g\omega((2K-9)T-a_3)-c_u(TK+a_3)\\
&=(f-c_u)((2K-9)T-a_3)-c_u(TK+a_3)\\
&=f((2K-9)T-a_3)-3c_u(K-3)T.
\end{aligned}
```

这条式子把 fixed-`3` descendant depth 与旧 denominator factor `f` 直接接起来。

---


<a id="a2-07-detail-src-0109-481-1"></a>
#### `已严格完成`：exact sphere/plane 的新 depth `8/12`

本节使用真实减向 transport 的 `H2,H3`，完全重建上一节失效后的下一层。
记 `zeta=a3/T`，引入 `3`-unit 的有理尺度

```math
\vartheta:=\frac{c_u}{g\omega},\qquad
a:=2^mc_u^2g^2T,\qquad t:=2^{2M+2}.
```

`a` 只在本节作归一化尺度；不与 numerator digits `a2,a3` 混用。
由原 sphere、primitive plane 和 source rows，

```math
H_0^2-g^2a_3^2=c_Q^2 5^{2d}N_0,\qquad
H_0=\frac{c_uT(K+\zeta)}\omega,\qquad
Q_0=c_Qq,\qquad 5^\lambda q=g\omega-c_u,\qquad\lambda+d=m.
```

此外 endpoint (16.291) 配合 `XY=5^{-nu5}N0`、`nu5=m-3d` 给
`That_2=aR0-5^m Q0^2 N0`。于是

```math
\frac{5^mQ_0^2N_0}{a}
=\frac{(g\omega-c_u)^2}{c_u^2g^2}
 \left[\frac{c_u^2(K+\zeta)^2}{\omega^2}-g^2\zeta^2\right]
=(1-\vartheta)^2(K+\zeta)^2
 -\left(\frac{1-\vartheta}{\vartheta}\right)^2\zeta^2.
```

这条等式已经使用真实 sphere，不能换成互不相关的 parent units。
从 (2.4)–(2.5) 同时得到

```math
y:=Y_d/a=U[U-\zeta-\vartheta(K+\zeta)]-\frac{63}{16}K^2,\qquad U=2K-9,
```

```math
w:=(X_d+Y_d)/a
=R_0-(1-\vartheta)^2(K+\zeta)^2
 +\left(\frac{1-\vartheta}{\vartheta}\right)^2\zeta^2,\qquad x:=X_d/a=w-y.
```

同一归一化还直接恢复 actual quartic point：

```math
J=J_0-y/U=\vartheta(K+\zeta)-\zeta,\qquad
R=R_0-w=(1-\vartheta)^2(K+\zeta)^2
 -\left(\frac{1-\vartheta}{\vartheta}\right)^2\zeta^2.
```

代入 `Phi=J(J+2zeta)(K-J)^2-R(J+zeta)^2` 精确为零：两项都等于

```math
[\vartheta^2(K+\zeta)^2-\zeta^2]\,(1-\vartheta)^2(K+\zeta)^2.
```

因此这里的 `x,y`、四阶 hierarchy 与原十进制 coefficient plane 同源。

真实第三阶整数的同源系数为

```math
A=5^mB^2=ta,\qquad C=2^{2M+10}5^2 11=70400t,\qquad
D=2^{4M+17}5^2 11^2=24780800t^2.
```

因此定义下列整数系数多项式（checker 独立检验其 `350` 项皆在 `Z`）：

```math
P_3(K,\zeta,\vartheta):=\vartheta^6
\left[64(81xG_<+2yG_>)+70400\mathcal H_2(x,y)+24780800\mathcal H_3(x,y)\right].
```

homogeneity 给出 exact identity

```math
\mathscr N_{63}^{(3)}=T^6t^2a^3\vartheta^{-6}P_3.
```

右侧除 `P3` 外全部为 `3`-unit，故 `v3(N3)=v3(P3)`。
这只重写同一个 `N3` parent，没有新增一份独立 inert budget。

**`a2`-shallow、`3∤f`。** 此时 `K=3k`、`zeta=9z`，`k` 为 unit，
而 `f=g omega+cu` 为 unit 等价于 `vartheta=1+3h`。符号全系数核对给

```math
P_3(3k,9z,1+3h)\in3^8\mathbf Z[k,z,h],\qquad
\frac{P_3(3k,9z,1+3h)}{3^8}\equiv-k^8\pmod3.
```

`k` 为 unit 使该初项非零，因此严格得到

```math
\boxed{v_3(\mathscr N_{63}^{(3)})=8.}
```

这对任意更深 `a3` 都成立，不能用旧失效 depth `6` 替代这份重建。

**全部 `a3`-shallow。** 写 `K=9k`、`zeta=3z`，`z` 为 unit。
`k` 允许任意 residue，故包含 generic 和 deeper-central。
`3∤f` 时写 `vartheta=1+3h`，符号核对给

```math
P_3(9k,3z,1+3h)\in3^{12}\mathbf Z[k,z,h],\qquad
\frac{P_3(9k,3z,1+3h)}{3^{12}}\equiv(k+1)^4z^4+1\pmod3.
```

若 `k=-1 mod3`，右侧为 `1`；其它两类为 `2`，都非零。
`3|f` 时写 `vartheta=-1+3h`，同样有

```math
P_3(9k,3z,-1+3h)\in3^{12}\mathbf Z[k,z,h],\qquad
\frac{P_3(9k,3z,-1+3h)}{3^{12}}\equiv1\pmod3.
```

所以两种 `f` 类型统一满足

```math
\boxed{v_3(\mathscr N_{63}^{(3)})=12\quad\text{on every a3-shallow channel}.}
```

上述 `k,z,h` 的求值允许在 `Z_(3)={r/s:3∤s}`：例如 `z=a3/(9T)`、
`h=(vartheta-1)/3` 或 `(vartheta+1)/3` 通常不是普通整数。
全系数多项式恒等式、整除与 modulo `3` 初项在这个域直接保持有效。
这些是无界参数的符号多项式证明。最后只枚举 `k,z` 的三个/两个
residue 来确认显式初项非零，并未用 bounded decimal search 替代证明。


来源：`SRC-0109:19–159`；`SRC-0109:481–607`。原文保全，当前论证以本节为准。

<a id="a2-08"></a>
### A2-08　fixed 3 contact 的 orientation、eta=1 与八型

**状态：已严格完成。** eta=1 contact 排除；eta=2,e3=1 八个 positive slot；不是全候选集。

依赖：[A2-07](#a2-07)、[A2-03](#a2-03)

核对：`a2-fixed3-exceptions`、`a2-contact-slots`

<a id="a2-08-detail-src-0107-16-1"></a>
#### 记号与 third recursion

沿用 `fixed3-terminal-spill.md` 的 descendant parent coordinates

```math
X_d:=5^\lambda\mathscr R_{63}^\star,
\qquad
Y_d:=g2^m\widehat{\mathscr D}_{63},
\qquad
\widehat{\mathcal T}_2=X_d+Y_d.
\tag{1.1}
```

历史 canonical recursion 可写成

```math
\mathscr N_{63}^{(3)}=T^6\mathscr E_3,
\tag{1.2}
```

其中 `T=10^m` 为 `3`-进单位，而

```math
\boxed{
\mathscr E_3
=64A^2(81X_d\mathfrak G_<+2Y_d\mathfrak G_>)
+AC\,\mathcal H_2(X_d,Y_d;K,\zeta)
+D\,\mathcal H_3(X_d,Y_d;K,\zeta),
}
\tag{1.3}
```

这里

```math
A:=5^mB^2,
\qquad B=2^{M+m+1}c_ug,
\tag{1.4}
```

```math
C:=2^{2M+10}5^2\cdot11,
\qquad
D:=2^{4M+17}5^2\cdot11^2,
\tag{1.5}
```

而 `G_<,G_>,H_2,H_3` 均为历史 checker canonical 重建的 primitive integer forms。

因为

```math
T^6\equiv1\pmod3,
\tag{1.6}
```

`N_63^(3)` 与 `E_3` 有相同 `3`-进赋值及相同最终 normalized first digit。

---

<a id="a2-08-detail-src-0107-16-2"></a>
#### `a_3`-shallow deeper-central 时自动有 `81|Y_d`

固定

```math
\boxed{
v_3(a_3)=1,
\qquad
v_3(a_2)\ge2,
\qquad
v_3(2K-9)\ge3.}
\tag{2.1}
```

写

```math
2K-9=27r,
\qquad
\zeta:=\frac{a_3}{T}=3z,
\qquad 3\nmid z.
\tag{2.2}
```

于是

```math
K=\frac{9+27r}{2}=9\frac{1+3r}{2},
\tag{2.3}
```

所以无论 `r` 是否再被 `3` 整除，始终有

```math
\boxed{v_3(K)=2.}
\tag{2.4}
```

沿用 exact bridge

```math
\omega B_\Delta
=f((2K-9)T-a_3)-3c_u(K-3)T.
\tag{2.5}
```

由 (2.2)：

```math
(2K-9)T-a_3
=3T(9r-z),
\tag{2.6}
```

其赋值恰为 `1`；同时

```math
K-3=3\frac{1+9r}{2}
\tag{2.7}
```

也恰含一份 `3`。因此无论 `3|f` 与否，至少有

```math
\boxed{v_3(B_\Delta)\ge1.}
\tag{2.8}
```

再看

```math
\mathscr F_{63}
=(2K-9)B_\Delta-\frac{63}{16}gTK^2.
\tag{2.9}
```

第一项至少含 `3^4`；第二项中

```math
v_3(63)+2v_3(K)=2+4=6.
```

所以

```math
\boxed{v_3(\mathscr F_{63})\ge4.}
\tag{2.10}
```

进而

```math
\boxed{81\mid Y_d.}
\tag{2.11}
```

注意这里**没有**使用 `3\nmid f`。因此旧 frontier 中的 `f`-contact 与 deeper-central 一旦同时发生，仍落入同一个四层以上的 parent divisibility box。

---

<a id="a2-08-detail-src-0107-16-3"></a>
#### 关键模 `27` collapse

令

```math
X_d=x,
\qquad
Y_d=81y,
\qquad
2K-9=27r,
\qquad
\zeta=3z.
\tag{3.1}
```

把 (3.1) 直接代入 canonical forms `G_<,G_>,H_2,H_3` 与 (1.3)。checker 对全部 monomials 做 exact coefficient audit，得到：

```math
3^{10}\mid\mathscr E_3.
\tag{3.2}
```

更关键的是，除以 `3^10` 后并不是留下一个庞大的多项式。先记

```math
t:=2^{2M+2}.
\tag{3.3}
```

本通道有三个纯 source-unit congruences。

首先，因为 `81|Y_d`，模 `27` 时

```math
x\equiv\widehat{\mathcal T}_2\pmod{27}.
\tag{3.4}
```

而

```math
\widehat{\mathcal T}_2
=2^mc_u^2g^2\mathscr S_0-5^mQ_0^2N_0.
\tag{3.5}
```

当前 `v_3(a_2)>=2`，且 `C_0` 本身含 `3^2`，所以

```math
81\mid N_0=C_0^2+a_2^2.
\tag{3.6}
```

另一方面，由 `K=(9+27r)/2` 与 `a_3=3Tz`：

```math
K^2-6K+1\equiv1\pmod{27},
\qquad
18-4K\equiv0\pmod{27}.
```

于是

```math
\boxed{\mathscr S_0\equiv T\pmod{27}.}
\tag{3.7}
```

故

```math
\boxed{x\equiv2^m(c_ug)^2T\pmod{27}.}
\tag{3.8}
```

现在由 `T=2^m5^m` 与 (1.4)：

```math
A
=5^m2^{2M+2m+2}(c_ug)^2
\equiv t x\pmod{27}.
\tag{3.9}
```

另外直接计算固定系数：

```math
2^8\cdot5^2\cdot11\equiv11\pmod{27},
\tag{3.10}
```

```math
2^{13}\cdot5^2\cdot11^2\equiv11\pmod{27}.
\tag{3.11}
```

所以

```math
\boxed{C\equiv11t,\qquad D\equiv11t^2\pmod{27}.}
\tag{3.12}
```

把 (3.9)、(3.12) 一次代入 checker 重建的完整 depth-`10` normalized polynomial，125 个原 monomials 在模 `27` 下坍缩成**唯一单项式**：

```math
\boxed{
\frac{\mathscr E_3}{3^{10}}
\equiv9t^2x^3\pmod{27}.}
\tag{3.13}
```

因此

```math
\boxed{
\frac{\mathscr N_{63}^{(3)}}{3^{12}}
\equiv t^2x^3\pmod3.}
\tag{3.14}
```

而 `t` 为单位，`t^2≡1 mod3`；(3.8) 又给

```math
x\equiv2^m\equiv(-1)^m\pmod3.
\tag{3.15}
```

故最终

```math
\boxed{
\frac{\mathscr N_{63}^{(3)}}{3^{12}}
\equiv(-1)^m\not\equiv0\pmod3.}
\tag{3.16}
```

即

```math
\boxed{v_3(\mathscr N_{63}^{(3)})=12.}
\tag{3.17}
```

这是 exact equality，不是 `>=12`。

因此：

```math
\boxed{
\begin{array}{c}
v_3(a_3)=1,\ v_3(a_2)\ge2,\ v_3(2K-9)\ge3\\[1mm]
\Longrightarrow\\[1mm]
v_3(\mathscr N_{63}^{(3)})=12,
\end{array}}
\tag{3.18}
```

并且结论与 `v_3(f)` 完全无关。deeper-central fixed `3` 对 third-order positive parent只贡献偶 parity。

deeper-central 片的这个 exact even-depth 结论独立保留。旧 generic
central-depth-`2` 的 `v3(N3)=10` 已失效。新
[`fixed3-terminal-spill.md` §5](RESEARCH.md#a2-fixed3)（原始记录 SRC-0109）
独立将全部 `a3`-shallow 的赋值重建为 `12`，覆盖 central exact-depth `2`，
但不使用旧 depth `10` 路线。

---

<a id="a2-08-detail-src-0107-16-4"></a>
#### `eta=1` 唯一 odd-`3` type 中 `a_2`-shallow f-contact 不存在

这一节只处理 `eta=1`，不把它误写成任意 `eta` 的结论。

`endpoint-lattice.md` 的 Gaussian-support classification 在 `eta=1` 最终只留下五型，其中 `v_3(k_h)` 为奇数的唯一类型是

```math
\boxed{(d,c_Q,k_h,\mathrm{slot})=(2,7,3,-).}
\tag{4.1}
```

因此若再处于 `a_2`-shallow channel：

```math
v_3(a_2)=1,
\qquad
v_3(a_3)\ge2,
\tag{4.2}
```

写

```math
a:=a_2/3\in\mathbf Z_3^\times.
\tag{4.3}
```

反设

```math
3\mid f.
\tag{4.4}
```

由

```math
f=5^\lambda q+2c_u,
\qquad
Q_0=c_Qq=5^M+2^mgc_u,
\tag{4.5}
```

以及

```math
M=2m-1,
\qquad
\lambda=m-d=m-2,
\tag{4.6}
```

令

```math
s:=(-1)^m.
```

模 `3` 时 (4.4) 给

```math
q\equiv s c_u.
\tag{4.7}
```

而 `c_Q=7≡1`、`M` 为奇数，所以 (4.5) 的 `Q_0` identity 给

```math
s c_u=-1+s g c_u.
```

也即

```math
\boxed{s c_u(1-g)=-1\pmod3.}
\tag{4.8}
```

若 `g≡1`，左边为零，立即矛盾；因此

```math
\boxed{g\equiv-1\pmod3.}
\tag{4.9}
```

另一方面，negative high slot 的 exact factor equality 是

```math
\boxed{H_0-Y_2=\frac{3g^2}{2},}
\tag{4.10}
```

其中

```math
Y_2=a_2c_Q5^d.
\tag{4.11}
```

现在除以 `3` 并模 `3`。原拼接分子

```math
\alpha=TK+a_3
```

在 (4.2) 下满足

```math
\frac\alpha3\equiv a\pmod3.
\tag{4.12}
```

又

```math
H_0=c_u\frac\alpha\omega,
\qquad
f=g\omega+c_u.
```

由 (4.4)、(4.9)：

```math
\frac{c_u}{\omega}\equiv-g\equiv1\pmod3.
```

所以

```math
\boxed{H_0/3\equiv a\pmod3.}
\tag{4.13}
```

同时 `c_Q5^d=7\cdot25≡1 mod3`：

```math
\boxed{Y_2/3\equiv a\pmod3.}
\tag{4.14}
```

于是 (4.10) 除以 `3` 后左边模 `3` 为零；右边却是

```math
\frac{g^2}{2}\equiv\frac12\equiv2\pmod3.
\tag{4.15}
```

矛盾。

因此严格得到

```math
\boxed{
\eta=1,\ (d,c_Q,k_h,slot)=(2,7,3,-),\ v_3(a_2)=1
\Longrightarrow
3\nmid f.}
\tag{4.16}
```

范围更正和撤回记录见 [研究审计](RESEARCH.md#a2-retired)。

---


<a id="a2-08-detail-src-0108-9-1"></a>
#### `a_2`-shallow odd-`3` channel

固定 `Z≡1 mod4` orientation 的第二个 odd-`3` endpoint channel：

```math
\boxed{
v_3(a_2)=1,
\qquad
v_3(a_3)\ge2.}
\tag{1.1}
```

写

```math
a_2=3a,
\qquad 3\nmid a.
\tag{1.2}
```

`endpoint-lattice.md` §16.11 已严格证明

```math
\boxed{
e_3:=v_3(k_h)\in\{1,3\},}
\tag{1.3}
```

同时 sphere norm 的总 `3`-depth为 `4`。令 high-2 factor 的方向为

```math
\boxed{
H_0+\varepsilon Y_2=\frac{g^2k_h}{2},
\qquad
\varepsilon\in\{-1,+1\},}
\tag{1.4}
```

以及

```math
Y_2=a_2c_Q5^d.
\tag{1.5}
```

则另一个 low-2 factor 是 `H_0-epsilon Y_2`，两者 `3`-进深度精确为

```math
\boxed{
\bigl(v_3(H_0+\varepsilon Y_2),
      v_3(H_0-\varepsilon Y_2)\bigr)
=(e_3,4-e_3).}
\tag{1.6}
```

---

<a id="a2-08-detail-src-0108-9-2"></a>
#### 假设 `3|f` 后的两个 normalized units

现在进入旧 fixed sheet

```math
\boxed{3\mid f.}
\tag{2.1}
```

由 `primitive-reduction.md`

```math
H_0=c_uW_q,
\qquad
\alpha=\omega W_q,
\qquad
f=g\omega+c_u.
\tag{2.2}
```

当前 `a_2`-shallow channel 中

```math
\alpha=TK+a_3,
\qquad
\frac\alpha3\equiv a\pmod3,
\tag{2.3}
```

因为 `K≡a_2 mod9`、`a_3` 至少含 `3^2`，且 `T=10^m≡1 mod3`。

由 (2.1),(2.2)，`g,omega,c_u` 都是 `3`-units 且

```math
\frac{c_u}{\omega}\equiv-g\pmod3.
\tag{2.4}
```

所以

```math
\boxed{
\frac{H_0}{3}\equiv-ag\pmod3.}
\tag{2.5}
```

定义

```math
\boxed{B:=c_Q5^d.}
\tag{2.6}
```

则

```math
\boxed{
\frac{Y_2}{3}\equiv aB\pmod3.}
\tag{2.7}
```

这里 `B` 是 unit，因为 odd-`3` channel 已有 `3∤c_Q`。

---

<a id="a2-08-detail-src-0108-9-3"></a>
#### exact factor depths 决定 `epsilon B/g`

<a id="a2-08-detail-src-0108-9-4"></a>
#### `e_3=1`

此时 high-2 factor 深度为 `1`，另一个 factor 深度为 `3`。因此

```math
3^2\mid
\frac{H_0-\varepsilon Y_2}{3}.
```

特别地模 `3`：

```math
-ag-\varepsilon aB\equiv0.
```

约去 unit `a`：

```math
\boxed{\varepsilon B\equiv-g\pmod3.}
\tag{3.1}
```

<a id="a2-08-detail-src-0108-9-5"></a>
#### `e_3=3`

现在 high-2 factor 本身深度为 `3`，所以

```math
3^2\mid
\frac{H_0+\varepsilon Y_2}{3}.
```

由 (2.5),(2.7)：

```math
-ag+\varepsilon aB\equiv0,
```

即

```math
\boxed{\varepsilon B\equiv g\pmod3.}
\tag{3.2}
```

为统一记号，令

```math
\sigma=
\begin{cases}
-1,&e_3=1,\\
+1,&e_3=3.
\end{cases}
```

则 (3.1),(3.2) 可写成

```math
\boxed{\varepsilon B\equiv\sigma g\pmod3.}
\tag{3.3}
```

---

<a id="a2-08-detail-src-0108-9-6"></a>
#### source `Q_0` identity 强迫唯一 orientation

另一方面，source split 给

```math
f=5^\lambda q+2c_u,
\qquad
Q_0=c_Qq=5^M+2^mgc_u,
\qquad
\lambda=m-d.
\tag{4.1}
```

由 `3|f`：

```math
q\equiv(-1)^\lambda c_u\pmod3.
\tag{4.2}
```

代入第二式：

```math
c_Q(-1)^\lambda c_u
\equiv
(-1)^M+(-1)^mgc_u
\pmod3.
```

约去 `c_u`，再用 `lambda=m-d` 与 `B=c_Q(-1)^d`：

```math
\boxed{
B\equiv g+\delta c_u^{-1}\pmod3,}
\tag{4.3}
```

其中

```math
\boxed{
\delta:=(-1)^{M+m}=(-1)^{m-\eta},
\qquad
\eta=2m-M.}
\tag{4.4}
```

把 (3.3) 写成

```math
B\equiv\sigma\varepsilon g.
```

与 (4.3) 比较：

```math
\delta c_u^{-1}
\equiv
(\sigma\varepsilon-1)g.
\tag{4.5}
```

左边是 unit，因此右边不能为零。于是

```math
\boxed{\sigma\varepsilon=-1.}
\tag{4.6}
```

这立即给出本文主 selector：

```math
\boxed{
\begin{array}{c|c}
e_3&\varepsilon\\ \hline
1&+1\\
3&-1
\end{array}}
\tag{4.7}
```

也即

```math
\boxed{
e_3=1\Longrightarrow\text{positive high-2 slot},}
\tag{4.8}
```

```math
\boxed{
e_3=3\Longrightarrow\text{negative high-2 slot}.}
\tag{4.9}
```

所以 `f`-contact 并不是一个可同时出现在两张 Gaussian sheets 上的自由异常；它严格选中其中一张。

---

<a id="a2-08-detail-src-0108-9-7"></a>
#### 同时固定三个 source-unit phases

由 (4.6)，`sigma epsilon=-1`，所以 (3.3) 进一步给

```math
\boxed{B\equiv-g\pmod3.}
\tag{5.1}
```

而 (4.5) 化成

```math
\delta c_u^{-1}\equiv g,
```
故

```math
\boxed{gc_u\equiv\delta=(-1)^{m-\eta}\pmod3.}
\tag{5.2}
```

再由 `f=gomega+c_u≡0 mod3`：

```math
\boxed{
\omega\equiv-\delta
=(-1)^{m-\eta+1}\pmod3.}
\tag{5.3}
```

因此 general `a_2`-shallow `f`-contact 不仅选择 slot，还把

```math
(c_Q5^d,\ gc_u,\ \omega)
```

的全部 first `3`-adic unit phase固定下来。

用 `S=2^{M+m+1}gc_Q5^d`、`beta=Somega` 还可校验

```math
S\equiv\delta,
\qquad
\boxed{\beta\equiv-1\pmod3.}
\tag{5.4}
```

这与 §16.11 已有 `3∤beta` 完全一致，而不是新的矛盾；故本文不把 (5.4) 误写成 closure。

---

<a id="a2-08-detail-src-0108-9-8"></a>
#### `eta=1` 旧异常成为立即推论

`fixed3-exception-collapse.md` 中 `eta=1` 唯一 odd-`3` survivor 是

```math
(d,c_Q,k_h,slot)=(2,7,3,-).
\tag{6.1}
```

这里

```math
e_3=v_3(k_h)=1,
\qquad
\varepsilon=-1.
```

但 (4.7) 对 `e_3=1` 强迫 `epsilon=+1`。矛盾。

因此旧结论

```math
\boxed{
\eta=1,\ a_2\text{-shallow}
\Longrightarrow 3\nmid f}
\tag{6.2}
```

现在不再依赖该单点的专门 high-factor 数值 `3g^2/2`；它只是 general orientation selector 的一个特例。

---


<a id="a2-08-detail-src-0108-417-1"></a>
#### `已严格完成`：`eta=2` contact 只剩八个 positive slot 类型

固定 `eta=2m-M=2`，`m,M` 不设上界。endpoint (16.1) 给

```math
G=\frac{c_Q\chi}{w}\,2^{-3}5^{d-3},\qquad
\chi=1+H/5^{M-1}>1.
```

若 `d>=5`，由 `cQ>=3,w<843/1000` 得
`G>(3/8)5^2/(843/1000)>1212/125`，超过全部 high-2 slots，故 `d<=4`。
对 `d=1,...,4`，(16.2) 给以下严格有界的奇整数 product：

```math
16\,5^{3-d}\,s_\pm\frac{837}{1000}\frac{19}{20}
<c_Qk_h<
16\,5^{3-d}\,s_\pm\frac{843}{1000},
```

其中下/上界分别取 endpoint 的 `s±` 下/上端点：
`s- in (393/125,1607/500)`、`s+ in (2389/500,606/125)`。
逐个因子分解这些有界 products，先施加 `cQ=3 mod4`、`3∤cQ`、`5∤cQ`、
`kh` 奇与 `v3(kh) in {1,3}`，共有 `27` 个粗类型。
再施加 Gaussian norm 的严格支持条件 `5∤kh`、
`p|kh,p=3 mod4 =>p=3`，以及本文 selector，恰剩

| `d` | `(cQ,kh,slot)` |
| --- | --- |
| `1` | `(7,219,+)`, `(31,51,+)`, `(511,3,+)`, `(523,3,+)`, `(527,3,+)`, `(539,3,+)` |
| `2` | `(103,3,+)`, `(107,3,+)` |

所以这个完整无界 source family 满足

```math
\boxed{\eta=2,\ a_2\text{-shallow},\ 3\mid f
\Longrightarrow d\le2,\quad v_3(k_h)=1,\quad\varepsilon=+1.}
```

特别地，`eta=2` 的全部 negative high-2 / `e3=3` contact sheets 与全部
`d>=3` contact 已严格排除。八型的 `N3` 最终 parity、其它 `eta` 与 non-`3`
supplier 仍待证；这是有限 slot 分类覆盖无界 `m,M`，不是原候选有限枚举。


来源：`SRC-0107:16–509`；`SRC-0108:9–377`；`SRC-0108:417–460`。原文保全，当前论证以本节为准。

<a id="a2-09"></a>
### A2-09　实际 A3、shared 7 与唯一整数余数恢复

**状态：已严格完成。** 列明子片的 inert label、gcd≤11、两型真实整数核；局部 lift 可无限存在。

依赖：[A2-06](#a2-06)、[A2-08](#a2-08)

核对：`a2-contact-orientation`

<a id="a2-09-detail-src-0108-475-1"></a>
#### 作用域与唯一实际归一化

所有结果沿用 `Z=1`、`a2`-shallow f-contact 与真实 high-2 allocation；
仅 §9.5 起专门限制为 `eta=2` shared-`7` 的两个 surviving slots。
`A3` 始终指正 source 整数 `Ug omega-Kcu`，不与第三分子 `a3` 混用。

`theta=cu/(g omega)`、`a=2^m cu²g²T` 及 actual `x,y,w,J,R,P3`
的唯一完整推导在 [`fixed3-terminal-spill.md` §5](RESEARCH.md#a2-fixed3)（原始记录 SRC-0109）。
特别是 `J=J0-y/U,R=R0-w`；本文所有 prime-power evaluations 均使用该减向。
旧 plus-transport 的高阶 parity 链已降级，不能借其旧 `6/10` 初项或
quartic positive-carrier orientation 补上本节缺口，见
[`crt-descent-ledger.md` 方向审计](RESEARCH.md#a2-transport)（原始记录 SRC-0096）。
下文整数 `Theta_H=(5^(3m-3)+cQ cu)/g` 与这个有理 `theta` 是不同对象。
所有 parent 与 source carrier 都接回同一十进制 coefficient plane；
没有因改写 hierarchy 而新增独立高度预算。

<a id="a2-09-detail-src-0108-475-2"></a>
#### source 奇数因子及与 `pC` 的分离

沿用 `fixed3-terminal-spill.md` 的正整数
`A3=Ug omega-Kcu`，本节仍在 `Z=1`、`a2`-shallow f-contact 及真实 high-2 allocation。
原 endpoint 的 `Wq=3Z mod4`、`H0=cu Wq`、`cu=1 mod4` 给 `H0=3 mod4`。
又 `B=cQ5^d=3 mod4`，而 high factor `H0+epsilon Y2=g^2 kh/2` 被 `8` 整除，
所以

```math
e_3=1,\ \varepsilon=+1\Longrightarrow a_2\equiv3\pmod4,\qquad
e_3=3,\ \varepsilon=-1\Longrightarrow a_2\equiv1\pmod4.
```

`omega` 为 odd，因为它整除 odd 拼接分子 `alpha=TK+a3`。
`K=9*10^M+10a2`、`M>=11` 给 `K/2=a2 mod4`，`U=3 mod4`。
`g=2^(t-1)rho`、`t>=3` 给 `v2(g)>=2`。因此

```math
\frac{\mathscr A_3}{2}
\equiv U\frac g2\omega-\frac K2c_u\pmod4
\in\{1,3\},\qquad v_2(\mathscr A_3)=1.
```

它等于 `3 mod4` 恰在以下两片：

```math
\bigl(v_2(g)=2,\ e_3=1,\varepsilon=+1\bigr)
\quad\text{or}\quad
\bigl(v_2(g)\ge3,\ e_3=3,\varepsilon=-1\bigr).
```

设其中一片还满足 `v3(A3)` 为偶数。除去全部 binary 与 `3` content 的正整数

```math
\mathscr A_3^\circ:=\frac{\mathscr A_3}{2\,3^{v_3(\mathscr A_3)}}
\equiv3\pmod4,\qquad\gcd(\mathscr A_3^\circ,6)=1
```

必含某枚 `r!=3,r=3 mod4` 到奇数次。这是一个实际 source carrier 的
parity consequence。特别在 `v3(A3)=2` 时，`N3` 的 depth `9` 可由 fixed `3`
支付，但上述片仍另外强迫一枚 non-`3` inert supplier。`eta=2` 的八型中全为
`e3=1/+`，所以 `v2(g)=2,v3(A3)=2` 给这一完整无界子片的 surcharge。
没有把 `N3` 和 `A3` 自动视为两份独立高度预算。

**与 `pC` 分离。** 在 genuine external shared-outer / descendant 的唯一
`pC=24303427940647` 点，
`K=21805672591624,zeta=9250192938088 mod pC`。
真实 `F=0` 给 `J=J0`；上一专题的 actual source identity 给

```math
\vartheta=\frac{J_0+\zeta}{K+\zeta}
\equiv18367788003561\pmod{p_C},\qquad
\frac{\mathscr A_3}{g\omega}=U-K\vartheta
\equiv11023269555785\not\equiv0\pmod{p_C}.
```

checker 同时核对该 `vartheta` 在真实 `y,w` 归一化上为零。
依赖 [`outer-external-q4-root-split.md`](#a2-06)
的共同点唯一性与 genuine unit 假设，严格得到 `pC∤A3`。
因此本节强迫的 `r` 必与 terminal label `pC` 不同；尚未证明它与全部其它 old pools 分离。

<a id="a2-09-detail-src-0108-475-3"></a>
#### prime-power gcd 与 height 接口

primitive source 已给
`gcd(cu,qf g omega)=1`。令 `D3=2g omega-cu`，则

```math
\begin{aligned}
\gcd(\mathscr A_3,q)&=\gcd(q,K-9),\\
\gcd(\mathscr A_3,f)&=\gcd(f,3(K-3)),\\
\gcd(\mathscr A_3,\omega)&=\gcd(\omega,K),\\
\gcd(\mathscr A_3,g)&=\gcd(g,K).
\end{aligned}
```

第一式用 `g omega=5^lambda q+cu`；第二式用 `g omega=f-cu`；
后两式直接模 `omega,g`。这些是完整 prime-power gcd 等式。
还有

```math
\mathscr A_3=KD_3-9g\omega,\qquad
\gcd(D_3,g\omega)=1,\qquad
\gcd(\mathscr A_3,D_3)=\gcd(9,D_3)\mid9.
```

令 third-block 整数 `H_A=9Tg omega+D3 a3`；exact Euclidean identity 为

```math
D_3\alpha-T\mathscr A_3=\mathscr H_A.
```

所以对每个 `p∤30`，`D3,T` 在 `p|A3` 时均为 units，

```math
\min\{v_p(\mathscr A_3),v_p(\alpha)\}
=\min\{v_p(\mathscr A_3),v_p(\mathscr H_A)\}.
```

任何 non-`3` inert height prime `r|Wq,A3` 还满足 `r∤omega`：
否则第三个 gcd 式给 `r|K`，`alpha=omega Wq` 给 `r|a3`，`H0=cu Wq` 与
sphere 给 `r|N0`；惰性 norm 再给 `r|b2`，与 height theorem 的
`r∤gcu cQ` 矛盾。因此这里的 height overlap 被同一个 `H_A` 逐 prime-power 读取。

<a id="a2-09-detail-src-0108-475-4"></a>
#### 固定支持界

<a id="a2-09-detail-src-0108-475-5"></a>
#### 共同 saturation 的单层 `11` 上界

本节的实际 source normalization
还给出一个覆盖无界参数的完整 gcd 结论。令

```math
G_A:=\gcd(\mathscr A_3,\widehat{\mathcal T}_2,\mathscr L_{23},qf),
\qquad \mathscr L_{23}=9T/2+a_3.
```

在当前 `Z=1,a2`-shallow f-contact 中，primitive additive carrier
`That2` 为 `2,5` 单位；`K,zeta=0 mod3` 与 `theta=-1 mod3` 又使
`w=That2/a=55=1 mod3`。因此 `gcd(G_A,30)=1`。
对任意 `p∤30`，设 `p^j|G_A`。primitive 假设使
`a=2^m cu²g²T`、`g omega`、`cu` 均为 `p`-进单位。
由于 `gcd(q,f)=1`，完整 `p^j` 必落在其中一侧。
`q` 侧给 `theta=1 mod p^j,K=9 mod p^j`；`f` 侧给
`theta=-1 mod p^j,K=3 mod p^j`。真实减向表达式满足

```math
\begin{aligned}
w(K,\zeta,1)=-26-18\zeta+(K-9)(K-9-4\zeta),\\
w(K,\zeta,-1)=-26-18\zeta-3(K-3)(K+9+4\zeta).
\end{aligned}
```

`p^j|L23` 给 `zeta=-9/2 mod p^j`，而 `p^j|That2` 给 `w=0`。
两侧都得到 `p^j|55`。故

```math
\boxed{G_A\mid11.}
```

这只限制所列四对象的共同 saturation，不是整个 `qf` 池的支持结论。
该唯一一层还不能进入 descendant common：在两种 `11` 点，真实
`y=Yd/a` 分别等于

```math
y(9,-9/2,1)=-3^4\,47/16\equiv2\pmod{11},\qquad
y(3,-9/2,-1)=-3^4\,7/16\equiv1\pmod{11}.
```

上述 `16,a,g omega,cu,T` 在 `11` 上均为单位；
`GDelta|widehat D63`、`Yd=g 2^m widehat D63` 因而与这些单位值矛盾。
结合 `GDelta|That2`，严格得到

```math
\boxed{\gcd(\mathscr A_3,\mathscr L_{23},qf,G_\Delta)=1.}
```

所以本文 source surcharge 的 non-`3` supplier 无法同时复用完整
denominator saturation 与 descendant common。未饱和的 `q/f` 接触、
仅单侧 outer、height overlap 等仍不受这个四对象结论自动排除。

<a id="a2-09-detail-src-0108-475-6"></a>
#### 未饱和 denominator / descendant 交集

不加 `L23` 条件仍有严格
的固定支持上界。若 `p∤30`、`p^j|A3,q,GDelta`，上述单位推导使
`K=9,theta=1 mod p^j`。由 `GDelta|That2,Yd`，真实 `w,y` 都为零，
而它们的差在该 source sheet 上恒为

```math
y(9,\zeta,1)-w(9,\zeta,1)=-4687/16=-43\cdot109/16.
```

若 `p^j|A3,f,GDelta`，则 `K=3,theta=-1 mod p^j`，
`y(3,zeta,-1)=-567/16=-3^4\cdot7/16`。结合当前 `GDelta` 为 `30` 单位，得

```math
\boxed{\gcd(A3,q,G_\Delta)\mid43\cdot109,\qquad
       \gcd(A3,f,G_\Delta)\mid7.}
```

两侧 surviving depth 都至多一层。`109=1 mod4` 不供应 inert parity。
`q` 侧还由 `w=0` 得 `zeta=-13/9`；此时 `R0=0`，实际 outer evaluations 为

```math
\Phi_2=-784/9,\qquad \Phi_4=1000/9.
```

它们在 `43,109` 上都为单位。因此 `A3` 的 `q`-side descendant overlap
不能同时支付任何一侧 outer cofactor。`f` 侧的 `7` 点为
`(K,zeta,theta)=(3,4,-1) mod7`；两 outer values 确实都为零。
这只是必要源值兼容，不能把该点写成 Exact Lift 解，也不能套用旧
fixed-`7` label 的 `K=1` 排除；它是不同的 residue sheet。

<a id="a2-09-detail-src-0108-475-7"></a>
#### 真实 height / descendant 交集

只对本文强迫的 non-`3` inert prime
读取 height。设
`j=min(vp(A3),vp(Wq),vp(GDelta))>=1`。
前述 height lemma 已给 `p∤omega`，且 `p∤30gcu`，所以
`alpha=omega Wq` 使 `zeta=-K mod p^j`。
`A3=0` 给 `theta=U/K mod p^j`；`K,U` 也都是单位。
在真实 source sheet 上精确有

```math
y(K,-K,U/K)=\frac3{16}\mathcal Y_A(K),\qquad
w(K,-K,U/K)=\frac{\mathcal W_A(K)}{U^2},
```

```math
\begin{aligned}
\mathcal Y_A&=11K^2-240K+432,\\
\mathcal W_A&=21K^4-342K^3+2002K^2-4896K+4455.
\end{aligned}
```

两者的整数 Bezout identity 为

```math
\begin{aligned}
&(1999434528K^3-28611870921K^2+133944686430K-202282077546)\mathcal Y_A\\
&\quad +(20781450135-1047322848K)\mathcal W_A
=3^{10}\cdot7\cdot12569471.
\end{aligned}
```

因此完整 prime-power 共深度只可能为 `p=7` 或 `p=12569471`，且 `j<=1`；
后者也是 `3 mod4` 的素数，checker 在确定性范围内核验素性。
在 `12569471` 的唯一共同点，`K=-267471,zeta=267471`，`U` 为单位，
`Phi2=12143998,Phi4=4798615 mod p`，故它不能支付任一 outer cofactor。
在 `7` 的唯一共同点仍是上述 `(3,4,-1)`，局部源值兼容而未关闭。
这些结论只限制 inert part 的 `A3/Wq/GDelta` 共同层；不能对所有
`p|alpha` 忽略 `omega` content，也不排除只有 height、没有 descendant
的 supplier。把 source、height、descendant 及 outer 两侧同时复用的
剩余必要标签现已压成该单层 `7` sheet，不能据此新增一份高度预算。

<a id="a2-09-detail-src-0108-475-8"></a>
#### 允许的 shared-`7` sheet

<a id="a2-09-detail-src-0108-475-9"></a>
#### `eta=2` 的两个 slot

将上述实际
`K=3,zeta=4,theta=-1 mod7` 与原 prefix、sphere 和 high-factor rows
联立。所有幂的模 `7` 周期整除 `6`，所以只需完整审计
`m mod6` 以及 `cu,g` 的全部 `7`-进单位。令 `M=2m-2,lambda=m-d`，
使用的必要原式是

```math
\begin{gathered}
a_2=(3-9\,10^M)/10,\qquad a_3=-3\,10^m,\qquad
b_2=2^{M+m+1}c_ug,\\
q=-2c_u5^{-\lambda},\qquad
c_Qq=5^M+2^mc_ug,\\
(c_Q5^d)^2[(9b_2/2)^2+a_2^2]+g^2a_3^2=0,\qquad
c_Q5^d a_2=g^2k_h/2\pmod7.
\end{gathered}
```

其中最后一式用 `eta=2` 已证明的 positive high-2 orientation；
球面式用 `H0=cu Wq=0`。对 §8 的八个 slot，这个完整单位审计
只剩以下四个必要 states（所有表项除 `m` 外均为模 `7`）：

| `(d,cQ,kh)` | `m mod6` | `(cu,g,a2,a3)` |
| --- | --- | --- |
| `(1,31,51)` | `2` | `(4,4,2,1)` |
| `(1,31,51)` | `5` | `(3,3,2,6)` |
| `(1,527,3)` | `2` | `(6,5,2,1)` |
| `(1,527,3)` | `5` | `(1,2,2,6)` |

所以其余六个 `eta=2` contact slot 以及这两型的 `m!=2 mod3`，
都不能复用 `A3/Wq/GDelta` 的单层 `7` 来同时支付 outer parity。
这是周期性必要条件覆盖无界 `m,M`，不是完整 Exact Lift 解枚举。
四个 remaining local states 和不作此共同复用的 carriers 仍待证。

<a id="a2-09-detail-src-0108-475-10"></a>
#### 原 source 的无限 `7`-进 lift

这个
边界可以用无界局部构造证明。固定两种 surviving slot 与任意
`m>=7,m=2 mod3`，取 `M=2m-2`、`B=cQ5^d`，并把 positive high-factor
代入原式，得到三个整数多项式

```math
\begin{aligned}
F_Q&=B(g\omega-c_u)-5^{M+m}-10^mc_ug,\\
F_P&=\omega(g^2k_h-2Ba_2)-2c_u[10^mK+a_3],\\
F_S&=(g^2k_h-2Ba_2)^2-4g^2a_3^2-B^2(81b_2^2+4a_2^2),
\end{aligned}
```

这里 `K=9*10^M+10a2,b2=2^(M+m+1)cu g`。
固定 `cu,g` 为各自允许的 `7`-进单位，以 `(omega,a2,a3)` 为未知。
上述四个 base states 的 Jacobian determinant 分别为 `3,3,4,4 mod7`；
故多变量 Hensel lemma 给每个 base state 唯一的无限 source lift。

checker 还完整审计 `m mod42`（全部模 `49` 幂的周期）及
`cu=cv+7dc,g=gv+7dg` 的 `49` 对首 lift digits。每个 slot / exponent phase
都至少有 `17` 个 lifts，使

```math
v_7(A3)=v_7(Wq)=v_7(That2)=v_7(Yd)
=v_7(\Phi_2^{actual})=v_7(\Phi_4^{actual})=1.
```

`Phi_j^actual` 此处使用真实 `R=R0-w`，不是把 `R0` 继续代到模 `49`。
单位尺度使 `v7(GDelta)=1`；`Jsource=3 mod7` 又给 `C=0 mod7`，
而 `D=2^m5^d g` 为单位，所以两个 outer denominators `D±C` 也为单位。
因此这些 lifts 同时保持真实两个 outer cofactors 的 `7` 深度为奇数 `1`。
同一光滑 chart 可无限提升，所有已经核验的 depth-`1` 值在提升后仍为 `1`。
这证明单独的 `7`-进 source/sphere/plane 与这些 carrier parity
相容，不证明正整数 decimal window、全局 prime support 或 Exact Lift 解存在。
若要关闭这张 sheet，必须再使用这些局部条件尚未控制的真实整数/位数或
其它 source allocation；不能把单层共深度或下一字层枚举改写成不存在性。

<a id="a2-09-detail-src-0108-475-11"></a>
#### 同源 `N3` 的下一字层与 odd-depth lift

使用 `fixed3-terminal-spill.md` §5 的唯一
实际 `P3`，令

```math
K=3+7k_7,\qquad\zeta=4+7z_7,\qquad\vartheta=-1+7h_7,\qquad
V_7:=k_7+z_7+1=\frac{\alpha}{7T}\pmod7.
```

在本节单位范围内 `N3` 与 `P3` 的 prefactors 均为 `7` 单位。
完整整数多项式展开严格给

```math
P3/7^2\equiv h_7^2-2V_7^2
=(h_7-3V_7)(h_7+3V_7)\pmod7.
```

两种 `eta=2` slot 的完整 source 三行首阶展开又给
`h7-3V7=5m mod7`；checker 对全部 `m mod42` 先作符号线性化，
然后审计所有 free first digits。因此

```math
\boxed{P3/7^2\equiv2m(V_7+2m)\pmod7.}
```

若 `7∤m` 且 `V7!=-2m mod7`，就有 exact depth `v7(N3)=2`，
该完整无界 word 子片不由 `7` 支付 third parity。
若 `7|m` 或 `V7=-2m`，仅凭这个初项得到 depth 至少 `3`；
不能把 zero digit 当作 odd 或 even。`V7` 是真实 height word，
没有为它新增独立预算。局部 `7` source compatibility 与全局整数关闭
仍必须区分。

进一步对完整 source 行作下一次 Hensel lift，得一个严格的局部奇数深度证书。
设 `m=14 mod21`，即当前允许相位且 `7|m`。checker 遍历 powers 模 `343`
的完整共同周期 `m mod294`，每型的 `14` 个 exponent phases，以及
`cu=cv+7dc,g=gv+7dg` 的 `49` 对首 digits；更高 free digits 暂取零，
三个 implicit variables 唯一提升到模 `343`。每型、每相位有
`12`–`17` 个已核验点同时满足

```math
v_7(A3)=v_7(Wq)=v_7(That2)=v_7(Yd)
=v_7(\Phi_2^{actual})=v_7(\Phi_4^{actual})=1,
\qquad v_7(N3)=3.
```

最后的 exact `3` 来自完整 `350` 项 `P3` 模 `2401` 的非零值，
不是首项为零后的 parity 猜测。由于 universal sheet expansion 整除 `49`，
`(K,zeta,theta)` 的模 `343` 值已确定 `P3 mod2401`：三个 sheet coordinates
模 `49` 的更高变化给 `P3` 的变化整除 `49²`。因此这些点的无限 source
Hensel extensions 保持上述全部 exact depths。这里显示 `7` 确可在当前
source chart 局部承担 odd third parity；仍未控制全局正窗口、整数恢复和
prime support，不能据此宣称 Exact Lift 解存在。

<a id="a2-09-detail-src-0108-475-12"></a>
#### 剩余两型的真实整数核

这一步只专门化既有 source identities，
不增加 product budget。两型均为 `d=1,cQ kh=1581`。给定 `m,cu`，

```math
M=2m-2,\quad T=10^m,\quad N=10^M,\quad B=5c_Q,
\quad b_3=B\,2^{3m-1}c_u,
```

```math
\frac{2(837/1000)}{5c_Q}(5/4)^m<c_u
<\frac{2(843/1000)}{5c_Q}(5/4)^m.
```

原整数 source quotient（不同于 `vartheta=cu/(g omega)`）为

```math
\Theta_H=\frac{5^{3m-3}+c_Qc_u}{g}\in\mathbb Z_{>0},\qquad
\omega=\frac{\Theta_H+2^m5^{m-1}c_u}{c_Q}\in\mathbb Z_{>0}.
```

所以只需考虑 `5^(3m-3)+cQ cu` 的正除数 `g`，并核对 `omega` 的整性。
`b2=2^(3m-1)cu g`；实际 positive high-factor window 还给
`2389/(250kh)<g/T<1212/(125kh)`。
令两个实际整数

```math
\mathcal L:=B\omega+10c_uT,\qquad
\mathcal E:=\frac{\omega g^2k_h}{2}-9c_uTN.
```

直接展开原 concatenation plane 得
`E-L a2=cu a3`，符号为减号。
source 的 `20<cQ omega/(2^m5^(m-1)cu)<21` 又给
`30cuT<L<31cuT`。把 `E-cuT` 作普通 Euclidean division：

```math
\mathcal E-c_uT=\mathcal L Q_E+R_E,\qquad 0\le R_E<\mathcal L.
```

真实 `1<a3/T<251/250` 严格等价于本次恢复所需的

```math
\boxed{a_2=Q_E,\quad 0<R_E<c_uT/250,\quad c_u\mid R_E,
\quad a_3=T+R_E/c_u.}
```

若 quotient 不等于 `a2`，相邻整数会把 `a3` 移动超过 `30T`，
所以没有第二个 numerator candidate。sphere 剩下一个精确整数核对：

```math
\boxed{k_h^2g^2=81b_3^2+4a_3^2+4k_hBa_2.}
```

最后仍须检查 numerator/denominator digit windows、既约性和本节
carrier valuations。每个 `(m,cu,g)` 至多恢复一组 `(a2,a3)`；
`m` 无上界，不能因每个固定参数只有有限 candidates 就宣称 A2 有限或为空。

在实际 surcharge 子片 `v2(g)=2`，source mod `8` 给
`cu=5^m mod8`。联立已证明的 `3` 与 `7` phase 后，完整必要 CRT 表为

| `(cQ,kh)` | `m mod6` | `cu mod168` | `g mod168` |
| --- | --- | --- | --- |
| `(31,51)` | `2` | `25` | `4` |
| `(31,51)` | `5` | `101` | `52` |
| `(527,3)` | `2` | `41` | `68` |
| `(527,3)` | `5` | `85` | `44` |

这个表与严格 `cu` interval、`5∤cu` 及 `cu` 只含 `1 mod4` 素因子相交，
给有限参数证书：第一型所有 `7<=m<68`、第二型所有 `7<=m<80`
都没有可能的 `cu`。首个 interval/unit survivors 分别是
`(m,cu)=(68,42193)` 与 `(80,35993),(80,36161)`；它们尚未通过上述
divisor、remainder、sphere 等检查，不能称为 Exact Lift candidates。
这个 lower-length certificate 不为无界 `m` 提供上界。

<a id="a2-09-detail-src-0108-475-13"></a>
#### 实际 fixed-`3` word 与剩余 parity 供应

上述精确 sphere 取消式
还控制真实 shallow prefix。写 `kh=3kappa,a2=3A2`，并用 `9|a3`；
除去共同 `9` 后模 `3` 得

```math
\kappa^2g^2=\kappa BA_2\pmod3.
```

对 `(31,51)` 与 `(527,3)`，均有 `kappa B=1 mod3`，且 `g²=1 mod3`，
所以严格强迫

```math
\boxed{k_3:=K/3\equiv a_2/3\equiv1\pmod3.}
```

这不是重新分配一份 source budget。将这个真实 prefix word 代入
`fixed3-terminal-spill.md` §6 已核验的 collision form，令
`r3=A3/(27g omega)`，两型的完整 fixed-`3` 状态为

| 实际 `A3` 状态 | `v3(N3)` | `3` 能否供应 odd parity |
| --- | --- | --- |
| `v3(A3)=2` | `9` | 可以 |
| `v3(A3)=3,r3=2 mod3` | `10` | 不可以 |
| `v3(A3)=3,r3=1 mod3` | 由下一初项决定 | 见下式 |
| `v3(A3)>=4` | `10` | 不可以 |

理由是 corrected depth-`10` 初项在 `k3=1` 时就是 `1-r3`，与
`a3/(9T)` 的更深 word 无关。在 `r3=1 mod3` 上写
`k3=1+3j,r3=1+3s,z=a3/(9T)`，同源完整 `P3` 再给

```math
N_3/3^{11}=\text{unit}\cdot[1-s+z(j-1)]\pmod3.
```

括号非零时 exact depth 为 `11`，仍供应 odd parity；为零时只能记
`v3(N3)>=12`。完整全系数推导集中在
[`fixed3-terminal-spill.md` §6](RESEARCH.md#a2-fixed3)（原始记录 SRC-0109）。
特别地，完整无界子片

```math
v_3(A3)\ge4,\qquad7\nmid m,\qquad V_7\not\equiv-2m\pmod7
```

同时有 `v3(N3)=10,v7(N3)=2`。方向审计已证明正第三阶 carrier
`-N3` 去除 binary/`5` content 后为 `3 mod4`；这些偶数 `3,7` 深度
不能支付它的 inert parity。因此该子片必有一枚
`ell=3 mod4,ell!=3,7` 到奇数次。它是与 shared-`7` 不同的供应标签，
尚未证明与全部其它 pools 分离，也不自动新增独立 height budget。

<a id="a2-09-detail-src-0108-475-14"></a>
#### 原 source 的无限 `3`-进 lift

只对这两个 `d=1` 型，
写 `a2=3A,a3=9Z,kh=3kappa,B=5cQ`，原 §9 的三行精确约成

```math
\begin{aligned}
B(g\omega-c_u)-5^{3m-2}-Tc_ug&=0,\\
\omega(\kappa g^2-2BA)-2c_u[T(3N+10A)+3Z]&=0,\\
\kappa^2g^2-4\kappa BA-9b_3^2-36Z^2&=0,\qquad
b_3=B2^{3m-1}c_u.
\end{aligned}
```

第二行从原 plane 除 `3` 得到，第三行从原 sphere 除 `9g²` 得到，
不是独立的 projective approximation。模 `3` 的唯一单位 base 为
`g=-B,cu=(-1)^m/g,omega=-(-1)^m,A=1`，而 `Z` 自由。
固定 `(g,Z)`、以 `(omega,A,cu)` 为 implicit variables 时，Jacobian 为

```math
\begin{pmatrix}-1&0&0\\-B&(-1)^mB&1\\0&-1&0\end{pmatrix}\pmod3,
\qquad\det=-1.
```

因此每个已核验 source 点均能 Hensel 提升到任意 `3`-进深度。
checker 完整遍历 `m mod18` 的六个允许相位、`g mod81` 的 `27` 个
允许类以及 `Z mod81` 的 `81` 类；原 powers 模 `81` 的共同周期为 `18`。
每个型、每个相位的 `2187` 个 source 点均分为

| 实际 `N3` 初项状态 | 数量 |
| --- | ---: |
| exact depth `9` | `1458` |
| exact depth `10` | `486` |
| depth-`11` 初项为 `1` | `81` |
| depth-`11` 初项为 `2` | `81` |
| depth 至少 `12` | `81` |

这证明上述原 source 行的 `3`-进必要条件不能统一消去 fixed-`3` odd supplier。
它只给局部 source 兼容点，未满足十进制正窗口、global prime support、
整数 divisor/remainder 等条件，不能称为 Exact Lift 解。

<a id="a2-09-detail-src-0108-475-15"></a>
#### 尚未关闭的核心

这些接口把新 supplier 接回 q/f/content/height 的真实对象，但不使它们自动为空。
`H_A` 的定义本身不提供统一 height drop 或额外 product budget。
尚缺这些 carriers 的 source support 或 product-height 的统一排除；A2 仍为 `待证`。


来源：`SRC-0108:475–1027`。原文保全，当前论证以本节为准。

<a id="dd"></a>
## DD 分支

<a id="dd-01"></a>
### DD-01　原 DD gap、surplus 与相对尾长基线

**状态：已严格完成。** DD 原 word/sphere 的必要系统；不把相对锥误作全局有限盒。

依赖：[C01](#c01)、[C03](#c03)

核对：正文推导；本次重写未为此项另增枚举。

<a id="dd-01-detail-src-0122-12-1"></a>
#### Double-deficit 分支：公共商正规化

DD 统一记

```math
\boxed{
d_3=s_3>0,
\qquad
k_{12}=s_2+s_3>0.
}
```

令

```math
T=10^{m_3},
```

```math
A=10^{m_2}b_1,
\qquad
B=b_2,
```

以及球面 gap

```math
\boxed{
e=H-y_3>0.
}
```

定义前两 ghost 平方和

```math
\boxed{
\mathcal S_{12}=y_1^2+y_2^2.
}
```

定义 DD 线性组合

```math
\mathcal M
=
10^{k_{12}}Ay_1
+
10^{d_3}By_2,
```

以及

```math
\mathcal G
=
\mathcal M-(A+B)H.
```

exact balance 可化为

```math
\boxed{
T\mathcal G=b_3e.
}
```

令

```math
\omega=\gcd(T,b_3),
\qquad
L=T/\omega,
\qquad
\tau=b_3/\omega.
```

则存在唯一正整数 \(a\) 使

```math
\boxed{
e=La,
\qquad
\mathcal G=\tau a.
}
```

由于球面恒等式

```math
(H-y_3)(H+y_3)
=
\mathcal S_{12},
```

有

```math
\boxed{
La\mid\mathcal S_{12},
}
```

并且

```math
\boxed{
H
=
\frac12
\left(
La+\frac{\mathcal S_{12}}{La}
\right),
}
```

```math
\boxed{
y_3
=
\frac12
\left(
\frac{\mathcal S_{12}}{La}
-La
\right).
}
```

因此固定 ghost \((y_1,y_2)\) 与正规化参数后，第三坐标只可能来自 \(\mathcal S_{12}\) 的有限除数。

这解决了“第三块是否还存在独立连续缩放自由度”的问题：没有。

真正的无界性来自前两 ghost 本身。

---

<a id="dd-01-detail-src-0122-12-2"></a>
#### DD 的判别平方与斜率锁

DD 的恢复方程可整理出平方判别条件

```math
\boxed{
LJ=W^2.
}
```

实际根甚至进一步满足

```math
\boxed{
W=L\Xi,
\qquad
J=L\Xi^2,
}
```

其中

```math
\Xi=
|\mathcal M-C_0a|
```

为显式整数。

另一方面由

```math
\frac{\mathcal G}{e}
=
\frac{\tau}{L}
```

得到斜率锁

```math
\boxed{
\frac1{10}
\le
\frac{\tau}{L}
<1.
}
```

这说明 DD 的尾 gap 与尾分母始终处在一个固定十倍窗口。

---

<a id="dd-01-detail-src-0122-12-3"></a>
#### DD 的 surplus simplex

定义总前两分母位数尺度

```math
\boxed{
S_{12}=m_1+m_2.
}
```

利用第一 denominator weight 在总权重中的固定占比，对 exact weighted average 做尺度比较，可以得到

```math
\boxed{
s_1+s_2+d_3
-
\max(s_1,s_2,d_3)
\le2.
}
```

因此 DD 被切成三个很薄的扇区：

```math
\boxed{
\begin{array}{c|c}
s_1=\max&s_2+d_3\le2\\
s_2=\max&s_1+d_3\le2\\
d_3=\max&s_1+s_2\le2
\end{array}
}
```

两个非 \(d_3\)-dominant 扇区都满足

```math
\boxed{
n_3\le7S_{12}+4.
}
```

所以一旦

```math
n_3>7S_{12}+4,
```

就必须进入

```math
\boxed{
d_3=\max(s_1,s_2,d_3).
}
```

这把真正可能无界的 DD 候选集中到第三分子 surplus 主导的一个扇区。

---

<a id="dd-01-detail-src-0122-12-4"></a>
#### DD 的 near-square 结构

定义普通前两分子拼接

```math
\boxed{
A_{12}
=
a_1 10^{n_2}+a_2.
}
```

从 exact lift 关于 \(a_3\) 的二次方程出发，其判别平方可写成

```math
\boxed{
Y^2
=
X^2
-
\mathcal N_{12}
10^{m_3}Q
\left(
10^{m_3}Q+2b_3
\right),
}
```

其中

```math
\boxed{
X=GA_{12}10^{n_3}.
}
```

所以

```math
\boxed{
(X-Y)(X+Y)
=
\mathcal N_{12}
10^{m_3}Q
(10^{m_3}Q+2b_3).
}
```

由于 \(X,Y\) 为正整数，两个不同平方之间至少相差

```math
2X-1.
```

因此得到

```math
\boxed{
2GA_{12}10^{n_3}-1
\le
\mathcal N_{12}
10^{m_3}Q
(10^{m_3}Q+2b_3).
}
```

粗化后得到

```math
\boxed{
n_3
\le
2m_3
+
3S_{12}
+
|s_1-s_2|
+1.
}
```

从而

```math
\boxed{
d_3
\le
m_3
+
3S_{12}
+
|s_1-s_2|
+1.
}
```

---

<a id="dd-01-detail-src-0122-12-5"></a>
#### DD 的 squarefree gap 加强

写

```math
\kappa=s_\kappa q_\square^2,
```

其中 \(s_\kappa\) 为平方自由部分。

统一判别平方要求 \(W\) 被 \(q_\square\) 整除。因此小平方差因子不能只用“至少为 1”，而至少包含平方部分带来的额外离散尺度。

由此可加强为

```math
\boxed{
10^{d_3}A_{12}
<
40Q^2\mathcal N_{12}.
}
```

按位数估计：

```math
\boxed{
d_3
\le
3S_{12}
+
|s_1-s_2|
+2.
}
```

在 \(d_3\)-dominant 扇区中

```math
|s_1-s_2|
\le
2(S_{12}-1),
```

所以

```math
\boxed{
d_3\le5S_{12}.
}
```

结合统一 denominator-tail cone，

```math
m_3\le6S_{12}+3,
```

得到

```math
\boxed{
n_3=m_3+d_3
\le11S_{12}+3.
}
```

这已经把 DD 的所有第三块位数压入一个显式线性锥。

---

<a id="dd-01-detail-src-0122-12-6"></a>
#### DD 的 \(2\)-进与 \(5\)-进双 resonance

near-square 的两个正因子可以写成

```math
F_-=
\frac{2(\kappa+2G)\mu^2}{G_0},
```

```math
F_+=
\frac{2\kappa\mathcal N_{12}\nu^2}{G_0},
```

并且

```math
\boxed{
F_-+F_+
=
2GA_{12}10^{n_3}.
}
```

对 \(p=2,5\)，若记

```math
r_p=v_p(\mu),
\qquad
s_p=v_p(\nu),
```

```math
k_p=v_p(\kappa),
\qquad
f_p=v_p(\kappa+2G),
```

```math
n_p=v_p(\mathcal N_{12}),
\qquad
c_p=v_p(G_0),
```

则

```math
v_p(F_-)
=
v_p(2)+f_p+2r_p-c_p,
```

```math
v_p(F_+)
=
v_p(2)+k_p+n_p+2s_p-c_p.
```

如果两边赋值不同，那么和的 \(p\)-进深度只能等于较小者，无法支持极长的十进制尾零。

因此足够大的 \(n_3\) 必须发生精确 resonance：

```math
\boxed{
f_p+2r_p
=
k_p+n_p+2s_p.
}
```

具体已经得到：

```math
\boxed{
d_3=\max,\ n_3\ge9S_{12}+2
\Longrightarrow
5\text{-adic resonance},
}
```

以及

```math
\boxed{
d_3=\max,\ n_3\ge10S_{12}+11
\Longrightarrow
2\text{-adic resonance}.
}
```

所以在最顶部区域

```math
\boxed{
n_3\ge10S_{12}+11
}
```

时，\(2\) 与 \(5\) 两处必须同时 resonance。

约掉共同赋值以后，还会留下深 Hensel 相位

```math
\boxed{
\mu_p
\equiv
\pm\rho_p\nu_p
\pmod{p^{R_p}}.
}
```

特别是 \(5\)-进剩余深度满足近似下界

```math
R_5>1.415S_{12}+9.
```

这意味着模数

```math
5^{R_5}
```

已经接近十进制尺度 \(10^{S_{12}}\)。

---

<a id="dd-01-detail-src-0122-12-7"></a>
#### DD 的 near-\(S\)-unit 化

若

```math
n_3\ge10S_{12}+11,
```

由

```math
d_3\le5S_{12}
```

可得

```math
m_3\ge5S_{12}+11.
```

定义

```math
\boxed{
\mathscr T
=
\frac{
\kappa^2(\kappa+2G)
}{
10^{m_3}
}
\in\mathbf Z_{>0}.
}
```

统一尾权区间给出

```math
\boxed{
1\le\mathscr T<10^{S_{12}-7}.
}
```

写

```math
\kappa=2^a5^bu,
\qquad
\gcd(u,10)=1,
```

```math
\kappa+2G=2^c5^ev,
\qquad
\gcd(v,10)=1.
```

则

```math
u^2\mid\mathscr T,
\qquad
v\mid\mathscr T.
```

所以

```math
\boxed{
u<10^{(S_{12}-7)/2},
}
```

```math
\boxed{
v<10^{S_{12}-7}.
}
```

相对于

```math
\kappa,\kappa+2G
\asymp QG
```

的整体尺度，其去掉 \(2,5\) 后的奇部分已经非常小。

因此最顶部 DD 候选必然满足：

```math
\boxed{
\kappa
\text{ 与 }
\kappa+2G
\text{ 同时接近 }2,5\text{-smooth}.
}
```

---

<a id="dd-01-detail-src-0122-12-8"></a>
#### DD 的 square-part 上下界夹逼与极端不对称

由统一终端式可以构造 \(\kappa\) 平方部分 \(q_\square\) 的上界。

一方面得到

```math
q_\square
<
1.92\times10^6
\,
10^{
9S_{12}
+
|s_1-s_2|
-
n_3
}.
```

另一方面 \(5\)-进深尾给出

```math
\log_{10}q_\square
>
0.1747425\,m_3
-\frac{S_{12}}2
-0.619281.
```

消元可得

```math
\boxed{
n_3
<
8.533128S_{12}
+
|s_1-s_2|
+
6.173325.
}
```

如果仍在顶部

```math
n_3\ge10S_{12}+11,
```

则必须有

```math
\boxed{
|s_1-s_2|
>
1.466872S_{12}
+
4.826675.
}
```

利用 digit window 再转化为分母位数不对称：

```math
\boxed{
|m_1-m_2|
>
0.466872S_{12}
+
4.826675.
}
```

所以一个前两分母块必须占据总位数的约 \(73.3\%\) 以上，另一个则低于约 \(26.7\%\)。

若长的一侧对应 \(s_1>s_2\)，还可得到短 numerator block 的估计

```math
\boxed{
n_2
<
0.266564S_{12}
-2.413.
}
```

交换 \(1,2\) 可得对称结论。

因此 DD 的顶部空间已经从多参数无界族压成：

```math
\boxed{
\text{极端 denominator 不对称}
+
\text{一个极短 numerator block}
+
2/5\text{-adic 双 resonance}
+
\text{near-}S\text{-unit}.
}
```

---

<a id="dd-01-detail-src-0122-12-9"></a>
#### DD 最大 denominator-tail 层已排除

若

```math
m_3=6S_{12}+3,
```

则

```math
\mathscr T=1,
```

即

```math
\kappa^2(\kappa+2G)=10^{6S_{12}+3}.
```

于是

```math
\kappa,\kappa+2G
```

只能含素数 \(2,5\)。

利用有理 \(2,5\)-单位之间距离 \(1\) 的最小间距，可以得到

```math
\frac{2G}{\kappa}
\ge5^{-S_{12}}.
```

但尾权区间给出

```math
\frac{2G}{\kappa}
<
\frac2Q
\le
20\cdot10^{-S_{12}}.
```

当

```math
S_{12}\ge5
```

时两者矛盾。

因此

```math
\boxed{
S_{12}\ge5
\Longrightarrow
m_3\ne6S_{12}+3,
}
```

从而加强为

```math
\boxed{
m_3\le6S_{12}+2.
}
```

---

<a id="dd-01-detail-src-0122-12-10"></a>
#### DD 的双 resonance 终端尖角

把目前的上界和 resonance 阈值合并，DD 的最顶层为

```math
\boxed{
10S_{12}+11
\le
n_3
\le
11S_{12}+3.
}
```

并同时满足

```math
\boxed{
d_3=\max(s_1,s_2,d_3),
}
```

```math
\boxed{
d_3\le5S_{12},
}
```

```math
\boxed{
m_3\le6S_{12}+2,
}
```

```math
\boxed{
2\text{-adic 与 }5\text{-adic 同时 resonance},
}
```

```math
\boxed{
|s_1-s_2|
>
1.466872S_{12}
+
4.826675,
}
```

```math
\boxed{
|m_1-m_2|
>
0.466872S_{12}
+
4.826675.
}
```

这是同时发生 \(2\)-进与 \(5\)-进 resonance 的终端尖角。需要注意，上述性质在本节之前只描述“如果候选进入该顶层，它必须长成什么样”；它们本身并没有排除随 \(S_{12}\) 一起增长的中低层线性锥。

---

<a id="dd-01-detail-src-0122-12-11"></a>
#### DD 双 resonance 尖角的严格排除

这一节给出一个新的 prefix-uniform 矛盾。它不再需要猜测判别式最接近哪个平方，而是把十进制拼接 gap 的赋值与一个显式高度直接比较。

<a id="dd-01-detail-src-0122-12-12"></a>
#### 拼接行列式 gap

定义

```math
\boxed{
E
=
b_3A_{12}10^{d_3}-a_3Q.
}
```

由 \(\mathcal R>r_3\) 以及拼接差的直接展开，

```math
\mathcal R-r_3
=
\frac{
10^{m_3}E
}{
b_3(10^{m_3}Q+b_3)
},
```

因此

```math
\boxed{E\in\mathbf Z_{>0}.}
```

利用

```math
b_3=\frac{10^{m_3}QG}{\kappa},
```

可将统一球面 gap 精确写为

```math
\boxed{
\frac{\mu}{\nu}
=
G(\mathcal R-r_3)
=
\frac{
E\kappa^2
}{
10^{m_3}Q^2(\kappa+G)
},
}
```

右端再约分成互素的 \(\mu,\nu\)。

<a id="dd-01-detail-src-0122-12-13"></a>
#### resonance 的赋值转移

对 \(p\in\{2,5\}\) 记

```math
e_p=v_p(E),
\quad
q_p=v_p(Q),
\quad
k_p=v_p(\kappa),
```

```math
h_p=v_p(\kappa+G),
\quad
f_p=v_p(\kappa+2G),
\quad
n_p=v_p(\mathcal N_{12}).
```

由上式约分前后的赋值差，

```math
\boxed{
r_p-s_p
=
e_p+2k_p-m_3-2q_p-h_p.
}
```

而 \(p\)-进 resonance 正是

```math
f_p+2r_p
=
k_p+n_p+2s_p.
```

消去 \(r_p,s_p\) 得到精确恒等式

```math
\boxed{
3k_p+f_p
=
2m_3+4q_p+2h_p+n_p-2e_p.
}
```

如果

```math
p\mid b_3,
\qquad
d_3+v_p(b_3)+v_p(A_{12})>q_p,
```

则由 \(\gcd(a_3,b_3)=1\)，

```math
v_p(a_3Q)=q_p
<
v_p(b_3A_{12}10^{d_3}),
```

所以

```math
\boxed{e_p=q_p.}
```

代回 resonance 恒等式即得

```math
\boxed{
v_p\!\left(\kappa^3(\kappa+2G)\right)
=
3k_p+f_p
=
2m_3+2q_p+2h_p+n_p
\ge2m_3.
}
```

这是尖角排除的核心赋值放大。

<a id="dd-01-detail-src-0122-12-14"></a>
#### 非 resonance 的两条精确支

同一个 gap 恒等式也能把非 resonance 情形从“赋值不相等”加强为两条显式线性恒等式。再记

```math
\lambda_p=v_p(2),
\qquad
g_p=v_p(G),
\qquad
a_p=v_p(A_{12}),
```

并定义两个 near-square 因子的赋值差

```math
\Delta_p
=
v_p(F_-)-v_p(F_+)
=
f_p+2r_p-k_p-n_p-2s_p.
```

由

```math
F_-+F_+=2GA_{12}10^{n_3}
```

及

```math
v_p(F_-F_+)
=
2m_3+2q_p+f_p-k_p+n_p,
```

当 \(\Delta_p\ne0\) 时，和的赋值等于两项中的较小者。把上述各式消元得到

```math
\boxed{
n_3
=
\begin{cases}
2m_3+3q_p+h_p+n_p-e_p-2k_p-\lambda_p-g_p-a_p,
&\Delta_p>0,\\[0.4em]
e_p+f_p+k_p-q_p-h_p-\lambda_p-g_p-a_p,
&\Delta_p<0.
\end{cases}
}
```

这两式尚未单独给出绝对高度界，但它们已经把 DD 的剩余中低层精确分成 resonance、\(\Delta_p>0\) 与 \(\Delta_p<0\) 三种可逐支估计的状态，不再只有一个粗阈值。

<a id="dd-01-detail-src-0122-12-15"></a>
#### 统一阿基米德上界

令

```math
S=S_{12},
\qquad
N=10^S.
```

\(Q\) 是恰有 \(S\) 位的前两分母拼接，并且 \(G=b_1b_2\)，因此

```math
Q<N,
\qquad
G<N.
```

再由 \(\kappa\le10QG\)，

```math
\begin{aligned}
\kappa^3(\kappa+2G)
&\le
(10QG)^3G(10Q+2)\\
&=
10^4Q^3G^4\left(Q+\frac15\right)\\
&<
10^4N^8.
\end{aligned}
```

于是得到严格高度上界

```math
\boxed{
\kappa^3(\kappa+2G)
<
10^{8S_{12}+4}.
}
```

<a id="dd-01-detail-src-0122-12-16"></a>
#### 排除整个双 resonance 顶部

反设存在第 26 节的候选。由

```math
n_3\ge10S+11,
\qquad
d_3\le5S,
```

有

```math
\boxed{m_3\ge5S+11.}
```

又由统一尾长锥 \(m_3\le6S+3\)，

```math
d_3=n_3-m_3\ge4S+8.
```

因此对 \(p=2,5\) 都有

```math
d_3>v_p(Q),
```

因为 \(Q<10^S\)。

首先必有

```math
\boxed{5\mid b_3.}
```

否则由 \(\kappa=10^{m_3}QG/b_3\)，

```math
v_5(\kappa)
=
m_3+v_5(Q)+v_5(G)
\ge m_3,
```

从而

```math
\kappa\ge5^{m_3}
\ge5^{5S+11}
>10^{2S+1}
>\kappa,
```

矛盾。这里最后一个上界来自

```math
\kappa\le10QG<10^{2S+1}.
```

现在分两种奇偶性。

<a id="dd-01-detail-src-0122-12-17"></a>
#### 情形 I：\(2\mid b_3\)

对 \(p=2,5\)，上述深度不等式都成立，所以双 resonance 给出

```math
2^{2m_3}5^{2m_3}
=
10^{2m_3}
\mid
\kappa^3(\kappa+2G).
```

因而

```math
\kappa^3(\kappa+2G)
\ge10^{2m_3}
\ge10^{10S+22},
```

与 \(10^{8S+4}\) 的上界矛盾。

<a id="dd-01-detail-src-0122-12-18"></a>
#### 情形 II：\(2\nmid b_3\)

此时

```math
v_2(\kappa)
=
m_3+v_2(Q)+v_2(G)
\ge m_3.
```

另一方面，\(5\mid b_3\) 且顶部的 \(5\)-进 resonance 已经给出

```math
v_5\!\left(\kappa^3(\kappa+2G)\right)
\ge2m_3.
```

所以

```math
200^{m_3}
=
2^{3m_3}5^{2m_3}
\mid
\kappa^3(\kappa+2G).
```

特别地

```math
\kappa^3(\kappa+2G)
\ge200^{m_3}
>10^{2m_3}
\ge10^{10S+22},
```

同样矛盾。

因此得到：

```math
\boxed{
\text{DD 中不存在 }
10S_{12}+11
\le n_3\le
11S_{12}+3
\text{ 的候选}.
}
```

同一论证还给出一个对剩余中高层有用的奇偶锁。若

```math
d_3=\max(s_1,s_2,d_3),
\qquad
n_3\ge9S+2,
```

则 \(5\)-进 resonance 已被强制，且由 \(d_3\le5S\) 有

```math
m_3\ge4S+2.
```

此时还有 \(d_3\ge3S-1>v_5(Q)\)，并且 \(5^{4S+2}>10^{2S+1}\)。因此与上面完全相同地，先得到 \(5\mid b_3\) 与

```math
5^{2m_3}\mid\kappa^3(\kappa+2G).
```

如果 \(b_3\) 为奇数，则还有 \(v_2(\kappa)\ge m_3\)，从而

```math
200^{m_3}\mid\kappa^3(\kappa+2G).
```

但

```math
200^{m_3}
>10^{2m_3}
\ge10^{8S+4},
```

与高度上界矛盾。所以

```math
\boxed{
d_3=\max(s_1,s_2,d_3),\ n_3\ge9S_{12}+2
\Longrightarrow
10\mid b_3.
}
```

在这个剩余中高层带中，五进相对位置还能被完全固定。记

```math
B_5=v_5(b_3),
\qquad
k_5=v_5(\kappa),
\qquad
g_5=v_5(G).
```

已知 \(e_5=q_5\)。若 \(k_5<g_5\)，则超距性给出

```math
h_5=f_5=k_5.
```

五进 resonance 恒等式因而化为

```math
2k_5=2m_3+2q_5+n_5,
```

所以 \(k_5\ge m_3\)。但 \(k_5<g_5\) 意味着

```math
5^{m_3}
\le5^{k_5}
<5^{g_5}
\le G
<10^S,
```

这与 \(m_3\ge4S+2\) 矛盾。

若 \(k_5=g_5\)，则 resonance 给出

```math
3g_5+f_5\ge2m_3.
```

因此

```math
5^{2m_3}
\le
5^{3g_5+f_5}
\le
G^3(\kappa+2G)
<
11\cdot10^{5S}.
```

可是

```math
5^{2m_3}
\ge
5^{8S+4}
>
11\cdot10^{5S},
```

再次矛盾。因而只剩

```math
\boxed{k_5>g_5.}
```

此时超距性给出

```math
h_5=f_5=g_5.
```

五进 resonance 与 \(\kappa=10^{m_3}QG/b_3\) 分别化为

```math
\boxed{
3k_5
=
2m_3+2q_5+g_5+n_5,
}
```

以及

```math
\boxed{
3B_5
=
m_3+q_5+2g_5-n_5.
}
```

所以只发生五进 resonance 的中高层，已被压成一条唯一的五进线性正规形，并自动带有两条模 \(3\) 整除条件。

这条正规形还能恢复 \(\mu,\nu,G_0,F_\pm\) 的全部五进深度。为避免与全局位数混淆，本段仍以 \(r_5=v_5(\mu)\)、\(s_5=v_5(\nu)\)、\(n_5=v_5(\mathcal N_{12})\) 表示赋值。由 gap 赋值差与五进正规形，

```math
r_5-s_5
=
\frac{m_3+q_5-g_5+2n_5}{3}
>0.
```

因为 \(\gcd(\mu,\nu)=1\)，必有

```math
\boxed{
s_5=0,
\qquad
r_5=\frac{m_3+q_5-g_5+2n_5}{3}.
}
```

还有两个精确差值

```math
2r_5-n_5=k_5-g_5>0,
```

```math
g_5+r_5-n_5=B_5>0.
```

因此在

```math
G_0
=
\gcd(
\mathcal N_{12}\nu^2-\mu^2,
2G\mu\nu
)
```

中，第一个参数的五进赋值恰为 \(n_5\)，第二个则为 \(n_5+B_5\)。所以

```math
\boxed{v_5(G_0)=n_5.}
```

代回 \(F_-,F_+\) 的定义，两个因子的五进赋值不仅相等，而且都恰为

```math
\boxed{
v_5(F_-)=v_5(F_+)=k_5.
}
```

记 \(a_5=v_5(A_{12})\)，则约去 \(5^{k_5}\) 后的两个五进单位在和中发生深度

```math
\boxed{
\mathscr R_5
=
n_3+g_5+a_5-k_5
}
```

的精确抵消。由 \(n_3\ge9S+2\) 与 \(\kappa<10^{2S+1}\)，

```math
\boxed{
\mathscr R_5
>
\left(9-2\log_5 10\right)S
+2-\log_5 10
>
6.1386S+0.569.
}
```

所以剩余中高层必须同时承担一个随 \(S\) 线性增长的超深五进单位抵消；这是后续做 rational reconstruction 或线性形下界时应直接攻击的目标。

五进正规形与阿基米德大小还会立即产生一次新的线性锥收缩。记

```math
L_5=\log_5 10.
```

由 \(\kappa<10^{2S+1}\)，

```math
k_5<(2S+1)L_5.
```

代入

```math
3k_5=2m_3+2q_5+g_5+n_5
```

先得到

```math
\boxed{
m_3
<
3L_5S+\frac32L_5.
}
```

再结合 \(d_3\le5S\)，对该中高层有

```math
\boxed{
n_3
<
\left(5+3L_5\right)S
+\frac32L_5.
}
```

在未达到五进 resonance 阈值时本来就有 \(n_3\le9S+1\)，而非 \(d_3\)-dominant 扇区有 \(n_3\le7S+4\)。因此这一上界对全部 DD 候选都成立：

```math
\boxed{
n_3
<
\left(5+3\log_5 10\right)S_{12}
+\frac32\log_5 10
<
9.29203S_{12}+2.14602.
}
```

这比先前的 \(n_3\le10S_{12}+10\) 真正降低了线性主系数。

还可以把这个新上界反代回 squarefree gap。在剩余中高层中，

```math
n_3\ge9S+2
```

与 \(m_3<3L_5S+\frac32L_5\) 给出

```math
d_3
>
\left(9-3L_5\right)S
+2-\frac32L_5.
```

第 21 节的界

```math
d_3
\le
3S+|s_1-s_2|+2
```

因而加强为

```math
\boxed{
|s_1-s_2|
>
\left(6-3L_5\right)S
-\frac32L_5
>
1.70797S-2.14602.
}
```

由 \(s_1+s_2\le2\) 且

```math
|n_1-n_2|
\le
n_1+n_2-2
\le S,
```

得到分母位数不对称

```math
\boxed{
|m_1-m_2|
>
\left(5-3L_5\right)S
-\frac32L_5
>
0.70797S-2.14602.
}
```

例如若 \(s_1>s_2\)，则第二分母块是长块，并且

```math
\boxed{
m_2
>
\left(3-\frac32L_5\right)S
-\frac34L_5
>
0.85398S-1.07301,
}
```

```math
\boxed{
n_2
<
\left(\frac32L_5-2\right)S
+\frac34L_5
<
0.14602S+1.07301.
}
```

交换 \(1,2\) 得到对称结论。这使

```math
\mathcal N_{12}=X_0^2+\varepsilon^2
```

的 near-square 误差得到新的指数级界。确实，选取 \(X_0\) 为较大的 \(a_1b_2,a_2b_1\) 之一，则十进制位数窗口给出

```math
\frac{|\varepsilon|}{X_0}
<
10^{2-|s_1-s_2|}.
```

因而：

```math
\boxed{
0<\frac{|\varepsilon|}{X_0}
<
10^{
-\left(6-3L_5\right)S
+2+\frac32L_5
}
<
10^{-1.70797S+4.14602}.
}
```

而且这里不只有相对误差小。在 \(s_1>s_2\) 时，短块正是 \(a_2\) 与 \(b_1\)，因而

```math
|\varepsilon|=a_2b_1.
```

由上述 \(n_2,m_1\) 界，

```math
\boxed{
0<|\varepsilon|
<
10^{
\left(3L_5-4\right)S
+\frac32L_5
}
<
10^{0.29203S+2.14602},
}
```

```math
\boxed{
\varepsilon^2
<
10^{
\left(6L_5-8\right)S
+3L_5
}
<
10^{0.58406S+4.29203}.
}
```

对称方向完全相同。

因而原先只在更高顶部出现的“极短 numerator block + near-square”现在已经下降到整个剩余单 resonance 薄带。

同时，由 \(m_3\ge4S+2\)，

```math
\boxed{
2q_5+g_5+n_5
<
\left(6L_5-8\right)S
+3L_5-4
<
0.58406S+0.29203.
}
```

再代入

```math
3B_5=m_3+q_5+2g_5-n_5
```

得到第三个统一挤压：

```math
\boxed{
B_5
>
\left(2-L_5\right)(2S+1)
>
1.13864S+0.569.
}
```

因而剩余中高层同时具有：极小的前缀五进赋值预算、线性深度的 \(5\mid b_3\)，以及超深五进单位抵消。

还可以把 \(\kappa\) 本身的非五进核直接压小。写

```math
\kappa=5^{k_5}u_5,
\qquad
5\nmid u_5.
```

由五进正规形与 \(m_3\ge4S+2\)，

```math
k_5
\ge
\frac{2m_3}{3}
\ge
\frac{8S+4}{3}.
```

再用 \(\kappa<10^{2S+1}\)，

```math
\boxed{
u_5
<
10^{
\left(2-\frac83\log_{10}5\right)S
+1-\frac43\log_{10}5
}
<
10^{0.13609S+0.06805}.
}
```

特别地，\(\mathfrak k=v_2(\kappa)=v_2(u_5)\)，所以

```math
\boxed{
\mathfrak k
<
0.45205S+0.22603.
}
```

由

```math
\mathfrak b
=
m_3+\mathfrak q+\mathfrak g-\mathfrak k
```

又得

```math
\boxed{
\mathfrak b
>
3.54795S+1.77397.
}
```

也就是说，剩余中高层不仅有深五进尾，还必须有更深的二进尾；与此同时，\(\kappa\) 除去五次幂后的整个核只能占前缀高度约 \(13.61\%\) 的十进制位数。

二进侧也可以做出精确分支。为避免与全局位数 \(n_2\) 混淆，局部记

```math
\mathfrak b=v_2(b_3),
\quad
\mathfrak q=v_2(Q),
\quad
\mathfrak g=v_2(G),
\quad
\mathfrak n=v_2(\mathcal N_{12}),
```

```math
\mathfrak a=v_2(A_{12}),
\quad
\mathfrak k=v_2(\kappa),
\quad
\mathfrak h=v_2(\kappa+G),
\quad
\mathfrak f=v_2(\kappa+2G).
```

先证明在该中高层中必有

```math
\boxed{v_2(E)=\mathfrak q.}
```

否则必须有

```math
\mathfrak b+d_3+\mathfrak a\le\mathfrak q.
```

但由

```math
\mathfrak k
=
m_3+\mathfrak q+\mathfrak g-\mathfrak b
```

就会得到

```math
\mathfrak k
\ge
m_3+d_3+\mathfrak a+\mathfrak g
\ge n_3.
```

于是

```math
\kappa
\ge2^{n_3}
\ge2^{9S+2}
>10^{2S+1},
```

与 \(\kappa<10^{2S+1}\) 矛盾。因此二进拼接 gap 中不可能发生比 \(Q\) 更深的额外抵消。

其次，二进侧不可能 resonance。否则 \(v_2(E)=\mathfrak q\) 给出

```math
2^{2m_3}\mid\kappa^3(\kappa+2G),
```

而五进 resonance 已给出

```math
5^{2m_3}\mid\kappa^3(\kappa+2G).
```

这会导致

```math
10^{2m_3}
\mid
\kappa^3(\kappa+2G),
\qquad
m_3\ge4S+2,
```

再次与严格上界 \(10^{8S+4}\) 矛盾。

最后，在二进非 resonance 中还必有

```math
\boxed{\Delta_2>0.}
```

确实，若 \(\Delta_2<0\)，则第 27.2 节的第二条恒等式化为

```math
n_3
=
\mathfrak f+\mathfrak k-\mathfrak h-1-\mathfrak g-\mathfrak a.
```

对 \(\mathfrak k<\mathfrak g\)、\(\mathfrak k=\mathfrak g\)、\(\mathfrak k>\mathfrak g\) 分别使用超距性：

- \(\mathfrak k<\mathfrak g\) 时 \(\mathfrak f=\mathfrak h=\mathfrak k\)，右端为负；
- \(\mathfrak k=\mathfrak g\) 时 \(\mathfrak f=\mathfrak g\) 且 \(\mathfrak h\ge\mathfrak g+1\)，右端仍为负；
- \(\mathfrak k\ge\mathfrak g+2\) 时 \(\mathfrak h=\mathfrak g\)、\(\mathfrak f=\mathfrak g+1\)，从而 \(n_3\le\mathfrak k<\log_2(10^{2S+1})<9S+2\)；
- \(\mathfrak k=\mathfrak g+1\) 时 \(\mathfrak h=\mathfrak g\)，并且 \(n_3\le\mathfrak f\le\log_2(\kappa+2G)<\log_2(11\cdot10^{2S})<9S+2\).

四种情形均矛盾。所以中高层的二进侧只能落在 \(\Delta_2>0\) 支。把第 27.2 节的第一条恒等式与

```math
\mathfrak k=m_3+\mathfrak q+\mathfrak g-\mathfrak b
```

合并，最终得到三条显式正规形：

```math
\boxed{
n_3
=
\begin{cases}
m_3+\mathfrak q+\mathfrak b+\mathfrak n-2\mathfrak g-1-\mathfrak a,
&\mathfrak k<\mathfrak g,\\[0.4em]
2\mathfrak b+\mathfrak h+\mathfrak n-3\mathfrak g-1-\mathfrak a,
&\mathfrak k=\mathfrak g,\\[0.4em]
2\mathfrak b-2\mathfrak g+\mathfrak n-1-\mathfrak a,
&\mathfrak k>\mathfrak g.
\end{cases}
}
```

至此，原来的“单五进 resonance 中高层”已被改写为：一条唯一五进正规形，加上三条互斥的二进正规形。

特别地，五进正规形本身先给出统一相对上界

```math
\boxed{
n_3
<
\left(5+3\log_5 10\right)S_{12}
+\frac32\log_5 10.
}
```

<a id="dd-01-detail-src-0122-12-19"></a>
#### 二进主导项关闭整个单五进 resonance 带

上面的三条二进正规形实际上还能继续闭合。关键不是再估计其中每一项，而是回到有理球面恒等式

```math
(\mathcal R-r_3)(\mathcal R+r_3)
=
r_1^2+r_2^2
=
\frac{\mathcal N_{12}}{G^2}.
```

仍处在

```math
d_3=\max(s_1,s_2,d_3),
\qquad
n_3\ge9S+2
```

的剩余中高层。沿用二进记号

```math
\mathfrak b=v_2(b_3),
\quad
\mathfrak q=v_2(Q),
\quad
\mathfrak g=v_2(G),
\quad
\mathfrak k=v_2(\kappa).
```

第 27.4 节已经给出

```math
\mathfrak b>3.54795S+1.77397.
```

另一方面，对 \(i=1,2\)，

```math
v_2(b_i)
<
m_i\log_2 10
\le
(S-1)\log_2 10
<
\mathfrak b.
```

所以 \(b_3\) 的二进分母指数严格独占最大值。又因 \(2\mid b_3\) 与 \(\gcd(a_3,b_3)=1\)，\(a_3\) 为奇数，从而 \(r_3^2\) 是

```math
r_1^2+r_2^2+r_3^2=\mathcal R^2
```

中唯一具有最小二进赋值的一项。因此

```math
v_2(\mathcal R)=-\mathfrak b.
```

拼接分子

```math
\alpha=10^{n_3}A_{12}+a_3
```

也是奇数，于是 exact lift 强迫

```math
v_2(\beta)=\mathfrak b.
```

由

```math
\beta
=
10^{m_3}Q+b_3
=
10^{m_3}Q\frac{\kappa+G}{\kappa}
```

以及

```math
\mathfrak b
=
m_3+\mathfrak q+\mathfrak g-\mathfrak k,
```

得到

```math
\mathfrak h=v_2(\kappa+G)=\mathfrak g.
```

若 \(\mathfrak k<\mathfrak g\)，则超距性给出 \(\mathfrak h=\mathfrak k\)；若 \(\mathfrak k=\mathfrak g\)，则 \(\mathfrak h\ge\mathfrak g+1\)。两者都不可能。因此三条二进正规形中前两条自动消失，并且

```math
\boxed{
\mathfrak k>\mathfrak g,
\qquad
\mathfrak h=\mathfrak g.
}
```

现在记

```math
\delta=\mathcal R-r_3>0.
```

由拼接 gap 赋值式 \(v_2(E)=\mathfrak q\)，

```math
v_2(\delta)
=
2\mathfrak k-m_3-\mathfrak q-2\mathfrak g.
```

而

```math
v_2(2r_3)
=
1-\mathfrak b
=
1-m_3-\mathfrak q-\mathfrak g+\mathfrak k.
```

两者之差恰为

```math
v_2(\delta)-v_2(2r_3)
=
\mathfrak k-\mathfrak g-1.
```

若 \(\mathfrak k\ge\mathfrak g+2\)，则 \(2r_3\) 在

```math
\mathcal R+r_3=2r_3+\delta
```

中严格主导。对球面差分取二进赋值便得到

```math
\mathfrak n-2\mathfrak g
=
v_2(\delta)+v_2(2r_3),
```

即

```math
\mathfrak n
=
3\mathfrak k
-2m_3
-2\mathfrak q
-\mathfrak g
+1.
```

但第 27.4 节的非五进核估计可以精确写成

```math
\mathfrak k
<
\eta S+\eta_0,
\qquad
\eta=\frac{8-2\log_2 10}{3}<0.452048,
\qquad
\eta_0=\frac{4-\log_2 10}{3}<0.226024.
```

结合 \(m_3\ge4S+2\) 与 \(\mathfrak q,\mathfrak g\ge0\)，上式右端满足

```math
\mathfrak n
<
(3\eta-8)S+3\eta_0-3
<0,
```

与 \(\mathfrak n\ge0\) 矛盾。故只能有

```math
\boxed{\mathfrak k=\mathfrak g+1.}
```

为避免与全局的第二个有理数 \(r_2\) 及位数差 \(s_2\) 混淆，改记

```math
\rho_2=v_2(\mu),
\qquad
\sigma_2=v_2(\nu).
```

由 gap 赋值差

```math
\rho_2-\sigma_2
=
\mathfrak g+2-m_3-\mathfrak q
<
(\eta-4)S+\eta_0-1
<0
```

且右端严格为负，所以互素性给出

```math
\rho_2=0,
\qquad
\sigma_2=m_3+\mathfrak q-\mathfrak g-2.
```

于是已证的 \(\Delta_2>0\) 化为

```math
0<\Delta_2
=
\mathfrak f+\mathfrak g+3
-\mathfrak n-2m_3-2\mathfrak q.
```

因此

```math
\mathfrak f
\ge
2m_3+2\mathfrak q+\mathfrak n-\mathfrak g-2
\ge
8S+2-\mathfrak g.
```

另一方面，\(\mathfrak g=\mathfrak k-1<\eta S+\eta_0-1\)，所以

```math
\mathfrak f
>
(8-\eta)S+3-\eta_0.
```

可是统一高度窗口给出

```math
2^{\mathfrak f}
\le
\kappa+2G
<
11\cdot10^{2S},
```

即

```math
\mathfrak f
<
2S\log_2 10+\log_2 11.
```

两条界的差至少为

```math
\left(8-\eta-2\log_2 10\right)S
+3-\eta_0-\log_2 11
>
0.90409S-0.68546
>0,
```

这里 \(S=m_1+m_2\ge2\)。矛盾。

所以单五进 resonance 的整个中高层带也是空的：

```math
\boxed{
d_3=\max(s_1,s_2,d_3),\quad
n_3\ge9S_{12}+2
\Longrightarrow
\text{无候选}.
}
```

与两个非 \(d_3\)-dominant 扇区的 \(n_3\le7S_{12}+4\) 合并，得到这一阶段的 DD 统一相对界

```math
\boxed{
n_3\le9S_{12}+1.
}
```

<a id="dd-01-detail-src-0122-12-20"></a>
#### 阈值以下上层的五进入口

虽然强制五进 resonance 的整带已经排除，但同一个方法还能把剩余区域的上层先压成两个精确状态。仍令

```math
L_5=\log_5 10.
```

首先，若 \(d_3\)-dominant 候选满足 \(5\nmid b_3\)，则

```math
k_5
=
m_3+q_5+g_5
\ge
m_3.
```

由 \(\kappa<10^{2S+1}\) 与 \(d_3\le5S\)，

```math
\boxed{
5\nmid b_3
\Longrightarrow
n_3
<
(5+2L_5)S+L_5
<
7.86136S+1.43068.
}
```

所以

```math
n_3\ge(5+2L_5)S+L_5
```

时必有 \(5\mid b_3\)。

其次，若

```math
n_3>(6+L_5)S+3,
```

则由 \(m_3\le6S+3\) 得

```math
d_3>L_5S>q_5.
```

在 \(5\mid b_3\) 时，\(\gcd(a_3,b_3)=1\) 给出 \(5\nmid a_3\)，故拼接行列式的第一项具有更深五进赋值，并且

```math
\boxed{e_5=q_5.}
```

当 \(S\ge4\) 时，

```math
(5+2L_5)S+L_5
>
(6+L_5)S+3.
```

对剩余的 \(S=2,3\)，整数性分别给出

```math
\begin{array}{c|c|c}
S&d_3\text{ 的下界}&q_5\text{ 的上界}\\
\hline
2&3&2\\
3&5&4
\end{array}
```

所以仍有 \(d_3>q_5\)。因此对所有 \(S=m_1+m_2\ge2\)，只要进入

```math
\boxed{
n_3\ge(5+2L_5)S+L_5,
}
```

就同时有

```math
\boxed{
5\mid b_3,
\qquad
e_5=q_5.
}
```

在这个上层，五进的 \(\Delta_5<0\) 支不可能发生。事实上，第 27.2 节的第二条恒等式化为

```math
n_3=f_5+k_5-h_5-g_5-a_5.
```

按 \(k_5\) 与 \(g_5\) 的相对大小分类：

- 若 \(k_5<g_5\)，则 \(h_5=f_5=k_5\)，右端为 \(k_5-g_5-a_5<0\)；
- 若 \(k_5>g_5\)，则 \(h_5=f_5=g_5\)，从而
```math
  n_3=k_5-g_5-a_5<k_5<(2S+1)L_5;
```
- 若 \(k_5=g_5\)，则
```math
  n_3=f_5-h_5-a_5
  \le f_5
  <
  2L_5S+\log_5 11.
```

三种情形都到不了 \((5+2L_5)S+L_5\)。所以

```math
\boxed{\Delta_5<0\text{ 在该上层为空}.}
```

若该上层发生五进 resonance，则同样只能有 \(k_5>g_5\)。确实：

- \(k_5<g_5\) 时 resonance 化为
```math
  2k_5=2m_3+2q_5+n_5,
```
  因而 \(k_5\ge m_3\)，但上层给出
```math
  m_3\ge n_3-d_3\ge2L_5S+L_5>g_5>k_5,
```
  矛盾；
- \(k_5=g_5\) 时 resonance 给出
```math
  g_5+f_5\ge2m_3.
```
  于是
```math
  5^{2m_3}
  \le
  G(\kappa+2G)
  <
  11\cdot10^{3S},
```
  但 \(m_3\ge2L_5S+L_5\) 又使左端至少为 \(10^{4S+2}\)，仍然矛盾。

故 resonance 情形重新落入唯一五进正规形

```math
\boxed{
k_5>g_5,
\qquad
3k_5=2m_3+2q_5+g_5+n_5.
}
```

\(\Delta_5>0\) 支也能化成唯一正规形。先排除 \(k_5<g_5\)。此时

```math
B_5
=
m_3+q_5+g_5-k_5
>
m_3
\ge
2L_5S+L_5.
```

而对 \(i=1,2\)，

```math
v_5(b_i)
<
m_iL_5
\le
(S-1)L_5
<
B_5.
```

所以 \(b_3\) 独占最大五进分母指数。与第 27.5 节的二进论证相同，\(r_3^2\) 是球面和中唯一具有最小五进赋值的一项；又因拼接分子是五进单位，exact lift 强迫

```math
v_5(\beta)=B_5.
```

由

```math
v_5(\beta)
=
m_3+q_5+h_5-k_5
```

与 \(B_5=m_3+q_5+g_5-k_5\)，得到 \(h_5=g_5\)。但 \(k_5<g_5\) 时超距性给出 \(h_5=k_5\)，矛盾。因此

```math
k_5\ge g_5.
```

若 \(k_5>g_5\)，超距性直接给出 \(h_5=g_5\)；若 \(k_5=g_5\)，上面的 unique-max 论证仍给出同一结论。于是 \(\Delta_5>0\) 的第一条精确恒等式统一化为

```math
\boxed{
k_5\ge g_5,
\qquad
h_5=g_5,
\qquad
n_3
=
2m_3+2q_5+n_5-2k_5-a_5.
}
```

因此阈值以下的剩余上层已经从三种五进状态压成两条显式正规形：

```math
\boxed{
\begin{array}{ll}
\text{resonance:}
&
k_5>g_5,\quad
3k_5=2m_3+2q_5+g_5+n_5,
\\[0.4em]
\Delta_5>0:
&
k_5\ge g_5,\quad
n_3=2m_3+2q_5+n_5-2k_5-a_5.
\end{array}
}
```

这一区域仍未排除，但新的精确攻关带已从 \(9S+2\) 下移到约 \(7.86136S+1.43068\)。

<a id="dd-01-detail-src-0122-12-21"></a>
#### 二进分母主导位置与全奇分母锥

剩余 DD 还可以按三个分母的二进最高指数来自何处做全局切分。记

```math
e_i^{(2)}=v_2(b_i),
\qquad
E_2=\max_i e_i^{(2)}.
```

若 \(E_2>0\)，整数球面模 \(4\) 与 primitive recovery 表明 \(E_2\) 必须唯一取得。exact lift 又进一步限制了这个唯一最大值的位置。

若 \(b_3\) 为奇数而 \(E_2>0\)，则拼接分母 \(\beta\) 为奇数，所以

```math
v_2(\alpha/\beta)\ge0.
```

但球面和中唯一拥有最大二进分母指数的坐标会给出

```math
v_2(\mathcal R)=-E_2<0,
```

矛盾。因此只要某个分母为偶数，就必有 \(2\mid b_3\)，从而 \(a_3\) 与拼接分子 \(\alpha\) 都是奇数。

沿用

```math
\mathfrak b=v_2(b_3),
\quad
\mathfrak g=v_2(G),
\quad
\mathfrak k=v_2(\kappa),
\quad
\mathfrak h=v_2(\kappa+G),
```

由 \(v_2(\mathcal R)=-E_2\) 及 exact lift，

```math
v_2(\beta)=E_2.
```

又

```math
v_2(\beta)-\mathfrak b
=
\mathfrak h-\mathfrak g.
```

因此出现严格二分：

```math
\boxed{
\begin{array}{c|c}
\mathfrak b>\max(e_1^{(2)},e_2^{(2)})
&
\mathfrak k>\mathfrak g,\quad
\mathfrak h=\mathfrak g
\\[0.4em]
\max(e_1^{(2)},e_2^{(2)})>\mathfrak b
&
\mathfrak k=\mathfrak g,\quad
\mathfrak h>\mathfrak g.
\end{array}
}
```

第二行还能给出第三尾长的显式前缀界。若唯一最大值来自 \(b_1\)，则

```math
\mathfrak q=e_2^{(2)},
\qquad
\mathfrak b=m_3+e_2^{(2)},
\qquad
e_1^{(2)}>m_3+e_2^{(2)},
```

所以

```math
\boxed{m_3<e_1^{(2)}-e_2^{(2)}<m_1\log_2 10.}
```

若唯一最大值来自 \(b_2\)，则必须先有

```math
e_2^{(2)}>e_1^{(2)}+m_2,
\qquad
\mathfrak q=e_1^{(2)}+m_2,
```

并进一步有

```math
e_2^{(2)}>m_3+e_1^{(2)}+m_2.
```

所以

```math
\boxed{
m_3
<
e_2^{(2)}-e_1^{(2)}-m_2
<
(\log_2 10-1)m_2.
}
```

特别地，二进最高分母指数来自前缀时，总有

```math
\boxed{
n_3
<
(5+\log_2 10)S_{12}-\log_2 10.
}
```

某些方向还能更强。若 \(s_1>s_2\)，则 \(b_1\) 是短 denominator block；如果此时二进唯一最大值恰来自 \(b_1\)，squarefree gap 给出

```math
\boxed{
n_3
<
(3+\log_2 10)S_{12}
+4-\log_2 10
<
6.32193S_{12}+0.67808.
}
```

最后处理

```math
e_1^{(2)}=e_2^{(2)}=\mathfrak b=0,
```

即三个分母全部为奇数的锥。此时

```math
\mathfrak q=\mathfrak g=0,
\qquad
\mathfrak k=m_3,
\qquad
\mathfrak h=0.
```

记 \(e=v_2(E)\)。拼接 gap 赋值差给出

```math
v_2(\mu)-v_2(\nu)=m_3+e>0.
```

由 \(\gcd(\mu,\nu)=1\)，

```math
v_2(\mu)=m_3+e,
\qquad
v_2(\nu)=0.
```

再对 primitive recovery

```math
10^{m_3}QG_0=2\kappa\mu\nu
```

取二进赋值，得到

```math
v_2(G_0)=m_3+e+1.
```

由于

```math
G_0
=
\gcd(
\mathcal N_{12}\nu^2-\mu^2,\,
2G\mu\nu
),
```

且 \(\mu^2\) 已被 \(2^{2(m_3+e)}\) 整除，必有

```math
\boxed{
v_2(\mathcal N_{12})\ge m_3+e+1.
}
```

写 \(u_i=v_2(a_i)\)。因 \(b_1,b_2\) 为奇数，二平方和的二进赋值律给出

```math
\min(u_1,u_2)
\ge
\frac{m_3+e}{2}.
```

所以两个前缀分子都必须含有至少约 \(2^{m_3/2}\) 的公共二进尺度。结合

```math
n_1+n_2=S+s_1+s_2\le S+2
```

先得到

```math
m_3<(S+2)\log_2 10.
```

再令 \(D_s=|s_1-s_2|\)。较短的 numerator block 满足

```math
n_{\rm short}\le S-\frac{D_s}{2},
```

而 squarefree gap 给出

```math
D_s\ge d_3-3S-2.
```

把 \(m_3/2<(\log_2 10)n_{\rm short}\) 代入并消去 \(D_s\)，得到

```math
d_3
<
5S+2-\frac{m_3}{\log_2 10}.
```

最终：

```math
\boxed{
\text{三个分母全奇}
\Longrightarrow
n_3
<
(4+\log_2 10)S_{12}
+2\log_2 10
<
7.32193S_{12}+6.64386.
}
```

这些界尚未排除整个低层，但已证明 DD 的真正最危险锥必须让 \(b_3\) 承担二进唯一最大值，或落入“\(b_1\) 为长 denominator block 且独占二进最大”的定向前缀锥。


来源：`SRC-0122:12–2715`。原文保全，当前论证以本节为准。

<a id="dd-b01"></a>
### DD-B01　corrected Schmidt、quantitative defect 与 one-channel 基线

**状态：已严格完成。** 经典 Subspace Theorem 下的非有效序列结论；canonical neighborhood 的参数和预算在此统一。

依赖：[DD-01](#dd-01)

核对：正文推导；本次重写未为此项另增枚举。

<a id="dd-b01-detail-src-0135-23-1"></a>
#### corrected high-funnel 5-adic data

记

```math
B_5=v_5(b_3),\qquad
E_5=\max_i v_5(b_i),
```
```math
q_5=v_5(Q),\quad g_5=v_5(G),\quad n_5=v_5(\mathcal N_{12}),
```
```math
k_5=v_5(\kappa).
```

canonical high funnel 有

```math
5\mid b_3,\qquad k_5>g_5,
```

以及 exact resonance / tail weight

```math
\boxed{3k_5=2m+2q_5+g_5+n_5,}
\tag{1.1}
```

```math
\boxed{k_5=m+q_5+g_5-B_5.}
\tag{1.2}
```

因此

```math
\boxed{3B_5=m+q_5+2g_5-n_5.}
\tag{1.3}
```

对任何试图保持 slope `>6` 的无界 high-funnel sequence，旧的独立 lemma
`B_5>=m => n<6S+O(1)` 已经排除 `B_5>=m`；所以只需研究 eventually

```math
\boxed{B_5<m.}
\tag{1.4}
```

令

```math
\delta_5:=E_5-B_5\ge0.
```

`dd-discriminant-root-dependency-audit-2026-08-22.md` 已严格恢复

```math
\boxed{v_5(a)=v_5(\Xi)=q_5+\delta_5,}
\tag{1.5}
```

以及

```math
\boxed{v_5(H_{\rm sph}-y_3)
=m+q_5+E_5-2B_5.}
\tag{1.6}
```

定义 S-unit exponent

```math
\boxed{T:=k_5-g_5.}
```

由 `(1.2)`：

```math
\boxed{T=m+q_5-B_5.}
\tag{1.7}
```

所以 `(1.6)` 精确改写为

```math
\boxed{v_5(H_{\rm sph}-y_3)=T+\delta_5.}
\tag{Gap5-corrected}
```

---

<a id="dd-b01-detail-src-0135-23-2"></a>
#### denominator-max deficit 在 `gap * overlap` 中精确消失

canonical `t_2=1` phase写

```math
G=\gamma V,
\qquad (V,10)=1.
```

因此

```math
v_5(\gamma)=g_5.
```

同时

```math
c_3:=q_{\rm lcm}/b_3
```
满足

```math
v_5(c_3)=E_5-B_5=\delta_5.
```

exact overlap normalization给

```math
\widehat g:=\frac{g_*}{V}=\frac\gamma{c_3}\in\mathbf Z_{>0}.
```

所以

```math
\boxed{v_5(\widehat g)=g_5-\delta_5.}
\tag{2.1}
```

与 `(Gap5-corrected)` 相加：

```math
\boxed{
v_5\bigl((H_{\rm sph}-y_3)\widehat g\bigr)
=T+g_5.}
\tag{Five-cancel}
```

这一步很关键：`b_3` 是否为 5-adic maximum 完全不再需要分类。
若 prefix max 高出 `delta_5`，sphere gap恰多 `delta_5`，normalized overlap恰少
`delta_5`；二者乘积的实际 small-factor 5-depth不变。

---

<a id="dd-b01-detail-src-0135-23-3"></a>
#### corrected universal `F_-` lower

exact S-unit factorization为

```math
\boxed{
F_-
=2^{H+1}Z\,(H_{\rm sph}-y_3)\widehat g,
}
\tag{3.1}
```

其中 `Z` 为 10-unit。

canonical funnel 中 `b_3` 是二进 unique maximum，所以

```math
v_2(c_3)=0,
\qquad
v_2(\widehat g)=v_2(\gamma)=:\mathfrak g.
```

sphere gap 的 2-depth非负，因此从 `(3.1)` 安全得到（忽略绝对 `O(1)`）

```math
\log_{10}F_-
\ge
H\log_{10}2
+\mathfrak g\log_{10}2
+(T+g_5)\log_{10}5
+\log_{10}Z
-O(1).
\tag{3.2}
```

令

```math
a:=\log_{10}2,\qquad b:=\log_{10}5=1-a,
```

并记 normalized rough overlap

```math
R:=\frac{\log_{10}\gamma_0}{S},
\qquad
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0.
```

S-unit pinning

```math
\kappa+2G=2\gamma2^HZ
```

与 `log10(kappa+2G)=2S+O(1)` 给

```math
a\frac HS+
rac{\log_{10}Z}{S}
=2-aG_2-bG_5-R+o(1),
\tag{3.3}
```

其中

```math
G_2=\mathfrak g/S,\qquad G_5=g_5/S.
```

把 `(3.3)` 代入 `(3.2)`，`G_2,G_5` 精确抵消：

```math
\boxed{
\frac{\log_{10}F_-}{S}
\ge
2+b\frac TS-R-o(1).
}
\tag{Fminus-corrected-lower}

```
这是替代旧 `Final-5` 分支 smooth lower 的统一 high-funnel inequality。

---

<a id="dd-b01-detail-src-0135-23-4"></a>
#### 与 Archimedean upper 联立

`high-funnel-defect-optimization.md` 的 d-dominant small-factor upper不依赖
5-adic dichotomy：

```math
\boxed{
\log_{10}F_-<4S+2m-n+O(1).}
\tag{4.1}
```

沿任意实现 limsup 的 subsequence，记

```math
\mathcal N:=\limsup\frac nS,
\quad
M:=m/S,
\quad Q_5:=q_5/S,
\quad G_5:=g_5/S,
\quad N_5:=n_5/S.
```

由 `(1.1)`：

```math
\boxed{
\frac TS
=\frac{2M+2Q_5-2G_5+N_5}{3}.}
\tag{4.2}
```

`(Fminus-corrected-lower)` 与 `(4.1)` 因而给

```math
\boxed{
\begin{aligned}
\mathcal N
\le{}&2
+\frac{2(2+a)}3M
-\frac{2b}{3}Q_5
+\frac{2b}{3}G_5\\
&-\frac b3N_5+R.
\end{aligned}}
\tag{Corrected-stability}

```
---

<a id="dd-b01-detail-src-0135-23-5"></a>
#### stronger Schmidt budget 可独立恢复

令

```math
Q_2=\mathfrak q/S,\qquad N_2=\mathfrak n/S.
```

canonical `t_2=1` phase有

```math
\kappa=2\gamma5^TU,
\qquad
\kappa+2G=2\gamma2^HZ,
```

以及 fixed-target Schmidt

```math
\log_{10}U+\log_{10}Z\ge S-o(S).
```

2-resonance给

```math
H/S=2M+2Q_2+N_2-2G_2+o(1).
```

直接消去 `U,Z,H,G_2`，得到无需 `Final-5-lock` 的安全 budget：

```math
\boxed{
A M
+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)
+2R
\le3,
}
\tag{Schmidt-safe}
```

其中

```math
\boxed{A:=\frac{2(1+2a)}3.}
```

后续只需丢掉非负 `Q_2,N_2`，得到

```math
\boxed{
A M
+\frac b3(2Q_5+4G_5+N_5)
+2R
\le3.
}
\tag{5.1}

```
---

<a id="dd-b01-detail-src-0135-23-6"></a>
#### 闭式 dual：恢复 `6.308883...`

`Corrected-stability` 的 `M` coefficient为

```math
\frac{2(2+a)}3.
```

取

```math
\boxed{
\lambda:=\frac{2+a}{1+2a}.}
\tag{6.1}
```

则

```math
\lambda A=\frac{2(2+a)}3.
```

将 `(5.1)` 乘 `lambda`：

- `M` coefficient与 `Corrected-stability` 正好相等；
- `Q_5,N_5` 在目标中本来就是非正 coefficient；
- 对 `G_5`，
```math
  \lambda\frac{4b}{3}>\frac{2b}{3};
```
- 对 `R`，
```math
  2\lambda>1.
```

所有 variables均非负，因此

```math
\boxed{
\mathcal N
\le2+3\lambda.}
\tag{6.2}

```
即

```math
\boxed{
\mathcal N
\le
2+3\frac{2+a}{1+2a}
=\frac{8+7a}{1+2a}.}
\tag{Corrected-6308}

```
数值为

```math
\boxed{
\frac{8+7\log_{10}2}{1+2\log_{10}2}
=6.308883577618031\ldots.}
```

所以原 canonical high-funnel 的 Schmidt frontier常数在纠错后仍被恢复，
但证明不再经过任何 fake 5-adic valuation mismatch。

---

<a id="dd-b01-detail-src-0135-23-7"></a>
#### equality rigidity

上述 dual 中：

- `G_5` coefficient有严格正 slack；
- `R` coefficient有严格正 slack；
- `Q_5,N_5` 在 `Corrected-stability` 中为负，而 Schmidt combination中为非负。

因此若存在 sequence逼近 `(Corrected-6308)`，必须有

```math
\boxed{Q_5,G_5,N_5,R\to0.}
\tag{7.1}
```

而 `(5.1)` 必须饱和，所以

```math
A M\to3.
```

即

```math
\boxed{
M\to\frac3A
=\frac{9}{2(1+2a)}
=2.808883577618031\ldots.}
\tag{7.2}
```

这正是旧 `6.308883...` equality frontier 的 tail ratio。

由 `Corrected-stability` equality再恢复

```math
\boxed{
d/S\to7/2.}
```

其余 `U,Z,T,H` 比例可继续由 canonical S-unit pinning恢复为 `core.md` 已记录的旧 terminal ratios。

因此 corrected proof picture 是：

```math
\boxed{
\text{`6.308883...` frontier 仍是唯一 equality geometry，}
\text{但目前没有正确的 5-adic argument 将它排除。}}
```

---


<a id="dd-b01-detail-src-0134-10-1"></a>
#### 记号

令

```math
a:=\log_{10}2,
\qquad
b:=1-a=\log_{10}5,
```

```math
A:=\frac{2(1+2a)}3,
\qquad
\lambda:=\frac{2+a}{1+2a}.
```

则

```math
\lambda A=\frac{2(2+a)}3.
```

corrected frontier constant 为

```math
\boxed{
c_*:=2+3\lambda
=\frac{8+7a}{1+2a}
=6.308883577618031\ldots.}
\tag{1.1}
```

沿任意 high-funnel subsequence，使用 normalized variables

```math
\mathcal N:=\frac nS,
\quad M:=\frac mS,
\quad Q_2,N_2,Q_5,G_5,N_5,R\ge0.
```

<a id="dd-b01-detail-src-0134-10-2"></a>
#### 两个 corrected 输入

`dd-corrected-high-funnel-schmidt-2026-08-22.md` 给出 stability：

```math
\boxed{
\mathcal N
\le
2+\frac{2(2+a)}3M
-\frac{2b}{3}Q_5
+\frac{2b}{3}G_5
-\frac b3N_5
+R+o(1).
}
\tag{2.1}
```

以及 safe Schmidt budget：

```math
\boxed{
AM+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)
+2R
\le3+o(1).
}
\tag{2.2}
```

定义 normalized Schmidt slack

```math
\boxed{
\sigma_S
:=
3-\left[
AM+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)
+2R
\right].
}
\tag{2.3}
```

在渐近意义下 `sigma_S>=-o(1)`；若把 `(2.2)` 的 `o(1)` 吸收进 slack，则可取非负版本。

<a id="dd-b01-detail-src-0134-10-3"></a>
#### 直接消去 `M`

由 `(2.3)`：

```math
3\lambda-\lambda AM
=
\lambda\sigma_S
+2a\lambda Q_2+a\lambda N_2
+\frac{2b\lambda}{3}Q_5
+\frac{4b\lambda}{3}G_5
+\frac{b\lambda}{3}N_5
+2\lambda R.
\tag{3.1}
```

而

```math
\lambda A=\frac{2(2+a)}3.
```

从 `(2.1)`：

```math
\begin{aligned}
c_*-\mathcal N
\ge{}&
3\lambda-\lambda AM
+\frac{2b}{3}Q_5
-\frac{2b}{3}G_5
+\frac b3N_5-R-o(1).
\end{aligned}
```

代入 `(3.1)` 得到：

```math
\boxed{
\begin{aligned}
c_*-\mathcal N
\ge{}&
\lambda\sigma_S
+2a\lambda Q_2
+a\lambda N_2\\
&+\frac{2b(\lambda+1)}3Q_5
+\frac{2b(2\lambda-1)}3G_5\\
&+\frac{b(\lambda+1)}3N_5
+(2\lambda-1)R
-o(1).
\end{aligned}}
\tag{Quantitative-defect}
```

所有显示 coefficient 都严格为正。

<a id="dd-b01-detail-src-0134-10-4"></a>
#### 数值 coefficient

```math
\lambda=1.436294525872677\ldots,
```

因此 `(Quantitative-defect)` 中：

```math
\boxed{
\begin{array}{c|c}
\text{defect}&\text{coefficient}\\ \hline
Q_2&0.864735469791304\ldots\\
N_2&0.432367734895652\ldots\\
Q_5&1.135264530208696\ldots\\
G_5&0.872589051745354\ldots\\
N_5&0.567632265104348\ldots\\
R&1.872589051745354\ldots\\
\sigma_S&1.436294525872677\ldots
\end{array}}
\tag{4.1}
```

<a id="dd-b01-detail-src-0134-10-5"></a>
#### `epsilon`-neighborhood rigidity

若某一 subsequence 满足

```math
\mathcal N\ge c_*-\varepsilon+o(1),
```

则由 `(Quantitative-defect)`，逐项有

```math
Q_2\le\frac{\varepsilon}{0.864735469791\ldots}+o(1),
```

```math
N_2\le\frac{\varepsilon}{0.432367734896\ldots}+o(1),
```

```math
Q_5\le\frac{\varepsilon}{1.135264530209\ldots}+o(1),
```

```math
G_5\le\frac{\varepsilon}{0.872589051745\ldots}+o(1),
```

```math
N_5\le\frac{\varepsilon}{0.567632265104\ldots}+o(1),
```

```math
R\le\frac{\varepsilon}{1.872589051745\ldots}+o(1),
```

并且 Schmidt budget slack 本身也只有

```math
\sigma_S\le\frac{\varepsilon}{1.436294525873\ldots}+o(1).
```

因此 corrected terminal geometry 不只是 equality-ray rigidity；它有显式线性 stability：

```math
\boxed{
\mathcal N\to c_*
\Longrightarrow
Q_2,N_2,Q_5,G_5,N_5,R,\sigma_S\to0
}
```

且收敛速度由 `c_*-mathcal N` 线性控制。


<a id="dd-b01-detail-src-0152-11-1"></a>
#### 记号

令

```math
a:=\log_{10}2,
\qquad b:=1-a,
\qquad
\lambda:=\frac{2+a}{1+2a},
```

```math
c_*:=2+3\lambda
=6.308883577618031\ldots.
```

沿 corrected canonical high-funnel sequence 写

```math
\mathcal N:=\frac nS,
\qquad
M:=\frac mS,
\qquad
\delta:=c_*-\mathcal N\ge0.
```

前两 prefix surplus 为

```math
s_i=n_i-m_i,
\qquad
s:=s_1+s_2,
\qquad
D_s:=|s_1-s_2|.
```

因此恒有

```math
\boxed{s+D_s=2\max(s_1,s_2).}
\tag{1.1}
```

在 d-dominant sector，surplus simplex 给

```math
\boxed{s_1+s_2=s\le2.}
\tag{1.2}
```

<a id="dd-b01-detail-src-0152-11-2"></a>
#### small-factor upper 与 corrected lower 联立

旧 d-dominant Archimedean upper 本身不依赖已撤销的 unified/gap discriminant-root identification：

```math
F_-<2\cdot10^{\,2S+s+D_s+2m-n+O(1)}.
```

归一化：

```math
\frac{\log_{10}F_-}{S}
\le
2+\frac{s+D_s}{S}+2M-\mathcal N+o(1).
\tag{2.1}
```

corrected exact-small-factor lower 为

```math
\frac{\log_{10}F_-}{S}
\ge
2+b\frac TS-R-o(1).
\tag{2.2}
```

所以

```math
\boxed{
\frac{s+D_s}{S}
\ge
\mathcal N-2M+b\frac TS-R-o(1).
}
\tag{2.3}
```

corrected 5-resonance 给

```math
\frac TS
=
\frac{2M+2Q_5-2G_5+N_5}{3}.
\tag{2.4}
```

令

```math
M_*:=2.808883577618031\ldots,
\qquad
\mu:=M_*-M.
```

由 `dd-corrected-terminal-neighborhood-geometry-2026-08-22.md`：

```math
0\le\mu\le\delta+o(1).
\tag{2.5}
```

又因为 terminal constants 满足

```math
c_*-2M_*+\frac{2b}{3}M_*=2,
\tag{2.6}
```

将 `(2.4)--(2.6)` 代入 `(2.3)`：

```math
\begin{aligned}
\frac{s+D_s}{S}
\ge{}&2-\delta
+\left(2-\frac{2b}{3}\right)\mu
+\frac{2b}{3}Q_5
-\frac{2b}{3}G_5
+\frac b3N_5
-R-o(1).
\end{aligned}
\tag{2.7}
```

其中 `mu,Q_5,N_5` 三项均非负，可安全丢掉：

```math
\frac{s+D_s}{S}
\ge
2-\delta-\frac{2b}{3}G_5-R-o(1).
\tag{2.8}
```

<a id="dd-b01-detail-src-0152-11-3"></a>
#### `G_5` 与 `R` 共用同一份 slope-defect budget

quantitative defect inequality 中

```math
\delta
\ge
c_GG_5+c_RR-o(1),
```

其中

```math
c_G=\frac{2b(2\lambda-1)}3,
\qquad
c_R=2\lambda-1.
```

注意两个坏方向的 cost/defect ratio 完全相同：

```math
\frac{(2b/3)}{c_G}
=
\frac1{c_R}
=
\frac1{2\lambda-1}.
```

所以不能分别给 `G_5,R` 各花一整份 `delta`；联合最优化直接给

```math
\boxed{
\frac{2b}{3}G_5+R
\le
\frac{\delta}{2\lambda-1}+o(1).
}
\tag{3.1}
```

代回 `(2.8)`：

```math
\boxed{
2-\frac{s+D_s}{S}
\le
\left(1+\frac1{2\lambda-1}\right)\delta+o(1).
}
\tag{Digit-defect}
```

数值上

```math
2\lambda-1
=1.872589051745354\ldots,
```

```math
\boxed{
1+\frac1{2\lambda-1}
=1.534019997109321\ldots.
}
\tag{3.2}
```

这改进了逐 defect 分别粗估得到的更差常数。

<a id="dd-b01-detail-src-0152-11-4"></a>
#### surplus polarization

定义

```math
\boxed{
\kappa_{\rm dig}
:=\frac12\left(1+\frac1{2\lambda-1}\right)
=0.767009998554660\ldots.
}
\tag{4.1}
```

由 `(1.1)` 与 `(Digit-defect)`：

```math
\boxed{
\frac{\max(s_1,s_2)}S
\ge
1-\kappa_{\rm dig}\delta-o(1).
}
\tag{4.2}
```

交换前两块后可设

```math
s_1=\max(s_1,s_2).
```

则

```math
\boxed{
s_1\ge(1-\kappa_{\rm dig}\delta)S-o(S).}
\tag{4.3}
```

由 `s_1+s_2<=2`：

```math
\boxed{
s_2\le-(1-\kappa_{\rm dig}\delta)S+O(1)+o(S).}
\tag{4.4}
```

<a id="dd-b01-detail-src-0152-11-5"></a>
#### block-length polarization

使用

```math
m_1+m_2=S,
\qquad
n_i=m_i+s_i\ge1.
```

由 `n_2>=1` 与 `(4.4)`：

```math
m_2\ge1-s_2
\ge(1-\kappa_{\rm dig}\delta)S-o(S).
```

故

```math
\boxed{
m_1\le\kappa_{\rm dig}\delta S+o(S),}
\tag{5.1}
```

```math
\boxed{
m_2\ge(1-\kappa_{\rm dig}\delta)S-o(S).}
\tag{5.2}
```

同时 `n_1=m_1+s_1>=s_1` 给

```math
\boxed{
n_1\ge(1-\kappa_{\rm dig}\delta)S-o(S).}
\tag{5.3}
```

而

```math
n_1+n_2=S+s_1+s_2\le S+2
```

所以

```math
\boxed{
n_2\le\kappa_{\rm dig}\delta S+o(S).}
\tag{5.4}
```

因此交换前两块后，统一得到

```math
\boxed{
\begin{aligned}
&m_1,n_2\le0.767009998555\,\delta S+o(S),\\
&m_2,n_1\ge(1-0.767009998555\,\delta)S-o(S).
\end{aligned}}
\tag{Quantitative-prefix-polarization}
```

当 `delta->0` 时恢复旧 equality terminal shape

```math
(m_1,m_2;n_1,n_2)
=(o(S),S-o(S);S-o(S),o(S))
```

（允许交换 prefix labels）。

<a id="dd-b01-detail-src-0152-11-6"></a>
#### 数值含义

例如若

```math
\frac nS\ge c_*-0.01,
```

则渐近上两个短 prefix blocks 的长度比例至多约为

```math
0.00767010,
```

而两个长块至少占

```math
0.99232990
```

的 `S` 尺度。

所以 digit polarization 对 slope defect 是线性稳定的，并且常数小于 `0.77`。


<a id="dd-b01-detail-src-0155-11-1"></a>
#### general moving-core decomposition

一般 DD reduced-tail moving odd core有 exact decomposition

```math
\boxed{V=v_1v_2,}
\tag{1.1}
```

其中：

- `v_1` 对应 pair-max `(b_1,b_3)`；
- `v_2` 对应 pair-max `(b_2,b_3)`；
- canonical denominator normal form给 `v_1|b_1`, `v_2|b_2`。

在 canonical S-unit phase中

```math
G=\gamma V,
\qquad G=b_1b_2,
\qquad (V,10)=1.
\tag{1.2}
```

交换前两 prefix labels后，quantitative digit polarization取长 denominator为 `b_2`。

<a id="dd-b01-detail-src-0155-11-2"></a>
#### 小 channel 的定量 upper

上一文件证明过程中有

```math
\frac{m_1}{S}
\le
\frac\delta2+\frac b3G_5+\frac R2+o(1),
\tag{2.1}
```

其中

```math
a=\log_{10}2,
\qquad b=1-a,
\qquad
\lambda=\frac{2+a}{1+2a}.
```

由 `v_1|b_1` 与 `b_1<10^{m_1}`：

```math
\frac{\log_{10}v_1}{S}
\le
\frac\delta2+\frac b3G_5+\frac R2+o(1).
```

quantitative defect中

```math
c_{G_5}=\frac{2b(2\lambda-1)}3,
\qquad
c_R=2\lambda-1.
```

两个 cost ratio相同：

```math
\frac{b/3}{c_{G_5}}
=
\frac{1/2}{c_R}
=
\frac1{2(2\lambda-1)}.
```

故

```math
\boxed{
\frac{\log_{10}v_1}{S}
\le
\left(\frac12+\frac1{2(2\lambda-1)}\right)\delta+o(1).
}
```

利用 `1/(2lambda-1)=(1+2a)/3`：

```math
\boxed{
\frac{\log_{10}v_1}{S}
\le
\frac{2+a}{3}\,\delta+o(1)
=0.767009998554660\ldots\,\delta+o(1).
}
\tag{Small-channel}
```

这与短 digit-block constant恰好相同。

<a id="dd-b01-detail-src-0155-11-3"></a>
#### `gamma` height 的显式 upper

写

```math
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0,
\qquad
\Gamma:=\frac{\log_{10}\gamma}{S}=aG_2+bG_5+R.
```

`dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md` 中更精确的中间式为

```math
aG_2
\le
\frac\delta2+aQ_2+\frac b3G_5+\frac R2+o(1).
```

所以

```math
\Gamma
\le
\frac\delta2
+aQ_2
+\frac{4b}{3}G_5
+\frac{3R}{2}
+o(1).
\tag{3.1}
```

后三项共用 quantitative-defect budget。其 cost ratios为

```math
\frac{a}{c_{Q_2}}=\frac1{2\lambda},
```

```math
\frac{4b/3}{c_{G_5}}=\frac2{2\lambda-1},
```

```math
\frac{3/2}{c_R}=\frac{3}{2(2\lambda-1)}.
```

最大值为中间项，因此

```math
\boxed{
\Gamma
\le
\left(\frac12+\frac2{2\lambda-1}\right)\delta+o(1).
}
\tag{Gamma-window}
```

即

```math
\boxed{
\frac{\log_{10}\gamma}{S}
\le
1.568039994218642\ldots\,\delta+o(1).
}
\tag{3.2}
```

<a id="dd-b01-detail-src-0155-11-4"></a>
#### `V` 仍保持 near-`S` height

因为 `b_i` 分别是 `m_i` 位正整数：

```math
10^{m_i-1}\le b_i<10^{m_i}.
```

所以

```math
10^{S-2}\le G=b_1b_2<10^S,
```

即

```math
\frac{\log_{10}G}{S}=1+o(1).
```

由 `G=gamma V` 与 `(Gamma-window)`：

```math
\boxed{
1-\left(\frac12+\frac2{2\lambda-1}\right)\delta-o(1)
\le
\frac{\log_{10}V}{S}
\le1+o(1).
}
\tag{V-window}
```

数值 lower coefficient为 `1.568039994218642...`。

<a id="dd-b01-detail-src-0155-11-5"></a>
#### 大 one-channel core

由 `V=v_1v_2`：

```math
\frac{\log v_2}{S}
=
\frac{\log V}{S}-\frac{\log v_1}{S}.
```

使用 `(Small-channel)` 与 `(V-window)`：

```math
\boxed{
\frac{\log_{10}v_2}{S}
\ge
1-C_{\rm one}\delta-o(1),
}
\tag{5.1}
```

其中

```math
\begin{aligned}
C_{\rm one}
&=
\left(\frac12+\frac2{2\lambda-1}\right)
+\left(\frac12+\frac1{2(2\lambda-1)}\right)\\
&=1+\frac{5}{2(2\lambda-1)}.
\end{aligned}
```

利用 `1/(2lambda-1)=(1+2a)/3`：

```math
\boxed{
C_{\rm one}
=1+\frac{5(1+2a)}6
=2.335049992773302\ldots.
}
\tag{5.2}
```

所以

```math
\boxed{
\frac{\log_{10}v_2}{S}
\ge
1-2.335049992773302\,\delta-o(1).
}
\tag{Quantitative-one-channel}
```

当 `delta->0` 时恢复 equality frontier 的 `log v_2=S+o(S)`。

<a id="dd-b01-detail-src-0155-11-6"></a>
#### Gaussian orientation continuation

对 `v_2` 的 odd moving primes，general denominator prime graph与integer sphere仍给：

```math
p\equiv1\pmod4,
```

并在 `(b_2,b_3)` pair-max channel产生 square-depth Gaussian contact。删去只含 bounded/exceptional coefficient overlap的部分后，可选择 oriented Gaussian integer `Pi_delta` 使

```math
\boxed{
N(\Pi_\delta)=v_2,
\qquad
\Pi_\delta^2\mid y_2+i y_3.
}
\tag{6.1}
```

因此 corrected terminal neighborhood中仍存在一个 norm height至少

```math
(1-2.335049992774\delta)S-o(S)
```

的单一 moving Gaussian channel；另一 channel只有 `0.767010 delta S+o(S)` 高度。

<a id="dd-b01-detail-src-0155-11-7"></a>
#### 对 `b_2` 的 consequence

由 `v_2|b_2` 与 `b_2<10^{m_2}`：

```math
\log(b_2/v_2)
\le
m_2-\log v_2+O(1)
\le
C_{\rm one}\delta S+o(S),
```

故按 logarithmic height：

```math
\boxed{
b_2=v_2\cdot10^{O(\delta S)+o(S)}.}
\tag{7.1}
```

这就是 equality statement `b_2=C_L*10^{o(S)}` 的 quantitative neighborhood版本。


来源：`SRC-0135:23–476`；`SRC-0134:10–226`；`SRC-0152:11–362`；`SRC-0155:11–313`。原文保全，当前论证以本节为准。

<a id="dd-b02"></a>
### DD-B02　actual small factor、source split 与共同尺度

**状态：已严格完成。** gcd-normal 身份和 corrected hard sheet 的明确假设；chosen orientation 不删除。

依赖：[DD-B01](#dd-b01)

核对：`dd-gap-reconstruction`

<a id="dd-b02-detail-src-0190-525-1"></a>
#### gcd-normal form

写

```math
\boxed{
\kappa=\gamma u,\qquad
G=\gamma v,\qquad
(u,v)=1.
}
\tag{1.1}

```
再令

```math
\boxed{
d_0=(u,Q),}
\qquad
\boxed{u=d_0r,\qquad Q=d_0q,}
\tag{1.2}

```
则

```math
\boxed{(r,q)=1,\qquad r\mid10^m.}
\tag{1.3}

`core.md` 的 tail recovery为

```
```math
\boxed{b_3=vt,\qquad ut=10^mQ.}
\tag{1.4}

```
---

<a id="dd-b02-detail-src-0190-525-2"></a>
#### tail normalization 精确等于 reduced pair

把 `(1.2)` 代入 `(1.4)`：

```math
d_0rt=10^md_0q.
```

约去 `d_0`：

```math
\boxed{rt=10^mq.}
\tag{2.1}

```
由 `(r,q)=1` 与 `r|10^m`：

```math
\boxed{
t=\frac{10^m}{r}q.}
\tag{2.2}

```
又 `(u,v)=1` 且 `r|u`，所以

```math
(r,v)=1.
```

因此

```math
\begin{aligned}
\omega
&=(10^m,b_3)\\
&=\left(10^m,
 v\frac{10^m}{r}q\right)\\
&=\frac{10^m}{r}(r,vq)\\
&=\frac{10^m}{r}.
\end{aligned}
```

故 DD tail normalization

```math
L=10^m/\omega,\qquad\tau=b_3/\omega
```

精确化为

```math
\boxed{L=r,\qquad\tau=vq.}
\tag{Tail-general}

```
此外 `(u,v)=1` 还给 `(d_0,v)=1`。于是

```math
\eta=(Q,\tau)
=(d_0q,vq)
=q(d_0,v)
=\boxed q.
\tag{2.3}

```
所以 overlap parameterization 中的 `eta` 正是 gcd-normal reduced source factor `q`。

---

<a id="dd-b02-detail-src-0190-525-3"></a>
#### reduced source factor整除 decimal determinant

DD determinant为

```math
\boxed{E=b_3A_{12}10^d-a_3Q.}
\tag{3.1}

```
由 `(Tail-general)`：

```math
b_3=\omega vq,\qquad Q=d_0q.
```

两项都含 `q`，故

```math
\boxed{q\mid E.}
\tag{3.2}

```
定义

```math
\boxed{E_0:=E/q\in\mathbf Z_{>0}.}
\tag{3.3}

```
---

<a id="dd-b02-detail-src-0190-525-4"></a>
#### universal identity 的 exact cancellation

通用恒等式为

```math
\boxed{
F_-Q(\kappa+G)=E\kappa(\kappa+2G).
}
\tag{4.1}

```
代入

```math
Q=d_0q,
\quad
\kappa=\gamma u,
\quad
G=\gamma v,
\quad
u=d_0r,
\quad
E=qE_0:
```

```math
F_-d_0q\,\gamma(u+v)
=qE_0\,\gamma d_0r\,\gamma(u+2v).
```

约去 `d_0 q gamma`：

```math
\boxed{
F_-(u+v)=E_0\gamma r(u+2v).
}
\tag{4.2}

```
因为 `(u,v)=1`：

```math
(u+v,r)=1
```

（`r|u`），并且

```math
(u+v,u+2v)=(u+v,v)=1.
```

所以

```math
\boxed{(u+v,r(u+2v))=1.}
\tag{4.3}

```
由 `(4.2)`：

```math
\boxed{u+v\mid E_0\gamma.}
\tag{4.4}

```
定义

```math
\boxed{
R:=\frac{E_0\gamma}{u+v}\in\mathbf Z_{>0}.
}
\tag{4.5}

```
则

```math
\boxed{F_-=r(u+2v)R.}
\tag{4.6}

```
---

<a id="dd-b02-detail-src-0190-525-5"></a>
#### 与 §35 exact factorization 对齐

`core.md` §35 已有

```math
\boxed{
F_-=a\,g_*
\frac{L(LQ+2\tau)}{\tau}.
}
\tag{5.1}

```
使用

```math
L=r,\qquad Q=d_0q,\qquad\tau=vq,
```

有

```math
LQ+2\tau
=rd_0q+2vq
=q(u+2v).
```

故

```math
\begin{aligned}
F_-
&=a g_*
\frac{r\,q(u+2v)}{vq}\\
&=\boxed{
a\frac{g_*}{v}\,r(u+2v).
}
\end{aligned}
\tag{5.2}

```
比较 `(4.6)` 与 `(5.2)`：

```math
\boxed{
R=a\frac{g_*}{v}.}
\tag{R-general}

§37 overlap 参数化本来就给

```
```math
g_*=vc\lambda r_*,
```

所以

```math
R=ac\lambda r_*
```

确为正整数。

最终 universal normalization：

```math
\boxed{
F_-=r(u+2v)
\;a\frac{g_*}{v}.
}
\tag{Exact-Fminus-general}

```
---


<a id="dd-b02-detail-src-0133-31-1"></a>
#### local notation

固定
```math
p^x\Vert X_Q,
\qquad p\nmid10.
```
写
```math
E=v_p(b_1)=v_p(b_2),
\qquad
j=v_p(b_3),
\qquad
M:=\max(E,j),
```
```math
c=v_p(C_Q),
\qquad
t=v_p(C)=v_p(A_{12}),
```
```math
n_0=v_p(N_0),
\qquad
r=(j-E)_+,
\qquad
\alpha=v_p(a).
```

`tail-rough-cq-excess` 已严格证明
```math
\boxed{
x=\max(c-j-\min(E,j),0).}
\tag{1.1}
```
本文只讨论 `x>0`。

---

<a id="dd-b02-detail-src-0133-31-2"></a>
#### 无需 transfer theorem 的五层定义

定义 remainder sequence：
```math
x_0:=x,
```
```math
\boxed{e_B:=\min(x_0,t),\qquad x_1:=x_0-e_B,}
\tag{2.1}
```
```math
\boxed{e_a:=\min(x_1,\alpha),\qquad x_2:=x_1-e_a,}
\tag{2.2}
```
```math
\boxed{e_N:=\min(x_2,n_0),\qquad x_3:=x_2-e_N,}
\tag{2.3}
```
```math
\boxed{e_3:=\min(x_3,r),\qquad h:=x_3-e_3.}
\tag{2.4}

```
于是完全由定义得到
```math
\boxed{x=e_B+e_a+e_N+e_3+h.}
\tag{Corrected-local-split}

```
没有使用 `General-transfer-local`，也没有假设 `h=0`。

逐 prime 聚合定义
```math
X_B:=\prod p^{e_B},
\quad
X_a:=\prod p^{e_a},
\quad
X_N:=\prod p^{e_N},
\quad
X_3:=\prod p^{e_3},
\quad
X_H:=\prod p^h.
```
因此全局严格有
```math
\boxed{
X_Q=X_BX_aX_NX_3X_H.
}
\tag{Corrected-global-split}

```
---

<a id="dd-b02-detail-src-0133-31-3"></a>
#### 前四层都有真实 reader

<a id="dd-b02-detail-src-0133-31-4"></a>
#### bottom

因为 `e_B<=t` 且 `p^x|C_Q|Q`，
```math
p^{e_B}\mid(A_{12},Q).
```
所以
```math
\boxed{X_B\mid C_{12}:=(A_{12},Q).}
\tag{3.1}

```
已有 exact bottom charge 对任意该因子成立：
```math
\boxed{X_BG<F_-.}
\tag{Bottom-charge-corrected}

<a id="dd-b02-detail-src-0133-31-5"></a>
```
#### gap

由定义 `e_a<=alpha=v_p(a)`：
```math
\boxed{X_a\mid a.}
\tag{3.2}
```
而 existing gap factorization 给
```math
\boxed{X_aQ<F_-.}
\tag{Gap-charge-corrected}

<a id="dd-b02-detail-src-0133-31-6"></a>
```
#### prefix norm

直接由 `e_N<=n_0`：
```math
\boxed{X_N\mid\operatorname{core}_{10}(N_0).}
\tag{3.3}

<a id="dd-b02-detail-src-0133-31-7"></a>
```
#### third denominator

由 `e_3<=r=v_p(R_3^{\rm den})`：
```math
\boxed{X_3\mid\operatorname{core}_{10}(R_3^{\rm den}).}
\tag{3.4}

`R_3^{den}|Z_0a` 的 projective divisibility只使用 sphere/projective denominator formula，
```
不依赖已暂停的 general-transfer contradiction。因此仍有
```math
\boxed{X_3\mid\operatorname{core}_{10}(Z_0a).}
\tag{3.5}

```
唯一没有预先 reader 的就是 `X_H`。

---

<a id="dd-b02-detail-src-0133-31-8"></a>
#### hard residual 为正时自动进入 corrected hard sheet

若
```math
\boxed{h>0,}
\tag{4.1}
```
则 `(2.1)--(2.4)` 中四个 `min` 都必须取满容量：
```math
\boxed{
e_B=t,
\qquad e_a=\alpha,
\qquad e_N=n_0,
\qquad e_3=r.}
\tag{4.2}

```
特别地
```math
x>t,
\qquad x>n_0,
\qquad x>r.
\tag{4.3}
```
所以 `dd-general-transfer-correction` 中的 hard hypothesis成立。

旧 general-transfer proof 的 §1–4 不使用错误的 unified/gap root identification；其
`Gap-baseline-lock` 因而仍给
```math
\boxed{
\alpha=t+(E-j)_+.
}
\tag{Gap-lock-hard}

```
于是
```math
\boxed{
h=x-t-\alpha-n_0-r.}
\tag{4.4}

```
---

<a id="dd-b02-detail-src-0133-31-9"></a>
#### hard source 的 exact ledger

将 `(1.1)` 与 `(Gap-lock-hard)` 代入 `(4.4)`。

<a id="dd-b02-detail-src-0133-31-10"></a>
#### `E>=j`

此时
```math
x=c-2j,
\qquad
\alpha=t+E-j,
\qquad
r=0.
```
故
```math
\begin{aligned}
h
&=c-2j-t-(t+E-j)-n_0\\
&=c-2t-n_0-E-j.
\end{aligned}
```

<a id="dd-b02-detail-src-0133-31-11"></a>
#### `j>E`

此时
```math
x=c-j-E,
\qquad
\alpha=t,
\qquad
r=j-E.
```
故
```math
\begin{aligned}
h
&=c-j-E-t-t-n_0-(j-E)\\
&=c-2t-n_0-2j.
\end{aligned}
```

两式用 `M=max(E,j)` 统一为
```math
\boxed{
 c=h+2t+n_0+M+j.
}
\tag{Hard-source-ledger}

```
定义 local hard cofactor depth
```math
\boxed{
y:=c-h=2t+n_0+M+j.}
\tag{5.1}
```
于是
```math
\boxed{c=h+y}
\tag{5.2}
```
为 exact equality。

这条 equality 是 corrected post-tail 中替代“`h=0`”的核心结构。

---

<a id="dd-b02-detail-src-0133-31-12"></a>
#### hard source-square / deep 二分

对 `h>0` 的 prime 按
```math
\boxed{h\le y}
\tag{6.1}
```
与
```math
\boxed{h>y}
\tag{6.2}
```
分类。

<a id="dd-b02-detail-src-0133-31-13"></a>
#### source-square hard part

若 `h<=y`，则
```math
2h\le h+y=c,
```
所以
```math
\boxed{p^{2h}\mid C_Q.}
\tag{Hard-square-local}

```
令
```math
X_{H,S}:=\prod_{h\le y}p^h.
```
各 prime support 不交，故
```math
\boxed{X_{H,S}^2\mid C_Q.}
\tag{Hard-square-global}

```
于是
```math
\boxed{
\log_{10}X_{H,S}<\frac S2.
}
\tag{Hard-square-half-S}

<a id="dd-b02-detail-src-0133-31-14"></a>
```
#### deep hard source

若 `h>y`，定义
```math
X_{H,D}:=\prod_{h>y}p^h,
\qquad
Y_{H,D}:=\prod_{h>y}p^y.
```
由 `(5.2)`：
```math
\boxed{X_{H,D}Y_{H,D}\mid C_Q.}
\tag{Deep-hard-source-product}

```
并且逐 prime
```math
\boxed{y<h.}
\tag{6.3}

```
把 cofactor进一步按 exact layers写成
```math
T_H:=\prod p^t,
\quad
N_H:=\prod p^{n_0},
\quad
M_H:=\prod p^M,
\quad
J_H:=\prod p^j
```
（均只在 deep-hard support上），则
```math
\boxed{
Y_{H,D}=T_H^2N_HM_HJ_H.
}
\tag{Deep-hard-cofactor}

```
所以
```math
\boxed{
\log X_{H,D}
+2\log T_H
+\log N_H
+\log M_H
+\log J_H
<S.
}
\tag{Deep-hard-height-tradeoff}

```
若 `X_{H,D}` 接近整份 `S` 高度，则 coefficient、prefix norm 与全部 denominator maximum
baseline都自动只有 sublinear aggregate height。

这比原 `X_Q` frontier 更精确：唯一 full-height escape 必须是一个
**asymptotically baseline-free pure source cancellation core**。

---

<a id="dd-b02-detail-src-0133-31-15"></a>
#### corrected second-Schmidt bootstrap

`tail-rough-cq-excess` 的原始、仍有效 second-Schmidt inequality为
```math
\log R_x+\log(g_*/v)
\ge S-\log X_Q-o(S),
```
左侧是真实 `F_-` factors，因此写 `f=log F_-`：
```math
f\ge S-\log X_Q-o(S).
\tag{7.1}

```
由 `Corrected-global-split`：
```math
\log X_Q
=\log X_B+\log X_a
+\log X_N+\log X_3+\log X_H.
```

而两条 exact small-factor charge给
```math
\log X_B\le f-S+O(1),
\qquad
\log X_a\le f-S+O(1).
```
代回 `(7.1)`：
```math
\boxed{
3f+\log(X_NX_3X_H)
\ge3S-o(S).
}
\tag{Corrected-triple-bootstrap}

```
这是此前 triple bootstrap 的 corrected version：
它不再把 residual 错误识别成 `Z_0-only`；真正 residual 是
```math
\boxed{X_NX_3X_H.}
```
其中前两项有 concrete norm/projective readers，最后一项再按
```math
X_H=X_{H,S}X_{H,D}
```
分成 half-`S` source-square 与 deep pure-source core。

---

<a id="dd-b02-detail-src-0133-31-16"></a>
#### deep source 对 bootstrap 的 exact tradeoff

若暂时把其它 residual reader单独记账，只看 deep-hard contribution `X_{H,D}`，
`Deep-hard-source-product` 给
```math
\log X_{H,D}\le S-\log Y_{H,D}+O(1).
```
所以它在 `Corrected-triple-bootstrap` 中造成的最坏 loss可改写为 source-cofactor tradeoff。

特别地，危险极限
```math
\log X_{H,D}=S-o(S)
```
自动强迫
```math
\boxed{
\log Y_{H,D}=o(S),
}
```
即
```math
\log T_H,
\quad\log N_H,
\quad\log M_H,
\quad\log J_H
=o(S).
```

研究目标见 [路线记录](RESEARCH.md)。

```math
\boxed{
\begin{gathered}
X_{H,D}\mid C_Q,\qquad
\log X_{H,D}=S-o(S),\\
\text{coefficient / prefix norm / denominator baselines}=10^{o(S)},\\
\text{local unit-Hensel 已由 sphere-parent 精确支付，无独立 local height。}
\end{gathered}}
\tag{Pure-source-terminal}

```
这说明 corrected frontier 的下一机制必须真正是 global source/digit-shell mechanism。

---


<a id="dd-b02-detail-src-0126-27-1"></a>
#### fixed factor split 的 determinant box只读取 decimal widths

沿前一 theorem notation：

```math
V=v_1v_2,
\qquad
\tau_1=b_1/v_1,
\qquad
\tau_2=b_2/v_2,
```

且同一 fixed phase/factor fiber 中

```math
U\mid
\Delta_\tau
:=\tau_2\tau_1'-\tau_2'\tau_1.
\tag{1.1}
```

因为 `b_1,b_1'` 都是 `m_1` 位正整数：

```math
0<\tau_1,\tau_1'<\frac{10^{m_1}}{v_1}.
```

同理

```math
0<\tau_2,\tau_2'<\frac{10^{m_2}}{v_2}.
```

于是两个 cross products都有 exact decimal-box upper

```math
\tau_2\tau_1'
<\frac{10^{m_1+m_2}}{v_1v_2}
=\frac{10^S}{V},
```

```math
\tau_2'\tau_1
<\frac{10^S}{V}.
```

所以若 determinant非零：

```math
\boxed{
0<|\Delta_\tau|
<\frac{2\,10^S}{V}.}
\tag{Det-box-sharp}
```

这比前一 theorem 的

```math
10^{(\kappa_{\rm dig}+C_{\rm one})\delta S+o(S)}
```

严格更自然：它不把两个 candidates 的 individual cofactor maxima独立相乘，而直接使用固定 decimal widths 与固定 factor split。

---

<a id="dd-b02-detail-src-0126-27-2"></a>
#### `UV` 的 uncoarsened lower

仍令

```math
a:=\log_{10}2,
\qquad b:=1-a,
```

```math
A:=\frac{2(1+2a)}3,
\qquad
\lambda:=\frac{2+a}{1+2a},
```

```math
U_*:=0.691116422381969\ldots,
\qquad
\mu:=M_*-M.
```

已有 uncoarsened `U` identity

```math
\boxed{
\frac{\log_{10}U}{S}-U_*
=
\frac{2b}{3}\mu
-aG_2
-\frac{2b}{3}Q_5
-\frac b3G_5
-\frac b3N_5
-R+o(1).}
\tag{2.1}
```

由

```math
G=\gamma V,
\qquad
\frac{\log_{10}G}{S}=1+o(1),
```

有

```math
\boxed{
\frac{\log_{10}V}{S}
=1-aG_2-bG_5-R+o(1).}
\tag{2.2}
```

相加：

```math
\begin{aligned}
\frac{\log_{10}(UV)}S-(1+U_*)
={}&\frac{2b}{3}\mu
-2aG_2
-\frac{2b}{3}Q_5\\
&-\frac{4b}{3}G_5
-\frac b3N_5-2R+o(1).
\end{aligned}
\tag{2.3}
```

---

<a id="dd-b02-detail-src-0126-27-3"></a>
#### 用同一个 short denominator读取 `G_2`

前一 sharp product-lock continuation已经恢复了 digit theorem 中未粗化的 short-denominator upper：

```math
\boxed{
\begin{aligned}
\frac{m_1}{S}
\le{}&\frac\delta2
-\left(1-\frac b3\right)\mu
-\frac b3Q_5
+\frac b3G_5\\
&-\frac b6N_5
+\frac R2+o(1).
\end{aligned}}
\tag{m1-sharp}
```

同时 two-adic theorem给

```math
\boxed{
aG_2
\le\frac{m_1}{S}+aQ_2+o(1).}
\tag{G2-via-m1}
```

在 `(2.3)` 中使用

```math
-2aG_2
\ge
-2\frac{m_1}{S}-2aQ_2-o(1),
```

再代入 `(m1-sharp)`。`Q_5,N_5` 精确 cancellation，得到

```math
\boxed{
\frac{\log_{10}(UV)}S-(1+U_*)
\ge
-\delta+2\mu-2aQ_2-2bG_5-3R-o(1).}
\tag{UV-prebudget}
```

---

<a id="dd-b02-detail-src-0126-27-4"></a>
#### `(Mu-budget)` 后所有 correction 都变成正项

沿用 exact normalized identity

```math
\boxed{
A\mu
=\sigma_S
+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)
+2R+o(1).}
\tag{Mu-budget}
```

代入 `(UV-prebudget)`。利用

```math
\frac2A=2\lambda-1,
```

整理得到

```math
\boxed{
\begin{aligned}
\frac{\log_{10}(UV)}S
\ge{}&1+U_*-\delta
+(2\lambda-1)\sigma_S\\
&+4a(\lambda-1)Q_2
+a(2\lambda-1)N_2\\
&+\frac{2b(2\lambda-1)}3Q_5
+\frac{2b(4\lambda-5)}3G_5\\
&+\frac{b(2\lambda-1)}3N_5
+(4\lambda-5)R-o(1).
\end{aligned}}
\tag{UV-sharp-full}
```

corrected constant满足

```math
\lambda=1.436294525872677\ldots>\frac54,
```

所以

```math
4\lambda-5>0.
```

所有显示 correction 均非负，于是得到 universal sharp lower

```math
\boxed{
\frac{\log_{10}(UV)}S
\ge1+U_*-\delta-o(1).}
\tag{UV-sharp}
```

---

<a id="dd-b02-detail-src-0126-27-5"></a>
#### cofactor projective ratio在整个 one-channel neighborhood 唯一

由 `(Det-box-sharp)`，若两个 cofactor ratios不同，则

```math
0<|\Delta_\tau|<2\,10^S/V.
```

若

```math
UV>2\,10^S,
```

则右侧严格小于 `U`，与 `U|Delta_tau` 矛盾。

`(UV-sharp)` 给

```math
\frac1S\log_{10}\frac{UV}{10^S}
\ge U_*-\delta-o(1).
```

因此对任意 fixed

```math
\boxed{\delta<U_*}
\tag{5.1}
```

sufficiently large `S` 上都有 `UV>2*10^S`，从而

```math
\boxed{
\tau_2/\tau_1
\text{ 在 fixed phase/factor fiber 中至多一个}.}
\tag{Projective-cofactor-lock-sharp}
```

数值上

```math
U_*=0.691116422381969\ldots.
```

但 quantitative one-channel theorem 的现行作用域已经固定

```math
\delta\le\frac12.
```

所以在当前证明树中可以直接写成：

```math
\boxed{
\text{整个 corrected quantitative one-channel neighborhood }
(\delta\le1/2)
\text{ 都满足 cofactor projective uniqueness}.}
\tag{One-channel-ray-global}
```

---

<a id="dd-b02-detail-src-0126-27-6"></a>
#### common-scale ray 与 entropy sharpen 全部扩展到 `delta<=1/2`

前一 common-scale theorem §§5--8 在 projective ratio唯一之后只使用 exact algebra：

1. 取 primitive ratio `s/r`；
2. 写 `tau_1=kr,tau_2=ks`；
3. 从 `Uq=kD` 抽出 `k=U_0 ell`；
4. 得到
```math
   (b_1,b_2,b_3,q,\gamma)
   =(\ell\bar b_1,\ell\bar b_2,\ell\bar b_3,
   \ell\bar q,\ell^2\bar\gamma);
```
5. common scale `ell` 对 padded-width Exact-Lift equality 是 homogeneous direction；
6. fixed `(sigma_S,R)` layer 中 scale multiplicity至多 `10^{(R/2)S+o(S)}`。

这些步骤不再需要原 `delta_ray=0.15696...` 的额外假设。因此它们全部扩展到 one-channel 的完整现行范围：

```math
\boxed{
N_{\rm den/SU}
\le
10^{(\sigma_S+R/2)S+o(S)}
\qquad(\delta\le1/2).}
\tag{Ray-refined-den-entropy-sharp}
```

注意 uniform worst-case coarse bound依然可能由 `sigma_S` 支配，故本文仍不单独给出 strict slope gap；但 rough `gamma` 作为独立 projective shape 的解释现在已经在整个 one-channel neighborhood 中被撤销。

---

<a id="dd-b02-detail-src-0126-27-7"></a>
#### 与 sharp `qZ` lock 的覆盖关系

sharp product-lock theorem作用于

```math
\delta<0.191116422381969\ldots,
```

而 common-scale ray现在作用于整个

```math
\delta\le1/2.
```

所以 product-lock neighborhood 自动拥有 scale-ray structure。特别地，在

```math
\delta<0.191116422381969\ldots
```

内同时有：

- `qZ` ordinary least-residue lock；
- fixed-`v_2` denominator reconstruction；
- common-scale-ray quotient；
- fixed-gap/suffix numerator conditional reconstruction。旧 fixed-denominator
  joint numerator collapse在 2026-09-30 因循环条件失效，见
  [`非循环修复`](#dd-08)。

这使 terminal 小邻域的非齐次 denominator shape residual只剩 Farey/S-unit primitive phase与 `V` 的 divisor split。

---


<a id="dd-b02-detail-src-0123-31-1"></a>
#### generic carry 强迫 `g_0 | Sigma`

上一 pair-max neighborhood theorem 已从 general overlap normalization恢复 exact carry

```math
\boxed{
 g_0Ua_3
 =g_0B10^dVA_{12}-\Sigma R_0,}
\tag{Carry}
```

其中

```math
(R_0,g_0)=1,
\qquad
\Sigma=2^HZ+5^TU.
```

移项：

```math
\Sigma R_0
=g_0\left(B10^dVA_{12}-Ua_3\right).
```

右边被 `g_0` 整除，而 `(R_0,g_0)=1`，故 Euclid lemma 直接给

```math
\boxed{g_0\mid\Sigma.}
\tag{g0-Sigma}
```

定义整数

```math
\boxed{\Sigma_0:=\Sigma/g_0.}
\tag{1.1}
```

则 `(Carry)` 可以除以 `g_0`：

```math
\boxed{
Ua_3
=B10^dVA_{12}-\Sigma_0R_0.}
\tag{Carry-primitive}
```

这条 divisibility 不需要 equality frontier 的 slow-height 结论。

---

<a id="dd-b02-detail-src-0123-31-2"></a>
#### 模 `U` 得到 full fixed `A_12` period

对 `(Carry-primitive)` 模 `U`：

```math
\boxed{
B10^dV A_{12}
\equiv
\Sigma_0R_0
\pmod U.}
\tag{U-CRT-raw}
```

canonical phase已有

```math
(U,10)=1,
\qquad
(U,V)=1.
```

而

```math
B=\frac{10^m}{2\cdot5^T}
```

只含 `2,5` 素因子。因此

```math
\boxed{(U,B10^dV)=1.}
\tag{2.1}
```

所以 `(U-CRT-raw)` 对 rational integer `A_12` 给完整 effective period `U`：

```math
\boxed{
A_{12}\equiv\rho_U\pmod U.}
\tag{U-CRT}
```

在固定 denominator/S-unit data 与 gap fiber `(R_0,g_0)` 后，右边 residue 完全固定；不需要固定 `a_3`。

---

<a id="dd-b02-detail-src-0123-31-3"></a>
#### `U` 与 pair-max `v_2` 严格互素

quantitative one-channel decomposition为

```math
V=v_1v_2,
```

故

```math
v_2\mid V.
```

canonical S-unit phase有

```math
(U,V)=1.
```

于是 exact 地

```math
\boxed{(U,v_2)=1.}
\tag{U-v2-transverse}
```

上一 pair-max fixed CRT theorem给 fixed `(R_0,g_0,a_2)` fiber 中

```math
\boxed{A_{12}\equiv\rho_V\pmod{v_2}.}
\tag{3.1}
```

所以 `(U-CRT)` 与 `(3.1)` 的联合 period是 exact product

```math
\boxed{M_{UV}:=Uv_2.}
\tag{3.2}
```

---

<a id="dd-b02-detail-src-0123-31-4"></a>
#### 不分别花两次 defect budget

若只把既有

```math
\log U/S\ge U_*-(1+a)\delta-o(1)
```

与

```math
\log v_2/S\ge1-C_{\rm one}\delta-o(1)
```

相加，会重复允许同一 defect 在两条 bound 中各自达到最坏值。这里重新做联合 ledger。

记

```math
a:=\log_{10}2,
\qquad
b:=1-a,
\qquad
\lambda:=\frac{2+a}{1+2a},
```

```math
A:=\frac{2(1+2a)}3,
\qquad
\mu:=M_*-M.
```

individual `U` identity为

```math
\frac{\log U}{S}-U_*
=
\frac{2b}{3}\mu
-aG_2
-\frac{2b}{3}Q_5
-\frac b3G_5
-\frac b3N_5
-R+o(1).
\tag{4.1}
```

one-channel proof在粗化前给

```math
\frac{\log v_1}{S}
\le
\frac\delta2+\frac b3G_5+\frac R2+o(1),
\tag{4.2}
```

而

```math
\frac{\log V}{S}
=1-aG_2-bG_5-R+o(1).
\tag{4.3}
```

所以

```math
\begin{aligned}
\frac{\log v_2}{S}
\ge{}&1-
rac\delta2
-aG_2-
rac{4b}{3}G_5-
rac{3R}{2}-o(1).
\end{aligned}
\tag{4.4}
```

把 `(4.1)` 与 `(4.4)` 相加：

```math
\begin{aligned}
\frac{\log(Uv_2)}S-(1+U_*)
\ge{}&-
rac\delta2+
rac{2b}{3}\mu
-2aG_2-
rac{2b}{3}Q_5\\
&-\frac{5b}{3}G_5-\frac b3N_5-
rac{5R}{2}-o(1).
\end{aligned}
\tag{4.5}
```

`G_2` 的未粗化 upper 为

```math
aG_2
\le
\frac\delta2+aQ_2+\frac b3G_5+\frac R2+o(1).
\tag{4.6}
```

故

```math
\begin{aligned}
\frac{\log(Uv_2)}S-(1+U_*)
\ge{}&-
rac{3\delta}{2}+
rac{2b}{3}\mu\\
&-2aQ_2-
rac{2b}{3}Q_5
-\frac{7b}{3}G_5-\frac b3N_5-
rac{7R}{2}-o(1).
\end{aligned}
\tag{4.7}
```

---

<a id="dd-b02-detail-src-0123-31-5"></a>
#### 用 exact `mu` budget 回收正项

corrected Schmidt slack identity给

```math
\boxed{
A\mu
=\sigma_S+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)+2R+o(1).}
\tag{mu-budget}
```

令

```math
\boxed{
c_\mu:=\frac{2b}{3A}=\frac{b}{1+2a}.}
\tag{5.1}
```

把 `(mu-budget)` 代入 `(4.7)`。忽略有利的 `sigma_S,N_2` 正贡献后，剩余 loss coefficients 为

```math
\begin{array}{c|c}
\text{variable}&\text{loss coefficient}\\ \hline
Q_2&2a(1-c_\mu)\\
Q_5&\frac{2b}{3}(1-c_\mu)\\
G_5&\frac b3(7-4c_\mu)\\
N_5&\frac b3(1-c_\mu)\\
R&\frac72-2c_\mu.
\end{array}
\tag{5.2}
```

quantitative-defect costs分别为

```math
2a\lambda,
\qquad
\frac{2b(\lambda+1)}3,
\qquad
\frac{2b(2\lambda-1)}3,
\qquad
\frac{b(\lambda+1)}3,
\qquad
2\lambda-1.
\tag{5.3}
```

逐项 loss/cost ratios化简为

```math
\begin{array}{c|c}
Q_2&0.392472061943\ldots\\
Q_5&0.231378213160\ldots\\
G_5&\frac12+3a\\
N_5&0.231378213160\ldots\\
R&\frac12+3a.
\end{array}
\tag{5.4}
```

最大 ratio由 `G_5` 与 `R` 同时达到：

```math
\boxed{
\rho_{UV}=\frac12+3a
=1.403089986991944\ldots.}
\tag{5.5}
```

所有 variables 共用同一份 slope-defect budget，所以 `(4.7)` 最终给

```math
\boxed{
\frac{\log_{10}(Uv_2)}S
\ge
1+U_*-C_{UV}\delta-o(1),}
\tag{UV-height}
```

其中

```math
\boxed{
C_{UV}
=\frac32+\rho_{UV}
=2+3a
=2.903089986991944\ldots
=\log_{10}800.}
\tag{5.6}
```

这严格优于把 individual `U` 与 `v_2` lower bounds直接相加所得的 coefficient `3.636079988...`。

---

<a id="dd-b02-detail-src-0123-31-6"></a>
#### 显式 `U × v_2` uniqueness neighborhood

`d_3`-dominant surplus simplex给

```math
n_1+n_2=S+s_1+s_2\le S+2.
```

因此

```math
0<A_{12}<10^{S+2}.
\tag{6.1}
```

由 `(UV-height)`，若

```math
1+U_*-C_{UV}\delta>1,
```

即

```math
\boxed{
\delta<\delta_{UV}:=\frac{U_*}{2+3a},}
\tag{6.2}
```

则 sufficiently large `S` 时

```math
Uv_2>10^{S+2}.
```

数值上

```math
\boxed{
\delta_{UV}
=0.238062349248111\ldots.}
\tag{6.3}
```

固定 denominator/S-unit data 与 `(R_0,g_0,a_2)` 后，`A_12` 同时落在一个 residue modulo `U` 与一个 residue modulo `v_2`；由于二者互素，若有两个不同合法 candidates，其差被 `Uv_2` 整除，却绝对值小于 `Uv_2`，矛盾。

因此

```math
\boxed{
\delta<0.238062349248111\ldots
\Longrightarrow
\#\{A_{12}\text{ in fixed }(R_0,g_0,a_2)\text{ fiber}\}\le1.}
\tag{UV-fixed-fiber-unique}
```

carry `(Carry-primitive)` 再唯一恢复 `a_3`；固定 `(n_2,a_2)` 后也唯一恢复 `a_1`。

---


<a id="dd-b02-detail-src-0132-62-1"></a>
#### 已有的 oriented gap congruence

沿用 canonical notation
```math
F:=5^T,
\qquad
q_{\rm lcm}=\operatorname{lcm}(b_1,b_2,b_3),
```
```math
c_2:=q_{\rm lcm}/b_2,
\qquad
c_3:=q_{\rm lcm}/b_3.
```

quantitative large pair-max channel写
```math
V=v_1v_2,
```
并对每个
```math
p^h\Vert v_2
```
有 denominator pattern
```math
v_p(b_1)=r,
\qquad
v_p(b_2)=v_p(b_3)=r+h.
```
因此
```math
\boxed{p\nmid c_2c_3.}
\tag{1.1}

`dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md` 还证明在这些 target primes 上
```
```math
\boxed{p\nmid g_0R_0 10.}
\tag{1.2}

pair-max Gaussian orientation可选择 Hensel root
```
```math
\iota_p^2\equiv-1\pmod{p^h}.
```
前一 short-suffix theorem 已严格得到
```math
\boxed{
 g_0a_2c_2
 \equiv
 2F\iota_pc_3R_0
 \pmod{p^h}.}
\tag{Gap-p-local}

```
注意 `(1.1)--(1.2)` 说明右侧 coefficient
```math
2F\iota_pc_3
```
是 `p`-unit。

---

<a id="dd-b02-detail-src-0132-62-2"></a>
#### 聚合成一个 modulo `v_2` 的 rational line

固定一个完整 Gaussian orientation vector
```math
\Omega=(\iota_p)_{p^h\Vert v_2}.
```
不同 prime powers互素，所以 Chinese remainder theorem给唯一 residue
```math
\boxed{
\iota_\Omega\pmod{v_2}
}
```
满足
```math
\iota_\Omega\equiv\iota_p\pmod{p^h}
```
对所有 `p^h||v_2` 成立。

定义
```math
\boxed{
K_\Omega:=2F\iota_\Omega c_3,
\qquad
A_2:=a_2c_2.
}
\tag{2.1}

```
由 `(1.1)`：
```math
\boxed{(K_\Omega,v_2)=1.}
\tag{2.2}

```
逐 prime-power 聚合 `(Gap-p-local)`：
```math
\boxed{
K_\Omega R_0
\equiv
A_2g_0
\pmod{v_2}.}
\tag{Gap-v2-line}

```
所以固定 denominator/S-unit data、orientation `Omega` 与 short suffix `a_2` 后，所有合法 primitive gap fractions
```math
R_0/g_0,
\qquad(R_0,g_0)=1,
```
都落在同一个 projective residue class modulo `v_2`。

---

<a id="dd-b02-detail-src-0132-62-3"></a>
#### 两个 gap fractions 强迫一个 `v_2`-deep Farey determinant

假设同一 fixed denominator/S-unit/orientation/`a_2` fiber 中存在两个合法 gap pairs
```math
(R_0,g_0),
\qquad
(R_0',g_0').
```

由 `(Gap-v2-line)`：
```math
K_\Omega R_0\equiv A_2g_0\pmod{v_2},
```
```math
K_\Omega R_0'\equiv A_2g_0'\pmod{v_2}.
```
第一式乘 `g_0'`，第二式乘 `g_0`，相减：
```math
K_\Omega(R_0g_0'-R_0'g_0)
\equiv0\pmod{v_2}.
```
由 `(2.2)` 可约去 `K_Omega`：
```math
\boxed{
 v_2\mid
 \Delta_{\rm gap}
 :=R_0g_0'-R_0'g_0.}
\tag{Gap-Farey-divisor}

```
若两个 reduced fractions不同，则
```math
\boxed{\Delta_{\rm gap}\ne0.}
\tag{3.1}
```
因为 `(R_0,g_0)=(R_0',g_0')=1` 且所有量为正整数；相同 rational number的最低项表示唯一。

这一步把 pair-max Gaussian orientation转成了一个 ordinary integer Farey determinant divisor。

---

<a id="dd-b02-detail-src-0132-62-4"></a>
#### determinant 的高度只有一份 `delta S`

`dd-corrected-neighborhood-gap-fiber-entropy-2026-08-22.md` 定义
```math
P_{\rm gap}
:=\frac1S\log_{10}\operatorname{core}_{10}(H_{\rm sph}-y_3),
```
以及 rough overlap height
```math
R:=\frac1S\log_{10}\gamma_0.
```
并证明每个 gap fiber满足
```math
\boxed{
\log_{10}R_0
\le P_{\rm gap}S+o(S),
}
\tag{4.1}
```
```math
\boxed{
\log_{10}g_0
\le RS+o(S),
}
\tag{4.2}
```
以及共同 defect budget
```math
\boxed{
P_{\rm gap}+R\le\delta+o(1).
}
\tag{4.3}

```
这里 fixed denominator/S-unit data下 `R` 固定。即使两个 numerator candidates对应不同的 `P_gap`，由 `(4.3)` 仍统一有
```math
P_{\rm gap},P_{\rm gap}'
\le\delta-R+o(1).
```

因此两个 cross products分别满足
```math
\begin{aligned}
\log_{10}(R_0g_0')
&\le(P_{\rm gap}+R)S+o(S)\\
&\le\delta S+o(S),
\end{aligned}
```
以及同样的
```math
\log_{10}(R_0'g_0)
\le\delta S+o(S).
```

所以
```math
\boxed{
0<|\Delta_{\rm gap}|
\le10^{\delta S+o(S)}
}
\tag{Gap-Farey-height}
```
对任何两个不同 gap fractions成立。

这里至关重要的是：cross determinant只花 **一份** `P_gap+R` budget；不能把两个 candidates的 `R_0g_0` product bounds机械平方成 `2delta S`。

---

<a id="dd-b02-detail-src-0132-62-5"></a>
#### `v_2` 比 Farey determinant 更大时 gap fiber唯一

quantitative one-channel theorem给
```math
\boxed{
\frac{\log_{10}v_2}{S}
\ge
1-C_{\rm one}\delta-o(1),
}
\tag{5.1}
```
其中
```math
\boxed{
C_{\rm one}
=1+\frac{5(1+2a)}6
=2.335049992773302\ldots,
\qquad a:=\log_{10}2.
}
\tag{5.2}

```
若
```math
1-C_{\rm one}\delta>\delta,
```
则 `(5.1)` 与 `Gap-Farey-height` 给 sufficiently large `S`：
```math
v_2>|\Delta_{\rm gap}|.
```
但 `Gap-Farey-divisor` 又要求非零 `Delta_gap` 被 `v_2` 整除，矛盾。

所以此时同一个 fixed denominator/S-unit/orientation/`a_2` fiber 中 gap fraction至多一个。

解阈值：
```math
\boxed{
\delta
<\delta_{\rm gap}
:=\frac1{1+C_{\rm one}}.
}
\tag{5.3}
```
使用 `(5.2)`：
```math
1+C_{\rm one}
=2+\frac{5(1+2a)}6
=\frac{17+10a}{6},
```
故
```math
\boxed{
\delta_{\rm gap}
=\frac6{17+10\log_{10}2}
=0.299845580176277\ldots.}
\tag{Gap-threshold}

```
于是：
```math
\boxed{
\delta<\delta_{\rm gap}
\Longrightarrow
\#\{(R_0,g_0)\mid
\text{fixed denominator/S-unit data, }\Omega,a_2\}
\le1.
}
\tag{Gap-fiber-unique}

```
---


来源：`SRC-0190:525–799`；`SRC-0133:31–454`；`SRC-0126:27–395`；`SRC-0123:31–453`；`SRC-0132:62–340`。原文保全，当前论证以本节为准。

<a id="dd-02"></a>
### DD-02　全奇分母的实际 norm residue 排除

**状态：已严格完成。** n3>m3；m3=2、m3≥3 与 m3=1 分别列出 exact residues。

依赖：[DD-01](#dd-01)、[C05](#c05)

核对：正文推导；本次重写未为此项另增枚举。

<a id="dd-02-detail-src-0122-2716-1"></a>
#### 原始 full-word norm 关闭全奇分母的模四剩余类

**状态：已严格完成（无界剩余类排除）。** 以下不是有限搜索，也不要求
canonical `t_2=1` neighborhood。只假设三个原分母 `b_1,b_2,b_3` 全奇，
原第三块位数 `n=n_3>m=m_3>=2`；`m_2,n_2>=1` 保持原十进制权重。
它关闭本节全奇锥的一部分，不关闭整个 DD，也不处理 `b_3` 为偶数的
canonical terminal。

依赖 [global-framework.md §10.2](#c06)
的 exact denominator norm，写

```math
Q=b_1 10^{m_2}+b_2,\qquad
t_1=b_1 10^{n_2+n},\qquad t_2=b_2 10^n,
```

则 `Q` 为奇数，且

```math
\Delta_{\rm dec}
=t_1^2+t_2^2-10^mQ(10^mQ+2b_3).
\tag{Odd-decimal-norm-expansion}
```

由于 `m>=2` 与 `b_3,Q` 为奇数，

```math
v_2\bigl(10^mQ(10^mQ+2b_3)\bigr)=m+1,
\qquad v_2(t_2^2)=2n\ge2m+2>m+1.
```

`t_1^2` 的二进赋值还更大。因此没有最低层 cancellation，严格得到

```math
\boxed{v_2(\Delta_{\rm dec})=m+1.}
\tag{Odd-decimal-norm-two-depth}
```

特别地 `Delta_dec!=0`。除以该二进 content，得到

```math
\frac{\Delta_{\rm dec}}{2^{m+1}}
\equiv-5^mQ\bigl(b_3+2^{m-1}5^mQ\bigr)\pmod4.
\tag{Odd-decimal-norm-unit}
```

这里两个 positive-square 项除以 `2^(m+1)` 都被四整除，因为
`2n-(m+1)>=m+1>=3`。于是

```math
\boxed{
\frac{\Delta_{\rm dec}}{2^{m+1}}
\equiv
\begin{cases}
-Qb_3-2& m=2,\\
-Qb_3& m\ge3
\end{cases}\pmod4.}
\tag{Odd-decimal-norm-unit-mod4}
```

一个非零有理 Gaussian norm 的二进 odd unit 必为 `1 mod4`：清分母后
先约去两个整数的共同二进 content；若二者奇偶不同，二平方和为
`1 mod4`，若二者均奇则其和为 `2 mod8`，除以二后也是 `1 mod4`。
清除有理分母只增加偶数二进赋值和 `1 mod4` 的 odd square。
因此 `(Odd-decimal-norm-unit-mod4)` 给出

```math
\boxed{
\begin{array}{ll}
m=2,&Qb_3\equiv3\pmod4\ \Longrightarrow\ \varnothing,\\
m\ge3,&Qb_3\equiv1\pmod4\ \Longrightarrow\ \varnothing.
\end{array}}
\tag{Odd-decimal-norm-mod4-exclusion}
```

该排除对所有分子、所有前缀尺度和任意 `n>m` 成立，没有绝对长度上界。
剩余 `m=2,Qb_3=1 mod4` 或 `m>=3,Qb_3=3 mod4` 只满足此局部必要条件，
不是存在性结论。`m=1` 的最低层可能与 `t_2^2` 接触，需使用下面的
独立 depth 分层，不能套用 `(Odd-decimal-norm-two-depth)`。
这条条件来自原 full-word/sphere 的 norm 投影，不增加另一份 sphere
或 Schmidt 高度预算。

**一位第三分母的 exact 分层。** 仍设三个分母全奇，现令 `m=1,n>1`。
写

```math
w=v_2(5Q+b_3)\ge1,\qquad c=\frac{5Q+b_3}{2^w}\quad\text{odd}.
```

则原 norm展开为

```math
\Delta_{\rm dec}=t_1^2+t_2^2-20Q(5Q+b_3),
\qquad v_2(t_2^2)=2n,\quad
v_2\bigl(20Q(5Q+b_3)\bigr)=w+2.
```

当两个最低 depths不相等时，exact norm二进 odd unit为

```math
\boxed{
\begin{array}{c|c|c}
\text{depth state}&v_2(\Delta_{\rm dec})
&\Delta_{\rm dec}/2^{v_2(\Delta_{\rm dec})}\pmod4\\ \hline
w\le2n-4&w+2&-Qc\\
w=2n-3&2n-1&2-Qc\\
w=2n-1&2n&3\\
w\ge2n&2n&1
\end{array}}
\tag{Odd-one-digit-decimal-norm-depth-states}
```

因为 `t_1^2/t_2^2` 额外具有 `2n_2>=2` 的二进 depth；在第二行
`t_2^2/2^(2n-1)=2b_2^2=2 mod4`，在第三行 negative term除以
`2^(2n)` 为 `2*5Qc=2 mod4`，其余行由最低 depth直接读取。
Gaussian norm unit必须为 `1 mod4`，因此又得到三个**无界子域排除**：

```math
\boxed{
\begin{array}{ll}
w\le2n-4,&Qc\equiv1\pmod4\ \Longrightarrow\ \varnothing,\\
w=2n-3,&Qc\equiv3\pmod4\ \Longrightarrow\ \varnothing,\\
w=2n-1,&\Longrightarrow\ \varnothing.
\end{array}}
\tag{Odd-one-digit-decimal-norm-exclusions}
```

深度相等的 `w=2n-2` 会在 `t_2^2` 与 negative term之间发生 cancellation，
此表没有覆盖；`w>=2n` 与前两行的允许 residue也没有被该二进 unit
条件排除。这不是所有一位尾分母的全局空性。

机械核对使用

证书命令与覆盖见 [统一核对目录](CHECKS.md)。

脚本核对 symbolic norm identity 与明确 bounded odd-denominator / digit
samples 的 exact two-depth、odd-unit residue与一位尾分母的非 tie depth
states；无界排除由上述赋值推导承担。


来源：`SRC-0122:2716–2858`。原文保全，当前论证以本节为准。

<a id="dd-03"></a>
### DD-03　一位偶尾的 third-two-dominant 闭合

**状态：有限证书。** 第三分母独占二进最高层，b3∈{2,4,6,8}，n3≥2；长前缀余 (17,6,8) 后有限。

依赖：[DD-01](#dd-01)、[C05](#c05)、[C09](#c09)

核对：`dd-third-two`

<a id="dd-03-detail-src-0122-3103-1"></a>
#### 一位偶第三分母的 third-two-dominant DD state 完整关闭

**状态：已严格完成（无界 denominator 归约 + 已有证书 + 额外有限证书）。**
设原 reduced blocks满足

```math
\boxed{b_3\in\{2,4,6,8\},\quad n_3>m_3=1,\quad
e_3:=v_2(b_3)>\max(e_1,e_2),\quad e_i=v_2(b_i).}
\tag{Single-digit-tail-third-two-dominant-domain}
```

前两分母和全部分子位数最初无界；本节关闭整个该 state。依赖仅为原
integer sphere / word 与 §27.7.3 的一位三分母证书，不使用上层高度或
canonical 假设。`n_3=1` 不在本节的结论内；prefix-two-dominant 的
一般一位偶尾状态也不在结论内。

**公开 denominator depth 条件。** 一般 sphere 中设正二进最高分母
depth `E` 唯一。当 `E>=2` 时，另外两分母中恰在 depth `E-1` 的
数量必须为偶数。最高坐标为 odd ghost，depth `E-1` 的分母仍为偶数，
故其既约分子必奇，ghost square为 `4 mod8`；其余坐标 square为
`0 mod8`。若恰有一项位于 `E-1`，sphere右边为 `1+4=5 mod8`，
不可能是 odd integer square。

```math
\boxed{E\ge2,\ E\text{ unique}\Longrightarrow
\#\{i:v_2(b_i)=E-1\}\in\{0,2\}.}
\tag{Sphere-second-two-depth-even-count}
```

这个必要条件对三分支统一成立。`E=1` 时非最高分母为奇数，其分子
parity自由，不能只数分母套用此式；它不是新 independent height预算。

**第一步：用 word 只保留 `b_3=8,b_2=2/6,b_1` 奇。** 本节第三分母
独占二进最大，既约性使 `a_3` 和原 numerator word奇。Sphere和原 word
分别给 `v_2(R)=-e_3` 与 `v_2(R)=-v_2(D)`，因此

```math
D=10Q+b_3,\quad Q=b_1 10^{m_2}+b_2,\qquad v_2(D)=e_3.
```

若 `b_3=2,6`，两个前缀分母均奇，`Q` 奇，故 `v_2(D)>=2`，与
`e_3=1` 矛盾。若 `b_3=4,8`，`v_2(D)=e_3` 要求
`v_2(10Q)>e_3`，因为小于或等于分别给过低或过高的 word depth。
于是 `v_2(Q)>=e_3`。又 `e_1,e_2<e_3`，这只可能在两个 prefix
summands的二进 depths相等时发生：

```math
e_2=m_2+e_1.
```

对于 `b_3=4`，只能 `e_2=1,m_2=1,e_1=0`，即 `b_2=2,6`；depth
pattern为 `(0,1,2)`，违反上式的 even-count 条件。对于 `b_3=8`，
`e_2=2` 同样给唯一的 `E-1=2` 坐标而被排除，只剩

```math
\boxed{b_3=8,\quad b_2\in\{2,6\},\quad m_2=1,
\quad b_1\text{ 奇},\quad8\mid Q.}
\tag{Single-digit-even-tail-third-two-survivor}
```

**第二步：将仍无界的 `b_1` 压成四个值。** 若 `b_2=2`，`b_1`
与 `b_2b_3=16` 互素。每个 `p^e||b_1` 均在第一分数上独占最高
denominator depth，sphere给 `v_p(R)=-e`，故 word要求 `v_p(D)>=e`。
逐素数合并得 `b_1|D=100b_1+28`，所以 `b_1|28`。因 `b_1` 奇，只剩
`b_1=1,7`。

若 `b_2=6`，先排除 `3|b_1`：第三分母为三进 unit，前两最高三进
depth只能由一个或两个坐标取得；`3` inert使两个 leading unit squares
不能抵消。因此 sphere要求 `v_3(R)<0`，而
`D=100b_1+68` 在 `3|b_1` 时为三进 unit，word要求 `v_3(R)>=0`，
矛盾。于是 `(b_1,48)=1`，再次逐素数 unique maximum得到
`b_1|D=100b_1+68`，故 `b_1|68`。奇数可能值只有 `1,17`。

三个 denominator triples `(1,2,8),(7,2,8),(1,6,8)` 均由 §27.7.3
的完整一位三分母证书关闭。只剩

```math
\boxed{(b_1,b_2,b_3)=(17,6,8),\quad Q=176,\quad
D=1768=8\cdot221,\quad q_{\rm lcm}=408.}
\tag{Third-two-tail-only-long-prefix-triple}
```

**第三步：排除该 triple 的 `n_3>=3`。** Ghosts为
`(24a_1,68a_2,51a_3)`；因 `a_2,a_3` 奇，有
`H^2-(51a_3)^2=0 mod16`。原 word给 `221H=51mathscr A`，当
`n_3>=3` 时 `mathscr A=a_3 mod8`，故 `H=5(51a_3) mod8`。两个 odd
integers满足此关系时，其平方之差为 `8 mod16`，矛盾。因此只剩
`n_3=2`。

**第四步：完整高度归约与 extra certificate。** 记 `X=10^{n_2}>=10`，
`10<=a_3<=99`。实际 rational triangle 与 word lower给

```math
\frac{100Xa_1}{1768}<R<\frac{a_1}{17}+\frac X6+\frac{99}8,
```

```math
a_1<\frac{X/6+99/8}{100X/1768-1/17}
\le\frac{74477}{2688}<28.
```

这里分母对 `X>=10` 为正，ratio随 `X` 递减，故 `a_1<=27` 对所有
`n_2` 统一成立。整数 sphere 的 `H-y_2>=1` 再给

```math
a_2<\frac{6\cdot408}{2}
\left((a_1/17)^2+(a_3/8)^2\right)
\le1224\left((27/17)^2+(99/8)^2\right)
=\frac{25912305}{136}<10^6.
```

因此 `1<=n_2<=6`。在这个全局归约后，固定
`a_1∈[1,27],(a_1,17)=1`、两位 odd `a_3` 与 `n_2∈[1,6]`，从
§27.7.3 的 exact quadratic reader恢复所有 `a_2`。共 `7020` 行，两个
独立 reader均给零个 positive reduced / correct-length 解。该 extra
certificate与前三个一位 triple 的已有证书合并，完整关闭本节无界
state。

证书命令与覆盖见 [统一核对目录](CHECKS.md)。

第二条只核对本节 extension，前三个一位 triple 使用第一条的 §27.7.3
证书。本结果没有排除 prefix-two-dominant state、奇数一位尾分母的
general-prefix state，也没有关闭 DD 全局分支。


来源：`SRC-0122:3103–3231`。原文保全，当前论证以本节为准。

<a id="dd-04"></a>
### DD-04　第二分母两位、尾分母 8 或 4 的完整 DD 子层

**状态：有限证书。** m2=2,b3=8/4,n3≥2,n2+n3>3；两 reader 全参数归约和严格尺度转移。

依赖：[DD-01](#dd-01)、[C04](#c04)、[C05](#c05)

核对：`dd-eight-tail`、`dd-eight-tail-factored`、`dd-four-tail`

<a id="dd-04-detail-src-0122-3438-1"></a>
#### 第二分母两位、第三分母为八的完整 DD 子层

**状态：已严格完成（全部 denominator / numerator 高度归约后给精确有限证书）。**
本节完整关闭

```math
\boxed{b_1\ge1,\quad10\le b_2\le99,\quad b_3=8,\quad
 n_3\ge2,\quad n_2+n_3>3.}
\tag{Two-digit-second-eight-tail-DD-domain}
```

全部分子与第一分母最初无界。最后两个位数条件分别是 `d_3>0` 和
`k_12=n_2+n_3-3>0`；特别是 `n_2=1,n_3=2` 不在本子层内。本结论
不覆盖一般两位第二分母的一位尾族，也不覆盖该 suffix 的全部跨分支域。

**完整 denominator 归约。** 本节 `Q=100b_1+b_2`、
`D=1000b_1+10b_2+8`。前节的公开 first-denominator bound 仍给
`b_1|lcm(b_2,8,10b_2+8)`。全部九十个 `b_2` 的 positive divisors
共 `3369` 个 triples，最大 `b_1=395208`。前节 filters 1--5 都来自
原 word / sphere，均不要求 `m_2=1`；把 `Q,D` 换成上述实际值后，
完整必要条件 projection 恰好留下

```text
(288,28,8) (448,44,8) (160,60,8) (3040,60,8) (3,64,8).
```

这里没有用 unique-five-tail filter，也没有只取 first-two-dominant
或 third-two-dominant 的某一个状态。全部五组仍须恢复原完整分子。

**全部 numerator 高度归约。** 写 `X=10^(n_2),Y=10^(n_3)`、
`q=lcm(b_i)`、`y_i=qa_i/b_i`。继续仅使用

```math
q\mathscr A=DH,\qquad H^2=y_1^2+y_2^2+y_3^2,\qquad
\mathscr A=a_1XY+a_2Y+a_3.
\tag{Two-digit-second-eight-original-parents}
```

取 `N=min{j>=3:10^j b_2>D}`、`Y_0=10^N`。高尾 `n_3>=N` 时，
严格 triangle 的 `a_2(Y-D/b_2)` 项为正，因此同前节有

```math
a_1\left(X-\frac D{b_1Y}\right)<\frac D8.
```

因 `D/b_1<=1998`、`Y>=1000`，括号严格正。于是
`X<D/8+D/(b_1Y_0)` 给全部 `n_2` 上界 `J_h`，
`A_h=ceil((D/8)/(10-D/(b_1Y_0)))-1` 给全部 `a_1` 上界。
由 `H-y_3>=1`、`H+y_3>2y_3` 得

```math
a_3<\frac{8q}{2}\left[(A_h/b_1)^2+
 ((10^{J_h}-1)/b_2)^2\right]=B_h.
```

`ceil(B_h)-1` 的 digit length 给全部 `n_3` 上界 `K_h`。

每个短尾 `2<=n_3<N` 取 `n_{2,\min}=max(1,4-n_3)` 和
`X_0=10^(n_{2,\min})`。DD 条件恰好给 `XY>=10000`，故
`XY/D-1/b_1>0`。原 word lower 与 triangle 给

```math
a_1<B_1(X,Y):=
\frac{X/b_2+(Y-1)/8}{XY/D-1/b_1}.
```

其导数 numerator 为 `-1/(b_1b_2)-Y(Y-1)/(8D)<0`，所以
`A_Y=ceil(B_1(X_0,Y))-1` 对全部允许 `n_2` 有效。
由 `H-y_2>=1` 得

```math
a_2<\frac{qb_2}{2}\left[(A_Y/b_1)^2+((Y-1)/8)^2\right]=B_Y.
```

`ceil(B_Y)-1` 的 digit length 给全部 `n_2` 上界 `J_Y`。
这两个盒覆盖全部原始 heights；实际枚举再使用每个 `X,Y` 的严格
`a_1` bound，不引入任意 cutoff。高盒记 `(J_h,K_h,A_h)`，短盒
记 `n_3:(n_{2,\min},J_Y,A_Y)`：

| denominator triple | `N` | 高盒 | 短盒 | 无长度预筛 rows | norm 长度筛后 rows |
|---|---:|---|---|---:|---:|
| `(288,28,8)` | 5 | `(4,10,3607)` | `2:(2,7,510); 3:(1,9,4011); 4:(1,11,3640)` | 6894971 | 6861185 |
| `(448,44,8)` | 5 | `(4,10,5611)` | `2:(2,8,729); 3:(1,10,6234); 4:(1,12,5662)` | 13797640 | 13757455 |
| `(160,60,8)` | 4 | `(4,8,2027)` | `2:(2,7,250); 3:(1,9,2232)` | 492398 | 444548 |
| `(3040,60,8)` | 5 | `(5,12,38045)` | `2:(2,8,4744); 3:(1,10,42245); 4:(1,12,38392)` | 82361789 | 10196669 |
| `(3,64,8)` | 3 | `(2,6,51)` | `2:(2,6,5)` | 1390 | 1105 |

**可选 exact norm 长度筛选。** 对每个完整盒内的实际 `(n_2,n_3)`，
[原 denominator-word norm](#c06) 必要条件读

```math
\Delta_{\rm dec}=b_1^2X^2Y^2+b_2^2Y^2+64-D^2.
```

程序只排除 `Delta<0`，或正 `Delta` 的二进 odd unit 非 `1 mod4`，
或 `p=3,7,11,19,23,31,43` 中任一个 valuation 为奇数；这些都是非零
rational Gaussian norm 的必要条件。`Delta=0` 保留；不以有限 prime
列表的全部通过作为充分条件。全部 `220` 个长度组合中保留 `187` 个，
其余 `33` 个由上述必要条件关闭。没有把盒外的无界长度交给此筛选。

**原方程精确证书。** 高盒枚举 `a_1,a_2` 恢复 `a_3`，短盒枚举
`a_1,a_3` 恢复 `a_2`。两种 quadratic reader 都由
`(Two-digit-second-eight-original-parents)` 符号消元，穷尽正整数根并
检查实际 digit interval、三处 reducedness 与原方程；leading
coefficient 不为零的理由同前节（`D>8`，且 `D` 末位为八）。

证书命令与覆盖见 [统一核对目录](CHECKS.md)。

标准与 factored 两种 reader **取消全部 norm 长度预筛**后，各核对
`103,548,188` 行（分别约 `68.6s/65.4s`），逐状态计数相同、零个原解。
两 reader 还各核对 norm 长度筛后的 `31,260,962` 行，仍为零个原解。
因此本节的空性不依赖可选长度筛选；它来自完整高度归约与全部有界盒
的原方程 exact reconstruction。这完成指定无界 DD 子层；不把该子域
结果提升为整个 DD 分支的空性。

**同专题推论（状态：已严格完成；不增加 numerator 枚举）。** 还可完整关闭

```math
\boxed{b_1\ge1,\quad10\le b_2\le99,\quad b_3=4,\quad
 n_3\ge2,\quad n_2+n_3>3.}
\tag{Two-digit-second-four-tail-DD-domain}
```

公开 first-denominator bound 与同样的 filters 1--5 完整遍历 `2818`
个 divisor triples（最大 `b_1=196812`），只余
`(144,14,4),(224,22,4),(80,30,4),(1520,30,4)`。四组的三个分母
全部偶数。将三个分母同时乘二，分别成为上述八尾证书的前四个 states。
第二分母仍两位、第三分母仍一位，故原 numerator word `mathscr A`
不变；第一分母位数的改变不进入后两 denominator blocks 的权重。
直接从原 parents 核对

```math
\beta'=2\beta,\quad q'=2q,\quad
y_i'=q'a_i/b_i'=y_i,\quad H'=H,
\qquad q'\mathscr A-\beta'H'=2(q\mathscr A-\beta H).
```

sphere 完全不变，word 等式两侧同乘二。因原三个分母已偶，乘二
不添任何 prime support，三处既约性也完全保持；numerator lengths、
`d_3` 与 `k_12` 都不变。因此四尾域的任何原解会给出已关闭八尾域的
原解，矛盾。这是完整 projection 后的严格尺度转移，不是未经审计的
Gaussian flip，也不需要重复一份分子 certificate。

证书命令与覆盖见 [统一核对目录](CHECKS.md)。

该入口重新生成四尾全部 divisor projection，并逐组核对 digit lengths、
prime supports、`q'=2q,beta'=2beta,y_i'=y_i`，输出 `PASS`。推论仍
只覆盖 `k_12>0,d_3>0` 的 DD 子层。


来源：`SRC-0122:3438–3595`。原文保全，当前论证以本节为准。

<a id="dd-05"></a>
### DD-05　gcd-normal 的两个真实 gap readers

**状态：已严格完成。** 整个 DD gcd-normal tail；odd source 模数的 coefficient stripping 另注明范围。

依赖：[DD-01](#dd-01)、[DD-B02](#dd-b02)

核对：`dd-gap-crt`

<a id="dd-05-detail-src-0174-32-1"></a>
#### gcd-normal exact data

写

```math
\kappa=\gamma u,
\qquad
G=\gamma v,
\qquad
(u,v)=1,
```

并令

```math
d_0=(u,Q),
\qquad
u=d_0L,
\qquad
Q=d_0q,
\qquad
(L,q)=1.
\tag{1.1}
```

这里使用 `gcd-normal-exact-small-factor` 已证明的 exact identification：其旧记号 `r` 就是 DD tail normalization 的 `L`。同时

```math
\boxed{\tau=vq,}
\tag{1.2}
```

```math
\boxed{(d_0,v)=1,\qquad(L,v)=1.}
\tag{1.3}
```

令

```math
\omega:=(10^m,b_3)=10^m/L,
```

以及

```math
c_3:=q_{\rm lcm}/b_3.
```

由 tail recovery

```math
b_3=v\omega q,
```

故

```math
\boxed{q_{\rm lcm}=v\omega q c_3.}
\tag{1.4}
```

注意 `omega` 是 `{2,5}`-smooth，但一般**不是**纯 `10` 次幂。后续 decimal phase shifting只能抽取其中的完整 `10`-power `10^{v_{10}(omega)}`；剩余 one-sided `2`/`5` factor必须保留在 coefficient 中。

---

<a id="dd-05-detail-src-0174-32-2"></a>
#### source-gap exact identity直接给 `v | H_sph`

DD gap exact identity为

```math
\boxed{
\mathcal M=q_{\rm lcm}A_{12}10^d
=QH_{\rm sph}+\tau a.
}
\tag{2.1}
```

代入 `(1.1)--(1.4)`：

```math
v\omega q c_3A_{12}10^d
=d_0qH_{\rm sph}+vqa.
```

约去正整数 `q`：

```math
\boxed{
v\omega c_3A_{12}10^d
=d_0H_{\rm sph}+va.
}
\tag{2.2}
```

右边说明

```math
v\mid d_0H_{\rm sph}.
```

由 `(d_0,v)=1`：

```math
\boxed{v\mid H_{\rm sph}.}
\tag{v-H}
```

定义

```math
\boxed{H_{\rm sph}=vH_0,\qquad H_0\in\mathbf Z_{>0}.}
\tag{2.3}
```

把 `(2.3)` 代回 `(2.2)` 并约去 `v`：

```math
\boxed{
\omega c_3A_{12}10^d
=a+d_0H_0.
}
\tag{D0-parent}
```

因此得到第一个 source residue：

```math
\boxed{
 a\equiv \omega c_3A_{12}10^d\pmod{d_0}.
}
\tag{D0-residue}
```

---

<a id="dd-05-detail-src-0174-32-3"></a>
#### sphere gap给互素 `v`-residue

因为

```math
y_3=a_3\frac{q_{\rm lcm}}{b_3}=a_3c_3,
```

而 DD gap normalization为

```math
H_{\rm sph}-y_3=La,
```

结合 `H_sph=vH_0`：

```math
\boxed{
vH_0=a_3c_3+La.}
\tag{V-parent}
```

模 `v`：

```math
\boxed{La\equiv-a_3c_3\pmod v.}
\tag{V-residue}
```

由 `(L,v)=1`：

```math
\boxed{
a\equiv-a_3c_3L^{-1}\pmod v.}
\tag{V-residue-unit}
```

又 `(d_0,v)=1`，所以 `(D0-residue)` 与 `(V-residue-unit)` 由 CRT 唯一确定一个

```math
\boxed{\rho_a\in[0,d_0v)}
\tag{3.1}
```

满足

```math
\boxed{a\equiv\rho_a\pmod{d_0v}.}
\tag{Gap-CRT}
```

这是两个**不同 coprime moduli** 对同一个 gap quotient 的 exact global reconstruction；本文不把它们当两份 p-adic height payer，只使用其 CRT location。

---

<a id="dd-05-detail-src-0174-32-4"></a>
#### small-gap / large-gap 二分

<a id="dd-05-detail-src-0174-32-5"></a>
#### small-gap branch

若

```math
\boxed{0<a<d_0v,}
\tag{4.1}
```

则 `(Gap-CRT)` 立即升级成 ordinary exact lift：

```math
\boxed{a=\rho_a.}
\tag{Gap-CRT-lock}
```

特别地，若 computed residue `rho_a=0`，则与 `a>0` 矛盾，该 fiber为空。

<a id="dd-05-detail-src-0174-32-6"></a>
#### large-gap branch

若

```math
\boxed{a\ge d_0v,}
\tag{4.2}
```

exact small-factor normalization为

```math
\boxed{
F_-=L(u+2v)\,a\frac{g_*}{v},
\qquad \frac{g_*}{v}\in\mathbf Z_{>0}.
}
\tag{4.3}
```

由 `u=d_0L`、`a>=d_0v`：

```math
F_-
\ge L(u+2v)d_0v
=uv(u+2v)
>u^2v.
\tag{4.4}
```

而 gcd-normal tail window给

```math
\boxed{Q<u/v\le10Q,}
\tag{4.5}
```

所以 `u>Qv`。代入 `(4.4)`：

```math
\boxed{F_->Q^2v^3.}
\tag{Large-gap-Fminus}
```

这严格强于 universal multiplicative lower

```math
F_->Qv^2.
```

---

<a id="dd-05-detail-src-0174-32-7"></a>
#### large-gap height consequence

由 decimal lengths

```math
Q\ge10^{S-1},
\qquad
G\ge10^{S-2},
```

且

```math
v=G/\gamma,
```

记

```math
\Gamma:=\frac{\log_{10}\gamma}{S}.
```

则 `(Large-gap-Fminus)` 给

```math
\boxed{
\frac{\log_{10}F_-}{S}
\ge5-3\Gamma-o(1).
}
\tag{5.1}
```

与 d-dominant Archimedean upper

```math
\log_{10}F_-<4S+2m-n+O(1)
```

联立：

```math
\boxed{
\frac nS
\le-1+2\frac mS+3\Gamma+o(1).
}
\tag{Large-gap-slope}
```

旧 universal multiplicative lower只给

```math
\frac nS\le1+2\frac mS+2\Gamma+o(1).
```

二者目标差为

```math
(-1+2M+3\Gamma)-(1+2M+2\Gamma)=\Gamma-2.
```

而 `gamma|G`，故 `Gamma<=1+o(1)`。所以在 large-gap branch，本文的新 slope inequality具有至少约一整份 normalized `S` 的严格余量。

---

<a id="dd-05-detail-src-0174-32-8"></a>
#### odd `d_0` source 的 coefficient-stripped modulus

现在回到 second-Schmidt odd non-decimal support。固定

```math
p\nmid10,
\qquad p\mid d_0.
```

沿用 `tail-rough-d0-allocation` 的 notation：

```math
E=v_p(b_1)=v_p(b_2),
\quad
j=v_p(b_3),
\quad
c=v_p(C_Q),
```

其中

```math
C_Q=Q/(b_1,b_2).
```

并令

```math
t=v_p(A_{12}).
```

旧 exact ledger给

```math
\boxed{v_p(d_0)=E+c-j,}
\tag{6.1}
```

以及

```math
\boxed{v_p(c_3)=(E-j)_+.}
\tag{6.2}
```

因为 `p` 为 non-decimal prime，`omega` 是 p-unit。故 `(D0-parent)` 左侧 coefficient

```math
\omega c_3A_{12}
```

在 p 处深度为

```math
\boxed{s_p=(E-j)_++t.}
\tag{6.3}
```

定义 stripping 后的 residual exponent

```math
\boxed{
r_p^{(d_0)}
:=\bigl(v_p(d_0)-s_p\bigr)_+.
}
\tag{6.4}
```

代入 `(6.1),(6.3)`：

```math
\boxed{
r_p^{(d_0)}
=\bigl(c-t-(j-E)_+\bigr)_+.
}
\tag{D0-local-depth}
```

若 `r_p^(d0)>0`，则 `s_p<v_p(d_0)`；由 `(D0-parent)` 的 unit `10^d` 可知两边要能相差 `p^{v_p(d0)}`，必有

```math
\boxed{v_p(a)=s_p.}
\tag{6.5}
```

所以除去 `p^{s_p}` 后确实留下一个 coefficient/right-side 都为 p-unit 的模 `p^{r_p^(d0)}` source residue。

同时

```math
r_p^{(d_0)}\le c,
```

故全局 modulus

```math
\boxed{
D_{d_0}:=\prod_{p\mid\operatorname{core}_{10}(d_0)}p^{r_p^{(d_0)}}
}
\tag{6.6}
```

满足

```math
\boxed{D_{d_0}\mid C_Q.}
\tag{6.7}
```

这点非常重要：虽然 reader源自更大的 `d_0`，stripping 后留下的有效 source modulus仍落回 primitive prefix modulus `C_Q`，所以可以继续合法使用 prefix block folding。

---

<a id="dd-05-detail-src-0174-32-9"></a>
#### 相比旧 `C_Q` Euclidean modulus精确恢复 `E` 层

旧 Euclidean coefficient stripping在同一 prime给

```math
\boxed{
r_p^{(E)}=(c-\max(E,j)-t)_+.}
\tag{7.1}
```

而

```math
\max(E,j)=E+(j-E)_+.
```

所以在取 positive part之前：

```math
\boxed{
 c-t-(j-E)_+
=
\bigl(c-\max(E,j)-t\bigr)+E.
}
\tag{7.2}
```

因此

```math
\boxed{r_p^{(d_0)}\ge r_p^{(E)}.}
\tag{7.3}
```

新 `d_0` reader恰好把旧 `C_Q` coefficient中被 `q_lcm` denominator maximum吞掉的 prefix-common depth `E` 恢复进 source modulus。

---

<a id="dd-05-detail-src-0174-32-10"></a>
#### corrected split 中 `D_{d_0}` 覆盖全部 `X_N X_H`

使用 `dd-corrected-hard-source-split` notation。

<a id="dd-05-detail-src-0174-32-11"></a>
#### hard support `h>0`

hard ledger为

```math
\boxed{c=h+2t+n_0+M+j,\qquad M=\max(E,j).}
\tag{8.1}
```

若 `E>=j`：

```math
r_p^{(d_0)}=c-t
=h+t+n_0+E+j
\ge h+n_0.
```

若 `j>E`：

```math
\begin{aligned}
r_p^{(d_0)}
&=c-t-(j-E)\\
&=h+t+n_0+j+E\\
&\ge h+n_0.
\end{aligned}
```

所以所有 hard source + hard prefix-norm exponent都进入 `D_d0`。

<a id="dd-05-detail-src-0174-32-12"></a>
#### soft prefix-norm support `e_N>0,h=0`

corrected split定义本身给

```math
e_B=t,
\qquad e_a=\alpha,
```

以及

```math
x=t+\alpha+e_N+e_3.
\tag{8.2}
```

若 `j>E`，由 source-excess identity

```math
c=x+j+E
```

得到

```math
\begin{aligned}
r_p^{(d_0)}
&=c-t-(j-E)\\
&=\alpha+e_N+e_3+2E\\
&\ge e_N.
\end{aligned}
```

若 `E>=j`，则 `e_3=0` 且

```math
c=x+2j,
```

故

```math
\begin{aligned}
r_p^{(d_0)}
&=c-t\\
&=\alpha+e_N+2j\\
&\ge e_N.
\end{aligned}
```

因此全局严格有

```math
\boxed{X_NX_H\mid D_{d_0}.}
\tag{D0-covers-NH}
```

这是相对旧 Euclidean modulus的主要结构升级：不再留下 `X_{N,D}|(b_1,b_2)` 的 denominator-common escape。

---

<a id="dd-05-detail-src-0174-32-13"></a>
#### decimal circular normalization 的正确边界

因为 `D_d0|C_Q`，在 `D_d0` 上 primitive prefix relation

```math
u_1 10^{m_2}\equiv-u_2
```

仍可用于 exponent folding，且 `u_1,u_2` 为 target units。

但必须注意：`omega` 只保证 `{2,5}`-smooth，不保证是纯 `10` 次幂。定义

```math
c_{10}^{(d_0)}:=v_{10}(\omega c_3A_{12}),
\qquad
s_{10}^{(d_0)}:=v_{10}(a),
```

其中

```math
v_{10}(N):=\min(v_2(N),v_5(N)).
```

只有这两份完整 decimal powers可向 exponent搬移；其余 one-sided smooth part保留在 unit coefficient中。

因此和前一 circular theorem完全相同的离散 interval argument给一个 normalized exponent

```math
\boxed{r_{d_0,\rm circ}\ge0}
```

满足

```math
\boxed{
r_{d_0,\rm circ}
\le
\max\left(
0,
\left\lfloor
\frac{m_2-c_{10}^{(d_0)}-s_{10}^{(d_0)}}2
\right\rfloor
\right)
\le\frac{m_2}{2}.
}
\tag{D0-circular-range}
```

并存在 target-unit coefficients `A_d,B_d` 使

```math
\boxed{
D_{d_0}\mid A_d10^{r_{d_0,\rm circ}}-B_d,
\qquad
(A_dB_d,D_{d_0})=1.
}
\tag{D0-circular-reader}
```

所以若

```math
D_{d_0}>10^{r_{d_0,\rm circ}},
```

则得到 ordinary exact source-phase lock；若 ordinary criterion失败，则由 `(D0-covers-NH)`：

```math
\boxed{
X_NX_H
\le D_{d_0}
\le10^{r_{d_0,\rm circ}}.
}
\tag{D0-failure}
```

结合现有 corrected third-gap bootstrap

```math
3\log F_-+\log(X_NX_H)\ge3S-o(S)
```

得到

```math
\boxed{
\log F_-
\ge S-\frac13r_{d_0,\rm circ}-o(S).
}
\tag{D0-failure-Fminus}
```

由于 `r_d0,circ<=m2/2<=S/2`，粗化为 `5S/6-o(S)`。这**不取代**前一 `7S/8` circular-failure lower；后者通过保留并再收费 denominator gcd 得到更强的 worst-case constant。本文 d0-reader的主要价值是：

1. source modulus更大；
2. `X_NX_H` 无 denominator-common escape；
3. ordinary-lock branch更容易触发；
4. 和 coprime `v`-residue一起直接控制 gap quotient `a`。

不能把同一 prefix-common `E` 同时当成新 modulus surplus与额外 independent height payer重复收费。

---


来源：`SRC-0174:32–709`。原文保全，当前论证以本节为准。

<a id="dd-06"></a>
### DD-06　共享预算下 canonical large gap 的渐近排除

**状态：已严格完成。** canonical t2=1，delta≤1/2 的无界序列最终 a<d0v；非有效，没有绝对 cutoff。

依赖：[DD-05](#dd-05)、[DD-B01](#dd-b01)

核对：`dd-gap-crt`

<a id="dd-06-detail-src-0174-721-1"></a>
#### 记号与命题

本节保留 `a` 为正整数 gap quotient，另用

```math
\alpha:=\log_{10}2,\qquad\beta:=1-\alpha,\qquad
A:=\frac{2(1+2\alpha)}3,\qquad
\lambda:=\frac{2+\alpha}{1+2\alpha},
```

```math
M_*:=\frac3A,\qquad c_*:=2+3\lambda,
\qquad \mu:=M_*-\frac mS,\qquad
\delta:=c_*-\frac nS.
```

Canonical `G=gamma V`、`(V,10)=1` 给

```math
\boxed{\Gamma:=\frac{\log_{10}\gamma}{S}
=\alpha G_2+\beta G_5+R.}
\tag{10.1}
```

这里 `G_2=v_2(G)/S`、`G_5=v_5(G)/S`、
`R=log_10(core_10(gamma))/S`；`Q_2,N_2,Q_5,N_5` 与
normalized Schmidt slack `sigma_S` 均沿上述 corrected quantitative-defect
文件定义，`sigma_S>=-o(1)`，其它 defects 非负。

令

```math
K_*:=c_*+1-2M_*
=\frac92-M_*
=1.691116422381968\ldots.
\tag{10.2}
```

则整个现行 one-channel neighborhood 有 quantitative gap location

```math
\boxed{
\frac1S\log_{10}\frac{a}{d_0v}
\le-K_*+\frac52\delta+o(1).}
\tag{Canonical-small-gap-location}
```

特别地 `delta<=1/2` 时右端至多
`-0.441116422381968...+o(1)`。所以该 neighborhood 中
**不存在 `a>=d_0v` 的无界 DD 序列**；任何满足这些假设的无界序列，最终都
落在 `0<a<d_0v`，并由 `(Gap-CRT-lock)` 得到 `a=rho_a`。

<a id="dd-06-detail-src-0174-721-2"></a>
#### 共享预算对 `3 Gamma - 2 mu` 的控制

未粗化 short-head estimate 为

```math
\frac{m_1}{S}
\le\frac\delta2
-\left(1-\frac\beta3\right)\mu
-\frac\beta3Q_5+\frac\beta3G_5
-\frac\beta6N_5+\frac R2+o(1).
\tag{10.3}
```

Two-adic reader给 `alpha G_2<=m_1/S+alpha Q_2+o(1)`。与 `(10.1)`
联立：

```math
\Gamma\le\frac\delta2
-\left(1-\frac\beta3\right)\mu
+\alpha Q_2-\frac\beta3Q_5
+\frac{4\beta}3G_5-\frac\beta6N_5
+\frac32R+o(1).
\tag{10.4}
```

因此

```math
3\Gamma-2\mu+\delta
\le\frac52\delta-(5-\beta)\mu
+3\alpha Q_2-\beta Q_5+4\beta G_5
-\frac\beta2N_5+\frac92R+o(1).
\tag{10.5}
```

使用**同一份** corrected Schmidt identity

```math
A\mu=\sigma_S+2\alpha Q_2+\alpha N_2
+\frac\beta3(2Q_5+4G_5+N_5)+2R+o(1),
\tag{10.6}
```

并写 `C:=(5-beta)/A=(4+alpha)/A`，得到

```math
\begin{aligned}
3\Gamma-2\mu+\delta
\le{}&\frac52\delta-C\sigma_S
+\alpha(3-2C)Q_2-\alpha C N_2\\
&-\beta\left(1+\frac{2C}3\right)Q_5
+\beta\left(4-\frac{4C}3\right)G_5\\
&-\beta\left(\frac12+\frac C3\right)N_5
+\left(\frac92-2C\right)R+o(1).
\end{aligned}
\tag{10.7}
```

因为 `alpha<2/3`（等价于 `2^3<10^2`），有 `C>3`。所以所有显示的
correction coefficients 都严格为负；`sigma_S>=-o(1)` 的误差仍可吸收进
`o(1)`。故

```math
\boxed{3\Gamma-2\mu+\delta\le\frac52\delta+o(1).}
\tag{Gamma-mu-shared-budget}
```

这一步没有把 common scale、prefix-common depth 或任何 local prime重复记账。

<a id="dd-06-detail-src-0174-721-3"></a>
#### exact small factor给 quantitative location

不先假设 large-gap。由 `(4.3)` 和 `g_*/v>=1`：

```math
F_-\ge L(u+2v)a
=\frac{a}{d_0v}\,uv(u+2v)
>\frac{a}{d_0v}\,Q^2v^3,
\tag{10.8}
```

最后一步使用 `u>Qv`。又 `Q>=10^{S-1}`、`G>=10^{S-2}`、
`v=G/gamma`，所以

```math
\frac1S\log_{10}\frac{a}{d_0v}
<\frac{\log_{10}F_-}{S}-5+3\Gamma+o(1).
\tag{10.9}
```

沿 d-dominant canonical sequence，前述 small-factor Archimedean upper 为

```math
\frac{\log_{10}F_-}{S}
\le4+2\frac mS-\frac nS+o(1).
\tag{10.10}
```

代入 `m/S=M_*-mu`、`n/S=c_*-delta`，再用
`(Gamma-mu-shared-budget)`，即得 `(Canonical-small-gap-location)`。

作为仅依赖 large-gap 假设的写法，`a>=d_0v` 会强迫

```math
\delta\ge\frac{2K_*}5-o(1)
=0.676446568952787\ldots-o(1),
```

与当前 `delta<=1/2` 有固定正余量。此 threshold 是联立不等式的必要条件，
不是把 one-channel 输入的作用域扩展到 `delta>1/2`。

<a id="dd-06-detail-src-0174-721-4"></a>
#### 更窄邻域中的两个单独 ordinary readers

本节还给出一个不增加 height payer 的位置推论。因为 `d_0|Q`、`v|G`，
且 `Q,G<10^S`，将 `(Canonical-small-gap-location)` 分别乘回 `d_0` 与 `v`
的 height可得

```math
\boxed{
\max\left\{
\frac1S\log_{10}\frac av,
\frac1S\log_{10}\frac a{d_0}
\right\}
\le-U_*+\frac52\delta+o(1),}
\qquad U_*:=K_*-1=0.691116422381968\ldots.
\tag{Separate-gap-reader-window}
```

因此对任意 fixed

```math
0\le\delta_0<\frac{2U_*}5
=0.276446568952787\ldots,
```

`delta<=delta_0` 的上述 canonical sequence最终满足

```math
\boxed{0<a<\min(d_0,v).}
\tag{Separate-ordinary-gap-locks}
```

此时两个 coprime reader各自都升级成普通整数重构：

```math
\boxed{
a=[\omega c_3A_{12}10^d]_{d_0}
=[-a_3c_3L^{-1}]_v,}
\tag{Separate-ordinary-gap-readers}
```

`[x]_M` 表示 `[0,M)` 中的 least residue。特别地这些 moduli 最终都大于
`1`，两个 residues都必须非零并彼此相等。

这是同一 location estimate的推论，不能把两个 least-residue equality
再当两份 independent lower height。`D0-parent` 与 `V-parent` 消去 `H_0`
只回到既有 exact determinant equation：

```math
\boxed{
c_3\bigl(v\omega A_{12}10^d-d_0a_3\bigr)=(u+v)a.}
\tag{Gap-reader-elimination}
```

因此，仅反复消去这两个 parents 不会产生新的 independent global
obstruction；仍须利用没有包含在该 exact source-gap normalization 中的
full-concat / chosen-orientation 兼容性，才能排除 ordinary-success 支。

<a id="dd-06-detail-src-0174-721-5"></a>
#### 核对与严格边界

机械核对命令：

证书命令与覆盖见 [统一核对目录](CHECKS.md)。

脚本以 symbolic substitution核对 `(10.5)--(10.7)`，以整数幂比较核对
`1/4<alpha<2/3`，并输出 threshold 和 uniform margin；这只是 exact algebra /
常数核对。无界排除来自本节的完整推导及输入定理，不来自有限枚举。

由于 corrected Schmidt 输入含非有效 `o(1)`，本节没有提供可计算的绝对
`S` 上界，没有排除剩余有限例外，也没有排除 small-gap ordinary CRT
representative。一般 DD 的 large-gap dichotomy、ordinary circular-lock
成功支与 DD 全局空性仍须另行处理。

---


来源：`SRC-0174:721–960`。原文保全，当前论证以本节为准。

<a id="dd-07"></a>
### DD-07　unique-five-tail、第二分母至多两位的无界排除

**状态：已严格完成。** b3=5,5∤b1b2,1≤m2≤2,n3≥2；不覆盖 m2≥3 或五进 prefix。

依赖：[DD-05](#dd-05)、[C08](#c08)

核对：`dd-gap-crt`

<a id="dd-07-detail-src-0174-961-1"></a>
#### 一位第三分母的 general source 归约

**状态：已严格完成（公开 necessary denominator condition；在 DD 中完整
关闭 `m_3=1,v>1`，保留 `v=1` 普通 source族）。** 本节允许前两分母和
全部分子位数无界，不使用 canonical、`t_2=1` 或 frozen top-DD。第一项
论证对三个分支统一成立，`n_3>=1` 即可。设 `1<=b_3<=9`，前缀 word 为
`Q=b_1 10^{m_2}+b_2`。原始 source ratio 给

```math
\frac uv=\frac{10Q}{b_3}\quad((u,v)=1),
\qquad
\boxed{v=\frac{b_3}{(10Q,b_3)}\le9.}
\tag{Single-digit-tail-source-denominator}
```

若 `2|v`，写 `e_3=v_2(b_3)>1+v_2(Q)`。原 word denominator
`D=10Q+b_3` 的二进 depth 是 `1+v_2(Q)<e_3`。但
[core.md §27.7](#dd-01) 的整数 sphere
要求最大分母二进 depth `E_2` 唯一，因而 `v_2(R)=-E_2<=-e_3`。
原 word ratio 则给 `v_2(R)>=-v_2(D)>-e_3`，矛盾。又因一位 `b_3`
的 five-depth 至多为一，`5` 不能整除 `v`。

余下任何 `v` 的素因子只能是 `p=3,7`，均为 Gaussian inert prime。
写 `e_i=v_p(b_i)`、`s=v_p(Q)`。因 `p|v`，有 `e_3>s`，故
`v_p(D)=s`。若 `e_1=e_2`，则 `s>=e_1=e_2`，第三分母独占最大值；
若 `e_1!=e_2`，则 `s=min(e_1,e_2)`，最高 depth只能由较大前缀与
第三分母中的一个或两个取得。两坐标同为最高时，其 leading unit
squares不能相消，因为 `-1` 在 `F_p` 中不是平方。因此在所有情况下
sphere均给

```math
v_p(R)=-\max(e_1,e_2,e_3)<-s,
```

与 word ratio的 `v_p(R)>=-v_p(D)=-s` 矛盾。这已排除 `v` 的全部
可能素因子，故

```math
\boxed{m_3=1\Longrightarrow b_3\mid10Q,\qquad v=1.}
\tag{Single-digit-tail-v-one}
```

这是跨分支的 necessary denominator condition，不是某个完整分支的
空性。特别地，在 DD normalization `u/v=kappa/G` 中还给 `gamma=G`。
这里是无界 state 排除，并非有限 prime enumeration 的经验结论：只有
`b_3<=9` 的素支持是有限的，prefix depths 与全部 word lengths均任意。
沿用 §1 的剥离定义可逐项恢复

```math
\omega=(10,b_3),\quad L=10/\omega,\quad
\tau=q=b_3/\omega,\quad d_0=Q/\tau,\quad u=LQ/\tau.
\tag{Single-digit-tail-reduced-source-dictionary}
```

其中 `q` 是 §1 的 reduced source quotient，不是 `q_lcm`。
`(L,tau)=1` 且 `tau|Q`；这一字典不能与 canonical `q_src/xi` 默认混用。
此时 `v`-residue 变为平凡模一条件，仍需处理 ordinary `d_0` / full-word
compatibility；没有由此增加第二份 source height。

<a id="dd-07-detail-src-0174-961-2"></a>
#### `b_3=5` 的 unique-five-tail unit 约束

**状态：已严格完成（必要条件，不是整个 `b_3=5` 子支空性）。** 进一步
假设 `5` 不整除 `b_1b_2`。因第三分母奇，core §27.7 已直接要求
`b_1,b_2` 均奇；不能再把这一二进 parent算成新排除。令
`q_lcm=5c_3`，其中 `c_3` 为 five-unit。原 word 与 integer sphere给

```math
H=\frac{c_3\mathscr A}{2Q+1},\qquad
H^2-y_3^2=y_1^2+y_2^2\equiv0\pmod{25},\qquad
y_3=c_3a_3.
```

第三分母独占 five-depth一，sphere要求 `v_5(R)=-1`。Reducedness使
`mathscr A=a_3 mod5` 为 unit，故 `2Q+1` 也必须是 five-unit。模五
sphere与原 word强迫 `(2Q+1)^2=1 mod5`；因 `Q=b_2!=0 mod5`，只剩

```math
Q\equiv4\pmod5,\qquad H\equiv-y_3\pmod5.
```

所以 `H-y_3` 为 five-unit，`H+y_3` 被 `25` 整除。DD 中 `n_3>=2`，
有 `mathscr A=a_3 mod25`，于是

```math
0\equiv(2Q+1)(H+y_3)
\equiv2c_3(Q+1)a_3\pmod{25}.
```

因 `2c_3a_3` 为 unit，得到

```math
\boxed{Q\equiv24\pmod{25},\qquad b_1,b_2\text{ 均奇}.}
\tag{Single-digit-five-tail-unit-necessary-state}
```

若 `m_2>=2`，这要求 `b_2=49 mod50`；若 `m_2=1`，则必须
`b_2=9,b_1=9 mod10`。这个 negative five-sheet在更高精度仍可兼容。
本节不宣称允许剩余类为空，不把该 unit condition收费为 independent
height budget。§27.7.3 的完整一位三分母证书是更小 denominator 域上的
另一结论，不能替代这里一般前缀分母的剩余证明。

<a id="dd-07-detail-src-0174-961-3"></a>
#### unique-five-tail 且第二分母至多两位的完整 DD state 关闭

**状态：已严格完成（无界 state 为空，无原候选有限枚举）。** 假设

```math
\boxed{b_3=5,\quad5\nmid b_1b_2,\quad1\le m_2\le2,\quad n_3>1.}
\tag{Unique-five-tail-one-digit-second-domain}
```

第一分母与全部分子位数均无界，不使用 canonical 或 frozen top-DD。
由 §11.1，两个 prefix denominators奇且 `Q=24 mod25`，故
`Q=49 mod50`。先设 `m_2=1`。因 `Q=10b_1+b_2`、`b_2` 一位，只剩

```math
b_2=9,\qquad b_1\equiv9\pmod{10},\qquad D=100b_1+95.
```

若 `3|b_1`，第三分母为三进 unit，前两最高三进 denominator depth
由一个或两个坐标取得。`3` inert使其 unit squares不能抵消，sphere
要求 `v_3(R)<0`。但 `D=100b_1+95` 是三进 unit，word要求
`v_3(R)>=0`，矛盾。因此 `(b_1,45)=1`。

对每个 `p^e||b_1`，其它两分母均为 `p`-unit，第一分数独占最高
denominator depth；sphere给 `v_p(R)=-e`，故原 word给 `p^e|D`。
合并所有 prime powers得 `b_1|D`，从而 `b_1|95`。排除五进 support后
只有 `b_1=1,19`，再由 `b_1=9 mod10` 只留 `19`。

最后 `(b_1,b_2,b_3)=(19,9,5)` 时 `D=1995` 的三进 depth为一，第二
分数独占三进 depth二。Sphere要求 `v_3(R)=-2`，word却给
`v_3(R)>=-1`，矛盾，关闭一位第二分母。

再设 `m_2=2`。必要 `b_2=49 mod50` 只留 `b_2=49,99`。

1. **`b_2=49`。** 若 `7|b_1`，前两最高七进 depth由一个或两个坐标
   取得，inert unit squares不能抵消；但 `D=1000b_1+495` 在七进为
   unit，矛盾。因此 `(b_1,245)=1`，逐 prime power unique maximum
   再给 `b_1|D`、`b_1|495`，five-unit使 `b_1|99`。
   `b_2` 独占七进 depth二，word必须 `D=0 mod49`，即
   `20b_1+5=0 mod49`，要求 `b_1=12 mod49`。`99` 的 positive divisors
   `1,3,9,11,33,99` 均不满足，矛盾。
2. **`b_2=99`。** 若 `3` 或 `11` 整除 `b_1`，原 denominator
   `D=1000b_1+995` 分别为该 inert prime的 unit，而 sphere的最高
   depth由一个或两个 prefix坐标取得，仍矛盾。因此 `(b_1,495)=1`。
   再由 unique maximum得 `b_1|995`，five-unit只留 `1,199`。
   `b_2` 独占三进 depth二，word要求 `D=0 mod9`，即 `b_1+5=0 mod9`。
   两个允许值均为 `1 mod9`，矛盾。

因此整个 `(Unique-five-tail-one-digit-second-domain)` 为空。本节只枚举
必要 denominator values / divisors，没有有限枚举 original numerators；
第一分母与分子长度的无界覆盖由上述父式承担。允许 `5|b_1b_2` 或
`m_2>=3` 的其它五进一位尾状态仍待证。

机械核对继续使用 §10.5 的专用脚本；新增部分遍历小样本只核对 source
dictionary 和 `mod5/mod25` unit projection，无界覆盖由以上赋值及
整除推导承担。

---


来源：`SRC-0174:961–1123`。原文保全，当前论证以本节为准。

<a id="dd-08"></a>
### DD-08　denominator entropy 与非循环 joint count

**状态：已严格完成。** fixed delta0<1/2；保留短 suffix 的线性 entropy，条件唯一性不串成 joint 唯一。

依赖：[DD-05](#dd-05)、[DD-B01](#dd-b01)、[DD-B02](#dd-b02)

核对：`dd-denominator-entropy`、`dd-numerator-count`、`dd-global-sparsity`、`dd-gap-reconstruction`

<a id="dd-08-detail-src-0151-51-1"></a>
#### 记号与 slope window

令

```math
a:=\log_{10}2,
\qquad
\lambda:=\frac{2+a}{1+2a}
=1.436294525872677\ldots,
```

```math
c_*:=2+3\lambda
=6.308883577618031\ldots.
```

对单个 candidate 写

```math
\delta':=c_*-\frac nS\ge0.
```

为便于做统一计数，固定一个常数 `delta_0`，考虑 terminal window

```math
\boxed{0\le\delta'\le\delta_0.}
\tag{1.1}
```

下文所有 `o(S)` 对 fixed `delta_0` 一致理解。

Schmidt/Farey slack 为 `sigma_S`，rough overlap height 为

```math
R:=\frac1S\log_{10}\gamma_0,
\qquad
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0,
\qquad
(\gamma_0,10)=1.
```

quantitative defect theorem 给

```math
\boxed{
\delta'
\ge
\lambda\sigma_S
+(2\lambda-1)R
+\text{其它非负 charged terms}
-o(1).}
\tag{1.2}

```
并且

```math
2\lambda-1
=1.872589051745354\ldots
>\lambda.
\tag{1.3}

```
因此立即有

```math
\boxed{
\sigma_S+R
\le\frac{\delta'}{\lambda}+o(1)
\le\frac{\delta_0}{\lambda}+o(1).}
\tag{Shared-entropy-budget}

```
其中

```math
\boxed{
\frac1\lambda
=\frac{1+2a}{2+a}
=0.696236030971719\ldots.}
\tag{1.4}

```
---

<a id="dd-08-detail-src-0151-51-2"></a>
#### Farey side 只支付 `sigma_S S`

canonical S-unit equation为

```math
\boxed{2^HZ-5^TU=V,}
\tag{2.1}

```
且

```math
(U,Z)=1.
```

`dd-corrected-schmidt-farey-slack-2026-08-22.md` 已证明

```math
\left|\frac ZU-\frac{5^T}{2^H}\right|
=
\frac{10^{\sigma_SS+o(S)}}{U^2}.
\tag{2.2}

```
因此在 fixed smooth/exponent fiber 中，Farey separation 给 projective rational candidates

```math
\boxed{
N_{UZ}
\le10^{\sigma_SS+o(S)}.}
\tag{2.3}

```
这里保留 candidate-specific `sigma_S`，而不先粗化成 `delta_0/lambda`。

`H,T` 以及 terminal 中所有 digit lengths / valuation exponents 都是 `O(S)` 的非负整数；固定有限个这类坐标只产生

```math
S^{O(1)}=10^{o(S)}
```

个 combinatorial/exponent fibers。若 `sigma_S` 在 window 内移动，可按宽 `1/S` 的区间分层；层数仍为 `S^{O(1)}`，不会改变正线性 exponent。

所以 Farey/projective side 的全部正线性 counting cost 就是

```math
\boxed{\sigma_SS.}
\tag{2.4}

```
---

<a id="dd-08-detail-src-0151-51-3"></a>
#### `gamma` 的 candidate entropy 只有 rough part `R S`

写

```math
\boxed{
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0.}
\tag{3.1}

```
对 fixed `S,delta_0`，terminal normalized valuation bounds保证

```math
\mathfrak g,g_5=O(S).
```

所以 smooth exponents `(mathfrak g,g_5)` 只有 `S^{O(1)}` 种。

固定一个 `R`-layer 后，

```math
1\le\gamma_0\le10^{RS+o(S)},
```

故最粗的整数计数已经给

```math
\boxed{
N_{\gamma}
\le10^{RS+o(S)}.}
\tag{3.2}

```
特别地，不应使用

```math
10^{(\log\gamma) }
```

去枚举 `gamma`：其中 `2^{mathfrak g}` 与 `5^{g_5}` 的巨大数值高度来自两个指数坐标，而不是指数多种独立整数选择。

---

<a id="dd-08-detail-src-0151-51-4"></a>
#### 固定 `V,gamma` 后 denominator factorization 只有 `10^{o(S)}` 种

quantitative one-channel decomposition给 exact

```math
\boxed{V=v_1v_2,}
\tag{4.1}

```
其中

```math
v_1\mid b_1,
\qquad
v_2\mid b_2.
```

又 canonical denominator product 为

```math
\boxed{G=b_1b_2=\gamma V.}
\tag{4.2}

```
定义整数

```math
t_1:=b_1/v_1,
\qquad
t_2:=b_2/v_2.
```

由 `(4.1)--(4.2)` exact 地得到

```math
\boxed{t_1t_2=\gamma.}
\tag{4.3}

```
因此固定 `V,gamma` 后，所有可能的 `(b_1,b_2)` 都来自

```math
v_1v_2=V,
\qquad
t_1t_2=\gamma,
```

再令

```math
\boxed{b_1=v_1t_1,
\qquad b_2=v_2t_2.}
\tag{4.4}

ordered factor assignments 的数目至多

```
```math
\tau(V)\tau(\gamma).
```

terminal heights 给

```math
\log V,\log\gamma=O(S).
```

由标准 divisor bound

```math
\log\tau(N)=O\left(\frac{\log N}{\log\log N}\right)
=o(S)
\qquad(N\le10^{O(S)}),
```

所以统一有

```math
\boxed{
\tau(V)\tau(\gamma)=10^{o(S)}.}
\tag{4.5}

```
这一步同时吸收了：

- small/large channel 的 prime assignment；
- `b_2/v_2` 的 cofactor freedom；
- `b_1/v_1` 的 cofactor freedom。

它们不再各自支付 `O(delta S)` 的 raw interval entropy。

---

<a id="dd-08-detail-src-0151-51-5"></a>
#### 其余 denominator/source data 随后被 exact reconstruction 固定

固定 digit lengths，特别是 `m_2` 后，prefix concat 为

```math
\boxed{Q=b_1 10^{m_2}+b_2.}
\tag{5.1}

canonical phase又有

```
```math
\boxed{Q=Uq.}
\tag{5.2}

```
所以固定 `(U,b_1,b_2,m_2)` 后：

- 若 `U` 不整除 `Q`，该 factor assignment 不合法；
- 若整除，则
```math
  \boxed{q=Q/U}
```
  唯一。

同时

```math
\boxed{B=\frac{10^m}{2\cdot5^T}}
\tag{5.3}

```
由 `(m,T)` 唯一，而 exact third-denominator factorization

```math
\boxed{b_3=BVq}
\tag{5.4}

```
进一步唯一恢复 `b_3`。

因此在 fixed combinatorial/exponent fiber 中：

1. Farey candidate `(U,Z)` 决定
```math
   V=2^HZ-5^TU;
```
2. `gamma_0` 与 smooth exponents决定 `gamma`；
3. `(V,gamma)` 只有 `10^{o(S)}` 个 factor assignments；
4. 每个 assignment 之后 `b_1,b_2,Q,q,B,b_3` 全部由 exact formulas 决定或被 integrality/digit-length test 淘汰。

所以 denominator/S-unit data 本身没有其它 positive-linear candidate entropy。

---

<a id="dd-08-detail-src-0151-51-6"></a>
#### denominator / S-unit family 的总 entropy bound

由 §§2--5，在一个 fixed `(sigma_S,R)` layer 内：

```math
N_{\rm den/SU}
\le
10^{(\sigma_S+R)S+o(S)}.
\tag{6.1}

```
再用 `(Shared-entropy-budget)`：

```math
\boxed{
N_{\rm den/SU}(S;\delta_0)
\le
10^{(\delta_0/\lambda)S+o(S)}.}
\tag{Den-SU-entropy}

```
数值即

```math
\boxed{
N_{\rm den/SU}(S;\delta_0)
\le
10^{0.696236030972\,\delta_0 S+o(S)}.}
\tag{6.2}

```
这比逐项把 `gamma`、`v_1`、`b_2/v_2` 的 raw height 都当成独立 entropy 的估计严格更强；关键改进来自 **smooth valuation coordinates 只按指数枚举** 与 **factor assignment 只花 divisor entropy**。

---


<a id="dd-08-detail-src-0140-61-1"></a>
#### constants 与现有 exact periods

令

```math
a:=\log_{10}2,
\qquad b:=1-a,
```

```math
A:=\frac{2(1+2a)}3,
\qquad
\lambda:=\frac{2+a}{1+2a},
```

```math
U_*:=0.691116422381969\ldots,
\qquad
z_*:=1-U_*=0.308883577618031\ldots.
```

固定

```math
\delta:=c_*-\frac nS,
\qquad
\mu:=M_*-\frac mS.
```

`dd-corrected-carry-u-pairmax-crt-2026-08-22.md` 已严格证明：固定 denominator/S-unit data 与 `(R_0,g_0,a_2)` 后，`A_12` 同时满足

```math
A_{12}\equiv\rho_U\pmod U,
\qquad
A_{12}\equiv\rho_V\pmod{v_2},
```

并且

```math
\boxed{(U,v_2)=1.}
```

所以 exact combined period 为

```math
\boxed{M_{UV}=Uv_2.}
\tag{1.1}
```

另一方面 `d_3`-dominant digit simplex 给

```math
\boxed{0<A_{12}<10^{S+2}.}
\tag{1.2}
```

因此只要能够证明

```math
Uv_2>10^{S+2},
```

fixed fiber 中 `A_12` 就至多一个。

---

<a id="dd-08-detail-src-0140-61-2"></a>
#### `Uv_2` 的未粗化 shared-defect lower

`dd-corrected-common-scale-ray-sharp-2026-09-06.md` 已记录

```math
\boxed{
\frac{\log U}{S}-U_*
=
\frac{2b}{3}\mu
-aG_2
-\frac{2b}{3}Q_5
-\frac b3G_5
-\frac b3N_5
-R+o(1),}
\tag{2.1}
```

以及

```math
\boxed{
\frac{\log V}{S}
=1-aG_2-bG_5-R+o(1).}
\tag{2.2}
```

因为

```math
V=v_1v_2,
\qquad
v_1\mid b_1,
\qquad
b_1<10^{m_1},
```

有

```math
\boxed{
\frac{\log v_2}{S}
\ge
\frac{\log V}{S}-\frac{m_1}{S}-o(1).}
\tag{2.3}
```

同一 sharp ledger 还给

```math
\boxed{
\begin{aligned}
\frac{m_1}{S}
\le{}&\frac\delta2
-\left(1-\frac b3\right)\mu
-\frac b3Q_5
+\frac b3G_5\\
&-\frac b6N_5
+\frac R2+o(1),
\end{aligned}}
\tag{m1-sharp}
```

以及

```math
\boxed{
aG_2\le\frac{m_1}{S}+aQ_2+o(1).}
\tag{G2-via-m1}
```

由 `(2.1)--(2.3)`：

```math
\frac{\log(Uv_2)}S-(1+U_*)
\ge
\left(\frac{\log U}{S}-U_*\right)
+\left(\frac{\log V}{S}-1\right)
-\frac{m_1}{S}-o(1).
\tag{2.4}
```

第一次代入 `(m1-sharp)`，再用 `(G2-via-m1)` 处理式中 `-2aG_2`，并第二次代入同一个 `(m1-sharp)`，精确整理得到

```math
\boxed{
\begin{aligned}
\frac{\log(Uv_2)}S-(1+U_*)
\ge{}&-\frac32\delta
+\left(3-\frac b3\right)\mu
-2aQ_2\\
&+\frac b3Q_5
-\frac{7b}{3}G_5
+\frac b6N_5
-\frac72R-o(1).
\end{aligned}}
\tag{Uv2-prebudget}
```

这一步正是旧 `carry-U × pair-max` theorem 中缺失的 sharper reuse：旧证明使用了已经粗化的 `G_2` upper，因此让 `G_5,R` 再次支付了一整份额外 defect。

---

<a id="dd-08-detail-src-0140-61-3"></a>
#### exact `mu` budget 后所有 correction 都非负

继续使用现行 exact normalized identity

```math
\boxed{
A\mu
=\sigma_S
+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)
+2R+o(1).}
\tag{Mu-budget}
```

定义

```math
\boxed{
\eta:=\frac{3-b/3}{A}
=\frac{8+a}{2(1+2a)}
=2.590736314681693\ldots.}
\tag{3.1}
```

将 `(Mu-budget)` 代入 `(Uv2-prebudget)`：

```math
\boxed{
\begin{aligned}
\frac{\log(Uv_2)}S
\ge{}&1+U_*-\frac32\delta
+\eta\sigma_S\\
&+2a(\eta-1)Q_2
+a\eta N_2\\
&+\frac{b(2\eta+1)}3Q_5
+\frac{b(4\eta-7)}3G_5\\
&+\frac{b(2\eta+1)}6N_5
+\left(2\eta-\frac72\right)R
-o(1).
\end{aligned}}
\tag{Uv2-sharp-full}
```

因为

```math
\eta>\frac74,
```

所有显示 correction coefficients 都严格为正。因此得到 universal lower：

```math
\boxed{
\frac{\log_{10}(Uv_2)}S
\ge1+U_*-\frac32\delta-o(1).}
\tag{Uv2-sharp}
```

这与  direct source-quotient lock 中出现的 `3/2` loss 来自同一个 shared-defect cancellation，但这里作用于不同的 exact period `Uv_2`。

---

<a id="dd-08-detail-src-0140-61-4"></a>
#### `A_12` uniqueness threshold 扩展到 `0.460744...`

由 `(1.2)` 与 `(Uv2-sharp)`，若

```math
U_*-\frac32\delta>0,
```

则 sufficiently large `S` 上

```math
Uv_2>10^{S+2}.
```

定义

```math
\boxed{
\delta_{UV}^{\sharp}
:=\frac{2U_*}{3}
=0.460744281587979\ldots.}
\tag{4.1}
```

于是

```math
\boxed{
\delta<\delta_{UV}^{\sharp}
\Longrightarrow
\#\{A_{12}\mid R_0,g_0,a_2,\text{fixed denominator/S-unit}\}
\le1.}
\tag{A12-sharp-unique}
```

carry 再唯一恢复 `a_3`；固定 `(n_2,a_2)` 后 `A_12` 也唯一恢复 `a_1`。

旧 threshold

```math
0.238062349248111\ldots
```

因此被严格替换为

```math
0.460744281587979\ldots.
```

---

<a id="dd-08-detail-src-0140-61-5"></a>
#### fixed gap fiber 的 short suffix 在整个 one-channel neighborhood 内唯一

 sharp one-channel lower 为

```math
\boxed{
\frac{\log v_2}{S}\ge1-\delta-o(1).}
\tag{5.1}
```

而 digit polarization 给

```math
\boxed{
\frac{n_2}{S}
\le\kappa_{\rm dig}\delta+o(1),
\qquad
\kappa_{\rm dig}:=\frac{2+a}{3}
=0.767009998554660\ldots.}
\tag{5.2}
```

pair-max short-suffix theorem只在 fixed primitive gap `(R_0,g_0)` 与
orientation `Omega` 下证明

```math
a_2\equiv\rho_{2,\Omega}(R_0/g_0)\pmod{v_2}.
```

若

```math
1-\delta>\kappa_{\rm dig}\delta,
```

则 `v_2>10^{n_2}>a_2`，故每个 fixed gap/orientation fiber至多一个 `a_2`。

对应 threshold 为

```math
\boxed{
\delta<\delta_{a_2}^{\sharp}
:=\frac1{1+\kappa_{\rm dig}}
=0.565927754125872\ldots.}
\tag{5.3}
```

现行 quantitative one-channel theorem 只使用 `delta<=1/2`。因此在它的整个严格内部 `delta<1/2`：

```math
\boxed{
\#\{a_2\mid\Omega,R_0,g_0,\text{fixed denominator/S-unit}\}\le1.}
\tag{a2-global-one-channel}
```

orientation 数量仍只有

```math
2^{\omega(v_2)}=10^{o(S)}.
```

---

<a id="dd-08-detail-src-0140-61-6"></a>
#### gap fraction 在整个 `delta<1/2` one-channel neighborhood 内唯一

已有 gap rational reconstruction 对 fixed denominator/S-unit、orientation `Omega` 与 `a_2` 给

```math
\boxed{
v_2\mid
\Delta_{\rm gap}
:=R_0g_0'-R_0'g_0,}
\tag{6.1}
```

且若两个 reduced fractions不同，则

```math
\boxed{
0<|\Delta_{\rm gap}|
\le10^{\delta S+o(S)}.}
\tag{6.2}
```

利用新的 `(5.1)`，只要

```math
1-\delta>\delta,
```

就有 sufficiently large `S`：

```math
v_2>|\Delta_{\rm gap}|,
```

与 `(6.1)` 对非零 determinant 的整除矛盾。

所以

```math
\boxed{
\delta<\frac12
\Longrightarrow
\#\{(R_0,g_0)\mid\Omega,a_2,\text{fixed denominator/S-unit}\}
\le1.}
\tag{Gap-global-one-channel}
```

旧 gap threshold

```math
0.299845580176277\ldots
```

因此不再是当前 sharp one-channel proof tree 的有效 barrier。

---


<a id="dd-08-detail-src-0140-494-1"></a>
#### 修复：先枚举真正未固定的 `a_2`

固定 denominator/S-unit data、全部 digit lengths及 selected Gaussian
orientations。直接枚举

```math
10^{n_2-1}\le a_2<10^{n_2},
```

至多 `10^{n_2}` 个 integers。对每个 `a_2`，§6 使用的实际 reader是

```math
K_\Omega R_0\equiv a_2c_2g_0\pmod{v_2},
\qquad K_\Omega=2F\iota_\Omega c_3,
\qquad(K_\Omega,v_2)=1.
```

`K_Omega,c_2,v_2` 只依赖已固定的 denominator/S-unit/orientation data；
这里没有固定或引用 `a_1,A_12`。共同 height bound
`P_gap+R<=delta+o(1)` 与 `log_10 v_2/S>=1-delta-o(1)`，严格在 fixed
`delta_0<1/2` 时使该 `a_2` 对应的 reduced gap fraction至多一个。

随后固定该 fraction，使用
[`两-channel period`](RESEARCH.md#dd-retired)（原始记录 SRC-0143）

```math
P_{\rm 2sh}=Uv_1^2v_2,
\qquad
\frac{\log_{10}P_{\rm 2sh}}S
\ge1+U_*-\delta-o(1),
```

使 `A_12` 至多一个，carry与 prefix splitting随后恢复 `a_3,a_1`。

两 channels的全部 orientation choices最多 `2^{omega(V)}`。因为
`V|G<10^S`，若 `k=omega(V)`，则 `k!<=V`，所以
`k=O(S/log S)`，即 `2^{omega(V)}=10^{o(S)}`。全部 digit / valuation
indices为 `O(S)`，其有限个坐标的选择数为 `S^{O(1)}=10^{o(S)}`。

所以安全的 fixed-denominator bound是

```math
\boxed{
N_{\rm num}(S;\delta)
\le10^{n_2+o(S)}
\le10^{\kappa_{\rm dig}\delta S+o(S)},
\quad \kappa_{\rm dig}=\frac{2+\log_{10}2}{3},
\quad \delta\le\delta_0<\frac12.}
\tag{Noncircular-numerator-bound}
```

范围更正和撤回记录见 [研究审计](RESEARCH.md#dd-retired)。

---


<a id="dd-08-detail-src-0153-19-1"></a>
#### 真实枚举顺序与范围

令

```math
\alpha:=\log_{10}2,\qquad\beta:=1-\alpha,\qquad
A:=\frac{2(1+2\alpha)}3,\qquad
\lambda:=\frac{2+\alpha}{1+2\alpha},
```

```math
M_*:=\frac3A,\qquad c_*:=2+3\lambda,\qquad
\delta:=c_*-\frac nS,\qquad \mu:=M_*-\frac mS.
```

固定任意 `0<=delta_0<1/2`，考虑 `0<=delta<=delta_0` 的 corrected canonical
candidates。全部 digit lengths和 normalized valuation/slack layers均只有
`S^{O(1)}` 个 combinatorial choices，吸收进 `10^{o(S)}`。

对每个 denominator/S-unit candidate，枚举两-channel Gaussian orientations，
然后直接枚举实际未固定的 `a_2`：

```math
10^{n_2-1}\le a_2<10^{n_2}.
```

Orientation choices至多 `2^{omega(V)}=10^{o(S)}`，因为 `V|G<10^S`。
对每个 fixed `a_2` 与 orientation，reader

```math
2\cdot5^T\iota_\Omega c_3R_0
\equiv a_2c_2g_0\pmod{v_2}
```

不含 `A_12,a_1`，且所有 coefficient由 denominator/S-unit data固定。
Gap Farey determinant的 height至多 `delta S+o(S)`，而
`log_10 v_2/S>=1-delta-o(1)`；因此 `delta<=delta_0<1/2` 时 reduced
`R_0/g_0` 至多一个。

随后 fixed `a_2+gap+两-channel orientations` 的 exact period为

```math
\boxed{P_{\rm 2sh}=Uv_1^2v_2,\qquad
\frac{\log_{10}P_{\rm 2sh}}S\ge1+U_*-\delta-o(1),}
```

其中 `U_*=0.691116422381969...>1/2`。于是 eventually
`P_2sh>10^{S+2}>A_12`，所以 `A_12` 至多一个，carry / prefix splitting
恢复 `a_3,a_1`。

故 **安全的 fixed-denominator bound** 是

```math
\boxed{N_{\rm num}\le10^{n_2+o(S)}.}
\tag{Direct-suffix-enumeration}
```

这仍允许 positive-linear numerator entropy；后续 global proof必须把
`n_2/S` 保留在联合预算中，不能先删成 `o(1)`。

---

<a id="dd-08-detail-src-0153-19-2"></a>
#### denominator entropy与 short-suffix height的未粗化联合式

Denominator-only Farey / rough-core / divisor-assignment proof保持有效。
Common-scale ray的 sharp refinement给每个 `(sigma_S,R)` layer

```math
\boxed{N_{\rm den/SU}\le10^{(\sigma_S+R/2)S+o(S)}.}
\tag{Denominator-scale-entropy}
```

这里 fixed phase/factor split 后 denominator movement仅沿
`gamma=ell^2 bar_gamma` 的 common scale，因此 rough `ell` 的计数只花
`R/2`，不是 `R`。这一步不使用 numerator joint collapse。

Short suffix的未粗化 height与 short denominator同样受 digit polarization
控制。由 `s_1=max(s_1,s_2)`、`n_1>=s_1+1`、`n_1+n_2<=S+2`，有
`n_2/S<=1-s_1/S+o(1)`。保留 digit theorem的 full correction，得到

```math
\boxed{
\frac{n_2}{S}
\le\frac\delta2-\left(1-\frac\beta3\right)\mu
-\frac\beta3Q_5+\frac\beta3G_5
-\frac\beta6N_5+\frac R2+o(1).}
\tag{Suffix-sharp}
```

由 `(Direct-suffix-enumeration)` 与 `(Denominator-scale-entropy)`，需要
控制的是联合 exponent

```math
E:=\sigma_S+\frac R2+\frac{n_2}{S}.
```

代入 `(Suffix-sharp)`：

```math
E\le\frac\delta2+\sigma_S+R
-\left(1-\frac\beta3\right)\mu
-\frac\beta3Q_5+\frac\beta3G_5
-\frac\beta6N_5+o(1).
\tag{Joint-entropy-prebudget}
```

不能分别把 denominator与 suffix各自的最坏 height加起来；二者使用同一份
Schmidt/digit defect budget。

---

<a id="dd-08-detail-src-0153-19-3"></a>
#### exact `Mu-budget` 后所有 rough/valuation corrections为负

使用

```math
A\mu=\sigma_S+2\alpha Q_2+\alpha N_2
+\frac\beta3(2Q_5+4G_5+N_5)+2R+o(1).
\tag{Mu-budget}
```

关键 exact coefficient identity为

```math
\frac{1-\beta/3}{A}=\frac\lambda2.
```

因此 `(Joint-entropy-prebudget)` 精确变成

```math
\boxed{
\begin{aligned}
E\le{}&\frac\delta2+\left(1-\frac\lambda2\right)\sigma_S
-\alpha\lambda Q_2-\frac{\alpha\lambda}2N_2\\
&-\frac{\beta(1+\lambda)}3Q_5
+\frac{\beta(1-2\lambda)}3G_5\\
&-\frac{\beta(1+\lambda)}6N_5
+(1-\lambda)R+o(1).
\end{aligned}}
\tag{Joint-entropy-shared-budget}
```

`1<lambda<2`，所以除 `sigma_S` 外，所有 correction coefficients严格为负。
Quantitative defect给

```math
\lambda\sigma_S\le\delta+o(1).
```

故

```math
\boxed{
E\le\frac\delta2+
\left(1-\frac\lambda2\right)\frac\delta\lambda+o(1)
=\frac\delta\lambda+o(1).}
\tag{Joint-entropy-bound}
```

这是 global count的非循环修复；未把 gap/suffix同源唯一性当独立 payer。

---

<a id="dd-08-detail-src-0153-19-4"></a>
#### 修复后的 global candidate count

对 fixed `delta_0<1/2`，逐 `O(1/S)`-width normalized layers应用上节，再
汇总 polynomial many layers，得到

```math
\boxed{
N_{\rm term}(S;\delta_0)
\le10^{(\delta_0/\lambda)S+o(S)},
\qquad 0\le\delta_0<\frac12.}
\tag{Terminal-sparsity-noncircular}
```

数值 coefficient仍是

```math
\boxed{\lambda^{-1}=0.696236030971719\ldots.}
```

旧 positive-width global exponent被恢复，作用域从
`delta_0<0.460744281587979...` 扩至现行 one-channel的整个严格内部。
不同之处是 surviving fixed-denominator numerators仍允许
`10^{n_2+o(S)}` 个；其 entropy在全局与 denominator entropy共用同一预算，
并没有单独消失。

当 `delta->0` 时，上述安全 numerator和 global bounds都仍给
`10^{o(S)}` 的 equality-scale sparsity。该结论不提供 deterministic
location obstruction、strict slope gap或 effective absolute height bound。

---


来源：`SRC-0151:51–391`；`SRC-0140:61–463`；`SRC-0140:494–551`；`SRC-0153:19–212`。原文保全，当前论证以本节为准。

<a id="dd-09"></a>
### DD-09　ordinary full-word 与 selected sheets 的依赖边界

**状态：已严格完成。** full-concat 恰被原 source-gap determinant 吸收；norm 不自动供新 payer。

依赖：[DD-05](#dd-05)、[DD-08](#dd-08)

核对：`dd-numerator-count`

<a id="dd-09-detail-src-0143-137-1"></a>
#### 统一两个 gap 记号

令 `F=5^T`，并把 canonical source 写成 `q_src`，以区别一般 gcd-normal
reduced source `q_red`。有

```math
u=2FU,\qquad v=V=v_1v_2,\qquad Q=Uq_{\rm src},
\qquad B=\frac{10^m}{2F}.
```

由于 `(U,2FV)=1`，写

```math
\xi:=(2F,q_{\rm src})
```

即得到 exact dictionary

```math
\boxed{
d_0=U\xi,\qquad L=\frac{2F}{\xi},\qquad
q_{\rm red}=\frac{q_{\rm src}}\xi,\qquad
\omega=B\xi,\qquad v=V.}
\tag{Gap-chart-dictionary}
```

注意 `xi` 只含 `2,5`；这里不把它与旧 overlap notation中的 `eta`
混同。`c_i=q_lcm/b_i`，sphere gap为

```math
H_{\rm sph}-y_3=La.
```

旧 primitive gap fraction的定义于是精确等于

```math
\boxed{
\frac{R_0}{g_0}
=\frac{H_{\rm sph}-y_3}{2Fc_3}
=\frac{a}{\xi c_3}.}
\tag{Ordinary-primitive-gap-dictionary}
```

因此令 `h_a=(a,xi c_3)`，则

```math
\boxed{R_0=a/h_a,\qquad g_0=\xi c_3/h_a.}
\tag{Reduced-gap-dictionary}
```

本轮 `a` 的 exponentially small ordinary window约束这个原有 fraction；
它没有引入第二个独立 gap variable。

<a id="dd-09-detail-src-0143-137-2"></a>
#### original full-concat equation恰被 exact gap determinant吸收

完整 decimal words为

```math
\mathsf A=A_{12}10^n+a_3,\qquad
\mathsf B=Q10^m+b_3,
\qquad d=n-m.
```

在 `y_3=a_3c_3`、`b_3=omega tau`、`10^m=omega L` 与
`H_sph-y_3=La` 已建立后，original equality

```math
q_{\rm lcm}\mathsf A=H_{\rm sph}\mathsf B
```

**等价于**

```math
\boxed{q_{\rm lcm}A_{12}10^d-QH_{\rm sph}=\tau a.}
\tag{Full-word-gap-equivalence}
```

两方向都只是乘除 `10^m`：右侧乘 `10^m` 等于
`b_3 La=b_3H_sph-q_lcm a_3`。再代入 gcd-normal data与
`H_sph=VH_0`，便得到原先的两个 parents

```math
\omega c_3 A_{12}10^d=a+d_0H_0,
\qquad VH_0=a_3c_3+La.
```

消去 `H_0` 并代入 `(Gap-chart-dictionary)` 与
`(Ordinary-primitive-gap-dictionary)`，恰恢复 exact carry

```math
\boxed{
Ua_3=BV10^d A_{12}-\Sigma\frac{R_0}{g_0},
\qquad\Sigma=2FU+V.}
\tag{Full-word-carry-dictionary}
```

所以把 ordinary `a` 再代回完整 word 的**代数 equality**，不会产生一个尚未
被 determinant/carry吸收的新 parent。剩余 original constraints是各块实际的
digit intervals、reducedness和 sphere/orientation compatibility；不能把
`(Full-word-gap-equivalence)` 作为第二份 height lower。

<a id="dd-09-detail-src-0143-137-3"></a>
#### 两个 selected Gaussian sheets及其实际 effective periods

对 `i=1,2`，general moving-core sphere theorem给 chosen Gaussian products

```math
N(\Pi_i)=v_i,\qquad \Pi_i^2\mid y_i+i y_3.
\tag{Two-selected-sheets}
```

这里 Gaussian imaginary unit与下标 `i` 区分理解。逐 `p^h||v_i`，equivalent
reader是某个 selected Hensel root `iota_{i,p}`，满足

```math
\iota_{i,p}^2\equiv-1\pmod{p^{2h}},\qquad
c_i a_i+\iota_{i,p}c_3a_3\equiv0\pmod{p^{2h}}.
\tag{Two-sheet-local-readers}
```

这些 target primes均 `p∤10 U c_i c_3 g_0`。将 carry代入，得到 W-free
full-prefix expression

```math
\boxed{
g_0Uc_i a_i
+\iota_{i,p}c_3
\bigl(g_0BV10^dA_{12}-\Sigma R_0\bigr)
\equiv0\pmod{p^{2h}}.}
\tag{Two-sheet-full-prefix}
```

它区分 chosen sheets，但仍属于原 sphere/orientation parent加上 exact carry；
不是一个独立于 sphere的第二 orientation parent。

不过该式可以安全加强**条件重构 period**。固定 denominator/S-unit data、
全部 digit lengths、`a_2`、primitive fraction `(R_0,g_0)`，以及两个 channels
上的 selected Hensel roots。若同一 fiber有两个 candidates，记
`Delta A=A_12'-A_12`。Carry先给

```math
U\Delta a_3=BV10^d\Delta A,\qquad U\mid\Delta A.
\tag{Two-sheet-carry-difference}
```

对 `p^h||v_2`，`a_2` fixed，故 selected sheet相减给

```math
p^{2h}\mid c_3\Delta a_3.
```

使用 `(Two-sheet-carry-difference)` 与 `v_p(V)=h`，得到
`p^h|Delta A`，即原来的 `v_2` period。

对 `p^h||v_1`，因为 `a_1=(A_12-a_2)/10^{n_2}`，相减并乘
`U10^{n_2}` 得

```math
\boxed{
\left(Uc_1+\iota_{1,p}c_3BV10^{d+n_2}\right)\Delta A
\equiv0\pmod{p^{2h}}.}
\tag{First-sheet-unit-coefficient}
```

括号第一项是 p-unit，第二项被 `p^h` 整除，所以整个 coefficient是
p-unit。因此 `p^{2h}|Delta A`，聚合得到

```math
\boxed{v_1^2\mid\Delta A.}
\tag{First-sheet-square-period}
```

`U,v_1,v_2` 两两互素，故这一明写条件的 fiber具有 exact joint period

```math
\boxed{P_{\rm 2sh}:=Uv_1^2v_2=UVv_1\mid\Delta A.}
\tag{Two-sheet-conditional-period}
```

由 common-scale sharp theorem的 `log_10(UV)/S>=1+U_*-delta-o(1)`，
有

```math
\frac{\log_{10}P_{\rm 2sh}}S
\ge1+U_*-\delta-o(1).
```

因为 `U_*=0.691116...>1/2`，整个 fixed `delta_0<1/2` neighborhood中，
eventually `P_2sh>10^{S+2}`。而 `0<A_12<10^{S+2}`，故 fixed
`a_2+gap+two-sheet orientations` 的 `A_12` 至多一个，carry随后唯一恢复
`a_3`。这是 conditional uniqueness，不能自行消除未固定的 `a_2/gap` 联合族。

<a id="dd-09-detail-src-0143-137-4"></a>
#### 机械核对与下一目标

对应 algebra / prime-power / conditional-uniqueness 核对已加入

证书命令与覆盖见 [统一核对目录](CHECKS.md)。

计算只核对字典、full-word equivalence、unit-coefficient depth以及计数修复的
bookkeeping，不承担无界 coverage。下一需要解决的具体对象仍是满足真实
digit intervals的 **joint ordinary gap/suffix/orientation family**；反复对
`(Two-sheet-full-prefix)` 与 raw sphere line作 resultant只会消去同源参数。

<a id="dd-09-detail-src-0143-137-5"></a>
#### denominator-only norm 的实际 selected-sheet 投影

**严格状态：已严格完成（局部 exact projection / 非独立 payer 审计）。**
[`global-framework.md §10.2`](#c06)
从 original full-word plane 与 sphere 得到 denominator-only Gaussian norm。
这里记录其真实 chosen-sheet 接口，不能将一个 norm 条件自动视作第二个
全 `V` orientation endpoint。

写 `n=n_3,m=m_3,d=n-m`，并定义原 decimal coefficients

```math
t_1=b_1 10^{n_2+n},\qquad t_2=b_2 10^n,\qquad t_3=b_3,
\qquad D=Q10^m+b_3.
```

令 `s=H+y_3>0`，则该 Gaussian integer 为

```math
G_{\rm dec}=(D+t_3)(y_1+i y_2)-(t_1+i t_2)s,
\qquad N(G_{\rm dec})=\Delta_{\rm dec}s^2,
\quad \Delta_{\rm dec}=\sum_jt_j^2-D^2.
\tag{Decimal-norm-carrier}
```

它同时是 [core.md §51](#c09) denominator-only circle 的整系数表达；
其中 sphere 与 original coefficient plane 仍是同两个 parents。其 inert-prime
norm obstruction 是有效必要条件，但并未产生一份新的 Archimedean height
预算，尤其不能重新收费 §§1--3 的 sphere-paid depths。

对 `p^h||v_2`，使用
[`pair-max scale quotient`](RESEARCH.md#dd-orientation)（原始记录 SRC-0141）
的 exact low-baseline `r_p=v_p(q_src)`；令

```math
\ell_2=\prod_{p^h\Vert v_2}p^{r_p},\qquad
b_j^{(2)}=b_j/\ell_2,
\qquad (t_j^{(2)},D^{(2)},G_{\rm dec}^{(2)})
=(t_j,D,G_{\rm dec})/\ell_2.
\tag{Decimal-second-sheet-strip}
```

这是保留原 decimal weights 的 integer scale quotient，ghost coordinates
`H,y_j` 不变。每个 target prime 上

```math
v_p(b_1^{(2)})=0,\qquad
v_p(b_2^{(2)})=v_p(b_3^{(2)})=h,
\quad p^h\mid H,y_1,\quad p\nmid y_2y_3.
```

若 selected `pi^h` 属于 `Pi_2`，则 `pi^{2h}|y_2+i y_3`。所以
`iy_2=y_3 mod pi^{2h}`；在 conjugate sheet 上则
`iy_2=-y_3 mod bar(pi)^{2h}`。代入 `(Decimal-norm-carrier)` 得到

```math
\boxed{G_{\rm dec}^{(2)}\equiv(D^{(2)}-t_1^{(2)})y_3\pmod{\pi^h},}
\quad
\boxed{G_{\rm dec}^{(2)}\equiv-(D^{(2)}+t_1^{(2)})y_3\pmod{\bar\pi^h}.}
\tag{Decimal-second-sheet-projection}
```

令 `k_{12}=n_2+n-m_2-m=s_2+d>0`。因

```math
D^{(2)}\equiv b_1^{(2)}10^{m_2+m}\pmod{p^h},\qquad
t_1^{(2)}=b_1^{(2)}10^{m_2+m}10^{k_{12}},
```

且 `b_1^(2),10,y_3` 均为 p-units，上两式具有 **exact truncated depths**

```math
\boxed{\min\{v_\pi(G_{\rm dec}^{(2)}),h\}
=\min\{v_p(10^{k_{12}}-1),h\},}
\quad
\boxed{\min\{v_{\bar\pi}(G_{\rm dec}^{(2)}),h\}
=\min\{v_p(10^{k_{12}}+1),h\}.}
\tag{Decimal-second-sheet-depths}
```

第一 channel 同理，但应明确剥离的是其自己的 low baseline。对
`p^h||v_1`，pair-max factorization 给

```math
v_p(b_1)=v_p(b_3)=r_p+h,\qquad v_p(b_2)=r_p.
```

令 `ell_1=prod_{p^h||v_1}p^{r_p}` 并定义相同的 `(1)` quotient。这时
`p^h|H,y_2,t_1^(1),t_3^(1)`，且 `b_2^(1),y_1,y_3` 为 p-units。
chosen `pi^{2h}|y_1+i y_3` 于是给

```math
\boxed{G_{\rm dec}^{(1)}\equiv-i(D^{(1)}+t_2^{(1)})y_3\pmod{\pi^h},}
\quad
\boxed{G_{\rm dec}^{(1)}\equiv i(D^{(1)}-t_2^{(1)})y_3\pmod{\bar\pi^h}.}
\tag{Decimal-first-sheet-projection}
```

使用 `D^(1)=b_2^(1)10^m mod p^h` 与
`t_2^(1)=b_2^(1)10^m10^d`，得到

```math
\boxed{\min\{v_\pi(G_{\rm dec}^{(1)}),h\}
=\min\{v_p(10^d+1),h\},}
\quad
\boxed{\min\{v_{\bar\pi}(G_{\rm dec}^{(1)}),h\}
=\min\{v_p(10^d-1),h\}.}
\tag{Decimal-first-sheet-depths}
```

这些 formulas 的实际含义是：若 `p∤10^{2k_12}-1`（第二 channel）或
`p∤10^{2d}-1`（第一 channel），则该 carrier 在两 Gaussian sheets 上都为
units。只有明确 decimal cyclotomic kernels 的 overlap 才产生 chosen-sheet
divisibility；它没有自动提供 `Pi_1` 或 `Pi_2` 的全模数第二 endpoint。
深于 `h` 的 valuation 也不由这些 congruences决定，不能延伸声称更深
Gaussian contact。

对应脚本核对 norm identity、两 sheets 的符号与截断深度。当前已关闭的
是“直接把此 norm carrier 当作全 `V` independent orientation payer”这条
推理路线；普通 small-gap 的 joint family 仍未排除。

<a id="dd-09-detail-src-0143-137-6"></a>
#### `U/Z` 上已有 inert source primes 不再提供 odd-valuation 排除

**严格状态：已严格完成（局部 no-go；不新增空性）。** 在同一 canonical
chart，设 `p=3 mod4` 且 `p|UZ`。由 `(UVZ,10)=1` 与 phase式，
`U,V,Z` 两两互素。写 `t=v_p(q_src)`；`B,F` 为 p-units，并且

```math
\Sigma=2FU+V\equiv
\begin{cases}V&p\mid U,\\FU&p\mid Z\end{cases}\pmod p
```

为 unit。所以原 full denominator `D=Bq_src Sigma` 与 `b_3=BVq_src`
满足 `v_p(D)=v_p(b_3)=t`。

对一个真实 reduced Exact-Lift candidate，必有

```math
\boxed{v_p(b_1),v_p(b_2)\le t.}
\tag{Inert-source-prefix-depth-cap}
```

否则最大 denominator depth `M>t` 只在一个或两个 prefix blocks中取得。
Reducedness使这些主导 rational coordinates 的 p-adic units 非零；一个
平方不能相消，而两个平方在 `p=3 mod4` 下也不能相消。故 sphere
的平方和赋值为 `-2M`，平方根赋值为 `-M`。原 word ratio `A_word/D`
却具有赋值至少 `-t`，矛盾。这里使用了原 full word，是已被 candidate
满足的必要条件，不是一份新 modulus。

令 `r=min(v_p(b_1),v_p(b_2))<=t`。两十进制 weights为 p-units，
inert二平方和律给

```math
v_p(t_1^2+t_2^2)=2r.
```

另一方面 `(Canonical-decimal-norm-expansion)` 的 negative term有

```math
v_p(D^2-b_3^2)=2t+v_p(UZ)>2r.
```

因此没有最低层相消，严格得到

```math
\boxed{v_p(\Delta_{\rm dec})=2r\quad(p=3\bmod4,\ p\mid UZ).}
\tag{Inert-source-decimal-norm-even-depth}
```

所以在真实 source/word parents 已满足后，`U` 或 `Z` 上这些 inert
primes 对 denominator norm 的 even-valuation条件是自动满足的。
不能因为 `U=3 mod4` 必携带 inert prime，就据此再次推断 norm 矛盾。
下一可攻击的 norm primes应来自 `p∤UZ` 的外部 odd-valuation，或
§7.5 中明确的 decimal-kernel overlap；是否能聚合成 height 或定位矛盾
仍待证明。这个结论不影响二进 odd-unit reader的 `Z=1 mod4` 限制。

---


来源：`SRC-0143:137–519`。原文保全，当前论证以本节为准。

<a id="dd-10"></a>
### DD-10　canonical Z=3 mod4 的无界序列排除

**状态：已严格完成。** 同一 corrected canonical delta≤1/2 neighborhood；不排 finite exceptions。

依赖：[DD-06](#dd-06)、[C05](#c05)

核对：正文推导；本次重写未为此项另增枚举。

<a id="dd-10-detail-src-0158-11-1"></a>
#### 记号

令

```math
a:=\log_{10}2,
\qquad b:=1-a,
\qquad
\lambda:=\frac{2+a}{1+2a},
```

```math
c_*:=2+3\lambda,
\qquad
\delta:=c_*-\frac nS.
```

quantitative defect inequality 中需要的 coefficients 为

```math
c_{Q_2}=2a\lambda,
```

```math
c_{G_5}=\frac{2b(2\lambda-1)}3,
\qquad
c_R=2\lambda-1.
```

又

```math
2\lambda-1=\frac3{1+2a}.
\tag{1.1}
```

`dd-corrected-terminal-digit-polarization-2026-08-22.md` 允许交换前两 prefix labels，使长 denominator 为第二块，并给

```math
m_1,n_2\le\kappa_{\rm dig}\delta S+o(S),
```

```math
m_2,n_1\ge(1-\kappa_{\rm dig}\delta)S-o(S),
```

其中

```math
\boxed{
\kappa_{\rm dig}
=\frac{2+a}{3}
=0.767009998554660\ldots.
}
\tag{1.2}
```

<a id="dd-10-detail-src-0158-11-2"></a>
#### long denominator 的 2-depth 等于 `v_2(Q)`

prefix concat 为

```math
\boxed{Q=b_1 10^{m_2}+b_2.}
\tag{2.1}
```

记

```math
\mathfrak q:=v_2(Q),
\qquad
Q_2:=\mathfrak q/S.
```

quantitative defect给

```math
Q_2\le\frac{\delta}{2a\lambda}+o(1).
\tag{2.2}
```

另一方面

```math
v_2(b_1 10^{m_2})=v_2(b_1)+m_2\ge m_2.
```

若固定 `delta<=1/2`，则

```math
\frac{\delta}{2a\lambda}
<1-\kappa_{\rm dig}\delta
```

有统一正 margin；更一般地该比较在

```math
\delta<
\left(\kappa_{\rm dig}+\frac1{2a\lambda}\right)^{-1}
=0.519903730696\ldots
```

时成立。

所以 sufficiently large `S` 上：

```math
v_2(Q)<v_2(b_1 10^{m_2}).
```

两项 valuation 不等时和的 valuation取较小者，因此 necessarily

```math
\boxed{v_2(b_2)=v_2(Q)=\mathfrak q.}
\tag{Long-2-depth}
```

这把 long denominator 的 2-adic depth直接放回 quantitative defect ledger。

<a id="dd-10-detail-src-0158-11-3"></a>
#### `G_2` 的显式 upper

全局 notation 有

```math
G=b_1b_2.
```

令

```math
G_2:=\frac{v_2(G)}S.
```

短 denominator 满足

```math
b_1<10^{m_1},
```

所以

```math
v_2(b_1)<m_1\log_2 10=\frac{m_1}{a}.
\tag{3.1}
```

先保留 digit defect 中尚未粗化的版本。上一文件证明过程给

```math
2-\frac{s+D_s}{S}
\le
\delta+\frac{2b}{3}G_5+R+o(1).
```

而选定 `s_1=max(s_1,s_2)` 后

```math
\frac{m_1}{S}
\le
1-\frac{s_1}{S}+o(1)
=
\frac12\left(2-\frac{s+D_s}{S}\right)+o(1),
```

故

```math
\boxed{
\frac{m_1}{S}
\le
\frac\delta2+\frac b3G_5+\frac R2+o(1).
}
\tag{3.2}
```

由 `(Long-2-depth)` 与 `(3.1)`：

```math
G_2
\le
\frac1a\frac{m_1}{S}+Q_2+o(1),
```

从而

```math
G_2
\le
\frac{\delta}{2a}
+Q_2
+\frac{b}{3a}G_5
+\frac{R}{2a}
+o(1).
\tag{3.3}
```

quantitative defect 给联合 budget

```math
c_{Q_2}Q_2+c_{G_5}G_5+c_RR\le\delta+o(1).
```

对 `(3.3)` 最后三项作一次线性优化。三个 cost ratio 为

```math
\frac1{c_{Q_2}}=\frac1{2a\lambda},
```

```math
\frac{b/(3a)}{c_{G_5}}
=
\frac1{2a(2\lambda-1)},
```

```math
\frac{1/(2a)}{c_R}
=
\frac1{2a(2\lambda-1)}.
```

因为 `2lambda-1>lambda`，最大者为第一项。因此

```math
\boxed{
G_2
\le
\left(\frac1{2a}+\frac1{2a\lambda}\right)\delta+o(1).
}
\tag{G2-window}
```

即

```math
\boxed{
G_2
\le
\frac{3(1+a)}{2a(2+a)}\,\delta+o(1)
=2.817387063422592\ldots\,\delta+o(1).
}
\tag{3.4}
```

所以 corrected equality 中隐含的 `G_2->0` 现在也获得显式线性 stability。

<a id="dd-10-detail-src-0158-11-4"></a>
#### `U` 的显式 window

canonical S-unit phase为

```math
\kappa=2\gamma5^TU,
\qquad
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0,
```

且 decimal pinning给

```math
\log_{10}\kappa=2S+O(1).
```

因此

```math
\frac{\log_{10}U}{S}
=2-aG_2-bG_5-R-b\frac TS+o(1).
\tag{4.1}
```

又

```math
\frac TS=\frac{2M+2Q_5-2G_5+N_5}{3}.
```

所以

```math
\frac{\log_{10}U}{S}
=2-\frac{2b}{3}M
-aG_2
-\frac{2b}{3}Q_5
-\frac b3G_5
-\frac b3N_5
-R+o(1).
\tag{4.2}
```

令

```math
M_*:=2.808883577618031\ldots,
```

```math
\boxed{
U_*:=2-\frac{2b}{3}M_*
=0.691116422381969\ldots.
}
\tag{4.3}
```

并写

```math
\mu:=M_*-M,
\qquad 0\le\mu\le\delta+o(1).
```

则

```math
\frac{\log U}{S}-U_*
=
\frac{2b}{3}\mu
-aG_2
-\frac{2b}{3}Q_5
-\frac b3G_5
-\frac b3N_5
-R+o(1).
\tag{4.4}
```

<a id="dd-10-detail-src-0158-11-5"></a>
#### upper

丢掉全部负项：

```math
\boxed{
\frac{\log U}{S}
\le
U_*+\frac{2b}{3}\delta+o(1).
}
\tag{U-upper}
```

数值 coefficient为

```math
\frac{2b}{3}=0.465980002890679\ldots.
```

<a id="dd-10-detail-src-0158-11-6"></a>
#### lower

使用 `(3.3)` 而非先使用粗 `(3.4)`：

```math
aG_2
\le
\frac\delta2
+aQ_2+\frac b3G_5+\frac R2+o(1).
```

于是 `(4.4)` 中全部负项至多为

```math
\frac\delta2
+aQ_2
+\frac{2b}{3}Q_5
+\frac{2b}{3}G_5
+\frac b3N_5
+\frac{3R}{2}
+o(1).
```

这些 variables 共用同一 quantitative-defect budget。对应 cost ratio最大值为

```math
\frac{3/2}{c_R}
=
\frac{3}{2(2\lambda-1)}
=\frac{1+2a}{2}.
```

所以

```math
\boxed{
\frac{\log U}{S}
\ge
U_*-\left[\frac12+\frac{1+2a}{2}\right]\delta-o(1).
}
```

即

```math
\boxed{
U_*-(1+a)\delta-o(1)
\le
\frac{\log_{10}U}{S}
\le
U_*+\frac{2b}{3}\delta+o(1).
}
\tag{U-window}
```

数值为

```math
\boxed{
U_*-1.301029995663981\,\delta-o(1)
\le
\frac{\log_{10}U}{S}
\le
U_*+0.465980002890679\,\delta+o(1).
}
```

<a id="dd-10-detail-src-0158-11-7"></a>
#### `Z` 的显式 window

第二条 S-unit phase为

```math
\kappa+2G=2\gamma2^HZ,
```

且

```math
\log_{10}(\kappa+2G)=2S+O(1).
```

2-resonance给

```math
\frac HS=2M+2Q_2+N_2-2G_2+o(1).
```

因此

```math
\begin{aligned}
\frac{\log_{10}Z}{S}
&=2-aG_2-bG_5-R-a\frac HS+o(1)\\
&=2-2aM-2aQ_2-aN_2+aG_2-bG_5-R+o(1).
\end{aligned}
\tag{5.1}
```

令

```math
\boxed{
Z_*:=2-2aM_*
=0.308883577618031\ldots.
}
\tag{5.2}
```

于是

```math
\frac{\log Z}{S}-Z_*
=2a\mu-2aQ_2-aN_2+aG_2-bG_5-R+o(1).
\tag{5.3}
```

<a id="dd-10-detail-src-0158-11-8"></a>
#### lower

丢掉正项 `2a mu+aG_2`，其余负项共用 defect budget。最大 cost ratio为

```math
\frac{b}{c_{G_5}}
=\frac{1+2a}{2}.
```

所以

```math
\boxed{
\frac{\log Z}{S}
\ge
Z_*-
rac{1+2a}{2}\delta-o(1).
}
\tag{Z-lower}
```

即 coefficient

```math
\frac{1+2a}{2}=0.801029995663981\ldots.
```

<a id="dd-10-detail-src-0158-11-9"></a>
#### upper

由 `(3.3)`：

```math
aG_2
\le
\frac\delta2+aQ_2+\frac b3G_5+\frac R2+o(1).
```

代入 `(5.3)` 并丢掉所有负项，可得

```math
\frac{\log Z}{S}-Z_*
\le
2a\delta+\frac\delta2
+aQ_2+\frac b3G_5+\frac R2+o(1).
```

后三项共用 defect budget，最大 cost ratio为

```math
\frac{a}{c_{Q_2}}=\frac1{2\lambda}.
```

因此

```math
\boxed{
\frac{\log Z}{S}
\le
Z_*+\left(2a+\frac12+\frac1{2\lambda}\right)\delta+o(1).
}
\tag{Z-upper}
```

数值 coefficient为

```math
2a+\frac12+\frac1{2\lambda}
=1.450178006813822\ldots.
```

综上

```math
\boxed{
Z_*-0.801029995663981\,\delta-o(1)
\le
\frac{\log_{10}Z}{S}
\le
Z_*+1.450178006813822\,\delta+o(1).
}
\tag{Z-window}
```


<a id="dd-10-detail-src-0158-574-1"></a>
#### original decimal norm 排除 `Z=3 mod4` 的无界 terminal state

**严格状态：已严格完成（exact finite criterion；共享预算下非有效 eventual
exclusion）。** 这条结果读取原 full-word coefficient plane 的二进 odd
unit；此前 `H` 的 resonance 只读取 depth。它不增加独立 height payer，
也不依赖任何 numerator-count 结论。以下在本文 corrected canonical
`t_2=1` chart 中使用原位数 `n=n_3,m=m_3`。

令 `F=5^T`，canonical source 为 `q_src`，且

```math
Q=Uq_{\rm src},\qquad B=\frac{10^m}{2F},\qquad
b_3=BVq_{\rm src},\qquad FU+V=2^HZ.
```

`U,V,Z` 均奇。设整数 depths

```math
\mathfrak q=v_2(Q)=v_2(q_{\rm src}),\qquad
r_1=v_2(b_1),\qquad e_N=v_2(\mathcal N_{12}).
```

这里 `e_N` 不是第二 numerator 的长度 `n_2`；其归一化是本文的
`N_2=e_N/S`。在 `Long-2-depth` 成立时，`v_2(b_2)=mathfrak q`，所以
`mathfrak g=r_1+mathfrak q`。引用 `high-funnel-ledger.md` 的 exact
2-resonance（Schmidt-dual 章节式 (6.3)）：

```math
\boxed{H=2m+2\mathfrak q+e_N-2\mathfrak g-4
=2m+e_N-2r_1-4.}
\tag{Canonical-H-exact-depth}
```

原 decimal weights 为 `t_1=b_1 10^(n_2+n)`、`t_2=b_2 10^n`、
`t_3=b_3` 与 `D=Q10^m+b_3=Bq_src(2FU+V)`。因此

```math
\boxed{
\Delta_{\rm dec}=t_1^2+t_2^2
-4B^2q_{\rm src}^2FU(FU+V).}
\tag{Canonical-decimal-norm-expansion}
```

最后项的 exact two-depth 为

```math
\ell=2m+2\mathfrak q+H.
```

**Exact finite criterion.** 若 `Long-2-depth`、`H>=2` 与

```math
\boxed{\min\{2n+2n_2+2r_1,\ 2n+2\mathfrak q\}\ge\ell+2}
\tag{Canonical-decimal-two-unit-criterion}
```

同时成立，则两个 positive-square terms 除以 `2^ell` 都被四整除。
写 `q_src=2^mathfrak q q_odd`，可得

```math
\boxed{v_2(\Delta_{\rm dec})=\ell,\qquad
\frac{\Delta_{\rm dec}}{2^\ell}\equiv-UZ\pmod4.}
\tag{Canonical-decimal-norm-two-unit}
```

因为 `4B^2=2^(2m)5^(2(m-T))`，其 odd factor与 `q_odd^2` 都为
`1 mod4`；`F=1 mod4`，故上面的 odd unit没有额外系数。
[`global-framework.md §10.2`](#c06)
要求 `Delta_dec` 是有理 Gaussian norm。非零 norm的二进 odd unit为
`1 mod4`，所以 `UZ=3 mod4`。另一方面所有 `V` primes均 `1 mod4`，
故 `V=1 mod4`；`H>=2` 的 phase式给 `U=-V=3 mod4`。最终

```math
\boxed{Z\equiv1\pmod4.}
\tag{Canonical-Z-mod4}
```

**整个 `delta<=1/2` neighborhood 的 eventual coverage.** 由 exact
resonance，两项 depth差分别为

```math
\begin{aligned}
L_1&=(2n+2n_2+2r_1)-\ell
=2n-4m+2n_2+4r_1-2\mathfrak q-e_N+4,\\
L_2&=(2n+2\mathfrak q)-\ell
=2n-4m+2r_1-e_N+4.
\end{aligned}
\tag{Canonical-decimal-two-depth-margins}
```

令 `alpha=log_10 2,beta=1-alpha`、`A=2(1+2alpha)/3`、
`mu=M_*-m/S`。同一份 sharp shared budget为

```math
A\mu=\sigma+2\alpha Q_2+\alpha N_2
+\frac\beta3(2Q_5+4G_5+N_5)+2R+o(1),
\qquad\sigma\ge-o(1).
```

因此 `2Q_2+N_2<=A mu/alpha+o(1)`；
`4-A/alpha>0` 严格等价于 `alpha>1/4`，由 `2^4>10` 成立。
利用 `2c_*-4M_*=2U_*`，上两 margin均满足

```math
\begin{aligned}
\frac{L_i}S
&\ge2U_*-2\delta+4\mu-2Q_2-N_2-o(1)\\
&\ge2U_*-2\delta+(4-A/\alpha)\mu-o(1)\\
&\ge2U_*-1-o(1)
=0.382232844763938\ldots-o(1)>0.
\end{aligned}
\tag{Canonical-decimal-two-depth-shared-margin}
```

故 sufficiently large `S` 上 `(Canonical-decimal-two-unit-criterion)`
成立。同时 `r_1<=m_1/alpha` 与 digit polarization给

```math
\frac HS\ge2M_*-
\left(2+\frac{2\kappa_{\rm dig}}\alpha\right)\delta-o(1)>0
\qquad(\delta\le1/2),
```

所以 `H>=2` 也 eventually 成立。由此 **不存在保持 `Z=3 mod4`、
`delta<=1/2` 的 corrected canonical unbounded sequence**。
Exact criterion 可逐个排除有限 candidate；渐近证明本身没有 effective
`S` cutoff，不能宣称已经排除所有 finite exceptions。`Z=1 mod4` 的
ordinary small-gap family、其 joint chosen-sheet compatibility 与 DD
global emptiness 仍未解决。

计算核对在现有
`research-checks/tail/check_dd_corrected_numerator_collapse_sharp.py`
检查 expansion、exact normalized unit、共享 margin cancellation，以及
明写 bounded canonical-denominator local models。计算不承担无界覆盖。


来源：`SRC-0158:11–552`；`SRC-0158:574–708`。原文保全，当前论证以本节为准。

<a id="a1"></a>
## A1 分支

<a id="a1-01"></a>
### A1-01　原 rational contact 与 universal denominator funnel

**状态：已严格完成。** A1 chamber；固定前缀和固定 g 的尾问题，不能合并为全局有限。

依赖：[C01](#c01)、[C02](#c02)

核对：正文推导；本次重写未为此项另增枚举。

<a id="a1-01-detail-src-0055-31-1"></a>
#### A1 位数参数的精确消元（已严格完成）

A1 条件为

```math
s_3\le 0,\qquad s_2+s_3>0.
```

记

```math
g=-s_3\ge 0,\qquad k=s_2+s_3\ge 1.
```

则

```math
\boxed{s_2=k+g}.
```

另一方面旧稿定义的有效第三尾长为

```math
\ell=m_3-g.
```

但 A1 中

```math
n_3=m_3+s_3=m_3-g,
```

所以实际上有精确恒等式

```math
\boxed{\ell=n_3}.
```

因此

```math
\boxed{m_3=g+n_3},
\qquad
\boxed{k=s_2-g=n_2-m_2-g}.
```

特别地

```math
\boxed{0\le g\le s_2-1=n_2-m_2-1}.
```

这说明：对固定前两块数据，`g` 从一开始就是有限的；A1 中真正可能随着第三块增长的是 `n_3=\ell`。

这不是全局有限性结论，因为前两块本身仍可变化。

---

<a id="a1-01-detail-src-0055-31-2"></a>
#### carrier 给出的第二个 `g` 上界（已严格完成）

A1 中

```math
\Lambda_2=10^{-g}\le 1,
```

故

```math
\Lambda_2r_2<R,
\qquad
r_3<R.
```

正权平均要等于 `R`，第一坐标必须严格承担 carrier：

```math
\boxed{10^k r_1>R>r_2}.
```

于是

```math
r_2<10^k r_1.
```

利用位数粗界

```math
10^{s_i-1}<r_i<10^{s_i+1}
```

得到

```math
10^{k+g-1}<r_2<10^k r_1<10^{k+s_1+1},
```

从而

```math
\boxed{g\le s_1+1}.
```

所以 A1 必须满足

```math
\boxed{s_1\ge -1}.
```

若 `n_1\le m_1-2`，A1 立即为空。

还有更精确的 carrier 必要条件：

```math
10^{2k}r_1^2>R^2>r_1^2+r_2^2,
```

故

```math
\boxed{
\frac{r_2}{10^k r_1}
<\sqrt{1-10^{-2k}}.
}
```

这是一个完全由前两块决定的薄环筛选条件。

---

<a id="a1-01-detail-src-0055-31-3"></a>
#### 前两块压成单一 rational contact 参数（已严格完成）

定义前两分母拼接

```math
\boxed{Q=b_1 10^{m_2}+b_2}
```

以及前两分子拼接

```math
\boxed{C=a_1 10^{n_2}+a_2}.
```

旧 A1 coefficient 中

```math
10^{g+k+m_2}a_1+a_2
```

由于 `g+k=s_2=n_2-m_2`，恰好就是上面的 `C`。因此 A1 的 numerator coefficient 与 `g` 无关。

再记

```math
\boxed{D=10^gQ},
\qquad
\boxed{P=\frac CD}.
```

因为 `\ell=n_3`，原始三块拼接可精确写成

```math
\boxed{\alpha=10^{\ell}C+a_3},
```

```math
\boxed{\beta=10^{\ell}D+b_3}.
```

令

```math
r=r_3=\frac{a_3}{b_3},
\qquad
\boxed{\theta=\frac{b_3}{10^{\ell}D}}
=\frac{b_3}{10^{m_3}Q}.
```

由于 `b_3` 恰有 `m_3` 位，

```math
\boxed{
\frac1{10Q}\le\theta<\frac1Q.
}
```

于是 exact lift 的拼接比严格化成

```math
\boxed{
R=\frac{P+\theta r}{1+\theta}.
}
```

换言之，整个 A1 是前两块 rational number `P` 与第三分数 `r_3` 的一次严格 mediant/contact。

因为 `R>r_3`，上式立刻给出

```math
\boxed{P>R>r_3}.
```

并且

```math
\boxed{
\frac{P-R}{R-r_3}=\theta
\in\left[\frac1{10Q},\frac1Q\right).
}
```

这条比例关系是后续 A1 的主几何坐标。

---

<a id="a1-01-detail-src-0055-31-4"></a>
#### A1 universal rational-contact quadratic（已严格完成）

定义前两平方和

```math
\boxed{S=r_1^2+r_2^2}.
```

球面条件为

```math
R^2=S+r^2.
```

把

```math
R=\frac{P+\theta r}{1+\theta}
```

代入并清理，得到关于 `r=r_3` 的二次式

```math
\boxed{
(1+2\theta)r^2
-2\theta P r
+(1+\theta)^2S-P^2
=0.
}
```

其判别式为

```math
\boxed{
\Delta_r
=4(1+\theta)^2
\left(P^2-(1+2\theta)S\right).
}
```

由于 `r_3` 是有理数，必要条件是

```math
\boxed{
\Xi:=P^2-(1+2\theta)S
\text{ 是非负有理平方}.
}
```

这是 A1 的统一判别平方；它直接来自原始拼接和球面，不使用第三块 Gaussian 正规化。

特别地，由

```math
\theta\ge\frac1{10Q}
```

得到纯前缀必要条件

```math
\boxed{
P^2\ge
\left(1+\frac1{5Q}\right)S.
}
```

即

```math
\boxed{
\left(\frac{C}{10^gQ}\right)^2
\ge
\left(1+\frac1{5Q}\right)
(r_1^2+r_2^2).
}
```

因此 `g` 还满足一个纯前缀上界：若右侧比值小于 1，则该 `g` 直接排除；等价地

```math
\boxed{
10^{2g}
\le
\frac{C^2}{Q^2S(1+1/(5Q))}.
}
```

由于每增加 `g` 一次，`P^2` 精确缩小 `100` 倍，这个筛选对 A1 很强。

若 `\Xi=z^2`，则第三分数只能取

```math
\boxed{
 r
=
\frac{
\theta P\pm(1+\theta)z
}{1+2\theta}.
}
```

因此在固定 `(prefix,g,\theta)` 后，`r_3` 至多只有两个候选。

---

<a id="a1-01-detail-src-0055-31-5"></a>
#### saturated `L=1` 的重新参数化（已严格完成）

旧稿中 saturated 定义为

```math
L=1,
```

亦即

```math
10^{\ell}\mid b_3.
```

写成

```math
\boxed{b_3=10^{\ell}\tau}.
```

<a id="a1-01-detail-src-0055-31-6"></a>
#### `g=0` 的 saturated 支为空

若 `g=0`，则 `m_3=\ell`，而 `b_3` 是 `\ell` 位整数，所以

```math
b_3<10^{\ell}.
```

这与 `10^\ell\mid b_3` 矛盾。因此

```math
\boxed{L=1\Longrightarrow g\ge1}.
```

<a id="a1-01-detail-src-0055-31-7"></a>
#### `\tau` 恰为 `g` 位整数

当 `g\ge1` 时，由 `m_3=g+\ell` 得

```math
10^{g+\ell-1}\le b_3<10^{g+\ell}.
```

除以 `10^\ell`：

```math
\boxed{10^{g-1}\le\tau<10^g}.
```

此时

```math
\boxed{\theta=\frac\tau D},
\qquad D=10^gQ.
```

关键点是：在 saturated 支中，`\theta` 已完全脱离 `\ell`。

---

<a id="a1-01-detail-src-0055-31-8"></a>
#### saturated integer-square certificate（已严格完成）

统一判别平方变成

```math
\Xi
=
\frac{C^2}{D^2}
-
\left(1+\frac{2\tau}{D}\right)
\frac{\mathcal N_{12}}{G^2},
```

其中

```math
G=b_1b_2,
\qquad
\mathcal N_{12}=(a_1b_2)^2+(a_2b_1)^2,
\qquad
S=\frac{\mathcal N_{12}}{G^2}.
```

故

```math
\boxed{
\Xi
=
\frac{
G^2C^2-D(D+2\tau)\mathcal N_{12}
}{D^2G^2}.
}
```

若 `\Xi` 是有理平方，则存在整数 `W\ge0` 使

```math
\boxed{
W^2
=G^2C^2-D(D+2\tau)\mathcal N_{12}.
}
```

这把 saturated A1 直接压成一个整数平方条件。

记

```math
K=G^2C^2-D^2\mathcal N_{12}.
```

则等价于

```math
\boxed{
W^2=K-2D\mathcal N_{12}\tau.
}
```

因此

```math
\boxed{
\tau=\frac{K-W^2}{2D\mathcal N_{12}}.
}
```

并且 `\tau` 还必须同时落在

```math
10^{g-1}\le\tau<10^g.
```

所以 saturated 支的 `\tau` 不再是自由变量：它由一个处在明确区间、明确同余类中的整数平方 `W^2` 决定。

等价的差平方分解是

```math
\boxed{
(GC-W)(GC+W)
=D(D+2\tau)\mathcal N_{12}.
}
```

这给出一个新的 divisor-pair 入口。

---

<a id="a1-01-detail-src-0055-31-9"></a>
#### saturated 第三分母整除证书（已严格完成）

由二次根公式，在 `\Xi=(W/(DG))^2` 时，

```math
\boxed{
 r_3
=
\frac{
G\tau C\pm(D+\tau)W
}{DG(D+2\tau)}.
}
```

而 `r_3=a_3/b_3` 已经是既约分数。因此它的既约分母必须整除上式的整数分母：

```math
\boxed{
 b_3\mid DG(D+2\tau).
}
```

在 saturated 支 `b_3=10^\ell\tau`，故得到

```math
\boxed{
10^\ell\tau
\mid
10^gQ\,G\,(10^gQ+2\tau).
}
```

这是一个不使用 `a_3/\delta_3` 正规化的 denominator-only certificate。

它立即表明：固定前两块、`g` 与 `\tau` 后，`\ell` 有显式有限上界；更强地，实际 `b_3` 必须是右侧固定整数的因子。

因此 saturated A1 对固定前缀已经归约为严格有限问题：

1. `g` 落在 §§1–4 的有限集合；
2. `\tau` 是 `g` 位整数并满足 §6 的整数平方条件；
3. `b_3=10^\ell\tau` 必须整除 `DG(D+2\tau)`；
4. `r_3` 由 §7 根式唯一恢复并检查位数、正号、既约性。

再次强调：这只证明 fixed-prefix finite reduction，不推出所有前缀的并集有限。

---

<a id="a1-01-detail-src-0055-31-10"></a>
#### 对旧 `z_3=a_3/\delta_3` 正规化的审计警告


<a id="a1-01-detail-src-0055-718-1"></a>
#### 记号

沿用 A1 rational-contact 框架：

```math
T=10^\ell=10^{n_3},
\qquad
D=10^gQ,
```

```math
C=a_1 10^{n_2}+a_2,
\qquad
G=b_1b_2,
```

```math
N=\mathcal N_{12}
=(a_1b_2)^2+(a_2b_1)^2,
```

```math
P=\frac CD,
\qquad
S=\frac N{G^2},
```

以及

```math
\theta=\frac{b_3}{TD}.
```

记

```math
\boxed{K=G^2C^2-D^2N}.
```

A1 rational-contact 判别平方是

```math
\Xi=P^2-(1+2\theta)S=z^2
```

对某个 `z\in\mathbf Q_{\ge0}`。

---

<a id="a1-01-detail-src-0055-718-2"></a>
#### universal integer-square certificate

直接代入 `P,S,\theta`：

```math
\Xi
=
\frac{C^2}{D^2}
-
\left(1+\frac{2b_3}{TD}\right)\frac N{G^2}.
```

通分得到

```math
\boxed{
\Xi
=
\frac{TK-2b_3DN}{T D^2G^2}.
}
```

因此

```math
z^2
=
\frac{TK-2b_3DN}{T(DG)^2}.
```

两边乘以 `T^2D^2G^2`：

```math
(zTDG)^2
=T(TK-2b_3DN).
```

右侧是整数；有理数的平方若为整数，则该有理数本身为整数。因此存在整数 `W\ge0` 满足

```math
\boxed{
W=zTDG
}
```

以及

```math
\boxed{
W^2
=T(TK-2b_3DN)
=T^2K-2Tb_3DN.
}
```

这是覆盖整个 A1 的整数平方证书。

特别地必须有

```math
\boxed{TK-2b_3DN\ge0}.
```

因为

```math
b_3\ge10^{m_3-1}=10^{g+\ell-1}=10^{g-1}T,
```

故得到纯前缀必要条件

```math
TK
\ge
2\cdot10^{g-1}T\cdot D N,
```

即

```math
\boxed{
K\ge2\cdot10^{2g-1}QN.
}
```

这与 rational-contact 框架中的

```math
P^2\ge\left(1+\frac1{5Q}\right)S
```

完全等价。

---

<a id="a1-01-detail-src-0055-718-3"></a>
#### universal root formula

由

```math
\Xi=z^2=\left(\frac{W}{TDG}\right)^2
```

以及

```math
r_3
=
\frac{\theta P\pm(1+\theta)z}{1+2\theta}
```

代入

```math
\theta=\frac{b_3}{TD},
\qquad
P=\frac CD,
```

得到

```math
\boxed{
 r_3
=
\frac{
TG b_3 C
\pm
(TD+b_3)W
}{
TDG(TD+2b_3)
}.
}
```

原问题中

```math
r_3=\frac{a_3}{b_3}
```

已经既约，因此其既约分母 `b_3` 必须整除上述整数分母：

```math
\boxed{
 b_3\mid TDG(TD+2b_3).
}
```

展开右侧并模 `b_3` 化简：

```math
TDG(TD+2b_3)
\equiv
T^2D^2G
\pmod{b_3}.
```

于是得到更干净的 universal denominator certificate：

```math
\boxed{
 b_3\mid T^2D^2G.
}
```

由于

```math
T=10^\ell,
\qquad
D=10^gQ,
```

还可写成

```math
\boxed{
 b_3\mid10^{2m_3}Q^2G.
}
```

这里使用了 `m_3=g+\ell`。

---

<a id="a1-01-detail-src-0055-718-4"></a>
#### 第三分母的非十进制 prime supply 被前缀完全控制

令

```math
b_3=2^u5^v h,
\qquad
\gcd(h,10)=1.
```

由

```math
b_3\mid10^{2m_3}Q^2G
```

立刻得到

```math
\boxed{h\mid Q^2G}.
```

更逐素数地，对每个奇素数 `p\ne5`，

```math
\boxed{
 v_p(b_3)
\le
2v_p(Q)+v_p(G).
}
```

所以 A1 中第三分母的所有非 `2,5` 素数以及其指数，都由前两块的

```math
Q^2G
```

控制。

这比“固定前缀下第三分母只有有限新奇素数”更具体：第三分母一定处在

```math
\boxed{
 b_3=h2^u5^v,
\qquad
h\mid Q^2G,
\quad\gcd(h,10)=1
}
```

这一 near-`S`-unit funnel 中。

固定前缀后 `h` 只有有限多个选择；所有无界性只能来自 `2`、`5` 指数 `u,v`。

---

<a id="a1-01-detail-src-0055-718-5"></a>
#### 2/5-adic parity split

整数平方证书

```math
W^2=T(TK-2b_3DN)
```

对 `p\in\{2,5\}` 给出直接的赋值奇偶约束。

记

```math
e_p=v_p(TK)=\ell+v_p(K).
```

再记

```math
f_2=v_2(2b_3DN)
=1+u+g+v_2(Q)+v_2(N),
```

```math
f_5=v_5(2b_3DN)
=v+g+v_5(Q)+v_5(N).
```

若 `e_p\ne f_p`，则

```math
v_p(TK-2b_3DN)=\min(e_p,f_p).
```

由于 `W^2` 的 `p`-进赋值必须为偶数，得到

```math
\boxed{
\ell+\min(e_p,f_p)\equiv0\pmod2
\qquad(e_p\ne f_p).
}
```

展开可分成：

<a id="a1-01-detail-src-0055-718-6"></a>
#### `p=5`

若

```math
\ell+v_5(K)
<
v+g+v_5(Q)+v_5(N),
```

则必须

```math
\boxed{v_5(K)\equiv0\pmod2}.
```

若反向严格不等式成立，则必须

```math
\boxed{
\ell+v+g+v_5(Q)+v_5(N)
\equiv0\pmod2.
}
```

相等时进入五进 resonance：

```math
\boxed{
\ell+v_5(K)
=v+g+v_5(Q)+v_5(N).
}
```

<a id="a1-01-detail-src-0055-718-7"></a>
#### `p=2`

若

```math
\ell+v_2(K)
<
1+u+g+v_2(Q)+v_2(N),
```

则必须

```math
\boxed{v_2(K)\equiv0\pmod2}.
```

若反向严格不等式成立，则必须

```math
\boxed{
\ell+1+u+g+v_2(Q)+v_2(N)
\equiv0\pmod2.
}
```

相等时进入二进 resonance：

```math
\boxed{
\ell+v_2(K)
=1+u+g+v_2(Q)+v_2(N).
}
```

因此整个 A1 的 2/5 无界尾部自然分成四类：

1. 二进非 resonance、五进非 resonance；
2. 仅二进 resonance；
3. 仅五进 resonance；
4. 双 resonance。

这给出了一个与 DD 分支类似、但由 A1 自身 rational-contact 方程直接产生的赋值分层。

---

<a id="a1-01-detail-src-0055-718-8"></a>
#### saturated 支作为 universal funnel 的特例

若 `L=1`，则

```math
b_3=T\tau.
```

代入 universal square certificate：

```math
W^2
=T^2(K-2\tau DN).
```

所以 `T\mid W`。写

```math
W=T W_0,
```

得到

```math
\boxed{
W_0^2
=K-2\tau DN
=G^2C^2-D(D+2\tau)N,
}
```

恰好恢复 `rational-contact.md` 中 saturated integer-square certificate。

同理 universal denominator certificate 给出

```math
T\tau\mid T^2D^2G.
```

而 saturated 专用根公式还能给出更锋利的

```math
T\tau\mid DG(D+2\tau).
```

所以两个新框架彼此一致。

---


<a id="a1-01-detail-src-0055-1240-1"></a>
#### 统一偏移坐标

由 denominator funnel，写

```math
\boxed{b_3=h2^u5^v},
\qquad
\gcd(h,10)=1,
\qquad
h\mid Q^2G.
```

同时

```math
T=10^\ell=2^\ell5^\ell,
\qquad
m_3=g+\ell.
```

定义两个尾赋值偏移

```math
\boxed{x=u-\ell},
\qquad
\boxed{y=v-\ell}.
```

于是

```math
\boxed{
\frac{b_3}{T}=h2^x5^y.
}
```

而 `b_3` 恰有 `m_3=g+\ell` 位，因此

```math
10^{g+\ell-1}\le b_3<10^{g+\ell}.
```

除以 `T=10^\ell`，得到整个 A1 的统一 decade window：

```math
\boxed{
10^{g-1}
\le h2^x5^y
<10^g.
}
\tag{1}
```

这是后面把 resonance 从一条无限直线压成有限整数点的关键。

---

<a id="a1-01-detail-src-0055-1240-2"></a>
#### 二进 resonance 精确锁定 `x`

沿用 denominator funnel 的记号

```math
K=G^2C^2-D^2N,
\qquad
D=10^gQ.
```

二进 resonance 条件为

```math
\ell+v_2(K)
=
1+u+g+v_2(Q)+v_2(N).
```

代入 `u=\ell+x`，消去 `\ell`：

```math
\boxed{
x=x_2^*}
```

其中

```math
\boxed{
 x_2^*
=
v_2(K)-1-g-v_2(Q)-v_2(N).
}
\tag{2}
```

所以二进 resonance 不只是控制赋值的增长率，而是把 `u-\ell` 精确固定成前缀常数。

把 (2) 代回 decade window (1)：

```math
10^{g-1}
\le h2^{x_2^*}5^y
<10^g.
```

取对数可得

```math
\frac{(g-1)\log10-\log h-x_2^*\log2}{\log5}
\le y
<
\frac{g\log10-\log h-x_2^*\log2}{\log5}.
```

这个实区间的长度恰为

```math
\frac{\log10}{\log5}
=1+\frac{\log2}{\log5}
<2.
```

因此：

```math
\boxed{
\text{固定前缀与 }h\text{ 后，二进 resonance 至多留下两个整数 }y.
}
\tag{3}
```

---

<a id="a1-01-detail-src-0055-1240-3"></a>
#### 五进 resonance 精确锁定 `y`

五进 resonance 条件为

```math
\ell+v_5(K)
=
v+g+v_5(Q)+v_5(N).
```

代入 `v=\ell+y`，消去 `\ell`：

```math
\boxed{y=y_5^*}
```

其中

```math
\boxed{
 y_5^*
=
v_5(K)-g-v_5(Q)-v_5(N).
}
\tag{4}
```

代回 decade window：

```math
10^{g-1}
\le h2^x5^{y_5^*}
<10^g.
```

于是

```math
\frac{(g-1)\log10-\log h-y_5^*\log5}{\log2}
\le x
<
\frac{g\log10-\log h-y_5^*\log5}{\log2}.
```

区间长度为

```math
\frac{\log10}{\log2}
=1+\frac{\log5}{\log2}
<4.
```

因此：

```math
\boxed{
\text{固定前缀与 }h\text{ 后，五进 resonance 至多留下四个整数 }x.
}
\tag{5}
```

---

<a id="a1-01-detail-src-0055-1240-4"></a>
#### 双 resonance 更强：偏移唯一

若二进、五进同时 resonance，则

```math
\boxed{(x,y)=(x_2^*,y_5^*)}
```

完全由前缀唯一确定。

此时只需检查一次 decade window

```math
10^{g-1}
\le h2^{x_2^*}5^{y_5^*}<10^g.
```

若不成立，整个双 resonance 状态立即为空。

若成立，定义

```math
\boxed{\rho=h2^{x_2^*}5^{y_5^*}}.
```

则

```math
\boxed{b_3=T\rho}.
```

尽管 `\rho` 未必是整数，它是一个由前缀唯一确定的正有理数。

---

<a id="a1-01-detail-src-0055-1240-5"></a>
#### 任意单 resonance 都把 `b_3/T` 压成有限集合

二进 resonance 时，由 §2，`x=x_2^*`，而 `y` 至多两个可能值；因此

```math
\boxed{
\rho:=\frac{b_3}{T}=h2^x5^y
}
```

只可能落在一个至多两元素集合中。

五进 resonance 时同理，`y=y_5^*`，`x` 至多四个可能值，因此 `\rho` 至多有四个值。

双 resonance 则至多一个值。

所以：

```math
\boxed{
\text{任意至少含一个 resonance 的 A1 状态，固定前缀与 }h\text{ 后，}
\rho=b_3/T\text{ 只有有限多个值。}
}
\tag{6}
```

注意这一步没有使用任何有限枚举；有限性直接来自 resonance 等式和十进制位数窗。

---

<a id="a1-01-detail-src-0055-1240-6"></a>
#### 固定 `\rho` 后 `r_3` 也被固定

A1 rational-contact 参数为

```math
\theta=\frac{b_3}{TD}.
```

若

```math
b_3=T\rho,
```

则

```math
\boxed{\theta=\frac\rho D}
```

与 `\ell` 无关。

而前缀 `P=C/D`、`S=N/G^2` 也均固定。故判别平方

```math
P^2-(1+2\theta)S=z^2
```

若成立，则二次根公式给出的

```math
 r_3
=
\frac{\theta P\pm(1+\theta)z}{1+2\theta}
```

也是固定有理数，至多两个符号候选。

写其既约形式为

```math
\boxed{r_3=\frac pq},
\qquad
\gcd(p,q)=1.
```

原问题本身规定 `r_3=a_3/b_3` 已经既约，因此必须有

```math
\boxed{b_3=q}.
\tag{7}
```

但另一方面

```math
b_3=T\rho=10^\ell\rho.
```

把 `\rho=A/B` 写成既约正有理数，(7) 变成

```math
10^\ell\frac AB=q.
```

所以

```math
\boxed{
10^\ell=\frac{qB}{A}.
}
\tag{8}
```

右端是固定有理数。

因此每个固定 `(prefix,h,\rho,\pm)` 状态至多存在一个 `\ell`，并且只有当右端恰为十的非负整数幂时才可能存在。

于是得到本文核心结论：

```math
\boxed{
\text{A1 中所有至少含一个 }2/5\text{ resonance 的尾部，固定前缀后均无无界 }\ell\text{ 族。}
}
\tag{9}
```

这比“固定前缀有限”更精确：对每一个 resonance offset 状态与根号符号，`\ell` 至多一个。

---


<a id="a1-01-detail-src-0055-1668-1"></a>
#### 固定阈值坐标

沿用

```math
x=u-\ell,
\qquad
y=v-\ell,
```

以及 decade window

```math
\boxed{
10^{g-1}\le h2^x5^y<10^g.
}
\tag{1}
```

二进 resonance 阈值为

```math
\boxed{
 x_*=v_2(K)-1-g-v_2(Q)-v_2(N),
}
\tag{2}
```

五进 resonance 阈值为

```math
\boxed{
 y_*=v_5(K)-g-v_5(Q)-v_5(N).
}
\tag{3}
```

在 denominator square

```math
W^2=T(TK-2b_3DN)
```

中，二进两项的赋值分别为

```math
e_2=\ell+v_2(K),
```

```math
f_2=1+u+g+v_2(Q)+v_2(N).
```

代入 `u=\ell+x`，得到

```math
f_2-e_2=x-x_*.
```

因此

```math
\boxed{
\begin{aligned}
x>x_*&\iff e_2<f_2,\\
x=x_*&\iff e_2=f_2,\\
x<x_*&\iff e_2>f_2.
\end{aligned}
}
\tag{4}
```

完全不再含 `\ell`。

同理五进有

```math
e_5=\ell+v_5(K),
```

```math
f_5=v+g+v_5(Q)+v_5(N),
```

且

```math
f_5-e_5=y-y_*.
```

所以

```math
\boxed{
\begin{aligned}
y>y_*&\iff e_5<f_5,\\
y=y_*&\iff e_5=f_5,\\
y<y_*&\iff e_5>f_5.
\end{aligned}
}
\tag{5}
```

这说明 A1 的 2/5-adic 位置图在 `(x,y)` 平面中就是两条固定直线

```math
x=x_*,
\qquad y=y_*.
```

---

<a id="a1-01-detail-src-0055-1668-2"></a>
#### `++` 象限固定前缀下有限

考虑

```math
 x>x_* ,
\qquad y>y_*.
```

因为 `x,y` 为整数，

```math
x\ge x_*+1,
\qquad y\ge y_*+1.
```

另一方面 decade window 上界给出

```math
h2^x5^y<10^g.
```

固定 `h,g,x_*,y_*` 后，若固定 `y\ge y_*+1`，则

```math
2^x<\frac{10^g}{h5^{y_*+1}},
```

所以 `x` 有统一上界。

同理 `x\ge x_*+1` 给出 `y` 的统一上界。

因此

```math
\boxed{
(x>x_*,\ y>y_*)
\text{ 与 decade window 的整数交集有限。}
}
\tag{6}
```

每个固定 `(x,y)` 又令

```math
\rho=h2^x5^y
```

固定，故按照 resonance-collapse 中相同的 rational-contact argument，每个 `(h,x,y,\pm)` 至多对应一个 `\ell`。

所以整个 `++` 象限固定前缀下严格有限。

---

<a id="a1-01-detail-src-0055-1668-3"></a>
#### `--` 象限固定前缀下有限

考虑

```math
 x<x_* ,
\qquad y<y_*.
```

于是

```math
x\le x_*-1,
\qquad y\le y_*-1.
```

此时 decade window 下界

```math
h2^x5^y\ge10^{g-1}
```

反过来给出两个坐标的下界。

例如使用 `y\le y_*-1`：

```math
h2^x5^{y_*-1}
\ge h2^x5^y
\ge10^{g-1},
```

故

```math
2^x
\ge
\frac{10^{g-1}}{h5^{y_*-1}},
```

从而 `x` 有统一下界。

对称地，使用 `x\le x_*-1` 得到 `y` 的统一下界。

因此

```math
\boxed{
(x<x_*,\ y<y_*)
\text{ 与 decade window 的整数交集有限。}
}
\tag{7}
```

再由固定 `(x,y)` 后 `\rho` 固定、`r_3` 固定、既约分母必须等于 `b_3` 的 argument，每个状态至多一个 `\ell`。

所以整个 `--` 象限固定前缀下严格有限。

---

<a id="a1-01-detail-src-0055-1668-4"></a>
#### 只有两个交叉象限能出现无穷整数偏移

剩余两个 double-nonresonant 象限为

```math
\boxed{
\mathcal C_{2+5-}:
\quad x>x_*,\ y<y_*
}
\tag{8}
```

以及

```math
\boxed{
\mathcal C_{2-5+}:
\quad x<x_*,\ y>y_*.
}
\tag{9}
```

在第一条走廊中，`x` 可以向 `+\infty` 增长，同时 `y` 向 `-\infty` 补偿，使

```math
h2^x5^y
```

继续停留在一个固定十进制 decade 中。

第二条走廊完全对称：`x\to-\infty`、`y\to+\infty`。

由于

```math
\frac{\log2}{\log5}\notin\mathbf Q,
```

单凭实数位数窗无法把这两条走廊截成有限整数集；这正是剩余的近 `S`-unit / Diophantine approximation 现象。

因此：

```math
\boxed{
\text{任何真正的 A1 无界尾族，只可能位于这两个 cross corridors 中。}
}
\tag{10}
```

---

<a id="a1-01-detail-src-0055-1668-5"></a>
#### cross corridors 中的平方赋值奇偶锁

虽然两个交叉走廊仍可能无限，但 square certificate 已给出奇偶锁。

<a id="a1-01-detail-src-0055-1668-6"></a>
#### `\mathcal C_{2+5-}`

这里

```math
x>x_*\iff e_2<f_2,
```

所以二进低赋值来自 `TK` 项。平方赋值要求

```math
\boxed{v_2(K)\equiv0\pmod2}.
\tag{11}
```

另一方面

```math
y<y_*\iff f_5<e_5,
```

五进低赋值来自 `2b_3DN` 项，因此

```math
\boxed{
\ell+v+g+v_5(Q)+v_5(N)
\equiv0\pmod2.
}
\tag{12}
```

利用 `v=\ell+y`，化成

```math
\boxed{
y+g+v_5(Q)+v_5(N)\equiv0\pmod2.}
\tag{13}
```

所以该走廊中的奇偶条件同样已经与 `\ell` 解耦。

<a id="a1-01-detail-src-0055-1668-7"></a>
#### `\mathcal C_{2-5+}`

这里二进由 `b_3` 项给出低赋值，因此

```math
\ell+1+u+g+v_2(Q)+v_2(N)
\equiv0\pmod2.
```

代入 `u=\ell+x`：

```math
\boxed{
1+x+g+v_2(Q)+v_2(N)
\equiv0\pmod2.
}
\tag{14}
```

五进则由 `TK` 项给出低赋值，所以必须

```math
\boxed{v_5(K)\equiv0\pmod2.}
\tag{15}
```

因此若

```math
v_2(K)\text{ 为奇数},
```

第一条 cross corridor `\mathcal C_{2+5-}` 整体为空；若

```math
v_5(K)\text{ 为奇数},
```

第二条 cross corridor `\mathcal C_{2-5+}` 整体为空。

特别地若

```math
\boxed{v_2(K),v_5(K)\text{ 均为奇数},}
```

则两个可能无界的 cross corridors 都为空，而其余 resonance / same-direction sectors 已经固定前缀有限。

所以这类前缀完全不存在无界 A1 尾族。

---

<a id="a1-01-detail-src-0055-1668-8"></a>
#### universal factor-pair identity

整数平方证书还有一个对 cross corridor 很有用的等价形式。

由

```math
W^2=T^2K-2Tb_3DN
```

和

```math
K=G^2C^2-D^2N
```

直接得到

```math
T^2G^2C^2-W^2
=T^2D^2N+2Tb_3DN.
```

因此

```math
\boxed{
(TGC-W)(TGC+W)
=TDN(TD+2b_3).
}
\tag{16}
```

又因为

```math
TD=10^{m_3}Q,
```

可写成

```math
\boxed{
(TGC-W)(TGC+W)
=10^{m_3}Q\,N\,(10^{m_3}Q+2b_3).
}
\tag{17}
```

左侧是两个中心在 `TGC`、间距 `2W` 的整数因子；右侧则由十进制主尺度和真实第三分母构成。

这个 factor-pair identity 将是继续攻击两个 cross corridors 的主算术入口之一。

---


<a id="a1-01-detail-src-0055-2152-1"></a>
#### 归一化第三块

记

```math
T=10^\ell,
\qquad
\rho=\frac{b_3}{T},
\qquad
\eta=\frac{a_3}{T}.
```

于是

```math
r_3=\frac{\eta}{\rho}.
```

由

```math
b_3=h2^{\ell+x}5^{\ell+y}
```

有

```math
\boxed{\rho=h2^x5^y}.
```

A1 rational-contact 判别式给出

```math
V^2=K-2\rho DN
\tag{1}
```

对某个 `V\in\mathbf Q`。这里可以直接取

```math
V=\frac WT,
```

因为 denominator-funnel 中

```math
W^2=T^2K-2Tb_3DN
=T^2(K-2\rho DN).
```

由 rational-contact 根公式，归一化分子满足

```math
\boxed{
\eta
=
\rho\,
\frac{
G\rho C\pm(D+\rho)V
}{DG(D+2\rho)}.
}
\tag{2}
```

所有 `C,D,G,N,K` 都只由固定前两块与 `g` 决定。

---

<a id="a1-01-detail-src-0055-2152-2"></a>
#### 第一交叉走廊 `\mathcal C_{2+5-}` 的二进结构

该走廊定义为

```math
x>x_*,
\qquad y<y_*.
```

由 `x>x_*`，在 (1) 中二进赋值由 `K` 项严格主导：

```math
v_2(K)<v_2(2\rho DN).
```

平方存在首先要求

```math
\boxed{k_2:=v_2(K)\text{ 为偶数}.}
```

并且

```math
\boxed{v_2(V)=\frac{k_2}{2}.}
\tag{3}
```

记

```math
d_2=v_2(D),
\qquad
g_2=v_2(G),
\qquad c_2=v_2(C).
```

若

```math
x>d_2,
```

则

```math
v_2(D+\rho)=d_2,
\qquad
v_2(D+2\rho)=d_2,
```

因为

```math
v_2(\rho)=x>d_2,
\qquad
v_2(2\rho)=x+1>d_2.
```

由 (2)，方括号中两项的二进赋值分别为

```math
g_2+c_2+x
```

与

```math
d_2+\frac{k_2}{2}.
```

因此无论是否发生额外抵消，都有

```math
v_2\!\left(
G\rho C\pm(D+\rho)V
\right)
\ge
\min\left(
g_2+c_2+x,\ d_2+\frac{k_2}{2}\right).
```

代回 (2)：

```math
\boxed{
 v_2(\eta)
\ge
x+
\min\left(
g_2+c_2+x,\ d_2+\frac{k_2}{2}\right)
-(2d_2+g_2).
}
\tag{4}
```

当

```math
x>d_2+\frac{k_2}{2}-g_2-c_2,
```

最小值已经固定为第二项，故

```math
\boxed{
 v_2(\eta)
\ge
x-d_2-g_2+\frac{k_2}{2}.
}
\tag{5}
```

特别地，若再有

```math
x>d_2+g_2-\frac{k_2}{2},
```

则

```math
\boxed{v_2(\eta)>0.}
\tag{6}
```

---

<a id="a1-01-detail-src-0055-2152-3"></a>
#### 既约性与 (6) 直接矛盾

在第一交叉走廊中

```math
u=\ell+x.
```

只要

```math
u>0,
```

就有

```math
2\mid b_3.
```

由于

```math
\gcd(a_3,b_3)=1,
```

必有

```math
v_2(a_3)=0.
```

所以

```math
\boxed{
 v_2(\eta)
=v_2(a_3)-v_2(T)
=-\ell
\le0.
}
\tag{7}
```

这与 (6) 矛盾。

因此定义显式阈值

```math
\boxed{
X_{\max}
=
\max\left(
 d_2,
 d_2+\frac{k_2}{2}-g_2-c_2,
 d_2+g_2-\frac{k_2}{2},
 -\ell
\right)
}
```

时最后一项不适合做前缀常数；更干净地分两步写：

- 若 `x\ge0`，则自动 `u=\ell+x>0`；
- 对 `x<0`，只有有限多个 `x` 落在 `x_*<x<0`。

故真正可能向 `+\infty` 延伸的部分满足 `x\ge0`，并且一旦

```math
\boxed{
 x>
X_0:=
\max\left(
0,
 d_2,
 d_2+\frac{k_2}{2}-g_2-c_2,
 d_2+g_2-\frac{k_2}{2}
\right),
}
\tag{8}
```

便产生 (6) 与 (7) 的矛盾。

所以：

```math
\boxed{
\mathcal C_{2+5-}
\text{ 中所有可行整数 }x\text{ 都有固定前缀上界。}
}
\tag{9}
```

结合 decade window，固定 `x` 后 `y` 落在长度小于 `2` 的区间，因此 `y` 也只有有限多个值。

于是第一交叉走廊固定前缀下严格有限。

---

<a id="a1-01-detail-src-0055-2152-4"></a>
#### 第二交叉走廊 `\mathcal C_{2-5+}` 的五进结构

现在考虑

```math
x<x_*,
\qquad y>y_*.
```

由 `y>y_*`，(1) 中五进赋值由 `K` 项严格主导：

```math
v_5(K)<v_5(2\rho DN).
```

平方存在要求

```math
\boxed{k_5:=v_5(K)\text{ 为偶数},}
```

并且

```math
\boxed{v_5(V)=\frac{k_5}{2}.}
\tag{10}
```

记

```math
d_5=v_5(D),
\qquad g_5=v_5(G),
\qquad c_5=v_5(C).
```

若

```math
y>d_5,
```

由于 `2` 是五进单位，

```math
v_5(D+\rho)=d_5,
\qquad
v_5(D+2\rho)=d_5.
```

由 (2) 得

```math
\boxed{
 v_5(\eta)
\ge
 y+
\min\left(g_5+c_5+y,\ d_5+\frac{k_5}{2}\right)
-(2d_5+g_5).
}
\tag{11}
```

一旦

```math
y>d_5+\frac{k_5}{2}-g_5-c_5,
```

有

```math
 v_5(\eta)
\ge
 y-d_5-g_5+\frac{k_5}{2}.
```

若再有

```math
y>d_5+g_5-\frac{k_5}{2},
```

便得到

```math
\boxed{v_5(\eta)>0.}
\tag{12}
```

另一方面，只要

```math
v=\ell+y>0,
```

就有 `5\mid b_3`，既约性强迫

```math
v_5(a_3)=0,
```

所以

```math
\boxed{v_5(\eta)=-\ell\le0,}
\tag{13}
```

与 (12) 矛盾。

如第一走廊一样，所有 `y<0` 且 `y_*<y<0` 的状态本来就是有限的；真正可能向 `+\infty` 延伸的部分有 `y\ge0`。因此定义

```math
\boxed{
Y_0=
\max\left(
0,
 d_5,
 d_5+\frac{k_5}{2}-g_5-c_5,
 d_5+g_5-\frac{k_5}{2}
\right),
}
\tag{14}
```

则任何可行解必须满足

```math
\boxed{y\le Y_0.}
\tag{15}
```

固定 `y` 后 decade window 把 `x` 限制在长度小于 `4` 的整数区间。

所以第二交叉走廊固定前缀下也严格有限。

---

<a id="a1-01-detail-src-0055-2152-5"></a>
#### 两条 cross corridors 均不能承载无界尾族

结合 §§2–4：

```math
\boxed{
\mathcal C_{2+5-}
\text{ 的 }x\text{ 有显式前缀上界};
}
```

```math
\boxed{
\mathcal C_{2-5+}
\text{ 的 }y\text{ 有显式前缀上界}.
}
```

再结合 decade window，两个走廊的另一坐标也随之只剩有限整数集合。

固定 `(h,x,y)` 后

```math
\rho=h2^x5^y
```

固定，进而 `\theta=\rho/D` 固定，rational-contact quadratic 给出的 `r_3` 至多两个固定有理根。原问题要求 `b_3` 正好等于该固定有理数的既约分母，而

```math
b_3=10^\ell\rho,
```

故每个根至多对应一个 `\ell`。

因此：

```math
\boxed{
\text{A1 的两个 cross corridors 均为 fixed-prefix finite。}
}
\tag{16}
```

---

<a id="a1-01-detail-src-0055-2152-6"></a>
#### A1 fixed-prefix finite theorem

此前已经证明：

- resonance sectors：fixed-prefix finite；
- double-nonresonant 的 `++`、`--` 象限：fixed-prefix finite；
- 本文：两个 cross corridors：fixed-prefix finite。

而 `h\mid Q^2G` 本身只有有限多个可能值，`g` 又满足

```math
0\le g\le\min(s_2-1,s_1+1)
```

并受到 rational-contact prefix gap 的进一步限制。

所以得到完整结论：

```math
\boxed{
\text{对任意固定的前两块 }(a_1,b_1,a_2,b_2),
\text{ A1 第三块候选集合是有限的。}
}
\tag{17}
```

而且这个有限性不是抽象存在：上述文件给出了 `g`、`h`、resonance 状态、cross-corridor offset 与每个 offset 的 `\ell` 恢复规则，可转化为显式有限证书。

必须保留证明边界：

```math
\boxed{
\text{(17) 仍不等于全局 A1 空性。}
}
```

前两块本身尚未得到 prefix-uniform 的绝对高度上界，因此不能把所有 fixed-prefix finite 集合的并集称为有限。

下一阶段的唯一任务已经从“控制第三尾”转为：利用本框架对前缀对象 `C,D,G,N,K` 的必要条件，证明所有可能前缀本身为空，或把前缀压入一个全局有限盒。

---


<a id="a1-01-detail-src-0055-2698-1"></a>
#### 整数球面对象

令

```math
q=\operatorname{lcm}(b_1,b_2,b_3),
```

并定义

```math
y_i=qr_i=\frac{qa_i}{b_i}.
```

exact lift 强迫存在正整数 `H` 满足

```math
\boxed{H=qR}
```

以及

```math
\boxed{H^2=y_1^2+y_2^2+y_3^2}.
```

A1 rational-contact 框架中

```math
P=\frac CD,
\qquad
D=10^gQ,
\qquad
T=10^\ell,
```

并有

```math
R=\frac{P+\theta r_3}{1+\theta},
\qquad
\theta=\frac{b_3}{TD}.
```

等价地

```math
P-R=\theta(R-r_3).
\tag{1}
```

---

<a id="a1-01-detail-src-0055-2698-2"></a>
#### contact gap 的整数化

定义两个正整数候选 gap：

```math
\boxed{E=Cq-DH}
```

以及

```math
\boxed{U=H-y_3}.
```

因为 A1 中

```math
P>R>r_3,
```

故

```math
E>0,
\qquad U>0.
```

把 (1) 写成

```math
\frac{Cq-DH}{Dq}
=
\frac{b_3}{TD}
\cdot
\frac{H-y_3}{q}.
```

直接清分母得到

```math
\boxed{
T E=b_3 U.
}
\tag{2}
```

这条等式完全由原始 exact lift 和整数球面推出，不需要 Gaussian integers，也没有对 `a_3` 做任何额外整除假设。

---

<a id="a1-01-detail-src-0055-2698-3"></a>
#### 安全的 `L,\tau` primitive recovery

定义

```math
\delta=\gcd(T,b_3),
```

```math
\boxed{L=\frac T\delta},
\qquad
\boxed{\tau=\frac{b_3}{\delta}}.
```

于是

```math
\gcd(L,\tau)=1.
```

把 (2) 除以 `\delta`：

```math
L E=\tau U.
```

由于 `L` 与 `\tau` 互素：

```math
L\mid U,
\qquad
\tau\mid E.
```

因此存在唯一正整数 `A` 使

```math
\boxed{U=LA}
```

以及

```math
\boxed{E=\tau A}.
\tag{3}
```

这就是 A1 中合法的 primitive gap 参数。

需要特别强调：

```math
\boxed{A\text{ 与原第三分子 }a_3\text{ 没有被证明相等，也不应混同。}}
```

旧公共框架中若某处把 `\delta\mid b_3` 进一步解释成 `\delta\mid a_3`，该步骤不能由 (2)–(3) 支持。

---

<a id="a1-01-detail-src-0055-2698-4"></a>
#### 球面因子分解恢复

由

```math
H^2-y_3^2=y_1^2+y_2^2
```

有

```math
U(H+y_3)=y_1^2+y_2^2.
```

代入 `U=LA`：

```math
\boxed{
LA(H+y_3)=y_1^2+y_2^2.
}
\tag{4}
```

所以

```math
\boxed{LA\mid y_1^2+y_2^2.}
\tag{5}
```

并且

```math
H+y_3
=
\frac{y_1^2+y_2^2}{LA}.
```

与

```math
H-y_3=LA
```

联立，严格恢复

```math
\boxed{
H
=\frac12\left(
LA+
rac{y_1^2+y_2^2}{LA}
\right),
}
\tag{6}
```

```math
\boxed{
y_3
=\frac12\left(
\frac{y_1^2+y_2^2}{LA}-LA
\right).
}
\tag{7}
```

因此旧 A1 基线中的球面 gap 分解可以保留，但其中的整数 `a` 应明确理解为本文的 gap 参数 `A`，不能理解成由 `a_3/\delta` 得到的第三分子正规化。

---

<a id="a1-01-detail-src-0055-2698-5"></a>
#### LCM 前缀化

令

```math
B=\operatorname{lcm}(b_1,b_2),
\qquad
d=\gcd(B,b_3).
```

则

```math
q=\operatorname{lcm}(B,b_3)
=\frac{Bb_3}{d}.
```

定义

```math
\boxed{c=\frac Bd},
\qquad
\boxed{t=\frac{b_3}{d}}.
```

于是

```math
q=b_3c=Bt.
```

第三坐标变成

```math
\boxed{y_3=ca_3,}
```

前两坐标则为

```math
\boxed{
y_1=t\,a_1\frac{B}{b_1},
\qquad
y_2=t\,a_2\frac{B}{b_2}.}
```

定义固定前两块平方和

```math
\boxed{
S_B=
\left(a_1\frac{B}{b_1}\right)^2
+
\left(a_2\frac{B}{b_2}\right)^2.
}
```

则

```math
\boxed{y_1^2+y_2^2=t^2S_B.}
\tag{8}
```

所以 (4) 进一步变成

```math
\boxed{
LA(H+ca_3)=t^2S_B.
}
\tag{9}
```

这是一条安全的整数 divisibility 接口：所有第三块增长都集中在 `L,A,t,c` 中，而 `S_B` 由前两块固定。

---

<a id="a1-01-detail-src-0055-2698-6"></a>
#### contact determinant 的另一种表达

由 `E=\tau A` 与定义

```math
E=Cq-DH
```

得到

```math
\boxed{Cq-DH=\tau A.}
\tag{10}
```

另一方面从 `q=b_3c`、`y_3=ca_3` 和 `H=y_3+LA`：

```math
E
=C b_3c-D(ca_3+LA).
```

又因

```math
b_3=\delta\tau,
\qquad T=\delta L,
```

可写为

```math
\boxed{
 c(Cb_3-Da_3)
=A(\tau+DL).
}
\tag{11}
```

也可直接由 (1) 清分母得到同一关系。

式 (11) 把正的 cross determinant

```math
Cb_3-Da_3>0
```

与整数 gap `A`、尾 primitive pair `(L,\tau)` 精确联系起来。

---

<a id="a1-01-detail-src-0055-2698-7"></a>
#### 对旧 A1 基线的审计结论

现在可以严格区分两类陈述：

<a id="a1-01-detail-src-0055-2698-8"></a>
#### 可以安全保留

```math
U=LA,
\qquad
LA\mid y_1^2+y_2^2,
```

以及由此得到的 `H,y_3` 两个半和/半差公式。

这些都由本文 (2)–(7) 独立重建。

<a id="a1-01-detail-src-0055-2698-9"></a>
#### 不能由本框架支持

若定义

```math
\delta=\gcd(T,b_3),
```

则因为原问题有

```math
\gcd(a_3,b_3)=1,
```

实际上

```math
\gcd(a_3,\delta)=1.
```

所以除 `\delta=1` 外，不能把 `a_3/\delta` 当成整数 primitive numerator。

因此 A1 后续应使用本文的 gap integer `A` 作为球面 primitive recovery，而第三分子继续保持原始整数 `a_3`。

---


来源：`SRC-0055:31–549`；`SRC-0055:718–1182`；`SRC-0055:1240–1589`；`SRC-0055:1668–2096`；`SRC-0055:2152–2673`；`SRC-0055:2698–3100`。原文保全，当前论证以本节为准。

<a id="a1-02"></a>
### A1-02　moving-prefix contact 与全局四层

**状态：已严格完成。** P=(1−lambda)10^k r1+lambda 10^(−g)r2；s1−g∈{−1,0,1,2}。

依赖：[A1-01](#a1-01)

核对：正文推导；本次重写未为此项另增枚举。

<a id="a1-02-detail-src-0089-23-1"></a>
#### 完全消去尾长 `\ell`

记

```math
T=10^\ell,
\qquad
\eta=\frac{a_3}{T},
\qquad
\rho=\frac{b_3}{T}.
```

因为 `a_3` 恰有 `\ell=n_3` 位，

```math
\boxed{\frac1{10}\le\eta<1.}
\tag{1}
```

因为 `b_3` 恰有 `m_3=g+\ell` 位，

```math
\boxed{10^{g-1}\le\rho<10^g.}
\tag{2}
```

并且

```math
\boxed{r_3=\frac\eta\rho.}
\tag{3}
```

原始拼接为

```math
\alpha=T(C+\eta),
\qquad
\beta=T(D+\rho).
```

所以 exact lift 等价于

```math
\boxed{
\frac{C+\eta}{D+\rho}
=
\sqrt{
\frac NG^2+\left(\frac\eta\rho\right)^2
}.
}
\tag{4}
```

这里

```math
C=a_1 10^{n_2}+a_2,
\quad
D=10^gQ,
\quad
Q=b_1 10^{m_2}+b_2,
```

```math
G=b_1b_2,
\qquad
N=(a_1b_2)^2+(a_2b_1)^2
```

完全由前两块和 `g` 决定。

因此连续几何层面的 A1 剩余问题已经完全不含 `\ell`；尾长只负责把 `(\eta,\rho)` 实现成同一个十进制尺度上的既约整数对。

---

<a id="a1-02-detail-src-0089-23-2"></a>
#### 归一化 cross determinant

定义

```math
\boxed{J=C\rho-D\eta.}
```

由于 A1 contact 中

```math
P=\frac CD>R>r_3=\frac\eta\rho,
```

有

```math
\boxed{J>0.}
\tag{5}
```

而

```math
P-R
=
\frac{C\rho-D\eta}{D(D+\rho)}
=
\boxed{
\frac{J}{D(D+\rho)}
},
\tag{6}
```

```math
R-r_3
=
\frac{C\rho-D\eta}{\rho(D+\rho)}
=
\boxed{
\frac{J}{\rho(D+\rho)}
}.
\tag{7}
```

二者之比自动恢复

```math
\frac{P-R}{R-r_3}=\frac\rho D.
```

球面差平方

```math
(R-r_3)(R+r_3)=\frac NG^2
```

再与 (7) 联立，可得到完全归一化的 determinant identity：

```math
\boxed{
G^2(C\rho-D\eta)
(C\rho+D\eta+2\rho\eta)
=
N\rho^2(D+\rho)^2.
}
\tag{8}
```

这是移动前缀与紧致尾矩形之间的一个纯有理代数曲面方程。

---

<a id="a1-02-detail-src-0089-23-3"></a>
#### 前缀值 `P` 必须贴住球面

由

```math
P-R=\frac\rho D(R-r_3)
```

和

```math
\frac\rho D<\frac1Q,
```

有

```math
0<P-R<\frac{R-r_3}{Q}<\frac RQ.
```

因此

```math
\boxed{
\frac{Q}{Q+1}P<R<P.
}
\tag{9}
```

也就是说，前两块拼接值 `P` 与完整球面半径的相对误差严格小于 `1/Q`。

这是 A1 移动前缀最重要的实数接触条件之一。

---

<a id="a1-02-detail-src-0089-23-4"></a>
#### `r_3` 的统一 digit window

由 (1)–(3)：

```math
\frac{1/10}{10^g}
<r_3<
\frac1{10^{g-1}},
```

即

```math
\boxed{
10^{-g-1}<r_3<10^{1-g}.
}
\tag{10}
```

因此

```math
\boxed{
\frac NG^2+10^{-2g-2}
<R^2
<
\frac NG^2+10^{2-2g}.
}
\tag{11}
```

---

<a id="a1-02-detail-src-0089-23-5"></a>
#### 前缀缺口 `K` 的第一个纯整数下界

定义

```math
\boxed{K=G^2C^2-D^2N.}
```

由于

```math
P^2-\frac NG^2
=
\frac{K}{D^2G^2},
```

而 `P>R`，由 (11) 的左侧得到

```math
P^2-\frac NG^2
>R^2-\frac NG^2
=r_3^2
>10^{-2g-2}.
```

故

```math
K>D^2G^2\,10^{-2g-2}.
```

利用

```math
D=10^gQ
```

得到完全消去 `g` 的下界

```math
\boxed{
K>\frac{Q^2G^2}{100}.
}
\tag{12}
```

因为 `K` 为整数，也可写成

```math
\boxed{
K\ge
\left\lfloor\frac{Q^2G^2}{100}\right\rfloor+1.
}
```

---

<a id="a1-02-detail-src-0089-23-6"></a>
#### 第二个纯前缀下界：切触判别

由 denominator-funnel 的 normalized square

```math
V^2=K-2\rho DN\ge0
```

可得

```math
K\ge2\rho DN.
```

而

```math
\rho\ge10^{g-1},
\qquad
D=10^gQ,
```

所以

```math
\boxed{
K\ge
2\cdot10^{2g-1}QN
=
\frac{10^{2g}QN}{5}.
}
\tag{13}
```

若考虑严格 `r_3>0` 对应的非退化接触，则实际候选还要满足相应根的正性；本文保留 (13) 作为无条件必要下界。

综合 (12)–(13)：

```math
\boxed{
K>
\max\left(
\frac{Q^2G^2}{100},
\frac{10^{2g}QN}{5}
\right)
}
\tag{14}
```

（第二项若恰为整数边界，则按 (13) 使用非严格形式。）

---

<a id="a1-02-detail-src-0089-23-7"></a>
#### 一个粗但纯前缀的上窗

由 (9)

```math
P<R\left(1+\frac1Q\right).
```

于是

```math
P^2-\frac NG^2
<
\left(1+\frac1Q\right)^2
\left(
\frac NG^2+r_3^2
\right)
-\frac NG^2.
```

利用

```math
r_3^2<10^{2-2g}
```

得到

```math
P^2-\frac NG^2
<
\left(\frac2Q+\frac1{Q^2}\right)\frac NG^2
+
\left(1+\frac1Q\right)^2 10^{2-2g}.
```

乘以 `D^2G^2=10^{2g}Q^2G^2`：

```math
\boxed{
K
<
10^{2g}(2Q+1)N
+100(Q+1)^2G^2.
}
\tag{15}
```

因此 A1 moving prefix 必须把特殊整数二次型 `K` 放进明确的前缀窗

```math
\boxed{
\max\left(
\frac{Q^2G^2}{100},
\frac{10^{2g}QN}{5}
\right)
<K
<
10^{2g}(2Q+1)N+100(Q+1)^2G^2.
}
\tag{16}
```

---

<a id="a1-02-detail-src-0089-23-8"></a>
#### `K` 作为前两分子的显式不定二次型

记 `p=10^{n_2}`。则

```math
C=a_1p+a_2,
```

所以

```math
K
=
\left(G^2p^2-D^2b_2^2\right)a_1^2
+2G^2p\,a_1a_2
+
\left(G^2-D^2b_1^2\right)a_2^2.
\tag{17}
```

其中

```math
G^2-D^2b_1^2<0,
```

而在 A1 carrier 可行区第一系数处于正侧。因此 `K` 是一个由 decimal-shift 参数固定的显式不定二元二次型。

A1 的剩余 prefix problem 可以表述为：

> 在 `a_i,b_i` 的位数、互素性和 carrier 约束下，证明这个特殊不定二次型无法同时落入 (16) 的接触窗，并支持 normalized square / primitive-gap 条件。

---


<a id="a1-02-detail-src-0089-969-1"></a>
#### 统一无量纲变量

沿用前文记号

```math
A_0=10^k r_1,
\qquad
t=\frac{r_2}{A_0},
\qquad
q_0=\frac{r_3}{A_0}.
```

A1 的第一坐标严格承担 carrier，因此

```math
0<t<1.
```

再记

```math
R_0=\frac{\mathcal R}{A_0}.
```

球面方程给出

```math
\boxed{R_0^2=t^2+10^{-2k}+q_0^2.}
\tag{1}
```

令

```math
Q=b_1 10^{m_2}+b_2,
\qquad
\lambda=\frac{b_2}{Q}.
```

A1 前两块拼接值满足

```math
\frac P{A_0}
=(1-\lambda)+\lambda10^{-g}t.
\tag{2}
```

而 rational-contact 条件给出

```math
\frac{Q}{Q+1}P<\mathcal R<P.
\tag{3}
```

---

<a id="a1-02-detail-src-0089-969-2"></a>
#### 一个此前未单独提取的统一事实：`R_0>1/2`

设

```math
B=b_1 10^{m_2}.
```

则

```math
Q=B+b_2.
```

由 (2)，第二项严格为正，所以

```math
\frac P{A_0}
>
1-\lambda
=
\frac BQ.
```

由 (3)：

```math
R_0
>
\frac{Q}{Q+1}\frac BQ
=
\frac{B}{Q+1}
=
\frac{B}{B+b_2+1}.
```

因为 `b_2` 恰有 `m_2` 位，

```math
b_2+1\le10^{m_2}\le B,
```

所以

```math
\frac{B}{B+b_2+1}\ge\frac12.
```

前面的第一步是严格不等式，因此最终得到

```math
\boxed{R_0>\frac12.}
\tag{4}
```

这个结论不依赖 `g,k` 的大小，也不依赖第三尾正规化。

---

<a id="a1-02-detail-src-0089-969-3"></a>
#### 对任意 A1 的统一 `t` 下界公式

A1 位数给出

```math
s_2=k+g,
\qquad
s_3=-g.
```

由十进制位数窗

```math
r_2>10^{k+g-1},
\qquad
r_3<10^{1-g},
```

故

```math
\boxed{
\frac{r_3}{r_2}<10^{2-k-2g}.
}
\tag{5}
```

因为

```math
q_0=\frac{r_3}{r_2}t,
```

有

```math
q_0^2
<
10^{4-2k-4g}t^2.
```

代入 (1)，再用 (4)：

```math
\frac14
<R_0^2
<
\left(1+10^{4-2k-4g}\right)t^2+10^{-2k}.
```

因此

```math
\boxed{
 t^2>
\frac{
\frac14-10^{-2k}
}{
1+10^{4-2k-4g}
}.
}
\tag{6}
```

这是覆盖整个 A1 的统一 carrier-ratio 下界。

---

<a id="a1-02-detail-src-0089-969-4"></a>
#### 泛型区域的旧四层结论得到更干净的证明

若

```math
k+2g\ge3,
```

则

```math
10^{4-2k-4g}\le\frac1{100}.
```

又 `k\ge1`，所以

```math
10^{-2k}\le\frac1{100}.
```

由 (6)：

```math
t^2>
\frac{
1/4-1/100
}{1+1/100}
=
\frac{24}{101}.
```

于是

```math
\boxed{t>\sqrt{\frac{24}{101}}>\frac25.}
\tag{7}
```

这重新得到前文用于四层压缩的下界，而且常数更强。

由

```math
r_1=\frac{r_2}{10^k t}
```

和

```math
r_2<10^{k+g+1}
```

可得

```math
r_1<\sqrt{\frac{101}{24}}\,10^{g+1}<10^{g+2}.
```

因此

```math
s_1\le g+2.
```

另一方面旧 carrier cap 已严格给出

```math
s_1\ge g-1.
```

所以泛型区域仍为

```math
\boxed{s_1-g\in\{-1,0,1,2\}.}
\tag{8}
```

---

<a id="a1-02-detail-src-0089-969-5"></a>
#### 低尺度角落 `(g,k)=(0,2)` 也只有四层

此时 (6) 变成

```math
t^2>
\frac{
1/4-10^{-4}
}{2}
=
\frac{2499}{20000}.
```

故

```math
t>\sqrt{\frac{2499}{20000}}>\frac13.
```

于是

```math
r_1
=
\frac{r_2}{100t}
<
\frac{10^3}{100t}
=
\frac{10}{t}
<30.
```

若 `s_1\ge3`，则位数窗强迫

```math
r_1>10^{s_1-1}\ge100,
```

矛盾。

所以

```math
\boxed{s_1\le2.}
```

而 `g=0` 时 carrier 下界为

```math
s_1\ge-1.
```

故

```math
\boxed{(g,k)=(0,2)\Longrightarrow s_1\in\{-1,0,1,2\}.}
\tag{9}
```

---

<a id="a1-02-detail-src-0089-969-6"></a>
#### 低尺度角落 `(g,k)=(0,1)` 先压到五层

现在 (6) 给出

```math
t^2>
\frac{
1/4-1/100
}{101}
=
\frac{24}{10100}.
```

因此

```math
t>\sqrt{\frac{24}{10100}}.
```

从而

```math
r_1
=
\frac{r_2}{10t}
<
\frac{10^2}{10t}
=
\frac{10}{t}
<206.
```

所以不可能有 `s_1\ge4`，即

```math
s_1\le3.
```

结合 `s_1\ge-1`，暂时只剩

```math
s_1\in\{-1,0,1,2,3\}.
```

---

<a id="a1-02-detail-src-0089-969-7"></a>
#### `(g,k)=(0,1)` 的最高层 `s_1=3` 直接为空

假设

```math
g=0,
\qquad k=1,
\qquad s_1=3.
```

则

```math
r_1>10^{s_1-1}=100,
```

故

```math
A_0=10r_1>1000.
```

又 `s_2=1`、`s_3=0`，因此

```math
r_2<100,
\qquad
r_3<10.
```

于是

```math
t=\frac{r_2}{A_0}<\frac1{10},
\qquad
q_0=\frac{r_3}{A_0}<\frac1{100}.
```

由球面式 (1)：

```math
R_0^2
<
\frac1{100}
+
\frac1{100}
+
\frac1{10000}
=
\frac{201}{10000}
<\frac14.
```

这与统一结论 (4)

```math
R_0>\frac12
```

矛盾。

所以

```math
\boxed{(g,k)=(0,1),\ s_1=3\text{ 为空}.}
\tag{10}
```

因此该低尺度角落最终也只剩

```math
\boxed{s_1\in\{-1,0,1,2\}.}
\tag{11}
```

---

<a id="a1-02-detail-src-0089-969-8"></a>
#### 全局四层定理

综合泛型区域 (8)、低尺度 `(0,2)` 的 (9) 与 `(0,1)` 的 (11)，A1 的两个旧例外已经全部消失。

最终对每一个 A1 exact-lift 候选均有

```math
\boxed{
 g-1\le s_1\le g+2.
}
```

等价地

```math
\boxed{
 s_1-g\in\{-1,0,1,2\}.
}
\tag{12}
```

因此 A1 moving-prefix problem 不再需要分“泛型 + 两个低尺度角落”；从现在开始可以全局只研究四个位数层

```math
\boxed{d:=s_1-g=-1,0,1,2.}
```

其中最高层 `d=2` 是十进制边界接触最强的一层，后续应优先处理。

---


来源：`SRC-0089:23–454`；`SRC-0089:969–1445`。原文保全，当前论证以本节为准。

<a id="a1-03"></a>
### A1-03　最高层的 residue、half gap 与正 excess

**状态：已严格完成。** 仅 d=2；endpoint 参数不移植到低层。

依赖：[A1-02](#a1-02)

核对：正文推导；本次重写未为此项另增枚举。

<a id="a1-03-detail-src-0089-1482-1"></a>
#### 最高层中的第三坐标极小

沿用

```math
A_0=10^k r_1,
\qquad
t=\frac{r_2}{A_0},
\qquad
q_0=\frac{r_3}{A_0},
\qquad
R_0=\frac{\mathcal R}{A_0}.
```

由 `top-layer.md`：

```math
\boxed{R_0>\frac12.}
\tag{1}
```

现在假设

```math
s_1=g+2.
```

位数窗给出

```math
r_1>10^{g+1},
\qquad
r_3<10^{1-g}.
```

于是

```math
A_0>10^{k+g+1},
```

从而

```math
\boxed{q_0<10^{-k-2g}.}
\tag{2}
```

球面式

```math
R_0^2=t^2+10^{-2k}+q_0^2
```

与 (1)–(2) 联立得到

```math
t^2>
\frac14-10^{-2k}-10^{-2k-4g}.
```

右侧在 `k\ge1,g\ge0` 时最小为

```math
\frac14-
rac1{100}-\frac1{100}=
rac{23}{100}.
```

故

```math
\boxed{t>\frac{\sqrt{23}}{10}>\frac{47}{100}.}
\tag{3}
```

---

<a id="a1-03-detail-src-0089-1482-2"></a>
#### 最高层的精确四因子分解

因为

```math
s_1=g+2,
\qquad
s_2=k+g,
```

有

```math
n_1=m_1+g+2,
\qquad
n_2=m_2+k+g.
```

直接检查十进制指数可得

```math
\boxed{
 t
=
\left(\frac{a_2}{10^{n_2}}\right)
\left(\frac{b_1}{10^{m_1}}\right)
\left(\frac{10^{n_1-1}}{a_1}\right)
\left(\frac{10^{m_2-1}}{b_2}\right).
}
\tag{4}
```

四个因子都属于 `(0,1]`，而它们的乘积由 (3) 大于 `47/100`。因此每一个因子都严格大于 `47/100`：

```math
\boxed{a_2>\frac{47}{100}10^{n_2},}
\tag{5}
```

```math
\boxed{b_1>\frac{47}{100}10^{m_1},}
\tag{6}
```

```math
\boxed{a_1<\frac{100}{47}10^{n_1-1},}
\tag{7}
```

```math
\boxed{b_2<\frac{100}{47}10^{m_2-1}.}
\tag{8}
```

所以最高层从一开始就位于四个十进制端点组成的角落，而不是一个普通内部矩形。

---

<a id="a1-03-detail-src-0089-1482-3"></a>
#### contact 把 `1-t` 锁到 `10^{-2k}` 尺度

记

```math
Q=b_1 10^{m_2}+b_2,
\qquad
\lambda=\frac{b_2}{Q}.
```

由 (6)、(8)：

```math
\lambda
<
\frac{b_2}{b_1 10^{m_2}}
<
\frac{1000}{2209}10^{-m_1}.
\tag{9}
```

同样

```math
\frac1Q
<
\frac1{b_1 10^{m_2}}
<
\frac{100}{47}10^{-m_1-m_2}
\le
\frac{10}{47}10^{-m_1}.
\tag{10}
```

rational contact 在无量纲坐标中为

```math
1-R_0
=
\lambda(1-10^{-g}t)
+
\theta(R_0-q_0),
\qquad
0<\theta<\frac1Q.
```

因为 `R_0<1`，所以由 (9)–(10)

```math
\boxed{
1-R_0
<
\frac{1470}{2209}10^{-m_1}.
}
\tag{11}
```

另一方面，(4) 中第二因子给出

```math
t<\frac{b_1}{10^{m_1}},
```

所以

```math
1-t
>
1-\frac{b_1}{10^{m_1}}
\ge10^{-m_1}.
\tag{12}
```

因此

```math
R_0-t
=(1-t)-(1-R_0)
>
\boxed{
\frac{739}{2209}10^{-m_1}.
}
\tag{13}
```

另一方面由球面式

```math
R_0-t
=
\frac{10^{-2k}+q_0^2}{R_0+t}.
```

由 (2)、(3)，

```math
R_0+t>2t>\frac{94}{100},
```

故

```math
R_0-t
<
\frac{100}{94}
10^{-2k}(1+10^{-4g})
\le
\boxed{\frac{100}{47}10^{-2k}.}
\tag{14}
```

若 `m_1\le2k-1`，则 (13) 给出

```math
R_0-t
>
\frac{7390}{2209}10^{-2k},
```

但

```math
\frac{7390}{2209}>
rac{4700}{2209}=
rac{100}{47},
```

与 (14) 矛盾。

所以最高层全局满足

```math
\boxed{m_1\ge2k.}
\tag{15}
```

这已经把 `k` 压入第一分母位数的一半尺度：

```math
k\le\frac{m_1}{2}.
```

---

<a id="a1-03-detail-src-0089-1482-4"></a>
#### 更强的贴边：`1-t<3\cdot10^{-2k}`

由 (15)：

```math
10^{-m_1}\le10^{-2k}.
```

把它代入 (11)：

```math
1-R_0
<
\frac{1470}{2209}10^{-2k}.
```

再与 (14) 相加：

```math
1-t
=(1-R_0)+(R_0-t)
<
\left(
\frac{1470}{2209}
+
\frac{4700}{2209}
\right)10^{-2k}.
```

因此

```math
\boxed{
1-t
<
\frac{6170}{2209}10^{-2k}
<3\cdot10^{-2k}.
}
\tag{16}
```

所以最高层的四因子乘积并非仅仅大于一个固定常数；它实际上以 `10^{-2k}` 的速度逼近 1。

---

<a id="a1-03-detail-src-0089-1482-5"></a>
#### 两个 surplus 与四个端点偏移

定义

```math
\boxed{r=m_1-2k\ge0.}
\tag{17}
```

再定义

```math
\boxed{s=m_2+g-k.}
\tag{18}
```

从 (4)、(16)，每个因子都大于

```math
1-3\cdot10^{-2k}.
```

令端点偏移

```math
\boxed{w=10^{m_1}-b_1\ge1,}
```

```math
\boxed{x=a_1-10^{n_1-1}\ge0,}
```

```math
\boxed{z=10^{n_2}-a_2\ge1,}
```

```math
\boxed{y=b_2-10^{m_2-1}\ge0.}
```

则由四因子逐项得到

```math
\boxed{1\le w<3\cdot10^r,}
\tag{19}
```

```math
\boxed{0\le x<4\cdot10^{r+g+1},}
\tag{20}
```

```math
\boxed{1\le z<3\cdot10^s,}
\tag{21}
```

```math
\boxed{0\le y<4\cdot10^{s-k-g-1}.}
\tag{22}
```

其中 (20)、(22) 使用了

```math
\frac{3\cdot10^{-2k}}{1-3\cdot10^{-2k}}
<4\cdot10^{-2k}.
```

由于 `z\ge1`，(21) 立即强迫

```math
\boxed{s\ge0,}
\tag{23}
```

即

```math
\boxed{m_2+g\ge k.}
```

特别地，若

```math
s=0,
```

则

```math
\boxed{z\in\{1,2\}.}
\tag{24}
```

若

```math
r=0,
```

则同理

```math
\boxed{w\in\{1,2\}.}
\tag{25}
```

此外若

```math
s\le k+g,
```

则 (22) 的右侧小于 1，故整数 `y` 必须为零：

```math
\boxed{s\le k+g\Longrightarrow b_2=10^{m_2-1}.}
\tag{26}
```

这时 `gcd(a_2,b_2)=1` 还等价强迫

```math
\boxed{\gcd(z,10)=1.}
\tag{27}
```

因为

```math
a_2=10^{n_2}-z.
```

---

<a id="a1-03-detail-src-0089-1482-6"></a>
#### endpoint normal form

利用

```math
m_1=2k+r,
\qquad
m_2=k-g+s,
```

最高层的四个前缀整数可以统一写成

```math
\boxed{
b_1=10^{2k+r}-w,}
\tag{28}
```

```math
\boxed{
a_1=10^{2k+r+g+1}+x,}
\tag{29}
```

```math
\boxed{
b_2=10^{k-g+s-1}+y,}
\tag{30}
```

```math
\boxed{
a_2=10^{2k+s}-z.}
\tag{31}
```

所有增长已经从原来的四个大整数转移到 `k,g,r,s`，而 `w,x,y,z` 只允许在 (19)–(22) 的端点薄层中移动。

---

<a id="a1-03-detail-src-0089-1482-7"></a>
#### 精确 determinant 展开

定义第一、第二坐标十进制移位差

```math
\boxed{
\Delta
=10^k a_1b_2-a_2b_1
>0.
}
\tag{32}
```

这里正性等价于 `t<1`。

把 (28)–(31) 代入并消去主导的相同十进制幂，可以得到完全正的展开：

```math
\boxed{
\begin{aligned}
\Delta={}&
10^{m_1+k+g+1}y
+10^{k+m_2-1}x
+10^kxy\\
&+10^{k+g+m_2}w
+b_1z.
\end{aligned}
}
\tag{33}
```

右端五项全部非负，且最后两项严格为正。

定义统一尺度

```math
\boxed{
L_0=10^{m_1+m_2+g-k}=10^{2k+r+s}.
}
\tag{34}
```

再定义紧致 offset 坐标

```math
\boxed{X=\frac{x}{10^{r+g+1}},}
\qquad
\boxed{W=\frac{w}{10^r},}
```

```math
\boxed{Z=\frac{z}{10^s},}
\qquad
\boxed{Y=10^{k+g+1-s}y.}
\tag{35}
```

并记

```math
\varepsilon=10^{-2k}.
```

则 (33) 精确化成

```math
\boxed{
\frac{\Delta}{L_0}
=
X+W+Y+Z
+
\varepsilon(XY-WZ).
}
\tag{36}
```

这就是最高层的紧致四-offset kernel。

还可以从

```math
1-t=\frac{\Delta}{10^k a_1b_2}
```

得到另一条精确表达：

```math
\boxed{
\frac{\Delta}{L_0}
=
\frac{1-t}{\varepsilon}
(1+\varepsilon X)(1+\varepsilon Y).
}
\tag{37}
```

由球面式

```math
R_0-t
>
\frac{\varepsilon}{2}
```

可得

```math
1-t>\frac\varepsilon2,
```

再结合 (16)、(37)：

```math
\boxed{
\frac12
<
\frac{\Delta}{L_0}
<
\frac72.
}
\tag{38}
```

因此原本无界的最高层已经被压成一个固定宽度的 compact determinant window。

---

<a id="a1-03-detail-src-0089-1482-8"></a>
#### `g\ge1` 时两个 surplus 都必须严格为正

现在额外假设

```math
g\ge1.
```

由 (16) 与四因子贴边：

```math
b_1>(1-3\varepsilon)10^{m_1},
\qquad
b_2<\frac{10^{m_2-1}}{1-3\varepsilon}.
```

因为 `m_1\ge2k`、`m_2\ge1`、`\varepsilon\le1/100`，有

```math
\lambda<\frac\varepsilon9,
\qquad
\frac1Q<\frac\varepsilon9.
```

所以

```math
\boxed{1-R_0<\frac{2}{9}\varepsilon.}
\tag{39}
```

又由 `g\ge1` 和 (2)：

```math
q_0^2<\frac{\varepsilon}{10000}.
```

设

```math
\delta=1-t.
```

由

```math
1-R_0^2
=2\delta-\delta^2-\varepsilon-q_0^2
```

以及

```math
1-R_0^2<2(1-R_0)<\frac49\varepsilon,
```

再用 `\delta<3\varepsilon`，得到

```math
2\delta
<
\left(
\frac9{100}+1+\frac1{10000}+\frac49
\right)\varepsilon
<
\frac85\varepsilon.
```

因此

```math
\boxed{\delta<\frac45\varepsilon.}
\tag{40}
```

代回 (37)。由于

```math
\delta<\frac45\varepsilon\le\frac1{125},
```

且

```math
1+\varepsilon X<\frac1{1-\delta},
\qquad
1+\varepsilon Y<\frac1{1-\delta},
```

有

```math
\boxed{
\frac{\Delta}{L_0}<\frac56.
}
\tag{41}
```

若 `r=0`，则 `W=w\ge1`，而 (33) 的归一化各项全为非负，故

```math
\frac{\Delta}{L_0}\ge W\ge1,
```

与 (41) 矛盾。因此

```math
\boxed{g\ge1\Longrightarrow r\ge1.}
\tag{42}
```

若 `s=0`，则 `Z=z\ge1`。在 (36) 中真正对应最后一项的是

```math
\frac{b_1}{10^{m_1}}Z.
```

而

```math
\frac{b_1}{10^{m_1}}>t=1-\delta>\frac{124}{125}>\frac56.
```

故单独这一项已经大于 `5/6`，再次与 (41) 矛盾。所以

```math
\boxed{g\ge1\Longrightarrow s\ge1.}
\tag{43}
```

综合：

```math
\boxed{
 d=2,\ g\ge1
\Longrightarrow
m_1\ge2k+1,
\qquad
m_2+g\ge k+1.
}
\tag{44}
```

---

<a id="a1-03-detail-src-0089-1482-9"></a>
#### `g=0` 时两个 equality surplus 不能同时出现

若 `g=0`，仍有 (39)。此时由 (2)

```math
q_0^2<\varepsilon.
```

同样计算得到

```math
\delta<\frac{13}{10}\varepsilon.
```

因此由 (37) 可取安全粗界

```math
\boxed{
\frac{\Delta}{L_0}<\frac75.
}
\tag{45}
```

若同时

```math
r=s=0,
```

则 `W=w\ge1`、`Z=z\ge1`，并且

```math
\frac{b_1}{10^{m_1}}>1-\delta>0.98.
```

所以 (33) 归一化后的 `w` 项与 `z` 项之和已经严格大于

```math
1+0.98>\frac75,
```

与 (45) 矛盾。

故

```math
\boxed{
 d=2,\ g=0
\Longrightarrow
(r,s)\ne(0,0).
}
\tag{46}
```

---


<a id="a1-03-detail-src-0089-2401-1"></a>
#### 端点基线

沿用前文

```math
m_1=2k+r,
\qquad
m_2=k-g+s,
```

以及

```math
b_1=10^{2k+r}-w,
\qquad
 a_1=10^{2k+r+g+1}+x,
```

```math
b_2=10^{k-g+s-1}+y,
\qquad
 a_2=10^{2k+s}-z.
```

其中

```math
w,z\ge1,
\qquad x,y\ge0.
```

定义

```math
\boxed{
U_1=x+10^{g+1}w,
}
\tag{1}
```

```math
\boxed{
U_2=z+10^{k+g+1}y.
}
\tag{2}
```

二者均为正整数。

---

<a id="a1-03-detail-src-0089-2401-2"></a>
#### 两个原分数变成十进制中心加减既约余量

由

```math
10^{g+1}b_1
=10^{2k+r+g+1}-10^{g+1}w,
```

结合 (1)：

```math
\boxed{
 a_1=10^{g+1}b_1+U_1.
}
\tag{3}
```

同理

```math
10^{k+g+1}b_2
=10^{2k+s}+10^{k+g+1}y,
```

结合 (2)：

```math
\boxed{
 a_2=10^{k+g+1}b_2-U_2.
}
\tag{4}
```

因此

```math
\boxed{
 r_1=10^{g+1}+\frac{U_1}{b_1},
}
\tag{5}
```

```math
\boxed{
 r_2=10^{k+g+1}-\frac{U_2}{b_2}.
}
\tag{6}
```

令共同十进制中心

```math
\boxed{M=10^{k+g+1}.}
```

则

```math
10^k r_1
=M+10^k\frac{U_1}{b_1},
\qquad
r_2
=M-\frac{U_2}{b_2}.
```

所以最高层精确描述成第一 carrier 坐标从 `M` 的上侧逼近、第二坐标从 `M` 的下侧逼近。

---

<a id="a1-03-detail-src-0089-2401-3"></a>
#### 原始既约性直接传给两个余量

由 (3)：

```math
\gcd(a_1,b_1)
=
\gcd(U_1,b_1).
```

原问题要求 `gcd(a_1,b_1)=1`，故

```math
\boxed{
\gcd(U_1,b_1)=1.
}
\tag{7}
```

同理由 (4)：

```math
\boxed{
\gcd(U_2,b_2)=1.
}
\tag{8}
```

因此两个 rational defects

```math
\frac{U_1}{b_1},
\qquad
\frac{U_2}{b_2}
```

本身已经是既约分数。

---

<a id="a1-03-detail-src-0089-2401-4"></a>
#### carrier gap 的二项分解

定义

```math
\Delta=10^k a_1b_2-a_2b_1>0.
```

把 (3)–(4) 代入：

```math
\begin{aligned}
\Delta
&=10^k(10^{g+1}b_1+U_1)b_2
 -(10^{k+g+1}b_2-U_2)b_1\\
&=10^k b_2U_1+b_1U_2.
\end{aligned}
```

所以

```math
\boxed{
\Delta=10^k b_2U_1+b_1U_2.
}
\tag{9}
```

除以 `G=b_1b_2`：

```math
\boxed{
10^k r_1-r_2
=
10^k\frac{U_1}{b_1}
+
\frac{U_2}{b_2}.
}
\tag{10}
```

这就是最高层真正的 rational gap。

---

<a id="a1-03-detail-src-0089-2401-5"></a>
#### 与四-offset compact kernel 的精确对应

沿用

```math
\varepsilon=10^{-2k},
```

```math
X=\frac{x}{10^{r+g+1}},
\quad
W=\frac{w}{10^r},
\quad
Y=10^{k+g+1-s}y,
\quad
Z=\frac{z}{10^s}.
```

则

```math
\boxed{
\frac{U_1}{10^{r+g+1}}=X+W,
}
\tag{11}
```

```math
\boxed{
\frac{U_2}{10^s}=Y+Z.
}
\tag{12}
```

又

```math
\frac{b_1}{10^{m_1}}=1-\varepsilon W,
\qquad
\frac{b_2}{10^{m_2-1}}=1+\varepsilon Y.
```

令

```math
L_0=10^{2k+r+s}.
```

把 (9) 除以 `L_0`：

```math
\boxed{
\frac{\Delta}{L_0}
=(1+\varepsilon Y)(X+W)
 +(1-\varepsilon W)(Y+Z).
}
\tag{13}
```

展开恰为前文

```math
X+W+Y+Z+\varepsilon(XY-WZ).
```

所以 residue kernel 与 compact offset kernel 完全等价，但 (13) 保留了两个正的既约余量块，后续做素数与整除分析更自然。

---

<a id="a1-03-detail-src-0089-2401-6"></a>
#### `g\ge1` 时两个余量都有固定十进制上界

前文已经证明在 `g\ge1` 的最高层：

```math
\boxed{
\frac12<\frac{\Delta}{L_0}<\frac56,
}
\tag{14}
```

并且

```math
\delta:=1-t<\frac45\varepsilon.
```

因此

```math
\frac{b_1}{10^{m_1}}>t>1-\frac45\varepsilon
\ge\frac{124}{125},
```

即

```math
1-\varepsilon W>\frac{124}{125}.
\tag{15}
```

从 (13) 的第一正项：

```math
(1+\varepsilon Y)(X+W)<\frac56,
```

故

```math
\boxed{
0<X+W<\frac56.
}
\tag{16}
```

也就是

```math
\boxed{
0<U_1<\frac56\,10^{r+g+1}.
}
\tag{17}
```

从第二正项及 (15)：

```math
\frac{124}{125}(Y+Z)<\frac56,
```

所以

```math
\boxed{
0<Y+Z<\frac{625}{744}.
}
\tag{18}
```

即

```math
\boxed{
0<U_2<\frac{625}{744}\,10^s.
}
\tag{19}
```

另一方面，由 (13) 下界 `>1/2`。又由 `\delta<4\varepsilon/5` 可得

```math
1+\varepsilon Y<\frac1{1-\delta}<\frac{125}{124}.
```

若同时

```math
X+W\le\frac{62}{249},
\qquad
Y+Z\le\frac{62}{249},
```

则

```math
\frac{\Delta}{L_0}
<
\left(\frac{125}{124}+1\right)\frac{62}{249}
=\frac12,
```

矛盾。因此

```math
\boxed{
\max\left(
\frac{U_1}{10^{r+g+1}},
\frac{U_2}{10^s}
\right)
>\frac{62}{249}.
}
\tag{20}
```

也就是说，两个余量至少有一个必须占据其自然十进制尺度的约四分之一以上；不能同时退化成极小余量。

---

<a id="a1-03-detail-src-0089-2401-7"></a>
#### rational gap 的固定半尺度窗口

由 (10) 与

```math
\frac{\Delta}{G}
=
\frac{L_0}{G}\frac{\Delta}{L_0},
```

而

```math
G=b_1b_2
=10^{3k+r+s-g-1}
(1-\varepsilon W)(1+\varepsilon Y),
```

有

```math
\boxed{
10^k\frac{U_1}{b_1}+\frac{U_2}{b_2}
=
10^{g+1-k}
\frac{\Delta/L_0}
{(1-\varepsilon W)(1+\varepsilon Y)}.
}
\tag{21}
```

在 `g\ge1` 时，利用

```math
\frac12<\frac{\Delta}{L_0}<\frac56,
```

以及

```math
1-\varepsilon W>\frac{124}{125},
\qquad
1+\varepsilon Y<\frac{125}{124},
```

得到安全窗口

```math
\boxed{
\frac{62}{125}\,10^{g+1-k}
<
10^k\frac{U_1}{b_1}+\frac{U_2}{b_2}
<
\frac{625}{744}\,10^{g+1-k}.
}
\tag{22}
```

因此最高层的 carrier gap 已被固定在大约 `1/2` 个自然十进制单位上。

---


<a id="a1-03-detail-src-0089-2938-1"></a>
#### 记号

沿用

```math
M=10^{k+g+1},
\qquad
A_0=10^k r_1,
```

```math
t=\frac{r_2}{A_0},
\qquad
R_0=\frac R{A_0},
\qquad
q_0=\frac{r_3}{A_0},
```

以及

```math
\varepsilon=10^{-2k},
\qquad
\delta=1-t,
\qquad
\alpha=1-R_0.
```

前文已严格证明，在 `d=2,g\ge1` 中

```math
r=m_1-2k\ge1,
\qquad
s=m_2+g-k\ge1,
```

并且

```math
\boxed{0<\delta<\frac45\varepsilon.}
\tag{1}
```

球面关系为

```math
R_0^2=t^2+\varepsilon+q_0^2.
\tag{2}
```

---

<a id="a1-03-detail-src-0089-2938-2"></a>
#### `alpha/epsilon` 只有百分之二量级

contact 恒等式给出

```math
\alpha
=\lambda(1-10^{-g}t)
+
\theta(R_0-q_0),
```

其中

```math
0<\theta<\frac1Q,
\qquad
\lambda=\frac{b_2}{Q}.
```

所以

```math
\boxed{0<\alpha<\lambda+\frac1Q.}
\tag{3}
```

最高层四因子分解与 (1) 说明每一个因子都大于 `t=1-delta`。因此

```math
\frac{b_1}{10^{m_1}}>1-\delta,
\qquad
\frac{b_2}{10^{m_2-1}}<\frac1{1-\delta}.
```

于是

```math
\lambda
<
\frac{10^{-m_1-1}}{(1-\delta)^2}.
```

因为

```math
m_1=2k+r,\qquad r\ge1,
```

除以 `epsilon=10^{-2k}`：

```math
\frac\lambda\varepsilon
<
\frac{10^{-r-1}}{(1-\delta)^2}
\le
\frac{10^{-2}}{(1-0.008)^2}
<0.0102.
\tag{4}
```

另一方面

```math
\frac1Q
<
\frac1{b_1 10^{m_2}}
<
\frac{10^{-m_1-m_2}}{1-\delta}.
```

由于 `r\ge1,m_2\ge1`：

```math
\frac1{Q\varepsilon}
<
\frac{10^{-r-m_2}}{1-\delta}
\le
\frac{10^{-2}}{0.992}
<0.0101.
\tag{5}
```

由 (3)–(5)：

```math
\boxed{
0<\frac\alpha\varepsilon<0.0203.
}
\tag{6}
```

---

<a id="a1-03-detail-src-0089-2938-3"></a>
#### `delta/epsilon` 被压到 `1/2` 附近

由

```math
R_0=1-\alpha,
\qquad
t=1-\delta,
```

把球面式 (2) 展开：

```math
1-2\alpha+\alpha^2
=1-2\delta+\delta^2+\varepsilon+q_0^2.
```

所以

```math
\boxed{
2(\delta-\alpha)
=\varepsilon+q_0^2+\delta^2-\alpha^2.
}
\tag{7}
```

最高层有

```math
q_0<10^{-k-2g},
```

因此

```math
\boxed{
\frac{q_0^2}{\varepsilon}<10^{-4g}\le10^{-4}.
}
\tag{8}
```

由 (1)：

```math
\frac{\delta^2}{2\varepsilon}
<\frac{8}{25}\varepsilon
\le0.0032.
\tag{9}
```

结合 (6)–(9)，从 (7) 得到

```math
\frac\delta\varepsilon
<
\frac12+0.0203+0.00005+0.0032
<\frac{21}{40}.
```

即

```math
\boxed{
\frac\delta\varepsilon<\frac{21}{40}.
}
\tag{10}
```

下界方面，(6) 给出 `alpha<0.0203 epsilon`，故 `alpha^2<epsilon^2/1600`。由 (7) 丢掉正的 `alpha,q_0,delta^2` 项，仅保留可能的 `-alpha^2`：

```math
\frac\delta\varepsilon
>
\frac12-
rac{\alpha^2}{2\varepsilon}
>
\frac12-
rac1{320000}
>
\frac{499}{1000}.
```

所以

```math
\boxed{
\frac{499}{1000}
<\frac\delta\varepsilon
<\frac{21}{40}.
}
\tag{11}
```

---

<a id="a1-03-detail-src-0089-2938-4"></a>
#### carrier gap 的半单位壳层

定义真实 carrier gap

```math
D_0:=A_0-r_2=\delta A_0.
```

自然十进制尺度为

```math
\boxed{
H_0=M\varepsilon=10^{g+1-k}.
}
\tag{12}
```

端点坐标给出

```math
\frac{A_0}{M}
=
\frac{1+\varepsilon X}{1-\varepsilon W}.
```

四因子乘积为 `t=1-delta`，故

```math
\frac1{1+\varepsilon X}>1-\delta,
\qquad
1-\varepsilon W>1-\delta.
```

于是

```math
1<\frac{A_0}{M}<\frac1{(1-\delta)^2}
<\left(\frac{125}{124}\right)^2.
\tag{13}
```

因为

```math
\frac{D_0}{H_0}
=\frac\delta\varepsilon\frac{A_0}{M},
```

由 (11)–(13)：

```math
\frac{D_0}{H_0}>
rac{499}{1000},
```

并且

```math
\frac{D_0}{H_0}
<
\frac{21}{40}\left(\frac{125}{124}\right)^2
<\frac{267}{500}.
```

因此

```math
\boxed{
\frac{499}{1000}
<
\frac{D_0}{10^{g+1-k}}
<
\frac{267}{500}.
}
\tag{14}
```

---

<a id="a1-03-detail-src-0089-2938-5"></a>
#### 用两个 coprime residues 重写半单位壳层

由 residue kernel：

```math
D_0
=10^k\frac{U_1}{b_1}+\frac{U_2}{b_2}.
```

所以 (14) 等价于

```math
\boxed{
\frac{499}{1000}
<
\frac{
10^kU_1/b_1+U_2/b_2
}{10^{g+1-k}}
<
\frac{267}{500}.
}
\tag{15}
```

此外利用

```math
U_1=10^{r+g+1}(X+W),
\qquad
b_1=10^{2k+r}(1-\varepsilon W),
```

```math
U_2=10^s(Y+Z),
\qquad
b_2=10^{k-g+s-1}(1+\varepsilon Y),
```

可以把 (15) 精确写成

```math
\boxed{
\frac{499}{1000}
<
\frac{X+W}{1-\varepsilon W}
+
\frac{Y+Z}{1+\varepsilon Y}
<
\frac{267}{500}.
}
\tag{16}
```

这比此前 `Delta/L0` 的 `1/2`–`5/6` 窗显著更窄。

---

<a id="a1-03-detail-src-0089-2938-6"></a>
#### 最小第二 surplus `s=1`

若

```math
s=1,
```

则前文已有

```math
s\le k+g,
```

故

```math
y=0,
\qquad
b_2=10^{m_2-1}=10^{k-g},
```

并且

```math
\gcd(z,10)=1.
```

此时

```math
Y=0,
\qquad
Z=\frac z{10},
```

而 (16) 中第一项严格为正。因此

```math
\frac z{10}<\frac{267}{500}=0.534,
```

所以

```math
z\le5.
```

再由 `gcd(z,10)=1`：

```math
\boxed{z\in\{1,3\}.}
\tag{17}
```

两个子核分别满足：

<a id="a1-03-detail-src-0089-2938-7"></a>
#### `z=1`

```math
\boxed{
\frac{399}{1000}
<
\frac{X+W}{1-\varepsilon W}
<
\frac{217}{500}.
}
\tag{18}
```

<a id="a1-03-detail-src-0089-2938-8"></a>
#### `z=3`

```math
\boxed{
\frac{199}{1000}
<
\frac{X+W}{1-\varepsilon W}
<
\frac{117}{500}.
}
\tag{19}
```

所以 `s=1` 已经压成两个明确的第一余量窄窗。

---


<a id="a1-03-detail-src-0089-3470-1"></a>
#### `delta>alpha`

沿用

```math
R_0=1-\alpha,
\qquad
t=1-\delta.
```

因为

```math
R^2=r_1^2+r_2^2+r_3^2>r_2^2,
```

有

```math
R>r_2.
```

除以 `A_0=10^kr_1>0`：

```math
R_0>t.
```

因此

```math
\boxed{\delta>\alpha>0.}
\tag{1}
```

---

<a id="a1-03-detail-src-0089-3470-2"></a>
#### 球面展开直接给 `delta/epsilon>1/2`

前文件已经得到精确恒等式

```math
2(\delta-\alpha)
=\varepsilon+q_0^2+\delta^2-\alpha^2.
\tag{2}
```

由 (1)：

```math
\delta^2-\alpha^2>0.
```

并且

```math
q_0^2>0.
```

所以 (2) 立刻给出

```math
2(\delta-\alpha)>\varepsilon.
```

从而

```math
\delta>\alpha+\frac\varepsilon2>
rac\varepsilon2.
```

即

```math
\boxed{
\frac\delta\varepsilon>\frac12.
}
\tag{3}
```

---

<a id="a1-03-detail-src-0089-3470-3"></a>
#### 真实 carrier gap 的严格半单位下界

真实 gap 为

```math
D_0=A_0-r_2=\delta A_0.
```

自然尺度

```math
H_0=M\varepsilon,
\qquad
M=10^{k+g+1}.
```

而 residue kernel 中

```math
A_0=M+10^k\frac{U_1}{b_1}>M.
```

所以

```math
\frac{A_0}{M}>1.
```

结合 (3)：

```math
\frac{D_0}{H_0}
=
\frac\delta\varepsilon\frac{A_0}{M}
>\frac12.
```

因此

```math
\boxed{
\frac{D_0}{10^{g+1-k}}>\frac12.
}
\tag{4}
```

再用

```math
D_0=10^k\frac{U_1}{b_1}+\frac{U_2}{b_2}
```

得到

```math
\boxed{
\frac{
10^kU_1/b_1+U_2/b_2
}{10^{g+1-k}}
>\frac12.
}
\tag{5}
```

---

<a id="a1-03-detail-src-0089-3470-4"></a>
#### 与既有上界合并

`top-layer.md` 已严格证明

```math
\frac{D_0}{10^{g+1-k}}<\frac{267}{500}.
```

故最终壳层为

```math
\boxed{
\frac12
<
\frac{D_0}{10^{g+1-k}}
<\frac{267}{500}.
}
\tag{6}

```
其宽度仅为

```math
\frac{267}{500}-\frac12
=\frac{17}{500}
=0.034.
```

---

<a id="a1-03-detail-src-0089-3470-5"></a>
#### `s=1` 两个子核的同步加强

当 `s=1` 时已知

```math
y=0,
\qquad z\in\{1,3\}.
```

定义第一 residue contribution

```math
\Phi_1
=\frac{
10^kU_1/b_1
}{10^{g+1-k}}.
```

第二项精确为

```math
\frac{U_2/b_2}{10^{g+1-k}}
=\frac z{10}.
```

由 (6)：

<a id="a1-03-detail-src-0089-3470-6"></a>
#### `z=1`

```math
\boxed{
\frac25<\Phi_1<\frac{217}{500}.
}
\tag{7}
```

<a id="a1-03-detail-src-0089-3470-7"></a>
#### `z=3`

```math
\boxed{
\frac15<\Phi_1<\frac{117}{500}.
}
\tag{8}
```

所以第一余量分别严格位于 `2/5` 与 `1/5` 自然尺度的上侧；这正是 minimal-surplus 六类型核使用的加强版本。

---


<a id="a1-03-detail-src-0089-3758-1"></a>
#### 中心化 residue 坐标

最高层 residue kernel 给出

```math
r_1=10^{g+1}+\frac{U_1}{b_1},
```

```math
r_2=M-\frac{U_2}{b_2},
\qquad
M=10^{k+g+1}.
```

定义自然 gap 尺度

```math
H_0=10^{g+1-k}=M\varepsilon,
\qquad
\varepsilon=10^{-2k}.
```

令

```math
\boxed{
\phi_1=
\frac{10^kU_1/b_1}{H_0},
}
\tag{1}
```

```math
\boxed{
\phi_2=
\frac{U_2/b_2}{H_0}.
}
\tag{2}
```

于是得到三个精确中心化公式：

```math
\boxed{
\frac{10^kr_1}{M}
=1+\varepsilon\phi_1,
}
\tag{3}
```

```math
\boxed{
\frac{r_2}{M}
=1-\varepsilon\phi_2,
}
\tag{4}
```

```math
\boxed{
\frac{r_1}{M}
=10^{-k}(1+\varepsilon\phi_1)
=\sqrt\varepsilon(1+\varepsilon\phi_1).
}
\tag{5}
```

因此

```math
10^kr_1-r_2
=M\varepsilon(\phi_1+\phi_2).
\tag{6}
```

---

<a id="a1-03-detail-src-0089-3758-2"></a>
#### 球面在中心坐标中的精确式

记

```math
\zeta=\frac{r_3}{M},
\qquad
\widehat R=\frac RM.
```

球面

```math
R^2=r_1^2+r_2^2+r_3^2
```

结合 (4)–(5) 给出

```math
\boxed{
\widehat R^2
=(1-\varepsilon\phi_2)^2
+\varepsilon(1+\varepsilon\phi_1)^2
+\zeta^2.
}
\tag{7}
```

另一方面令

```math
A_0=10^kr_1=M(1+\varepsilon\phi_1).
```

则直接展开

```math
\frac{A_0^2-R^2}{M^2}
=
\varepsilon
\left[
2(\phi_1+\phi_2)-1
+\varepsilon(\phi_1^2-2\phi_1-\phi_2^2)
-\varepsilon^2\phi_1^2
\right]
-\zeta^2.
\tag{8}

```
---

<a id="a1-03-detail-src-0089-3758-3"></a>
#### contact height `h`

定义第一 carrier 与球面的正 gap

```math
\boxed{
\mathfrak h=A_0-R>0.
}
\tag{9}
```

则差平方给出

```math
A_0^2-R^2
=\mathfrak h(A_0+R).
```

除以 `M^2`：

```math
\boxed{
\frac{A_0^2-R^2}{M^2}
=
\frac{\mathfrak h}{M}
\left(
1+\varepsilon\phi_1+\widehat R
\right).
}
\tag{10}
```

同时 rational contact 给出

```math
P-R=\theta(R-r_3),
```

而前两块权重表达为

```math
P=(1-\lambda)A_0+\lambda10^{-g}r_2.
```

故

```math
A_0-P
=\lambda(A_0-10^{-g}r_2).
```

因此

```math
\boxed{
\frac{\mathfrak h}{M}
=
\lambda
\left[
(1+\varepsilon\phi_1)
-10^{-g}(1-\varepsilon\phi_2)
\right]
+\theta(\widehat R-\zeta).
}
\tag{11}
```

右端两项均为正。

---

<a id="a1-03-detail-src-0089-3758-4"></a>
#### 正项 excess 分解

把 (10) 代入 (8)，再除以 `epsilon` 并移项：

```math
\begin{aligned}
2(\phi_1+\phi_2)-1
={}&
\frac{\mathfrak h}{M\varepsilon}
\left(
1+\varepsilon\phi_1+\widehat R
\right)\\
&+\frac{\zeta^2}{\varepsilon}\\
&+\varepsilon
\left(
2\phi_1+\phi_2^2-\phi_1^2
\right)\\
&+\varepsilon^2\phi_1^2.
\end{aligned}
```

即

```math
\boxed{
\begin{aligned}
2(\phi_1+\phi_2)-1
={}&
\frac{\mathfrak h}{M\varepsilon}
\left(
1+\varepsilon\phi_1+\frac RM
\right)\\
&+\frac{(r_3/M)^2}{\varepsilon}\\
&+\varepsilon
\left(
2\phi_1+\phi_2^2-\phi_1^2
\right)
+\varepsilon^2\phi_1^2.
\end{aligned}
}
\tag{12}
```

由于 half-gap shell 已给出

```math
0<\phi_1,\phi_2<\frac{267}{500}<1,
```

所以

```math
2\phi_1+\phi_2^2-\phi_1^2
=\phi_1(2-\phi_1)+\phi_2^2>0.
```

结合 (9)、`r_3>0`：式 (12) 右边四行全部为正。

这直接重新证明

```math
\boxed{\phi_1+\phi_2>\frac12.}
```

---

<a id="a1-03-detail-src-0089-3758-5"></a>
#### 四种 excess source

式 (12) 把超过 `1/2` 的 excess 精确分成：

1. **prefix/contact height**
```math
   \frac{\mathfrak h}{M\varepsilon}
   \left(1+\varepsilon\phi_1+R/M\right);
```
   其中 `h` 又按 (11) 分成 `lambda` 前缀混合与 `theta` 第三块接触两项；
2. **third-radius source**
```math
   (r_3/M)^2/\varepsilon;
```
3. **first curvature source**
```math
   \varepsilon\phi_1(2-\phi_1);
```
4. **second curvature source**
```math
   \varepsilon\phi_2^2+\varepsilon^2\phi_1^2.
```

由于 `g\ge1` 时 half-gap sharpening 给出

```math
2(\phi_1+\phi_2)-1<\frac{34}{500}=0.068,
```

上述每个正 source 都自动小于 `0.068`。

---

<a id="a1-03-detail-src-0089-3758-6"></a>
#### 最小双 surplus `r=s=1` 的进一步下推

现在取

```math
r=s=1,
\qquad g\ge1.
```

此前已有

```math
b_2=10^{k-g},
\qquad
z\in\{1,3\},
```

以及

```math
\phi_2=\frac z{10}.
```

此时

```math
\lambda
=\frac{b_2}{b_1 10^{m_2}+b_2}
=\frac1{10b_1+1}.
\tag{13}
```

又

```math
b_1=10^{2k+1}-w<10^{2k+1},
```

所以

```math
\boxed{
\frac\lambda\varepsilon
>
\frac1{100}.
}
\tag{14}
```

由 `g\ge1`、`t<1`：

```math
(1+\varepsilon\phi_1)
-10^{-g}(1-\varepsilon\phi_2)
>1-10^{-g}\ge\frac9{10}.
```

故 (11)、(14) 给出

```math
\frac{\mathfrak h}{M\varepsilon}
>
\frac9{1000}.
\tag{15}
```

同时

```math
R>r_2=M(1-\varepsilon\phi_2),
```

所以

```math
1+\varepsilon\phi_1+\frac RM
>
2-\varepsilon\phi_2
\ge2-
rac3{1000}
>\frac{199}{100}.
```

因此式 (12) 的第一 source 单独已经给出

```math
2(\phi_1+\phi_2)-1
>
\frac9{1000}\frac{199}{100}
>
\frac{17}{1000}.
```

从而

```math
\boxed{
\phi_1+\phi_2>\frac{1017}{2000}=0.5085.
}
\tag{16}
```

于是六类型中的第一余量窗同步加强为：

<a id="a1-03-detail-src-0089-3758-7"></a>
#### `z=1`

```math
\boxed{
\frac{817}{2000}
<\phi_1<\frac{217}{500},
}
\tag{17}
```

即

```math
0.4085<\phi_1<0.434.
```

<a id="a1-03-detail-src-0089-3758-8"></a>
#### `z=3`

```math
\boxed{
\frac{417}{2000}
<\phi_1<\frac{117}{500},
}
\tag{18}
```

即

```math
0.2085<\phi_1<0.234.
```

所以最小双 surplus 的两个 first-residue interval 宽度已经压到约 `0.0255`。

---


来源：`SRC-0089:1482–2310`；`SRC-0089:2401–2856`；`SRC-0089:2938–3401`；`SRC-0089:3470–3696`；`SRC-0089:3758–4194`。原文保全，当前论证以本节为准。

<a id="a1-04"></a>
### A1-04　任意双 surplus 的统一稳定区

**状态：已严格完成。** d=2,g≥1,k+s≥2g+2,k+r≥g+1,N≤min(4g,2k)；原整数严格落入 (0,1)。

依赖：[A1-03](#a1-03)

核对：`a1-joint-surplus`

<a id="a1-04-detail-src-0085-448-1"></a>
#### 命题与新增覆盖

考虑 A1 的最高层 `d=s1-g=2`，令
```math
g,k,r,s\in\mathbf Z_{\ge1},\qquad
m_1=2k+r,\quad m_2=k-g+s\ge1,
\qquad N=\max(r+g+1,s).
```
若
```math
\boxed{
k+s\ge2g+2,\qquad k+r\ge g+1,\qquad
N\le4g,\qquad N\le2k-1,
}
\tag{JS1}
```
则不存在这样的 exact-lift 候选。

这同时允许 `r>=2,s>=2`。例如对每个 `g>=1,k>=2g+1`，整个矩形
```math
\boxed{1\le r\le3g-1,\qquad1\le s\le4g}
\tag{JS2}
```
均为空：此时四条 (JS1) 自动成立。特别地
`g=1,k>=3,r=2,2<=s<=4` 已超出此前分别处理 `r=1` 或 `s=1` 的边界。
这里没有限制 `k` 或 `g` 的绝对上界。

<a id="a1-04-detail-src-0085-448-2"></a>
#### 精确的 joint integer

沿用端点整数
```math
\begin{aligned}
b_1&=10^{2k+r}-w,&a_1&=10^{2k+r+g+1}+x,\\
b_2&=10^{k-g+s-1}+y,&a_2&=10^{2k+s}-z,
\end{aligned}
```
其中 `w,z>=1,x,y>=0`。记
```math
\begin{gathered}
\varepsilon=10^{-2k},\quad H=10^g,\quad t=10^{-r-1},\\
U_1=x+10^{g+1}w,\quad U_2=z+10^{k+g+1}y,\\
A=U_1/10^{r+g+1},\quad B=U_2/10^s,\\
W=w/10^r,\quad Y=10^{k+g+1-s}y,\\
p=A/(1-\varepsilon W),\quad q=B/(1+\varepsilon Y).
\end{gathered}
```
half-gap shell 给出
```math
\tfrac12<p+q<267/500,
\quad 0<W<p<0.534,\quad 0<q<0.534.
\tag{JS3}
```
由于 `Y<=B=q(1+epsilon Y)`，且 (JS1) 强迫 `k>=2`，有
```math
0\le Y<0.535,\qquad 0<\varepsilon\le10^{-4},\qquad0<t\le1/100.
\tag{JS4}
```
定义
```math
\boxed{
\mathcal K=10^N\left(A+B-\frac12-t+\frac tH\right)\in\mathbf Z,
\qquad T=10^{N-r-1}.
}
\tag{JS5}
```
整数性来自 `N>=r+g+1` 和 `N>=s`；具体为
```math
\mathcal K=10^{N-r-g-1}(U_1+1)+10^{N-s}U_2
-10^N/2-10^{N-r-1}.
```

<a id="a1-04-detail-src-0085-448-3"></a>
#### 从原 contact 恒等式估计主项

记 `rho=b3/10^n3`，所以
```math
H/10\le\rho<H,\qquad \rho r_3=a_3/10^{n_3}<1.
```
令
```math
M=10^{k+g+1},\quad \widehat R=\mathcal R/M,\quad
\zeta=r_3/M,\quad \psi=10^{g-1}r_3\in(0,1),
```
以及
```math
\lambda=b_2/Q,\quad\theta=\rho/(HQ),\quad
\delta=\theta/\lambda=\rho/(Hb_2).
```
由 (JS1) 的第一条，
```math
0<\delta<10^{g-k-s+1}\le10^{-g-1}\le1/100.
\tag{JS6}
```
carrier 和球面给 `1-epsilon q<Rhat<1+epsilon p`。此外
```math
\delta\zeta<\frac1{Hb_2M}
\le\varepsilon10^{-g-s}<\varepsilon/H.
\tag{JS7}
```
定义
```math
\Lambda=\frac{\lambda}{t\varepsilon}
=\frac{1+\varepsilon Y}{1-\varepsilon W+t\varepsilon(1+\varepsilon Y)},
\quad F=\frac{1+\varepsilon p+\widehat R}{2},
```
```math
\mathcal B=(1+\varepsilon p)-H^{-1}(1-\varepsilon q)
+\delta(\widehat R-\zeta),\qquad B_0=1-H^{-1}+\delta.
```
则原 contact contribution **精确**为
```math
S_{\rm contact}=2t\Lambda\mathcal B F.
\tag{JS8}
```
由 (JS3)--(JS7)，
```math
|\Lambda-1|<1.1\varepsilon,\quad
|F-1|<0.534\varepsilon,\quad
|\mathcal B-B_0|<0.7\varepsilon,\quad0<B_0<1.01.
```
第三个界可直接由
`0.534(1+0.1+0.01)+0.1=0.69274<0.7` 得到。
对第一个界，分子差除以 `epsilon` 的绝对值不超过
`0.535+0.534+0.01(1+10^-4*0.535)`，分母大于
`1-10^-4*0.534`，商小于 `1.1`。
望远镜展开乘积，得到安全的统一界
```math
\boxed{|\Lambda\mathcal B F-B_0|<4\varepsilon.}
\tag{JS9}
```
例如除以 `epsilon` 后的上界是
```math
1.1(1.01+0.7\cdot10^{-4})(1+0.534\cdot10^{-4})
+0.7(1+0.534\cdot10^{-4})+1.01\cdot0.534<4.
```

<a id="a1-04-detail-src-0085-448-4"></a>
#### 两个主相位之外的余量严格为正

原 positive-excess 恒等式为
```math
2(p+q)-1=S_{\rm contact}+S_{\rm rad}
+\varepsilon f+\varepsilon^2p^2,
\quad f=2p+q^2-p^2,
```
其中
```math
S_{\rm rad}=\zeta^2/\varepsilon=10^{-4g}\psi^2.
```
又 `A+B=p+q+epsilon(Yq-Wp)`。代入 (JS5) 得精确恒等式
```math
\boxed{
\begin{aligned}
\mathcal E
&:=\mathcal K-T\delta-\tfrac12 10^{N-4g}\psi^2\\
&=10^N\left[t(\Lambda\mathcal B F-B_0)
+\varepsilon\left(\frac f2+Yq-Wp\right)
+\frac{\varepsilon^2p^2}{2}\right].
\end{aligned}}
\tag{JS10}
```
这是一次代入，不把各项当成独立方程。

由 (JS3) 有
```math
2p+q^2-3p^2>0.21.
```
证明分为：`p>=1/2` 时 `2p-3p^2>0.212532`；`p<1/2` 时
`q>1/2-p`，故左侧大于 `1/4+p-2p^2>=1/4`。
再由 `W<p,Yq>=0`，得
```math
f/2+Yq-Wp>0.105.
```
因此 (JS9) 中可能为负的项至多消耗 `4t<=0.04`，从而
```math
\mathcal E>\frac{13}{200}10^N\varepsilon>0.
```
上界则丢掉 `-Wp` 与 `-p^2/2`，得到
```math
\frac{\mathcal E}{10^N\varepsilon}
<0.04+0.534+0.534^2/2+0.535\cdot0.534
+10^{-4}\cdot0.534^2/2<2.
```
所以
```math
\boxed{
0<\mathcal K-T\delta-\tfrac12 10^{N-4g}\psi^2
<2\cdot10^{N-2k}.
}
\tag{JS11}
```
在 `k>=2,k+s>=2g+2` 下，(JS11) 本身就成立；后两条稳定性条件
只在下一步将各项压到单位以下时使用。

<a id="a1-04-detail-src-0085-448-5"></a>
#### 完成整数矛盾

不分支地写 contact 上界：
```math
T\delta<10^{N-r-k+g-s}.
```
由于 `N=max(r+g+1,s)`，指数恰为
```math
\max(2g+1-k-s,\ g-r-k).
```
故 (JS1) 的前两条 **同时**保证 `0<T delta<1/10`。
这也准确定位了旧 `r=1` 证明漏掉的条件。
另两条给
```math
\tfrac12 10^{N-4g}\psi^2<\tfrac12,\qquad
2\cdot10^{N-2k}\le\tfrac15.
```
于是 (JS11) 强迫
```math
\boxed{0<\mathcal K<\tfrac1{10}+\tfrac12+\tfrac15=\tfrac45<1,}
```
与 (JS5) 的整数性矛盾。证毕。

<a id="a1-04-detail-src-0085-448-6"></a>
#### 剩余范围与验证

任何 `d=2,g>=1` 候选必须违反 (JS1) 至少一条。尤其 `k>=2g+1`
时必须有
```math
\boxed{r\ge3g\quad\text{或}\quad s\ge4g+1.}
```
这里完整保留了两个 surplus 都可增长的内部区域；没有把最高层、
`g=0` 或其余 `d=-1,0,1` 宣布为空。新的目标应是 (JS11) 中被放大的
contact/radius 项能否与真实第三块的十进制恢复兼容。

核对命令：
证书命令与覆盖见 [统一核对目录](CHECKS.md)。
脚本检查精确代数、全部统一有理常数，并在明确有限的位数网格核对
区域蕴含及漏条件示例；无界覆盖来自上面的证明，不来自网格枚举。
 运行通过：符号恒等式为零，contact 误差系数小于 `4`、
余量系数小于 `2`；`1<=g,k,r,s<=24` 网格中 69,417 个稳定参数元组
通过区域蕴含核对，其中 63,947 个有 `r,s>=2`。这些计数不是解的枚举。


<a id="a1-04-detail-src-0085-717-1"></a>
#### 真实第三块耦合把 curvature 稳定墙推进一格

**状态：已严格完成。** 本节严格扩大 (JS1) 的无界区域；仍只处理
`d=2,g>=1,r,s>=1`。依赖为 §10.2--10.4 的精确恒等式与误差界，
以及真实第三块的 `eta=a3/10^n3<1`、`rho>=10^(g-1)`。

现在只须
```math
\boxed{
k+s\ge2g+2,\qquad k+r\ge g+1,\qquad
N\le4g,\qquad N\le2k
}
\tag{JS13}
```
就已经没有候选。这里最后一条比 (JS1) 放宽一格。
例如 `(g,k,r,s)=(1,2,2,2)` 满足 (JS13)，却不满足 (JS1)；
该例只是新增覆盖区域的参数，不是候选解。

<a id="a1-04-detail-src-0085-717-2"></a>
#### 联合 half-gap 约束收紧余量

写 `C=267/500`、`e0=1/10000` 以及
```math
c_0:=\frac12+\frac1{1-e_0C}.
```
由 `p+q<C` 与 `Y<=q/(1-epsilon q)`，
```math
\begin{aligned}
\frac f2+Yq-Wp+\frac{\varepsilon p^2}{2}
&<p-\frac{p^2}{2}+c_0q^2+\frac{e_0C^2}{2}\\
&\le p-\frac{p^2}{2}+c_0(C-p)^2+\frac{e_0C^2}{2}.
\end{aligned}
```
右侧除最后常数外是 `p in [0,C]` 上的凸二次式，因为二次系数
`c0-1/2>0`。因此其最大值在两个端点之一：
```math
\max\left(c_0C^2,\ C-\frac{C^2}{2}\right).
```
合并 (JS9) 的 `4t<=1/25`，全部有理常数满足
```math
\frac1{25}+\max\left(c_0C^2,\ C-\frac{C^2}{2}\right)
+\frac{e_0C^2}{2}<\frac{47}{100}.
```
这一步使用 `p+q<C` 的联合约束；不能同时把 `p` 与 `q` 取为 `C`。
(JS10) 的正下界保持不变，故有更强的统一余量：
```math
\boxed{
0<\mathcal E<\frac{47}{100}10^{N-2k}.
}
\tag{JS14}
```
此式在 `k>=2,k+s>=2g+2` 时已成立，不需要 (JS13) 的后两条。

<a id="a1-04-detail-src-0085-717-3"></a>
#### contact 和 radius 来自同一个第三块

记
```math
u:=\rho/H\in[1/10,1),\qquad \eta:=a_3/10^{n_3}\in[1/10,1).
```
真实尾部满足
```math
\boxed{\psi=\frac\eta{10u}<\frac1{10u}.}
```
令 `E=max(2g+1-k-s,g-r-k)`。§10.5 的 contact 估计保留
`rho/H` 后实际上是
```math
T\delta\le u10^E\le\frac u{10},
```
第一处允许等号是因为 `b2>=10^(k-g+s-1)`；不需要假设 `y>0`。
(JS13) 另给 radius 项不超过 `psi^2/2`。
于是两项不能同时独立地逼近 `1/10` 与 `1/2`，而是
```math
T\delta+\tfrac12 10^{N-4g}\psi^2
<\frac u{10}+\frac1{200u^2}\le\frac{51}{100}.
\tag{JS15}
```
最后一个界对整个 `u in [1/10,1]` 直接由因式分解验证：
```math
\frac{51}{100}-\frac u{10}-\frac1{200u^2}
=\frac{(10u-1)(-2u^2+10u+1)}{200u^2}\ge0.
```
后一因子在该区间严格正；前一个严格小于号来自 `eta<1`。

<a id="a1-04-detail-src-0085-717-4"></a>
#### 整数矛盾与新边界

(JS13) 的 `N<=2k` 与 (JS14)--(JS15) 最终给
```math
\boxed{0<\mathcal K<\frac{51}{100}+\frac{47}{100}
=\frac{49}{50}<1.}
```
与 (JS5) 矛盾，证明 (JS13)。

因此整个无界矩形现在扩大为
```math
\boxed{k\ge2g,\qquad 1\le r\le3g-1,\qquad 2\le s\le4g}
\tag{JS16}
```
为空；在 `k>=2g+1` 时仍允许 `s=1`。这是实际扩大了关闭范围，
没有关闭 `N>4g` 的 amplified-radius 区，也没有处理全部近接触区域。
对于首个 radius 壳层 (JS12)，(JS14) 还把误差收紧为
```math
\boxed{0<\mathcal K-5\psi^2<\frac{1047}{100000}}
\qquad(k\ge2g+2,\ N=4g+1),
```
仍是必要条件，不能据此声称该壳层为空。

核对使用同一个脚本：
证书命令与覆盖见 [统一核对目录](CHECKS.md)。
脚本以精确有理数检查凸二次式的端点界和 (JS15) 的因式分解，
并只把有限位数网格用作区域回归核对。无界结论来自上面的推导。


来源：`SRC-0085:448–683`；`SRC-0085:717–831`。原文保全，当前论证以本节为准。

<a id="a1-05"></a>
### A1-05　首 radius 壳与 contact 壁的严格子片

**状态：已严格完成。** N=4g+1 的上 significand；k+r=g 的低 significand；其余保留。

依赖：[A1-04](#a1-04)

核对：`a1-joint-surplus`

<a id="a1-05-detail-src-0085-684-1"></a>
#### 首个放大壳层只剩五个 radius 窗口

**状态：已严格完成（必要条件，不是空性）。** 在
```math
k\ge2g+2,\qquad N=\max(r+g+1,s)=4g+1
```
下，(JS11) 仍然成立，而且
```math
T\delta<1/100,\qquad
\mathcal E<2\cdot10^{N-2k}\le1/500.
```
因此
```math
\boxed{
\mathcal K\in\{1,2,3,4,5\},\qquad
0<\mathcal K-5\psi^2<3/250,
}
\tag{JS12}
```
即
```math
\frac{\mathcal K}{5}-\frac3{1250}<\psi^2<\frac{\mathcal K}{5}.
```
证明只需将 `N=4g+1` 代入 (JS11)：contact 指数不超过 `-2`，
curvature 指数不超过 `-3`，再由 `0<psi<1` 与 `K` 的整数性收束。

这给出了一个具体的新接口：首个未关闭的 squared-tail 壳层不是任意
相位，而是上述五个固定窗口，且 `psi=10^(g-1)a3/b3` 必须来自真实既约
第三块。仍须把窗口与 exact decimal recovery 联立；仅有五个窗口不构成矛盾。


<a id="a1-05-detail-src-0085-832-1"></a>
#### 首个 radius 壳层的 upper-significand 子支关闭

**状态：已严格完成（条件空性及剩余走廊）。** 本节只考虑
```math
k\ge2g+2,\qquad N=4g+1,\qquad g\ge1.
```
依赖 §10.7--10.8。令 `u=rho/H`、`eta=a3/10^n3`，则
```math
\mathcal K\in\{1,2,3,4,5\},\qquad
T\delta\le\frac u{100},\qquad
0<\mathcal E<\frac{47}{100000},\qquad
\psi=\frac\eta{10u}.
```
所以对真实第三块有严格必要不等式
```math
\boxed{
\mathcal K
<\frac u{100}+\frac1{20u^2}+\frac{47}{100000}.
}
\tag{JS17}
```

右边是 `u>0` 上的凸函数。在 `[c,1]` 上只须检查两个端点。
取 `c=28/125`，其两端精确上界为
```math
\frac{9792183}{9800000}<1,\qquad
\frac{6047}{100000}<1.
```
故 (JS17) 与 `K>=1` 矛盾，得到整个子支
```math
\boxed{k\ge2g+2,\ N=4g+1,\ \rho/H\ge28/125
\Longrightarrow\varnothing.}
\tag{JS18}
```
这覆盖无界 `g,k,r,s,n3`，不依赖有限枚举。

按 `K` 分别对同一个凸函数检查端点，还得到如下严格剩余走廊：

| `K` | 候选必需的 `u=rho/H` 上界 |
|---:|---:|
| 1 | `u<28/125` |
| 2 | `u<791/5000` |
| 3 | `u<323/2500` |
| 4 | `u<1119/10000` |
| 5 | `u<20003/200000` |

每行的有理端点代入 (JS17) 右侧严格小于相应的 `K`；
另一端 `u=1` 的值始终为 `6047/100000<K`。各行并非完整空性，
因为真实尾窗只要求 `u>=1/10`，仍与这些上界相交。

此外精确 `K=T delta+5psi^2+E` 给出
```math
\boxed{
20u^2\left(K-\frac u{100}-\frac{47}{100000}\right)
<\eta^2<20Ku^2.
}
\tag{JS19}
```
例如 `K=5` 时，左边作为 `u in [1/10,1]` 的函数严格递增：
其导数为
`40u(5-47/100000)-(3/5)u^2>0`。
取 `u=1/10` 得
```math
\eta^2>\frac{499853}{500000}
>\left(\frac{99985}{100000}\right)^2.
```
因此这个最末窗口已压为
```math
\boxed{
\frac1{10}\le u<\frac{20003}{200000},\qquad
\frac{99985}{100000}<\eta<1,\qquad n_3\ge4.
}
\tag{JS20}
```
`n3>=4` 来自 `n3<=3` 时 `a3/10^n3<=999/1000`，而不是高度猜测。
这里没有尾长上界；(JS20) 仍是无界 endpoint corridor，不能声称
`K=5` 或首个 radius 壳层全部关闭。

核对命令与 §10.8 相同；脚本逐一以精确有理数验证端点、
`K=5` 的导数下界及 `eta` 的平方比较。有限位数网格仍仅是回归核对。


<a id="a1-05-detail-src-0085-832-2"></a>
#### 必要 phase 系统的兼容点：不能只靠窗口完成关闭

**状态：失效/降级（仅用 phase 窗口加尾既约性关闭的路线不足）。**
取 `g=1,k=4,r=3,s=1,N=5,K=1`，真实既约第三块
```math
(a_3,b_3)=(5591,12511),\qquad
n_3=4,\quad m_3=5,
```
给出 `u=12511/100000`、`eta=5591/10000`、`psi=5591/12511`。
`s=1` 的真实第二块可取 `b2=1000`，此时 `T delta=u/100`。
精确有理数核对满足
```math
\frac{13}{200000}
<1-\frac u{100}-5\psi^2
<\frac{47}{100000}.
```
故连 §10.4 的严格余量下界、§10.8 的上界、真实尾位数及既约性
一起也不能排除这个 phase 兼容点。

还可取 `w=287,z=1,U1=40010,x=11310`，得到既约前两块
```math
(a_1,b_1)=(10^{13}+11310,10^{11}-287),\qquad
(a_2,b_2)=(10^9-1,1000),
```
它们有正确的位数层和联合整数 `K=1`。
**这不是 exact-lift 解**：其拼接比值的平方严格不等于三个比值平方和，
脚本对此作精确分数核对。该点只用于表明尚缺的 full contact/sphere
等式不可被当前窄 phase 不等式替代。下一步必须把 (JS10) 的精确余量
与实际前两块联立，或增加独立的 denominator/decimal-recovery obstruction。


<a id="a1-05-detail-src-0085-832-3"></a>
#### 首个 contact 放大边界：endpoint 归约与剩余系统

本节的统一假设为 `k+r=g,k+s>=2g+2,N<=2k`。
它自动给 `g>=3r+2,k>=4,N=s`；记 `nu=s-r-1`。
当前严格结果先关闭 `u<=529/1000`，余核必须 `u>529/1000`、
`y=0,K=1,z=1 mod10`。以下表格区分已排除区与必须继续恢复的系统。

| 深度分支 | 当前有效归约 | 仍须恢复的条件 |
| --- | --- | --- |
| 全部候选 | `nu+1<=v5(b3)<=nu+m3`，`max(v2(w),nu)<v2(b3)<nu+m3` | (JS24)--(JS29)、(JS35) 与原 word/sphere |
| `(2S):v2(w)<nu`；非 `2-near-beta`、非 `5-beta` | 仅 `d2,d5<=g,max(d2,d5)=g`，相对 gap 为 (JS34) | 精确 balanced cancellation 与整数恢复 |
| `(2S)`、`5-beta:d5=m3` | `13<=g<26r+6,g<d2<11g/6,m3=3d2-1` | (JS38)--(JS40) 的三项 cancellation；相对盒内未枚举 |
| `(2S)`、`2-near-beta:d2=m3-1` | `5-low:g<=24r-4`；`5-balanced:g<=24r+4`；`5-high:d5<6g` | (JS41)--(JS42) 的真实加法 word、prefix divisor 和 sphere |
| `v2(w)>=nu` | `r>=13`，并满足真实 `2^(g+1)<(267/500)10^r` | (JS35)--(JS37) 的三分裂；不沿用 (2S) 的 regular 排除 |
| `v2(w)=nu,d2=d5=d<g` | `1<=g-d<=3r` | (JS43) 的整数 gap；该相对 gap 内仍待证 |

这里 `d2=v2(b3)-nu,d5=v5(b3)-nu`。`5-beta` 的 `H_sph+y3` 深度
以及 `2-near-beta` 的 `v2(H_sph-y3)=1` 都由精确恒等式决定，
不能只凭模二同余选择符号。下面先保留简单区间证明作为中间步骤，再给加强范围、
完整 endpoint 方程和各条深度推导。

**状态：已严格完成。** 本节不要求 (JS13) 的 `k+r>=g+1`，
而覆盖此前稳定区之外的 `k+r=g` 接触边界。命题范围为
```math
\boxed{
\begin{gathered}
d=2,\quad g,k,r,s\ge1,\quad k\ge2,\quad k+r=g,\\
k+s\ge2g+2,\qquad
N=\max(r+g+1,s)\le\min(4g,2k),\\
\frac19\le u:=\rho/H\le\frac12.
\end{gathered}}
\tag{JS21}
```
这些条件下不存在 exact-lift 候选。

依赖审计：§10.2--10.4 的整数构造、contact 误差与正余量下界，
以及 §10.8 的 (JS14)，只使用 `k>=2,k+s>=2g+2`。
原 `k+r>=g+1` 仅用于 §10.5 将 `T delta` 压到 `1/10` 以下，
因此本节可用新的 `T delta<=u` 上界替代；不是把旧定理的假设静默删去。
`m2=k-g+s=s-r>=1` 也由 `k+s>=2g+2` 自动保证。

在 (JS21) 下 contact 指数为
```math
E=\max(2g+1-k-s,g-r-k)=0,
```
故 `T delta<=u`。仍由真实第三块的 `psi=eta/(10u)` 与 `eta<1`，
```math
T\delta+\tfrac12 10^{N-4g}\psi^2
<u+\frac1{200u^2}.
```
这个凸函数在 `[1/9,1/2]` 上的最大值出现在端点，且
```math
\frac19+\frac{81}{200}=\frac{929}{1800}<\frac{13}{25},
\qquad
\frac12+\frac1{50}=\frac{13}{25}.
```
因此结合 (JS14) 的 `N<=2k`，
```math
\boxed{0<\mathcal K<\frac{13}{25}+\frac{47}{100}
=\frac{99}{100}<1.}
```
整数矛盾证明 (JS21)。

这确实覆盖非空的无界参数形状：对任意整数
```math
\boxed{
r\ge1,\qquad g\ge3r+2,\qquad k=g-r,\qquad
 g+r+2\le s\le2g-2r,
}
\tag{JS22}
```
以及 `1/9<=rho/H<=1/2`，全部为空。
因为此时 `N=s`、`k+s>=2g+2`、`N<=2k<4g` 且 `k>=2`。
例如每个 `r>=1` 都可取 `g=3r+2,k=2r+2,s=4r+4`；
其 `k+r=g` 违反此前稳定区假设，故是新增覆盖。

contact 边界的 `u<1/9` 与 `u>1/2`、更深的 `k+r<g`，
以及其他 amplified source 区仍为 **待证**。
验证脚本用精确有理数检查两个端点和 `99/100` 的整数预算，
并在有限位数网格回归核对 (JS22) 的范围蕴含；无界覆盖来自本节证明。


<a id="a1-05-detail-src-0085-832-4"></a>
#### 同一 contact 边界的范围蕴含给出更强关闭

上述位数条件之间还有额外耦合，故 (JS21) 的 `u` 范围并非最终界。
由 `k=g-r` 与 `k+s>=2g+2`，
```math
s\ge g+r+2>r+g+1,
```
因此 `N=s`。再由 `N<=2k=2g-2r`，得到
```math
\boxed{g\ge3r+2,\qquad g+r\ge6,\qquad
N-4g\le-2(g+r)\le-12.}
```
所以真实 radius 项实际上严格小于 `1/(2*10^12)`，不需要用
`1/(200u^2)` 的粗上界。

于是完整命题可加强为
```math
\boxed{
\begin{gathered}
d=2,\quad g,k,r,s\ge1,\quad k+r=g,\\
k+s\ge2g+2,\qquad N\le2k,\qquad
\frac1{10}\le\rho/H\le\frac{529}{1000}
\end{gathered}
\Longrightarrow\varnothing.
}
\tag{JS23}
```
`k>=2` 与 `N<=4g` 都已由这些条件自动推出。
(JS14) 与 `T delta<=u` 给
```math
0<\mathcal K
<\frac{529}{1000}+\frac{47}{100}+\frac1{2\cdot10^{12}}<1,
```
证明 (JS23)。

因此 (JS22) 所给无界参数族在整个 `1/10<=rho/H<=529/1000`
范围已经关闭，包含原 (JS21) 未覆盖的 `u<1/9`。
首个 contact 边界只需继续研究 `rho/H>529/1000` 或 `N>2k`；
更深 contact 放大区 `k+r<g` 仍待证。


<a id="a1-05-detail-src-0085-832-5"></a>
#### 剩余 contact 边界已经是一个精确 endpoint corridor

**状态：已严格完成（必要条件）。** 仍只考虑 `k+r=g`、
`k+s>=2g+2`、`N<=2k`。上面的范围蕴含给
```math
N=s\le2g-2r\le k+g.
```
因此 [top-layer.md](#a1-02) §4 的短第二 surplus endpoint kernel
强迫 `y=0`，从而
```math
b_2=10^{k-g+s-1}=10^{s-r-1}=T,\qquad Y=0,
\qquad \boxed{T\delta=u.}
```
这次 contact phase 并非仅有上界，而是精确等于 `rho/H`。
由 `0<u<1`、radius `<1/(2*10^12)` 与 (JS14)，
```math
0<K<1+\frac{47}{100}+\frac1{2\cdot10^{12}}<2,
```
故整数 `K=1`。因此整个剩余系统必须满足
```math
\boxed{
K=1,\qquad
0<1-u-\tfrac12 10^{N-4g}\psi^2
<\frac{47}{100}10^{N-2k}.
}
\tag{JS24}
```
特别地
```math
u>1-\frac{47}{100}10^{N-2k}-\frac1{2\cdot10^{12}}.
```
当 `N<2k` 时，第三分母 significand 更贴近上端点。

联合整数式还给出一个独立的十进制尾数条件。由于
`s-r-g-1>=1`，(JS5) 中除 `U2=z` 外的每项都是 `10` 的倍数，故
```math
\boxed{z\equiv K\equiv1\pmod{10}.}
```
这没有造成矛盾；应把 `K=1`、`Y=0`、(JS24) 和真实既约第三块
一起送入精确恢复。该 endpoint corridor 仍为 **待证**。


<a id="a1-05-detail-src-0085-832-6"></a>
#### 公共模 9 条件不能自动关闭这个 endpoint corridor

**状态：已严格完成（局部过滤和不充分性审计）；完整空性仍待证。**
本段接入 [global-framework.md](RESEARCH.md#common-model)（原始记录 SRC-0199）
的公共分母模 `9` 必要条件，不把该条件当作充分条件。

在 `y=0` 下 `b2=10^(s-r-1)=1 mod9`。若 `w=0 mod3`，则
`b1=1 mod3`。此时：

- 若 `3|b3`，原既约性使第三比值成为唯一具有负 `3`-adic 赋值的比值，
  球面强迫拼接分母被 `3` 整除；但 `beta=b1+b2+b3=2 mod3`，矛盾。
- 若 `b3=1 mod3`，公共模 `9` 条件要求
  `(1-w)^2+1+b3^2=0 mod9`，等价于
```math
  \boxed{b_3\equiv w+4\pmod9.}
```
  `w=0,3,6 mod9` 分别只留下 `b3=4,7,1 mod9`。

从联合整数 `K=1` 另有
```math
z\equiv6-x-w\pmod9,\qquad
 a_1\equiv1+x,\quad a_2\equiv x+w+4\pmod9.
```
因此在 `w=0 mod3` 时 `a1=a2 mod3`；这是新的联立条件，但不会
使所有模 `9` 或模 `27` 类为空。一个精确核对点为
```math
\begin{gathered}
g=5,\ k=4,\ r=1,\ s=N=8,\ x=0,\ w=3,\ z=20999991,\\
(a_1,b_1)=(10^{15},10^9-3),\quad
(a_2,b_2)=(10^{16}-20999991,10^6),\\
(a_3,b_3)=(1,599974),\quad n_3=1,\quad m_3=6.
\end{gathered}
```
三块均既约，有联合整数 `K=1`，且 `u=599974/10^6>529/1000`。
它满足 (JS24) 的正余量上下界。分母模 `9` 类为 `(7,1,7)`，通过
公共模 `9` 条件；拼接比值在约去公共 `3` 因子后以及三个比值的
模 `27` 类分别为
```math
R\equiv0,\qquad (r_1,r_2,r_3)\equiv(13,25,4)\pmod{27},
```
并有 `13^2+25^2+4^2=0 mod27`。
**该点不是 exact-lift 解**：脚本精确核对其完整平方等式非零。
它只证明当时的必要 phase / 位数 / 既约条件连同这一级模 `9/27`
过滤仍有允许类，不能据此把整个 corridor 宣布为空。该点
`v5(b3)=0`；它被下方新增的无界 `5`-深度条件排除，因此不是最新
全部必要条件的允许点。

消去 `z` 后，真正仍须关闭的独立精确方程可以写成
```math
\begin{aligned}
z&=1-10^{s-r-g-1}(x+10^{g+1}w+1)
  +5\cdot10^{s-1}+10^{s-r-1},\\
\alpha&=a_1 10^{2k+s+\ell}+a_2 10^\ell+a_3,\\
\beta&=b_1 10^{s-r+g+\ell}+b_2 10^{g+\ell}+b_3,
\end{aligned}
```
以及
```math
\boxed{
\alpha^2(b_1b_2b_3)^2
=\beta^2\left[(a_1b_2b_3)^2+(a_2b_1b_3)^2+(a_3b_1b_2)^2\right].
}
\tag{JS25}
```
这里 `ell=n3`、`k=g-r`，`a1,b1,a2,b2` 仍按原 endpoint 形状恢复，
还须同时保持各块的位数、正性、既约性和 (JS24)。
(JS25) 不可用较宽 phase 不等式代替；模 `9/27` 的局部允许类也不证明
(JS25) 在有理数上存在解。


<a id="a1-05-detail-src-0085-832-7"></a>
#### 5-adic 深度的两个无界子支关闭

**状态：已严格完成（条件空性及高深度剩余范围）。**
仍只考虑 `k+r=g,k+s>=2g+2,N<=2k` 的首 contact endpoint。
为避免与第三尾长 `ell=n3` 混淆，第二分母的指数记为
```math
\nu:=s-r-1,\qquad b_2=10^\nu,\qquad
\nu\ge g+1\ge3r+3.
```
任意完整候选必须满足
```math
\boxed{\nu+1\le e_3:=v_5(b_3)\le\nu+m_3.}
\tag{JS26}
```
特别地，整个 `v5(b3)<=nu` 的无界子支已关闭；这没有关闭全部高深度尾部。

先证明第一分母更浅。由 `W<p<267/500`，
```math
1\le w<10^r<5^{3r+3}.
```
最后一个严格界可直接写成 `5^(3r+3)/10^r=125*(25/2)^r>1`。
又 `k=g-r>=2r+2`，所以 `2k+r>=5r+4>3r+3`，故
```math
v_5(w)<3r+3\le\nu,\qquad v_5(w)<2k+r.
```
对 `b1=10^(2k+r)-w` 使用不同赋值相减，得到
```math
\boxed{v_5(b_1)=v_5(w)<\nu.}
```
前两分母拼接还精确满足
```math
Q=b_1 10^{s-r}+b_2=b_2(10b_1+1),\qquad v_5(Q)=\nu.
```

令
```math
q_{\rm lcm}:=\operatorname{lcm}(b_1,b_2,b_3),\qquad
 y_i:=a_iq_{\rm lcm}/b_i\in\mathbf Z,
```
完整候选的整数球面半径记为
```math
H_{\rm sph}:=q_{\rm lcm}\alpha/\beta\in\mathbf Z_{>0}.
```
整数性来自 `H_sph^2=sum(y_i^2)`：整数的有理平方根必为整数。
因此同时有
```math
H_{\rm sph}^2=y_1^2+y_2^2+y_3^2,\qquad
\boxed{q_{\rm lcm}\alpha=H_{\rm sph}\beta.}
```

若 `e3<nu`，则 `v5(q_lcm)=nu`，第二分母是唯一最深分母。
原既约性保证 `y2` 为 `5` 单位，`y1,y3` 被 `5` 整除，故
`H_sph` 为 `5` 单位。但
```math
\beta=Q10^{m_3}+b_3,
\qquad v_5(\beta)=e_3<\nu,
```
所以 `q_lcm alpha` 的赋值至少为 `nu`，`H_sph beta` 的赋值却为
`e3`，矛盾。这关闭 `e3<nu`。

若 `e3=nu`，则 `b3` 被 `5` 整除，原既约性强迫 `a3` 为 `5` 单位。
由于 `alpha=C10^ell+a3`、`ell>=1`，`alpha` 也是 `5` 单位。
此时 `v5(q_lcm)=v5(beta)=nu`，拼接整数恒等式强迫 `H_sph` 为 `5` 单位。
然而 `y1=0 mod5`，`y2,y3` 都为 `5` 单位；两个非零平方模 `5` 的和
只能属于 `{0,2,3}`，不能等于 `H_sph^2 in {1,4}`。矛盾。
这独立关闭等深的无界子支 `e3=nu`，给出 (JS26) 的严格下界。

最后若 `e3>nu`，第三分母是唯一最深分母，故 `H_sph` 为 `5` 单位。
同时 `alpha` 为 `5` 单位，所以整数拼接恒等式要求
`v5(beta)=v5(q_lcm)=e3`。若 `e3>nu+m3`，则
`v5(beta)=nu+m3<e3`，矛盾。这给出上界 `e3<=nu+m3`。
**上界等号不能删去。** 在 `e3=nu+m3` 时令
```math
B:=b_3/5^{e_3},\qquad
A:=2^{\nu+m_3}(10b_1+1).
```
二者都是 `5` 单位，`beta/5^e3=A+B`。球面模 `5` 给
`H_sph/y3=+1` 或 `-1`；拼接等式的 `+1` 分支会要求 `A=0 mod5`，
不可能，而 `-1` 分支允许必要条件
```math
\boxed{2B+A\equiv0\pmod5.}
\tag{JS27}
```
这时 `A+B=-B mod5` 仍为单位，故本轮赋值论证没有关闭该 resonance。

先前的模 `9/27` 允许点 `(a3,b3)=(1,599974)` 有 `v5(b3)=0`，
被 (JS26) 排除。这只说明新 `5`-深度条件严格加强了独立过滤，
不证明高深度尾部为空。最新剩余核心应联立 (JS24)--(JS27)、
各块十进制恢复与完整平方方程 (JS25)。

验证脚本以精确整数检查指数范围、第一分母赋值关系、模 `5` 两单位
平方和的全部 16 个 residue pairs、以及等深上界的 `-1` 允许分支。
无界覆盖来自上述赋值证明，不来自参数枚举。


<a id="a1-05-detail-src-0085-832-8"></a>
#### 完整 word 与 sphere 联立的 5-adic gap 形状

**状态：已严格完成（无界必要形状，非全局空性）。**
接续 (JS26)，写 `d5=e3-nu>=1`、`m3=n3+g`。
在非 beta-resonance 区 `e3<nu+m3`（即 `d5<m3`）中，候选必须落入
```math
\boxed{
\begin{array}{c|c}
d_5<g&n_3=2d_5\\
d_5>g&m_3=3d_5\\
d_5=g&n_3\le2g
\end{array}}
\tag{JS28}
```
每一行以外的对应参数子支已经严格关闭；覆盖无界位数参数。

证明如下。第三分母最深时 `y3,H_sph` 都为 `5` 单位，而
```math
v_5(y_2)=d_5,\qquad v_5(y_1)>d_5.
```
非 beta-resonance 时 `beta/b3=1 mod5`，并且 `alpha/a3=1 mod5`，
故 `H_sph/y3=1 mod5`。于是 `H_sph+y3` 为单位；球面差平方精确给
```math
\boxed{v_5(H_{\rm sph}-y_3)=2d_5.}
```
这里右侧平方和中第二坐标更浅，故没有取消。

设 `A12=a1 10^n2+a2`，其为 `5` 单位。完整 word identity 与
`q_lcm a3=y3 b3` 相减得到
```math
\boxed{
(H_{\rm sph}-y_3)\beta
=q_{\rm lcm}A_{12}10^{n_3}-y_3Q10^{m_3}.
}
\tag{WG5}
```
左端赋值为 `nu+3d5`，右端两项赋值分别为
`nu+d5+n3` 与 `nu+n3+g`。若 `d5<g`，第一项更浅，故
`nu+3d5=nu+d5+n3`，得到 `n3=2d5`；若 `d5>g`，第二项更浅，
故 `nu+3d5=nu+m3`，得到 `m3=3d5`。

若 `d5=g`，右端两项等深，故 `nu+3g>=nu+g+n3`，即 `n3<=2g`。
更精确地，令
```math
C_5:=q_{\rm lcm}/5^{e_3},\qquad Q_5:=Q/5^\nu,
```
其单位差必须满足
```math
\boxed{
v_5\left(C_5A_{12}2^{n_3}-y_3Q_5 2^{m_3}\right)=2g-n_3.
}
```
`n3<2g` 时必须有正深度 cancellation；`n3=2g` 时额外深度可以为零。
不能把等深本身当作已经发生非平凡消去。

上界 beta-resonance `e3=nu+m3` 必须单列。由 (JS27) 的负号分支，
`H_sph=-y3 mod5`，因此 `H_sph-y3` 为单位，球面反而给
```math
\boxed{v_5(H_{\rm sph}+y_3)=2m_3.}
\tag{JS29}
```
对应的精确加法 word identity 是
```math
(H_{\rm sph}+y_3)\beta
=q_{\rm lcm}A_{12}10^{n_3}+y_3Q10^{m_3}+2q_{\rm lcm}a_3.
```
它有三个项，不能混入 (WG5) 的两项不等深论证。
(JS28)--(JS29) 均保留了真实十进制 word，而不是只使用较宽的 phase 窗口；
各允许形状仍须满足 (JS24)--(JS27) 和完整恢复，尚未证明全部为空。


<a id="a1-05-detail-src-0085-832-9"></a>
#### 较浅第一分母的 2-adic 深度与两个跨素数子支关闭

**状态：已严格完成（显式条件下的无界空性）；其他深度仍待证。**
在同一首 contact endpoint 中，还可独立利用 `2`-adic word 与 sphere。
第一分母总满足
```math
v_2(b_1)=v_2(w),
```
因为 `w<10^r<2^(4r)`、`2k+r>=5r+4>4r`。
本段明确添加条件
```math
\boxed{v_2(w)<\nu.}
\tag{2S}
```
对 `1<=r<=12`，它由已有位数范围自动保证：
```math
\frac{2^{3r+3}}{10^r}=8(4/5)^r
\ge\frac{2^{39}}{10^{12}}>\frac{267}{500},
```
故 `w<(267/500)10^r<2^(3r+3)<=2^nu`。
`r>12` 时仍可使用 (2S)，但不能自动假设它成立。

在 (2S) 下，完整候选必须满足
```math
\boxed{\nu+2\le e_{3,2}:=v_2(b_3)<\nu+m_3.}
\tag{JS30}
```
证明 `e3,2<nu` 的空性与上面的 `5`-adic unique-max 赋值论证相同。
若 `e3,2=nu`，`y1` 为偶数，`y2,y3` 为奇数，其平方和 `=2 mod4`，
不可能是整数平方。若 `e3,2=nu+1`，第三坐标最深，`H_sph,y3` 均奇，
`v2(y2)=1`、`v2(y1)>1`；球面差平方右端赋值恰为 `2`，但两个奇数
平方之差必被 `8` 整除。矛盾。因此 `e3,2>=nu+2`。

此时第三分母是唯一最深者，`H_sph` 与 `alpha` 均奇，整数 word 要求
`v2(beta)=e3,2`。若 `e3,2>nu+m3`，前缀分母项更浅，矛盾；若
`e3,2=nu+m3`，两个相同赋值的奇单位项相加使 `beta` 更深，也矛盾。
这次上界是严格的；它与允许负号 unit resonance 的 `5`-adic 上界不同。

联立 (JS26) 与 (JS30)，`b3` 至少被
`2^(nu+2)5^(nu+1)=20*10^nu` 整除。因此
```math
\boxed{m_3\ge\nu+2,\qquad n_3\ge\nu-g+2\ge3.}
```
这个真实十进制高度下界在后面的 sign split 中不可遗漏。

令 `d2=e3,2-nu>=2`。因 `v2(y2)=d2<v2(y1)`，球面右端
`y1^2+y2^2` 的赋值恰为 `2d2`。仍使用完整两项 word identity (WG5)，
但这次其左端 `beta` 的赋值为 `nu+d2`；两项比较给：

- 若 `d2<g`，`v2(H_sph-y3)=n3>=3`；于是 `v2(H_sph+y3)=1`，
  得 `n3=2d2-1`。
- 若 `d2=g`，右端两项等深，故 `v2(H_sph-y3)>=n3>=3`；
  同理 `v2(H_sph+y3)=1`，得到 `n3<=2g-1`。
- 若 `d2>g`，`v2(H_sph-y3)=m3-d2>=1`。当 `m3-d2>=2`，
  另一个因子赋值为 `1`，得 `m3=3d2-1`；当 `m3-d2=1`，
  必须单列 near-beta 边界 `d2=m3-1`，此时正因子的赋值为 `2d2-1`。

因此严格必要形状为
```math
\boxed{
\begin{array}{c|c}
d_2<g&n_3=2d_2-1\\
d_2=g&n_3\le2g-1\\
d_2>g&m_3=3d_2-1\ \text{或}\ d_2=m_3-1
\end{array}}
\tag{JS31}
```

把这与 (JS28) 的独立 `5`-adic 形状联立，立即得到两个无界子支关闭：
```math
\boxed{
\begin{aligned}
d_2<g,\ d_5<g&\Longrightarrow\varnothing,\\
g<d_2\le m_3-2,\quad g<d_5<m_3&\Longrightarrow\varnothing.
\end{aligned}}
\tag{JS32}
```
第一行同时要求 `n3` 为奇数与偶数；第二行同时要求
`m3=2 mod3` 与 `m3=0 mod3`。证明依赖完整 word、sphere、真实位数
以及 (2S)，不来自有界枚举。

混合高低深度、`d2=g` 或 `d5=g`、`5`-adic beta-resonance `d5=m3`、
`2`-adic near-beta 边界 `d2=m3-1`，以及违反 (2S) 的第一分母深区，
都仍为 **待证**；(JS32) 不能被扩大为整个 contact endpoint 已关闭。


<a id="a1-05-detail-src-0085-832-10"></a>
#### Regular 高深度（含 mixed）全部排除

**状态：已严格完成。** 在 (2S) 下，去掉两个须单列的边界
`d2=m3-1` 与 `d5=m3` 后，(JS28)、(JS31) 还能严格加强 (JS32)：
```math
\boxed{
d_2\ne m_3-1,\quad d_5<m_3
\quad\Longrightarrow\quad
 d_2\le g,\quad d_5\le g,\quad\max(d_2,d_5)=g.
}
\tag{JS33}
```

若 regular `d2>g`，则 `m3=3d2-1>=3g+2`，即 `n3>=2g+2`。
这与 `d5<=g` 的 `n3<=2g` 冲突；而 `d5>g` 已由 regular double-high
的模 `3` 冲突排除。反向若 regular `d5>g`，则 `m3=3d5>3g`、
`n3>2g`，与 `d2<=g` 的 `n3<=2g-1` 冲突，其余再次由 double-high
排除。因此两个深度都不高于 `g`；double-low 又要求至少一侧等于 `g`。

这里 `H_sph-y3` 或 `H_sph+y3` 的赋值完全来自精确 word gap 与
sphere 差平方；没有用模 `2` 同余替代正负因子的实际赋值。
(JS33) 不适用于上面两个不同号边界。

<a id="a1-05-detail-src-0085-832-11"></a>
#### Balanced regular 剩余压到有界相对 gap

**状态：已严格完成（条件空性和相对 gap 压缩）。**
仍加 (2S)，并处于 (JS33) 的 regular 部分。则剩余必须满足
```math
\boxed{
\begin{array}{c|c}
d_2=g,\ d_5<g&1\le g-d_5\le3r\\
d_5=g,\ d_2<g&1\le g-d_2\le3r-1\\
d_2=d_5=g&2g-3r\le n_3\le2g-1
\end{array}}
\tag{JS34}
```
各行上界以外的无界子支已关闭；这些是相对参数界，不是所有前缀的
全局有限盒。

证明使用真实第三分母的十进制格点。令
```math
S:=N-2k=\nu+3r+1-2g\le0,
```
并把 `u=b3/10^m3` 约为分母
```math
D=2^A5^B,\qquad
 A=(m_3-\nu-d_2)_+,\quad B=(m_3-\nu-d_5)_+.
```
由于 `0<u<1`，`D(1-u)` 是正整数。若 `D=1`，已立即矛盾；以下
可假设 `D>1`。由 (JS24) 得
```math
0<D(1-u)<\tfrac12D10^{N-4g}\psi^2
+\frac{47}{100}D10^S.
\tag{DB}
```

若 `d2=g,d5<g`，写 `Delta5=g-d5>=1`，由 `n3=2d5`：
```math
A=(2d_5-\nu)_+,\quad B=(g+d_5-\nu)_+,\quad B\ge A.
```
于是
```math
S+A=\max(S,3r+1-2\Delta_5),\qquad
S+B=\max(S,3r+1-\Delta_5).
```
若 `Delta5>=3r+1`，两者都不正，故 `D10^S<=1`。
同时 `B>0`（否则 `D=1`）并且 `D<=10^B`，所以
```math
\tfrac12D10^{N-4g}\psi^2
<\tfrac12 10^{r+1-2g-\Delta_5}
\le\frac1{2\cdot10^9}.
```
代入 (DB) 得正整数 `<47/100+1/(2*10^9)<1`，矛盾。

若 `d5=g,d2<g`，写 `Delta2=g-d2>=1`，由 `n3=2d2-1`：
```math
A=(g+d_2-1-\nu)_+,\quad B=(2d_2-1-\nu)_+,\quad A\ge B,
```
```math
S+A=\max(S,3r-\Delta_2),\qquad
S+B=\max(S,3r-2\Delta_2).
```
若 `Delta2>=3r`，仍有 `D10^S<=1`；`A>0` 且 `D<=10^A` 给 radius
项 `<(1/2)10^(r-2g-Delta2)<=1/(2*10^9)`，同一整数矛盾完成第二行。

若 `d2=d5=g`，则 `D=10^(n3-nu)`，且 `n3>nu`（否则 `D=1`）。
写 `c=2g-n3>=1`，有
```math
D10^S=10^{3r+1-c},\qquad
\tfrac12D10^{N-4g}\psi^2
<\tfrac12 10^{r+1-2g-c}\le\frac1{2\cdot10^9}.
```
`c>=3r+1` 时再次矛盾，给出第三行。
所有 radius 小量界只用 `g>=3r+2` 与各 gap 至少 `1`，不对 `g` 或
`n3` 设置绝对上界。

最新 regular core 是 (JS34) 三类相对 gap 加上真实 denominator
unit、精确 cancellation、(JS24)--(JS25)。两个不同号边界及不满足
(2S) 的区域仍必须分别处理。


<a id="a1-05-detail-src-0085-832-12"></a>
#### 去掉 (2S) 后的第一分母 2-adic 三分裂

**状态：已严格完成（必要形状及子支空性）；不扩大 (JS33)--(JS34) 的范围。**
令 `e1=v2(w)=v2(b1)<4r`。已有范围保证
```math
\nu+m_3\ge(3r+3)+(g+1)\ge6r+6>e_1.
```
因此 potential first-max beta-resonance `e3,2=nu+m3<=e1` 实际不可能。

完整候选必须满足
```math
\boxed{\max(e_1,\nu)<e_{3,2}<\nu+m_3.}
\tag{JS35}
```
证明下界需要分开三种第一分母深度：`e1<nu` 已在 (JS30) 中处理。
`e1=nu` 且 `e3,2<=nu` 时，最大分母层有两个或三个奇坐标，球面模
`4` 的平方和分别为 `2` 或 `3`，不可能。`e1>nu,e3,2<e1` 时第一分母
唯一最深，`H_sph` 为奇数，而上面的 arch bound 保证
`v2(beta)=e3,2<e1`，与整数 word 相矛盾；`e3,2=e1` 时第一、第三坐标
同为奇数，又得到模 `4` 的 `2`。上界则和 (JS30) 一样来自第三坐标唯一
最深、`alpha` 为奇数及 beta 等深时两个奇单位相加。

现在写 `t=e1-nu`、`d2=e3,2-nu`，则 `v2(y1)=d2-t`、`v2(y2)=d2`。
球面右端实际赋值是
```math
V:=v_2(y_1^2+y_2^2)=
\begin{cases}
2d_2,&t<0,\\
2d_2+1,&t=0,\\
2(d_2-t),&t>0.
\end{cases}
```
`t=0` 时两个归一奇数平方的和 `=2 mod4`，所以多出的 `1` 不能遗漏。
`t!=0` 时只有一个更浅坐标，其 gap 至少为 `2`；`t=0` 时 gap 可以为 `1`。
(JS26)、(JS35) 共同保证 `10^(nu+1)|b3`，故仍有真实高度 `n3>=nu-g+2>=3`。

完整两项 word 仍按 `d2` 与 `g` 比较，而球面按上述 `V` 分裂，得到
```math
\boxed{
\begin{array}{c|ccc}
&t<0&t=0&t>0\\ \hline
d_2<g&n_3=2d_2-1&n_3=2d_2&n_3=2(d_2-t)-1\\
d_2=g&n_3\le2g-1&n_3\le2g&n_3\le2(g-t)-1\\
d_2>g,\ d_2\le m_3-2&m_3=3d_2-1&m_3=3d_2&m_3=3d_2-2t-1
\end{array}}
\tag{JS36}
```
若 `d2=m3-1`，则 `v2(H_sph-y3)=1`、`v2(H_sph+y3)=V-1`，仍单列
near-beta 边界。这些赋值来自实际整数正因子 `H_sph±y3` 与完整 word，
不是从模 `2` 同余臆定正负号。

与独立的 `5`-adic 形状联立，得到无 (2S) 的必要过滤：
```math
\boxed{
\begin{aligned}
d_2<g, d_5<g&\Longrightarrow t=0\ \text{且}\ d_2=d_5,\\
g<d_2\le m_3-2, g<d_5<m_3&\Longrightarrow
\begin{cases}
\varnothing,&t<0,\\
d_2=d_5,&t=0,\\
t\equiv1\pmod3,&t>0.
\end{cases}
\end{aligned}}
\tag{JS37}
```
第一行在 `t!=0` 时仍因 `n3` 奇偶矛盾而关闭，但 `t=0` 的新 two-coordinate
balanced branch 不能删除。第二行的 `t>0` 来自
`3d2-2t-1=3d5`，只给必要同余；局部允许的 `t=1 mod3` 仍待证。
`e1=nu` 自动要求 `r>=13`，因为 `r<=12` 已证明 `e1<nu`。

<a id="a1-05-detail-src-0085-832-13"></a>
#### 5-adic beta-resonance 的精确三项 cancellation 与相对高度

**状态：已严格完成（无界必要条件；高尾子支空性）。**
这段处理 `d5=m3`，不要求 (2S)。仍沿用 (JS27) 的 `A,B`，并令
`C5=q_lcm/5^(nu+m3)`。把正 gap word 除以 `5^(nu+m3)`，利用
`C5 a3=y3 B`，得到精确式
```math
(H_{\rm sph}+y_3)(A+B)
=C_5 A_{12}10^{n_3}+y_3(A+2B).
```
左端深度为 `2m3`，第一项深度为 `n3<m3`，故必须
```math
\boxed{v_5(A+2B)=n_3,}
\tag{JS38}
```
并且
```math
v_5\left(C_5A_{12}2^{n_3}
+y_3\frac{A+2B}{5^{n_3}}\right)=2m_3-n_3.
```
这是比 (JS27) 的单层 unit congruence 更强的精确 cancellation。

真实位数给 `B<2^m3/5^nu`，而
`10b1+1<10^(2g)`、`nu<=2g-4`，故
```math
A+2B
<2^{m_3}\left(2^\nu10^{2g}+2/5^\nu\right)
<2^{m_3}400^g.
```
由 (JS38) 的 `5^n3<=A+2B` 与 `n3=m3-g`，
```math
(5/2)^{m_3}<2000^g.
```
因为 `(5/2)^9>2000`，得到完整的无界条件空性
```math
\boxed{d_5=m_3\Longrightarrow m_3<9g.}
\tag{JS39}
```
`m3>=9g` 的整个 beta-resonance 高尾子支已关闭，`m3<9g` 仍是相对
高度范围；`g` 可无界增长，不能称为全局有限盒。

(JS38) 还要求
```math
B\equiv-2^{\nu+m_3-1}(10b_1+1)\pmod{5^{n_3}}.
```
`nu>=g+1` 保证 `2^m3/5^nu<5^n3`，故每个固定前缀与固定 `m3` 的
允许区间中至多一个整数 `B`。这只是精确恢复的候选压缩，仍须联立
完整 sphere、既约性和另一素数的真实深度。

在 (2S) 下，5-beta 也不能与 2-near-beta `d2=m3-1` 同时出现，因为
真实分母质量要求 `10^nu<2^(m3-d2)=2`。若 `d2<=g`，2-word 形状给
`m3-d2<=2g-1`，但 `2^(2g-1)<10^(g+1)<=10^nu`，同样矛盾。
因此 (2S) 内若 5-beta 仍存，只能搭配 regular 2-high
`d2>g,m3=3d2-1`，并满足精确质量条件
```math
\boxed{2^{2d_2-1}>10^\nu.}
```
该搭配还要遵守 (JS38)--(JS39)；本轮没有把它宣称为空。


<a id="a1-05-detail-src-0085-832-14"></a>
#### (2S) 内 5-beta 的跨素数高度与 `g/r` 相对界

**状态：已严格完成（无界子支空性及相对盒）；有限盒内未枚举解。**
本段重新添加 (2S)，不能把结论扩到首分母的新增 balanced/deep 分支。
5-beta 只剩 regular 2-high，故 `m3=3d2-1,d2>g`。
(JS38) 中 `A` 的 `2` 深度为 `nu+m3`，`2B` 的 `2` 深度为
`nu+d2+1`；后者严格更浅。因此
```math
v_2(A+2B)=\nu+d_2+1,\qquad v_5(A+2B)=n_3.
```
而 `10b1+1<=10^(2g)-9`，`2B/2^(nu+m3)<2/10^nu<9`，给出更紧
的真实 arch bound `A+2B<2^(nu+m3)10^(2g)`。所以
```math
\boxed{5^{3d_2-g-1}<2^{2d_2-2}10^{2g}.}
\tag{BP}
```
这首先排除 `d2>=2g`；在 `d2=2g` 时左/右比为
`(4/5)(125/64)^g>1`，且该比随 `d2` 严格增加。

还可统一加强为
```math
\boxed{g<d_2<11g/6.}
\tag{BH}
```
在 `d2=11g/6` 时左/右比为 `(4/5)(5^(5/2)/2^(17/3))^g`。
其底数大于 `1`（`5^15>2^34`），`g>=5` 的最小端点比也大于 `1`，
把 `g=5` 端点比提升到六次方正是 `5^69/2^158>1`。
这给出全部无界 `g` 的阈值证明，不来自枚举。

接回真实分母质量。令 `alpha_2=log10(2)`，则
```math
\nu<\alpha_2(2d_2-1),\qquad
\frac3{10}<\alpha_2<\frac{151}{500}.
```
两个有理常数界分别由 `2^10>10^3`、`2^500<10^151` 精确验证。
结合 (BH) 与 `nu>=g+1` 得 `g>1953/161`，所以 **`g>=13`**。

这里 `u=b3/10^m3` 的既约分母为
```math
D=2^{2d_2-1-\nu};
```
指数为正，另一素数已在分子中。写 `S=nu+3r+1-2g`，并令
```math
C:=\frac{11}{3}\frac{151}{500}\left(2-\frac{151}{500}\right)
=\frac{470063}{250000}<2.
```
用严格质量界以及 (BH)，
```math
\begin{aligned}
\log_{10}(D10^S)
&=2\alpha_2d_2+(1-\alpha_2)\nu+3r+1-\alpha_2-2g\\
&<2\alpha_2(2-\alpha_2)d_2+3r+(1-\alpha_2)^2-2g\\
&<(C-2)g+3r+49/100.
\end{aligned}
```
如果 `g>=26r+6`，最后一行至多
```math
-\frac{14181}{125000}r-\frac{28561}{125000}<0.
```
同理 scaled radius 的十进制指数满足
```math
\log_{10}(D10^{N-4g})<(C-4)g+r+49/100
\le-\frac{6764181}{125000}r-\frac{1528561}{125000}<-9.
```
因此乘 (JS24) 得到正整数
`0<D(1-u)<47/100+1/(2*10^9)<1`，矛盾。
最终 5-beta 在 (2S) 内必须满足
```math
\boxed{13\le g<26r+6,\qquad g<d_2<11g/6,
\qquad m_3=3d_2-1.}
\tag{JS40}
```
当 `r<=12` 时确实得到 `g<=317`，但本轮没有枚举该有界形状中的
实际前缀、offset 或解；不能把这个相对高度归约宣称为 5-beta 已全部关闭。
高于 (JS40) 的整片无界参数已由精确格点矛盾关闭，盒内仍须用
(JS38)、唯一 `B` residue、原既约性与完整 sphere 继续审计。


<a id="a1-05-detail-src-0085-832-15"></a>
#### 2-near-beta 的真实加法 word 与低/平衡 5 支相对盒

**状态：已严格完成（无界条件空性与恢复条件）；盒内仍待证。**
本段保留 (2S)，处理 `d2=m3-1`，且 `d5<m3`。
写
```math
b_3=2^{\nu+m_3-1}B_2,\qquad
 A_2=5^{\nu+m_3}(10b_1+1),\qquad
 C_2=q_{\rm lcm}/2^{\nu+m_3-1}.
```
正 gap 的真实加法 word 给
```math
\boxed{
(H_{\rm sph}+y_3)(B_2+2A_2)
=C_2A_{12}10^{n_3}+2y_3(A_2+B_2).
}
```
左端 `2` 深度为 `2m3-3`，第一项深度为 `n3=m3-g`，故
```math
\boxed{v_2(A_2+B_2)=n_3-1.}
\tag{JS41}
```
不把模 `2` 同余当作 `H_sph±y3` 的符号；该深度来自 (JS31) 中真实
near-beta 因子的赋值。

此时 `u` 的既约分母只能为 `D=5^b`，其中
`b=m3-nu-d5>0`；若 `b<=0`，`u` 为整数，与 `0<u<1` 直接矛盾。
`u` 的分子至少被 `2^(nu-1)` 整除，所以质量条件为
```math
\boxed{2^{\nu-1}<5^b.}
```
令 `h=2g-3r-1-nu>=0`，则 `S=-h`。

若 `d5<g`，写 `Delta=g-d5>=1`，由 `n3=2d5` 得
```math
b=3r+1+h-\Delta,\qquad
D10^S=2^{-h}5^{3r+1-\Delta}.
```
scaled radius 小于 `(1/2)10^(r+1-2g-Delta)<=1/(2*10^9)`。
正整数 `D(1-u)` 先排除 `Delta>=3r+1`，所以 `Delta<=3r`。
再由 `47/100*2+1/(2*10^9)<1`，必有 `D10^S>2`，于是
```math
2^{h+1}<5^{3r+1-\Delta}<2^{3(3r+1-\Delta)},\qquad
h\le9r+1-3\Delta.
```
结合质量 `2^(nu-1)<5^b<2^(3b)` 和 `nu=2g-3r-1-h`，
```math
2g<12r+5+4h-3\Delta\le48r+9-15\Delta\le48r-6.
```
因此严格得到
```math
\boxed{d_2=m_3-1,\ d_5<g\Longrightarrow
1\le g-d_5\le3r,\qquad g\le24r-4.}
\tag{JS42a}
```

若 `d5=g`，写 `c=2g-n3>=0`，则
```math
b=3r+1+h-c,\qquad D10^S=2^{-h}5^{3r+1-c}.
```
scaled radius `<(1/2)10^(r+1-2g-c)<=1/(2*10^8)`。
同一正整数预算给 `c<=3r`、`h<=9r+1-3c`，质量再给
`2g<48r+9-15c<=48r+9`，故
```math
\boxed{d_2=m_3-1,\ d_5=g\Longrightarrow
2g-3r\le n_3\le2g,\qquad g\le24r+4.}
\tag{JS42b}
```
两行给出真实高 `g` 子支的无界关闭，但 `r` 没有全局上界；即使
`r<=12` 把 `g` 压到绝对有界，本轮也没有枚举盒内解。

`d5>g` 的 5-regular-high 仍保留 `m3=3d5`、(JS41)、真实 denominator
unit 和完整恢复。一个独立的 prefix-source bound 来自
[rational-contact.md](#a1-01) 的 universal denominator funnel：
令 `j` 为 `b3` 的非 `2,5` 部分，则
```math
j\mid b_1(10b_1+1)^2,\qquad
u=2^{\nu-1}j/5^{2d_5-\nu}.
```
用已证明的 `u>529/1000`，
```math
25^{d_5}<10^\nu j<10^{\nu+3(2g-r)+2}\le10^{8g-6r+1}.
```
因为 `25^6>10^8`，完整候选必须 `d5<6g`，即 `m3<18g`。
这仍是相对尾高压缩，不是 5-regular-high 全部空性；最新剩余应联立
该 divisor condition、(JS41) 与原 sphere，而不能只使用 phase 窗口。

<a id="a1-05-detail-src-0085-832-16"></a>
#### non-(2S) 的真实第一分母质量与 two-coordinate low balanced

**状态：已严格完成（必要恢复与无界子支空性）。**
若 `e1=v2(w)>=nu`，真实 `w` 的上界直接给
```math
\boxed{2^{g+1}\le2^\nu\le w<(267/500)10^r.}
```
因此 `r>=13`；`g` 还须满足这个 exact power criterion，不能把首分母
更深的范围忽略。该条件可用于审计 `t=0` 和 `t>0` 的新增分支。

在 `e1=nu,d2=d5=d<g` 的 two-coordinate low balanced 中，
`n3=2d`，`u` 的既约分母为 `D=10^(g+d-nu)`；若指数不正则 `u` 为
整数而为空。写 `Delta=g-d`，有
```math
D10^S=10^{3r+1-\Delta},\qquad
\tfrac12 D10^{N-4g}\psi^2
<\tfrac12 10^{r+1-2g-\Delta}\le\frac1{2\cdot10^9}.
```
因此 `Delta>=3r+1` 仍被正整数预算排除，得到
```math
\boxed{e_1=\nu,\ d_2=d_5=d<g
\Longrightarrow1\le g-d\le3r.}
\tag{JS43}
```
这是去掉 (2S) 后的新恢复条件；该相对 gap 内仍待证，没有宣称该
two-coordinate balanced branch 已全局关闭。


来源：`SRC-0085:684–716`；`SRC-0085:832–1859`。原文保全，当前论证以本节为准。

<a id="a1-k01"></a>
### A1-K01　最低层 significand 严格递增

**状态：已严格完成。** d=-1，tau2≤tau1（特别是 b2 为十进制幂）无界为空。

依赖：[A1-02](#a1-02)、[C05](#c05)

核对：`a1-kernels`

<a id="a1-k01-detail-src-0089-5064-1"></a>
#### 最低层的分母 significand 必须严格递增

令 `d=s1-g=-1`，`k=s2-g>=1`，并写
```math
\tau_i=b_i/10^{m_i-1}\in[1,10),\qquad i=1,2.
```
因为 `n1=m1+g-1`、`n2=m2+k+g`，原位数范围给出
```math
r_1<10^g/\tau_1,
\qquad r_2\ge10^{k+g}/\tau_2.
```
第一块严格承担 carrier，故 `10^k r1>r2`。因此
```math
\boxed{d=-1\Longrightarrow\tau_2>\tau_1.}
\tag{LK1}
```
这严格关闭全部 `d=-1,tau2<=tau1` 的无界子域。特别地
```math
\boxed{d=-1,\quad b_2=10^{m_2-1}\Longrightarrow\varnothing,}
\tag{LK2}
```
无论第一分母、第三块和六块位数如何增长。它只是一个最低层
endpoint kernel，不排除 `tau2>tau1` 的完整最低层。


来源：`SRC-0089:5064–5087`。原文保全，当前论证以本节为准。

<a id="a1-k02"></a>
### A1-K02　balanced 且前缀深度不等的 g=0 子域

**状态：已严格完成。** 三个分母 balanced、g=0、a≠b；一般 g 的 c>b+g 子片同样排除。

依赖：[A1-02](#a1-02)、[C05](#c05)

核对：`a1-kernels`

<a id="a1-k02-detail-src-0089-5088-1"></a>
#### `g=0` 的 balanced-denominator / unequal-prefix-depth state 为空

设
```math
b_1=10^a u_1,\qquad b_2=10^b u_2,\qquad
b_3=10^c j,\qquad (j,10)=1,
\qquad (u_1,10)=(u_2,10)=1,
\qquad a,b,c\ge0,\quad u_1,u_2,j\ge1.
\tag{LK3}
```
这恰好表示三个分母都满足 `v2(bi)=v5(bi)`，其三个 `10`-unit
因子都无界。记 `m3=c+digits(j)`、`D2=digits(u2)`。
本节证明
```math
\boxed{g=0,\quad a\ne b,\quad\text{(LK3)}
\Longrightarrow\varnothing.}
\tag{LK4}
```
这是跨全部四层 `d=-1,0,1,2` 的无界排除；并非固定参数搜索。
更一般，当 `g>=0` 且 `c>b+g` 时，同一证明排除 (LK3) 的
`a!=b` 子域。

<a id="a1-k02-detail-src-0089-5088-2"></a>
#### 真正第三块必须同时最深

令 `q=lcm(b1,b2,b3)`、`yi=ai q/bi`、`H=q alpha/beta`。
原 exact lift 的 sphere 保证 `H` 是正整数，且
```math
H^2=y_1^2+y_2^2+y_3^2,\qquad q\alpha=H\beta.
```
第三分母的两个深度均为 `c`，原始分母拼接精确为
```math
\beta=10^{m_3+b}Q0+10^c j,
\qquad Q0=u_1 10^{a+D2}+u_2.
\tag{LK5}
```
因为 `m3>=c+1`，且 `Q0` 为 `2/5` unit，有
`v2(beta)=v5(beta)=c`。

令 `E=max(a,b,c)`。在 `a!=b` 下 `max(a,b)>=1`。若 `c<E`，
且第一或第二分母唯一达到 `E`，该 sphere 坐标为奇数，其余为偶数，
所以 `H` 为奇数。于是 `q alpha=H beta` 的左端 `2` 深度至少为
`E`，右端恰为 `c`，矛盾。若有两个分母达到正的 `E`，sphere
右端为 `2 mod4`，也矛盾。由此必有
```math
\boxed{c>\max(a,b),\qquad q=10^c l,\qquad y_3=a_3 l/j,}
\qquad l=\operatorname{lcm}(u_1,u_2,j).
\tag{LK6}
```
这一步允许 `a=0` 或 `b=0`；只在正的最大分母深度上用既约性
推出相应分子为奇数，不假定分母 `1` 的分子为 `2/5` unit。

<a id="a1-k02-detail-src-0089-5088-3"></a>
#### 同一个 word gap 的两个素数深度互相冲突

令 `A12=a1 10^n2+a2`，以及
```math
L=m_3+b-c\ge1.
```
由 (LK5) 和 `q alpha=H beta` 得精确恒等式
```math
\boxed{j(H-y_3)=l A12\,10^{n_3}-H Q0\,10^L.}
\tag{LK7}
```
由 (LK6)，`H`、`y3`、`j`、`l`、`Q0` 都为 `2/5` unit。
若 `c>b+g`，则 `n3=m3-g>L`，所以右端第二项严格较浅，得到
```math
v_2(H-y_3)=v_5(H-y_3)=L.
\tag{LK8}
```
在 `g=0` 时，这个严格范围由 `c>b` 自动成立。

令 `E0=max(a,b)`、`delta=c-E0>=1`。因为 `a!=b`，两个 sphere
坐标中，只有与较深的第一或第二分母对应的坐标在去掉
`10^delta` 后仍为 `2/5` unit；`l/u1,l/u2` 也均为 unit。因此
```math
v_2(y_1^2+y_2^2)=v_5(y_1^2+y_2^2)=2\delta.
\tag{LK9}
```
sphere gap 给 `(H-y3)(H+y3)=y1^2+y2^2`。由 (LK8)，
`H=y3 mod5`，所以 `H+y3` 为 `5` unit，故
```math
L=2\delta\ge2.
```
现在 `H-y3=0 mod4` 且两者为奇数，故 `v2(H+y3)=1`。
同一 gap 的 `2` 深度随后给
```math
L+1=2\delta,
```
矛盾。这证明 (LK4) 及其显式一般化范围。


来源：`SRC-0089:5088–5176`。原文保全，当前论证以本节为准。

<a id="a1-k03"></a>
### A1-K03　等深 word corridor 与公共模九边界

**状态：已严格完成。** equal-prefix e≥1，c>e+g 的严格 word corridor；只是必要形状。

依赖：[A1-02](#a1-02)、[C05](#c05)

核对：`a1-kernels`

<a id="a1-k03-detail-src-0089-5177-1"></a>
#### 剩余边界与公共模九过滤

三个分母都为十进制幂的更窄状态，已由
[global-framework §10.1](RESEARCH.md#common-model)（原始记录 SRC-0199）
整体关闭：三个分母都是 `1 mod9`，违反公共分母条件 (D9)。
本节 (LK4) 更宽。例如分母 `(10,100,13000)` 满足 (LK3)，
而其模九类为 `(1,1,4)`，通过 (D9)；它仍被这里的实际 word/sphere
深度矛盾排除。这只是说明两项过滤的覆盖差异，不声称该分母能支持
原 exact lift。

当 `a=b=e>=1` 且 `c>e+g` 时，上面的同深比较不矛盾，而只给
```math
\boxed{m_3=3(c-e),\qquad v_5(a_1^2u_2^2+a_2^2u_1^2)=0.}
\tag{LK10}
```
具体地，此时 sphere 的 `2` 深度为 `2(c-e)+1`，(LK8) 先由
`5` 深度说明 `L>=2`，然后 `2` 深度强迫 `L=2(c-e)`。
这一 equal-prefix-depth / 非纯十进制分母状态仍开放；`e=0` 的两个分子
不自动为 unit，必须另列而不能沿用 (LK10)。对 `g>=1,c<=b+g`
的状态，(LK7) 的两项次序可能交换或等深，也不在 (LK4) 范围内。
完整 `g=0` 和完整 `d=-1,0,1` 仍待证。


来源：`SRC-0089:5177–5198`。原文保全，当前论证以本节为准。

<a id="a1-k04"></a>
### A1-K04　g=1 的 unequal-prefix-depth 排除

**状态：已严格完成。** 三个分母 balanced、g=1、a≠b，unit 因子任意。

依赖：[A1-02](#a1-02)、[C05](#c05)

核对：`a1-kernels`

<a id="a1-k04-detail-src-0089-5199-1"></a>
#### 不等首深度的 word resonance 与 `g=1` 该状态排除

继续 (LK3)，设 `a!=b`，并假设 `b>=1`；更一般只需
`gcd(a2,10)=1`。于是 `A12` 也是 `2/5` unit。由 (LK6) 已有
`c>max(a,b)`。若 `n3!=L`，(LK7) 两项中的较浅项在两个素数上
都是 unit，故 `H-y3` 的两个深度同时为 `min(n3,L)`。
与 (LK9) 联立后仍得到 `L'=2delta` 与 `L'+1=2delta` 的矛盾。
因此全部非等深 word 状态已经关闭，剩余必须满足
```math
\boxed{c-b=g,\qquad n_3=L\le2\delta-2,
\qquad\delta=c-\max(a,b).}
\tag{LK11}
```
最后的强界不是只用球面给出的弱高度界。在等深时，
```math
j(H-y_3)=10^{n_3}(l A12-H Q0).
```
括号是两个奇数之差，故 `v2(H-y3)>=n3+1>=2`。
真实 sphere gap 随后给 `v2(H+y3)=1`、
`v2(H-y3)=2delta-1`，证明 `n3<=2delta-2`。
相应精确 cancellation 条件为
```math
v_2(l A12-H Q0)=2\delta-1-n_3\ge1,
\quad
v_5(l A12-H Q0)=2\delta-n_3\ge2.
```
这里 `5` 深度由 `H=y3 mod5` 后的正 minus gap 得出；两个符号
都由同一个原始 gap 确定。

当 `g=1,b>=1` 时，(LK11) 给 `c=b+1`、`delta<=1`，与
`n3>=1` 冲突。当 `g=1,b=0` 时，`a>=1`、`c>a` 强迫
`c>=2>b+g`，直接落入 (LK4) 的已闭 strict 范围，无需假设
第二分子是 unit。因此
```math
\boxed{0\le g\le1,\quad a\ne b,\quad\text{(LK3)}
\Longrightarrow\varnothing.}
\tag{LK12}
```
这跨全部四层关闭新的无界子域。一般 `g>=2` 的等深
(LK11) corridor 仍开放；`b=0,gcd(a2,10)!=1` 时不能自动推广
其中关于较浅第一项的 unit 论证。


来源：`SRC-0089:5199–5240`。原文保全，当前论证以本节为准。

<a id="a1-k05"></a>
### A1-K05　实际 product 的分段条件

**状态：已严格完成。** g=0 或 delta≥g+2 为 11/19 mod20；delta=g+1 且 g≥1 为 1/9。

依赖：[A1-02](#a1-02)、[C05](#c05)

核对：`a1-kernels`

<a id="a1-k05-detail-src-0089-5241-1"></a>
#### `g=0` 的 unit product 与一般 `g` 的首 strict 边界

设 `g=0,a=b=e>=1`。正的 `2` 最大分母深度必须唯一取得，故
`c>e`，从而 (LK10) 自动适用。写 `delta=c-e>=1`、
`m3=3delta`，并令
```math
U=(H-y_3)/10^{2\delta}.
```
由 (LK8)/(LK10)，`U` 为 `2/5` unit，且原 word 与 sphere 精确给
```math
jU=l A12\,10^\delta-H Q0,
\qquad
U(2y_3+10^{2\delta}U)=l^2 S,
\quad S=(a_1/u_1)^2+(a_2/u_2)^2.
```
模五中 `Q0=u2`、`H=y3=a3 l/j`。因此
```math
S\equiv-2a_3^2u_2/j^3\pmod5.
```
`S` 是两个非零平方之和且为 unit，故其剩余类只能 `2` 或 `3`。
这强迫 `u2/j^3` 为模五平方，也即 `u2 j=1` 或 `4 mod5`。

模八中 `l² S=2`。令 `I=1` 当 `delta=1`、否则 `I=0`。
因 `e+digits(u2)>=2`，word 模四和 sphere 模八分别给
```math
Uy_3\equiv2I-u_2/j\pmod4,
\qquad Uy_3\equiv1-2I\pmod4.
```
这里 `delta=1` 时，sphere 的 `10²U²=4 mod8` 与 word 的
`10l A12=2 mod4` 都必须保留；两项在联立后恰好抵消。
所以任意 `delta>=1` 都强迫 `u2 j=3 mod4`。合并两素数得
```math
\boxed{g=0,a=b=e\ge1\Longrightarrow
u_2j\equiv11\text{ 或 }19\pmod{20}.}
\tag{LK13}
```
另外六个单位 product 类整片为空。例如分母 `(10,10,300)` 的
模九 class `(1,1,3)` 通过公共 (D9-general)，但 product `3 mod20`
违反 (LK13)。允许的两个 product 类仍不是存在性结论，也没有据此
关闭整个 equal-prefix-depth state。对于一般 `g>=0,c>e+g`，
(LK10) 仍成立，但除去 gap 深度后的 word 第一项是
`l A12 10^(delta-g)`，不能改成 `10^delta`。令 `Iword=1` 当
`delta-g=1`、否则为零，`Isphere=1` 当 `delta=1`、否则为零，
则精确模四关系为
```math
u_2j\equiv2Iword+2Isphere-1\pmod4.
```
模五平方条件不变。因此 `g>=1,delta=g+1` 必须是
`product=1` 或 `9 mod20`；`delta>=g+2` 才必须 `11` 或 `19 mod20`。
`g=0` 的两个 extra term 同时出现，故 (LK13) 原范围完全保留。
**审计状态：失效/降级。** 此前把 `11/19 mod20` 延伸到所有
`c>e+g` 的推断遗漏 `delta=g+1` 的一阶 word 项，现撤回该扩张；
上面的分段条件是当前有效范围。


来源：`SRC-0089:5241–5294`。原文保全，当前论证以本节为准。

<a id="a1-k06"></a>
### A1-K06　equal-prefix 三层与 g=1 resonance

**状态：已严格完成。** equal-prefix e≥1 的 delta>g / <g / =g；g=1,delta=1 为空。

依赖：[A1-02](#a1-02)、[C05](#c05)

核对：`a1-kernels`

<a id="a1-k06-detail-src-0089-5295-1"></a>
#### Equal-prefix-depth 的三层 source 与 `g=1` resonance 排除

在 (LK3) 中设 `a=b=e>=1`，仍令 `delta=c-e`。
正的 `2` 最大分母深度唯一性先给 `delta>=1`。
两个 sphere 坐标同为浅坐标，故
```math
v_2(y_1^2+y_2^2)=2\delta+1,
\qquad v_5(y_1^2+y_2^2)\ge2\delta.
```
与 (LK7) 两项的真实次序比较，得到完整必要表：

| 范围 | 原 word 的较浅 source | 必须满足的形状 |
| --- | --- | --- |
| `delta>g` | `H Q0 10^L` | `m3=3delta`，(LK10) 的 `5`-unit 条件及上述分段 product 过滤 |
| `delta<g` | `l A12 10^n3` | `n3=2delta,m3=g+2delta`，(LK10) 的 `5`-unit 条件 |
| `delta=g` | 两项同深 | `n3<=2g-1`，即 `e+digits(j)<=2g-1` |

第一行已在 (LK10)/(LK13) 证明。第二行中，word 先给
`v2(H-y3)=v5(H-y3)=n3`。sphere 的 `5` 深度先迫 `n3>=2delta>=2`，
所以 `v2(H+y3)=1`，随后 `n3+1=2delta+1` 迫 `n3=2delta`；
`5` 深度也迫两个归一化浅坐标的平方和为 unit。
第三行中，word 括号是 odd−odd，故 `v2(H-y3)>=n3+1>=2`；
真实 sphere 再给 `v2(H-y3)=2g`，证明该界。

特别地，`g=1,delta=1` 的第三行给 `n3<=1`，但是
`n3=m3-g=e+digits(j)>=2`。因此
```math
\boxed{g=1,\quad a=b=e\ge1,\quad c=e+1,
\quad\text{(LK3)}\Longrightarrow\varnothing.}
\tag{LK14}
```
与 (LK12) 合并，`g=1` 且至少一个第一/第二分母的共同 `2/5`
深度为正时，所有 balanced-denominator 候选只余
```math
a=b=e\ge1,\quad \delta\ge2,\quad m_3=3\delta,
\quad
\begin{cases}
u_2j=1\text{ 或 }9\pmod{20},&\delta=2,\\
u_2j=11\text{ 或 }19\pmod{20},&\delta\ge3.
\end{cases}
```
这仍是一个开放的无界系统；两个首分母深度都为零、非 balanced
分母与其他位数层也没有据此关闭。


来源：`SRC-0089:5295–5338`。原文保全，当前论证以本节为准。

<a id="a1-k07"></a>
### A1-K07　纯等前缀 j|Q0 与奇数深度排除

**状态：已严格完成。** 纯等前缀、balanced tail 的 j|Q0；g=0 奇数 e 及 strict 指定范围为空。

依赖：[A1-K06](#a1-k06)

核对：正文推导；本次重写未为此项另增枚举。

<a id="a1-k07-detail-src-0089-5339-1"></a>
#### Pure equal-prefix 的完整 prime supply 与奇数首深度排除

在 `g=0,a=b=e>=1` 中进一步限制 `u1=u2=1`，即
`b1=b2=10^e`。记 `Q0=10^(e+1)+1`。
此时 `q=b3=10^(e+delta)j`、`y1=j10^delta a1`、
`y2=j10^delta a2`、`y3=a3`。对任意 `p|j`，sphere 模 `p`
给 `H²=a3²`，而既约性给 `p not|a3`，故 `p not|H`。
所以 `gcd(H,j)=1`。原始 word 精确为
```math
j\alpha=H(10^{2\delta}Q0+j),
```
于是 `j|H 10^(2delta)Q0`，直接得到完整素数幂深度的整除
```math
\boxed{j\mid Q0.}
\tag{LK15}
```
这比 [universal denominator funnel](#a1-01) 只给的
`j|Q0²` 更强，没有把同余过滤当作整数 recovery。
整除结论也适用于任意 `g` 的 pure equal-prefix / balanced-tail：
正首深度时，最大 `2` 深度唯一性仍迫 `c>e`，故 `q=b3`；原 word 为
`j alpha=H[Q0 10^(m3-delta)+j]`，其中 `m3-delta=e+digits(j)>=1`。
同一个 `gcd(H,j)=1` 直接给 `j|Q0`，不使用 contact 的 `P` 或错误的
(LK17G) 推广。这里不能把 balanced-tail 条件删去。

若 `e` 为奇数，则 `Q0=X²+1`，其中 `X=10^((e+1)/2)`。
任何 `p=3 mod4` 若整除 `X²+1`，二平方和局部引理会迫
`p|X` 且 `p|1`，矛盾。因此 `Q0` 的所有素因子都是 `1 mod4`，
其所有正因子 `j` 也都是 `1 mod4`。这与 (LK13) 的 `j=3 mod4`
冲突。故全部奇数 `e` 的 pure equal-prefix / balanced-tail 状态为空。
`g=1,delta>=3` 的 strict 子域同样被这个奇数 `e` 论证排除。
`g=1,delta=2` 的 product 却为 `1` 或 `9 mod20`，与 `j=1 mod4`
相容；不能从此推出该边界为空。更一般 `g>=1,delta=g+1`
必须保留这一独立状态。

在 `g=0` 的剩余中，`digits(j)=2delta-e>=1` 且 `j<=Q0`，先给
`delta<=e+1`。若 `delta=e+1`，`j` 和 `Q0` 都有 `e+2` 位；
所有 proper divisor 不超过 `Q0/2<10^(e+1)`，故只能 `j=Q0`，
再次与 `j=3 mod4` 矛盾。因此必要条件收紧到
```math
\boxed{e\text{ 为偶数},\quad e\ge2,\quad
e/2+1\le\delta\le e,\quad j\mid Q0,
\quad j=11\text{ 或 }19\pmod{20}.}
\tag{LK16}
```
这是无界 `e` 上的严格相对界，不是有限全局盒。
例如 `e=2` 只余 `delta=2,j in {11,91}`。


来源：`SRC-0089:5339–5385`。原文保全，当前论证以本节为准。

<a id="a1-k08"></a>
### A1-K08　纯等前缀 g=0,d=1 的深 k 排除

**状态：已严格完成。** g=0,d=1,b1=b2=10^e,e≥1,2k≥e+2；第三分母任意。

依赖：[A1-K06](#a1-k06)

核对：正文推导；本次重写未为此项另增枚举。

<a id="a1-k08-detail-src-0089-5386-1"></a>
#### `g=0,d=1` 的 pure equal-prefix deep-`k` 状态为空

本段使用 actual carrier/contact 和分子位数，不要求第三分母 balanced。
设 `g=0,d=1,b1=b2=10^e,e>=1`。令
```math
E=10^e\ge10,\quad T=10^k\ge10,\quad
Q=E(10E+1),\quad\lambda=1/(10E+1),\quad\xi=Q/(Q+1).
```
由 actual 位数和既约性，
```math
10+1/E\le r_1<100,\qquad
T\le r_2\le10T-1/E,\qquad0<r_3<10.
```
原 contact 的必要条件为
```math
R>\xi P,\qquad P=(1-\lambda)Tr_1+\lambda r_2.
```
考虑 `Phi=R-xi P`。其对 `r1` 的偏导小于
`1-xi(1-lambda)T<0`；对 `r2` 的偏导严格大于
`1/12-lambda>0`，因为 `r2/R>r2/(r2+110)>=1/12`。
它也对 `r3` 严格递增。因此最大允许值由如下角点控制：
```math
r_1^*=10+1/E,\quad r_2^*=10T-1/E,\quad r_3^*=10.
```
记 `L=xi P*`。精确展开给
```math
L-r_2^*
=\frac{10T(E-1)+10E+1/E}{Q+1}
>\frac{4T}{5E},
\qquad r_2^*>9T.
```
若 `2k>=e+2`，则 `T²/E>=100`，于是
```math
L^2-(r_2^*)^2>\frac{72}{5}\frac{T^2}{E}\ge1440,
\quad (r_1^*)^2+100\le(101/10)^2+100<203.
```
所以 `L>R*`，与 `Phi>0` 冲突，证明
```math
\boxed{g=0,d=1,b_1=b_2=10^e,e\ge1,
\quad2k\ge e+2\Longrightarrow\varnothing.}
\tag{LK17}
```
特别是 (LK16) 的偶数 `e` 中，`d=1` 只余 `k<=e/2`。
这仍不关闭 `d=0` 或上述较浅 `k` 的系统。


来源：`SRC-0089:5386–5430`。原文保全，当前论证以本节为准。

<a id="a1-k09"></a>
### A1-K09　原 numerator quadratic、norm 允许点与纯等前缀 d=2 排除

**状态：已严格完成。** 原恢复方程及全部 g≥0,d=2,b1=b2=10^e；norm 允许点不证明解。

依赖：[A1-K07](#a1-k07)、[A1-K08](#a1-k08)

核对：正文推导；本次重写未为此项另增枚举。

<a id="a1-k09-detail-src-0089-5452-1"></a>
#### 回到 original numerator quadratic 的剩余核心

在 (LK16) 中令 `h0=Q0/j`、`T=10^delta`、`F0=1+T²h0`。
原 word 是 `alpha=H F0`。写 `H-a3=T²U`，则完整 tail recovery 为
```math
\boxed{a_3=(T A12-F0 U)/h0,}
\quad
\boxed{(2+T^2h0)U^2-2T A12\,U
+h0 j^2(a_1^2+a_2^2)=0.}
\tag{LK18}
```
还必须同时满足 `U>0,gcd(U,10)=1`、
`10^(3delta-1)<=a3<10^(3delta)`、`gcd(a3,10^(e+delta)j)=1`，
以及原 `a1,a2` 位数、既约与 `10^k a1>a2`。
这是一条真实 numerator quadratic 和 integer recovery，不是
Gaussian flip 后的新 coefficient plane。

单独再使用 actual denominator norm 也不能直接关闭整个余核。
例如 `e=2,delta=2,j=11,k=1` 的分母为 `(100,100,110000)`，
有 `n2=4,n3=m3=6`、`j|Q0=1001`、product `11 mod20`，
公共模九类 `(1,1,2)` 的 pair-sum 为 `5`，允许。实际 coefficients 为
```math
t_1=10^{12},\quad t_2=10^8,\quad t_3=110000,
\quad\beta=100100110000.
```
其 original decimal norm 精确满足
```math
\Delta_{\rm dec}=989979977978000000000000
=977355748928^2+186428855104^2.
```
这是 **已严格完成的投影路线边界见证**，没有给出任何分子，
不声称满足 (LK18)、完整 sphere/word、位数或既约 recovery。
较早 `e=1,j=111/119` 的 norm-only 允许点则被新的 `j|Q0`
排除；它们不属于这里的新余核，不作为完整必要条件的允许点。
下一步必须继续 (LK18)，不能将允许的 norm/squareclass 等同于解。

<a id="a1-k09-detail-src-0089-5452-2"></a>
#### 正确的第二坐标 gap 与 `e=2` 完整有限末端

令 `Z=10^k`、`M=10^delta`、`C=10^(2delta+e+1)`，并保留
`F0=1+M²Q0/j`。真实 carrier 与 sphere 给
```math
J=Za_1-a_2\ge1,\qquad V=H-jMa_2=q(R-r_2)>0.
```
原始 word 精确消元为
```math
\boxed{a_3=M[jZa_1-(C+j)J]+F0V.}
\tag{LK19}
```

对 `d=0`，`q=b3<10^(3delta)`、`r1<10,r3<10,r2>=10^k`，故
```math
1\le V<\frac{100q}{10^k}<10^{3\delta+2-k}.
```
因此 `k<=3delta+1`。`d=-1` 已由 (LK2) 排除。
`d=2` 的 pure equal-prefix 直接为空，且可覆盖全部 `g>=0`、
`e>=0`，无需第三分母 balanced。原位数给
`r1>=10^(g+2),r2<10^(g+1)Z,r3<10^(1-g),Z>=10`，所以
```math
\left(\frac R{Zr_1}\right)^2
<\frac1{Z^2}+\frac1{100}+\frac{10^{-4g-2}}{Z^2}
\le\frac{201}{10000}<\left(\frac56\right)^2.
```
另一方面 `xi(1-lambda)=10E²/(10E²+E+1)>=5/6`（`E>=1`），
`P>(1-lambda)Zr1`，与 actual `R>xi P` 矛盾。这证明
```math
\boxed{g\ge0,d=2,b_1=b_2=10^e,e\ge0
\Longrightarrow\varnothing.}
\tag{LK19G}
```
该范围允许第三分母任意；并未移植最高层的 `p+q` 或 endpoint 窗口。


来源：`SRC-0089:5452–5526`。原文保全，当前论证以本节为准。

<a id="a1-f02"></a>
### A1-F02　g=0,e=2 的完整有限末端

**状态：有限证书。** b1=b2=100，第三分母 balanced；(delta,j) 与全部原分子窗口在 A1-K09 给出。

依赖：[A1-K09](#a1-k09)

核对：`a1-e2`

本節从 A1-K09 的正确符号与 contact 出发，给出完整参数界、原 quadratic 和证书：5050 个合法 prefix、219101 个合法 J，0 个平方判别式；没有为 e≥6 给出上界。

当 `e=2`，(LK16) 先给 `delta=2`，`1001=7*11*13` 的两位
divisors 经 product 过滤只留下 `j=11,91`。
因此 `d=0` 只需 `1<=k<=7`，`d=1` 经 (LK17) 只需 `k=1`。
这已是完全有界的末端，下面的整数核验覆盖全部余核。

令 `E=M=100`，`C=10^7`、`xi=100100/100101`、`lambda=1/1001`，
`q=10000j`、`amin=100000`、`amax=999999`。contact 先给严格 bound
```math
a_1^2<\frac{E^2(100Z^2+100)}{\xi^2(1-\lambda)^2Z^2-1}.
```
对每个满足原位数和既约性的 `a1`，sphere 给
```math
V<\frac{q[(a_1/E)^2+100]}{2Z};
```
令 `vmax` 为此严格 rational 上界之下的最大整数。
写 `base=M jZ a1`、`den=M(C+j)`，(LK19) 与 tail digit box 给完整窗口
```math
\begin{aligned}
J_{\rm lo}&=\max\left(1,Za_1-a_{2,\max},
\left\lceil\frac{base-amax+F0}{den}\right\rceil\right),\\
J_{\rm hi}&=\min\left(Za_1-a_{2,\min},
\left\lfloor\frac{base-amin+F0\,vmax}{den}\right\rfloor\right).
\end{aligned}
```
这里 `a2min=10^(e+k)`、`a2max=10^(e+k+1)-1`，`a2=Za1-J`。
对每个窗口内的合法 `J`，令 `B=base-den J`。原 sphere 与 (LK19)
精确等价于
```math
(F0^2-1)V^2+2(F0B-jMa_2)V+B^2+j^2M^2a_1^2=0.
\tag{LK20}
```
任何整数根都要求
`(F0B-jMa2)^2-(F0²-1)(B²+j²M²a1²)` 为非负整数平方。

**状态：有限证书（完整覆盖上述明示 `e=2` 子域）。** 程序穷尽
`5050` 个 `(d,k,j,a1)` prefix 与 `219101` 个满足第二分子既约性的
`J`，平方 discriminant 数为零。因此
```math
\boxed{g=0,b_1=b_2=100,v_2(b_3)=v_5(b_3)
\Longrightarrow\varnothing.}
\tag{LK21}
```
运行命令：

证书命令与覆盖见 [统一核对目录](CHECKS.md)。

上面的 norm 允许点也被这项真实 integer recovery 证书排除，说明
仅有 norm 投影的局部兼容远远不够。下面继续关闭 `e=4`；
更高的偶数首深度仍无界，
`d=0` 只有 `k<=3delta+1`，`d=1` 只有 (LK17) 的相对界；没有恢复
被撤回的整 `d=1` 或全局 `k` 下界。


来源：`SRC-0089:5527–5580`。原文保全，当前论证以本节为准。

<a id="a1-f04"></a>
### A1-F04　g=0,e=4 的完整有限末端

**状态：有限证书。** b1=b2=10^4，第三分母 balanced；两个 (delta,j) 状态，全部合法 k。

依赖：[A1-K09](#a1-k09)

核对：`a1-e4`、`cpp-a1-e4`

<a id="a1-f04-detail-src-0089-5581-1"></a>
#### `e=4` 的完整有限证书

**命题 (LK22)，状态：有限证书。** 在 `g=0,b1=b2=10^4` 且
`v2(b3)=v5(b3)` 的全部四层中，没有原 exact lift。
(LK16) 与 `100001=11*9091` 先把第三分母压成两种状态：

| `delta,j` | `d=0` 的全部剩余 `k` | `d=1` 的全部剩余 `k` |
| --- | --- | --- |
| `3,11` | `1..10` | `1..2` |
| `4,9091` | `1..13` | `1..2` |

`d=-1,2` 已由上述无界推导排除。每个表内状态沿用 (LK19)--(LK20)
以及相同 contact cap，但用真实第三分子上界加强 `V` 的窗口。
写 `M=10^delta,E=10^4,q=EMj`；由 `a3<M³` 与 `a2>0`，
```math
0<V=q(R-r_2)<\frac{M(j^2a_1^2+M^4)}{2j a_2}.
```
令 `vn=M(j²a1²+M⁴)`，先用 `a2>=ZE` 给
`vmax=floor((vn-1)/(2jZE))`。在已给出的 `Jlo..Jhi` 上，必要条件还包括
```math
2j(Za_1-J)(amin-base+den\,J)<F0\,vn.
```
左侧除去正因子 `2j` 后的导数恰为
```math
M(C+2j)Za_1-2M(C+j)J-amin.
```
程序对每个非空有限窗口精确验证其在 `Jhi` 非负，因此整段单调，
可以用整数二分进一步缩短窗口；这项断言只用于本证书的明示范围。

原 quadratic discriminant 有精确平方因子分解
```math
\begin{aligned}
D_{\rm original}&=M^4D_n,\\
D_n&=M^2\bigl[(Q0Za_1-J)^2-Q0^2(a_1^2+a_2^2)\bigr]
-2jQ0(a_1^2+a_2^2).
\end{aligned}
\tag{LK22}
```
其中必须使用 `C=M²(Q0-1)`。所以整数 `V` 必须使 `Dn` 为非负
整数平方。C++ 先在 `17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97`
上筛平方余类，全部包含零；随后对筛后候选使用精确整数平方根。
输出为 `828814` 个合法 prefix、`262115848` 个合法 `J`、
`1377` 个筛后候选、`0` 个平方 `Dn`、`0` 个原整数根。
Python 逐一独立重算全部 `1377` 个候选的十九个素数条件、`Dn` 与
`Doriginal=M⁴Dn`，同时核对 `100001` 的完整因子分解。二者都不给
浮点平方判断；所有生成物保存在临时目录。

**整数宽度。** 原生整数计算统一满足 `Z<=10^13,a1<2*10^5,j<=10^4,
M<=10^4,F0<10^10,vn<10^23`。`J<=Za1` 给
`base,den*J` 与导数绝对值小于 `2*10^36`。窗口还给
`amin-F0*vmax<=B<=amax-F0`，故 `|F0B|<5*10^36`，
`|lin|=|F0B-jMa2|<6*10^36`。非负 discriminant 时
`sqrt(Doriginal)<|lin|`，所以根分子小于 `1.2*10^37<2^127`。
`qa=F0²-1<10^20`。`possible(J)` 的乘积正负两侧均小于 `10^35`：
正侧利用 `vmax<=vn/(2jZE)` 约去 `Z`，负侧利用 `B<=amax<M³`。
`k<=3` 的 `Dn` 各项小于 `10^35`，程序另以 256 位数逐 prefix
断言其逐项绝对上界小于 `2^127`；其余 `k` 的各项小于 `10^56<2^255`，
直接以 256 位计算。完整 UBSan 重跑也得到相同计数，未发现未定义行为。

复核命令：

证书命令与覆盖见 [统一核对目录](CHECKS.md)。

**剩余系统。** 在 `g=0` 的纯等前缀 balanced-tail 中，现在只余偶数 `e>=6`，
`e/2+1<=delta<=e`、`digits(j)=2delta-e`、`j|10^(e+1)+1`、
`j=11/19 mod20`；仅需 `d=0,1`，分别有 `k<=3delta+1`、`k<=e/2`。
必须继续解 (LK18) 或 (LK19)--(LK20) 的原整数 recovery，且满足
全部 digit/reducedness。这里没有给 `e` 的绝对上界，不能把两份有限
证书提升为整个纯等前缀、整个 `g=0` 或整个 A1 的闭合。


来源：`SRC-0089:5581–5654`。原文保全，当前论证以本节为准。

<a id="a1-f12"></a>
### A1-F12　g=1 首 strict 边界与单位前缀的完整末端

**状态：有限证书。** g=1,delta=2,e≥1 balanced-tail；g=0,b1=b2=1 balanced-tail。

依赖：[A1-K07](#a1-k07)、[A1-K09](#a1-k09)

核对：`a1-first-strict`、`a1-unit-prefix`

<a id="a1-f12-detail-src-0089-5655-1"></a>
#### `g=1` 的 pure equal-prefix 首 strict 边界

**命题 (LK23)，状态：已严格完成（精确归约接完整有限末端）。**
设 `g=1,b1=b2=10^e,e>=1`，第三分母 balanced，且 `delta=2`。
由 (LK14) 有 `m3=6,c=e+2`，故 `digits(j)=4-e`、`1<=e<=3`。
(LK15) 的完整整除仍给 `j|10^(e+1)+1`。该边界的 product 是
`j=1/9 mod20`，不能使用 strict 更深层的 `11/19` 条件。
当 `e=2`，两个两位 divisors `11,91` 都被该 product 排除。
当 `e=3`，一位 divisor 只有 `j=1`，三个分母都为十进制幂，
由公共 (D9) 排除。因此仅剩
```math
e=1,j=101,\quad b_3=q=101000,\quad n_3=5,
\quad M=100,F0=10001,\quad\alpha=F0H.
```
`d=-1` 已由 (LK2) 排除，`d=2` 已由 (LK19G) 排除。
两层中 `V=q(R-r2)>=1` 都是整数，且原位数给
```math
V<\begin{cases}
\displaystyle\frac{101000(10000+1)}{20\,10^k},&d=0,\\
\displaystyle\frac{101000(1000000+1)}{20\,10^k},&d=1.
\end{cases}
```
故 `d=0` 只余 `1<=k<=7`，`d=1` 只余 `1<=k<=9`。
没有沿用上面的失效 (LK17G) 角点排除。contact cap 只使用
`P>(1-lambda)Zr1`，仍可安全收紧第一分子范围。
原 word 的正确第二坐标 recovery 为
```math
a_3=910100\,Za_1-100910100\,J+10001\,V,
\quad J=Za_1-a_2\ge1.
\tag{LK23}
```
用与 (LK20) 相同的 sphere quadratic，程序完整检查 `2566` prefix、
`30923` 合法 `J`。唯一平方 discriminant 投影是
`d=0,k=1,a1=981,J=489,a2=9321`。两根分别给
`V=6741178441/1667`（非整数），以及 `V=4038687`、
`a3=-26049213`（不在正的五位 tail digit box）。故原合法 root 与解均为零。

证书命令与覆盖见 [统一核对目录](CHECKS.md)。

结合 (LK14)--(LK16)，这还关闭 `g=1` 的全部正奇数 `e` pure equal-prefix /
balanced-tail 状态：`delta=1` 已空，`delta=2` 由本命题排除，
`delta>=3` 的 product 与奇数 `e` 的 divisor `1 mod4` 冲突。
`g=1,e=2` 也全部关闭：`delta=2` 已空，唯一更深合法位数 `delta=3`
会迫 `j=Q0=1001=1 mod4`，同样违反 `11/19 mod20`。
一般 `g=1` 偶数 `e>=4,delta>=3` 的 pure equal-prefix 状态仍开放。

<a id="a1-f12-detail-src-0089-5655-2"></a>
#### `g=0`、两个整数首块的 balanced-tail 状态

**命题 (LK24)，状态：已严格完成（无界五进深度排除接完整有限末端）。**
设 `g=0,b1=b2=1`、`b3=10^c j`、`c>=0,gcd(j,10)=1`。
这里第一、第二分子可以是任意正整数，不能假定它们为 `2/5` unit。
仍有 `q=b3`，且对所有 `p|j`，sphere 与第三分数既约性给 `p not|H`。
原 word 于是给 `j|11`。`j=1` 已由公共 (D9) 排除，所以
```math
b_3=11\,10^c,\quad m_3=n_3=c+2,\quad\beta/q=101,
\quad\alpha=101H.
```
若 `c>=2`，则 `H,a3` 为 `5` unit，word 模五给 `H=a3 mod5`。
真实 sphere gap 给
```math
v_5(H-a_3)=2c+v_5(a_1^2+a_2^2)\ge2c\ge4.
```
但同一个 word 等价于
```math
A12\,10^{c+2}=100a_3+101(H-a_3),
```
左端深度至少四，右端精确深度二，矛盾。因此必有 `c=0,1`。
`d=-1` 时 `n1=0` 不可能，`d=2` 由 (LK19G) 排除。
在其余两层，正整数 `V=H-q a2=q(R-r2)` 满足
```math
V<\begin{cases}
(1991/2)10^{c-k},&d=0\quad(r1\le9,r3<10),\\
55550\,10^{c-k},&d=1\quad(r1<100,r3<10).
\end{cases}
```
所以 `d=0` 只余 `k<=2+c`，`d=1` 只余 `k<=4+c`。
原 recovery 精确为
```math
a_3=qZa_1-1011\,10^cJ+101V,\quad
J=Za_1-a_2\ge1.
\tag{LK24}
```
程序完整覆盖 `c=0,1`、上述所有 `d,k`、第一分子 `1..9` 或 `10..99`，
以及全部合法 `J` 和原 tail digits/reducedness。输出 `855` prefix、
`161` 个 `J`、`0` 个平方 discriminant、`0` 个原 root 和解。

证书命令与覆盖见 [统一核对目录](CHECKS.md)。

该命题关闭全部无界 `c` 的明示 state；它没有关闭 `g>=1,e=0`、
一般首分母 unit 因子或非 balanced 第三分母。


来源：`SRC-0089:5655–5749`。原文保全，当前论证以本节为准。

<a id="remaining"></a>
## 剩余目标

<a id="open-a2"></a>
### OPEN-A2　A2 整分支空性

**状态：待证。** 全部原始正既约三块数据。

依赖：[A2-F01](#a2-f01)、[A2-F02](#a2-f02)、[A2-F03](#a2-f03)、[A2-F04](#a2-f04)、[A2-F05](#a2-f05)、[A2-F06](#a2-f06)、[A2-F07](#a2-f07)、[A2-G10](#a2-g10)、[A2-G11](#a2-g11)、[A2-G12](#a2-g12)、[A2-G13](#a2-g13)、[A2-G14](#a2-g14)、[A2-G15](#a2-g15)、[A2-G16](#a2-g16)、[A2-F09](#a2-f09)、[A2-F08](#a2-f08)、[A2-G08](#a2-g08)、[A2-G09](#a2-g09)、[A2-G06](#a2-g06)、[A2-G03](#a2-g03)、[A2-G04](#a2-g04)、[A2-G05](#a2-g05)、[A2-09](#a2-09)

核对：正文推导；本次重写未为此项另增枚举。

全部第一块已经由 G01 限为 13 种。F05/F06 已排除第二分母两至四位
的整个子层；F01/F02 已排除尾分母一、两位的整个子层，所以余核须
`m2≥5,m3≥3`。F04/F07 还排除三位尾且 `5|b2b3` 的原候选。

奇尾只余第一分子 4、8 的三至六位尾系列。G03 证明这个原候选集合
有限，但没有有效指数界，也未排除其余有限例外。三位奇尾已由 F08
排除后两分母互素的整个子域，非互素余核仍保留。偶尾的二进分类、
五进尾主导、source 桥梁及 gap 分裂见 G04–G08；F03 已排除三至六位
偶尾的两个有界二进类，ordinary 联合系统仍待排除。G10 给固定原
前两块的有效尾界；G09 给固定尾长的非有效有限性，都没有关闭全部
位数的无限并集。全部原候选满足 `m3≤10m2`；后两分母五进单位
时 `m3≤3m2`。G11 的完整非十进制支持和原标签锁仍是必要条件。
G12 已关闭 `b2∣b1·10^m2` 的整个无界子域。G13 关闭一位有效数字
的第二分母；G14 将两位有效数字归约为唯一必要族
`b1=1,a1=2,b2=24·10^(2E−1),b3=8·10^(3E−1)`。F09 将其收紧为
`E≥13,m2≥27,m3≥39`；G15 给原恢复窗、平方和障碍和四组无限
指数余类排除。G16 证明该族在严格实数弧上的有理可行性恰由同一
norm 条件控制，并把原整数恢复等价为两个整数未知量的系统；`E=13`
有精确有理但非整数见证。尚缺的是对所有保留 `E≥13` 证明该整数
系统无点；一般第二分母余核也仍保留。

deep-even 中 `m2≥11` 的系统仍无界。fixed 3、shared 7、其它 terminal
类型、prefix-gcd 与 sphere-height 的联合整数实现没有统一排除。

<a id="open-dd"></a>
### OPEN-DD　DD 整分支空性

**状态：待证。** 全部原始正既约三块数据。

依赖：[DD-10](#dd-10)

核对：正文推导；本次重写未为此项另增枚举。

canonical 余核为 Z=1 mod4 的 ordinary small-gap joint family；noncanonical 余核包括 ordinary circular-lock / source-gap CRT 成功支。渐近排除没有有效绝对上界。

<a id="open-a1"></a>
### OPEN-A1　A1 整分支空性

**状态：待证。** 全部原始正既约三块数据。

依赖：[A1-F12](#a1-f12)、[A1-05](#a1-05)

核对：正文推导；本次重写未为此项另增枚举。

仍有一般 units、非 balanced 分母、放大的 contact/radius 区域；纯等前缀 g=0 偶数 e≥6，g=1 偶数 e≥4 且 delta≥3 仍开放。

<a id="main"></a>
### MAIN　主不存在性命题

**状态：待证。** 全部原始正既约三块数据。

依赖：[C01](#c01)、[OPEN-A2](#open-a2)、[OPEN-DD](#open-dd)、[OPEN-A1](#open-a1)

核对：正文推导；本次重写未为此项另增枚举。

主不存在性命题尚未完成证明。三个完整异常分支仍未全部关闭。
现有绝对界、有限系列和非有效有限性均按各自范围使用，尚未构成三分支的完整空性证明。

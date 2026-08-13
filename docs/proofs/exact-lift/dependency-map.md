# 关键公式依赖图

本文件对应原总稿 §42，用于从 exact lift 追踪到三分支终端系统和最终的 prefix-uniform 缺口。

## 2026-08-13 DD 接续依赖

下列网络覆盖本文件后文的 DD 旧基线；完整公式与证明边界见
[double-deficit.md §27.33](branches/double-deficit.md#2733-2026-08-13-后续合并进展)。

\[
\text{reduced tail }(\kappa,G)=\gamma(u,v)
+F_-Q(\kappa+G)=E\kappa(\kappa+2G)
\Longrightarrow
u(u+2v)\mid F_-Q
\]

\[
\Downarrow\qquad
n_3<\frac{31}{4}S_{12}+\frac{6581}{960},
\qquad
n_3=8S_{12}-1\text{ 为空}
\]

\[
10^{m_3}\mid\kappa^2(\kappa+2G)
+\frac{Q^2}{11}<\kappa<10Q^2
+\text{fixed-target Schmidt Subspace Theorem}
\Longrightarrow
\limsup\frac{m_3}{S_{12}}\le5
\]

\[
\text{unique }2/5\text{-resonant S-unit funnel}
+\text{tail slope collapse}
\Longrightarrow
\limsup_{DD}\frac{n_3}{S_{12}}
\le6.308883577618\ldots
\]

\[
\text{frontier rigidity}
+\text{primitive determinant ladder}
+\text{carrier tetrahedron/projective circle}
+R_2\text{ residue transfer}
\Longrightarrow
\boxed{\text{唯一剩余 moving core }(C_L,\Pi)}
\]

最后一个方框是剩余对象而非矛盾；它不能推出 DD 已关闭。

> 迁移说明：以下正文由原始总稿机械拆分，公式和证明状态不作数学改写。
# 42. 关键公式依赖图

可以把当前全部证明压缩成下面的逻辑网络：

\[
\boxed{
\text{exact lift}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{positive weighted average}
}
\]

\[
\Downarrow
\]

\[
\boxed{
A_2\ \cup\ DD\ \cup\ A_1
}
\]

同时

\[
\boxed{
\text{exact lift}
}
\]

\[
\Downarrow
\]

\[
\boxed{
y_1^2+y_2^2+y_3^2=H^2,
\quad
q\alpha=H\beta
}
\]

\[
\Downarrow
\]

\[
\boxed{
\gcd(q,y_i)=q/b_i
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{denominator prime graph}
}
\]

三个分支分别做第三尾正规化：

\[
\boxed{
(\delta_3,L,\tau)
}
\]

\[
\Downarrow
\]

\[
\boxed{
QG<\kappa\le10QG
}
\]

\[
\Downarrow
\]

\[
\boxed{
\kappa(
\kappa K_{C,D}
-2GD^2\mathcal N_{12}
)
=W^2
}
\]

以及

\[
\boxed{
10^\ell\mid\kappa^2(\kappa+2G)
}
\]

\[
\Downarrow
\]

\[
\boxed{
\ell\le6S_{12}+3
}
\]

随后：

\[
A_2
\Longrightarrow
\boxed{
\text{deep-even}
+
\text{source split}
+
\text{odd inert excess}
+
\text{double Hensel}
}
\]

\[
DD
\Longrightarrow
\boxed{
\text{surplus simplex}
+
\text{near-square}
+
2/5\text{ resonance}
+
\text{near-}S\text{-unit}
}
\]

\[
\text{DD gap valuation}
+
F_-\text{ small-factor height}
+
2/5\text{-adic position split}
\Longrightarrow
\boxed{
\Delta_5>0
\text{ 在五进入口以上为空}
}
\Longrightarrow
\boxed{
n_3\le8S_{12}+6
}
\]

\[
\text{resonance 全赋值保留}
+
F_-<10^{4S+2m_3-n_3+4+\log_{10}2}
+
\text{模 }3\text{ 锁}
\Longrightarrow
\boxed{
n_3\le8S_{12}+5
}
\]

\[
n_3=8S_{12}+5
+
\text{三个二进位置穷尽}
\Longrightarrow
\boxed{
\text{最高整数层为空}
}
\Longrightarrow
\boxed{
n_3\le8S_{12}+4
}
\]

\[
\text{入口以上 resonance}
+
b_3\text{ 二进主导},\ t_2\ge2
+
\text{加权 }m_3\text{ 界}
\Longrightarrow
\boxed{
n_3\le8S_{12}
\text{（该子锥）}
}
\]

\[
n_3=8S_{12}+4
+
\text{其余二进位置排除}
+
t_2=1\text{ 的未粗化 small-factor 界}
\Longrightarrow
\boxed{
\text{十个 }(S,m_3)\text{ 尺寸}
+
\text{统一极端位数形状}
}
\]

\[
\text{十尺寸核}
+
\text{225 个赋值元组}
+
v_2(\kappa+2G)\text{ 的余因子区间证书}
\Longrightarrow
\boxed{
n_3=8S_{12}+4
\text{ 为空}
}
\Longrightarrow
\boxed{
n_3\le8S_{12}+3
}
\]

\[
n_3\in\{8S_{12}+3,8S_{12}+2\}
+
\text{一般 }G<10^S\text{ 余因子区间}
+
\text{16772 个赋值元组有限证书}
\Longrightarrow
\boxed{
\text{两层均为空}
}
\Longrightarrow
\boxed{
n_3\le8S_{12}+1
}
\]

\[
n_3=8S_{12}+1,\ S\ge4
+
\text{48808 个赋值元组}
+
\text{唯一余因子与模 }3\text{ 判别式矛盾}
\Longrightarrow
\boxed{
\text{该层只剩 }S=2,3
}
\]

\[
\text{非 dominant 的 }n_3\le7S+3
+
S=2,3\text{ 的统一尾权有限核}
+
\text{二/五进必要条件与十个判别式}
\Longrightarrow
\boxed{
n_3=8S_{12}+1
\text{ 整层为空}
}
\Longrightarrow
\boxed{
n_3\le8S_{12}
}
\]

最后这个界仍是相对线性界，不是 DD 的 prefix-uniform 绝对高度界；
\(S=2,3\) 的步骤是明确有界的有限证书，不覆盖更低无界层。

在新的等号层还有进一步分解：

\[
n_3=8S_{12},\ S\ge11
+
\text{五进入口与二进位置强制}
\Longrightarrow
\boxed{
b_3\text{ 二进主导},\quad t_2\ge1
}
\]

\[
t_2=1
+
\text{70 个尺寸与 51828 个赋值行}
+
\text{精确模余因子计数}
\Longrightarrow
\boxed{
S\ge11\text{ 的 }t_2=1\text{ 边界为空}
}
\]

\[
t_2\ge2
+
\text{加权 }m_3\text{ 界}
+
\text{squarefree gap 取等}
\Longrightarrow
\boxed{
m_3=3S,\ d_3=5S,\
\kappa=10^{2S}c,\ 1\le c\le8,\
10^{S-3}\mid b_3
}
\]

后一个方框是八个无界常数核族，不是有限候选。它们与
在这一中间节点，\(2\le S\le10\) 仍只是入口下的有限 \(S\)-列表，
并非完整有限候选盒，所以单凭这里还不能推出
\(n_3\le8S_{12}-1\)。

随后八核还满足

\[
F_-=10^{2S}\rho,
\quad0<\rho<20000
+
\text{primitive recovery 与 gap 的两个 }\mu/\nu\text{ 式}
\Longrightarrow
\boxed{
\frac{c10^{2S}+2G}{\gcd(c10^{2S},G)}\mid\rho Q
}
\]

\[
\frac{\gcd(c10^{2S},G)}c\le128
+
Q<10^S
\Longrightarrow
\boxed{
n_3=8S_{12}\Longrightarrow S\le10
}
\]

所以八个无界核现已关闭；在这一中间节点仍待处理的是
\(2\le S\le10\) 的等号层有限 \(S\)-列表与 \(n_3<8S\) 的无界
区域。此时统一界仍为 \(n_3\le8S\)，但对 \(S\ge11\) 已有更强的
\(n_3\le8S-1\)。

对小切片中的唯一五进正规形还有：

\[
4\le S\le10,\ t_2=1
+
\text{同步 }F_-\text{ 因子界}
+
\text{余因子与真实分母证书}
\Longrightarrow
\boxed{
\text{唯一尾核模 }3\text{ 非平方}
}
\]

\[
t_2\ge2,\ S\ge7
+
\text{大除数无界矛盾}
\quad\text{或}\quad
S\in\{4,5,6\}
+
\text{真实分母有限证书}
\Longrightarrow
\boxed{
\text{该正规形在 }4\le S\le10\text{ 全空}
}
\]

这个方框只指
\(e_5=q_5,k_5>g_5,h_5=f_5=g_5\) 的唯一五进正规形；普通入口下
resonance、\(5\nmid b_3\) 与 \(\Delta_5^\pm\) 不在其覆盖范围。

最后对全部剩余五进状态：

\[
S\ge4,\ n_3=8S,\ 5\mid b_3
+
\text{位数 gap 锁 }e_5=q_5
+
\text{三种五进状态穷尽}
\Longrightarrow
\boxed{
5\mid b_3\text{ 的等号层为空}
}
\]

\[
5\nmid b_3
+
\text{尾权 }\kappa=2\cdot5^{3S}
+
\text{二进 resonance 剩余类}
\Longrightarrow
\boxed{
5\nmid b_3\text{ 的等号层为空}
}
\]

\[
\Longrightarrow
\boxed{
n_3=8S_{12}\Longrightarrow S_{12}\in\{2,3\},
\qquad
S_{12}\ge4\Longrightarrow n_3\le8S_{12}-1
}
\]

最后两个尺寸按 dominant 性质分开：

\[
S\in\{2,3\},\ n_3=8S,
\ \text{non-dominant}
+
m_3\ge7S
+
\text{primitive denominator-tail 核}
\Longrightarrow
\boxed{\text{该扇区为空}}
\]

这里尾核分别在 \(m_3=10,17\) 后为空，而 non-dominant 分别要求
\(m_3\ge14,21\)，所以没有截断无界 prefix surplus。

\[
S\in\{2,3\},\ n_3=8S,
\ \text{dominant}
+
n_1+n_2\le S+2
+
\text{两素数三状态与 squarefree gap}
+
\text{703、38633 个判别式}
\Longrightarrow
\boxed{\text{该扇区为空}}
\]

\[
\Longrightarrow
\boxed{
n_3=8S_{12}\text{ 整层为空},
\qquad
n_3\le8S_{12}-1
}
\]

最后一步只有 dominant 子扇区使用明确有界的 numerator 有限证书；
更低的 \(n_3\le8S-1\) 无界区域仍为 `待证`。

再把第 25 节的取等层补齐到全部小尺寸：

\[
S\ge5\text{ 的 }2,5\text{-单位间距}
+
S=2,3\text{ 的完整尾表}
+
S=4,m_3=27\text{ 的零尾核}
\Longrightarrow
\boxed{m_3\le6S+2}
\]

\[
m_3\le6S+2
+
\text{non-dominant 时 }d_3\le S
\Longrightarrow
\boxed{n_3\le7S+2\text{（non-dominant）}}
\]

所以 \(n_3=8S-1\) 对所有 \(S\) 都进入 dominant 扇区。在
\(S\ge18\) 的五进入口以上还有

\[
t_2\ge2
+
m_3=3S-1+j,\quad j\in\{0,1,2\}
+
\kappa=\frac{c10^{2S}}2,\quad1\le c<20
+
\text{19、9、0 个常数核}
\Longrightarrow
\boxed{\text{大除数矛盾}}
\]

\[
t_2=1
+
\text{45 个尺寸与 15525 个 valuation rows}
+
\text{精确 floor-sum 余因子证书}
\Longrightarrow
\boxed{S\ge18\text{ 的该支为空}}
\]

\[
\Longrightarrow
\boxed{
n_3=8S_{12}-1
\Longrightarrow
d_3=\max(s_1,s_2,d_3),\quad S_{12}\le17
}
\]

这个方框只证明最高允许层已成为有限原问题切片；该有限盒尚未核验
为空，\(n_3\le8S-2\) 的无界区域也仍为 `待证`。

对这个有限盒的两个最小尺寸：

\[
S\in\{2,3\},\quad n_3=8S-1
+
\text{2665、126669 个 dominant tail rows}
+
\text{两素数三状态与无溢出 squarefree gap}
+
\text{24396、1582338 个统一判别式}
\Longrightarrow
\boxed{\text{两个尺寸均为空}}
\]

\[
\Longrightarrow
\boxed{n_3=8S_{12}-1\Longrightarrow4\le S_{12}\le17}
\]

这里的空性是明确有界的有限证书；在下面继续处理 \(S=4\) 之前，
\(4\le S\le17\) 尚未核验。

同一最高层还有新的通用过滤与首个逐尾长证书：

\[
F_-=\frac{2(\kappa+2G)\mu^2}{G_0}
+
10^{m_3}QG_0=2\kappa\mu\nu
+
\frac{\mu}{\nu}
=\frac{E\kappa^2}{10^{m_3}Q^2(\kappa+G)}
\Longrightarrow
\boxed{
\frac{\mathfrak L_F}{\gcd(\mathfrak L_F,Q)}\mid F_-
}
\]

其中

\[
\mathfrak L_F=
\frac{\kappa(\kappa+2G)}
{\gcd(\kappa(\kappa+2G),\kappa+G)}.
\]

这个大除数不要求 resonance。进一步，最低四层给出

\[
S=4,\quad n_3=31,\quad m_3\in\{11,12,13,14\}
+
\text{squarefree-gap 位数核}
+
\text{精确二次区间与两素数三状态}
+
\text{694825、10987773、714489、99342 个大整数判别式}
\Longrightarrow
\boxed{m_3\ge15\text{（该 }S=4\text{ 切片）}}
\]

再由

\[
m_3\in\{15,\ldots,21\}
+
\text{流式精确两素数剩余树与统一判别式}
+
\text{固定全量计数中零个平方}
\Longrightarrow
\boxed{15\le m_3\le21\text{ 为空}}
\]

以及

\[
m_3\in\{22,\ldots,26\}
+
\text{primitive denominator-tail divisor tree}
\Longrightarrow
\boxed{\text{tail 核为空}},
\]

最终得到

\[
\boxed{S=4,\ n_3=31\text{ 为空}}
\Longrightarrow
\boxed{n_3=8S-1\Longrightarrow5\le S\le17}.
\]

这里仍是明确有界的有限证书；\(5\le S\le17\) 与更低无界层尚未
关闭。

下一个尺寸的高尾依赖链为

\[
S=5,\quad n_3=39
+
22\le m_3\le26
+
\text{128 位两素数剩余树与多精度统一判别式}
\Longrightarrow
\boxed{22\le m_3\le26\text{ 为空}},
\]

以及

\[
27\le m_3\le32
+
\text{primitive denominator-tail divisor tree}
\Longrightarrow
\boxed{\text{tail 核为空}}.
\]

再有最低层依赖链

\[
S=5,\quad n_3=39,\quad m_3=14
+
\text{唯一位数形状}
+
\text{四角、valuation box、}L_F\text{ 与 denominator-unit box}
+
\text{75 条 primitive tails 的完整两素数状态}
\Longrightarrow
\boxed{m_3=14\text{ 为空}}.
\]

再接上下一层的完整有限链

\[
S=5,\quad n_3=39,\quad m_3=15
+
\text{三个严格位数形状}
+
\text{四类 numerator-free 必要过滤}
+
\text{完整两素数状态与多精度判别式}
\Longrightarrow
\boxed{m_3=15\text{ 为空}}.
\]

同理，下一层的七个严格位数形状给出

\[
S=5,\quad n_3=39,\quad m_3=16
+
\text{完整两素数状态与多精度判别式}
\Longrightarrow
\boxed{m_3=16\text{ 为空}}.
\]

所以

\[
\boxed{
S=5,\ n_3=39
\Longrightarrow
17\le m_3\le21,
\quad18\le d_3\le22.
}
\]

这个结论不排除其余五个尾层，也不改变 DD 更低层的无界性。

\[
A_1
\Longrightarrow
\boxed{
\text{thin annulus}
+
\text{slope lock}
+
\text{saturated tail bound}
}
\]

最终都汇入同一个尚未完全解决的问题：

\[
\boxed{
\text{如何对无界前缀得到 prefix-uniform contradiction?}
}
\]

---

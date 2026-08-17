# 关键公式依赖图

本文件对应原总稿 §42，用于从 exact lift 追踪到三分支终端系统和最终的 prefix-uniform 缺口。

## 2026-08-13 DD 接续依赖

下列网络覆盖本文件后文的 DD 旧基线；完整公式与证明边界见
[DD 主干 §27.33](branches/double-deficit/core.md#2733-2026-08-13-后续合并进展)。

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

并且在最危险 endpoint core 中：

\[
\text{endpoint shell}
+
\rho^2\text{ high-2 slot}
\Longrightarrow
\boxed{
\eta=-1,0\text{ 排除},
\quad
\eta=1\text{ 压成五型}
}
\]

但

\[
\boxed{
\text{粗 slot 有真实区间交点}
}
\Longrightarrow
\boxed{
\text{后续必须加入 prefix/source/CRT 条件}
}
\]

\[
\eta=1\text{ 五型}
+
\text{exact high/low factor}
\Longrightarrow
\boxed{
\text{模 }515,795,775,53\text{ 的有限相位}
}
\]

但真正覆盖无界层的接口是

\[
\text{任意 }\eta\text{ 的 reflection high-2}
+
c_Q=c_-c_+\text{ square-side allocation}
\Longrightarrow
\boxed{
5^dc_-\mid \frac{k_hg}{2}-a_3,
\quad
c_+\mid \frac{k_hg}{2}+a_3
}
\]

并进一步推出

\[
\boxed{
gr_-\equiv\varepsilon a_2c_+
\pmod{5^{\lambda-d}},
\qquad
\lambda-d\ge\lambda/2
}
\]

再与 source Hensel 和 `v_5(N_0)=lambda-2d` 合并：

\[
\boxed{
r_-\equiv
\varepsilon\iota\,9\cdot2^{M+m}c_+c_u
\pmod{5^{\lambda-2d}},
\quad
\iota^2\equiv-1
}
\]

\[
\Downarrow
\]

\[
\boxed{
r_-^2+(9\cdot2^{M+m}c_+c_u)^2
=k_h5^{\lambda-2d}X,
\quad
\gcd(r_-,9\cdot2^{M+m}c_+c_u)\mid9
}
\]

共同 Gaussian `5`-depth 归一化后：

\[
\boxed{
v_5\!\left(
\operatorname{Im}(\mathcal R_5\overline{\mathcal A_5})
\right)=d
}
\]

\[
\boxed{
r_+^2+(9\cdot2^{M+m}c_uc_-5^d)^2=k_hY
}
\]

并有精确 Gaussian composition

\[
\boxed{
\mathcal R_5\overline{\mathcal A_5}
=X\left(
\varepsilon r_+-i\,9\cdot2^{M+m}c_uc_-5^d
\right)
}
\]

\[
\Downarrow\quad(\mathbb Z[i]\text{ 唯一分解})
\]

\[
\boxed{
N(\alpha_X)=X/3^{v_3(X)},
\quad
\alpha_X\mid\mathcal A_5,\mathcal R_5
}
\]

\[
\boxed{
v_3(X)+v_3(Y)\le4,
\qquad
v_3(k_h)\le4
}
\]

奇 `3`-defect 的进一步分类：

\[
\boxed{
v_3(k_h)\text{ odd}
\Longrightarrow
\begin{cases}
v_3(a_3)=1,\ v_3(k_h)=1,\ v_3(a_2)\ge2,\\
\text{or}\\
v_3(a_2)=1,\ v_3(a_3)\ge2,\ v_3(k_h)\in\{1,3\}
\end{cases}
}
\]

\[
\boxed{
v_3(H)=v_3(\alpha)=1,
\qquad
v_3(\beta)=0
}
\]

平衡转移公共奇偶性 `delta`：

\[
\boxed{
N(\alpha_X^\sharp)=3^\delta X,
\quad
\alpha_X^\sharp\mid\mathcal A_5,\mathcal R_5
}
\]

\[
\boxed{
N(\mathcal B_5)=Y/3^\delta,
\quad
N(\mathcal G_5)=k_h/3^\delta,
\quad
\varepsilon r_+-iR_1
=3^\delta\mathcal G_5\overline{\mathcal B_5}
}
\]

消去共同 divisor 后的 source Hensel kernel：

\[
\boxed{
\pi_\iota^d\bar\pi_\iota^{\lambda-d}
\mid
c_u\mathcal G_5
-\varepsilon c_+\omega\mathcal B_5
}
\]

\[
\boxed{
5^\lambda
\mid
N(c_u\mathcal G_5
-\varepsilon c_+\omega\mathcal B_5)
}
\]

而且该同余提升为精确商：

\[
\boxed{
c_u\mathcal G_5-\varepsilon c_+\omega\mathcal B_5
=\pi_\iota^d\bar\pi_\iota^{\lambda-d}\mathcal W_5,
\qquad
v_{\pi_\iota}(\mathcal W_5)=0
}
\]

`theta` 同伴与上式只差一个已含完整 `5^lambda` 的项，故不是独立
obstruction。原 decimal plane 另外给出

\[
\boxed{
5^\lambda C
=g(a_3+3\cdot10^m)
+\varepsilon a_2c_Q5^d
-g^2k_h/2,
\qquad
0<C<\mathfrak L_0/1000
}
\]

同一个精确商还有统一 Archimedean 方向：

\[
\boxed{
4<\tan\arg(-\varepsilon\mathcal S_5)<5,
\qquad
\operatorname{sgn}
\left(
\arg(-\varepsilon\mathcal S_5)-\arg(a_2+iC_0)
\right)=\varepsilon
}
\]

约掉共同 `X` 后的有向面积为

\[
\boxed{
\operatorname{Im}
\left(
\mathcal W_5\bar\pi_\iota^{\nu_5}
\overline{\mathcal B_5}
\right)
=-\frac{c_uR_1}{3^\delta5^d}
}
\]

精确商再乘回共同 `5`-orientation：

\[
\boxed{
5^{\lambda-d}\mathcal W_5
+\varepsilon c_+\omega
\pi_\iota^{\nu_5}\mathcal B_5
=c_u\pi_\iota^{\nu_5}\mathcal G_5,
\qquad
\left|c_u\pi_\iota^{\nu_5}\mathcal G_5\right|
<5^{\lambda-d}/5
}
\]

因此右端是模 \(5^{\lambda-d}\mathbf Z[i]\) 的唯一中心 Gaussian
代表；剩余目标是把其 norm / area 与 `C` 代表联立排除。

进一步比较中心误差与主向量，得到

\[
\frac{
|c_u\pi_\iota^{\nu_5}\mathcal G_5|
}{
c_+\omega|\pi_\iota^{\nu_5}\mathcal B_5|
}
<\frac1{7680}.
\]

所以 \(\mathcal W_5\) 是逐坐标唯一最近整数商，并且

\[
\boxed{
0<\varepsilon
\left(
\tan\arg(-\varepsilon\mathcal S_5)-\frac{C_0}{a_2}
\right)
<\frac7{2000}
}
\]

即 Gaussian 商被压到真实 decimal prefix slope 的确定单侧窄条带；
下一步须将这个确定商与 `C` 自然代表联立，而不是继续增加粗角窗。

把 quotient slope 精确展开，并用

\[
C_0\mathcal U=\frac92wa_2,
\qquad
\mathcal K C_0=9\cdot2^Mc_Qq+\frac92w
\]

消去两项 decimal contribution，可进一步得到

\[
\boxed{
0<\varepsilon
\left(
\tan\arg(-\varepsilon\mathcal S_5)-\frac{C_0}{a_2}
\right)
<\frac1{a_2}
}
\]

以及

\[
\varepsilon=+1:\ 
C_0=\lfloor a_2\tan\phi_S\rfloor,
\qquad
\varepsilon=-1:\ 
C_0=\lceil a_2\tan\phi_S\rceil.
\]

所以提升后 quotient \(\mathcal S_5=\alpha_X^\sharp\mathcal W_5\) 的
方向唯一解码原 prefix 系数。由于它仍含共同 Gaussian factor，这尚未
给出裸 quotient 的 absolute argument；后者以及完整尺度、
\(a_2\) 与 `C` 仍待恢复。

方向条带的有向面积还满足

\[
\boxed{
\frac35<\frac{\Delta_S}{X_S}<\frac45,
\qquad
X_S=\Delta_S+E_S,
\qquad
\frac14\Delta_S<E_S<\frac23\Delta_S
}
\]

故出现商恰为 `1` 的正 Euclidean step；其 Gaussian norm 与 decimal
plane 协变性是下一条明确的下降缺口。

该实线性 step 的 determinant 实为 \(-\varepsilon a_2\)，因此不保持
Gaussian norm。真正的 quotient-pair Euclidean step 是

\[
Q_E=\operatorname{nint}
\left(\frac{c_+\omega}{5^{\lambda-d}}\right),
\qquad
\mathcal R_E=-\varepsilon\mathcal W_5-Q_E\mathcal V_5,
\]

并严格满足

\[
\boxed{
0<N(\mathcal R_E)<\frac14N(\mathcal V_5),
\qquad
v_{\pi_\iota}(\mathcal R_E)=0
}.
\]

下一依赖边是证明 \(\mathcal R_E\) 的 decimal-plane / Hensel covariance；
若不能建立，该 Gaussian norm descent 仍不能迭代成 A2 descent。

同时

\[
\mathfrak K_5\mathcal R_E
=r_E\mathcal B_5-\varepsilon c_u\mathcal G_5,
\qquad
r_E\equiv c_-^{-1}\theta\pmod{5^{\lambda-d}},
\]

且 \(r_E\) 是中心区间内唯一的 `5`-进单位代表。取 norm：

\[
\boxed{
5^\lambda N(\mathcal R_E)
=
\frac{Yr_E^2-2c_ur_+r_E+c_u^2k_h}{3^\delta},
\qquad
\operatorname{disc}=-4c_u^2R_1^2.
}
\]

故二维 quotient kernel 最终依赖到唯一 scalar representative 的一维
正定二次核；剩余边是排除其长 orientation 或建立 decimal child。

Hensel slot 的真实 decimal lift 为

\[
g\varrho=5^{\lambda+1}H-c_Qc_u,
\qquad
z_E=\frac{gr_E-c_+c_u}{5^{\lambda-d}},
\]

其中

\[
-g/2<z_E<g/2,
\qquad
c_-z_E\equiv-5^{d+1}H\pmod g.
\]

代入标量核：

\[
\boxed{
3^\delta g^2N(\mathcal R_E)
=5^{\nu_5}Yz_E^2
-2\varepsilon c_ua_2c_-z_E+c_u^2c_-^2X,
\quad
\operatorname{disc}=-4c_u^2c_-^2C_0^2.
}
\]

相应 Gaussian 向量可约去完整 \(g\)，且

\[
\frac{U_E+i\varepsilon V_E}{g}
=3^\delta\bar\pi_\iota^{\nu_5}
\mathcal R_E\overline{\mathcal B_5}.
\]

这条边把 `H` 与 prefix vector 接入 quotient composition；下一依赖仍是
decimal-child covariance 或与 `C` 代表的直接矛盾。

顶部代表与第二层代表继续合并为

\[
c_uC+\varepsilon a_2c_-z_E=g\chi_E,
\]

但完整 `g`-约分产生的 canonical Gaussian child 斜率严格落在
\((0,1/3999)\)（乘 unit 后落在 \((3999,\infty)\)），因此不能回到
A2 prefix window \((9/2,5)\)。这关闭的是同型下降路线，不是原候选。

独立的 rational-root 边则变为

\[
\boxed{
\Xi_C=\frac{F(3)}{2^{2M+2}5^{\nu_5}C}
\in\mathbf Z_{>0},
\quad
\gcd(\Xi_C,10)=1,
\quad
\Xi_C\equiv q^2c_+^2Y(3T+a_3)^2\pmod D.
}
\]

其相邻平移同时给出

\[
\boxed{
D-C\mid F(2),\qquad D+C\mid F(4),\qquad
\gcd(D-C,D+C)=1,
}
\]

并产生正奇 `5`-进单位 `Xi_-,Xi_+`。三个 cofactor 均满足

\[
\Xi_\bullet\equiv Y(qc_+a_3)^2\pmod{2^m5^d}.
\]

mixed bridge 还给出

\[
\gcd(c_uH,g)=1,\qquad
\operatorname{sgn}\chi_E=\operatorname{sgn}(\varepsilon z_E),
\qquad
\left|
\frac{g\chi_E}{\varepsilon a_2c_-z_E}-1
\right|<\frac3{50000}.
\]

且对 \(p^e\Vert g\)，

\[
\min\{v_p(\Xi_C),e\}
=\min\{2v_p(3T+a_3),e\};
\]

唯一需保留的零因子分支是 \(3T+a_3\) 的饱和通道。

非饱和奇素通道继续消去全部中心变量后：

\[
\boxed{
\left(\frac{\Xi_C}{p}\right)
=\left(\frac{-\varepsilon a_25^{M+d}}p\right),
\qquad
p\mid g,\quad p\nmid3T+a_3.
}
\]

二阶提升审计：

\[
\Xi_C\equiv
Y(qc_+(3T+a_3))^2(1-3DC^{-1})\pmod{g^2},
\]

\[
\boxed{
1-3DC^{-1}\text{ 在 }g^2\text{ 的每个 prime-power 分量上为平方}.
}
\]

故 quadratic-character 加深不再是一条独立依赖边。

三点 secant cubic 的 non-character 边：

\[
\Delta_-=\frac{\Xi_C-\Xi_-}{2^m5^d},
\qquad
\Delta_+=\frac{\Xi_+-\Xi_C}{2^m5^d},
\]

\[
\boxed{
1<\frac{\Delta_-}{\Delta_+}<2,\qquad
v_2(\Delta_-)=v_2(\Delta_+)=1,
}
\]

\[
\boxed{
\Delta_--\Delta_+
=2^{m+1}5^dc_u^2
\{g((20P-9)T-a_3)-H_0\},
}
\]

\[
v_2(\Delta_--\Delta_+)=m+1,\qquad
v_5(\Delta_--\Delta_+)=d.
\]

中心二阶差分继续给出

\[
\mathcal T_2=(D+C)\Delta_++(D-C)\Delta_-,
\]

从而 \(\Delta_+\) 落入模 \(D^2-C^2\) 的唯一显式 CRT 类。新的开放量为
\[
Q_\Delta=\left\lfloor\Delta_+/(D^2-C^2)\right\rfloor.
\]

中心二阶差分先给出 once-normalized
\(\widetilde{\mathcal T}_2\)，且
\(v_5(\widetilde{\mathcal T}_2)=d\)。真正的 \(2,5\)-primitive
additive cofactor 是

\[
\widehat{\mathcal T}_2
=\mathcal T_2/(2^{m+1}5^{2d}),
\]

并满足：

\[
\boxed{
\widehat{\mathcal T}_2
\equiv-5^{\lambda-d}(c_uC)^2\pmod g,
\qquad
\widehat{\mathcal T}_2\equiv3\pmod4,
\qquad
\gcd(\widehat{\mathcal T}_2,10c_ug)=1.
}
\]

因此它含有外部 \(3\bmod4\) 素数到奇次；待证边是
\[
5^d\widehat{\mathcal T}_2
=5^{\epsilon_5}Z_\nu^2+\mathscr J_\Delta,
\qquad
\mathscr J_\Delta\equiv2\pmod4.
\]

这与旧 odd inert excess 是同一机制；待证边改为排除
\(\mathscr J_\Delta\) 的 denominator-prefix / source / spontaneous
三类 prime 来源。

显式审计：
\[
\widehat{\mathcal T}_2
=2^mc_u^2g^2\mathscr S_0
-(c_Qq)^2 5^{2\lambda-d}XY.
\]
当前 norm difference 没有精确 orientation / inner-product identity；
canonical square 代入后只恢复上述 odd inert excess。

prime-source 接触边：
\[
\gcd(\widehat{\mathcal T}_2,Q_0XY)
=\gcd(\mathscr S_0,Q_0XY),
\qquad
\gcd(\widehat{\mathcal T}_2,f)
=\gcd(\mathscr R_f,f).
\]
非 \(3\) inert prime 不进入 \(XY,c_u,g\)；固定 \(3\) 的一阶接触由
\(3\mid Q_0\) 与 \(a_2a_3\bmod3\) 的 (16.310) 分类。剩余边是排除
\((q,\mathscr S_0)\)、\((f,\mathscr R_f)\)、source
\(\mathfrak n\) 与 endpoint-external 通道。

curvature character 边：
\[
\operatorname{disc}_K(\mathscr S_0)=8\mathscr R_{23},
\qquad
\operatorname{disc}_K(\mathscr R_f)=8A_f\mathscr R_{23,f}.
\]
其中 \(\mathscr R_{23}\) 是判别数 \(-23\) 的二元型；simple-root
\(q\)-contact 给 (16.316)，double-root 给 (16.318)，
\(f\)-contact 给 (16.320)。剩余依赖是把这些 \(23\)-分裂条件与
source / factor-allocation character 联立成矛盾。

全局配方审计边：
\[
\left[c_ug(TK-9T-2a_3)\right]^2
=\mathscr C_{23}+5^m\widehat{\mathcal T}_2.
\]
所以前述 curvature character 都是 (16.323) 的 principal-square
投影；必须另取 source/prefix 的独立 character，不能重复收费。

cross-field companion：
\[
\mathscr C_{23}
=U_{23}^2+23V_{23}^2+5^{3\lambda}Q_0^2XY,
\]
且它模 \(5^{2m}\) 为 principal square、模 \(8\) 为 \(1\)。因此
\(2,5\)-进局部非平方边已降级；剩余边只能来自 odd-prime
orientation 或实数 gap。

canonical shifted-factor 边：
\[
\mathscr V_-=5^\lambda fc_-^2X-\mathscr E_{23},
\qquad
\mathscr V_+=5^\lambda qc_+^2Y-\mathscr E_{23},
\]
\[
\gcd(\mathscr V_-,f)=\gcd(\mathscr L_{23},f),
\quad
\gcd(\mathscr V_+,q)=\gcd(\mathscr L_{23},q),
\quad
\gcd(\mathscr V_-,\mathscr V_+)
=\gcd(TK-9T-2a_3,Z).
\]
消去 \(Z\) 的 \(\mathscr D_Z\) 满足
\[
\gcd(\mathscr D_Z,qf)=\gcd(\mathscr L_{23}^2,qf),
\]
故未饱和 denominator contact 全为偶赋值，剩余依赖缩成
\(p^e\Vert qf,\ p^e\mid\mathscr L_{23}\) 的 saturation。

模 \(4\) orientation 边：
\[
q\equiv3,\quad f\equiv1,\quad
X\equiv Y\equiv-Z\pmod4.
\]
\(Z\equiv1\) 对应固定 \(3\) balanced transfer，shifted pair 恰共享
一份 \(3\) 且 \(3\nmid\widehat{\mathcal T}_2\)；
\(Z\equiv3\) 对应 denominator \(q\) carrier。

saturation Hensel-target 边：
\[
\mathscr G_q=5^{M-1}(a_3-90T)+a_3H,
\qquad
\mathscr G_f=\mathscr G_q-18\cdot2^{m+1}c5^d.
\]
剩余 denominator 候选必须满足
\[
p^e\Vert q,\ p^e\mid\mathscr G_q
\quad\text{或}\quad
p^e\Vert f,\ p^e\mid\mathscr G_f.
\]
下一依赖是用 \(C\) 自然代表/source phase 对这两个完整
prime-power gcd 作无界排除。

\(q\)-saturation amplification：令
\(a_p=v_p(c_Q)\)、\(n_p=a_p+e\)。rational-root 等式给出完整
prime-power budget；middle branch 满足
\[
v_p(gs_p-5^\lambda r_p)=e+2a_p,
\]
third branch 在 generic 层满足
\(v_p(KD-N)=n_p\)。若同时是 \(q\)-侧 additive-cofactor carrier，
则
\[
\mathscr S_0=T(K^2-26)-(2K-9)(2a_3+9T),
\qquad K^2\equiv26\pmod p.
\]
这排除第一 valuation branch，并把结构例外压到固定素数
\(11,23\)。下一依赖是排除这两个固定 prime 的无限 Hensel lift，
并关闭 middle/third 的精确 residual-unit character。
在 \(p\nmid c_Q\) 的 generic 层，\(f\)-侧 saturation 不落在同一个零点，而满足
\[
K^2-26\equiv
\left(\frac{2c_Q}{2^m5^\lambda g}\right)^2N_0\not\equiv0\pmod p.
\]
\(p\mid c_Q\) 时该式退化回零点，正是显式 overlap。
\(q\)-侧另有 prefix bridge
\(J_{101}^2\equiv101N_0-26\pmod p\)；下一 character/resultant
必须同时使用这些 Gaussian-prefix 数据。
canonical factor allocation 还直接给出
\[
p\mid q\Longrightarrow N\equiv DK\pmod p.
\]
因此 generic middle branch 被删除，\(p\ne11,23\) 时唯一剩
\(v_p(KD-N)=v_p(c_Qq)\)；固定 \(11\) 是 middle/third overlap，
固定 \(23\) 是 right rational-root factor 的额外增深。
整数层还有
\[
q\mid DK-N,\qquad
2c_u(DK-N)/q=c_+^2Y+5^\lambda c_-^2X.
\]
在 saturation 内，两侧的截断赋值分别只读取
\[
K^2-26,\qquad
\Psi_f=b_2^2(K^2-26)-Q^2N_0>0.
\]
而 \((DK-N)/q\) 的非 \(3\) inert prime 满足
\(v_r((DK-N)/q)=v_r(H_0)\) 与 \((N_0/r)=-1\)。
下一依赖因而是两个纯 prefix gcd 加一个明确 sphere-height channel。

\[
Q_\Delta\ge5K,
\]

故 CRT 商路线仍含一个无界大商。

因此当前新增依赖边是

\[
\boxed{
(z_E,\chi_E)\text{ 中心核}
+
(\Xi_-,\Xi_C,\Xi_+)\text{ 三点平方类}
\Longrightarrow \text{待证矛盾}.
}
\]

所以后续主线是统一定向因子系统与 source 双 Hensel / prefix defect
的矛盾，具体即排除这个 `C` 的唯一自然代表或建立合法降高，而不是
继续固定 `eta` 枚举。

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

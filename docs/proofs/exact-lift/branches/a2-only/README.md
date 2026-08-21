# `A_2`-only 分支

这是 `A_2` 分支的唯一规范编辑入口。主线结论保留在六个规范专题文件中；大量细粒度 continuation 已按依赖机械归并为五本研究账本。不要再在本目录新增同一主题的平行副本。

## 阅读顺序

1. [`core.md`](core.md)：原 §§12–16 的 terminal 主干、开放核和历史状态。
2. [`phase-and-defect.md`](phase-and-defect.md)：decimal ellipse → finite-defect remainder → 两个低商状态的 angle squeeze；文件内部按三个来源的依赖顺序排列。
3. [`hensel.md`](hensel.md)：source 双 Hensel/resultant 恒等式及 source-excess 审计。
4. [`endpoint-lattice.md`](endpoint-lattice.md)：2026-08-17 的 endpoint shell、height split、Gaussian allocation 和降级结论。
5. [`prime-source.md`](prime-source.md)：在 endpoint lattice 的最终 prime-source 层继续吸收固定 `11,23` Hensel 例外，并把 special `23` height carrier 压成 `M mod 22` 的有限同余类。
6. [`primitive-reduction.md`](primitive-reduction.md)：识别 `W_q` 为拼接分子/球面高度的 primitive gcd 与 reduced numerator，审计 height character，并分离 q/f saturation 与 height channel 的交集；最新把 f-height 交集压到固定素数 `7,43` 并排除共同二阶深接触。

## 研究账本

账本保留被归并文件的原标题、正文、证明状态和来源锚点，供审计与回溯；新增主结论应先回写上面的规范专题与本 README，而不是继续增加平行小文件。

- [`auxiliary-reductions-ledger.md`](auxiliary-reductions-ledger.md)：decimal、length-orbit、source discriminant 等辅助降维。
- [`source-angle-ledger.md`](source-angle-ledger.md)：spontaneous source、angle、cross-sign、tangent 与 parity 记录。
- [`crt-descent-ledger.md`](crt-descent-ledger.md)：additive CRT、descendant、height descent 与 projective reader。
- [`height-ledger.md`](height-ledger.md)：moving height、equal-depth、tail reader 与固定低层审计。
- [`fixed23-and-cq-ledger.md`](fixed23-and-cq-ledger.md)：pure-`c_Q`、固定 `23` 及其 Hensel/height continuation。

## 当前状态

本分支仍为 `待证`：已有严格的局部压缩、有限证书和若干 `失效/降级` 审计，但没有关闭 `m_2\ge11` 的无界 deep-even 核。`endpoint-lattice.md` 现已严格排除 reflection high-2 的 `eta=-1,0`，并把 `eta=1` 压成五个 Gaussian-support-compatible 类型。更重要的是，§16.7–16.41 已把任意 `eta` 的 high/low equality、Gaussian quotient 与三点 rational-root cofactors 接成同一严格链；平衡转移至多一份 `3` 后，所有共同 prime allocation 都可消去。裸 quotient pair 的 Gaussian 除法已有唯一纯实首商 `Q_E`，非零余数 norm 严格下降四倍；大系数 `c_+omega` 随后降成唯一中心 `5`-进单位 `r_E`。其提升商 `z_E` 是由真实 denominator 缺口 `H` 模 `g` 唯一决定的中心奇代表，并与顶部补余量组成整数核 `(z_E,chi_E)`。代入后得到 discriminant 为 `-4c_u^2c_-^2C_0^2` 的 prefix norm；全部 `g`-common factor 可严格约去，并精确识别为 `R_E overline(B_5)` composition。直接同型 Gaussian child 的斜率已被证明远离 A2 prefix window，因此该下降路线严格降级。

独立的 rational-root 条件现已精确正规化：
\[
\Xi_C=\frac{F(3)}{2^{2M+2}5^{\nu_5}C}
\]
是正奇 `5`-进单位，且 `Xi_C/Y` 在 `2^m5^d` 上是显式平方类；相邻整数点还强迫互素的 `D-C,D+C` 分别整除 `F(2),F(4)`，产生共享同一 denominator 平方类的正 cofactor `Xi_-,Xi_+`。下一步主线已转为证明这三个 odd-prime cofactor 与 `(z_E,chi_E)` 中心核不相容。当前尚未得到该 reciprocity/resultant 矛盾，因此仍不能写成 `A_2` 全局空性。
mixed bridge 还重新恢复 `gcd(c_uH,g)=1`，并把
`sgn(chi_E)=sgn(epsilon z_E)` 及相对误差 `<3/50000`
严格锁定。前一 coprimality 与旧 source split 一致，不重复收费；新的
用途是消去象限分支，并把 cofactor 与 \(g\) 的共同素因子精确隔离到
`A_3=3T+a_3` 的平方/饱和通道。
在非饱和奇素数 \(p\mid g\) 上，所有中心变量还可完全消去为
\[
\left(\frac{\Xi_C}{p}\right)
=\left(\frac{-\varepsilon a_25^{M+d}}p\right).
\]
尚缺的是从 `2^m5^d` 一侧或三 cofactor 的共同 cubic quotient
固定相反字符。
进一步审计模 `g^2` 的提升后，二阶修正
`1-3DC^{-1}` 在每个 prime-power 分量上自动是平方；因此仅靠
quadratic-character 加深不会闭环，必须使用三 cubic cofactor 的加性
resultant、符号/高度，或饱和 prime-power 的精确大小。
三点 secant cubic 现已给出第一组非 character 约束。若
\[
\Delta_-=\frac{\Xi_C-\Xi_-}{2^m5^d},
\qquad
\Delta_+=\frac{\Xi_+-\Xi_C}{2^m5^d},
\]
则
\[
1<\Delta_-/\Delta_+<2,\qquad
v_2(\Delta_-)=v_2(\Delta_+)=1,
\]
且 \(\Delta_--\Delta_+\) 有 (16.245) 的精确正公式，并满足
\[
v_2(\Delta_--\Delta_+)=m+1,\qquad
v_5(\Delta_--\Delta_+)=d.
\]
下一缺口是把这条固定加法与 \(D\pm C\) 的奇除数结构联立。
该联立现已完成到 additive CRT：\(\Delta_+\) 落入模
\(D^2-C^2\) 的唯一显式余类，\(\Delta_-=\Delta_++\Gamma_\Delta\)。
尚缺对 CRT 商
\(Q_\Delta=\lfloor\Delta_+/(D^2-C^2)\rfloor\) 的无界高度控制。
把中心二阶差分先除去 \(2^{m+1}5^d\) 得到
\(\widetilde{\mathcal T}_2\) 后，显式式进一步证明
\(v_5(\widetilde{\mathcal T}_2)=d\)。因此真正的 \(2,5\)-本原正整数是
\[
\widehat{\mathcal T}_2
=\frac{\mathcal T_2}{2^{m+1}5^{2d}},
\]
并满足
\[
\widehat{\mathcal T}_2\equiv-5^{\lambda-d}(c_uC)^2\pmod g,
\qquad
\gcd(\widehat{\mathcal T}_2,10c_ug)=1,
\qquad
\widehat{\mathcal T}_2\equiv3\pmod4.
\]
故它必含一个不整除 \(g\) 的 \(3\bmod4\) 惰性素数到奇次。完整代入
canonical square 后，这恰好恢复旧 odd inert excess，而非第二个独立
obstruction；必须继续排除其 denominator-prefix、source、spontaneous
三类来源。
完全约去十进制 content 后，显式式实际为
\[
\widehat{\mathcal T}_2
=2^mc_u^2g^2\mathscr S_0
-(c_Qq)^2 5^{2\lambda-d}XY.
\]
它只是“尺度项减 norm”；缺少精确交叉项，不能直接升级为 norm。
新的精确接触律为
\[
\gcd(\widehat{\mathcal T}_2,Q_0XY)
=\gcd(\mathscr S_0,Q_0XY),
\qquad
\gcd(\widehat{\mathcal T}_2,f)
=\gcd(\mathscr R_f,f).
\]
因此 core 的 \(qf\) denominator excess 已降成
\((q,\mathscr S_0)\)、\((f,\mathscr R_f)\) 两个显式接触问题；
非 \(3\) inert prime 不能来自 \(XY,c_u,g\)。固定素数 \(3\) 也已由
\(a_2a_3\bmod3\) 与 \(3\mid Q_0\) 精确分类到 (16.310)，但允许的
两类 residue 中尚未控制其赋值奇偶。
此外 \(\mathscr S_0\) 关于 \(K\) 的判别式为
\[
8\mathscr R_{23},\qquad
\mathscr R_{23}
=2(a_3+2T)^2+(a_3+2T)T+3T^2,
\]
其中二元型判别数为 \(-23\)。所以 \(q\)-channel 的非重根
denominator inert prime 必满足
\((\mathscr R_{23}/p)=(2/p)\)，重根则除 \(p=23\) 外强迫
\((p/23)=1\)。\(f\)-channel 也有 (16.320) 的独立 curvature
character。完整配方 (16.323) 又证明这些 character 都是同一个全局
principal-square identity 的投影，不能自行闭环；尚缺从 source 或
prefix defect 独立固定相反的分裂类型。
其 companion 进一步精确分解为
\[
\mathscr C_{23}
=U_{23}^2+23V_{23}^2+5^{3\lambda}Q_0^2XY,
\]
并满足 \(\mathscr C_{23}\equiv U_{23}^2\pmod{5^{2m}}\)、
\(\mathscr C_{23}\equiv1\pmod8\)。所以纯 \(2,5\)-进非平方路线也已
降级，剩余输入必须来自 odd-prime orientation 或 Archimedean gap。
把 companion 与 canonical \(Z\) 联立后又得到正 shifted pair
\[
\mathscr V_-=5^\lambda fc_-^2X-\mathscr E_{23},
\qquad
\mathscr V_+=5^\lambda qc_+^2Y-\mathscr E_{23}.
\]
其同侧 denominator 接触由
\(\mathscr L_{23}=9T/2+a_3\) 完全控制，公共因子则等价于
\(\gcd(TK-9T-2a_3,Z)\)。消去 \(Z\) 后，所有 \(qf\) 未饱和接触
严格为偶赋值；odd denominator excess 只能来自完整 prime power
\(p^e\Vert qf,\ p^e\mid\mathscr L_{23}\)。
模 \(4\) 还给出 \(q\equiv3,f\equiv1\) 的全局 orientation：
\(Z\equiv1\) 对应 \(X,Y,k_h\) 的固定 \(3\) balanced transfer，
\(Z\equiv3\) 对应 denominator \(q\) carrier。前一 orientation 中
shifted pair 恰共享一份 \(3\)，且 \(3\nmid\widehat{\mathcal T}_2\)。
完整 saturation 又等价于
\[
p^e\Vert q,\ p^e\mid\mathscr G_q
\quad\text{或}\quad
p^e\Vert f,\ p^e\mid\mathscr G_f,
\]
其中
\[
\mathscr G_q=5^{M-1}(a_3-90T)+a_3H,\qquad
\mathscr G_f=\mathscr G_q-18\cdot2^{m+1}c5^d.
\]
两 target 已接回真实小缺口 \(H\)，但其高度约为
\(89\cdot5^{M-1}T\)；剩余需要无界 prime-power resultant，而不是
小余数或有限枚举。
在 generic \(q\)-saturation 中，rational-root 四次式还把深度放大为
\[
p^e\mid(6D+C),\quad
p^{2e}\mid\bigl(D(3T+2a_3)-TC\bigr),
\]
或 \(p^e\mid((K-3)D+C)\)。进一步按
\(n_p=v_p(c_Qq)=v_p(c_Q)+e\) 精确计价后，middle branch 实为
\[
v_p(gs_p-5^\lambda r_p)=e+2v_p(c_Q),
\]
third branch 则吸收完整 \(n_p\) 深度。若该素数确实接触
\(q\)-侧 additive cofactor，精确 resultant
\[
\mathscr S_0=T(K^2-26)-(2K-9)(2a_3+9T)
\]
强迫 \(K^2\equiv26\pmod p\)：第一 valuation branch 因而完全消失，
原无界 exceptional primes 缩成固定的 \(11,23\)。`prime-source.md`
进一步证明这两个 fixed primes 均不再构成独立开放 Hensel 核：special
`11` 必有 \(11\mid c_+\)、\(11\nmid W_q\)，其 middle depth 恰为
\(2v_{11}(c_Q)\)；special `23` 必有 \(23\nmid c_Q\)，并满足
\(v_{23}(W_q)=v_{23}(H_0)\)，所以完全并入已有 height channel。
`primitive-reduction.md` 进一步证明
\[
H_0=c_uW_q,
\qquad
W_q=\gcd(\alpha,H_0),
\qquad
\gcd(\alpha,\beta)=\omega,
\]
从而 `W_q` 正是原拼接分数最低项的 reduced numerator。它还证明
\[
p\mid W_q,\quad p\mid\mathscr L_{23}
\Longrightarrow
2K-9\equiv0\pmod p.
\]
因此 q-carrier 与 height channel 的交集只可能是 `p=23`；对所有
`p\ne11,23` 的 generic q-carrier，原来的 `c_Q` overlap 也被完全排除：
\[
v_p(W_q)=v_p(c_Q)=0.
\]
在 \(p\nmid c_Q\) 的 generic 层，\(f\)-侧则取互补局部类型：
\[
K^2-26\equiv
\left(\frac{2c_Q}{2^m5^\lambda g}\right)^2N_0\pmod p\ne0.
\]
若 f-carrier 同时进入 height channel，则 `primitive-reduction.md` 进一步强迫
\[
\left(\frac p{23}\right)=-1,
\qquad
\left(\frac p5\right)\left(\frac p{11}\right)=1,
\qquad
2K\equiv9\pmod p,
\]
且 `p\notin\{3,5,11,23\}`。继续保留完整剩余类而不只取 quadratic character 后，§10 更强地得到
\[
p\in\{7,43\}.
\]
若写 \(e=v_p(f)\)、\(h=v_p(W_q)\)、\(\tau=v_p(\widehat{\mathcal T}_2)\)，并假设完整 saturation \(p^e\mid\mathscr L_{23}\)，则还有
\[
\boxed{\min\{\tau,e,h\}=1.}
\]
因此 f-denominator、height/reduced-numerator 与 odd-excess 三条深接触不能同时进入二阶。`7,43` 两个固定点本身仍与旧 reciprocity signature 兼容，尚需分别做 Hensel/digit-phase 审计，所以这里仍不是 A2 空性。
\(q\)-侧根还通过
\(J_{101}^2\equiv101N_0-26\pmod p\) 接回真实 prefix Gaussian
vector；这些条件尚未形成最终矛盾。
进一步把 carrier 放回 canonical factor allocation 后，无条件得到
\(N\equiv DK\pmod p\)：所以 generic middle branch 实际不存在，
所有 \(p\ne11,23\) 的 \(q\)-carrier 都走唯一 third branch，并满足
\[
v_p(KD-N)=v_p(c_Qq).
\]
此前保留的 `11` middle/third 与 `23` right-factor 两条 fixed budgets
现已由 `prime-source.md` 吸收到既有 square-allocation / height 两条通道，
不再单列为新的无界例外。
更强地，canonical 两因子等式在整数层直接给出
\[
q\mid DK-N,\qquad
2c_u\frac{DK-N}{q}=c_+^2Y+5^\lambda c_-^2X.
\]
因此两个 denominator channels 的完整饱和深度已统一降为纯
prefix gcd
\[
\gcd(q,K^2-26),\qquad
\gcd(f,\Psi_f),\quad
\Psi_f=b_2^2(K^2-26)-Q^2N_0>0.
\]
`primitive-reduction.md` 还审计出：对于任意非 `3` inert prime
\(r\mid W_q\)，此前记录的
\[
\left(\frac{N_0}{r}\right)=-1
\]
会由 canonical factor equality 自动推出，所以它不是第二条独立
height obstruction，后续不得重复收费。真正新增的 height 信息是
`W_q` 的 reduced-numerator 身份、saturation 交集律，以及去掉 balanced
`3` 后
\[
W_q/3^\delta\equiv1\pmod4,
\]
即 non-`3` inert odd carriers 的总体 parity 为偶。
对 special `23` height carrier，纯十进制化还强迫
\[
M\equiv0,1,2,8,9,10,12,13,15,17,19,20\pmod{22},
\]
从而删除其余十个长度同余类。
此外 CRT 商并非小商：严格有 \(Q_\Delta\ge5K\)。因此 additive CRT
路线若继续，必须控制新的无界大商结构。

## 可复核脚本

分支专用脚本位于 [`scripts/exact-lift/a2-only/`](../../../../../scripts/exact-lift/a2-only/)；它们验证恒等式和明确的有限/局部不等式，不是全局证明器。`check_a2_prime_source.py` 精确复核 special `23` 的 `M mod 22` residue 表；`check_a2_primitive_reduction.py` 复核新的固定系数与二次互反化简；`check_a2_f_height_fixed_primes.py` 核对 f-height 的 `301=7*43` 固定素数塌缩和共同二阶深度排除。

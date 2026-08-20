# A2-only Fixed23 And Cq Ledger

> 本文件是细粒度研究记录的机械归并账本。各来源的标题、正文和证明状态原样保留；账本中的局部闭合、有限证书或降级路线均不表示该分支或主不存在性命题已经关闭。

## 来源索引

- [`spontaneous-cq-canonical-defect-overlap.md`](#source-spontaneous-cq-canonical-defect-overlap)
- [`spontaneous-cq-canonical-natural-representative-nogo.md`](#source-spontaneous-cq-canonical-natural-representative-nogo)
- [`spontaneous-cq-fixed23-eta2-c1-source-bridge.md`](#source-spontaneous-cq-fixed23-eta2-c1-source-bridge)
- [`spontaneous-cq-fixed23-eta2-c2-a3-crt-representative.md`](#source-spontaneous-cq-fixed23-eta2-c2-a3-crt-representative)
- [`spontaneous-cq-fixed23-eta2-c2-blowup-nogo.md`](#source-spontaneous-cq-fixed23-eta2-c2-blowup-nogo)
- [`spontaneous-cq-fixed23-eta2-c2-centered-a3-map.md`](#source-spontaneous-cq-fixed23-eta2-c2-centered-a3-map)
- [`spontaneous-cq-fixed23-eta2-c2-centered-canonical-root.md`](#source-spontaneous-cq-fixed23-eta2-c2-centered-canonical-root)
- [`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md`](#source-spontaneous-cq-fixed23-eta2-c2-centered-source-slot)
- [`spontaneous-cq-fixed23-eta2-c2-decimal-gaussian-kernel.md`](#source-spontaneous-cq-fixed23-eta2-c2-decimal-gaussian-kernel)
- [`spontaneous-cq-fixed23-eta2-c2-fixed-modulus-nogo.md`](#source-spontaneous-cq-fixed23-eta2-c2-fixed-modulus-nogo)
- [`spontaneous-cq-fixed23-eta2-c2-full-a3-crt.md`](#source-spontaneous-cq-fixed23-eta2-c2-full-a3-crt)
- [`spontaneous-cq-fixed23-eta2-c2-gaussian-unit.md`](#source-spontaneous-cq-fixed23-eta2-c2-gaussian-unit)
- [`spontaneous-cq-fixed23-eta2-c2-lambda52-divisor-exclusion.md`](#source-spontaneous-cq-fixed23-eta2-c2-lambda52-divisor-exclusion)
- [`spontaneous-cq-fixed23-eta2-c2-lambda74-divisor-exclusion.md`](#source-spontaneous-cq-fixed23-eta2-c2-lambda74-divisor-exclusion)
- [`spontaneous-cq-fixed23-eta2-c2-reconstruction-certificate.md`](#source-spontaneous-cq-fixed23-eta2-c2-reconstruction-certificate)
- [`spontaneous-cq-fixed23-eta2-c2-source-content-depth-ladder.md`](#source-spontaneous-cq-fixed23-eta2-c2-source-content-depth-ladder)
- [`spontaneous-cq-fixed23-eta2-c2-source-content-mod23.md`](#source-spontaneous-cq-fixed23-eta2-c2-source-content-mod23)
- [`spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`](#source-spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate)
- [`spontaneous-cq-fixed23-eta2-c2-source-window.md`](#source-spontaneous-cq-fixed23-eta2-c2-source-window)
- [`spontaneous-cq-fixed23-eta2-c2-theta-p3-filter.md`](#source-spontaneous-cq-fixed23-eta2-c2-theta-p3-filter)
- [`spontaneous-cq-fixed23-eta2-c2-three-primary-exclusion.md`](#source-spontaneous-cq-fixed23-eta2-c2-three-primary-exclusion)
- [`spontaneous-cq-fixed23-eta2-slots.md`](#source-spontaneous-cq-fixed23-eta2-slots)
- [`spontaneous-cq-global-coupling.md`](#source-spontaneous-cq-global-coupling)
- [`spontaneous-cq-relative-depth-nogo.md`](#source-spontaneous-cq-relative-depth-nogo)
- [`spontaneous-cq-source-tail-nogo.md`](#source-spontaneous-cq-source-tail-nogo)

<a id="source-spontaneous-cq-canonical-defect-overlap"></a>

> 整合来源：`spontaneous-cq-canonical-defect-overlap.md`

# A2 pure-`c_Q` canonical defect orientation 与 fixed `23` overlap

> **依赖：** `spontaneous-cq-global-coupling.md`、`spontaneous-cq-relative-depth-nogo.md`、`spontaneous-cq-source-tail-nogo.md`、`phase-and-defect.md`、`primitive-reduction.md`。
>
> **严格状态：**本文把 pure-`c_Q` 的 canonical square allocation 直接写入 finite-defect 坐标 `J_def=j-C/D`，得到两种 orientation 在 `C` 上互异的 `p^{2c}` residue。随后专门处理 fixed `23`：两个 additive orientation gate 在第一层同时退化，但它们同时提升到 `23^2` 的唯一 correction 是 `kappa=4`，且此时 source ratio `rho=z/c_u=-1 mod 23`，等价于 `23|omega`。因此 simultaneous additive lift 的来源是原拼接 gcd `omega` 的 content；canonical `c_- / c_+` orientation 仍由 finite-defect residue 区分。对 `v_23(c_Q)>=2`，该 overlap 只发生在 `M=49,302 mod 506` 的两条 length classes。本文尚未证明这些 classes 全部不可能，因此不关闭 A2。

---

## 1. finite-defect 坐标精确恢复 canonical factors

固定 reflection，沿用

\[
T:=10^m,
\qquad
5^\lambda D=gT,
\]

以及 finite-defect

\[
J:=J_{\rm def}=\frac{c_-^2X}{D}
=k+\frac RD
=j-\frac CD,
\qquad j:=k+1,
\qquad C:=D-R.
\tag{1.1}
\]

canonical height factorization 为

\[
H_0-Y_3=5^\lambda c_-^2X,
\qquad
H_0+Y_3=c_+^2Y,
\qquad
Y_3=ga_3.
\tag{1.2}
\]

由 (1.1) 与 `5^lambda D=gT`：

\[
\boxed{H_0-Y_3=gTJ.}
\tag{1.3-}
\]

所以

\[
H_0=g(a_3+TJ),
\]
进而

\[
\boxed{H_0+Y_3=g(TJ+2a_3).}
\tag{1.3+}
\]

这给出 canonical factor 与 finite-defect 的无损坐标转换。

---

## 2. pure-`c_Q` orientation 直接固定 `C` 的 square-depth residue

固定 genuine non-`3` inert prime

\[
p^c\Vert c_Q,
\qquad p\nmid q,
\qquad c\ge1.
\tag{2.1}
\]

已有 primitive separation

\[
p\nmid gTDXYa_3.
\tag{2.2}
\]

若 `p^c||c_-`，canonical allocation 给

\[
v_p(H_0-Y_3)=2c,
\]
结合 (1.3-) 得

\[
\boxed{v_p(J)=2c.}
\tag{2.3-}
\]

若 `p^c||c_+`，则

\[
v_p(H_0+Y_3)=2c,
\]
结合 (1.3+) 得

\[
\boxed{v_p(TJ+2a_3)=2c.}
\tag{2.3+}
\]

把 `J=j-C/D` 代回。由于 `p∤DT`，得到两个精确 residue：

### minus orientation

\[
\boxed{
C\equiv jD\pmod{p^{2c}}.
}
\tag{2.4-}
\]

### plus orientation

\[
\boxed{
C\equiv
D\left(j+2a_3T^{-1}\right)
\pmod{p^{2c}}.
}
\tag{2.4+}
\]

其中 `T^{-1}` 按模 `p^{2c}` 读取。

特别地模 `p` 时，两类永不重合，因为

\[
2a_3T^{-1}D\not\equiv0\pmod p.
\]

因此

\[
\boxed{
\text{finite-defect natural representative }C
\text{ 保留完整的 }c_- / c_+\text{ orientation label}.}
\tag{2.5}
\]

这条 label 可以与 `endpoint-lattice.md` 的自然代表公式直接联立。

---

## 3. `R_±` 的额外深度恰好来自 `omega`

`spontaneous-cq-global-coupling.md` 定义

\[
R_-:=Tc_uK-za_3,
\qquad
R_+:=Tc_uK+fa_3,
\]
且

\[
R_-=\omega(H_0-Y_3),
\qquad
R_+=\omega(H_0+Y_3).
\tag{3.1}
\]

利用 (1.3±) 与

\[
g\omega=z+c_u,
\]
还可写成

\[
\boxed{R_-=(z+c_u)TJ,}
\tag{3.2-}
\]

\[
\boxed{R_+=(z+c_u)(TJ+2a_3).}
\tag{3.2+}
\]

令

\[
w_\omega:=v_p(\omega).
\]

由于 `p∤g`，有 `v_p(z+c_u)=w_omega`。于是 canonical chosen branch 的精确深度是

\[
\boxed{v_p(R_{\rm chosen})=2c+w_\omega,}
\tag{3.3}
\]

而 unchosen height factor 是 unit，所以

\[
\boxed{v_p(R_{\rm unchosen})=w_\omega.}
\tag{3.4}
\]

因此若两个 `R` 同时出现额外 `p`-content，其来源只能是 `omega`；这不表示 `p` 同时进入 `c_-` 与 `c_+`。

---

# II. fixed `23` 的 orientation overlap

## 4. 两个 additive gate 的 sum/difference

写

\[
A_K:=K^2-18K+55,
\]

\[
F_W(K):=5K^2-36K+55.
\]

两个 integer gate 满足精确恒等式

\[
\boxed{
\mathcal G_++\mathcal G_-
=2g\omega A_K,}
\tag{4.1}
\]

\[
\boxed{
\mathcal G_+-\mathcal G_-
=2c_uF_W(K).}
\tag{4.2}
\]

fixed `23` 第一层有

\[
K=16+23\kappa.
\]

直接展开：

\[
\boxed{
\frac{A_K}{23}
\equiv1+14\kappa\pmod{23},}
\tag{4.3}
\]

\[
\boxed{
\frac{F_W(K)}{23}
\equiv10+9\kappa\pmod{23}.}
\tag{4.4}
\]

第一层 `K=16 mod23` 时 `A_K` 与 `F_W` 都被 `23` 整除，所以两个 orientation gate 都自动至少含一个 `23`。这就是 fixed `23` 的共同 degeneracy。

---

## 5. 两个 gate 同时提升到 `23^2` 的唯一 class

设

\[
23^2\mid\mathcal G_+,
\qquad
23^2\mid\mathcal G_-.
\tag{5.1}
\]

由差式 (4.2) 和 `23∤c_u`：

\[
10+9\kappa=0\pmod{23}.
\]

唯一得到

\[
\boxed{\kappa=4.}
\tag{5.2}
\]

此时

\[
1+14\kappa=11\ne0\pmod{23}.
\]

再由和式 (4.1)、`23∤g`：

\[
23\mid\omega.
\tag{5.3}
\]

反过来，若 `kappa=4` 且 `23|omega`，则 (4.1)–(4.4) 同时给

\[
23^2\mid\mathcal G_+,
\qquad
23^2\mid\mathcal G_-.
\]

所以有严格等价：

\[
\boxed{
23^2\mid\mathcal G_+,\mathcal G_-
\Longleftrightarrow
\kappa=4\text{ and }23\mid\omega.
}
\tag{5.4}
\]

用 source ratio

\[
\rho:=\frac z{c_u}
\]
表示，`gomega=z+c_u` 给

\[
23\mid\omega
\Longleftrightarrow
\boxed{\rho\equiv-1\pmod{23}}.
\tag{5.5}
\]

因此 fixed `23` 的 simultaneous orientation lift 精确等价于

\[
\boxed{(\kappa,\rho)=(4,-1).}
\tag{5.6}
\]

这与 `spontaneous-cq-relative-depth-nogo.md` 的两个 Möbius chart 一致：在 `kappa=4` 时，plus/minus 两图都给 `rho=-1`。

---

## 6. simultaneous gate lift 仍保留 canonical orientation

令

\[
\zeta:=\frac{a_3}{T}\in\mathbf Z_{23}^\times.
\]

由 (3.2-) 除以 `Tc_u`，得到精确关系

\[
\boxed{
K-\rho\zeta=(\rho+1)J.}
\tag{6.1}
\]

在 simultaneous class `(kappa,rho)=(4,-1)` 的第一层，(6.1) 给

\[
K+\zeta=0\pmod{23}.
\]

因为 `K=16 mod23`：

\[
\boxed{\zeta=7\pmod{23}.}
\tag{6.2}
\]

现在使用 §2 的 finite-defect orientation marker：

### minus orientation

\[
\boxed{C/D\equiv j\pmod{23}.}
\tag{6.3-}
\]

### plus orientation

\[
\boxed{C/D\equiv j+14\pmod{23}.}
\tag{6.3+}
\]

两类仍严格不同。因此 (5.4) 的 simultaneous additive lift 没有把 canonical square allocation 合并；`C` 的 residue 继续记录唯一 orientation。

特别地，对最危险的 `(a,k)=(9,2)` endpoint，`j=3`，于是

\[
\boxed{
\begin{array}{c|c}
23\mid c_-&C/D\equiv3\pmod{23},\\
23\mid c_+&C/D\equiv17\pmod{23}.
\end{array}}
\tag{6.4}
\]

这可以直接与 `endpoint-lattice.md` §16.15 的 `C` 自然代表联立。

---

## 7. `v_23(c_Q)>=2` 时的 length classes

若

\[
c:=v_{23}(c_Q)\ge2,
\]
则

\[
q_1:=Q/23\equiv0\pmod{23}.
\]

fixed `23` prefix second-layer equation退化为

\[
9\kappa\equiv16h_N+22\pmod{23}.
\tag{7.1}
\]

simultaneous class `kappa=4` 因而要求

\[
h_N=21\pmod{23}.
\tag{7.2}
\]

沿用 length lift

\[
M=M_0+22r,
\]

\[
M_0=5:\quad h_N=15+3r,
\]

\[
M_0=16:\quad h_N=5+3r.
\]

(7.2) 分别给

\[
r=2\quad\text{or}\quad r=13.
\]

所以

\[
\boxed{
\kappa=4
\Longleftrightarrow
M\equiv49\text{ or }302\pmod{506}
}
\tag{7.3}
\]

在 `c>=2` 且 prefix 已提升到第二层的前提下。

结合 §5：

\[
\boxed{
\begin{aligned}
&M\equiv49,302\pmod{506},\quad23\nmid\omega
\\&\qquad\Longrightarrow\text{ additive common depth 停在第一层},\\[1mm]
&M\equiv49,302\pmod{506},\quad23\mid\omega
\\&\qquad\Longrightarrow\mathcal G_+,\mathcal G_-\text{ 同时提升到 }23^2.
\end{aligned}}
\tag{7.4}
\]

因此这两条 length class 把 second-layer survival 直接转化成原拼接 gcd content `23|omega`。

与前一文件的强制 odd classes 合并，`c>=2` 的六条特殊 `mod 506` class 为

\[
\boxed{
\begin{array}{c|c|c}
M\bmod506&\kappa&\text{second-layer meaning}\\ \hline
49&4&\omega\text{-content overlap}\\
170&18&\text{chosen gate cannot lift}\\
236&11&\text{chosen gate incompatible with source unit}\\
302&4&\omega\text{-content overlap}\\
423&18&\text{chosen gate cannot lift}\\
489&11&\text{chosen gate incompatible with source unit}
\end{array}}
\tag{7.5}
\]

这里后四类的准确含义是 common depth 恰停在第一层；它们不表示整个 arithmetic state 被排除。

---

## 8. rational-root route 的局部审计

`endpoint-lattice.md` 的 finite-defect quartic 为

\[
F(J)=
 b_2^2T J(TJ+2a_3)(K-J)^2
-Q^2N_0(TJ+a_3)^2.
\tag{8.1}
\]

canonical product 与 reflection scale 给

\[
g^2T J(TJ+2a_3)=5^\lambda c_Q^2XY,
\]

\[
N_0=5^{\lambda-2d}XY,
\]

\[
b_2=2^{M+m+1}c_ug,
\qquad
Q=2^{M+1}c_Qq.
\]

在真实 solution `J` 上代入 (8.1)，消去公共正因子后得到

\[
\left(2^m5^dc_u(K-J)\right)^2
=
\left(q(TJ+a_3)\right)^2.
\tag{8.2}
\]

两边括号均为正，因此取正平方根并乘 `5^lambda`：

\[
\boxed{
Tc_u(K-J)=z(TJ+a_3).}
\tag{8.3}
\]

即

\[
\boxed{
Tc_uK-za_3=(z+c_u)TJ,}
\tag{8.4}
\]

这正是 (3.2-)。

因此 quartic `F(J)=0` 在 canonical product 已加入后，其**局部 root equation**不会给 fixed `23` 再产生第三条独立 branch；它恢复同一个 source/canonical linear relation。这里不把 rational-root consequence `C|F(j)` 一并降级：`F(j)` 在整数中心 `j` 的自然代表 divisibility 仍可能含有额外 global arithmetic，后续仍值得与 (2.4±) 和 `C` 的自然代表联合使用。

---

## 9. 更新后的 frontier

本轮得到三条可继续使用的接口：

\[
\boxed{
C\equiv jD\pmod{p^{2c}}
\quad\text{or}\quad
C\equiv D(j+2a_3T^{-1})\pmod{p^{2c}},
}
\]
由 canonical allocation 唯一选择；

\[
\boxed{
(\kappa,\rho)=(4,-1)
\Longleftrightarrow
23^2\mid\mathcal G_+,\mathcal G_-
\Longleftrightarrow
23\mid\omega,
}
\]
在 second-layer common root 上成立；

以及 `c>=2` 时

\[
\boxed{M\equiv49,302\pmod{506}}
\]
是唯一的 `omega`-content overlap length pair。

下一步应把 `C` 的 orientation residue (2.4±)/(6.4) 与 `endpoint-lattice.md` §16.15 的唯一自然代表 (16.101)–(16.104) 以及 `C|F(j)` 联立。这样会真正比较两个独立整数坐标，而不会回到已经审计完的 source quotient 或 local Hensel derivative。

---

<a id="source-spontaneous-cq-canonical-natural-representative-nogo"></a>

> 整合来源：`spontaneous-cq-canonical-natural-representative-nogo.md`

# A2 pure-`c_Q` canonical residue 与 `C` natural representative 的局部 no-go

> **依赖：** `spontaneous-cq-canonical-defect-overlap.md`、`endpoint-lattice.md` §16.15。
>
> **严格状态：**前一文件得到 canonical `c_- / c_+` allocation 在 finite-defect 顶部余量 `C` 上的精确 `p^{2c}` residue。本文检查最直接的下一步：把该 residue 代入 `(a,k)=(9,2)` reflection high-2 endpoint 的自然代表公式 (16.101)，是否会产生一个新的 pure-`c_Q` 局部 obstruction。结论是否定的：模 `p^{2c}` 后，(16.101) 精确退化为已有 high-2 equality 与 `H_0=±Y_3` canonical congruence。fixed `23` 的 simultaneous class 中，它进一步退化为 §16.37 已有的 directed square-root lock。新的信息只能来自与 `g/2^m` 等互素方向以及 `0<C<<L_0` 小代表区间的真正 CRT 比较。

---

## 1. endpoint natural representative

固定 `endpoint-lattice.md` 的危险 reflection high-2 core

\[
a=9,
\qquad k=2,
\qquad j=3,
\qquad T=10^m.
\]

§16.15 给出

\[
\boxed{
5^\lambda C
=gA_3+\varepsilon a_2c_Q5^d-\frac{g^2k_h}{2},
}
\tag{1.1}
\]

其中

\[
A_3=a_3+3T,
\qquad
\varepsilon\in\{-1,+1\},
\]

且 high-2 equality 为

\[
\boxed{
H_0+\varepsilon Y_2=\frac{g^2k_h}{2},
\qquad
Y_2=a_2c_Q5^d.
}
\tag{1.2}

另一方面 finite-defect/canonical 坐标满足

\[
5^\lambda D=gT,
\qquad
J=3-\frac CD,
\]

\[
H_0-Y_3=gTJ,
\qquad
H_0+Y_3=g(TJ+2a_3),
\qquad
Y_3=ga_3.
\tag{1.3}

---

## 2. minus orientation 代回 natural representative

固定 pure-`c_Q` prime

\[
p^c\Vert c_Q,
\qquad p\nmid q,
\qquad c\ge1,
\]
并假设

\[
p^c\Vert c_-.
\]

canonical factor 给

\[
p^{2c}\mid H_0-Y_3,
\]
所以前一文件得到

\[
\boxed{C\equiv3D\pmod{p^{2c}}.}
\tag{2.1}

用 `5^lambda D=gT`：

\[
5^\lambda C\equiv3gT\pmod{p^{2c}}.
\tag{2.2}

把 (2.2) 代入 (1.1)：

\[
3gT
\equiv
g(a_3+3T)+\varepsilon a_2c_Q5^d-rac{g^2k_h}{2}
\pmod{p^{2c}}.
\]

消去 `3gT`：

\[
\boxed{
\frac{g^2k_h}{2}
\equiv
ga_3+\varepsilon a_2c_Q5^d
\pmod{p^{2c}}.}
\tag{2.3}

但 minus canonical congruence本身就是

\[
H_0\equiv Y_3=ga_3\pmod{p^{2c}}.
\]

代入 high-2 equality (1.2) 后立刻得到 (2.3)。因此 minus side 没有新增局部条件。

---

## 3. plus orientation 同样退化

现在假设

\[
p^c\Vert c_+.
\]

前一文件给

\[
\boxed{
C\equiv
D\left(3+2a_3T^{-1}\right)
\pmod{p^{2c}}.}
\tag{3.1}

乘 `5^lambda`：

\[
5^\lambda C
\equiv
g(3T+2a_3)
\pmod{p^{2c}}.
\tag{3.2}

代入 (1.1)：

\[
g(3T+2a_3)
\equiv
g(a_3+3T)+\varepsilon a_2c_Q5^d-rac{g^2k_h}{2}.
\]

整理：

\[
\boxed{
\frac{g^2k_h}{2}
\equiv
-ga_3+\varepsilon a_2c_Q5^d
\pmod{p^{2c}}.}
\tag{3.3}

plus canonical congruence是

\[
H_0\equiv-Y_3=-ga_3\pmod{p^{2c}}.
\]

与 (1.2) 联立恰好就是 (3.3)。因此 plus side 也没有新的 pure-`c_Q` 局部 obstruction。

---

## 4. fixed `23` simultaneous class 只恢复 directed root lock

对 fixed `23` 的 simultaneous gate class，前一文件证明

\[
\kappa=4,
\qquad
\rho:=z/c_u=-1,
\qquad
\zeta:=a_3/T=7\pmod{23}.
\tag{4.1}

令

\[
X_h:=\frac{k_hg}{2}.
\]

因为 `23|c_Q`，(2.3)/(3.3) 模 `23` 时 `Y_2` 项消失，因此

### `23|c_-`

\[
\boxed{X_h\equiv a_3\equiv7T\pmod{23}.}
\tag{4.2-}

### `23|c_+`

\[
\boxed{X_h\equiv-a_3\equiv16T\pmod{23}.}
\tag{4.2+}

这正是 `endpoint-lattice.md` §16.37

\[
X_h\equiv a_3\pmod{5^dc_-},
\qquad
X_h\equiv-a_3\pmod{c_+}
\]
在 prime `23` 上的投影。

所以 fixed `23` 上把 `C` natural representative 再局部化，并不会得到第三个 orientation equation。

---

## 5. 审计结论

canonical residue 与 (16.101) 的关系可以准确记为

\[
\boxed{
\text{canonical }C\bmod p^{2c}
+
\text{natural representative (16.101) mod }p^{2c}
}
\]

\[
\boxed{
\Longleftrightarrow
H_0\equiv\pm Y_3\pmod{p^{2c}}
+
\text{high-2 equality mod }p^{2c}.
}
\tag{5.1}

因此以下路线应停止重复：

1. 单独把 (16.101) 再模 `23`, `23^2`, ...；
2. 把 resulting `X_h=±a_3` 当作新的 fixed-`23` obstruction；
3. 在同一个 pure-`c_Q` prime 上重复收取 canonical height 与 natural-representative 的局部 congruence。

真正仍然开放的对象是跨互素模数的自然代表问题。`endpoint-lattice.md` 还有

\[
c_uC\equiv-\varepsilon a_2 5^{M+d}\pmod g,
\]

\[
C\theta\equiv5^Ma_3\pmod{2^m},
\]
以及

\[
0<C<\frac{\mathfrak L_0}{1000},
\qquad
\mathfrak L_0=2c_u^2g^2.
\]

而本文/前一文件给出独立的

\[
C\equiv3D
\quad\text{or}\quad
C\equiv D(3+2a_3T^{-1})
\pmod{23^{2c}}.
\]

因为 `23∤2c_ug`，这些方向互素。下一步只有把它们组成真正的 CRT natural representative，并利用 `C` 的极小 Archimedean interval，才可能产生新的 fixed-`23` global obstruction。

---

<a id="source-spontaneous-cq-fixed23-eta2-c1-source-bridge"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c1-source-bridge.md`

# A2 fixed `23` `eta=2`, `v_23(c_Q)=1` 的 high-2/source-ratio bridge

> **依赖：** `spontaneous-cq-fixed23-eta2-slots.md`、`spontaneous-cq-relative-depth-nogo.md`、`spontaneous-cq-canonical-defect-overlap.md`、`endpoint-lattice.md` §16.7。
>
> **严格状态：**`eta=2` 的 fixed-`23` high-2 lattice 已压成三型，其中两个 `d=2` 类型满足 `v_23(c_Q)=1`。本文利用 high-2 equality 与 canonical `c_- / c_+` allocation，把 source ratio `rho=z/c_u` 与 normalized denominator `q_1=Q/23` 直接联立。两个 surviving `c=1` 类型给出完全相同的 bridge。再与 fixed-`23` prefix 二阶式和 orientation gate 联立，得到显式 `(kappa,h_N)` 曲线，并识别四条 orientation-independent 的 `M mod 506` 强制 depth-1 class。这里的“强制 depth 1”指 pure-`c_Q` common depth 在 `23` 处恰为奇数 `1`，并不排除 arithmetic state。

---

## 1. 两个 `c=1` high-2 类型共享同一个 odd product

`spontaneous-cq-fixed23-eta2-slots.md` 的三型中，两个 `v_23(c_Q)=1` 类型为

\[
(d,c_Q,k_h,\varepsilon)
=(2,23,9,-),
\qquad
(2,207,1,-).
\tag{1.1}
\]

写

\[
c_Q=23\bar c.
\]

则两型分别有

\[
(\bar c,k_h)=(1,9),
\qquad
(9,1),
\]
所以统一满足

\[
\boxed{\bar c\,k_h=9.}
\tag{1.2}
\]

此外 `eta=2,d=2` 给

\[
M=2m-2,
\qquad
M\equiv16\pmod{22}.
\tag{1.3}
\]

因此

\[
N:=10^M\equiv4\pmod{23},
\qquad
B:=b_2\equiv-2N\equiv15\pmod{23}.
\tag{1.4}
\]

由 `2m=M+2` 与 (1.3)，

\[
m\equiv9\text{ or }20\pmod{22},
\]
故无论哪一类

\[
\boxed{T^2=10^{2m}\equiv9\pmod{23}.}
\tag{1.5}
\]

---

## 2. high-2 equality 直接恢复 `g mod 23`

令

\[
s=+1
\quad\Longleftrightarrow\quad23\mid c_-,
\]

\[
s=-1
\quad\Longleftrightarrow\quad23\mid c_+.
\tag{2.1}
\]

canonical factorization 给

\[
H_0\equiv sY_3=sga_3\pmod{23}.
\tag{2.2}
\]

high-2 equality 为

\[
H_0+\varepsilon Y_2=\frac{g^2k_h}{2},
\qquad
Y_2=a_2c_Q5^d.
\tag{2.3}
\]

由于 `23|c_Q`，模 `23` 时 `Y_2=0`。又 `23∤gk_h`，所以 (2.2)–(2.3) 给

\[
\boxed{
g\equiv\frac{2sa_3}{k_h}\pmod{23}.}
\tag{2.4}
\]

注意这个 congruence 不依赖 high-2 side `varepsilon`；`s` 只记录 canonical `Y_3` orientation。

---

## 3. 消去 `g/c_u` 得到 normalized denominator bridge

定义

\[
\rho:=\frac{q5^\lambda}{c_u},
\qquad
q_1:=\frac Q{23}.
\tag{3.1}
\]

因为

\[
Q=2^{M+1}c_Qq
=23\cdot2^{M+1}\bar c\,q,
\]
所以

\[
\boxed{q_1=2^{M+1}\bar c\,q.}
\tag{3.2}
\]

而 reflection denominator 为

\[
B=2^{M+m+1}c_ug.
\tag{3.3}
\]

由 (3.1)–(3.3) 与 (2.4)：

\[
\begin{aligned}
\rho
&=q5^\lambda\frac1{c_u}
=q5^\lambda\frac{2^{M+m+1}g}{B}\\
&\equiv
s\frac{2q_1a_3T}{\bar c\,k_h\,B5^d}
\pmod{23}.
\end{aligned}
\tag{3.4}
\]

这里使用

\[
2^{m+1}5^\lambda=\frac{2T}{5^d}.
\]

对两个 surviving 类型，(1.2)、`d=2`、(1.4)–(1.5) 给

\[
\frac{2T^2}{\bar c k_h B5^d}
\equiv
\frac{18}{9\cdot15\cdot25}
\equiv20
\pmod{23}.
\]

写

\[
\zeta:=\frac{a_3}{T}.
\]
于是统一得到

\[
\boxed{
\rho\equiv20s\,q_1\zeta\pmod{23}.}
\tag{3.5}

这条式同时适用于 `(23,9)` 与 `(207,1)` 两型。

---

## 4. canonical orientation 把 `zeta` 消去

`spontaneous-cq-canonical-defect-overlap.md` 有 exact identity

\[
K-\rho\zeta=(\rho+1)J.
\tag{4.1}
\]

fixed `23` 第一层 `K=16 mod23`。

### minus orientation: `23|c_-`

此时

\[
J=0\pmod{23},
\]
所以

\[
\boxed{\zeta=\frac{16}{\rho}.}
\tag{4.2-}
\]

代入 (3.5)，且 `s=+1`：

\[
\boxed{
\rho^2=21q_1\pmod{23}.}
\tag{4.3-}
\]

### plus orientation: `23|c_+`

此时

\[
J+2\zeta=0\pmod{23},
\]
从 (4.1) 得

\[
\boxed{\zeta=-\frac{16}{\rho+2}.}
\tag{4.2+}
\]

代入 (3.5)，且 `s=-1`：

\[
\boxed{
\rho(\rho+2)=21q_1\pmod{23}.}
\tag{4.3+}
\]

由 primitive orientation separation，minus 中 `rho!=0`，plus 中 `rho(rho+2)!=0`，所以两式都自动保证

\[
q_1\ne0,
\]
与 `v_23(c_Q)=1` 一致。

---

## 5. 与 additive gate 和 prefix 二阶式联立

写

\[
K=16+23\kappa,
\qquad
N^2=16+23h_N.
\]

fixed-`23` prefix equation在 `N=4 mod23` 时为

\[
\boxed{
9\kappa=16h_N+22-16q_1.
}
\tag{5.1}

orientation gates为

\[
\boxed{
\rho(1+14\kappa)-9-18\kappa=0
}
\tag{5.2-}
\]

和

\[
\boxed{
\rho(1+14\kappa)+11=0.
}
\tag{5.2+}
\]

把 (4.3±)、(5.1)、(5.2±) 在 `F_23` 中消去 `rho,q_1`，得到：

### plus orientation

\[
\boxed{
11h_N\kappa^2-5h_N\kappa-h_N
+\kappa^3+5\kappa^2-9\kappa-2=0.
}
\tag{5.3+}
\]

### minus orientation

\[
\boxed{
11h_N\kappa^2-5h_N\kappa-h_N
+\kappa^3+4\kappa^2-3\kappa+7=0.
}
\tag{5.3-}
\]

两式的 `h_N` 系数相同：

\[
11\kappa^2-5\kappa-1.
\]

该系数在 `F_23` 中唯一零点是 `kappa=18`；代回常数项为 `20!=0`，所以这正好恢复 shared pole `kappa=18` 的不能提升。

`kappa=11` 需另外按 source unit boundary 删除：plus 给 `rho=-2`，minus 给 `rho=0`。

---

## 6. length image 与强制 depth-1 classes

当前 `M=16 mod22`，写

\[
M=16+22r,
\qquad0\le r<23.
\]

已有

\[
\boxed{h_N=5+3r\pmod{23}.}
\tag{6.1}

对所有

\[
\kappa\in\mathbf F_{23}\setminus\{11,18\}
\]
逐一使用 (5.3±)，得到 second-layer compatible length images：

### plus orientation compatible

\[
\boxed{
M\bmod506\in
\{38,104,126,192,214,258,280,302,324,390,412,434,456,478,500\}.
}
\tag{6.2+}

所以 plus orientation 的强制 depth-1 classes 为

\[
\boxed{
\{16,60,82,148,170,236,346,368\}\pmod{506}.}
\tag{6.3+}

### minus orientation compatible

\[
\boxed{
M\bmod506\in
\{16,82,104,126,214,236,258,302,324,368,434,456\}.
}
\tag{6.2-}

所以 minus orientation 的强制 depth-1 classes 为

\[
\boxed{
\{38,60,148,170,192,280,346,390,412,478,500\}\pmod{506}.}
\tag{6.3-}

两种 canonical orientation 的 forbidden length 交集是

\[
\boxed{
M\equiv60,148,170,346\pmod{506}.}
\tag{6.4}

因此，无论 `23` 被 allocated 到 `c_-` 还是 `c_+`，只要处于两个 `eta=2,d=2,c=1` high-2 类型之一，并且

\[
M\equiv60,148,170,346\pmod{506},
\]
那么 selected additive gate 都不能与 prefix 一起提升到 `23^2`。于是 pure-`c_Q` common depth 精确停在

\[
\boxed{d_{23}=1.}
\tag{6.5}

这四类是 orientation-independent 的强制 odd-depth classes，不是 arithmetic-state exclusion。

---

## 7. 结果的作用边界

本文首次把 `eta=2` high-2 equality 真正送入 fixed-`23` source ratio；(4.3±) 不属于此前 `theta/omega` source quotient 的代数闭包，因为它使用了独立的 Gaussian high-2 equality。

它仍没有消去全部 `c=1` 类型。对 (6.2±) 中的 compatible classes，局部二阶系统存在满足 high-2/source/prefix/additive 四层条件的 residue，因此继续只做 `mod23` 消元不会关闭它们。

下一步最自然的是：

1. 对第三型 `(d,c_Q,k_h)=(1,1587,1)`，其中 `v_23(c_Q)=2`，建立对应的 `q_2=Q/23^2` high-2 bridge并进入第三层 prefix；
2. 对两个 `c=1` 类型，把 (4.3±) 与 `C` 的 canonical `23^2` residue和 `g/2^m` CRT natural representative联立；
3. 在 global parity ledger 中记录 (6.4) 的四条 forced odd `23` classes，避免后续把“不能 lift”误记成候选被删。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-a3-crt-representative"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-a3-crt-representative.md`

# A2 fixed `23` `eta=2` `c=2` 的 third numerator 唯一 CRT 代表

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-decimal-gaussian-kernel.md`、`endpoint-lattice.md` §§8–9。
>
> **严格状态：**唯一 fixed-`23` `c=2` type 已被压成 pure third-block Gaussian kernel `Z_*=g-2a_3-9ib_3`，其长 Gaussian `5`-orientation具有精确深度 `lambda-1`。本文把该 `5`-adic residue 与 endpoint 原有的 `C theta` 二进 phase 联立。首先消去 finite-defect `C`，得到关于 `a_3` 的单变量 `2^m` congruence，其 derivative 恒为奇数，因此固定 source data 后存在唯一 `a_3 mod2^m`。再与 Gaussian orientation 给出的唯一 `a_3 mod5^{lambda-1}` 做 CRT，模数正好为 `T/25`；而真实 third-numerator digit window宽度只有该模数的 `1/10`。因此每个 Gaussian orientation 在完整第三分子窗口中至多留下一个整数代表。本文把连续 `a_3` 自由压成显式 natural-representative test，但尚未证明该代表总落在窗口外。

---

## 1. current type 与 two growing moduli

固定

\[
(d,c_Q,k_h,\varepsilon)
=(1,1587,1,+1),
\]

\[
M=2\lambda,
\qquad
m=\lambda+1,
\qquad
T:=10^m.
\tag{1.1}

已有 `lambda>=8`，并且

\[
M\equiv16\pmod{22}
\Longrightarrow
\lambda\equiv8\pmod{11}.
\tag{1.2}

finite-defect endpoint 使用

\[
J=3-\frac CD,
\qquad
5^\lambda D=gT,
\tag{1.3}

而 source Hensel quotient满足

\[
\boxed{
g\theta=5^{M+\lambda}+c_Qc_u
=5^{3\lambda}+c_Qc_u.}
\tag{1.4}

旧 endpoint 二进 phase 为

\[
\boxed{
C\theta\equiv5^Ma_3
=5^{2\lambda}a_3
\pmod{2^m}.}
\tag{1.5}

---

## 2. Gaussian near-norm 给 `C` 的 deep binary square phase

前一文件定义

\[
\mathcal Z_*:=g-2a_3-9ib_3
\]
并证明

\[
N(\mathcal Z_*)
=(g-2a_3)^2+81b_3^2
=12gT-4\cdot5^\lambda C.
\tag{2.1}

令

\[
A_0:=\frac g2-a_3.
\tag{2.2}

则 (2.1) 除以 `4`：

\[
\boxed{
5^\lambda C
=3gT-A_0^2-
\frac{81b_3^2}{4}.}
\tag{2.3}

当前

\[
v_2(T)=m,
\qquad
v_2(g)\ge2,
\]
所以

\[
2^m\mid gT.
\]
同时

\[
b_3=2^{M+m+1}5c_Qc_u
\]
给

\[
v_2(b_3^2/4)=2(M+m+1)-2
=6\lambda+2>m.
\]
故 (2.3) 模 `2^m` 精确化为

\[
\boxed{
5^\lambda C
\equiv-A_0^2
\pmod{2^m}.}
\tag{2.4}

这是 natural representative的 binary square phase。

---

## 3. 消去 `C` 得到单变量 `a_3` congruence

把 (2.4) 乘 `theta`，再用 (1.5)：

\[
-\theta A_0^2
\equiv5^{M+\lambda}a_3
=5^{3\lambda}a_3
\pmod{2^m}.
\tag{3.1}

由 (1.4)：

\[
5^{3\lambda}=g\theta-c_Qc_u.
\]
代入 (3.1)：

\[
-\theta A_0^2
\equiv(g\theta-c_Qc_u)a_3.
\]
移项：

\[
\theta(A_0^2+ga_3)
\equiv c_Qc_u a_3
\pmod{2^m}.
\]
而

\[
A_0^2+ga_3
=\left(\frac g2-a_3\right)^2+ga_3
=\frac{g^2}{4}+a_3^2.
\]
因此得到新的 `C`-free bridge：

\[
\boxed{
F_2(a_3)
:=
\theta\left(\frac{g^2}{4}+a_3^2\right)
-c_Qc_u a_3
\equiv0
\pmod{2^m}.}
\tag{3.2}

这条式只含真实 source/third-block integers。

---

## 4. `F_2` 在二进方向永远 simple，因此 residue 唯一

当前 `g` 被 `4` 整除，而 `a_3,theta,c_Q,c_u` 都为奇数。模 `2`：

\[
\frac{g^2}{4}\equiv0,
\qquad
a_3^2\equiv1,
\]
所以

\[
F_2(a_3)
\equiv1-1
\equiv0\pmod2.
\tag{4.1}

也就是说唯一 odd class本身就是 first root。

另一方面

\[
\boxed{
F_2'(a_3)
=2\theta a_3-c_Qc_u.}
\tag{4.2}

第一项为偶数，第二项为奇数，因此

\[
\boxed{F_2'(a_3)\equiv1\pmod2.}
\tag{4.3}

ordinary Hensel lemma 遂给：从唯一 root modulo `2` 开始，对每个 `n>=1` 都存在唯一 lift modulo `2^n`。特别地存在唯一

\[
\boxed{
a_{3,(2)}\in\mathbb Z/2^m\mathbb Z}
\tag{4.4}

满足 (3.2)。

因此固定 `(lambda,g,c_u,theta)` 后，third numerator 在整个 binary direction没有 residue branching。

---

## 5. 长 Gaussian orientation 给唯一 `5^{lambda-1}` residue

前一文件已严格证明

\[
v_{\pi_\iota}(\mathcal Z_*)=1,
\qquad
v_{\bar\pi_\iota}(\mathcal Z_*)=\lambda-1,
\tag{5.1}

其中 `pi_iota in {2+i,2-i}`；交换命名会同步交换两条 orientation。

固定长 orientation `bar pi_iota^{lambda-1}`。在 quotient

\[
\mathbb Z[i]/(\bar\pi_\iota^{\lambda-1})
\cong
\mathbb Z/5^{\lambda-1}\mathbb Z
\]
中，`i` 映到唯一对应的 Hensel root

\[
\iota_{\lambda-1}^2\equiv-1
\pmod{5^{\lambda-1}}.
\tag{5.2}

由

\[
\mathcal Z_*=g-2a_3-9ib_3
\]
得到

\[
\boxed{
g-2a_3-9\iota_{\lambda-1}b_3
\equiv0
\pmod{5^{\lambda-1}}.}
\tag{5.3}

因为 `2` 是 `5`-进单位，orientation选定后唯一固定

\[
\boxed{
a_{3,(5)}
\equiv
\frac{g-9\iota_{\lambda-1}b_3}{2}
\pmod{5^{\lambda-1}}.}
\tag{5.4}

另一 Gaussian orientation对应另一个 root `-iota_{lambda-1}`。因此在未预先固定 orientation 时，最多有两条 `5`-adic residue；固定 canonical Gaussian phase后只有一条。

---

## 6. CRT modulus 恰好是 `T/25`

两个模数互素：

\[
2^m,
\qquad
5^{\lambda-1}.
\]
所以固定 Gaussian orientation 后，(4.4) 与 (5.4) 由 CRT 唯一确定

\[
\boxed{
R_3^{\rm CRT}
\in[0,\mathfrak M_3),}
\tag{6.1}

其中

\[
\begin{aligned}
\mathfrak M_3
&:=2^m5^{\lambda-1}\\
&=2^{\lambda+1}5^{\lambda-1}\\
&=\frac{10^{\lambda+1}}{25}\\
&=\boxed{\frac T{25}}.
\end{aligned}
\tag{6.2}

这个 modulus随无界高度指数增长；它与之前 fixed `23^4` residue性质完全不同。

---

## 7. third-numerator digit window 只有 CRT cell 的十分之一

当前危险 endpoint 已有严格 third numerator window

\[
\boxed{
1<\zeta:=\frac{a_3}{T}<\frac{251}{250}.}
\tag{7.1}

所以

\[
\boxed{
T<a_3<T+\frac T{250}.}
\tag{7.2}

由 (6.2)：

\[
T=25\mathfrak M_3,
\qquad
\frac T{250}=\frac{\mathfrak M_3}{10}.
\tag{7.3}

因此 `T` 本身被 `mathfrak M_3` 整除。写

\[
h:=a_3-T.
\]
则实际 third numerator 必满足

\[
\boxed{
0<h<\frac{\mathfrak M_3}{10},
\qquad
h\equiv R_3^{\rm CRT}\pmod{\mathfrak M_3}.}
\tag{7.4}

因为区间长度严格小于一个完整 modulus，立即得到：

\[
\boxed{
\text{每个 Gaussian orientation 在真实 third-numerator window中至多有一个 }a_3.}
\tag{7.5}

更精确地，存在候选当且仅当 CRT 的最小非负代表满足

\[
\boxed{
0<R_3^{\rm CRT}<\frac{\mathfrak M_3}{10}.}
\tag{7.6}

若成立，则候选被完全恢复为

\[
\boxed{
a_3=T+R_3^{\rm CRT}.}
\tag{7.7}

---

## 8. 更新后的 global representative frontier

此前 fixed-`23^4` canonical residue相对于 `C` interval太短，无法提供 pruning。本文得到的是不同量级的结果：

\[
\boxed{\mathfrak M_3=T/25}
\]
与 third-numerator window同指数尺度，而窗口只占一个 CRT cell 的 `1/10`。

因此最后的 `(1,1587,1,+)` type 已经从

\[
\text{连续 }a_3\text{ digit interval}
\]
压成

\[
\boxed{
\text{每个 source state / Gaussian orientation至多一个显式 CRT representative}.}
\]

下一步不应再对 `a_3` 做连续估计。应研究 representative test (7.6)：

1. 用 `g theta=5^{3lambda}+1587c_u` 计算唯一 binary root `a_{3,(2)}`；
2. 用 long Gaussian orientation计算 `a_{3,(5)}`；
3. 证明 CRT representative统一不进入 `(0,M_3/10)`，或把进入情况进一步压成有限 source residue classes。

这已经是一个真正随高度增长的 natural-representative closure target。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-blowup-nogo"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-blowup-nogo.md`

# A2 fixed `23` `eta=2`, `v_23(c_Q)=2` 的 high-2 bridge 与三变量 blow-up no-go

> **依赖：** `spontaneous-cq-fixed23-eta2-slots.md`、`spontaneous-cq-relative-depth-nogo.md`、`spontaneous-cq-canonical-defect-overlap.md`、`endpoint-lattice.md` §16.7。
>
> **严格状态：**`eta=2` 的 fixed-`23` high-2 lattice只剩一个 `v_23(c_Q)=2` 类型 `(d,c_Q,k_h,slot)=(1,1587,1,+)`。本文把 high-2 equality 与 canonical `c_- / c_+` allocation 提升到 `23^4` square depth，得到一个以 `q_2:=Q/23^2` 为第三坐标的精确有限阶 bridge。第二层化简后，两种 orientation 分别为 `rho^2=16q_2` 与 `rho(rho+2)=16q_2`。与 prefix/additive blow-up 联立后，只有 `M=170,236 mod506` 强迫 common depth停在第一层；其余 `21` 个 `mod506` 类的 augmented Jacobian 都是 unit。故在该类型中，普通 higher-order Hensel singularity 不能继续产生 parity obstruction；若要进一步限制真实 arithmetic orbit，必须加入 finite-defect natural representative、decimal interval 或其他 global input。

---

## 1. 唯一 `c=2` high-2 类型

固定

\[
p:=23.
\]

`spontaneous-cq-fixed23-eta2-slots.md` 已证明 `eta=2`、`23|c_Q` 的 high-2 family 只有三型。唯一满足

\[
v_p(c_Q)=2
\]
的是

\[
\boxed{
(d,c_Q,k_h,\varepsilon)
=(1,1587,1,+1),
}
\tag{1.1}

其中

\[
1587=3p^2.
\]

`eta=2` 与 `d=1` 给

\[
M=2m-2,
\qquad
\lambda=m-1,
\qquad
\boxed{M=2\lambda}.
\tag{1.2}

fixed `23` first layer又给

\[
\boxed{M\equiv16\pmod{22}}.
\tag{1.3}

记

\[
N:=10^M,
\qquad
T:=10^m,
\qquad
A:=a_2,
\qquad
B:=b_2,
\qquad
K:=9N+10A.
\tag{1.4}

因为 `v_p(c_Q)=2` 且 `p\nmid q`，定义 unit

\[
\boxed{q_2:=\frac Q{p^2}},
\qquad
Q=B+2N=p^2q_2.
\tag{1.5}

所以

\[
\boxed{B=-2N+p^2q_2.}
\tag{1.6}

并且

\[
A=\frac{K-9N}{10}.
\tag{1.7}

---

## 2. canonical square depth 给 high-2 的 `p^4` congruence

令

\[
s=+1\Longleftrightarrow p^2\Vert c_-,
\qquad
s=-1\Longleftrightarrow p^2\Vert c_+.
\tag{2.1}

canonical factorization 为

\[
H_0-Y_3=5^\lambda c_-^2X,
\qquad
H_0+Y_3=c_+^2Y,
\qquad
Y_3=ga_3.
\tag{2.2}

由于 `p\nmid XYg`，chosen orientation具有精确 square depth `4`，故

\[
\boxed{H_0\equiv sga_3\pmod{p^4}.}
\tag{2.3}

当前 high-2 slot 为 `varepsilon=+1`：

\[
H_0+Y_2=\frac{g^2}{2},
\qquad
Y_2=A c_Q5^d=15p^2A.
\tag{2.4}

因此

\[
\boxed{
\frac{g^2}{2}-15p^2A
\equiv sga_3
\pmod{p^4}.}
\tag{2.5}

另一方面 reflection denominator 与 source ratio给

\[
B=2^{M+m+1}c_ug,
\qquad
\rho:=\frac{q5^\lambda}{c_u}.
\tag{2.6}

由

\[
q_2=2^{M+1}\cdot3q,
\qquad
\lambda=m-1,
\]
直接得到 exact identity

\[
\boxed{15B\rho=q_2Tg.}
\tag{2.7}

这将 high-2 equality中的 `g/c_u` 完全消去。

---

## 3. 两个 orientation 的 finite-order high-2 bridge

`spontaneous-cq-canonical-defect-overlap.md` 已有 exact identity

\[
K-\rho\zeta=(\rho+1)J,
\qquad
\zeta:=\frac{a_3}{T}.
\tag{3.1}

### minus orientation: `p^2||c_-`

此时

\[
v_p(J)=4,
\]
故模 `p^4`：

\[
\zeta\equiv\frac K\rho,
\qquad
 a_3\equiv\frac{TK}{\rho}.
\tag{3.2-}

把 (2.7)、(3.2-) 代入 (2.5)，清去 p-adic units 后得到

\[
\boxed{
\mathcal H_-
:=15B^2\rho^2
-2BKT^2q_2
-2p^2AT^2q_2^2
\equiv0\pmod{p^4}.}
\tag{3.3-}

### plus orientation: `p^2||c_+`

此时

\[
v_p(TJ+2a_3)=4,
\]
等价于

\[
J+2\zeta\equiv0\pmod{p^4}.
\]
结合 (3.1)：

\[
\zeta\equiv-\frac K{\rho+2},
\qquad
 a_3\equiv-\frac{TK}{\rho+2}.
\tag{3.2+}

因此

\[
\boxed{
\begin{aligned}
\mathcal H_+
:={}&15B^2\rho^2(\rho+2)
-2B\rho KT^2q_2\\
&-2p^2AT^2q_2^2(\rho+2)
\equiv0\pmod{p^4}.
\end{aligned}}
\tag{3.3+}

这两式只使用了真实 high-2 equality、canonical square allocation 与 denominator/source 定义；没有引入新的自由参数。

---

## 4. 第一 normalized layer：`q_2` bridge

由 (1.3)：

\[
N\equiv4\pmod p,
\qquad
B\equiv-8\equiv15\pmod p.
\tag{4.1}

又

\[
m=\frac{M+2}{2}
\]
且 `M=16 mod22`，故

\[
\boxed{T^2\equiv9\pmod p.}
\tag{4.2}

fixed `23` angle first layer为

\[
K\equiv16\pmod p.
\tag{4.3}

把 (4.1)–(4.3) 代入 (3.3±)。minus 中得到

\[
17\rho^2+4q_2=0\pmod p,
\]
即

\[
\boxed{\rho^2=16q_2\pmod p.}
\tag{4.4-}

plus 中先约去 unit `rho`，得到

\[
17\rho(\rho+2)+4q_2=0\pmod p,
\]
即

\[
\boxed{\rho(\rho+2)=16q_2\pmod p.}
\tag{4.4+}

minus orientation有 `rho!=0`；plus orientation有 `rho!=0,-2`。所以两边都自动推出

\[
\boxed{q_2\in\mathbf F_{23}^\times,}
\]
与 `v_p(c_Q)=2` 完全一致。

---

## 5. prefix second layer不含 `q_2`

写

\[
K=16+p\kappa,
\qquad
N^2=16+ph_N.
\tag{5.1}

prefix exact identity为

\[
D_{\rm pref}
=8181N^2-K^2+2025Q(Q-4N).
\tag{5.2}

当前 `Q=p^2q_2`，所以最后一项被 `p^2` 整除。除以 `p` 后模 `p`：

\[
\boxed{
\delta_D:=\frac{D_{\rm pref}}p
\equiv16h_N+22-9\kappa
\pmod p.}
\tag{5.3}

因此 depth 至少 `2` 时

\[
\boxed{9\kappa=16h_N+22\pmod p.}
\tag{5.4}

decimal length写成

\[
M=16+22j,
\qquad0\le j<23.
\]
已有

\[
\boxed{h_N=5+3j\pmod p.}
\tag{5.5}

所以 `M mod506` 唯一固定 `kappa`。

---

## 6. additive second layer继续使用同一 Möbius chart

orientation-resolved additive normalized equations为

\[
\boxed{
\delta_+
:=\frac{g_+}{p}
\equiv\rho(1+14\kappa)+11
\pmod p,}
\tag{6.1+}

\[
\boxed{
\delta_-
:=\frac{g_-}{p}
\equiv\rho(1+14\kappa)-9-18\kappa
\pmod p.}
\tag{6.1-}

因此 genuine depth-`2` additive lift要求

\[
\kappa\notin\{11,18\}.
\tag{6.2}

若 `kappa=18`，projective coefficient消失而常数不消失；若 `kappa=11`，plus 要求 `rho=-2`，minus 要求 `rho=0`，均违反 canonical unit separation。

于是

\[
\boxed{
\kappa\in\{11,18\}
\Longrightarrow d_{23}=1.}
\tag{6.3}

在 `M=16 mod22` 的 `23` 个 `mod506` classes 中，(5.4)–(5.5) 给

\[
\boxed{
\kappa=18\Longleftrightarrow M\equiv170\pmod{506},}
\tag{6.4a}

\[
\boxed{
\kappa=11\Longleftrightarrow M\equiv236\pmod{506}.}
\tag{6.4b}

所以当前 `c=2` high-2 type 已有两条 orientation-independent odd-depth certification：

\[
\boxed{
M\equiv170,236\pmod{506}
\Longrightarrow d_{23}=1.}
\tag{6.5}

---

## 7. 其余 `21` 类：`rho` 与 `q_2` 都被唯一固定

若

\[
\kappa\notin\{11,18\},
\]
则 additive equation唯一给

\[
\rho_+(\kappa)
=-\frac{11}{1+14\kappa},
\tag{7.1+}

\[
\rho_-(\kappa)
=\frac{9+18\kappa}{1+14\kappa}.
\tag{7.1-}

再由 high-2 bridge：

### minus orientation

\[
\boxed{
q_2=16^{-1}\rho_-^2\pmod p.}
\tag{7.2-}

### plus orientation

\[
\boxed{
q_2=16^{-1}\rho_+(\rho_++2)\pmod p.}
\tag{7.2+}

由于 genuine unit boundaries，上述 `q_2` 都非零。因此对每个 surviving `M mod506` class、每个 canonical orientation，第二层存在唯一 normalized triple

\[
\boxed{(\kappa,\rho,q_2)\pmod{23}.}
\tag{7.3}

---

## 8. augmented blow-up Jacobian 是 unit

把第二层 normalized system写成

\[
F_1:=\delta_D,
\qquad
F_2:=\delta_\sigma,
\qquad
F_3:=h_\sigma,
\]
其中

\[
h_-:=\rho^2-16q_2,
\tag{8.1-}

\[
h_+:=\rho(\rho+2)-16q_2.
\tag{8.1+}

以

\[
(\kappa,\rho,q_2)
\]
为 correction variables。三个关键 transverse derivatives 为

\[
\frac{\partial F_1}{\partial\kappa}=-9,
\tag{8.2a}

\[
\frac{\partial F_2}{\partial\rho}=1+14\kappa,
\tag{8.2b}

\[
\frac{\partial F_3}{\partial q_2}=-16.
\tag{8.2c}

而 `F_1` 不含 `rho,q_2`，`F_2` 不含 `q_2`，故 Jacobian 为下三角形：

\[
\boxed{
J_{\rm aug}
=(-9)(1+14\kappa)(-16).}
\tag{8.3}

在 genuine surviving root上

\[
\kappa\ne18,
\]
所以

\[
1+14\kappa\ne0.
\]
因此

\[
\boxed{J_{\rm aug}\in\mathbf F_{23}^\times.}
\tag{8.4}

`kappa=11` 虽然 determinant仍为 unit，但该点没有 genuine source-unit root，已经在 §6 删除。

---

## 9. finite-order Hensel no-go 到 full square cap

当前 pure-`c_Q` cap 为

\[
2c=4.
\]

canonical high-2 bridge (3.3±) 本身已经有效到 `p^4`。§8 表明，在任意 genuine second-layer root处，`prefix/additive/high-2` 三变量 correction map 对

\[
(\kappa,\rho,q_2)
\]
是 transverse unit system。

因此继续从 `p^2` 推到 `p^3`、再推到 `p^4` 时：

1. 新的 decimal-length digit只进入 normalized constant term；
2. `K` 的下一 correction 由 prefix equation线性确定；
3. `rho` 的下一 correction由 additive equation线性确定；
4. `q_2` 的下一 correction由 high-2 equation线性确定；
5. 三个线性系数始终分别还原为 (8.2a)–(8.2c) 的 units。

故不存在新的 singular branch、odd-layer跳跃或 fixed exceptional residue。

严格地说，这证明的是：

\[
\boxed{
\text{对 surviving second-layer class，普通 local Hensel / derivative 路线}
\text{不能强迫 common depth 的 parity。}}
\tag{9.1}

特别地，继续单独计算 `23^3`、`23^4` 的 discriminant/resultant 不会产生新的 local obstruction；任何新的限制必须来自真实 arithmetic orbit 对 `(K,rho,q_2)` 的 global representative 约束。

---

## 10. 与 fixed `23` length ledger 的合并

当前 `(d,c_Q,k_h)=(1,1587,1)` type 的 fixed `23` ledger 可写成：

\[
\boxed{
\begin{array}{c|c}
M\bmod506&\text{结论}\\ \hline
170,236&d_{23}=1\text{，严格 odd-depth}\\
\text{其余 }21\text{ 类}&\text{第二层有唯一 }(\kappa,\rho,q_2)\text{；augmented system smooth}
\end{array}}
\tag{10.1}

其中 `M=302 mod506` 对应旧 simultaneous-gate class

\[
\kappa=4,
\qquad
\rho=-1.
\]
此时两个 additive orientation gate同时提升到第二层；high-2 bridge仍用 `C` / canonical allocation 区分 orientation，并分别唯一固定不同的 `q_2 mod23`。

---

## 11. 更新后的 frontier

`eta=2` fixed `23` 三型现在分成两种性质：

1. 两个 `c=1,d=2` 类型已有真正的 high-2/source/prefix 三方曲线，产生四条 orientation-independent `mod506` depth-1 classes；
2. 唯一 `c=2,d=1` 类型在第二层只留下 `M=170,236` 两条强制 depth-1 class，而其余 roots 的 augmented Jacobian 为 unit。

所以 `(1,1587,1,+)` 后续最有价值的输入已经不再是 higher-order local `23` algebra。应直接加入

\[
\boxed{
C=\operatorname{res}_{(0,\mathfrak L_0)}(\cdots),
\qquad
0<C<\frac{3D}{250},
}
\]

以及本文 §2 的 canonical `C mod23^4` orientation residue，或使用 Gaussian center representative。目标应是限制真实 global representative，而不是继续扩展 smooth Hensel tree。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-centered-a3-map"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-centered-a3-map.md`

# A2 fixed `23` `eta=2` `c=2` 的 centered `a_3` map

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`、`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md`、`spontaneous-cq-fixed23-eta2-c2-full-a3-crt.md`。
>
> **严格状态：**source divisor certificate以 `theta` 参数化每个候选，并分别计算 binary Hensel root。本文改用 centered variable `varrho=20L_*-theta`。由于 `L_*` 同时含完整 `2^m` 与 `5^lambda`，局部有 `theta=-varrho`；再利用 `gtheta=S_lambda(c_u)`，binary polynomial在变量 `u=varrho*a_3` 下完全消去 `theta,g,varrho`，变成只依赖 `(lambda,c_u)` 的唯一 Hensel root。long-5 residue也化成 `varrho^{-1}` 的仿射式。因此同一 `(lambda,c_u)` 下所有 source divisors共享一套预计算 local data。

---

## 1. centered source variable

定义

\[
c:=c_Qc_u=1587c_u,
\]

\[
\boxed{
S:=\mathscr S_\lambda(c_u)
=5^{3\lambda}+c.}
\tag{1.1}

已有

\[
g\theta=S.
\tag{1.2}

同时

\[
L_*=2^m5^\lambda c_u,
\qquad
\boxed{\varrho:=20L_*-\theta.}
\tag{1.3}

centered source-slot proof给

\[
\frac14L_*<\varrho<\frac12L_*,
\qquad
\gcd(\varrho,L_*)=1.
\tag{1.4}

特别地 `varrho` 是 `2`-进与 `5`-进 unit。

因为

\[
2^m\mid L_*,
\qquad
5^{\lambda-1}\mid L_*,
\]
在两套 local rings 中统一有

\[
\boxed{\theta\equiv-\varrho.}
\tag{1.5}

---

## 2. binary polynomial 在 `u=varrho a_3` 下完全 source-only

前面的 binary bridge为

\[
\theta\left(\frac{g^2}{4}+a_3^2\right)
-ca_3
\equiv0
\pmod{2^m}.
\tag{2.1}

由 (1.2)、(1.5)：

\[
g\equiv-S\varrho^{-1}\pmod{2^m}.
\tag{2.2}

将其代入 (2.1)：

\[
-\varrho
\left(
\frac{S^2}{4\varrho^2}+a_3^2
\right)
-ca_3
\equiv0.
\]
乘以 unit `-varrho`：

\[
\varrho^2a_3^2
+c\varrho a_3
+\frac{S^2}{4}
\equiv0
\pmod{2^m}.
\]
定义

\[
\boxed{u:=\varrho a_3.}
\tag{2.3}

得到完全 source-only 的二次式

\[
\boxed{
F_{\rm cent}(u)
:=u^2+cu+\frac{S^2}{4}
\equiv0
\pmod{2^m}.}
\tag{2.4}

这里 `S` 被 `4` 整除，因为 `S=gtheta`、`v_2(g)>=2`，所以 `S^2/4` 为整数。

---

## 3. centered binary root 对每个 `(lambda,c_u)` 唯一

导数为

\[
\boxed{F_{\rm cent}'(u)=2u+c.}
\tag{3.1}

`c=1587c_u` 为奇数，所以

\[
\boxed{F_{\rm cent}'(u)\equiv1\pmod2.}
\tag{3.2}

模 `2` 时 `S^2/4` 为偶数，因为 `v_2(S)>=2`，而 `u` 必为奇数，因此

\[
F_{\rm cent}(1)
\equiv1+1+0
\equiv0\pmod2.
\]
ordinary Hensel lemma给出唯一

\[
\boxed{u_2(\lambda,c_u)\pmod{2^m}}
\tag{3.3}

满足 (2.4)。

于是对同一 `(lambda,c_u)` 下任何 admissible source divisor `theta`，只需计算

\[
\varrho=20L_*-\theta
\]
并取 inverse：

\[
\boxed{
a_{3,(2)}
\equiv
u_2\varrho^{-1}
\pmod{2^m}.}
\tag{3.4}

binary Hensel tree只需预计算一次。

---

## 4. long-5 root 也变成 centered affine map

source-divisor certificate 的 long-5 residue为

\[
a_{3,(5)}
\equiv
\frac c2
\left(
\theta^{-1}
-45\iota\,2^{3\lambda+2}
\right)
\pmod{5^{\lambda-1}}.
\tag{4.1}

由 (1.5)：

\[
\theta^{-1}\equiv-\varrho^{-1}
\pmod{5^{\lambda-1}}.
\]
所以

\[
\boxed{
a_{3,(5)}
\equiv
-\frac c2\varrho^{-1}
-\frac{45c}{2}\iota\,2^{3\lambda+2}
\pmod{5^{\lambda-1}}.}
\tag{4.2}

固定 `(lambda,c_u,iota)` 后，第二项是常量，divisor dependency只在 `varrho^{-1}`。

若改写成 `u=varrho a_3`：

\[
\boxed{u_{(5)}
\equiv
-\frac c2
-\frac{45c}{2}\iota\,2^{3\lambda+2}\varrho
\pmod{5^{\lambda-1}}.}
\tag{4.3}

因此 `u` 的 binary residue完全固定，而 5-adic residue对 `varrho` 只是线性函数。

---

## 5. full CRT 的 centered implementation

对 fixed `(lambda,c_u)` 可预计算：

\[
A:=2^m,
\qquad
B:=5^{\lambda-1},
\qquad
u_2\pmod A.
\]

然后每个 source divisor只需：

1. `varrho=20L_*-theta`；
2. 检查 centered slot `L_*/4<varrho<L_*/2`；
3. 计算 `varrho^{-1} mod A,B`；
4. 用 (3.4)、(4.2) 得两条 `a_3` residue；
5. 加入 canonical `c_Q` root并做 full CRT `1/15870` cell test。

这把每 divisor 的 expensive local lifting替换为常数次 modular inverse / affine arithmetic。

---

## 6. source discriminant interpretation

(2.4) 的判别式为

\[
\begin{aligned}
\Delta_{\rm cent}
&=c^2-S^2\\
&=c^2-(5^{3\lambda}+c)^2\\
&=\boxed{-5^{3\lambda}(5^{3\lambda}+2c).}
\end{aligned}
\tag{6.1}

由于 `c=1587c_u` 且 `c_u=1 mod4`，直接检查有

\[
\Delta_{\rm cent}\equiv1\pmod8,
\]
所以它在 `Z_2^times` 中确实为平方。这个 character没有提供额外 obstruction；真正有用的信息是 derivative unit导致的**唯一 centered branch**。

---

## 7. updated frontier

当前 source divisor family 的 local dependence 已降到：

\[
\boxed{
\theta
\longleftrightarrow
\varrho
\longmapsto
\left(
\nu_2\varrho^{-1},
-\frac c2\varrho^{-1}-K_5
\right),}
\]
其中 `u_2` 和 `K_5` 对固定 `(lambda,c_u,orientation)` 都预先确定。

因此若继续统一 closure，最自然的对象已是 centered divisor `varrho` 在 full CRT cell 中的 Möbius/affine image，而不是重新研究 `g,a_3` 的 local Hensel lifting。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-centered-canonical-root"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-centered-canonical-root.md`

# A2 fixed `23` `eta=2` `c=2` 的 centered canonical root

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-centered-a3-map.md`、`spontaneous-cq-fixed23-eta2-c2-full-a3-crt.md`、`spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`。
>
> **严格状态：**令 `u=varrho*a_3`。前一文件已使 binary root `u mod2^m` 完全 source-only，而 long-5 root对 `varrho` 线性。本文证明 canonical `c_Q=1587` residue 在 centered 变量中也完全消去 `c_u,theta,g,varrho`：对完整 allocation `c_Q=c_-c_+`，有 `u=-(21/2)5^(3lambda) mod c_-` 与相反符号的 `mod c_+` root。注意 `varrho` 不是完整的 `c_Q`-unit：它被 `3` 整除、但仍是 `23`-进 unit。该事实不影响推导，因为本文在 canonical 方向只乘 `varrho`，不对它取模 `c_Q` 的逆。于是 full local data中只有 `5^(lambda-1)` coordinate仍依赖具体 source divisor；`2^m` 与 `c_Q` 两个方向均可预计算。

---

## 1. centered variable modulo `c_Q`

当前

\[
c_Q=1587=3\cdot23^2,
\qquad
S:=5^{3\lambda}+c_Qc_u,
\]

\[
g\theta=S,
\qquad
\varrho=20L_*-\theta,
\]

\[
L_*=2^{\lambda+1}5^\lambda c_u.
\tag{1.1}

exact Hensel relation为

\[
\theta=c_Q\omega-L_*.
\]
所以

\[
\boxed{\theta\equiv-L_*\pmod{c_Q}.}
\tag{1.2}

又

\[
\varrho=20L_*-\theta,
\]
故

\[
\boxed{\varrho\equiv21L_*\pmod{c_Q}.}
\tag{1.3}

source primitive separation给

\[
\gcd(L_*,c_Q)=1.
\]
因此 `theta` 是完整的 `c_Q`-unit。对 `varrho` 则必须分别读取 `3` 与 `23`：

\[
\boxed{3\mid\varrho,}
\tag{1.4a}

因为 `21L_*` 被 `3` 整除；而

\[
\boxed{23\nmid\varrho,}
\tag{1.4b}

因为 `21L_*` 是 `23`-进 unit。也就是说

\[
\boxed{\gcd(\varrho,23)=1,
\qquad 3\mid\varrho.}
\tag{1.5}

本文后续不在模 `c_Q` 下对 `varrho` 取逆，所以这一非单位性不会造成任何除法问题。

由于 `c_Q\mid b_3` 且 `\gcd(a_3,b_3)=1`，还有

\[
\boxed{3\nmid a_3.}
\tag{1.6}

故 centered variable

\[
u:=\varrho a_3
\]
自动满足

\[
\boxed{3\mid u.}
\tag{1.7}

本文暂不宣称 `v_3(varrho)=1`；更高 `3`-进深度仍可能发生。

---

## 2. `g mod c_Q` 与具体 divisor `theta` 无关

由

\[
g\theta=S
\]
模 `c_Q`：

\[
g(-L_*)
\equiv5^{3\lambda}
\pmod{c_Q}.
\]
所以

\[
\boxed{
g
\equiv
-5^{3\lambda}L_*^{-1}
\pmod{c_Q}.}
\tag{2.1}

将 `L_*` 展开也可写成

\[
\boxed{
g
\equiv
-5^{2\lambda}
(2^{\lambda+1}c_u)^{-1}
\pmod{c_Q}.}
\tag{2.2}

这里逆元合法，因为 `L_*` 与 `c_Q` 互素。于是固定 `(lambda,c_u)` 后，canonical `a_3 mod c_Q` root与具体 source divisor完全无关。

---

## 3. centered canonical root 完全消去 source content

定义

\[
\boxed{u:=\varrho a_3.}
\tag{3.1}

endpoint directed factors给

\[
a_3\equiv\frac g2\pmod{c_-},
\qquad
 a_3\equiv-\frac g2\pmod{c_+}.
\tag{3.2}

由 (1.3)、(2.1)：

\[
\varrho\frac g2
\equiv
21L_*\cdot
\frac{-5^{3\lambda}L_*^{-1}}2
\pmod{c_Q}.
\]
所以

\[
\boxed{
\varrho\frac g2
\equiv
-\frac{21}{2}5^{3\lambda}
\pmod{c_Q}.}
\tag{3.3}

把 (3.2) 乘 `varrho`，得到：

### minus canonical side

\[
\boxed{u
\equiv
-\frac{21}{2}5^{3\lambda}
\pmod{c_-}.}
\tag{3.4-}

### plus canonical side

\[
\boxed{u
\equiv
+\frac{21}{2}5^{3\lambda}
\pmod{c_+}.}
\tag{3.4+}

这里 `2` 与 `5` 在 `c_Q` 上都是 units，因此两个 residue 都良定义；若相应 modulus 含 `3`，右边自然为 `0 mod3`，与 (1.7) 一致。若相应 modulus含 `23^2`，右边则是 `23`-进 unit。

最关键的是：

\[
\boxed{
\text{centered canonical residue只依赖 }(\lambda,c_-,c_+),
\text{与 }c_u,\theta,g,\varrho\text{ 全部无关}.}
\tag{3.5}

---

## 4. full centered local system

`spontaneous-cq-fixed23-eta2-c2-centered-a3-map.md` 已给：

### binary direction

\[
\boxed{u\equiv u_2(\lambda,c_u)\pmod{2^m},}
\tag{4.1}

其中 `u_2` 是

\[
u^2+c_Qc_u u+
\frac{(5^{3\lambda}+c_Qc_u)^2}{4}
\equiv0\pmod{2^m}
\]
的唯一 odd root。

### long Gaussian direction

固定 `iota^2=-1 mod5^(lambda-1)`：

\[
\boxed{u
\equiv
-\frac{c_Qc_u}{2}
-\frac{45c_Qc_u}{2}\,
\iota\,2^{3\lambda+2}\varrho
\pmod{5^{\lambda-1}}.}
\tag{4.2}

### canonical direction

由 (3.4±) 对 `c_-,c_+` 唯一拼成

\[
\boxed{u\equiv u_Q(\lambda,c_-,c_+)\pmod{1587}.}
\tag{4.3}

因此在三个互素模数

\[
2^m,\qquad5^{\lambda-1},\qquad1587
\]
中，只有中间的 `5`-adic coordinate含具体 source divisor `varrho`，而且是线性 dependence。

---

## 5. source-divisor dependence降为单一 affine coordinate

令

\[
B:=5^{\lambda-1}.
\]
固定 `(lambda,c_u,iota)` 后定义 constants

\[
A_5:=-\frac{c_Qc_u}{2},
\]

\[
B_5:=-\frac{45c_Qc_u}{2}
\iota2^{3\lambda+2}.
\]
那么

\[
\boxed{u_{(5)}(\varrho)=A_5+B_5\varrho\pmod B.}
\tag{5.1}

而 `u mod2^m` 与 `u mod1587` 都固定。因此 full CRT representative作为 `varrho` 的函数，已经降为“固定两个 coordinates + 一个 mod-B affine coordinate”的格点轨道。

这提供了比 `a_3`-坐标更适合无界分析的形式：不再有 modular inverse dependence。

---

## 6. proof boundary

本文没有把 `u` 的 full CRT cell直接转回 third-digit interval；因为真实 Archimedean relation

\[
u=\varrho a_3
\]
中的 `varrho` 本身随 source divisor变化。当前严格收益是 local algebra的大幅简化：

\[
\boxed{
\text{divisor dependence}
\quad\text{只存在于一个 }5^{\lambda-1}\text{-adic affine coordinate}.}
\]

下一步应利用 centered real window

\[
L_*/4<\varrho<L_*/2
\]
与 `theta|S`，研究 affine orbit (5.1) 是否能进入 full canonical `a_3` cell；或把这个 affine orbit转成对 source divisor的更深 congruence。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-centered-source-slot"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md`

# A2 fixed `23` `eta=2` `c=2` 的 centered source-divisor slot

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`、`endpoint-lattice.md` §§5,9,13。
>
> **严格状态：**source-only certificate 使用旧的 `19L_*<theta<20L_*`。本文利用当前唯一 type 的 exact high-2 equality，把 `G=g/T` 从 generic plus slot进一步压到 `9.619–9.653`，进而收紧真实 prefix ratio `x`。代回 endpoint 的精确 Hensel quotient ratio后，得到 centered remainder `varrho=20L_*-theta` 的统一窄窗 `L_*/4<varrho<L_*/2`，等价于 `19.5L_*<theta<19.75L_*`。因此 source divisor search 的相对宽度从约 `5.26%` 降至约 `1.28%`。

---

## 1. exact high-2 equation for `G`

当前 type 为

\[
(d,c_Q,k_h,\varepsilon)
=(1,1587,1,+1).
\]

定义

\[
G:=\frac gT,
\qquad
\mathcal H:=\frac{H_0}{gT}
=J+\zeta,
\qquad
\zeta:=\frac{a_3}{T}.
\]

high-2 equality为

\[
H_0+Y_2=\frac{g^2}{2},
\]
其中

\[
Y_2=5c_Qa_2.
\]
又

\[
a_2=y10^{M-1},
\qquad
T^2=10^{2m}=10^{M+2}
\]
因为 `eta=2`。所以

\[
\frac{Y_2}{gT}
=\frac{c_Qy}{200G}.
\]
将 high-2 equality除以 `gT`：

\[
\mathcal H+
\frac{c_Qy}{200G}
=\frac G2.
\]
于是

\[
\boxed{
G^2-2\mathcal HG-
\frac{1587}{100}y=0.}
\tag{1.1}

正根关于 `mathcal H,y` 都严格递增。

---

## 2. `G` 的 type-specific 窄窗

已有 endpoint bounds：

\[
\boxed{
\frac{997}{250}<\mathcal H<\frac{1001}{250},}
\tag{2.1}

\[
\boxed{
\frac{249}{250}<y<1.}
\tag{2.2}

令

\[
P(G;H,y):=G^2-2HG-\frac{1587}{100}y.
\]
在 lower corner直接计算：

\[
P\!\left(
\frac{9619}{1000};
\frac{997}{250},
\frac{249}{250}
\right)
=-\frac{2503}{10^6}<0.
\tag{2.3}

因为正根右侧 `P` 才变正，得到

\[
G>\frac{9619}{1000}.
\]

在 upper corner：

\[
P\!\left(
\frac{9653}{1000};
\frac{1001}{250},1
\right)
=\frac{1837}{200000}>0,
\tag{2.4}

故

\[
G<\frac{9653}{1000}.
\]

所以

\[
\boxed{
\frac{9619}{1000}
<G<
\frac{9653}{1000}.}
\tag{2.5}

---

## 3. exact `x`–`G`–`w` relation

沿用

\[
x:=\frac{b_2}{10^M},
\qquad
w:=\frac{b_3}{10^m}.
\]
reflection denominator ratio为

\[
\frac{b_3}{b_2}=\frac{5c_Q}{g}.
\]
因此

\[
\frac wx
=\frac{5c_Q}{g}\,10^{M-m}.
\]
当前

\[
M-m=\lambda-1,
\qquad
g=GT=G10^{\lambda+1},
\]
所以

\[
\boxed{
\frac wx=\frac{c_Q}{20G}.}
\tag{3.1}

即

\[
\boxed{x=\frac{20Gw}{1587}.}
\tag{3.2}

已有

\[
\frac{837}{1000}<w<\frac{843}{1000}.
\tag{3.3}

结合 (2.5)：

\[
\boxed{
x>x_-:=
\frac{20}{1587}
\frac{9619}{1000}
\frac{837}{1000},}
\tag{3.4}

\[
\boxed{
x<x_+:=
\frac{20}{1587}
\frac{9653}{1000}
\frac{843}{1000}.}
\tag{3.5}

数值上只是帮助阅读：

\[
0.10146<x<0.10256.
\]
证明本身只使用 (3.4)–(3.5) 的精确有理数。

---

## 4. centered Hensel remainder进入 `(1/4,1/2)`

endpoint §9 有 exact ratio

\[
\boxed{
\frac\theta{L_*}
=\frac{2+10^{-M}w}{x},}
\tag{4.1}

以及 centered variable

\[
\boxed{\varrho:=20L_*-\theta.}
\tag{4.2}

因此

\[
\frac\varrho{L_*}
=20-rac{2+10^{-M}w}{x}.
\tag{4.3}

### lower bound

当前 source-window proof 已有 `M>=104`；其实 `M>=16` 已经足够。使用 `w<1`、`x>x_->1/10`：

\[
\frac{10^{-M}w}{x}<10^{1-M}<\frac1{1000}.
\]
所以

\[
\frac\theta{L_*}
<\frac2{x_-}+\frac1{1000}.
\]
精确有理比较给

\[
\frac2{x_-}+\frac1{1000}
<\frac{79}{4}.
\tag{4.4}

故

\[
\boxed{\frac\varrho{L_*}>\frac14.}
\tag{4.5}

### upper bound

由 (4.1) 的 numerator严格大于 `2`，且 `x<x_+`：

\[
\frac\theta{L_*}>rac2{x_+}.
\]
精确比较给

\[
20-rac2{x_+}<\frac12.
\tag{4.6}

故

\[
\boxed{\frac\varrho{L_*}<\frac12.}
\tag{4.7}

综上：

\[
\boxed{
\frac14L_*<\varrho<\frac12L_*.}
\tag{4.8}

---

## 5. source divisor interval同步收紧

由

\[
\theta=20L_*-\varrho,
\]
(4.8) 等价于

\[
\boxed{
\frac{39}{2}L_*
<\theta<
\frac{79}{4}L_*.}
\tag{5.1}

也就是

\[
\boxed{19.5L_*<\theta<19.75L_*.}
\]

相对宽度为

\[
\frac{19.75-19.5}{19.5}
=\frac1{78}
\approx1.28\%.
\]

所以 source-only certificate 中原条件

\[
19L_*<\theta<20L_*
\]
可严格替换成 (5.1)。

仍保留旧本原性

\[
\gcd(\varrho,L_*)=1.
\tag{5.2}

因此真实 source divisor现在必须同时满足：

\[
\boxed{
\theta\mid\mathscr S_\lambda(c_u),
\quad
\theta\text{ odd},
\quad
\frac{39}{2}L_*<\theta<\frac{79}{4}L_*,
\quad
\gcd(20L_*-\theta,L_*)=1.}
\tag{5.3}

---

## 6. 更新后的 certificate

对固定 `(lambda,c_u)`，后续 finite source check应只搜索 (5.3) 的窄 divisor interval，再做 `a_3` CRT representative test。`19–20` 的旧 slot不应继续作为当前 type 的最终搜索窗口。

这仍不证明所有高度的 divisor interval为空；新增的是 type-specific 的严格 centered compression。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-decimal-gaussian-kernel"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-decimal-gaussian-kernel.md`

# A2 fixed `23` `eta=2` `c=2` 的纯 third-block Gaussian kernel

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-gaussian-unit.md`、`endpoint-lattice.md` §§16.7–16.14。
>
> **严格状态：**前一文件利用 `k_h=1` 把 abstract Gaussian quotient压成 unit，并得到 growing Hensel linear form。本文继续消去 `c_u,omega,r_+,R_1`，证明该 linear form的 relevant Gaussian `5`-depth等价于一个只含真实整数 `g,a_3,b_3` 的向量 `Z_*=g-2a_3-9ib_3`。该向量的两个 Gaussian orientations 具有精确深度 `(1,lambda-1)`，其 norm 还精确等于 `12gT-4*5^lambda C`。于是最后的 `c=2` type 已被压成纯 third-block Gaussian near-norm / natural-representative 问题。

---

## 1. 当前 fixed type 的显式 `r_+,R_1`

固定

\[
(d,c_Q,k_h,\varepsilon)
=(1,1587,1,+1).
\tag{1.1}

`endpoint-lattice.md` 的 directed factor system 给

\[
X_h:=\frac{k_hg}{2}=\frac g2,
\]

\[
X_h+a_3=c_+r_+,
\]
以及

\[
R_1=\frac{9b_3}{2c_+}.
\]
因此

\[
\boxed{
c_+r_+=\frac g2+a_3,}
\tag{1.2}

\[
\boxed{
c_+R_1=\frac{9b_3}{2}.}
\tag{1.3}

前一文件的 explicit quotient为

\[
Q_5:=r_++iR_1.
\tag{1.4}

故

\[
\boxed{
c_+Q_5
=\frac12\left(g+2a_3+9ib_3\right).}
\tag{1.5}

---

## 2. source linear form 与纯 third-block 向量等价

前一文件已把 quotient-Hensel kernel写成

\[
\mathcal L_5
:=c_u-c_+\omega Q_5,
\]
并证明

\[
\pi_\iota\bar\pi_\iota^{\lambda-1}
\mid\mathcal L_5,
\qquad
v_{\pi_\iota}(\mathcal L_5)=1.
\tag{2.1}

由 (1.5)：

\[
2\mathcal L_5
=2c_u-\omega(g+2a_3+9ib_3).
\tag{2.2}

source triangle 为

\[
\boxed{g\omega=5^\lambda q+c_u.}
\tag{2.3}

定义

\[
\boxed{
\mathcal Z_*:=g-2a_3-9ib_3.}
\tag{2.4}

则 (2.2)–(2.3) 给精确差式

\[
\boxed{
2\mathcal L_5
=\omega\mathcal Z_*-2\cdot5^\lambda q.}
\tag{2.5}

这里 `2` 与 rational integer `omega` 都是 Gaussian `5`-units；而 `5^lambda q` 在两个 Gaussian orientations 都至少具有深度 `lambda`。因此在所有低于 `lambda` 的 relevant levels，`mathcal L_5` 与 `mathcal Z_*` 具有相同 orientation depths。

---

## 3. `Z_*` 本身就是 scaled canonical Gaussian vector

`endpoint-lattice.md` 还有

\[
X_h-a_3=c_-5^dr_-,
\qquad
R_3=\frac{9b_3}{2c_-5^d}.
\]
当前 `d=1,k_h=1`，所以

\[
\frac g2-a_3=5c_-r_-.
\]
乘 `2`：

\[
\boxed{g-2a_3=10c_-r_-.}
\tag{3.1}

同时

\[
\boxed{9b_3=10c_-R_3.}
\tag{3.2}

因此

\[
\boxed{
\mathcal Z_*
=10c_-\,(r_--iR_3).}
\tag{3.3}

也就是

\[
\boxed{
\mathcal Z_*
=10c_-\,\overline{Z_r},
\qquad Z_r:=r_-+iR_3.}
\tag{3.4}

这说明 (2.5) 中出现的 pure third-block vector并非新的对象；它正是 canonical `Z_r` 去分母后的真实整数代表。

---

## 4. 两个 Gaussian orientation 的赋值都精确

沿用 endpoint 的

\[
\nu_5=\lambda-2d=\lambda-2.
\]
存在 `pi_iota in {2+i,2-i}` 使

\[
Z_r=\pi_\iota^{\nu_5}\mathcal R_5,
\]
且

\[
5\nmid N(\mathcal R_5)=k_hX=X.
\]
所以

\[
v_{\pi_\iota}(Z_r)=\lambda-2,
\qquad
v_{\bar\pi_\iota}(Z_r)=0.
\tag{4.1}

取共轭后两个 orientation 交换。又

\[
10c_-=2c_-\cdot5
=2c_-\pi_\iota\bar\pi_\iota
\]
且 `5\nmid c_-`。由 (3.4)：

\[
\boxed{
 v_{\pi_\iota}(\mathcal Z_*)=1,
\qquad
 v_{\bar\pi_\iota}(\mathcal Z_*)=\lambda-1,}
\tag{4.2}

其中 `pi_iota` 的命名按 (4.1) 选定；若交换 initial orientation，则两式同步交换。

尤其

\[
\boxed{
\pi_\iota\bar\pi_\iota^{\lambda-1}
\Vert_{\rm orient}\mathcal Z_*}
\tag{4.3}

是精确 depth statement。没有隐藏 extra depth。

作为 rational `5`-进投影，(4.2) 立即给

\[
\boxed{v_5(g-2a_3)=1.}
\tag{4.4}

因为 `v_5(b_3)=d=1`，两个坐标都恰好含一个 rational factor `5`，其余 `lambda-2` 深度全部集中到单一 Gaussian orientation。

---

## 5. norm 精确化成 finite-defect near-norm

由 (3.4)：

\[
N(\mathcal Z_*)
=100c_-^2N(Z_r).
\]
endpoint norm transfer 在 `k_h=1` 时为

\[
N(Z_r)=r_-^2+R_3^2
=5^{\nu_5}X
=5^{\lambda-2}X.
\]
所以

\[
\boxed{
N(\mathcal Z_*)
=4\cdot5^\lambda c_-^2X.}
\tag{5.1}

canonical height factor为

\[
H_0-Y_3=5^\lambda c_-^2X.
\]
又 finite-defect coordinate给

\[
H_0-Y_3=gTJ,
\qquad
J=3-\frac CD,
\qquad
5^\lambda D=gT.
\]
因此

\[
\boxed{
(g-2a_3)^2+81b_3^2
=4gTJ.}
\tag{5.2}

展开 `J`：

\[
4gTJ
=12gT-4gT\frac CD
=12gT-4\cdot5^\lambda C.
\]
故最终得到

\[
\boxed{
(g-2a_3)^2+81b_3^2
=12gT-4\cdot5^\lambda C.}
\tag{5.3}

等价地，顶部 finite-defect 具有完全显式的 quadratic representative：

\[
\boxed{
5^\lambda C
=3gT-
\frac{(g-2a_3)^2+81b_3^2}{4}.}
\tag{5.4}

右边确为整数；(3.1)–(3.2) 已表明两个平方项都被 `4` 整除。

---

## 6. Archimedean 近范数

危险 endpoint 有

\[
0<C<\frac{3D}{250}.
\]
由 `gT=5^lambda D`，(5.3) 除以 `12gT` 得

\[
\boxed{
1-\frac1{250}
<
\frac{(g-2a_3)^2+81b_3^2}{12gT}
<1.}
\tag{6.1}

所以

\[
\boxed{
\frac{249}{250}
<
\frac{N(\mathcal Z_*)}{12gT}
<1.}
\tag{6.2}

这把 growing Gaussian-depth condition 与真实 Archimedean scale 放在同一个整数对象上：`mathcal Z_*` 同时具有

\[
(v_{\pi},v_{\bar\pi})=(1,\lambda-1)
\]
和 norm 紧贴 `12gT` 的性质。

---

## 7. 更新后的统一目标

当前 `(1,1587,1,+)` 的 Gaussian 核已可完全抛弃 abstract quotient notation。后续只需研究

\[
\boxed{
\mathcal Z_*=g-2a_3-9ib_3,}
\]
满足

\[
\boxed{
 v_{\pi_\iota}(\mathcal Z_*)=1,
\qquad
 v_{\bar\pi_\iota}(\mathcal Z_*)=\lambda-1,}
\tag{7.1}

\[
\boxed{
N(\mathcal Z_*)
=12gT-4\cdot5^\lambda C,
\qquad0<C<3D/250.}
\tag{7.2}

这已经是一个纯 third-block / source-scale Gaussian approximation problem。若继续推进，优先方向应是：

1. 使用 `b_3=2^{M+m+1}5c_Qc_u` 与 `c_Q=1587` 消去 `b_3`；
2. 使用 `M=2lambda,m=lambda+1` 把全部 exponential scale写成单参数 `lambda`；
3. 对 (7.1) 的 long Gaussian orientation求 natural representative，并与 (6.2) 的窄 norm shell 联立。

local fixed-`23` algebra在这里已完全退出主方程。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-fixed-modulus-nogo"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-fixed-modulus-nogo.md`

# A2 fixed `23` `eta=2` `c=2` 的 fixed-modulus natural-representative no-go

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-blowup-nogo.md`、`spontaneous-cq-canonical-defect-overlap.md`、`endpoint-lattice.md` §§5,13。
>
> **严格状态：**唯一 `v_23(c_Q)=2` high-2 类型 `(d,c_Q,k_h,slot)=(1,1587,1,+)` 具有 canonical `C mod23^4` orientation residue，同时 endpoint 给 `0<C<3D/250`。本文量化这两个条件的尺度，证明允许的 `C` 区间从最小合法长度开始就远长于 `23^4`。因此单独的 fixed `23^4` residue 无法排除任何 orientation；若要获得新 obstruction，必须与随高度增长的 `g,2^m,5^lambda,L_0` 或 Gaussian-center modulus 联立。

---

## 1. type-specific length lattice

当前类型满足

\[
(d,c_Q,k_h,\varepsilon)=(1,1587,1,+1),
\]

\[
M=2m-2,
\qquad
\lambda=m-1,
\qquad
M\equiv16\pmod{22}.
\tag{1.1}

因此

\[
2m-2\equiv16\pmod{22},
\]
即

\[
\boxed{m\equiv9\pmod{11}.}
\tag{1.2}

当前开放 endpoint 已有 `M>=11`，而 (1.1) 的最小非负 fixed-`23` length 是 `M=16`，故

\[
\boxed{m\ge9.}
\tag{1.3}

---

## 2. finite-defect denominator `D` 的指数下界

finite-defect normalization 为

\[
5^\lambda D=g10^m.
\]

由于 `lambda=m-1`：

\[
\boxed{D=5\cdot2^m g.}
\tag{2.1}

另一方面 `endpoint-lattice.md` 的 plus high-2 slot，在 `k_h=1` 时给

\[
\boxed{
\frac g{10^m}>
\frac{2389}{250}.}
\tag{2.2}

代入 (2.1)：

\[
D
>
5\cdot2^m\frac{2389}{250}10^m
=
\boxed{
\frac{2389}{50}\,20^m.}
\tag{2.3}

---

## 3. `C` 的允许区间远长于 `23^4`

危险 `(a,k)=(9,2)` endpoint 已有

\[
\boxed{0<C<\frac{3D}{250}.}
\tag{3.1}

由 (2.3)：

\[
\frac{3D}{250}
>
\frac{3\cdot2389}{12500}\,20^m.
\tag{3.2}

使用最小 `m=9`：

\[
\boxed{
\frac{3D}{250}
>
\frac{3\cdot2389}{12500}\,20^9
=293560320000.}
\tag{3.3}

而 canonical `23^2` square allocation只给固定模数

\[
23^{2c}=23^4=279841.
\tag{3.4}

因此从最小合法长度开始就有

\[
\boxed{
\frac{3D}{250}>23^4.}
\tag{3.5}

实际上两者相差超过一百万倍。

---

## 4. 任意 canonical orientation residue 都有区间代表

两种 orientation 分别要求

\[
C\equiv3D\pmod{23^4}
\tag{4.1-}

\]

或

\[
C\equiv
D\left(3+2a_3T^{-1}\right)
\pmod{23^4}.
\tag{4.1+}

无论右边是哪一个 residue class，取其模 `23^4` 的最小正代表 `r`；若 residue 为零则取 `r=23^4`。总有

\[
0<r\le23^4.
\]

由 (3.5)：

\[
0<r<\frac{3D}{250}.
\]

所以

\[
\boxed{
\text{每一个 fixed }23^4\text{ residue class}
\text{ 都至少有一个代表位于允许的 }C\text{ 区间。}}
\tag{4.2}

因此 canonical orientation residue与 `0<C<3D/250` 单独联立时不可能产生空性。

---

## 5. 更强的审计含义

本文给出的结论比“尚未找到矛盾”更强。对当前无界 type：

\[
\boxed{
C\bmod23^4
+0<C<3D/250
\text{ 在尺度上必然兼容。}}
\tag{5.1}

所以以下路线应停止：

1. 继续只提高 fixed `23` canonical residue的显式写法；
2. 只把 `C mod23^4` 与同一个固定小模数继续 CRT；
3. 期待 `C/D<3/250` 本身与 `23^4` residue冲突。

真正可能提供全局 pruning 的 modulus 必须随无界参数增长。当前规范候选是

\[
\boxed{
g,\quad2^m,\quad5^\lambda,\quad\mathfrak L_0=2c_u^2g^2}
\]

以及 `endpoint-lattice.md` 的 Gaussian center representative。下一步应把 canonical orientation label送入这些 growing-modulus natural representatives，而不是继续研究 fixed `23^4` 单独的 residue geometry。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-full-a3-crt"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-full-a3-crt.md`

# A2 fixed `23` `eta=2` `c=2` 的 full canonical `a_3` CRT representative

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-a3-crt-representative.md`、`spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`、`spontaneous-cq-canonical-defect-overlap.md`。
>
> **严格状态：**此前 third numerator CRT只使用 `2^m` binary root 与 `5^(lambda-1)` Gaussian root，得到 modulus `T/25`，真实 digit window占其 `1/10`。本文加入 canonical square allocation 对 `a_3 mod c_Q` 的 exact directed root。当前 `c_Q=1587=3*23^2` 与 decimal moduli互素，因此 full CRT modulus提升为 `1587*T/25`，而窗口宽度不变，故候选必须落在完整 CRT cell 的前 `1/15870`。固定 pure-23 orientation 后，剩余 3-primary allocation只有两个选择，所以每个 source divisor / Gaussian phase至多检查两个 full representatives。

---

## 1. current canonical divisor choices

当前

\[
\boxed{c_Q=1587=3\cdot23^2.}
\tag{1.1}

canonical allocation满足

\[
c_Q=c_-c_+,
\]
且每个 prime power完整分配到唯一一侧。因此

\[
\boxed{
(c_-,c_+)\in
\{(1,1587),(3,529),(529,3),(1587,1)\}.}
\tag{1.2}

pure fixed-`23` orientation进一步将其二分：

### `23^2|c_-`

\[
\boxed{c_-\in\{529,1587\}.}
\tag{1.3-}

### `23^2|c_+`

\[
\boxed{c_-\in\{1,3\}.}
\tag{1.3+}

也就是说 fixed `23` orientation选定后，只剩 `3`-primary factor在同侧或对侧的二元选择。

---

## 2. directed factor system唯一固定 `a_3 mod c_Q`

当前 `d=1,k_h=1` 的 endpoint directed factors为

\[
\boxed{
\frac g2-a_3=5c_-r_-,}
\tag{2.1-}

\[
\boxed{
\frac g2+a_3=c_+r_+.}
\tag{2.1+}

因为 `g` 被 `4` 整除，`g/2` 为整数；又 `5` 与 `c_Q` 互素。因此

\[
\boxed{
a_3\equiv\frac g2\pmod{c_-},}
\tag{2.2-}

\[
\boxed{
a_3\equiv-\frac g2\pmod{c_+}.}
\tag{2.2+}

并且

\[
\gcd(c_-,c_+)=1.
\]
所以对每个完整 canonical allocation `(c_-,c_+)`，CRT唯一确定

\[
\boxed{
a_{3,(Q)}\pmod{c_Q}.}
\tag{2.3}

这个 residue包含此前 pure-23 marker之外的 `3`-primary side choice。

---

## 3. three-way coprime CRT

前一文件已经得到：

1. 唯一 binary root
   \[
   a_{3,(2)}\pmod{2^m};
   \]
2. 固定 Gaussian orientation后的唯一 long-5 root
   \[
   a_{3,(5)}\pmod{5^{\lambda-1}}.
   \]

现在再加入 (2.3)。三个模数

\[
2^m,
\qquad
5^{\lambda-1},
\qquad
c_Q=1587
\]
两两互素。因此完整 CRT modulus 为

\[
\boxed{
\mathfrak M_3^\sharp
:=c_Q2^m5^{\lambda-1}.}
\tag{3.1}

由 `m=lambda+1` 和 `T=10^m`：

\[
2^m5^{\lambda-1}=\frac T{25}.
\]
故

\[
\boxed{
\mathfrak M_3^\sharp
=1587\frac T{25}.}
\tag{3.2}

固定 source divisor `theta`、Gaussian orientation与 canonical allocation后，三条 residue唯一给

\[
\boxed{
R_{3,\sharp}^{\rm CRT}
\in[0,\mathfrak M_3^\sharp).}
\tag{3.3}

---

## 4. digit window只占 full CRT cell 的 `1/15870`

真实 third-numerator window为

\[
T<a_3<T+\frac T{250}.
\tag{4.1}

full modulus不再整除 `T`，所以定义 shifted representative

\[
\boxed{
H_{3,\sharp}
:=\operatorname{res}_{[0,\mathfrak M_3^\sharp)}
\left(R_{3,\sharp}^{\rm CRT}-T\right).}
\tag{4.2}

若真实 `a_3` 存在，则

\[
a_3=T+h,
\qquad0<h<T/250,
\]
从而 `h` 与 (4.2) 同余。因为 interval长度远小于 modulus，必须有

\[
\boxed{
0<H_{3,\sharp}<\frac T{250}.}
\tag{4.3}

而由 (3.2)：

\[
\frac T{250}
=rac{\mathfrak M_3^\sharp}{1587\cdot10}.
\]
所以 exact representative test 是

\[
\boxed{
0<H_{3,\sharp}
<\frac{\mathfrak M_3^\sharp}{15870}.}
\tag{4.4}

反过来若 (4.4) 成立，则该 CRT class在 digit interval中唯一可能的整数就是

\[
\boxed{a_3=T+H_{3,\sharp}.}
\tag{4.5}

因此 candidate cell比例从旧 two-way CRT 的

\[
\frac1{10}
\]
收紧到

\[
\boxed{\frac1{15870}.}
\tag{4.6}

---

## 5. fixed `23` orientation后的候选数

source-only divisor certificate已经把 `(lambda,c_u,theta)` 固定后 `g` 唯一恢复；Gaussian phase最多两种。

对一个已经选定的 pure-23 canonical orientation：

- 若 `23^2|c_-`，只需检查 `c_-=529,1587`；
- 若 `23^2|c_+`，只需检查 `c_-=1,3`。

所以固定 source divisor与 Gaussian orientation后，full canonical level最多两个 shifted representatives `H_{3,#}`。

每一个必须通过极窄 test (4.4)。

---

## 6. post-CRT reconstruction

若某个 full representative通过 (4.4)，则 `a_3` 已被 exact 恢复。随后无需再搜索其它 continuous third-block variable：

\[
g=\frac{5^{3\lambda}+1587c_u}{\theta},
\]

\[
b_3=2^{3\lambda+2}\cdot5\cdot1587c_u,
\]

\[
a_3=T+H_{3,\sharp}.
\]

接着可由 exact quadratic identity恢复

\[
\boxed{
a_2
=\frac{g^2-4a_3^2-81b_3^2}{20\cdot1587}.}
\tag{6.1}

并检查 prefix digit window、primitive gcd 与 finite-defect `C`。因此 full CRT通过后也只剩确定性验证，没有新的整数枚举。

---

## 7. updated source certificate

对最后的 `(1,1587,1,+)` type，规范 finite certificate应按以下顺序：

1. `lambda=8 mod11` 与 source-content window枚举 `c_u`；
2. 在 centered `19.5–19.75 L_*` interval 中找满足 `theta mod23^3` filter 的奇 divisor；
3. 恢复 `g`；
4. 对至多两个 Gaussian orientations和两个 compatible `3`-allocations计算 full `a_3` CRT；
5. 只保留
   \[
   H_{3,\sharp}/\mathfrak M_3^\sharp<1/15870;
   \]
6. 用 (6.1) 等 exact formulas做最终确定性审计。

与原始无界连续搜索相比，third numerator的 geometric freedom现在被压缩成极小的 canonical CRT cell。无界 closure剩余任务是证明这些 full representatives统一无法进入该 cell，或把进入情况进一步同步到已知 odd-depth classes。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-gaussian-unit"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-gaussian-unit.md`

# A2 fixed `23` `eta=2` `c=2` 的 Gaussian quotient unit collapse

> **依赖：** `spontaneous-cq-fixed23-eta2-slots.md`、`endpoint-lattice.md` §§16.8–16.14。
>
> **严格状态：**唯一 `v_23(c_Q)=2` high-2 类型 `(d,c_Q,k_h,slot)=(1,1587,1,+)` 具有 `k_h=1`。将这一固定值代入 endpoint 的共同 Gaussian divisor reduction，立即强迫 `delta=0` 且 quotient `G_5` 为 Gaussian unit。于是抽象的 `B_5,G_5` composition 完全具体化：原 prefix Gaussian integer `a_2+iC_0` 精确分解为 `(r_-+iR_3)(r_++iR_1)`；同时 Gaussian Hensel kernel化成一个显式随 `lambda` 增长的 linear form `c_u-c_+omega(r_++iR_1)`。本文尚未证明该 linear form不可能具有所需的不对称 `(1,lambda-1)` Gaussian depth，因此不关闭 A2，但删除了该类型中剩余的 abstract quotient-factor freedom。

---

## 1. endpoint Gaussian reduction

沿用 `endpoint-lattice.md`。reflection high-2 中定义

\[
Z_r:=r_-+i\varepsilon R_3,
\qquad
Z_a:=a_2+iC_0.
\]

令

\[
\nu_5:=\lambda-2d.
\]

存在 `pi_iota in {2+i,2-i}` 使

\[
Z_r=\pi_\iota^{\nu_5}\mathcal R_5,
\qquad
Z_a=\pi_\iota^{\nu_5}\mathcal A_5,
\]
且

\[
N(\mathcal R_5)=k_hX,
\qquad
N(\mathcal A_5)=XY.
\tag{1.1}

endpoint §16.12 再定义

\[
\delta:=v_3(X)\bmod2\in\{0,1\}
\]
及共同 Gaussian divisor `alpha_X^sharp`，满足

\[
\mathcal A_5=\alpha_X^\sharp\mathcal B_5,
\qquad
\mathcal R_5=\alpha_X^\sharp\mathcal G_5,
\tag{1.2}

\[
N(\alpha_X^\sharp)=3^\delta X,
\]

\[
\boxed{
N(\mathcal B_5)=\frac{Y}{3^\delta},
\qquad
N(\mathcal G_5)=\frac{k_h}{3^\delta}.}
\tag{1.3}

composition identity 为

\[
\boxed{
\varepsilon r_+-iR_1
=3^\delta\mathcal G_5\overline{\mathcal B_5}.}
\tag{1.4}

---

## 2. `k_h=1` 强迫 `delta=0`

当前 fixed-`23` type 为

\[
\boxed{
(d,c_Q,k_h,\varepsilon)
=(1,1587,1,+1).}
\tag{2.1}

由 (1.3)：

\[
N(\mathcal G_5)=3^{-\delta}.
\]

左边是 Gaussian integer 的非负整数 norm，而 `mathcal G_5` 非零。因此 `delta=1` 会给 `1/3`，不可能。故

\[
\boxed{\delta=0.}
\tag{2.2}

于是

\[
\boxed{N(\mathcal G_5)=1.}
\tag{2.3}

Gaussian 整数中 norm `1` 的元素只有 units：

\[
\boxed{
\mathcal G_5=:u\in\{\pm1,\pm i\}.}
\tag{2.4}

所以该 type 中 endpoint §16.12 的 quotient `G_5` 没有任何非平凡 prime content。

---

## 3. 原 prefix Gaussian integer得到精确二因子分解

由 (1.2) 与 (2.4)：

\[
\mathcal R_5=\alpha_X^\sharp u,
\qquad
\mathcal A_5=\alpha_X^\sharp\mathcal B_5.
\]
因此

\[
\frac{\mathcal A_5}{\mathcal R_5}
=u^{-1}\mathcal B_5.
\tag{3.1}

另一方面 (1.4) 在 `delta=0` 时为

\[
\varepsilon r_+-iR_1
=u\overline{\mathcal B_5}.
\]
取共轭：

\[
\varepsilon r_++iR_1
=\bar u\mathcal B_5
=u^{-1}\mathcal B_5.
\tag{3.2}

与 (3.1) 比较：

\[
\boxed{
\mathcal A_5
=\mathcal R_5(\varepsilon r_++iR_1).}
\tag{3.3}

乘回共同的 `pi_iota^{nu_5}`：

\[
\boxed{
Z_a=Z_r(\varepsilon r_++iR_1).}
\tag{3.4}

当前 `varepsilon=+1`，所以得到完全显式的整数 Gaussian factorization

\[
\boxed{
 a_2+iC_0
=(r_-+iR_3)(r_++iR_1).}
\tag{3.5}

展开两坐标：

\[
\boxed{
a_2=r_-r_+-R_3R_1,}
\tag{3.6a}

\[
\boxed{C_0=r_-R_1+r_+R_3.}
\tag{3.6b}

取范数则恢复

\[
N_0
=(r_-^2+R_3^2)(r_+^2+R_1^2)
=5^{\nu_5}XY,
\]
与已有 norm transfer一致。

(3.5) 的意义在于：此前 endpoint 中“共同 divisor约去后 quotient 是否仍有复杂 Gaussian prime allocation”的问题，在该 fixed type 上完全消失。quotient 已经是显式向量 `r_++iR_1`。

---

## 4. abstract Gaussian Hensel kernel具体化

endpoint §16.13 有

\[
\boxed{
\pi_\iota^d\bar\pi_\iota^{\nu_5+d}
\mid
c_u\mathcal G_5
-\varepsilon c_+\omega\mathcal B_5.}
\tag{4.1}

当前

\[
d=1,
\qquad
\nu_5=\lambda-2,
\qquad
\varepsilon=+1,
\qquad
\mathcal G_5=u.
\]

由 (3.2)：

\[
\mathcal B_5=u(r_++iR_1).
\tag{4.2}

代入 (4.1) 并约去 Gaussian unit `u`：

\[
\boxed{
\pi_\iota\bar\pi_\iota^{\lambda-1}
\mid
c_u-c_+\omega(r_++iR_1).}
\tag{4.3}

其 modulus norm 为

\[
\boxed{
N\!\left(\pi_\iota\bar\pi_\iota^{\lambda-1}\right)
=5^\lambda.}
\tag{4.4}

因此原来的 abstract quotient-Hensel condition 被压成一个明确 Gaussian linear form：

\[
\boxed{
\mathcal L_5
:=c_u-c_+\omega(r_++iR_1).}
\tag{4.5}

它必须具有不对称 Gaussian depth

\[
v_{\pi_\iota}(\mathcal L_5)\ge1,
\qquad
v_{\bar\pi_\iota}(\mathcal L_5)\ge\lambda-1.
\tag{4.6}

而 endpoint §16.14 的短 orientation 精确性进一步给

\[
\boxed{v_{\pi_\iota}(\mathcal L_5)=1.}
\tag{4.7}

所以所有随高度增长的额外 depth 全部集中到 `bar pi_iota` 一侧。

---

## 5. exact quotient form

endpoint §16.14 还给

\[
\mathcal M_5
=\pi_\iota^d\bar\pi_\iota^{\nu_5+d}\mathcal W_5.
\]

在当前 unit collapse 后可吸收 `u` 到 `mathcal W_5`，得到某个

\[
\mathcal W_5^\sharp\in\mathbb Z[i]
\]
使

\[
\boxed{
 c_u-c_+\omega(r_++iR_1)
=
\pi_\iota\bar\pi_\iota^{\lambda-1}
\mathcal W_5^\sharp,}
\tag{5.1}

并且

\[
\boxed{\pi_\iota\nmid\mathcal W_5^\sharp.}
\tag{5.2}

取 norm：

\[
\boxed{
(c_u-c_+\omega r_+)^2
+(c_+\omega R_1)^2
=5^\lambda N(\mathcal W_5^\sharp).}
\tag{5.3}

这已经不含 `alpha_X^sharp,G_5,B_5` 等抽象共同-divisor变量。

---

## 6. 更新后的 closure target

对 `(1,1587,1,+)`，已有两条 local no-go：

1. fixed `23` 的 prefix/additive/high-2 blow-up 在第二层后 smooth；
2. fixed `23^4` orientation residue相对于 `C` 实区间太短，单独没有排除力。

本文进一步把 growing Gaussian modulus压成具体 linear form (4.5)。所以该 type 后续真正的统一目标可写成：

\[
\boxed{
\pi_\iota\bar\pi_\iota^{\lambda-1}
\mid
c_u-c_+\omega(r_++iR_1),
\qquad
v_{\pi_\iota}=1.}
\tag{6.1}

要继续推进，应把 (6.1) 与下面至少一项联立：

- `r_+,R_1` 的 exact endpoint / decimal expressions；
- `c_Q=1587` 对 `c_+` 的有限 divisor choices；
- source Hensel 的 `omega` natural representative；
- 或 (3.5) 的 exact Gaussian factorization 与 prefix digit window。

这里已经没有剩余的 abstract Gaussian quotient prime allocation；开放项是一个显式、随 `lambda` 线性增深的 Gaussian approximation problem。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-lambda52-divisor-exclusion"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-lambda52-divisor-exclusion.md`

# A2 fixed `23` `eta=2` `c=2` 的 `lambda=52, c_u=29` source-divisor exclusion

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-source-window.md`、`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md`、`spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`。
>
> **严格状态：**source window 在最低允许高度 `lambda=52` 只留下 `c_u=29`。本文对 source integer 做完整可验证分解。centered source divisor `theta` 必须落在一个 56 位窄区间；而 source integer 的因子结构分成一个 72 位素数与总乘积仅 38 位的其余因子。任何 divisor 因而必定过小或过大。故 `(lambda,c_u)=(52,29)` 从完整 arithmetic candidate set 中严格排除。

---

## 1. centered divisor requirement

当前唯一 `c=2` type 满足

\[
M=2\lambda,
\qquad
m=\lambda+1,
\qquad
c_Q=1587.
\]

source product 为

\[
\boxed{
\mathscr S_\lambda(c_u)
=5^{3\lambda}+1587c_u
=g\theta.}
\tag{1.1}
\]

并定义

\[
L_*:=2^{\lambda+1}5^\lambda c_u.
\tag{1.2}
\]

`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md` 已证明真实 source divisor 必须满足

\[
\boxed{
\frac{39}{2}L_*<\theta<\frac{79}{4}L_*.
}
\tag{1.3}

本文固定

\[
\boxed{\lambda=52,\qquad c_u=29.}
\tag{1.4}

此时

\[
L_*=580000000000000000000000000000000000000000000000000000.
\tag{1.5}

所以 centered interval 为

\[
\boxed{
11310000000000000000000000000000000000000000000000000000
<\theta
}
\tag{1.6a}

和

\[
\boxed{
\theta<
11455000000000000000000000000000000000000000000000000000.
}
\tag{1.6b}

任何合法 `theta` 因而必须是 56 位整数。

---

## 2. source integer 的完整分解

直接 exact integer factorization 得到

\[
\boxed{
\begin{aligned}
\mathscr S_{52}(29)
={}&2^3\cdot311\cdot1013\cdot1540787\\
&\cdot4691120092228268769101767\\
&\cdot P_{72},
\end{aligned}}
\tag{2.1}

其中

\[
\boxed{
P_{72}
=600954647989450344901853769984896357520599617802323154990245217256098773
}
\tag{2.2}

为素数。

除去 `P_72` 后，其余全部因子的总乘积为

\[
\boxed{
S_{\rm small}
=18217088908728795407321637435454176376.
}
\tag{2.3}

checker 使用 exact multiplication 与 `sympy.isprime` 验证 (2.1)–(2.2)。

---

## 3. divisor gap

任取正 divisor

\[
d\mid\mathscr S_{52}(29).
\]

因为 `P_72` 在完整分解中指数为 `1`，分两种情况。

### 3.1 `P_72` 不整除 `d`

此时

\[
d\mid S_{\rm small},
\]
所以

\[
d\le S_{\rm small}.
\]

而 exact comparison 给

\[
\boxed{
S_{\rm small}<\frac{39}{2}L_*.
}
\tag{3.1}

故 `d` 太小，不能进入 centered interval。

### 3.2 `P_72` 整除 `d`

此时

\[
d\ge P_{72}.
\]

而

\[
\boxed{
P_{72}>\frac{79}{4}L_*.
}
\tag{3.2}

故 `d` 又太大。

因此

\[
\boxed{
\operatorname{Div}(\mathscr S_{52}(29))
\cap
\left(\frac{39}{2}L_*,\frac{79}{4}L_*\right)
=\varnothing.}
\tag{3.3}

该结论比 `theta` 必须为 odd 更强：事实上 source integer 根本没有任何正 divisor 落入窗口。

---

## 4. arithmetic-state exclusion

source-only certificate要求真实 state 至少先存在

\[
\theta\mid\mathscr S_{52}(29)
\]
满足 centered interval。式 (3.3) 已否定这一必要条件，所以无需进入 Gaussian orientation、full `a_3` CRT 或 deterministic reconstruction。

因此

\[
\boxed{
(\lambda,c_u)=(52,29)
\Longrightarrow
\text{no arithmetic state in the final }c=2\text{ type}.}
\tag{4.1}

于是最后 `c=2` type 的最低实际 arithmetic height 已从 `lambda=52` 提升到至少

\[
\boxed{\lambda\ge63.}
\tag{4.2}

这里 (4.2) 是 arithmetic candidate 的高度下界；它不同于此前只针对 fixed-`23` common depth 的 source-content hierarchy。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-lambda74-divisor-exclusion"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-lambda74-divisor-exclusion.md`

# A2 fixed `23` `eta=2` `c=2` 的 `lambda=74, c_u=3917` source-divisor exclusion

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-source-window.md`、`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md`、`spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`。
>
> **严格状态：**source window 在 `lambda=74` 留下 `c_u in {3917,3929}`。本文对 `c_u=3917` 的 source integer 做完整可验证分解。合法 centered source divisor `theta` 必须落在一个 80 位窄区间；而 source integer 的因子结构恰好分成一个 114 位素数与总乘积仅 42 位的其余因子。任何 divisor 因而要么过小、要么过大，centered interval 中没有 divisor。故 `(lambda,c_u)=(74,3917)` arithmetic source state 被严格排除。本文不处理同高度的 `c_u=3929`。

---

## 1. centered divisor requirement

当前唯一 `c=2` type 满足

\[
M=2\lambda,
\qquad
m=\lambda+1,
\qquad
c_Q=1587.
\]

source product为

\[
\boxed{
\mathscr S_\lambda(c_u)
=5^{3\lambda}+1587c_u
=g\theta.}
\tag{1.1}

并定义

\[
L_*:=2^{\lambda+1}5^\lambda c_u.
\tag{1.2}

`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md` 已把真实 divisor window收紧为

\[
\boxed{
\frac{39}{2}L_*<\theta<\frac{79}{4}L_*.}
\tag{1.3}

此外 `theta` 必须为正奇 divisor of `S_lambda(c_u)`。

本文固定

\[
\boxed{\lambda=74,\qquad c_u=3917.}
\tag{1.4}

此时

\[
L_*=2^{75}5^{74}\cdot3917
=\boxed{783400000000000000000000000000000000000000000000000000000000000000000000000000}.
\tag{1.5}

所以 (1.3) 的整数范围为

\[
\boxed{
15276300000000000000000000000000000000000000000000000000000000000000000000000000
<\theta
}
\tag{1.6a}

和

\[
\boxed{
\theta<
15472150000000000000000000000000000000000000000000000000000000000000000000000000.}
\tag{1.6b}

也就是说任何合法 `theta` 必为一个 80 位整数。

---

## 2. source integer 的完整分解

直接整数计算得到

\[
\boxed{
\begin{aligned}
\mathscr S_{74}(3917)
={}&2^8\cdot7\cdot149
\cdot1660311777398843\\
&\cdot755010757548746032247\\
&\cdot P_{114},
\end{aligned}}
\tag{2.1}

其中

\[
\boxed{
P_{114}
=443275675908365257356310830167221246577649755270106234437033874498268569377246437010851938887432890877364857937953
}
\tag{2.2}

为素数。

其余全部因子的总乘积为

\[
\boxed{
S_{\rm small}
:=2^8\cdot7\cdot149
\cdot1660311777398843
\cdot755010757548746032247
=334708746929231021723648971080910156928768.}
\tag{2.3}

这是一个 42 位整数。

checker 使用 exact multiplication 与 `sympy.isprime` 分别验证 (2.1) 和 (2.2)；因此这里不是依赖未证实的 probable-factor heuristic。

---

## 3. divisor gap

任取正 divisor

\[
d\mid\mathscr S_{74}(3917).
\]

因为 `P_114` 在 (2.1) 中指数为 `1`，只有两种情况。

### 3.1 `P_114 not divide d`

则

\[
d\mid S_{\rm small},
\]
所以

\[
\boxed{d\le S_{\rm small}.}
\tag{3.1}

而 exact comparison给

\[
\boxed{
S_{\rm small}
<\frac{39}{2}L_*.}
\tag{3.2}

故 `d` 太小，不能满足 centered window。

### 3.2 `P_114 | d`

则

\[
d\ge P_{114}.
\]
exact comparison给

\[
\boxed{
P_{114}
>\frac{79}{4}L_*.}
\tag{3.3}

所以 `d` 又太大。

综上，source integer中没有 divisor跨入 (1.3)：

\[
\boxed{
\operatorname{Div}(\mathscr S_{74}(3917))
\cap
\left(\frac{39}{2}L_*,\frac{79}{4}L_*\right)
=\varnothing.}
\tag{3.4}

---

## 4. arithmetic-state exclusion

source-only certificate要求真实 state 至少先提供一个 odd divisor

\[
\theta\mid\mathscr S_{74}(3917)
\]
满足 centered interval (1.3)。式 (3.4) 已在进入 `a_3` CRT、Gaussian orientation、canonical `3`-allocation之前否定这个必要条件。

因此得到严格排除：

\[
\boxed{
(\lambda,c_u)=(74,3917)
\Longrightarrow
\text{no arithmetic state in the final }c=2\text{ type}.}
\tag{4.1}

特别地，该 state 不再只是在 fixed-23 parity ledger中被标为 `d_23=1`；它从完整 arithmetic candidate set中消失。

---

## 5. 更新后的 `lambda=74` frontier

`spontaneous-cq-fixed23-eta2-c2-source-window.md` 原来给

\[
\lambda=74:\qquad c_u\in\{3917,3929\}.
\]

本文删除第一项，所以

\[
\boxed{
\lambda=74\Longrightarrow c_u=3929
}
\tag{5.1}

是该高度唯一仍需审计的 source content。

`c_u=3929` 的 source integer虽已有多个小因子，但剩余 127 位部分仍为合数；本文没有完整分解它，因此不对该 state 作越界结论。后续可继续 source divisor factor certificate，或绕过完整 factorization直接使用 full centered `a_3` map / natural representative。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-reconstruction-certificate"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-reconstruction-certificate.md`

# A2 fixed `23` `eta=2` `c=2` 的 deterministic reconstruction certificate

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`、`spontaneous-cq-fixed23-eta2-c2-full-a3-crt.md`、`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md`、`spontaneous-cq-global-coupling.md`。
>
> **严格状态：**前面的工作已把唯一 type `(d,c_Q,k_h,slot)=(1,1587,1,+)` 压成 source divisor `theta` 与 full canonical `a_3` CRT representative。本文记录通过该 representative 后的完整确定性恢复链：`g,b_3,a_3` 固定后，`a_2,b_2,C,X,Y,q,omega` 全部由精确整数公式唯一确定，最后可直接计算 fixed-`23` common depth。于是未来的有限 certificate / agent search只需产生 source divisor `theta`；任何 candidate均可在无进一步枚举的情况下完成全链审计。

---

## 1. certificate input

固定

\[
\boxed{
\lambda\equiv8\pmod{11},
\qquad
c_u,
\qquad
\theta,
\qquad
\iota,
\qquad
c_-c_+=1587.}
\tag{1.1}

其中：

- `c_u` 满足 source-content real window，并且每个素因子 `=1 mod4`；
- `theta` 为
  \[
  S:=5^{3\lambda}+1587c_u
  \]
  的正奇因子；
- centered slot
  \[
  \frac{39}{2}L_*<\theta<\frac{79}{4}L_*,
  \qquad
  L_*=2^{\lambda+1}5^\lambda c_u;
  \]
- `iota` 是 `i^2=-1 mod5^(lambda-1)` 的两种 Gaussian orientation之一；
- `(c_-,c_+)` 属于
  \[
  (1,1587),(3,529),(529,3),(1587,1).
  \]

fixed `23` orientation已知时，只保留相应的两个 allocation。

---

## 2. source variables全部恢复

定义

\[
M:=2\lambda,
\qquad
m:=\lambda+1,
\qquad
T:=10^m,
\qquad
N:=10^M.
\tag{2.1}

由 source product：

\[
\boxed{
g=\frac{5^{3\lambda}+1587c_u}{\theta}.}
\tag{2.2}

真实 third denominator：

\[
\boxed{
b_3
=2^{3\lambda+2}\cdot5\cdot1587c_u.}
\tag{2.3}

并有

\[
\boxed{D=\frac{gT}{5^\lambda}=5\cdot2^m g.}
\tag{2.4}

Hensel quotient由

\[
\boxed{
\omega=\frac{\theta+L_*}{1587}}
\tag{2.5}

唯一恢复。真实 candidate必须使右边为整数。

---

## 3. `a_3` 由 full canonical CRT唯一恢复

前述 three-way CRT使用模数

\[
2^m,
\qquad
5^{\lambda-1},
\qquad
1587.
\]

其 full modulus为

\[
\mathfrak M_3^\sharp
=1587\frac T{25}.
\]

固定 `(lambda,c_u,theta,iota,c_-,c_+)` 后得到 shifted representative

\[
H_{3,\sharp}
\in[0,\mathfrak M_3^\sharp).
\]

只有

\[
\boxed{
0<H_{3,\sharp}<\frac T{250}}
\tag{3.1}

才可能进入真实 third-numerator digit window；若成立，则

\[
\boxed{a_3=T+H_{3,\sharp}.}
\tag{3.2}

所以 `a_3` 不再存在第二个 integer choice。

---

## 4. high-2 equality唯一恢复 `a_2`

当前 high-2 equality为

\[
H_0+Y_2=\frac{g^2}{2},
\qquad
Y_2=5c_Qa_2,
\qquad c_Q=1587.
\tag{4.1}

另一方面 pure third-block Gaussian norm已证明

\[
(g-2a_3)^2+81b_3^2
=4(H_0-ga_3).
\tag{4.2}

消去 `H_0`：

\[
\boxed{
a_2
=\frac{g^2-4a_3^2-81b_3^2}{20\cdot1587}.}
\tag{4.3}

因此 candidate首先必须满足 numerator被 `20*1587` 整除，并且

\[
\boxed{
\frac{249}{250}10^{M-1}<a_2<10^{M-1}.}
\tag{4.4}

---

## 5. `b_2,q,z,f` 全部恢复

reflection denominator formula给

\[
\boxed{
b_2=2^{M+m+1}c_ug.}
\tag{5.1}

危险 endpoint要求

\[
\boxed{
\frac1{10}10^M<b_2<\frac2{19}10^M.}
\tag{5.2}

令

\[
Q:=b_2+2N.
\]
则

\[
\boxed{
q=\frac{Q}{2^{M+1}1587}.}
\tag{5.3}

必须为正整数且

\[
23\nmid q.
\]

然后

\[
\boxed{z=q5^\lambda,}
\qquad
\boxed{f=z+2c_u.}
\tag{5.4}

source triangle的最终 exact audit为

\[
\boxed{g\omega=z+c_u.}
\tag{5.5}

---

## 6. finite defect `C` 无搜索恢复

定义

\[
\mathcal N_*:=(g-2a_3)^2+81b_3^2.
\]

pure third-block norm给

\[
\boxed{
C
=\frac{3gT-\mathcal N_*/4}{5^\lambda}.}
\tag{6.1}

candidate必须满足：

\[
C\in\mathbb Z,
\]

\[
\boxed{0<C<\frac{3D}{250}.}
\tag{6.2}

并且

\[
\boxed{\gcd(C,D)=1.}
\tag{6.3}

因此 `C` 同样不再需要 CRT 搜索；full `a_3` representative一旦通过，`C` 是确定值。

---

## 7. canonical `X,Y` 也唯一恢复

finite-defect relation

\[
c_-^2X=3D-C
\]
直接给

\[
\boxed{X=\frac{3D-C}{c_-^2}.}
\tag{7.1}

必须为正整数。

令

\[
\boxed{
H_0:=\frac{g^2}{2}-5\cdot1587a_2.}
\tag{7.2}

则另一 canonical factor

\[
H_0+ga_3=c_+^2Y
\]
给

\[
\boxed{
Y=\frac{H_0+ga_3}{c_+^2}.}
\tag{7.3}

也必须为正整数。

同时做 exact consistency audit：

\[
\boxed{H_0-ga_3=5^\lambda c_-^2X,}
\tag{7.4-}

\[
\boxed{H_0+ga_3=c_+^2Y.}
\tag{7.4+}

以及

\[
N_0:=\left(\frac{9b_2}{2}\right)^2+a_2^2,
\]

\[
\boxed{N_0=5^{\lambda-2}XY.}
\tag{7.5}

---

## 8. primitive audits

真实 endpoint还要求至少：

\[
\boxed{\gcd(a_2,b_2)=1,}
\tag{8.1}

\[
\boxed{\gcd(a_3,b_3)=1.}
\tag{8.2}

以及 source/canonical separations

\[
\gcd(g,c_u)=1,
\qquad
\gcd(g,1587)=1,
\qquad
\gcd(XY,1587)=1.
\tag{8.3}

这些都是 candidate恢复后的普通整数 gcd 检查。

---

## 9. fixed `23` common depth直接读取

定义

\[
K:=9N+10a_2,
\]

\[
D_{\rm pref}
:=2025b_2^2+81N^2-K^2.
\tag{9.1}

再定义

\[
A_K:=K^2-18K+55,
\qquad
E_K:=K(2K-9),
\]

\[
\mathcal G_+
:=fA_K+2c_uE_K,
\]

\[
\mathcal G_-
:=zA_K-2c_uE_K.
\tag{9.2}

若 `23^2|c_+`，选 `G_+`；若 `23^2|c_-`，选 `G_-`。当前 cap 为

\[
2v_{23}(c_Q)=4.
\]

所以 actual pure-`c_Q` common depth为

\[
\boxed{
 d_{23}
=\min\left(
 v_{23}(D_{\rm pref}),
 v_{23}(\mathcal G_\sigma),
 4
\right).}
\tag{9.3}

这允许 finite certificate直接给每个 surviving arithmetic candidate标注 odd/even depth，无需再回到 Hensel chart。

---

## 10. deterministic certificate 的意义

从 `(lambda,c_u,theta,iota,c_-,c_+)` 开始，整个剩余 endpoint现在只有以下一种流程：

\[
\theta
\to g,b_3
\to a_3\text{ (full CRT)}
\to a_2,b_2,C,X,Y,q,\omega
\to d_{23}.
\]

每个箭头都是单值的 exact integer formula。

因此后续任何 finite search都不应重新枚举 `a_2,a_3,b_2,b_3,C,X,Y`。真正的搜索变量只剩 source divisor `theta`、两种 Gaussian orientation和 fixed `23` orientation下至多两个 `3`-allocations。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-source-content-depth-ladder"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-source-content-depth-ladder.md`

# A2 fixed `23` `eta=2` `c=2` 的 source-content depth ladder

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-blowup-nogo.md`、`spontaneous-cq-fixed23-eta2-c2-source-content-mod23.md`、`spontaneous-cq-fixed23-eta2-c2-source-window.md`。
>
> **严格状态：**唯一 `c=2` type `(d,c_Q,k_h,slot)=(1,1587,1,+)` 已有 local 三变量 blow-up no-go。本文把真实 global relation `q_2=3*2^(2lambda+1) q` 与 `rho=q5^lambda/c_u` 直接代入 high-2 equation，把第三个 correction coordinate从自由 `q_2` 改成真实 source content `c_u`。得到的 normalized `(K,rho,c_u)` Jacobian仍为 unit，因此对每个 genuine orientation存在唯一 finite Hensel source-content branch：common depth `>=2,>=3,>=4` 分别强迫 `c_u` 落在唯一的 `mod 23,23^2,23^3` residue。与真实 source window / prime support联立后得到严格高度阶梯
> \[
> d_{23}\ge2\Rightarrow\lambda\ge63,
> \qquad
> d_{23}\ge3\Rightarrow\lambda\ge96,
> \qquad
> d_{23}=4\Rightarrow\lambda\ge129.
> \]
> 在 `lambda=96`，若 depth 能达到 `3`，canonical orientation 必须是 `23^2|c_-` 且 `c_u=533221`。这些条件均为必要条件；residue 命中本身不保证真实 arithmetic state 达到相应深度。

---

## 1. unique type 与真实 `q_2` coordinate

固定

\[
p:=23,
\qquad
c_Q=3p^2=1587,
\]

\[
M=2\lambda,
\qquad
m=\lambda+1,
\qquad
T=10^m,
\qquad
N=10^M.
\tag{1.1}

定义

\[
\rho:=\frac{q5^\lambda}{c_u},
\qquad
q_2:=\frac Q{p^2}.
\]

由真实 denominator relation

\[
Q=2^{M+1}c_Qq
\]
得到 exact `23`-adic identity

\[
\boxed{
q_2=\chi_\lambda\rho c_u,
\qquad
\chi_\lambda:=3\cdot2^{2\lambda+1}5^{-\lambda}
\in\mathbf Z_{23}^\times.}
\tag{1.2}

这里 `5^{-lambda}` 在 `Z_23` 中读取；它是 unit。

因此 blow-up proof 中看似独立的 `q_2` correction，在真实 arithmetic orbit上由 `(rho,c_u)` 唯一给出。

---

## 2. high-2 equation 改写成 source-content equation

沿用

\[
B=p^2q_2-2N,
\qquad
A=\frac{K-9N}{10}.
\tag{2.1}

`spontaneous-cq-fixed23-eta2-c2-blowup-nogo.md` 已给 finite-order high-2 bridges：

### minus canonical orientation `p^2||c_-`

\[
15B^2\rho^2
-2BKT^2q_2
-2p^2AT^2q_2^2
\equiv0\pmod{p^4}.
\tag{2.2-}

### plus canonical orientation `p^2||c_+`

\[
15B^2\rho^2(\rho+2)
-2B\rho KT^2q_2
-2p^2AT^2q_2^2(\rho+2)
\equiv0\pmod{p^4}.
\tag{2.2+}

代入 (1.2)。因为 `rho` 在两个 genuine orientations 中均为 unit，minus 可除去一份 `rho`，plus 可除去 `rho^2`。得到 analytic source-content forms：

\[
\boxed{
\begin{aligned}
\mathscr H_-
={}&15B^2\rho
-2BKT^2\chi_\lambda c_u\\
&-2p^2AT^2\chi_\lambda^2\rho c_u^2
\equiv0\pmod{p^4},
\end{aligned}}
\tag{2.3-}

\[
\boxed{
\begin{aligned}
\mathscr H_+
={}&15B^2(\rho+2)
-2BKT^2\chi_\lambda c_u\\
&-2p^2AT^2\chi_\lambda^2c_u^2(\rho+2)
\equiv0\pmod{p^4}.
\end{aligned}}
\tag{2.3+}

其中现在

\[
B=p^2\chi_\lambda\rho c_u-2N.
\tag{2.4}

所以 high-2 constraint 的第三个真实变量已经是 `c_u`。

---

## 3. normalized global Jacobian 仍为 unit

写

\[
K=16+p\kappa,
\qquad
N^2=16+ph_N.
\]

prefix 与 additive 的第一 normalized equations 为

\[
\boxed{F_1=16h_N+22-9\kappa,}
\tag{3.1}

\[
\boxed{F_{2,+}=\rho(1+14\kappa)+11,}
\tag{3.2+}

\[
\boxed{F_{2,-}=\rho(1+14\kappa)-9-18\kappa.}
\tag{3.2-}

而 (2.3) 降模 `p`，使用

\[
N\equiv4,
\quad
T^2\equiv9,
\quad
K\equiv16,
\quad
B\equiv15
\pmod p,
\]
后，乘去一个固定 unit，可分别写成

\[
\boxed{F_{3,-}=\rho-16\chi_\lambda c_u,}
\tag{3.3-}

\[
\boxed{F_{3,+}=\rho+2-16\chi_\lambda c_u.}
\tag{3.3+}

因此在 correction variables

\[
(\kappa,\rho,c_u)
\]
上，Jacobian 的三个 transverse diagonal entries 是

\[
-9,
\qquad
1+14\kappa,
\qquad
-16\chi_\lambda.
\]

故

\[
\boxed{
\det J_{\rm src}
=144\chi_\lambda(1+14\kappa).}
\tag{3.4}

`chi_lambda` 永远是 unit；genuine second-layer root 已排除 `kappa=18`，所以

\[
\boxed{\det J_{\rm src}\in\mathbf F_{23}^\times.}
\tag{3.5}

这给出 finite Hensel uniqueness：在 common-depth cap `4` 内，每升一层都会唯一固定 `c_u` 的下一位 `23`-adic digit。

---

## 4. canonical source-content branch

对固定 `lambda` 与 orientation `sigma in {-,+}`，若 `kappa` 为 `11` 或 `18`，selected additive gate 已在第一层停止，因此不定义 deeper branch。

其余情形定义三个唯一 residues

\[
C_{1,\sigma}(\lambda)\pmod p,
\]

\[
C_{2,\sigma}(\lambda)\pmod{p^2},
\]

\[
C_{3,\sigma}(\lambda)\pmod{p^3}
\]
为 §3 的 finite Hensel branch 的前三个 source-content truncations。

逻辑方向为

\[
\boxed{
d_{23}\ge2
\Longrightarrow
c_u\equiv C_{1,\sigma}(\lambda)\pmod p,}
\tag{4.1}

\[
\boxed{
d_{23}\ge3
\Longrightarrow
c_u\equiv C_{2,\sigma}(\lambda)\pmod{p^2},}
\tag{4.2}

\[
\boxed{
d_{23}\ge4
\Longrightarrow
c_u\equiv C_{3,\sigma}(\lambda)\pmod{p^3}.}
\tag{4.3}

反向命题不在本文声称范围内：一个 residue 命中只说明这一 source-content gate没有排除相应深度；真实 `K,rho` 仍须来自完整 decimal reconstruction。

---

## 5. 首批 height residues

当前 height lattice 为

\[
\lambda\equiv8\pmod{11}.
\]

exact checker 对 (2.2)–(3.3) 做逐位提升，得到：

\[
\boxed{
\begin{array}{c|c|ccc|ccc}
\lambda&\kappa
&C_{1,-}&C_{2,-}&C_{3,-}
&C_{1,+}&C_{2,+}&C_{3,+}\\ \hline
52&2&11&425&8360&12&288&11926\\
63&15&15&84&2200&8&192&1779\\
74&5&22&367&3012&1&300&7706\\
85&18&\multicolumn{3}{c|}{d_{23}=1}&\multicolumn{3}{c}{d_{23}=1}\\
96&8&12&518&3163&11&471&5232\\
107&21&20&411&5701&3&486&4189\\
118&11&\multicolumn{3}{c|}{d_{23}=1}&\multicolumn{3}{c}{d_{23}=1}\\
129&1&13&335&7741&10&148&11257
\end{array}}
\tag{5.1}

其中

\[
0\le C_1<23,
\quad
0\le C_2<529,
\quad
0\le C_3<12167.
\]

`C_1` 行与 `spontaneous-cq-fixed23-eta2-c2-source-content-mod23.md` 完全一致；`C_2,C_3` 是本文新增的 higher-depth global source-content filters。

---

# I. depth `>=2` 的高度下界

## 6. `d_23>=2` 强迫 `lambda>=63`

source-window proof 已严格给

\[
\lambda\ge52.
\]

在 `lambda=52` 唯一 source content 为

\[
c_u=29.
\]
而

\[
29\equiv6\pmod{23},
\]
与 (5.1) 的

\[
C_{1,-}=11,
\qquad
C_{1,+}=12
\]
均不相同。因此

\[
\boxed{\lambda=52\Longrightarrow d_{23}=1.}
\tag{6.1}

所以

\[
\boxed{d_{23}\ge2\Longrightarrow\lambda\ge63.}
\tag{6.2}

该 bound 对当前 filters 是 sharp 的：`lambda=63` 的 source window留下 `c_u=337`，且

\[
337\equiv15=C_{1,-}\pmod{23}.
\]
因此 minus orientation 的 second-layer source-content gate在 `lambda=63` 不再排除。

---

# II. depth `>=3` 的高度下界

## 7. `lambda=63,74,85` 都不能达到 depth `3`

### `lambda=63`

唯一 source content 为

\[
c_u=337.
\]
plus orientation 已在 `mod23` 失败。minus orientation虽然满足

\[
337\equiv15\pmod{23},
\]
但

\[
337\not\equiv84\pmod{529}=C_{2,-}(63).
\]
故

\[
\boxed{\lambda=63\Longrightarrow d_{23}<3.}
\tag{7.1}

### `lambda=74`

source support只留下

\[
c_u\in\{3917,3929\}.
\]
二者在第一层已同时违反两种 orientation 的 `C_1` 条件，所以

\[
\boxed{\lambda=74\Longrightarrow d_{23}=1.}
\tag{7.2}

### `lambda=85`

此时

\[
\kappa=18,
\]
additive gate强迫

\[
\boxed{d_{23}=1.}
\tag{7.3}

因此任何 depth `>=3` state 必有

\[
\lambda\ge96.
\]

---

## 8. `lambda=96` 的 depth-3 source content 唯一

source real window为

\[
\boxed{530249\le c_u\le534049.}
\tag{8.1}

### minus orientation

`d_23>=3` 要求

\[
c_u\equiv518\pmod{529}.
\]
区间内只有七个 representatives：

\[
530576,531105,531634,532163,532692,533221,533750.
\]

source content必须为奇数，且每个素因子都为 `1 mod4`，并且 `5` 不整除。逐项检查后唯一 survivor 是

\[
\boxed{533221=13\cdot41017,}
\tag{8.2}

其中两素因子均为 `1 mod4`。

### plus orientation

`d_23>=3` 要求

\[
c_u\equiv471\pmod{529}.
\]
区间内 representatives 为

\[
530529,531058,531587,532116,532645,533174,533703.
\]

它们分别被 `3`、偶性、`3 mod4`、偶性、`5`、偶性、`3` 排除，没有合法 source content。

因此

\[
\boxed{
d_{23}\ge3
\Longrightarrow
\lambda\ge96.}
\tag{8.3}

并且等号情形被压成

\[
\boxed{
\lambda=96,
\quad23^2\mid c_-,
\quad c_u=533221.}
\tag{8.4}

这里仍只声明 depth-3 的必要 source state；(8.4) 不保证真实 reconstructed candidate 存在或真的达到 depth `3`。

---

# III. full saturation `d_23=4` 的高度下界

## 9. `lambda=96` 不可能达到 depth `4`

minus orientation 的 depth-4 residue为

\[
C_{3,-}(96)=3163\pmod{12167},
\]
plus 为

\[
C_{3,+}(96)=5232\pmod{12167}.
\]

但 source interval (8.1) 的长度只有 `3801<12167`，而 exact representative check显示两种 residue在该 interval中都没有整数代表。因此

\[
\boxed{\lambda=96\Longrightarrow d_{23}<4.}
\tag{9.1}

---

## 10. `lambda=107` 的全部 depth-4 representatives违反 source support

source interval为

\[
\boxed{6172910\le c_u\le6217159.}
\tag{10.1}

### minus orientation

要求

\[
c_u\equiv5701\pmod{12167}.
\]
区间内只有

\[
6174370,
6186537,
6198704,
6210871.
\]

前三个分别含偶/`5`、`3`/`7`、偶因子；最后一个满足

\[
6210871=59\cdot105269
\]
且 `59=3 mod4`。所以全部不合法。

### plus orientation

要求

\[
c_u\equiv4189\pmod{12167}.
\]
区间内只有

\[
6185025,
6197192,
6209359.
\]

前两个分别含 `3,5` 与偶因子；最后一个

\[
6209359=13\cdot67\cdot7129
\]
含 `67=3 mod4`。同样全部不合法。

故

\[
\boxed{\lambda=107\Longrightarrow d_{23}<4.}
\tag{10.2}

---

## 11. `lambda=118` 已在第一层停止

此时

\[
\kappa=11,
\]
所以

\[
\boxed{d_{23}=1.}
\tag{11.1}

结合 §§9–11 与此前更低高度结果：

\[
\boxed{
d_{23}\ge4
\Longrightarrow
\lambda\ge129.}
\tag{11.2}

因为 cap 为 `4`，也可写成

\[
\boxed{d_{23}=4\Longrightarrow\lambda\ge129.}
\tag{11.3}

---

## 12. `lambda=129` 说明该 filter 到此达到边界

`lambda=129` 的 depth-4 residues为

\[
C_{3,-}=7741,
\qquad
C_{3,+}=11257
\pmod{12167}.
\]

source interval已经包含满足这些 congruences且满足 source prime support 的整数。例如 minus orientation 有

\[
\boxed{
836610661
=617\cdot1355933,}
\tag{12.1}

其中 `617` 与 `1355933` 都是 `1 mod4` primes；plus orientation有

\[
\boxed{836760181,}
\tag{12.2}

它本身为 `1 mod4` prime。

所以 source-window + `23^3` residue + prime-support 这套 filters 无法把 saturation height继续统一推到 `lambda>129`。更高 closure 必须使用 source divisor `theta`、full `a_3` CRT representative 或 deterministic reconstruction。

---

## 13. 更新后的 fixed-23 depth ledger

当前唯一 `c=2` type 的 source-content hierarchy为

\[
\boxed{
\begin{array}{c|c}
\text{desired common depth}&\text{necessary height/source consequence}\\ \hline
\ge2&\lambda\ge63\\
\ge3&\lambda\ge96;\ \lambda=96\Rightarrow(c_-,c_u=533221)\\
4&\lambda\ge129
\end{array}}
\tag{13.1}

它把 `spontaneous-cq-fixed23-eta2-c2-source-content-mod23.md` 的 single-digit filter扩展到了完整 square cap。

后续不应继续把 `q_2` 当作独立 local correction来枚举；对真实 arithmetic orbit，最规范的 `23`-adic source coordinate是本文的唯一 `c_u` finite-Hensel branch。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-source-content-mod23"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-source-content-mod23.md`

# A2 fixed `23` `eta=2` `c=2` 的 high-2 / source-content `mod 23` synchronization

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-blowup-nogo.md`、`spontaneous-cq-fixed23-eta2-c2-source-window.md`、`spontaneous-cq-relative-depth-nogo.md`。
>
> **严格状态：**c=2 high-2 blow-up将 normalized denominator `q_2=Q/23^2` 当作局部 correction coordinate，这足以证明 local system smooth；真实 arithmetic orbit还满足 exact coordinate relation `q_2=3*2^(2lambda+1)q` 与 `rho=q5^lambda/c_u`。本文把这条 global relation代回 high-2 bridge，得到 orientation-specific 的 `c_u mod23` **second-layer survival 必要条件**。若真实 state 已进入 fixed-23 first layer但不满足该 residue，则 common depth严格停在 `1`；这并不排除 arithmetic state。低高度中，`lambda=52` 与 `lambda=74` 在两种 orientation 下都强迫 `d_23=1`，`lambda=63` 的 plus orientation强迫 `d_23=1`，minus orientation才可能继续进入第二层。这是 high-2 equality提供的新增 global synchronization，不属于此前 source-tail quotient shadow。

---

## 1. global relation between `q_2` and `rho`

固定

\[
p:=23,
\qquad
c_Q=3p^2,
\qquad
M=2\lambda.
\]

定义

\[
q_2:=\frac Q{p^2}.
\]
由真实 denominator formula

\[
Q=2^{M+1}c_Qq
\]
精确得到

\[
\boxed{
q_2=3\cdot2^{2\lambda+1}q.}
\tag{1.1}

source ratio为

\[
\boxed{
\rho:=\frac{q5^\lambda}{c_u}.}
\tag{1.2}

所以模 `p`：

\[
\boxed{
q_2
\equiv
3\cdot2^{2\lambda+1}\rho c_u5^{-\lambda}
\pmod p.}
\tag{1.3}

这里 `rho,c_u,5` 都是 `p`-进 units。

---

## 2. high-2 bridge直接固定 second-layer 的 `c_u mod23`

c=2 high-2 blow-up 已证明：

### `c_-` orientation

\[
\boxed{\rho^2=16q_2\pmod p.}
\tag{2.1-}

代入 (1.3)：

\[
\rho^2
\equiv
48\cdot2^{2\lambda+1}\rho c_u5^{-\lambda}.
\]
因为

\[
48\equiv2\pmod{23},
\]
并约去 unit `rho`：

\[
\boxed{
\rho
\equiv
2^{2\lambda+2}c_u5^{-\lambda}
\pmod{23}.}
\tag{2.2-}

### `c_+` orientation

\[
\boxed{\rho(\rho+2)=16q_2\pmod p.}
\tag{2.1+}

同理约去 `rho`：

\[
\boxed{
\rho+2
\equiv
2^{2\lambda+2}c_u5^{-\lambda}
\pmod{23}.}
\tag{2.2+}

因此真实 high-2 state并不能任意选择 blow-up coordinate `q_2`；若 common depth想从第一层继续到第二层，它必须同时落在由 source content固定的 global orbit上。

---

## 3. 与 additive Möbius chart 联立

second-layer prefix已由 decimal length固定

\[
\kappa=\kappa(\lambda)\pmod{23}.
\]
若

\[
\kappa\notin\{11,18\},
\]
additive gate唯一给

\[
\boxed{
\rho_+(\kappa)
=-\frac{11}{1+14\kappa},}
\tag{3.1+}

\[
\boxed{
\rho_-(\kappa)
=\frac{9+18\kappa}{1+14\kappa}.}
\tag{3.1-}

将其代入 (2.2±)，得到 common depth `>=2` 的 source-content 必要 residue：

### plus / `23^2|c_+`

\[
\boxed{
c_u
\equiv
5^\lambda2^{-2\lambda-2}
\left(\rho_+(\kappa)+2\right)
\pmod{23}.}
\tag{3.2+}

也可写成

\[
\boxed{
c_u
\equiv
5^\lambda2^{-2\lambda-2}
\frac{5\kappa-9}{1+14\kappa}
\pmod{23}.}
\tag{3.3+}

### minus / `23^2|c_-`

\[
\boxed{
c_u
\equiv
5^\lambda2^{-2\lambda-2}
\rho_-(\kappa)
\pmod{23},}
\tag{3.2-}

即

\[
\boxed{
c_u
\equiv
5^\lambda2^{-2\lambda-2}
\frac{9+18\kappa}{1+14\kappa}
\pmod{23}.}
\tag{3.3-}

所以

\[
\boxed{
\text{若 first-layer state 不满足对应 (3.2)，则 }d_{23}=1.}
\tag{3.4}

满足 (3.2) 只说明 second-layer survival **尚未被这条 global gate排除**；它不能单独推出 `d_23>=2`。

---

## 4. periodicity

已有

\[
\lambda\equiv8\pmod{11}.
\]
又

\[
\operatorname{ord}_{23}(2)=11,
\qquad
\operatorname{ord}_{23}(5)=22.
\]
所以 `2^(2lambda+2)` 在整个 height lattice上固定，而 `5^lambda` 随 `lambda -> lambda+11` 改变符号。

另一方面 `kappa` 由

\[
M=2\lambda=16+22j
\]
中的 `j mod23` 决定。因此完整 residue pattern 对

\[
\lambda\mapsto\lambda+506
\]
周期化；在 `lambda=8 mod11` 的序列中等价于 `46` 个 `j`-steps 周期。

特殊 classes

\[
\kappa=18\Longleftrightarrow\lambda\equiv85\pmod{253},
\]

\[
\kappa=11\Longleftrightarrow\lambda\equiv118\pmod{253}
\]
已经由 additive gate直接强迫 `d_23=1`，不进入本文 second-layer source-content gate。

---

## 5. low-height depth ledger

source-window proof已给最初 source-content possibilities：

\[
(\lambda,c_u)
=(52,29),
(63,337),
(74,3917),
(74,3929).
\]
下面所有结论都只讨论 fixed-23 common depth；不宣称 arithmetic state本身不存在。

### `lambda=52`

prefix给

\[
\kappa=2.
\]
(3.2±) exact 计算为

\[
\boxed{c_u\equiv12\pmod{23}\quad(c_+),}
\]

\[
\boxed{c_u\equiv11\pmod{23}\quad(c_-).}
\]
但

\[
29\equiv6\pmod{23}.
\]
两种 canonical orientation都不能进入 second layer。因此若该 arithmetic state存在：

\[
\boxed{\lambda=52\Longrightarrow d_{23}=1.}
\tag{5.1}

这是 orientation-independent odd-depth certification。

### `lambda=63`

\[
\kappa=15.
\]
所需 residue为

\[
\boxed{c_u\equiv8\pmod{23}\quad(c_+),}
\]

\[
\boxed{c_u\equiv15\pmod{23}\quad(c_-).}
\]
而

\[
337\equiv15\pmod{23}.
\]
所以：

\[
\boxed{
23^2\mid c_+
\Longrightarrow d_{23}=1,}
\tag{5.2+}

而

\[
\boxed{
23^2\mid c_-
\Longrightarrow
\text{second-layer survival仍可能发生}.}
\tag{5.2-}

后者不是 `d_23>=2` 的充分条件；仍需检查真实下一 correction。

### `lambda=74`

\[
\kappa=5.
\]
所需 residue为

\[
\boxed{c_u\equiv1\pmod{23}\quad(c_+),}
\]

\[
\boxed{c_u\equiv22\pmod{23}\quad(c_-).}
\]
而

\[
3917\equiv7,
\qquad
3929\equiv19
\pmod{23}.
\]
两个 source contents在两种 orientations 下都不能进入 second layer。因此若 arithmetic state存在：

\[
\boxed{\lambda=74\Longrightarrow d_{23}=1.}
\tag{5.3}

同样是 orientation-independent odd-depth certification。

---

## 6. updated low-height parity ledger

source real window仍给

\[
\lambda\ge52.
\]
结合本文与旧 `kappa=11,18` certification，最初四个 relevant heights的 fixed-23 ledger为

\[
\boxed{
\begin{array}{c|c}
\lambda&\text{fixed-23 conclusion if an arithmetic state exists}\\ \hline
52&d_{23}=1\\
63&c_+:d_{23}=1;\quad c_-:\text{may deepen}\\
74&d_{23}=1\\
85&d_{23}=1\quad(\kappa=18)
\end{array}}
\tag{6.1}

所以 `52,74,85` 已经在 pure-23 parity ledger 中完全结算为 odd depth；只有 `lambda=63` 的 minus orientation在这些最低层中仍需要 deeper-depth audit。

---

## 7. proof boundary

(3.2±) 是一个真正 global condition，因为它同时使用：

1. real denominator coordinate `q_2=Q/23^2`；
2. source ratio `rho=q5^lambda/c_u`；
3. high-2 equality；
4. additive orientation gate。

它不是 `theta/omega` quotient identity的重写。

逻辑方向必须保持为：

\[
\boxed{d_{23}\ge2\Longrightarrow c_u\text{ 满足对应 residue}.}
\]

其逆命题未证明。后续 higher-depth source-content Hensel branch应沿同一方向使用：每升一层都会进一步固定 `c_u` 的 `23`-adic digits；某一层 residue失败时，才可在“前一层已进入”的条件下判定 common depth精确停止。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`

# A2 fixed `23` `eta=2` `c=2` 的 source-only divisor / CRT certificate

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-a3-crt-representative.md`、`spontaneous-cq-fixed23-eta2-c2-source-window.md`、`endpoint-lattice.md` §9。
>
> **严格状态：**前一文件把 third numerator压成每个 source state / Gaussian orientation至多一个 CRT representative。本文进一步消去 source variable `g`：source Hensel product把候选参数化为 `S_lambda(c_u)=5^(3lambda)+1587c_u` 的一个窄区间奇因子 `theta`，而 binary/5-adic 两个 `a_3` residues都可只用 `(lambda,c_u,theta)` 表示。因此最后的 `c=2` type 已被改写成 source-only divisor certificate；对固定 `(lambda,c_u)`，只需检查 `S_lambda(c_u)` 在 `(19L_*,20L_*)` 中的奇因子及至多两个 Gaussian orientations。本文不证明该 divisor interval 对所有高度为空。

---

## 1. source product 与 Hensel slot

当前 type 满足

\[
M=2\lambda,
\qquad
m=\lambda+1,
\qquad
c_Q=1587.
\]

source Hensel identity 为

\[
\boxed{
g\theta
=5^{M+\lambda}+c_Qc_u
=5^{3\lambda}+1587c_u.}
\tag{1.1}

定义 source integer

\[
\boxed{
\mathscr S_\lambda(c_u)
:=5^{3\lambda}+1587c_u.}
\tag{1.2}

所以

\[
\boxed{g\theta=\mathscr S_\lambda(c_u).}
\tag{1.3}

`endpoint-lattice.md` §9 对危险 `(a,k)=(9,2)` core 已证明

\[
19L_*<\theta<20L_*,
\tag{1.4}

其中

\[
L_*:=2^m5^\lambda c_u.
\]
当前 `m=lambda+1`，故

\[
\boxed{
L_*=2^{\lambda+1}5^\lambda c_u.}
\tag{1.5}

并且 `theta` 为正奇整数。因此任何真实候选必须先提供

\[
\boxed{
\theta\mid\mathscr S_\lambda(c_u),
\qquad
\theta\text{ odd},
\qquad
19L_*<\theta<20L_*.}
\tag{1.6}

一旦 `theta` 选定，

\[
\boxed{
g=\frac{\mathscr S_\lambda(c_u)}{\theta}}
\tag{1.7}

唯一恢复。于是 `(g,theta)` 不再是两维自由。

---

## 2. binary `a_3` root 只依赖 `(lambda,c_u,theta)`

前一文件的 binary polynomial 是

\[
F_2(a)
=
\theta\left(\frac{g^2}{4}+a^2\right)
-1587c_u a.
\tag{2.1}

由于 `theta` 为奇数，而 (1.3) 的全部二进 content进入 `g`，当前 `g` 被 `4` 整除。将 (1.7) 代入即可把 (2.1) 完全视为

\[
\boxed{
F_{2,\lambda,c_u,\theta}(a)
\in\mathbb Z/2^m\mathbb Z.}
\tag{2.2}

前一文件已证明

\[
F_2'(a)=2\theta a-1587c_u
\]
恒为奇数，所以存在唯一 root

\[
\boxed{
a_{3,(2)}(\lambda,c_u,\theta)
\pmod{2^m}.}
\tag{2.3}

因此 binary side不再需要额外枚举 `g`。

---

## 3. Gaussian `5`-residue 也可消去 `g`

固定 long Gaussian orientation，令

\[
\iota:=\iota_{\lambda-1},
\qquad
\iota^2\equiv-1\pmod{5^{\lambda-1}}.
\]

前一文件有

\[
a_{3,(5)}
\equiv
\frac{g-9\iota b_3}{2}
\pmod{5^{\lambda-1}}.
\tag{3.1}

source product (1.3) 模 `5^{lambda-1}` 时，`5^{3lambda}` 消失：

\[
g\theta
\equiv1587c_u
\pmod{5^{\lambda-1}}.
\]
`theta` 是 `5`-进 unit，所以

\[
\boxed{
g
\equiv1587c_u\theta^{-1}
\pmod{5^{\lambda-1}}.}
\tag{3.2}

另一方面当前 denominator exact formula为

\[
b_3
=2^{3\lambda+2}\cdot5\cdot1587c_u.
\tag{3.3}

代入 (3.1)：

\[
\boxed{
a_{3,(5)}
\equiv
\frac{1587c_u}{2}
\left(
\theta^{-1}
-45\iota\,2^{3\lambda+2}
\right)
\pmod{5^{\lambda-1}}.}
\tag{3.4}

所以 long-5 residue 同样只依赖

\[
(\lambda,c_u,\theta,\iota).
\]
交换 Gaussian orientation只需把 `iota` 换成 `-iota`。

---

## 4. source-only CRT representative

定义

\[
A:=2^m=2^{\lambda+1},
\qquad
B:=5^{\lambda-1},
\]

\[
\mathfrak M_3:=AB=T/25.
\]

对每个满足 (1.6) 的 `theta` 和每个 Gaussian orientation `iota`：

1. 由 (2.3) 得唯一 `a_(2) mod A`；
2. 由 (3.4) 得唯一 `a_(5) mod B`；
3. CRT 得唯一
   \[
   R_3^{\rm CRT}(\lambda,c_u,\theta,\iota)
   \in[0,\mathfrak M_3).
   \]

前一文件已证明真实 third numerator存在的必要充分 representative 条件是

\[
\boxed{
0<R_3^{\rm CRT}
<\frac{\mathfrak M_3}{10}.}
\tag{4.1}

若成立，则

\[
\boxed{
a_3=T+R_3^{\rm CRT}.}
\tag{4.2}

因此对固定 `(lambda,c_u)`，third-block 搜索已完全变成：

\[
\boxed{
\theta\in
\operatorname{Div}(\mathscr S_\lambda(c_u))
\cap(19L_*,20L_*)
\quad\text{和至多两个 }\iota\text{ 的有限检查}.}
\tag{4.3}

---

## 5. normalized CRT-cell formulation

若希望避免直接构造一个 `T/25` 级别的大整数，可以使用标准 CRT coefficient。取

\[
r_2:=a_{3,(2)}\in[0,A),
\]

并定义

\[
\boxed{
\kappa_3
:=\operatorname{res}_{[0,B)}
\left((a_{3,(5)}-r_2)A^{-1}\right).}
\tag{5.1}

则

\[
R_3^{\rm CRT}=r_2+A\kappa_3.
\tag{5.2}

所以 (4.1) 等价于

\[
\boxed{
0<r_2+A\kappa_3<\frac{AB}{10}.}
\tag{5.3}

特别地必要条件为

\[
\boxed{\kappa_3<\frac B{10}.}
\tag{5.4}

这把 global representative test转成一个单纯的 `5^{lambda-1}` centered coefficient test：真实候选要求两个 local roots的 relative CRT coefficient进入最前面的 `10%` cell。

---

## 6. 与低 source-content window 联立

`spontaneous-cq-fixed23-eta2-c2-source-window.md` 已给最初 source states：

\[
(\lambda,c_u)
=(52,29),
(63,337),
(74,3917),
(74,3929),\ldots
\]

因此这些低层已经是完全有限的 certificate：对每一对 `(lambda,c_u)`，只需因式分解单个整数

\[
\mathscr S_\lambda(c_u)=5^{3\lambda}+1587c_u,
\]
取其 `(19L_*,20L_*)` 内奇因子，并检查 (5.3)。不再需要搜索 `g,a_3` 的大区间。

---

## 7. 更新后的 closure target

唯一 `c=2` type 当前可以规范地表述为：

\[
\boxed{
\exists\lambda\equiv8\pmod{11},\ c_u,\ \theta,\ \iota
}
\]
满足

\[
\boxed{
\begin{aligned}
&c_u\text{ obeys source-content window and prime support},\\
&\theta\mid5^{3\lambda}+1587c_u,\\
&19L_*<\theta<20L_*,\\
&0<R_3^{\rm CRT}(\lambda,c_u,\theta,\iota)<\mathfrak M_3/10.
\end{aligned}}
\tag{7.1}

这已经是 source-only divisor/natural-representative problem。后续若继续无界 closure，目标应是证明 (7.1) 为空，或证明其 solution强迫 fixed `23` common depth进入已知 odd class。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-source-window"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-source-window.md`

# A2 fixed `23` `eta=2` `c=2` 的 source-content 窄窗与高度下界

> **依赖：** `spontaneous-cq-fixed23-eta2-slots.md`、`endpoint-lattice.md` 的 `(a,k)=(9,2)` endpoint window、`core.md` 的 source split。
>
> **严格状态：**唯一 `c=2` type 满足 `M=2lambda,m=lambda+1,c_Q=1587`。本文把 third denominator 的真实十进制窗口直接代入 exact denominator formula，得到 `c_u` 的指数窄窗。结合 `lambda=8 mod11` 与 `c_u` 的素因子全部为 `1 mod4`，严格排除 `lambda<52` 的全部 length classes，并把 `lambda=52,63,74` 的 source content分别压成 `{29}`、`{337}`、`{3917,3929}`。本文是低高度有限压缩，不宣称无界 family关闭。

---

## 1. exact `w` formula

当前 type 为

\[
(d,c_Q,k_h,\varepsilon)
=(1,1587,1,+1),
\]

\[
M=2\lambda,
\qquad
m=\lambda+1.
\tag{1.1}

reflection third denominator为

\[
b_3
=2^{M+m+1}5^dc_Qc_u.
\]
代入 (1.1) 与 `d=1`：

\[
\boxed{
b_3
=2^{3\lambda+2}\cdot5\cdot1587\,c_u.}
\tag{1.2}

令

\[
w:=\frac{b_3}{10^m}.
\]
因为

\[
10^m=2^{\lambda+1}5^{\lambda+1},
\]
得到

\[
\boxed{
w
=3174\left(\frac45\right)^\lambda c_u.}
\tag{1.3}

---

## 2. endpoint window 给 `c_u` 的精确指数区间

危险 `(a,k)=(9,2)` endpoint 已有严格界

\[
\boxed{
\frac{837}{1000}<w<\frac{843}{1000}.}
\tag{2.1}

这里下界是已有更强 bound `42/sqrt(2515)` 的有理放宽。

由 (1.3)：

\[
\boxed{
\frac{837}{3174000}
\left(\frac54\right)^\lambda
<c_u<
\frac{843}{3174000}
\left(\frac54\right)^\lambda.}
\tag{2.2}

这是当前 type 的 source-content real window。

另一方面 fixed `23` / `eta=2` 已给

\[
M\equiv16\pmod{22}.
\]
结合 `M=2lambda`：

\[
\boxed{\lambda\equiv8\pmod{11}.}
\tag{2.3}

所以只需依次检查

\[
\lambda=8,19,30,41,52,\ldots
\]

---

## 3. `lambda<52` 全部排除

对 (2.2) 做 exact integer comparison：

### `lambda=8,19,30`

三者的 upper endpoint均小于 `1`，而

\[
c_u\in\mathbb Z_{>0}.
\]
故全部不可能。

### `lambda=41`

exact bounds 满足

\[
2<c_u<3.
\]
同样没有整数。

因此

\[
\boxed{\lambda\ge52.}
\tag{3.1}

于是

\[
\boxed{M=2\lambda\ge104,}
\qquad
\boxed{m=\lambda+1\ge53.}
\tag{3.2}

这把唯一 `c=2` type 的真实 decimal length 从原 `M>=16` 直接提高到 `M>=104`。

---

## 4. first surviving source contents

source split 的本原性已有：

\[
\boxed{
c_u\text{ 的每个奇素因子都 }\equiv1\pmod4,}
\tag{4.1}

并且

\[
5\nmid c_u.
\]
特别地

\[
c_u\equiv1\pmod4.
\tag{4.2}

### `lambda=52`

(2.2) 精确给

\[
28<c_u<30.
\]
唯一整数是

\[
\boxed{c_u=29.}
\tag{4.3}

且 `29=1 mod4`，合法于当前 source-content 筛选。

### `lambda=63`

精确区间满足

\[
336<c_u<339.
\]
其中唯一 `1 mod4` 整数是

\[
\boxed{c_u=337.}
\tag{4.4}

`337` 为素数且 `337=1 mod4`。

### `lambda=74`

(2.2) 给

\[
3912<c_u<3941.
\]
逐个检查该有限区间中所有正整数，并施加 (4.1)，只有

\[
\boxed{c_u\in\{3917,3929\}.}
\tag{4.5}

两者均为 `1 mod4` 素数。

所以最初三条可能的无界-height lattice state 被压成

\[
\boxed{
\begin{array}{c|c|c|c}
\lambda&M&m&c_u\\ \hline
52&104&53&29\\
63&126&64&337\\
74&148&75&3917\text{ or }3929
\end{array}}
\tag{4.6}

---

## 5. 与 fixed `23` depth ledger 的关系

当前 `c=2` blow-up proof 已证明：

\[
M\equiv170,236\pmod{506}
\Longrightarrow d_{23}=1.
\]

因为 `M=2lambda`，前两个对应

\[
\lambda=85,
\qquad
\lambda=118
\]
在 `lambda=8 mod11` 的序列中。

所以 source-content window 与 fixed-`23` depth table 可以共同使用：低层 `52,63,74` 需要进入新建的 `a_3` CRT representative test；`lambda=85` 无论 source content如何，`23`-common depth 已知恰为 `1`。

再次强调：`d_23=1` 是 odd-depth certification，不是 arithmetic state exclusion。

---

## 6. 更新后的 finite-height frontier

对于最后的 `(1,1587,1,+)` family，当前最小需要实际考虑的 source state 已不再从 `lambda=8` 开始，而是

\[
\boxed{(\lambda,c_u)=(52,29),(63,337),(74,3917),(74,3929),\ldots}
\]

每一个这样的 source state 再由
`spontaneous-cq-fixed23-eta2-c2-a3-crt-representative.md`
把 third numerator压到每个 Gaussian orientation至多一个 CRT representative。

因此低高度部分已经成为真正有限的 divisor/representative certificate；无界 closure仍需控制这些 representative 随 `lambda` 的行为。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-theta-p3-filter"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-theta-p3-filter.md`

# A2 fixed `23` `eta=2` `c=2` 的 source divisor `theta mod 23^3` filter

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-blowup-nogo.md`、`spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`、`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md`。
>
> **严格状态：**对 `v_23(c_Q)=2` 的 second-layer surviving classes，additive Möbius chart固定 `rho=z/c_u mod23`，而 source split固定 `g mod23`。本文把二者送回 exact identity `theta=c_Q omega-L_*`，得到 orientation-specific 的 `theta mod23^3` residue。于是 source divisor certificate 可在窄实区间之外再施加一个 `23^3` congruence。本文给出最初 source states 的显式 residue 表，但不声称这一个固定模数单独关闭无界 family。

---

## 1. notation

固定

\[
p:=23,
\qquad
c_Q=3p^2=1587,
\]

\[
M=2\lambda,
\qquad
m=\lambda+1,
\]

\[
L_*:=2^m5^\lambda c_u
=2^{\lambda+1}5^\lambda c_u.
\tag{1.1}

source ratio记

\[
\rho:=\frac z{c_u}.
\]

source triangle与 Hensel relation 为

\[
g\omega=z+c_u=c_u(\rho+1),
\tag{1.2}

\[
\boxed{
\theta=c_Q\omega-L_*
=3p^2\omega-L_*.}
\tag{1.3}

本文只处理 fixed `23` common depth已进入第二层的 genuine class；因此 `kappa notin {11,18}`，orientation-resolved additive chart给合法 unit `rho mod p`。

---

## 2. source split 固定 `g mod23`

reflection source split为

\[
\boxed{
c_Qq
=5^M+2^mgc_u.}
\tag{2.1}

左边被 `p^2` 整除。降模 `p` 已足够得到

\[
5^{2\lambda}
+2^{\lambda+1}gc_u
\equiv0\pmod p.
\]
因为 `2,5,c_u` 都是 `p`-进 units：

\[
\boxed{
g_0
\equiv
-5^{2\lambda}
(2^{\lambda+1}c_u)^{-1}
\pmod p.}
\tag{2.2}

所以 fixed `(lambda,c_u)` 已唯一固定 `g mod23`。

---

## 3. additive orientation 固定 `omega mod23`

second-layer additive charts为

\[
\boxed{
\rho_+(\kappa)
=-\frac{11}{1+14\kappa},}
\tag{3.1+}

\[
\boxed{
\rho_-(\kappa)
=\frac{9+18\kappa}{1+14\kappa}.}
\tag{3.1-}

其中 `+` 对应 canonical `c_+` orientation，`-` 对应 `c_-` orientation。

由 (1.2) 模 `p`：

\[
g_0\omega
\equiv c_u(\rho_\sigma+1)
\pmod p.
\]
故

\[
\boxed{
\omega_{0,\sigma}
\equiv
c_u(\rho_\sigma+1)g_0^{-1}
\pmod p.}
\tag{3.2}

将 (2.2) 的逆元显式代回，还可写成

\[
\boxed{
\omega_{0,\sigma}
\equiv
-2^{\lambda+1}c_u^2
(\rho_\sigma+1)
5^{-2\lambda}
\pmod p.}
\tag{3.3}

---

## 4. `theta` 自动提升到 `mod23^3`

由 exact (1.3)：

\[
\theta+L_*=3p^2\omega.
\]
要读取 `theta mod p^3`，右边只需要 `omega mod p`。因此 (3.2) 直接给

\[
\boxed{
\theta
\equiv
-L_*+3p^2\omega_{0,\sigma}
\pmod{p^3}.}
\tag{4.1}

也就是

\[
\boxed{
\theta
\equiv
-L_*
-3p^2\,2^{\lambda+1}c_u^2
(\rho_\sigma+1)5^{-2\lambda}
\pmod{p^3}.}
\tag{4.2}

这个 residue 已完全由

\[
(\lambda,c_u,\sigma)
\]
决定；`g,omega,q,a_3` 都已经消失。

若 `rho=-1`，则 `omega_0=0`，(4.1)退化成

\[
\theta\equiv-L_*\pmod{p^3},
\]
正好对应旧 simultaneous-gate class `p|omega`。

---

## 5. 与 source divisor certificate 合并

`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md` 已把 divisor window收紧为

\[
\frac{39}{2}L_*<\theta<\frac{79}{4}L_*.
\tag{5.1}

因此任何 second-layer surviving source divisor现在必须同时满足

\[
\boxed{
\begin{aligned}
&\theta\mid\mathscr S_\lambda(c_u),\\
&\theta\text{ odd},\\
&\frac{39}{2}L_*<\theta<\frac{79}{4}L_*,\\
&\theta\equiv\Theta_{\lambda,c_u,\sigma}\pmod{23^3},
\end{aligned}}
\tag{5.2}

其中 `Theta` 由 (4.1)/(4.2) 显式给出。

这比只用 `theta+L_* divisible c_Q=3*23^2` 多一层：旧 integrality只给 `theta=-L_* mod23^2`；当前 additive/source synchronization进一步固定 quotient `omega mod23`，从而升级到 `23^3`。

---

## 6. first source states 的 residue 表

使用 source-content proof 的

\[
(\lambda,c_u)
=(52,29),
(63,337),
(74,3917),
(74,3929)
\]
以及 fixed-23 blow-up 的 `kappa/rho` chart，可 exact 计算：

\[
\boxed{
\begin{array}{c|c|c|c}
\lambda&c_u&c_+\text{ orientation}&c_-\text{ orientation}\\ \hline
52&29&2713&6945\\
63&337&9053&3763\\
74&3917&731&202\\
74&3929&5444&10734
\end{array}
\quad(\bmod\ 23^3).}
\tag{6.1}

这些 `lambda` 对应的 `M=104,126,148` 都属于 c=2 second-layer surviving classes，因此两种 orientation chart均 genuine。

---

## 7. proof boundary

`23^3` 仍是 fixed modulus，所以本文不把它单独视为无界 closure。它的用途是强化 source-only finite certificate：

1. source window先给有限 `c_u`；
2. centered slot只查 `1.28%` 宽的 divisor interval；
3. (5.2) 再只保留一个 `23^3` residue class；
4. 最后对 surviving divisor做 `a_3` growing CRT representative test。

对低高度，这已经把 certificate 的搜索空间显著压缩；对无界高度仍需控制 divisor/CRT representative 的统一行为。

---

<a id="source-spontaneous-cq-fixed23-eta2-c2-three-primary-exclusion"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-c2-three-primary-exclusion.md`

# A2 fixed `23` `eta=2` `c=2` 的 `3`-primary angle exclusion

> **依赖：** `spontaneous-cq-fixed23-eta2-slots.md`、`spontaneous-angle-pair-q0-depth.md`、`primitive-reduction.md`。
>
> **严格状态：**唯一 `c=2` type 的 `c_Q=1587=3*23^2` 含一个奇指数 `3`-primary。此前 pure-`c_Q` generic depth law始终排除 `p=3`，所以这一因子必须单独审计。本文直接在真实 primitive angle integers上计算模 `3`，证明 `3` 根本不整除任一 angle sign。故 `3` 不进入 angle/additive common gcd，也不能作为该 type 的 inert odd-depth supplier。

---

## 1. primitive separation先给 `3 not divide a_2`

当前 reflection 有

\[
N_0=\left(\frac{9b_2}{2}\right)^2+a_2^2
=5^{\lambda-2}XY.
\tag{1.1}

canonical primitive separation给

\[
\gcd(XY,c_Q)=1.
\]
由于

\[
3\mid c_Q,
\qquad
3\ne5,
\]
得到

\[
3\nmid N_0.
\tag{1.2}

第一平方项显然被 `3^2` 整除，所以模 `3`：

\[
N_0\equiv a_2^2\pmod3.
\]
因此

\[
\boxed{3\nmid a_2.}
\tag{1.3}

记

\[
A:=a_2,
\qquad
B:=b_2,
\qquad
N:=10^M.
\]
于是 `A,N,T=10^m` 都是 `3`-进 units。

---

## 2. `Q`-contact固定 `B mod3`

当前

\[
Q=B+2N=2^{M+1}c_Qq.
\]
因为 `3|c_Q`：

\[
Q\equiv0\pmod3.
\]
故

\[
B\equiv-2N\equiv N\pmod3.
\tag{2.1}

特别地

\[
3\nmid B.
\]

---

## 3. exact angle core在模 `3` 下是 unit

真实 angle core为

\[
\mathcal U_\Omega
=(45B^2-2AN)^2
-A^2B(99B-4N).
\tag{3.1}

模 `3`：

\[
45\equiv99\equiv0,
\qquad
4\equiv1.
\]
所以

\[
\begin{aligned}
\mathcal U_\Omega
&\equiv
(-2AN)^2
-A^2B(-4N)\\
&\equiv
A^2N^2+A^2BN\\
&=A^2N(N+B)
\pmod3.
\end{aligned}
\tag{3.2}

由 (2.1)：

\[
N+B\equiv2N\equiv-N\pmod3.
\]
因此

\[
\boxed{
\mathcal U_\Omega
\equiv-A^2N^2
\not\equiv0
\pmod3.}
\tag{3.3}

---

## 4. 两个 angle signs 都是 `3`-进 units

真实 sign-pair angle integers为

\[
\mathcal O_\pm
=T\mathcal U_\Omega
\pm2A^2Qb_3.
\tag{4.1}

第二项含 `Q`，故被 `3` 整除。于是

\[
\mathcal O_\pm
\equiv T\mathcal U_\Omega
\pmod3.
\]
由 `3 not divide T` 与 (3.3)：

\[
\boxed{
3\nmid\mathcal O_+,
\qquad
3\nmid\mathcal O_-.}
\tag{4.2}

primitive normalization只除去 `2`-power，所以同样有

\[
\boxed{
3\nmid\widehat{\mathcal O}_+,
\qquad
3\nmid\widehat{\mathcal O}_-.}
\tag{4.3}

---

## 5. common gcd 中完全没有 `3`

无论 additive side 的 `3`-adic行为怎样，angle side已经是 unit。因此对任意包含 angle integer的 common gcd，特别是当前

\[
G_{\rm sp}
=\gcd(\widehat{\mathcal O}_+,\widehat{\mathcal T}_2),
\]
都有

\[
\boxed{v_3(G_{\rm sp})=0.}
\tag{5.1}

所以

\[
\boxed{
 c_Q=3\cdot23^2
\text{ 中的 odd }3\text{-primary 不贡献任何 common parity}.}
\tag{5.2}

这也说明 generic pure-`c_Q` 分析排除 `p=3` 没有遗漏一个潜在 closure shortcut；在最后的 `c=2` type中，真正开放的 pure-`c_Q` inert common prime仍是 fixed `23`。

---

## 6. 对 frontier 的影响

该 type 的 denominator square content从 mod-4 角度看含一个 `3`，但它在 angle primitive carrier中完全消失。因此后续 parity ledger不能使用 `c_Q=3 mod4` 本身推断 common gcd 的 parity。

剩余工作仍是：

1. fixed `23` 的 actual common depth；
2. source divisor / full canonical `a_3` representative；
3. reconstruction 后其它 residual prime pools的审计。

本文把唯一特殊 `p=3` loophole严格关闭。

---

<a id="source-spontaneous-cq-fixed23-eta2-slots"></a>

> 整合来源：`spontaneous-cq-fixed23-eta2-slots.md`

# A2 fixed `23` 在 `(a,k)=(9,2)` reflection `eta=2` high-2 lattice 的三型压缩

> **依赖：** `endpoint-lattice.md` §§16.1–16.7、`spontaneous-cq-relative-depth-nogo.md`、`spontaneous-cq-canonical-defect-overlap.md`。
>
> **严格状态：**本文把 pure-`c_Q` fixed prime `23` 放入 `endpoint-lattice.md` 的最危险 `(a,k)=(9,2)` reflection high-2 lattice，并固定 `eta:=2m-M=2`。利用已有 correlated endpoint interval、`23|c_Q`、high quotient 的 Gaussian norm support 与 `c_Q≡3 mod4`，把整个 `eta=2` fixed-`23` high-2 family 精确压成三个 `(d,c_Q,k_h,slot)` 类型。三型还统一满足 `M=16 mod22`。本文不排除这三个类型，因此不关闭 A2。

---

## 1. general fixed-`eta` slot equation

沿用 `endpoint-lattice.md`：

\[
\eta:=2m-M,
\qquad
d:=m-\lambda>0,
\]

\[
\chi:=1+\frac{H}{5^{M-1}},
\qquad
r:=\frac w\chi,
\qquad
\mathcal H:=3+\zeta-\frac CD.
\]

high-2 factor 取一侧

\[
H_0+\varepsilon Y_2=\frac{g^2k_h}{2},
\qquad
\varepsilon\in\{-1,+1\}.
\]

§16.2/16.7 的 scale equation 可统一写为

\[
\boxed{
K_{\eta,d}
:=
\frac{c_Qk_h5^{d-\eta-1}}{2^{\eta+2}}
=r(\mathcal H+\varepsilon yr).
}
\tag{1.1}

本文固定

\[
\boxed{\eta=2.}
\]

于是

\[
\boxed{
K_{2,d}
=\frac{c_Qk_h5^{d-3}}{16}.
}
\tag{1.2}

---

## 2. endpoint interval 的精确统一界

已有

\[
\frac45<r<\frac{843}{1000},
\]

\[
\frac{997}{250}<\mathcal H<\frac{1001}{250},
\qquad
\frac{249}{250}<y<1.
\tag{2.1}

对 minus slot

\[
K_-=r(\mathcal H-yr).
\]

在上述 rectangle 中，`K_-` 对 `r,mathcal H` 递增、对 `y` 递减，因此

\[
\boxed{
\frac{1594}{625}
<K_-
<\frac{666891399}{250000000}.
}
\tag{2.2-}

对 plus slot

\[
K_+=r(\mathcal H+yr).
\]

已有 §16.15 的 lower bound 与 §16.10 的 correlated upper bound：

\[
\boxed{
\frac{11962}{3125}
<K_+
<\frac{163}{40}.
}
\tag{2.2+}

这些界已经足够在 `eta=2` 上做完整整数筛选。

---

## 3. 把短实区间变成 `P=c_Qk_h` 的整数窗口

记

\[
P:=c_Qk_h.
\]

由 (1.2)，

\[
P=16\cdot5^{3-d}K_{2,d}.
\tag{3.1}

同时 fixed `23` 给

\[
23\mid c_Q
\Longrightarrow
23\mid P.
\tag{3.2}

`c_Q,k_h` 都为正奇数，并且 reflection 中都是 `5`-进单位，所以

\[
\boxed{P\text{ 为 odd }5\text{-unit 且 }23\mid P.}
\tag{3.3}

### `d=1`

minus window：

\[
1020.16<P<1067.026\ldots
\]

区间内仅有两个 `23` 的倍数

\[
1035,\qquad1058.
\]

前者被 `5` 整除，后者为偶数。因此

\[
\boxed{d=1,\ -\text{ slot 无解}.}
\tag{3.4-}

plus window：

\[
1531.136<P<1630.
\]

区间内 `23` 的倍数为

\[
1541,\ 1564,\ 1587,\ 1610.
\]

odd 5-unit 只剩

\[
\boxed{P\in\{1541,1587\}.}
\tag{3.4+}

### `d=2`

minus window：

\[
204.032<P<213.406,
\]
唯一 `23` 倍数是

\[
\boxed{P=207.}
\tag{3.5-}

plus window：

\[
306.2272<P<326,
\]
唯一 `23` 倍数是 `322`，为偶数。因此

\[
\boxed{d=2,\ +\text{ slot 无解}.}
\tag{3.5+}

### `d=3`

minus window落在

\[
40.8064<P<42.682,
\]
plus window落在

\[
61.2454<P<65.2.
\]

都没有 `23` 的倍数。

### `d>=4`

即使取 plus 的统一上界，

\[
P
<16\cdot5^{3-d}\frac{163}{40}
\le\frac{652}{50}<23,
\]
与 `23|P`, `P>0` 矛盾。

所以只需继续筛

\[
(d,slot,P)
=(1,+,1541),
(1,+,1587),
(2,-,207).
\tag{3.6}

---

## 4. Gaussian norm support 删除 `P=1541`

`endpoint-lattice.md` §16.7 已证明

\[
\boxed{\gcd(k_h,c_Q5^d)=1.}
\tag{4.1}

并且若

\[
r\mid k_h,
\qquad r\equiv3\pmod4,
\]
则只能有

\[
\boxed{r=3.}
\tag{4.2}

另外 core/source split 给

\[
\boxed{c_Q\equiv3\pmod4.}
\tag{4.3}

先看

\[
1541=23\cdot67.
\]

因为 `23|c_Q` 且 `(c_Q,k_h)=1`，只有两种 prime-power allocation：

1. `c_Q=23, k_h=67`；
2. `c_Q=1541, k_h=1`。

第一种违反 (4.2)，因为

\[
67\equiv3\pmod4,
\qquad67\ne3.
\]

第二种违反 (4.3)，因为

\[
1541\equiv1\pmod4.
\]

故

\[
\boxed{P=1541\text{ 被完全排除}.}
\tag{4.4}

---

## 5. 剩余两个 product 的完整 factor allocation

### `P=1587`

\[
1587=3\cdot23^2.
\]

因为 `23|c_Q` 且 `(c_Q,k_h)=1`，完整 `23^2` 必须进入 `c_Q`。prime `3` 只能完整进入其中一侧。

若

\[
c_Q=23^2=529,
\qquad k_h=3,
\]
则 `c_Q=1 mod4`，不合法。

唯一剩下

\[
\boxed{
(d,c_Q,k_h,slot)
=(1,1587,1,+).
}
\tag{5.1}

### `P=207`

\[
207=3^2\cdot23.
\]

同样由 `(c_Q,k_h)=1`，完整 `3^2` 只能进入一侧。因此两种合法 allocation 为

\[
\boxed{
(d,c_Q,k_h,slot)
=(2,23,9,-),
}
\tag{5.2a}

\[
\boxed{
(d,c_Q,k_h,slot)
=(2,207,1,-).
}
\tag{5.2b}

两者都满足 `c_Q=3 mod4`，且 `k_h` 的 `3 mod4` prime support只含允许的 `3`。

因此 `eta=2` fixed-`23` high-2 family 被完整压成

\[
\boxed{
\begin{array}{c|c|c|c}
d&c_Q&k_h&slot\\ \hline
1&1587&1&+\\
2&23&9&-\\
2&207&1&-
\end{array}}
\tag{5.3}

---

## 6. 三型统一进入 `M=16 mod22`

`eta=2` 定义给

\[
M=2m-2,
\]
所以

\[
\boxed{M\text{ 为偶数}.}
\tag{6.1}

fixed `23` angle first layer 已严格给出

\[
M\equiv5\text{ or }16\pmod{22}.
\tag{6.2}

第一类为奇数 residue，和 (6.1) 不相容。因此三型统一满足

\[
\boxed{M\equiv16\pmod{22}.}
\tag{6.3}

进一步，三型的 `M,lambda` 关系为：

- `(d,c_Q,k_h)=(1,1587,1)`：`m=lambda+1`，故
  \[
  \boxed{M=2\lambda.}
  \tag{6.4a}
  \]
- 两个 `d=2` 类型：`m=lambda+2`，故
  \[
  \boxed{M=2\lambda+2.}
  \tag{6.4b}
  \]

因此 fixed `23` 的 unbounded length 参数已经被放入两条精确 affine lattice。

---

## 7. 与 `eta<=1` 的现有结果合并

`endpoint-lattice.md` 已有：

- `eta=0` reflection high-2 allocation 全部排除；
- `eta=1` 最终只剩 (16.21) 的五型，其 `c_Q` 分别为
  \[
  3,103,159,7,31,
  \]
  均不被 `23` 整除。

所以 pure-`c_Q` fixed `23` 在当前 dangerous reflection high-2 core 中满足

\[
\boxed{
\eta\le1\Longrightarrow\text{无解},
}
\tag{7.1}

而

\[
\boxed{
\eta=2\Longrightarrow\text{只剩 (5.3) 三型}.}
\tag{7.2}

这是 fixed `23` 与 endpoint high-2 lattice 的第一次有限类型交叉压缩。

---

## 8. 更新后的 frontier

三个剩余类型已经足够具体，后续不应再研究 general `eta=2` real slots。下一步可以分别使用：

1. `(1,1587,1,+)` 中 `v_23(c_Q)=2`，直接接 `spontaneous-cq-canonical-defect-overlap.md` 的 `c>=2` `mod 506` length table；
2. `(2,23,9,-)` 与 `(2,207,1,-)` 都有 `v_23(c_Q)=1`，接 fixed-`23` normalized tail `q_1` / source-ratio Möbius compatibility；
3. 三型都满足 `M=16 mod22`，所以 decimal first-layer root统一为 `10^M=4 mod23`；
4. 再加入 canonical `C` residue 与 `C` 的 natural representative/CRT phase，目标已经是三个明确 lattice family，而非原无界参数空间。

---

<a id="source-spontaneous-cq-global-coupling"></a>

> 整合来源：`spontaneous-cq-global-coupling.md`

# A2 pure-`c_Q` 的 sphere 退化与双 orientation additive coupling

> **依赖：** `spontaneous-angle-pair-q0-depth.md`、`spontaneous-angle-pair-cq-nogo.md`、`height-cofactor.md`、`source-discriminant.md`、`primitive-reduction.md`。
>
> **严格状态：**本文修正上一版中的记号碰撞：decimal length `N_dec=10^M` 与 endpoint-lattice 中的 source quantity `N_src=3D-C=c_-^2X` 必须严格分离。修正后，pure-`c_Q` prime 按 canonical square allocation 分成 `c_-` 与 `c_+` 两个对称 orientation。退化 sphere 的两条线性 branch 仍精确等于 `omega(H_0-Y_3)` 与 `omega(H_0+Y_3)`；真正具有 `2v_p(c_Q)` square depth 的 branch 取决于该 prime 落在 `c_-` 还是 `c_+`。对应地 additive carrier 有两个对称 source-prefix gate `G_-`、`G_+`。二者的 ratio-degeneracy resultant 完全相同，均为 `-5060`；除固定 `23` length orbit 外，orientation-resolved first-layer system 都是 smooth。本文不证明 relative depth parity，因此不关闭 A2。

---

## 1. 记号与 pure-`c_Q` channel

为避免旧稿中 `N` 的重名，本文件固定

\[
N_{\rm dec}:=10^M,
\qquad T:=10^m,
\qquad A:=a_2,
\qquad B:=b_2,
\]

\[
Q=B+2N_{\rm dec}=2^{M+1}c_Qq,
\qquad
K=9N_{\rm dec}+10A,
\]

\[
N_0=\left(\frac{9B}{2}\right)^2+A^2.
\]

source notation 保持

\[
z:=q5^\lambda,
\qquad f:=z+2c_u,
\]

\[
H_0=c_uW_q,
\qquad Y_3=ga_3,
\qquad
TK+a_3=\omega W_q.
\]

`source-discriminant.md` 已证明

\[
\boxed{z=g\omega-c_u,\qquad f=g\omega+c_u}
\tag{1.1}
\]

以及 exact denominator ratio

\[
\boxed{b_3z=Tc_uQ.}
\tag{1.2}
\]

固定 genuine non-`3` inert prime

\[
p\equiv3\pmod4,
\qquad p\ne3,5,
\]

并假设

\[
\boxed{p^c\Vert c_Q,\qquad c\ge1,\qquad p\nmid q.}
\tag{1.3}
\]

由 `primitive-reduction.md` 与 canonical primitive separation：

\[
\boxed{p\nmid c_u gW_qXYN_{\rm dec}.}
\tag{1.4}
\]

这里 `p\nmid XY` 也可直接由

\[
N_0=5^{\nu_5}XY
\]
与 Gaussian norm

\[
N_0=(9B/2)^2+A^2
\]
推出：若 inert `p|N_0`，则 `p|A,B`，违背 `(A,B)=1`。

定义 decimal prefix defect

\[
\boxed{
D_{\rm pref}:=2025B^2+81N_{\rm dec}^2-K^2
=N_{\rm dec}^2\Delta_0.}
\tag{1.5}
\]

已有 pure-`c_Q` angle depth law

\[
\boxed{
\min\{v_p(\widehat{\mathcal O}_\pm),2c\}
=
\min\{v_p(D_{\rm pref}),2c\}.}
\tag{1.6}
\]

---

# I. `Q_0`-degenerate sphere

## 2. `x+2` 与 third denominator 的 exact ratio

令

\[
x=\frac{B}{N_{\rm dec}},
\qquad
s=\frac{K}{N_{\rm dec}},
\qquad
\nu=x+2=\frac{Q}{N_{\rm dec}},
\]

\[
\bar w=\frac{b_3}{TN_{\rm dec}},
\qquad
\bar\zeta=\frac{a_3}{TN_{\rm dec}},
\qquad
n=\frac{N_0}{N_{\rm dec}^2}.
\]

由 (1.2)：

\[
\boxed{z\bar w=c_u\nu.}
\tag{2.1}
\]

所以

\[
v_p(\nu)=v_p(\bar w)=c.
\]

generic cross-sign formula 中把 `(x+2)` 当 unit 后出现的负次幂，因此不能直接搬入 pure-`c_Q` channel。

exact normalized sphere 为

\[
\mathscr S
=x^2\bar w^2(s+\bar\zeta)^2
-(\nu+\bar w)^2
\left(n\bar w^2+x^2\bar\zeta^2\right)=0.
\tag{2.2}
\]

代入 `bar w=c_u nu/z` 并在 exact rational identity 中约去真实非零的 `nu^2`，得到

\[
\boxed{
\begin{aligned}
&x^2z^2
(c_us-z\bar\zeta)
(c_us+f\bar\zeta)\\
&\qquad=(z+c_u)^2nc_u^2\nu^2.
\end{aligned}}
\tag{2.3}
\]

因此 first layer `nu=0` 精确分裂成

\[
\boxed{c_us-z\bar\zeta=0}
\tag{2.4-}
\]

与

\[
\boxed{c_us+f\bar\zeta=0.}
\tag{2.4+}
\]

---

## 3. 两条线性 branch 是 canonical height factors

定义整数代表

\[
\boxed{
R_-:=Tc_uK-za_3,
\qquad
R_+:=Tc_uK+fa_3.}
\tag{3.1}
\]

由 (1.1) 与 `TK+a_3=omega W_q`：

\[
\boxed{R_-=\omega(H_0-Y_3),}
\tag{3.2-}
\]

\[
\boxed{R_+=\omega(H_0+Y_3).}
\tag{3.2+}
\]

canonical allocation 是

\[
\boxed{
H_0-Y_3=5^\lambda c_-^2X,
\qquad
H_0+Y_3=c_+^2Y,
\qquad
c_Q=c_-c_+.}
\tag{3.3}
\]

注意这里的 `c_-^2X` 是 endpoint-lattice 的 source quantity；它**不等于** `N_dec=10^M`。

`primitive-reduction.md` 已有

\[
\gcd(H_0,c_Q)=1.
\tag{3.4}
\]

所以一个 prime `p|c_Q` 不可能同时整除 `c_-` 与 `c_+`；否则 (3.3) 两式都会被 `p` 整除，从而 `p|H_0`，与 (3.4) 冲突。结合 `p\nmid XY`，pure-`c_Q` prime 恰好属于以下两个互斥 orientation 之一。

### minus orientation: `p^c || c_-`

\[
\boxed{
v_p(H_0-Y_3)=2c,
\qquad
v_p(H_0+Y_3)=0.}
\tag{3.5-}
\]

于是

\[
\boxed{v_p(R_-)\ge2c.}
\tag{3.6-}
\]

### plus orientation: `p^c || c_+`

\[
\boxed{
v_p(H_0+Y_3)=2c,
\qquad
v_p(H_0-Y_3)=0.}
\tag{3.5+}
\]

于是

\[
\boxed{v_p(R_+)\ge2c.}
\tag{3.6+}
\]

因此 sphere 的严格结论仍然是一个 no-go：它只告诉我们 pure-`c_Q` prime 被放进哪一个 canonical square orientation；对应 branch 的深度是偶数 `2c`，但它并不强迫 angle defect `D_pref` 的 unsaturated depth变偶。

---

# II. additive carrier 的双 orientation reduction

## 4. 先把 additive depth 降到 `S_0`

沿用

\[
\boxed{
\widehat{\mathcal T}_2
=2^mc_u^2g^2\mathscr S_0
-(c_Qq)^2 5^{2\lambda-d}XY,}
\tag{4.1}
\]

\[
\boxed{
\mathscr S_0
=T(K^2-26)-(2K-9)(2a_3+9T).}
\tag{4.2}
\]

由 (1.3)–(1.4)，第二项的 `p`-进赋值恰为 `2c`，第一项前系数为 unit，所以

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),2c\}
=
\min\{v_p(\mathscr S_0),2c\}.}
\tag{4.3}
\]

定义

\[
A_K:=K^2-18K+55,
\qquad
E_K:=K(2K-9),
\]

以及两个 orientation gate

\[
\boxed{
\mathcal G_+:=fA_K+2c_uE_K,}
\tag{4.4+}
\]

\[
\boxed{
\mathcal G_-:=zA_K-2c_uE_K.}
\tag{4.4-}
\]

直接展开得到一对 exact bridge：

\[
\boxed{
f\mathscr S_0
=T\mathcal G_+
-2(2K-9)R_+,}
\tag{4.5+}
\]

\[
\boxed{
z\mathscr S_0
=T\mathcal G_-
+2(2K-9)R_-.}
\tag{4.5-}
\]

若 prime 还进入 angle first layer，则由 `B=-2N_dec mod p` 与 `D_pref=0`：

\[
\boxed{K^2\equiv8181N_{\rm dec}^2\pmod p.}
\tag{4.6}
\]

由于 `8181=3^4*101` 且 `101=1 mod4`，genuine non-`3` inert `p` 上有

\[
p\nmid K.
\tag{4.7}
\]

在 plus orientation，若 `p|f`，则 (3.1) 给 `R_+ congruent Tc_uK mod p`，与 (3.6+) 矛盾；因此 `p\nmid f`。同理 minus orientation 有 `p\nmid z`。

于是：

### plus orientation

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),2c\}
=
\min\{v_p(\mathcal G_+),2c\}.}
\tag{4.8+}
\]

### minus orientation

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),2c\}
=
\min\{v_p(\mathcal G_-),2c\}.}
\tag{4.8-}
\]

这才是 pure-`c_Q` additive depth 的正确 orientation-resolved 形式。

---

## 5. corrected depth matrix

令

\[
G_{\rm sp}=\gcd(\widehat{\mathcal O}_+,\widehat{\mathcal T}_2).
\]

若 `p^c||c_+`：

\[
\boxed{
\min\{v_p(G_{\rm sp}),2c\}
=
\min\{v_p(D_{\rm pref}),v_p(\mathcal G_+),2c\}.}
\tag{5.1+}
\]

若 `p^c||c_-`：

\[
\boxed{
\min\{v_p(G_{\rm sp}),2c\}
=
\min\{v_p(D_{\rm pref}),v_p(\mathcal G_-),2c\}.}
\tag{5.1-}
\]

因此旧版本中的单一 `G_{c_Q}` 必须替换成由 canonical square allocation 选择的 `G_+` 或 `G_-`。

---

# III. 两个 orientation 具有同一个 first-layer degeneracy

## 6. source ratio form

写

\[
\rho:=\frac z{c_u}.
\]

定义

\[
C_+(K):=3K^2-27K+55,
\qquad
C_-(K):=-K(2K-9).
\tag{6.1}
\]

则

\[
\boxed{
\frac{\mathcal G_+}{c_u}
=\rho A_K+2C_+(K),}
\tag{6.2+}
\]

\[
\boxed{
\frac{\mathcal G_-}{c_u}
=\rho A_K+2C_-(K).}
\tag{6.2-}
\]

只要 `A_K` 是 unit，两侧都唯一固定 source ratio

\[
\rho=-\frac{2C_\pm(K)}{A_K}.
\tag{6.3}
\]

---

## 7. 两边的 ratio-degenerate resultant 完全相同

直接计算

\[
\boxed{
\operatorname{Res}_K(A_K,2C_+)
=\operatorname{Res}_K(A_K,2K(2K-9))
=-5060.}
\tag{7.1}
\]

并且

\[
-5060=-2^2\cdot5\cdot11\cdot23.
\]

对 genuine non-`3` inert prime只需看 `11,23`。两种 orientation 的共同根都相同：

\[
p=11:\quad K=0,
\]

\[
p=23:\quad K=16.
\]

`p=11` 与 (4.6) 冲突，因为 `8181=8 mod11` 且 `N_dec` 为 unit，所以被删除。

`p=23` 时 (4.6) 给

\[
N_{\rm dec}^2=16\pmod{23}.
\]

`10` 在 `F_23^*` 的阶为 `22`，故

\[
\boxed{M=5\text{ or }16\pmod{22}.}
\tag{7.2}
\]

这是两个 orientation 共同的唯一 ratio-degenerate length orbit。

---

## 8. generic first layer 均 smooth

把 angle equation记为

\[
F(K,N_{\rm dec})=K^2-8181N_{\rm dec}^2.
\]

任一 orientation 的 additive equation记为

\[
G_\pm(K,\rho)=\rho A_K+2C_\pm(K).
\]

对变量 `(K,rho)`，Jacobian determinant 为

\[
\boxed{
J_\pm=2K\,A_K.}
\tag{8.1}
\]

由 (4.7) 及 §7：

\[
\boxed{p\ne23\Longrightarrow J_\pm\ne0\pmod p.}
\tag{8.2}
\]

所以除固定 `23` length orbit 外，两种 pure-`c_Q` orientation 的 first-layer common root 都是二维 smooth root；高阶只能沿唯一 coupled Hensel lift传播。

---

# IV. 两个 additive gates 的 pair identities

## 9. sum / difference 完全因子化

两个 gate 还满足

\[
\boxed{
\mathcal G_+-\mathcal G_-
=2c_u(5K^2-36K+55),}
\tag{9.1}
\]

\[
\boxed{
\mathcal G_++\mathcal G_-
=2(z+c_u)(K^2-18K+55)
=2g\omega A_K.}
\tag{9.2}
\]

其中

\[
5K^2-36K+55=(K-5)(5K-11).
\tag{9.3}
\]

所以 `G_+` 与 `G_-` 不是两套无关 polynomial；它们是一对围绕 fixed split quadratic `F_W(K)` 与 content factor `g omega A_K` 的 companion gates。后续若要做 global `c_- / c_+` parity allocation，应使用 (9.1)–(9.2)，而不能把两 orientation 当成独立 supplier 重复收费。

---

## 10. 更新后的 frontier

修正后的 pure-`c_Q` 开放核是：

1. 每个 inert `p|c_Q` 先由 canonical factor equality 唯一选择 `c_-` 或 `c_+` orientation；
2. angle depth 仍由 `D_pref` 读取；
3. additive depth分别由 `G_-` 或 `G_+` 读取；
4. 两 orientation 的 first-layer bad set 完全一致，只剩固定 `23`, `M=5,16 mod22`；
5. generic roots 均 smooth，因此局部 discriminant / singular-prime hunting再次降级；
6. 真正剩余的是 orientation-resolved relative-depth synchronization，以及利用 (9.1)–(9.2) 把 `c_- / c_+` 的 global parity allocation 接回同一 companion pair。

本文的旧单-gate版本因 `N` 记号碰撞已被本版完全替换。

---

<a id="source-spontaneous-cq-relative-depth-nogo"></a>

> 整合来源：`spontaneous-cq-relative-depth-nogo.md`

# A2 pure-`c_Q` relative-depth no-go 与 fixed `23` blow-up chart

> **依赖：** `spontaneous-cq-global-coupling.md`、`spontaneous-angle-pair-cq-nogo.md`、`source-discriminant.md`。
>
> **严格状态：**本文保留 generic `p\ne23` 的 relative-derivative no-go，并修正上一版对 fixed `23` 的逻辑解释：`23^2` lift 失败并不删除真实 state；在 residual-parity 问题中它恰好意味着 common depth 停在 `1`，因此是潜在 odd supplier。修正后，fixed `23` 的二阶层得到完整 depth-1 / depth-2 dichotomy。两个 orientation 的 normalized additive gate 都是 Möbius chart；除去已有的 source unit 边界 `rho=0,-2` 后，它们都双射于同一个 21 元 unit torus。若二阶 common lift 真正发生，blow-up Jacobian 立即恢复为 unit，因此 fixed `23` 也不存在无界 singular Hensel tree。本文没有证明 odd depth 不出现；相反，它精确识别了哪些 normalized states 强迫 depth `1`。A2 仍未关闭。

---

## 1. orientation-resolved exact system

沿用

\[
N:=N_{\rm dec}=10^M,
\qquad
D_{\rm pref}=2025B^2+81N^2-K^2,
\]

\[
A_K:=K^2-18K+55,
\qquad
E_K:=K(2K-9),
\]

\[
C_+(K):=3K^2-27K+55,
\qquad
C_-(K):=-E_K.
\]

写 source ratio

\[
\boxed{\rho:=\frac z{c_u}=\frac{q5^\lambda}{c_u}.}
\tag{1.1}
\]

因为 pure-`c_Q` prime满足 `p\nmid q5c_u`，总有

\[
\boxed{\rho\in\mathbf Z_p^\times.}
\tag{1.2}
\]

`spontaneous-cq-global-coupling.md` 已证明，在 canonical orientation
`\sigma\in\{+,-\}` 中 additive gate可写成

\[
\boxed{
g_\sigma(K,\rho)
:=\frac{\mathcal G_\sigma}{c_u}
=\rho A_K+2C_\sigma(K).}
\tag{1.3}
\]

若

\[
p^c\Vert c_Q,
\qquad p\nmid q,
\]
则 actual angle/additive common depth 的 `2c` 截断为

\[
\boxed{
\min\{v_p(G_{\rm sp}),2c\}
=
\min\{v_p(D_{\rm pref}),v_p(g_\sigma),2c\}.}
\tag{1.4}
\]

---

# I. generic derivative route is a strict no-go

## 2. exact Jacobian

把 background integers `B,N` 固定，视

\[
F_1(K,\rho):=D_{\rm pref},
\qquad
F_2(K,\rho):=g_\sigma(K,\rho).
\]

则

\[
\partial_KF_1=-2K,
\qquad
\partial_\rho F_1=0,
\qquad
\partial_\rho F_2=A_K.
\]

所以

\[
\boxed{
\det\frac{\partial(F_1,F_2)}{\partial(K,\rho)}
=-2KA_K.}
\tag{2.1}
\]

保留 integer gate `\mathcal G_\sigma` 时只多一个 unit `c_u`：

\[
\boxed{J_\sigma=-2c_uKA_K.}
\tag{2.2}
\]

angle first layer给

\[
K^2\equiv8181N^2\pmod p,
\]
所以 genuine non-`3` inert prime上 `K` 是 unit。

若同时 `A_K=C_\sigma=0`，两个 orientation 的 resultant 都是

\[
\boxed{
\operatorname{Res}_K(A_K,2C_\sigma)
=-5060=-2^2\cdot5\cdot11\cdot23.}
\tag{2.3}
\]

`p=11` 的共同根为 `K=0`，与 angle root 冲突。因此

\[
\boxed{p\ne23\Longrightarrow J_\sigma\in\mathbf Z_p^\times.}
\tag{2.4}
\]

于是 generic `p\ne23` 上，逐层提高 `D_pref` 与 `g_sigma` 只需普通二维 Hensel correction。局部 derivative 不会强迫 valuation 差为偶：

\[
\boxed{
\text{generic relative-depth derivative route 是严格 no-go。}}
\tag{2.5}
\]

---

# II. fixed `23`: first blow-up

## 3. first-layer data

唯一 Jacobian-degenerate genuine prime为

\[
\boxed{p=23.}
\]

两种 orientation 都有

\[
\boxed{K\equiv16\pmod{23}.}
\tag{3.1}
\]

angle equation又给

\[
8181\equiv16\pmod{23},
\qquad
N^2\equiv16\pmod{23},
\]
所以

\[
\boxed{M\equiv5\text{ or }16\pmod{22}.}
\tag{3.2}
\]

写

\[
K=16+23\kappa,
\qquad
N^2=16+23h_N,
\qquad
Q=B+2N=23q_1.
\tag{3.3}
\]

若 `v_23(c_Q)\ge2`，则 `q_1\equiv0\pmod{23}`；若 `v_23(c_Q)=1`，则 `q_1` 是 unit。

---

## 4. normalized prefix equation

有 exact identity

\[
\boxed{
D_{\rm pref}
=8181N^2-K^2+2025Q(Q-4N).}
\tag{4.1}
\]

因为

\[
8181=16+23\cdot355,
\qquad
2025\equiv1\pmod{23},
\]
除以 `23` 并模 `23` 得

\[
\boxed{
\delta_D:=\frac{D_{\rm pref}}{23}
\equiv
16h_N+22-9\kappa-4Nq_1
\pmod{23}.}
\tag{4.2}
\]

其中

\[
N\equiv19\quad(M=5\bmod22),
\qquad
N\equiv4\quad(M=16\bmod22).
\tag{4.3}
\]

所以 prefix depth 至少 `2` 当且仅当

\[
\boxed{
9\kappa
\equiv16h_N+22-4Nq_1
\pmod{23}.}
\tag{4.4}
\]

并且 blow-up coordinate中的 transverse derivative为

\[
\boxed{\partial_\kappa\delta_D\equiv-9\not\equiv0\pmod{23}.}
\tag{4.5}
\]

---

## 5. normalized additive equations

在 `K=16`：

\[
A_K=23,
\qquad
C_+(16)=17\cdot23,
\qquad
E_K(16)=16\cdot23.
\]

且

\[
A_K'(16)=14,
\qquad
C_+'(16)=69,
\qquad
E_K'(16)=55.
\]

于是

\[
\boxed{
\delta_+:=\frac{g_+}{23}
\equiv\rho(1+14\kappa)+11
\pmod{23},}
\tag{5.1+}
\]

\[
\boxed{
\delta_-:=\frac{g_-}{23}
\equiv\rho(1+14\kappa)-9-18\kappa
\pmod{23}.}
\tag{5.1-}
\]

因此 common depth 至少 `2` 还要求 `delta_sigma=0`。

---

# III. 修正后的 depth interpretation

## 6. `不能 lift` 意味着 depth `1`，不是 state 矛盾

设

\[
d_{23}:=\min\{v_{23}(D_{\rm pref}),v_{23}(g_\sigma),2c\}.
\]

first layer已经保证

\[
d_{23}\ge1.
\]

由 (4.2)、(5.1)：

\[
\boxed{
 d_{23}=1
\iff
\delta_D\ne0
\text{ 或 }
\delta_\sigma\ne0.}
\tag{6.1}
\]

而

\[
\boxed{
 d_{23}\ge2
\iff
\delta_D=\delta_\sigma=0.}
\tag{6.2}
\]

特别地若 `c=1`，cap 正好为 `2`，所以

\[
\boxed{
\begin{array}{c|c}
(\delta_D,\delta_\sigma)\ne(0,0)&d_{23}=1\quad\text{(odd)}\\
(\delta_D,\delta_\sigma)=(0,0)&d_{23}=2\quad\text{(even)}.
\end{array}}
\tag{6.3}
\]

因此上一版把 `kappa=18` 称为“删除 state”是错误解释；正确结论是该 correction 使 additive depth停在第一层，从而**强迫 common depth 为 `1`**。

---

## 7. 两个 orientation 的 unit boundaries

source 本原性总给

\[
\boxed{\rho\ne0\pmod{23}.}
\tag{7.1}
\]

在 `c_+` orientation 中，高深度 branch 是

\[
R_+=Tc_uK+fa_3,
\qquad f=c_u(\rho+2).
\]

`R_+` 具有至少 `2c` 深度，而 `T,c_u,K,a_3` 都是 genuine units。若 `rho=-2`，则 `f=0 mod23`，从而

\[
R_+\equiv Tc_uK\ne0\pmod{23},
\]
矛盾。因此

\[
\boxed{c_+\text{ orientation}:\quad \rho\ne0,-2.}
\tag{7.2+}
\]

在 `c_-` orientation 中只需使用 `rho\ne0`；稍后可见其 Möbius image 本身永远取不到 `-2`。

---

# IV. fixed `23` additive chart 是 Möbius parametrization

## 8. plus orientation

若 `1+14kappa` 为 unit，则 `delta_+=0` 唯一给

\[
\boxed{
\rho_+(\kappa)
=-\frac{11}{1+14\kappa}.}
\tag{8.1+}
\]

特殊点：

- `kappa=18` 时 denominator 为 `0`，而常数 `11` 非零，所以 `delta_+\ne0`；
- `kappa=11` 时
  \[
  \rho_+(11)=-2,
  \]
  与 (7.2+) 冲突。

所以 second-layer additive lift 的 genuine domain 为

\[
\boxed{
\kappa\in\mathbf F_{23}\setminus\{11,18\}.}
\tag{8.2+}

反解 (8.1+)：

\[
\boxed{
\kappa
=-\frac{\rho+11}{14\rho}.}
\tag{8.3+}

因此

\[
\boxed{
\rho_+:
\mathbf F_{23}\setminus\{11,18\}
\xrightarrow{\sim}
\mathbf F_{23}^{\times}\setminus\{-2\}.}
\tag{8.4+}

---

## 9. minus orientation

`delta_-=0` 给

\[
\boxed{
\rho_-(\kappa)
=\frac{9+18\kappa}{1+14\kappa}.}
\tag{9.1-}

特殊点：

- `kappa=18` 仍是 projective pole，并且常数项非零；
- `kappa=11` 时 numerator 为 `0`，所以唯一可能是 `rho=0`，与 (7.1) 冲突；
- 方程 `rho_-=-2` 化为 `11=0 mod23`，因此无解。

反解为

\[
\boxed{
\kappa
=\frac{9-\rho}{14\rho-18}.}
\tag{9.2-}

所以同样有

\[
\boxed{
\rho_-:
\mathbf F_{23}\setminus\{11,18\}
\xrightarrow{\sim}
\mathbf F_{23}^{\times}\setminus\{-2\}.}
\tag{9.3-}

这说明两个 orientation 的二阶 additive geometry 完全相同：它们只是对同一个 source-unit torus 使用不同坐标。

---

## 10. `kappa=11,18` 的正确结论

由 §§8–9：

\[
\boxed{
\kappa\in\{11,18\}
\Longrightarrow
\delta_\sigma\ne0
\quad\text{for both orientations}.}
\tag{10.1}
\]

因此无论 prefix 是否继续提升，

\[
\boxed{
\kappa\in\{11,18\}
\Longrightarrow
d_{23}=1.}
\tag{10.2}
\]

这是一条**odd-depth certification**，不是状态排除。

---

# V. second blow-up 立即恢复 smoothness

## 11. normalized Jacobian

现在假设真正进入 depth `>=2` locus：

\[
\delta_D=\delta_\sigma=0.
\]

那么由 genuine domain

\[
\kappa\notin\{11,18\},
\]
尤其

\[
1+14\kappa\ne0.
\]

在 blow-up variables `(kappa,rho)` 上，normalized system 的 Jacobian 是三角形：

\[
\partial_\kappa\delta_D=-9,
\qquad
\partial_\rho\delta_\sigma=1+14\kappa.
\]

故

\[
\boxed{
J_{23}^{\rm blow}
=-9(1+14\kappa)
\in\mathbf F_{23}^{\times}.}
\tag{11.1}

因此 fixed `23` 的 singularity 只存在于第一层。一次 blow-up 后，只要 depth `2` compatibility 成立，后续又回到普通 unique Hensel lift：

\[
\boxed{
\text{fixed }23\text{ 没有 surviving unbounded singular tree。}}
\tag{11.2}

这同样不能推出 valuation parity；它只证明继续做更高阶 singular-discriminant hunting 不会产生新 obstruction。

---

# VI. decimal-length specialization

## 12. `M mod 506`

有

\[
\boxed{\operatorname{ord}_{23^2}(10)=506,}
\tag{12.1}
\]

\[
\boxed{10^{22}\equiv1+8\cdot23\pmod{23^2}.}
\tag{12.2}
\]

写

\[
M=M_0+22j,
\qquad0\le j<23,
\qquad M_0\in\{5,16\}.
\]

则

\[
\boxed{h_N\equiv h_0+3j\pmod{23},}
\tag{12.3}
\]

其中

\[
\boxed{M_0=5:\ h_0=15,
\qquad
M_0=16:\ h_0=5.}
\tag{12.4}
\]

若 `v_23(c_Q)\ge2`，则 `q_1=0`。此时 prefix depth `>=2` 唯一要求

\[
\kappa=9^{-1}(16h_N+22).
\]

四个 length classes 恰好命中 `kappa=11` 或 `18`：

\[
\boxed{
M\equiv170,236,423,489\pmod{506}.}
\tag{12.5}
\]

其对应为

\[
\begin{array}{c|c}
M\bmod506&\kappa\\ \hline
170&18\\
236&11\\
423&18\\
489&11.
\end{array}
\tag{12.6}

所以若 `v_23(c_Q)\ge2` 且 first-layer common contact 存在，则在这四个 length classes 中：

- 若 `D_pref` 不提升，common depth 已是 `1`；
- 若 `D_pref` 提升，则 `kappa` 被迫为 `11/18`，additive side 不提升。

统一得到

\[
\boxed{
M\equiv170,236,423,489\pmod{506},\quad
v_{23}(c_Q)\ge2
\Longrightarrow d_{23}=1.}
\tag{12.7}

再次强调：这是对 odd supplier 的精确识别，不是对全局 state 的排除。

---

# VII. source normalization

## 13. `q_1` 与 `rho` 的 exact global bridge

令

\[
h:=v_{23}(c_Q),
\qquad
\widetilde Q:=\frac{Q}{23^h},
\qquad
\widetilde c:=\frac{c_Qc_u}{23^h}.
\]

由

\[
Q=2^{M+1}c_Qq,
\qquad
\rho=\frac{q5^\lambda}{c_u},
\]
直接得到 exact identity

\[
\boxed{
5^\lambda\widetilde Q
=2^{M+1}\rho\widetilde c.}
\tag{13.1}

这只是 `b_3z=Tc_uQ` 的 normalized 版本，因此本身不是新 obstruction；它的作用是把 second-layer source ratio翻译回真实 tail factor。

特别地若 `h=1`，则 `widetilde Q=q_1`，记

\[
\gamma:=\frac{c_Qc_u}{23}.
\]
则

\[
\boxed{
\gamma\rho
=\frac{5^\lambda q_1}{2^{M+1}}.}
\tag{13.2}

若 common depth `>=2`，代入 Möbius charts 得

### plus

\[
\boxed{
\gamma
\equiv
-\frac{5^\lambda q_1}{2^{M+1}}
\frac{1+14\kappa}{11}
\pmod{23}.}
\tag{13.3+}

### minus

\[
\boxed{
\gamma
\equiv
\frac{5^\lambda q_1}{2^{M+1}}
\frac{1+14\kappa}{9+18\kappa}
\pmod{23}.}
\tag{13.3-}

所以 `h=1` 的真正 global synchronization 已经可以写成

\[
\boxed{
\kappa_{\rm pref}(M,q_1)
=\kappa_\sigma(\rho)
}
\tag{13.4}

或者等价地写成 normalized tail congruence (13.3)。目前尚无独立 relation 固定 `gamma mod23`，所以不能把 (13.3) 宣称为 contradiction。

---

## 14. 更新后的 frontier

本轮修正并严格得到：

1. generic `p\ne23` 的 local derivative route 是 no-go；
2. fixed `23` 的 common depth 第一层总至少为 `1`；
3. `kappa=11,18` 强迫 common depth恰为 `1`，它们是 odd-depth states，不是被删除的 states；
4. 对其余 `kappa`，两个 orientation 都只是
   \[
   \mathbf F_{23}\setminus\{11,18\}
   \leftrightarrow
   \mathbf F_{23}^\times\setminus\{-2\}
   \]
   的 Möbius parametrization；
5. 一旦 depth `2` compatibility 成立，blow-up Jacobian 立刻恢复为 unit，所以没有新的 singular tree；
6. `v_23(c_Q)\ge2` 时，四个 length classes
   \[
   M\equiv170,236,423,489\pmod{506}
   \]
   自动把 common depth固定在 `1`；
7. `v_23(c_Q)=1` 时，剩余开放核是 exact global synchronization
   \[
   \kappa_{\rm pref}(M,q_1)=\kappa_\sigma(\rho),
   \]
   并可用 normalized tail `gamma=(c_Qc_u)/23` 改写。

因此下一步不应继续做 fixed-`23` 的局部高阶展开。真正可增加信息的方向只剩：

\[
\boxed{
\text{用 tail/source 的独立全局等式限制 }\gamma\text{ 或 }\rho,
\text{再与 }\kappa_{\rm pref}\text{ 比较。}}
\]

---

<a id="source-spontaneous-cq-source-tail-nogo"></a>

> 整合来源：`spontaneous-cq-source-tail-nogo.md`

# A2 pure-`c_Q` fixed-`23` 的 source/tail Hensel quotient no-go

> **依赖：** `core.md` §§12.5–12.7、`source-discriminant.md`、`spontaneous-cq-relative-depth-nogo.md`。
>
> **严格状态：**`spontaneous-cq-relative-depth-nogo.md` 已把 fixed `23` 的 depth `>=2` compatibility 压成 prefix correction `kappa` 与 source ratio `rho=z/c_u` 的同步，并把 `v_23(c_Q)=1` 写成 normalized tail `gamma=(c_Qc_u)/23` 的同余。本文检查最自然的下一步：是否能使用 core 的 Hensel quotients `omega,theta` 再独立固定 `gamma` 或 `rho`。结论是否定的。reflection 下，`theta` 方程与 `c_Q omega-theta` 方程都由 source split 与 source triangle 精确推出；normalized `23` tail bridge也只是 denominator-ratio identity 的重写。因此 source/tail quotient 层没有新的独立 mod-`23` obstruction。后续必须引入 canonical factor allocation、finite-defect/rational-root 或其他 natural representative。

---

## 1. reflection source identities

固定当前 reflection endpoint，使用不会与 source ratio 混淆的记号

\[
D_0:=2^m g.
\]

core/source split 为

\[
\boxed{
c_Qq=5^M+D_0c_u.}
\tag{1.1}

`source-discriminant.md` 的 source triangle 等价于

\[
\boxed{
g\omega=5^\lambda q+c_u.}
\tag{1.2}

因为

\[
z=q5^\lambda=g\omega-c_u.
\]

core §12.7 还记录两个 Hensel quotient identities：

\[
\boxed{
g\theta=5^{M+\lambda}+c_Qc_u,}
\tag{1.3}

\[
\boxed{
c_Q\omega-\theta=2^m5^\lambda c_u.}
\tag{1.4}

本文证明 (1.3)–(1.4) 不独立。

---

## 2. `已严格完成`：`theta` 可由 source split + source triangle 消掉

由 (1.2)：

\[
gc_Q\omega
=c_Q5^\lambda q+c_Qc_u.
\]

再由 (1.1)：

\[
c_Q5^\lambda q
=5^\lambda(5^M+D_0c_u)
=5^{M+\lambda}+5^\lambda D_0c_u.
\]

因此

\[
\boxed{
gc_Q\omega
=5^{M+\lambda}+5^\lambda D_0c_u+c_Qc_u.}
\tag{2.1}

又 `D_0=2^mg`，所以

\[
5^\lambda D_0c_u
=g\,2^m5^\lambda c_u.
\]

移项：

\[
\boxed{
g(c_Q\omega-2^m5^\lambda c_u)
=5^{M+\lambda}+c_Qc_u.}
\tag{2.2}

定义

\[
\theta:=c_Q\omega-2^m5^\lambda c_u.
\]
就同时得到

\[
\boxed{c_Q\omega-\theta=2^m5^\lambda c_u}
\]
和

\[
\boxed{g\theta=5^{M+\lambda}+c_Qc_u.}
\]

也就是说：

\[
\boxed{(1.1)+(1.2)\Longrightarrow(1.3)+(1.4).}
\tag{2.3}

core 的 `theta` 并没有提供第三条独立 source/tail equation。

---

## 3. converse dependency

反过来，若保留 (1.2)、(1.3)、(1.4)，则

\[
\begin{aligned}
g\theta
&=gc_Q\omega-g2^m5^\lambda c_u\\
&=c_Q(5^\lambda q+c_u)-D_05^\lambda c_u\\
&=5^\lambda(c_Qq-D_0c_u)+c_Qc_u.
\end{aligned}
\]

与 (1.3) 比较并约去 `c_Qc_u`：

\[
5^\lambda(c_Qq-D_0c_u)=5^{M+\lambda},
\]
故

\[
\boxed{c_Qq=5^M+D_0c_u.}
\tag{3.1}

所以四个方程的独立秩只有两条；任何三条都会恢复第四条。尤其不能把 `theta` 当成新的 mod-`23` gate 再收费。

---

## 4. normalized fixed-`23` tail bridge同样是 shadow

固定

\[
h:=v_{23}(c_Q)\ge1,
\]
并定义

\[
\widetilde Q:=\frac{Q}{23^h},
\qquad
\widetilde c:=\frac{c_Qc_u}{23^h},
\qquad
\rho:=\frac{q5^\lambda}{c_u}.
\]

由真实 denominator formulas

\[
Q=2^{M+1}c_Qq
\]
直接有

\[
\boxed{
5^\lambda\widetilde Q
=2^{M+1}\rho\widetilde c.}
\tag{4.1}

若 `h=1`，写

\[
q_1:=Q/23,
\qquad
\gamma:=(c_Qc_u)/23,
\]
则

\[
\boxed{
\gamma\rho
=\frac{5^\lambda q_1}{2^{M+1}}.}
\tag{4.2}

另一方面 `source-discriminant.md` 已有

\[
b_3z=Tc_uQ.
\]
利用

\[
b_3=2^{M+m+1}5^dc_Qc_u,
\qquad
z=q5^\lambda,
\qquad
\lambda=m-d,
\]
约去同一组因子，恰好重新得到 (4.1)。

因此

\[
\boxed{
\text{normalized tail bridge}
=\text{real denominator-ratio identity 的逐 }23^h\text{ 约分。}}
\tag{4.3}

它非常适合作为坐标转换，但不是独立 obstruction。

---

## 5. 对 fixed `23` synchronization 的影响

`spontaneous-cq-relative-depth-nogo.md` 已给 depth `>=2` 的两个等价接口：

\[
\kappa_{\rm pref}(M,q_1)=\kappa_\sigma(\rho),
\tag{5.1}
\]

或在 `h=1` 时写成

\[
\gamma\equiv\Gamma_\sigma(M,q_1,\lambda,\kappa)\pmod{23}.
\tag{5.2}

本文证明：把 core 的 `omega,theta` 方程加入 (5.2) 后，不会产生第二个关于 `gamma` 的同余，因为它们精确退化回 (1.1)、(1.2)、(4.2)。

所以以下路线必须降级：

1. 再对 `theta` 做 mod `23` / mod `23^2` 消元；
2. 把 `c_Qomega-theta` 当成独立 linear gate；
3. 用 `b_3z=Tc_uQ` 与 (4.2) 制造两个看似不同的 tail 条件。

它们都是同一 source/denominator identity 的不同坐标。

---

## 6. 更新后的真正开放核

fixed `23` 的局部和 source quotient 自由现在都已经审计清楚：

- first layer singularity 经一次 blow-up 后恢复 smooth；
- additive second layer只是 `kappa <-> rho` 的 Möbius chart；
- `theta` 与 normalized tail bridge没有新增独立约束。

因此若要继续封锁 pure-`c_Q` odd depth，必须加入一个**不属于 source quotient 闭包**的对象。当前规范候选为：

\[
\boxed{
\begin{array}{l}
\text{canonical factors }H_0\pm Y_3=c_\pm^2(5^\lambda X\text{ or }Y),\\
\text{finite-defect / rational-root integer }F(J),\ \Xi_C,\ \Delta_\pm,\\
\text{或其他具有独立 sign/height 的 natural representative.}
\end{array}}
\tag{6.1}

下一步若继续 fixed `23`，应直接把 `kappa_pref=kappa_sigma(rho)` 与其中一类对象联立；继续 source Hensel quotient algebra 已经没有新增信息。

---

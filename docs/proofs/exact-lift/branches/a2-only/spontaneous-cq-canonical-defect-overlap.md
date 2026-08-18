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
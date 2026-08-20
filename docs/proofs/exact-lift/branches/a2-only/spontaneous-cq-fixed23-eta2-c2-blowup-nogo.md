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
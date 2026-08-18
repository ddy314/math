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
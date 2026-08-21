# A2 fixed `3` exception collapse：deeper-central 精确 `12` 与 `eta=1` f-contact 横截

> **依赖：** `fixed3-terminal-spill.md`、`descendant-f-gd-bridge.md`、`endpoint-lattice.md` §§16.3–16.7、16.57–16.59，以及历史 descendant second/third-order canonical recursion。
>
> **严格状态：**本文继续处理 `fixed3-terminal-spill.md` 留下的两个 fixed sheets。第一，`a_3`-shallow 通道中只要 `v_3(2K-9)>=3`，不论 `3|f` 与否，third-order descendant numerator 的 `3`-进赋值都精确等于 `12`，所以 deeper-central sheet 整体不能供应 odd spill parity。第二，在 `eta=1` 的唯一 odd-`3` endpoint 类型 `(d,c_Q,k_h,slot)=(2,7,3,-)` 上，`a_2`-shallow 的 `3|f` 直接与 high-factor equality 模 `3` 矛盾。本文仍未排除一般 `eta>=2` 的 `a_2`-shallow `f`-contact，以及 `a_3`-shallow 中 `v_3(2K-9)=2` 且 `3|f` 的残余通道，因此仍不宣称 A2 关闭。

---

## 1. 记号与 third recursion

沿用 `fixed3-terminal-spill.md` 的 descendant parent coordinates

\[
X_d:=5^\lambda\mathscr R_{63}^\star,
\qquad
Y_d:=g2^m\widehat{\mathscr D}_{63},
\qquad
\widehat{\mathcal T}_2=X_d+Y_d.
\tag{1.1}
\]

历史 canonical recursion 可写成

\[
\mathscr N_{63}^{(3)}=T^6\mathscr E_3,
\tag{1.2}
\]

其中 `T=10^m` 为 `3`-进单位，而

\[
\boxed{
\mathscr E_3
=64A^2(81X_d\mathfrak G_<+2Y_d\mathfrak G_>)
+AC\,\mathcal H_2(X_d,Y_d;K,\zeta)
+D\,\mathcal H_3(X_d,Y_d;K,\zeta),
}
\tag{1.3}
\]

这里

\[
A:=5^mB^2,
\qquad B=2^{M+m+1}c_ug,
\tag{1.4}
\]

\[
C:=2^{2M+10}5^2\cdot11,
\qquad
D:=2^{4M+17}5^2\cdot11^2,
\tag{1.5}
\]

而 `G_<,G_>,H_2,H_3` 均为历史 checker canonical 重建的 primitive integer forms。

因为

\[
T^6\equiv1\pmod3,
\tag{1.6}
\]

`N_63^(3)` 与 `E_3` 有相同 `3`-进赋值及相同最终 normalized first digit。

---

## 2. `a_3`-shallow deeper-central 时自动有 `81|Y_d`

固定

\[
\boxed{
v_3(a_3)=1,
\qquad
v_3(a_2)\ge2,
\qquad
v_3(2K-9)\ge3.}
\tag{2.1}
\]

写

\[
2K-9=27r,
\qquad
\zeta:=\frac{a_3}{T}=3z,
\qquad 3\nmid z.
\tag{2.2}
\]

于是

\[
K=\frac{9+27r}{2}=9\frac{1+3r}{2},
\tag{2.3}
\]

所以无论 `r` 是否再被 `3` 整除，始终有

\[
\boxed{v_3(K)=2.}
\tag{2.4}
\]

沿用 exact bridge

\[
\omega B_\Delta
=f((2K-9)T-a_3)-3c_u(K-3)T.
\tag{2.5}
\]

由 (2.2)：

\[
(2K-9)T-a_3
=3T(9r-z),
\tag{2.6}
\]

其赋值恰为 `1`；同时

\[
K-3=3\frac{1+9r}{2}
\tag{2.7}
\]

也恰含一份 `3`。因此无论 `3|f` 与否，至少有

\[
\boxed{v_3(B_\Delta)\ge1.}
\tag{2.8}
\]

再看

\[
\mathscr F_{63}
=(2K-9)B_\Delta-rac{63}{16}gTK^2.
\tag{2.9}
\]

第一项至少含 `3^4`；第二项中

\[
v_3(63)+2v_3(K)=2+4=6.
\]

所以

\[
\boxed{v_3(\mathscr F_{63})\ge4.}
\tag{2.10}
\]

进而

\[
\boxed{81\mid Y_d.}
\tag{2.11}
\]

注意这里**没有**使用 `3\nmid f`。因此旧 frontier 中的 `f`-contact 与 deeper-central 一旦同时发生，仍落入同一个四层以上的 parent divisibility box。

---

## 3. 关键模 `27` collapse

令

\[
X_d=x,
\qquad
Y_d=81y,
\qquad
2K-9=27r,
\qquad
\zeta=3z.
\tag{3.1}
\]

把 (3.1) 直接代入 canonical forms `G_<,G_>,H_2,H_3` 与 (1.3)。checker 对全部 monomials 做 exact coefficient audit，得到：

\[
3^{10}\mid\mathscr E_3.
\tag{3.2}
\]

更关键的是，除以 `3^10` 后并不是留下一个庞大的多项式。先记

\[
t:=2^{2M+2}.
\tag{3.3}
\]

本通道有三个纯 source-unit congruences。

首先，因为 `81|Y_d`，模 `27` 时

\[
x\equiv\widehat{\mathcal T}_2\pmod{27}.
\tag{3.4}
\]

而

\[
\widehat{\mathcal T}_2
=2^mc_u^2g^2\mathscr S_0-5^mQ_0^2N_0.
\tag{3.5}
\]

当前 `v_3(a_2)>=2`，且 `C_0` 本身含 `3^2`，所以

\[
81\mid N_0=C_0^2+a_2^2.
\tag{3.6}
\]

另一方面，由 `K=(9+27r)/2` 与 `a_3=3Tz`：

\[
K^2-6K+1\equiv1\pmod{27},
\qquad
18-4K\equiv0\pmod{27}.
\]

于是

\[
\boxed{\mathscr S_0\equiv T\pmod{27}.}
\tag{3.7}
\]

故

\[
\boxed{x\equiv2^m(c_ug)^2T\pmod{27}.}
\tag{3.8}
\]

现在由 `T=2^m5^m` 与 (1.4)：

\[
A
=5^m2^{2M+2m+2}(c_ug)^2
\equiv t x\pmod{27}.
\tag{3.9}
\]

另外直接计算固定系数：

\[
2^8\cdot5^2\cdot11\equiv11\pmod{27},
\tag{3.10}
\]

\[
2^{13}\cdot5^2\cdot11^2\equiv11\pmod{27}.
\tag{3.11}
\]

所以

\[
\boxed{C\equiv11t,\qquad D\equiv11t^2\pmod{27}.}
\tag{3.12}
\]

把 (3.9)、(3.12) 一次代入 checker 重建的完整 depth-`10` normalized polynomial，125 个原 monomials 在模 `27` 下坍缩成**唯一单项式**：

\[
\boxed{
\frac{\mathscr E_3}{3^{10}}
\equiv9t^2x^3\pmod{27}.}
\tag{3.13}
\]

因此

\[
\boxed{
\frac{\mathscr N_{63}^{(3)}}{3^{12}}
\equiv t^2x^3\pmod3.}
\tag{3.14}
\]

而 `t` 为单位，`t^2≡1 mod3`；(3.8) 又给

\[
x\equiv2^m\equiv(-1)^m\pmod3.
\tag{3.15}
\]

故最终

\[
\boxed{
\frac{\mathscr N_{63}^{(3)}}{3^{12}}
\equiv(-1)^m\not\equiv0\pmod3.}
\tag{3.16}
\]

即

\[
\boxed{v_3(\mathscr N_{63}^{(3)})=12.}
\tag{3.17}
\]

这是 exact equality，不是 `>=12`。

因此：

\[
\boxed{
\begin{array}{c}
v_3(a_3)=1,\ v_3(a_2)\ge2,\ v_3(2K-9)\ge3\\[1mm]
\Longrightarrow\\[1mm]
v_3(\mathscr N_{63}^{(3)})=12,
\end{array}}
\tag{3.18}
\]

并且结论与 `v_3(f)` 完全无关。deeper-central fixed `3` 对 third-order positive parent只贡献偶 parity。

结合 `fixed3-terminal-spill.md` §4，`a_3`-shallow 通道的 fixed-`3` frontier 因而从

\[
3|f\quad\text{or}\quad v_3(2K-9)\ge3
\]
进一步收缩为

\[
\boxed{3|f\quad\text{and}\quad v_3(2K-9)=2.}
\tag{3.19}
\]

因为 central 一旦再深，无论 `f` 是否同时接触，赋值都立刻固定为 `12`。

---

## 4. `eta=1` 唯一 odd-`3` type 中 `a_2`-shallow f-contact 不存在

这一节只处理 `eta=1`，不把它误写成任意 `eta` 的结论。

`endpoint-lattice.md` 的 Gaussian-support classification 在 `eta=1` 最终只留下五型，其中 `v_3(k_h)` 为奇数的唯一类型是

\[
\boxed{(d,c_Q,k_h,\mathrm{slot})=(2,7,3,-).}
\tag{4.1}
\]

因此若再处于 `a_2`-shallow channel：

\[
v_3(a_2)=1,
\qquad
v_3(a_3)\ge2,
\tag{4.2}
\]

写

\[
a:=a_2/3\in\mathbf Z_3^\times.
\tag{4.3}
\]

反设

\[
3\mid f.
\tag{4.4}
\]

由

\[
f=5^\lambda q+2c_u,
\qquad
Q_0=c_Qq=5^M+2^mgc_u,
\tag{4.5}
\]

以及

\[
M=2m-1,
\qquad
\lambda=m-d=m-2,
\tag{4.6}
\]

令

\[
s:=(-1)^m.
\]

模 `3` 时 (4.4) 给

\[
q\equiv s c_u.
\tag{4.7}
\]

而 `c_Q=7≡1`、`M` 为奇数，所以 (4.5) 的 `Q_0` identity 给

\[
s c_u=-1+s g c_u.
\]

也即

\[
\boxed{s c_u(1-g)=-1\pmod3.}
\tag{4.8}
\]

若 `g≡1`，左边为零，立即矛盾；因此

\[
\boxed{g\equiv-1\pmod3.}
\tag{4.9}
\]

另一方面，negative high slot 的 exact factor equality 是

\[
\boxed{H_0-Y_2=\frac{3g^2}{2},}
\tag{4.10}
\]

其中

\[
Y_2=a_2c_Q5^d.
\tag{4.11}
\]

现在除以 `3` 并模 `3`。原拼接分子

\[
\alpha=TK+a_3
\]

在 (4.2) 下满足

\[
\frac\alpha3\equiv a\pmod3.
\tag{4.12}
\]

又

\[
H_0=c_u\frac\alpha\omega,
\qquad
f=g\omega+c_u.
\]

由 (4.4)、(4.9)：

\[
\frac{c_u}{\omega}\equiv-g\equiv1\pmod3.
\]

所以

\[
\boxed{H_0/3\equiv a\pmod3.}
\tag{4.13}
\]

同时 `c_Q5^d=7\cdot25≡1 mod3`：

\[
\boxed{Y_2/3\equiv a\pmod3.}
\tag{4.14}
\]

于是 (4.10) 除以 `3` 后左边模 `3` 为零；右边却是

\[
\frac{g^2}{2}\equiv\frac12\equiv2\pmod3.
\tag{4.15}
\]

矛盾。

因此严格得到

\[
\boxed{
\eta=1,\ (d,c_Q,k_h,slot)=(2,7,3,-),\ v_3(a_2)=1
\Longrightarrow
3\nmid f.}
\tag{4.16}
\]

再结合 `fixed3-terminal-spill.md` §3：该类型的 `a_2`-shallow fixed `3` third-parent depth只能是

\[
\boxed{v_3(\mathscr N_{63}^{(3)})=6.}
\tag{4.17}
\]

所以 `eta=1` 的这一半 fixed-`3` spill source 已完全消失。

---

## 5. 更新后的 fixed-`3` frontier

目前可严格写成：

### `a_2`-shallow

\[
v_3(a_2)=1,
\qquad v_3(a_3)\ge2.
\]

若 `3∤f`，已有 exact depth `6`。在 `eta=1` 唯一 odd-`3` 类型中，本文又排除了 `3|f`。因此：

\[
\boxed{\eta=1\text{ 的 }a_2\text{-shallow fixed-3 不可能供应 spill parity}.}
\tag{5.1}
\]

一般 `eta>=2` 的 `f`-contact 仍需独立处理。

### `a_3`-shallow

\[
v_3(a_3)=1,
\qquad v_3(a_2)\ge2.
\]

- `3∤f` 且 central depth `2`：exact depth `10`；
- central depth `>=3`：**无论 `3|f` 与否**，exact depth `12`。

所以唯一仍能让 fixed `3` 保持 odd-depth 可能性的区域已经缩成

\[
\boxed{
3\mid f,
\qquad
v_3(2K-9)=2.}
\tag{5.2}
\]

这比上一文件的并集 frontier 严格更小：两个 exceptions 必须真正发生交叉，而不是任选其一。

A2 仍为 `待证`。下一步应直接处理 (5.2) 的交叉 residue，并同步审计一般 `eta>=2` 的 `a_2`-shallow f-contact；不应再对 deeper-central 做机械 `3^k` 展开。

---

## 6. verification

```bash
uv run python scripts/exact-lift/a2-only/check_a2_fixed3_exception_collapse.py
```

checker canonical 重建 `G_<,G_>,H_2,H_3`，验证 (3.13) 的模 `27` 单项式 collapse，并独立验证 §4 的 `F_3` source/high-factor 矛盾。
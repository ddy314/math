# A1 minimal diagonal: moderate `LL` fixed Pell normal form

> 日期：2026-08-20。依赖 `deep-moderate-factorization.md`、`deep-double-5high-collapse.md`、`deep-typewise-r-window.md`。当前范围 `k=g>=31`。

本文证明 moderate double-deep 的 `LL` 分支已经和 central sector 一样，归约成**绝对有限个固定系数 generalized Pell families**。

核心点：LL 中 `D|r`，而 `r` 有绝对 typewise 上界，所以 `D,gamma,r` 都与 `k` 无关且绝对有限。全部 `k`-依赖只剩

\[
L=T/D.
\]

状态：**归约与 local squareclass 严格完成；剩余 nonsquare families 的 finite modular exhaustion 待做。**

---

## 1. LL 中 `D|r`

LL 有

\[
v_2(r)=A+2\nu_2+e,
\qquad
v_5(r)=B+2\nu_5,
\]

其中

\[
e=v_2(w).
\]

因此

\[
\boxed{D=2^A5^B\mid r.}
\tag{1}
\]

定义

\[
\boxed{R:=r/D\in\mathbf Z_{>0}.}
\tag{2}
\]

又由 `deep-typewise-r-window.md`：

\[
r<15,204,353.
\]

所以

\[
\boxed{D<15,204,353.}
\tag{3}
\]

由于

\[
15.09<\Gamma_k=\gamma/D<39.003,
\]

得到

\[
\boxed{0<\gamma<39.003D<6\times10^8.}
\tag{4}
\]

因此 `(D,gamma,r)` 全部属于绝对有限整数集合。

---

## 2. 从 moderate quadratic 除去 `D^2`

`deep-moderate-factorization.md` 的 quadratic 为

\[
C_0D^2N_0^2
-DuTN_0
+1000\gamma^2T^2
+\gamma Dr
=0,
\tag{5}
\]

其中

\[
C_0=w(10w-1),
\qquad
\boxed{u=10\gamma(20w-1)+Dr.}
\tag{6}
\]

LL 中 `D|T`，因为 `A<=23,B<=10` 而 `k>=31`。令

\[
\boxed{L:=T/D\in\mathbf Z.}
\tag{7}
\]

把 (5) 除以 `D^2`，并使用 `R=r/D`：

\[
\boxed{
C_0N_0^2-uLN_0+1000\gamma^2L^2+\gamma R=0.
}
\tag{8}
\]

所有系数 `C_0,u,gamma,R` 都与 `k` 无关；唯一的 unbounded variable ray 是

\[
L=10^k/D.
\]

---

## 3. fixed generalized Pell family

把 (8) 看成关于 `N_0` 的二次方程。判别式必须是整数平方：

\[
\boxed{
Y^2=A_{\gamma,r,D}L^2+B_{\gamma,r,D},
}
\tag{9}
\]

其中

\[
\boxed{
A_{\gamma,r,D}:=u^2-4000C_0\gamma^2,
}
\tag{10}
\]

\[
\boxed{
B_{\gamma,r,D}:=-4C_0\gamma R<0.
}
\tag{11}

定义 natural point

\[
u_0:=10\gamma(20w-1).
\]

已有恒等式

\[
u_0^2-4000C_0\gamma^2=100\gamma^2.
\]

而 `u=u_0+Dr>u_0`，所以

\[
\boxed{A_{\gamma,r,D}>100\gamma^2>0.}
\tag{12}
\]

故每个 fixed parameter tuple 都是一条正主系数、负固定 norm 的 generalized Pell family。

---

## 4. square-`A` 退化族统一无解

若

\[
A_{\gamma,r,D}=S^2,
\]

则 (9) 为

\[
Y^2=(SL)^2-|B|.
\]

由 (12)：

\[
S>10\gamma>150D.
\]

于是

\[
SL>150D\frac TD=150T\ge1.5\times10^{33}.
\]

另一方面由 (3)-(4)、`C_0<=156`、`R=r/D<15,204,353` 可取极粗安全界

\[
|B|<6\times10^{18}.
\]

所以

\[
0<|B|<2SL-1.
\]

从而

\[
(SL-1)^2<(SL)^2-|B|<(SL)^2,
\]

矛盾。因此

\[
\boxed{
A_{\gamma,r,D}\text{ square}
\Longrightarrow
\text{LL family empty}.}
\tag{13}
\]

后续只需处理 nonsquare `A`。

---

## 5. `B` 必须是完整 2/5-adic squareclass

写

\[
R=2^{2\nu_2+e}5^{2\nu_5}r_{10},
\qquad
r_{10}=r/2^{v_2(r)}5^{v_5(r)}.
\]

又写

\[
w=2^e w_0,
\qquad w_0\text{ odd}.
\]

因为 double-deep 中 `gamma` 与 10 互素，(11) 给

\[
v_2(B)=2+2e+2\nu_2,
\qquad
v_5(B)=2\nu_5.
\]

由 `v_2(r)<=23,v_5(r)<=10` 和 `k>=31`，这两个固定赋值都严格小于 `2v_2(L),2v_5(L)`。所以 (9) 模任意深 `2/5` 次幂强迫

\[
\boxed{B\in\mathbf Q_2^{\times2}\cap\mathbf Q_5^{\times2}.}
\tag{14}
\]

提出全部偶次 prime powers 后，两个单位条件统一落到

\[
\boxed{
-\gamma w_0(10w-1)r_{10}\equiv1\pmod8,
}
\tag{15}
\]

以及

\[
\boxed{
\left(\frac{-\gamma w_0(10w-1)r_{10}}5\right)=1.
}
\tag{16}
\]

所以对固定 `(w,r,D,nu_2,nu_5)`：

- `gamma mod 8` 唯一；
- `gamma mod 5` 只有两个 quadratic-character classes；
- CRT 后 `gamma` 只落在两个 `mod 40` residue classes。

这正是 central modular exhaustion 之前使用过的同型 local-squareclass funnel。

---

## 6. 当前 LL 核心

moderate LL 现在可按绝对有限参数

\[
\boxed{(z,w,r,\nu_2,\nu_5,D,\gamma)}
\]

组织，其中：

1. `r` 在 `deep-typewise-r-window.md` 的 typewise finite interval；
2. `D|r` 且 `D=2^A5^B`，`A,B>0`；
3. `gamma` 在 `15.09D..39.003D` 的 typewise 更窄 interval；
4. `gamma` 只允许 (15)-(16) 的两个 `mod40` classes；
5. square-`A` families 已全部删除；
6. nonsquare family 只需检查
   \[
   Y^2=A L^2+B,
   \qquad L=10^k/D.
   \]

因此 LL 已经不再是 unbounded coefficient problem。下一步可沿 central 的经验，对这些 fixed nonsquare families 做 period-prime modular cover；不需要 factor `b_1,Q`。
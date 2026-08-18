# A2 pure-`c_Q` relative-depth derivative no-go 与 fixed `23` 二阶提升

> **依赖：** `spontaneous-cq-global-coupling.md`、`spontaneous-angle-pair-cq-nogo.md`。
>
> **严格状态：**修正后的 pure-`c_Q` depth matrix 有两个 orientation gate `G_+`,`G_-`。本文直接审计“比较 `D_pref` 与 `G_±` 的 normalized derivative 能否强迫 parity equality”这条路线。结论是 generic `p!=23` 上完全失败：精确二维系统对 `(K,rho)` 的 Jacobian 永远为 unit，因此局部 Hensel 几何允许唯一无障碍提升，不能产生 valuation-parity obstruction。唯一真正退化的 prime 是 `23`。本文进一步把 `23` 的第一层退化展开到 `23^2`，得到显式 normalized compatibility；其中一个 `K` correction 类 `kappa=18 mod23` 在两种 orientation 中都不能提升。剩余 classes 中 source ratio `rho=z/c_u` 被唯一固定。本文尚未把该 ratio 与 source split 全局联立，因此不关闭 A2。

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
\rho:=\frac z{c_u}.
\]

`spontaneous-cq-global-coupling.md` 已证明，在 canonical orientation `sigma in {+,-}` 中 additive gate 可写成

\[
\boxed{
g_\sigma(K,\rho)
:=\frac{\mathcal G_\sigma}{c_u}
=\rho A_K+2C_\sigma(K).}
\tag{1.1}
\]

而 pure-`c_Q` actual common depth由

\[
D_{\rm pref},\qquad g_\sigma
\]
共同读取。

---

# I. generic derivative route is a strict no-go

## 2. exact Jacobian 是三角 unit

把 background integers `B,N` 固定，视

\[
F_1(K,\rho):=D_{\rm pref},
\qquad
F_2(K,\rho):=g_\sigma(K,\rho).
\]

因为 `D_pref` 不含 `rho`：

\[
\frac{\partial F_1}{\partial K}=-2K,
\qquad
\frac{\partial F_1}{\partial\rho}=0.
\]

另一方面

\[
\frac{\partial F_2}{\partial\rho}=A_K.
\]

故

\[
\boxed{
\det\frac{\partial(F_1,F_2)}{\partial(K,\rho)}
=-2K A_K.}
\tag{2.1}
\]

若保留未除去的 integer gate `G_sigma`，只多一个 unit `c_u`：

\[
\boxed{J_\sigma=-2c_uKA_K.}
\tag{2.2}
\]

angle first layer给

\[
K^2=8181N^2\pmod p,
\]
所以 genuine non-`3` inert prime上 `K` 是 unit。

若同时 `A_K=0`，则由 `g_sigma=0` 还必须 `C_sigma=0`。两个 orientation 的 resultant 都是

\[
\operatorname{Res}_K(A_K,2C_\sigma)=-5060
=-2^2\cdot5\cdot11\cdot23.
\]

`p=11` 的共同根是 `K=0`，与 angle root矛盾。因此

\[
\boxed{p\ne23\Longrightarrow J_\sigma\in\mathbf Z_p^\times.}
\tag{2.3}
\]

---

## 3. 严格 no-go 含义

对任意 generic first-layer root

\[
D_{\rm pref}=g_\sigma=0\pmod p,
\qquad p\ne23,
\]
二维 Hensel lemma 直接给唯一 local lift。更具体地：

- `D_pref` 对 `K` 的 transverse derivative `-2K` 是 unit；
- 在任意已经选定的 `K` lift 上，`g_sigma` 对 `rho` 的 derivative `A_K` 是 unit。

因此逐层提升时，prefix correction 与 source-ratio correction 都只是普通的一次线性修正；不存在奇偶层被跳过、二次分叉或 fixed singular prime。

于是：

\[
\boxed{
\text{比较 }D_{\rm pref}\text{ 与 }G_\pm\text{ 的 local derivative}
\text{ 不能证明 valuation 差为偶。}}
\tag{3.1}
\]

这比仅说“first layer smooth”更强：**relative-depth derivative route 本身已经降级。** 若最终要删除 pure-`c_Q` residual parity，必须使用限制真实 `(K,rho)` 共同轨道的 global integer relation，而不是继续局部 Hensel 展开。

---

# II. unique exceptional prime `23`

## 4. first layer 数据

唯一 Jacobian-degenerate genuine prime是

\[
\boxed{p=23.}
\]

两种 orientation 都有共同根

\[
\boxed{K_0=16\pmod{23}.}
\tag{4.1}
\]

angle equation给

\[
8181\equiv16\pmod{23},
\]
所以

\[
N^2\equiv16\pmod{23}.
\tag{4.2}
\]

故

\[
M\equiv5\text{ or }16\pmod{22}.
\tag{4.3}
\]

为做下一层，写

\[
K=16+23\kappa,
\tag{4.4}
\]

\[
N^2=16+23h_N,
\tag{4.5}
\]

\[
Q=B+2N=23q_1.
\tag{4.6}
\]

这里 `h_N,q_1` 都先只按 `mod23` 读取；若 `v_23(Q)>=2`，则 `q_1=0 mod23`。

---

## 5. prefix defect 的 normalized `23^2` equation

有 exact identity

\[
\boxed{
D_{\rm pref}
=8181N^2-K^2+2025Q(Q-4N).}
\tag{5.1}
\]

因为

\[
8181=16+23\cdot355,
\qquad
2025\equiv1\pmod{23},
\]
把 (4.4)–(4.6) 代入并除以 `23`：

\[
\boxed{
\frac{D_{\rm pref}}{23}
\equiv
16h_N+22-9\kappa-4Nq_1
\pmod{23}.}
\tag{5.2}
\]

其中最后一项的 `N` 只需取模 `23`，即

\[
N\equiv19\quad(M=5\bmod22),
\]

或

\[
N\equiv4\quad(M=16\bmod22).
\]

所以 angle/prefix 想提升到 `23^2`，会唯一固定

\[
\boxed{
9\kappa
\equiv16h_N+22-4Nq_1
\pmod{23}.}
\tag{5.3}
\]

---

## 6. 两个 additive gate 的 normalized next layer

在 `K=16`：

\[
A_K=23,
\]

\[
C_+(16)=391=17\cdot23,
\]

\[
E_K(16)=368=16\cdot23.
\]

并且 derivatives 为

\[
A_K'(16)=14,
\qquad
C_+'(16)=69=3\cdot23,
\qquad
E_K'(16)=55\equiv9\pmod{23}.
\]

因此：

### plus orientation

\[
\boxed{
\frac{g_+}{23}
\equiv
\rho(1+14\kappa)+11
\pmod{23}.}
\tag{6.1+}
\]

### minus orientation

\[
\boxed{
\frac{g_-}{23}
\equiv
\rho(1+14\kappa)-9-18\kappa
\pmod{23}.}
\tag{6.1-}
\]

所以当

\[
1+14\kappa\ne0\pmod{23},
\]
两种 orientation 都会唯一固定 source ratio：

\[
\boxed{
\rho_+
=-\frac{11}{1+14\kappa},}
\tag{6.2+}
\]

\[
\boxed{
\rho_-
=\frac{9+18\kappa}{1+14\kappa}.}
\tag{6.2-}
\]

---

## 7. 一个 `K` correction class 被两边同时删除

方程

\[
1+14\kappa=0\pmod{23}
\]
唯一给

\[
\boxed{\kappa=18.}
\tag{7.1}
\]

此时 plus equation (6.1+) 的右边恒为

\[
11\ne0\pmod{23},
\]
所以不能 lift。

minus equation则变成

\[
-9-18\cdot18
\equiv-11\ne0\pmod{23},
\]
同样不能 lift。

因此有新的严格删除：

\[
\boxed{
\kappa\equiv18\pmod{23}
\Longrightarrow
\text{pure-}c_Q\text{ common root不能提升到 }23^2,}
\tag{7.2}
\]

而且这个结论与 `c_- / c_+` orientation 无关。

结合 (5.3)，可把它写成 background normalized quotient 的排除条件：

\[
\boxed{
16h_N+22-4Nq_1
\not\equiv9\cdot18=1
\pmod{23}.}
\tag{7.3}
\]

即任何 surviving `23^2` state 必满足

\[
\boxed{16h_N+21-4Nq_1\ne0\pmod{23}.}
\tag{7.4}
\]

---

## 8. decimal length quotient 已完全周期化

`10` modulo `23^2=529` 的阶为

\[
\boxed{506=22\cdot23.}
\tag{8.1}
\]

并且

\[
\boxed{10^{22}\equiv1+8\cdot23\pmod{529}.}
\tag{8.2}
\]

写

\[
M=M_0+22j,
\qquad0\le j<23,
\]
其中 `M_0=5` 或 `16`。则

\[
\boxed{
h_N\equiv h_0+3j\pmod{23},}
\tag{8.3}
\]

其中

\[
\boxed{
M_0=5:\ h_0=15,
\qquad
M_0=16:\ h_0=5.}
\tag{8.4}
\]

所以 fixed `23` 的 decimal coordinate 在 `mod506` 内已经完全显式。剩余非十进制自由只在 `q_1=Q/23` 与 source ratio `rho=z/c_u`。

---

## 9. 更新后的 frontier

本轮给出两个明确结论。

第一，generic `p!=23`：

\[
\boxed{
\text{relative derivative / ordinary Hensel synchronization 是严格 no-go。}}
\]

后续不得再试图从 `D_pref,G_±` 的 local Jacobian 推 valuation parity。

第二，fixed `23` 已从 first-layer exception推进到 next layer：

\[
M\bmod22
\longrightarrow
h_N\bmod23,
\]

\[
D_{\rm pref}/23=0
\longrightarrow
\kappa,
\]

\[
g_\pm/23=0
\longrightarrow
\rho_\pm,
\]

并严格删除

\[
\kappa=18.
\]

下一步若继续 `23`，应把

\[
q_1=Q/23,
\qquad
\rho=q5^\lambda/c_u
\]
用 source split `Q_0=c_Qq` 与 canonical `c_- / c_+` allocation 联立；这已经是一个真正的 global source/length congruence，而不再是 local Hensel derivative 问题。
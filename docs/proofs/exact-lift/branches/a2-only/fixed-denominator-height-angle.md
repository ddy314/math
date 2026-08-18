# A2 fixed denominator–height–angle shallow templates `7,23,43`

> **依赖：** `height-cofactor.md`、`spontaneous-denominator-common.md`、`spontaneous-denominator-depth-matrix.md`。
>
> **严格状态：**`height-cofactor.md` 已证明：若 non-`3` inert prime 同时进入 saturated denominator、height `W_q` 与 additive cofactor `widehat(T)_2`，则 q-side 只能是 `23`，f-side只能是 `7,43`，且三对象共同深度最多一层。本文继续加入 spontaneous angle/common contact，完整枚举这三个 fixed primes 的 genuine first-layer decimal states。结论是恰有 5 个 genuine templates，全部 Jacobian nonsingular，且全部与真实 decimal orbit `tau=10^{-M}` 兼容。因此这些 primes 不能靠 first-layer/decimal枚举排除；它们应作为固定浅层 parity correction处理，而不是继续做机械三重 `p^k` lifting。本文不宣称 A2 closure。

---

## 1. height + saturation 固定共同 `K` center

若 prime同时满足 height

\[
p\mid W_q,
\]
则

\[
TK+a_3\equiv0\pmod p.
\tag{1.1}
\]

saturated denominator odd excess给

\[
2a_3+9T\equiv0\pmod p.
\tag{1.2}
\]

相消得到

\[
\boxed{2K-9\equiv0\pmod p,}
\qquad
\boxed{K\equiv9/2\pmod p.}
\tag{1.3}
\]

`height-cofactor.md` 随后用 `F_W/G_W` 的整数 Bézout identity证明：

\[
\boxed{q\text{-side}:p=23,}
\tag{1.4q}
\]

\[
\boxed{f\text{-side}:p\in\{7,43\},}
\tag{1.4f}
\]

并且三对象共享深度

\[
\min(v_p(\text{den}),v_p(W_q),v_p(\widehat T_2))=1.
\tag{1.5}
\]

本文只审计再加入 angle common 后的 first-layer状态。

---

# q-side: `p=23`

## 2. q-line 与 angle/common 方程

q denominator line给

\[
\boxed{x=-2.}
\tag{2.1}
\]

angle contact给

\[
\boxed{\Delta_0=2025x^2-18y-y^2=0.}
\tag{2.2}
\]

令

\[
s:=9+y,
\qquad
\tau:=10^{-M}.
\]

因为

\[
K=10^M(9+y)=s/\tau,
\]
center (1.3) 等价于

\[
\boxed{2s-9\tau=0.}
\tag{2.3}
\]

在 `x=-2`：

\[
\Delta_0=8181-s^2.
\]
所以 q-side fixed common system就是

\[
\boxed{s^2=8181,\qquad2s=9\tau\pmod{23}.}
\tag{2.4}
\]

模 `23`：

\[
8181\equiv16,
\]
因此

\[
s=4\quad\text{or}\quad19=-4.
\]

得到恰好两个 states：

\[
\boxed{(y,\tau)=(18,6),\qquad(10,17)\pmod{23}.}
\tag{2.5}
\]

---

## 3. 两个 q-states 都是 simple

取方程

\[
F_q:=2(y+9)-9\tau,
\qquad
G_q:=8100-18y-y^2.
\]

Jacobian determinant关于 `(y,tau)` 为

\[
\det\frac{\partial(F_q,G_q)}{\partial(y,\tau)}
=-18(y+9).
\tag{3.1}
\]

在两个 states上分别为 nonzero residues，因此

\[
\boxed{p=23\text{ 的两个 q-angle templates均 nonsingular}.}
\tag{3.2}
\]

---

## 4. 两个 q-states 都属于真实 decimal orbit

精确计算

\[
\boxed{\operatorname{ord}_{23}(10)=22.}
\tag{4.1}
\]

即 `10` 是 `F_23^×` 的生成元。因此所有 nonzero `tau` 都属于 decimal subgroup。

离散指数为

\[
10^{-16}\equiv6\pmod{23},
\qquad
10^{-5}\equiv17\pmod{23}.
\]
所以

\[
\boxed{
\begin{aligned}
(y,\tau)=(18,6)&\Longrightarrow M\equiv16\pmod{22},\\
(y,\tau)=(10,17)&\Longrightarrow M\equiv5\pmod{22}.
\end{aligned}}
\tag{4.2}
\]

first-layer decimal orbit不排除 `23`。

---

# f-side: `p=7,43`

## 5. f common 的三方程系统

f-line + saturation + exact sphere在 `spontaneous-denominator-common.md` 已降成

\[
\Delta_0=0,
\tag{5.1}
\]

\[
\mathcal L_f^{\rm sat}
:=200x^2(s-9\tau)-y(x+2)^2=0.
\tag{5.2}
\]

height+saturation center仍是

\[
\boxed{2s-9\tau=0.}
\tag{5.3}
\]

在该 center，additive f-quadratic

\[
P_f(K)=3K^2-36K+26
\]
取值

\[
P_f(9/2)=-301/4=-7\cdot43/4,
\]
正好解释 fixed primes `7,43`。

所以 f-side只需在 `F_p` 中解

\[
\boxed{
2(y+9)-9\tau=0,
\quad
2025x^2-18y-y^2=0,
\quad
200x^2(y+9-9\tau)-y(x+2)^2=0.}
\tag{5.4}
\]

---

## 6. `p=7`：唯一 genuine state

完整枚举 `F_7^3` 得两点：

\[
(x,y,\tau)=(4,6,1),\qquad(0,0,2).
\]

第二点具有 `x=y=0`，属于已排除 boundary。故 genuine state唯一：

\[
\boxed{p=7:\quad(x,y,\tau)=(4,6,1).}
\tag{6.1}
\]

对 (5.4) 三方程关于 `(x,y,tau)` 的 Jacobian determinant，在该点为

\[
\boxed{4\pmod7,}
\tag{6.2}
\]
所以它是 simple state。

又

\[
\boxed{\operatorname{ord}_7(10)=6,}
\]
且 `tau=1`，因此

\[
\boxed{M\equiv0\pmod6.}
\tag{6.3}

所以 first-layer decimal orbit也不排除 `7`。

---

## 7. `p=43`：恰有两个 genuine states

完整枚举 `F_43^3` 得

\[
(0,0,2),
\qquad
(5,37,15),
\qquad
(18,33,38).
\]

第一点同样是 `x=y=0` boundary。故 genuine states为

\[
\boxed{
(5,37,15),\qquad(18,33,38)\pmod{43}.}
\tag{7.1}

三方程 Jacobian determinants分别为

\[
\boxed{4,\qquad3\pmod{43},}
\tag{7.2}
\]
均为 units。

decimal subgroup：

\[
\boxed{\operatorname{ord}_{43}(10)=21.}
\tag{7.3}
\]

两个 `tau` 都属于该 index-2 subgroup：

\[
10^{-10}\equiv15\pmod{43},
\qquad
10^{-8}\equiv38\pmod{43}.
\]
因此

\[
\boxed{
\begin{aligned}
(5,37,15)&\Longrightarrow M\equiv10\pmod{21},\\
(18,33,38)&\Longrightarrow M\equiv8\pmod{21}.
\end{aligned}}
\tag{7.4}

first-layer decimal orbit不排除 `43`。

---

## 8. fixed shallow template table

综合 q/f 两侧：

\[
\boxed{
\begin{array}{c|c|c}
p&\text{genuine angle/common state}&M\text{ class}\\ \hline
23&(x,y,\tau)=(-2,18,6)&16\pmod{22}\\
23&(x,y,\tau)=(-2,10,17)&5\pmod{22}\\
7&(4,6,1)&0\pmod6\\
43&(5,37,15)&10\pmod{21}\\
43&(18,33,38)&8\pmod{21}
\end{array}}
\tag{8.1}
\]

五个 states均 nonsingular且 decimal-compatible。

---

## 9. `审计 / no-go`：不要继续做机械三重 `p^k` lifting

这里必须结合 `height-cofactor.md` 的深度结论：

\[
\boxed{
\min(v_p(\text{den}),v_p(W_q),v_p(\widehat T_2))=1
\quad(p=7,23,43).}
\tag{9.1}
\]

所以不存在“denominator + height + additive cofactor 三对象一起继续到 `p^2,p^3,...`”的无界树。至少一个对象在第一层后立即停止。

因此本文的 5 个 simple templates不应被机械地向同一三重系统做 `p^k` lift；那会研究一个旧定理已经证明不存在的对象。

它们真正的作用是 global parity ledger中的固定浅层 correction：

- 每个 fixed prime都为 `3 mod4`；
- 若实际 endpoint命中某个 template，它最多贡献一层三对象共同 support；
- 之后只能研究哪一对象继续加深，以及它与 angle/common gcd 的 residual allocation。

---

## 10. 更新后的 fixed-prime frontier

本文没有关闭 `7,23,43`，反而严格证明它们的 first-layer templates是真实的 modular possibilities。因此后续不能声称 fixed denominator-height pool为空。

正确状态是：

\[
\boxed{
\{7,23,43\}\text{ 是有限、nonsingular、decimal-compatible 的 shallow correction pool}.}
\tag{10.1}
\]

如果要把它们从最终 `G_sp` parity中删除，必须利用 shared depth停止后的 **asymmetric higher-depth allocation** 或真实 natural representative；first-layer Legendre、decimal subgroup、singularity audit均已无新增排除力。
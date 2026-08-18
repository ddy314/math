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

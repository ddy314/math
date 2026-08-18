# A2 pure-`c_Q` 的 sphere 退化与 additive source-prefix coupling

> **依赖：** `spontaneous-angle-pair-q0-depth.md`、`spontaneous-angle-pair-cq-nogo.md`、`height-cofactor.md`、`source-discriminant.md`、`primitive-reduction.md`。
>
> **严格状态：**`spontaneous-angle-pair-cq-nogo.md` 已证明 pure-`c_Q` angle sign-pair 的 unsaturated odd depth 不能靠局部 conic/Hensel 几何排除。本文加入此前尚未在该退化层显式使用的 exact sphere 与 additive cofactor。结论有两层：第一，`x+2=0` 使 generic cross-sign sphere 公式退化后，两条 third-numerator 线性 branch 恰好是 `omega(H_0-Y_3)` 与 `omega(H_0+Y_3)`；其中 `H_0-Y_3` 是单位，`H_0+Y_3` 对 pure-`c_Q` 惰性素数恰有 `2v_p(c_Q)` 的平方深度，所以 sphere 本身仍只是 canonical height-square shadow。第二，若同一 pure-`c_Q` prime 还进入 additive carrier，则其 `2v_p(c_Q)` 截断深度可完全由一个新的 source-prefix polynomial `G_{c_Q}` 读取。于是 pure-`c_Q` 的 actual angle/additive common depth 被压成 `D_pref` 与 `G_{c_Q}` 的二维 simple synchronization；除固定 `23` 长度例外外，该 first-layer system Jacobian 满秩。本文不证明这两个 simple depths 的 parity 必相同，因此不关闭 A2。

---

## 1. 记号与 pure-`c_Q` channel

固定 reflection endpoint：

\[
N=10^M,
\qquad T=10^m,
\qquad A=a_2,
\qquad B=b_2,
\]

\[
Q=B+2N=2^{M+1}c_Qq,
\qquad
K=9N+10A,
\]

\[
N_0=\left(\frac{9B}{2}\right)^2+A^2.
\]

沿用 source notation

\[
z:=q5^\lambda,
\qquad
f=z+2c_u,
\]

以及

\[
H_0=c_uW_q,
\qquad
Y_3=ga_3,
\qquad
\alpha=TK+a_3=\omega W_q.
\]

`source-discriminant.md` 已证明

\[
\boxed{
z=g\omega-c_u,
\qquad
f=g\omega+c_u,
}
\tag{1.1}
\]

和 exact denominator ratio

\[
\boxed{
b_3z=Tc_uQ.}
\tag{1.2}
\]

本文固定 genuine non-`3` inert prime

\[
p\equiv3\pmod4,
\qquad p\ne3,5,
\]

并假设它是 pure-`c_Q` prime：

\[
\boxed{
p^c\Vert c_Q,
\qquad c\ge1,
\qquad p\nmid q.}
\tag{1.3}

由已有本原性，本文所需的

\[
p\nmid Ncu gW_q
\tag{1.4}
\]

均成立。

定义整数 prefix defect

\[
\boxed{
D_{\rm pref}
:=2025B^2+81N^2-K^2
=N^2\Delta_0.}
\tag{1.5}

`spontaneous-angle-pair-q0-depth.md` 已给 pure-`c_Q` angle 截断律

\[
\boxed{
\min\{v_p(\widehat{\mathcal O}_+),2c\}
=
\min\{v_p(D_{\rm pref}),2c\}.}
\tag{1.6}

同式也适用于 `widehat(O)_-`。

---

# I. `Q_0`-degenerate sphere

## 2. `x+2` 与 third denominator 不是两个自由小量

令

\[
x=\frac BN,
\qquad
s=\frac KN,
\qquad
u:=x+2=\frac QN,
\]

\[
\bar w:=\frac{b_3}{TN},
\qquad
\bar\zeta:=\frac{a_3}{TN},
\qquad
n:=\frac{N_0}{N^2}.
\]

由 (1.2)：

\[
\boxed{
z\bar w=c_u\nu.}
\tag{2.1}

所以在 pure-`c_Q` prime 上

\[
v_p(\nu)=v_p(\bar w)=c,
\]

并且两者的 ratio 已由 source data 精确固定。generic cross-sign 公式中把 `x+2` 当 unit 后出现的 `(x+2)^{-4}` 因而不能在该 channel 直接使用。

exact normalized sphere 为

\[
\boxed{
\mathscr S
=x^2\bar w^2(s+\bar\zeta)^2
-(\nu+\bar w)^2
\left(n\bar w^2+x^2\bar\zeta^2\right)=0.}
\tag{2.2}

把

\[
\bar w=\frac{c_u}{z}\nu
\]
代入。真实 endpoint 中 `Q>0`，故 `nu` 作为有理数并非零，可以在 exact rational identity 中约去 `nu^2`。清掉 `z` 分母后得到

\[
\boxed{
\begin{aligned}
&x^2z^2
\bigl(c_us-z\bar\zeta\bigr)
\bigl(c_us+f\bar\zeta\bigr)\\
&\qquad
=(z+c_u)^2n c_u^2\nu^2.
\end{aligned}}
\tag{2.3}

这里使用了 `f=z+2c_u`。所以 `nu=0` 的 first layer 并没有留下 generic quadratic extension，而是精确分裂成两条线性 branch：

\[
\boxed{
c_us-z\bar\zeta=0,}
\tag{2.4-}
\]

\[
\boxed{
c_us+f\bar\zeta=0.}
\tag{2.4+}

---

## 3. 两条 sphere branch 恰好是 canonical height factors

定义对应的整数线性量

\[
\boxed{
R_-:=Tc_uK-za_3,
\qquad
R_+:=Tc_uK+fa_3.}
\tag{3.1}

由 (1.1) 与 `alpha=omega W_q`：

\[
\begin{aligned}
R_-
&=c_u(TK+a_3)-g\omega a_3\\
&=\omega(c_uW_q-ga_3),
\end{aligned}
\]

故

\[
\boxed{R_-=\omega(H_0-Y_3).}
\tag{3.2-}

同理

\[
\boxed{R_+=\omega(H_0+Y_3).}
\tag{3.2+}

`height-cofactor.md` 的 canonical factor equality 给

\[
H_0-Y_3=5^\lambda c_-^2X,
\qquad
N=c_-^2X,
\]
因此

\[
\boxed{H_0-Y_3=5^\lambda N.}
\tag{3.3}

又

\[
(H_0-Y_3)(H_0+Y_3)
=5^\lambda c_Q^2XY,
\]
所以

\[
\boxed{
H_0+Y_3=\frac{c_Q^2XY}{N}.}
\tag{3.4}

对本文的 inert `p`，`p\nmid XY`。理由是已有

\[
N_0=5^{\nu_5}XY,
\]
而若 `p|N_0`，则

\[
\left(\frac{9B}{2}\right)^2+A^2\equiv0\pmod p.
\]
对 `p=3 mod4`，这会强迫 `p|A,B`，与 `(A,B)=1` 冲突。

因此 pure-`c_Q` 上有精确深度

\[
\boxed{
v_p(H_0-Y_3)=0,}
\tag{3.5-}

\[
\boxed{
v_p(H_0+Y_3)=2c.}
\tag{3.5+}

从而

\[
\boxed{
v_p(R_-)=v_p(\omega),
\qquad
v_p(R_+)=v_p(\omega)+2c.}
\tag{3.6}

这说明 `Q_0`-degenerate sphere 的两条 first-layer branch 完全没有新自由度：

- minus branch 只读取旧 `omega` content；
- plus branch 只读取 canonical `c_Q^2` height square，且深度严格为偶数 `2c`。

所以在 `spontaneous-angle-pair-cq-nogo.md` 之后，**exact sphere 本身不能把 unsaturated `v_p(Delta_0)<2c` 强迫成偶深度**。

---

# II. additive carrier 在 pure-`c_Q` 上的 source-prefix reduction

## 4. additive cofactor 的 `2c` 截断先降到 `S_0`

沿用 `height-cofactor.md`：

\[
\boxed{
\widehat{\mathcal T}_2
=2^mc_u^2g^2\mathscr S_0
-(c_Qq)^2 5^{2\lambda-d}XY,}
\tag{4.1}

其中

\[
\boxed{
\mathscr S_0
=T(K^2-26)-(2K-9)(2a_3+9T).}
\tag{4.2}

在 (1.3) 下，第二项的 `p`-进赋值恰为 `2c`，第一项前系数为 unit。因此

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),2c\}
=
\min\{v_p(\mathscr S_0),2c\}.}
\tag{4.3}

现在定义新的 pure source-prefix polynomial

\[
\boxed{
\begin{aligned}
\mathcal G_{c_Q}
&:=f(K^2-18K+55)+2c_uK(2K-9)\\
&=z(K^2-18K+55)
+2c_u(3K^2-27K+55).
\end{aligned}}
\tag{4.4}

直接展开得到 exact bridge

\[
\boxed{
f\mathscr S_0
=T\mathcal G_{c_Q}
-2(2K-9)R_+.}
\tag{4.5}

由 (3.6)：

\[
v_p(R_+)\ge2c.
\tag{4.6}

如果同一个 pure-`c_Q` prime 还进入 angle first layer，则 (1.5) 与 `B=-2N mod p` 给

\[
K^2\equiv8181N^2\pmod p.
\tag{4.7}

因为

\[
8181=3^4\cdot101,
\qquad 101\equiv1\pmod4,
\]
本文的 genuine non-`3` inert `p` 满足 `p\nmid K`。

此时 `p\nmid f`。否则 (3.1) 给

\[
R_+\equiv Tc_uK\not\equiv0\pmod p,
\]
与 (4.6) 冲突。

于是 (4.5) 在 `2c` 截断内可除以 `f,T`：

\[
\boxed{
\min\{v_p(\mathscr S_0),2c\}
=
\min\{v_p(\mathcal G_{c_Q}),2c\}.}
\tag{4.8}

结合 (4.3)：

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),2c\}
=
\min\{v_p(\mathcal G_{c_Q}),2c\}.}
\tag{4.9}

这一步把 pure-`c_Q` additive depth 中的 `a_3` 完全消掉；third block 只通过一个已经具有 `2c` square depth 的 `R_+` 余项出现。

---

## 5. pure-`c_Q` actual angle/additive depth matrix

令

\[
G_{\rm sp}
:=\gcd(\widehat{\mathcal O}_+,\widehat{\mathcal T}_2).
\]

由 (1.6) 与 (4.9)：

\[
\boxed{
\min\{v_p(G_{\rm sp}),2c\}
=
\min\{
 v_p(D_{\rm pref}),
 v_p(\mathcal G_{c_Q}),
 2c
\}.}
\tag{5.1}

所以 pure-`c_Q` odd common depth 已经从

\[
\text{angle conic}+\text{third block}+\text{sphere}+\text{height square}
\]

压成两个整数对象：

\[
\boxed{D_{\rm pref},\qquad\mathcal G_{c_Q}.}
\tag{5.2}

其中 `D_pref` 是 pure decimal prefix defect，`G_cQ` 只含 `(K,z,c_u,f)` 的 source-prefix data。

特别地，若

\[
v_p(D_{\rm pref})<2c
\]
产生 unsaturated angle odd depth，那么这个 prime 真正进入 `G_sp` 还必须让 `G_cQ` 至少同步到相同深度。局部 conic 的任意 Hensel lift已不足够。

---

# III. first-layer system is generically smooth

## 6. `G_{c_Q}=0` 对 source ratio 是线性的

在 pure-`c_Q` first layer，写

\[
\rho:=\frac z{c_u}.
\]
因为 `p\nmid zc_u`，`rho` 是单位。由 (4.4)：

\[
\boxed{
\frac{\mathcal G_{c_Q}}{c_u}
=
\rho A(K)+2C(K),}
\tag{6.1}

其中

\[
\boxed{A(K):=K^2-18K+55,}
\tag{6.2}

\[
\boxed{C(K):=3K^2-27K+55.}
\tag{6.3}

而 angle first layer由 (4.7) 读取：

\[
\boxed{F(K,N):=K^2-8181N^2=0.}
\tag{6.4}

只要 `A(K)` 是 unit，additive contact就唯一固定 source ratio：

\[
\boxed{
\rho
=-\frac{2C(K)}{A(K)}.}
\tag{6.5}

---

## 7. ratio-degenerate prime 只剩固定 `23`

计算

\[
\boxed{
\operatorname{Res}_K(A,2C)
=-5060
=-2^2\cdot5\cdot11\cdot23.}
\tag{7.1}

所以 genuine non-`3` inert prime中，`A=C=0` 只可能发生在

\[
p=11,23.
\]

逐个检查：

### `p=11`

共同根为

\[
K\equiv0\pmod{11}.
\]
但 (6.4) 右侧有

\[
8181\equiv8\not\equiv0\pmod{11},
\]
且 `N` 为 unit，所以 angle first layer不允许 `K=0`。因此

\[
\boxed{p=11\text{ 不进入 ratio-degenerate pure-}c_Q\text{ common system}.}
\tag{7.2}

### `p=23`

共同根为

\[
\boxed{K\equiv16\pmod{23}.}
\tag{7.3}

而

\[
8181\equiv16\pmod{23},
\qquad
16^2\equiv3\pmod{23},
\]
故 (6.4) 进一步要求

\[
\boxed{N^2\equiv16\pmod{23}.}
\tag{7.4}

`10` 在 `F_23^*` 中的 order 为 `22`，所以对 `N=10^M`：

\[
\boxed{
M\equiv5\text{ or }16\pmod{22}.}
\tag{7.5}

因此唯一 ratio-degenerate genuine inert exception 是一个固定 `23` decimal-length orbit；本文不在此宣称它为空。

---

## 8. 除固定 `23` 外，first-layer Jacobian 满秩

把 first-layer system写成

\[
F(K,N)=0,
\qquad
G(K,\rho)=\rho A(K)+2C(K)=0.
\]

对变量 `(K,rho)` 的 Jacobian determinant为

\[
\boxed{
J=2K\,A(K).}
\tag{8.1}

在 genuine non-`3` inert angle root上，§4 已说明 `K` 是 unit；§7 又说明除固定 `23` 外 `A(K)` 也是 unit。因此

\[
\boxed{
p\ne23
\Longrightarrow
J\not\equiv0\pmod p.}
\tag{8.2}

所以 pure-`c_Q` angle/additive first-layer common root 对所有 generic genuine inert prime都是二维 smooth root。它们若继续到高次，只能沿唯一 coupled Hensel lift传播，不存在新的 singular tree 或 quadratic branch。

---

## 9. 更新后的 pure-`c_Q` frontier

`spontaneous-angle-pair-cq-nogo.md` 留下的问题现在可以进一步精确化：

1. local angle conic 确实允许任意 unsaturated depth；
2. exact sphere 在 `Q_0` 退化层只恢复
   \[
   \omega(H_0-Y_3),\qquad\omega(H_0+Y_3),
   \]
   因此不提供新的 odd obstruction；
3. 若 prime 真正进入 A2 的 actual angle/additive common gcd，它还必须满足
   \[
   D_{\rm pref}\equiv0,
   \qquad
   \mathcal G_{c_Q}\equiv0,
   \]
   且其共同截断深度由 (5.1) 精确读取；
4. 除固定 `23` 的 `M=5,16 mod22` 长度轨道外，该二维 system 在 first layer 一律 smooth。

因此 pure-`c_Q` 的最后自由已经变成一个明确的 **simple relative-depth synchronization**：

\[
\boxed{
D_{\rm pref}
\quad\leftrightarrow\quad
\mathcal G_{c_Q}
\quad\text{inside the unique coupled Hensel orbit}.}
\tag{9.1}

下一步若继续这条线，应直接比较这两个 simple equations 的 normalized derivative / lifting depth，或单独封锁固定 `23` length orbit。继续追 generic sphere discriminant、height square character 或 conic singularity都不会增加约束。
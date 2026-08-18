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
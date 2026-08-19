# A2 height oversaturation 的 equal-depth resonance

> **依赖：** `spontaneous-height-oversaturation-depth-ledger.md`、`spontaneous-height-content-oversaturation.md`、`source-discriminant.md`、`primitive-reduction.md`。
>
> **严格状态：**前一 depth ledger 已证明 `e=v_p(omega)` 与 `h=v_p(W_q)` 不相等时，`J_H/B_W` 的较浅 residual oversaturation 被 `min(e,h)` 封顶。因此真正可能继续无界加深的只剩 `e=h`。本文把该 equal-depth branch 改写成两个自然整数 `A_H=g omega=z+c_u` 与 `B_H=qW_q=DK-N` 的 unit-ratio synchronization，并证明它对应的二次判别式恒为显式平方；所以 ordinary quadratic character / discriminant 不能再关闭该 branch。本文把剩余困难精确压成一个 projective unit ratio，不宣称 A2 closure。

---

## 1. equal-depth setting

固定 genuine non-`3` inert oversaturation prime `p`，令

\[
 e=v_p(\omega),
 \qquad
 h=v_p(W_q).
\]

本文只处理

\[
\boxed{e=h.}
\tag{1.1}
\]

写

\[
\omega=p^h\omega_0,
\qquad
W_q=p^hW_0,
\qquad
p\nmid\omega_0W_0.
\tag{1.2}
\]

于是原拼接 numerator

\[
\alpha=TK+a_3=\omega W_q
\]
满足精确赋值

\[
\boxed{v_p(\alpha)=2h.}
\tag{1.3}
\]

所以 equal-depth branch 的第一条硬结构是：指定 oversaturation prime 在真实 concatenated numerator 中形成一个**恰好偶深度的 p-primary block**。

---

## 2. 两个 natural height/content 线性形式具有同一深度

source triangle 为

\[
z=g\omega-c_u,
\qquad
f=g\omega+c_u,
\]
故

\[
\boxed{
g\omega=z+c_u.}
\tag{2.1}
\]

另有

\[
\boxed{qW_q=DK-N.}
\tag{2.2}
\]

定义

\[
\boxed{
A_H:=g\omega=z+c_u,
\qquad
B_H:=qW_q=DK-N.}
\tag{2.3}
\]

当前 prime 与 `gq` 分离，因此 (1.1) 等价于

\[
\boxed{
v_p(A_H)=v_p(B_H)=h.}
\tag{2.4}
\]

写

\[
A_H=p^hA_0,
\qquad
B_H=p^hB_0,
\qquad
p\nmid A_0B_0.
\tag{2.5}
\]

又因为 `alpha=omega W_q`：

\[
\boxed{A_HB_H=gq\alpha.}
\tag{2.6}
\]

因此 equal-depth 的两个 unit 并非独立：它们的乘积已经由真实 concatenated numerator 固定。

---

## 3. cross linear gate 变成唯一的 unit-ratio synchronization

前一文件的 cross gate 为

\[
L_{JB}=DzK+fN.
\]

利用

\[
f=z+2c_u,
\qquad
B_H=DK-N,
\qquad
A_H=z+c_u,
\]
直接展开：

\[
\begin{aligned}
L_{JB}
&=zDK+(z+2c_u)N\\
&=z(DK-N)+2N(z+c_u)\\
&=zB_H+2NA_H.
\end{aligned}
\]

所以有 exact identity

\[
\boxed{
L_{JB}=2NA_H+zB_H.}
\tag{3.1}
\]

定义 resonance depth

\[
\boxed{
\rho_p
:=v_p(2NA_0+zB_0)\ge0.}
\tag{3.2}
\]

则

\[
\boxed{v_p(L_{JB})=h+\rho_p.}
\tag{3.3}
\]

特别地，`rho_p>=r` 等价于唯一 projective ratio

\[
\boxed{
B_0\equiv-2Nz^{-1}A_0\pmod{p^r}.}
\tag{3.4}
\]

所以 equal-depth 的所有额外 Hensel 深化不再是一棵多分支系统：给定 `A_0` 后，`B_0` 的 unit class 被唯一确定。

---

## 4. resonance 与 `J_H/B_W` difference 的精确深度

前一 depth ledger 已得到

\[
5^{2d}
\left(
\widehat{\mathcal J}_H-(2^mg)^2\mathscr B_W
\right)
=-qzW_qL_{JB}.
\tag{4.1}
\]

由于 `p\nmid5qz`，结合 (3.3)：

\[
\boxed{
v_p\!\left(
\widehat{\mathcal J}_H-(2^mg)^2\mathscr B_W
\right)
=2h+\rho_p.}
\tag{4.2}
\]

这说明 equal-depth branch 中所有超出 generic `2h` 的 companion synchronization，都被**同一个** `rho_p` 精确读取。

---

## 5. `A_H,B_H,L_JB` 自带一个 exact square discriminant

由 (2.6) 与 (3.1)，把 `B_H` 消掉：

\[
A_H(L_{JB}-2NA_H)
=zA_HB_H
=zgq\alpha.
\]
因此

\[
\boxed{
2NA_H^2-L_{JB}A_H+zgq\alpha=0.}
\tag{5.1}
\]

把它看成关于 `A_H` 的 quadratic，判别式为

\[
\Delta_{\rm eq}
:=L_{JB}^2-8Nzgq\alpha.
\tag{5.2}
\]

但直接使用 (3.1)、(2.6)：

\[
\begin{aligned}
\Delta_{\rm eq}
&=(2NA_H+zB_H)^2-8NzA_HB_H\\
&=(2NA_H-zB_H)^2.
\end{aligned}
\]

所以得到 exact square identity

\[
\boxed{
L_{JB}^2-8Nzgq\alpha
=(2NA_H-zB_H)^2.}
\tag{5.3}
\]

这不是新 obstruction；它说明 equal-depth resonance 的 quadratic discriminant **全局就是平方**。

---

## 6. deep resonance 下 complementary linear form 恰停在 `h`

设

\[
\rho_p\ge1.
\]

由 (3.2)：

\[
2NA_0+zB_0\equiv0\pmod p.
\tag{6.1}
\]

定义 complementary form

\[
\boxed{M_{JB}:=2NA_H-zB_H.}
\tag{6.2}
\]

除以 `p^h` 后，利用 (6.1)：

\[
\frac{M_{JB}}{p^h}
=2NA_0-zB_0
\equiv4NA_0\not\equiv0\pmod p,
\]
因为 genuine prime 满足 `p\nmid2NA_0`。于是

\[
\boxed{v_p(M_{JB})=h
\qquad(\rho_p\ge1).}
\tag{6.3}
\]

因此 (5.3) 的右侧在 deep resonance 中赋值**精确**为 `2h`。

---

## 7. quadratic-character 路线在 equal-depth resonance 中自动退化

把 (5.3) 除以 `p^{2h}`，并令

\[
\alpha_0:=\alpha/p^{2h}.
\]

若 `rho_p>=1`，则模 `p` 有

\[
-8Nzgq\alpha_0
\equiv
\left(\frac{M_{JB}}{p^h}\right)^2
\equiv
(4NA_0)^2.
\tag{7.1}
\]

所以任何试图从 resonance 导出

\[
\left(\frac{-8Nzgq\alpha_0}{p}\right)=-1
\]
的 ordinary discriminant obstruction 都不可能成立；实际恒有

\[
\boxed{
\left(\frac{-8Nzgq\alpha_0}{p}\right)=1.}
\tag{7.2}
\]

而且这个 square class 已由 (3.4) 的 unit ratio自动解释，不是独立条件。

因此：

\[
\boxed{
\text{equal-depth resonance}
\Longrightarrow
\text{projective unit synchronization, not a new quadratic character}.}
\tag{7.3}
\]

---

## 8. 当前 equal-depth frontier

综合 §§1–7，真正剩余的 branch 已压成

\[
\boxed{
\begin{gathered}
p\equiv7,11\pmod{24},\\
v_p(\omega)=v_p(W_q)=h\ge1,\\
v_p(\alpha)=2h,\\
v_p(g\omega)=v_p(qW_q)=h,\\
B_0/A_0
\equiv-2Nz^{-1}\pmod{p^{\rho_p}},\\
v_p\!\left(
\widehat{\mathcal J}_H-(2^mg)^2\mathscr B_W
\right)=2h+\rho_p.
\end{gathered}}
\tag{8.1}
\]

同时 (5.3) 已证明 discriminant/Legendre 方向只是平方 shadow。

所以后续真正可能推进 closure 的输入只能来自：

1. 把 ratio (3.4) 与 decimal determinant `K b_3-Q a_3` 联立；
2. 把 `A_H=z+c_u`、`B_H=DK-N` 的单位代表与 endpoint Hensel slot 的**自然代表大小**联立；
3. 或证明 `alpha=TK+a_3` 的 exact square p-primary depth `2h` 与第三块窄窗不相容。

继续 ordinary quadratic character、判别式或重复 simple-root Hensel 不会产生新 closure。

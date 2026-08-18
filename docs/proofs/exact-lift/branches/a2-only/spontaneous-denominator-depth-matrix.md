# A2 denominator parity 的纯 prefix depth matrix

> **依赖：** `spontaneous-angle-overlap-depth.md`、`spontaneous-denominator-common.md`、`endpoint-lattice.md` §§16.56、16.68–16.70。
>
> **严格状态：**本文把 angle/additive 两侧的 denominator prime-power depth 统一降成三个 pure-prefix objects：`Delta_0`、`P_q(K)=K^2-26`、`P_f(K)=3K^2-36K+26`。q-side additive reduction来自旧 (16.412q)；f-side在旧 `Psi_f` reduction基础上进一步使用真实 sphere，把 `Psi_f` 也降成固定 K-quadratic。两个 additive quadratics 对所有 genuine non-3 inert prime 都是 simple-root。本文还给出 q-side 的 exact decimal-length三项 bridge，并审计 common channel 上旧 residual Legendre characters 都只是 sphere-square shadow。最后的 parity equality 尚未证明，所以 A2 仍未全局关闭。

---

## 1. angle side：denominator 截断深度统一由 `Delta_0` 读取

设 genuine non-`3` inert prime

\[
p^e\Vert qf,
\qquad e\ge1.
\]

`spontaneous-angle-overlap-depth.md` 已证明：

### q-side

因为

\[
v_p(q)=v_p(x+2)=e,
\]
且

\[
\Omega_{\rm sp}
=400r_s\Delta_0+(x+2)J_q,
\]
共同 first-layer root 上 `J_q` 为单位，所以

\[
\boxed{
\min\{v_p(\Omega_{\rm sp}),e\}
=
\min\{v_p(\Delta_0),e\}.}
\tag{1.1q}
\]

### f-side

由 exact Bezout

\[
(x+2)\Omega_{\rm sp}-A_{\rm sp}F_f
=-200x^3\Delta_0,
\]
以及

\[
v_p(F_f)=v_p(f)=e,
\]
得到

\[
\boxed{
\min\{v_p(\Omega_{\rm sp}),e\}
=
\min\{v_p(\Delta_0),e\}.}
\tag{1.1f}
\]

对 genuine denominator prime，`Omega_sp` 与 primitive integer `widehat(O)_sp` 只差 odd p-adic unit 和固定 2-power，因此可以统一写成

\[
\boxed{
\min\{v_p(\widehat{\mathcal O}_{\rm sp}),e\}
=
\min\{v_p(\Delta_0),e\}.}
\tag{1.2}
\]

也就是说 angle denominator projection 与 q/f 来源无关：两侧都只读同一个 prefix defect `Delta_0`。

---

## 2. additive q-side：旧 saturation reduction 已经是固定 quadratic

定义

\[
\boxed{\mathcal P_q(K):=K^2-26.}
\tag{2.1}
\]

`endpoint-lattice.md` (16.412q) 已严格证明，在完整 saturation

\[
p^e\Vert q,
\qquad
p^e\mid\mathscr L_{23}
\]
下：

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),e\}
=
\min\{v_p(\mathcal P_q(K)),e\}.}
\tag{2.2}
\]

所以 q-side additive denominator depth 已完全 source-free。

其 discriminant 为

\[
\operatorname{Disc}(\mathcal P_q)=104=2^3\cdot13.
\tag{2.3}
\]

唯一 odd ramified prime `13` 为 `1 mod 4`。故

\[
\boxed{
\text{对 genuine non-3 inert prime，q-side additive K-root 永远 simple。}}
\tag{2.4}

---

## 3. `已严格完成`：f-side sphere 在完整 saturation 深度内产生第二个固定 quadratic

旧 (16.408) 已有

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),e\}
=
\min\{v_p(\Psi_f),e\}
\qquad
(p^e\Vert f,\ p^e\mid\mathscr L_{23}).}
\tag{3.1}

现在进一步消去 `Psi_f`。

使用 normalized variables

\[
x=B/N,
\quad y=a_2/10^{M-1},
\quad \tau=N^{-1},
\quad s=K/N,
\]

\[
\bar w=b_3/(TN),
\qquad
\bar\zeta=a_3/(TN),
\]
其中 `N=10^M`。

对 `p^e || f`，source exact line 给

\[
2\bar w+x+2\equiv0\pmod{p^e}.
\tag{3.2}

saturation 给

\[
2\bar\zeta+9\tau\equiv0\pmod{p^e}.
\tag{3.3}

把 exact sphere 的 cleared polynomial记为

\[
\begin{aligned}
\mathscr S_{100}:={}&100x^2\bar w^2(s+\bar\zeta)^2\\
&-(x+2+\bar w)^2
\left[(2025x^2+y^2)\bar w^2+100x^2\bar\zeta^2\right].
\end{aligned}
\tag{3.4}
\]

真实 solution 满足 `S_100=0`。在多项式环 `Z[1/2][x,y,tau,w,z]` 中，对两个线性 ideal generators

\[
2\bar w+x+2,
\qquad
2\bar\zeta+9\tau
\]
取余，得到

\[
\boxed{
16\mathscr S_{100}
\equiv
(x+2)^2\mathscr R_f^{\rm sph}
\pmod{(2\bar w+x+2,\,2\bar\zeta+9\tau)},}
\tag{3.5}
\]

其中

\[
\boxed{
\mathscr R_f^{\rm sph}
:=400x^2s(s-9\tau)
-(2025x^2+y^2)(x+2)^2.}
\tag{3.6}

对 genuine f-prime，`2(x+2)` 为单位；由 (3.2)–(3.5)：

\[
\boxed{p^e\mid\mathscr R_f^{\rm sph}.}
\tag{3.7}

乘回原始 decimal blocks，(3.6) 与

\[
\mathscr R_{f,\rm int}^{\rm sph}
:=4B^2K(K-9)-Q^2N_0
\]
只差 p-adic unit `100/N^4`，故

\[
\boxed{
p^e\mid
\left[Q^2N_0-4B^2K(K-9)\right].}
\tag{3.8}

---

## 4. `已严格完成`：f-side `Psi_f` 截断深度等于固定 quadratic 深度

定义

\[
\boxed{
\mathcal P_f(K):=3K^2-36K+26.}
\tag{4.1}

存在 exact integer identity

\[
\boxed{
\Psi_f
+\left[Q^2N_0-4B^2K(K-9)\right]
=-B^2\mathcal P_f(K).}
\tag{4.2}

因为 genuine f-prime 满足 `p \nmid B`，结合 (3.8)：

\[
\boxed{
\min\{v_p(\Psi_f),e\}
=
\min\{v_p(\mathcal P_f(K)),e\}.}
\tag{4.3}

再与旧 (3.1) 合并：

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),e\}
=
\min\{v_p(\mathcal P_f(K)),e\}
\qquad
(p^e\Vert f,\ p^e\mid\mathscr L_{23}).}
\tag{4.4}

所以 f-side additive denominator depth 也彻底变成 pure K-quadratic；`Psi_f` 只保留为旧接口，不再是最终规范对象。

其 discriminant 为

\[
\boxed{
\operatorname{Disc}(\mathcal P_f)
=984=2^3\cdot3\cdot41.}
\tag{4.5}

唯一 non-`3` odd ramified prime `41` 为 `1 mod 4`。因此

\[
\boxed{
\text{对 genuine non-3 inert prime，f-side additive K-root 永远 simple。}}
\tag{4.6}

---

## 5. denominator depth matrix

综合 §§1–4，完整 saturation 内的规范对象只有

\[
\boxed{
\begin{array}{c|cc}
&\text{angle side}&\text{additive side}\\ \hline
q&\Delta_0&\mathcal P_q(K)=K^2-26\\[1mm]
f&\Delta_0&\mathcal P_f(K)=3K^2-36K+26.
\end{array}}
\tag{5.1}

逐 prime-power 截断赋值为

\[
\boxed{
\begin{aligned}
a_p&:=\min\{v_p(\widehat{\mathcal O}_{\rm sp}),e\}
=\min\{v_p(\Delta_0),e\},\\
t_p^{(q)}&:=\min\{v_p(\widehat{\mathcal T}_2),e\}
=\min\{v_p(\mathcal P_q(K)),e\},\\
t_p^{(f)}&:=\min\{v_p(\widehat{\mathcal T}_2),e\}
=\min\{v_p(\mathcal P_f(K)),e\}.
\end{aligned}}
\tag{5.2}

因此 denominator residual parity 已不再依赖 source ratios、third-block Hensel roots 或 curvature discriminants；它只取决于 `Delta_0` 与两个 simple K-roots 的 depth difference。

---

## 6. `已严格完成`：q-side depth mismatch 被一个 simple decimal-length target控制

有 exact identity

\[
\boxed{
\mathcal P_q(K)+N^2\Delta_0
-\left(8181N^2-26\right)
=Q(2025Q-8100N).}
\tag{6.1}

证明只需使用

\[
K=N(9+y),
\qquad
Q=N(x+2).
\]

若 `p^e || q` 且 genuine `p \nmid c_Q`，则

\[
v_p(Q)=e.
\]
所以模 `p^e`：

\[
\boxed{
\mathcal P_q(K)+N^2\Delta_0
\equiv
\mathcal R_q(N)
:=8181N^2-26
\pmod{p^e}.}
\tag{6.2}

`N^2` 是平方单位。于是令

\[
a=v_p(\mathcal P_q),
\quad d=v_p(\Delta_0),
\quad r=v_p(\mathcal R_q),
\]
并截断到 `e` 后，三者满足 ultrametric triangle：若最小深度小于 `e`，它不可能只出现一次。

特别地：

\[
\boxed{
\begin{aligned}
a<d,\ a<e&\Longrightarrow r=a,\\
d<a,\ d<e&\Longrightarrow r=d.
\end{aligned}}
\tag{6.3}

所以 q-side angle/additive depth 若不相等，较浅的那个 depth 必精确出现在 fixed decimal-length integer `R_q(N)` 中。

而

\[
\mathcal R_q'(N)=2\cdot8181N,
\qquad
\gcd(8181,26)=1,
\]
已证明 `R_q` 对所有 genuine odd prime 都没有 repeated root。因此 q-side parity mismatch 也只能沿 simple decimal-length Hensel orbit 传播，不存在新的 singular length tree。

---

## 7. `审计 / no-go`：common q-character 是 sphere-square shadow

若同一个 saturated q-prime还属于 angle common channel，则

\[
x=-2,
\qquad
\Delta_0=0,
\qquad
\bar\zeta=-\frac92\tau.
\]

在 exact sphere 中，`x+2=0` 后直接得到

\[
(2025x^2+y^2)\bar w^2
=400s(s-9\tau).
\]
乘回 `N_0=N^2(2025x^2+y^2)/100`：

\[
\boxed{
N_0\bar w^2
=4K(K-9)
\pmod p.}
\tag{7.1}

因此

\[
\boxed{
\left(\frac{N_0}{p}\right)
=
\left(\frac{K(K-9)}p\right).}
\tag{7.2}

这正是 `endpoint-lattice.md` (16.384) 的 q-side residual-unit character。也就是说一旦 prime 已进入 angle/additive common sphere，旧 q-character 自动由 square identity (7.1) 满足；它不能再被计作 independent obstruction。

---

## 8. `审计 / no-go`：common f-character 同样自动

对 saturated f-common prime，§3 的 sphere congruence给

\[
Q^2N_0
\equiv4B^2K(K-9).
\]
所以

\[
\boxed{
\left(\frac{N_0}{p}\right)
=
\left(\frac{K(K-9)}p\right).}
\tag{8.1}

而 additive f-root `P_f(K)=0` 等价于

\[
\boxed{K^2-26=4K(K-9).}
\tag{8.2}

因此

\[
\boxed{
\left(\frac{K^2-26}{p}\right)
=
\left(\frac{N_0}{p}\right).}
\tag{8.3}

这正是旧 (16.396) 的 generic f-prefix character。故 f-common channel 中该 character 也只是 sphere-square shadow。

结论与 q-side 一致：**不能再靠叠加旧 denominator Legendre characters 关闭 common branch。** 真正剩余的是 prime-power depth equality / decimal orbit，而不是 first-layer quadratic character。

---

## 9. 对 `G_sp` parity dichotomy 的更新

`spontaneous-angle-parity.md` 的 residual denominator 问题现在可以精确改写为：对每个 saturated inert primary `p^e || qf`，比较

\[
\boxed{
\min(v_p(\Delta_0),e)
}

与

\[
\boxed{
\begin{cases}
\min(v_p(K^2-26),e),&p\mid q,\\
\min(v_p(3K^2-36K+26),e),&p\mid f.
\end{cases}}
\tag{9.1}

三个对象的 genuine inert roots全部 simple。repeated spontaneous 与 saturated denominator 的交集又已经由 `spontaneous-denominator-repeated-common.md` 关闭。

因此 denominator pool 现在只剩一个真正开放机制：

\[
\boxed{
\text{simple-root depth mismatch / equal-depth normalized cancellation}.}
\tag{9.2}

若后续能证明 (9.1) 两侧的 parity difference 对所有 denominator primary 都为偶，则 `G_sp = 1 mod 4` 分支中的 residual odd supplier 将不能来自 denominator pool；届时只剩 `spontaneous-source-equal-depth.md` 的 source normalized gate 与 pure spontaneous external channel。

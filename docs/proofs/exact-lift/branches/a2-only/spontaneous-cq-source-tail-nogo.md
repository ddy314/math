# A2 pure-`c_Q` fixed-`23` 的 source/tail Hensel quotient no-go

> **依赖：** `core.md` §§12.5–12.7、`source-discriminant.md`、`spontaneous-cq-relative-depth-nogo.md`。
>
> **严格状态：**`spontaneous-cq-relative-depth-nogo.md` 已把 fixed `23` 的 depth `>=2` compatibility 压成 prefix correction `kappa` 与 source ratio `rho=z/c_u` 的同步，并把 `v_23(c_Q)=1` 写成 normalized tail `gamma=(c_Qc_u)/23` 的同余。本文检查最自然的下一步：是否能使用 core 的 Hensel quotients `omega,theta` 再独立固定 `gamma` 或 `rho`。结论是否定的。reflection 下，`theta` 方程与 `c_Q omega-theta` 方程都由 source split 与 source triangle 精确推出；normalized `23` tail bridge也只是 denominator-ratio identity 的重写。因此 source/tail quotient 层没有新的独立 mod-`23` obstruction。后续必须引入 canonical factor allocation、finite-defect/rational-root 或其他 natural representative。

---

## 1. reflection source identities

固定当前 reflection endpoint，使用不会与 source ratio 混淆的记号

\[
D_0:=2^m g.
\]

core/source split 为

\[
\boxed{
c_Qq=5^M+D_0c_u.}
\tag{1.1}

`source-discriminant.md` 的 source triangle 等价于

\[
\boxed{
g\omega=5^\lambda q+c_u.}
\tag{1.2}

因为

\[
z=q5^\lambda=g\omega-c_u.
\]

core §12.7 还记录两个 Hensel quotient identities：

\[
\boxed{
g\theta=5^{M+\lambda}+c_Qc_u,}
\tag{1.3}

\[
\boxed{
c_Q\omega-\theta=2^m5^\lambda c_u.}
\tag{1.4}

本文证明 (1.3)–(1.4) 不独立。

---

## 2. `已严格完成`：`theta` 可由 source split + source triangle 消掉

由 (1.2)：

\[
gc_Q\omega
=c_Q5^\lambda q+c_Qc_u.
\]

再由 (1.1)：

\[
c_Q5^\lambda q
=5^\lambda(5^M+D_0c_u)
=5^{M+\lambda}+5^\lambda D_0c_u.
\]

因此

\[
\boxed{
gc_Q\omega
=5^{M+\lambda}+5^\lambda D_0c_u+c_Qc_u.}
\tag{2.1}

又 `D_0=2^mg`，所以

\[
5^\lambda D_0c_u
=g\,2^m5^\lambda c_u.
\]

移项：

\[
\boxed{
g(c_Q\omega-2^m5^\lambda c_u)
=5^{M+\lambda}+c_Qc_u.}
\tag{2.2}

定义

\[
\theta:=c_Q\omega-2^m5^\lambda c_u.
\]
就同时得到

\[
\boxed{c_Q\omega-\theta=2^m5^\lambda c_u}
\]
和

\[
\boxed{g\theta=5^{M+\lambda}+c_Qc_u.}
\]

也就是说：

\[
\boxed{(1.1)+(1.2)\Longrightarrow(1.3)+(1.4).}
\tag{2.3}

core 的 `theta` 并没有提供第三条独立 source/tail equation。

---

## 3. converse dependency

反过来，若保留 (1.2)、(1.3)、(1.4)，则

\[
\begin{aligned}
g\theta
&=gc_Q\omega-g2^m5^\lambda c_u\\
&=c_Q(5^\lambda q+c_u)-D_05^\lambda c_u\\
&=5^\lambda(c_Qq-D_0c_u)+c_Qc_u.
\end{aligned}
\]

与 (1.3) 比较并约去 `c_Qc_u`：

\[
5^\lambda(c_Qq-D_0c_u)=5^{M+\lambda},
\]
故

\[
\boxed{c_Qq=5^M+D_0c_u.}
\tag{3.1}

所以四个方程的独立秩只有两条；任何三条都会恢复第四条。尤其不能把 `theta` 当成新的 mod-`23` gate 再收费。

---

## 4. normalized fixed-`23` tail bridge同样是 shadow

固定

\[
h:=v_{23}(c_Q)\ge1,
\]
并定义

\[
\widetilde Q:=\frac{Q}{23^h},
\qquad
\widetilde c:=\frac{c_Qc_u}{23^h},
\qquad
\rho:=\frac{q5^\lambda}{c_u}.
\]

由真实 denominator formulas

\[
Q=2^{M+1}c_Qq
\]
直接有

\[
\boxed{
5^\lambda\widetilde Q
=2^{M+1}\rho\widetilde c.}
\tag{4.1}

若 `h=1`，写

\[
q_1:=Q/23,
\qquad
\gamma:=(c_Qc_u)/23,
\]
则

\[
\boxed{
\gamma\rho
=\frac{5^\lambda q_1}{2^{M+1}}.}
\tag{4.2}

另一方面 `source-discriminant.md` 已有

\[
b_3z=Tc_uQ.
\]
利用

\[
b_3=2^{M+m+1}5^dc_Qc_u,
\qquad
z=q5^\lambda,
\qquad
\lambda=m-d,
\]
约去同一组因子，恰好重新得到 (4.1)。

因此

\[
\boxed{
\text{normalized tail bridge}
=\text{real denominator-ratio identity 的逐 }23^h\text{ 约分。}}
\tag{4.3}

它非常适合作为坐标转换，但不是独立 obstruction。

---

## 5. 对 fixed `23` synchronization 的影响

`spontaneous-cq-relative-depth-nogo.md` 已给 depth `>=2` 的两个等价接口：

\[
\kappa_{\rm pref}(M,q_1)=\kappa_\sigma(\rho),
\tag{5.1}
\]

或在 `h=1` 时写成

\[
\gamma\equiv\Gamma_\sigma(M,q_1,\lambda,\kappa)\pmod{23}.
\tag{5.2}

本文证明：把 core 的 `omega,theta` 方程加入 (5.2) 后，不会产生第二个关于 `gamma` 的同余，因为它们精确退化回 (1.1)、(1.2)、(4.2)。

所以以下路线必须降级：

1. 再对 `theta` 做 mod `23` / mod `23^2` 消元；
2. 把 `c_Qomega-theta` 当成独立 linear gate；
3. 用 `b_3z=Tc_uQ` 与 (4.2) 制造两个看似不同的 tail 条件。

它们都是同一 source/denominator identity 的不同坐标。

---

## 6. 更新后的真正开放核

fixed `23` 的局部和 source quotient 自由现在都已经审计清楚：

- first layer singularity 经一次 blow-up 后恢复 smooth；
- additive second layer只是 `kappa <-> rho` 的 Möbius chart；
- `theta` 与 normalized tail bridge没有新增独立约束。

因此若要继续封锁 pure-`c_Q` odd depth，必须加入一个**不属于 source quotient 闭包**的对象。当前规范候选为：

\[
\boxed{
\begin{array}{l}
\text{canonical factors }H_0\pm Y_3=c_\pm^2(5^\lambda X\text{ or }Y),\\
\text{finite-defect / rational-root integer }F(J),\ \Xi_C,\ \Delta_\pm,\\
\text{或其他具有独立 sign/height 的 natural representative.}
\end{array}}
\tag{6.1}

下一步若继续 fixed `23`，应直接把 `kappa_pref=kappa_sigma(rho)` 与其中一类对象联立；继续 source Hensel quotient algebra 已经没有新增信息。

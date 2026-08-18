# A2 height companion oversaturation 回流到 `omega` content

> **依赖：** `spontaneous-height-resultant-parity.md`、`spontaneous-height-companion-cross.md`、`primitive-reduction.md`、`source-discriminant.md`。
>
> **严格状态：**本文处理一个比 first-layer common height 更深的交叉情形：某 prime 的 `W_q` height exponent 已被共同 gcd `D_H` 完整吃掉，但 `J_H` 与 `B_W` 两个 companion 在该 prime上仍同时继续加深。利用 cross linear gate与 `qW_q=DK-N`，证明这种 oversaturation必强迫 `p|omega`；于是 `B_W` 在 source triangle 上退化为固定 quadratic `6K^2-36K+55`。该 quadratic 对所有 non-`3` odd primes均 simple，其 inert character又只是 `D_W mod omega` 的已有 shadow。因此 height-supported companion oversaturation不是 generic external mechanism，而是一个 simple omega-content orbit。本文不排除所有 simple omega roots，也不关闭 A2。

---

## 1. oversaturation setting

令

\[
D_H=\gcd(\mathscr B_W,W_q)=\gcd(\widehat J_H,W_q),
\]

\[
B^\circ=\mathscr B_W/D_H,
\qquad
J^\circ=\widehat J_H/D_H,
\qquad
W^\circ=W_q/D_H.
\]

固定 genuine non-`3` inert prime `p`，并假设：

1. `p|W_q`，所以它是真正 height-supported prime；
2. `p|B^circ`；
3. `p|J^circ`。

由于 `D_H` 已经是 `B_W` 与 `W_q` 的完整 gcd，`p|B^circ` 强迫 `D_H` 在 p 上已经吃掉 `W_q` 的全部 exponent。因此

\[
\boxed{p\nmid W^\circ.}
\tag{1.1}
\]

`spontaneous-height-companion-cross.md` 的 difference identity于是给 cross linear gate

\[
\boxed{L_{JB}:=DzK+fN\equiv0\pmod p,}
\tag{1.2}
\]

在 genuine external/content-free denominator separation下 `p\nmid qz`。

---

## 2. `L_JB` modulo `W_q` 精确回到 `omega K`

使用

\[
qW_q=DK-N,
\qquad
z=g\omega-c_u,
\qquad
f=g\omega+c_u.
\]

有 exact Euclidean identity

\[
\begin{aligned}
L_{JB}
&=DzK+f(DK-qW_q)\\
&=DK(z+f)-fqW_q\\
&=2Dg\omega K-fqW_q.
\end{aligned}
\]

所以

\[
\boxed{
L_{JB}=2Dg\omega K-fqW_q.}
\tag{2.1}
\]

若 `p|W_q` 且 `p|L_JB`：

\[
\boxed{p\mid2Dg\omega K.}
\tag{2.2}
\]

`primitive-reduction.md` 已证明 genuine non-`3` height prime满足

\[
p\nmid2\cdot5\cdot g,
\]
故 `p\nmid D`。它还满足 `p\nmid a_3`。而

\[
TK+a_3=\omega W_q\equiv0\pmod p.
\]
若 `p|K`，则上式会给 `p|a_3`，矛盾。因此

\[
\boxed{p\nmid K.}
\tag{2.3}
\]

由 (2.2)：

\[
\boxed{p\mid\omega.}
\tag{2.4}
\]

所以 height-supported `J^circ/B^circ` oversaturation不能留在 generic endpoint-external pool；它必回到 concatenation content `omega`。

---

## 3. `B_W` 在 omega-content 上退化为固定 quadratic

由 source triangle，模 `p|omega`：

\[
z=g\omega-c_u\equiv-c_u,
\]

\[
f=g\omega+c_u\equiv c_u.
\tag{3.1}
\]

而

\[
\mathscr B_W
=c_u^2(5K^2-36K+55)+z^2K^2.
\]

所以

\[
\boxed{
\mathscr B_W
\equiv
c_u^2(6K^2-36K+55)
\pmod p.}
\tag{3.2}
\]

height prime与 `c_u` 分离，因此 `p|B_W` 等价于

\[
\boxed{
\mathcal P_{\omega H}(K)
:=6K^2-36K+55
\equiv0\pmod p.}
\tag{3.3}
\]

这是一条完全 source-ratio-free 的固定 K-quadratic。

---

## 4. 所有 non-3 roots 都是 simple

其 discriminant为

\[
\boxed{
\operatorname{Disc}(\mathcal P_{\omega H})
=(-36)^2-4\cdot6\cdot55
=-24.}
\tag{4.1}
\]

因此 repeated root只可能出现在

\[
p\mid24,
\]
即 `p=2` 或 `3`。所以

\[
\boxed{
\text{对所有 genuine non-`3` odd primes，}
\mathcal P_{\omega H}\text{ 的 root 都是 simple。}}
\tag{4.2}
\]

height-supported companion oversaturation因此不存在新的 singular Hensel tree。

---

## 5. inert quadratic character只是 source-discriminant shadow

对

\[
p\equiv3\pmod4,
\quad p\ne3,
\]
(3.3) 有 root iff

\[
\left(\frac{-24}{p}\right)=1.
\]
因为 `4` 为平方且 `(-1/p)=-1`：

\[
\boxed{
\left(\frac6p\right)=-1.}
\tag{5.1}
\]

另一方面 `source-discriminant.md` 给

\[
\mathscr D_W=55z^2-49c_u^2.
\]
模 `omega` 有 `z=-c_u`，因此

\[
\boxed{
\mathscr D_W\equiv6c_u^2\pmod\omega.}
\tag{5.2}
\]

所以对 `p|omega`：

\[
\boxed{
\left(\frac{\mathscr D_W}{p}\right)
=\left(\frac6p\right)=-1.}
\tag{5.3}
\]

这正是一般 external `B_W` root已有的 discriminant nonresidue condition。故 (5.1) 不是新的 independent character；它只是 source triangle在 omega-content上的投影。

---

## 6. updated height cross ledger

height `J/B` cross-overlap现在严格分成两类：

### A. `p\nmid W_q`

这是 `spontaneous-height-companion-cross.md` 的 generic residual overlap：

\[
\mathscr B_W=0,
\quad
DzK+fN=0,
\quad
\mathscr R_{JB}=0,
\]

只剩 positive norm / simple p-adic synchronization。

### B. `p\mid W_q`

若 height exponent已经被 `D_H` 完整吃掉后 `J^circ,B^circ` 仍共同加深，则

\[
\boxed{p\mid\omega,}
\]
并且

\[
\boxed{6K^2-36K+55=0\pmod p}
\]
是 simple fixed quadratic。

因此

\[
\boxed{
\text{height-supported companion oversaturation}
\Longrightarrow
\text{simple omega-content orbit}.}
\tag{6.1}
\]

没有第三种 hidden prime-source mechanism。

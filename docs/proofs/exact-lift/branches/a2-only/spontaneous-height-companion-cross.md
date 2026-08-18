# A2 `J_H` / `B_W` residual cross-overlap 的 linear gate 与 positive norm

> **依赖：** `spontaneous-height-resultant-parity.md`、`source-discriminant.md`、`height-cofactor.md`。
>
> **严格状态：**本文研究从共同 height gcd `D_H` 中约去以后，pure-decimal companion `J^circ` 与 source-side resultant companion `B^circ` 能否再次共享 odd prime。利用前一文件的 exact difference，generic external overlap首先被压到线性 K-gate `DzK+fN=0`；再与 `B_W=0` 消去 K，得到 positive definite quadratic `R_JB`，其 discriminant恰为 `-4 D^2 c_u^2 f^2 z^2 D_W`。因此所有 simple cross-overlap只重复 `B_W` 已有的 source-discriminant square class；没有第二个 independent Legendre obstruction，也没有实根。本文不排除 simple p-adic roots，不关闭 A2。

---

## 1. 从 common height part 中约去

定义

\[
D_H=\gcd(\widehat J_H,W_q)=\gcd(\mathscr B_W,W_q),
\]

\[
J^\circ:=\widehat J_H/D_H,
\qquad
B^\circ:=\mathscr B_W/D_H,
\qquad
W^\circ:=W_q/D_H.
\]

于是

\[
\boxed{
\gcd(J^\circ,W^\circ)=
\gcd(B^\circ,W^\circ)=1.}
\tag{1.1}
\]

前一文件 (6.1) 除以 `D_H` 后给

\[
\begin{aligned}
5^{2d}J^\circ
-2^{2m}5^{2d}g^2B^\circ
={}&q^2W^\circ\Bigl[
(g^2\omega^2-c_u^2)W_q\\
&\qquad -2g^2\omega TK
\Bigr].
\end{aligned}
\tag{1.2}

因此若 odd prime `p` 同时满足

\[
p\mid J^\circ,\qquad p\mid B^\circ,
\]
则由 (1.1)，`p\nmid W^circ`。在 genuine external channel再假设

\[
p\nmid q,
\]
就必须有

\[
\boxed{
(g^2\omega^2-c_u^2)W_q
-2g^2\omega TK
\equiv0\pmod p.}
\tag{1.3}
\]

---

## 2. bracket 精确化成 linear K-gate

沿用 source triangle

\[
z:=q5^\lambda=g\omega-c_u,
\qquad
f=g\omega+c_u,
\]
所以

\[
\boxed{g^2\omega^2-c_u^2=zf.}
\tag{2.1}
\]

另有

\[
qW_q=DK-N,
\qquad
D=g2^m5^d,
\qquad
T=2^m5^{d+\lambda}.
\]

直接展开：

\[
\boxed{
q\Bigl[
(g^2\omega^2-c_u^2)W_q-2g^2\omega TK
\Bigr]
=-z(DzK+fN).}
\tag{2.2}
\]

因此 genuine `p\nmid qz` external overlap满足真正的一次条件

\[
\boxed{DzK+fN\equiv0\pmod p.}
\tag{2.3}
\]

这里

\[
N=3D-C=c_-^2X>0
\]
是 canonical height-side integer；不要与 decimal `10^M` 混淆。

所以 `J^circ/B^circ` overlap并不是新的三变量 Hensel system：K 坐标已被一条 unit-slope linear equation固定。

---

## 3. 消掉 K 得到显式 positive norm

写

\[
A_W:=5c_u^2+z^2,
\]

\[
\mathscr B_W
=A_WK^2-36c_u^2K+55c_u^2.
\]

对 K 求 resultant：

\[
\boxed{
\operatorname{Res}_K(
\mathscr B_W,\ DzK+fN
)
=
\mathscr R_{JB},}
\tag{3.1}
\]

其中

\[
\boxed{
\begin{aligned}
\mathscr R_{JB}:={}&
55D^2c_u^2z^2
+36DNc_u^2fz\\
&+N^2f^2(5c_u^2+z^2).
\end{aligned}}
\tag{3.2}
\]

所有显示量在真实 endpoint 中均正，因此立刻有

\[
\boxed{\mathscr R_{JB}>0.}
\tag{3.3}
\]

更强的是 exact completion：

\[
\boxed{
A_W\mathscr R_{JB}
=
(A_WfN+18Dc_u^2z)^2
+D^2c_u^2z^2\mathscr D_W,}
\tag{3.4}
\]

其中

\[
\mathscr D_W=55z^2-49c_u^2>0.
\]

所以该 cross-resultant 是严格 positive definite 的 source norm；它在真实轴上不存在任何 zero / near-sign-change mechanism。

---

## 4. discriminant 只是旧 source-discriminant shadow

把 (3.2) 看成 N 的 quadratic。其 discriminant exact 为

\[
\boxed{
\operatorname{Disc}_N(\mathscr R_{JB})
=-4D^2c_u^2f^2z^2\mathscr D_W.}
\tag{4.1}
\]

所以对 genuine odd inert prime

\[
p\equiv3\pmod4,
\qquad
p\nmid2D c_u fz\mathscr D_W,
\]
若 `R_JB=0 mod p` 有 root，必要且充分的 quadratic character是

\[
\left(\frac{-\mathscr D_W}{p}\right)=1.
\]
由于 `(-1/p)=-1`：

\[
\boxed{
\left(\frac{\mathscr D_W}{p}\right)=-1.}
\tag{4.2}
\]

但这正是 `B_W(K)=0` 在 nonzero-discriminant external height channel中的已有 square-class condition。故 (4.2) 只是同一 quadratic extension的 shadow，不能作为第二个 Legendre obstruction收费。

若

\[
p\mid\mathscr D_W,
\]
则进入已经单列的 external double-root / source-discriminant channel；本文不重复其 linear-decimal audit。

---

## 5. cross-companion frontier

因此 generic `J^circ/B^circ` common prime必须依次满足

\[
\boxed{
\mathscr B_W(K)=0,
\qquad
DzK+fN=0,
\qquad
\mathscr R_{JB}=0.}
\tag{5.1}

其中：

- 第二式线性固定 K；
- 第三式是 positive norm；
- nonzero-discriminant root只使用 `B_W` 原有的 square class；
- discriminant-zero branch回流到已知 `D_W=0` external double root。

所以这条 cross-pair不能通过继续叠 quadratic character关闭。它的剩余自由也是 **simple p-adic/natural-representative synchronization**。

这给 global parity ledger一个重要 no-go：即使 `J^circ` 与 `B^circ` 都携带 odd inert parity，也不能仅凭各自的 quadratic character证明二者不能由同一 generic prime承担。真正的新输入必须来自 linear gate (2.3) 的 decimal/height orbit或 size。

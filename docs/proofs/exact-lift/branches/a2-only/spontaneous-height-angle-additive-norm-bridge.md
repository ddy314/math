# A2 moving height angle-norm / additive 的 universal exact bridge

> **依赖：** `spontaneous-height-parity-ledger.md`、`spontaneous-height-resultant-parity.md`、`height-cofactor.md`、`spontaneous-height-moving-singular-nogo.md`。
>
> **严格状态：**本文给两张 moving height orientations 一个共同的高阶接口。把 angle-height norm `H_O` 与 additive-height `J_H` 精确消去 `N_0`，得到新的 positive primitive `3 mod4` carrier `R_HO`；再代入 `J_H/B_W mod W_q` 的 square-coefficient bridge，得到 `H_O,B_W,R_HO` 在整个 `W_q` depth 内的三项关系。若 angle-height 与 additive-height 深度不等，则 `R_HO` 精确读取较浅者；只有 equal-depth cancellation 能 extra lift，而且该 cancellation 强迫 normalized `B_W/H_O` ratio 为一个显式 non-square `-square`。因此 moving height 的普通 unequal-depth区全部从开放 parity mechanism中删除；剩余核心成为 same-prime orientation 是否能把这个 ratio独立固定为 square。本文不证明该最后 square/non-square 矛盾，因此不关闭 height pool。

---

## 1. notation

固定 reflection endpoint：

\[
N:=N_{\rm dec}=10^M,
\quad T:=10^m,
\quad A:=a_2,
\quad B:=b_2,
\]

\[
Q:=B+2N,
\qquad
K:=9N+10A,
\]

\[
N_0:=\left(\frac{9B}{2}\right)^2+A^2.
\]

angle pure-prefix integer为

\[
\boxed{
\mathcal U_\Omega
:=(45B^2-2AN)^2-A^2B(99B-4N).}
\tag{1.1}

angle-height norm为

\[
\boxed{
\mathcal H_O
:=N_0\mathcal U_\Omega^2
+4A^4B^2Q^2K^2.}
\tag{1.2}

additive-height pure-prefix carrier为

\[
\boxed{
\mathcal J_H
:=B^2F_W(K)-Q^2N_0,}
\tag{1.3}

其中

\[
\boxed{
F_W(K):=(K-5)(5K-11)=5K^2-36K+55.}
\tag{1.4}

---

## 2. exact angle-norm/additive identity

定义新的 pure-prefix integer

\[
\boxed{
\mathscr R_{HO}
:=F_W(K)\mathcal U_\Omega^2
+4A^4Q^4K^2.}
\tag{2.1}

由 (1.3)：

\[
Q^2N_0=B^2F_W-\mathcal J_H.
\]
将其代入 `Q^2 H_O`：

\[
\begin{aligned}
Q^2\mathcal H_O
&=(B^2F_W-\mathcal J_H)\mathcal U_\Omega^2
+4A^4B^2Q^4K^2.
\end{aligned}
\]
所以得到 exact identity

\[
\boxed{
Q^2\mathcal H_O
+\mathcal U_\Omega^2\mathcal J_H
=B^2\mathscr R_{HO}.}
\tag{2.2}

它不选择 `H_1/H_2` orientation。因为已有

\[
\mathcal H_1\mathcal H_2=4\mathcal H_O,
\]
所以 (2.2) 同时覆盖两张 moving height sheets。

---

## 3. `R_HO` 是 positive primitive `3 mod4` carrier

真实 endpoint 中

\[
K>5,
\]
故

\[
F_W(K)=(K-5)(5K-11)>0.
\]
式 (2.1) 是两个非负项之和，第一项严格正，因此

\[
\boxed{\mathscr R_{HO}>0.}
\tag{3.1}

已有 angle parity audit：

\[
\boxed{
v_2(\mathcal U_\Omega)=2M+2,}
\tag{3.2}

并且

\[
\boxed{
\frac{\mathcal U_\Omega}{2^{2M+2}}
\equiv1\pmod4.}
\tag{3.3}

同时 `K=2 mod4`，所以

\[
F_W(K)\equiv3\pmod4.
\tag{3.4}

在 (2.1) 中第一项的 `2`-进深度为

\[
4M+4,
\]
第二项因为

\[
v_2(Q)=M+1,\qquad v_2(K)=1
\]
具有深度

\[
4+4(M+1)+2=4M+10,
\]
严格更深。因此

\[
\boxed{v_2(\mathscr R_{HO})=4M+4,}
\tag{3.5}

并且

\[
\boxed{
\widehat{\mathscr R}_{HO}
:=\frac{\mathscr R_{HO}}{2^{4M+4}}
>0,
\qquad
\widehat{\mathscr R}_{HO}\equiv3\pmod4.}
\tag{3.6}

所以 `R_HO` 自身又是一份 positive odd-inert-parity carrier。

---

## 4. 代入 `J_H/B_W` height square bridge

`spontaneous-height-resultant-parity.md` 已证明

\[
\widehat{\mathcal J}_H
\equiv(2^mg)^2\mathscr B_W
\pmod{W_q},
\]
并且

\[
\mathcal J_H=2^{2M+2}\widehat{\mathcal J}_H,
\qquad
B=2^{M+m+1}c_ug.
\]
因此无分母地：

\[
\boxed{
c_u^2\mathcal J_H
\equiv B^2\mathscr B_W
\pmod{W_q}.}
\tag{4.1}

把 (4.1) 代入 (2.2) 乘 `c_u^2` 后的形式，得到 universal bridge

\[
\boxed{
B^2c_u^2\mathscr R_{HO}
\equiv
Q^2c_u^2\mathcal H_O
+\mathcal U_\Omega^2B^2\mathscr B_W
\pmod{W_q}.}
\tag{4.2}

这里两项的显式 coefficients

\[
Q^2c_u^2=(Qc_u)^2,
\]

\[
\mathcal U_\Omega^2B^2=(\mathcal U_\Omega B)^2
\]
都是完整 squares。

---

## 5. genuine external height prime上的 unit audit

固定 genuine non-`3` inert external height prime

\[
p^h\Vert W_q,
\qquad p\equiv3\pmod4,
\qquad p\ne3,5.
\]

primitive/external separation给

\[
p\nmid BQc_u.
\tag{5.1}

若该 prime进入 angle-height sheet，则某一个 raw angle integer

\[
\mathcal O_\pm
=T\mathcal U_\Omega\pm2A^2Qb_3
\]
被 `p` 整除。第二项是 external unit，因此

\[
\boxed{p\nmid\mathcal U_\Omega.}
\tag{5.2}

所以 (4.2) 的三个 coefficients在该 prime上全部为 units。

`spontaneous-height-parity-ledger.md` 还给

\[
\min\{v_p(\mathcal H_O),h\}
=
\min\{v_p(\mathcal O_{\rm hit}),h\},
\]
所以 `H_O` 正是两张 height orientations共同可用的 angle-depth reader。

---

## 6. universal unequal-depth law

定义

\[
e_B:=v_p(\mathscr B_W),
\qquad
e_O:=v_p(\mathcal H_O),
\qquad
e_R:=v_p(\mathscr R_{HO}).
\]

若

\[
\min(e_B,e_O)<h
\]
且两者不等，则 (4.2) 中较浅的 unit-coefficient term不可能被较深项取消。因此：

\[
\boxed{
e_B<e_O<h\Longrightarrow e_R=e_B,}
\tag{6.1}

\[
\boxed{
e_O<e_B<h\Longrightarrow e_R=e_O.}
\tag{6.2}

统一写成

\[
\boxed{
e_B\ne e_O,
\quad\min(e_B,e_O)<h
\Longrightarrow
v_p(\mathscr R_{HO})=\min(e_B,e_O).}
\tag{6.3}

所以 ordinary unequal-depth moving contact不会产生隐藏 extra lift。

---

## 7. equal-depth extra lift强迫 normalized non-square ratio

现在设

\[
e_B=e_O=e<h.
\]

若 `R_HO` 的 valuation严格超过 `e`，则 (4.2) 除以 `p^e` 后必须满足

\[
Q^2c_u^2\frac{\mathcal H_O}{p^e}
+\mathcal U_\Omega^2B^2\frac{\mathscr B_W}{p^e}
\equiv0\pmod p.
\]
所以

\[
\boxed{
\frac{\mathscr B_W/p^e}{\mathcal H_O/p^e}
\equiv
-\left(
\frac{Qc_u}{\mathcal U_\Omega B}
\right)^2
\pmod p.}
\tag{7.1}

右边是 `-1` 乘一个非零平方。因为

\[
p\equiv3\pmod4,
\]
有

\[
\boxed{
\left(
\frac{(\mathscr B_W/p^e)/(\mathcal H_O/p^e)}p
\right)=-1.}
\tag{7.2}

因此 equal-depth extra lift 需要一个非常具体的 same-prime orientation：normalized additive-height / angle-height ratio必须是 non-square。

这与单独对 `B_W` 或 `H_i` 做 discriminant character不同；(7.2) 是两个真实 depth readers之间的**相对 orientation**。

---

## 8. updated moving-height frontier

结合 `spontaneous-height-moving-singular-nogo.md`，moving height common channel现在满足：

1. 所有 genuine singular Hensel trees已删除；
2. unequal-depth simple contacts由 (6.3) 精确同步；
3. 唯一仍可能产生 extra depth的 unsaturated shell为
   \[
   e_B=e_O<h;
   \]
4. 该 shell若 extra lift，必须满足 relative non-square law (7.2)。

所以剩余目标已从“继续找 local singular prime”变成：

\[
\boxed{
\text{从 actual/conjugate angle sheet、canonical Gaussian orientation
或 }W_q=\alpha/\omega\text{ 的 natural representative，}
}
\]

\[
\boxed{
\text{独立确定 }
(\mathscr B_W/p^e)/(\mathcal H_O/p^e)
\text{ 的 square class。}}
\]

若该独立 orientation给 square，则 (7.2) 立即矛盾，整个 unsaturated equal-depth shell即关闭。
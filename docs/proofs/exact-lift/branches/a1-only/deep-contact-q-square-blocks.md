# A1 minimal diagonal: contact-square Q-side block lifting

> 日期：2026-08-20。依赖 `rational-contact.md`、minimal diagonal odd-prime supply 与 `deep-double-2high-master.md`。本文只使用 double-deep `lambda=1`；当前 surviving double-deep 都属于 2-high/5-low master branch。

本文从**原 rational-contact square** 导出一条与 four-factor/Hensel skeleton 不同源的全局因子结构。核心现象是 Q-side supply divisor `q` 在 contact 差平方中以 `q^2` 出现，因此其 regular prime-power blocks 会平方提升并 whole-block 分配到两个 contact factors。

状态：**已严格完成。**

---

## 1. 原 contact square 的差平方

minimal diagonal 的 contact square 写成

\[
V^2=K-2\rho\,TQ\,N,
\]

其中

\[
K=b_1^2C^2-(TQ)^2N.
\]

因此

\[
\boxed{
(b_1C)^2-V^2
=TQN(TQ+2\rho).}
\tag{1}

在 double-deep 中

\[
\Gamma=\frac\gamma D,
\qquad
\rho=N_0-\frac\gamma{DT},
\]

且

\[
\gamma=DTN_0-h.
\]

因为 `V^2` 的 reduced denominator 整除 `D`，若 `V=a/b` 既约，则 `b^2|D`，故 `b|D`。所以

\[
\boxed{Z:=DV\in\mathbf Z.}
\tag{2}

把 (1) 乘以 `D^2`：

\[
(Db_1C-Z)(Db_1C+Z)
=DQN\bigl(DT(TQ+2N_0)-2\gamma\bigr).
\]

代入 `gamma=DTN_0-h`：

\[
\boxed{
(Db_1C-Z)(Db_1C+Z)
=DQN(DT^2Q+2h).}
\tag{3}

---

## 2. Q-side supply 产生 `q^2`

写完整 odd supply

\[
h=qs,
\qquad Q=qv.
\]

则

\[
DT^2Q+2h
=q(DT^2v+2s).
\]

所以 (3) 精确化为

\[
\boxed{
L_-L_+
=D\,N\,q^2v\,(DT^2v+2s),}
\tag{4}

其中

\[
\boxed{L_\pm:=Db_1C\pm Z.}
\]

这就是 contact Q-side square lifting 的来源。

---

## 3. 两个 contact factors 的公共奇因子

显然

\[
\gcd(L_-,L_+)\mid2Db_1C.
\tag{5}

另一方面

\[
\gcd(Q,Db_1)=1
\]

因为 `D` 只含 2、5，`Q` 与 10 互素，并且 `gcd(Q,b1)=1`。

所以若奇素数

\[
p\mid q\mid Q,
\]

则 `p` 能同时整除 `L_-`,`L_+` 的唯一来源是

\[
\boxed{p\mid C.}
\tag{6}

---

## 4. regular `q` blocks 平方 whole-block lifting

设

\[
p^e\Vert q.
\]

由 (4)：

\[
v_p(L_-)+v_p(L_+)\ge2e.
\tag{7}

若

\[
p\nmid C,
\]

则由 (5)-(6)：

\[
\min(v_p(L_-),v_p(L_+))=0.
\]

故另一边必须承担全部 `2e`：

\[
\boxed{
p^{2e}\mid L_-
\quad\text{or}\quad
p^{2e}\mid L_+.}
\tag{8}

所以每一个不碰 `C` 的 selected Q-side prime-power block 都会：

1. 不能拆到两个 contact factors；
2. exponent 从 `e` 提升到至少 `2e`。

定义

\[
q_{\rm reg}
:=\prod_{p^e\Vert q,\ p\nmid C}p^e.
\]

则存在互素分解

\[
\boxed{q_{\rm reg}=q_-q_+}
\]

使

\[
\boxed{q_-^2\mid L_-,
\qquad q_+^2\mid L_+.}
\tag{9}

这里每个 `p^e` block 整块进入一边。

---

## 5. 即使是 exceptional block，也至少 whole-block 进入一边

若 `p|C`，令

\[
c=v_p(C).
\]

由 (5)：

\[
\min(v_p(L_-),v_p(L_+))\le c.
\]

结合 (7)：

\[
\max(v_p(L_-),v_p(L_+))
\ge2e-c.
\]

同时仅由 `x+y>=2e` 已有

\[
\max(x,y)\ge e.
\]

因此

\[
\boxed{
\max(v_p(L_-),v_p(L_+))
\ge\max(e,2e-c).}
\tag{10}

特别地，哪怕 `p|C`，完整 selected block `p^e` 仍不能被迫拆碎：至少有一个 contact factor 含整个 `p^e`。

regular case `c=0` 正好恢复平方提升 `2e`。

---

## 6. exceptional prime support 只落在一个 `O(T)` resultant 上

现在精确控制

\[
\gcd(Q,C).
\]

minimal diagonal 中

\[
Q=100T^2-10w+1,
\]

\[
a_1=100T^3+(10(5-z-w)+1)T+N_0-1,
\]

\[
C=10T^2a_1+a_2,
\qquad a_2=10T^2-z.
\]

模 `Q`：

\[
100T^2\equiv10w-1,
\]

所以

\[
a_1\equiv10(5-z)T+N_0-1\pmod Q.
\]

乘 `C` 以 10，消去 `10^{-1}`：

\[
\boxed{
10C\equiv
(10w-1)N_0
+10(10w-1)(5-z)T
-10z
\pmod Q.}
\tag{11}

因为 `gcd(10,Q)=1`，令右侧为 `E_C`，则

\[
\boxed{\gcd(Q,C)\mid E_C.}
\tag{12}

使用 `0<N0<=T`，六类型分别有安全界：

\[
\boxed{
\begin{array}{c|c}
(z,w)&0<E_C<c_{z,w}T\\ \hline
(1,1)&c_{z,w}=369\\
(1,2)&779\\
(1,3)&1189\\
(1,4)&1599\\
(3,1)&189\\
(3,2)&399
\end{array}}
\tag{13}

因此统一：

\[
\boxed{\gcd(Q,C)<1599T.}
\tag{14}

所以能破坏平方 whole-block lifting 的 exceptional prime support 必须来自这个显式线性 resultant `E_C=O(T)`；它不可能在 `Q~100T^2` 中任意游走。

---

## 7. 当前意义

剩余 double-deep 2-high master branch 现在同时受两套真正独立的 prime-block skeleton 控制：

1. four-factor：`q,s,bar q,bar s` 与 `alpha,beta` 的 unimodular frame；
2. contact factor：Q-side `q` 的 regular prime-power blocks在 `L_-,L_+` 中平方 whole-block lifting。

尤其后续可以把 `q=q_reg*q_exc` 分开：

- `q_reg` 具有 (9) 的平方 block partition；
- `q_exc` 的 prime support 必须落在 `E_C` 上；
- strict-2 unit square 还固定 `q mod4` 与 `r_10 mod8`。

这为真正利用原 rational-contact square（而不是重复 root/Hensel 条件）提供了新的全局入口。

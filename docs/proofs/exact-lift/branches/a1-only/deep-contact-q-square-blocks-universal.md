# A1 minimal diagonal: universal deep contact Q-side lifting

> 日期：2026-08-20。推广 `deep-contact-q-square-blocks.md`，并吸收 `deep-b1-sharp-mandatory-blocks.md`。本文适用于任意 deep denominator state，包括 single-2、single-5 与 double-deep。

状态：**已严格完成。**

---

## 1. universal contact factorization

原 rational-contact square：

\[
V^2=K-2\rho TQN,
\]

其中

\[
K=b_1^2C^2-T^2Q^2N.
\]

所以

\[
(b_1C)^2-V^2=TQN(TQ+2\rho).
\tag{1}

任意 deep state 都有

\[
DT\rho=h\lambda,
\qquad h=qs,
\qquad Q=qv.
\]

若 `V=a/b` 既约，则 `V^2` 的分母 `b^2` 整除 D，故 `b|D`，所以

\[
\boxed{Z:=DV\in\mathbf Z.}
\tag{2}

乘以 `D^2` 并代入 supply：

\[
\boxed{
L_-L_+
=DNq^2v(DT^2v+2s\lambda),}
\tag{3}

其中

\[
\boxed{L_\pm:=Db_1C\pm Z.}
\]

因此 Q-side `q^2` lifting 不依赖 `lambda=1`。

---

## 2. q-primary lifting

对任意

\[
p^e\Vert q,
\]

有

\[
v_p(L_-)+v_p(L_+)\ge2e.
\]

且

\[
\gcd(L_-,L_+)\mid2Db_1C.
\]

因为 `p|Q` 与 `2Db_1D` 互素：

\[
\boxed{
\max(v_p(L_-),v_p(L_+))
\ge2e-\min(e,v_p(C)).}
\tag{4}

特别地

\[
p\nmid C
\Longrightarrow
\boxed{p^{2e}\mid L_-\text{ or }L_+.}
\tag{5}

---

## 3. resultant exceptional loss

minimal diagonal：

\[
10C\equiv E_C\pmod Q,
\]

\[
E_C=(10w-1)N_0+10(10w-1)(5-z)T-10z.
\]

所以对任意 `q|Q`：

\[
\boxed{\gcd(q,C)=\gcd(q,E_C).}
\]

令

\[
g:=\gcd(q,C).
\]

六类型：

\[
\boxed{
\begin{array}{c|c}
(z,w)&g<c_{z,w}T\\ \hline
(1,1)&369T\\
(1,2)&779T\\
(1,3)&1189T\\
(1,4)&1599T\\
(3,1)&189T\\
(3,2)&399T
\end{array}}
\tag{6}

并存在 coprime block products `Q_-,Q_+`：

\[
\boxed{Q_-Q_+=q^2/g,}
\]

\[
\boxed{Q_-\mid L_-,
\qquad Q_+\mid L_+.}
\tag{7}

---

## 4. universal selected-Q lower bound

\[
h=\frac{D(TN_0-\Gamma)}\lambda.
\]

当前 `N_0>=T/10`、`Gamma<39.003`，所以对 `k>=32`：

\[
TN_0-\Gamma>T^2/11.
\]

故

\[
\boxed{h>DT^2/(11\lambda).}
\tag{8}

sharpened mandatory `b_1` complements：

\[
\boxed{(c_1,c_2,c_3,c_4)=(9,38,1,12),}
\tag{9}

且

\[
s\le b_1/c_w<10T^2/c_w.
\]

所以

\[
\boxed{
q=h/s>
\frac{c_w}{110}\frac D\lambda.}
\tag{10}

---

## 5. sharpened forced-lift criterion

若

\[
\frac D\lambda>K_{z,w}T,
\]

其中

\[
K_{z,w}:=110c_{z,w}/c_w,
\]

则由 (6),(10)：

\[
q>c_{z,w}T>g,
\]

所以 contact exceptional resultant 不可能吞掉整个 q，必出现 strict exponent amplification。

sharpened constants：

\[
\boxed{
\begin{array}{c|c}
(z,w)&K_{z,w}\\ \hline
(1,1)&4510\\
(1,2)&2255\\
(1,3)&130790\\
(1,4)&14657.5\\
(3,1)&2310\\
(3,2)&1155
\end{array}}
\tag{11}

其中 `(1,1),(1,2),(3,1),(3,2)` 比旧值明显下降。

---

## 6. 当前用途

contact-square block mechanism 现在统一覆盖所有 deep：

- double-deep 2-high master 远超 criterion (11)；
- single-5 使用 `D/lambda=5^B/2^lambda2`；
- single-2 使用 `D/lambda=2^A/5^lambda5`。

所以 single-deep 也可自然分为：

1. typewise low-ratio strip；
2. forced contact-lift strip。

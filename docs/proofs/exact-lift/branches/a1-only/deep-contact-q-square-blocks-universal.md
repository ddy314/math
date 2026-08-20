# A1 minimal diagonal: universal deep contact Q-side lifting

> 日期：2026-08-20。推广 `deep-contact-q-square-blocks.md`。本文适用于任意 deep denominator state，包括 single-2、single-5 与 double-deep。

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
\qquad
h=qs,
\qquad Q=qv.
\]

又 `V^2` 的 reduced denominator 整除 `D`。若 `V=a/b` 既约，则其平方分母为 `b^2`，故

\[
b^2\mid D
\Longrightarrow
b\mid D.
\]

因此

\[
\boxed{Z:=DV\in\mathbf Z.}
\tag{2}

把 (1) 乘 `D^2`：

\[
\begin{aligned}
(Db_1C-Z)(Db_1C+Z)
&=D^2TQN\left(TQ+\frac{2h\lambda}{DT}\right)\\
&=DQN(DT^2Q+2h\lambda).
\end{aligned}
\]

代入 `Q=qv,h=qs`：

\[
\boxed{
L_-L_+
=DNq^2v(DT^2v+2s\lambda),}
\tag{3}

其中

\[
\boxed{L_\pm:=Db_1C\pm Z.}
\]

所以此前的 Q-side `q^2` 并不依赖 `lambda=1`。

---

## 2. q-primary lifting 完全保留

对任意

\[
p^e\Vert q,
\]

(3) 给

\[
v_p(L_-)+v_p(L_+)\ge2e.
\]

同时

\[
\gcd(L_-,L_+)\mid2Db_1C.
\]

而 `p|q|Q` 与 `2Db_1D` 互素，所以

\[
\min(v_p(L_-),v_p(L_+))\le v_p(C).
\]

于是

\[
\boxed{
\max(v_p(L_-),v_p(L_+))
\ge2e-\min(e,v_p(C)).}
\tag{4}

特别地：

\[
p\nmid C
\Longrightarrow
\boxed{p^{2e}\mid L_-\text{ or }L_+.}
\tag{5}

所以 regular selected Q-primary blocks 在所有 deep sectors 中都 square-lift。

---

## 3. resultant exceptional loss 也不依赖 deep type

minimal diagonal 的 prefix congruence仍为

\[
10C\equiv E_C\pmod Q,
\]

\[
E_C=(10w-1)N_0+10(10w-1)(5-z)T-10z.
\]

因此对任意 `q|Q`：

\[
\boxed{\gcd(q,C)=\gcd(q,E_C).}
\]

令

\[
g:=\gcd(q,C).
\]

六类型安全界：

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

这同样适用于 single-deep。

---

## 4. universal supply lower bound for `q`

由

\[
h=\frac{D(TN_0-\Gamma)}\lambda.
\]

当前 `rho` 有 k 位，故

\[
N_0\ge T/10.
\]

而 `Gamma<39.003`。对 `k>=32`：

\[
TN_0-\Gamma
>\frac{T^2}{11}.
\]

所以

\[
\boxed{h>\frac{DT^2}{11\lambda}.}
\tag{8}

whole-block selector `s` 的 structural upper bounds：

\[
s\le\frac{b_1}{c_w},
\]

其中

\[
\boxed{
(c_1,c_2,c_3,c_4)=(3,14,1,12).}
\tag{9}

这里：

- `w=1` 固定丢失 3-block；
- `w=2` 丢失 2 与至少一个 `>=7` 的 `3 mod4` block；
- `w=3` 暂无 universal extra loss；
- `w=4` 丢失 `2^2*3`。

又 `b_1<10T^2`，所以

\[
q=h/s
>\frac{c_wD}{110\lambda}.
\]

即

\[
\boxed{
q>\frac{c_w}{110}\frac D\lambda.}
\tag{10}

这是任意 deep sector 的 universal selected-Q lower bound。

---

## 5. forced-lift criterion

若

\[
\frac D\lambda>K_{z,w}T,
\]

其中

\[
\boxed{
K_{z,w}:=\frac{110c_{z,w}}{c_w},}
\]

则由 (6),(10)：

\[
q>c_{z,w}T>g.
\]

六类型常数：

\[
\boxed{
\begin{array}{c|c}
(z,w)&K_{z,w}\\ \hline
(1,1)&13530\\
(1,2)&6120.715\\
(1,3)&130790\\
(1,4)&14657.5\\
(3,1)&6930\\
(3,2)&3135
\end{array}}
\tag{11}

所以只要 `D/lambda` 超过对应 `O(T)` threshold，contact exceptional resultant不可能吞掉整个 q，必存在至少一个 selected Q-primary block发生 strict exponent amplification。

---

## 6. 当前用途

本文把 contact-square block mechanism 从 double-deep 扩展到全部 deep。后续：

- double-deep 2-high master 已远超 criterion (11)；
- single-5 可用 `D/lambda=5^B/2^{lambda_2}`；
- single-2 可用 `D/lambda=2^A/5^{lambda_5}`。

所以 single-deep 也可自然分成：

1. `D/lambda` 小于 typewise threshold 的 low-ratio strip；
2. forced contact-lift strip。

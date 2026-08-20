# A2 fixed `23` `eta=2` `c=2` 的 high-2 / source-content `mod 23` synchronization

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-blowup-nogo.md`、`spontaneous-cq-fixed23-eta2-c2-source-window.md`、`spontaneous-cq-relative-depth-nogo.md`。
>
> **严格状态：**c=2 high-2 blow-up将 normalized denominator `q_2=Q/23^2` 当作局部 correction coordinate，这足以证明 local system smooth；真实 arithmetic orbit还满足 exact coordinate relation `q_2=3*2^(2lambda+1)q` 与 `rho=q5^lambda/c_u`。本文把这条 global relation代回 high-2 bridge，得到 orientation-specific 的 `c_u mod23` **second-layer survival 必要条件**。若真实 state 已进入 fixed-23 first layer但不满足该 residue，则 common depth严格停在 `1`；这并不排除 arithmetic state。低高度中，`lambda=52` 与 `lambda=74` 在两种 orientation 下都强迫 `d_23=1`，`lambda=63` 的 plus orientation强迫 `d_23=1`，minus orientation才可能继续进入第二层。这是 high-2 equality提供的新增 global synchronization，不属于此前 source-tail quotient shadow。

---

## 1. global relation between `q_2` and `rho`

固定

\[
p:=23,
\qquad
c_Q=3p^2,
\qquad
M=2\lambda.
\]

定义

\[
q_2:=\frac Q{p^2}.
\]
由真实 denominator formula

\[
Q=2^{M+1}c_Qq
\]
精确得到

\[
\boxed{
q_2=3\cdot2^{2\lambda+1}q.}
\tag{1.1}

source ratio为

\[
\boxed{
\rho:=\frac{q5^\lambda}{c_u}.}
\tag{1.2}

所以模 `p`：

\[
\boxed{
q_2
\equiv
3\cdot2^{2\lambda+1}\rho c_u5^{-\lambda}
\pmod p.}
\tag{1.3}

这里 `rho,c_u,5` 都是 `p`-进 units。

---

## 2. high-2 bridge直接固定 second-layer 的 `c_u mod23`

c=2 high-2 blow-up 已证明：

### `c_-` orientation

\[
\boxed{\rho^2=16q_2\pmod p.}
\tag{2.1-}

代入 (1.3)：

\[
\rho^2
\equiv
48\cdot2^{2\lambda+1}\rho c_u5^{-\lambda}.
\]
因为

\[
48\equiv2\pmod{23},
\]
并约去 unit `rho`：

\[
\boxed{
\rho
\equiv
2^{2\lambda+2}c_u5^{-\lambda}
\pmod{23}.}
\tag{2.2-}

### `c_+` orientation

\[
\boxed{\rho(\rho+2)=16q_2\pmod p.}
\tag{2.1+}

同理约去 `rho`：

\[
\boxed{
\rho+2
\equiv
2^{2\lambda+2}c_u5^{-\lambda}
\pmod{23}.}
\tag{2.2+}

因此真实 high-2 state并不能任意选择 blow-up coordinate `q_2`；若 common depth想从第一层继续到第二层，它必须同时落在由 source content固定的 global orbit上。

---

## 3. 与 additive Möbius chart 联立

second-layer prefix已由 decimal length固定

\[
\kappa=\kappa(\lambda)\pmod{23}.
\]
若

\[
\kappa\notin\{11,18\},
\]
additive gate唯一给

\[
\boxed{
\rho_+(\kappa)
=-\frac{11}{1+14\kappa},}
\tag{3.1+}

\[
\boxed{
\rho_-(\kappa)
=\frac{9+18\kappa}{1+14\kappa}.}
\tag{3.1-}

将其代入 (2.2±)，得到 common depth `>=2` 的 source-content 必要 residue：

### plus / `23^2|c_+`

\[
\boxed{
c_u
\equiv
5^\lambda2^{-2\lambda-2}
\left(\rho_+(\kappa)+2\right)
\pmod{23}.}
\tag{3.2+}

也可写成

\[
\boxed{
c_u
\equiv
5^\lambda2^{-2\lambda-2}
\frac{5\kappa-9}{1+14\kappa}
\pmod{23}.}
\tag{3.3+}

### minus / `23^2|c_-`

\[
\boxed{
c_u
\equiv
5^\lambda2^{-2\lambda-2}
\rho_-(\kappa)
\pmod{23},}
\tag{3.2-}

即

\[
\boxed{
c_u
\equiv
5^\lambda2^{-2\lambda-2}
\frac{9+18\kappa}{1+14\kappa}
\pmod{23}.}
\tag{3.3-}

所以

\[
\boxed{
\text{若 first-layer state 不满足对应 (3.2)，则 }d_{23}=1.}
\tag{3.4}

满足 (3.2) 只说明 second-layer survival **尚未被这条 global gate排除**；它不能单独推出 `d_23>=2`。

---

## 4. periodicity

已有

\[
\lambda\equiv8\pmod{11}.
\]
又

\[
\operatorname{ord}_{23}(2)=11,
\qquad
\operatorname{ord}_{23}(5)=22.
\]
所以 `2^(2lambda+2)` 在整个 height lattice上固定，而 `5^lambda` 随 `lambda -> lambda+11` 改变符号。

另一方面 `kappa` 由

\[
M=2\lambda=16+22j
\]
中的 `j mod23` 决定。因此完整 residue pattern 对

\[
\lambda\mapsto\lambda+506
\]
周期化；在 `lambda=8 mod11` 的序列中等价于 `46` 个 `j`-steps 周期。

特殊 classes

\[
\kappa=18\Longleftrightarrow\lambda\equiv85\pmod{253},
\]

\[
\kappa=11\Longleftrightarrow\lambda\equiv118\pmod{253}
\]
已经由 additive gate直接强迫 `d_23=1`，不进入本文 second-layer source-content gate。

---

## 5. low-height depth ledger

source-window proof已给最初 source-content possibilities：

\[
(\lambda,c_u)
=(52,29),
(63,337),
(74,3917),
(74,3929).
\]
下面所有结论都只讨论 fixed-23 common depth；不宣称 arithmetic state本身不存在。

### `lambda=52`

prefix给

\[
\kappa=2.
\]
(3.2±) exact 计算为

\[
\boxed{c_u\equiv12\pmod{23}\quad(c_+),}
\]

\[
\boxed{c_u\equiv11\pmod{23}\quad(c_-).}
\]
但

\[
29\equiv6\pmod{23}.
\]
两种 canonical orientation都不能进入 second layer。因此若该 arithmetic state存在：

\[
\boxed{\lambda=52\Longrightarrow d_{23}=1.}
\tag{5.1}

这是 orientation-independent odd-depth certification。

### `lambda=63`

\[
\kappa=15.
\]
所需 residue为

\[
\boxed{c_u\equiv8\pmod{23}\quad(c_+),}
\]

\[
\boxed{c_u\equiv15\pmod{23}\quad(c_-).}
\]
而

\[
337\equiv15\pmod{23}.
\]
所以：

\[
\boxed{
23^2\mid c_+
\Longrightarrow d_{23}=1,}
\tag{5.2+}

而

\[
\boxed{
23^2\mid c_-
\Longrightarrow
\text{second-layer survival仍可能发生}.}
\tag{5.2-}

后者不是 `d_23>=2` 的充分条件；仍需检查真实下一 correction。

### `lambda=74`

\[
\kappa=5.
\]
所需 residue为

\[
\boxed{c_u\equiv1\pmod{23}\quad(c_+),}
\]

\[
\boxed{c_u\equiv22\pmod{23}\quad(c_-).}
\]
而

\[
3917\equiv7,
\qquad
3929\equiv19
\pmod{23}.
\]
两个 source contents在两种 orientations 下都不能进入 second layer。因此若 arithmetic state存在：

\[
\boxed{\lambda=74\Longrightarrow d_{23}=1.}
\tag{5.3}

同样是 orientation-independent odd-depth certification。

---

## 6. updated low-height parity ledger

source real window仍给

\[
\lambda\ge52.
\]
结合本文与旧 `kappa=11,18` certification，最初四个 relevant heights的 fixed-23 ledger为

\[
\boxed{
\begin{array}{c|c}
\lambda&\text{fixed-23 conclusion if an arithmetic state exists}\\ \hline
52&d_{23}=1\\
63&c_+:d_{23}=1;\quad c_-:\text{may deepen}\\
74&d_{23}=1\\
85&d_{23}=1\quad(\kappa=18)
\end{array}}
\tag{6.1}

所以 `52,74,85` 已经在 pure-23 parity ledger 中完全结算为 odd depth；只有 `lambda=63` 的 minus orientation在这些最低层中仍需要 deeper-depth audit。

---

## 7. proof boundary

(3.2±) 是一个真正 global condition，因为它同时使用：

1. real denominator coordinate `q_2=Q/23^2`；
2. source ratio `rho=q5^lambda/c_u`；
3. high-2 equality；
4. additive orientation gate。

它不是 `theta/omega` quotient identity的重写。

逻辑方向必须保持为：

\[
\boxed{d_{23}\ge2\Longrightarrow c_u\text{ 满足对应 residue}.}
\]

其逆命题未证明。后续 higher-depth source-content Hensel branch应沿同一方向使用：每升一层都会进一步固定 `c_u` 的 `23`-adic digits；某一层 residue失败时，才可在“前一层已进入”的条件下判定 common depth精确停止。
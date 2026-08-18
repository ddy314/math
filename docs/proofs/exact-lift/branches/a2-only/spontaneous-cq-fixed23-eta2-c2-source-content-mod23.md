# A2 fixed `23` `eta=2` `c=2` 的 high-2 / source-content `mod 23` synchronization

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-blowup-nogo.md`、`spontaneous-cq-fixed23-eta2-c2-source-window.md`、`spontaneous-cq-relative-depth-nogo.md`。
>
> **严格状态：**c=2 high-2 blow-up将 normalized denominator `q_2=Q/23^2` 当作局部 correction coordinate，这足以证明 local system smooth；真实 arithmetic orbit还满足 exact coordinate relation `q_2=3*2^(2lambda+1)q` 与 `rho=q5^lambda/c_u`。本文把这条 global relation代回 high-2 bridge，得到 orientation-specific 的 `c_u mod23` 必要条件。它严格删除 `lambda=52` 和 `lambda=74` 的全部低 source states，并把 `lambda=63` 唯一保留为 `c_-` orientation。这是 high-2 equality提供的新增 global synchronization，不属于此前 source-tail quotient shadow。

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

## 2. high-2 bridge直接固定 `c_u mod23`

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

因此真实 high-2 state并不能任意选择 blow-up coordinate `q_2`；它必须同时落在由 source content固定的 global orbit上。

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

将其代入 (2.2±)，得到 source-content residue：

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

这是当前 type 的 orientation-specific source-content gate。

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
已经强迫 `d_23=1`，不进入本文 second-layer source-content gate。

---

## 5. low-height source states被严格筛掉

source-window proof已给：

\[
(\lambda,c_u)
=(52,29),
(63,337),
(74,3917),
(74,3929)
\]
是最初可能 states。

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
故

\[
\boxed{\lambda=52\text{ 全排除}.}
\tag{5.1}

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
所以

\[
\boxed{
\lambda=63,c_u=337
\text{ 只允许 }23^2\mid c_- .}
\tag{5.2}

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
两者均失败。因此

\[
\boxed{\lambda=74\text{ 全排除}.}
\tag{5.3}

---

## 6. updated height frontier

source real window原先给

\[
\lambda\ge52.
\]
本文把最底层推进为：

\[
\boxed{
\lambda=52\text{ impossible},
\qquad
\lambda=63\text{ only minus orientation},
\qquad
\lambda=74\text{ impossible}.}
\tag{6.1}

下一 lattice height为

\[
\lambda=85,
\]
它恰属于

\[
\kappa=18
\]
的 fixed-23 forced depth-1 class。因此即便存在 arithmetic state，已有

\[
\boxed{d_{23}=1.}
\tag{6.2}

所以在 height ledger 中，最初四个 possible `lambda` levels现在分别为：

\[
\boxed{
52:\emptyset,
\quad63:\text{single 23 orientation},
\quad74:\emptyset,
\quad85:\text{fixed odd }23\text{-depth}.}
\tag{6.3}

---

## 7. proof boundary

(3.2±) 是一个真正 global condition，因为它同时使用：

1. real denominator coordinate `q_2=Q/23^2`；
2. source ratio `rho=q5^lambda/c_u`；
3. high-2 equality；
4. additive orientation gate。

它不是 `theta/omega` quotient identity的重写。

对无界高度，它把 source-content real interval再切到每个 orientation唯一的 `mod23` class，但单独尚不能证明所有 classes为空。其主要用途是：先筛 `c_u`，再进入 centered source-divisor / full canonical CRT certificate。
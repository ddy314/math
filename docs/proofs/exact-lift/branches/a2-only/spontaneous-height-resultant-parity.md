# A2 `B_W` / reduced-height 的第二个 global parity pair

> **依赖：** `endpoint-lattice.md` (16.427)、`height-cofactor.md`、`source-discriminant.md`、`spontaneous-height-parity-ledger.md`。
>
> **严格状态：**本文把 height-cofactor resultant `B_W` 与 reduced numerator `W_q` 直接视为第二个 global parity pair。`B_W` 是 positive `7 mod 8` integer，而 `W_q≡3Z mod4`。因此在 `Z≡1 mod4` orientation 中，两者都是 `3 mod4`，其 gcd恰为 additive height common part `D_H`; 若 `D_H≡1 mod4`，两个互素 residual quotients都被迫携带 odd inert parity。本文还把 pure-decimal `J_H` 与 `B_W` 放进一个 exact square-coefficient congruence modulo `W_q`，为下一层 cross-companion 分析提供接口。本文不证明这些 residual primes不存在，也不关闭 A2。

---

## 1. height gcd 的三个等价读取器

沿用

\[
\alpha=TK+a_3=\omega W_q,
\qquad
H_0=c_uW_q,
\]

以及

\[
\boxed{
\mathscr B_W
=c_u^2(5K^2-36K+55)+(q5^\lambda K)^2.}
\tag{1.1}
\]

`height-cofactor.md` 已证明

\[
\boxed{
D_H:=\gcd(\widehat{\mathcal T}_2,W_q)
=\gcd(\mathscr B_W,W_q).}
\tag{1.2}
\]

`spontaneous-height-parity-ledger.md` 又给 pure-decimal

\[
\mathcal J_H=B^2(5K^2-36K+55)-Q^2N_0,
\]

\[
\widehat{\mathcal J}_H=\mathcal J_H/2^{2M+2},
\]
以及

\[
\boxed{
D_H=\gcd(\widehat{\mathcal J}_H,W_q).}
\tag{1.3}
\]

所以同一个 height common part有三个完全等价的读取器：

\[
\boxed{
D_H
=\gcd(\widehat T_2,W_q)
=\gcd(\widehat J_H,W_q)
=\gcd(\mathscr B_W,W_q).}
\tag{1.4}
\]

---

## 2. `B_W` 本身是 positive `3 mod 4` carrier

`source-discriminant.md` 已证明

\[
\boxed{\mathscr B_W\equiv7\pmod8.}
\tag{2.1}
\]

正性也直接来自当前 endpoint 的巨大正 `K`：

\[
5K^2-36K+55=(K-5)(5K-11)>0,
\]
且第二项为平方。因此

\[
\boxed{\mathscr B_W>0,\qquad \mathscr B_W\equiv3\pmod4.}
\tag{2.2}
\]

于是 `B_W` 自身强迫一份 odd total inert parity。

---

## 3. `W_q` 的真实 mod-4 orientation

`endpoint-lattice.md` (16.427) 给无条件 identity

\[
\boxed{W_q\equiv3Z\pmod4.}
\tag{3.1}
\]

所以

\[
\boxed{
Z\equiv1\pmod4\Longrightarrow W_q\equiv3\pmod4,}
\tag{3.2a}
\]

\[
\boxed{
Z\equiv3\pmod4\Longrightarrow W_q\equiv1\pmod4.}
\tag{3.2b}
\]

这条 orientation此前主要用于 prime-source 分类；和 (2.2) 合并后，它直接产生一个新的 gcd parity dichotomy。

---

## 4. `Z=1 mod4` 时 `B_W` 与 `W_q` 形成完整 parity pair

定义

\[
\boxed{
B^\circ:=\frac{\mathscr B_W}{D_H},
\qquad
W^\circ:=\frac{W_q}{D_H}.}
\tag{4.1}
\]

由 gcd 定义：

\[
\boxed{\gcd(B^\circ,W^\circ)=1.}
\tag{4.2}
\]

若

\[
Z\equiv1\pmod4,
\]
则由 (2.2)、(3.2a)：

\[
\mathscr B_W\equiv W_q\equiv3\pmod4.
\]
因此

\[
\boxed{
B^\circ\equiv W^\circ
\equiv3D_H^{-1}\pmod4.}
\tag{4.3}
\]

于是得到严格 dichotomy：

\[
\boxed{
\begin{array}{c|c|c}
D_H\bmod4&B^\circ\bmod4&W^\circ\bmod4\\ \hline
1&3&3\\
3&1&1
\end{array}}
\qquad(Z\equiv1\bmod4).
\tag{4.4}
\]

所以当

\[
D_H\equiv1\pmod4
\]
时，`B^circ` 与 `W^circ` 是两个互素 positive `3 mod4` integers：

\[
\boxed{
\text{height common part若不承担 odd inert parity，}
\text{则必须出现两份互不复用的 height residual odd parity。}}
\tag{4.5}
\]

这与 `G_sp` 和 angle/additive companion pair的 parity doubling完全同型，但来源不同：这里一边是 cofactor resultant，一边是真实 reduced numerator。

---

## 5. `Z=3 mod4` orientation 是 parity transfer 而非 doubling

若

\[
Z\equiv3\pmod4,
\]
则

\[
W_q\equiv1\pmod4,
\qquad
\mathscr B_W\equiv3\pmod4.
\]
所以

\[
\boxed{
B^\circ\equiv3D_H^{-1},
\qquad
W^\circ\equiv D_H^{-1}\pmod4.}
\tag{5.1}
\]

即

\[
\boxed{
\begin{array}{c|c|c}
D_H\bmod4&B^\circ\bmod4&W^\circ\bmod4\\ \hline
1&3&1\\
3&1&3
\end{array}}
\qquad(Z\equiv3\bmod4).
\tag{5.2}
\]

这里始终只有 `B_W` 与 `D_H/W^circ` 两边之一承担 residual odd parity；不存在双份复制。因此后续 global ledger必须保留 `Z` orientation，不能把两种情况混为一个无条件 doubling。

---

## 6. `J_H` 与 `B_W` 的 exact square-coefficient bridge modulo height

令

\[
z:=q5^\lambda,
\qquad
D=g2^m5^d,
\qquad
T=10^m,
\]
并使用 canonical height equality

\[
H_0^2-g^2a_3^2=5^\lambda c_Q^2XY,
\qquad
H_0=c_uW_q.
\]

把 `J_H` 除去 primitive 2-scale后直接展开，可得 exact integer identity

\[
\boxed{
\begin{aligned}
5^{2d}\widehat{\mathcal J}_H
&-2^{2m}5^{2d}g^2\mathscr B_W\\
&=q^2W_q\left[
(g^2\omega^2-c_u^2)W_q
-2g^2\omega TK
\right].
\end{aligned}}
\tag{6.1}
\]

左边 `B_W` 的 coefficient

\[
2^{2m}g^2=(2^mg)^2
\]
是完整平方。特别地 modulo `W_q`：

\[
\boxed{
5^{2d}\widehat J_H
\equiv
(2^mg)^2 5^{2d}\mathscr B_W
\pmod{W_q}.}
\tag{6.2}
\]

由于 `gcd(W_q,10g)=1`：

\[
\boxed{
\widehat J_H\equiv(2^mg)^2\mathscr B_W
\pmod{W_q}}
\tag{6.3}
\]
在局部 square-class 意义下完全无损。这重新证明两者与 `W_q` 读取相同 `D_H`，并说明它们在每个 height prime上的 residual unit只差一个显式平方。

这也意味着：继续给 `J_H` 与 `B_W` 各自叠加同一个 Legendre condition不会产生新的 obstruction；真正的新信息只能来自两者在离开 `W_q` 后的 additive difference / natural representative。

---

## 7. global ledger 的更新

在 `Z=1 mod4` orientation 中，现在至少有三种独立的 parity-doubling结构：

1. actual/conjugate angle pair；
2. actual additive / `J_H` pair after removing common height;
3. `B_W/W_q` height-resultant pair (本文)。

它们的共同点是：common gcd若为 `1 mod4`，两个互素 residuals都被迫为 `3 mod4`。

但本文仍不构成 closure。尤其 `B^circ` 与其它 companion residual可能共享同一个 external prime；要继续推进必须研究这种 cross-companion overlap，而不是再证明单个 carrier是 `3 mod4`。

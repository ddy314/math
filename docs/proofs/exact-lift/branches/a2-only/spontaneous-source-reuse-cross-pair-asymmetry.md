# A2 source parity reuse 上的 cross-pair asymmetry

> **依赖：** `spontaneous-source-reuse-cross-pair-length.md`、`spontaneous-residual-parity-doubling.md`、`spontaneous-source-parity-collision-gate.md`。
>
> **严格状态：**`O/J` cross-pair 在 source-reuse sheet上被投影成两个 pure-length octics。本文审计另一个建议 cross-pair `T/O`，证明 first layer存在结构性自由：source reused prime是 noncentral且与 `B` 分离，而 raw additive carrier `Theta_dec` 对 third numerator `a_3` 是 unit-coefficient线性式，因此任意 prefix/angle first-layer state都唯一恢复一个 `a_3 mod r`。所以 `T/O` first layer不能再作为独立 prefix obstruction收费；真正新增信息必须来自真实 `a_3` digit window或更高 p-adic digit。本文是 no-double-count 审计，不关闭 A2。

---

## 1. source reused prime is noncentral and `B`-free

固定 genuine odd/odd source parity reused inert prime `r`。已有

\[
\boxed{r\mid18K-55,}
\tag{1.1}

并且 source parity collision theorem证明

\[
\boxed{r\nmid(2K-9)\omega.}
\tag{1.2}

另一方面 deep-even denominator为

\[
B=2^{M+m+1}c_ug.
\]

source-discriminant overlap给 genuine reused prime与 `c_u,g` 分离，因此

\[
\boxed{r\nmid B.}
\tag{1.3}

所以

\[
\boxed{2B^2(2K-9)\text{ 是模 }r\text{ 的单位}.}
\tag{1.4}

---

## 2. raw additive carrier is linear in `a_3`

height parity ledger给

\[
\boxed{
\Theta_{\rm dec}
=T\left[B^2(K^2-18K+55)-Q^2N_0\right]
-2B^2(2K-9)a_3.}
\tag{2.1}

若 residual

\[
r\mid T^\circ,
\]
则其 raw parent当然满足

\[
\boxed{r\mid\Theta_{\rm dec}.}
\tag{2.2}

由 (1.4)，(2.1) 对 `a_3` 是非退化的一次方程。因此 (2.2) 对任意已固定的 prefix state `(B,N)` 唯一恢复

\[
\boxed{
a_3
\equiv
\frac{T\left[B^2(K^2-18K+55)-Q^2N_0\right]}
{2B^2(2K-9)}
\pmod r.}
\tag{2.3}

不存在第二个 branch，也不存在 first-layer discriminant。

---

## 3. angle/source conditions do not remove this linear freedom

若同一 reused prime还进入某一 angle sheet `O_±`，source discriminant与 angle equation确实给 third-free必要 gate

\[
49\mathcal U_\Omega^2-220A^4Q^4=0\pmod r.
\tag{3.1}

再加 source collision

\[
18K-55=0
\]
后，(3.1) 是 `(B,N)` 上的一条 algebraic curve。

但它不含 `a_3`。因此在该 curve上的每个 genuine first-layer prefix point，(2.3) 仍然唯一给出一个 `a_3 mod r`。

所以：

\[
\boxed{
\text{source reuse}+O_\pm+T^\circ
\text{ 的 first layer保留一维 prefix freedom，且 }a_3\text{ 仅被唯一恢复}.}
\tag{3.2}

这与 `O/J` 情形完全不同：`J_H` 本身 pure-prefix，因此 `J_H=0` 与 (3.1) 两条 prefix equations对 `B` 消元后产生 pure-length octics。

---

## 4. cross-pair asymmetry

在 source odd/odd reuse sheet上：

### `J / angle`

\[
J_H=0,
\qquad
O_\pm=0
\]
投影到

\[
\boxed{\Phi_1(10^M)\Phi_2(10^M)=0\pmod r.}
\tag{4.1}

prefix continuous freedom消失。

### `T / angle`

\[
\Theta_{\rm dec}=0,
\qquad
O_\pm=0
\]
只给 angle prefix curve加唯一 `a_3` recovery (2.3)，不会生成纯 `N` first-layer resultant。

因此

\[
\boxed{
\text{两个 cross-pairs 在 source-reuse sheet上算术强度不对称}.}
\tag{4.2}

---

## 5. correct next target for the `T/O` side

由于 first layer的 `a_3 mod r` 总可唯一恢复，后续若继续 `T/O` overlap，不应再做普通 resultant/discriminant。真正可新增的输入只有：

1. 真实 third numerator defect
   \[
   a_3=T+h_3,
   \qquad0<h_3<T/250;
   \]
2. decimal exponent `m`；
3. `p^2` 以上要求恢复的 `a_3` residue必须与该 short digit interval相交。

所以 `T/O` 剩余问题属于 short-digit / multiplicative-orbit synchronization，而非 first-layer local geometry。

A2 仍为 `待证`。

# A2 equal-depth target 的 dual short carriers 与 exact sheet split

> **依赖：** `spontaneous-height-content-oversaturation.md`、`spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-equal-depth-square-core.md`、`primitive-reduction.md`。
>
> **严格状态：**本文把 omega-height target 的 fixed prefix quadratic 与真实第三块正定型放到同一个短-carrier框架中。当前 endpoint 下 prefix carrier `P=6K^2-36K+55` 恰有 `2M+3` 位，而 third carrier `R_3=6(a_3+3T)^2+T^2` 实际落在极窄区间 `97T^2<R_3<98T^2`。对 equal-depth target，二者的 p-depth 都精确等于 baseline `h`。更进一步，exact identity `T^2P-R_3=6 alpha L_3` 把 `gcd(P,R_3)` 精确分成互素的 numerator sheet `gcd(P,alpha)` 与 conjugate sheet `gcd(P,L_3)`，其中 `L_3=T(K-6)-a_3`；真正 equal-depth target 只进入 numerator sheet，并在那里以 exact depth `h` 出现。本文提供纯 decimal / prefix 的 baseline selector和全局乘积预算，不排除该 selector 的 inert support，因此不关闭 A2。

---

## 1. 两个 short carriers

沿用

\[
N=10^M,\qquad T=10^m,
\]

\[
\boxed{P:=\mathcal P_{\omega H}(K)=6K^2-36K+55,}
\tag{1.1}
\]

以及 `spontaneous-height-content-oversaturation.md` 的第三块正定型

\[
\boxed{R_3:=\mathscr R_{\omega H}=6(a_3+3T)^2+T^2.}
\tag{1.2}
\]

`spontaneous-height-equal-depth-target-ladder.md` 已证明

\[
\boxed{599N^2<P<600N^2,}
\tag{1.3}
\]

所以 `P` 恰有 `2M+3` 位。

当前 endpoint 更强地有

\[
1<\frac{a_3}{T}<\frac{251}{250}.
\tag{1.4}
\]

因此

\[
4<\frac{a_3+3T}{T}<\frac{1001}{250},
\]

从而

\[
97
<\frac{R_3}{T^2}
<6\left(\frac{1001}{250}\right)^2+1
=\frac{3037253}{31250}
<98.
\]

即

\[
\boxed{97T^2<R_3<98T^2.}
\tag{1.5}
\]

这把旧的粗界 `R_3<1015T^2` 收紧了一个数量级，并且只使用当前 endpoint 的真实 third-digit window。

---

## 2. 两个 primitive parts 都是 `3 mod 4`

当前 `a_2` 为奇数，且 `M>=11`，所以

\[
9\cdot10^{M-1}+a_2
\]

为奇数。由于

\[
K=10(9\cdot10^{M-1}+a_2),
\]
有

\[
\boxed{K\equiv10\pmod{20}.}
\tag{2.1}
\]

于是

\[
P=6K^2-36K+55\equiv15\pmod{20}.
\]
特别地 `5|P`，并且

\[
\boxed{\frac P5\equiv3\pmod4.}
\tag{2.2}
\]

另一方面 `a_3` 为奇数，而当前 `m>=5`，故 `T` 被 `8` 整除。于是

\[
(a_3+3T)^2\equiv1\pmod8,
\qquad T^2\equiv0\pmod8,
\]
所以

\[
\boxed{R_3\equiv6\pmod8,}
\tag{2.3}
\]

即

\[
\boxed{v_2(R_3)=1,
\qquad \frac{R_3}{2}\equiv3\pmod4.}
\tag{2.4}
\]

因此 prefix carrier 与 third carrier 在除去固定 decimal prime 后都各自携带 odd inert parity。本文不把这两份 parity自动视作独立 obstruction；下面先审计它们的公共 prime 如何分配。

---

## 3. exact two-sheet identity

真实 concatenated numerator 为

\[
\boxed{\alpha=TK+a_3.}
\tag{3.1}
\]

定义 conjugate linear form

\[
\boxed{L_3:=T(K-6)-a_3.}
\tag{3.2}
\]

直接展开：

\[
\begin{aligned}
T^2P-R_3
&=T^2(6K^2-36K+55)
  -\bigl(6a_3^2+36Ta_3+55T^2\bigr)\\
&=6(TK+a_3)(TK-a_3-6T).
\end{aligned}
\]

因此

\[
\boxed{T^2P-R_3=6\alpha L_3.}
\tag{3.3}
\]

同时

\[
\boxed{\alpha+L_3=2T(K-3),}
\tag{3.4}
\]

而

\[
\boxed{P=6(K-3)^2+1.}
\tag{3.5}
\]

所以

\[
\boxed{\gcd(P,K-3)=1.}
\tag{3.6}
\]

这将把 (3.3) 的两个 third-root sheets完全分离。

---

## 4. `gcd(P,R_3)` 的 exact coprime factorization

令

\[
G_{P3}:=\gcd(P,R_3).
\]

先注意 `P` 为奇数且

\[
P\equiv1\pmod3,
\]
所以 `2,3` 不整除 `G_{P3}`。

另外当前 source/primitive reduction给 `5\nmid\omega W_q=\alpha`，故 `5\nmid a_3`。因为 `T\equiv0 (mod 5)`：

\[
R_3\equiv6a_3^2\not\equiv0\pmod5.
\]
所以

\[
\boxed{\gcd(G_{P3},6T)=1.}
\tag{4.1}
\]

固定任意 `p|G_{P3}`，令

\[
r:=\min\{v_p(P),v_p(R_3)\}.
\]

由 (3.3)、(4.1)：

\[
p^r\mid\alpha L_3.
\tag{4.2}
\]

但 `p` 不可能同时整除 `alpha,L_3`。否则由 (3.4) 与 `p\nmid2T`：

\[
p\mid K-3,
\]
与 (3.6) 及 `p|P` 矛盾。

因此每个 `p|G_{P3}` 唯一落在两条 sheet 之一。

反过来，若 `p^s|P` 且 `p^s|alpha`，则 (3.3) 给 `p^s|R_3`；若 `p^s|P` 且 `p^s|L_3`，同理也有 `p^s|R_3`。逐 prime 比较 valuation 后得到 exact global factorization：

\[
\boxed{
\gcd(P,R_3)
=\gcd(P,\alpha)\,\gcd(P,L_3).}
\tag{4.3}
\]

并且由上面的 mutual exclusion：

\[
\boxed{
\gcd\bigl(\gcd(P,\alpha),\gcd(P,L_3)\bigr)=1.}
\tag{4.4}
\]

所以 `R_3` 的两个 p-adic roots已经在整数层被拆成两个互素 natural sheets：

- numerator sheet `alpha=0`；
- conjugate sheet `L_3=0`。

---

## 5. equal-depth target 只进入 numerator sheet，而且 depth 恰为 `h`

固定 genuine equal-depth omega-height target：

\[
v_p(\omega)=v_p(W_q)=h\ge1.
\]

于是

\[
\boxed{v_p(\alpha)=2h.}
\tag{5.1}
\]

而 target-ladder 已证明

\[
\boxed{v_p(P)=h.}
\tag{5.2}
\]

所以直接有

\[
\boxed{v_p(\gcd(P,\alpha))=h.}
\tag{5.3}
\]

由 (4.4)：

\[
\boxed{p\nmid\gcd(P,L_3).}
\tag{5.4}
\]

因此真正 equal-depth target 完全落在 numerator sheet，不会混入 conjugate sheet。

再由 (3.3)，因为 `v_p(alpha)=2h>h=v_p(P)` 且 `p\nmid T`：

\[
\boxed{v_p(R_3)=h.}
\tag{5.5}
\]

这也直接恢复了 equal-depth case 下 third carrier 的 exact baseline depth，而不需要额外使用 valuation bridge。

---

## 6. 所有 targets 的 global dual-carrier budget

令 `E_tar` 为所有当前 genuine equal-depth omega-height targets，并定义

\[
G_{\rm tar}:=\prod_{p\in E_{\rm tar}}p^{h_p}.
\]

由 (5.2)、(5.5)：

\[
\boxed{
G_{\rm tar}\mid P,
\qquad
G_{\rm tar}\mid R_3.}
\tag{6.1}
\]

更强地，由 (5.3)：

\[
\boxed{G_{\rm tar}\mid\gcd(P,\alpha).}
\tag{6.2}
\]

因此

\[
\boxed{
G_{\rm tar}\mid\gcd(P,R_3)
=\gcd(P,\alpha)\gcd(P,L_3).}
\tag{6.3}
\]

且所有 target prime powers都在第一个互素 factor 中。

由 (1.3)、(1.5)：

\[
\boxed{
G_{\rm tar}
<\min\{600N^2,98T^2\}.}
\tag{6.4}
\]

即

\[
\boxed{
\sum_{p\in E_{\rm tar}}h_p\log p
<\min\{\log600+2M\log10,
         \log98+2m\log10\}.}
\tag{6.5}
\]

这是一个完全不使用 source quotient 的 dual-length baseline budget。

---

## 7. composite target congruence

每个 target prime满足 `p^(2h_p)|alpha`，所以

\[
G_{\rm tar}^2\mid\alpha.
\tag{7.1}
\]

又 `G_tar|P,R_3`。把 (3.3) 除以 `G_tar`：

\[
T^2\frac{P}{G_{\rm tar}}
-\frac{R_3}{G_{\rm tar}}
=6\frac{\alpha}{G_{\rm tar}}L_3.
\]

右边仍被 `G_tar` 整除，因此

\[
\boxed{
T^2\frac{P}{G_{\rm tar}}
\equiv
\frac{R_3}{G_{\rm tar}}
\pmod{G_{\rm tar}}.}
\tag{7.2}
\]

而 target support 上两边都是 units。它把 prefix 与 third-block 两个短 carrier的 normalized first layer统一到同一个 composite modulus。

必须审计：该 congruence来自 exact sheet identity与 `alpha` square depth，本身不是新的独立 character obstruction；它的价值是给后续 global CRT / Archimedean comparison一个 source-free接口。

---

## 8. 当前 dual-short frontier

现在真正 equal-depth target baseline可以完全不用 source/sphere记号地读取：

\[
\boxed{
G_{\alpha P}:=\gcd(P,\alpha).}
\tag{8.1}
\]

对每个 target prime：

\[
\boxed{v_p(G_{\alpha P})=h_p.}
\tag{8.2}
\]

而第三块 companion给独立的短 carrier和 exact sheet audit：

\[
\boxed{
\gcd(P,R_3)
=G_{\alpha P}\cdot\gcd(P,L_3),
\qquad
\gcd(G_{\alpha P},\gcd(P,L_3))=1.}
\tag{8.3}
\]

因此后续若要关闭 `Sigma_deep` 的 inert support，不再需要把 third-block quadratic的另一根与 target混在一起；真正 target 已 canonical 地锁在 numerator sheet `G_{alpha P}` 中。

下一步最有价值的接口是：

1. 把 `Sigma_deep` 与 `G_{alpha P}` 取 gcd，得到 fully decimal target-baseline selector；
2. 审计 numerator/conjugate 两个互素 sheets各自承担的 `3 mod 4` parity；
3. 或把 (7.2) 与 `C_alpha=10TN-alpha` 的小 residue联立。

A2 仍为 `待证`。

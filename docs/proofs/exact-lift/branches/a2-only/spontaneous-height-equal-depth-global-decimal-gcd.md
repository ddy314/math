# A2 equal-depth square core 与 decimal pair 的 global gcd bridge

> **依赖：** `spontaneous-height-equal-depth-square-core.md`、`spontaneous-height-equal-depth-decimal-pair.md`、`spontaneous-height-content-oversaturation.md`。
>
> **严格状态：**本文把 equal-depth square core `G_eq` 与 decimal companion pair `E_+,E_-` 联立。所有 equal-depth oversaturation primes 在 `alpha,E_+` 中承担完整平方深度，在 `Delta_omega,E_-` 中只承担一半深度，因此得到 composite-modulus unit ratio。随后审计发现该 first-layer ratio 等价于已知 fixed quadratic `P_{omega H}(K)=0`，不能重复收费。真正新增的是 deep resonance 子集 `rho_p>=1` 会在 `E_+` 中比 square core 多贡献一份 squarefree radical：`G_deep^2 rad(G_deep)|E_+`。本文把局部 deep resonance 提升为全局 weighted-prime budget，但仍不关闭 A2。

---

## 1. equal-depth oversaturation product

沿用 square-core 文件的 prime 集合

\[
E_{\rm eq}
=\left\{
 p:\ p\text{ 为当前 genuine equal-depth oversaturation prime}
\right\}.
\]

对每个 `p in E_eq` 写

\[
\boxed{
v_p(\omega)=v_p(W_q)=h_p\ge1.}
\tag{1.1}
\]

定义

\[
\boxed{
G_{\rm eq}:=\prod_{p\in E_{\rm eq}}p^{h_p}.}
\tag{1.2}
\]

square-core 文件已经证明

\[
\boxed{G_{\rm eq}^2\mid\alpha.}
\tag{1.3}
\]

而 exact decimal determinant

\[
\Delta_\omega=E_MN\omega
\]
在每个 target prime 上满足 `p not| E_MN`，故

\[
\boxed{v_p(\Delta_\omega)=h_p.}
\tag{1.4}
\]

所以全局有

\[
\boxed{G_{\rm eq}\mid\Delta_\omega,}
\tag{1.5}
\]
并且相对于 modulus `G_eq^2` 是 exact half-depth：

\[
\boxed{
\gcd(\Delta_\omega,G_{\rm eq}^2)
=G_{\rm eq}.}
\tag{1.6}
\]

---

## 2. decimal companion pair 对同一 square core 的深度

`spontaneous-height-equal-depth-decimal-pair.md` 已证明逐 prime

\[
\boxed{v_p(\mathcal E_-)=h_p,}
\tag{2.1}
\]

\[
\boxed{
v_p(\mathcal E_+)
\ge2h_p+\min(r_{B,p},h_p,\rho_p).}
\tag{2.2}
\]

特别地无论 `rho_p` 是否为正：

\[
\boxed{v_p(\mathcal E_+)\ge2h_p.}
\tag{2.3}
\]

因此聚合所有 distinct primes：

\[
\boxed{G_{\rm eq}^2\mid\mathcal E_+,}
\tag{2.4}
\]

\[
\boxed{
\gcd(\mathcal E_-,G_{\rm eq}^2)
=G_{\rm eq}.}
\tag{2.5}
\]

于是同一个 equal-depth square modulus 在三个真实 decimal integers 中的 target-prime 深度是

\[
\boxed{
\begin{array}{c|c}
\text{integer}&E_{\rm eq}\text{ prime depth}\\ \hline
\alpha&2h_p\\
\mathcal E_+&\ge2h_p\\
\Delta_\omega&h_p\\
\mathcal E_-&h_p.
\end{array}}
\tag{2.6}
\]

这已经完全摆脱 source quotient。

---

## 3. composite-modulus unit ratio

两个 decimal companions 满足 exact difference

\[
\boxed{
\mathcal E_+-\mathcal E_-
=2K\Delta_\omega.}
\tag{3.1}
\]

由 (2.4)：

\[
\mathcal E_-+2K\Delta_\omega
\equiv0\pmod{G_{\rm eq}^2}.
\tag{3.2}
\]

由 (1.5)、(2.5) 可除去一份 `G_eq`：

\[
\boxed{
\frac{\mathcal E_-}{G_{\rm eq}}
\equiv
-2K\frac{\Delta_\omega}{G_{\rm eq}}
\pmod{G_{\rm eq}}.}
\tag{3.3}
\]

并且两边都是 modulus `G_eq` 的单位：

\[
\boxed{
\gcd\left(\frac{\mathcal E_-}{G_{\rm eq}},G_{\rm eq}\right)
=
\gcd\left(\frac{\Delta_\omega}{G_{\rm eq}},G_{\rm eq}\right)
=1.}
\tag{3.4}
\]

所以 equal-depth pool 已经产生一个单一 composite modulus 上的 projective unit synchronization，而不需要逐 prime 写 `omega_0,W_0`。

---

## 4. no-double-count audit：first-layer unit ratio 只是 `P_omegaH` root

必须检查 (3.3) 是否真的独立。

由

\[
\Delta_\omega=K\beta-Q\alpha
\tag{4.1}
\]
以及 `G_eq^2|alpha`：

\[
\frac{\Delta_\omega}{G_{\rm eq}}
\equiv
K\frac\beta{G_{\rm eq}}
\pmod{G_{\rm eq}}.
\tag{4.2}
\]

另一方面

\[
\mathcal E_-
=F_H(K)\beta-K\Delta_\omega,
\]
其中

\[
F_H(K)=5K^2-36K+55.
\]
除以 `G_eq` 并使用 (4.2)：

\[
\frac{\mathcal E_-}{G_{\rm eq}}
\equiv
\left(F_H(K)-K^2\right)
\frac\beta{G_{\rm eq}}
\pmod{G_{\rm eq}}.
\tag{4.3}
\]

把 (3.3) 右边也用 (4.2) 改写，并利用 `beta/G_eq`、`K` 都是 units，得到

\[
F_H(K)-K^2
\equiv-2K^2
\pmod{G_{\rm eq}}.
\]
也就是

\[
\boxed{
6K^2-36K+55
=\mathcal P_{\omega H}(K)
\equiv0
\pmod{G_{\rm eq}}.}
\tag{4.4}
\]

这正是 parent oversaturation 已经得到的 fixed quadratic root，聚合到 composite modulus 后的重写。

所以：

\[
\boxed{
\text{(3.3) 的 first layer 不构成新的 obstruction。}}
\tag{4.5}
\]

它的作用是给后面的 deep-radical amplification 提供完全 decimal 的统一接口。

---

## 5. deep resonance primes 额外贡献一份 radical

定义 deep subset

\[
\boxed{
E_{\rm deep}
:=\{p\in E_{\rm eq}:\rho_p\ge1\}.}
\tag{5.1}
\]

令

\[
\boxed{
G_{\rm deep}
:=\prod_{p\in E_{\rm deep}}p^{h_p},
\qquad
R_{\rm deep}
:=\operatorname{rad}(G_{\rm deep})
=\prod_{p\in E_{\rm deep}}p.}
\tag{5.2}
\]

对每个 deep prime，decimal-pair 文件给

\[
v_p(\mathcal E_+)\ge2h_p+1.
\]
由于这些 prime 互异，直接聚合：

\[
\boxed{
G_{\rm deep}^2R_{\rm deep}
\mid\mathcal E_+.}
\tag{5.3}
\]

这就是 first-layer square core 之外真正新增的 global cost：每一枚 deep resonance prime 至少还要额外支付**一份 squarefree radical**。

由 fixed decimal window

\[
\mathcal E_+<1053\,TN^3
=1053\cdot10^{m+3M}
\]
得到

\[
\boxed{
G_{\rm deep}^2R_{\rm deep}
<1053\cdot10^{m+3M}.}
\tag{5.4}
\]

等价地

\[
\boxed{
\sum_{p\in E_{\rm deep}}
(2h_p+1)\log p
<
\log1053+(m+3M)\log10.}
\tag{5.5}
\]

这把局部 `rho_p>=1` 提升成了一个全局 weighted-prime budget。

---

## 6. 同一个 square modulus 现在控制两个真实 decimal residues

square-core 文件还给

\[
\boxed{
10TN\equiv C_\alpha
\pmod{G_{\rm eq}^2},}
\tag{6.1}
\]
其中

\[
0<C_\alpha<\frac{TN}{250}.
\]

而本文有

\[
\boxed{
\mathcal E_-
\equiv-2K\Delta_\omega
\pmod{G_{\rm eq}^2}.}
\tag{6.2}
\]

因此同一个 original-integer square core `G_eq^2` 已同时控制：

1. `10TN` 的小 positive endpoint residue `C_alpha`；
2. `E_-` 的 determinant residue `-2K Delta_omega`；
3. deep subset 还通过 (5.3) 在 `E_+` 上额外支付 radical。

这正是前一 square-core 文件留下的“两个 independent decimal residues”接口。

---

## 7. 当前 global frontier

综合本文：

\[
\boxed{
\begin{gathered}
G_{\rm eq}^2\mid\alpha,\mathcal E_+,\\
\gcd(\Delta_\omega,G_{\rm eq}^2)
=\gcd(\mathcal E_-,G_{\rm eq}^2)
=G_{\rm eq},\\
10TN\equiv C_\alpha\pmod{G_{\rm eq}^2},\\
\mathcal E_-\equiv-2K\Delta_\omega
\pmod{G_{\rm eq}^2},\\
G_{\rm deep}^2\operatorname{rad}(G_{\rm deep})
\mid\mathcal E_+.
\end{gathered}}
\tag{7.1}
\]

其中 composite unit congruence 的 first layer 已审计为旧 `P_{omega H}` root，不重复计作障碍；真正新信息是 deep subset 的额外 radical 与两个真实 decimal residue共享同一 square modulus。

下一步若要逼近 closure，应研究：

- `C_alpha` 很小时，(6.1) 对 `G_eq^2` 的 natural representative 是否与 (6.2) 同时可行；
- `G_deep^2 rad(G_deep)` 与 `alpha` 的更短 `m+M+1` 位 square-core budget 是否可联合给出 radical 过饱和；
- 或构造二阶 corrected `E_+`，继续读取 `rho_p>min(h_p,r_{B,p})` 的 tail。
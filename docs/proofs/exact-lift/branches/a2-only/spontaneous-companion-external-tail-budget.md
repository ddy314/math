# A2 external `J^circ/B^circ` common depth 的 decimal tail budget

> **依赖：** `spontaneous-companion-common-parity-dichotomy.md`、`spontaneous-height-companion-cross.md`、`spontaneous-height-equal-depth-tail-reader.md`、`spontaneous-height-equal-depth-tail-normalization.md`。
>
> **严格状态：**上一层把 `G_JB=gcd(J^circ,B^circ)` 的 common parity分成 external 与 height-supported 两类，并证明 generic external common exponent `k` 全部进入 linear gate `L_JB`。本文进一步证明 generic external common prime不能进入 `omega` content：因为 `p∤W_q` 且 `L_JB=2Dg omega K-fqW_q`，若 `p|omega` 则第二项为唯一 unit，和 `p|L_JB` 矛盾。因此 external common prime与 `alpha=omega W_q` 分离；full-tail decimal identity随即把 `L_JB` 的完整深度无损搬到 `Lambda_dec`，而 tail normalization在该 prime上不约掉任何 p-factor。于是整个 generic external `G_JB` subproduct整除 pure-decimal `Lambda_tail`。本文不排除该 subproduct，因此不关闭 A2。

---

## 1. generic external common setting

固定 genuine inert external common prime `p`，满足

\[
p\mid G_{JB}:=\gcd(J^\circ,B^\circ),
\qquad
p\nmid W_q.
\tag{1.1}
\]

沿用 generic separation

\[
\boxed{
p\nmid2\cdot5\cdot DgKfqzb_3E_Mc_u.}
\tag{1.2}
\]

固定 source/contact exceptional primes继续由既有文件单列；本文只处理真正 moving generic external sector。

写

\[
j:=v_p(J^\circ),
\qquad
b:=v_p(B^\circ),
\]

\[
\boxed{k:=v_p(G_{JB})=\min(j,b)\ge1.}
\tag{1.3}
\]

上一层已证明

\[
\boxed{v_p(L_{JB})\ge k,}
\tag{1.4}
\]

若 `j!=b` 则等号成立。

---

## 2. external common prime cannot divide `omega`

已有 exact form

\[
\boxed{
L_{JB}=2Dg\omega K-fqW_q.}
\tag{2.1}
\]

由 (1.1),(1.2)：

\[
p\nmid fqW_q.
\]

若假设

\[
p\mid\omega,
\]

则 (2.1) 模 `p` 变成

\[
L_{JB}\equiv-fqW_q\not\equiv0\pmod p,
\]

与 `p|G_JB -> p|L_JB` 矛盾。

因此

\[
\boxed{p\nmid\omega.}
\tag{2.2}
\]

结合 `p∤W_q`：

\[
\boxed{p\nmid\alpha=\omega W_q.}
\tag{2.3}
\]

所以 generic external companion-common prime既不是 height prime，也不是 concatenated numerator-content prime。

---

## 3. full-tail identity reads `L_JB` exactly

full decimal tail reader已有全局 exact identity

\[
\boxed{
b_3E_M\omega L_{JB}
=c_u\Lambda_{\rm dec}.}
\tag{3.1}
\]

在当前 generic external prime上，由 (1.2),(2.2)：

\[
p\nmid b_3E_M\omega c_u.
\]

所以 (3.1) 给精确 valuation equality

\[
\boxed{
v_p(\Lambda_{\rm dec})
=v_p(L_{JB}).}
\tag{3.2}
\]

结合 (1.4)：

\[
\boxed{
v_p(\Lambda_{\rm dec})
\ge v_p(G_{JB}).}
\tag{3.3}
\]

如果 `j!=b`：

\[
\boxed{
v_p(\Lambda_{\rm dec})
=v_p(G_{JB})=k.}
\tag{3.4}
\]

只有 equal companion depth `j=b` 时，tail reader才可能继续更深。

---

## 4. normalization removes no external p-factor

canonical tail quotient为

\[
\boxed{
\Lambda_{\rm tail}
:=\frac{\Lambda_{\rm dec}}
{\gcd(\alpha,\Lambda_{\rm dec})}.}
\tag{4.1}
\]

由 (2.3)，`p∤alpha`，因此

\[
v_p(\gcd(\alpha,\Lambda_{\rm dec}))=0.
\]

所以

\[
\boxed{
v_p(\Lambda_{\rm tail})
=v_p(\Lambda_{\rm dec})
=v_p(L_{JB})
\ge k.}
\tag{4.2}
\]

这把 external common depth从 source linear gate完全搬到了 ordinary decimal tail quotient。

---

## 5. global generic external common product

令 `E_ext` 为 generic external common primes集合，并定义

\[
\boxed{
G_{JB}^{\rm ext}
:=\prod_{p\in E_{\rm ext}}
p^{v_p(G_{JB})}.}
\tag{5.1}
\]

逐 prime由 (4.2)：

\[
\boxed{G_{JB}^{\rm ext}\mid\Lambda_{\rm tail}.}
\tag{5.2}
\]

而 tail normalization给

\[
\Lambda_{\rm tail}
=\frac{\Lambda_{\rm dec}}{\omega\Gamma},
\qquad
\Gamma=\gcd(\omega,W_q),
\]
以及

\[
44T^2N^3<\Lambda_{\rm dec}<45T^2N^3.
\]

因此

\[
\boxed{
G_{JB}^{\rm ext}
\le\Lambda_{\rm tail}
<\frac{45T^2N^3}{\omega\Gamma}.}
\tag{5.3}
\]

若只需不含 source quantities 的粗界：

\[
\boxed{G_{JB}^{\rm ext}<45T^2N^3.}
\tag{5.4}
\]

---

## 6. updated companion-parity trichotomy

在危险 parent orientation `D_H=1 mod4` 中，上一层三岔现在加强为：

1. **split residual parity**：`G_JB=1 mod4`，需要两枚不同 inert residual suppliers；
2. **common external parity**：common inert supplier位于 external sector，其完整 `G_JB` depth进入 `Lambda_tail`，满足 (5.3)；
3. **common height-supported parity**：进入 omega-content oversaturation，随后按 unequal/equal-depth与 serial hierarchy继续分类。

因此 case B 已从 source linear gate升级为 pure-decimal global height budget。

特别地，不能把 case B 和 equal-depth tail混为同一 prime pool：external common prime满足

\[
p\nmid\omega W_q,
\]
而 equal-depth target prime满足

\[
p\mid\omega W_q.
\]

两者在 support 上严格互斥，只是都由同一个 canonical `Lambda_tail` 记录各自的 resonance depth。

A2 仍为 `待证`。

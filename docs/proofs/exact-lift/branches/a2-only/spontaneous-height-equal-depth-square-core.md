# A2 equal-depth oversaturation 的 concatenated square core

> **依赖：** `spontaneous-height-equal-depth-resonance.md`、`spontaneous-height-oversaturation-depth-ledger.md`、`primitive-reduction.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文把逐 prime 的 `e=v_p(omega)` / `h=v_p(W_q)` 二分提升为 `alpha=omega W_q` 的全局 square-core factorization。`Gamma=gcd(omega,W_q)` 的平方完整进入真实拼接 numerator，而 residual cofactor 的逐 prime 深度恰为 `|e-h|`；更进一步，`Gamma` 可完全恢复为原始整数的三重 gcd `gcd(alpha,beta,H_0)`，所以该 square core 无需 source 记号即可定义。对当前 endpoint，`alpha` 恰有 `m+M+1` 位，并且距顶部 `10TN` 只有一个显式小 defect `C_alpha=10Te_2-a_3`。所有 equal-depth oversaturation primes 的总平方块共同整除 `alpha`，从而受到单一 `sqrt(alpha)` 高度约束；若该平方模数超过 `C_alpha`，后者就是 `10TN` 模整个 equal-depth square core 的最小正代表。本文给出新的 global allocation / CRT 接口，不宣称 A2 closure。

---

## 1. `omega/W_q` 的 canonical square-core decomposition

沿用

\[
\boxed{\alpha=TK+a_3=\omega W_q.}
\tag{1.1}
\]

定义

\[
\boxed{\Gamma:=\gcd(\omega,W_q),}
\tag{1.2}
\]
以及

\[
\boxed{
\omega^\circ:=\frac\omega\Gamma,
\qquad
W^\circ:=\frac{W_q}{\Gamma}.}
\tag{1.3}
\]

由 gcd 定义：

\[
\boxed{\gcd(\omega^\circ,W^\circ)=1.}
\tag{1.4}
\]

因此

\[
\boxed{
\alpha
=\Gamma^2\omega^\circ W^\circ.}
\tag{1.5}
\]

这给出了 `alpha` 的 canonical common-square / imbalance factorization。

`primitive-reduction.md` 已经证明

\[
\omega=\gcd(\alpha,\beta),
\qquad
W_q=\gcd(\alpha,H_0),
\tag{1.6}
\]
并且

\[
\beta=\omega S,
\qquad
H_0=c_uW_q,
\qquad
\gcd(W_q,S)=1,
\qquad
\gcd(\omega,c_u)=1.
\tag{1.7}
\]

因此 `Gamma` 还有一个完全 original-integer 的读取器：

\[
\boxed{
\Gamma
=\gcd(\omega,W_q)
=\gcd(\alpha,\beta,H_0).}
\tag{1.8}
\]

逐 prime 验证很直接。若

\[
e=v_p(\omega),\quad
h=v_p(W_q),\quad
s=v_p(S),\quad
c=v_p(c_u),
\]
则 (1.7) 给

\[
\min(h,s)=0,
\qquad
\min(e,c)=0.
\]
而三原始整数的赋值分别为

\[
e+h,\qquad e+s,\qquad c+h.
\]
所以

\[
\min(e+h,e+s,c+h)=\min(e,h),
\]
恰好就是 `v_p(Gamma)`。

因此本文的 common square core 不依赖后续 source quotient 的选取：它就是**原拼接 numerator、原拼接 denominator 与整数 sphere height 的三重公共部分**。

逐 prime 写

\[
e_p:=v_p(\omega),
\qquad
h_p:=v_p(W_q).
\]
则

\[
v_p(\Gamma)=\min(e_p,h_p),
\]
而

\[
\boxed{
v_p(\omega^\circ W^\circ)
=|e_p-h_p|.}
\tag{1.9}
\]

所以：

\[
\boxed{
e_p=h_p
\Longleftrightarrow
p\mid\Gamma\ \text{且}\ p\nmid\omega^\circ W^\circ}
\tag{1.10}
\]
（这里默认 `e_p=h_p>=1`）。

换句话说，前两轮逐 prime 发现的 equal-depth / unequal-depth dichotomy 已经有一个完全 canonical 的全局含义：

- equal-depth common prime 完全被吸收到 `Gamma^2`；
- unequal-depth common prime 在抽掉共同平方后仍留下 `|e_p-h_p|` 层，并且因为 (1.4) 只能留在 `omega^circ` 或 `W^circ` 的一边。

---

## 2. equal-depth oversaturation primes 的总平方块

令 `E_eq` 为当前 height companion oversaturation 中满足

\[
p\equiv7,11\pmod{24},
\qquad
v_p(\omega)=v_p(W_q)=h_p\ge1
\]
的 distinct primes 集合。

定义

\[
\boxed{
G_{\rm eq}:=\prod_{p\in E_{\rm eq}}p^{h_p}.}
\tag{2.1}
\]

由 (1.5)、(1.10)：

\[
\boxed{G_{\rm eq}\mid\Gamma,}
\tag{2.2}
\]

且更重要地

\[
\boxed{G_{\rm eq}^2\mid\alpha.}
\tag{2.3}
\]

同时每个 `p in E_eq` 在

\[
\alpha/G_{\rm eq}^2
\]
中已没有剩余 p-factor。因此 equal-depth oversaturation 的整个指定 prime pool 在真实 numerator 中表现为一个**完整平方块**，不再只是若干互不关联的局部条件。

---

## 3. 真实拼接 numerator `alpha` 恰有 `m+M+1` 位

当前 endpoint defect parametrization 为

\[
\boxed{
a_2=10^{M-1}-e_2,}
\qquad
0<e_2<\frac{10^{M-1}}{250},
\tag{3.1}
\]

以及

\[
\boxed{
a_3=T+h_3,}
\qquad
0<h_3<\frac{T}{250},
\qquad T=10^m.
\tag{3.2}
\]

令

\[
N=10^M.
\]
则

\[
K=9N+10a_2
=10N-10e_2.
\tag{3.3}
\]

由 `e_2<N/2500`：

\[
\boxed{
\frac{2499}{250}N<K<10N.}
\tag{3.4}
\]

因此

\[
\alpha=TK+a_3
>\frac{2499}{250}TN.
\tag{3.5}
\]

另一方面 `e_2>=1`，而

\[
a_3<\frac{251}{250}T.
\]
所以

\[
\begin{aligned}
\alpha
&=10TN-10Te_2+a_3\\
&<10TN-10T+\frac{251}{250}T\\
&=10TN-\frac{2249}{250}T
<10TN.
\end{aligned}
\tag{3.6}
\]

于是

\[
\boxed{
\frac{2499}{250}\,10^{m+M}
<\alpha
<10^{m+M+1}.}
\tag{3.7}
\]

特别地

\[
\boxed{
\alpha
\text{ 恰有 }m+M+1\text{ 个十进制数字}.}
\tag{3.8}
\]

---

## 4. 单个 equal-depth prime 的 square-depth 高度界

若

\[
v_p(\omega)=v_p(W_q)=h,
\]
则由 `alpha=omega W_q`：

\[
\boxed{v_p(\alpha)=2h.}
\tag{4.1}
\]

所以

\[
\boxed{p^{2h}\Vert\alpha.}
\tag{4.2}
\]

结合 (3.7)：

\[
\boxed{p^{2h}<10^{m+M+1}.}
\tag{4.3}
\]

这比 `E_+` 的 `m+3M+4` 位 bound 更短；`E_+` 的额外价值在于读取 resonance tail `rho_p`，而 `alpha` 则是 equal-depth **基础平方深度 `2h`** 的最短自然代表。

---

## 5. 所有 equal-depth oversaturation primes 的 global product bound

由 (2.3)、(3.7)：

\[
G_{\rm eq}^2\le\alpha<10TN.
\]
所以

\[
\boxed{
G_{\rm eq}
<\sqrt{10TN}
=10^{(m+M+1)/2}.}
\tag{5.1}
\]

等价地

\[
\boxed{
\sum_{p\in E_{\rm eq}}h_p\log p
<\frac12(m+M+1)\log10.}
\tag{5.2}
\]

这是一条真正的 global allocation inequality：所有 equal-depth oversaturation primes 不再能各自独立消耗高度，它们必须共同装进同一个 `alpha` square core。

---

## 6. 顶部 complement 是一个远小于 `alpha` 的真实 endpoint defect

定义

\[
\boxed{
C_\alpha:=10TN-\alpha.}
\tag{6.1}
\]

由 (3.3)：

\[
\boxed{
C_\alpha=10Te_2-a_3.}
\tag{6.2}
\]

由于 `e_2>=1`、`a_3<251T/250`：

\[
\boxed{
C_\alpha>\frac{2249}{250}T.}
\tag{6.3}
\]

另一方面 `e_2<N/2500` 且 `a_3>T>0`：

\[
C_\alpha
<\frac{TN}{250}-T
<\frac{TN}{250}.
\]
所以

\[
\boxed{
\frac{2249}{250}T
<C_\alpha
<\frac1{250}TN.}
\tag{6.4}
\]

因此 `alpha` 位于十进制顶部 `10TN` 下方一个相对小于 `1/2500` 的显式整数 defect 内。

---

## 7. equal-depth square core 的 CRT natural representative

由 (2.3)：

\[
\alpha\equiv0\pmod{G_{\rm eq}^2}.
\]
结合 (6.1)：

\[
\boxed{
10TN\equiv C_\alpha
\pmod{G_{\rm eq}^2}.}
\tag{7.1}
\]

所有 `p in E_eq` 都是 genuine non-`3` inert prime，因此

\[
\gcd(G_{\rm eq},10TN)=1.
\]
从 (7.1) 也有

\[
\boxed{
\gcd(G_{\rm eq},C_\alpha)=1.}
\tag{7.2}
\]

若进一步进入规模区间

\[
\boxed{G_{\rm eq}^2>C_\alpha,}
\tag{7.3}
\]
那么 (7.1)、`0<C_alpha<G_eq^2` 立即说明：

\[
\boxed{
C_\alpha
=10TN\bmod G_{\rm eq}^2
}
\tag{7.4}
\]
是最小正代表。

所以 large equal-depth square core 不再只是抽象因子乘积；它会把真实 endpoint defect `10Te_2-a_3` 直接固定成一个 CRT representative。

---

## 8. 当前 square-core frontier

现在 `omega/W_q` overlap 可统一看成

\[
\boxed{
\alpha
=\Gamma^2\omega^\circ W^\circ,
\qquad
\Gamma=\gcd(\alpha,\beta,H_0),
\qquad
\gcd(\omega^\circ,W^\circ)=1,}
\tag{8.1}
\]

其中

\[
v_p(\omega^\circ W^\circ)=|e_p-h_p|.
\]

因此：

- unequal-depth sector 已由 residual-depth ledger 控制，并显式留在 imbalance cofactor；
- equal-depth sector 完全进入由原始整数三重 gcd 读取的 square core；
- equal-depth oversaturation pool 的总尺度满足 (5.1)；
- 当该 pool 足够大时，顶部小 defect `C_alpha` 成为其平方模数的 exact natural residue。

下一步若要继续压缩 equal-depth pool，最有希望的接口是把 (7.1) 与 `E_+/E_-` 的 near-equal decimal pair 或 determinant `Delta_omega=E_MN omega` 联立，从而让同一个 `G_eq` 同时控制两个独立的真实 decimal residues。
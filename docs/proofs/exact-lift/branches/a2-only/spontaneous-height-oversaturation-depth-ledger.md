# A2 height companion oversaturation 的 residual-depth ledger

> **依赖：** `spontaneous-height-content-oversaturation.md`、`spontaneous-height-resultant-parity.md`、`spontaneous-height-companion-cross.md`、`spontaneous-height-parity-ledger.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文是 `spontaneous-height-content-oversaturation.md` 的下一层 depth audit。对已经满足 `p|omega`、`p|W_q` 且 `J_H/B_W` 在完整 height gcd 之后继续共同加深的 genuine non-`3` inert prime，本文证明：`J_H` 本身就是一个恰有 `4M+1` 位的 positive pure-prefix carrier，并完整承担 `p^{h+1}`；更短的 prefix height carrier `H_pref=B^2K^2+Q^2N_0` 只需 `4M+1` 位便承担 `p^{min(e,h+1)}`，在 `e<=h` 时其 p-adic 深度精确等于 `e`。此外利用 `J_H/B_W` 的 exact difference，若 `e!=h`，两 companion 的较浅 oversaturation residual depth 至多为 `min(e,h)`，若两边深度不同则恰等于 `min(e,h)`。因此任意超出这一 cap 的行为只能进入唯一的 equal-depth resonance `e=h`。本文不排除该 resonance，也不关闭 A2。

---

## 1. 记号与 oversaturation 深度

沿用 parent 文件的 genuine non-`3` inert prime `p`。令

\[
 e:=v_p(\omega)\ge1,
 \qquad
 h:=v_p(W_q)\ge1,
\]

并记

\[
 j:=v_p(\widehat{\mathcal J}_H)
   =v_p(\mathcal J_H),
 \qquad
 V:=v_p(\mathscr B_W).
\]

因为 `D_H` 在该 prime 上已经完整吃掉 `W_q` 的 `p^h`，而

\[
p\mid J^\circ,
\qquad
p\mid B^\circ,
\]
所以

\[
\boxed{j\ge h+1,\qquad V\ge h+1.}
\tag{1.1}
\]

定义两个 residual depths

\[
\boxed{
r_J:=j-h\ge1,
\qquad
r_B:=V-h\ge1.}
\tag{1.2}
\]

parent 文件已经证明

\[
\boxed{p\mid\omega,}
\tag{1.3}
\]

并定义 fixed quadratic

\[
\boxed{
\mathcal P_{\omega H}(K)
:=6K^2-36K+55.
}
\tag{1.4}
\]

---

## 2. `J_H` 自身已经给出一个更短的 pure-prefix depth carrier

沿用

\[
B=b_2,
\qquad
Q=B+2N,
\qquad
N=10^M,
\]

\[
N_0=\left(\frac{9B}{2}\right)^2+a_2^2,
\]
以及

\[
\mathcal J_H
=B^2(5K^2-36K+55)-Q^2N_0.
\tag{2.1}
\]

由 (1.1) 直接有

\[
\boxed{p^{h+1}\mid\mathcal J_H.}
\tag{2.2}
\]

这比 parent 文件的 resultant depth

\[
p^{\min(e,h+1)}\mid\mathscr R_{\omega H}^{\rm pref}
\]
在 `e<h+1` 时更强，因为 (2.2) **无条件读取完整 `h+1` depth**。

当前 endpoint box 为

\[
\frac1{10}<x:=\frac BN<\frac2{19},
\qquad
\frac{249}{250}<y:=\frac{10a_2}{N}<1,
\qquad
\tau=N^{-1}<10^{-11},
\]

并令

\[
s:=9+y.
\]
则

\[
\frac{\mathcal J_H}{N^4}
=x^2\left(5s^2-36s\tau+55\tau^2\right)
-(x+2)^2
\left(\frac{2025x^2+y^2}{100}\right).
\tag{2.3}
\]

由

\[
x>\frac1{10},
\quad
s>\frac{2499}{250},
\quad
(x+2)^2\frac{2025x^2+y^2}{100}<\frac{26}{25},
\]
有

\[
\frac{\mathcal J_H}{N^4}
>
\frac1{100}
\left[
5\left(\frac{2499}{250}\right)^2
-\frac{360}{10^{11}}
\right]
-\frac{26}{25}
>rac{79}{20}.
\tag{2.4}
\]

另一方面忽略负项并用 `x<2/19`、`s<10`：

\[
\frac{\mathcal J_H}{N^4}
<
\frac4{361}
\left(500+\frac{55}{10^{22}}\right)
<\frac{111}{20}.
\tag{2.5}
\]

所以

\[
\boxed{
\frac{79}{20}N^4
<\mathcal J_H
<\frac{111}{20}N^4.
}
\tag{2.6}
\]

特别地

\[
\boxed{
\mathcal J_H
\text{ 恰有 }4M+1\text{ 个十进制数字}.}
\tag{2.7}
\]

结合 (2.2)：

\[
\boxed{
p^{h+1}<\frac{111}{20}\,10^{4M}.}
\tag{2.8}
\]

因此 oversaturation 的完整 height depth `h+1` 已经被一个比 `8M+2` 位 resultant 短一半的 pure-prefix natural representative 控制。

---

## 3. `J_H` 的 primitive orientation 实际是 `7 mod 8`

已有

\[
B=2^{M+m+1}b_0,
\qquad
Q=2^{M+1}Q_0,
\]
其中 `b_0,Q_0` 为奇数。

当前 endpoint 还有

\[
\lambda>\frac{3M}{7},
\qquad
m\ge\lambda,
\qquad
M\ge11,
\]
故

\[
\boxed{m\ge5.}
\tag{3.1}
\]

`N_0` 为奇数，并且更精确地

\[
N_0\equiv a_2^2\equiv1\pmod8,
\tag{3.2}
\]
因为 `(9B/2)^2` 含很深的 `2`-power。

把 (2.1) 除以 `2^{2M+2}`：第一项含因子 `2^{2m}`，由 (3.1) 在模 `8` 下消失；第二项给

\[
-Q_0^2N_0\equiv-1\equiv7\pmod8.
\]
所以

\[
\boxed{
v_2(\mathcal J_H)=2M+2,
\qquad
\frac{\mathcal J_H}{2^{2M+2}}
\equiv7\pmod8.}
\tag{3.3}
\]

这强化了旧的 `3 mod 4` orientation；但它仍只是 global parity information，不能单独排除指定的 oversaturation prime。

---

## 4. 更短的 `H_pref` carrier：只有 `4M+1` 位

定义 parent 文件已经使用的

\[
\boxed{
\mathscr H_{\omega H}^{\rm pref}
:=B^2K^2+Q^2N_0.
}
\tag{4.1}
\]

有 exact identity

\[
\boxed{
\mathcal J_H
=B^2\mathcal P_{\omega H}(K)
-\mathscr H_{\omega H}^{\rm pref}.}
\tag{4.2}
\]

parent 文件给

\[
\ell_p:=\min(e,h+1),
\]

\[
p^{\ell_p}\mid\mathcal P_{\omega H}(K).
\tag{4.3}
\]

而 (2.2) 当然也给

\[
p^{\ell_p}\mid\mathcal J_H.
\]
由于 `p\nmid B`，由 (4.2)：

\[
\boxed{
p^{\ell_p}\mid
\mathscr H_{\omega H}^{\rm pref}.}
\tag{4.4}
\]

这条 divisibility 不需要再经过 degree-2 resultant。

写

\[
n_0:=\frac{N_0}{N^2}
=\frac{81}{4}x^2+\frac{y^2}{100}.
\]
则

\[
\frac{\mathscr H_{\omega H}^{\rm pref}}{N^4}
=x^2s^2+(x+2)^2n_0.
\tag{4.5}
\]

利用

\[
 n_0>\frac{53}{250},
 \qquad
 (x+2)^2>\left(\frac{21}{10}\right)^2,
\]
以及 `x>1/10,s>2499/250`：

\[
\frac{\mathscr H_{\omega H}^{\rm pref}}{N^4}
>
\frac1{100}\left(\frac{2499}{250}\right)^2
+\left(\frac{21}{10}\right)^2\frac{53}{250}
>rac{193}{100}.
\tag{4.6}
\]

上界则由

\[
x^2s^2<\frac{400}{361},
\qquad
(x+2)^2n_0<\frac{26}{25}
\]
得到

\[
\frac{\mathscr H_{\omega H}^{\rm pref}}{N^4}
<\frac{400}{361}+\frac{26}{25}
<\frac{43}{20}.
\tag{4.7}
\]

因此

\[
\boxed{
\frac{193}{100}N^4
<\mathscr H_{\omega H}^{\rm pref}
<\frac{43}{20}N^4.}
\tag{4.8}
\]

特别地

\[
\boxed{
\mathscr H_{\omega H}^{\rm pref}
\text{ 也恰有 }4M+1\text{ 个十进制数字}.}
\tag{4.9}
\]

由 (4.4)：

\[
\boxed{
p^{\min(e,h+1)}
<\frac{43}{20}\,10^{4M}.}
\tag{4.10}
\]

这把 parent 文件的

\[
p^{\min(e,h+1)}<39\cdot10^{8M}
\]
提升为真正的 `4M`-scale bound。

---

## 5. `H_pref` 的 primitive orientation 为 `1 mod 8`

`K=10P` 且 `P` 为奇数，所以

\[
v_2(K)=1.
\]

因此 `B^2K^2` 的二进深度为

\[
2M+2m+4,
\]
而 `Q^2N_0` 的二进深度恰为

\[
2M+2.
\]
故

\[
\boxed{
v_2(\mathscr H_{\omega H}^{\rm pref})=2M+2.}
\tag{5.1}
\]

除去该 primitive `2`-scale 后，第一项至少仍含 `2^{2m+2}`，第二项为 `Q_0^2N_0`。所以

\[
\boxed{
\frac{\mathscr H_{\omega H}^{\rm pref}}{2^{2M+2}}
\equiv1\pmod8.}
\tag{5.2}
\]

于是 `J_H/H_pref` 在 primitive orientation 上形成

\[
\boxed{7\pmod8\quad/\quad1\pmod8}
\tag{5.3}
\]
的 pure-prefix pair。

这并没有自动产生矛盾，因为它们可以共享指定的 inert prime后再由其它素数补偿 orientation；真正可用的是下面的 **exact residual-depth law**。

---

## 6. shallow content 中 `H_pref` 精确读取全部 `omega` depth

parent 文件的 exact decomposition 为

\[
\boxed{
\mathscr B_W
=c_u^2\mathcal P_{\omega H}(K)
+g\omega(g\omega-2c_u)K^2.}
\tag{6.1}
\]

第二项在当前 prime 上的赋值恰为 `e`。

若

\[
e\le h,
\]
则 `V>=h+1>e`。为了使 (6.1) 的和达到 `V`，必有

\[
\boxed{v_p(\mathcal P_{\omega H}(K))=e.}
\tag{6.2}
\]

另一方面 `j>=h+1>e`。由 (4.2) 且 `p\nmid B`：

\[
\boxed{
v_p(\mathscr H_{\omega H}^{\rm pref})=e
\qquad(e\le h).}
\tag{6.3}
\]

所以 shallow-content 分支中，`omega` 的**完整** p-adic depth 已经由一个恰有 `4M+1` 位、primitive `1 mod 8` 的 pure-prefix integer 精确读取。

---

## 7. exact `J_H/B_W` difference 把 oversaturation residual depth 封顶

`spontaneous-height-resultant-parity.md` 给

\[
5^{2d}\widehat{\mathcal J}_H
-2^{2m}5^{2d}g^2\mathscr B_W
=q^2W_q\,\mathscr C_{JB},
\tag{7.1}
\]
其中

\[
\mathscr C_{JB}
=(g^2\omega^2-c_u^2)W_q
-2g^2\omega TK.
\]

`spontaneous-height-companion-cross.md` 又有

\[
\boxed{
q\mathscr C_{JB}
=-zL_{JB},
}
\tag{7.2}
\]
其中

\[
L_{JB}=DzK+fN
=2Dg\omega K-fqW_q.
\tag{7.3}
\]

把 (7.2) 代入 (7.1)：

\[
\boxed{
5^{2d}
\left(
\widehat{\mathcal J}_H-(2^mg)^2\mathscr B_W
\right)
=-qzW_qL_{JB}.}
\tag{7.4}
\]

当前 prime 满足

\[
p\nmid5qz(2^mg),
\]
所以

\[
\boxed{
v_p\!\left(
\widehat{\mathcal J}_H-(2^mg)^2\mathscr B_W
\right)
=h+v_p(L_{JB}).}
\tag{7.5}
\]

而 (7.3) 的两个 coefficient

\[
2DgK,
\qquad fq
\]
都是 p-adic units。因此如果

\[
e\ne h,
\]
两项赋值不同，不可能首层抵消，于是

\[
\boxed{v_p(L_{JB})=\min(e,h).}
\tag{7.6}
\]

合并：

\[
\boxed{
v_p\!\left(
\widehat{\mathcal J}_H-(2^mg)^2\mathscr B_W
\right)
=h+\min(e,h)
\qquad(e\ne h).}
\tag{7.7}
\]

---

## 8. unequal content/height depth 时，较浅 residual 被 `min(e,h)` 精确控制

回忆

\[
j=v_p(\widehat{\mathcal J}_H),
\qquad
V=v_p(\mathscr B_W),
\]
且 `(2^mg)^2` 为 unit。

若

\[
j\ne V,
\]
则两个 summand 赋值不同，因此

\[
v_p\!\left(
\widehat{\mathcal J}_H-(2^mg)^2\mathscr B_W
\right)
=\min(j,V).
\]
与 (7.7) 比较：

\[
\boxed{
\min(j,V)=h+\min(e,h)
\qquad(e\ne h,\ j\ne V).}
\tag{8.1}
\]

也就是 residual depths 满足

\[
\boxed{
\min(r_J,r_B)=\min(e,h)
\qquad(e\ne h,\ r_J\ne r_B).}
\tag{8.2}
\]

若 `j=V`，左边 difference 的赋值至少为 `j`。结合 (7.7) 立刻得到

\[
\boxed{j=V\le h+\min(e,h).}
\tag{8.3}
\]

所以无论两边是否等深，都有统一 cap：

\[
\boxed{
1\le\min(r_J,r_B)\le\min(e,h)
\qquad(e\ne h).}
\tag{8.4}
\]

因此在 unequal content/height depth 上，companion oversaturation 的较浅额外深度永远不能超过 `min(e,h)`；若两 companion 深度本身不同，这个 cap 还是精确等号。

---

## 9. 唯一未被该 cap 控制的机制是 `e=h` equal-depth resonance

现在令

\[
e=h.
\]
写

\[
\omega=p^h\omega_0,
\qquad
W_q=p^hW_0,
\qquad
p\nmid\omega_0W_0.
\]

由 (7.3)：

\[
L_{JB}
=p^h
\left(
2DgK\omega_0-fqW_0
\right).
\tag{9.1}
\]

定义唯一的 resonance depth

\[
\boxed{
\rho_p
:=v_p\!\left(
2DgK\omega_0-fqW_0
\right)\ge0.}
\tag{9.2}
\]

于是

\[
\boxed{v_p(L_{JB})=h+\rho_p,}
\tag{9.3}
\]

并由 (7.5)：

\[
\boxed{
v_p\!\left(
\widehat{\mathcal J}_H-(2^mg)^2\mathscr B_W
\right)
=2h+\rho_p.}
\tag{9.4}
\]

所以所有可能突破 §8 cap 的行为都已经严格集中到一个 unit synchronization：

\[
\boxed{
2DgK\omega_0
\equiv fqW_0
\pmod{p^r}.}
\tag{9.5}
\]

换言之，height-supported omega oversaturation 现在分成：

\[
\boxed{
\begin{array}{ll}
e\ne h:&
\min(r_J,r_B)\le\min(e,h),\\[1mm]
e=h:&
\text{只剩单一 equal-depth unit resonance }\rho_p.
\end{array}}
\tag{9.6}
\]

这比“simple moving root”更窄：真正无界的 deep synchronization 已经只剩 codimension-one 的 equal-depth resonance。

---

## 10. 当前统一 depth/height ledger

综合 parent 文件和本文：

\[
\boxed{
\begin{gathered}
p\equiv7,11\pmod{24},\\
e=v_p(\omega)\ge1,
\qquad
h=v_p(W_q)\ge1,\\
p^{h+1}\mid\mathcal J_H,
\qquad
\frac{79}{20}10^{4M}<\mathcal J_H<\frac{111}{20}10^{4M},\\
p^{\min(e,h+1)}\mid\mathscr H_{\omega H}^{\rm pref},
\qquad
\frac{193}{100}10^{4M}
<\mathscr H_{\omega H}^{\rm pref}
<\frac{43}{20}10^{4M},\\
\frac{\mathcal J_H}{2^{2M+2}}\equiv7\pmod8,
\qquad
\frac{\mathscr H_{\omega H}^{\rm pref}}{2^{2M+2}}\equiv1\pmod8,\\
e\le h
\Longrightarrow
v_p(\mathscr H_{\omega H}^{\rm pref})=e,\\
e\ne h
\Longrightarrow
1\le\min(r_J,r_B)\le\min(e,h).
\end{gathered}}
\tag{10.1}
\]

其中若 `e!=h` 且 `r_J!=r_B`，最后一个不等式强化为等式。

所以后续再推进时不应继续研究 generic `e!=h` 的无界 oversaturation tree；它已经有显式 residual cap。真正剩余的目标是：

\[
\boxed{
 e=h,
 \qquad
 2DgK\omega_0-fqW_0
 \text{ 的 unit resonance}.}
\tag{10.2}
\]

需要把该 unit congruence再投影到 decimal determinant、`H_pref/J_H` natural representatives 或现有 source slot 上，才能继续逼近 closure。

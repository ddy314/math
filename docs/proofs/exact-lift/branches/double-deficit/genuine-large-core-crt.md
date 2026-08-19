# DD genuine-large core 的 fixed `q_c^2 × C_G` prefix CRT

> **依赖：** [`genuine-a12-fixed-crt.md`](genuine-a12-fixed-crt.md)、[`good-prefix-crt-location-audit.md`](good-prefix-crt-location-audit.md) 的 Q-side exact parent、frontier constants。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文把两个 coefficients 不含 `A_12,a_3,W` 的 fixed decimal periods联立：
>
> 1. clean-source Q-side period `q_c^2`；
> 2. orientation-locked genuine period `C_G`。
>
> 因 `q_c` 与 pair-max core渐近互素，联合 period 高度为
> \[
> (2z_*+c)S+o(S),
> \qquad c:=\frac{\log C_G}{S}.
> \]
> 当
> \[
> c>1-2z_*=0.382232844764\ldots
> \]
> 时，它严格超过 `A_12` 的 `S+o(S)` digit window，因此在固定 denominator/source/small-prefix fiber中 `A_12` 至多一个。
>
> 本文是 counting/uniqueness 结果，不证明该唯一 candidate不存在。

---

## 1. fixed Q-side `A_12` congruence

记

\[
D:=10^d,
\qquad
F:=5^T,
\]

\[
X=2^HZ,
\qquad
\Sigma=X+FU,
\qquad
V=X-FU.
\]

已有 exact identities

\[
\Sigma R_0
=g_0(BDVA_{12}-Ua_3),
\tag{1.1}
\]

以及

\[
q_c^2L_{\rm clean}
=g_0a_3+FR_0.
\tag{1.2}
\]

由 `(1.1)`：

\[
g_0BDVA_{12}
=\Sigma R_0+g_0Ua_3.
\]

用 `(1.2)` 消去 `g_0a_3`：

\[
\begin{aligned}
g_0BDVA_{12}
&=\Sigma R_0+U(q_c^2L_{\rm clean}-FR_0)\\
&=(\Sigma-UF)R_0+Uq_c^2L_{\rm clean}\\
&=XR_0+Uq_c^2L_{\rm clean}.
\end{aligned}
\]

因此得到 exact parent

\[
\boxed{
g_0BDVA_{12}-XR_0
=Uq_c^2L_{\rm clean}.}
\tag{Q-fixed-exact}

模 `q_c^2`：

\[
\boxed{
g_0BDV A_{12}
\equiv XR_0
\pmod{q_c^2}.}
\tag{Q-fixed}

删去 coefficient exceptional core后，`A_12` coefficient与 `q_c` 互素，所以 effective period为

\[
\boxed{q_c^2/10^{o(S)}.}
\tag{1.3}

frontier 给

\[
\log q_c
=z_*S+o(S),
\qquad
z_*=0.308883577618\ldots,
\]

故

\[
\boxed{
\log(q_c^2)
=0.617767155236\ldots S+o(S).
}
\tag{1.4}

---

## 2. fixed genuine `A_12` congruence

`genuine-a12-fixed-crt.md` 已证明

\[
\boxed{
2\mathscr T g_0BD e_G\Sigma R_0 A_{12}
\equiv M_{G,0}
\pmod{C_G},
}
\tag{G-fixed}

其中

\[
e_G=V/C_G
\]

且 coefficient在 genuine main support上为 unit。因此 effective period为

\[
\boxed{C_G/10^{o(S)}.}
\tag{2.1}

重要的是 `(G-fixed)` 的 coefficient与 `M_{G,0}` 都不含

\[
A_{12},\quad a_3,\quad W.
\]

所以 `(Q-fixed)` 与 `(G-fixed)` 可以在同一个 fixed denominator/source/small-prefix fiber中真正作为两个固定 residue classes联立，而不是 moving-root congruences。

---

## 3. 两个 periods 渐近互素

terminal source separation给

\[
\boxed{(q_c,C_L)=10^{o(S)}}
\]

按 gcd height理解。

又

\[
C_G\mid C_L.
\]

所以

\[
\boxed{(q_c^2,C_G)=10^{o(S)}.}
\tag{3.1}

因此两个 fixed congruences的联合 effective period为

\[
\boxed{
M_G^{\rm CRT}
=\frac{q_c^2C_G}{10^{o(S)}}.
}
\tag{3.2}

---

## 4. genuine mass parameter 与 threshold

定义 genuine main-height ratio

\[
\boxed{
c:=\frac{\log C_G}{S}.}
\tag{4.1}

则

\[
\log M_G^{\rm CRT}
=(2z_*+c)S+o(S).
\tag{4.2}

prefix polarization 已证明

\[
\boxed{\log A_{12}=S+o(S).}
\tag{4.3}

因此若

\[
2z_*+c>1,
\]

联合 period严格大于合法 `A_12` 窗口。

阈值为

\[
\boxed{
c>1-2z_*}
\tag{4.4}

即

\[
\boxed{
c>0.382232844764\ldots.}
\tag{Genuine-CRT-threshold}

---

## 5. uniqueness lemma

固定一个 terminal denominator/source/small-prefix fiber，使 `(Q-fixed)` 与 `(G-fixed)` 的所有 coefficients、right-hand residues、`q_c,C_G` 固定。

若存在两个不同合法 prefixes

\[
A_{12}^{(1)}\ne A_{12}^{(2)}
\]

同时满足两个 congruences，则其差被联合 period整除：

\[
M_G^{\rm CRT}
\mid
A_{12}^{(1)}-A_{12}^{(2)}.
\]

另一方面 digit window给

\[
|A_{12}^{(1)}-A_{12}^{(2)}|
<10^{S+o(S)}.
\]

当 `(Genuine-CRT-threshold)` 成立时：

\[
M_G^{\rm CRT}
=10^{(2z_*+c)S+o(S)}
>10^{S+o(S)}
\]

for sufficiently large `S`，矛盾。

所以：

\[
\boxed{
 c>0.382232844764\ldots
 \Longrightarrow
 \#\{A_{12}\text{ in a fixed genuine fiber}\}\le1.
}
\tag{Large-genuine-uniqueness}

---

## 6. leading-block version

prefix polarization还有

\[
A_{12}=10^{n_2}a_1+a_2,
\qquad
n_2=o(S),
\qquad
\log a_2=o(S).
\]

固定 small suffix data `(n_2,a_2)` 后，`A_12` 与 `a_1` 是 injective affine correspondence。因此同样有

\[
\boxed{
 c>0.382232844764\ldots
 \Longrightarrow
 \#\{a_1\text{ in the fixed fiber}\}\le1.
}
\tag{Large-genuine-a1}

这把此前只在 full-rational Q/G CRT 中得到的 prefix uniqueness扩展到 genuine core足够大的 sector。

---

## 7. threshold 以下意味着 rational-contact mass 至少 `2z_*`

rational/genuine main split满足

\[
\log(D_+D_-)+\log C_G
=S+o(S).
\]

若 genuine sector未达到 `(Genuine-CRT-threshold)`，即

\[
c\le1-2z_*+o(1),
\]

则 rational-contact mass至少为

\[
\boxed{
\frac{\log(D_+D_-)}S
\ge2z_*+o(1)
=0.617767155236\ldots+o(1).
}
\tag{Rational-mass-floor}

所以 terminal frontier被进一步切成：

1. **large-genuine sector**
   \[
   c>0.382232844764\ldots,
   \]
   fixed fiber中 `A_12/a_1` 至多一个；
2. **rational-heavy sector**
   \[
   \log(D_+D_-)
   \ge0.617767155236\ldots S+o(S).
   \]

第二支仍待把 partial rational-contact mass与已有 Good/Bad/cofactor machinery重新做容量账本。

---

## 8. no-double-count 边界

联合 period大于 digit window只给

\[
\#\{A_{12}\}\le1,
\]

不自动给

\[
\#\{A_{12}\}=0.
\]

而 genuine period `C_G` 的 p-adic depth已知由 sphere carrier支付；本文只把它用作 CRT period，不增加 local height surplus。

下一步有两个互补方向：

- 对 large-genuine sector研究唯一 CRT lift 的 Archimedean location；
- 对 rational-heavy sector把 `0.617767...S` 的 contact mass重新代入 partial Good/Bad capacity ledger，争取得到严格 mass inequality。

---

## 9. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：fixed Q-side `A_12` congruence、fixed genuine `A_12` congruence、联合 period、threshold `c>0.382232844764...`、large-genuine fixed-fiber uniqueness、complementary rational mass floor。
- **`有限/计数结论`**：上述 uniqueness 只在 fixed terminal fiber中使用，不是 eventual emptiness。
- **`待证`**：large-genuine unique-lift location；rational-heavy partial-contact capacity；genuine / DD frontier emptiness。

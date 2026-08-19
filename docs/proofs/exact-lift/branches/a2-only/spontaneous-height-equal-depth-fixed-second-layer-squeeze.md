# A2 fixed `7/2671` exceptional directions 的统一 second-layer squeeze

> **依赖：** `spontaneous-height-equal-depth-orthogonal-decimal-norm.md`、`spontaneous-height-equal-depth-fixed-exception-transversality.md`、`spontaneous-height-equal-depth-decimal-pair.md`。
>
> **严格状态：**本文处理 fixed exceptions 真正剩余的 normalized cancellation。对 baseline depth `h>=2`，fixed `7` 的两张 roots与 fixed `2671` orientation root都具有同一结构：exceptional linear coefficient在 target quadratic Hensel branch上精确只有一层 `p`。因此若相应 exceptional natural direction不只多一层、而是 excess `sigma>=2`，则 decimal companion `E_+` 必须恰好具有最小 deep depth `2h+1`。结合已有 `v_p(E_+)>=2h+min(r_B,h,rho_p)`，进一步强迫 `min(r_B,rho_p)=1`。所以 `h>=2,r_B>=2,rho_p>=2` 时所有 fixed exceptional directions都至多只有一个 extra digit。本文不处理 `h=1` 的三项同深 cancellation，因此不关闭 A2。

---

## 1. common notation

固定 genuine deep equal-depth target：

\[
v_p(\omega)=v_p(W_q)=h\ge1,
\qquad
\rho_p\ge1.
\]

沿用

\[
U=DK-N,
\qquad
P=6K^2-36K+55,
\]

\[
R_+=DP-KU,
\]

以及 decimal pair

\[
E_+=E_M\omega R_+.
\]

因为

\[
v_p(E_M\omega)=h,
\]
定义

\[
\boxed{
r_+:=v_p(R_+)-h=v_p(E_+)-2h.}
\tag{1.1}
\]

已有 deep resonance transfer

\[
\boxed{r_+\ge1}
\tag{1.2}
\]

以及更强下界

\[
\boxed{
r_+\ge\min\{r_B,h,\rho_p\},}
\tag{1.3}
\]
其中

\[
v_p(B_W)=h+r_B,
\qquad r_B\ge1.
\]

---

## 2. fixed `7`, root `K=2`: `R_PD` direction

在 fixed-7 extra-resultant root

\[
K\equiv2\pmod7
\]
上，已有 exact identity

\[
\boxed{
R_{PD}
=DR_+ +(36D-11N)U-5U^2.}
\tag{2.1}
\]

记

\[
F_7:=36D-11N.
\]

若现在

\[
\boxed{h\ge2,}
\tag{2.2}
\]
则 `R_PD` 本身至少被 `7^h` 整除。fixed-exception transversality 的 Bezout

\[
1296R_{PD}-(1980D-691N)F_7=175N^2
\]
右端只有一层 `7`，所以在该 root 上

\[
\boxed{v_7(F_7)=1.}
\tag{2.3}
\]

三项赋值为

\[
v_7(DR_+)=h+r_+,
\]

\[
v_7(F_7U)=h+1,
\]

\[
v_7(5U^2)=2h\ge h+2.
\tag{2.4}
\]

定义 extra-resultant depth

\[
\boxed{
\sigma_{7,-}:=v_7(R_{PD})-h\ge1.}
\tag{2.5}
\]

若

\[
r_+\ge2,
\]
则 (2.4) 中 `F_7U` 是唯一最浅项，故

\[
\boxed{\sigma_{7,-}=1.}
\tag{2.6}
\]

逆否命题即

\[
\boxed{
\sigma_{7,-}\ge2
\Longrightarrow
r_+=1.}
\tag{2.7}
\]

用 orthogonal-decimal 文件的

\[
\Xi_{PD}=c^2R_{PD},\qquad v_7(c)=h,
\]
也可完全 decimal 地写成

\[
\boxed{
v_7(\Xi_{PD})\ge3h+2
\Longrightarrow
v_7(E_+)=2h+1.}
\tag{2.8}
\]

---

## 3. fixed `7`, root `K=4`: orthogonal direction

另一张 fixed-7 root为

\[
K\equiv4\pmod7.
\]

orthogonal file证明

\[
\boxed{
L_\perp
=(55D-18N)\alpha
+3TR_+
+T(53-15K)U.}
\tag{3.1}
\]

记

\[
F_\perp:=53-15K.
\]

`P` 与该 linear factor有

\[
75P+(74-30K)(15K-53)=203=7\cdot29.
\tag{3.2}
\]

在 `K=4 mod7` 时 `74-30K` 为 `7`-进单位；又 `h>=2` 意味着 `v_7(P)>=2`。因此 (3.2) 强迫

\[
\boxed{v_7(F_\perp)=1.}
\tag{3.3}
\]

三项赋值为

\[
v_7((55D-18N)\alpha)=2h,
\]

\[
v_7(3TR_+)=h+r_+,
\]

\[
v_7(TF_\perp U)=h+1.
\tag{3.4}
\]

其中 `2h>=h+2`。定义

\[
\boxed{
\sigma_{7,+}:=v_7(L_\perp)-h\ge1.}
\tag{3.5}
\]

若 `r_+>=2`，第三项唯一最浅，因此

\[
\sigma_{7,+}=1.
\]
于是

\[
\boxed{
\sigma_{7,+}\ge2
\Longrightarrow
r_+=1.}
\tag{3.6}
\]

利用

\[
\Xi_\perp=cL_\perp,
\]
等价的 pure-decimal form为

\[
\boxed{
v_7(\Xi_\perp)\ge2h+2
\Longrightarrow
v_7(E_+)=2h+1.}
\tag{3.7}
\]

---

## 4. fixed `2671`: parallel orientation direction

令

\[
p_*=2671,
\qquad
F_*:=5K-36.
\]

parallel carrier identity为

\[
\boxed{
L_{D3}
=TR_+-TF_*U-6N\alpha.}
\tag{4.1}
\]

在 fixed root

\[
K\equiv2144\pmod{2671}
\]
上，transversality 已证明：若

\[
h=v_{p_*}(P)\ge2,
\]
则

\[
\boxed{v_{p_*}(F_*)=1.}
\tag{4.2}
\]

所以三项赋值为

\[
h+r_+,
\qquad
h+1,
\qquad
2h\ge h+2.
\tag{4.3}
\]

定义

\[
\boxed{
\sigma_{2671}:=v_{2671}(L_{D3})-h\ge1.}
\tag{4.4}
\]

若 `r_+>=2`，中间项 `-TF_*U` 唯一最浅，因此

\[
\sigma_{2671}=1.
\]
故

\[
\boxed{
\sigma_{2671}\ge2
\Longrightarrow
r_+=1.}
\tag{4.5}
\]

又

\[
\Xi_{\parallel}=cL_{D3},
\]
所以 decimal form为

\[
\boxed{
v_{2671}(\Xi_{\parallel})\ge2h+2
\Longrightarrow
v_{2671}(E_+)=2h+1.}
\tag{4.6}
\]

---

## 5. unified second-layer squeeze

综合 §§2--4。对三种 exceptional direction中的任意一个，若

\[
\boxed{h\ge2}
\]
且它的 extra depth 不止一层：

\[
\boxed{\sigma\ge2,}
\]
则统一有

\[
\boxed{r_+=1,}
\tag{5.1}
\]
即

\[
\boxed{v_p(R_+)=h+1,}
\tag{5.2}
\]

以及完全 decimal 的

\[
\boxed{v_p(E_+)=2h+1.}
\tag{5.3}
\]

因此 fixed exception越想继续加深，`E_+` 反而越被锁到最浅的 deep level；不存在 `exceptional direction` 与 `E_+` 同时继续无界加深的 branch。

---

## 6. full tail / B_W residual 必有一个只有一层

由 (1.3)、(5.1)：

\[
1=r_+\ge\min\{r_B,h,\rho_p\}.
\]

当前

\[
h\ge2,
\qquad r_B\ge1,
\qquad\rho_p\ge1.
\]

所以严格得到

\[
\boxed{
\min\{r_B,\rho_p\}=1.}
\tag{6.1}
\]

而 full tail reader 已证明

\[
\rho_p=v_p(\Lambda_{\rm tail}).
\]

所以也可写成

\[
\boxed{
\min\{r_B,v_p(\Lambda_{\rm tail})\}=1.}
\tag{6.2}
\]

特别地：

\[
\boxed{
h\ge2,\quad r_B\ge2,\quad\rho_p\ge2
\Longrightarrow
\sigma=1}
\tag{6.3}

对三种 fixed exceptional directions全部成立。

这删除了最危险的三重深同步：

\[
\boxed{
\text{fixed exceptional depth}\ge2,
\quad B_W\text{ residual depth}\ge2,
\quad resonance tail depth\ge2
}
\]
不能同时发生。

---

## 7. normalized first-digit consequences

当 `sigma>=2` 时，除了 `r_+=1`，还得到一个显式 first normalized cancellation。

写

\[
R_+=p^{h+1}R_1,
\qquad
U=p^hU_0,
\qquad
p\nmid R_1U_0.
\]

### `7`, root `K=2`

由 quadratic root提升 `K=23 mod49` 与 `U=0 mod49` 得

\[
D/N\equiv32\pmod{49},
\qquad
\frac{36D-11N}{7N}\equiv2\pmod7.
\]

(2.1) 除以 `7^(h+1)` 后得到

\[
\boxed{2R_1+U_0\equiv0\pmod7.}
\tag{7.1}
\]

### `7`, root `K=4`

`P=0` 的 `mod49` lift为

\[
K\equiv32\pmod{49},
\]
并且

\[
\frac{53-15K}{7}\equiv2\pmod7.
\]

由 (3.1)：

\[
\boxed{3R_1+2U_0\equiv0\pmod7.}
\tag{7.2}
\]

### `2671`

fixed-exception transversality 已给 quadratic branch上

\[
\frac{5K-36}{2671}\equiv2618\equiv-53\pmod{2671}.
\]

由 (4.1)：

\[
\boxed{R_1+53U_0\equiv0\pmod{2671}.}
\tag{7.3}
\]

所以第二层 cancellation并非自由参数：三条 exceptional branches各自只允许一个 fixed normalized ratio `R_1/U_0`。

---

## 8. remaining frontier

fixed exceptions现在被压成：

1. excess `sigma=1`：只多一个 digit，已无需继续 Hensel root分类；
2. excess `sigma>=2` 且 `h>=2`：强迫
   \[
   v_p(E_+)=2h+1,
   \qquad
   \min(r_B,\rho_p)=1,
   \]
   并满足 §§7 的 fixed normalized ratio；
3. 唯一未被本文覆盖的低 baseline 是
   \[
   h=1,
   \]
   因为此时 `alpha`/`U^2` 也正好落在 `h+1=2` 层，三项可能共同 cancellation。

因此 fixed-prime frontier已经从“任意深 Hensel exception”缩成了：

\[
\boxed{
h=1\text{ low-baseline residue problem}
\quad\text{或}\quad
h\ge2\text{ 的单层 }E_+\text{ / tail gate}.}
\]

A2 仍为 `待证`。

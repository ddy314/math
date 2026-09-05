# DD frontier: terminal `q-Z` overlap 的 complementary collapse 与 deep-source square amplification

> 日期：2026-08-22
>
> 作用域：假想 corrected
> \[
> n/S\to6.308883577618\ldots
> \]
> 的 terminal one-channel frontier。
>
> **状态：已严格完成（frontier 条件蕴含；非 closure）。**
>
> 本文把三个此前独立建立的结构联立：
>
> 1. source core `q_c` 强制进入 projective denominator `Z_0`；
> 2. canonical `q-Z` excess 的 gap/complementary two-sheet theorem；
> 3. phase-normalized secondary rational reader `K_UZ`。
>
> 结论是：删去总高度 `o(S)` 的 slow / overlap core 后，terminal source 与 `Z` 的公共 prime-power **只能处于 complementary sheet**。此外，当 `Z` 的 depth 至少为 source depth 的两倍时，source square同时进入 `A_12` 与 `K_UZ`。

## 1. main source overlap

terminal normalization有

\[
Q=Uq,
\qquad
q=J\theta q_c,
\tag{1.1}
\]

其中 `J theta` 只贡献 `10^{o(S)}` 的 terminal slow height；同时

\[
\log\gamma=o(S),
\qquad
\log\rho_0=o(S).
\]

本文把所有进入

\[
10\gamma\rho_0J\theta
\]

以及既有 coefficient exceptional core 的 prime-power统称为 `exceptional`。

固定一个非 exceptional odd prime `p`，写

\[
r:=v_p(q_c)=v_p(q)=v_p(Q)>0,
\qquad
z:=v_p(Z)>0.
\tag{1.2}
\]

因为 `p\nmid gamma`，旧 `q-Z` excess theorem 中的 denominator baseline为

\[
M=0.
\]

因此这个 prime-power全部属于真正的 `D_ex` support。

## 2. gap sheet 在 terminal main source 上不可能

[`dd-frontier-source-core-projective-denominator-2026-08-22.md`](dd-frontier-source-core-projective-denominator-2026-08-22.md) 已证明：若 `p\nmid rho_0`，则

\[
\boxed{v_p(Z_0)\ge r>0.}
\tag{2.1}
\]

另一方面 canonical `q-Z` two-sheet theorem 的 gap sheet满足

\[
v_p(H_{\rm sph}+y_3)=0.
\]

由于

\[
Z_0=\frac{H_{\rm sph}+y_3}
{((y_1,y_2),H_{\rm sph}+y_3)},
\]

gap sheet必有

\[
\boxed{v_p(Z_0)=0.}
\tag{2.2}
\]

`(2.1)` 与 `(2.2)` 矛盾。因此：

\[
\boxed{
\text{每个 terminal main }p\mid(q_c,Z)
\text{ 都处于 complementary sheet。}
}
\tag{Complementary-only}

所以旧 `D_gap` 在 terminal equality ray 上只可能留在 exceptional `10^{o(S)}` core 中。

## 3. main `q_c-Z` overlap 同时进入 `A_12,Theta_12,Z_0`

旧 complementary theorem 在 baseline `M=0` 时给

\[
e=\min(r,z).
\]

并有

\[
\boxed{p^e\mid A_{12},}
\tag{3.1}
\]

\[
\boxed{p^e\mid\Theta_{12},}
\tag{3.2}
\]

\[
\boxed{p^e\mid Z_0.}
\tag{3.3}
\]

又因

\[
p^r\mid Q,
\qquad e\le r,
\]

所以

\[
\boxed{p^e\mid C_{12}:=(A_{12},Q).}
\tag{3.4}

全局定义删去 exceptional core后的 source overlap

\[
D_{q_cZ}^{\rm main}
:=\prod_p p^{\min(v_p(q_c),v_p(Z))}.
\tag{3.5}

逐素数相乘得到

\[
\boxed{
D_{q_cZ}^{\rm main}
\mid C_{12},\quad
D_{q_cZ}^{\rm main}
\mid\Theta_{12},\quad
D_{q_cZ}^{\rm main}
\mid Z_0.
}
\tag{Main-qZ-triple-reader}

所以在 terminal equality ray 上，`q-Z` overlap不再只有 projective reader；它同时是 prefix bottom gcd reader。

## 4. deep-`Z` source prime把 `A_12` depth翻倍

现在仍固定 main source prime `p^r||q_c`，进一步假设

\[
\boxed{z=v_p(Z)\ge2r.}
\tag{4.1}

使用三个 exact terminal identities：

\[
UA_0+R_0=g_0B10^dA_{12},
\tag{4.2}
\]

\[
q_c^2L_{\rm clean}=VA_0-5^TR_0,
\tag{4.3}
\]

\[
V=2^HZ-5^TU.
\tag{4.4}
\]

将 `(4.4)` 代入 `(4.3)`：

\[
\boxed{
q_c^2L_{\rm clean}
=2^HZA_0-5^T(UA_0+R_0).
}
\tag{4.5}

左边被 `p^{2r}` 整除；由 `(4.1)`，第一项 `2^HZA_0` 也被 `p^{2r}` 整除。因为 `p\ne5`，所以

\[
\boxed{p^{2r}\mid UA_0+R_0.}
\tag{4.6}

在 main support 上 `p\nmid g_0B10`，由 `(4.2)`：

\[
\boxed{p^{2r}\mid A_{12}.}
\tag{Deep-A12-square}

注意这比 ordinary complementary selector `(3.1)` 的 `p^r|A_12` 强一整份 source depth。

## 5. 同一 source square进入 `K_UZ`

[`dd-frontier-phase-normalized-secondary-norm-2026-08-22.md`](dd-frontier-phase-normalized-secondary-norm-2026-08-22.md) 定义

\[
C_LK_{UZ}=c_Uq_c^2U+c_ZZ,
\tag{5.1}
\]

其中

\[
\log c_U+\log c_Z=o(S),
\]

且在 main support上

\[
p\nmid C_Lc_Uc_ZU.
\]

由 `p^{2r}|q_c^2` 与 `(4.1)`：

\[
p^{2r}\mid c_Uq_c^2U,
\qquad
p^{2r}\mid c_ZZ.
\]

故

\[
\boxed{p^{2r}\mid K_{UZ}.}
\tag{Deep-K-square}

因此 deep source core同时被两个 rational coordinates读取。

定义

\[
\boxed{
D_{\rm deep}
:=\prod_{\substack{p\ {m main}\\
v_p(Z)\ge2v_p(q_c)}}
p^{v_p(q_c)}.
}
\tag{5.2}

则

\[
\boxed{
D_{\rm deep}^{\,2}\mid A_{12},
\qquad
D_{\rm deep}^{\,2}\mid K_{UZ},
}
\tag{Deep-double-reader}

即

\[
\boxed{
D_{\rm deep}^{\,2}\mid(A_{12},K_{UZ}).
}
\tag{Deep-gcd}

## 6. immediate capacity bound

terminal 已证明

\[
\log K_{UZ}=z_*S+o(S),
\qquad
z_*=0.308883577618\ldots.
\]

由 `(Deep-K-square)`：

\[
2\log D_{\rm deep}
\le z_*S+o(S).
\]

所以

\[
\boxed{
\log D_{\rm deep}
\le
\frac{z_*}{2}S+o(S)
=0.154441788809\ldots S+o(S).
}
\tag{Deep-capacity}

这是一个真实 source-overlap capacity bound：任何 `Z` 至少比 source平方还深的 prime mass，最多只能承载半份 `q_c/Z/K_UZ` terminal height。

## 7. equal-depth `z=2r` 的剩余 extra cancellation

若

\[
z=2r,
\]

写

\[
q_c=p^rq_0,
\qquad
Z=p^{2r}Z_0^{(p)},
\]

其中两个 quotient都是 `p`-units。由 `(5.1)`：

\[
\frac{C_LK_{UZ}}{p^{2r}}
=c_Uq_0^2U+c_ZZ_0^{(p)}.
\tag{7.1}

因此 `v_p(K_UZ)>2r` 当且仅当

\[
\boxed{
c_Uq_0^2U+c_ZZ_0^{(p)}\equiv0\pmod p.}
\tag{K-extra-local}

这确实是一条新的 unit-unit relation，但本文**不**宣称它与 `(Deep-A12-square)` 联立后自动继续提升 `A_12` 到 `p^{2r+1}`。直接代入 clean-source equations 后，`K-extra-local` 保留一个真实 Hensel-quotient relation；目前没有得到这种 extra lift。

所以本文严格关闭的是：

- terminal q-Z 的 gap sheet；
- deep-source baseline的 square amplification与容量。

`z=2r` 后的额外 `K_UZ` cancellation仍是开放的局部子问题，但它不是当前 strict-gap 的唯一可能来源，因为 equality frontier并不要求 `(q_c,Z)` 具有正线性 overlap。

## 8. 证明策略更新

本文说明 terminal source/projective overlap比旧 two-sheet picture更刚性：

\[
\boxed{
q_c\cap Z
\Longrightarrow
\text{complementary only}
\Longrightarrow
C_{12}\cap\Theta_{12}\cap Z_0.
}
\]

若再有 `Z` depth `>=2*source depth`，则 source square同时进入

\[
A_{12}\cap K_{UZ}.
\]

但这仍不足以排除 equality frontier：`q_c` 与 `Z` 可以在 leading order上几乎互素。因此后续主攻目标仍应回到不可消失的

\[
C_L=10^{S+o(S)}
\]

moving split-prime orientation，而不是把全部精力继续投入 `q_c-Z` overlap。

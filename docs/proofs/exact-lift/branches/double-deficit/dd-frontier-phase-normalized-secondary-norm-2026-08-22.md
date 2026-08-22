# DD frontier: phase-normalized secondary norm 与 `q_c-Z` rational reader

> 日期：2026-08-22
>
> 作用域：假想 corrected
> \[
> n/S\to6.308883577618\ldots
> \]
> 的 terminal one-channel frontier。
>
> **状态：已严格完成（frontier 条件蕴含 / 新 canonical reader；非 closure）。**
>
> 本文只使用 corrected terminal 上仍可靠的两条 parent identities：secondary Gaussian norm 与 S-unit phase。它不使用已经撤销的 unified-discriminant valuation mismatch。

## 1. 输入

secondary Gaussian numerator写成

\[
\boxed{
\mathcal G_1
=A_*2^{m-2}q_c-iB_*5^{2T-m}
=\Pi\Delta_1,
}
\tag{1.1}
\]

其中

\[
A_*=g_0a_2\theta s,
\qquad
B_*=\widetilde rR_0,
\qquad
N(\Pi)=C_L.
\]

取 norm：

\[
\boxed{
C_LN(\Delta_1)
=A_*^22^{2m-4}q_c^2
+B_*^25^{4T-2m}.
}
\tag{Secondary-norm}
\]

S-unit phase与 one-channel moving core给

\[
\boxed{
2^HZ-5^TU=V=C_Lv_0,
}
\tag{Phase}
\]

并且 terminal normalization 有

\[
(C_L,10)=1,
\qquad
(C_L,q_c)=1,
\qquad
(C_L,Z)=1,
\qquad
(U,Z)=1.
\tag{1.2}
\]

最后两个 coprimality 中，`(C_L,Z)=1` 直接来自 `C_L|V` 与 `(V,Z)=1`。

## 2. 两个 smooth resonance defect

定义整数

\[
\boxed{
d_2:=H-(2m-4),
\qquad
d_5:=(4T-2m)-T=3T-2m.
}
\tag{2.1}
\]

并记

\[
d^+:=\max(d,0),
\qquad
d^-:=\max(-d,0).
\]

在 canonical `t_2=1` 2-resonance 中，若

\[
\mathfrak q=v_2(Q),
\quad
\mathfrak g=v_2(G),
\quad
\mathfrak n=v_2(\mathcal N_{12}),
\]

则已有 exact

\[
\mathfrak f
=2m+2\mathfrak q+\mathfrak n-\mathfrak g-3,
\]

而

\[
\mathfrak f=\mathfrak g+H+1.
\]

故

\[
\boxed{
d_2=2\mathfrak q+\mathfrak n-2\mathfrak g.}
\tag{2.2}
\]

五进 corrected resonance给

\[
T=\frac{2m+2q_5-2g_5+n_5}{3},
\]

所以

\[
\boxed{
d_5=2q_5-2g_5+n_5.}
\tag{2.3}
\]

在 corrected equality ray 上

\[
H-2m=o(S),
\qquad
3T-2m=o(S),
\]

从而

\[
\boxed{|d_2|+|d_5|=o(S).}
\tag{2.4}
\]

因此下面出现的 `2/5` defect factors只有 `10^{o(S)}` 高度。

## 3. phase-normalized rational carrier

将 `(Secondary-norm)` 乘以

\[
2^{d_2^+}5^{d_5^-}Z.
\]

第一项中的二进 exponent满足

\[
2m-4+d_2^+=H+d_2^-,
\]

故由 `(Phase)`：

\[
2^{2m-4+d_2^+}Z
=2^{d_2^-}(5^TU+C_Lv_0).
\]

第二项中的五进 exponent满足

\[
4T-2m+d_5^-=T+d_5^+.
\]

于是

\[
\begin{aligned}
&C_LN(\Delta_1)2^{d_2^+}5^{d_5^-}Z\\
={}&5^T\Bigl(
A_*^2q_c^2\,2^{d_2^-}5^{d_5^-}U
+B_*^2\,2^{d_2^+}5^{d_5^+}Z
\Bigr)\\
&\quad+C_LA_*^2q_c^2\,2^{d_2^-}5^{d_5^-}v_0.
\end{aligned}
\tag{3.1}
\]

定义正整数

\[
\boxed{
\mathcal C_{UZ}
:=
A_*^2q_c^2\,2^{d_2^-}5^{d_5^-}U
+B_*^2\,2^{d_2^+}5^{d_5^+}Z.
}
\tag{UZ-carrier}
\]

因为 `(C_L,5)=1`，由 `(3.1)` 得

\[
\boxed{C_L\mid\mathcal C_{UZ}.}
\tag{3.2}
\]

定义

\[
\boxed{K_{UZ}:=\mathcal C_{UZ}/C_L\in\mathbf Z_{>0}.}
\tag{3.3}
\]

这给出一个完全 rational、没有 Gaussian orientation choice 的 secondary reader。

## 4. quotient 的 exact companion identity

将 `(3.1)` 除以 `C_L` 并移项：

\[
\boxed{
5^TK_{UZ}
=
2^{d_2^+}5^{d_5^-}Z N(\Delta_1)
-A_*^2q_c^2\,2^{d_2^-}5^{d_5^-}v_0.
}
\tag{K-companion}
\]

所以 `(UZ-carrier)` 也可理解为：secondary norm先由 phase把主 `2^H/5^T` smooth ratio消掉，留下一个 `q_c/Z` 尺度的 rational quotient。

注意 `(UZ-carrier)` 与 `(K-companion)` 都是 `(Secondary-norm)+(Phase)` 的严格推论；它们不是第三份独立 height，后续不得重复计费。

## 5. terminal height

corrected terminal ratios为

\[
\log q_c=z_*S+o(S),
\qquad
\log U=(1-z_*)S+o(S),
\qquad
\log Z=z_*S+o(S),
\]

\[
\log C_L=S+o(S),
\qquad
z_*=0.308883577618\ldots,
\]

且

\[
\log|A_*|+\log|B_*|+|d_2|+|d_5|=o(S).
\]

因此 `(UZ-carrier)` 的第一项具有高度

\[
(2z_*+1-z_*)S+o(S)
=(1+z_*)S+o(S),
\]

第二项只有

\[
z_*S+o(S).
\]

两项均为正，故没有 Archimedean cancellation：

\[
\boxed{
\log\mathcal C_{UZ}
=(1+z_*)S+o(S).
}
\tag{5.1}
\]

除去 `C_L`：

\[
\boxed{
\log K_{UZ}
=z_*S+o(S)
=0.308883577618\ldots S+o(S).
}
\tag{K-height}
\]

所以 `K_UZ` 与 `q_c,Z` 恰在同一 terminal scale。

`(UZ-carrier)` 还给近乘法形式

\[
\boxed{
C_LK_{UZ}
=c_Uq_c^2U+c_ZZ,
}
\tag{Near-product}
\]

其中

\[
c_U=A_*^22^{d_2^-}5^{d_5^-},
\qquad
c_Z=B_*^22^{d_2^+}5^{d_5^+},
\]

且

\[
\log c_U+\log c_Z=o(S).
\]

主乘积高度是 `(1+z_*)S`，误差项只有 `z_*S`，即 relative error为

\[
10^{-S+o(S)}.
\]

## 6. `q_c-Z` gcd 的 exact rational re-reader

由 `(Near-product)` 模 `q_c`，并使用 `(C_L,q_c)=1`：

\[
\boxed{
(K_{UZ},q_c)
=(c_ZZ,q_c).
}
\tag{6.1}
\]

同理模 `Z`，使用 `(C_L,Z)=(U,Z)=1`：

\[
\boxed{
(K_{UZ},Z)
=(c_Uq_c^2,Z).
}
\tag{6.2}
\]

因此删去 coefficient overlaps

\[
(q_c,c_Z),\qquad (Z,c_U),
\]

后，`K_UZ` 精确读取旧 `q_c-Z` bottleneck：

\[
\boxed{
\gcd(K_{UZ},q_c)_{\rm main}
=\gcd(Z,q_c)_{\rm main}.
}
\tag{qZ-reader-1}
\]

同时

\[
\boxed{
\gcd(K_{UZ},Z)_{\rm main}
=\gcd(q_c^2,Z)_{\rm main}.
}
\tag{qZ-reader-2}
\]

特别地，若

\[
D_{qZ}:=(q_c,Z)
\]

并删去 `c_Uc_Z` overlap，则

\[
\boxed{D_{qZ}\mid K_{UZ}.}
\tag{qZ-in-K}
\]

所以原先只通过 projective payer 读取的 source overlap，现在也有一个 canonical **rational secondary-norm reader**。

## 7. 局部 valuation split

固定 odd non-decimal prime `p`，假设

\[
p\nmid C_Lc_Uc_ZU,
\]

并写

\[
r=v_p(q_c),
\qquad z=v_p(Z).
\]

由 `(Near-product)`：

\[
v_p(K_{UZ})
=v_p(c_Uq_c^2U+c_ZZ).
\]

若

\[
2r\ne z,
\]

两项 valuation不同，所以

\[
\boxed{v_p(K_{UZ})=\min(2r,z).}
\tag{7.1}
\]

只有 equal-depth sheet

\[
\boxed{z=2r}
\tag{7.2}
\]

可能出现额外 unit-unit cancellation，并使 `v_p(K_UZ)>2r`。

因此 `K_UZ` 把 source/projective overlap重新组织成一个简单的 square-threshold split：

\[
\boxed{
\begin{array}{c|c}
z<2r&v_p(K_{UZ})=z\\
z>2r&v_p(K_{UZ})=2r\\
z=2r&\text{possible extra cancellation}
\end{array}}
\tag{K-local-split}
\]

这与旧 `q-Z` gap/complementary Hensel split不是同一个坐标：旧 split按 sphere/projective reader分类；这里按 phase-normalized secondary norm 的两项 valuation分类。

## 8. no-double-count 与下一目标

`K_UZ` 是新 **canonical rational object**，但不是新独立 equation。其价值是把

\[
(q_c,Z)
\]

这个旧 projective bottleneck转译到一个和 `q_c,Z` 同尺度的正整数上，而不再携带 Gaussian orientation。

因此当前不能从 `(K-height)` 或 `(qZ-in-K)` 直接宣称 strict gap。

真正值得继续检查的是：

1. `K_UZ` 与已有 projective payer `Z_0` 的 common-core是否完全由 `q_c` source baseline解释；
2. equal-depth sheet `z=2r` 的 extra cancellation是否会回到 hidden square / `Delta_U` norm，还是形成真正新 slot；
3. `(Near-product)` 的 `q_c^2` modulus能否和 denominator-prefix 的 `q_c` source congruence形成一个 **location** obstruction，而非另一份 height计数。

若上述三项全部退化，则 `(UZ-carrier)` 应作为新的 no-go/translation lemma保留，而不能继续收费。

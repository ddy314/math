# A2 spontaneous angle 与 source/q/f overlap 的赋值定律

> **依赖：** `spontaneous-angle.md`、`hensel.md`、`spontaneous-angle-parity.md`、`spontaneous-angle-content.md`。
>
> **严格状态：**旧 `Omega_sp` resultant 已把 source、q-side、f-side 的一阶交点分别压回 `D_src` 或 `Delta_0`。本文把这些一阶 resultant 升级为 exact `p`-adic depth laws：在 genuine units 下，angle valuation 由两个接触深度的较浅者决定，只有**等深 cancellation**才可能额外提升。source excess 尤其强：非等深时 angle valuation 精确为偶数 `2h`。因此 angle primitive integer 的 residual odd inert parity 若来自 source pool，只能集中在 source 等深 cancellation 层；q/f pool 也只有等深层能产生超出较浅深度的额外奇偶。本文不宣称这些等深层已经排除，也不宣称 A2 全局关闭。

---

## 1. 统一记号

沿用

\[
d:=225x^2-y,
\qquad
\Delta_0:=2025x^2-18y-y^2,
\]

\[
\Phi_s=(99x-4)r_s-2x-4,
\]

\[
A_{\rm sp}=4d^2-xy^2(99x-4),
\]

\[
\boxed{
\Omega_{\rm sp}
=A_{\rm sp}r_s+2xy^2(x+2)
=4r_sd^2-xy^2\Phi_s.
}
\tag{1.1}
\]

f-denominator line 为

\[
F_f:=r_s(x+2)+2x.
\tag{1.2}
\]

以下所有 valuation law 都只声称用于 genuine non-`2,3,5` inert prime；因此相关 decimal/source denominators、`x,y,r_s,A_sp` 等按对应 channel 的 separation 假设均为单位，除非明确写出的接触量。

---

## 2. `已严格完成`：source excess 非等深时 angle valuation 精确为偶数

设 `p` 为 genuine source excess inert prime，并写

\[
p^{2h}\Vert\sigma,
\qquad h\ge1.
\]

`hensel.md` 已严格证明

\[
\boxed{v_p(\Phi_s)=2h,}
\tag{2.1}
\]

以及

\[
\boxed{v_p(d)\ge h.}
\tag{2.2}
\]

令

\[
e_d:=v_p(d).
\]

由 (1.1)，两项 valuation 分别为

\[
v_p(4r_sd^2)=2e_d,
\]

\[
v_p(xy^2\Phi_s)=2h.
\]

因为 `e_d>=h`，只有两种情况。

### 2.1 严格深于 threshold

若

\[
e_d>h,
\]
则

\[
2h<2e_d.
\]
两项 valuation 不同，较浅项不可能被较深项抵消，因此

\[
\boxed{
v_p(\Omega_{\rm sp})=2h.}
\tag{2.3}
\]

特别地 valuation 必为偶数。

### 2.2 唯一危险层：等深

若

\[
e_d=h,
\]
则两项都恰有深度 `2h`：

\[
\boxed{
v_p(\Omega_{\rm sp})\ge2h,}
\tag{2.4}
\]

而额外提升是否发生只取决于 normalized cancellation

\[
\boxed{
4r_s\left(\frac d{p^h}\right)^2
-xy^2\frac{\Phi_s}{p^{2h}}
\equiv0\pmod p.
}
\tag{2.5}
\]

所以：

\[
\boxed{
\text{source excess 对 angle carrier 产生奇 valuation}
\Longrightarrow
v_p(d)=h
\text{ 且发生 normalized equal-depth cancellation}.}
\tag{2.6}
\]

这比旧 `p^h|D_src` 更明确：source pool 的 ordinary non-equal-depth 部分对 angle inert parity 完全是偶贡献。

---

## 3. `已严格完成`：f-line 的 exact Bézout depth law

从定义直接展开：

\[
\boxed{
(x+2)\Omega_{\rm sp}
-A_{\rm sp}F_f
=-200x^3\Delta_0.
}
\tag{3.1}
\]

这就是旧 resultant

\[
\operatorname{Res}_{r_s}(F_f,\Omega_{\rm sp})
=-200x^3\Delta_0
\]
的无除法版本。

设 genuine prime 同时接触 f-line 与 angle：

\[
p\mid F_f,
\qquad p\mid\Omega_{\rm sp}.
\]
旧一阶结论给

\[
p\mid\Delta_0.
\]

写

\[
e_f:=v_p(F_f),
\qquad
e_\Delta:=v_p(\Delta_0),
\qquad
e_\Omega:=v_p(\Omega_{\rm sp}).
\]

在 genuine f-contact 中

\[
p\nmid x(x+2)A_{\rm sp},
\]
所以 (3.1) 左右三个显式系数都是单位。

若

\[
e_f<e_\Delta,
\]
则右边两项 `A_sp F_f` 与 `200x^3 Delta_0` 深度不同，故

\[
\boxed{e_\Omega=e_f.}
\tag{3.2}
\]

若

\[
e_\Delta<e_f,
\]
则

\[
\boxed{e_\Omega=e_\Delta.}
\tag{3.3}
\]

若

\[
e_f=e_\Delta=e,
\]
则

\[
\boxed{e_\Omega\ge e,}
\tag{3.4}
\]
且只有 normalized cancellation

\[
A_{\rm sp}\frac{F_f}{p^e}
-200x^3\frac{\Delta_0}{p^e}
\equiv0\pmod p
\tag{3.5}
\]
才会使 angle depth 超过 `e`。

因此 compact 写成：

\[
\boxed{
\begin{aligned}
e_f\ne e_\Delta
&\Longrightarrow
v_p(\Omega_{\rm sp})=\min(e_f,e_\Delta),\\
e_f=e_\Delta
&\Longrightarrow
v_p(\Omega_{\rm sp})\ge e_f,
\end{aligned}}
\tag{3.6}
\]

并且只有第二行存在额外 lift。

---

## 4. `已严格完成`：q-line 也有同型 depth law

对 `Omega_sp` 关于 `x+2` 做 exact Euclidean division，可得到

\[
\boxed{
\Omega_{\rm sp}
=400r_s\Delta_0+(x+2)J_q,
}
\tag{4.1}
\]
其中

\[
\boxed{
\begin{aligned}
J_q={}&202500r_sx^3-405000r_sx^2
-99r_sxy^2-1800r_sxy\\
&+202r_sy^2+3600r_sy+2xy^2.
\end{aligned}}
\tag{4.2}
\]

q-denominator formula 为

\[
q=\frac{U(x+2)}{2c_Q},
\]
所以对 genuine q-prime，`U,2c_Q` 为单位且

\[
\boxed{v_p(q)=v_p(x+2).}
\tag{4.3}
\]

若 `p|q` 且 `p|Omega_sp`，旧 q-side resultant 重新给

\[
p\mid\Delta_0.
\]

现在关键是 `J_q` 在共同第一层根上为单位。由 `x=-2`：

\[
J_q(-2,y)
=4\left[100r_s(y^2+18y-8100)-y^2\right].
\]

而 `Delta_0(-2,y)=0` 等价于

\[
y^2+18y-8100=0.
\]
所以在共同根上

\[
\boxed{J_q\equiv-4y^2\not\equiv0\pmod p.}
\tag{4.4}
\]

写

\[
e_q:=v_p(q)=v_p(x+2),
\qquad
e_\Delta:=v_p(\Delta_0).
\]

由 (4.1)、(4.4)：

\[
\boxed{
\begin{aligned}
e_q\ne e_\Delta
&\Longrightarrow
v_p(\Omega_{\rm sp})=\min(e_q,e_\Delta),\\
e_q=e_\Delta
&\Longrightarrow
v_p(\Omega_{\rm sp})\ge e_q,
\end{aligned}}
\tag{4.5}
\]

而第二行的额外 lift 仍只能来自 normalized equal-depth cancellation。

---

## 5. 三类 overlap 的统一表

因此 genuine non-`3` inert overlap 有统一形态：

\[
\boxed{
\begin{array}{c|c|c|c}
\text{pool}&\text{depth 1}&\text{depth 2}&\text{angle depth away from equality}\\ \hline
\text{source}&2h&2e_d,\ e_d\ge h&2h\text{ (even)}\\
q&e_q&e_\Delta&\min(e_q,e_\Delta)\\
f&e_f&e_\Delta&\min(e_f,e_\Delta)
\end{array}}
\tag{5.1}
\]

所有“额外” angle depth 都只存在于

\[
\boxed{\text{equal-depth cancellation locus}.}
\tag{5.2}
\]

source pool 最强：普通非等深 source overlap 对 angle carrier 的 valuation 精确为 `2h`，完全不贡献 odd inert parity。

---

## 6. 对 `G_sp` parity dichotomy 的直接意义

`spontaneous-angle-parity.md` 定义

\[
G_{\rm sp}
=\gcd(\widehat{\mathcal O}_{\rm sp},\widehat{\mathcal T}_2),
\]
且如果

\[
G_{\rm sp}\equiv1\pmod4,
\]
angle residual quotient 必须携带一份 odd inert parity。

`spontaneous-angle-content.md` 已证明这份 parity 不能来自 `c_ug` source content。本文进一步证明：若它来自真正 source excess，则必须落在非常窄的

\[
\boxed{
v_p(d)=h\text{ 的 normalized equal-depth cancellation}}
\tag{6.1}
\]
层；所有 `v_p(d)>h` 的 source overlap 都只给偶 valuation。

q/f residual parity 同样不能来自普通“一个 contact 明显更浅”的情形之外的额外 lift；其未知自由度也被集中到 equal-depth loci。

所以接下来要逼

\[
G_{\rm sp}\equiv3\pmod4
\]
时，不再需要处理整个 source/q/f 参数空间，只需处理三个 equal-depth cancellation shell。特别是 source shell 已从无界二维 Hensel 接触缩成单个 normalized congruence (2.5)。

---

## 7. 当前开放项

本文没有证明 q/f 的 `min(e_*,e_Delta)` 自身一定为偶数，因此尚不能直接排除 denominator pool 对 residual odd parity 的贡献。

下一步最有价值的是：

1. 把 additive side 的 q/f **full saturation exponent** 与 (3.6)/(4.5) 对齐，看 denominator odd-excess 是否正好强迫 equal-depth；
2. 对 source equal-depth congruence (2.5)，利用 `Psi_9` / `D_src` 的第二 Hensel 条件求 normalized residue，尝试证明 cancellation 不发生或只能固定到有限素数；
3. 若三类 equal-depth shell 都被消掉，就会强迫 angle residual quotient `U≡1 mod4`，从而迫使 `G_sp≡3 mod4`。

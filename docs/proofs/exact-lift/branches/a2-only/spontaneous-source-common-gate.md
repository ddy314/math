# A2 source angle-extra 进入 additive common gcd 的 pure-prefix gate

> **依赖：** `spontaneous-source-equal-depth-nogo.md`、`spontaneous-prefix-eliminant.md`、`spontaneous-angle.md`。
>
> **严格状态：**source equal-depth angle extra-lift本身是可解的二阶 Hensel自由度，不能靠 source 局部系统排除。本文加入真正独立的 additive condition `Theta_dec=0` 与 exact sphere：在 source first-layer curve上，第三块再次完全消去，sphere numerator塌成一个显式 quadratic 的平方。因此 source-supported angle prime要进一步进入 angle/additive common gcd，必须命中一个只含 `(x,tau=10^-M)` 的 pure-prefix decimal gate `C_src=0`。该 gate在真实 endpoint box 中统一大于 `448`，所以 common contact只能来自 p-adic wrapping。本文不排除这些 modular roots，也不宣称 A2 全局关闭。

---

## 1. source first-layer curve

沿用

\[
d=225x^2-y,
\qquad
\Phi_s=(99x-4)r_s-2x-4.
\]

真正 source excess prime在 first layer 满足

\[
d\equiv0,
\qquad
\Phi_s\equiv0.
\]

因此令

\[
\boxed{y=225x^2,}
\tag{1.1}

\[
A:=99x-4,
\qquad
\boxed{r_s=\frac{2(x+2)}A.}
\tag{1.2}

source separation保证

\[
p\nmid x(x+2)A.
\tag{1.3}

第三分母 normalized phase

\[
\bar w:=\frac{b_3}{T10^M}
\]
满足 `r_s=x/bar w`，所以

\[
\boxed{
\bar w=\frac{xA}{2(x+2)}.}
\tag{1.4}

---

## 2. additive root恢复第三分子

记

\[
\tau:=10^{-M},
\qquad
s:=9+y,
\]

以及

\[
\bar\zeta:=\frac{a_3}{T10^M}.
\]

`Theta_dec=0` 在 noncentral channel给

\[
\boxed{
\bar\zeta_\Theta
=
\frac{
 x^2(s^2-18s\tau+55\tau^2)
 -\frac1{100}(x+2)^2(2025x^2+y^2)
}
{2x^2(2s-9\tau)}.}
\tag{2.1}

本文只处理 denominator为单位的 generic noncentral source/common channel；central line已由 `spontaneous-prefix-branch-audit.md` 单列。

---

## 3. `已严格完成`：source first-layer 上 sphere numerator 是一个完整平方

exact sphere为

\[
 x^2\bar w^2(s+\bar\zeta)^2
=(x+2+\bar w)^2
\left(
\frac{2025x^2+y^2}{100}\bar w^2+x^2\bar\zeta^2
\right).
\tag{3.1}

把 (1.1)、(1.4)、(2.1) 全部代入 (3.1)，清去 rational denominators。直接因式分解得到

\[
\boxed{
\operatorname{num}(\text{sphere})
=-x^2(25x^2+1)\,\mathcal C_{\rm src}(x,\tau)^2.}
\tag{3.2}

其中

\[
\boxed{
\begin{aligned}
\mathcal C_{\rm src}(x,\tau)
={}&440(x+2)^2\tau^2\\
&+81(9401x^4-2392x^3-1600x^2-64x-64)\tau\\
&-324x(99x-4)(25x^2+1)(49x^2-4x-2).
\end{aligned}}
\tag{3.3}

对 genuine source prime，`x` 为单位；而在 source first layer

\[
2025x^2+y^2
=2025x^2(25x^2+1),
\]
且 base norm为单位，所以

\[
p\nmid25x^2+1.
\tag{3.4}

因此 (3.2) 给出精确 necessary-and-sufficient first-layer gate：

\[
\boxed{
\text{source first-layer angle root}+\Theta_{\rm dec}=0+\text{sphere}
\iff
\mathcal C_{\rm src}(x,\tau)=0\pmod p,}
\tag{3.5}

在本文列出的 genuine/noncentral denominator单位条件下成立。

这就是 source angle-extra 是否进一步成为 additive common carrier 的独立外部接口。

---

## 4. 二阶 source correction完全不进入 common gate

`spontaneous-source-equal-depth-nogo.md` 把 source equal-depth shell写成

\[
y=225x^2-\varepsilon d_1,
\]

\[
r_s=\frac{2(x+2)+\varepsilon^2\phi_2}{99x-4},
\qquad\varepsilon=p^h.
\]

angle extra-lift只是在二阶唯一选择 `phi_2`。而 (3.3) 完全不含

\[
d_1,\quad\phi_2,\quad\sigma^\sharp,\quad\Psi_9^\sharp.
\]

因此 source prime是否进入 additive common gcd，第一层已经由

\[
\boxed{\mathcal C_{\rm src}(x,10^{-M})\equiv0\pmod p}
\tag{4.1}

独立决定；不能通过重新调节二阶 source correction来改变。

这正是 source equal-depth no-go 所缺的“source 外部约束”。

---

## 5. `已严格完成`：defect 坐标中的短表达

真实 denominator defect记为

\[
u:=10x-1=\frac{H}{5^{M-1}},
\qquad
0<u<\frac1{19}.
\]

所以

\[
x=\frac{1+u}{10}.
\]

代入 (3.3) 并乘 `10000`，得到整数系数表达

\[
\boxed{
\begin{aligned}
10000\mathcal C_{\rm src}
={}&44000(u+21)^2\tau^2\\
&+81(9401u^4+13684u^3-175354u^2\\
&\hspace{22mm}-418156u-878519)\tau\\
&-81(u+1)(99u+59)(u^2+2u+5)\\
&\hspace{22mm}\cdot(49u^2+58u-191).
\end{aligned}}
\tag{5.1}

这比 expanded `(x,tau)` polynomial更适合 endpoint natural representative：所有真实 defect都只通过小正参数 `u` 出现。

---

## 6. `已严格完成`：真实 endpoint 上 `C_src` 统一远离零

在

\[
0<u<1/19
\]
中：

\[
u+1>1,
\qquad99u+59>59,
\qquad u^2+2u+5>5.
\]

又

\[
49u^2+58u-191
<\frac{49}{19^2}+\frac{58}{19}-191
< -187.
\]

因此 (5.1) 最后一项为正，而且除以 `10000` 后单独给出粗下界

\[
\frac{81\cdot59\cdot5\cdot187}{10000}>446.
\tag{6.1}

更直接使用原 `x`-box

\[
\frac1{10}<x<\frac2{19}
\]
可得到稍强的 constant-term 下界：

\[
\begin{aligned}
&-324x(99x-4)(25x^2+1)(49x^2-4x-2)\\
&\qquad>
324\cdot\frac1{10}\cdot\frac{59}{10}\cdot\frac54\cdot\frac{678}{361}
=
\frac{1620081}{3610}
>448.77.
\end{aligned}
\tag{6.2}

线性 coefficient

\[
H_4(x):=9401x^4-2392x^3-1600x^2-64x-64
\]
满足粗界

\[
|H_4(x)|<93
\tag{6.3}

因为各绝对项在 `x<2/19` 上总和小于 `93`。

而实际

\[
0<\tau=10^{-M}\le10^{-11}.
\]
因此线性项的绝对值小于

\[
81\cdot93\cdot10^{-11}<8\cdot10^{-8}.
\tag{6.4}

二次项非负。综合：

\[
\boxed{
\mathcal C_{\rm src}(x,10^{-M})>448.77-8\cdot10^{-8}>448.}
\tag{6.5}

所以 source→common gate在真实轴上与零有巨大的统一距离。

---

## 7. `审计`：这仍不是 modular contradiction

(6.5) 不能推出

\[
p\nmid\mathcal C_{\rm src}
\]
因为 `p`-adic divisibility不要求实数接近零。其意义与此前 sphere-root sign gap相同：所有 source→common contact都必须靠真正的 modular wrapping实现。

若要把 (6.5) 升级为空性，必须比较清分母后的自然整数 representative 与 source prime-power depth，或与 decimal orbit `tau=10^-M` 做高阶同步。

---

## 8. common gate 的 tau-discriminant

把 (3.3) 看成 `tau` 的 quadratic，其 discriminant为

\[
\boxed{
\operatorname{Disc}_\tau(\mathcal C_{\rm src})
=81\mathcal D_{\rm srccom}(x),}
\tag{8.1}

其中

\[
\boxed{
\begin{aligned}
\mathcal D_{\rm srccom}(x)={}&
8012458881x^8-332013104x^7+1027170624x^6\\
&+111485312x^5+130846848x^4+25281536x^3\\
&+12020736x^2+888832x+331776.
\end{aligned}}
\tag{8.2}

所以即使 source angle-extra已经存在，进一步进入 common gcd仍要求 decimal length在一个明确 quadratic extension 中选根。本文不把该 discriminant character当成 closure；它只是后续 decimal-orbit Hensel同步的规范对象。

---

## 9. 更新后的 source residual frontier

source angle residual现在具有两层彼此独立的结构：

1. source 局部二阶 extra-lift：
   \[
   \phi_2=
   \frac{8(x+2)}{50625(99x-4)x^5}d_1^2;
   \]
   这是 simple local freedom；
2. additive common gate：
   \[
   \mathcal C_{\rm src}(x,10^{-M})=0\pmod p;
   \]
   这是 pure-prefix/decimal external constraint。

因此 `G_sp=1 mod4` 中 source-over-saturated angle residual能否保持为“只在 angle side出现”的 prime，已经不再是模糊问题，而精确等价于：source extra-lift成立但 `C_src` 不成立。

下一步最值得做的是把 `C_src` 与 `D_src` / source length orbit / natural integer representative联立；继续只研究 `phi_2` 已无新增信息。

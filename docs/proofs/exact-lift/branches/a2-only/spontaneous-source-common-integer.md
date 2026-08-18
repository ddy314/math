# A2 source→common gate 的自然整数代表与 singular/transverse audit

> **依赖：** `spontaneous-source-common-gate.md`、`spontaneous-source-equal-depth-nogo.md`、`spontaneous-source-saturation-parity.md`。
>
> **严格状态：**本文先把 source→additive-common 的 normalized first-layer gate `C_src(x,tau)` 精确乘回真实 denominator defect `H` 与 decimal length `M`，得到整数 target `K_src(H,E,F)`。随后完整审计该投影 gate 的 non-`3` inert singular bad reduction：唯一 genuine singular first-layer point位于 `p=1746991`。仅证明 `C_src=0` 自身不能升到 `p^2` **不足以**关闭完整 source/common 系统，因为 higher source layer允许离开 `d=Phi=0` 切片；本文进一步把真实 source transverse correction与 angle extra-lift一起代回 `Theta_dec + exact sphere`，证明该唯一 singular point对任意 source half-depth `h>=1` 都无法成为 full source/common lift。generic simple roots仍可能存在，因此本文不宣称 A2 全局关闭。

---

## 1. source→common first-layer quadratic

沿用

\[
\boxed{
\begin{aligned}
\mathcal C_{\rm src}(x,\tau)
={}&440(x+2)^2\tau^2\\
&+81(9401x^4-2392x^3-1600x^2-64x-64)\tau\\
&-324x(99x-4)(25x^2+1)(49x^2-4x-2).
\end{aligned}}
\tag{1.1}
\]

在 genuine/noncentral source first layer

\[
d:=225x^2-y=0,
\qquad
\Phi_s=(99x-4)r_s-2x-4=0,
\]
且 `Theta_dec=0` 时，exact sphere 的清分母 numerator 为

\[
-x^2(25x^2+1)\mathcal C_{\rm src}(x,\tau)^2.
\tag{1.2}
\]

因此

\[
\boxed{
\mathcal C_{\rm src}(x,10^{-M})\equiv0\pmod p
}
\tag{1.3}
\]

是 source-supported angle prime进入 additive common channel 的 first-layer gate。

---

# 第一部分：真实 defect 的自然整数代表

## 2. `已严格完成`：`C_src` 精确整数化

真实 endpoint denominator defect写成

\[
x=\frac{1+u}{10},
\qquad
u=\frac{H}{5^{M-1}}.
\]

定义

\[
\boxed{F:=5^{M-1},\qquad E:=2^{M-1}.}
\tag{2.1}
\]

于是

\[
u=H/F,
\qquad
\tau=10^{-M}=\frac1{10EF}.
\tag{2.2}
\]

已有 defect form

\[
\begin{aligned}
10000\mathcal C_{\rm src}
={}&44000(u+21)^2\tau^2\\
&+81(9401u^4+13684u^3-175354u^2-418156u-878519)\tau\\
&-81(u+1)(99u+59)(u^2+2u+5)(49u^2+58u-191).
\end{aligned}
\tag{2.3}
\]

把 (2.2) 代入并清去全部 `2,5` denominator：

\[
\boxed{
10E^2F^6\,(10000\mathcal C_{\rm src})
=\mathcal K_{\rm src}(H,E,F),}
\tag{2.4}
\]

其中

\[
\boxed{
\begin{aligned}
\mathcal K_{\rm src}
={}&4400F^2(H+21F)^2\\
&+81EF\,\mathcal P_4(H,F)\\
&-810E^2(H+F)(99H+59F)\\
&\qquad\cdot(H^2+2HF+5F^2)(49H^2+58HF-191F^2),
\end{aligned}}
\tag{2.5}
\]

\[
\boxed{
\begin{aligned}
\mathcal P_4(H,F):={}&9401H^4+13684H^3F-175354H^2F^2\\
&-418156HF^3-878519F^4.
\end{aligned}}
\tag{2.6}
\]

所以对 genuine source prime `p !=2,5`，单纯作为数值 identity：

\[
\boxed{
v_p(\mathcal C_{\rm src})=v_p(\mathcal K_{\rm src}).}
\tag{2.7}
\]

特别地 first-layer condition (1.3) 等价于

\[
\boxed{p\mid\mathcal K_{\rm src}(H,E,F).}
\tag{2.8}
\]

这里必须保留逻辑边界：`C_src` 是先限制到 `d=Phi=0` 得到的投影 gate；(2.7) **不**意味着 full higher source/common system 的全部 prime-power depth都由 `K_src` 独自读取。后文会显式处理 transverse correction。

---

## 3. genuine source units 的 defect 形式

\[
x=\frac{H+F}{10F},
\qquad
99x-4=\frac{99H+59F}{10F},
\]

\[
25x^2+1=\frac{H^2+2HF+5F^2}{4F^2}.
\]

因此 source separation中的 `x`、`99x-4`、base norm units在 `K_src` 中都有直接整数对应；整数化没有制造新的伪 boundary。

---

# 第二部分：projected gate 的 singular bad set

## 4. `tau`-discriminant与固定 bad primes

把 (1.1) 看成

\[
\mathcal C_{\rm src}=a(x)\tau^2+b(x)\tau+c(x),
\qquad a(x)=440(x+2)^2.
\]

其 discriminant为

\[
\boxed{
\operatorname{Disc}_\tau(\mathcal C_{\rm src})
=81\mathcal D_{\rm sc}(x),}
\tag{4.1}
\]

\[
\boxed{
\begin{aligned}
\mathcal D_{\rm sc}(x)={}&8012458881x^8-332013104x^7+1027170624x^6\\
&+111485312x^5+130846848x^4+25281536x^3\\
&+12020736x^2+888832x+331776.
\end{aligned}}
\tag{4.2}
\]

而

\[
\boxed{
\begin{aligned}
\operatorname{Disc}_x(\mathcal D_{\rm sc})
={}&2^{96}3^55^4 11^4 101^{24}\cdot109\cdot233\\
&\cdot1746991\cdot405504443^2.
\end{aligned}}
\tag{4.3}
\]

所以 genuine non-`3` inert singular projection只需审计

\[
\boxed{11,\quad1746991,\quad405504443.}
\tag{4.4}
\]

当 `p` 不整除 `2a(x)` 时，repeated `tau` root满足 `tau=-b/(2a)`；在该 root上，`Disc_tau'=-4a partial_x C_src`。故 full projected singularity等价于 `D_sc=D_sc'=0`。`p=11` 因 `440=0 mod 11` 单独处理。

---

## 5. `p=11` 与 `p=405504443` 均无 finite singular projection

模 `11`：

\[
\boxed{
\partial_\tau\mathcal C_{\rm src}
\equiv-5(x^2-5x-1)(x^2-2x-5).}
\tag{5.1}
\]

两个二次因子的判别式分别为 `7,2`，均为模 `11` 非平方，所以 `dC/dtau` 在 `F_11` 从不为零；没有 singular projection。

对 `p=405504443`：

\[
\boxed{
\gcd(\mathcal D_{\rm sc},\mathcal D_{\rm sc}')
=x^2-63668219x+95115196.}
\tag{5.2}
\]

其 discriminant为 `345543957`，并满足

\[
\left(\frac{345543957}{405504443}\right)=-1.
\]

故也没有 `F_p` repeated root。

---

## 6. 唯一 genuine singular projection：`p=1746991`

\[
\boxed{
\gcd(\mathcal D_{\rm sc},\mathcal D_{\rm sc}')
=x+384338\pmod p.}
\]

唯一 residue为

\[
\boxed{x_0=1362653,\qquad\tau_0=807263\pmod p.}
\tag{6.1}
\]

并且

\[
\mathcal C_{\rm src}
=\partial_x\mathcal C_{\rm src}
=\partial_\tau\mathcal C_{\rm src}=0\pmod p.
\tag{6.2}
\]

以下 genuine/noncentral factors 的 residues分别为

\[
1362653,\quad1362655,\quad384336,\quad1554823,\quad1504546,
\tag{6.3}
\]

对应 `x_0, x_0+2, 99x_0-4, 25x_0^2+1, 2(9+225x_0^2)-9tau_0`，全部为单位。

对最小非负 representatives还有

\[
\boxed{
\frac{\mathcal C_{\rm src}(x_0,\tau_0)}p
\equiv1642591\not\equiv0\pmod p.}
\tag{6.4}
\]

由于两个 projected derivatives 都被 `p` 整除，任何 `x=x_0+pX, tau=tau_0+pT` 都仍满足

\[
\boxed{v_p(\mathcal C_{\rm src})=1.}
\tag{6.5}
\]

注意：(6.5) 只说明 projected gate `C_src=0` 不能自身升到 `p^2`；此处尚不能推出 full source/common 不可提升。

---

# 第三部分：source transverse correction补上 projected audit 的逻辑缺口

## 7. source higher layer 的规范坐标

source excess写成

\[
p^{2h}\Vert\sigma,
\qquad h\ge1.
\]

只有 `v_p(d)=h` 的 equal-depth shell可能产生 extra angle depth。令

\[
\varepsilon:=p^h,
\qquad d=\varepsilon D,\quad D\in\mathbf Z_p^\times,
\]

并写

\[
\Phi_s=\varepsilon^2\phi.
\]

则

\[
\boxed{
r_s=\frac{2(x+2)+\varepsilon^2\phi}{99x-4}.}
\tag{7.1}
\]

angle extra-lift唯一规定

\[
\boxed{
\phi
\equiv
\frac{8(x+2)}{50625(99x-4)x^5}D^2\pmod p.}
\tag{7.2}
\]

在 singular residue (6.1) 上：

\[
\boxed{\phi\equiv1007439D^2\pmod p.}
\tag{7.3}
\]

---

## 8. `已严格完成`：source slice 与 transverse direction 二阶相切

令 `S_Theta` 表示先用 `Theta_dec=0` 恢复第三分子、再代入 exact sphere 后的 rational residual；同时取 source linear line

\[
r_s=\frac{2(x+2)}{99x-4}.
\]

在 `y_0=225x^2` 上，除了 numerator square (1.2) 外，还存在 exact tangency：

\[
\boxed{
\left.\partial_y\mathscr S_\Theta\right|_{y=y_0}
=\mathcal C_{\rm src}(x,\tau)
\frac{\mathcal P_d(x,\tau)}
{23328(x+2)^4(50x^2+2-\tau)^3},}
\tag{8.1}
\]

其中

\[
\boxed{
\begin{aligned}
\mathcal P_d={}&783481\tau^2x^6-105752\tau^2x^5-40720\tau^2x^4\\
&-1664\tau^2x^3-1664\tau^2x^2-78586200\tau x^8\\
&+9590400\tau x^7-195048\tau x^6+254016\tau x^5\\
&+117936\tau x^4-5184\tau x^3+1964655000x^{10}\\
&-239760000x^9+83462400x^8-15940800x^7\\
&-2753352x^6-124416x^5-117936x^4+5184x^3.
\end{aligned}}
\tag{8.2}
\]

对 (6.1) 的 genuine/noncentral residue，(8.1) denominator为单位。因此 singular projection上

\[
\boxed{\partial_y\mathscr S_\Theta\equiv0\pmod p.}
\tag{8.3}
\]

所以 projected square 与 source transverse direction确实同阶相切；必须看二阶，不能从 (6.5) 直接宣布 full no-lift。

---

## 9. `已严格完成`：`h=1` 的完整二阶 lift被 angle correction杀死

固定 `p=1746991`、`h=1`，写

\[
\boxed{
\begin{aligned}
x&=x_0+pX,\\
\tau&=\tau_0+pT,\\
d&=pD,\qquad D\ne0\pmod p,\\
\Phi_s&=p^2\phi.
\end{aligned}}
\tag{9.1}
\]

把 (9.1)、source root (7.1)、`Theta_dec=0` 的第三分子以及 exact sphere全部做二阶 Taylor。exact checker给出

\[
\boxed{
\frac{\mathscr S_\Theta}{p^2}
\equiv32070D^2-680549\phi\pmod p.}
\tag{9.2}
\]

`X,T` 完全消失。代入 (7.3)：

\[
\boxed{
\frac{\mathscr S_\Theta}{p^2}
\equiv286982D^2\pmod p.}
\tag{9.3}
\]

由于 `286982 !=0 mod p` 且 `D` 为单位，矛盾。因此

\[
\boxed{
\text{the }1746991\text{ singular source/common state has no }h=1\text{ lift}.}
\tag{9.4}
\]

---

## 10. `已严格完成`：`h>=2` 也不能绕过 projected square depth

若 `h>=2`，则

\[
v_p(d)\ge2,
\qquad
v_p(\Phi_s)=2h\ge4.
\]

由 (6.5)，任意 projected lift都保持 `v_p(C_src)=1`。在 `d=Phi=0` slice上，sphere numerator 的 `C_src^2` 项因此恰从深度 `2` 开始。

而 transverse correction满足：

- 由 (8.1)，线性 `d` 修正的 coefficient 自带一份 `C_src`，深度至少 `h+1>=3`；
- `d^2` 项深度至少 `4`；
- `Phi_s` 导致的 source-ratio correction从深度 `2h>=4` 才开始。

因此谁都不能抵消已有的 `p^2` 主项。故

\[
\boxed{
\text{the }1746991\text{ singular state has no full source/common lift for any }h\ge2.}
\tag{10.1}
\]

与 (9.4) 合并：

\[
\boxed{
\text{the unique genuine singular projection at }p=1746991
\text{ is dead for every source half-depth }h\ge1.}
\tag{10.2}
\]

---

## 11. 更新后的严格 frontier

现在可以无逻辑缺口地写：

\[
\boxed{
\text{source→common channel没有 surviving genuine non-3 inert singular Hensel tree}.}
\tag{11.1}
\]

剩余结构为：

1. source base primary `p^{2h}` 对 angle parity为偶深；
2. source-local angle extra是 simple second-order correction；
3. external common first layer由 integer gate `K_src` 控制；
4. projected singular bad set有限，唯一 genuine point `1746991` 经 full transverse audit后对所有 `h>=1` 都死亡；
5. 真正剩余的是 **simple source→common roots 与真实 decimal defect orbit `(H,E,F)` 的同步**。

下一步不应再做 singular-discriminant hunting。最有价值的是寻找 `K_src` 与 source prefix depth `D_src` 之间的 denominator-style simple residual，或者直接研究 simple root的 decimal orbit / natural representative。
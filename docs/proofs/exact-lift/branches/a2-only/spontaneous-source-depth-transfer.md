# A2 source→common 的 half-depth transfer

> **依赖：** `spontaneous-source-common-gate.md`、`spontaneous-source-prefix-simple.md`、`spontaneous-source-saturation-parity.md`、`spontaneous-angle.md`。
>
> **严格状态：**本文解释 `C_src(x,tau)` 的局部几何含义，并把 source half-depth 与 additive cofactor depth 对齐。对 genuine non-`3` inert source prime `p^{2h} || sigma`，source Hensel 给 `v_p(d)>=h`、`v_p(Phi_s)=2h`。本文证明真实 sphere third-numerator root在模 `p^h` 内必贴住 source slice 的 double root，而 `Theta_dec=0` 的 affine root与该 double root之差恰为 `C_src` 乘一个单位。因此在 generic noncentral channel有截断赋值律
>
> `min(v_p(widehat(T)_2),h)=min(v_p(C_src),h)`。
>
> 这给出 source 版的 depth matrix；它不证明 `C_src` 的 simple decimal lifts不存在，也不宣称 A2 全局关闭。

---

## 1. source slice 的 double-sphere root

沿用

\[
d:=225x^2-y,
\qquad
\Phi_s=(99x-4)r_s-2x-4.
\]

source first layer为

\[
y_0:=225x^2,
\qquad
r_0:=\frac{2(x+2)}{99x-4}.
\tag{1.1}
\]

用

\[
\bar w:=\frac{b_3}{T10^M},
\qquad r_s=\frac{x}{\bar w},
\]
可得 source slice 的 third-denominator phase

\[
\boxed{
\bar w_0
=\frac{x(99x-4)}{2(x+2)}.}
\tag{1.2}
\]

exact sphere写成

\[
\mathscr S(x,y,\bar w,\bar\zeta)
:=x^2\bar w^2(9+y+\bar\zeta)^2
-(x+2+\bar w)^2
\left(
\frac{2025x^2+y^2}{100}\bar w^2+x^2\bar\zeta^2
\right).
\tag{1.3}
\]

把 `(y,w)=(y_0,w_0)` 代入，直接因式分解：

\[
\boxed{
\mathscr S(x,y_0,\bar w_0,\bar\zeta)
=-\frac{x^2(25x^2+1)}{64(x+2)^4}
\left[
16(x+2)^2\bar\zeta-x^2(297x-12)^2
\right]^2.}
\tag{1.4}
\]

因此 source slice 上 sphere 有唯一 double root

\[
\boxed{
\bar\zeta_s
=\frac{x^2(297x-12)^2}{16(x+2)^2}.}
\tag{1.5}
\]

对 genuine source prime，`x(x+2)(25x^2+1)` 都是单位，所以 (1.4) 的 quadratic coefficient也是单位。事实上

\[
\boxed{
[\bar\zeta^2]\,\mathscr S(x,y_0,\bar w_0,\bar\zeta)
=-4x^2(25x^2+1).}
\tag{1.6}
\]

---

## 2. `已严格完成`：`C_src` 就是 additive root 到 double center 的距离

在 noncentral channel，`Theta_dec=0` 给

\[
\bar\zeta_\Theta(x,y,\tau)
=
\frac{
 x^2((9+y)^2-18(9+y)\tau+55\tau^2)
 -\frac1{100}(x+2)^2(2025x^2+y^2)
}
{2x^2(2(9+y)-9\tau)}.
\tag{2.1}
\]

把 `y=y_0=225x^2` 代入，和 (1.5) 相减。exact factorization为

\[
\boxed{
\bar\zeta_\Theta(x,y_0,\tau)-\bar\zeta_s
=
\frac{\mathcal C_{\rm src}(x,\tau)}
{144(x+2)^2(50x^2+2-\tau)}.}
\tag{2.2}
\]

这里 `C_src` 正是 `spontaneous-source-common-gate.md` 的

\[
\begin{aligned}
\mathcal C_{\rm src}(x,\tau)
={}&440(x+2)^2\tau^2\\
&+81(9401x^4-2392x^3-1600x^2-64x-64)\tau\\
&-324x(99x-4)(25x^2+1)(49x^2-4x-2).
\end{aligned}
\tag{2.3}
\]

因此 `C_src` 不是一个黑箱 resultant：它精确测量 additive affine root 与 source double-sphere center 的距离。

在本文 generic channel中

\[
p\nmid144(x+2)^2(50x^2+2-\tau),
\tag{2.4}
\]
所以

\[
\boxed{
v_p(\bar\zeta_\Theta(x,y_0,\tau)-\bar\zeta_s)
=v_p(\mathcal C_{\rm src}).}
\tag{2.5}
\]

---

## 3. source half-depth 把真实 third denominator贴到 slice达 `2h`

固定 genuine source excess prime

\[
p^{2h}\Vert\sigma,
\qquad h\ge1.
\]

旧 source Hensel 给

\[
\boxed{v_p(\Phi_s)=2h,}
\tag{3.1}
\]
以及

\[
\boxed{v_p(d)\ge h.}
\tag{3.2}
\]

令 `A=99x-4`。由

\[
\Phi_s=A(r_s-r_0)
\]
且 `A` 为单位，

\[
\boxed{v_p(r_s-r_0)=2h.}
\tag{3.3}
\]

又 `bar w=x/r_s` 且 `x,r_s,r_0` 都为单位，所以

\[
\boxed{v_p(\bar w-\bar w_0)=2h.}
\tag{3.4}
\]

同时

\[
y-y_0=-d,
\qquad
\boxed{v_p(y-y_0)\ge h.}
\tag{3.5}
\]

---

## 4. `已严格完成`：真实 sphere root 必在 `p^h` 内贴住 double center

令真实 third-numerator phase写成

\[
\bar\zeta=\bar\zeta_s+Z.
\]

把 exact sphere视为关于 `Z` 的 quadratic：

\[
aZ^2+bZ+c=0.
\tag{4.1}
\]

在 source slice `(y_0,w_0,zeta_s)` 上：

\[
\mathscr S=0,
\qquad
\partial_{\bar\zeta}\mathscr S=0,
\tag{4.2}
\]

并且还有关键 tangency

\[
\boxed{
\left.\partial_y\mathscr S\right|_{(y_0,\bar w_0,\bar\zeta_s)}=0.}
\tag{4.3}
\]

而

\[
\left.\partial_{\bar w}\mathscr S\right|_{(y_0,\bar w_0,\bar\zeta_s)}
=-\frac{81x^4(99x-4)^2(101x^2+4x+8)^2}
{128(x+2)^3},
\tag{4.4}
\]
可非零，但 (3.4) 已给 `bar w-bar w_0` 深度 `2h`。

因此由 Taylor 展开和 (3.4)–(3.5)：

\[
\boxed{v_p(c)\ge2h,}
\tag{4.5}
\]

\[
\boxed{v_p(b)\ge h.}
\tag{4.6}
\]

而由 (1.6)，quadratic coefficient `a` 仍为单位。

若反设 `v_p(Z)<h`，则三项深度分别满足

\[
2v_p(Z)
< h+v_p(Z),
\qquad
2v_p(Z)<2h,
\]
所以单位首项 `aZ^2` 具有唯一最小 valuation，不可能与其余两项相消。矛盾。

故

\[
\boxed{
v_p(\bar\zeta-\bar\zeta_s)\ge h.}
\tag{4.7}
\]

这个结论不需要 source roots在 `p^h` 层已经分开；即使额外 branch-collision 使分裂更深，也仍成立。

---

## 5. additive affine root 对真实 `y` 的移动也只有 `p^h`

由 (2.1) 直接相减可因式分解：

\[
\boxed{
\bar\zeta_\Theta(x,y,\tau)
-\bar\zeta_\Theta(x,y_0,\tau)
=(225x^2-y)\,\mathcal U_\Theta(x,y,\tau),}
\tag{5.1}
\]

其中 `U_Theta` 的 denominator在 generic source channel中为单位。因此 (3.2) 给

\[
\boxed{
v_p(
\bar\zeta_\Theta(x,y,\tau)
-\bar\zeta_\Theta(x,y_0,\tau))\ge h.}
\tag{5.2}
\]

结合 (2.2)、(4.7)：

\[
\bar\zeta_\Theta(x,y,\tau)-\bar\zeta
=
\frac{\mathcal C_{\rm src}}
{144(x+2)^2(50x^2+2-\tau)}
+O(p^h).
\tag{5.3}
\]

因此

\[
\boxed{
\min\left\{
v_p(\bar\zeta_\Theta-\bar\zeta),h
\right\}
=
\min\left\{
v_p(\mathcal C_{\rm src}),h
\right\}.}
\tag{5.4}
\]

---

## 6. `已严格完成`：source half-depth matrix

由

\[
\Theta_{\rm dec}
=T\mathcal R_\Theta-2B^2(2K-9)a_3
\]
和 `a_3=TN bar zeta`，得到 exact affine factorization

\[
\boxed{
\Theta_{\rm dec}
=2B^2(2K-9)TN
(\bar\zeta_\Theta-\bar\zeta).}
\tag{6.1}
\]

在 genuine noncentral source prime上，前面的 coefficient为 `p`-进单位；`widehat(T)_2` 与 `Theta_dec` 又只差固定 `2`-power。因此 (5.4) 给

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),h\}
=
\min\{v_p(\mathcal C_{\rm src}),h\}.}
\tag{6.2}

另一方面 `spontaneous-source-saturation-parity.md` 已有

\[
\boxed{v_p(\widehat{\mathcal O}_{\rm sp})\ge2h.}
\tag{6.3}

故对 common gcd

\[
G_{\rm sp}=\gcd(
\widehat{\mathcal O}_{\rm sp},
\widehat{\mathcal T}_2),
\]
也有

\[
\boxed{
\min\{v_p(G_{\rm sp}),h\}
=
\min\{v_p(\mathcal C_{\rm src}),h\}.}
\tag{6.4}

这就是 source pool 对 `G_sp` 的规范 half-depth matrix。

---

## 7. 新的 source common dichotomy

令

\[
c_p:=v_p(\mathcal C_{\rm src}).
\]

由 (6.2)：

### unsaturated source-common

若

\[
c_p<h,
\]
则

\[
\boxed{
v_p(\widehat{\mathcal T}_2)=v_p(G_{\rm sp})=c_p.}
\tag{7.1}
\]

因此 source common 的低于 half-depth 部分完全由 pure-prefix/decimal gate `C_src` 读取。

### half-depth saturation

若

\[
c_p\ge h,
\]
则

\[
\boxed{p^h\mid\widehat{\mathcal T}_2,}
\qquad
\boxed{p^h\mid G_{\rm sp}.}
\tag{7.2}

从这一层开始，source transverse split 与 additive root位于同一尺度；后续必须使用 normalized blow-up，而不能继续把 `C_src` 当作独立的一变量 root。

因此 source common 的开放机制已经被精确压成

\[
\boxed{
\text{simple unsaturated `C_src` depth}
\quad\text{or}\quad
\text{half-depth saturated blow-up}.}
\tag{7.3}

`spontaneous-source-singular-decimal-orbit.md` 已经关闭 projected singular sector，所以 generic `C_src` roots本身都是 simple；本文新增的是它们与真实 source half-depth / additive cofactor的精确 valuation transfer。
# A2 spontaneous sphere 的两个有理第三分子根

> **依赖：** `spontaneous-prefix-eliminant.md`、`spontaneous-prefix-branch-audit.md`。
>
> **严格状态：**本文解释 `Q_1,Q_2` 为什么会出现：`Omega_sp=0` 固定第三分母后，exact sphere 关于 normalized third numerator 本身已经分裂成两个有理函数根；`Q_1,Q_2` 只是 `Theta_dec` root 与这两个 sphere root 的交点。还证明在真实 endpoint box 中两个 sphere root 都严格小于 `-4.77`，而真实 third digit phase 为正且 `O(10^{-M})`。这提供新的 Archimedean separation，但尚未把 modular divisibility 升级成全局矛盾。

---

## 1. 记号

继续使用

\[
x=\frac{b_2}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}},
\qquad
\tau=10^{-M}.
\]

定义

\[
d:=225x^2-y,
\]

\[
A_{\rm sp}:=4d^2-xy^2(99x-4),
\]

\[
A_-:=A_{\rm sp}-2y^2(x+2)^2,
\]

\[
\Delta_0:=2025x^2-18y-y^2.
\]

第三块 normalized decimal phases 为

\[
\bar w:=\frac{b_3}{T10^M},
\qquad
\bar\zeta:=\frac{a_3}{T10^M}.
\tag{1.1}
\]

`Omega_sp=0` 已给

\[
\boxed{
\bar w=-\frac{A_{\rm sp}}{2y^2(x+2)}.
}
\tag{1.2}
\]

---

## 2. `已严格完成`：固定 `bar w` 后 sphere discriminant 是完整平方

exact sphere 在 `(x,y,bar w,bar zeta)` 中为

\[
\boxed{
 x^2\bar w^2(9+y+\bar\zeta)^2
=(2+x+\bar w)^2
\left(
\frac{2025x^2+y^2}{100}\bar w^2
+x^2\bar\zeta^2
\right).
}
\tag{2.1}
\]

把 (1.2) 代入，把 (2.1) 看成 `bar zeta` 的二次式。直接计算 discriminant：

\[
\boxed{
\operatorname{disc}_{\bar\zeta}
=
\left[
7200x^2y^3(x+2)^2dA_-A_{\rm sp}
\right]^2.
}
\tag{2.2}
\]

所以一旦 spontaneous angle condition 固定第三分母，sphere 不再提供新的 quadratic-character gate：它已经在函数域 `Q(x,y)` 上完全 split。

这也解释 `spontaneous-prefix-eliminant.md` 为什么最终会得到两个而不是一个 quadratic branch。

---

## 3. `已严格完成`：两个 sphere root 显式化

定义

\[
\boxed{
A_+
:=202500x^4+99x^2y^2-4xy^2-4y^2,
}
\tag{3.1}
\]

以及

\[
\boxed{
\begin{aligned}
G_*:={}&410062500x^6
-407025x^4y^2
-7290000x^4y
-8100x^3y^2\\
&+99x^2y^4
+3600x^2y^3
+24300x^2y^2
-4xy^4-4y^4.
\end{aligned}}
\tag{3.2}
\]

则 (2.1) 的两个根精确为

\[
\boxed{
\bar\zeta_1
=-\frac{A_+A_{\rm sp}}
{400x^2y^3(x+2)^2},
}
\tag{3.3}
\]

\[
\boxed{
\bar\zeta_2
=\frac{A_{\rm sp}G_*}
{400x^2y^3(x+2)^2\Delta_0}.
}
\tag{3.4}
\]

它们的差进一步完全因子化：

\[
\boxed{
\bar\zeta_2-\bar\zeta_1
=\frac{
9dA_-A_{\rm sp}
}{
200x^2y^3(x+2)^2\Delta_0
}.
}
\tag{3.5}
\]

因此在 genuine separation

\[
p\nmid dA_-A_{\rm sp}\Delta_0xy(x+2)
\]
下，两个 sphere root 在模 `p` 中也严格不同。

`A_-=0` 正是 sphere double-root locus；`spontaneous-prefix-branch-audit.md` 已证明它同时是 concatenated numerator / denominator 双零的 common-`alpha` 通道。

---

## 4. `已严格完成`：`Q_1,Q_2` 就是 `Theta` root 撞两个 sphere roots

在 noncentral channel `2K-9\ne0`，`Theta_dec=0` 给 normalized root

\[
\boxed{
\bar\zeta_\Theta(\tau)
=
\frac{
 x^2\bigl((9+y)^2-18(9+y)\tau+55\tau^2\bigr)
 -\frac1{100}(x+2)^2(2025x^2+y^2)
}
{2x^2\bigl(2(9+y)-9\tau\bigr)}.
}
\tag{4.1}
\]

直接清分母可得：

\[
\boxed{
\operatorname{num}
(\bar\zeta_\Theta-\bar\zeta_1)
=\mathcal Q_1(\tau;x,y),
}
\tag{4.2}
\]

\[
\boxed{
\operatorname{num}
(\bar\zeta_\Theta-\bar\zeta_2)
=-\mathcal Q_2(\tau;x,y).
}
\tag{4.3}
\]

所以两个几十项 quadratic 的几何含义完全明确：

\[
\boxed{
\begin{array}{ccl}
\mathcal Q_1=0
&\Longleftrightarrow&
\bar\zeta_\Theta=\bar\zeta_1,\\
\mathcal Q_2=0
&\Longleftrightarrow&
\bar\zeta_\Theta=\bar\zeta_2.
\end{array}}
\tag{4.4}
\]

这不是两个任意 resultant factors，而是 sphere 的两种真实 algebraic orientation。

---

## 5. `已严格完成`：真实 endpoint box 中两个 sphere roots 都远在负半轴

当前危险 endpoint 有

\[
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1.
\tag{5.1}
\]

已有

\[
d>\frac54,
\qquad
\Delta_0>\frac54,
\qquad
A_{\rm sp}>\frac{8049}{1444}.
\tag{5.2}
\]

### 5.1 `A_-` 严格为负

\[
A_-
=202500x^4-101x^2y^2-1800x^2y-4xy^2-4y^2.
\]

在 (5.1) 上

\[
\frac{\partial A_-}{\partial x}>0,
\qquad
\frac{\partial A_-}{\partial y}<0.
\]

所以最大值位于

\[
x=\frac2{19},
\qquad
y=\frac{249}{250}.
\]

该点精确值为

\[
\boxed{
A_-
<-\frac{8129844}{16290125}<0.
}
\tag{5.3}
\]

于是由 (3.5)：

\[
\boxed{
\bar\zeta_2<\bar\zeta_1.
}
\tag{5.4}
\]

### 5.2 第一根已有统一负下界

`A_+` 在 box 中对 `x` 递增、对 `y` 递减，所以

\[
A_+>A_+(1/10,1)=\frac{421}{25}.
\tag{5.5}
\]

另一方面

\[
400x^2y^3(x+2)^2
<\frac{2560000}{130321}.
\tag{5.6}
\]

结合 (3.3)、(5.2)、(5.5)：

\[
\boxed{
\bar\zeta_1
<-\frac{1223295069}{256000000}
<-4.778.
}
\tag{5.7}
\]

再由 (5.4)：

\[
\boxed{
\bar\zeta_2<\bar\zeta_1<-4.778.
}
\tag{5.8}
\]

---

## 6. 真实 third digit phase 与 modular roots 的巨大符号错位

实际 endpoint 中

\[
1<\zeta=\frac{a_3}{T}<\frac{251}{250}.
\]

因此

\[
\boxed{
0<\bar\zeta
=\frac{a_3}{T10^M}
<\frac{251}{250}\,10^{-M}.
}
\tag{6.1}
\]

而 `M>=11`，所以真实 `bar zeta` 是极小正数；与 (5.8) 的两个 modular sphere roots 相比：

\[
\boxed{
\bar\zeta-\bar\zeta_i>4.778
\qquad(i=1,2)
}
\tag{6.2}
\]

在实数轴上二者根本不接近。换句话说，generic spontaneous common-prime condition 只能靠真正的 `p`-adic wrapping 实现，绝不来自真实 third coordinate 接近某个 sphere root。

这与 `spontaneous-angle.md` 已得到的 `Omega_sp>0` / modular source root 位于负侧是同一类 Archimedean separation，但这里作用在**第三分子方向**，是第二个独立的真实坐标错位。

---

## 7. 当前证明边界

本文件严格完成：

1. `Omega_sp=0` 后 sphere discriminant 是完整平方；
2. 两个 third-numerator root 显式化；
3. `Q_1,Q_2` 精确识别为 `Theta` root 与两个 sphere root 的交点；
4. genuine endpoint 中两 root 严格排序且都 `<-4.778`；
5. 真实 `bar zeta` 为极小正数，因此存在统一的 `>4.778` Archimedean gap。

但 congruence `p | Q_i` 不要求实数接近，所以 (6.2) **本身不是矛盾**。下一步若要利用这条 sign gap，必须把 `p`-进深度与清分母后的自然整数代表大小联立；例如证明 odd-excess 所需的 `p^e` 超过对应正整数 numerator 的高度。单纯重复“root 为负、实际值为正”不能关闭 A2。

# A2 omega-content simple branch as an explicit biquadratic tower

> **依赖：** `spontaneous-omega-content-common.md`、`spontaneous-alpha-supported-resultant.md`。
>
> **严格状态：**`spontaneous-omega-content-common.md` 已证明 omega-content angle/additive common curve没有 surviving genuine singular Hensel tree。本文进一步把该 simple curve从两个隐式方程 `A_-=0,J=0` 改写为两层显式 quadratic tower：第一层 `r^2=R(x)` 给 content 的两个 numerator orientations；第二层 `u^2=L_±(x,r)` 给 additive decimal root。此前出现的 degree-8 `Q_omega(x)` 恰是 `L_+L_-` 的 quadratic norm，不是新的黑箱多项式。本文还证明两个 real content roots都严格避开真实 endpoint numerator window。本文不排除 p-adic wrapping，也不宣称 A2 closure。

---

## 1. content first layer

omega-content angle gate的 normalized polynomial为

\[
\boxed{
A_-(x,y)
=202500x^4-(101x^2+4x+4)y^2-1800x^2y.
}
\tag{1.1}

定义

\[
\boxed{P(x):=101x^2+4x+4,}
\tag{1.2}
\]

\[
\boxed{R(x):=101x^2+4x+8=P(x)+4.}
\tag{1.3}

将 (1.1) 改写为

\[
P(x)y^2+1800x^2y-202500x^4=0.
\tag{1.4}

其 `y`-discriminant为

\[
\boxed{
\operatorname{Disc}_y(A_-)
=(900x^2)^2R(x).
}
\tag{1.5}

因此 genuine `P x !=0` content root首先要求

\[
\boxed{r^2=R(x).}
\tag{1.6}

两个 `y` roots原本是

\[
y=
\frac{-1800x^2\pm900x^2r}{2P}.
\]

利用

\[
P=r^2-4=(r-2)(r+2),
\]
可完全约简为

\[
\boxed{
y_+=\frac{450x^2}{2+r},}
\tag{1.7+}
\]

\[
\boxed{
y_-=\frac{450x^2}{2-r}.}
\tag{1.7-}

所以 omega-content first layer并非任意 quadratic extension；它是单一平方根 `r=sqrt(R)` 的两个 Möbius orientations。

---

## 2. source-line collision就是 `r=0`

`spontaneous-alpha-supported-resultant.md` 已发现 content 与 height sheet collision 的共同 factor `R(x)`。

从 (1.6) 看得更直接：

\[
R=0
\iff r=0.
\]

此时两张 orientation合并：

\[
y_+=y_-=225x^2.
\]

即

\[
\boxed{R=0\Longrightarrow y=225x^2,}
\tag{2.1}

正是 source first-layer sheet `d=225x^2-y=0`。

所以此前所有 `R` collision的几何含义统一为：**omega-content 的两个 numerator orientations发生 branch collision，并退化到 source line。**

---

## 3. additive quadratic

omega-content additive gate使用

\[
\boxed{
\begin{aligned}
J(x,y,\tau)
={}&100x^2\left[5(y+9)^2-36(y+9)\tau+55\tau^2\right]\\
&-(x+2)^2(2025x^2+y^2).
\end{aligned}}
\tag{3.1}

其 `tau`-discriminant为

\[
\boxed{
\operatorname{Disc}_\tau J
=2000x^2D_\omega(x,y),
}
\tag{3.2}

其中

\[
\boxed{
\begin{aligned}
D_\omega={}&22275x^4+89100x^3
+991x^2y^2+17640x^2y\\
&+168480x^2+44xy^2+44y^2.
\end{aligned}}
\tag{3.3}

`spontaneous-omega-content-common.md` 通过 `Res_y(A_-,D_omega)` 得到过 degree-8 polynomial。下面解释它的真实结构。

---

## 4. 在 content sheet 上，第二层 discriminant只剩一个线性 quadratic-unit

先取 `y_+=450x^2/(2+r)`。在 quotient ring

\[
\mathbf Q(x)[r]/(r^2-R(x))
\]
中直接化简 (3.3)，得到

\[
\boxed{
D_\omega(x,y_+)
=
\frac{405x^2}{(r+2)^2}
L_+(x,r),
}
\tag{4.1}

其中

\[
\boxed{
L_+(x,r)=A_L(x)+rB_L(x),
}
\tag{4.2}

\[
\boxed{
A_L(x)
=501055x^4+44440x^3+104756x^2+4304x+4992,
}
\tag{4.3}

\[
\boxed{
B_L(x)=4(4955x^2+220x+416).
}
\tag{4.4}

因为

\[
2000\cdot405=810000=900^2,
\]
(3.2) 进一步变成

\[
\boxed{
\operatorname{Disc}_\tau J\big|_{y_+}
=
\left(\frac{900x^2}{r+2}\right)^2L_+(x,r).
}
\tag{4.5+}

对 conjugate orientation `r -> -r`：

\[
\boxed{
L_-(x,r)=A_L(x)-rB_L(x),
}
\tag{4.6}

\[
\boxed{
\operatorname{Disc}_\tau J\big|_{y_-}
=
\left(\frac{900x^2}{2-r}\right)^2L_-(x,r).
}
\tag{4.5-}

因此第二层 root condition只是

\[
\boxed{u^2=L_\pm.}
\tag{4.7}

omega-content common curve由两层 quadratic choice完全描述：

\[
\boxed{
r^2=R(x),\qquad u^2=L_\pm(x,r).}
\tag{4.8}

---

## 5. degree-8 `Q_omega` 正是 quadratic norm

两张 content sheet的 additive discriminant units互为 `r`-conjugate，所以

\[
\operatorname{Norm}(L_+)
=L_+L_-
=A_L^2-RB_L^2.
\]

直接展开：

\[
\boxed{
L_+L_-
=\mathcal Q_\omega(x),
}
\tag{5.1}

其中

\[
\boxed{
\begin{aligned}
\mathcal Q_\omega(x)={}&
251056113025x^8+44533768400x^7+67275876360x^6\\
&+8529261920x^5+6336428816x^4+503628928x^3\\
&+239152384x^2+8466432x+2768896.
\end{aligned}}
\tag{5.2}

这正是 `spontaneous-omega-content-common.md` 中

\[
\operatorname{Res}_y(A_-,D_\omega)
=164025x^4\mathcal Q_\omega(x)
\]
的 degree-8 factor。

所以 `Q_omega` 不是新的 independent obstruction；它只是第二层 discriminant在第一层 quadratic extension中的 norm。

这也解释了为什么只盯 `Q_omega` 的 Legendre character不会自动关闭 actual content branch：actual branch只要求对应的 `L_+` 或 `L_-` 为平方，而其 conjugate可以自由补偿 norm character。

---

## 6. explicit tau roots

由 (3.1)，quadratic formula给

\[
\boxed{
\tau
=
\frac{18(y+9)}{55}
\pm
\frac{\sqrt{\operatorname{Disc}_\tau J}}{11000x^2}.
}
\tag{6.1}

在 `y_+` sheet，若 `u^2=L_+`，则

\[
\boxed{
\tau
=
\frac{18(y_++9)}{55}
\pm
\frac{9u}{110(r+2)}.
}
\tag{6.2+}

同理 `y_-` sheet：

\[
\boxed{
\tau
=
\frac{18(y_-+9)}{55}
\pm
\frac{9u}{110(2-r)}.
}
\tag{6.2-}

因此 simple omega-content common prime最终只需要同步：

1. first-layer square root `r`；
2. second-layer square root `u`；
3. decimal orbit `tau=10^{-M}`。

不存在额外 source ratio或 hidden Hensel coordinate。

---

## 7. real endpoint separation：两张 content roots都不进入 actual numerator window

真实 denominator phase满足

\[
\frac1{10}<x<\frac2{19}.
\tag{7.1}

因此

\[
R(x)
>R(1/10)
=\frac{941}{100}.
\]

故 positive real square root满足

\[
\boxed{r>\frac{301}{100}>3.}
\tag{7.2}

于是 negative-orientation denominator

\[
2-r<0,
\]
所以

\[
\boxed{y_-<0.}
\tag{7.3}

对 positive orientation：

\[
y_+
=\frac{450x^2}{2+r}
<
\frac{450(2/19)^2}{2+301/100}.
\]

右端精确为

\[
\boxed{
\frac{60000}{60287}
<\frac{249}{250}.
}
\tag{7.4}

因此

\[
\boxed{
y_+<\frac{60000}{60287}<\frac{249}{250}.}
\tag{7.5}

而真实 endpoint要求

\[
\boxed{
\frac{249}{250}<y<1.
}
\tag{7.6}

所以两张 algebraic content roots都与真实 numerator window严格分离：

\[
\boxed{
 y_-<0,
\qquad
 y_+<0.99524,
\qquad
 y_{\rm actual}>0.996.
}
\tag{7.7}

这不是模素数矛盾；它说明任何 omega-content common state必须依赖真正的 p-adic wrapping，而不是实数附近的 root。

---

## 8. quadratic-character no-go

本文件把 content branch精确写成

\[
r^2=R,
\qquad
u^2=L_\pm.
\]

这并没有产生一个固定 quadratic nonresidue：`L_+L_-=Q_omega` 只是 conjugate norm。对 finite field中的一个 actual sheet，`L_+` 可以为平方而 `L_-` 取任意 compatible character；反之亦然。

因此下面这种路线应正式降级：

- 从 `Disc_y(A_-)` 取一次 Legendre symbol；
- 再从 `Disc_tau(J)` 取一次 Legendre symbol；
- 希望两者自动冲突。

完整 quadratic tower显示两层 character是独立 sheet choices，没有固定符号矛盾。真正剩余的约束是 decimal orbit / natural representative。

---

## 9. 更新后的 omega-content frontier

结合前一文件：

- full common curve没有 surviving singular Hensel tree；
- first layer是显式 `r^2=R`；
- second layer是显式 `u^2=L_±`；
- degree-8 eliminant只是 `Norm(L_±)`；
- 两个 real `y` roots都严格避开 endpoint numerator window。

所以 omega-content 已经是一个完全显式的 **simple biquadratic decimal-orbit problem**。

若后续继续这条支线，应直接研究

\[
\tau=10^{-M}
\]
与 (6.2±) 的离散同步，或为 modulus/source content建立足够强的 natural-representative bound；不应再做 generic discriminant/Legendre stacking。

A2 仍保持 open。
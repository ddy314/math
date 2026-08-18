# A2 conjugate-angle cross-sign sphere 的 quadratic gate

> **依赖：** `spontaneous-sign-companion-parity.md`、`spontaneous-sphere-roots.md`、`spontaneous-height-parity-ledger.md`。
>
> **严格状态：**actual angle sheet `O_+=0` 已知使 exact sphere关于 third numerator完全 split。本文研究相反的 angle sign companion `O_-=0`。结论是：conjugate-angle sphere不再 split over `Q(x,y)`，而恰好引入一个 quadratic extension `v^2=-2X_cross`；在真实 endpoint 上 `X_cross>56`，所以该 sphere没有任何 real third-numerator root。对 genuine `p=3 mod4`，cross-sign overlap必须满足 `(-2X_cross/p)=1`。同时在旧 height-2 orientation上该 character自动退化成 `-1` times a square，因此不能重复收费。本文不排除 generic p-adic cross-sign roots，也不宣称 A2 closure。

---

## 1. normalized exact sphere与 angle sign roots

沿用

\[
x=\frac{b_2}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}},
\qquad
s=9+y,
\]

\[
n:=\frac{2025x^2+y^2}{100}.
\]

第三块 normalized variables 为

\[
\bar w=\frac{b_3}{T10^M},
\qquad
\bar\zeta=\frac{a_3}{T10^M}.
\]

exact sphere：

\[
\boxed{
\mathscr S(\bar w,\bar\zeta)
=x^2\bar w^2(s+\bar\zeta)^2
-(x+2+\bar w)^2
\left(n\bar w^2+x^2\bar\zeta^2\right).
}
\tag{1.1}
\]

定义

\[
d:=225x^2-y,
\]

\[
A_{\rm sp}:=4d^2-xy^2(99x-4),
\]

以及正的 rational magnitude

\[
\boxed{
W:=\frac{A_{\rm sp}}{2y^2(x+2)}.
}
\tag{1.2}
\]

actual angle carrier `O_+=0` 给

\[
\bar w=-W,
\]

而 sign companion `O_-=0` 给

\[
\boxed{\bar w=+W.}
\tag{1.3}
\]

`spontaneous-sphere-roots.md` 已证明 `bar w=-W` 时 sphere discriminant是完整平方。本文处理 (1.3)。

---

## 2. conjugate-angle discriminant完全因子化

定义

\[
\boxed{
H:=202500x^4-99x^2y^2-1800x^2y+4xy^2+4y^2,
}
\tag{2.1}
\]

\[
\boxed{
H^\vee:=H+2y^2(x+2)^2
=202500x^4-97x^2y^2-1800x^2y+12xy^2+12y^2.
}
\tag{2.2}
\]

再定义新的 cross polynomial

\[
\boxed{
\begin{aligned}
X_\times:={}&205031250x^6+2025x^4y^2-1822500x^4y\\
&+8100x^3y^2-99x^2y^4-1800x^2y^3\\
&+4050x^2y^2+4xy^4+4y^4.
\end{aligned}}
\tag{2.3}
\]

把 `bar w=W` 代入 (1.1)，视为 `bar zeta` 的二次式。直接 exact discriminant calculation 给

\[
\boxed{
\operatorname{Disc}_{\bar\zeta}
\mathscr S(W,\bar\zeta)
=
-\frac{
 x^2H^2(H^\vee)^2X_\times
}{
200y^{10}(x+2)^4
}.
}
\tag{2.4}
\]

除了 `X_cross` 外其余 nontrivial factors全为平方。

因为

\[
200=2\cdot10^2,
\]
对 genuine odd prime `p` 且所有 displayed denominator / square factors为 unit：

\[
\left(
\frac{\operatorname{Disc}}p
\right)
=
\left(\frac{-2X_\times}{p}\right).
\tag{2.5}
\]

所以 sphere 在 `F_p` 中有 third-numerator root的必要条件为

\[
\boxed{
\left(\frac{-2X_\times}{p}\right)=1.
}
\tag{2.6}
\]

若 `p=3 mod4`，也可写成

\[
\boxed{
\left(\frac{2X_\times}{p}\right)=-1.
}
\tag{2.7}
\]

---

## 3. quadratic tower坐标

定义 quadratic coordinate

\[
\boxed{v^2=-2X_\times.}
\tag{3.1}
\]

则 (2.4) 的平方根可以无 radical denominator 地写成

\[
\sqrt{\operatorname{Disc}}
=
\frac{xHH^\vee}{20y^5(x+2)^2}v.
\tag{3.2}
\]

因此 conjugate-angle sphere 的两个 third-numerator orientations已经完全进入单一 quadratic extension

\[
\mathbf Q(x,y)(v),
\qquad v^2=-2X_\times.
\]

所以 cross pair `(O_-,Theta_-)` 或 `(O_-,Theta_+)` 并不存在新的隐藏高次 extension；第一层恰好只是 (3.1)。后续把 additive linear root代入，只会在这一 quadratic extension上产生关于 `tau` 的二次式，其 pure-prefix quartic只是 quadratic norm。

---

## 4. `已严格完成`：真实 endpoint 中 `X_cross>56`

endpoint box：

\[
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1.
\]

把 (2.3) 分成三个显然可控的正块：

\[
\begin{aligned}
X_\times={}&
 x^4\bigl(
205031250x^2-1822500y+2025y^2
\bigr)\\
&+x^2y^2\bigl(
8100x-99y^2-1800y+4050
\bigr)\\
&+4y^4(x+1).
\end{aligned}
\tag{4.1}
\]

第一括号对 `x` 递增、对 `y` 递减，所以

\[
205031250x^2-1822500y+2025y^2
>
\frac{459675}{2}.
\]

故第一块

\[
>\frac{459675}{20000}>22.
\tag{4.2}
\]

第二括号同样在 `x=1/10,y=1` 取得粗下界：

\[
8100x-99y^2-1800y+4050>2961.
\]

因此第二块

\[
>
\frac1{100}\left(\frac{249}{250}\right)^2 2961
>29.
\tag{4.3}
\]

第三块显然

\[
4y^4(x+1)
>
4\left(\frac{249}{250}\right)^4\frac{11}{10}
>4.
\tag{4.4}
\]

合并：

\[
\boxed{X_\times>22+29+4=55.}
\]

用 exact fractions稍微保留余量可得到

\[
\boxed{X_\times>56.}
\tag{4.5}
\]

因此真实 endpoint中 (2.4) 严格为负：

\[
\boxed{
\operatorname{Disc}_{\bar\zeta}\mathscr S(W,\bar\zeta)<0.
}
\tag{4.6}
\]

所以 conjugate-angle sheet根本没有 real third-numerator orientation；任何 cross-sign contact都必须是纯 modular / p-adic phenomenon。

---

## 5. height-2 上 quadratic character是自动 shadow

`spontaneous-height-parity-ledger.md` 的第二 height orientation为

\[
\boxed{
\begin{aligned}
H_2={}&410062500x^6-402975x^4y^2-7290000x^4y\\
&+8100x^3y^2+101x^2y^4+3600x^2y^3\\
&+40500x^2y^2+4xy^4+4y^4.
\end{aligned}}
\tag{5.1}
\]

直接展开有 exact syzygy：

\[
\boxed{
X_\times
=H_2
-50x^2\left(2025x^2-2y^2-27y\right)^2.
}
\tag{5.2}
\]

因此在 `H_2=0` 上：

\[
\boxed{
2X_\times
=-\left[
10x(2025x^2-2y^2-27y)
\right]^2.
}
\tag{5.3}
\]

对 genuine `p=3 mod4` 且右边线性 factor为 unit：

\[
\left(\frac{2X_\times}{p}\right)
=\left(\frac{-1}{p}\right)
=-1.
\]

这正好等于 (2.7) 所需的 cross-sign character。

所以：

\[
\boxed{
\text{在 height-2 sheet 上，cross-sign quadratic character 自动满足。}
}
\tag{5.4}
\]

它只是旧 height geometry 的 shadow，不能作为第二个独立 obstruction再次收费。

若 (5.3) 的 square factor也为零，则进入 discriminant-zero collision；那是单独的 singular/common-root问题，本文不把它自动判空。

---

## 6. 更新后的 cross-pair frontier

结合 `spontaneous-sign-companion-parity.md`：

- same-sign-pair common support已经被压到 prefix content / central / `a_3`；
- 最难的 cross pair `O_-` 与 additive sheets必须先穿过 quadratic gate `v^2=-2X_cross`；
- 该 quadratic gate在 real endpoint完全没有 root；
- 在 height-2 上它又退化为自动 square shadow。

因此下一步若继续 cross allocation，真正有新增信息的只剩：

1. generic `X_cross` quadratic sheet上的 decimal `tau` orbit；
2. height-1 orientation与 `X_cross` 的相对 character/depth；
3. `X_cross=0` 的 singular bad-reduction audit。

继续在 height-2 上叠加同一 Legendre condition不会增加约束。

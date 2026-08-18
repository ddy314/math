# A2 spontaneous prefix 的 `Delta_0=0` 降阶边界

> **依赖：** `spontaneous-prefix-eliminant.md`、`spontaneous-sphere-roots.md`、`spontaneous-prefix-branch-audit.md`。
>
> **严格状态：**此前为了把两个 sphere orientation 都写成有限有理函数，曾在 branch-collision 审计中单列 `p∤Delta_0`。本文直接处理 `Delta_0=0`：证明此时 `Omega_sp` 固定第三分母后，exact sphere 关于第三分子从二次式严格降为一次式，而且 genuine non-`3,5` prime 下线性系数绝不同时消失。因此只有一个有限第三分子 orientation；`Q_2` 在该边界上的额外清分母根是 projective/infinite-root artifact，不属于真实 third-coordinate branch。由此 generic pure-spontaneous 的“唯一 admissible branch”不再需要假设 `p∤Delta_0`。本文仍**不宣称 A2 全局关闭**。

---

## 1. 记号

沿用

\[
x=\frac{b_2}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}},
\]

\[
d=225x^2-y,
\qquad
A_{\rm sp}=4d^2-xy^2(99x-4),
\]

以及

\[
\boxed{
\Delta_0:=2025x^2-18y-y^2.
}
\tag{1.1}

`Omega_sp=0` 固定

\[
\bar w=-\frac{A_{\rm sp}}{2y^2(x+2)}.
\tag{1.2}

exact sphere 为

\[
x^2\bar w^2(9+y+\bar\zeta)^2
=(x+2+\bar w)^2
\left(
\frac{2025x^2+y^2}{100}\bar w^2+x^2\bar\zeta^2
\right).
\tag{1.3}

---

## 2. `已严格完成`：sphere 的最高次系数就是 `Delta_0`

把 (1.2) 代入 (1.3)，清去全部分母。关于 `bar zeta` 的 primitive numerator 写成

\[
\mathscr F_\zeta
=A_2\bar\zeta^2+A_1\bar\zeta+A_0.
\]

直接展开得到

\[
\boxed{
A_2
=160000x^4y^6(x+2)^4\Delta_0.
}
\tag{2.1}

所以

\[
\boxed{
\Delta_0=0
\Longrightarrow
\deg_{\bar\zeta}\mathscr F_\zeta\le1.
}
\tag{2.2}

这解释了 `spontaneous-sphere-roots.md` 中第二根

\[
\bar\zeta_2
=\frac{A_{\rm sp}G_*}
{400x^2y^3(x+2)^2\Delta_0}
\]
为什么在 `Delta_0=0` 上跑向 projective infinity；它不是一个仍应保留的有限第三分子值。

---

## 3. `已严格完成`：线性系数在 genuine 边界绝不消失

定义

\[
\boxed{
H_{\rm lin}
:=202500x^4-99x^2y^2-1800x^2y
+4xy^2+4y^2.
}
\tag{3.1}

同一展开给

\[
\boxed{
A_1
=800x^2y^4(x+2)^2(y+9)H_{\rm lin}^2.
}
\tag{3.2}

先控制 `y+9`。在 `Delta_0=0` 下

\[
2025x^2=y(y+18),
\]
所以 normalized base norm

\[
2025x^2+y^2=2y(y+9).
\tag{3.3}

对 genuine spontaneous prime，`p∤yN_0`，故

\[
\boxed{p\nmid y(y+9).}
\tag{3.4}

再对 `H_lin` 与 `Delta_0` 消去 `y`：

\[
\boxed{
\operatorname{Res}_y(H_{\rm lin},\Delta_0)
=4100625x^4(x+2)^4
=3^8 5^4x^4(x+2)^4.
}
\tag{3.5}

因此对 genuine

\[
p\ne3,5,
\qquad
p\nmid x(x+2),
\]
有

\[
\boxed{
\Delta_0\equiv0
\Longrightarrow
H_{\rm lin}\not\equiv0
\Longrightarrow
A_1\not\equiv0
\pmod p.
}
\tag{3.6}

结合 (2.2)：

\[
\boxed{
\Delta_0=0
\Longrightarrow
\mathscr F_\zeta\text{ 恰为一次式，且恰有一个有限根。}
}
\tag{3.7}

---

## 4. `已严格完成`：`Q_2` 的 `Delta_0` 根是清分母 artifact

`Q_1,Q_2` 是把 `Theta` root 与两个 projective sphere roots 比较后清分母所得。对 `Delta_0` 消去 `y` 时，`Q_2` 的 resultant 确实出现

\[
\boxed{
\begin{aligned}
\operatorname{Res}_y(\mathcal Q_2,\Delta_0)
={}&C\,x^{10}(x+2)^8(25x^2+1)\\
&\cdot(100x^2+4-\tau^2),
\end{aligned}}
\tag{4.1}

其中 `C` 只含 `2,3,5`。

在 `Delta_0=0` 下还有

\[
25x^2+1
=\frac{(y+9)^2}{81}.
\tag{4.2}

所以最后一因子等价于

\[
\tau^2=\frac{4(y+9)^2}{81},
\qquad
9\tau=\pm2(y+9).
\tag{4.3}

但 §3 已证明真实 sphere 此时只有**一个有限** `bar zeta` root；原来以 `1/Delta_0` 表示的第二 root 已位于无穷远。因此 (4.1)–(4.3) 只描述在统一清分母多项式里保留下来的 projective degeneration，不能当成第二个真实 third-coordinate branch 收费。

特别地，`9tau=2(y+9)` 确实重新命中旧 central line `2K-9=0`；负号对应 projective anti-central companion。二者都不恢复第二个有限 sphere orientation。

---

## 5. `已严格完成`：唯一 admissible branch 不再需要 `p∤Delta_0`

现在分两种情况：

### 5.1 `Delta_0` 为单位

`spontaneous-sphere-roots.md` 给两个有限 sphere roots。`spontaneous-prefix-branch-audit.md` 已证明在 pure-spontaneous noncentral channel：

- `A_-=0` 会落回 common-`alpha`；
- 两 branch 同时命中只可能命中 central `2K-9=0`（或 fixed coefficient prime `11`）。

所以非中心 pure branch 至多一个。

### 5.2 `Delta_0=0`

本文 §3 直接证明 sphere 只有一个有限 root，所以无论 `Q_2` 的 cleared polynomial 是否形式上为零，都只有一个 admissible third-coordinate orientation。

因此除 fixed coefficient prime `11` 与 central line 的单独审计外，可统一写成：

\[
\boxed{
\text{genuine pure-spontaneous, noncentral}
\Longrightarrow
\text{exactly one finite sphere orientation is admissible.}
}
\tag{5.1}

这里不再要求

\[
p\nmid\Delta_0.
\]

这修补了前一 branch-audit 中为了使用 `zeta_2` 有理式而保留的技术性边界。

---

## 6. 更新后的开放核

`Delta_0=0` 不产生新的 moving branch；它只是 sphere degree drop。于是 generic moving carrier 的规范分类现在是：

1. `Delta_0≠0`：两个 finite sphere orientations 中精确选择一个；
2. `Delta_0=0`：sphere 本身只有一个 finite orientation；
3. `A_-=0`：common-`alpha`，不属 pure spontaneous；
4. `2K-9=0`：central `C_*` 支，单列；
5. fixed coefficient prime `11`：仍需单列。

因此下一步对 generic moving prime 可以直接研究**唯一有限 orientation**的 compact quadratic / tangent，而无需再把 `Delta_pref` 零层视为额外 branch。

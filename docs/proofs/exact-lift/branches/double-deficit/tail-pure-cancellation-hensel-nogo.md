# DD baseline-free `Q`-cancellation Hensel 的 sphere-collapse no-go

> **依赖：** [`tail-pure-cancellation-three-sheet.md`](tail-pure-cancellation-three-sheet.md)、
> exact lift、unified gap definition与 sphere factorization。
>
> **严格状态：** `已严格完成（no-go audit）`。
>
> 前一文件把 baseline-free `p^c||Q` 的 unified quadratic压成 three-sheet Hensel
> partition。本文证明：其中看似最有希望的 deep unit-Hensel并不是独立 obstruction。
> 存在 exact identity
> \[
> \boxed{
> b_3(\kappa+2G)\mu
> -2\cdot10^mG^2C\nu
> =
> -10^mQG^2(\mathcal R+r_3)\nu,
> }
> \]
> 其中 DD coefficient `C=10^dA_12`。
> 因此所谓 Hensel depth精确等于 sphere complementary factor
> `R+r_3` 的已有深度。three-sheet ledger正确，但不能作为第二份独立高度收费。

---

## 1. DD coefficient `C` 就是前缀 numerator concat

统一 framework 在 DD 中定义

\[
C=10^{m_2+k_{12}}a_1+10^da_2.
\]

由于

\[
k_{12}=s_2+d,
\qquad
m_2+s_2=n_2,
\]

有

\[
m_2+k_{12}=n_2+d.
\]

所以

\[
\boxed{
C=10^d(a_1 10^{n_2}+a_2)
=10^dA_{12}.}
\tag{1.1}

因此

\[
\boxed{10^mC=10^{m+d}A_{12}=10^{n_3}A_{12}.}
\tag{1.2}

而完整 numerator concat为

\[
\boxed{\alpha=10^mC+a_3.}
\tag{1.3}

---

## 2. 先恢复一个 exact gap/concat identity

gap parameter定义

\[
\boxed{
\frac\mu\nu=G(\mathcal R-r_3).}
\tag{2.1}

乘 `b_3`：

\[
\frac{b_3\mu}{\nu}
=G(b_3\mathcal R-a_3).
\]

因此由 `(1.3)`：

\[
\begin{aligned}
\frac{b_3\mu}{\nu}-10^mGC
&=G(b_3\mathcal R-a_3-10^mC)\\
&=G(b_3\mathcal R-\alpha).
\end{aligned}
\]

exact lift给

\[
\mathcal R=\alpha/\beta,
\qquad
\beta=10^mQ+b_3.
\]

所以

\[
b_3\mathcal R-\alpha
=\alpha\left(\frac{b_3}{\beta}-1\right)
=-10^mQ\mathcal R.
\]

于是得到

\[
\boxed{
 b_3\mu-10^mGC\nu
=-10^mGQ\mathcal R\nu.
}
\tag{Gap-concat-parent}

---

## 3. `Unit-Hensel` parent精确等于 complementary sphere factor

考虑前一文件中出现的 linear combination

\[
\mathcal U
:=
 b_3(\kappa+2G)\mu
-2\cdot10^mG^2C\nu.
\]

展开第一项：

\[
\begin{aligned}
\mathcal U
&=b_3\kappa\mu
+2G(b_3\mu-10^mGC\nu).
\end{aligned}
\]

由 tail weight

\[
\boxed{b_3\kappa=10^mQG}
\tag{3.1}

以及 `(Gap-concat-parent)`：

\[
\begin{aligned}
\mathcal U
&=10^mQG\mu
-2\cdot10^mG^2Q\mathcal R\nu\\
&=10^mQG\nu
\left(\frac\mu\nu-2G\mathcal R\right).
\end{aligned}
\]

使用 `(2.1)`：

\[
\frac\mu\nu-2G\mathcal R
=G(\mathcal R-r_3)-2G\mathcal R
=-G(\mathcal R+r_3).
\]

故

\[
\boxed{
\mathcal U
=-10^mQG^2(\mathcal R+r_3)\nu.
}
\tag{Sphere-parent}

这是 exact rational identity；左边为整数，所以右边当然也是同一整数。

---

## 4. baseline-free prime 下 Hensel depth完全由 sphere 支付

回到

\[
p\nmid10b_1b_2b_3,
\qquad p^c\Vert Q,
\]

并沿用前一文件

\[
\rho=v_p(\mu)=v_p(G_0),
\qquad
v_p(\nu)=0,
\qquad
n=v_p(\mathcal N_{12})\ge\rho.
\]

因为 `p` 不整除 `G`，`(2.1)` 给

\[
\boxed{v_p(\mathcal R-r_3)=\rho.}
\tag{4.1}

sphere identity为

\[
(\mathcal R-r_3)(\mathcal R+r_3)
=r_1^2+r_2^2
=\frac{\mathcal N_{12}}{G^2}.
\]

所以

\[
\boxed{
v_p(\mathcal R+r_3)=n-\rho.}
\tag{4.2}

由 `(Sphere-parent)` 且 `nu,G` 为 units：

\[
\boxed{
v_p(\mathcal U)=c+n-\rho.}
\tag{4.3}

而前一文件 divided quadratic中的前两项有共同 `mu` factor；乘回 `mu`
后其和的 valuation为

\[
\rho+(c+n-\rho)=\boxed{c+n},
\]

正好等于第三项 forced valuation。

因此 three-sheet 中出现的 deep cancellation没有新增任何 `p`-adic height：

\[
\boxed{
\text{source }c
+\text{ complementary sphere depth }(n-\rho)
}
\]

已经精确解释全部 Hensel深度。

---

## 5. `rho=0` 的 unit-Hensel完全退化

尤其在最危险的

\[
\rho=0
\]

sheet：

\[
v_p(\mathcal R-r_3)=0,
\qquad
v_p(\mathcal R+r_3)=n.
\]

前一文件的

\[
Q_0(\kappa+2G)\mu
\equiv2G\kappa_0C\nu
\pmod{p^{c+n}}
\]

经 `kappa_0 b_3=10^mQ_0G` 清分母后，正是 `(Sphere-parent)` 模
`p^{c+n}` 的重写。

所以：

\[
\boxed{
\text{`Unit-Hensel` 不是独立 source carrier.}
}
\tag{Unit-Hensel-nogo}

不能把它与 sphere factorization再次相加收费。

---

## 6. 对 three-sheet 文件的正确定位

`tail-pure-cancellation-three-sheet.md` 的 valuation partition仍然严格正确：它准确描述
unified quadratic的 local tropical geometry。

但其用途应降级为：

- `AB/AD/BD` 是 sphere/gap depth在 quadratic 三项中的不同投影；
- 它们可以帮助 bookkeeping；
- **不能**被当作控制 primitive `Q` cancellation overflow `X_Q` 的第二份独立
Hensel obstruction。

因此 `X_Q` 的真正下一攻击必须来自 quadratic/sphere 之外的独立结构，例如：

1. full decimal concat / exact lift 的另一线性 carrier；
2. Gaussian orientation 不变量；
3. source cancellation prime的全局 product/parity；
4. 新的 Subspace/Ridout 输入。

---

## 7. 状态摘要

- **`已严格完成`**：`Gap-concat-parent`、`Sphere-parent`、valuation collapse。
- **`失效/降级`**：把 baseline-free `Unit-Hensel` 视为独立 obstruction或高度 payer。
- **`待证`**：真正独立的 `X_Q` source-cancellation control；post-tail global branch
reoptimization；DD absolute height / emptiness。

# DD `q-Z` gcd 的 projective / gap allocation

> **依赖：** [`high-funnel-qz-gcd-allocation.md`](high-funnel-qz-gcd-allocation.md)
> 与 `core.md` 的 stereographic projective denominator formula。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
> 本文继续消去上一文件中的临时 payer `R_3^{den}`：其 non-decimal
> prime-power 深度必须进一步进入 projective denominator `Z_0` 或 sphere-gap
> quotient `a`。因此 `gcd(q,Z)` 的全部 rough height最终只有三个 payer：
> `gamma`、`Z_0`、`a`。

---

## 1. 已有 denominator allocation

上一文件定义

\[
D_{qZ}=\gcd(q,Z),
\]

\[
R_3^{\rm den}
=
\frac{b_3}{\gcd(b_3,\operatorname{lcm}(b_1,b_2))},
\]

并严格证明

\[
\boxed{
D_{qZ}^2
\mid
\gamma(R_3^{\rm den})^2.
}
\tag{1.1}

同时若

\[
g_y:=\gcd(y_1,y_2),
\]

则

\[
\boxed{
\operatorname{core}_{10}(R_3^{\rm den})\mid g_y.
}
\tag{1.2}

由于 `D_qZ` 本身为 10-unit，后续只需处理 `(R_3^{den})` 的
non-decimal support。

---

## 2. projective denominator 的 exact local formula

把 ghost pair写成

\[
y_1=g_yX,
\qquad
y_2=g_yY,
\qquad
(X,Y)=1.
\]

令

\[
\omega_p:=v_p(X^2+Y^2),
\qquad
r_p:=v_p(g_y),
\]

并记 sphere gap

\[
H_{\rm sph}-y_3=La.
\]

最低项 stereographic denominator满足 `core.md` 的 exact valuation formula

\[
\boxed{
v_p(Z_0)
=
\max(0,r_p+\omega_p-\alpha_p),
}
\tag{2.1}

其中

\[
\alpha_p:=v_p(La).
\]

固定本文关心的 odd non-decimal prime `p`。因为 `L|10^m`，

\[
\boxed{v_p(L)=0,\qquad \alpha_p=v_p(a).}
\tag{2.2}

---

## 3. third-excess 必进 `Z_0` 或 `a`

固定

\[
p^c\Vert\operatorname{core}_{10}(R_3^{\rm den}).
\]

由上一文件的 ghost allocation：

\[
\boxed{r_p\ge c.}
\tag{3.1}

现在分 `(2.1)` 的两种情况。

若

\[
r_p+\omega_p\le v_p(a),
\]

则 `v_p(Z_0)=0`，但

\[
v_p(a)\ge r_p+\omega_p\ge c.
\]

若

\[
r_p+\omega_p>v_p(a),
\]

则

\[
\begin{aligned}
v_p(Z_0)+v_p(a)
&=r_p+\omega_p\\
&\ge r_p\\
&\ge c.
\end{aligned}
\]

所以无论哪种情况都有

\[
\boxed{
c\le v_p(Z_0)+v_p(a).}
\tag{3.2}

逐素数相乘：

\[
\boxed{
\operatorname{core}_{10}(R_3^{\rm den})\mid Z_0a.
}
\tag{R3-projective-pay}

这说明 third denominator unique-max excess并不是第四个独立 rough pool；
它已经被 projective/gap system完全吸收。

---

## 4. `q-Z` gcd 的三 payer theorem

`D_qZ` 为 10-unit，所以 `(1.1)` 中只有 `R_3^{den}` 的 non-decimal part
会参与 `D_qZ` 的 prime exponents。由 `(R3-projective-pay)`：

\[
\boxed{
D_{qZ}^2
\mid
\gamma Z_0^2a^2.
}
\tag{qZ-three-payer}

因此高度上

\[
\boxed{
\log D_{qZ}
\le
\frac12\log\gamma
+
\log Z_0
+
\log a.
}
\tag{4.1}

这个结论没有假设三者互素，也没有把同一 prime强行分给唯一 payer；
它是逐 prime exponent inequality 的精确全局乘积版本。

---

## 5. 回代 `L_Z|F_-`

上一文件已有

\[
L_Z=
\frac{2^{H+2}5^TZ}
{\gcd(2^{H+2}5^TZ,q)}
\mid F_-.
\]

因为 `Z` 为 10-unit：

\[
\gcd(2^{H+2}5^TZ,q)
\mid
2^{\mathfrak q}5^{q_5}D_{qZ}.
\]

结合 `(4.1)`，得到无需 `R_3^{den}` 的 height form：

\[
\boxed{
\begin{aligned}
\log_{10}F_-
\ge{}&aH+bT+\log_{10}Z\\
&-a\mathfrak q-bq_5
-\frac12\log_{10}\gamma\\
&-\log_{10}Z_0-\log_{10}a
+O(1).
\end{aligned}}
\tag{Projective-LZ-height}

所以 `q-Z` overlap 想吃掉 `Z`-divisor，只剩三种付款方式：

1. denominator overlap `gamma`；
2. stereographic projective denominator `Z_0`；
3. sphere-gap quotient `a`。

前者已经进入 `Subspace-defect`；后两者正是 carrier-circle / projective
allocation line中的 canonical variables。

---

## 6. 与 common/angular split 的关系

projective formula还给

\[
v_p(Z_0)=\max(0,r_p+\omega_p-v_p(a)).
\]

所以 `(qZ-three-payer)` 并没有把同一份 ghost depth重复收费：

- 当 gap depth `v_p(a)` 足够大时，`Z_0` 自动下降；
- 当 gap depth不足时，剩余 common/angle depth才进入 `Z_0`。

特别地，在 decimal prime `5` 的 angular branch中已有

\[
\omega_5>0
\Longrightarrow
v_5(U_{12}^{\rm prim})=0,
\]

而 `D_qZ` 本身不含 5。因此本文的 rough gcd allocation与已有
5-adic angular/bottom exclusion是互补而非重复的。

---

## 7. 当前边界

- **`已严格完成`**：`R3-projective-pay`、`qZ-three-payer`、
  `Projective-LZ-height`。
- **`结构压缩`**：`gcd(q,Z)` 不再需要独立 gcd-smallness 假设；其高度
  被完全归入 `gamma / Z_0 / a`。
- **`待证`**：证明 `Z_0` 与 `a` 的正线性高度不能同时支付
  `(Projective-LZ-height)` 所需 loss；最自然接口是无 `E_D` carrier-circle
  eliminant与 primitive determinant ladder。

# A2 moving height equal-depth 的 same-sign companion shadow

> **依赖：** `spontaneous-height-equal-depth-source-orientation.md`、`spontaneous-sign-companion-parity.md`。
>
> **严格状态：**本文检查同号 companions `O_-`、`Theta_+` 是否能为 moving-height equal-depth shell 提供独立 quadratic character。结论：在 generic noncentral height prime 上，它们与两个 sign-product 的 character 精确合并回既有
> \[
> \chi\!\left((\Theta_-/p^e)/(\mathcal O_+/p^e)\right)=\chi(-\rho).
> \]
> 因此 same-sign companion Legendre calculation 没有新增局部约束。

## 1. companion first layer

固定
\[
p^h\Vert W_q,\qquad e<h,\qquad p\equiv3\pmod4,
\]
并假设
\[
v_p(\mathcal O_+)=v_p(\Theta_-)=e,
\qquad p\nmid K(2K-9)ABQb_3Tc_uz.
\]

由
\[
\mathcal O_+-\mathcal O_-=4A^2Qb_3
\]
与 `p|O_+`：
\[
\boxed{\mathcal O_-\equiv-4A^2Qb_3\pmod p.}
\tag{1.1}
\]

又
\[
\Theta_+-\Theta_-=4B^2(2K-9)a_3,
\]
而 height prime 上 `a_3=-TK mod p`，故
\[
\boxed{\Theta_+\equiv-4TB^2K(2K-9)\pmod p.}
\tag{1.2}
\]

使用 `b_3z=Tc_uQ` 与 `rho=z/c_u`：
\[
\boxed{
\left(\frac{\Theta_+/\mathcal O_-}{p}\right)
=
\left(\frac{K(2K-9)/\rho}{p}\right).}
\tag{1.3}
\]

## 2. sign-product character

height product bridge给
\[
T^2\mathcal H_O\equiv N_0\mathcal O_+\mathcal O_-\pmod{W_q}.
\]
所以在 `e<h`
\[
\frac{\mathcal O_+\mathcal O_-}{p^e}
\equiv
\frac{T^2}{N_0}\frac{\mathcal H_O}{p^e}\pmod p.
\tag{2.1}
\]

另一方面 `alpha=TK+a_3` 有深度至少 `h`，从 additive pair 得
\[
\frac{\Theta_-\Theta_+}{p^e}
\equiv
-4T^2B^2K(2K-9)\frac{\mathcal J_H}{p^e}\pmod p.
\tag{2.2}
\]

height square给 `(N_0/p)=-1`。在 equal-depth extra shell，`J_H/B_W` 只差 square，而 universal norm bridge要求
\[
\left(
\frac{(\mathscr B_W/p^e)/(\mathcal H_O/p^e)}p
\right)=-1.
\]
因此
\[
\boxed{
\left(
\frac{(\Theta_-\Theta_+/p^e)/(\mathcal O_+\mathcal O_-/p^e)}p
\right)
=-\left(\frac{K(2K-9)}p\right).}
\tag{2.3}
\]

## 3. companion calculation is the same law

分解 sign-product ratio：
\[
\frac{\Theta_-\Theta_+}{\mathcal O_+\mathcal O_-}
=
\frac{\Theta_-}{\mathcal O_+}
\frac{\Theta_+}{\mathcal O_-}.
\]
结合 (1.3)、(2.3)：
\[
\boxed{
\left(
\frac{(\Theta_-/p^e)/(\mathcal O_+/p^e)}p
\right)
=-\left(\frac\rho p\right)
=\left(\frac{-\rho}p\right).}
\tag{3.1}
\]

这与 `spontaneous-height-equal-depth-source-orientation.md` 完全相同。

故在 generic noncentral moving-height shell，同号 companion character 只是既有 source-orientation law 的代数投影。继续处理时应转向 cross-sign sphere、`p|(2K-9)` 的显式例外，或 global `W_q=alpha/omega` representative。
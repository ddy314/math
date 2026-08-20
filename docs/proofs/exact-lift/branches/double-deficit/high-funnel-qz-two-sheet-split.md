# DD high-funnel 的 `q-Z` excess two-sheet split

> **依赖：** [`high-funnel-qz-gcd-allocation.md`](high-funnel-qz-gcd-allocation.md)、
> [`high-funnel-qz-projective-allocation.md`](high-funnel-qz-projective-allocation.md)、
> `core.md` 的 `t_2=1` S-unit phase、integer sphere / exact lift、nested carry、
> Plücker 关系与 projective denominator 公式。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
>
> 本文处理 `D_{qZ}=gcd(q,Z)` 中没有被 denominator-overlap `gamma` 的
> square-root baseline 支付的部分。结论不是“该 excess 自动进入两条独立
> carrier residual”；恰恰相反，它有一个精确 two-sheet split：
>
> - **gap sheet**：excess 进入 sphere gap 与 decimal determinant `E`，而
>   bottom carrier 没有 excess；
> - **complementary sheet**：`E` 只有 baseline，而 bottom carrier获得全部
>   excess，并且同一 prime 同时进入 projective denominator `Z_0`。
>
> 作为全局推论，旧 payer bound
> \[
> D_{qZ}^2\mid \gamma Z_0^2a^2
> \]
> 可严格加强为
> \[
> \boxed{D_{qZ}^2\mid \gamma a Z_0^2.}
> \]

---

## 1. canonical excess modulus

在 `t_2=1` funnel 中：

\[
\kappa=\gamma u,\qquad G=\gamma V,
\qquad u=2\cdot5^TU,
\qquad Q=Uq,
\]

\[
2^HZ=5^TU+V,
\qquad (UVZ,10)=1,
\qquad (U,V)=1.
\]

沿用

\[
D_{qZ}:=(q,Z).
\]

因为 `Z` 是 10-unit，`D_{qZ}` 也只含 `p\nmid10` 的素数。

定义 `gamma` 的 non-decimal square-root part

\[
\boxed{
\Gamma_{1/2}
:=\prod_{p\nmid10}p^{\lfloor v_p(\gamma)/2\rfloor}.
}
\tag{1.1}

于是

\[
\Gamma_{1/2}^2\mid\gamma.
\]

把 `q-Z` gcd 分成

\[
\boxed{
D_{\rm base}:=(D_{qZ},\Gamma_{1/2}),
\qquad
D_{\rm ex}:=D_{qZ}/D_{\rm base}.
}
\tag{1.2}

`D_base` 是可以直接由 `gamma` 的平方深度支付的部分；真正需要继续追踪的
是 `D_ex`。

---

## 2. `D_ex` prime 必然是第三分母 unique-max

固定

\[
p^e\Vert D_{\rm ex},\qquad e>0.
\]

写

\[
r:=v_p(q)=v_p(Q),
\qquad z:=v_p(Z),
\qquad d_p:=v_p(D_{qZ})=\min(r,z),
\]

以及 denominator valuations

\[
e_i:=v_p(b_i).
\]

`high-funnel-qz-gcd-allocation.md` 已证明：

\[
p\nmid UV,
\qquad e_3=r,
\qquad v_p(\gamma)=e_1+e_2.
\tag{2.1}

若 `e_1\ne e_2`，二项赋值给

\[
r=\min(e_1,e_2),
\]

从而

\[
\left\lfloor\frac{v_p(\gamma)}2\right\rfloor
\ge r\ge d_p,
\]

与 `e>0` 矛盾。

因此必有

\[
\boxed{e_1=e_2=:M.}
\tag{2.2}

此时

\[
v_p(\gamma)=2M.
\]

如果 `r=M`，仍有 `d_p<=M`，不会进入 `D_ex`。故必有

\[
\boxed{r=M+c,\qquad c>0.}
\tag{2.3}

并且

\[
\boxed{e=d_p-M>0,\qquad e\le c,\qquad z\ge M+e.}
\tag{2.4}

所以每个 `D_ex` prime 都具有唯一 denominator pattern

\[
\boxed{e_1=e_2=M<e_3=M+c.}
\tag{Third-exclusive}

---

## 3. 两条 denominator Hensel relations

写

\[
b_1=p^MB_1,\qquad
b_2=p^MB_2,\qquad
b_3=p^{M+c}B_3,
\]

\[
Q=p^{M+c}Q_0,
\]

其中 `B_1,B_2,B_3,Q_0` 都是 `p`-units。

由

\[
Q=b_1 10^{m_2}+b_2
\]

得到 prefix cancellation

\[
\boxed{
B_1 10^{m_2}+B_2=p^cQ_0.
}
\tag{3.1}

另一方面

\[
\kappa+2G
=G\frac{10^mQ+2b_3}{b_3}.
\]

而 S-unit phase 给

\[
v_p(\kappa+2G)
=v_p(\gamma)+v_p(Z)
=2M+z.
\]

所以

\[
\boxed{
v_p(10^mQ+2b_3)=M+c+z=r+z.}
\tag{3.2}

除去 `p^r`：

\[
\boxed{
10^mQ_0+2B_3\equiv0\pmod{p^z}.}
\tag{Tail-sign}

令完整 denominator concat

\[
\beta=10^mQ+b_3
=p^r\beta_0,
\qquad
\beta_0:=10^mQ_0+B_3.
\]

由 `(Tail-sign)`：

\[
\boxed{
\beta_0\equiv-B_3\pmod{p^z},
\qquad p\nmid\beta_0.}
\tag{3.3}

---

## 4. sphere 强迫唯一的两条 sign sheets

记整数球面半径为 `H_sph`，避免与 S-unit exponent `H` 混淆。

由于第三分母在 `p` 处唯一最大，lcm denominator 的 `p`-depth为 `r`。
于是

\[
p^c\mid y_1,y_2,
\qquad p\nmid y_3.
\]

sphere equation

\[
H_{\rm sph}^2-y_3^2=y_1^2+y_2^2
\]

说明 `H_sph` 也是 `p`-unit，并且

\[
v_p(y_1^2+y_2^2)\ge2c.
\]

因为 `p` 为奇素数且 `y_3` 为 unit，

\[
(H_{\rm sph}-y_3,\ H_{\rm sph}+y_3)
\]

不可能同时被 `p` 整除。因此恰有一条深：

\[
\boxed{
\begin{array}{ll}
\text{gap sheet:}&
 v_p(H_{\rm sph}-y_3)\ge2c,
 \quad v_p(H_{\rm sph}+y_3)=0,\\[1mm]
\text{complementary sheet:}&
 v_p(H_{\rm sph}+y_3)\ge2c,
 \quad v_p(H_{\rm sph}-y_3)=0.
\end{array}}
\tag{Sphere-sheets}

现在令完整 numerator concat

\[
\alpha=A_{12}10^{n_3}+a_3,
\qquad n_3=m+d.
\]

写 lcm denominator 为

\[
q_{\rm lcm}=p^rq_0,
\qquad p\nmid q_0.
\]

exact lift 与第三 ghost coordinate给

\[
q_0\alpha=H_{\rm sph}\beta_0,
\qquad
y_3=a_3\frac{q_0}{B_3}.
\]

所以

\[
\frac{H_{\rm sph}}{y_3}
=\frac{\alpha B_3}{a_3\beta_0}
\equiv-\frac\alpha{a_3}
\pmod{p^z}.
\tag{4.1}

由 `(2.4)` 有 `e<=c` 且 `z>=e`。结合 `(Sphere-sheets)`：

### gap sheet

\[
H_{\rm sph}/y_3\equiv1\pmod{p^e},
\]

故

\[
\boxed{
p^e\mid\alpha+a_3
=A_{12}10^{n_3}+2a_3.}
\tag{Gap-num}

### complementary sheet

\[
H_{\rm sph}/y_3\equiv-1\pmod{p^e},
\]

故

\[
\boxed{
p^e\mid\alpha-a_3=A_{12}10^{n_3}.}
\]

因为 `p\nmid10`：

\[
\boxed{p^e\mid A_{12}.}
\tag{Comp-num}

这就是 `q-Z` excess 的 numerator two-sheet selector。

---

## 5. gap sheet：`E` 深、bottom carrier 恰为 baseline

DD decimal determinant为

\[
\boxed{E=b_3A_{12}10^d-a_3Q.}
\tag{5.1}

由 `(Gap-num)` 与 `n_3=m+d`：

\[
A_{12}10^d
\equiv-2a_3 10^{-m}
\pmod{p^e}.
\tag{5.2}

由 `(Tail-sign)`：

\[
Q_0\equiv-2B_3 10^{-m}\pmod{p^e}.
\tag{5.3}

代入 `(5.1)`：

\[
\boxed{v_p(E)\ge r+e.}
\tag{Gap-E}

下面证明 bottom carrier没有获得同一 excess。

定义三个 raw carrier determinants：

\[
\Delta_{12}
=a_1 10^k b_2-a_2 10^d b_1,
\]

\[
\Delta_{13}
=a_1 10^k b_3-a_3b_1,
\qquad
\Delta_{23}
=a_2 10^d b_3-a_3b_2,
\]

其中

\[
k=s_2+d,
\qquad n_2=m_2+s_2.
\]

由于 `r>M` 且 `p\mid b_3` 强迫 `p\nmid a_3`：

\[
\boxed{v_p(\Delta_{13})=v_p(\Delta_{23})=M.}
\tag{5.4}

写

\[
\Delta_{13}=p^MD_{13},
\qquad
\Delta_{23}=p^MD_{23},
\]

其中 `D_13,D_23` 为 units。

nested carry 是 exact identity

\[
\boxed{E=10^{m_2}\Delta_{13}+\Delta_{23}.}
\tag{5.5}

由 `(Gap-E)`：

\[
10^{m_2}D_{13}+D_{23}=p^{c+e}W_p
\tag{5.6}

对某个整数 `W_p`。

同时 Plücker 关系

\[
b_1\Delta_{23}-b_2\Delta_{13}+b_3\Delta_{12}=0
\]

除去 `p^{2M}`，并使用 `(3.1)` 与 `(5.6)`，得到

\[
B_3\frac{\Delta_{12}}{p^M}
=Q_0D_{13}-p^eB_1W_p.
\tag{5.7}

右边模 `p` 等于 unit `Q_0D_13`，故

\[
\boxed{v_p(\Delta_{12})=M.}
\tag{Gap-bottom-baseline}

令

\[
d_{12}:=(b_1,b_2),
\qquad
\Theta_{12}:=\Delta_{12}/d_{12}.
\]

因为当前 `v_p(d_12)=M`：

\[
\boxed{v_p(\Theta_{12})=0.}
\tag{Gap-Theta-unit}

所以 gap sheet 的 excess只进入 `E`，不会再次进入 bottom carrier。

---

## 6. complementary sheet：`E` 恰为 baseline、bottom carrier变深

由 `(Comp-num)`：

\[
p^e\mid A_{12},
\qquad e>0.
\]

在 `(5.1)` 除去 `p^r` 后，第一项仍被 `p` 整除，而
`a_3Q_0` 是 unit。因此

\[
\boxed{v_p(E)=r.}
\tag{Comp-E-baseline}

另一方面有 exact bottom identity

\[
\boxed{
\frac{\Delta_{12}}{10^d}
=Qa_1 10^{s_2}-b_1A_{12}.}
\tag{6.1}

第一项的 `p`-depth至少为 `r>=M+e`，第二项至少为 `M+e`，所以

\[
\boxed{v_p(\Delta_{12})\ge M+e.}
\]

即

\[
\boxed{v_p(\Theta_{12})\ge e.}
\tag{Comp-bottom-excess}

因此 complementary sheet 与 gap sheet恰好相反：bottom carrier获得全部
`D_ex` depth，而 `E` 没有任何 excess。

---

## 7. canonical integer sheet selectors

定义 normalized decimal-determinant excess reader

\[
\boxed{
E_{\rm exc}
:=\frac{E}{(E,Q)}.}
\tag{7.1}

对每个 `p^e||D_ex`：

\[
\boxed{
\begin{array}{c|cc}
&v_p(E_{\rm exc})&v_p(\Theta_{12})\\ \hline
\text{gap sheet}&\ge e&0\\
\text{complementary sheet}&0&\ge e
\end{array}}
\tag{7.2}

于是可完全整数化地定义

\[
\boxed{
D_{\rm gap}:=(D_{\rm ex},E_{\rm exc}),
\qquad
D_{\rm comp}:=D_{\rm ex}/D_{\rm gap}.}
\tag{7.3}

逐素数由 `(7.2)` 得

\[
\boxed{(D_{\rm gap},D_{\rm comp})=1,}
\tag{7.4}

\[
\boxed{D_{\rm gap}\mid E_{\rm exc},}
\tag{7.5}

\[
\boxed{D_{\rm comp}\mid\Theta_{12},}
\tag{7.6}

以及 no-double-contact：

\[
\boxed{(D_{\rm ex},E_{\rm exc},\Theta_{12})=1.}
\tag{7.7}

特别地

\[
\boxed{D_{\rm ex}\mid E_{\rm exc}\Theta_{12}}
\tag{Two-sheet-product}

但 `D_ex` 的同一个 prime不可能同时由这两个 carrier reader支付。

这正式说明：从 `p|q,Z` 直接跳到“两条独立 carrier residual 同时深”是错误路线。

---

## 8. sphere/projective payer也随 sheet 锁定

### gap sheet

这里

\[
v_p(H_{\rm sph}-y_3)\ge2c.
\]

对 `p\nmid10`，tail quotient `L` 没有 `p`-part，而

\[
H_{\rm sph}-y_3=La.
\]

所以

\[
v_p(a)\ge2c\ge2e.
\]

因此

\[
\boxed{D_{\rm gap}^2\mid a.}
\tag{Gap-a-pay}

### complementary sheet

令

\[
g_y:=(y_1,y_2),
\qquad \rho:=v_p(g_y)\ge c.
\]

写 primitive sum depth

\[
v_p(y_1^2+y_2^2)=2\rho+\omega_p.
\]

complementary sheet中全部深度进入 `H_sph+y_3`，故

\[
v_p(H_{\rm sph}+y_3)=2\rho+\omega_p.
\]

projective denominator已有 exact formula

\[
Z_0=\frac{H_{\rm sph}+y_3}{(g_y,H_{\rm sph}+y_3)}.
\]

所以

\[
v_p(Z_0)=\rho+\omega_p\ge c\ge e.
\]

因此

\[
\boxed{D_{\rm comp}\mid Z_0.}
\tag{Comp-Z0-pay}

---

## 9. `q-Z` payer theorem 的严格加强

由定义

\[
D_{qZ}=D_{\rm base}D_{\rm ex}
=D_{\rm base}D_{\rm gap}D_{\rm comp}.
\]

又

\[
D_{\rm base}^2\mid\Gamma_{1/2}^2\mid\gamma,
\]

并由 `(Gap-a-pay)`、`(Comp-Z0-pay)`：

\[
D_{\rm gap}^2D_{\rm comp}^2
\mid aZ_0^2.
\]

逐素数相加 exponent 得到

\[
\boxed{
D_{qZ}^{\,2}\mid\gamma\,a\,Z_0^2.}
\tag{qZ-three-payer-sharp}

因此高度形式严格加强为

\[
\boxed{
\log_{10}D_{qZ}
\le
\frac12\log_{10}\gamma
+\frac12\log_{10}a
+\log_{10}Z_0.}
\tag{9.1}

相比旧 `gamma Z_0^2 a^2`，sphere-gap payer 的 coefficient 从 `1` 降为
`1/2`。

---

## 10. sharpened `L_Z` height

`high-funnel-qz-gcd-allocation.md` 已有

\[
L_Z=
\frac{2^{H+2}5^TZ}
{(2^{H+2}5^TZ,q)}
\mid F_-.
\]

记

\[
a_2:=\log_{10}2,
\qquad a_5:=\log_{10}5.
\]

因为 `Z` 为 10-unit：

\[
\log_{10}(2^{H+2}5^TZ,q)
\le
a_2\mathfrak q+a_5q_5+\log_{10}D_{qZ}+O(1).
\]

使用 `(9.1)`：

\[
\boxed{
\begin{aligned}
\log_{10}F_-
\ge{}&a_2H+a_5T+\log_{10}Z
-a_2\mathfrak q-a_5q_5\\
&-\frac12\log_{10}\gamma
-\frac12\log_{10}a
-\log_{10}Z_0
+O(1).
\end{aligned}}
\tag{LZ-height-sharp}

所以未来的 global height optimization 不再需要把 `q-Z` gcd作为一个未知
loss；它只剩三个明确 payer，而且 sphere-gap payer已经按真实 square depth只收费
半份。

---

## 11. 当前边界

本文同时给出一个正面结构结论和一个重要 no-go：

1. **正面：** `q-Z` excess 被 canonical 地分成 `gap / complementary` 两个
   Hensel sheets，并得到 sharpened three-payer theorem
   \[
   D_{qZ}^2\mid\gamma aZ_0^2.
   \]
2. **no-go：** `q-Z` excess **不会**自动制造两条独立 carrier residual 的共同
   深度；在同一 prime上，`E_exc` 与 `Theta_12` 两个 reader严格互斥。

因此下一步不能无条件套 `core.md` §56 的 two-residual circle eliminant。真正应分别攻击：

- `gap sheet`：`D_gap^2|a` 与 primitive determinant ladder / `E_exc` 的兼容；
- `complementary sheet`：`D_comp|Z_0` 且 `D_comp|Theta_12` 的 projective-bottom
  simultaneous contact。

DD 全局仍为 `待证`。
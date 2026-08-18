# A2 spontaneous angle primitive carrier 的 source-content 分离

> **依赖：** `spontaneous-angle-parity.md`、`source-discriminant.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文证明 `spontaneous-angle-parity.md` 的 primitive positive `3 mod 4` integer `widehat(O)_sp` 不能从 source content `c_u g` 中获得任何 non-`5` odd prime，特别不能从那里获得 `3 mod 4` inert parity。这个结论与已有 `gcd(widehat(T)_2,10c_ug)=1` 平行。本文并不排除 denominator/source-excess/spontaneous primes，也不宣称 A2 全局关闭。

---

## 1. primitive angle integer

沿用

\[
\widehat{\mathcal O}_{\rm sp}
=5^m\mathcal U_\Omega^\sharp
+2A^2Q_0b_{30},
\tag{1.1}
\]
其中

\[
A=a_2,
\qquad
b_0=c_ug,
\qquad
b_{30}=5^dc_Qc_u,
\tag{1.2}
\]

\[
Q_0=c_Qq=5^M+2^mgc_u,
\tag{1.3}
\]
以及

\[
\begin{aligned}
\mathcal U_\Omega^\sharp
={}&\left(45\,2^{M+2m+1}b_0^2-A5^M\right)^2\\
&-A^2 2^{m+1}b_0
\left(99\,2^{m-1}b_0-5^M\right).
\end{aligned}
\tag{1.4}
\]

已有

\[
\widehat{\mathcal O}_{\rm sp}>0,
\qquad
\widehat{\mathcal O}_{\rm sp}\equiv3\pmod4.
\tag{1.5}
\]

---

## 2. `已严格完成`：任何 odd prime `p|c_u`, `p!=5` 都不能整除 angle carrier

设

\[
p\mid c_u,
\qquad p\ne2,5.
\]

则 `b_0` 与 `b_30` 都被 `p` 整除。因此 (1.4) 给

\[
\mathcal U_\Omega^\sharp
\equiv A^25^{2M}\pmod p,
\]
而 (1.1) 的第二项为零：

\[
\boxed{
\widehat{\mathcal O}_{\rm sp}
\equiv A^25^{2M+m}\pmod p.
}
\tag{2.1}
\]

因为 `c_u|B=b_2` 且 `(A,B)=1`，故 `p∤A`；又 `p!=5`。于是右边为单位：

\[
\boxed{
p\mid c_u,\ p\ne2,5
\Longrightarrow
p\nmid\widehat{\mathcal O}_{\rm sp}.}
\tag{2.2}
\]

特别地任意 `3 mod 4` prime 都满足 `p!=5`，所以 angle side 的 inert parity 绝不来自 `c_u`。

---

## 3. `已严格完成`：任何 odd `p|g`, `p!=5` 也不能整除 angle carrier

设

\[
p\mid g,
\qquad p\ne2,5.
\]

则

\[
b_0=c_ug\equiv0\pmod p,
\]
所以仍有

\[
\mathcal U_\Omega^\sharp
\equiv A^25^{2M}\pmod p.
\tag{3.1}
\]

由 (1.3)：

\[
Q_0\equiv5^M\pmod p.
\tag{3.2}
\]

代入 (1.1)：

\[
\begin{aligned}
\widehat{\mathcal O}_{\rm sp}
&\equiv
A^25^{2M+m}
+2A^25^M5^dc_Qc_u\\
&=A^25^{M+d}
\left(5^{M+m-d}+2c_Qc_u\right).
\end{aligned}
\]

记

\[
\lambda=m-d.
\]
旧 source relation 为

\[
5^{M+\lambda}+c_Qc_u=g\theta.
\tag{3.3}
\]

所以模 `p|g`：

\[
5^{M+m-d}+2c_Qc_u
=5^{M+\lambda}+2c_Qc_u
\equiv c_Qc_u.
\]
因此

\[
\boxed{
\widehat{\mathcal O}_{\rm sp}
\equiv A^25^{M+d}c_Qc_u
\pmod p.}
\tag{3.4}
\]

对于 odd prime `p|g`：

- `(A,B)=1` 且 `g|B`，故 `p∤A`；
- `gcd(c_u,g)=1`，故 `p∤c_u`；
- `g=2^{t-1}\rho` 且旧本原性 `gcd(c_Q,\rho)=1`，故 odd `p|g` 时 `p∤c_Q`；
- 本节假设 `p!=5`。

故 (3.4) 为单位：

\[
\boxed{
p\mid g,\ p\ne2,5
\Longrightarrow
p\nmid\widehat{\mathcal O}_{\rm sp}.}
\tag{3.5}
\]

---

## 4. inert source-content exclusion

综合 §§2–3，任意 odd inert prime

\[
p\equiv3\pmod4
\]
自动满足 `p!=5`，所以

\[
\boxed{
p\mid c_ug,
\quad p\equiv3\pmod4
\Longrightarrow
p\nmid\widehat{\mathcal O}_{\rm sp}.}
\tag{4.1}
\]

也就是说 `widehat(O)_sp≡3 mod4` 所强迫的 odd inert parity 必须来自 `c_ug` 之外。

已有 additive side 更强的

\[
\boxed{
\gcd(\widehat{\mathcal T}_2,10c_ug)=1.
}
\tag{4.2}
\]

所以两侧 parity carrier 在 source content 上完全对齐：

\[
\boxed{
\begin{array}{c|c}
\text{primitive object}&\text{non-5 odd source-content primes}\\ \hline
\widehat{\mathcal O}_{\rm sp}&\text{none from }c_ug\\
\widehat{\mathcal T}_2&\text{none from }c_ug
\end{array}}
\tag{4.3}
\]

---

## 5. 与 prime-source 图的意义

这一步不能单独强迫

\[
G_{\rm sp}
=\gcd(\widehat{\mathcal O}_{\rm sp},\widehat{\mathcal T}_2)
\equiv3\pmod4.
\]

如果 `G_sp≡1 mod4`，两侧 residual quotient 仍可能各自携带不同 inert prime。但 (4.3) 已经排除了最廉价的一整类解释：这些 residual inert primes 不可能只是 source content `c_u` 或 `g` 的旧因子。

因此 residual parity 现在必须进入真正的 prime-source geometry：

- q/f denominator contact；
- source excess (`Phi_s / D_src`)；
- 或 pure spontaneous contact。

下一步应该把 `Omega_sp` 与 q/f/source 三条 overlap resultant 的 valuation parity，和 additive side 已有 saturation/height 分类逐类对齐；若 residual denominator/source contribution 都能证明为偶 parity，就会强迫 `G_sp≡3 mod4`。

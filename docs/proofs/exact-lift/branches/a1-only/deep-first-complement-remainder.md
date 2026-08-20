# A1 minimal diagonal: universal first complement remainder

> 日期：2026-08-20。依赖 `deep-complement-height.md`。当前统一范围 `k=g>=31`。

本文保留 complement identity 的第一层十进制余数。这个对象对 single / double deep 都成立，并给出一个只有 `O(lambda*T)` 大小、但必须承载原 `MDN_0` 的局部深赋值的整数。

状态：**已严格完成。**

---

## 1. 定义 first remainder

沿用

\[
T=10^k,
\qquad
D=2^A5^B,
\qquad
DTN_0-\gamma=h\lambda,
\]

\[
M:=\frac{Qb_1}{h},
\qquad
\lambda=2^{\lambda_2}5^{\lambda_5}.
\]

又

\[
Qb_1=1000T^4+c_2T^2+C_0,
\]

其中

\[
c_2=10(1-20w),
\qquad
C_0=w(10w-1).
\]

乘以 `M`：

\[
M(DTN_0-\gamma)=\lambda Qb_1.
\]

模 `T` 看：

\[
-M\gamma\equiv C_0\lambda\pmod T.
\]

因此

\[
\boxed{
J_1:=\frac{M\gamma+C_0\lambda}{T}\in\mathbf Z.
}
\tag{1}
\]

把它代回原恒等式并除以 `T`：

\[
\boxed{
MDN_0
=1000\lambda T^3+c_2\lambda T+J_1.
}
\tag{2}
\]

---

## 2. `J_1/(lambda*T)` 落在固定区间

由 `deep-complement-height.md`：

\[
\mu:=\frac{MD}{\lambda T^2},
\qquad
1000<\mu<10001,
\]

以及

\[
\Gamma_k=\frac\gamma D,
\qquad
15.09<\Gamma_k<39.003.
\]

所以

\[
\frac{J_1}{\lambda T}
=
\frac{M\gamma}{\lambda T^2}
+
\frac{C_0}{T^2}
=
\mu\Gamma_k+\frac{C_0}{T^2}.
\]

因此

\[
\boxed{
15090<\frac{J_1}{\lambda T}<390070.
}
\tag{3}
\]

特别地 `J_1>0`。

---

## 3. 真正的小 remainder `R_1`

定义

\[
\boxed{R_1:=c_2\lambda T+J_1.}
\tag{4}
\]

由于

\[
-790\le c_2\le-190,
\]

由 (3) 得安全统一界

\[
\boxed{
14300\,\lambda T<R_1<390100\,\lambda T.
}
\tag{5}
\]

而 (2) 变成

\[
\boxed{
MDN_0=1000\lambda T^3+R_1.
}
\tag{6}
\]

所以任何落在 `MDN_0` 上、但比 `1000 lambda T^3` 更浅的 2/5-adic valuation，都必须完整落到这个只有 `O(lambda*T)` 大小的 `R_1` 上。

---

## 4. fully-balanced collapse 的解释

若两侧 cancellation depth 都达到

\[
A+e+\nu_2\ge k+\lambda_2,
\qquad
B+\nu_5\ge k+\lambda_5,
\]

则 `lambda*T^2 | MDTN_0`。由原 identity 进一步得到 `lambda*T | J_1`，于是可以写

\[
J_1=J\lambda T
\]

并得到 `deep-balanced-collapse.md` 中绝对有界的整数 `J`。

所以 `J_1` 是 balanced descent 与剩余 shallow branches 的公共第一层对象。

---

## 5. 当前用途

后续无需每次重新展开 `Qb_1`。任何 deep branch 若能证明某个素数 `p in {2,5}` 满足

\[
v_p(MDN_0)<v_p(1000\lambda T^3),
\]

就自动得到

\[
p^{v_p(MDN_0)}\mid R_1.
\]

再和 (5) 的实数尺寸比较即可产生 branch-specific contradiction 或高度上界。

`deep-double-5high-collapse.md` 将给出第一个整支应用。
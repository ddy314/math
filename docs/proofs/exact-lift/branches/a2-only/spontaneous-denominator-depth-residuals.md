# A2 denominator depth mismatch 的两个 simple residual

> **依赖：** `spontaneous-denominator-depth-matrix.md`。
>
> **严格状态：**denominator depth matrix 已把 angle/additive 两侧分别降成 `Delta_0` 与两个 K-quadratic。本文继续证明：q/f 两侧若出现 depth mismatch，较浅深度必须精确落在一个额外的 simple residual 上。q residual 只依赖 decimal length `N=10^M`；f residual只依赖前缀平方量 `A_pref=2025b_2^2+81N^2`。两个 residual 对所有 genuine non-3 inert prime 都无 repeated root。本文同时审计其 quadratic characters，证明它们与旧 additive roots 位于同一个 quadratic extension，因此 character stacking 是 no-go。本文仍不证明 simple-root depth mismatch 不存在，也不宣称 A2 全局关闭。

---

## 1. 统一整数 prefix defect

令

\[
N:=10^M,
\qquad
B:=b_2,
\qquad
K:=9N+10a_2.
\]

因为

\[
x=B/N,
\qquad
s=9+y=K/N,
\]
定义

\[
\boxed{
A_{\rm pref}:=2025B^2+81N^2.}
\tag{1.1}
\]

则

\[
\boxed{
D_{\rm pref}:=N^2\Delta_0
=A_{\rm pref}-K^2.}
\tag{1.2}

对 genuine odd prime，`N` 为单位，所以

\[
\boxed{v_p(D_{\rm pref})=v_p(\Delta_0).}
\tag{1.3}

这允许直接在整数环中比较 angle defect 与 additive K-root 的深度。

---

# q-side

## 2. q residual 是纯 decimal-length quadratic

定义

\[
\boxed{
P_q(K):=K^2-26,}
\tag{2.1}

\[
\boxed{
R_q(N):=8181N^2-26.}
\tag{2.2}

又有

\[
Q=B+2N.
\]

直接展开得到 exact identity

\[
\boxed{
P_q(K)+D_{\rm pref}-R_q(N)
=2025Q(B-2N).}
\tag{2.3}

等价地

\[
P_q(K)+N^2\Delta_0-R_q(N)
=Q(2025Q-8100N).
\]

若

\[
p^e\Vert q
\]
且属于 generic q-denominator layer `p∤c_Q`，则

\[
v_p(Q)=e.
\]
因此模 `p^e`：

\[
\boxed{P_q(K)+D_{\rm pref}\equiv R_q(N)\pmod{p^e}.}
\tag{2.4}

令

\[
a=v_p(P_q),
\qquad d=v_p(D_{\rm pref}),
\qquad r=v_p(R_q).
\]

如果最小深度严格小于 `e`，ultrametric law 立即给

\[
\boxed{
\begin{aligned}
a<d,\ a<e&\Longrightarrow r=a,\\
d<a,\ d<e&\Longrightarrow r=d.
\end{aligned}}
\tag{2.5}

所以 q-side angle/additive depth mismatch 的较浅一侧，必须以完全相同的深度出现在 `R_q` 中。

---

## 3. q residual 对所有 genuine odd prime 都 simple

\[
R_q'(N)=2\cdot8181N.
\]

若 odd prime同时使 `R_q=R_q'=0`，因为 `N` 为单位，只能

\[
p\mid8181.
\]
原方程又要求 `p|26`，与

\[
\gcd(8181,26)=1
\]
矛盾。因此

\[
\boxed{R_q\text{ 在任意 genuine odd prime 上没有 repeated root。}}
\tag{3.1}

q-side depth mismatch 只能沿唯一 simple decimal-length Hensel lift传播。

---

# f-side

## 4. f residual 只依赖 `A_pref`

定义 additive quadratic

\[
\boxed{P_f(K):=3K^2-36K+26.}
\tag{4.1}

由 (1.2)：

\[
P_f(K)+3D_{\rm pref}
=3A_{\rm pref}-36K+26.
\tag{4.2}

记

\[
C_f:=3A_{\rm pref}+26,
\]
以及

\[
\boxed{
R_f^{\rm len}(A_{\rm pref})
:=C_f^2-1296A_{\rm pref}
=9A_{\rm pref}^2-1140A_{\rm pref}+676.}
\tag{4.3}

有 exact Bezout identity

\[
\boxed{
R_f^{\rm len}
=
\bigl(P_f+3D_{\rm pref}\bigr)
\bigl(C_f+36K\bigr)
-1296D_{\rm pref}.}
\tag{4.4}

展开为关于两个 depth objects 的形式：

\[
\boxed{
R_f^{\rm len}
=P_fU_f+D_{\rm pref}V_f,}
\tag{4.5}

其中

\[
U_f:=C_f+36K,
\qquad
V_f:=3U_f-1296.
\tag{4.6}

---

## 5. common f-root 上两个 Bezout 系数都是单位

在 first-layer common root

\[
P_f\equiv0,
\qquad
D_{\rm pref}\equiv0
\pmod p,
\]
有

\[
A_{\rm pref}\equiv K^2.
\]
由 `P_f=0`：

\[
3K^2+26\equiv36K.
\]
所以

\[
\boxed{U_f\equiv72K\pmod p.}
\tag{5.1}

如果 `p|K`，`P_f(0)=26` 强迫 `p|26`，没有 genuine non-3 inert prime。故 `U_f` 为单位。

另一方面

\[
\boxed{V_f\equiv216(K-6)\pmod p.}
\tag{5.2}

若 `p|K-6`，则

\[
P_f(6)=-82=-2\cdot41,
\]
所以唯一 odd candidate 是 `41`，而

\[
41\equiv1\pmod4.
\]
因此对 genuine non-3 inert prime，`V_f` 也是单位。

于是令

\[
a=v_p(P_f),
\qquad d=v_p(D_{\rm pref}),
\qquad r=v_p(R_f^{\rm len}).
\]
由 (4.5)：

\[
\boxed{
\begin{aligned}
a<d&\Longrightarrow r=a,\\
d<a&\Longrightarrow r=d.
\end{aligned}}
\tag{5.3}

若两者等深，才可能因 normalized cancellation 使 residual 更深。

所以 f-side depth mismatch 也被一个低次 residual 精确承接，而不需要使用 `spontaneous-denominator-common.md` 的完整 octic。

---

## 6. f residual 同样没有 genuine inert repeated root

把 `R_f^{len}` 看成 `A_pref` 的 quadratic：

\[
9A^2-1140A+676.
\]
其判别式为

\[
\boxed{
\begin{aligned}
\operatorname{Disc}_A(R_f^{\rm len})
&=1140^2-4\cdot9\cdot676\\
&=1275264\\
&=2^7\cdot3^5\cdot41\\
&=72^2\cdot246.
\end{aligned}}
\tag{6.1}

唯一 non-`3` odd ramified prime仍是 `41=1 mod4`。因此

\[
\boxed{
R_f^{\rm len}\text{ 对所有 genuine non-3 inert prime 都只有 simple root。}}
\tag{6.2}

结合 §5，f-side parity mismatch 同样只能沿 simple Hensel orbit传播。

---

## 7. 两个 channel 的 residual 表

因此 denominator depth matrix 可进一步扩展为

\[
\boxed{
\begin{array}{c|c|c|c}
&\text{angle}&\text{additive}&\text{mismatch residual}\\ \hline
q&D_{\rm pref}&P_q(K)=K^2-26&R_q(N)=8181N^2-26\\[1mm]
f&D_{\rm pref}&P_f(K)=3K^2-36K+26&R_f^{\rm len}(A_{\rm pref})
\end{array}}
\tag{7.1}

三个 additive/residual polynomial 在 genuine non-3 inert primes 上全都 simple。

因此 denominator pool 中已经没有任何需要继续追踪的 singular polynomial tree。剩余自由只可能是：

1. 两个 simple depths 恰好相等后的 normalized cancellation；
2. 两个 simple roots沿 decimal/source orbit同步提升。

---

## 8. `审计 / no-go`：f residual 没有新的 quadratic character

additive f quadratic 的判别式为

\[
\operatorname{Disc}_K(P_f)=984=4\cdot246.
\tag{8.1}

而 (6.1) 给

\[
\operatorname{Disc}_{A}(R_f^{\rm len})=72^2\cdot246.
\tag{8.2}

因此两种 root 的 quadratic field完全相同：

\[
\boxed{
P_f\text{ has a simple root mod }p
\iff
R_f^{\rm len}\text{ 的 discriminant square class也是 }246.}
\tag{8.3}

所以从 residual 再提取

\[
\left(\frac{246}{p}\right)=1
\]
不是新 obstruction，而是同一个 quadratic extension 的影子。

q-side同样如此：

\[
R_q=0
\Longrightarrow
8181N^2=26,
\]
而 `8181=81*101`；其 character正是旧 common q-system 中 `(101/p)` 与 `(26/p)` 的组合，没有独立新信息。

结论：后续不得再沿 denominator residual 做 Legendre/Jacobi stacking。真正的前沿是 simple-root **depth synchronization**。

---

## 9. 当前 denominator 开放核

结合 `spontaneous-denominator-repeated-common.md`：repeated spontaneous 与 saturated denominator common 已没有 surviving unbounded Hensel branch。

本文又证明所有 depth-mismatch residual 都是 simple。因此 denominator residual odd parity 的最后规范形态是

\[
\boxed{
\text{simple }D_{\rm pref}\text{ root}
\quad\leftrightarrow\quad
\text{simple }P_q/P_f\text{ root}
\quad\leftrightarrow\quad
\text{simple }R_q/R_f\text{ root}.}
\tag{9.1}

下一步如果继续 denominator parity，应研究这些 simple roots 的**相对 Hensel derivative / decimal-orbit synchronization**，而不是再求 discriminant或 singular bad primes。若能证明每个 denominator primary 上 angle/additive depth差恒为偶数，就能从 `G_sp mod4` dichotomy 中完全删除 denominator residual supplier。

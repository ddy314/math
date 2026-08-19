# A1 minimal diagonal: `HL` exact 5-adic Hensel lock

> 日期：2026-08-20。依赖 `deep-moderate-factorization.md` 与 `deep-double-5high-collapse.md`。当前范围 `k=g>=31`。

moderate double-deep 现只剩 `HL`。本文从 moderate quadratic 中提取一个精确的 5-adic valuation identity；它比仅有的 `B+2nu_5=v_5(r)` 更强，因为它锁定了 gap numerator `gamma` 与 prefix integer `N_0` 的一个 Hensel combination。

状态：**已严格完成。**

---

## 1. HL 参数

记

\[
a_2:=v_2(r),
\qquad
a_5:=v_5(r),
\qquad
\nu:=v_5(N_0).
\]

HL 的 5-low identity 为

\[
\boxed{B+2\nu=a_5.}
\tag{1}
\]

因此

\[
Y:=B+\nu=a_5-\nu\le10,
\]

以及

\[
\boxed{d:=k+1-Y=k+1-B-\nu>0.}
\tag{2}

double-deep 的 reduced gap numerator `gamma` 与 5 互素。

---

## 2. moderate quadratic in `Gamma`

由 `deep-moderate-factorization.md` 的 factor identity，令

\[
\Gamma:=\gamma/D,
\qquad
C_0=w(10w-1),
\]

可写成

\[
\boxed{
1000T^2\Gamma^2
+\bigl(r-10(20w-1)N_0T\bigr)\Gamma
+C_0N_0^2-rTN_0
=0.
}
\tag{3}

移项：

\[
\boxed{
r\Gamma+C_0N_0^2
=10(20w-1)N_0T\Gamma
+rTN_0
-1000T^2\Gamma^2.
}
\tag{4}

---

## 3. 右侧三项的 5-adic valuation

因为 `20w-1` 是 5-adic unit，且

\[
v_5(\Gamma)=-B,
\]

第一项有

\[
v_5\bigl(10(20w-1)N_0T\Gamma\bigr)
=k+1+\nu-B.
\tag{5}

第二项：

\[
v_5(rTN_0)
=a_5+k+\nu
=k+B+3\nu.
\]

与 (5) 的差为

\[
2B+2\nu-1\ge1.
\tag{6}

第三项：

\[
v_5(1000T^2\Gamma^2)
=2k+3-2B.
\]

与 (5) 的差为

\[
k+2-B-\nu=d+1>0.
\tag{7}

所以 (4) 右侧第一项**唯一**取得最小 5-adic valuation。不存在额外 cancellation。

因此

\[
\boxed{
v_5(r\Gamma+C_0N_0^2)=k+1+\nu-B.}
\tag{8}

---

## 4. integer form

乘以

\[
D=2^A5^B
\]

得到整数：

\[
D(r\Gamma+C_0N_0^2)
=r\gamma+C_0DN_0^2.
\]

由 (8)：

\[
\boxed{
v_5(r\gamma+C_0DN_0^2)=k+1+\nu.}
\tag{9}

这已经把一个随 `k` 增长的 exact valuation 直接压到 gap numerator / decimal prefix 的二项组合上。

进一步写

\[
r=5^{a_5}r_5,
\qquad
N_0=5^\nu n,
\qquad
5\nmid r_5n\gamma.
\]

由 (1)：

\[
a_5=B+2\nu.
\]

提出共同因子 `5^(B+2nu)`：

\[
r\gamma+C_0DN_0^2
=5^{B+2\nu}
\left(
 r_5\gamma+C_0 2^A n^2
\right).
\]

结合 (9)：

\[
\boxed{
v_5\left(r_5\gamma+C_0 2^A n^2\right)=d.}
\tag{10}

也就是精确 Hensel congruence

\[
\boxed{
r_5\gamma+C_0 2^A n^2\equiv0\pmod{5^d},}
\tag{11}

但

\[
\boxed{
r_5\gamma+C_0 2^A n^2\not\equiv0\pmod{5^{d+1}}.}
\tag{12}

这里

\[
d=k+1-B-\nu
\]

随 `k` 线性增长。

---

## 5. HL 的参数化版本

HL 还有

\[
A=2k+3-a_2.
\]

因此 (10) 可完全写成有限 `r` 与一个随 `k` 的 5-adic Hensel equation：

\[
\boxed{
v_5\left(
 r_5\gamma
 +C_0\,2^{2k+3-a_2}n^2
\right)
=k+1-a_5+\nu.}
\tag{13}

其中

\[
0\le\nu\le\left\lfloor\frac{a_5-1}{2}\right\rfloor,
\]

所以对固定 `r`，`nu,B,Y` 都来自绝对有限集合。

---

## 6. 当前意义

moderate LL 已由 exact modular exhaustion 全部关闭，所以 (13) 现在直接作用于唯一 surviving moderate branch `HL`。

HL 当前同时满足：

1. finite typewise `r` window；
2. `r_10` / `(alpha,beta)` mod-4 orientation；
3. whole-block partition `alpha*beta=r_10`；
4. adjugate gcd lock `gcd(N_0,gamma)|r_10`；
5. 本文 exact `5^d || (...)` Hensel lock；
6. Q-side strict-2-low orientation / proper-divisor loss。

下一步应把 (13) 与 stripped equations

\[
2\beta\bar s-\alpha\bar q=5^d,
\]

\[
\beta q-5\alpha s=2^{c'}n_0
\]

联立，尝试把 growing Hensel depth `d` 转成有限 periodic / descent obstruction。
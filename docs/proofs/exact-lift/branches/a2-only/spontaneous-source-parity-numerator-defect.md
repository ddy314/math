# A2 source parity numerator-angle reuse 的 pure defect gate

> **依赖：** `spontaneous-source-parity-angle-overlap.md`、`endpoint-lattice.md` 的最危险 `(a,k)=(9,2)` endpoint defect shell。
>
> **严格状态：**source odd/odd reused prime若进入 angle common numerator sheet，前文只把它投影到 `162*10^M-55` length gate。本文恢复 endpoint defect `a_2=10^(M-1)-e`，把该 gate进一步降到极短整数 `324e-11`。所有 numerator-angle reused primes的 radical都整除 `324e-11 < (81/625)N`。本文不排除该 defect integer拥有 inert divisors，因此不关闭 A2。

---

## 1. endpoint numerator defect

当前最危险 core 已严格固定

\[
\boxed{a_2=10^{M-1}-e,}
\tag{1.1}
\]

并有

\[
\boxed{0<e<\frac{10^{M-1}}{250}.}
\tag{1.2}
\]

令

\[
N=10^M.
\]

则

\[
10^{M-1}=\frac N{10},
\]
所以

\[
\boxed{a_2=\frac N{10}-e.}
\tag{1.3}
\]

当前

\[
K=9N+10a_2,
\]
因此

\[
\boxed{K=10(N-e).}
\tag{1.4}
\]

---

## 2. numerator overlap plus source collision

固定 source odd/odd reused prime `r`，并进一步假设它进入 angle numerator sheet：

\[
\boxed{r\mid a_2.}
\tag{2.1}
\]

source parity collision gate已有

\[
\boxed{r\mid18K-55.}
\tag{2.2}
\]

由 (1.3)、(2.1)：

\[
\boxed{N\equiv10e\pmod r.}
\tag{2.3}
\]

再由 (1.4)：

\[
18K-55
=180(N-e)-55.
\]

模 `r` 使用 (2.3)：

\[
18K-55
\equiv180(10e-e)-55
=1620e-55
=5(324e-11).
\]

因此 genuine reused prime `r!=5` 满足

\[
\boxed{r\mid324e-11.}
\tag{2.4}
\]

这比原 length gate

\[
r\mid162N-55
\]
更短，并且只依赖小 numerator defect `e`。

---

## 3. positive short window

由 `e>=1`：

\[
324e-11\ge313>0.
\]

由 (1.2)：

\[
e<\frac{N}{2500}.
\]
所以

\[
324e-11<\frac{324}{2500}N
=\frac{81}{625}N.
\]

因此定义

\[
\boxed{L_e:=324e-11}
\tag{3.1}
\]
后有

\[
\boxed{
0<L_e<\frac{81}{625}N<0.13N.}
\tag{3.2}
\]

这是一个仅 `O(10^M)`、且常数不到 `0.13` 的 pure-defect natural representative。

---

## 4. radical budget for numerator-angle reused primes

令 `E_A` 为所有同时满足

1. source odd/odd parity reuse；
2. angle common numerator sheet `r|a_2`；

的 genuine inert primes。

定义其 radical

\[
\boxed{R_A:=\prod_{r\in E_A}r.}
\tag{4.1}
\]

由 (2.4)，所有这些 distinct primes都整除同一个 `L_e`，所以

\[
\boxed{R_A\mid L_e.}
\tag{4.2}
\]

进而

\[
\boxed{R_A<\frac{81}{625}N.}
\tag{4.3}
\]

因此 numerator-angle reuse的 moving support无法比 `N` 更快增长，而且实际常数小于 `0.13`。

---

## 5. relation to reuse half-depth

source parity reuse depth theorem还给每个 `r in E_A`

\[
r^{(e_r+1)/2}\mid18K-55,
\]
其中 `e_r=v_r(B_W)=v_r(D_W)` 为奇数。

所以 numerator-angle reused pool同时受到两种独立形状的 natural representatives约束：

\[
\boxed{
\prod r^{(e_r+1)/2}\mid18K-55<180N,}
\tag{5.1}
\]

\[
\boxed{
\prod r\mid324e-11<\frac{81}{625}N.}
\tag{5.2}
\]

前者控制 depth，后者控制 distinct support。

---

## 6. current angle-reuse split

source parity reused prime若再被 angle pair复用，现在只剩：

### numerator-defect sheet

\[
\boxed{r\mid a_2,\qquad r\mid324e-11,}
\]
并有 radical budget (4.3)；

### denominator sheet

\[
\boxed{r\mid c_Q.}
\]

所以原来的 generic `A Q_0 c_Q` overlap已经从三块 support压成一个 very short defect carrier加一个 denominator-content exception。

A2 仍为 `待证`。

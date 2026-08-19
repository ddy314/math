# A2 source-reuse `O/J` cross-pair 的 fixed `67` defect templates

> **依赖：** `spontaneous-source-reuse-cross-pair-length.md`、`endpoint-lattice.md` 的 defect coordinates。
>
> **严格状态：**pure-length projection的唯一 surviving repeated projection prime `67` 实际只有两个 simple full states。本文把它们代回真实 numerator/denominator defect，得到 `M=33t`, `e=10 mod67` 与四个 `(t mod2,B,H)` templates。所有模板仍局部可行，因此 `67` 被严格降级为 finite fixed simple templates，而非 singular Hensel exception。本文不排除这些 templates 的全局 lift，故不关闭 A2。

---

## 1. decimal length phase

cross-pair audit给

\[
\boxed{N=10^M\equiv1\pmod{67}.}
\tag{1.1}

直接计算

\[
\boxed{\operatorname{ord}_{67}(10)=33,}
\tag{1.2}

所以

\[
\boxed{M=33t,\qquad t\ge1.}
\tag{1.3}

---

## 2. numerator defect

source collision linear gate给

\[
18K-55=0\pmod{67}.
\]

因此

\[
\boxed{K\equiv44\pmod{67}.}
\tag{2.1}

由

\[
K=9N+10A
\]
和 `N=1`：

\[
\boxed{A\equiv37\pmod{67}.}
\tag{2.2}

endpoint numerator defect为

\[
A=N/10-e.
\]

因为

\[
10^{-1}\equiv47\pmod{67},
\]
得到

\[
\boxed{e\equiv47-37\equiv10\pmod{67}.}
\tag{2.3}

该 residue与 `0<e<N/2500` 并不冲突，因此不能删除 fixed `67`。

---

## 3. denominator phase

endpoint denominator defect为

\[
\boxed{B=N/10+2^{M-1}H.}
\tag{3.1}

cross-pair full system的两个 simple states为

\[
\boxed{B\equiv53,37\pmod{67}.}
\tag{3.2}

又

\[
2^{33}\equiv-1\pmod{67},
\qquad2^{-1}\equiv34\pmod{67}.
\]

所以对 `M=33t`：

\[
\boxed{
2^{M-1}
\equiv34(-1)^t
\equiv
\begin{cases}
33,&t\text{ odd},\\
34,&t\text{ even}
\end{cases}
\pmod{67}.}
\tag{3.3}

---

## 4. four exact templates

由 `N/10=47 mod67`，(3.1)--(3.3) 给

\[
\boxed{
\begin{array}{c|c|c}
t\bmod2&B\bmod67&H\bmod67\\ \hline
0&53&12\\
0&37&47\\
1&53&55\\
1&37&20
\end{array}}
\tag{4.1}

并统一有

\[
\boxed{e\equiv10\pmod{67}.}
\tag{4.2}

这四个 states的 parent `(B,N)` Jacobian均为 unit，因此各自若继续，只能沿唯一 simple local lift，不会形成 singular branching。

---

## 5. strict classification

fixed `67` 现在应分类为

\[
\boxed{
\text{four simple decimal-defect templates indexed by }t\bmod2,}
\]

而非

- resultant bad coefficient；
- repeated full-system root；
- singular Hensel tree。

后续若要删除 `67`，必须把表 (4.1) 与 source factor allocation、third defect或更高 decimal exponent lift联立；继续做 discriminant分析不会增加信息。

A2 仍为 `待证`。

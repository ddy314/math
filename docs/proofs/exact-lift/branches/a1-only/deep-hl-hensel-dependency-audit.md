# A1 minimal diagonal: HL Hensel lock dependency audit

> 日期：2026-08-20。依赖 `deep-four-factor-frame.md`、`deep-moderate-adjugate-gcd-lock.md`、`deep-hl-5adic-hensel-lock.md`。当前范围 `k=g>=31`。

本文纠正一个证明架构问题：`deep-hl-5adic-hensel-lock.md` 中的 growing-depth 5-adic valuation identity 虽然公式本身正确，但它**不是**独立于 four-factor frame 的新 obstruction。事实上，完整的整除深度以及“恰好到这一层、不再多一层”都可由 stripped four-factor identities 直接推出。

因此后续不能把该 Hensel lock 与 four-factor frame 当作两层独立筛重复计数。

状态：**依赖关系已严格完成。**

---

## 1. HL 记号

在 moderate HL 中写

\[
r=2^{a_2}5^{a_5}r_{10},
\qquad \alpha\beta=r_{10},
\qquad (r_{10},10)=1.
\]

令

\[
\nu=v_5(N_0),
\qquad \nu_2=v_2(N_0),
\qquad N_0=2^{\nu_2}5^\nu n_0,
\]

其中 `(n_0,10)=1`。HL 给

\[
B+2\nu=a_5,
\qquad
A=2k+3-a_2.
\]

定义

\[
c=k+1-a_2+\nu_2,
\qquad
d=k+1-a_5+\nu.
\]

stripped supply / complement equations 为

\[
\boxed{\beta q-5\alpha s=2^c n_0,}
\tag{1}
\]

\[
\boxed{2\beta u-\alpha v=5^d,}
\tag{2}
\]

其中

\[
h=qs,
\quad su=b_1,
\quad qv=Q.
\]

令

\[
\boxed{C:=2^c n_0.}
\]

adjugate small remainders 给

\[
\boxed{2uC-5^d q=\alpha,}
\tag{3}
\]

\[
\boxed{Cv-5^{d+1}s=\beta.}
\tag{4}

---

## 2. Hensel combination

`deep-hl-5adic-hensel-lock.md` 的组合是

\[
E:=r_5\gamma+C_0 2^A n^2,
\]

其中

\[
r_5=r/5^{a_5}=2^{a_2}\alpha\beta,
\qquad n=N_0/5^\nu=2^{\nu_2}n_0,
\qquad C_0=w(10w-1).
\]

由 `A=2k+3-a_2` 与 `c=k+1-a_2+nu_2`：

\[
\boxed{2^A n^2=2^{a_2+1}C^2.}
\tag{5}

因此

\[
\boxed{
\frac{E}{2^{a_2}}
=\alpha\beta\gamma+2C_0C^2.}
\tag{6}

---

## 3. 用 four-factor frame 展开

在 double-deep 中

\[
\gamma=DTN_0-h.
\]

另一方面

\[
Qb_1=huv
=1000T^4+c_2T^2+C_0,
\qquad c_2=10(1-20w),
\]

故

\[
C_0=huv-1000T^4-c_2T^2.
\]

代入 (6)：

\[
\begin{aligned}
\frac{E}{2^{a_2}}
={}&\alpha\beta DTN_0
+h(2uvC^2-\alpha\beta)\\
&-2(1000T^4+c_2T^2)C^2.
\end{aligned}
\tag{7}

而 (3)-(4) 直接给

\[
2uC=\alpha+5^dq,
\qquad
Cv=\beta+5^{d+1}s.
\]

于是

\[
\begin{aligned}
2uvC^2
&=(\alpha+5^dq)(\beta+5^{d+1}s)\\
&=\alpha\beta
+5^d\bigl(\beta q+5\alpha s+5^{d+1}h\bigr).
\end{aligned}
\tag{8}

把 (8) 放回 (7)：

\[
\boxed{
\begin{aligned}
\frac{E}{2^{a_2}}
={}&\alpha\beta DTN_0\\
&+h5^d(\beta q+5\alpha s+5^{d+1}h)\\
&-2(1000T^4+c_2T^2)C^2.
\end{aligned}}
\tag{9}

---

## 4. exact valuation 自动出现

记

\[
Y:=B+\nu\ge1.
\]

由

\[
d=k+1-B-\nu,
\]

第一项在除以 `5^d` 后仍至少含

\[
5^{2Y-1},
\]

所以模 5 消失。

最后一项含 `T^2`，而 `d<=k`，除以 `5^d` 后同样仍被 5 整除。

因此 (9) 除以 `5^d` 并降模 5，只剩中间项：

\[
\boxed{
\frac{E}{2^{a_2}5^d}
\equiv h\,\beta q
=\beta q^2s
\pmod5.}
\tag{10}

`q,s,beta` 都是 5-adic units，所以右侧非零。于是

\[
\boxed{v_5(E)=d.}
\tag{11}

即

\[
\boxed{
v_5\left(
 r_5\gamma+C_0 2^{2k+3-a_2}n^2
\right)
=k+1-a_5+\nu.}
\tag{12}

这正是旧 Hensel lock 的完整结论，包括“不再多整除一个 5”。

---

## 5. 结论

所以 (12) 不是 four-factor frame 之外的新约束，而是

\[
\boxed{
\text{four-factor + decimal }Qb_1\text{ identity}
\Longrightarrow
\text{HL exact Hensel lock}.}
\]

后续 HL 证明中：

- 可以使用 (12) 作为方便的压缩坐标；
- 但不能把它与 (1)-(4) 当成统计独立的第二层 obstruction；
- 纯 5-adic contact-square lifting 也不会提供额外深度：对 5-adic unit，是否为平方完全由 mod-5 Legendre class 决定。

因此 HL 的下一真正独立输入必须来自**原 rational-contact square 的全局结构**、prime-source 结构或新的实/整除约束，而不是重复 Hensel lifting。

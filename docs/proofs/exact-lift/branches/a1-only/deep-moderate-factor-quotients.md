# A1 minimal diagonal: moderate factor quotient refinement

> 日期：2026-08-20。依赖 `deep-moderate-three-pattern.md` 与 `deep-four-factor-frame.md`。当前范围 `k=g>=31`。

`deep-moderate-three-pattern.md` 已证明 moderate double-deep 只有 LL/LH/HL 三种模板。本文把 factor pair

\[
X_1=sa,
\qquad
X_2=qb,
\qquad
ab=Dr
\]

中的全部 `2,5` 次幂精确剥离。

写

\[
a_2:=v_2(r),
\qquad
a_5:=v_5(r),
\]

\[
\boxed{
r_{10}:=\frac{r}{2^{a_2}5^{a_5}},
\qquad\gcd(r_{10},10)=1.}
\]

则三种模板中都存在正整数 `alpha,beta` 满足

\[
\boxed{\alpha\beta=r_{10}.}
\]

所以 strip 掉显式 `2/5` 幂后，未知 quotient 只来自一个绝对有限 divisor pair。

状态：**已严格完成。**

---

## 1. LL

LL 满足

\[
a_2=A+2\nu_2+e,
\qquad
a_5=B+2\nu_5,
\]

其中

\[
e=v_2(w),
\qquad
\nu_p=v_p(N_0).
\]

两个 factor 的精确 valuation 为

\[
v_2(X_1)=A+\nu_2+e,
\qquad
v_2(X_2)=A+\nu_2,
\]

\[
v_5(X_1)=v_5(X_2)=B+\nu_5.
\]

因为 `q,s` 与 10 互素，这也是 `a,b` 的 valuation。因此存在 `alpha,beta` 与 10 互素，使

\[
\boxed{
a=
2^{A+\nu_2+e}
5^{B+\nu_5}\alpha,}
\tag{1}

\[
\boxed{
b=
2^{A+\nu_2}
5^{B+\nu_5}\beta.}
\tag{2}

把 (1)-(2) 相乘，并使用 LL 两个 valuation identity，得到

\[
\boxed{\alpha\beta=r_{10}.}
\tag{3}

---

## 2. LH

LH 为 2-low / 5-high：

\[
a_2=A+2\nu_2+e,
\]

\[
B=2k+3-a_5.
\]

2-adic valuation 仍为 low branch：

\[
v_2(a)=A+\nu_2+e,
\qquad
v_2(b)=A+\nu_2.
\]

5-adic high branch 则精确为

\[
v_5(a)=k+1,
\qquad
v_5(b)=k+2.
\]

所以

\[
\boxed{
a=
2^{A+\nu_2+e}
5^{k+1}\alpha,}
\tag{4}

\[
\boxed{
b=
2^{A+\nu_2}
5^{k+2}\beta,}
\tag{5}

并且仍然

\[
\boxed{\alpha\beta=r_{10}.}
\tag{6}

此前只知道 strip 掉 `5^{k+1},5^{k+2}` 后乘积为 `2^A r_5`；(4)-(6) 把 2-adic low branch 也同时剥净，故剩余 quotient 真正只来自 `r_{10}`。

---

## 3. HL

完全对称。HL 为 2-high / 5-low：

\[
A=2k+3-a_2,
\]

\[
a_5=B+2\nu_5.
\]

2-adic high branch：

\[
v_2(a)=k+1,
\qquad
v_2(b)=k+2.
\]

5-adic low branch：

\[
v_5(a)=v_5(b)=B+\nu_5.
\]

因此

\[
\boxed{
a=
2^{k+1}
5^{B+\nu_5}\alpha,}
\tag{7}

\[
\boxed{
b=
2^{k+2}
5^{B+\nu_5}\beta,}
\tag{8}

\[
\boxed{\alpha\beta=r_{10}.}
\tag{9}

---

## 4. 与 four-factor frame 联立

`deep-four-factor-frame.md` 还给出

\[
qb-10sa=DN_0,
\tag{10}

\[
\bar s b-\bar q a=10T
\tag{11}

（double-deep 中 `lambda=1`）。

因此在 LL/LH/HL 任一模板中，代入本文的 `(a,b)` 后：

- `alpha,beta` 只需遍历 `r_{10}` 的 divisor pairs；
- `A,B` 要么绝对小，要么由 `k,a_2,a_5` 线性确定；
- `nu_2,nu_5` 在 low side 被 `a_2,a_5` 限制在绝对有限集合；
- Q-side / `b_1`-side divisors 同时受到 (10)-(11)。

因此 moderate double-deep 的剩余离散参数已经可取为

\[
\boxed{
(w,r,\alpha,\beta,\nu_2,\nu_5,\text{LL/LH/HL})
}
\]

加上 `k`；不再需要独立扫描 `(A,B,a,b)`。

下一步可把 (10)-(11) 对每种模板除去已知的巨大 `2/5` 幂，得到适合 periodic modular exhaustion 的线性同余系统。
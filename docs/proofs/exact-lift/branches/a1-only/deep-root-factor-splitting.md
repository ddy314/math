# A1 minimal diagonal: moderate root-square factor splitting

> 日期：2026-08-20。依赖 `deep-moderate-root-normal-form.md` 与 `deep-four-factor-frame.md`。当前范围 `k=g>=31`。

本文审计 moderate root normal form 中的平方

\[
Z^2=(10N_0T+r)^2+400N_0Tr(10T^2-w).
\]

结论：该平方在 full four-factor frame 中并不是新的独立 obstruction；其差平方因子可以精确写成 supply / complementary divisors 的乘积。

状态：**已严格完成。**

---

## 1. 完成平方

定义

\[
\boxed{C:=200T^2-20w+1,}
\qquad
\boxed{X:=10N_0T+rC.}
\]

直接展开：

\[
\begin{aligned}
X^2-Z^2
&=r^2(C^2-1)\\
&=r^2(C-1)(C+1).
\end{aligned}
\]

而

\[
C-1=20(10T^2-w)=20b_1,
\]

\[
C+1=2(100T^2-10w+1)=2Q.
\]

所以

\[
\boxed{
(X-Z)(X+Z)=40r^2b_1Q.
}
\tag{1}
\]

---

## 2. 用 universal factor pair 分解两个根因子

moderate double-deep 有

\[
t=Dr,
\qquad
ab=t=Dr,
\]

以及

\[
X_1=sa,
\qquad
X_2=qb,
\]

\[
\bar q=Q/q,
\qquad
\bar s=b_1/s,
\]

\[
\bar s b-\bar q a=10T.
\]

由 root formula

\[
Z=2000T^2\Gamma-10(20w-1)N_0T+r.
\]

直接整理：

\[
X-Z
=20\left(rb_1-10T\frac{X_1}{D}\right).
\]

代入

\[
b_1=s\bar s,
\qquad X_1=sa,
\qquad r=ab/D,
\]

得到

\[
X-Z
=\frac{20sa}{D}(b\bar s-10T).
\]

再用

\[
b\bar s-10T=a\bar q,
\]

即

\[
\boxed{
X-Z=\frac{20a^2s\bar q}{D}.
}
\tag{2}
\]

由 (1) 或对称计算：

\[
\boxed{
X+Z=\frac{2b^2\bar s q}{D}.
}
\tag{3}

两式相乘恰好恢复 (1)。

---

## 3. `HL` 专门化

HL 中

\[
a=2^{k+1}5^Y\alpha,
\qquad
b=2^{k+2}5^Y\beta,
\]

\[
A=2k+3-v_2(r),
\qquad
B+2\nu_5=v_5(r),
\]

\[
\alpha\beta=r_{10}.
\]

记

\[
a_2=v_2(r),
\qquad a_5=v_5(r).
\]

则

\[
\frac{20a^2}{D}
=2^{a_2+1}5^{a_5+1}\alpha^2
=10\frac{r\alpha}{\beta},
\]

以及

\[
\frac{2b^2}{D}
=2^{a_2+2}5^{a_5}\beta^2
=4\frac{r\beta}{\alpha}.
\]

所以 HL 的 root factors 是

\[
\boxed{
X-Z=10\frac{r\alpha}{\beta}\,s\bar q,
}
\tag{4}
\]

\[
\boxed{
X+Z=4\frac{r\beta}{\alpha}\,\bar s q.
}
\tag{5}

由于 `alpha,beta` 是 `r_10` 的 coprime whole-block partition，两个系数均为整数。

---

## 4. `LL` 专门化

LL 中同理得到

\[
\boxed{
X-Z=20\,2^e\frac{r\alpha}{\beta}\,s\bar q,
}
\tag{6}

\[
\boxed{
X+Z=2^{1-e}\frac{r\beta}{\alpha}\,\bar s q,
}
\tag{7}

其中 `e=v_2(w)`；(7) 虽写有 `2^(1-e)`，由 LL 的 `v_2(r)=A+2nu_2+e` 可知整体系数始终为整数。

---

## 5. 审计意义

`deep-moderate-root-normal-form.md` 的 square `Z^2=...` 是由 supply quadratic 的判别式产生的。本文说明，一旦 full factor-pair / four-factor frame 已经成立，`X±Z` 被 (2)-(3) 显式构造，因此 root square 不能再被重复当作一层独立 arithmetic obstruction。

这解释了仅用 root-square + contact-square 的 odd-prime modular sieve 很弱：它没有加入真正新的 prime-source information。

后续 HL 攻击应优先使用：

- stripped complement / supply equations；
- Q-side orientation 与 whole-block source；
- first complement remainder；
- 5-adic Hensel lock；

而不应把 (1) 再计作“第三个独立平方”。
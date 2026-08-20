# A1 minimal diagonal: sharp superlinear Q-side supply in moderate HL

> 日期：2026-08-20。强化 `deep-hl-forced-contact-lift.md`。

旧 uniform proof 分别粗取 `D` 最小与 `beta` 最大，只得到 `q>1683T`。本文保留 HL 中 `D,beta,r` 的相关性，使 `v_2(r)` 精确消掉，得到：

\[
\boxed{q>1.09\times10^7 T\qquad(k\ge32).}
\]

因此 contact exceptional resultant 只占 `q` 的不到约 `1/6800`，而该比例随 k 指数改善。

状态：**已严格完成。**

---

## 1. 从 complement equation 到 q 下界

沿用

\[
2\beta u-\alpha v=5^d>0,
\qquad M=uv,
\]

所以

\[
v^2<\frac{2\beta}{\alpha}M.
\]

又

\[
M<10001\frac{T^2}{D}.
\]

因此

\[
v<T\sqrt{\frac{20002\beta}{\alpha D}}.
\]

而

\[
Q>99T^2,
\qquad q=Q/v,
\]

故

\[
\boxed{
\frac qT
>99\sqrt{\frac{\alpha D}{20002\beta}}.}
\tag{1}

---

## 2. 保留 `alpha beta=r_10`

因为

\[
\alpha\beta=r_{10},
\]

有

\[
\frac{\alpha D}{\beta}
=\frac{D\alpha^2}{r_{10}}
\ge\frac D{r_{10}}.
\tag{2}

HL 中记

\[
a_2=v_2(r),
\qquad a_5=v_5(r).
\]

则

\[
D=2^{2k+3-a_2}5^B,
\]

\[
r=2^{a_2}5^{a_5}r_{10}.
\]

所以出现关键 cancellation：

\[
\boxed{
\frac D{r_{10}}
=
\frac{2^{2k+3}5^{B+a_5}}r.}
\tag{3}

`a_2` 完全消失。

---

## 3. uniform finite-window lower bound

HL 为 double-deep，所以

\[
B\ge1,
\qquad a_5\ge1.
\]

因此

\[
5^{B+a_5}\ge25.
\]

contact-sign typewise windows 给全局

\[
r\le15,204,352.
\]

故 (3)：

\[
\boxed{
\frac D{r_{10}}
\ge
\frac{25\cdot2^{2k+3}}{15,204,352}.}
\tag{4}

结合 (1)-(2)：

\[
\boxed{
\frac qT
>
99\sqrt{
\frac{25\cdot2^{2k+3}}
{20002\cdot15,204,352}
}.}
\tag{5}

右侧每增加一个 k 精确乘 2。因此最弱是 `k=32`。

直接取安全十进制：

\[
99\sqrt{
\frac{25\cdot2^{67}}
{20002\cdot15,204,352}
}
>10,900,000.
\]

所以

\[
\boxed{q>10,900,000\,T.}
\tag{6}

---

## 4. 与 contact resultant 的比例

`deep-contact-q-resultant-loss.md`：

\[
g:=\gcd(q,C)<1599T.
\]

所以当前首层已满足

\[
\boxed{
\frac qg
>
\frac{10,900,000}{1599}
>6800.}
\tag{7}

并且 (5) 说明 k 每增加 1，右侧至少再乘 2：

\[
\boxed{
\frac qg>6800\cdot2^{k-32}.}
\tag{8}

因此 contact block theorem 中相对于 ideal `q^2` lifting 的 total loss `g` 极小；guaranteed extra amplification product `q/g` 从 k=32 起就至少是四位数，并指数增长。

---

## 5. complementary divisor 同时极小

由 `qv=Q<101T^2` 与 (6)：

\[
\boxed{
v<\frac{101}{10,900,000}T<10^{-5}T.}
\tag{9}

所以 moderate HL 的 Q-side 已呈现强烈的不对称：

\[
\boxed{q>10^7T,
\qquad v<10^{-5}T.}
\]

后续 one-exponent divisor analysis 应利用这个尺度，而不再把 `q,v` 当作两个可同尺度变化的 arbitrary divisors of Q。

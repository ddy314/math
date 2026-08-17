# A1 rational-contact discriminant audit — 2026-08-17

本文审计 A1 新框架中反复出现的判别平方

\[
\Xi=P^2-(1+2\theta)S,
\qquad
S=r_1^2+r_2^2.
\]

结论很重要：**在完整 exact-contact 系统中，`Xi` 为有理平方并不是额外独立障碍；它是 contact 恒等式与球面方程的代数重写。**

这不使由其清分母得到的整数恒等式失效；那些恒等式仍可用于赋值、整除和 prime-flow bookkeeping。需要修正的是证明解释：不能再把“`Xi` 是平方”本身当成一条独立于 exact contact 的新筛选器。

本文结论为 **已严格完成 / 审计澄清**。

---

## 1. 完整 contact 系统

A1 rational-contact 坐标满足

\[
\boxed{
P-R=\theta(R-r),
}
\tag{1}
\]

其中

\[
r=r_3,
\qquad
R^2=S+r^2.
\tag{2}
\]

所以

\[
\boxed{
P=R+\theta(R-r).
}
\tag{3}
\]

---

## 2. 判别核精确平方化

代入 (3)：

\[
\begin{aligned}
\Xi
&=P^2-(1+2\theta)S\\
&=\left(R+\theta(R-r)\right)^2
 -(1+2\theta)(R^2-r^2).
\end{aligned}
\]

展开：

\[
\begin{aligned}
\Xi
={}&R^2+2\theta R(R-r)+\theta^2(R-r)^2\\
&-R^2+r^2-2\theta(R^2-r^2).
\end{aligned}
\]

注意

\[
R(R-r)-(R^2-r^2)
=R(R-r)-(R-r)(R+r)
=-r(R-r).
\]

因此

\[
\Xi
=r^2-2\theta r(R-r)+\theta^2(R-r)^2,
\]

即

\[
\boxed{
\Xi
=\left(r-\theta(R-r)\right)^2.
}
\tag{4}
\]

所以只要完整 exact contact (1) 与球面 (2) 成立，`Xi` 自动就是有理平方，因为 `r,theta,R` 在 exact lift 下均为有理数。

---

## 3. 与二次根公式的关系

此前把 `r` 看成未知量时，从

\[
R=\frac{P+\theta r}{1+\theta}
\]

与

\[
R^2=S+r^2
\]

消去 `R`，得到关于 `r` 的二次式，并把

\[
\Xi=P^2-(1+2\theta)S
\]

识别为判别核。

这个步骤作为**反向构造测试**仍然完全正确：如果只固定 `(P,S,theta)`，想问是否存在有理 `r`，那么 `Xi` 必须为有理平方。

但一旦已经假设存在完整 exact-lift 候选 `(R,r)` 并满足 contact，(4) 说明这个平方条件不再提供第二条独立方程。

因此后续应区分：

- **prefix/tail partial data sieve**：固定部分数据、尚未构造 `r` 时，平方判别仍可用于筛选；
- **full exact-candidate deduction**：已经使用完整 contact 与球面后，不能再把同一个平方性质重复计作独立约束。

---

## 4. 整数平方证书仍然有效，但应理解为整数化恒等式

此前定义

\[
T=10^\ell,
\qquad
D=10^gQ,
\qquad
K=G^2C^2-D^2N,
\]

并得到

\[
\boxed{
W^2=T^2K-2Tb_3DN.
}
\tag{5}
\]

式 (5) 仍然是 exact lift 的严格必要整数恒等式。

根据 (4)，其平方根可以理解为 contact residual 的清分母：

\[
\sqrt\Xi
=\left|r-\theta(R-r)\right|.
\]

因此 (5) 的价值在于：

1. 把有理 contact residual 强制整数化；
2. 允许对 `2,5` 赋值进行严格比较；
3. 与 denominator certificate、prime supply 和 fixed-prefix tail reduction 联用；
4. 在只给定 partial data 时作为有效的平方筛选。

它的价值**不应**表述为“在完整 contact 之外又多出一个神秘平方障碍”。

---

## 5. 对现有 A1 证明树的影响

### 保持有效

以下已经完成的 A1 结果不依赖“平方条件独立”这一解释，因此保持有效：

- rational-contact 恒等式；
- universal integer-square identity 本身；
- denominator divisibility certificate；
- `2/5` 赋值分层；
- resonance/cross-corridor fixed-prefix finite 结论；
- safe integer-gap recovery；
- moving-prefix contact window 中直接由 `P>R`、digit window 得到的 `K` 不等式；
- 2026-08-17 的全局四层定理与最高层 endpoint/residue kernel。

### 需要避免的表述

后续不得使用以下逻辑：

\[
\text{full contact + sphere}
\Longrightarrow
\Xi\text{ square}
\]

然后把 `Xi square` 再当成与前两者独立的第三条方程进行维数计数或“额外稀疏性”论证。

---

## 6. 当前研究意义

这次审计把 A1 的真正独立输入进一步厘清：

\[
\boxed{
\text{decimal contact}
+\text{sphere/rationality}
+\text{primitive denominator structure}
+\text{digit geometry}
}
\]

其中平方证书属于前两者的整数化接口。

因此 moving-prefix 的下一步应继续使用：

- endpoint/residue kernel；
- `gcd(U_i,b_i)=1`；
- denominator prime graph；
- safe integer-gap divisibility；
- `2/5` 整数赋值；

而不把判别平方本身重复计算成新的独立约束。

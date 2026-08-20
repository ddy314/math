# A1 minimal diagonal: moderate HL as one-exponent divisor families

> 日期：2026-08-20。依赖 `deep-double-2high-master.md`、`deep-typewise-r-window.md`、`deep-moderate-block-partition.md`。本文只研究 master branch 的 moderate part `eta<=0`，即原 HL。

本文把 moderate HL 的 unbounded dependence 从 `k` 改写成一个单独指数 `d`。所有其余离散数据来自绝对有限集合。

状态：**归约严格完成；一指数 divisor family 尚待关闭。**

---

## 1. finite HL data

moderate HL 有有限整数

\[
r\in[r_{\min}(z,w),r_{\max}(z,w)],
\]

并记

\[
a_2=v_2(r),
\qquad a_5=v_5(r),
\qquad r_{10}=r/(2^{a_2}5^{a_5}).
\]

5-low identity：

\[
\boxed{B+2\nu_5=a_5.}
\tag{1}

所以 `nu_5` 只可取

\[
0\le\nu_5\le\left\lfloor\frac{a_5-1}{2}\right\rfloor,
\]

并且

\[
\boxed{B=a_5-2\nu_5,}
\qquad
\boxed{Y:=B+\nu_5=a_5-\nu_5.}
\tag{2}

因此对固定 `r,nu_5`，`B,Y` 都是绝对常数。

另外

\[
\alpha\beta=r_{10},
\qquad\gcd(\alpha,\beta)=1,
\]

且每个 `p^e||r_10` block 必须整个分给 `alpha` 或 `beta`。所以 `(alpha,beta)` 也是 finite whole-block partition。

---

## 2. 以 `d` 取代 `k`

HL 定义

\[
\boxed{d:=k+1-Y>0.}
\tag{3}

因为 `Y` 已固定：

\[
\boxed{k=d+Y-1.}
\tag{4}

所以所有十进制母体都变成 `d` 的显式 exponential polynomial。

---

## 3. complementary divisor 母体

minimal diagonal：

\[
b_1=10^{2k+1}-w,
\qquad
Q=10^{2k+2}-(10w-1).
\]

代入 (4)：

\[
\boxed{
b_1(d)=10^{2d+2Y-1}-w,}
\tag{5}

\[
\boxed{Q(d)=10^{2d+2Y}-(10w-1).}
\tag{6}

写 complementary divisors

\[
u=b_1/s,
\qquad v=Q/q.
\]

于是

\[
\boxed{u\mid b_1(d),
\qquad v\mid Q(d).}
\tag{7}

并且 `u` 不是任意 divisor：由于 `s` 只能使用 `b_1` 的 `1 mod4` whole prime-power blocks，`u` 必须包含

1. `b_1` 的全部 2-power；
2. `b_1` 的全部 `p=3 mod4` prime-power blocks；
3. 未被 `s` 选择的其余 `1 mod4` whole blocks。

---

## 4. one-exponent linear divisor equation

master stripped complement equation在 HL 中为

\[
\boxed{2\beta u-\alpha v=5^d.}
\tag{8}

结合 (5)-(7)，任何 moderate HL candidate 必须给出

\[
\boxed{
\begin{aligned}
&u\mid10^{2d+2Y-1}-w,\\
&v\mid10^{2d+2Y}-(10w-1),\\
&2\beta u-\alpha v=5^d,
\end{aligned}}
\tag{9}

其中

\[
(w,Y,\alpha,\beta)
\]

来自绝对有限集合。

所以原先的 unbounded variables

\[
(k,N_0,\gamma,A,B,q,s,u,v)
\]

在这条**必要条件**中已经只剩：

\[
\boxed{
\text{一个指数 }d
+\text{两个 complementary divisors }u,v.}
\]

---

## 5. 固定系数解格

因为 `gcd(alpha,2beta)=1`，任选一组 Bezout 解

\[
2\beta U_0-\alpha V_0=1.
\]

则 (8) 的全部整数解为

\[
\boxed{
u=5^dU_0+\alpha m,}
\]

\[
\boxed{v=5^dV_0+2\beta m,}
\tag{10}

其中 `m in Z`。

因此每个 fixed `(w,Y,alpha,beta)` family 还可以改写成单参数 lattice line (10) 与两个 exponential-divisor 条件 (7) 的交。

这给后续两条明确入口：

- 使用 `10^(2d+c)-const` 的 primitive/cyclotomic blocks；
- 对最小正解 `(u,v)` 尝试 Vieta / divisor descent。

---

## 6. 当前额外 finite filters

真正进入 (9) 前还应先应用已证明的：

- typewise contact-sign `r` window；
- `eta=-a_2` 的 2-adic parity；
- `r_10 mod8` master lock；
- `mod5` Legendre lock；
- `alpha,beta` whole-block partition；
- Q-side `q mod4` orientation / proper-divisor loss。

所以 (9) 是一个安全上层必要 family；实际 admissible finite parameter list 比“所有 r、所有 block partitions”更小。

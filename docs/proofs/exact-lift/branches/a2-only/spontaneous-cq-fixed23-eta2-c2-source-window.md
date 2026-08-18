# A2 fixed `23` `eta=2` `c=2` 的 source-content 窄窗与高度下界

> **依赖：** `spontaneous-cq-fixed23-eta2-slots.md`、`endpoint-lattice.md` 的 `(a,k)=(9,2)` endpoint window、`core.md` 的 source split。
>
> **严格状态：**唯一 `c=2` type 满足 `M=2lambda,m=lambda+1,c_Q=1587`。本文把 third denominator 的真实十进制窗口直接代入 exact denominator formula，得到 `c_u` 的指数窄窗。结合 `lambda=8 mod11` 与 `c_u` 的素因子全部为 `1 mod4`，严格排除 `lambda<52` 的全部 length classes，并把 `lambda=52,63,74` 的 source content分别压成 `{29}`、`{337}`、`{3917,3929}`。本文是低高度有限压缩，不宣称无界 family关闭。

---

## 1. exact `w` formula

当前 type 为

\[
(d,c_Q,k_h,\varepsilon)
=(1,1587,1,+1),
\]

\[
M=2\lambda,
\qquad
m=\lambda+1.
\tag{1.1}

reflection third denominator为

\[
b_3
=2^{M+m+1}5^dc_Qc_u.
\]
代入 (1.1) 与 `d=1`：

\[
\boxed{
b_3
=2^{3\lambda+2}\cdot5\cdot1587\,c_u.}
\tag{1.2}

令

\[
w:=\frac{b_3}{10^m}.
\]
因为

\[
10^m=2^{\lambda+1}5^{\lambda+1},
\]
得到

\[
\boxed{
w
=3174\left(\frac45\right)^\lambda c_u.}
\tag{1.3}

---

## 2. endpoint window 给 `c_u` 的精确指数区间

危险 `(a,k)=(9,2)` endpoint 已有严格界

\[
\boxed{
\frac{837}{1000}<w<\frac{843}{1000}.}
\tag{2.1}

这里下界是已有更强 bound `42/sqrt(2515)` 的有理放宽。

由 (1.3)：

\[
\boxed{
\frac{837}{3174000}
\left(\frac54\right)^\lambda
<c_u<
\frac{843}{3174000}
\left(\frac54\right)^\lambda.}
\tag{2.2}

这是当前 type 的 source-content real window。

另一方面 fixed `23` / `eta=2` 已给

\[
M\equiv16\pmod{22}.
\]
结合 `M=2lambda`：

\[
\boxed{\lambda\equiv8\pmod{11}.}
\tag{2.3}

所以只需依次检查

\[
\lambda=8,19,30,41,52,\ldots
\]

---

## 3. `lambda<52` 全部排除

对 (2.2) 做 exact integer comparison：

### `lambda=8,19,30`

三者的 upper endpoint均小于 `1`，而

\[
c_u\in\mathbb Z_{>0}.
\]
故全部不可能。

### `lambda=41`

exact bounds 满足

\[
2<c_u<3.
\]
同样没有整数。

因此

\[
\boxed{\lambda\ge52.}
\tag{3.1}

于是

\[
\boxed{M=2\lambda\ge104,}
\qquad
\boxed{m=\lambda+1\ge53.}
\tag{3.2}

这把唯一 `c=2` type 的真实 decimal length 从原 `M>=16` 直接提高到 `M>=104`。

---

## 4. first surviving source contents

source split 的本原性已有：

\[
\boxed{
c_u\text{ 的每个奇素因子都 }\equiv1\pmod4,}
\tag{4.1}

并且

\[
5\nmid c_u.
\]
特别地

\[
c_u\equiv1\pmod4.
\tag{4.2}

### `lambda=52`

(2.2) 精确给

\[
28<c_u<30.
\]
唯一整数是

\[
\boxed{c_u=29.}
\tag{4.3}

且 `29=1 mod4`，合法于当前 source-content 筛选。

### `lambda=63`

精确区间满足

\[
336<c_u<339.
\]
其中唯一 `1 mod4` 整数是

\[
\boxed{c_u=337.}
\tag{4.4}

`337` 为素数且 `337=1 mod4`。

### `lambda=74`

(2.2) 给

\[
3912<c_u<3941.
\]
逐个检查该有限区间中所有正整数，并施加 (4.1)，只有

\[
\boxed{c_u\in\{3917,3929\}.}
\tag{4.5}

两者均为 `1 mod4` 素数。

所以最初三条可能的无界-height lattice state 被压成

\[
\boxed{
\begin{array}{c|c|c|c}
\lambda&M&m&c_u\\ \hline
52&104&53&29\\
63&126&64&337\\
74&148&75&3917\text{ or }3929
\end{array}}
\tag{4.6}

---

## 5. 与 fixed `23` depth ledger 的关系

当前 `c=2` blow-up proof 已证明：

\[
M\equiv170,236\pmod{506}
\Longrightarrow d_{23}=1.
\]

因为 `M=2lambda`，前两个对应

\[
\lambda=85,
\qquad
\lambda=118
\]
在 `lambda=8 mod11` 的序列中。

所以 source-content window 与 fixed-`23` depth table 可以共同使用：低层 `52,63,74` 需要进入新建的 `a_3` CRT representative test；`lambda=85` 无论 source content如何，`23`-common depth 已知恰为 `1`。

再次强调：`d_23=1` 是 odd-depth certification，不是 arithmetic state exclusion。

---

## 6. 更新后的 finite-height frontier

对于最后的 `(1,1587,1,+)` family，当前最小需要实际考虑的 source state 已不再从 `lambda=8` 开始，而是

\[
\boxed{(\lambda,c_u)=(52,29),(63,337),(74,3917),(74,3929),\ldots}
\]

每一个这样的 source state 再由
`spontaneous-cq-fixed23-eta2-c2-a3-crt-representative.md`
把 third numerator压到每个 Gaussian orientation至多一个 CRT representative。

因此低高度部分已经成为真正有限的 divisor/representative certificate；无界 closure仍需控制这些 representative 随 `lambda` 的行为。
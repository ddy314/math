# A1 minimal diagonal: reduced-denominator gap normal form

> 日期：2026-08-19。本文以 `sharp-positive-tail-window.md` 为输入，把 gap-desert 问题按 `rho` 的既约 `2/5` 分母分裂。
> 当前只关心 fixed-layer 前沿 `k=g>=6`。

写

\[
\rho=h2^x5^y,
\qquad \gcd(h,10)=1,
\]

并定义

\[
a=\max(-x,0),
\qquad
b=\max(-y,0),
\qquad
d=2^a5^b.
\]

则 `rho=n/d` 为既约分数。

本文核心结论：

1. 任意 candidate 的既约分母满足
   \[
   \boxed{d>\frac{10^k}{39.003}.}
   \]
2. 若 `d|10^k`，则归一化 gap 只能是固定的 24 个整数
   \[
   \boxed{\Gamma\in\{16,17,\ldots,39\}.}
   \]
3. 在这一 central-denominator sector 中，指数被完全显式化：
   \[
   \boxed{x=-k+v_2(\Gamma),\qquad y=-k+v_5(\Gamma),}
   \]
   并有
   \[
   \boxed{
   2^{v_2(\Gamma)}5^{v_5(\Gamma)}h
   =N_0 10^k-\Gamma.
   }
   \]
4. 因而全部剩余无界性都被推入
   \[
   \boxed{a>k\quad\text{或}\quad b>k}
   \]
   的 deep-denominator sector。

状态：**已严格完成。**

---

## 1. 既约 residual

由 sharpened positive-tail theorem，

\[
15.09\,10^{-k}<N_0-\rho<39.003\,10^{-k},
\tag{1}
\]

且 `N_0=ceil(rho)`。

写既约分数

\[
\rho=\frac nd,
\qquad \gcd(n,d)=1,
\]

并定义

\[
\boxed{r:=N_0d-n.}
\tag{2}
\]

因为 `0<N_0-rho<1`，有

\[
1\le r<d.
\]

又

\[
r\equiv-n\pmod d,
\]

所以

\[
\boxed{\gcd(r,d)=1.}
\tag{3}
\]

特别地：若 `a>0` 则 `r` 为奇数；若 `b>0` 则 `5 not| r`。

定义归一化 gap

\[
\boxed{
\Gamma:=10^k(N_0-\rho)=\frac{10^k r}{d}.
}
\tag{4}
\]

由 (1)：

\[
\boxed{15.09<\Gamma<39.003.}
\tag{5}
\]

---

## 2. 分母的统一下界

由 `r>=1` 与 (4)-(5)：

\[
\frac{10^k}{d}<39.003.
\]

所以

\[
\boxed{
d>\frac{10^k}{39.003}.}
\tag{6}
\]

这已经说明任何 gap candidate 都必须有一个接近 `10^k` 尺度或更大的 terminating-decimal reduced denominator。

---

## 3. central denominator：`d|10^k`

现在假设

\[
\boxed{d\mid10^k,}
\tag{7}
\]

等价于

\[
a\le k,\qquad b\le k.
\]

由 (4)，`Gamma` 是正整数。结合 (5)：

\[
\boxed{
\Gamma\in\{16,17,\ldots,39\}.
}
\tag{8}
\]

### 3.1 `a,b` 都必须为正

若 `a=0`，则 `d=5^b`，于是

\[
\frac{10^k}{d}=2^k5^{k-b}
\]

被 `2^k` 整除。因 `k>=6`，任何正整数 `Gamma=r10^k/d` 至少为 `64`，与 (5) 矛盾。

同理，若 `b=0`，则 `Gamma` 被 `5^k>=15625` 整除，更不可能落在 (5)。

因此 central sector 自动满足

\[
\boxed{a>0,\qquad b>0.}
\tag{9}
\]

由 (3)：

\[
\boxed{\gcd(r,10)=1.}
\tag{10}
\]

---

## 4. 24 个整数 gap 精确恢复 `(x,y,r)`

由

\[
\Gamma
=r\,2^{k-a}5^{k-b}
\]

以及 `gcd(r,10)=1`，立即有

\[
v_2(\Gamma)=k-a,
\qquad
v_5(\Gamma)=k-b.
\]

所以

\[
\boxed{
a=k-v_2(\Gamma),}
\tag{11}
\]

\[
\boxed{
b=k-v_5(\Gamma).}
\tag{12}
\]

并且

\[
\boxed{
r=rac{\Gamma}{2^{v_2(\Gamma)}5^{v_5(\Gamma)}}.}
\tag{13}
\]

因为 `a,b>0`，此时 `x=-a,y=-b`，故

\[
\boxed{
x=-k+v_2(\Gamma),}
\tag{14}
\]

\[
\boxed{
y=-k+v_5(\Gamma).}
\tag{15}
\]

整个 central sector 的二维 exponent freedom 因而彻底消失，只剩固定集合 (8) 中的 24 个 `Gamma`。

---

## 5. `h` 的十进制 normal form

在 central sector 中 `x,y<0`，因此既约分子就是

\[
n=h.
\]

由 residual 定义

\[
h=N_0d-r.
\tag{16}
\]

令

\[
\boxed{
c_\Gamma:=2^{v_2(\Gamma)}5^{v_5(\Gamma)}.}
\tag{17}
\]

由 (11)-(13)：

\[
d=\frac{10^k}{c_\Gamma},
\qquad
r=\frac\Gamma{c_\Gamma}.
\]

代入 (16) 并乘以 `c_Gamma`：

\[
\boxed{
 c_\Gamma h=N_0 10^k-\Gamma.
}
\tag{18}
\]

所以对每个固定 `Gamma=16,...,39`，candidate odd supply 必须具有一个极端刚性的十进制尾：

\[
\boxed{
N_0=\frac{c_\Gamma h+\Gamma}{10^k}
\in[10^{k-1},10^k].
}
\tag{19}
\]

这为下一步把 odd-prime supply 与固定 24 个 decimal congruences 联用提供了统一入口。

---

## 6. deep denominator 是唯一剩余无界区

若不满足 `d|10^k`，因为

\[
d=2^a5^b,
\]

必有

\[
\boxed{a>k\quad\text{或}\quad b>k.}
\tag{20}
\]

因此 gap-desert 的统一证明可以严格拆成两个互不重叠的任务：

### A. central sector

\[
a\le k,\ b\le k,
\]

只需处理 24 个固定 `Gamma` 及 (18) 的十进制 supply condition。

### B. deep sector

\[
a>k\quad\text{或}\quad b>k.
\]

至少一个 reduced denominator exponent 穿过 prefix scale `k`，应继续与 typewise resonance/cross-corridor 联用。

相比原来的整个 `(x,y)` 平面，这已经把无界算术问题切成一个绝对有限 central core 与一个具有明确方向性的 deep sector。
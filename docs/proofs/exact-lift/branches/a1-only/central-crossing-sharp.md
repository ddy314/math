# A1 minimal diagonal: sharp bound for the unique central sign crossing

> 日期：2026-08-19。依赖 `central-gap-sign-collapse.md` 与 `central-supply-pell-normal-form.md`。
> 当前统一范围为 `k=g>=26`。

`central-gap-sign-collapse.md` 中唯一没有固定正/负 leading sign 的 surviving family 是

\[
\boxed{(z,w,\Gamma)=(3,1,22).}
\]

旧安全界只记录

\[
N_0/10^k<0.251.
\]

本文利用当前真正前沿 `k>=26` 后极小的 normalized remainder，把它收紧到

\[
\boxed{
\frac{N_0}{10^k}<0.250261,
}
\]

并传入 central Pell descent，得到新的绝对 `U` 下界

\[
\boxed{U\ge3,867,967.}
\]

状态：**已严格完成。**

---

## 1. crossing leading polynomial

令

\[
T=10^k,
\qquad \sigma=N_0/T.
\]

该 family 的 contact integer square kernel 满足

\[
R=10000F(\sigma)T^{10}+\operatorname{Rem},
\]

其中

\[
\boxed{F(\sigma)=\sigma^2-240\sigma+60.}
\tag{1}
\]

且旧精确 coefficient audit 给出

\[
\boxed{|
\operatorname{Rem}|
\le101834561\,T^9.}
\tag{2}
\]

当前 `k>=26`，所以

\[
\frac{|\operatorname{Rem}|}{T^{10}}
\le\frac{101834561}{10^{26}}
<1.019\cdot10^{-18}.
\tag{3}
\]

---

## 2. `0.250261` 已经严格进入负区

取

\[
\sigma_0=\frac{250261}{10^6}.
\]

精确代入 (1)：

\[
F(\sigma_0)
=-9.431879\ldots\times10^{-6}.
\]

因此

\[
10000F(\sigma_0)<-0.0943.
\]

另一方面 `F'(sigma)=2sigma-240<0` 在当前 decade 上严格成立，所以若

\[
\sigma\ge\sigma_0,
\]

则

\[
10000F(\sigma)T^{10}
\le-0.0943T^{10}.
\]

这与 (3) 相比有超过 `10^16` 的安全余量，因此

\[
R<0,
\]

不可能是整数平方。

故 exact candidate 必须满足

\[
\boxed{\sigma<0.250261.}
\tag{4}
\]

---

## 3. 传入 Pell descent 的单调主函数

本 family 有

\[
w=1,
\quad C_0=9,
\quad\Gamma=22,
\quad c=2,
\quad r=11.
\]

central Pell note 使用

\[
L=T/c,
\qquad s=N_0/L=c\sigma.
\]

所以 (4) 给

\[
\boxed{s<0.500522.}
\tag{5}
\]

而 Euclidean descent 中已严格证明

\[
U>f(s),
\qquad
f(s)=C_0s+\frac{1000c^4r^2}{s}.
\tag{6}
\]

并且 `f` 在整个允许区间严格递减。由 (5)：

\[
U>f(0.500522).
\]

精确有理数计算为

\[
f(0.500522)
=\frac{44000051243192099}{11375500000}
=3867966.3525\ldots
\]

所以整数 `U` 必满足

\[
\boxed{U\ge3,867,967.}
\tag{7}
\]

相比此前只由 coarse decade 得到的

\[
U>968018,
\]

低端被删除了约三百万个整数。

---

## 4. 对 `t=U-U_0` 的直接结果

这里

\[
U_0=10c\Gamma(20w-1)
=8360.
\]

所以

\[
\boxed{t=U-U_0\ge3,859,607.}
\tag{8}
\]

另一方面原 k-independent upper window 不变，故该 crossing family 后续的 local-square / Pell 搜索应从 (7)-(8) 开始，不再扫描旧的 `[~0.96M,~9.68M]` 全窗。
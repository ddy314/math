# A1 top-layer minimal diagonal valuation normal form — 2026-08-17

本文继续最小双 surplus diagonal，并结合 `k=g=1,2` 两个有限证书，把剩余无界部分统一置于

\[
\boxed{k=g\ge3.}
\]

在这一范围，六个 `(z,w)` 类型的 `2/5`-进前缀结构完全稳定，两个 primitive cross-corridor 上界都精确退化成同一个整数 `k`。

核心结论：

\[
\boxed{v_5(K)=0,}
\]

\[
\boxed{v_2(K)=2v_2(w),}
\]

以及

\[
\boxed{X_0=Y_0=k.}
\]

本文结论均为 **已严格完成**。

---

## 1. minimal diagonal 数据

当前范围为

\[
d=2,
\qquad r=s=1,
\qquad k=g\ge3.
\]

因此

\[
\boxed{b_2=1,}
\]

\[
\boxed{b_1=10^{2k+1}-w,}
\]

\[
\boxed{a_2=10^{2k+1}-z,}
\]

其中

\[
(z,w)
\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\}.
\]

又

\[
Q=10b_1+1,
\qquad
G=b_1,
\qquad
D=10^kQ.
\]

第二分子位数为

\[
n_2=2k+1,
\]

所以

\[
C=a_1 10^{2k+1}+a_2.
\]

---

## 2. `Q,C,G` 的 `2/5` 赋值

因为

\[
Q=10b_1+1,
\]

立即有

\[
\boxed{v_2(Q)=v_5(Q)=0.}
\tag{1}
\]

又 `a_2` 的末位为 `9` 或 `7`，而第一项 `a_1 10^{2k+1}` 同时被 `2,5` 整除，因此

\[
C\equiv a_2\pmod{10}.
\]

所以

\[
\boxed{v_2(C)=v_5(C)=0.}
\tag{2}
\]

对

\[
G=b_1=10^{2k+1}-w,
\]

六类型中 `1\le w\le4`。由于

\[
v_2(10^{2k+1})=2k+1>v_2(w),
\]

有

\[
\boxed{v_2(G)=v_2(w)\in\{0,1,2\}.}
\tag{3}
\]

同时 `w` 不被 `5` 整除，故

\[
\boxed{v_5(G)=0.}
\tag{4}
\]

由 (1)：

\[
\boxed{v_2(D)=v_5(D)=k.}
\tag{5}
\]

---

## 3. `N` 的二进结构

这里

\[
N=a_1^2+(a_2b_1)^2.
\]

若 `w` 为偶数，则 `b_1` 为偶数。原问题有

\[
\gcd(a_1,b_1)=1,
\]

所以 `a_1` 必为奇数，而第二项为偶平方。因此

\[
\boxed{w\text{ 偶}\Longrightarrow v_2(N)=0.}
\tag{6}
\]

若 `w` 为奇数，则 `b_1,a_2` 均为奇数。

- `a_1` 偶时，`N` 为奇数；
- `a_1` 奇时，两项均为 `1 mod 4`，所以
  \[
  N\equiv2\pmod4.
  \]

因此全局有

\[
\boxed{v_2(N)\in\{0,1\}.}
\tag{7}
\]

---

## 4. `K` 的五进赋值恒为零

定义

\[
K=G^2C^2-D^2N.
\]

由 (2)、(4)：

\[
v_5(G^2C^2)=0.
\]

而由 (5)：

\[
v_5(D^2N)\ge2k\ge6.
\]

两项赋值不同，所以

\[
\boxed{v_5(K)=0.}
\tag{8}
\]

---

## 5. `K` 的二进赋值等于 `2v_2(w)`

令

\[
e=v_2(w)=v_2(G)\in\{0,1,2\}.
\]

由 (2)：

\[
v_2(G^2C^2)=2e\le4.
\]

另一方面由 (5)、(7)：

\[
v_2(D^2N)=2k+v_2(N)\ge6.
\]

因此仍是严格不同赋值，低侧由第一项唯一承担：

\[
\boxed{v_2(K)=2e=2v_2(w).}
\tag{9}
\]

所以六类型只有

\[
v_2(K)=
\begin{cases}
0,&w=1,3,\\
2,&w=2,\\
4,&w=4.
\end{cases}
\]

这里 `k\ge3` 很重要；`k=2,w=4` 时两个主项可能在同一二进深度相遇，因此已经被单独的有限证书处理。

---

## 6. resonance lines

normalized tail 写成

\[
\rho=h2^x5^y.
\]

二进 resonance line 为

\[
x_*
=v_2(K)-\left(1+v_2(D)+v_2(N)\right).
\]

所以

\[
\boxed{
 x_*=2v_2(w)-1-k-v_2(N).
}
\tag{10}
\]

五进 resonance line 为

\[
y_*
=v_5(K)-v_5(D)-v_5(N),
\]

故

\[
\boxed{
 y_*=-k-v_5(N).
}
\tag{11}
\]

---

## 7. 两个 primitive cross-corridor cap 都等于 `k`

旧 primitive cross-corridor 公式为

\[
X_0=
\max\left(
0,
 d_2,
 d_2+\frac{k_2}{2}-g_2-c_2,
 d_2+g_2-\frac{k_2}{2}
\right),
\]

其中

\[
d_2=k,
\quad
k_2=2e,
\quad
g_2=e,
\quad c_2=0.
\]

所以后两项都恰为 `k`：

\[
d_2+\frac{k_2}{2}-g_2-c_2=k+e-e=k,
\]

\[
d_2+g_2-\frac{k_2}{2}=k+e-e=k.
\]

因此

\[
\boxed{X_0=k.}
\tag{12}
\]

五进同理：

\[
d_5=k,
\quad k_5=0,
\quad g_5=c_5=0,
\]

故

\[
\boxed{Y_0=k.}
\tag{13}
\]

---

## 8. 当前意义

minimal diagonal 的六个 prefix 类型虽然在十进制外形上不同，但 `2/5`-进 tail geometry 在 `k\ge3` 已经统一成：

\[
\boxed{
X_0=Y_0=k,
}
\]

配合 resonance lines

\[
x_*=2v_2(w)-1-k-v_2(N),
\]

\[
y_*=-k-v_5(N).
\]

所以：

- `2+5-` cross corridor 中一旦 `x>k` 就不可能；
- `2-5+` cross corridor 中一旦 `y>k` 就不可能；
- 五进前缀没有任何隐藏的 `5`-adic supply，因为 `v_5(K)=0`；
- 二进前缀只由绝对小常数 `w` 的赋值决定。

这为把 diagonal significand lock 与 tail resonance/cross-corridor 系统直接耦合提供了统一入口。

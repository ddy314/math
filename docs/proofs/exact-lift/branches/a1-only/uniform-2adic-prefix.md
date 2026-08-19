# A1 minimal diagonal: uniform 2-adic prefix theorem

> 日期：2026-08-19。本文补充 `uniform-layer-finite-box.md` 中的 2-adic 部分。
> 当前范围
> \[
> d=2,\qquad r=s=1,\qquad k=g\ge3.
> \]

核心结论：2-adic prefix valuation 根本不需要 root lifting。对所有合法 prefix，

\[
\boxed{
 w\text{ even}\Longrightarrow v_2(N)=0,
}
\tag{1}
\]

\[
\boxed{
 w\text{ odd}\Longrightarrow v_2(N)\le1.
}
\tag{2}
\]

因此 resonance threshold

\[
x_*=2v_2(w)-1-k-v_2(N)
\]

在六类型上的全局精确 floor 为

\[
\boxed{
\underline x_*(k)=-k-2.
}
\tag{3}
\]

状态：**已严格完成。**

---

## 1. 输入

minimal diagonal 中

\[
b_1=10^{2k+1}-w,
\qquad
a_2=10^{2k+1}-z,
\]

其中 `z` 始终为奇数，`w in {1,2,3,4}`，并且原问题始终带有

\[
\gcd(a_1,b_1)=1.
\tag{4}
\]

定义

\[
N=a_1^2+(a_2b_1)^2.
\tag{5}
\]

又因为 `2k+1>v_2(w)`，有

\[
v_2(b_1)=v_2(w).
\tag{6}
\]

同时 `a_2` 为奇数。

---

## 2. `w` 为偶数时 `N` 必为奇数

若 `w` 偶，则由 (6) `b_1` 为偶数。

结合 (4)，`a_1` 必为奇数。因此

\[
a_1^2\equiv1\pmod2,
\]

而

\[
(a_2b_1)^2\equiv0\pmod2.
\]

所以

\[
N\equiv1\pmod2,
\]

即

\[
\boxed{v_2(N)=0.}
\tag{7}
\]

这同时覆盖 `w=2` 与 `w=4`。

---

## 3. `w` 为奇数时 `v_2(N)` 至多为 1

若 `w` 奇，则 `b_1` 与 `a_2` 都为奇数，所以 `a_2b_1` 为奇数。

### `a_1` 偶

此时

\[
a_1^2\equiv0\pmod2,
\qquad
(a_2b_1)^2\equiv1\pmod2,
\]

故 `N` 为奇数：

\[
v_2(N)=0.
\]

### `a_1` 奇

任意奇数平方都满足

\[
x^2\equiv1\pmod8.
\]

因此

\[
N=a_1^2+(a_2b_1)^2\equiv1+1\equiv2\pmod8.
\]

所以此时恰有

\[
v_2(N)=1.
\]

综上：

\[
\boxed{w\text{ odd}\Longrightarrow v_2(N)\in\{0,1\}.}
\tag{8}
\]

---

## 4. resonance threshold 的闭式

已有

\[
x_*=2v_2(w)-1-k-v_2(N).
\tag{9}
\]

逐 `w` 得：

### `w=1,3`

`v_2(w)=0` 且 `v_2(N)<=1`，所以

\[
x_*\ge-k-2.
\tag{10}
\]

而允许 `a_1` 为奇的 prefix 确实可达到 `v_2(N)=1`，故这一 floor 是 sharp 的。

### `w=2`

`v_2(w)=1` 且由 (7) `v_2(N)=0`：

\[
\boxed{x_*=1-k.}
\tag{11}
\]

### `w=4`

`v_2(w)=2` 且 `v_2(N)=0`：

\[
\boxed{x_*=3-k.}
\tag{12}
\]

因此六类型统一的最小 threshold 为

\[
\boxed{\underline x_*(k)=-k-2.}
\tag{13}
\]

---

## 5. 对 fixed-layer certificate 的意义

`uniform-layer-finite-box.md` 原先通过模 `2^e` root lifting 计算每一层的 `x* floor`。本文说明该步骤可以永久删除：

\[
\boxed{x\text{-floor 直接写成 }-k-2.}
\]

以后只有 `5`-adic threshold

\[
y_*=-k-v_5(N)
\]

仍需要 root lifting 或进一步的统一解析估计。

此外 even-`w` 类型拥有比全局 floor 强得多的具体 threshold `(1-k)` 与 `(3-k)`，后续若需要做 typewise gap-desert 证明，应优先保留这一额外余量。
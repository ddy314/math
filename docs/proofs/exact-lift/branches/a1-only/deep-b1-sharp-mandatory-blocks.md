# A1 minimal diagonal: sharpened mandatory `b_1` complement blocks

> 日期：2026-08-20。强化 `deep-b1-block-loss.md`。本文只研究 whole-block selector 本身，因此结论可用于所有需要 `s|b_1` supply 的 deep sectors。

最终 prefix-uniform minima：

\[
\boxed{u=b_1/s\ge(27,38,1,12)}
\]

按 `w=1,2,3,4`。

状态：**已严格完成。**

---

## 1. `w=1`：universal complement 至少 27

\[
b_1=10^{2k+1}-1.
\]

令

\[
n=2k+1
\]

为奇数。LTE 对 p=3：

\[
\boxed{
v_3(b_1)=v_3(10^n-1)=2+v_3(n).}
\tag{1}

整个 3-primary block 都是 `3 mod4` prime-power source，不能进入 selector s。

分 parity。

### `v_3(n)` 为奇数

则

\[
2+v_3(n)\ge3,
\]

所以

\[
\boxed{27\mid u.}
\tag{2}

### `v_3(n)` 为偶数

此时 3-primary exponent

\[
2+v_3(n)
\]

为偶数，所以整个 3-block本身

\[
3^{2+v_3(n)}\equiv1\pmod4.
\]

但

\[
b_1\equiv-1\equiv3\pmod4.
\]

因此 b1 中必须存在另一个 `p=3 mod4` prime-power block以 odd parity贡献。

排除所有小于 31 的候选：

\[
\operatorname{ord}_7(10)=6,
\quad
\operatorname{ord}_{11}(10)=2,
\quad
\operatorname{ord}_{19}(10)=18,
\quad
\operatorname{ord}_{23}(10)=22.
\]

这些 order 全为偶数，不可能整除 odd exponent n，因此

\[
7,11,19,23\nmid10^n-1.
\]

所以这个额外 `3 mod4` prime至少为 31。又 3-primary block 至少为 9：

\[
\boxed{u\ge9\cdot31=279}
\tag{3}

在该 parity branch。

综合 (2)-(3)：

\[
\boxed{w=1:\quad u\ge27.}
\tag{4}

因此

\[
\boxed{s\le b_1/27.}
\tag{5}

该界可达其数量级：例如 n=3 时 `10^3-1=3^3*37`，3-mod-4 complement 正好包含 27。

---

## 2. `w=2`：mandatory `3 mod4` odd prime 至少是 19

\[
b_1=10^{2k+1}-2.
\]

模 8：

\[
b_1\equiv6\pmod8,
\]

故

\[
\boxed{v_2(b_1)=1.}
\]

写

\[
b_1=2m.
\]

则

\[
\boxed{m\equiv3\pmod4.}
\]

所以 m 中至少有一个 `p=3 mod4` odd prime-power block以 odd parity贡献。

排除 3,7,11：

- `p=3`: `b_1=1-2=-1 mod3`；
- `p=7`: `10^(2k+1)=3*2^k mod7`，等于 2 会要求 `2^k=3 mod7`，不可能；
- `p=11`: odd exponent 给 `10^(2k+1)=-1 mod11`，所以 `b_1=-3 mod11`。

因此 mandatory odd prime至少 19，整个 block留在 u：

\[
\boxed{w=2:\quad u\ge2\cdot19=38.}
\tag{6}

所以

\[
\boxed{s\le b_1/38.}
\tag{7}

---

## 3. `w=3,4`

`w=3`：目前没有 prefix-uniform mandatory `3 mod4` odd block，安全保留

\[
\boxed{u\ge1.}
\]

`w=4`：

\[
v_2(b_1)=2,
\qquad v_3(b_1)=1,
\]

所以

\[
\boxed{u\ge12,}
\qquad
\boxed{s\le b_1/12.}
\]

---

## 4. final structural minima

\[
\boxed{
(c_1,c_2,c_3,c_4)=(27,38,1,12).}
\tag{8}

以后所有仅依赖 mandatory `b_1` complement 的 supply bounds 应使用 (8)，而不再使用历史粗值 `(3,14,1,12)` 或中间值 `(9,38,1,12)`。

# A1 minimal diagonal: sharpened mandatory `b_1` complement blocks

> 日期：2026-08-20。强化 `deep-b1-block-loss.md`。本文只研究 whole-block selector 本身，因此结论可用于所有需要 `s|b_1` supply 的 deep sectors。

旧统一 minima 为

\[
u=b_1/s\ge(3,14,1,12)
\]

按 `w=1,2,3,4`。本文把前两型严格提高为

\[
\boxed{u\ge(9,38,1,12).}
\]

状态：**已严格完成。**

---

## 1. `w=1`：完整 3-primary block 至少是 `3^2`

\[
b_1=10^{2k+1}-1.
\]

令

\[
n=2k+1
\]

为奇数。LTE 对 p=3：

\[
v_3(10^n-1)
=v_3(10-1)+v_3(n).
\]

而

\[
v_3(9)=2.
\]

所以

\[
\boxed{
v_3(b_1)=2+v_3(2k+1)\ge2.}
\tag{1}

因为 `3=3 mod4`，整个 `3^(2+v3(2k+1))` block 都不能进入 selector `s`，必须留在 complement `u=b_1/s`。

因此

\[
\boxed{9\mid u,\qquad u\ge9.}
\tag{2}

旧的 `u>=3` / `s<=b_1/3` 可统一加强为

\[
\boxed{s\le b_1/9.}
\tag{3}

---

## 2. `w=2`：mandatory `3 mod4` odd prime 至少是 19

这里

\[
b_1=10^{2k+1}-2.
\]

当前 `k>=32`，当然指数至少 3；模 8：

\[
b_1\equiv-2\equiv6\pmod8.
\]

所以

\[
\boxed{v_2(b_1)=1.}
\]

写

\[
b_1=2m,
\]

则

\[
\boxed{m\equiv3\pmod4.}
\tag{4}

所以 m 的 prime-power factorization 中至少存在一个 `p=3 mod4` block以奇 parity贡献；该完整 block不能进入 s。

现在排除前三个 `3 mod4` primes。

### p=3

\[
b_1\equiv1-2\equiv-1\not\equiv0\pmod3.
\]

### p=7

`10 mod7=3`，且

\[
10^{2k+1}
=3(3^2)^k
\equiv3\cdot2^k\pmod7.
\]

若 `7|b_1`，则

\[
3\cdot2^k\equiv2\pmod7,
\]

即

\[
2^k\equiv3\pmod7.
\]

但 powers of 2 mod7 只循环于

\[
1,2,4,
\]

矛盾。所以

\[
\boxed{7\nmid b_1.}
\]

### p=11

指数 `2k+1` 为奇数，而

\[
10\equiv-1\pmod{11}.
\]

所以

\[
10^{2k+1}-2\equiv-3\not\equiv0\pmod{11}.
\]

因此 mandatory `3 mod4` odd prime至少为

\[
\boxed{19.}
\]

结合 fixed factor 2：

\[
\boxed{u\ge2\cdot19=38.}
\tag{5}

即

\[
\boxed{s\le b_1/38.}
\tag{6}

注意本文不声称 19 必须整除每个 `b_1`；只需要“某个 mandatory `3 mod4` prime存在且不可能小于 19”。

---

## 3. 其余两型

`w=3`：目前没有 prefix-uniform mandatory `3 mod4` odd block，所以安全保留

\[
\boxed{u\ge1.}
\]

`w=4`：已有

\[
v_2(b_1)=2,
\qquad v_3(b_1)=1,
\]

所以

\[
\boxed{12\mid u,\qquad u\ge12.}
\]

---

## 4. 新 structural minima

综上：

\[
\boxed{
(c_1,c_2,c_3,c_4)=(9,38,1,12),}
\tag{7}

其中

\[
u\ge c_w,
\qquad s\le b_1/c_w.
\]

这些 sharpened constants 应替换后续所有只依赖 mandatory `b_1` block 的旧 `(3,14,1,12)` 粗界。

# A1 minimal diagonal: joint complement minimum for `w=1`

> 日期：2026-08-20。依赖 `deep-b1-sharp-mandatory-blocks.md` 与 strict-2 Q-side orientation。本文适用于 surviving double-deep 2-high master。

单独看 structural minima 只能得到 `u>=27`,`v>=7`，即 `M=uv>=189`。本文利用它们各自的 decimal divisibility period不能同时取到最弱值，严格提高为

\[
\boxed{w=1:\quad M=uv\ge621.}
\]

状态：**已严格完成。**

---

## 1. 3-primary branch of `u`

写

\[
n=2k+1,
\qquad r_3=v_3(n).
\]

LTE：

\[
v_3(b_1)=2+r_3.
\]

### r3 odd

若 `r3=1`：

\[
\boxed{u\ge27.}
\tag{1}

若 `r3>=3`：

\[
u\ge3^5=243.
\tag{2}

### r3 even

3-primary block exponent为偶数；因 `b1=3 mod4`，还需要另一个 `3 mod4` block，最小 prime至少 31。所以：

- `r3=0`: `u>=9*31=279`；
- `r3>=2`: 更大，至少 `3^4*31=2511`。

---

## 2. v 的 small `3 mod4` primes

strict-2 orientation给

\[
v=Q/q\equiv3\pmod4.
\]

而 `3 not|Q`、`11 not|Q` 对 w=1 恒成立。

### p=7

\[
Q=10^{2k+2}-9.
\]

模 7：

\[
10^2\equiv2,
\qquad9\equiv2.
\]

所以

\[
7\mid Q
\iff2^{k+1}\equiv2\pmod7
\iff2^k\equiv1\pmod7
\iff\boxed{k\equiv0\pmod3.}
\tag{3}

此时

\[
n=2k+1\equiv1\pmod3,
\]

故 `r3=0`，于是由上一节

\[
\boxed{7\mid v\Longrightarrow u\ge279.}
\tag{4}

因此该 branch：

\[
uv\ge279\cdot7=1953.
\]

### p=19

`ord_19(10)=18`，且直接计算

\[
10^{10}\equiv9\pmod{19}.
\]

所以

\[
19\mid Q
\iff2k+2\equiv10\pmod{18}
\iff\boxed{k\equiv4\pmod9.}
\tag{5}

于是

\[
n=2k+1\equiv9\pmod{18},
\]

特别地

\[
9\mid n,
\qquad r_3\ge2.
\tag{6}

因此 `r3=1` branch 不可能使用 p=19 作为 v 的 `3 mod4` source。

---

## 3. 分支合并

### r3=1

此时 `k=1 mod3`，所以由 (3) `7 not|Q`；又由 (5)-(6)，`19 not|Q`。

加上 universal `3,11 not|Q`，v 中 mandatory `3 mod4` prime至少是下一个

\[
\boxed{23.}
\]

结合 u>=27：

\[
\boxed{uv\ge27\cdot23=621.}
\tag{7}

### r3=0

u>=279，而 v>=7：

\[
uv\ge1953>621.
\]

### r3>=2

若 r3 odd，u>=243，而 k=1 mod3，所以 7 absent，v>=19：

\[
uv\ge243\cdot19>621.
\]

若 r3 even，u>=2511，显然更大。

综上：

\[
\boxed{M=uv\ge621.}
\tag{8}

---

## 4. immediate denominator cap

complement height：

\[
MD/T^2<10001.
\]

所以

\[
\boxed{
D<\frac{10001}{621}T^2<17T^2.}
\tag{9}

这应替换 `deep-2high-denominator-cap.md` 中 w=1 仅用独立 minima 得到的 `159T^2`；真正 joint cap 是 17。

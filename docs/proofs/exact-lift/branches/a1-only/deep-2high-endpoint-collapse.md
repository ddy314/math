# A1 minimal diagonal: top 2-high endpoint collapse

> 日期：2026-08-20。依赖 `deep-b1-sharp-mandatory-blocks.md`、`deep-2high-denominator-cap.md` 与 `deep-double-2high-master.md`。当前 `k>=32`。

当

\[
\delta:=D/T^2
\]

靠近 typewise denominator cap 时，complement product

\[
M=uv<10001/\delta
\]

变成很小的整数。结合 sharpened mandatory blocks、`v` orientation 与 `gcd(u,v)=1`，top endpoint 的 complementary divisors 被唯一锁死。

状态：**已严格完成。**

---

## 1. sharp structural minima

因为

\[
u\mid b_1,
\qquad v\mid Q,
\qquad\gcd(b_1,Q)=1,
\]

有

\[
\boxed{\gcd(u,v)=1.}
\tag{1}

sharpened minima：

\[
\boxed{
\begin{array}{c|c|c|c}
w&u_{\min}&v_{\min}&M_{\min}\\ \hline
1&9&7&63\\
2&38&3&114\\
3&1&7&7\\
4&12&7&84
\end{array}}
\tag{2}

其中 `w=1` 的 `u>=9` 来自 `v3(b1)>=2`；`w=2` 的 `u>=38` 来自 mandatory `3 mod4` odd prime至少 19。

---

## 2. next possible complement product

可安全取：

\[
\boxed{
\begin{array}{c|c}
w&M_{\rm next}\\ \hline
1&99\\
2&186\\
3&11\\
4&132
\end{array}}
\tag{3}

说明：

### w=1

`u` 是 odd multiple of完整 `3^e` block，至少 9；`v>=7`, `v=3 mod4`, 且 `3 not|Q`。

minimum：

\[
9\cdot7=63.
\]

若不取 `(9,7)`，最小下一可能是

\[
9\cdot11=99
\]

（而下一 3-power `27*7=189` 更大）。

### w=2

`u` 必含 fixed 2 与一个至少 19 的 `3 mod4` odd block，所以 minimum `u=38`; `v>=3`。

minimum：

\[
38\cdot3=114.
\]

若 mandatory odd block不是 19，则下一个可能至少 31，故 `u>=62`, 与 `v=3` 给

\[
62\cdot3=186.
\]

另一方面保留 `u=38` 而把 `v` 提到下一个 `3 mod4` unit至少 7，得到 266，更大。所以 next product可取 186。

### w=3

保留 `M_next=11`。

### w=4

保留 `M_next=132`。

---

## 3. sharpened endpoint thresholds

若

\[
\delta>10001/M_{\rm next},
\]

则

\[
M<M_{\rm next}.
\]

结合 `M>=M_min`，只能取 minimum pair。

取整洁 safe thresholds：

\[
\boxed{
\frac D{T^2}>
\begin{cases}
102,&w=1,\\
54,&w=2,\\
910,&w=3,\\
76,&w=4
\end{cases}}
\Longrightarrow
(u,v)=
\begin{cases}
(9,7),&w=1,\\
(38,3),&w=2,\\
(1,7),&w=3,\\
(12,7),&w=4.
\end{cases}}
\tag{4}

注意 `w=2` 的 top endpoint 已从旧 threshold 152 大幅降到 54，而其整个 denominator cap 只有 88。

---

## 4. fixed-coefficient S-unit equations

master complement：

\[
2\beta u-\alpha v=5^d.
\]

代入 (4)：

\[
\boxed{
\begin{array}{c|c}
w&\text{endpoint equation}\\ \hline
1&18\beta-7\alpha=5^d\\
2&76\beta-3\alpha=5^d\\
3&2\beta-7\alpha=5^d\\
4&24\beta-7\alpha=5^d
\end{array}}
\tag{5}

并仍有

\[
\alpha\beta=r_{10},
\qquad\gcd(\alpha,\beta)=1.
\]

---

## 5. supply equation 统一简化

endpoint 中

\[
q=Q/v,
\qquad s=b_1/u,
\qquad M=uv.
\]

master supply

\[
\beta q-5\alpha s=2^cn_0
\]

乘 `uv`：

\[
\beta uQ-5\alpha vb_1=M2^cn_0.
\]

利用

\[
Q=10b_1+1,
\qquad2\beta u-\alpha v=5^d,
\]

得到统一恒等式

\[
\boxed{
5^{d+1}b_1+\beta u
=M2^cn_0.}
\tag{6}

其中 `u,v,M` 现在只依赖 w。

---

## 6. periodic divisibility入口

固定 pairs 还要求：

\[
u\mid b_1,
\qquad v\mid Q.
\]

例如：

- `w=1`: `u=9` 自动整除 `b_1`; `v=7` 强迫 `k mod3` 的一个固定 class；
- `w=2`: `u=38` 强迫 `19|b_1`，因此 k 落在 mod9 的固定 class；`v=3` 自动可行；
- `w=3`: `v=7` 给一个 mod3 class；
- `w=4`: `u=12` 自动，`v=7` 给一个 mod3 class。

所以 top endpoint 已是 fixed coefficient + short-period k classes，适合下一步对 (5)-(6) 做 2-adic/periodic exhaustion。

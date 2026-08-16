# A1 inert-prime routing — 2026-08-16

本文从 universal denominator funnel 与整数平方证书推出一个覆盖整个 A1 的奇素数流向规则。

核心结论：

\[
\boxed{
p\equiv3\pmod4,\ p\mid b_3
\Longrightarrow
p\mid Q.
}
\]

也就是说，第三分母中的 Gaussian inert 奇素数不能只从 `G=b_1b_2` 的单侧 denominator 因子流入；它们全部必须被前两分母拼接 `Q=b_1 10^{m_2}+b_2` 支撑。

本文结论为 **已严格完成**。

---

## 1. 两个已知输入

A1 universal denominator certificate 为

\[
\boxed{
b_3\mid T^2D^2G,}
\]

其中

\[
T=10^\ell,
\qquad
D=10^gQ,
\qquad
G=b_1b_2.
\]

所以对任意奇素数 `p\ne5`：

\[
p\mid b_3
\Longrightarrow
p\mid QG.
\tag{1}
\]

另一方面 universal integer-square certificate 为

\[
\boxed{
W^2=T^2K-2Tb_3DN,
}
\tag{2}
\]

其中

\[
K=G^2C^2-D^2N,
\]

\[
N=(a_1b_2)^2+(a_2b_1)^2.
\]

---

## 2. 反设一个 inert prime 不整除 `Q`

令

\[
\boxed{p\equiv3\pmod4}
\]

且

\[
p\mid b_3.
\]

这样的 `p` 自动满足

\[
p\ne2,5,
\]

所以

\[
p\nmid T.
\]

反设

\[
\boxed{p\nmid Q.}
\tag{3}
\]

由 (1)，必有

\[
p\mid G=b_1b_2.
\]

而 `p\nmid Q` 又强迫 `p` 不可能同时整除 `b_1,b_2`：若同时整除，则当然 `p\mid Q`。

所以 `p` 恰好整除 `b_1,b_2` 中一个。

---

## 3. 若 `p\mid b_1,\ p\nmid b_2`

因为

\[
\gcd(a_1,b_1)=1,
\]

有

\[
p\nmid a_1.
\]

模 `p`：

\[
G^2C^2\equiv0,
\]

\[
Q=b_1 10^{m_2}+b_2\equiv b_2,
\]

所以

\[
D=10^gQ\equiv10^gb_2.
\]

又

\[
N
=(a_1b_2)^2+(a_2b_1)^2
\equiv(a_1b_2)^2.
\]

因此

\[
\boxed{
K
\equiv
-10^{2g}a_1^2b_2^4
=-(10^g a_1b_2^2)^2
\pmod p.
}
\tag{4}
\]

右侧是一个**非零负平方**，因为

\[
p\nmid10a_1b_2.
\]

---

## 4. 若 `p\mid b_2,\ p\nmid b_1`

同理由

\[
\gcd(a_2,b_2)=1
\]

得到

\[
p\nmid a_2.
\]

记

\[
M=10^{m_2}.
\]

模 `p`：

\[
Q\equiv b_1M,
\qquad
D\equiv10^gb_1M,
\]

\[
N\equiv(a_2b_1)^2.
\]

所以

\[
\boxed{
K
\equiv
-(10^g M a_2 b_1^2)^2
\pmod p,
}
\tag{5}
\]

同样是非零负平方。

---

## 5. 平方证书强迫 `K` 同时成为平方

由于

\[
p\mid b_3,
\]

整数平方证书 (2) 模 `p` 化成

\[
W^2\equiv T^2K\pmod p.
\]

而

\[
p\nmid T.
\]

所以

\[
\boxed{K\text{ 是模 }p\text{ 的平方剩余}.}
\tag{6}
\]

但由 (4) 或 (5)，在反设 `p\nmid Q` 下

\[
K\equiv-\xi^2\pmod p
\]

且 `\xi\not\equiv0\pmod p`。

因此 (6) 强迫

\[
-1
\]

是模 `p` 的平方剩余。

这与

\[
p\equiv3\pmod4
\]

矛盾。

所以反设 (3) 不成立。

由此得到

\[
\boxed{
p\equiv3\pmod4,\ p\mid b_3
\Longrightarrow
p\mid Q.}
\tag{7}
\]

---

## 6. 两个等价表述

若记第三分母的 `3 mod 4` radical 为

\[
\operatorname{rad}_{3(4)}(b_3)
=
\prod_{\substack{p\mid b_3\\p\equiv3(4)}}p,
\]

则

\[
\boxed{
\operatorname{rad}_{3(4)}(b_3)\mid Q.
}
\tag{8}
\]

另一方面，denominator funnel 原本只有

\[
\operatorname{rad}_{\mathrm{odd}}(b_3)
\mid\operatorname{rad}(QG).
\]

现在对 inert primes 可强化成：

\[
\boxed{
\text{所有 }3\bmod4\text{ 奇素数只能从 }Q\text{ 通道进入 }b_3.
}
\]

因此 `G` 中只出现在 `b_1` 或 `b_2` 单侧的 inert prime，不能再成为第三分母的 prime supply。

---

## 7. 与安全 integer-gap 的后续接口

安全球面 gap 有

\[
LA(H+y_3)=y_1^2+y_2^2.
\]

对 `p\equiv3\pmod4`，若 `p` 进一步进入 `LA`，二平方和性质会迫使 `p` 同时进入 `y_1,y_2`。

因此 (7) 给出了下一步局部分析的第一半：第三分母的 inert prime 已先被路由到 `Q`；随后可以把它在 `Q`、`A`、`y_1,y_2` 之间的赋值继续联立。

本文只记录已经严格完成的 routing 结论，不提前声称该局部链已经关闭整个 A1。
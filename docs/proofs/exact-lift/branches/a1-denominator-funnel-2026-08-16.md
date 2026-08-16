# A1 universal denominator funnel — 2026-08-16

本文件继续 `a1-rational-contact-framework-2026-08-16.md`，从其中的 universal rational-contact 判别式推出一个覆盖 saturated 与 non-saturated 的整数平方证书和第三分母 prime-supply 约束。

以下各节均为 **已严格完成**，最后一节列出尚未关闭的无界核心。

---

## 1. 记号

沿用 A1 rational-contact 框架：

\[
T=10^\ell=10^{n_3},
\qquad
D=10^gQ,
\]

\[
C=a_1 10^{n_2}+a_2,
\qquad
G=b_1b_2,
\]

\[
N=\mathcal N_{12}
=(a_1b_2)^2+(a_2b_1)^2,
\]

\[
P=\frac CD,
\qquad
S=\frac N{G^2},
\]

以及

\[
\theta=\frac{b_3}{TD}.
\]

记

\[
\boxed{K=G^2C^2-D^2N}.
\]

A1 rational-contact 判别平方是

\[
\Xi=P^2-(1+2\theta)S=z^2
\]

对某个 `z\in\mathbf Q_{\ge0}`。

---

## 2. universal integer-square certificate

直接代入 `P,S,\theta`：

\[
\Xi
=
\frac{C^2}{D^2}
-
\left(1+\frac{2b_3}{TD}\right)\frac N{G^2}.
\]

通分得到

\[
\boxed{
\Xi
=
\frac{TK-2b_3DN}{T D^2G^2}.
}
\]

因此

\[
z^2
=
\frac{TK-2b_3DN}{T(DG)^2}.
\]

两边乘以 `T^2D^2G^2`：

\[
(zTDG)^2
=T(TK-2b_3DN).
\]

右侧是整数；有理数的平方若为整数，则该有理数本身为整数。因此存在整数 `W\ge0` 满足

\[
\boxed{
W=zTDG
}
\]

以及

\[
\boxed{
W^2
=T(TK-2b_3DN)
=T^2K-2Tb_3DN.
}
\]

这是覆盖整个 A1 的整数平方证书。

特别地必须有

\[
\boxed{TK-2b_3DN\ge0}.
\]

因为

\[
b_3\ge10^{m_3-1}=10^{g+\ell-1}=10^{g-1}T,
\]

故得到纯前缀必要条件

\[
TK
\ge
2\cdot10^{g-1}T\cdot D N,
\]

即

\[
\boxed{
K\ge2\cdot10^{2g-1}QN.
}
\]

这与 rational-contact 框架中的

\[
P^2\ge\left(1+\frac1{5Q}\right)S
\]

完全等价。

---

## 3. universal root formula

由

\[
\Xi=z^2=\left(\frac{W}{TDG}\right)^2
\]

以及

\[
r_3
=
\frac{\theta P\pm(1+\theta)z}{1+2\theta}
\]

代入

\[
\theta=\frac{b_3}{TD},
\qquad
P=\frac CD,
\]

得到

\[
\boxed{
 r_3
=
\frac{
TG b_3 C
\pm
(TD+b_3)W
}{
TDG(TD+2b_3)
}.
}
\]

原问题中

\[
r_3=\frac{a_3}{b_3}
\]

已经既约，因此其既约分母 `b_3` 必须整除上述整数分母：

\[
\boxed{
 b_3\mid TDG(TD+2b_3).
}
\]

展开右侧并模 `b_3` 化简：

\[
TDG(TD+2b_3)
\equiv
T^2D^2G
\pmod{b_3}.
\]

于是得到更干净的 universal denominator certificate：

\[
\boxed{
 b_3\mid T^2D^2G.
}
\]

由于

\[
T=10^\ell,
\qquad
D=10^gQ,
\]

还可写成

\[
\boxed{
 b_3\mid10^{2m_3}Q^2G.
}
\]

这里使用了 `m_3=g+\ell`。

---

## 4. 第三分母的非十进制 prime supply 被前缀完全控制

令

\[
b_3=2^u5^v h,
\qquad
\gcd(h,10)=1.
\]

由

\[
b_3\mid10^{2m_3}Q^2G
\]

立刻得到

\[
\boxed{h\mid Q^2G}.
\]

更逐素数地，对每个奇素数 `p\ne5`，

\[
\boxed{
 v_p(b_3)
\le
2v_p(Q)+v_p(G).
}
\]

所以 A1 中第三分母的所有非 `2,5` 素数以及其指数，都由前两块的

\[
Q^2G
\]

控制。

这比“固定前缀下第三分母只有有限新奇素数”更具体：第三分母一定处在

\[
\boxed{
 b_3=h2^u5^v,
\qquad
h\mid Q^2G,
\quad\gcd(h,10)=1
}
\]

这一 near-`S`-unit funnel 中。

固定前缀后 `h` 只有有限多个选择；所有无界性只能来自 `2`、`5` 指数 `u,v`。

---

## 5. 2/5-adic parity split

整数平方证书

\[
W^2=T(TK-2b_3DN)
\]

对 `p\in\{2,5\}` 给出直接的赋值奇偶约束。

记

\[
e_p=v_p(TK)=\ell+v_p(K).
\]

再记

\[
f_2=v_2(2b_3DN)
=1+u+g+v_2(Q)+v_2(N),
\]

\[
f_5=v_5(2b_3DN)
=v+g+v_5(Q)+v_5(N).
\]

若 `e_p\ne f_p`，则

\[
v_p(TK-2b_3DN)=\min(e_p,f_p).
\]

由于 `W^2` 的 `p`-进赋值必须为偶数，得到

\[
\boxed{
\ell+\min(e_p,f_p)\equiv0\pmod2
\qquad(e_p\ne f_p).
}
\]

展开可分成：

### `p=5`

若

\[
\ell+v_5(K)
<
v+g+v_5(Q)+v_5(N),
\]

则必须

\[
\boxed{v_5(K)\equiv0\pmod2}.
\]

若反向严格不等式成立，则必须

\[
\boxed{
\ell+v+g+v_5(Q)+v_5(N)
\equiv0\pmod2.
}
\]

相等时进入五进 resonance：

\[
\boxed{
\ell+v_5(K)
=v+g+v_5(Q)+v_5(N).
}
\]

### `p=2`

若

\[
\ell+v_2(K)
<
1+u+g+v_2(Q)+v_2(N),
\]

则必须

\[
\boxed{v_2(K)\equiv0\pmod2}.
\]

若反向严格不等式成立，则必须

\[
\boxed{
\ell+1+u+g+v_2(Q)+v_2(N)
\equiv0\pmod2.
}
\]

相等时进入二进 resonance：

\[
\boxed{
\ell+v_2(K)
=1+u+g+v_2(Q)+v_2(N).
}
\]

因此整个 A1 的 2/5 无界尾部自然分成四类：

1. 二进非 resonance、五进非 resonance；
2. 仅二进 resonance；
3. 仅五进 resonance；
4. 双 resonance。

这给出了一个与 DD 分支类似、但由 A1 自身 rational-contact 方程直接产生的赋值分层。

---

## 6. saturated 支作为 universal funnel 的特例

若 `L=1`，则

\[
b_3=T\tau.
\]

代入 universal square certificate：

\[
W^2
=T^2(K-2\tau DN).
\]

所以 `T\mid W`。写

\[
W=T W_0,
\]

得到

\[
\boxed{
W_0^2
=K-2\tau DN
=G^2C^2-D(D+2\tau)N,
}
\]

恰好恢复 `a1-rational-contact-framework-2026-08-16.md` 中 saturated integer-square certificate。

同理 universal denominator certificate 给出

\[
T\tau\mid T^2D^2G.
\]

而 saturated 专用根公式还能给出更锋利的

\[
T\tau\mid DG(D+2\tau).
\]

所以两个新框架彼此一致。

---

## 7. 当前无界核心

经过本文件，A1 的第三分母已被严格压入

\[
\boxed{
 b_3=h2^u5^v,
\qquad h\mid Q^2G
}
\]

并同时受

\[
\boxed{
W^2=T^2K-2Tb_3DN
}
\]

控制。

因此真正需要继续关闭的对象已经缩成：

\[
\boxed{
(h,u,v,\ell)
\text{ 的 near-}S\text{-unit square system}
}
\]

其中 `h` 来自固定前缀有限因子集，所有无界性集中在 `u,v,\ell`，并且二进、五进各自只有“低侧 / 高侧 / resonance”三种赋值位置。

下一步应优先证明：

- 双非 resonance 区域是否能由赋值奇偶 + 位数窗直接排空；
- 单 resonance 是否强迫一个 `2^a5^b` 近等式，从而只剩有限 offset；
- 双 resonance 是否能把 `u,v` 都线性锁定到 `\ell+g`，再用 `b_3` 的位数窗排除。

这些仍为 **待证**，不能把 fixed-prefix near-`S`-unit funnel 误写成 A1 已关闭。

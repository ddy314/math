# A1 `d=2` frontier after minimal-surplus closure

> 日期：2026-08-22。
>
> 本文件只记录已证明的 sector exhaustion 与当前开放区；不引入新局部证明。

## 1. minimal surplus is closed

`top-layer-minimal-surplus-closure.md` 已证明
\[
\boxed{d=2,\ r=s=1\Longrightarrow\varnothing.}
\]

因此对 `g>=1` 的最高层，`top-layer.md` 已有 `r,s>=1`，当前只需研究
\[
\boxed{r+s\ge3.}
\]

---

## 2. `s=1` edge

`top-layer-s1-far-lowr-collapse.md` 与 `top-layer-s1-far-radius-phase.md` 给出：

### closed strip
\[
\boxed{
 k\ge2g+1,
 \qquad
 1\le r\le3g-1
 \Longrightarrow\varnothing.
}
\]

### radius phase in the next strip
若
\[
k\ge2g+1,
\qquad
3g\le r\le2k-g-2,
\]
则定义
\[
U_1=(5-z)10^{r+g}+10^g+J,
\qquad
\psi=10^{g-1}r_3,
\]
有
\[
\boxed{
0<
J+1-\rho10^{g-k}
-5\cdot10^{r-3g}\psi^2
<1/25.
}
\]

因此 `s=1` 剩余必须属于：

1. `k<=2g` 的 near-contact 区；或
2. `k>=2g+1,r>=3g` 的 squared-tail phase 区；其中
3. `r>=2k-g-1` 时 curvature 也进入 leading scale。

---

## 3. `r=1` edge

`top-layer-r1-joint-halfgap-collapse.md` 定义
\[
A=U_1/10^{g+2},
\qquad
B=U_2/10^s,
\qquad
N=\max(g+2,s),
\]
以及 joint integer
\[
K
=10^N(A+B-51/100)+10^{N-g-2}.
\]

已证明若
\[
 k+s\ge2g+2,
 \qquad
 N\le4g,
 \qquad
 N\le2k-2,
\]
则
\[
\boxed{r=1\Longrightarrow\varnothing.}
\]

所以 `r=1,s>=2` 的任何剩余 candidate 必须突破至少一面：
\[
\boxed{
 k+s<2g+2
\quad\text{or}\quad
N>4g
\quad\text{or}\quad
N>2k-2.
}
\]

三者分别对应：

1. denominator-contact amplified；
2. squared-tail amplified；
3. curvature amplified。

---

## 4. structural picture

当前两条一-surplus edges 已经表现出完全相同的三尺度结构：

- contact phase；
- third-radius square phase；
- curvature / prefix phase。

minimal-surplus closure 对应三者都在 sub-unit 范围，从而 integer phase 无法存在；surplus 增大后，开放区恰好从某一个 source 被放大到整数 leading digits 的位置开始。

因此下一步不应恢复到原始 `(a1,b1,a2,b2)` 大整数枚举，而应继续提取 amplified source 的 leading-digit integer，并尝试证明它形成 surplus descent 或与 global decimal recovery 冲突。
# A1 minimal diagonal: joint `w=2` coefficient source conflict

> 日期：2026-08-26。依赖 `deep-2high-coefficient-source-minima.md`、`deep-2high-normalized-complement-shell.md`。适用于全部 surviving double-deep 2-high / 5-low master states。

`deep-2high-coefficient-source-minima.md` 分别给出了 `w=2` 的 coefficient-sensitive bounds

\[
u\ge2P_b(\alpha),
\qquad
v\ge P_Q(2,\beta).
\]

但两侧不能独立同时取到自己的最小 source prime，因为

\[
\boxed{\gcd(b_1,Q)=1.}
\]

本文把这一点加入 source-prime minimization，得到严格更强的 joint bound。最重要的显式结果是

\[
\boxed{
19\mid\alpha,\quad3\mid\beta
\Longrightarrow
uv\ge3658,
}
\]

从而

\[
\boxed{
D/T^2<10001/3658<2.735.
}
\]

状态：**严格完成；这是 full 2-high master 的 coefficient subfamily elimination/cap，不宣称关闭全部 `w=2`。**

---

## 1. 两个 source sets

沿用

\[
\mathcal P_b(2)
=19,31,59,71,131,151,179,191,199,251,311,359,\ldots
\]

和

\[
\mathcal P_Q(2)
=3,31,59,67,71,107,127,151,167,179,211,223,\ldots.
\]

对实际 candidate，`u/2=3 mod 4`，故存在

\[
p\equiv3\pmod4,
\qquad
p\mid u/2,
\]

并且

\[
p\in\mathcal P_b(2),
\qquad
p\nmid\alpha
\]

（最后一条来自 `gcd(alpha,u)=1`）。

同理 `v=3 mod 4` 给出

\[
q\equiv3\pmod4,
\qquad
q\mid v,
\]

且

\[
q\in\mathcal P_Q(2),
\qquad
q\nmid\beta.
\]

---

## 2. source primes 必须不同

因为

\[
p\mid u\mid b_1,
\qquad
q\mid v\mid Q,
\]

而

\[
Q=10b_1+1,
\]

所以

\[
\boxed{\gcd(b_1,Q)=1.}
\]

特别地

\[
\boxed{p\ne q.}
\tag{1}
\]

因此不能把两侧 lower bound 当成两个互不相关的 minima 相乘。

定义

\[
\boxed{
J_2(\alpha,\beta)
:=
2\min
\left\{
 pq:
\begin{array}{l}
 p\in\mathcal P_b(2),\ p\nmid\alpha,\\
 q\in\mathcal P_Q(2),\ q\nmid\beta,\\
 p\ne q
\end{array}
\right\}.}
\tag{2}
\]

实际 candidate 自身提供至少一对 `(p,q)`，所以集合非空。由 `u>=2p`、`v>=q`：

\[
\boxed{w=2:\quad M=uv\ge J_2(\alpha,\beta).}
\tag{3}
\]

这严格强化独立乘积

\[
2P_b(\alpha)P_Q(2,\beta)
\]

恰好发生在两个独立 minima 指向同一个 source prime 时。

---

## 3. 核心 collision：`19|alpha` 且 `3|beta`

若

\[
19\mid\alpha,
\]

则 b-side 最小可用 source 从 19 跳到 31：

\[
p\ge31.
\]

若

\[
3\mid\beta,
\]

则 Q-side 最小可用 source 也从 3 跳到 31：

\[
q\ge31.
\]

若只做独立估计，会得到

\[
M\ge2\cdot31\cdot31=1922.
\]

但 `p=q=31` 与 (1) 冲突。

两套 source list 中，31 之后的下一个可用 prime 都至少为 59：

- b-side：`31,59,...`；
- Q-side：`31,59,...`。

因此至少一侧必须提升到 59，得到

\[
\boxed{
M\ge2\cdot31\cdot59=3658.
}
\tag{4}
\]

complement height

\[
\frac{MD}{T^2}<10001
\]

于是

\[
\boxed{
19\mid\alpha,\ 3\mid\beta
\Longrightarrow
\frac D{T^2}<\frac{10001}{3658}<2.735.
}
\tag{5}
\]

与独立 bound `D/T^2<10001/1922<5.204` 相比，joint coprime source 再缩了接近一半。

---

## 4. 更深 coefficient collisions

同一个定义 (2) 会自动处理更多 small-source blocks。

### 4.1 `19*31|alpha`, `3|beta`

此时 b-side 首个可用 source 已是 59，Q-side 首个可用 source是 31，二者不同：

\[
\boxed{J_2=2\cdot59\cdot31=3658.}
\tag{6}
\]

### 4.2 `19|alpha`, `3*31|beta`

此时 b-side 首个可用 source是 31，Q-side 首个可用 source是 59：

\[
\boxed{J_2=3658.}
\tag{7}
\]

### 4.3 `19*31|alpha`, `3*31|beta`

两侧独立 minima 又同时落到 59，但 `p=q=59` 仍被 `gcd(b_1,Q)=1` 禁止。

b-side 在 59 后是 71，Q-side 在 59 后先有 67，因此最便宜的 distinct pair 是

\[
(p,q)=(59,67).
\]

所以

\[
\boxed{
J_2=2\cdot59\cdot67=7906,
}
\tag{8}
\]

从而

\[
\boxed{
D/T^2<10001/7906<1.265.
}
\tag{9}
\]

这说明随着 coefficient 吸收更多早期 source primes，允许的 pure-2 excess 区域会出现离散阶梯式收缩。

---

## 5. source matching formulation

对 `w=2`，后续不应再分别维护一个 `u_min(alpha)` 与一个 `v_min(beta)`。更自然的 finite arithmetic object 是 bipartite source matching：

\[
\mathcal A_\alpha
=
\{p\in\mathcal P_b(2):p\nmid\alpha\},
\]

\[
\mathcal B_\beta
=
\{q\in\mathcal P_Q(2):q\nmid\beta\},
\]

允许边只有

\[
(p,q)\in\mathcal A_\alpha\times\mathcal B_\beta,
\qquad p\ne q.
\]

边权为

\[
2pq.
\]

则 `J_2(alpha,beta)` 正是最小边权。

这把 source-prime divisibility、cross-coprimality 与 `gcd(b_1,Q)=1` 合成一个很小的 exact combinatorial certificate。

---

## 6. 与后续 R-shell certificate 的接口

normalized complement shell 的下一层原本建议按

\[
(w,Y,\alpha,\beta,m)
\]

固定 coefficient 后扫描 `d` 的 periodic source exclusions。

对于 `w=2`，现在可以在进入任何 `d` 扫描前先计算

\[
\boxed{J_2(\alpha,\beta)}
\]

并立即施加

\[
\boxed{
D/T^2<10001/J_2(\alpha,\beta).
}
\]

特别是 (5)、(9) 这样的 coefficient classes 已被强制推离旧 top-denominator region。后续 periodic certificate 只需处理经过这个 joint source cap 后仍有可能存在的 `(eta,B,d)` 区域。

---

## 7. 审计边界

本文只使用：

1. `u/2=3 mod 4` 与 `v=3 mod 4`；
2. `gcd(alpha,u)=gcd(beta,v)=1`；
3. `u|b_1`、`v|Q`；
4. `Q=10b_1+1`；
5. 两个 decimal source prime list 的有限 residue-cycle 计算。

没有使用 factorization of gigantic `b_1,Q`，也没有假设 source prime 在每个 `k` 都出现。`P_b,P_Q,J_2` 只是对实际 candidate 必须已经包含的 `3 mod 4` source 做 lower-bound matching。
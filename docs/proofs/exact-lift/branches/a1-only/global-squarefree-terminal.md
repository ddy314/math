# A1 exact `kappa` square terminal and decimal recovery

> 日期：2026-08-21。依赖 `global-terminal-bridge.md`、`rational-contact.md` 与整数球面 primitive recovery。本文覆盖整个 A1 四层
> \[
> d=s_1-g\in\{-1,0,1,2\}.
> \]

状态：**本文各结论均已严格完成。** 本文给出一个不含自由第三块的 exact terminal criterion；A1 全局空性仍需证明所有移动前缀都无法通过该 criterion。

---

## 1. 前缀量

记

\[
Q=b_1 10^{m_2}+b_2,
\qquad
G=b_1b_2,
\]

\[
C=a_1 10^{n_2}+a_2,
\qquad
D=10^gQ,
\]

\[
N=(a_1b_2)^2+(a_2b_1)^2,
\]

\[
K=G^2C^2-D^2N.
\]

由 `global-terminal-bridge.md`，存在整数

\[
QG<\kappa\le10QG
\]

满足

\[
\theta=G/\kappa.
\]

---

## 2. 统一 `kappa` 判别平方

### 定理 A1-S1

任何 A1 exact-lift candidate 必满足

\[
\boxed{
\kappa\bigl(\kappa K-2GD^2N\bigr)=W^2
}
\tag{1}
\]

对某个整数 `W>=0`。特别地

\[
\boxed{\kappa K>2GD^2N.}
\tag{2}
\]

### 证明

rational-contact 判别平方为

\[
z^2=P^2-(1+2\theta)\frac N{G^2},
\qquad
P=C/D.
\]

代入 `theta=G/kappa`：

\[
z^2
=
\frac{
\kappa(G^2C^2-D^2N)-2GD^2N
}{\kappa D^2G^2}
=
\frac{\kappa K-2GD^2N}{\kappa D^2G^2}.
\]

所以

\[
(\kappa DGz)^2
=
\kappa(\kappa K-2GD^2N).
\]

右侧是整数，而有理数平方若为整数则有理数本身为整数。令

\[
W=\kappa DGz\in\mathbf Z_{\ge0}
\]

即得 (1)。因为原第三分数正且 contact 非退化，实际 discriminant 根不能产生 `K` 的负侧；于是 (2) 是所有 candidate 的必要条件。证毕。

---

## 3. 直接恢复两个有理第三分数根

由 quadratic root formula，两个形式根精确为

\[
\boxed{
 r_\sigma
 =
 \frac{
 \kappa G^2C+\sigma(\kappa+G)W
 }{
 \kappa DG(\kappa+2G)
 },
 \qquad \sigma\in\{+1,-1\}.
}
\tag{3}
\]

任何真正 A1 candidate 的 `r_3` 必须等于其中某个正根。

### 证明

由

\[
r_3
=
\frac{\theta P\pm(1+\theta)z}{1+2\theta},
\]

代入

\[
\theta=G/\kappa,
\qquad
P=C/D,
\qquad
z=W/(\kappa DG)
\]

并通分即可。证毕。

---

## 4. `kappa` 自身恢复 `(L,M)`

A1 normalization 给

\[
\kappa=\frac{10^gLQG}{M},
\qquad
\gcd(L,M)=1,
\]

其中 `L` 只含素数 `2,5`。

令

\[
h:=\gcd(\kappa,10^gQG).
\]

约分有理数

\[
\frac{\kappa}{10^gQG}=\frac LM.
\]

因此 `(L,M)` 被 `kappa` 唯一决定：

\[
\boxed{
L=\frac{\kappa}{h},
\qquad
M=\frac{10^gQG}{h}.
}
\tag{4}
\]

所以任何候选 `kappa` 还必须通过两个纯整数检查：

\[
\boxed{L=2^a5^b\quad(a,b\ge0),}
\tag{5}
\]

以及 slope window

\[
\boxed{
10^{g-1}\le M/L<10^g.
}
\tag{6}
\]

这说明 `kappa` 不是 `(QG,10QG]` 中任意整数；其约化 numerator 必须是纯 `2/5`-smooth。

---

## 5. 十进制第三块的 exact recovery criterion

固定通过 (1),(4)-(6) 的 `(prefix,kappa)`，对某个 `sigma` 令 (3) 的正根约成最简分数

\[
r_\sigma=\frac ab,
\qquad
\gcd(a,b)=1.
\]

### 定理 A1-S2（decimal recovery iff）

该根来自一个合法 A1 第三块，当且仅当存在整数 `n>=1` 使

\[
\boxed{
\frac{Lb}{M}=10^n,
}
\tag{7}
\]

并且 digit windows

\[
\boxed{
10^{n-1}\le a<10^n,
}
\tag{8}
\]

\[
\boxed{
10^{n+g-1}\le b<10^{n+g}
}
\tag{9}
\]

成立。

等价地，算法上只需检查：

1. `M|b`；
2. `L*(b/M)` 是否恰为 `10` 的正整数幂；
3. 若该幂为 `10^n`，则检查 (8)-(9)。

### 证明

必要性：真正 A1 normalization 为

\[
10^n=\omega L,
\qquad
b_3=\omega M.
\]

而 `r_3=a_3/b_3` 已既约，所以若 (3) 的约分根就是实际第三块，必有

\[
a=a_3,
\qquad b=b_3=\omega M.
\]

因此

\[
Lb/M=L\omega=10^n,
\]

得到 (7)。第三分子有 `n=n_3` 位、第三分母有 `m_3=n+g` 位，正是 (8)-(9)。

充分性：反过来若 (7)-(9) 成立，置

\[
\omega=b/M=10^n/L,
\qquad
a_3=a,
\qquad b_3=b.
\]

则 `omega` 为正整数，且

\[
\gcd(10^n/\omega,b_3/\omega)
=
\gcd(L,M)=1.
\]

由 (3) 该 `r_3` 已满足 rational-contact quadratic；(8)-(9) 给出正确第三块位数，且 `(a,b)=1` 已由最简分数保证。于是它正是与当前 prefix、kappa 对应的合法第三块恢复。证毕。

---

## 6. squarefree terminal

把

\[
\kappa=sq^2,
\qquad s\text{ squarefree}
\]

唯一分解。由 (1)，`s|2GD^2N`，且存在 `w>=0` 使

\[
\boxed{
q^2K-w^2=\frac{2GD^2N}{s}.
}
\tag{10}
\]

令

\[
U=GCq-w,
\qquad
V=GCq+w.
\]

则

\[
\boxed{
UV=\frac{D^2N(sq^2+2G)}s,
\qquad
U+V=2GCq.
}
\tag{11}
\]

并且 `0<U<V`。

这把判别平方改写成一个共轭 factor pair；与 (7) 联用后，A1 terminal 的剩余任务是证明不存在同时满足：

\[
\boxed{
\begin{gathered}
QG<sq^2\le10QG,\\
L=\kappa/\gcd(\kappa,10^gQG)\text{ is }2/5\text{-smooth},\\
q^2K-w^2=2GD^2N/s,\\
Lb/M=10^n\text{ for one reduced root }a/b.
\end{gathered}}
\tag{12}
\]

---

## 7. 不含第三块的整尾证书

primitive recovery 还给出

\[
\boxed{
10^n
\mid
2\kappa^2 10^g QN(\kappa+2G).
}
\tag{13}
\]

### 推导

统一 primitive recovery 写成

\[
10^{m_3}QG_0=2\kappa\mu\nu,
\]

而 normalized quadratic 分别模 `mu,nu` 给

\[
\mu\nu\mid \kappa D^2N(\kappa+2G).
\]

故

\[
10^{m_3}\mid
2\kappa^2\frac{D^2}{Q}N(\kappa+2G).
\]

A1 中

\[
D=10^gQ,
\qquad
m_3=n+g,
\]

所以

\[
10^{n+g}\mid
2\kappa^2 10^{2g}QN(\kappa+2G),
\]

约去公共 `10^g` 即得 (13)。

因此，一旦 `(prefix,kappa)` 固定，`n` 已被一个完全显式的二五赋值上界控制；再用 (7) 检查实际 root denominator 即可完成该 terminal state 的 exact certification。

---

## 8. 当前目标

与旧的 fixed-prefix finite statement 相比，本文把第三块变量完全删掉了。现在 A1 的移动部分只剩

\[
(a_1,b_1,a_2,b_2;g,k;\kappa),
\]

其中 `d=s1-g` 只有四种。下一步应直接研究 (10)-(12) 在四层 digit geometry 下的局部/高度不相容，而不再恢复任意 `a3,b3` 搜索空间。

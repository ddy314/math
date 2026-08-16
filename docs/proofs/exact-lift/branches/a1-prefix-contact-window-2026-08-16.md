# A1 moving-prefix contact window — 2026-08-16

本文在完整 fixed-prefix finite theorem 之后，把 A1 的剩余问题改写成纯前缀对象 `(C,D,G,N,K)` 与一个紧致归一化第三块 `(\eta,\rho)` 的接触问题。

目标不是再次控制 `\ell`，而是精确描述移动前缀必须满足的必要条件。

本文结论均为 **已严格完成**；最后一节是当前剩余核心。

---

## 1. 完全消去尾长 `\ell`

记

\[
T=10^\ell,
\qquad
\eta=\frac{a_3}{T},
\qquad
\rho=\frac{b_3}{T}.
\]

因为 `a_3` 恰有 `\ell=n_3` 位，

\[
\boxed{\frac1{10}\le\eta<1.}
\tag{1}
\]

因为 `b_3` 恰有 `m_3=g+\ell` 位，

\[
\boxed{10^{g-1}\le\rho<10^g.}
\tag{2}
\]

并且

\[
\boxed{r_3=\frac\eta\rho.}
\tag{3}
\]

原始拼接为

\[
\alpha=T(C+\eta),
\qquad
\beta=T(D+\rho).
\]

所以 exact lift 等价于

\[
\boxed{
\frac{C+\eta}{D+\rho}
=
\sqrt{
\frac NG^2+\left(\frac\eta\rho\right)^2
}.
}
\tag{4}
\]

这里

\[
C=a_1 10^{n_2}+a_2,
\quad
D=10^gQ,
\quad
Q=b_1 10^{m_2}+b_2,
\]

\[
G=b_1b_2,
\qquad
N=(a_1b_2)^2+(a_2b_1)^2
\]

完全由前两块和 `g` 决定。

因此连续几何层面的 A1 剩余问题已经完全不含 `\ell`；尾长只负责把 `(\eta,\rho)` 实现成同一个十进制尺度上的既约整数对。

---

## 2. 归一化 cross determinant

定义

\[
\boxed{J=C\rho-D\eta.}
\]

由于 A1 contact 中

\[
P=\frac CD>R>r_3=\frac\eta\rho,
\]

有

\[
\boxed{J>0.}
\tag{5}
\]

而

\[
P-R
=
\frac{C\rho-D\eta}{D(D+\rho)}
=
\boxed{
\frac{J}{D(D+\rho)}
},
\tag{6}
\]

\[
R-r_3
=
\frac{C\rho-D\eta}{\rho(D+\rho)}
=
\boxed{
\frac{J}{\rho(D+\rho)}
}.
\tag{7}
\]

二者之比自动恢复

\[
\frac{P-R}{R-r_3}=\frac\rho D.
\]

球面差平方

\[
(R-r_3)(R+r_3)=\frac NG^2
\]

再与 (7) 联立，可得到完全归一化的 determinant identity：

\[
\boxed{
G^2(C\rho-D\eta)
(C\rho+D\eta+2\rho\eta)
=
N\rho^2(D+\rho)^2.
}
\tag{8}
\]

这是移动前缀与紧致尾矩形之间的一个纯有理代数曲面方程。

---

## 3. 前缀值 `P` 必须贴住球面

由

\[
P-R=\frac\rho D(R-r_3)
\]

和

\[
\frac\rho D<\frac1Q,
\]

有

\[
0<P-R<\frac{R-r_3}{Q}<\frac RQ.
\]

因此

\[
\boxed{
\frac{Q}{Q+1}P<R<P.
}
\tag{9}
\]

也就是说，前两块拼接值 `P` 与完整球面半径的相对误差严格小于 `1/Q`。

这是 A1 移动前缀最重要的实数接触条件之一。

---

## 4. `r_3` 的统一 digit window

由 (1)–(3)：

\[
\frac{1/10}{10^g}
<r_3<
\frac1{10^{g-1}},
\]

即

\[
\boxed{
10^{-g-1}<r_3<10^{1-g}.
}
\tag{10}
\]

因此

\[
\boxed{
\frac NG^2+10^{-2g-2}
<R^2
<
\frac NG^2+10^{2-2g}.
}
\tag{11}
\]

---

## 5. 前缀缺口 `K` 的第一个纯整数下界

定义

\[
\boxed{K=G^2C^2-D^2N.}
\]

由于

\[
P^2-rac NG^2
=
\frac{K}{D^2G^2},
\]

而 `P>R`，由 (11) 的左侧得到

\[
P^2-rac NG^2
>R^2-rac NG^2
=r_3^2
>10^{-2g-2}.
\]

故

\[
K>D^2G^2\,10^{-2g-2}.
\]

利用

\[
D=10^gQ
\]

得到完全消去 `g` 的下界

\[
\boxed{
K>\frac{Q^2G^2}{100}.
}
\tag{12}
\]

因为 `K` 为整数，也可写成

\[
\boxed{
K\ge
\left\lfloor\frac{Q^2G^2}{100}\right\rfloor+1.
}
\]

---

## 6. 第二个纯前缀下界：切触判别

由 denominator-funnel 的 normalized square

\[
V^2=K-2\rho DN\ge0
\]

可得

\[
K\ge2\rho DN.
\]

而

\[
\rho\ge10^{g-1},
\qquad
D=10^gQ,
\]

所以

\[
\boxed{
K\ge
2\cdot10^{2g-1}QN
=
\frac{10^{2g}QN}{5}.
}
\tag{13}
\]

若考虑严格 `r_3>0` 对应的非退化接触，则实际候选还要满足相应根的正性；本文保留 (13) 作为无条件必要下界。

综合 (12)–(13)：

\[
\boxed{
K>
\max\left(
\frac{Q^2G^2}{100},
\frac{10^{2g}QN}{5}
\right)
}
\tag{14}
\]

（第二项若恰为整数边界，则按 (13) 使用非严格形式。）

---

## 7. 一个粗但纯前缀的上窗

由 (9)

\[
P<R\left(1+\frac1Q\right).
\]

于是

\[
P^2-rac NG^2
<
\left(1+\frac1Q\right)^2
\left(
\frac NG^2+r_3^2
\right)
-rac NG^2.
\]

利用

\[
r_3^2<10^{2-2g}
\]

得到

\[
P^2-rac NG^2
<
\left(\frac2Q+\frac1{Q^2}\right)\frac NG^2
+
\left(1+\frac1Q\right)^2 10^{2-2g}.
\]

乘以 `D^2G^2=10^{2g}Q^2G^2`：

\[
\boxed{
K
<
10^{2g}(2Q+1)N
+100(Q+1)^2G^2.
}
\tag{15}
\]

因此 A1 moving prefix 必须把特殊整数二次型 `K` 放进明确的前缀窗

\[
\boxed{
\max\left(
\frac{Q^2G^2}{100},
\frac{10^{2g}QN}{5}
\right)
<K
<
10^{2g}(2Q+1)N+100(Q+1)^2G^2.
}
\tag{16}
\]

---

## 8. `K` 作为前两分子的显式不定二次型

记 `p=10^{n_2}`。则

\[
C=a_1p+a_2,
\]

所以

\[
K
=
\left(G^2p^2-D^2b_2^2\right)a_1^2
+2G^2p\,a_1a_2
+
\left(G^2-D^2b_1^2\right)a_2^2.
\tag{17}
\]

其中

\[
G^2-D^2b_1^2<0,
\]

而在 A1 carrier 可行区第一系数处于正侧。因此 `K` 是一个由 decimal-shift 参数固定的显式不定二元二次型。

A1 的剩余 prefix problem 可以表述为：

> 在 `a_i,b_i` 的位数、互素性和 carrier 约束下，证明这个特殊不定二次型无法同时落入 (16) 的接触窗，并支持 normalized square / primitive-gap 条件。

---

## 9. 当前移动前缀核心

第三尾的所有无界机制已被前序文件封锁后，A1 现在只剩以下移动前缀系统：

\[
\boxed{
0\le g\le\min(s_2-1,s_1+1),
}
\]

\[
\boxed{
K=G^2C^2-D^2N
}
\]

满足接触窗 (16)，并且存在

\[
\eta\in[1/10,1),
\qquad
\rho\in[10^{g-1},10^g)
\]

满足代数曲面 (8)，同时 `(\eta,\rho)` 必须来自同一十进制尺度 `T=10^\ell` 的既约整数对。

这就是当前 A1 的真正 moving-prefix core；后续任何“全局关闭”都应直接攻击这一系统，而无需再次分析第三尾的无界分类。

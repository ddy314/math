# A1 minimal diagonal: moderate double-deep root normal form

> 日期：2026-08-20。依赖 `deep-moderate-factorization.md` 与 `deep-moderate-three-pattern.md`。当前范围 `k=g>=31`。

本文给 moderate double-deep 一个新的正规形：把 supply quadratic 改看成关于 gap numerator `gamma` 的二次方程后，deep denominator

\[
D=2^A5^B
\]

从根公式中**完全消失**。

设

\[
T=10^k,
\qquad
196000<r<15214000,
\]

并沿用

\[
N_0,\quad w,\quad
\Gamma_k=\gamma/D.
\]

核心结论：存在正整数 `Z` 满足

\[
\boxed{
Z^2=(10N_0T+r)^2+400N_0Tr(10T^2-w),
}
\tag{1}

而 normalized gap 唯一等于

\[
\boxed{
\Gamma_k=
\frac{
10(20w-1)N_0T-r+Z
}{2000T^2}.
}
\tag{2}

所以 `D` 只是右侧有理数约分后的 `2/5` denominator，而不再是独立变量。

状态：**已严格完成。**

---

## 1. 从 moderate supply quadratic 出发

`deep-moderate-factorization.md` 给出

\[
C_0D^2N_0^2
-DuTN_0
+1000\gamma^2T^2
+\gamma u
+c_2\gamma^2=0,
\tag{3}
\]

其中

\[
C_0=w(10w-1),
\qquad
c_2=10(1-20w),
\]

\[
u=u_0+Dr,
\qquad
u_0=10\gamma(20w-1).
\]

代入后关于 `gamma` 收集：

\[
1000T^2\gamma^2
+D\bigl(r-10(20w-1)N_0T\bigr)\gamma
+D^2\bigl(C_0N_0^2-N_0Tr\bigr)=0.
\tag{4}

---

## 2. 判别式恰为 `D^2 Z^2`

(4) 关于 `gamma` 的判别式为

\[
D^2\left(
100N_0^2T^2
+4000N_0T^3r
-400wN_0Tr
+20N_0Tr
+r^2
\right).
\]

括号重新组合：

\[
\begin{aligned}
&100N_0^2T^2+20N_0Tr+r^2
+400N_0Tr(10T^2-w)\\
&\qquad=(10N_0T+r)^2
+400N_0Tr(10T^2-w).
\end{aligned}
\]

因此 exact candidate 必须存在整数 `Z>0`，满足主式 (1)。

---

## 3. 只有 `+Z` 根可能为正

令

\[
H:=10(20w-1)N_0T-r.
\]

根公式给

\[
\Gamma_k=\frac{H\pm Z}{2000T^2}.
\tag{5}

计算

\[
\boxed{
Z^2-H^2
=4000N_0T^2(Tr-C_0N_0).
}
\tag{6}

因为

\[
r>196000,
\qquad
C_0=w(10w-1)\le156,
\qquad
N_0\le T,
\]

有

\[
Tr-C_0N_0>(196000-156)T>0.
\]

因此

\[
Z>|H|.
\]

所以

\[
H-Z<0,
\]

而 normalized gap 必须正。唯一可能根是

\[
\boxed{
\Gamma_k=\frac{H+Z}{2000T^2},
}
\]

即 (2)。

---

## 4. `D` 由根的约分唯一恢复

记

\[
\boxed{S:=H+Z.}
\]

则

\[
\Gamma_k=\frac{S}{2000T^2}.
\]

原定义 `Gamma_k=gamma/D` 已经既约，且 moderate double-deep 有 `A,B>0`。因为

\[
2000T^2=2^{2k+4}5^{2k+3},
\]

所以

\[
\boxed{
A=2k+4-v_2(S),
}
\tag{7}

\[
\boxed{
B=2k+3-v_5(S).
}
\tag{8}

因此 LL/LH/HL 的 denominator exponents 都只是同一个整数 `S` 的局部 valuation 输出。

---

## 5. conjugate product

令

\[
R:=Z-H>0.
\]

由 (6)：

\[
\boxed{
SR
=4000N_0T^2(Tr-C_0N_0).
}
\tag{9}

这给 2/5 两侧一个非常透明的 root-branch interpretation。

因为

\[
H=10(20w-1)N_0T-r,
\]

而 `v_2(r)<=23`、`v_5(r)<=10`、`k>=31`，有

\[
v_2(H)=v_2(r),
\qquad
v_5(H)=v_5(r).
\tag{10}

于是：

- 在 5-adic 中，`S=Z+H` 与 `R=Z-H` 的差是 `2H`，valuation 为 `v_5(r)`；故一个 root branch 保持 shallow valuation `v_5(r)`，另一个承担全部高 valuation。
- 在 2-adic 中，`2H` 的 valuation 为 `v_2(r)+1`；所以 shallow branch 的 valuation 是 `v_2(r)+1`，另一 branch 承担高 valuation。

这正对应 `deep-moderate-three-pattern.md` 的 low/high dichotomy。

---

## 6. `Z^2=r^2 mod T` 与 p-adic branch labels

由 (1) 直接模 `T`：

\[
\boxed{Z^2\equiv r^2\pmod T.}
\tag{11}

写

\[
a=v_2(r)\le23,
\qquad
b=v_5(r)\le10.
\]

由于 `k>=31>2a,2b`，标准 prime-power square-root lifting 给：

\[
\boxed{
Z\equiv\pm r\pmod{5^{k-b}},
}
\tag{12}

以及 2-adic 的四根合并为

\[
\boxed{
Z\equiv\pm r\pmod{2^{k-a-1}}.
}
\tag{13}

另一方面高十进制项使

\[
H\equiv-r
\]

模上述幂。因此：

- `Z congruent +r` 时 `S=H+Z` 发生大规模 cancellation，对应 **low denominator exponent**；
- `Z congruent -r` 时 `S` 留在 shallow root，因 (7)-(8) 对应 **high denominator exponent**。

所以 three-pattern 可重新标记为：

\[
\boxed{
\begin{array}{c|cc}
&2\text{-branch}&5\text{-branch}\\ \hline
LL&+&+\\
LH&+&-\\
HL&-&+
\end{array}}
\tag{14}

而 `(-,-)` 正是 high-high，已由 `deep-balanced-collapse.md` 排除。

---

## 7. normalized real equation

把 factorization

\[
(10\gamma T-wDN_0)
(100\gamma T-(10w-1)DN_0)
=Dr(DTN_0-\gamma)
\]

除以 `D^2T^2`，并令

\[
s=N_0/T,
\qquad \Gamma=\gamma/D,
\]

得到精确关系

\[
\boxed{
(10\Gamma-ws)
(100\Gamma-(10w-1)s)
=r\left(s-\frac{\Gamma}{T^2}\right).
}
\tag{15}

除了最后一个 `T^-2` 修正外，整个 moderate double-deep 的实数几何只由

\[
(w,r,s,\Gamma)
\]

控制，并且 `r` 已处于绝对有限区间。

下一步可直接在 root equation (1) / branch labels (12)-(14) 上做局部 lifting 或 periodic modular exhaustion，而无需重新引入二维 `(A,B)` 搜索。
# A1 top-layer minimal-surplus off-diagonal squeeze — 2026-08-17

本文继续 `a1-top-layer-excess-decomposition-2026-08-17.md`，研究最小双 surplus

\[
r=s=1,
\qquad g\ge1
\]

中的 off-diagonal 区域

\[
\boxed{k>g.}
\]

此时第三 contact source 比 prefix source 至少再小一个十倍，且 `k\ge2` 令曲率参数

\[
\varepsilon=10^{-2k}
\]

至多为 `10^{-4}`。因此正项 excess 分解可以显著收紧。

核心结论：

\[
\boxed{
\frac{1017}{2000}
<\phi_1+\phi_2
<\frac{5111}{10000}.
}
\]

于是：

\[
\boxed{
z=1:\quad
\frac{817}{2000}<\phi_1<\frac{4111}{10000},
}
\]

\[
\boxed{
z=3:\quad
\frac{417}{2000}<\phi_1<\frac{2111}{10000}.
}
\]

两个 first-residue interval 的宽度都小于 `0.0026`。

本文结论均为 **已严格完成**。

---

## 1. 最小边界回顾

`r=s=1` 已有

\[
1\le g\le k,
\]

\[
b_1=10^{2k+1}-w,
\qquad
b_2=10^{k-g},
\]

\[
z\in\{1,3\},
\]

以及六类型

\[
(z,w)
\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\}.
\]

定义

\[
\varepsilon=10^{-2k},
\]

\[
\phi_1
=\frac{10^kU_1/b_1}{10^{g+1-k}},
\qquad
\phi_2=\frac z{10}.
\]

positive excess decomposition 给出

\[
\begin{aligned}
2(\phi_1+\phi_2)-1
={}&
\frac{\mathfrak h}{M\varepsilon}
\left(1+\varepsilon\phi_1+\frac RM\right)\\
&+\frac{(r_3/M)^2}{\varepsilon}
+\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
+\varepsilon^2\phi_1^2.
\end{aligned}
\tag{1}
\]

并且此前已证明下界

\[
\boxed{
\phi_1+\phi_2>\frac{1017}{2000}.
}
\tag{2}
\]

---

## 2. `lambda/epsilon` 几乎精确等于 `1/100`

因为

\[
b_2=10^{k-g},
\qquad
m_2=k-g+1,
\]

有

\[
Q=10^{k-g}(10b_1+1),
\]

所以

\[
\lambda=\frac{b_2}{Q}
=\frac1{10b_1+1}.
\]

又

\[
b_1=10^{2k+1}-w,
\]

故

\[
\boxed{
\frac\lambda\varepsilon
=
\frac1{100-(10w-1)\varepsilon}.
}
\tag{3}
\]

六类型中 `w\le4`。

现在额外假设

\[
k>g\ge1.
\]

于是

\[
k\ge2,
\qquad
\varepsilon\le10^{-4}.
\]

因此

\[
100-(10w-1)\varepsilon
\ge100-39\cdot10^{-4}
=99.9961,
\]

所以

\[
\boxed{
\frac\lambda\varepsilon<0.010001.
}
\tag{4}
\]

---

## 3. `theta` source 再小一个十倍

在 `s=1` 时

\[
D=10^gQ=10^k(10b_1+1).
\]

又

\[
\theta=\frac\rho D,
\qquad
10^{g-1}\le\rho<10^g.
\]

所以

\[
\frac{\theta}{\lambda}
=\frac\rho{10^k}.
\]

若 `k>g`：

\[
\frac\rho{10^k}<10^{g-k}\le\frac1{10}.
\]

因此由 (4)

\[
\boxed{
\frac\theta\varepsilon<0.0010001.
}
\tag{5}
\]

---

## 4. contact-height source 的统一上界

此前 half-gap shell 给出

\[
0<\phi_1<0.434,
\qquad
0<\phi_2\le0.3.
\]

因此

\[
1+\varepsilon\phi_1<1.0000434.
\tag{6}
\]

contact height 满足

\[
\frac{\mathfrak h}{M}
=
\lambda
\left[(1+\varepsilon\phi_1)
-10^{-g}(1-\varepsilon\phi_2)\right]
+\theta\left(\frac RM-\frac{r_3}{M}\right).
\]

两个方括号均严格小于 `1+epsilon phi_1`，并且

\[
\frac RM<\frac{10^kr_1}{M}=1+\varepsilon\phi_1.
\]

于是由 (4)–(6)：

\[
\boxed{
\frac{\mathfrak h}{M\varepsilon}
<
(0.010001+0.0010001)\,1.0000434
<0.011002.
}
\tag{7}
\]

此外

\[
1+\varepsilon\phi_1+\frac RM
<2(1+\varepsilon\phi_1)
<2.0000868.
\]

所以 (1) 第一项严格小于

\[
\boxed{0.022005.}
\tag{8}
\]

---

## 5. 其余三个 source 的总量不到 `0.000196`

最高层有

\[
\frac{(r_3/M)^2}{\varepsilon}<10^{-4g}\le10^{-4}.
\tag{9}
\]

又

\[
2\phi_1+\phi_2^2-\phi_1^2
<2\phi_1+\phi_2^2
<2(0.434)+0.3^2
=0.958.
\]

因为 `epsilon<=10^{-4}`：

\[
\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
<0.0000958.
\tag{10}
\]

并且

\[
\varepsilon^2\phi_1^2
<10^{-8}(0.434)^2
<2\cdot10^{-9}.
\tag{11}
\]

所以 (9)–(11) 总和严格小于

\[
0.000196.
\tag{12}
\]

---

## 6. off-diagonal half-gap 被压到宽度 `0.0026`

把 (8)、(12) 代入 (1)：

\[
2(\phi_1+\phi_2)-1
<0.022201.
\]

因此

\[
\phi_1+\phi_2
<0.5111005
<\frac{5111}{10000}.
\]

结合 (2)：

\[
\boxed{
\frac{1017}{2000}
<\phi_1+\phi_2
<\frac{5111}{10000}.
}
\tag{13}
\]

### `z=1`

此时 `phi_2=1/10`：

\[
\boxed{
\frac{817}{2000}
<\phi_1
<\frac{4111}{10000}.
}
\tag{14}
\]

即

\[
0.4085<\phi_1<0.4111.
\]

### `z=3`

此时 `phi_2=3/10`：

\[
\boxed{
\frac{417}{2000}
<\phi_1
<\frac{2111}{10000}.
}
\tag{15}
\]

即

\[
0.2085<\phi_1<0.2111.
\]

两个区间宽度均为

\[
0.0026.
\]

---

## 7. 当前剩余分裂

最小双 surplus `r=s=1,g\ge1` 现在自然分成：

1. **off-diagonal** `k>g`：本文的极窄 first-residue interval；
2. **diagonal** `k=g`：`b_2=1`，且 `theta/lambda` 可在 `[1/10,1)` 中移动，需要单独处理。

因此六类型核中真正保留较大连续自由度的部分已经集中到

\[
\boxed{k=g.}
\]

后续应先攻击 diagonal kernel；off-diagonal 则适合继续做十进制 residue / congruence refinement。

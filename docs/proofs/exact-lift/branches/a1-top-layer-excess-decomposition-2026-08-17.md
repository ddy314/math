# A1 top-layer positive excess decomposition — 2026-08-17

本文把最高层 `d=2` 的 half-gap 刚性进一步改写成一个精确的**正项分解**。

设两个 coprime residue 对 carrier gap 的自然尺度贡献为

\[
\phi_1
:=
\frac{10^kU_1/b_1}{10^{g+1-k}},
\qquad
\phi_2
:=
\frac{U_2/b_2}{10^{g+1-k}}.
\]

则真实 normalized carrier gap 是

\[
\phi_1+\phi_2.
\]

本文证明

\[
\boxed{
\begin{aligned}
2(\phi_1+\phi_2)-1
={}&
\frac{\mathfrak h}{M\varepsilon}
\left(
1+\varepsilon\phi_1+\frac RM
\right)\\
&+\frac{(r_3/M)^2}{\varepsilon}\\
&+\varepsilon
\left(
2\phi_1+\phi_2^2-\phi_1^2
\right)
+\varepsilon^2\phi_1^2,
\end{aligned}
}
\]

其中

\[
M=10^{k+g+1},
\qquad
\varepsilon=10^{-2k},
\qquad
\mathfrak h=10^kr_1-R>0.
\]

右端每一项都严格非负，第一项严格正。因此 half-gap 超过 `1/2` 的 excess 被拆成四个可独立估计的来源。

本文结论均为 **已严格完成**。

---

## 1. 中心化 residue 坐标

最高层 residue kernel 给出

\[
r_1=10^{g+1}+\frac{U_1}{b_1},
\]

\[
r_2=M-\frac{U_2}{b_2},
\qquad
M=10^{k+g+1}.
\]

定义自然 gap 尺度

\[
H_0=10^{g+1-k}=M\varepsilon,
\qquad
\varepsilon=10^{-2k}.
\]

令

\[
\boxed{
\phi_1=
\frac{10^kU_1/b_1}{H_0},
}
\tag{1}
\]

\[
\boxed{
\phi_2=
\frac{U_2/b_2}{H_0}.
}
\tag{2}
\]

于是得到三个精确中心化公式：

\[
\boxed{
\frac{10^kr_1}{M}
=1+\varepsilon\phi_1,
}
\tag{3}
\]

\[
\boxed{
\frac{r_2}{M}
=1-\varepsilon\phi_2,
}
\tag{4}
\]

\[
\boxed{
\frac{r_1}{M}
=10^{-k}(1+\varepsilon\phi_1)
=\sqrt\varepsilon(1+\varepsilon\phi_1).
}
\tag{5}
\]

因此

\[
10^kr_1-r_2
=M\varepsilon(\phi_1+\phi_2).
\tag{6}
\]

---

## 2. 球面在中心坐标中的精确式

记

\[
\zeta=\frac{r_3}{M},
\qquad
\widehat R=\frac RM.
\]

球面

\[
R^2=r_1^2+r_2^2+r_3^2
\]

结合 (4)–(5) 给出

\[
\boxed{
\widehat R^2
=(1-\varepsilon\phi_2)^2
+\varepsilon(1+\varepsilon\phi_1)^2
+\zeta^2.
}
\tag{7}
\]

另一方面令

\[
A_0=10^kr_1=M(1+\varepsilon\phi_1).
\]

则直接展开

\[
\frac{A_0^2-R^2}{M^2}
=
\varepsilon
\left[
2(\phi_1+\phi_2)-1
+\varepsilon(\phi_1^2-2\phi_1-\phi_2^2)
-\varepsilon^2\phi_1^2
\right]
-\zeta^2.
\tag{8}

---

## 3. contact height `h`

定义第一 carrier 与球面的正 gap

\[
\boxed{
\mathfrak h=A_0-R>0.
}
\tag{9}
\]

则差平方给出

\[
A_0^2-R^2
=\mathfrak h(A_0+R).
\]

除以 `M^2`：

\[
\boxed{
\frac{A_0^2-R^2}{M^2}
=
\frac{\mathfrak h}{M}
\left(
1+\varepsilon\phi_1+\widehat R
\right).
}
\tag{10}
\]

同时 rational contact 给出

\[
P-R=\theta(R-r_3),
\]

而前两块权重表达为

\[
P=(1-\lambda)A_0+\lambda10^{-g}r_2.
\]

故

\[
A_0-P
=\lambda(A_0-10^{-g}r_2).
\]

因此

\[
\boxed{
\frac{\mathfrak h}{M}
=
\lambda
\left[
(1+\varepsilon\phi_1)
-10^{-g}(1-\varepsilon\phi_2)
\right]
+\theta(\widehat R-\zeta).
}
\tag{11}
\]

右端两项均为正。

---

## 4. 正项 excess 分解

把 (10) 代入 (8)，再除以 `epsilon` 并移项：

\[
\begin{aligned}
2(\phi_1+\phi_2)-1
={}&
\frac{\mathfrak h}{M\varepsilon}
\left(
1+\varepsilon\phi_1+\widehat R
\right)\\
&+\frac{\zeta^2}{\varepsilon}\\
&+\varepsilon
\left(
2\phi_1+\phi_2^2-\phi_1^2
\right)\\
&+\varepsilon^2\phi_1^2.
\end{aligned}
\]

即

\[
\boxed{
\begin{aligned}
2(\phi_1+\phi_2)-1
={}&
\frac{\mathfrak h}{M\varepsilon}
\left(
1+\varepsilon\phi_1+\frac RM
\right)\\
&+\frac{(r_3/M)^2}{\varepsilon}\\
&+\varepsilon
\left(
2\phi_1+\phi_2^2-\phi_1^2
\right)
+\varepsilon^2\phi_1^2.
\end{aligned}
}
\tag{12}
\]

由于 half-gap shell 已给出

\[
0<\phi_1,\phi_2<\frac{267}{500}<1,
\]

所以

\[
2\phi_1+\phi_2^2-\phi_1^2
=\phi_1(2-\phi_1)+\phi_2^2>0.
\]

结合 (9)、`r_3>0`：式 (12) 右边四行全部为正。

这直接重新证明

\[
\boxed{\phi_1+\phi_2>\frac12.}
\]

---

## 5. 四种 excess source

式 (12) 把超过 `1/2` 的 excess 精确分成：

1. **prefix/contact height**
   \[
   \frac{\mathfrak h}{M\varepsilon}
   \left(1+\varepsilon\phi_1+R/M\right);
   \]
   其中 `h` 又按 (11) 分成 `lambda` 前缀混合与 `theta` 第三块接触两项；
2. **third-radius source**
   \[
   (r_3/M)^2/\varepsilon;
   \]
3. **first curvature source**
   \[
   \varepsilon\phi_1(2-\phi_1);
   \]
4. **second curvature source**
   \[
   \varepsilon\phi_2^2+\varepsilon^2\phi_1^2.
   \]

由于 `g\ge1` 时 half-gap sharpening 给出

\[
2(\phi_1+\phi_2)-1<\frac{34}{500}=0.068,
\]

上述每个正 source 都自动小于 `0.068`。

---

## 6. 最小双 surplus `r=s=1` 的进一步下推

现在取

\[
r=s=1,
\qquad g\ge1.
\]

此前已有

\[
b_2=10^{k-g},
\qquad
z\in\{1,3\},
\]

以及

\[
\phi_2=\frac z{10}.
\]

此时

\[
\lambda
=\frac{b_2}{b_1 10^{m_2}+b_2}
=\frac1{10b_1+1}.
\tag{13}
\]

又

\[
b_1=10^{2k+1}-w<10^{2k+1},
\]

所以

\[
\boxed{
\frac\lambda\varepsilon
>
\frac1{100}.
}
\tag{14}
\]

由 `g\ge1`、`t<1`：

\[
(1+\varepsilon\phi_1)
-10^{-g}(1-\varepsilon\phi_2)
>1-10^{-g}\ge\frac9{10}.
\]

故 (11)、(14) 给出

\[
\frac{\mathfrak h}{M\varepsilon}
>
\frac9{1000}.
\tag{15}
\]

同时

\[
R>r_2=M(1-\varepsilon\phi_2),
\]

所以

\[
1+\varepsilon\phi_1+\frac RM
>
2-\varepsilon\phi_2
\ge2-rac3{1000}
>\frac{199}{100}.
\]

因此式 (12) 的第一 source 单独已经给出

\[
2(\phi_1+\phi_2)-1
>
\frac9{1000}\frac{199}{100}
>
\frac{17}{1000}.
\]

从而

\[
\boxed{
\phi_1+\phi_2>\frac{1017}{2000}=0.5085.
}
\tag{16}
\]

于是六类型中的第一余量窗同步加强为：

### `z=1`

\[
\boxed{
\frac{817}{2000}
<\phi_1<\frac{217}{500},
}
\tag{17}
\]

即

\[
0.4085<\phi_1<0.434.
\]

### `z=3`

\[
\boxed{
\frac{417}{2000}
<\phi_1<\frac{117}{500},
}
\tag{18}
\]

即

\[
0.2085<\phi_1<0.234.
\]

所以最小双 surplus 的两个 first-residue interval 宽度已经压到约 `0.0255`。

---

## 7. 后续用途

式 (12) 是当前最高层最适合作为下一阶段主方程的形式：

- 所有项同号，不能互相抵消；
- 可以按 `r,m_2,k,g` 分别估计 `lambda,theta,zeta,epsilon`；
- 边界 surplus 越小，`lambda/theta` source 越大；
- surplus 越大，half-gap 越趋近纯曲率中心 `1/2`；
- `g=0` 时 third-radius source 不再自动很小，正好解释该扇区为何需要单独处理。

后续关闭 `d=2` 应围绕这个 positive source decomposition 做 surplus source split，而无需重新回到四个原始大整数。

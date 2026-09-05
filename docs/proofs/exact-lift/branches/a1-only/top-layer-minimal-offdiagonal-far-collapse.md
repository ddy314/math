# A1 top layer: far off-diagonal minimal-surplus collapse

> 日期：2026-08-22。
>
> 依赖：`top-layer.md` 中 top-layer residue kernel、positive-excess decomposition 与 minimal-surplus off-diagonal squeeze。
>
> 范围：完整 A1 的最高层
> \[
> d=s_1-g=2,
> \]
> 最小双 surplus
> \[
> r=s=1,
> \qquad g\ge1,
> \qquad k>g.
> \]

状态：**已严格完成。** 本文关闭整个 far off-diagonal 区域
\[
\boxed{k\ge2g+1}.
\]
因此在 minimal diagonal 已关闭后，`r=s=1,g>=1` 只可能剩下
\[
\boxed{g<k\le2g}.
\]

---

## 1. 六类型与 first-residue 窄窗

`top-layer.md` 已证明，在
\[
r=s=1,\qquad g\ge1
\]
中
\[
b_1=10^{2k+1}-w,
\qquad
b_2=10^{k-g},
\qquad
z\in\{1,3\},
\]
且
\[
(z,w)\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\}.
\tag{1}
\]

令
\[
\varepsilon=10^{-2k},
\qquad
H=10^g,
\]
以及 positive-excess 坐标
\[
p:=\phi_1,
\qquad
q:=\phi_2=\frac z{10}.
\]

在 off-diagonal `k>g` 中已有严格窄窗
\[
\boxed{
\frac{817}{2000}<p<\frac{4111}{10000}
\qquad(z=1),
}
\tag{2}
\]

\[
\boxed{
\frac{417}{2000}<p<\frac{2111}{10000}
\qquad(z=3).
}
\tag{3}
\]

---

## 2. 新整数坐标 `J`

residue kernel 写
\[
a_1=10^{g+1}b_1+U_1,
\qquad U_1\in\mathbf Z_{>0}.
\]

定义
\[
\boxed{
U_1=(51-10z)H+J,
\qquad J\in\mathbf Z.
}
\tag{4}
\]

由
\[
p
=\frac{10^{2k-g-1}U_1}{b_1},
\qquad
b_1=10^{2k+1}-w,
\]
精确得到
\[
\boxed{
p
=\frac{51-10z+J/H}{100-10w\varepsilon}.
}
\tag{5}
\]

记
\[
S:=2(p+q)-1.
\]
因为 `51-10z=51-100q`，由 (5) 直接整理得
\[
\boxed{
\frac JH+1
=50S-10w\varepsilon p.
}
\tag{6}
\]

这条式子把 moving-prefix 的整数自由度 `J` 直接接到了 positive-excess identity。

---

## 3. positive-excess identity

沿用
\[
M=10^{k+g+1},
\qquad
\zeta=\frac{r_3}{M},
\qquad
\widehat R=\frac RM.
\]

`top-layer.md` 已严格证明
\[
\boxed{
\begin{aligned}
S={}&
\frac{\mathfrak h}{M\varepsilon}
\left(1+\varepsilon p+\widehat R\right)
+\frac{\zeta^2}{\varepsilon}\\
&+\varepsilon(2p+q^2-p^2)
+\varepsilon^2p^2,
\end{aligned}}
\tag{7}
\]
其中
\[
\frac{\mathfrak h}{M}
=
\lambda\left[(1+\varepsilon p)-H^{-1}(1-\varepsilon q)\right]
+\theta(\widehat R-\zeta),
\tag{8}
\]
并且所有 source 均为正。

在 `r=s=1` 中
\[
\boxed{
\frac{\lambda}{\varepsilon}
=\frac1{100-(10w-1)\varepsilon}.
}
\tag{9}
\]

---

## 4. `J>-1`

令
\[
d_0:=1-H^{-1}.
\]

从 (8) 丢掉正的 `theta` 项，并用
\[
\frac{\lambda}{\varepsilon}>\frac1{100},
\]
得到
\[
\frac{\mathfrak h}{M\varepsilon}
>
\frac1{100}(d_0+\varepsilon p).
\tag{10}
\]

又因为球面半径严格大于第二坐标，
\[
\widehat R>1-\varepsilon q.
\]
故
\[
1+\varepsilon p+\widehat R
>2+\varepsilon(p-q)>2-\frac1{10}\varepsilon.
\tag{11}
\]

把 (10)-(11) 与 curvature source 代入 (7)，再用 (6)：
\[
\begin{aligned}
\frac JH+1
>{}&d_0
+\varepsilon\Bigl[
 p-\frac1{20}d_0
 +50(2p+q^2-p^2)
 -10wp
\Bigr]\\
&-\frac1{20}\varepsilon^2p.
\end{aligned}
\tag{12}
\]

现在只需对两个绝对窄窗做 endpoint audit。

### `z=1`

这里
\[
q=\frac1{10},
\qquad1\le w\le4,
\qquad
\frac{817}{2000}<p<\frac{4111}{10000}.
\]

由于括号中关于 `p` 是凹二次式，其区间最小值在端点。取最坏 `w=4`、`d_0<1` 后，两个端点均给出大于
\[
17.
\]

### `z=3`

这里
\[
q=\frac3{10},
\qquad1\le w\le2,
\qquad
\frac{417}{2000}<p<\frac{2111}{10000}.
\]

同样取最坏 `w=2,d_0<1`，两个端点均给出大于
\[
19.
\]

因此六类型统一有
\[
\frac JH+1>d_0=1-\frac1H,
\]
即
\[
\boxed{J>-1.}
\tag{13}
\]

---

## 5. `k>=2g+1` 时 `J<0`

现在额外假设
\[
\boxed{k\ge2g+1.}
\tag{14}
\]

因为 `H=10^g`，
\[
\boxed{
\varepsilon=10^{-2k}
\le\frac1{100H^4}.
}
\tag{15}
\]

六类型统一使用粗界
\[
p<\frac12,
\qquad q\le\frac3{10},
\qquad w\le4.
\]

由 (9)：
\[
\frac{\lambda}{\varepsilon}
\le\frac1{100-39\varepsilon}.
\tag{16}
\]

同时
\[
\frac{\theta}{\varepsilon}
=
\frac{\lambda}{\varepsilon}\frac{\rho}{10^k}.
\]
而 `rho<10^g=H`，由 (14)
\[
\frac{\rho}{10^k}<\frac1{10H},
\]
所以
\[
\boxed{
\frac{\theta}{\varepsilon}
<
\frac1{10H}\frac1{100-39\varepsilon}.
}
\tag{17}
\]

由
\[
\widehat R<1+\varepsilon p<1+\frac12\varepsilon
\]
以及 (8)，得到
\[
\frac{\mathfrak h}{M\varepsilon}
<
\frac{
1-\frac9{10H}+\frac{535}{1000}\varepsilon
}{100-39\varepsilon}.
\tag{18}
\]

并且
\[
1+\varepsilon p+\widehat R<2+\varepsilon.
\]
因此 contact source 满足
\[
50S_{\rm contact}
<
\frac{1+\varepsilon/2}{1-0.39\varepsilon}
\left(
1-\frac9{10H}+0.535\varepsilon
\right).
\tag{19}
\]

由 (15) 特别有 `epsilon<=10^-6`，所以
\[
\frac{1+\varepsilon/2}{1-0.39\varepsilon}
<1+0.9\varepsilon.
\]
从而
\[
\boxed{
50S_{\rm contact}
<1-\frac9{10H}+2\varepsilon.
}
\tag{20}
\]

其余三个 source：

第三半径方面，`r_3<10^{1-g}=10/H`，故
\[
\frac{\zeta^2}{\varepsilon}<\frac1{H^4}.
\tag{21}
\]

curvature 方面
\[
2p+q^2-p^2<1.1,
\qquad
p^2<\frac14,
\]
所以
\[
50\left(
\frac{\zeta^2}{\varepsilon}
+\varepsilon(2p+q^2-p^2)
+\varepsilon^2p^2
\right)
<
\frac{50}{H^4}+67.5\varepsilon.
\tag{22}
\]

由 (15)，(20)-(22) 给
\[
50S
<
1-\frac9{10H}
+\frac{51}{H^4}.
\tag{23}
\]

而 `H>=10`，所以
\[
\frac{51}{H^4}<\frac9{10H}.
\]
于是
\[
\boxed{50S<1.}
\tag{24}
\]

最后由 (6)，减去的 `10w epsilon p` 还是严格正项，因此
\[
\frac JH+1<1,
\]
即
\[
\boxed{J<0.}
\tag{25}
\]

---

## 6. 整数矛盾

(13)、(25) 联立：
\[
\boxed{-1<J<0.}
\]

但 `J` 由 (4) 是整数，矛盾。

因此
\[
\boxed{
 d=2,\quad r=s=1,\quad g\ge1,\quad k\ge2g+1
 \Longrightarrow\text{empty}.
}
\tag{26}
\]

minimal diagonal `k=g` 已由 `minimal-diagonal-closure.md` 独立关闭，所以当前最小双 surplus 的 `g>=1` 前沿被严格压成
\[
\boxed{g<k\le2g.}
\tag{27}
\]

---

## 7. 与 minimal-diagonal phase normal form 的新桥

令
\[
T=10^k,
\qquad
\tau=10^{k-g}.
\]

由
\[
a_1=10^{g+1}b_1+U_1,
\qquad
b_2=10^{k-g},
\]
以及 (4)，精确得到
\[
\boxed{
 a_1b_2
 =100T^3
 +\bigl(10(5-z-w)+1\bigr)T
 +\tau J.
}
\tag{28}
\]

因此若定义
\[
\boxed{N_{\rm eff}:=\tau J+1,}
\tag{29}
\]
则
\[
\boxed{
 a_1b_2
 =100T^3
 +\bigl(10(5-z-w)+1\bigr)T
 +N_{\rm eff}-1.
}
\tag{30}
\]

这与 minimal diagonal 中被 phase-shell 方法关闭的第一 prefix square 具有完全相同的十进制形状。后续窄楔 `g<k<=2g` 应优先把 minimal-diagonal 的 exact phase remainder 改写到 `(tau,J)` 坐标，而不是重新从原始四块变量开始。
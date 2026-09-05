# A1 top layer: `s=1` far / low-`r` surplus collapse

> 日期：2026-08-22。
>
> 依赖：`top-layer.md` 的 half-gap sharpening、positive-excess decomposition 与 residue kernel。
>
> 范围：
> \[
> d=2,\qquad s=1,\qquad g\ge1,
> \]
> 以及
> \[
> k\ge2g+1,
> \qquad
> 1\le r\le3g-2.
> \]

状态：**严格关闭。** 本文把 minimal-surplus 中的 `J` phase identity 推广到任意 first surplus `r`，并关闭整个 far / low-`r` 条带。

最终：
\[
\boxed{
 d=2,\ s=1,\ k\ge2g+1,\ 1\le r\le3g-2
 \Longrightarrow\text{empty}.
}
\tag{1}

---

## 1. `s=1` 的固定 second residue

`top-layer.md` 的 half-gap theorem 对任意 `s=1,g>=1` 已给
\[
y=0,
\qquad
b_2=10^{k-g},
\qquad
z\in\{1,3\}.
\tag{2}
\]

令
\[
p:=\phi_1,
\qquad
q:=\phi_2=\frac z{10}.
\]
则
\[
\boxed{
\begin{array}{c|c}
z&p\\ \hline
1&(2/5,\ 217/500)\\
3&(1/5,\ 117/500)
\end{array}}
\tag{3}
\]

写
\[
\varepsilon:=10^{-2k},
\qquad
H:=10^g,
\qquad
W:=\frac{w}{10^r}.
\]
compact residue formula 给
\[
p=\frac{U_1/10^{r+g+1}}{1-\varepsilon W}.
\tag{4}
\]
因为 `U1=x+10^(g+1)w` 且 `x>=0`：
\[
W\le \frac{U_1}{10^{r+g+1}}=(1-\varepsilon W)p<p.
\tag{5}
\]
特别地
\[
\boxed{0<W<p<217/500<0.434.}
\tag{6}

---

## 2. general-`r` integer phase coordinate

定义整数
\[
\boxed{
U_1=(5-z)10^{r+g}+H+J,
\qquad J\in\mathbf Z.
}
\tag{7}

记
\[
S:=2(p+q)-1>0.
\]
由 (4)：
\[
\frac{U_1}{10^{r+g+1}}
=(1-\varepsilon W)p.
\]
而 (7) 左端等于
\[
\frac{5-z}{10}+10^{-r-1}\left(1+\frac JH\right).
\]
因为
\[
p-\frac{5-z}{10}=p+q-\frac12=\frac S2,
\]
整理得到 exact identity
\[
\boxed{
1+\frac JH
=5\cdot10^r S-10w\varepsilon p.
}
\tag{8}

当 `r=1` 时这正是此前 minimal-surplus 的
\[
1+J/H=50S-10w\varepsilon p.
\]

---

## 3. contact main term

positive-excess decomposition 为
\[
S=S_{\rm contact}+S_{\rm rad}
+\varepsilon(2p+q^2-p^2)+\varepsilon^2p^2,
\tag{9}
\]
其中
\[
S_{\rm rad}=\frac{\zeta^2}{\varepsilon},
\qquad
\frac{\zeta^2}{\varepsilon}<10^{-4g}.
\tag{10}

令
\[
\delta:=\frac{\rho}{10^k}.
\]
在 far region `k>=2g+1`：
\[
0<\delta<10^{g-k}\le10^{-g-1}\le10^{-2}.
\tag{11}

又 `s=1` 时
\[
\frac{\lambda}{\varepsilon}
=
\frac{10^{-r-1}}
{1-(10w-1)10^{-2k-r-1}}.
\]
定义
\[
\Lambda:=10^{r+1}\frac{\lambda}{\varepsilon}.
\]
由 (6)：
\[
0<(10w-1)10^{-2k-r-1}<W\varepsilon<0.434\varepsilon.
\]
而 far region 有 `epsilon<=10^-6`，故
\[
1<\Lambda<1+0.435\varepsilon.
\tag{12}

contact-height bracket 写成
\[
(1+\varepsilon p)-H^{-1}(1-\varepsilon q)
+\delta(\widehat R-\zeta).
\]
记主中心
\[
\boxed{B_0:=1-H^{-1}+\delta.}
\tag{13}

由
\[
1-\varepsilon q<\widehat R<1+\varepsilon p
\]
和 third-radius bound，可取安全统一误差
\[
\left|
(1+\varepsilon p)-H^{-1}(1-\varepsilon q)
+\delta(\widehat R-\zeta)-B_0
\right|<0.61\varepsilon.
\tag{14}

同时
\[
\left|\frac{1+\varepsilon p+\widehat R}{2}-1\right|<0.434\varepsilon.
\tag{15}

由 (12)--(15)，将 contact source 乘 `5*10^r` 后得到
\[
\boxed{
B_0-2\varepsilon
<5\cdot10^rS_{\rm contact}
<B_0+2\varepsilon.
}
\tag{16}

---

## 4. curvature pays for the denominator correction

令
\[
f(p,q):=2p+q^2-p^2.
\]
由 (3)，逐 endpoint 检查：
\[
\boxed{f(p,q)-2p^2>0.31.}
\tag{17}

由 (5)：
\[
10w\varepsilon p
=10^{r+1}W\varepsilon p
<10^{r+1}\varepsilon p^2.
\]
所以
\[
\begin{aligned}
&5\cdot10^r\varepsilon f(p,q)
-10w\varepsilon p\\
&\qquad>
5\cdot10^r\varepsilon\bigl(f(p,q)-2p^2\bigr)\\
&\qquad>
1.55\cdot10^r\varepsilon.
\end{aligned}
\tag{18}

因为 `r>=1`，右端大于 `15.5 epsilon`，足以严格覆盖 (16) 可能损失的 `2 epsilon`。radius 与 `epsilon^2 p^2` 仍非负。

将 (9),(16),(18) 代入 (8)：
\[
1+\frac JH>B_0.
\]
由 (13)：
\[
\boxed{
J+1>H\delta=\rho\,10^{g-k}>0.
}
\tag{19}

特别地
\[
\boxed{J+1\in\mathbf Z_{>0}.}
\tag{20}

---

## 5. upper phase width in the low-`r` strip

从 (8),(9) 做上界时丢掉负项 `-10w epsilon p`。由 (16)：
\[
5\cdot10^rS_{\rm contact}<B_0+2\varepsilon.
\]

radius 由 (10)：
\[
5\cdot10^rS_{\rm rad}<5\cdot10^{r-4g}.
\tag{21}

由 (3) 可安全取
\[
f(p,q)<0.7,
\qquad p^2<0.19,
\]
故 curvature 两项满足
\[
5\cdot10^r
\left(\varepsilon f+\varepsilon^2p^2\right)
<3.51\cdot10^r\varepsilon.
\tag{22}

于是
\[
0<J+1-\rho10^{g-k}
<2H\varepsilon
+5\cdot10^{r-3g}
+3.51\cdot10^{r+g-2k}.
\tag{23}

现在使用
\[
k\ge2g+1,
\qquad
r\le3g-2.
\]
三项分别满足
\[
2H\varepsilon\le2\cdot10^{-3g-2}<2\cdot10^{-5},
\]
\[
5\cdot10^{r-3g}\le\frac1{20},
\]
\[
3.51\cdot10^{r+g-2k}
\le3.51\cdot10^{-4}<0.000351.
\]
所以安全地
\[
\boxed{
0<J+1-\rho10^{g-k}<\frac15.
}
\tag{24}

---

## 6. integer contradiction

far condition 给
\[
0<\rho10^{g-k}<10^{2g-k}\le\frac1{10}.
\tag{25}

由 (24)-(25)：
\[
0<J+1<rac3{10}.
\]
但 (20) 说明 `J+1` 是正整数。矛盾。

因此得到 (1)。

---

## 7. new frontier on the `s=1` edge

本文之后，`s=1` 的 far region只可能满足
\[
\boxed{
k\ge2g+1,\qquad r\ge3g-1}
\]
（另加非 far 区 `k<=2g`）。

下一步应对 `r>=3g-1` 保留 amplified third-radius source，而不能再把它作为误差丢掉；在该区它正好成为新的主相位。
# `A_2` low-defect angle squeeze

> 分支：`agent/a2-hensel-resultant-progress`  
> 状态：**已严格完成两个低商状态的额外十进制窗口收缩。**  
> 依赖：[`a2-decimal-ellipse-phase.md`](a2-decimal-ellipse-phase.md) 与 [`a2-ellipse-to-defect-window.md`](a2-ellipse-to-defect-window.md)。

本文利用 finite-defect 商的上界

\[
J_{\rm def}=k+\frac RD<k+1
\]

反向给 canonical angle \(T/A\) 一个下界，再与前一文件的 ellipse 上界夹逼。其作用集中在 \((a,k)=(9,2)\) 与 \((11,3)\)。

---

## 1. 从 `J_def < k+1` 得到 angle 下界

记

\[
s:=\frac{H_0-Y_3}{H_0+Y_3}
=
\frac{J_{\rm def}}{J_{\rm def}+2\zeta},
\qquad
\zeta=\frac{a_3}{10^m}>1.
\]

因为 \(J_{\rm def}<k+1\)，函数 \(J/(J+2\zeta)\) 关于 \(J\) 递增、关于 \(\zeta\) 递减，所以

\[
\boxed{
s<\frac{k+1}{k+3}=:s_k.}
\tag{1.1}
\]

canonical mixed-sign ratio 为

\[
r_{\rm can}:=\frac{A-T}{A+T}
=\frac{fZ}{qW}
=\frac{s}{\vartheta},
\]

其中前一文件已证

\[
\vartheta=rac{5^Eq}{f}
>artheta_{11}:=\frac{10^{11}}{10^{11}+1}
\]

对全部当前开放范围 \(M\ge11\) 成立。因此

\[
r_{\rm can}<\frac{s_k}{\vartheta_{11}}.
\]

而

\[
\frac TA=\frac{1-r_{\rm can}}{1+r_{\rm can}},
\]

故

\[
\boxed{
\frac TA>\lambda_k
:=
\frac{\vartheta_{11}-s_k}{\vartheta_{11}+s_k}.
}
\tag{1.2}
\]

对两个关键低商状态：

\[
\boxed{
\lambda_2
=\frac{199999999997}{800000000003}
=0.2499999999953125\ldots,
}
\tag{1.3}
\]

\[
\boxed{
\lambda_3
=\frac{49999999999}{250000000001}
=0.1999999999952\ldots.
}
\tag{1.4}
\]

所以 \(k=2\) 几乎强制 \(T/A>1/4\)，\(k=3\) 几乎强制 \(T/A>1/5\)。

---

## 2. 与 scale-free ellipse 上界夹逼

前一文件已证

\[
\left(\frac TA\right)^2<H_a(x,y)<H_a(x,1),
\]

其中

\[
H_a(x,1)
=-\frac{
25a^2x^4+100a^2x^3-(200a+99)x^2+4x+4
}{100x^2(a+1)^2},
\]

且

\[
\frac d{dx}H_a(x,1)
=-\frac{(x+2)(25a^2x^3-2)}{50x^3(a+1)^2}.
\]

对于 \(a=9,11\)，唯一正临界点

\[
x_*=(2/(25a^2))^{1/3}
\]

都严格小于 \(1/10\)。因此 \(H_a(x,1)\) 在整个合法窗口 \(x\ge1/10\) 上严格递减。

---

## 3. `已严格完成`：`a=9,k=2` 只剩最左 `6%` 薄层

若 \(a=9,k=2\)，由 (1.2)–(1.3)

\[
\left(\frac TA\right)^2>\lambda_2^2.
\]

另一方面精确有理计算给出

\[
H_9\!\left(\frac{53}{500},1\right)
<\lambda_2^2.
\tag{3.1}
\]

两边之差精确为正：

\[
\lambda_2^2-H_9(53/500,1)
=
\frac{19547494618796606215170368636649}
{179776000001348320000002528100000000}>0.
\]

由于 \(H_9(x,1)\) 在 \([1/10,3/20)\) 上递减，若 \(x\ge53/500\)，则

\[
(T/A)^2<H_9(x,1)\le H_9(53/500,1)<\lambda_2^2,
\]

与 angle 下界矛盾。

故

\[
\boxed{
(a,k)=(9,2)
\Longrightarrow
\frac1{10}\le x<\frac{53}{500}.
}
\tag{3.2}
\]

原窗口为 \(1/10\le x<3/20\)，现在只剩左端宽度 \(0.006\)。

---

## 4. `已严格完成`：`a=11,k=3` 只剩最左 `9%` 薄层

若 \(a=11,k=3\)，同理由 (1.4)

\[
(T/A)^2>\lambda_3^2.
\]

精确有理计算：

\[
H_{11}\!\left(\frac{109}{1000},1\right)
<\lambda_3^2,
\tag{4.1}
\]

且

\[
\lambda_3^2-H_{11}(109/1000,1)
=
\frac{17192037971391456305230243712609}
{47524000000380192000000760384000000}>0.
\]

由于 \(H_{11}(x,1)\) 在合法窗口递减，得到

\[
\boxed{
(a,k)=(11,3)
\Longrightarrow
\frac1{10}\le x<\frac{109}{1000}.
}
\tag{4.2}
\]

原窗口为 \(1/10\le x<1/8\)，现只剩 \([0.1,0.109)\)。

---

## 5. 当前意义

结合上一文件：

\[
(a,k)=(9,2):
\qquad
\frac RD>\frac{21}{25},
\qquad
\frac1{10}\le x<\frac{53}{500},
\]

\[
(a,k)=(11,3):
\qquad
\frac RD>\frac{19}{25},
\qquad
\frac1{10}\le x<\frac{109}{1000}.
\]

因此这两个状态同时受到：

1. CRT 余量必须位于 \((0,D)\) 的最顶部；
2. 第二分母归一化量必须位于其 core window 的最左端；
3. canonical angle 必须位于极窄区间
   \[
   \lambda_k<T/A<\text{core cap}.
   \]

下一步应把 \(x=2^{m+t}u/5^M\) 的 source 格点和统一 square-depth CRT 代表一起代入这两个薄层，而不再对完整原参数空间做无差别搜索。

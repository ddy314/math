# A1 top-layer diagonal significand lock — 2026-08-17

本文继续 `a1-top-layer-minimal-diagonal-2026-08-17.md`，仍处于

\[
d=2,
\qquad
r=s=1,
\qquad
k=g\ge2.
\]

上一文件得到

\[
U_1=(5-z)10^{k+1}+j,
\qquad
0\le j<\frac{17}{5}10^k.
\]

本文把 positive excess decomposition 与 diagonal identity

\[
\frac\theta\lambda
=\frac{b_3}{10^{m_3}}
\]

结合，证明 prefix remainder `j` 与第三分母的十进制 significand 被直接锁在一起。

定义

\[
\boxed{
 u=\frac{j}{10^{k+1}},
}
\]

\[
\boxed{
 \sigma=\frac{b_3}{10^{m_3}}\in[0.1,1).
}
\]

核心结论：

\[
\boxed{
0.098+0.099\sigma
<u
<0.101+0.101\sigma.
}
\]

因此

\[
\boxed{
\left|
\frac{j}{10^k}-(1+\sigma)
\right|<0.03.
}
\]

本文结论均为 **已严格完成**。

---

## 1. diagonal 中 `phi_1` 的精确 `u` 表达

令

\[
c=5-z\in\{4,2\}.
\]

由上一文件

\[
U_1=c10^{k+1}+j
=10^{k+1}(c+u).
\]

又

\[
b_1=10^{2k+1}-w.
\]

在 diagonal 中自然 gap 尺度是 `10`，所以

\[
\phi_1
=\frac{10^kU_1/b_1}{10}
=\frac{10^{k-1}U_1}{b_1}.
\]

代入后除以 `10^{2k}`：

\[
\boxed{
\phi_1
=\frac{c+u}{10-w\varepsilon},
}
\tag{1}
\]

其中

\[
\varepsilon=10^{-2k}.
\]

而

\[
\phi_2=\frac z{10}.
\]

因此总 normalized gap

\[
\Phi:=\phi_1+\phi_2
\]

满足

\[
2\Phi-1
=2\frac{c+u}{10-w\varepsilon}+rac z5-1.
\]

因为 `c=5-z`，整理为

\[
\boxed{
2\Phi-1
=\frac{10u+cw\varepsilon}
{5(10-w\varepsilon)}.
}
\tag{2}
\]

等价地

\[
\boxed{
 u
=5(2\Phi-1)
-\frac{w\varepsilon}{2}(2\Phi-1)
-\frac{cw\varepsilon}{10}.
}
\tag{3}

---

## 2. `lambda/epsilon` 在 diagonal 中几乎精确为 `1/100`

最小边界中

\[
\lambda=\frac1{10b_1+1}.
\]

所以

\[
\frac\lambda\varepsilon
=\frac1{100-(10w-1)\varepsilon}.
\]

六类型有 `w\le4`，并且 `k\ge2` 给出

\[
\varepsilon\le10^{-4}.
\]

因此

\[
\boxed{
\frac1{100}
<\frac\lambda\varepsilon
<0.010001.
}
\tag{4}
\]

---

## 3. 第三 contact 比例就是第三分母 significand

写

\[
\rho=\frac{b_3}{10^\ell}.
\]

由于 diagonal 中

\[
g=k,
\qquad
m_3=k+\ell,
\]

有

\[
\frac\rho{10^k}
=\frac{b_3}{10^{k+\ell}}
=\frac{b_3}{10^{m_3}}
=\sigma.
\]

而最小边界满足

\[
\frac\theta\lambda=\frac\rho{10^k}.
\]

所以

\[
\boxed{
\theta=\sigma\lambda.
}
\tag{5}
\]

这是 diagonal 中 prefix-contact 与 third-contact 的精确比例。

---

## 4. positive excess 的下界

沿用正项分解

\[
\begin{aligned}
E:=2\Phi-1
={}&
\frac{\mathfrak h}{M\varepsilon}
\left(1+\varepsilon\phi_1+\frac RM\right)\\
&+\frac{(r_3/M)^2}{\varepsilon}
+\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
+\varepsilon^2\phi_1^2.
\end{aligned}
\tag{6}
\]

其中

\[
\frac{\mathfrak h}{M}
=\lambda A+\theta B,
\]

\[
A=(1+\varepsilon\phi_1)
-10^{-k}(1-\varepsilon\phi_2),
\]

\[
B=\frac RM-\frac{r_3}{M}.
\]

因为 `k\ge2`：

\[
10^{-k}\le0.01,
\]

故

\[
\boxed{A>0.99.}
\tag{7}
\]

又

\[
\frac RM>\frac{r_2}{M}=1-\varepsilon\phi_2
\ge1-0.3\cdot10^{-4}>0.99997.
\]

最高层还有

\[
\frac{r_3}{M}<10^{-3k}\le10^{-6},
\]

所以

\[
\boxed{B>0.9999.}
\tag{8}
\]

结合 (4)、(5)、(7)、(8)：

\[
\frac{\mathfrak h}{M\varepsilon}
>
0.01(0.99+0.9999\sigma).
\tag{9}
\]

此外

\[
1+\varepsilon\phi_1+R/M
>1+0.99997>1.9999.
\]

因此只保留 (6) 第一正项即可得到

\[
\boxed{
E
>0.01979+0.01997\sigma.
}
\tag{10}
\]

---

## 5. positive excess 的上界

half-gap kernel 给出

\[
\phi_1<0.434,
\qquad
\phi_2\le0.3.
\]

故

\[
1+\varepsilon\phi_1<1.000044.
\]

于是

\[
A<1.000044,
\qquad
B<1.000044.
\]

由 (4)、(5)：

\[
\frac{\mathfrak h}{M\varepsilon}
<0.010001\cdot1.000044(1+\sigma).
\]

又

\[
1+\varepsilon\phi_1+R/M<2.000088.
\]

所以第一 source 小于

\[
0.020013(1+\sigma).
\tag{11}
\]

第三半径满足

\[
\frac{(r_3/M)^2}{\varepsilon}
<10^{-4k}
\le10^{-8}.
\tag{12}
\]

曲率项满足

\[
\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
<10^{-4}(0.868+0.09)
<0.000096,
\tag{13}
\]

以及

\[
\varepsilon^2\phi_1^2<2\cdot10^{-9}.
\tag{14}
\]

故

\[
\boxed{
E
<0.020013(1+\sigma)+0.000097.
}
\tag{15}
\]

---

## 6. 转回 `u`

由精确式 (3)：

\[
u
=5E
-\frac{w\varepsilon}{2}E
-\frac{cw\varepsilon}{10}.
\]

### 下界

由 (10)：

\[
5E>0.09895+0.09985\sigma.
\]

又六类型中

\[
w,c\le4,
\qquad
\varepsilon\le10^{-4},
\qquad
E<0.041,
\]

所以两个减项之和小于 `0.00017`。于是

\[
\boxed{
 u>0.098+0.099\sigma.
}
\tag{16}
\]

### 上界

从 (3) 直接丢掉两个负项并用 (15)：

\[
u<5E
<0.100065(1+\sigma)+0.000485.
\]

因此

\[
\boxed{
 u<0.101+0.101\sigma.
}
\tag{17}
\]

合并 (16)–(17)：

\[
\boxed{
0.098+0.099\sigma
<u
<0.101+0.101\sigma.
}
\tag{18}
\]

---

## 7. 十进制 significand lock

因为

\[
u=\frac{j}{10^{k+1}},
\]

把 (18) 与

\[
0.1(1+\sigma)
\]

比较：

下侧误差最多

\[
0.1(1+\sigma)-(0.098+0.099\sigma)
=0.002+0.001\sigma<0.003,
\]

上侧误差最多

\[
(0.101+0.101\sigma)-0.1(1+\sigma)
=0.001+0.001\sigma<0.002.
\]

所以

\[
\boxed{
\left|
 u-\frac{1+\sigma}{10}
\right|<0.003.
}
\tag{19}
\]

乘以 `10`：

\[
\boxed{
\left|
\frac{j}{10^k}-(1+\sigma)
\right|<0.03.
}
\tag{20}
\]

最后代回

\[
\sigma=\frac{b_3}{10^{m_3}}:
\]

\[
\boxed{
\left|
\frac{j}{10^k}
-
1
-
\frac{b_3}{10^{m_3}}
\right|<0.03.
}
\tag{21}
\]

这是一条直接连接 moving prefix 与第三分母 leading decimal 的约束。

---

## 8. `j` 的位数被锁定

由 `sigma>=0.1` 和 (18)：

\[
u>0.098+0.0099=0.1079.
\]

由 `sigma<1`：

\[
u<0.101+0.101=0.202.
\]

所以

\[
1.079
<\frac{j}{10^k}
<2.02.
\]

因此

\[
\boxed{j\text{ 恰有 }k+1\text{ 位}.}
\tag{22}
\]

若

\[
\frac j{10^k}\ge2,
\]

则由 (20)

\[
1+\sigma>1.97,
\]

所以

\[
\boxed{
 j\text{ 以 }2\text{ 开头}
\Longrightarrow
\sigma>0.97.
}
\tag{23}
\]

除第三分母 significand 已经落在最顶部 `3%` 的情形外，`j` 必须以十进制数字 `1` 开头。

---

## 9. 当前意义

minimal diagonal kernel 现在具有直接的 prefix-tail 数字锁：

\[
\frac j{10^k}-1
\approx
\frac{b_3}{10^{m_3}}
\]

误差严格小于 `0.03`。

这说明第三分母的 leading decimal 已不再只通过抽象 `theta` 进入证明；它与 prefix remainder `j` 的 leading decimal 发生直接耦合。

下一步应把该 significand lock 与：

- `b_3\mid10^{2m_3}Q^2G`；
- `2/5` resonance/cross-corridor 赋值；
- `j` 在六 `(z,w)` 类型中的同余；

联用，尝试把 `0.03` 窗继续压到单个 leading-prefix 或产生模矛盾。

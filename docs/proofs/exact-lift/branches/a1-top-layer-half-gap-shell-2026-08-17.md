# A1 top-layer half-gap shell — 2026-08-17

本文继续 `a1-top-layer-residue-kernel-2026-08-17.md`，在最高层

\[
d=s_1-g=2,
\qquad g\ge1
\]

中把两个既约 rational defects 的总 gap 从此前的粗窗口进一步压到一个宽度约 `0.035` 的半单位壳层。

核心结论是

\[
\boxed{
\frac{499}{1000}
<
\frac{
10^kU_1/b_1+U_2/b_2
}{10^{g+1-k}}
<
\frac{267}{500}.
}
\]

特别地，最小第二 surplus `s=1` 时强迫

\[
\boxed{z\in\{1,3\}.}
\]

本文结论均为 **已严格完成**。

---

## 1. 记号

沿用

\[
M=10^{k+g+1},
\qquad
A_0=10^k r_1,
\]

\[
t=\frac{r_2}{A_0},
\qquad
R_0=\frac R{A_0},
\qquad
q_0=\frac{r_3}{A_0},
\]

以及

\[
\varepsilon=10^{-2k},
\qquad
\delta=1-t,
\qquad
\alpha=1-R_0.
\]

前文已严格证明，在 `d=2,g\ge1` 中

\[
r=m_1-2k\ge1,
\qquad
s=m_2+g-k\ge1,
\]

并且

\[
\boxed{0<\delta<\frac45\varepsilon.}
\tag{1}
\]

球面关系为

\[
R_0^2=t^2+\varepsilon+q_0^2.
\tag{2}
\]

---

## 2. `alpha/epsilon` 只有百分之二量级

contact 恒等式给出

\[
\alpha
=\lambda(1-10^{-g}t)
+
\theta(R_0-q_0),
\]

其中

\[
0<\theta<\frac1Q,
\qquad
\lambda=\frac{b_2}{Q}.
\]

所以

\[
\boxed{0<\alpha<\lambda+\frac1Q.}
\tag{3}
\]

最高层四因子分解与 (1) 说明每一个因子都大于 `t=1-delta`。因此

\[
\frac{b_1}{10^{m_1}}>1-\delta,
\qquad
\frac{b_2}{10^{m_2-1}}<\frac1{1-\delta}.
\]

于是

\[
\lambda
<
\frac{10^{-m_1-1}}{(1-\delta)^2}.
\]

因为

\[
m_1=2k+r,\qquad r\ge1,
\]

除以 `epsilon=10^{-2k}`：

\[
\frac\lambda\varepsilon
<
\frac{10^{-r-1}}{(1-\delta)^2}
\le
\frac{10^{-2}}{(1-0.008)^2}
<0.0102.
\tag{4}
\]

另一方面

\[
\frac1Q
<
\frac1{b_1 10^{m_2}}
<
\frac{10^{-m_1-m_2}}{1-\delta}.
\]

由于 `r\ge1,m_2\ge1`：

\[
\frac1{Q\varepsilon}
<
\frac{10^{-r-m_2}}{1-\delta}
\le
\frac{10^{-2}}{0.992}
<0.0101.
\tag{5}
\]

由 (3)–(5)：

\[
\boxed{
0<\frac\alpha\varepsilon<0.0203.
}
\tag{6}
\]

---

## 3. `delta/epsilon` 被压到 `1/2` 附近

由

\[
R_0=1-\alpha,
\qquad
t=1-\delta,
\]

把球面式 (2) 展开：

\[
1-2\alpha+\alpha^2
=1-2\delta+\delta^2+\varepsilon+q_0^2.
\]

所以

\[
\boxed{
2(\delta-\alpha)
=\varepsilon+q_0^2+\delta^2-\alpha^2.
}
\tag{7}
\]

最高层有

\[
q_0<10^{-k-2g},
\]

因此

\[
\boxed{
\frac{q_0^2}{\varepsilon}<10^{-4g}\le10^{-4}.
}
\tag{8}
\]

由 (1)：

\[
\frac{\delta^2}{2\varepsilon}
<\frac{8}{25}\varepsilon
\le0.0032.
\tag{9}
\]

结合 (6)–(9)，从 (7) 得到

\[
\frac\delta\varepsilon
<
\frac12+0.0203+0.00005+0.0032
<\frac{21}{40}.
\]

即

\[
\boxed{
\frac\delta\varepsilon<\frac{21}{40}.
}
\tag{10}
\]

下界方面，(6) 给出 `alpha<0.0203 epsilon`，故 `alpha^2<epsilon^2/1600`。由 (7) 丢掉正的 `alpha,q_0,delta^2` 项，仅保留可能的 `-alpha^2`：

\[
\frac\delta\varepsilon
>
\frac12-rac{\alpha^2}{2\varepsilon}
>
\frac12-rac1{320000}
>
\frac{499}{1000}.
\]

所以

\[
\boxed{
\frac{499}{1000}
<\frac\delta\varepsilon
<\frac{21}{40}.
}
\tag{11}
\]

---

## 4. carrier gap 的半单位壳层

定义真实 carrier gap

\[
D_0:=A_0-r_2=\delta A_0.
\]

自然十进制尺度为

\[
\boxed{
H_0=M\varepsilon=10^{g+1-k}.
}
\tag{12}
\]

端点坐标给出

\[
\frac{A_0}{M}
=
\frac{1+\varepsilon X}{1-\varepsilon W}.
\]

四因子乘积为 `t=1-delta`，故

\[
\frac1{1+\varepsilon X}>1-\delta,
\qquad
1-\varepsilon W>1-\delta.
\]

于是

\[
1<\frac{A_0}{M}<\frac1{(1-\delta)^2}
<\left(\frac{125}{124}\right)^2.
\tag{13}
\]

因为

\[
\frac{D_0}{H_0}
=\frac\delta\varepsilon\frac{A_0}{M},
\]

由 (11)–(13)：

\[
\frac{D_0}{H_0}>rac{499}{1000},
\]

并且

\[
\frac{D_0}{H_0}
<
\frac{21}{40}\left(\frac{125}{124}\right)^2
<\frac{267}{500}.
\]

因此

\[
\boxed{
\frac{499}{1000}
<
\frac{D_0}{10^{g+1-k}}
<
\frac{267}{500}.
}
\tag{14}
\]

---

## 5. 用两个 coprime residues 重写半单位壳层

由 residue kernel：

\[
D_0
=10^k\frac{U_1}{b_1}+\frac{U_2}{b_2}.
\]

所以 (14) 等价于

\[
\boxed{
\frac{499}{1000}
<
\frac{
10^kU_1/b_1+U_2/b_2
}{10^{g+1-k}}
<
\frac{267}{500}.
}
\tag{15}
\]

此外利用

\[
U_1=10^{r+g+1}(X+W),
\qquad
b_1=10^{2k+r}(1-\varepsilon W),
\]

\[
U_2=10^s(Y+Z),
\qquad
b_2=10^{k-g+s-1}(1+\varepsilon Y),
\]

可以把 (15) 精确写成

\[
\boxed{
\frac{499}{1000}
<
\frac{X+W}{1-\varepsilon W}
+
\frac{Y+Z}{1+\varepsilon Y}
<
\frac{267}{500}.
}
\tag{16}
\]

这比此前 `Delta/L0` 的 `1/2`–`5/6` 窗显著更窄。

---

## 6. 最小第二 surplus `s=1`

若

\[
s=1,
\]

则前文已有

\[
s\le k+g,
\]

故

\[
y=0,
\qquad
b_2=10^{m_2-1}=10^{k-g},
\]

并且

\[
\gcd(z,10)=1.
\]

此时

\[
Y=0,
\qquad
Z=\frac z{10},
\]

而 (16) 中第一项严格为正。因此

\[
\frac z{10}<\frac{267}{500}=0.534,
\]

所以

\[
z\le5.
\]

再由 `gcd(z,10)=1`：

\[
\boxed{z\in\{1,3\}.}
\tag{17}
\]

两个子核分别满足：

### `z=1`

\[
\boxed{
\frac{399}{1000}
<
\frac{X+W}{1-\varepsilon W}
<
\frac{217}{500}.
}
\tag{18}
\]

### `z=3`

\[
\boxed{
\frac{199}{1000}
<
\frac{X+W}{1-\varepsilon W}
<
\frac{117}{500}.
}
\tag{19}
\]

所以 `s=1` 已经压成两个明确的第一余量窄窗。

---

## 7. 当前意义

最高层 `d=2,g\ge1` 现已具有一条真正的半单位刚性：

\[
10^k\frac{U_1}{b_1}+\frac{U_2}{b_2}
\]

只能落在

\[
(0.499,0.534)\cdot10^{g+1-k}
\]

中，而两个分数各自既约。

因此后续可以按 `s` 从小到大继续：

- `s=1` 已只剩 `z=1,3`；
- 一般短 `s\le k+g` 中 `y=0`，故第二项精确为 `z/10^s`，并且 `gcd(z,10)=1`；
- 长 `s>k+g` 才允许 `y>0`，需要单独研究。

这提供了一条比原四-offset kernel 更适合做有限 leading-digit / p-adic 分层的入口。

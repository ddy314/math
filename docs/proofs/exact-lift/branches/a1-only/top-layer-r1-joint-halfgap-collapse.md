# A1 top layer: `r=1` joint half-gap phase collapse

> 日期：2026-08-22。
>
> 依赖：`top-layer.md` 的 residue kernel、half-gap sharpening 与 positive-excess decomposition。
>
> 范围：
> \[
> d=2,\qquad r=1,\qquad s\ge2,\qquad g\ge1.
> \]

状态：**严格关闭一个 prefix-uniform 稳定区。** 本文把两个 coprime residues 合并成一个 joint half-gap integer，并证明在 third-contact / squared-tail / curvature 三个尺度都尚未越界时不存在候选。

最终：若
\[
\boxed{
 k+s\ge2g+2,
 \qquad
 N:=\max(g+2,s)\le4g,
 \qquad
 N\le2k-2,
}
\tag{1}
\]
则
\[
\boxed{
 d=2,\ r=1,\ s\ge2
 \Longrightarrow\text{empty}.
}
\tag{2}

---

## 1. decimal residue coordinates

令
\[
\varepsilon:=10^{-2k},
\qquad
H:=10^g.
\]
在 `r=1` 中写
\[
W:=w/10.
\]
一般 second residue 写
\[
Y:=10^{k+g+1-s}y,
\qquad
Z:=z/10^s.
\]

residue kernel 给
\[
A:=\frac{U_1}{10^{g+2}}=X+W,
\qquad
B:=\frac{U_2}{10^s}=Y+Z,
\tag{3}
\]
以及
\[
\boxed{
 p:=\phi_1=\frac{A}{1-\varepsilon W},
 \qquad
 q:=\phi_2=\frac{B}{1+\varepsilon Y}.
}
\tag{4}

half-gap shell 给
\[
\boxed{
\frac12<p+q<\frac{267}{500}<0.534.
}
\tag{5}
特别地
\[
0<p,q<0.534.
\tag{6}

由 `A=X+W>=W` 与 (4)：
\[
\boxed{0<W<p<0.534.}
\tag{7}

同理 `B=Y+Z>=Y`，由 (4)：
\[
Y\le q(1+\varepsilon Y).
\]
本文的 (1) 强迫 `k>=2`，故 `epsilon<=10^-4`。因此
\[
\boxed{0\le Y<0.535.}
\tag{8}

---

## 2. joint half-gap integer

令
\[
\boxed{N:=\max(g+2,s).}
\]
因为 `A` 的十进制分母整除 `10^(g+2)`，`B` 的十进制分母整除 `10^s`，所以
\[
\boxed{
\mathcal J
:=10^N\left(A+B-\frac{51}{100}\right)
\in\mathbf Z.
}
\tag{9}

又 `N>=g+2`，定义
\[
\boxed{
K:=\mathcal J+10^{N-g-2}\in\mathbf Z.
}
\tag{10}

记
\[
S:=2(p+q)-1>0,
\qquad
T:=10^{N-2}.
\]
由 (4)：
\[
A+B
=p+q+\varepsilon(Yq-Wp).
\]
所以
\[
100(A+B-51/100)
=50S-1+100\varepsilon(Yq-Wp).
\]
结合 (9)-(10)：
\[
\boxed{
\frac KT
=50S-\left(1-\frac1H\right)
+100\varepsilon(Yq-Wp).
}
\tag{11}

这是一般 `s` 的 joint 版本；当 `s=1`、`N=g+2` 时退化为此前单 residue `J` identity。

---

## 3. contact phase

rational-contact definitions 给
\[
\lambda=\frac{b_2}{Q},
\qquad
\theta=\frac{\rho}{HQ},
\]
故
\[
\boxed{
\frac\theta\lambda=\frac\rho{Hb_2}.
}
\tag{12}
定义
\[
\boxed{
\delta:=\frac\rho{Hb_2}.
}
\tag{13}

在 `r=1`，由
\[
b_1=10^{2k+1}(1-\varepsilon W),
\]
\[
b_2=10^{m_2-1}(1+\varepsilon Y),
\]
直接得到
\[
\boxed{
100\frac\lambda\varepsilon
=
\frac{1+\varepsilon Y}
{1-\varepsilon W+\frac\varepsilon{100}(1+\varepsilon Y)}.
}
\tag{14}
由 (7)-(8)、`epsilon<=10^-4`：
\[
\left|100\frac\lambda\varepsilon-1\right|<1.1\varepsilon.
\tag{15}

positive-excess contact bracket 为
\[
(1+\varepsilon p)-H^{-1}(1-\varepsilon q)
+\delta(\widehat R-\zeta).
\tag{16}

由 (1) 的 `k+s>=2g+2` 与 `rho<H`、`b2>=10^(k-g+s-1)`：
\[
0<\delta<10^{g-k-s+1}\le10^{-g-1}\le10^{-2}.
\tag{17}

又
\[
1-\varepsilon q<\widehat R<1+\varepsilon p
\]
以及 third-radius bound 给出的 `delta*zeta<epsilon/H`，所以 (16) 与
\[
B_0:=1-H^{-1}+\delta
\]
之差绝对值小于 `0.6 epsilon`。

再由
\[
\left|\frac{1+\varepsilon p+\widehat R}{2}-1\right|<0.534\varepsilon,
\]
和 (15)，可安全得到
\[
\boxed{
B_0-3\varepsilon
<50S_{\rm contact}
<B_0+3\varepsilon.
}
\tag{18}

---

## 4. curvature pays the only negative decimal correction

由 (5) 可证明统一不等式
\[
\boxed{
2p+q^2-3p^2>0.21.
}
\tag{19}
证明：

- 若 `p>=1/2`，则 `p<0.534`，故
  \[
  2p-3p^2>2(0.534)-3(0.534)^2>0.21;
  \]
- 若 `p<1/2`，由 `p+q>1/2` 有 `q>1/2-p`，所以
  \[
  2p+q^2-3p^2
  >\frac14+p-2p^2\ge\frac14.
  \]

由 (7)：
\[
-100\varepsilon Wp>-100\varepsilon p^2.
\]
所以 curvature source 与该负项合并后：
\[
\begin{aligned}
&50\varepsilon(2p+q^2-p^2)
-100\varepsilon Wp\\
&\qquad>
50\varepsilon(2p+q^2-3p^2)
>10.5\varepsilon.
\end{aligned}
\tag{20}

`+100 epsilon Yq`、third-radius source 与 `epsilon^2p^2` 均非负。因此 (18),(20) 与 (11) 给
\[
\boxed{
\frac KT>\delta+50S_{\rm rad}>0.
}
\tag{21}
特别地
\[
\boxed{K\in\mathbf Z_{>0}.}
\tag{22}

---

## 5. exact squared-tail phase

沿用
\[
\psi:=10^{g-1}r_3,
\qquad0<\psi<1.
\]
positive-excess 中
\[
S_{\rm rad}=rac{r_3^2}{10^{2g+2}}.
\]
因此
\[
\boxed{
50T S_{\rm rad}
=5\cdot10^{N-4g-1}\psi^2.
}
\tag{23}

---

## 6. uniform upper remainder

上界时从 (11) 丢掉负项 `-100 epsilon Wp`。由 (18)：contact error `<3 epsilon`。

又由 (6),(8)：
\[
2p+q^2-p^2<1.354,
\]
\[
100Yq<28.6,
\qquad
50\varepsilon p^2<0.002\quad(\varepsilon\le10^{-4}).
\]
所以除 contact center 与 exact radius phase 外，normalized remainder 安全小于
\[
\boxed{101\varepsilon.}
\tag{24}

结合 (21),(23)：
\[
\boxed{
0<
K-T\delta
-5\cdot10^{N-4g-1}\psi^2
<101T\varepsilon.
}
\tag{25}

---

## 7. the three stable scales are all below one

现在使用 (1)。

### 7.1 denominator-contact phase

若 `N=s>=g+2`，则由 `b2>=10^(k-g+s-1)`：
\[
T\delta
<10^{s-2}\frac{10^g}{10^g10^{k-g+s-1}}
=10^{g-k-1}\le\frac1{10}.
\]

若 `N=g+2>s`，则
\[
T\delta=H\delta=\frac\rho{b_2}
<10^{2g-k-s+1}\le\frac1{10}
\]
由 `k+s>=2g+2`。

所以统一有
\[
\boxed{0<T\delta<1/10.}
\tag{26}

### 7.2 squared-tail phase

由 `N<=4g` 与 `psi<1`：
\[
\boxed{
0<5\cdot10^{N-4g-1}\psi^2<\frac12.
}
\tag{27}

### 7.3 curvature remainder

由 `N<=2k-2`：
\[
101T\varepsilon
=101\cdot10^{N-2-2k}
\le0.0101<0.012.
\tag{28}

---

## 8. integer contradiction

由 (25)--(28)：
\[
0<K<\frac1{10}+\frac12+0.012<1.
\]
但 (22) 给 `K` 为正整数。矛盾。

这证明 (2)。

---

## 9. new `r=1` frontier

本文之后，`r=1,s>=2` 若仍有 candidate，至少必须突破以下三道稳定墙之一：
\[
\boxed{
 k+s<2g+2
\quad\text{or}\quad
\max(g+2,s)>4g
\quad\text{or}\quad
\max(g+2,s)>2k-2.
}
\]
也就是说剩余状态只能进入：

1. denominator-contact 不再小的 near-diagonal corridor；
2. squared-tail amplified region `s>4g`；
3. curvature amplified region `s>2k-2`。

这与 `s=1` 边的 `r~3g` / `r~2k-g` 三尺度分裂完全对应。
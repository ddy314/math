# A1 top layer: uniform inner-wedge phase and generic high-height mismatch

> 日期：2026-08-22。
>
> 依赖：`top-layer-minimal-offdiagonal-J-compression.md`、`top-layer.md` positive-excess identity、global `kappa` square、`decimal-height-synchronization.md`。
>
> 范围：最高层最小双 surplus
> \[
> d=2,\qquad r=s=1,
> \]
> 的整个真正 off-diagonal 内楔。

定义
\[
\boxed{u:=2g-k.}
\]
因 `g<k<2g`：
\[
\boxed{1\le u\le g-1.}
\]
并令
\[
H:=10^g,
\qquad
\tau:=10^{k-g}=10^{g-u}=H/10^u.
\]

状态：**已严格完成统一 reduction。**

---

# Part I. uniform real phase

## 1. `J` range

`top-layer-minimal-offdiagonal-J-compression.md` 给
\[
0\le J< -1+\frac{11}{10}10^u.
\]
所以
\[
\boxed{J+1<1.1\cdot10^u.}
\tag{1}

沿用 exact identity
\[
\boxed{
1+\frac JH=50S-10w\varepsilon p,
}
\tag{2}
其中
\[
\varepsilon=10^{-2k}
=\frac1{H^2\tau^2}
=\frac{10^{2u}}{H^4}.
\tag{3}

因为 `u<=g-1`：
\[
\tau\ge10,
\qquad
\varepsilon\le10^{-6}.
\]

---

## 2. normalized tail ratio remains uniformly small

定义
\[
r:=\frac{\rho}{H\tau}.
\]
由
\[
H/10\le\rho<H
\]
与 `tau=H/10^u`：
\[
\boxed{
\frac{10^{u-1}}H\le r<\frac{10^u}H\le\frac1{10}.
}
\tag{4}

记
\[
\boxed{B_0:=1-H^{-1}+r.}
\]
则统一有
\[
B_0<1.1.
\tag{5}

positive-excess 中仍有
\[
p<0.412,
\qquad q\le0.3,
\]
\[
1-\varepsilon q<\widehat R<1+\varepsilon p,
\]
以及
\[
\frac{\zeta^2}{\varepsilon}<H^{-4}.
\]
因此
\[
0<\zeta<\frac{10^u}{H^4},
\qquad
r\zeta<\frac{10^{2u}}{H^5}\le\frac\varepsilon{100}.
\tag{6}

---

## 3. lower orientation is uniform in `u`

positive-excess contact bracket gives
\[
\frac{\mathfrak h}{M_0\varepsilon}
>
\frac1{100}
\left[
B_0
+\varepsilon\left(p+\frac qH-rq\right)
-r\zeta
\right].
\]

由 (4),(6) 与 `p>0.2085`：
\[
p+q/H-rq-r\zeta/\varepsilon>0.168.
\]
所以
\[
\frac{\mathfrak h}{M_0\varepsilon}
>
\frac1{100}(B_0+0.168\varepsilon).
\]

再用
\[
1+\varepsilon p+\widehat R
>2(1-\varepsilon/20)
\]
与 `B0<1.1`：
\[
50S_{\rm contact}>B_0+0.11\varepsilon.
\]

curvature source贡献大于 `23 epsilon`，而 (2) 中减项小于 `16.5 epsilon`。故
\[
1+J/H>B_0.
\]
即
\[
\boxed{(J+1)\tau>\rho.}
\tag{7}

---

## 4. upper width is `40*10^u/H^2`

同样由 uniform upper estimates：
\[
50S_{\rm contact}<B_0+1.4\varepsilon.
\]

third-radius source满足
\[
50\frac{\zeta^2}{\varepsilon}
<\frac{50}{H^4}
\le0.5\varepsilon
\]
（因 `u>=1`），其余 curvature sources总计小于 `37.3 epsilon`。所以
\[
50S<B_0+39.2\varepsilon.
\]

由 (2) 丢掉严格正的减项：
\[
1+J/H<50S.
\]
因此
\[
\frac{J+1}{H}<r+39.2\varepsilon.
\]
乘 `H tau`：
\[
(J+1)\tau-\rho
<39.2H\tau\varepsilon
=39.2\frac{10^u}{H^2}
<40\frac{10^u}{H^2}.
\]
与 (7) 合并：
\[
\boxed{
0<(J+1)\tau-\rho
<\frac{40\cdot10^u}{H^2}.
}
\tag{8}

---

## 5. uniform integer gap

写
\[
\rho=M/L,
\qquad (L,M)=1,
\]
定义
\[
\boxed{A_J:=((J+1)\tau)L-M.}
\]
则
\[
\boxed{A_J\in\mathbf Z_{>0},}
\]
并且
\[
\boxed{
0<A_JH^2<40\cdot10^u L.
}
\tag{9}

特别地
\[
\boxed{
L>\frac{H^2}{40\cdot10^u}.
}
\tag{10}

`u=1,2` 分别恢复此前的 `400/H^2` 与 `4000/H^2` phase shells。

---

# Part II. generic local high structure

以下额外假设
\[
\boxed{g-u\ge3,}
\tag{11}
即 `tau>=1000`。这保证第一平方项在 2-adic prefix norm 中严格深于 `b1`-side 项，从而 local table稳定。

令
\[
e:=v_2(w).
\]
则
\[
\boxed{v_2(N)=2e,}
\qquad
\boxed{v_2(K)=2g-2u+2e,}
\tag{12}
\]
\[
\boxed{v_5(N)=0,}
\qquad
\boxed{v_5(K)=2g-2u.}
\tag{13}

base depths 为
\[
\boxed{v_2(10^gQG)=3g-2u+e,}
\qquad
\boxed{v_5(10^gQG)=3g-2u.}
\tag{14}

写
\[
L=2^a5^b.
\]

---

## 6. generic 2-high formula

若
\[
\boxed{a>u+1,}
\tag{15}
则 `kappa` square 中第二项严格更浅。直接 valuation 给
\[
v_2(W^2)=8g-5u+1+4e+a.
\]
square parity 因此强迫
\[
\boxed{a\equiv u-1\pmod2.}
\tag{16}

normalized root 的 exact 2-completion height为
\[
\boxed{
H_2
=2g+\frac{3(a-u)+1}{2}.
}
\tag{17}

---

## 7. generic 5-high formula

若
\[
\boxed{b>u,}
\tag{18}
则 5-side 第二项严格更浅：
\[
v_5(W^2)=8g-5u+b.
\]
square parity 强迫
\[
\boxed{b\equiv u\pmod2.}
\tag{19}

exact 5-completion height为
\[
\boxed{
H_5
=2g+\frac{3(b-u)}2.
}
\tag{20}

---

## 8. all generic mixed-high states are empty

若同时
\[
a>u+1,
\qquad
b>u,
\]
exact decimal-height synchronization 要求 (17)=(20)：
\[
3(a-b)+1=0.
\]
无整数解。

所以统一得到
\[
\boxed{
 a>u+1,\ b>u
 \Longrightarrow\text{empty}.
}
\tag{21}

这是整个 inner wedge 的 `u`-independent high-high obstruction。

---

# Part III. pure-side resonance normal forms

## 9. pure-5 necessary resonance

假设
\[
a=0,
\qquad b>u.
\]
由 (20)：
\[
H_5=2g+\frac{3(b-u)}2.
\]

2-side 若想同步，只能落在
\[
\boxed{v_2(\kappa)=g-u+1+e.}
\]
因此
\[
\boxed{v_2(M)=2g-u-1.}
\]
写
\[
\boxed{M=2^{2g-u-1}m,}
\qquad (m,10)=1,
\qquad m\mid b_1Q_0.
\]

令
\[
c_5:=5^{2g-u+b}.
\]
共轭 root 的 2-denominator depths为
\[
\{1,\ 1+v_2(m+c_5Q_0)\}.
\]
所以必要且精确的 high-sign resonance 为
\[
\boxed{
v_2(m+5^{2g-u+b}Q_0)
=2g-1+\frac{3(b-u)}2.
}
\tag{22}

`u=1,2` 分别恢复前两层 pure-5 resonance。

---

## 10. pure-2 necessary resonance

假设
\[
b=0,
\qquad a>u+1.
\]
由 (17)：
\[
H_2=2g+\frac{3(a-u)+1}{2}.
\]

5-side只能落在
\[
\boxed{v_5(\kappa)=g-u,}
\]
所以
\[
\boxed{v_5(M)=2g-u.}
\]
写
\[
\boxed{M=5^{2g-u}m,}
\qquad (m,10)=1,
\qquad m\mid b_1Q_0.
\]

令
\[
c_2:=2^{2g-u-1+a}.
\]
exact 5-adic root allocation给
\[
\boxed{
v_5(m+2^{2g-u-1+a}Q_0)
=2g+\frac{3(a-u)+1}{2}.
}
\tag{23}

---

## 11. new global frontier

因此 remaining `r=s=1` inner wedge 已统一压成：

1. universal ultrathin integer phase (9)；
2. generic mixed-high sector完全为空；
3. pure-5 与 pure-2 各只有一个显式 low-resonance progression；
4. 尚需单独处理的 mixed states至少有一侧位于 small strip
   \[
   a\le u+1
   \quad\text{或}\quad
   b\le u.
   \]

这比逐层 `k=2g-c` 重开 local analysis 更适合作为后续统一入口。

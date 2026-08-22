# A1 top layer: ultrathin tail centers on `k=2g-2`

> 日期：2026-08-22。
>
> 依赖：`top-layer-minimal-offdiagonal-J-compression.md`、`top-layer.md` positive-excess identity、`top-layer-k2gminus1-tail-center.md` 的同一估计模板。
>
> 范围：
> \[
> d=2,\quad r=s=1,\quad g\ge3,\quad k=2g-2.
> \]

`J` compression 给
\[
\boxed{0\le J\le108.}
\]

状态：**已严格完成 reduction。** 第三尾被锁到 `J` 对应的第二层 decimal subcell：
\[
\boxed{
0<(J+1)10^{g-2}-\rho<4000\,10^{-2g}.
}
\]

---

## 1. notation

令
\[
H:=10^g,
\qquad
\tau:=10^{g-2}=H/100,
\qquad
\varepsilon:=10^{-2k}=\frac1{H^2\tau^2}=\frac{10000}{H^4}.
\]
因 `g>=3`：
\[
H\ge1000,
\qquad
\tau\ge10,
\qquad
\varepsilon\le10^{-8}.
\]

沿用
\[
p=\phi_1,
\qquad
q=\phi_2=z/10,
\]
与 exact `J` identity
\[
\boxed{
1+\frac JH=50S-10w\varepsilon p.
}
\tag{1}

positive-excess identity 写成
\[
\begin{aligned}
S={}&
\frac{\mathfrak h}{M_0\varepsilon}
(1+\varepsilon p+\widehat R)
+\frac{\zeta^2}{\varepsilon}\\
&+\varepsilon(2p+q^2-p^2)
+\varepsilon^2p^2,
\end{aligned}
\tag{2}
\]
其中
\[
\frac{\mathfrak h}{M_0\varepsilon}
=
\frac{\lambda}{\varepsilon}
\left[
(1+\varepsilon p)-H^{-1}(1-\varepsilon q)
+\frac{\rho}{H\tau}(\widehat R-\zeta)
\right],
\tag{3}
\]
且
\[
\frac{\lambda}{\varepsilon}
=\frac1{100-(10w-1)\varepsilon}.
\tag{4}

定义
\[
r:=\frac{\rho}{H\tau}.
\]
由 slope window `H/10<=rho<H` 与 `tau=H/100`：
\[
\boxed{\frac{10}{H}\le r<\frac{100}{H}<\frac1{10}.}
\tag{5}

再记
\[
\boxed{B_0:=1-H^{-1}+r.}
\tag{6}
因此 `B0<1.1`。

---

## 2. uniform auxiliary bounds

六类型仍满足
\[
p<0.412,
\qquad
q\le0.3,
\]
以及
\[
1-\varepsilon q<\widehat R<1+\varepsilon p.
\]

已有 third-radius bound
\[
\frac{\zeta^2}{\varepsilon}<H^{-4}
\]
给
\[
0<\zeta<\frac1{H^3\tau}=\frac{100}{H^4}.
\]
由 (5)：
\[
r\zeta<\frac{10000}{H^5}<\frac\varepsilon{1000}.
\tag{7}

curvature 仍有
\[
0.46<2p+q^2-p^2<0.745.
\tag{8}

---

## 3. lower sign: center lies above `rho`

从 (3)-(4) 且 `lambda/epsilon>1/100`：
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

由 `p>0.2085`、`rq<0.03`、(7)：
\[
\frac{\mathfrak h}{M_0\varepsilon}
>
\frac1{100}(B_0+0.177\varepsilon).
\]

又
\[
1+\varepsilon p+\widehat R
>2(1-\varepsilon/20).
\]
因 `B0<1.1`：
\[
\boxed{50S_{\rm contact}>B_0+0.12\varepsilon.}
\tag{9}

由 (8)，curvature source贡献大于 `23 epsilon`；而
\[
10w\varepsilon p<16.5\varepsilon.
\]
其余 sources非负。因此 (1),(9) 给
\[
1+\frac JH>B_0.
\]
代入 (6)：
\[
\frac{J+1}{H}>\frac{\rho}{H\tau}.
\]
故
\[
\boxed{(J+1)\tau>\rho.}
\tag{10}

---

## 4. upper width

由 (3) 与 auxiliary bounds：
\[
\frac{\mathfrak h}{M_0\varepsilon}
<
\frac{B_0+0.46\varepsilon}{100-39\varepsilon}.
\]
又
\[
1+\varepsilon p+\widehat R<2(1+0.412\varepsilon).
\]
因为 `epsilon<=10^-8,B0<1.1`，可安全取
\[
\boxed{50S_{\rm contact}<B_0+1.4\varepsilon.}
\tag{11}

third-radius source满足
\[
50\frac{\zeta^2}{\varepsilon}<\frac{50}{H^4}=0.005\varepsilon,
\]
curvature 加最后 `epsilon^2` source小于
\[
37.3\varepsilon.
\]
故
\[
\boxed{50S<B_0+39\varepsilon.}
\tag{12}

在 (1) 中丢掉严格正的减项：
\[
1+\frac JH<50S.
\]
由 (6),(12)：
\[
\frac{J+1}{H}
<r+39\varepsilon.
\]
乘 `H tau`：
\[
(J+1)\tau-\rho
<39H\tau\varepsilon
=\frac{39}{H\tau}
=\frac{3900}{H^2}
<\frac{4000}{H^2}.
\tag{13}

与 (10) 合并：
\[
\boxed{
0<(J+1)\tau-\rho<\frac{4000}{H^2}.
}
\tag{14}

---

## 5. integer gap

写
\[
\rho=M/L,
\qquad (L,M)=1,
\]
并定义
\[
\boxed{A_J:=((J+1)\tau)L-M.}
\]
则
\[
A_J\in\mathbf Z_{>0}
\]
且
\[
\boxed{0<A_JH^2<4000L.}
\tag{15}

特别地
\[
\boxed{L>H^2/4000.}
\tag{16}

这就是 `k=2g-2` 后续 prime-shape / phase-divisor arguments 的统一 real input。

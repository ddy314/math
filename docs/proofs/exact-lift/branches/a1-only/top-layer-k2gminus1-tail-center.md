# A1 top layer: ultrathin tail centers on `k=2g-1`

> 日期：2026-08-22。
>
> 依赖：`top-layer-minimal-offdiagonal-J-compression.md` 与 `top-layer.md` 的 positive-excess identity。
>
> 范围：
> \[
> d=2,\quad r=s=1,\quad g\ge2,\quad k=2g-1.
> \]
> 由 `J` compression：
> \[
> J\in\{0,1,\ldots,9\}.
> \]

状态：**已严格完成 reduction。** 本文证明第三尾斜率不是在整个 decade 中自由移动，而是被 `J` 锁到相应 decimal subcell：
\[
\boxed{
0<(J+1)10^{g-1}-\rho<400\,10^{-2g}.
}
\]

---

## 1. notation

令
\[
H:=10^g,
\qquad
\tau:=10^{k-g}=\frac H{10},
\qquad
\varepsilon:=10^{-2k}=\frac1{H^2\tau^2}.
\tag{1}
\]
因为 `g>=2`：
\[
H\ge100,
\qquad
\tau\ge10,
\qquad
\varepsilon\le10^{-6}.
\tag{2}
\]

沿用
\[
p=\phi_1,
\qquad
q=\phi_2=\frac z{10},
\]
以及
\[
\boxed{
1+\frac JH=50S-10w\varepsilon p.
}
\tag{3}
\]

positive-excess identity 为
\[
\begin{aligned}
S={}&
\frac{\mathfrak h}{M_0\varepsilon}
(1+\varepsilon p+\widehat R)
+\frac{\zeta^2}{\varepsilon}\\
&+\varepsilon(2p+q^2-p^2)
+\varepsilon^2p^2,
\end{aligned}
\tag{4}
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
\tag{5}
\]
且
\[
\frac{\lambda}{\varepsilon}
=\frac1{100-(10w-1)\varepsilon}.
\tag{6}

记
\[
r:=\frac{\rho}{H\tau}.
\]
由 slope window `H/10<=rho<H` 和 `tau=H/10`：
\[
\boxed{
\frac1H\le r<\frac{10}{H}\le\frac1{10}.
}
\tag{7}

再记主中心
\[
\boxed{B_0:=1-\frac1H+r.}
\tag{8}

---

## 2. auxiliary uniform bounds

六类型 off-diagonal 窄窗给
\[
p<0.412,
\qquad q\le0.3.
\tag{9}
\]
球面半径给
\[
1-\varepsilon q<\widehat R<1+\varepsilon p.
\tag{10}
\]
此前 third-radius bound 为
\[
\frac{\zeta^2}{\varepsilon}<\frac1{H^4}.
\tag{11}
\]
由 `sqrt(epsilon)=1/(H tau)` 和 (11)：
\[
\boxed{
0<\zeta<\frac1{H^3\tau}=\frac{10}{H^4}.
}
\tag{12}

curvature 在六类型窄窗中满足
\[
\boxed{2p+q^2-p^2>0.46}
\tag{13}
\]
以及安全上界
\[
\boxed{2p+q^2-p^2<0.745.}
\tag{14}

---

## 3. lower bound: the tail lies below `(J+1)tau`

由 (5)-(6) 与 `lambda/epsilon>1/100`：
\[
\frac{\mathfrak h}{M_0\varepsilon}
>
\frac1{100}
\left[
B_0
+\varepsilon\left(p+\frac qH-rq\right)
-r\zeta
\right].
\tag{15}

在全部六类型中
\[
p+\frac qH-rq>0.1785.
\]
又由 (7),(12) 与 `epsilon=100/H^4`：
\[
r\zeta<\frac1{H^4}=\frac\varepsilon{100}.
\]
因此
\[
\frac{\mathfrak h}{M_0\varepsilon}
>
\frac1{100}(B_0+0.168\varepsilon).
\tag{16}

由 (10)：
\[
1+\varepsilon p+\widehat R
>2+\varepsilon(p-q)
>2\left(1-\frac\varepsilon{20}\right).
\tag{17}

注意 `B0<1.09`。所以 contact source 从 (16)-(17) 给
\[
50S_{\rm contact}
>
(B_0+0.168\varepsilon)
\left(1-\frac\varepsilon{20}\right)
>B_0+0.11\varepsilon.
\tag{18}

由 (13)，curvature source 进一步贡献
\[
50\varepsilon(2p+q^2-p^2)>23\varepsilon.
\tag{19}
其余 sources 非负。

另一方面
\[
10w\varepsilon p
<40(0.412)\varepsilon
<16.5\varepsilon.
\tag{20}

因此由 (3)：
\[
1+\frac JH
=50S-10w\varepsilon p
>B_0.
\]
代入 (8)：
\[
\frac{J+1}{H}>r=rac{\rho}{H\tau}.
\]
故
\[
\boxed{(J+1)\tau>\rho.}
\tag{21}

---

## 4. upper bound: width is `O(H^-2)`

由 (5),(9)-(10)：
\[
\frac{\mathfrak h}{M_0\varepsilon}
<
\frac{
B_0+0.46\varepsilon
}{100-39\varepsilon}.
\tag{22}

并且
\[
1+\varepsilon p+\widehat R
<2(1+0.412\varepsilon).
\]
因此
\[
50S_{\rm contact}
<
\frac{1+0.412\varepsilon}{1-0.39\varepsilon}
(B_0+0.46\varepsilon).
\]
由 `epsilon<=10^-6`、`B0<1.09`，可安全取
\[
\boxed{
50S_{\rm contact}<B_0+1.4\varepsilon.
}
\tag{23}

第三半径由 (11) 与 `epsilon=100/H^4` 给
\[
50\frac{\zeta^2}{\varepsilon}
<\frac{50}{H^4}
=\frac\varepsilon2.
\tag{24}

由 (14) 与 `p^2<1/4`：
\[
50\varepsilon(2p+q^2-p^2)
+50\varepsilon^2p^2
<37.3\varepsilon.
\tag{25}

所以
\[
\boxed{50S<B_0+39.2\varepsilon.}
\tag{26}

由 (3) 中减去项为正：
\[
1+\frac JH<50S.
\]
结合 (8),(26)：
\[
\frac{J+1}{H}
<r+39.2\varepsilon.
\]
乘 `H tau`：
\[
(J+1)\tau-\rho
<39.2H\tau\varepsilon.
\]
而
\[
H\tau\varepsilon=\frac1{H\tau}=\frac{10}{H^2}.
\]
故
\[
\boxed{
(J+1)\tau-\rho<\frac{392}{H^2}<\frac{400}{H^2}.
}
\tag{27}

与 (21) 合并：
\[
\boxed{
0<(J+1)\tau-\rho<\frac{400}{H^2}.
}
\tag{28}

---

## 5. integer tail gap

恢复
\[
\rho=\frac ML,
\qquad (L,M)=1.
\]
定义
\[
\boxed{
A_J:=((J+1)\tau)L-M.
}
\tag{29}
由 (28)：
\[
A_J\in\mathbf Z_{>0}
\]
并且
\[
\boxed{
0<A_JH^2<400L.
}
\tag{30}

特别地
\[
\boxed{L>\frac{H^2}{400}.}
\tag{31}

所以 `k=2g-1` 已从十个连续 tail intervals 压成十个 ultrathin rational cells。下一步应按 `L=2^a5^b` 的 prime shape 与 prefix 的 `J`-dependent 2/5 valuations 分流；不再需要把第三块作为自由变量。
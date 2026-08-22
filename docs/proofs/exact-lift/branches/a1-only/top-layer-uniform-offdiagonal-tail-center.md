# A1 top layer: uniform off-diagonal ultrathin tail center

> 日期：2026-08-22。
>
> 依赖：`top-layer-minimal-offdiagonal-J-compression.md`、`top-layer.md` 的 positive-excess identity。
>
> 范围：
> \[
> d=2,\qquad r=s=1,\qquad g\ge2,
> \]
> 且
> \[
> g<k\le2g-1.
> \]

状态：**已严格完成 reduction。** 本文把此前在 `k=2g-1,2g-2` 上分别证明的 ultrathin tail center 统一到整个 off-diagonal wedge。

令
\[
H:=10^g,\qquad c:=k-g\ge1,\qquad \tau:=10^c,
\]
\[
u:=2g-k=g-c\ge1,
\qquad
\varepsilon:=10^{-2k}=\frac1{H^2\tau^2}.
\]
由 `J`-compression，写
\[
U_1=(51-10z)H+J,
\qquad J\in\mathbf Z,
\]
并有 exact identity
\[
\boxed{1+\frac JH=50S-10w\varepsilon p.}
\tag{1}
\]
其中 `S` 是 positive-excess 四个正 source 之和，`p=phi_1`。

本文证明
\[
\boxed{
0<(J+1)\tau-\rho<\frac{40}{H\tau}.
}
\tag{2}
\]
等价地，若
\[
A_J:=((J+1)\tau)L-M,
\qquad \rho=M/L,
\]
则
\[
\boxed{
A_J\in\mathbf Z_{>0},
\qquad
0<A_JH\tau<40L.
}
\tag{3}
\]

---

## 1. uniform normalized bounds

仍记
\[
r:=\frac{\rho}{H\tau}.
\]
第三尾 slope 给
\[
\frac H{10}\le\rho<H.
\]
而 `tau>=10`，故
\[
0<r<\frac1\tau\le\frac1{10}.
\tag{4}
\]

因为 `g>=2`、`tau>=10`：
\[
H\ge100,
\qquad
\varepsilon\le10^{-6}.
\tag{5}
\]

六类型 off-diagonal narrow window 仍给
\[
0.2085<p<0.4111,
\qquad q:=\phi_2\le0.3,
\qquad w\le4.
\tag{6}
\]

positive-excess identity 中
\[
\frac{\lambda}{\varepsilon}
=\frac1{100-(10w-1)\varepsilon},
\tag{7}
\]
且
\[
\frac{\mathfrak h}{M_0\varepsilon}
=
\frac{\lambda}{\varepsilon}
\left[
(1+\varepsilon p)-H^{-1}(1-\varepsilon q)
+r(\widehat R-\zeta)
\right].
\tag{8}
\]

球面半径给
\[
1-\varepsilon q<\widehat R<1+\varepsilon p,
\tag{9}
\]
以及既有 third-radius bound
\[
\frac{\zeta^2}{\varepsilon}<\frac1{H^4}.
\tag{10}
\]
于是
\[
0<\zeta<\frac1{H^3\tau}.
\tag{11}
\]
结合 (4)：
\[
r\zeta<\frac1{H^3\tau^2}
=\frac\varepsilon H
\le\frac\varepsilon{100}.
\tag{12}
\]

定义主中心
\[
B_0:=1-\frac1H+r.
\tag{13}
\]
由 (4)、`H>=100`：
\[
B_0<1.09.
\tag{14}
\]

---

## 2. lower bound: `(J+1)tau>rho`

由 (6)：
\[
p+\frac qH-rq>0.1785.
\]
结合 (7),(8),(12)：
\[
\frac{\mathfrak h}{M_0\varepsilon}
>
\frac1{100}(B_0+0.168\varepsilon).
\tag{15}
\]

又由 (9)：
\[
1+\varepsilon p+\widehat R
>2+\varepsilon(p-q)
>2\left(1-\frac\varepsilon{20}\right).
\tag{16}
\]
由 (14)--(16)，contact source 给
\[
50S_{\rm contact}>B_0+0.11\varepsilon.
\tag{17}
\]

curvature source 在六类型 narrow window 中满足
\[
2p+q^2-p^2>0.46,
\]
故额外贡献
\[
50\varepsilon(2p+q^2-p^2)>23\varepsilon.
\tag{18}

另一方面
\[
10w\varepsilon p<16.5\varepsilon.
\tag{19}
\]
其余 source 非负。把 (17)--(19) 代入 (1)：
\[
1+\frac JH>B_0.
\]
由 (13)：
\[
\frac{J+1}{H}>r=\frac\rho{H\tau}.
\]
因此
\[
\boxed{(J+1)\tau>\rho.}
\tag{20}
\]

---

## 3. upper bound: width `<40/(H tau)`

由 (6)--(9) 与 `epsilon<=10^-6`，与 `k=2g-1` proof 相同的 endpoint audit 给
\[
\boxed{50S_{\rm contact}<B_0+1.4\varepsilon.}
\tag{21}
\]

因为 `k<=2g-1`，即 `tau<=H/10`，由 (10)：
\[
\frac{50}{H^4}\le\frac\varepsilon2.
\tag{22}
\]
又
\[
2p+q^2-p^2<0.745,
\qquad p^2<\frac14,
\]
所以 curvature 与 `epsilon^2 p^2` 合计小于
\[
37.3\varepsilon.
\tag{23}
\]
由 (21)--(23)：
\[
\boxed{50S<B_0+39.2\varepsilon.}
\tag{24}

由 (1) 中减去项严格为正：
\[
1+\frac JH<50S.
\]
结合 (13),(24)：
\[
\frac{J+1}{H}<r+39.2\varepsilon.
\]
乘 `H tau`：
\[
(J+1)\tau-\rho
<39.2H\tau\varepsilon
=\frac{39.2}{H\tau}
<\frac{40}{H\tau}.
\tag{25}
\]
与 (20) 合并即得 (2)。

---

## 4. leading decimal block is exact

令
\[
s:=J+1.
\]
由 (20) 与 `rho>=H/10`：
\[
s>\frac{H}{10\tau}=10^{u-1}.
\tag{26}
\]

另一方面若 `s>=10^u+1=H/tau+1`，则
\[
s\tau-\rho>H+\tau-H=\tau\ge10,
\]
与 (2) 的右端 `<1` 矛盾。因此
\[
\boxed{10^{u-1}<J+1\le10^u.}
\tag{27}
\]

所以 `J+1` 恰为一个 `u=2g-k` 位十进制整数，并由 `rho` 唯一确定：
\[
\boxed{
J+1=\left\lceil\frac\rho\tau\right\rceil.
}
\tag{28}
\]

这条唯一性是最终 `k-g=1,2` corridor certificate 的主要压缩入口。
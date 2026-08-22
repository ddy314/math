# A1 top layer: residual off-diagonal `J` compression

> 日期：2026-08-22。
>
> 依赖：`top-layer-minimal-offdiagonal-far-collapse.md` 与 `top-layer.md` 的 positive-excess identity。
>
> 范围：
> \[
> d=2,\quad r=s=1,\quad g\ge1,\quad k>g.
> \]

状态：**已严格完成 reduction。** far region `k>=2g+1` 已空后，本文把剩余窄楔
\[
 g<k\le2g
\]
中的 first-residue 整数自由度压到 `10^{2g-k}` 尺度。

---

## 1. 记号与既有下界

令
\[
H=10^g,
\qquad
\tau=10^{k-g},
\qquad
\varepsilon=10^{-2k}=\frac1{H^2\tau^2}.
\]

沿用
\[
p=\phi_1,
\qquad
q=\phi_2=\frac z{10},
\]
以及整数坐标
\[
\boxed{U_1=(51-10z)H+J.}
\tag{1}
\]

`top-layer-minimal-offdiagonal-far-collapse.md` 的 §4 不使用 `k>=2g+1`，只使用 off-diagonal 六类型窄窗，因此对所有 `k>g` 都有
\[
\boxed{J>-1.}
\]

因为 `J` 是整数：
\[
\boxed{J\ge0.}
\tag{2}
\]

另外仍有 exact identity
\[
\boxed{
\frac JH+1=50S-10w\varepsilon p,
}
\tag{3}
\]
其中
\[
S=2(p+q)-1
\]
是 positive-excess 四个正 source 的和。

---

## 2. 剩余窄楔中的尺度关系

far region 已关闭，所以只需研究
\[
\boxed{g<k\le2g.}
\tag{4}
\]

因此
\[
\boxed{10\le\tau\le H.}
\tag{5}
\]

六类型统一有
\[
p<0.412,
\qquad q\le0.3,
\qquad w\le4.
\tag{6}
\]

在 `r=s=1` 中
\[
\frac{\lambda}{\varepsilon}
=\frac1{100-(10w-1)\varepsilon}
\le\frac1{100-39\varepsilon}.
\tag{7}
\]

又
\[
\frac{\theta}{\varepsilon}
=\frac{\lambda}{\varepsilon}\frac{\rho}{10^k}.
\]
因为 `rho<H` 且 `10^k=H tau`：
\[
\boxed{
\frac{\theta}{\varepsilon}
<\frac1\tau\frac{\lambda}{\varepsilon}.
}
\tag{8}
\]

---

## 3. contact source 的 sharpened 上界

positive-excess notation 中
\[
\frac{\mathfrak h}{M\varepsilon}
=
\frac{\lambda}{\varepsilon}
\left[(1+\varepsilon p)-H^{-1}(1-\varepsilon q)\right]
+
\frac{\theta}{\varepsilon}(\widehat R-\zeta).
\]

使用
\[
\widehat R-\zeta<\widehat R<1+\varepsilon p,
\]
(6)-(8) 得
\[
\frac{\mathfrak h}{M\varepsilon}
<
\frac{
1-H^{-1}+\tau^{-1}+0.484\varepsilon
}{100-39\varepsilon}.
\tag{9}
\]

并且
\[
1+\varepsilon p+\widehat R
<2(1+0.412\varepsilon).
\]
于是 contact source 满足
\[
50S_{\rm contact}
<
\frac{1+0.412\varepsilon}{1-0.39\varepsilon}
\left(
1-\frac1H+\frac1\tau+0.484\varepsilon
\right).
\tag{10}
\]

由 (5)
\[
\varepsilon=\frac1{H^2\tau^2}
\le\frac1{100\tau^2}
\le10^{-4}.
\]
因此
\[
\frac{1+0.412\varepsilon}{1-0.39\varepsilon}
<1+0.803\varepsilon.
\]
且 (10) 直接给安全界
\[
\boxed{
50S_{\rm contact}
<
1-\frac1H+\frac1\tau+1.4\varepsilon.
}
\tag{11}
\]

---

## 4. 其余 source 只占不到 `0.09/tau`

与前文相同，第三半径满足
\[
\frac{\zeta^2}{\varepsilon}<\frac1{H^4}.
\]
由 `tau<=H`、`H>=10`：
\[
\boxed{
\frac{50}{H^4}\le\frac{0.05}{\tau}.
}
\tag{12}
\]

对 curvature，`p<0.412,q<=0.3` 给
\[
2p+q^2-p^2<0.745.
\]
所以
\[
50\varepsilon(2p+q^2-p^2)
<37.25\varepsilon.
\]
再加 `50 epsilon^2 p^2`，可安全取
\[
<37.3\varepsilon.
\]
由 `epsilon<=1/(100 tau^2)`、`tau>=10`：
\[
\boxed{
37.3\varepsilon<\frac{0.0373}{\tau}.
}
\tag{13}
\]

(11) 中额外的 `1.4 epsilon` 也满足
\[
1.4\varepsilon<\frac{0.0014}{\tau}.
\]

因此四个 source 合计严格满足
\[
\boxed{
50S
<
1-\frac1H+\frac{1.09}{\tau}
<
1-\frac1H+\frac{11}{10\tau}.
}
\tag{14}
\]

---

## 5. `J` 的新绝对高度

由 (3) 且 `10w epsilon p>0`：
\[
\frac JH+1<50S.
\]
结合 (14)：
\[
\frac JH
<
-\frac1H+\frac{11}{10\tau}.
\]
乘 `H`：
\[
\boxed{
J<
-1+\frac{11}{10}\frac H\tau
=
-1+\frac{11}{10}10^{2g-k}.
}
\tag{15}
\]

与 (2) 联立：
\[
\boxed{
0\le J<
-1+\frac{11}{10}10^{2g-k}.
}
\tag{16}
\]

令
\[
\boxed{u:=2g-k.}
\]
在剩余窄楔中
\[
0\le u\le g-1.
\]
所以 `J` 只在 `10^u` 尺度上移动，而原始第一余量尺度为 `10^g`。

两个最外层尤其简单：

### `u=0`, 即 `k=2g`

(16) 给
\[
0\le J<\frac1{10},
\]
故
\[
\boxed{J=0.}
\tag{17}
\]

### `u=1`, 即 `k=2g-1`

(16) 给
\[
0\le J<10,
\]
故
\[
\boxed{J\in\{0,1,\ldots,9\}.}
\tag{18}
\]

更一般地，对 `u>=1`：
\[
J<11\cdot10^{u-1}-1,
\]
所以整数 `J` 至多具有 `u+1` 位且其 leading range 被固定压缩。

---

## 6. 当前 `r=s=1` 前沿

minimal diagonal `k=g` 已关闭，far off-diagonal `k>=2g+1` 已关闭。因此
\[
\boxed{
 d=2,\ r=s=1,\ g\ge1
}
\]
的全部 remaining candidates 必须满足
\[
\boxed{
g<k\le2g}
\]
和 (16)。

尤其首个应攻击的边界已完全固定为
\[
\boxed{k=2g,\qquad J=0.}
\]
下一步应把 primitive residue conditions 与 global terminal bridge 直接代入该单值边界。
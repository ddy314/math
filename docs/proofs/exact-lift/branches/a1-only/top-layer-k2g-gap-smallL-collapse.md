# A1 top layer: `k=2g` ultrathin tail gap and small-`L` collapse

> 日期：2026-08-22。
>
> 依赖：`top-layer-minimal-offdiagonal-J-compression.md`、`top-layer.md` positive-excess identity、`decimal-height-synchronization.md`。
>
> 范围：
> \[
> d=2,\quad r=s=1,\quad g\ge1,\quad k=2g.
> \]

状态：**已严格完成 reduction。** `J` compression 已给 `J=0`；本文进一步：

1. primitive reducedness 把六类型压到 `(z,w)=(1,1),(1,3)`；
2. 强迫
   \[
   0<10^g-\rho<95\,10^{-2g};
   \]
3. 因此
   \[
   L>10^{2g}/95;
   \]
4. 特别地 `L=1,2` 均为空。

---

## 1. `J=0` 后的 prefix

令
\[
H=10^g,
\qquad k=2g.
\]

`top-layer-minimal-offdiagonal-J-compression.md` 给
\[
\boxed{J=0.}
\tag{1}
\]

于是
\[
U_1=(51-10z)H.
\]
并且
\[
b_1=10^{4g+1}-w,
\qquad
b_2=H,
\qquad
 a_2=10^{4g+1}-z,
\]
\[
 a_1=10^{g+1}b_1+(51-10z)H.
\tag{2}
\]

primitive reducedness 等价于
\[
\gcd(U_1,b_1)=1.
\tag{3}
\]

---

## 2. primitive pruning：六类型只剩两型

若 `w=2,4`，则 `b_1` 为偶数，而 `H|U_1`，故 (3) 失败。

若 `(z,w)=(3,1)`，则 `51-10z=21`，而
\[
3\mid10^{4g+1}-1=b_1,
\]
故 (3) 同样失败。

`(3,2)` 已被 `w=2` 包含。

所以只剩
\[
\boxed{(z,w)=(1,1),(1,3).}
\tag{4}
\]

此时
\[
U_1=41H.
\]

对 `(1,1)` 还有一个附加周期条件：`41` 在模 41 下的 `10` 阶为 5，故
\[
41\mid10^{4g+1}-1
\Longleftrightarrow
4g+1\equiv0\pmod5
\Longleftrightarrow
g\equiv1\pmod5.
\]
因此 `(1,1)` 还必须满足
\[
\boxed{g\not\equiv1\pmod5.}
\tag{5}
\]

---

## 3. prefix 的统一 2/5 赋值

对 (4) 两型，`w` 为奇数，故 `b_1` 是 2/5-unit。写
\[
Q_0:=10b_1+1.
\]
则
\[
Q=HQ_0,
\qquad
G=Hb_1,
\qquad
D=H^2Q_0.
\tag{6}
\]

又由 (2)，`a_1` 恰含一个 `H` 因子，而 `a_2,b_1,Q_0` 都是 2/5-unit。因此
\[
\boxed{v_2(N)=v_5(N)=0.}
\tag{7}
\]

同时 `C` 为 2/5-unit，故
\[
K=G^2C^2-D^2N
=H^2\left(b_1^2C^2-H^2Q_0^2N\right),
\]
括号仍为 2/5-unit。于是
\[
\boxed{v_2(K)=v_5(K)=2g.}
\tag{8}
\]

---

## 4. exact excess 强迫 `rho` 极贴近 `H`

沿用
\[
\varepsilon=10^{-2k}=H^{-4},
\qquad
p=\phi_1,
\qquad
q=\phi_2=\frac1{10}.
\]

因为 `J=0`，`J` identity
\[
J/H+1=50S-10w\varepsilon p
\]
化成
\[
\boxed{
50S=1+10w\varepsilon p>1.
}
\tag{9}
\]

另一方面在当前两型中 `p<0.412,w<=3`。`r=s=1` 给
\[
\frac{\lambda}{\varepsilon}
=\frac1{100-(10w-1)\varepsilon}
\le\frac1{100-29\varepsilon}.
\tag{10}
\]

令 normalized tail denominator
\[
\rho=\frac ML,
\qquad
H/10\le\rho<H.
\]
则
\[
\frac{\theta}{\varepsilon}
=
\frac{\lambda}{\varepsilon}\frac{\rho}{H^2}.
\tag{11}
\]

positive-excess contact bracket 满足
\[
(1+\varepsilon p)-H^{-1}(1-\varepsilon q)
+
\frac{\rho}{H^2}(\widehat R-\zeta)
<
1-\frac{H-\rho}{H^2}+0.464\varepsilon,
\tag{12}
\]
其中使用
\[
\widehat R-\zeta<\widehat R<1+\varepsilon p.
\]

并且 multiplier
\[
1+\varepsilon p+\widehat R
<2(1+0.412\varepsilon).
\]
由 (10)-(12)，对 contact source 可取安全界
\[
\boxed{
50S_{\rm contact}
<
1-\frac{H-\rho}{H^2}+1.2\varepsilon.
}
\tag{13}
\]

其余 source 方面：

- 由第三块位数粗窗，
  \[
  \zeta^2/\varepsilon< H^{-4}=\varepsilon;
  \]
- curvature 满足
  \[
  2p+q^2-p^2<0.84;
  \]
- `p^2<0.17`。

因此三者乘 50 后总和小于
\[
93\varepsilon.
\]
与 (13) 合并：
\[
\boxed{
50S
<
1-\frac{H-\rho}{H^2}+95H^{-4}.
}
\tag{14}
\]

由 (9)：
\[
1<50S.
\]
所以
\[
\frac{H-\rho}{H^2}<95H^{-4},
\]
即
\[
\boxed{
0<H-\rho<\frac{95}{H^2}.
}
\tag{15}
\]

---

## 5. denominator lower bound

由 global normalization
\[
\rho=\frac ML,
\qquad (L,M)=1,
\qquad L\in\{2^a5^b:a,b\ge0\}.
\]

因为 `rho<H`：
\[
A:=HL-M\in\mathbf Z_{>0}.
\]
且
\[
H-\rho=\frac AL.
\]
由 (15)：
\[
\frac1L\le\frac AL<\frac{95}{H^2}.
\]
因此
\[
\boxed{
L>\frac{H^2}{95}.
}
\tag{16}
\]

这已经说明 surviving tail denominator 必须非常大。

---

## 6. `L=1` 立即为空

若 `L=1`，则
\[
\rho=M\in\mathbf Z.
\]
而 (15) 与 `H>=10` 给
\[
H-1<\rho<H,
\]
不存在整数 `rho`。所以
\[
\boxed{L=1\Longrightarrow\text{empty}.}
\tag{17}
\]

（这也可直接视为 (16) 的特例。）

---

## 7. `L=2` 的 decimal-height mismatch

现在假设
\[
L=2.
\]

记
\[
e_p=v_p(\kappa).
\]
因为
\[
v_p(10^gQG)=3g
\]
对 `p=2,5` 同时成立，`L=2` 精确给
\[
\boxed{e_2=3g+1,\qquad e_5\le3g.}
\tag{18}
\]

### 7.1 2-adic side

由 (7)-(8)：
\[
v_2(\kappa K)=5g+1,
\]
\[
v_2(2GD^2N)=5g+1.
\]

除去 `2^{5g+1}` 后，两项都是 odd units，所以 inner difference 至少再多一个 2。又
\[
W^2=\kappa(\kappa K-2GD^2N)
\]
必须为平方，而
\[
v_2(\kappa)=3g+1,
\]
故额外 cancellation depth 必为偶数；因此至少为 2。于是
\[
\boxed{v_2(W)\ge4g+2.}
\tag{19}
\]

root numerator
\[
X_\sigma=\kappa G^2C+\sigma(\kappa+G)W
\]
中第一项 valuation 恰为
\[
5g+1,
\]
第二项至少为
\[
g+(4g+2)=5g+2.
\]
所以两个 signs 都有
\[
\boxed{v_2(X_\sigma)=5g+1.}
\tag{20}
\]

另一方面
\[
v_2(\kappa+2G)=g+1,
\]
故 raw denominator
\[
Y=\kappa^2(\kappa+2G)
\]
满足
\[
v_2(Y)=7g+3.
\]
于是
\[
\boxed{d_2=2g+2,\qquad H_2=2g+2.}
\tag{21}
\]

### 7.2 5-adic side

`L=2` 与 `(L,M)=1` 给 `M` odd，且 slope window 给
\[
M<2H.
\tag{22}
\]

若 `e_5<=g`，则
\[
v_5(M)=3g-e_5\ge2g,
\]
所以
\[
M\ge5^{2g}.
\]
但
\[
5^{2g}>2\cdot10^g=2H
\qquad(g\ge1),
\]
与 (22) 矛盾。因此
\[
\boxed{g<e_5\le3g.}
\tag{23}
\]

若 `e_5<3g`，square inner 中
\[
v_5(\kappa K)=e_5+2g<5g=v_5(2GD^2N),
\]
所以
\[
v_5(W)=e_5+g.
\]
又 `e_5>g`，故
\[
v_5(\kappa+G)=v_5(\kappa+2G)=g.
\]
root numerator 两项都至少从 `e_5+2g` 开始，因此
\[
v_5(X_\sigma)\ge e_5+2g.
\]
而
\[
v_5(Y)=2e_5+g,
\]
故
\[
d_5\le e_5-g<2g.
\]

若 `e_5=3g`，即使 inner resonance 增加 `W` depth，也仍有
\[
v_5(X_\sigma)\ge5g,
\qquad
v_5(Y)=7g,
\]
所以
\[
d_5\le2g.
\]

综上
\[
\boxed{H_5\le2g.}
\tag{24}
\]

(21)、(24) 与 exact decimal-height synchronization
\[
H_2=H_5
\]
矛盾。因此
\[
\boxed{L=2\Longrightarrow\text{empty}.}
\tag{25}
\]

---

## 8. 当前 `k=2g` terminal

当前若 `k=2g,J=0` 仍有 candidate，则必须满足
\[
\boxed{(z,w)=(1,1)\text{ or }(1,3),}
\]
以及
\[
\boxed{
L>\frac{10^{2g}}{95}>1.
}
\]
并且 `L=2` 已独立排除。

因此最外 off-diagonal 边界已经变成一个大 `2/5`-smooth denominator problem。下一步应按
\[
L=2^a5^b
\]
的 prime shape 分流，并把 (15) 的超薄 rational gap 与 `kappa`-square 的 high/resonance allocation 联立。
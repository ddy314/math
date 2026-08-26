# A1 minimal diagonal: exact contact/remainder coupling in the normalized `R` shell

> 日期：2026-08-27。依赖 `deep-first-complement-remainder.md`、`deep-double-2high-master.md`、`deep-2high-normalized-complement-shell.md` 与 `deep-contact-sign-window.md`。当前 frontier `k>=32`。
>
> 本文适用于全部 surviving double-deep 2-high / 5-low master；finite slot-count application 只用于 moderate HL (`eta<=0`, `xi=r`).

normalized shell 已给

\[
y:=\frac{R}{5^d},
\qquad
\boxed{y^2=1+\frac{\mu\xi}{25}}.
\tag{1}
\]

旧 first complement remainder 独立给出

\[
J_1=\frac{M\gamma+C_0}{T},
\qquad
\frac{J_1}{T}=\mu\Gamma+\frac{C_0}{T^2},
\tag{2}
\]

其中

\[
C_0=w(10w-1).
\]

本文证明这两个对象之间还有一个**精确线性恒等式**：

\[
\boxed{
\frac{J_1}{T}=5\left(y+20w-1\right).
}
\tag{3}
\]

于是 `mu` 可以完全消去，得到

\[
\boxed{
\Gamma
=\frac{\xi}{5}\,
\frac{y+20w-1-\dfrac{C_0}{5T^2}}
{y^2-1}.}
\tag{4}
\]

这把 contact-sign window 直接变成 fixed-`xi` 的 `R/5^d` window。对 moderate HL，每个 fixed `r` 的 leading slots 因而比旧的 typewise universal slot interval 小很多。

状态：**严格完成；附 exact-integer certificate。该结果重组已有 four-factor/remainder 信息，不作为独立 obstruction 重复计数。**

---

## 1. 从 stripped supply 恢复 `MDN_0`

沿用 master

\[
2\beta u-\alpha v=5^d,
\tag{5}
\]

\[
\beta q-5\alpha s=2^cn_0,
\tag{6}
\]

以及

\[
su=b_1,
\qquad
qv=Q,
\qquad
M=uv,
\qquad
Q=10b_1+1.
\]

把 (6) 乘以 `M=uv`：

\[
2^cn_0M
=\beta uQ-5\alpha vb_1.
\]

使用 `Q=10b_1+1` 与 (5)：

\[
\begin{aligned}
\beta uQ-5\alpha vb_1
&=\beta u+5b_1(2\beta u-\alpha v)\\
&=\beta u+5^{d+1}b_1.
\end{aligned}
\]

所以

\[
\boxed{
2^cn_0M=\beta u+5^{d+1}b_1.}
\tag{7}
\]

master 参数为

\[
D=2^{2k+3+\eta}5^B,
\qquad
N_0=2^{\nu_2}5^{\nu_5}n_0,
\]

\[
c=k+1+\eta+\nu_2,
\qquad
Y=B+\nu_5,
\qquad
d=k+1-Y.
\]

因此

\[
\frac{DN_0}{2^cn_0}
=2^{k+2}5^Y.
\]

乘 (7)：

\[
\boxed{
MDN_0
=2^{k+2}5^Y
\left(\beta u+5^{d+1}b_1\right).}
\tag{8}

---

## 2. 引入 normalized complement coordinate

`R` 定义为

\[
R=2\beta u+\alpha v,
\]

所以由 (5)

\[
\beta u=\frac{R+5^d}{4}.
\]

代入 (8)：

\[
MDN_0
=2^k5^Y
\left(R+(1+20b_1)5^d\right).
\tag{9}
\]

又

\[
b_1=10T^2-w,
\qquad
Y+d=k+1.
\]

因此

\[
2^k5^Y\cdot5^d=5T,
\]

并且

\[
5T(1+20b_1)
=1000T^3-(100w-5)T.
\]

于是得到精确 identity

\[
\boxed{
MDN_0
=1000T^3
+2^k5^YR
-(100w-5)T.}
\tag{10}

---

## 3. first remainder 在 `R` 坐标中完全线性

旧定义

\[
MDN_0=1000T^3+R_1
\]

立即与 (10) 比较：

\[
\boxed{
R_1=2^k5^YR-(100w-5)T.}
\tag{11}

除以 `T`，并用

\[
\frac{2^k5^Y}{T}=5^{Y-k}=5^{1-d},
\]

得到

\[
\boxed{
\frac{R_1}{T}
=5\frac{R}{5^d}-(100w-5)
=5y-(100w-5).}
\tag{12}

first-remainder 文档又定义

\[
R_1=c_2T+J_1,
\qquad
c_2=10(1-20w).
\]

所以

\[
\begin{aligned}
\frac{J_1}{T}
&=5y-(100w-5)-10(1-20w)\\
&=5(y+20w-1),
\end{aligned}
\]

即主恒等式 (3)。

---

## 4. 消去 `mu`

由 first remainder：

\[
\frac{J_1}{T}
=\mu\Gamma+\frac{C_0}{T^2}.
\]

结合 (3)：

\[
\boxed{
5(y+20w-1)
=\mu\Gamma+\frac{C_0}{T^2}.}
\tag{13}

另一方面 normalized shell (1) 给

\[
\mu=\frac{25(y^2-1)}{\xi}.
\]

代入 (13)：

\[
5(y+20w-1)
=\frac{25\Gamma(y^2-1)}{\xi}
+\frac{C_0}{T^2}.
\]

整理即得 (4)：

\[
\boxed{
\Gamma
=\frac{\xi}{5}\,
\frac{y+20w-1-\dfrac{C_0}{5T^2}}
{y^2-1}.}
\tag{14}

这条式子中 `mu,M,D,eta` 已全部消失。

---

## 5. correction term 在当前 frontier 可统一忽略到 `10^-63`

定义不含有限 `T` correction 的函数

\[
\boxed{
F_{\xi,w}(y)
:=\frac{\xi(y+20w-1)}{5(y^2-1)}.}
\tag{15}

由 (14)：

\[
F_{\xi,w}(y)-\Gamma
=\frac{\xi C_0}{25T^2(y^2-1)}.
\tag{16}

当前统一已有

\[
\xi<15,214,000,
\qquad
C_0\le156,
\qquad
T\ge10^{32},
\qquad
y>3780.
\]

因此

\[
0<F_{\xi,w}(y)-\Gamma
<6.65\times10^{-64}
<10^{-63}.
\tag{17}

后续 finite certificate 为避免任何浮点边界问题，统一使用更宽得多的 safe margin

\[
\boxed{10^{-4}.}
\]

所以若某类型 contact window 为

\[
\Gamma_L<\Gamma<\Gamma_U,
\]

则严格有

\[
\boxed{
\Gamma_L<F_{\xi,w}(y)<\Gamma_U+10^{-4}.}
\tag{18}

---

## 6. monotone inversion

在当前 `y>3780` 上，令

\[
a=20w-1>0.
\]

则

\[
\frac{d}{dy}\frac{y+a}{y^2-1}
=
\frac{-y^2-2ay-1}{(y^2-1)^2}<0.
\]

所以 `F_{xi,w}` 严格递减。

对任意 `G>0`，方程

\[
F_{\xi,w}(y)=G
\]

的正根为

\[
\boxed{
\mathcal Y(\xi,w;G)
=
\frac{
\xi+\sqrt{\xi^2+20G(5G+\xi(20w-1))}
}{10G}.}
\tag{19}

由 (18)：

\[
\boxed{
\mathcal Y(\xi,w;\Gamma_U+10^{-4})
<y<
\mathcal Y(\xi,w;\Gamma_L).}
\tag{20}

moderate HL 中 `xi=r`，所以这是一个**逐 `r`** 的 leading-slot interval。

---

## 7. 不用平方根的 exact integer slot certificate

令

\[
m=\lfloor y\rfloor.
\]

所有 contact endpoints 都以四位小数保存。写

\[
\Gamma_L=L/10000,
\qquad
\Gamma_U+10^{-4}=U_*/10000.
\]

因为 `F` 递减，candidate slot 必满足

\[
F_{r,w}(m+1)<U_*/10000,
\]

\[
F_{r,w}(m)>L/10000.
\]

这两式分别等价于纯整数比较

\[
\boxed{
10000r(m+20w)
<5U_*\left((m+1)^2-1\right),}
\tag{21}

\[
\boxed{
10000r(m+20w-1)
>5L(m^2-1).}
\tag{22}

所以 `m_min(r),m_max(r)` 可通过 exact integer binary search 得到，不需要浮点、根号或任意精度库。

附带 checker：

`scripts/exact-lift/a1-only/research-checks/deep-denominator/check_a1_deep_hl_contact_shell_slots.cpp`。

---

## 8. corrected local signatures 上的实际压缩

使用 2026-08-27 修正后的 local-compatible moderate counts

\[
\boxed{2,603,440}
\]

并把 (21)-(22) 与旧 normalized shell 的 typewise slot intervals 取交，exact checker 得：

\[
\boxed{
\begin{array}{c|r|r|r}
(z,w)&r\text{ count}&\text{new }(r,m)\text{ pairs}&\text{average slots/r}\\ \hline
(1,1)&579692&1,881,136,022&3245.06\\
(1,2)&255519&821,624,445&3215.51\\
(1,3)&328609&1,060,138,361&3226.14\\
(1,4)&134570&429,109,928&3188.75\\
(3,1)&863426&15,361,714,596&17791.6\\
(3,2)&441624&7,802,825,159&17668.5
\end{array}}
\tag{23}

总计

\[
\boxed{27,356,548,511}
\]

个 safe `(r,m)` pairs。

若只把每个 surviving `r` 配上旧 typewise universal slot interval，则对应数量为

\[
\boxed{162,338,926,240}.
\]

所以 contact/remainder coupling 一步把 moderate `(r,m)` 上集压到

\[
\boxed{16.8515\%}
\]

左右，即删除约

\[
\boxed{83.15\%}
\]

的旧 leading-slot pairs。

四个 `z=1` 类型尤其明显，分别只剩旧 `(r,m)` pairs 的约

\[
5.43\%,\ 6.12\%,\ 7.11\%,\ 8.36\%.
\]

---

## 9. 下一接口

moderate one-exponent certificate 现在不再需要从

\[
(w,Y,\alpha,\beta,m)
\]

中的整个 typewise `m` 区间起步。对每个 finite `r` 可以先做

\[
\boxed{
m_{\min}(r)\le m\le m_{\max}(r),}
\]

再叠加：

1. `(alpha,beta)` 的 fixed CRT ray；
2. coefficient-sensitive source minima / `w=2` joint source matching；
3. `d` 的 periodic prime-source exclusions；
4. `u|b_1(d), v|Q(d)` 的最终 divisor test。

特别地，`z=1` 四型的平均 leading slots 已降到约 3200，而旧区间宽度是 3.8 万到 6 万。

---

## 10. dependency audit

(3)-(14) 没有引入新的独立平方或 Hensel condition。它只是把：

- four-factor stripped supply/complement；
- first complement remainder；
- normalized complement shell；

写到同一个 `y=R/5^d` 坐标中并消去重复变量 `mu`。

因此该 coupling 可安全作为后续 certificate 的**坐标压缩**，但不能和上述三项再当作三个统计独立 obstruction 重复计数。
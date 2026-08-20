# A2 descendant recycling 的 finite quartic tail hierarchy

> **依赖：** `spontaneous-crt-descendant-second-order-tail.md`、`spontaneous-crt-descendant-second-order-gcd-ladder.md`、`spontaneous-crt-descendant-transport-resonance.md`。
>
> **严格状态：**exact transported/Euclidean remainder对 parent errors `(F,L)` 的总次数最高只有4。本文把 cubic 与 quartic homogeneous blocks canonical 清分母，并递归定义 third tail `C_63^(3)` 与 terminal fourth tail `C_63^(4)`。每一层都用上一层 ordinary gcd saturation作为全局整数 divisor；由此得到完整四层 local valuation resolution：若某一 tail没有吞下完整 common baseline，则 actual remainder depth在该层立刻精确停止；连续三层都 full-saturated 后，terminal fourth tail读取**全部剩余 p-adic depth**，因为再无第五阶项。本文还证明 cubic/terminal parent numerators在真实 endpoint均严格为负；第三阶 positive primitive parent carrier为 `3 mod4`，额外携带 odd-inert parity，而 terminal positive primitive为 `5 mod8`。本文仍未排除 terminal modular roots，因此不关闭 A2。

---

## 1. exact degree of the transported remainder

沿用 parent errors

\[
F=K^2s_LY,
\qquad
L=s_L(X+Y),
\]
其中

\[
X=5^\lambda\mathscr R_{63}^\star,
\qquad
Y=g2^m\widehat{\mathscr D}_{63}.
\]

对 exact transported polynomial与 exact Euclidean quotient直接展开。checker验证 remainder只含 monomials

\[
F,\ L,\ F^2,\ FL,\ L^2,\ F^3,\ F^2L,\ L^3,\ F^4,\ L^4.
\]

所以

\[
\boxed{
M=M^{(1)}+M^{(2)}+M^{(3)}+M^{(4)},}
\tag{1.1}
\]

并且

\[
\boxed{M^{(n)}\text{ 对 }(X,Y)\text{ 齐次次数 }n.}
\tag{1.2}
\]

不存在 `M^(>=5)`。

---

## 2. primitive cubic and quartic forms

将 `s_L^n` 抽出后，exact coefficient audit给

\[
\boxed{
M^{(3)}
=s_L^3
\frac{8192\,\mathcal H_3(X,Y;K,\zeta)}
{5^5 11^5K^2},}
\tag{2.1}
\]

其中

\[
\boxed{
\deg_{X,Y}\mathcal H_3=3,
\quad
\deg_\zeta\mathcal H_3=2,
\quad
\#\operatorname{supp}=24.}
\tag{2.2}
\]

四阶更简单：

\[
\boxed{
M^{(4)}
=s_L^4
\frac{65536\,\mathcal H_4(X,Y)}{5^4 11^4},}
\tag{2.3}
\]

其中 exact

\[
\boxed{
\mathcal H_4(X,Y)
=2\cdot3^{12}\cdot13\,(X+Y)^4
+5^4 11^4Y^4.}
\tag{2.4}
\]

所以

\[
\boxed{\mathcal H_4>0}
\tag{2.5}
\]
对 positive parent coordinates无条件成立。

`H_3` 的 expanded 24 项由 checker canonical 重建。其 projective form在

\[
0<1/K<10^{-3},
\qquad
0<\zeta/K<10^{-3},
\qquad
0<X/Y<1/23
\]
上的全部 36 个 exact Bernstein coefficients严格为正：

\[
\boxed{
77742383923
\le b
\le
\frac{70017378306520823817}{760437500}.}
\tag{2.6}
\]

故真实 endpoint上

\[
\boxed{\mathcal H_3>0.}
\tag{2.7}
\]

---

## 3. recursive third-order integer

上一层定义

\[
\mathscr N_{63}^{(2)}
=U_2(M^{(1)}+M^{(2)}),
\]
其中 `U_2` 为 genuine p-unit rational scale。

定义

\[
\boxed{
\begin{aligned}
\mathscr N_{63}^{(3)}:={}&
5^mB^2\mathscr N_{63}^{(2)}\\
&+2^{4M+17}5^2 11^2T^6
\mathcal H_3(X,Y;K,a_3/T).
\end{aligned}}
\tag{3.1}
\]

直接代

\[
s_L=\frac{2^{2M+2}}{5^mB^2K^2}
\]
验证：

\[
\boxed{
\mathscr N_{63}^{(3)}
=U_3(M^{(1)}+M^{(2)}+M^{(3)}),}
\tag{3.2}
\]

其中

\[
U_3=(5^mB^2)U_2
\]
仍为 genuine p-unit rational scale。

定义

\[
S_1:=\gcd(G_\Delta,\mathscr B_{63}),
\qquad
S_2:=\gcd(G_\Delta,\mathscr C_{63}^{(2)}).
\tag{3.3}
\]

已有

\[
\mathscr N_{63}^{(2)}
=-G_\Delta S_1\mathscr C_{63}^{(2)}.
\]

所以第一行被 `G_Delta S_1 S_2` 整除。

第二行中 `H_3` 对 `(X,Y)` 齐次三次，而 `G_Delta|X,Y`；故被 `G_Delta^3` 整除。因为 `S_1,S_2|G_Delta`：

\[
\boxed{
G_\Delta S_1S_2
\mid\mathscr N_{63}^{(3)}.}
\tag{3.4}
\]

---

## 4. third-order real sign

写 reduced real parent ratio

\[
\chi=X/Y,
\qquad
w:=s_LY.
\]

由

\[
L=s_L(X+Y)=w(1+\chi)
\]
以及 actual projective box：

\[
0<w<L<\frac8{125}.}
\tag{4.1}
\]

令

\[
M^{(n)}=w^n h_n(K,\zeta,\chi).
\]

exact Bernstein bounds给

\[
\boxed{h_1<-350000,}
\tag{4.2}
\]

\[
\boxed{h_2<0,}
\tag{4.3}
\]

\[
\boxed{0<h_3<1500000.}
\tag{4.4}
\]

于是

\[
h_1+w h_2+w^2h_3
<h_1+\left(\frac8{125}\right)^2 1500000<0.
\]

故

\[
\boxed{
M^{(1)}+M^{(2)}+M^{(3)}<0,}
\tag{4.5}
\]
从 (3.2)：

\[
\boxed{\mathscr N_{63}^{(3)}<0.}
\tag{4.6}
\]

定义 positive third tail

\[
\boxed{
\mathscr C_{63}^{(3)}
:=-\frac{\mathscr N_{63}^{(3)}}{G_\Delta S_1S_2}
\in\mathbf Z_{>0}.}
\tag{4.7}
\]

---

## 5. recursive terminal fourth-order integer

定义

\[
S_3:=\gcd(G_\Delta,\mathscr C_{63}^{(3)}).
\tag{5.1}
\]

再定义 terminal integer

\[
\boxed{
\begin{aligned}
\mathscr N_{63}^{(4)}:={}&
5^mB^2\mathscr N_{63}^{(3)}\\
&+2^{6M+22}5^3 11^3T^6
\mathcal H_4(X,Y).
\end{aligned}}
\tag{5.2}
\]

同样直接代 `s_L` 与 (2.3)：

\[
\boxed{
\mathscr N_{63}^{(4)}
=U_4M,}
\tag{5.3}
\]

其中

\[
U_4=(5^mB^2)U_3
\]
为 genuine p-unit rational scale。这里使用了 (1.1)：四阶以后没有任何 remainder。

由 (4.7)，第一行被

\[
G_\Delta S_1S_2S_3
\]
整除；第二行因 `H_4` 齐次四次而被 `G_Delta^4` 整除。因此

\[
\boxed{
G_\Delta S_1S_2S_3
\mid\mathscr N_{63}^{(4)}.}
\tag{5.4}
\]

---

## 6. terminal real sign

(2.4) 给 `h_4>0`。actual ratio `chi<1/23` 还给粗但严格界

\[
\boxed{0<h_4<183000.}
\tag{6.1}
\]

结合 §4 与 `w<8/125`：

\[
\begin{aligned}
&h_1+w h_2+w^2h_3+w^3h_4\\
&< -350000
+\left(\frac8{125}\right)^2 1500000
+\left(\frac8{125}\right)^3 183000
<0.
\end{aligned}
\]

所以 exact full remainder在真实 endpoint满足

\[
\boxed{M<0,}
\tag{6.2}
\]
从而

\[
\boxed{\mathscr N_{63}^{(4)}<0.}
\tag{6.3}
\]

定义 positive terminal tail

\[
\boxed{
\mathscr C_{63}^{(4)}
:=-\frac{\mathscr N_{63}^{(4)}}
{G_\Delta S_1S_2S_3}
\in\mathbf Z_{>0}.}
\tag{6.4}
\]

---

## 7. exact recursive support laws

固定 genuine common prime，写

\[
h=v_p(G_\Delta),
\quad
\rho=v_p(B_{63}),
\quad
\sigma=v_p(C_{63}^{(2)}),
\quad
\tau=v_p(C_{63}^{(3)}),
\quad
\kappa=v_p(C_{63}^{(4)}).
\]

逐层使用 `S_i` 的定义，有：

### first unsaturated layer

若

\[
\rho<h,
\]
则已有

\[
\boxed{v_p(M)=h+\rho.}
\tag{7.1}
\]

### second unsaturated layer

若

\[
\rho\ge h,
\qquad
\sigma<h,
\]
则

\[
\boxed{v_p(M)=2h+\sigma.}
\tag{7.2}
\]

### third unsaturated layer

若

\[
\rho\ge h,
\qquad
\sigma\ge h,
\qquad
\tau<h,
\]
则 `N_63^(3)` 有 exact depth `3h+tau`，而 quartic block至少 `4h`，所以

\[
\boxed{v_p(M)=3h+\tau.}
\tag{7.3}
\]

### all first three layers saturated

若

\[
\rho\ge h,
\qquad
\sigma\ge h,
\qquad
\tau\ge h,
\]
则 denominator in (6.4)在 `p` 上恰为 `p^(4h)`。由于 `N_63^(4)=U_4M` 且 `U_4` 为 p-unit：

\[
\boxed{
v_p(M)=4h+\kappa.}
\tag{7.4}
\]

这里没有 truncation：四阶就是 terminal exact formula。

所以 entire p-adic depth被有限四层 ordinary tails完全解析：

\[
\boxed{
\begin{array}{c|c}
\rho<h & h+\rho,\\
\rho\ge h,\ \sigma<h & 2h+\sigma,\\
\rho,\sigma\ge h,\ \tau<h & 3h+\tau,\\
\rho,\sigma,\tau\ge h & 4h+\kappa.
\end{array}}
\tag{7.5}
\]

因此**不再存在未显式记录的 fifth-order normalized unit**。

---

## 8. third-order 2-adic parity surcharge

`H_3` 清 `T^6` 后，checker验证唯一最低 binary monomial为

\[
\boxed{
-8800610472\,X^3\zeta^2
=-2^3 3^8\cdot107\cdot1567\,X^3\zeta^2.}
\tag{8.1}
\]

对应 ordinary term为

\[
-2^3 3^8\cdot107\cdot1567\,X^3a_3^2T^4.
\]

其它23项在 `(m,t)=(5,3)` 已至少更深6层，且相对 slopes非负。因此 (3.1) cubic block唯一控制 `N_63^(3)` 的最低 binary layer；第一行额外至少深 `2t>=6`。

于是

\[
\boxed{
v_2(\mathscr N_{63}^{(3)})
=4M+4m+20.}
\tag{8.2}

除去该幂后：

\[
\frac{\mathscr N_{63}^{(3)}}{2^{4M+4m+20}}
\equiv3X\pmod8.
\tag{8.3}

已有

\[
X=5^\lambda Rstar,
\qquad
Rstar\equiv3\pmod4,
\]
所以

\[
X\equiv3\pmod4.
\]
故 (8.3) 给

\[
\boxed{
\frac{\mathscr N_{63}^{(3)}}{2^{4M+4m+20}}
\equiv1\pmod4.}
\tag{8.4}

结合 `N_63^(3)<0`：

\[
\boxed{
\frac{-\mathscr N_{63}^{(3)}}{2^{4M+4m+20}}
\equiv3\pmod4.}
\tag{8.5}

所以 third-order positive parent numerator必含 odd number of `3 mod4` prime valuations：连续两层 full-baseline saturation进入三阶时会产生一份新的 odd-inert parity surcharge。

---

## 9. terminal 2-adic orientation

`H_4` 中 `Y` 带额外 binary depth，唯一最低项是

\[
2\cdot3^{12}\cdot13\,X^4.
\]

清 `T^6` 后仍唯一最低。由 (5.2)：

\[
\boxed{
v_2(\mathscr N_{63}^{(4)})
=6M+6m+23.}
\tag{9.1}
\]

第一行至少再深

\[
2t-3\ge3
\]
层。

primitive residue为

\[
5^3 11^3\cdot3^{12}\cdot13
\equiv3\pmod8,
\]
且 `X^4`、`(T/2^m)^6` 都为 `1 mod8`。所以

\[
\boxed{
\frac{\mathscr N_{63}^{(4)}}{2^{6M+6m+23}}
\equiv3\pmod8.}
\tag{9.2}

结合 negativity：

\[
\boxed{
\frac{-\mathscr N_{63}^{(4)}}{2^{6M+6m+23}}
\equiv5\pmod8.}
\tag{9.3}

terminal positive parent numerator的 total inert parity因此为偶数。

---

## 10. revised descendant frontier

same-prime descendant recycling现在已经不再有无限-order local ambiguity。所有 depth都由

\[
\boxed{
B_{63},\quad
C_{63}^{(2)},\quad
C_{63}^{(3)},\quad
C_{63}^{(4)}}
\]
四个 ordinary integers递归读取；第四个是 terminal exact tail。

真正 generic branch若想连续跨越前三个 common baselines，必须同时满足

\[
\boxed{
\rho\ge h,
\qquad
\sigma\ge h,
\qquad
\tau\ge h,}
\]
并且此过程还伴随 §8 的 new odd-inert third-order surcharge。

下一步最值得做的已经不是继续 Taylor expansion，而是：

1. 审计 third-order surcharge能否由原 `G_Delta` / target / source pools复用；
2. 在 fully saturated branch上研究 terminal `C_63^(4)` 与 parent coordinates的 gcd；
3. 或把 simple quartic coefficient (2.4) 与 first-order balance ratio联立，得到 terminal saturation的固定 algebraic gate。

A2 仍为 `待证`。

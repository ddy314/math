# A2 spontaneous/additive height parity ledger

> **依赖：** `primitive-reduction.md`、`height-cofactor.md`、`spontaneous-angle-parity.md`、`spontaneous-prefix-eliminant.md`、`decimal-prefix-bridge.md`。
>
> **严格状态：**本文把 reduced numerator `W_q` 与 angle/additive 两个 primitive `3 mod 4` carrier 的共同部分全部改写为纯 decimal integer。additive-height 由一个新的 positive `3 mod 4` integer `J_H` 精确读取；angle-height 则由 actual/conjugate 两个 positive `3 mod 4` angle sheets 的乘积读取，并产生一个 positive `1 mod 8` height norm `H_O`。对 endpoint-external height prime，actual 与 conjugate sheet 互斥，且 `H_O` 与 actual angle carrier 在 `v_p(W_q)` 深度内具有相同截断赋值。本文不证明所有 additive external odd prime 必进入 `W_q`，也不宣称 A2 全局关闭。

---

## 1. 原始 decimal blocks

固定 reflection endpoint，记

\[
N:=10^M,
\qquad T:=10^m,
\qquad A:=a_2,
\qquad B:=b_2,
\]

\[
Q:=B+2N,
\qquad
K:=9N+10A,
\]

\[
N_0:=\left(\frac{9B}{2}\right)^2+A^2.
\tag{1.1}
\]

`spontaneous-prefix-eliminant.md` 的 pure-prefix angle integer为

\[
\boxed{
\mathcal U_\Omega
=(45B^2-2AN)^2-A^2B(99B-4N).
}
\tag{1.2}
\]

原 angle raw carrier 是

\[
\boxed{
\mathcal O_+
:=T\mathcal U_\Omega+2A^2Qb_3.
}
\tag{1.3}
\]

它与 `spontaneous-angle-parity.md` 的 primitive carrier关系为

\[
\mathcal O_+
=2^{2M+m+2}\widehat{\mathcal O}_{\rm sp}.
\tag{1.4}
\]

已有

\[
\widehat{\mathcal O}_{\rm sp}>0,
\qquad
\widehat{\mathcal O}_{\rm sp}\equiv3\pmod4.
\tag{1.5}
\]

height/reduced numerator 仍使用

\[
\alpha:=TK+a_3=\omega W_q,
\qquad
H_0=c_uW_q.
\tag{1.6}
\]

且 `primitive-reduction.md` 已证明 `W_q` 为 odd、`5`-free，并与 `gc_Q` 分离。

---

## 2. `已严格完成`：additive-height 具有纯 decimal exact bridge

定义

\[
\boxed{
\mathcal J_H
:=B^2(5K^2-36K+55)-Q^2N_0.
}
\tag{2.1}
\]

另一方面

\[
\Theta_{\rm dec}
=T\mathcal R_\Theta-2B^2(2K-9)a_3,
\]

其中

\[
\mathcal R_\Theta
=B^2(K^2-18K+55)-Q^2N_0.
\]

由

\[
a_3=\omega W_q-TK
\]
直接代入：

\[
\begin{aligned}
\Theta_{\rm dec}
={}&T\mathcal R_\Theta
-2B^2(2K-9)(\omega W_q-TK)\\
={}&T\left[\mathcal R_\Theta+2B^2K(2K-9)\right]
-2B^2(2K-9)\omega W_q.
\end{aligned}
\]

方括号恰为 `J_H`，故

\[
\boxed{
\Theta_{\rm dec}
=T\mathcal J_H
-2B^2(2K-9)\omega W_q.
}
\tag{2.2}
\]

由于 `W_q` 与 `T` 互素且为奇数，(2.2) 立即给全局 gcd identity：

\[
\boxed{
\gcd(\Theta_{\rm dec},W_q)
=
\gcd(\mathcal J_H,W_q).
}
\tag{2.3}
\]

又

\[
\Theta_{\rm dec}
=2^{2M+m+2}\widehat{\mathcal T}_2
\]
而 `W_q` 为奇数，因此进一步

\[
\boxed{
\gcd(\widehat{\mathcal T}_2,W_q)
=
\gcd(\mathcal J_H,W_q).
}
\tag{2.4}
\]

逐 prime-power 地，若

\[
p^h\Vert W_q,
\qquad p\ne2,5,
\]
则

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),h\}
=
\min\{v_p(\mathcal J_H),h\}.
}
\tag{2.5}
\]

这与 `height-cofactor.md` 的 `B_W` bridge 等价于同一 height flow，但 (2.1) 完全 source-free，只含真实 decimal blocks。

---

## 3. `已严格完成`：`J_H` 本身是 positive primitive `3 mod 4` carrier

reflection deep-even 中

\[
B=2^{M+m+1}c_ug,
\qquad
Q=2^{M+1}Q_0,
\]
其中 `Q_0` 为奇数；并且 `A` 为奇数。

`K=10P` 且当前 `P` 为奇数，所以

\[
5K^2-36K+55
\]
为奇数。

第一项 `B^2(\cdots)` 的 `2`-进深度为

\[
2M+2m+2,
\]
而

\[
v_2(Q^2N_0)=2M+2,
\]
因为 `N_0` 为奇数。因此

\[
\boxed{v_2(\mathcal J_H)=2M+2.}
\tag{3.1}
\]

定义

\[
\boxed{
\widehat{\mathcal J}_H
:=\frac{\mathcal J_H}{2^{2M+2}}.
}
\tag{3.2}
\]

因为 `m>=1`，第一项在 (3.2) 中被 `4` 整除，而

\[
N_0\equiv A^2\equiv1\pmod4,
\qquad Q_0^2\equiv1\pmod4.
\]
故

\[
\boxed{
\widehat{\mathcal J}_H\equiv-1\equiv3\pmod4.
}
\tag{3.3}
\]

它还严格为正。用 normalized variables

\[
x=B/N,
\quad y=10A/N,
\quad \tau=N^{-1},
\quad s=9+y
\]
可写成

\[
\frac{100\mathcal J_H}{N^4}
=
100x^2(5s^2-36s\tau+55\tau^2)
-(x+2)^2(2025x^2+y^2).
\tag{3.4}
\]

在 endpoint box

\[
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1,
\qquad
0<\tau<10^{-11},
\]
第一项统一大于 `~499`，第二项小于 `100`，故

\[
\boxed{
\mathcal J_H>0.
}
\tag{3.5}
\]

因此 additive-height companion 自身也是一份新的 positive `3 mod 4` primitive integer：

\[
\boxed{
\widehat{\mathcal J}_H>0,
\qquad
\widehat{\mathcal J}_H\equiv3\pmod4.
}
\tag{3.6}
\]

---

## 4. `已严格完成`：angle carrier 存在 natural conjugate sheet

定义 actual / conjugate angle raw integers

\[
\boxed{
\mathcal O_+
=T\mathcal U_\Omega+2A^2Qb_3,
}
\tag{4.1}
\]

\[
\boxed{
\mathcal O_-
=T\mathcal U_\Omega-2A^2Qb_3.
}
\tag{4.2}
\]

两者只差

\[
\boxed{
\mathcal O_+-\mathcal O_-
=4A^2Qb_3.
}
\tag{4.3}
\]

`spontaneous-angle-parity.md` 已证明

\[
v_2(T\mathcal U_\Omega)=2M+m+2
\]
且

\[
\frac{T\mathcal U_\Omega}{2^{2M+m+2}}
\equiv1\pmod4.
\]

又

\[
\frac{2A^2Qb_3}{2^{2M+m+2}}
\equiv2\pmod4.
\]
注意 `+2` 与 `-2` 模 `4` 都等于 `2`，所以

\[
\boxed{
v_2(\mathcal O_+)
=v_2(\mathcal O_-)
=2M+m+2,
}
\tag{4.4}
\]

并且定义

\[
\widehat{\mathcal O}_\pm
:=\frac{\mathcal O_\pm}{2^{2M+m+2}}
\]
后有

\[
\boxed{
\widehat{\mathcal O}_+
\equiv
\widehat{\mathcal O}_-
\equiv3\pmod4.
}
\tag{4.5}
\]

两者在真实 endpoint 中都为正。由

\[
\mathcal U_\Omega=\frac{N^4}{100}A_{\rm sp},
\qquad
\bar w=\frac{b_3}{TN},
\]
可写成

\[
\boxed{
\mathcal O_\pm
=\frac{TN^4}{100}
\left[
A_{\rm sp}
\pm2y^2(x+2)\bar w
\right].
}
\tag{4.6}
\]

已有 `A_sp>5`；而 `M>=11`、`b_3/T<843/1000` 给 `bar w<10^{-11}`。因此括号在两个符号下都严格为正：

\[
\boxed{
\widehat{\mathcal O}_\pm>0.
}
\tag{4.7}
\]

所以 actual 与 conjugate angle sheet 各自都携带 odd inert parity。

---

## 5. `已严格完成`：height norm 是 actual/conjugate angle carrier 的乘积模 `W_q`

定义

\[
\boxed{
\mathcal H_O
:=N_0\mathcal U_\Omega^2
+4A^4B^2Q^2K^2.
}
\tag{5.1}
\]

先注意

\[
\mathcal O_+\mathcal O_-
=T^2\mathcal U_\Omega^2
-4A^4Q^2b_3^2.
\tag{5.2}
\]

因此

\[
\begin{aligned}
T^2\mathcal H_O-N_0\mathcal O_+\mathcal O_-
={}&4A^4Q^2
\left(b_3^2N_0+B^2T^2K^2\right).
\end{aligned}
\tag{5.3}
\]

使用

\[
TK=\alpha-a_3,
\qquad
\alpha=\omega W_q,
\]
以及 exact height square

\[
\boxed{
b_3^2N_0+B^2a_3^2
=\left(\frac{BH_0}{g}\right)^2,
}
\tag{5.4}
\]

得到

\[
\boxed{
\begin{aligned}
T^2\mathcal H_O
={}&N_0\mathcal O_+\mathcal O_-\\
&+4A^4Q^2W_q
\left[
W_q\left(\left(\frac{Bc_u}{g}\right)^2+B^2\omega^2\right)
-2B^2\omega a_3
\right].
\end{aligned}}
\tag{5.5}
\]

这里 `B/g` 是整数，所以整个式子在整数环中成立。

特别地模 `W_q`：

\[
\boxed{
T^2\mathcal H_O
\equiv
N_0\mathcal O_+\mathcal O_-
\pmod{W_q}.
}
\tag{5.6}
\]

这是本文的核心 height-angle product bridge。

---

## 6. `已严格完成`：endpoint-external height prime 上 actual / conjugate sheet互斥

固定 non-`3` inert endpoint-external height prime

\[
p^h\Vert W_q,
\qquad
p\nmid qf.
\]

height 本原性与 angle-content 分离给

\[
p\nmid 10A Qb_3N_0.
\tag{6.1}
\]

这里 `p\nmid A` 也可由 height character恢复：若 `p\mid A`，则 `N_0=(9B/2)^2` 为平方，与 non-`3` inert height prime的 `N_0` 非剩余性质冲突。

由 (4.3)，若 `p` 同时整除 `O_+` 与 `O_-`，则 `p|4A^2Qb_3`，与 (6.1) 矛盾。因此

\[
\boxed{
p\mid W_q,\ p\nmid qf
\Longrightarrow
p\text{ 不可能同时命中 }\mathcal O_+,\mathcal O_-.
}
\tag{6.2}
\]

若进一步

\[
p\mid\mathcal O_+,
\]
则 `O_-` 为单位。由 (5.6)，因为 `T,N_0` 也是单位，得到完整截断赋值律：

\[
\boxed{
\min\{v_p(\mathcal H_O),h\}
=
\min\{v_p(\mathcal O_+),h\}.
}
\tag{6.3+}
\]

同理若 `p|O_-`：

\[
\boxed{
\min\{v_p(\mathcal H_O),h\}
=
\min\{v_p(\mathcal O_-),h\}.
}
\tag{6.3-}
\]

所以 external height 上的 angle contact不是新的 source ratio；它只是 `H_O` 的两个互斥 simple sheets。

q-side 的固定 `p=23` 允许 `Q=0 mod p`，故不被 (6.1)–(6.3) 偷偷包含；该浅层例外已经由 `fixed-denominator-height-angle.md` 单独审计。

---

## 7. `已严格完成`：`H_O` 精确分裂成两个 pure-prefix orientation integers

把

\[
x=B/N,
\qquad y=10A/N
\]
代入 source-free sphere orientation。定义两个整数

\[
\boxed{
\mathcal H_1
:=2025B^4+101A^2B^2+4A^2BN+4A^2N^2,
}
\tag{7.1}
\]

以及

\[
\boxed{
\begin{aligned}
\mathcal H_2:={}&
404A^4B^2+16A^4BN+16A^4N^2
+1440A^3B^2N\\
&-16119A^2B^4+324A^2B^3N
+1620A^2B^2N^2\\
&-29160AB^4N+164025B^6.
\end{aligned}}
\tag{7.2}
\]

直接展开得到 exact factorization

\[
\boxed{
\mathcal H_1\mathcal H_2
=4\mathcal H_O.
}
\tag{7.3}
\]

normalized 形式分别为

\[
H_1(x,y)
=202500x^4+101x^2y^2+4xy^2+4y^2,
\tag{7.4}
\]

\[
\begin{aligned}
H_2(x,y)={}&
410062500x^6-402975x^4y^2-7290000x^4y\\
&+8100x^3y^2+101x^2y^4+3600x^2y^3\\
&+40500x^2y^2+4xy^4+4y^4.
\end{aligned}
\tag{7.5}
\]

若 `Omega` 固定 third denominator，并令 height root

\[
\bar\zeta=-s,
\qquad s=9+y,
\]
则 exact sphere remainder 为

\[
\boxed{
\mathscr S\big|_{\Omega,\,\bar\zeta=-s}
=
-\frac{A_-^2H_1H_2}
{1600y^8(x+2)^4}.
}
\tag{7.6}
\]

因此在 genuine `A_-xy(x+2) != 0` channel：

\[
\boxed{
\text{angle}\cap\text{height}
\Longrightarrow
H_1H_2=0.
}
\tag{7.7}

两因子正是 sphere 的两个 rational third-numerator orientations撞上 height root `bar zeta=-s` 的两张 pure-prefix sheet。

---

## 8. `已严格完成`：两个 orientation integer 都是 primitive `1 mod 4`

利用

\[
B=2^{M+m+1}b_0,
\qquad
N=2^M5^M,
\qquad A\text{ odd},
\]
逐项比较 (7.1)：最浅项是

\[
4A^2N^2
\]
的深度 `2M+2`，其它项至少再深两层。因此

\[
\boxed{v_2(\mathcal H_1)=2M+2,}
\tag{8.1}
\]

并且

\[
\boxed{
\frac{\mathcal H_1}{2^{2M+2}}
\equiv1\pmod4.
}
\tag{8.2}
\]

同理 (7.2) 的唯一最浅项是

\[
16A^4N^2,
\]
深度 `2M+4`；其余各项至少再深两层。所以

\[
\boxed{v_2(\mathcal H_2)=2M+4,}
\tag{8.3}
\]

\[
\boxed{
\frac{\mathcal H_2}{2^{2M+4}}
\equiv1\pmod4.
}
\tag{8.4}
\]

由 (7.3)：

\[
\boxed{v_2(\mathcal H_O)=4M+4.}
\tag{8.5}
\]

更直接地，由 (5.1) 第一项为唯一最浅项，`U_Omega/2^{2M+2}` 与 `N_0` 都为 odd square-class `1 mod 8`，得到

\[
\boxed{
\widehat{\mathcal H}_O
:=\frac{\mathcal H_O}{2^{4M+4}}
\equiv1\pmod8.
}
\tag{8.6}
\]

`H_O>0` 显然，故 (7.3) 与 `H_1>0` 还给 `H_2>0`。因此：

\[
\boxed{
\widehat{\mathcal H}_O>0,
\qquad
\widehat{\mathcal H}_O\equiv1\pmod8.
}
\tag{8.7}
\]

---

## 9. three-carrier height ledger

本文得到的 pure-decimal height ledger 可总结为

\[
\boxed{
\begin{array}{c|c|c}
\text{channel}&\text{decimal carrier}&\text{primitive orientation}\\ \hline
\text{additive}\cap W_q&\widehat{\mathcal J}_H&3\pmod4\\
\text{actual angle}&\widehat{\mathcal O}_+&3\pmod4\\
\text{conjugate angle}&\widehat{\mathcal O}_-&3\pmod4\\
\text{angle product over height}&\widehat{\mathcal H}_O&1\pmod8.
\end{array}}
\tag{9.1}
\]

并且

\[
\boxed{
\gcd(\widehat{\mathcal T}_2,W_q)
=
\gcd(\widehat{\mathcal J}_H,W_q),
}
\tag{9.2}
\]

而对 endpoint-external angle-height prime：

\[
\boxed{
\min(v_p(\widehat{\mathcal O}_\pm),v_p(W_q))
=
\min(v_p(\widehat{\mathcal H}_O),v_p(W_q))
}
\tag{9.3}
\]
在对应 actual/conjugate sheet上成立。

如果同一个 endpoint-external inert prime同时进入

\[
W_q,
\quad
\widehat{\mathcal O}_{\rm sp},
\quad
\widehat{\mathcal T}_2,
\]
则它现在完全由 pure decimal system

\[
\boxed{
H_1H_2=0,
\qquad
J_H=0
}
\tag{9.4}
\]
读取；source ratio、`c_u,q,g,omega` 都已从 first-layer common geometry中消失。

---

## 10. 对 global `G_sp` parity 的更新

本文仍没有证明

\[
G_{\rm sp}
=\gcd(\widehat{\mathcal O}_{\rm sp},\widehat{\mathcal T}_2)
\equiv3\pmod4.
\]

但它删除了 global parity ledger 中一个长期混杂的自由度：**height-supported residual 不再需要同时追 source split 与 third-block sphere。**

现在 height pool只有：

1. fixed saturated shallow corrections `7,23,43`，已由 `fixed-denominator-height-angle.md` 完整 first-layer分类；
2. endpoint-external actual/conjugate angle sheets，由 `H_1,H_2` 控制；
3. additive-height depth，由 positive `3 mod 4` carrier `J_H` 控制。

下一步应直接研究 (9.4) 的 external moving roots与 global parity allocation，特别是：

- additive external odd carrier是否必须进入 `W_q`；
- 若进入 `W_q`，`J_H` 与 `H_1/H_2` 的 common depth能否只留下 fixed shallow correction；
- actual 与 conjugate `O_+,O_-` 各自都是 `3 mod 4`，它们在 `W_q` 上互斥，这能否把 `G_sp=1 mod4` 所要求的两份分离 residual parity压回同一个 external prime-source。

在这些问题解决前，A2 仍保持 open。
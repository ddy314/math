# A2 spontaneous/additive height parity ledger

> **依赖：** `primitive-reduction.md`、`height-cofactor.md`、`spontaneous-angle-parity.md`、`spontaneous-prefix-eliminant.md`、`decimal-prefix-bridge.md`。
>
> **严格状态：**本文把 reduced numerator `W_q` 与 angle/additive 两个 primitive `3 mod 4` carrier 的 height-supported 部分改写为纯 decimal integers。additive-height 由一个新的 positive `3 mod 4` integer `J_H` 精确读取；angle-height 则由 actual/conjugate 两个 positive `3 mod 4` angle sheets 的乘积读取，并产生一个 positive `1 mod 8` height norm `H_O`。对 endpoint-external height prime，actual 与 conjugate sheet互斥，且 `H_O` 与命中的 angle sheet在 `v_p(W_q)` 深度内具有相同截断赋值。本文不证明所有 additive external odd prime 必进入 `W_q`，也不宣称 A2 全局关闭。

---

## 1. 记号

固定 reflection endpoint：

\[
N=10^M,
\quad T=10^m,
\quad A=a_2,
\quad B=b_2,
\]

\[
Q=B+2N,
\qquad
K=9N+10A,
\]

\[
N_0=\left(\frac{9B}{2}\right)^2+A^2.
\tag{1.1}
\]

angle pure-prefix integer为

\[
\boxed{
\mathcal U_\Omega
=(45B^2-2AN)^2-A^2B(99B-4N).
}
\tag{1.2}
\]

原 angle raw carrier记作

\[
\boxed{
\mathcal O_+
:=T\mathcal U_\Omega+2A^2Qb_3.
}
\tag{1.3}
\]

已有

\[
\mathcal O_+
=2^{2M+m+2}\widehat{\mathcal O}_{\rm sp},
\qquad
\widehat{\mathcal O}_{\rm sp}>0,
\qquad
\widehat{\mathcal O}_{\rm sp}\equiv3\pmod4.
\tag{1.4}
\]

height/reduced numerator为

\[
\boxed{
\alpha=TK+a_3=\omega W_q,
\qquad
H_0=c_uW_q.
}
\tag{1.5}

---

## 2. additive-height 的 pure-decimal bridge

定义

\[
\boxed{
\mathcal J_H
:=B^2(5K^2-36K+55)-Q^2N_0.
}
\tag{2.1}
\]

由

\[
\Theta_{\rm dec}
=T\bigl[B^2(K^2-18K+55)-Q^2N_0\bigr]
-2B^2(2K-9)a_3
\]
和

\[
a_3=\omega W_q-TK
\]
直接得到

\[
\boxed{
\Theta_{\rm dec}
=T\mathcal J_H
-2B^2(2K-9)\omega W_q.
}
\tag{2.2}
\]

`W_q` 为 odd 且 `gcd(T,W_q)=1`，故

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
\Theta_{\rm dec}=2^{2M+m+2}\widehat{\mathcal T}_2,
\]
所以

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

这把 additive-height depth 从 source quantity `B_W` 再降成一个完全 source-free 的 decimal integer。

---

## 3. `J_H` 是 positive primitive `3 mod 4` integer

reflection deep-even 中

\[
B=2^{M+m+1}b_0,
\qquad
Q=2^{M+1}Q_0,
\]
其中 `b_0,Q_0` 为奇数，且 `A,N_0` 均为奇数。

`5K^2-36K+55` 为奇数。因此 `J_H` 两项的 `2`-进深度分别是

\[
2M+2m+2,
\qquad
2M+2.
\]

由于 `m>=1`：

\[
\boxed{v_2(\mathcal J_H)=2M+2.}
\tag{3.1}
\]

令

\[
\widehat{\mathcal J}_H
:=\frac{\mathcal J_H}{2^{2M+2}}.
\]
第一项被 `4` 整除，而第二项模 `4` 为 `-Q_0^2N_0=-1`，故

\[
\boxed{
\widehat{\mathcal J}_H\equiv3\pmod4.
}
\tag{3.2}
\]

它还严格为正。令

\[
x=B/N,
\quad y=10A/N,
\quad \tau=N^{-1},
\quad s=9+y.
\]
则

\[
\frac{100\mathcal J_H}{N^4}
=
100x^2(5s^2-36s\tau+55\tau^2)
-(x+2)^2(2025x^2+y^2).
\tag{3.3}
\]

endpoint box 给

\[
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1,
\qquad
0<\tau<10^{-11}.
\]

第一项统一 `>499`；第二项统一 `<104`。因此

\[
\boxed{
\mathcal J_H>0,
\qquad
\widehat{\mathcal J}_H>0,
\qquad
\widehat{\mathcal J}_H\equiv3\pmod4.
}
\tag{3.4}

---

## 4. actual/conjugate angle sheets

定义

\[
\boxed{
\mathcal O_\pm
:=T\mathcal U_\Omega\pm2A^2Qb_3.
}
\tag{4.1}
\]

所以

\[
\boxed{
\mathcal O_+-\mathcal O_-=4A^2Qb_3.
}
\tag{4.2}
\]

`spontaneous-angle-parity.md` 已证明

\[
\frac{T\mathcal U_\Omega}{2^{2M+m+2}}
\equiv1\pmod4,
\]
而

\[
\frac{2A^2Qb_3}{2^{2M+m+2}}
\equiv2\pmod4.
\]
由于 `+2` 与 `-2` 模 `4` 都等于 `2`：

\[
\boxed{
 v_2(\mathcal O_+)
=v_2(\mathcal O_-)
=2M+m+2,
}
\tag{4.3}
\]

\[
\boxed{
\widehat{\mathcal O}_+
\equiv
\widehat{\mathcal O}_-
\equiv3\pmod4.
}
\tag{4.4}
\]

两者在真实 endpoint 上都为正。事实上

\[
\mathcal U_\Omega=\frac{N^4}{100}A_{\rm sp},
\qquad
\bar w=\frac{b_3}{TN},
\]
给

\[
\boxed{
\mathcal O_\pm
=\frac{TN^4}{100}
\left(A_{\rm sp}\pm2y^2(x+2)\bar w\right).
}
\tag{4.5}
\]

已有 `A_sp>5`，而 `M>=11` 与 `b_3/T<843/1000` 给 `bar w<10^{-11}`，故两个括号都严格为正。

因此 actual 与 conjugate angle sheet **各自**都是 positive primitive `3 mod 4` carrier。

---

## 5. height norm 与两个 angle sheets 的 exact product bridge

定义

\[
\boxed{
\mathcal H_O
:=N_0\mathcal U_\Omega^2
+4A^4B^2Q^2K^2.
}
\tag{5.1}
\]

由

\[
\mathcal O_+\mathcal O_-
=T^2\mathcal U_\Omega^2-4A^4Q^2b_3^2
\]
有

\[
T^2\mathcal H_O-N_0\mathcal O_+\mathcal O_-
=
4A^4Q^2\left(b_3^2N_0+B^2T^2K^2\right).
\tag{5.2}
\]

使用

\[
TK=\omega W_q-a_3
\]
及 exact height square

\[
\boxed{
 b_3^2N_0+B^2a_3^2
=\left(\frac{BH_0}{g}\right)^2
}
\tag{5.3}
\]
和 `H_0=c_uW_q`，得到

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
\tag{5.4}
\]

因此

\[
\boxed{
T^2\mathcal H_O
\equiv
N_0\mathcal O_+\mathcal O_-
\pmod{W_q}.
}
\tag{5.5}
\]

这是 height-supported angle parity 的核心 product bridge。

---

## 6. endpoint-external height prime 上两张 sheet互斥

固定 non-`3` inert endpoint-external height prime

\[
p^h\Vert W_q,
\qquad
p\nmid qf.
\]

height 本原性与 angle-content 分离给

\[
p\nmid10AQb_3N_0.
\tag{6.1}
\]

由 (4.2)，这种 prime 不可能同时整除 `O_+` 与 `O_-`。

因此若 `p|O_+`，则 `O_-` 是单位，结合 (5.5)：

\[
\boxed{
\min\{v_p(\mathcal H_O),h\}
=
\min\{v_p(\mathcal O_+),h\}.
}
\tag{6.2+}
\]

若 `p|O_-`，同理

\[
\boxed{
\min\{v_p(\mathcal H_O),h\}
=
\min\{v_p(\mathcal O_-),h\}.
}
\tag{6.2-}
\]

q-side fixed `23` 允许 `Q=0 mod23`，因此不被本节偷偷包含；它已经在 `fixed-denominator-height-angle.md` 中单列。

---

## 7. `H_O` 分裂成两个 pure-prefix sphere orientations

定义

\[
\boxed{
\mathcal H_1
=2025B^4+101A^2B^2+4A^2BN+4A^2N^2,
}
\tag{7.1}
\]

\[
\boxed{
\begin{aligned}
\mathcal H_2={}&
404A^4B^2+16A^4BN+16A^4N^2
+1440A^3B^2N\\
&-16119A^2B^4+324A^2B^3N
+1620A^2B^2N^2\\
&-29160AB^4N+164025B^6.
\end{aligned}}
\tag{7.2}
\]

直接展开：

\[
\boxed{
\mathcal H_1\mathcal H_2=4\mathcal H_O.
}
\tag{7.3}
\]

normalized factors为

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

当 angle condition固定 third denominator，并令 height root

\[
\bar\zeta=-s,
\qquad s=9+y,
\]
exact sphere remainder精确为

\[
\boxed{
\mathscr S\big|_{\Omega,\bar\zeta=-s}
=-\frac{A_-^2H_1H_2}{1600y^8(x+2)^4}.
}
\tag{7.6}
\]

所以在 genuine `A_-xy(x+2) != 0` channel：

\[
\boxed{
\text{angle}\cap\text{height}
\Longrightarrow
H_1H_2=0.
}
\tag{7.7}

它们就是 sphere 两个 rational orientations撞上 height root `bar zeta=-s` 的两张 pure-prefix sheet。

---

## 8. orientation integers 的 `2`-进方向

由

\[
B=2^{M+m+1}b_0,
\qquad
N=2^M5^M,
\qquad
A\text{ odd},
\]
在 `H_1` 中唯一最浅项为 `4A^2N^2`：

\[
\boxed{
v_2(\mathcal H_1)=2M+2,
\qquad
\frac{\mathcal H_1}{2^{2M+2}}\equiv1\pmod4.
}
\tag{8.1}
\]

在 `H_2` 中唯一最浅项为 `16A^4N^2`：

\[
\boxed{
v_2(\mathcal H_2)=2M+4,
\qquad
\frac{\mathcal H_2}{2^{2M+4}}\equiv1\pmod4.
}
\tag{8.2}

由 (7.3)：

\[
\boxed{v_2(\mathcal H_O)=4M+4.}
\tag{8.3}
\]

而 (5.1) 中第一项在该深度唯一最浅，且 `N_0` 与 `U_Omega/2^{2M+2}` 都是 `1 mod8` square class。因此

\[
\boxed{
\widehat{\mathcal H}_O
:=\frac{\mathcal H_O}{2^{4M+4}}
>0,
\qquad
\widehat{\mathcal H}_O\equiv1\pmod8.
}
\tag{8.4}

`H_O>0` 与 `H_1>0` 再由 (7.3) 给 `H_2>0`。

---

## 9. height parity ledger

当前 height-supported prime flow 已可写成

\[
\boxed{
\begin{array}{c|c|c}
\text{channel}&\text{pure decimal carrier}&\text{primitive orientation}\\ \hline
\text{additive}\cap W_q&\widehat{\mathcal J}_H&3\pmod4\\
\text{actual angle}&\widehat{\mathcal O}_+&3\pmod4\\
\text{conjugate angle}&\widehat{\mathcal O}_-&3\pmod4\\
\text{angle product over height}&\widehat{\mathcal H}_O&1\pmod8.
\end{array}}
\tag{9.1}

并有

\[
\boxed{
\gcd(\widehat{\mathcal T}_2,W_q)
=
\gcd(\widehat{\mathcal J}_H,W_q).
}
\tag{9.2}

对 endpoint-external angle-height prime，对应 sheet还有

\[
\boxed{
\min(v_p(\widehat{\mathcal O}_\pm),v_p(W_q))
=
\min(v_p(\widehat{\mathcal H}_O),v_p(W_q)).
}
\tag{9.3}

因此若同一个 endpoint-external inert prime同时进入

\[
W_q,
\quad
\widehat{\mathcal O}_{\rm sp},
\quad
\widehat{\mathcal T}_2,
\]
其 first-layer common geometry完全由 pure decimal system

\[
\boxed{
H_1H_2=0,
\qquad
\mathcal J_H=0
}
\tag{9.4}
\]
读取。

---

## 10. 当前边界

本文没有证明

\[
G_{\rm sp}
=\gcd(\widehat{\mathcal O}_{\rm sp},\widehat{\mathcal T}_2)
\equiv3\pmod4.
\]

但 height pool 已经不再需要 source ratio、third-block Hensel 或额外 Gaussian character：

- saturated height corrections只剩 fixed `7,23,43`，见 `fixed-denominator-height-angle.md`；
- moving endpoint-external angle-height由 `H_1,H_2` 两张互斥 sheet控制；
- additive-height由 positive `3 mod4` carrier `J_H` 控制。

下一步最值得做的是：

1. 研究 moving system `H_1H_2=J_H=0` 的 prime-source / decimal-orbit；
2. 或证明 additive external odd carrier必须进入 `W_q`，从而把 additive residual parity全部拉进本文 ledger；
3. 利用 actual/conjugate `O_+,O_-` 在 external `W_q` 上互斥，进一步压缩 `G_sp=1 mod4` 所要求的两份独立 residual parity。

在此之前 A2 仍为 open。
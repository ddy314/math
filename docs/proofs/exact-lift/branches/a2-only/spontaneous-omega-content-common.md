# A2 common-`alpha` / `omega` content branch

> **依赖：** `primitive-reduction.md`、`spontaneous-prefix-branch-audit.md`、`spontaneous-height-parity-ledger.md`、`source-discriminant.md`。
>
> **严格状态：**本文把拼接 content `omega=gcd(alpha,beta)` 与 angle/additive 两个 primitive carrier 的公共部分改写成两个 pure-prefix decimal integers `C_omega`、`J_H`。`C_omega=0` 正是此前 `A_-=0` 的 common-`alpha` branch；`J_H=0` 是 additive carrier在 `alpha=0` 上的降维。本文进一步完成这条二维 common-content curve 的 genuine non-`3` inert singular bad-reduction audit：除边界外只有一个巨大素数的 singular point，而它不能提升到 `p^2`。因此 omega-content common channel不存在 surviving singular Hensel tree，只剩 simple moving decimal orbit。本文不排除所有 simple content roots，也不宣称 A2 closure。

---

## 1. concatenated content

沿用 reflection endpoint：

\[
N=10^M,
\quad T=10^m,
\quad A=a_2,
\quad B=b_2,
\]

\[
Q=B+2N,
\qquad
K=9N+10A.
\]

原拼接 numerator / denominator为

\[
\boxed{
\alpha=TK+a_3=\omega W_q,
}
\tag{1.1}
\]

\[
\boxed{
\beta=TQ+b_3=\omega S,
}
\tag{1.2}
\]

其中

\[
\gcd(W_q,S)=1.
\]

因此

\[
\boxed{\omega=\gcd(\alpha,\beta).}
\tag{1.3}
\]

对本文关心的 odd inert prime `p|omega`，`T` 为 unit。

---

## 2. angle content gate 是 `A_-` 的原始整数代表

定义

\[
\mathcal U_\Omega
=(45B^2-2AN)^2-A^2B(99B-4N),
\]

以及 angle raw carrier

\[
\mathcal O_+
=T\mathcal U_\Omega+2A^2Qb_3.
\]

定义

\[
\boxed{
\mathcal C_\omega
:=\mathcal U_\Omega-2A^2Q^2.
}
\tag{2.1}
\]

由 `beta=TQ+b3`：

\[
\boxed{
\mathcal O_+
=T\mathcal C_\omega
+2A^2Q\beta.
}
\tag{2.2}
\]

所以若

\[
p^e\mid\omega,
\]
则

\[
\boxed{
\min\{v_p(\widehat{\mathcal O}_{\rm sp}),e\}
=
\min\{v_p(\mathcal C_\omega),e\}.
}
\tag{2.3}
\]

使用 normalized variables

\[
x=B/N,
\qquad y=10A/N,
\]
有

\[
\boxed{
\mathcal C_\omega
=\frac{N^4}{100}A_-(x,y),
}
\tag{2.4}
\]

其中

\[
\boxed{
A_-(x,y)
=202500x^4-(101x^2+4x+4)y^2-1800x^2y.
}
\tag{2.5}
\]

这正是 `spontaneous-prefix-branch-audit.md` 识别的 common-`alpha` collision locus。

真实 endpoint已有

\[
A_-<0,
\]
故

\[
\boxed{\mathcal C_\omega<0.}
\tag{2.6}
\]

---

## 3. `C_omega` 的 2-adic orientation

`spontaneous-angle-parity.md` 已证明

\[
v_2(\mathcal U_\Omega)=2M+2,
\qquad
\frac{\mathcal U_\Omega}{2^{2M+2}}\equiv1\pmod4.
\]

另一方面

\[
Q=2^{M+1}Q_0,
\qquad A,Q_0\text{ odd},
\]
所以

\[
v_2(2A^2Q^2)=2M+3.
\]

因此

\[
\boxed{
v_2(\mathcal C_\omega)=2M+2,
}
\tag{3.1}
\]

且

\[
\boxed{
\frac{\mathcal C_\omega}{2^{2M+2}}
\equiv1-2\equiv3\pmod4.
}
\tag{3.2}
\]

结合 `C_omega<0`：

\[
\boxed{
-\frac{\mathcal C_\omega}{2^{2M+2}}>0,
\qquad
-\frac{\mathcal C_\omega}{2^{2M+2}}\equiv1\pmod4.
}
\tag{3.3}
\]

所以 common-`alpha` angle gate作为**正的绝对自然代表**本身具有 even total inert parity；这和 additive content gate的 `3 mod4` orientation不同。

---

## 4. additive content gate正是 `J_H`

`spontaneous-height-parity-ledger.md` 定义

\[
\boxed{
\mathcal J_H
=B^2(5K^2-36K+55)-Q^2N_0
}
\tag{4.1}
\]

并证明

\[
\boxed{
\Theta_{\rm dec}
=T\mathcal J_H
-2B^2(2K-9)\alpha.
}
\tag{4.2}
\]

由 `alpha=omega Wq`，对 `p^e|omega`：

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),e\}
=
\min\{v_p(\mathcal J_H),e\}.
}
\tag{4.3}
\]

已有

\[
\boxed{
\widehat{\mathcal J}_H
:=\frac{\mathcal J_H}{2^{2M+2}}>0,
\qquad
\widehat{\mathcal J}_H\equiv3\pmod4.
}
\tag{4.4}

所以 omega-supported angle/additive common prime完全由

\[
\boxed{
\omega,
\qquad
\mathcal C_\omega,
\qquad
\mathcal J_H
}
\tag{4.5}
\]
读取；third block已消失。

---

## 5. omega-content 与 source discriminant / denominator 自动分离

`source-discriminant.md` 给 source triangle

\[
z=g\omega-c_u,
\qquad
f=g\omega+c_u,
\]

以及

\[
\mathscr D_W=55z^2-49c_u^2.
\]

旧本原性有

\[
\gcd(\omega,c_u)=1.
\]

若 genuine non-`3` inert prime `p|omega`，则

\[
z\equiv-c_u\pmod p,
\qquad
f\equiv c_u\pmod p.
\]

故

\[
\boxed{p\nmid qf c_u.}
\tag{5.1}
\]

同时

\[
\boxed{
\mathscr D_W
\equiv(55-49)c_u^2
=6c_u^2\not\equiv0\pmod p.
}
\tag{5.2}
\]

所以 omega-content 与 denominator saturation、source-discriminant double-root 均严格分离。它是 common-`alpha` content，不应混入 pure spontaneous external discriminant-zero channel。

---

## 6. normalized common-content curve

定义

\[
\boxed{F(x,y):=A_-(x,y).}
\tag{6.1}
\]

把 `J_H` 除去正的 decimal scale后，定义

\[
\boxed{
\begin{aligned}
G(x,y,\tau)
:={}&100x^2\left[5(y+9)^2-36(y+9)\tau+55\tau^2\right]\\
&-(x+2)^2(2025x^2+y^2).
\end{aligned}}
\tag{6.2}
\]

其中

\[
\tau=10^{-M}.
\]

于是 genuine omega-supported angle/additive common first layer必须落在

\[
\boxed{F=G=0.}
\tag{6.3}
\]

这是一条一维 moving curve；本文接下来审计其 singular bad reduction。

---

# singular audit I: `F` 本身奇异

## 7. rank-drop 的第一种机制

因为

\[
F_\tau=0,
\]
若 `G_tau` 为 unit，而系统 Jacobian rank小于 `2`，就必须有

\[
F_x=F_y=0.
\]

直接 elimination：

\[
\boxed{
\operatorname{Res}_y(F,F_y)
=810000x^4
(101x^2+4x+4)(101x^2+4x+8).
}
\tag{7.1}
\]

另有

\[
\boxed{
\begin{aligned}
\operatorname{Res}_y(F,F_x)
={}&164025000000x^6\\
&\cdot(10201x^4+1212x^3+1652x^2+128x+128).
\end{aligned}}
\tag{7.2}
\]

排除 `x=0` 后，两个 x-polynomial 的 resultant为

\[
\boxed{
2^{22}3^25^2\cdot17\cdot37\cdot67^2\cdot101^4.
}
\tag{7.3}
\]

所以 genuine non-`3` inert prime中唯一候选是

\[
\boxed{p=67.}
\]

完整有限域审计却给：模 `67` 的所有 full-system singular states都满足

\[
\boxed{x=y=0,}
\]

而 `tau` 任意。这是 prefix boundary，不是 genuine omega-content state。

故第一种 singular mechanism为空。

---

# singular audit II: repeated decimal root

## 8. `G_tau=0` 等价于一个固定 repeated-`tau` center

把 `G` 看成 `tau` 的二次式：

\[
G
=5500x^2\tau^2
-3600x^2(y+9)\tau+\cdots.
\]

对 `p\nmid2\cdot5\cdot11\cdot x`：

\[
\boxed{
G_\tau=0
\iff
55\tau=18(y+9).
}
\tag{8.1}
\]

其 discriminant精确为

\[
\boxed{
\operatorname{Disc}_\tau(G)
=2000x^2D_\omega(x,y),
}
\tag{8.2}
\]

其中

\[
\boxed{
\begin{aligned}
D_\omega={}&22275x^4+89100x^3
+991x^2y^2+17640x^2y\\
&+168480x^2+44xy^2+44y^2.
\end{aligned}}
\tag{8.3}
\]

所以 repeated-`tau` branch必须满足

\[
F=D_\omega=0.
\]

消去 `y`：

\[
\boxed{
\operatorname{Res}_y(F,D_\omega)
=164025x^4\mathcal Q_\omega(x),
}
\tag{8.4}
\]

其中

\[
\boxed{
\begin{aligned}
\mathcal Q_\omega(x)={}&
251056113025x^8+44533768400x^7+67275876360x^6\\
&+8529261920x^5+6336428816x^4+503628928x^3\\
&+239152384x^2+8466432x+2768896.
\end{aligned}}
\tag{8.5}
\]

所有系数均为正，所以

\[
\boxed{\mathcal Q_\omega(x)>0\quad(x>0).}
\tag{8.6}
\]

因此真实 endpoint没有 repeated-`tau` Archimedean root；只可能发生 p-adic wrapping。

---

## 9. fixed bad primes of the repeated-`tau` intersection

`Q_omega` 的整数判别式因子分解为

\[
\boxed{
\begin{aligned}
\operatorname{Disc}(\mathcal Q_\omega)
={}&2^{120}3^{11}5^{26}7^{12}11^4 13^4 23^2 101^8\\
&\cdot557\cdot4357^2\cdot7596456621900959.
\end{aligned}}
\tag{9.1}
\]

其中最后的大因子为素数。限制到 non-`3` inert prime，候选为

\[
\boxed{
7,\ 11,\ 23,\ 7596456621900959.
}
\tag{9.2}
\]

对 `7,11,23`，完整 `(F,G)` singular-state枚举都只得到

\[
x=y=0
\]
边界，没有 genuine finite state。

剩下

\[
\boxed{p=7596456621900959}
\tag{9.3}
\]
有唯一 genuine finite singular state：

\[
\boxed{
x_0=596722596594438,}
\tag{9.4}
\]

\[
\boxed{
y_0=7182062884214340,}
\tag{9.5}
\]

\[
\boxed{
\tau_0=7460836853203523
\pmod p.
}
\tag{9.6}
\]

---

## 10. 巨大 singular prime不能提升到 `p^2`

在 (9.4)--(9.6) 的标准 `[0,p)` representatives上写

\[
x=x_0+pX,
\qquad
y=y_0+pY,
\qquad
\tau=\tau_0+pT_1.
\]

把 `F=G=0 mod p^2` 线性化。两行 Jacobian模 `p` 分别为

\[
\boxed{
(3088566246132647,\ 763538860035101,\ 0),
}
\tag{10.1}
\]

\[
\boxed{
(5543473436650293,\ 7013503068586219,\ 0).
}
\tag{10.2}
\]

第二行是第一行的

\[
\boxed{2399356256055466}
\tag{10.3}
\]
倍。

而常数 carry为

\[
\boxed{
F(x_0,y_0)/p
\equiv7136724306802588\pmod p,
}
\tag{10.4}
\]

\[
\boxed{
G(x_0,y_0,\tau_0)/p
\equiv6411661286654023\pmod p.
}
\tag{10.5}
\]

compatibility residual为

\[
\boxed{
6411661286654023
-2399356256055466\cdot7136724306802588
\equiv4160590904825983\not\equiv0\pmod p.
}
\tag{10.6}
\]

因此 augmented linear system不相容：

\[
\boxed{
\text{该唯一 genuine singular state 没有 }p^2\text{ lift}.}
\tag{10.7}

---

## 11. omega-content common channel 的最终局部分类

综合 §§7--10：

\[
\boxed{
\text{genuine non-`3` inert omega-content angle/additive common curve}
}
\]

没有 surviving singular Hensel tree。

所有真正可能继续到任意深度的 omega-content state都必须位于

\[
\boxed{F=A_-=0,\qquad G=J=0}
\]
的 **simple moving branches** 上。

这和此前 source / denominator / height pool 的审计结果一致：A2 的局部 singular mechanisms基本都已被剥掉；剩余困难是 simple decimal-orbit / natural-representative synchronization与 global parity allocation。

---

## 12. 对 `G_sp` parity 的意义

omega-content 对 global common gcd 的贡献现在具有明确 ledger：

- angle content由 negative `C_omega` 读取，取绝对 primitive后是 `1 mod4`；
- additive content由 positive `J_H` 读取，primitive为 `3 mod4`；
- content prime与 denominator / source-discriminant double-root分离；
- angle/additive 同时 content contact只剩 simple moving curve。

所以后续不能再把 common-`alpha` content当成未命名的第四种奇异 supplier。若 `G_sp=1 mod4` 分支仍需要两份独立 residual inert parity，omega-content只能通过这条已完全正规化的 simple curve参与；它不再提供额外 singular branching。

A2 仍保持 open。
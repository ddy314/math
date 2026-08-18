# A2 fixed `23` `eta=2` `c=2` 的 deterministic reconstruction certificate

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`、`spontaneous-cq-fixed23-eta2-c2-full-a3-crt.md`、`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md`、`spontaneous-cq-global-coupling.md`。
>
> **严格状态：**前面的工作已把唯一 type `(d,c_Q,k_h,slot)=(1,1587,1,+)` 压成 source divisor `theta` 与 full canonical `a_3` CRT representative。本文记录通过该 representative 后的完整确定性恢复链：`g,b_3,a_3` 固定后，`a_2,b_2,C,X,Y,q,omega` 全部由精确整数公式唯一确定，最后可直接计算 fixed-`23` common depth。于是未来的有限 certificate / agent search只需产生 source divisor `theta`；任何 candidate均可在无进一步枚举的情况下完成全链审计。

---

## 1. certificate input

固定

\[
\boxed{
\lambda\equiv8\pmod{11},
\qquad
c_u,
\qquad
\theta,
\qquad
\iota,
\qquad
c_-c_+=1587.}
\tag{1.1}

其中：

- `c_u` 满足 source-content real window，并且每个素因子 `=1 mod4`；
- `theta` 为
  \[
  S:=5^{3\lambda}+1587c_u
  \]
  的正奇因子；
- centered slot
  \[
  \frac{39}{2}L_*<\theta<\frac{79}{4}L_*,
  \qquad
  L_*=2^{\lambda+1}5^\lambda c_u;
  \]
- `iota` 是 `i^2=-1 mod5^(lambda-1)` 的两种 Gaussian orientation之一；
- `(c_-,c_+)` 属于
  \[
  (1,1587),(3,529),(529,3),(1587,1).
  \]

fixed `23` orientation已知时，只保留相应的两个 allocation。

---

## 2. source variables全部恢复

定义

\[
M:=2\lambda,
\qquad
m:=\lambda+1,
\qquad
T:=10^m,
\qquad
N:=10^M.
\tag{2.1}

由 source product：

\[
\boxed{
g=\frac{5^{3\lambda}+1587c_u}{\theta}.}
\tag{2.2}

真实 third denominator：

\[
\boxed{
b_3
=2^{3\lambda+2}\cdot5\cdot1587c_u.}
\tag{2.3}

并有

\[
\boxed{D=\frac{gT}{5^\lambda}=5\cdot2^m g.}
\tag{2.4}

Hensel quotient由

\[
\boxed{
\omega=\frac{\theta+L_*}{1587}}
\tag{2.5}

唯一恢复。真实 candidate必须使右边为整数。

---

## 3. `a_3` 由 full canonical CRT唯一恢复

前述 three-way CRT使用模数

\[
2^m,
\qquad
5^{\lambda-1},
\qquad
1587.
\]

其 full modulus为

\[
\mathfrak M_3^\sharp
=1587\frac T{25}.
\]

固定 `(lambda,c_u,theta,iota,c_-,c_+)` 后得到 shifted representative

\[
H_{3,\sharp}
\in[0,\mathfrak M_3^\sharp).
\]

只有

\[
\boxed{
0<H_{3,\sharp}<\frac T{250}}
\tag{3.1}

才可能进入真实 third-numerator digit window；若成立，则

\[
\boxed{a_3=T+H_{3,\sharp}.}
\tag{3.2}

所以 `a_3` 不再存在第二个 integer choice。

---

## 4. high-2 equality唯一恢复 `a_2`

当前 high-2 equality为

\[
H_0+Y_2=\frac{g^2}{2},
\qquad
Y_2=5c_Qa_2,
\qquad c_Q=1587.
\tag{4.1}

另一方面 pure third-block Gaussian norm已证明

\[
(g-2a_3)^2+81b_3^2
=4(H_0-ga_3).
\tag{4.2}

消去 `H_0`：

\[
\boxed{
a_2
=\frac{g^2-4a_3^2-81b_3^2}{20\cdot1587}.}
\tag{4.3}

因此 candidate首先必须满足 numerator被 `20*1587` 整除，并且

\[
\boxed{
\frac{249}{250}10^{M-1}<a_2<10^{M-1}.}
\tag{4.4}

---

## 5. `b_2,q,z,f` 全部恢复

reflection denominator formula给

\[
\boxed{
b_2=2^{M+m+1}c_ug.}
\tag{5.1}

危险 endpoint要求

\[
\boxed{
\frac1{10}10^M<b_2<\frac2{19}10^M.}
\tag{5.2}

令

\[
Q:=b_2+2N.
\]
则

\[
\boxed{
q=\frac{Q}{2^{M+1}1587}.}
\tag{5.3}

必须为正整数且

\[
23\nmid q.
\]

然后

\[
\boxed{z=q5^\lambda,}
\qquad
\boxed{f=z+2c_u.}
\tag{5.4}

source triangle的最终 exact audit为

\[
\boxed{g\omega=z+c_u.}
\tag{5.5}

---

## 6. finite defect `C` 无搜索恢复

定义

\[
\mathcal N_*:=(g-2a_3)^2+81b_3^2.
\]

pure third-block norm给

\[
\boxed{
C
=\frac{3gT-\mathcal N_*/4}{5^\lambda}.}
\tag{6.1}

candidate必须满足：

\[
C\in\mathbb Z,
\]

\[
\boxed{0<C<\frac{3D}{250}.}
\tag{6.2}

并且

\[
\boxed{\gcd(C,D)=1.}
\tag{6.3}

因此 `C` 同样不再需要 CRT 搜索；full `a_3` representative一旦通过，`C` 是确定值。

---

## 7. canonical `X,Y` 也唯一恢复

finite-defect relation

\[
c_-^2X=3D-C
\]
直接给

\[
\boxed{X=\frac{3D-C}{c_-^2}.}
\tag{7.1}

必须为正整数。

令

\[
\boxed{
H_0:=\frac{g^2}{2}-5\cdot1587a_2.}
\tag{7.2}

则另一 canonical factor

\[
H_0+ga_3=c_+^2Y
\]
给

\[
\boxed{
Y=\frac{H_0+ga_3}{c_+^2}.}
\tag{7.3}

也必须为正整数。

同时做 exact consistency audit：

\[
\boxed{H_0-ga_3=5^\lambda c_-^2X,}
\tag{7.4-}

\[
\boxed{H_0+ga_3=c_+^2Y.}
\tag{7.4+}

以及

\[
N_0:=\left(\frac{9b_2}{2}\right)^2+a_2^2,
\]

\[
\boxed{N_0=5^{\lambda-2}XY.}
\tag{7.5}

---

## 8. primitive audits

真实 endpoint还要求至少：

\[
\boxed{\gcd(a_2,b_2)=1,}
\tag{8.1}

\[
\boxed{\gcd(a_3,b_3)=1.}
\tag{8.2}

以及 source/canonical separations

\[
\gcd(g,c_u)=1,
\qquad
\gcd(g,1587)=1,
\qquad
\gcd(XY,1587)=1.
\tag{8.3}

这些都是 candidate恢复后的普通整数 gcd 检查。

---

## 9. fixed `23` common depth直接读取

定义

\[
K:=9N+10a_2,
\]

\[
D_{\rm pref}
:=2025b_2^2+81N^2-K^2.
\tag{9.1}

再定义

\[
A_K:=K^2-18K+55,
\qquad
E_K:=K(2K-9),
\]

\[
\mathcal G_+
:=fA_K+2c_uE_K,
\]

\[
\mathcal G_-
:=zA_K-2c_uE_K.
\tag{9.2}

若 `23^2|c_+`，选 `G_+`；若 `23^2|c_-`，选 `G_-`。当前 cap 为

\[
2v_{23}(c_Q)=4.
\]

所以 actual pure-`c_Q` common depth为

\[
\boxed{
 d_{23}
=\min\left(
 v_{23}(D_{\rm pref}),
 v_{23}(\mathcal G_\sigma),
 4
\right).}
\tag{9.3}

这允许 finite certificate直接给每个 surviving arithmetic candidate标注 odd/even depth，无需再回到 Hensel chart。

---

## 10. deterministic certificate 的意义

从 `(lambda,c_u,theta,iota,c_-,c_+)` 开始，整个剩余 endpoint现在只有以下一种流程：

\[
\theta
\to g,b_3
\to a_3\text{ (full CRT)}
\to a_2,b_2,C,X,Y,q,\omega
\to d_{23}.
\]

每个箭头都是单值的 exact integer formula。

因此后续任何 finite search都不应重新枚举 `a_2,a_3,b_2,b_3,C,X,Y`。真正的搜索变量只剩 source divisor `theta`、两种 Gaussian orientation和 fixed `23` orientation下至多两个 `3`-allocations。
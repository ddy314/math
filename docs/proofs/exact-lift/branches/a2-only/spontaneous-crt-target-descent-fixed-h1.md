# A2 fixed `31/179`, baseline `h=1` 的 target/descent 低层压缩

> **依赖：** `spontaneous-crt-target-descent-overlap.md`、`spontaneous-crt-target-descent-depth-squeeze.md`、`spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-equal-depth-decimal-pair.md`。
>
> **严格状态：**此前 equal-depth target 与 height-descent overlap 已只剩 fixed `p=31,179`；对 `h>=2` 已证明两个 descended carriers 都只能保留一层。本文处理剩余的 `h=1`。先把 source ratio `d=D/N` 与 target root `K` 在模 `p^2` 展开；deep resonance `p^2|R_+` 给一条线性 digit relation，而 `p^2|Dhat_63` 再给第二条。两式联立后，每个 fixed prime 都只剩唯一一个模 `p^2` collision state。进一步利用 full resonance `rho_p>=1` 的 projective unit relation，可把 `p^3|Dhat_63` 再压成唯一一条 affine next-digit line。本文尚未排除这两条 third-layer lines，因此不关闭 A2。

---

## 1. low-baseline setting

固定

\[
p\in\{31,179\},
\qquad h=v_p(P)=v_p(U)=1,
\]

其中

\[
P(K):=6K^2-36K+55,
\qquad
U:=DK-N=qW_q.
\]

此前 target/descent overlap 已证明 first-layer root 唯一为

\[
\boxed{
(p,K_0)=(31,9),\qquad(179,71).}
\tag{1.1}
\]

因为 `p∤N`，在 `Z_p` 中定义

\[
\boxed{d:=D/N.}
\tag{1.2}
\]

由 `p|U`：

\[
dK\equiv1\pmod p.
\]

所以 first source roots 为

\[
\boxed{
(p,d_0)=(31,7),\qquad(179,58).}
\tag{1.3}
\]

写

\[
K=K_0+pk,
\qquad
d=d_0+p\ell
\qquad(k,\ell\in\mathbf F_p).
\tag{1.4}
\]

并记

\[
u_0:=\frac{dK-1}{p}\pmod p,
\qquad
P_0:=\frac{P(K)}p\pmod p.
\tag{1.5}
\]

当前 exact `h=1` 要求

\[
P_0u_0\ne0.
\tag{1.6}
\]

---

## 2. deep resonance 的第一条 digit line

由

\[
R_+=DP-KU
\]
除以 `N`：

\[
\frac{R_+}{N}=dP-K(dK-1).
\tag{2.1}
\]

真正 deep target 满足 `rho_p>=1`，所以

\[
\boxed{p^2\mid R_+.}
\tag{2.2}
\]

除以 `pN` 并模 `p`：

\[
\boxed{d_0P_0-K_0u_0\equiv0\pmod p.}
\tag{2.3}
\]

### 2.1 `p=31`

直接展开：

\[
\boxed{P_0\equiv7+10k,}
\tag{2.4}
\]

\[
\boxed{u_0\equiv2+7k+9\ell.}
\tag{2.5}
\]

代入 (2.3)：

\[
7k+12\ell\equiv0\pmod{31},
\]
所以

\[
\boxed{\ell\equiv2k\pmod{31}.}
\tag{2.6}
\]

### 2.2 `p=179`

对应展开为

\[
\boxed{P_0\equiv155+100k,}
\tag{2.7}
\]

\[
\boxed{u_0\equiv23+58k+71\ell.}
\tag{2.8}
\]

(2.3) 化为

\[
18+71k+150\ell\equiv0\pmod{179},
\]
即

\[
\boxed{\ell\equiv50+58k\pmod{179}.}
\tag{2.9}
\]

所以仅 deep target 本身仍各留 `p-1` 个 exact-`h=1` digit classes；下面的 descended quotient 会把它们压成一个。

---

## 3. descended quotient 的 exact source form

沿用

\[
\widehat{\mathscr D}_{63}=c_u^2\mathscr F_{63},
\]

以及 exact identity

\[
16\mathscr F_{63}
=3gT G_D(K)
-16(2K-9)(g\alpha+H_0),
\tag{3.1}
\]

其中

\[
\boxed{G_D(K):=11K^2-240K+432.}
\tag{3.2}
\]

在 `h=1` 中写

\[
\omega=p\omega_0,
\qquad
U=qW_q.
\]

source triangle 给

\[
g\omega=q5^\lambda+c_u.
\tag{3.3}
\]

因此

\[
\begin{aligned}
g\alpha+H_0
&=(g\omega+c_u)W_q\\
&=(2g\omega-q5^\lambda)\frac Uq.
\end{aligned}
\]

令

\[
t:=\frac{g\omega_0}{q}\in\mathbf Z_p,
\]
则有 exact identity

\[
\boxed{
g\alpha+H_0=(2pt-5^\lambda)U.}
\tag{3.4}
\]

又因

\[
gT=D5^\lambda,
\]
将 (3.4) 代入 (3.1)：

\[
\boxed{
16\mathscr F_{63}
=5^\lambda\bigl[3DG_D+16(2K-9)U\bigr]
-32p(2K-9)tU.}
\tag{3.5}
\]

除去 `N` 并使用 `D=dN,U=N(dK-1)`：

\[
\boxed{
\frac{16\mathscr F_{63}}N
=5^\lambda A
-32p(2K-9)t(dK-1),}
\tag{3.6}
\]

其中

\[
\boxed{
A:=3dG_D+16(2K-9)(dK-1).}
\tag{3.7}
\]

first target layer使 `p|G_D` 且 `p|(dK-1)`。所以第二项自动含 `p^2`，从而

\[
\boxed{
p^2\mid\widehat{\mathscr D}_{63}
\iff
\frac Ap\equiv0\pmod p.}
\tag{3.8}
\]

等价地

\[
\boxed{
3d_0\frac{G_D(K)}p
+16(2K_0-9)u_0
\equiv0\pmod p.}
\tag{3.9}
\]

这里 `c_u,N,5^lambda` 全为 p-units，所以没有隐藏零因子。

---

## 4. `p=31`: second layer 只有 `K=9, d=7 mod31^2`

在 `K=9+31k` 下：

\[
\boxed{
\frac{G_D(K)}{31}
\equiv4+20k\pmod{31}.}
\tag{4.1}
\]

将 deep line `ell=2k` 代入 (3.9)，所有常数项消掉，只剩

\[
\boxed{21k\equiv0\pmod{31}.}
\tag{4.2}
\]

因此

\[
\boxed{k\equiv0,\qquad\ell\equiv0\pmod{31}.}
\tag{4.3}
\]

也就是

\[
\boxed{
K\equiv9\pmod{31^2},
\qquad
\frac DN\equiv7\pmod{31^2}.}
\tag{4.4}
\]

该 state 确实仍是 exact `h=1`：

\[
\boxed{
P/31\equiv7,
\qquad
U/(31N)\equiv2
\pmod{31}.}
\tag{4.5}
\]

并且 source-prefix reader 保持 exact baseline：

\[
\boxed{
\frac{R_{PD}}{31N^2}\equiv17\pmod{31}.}
\tag{4.6}
\]

所以这不是 baseline 被偷偷提升到 `h>=2` 的假状态。

---

## 5. `p=179`: second layer 也只有一个 state

在 `K=71+179k` 下：

\[
\boxed{
\frac{G_D(K)}{179}
\equiv38+69k\pmod{179}.}
\tag{5.1}
\]

将 deep line

\[
\ell\equiv50+58k
\]
代入 (3.9)，得到

\[
\boxed{129+86k\equiv0\pmod{179}.}
\tag{5.2}
\]

唯一解为

\[
\boxed{k\equiv88\pmod{179}.}
\tag{5.3}
\]

进而

\[
\boxed{\ell\equiv142\pmod{179}.}
\tag{5.4}
\]

所以唯一 second-layer collision 为

\[
\boxed{
K\equiv15823\pmod{179^2},
\qquad
\frac DN\equiv25476\pmod{179^2}.}
\tag{5.5}
\]

同样 exact baseline 没有提升：

\[
\boxed{
P/179\equiv5,
\qquad
U/(179N)\equiv173
\pmod{179},}
\tag{5.6}
\]

\[
\boxed{
\frac{R_{PD}}{179N^2}\equiv68\pmod{179}.}
\tag{5.7}
\]

---

## 6. second-layer compression theorem

综合 §§2–5：

\[
\boxed{
\begin{array}{c|c|c}
p&K\pmod{p^2}&D/N\pmod{p^2}\\ \hline
31&9&7\\
179&15823&25476
\end{array}}
\tag{6.1}
\]

是 fixed `31/179,h=1` deep target 中使

\[
p^2\mid\widehat{\mathscr D}_{63}
\]
成为可能的全部 states。

fully primitive descent为

\[
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.
\]

而 `h=1` target 已有

\[
p^2\mid\widehat{\mathcal T}_2.
\]

所有 prefactors 对 `31,179` 都是 units，所以

\[
\boxed{
p^2\mid\widehat{\mathscr D}_{63}
\iff
p^2\mid\mathscr R_{63}^\star.}
\tag{6.2}
\]

因此 (6.1) 同时也是两个 descended carriers 的完整 second-layer collision table。

---

## 7. full resonance 把 third layer 再压成一条 affine line

现在固定 (6.1) 的 unique second-layer state，并写

\[
K=K_2+p^2\kappa,
\qquad
d=d_2+p^2\mu.
\tag{7.1}
\]

令

\[
u_1:=\frac{dK-1}{p}\pmod p.
\]

full equal-depth resonance `rho_p>=1` 来自

\[
L_{JB}=2Dg\omega K-fqW_q,
\qquad p^2\mid?\text{ no; }v_p(L_{JB})\ge2.
\]

除去一层 `p` 并用

\[
f=g\omega+c_u\equiv-q5^\lambda\pmod p
\]
得到

\[
\boxed{2dK\,t+5^\lambda u_1\equiv0\pmod p.}
\tag{7.2}
\]

而 `dK≡1 mod p`，所以

\[
\boxed{t\equiv-\frac{5^\lambda}{2}u_1\pmod p.}
\tag{7.3}
\]

在 unique second-layer state中 `p^2|A`。将 (3.6) 除以 `p^2` 并模 `p`，再代入 (7.3)，得到完全不含 `t` 的 third-layer criterion：

\[
\boxed{
p^3\mid\widehat{\mathscr D}_{63}
\iff
\frac{A}{p^2}
+16(2K_0-9)u_1^2
\equiv0\pmod p.}
\tag{7.4}
\]

直接展开 (7.4)：

### `p=31`

\[
K=9+31^2\kappa,
\qquad d=7+31^2\mu,
\]
给

\[
\boxed{9+2\kappa+25\mu\equiv0\pmod{31},}
\tag{7.5}
\]
即

\[
\boxed{\mu\equiv17+21\kappa\pmod{31}.}
\tag{7.6}
\]

### `p=179`

\[
K=15823+179^2\kappa,
\qquad d=25476+179^2\mu,
\]
给

\[
\boxed{20+106\kappa+12\mu\equiv0\pmod{179},}
\tag{7.7}
\]
即

\[
\boxed{\mu\equiv58+21\kappa\pmod{179}.}
\tag{7.8}

所以 second layer 的单点并不会重新炸成 `p^2` 个 third-digit states；每个 fixed prime只剩一条 `p` 点 affine line。

---

## 8. current fixed-`31/179` frontier

当前 target/descent reuse 的 low-baseline局部结构已经压成：

\[
\boxed{
\begin{array}{c|c|c}
p&\text{second layer}&\text{third layer}\\ \hline
31&(K,d)=(9,7)\bmod31^2
&\mu=17+21\kappa\bmod31\\
179&(K,d)=(15823,25476)\bmod179^2
&\mu=58+21\kappa\bmod179
\end{array}}
\tag{8.1}
\]

同时两 second-layer states都满足：

\[
v_p(P)=v_p(U)=v_p(R_{PD})=1.
\]

所以没有 hidden baseline lift，也没有 source-prefix exceptional branch。

这已经删除了 fixed `31/179,h=1` 的大部分 next-digit自由，但尚未证明 affine third-layer line为空。下一步应把 (7.6)/(7.8) 与 `H_pref/J_H` 的 oversaturation second digit或 `Lambda_tail` 的 exact tail digit联立；继续只升 `K,d` 自身不会自动产生矛盾。

A2 仍为 `待证`。

# A2 fixed `23` `eta=2` `c=2` 的 source divisor `theta mod 23^3` filter

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-blowup-nogo.md`、`spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`、`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md`。
>
> **严格状态：**对 `v_23(c_Q)=2` 的 second-layer surviving classes，additive Möbius chart固定 `rho=z/c_u mod23`，而 source split固定 `g mod23`。本文把二者送回 exact identity `theta=c_Q omega-L_*`，得到 orientation-specific 的 `theta mod23^3` residue。于是 source divisor certificate 可在窄实区间之外再施加一个 `23^3` congruence。本文给出最初 source states 的显式 residue 表，但不声称这一个固定模数单独关闭无界 family。

---

## 1. notation

固定

\[
p:=23,
\qquad
c_Q=3p^2=1587,
\]

\[
M=2\lambda,
\qquad
m=\lambda+1,
\]

\[
L_*:=2^m5^\lambda c_u
=2^{\lambda+1}5^\lambda c_u.
\tag{1.1}

source ratio记

\[
\rho:=\frac z{c_u}.
\]

source triangle与 Hensel relation 为

\[
g\omega=z+c_u=c_u(\rho+1),
\tag{1.2}

\[
\boxed{
\theta=c_Q\omega-L_*
=3p^2\omega-L_*.}
\tag{1.3}

本文只处理 fixed `23` common depth已进入第二层的 genuine class；因此 `kappa notin {11,18}`，orientation-resolved additive chart给合法 unit `rho mod p`。

---

## 2. source split 固定 `g mod23`

reflection source split为

\[
\boxed{
c_Qq
=5^M+2^mgc_u.}
\tag{2.1}

左边被 `p^2` 整除。降模 `p` 已足够得到

\[
5^{2\lambda}
+2^{\lambda+1}gc_u
\equiv0\pmod p.
\]
因为 `2,5,c_u` 都是 `p`-进 units：

\[
\boxed{
g_0
\equiv
-5^{2\lambda}
(2^{\lambda+1}c_u)^{-1}
\pmod p.}
\tag{2.2}

所以 fixed `(lambda,c_u)` 已唯一固定 `g mod23`。

---

## 3. additive orientation 固定 `omega mod23`

second-layer additive charts为

\[
\boxed{
\rho_+(\kappa)
=-\frac{11}{1+14\kappa},}
\tag{3.1+}

\[
\boxed{
\rho_-(\kappa)
=\frac{9+18\kappa}{1+14\kappa}.}
\tag{3.1-}

其中 `+` 对应 canonical `c_+` orientation，`-` 对应 `c_-` orientation。

由 (1.2) 模 `p`：

\[
g_0\omega
\equiv c_u(\rho_\sigma+1)
\pmod p.
\]
故

\[
\boxed{
\omega_{0,\sigma}
\equiv
c_u(\rho_\sigma+1)g_0^{-1}
\pmod p.}
\tag{3.2}

将 (2.2) 的逆元显式代回，还可写成

\[
\boxed{
\omega_{0,\sigma}
\equiv
-2^{\lambda+1}c_u^2
(\rho_\sigma+1)
5^{-2\lambda}
\pmod p.}
\tag{3.3}

---

## 4. `theta` 自动提升到 `mod23^3`

由 exact (1.3)：

\[
\theta+L_*=3p^2\omega.
\]
要读取 `theta mod p^3`，右边只需要 `omega mod p`。因此 (3.2) 直接给

\[
\boxed{
\theta
\equiv
-L_*+3p^2\omega_{0,\sigma}
\pmod{p^3}.}
\tag{4.1}

也就是

\[
\boxed{
\theta
\equiv
-L_*
-3p^2\,2^{\lambda+1}c_u^2
(\rho_\sigma+1)5^{-2\lambda}
\pmod{p^3}.}
\tag{4.2}

这个 residue 已完全由

\[
(\lambda,c_u,\sigma)
\]
决定；`g,omega,q,a_3` 都已经消失。

若 `rho=-1`，则 `omega_0=0`，(4.1)退化成

\[
\theta\equiv-L_*\pmod{p^3},
\]
正好对应旧 simultaneous-gate class `p|omega`。

---

## 5. 与 source divisor certificate 合并

`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md` 已把 divisor window收紧为

\[
\frac{39}{2}L_*<\theta<\frac{79}{4}L_*.
\tag{5.1}

因此任何 second-layer surviving source divisor现在必须同时满足

\[
\boxed{
\begin{aligned}
&\theta\mid\mathscr S_\lambda(c_u),\\
&\theta\text{ odd},\\
&\frac{39}{2}L_*<\theta<\frac{79}{4}L_*,\\
&\theta\equiv\Theta_{\lambda,c_u,\sigma}\pmod{23^3},
\end{aligned}}
\tag{5.2}

其中 `Theta` 由 (4.1)/(4.2) 显式给出。

这比只用 `theta+L_* divisible c_Q=3*23^2` 多一层：旧 integrality只给 `theta=-L_* mod23^2`；当前 additive/source synchronization进一步固定 quotient `omega mod23`，从而升级到 `23^3`。

---

## 6. first source states 的 residue 表

使用 source-content proof 的

\[
(\lambda,c_u)
=(52,29),
(63,337),
(74,3917),
(74,3929)
\]
以及 fixed-23 blow-up 的 `kappa/rho` chart，可 exact 计算：

\[
\boxed{
\begin{array}{c|c|c|c}
\lambda&c_u&c_+\text{ orientation}&c_-\text{ orientation}\\ \hline
52&29&2713&6945\\
63&337&9053&3763\\
74&3917&731&202\\
74&3929&5444&10734
\end{array}
\quad(\bmod\ 23^3).}
\tag{6.1}

这些 `lambda` 对应的 `M=104,126,148` 都属于 c=2 second-layer surviving classes，因此两种 orientation chart均 genuine。

---

## 7. proof boundary

`23^3` 仍是 fixed modulus，所以本文不把它单独视为无界 closure。它的用途是强化 source-only finite certificate：

1. source window先给有限 `c_u`；
2. centered slot只查 `1.28%` 宽的 divisor interval；
3. (5.2) 再只保留一个 `23^3` residue class；
4. 最后对 surviving divisor做 `a_3` growing CRT representative test。

对低高度，这已经把 certificate 的搜索空间显著压缩；对无界高度仍需控制 divisor/CRT representative 的统一行为。
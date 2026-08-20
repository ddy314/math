# A1 minimal diagonal: unified 2-high mod-5 Legendre lock

> 日期：2026-08-20。依赖 `deep-double-2high-master.md`、`deep-gap-unit-square.md`。本文提取 strict-5 contact square 在 surviving double-deep master branch 中真正独立的局部信息。

状态：**已严格完成。**

---

## 1. master stripped equations mod 5

剩余 double-deep 全部处于 2-high / 5-low。沿用

\[
\alpha\beta=r_{10},
\qquad
2\beta u-\alpha v=5^d,
\]

\[
\beta q-5\alpha s=2^c n_0,
\]

以及

\[
qv=Q,
\qquad su=b_1.
\]

其中所有 `alpha,beta,q,s,u,v,n0` 都与 5 互素。

模 5：

\[
\boxed{\beta q\equiv2^c n_0,}
\tag{1}
\]

\[
\boxed{2\beta u\equiv\alpha v.}
\tag{2}

又

\[
Q\equiv1\pmod5,
\qquad b_1\equiv-w\pmod5,
\]

所以

\[
\boxed{qv\equiv1,}
\qquad
\boxed{su\equiv-w}
\pmod5.
\tag{3}

---

## 2. 消去 four-factor variables

由 (1)：

\[
q\equiv2^c n_0\beta^{-1}.
\]

于是由 `qv=1 mod 5`：

\[
v\equiv\beta 2^{-c}n_0^{-1}.
\]

代入 (2)：

\[
u\equiv\alpha 2^{-c-1}n_0^{-1}.
\]

再由 `su=-w mod 5`：

\[
s\equiv-w\,2^{c+1}n_0\alpha^{-1}.
\]

所以

\[
\begin{aligned}
h=qs
&\equiv
-w\,2^{2c+1}n_0^2(\alpha\beta)^{-1}\\
&=-w\,2^{2c+1}n_0^2r_{10}^{-1}
\pmod5.
\end{aligned}
\tag{4}

取 Legendre symbol。因为

\[
\left(\frac{-1}{5}\right)=1,
\qquad
\left(\frac2{5}\right)=-1,
\]

且 `2c+1` 为奇数：

\[
\boxed{
\left(\frac h5\right)
=-\left(\frac w5\right)
\left(\frac{r_{10}}5\right).}
\tag{5}

这里逆元与原数具有相同 Legendre symbol。

---

## 3. 与原 contact square 的 strict-5 unit lock 联立

`deep-gap-unit-square.md` 在 double-deep `lambda_2=0` 中给

\[
\boxed{
\left(\frac{hN_5}{5}\right)
=(-1)^{1-A},}
\tag{6}

其中

\[
N_5=N/5^{v_5(N)}
\]

是 prefix square norm 的 5-adic unit part。

把 (5) 代入 (6)：

\[
-\left(\frac{wr_{10}N_5}{5}\right)
=(-1)^{1-A}.
\]

因此

\[
\boxed{
\left(\frac{w\,r_{10}\,N_5}{5}\right)
=(-1)^A.}
\tag{7}

这是主结论。

---

## 4. 用 master offset `eta` 表示

master branch 有

\[
A=2k+3+\eta.
\]

由于 `2k+3` 为奇数：

\[
(-1)^A=-(-1)^\eta.
\]

故也可写为

\[
\boxed{
\left(\frac{w\,r_{10}\,N_5}{5}\right)
=-(-1)^\eta.}
\tag{8}

所以 RHS 完全不依赖 `k`，只依赖 `eta mod 2`。

再结合 `deep-double-2high-master.md`：

- even `w=2,4` 时 `eta` 必为偶数，因此
  \[
  \boxed{\left(\frac{w r_{10}N_5}{5}\right)=-1;}
  \]
- odd `w=1,3` 时 `eta mod2=v_2(N) mod2`，所以 (8) 与 prefix 2-adic branch直接联动。

---

## 5. prefix `N_5` 可稳定局部化

对当前 `k>=32`，任意固定小 `m<=31` 有

\[
\boxed{
N\equiv(N_0-1)^2+(zw)^2\pmod{5^m}.}
\tag{9}

因此 `v_5(N)` 与 `N_5 mod5` 可完全由 `N_0 mod 5^{m}` 的有限 Hensel branch决定。

特别地若 `v_5(N_0)>=2`，则 `N_0=0 mod25`，直接得到：

\[
\boxed{
\begin{array}{c|c|c}
(z,w)&v_5(N)&N_5\bmod5\\ \hline
(1,1)&0&2\\
(1,2)&1&1\\
(1,3)&1&2\\
(1,4)&0&2\\
(3,1)&1&2\\
(3,2)&0&2
\end{array}}
\tag{10}

所以在这些 prefix cells 上，(7) 立即变成只含 `w,r_10,eta` 的显式 Legendre filter。

---

## 6. 审计边界

(7) 是 contact square 的独立局部信息；它不应与 `deep-hl-hensel-dependency-audit.md` 中已证明为 four-factor推论的 growing-depth Hensel lock混淆。

当前 surviving 2-high master branch 的安全独立局部组合可以取：

1. 2-adic mod-8 block lock；
2. 本文 mod-5 Legendre lock；
3. contact Q-side square-block lifting；
4. contact continuous sign window；
5. four-factor prime-source skeleton。

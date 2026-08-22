# A1 minimal diagonal: finite-height collapse of the single-5 top edge

> 日期：2026-08-22。
>
> 依赖：`deep-single5-topedge-phase-shell.md`、`deep-single5-topedge-supply-compression.md`、`deep-universal-factorization.md`。
>
> 范围：minimal diagonal `k=g>=32` 的唯一 surviving single-5 top edge
> \[
> D_{\rm gap}=5^B,\qquad B>k,\qquad \lambda_2=2k-1.
> \]

状态：**本文严格证明 top edge 只能出现在有限层 `32<=k<=77`，并给出 typewise 更强上界；本文本身尚未枚举这些有限层。**

---

## 1. phase remainder

置

\[
d:=B-k\ge1,
\qquad T:=10^k.
\]

`deep-single5-topedge-phase-shell.md` 给出显式 phase integer

\[
A_{z,w}:=
\begin{cases}
14N_0+(339-40w)T,&z=1,\\
12N_0+(237-20w)T,&z=3,
\end{cases}
\]

以及正整数

\[
E:=5^dA_{z,w}-10\,2^k\gamma
\]

满足

\[
\boxed{0<E<30\,5^d.}
\tag{1}
\]

令

\[
\boxed{\varepsilon:=E/5.}
\tag{2}
\]

由于 `d>=1` 且 gap numerator 的 5-adic reducedness 给 `5\nmid\gamma`，`E` 至少被 5 整除；因此 `epsilon` 为正整数，并由 (1)

\[
\boxed{0<\varepsilon<6\,5^d.}
\tag{3}
\]

---

## 2. 与第一 four-factor quotient 的 exact identity

写

\[
\alpha:=15-z,
\]

\[
c_{z,w}:=
\begin{cases}
339-40w,&z=1,\\
237-20w,&z=3.
\end{cases}
\]

于是

\[
A_{z,w}=\alpha N_0+c_{z,w}T.
\]

定义

\[
\boxed{
P:=(\alpha-w)N_0+c_{z,w}T.
}
\tag{4}
\]

六类型中 `alpha-w>0`、`c_{z,w}>0`，故 `P>0`。

universal first factor 为

\[
X_1=5^B(10T\Gamma-wN_0)=sa.
\]

top edge 中 `v_5(a)=k+1`，写

\[
a=5^{k+1}a_0,
\qquad 5\nmid a_0.
\]

则

\[
sa_0=5^{d-1}(10T\Gamma-wN_0).
\]

而由 `E=5^dA_{z,w}-10\,2^k\gamma` 与

\[
T\Gamma=\frac{2^k\gamma}{5^d}
\]

可得

\[
\varepsilon
=5^{d-1}\bigl(A_{z,w}-10T\Gamma\bigr).
\]

因此

\[
\boxed{
sa_0=5^{d-1}P-\varepsilon.
}
\tag{5}
\]

另一方面 universal factorization / gap identity 在 top edge 给

\[
\boxed{
sa_0=b_1\,5^{d-1}N_0-h2^{3k}.
}
\tag{6}
\]

将 (5),(6) 比较，得到

\[
\boxed{
h2^{3k}=5^{d-1}L+\varepsilon,}
\tag{7}
\]

其中

\[
\boxed{
L:=b_1N_0-P
=(10T^2-\alpha)N_0-c_{z,w}T.
}
\tag{8}
\]

---

## 3. selected supply 与 `L` 的小 resultant

写 legal odd supply

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1,
\qquad Q=10b_1+1.
\]

并且 `(q,s)=1`。

由 (8) 模 `b1`：

\[
\boxed{L\equiv-P\pmod{b_1}.}
\tag{9}
\]

又

\[
10L
=10b_1N_0-10P
=(Q-1)N_0-10P,
\]

故模 `Q`

\[
\boxed{10L\equiv-(10P+N_0)\pmod Q.}
\tag{10}
\]

因为 `(10,Q)=1`，若

\[
g_s:=\gcd(s,L),
\qquad
g_q:=\gcd(q,L),
\]

则

\[
 g_s\mid P,
\qquad
 g_q\mid 10P+N_0.
\]

又 `(q,s)=1`，所以

\[
\boxed{
 g:=\gcd(h,L)=g_qg_s<P(10P+N_0).
}
\tag{11}
\]

使用 `N0<T` 得 typewise：

\[
P<C_1T,
\qquad
10P+N_0<C_2T,
\]

其中

\[
\boxed{
\begin{array}{c|c|c|c}
(z,w)&C_1&C_2&C:=C_1C_2\\ \hline
(1,1)&312&3121&973752\\
(1,2)&271&2711&734681\\
(1,3)&230&2301&529230\\
(1,4)&189&1891&357399\\
(3,1)&228&2281&520068\\
(3,2)&207&2071&428697
\end{array}}
\tag{12}
\]

故

\[
\boxed{g<C_{z,w}T^2.}
\tag{13}
\]

---

## 4. `h/g` 必须塞进 phase remainder

由 (7) 模 `h`：

\[
5^{d-1}L+\varepsilon\equiv0\pmod h.
\]

因为 `(h,5)=1`，

\[
\gcd(h,5^{d-1}L)=\gcd(h,L)=g.
\]

因此标准 gcd quotient 给

\[
\boxed{\frac hg\mid\varepsilon.}
\tag{14}
\]

特别地由 (3),(13)：

\[
\boxed{
 h\le g\varepsilon
<6C_{z,w}T^2 5^d.
}
\tag{15}
\]

另一方面 `deep-single5-topedge-supply-compression.md` 的 kappa window 给

\[
\boxed{h\ge5^{B+2k-1}=5^{d+3k-1}.}
\tag{16}
\]

联立 (15),(16)，约去 `5^d`：

\[
5^{3k-1}<6C_{z,w}T^2.
\]

由于 `T^2=2^{2k}5^{2k}`，等价于

\[
\boxed{
\left(\frac54\right)^k<30C_{z,w}.
}
\tag{17}
\]

注意 `d=B-k` 已经完全消失；因此这是对整个无界 top edge 的纯 `k` 上界。

---

## 5. typewise finite-height bounds

逐型代入 (12)，直接检查整数阈值：

\[
\boxed{
\begin{array}{c|c}
(z,w)&\text{必要条件}\\ \hline
(1,1)&k\le77\\
(1,2)&k\le75\\
(1,3)&k\le74\\
(1,4)&k\le72\\
(3,1)&k\le74\\
(3,2)&k\le73
\end{array}}
\tag{18}
\]

例如最弱的 `(1,1)` 中

\[
(5/4)^{78}>30\cdot973752,
\]

故 `k>=78` 不可能；其余类型阈值更低。

结合此前 deep frontier 的 `k>=32`：

\[
\boxed{
\text{surviving minimal-diagonal single-5 top edge is confined to }32\le k\le77.
}
\tag{19}
\]

因此 minimal-diagonal deep sector 已不存在任何无界 parameter direction；剩余工作是对 (18) 的有限 fixed layers 给出 exact certificate，不能用有限检查替代未证明的下降。
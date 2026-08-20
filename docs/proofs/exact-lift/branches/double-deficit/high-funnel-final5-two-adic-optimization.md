# DD `Final-5` 的 `Z`-enhanced stability 与二进两格优化

> **依赖：** [`high-funnel-fminus-sunit-factorization.md`](high-funnel-fminus-sunit-factorization.md)、
> [`high-funnel-defect-optimization.md`](high-funnel-defect-optimization.md)、
> [`high-funnel-denominator-max-lock.md`](high-funnel-denominator-max-lock.md)、
> [`high-funnel-two-adic-balance.md`](high-funnel-two-adic-balance.md)。
>
> **严格状态：** `已严格完成（canonical t_2=1 double-resonant sector）`。
>
> 本文把 exact factorization
> \[
> F_-=2^{H+1}Z(H_{\rm sph}-y_3)\widehat g
> \]
> 中旧 smooth-valuation proof 丢掉的 rough factor `Z` 保留下来，得到
> `Z`-enhanced defect stability。与 `Final-5-lock` 和二进
> `2-short / 2-balanced` 二分联立后：
>
> \[
> \boxed{
> \text{2-short:}\quad
> \limsup\frac nS
> \le
> \frac{5(5+11\log_{10}2)}
> {4(1+\log_{10}2)^2}
> =6.137703685012\ldots}
> \]
>
> \[
> \boxed{
> \text{2-balanced:}\quad
> \limsup\frac nS\le\frac{25}{4}=6.25.}
> \]
>
> 因而整个 `Final-5` sheet满足
> \[
> \boxed{
> \limsup_{\rm Final\text{-}5}\frac nS\le6.25.}
> \]
>
> 结合此前 Tail-short `<=6.215109...`、5-adic/non-max branches `<=6`，
> canonical `t_2=1` double-resonant sector整体得到显式 `<=6.25`。
> **这不是全 DD bound**：旧 funnel 的结构入口有自己的作用域；本文不把 sector
> 结论外推到其他 DD states。

---

## 1. normalized variables

令

\[
a:=\log_{10}2,
\qquad
b:=\log_{10}5=1-a.
\]

沿无界 sequence 取 normalized limsup variables：

\[
M:=\frac mS,
\qquad
Q_5:=\frac{q_5}{S},
\qquad
G_5:=\frac{g_5}{S},
\qquad
N_5:=\frac{n_5}{S},
\]

\[
Q_2:=\frac{\mathfrak q}{S},
\qquad
G_2:=\frac{\mathfrak g}{S},
\qquad
N_2:=\frac{\mathfrak n}{S}.
\]

写

\[
\gamma
=2^{\mathfrak g}5^{g_5}\gamma_0,
\qquad
(\gamma_0,10)=1,
\]

并记 rough overlap height

\[
\boxed{R:=\limsup\frac{\log_{10}\gamma_0}{S}\ge0.}
\tag{1.1}

总 slope记为

\[
\boxed{\mathcal N:=\limsup\frac nS.}
\]

以下所有 `<=` 均是沿 subsequence 去掉 `O(1/S)` 后的 asymptotic inequality。

---

## 2. exact factorization把旧 smooth lower加强一个 `log Z`

`high-funnel-fminus-sunit-factorization.md` 已证明

\[
\boxed{
F_-
=2^{H+1}Z(H_{\rm sph}-y_3)\widehat g,
\qquad
\widehat g=\gamma/c_3.}
\tag{2.1}

在当前 canonical funnel：

- `b_3` 是二进 unique maximum，所以 `c_3=q_lcm/b_3` 是 2-unit；
- `Final-5` 中 `b_3` 是 5-adic maximum，所以 `c_3` 是 5-unit；
- `v_2(H_sph-y_3)=1`；
- `v_5(H_sph-y_3)=T`；
- `v_2(gamma)=mathfrak g`、`v_5(gamma)=g_5`。

因此

\[
v_2(\widehat g)=\mathfrak g,
\qquad
v_5(\widehat g)=g_5.
\]

而 `t_2=1` 给

\[
v_2(\kappa+2G)=\mathfrak f=\mathfrak g+H+1,
\]

`Final-5` 给

\[
k_5=T+g_5.
\]

所以 `(2.1)` 直接给比旧 local valuation lower更强的整除：

\[
\boxed{
2^{\mathfrak f+1}5^{k_5}Z\mid F_-.}
\tag{2.2}

于是

\[
\boxed{
\log_{10}F_-
\ge
 a(\mathfrak f+1)+bk_5+\log_{10}Z.}
\tag{Z-smooth-lower}

`high-funnel-defect-optimization.md` 的旧推导从
`a(f+1)+bk_5` 出发。逐行保留新增的 `+log Z`，其余 algebra不变，得到

\[
\boxed{
\begin{aligned}
\mathcal N
\le{}&6+\frac{2b}{3}M
-2aQ_2-aN_2\\
&-\frac{2b}{3}(2Q_5+G_5+N_5)
-Z_* ,
\end{aligned}}
\tag{Z-defect-stability}

其中

\[
Z_*:=\liminf\frac{\log_{10}Z}{S}.
\]

这就是旧 defect stability 在 `Final-5` 上新增的一份 genuine rough `Z` charge。

---

## 3. 用 S-unit pinning消去 `Z_*`

`t_2=1` phase有

\[
\kappa+2G=2\gamma\,2^HZ.
\]

又由 decimal pinning `Q^2/11<kappa<10Q^2` 与 `Q/G` 的常数窗口：

\[
\log_{10}(\kappa+2G)=2S+O(1).
\]

二进 resonance给

\[
\frac HS
=2M+2Q_2+N_2-2G_2+o(1).
\tag{3.1}

而

\[
\frac{\log_{10}\gamma}{S}
=aG_2+bG_5+R+o(1).
\]

所以

\[
\boxed{
Z_*
=2-a(2M+2Q_2+N_2-2G_2)
-aG_2-bG_5-R.}
\tag{3.2}

把 `(3.2)` 代回 `(Z-defect-stability)`，`Q_2,N_2` 精确消去，得到

\[
\mathcal N
\le
4+\left(2a+\frac{2b}{3}\right)M
-aG_2+bG_5+R
-\frac{2b}{3}(2Q_5+G_5+N_5).
\tag{3.3}

`Final-5-lock` 为

\[
\boxed{M=2Q_5+4G_5+N_5.}
\tag{Final5-M}

消去 `G_5` 后：

\[
\boxed{
\mathcal N
\le
4+\frac{5a+3}{4}M
-aG_2+R
-\frac{3b}{2}Q_5
-\frac{3b}{4}N_5.}
\tag{Final5-Zstab}

特别地丢掉最后两个非正项仍有安全弱化

\[
\boxed{
\mathcal N
\le
4+\frac{5a+3}{4}M-aG_2+R.}
\tag{3.4}

---

## 4. Schmidt budget

`high-funnel-two-adic-balance.md` 已在 `Final-5` 上严格恢复

\[
\boxed{
(1+a)M+2aQ_2+aN_2+2R\le3.}
\tag{Subspace-Final5}

因此特别地

\[
\boxed{M\le\frac3{1+a}.}
\tag{Mmax}

这个 bound 与旧 extremal `M=2.8088...` 不同；它是当前 `Final-5`
新 sheet上的 defect-aware budget。

---

## 5. `2-short`：凸组合消去 `G_2`

`2-short` exact branch为

\[
d\le m+2\mathfrak q+\mathfrak n+\mathfrak g+O(1),
\]

所以 normalized：

\[
\boxed{
\mathcal N
\le2M+2Q_2+N_2+G_2.}
\tag{2-short-N}

取 `(3.4)` 的权

\[
\frac1{1+a}
\]

与 `(2-short-N)` 的权

\[
\frac a{1+a}.
\]

两式右端的 `G_2` coefficient恰好抵消：

\[
-\frac{a}{1+a}G_2
+\frac{a}{1+a}G_2=0.
\]

得到

\[
\begin{aligned}
\mathcal N
\le{}&
\frac4{1+a}
+\frac{13a+3}{4(1+a)}M\\
&+\frac{2aQ_2+aN_2+R}{1+a}.
\end{aligned}
\tag{5.1}

而 `(Subspace-Final5)` 给

\[
2aQ_2+aN_2+R
\le3-(1+a)M,
\]

因为 `R>=0` 且原式有 `2R`。所以

\[
\boxed{
\mathcal N
\le
\frac7{1+a}
+\frac{9a-1}{4(1+a)}M.}
\tag{5.2}

注意

\[
9a-1>0
\]

（甚至 `a>1/9` 已足够）。故用 `(Mmax)`：

\[
\begin{aligned}
\mathcal N
&\le
\frac7{1+a}
+\frac{3(9a-1)}{4(1+a)^2}\\
&=
\boxed{
\frac{5(5+11a)}{4(1+a)^2}}.
\end{aligned}
\tag{2-short-bound}

数值为

\[
\boxed{
\mathcal N
\le6.137703685012\ldots.}
\]

这比此前 Tail-short sector 的 `6.215109...` 还低。

---

## 6. `2-balanced`：直接代入 Schmidt budget

`2-balanced` exact equality为

\[
2\mathfrak g=m+\mathfrak q+\ell-2,
\]

其中 `ell in {0,1}`。归一化后

\[
\boxed{2G_2=M+Q_2.}
\tag{6.1}

把 `(6.1)` 代入完整 `(Final5-Zstab)`：

\[
\begin{aligned}
\mathcal N
\le{}&
4+\frac{3(1+a)}4M
-\frac a2Q_2+R\\
&-\frac{3b}{2}Q_5
-\frac{3b}{4}N_5.
\end{aligned}
\tag{6.2}

由 `(Subspace-Final5)`：

\[
R
\le
\frac{3-(1+a)M-2aQ_2-aN_2}{2}.
\]

代入 `(6.2)`：

\[
\boxed{
\begin{aligned}
\mathcal N
\le{}&
\frac{11}{2}+\frac{1+a}{4}M
-\frac{3a}{2}Q_2-\frac a2N_2\\
&-\frac{3b}{2}Q_5-\frac{3b}{4}N_5.
\end{aligned}}
\tag{6.3}

丢掉所有非正 defect项，再用 `(Mmax)`：

\[
\boxed{
\mathcal N
\le
\frac{11}{2}+\frac34
=\frac{25}{4}=6.25.}
\tag{2-balanced-bound}

该常数是 exact rational number，不是数值 LP 猜测。

---

## 7. `Final-5` 与 canonical funnel 的新 sector bound

`high-funnel-two-adic-balance.md` 已证明 `2-short / 2-balanced` 穷尽
当前 canonical `Final-5` sheet。因此

\[
\boxed{
\limsup_{\rm Final\text{-}5}\frac nS
\le\max(6.137703685012\ldots,6.25)
=6.25.}
\tag{Final5-625}

再回到此前 5-adic branch tree：

- Tail-short：
  \[
  \limsup n/S\le6.215109404735\ldots;
  \]
- defect-heavy 且 `B_5>=m`：`<=6`；
- `b_3` 非 5-adic maximum：`<=6`；
- 剩余 `Final-5`：本文 `<=6.25`。

所以在这些 structural hypotheses 定义的 canonical `t_2=1`
double-resonant sector中：

\[
\boxed{
\limsup\frac nS\le6.25.}
\tag{Canonical-sector-625}

**作用域再次强调：**最早把 arbitrary high candidate压入该 canonical funnel的
分类有自己的 slope/sector前提。`(Canonical-sector-625)` 是对该 algebraic sector
的显式改进，不是对所有 DD states 的无条件 `limsup<=6.25`。

---

## 8. 状态摘要

- **`已严格完成（sector）`**：`Z-defect-stability`、`Final5-Zstab`。
- **`已严格完成（sector）`**：`2-short <= 6.137703685012...` 的闭式凸组合证书。
- **`已严格完成（sector）`**：`2-balanced <= 25/4`。
- **`已严格完成（sector）`**：`Final-5 <= 6.25`，canonical `t_2=1`
  double-resonant sector `<=6.25`。
- **`待证`**：把其他 DD states统一降到同一显式常数以下，或直接给 DD
  absolute height / emptiness；不能把本文件的 sector bound外推成全局结论。
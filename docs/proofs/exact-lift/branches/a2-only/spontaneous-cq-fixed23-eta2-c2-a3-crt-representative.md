# A2 fixed `23` `eta=2` `c=2` 的 third numerator 唯一 CRT 代表

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-decimal-gaussian-kernel.md`、`endpoint-lattice.md` §§8–9。
>
> **严格状态：**唯一 fixed-`23` `c=2` type 已被压成 pure third-block Gaussian kernel `Z_*=g-2a_3-9ib_3`，其长 Gaussian `5`-orientation具有精确深度 `lambda-1`。本文把该 `5`-adic residue 与 endpoint 原有的 `C theta` 二进 phase 联立。首先消去 finite-defect `C`，得到关于 `a_3` 的单变量 `2^m` congruence，其 derivative 恒为奇数，因此固定 source data 后存在唯一 `a_3 mod2^m`。再与 Gaussian orientation 给出的唯一 `a_3 mod5^{lambda-1}` 做 CRT，模数正好为 `T/25`；而真实 third-numerator digit window宽度只有该模数的 `1/10`。因此每个 Gaussian orientation 在完整第三分子窗口中至多留下一个整数代表。本文把连续 `a_3` 自由压成显式 natural-representative test，但尚未证明该代表总落在窗口外。

---

## 1. current type 与 two growing moduli

固定

\[
(d,c_Q,k_h,\varepsilon)
=(1,1587,1,+1),
\]

\[
M=2\lambda,
\qquad
m=\lambda+1,
\qquad
T:=10^m.
\tag{1.1}

已有 `lambda>=8`，并且

\[
M\equiv16\pmod{22}
\Longrightarrow
\lambda\equiv8\pmod{11}.
\tag{1.2}

finite-defect endpoint 使用

\[
J=3-\frac CD,
\qquad
5^\lambda D=gT,
\tag{1.3}

而 source Hensel quotient满足

\[
\boxed{
g\theta=5^{M+\lambda}+c_Qc_u
=5^{3\lambda}+c_Qc_u.}
\tag{1.4}

旧 endpoint 二进 phase 为

\[
\boxed{
C\theta\equiv5^Ma_3
=5^{2\lambda}a_3
\pmod{2^m}.}
\tag{1.5}

---

## 2. Gaussian near-norm 给 `C` 的 deep binary square phase

前一文件定义

\[
\mathcal Z_*:=g-2a_3-9ib_3
\]
并证明

\[
N(\mathcal Z_*)
=(g-2a_3)^2+81b_3^2
=12gT-4\cdot5^\lambda C.
\tag{2.1}

令

\[
A_0:=\frac g2-a_3.
\tag{2.2}

则 (2.1) 除以 `4`：

\[
\boxed{
5^\lambda C
=3gT-A_0^2-
\frac{81b_3^2}{4}.}
\tag{2.3}

当前

\[
v_2(T)=m,
\qquad
v_2(g)\ge2,
\]
所以

\[
2^m\mid gT.
\]
同时

\[
b_3=2^{M+m+1}5c_Qc_u
\]
给

\[
v_2(b_3^2/4)=2(M+m+1)-2
=6\lambda+2>m.
\]
故 (2.3) 模 `2^m` 精确化为

\[
\boxed{
5^\lambda C
\equiv-A_0^2
\pmod{2^m}.}
\tag{2.4}

这是 natural representative的 binary square phase。

---

## 3. 消去 `C` 得到单变量 `a_3` congruence

把 (2.4) 乘 `theta`，再用 (1.5)：

\[
-\theta A_0^2
\equiv5^{M+\lambda}a_3
=5^{3\lambda}a_3
\pmod{2^m}.
\tag{3.1}

由 (1.4)：

\[
5^{3\lambda}=g\theta-c_Qc_u.
\]
代入 (3.1)：

\[
-\theta A_0^2
\equiv(g\theta-c_Qc_u)a_3.
\]
移项：

\[
\theta(A_0^2+ga_3)
\equiv c_Qc_u a_3
\pmod{2^m}.
\]
而

\[
A_0^2+ga_3
=\left(\frac g2-a_3\right)^2+ga_3
=\frac{g^2}{4}+a_3^2.
\]
因此得到新的 `C`-free bridge：

\[
\boxed{
F_2(a_3)
:=
\theta\left(\frac{g^2}{4}+a_3^2\right)
-c_Qc_u a_3
\equiv0
\pmod{2^m}.}
\tag{3.2}

这条式只含真实 source/third-block integers。

---

## 4. `F_2` 在二进方向永远 simple，因此 residue 唯一

当前 `g` 被 `4` 整除，而 `a_3,theta,c_Q,c_u` 都为奇数。模 `2`：

\[
\frac{g^2}{4}\equiv0,
\qquad
a_3^2\equiv1,
\]
所以

\[
F_2(a_3)
\equiv1-1
\equiv0\pmod2.
\tag{4.1}

也就是说唯一 odd class本身就是 first root。

另一方面

\[
\boxed{
F_2'(a_3)
=2\theta a_3-c_Qc_u.}
\tag{4.2}

第一项为偶数，第二项为奇数，因此

\[
\boxed{F_2'(a_3)\equiv1\pmod2.}
\tag{4.3}

ordinary Hensel lemma 遂给：从唯一 root modulo `2` 开始，对每个 `n>=1` 都存在唯一 lift modulo `2^n`。特别地存在唯一

\[
\boxed{
a_{3,(2)}\in\mathbb Z/2^m\mathbb Z}
\tag{4.4}

满足 (3.2)。

因此固定 `(lambda,g,c_u,theta)` 后，third numerator 在整个 binary direction没有 residue branching。

---

## 5. 长 Gaussian orientation 给唯一 `5^{lambda-1}` residue

前一文件已严格证明

\[
v_{\pi_\iota}(\mathcal Z_*)=1,
\qquad
v_{\bar\pi_\iota}(\mathcal Z_*)=\lambda-1,
\tag{5.1}

其中 `pi_iota in {2+i,2-i}`；交换命名会同步交换两条 orientation。

固定长 orientation `bar pi_iota^{lambda-1}`。在 quotient

\[
\mathbb Z[i]/(\bar\pi_\iota^{\lambda-1})
\cong
\mathbb Z/5^{\lambda-1}\mathbb Z
\]
中，`i` 映到唯一对应的 Hensel root

\[
\iota_{\lambda-1}^2\equiv-1
\pmod{5^{\lambda-1}}.
\tag{5.2}

由

\[
\mathcal Z_*=g-2a_3-9ib_3
\]
得到

\[
\boxed{
g-2a_3-9\iota_{\lambda-1}b_3
\equiv0
\pmod{5^{\lambda-1}}.}
\tag{5.3}

因为 `2` 是 `5`-进单位，orientation选定后唯一固定

\[
\boxed{
a_{3,(5)}
\equiv
\frac{g-9\iota_{\lambda-1}b_3}{2}
\pmod{5^{\lambda-1}}.}
\tag{5.4}

另一 Gaussian orientation对应另一个 root `-iota_{lambda-1}`。因此在未预先固定 orientation 时，最多有两条 `5`-adic residue；固定 canonical Gaussian phase后只有一条。

---

## 6. CRT modulus 恰好是 `T/25`

两个模数互素：

\[
2^m,
\qquad
5^{\lambda-1}.
\]
所以固定 Gaussian orientation 后，(4.4) 与 (5.4) 由 CRT 唯一确定

\[
\boxed{
R_3^{\rm CRT}
\in[0,\mathfrak M_3),}
\tag{6.1}

其中

\[
\begin{aligned}
\mathfrak M_3
&:=2^m5^{\lambda-1}\\
&=2^{\lambda+1}5^{\lambda-1}\\
&=\frac{10^{\lambda+1}}{25}\\
&=\boxed{\frac T{25}}.
\end{aligned}
\tag{6.2}

这个 modulus随无界高度指数增长；它与之前 fixed `23^4` residue性质完全不同。

---

## 7. third-numerator digit window 只有 CRT cell 的十分之一

当前危险 endpoint 已有严格 third numerator window

\[
\boxed{
1<\zeta:=\frac{a_3}{T}<\frac{251}{250}.}
\tag{7.1}

所以

\[
\boxed{
T<a_3<T+\frac T{250}.}
\tag{7.2}

由 (6.2)：

\[
T=25\mathfrak M_3,
\qquad
\frac T{250}=\frac{\mathfrak M_3}{10}.
\tag{7.3}

因此 `T` 本身被 `mathfrak M_3` 整除。写

\[
h:=a_3-T.
\]
则实际 third numerator 必满足

\[
\boxed{
0<h<\frac{\mathfrak M_3}{10},
\qquad
h\equiv R_3^{\rm CRT}\pmod{\mathfrak M_3}.}
\tag{7.4}

因为区间长度严格小于一个完整 modulus，立即得到：

\[
\boxed{
\text{每个 Gaussian orientation 在真实 third-numerator window中至多有一个 }a_3.}
\tag{7.5}

更精确地，存在候选当且仅当 CRT 的最小非负代表满足

\[
\boxed{
0<R_3^{\rm CRT}<\frac{\mathfrak M_3}{10}.}
\tag{7.6}

若成立，则候选被完全恢复为

\[
\boxed{
a_3=T+R_3^{\rm CRT}.}
\tag{7.7}

---

## 8. 更新后的 global representative frontier

此前 fixed-`23^4` canonical residue相对于 `C` interval太短，无法提供 pruning。本文得到的是不同量级的结果：

\[
\boxed{\mathfrak M_3=T/25}
\]
与 third-numerator window同指数尺度，而窗口只占一个 CRT cell 的 `1/10`。

因此最后的 `(1,1587,1,+)` type 已经从

\[
\text{连续 }a_3\text{ digit interval}
\]
压成

\[
\boxed{
\text{每个 source state / Gaussian orientation至多一个显式 CRT representative}.}
\]

下一步不应再对 `a_3` 做连续估计。应研究 representative test (7.6)：

1. 用 `g theta=5^{3lambda}+1587c_u` 计算唯一 binary root `a_{3,(2)}`；
2. 用 long Gaussian orientation计算 `a_{3,(5)}`；
3. 证明 CRT representative统一不进入 `(0,M_3/10)`，或把进入情况进一步压成有限 source residue classes。

这已经是一个真正随高度增长的 natural-representative closure target。
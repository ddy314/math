# A2 fixed `23` `eta=2` `c=2` 的 source-only divisor / CRT certificate

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-a3-crt-representative.md`、`spontaneous-cq-fixed23-eta2-c2-source-window.md`、`endpoint-lattice.md` §9。
>
> **严格状态：**前一文件把 third numerator压成每个 source state / Gaussian orientation至多一个 CRT representative。本文进一步消去 source variable `g`：source Hensel product把候选参数化为 `S_lambda(c_u)=5^(3lambda)+1587c_u` 的一个窄区间奇因子 `theta`，而 binary/5-adic 两个 `a_3` residues都可只用 `(lambda,c_u,theta)` 表示。因此最后的 `c=2` type 已被改写成 source-only divisor certificate；对固定 `(lambda,c_u)`，只需检查 `S_lambda(c_u)` 在 `(19L_*,20L_*)` 中的奇因子及至多两个 Gaussian orientations。本文不证明该 divisor interval 对所有高度为空。

---

## 1. source product 与 Hensel slot

当前 type 满足

\[
M=2\lambda,
\qquad
m=\lambda+1,
\qquad
c_Q=1587.
\]

source Hensel identity 为

\[
\boxed{
g\theta
=5^{M+\lambda}+c_Qc_u
=5^{3\lambda}+1587c_u.}
\tag{1.1}

定义 source integer

\[
\boxed{
\mathscr S_\lambda(c_u)
:=5^{3\lambda}+1587c_u.}
\tag{1.2}

所以

\[
\boxed{g\theta=\mathscr S_\lambda(c_u).}
\tag{1.3}

`endpoint-lattice.md` §9 对危险 `(a,k)=(9,2)` core 已证明

\[
19L_*<\theta<20L_*,
\tag{1.4}

其中

\[
L_*:=2^m5^\lambda c_u.
\]
当前 `m=lambda+1`，故

\[
\boxed{
L_*=2^{\lambda+1}5^\lambda c_u.}
\tag{1.5}

并且 `theta` 为正奇整数。因此任何真实候选必须先提供

\[
\boxed{
\theta\mid\mathscr S_\lambda(c_u),
\qquad
\theta\text{ odd},
\qquad
19L_*<\theta<20L_*.}
\tag{1.6}

一旦 `theta` 选定，

\[
\boxed{
g=\frac{\mathscr S_\lambda(c_u)}{\theta}}
\tag{1.7}

唯一恢复。于是 `(g,theta)` 不再是两维自由。

---

## 2. binary `a_3` root 只依赖 `(lambda,c_u,theta)`

前一文件的 binary polynomial 是

\[
F_2(a)
=
\theta\left(\frac{g^2}{4}+a^2\right)
-1587c_u a.
\tag{2.1}

由于 `theta` 为奇数，而 (1.3) 的全部二进 content进入 `g`，当前 `g` 被 `4` 整除。将 (1.7) 代入即可把 (2.1) 完全视为

\[
\boxed{
F_{2,\lambda,c_u,\theta}(a)
\in\mathbb Z/2^m\mathbb Z.}
\tag{2.2}

前一文件已证明

\[
F_2'(a)=2\theta a-1587c_u
\]
恒为奇数，所以存在唯一 root

\[
\boxed{
a_{3,(2)}(\lambda,c_u,\theta)
\pmod{2^m}.}
\tag{2.3}

因此 binary side不再需要额外枚举 `g`。

---

## 3. Gaussian `5`-residue 也可消去 `g`

固定 long Gaussian orientation，令

\[
\iota:=\iota_{\lambda-1},
\qquad
\iota^2\equiv-1\pmod{5^{\lambda-1}}.
\]

前一文件有

\[
a_{3,(5)}
\equiv
\frac{g-9\iota b_3}{2}
\pmod{5^{\lambda-1}}.
\tag{3.1}

source product (1.3) 模 `5^{lambda-1}` 时，`5^{3lambda}` 消失：

\[
g\theta
\equiv1587c_u
\pmod{5^{\lambda-1}}.
\]
`theta` 是 `5`-进 unit，所以

\[
\boxed{
g
\equiv1587c_u\theta^{-1}
\pmod{5^{\lambda-1}}.}
\tag{3.2}

另一方面当前 denominator exact formula为

\[
b_3
=2^{3\lambda+2}\cdot5\cdot1587c_u.
\tag{3.3}

代入 (3.1)：

\[
\boxed{
a_{3,(5)}
\equiv
\frac{1587c_u}{2}
\left(
\theta^{-1}
-45\iota\,2^{3\lambda+2}
\right)
\pmod{5^{\lambda-1}}.}
\tag{3.4}

所以 long-5 residue 同样只依赖

\[
(\lambda,c_u,\theta,\iota).
\]
交换 Gaussian orientation只需把 `iota` 换成 `-iota`。

---

## 4. source-only CRT representative

定义

\[
A:=2^m=2^{\lambda+1},
\qquad
B:=5^{\lambda-1},
\]

\[
\mathfrak M_3:=AB=T/25.
\]

对每个满足 (1.6) 的 `theta` 和每个 Gaussian orientation `iota`：

1. 由 (2.3) 得唯一 `a_(2) mod A`；
2. 由 (3.4) 得唯一 `a_(5) mod B`；
3. CRT 得唯一
   \[
   R_3^{\rm CRT}(\lambda,c_u,\theta,\iota)
   \in[0,\mathfrak M_3).
   \]

前一文件已证明真实 third numerator存在的必要充分 representative 条件是

\[
\boxed{
0<R_3^{\rm CRT}
<\frac{\mathfrak M_3}{10}.}
\tag{4.1}

若成立，则

\[
\boxed{
a_3=T+R_3^{\rm CRT}.}
\tag{4.2}

因此对固定 `(lambda,c_u)`，third-block 搜索已完全变成：

\[
\boxed{
\theta\in
\operatorname{Div}(\mathscr S_\lambda(c_u))
\cap(19L_*,20L_*)
\quad\text{和至多两个 }\iota\text{ 的有限检查}.}
\tag{4.3}

---

## 5. normalized CRT-cell formulation

若希望避免直接构造一个 `T/25` 级别的大整数，可以使用标准 CRT coefficient。取

\[
r_2:=a_{3,(2)}\in[0,A),
\]

并定义

\[
\boxed{
\kappa_3
:=\operatorname{res}_{[0,B)}
\left((a_{3,(5)}-r_2)A^{-1}\right).}
\tag{5.1}

则

\[
R_3^{\rm CRT}=r_2+A\kappa_3.
\tag{5.2}

所以 (4.1) 等价于

\[
\boxed{
0<r_2+A\kappa_3<\frac{AB}{10}.}
\tag{5.3}

特别地必要条件为

\[
\boxed{\kappa_3<\frac B{10}.}
\tag{5.4}

这把 global representative test转成一个单纯的 `5^{lambda-1}` centered coefficient test：真实候选要求两个 local roots的 relative CRT coefficient进入最前面的 `10%` cell。

---

## 6. 与低 source-content window 联立

`spontaneous-cq-fixed23-eta2-c2-source-window.md` 已给最初 source states：

\[
(\lambda,c_u)
=(52,29),
(63,337),
(74,3917),
(74,3929),\ldots
\]

因此这些低层已经是完全有限的 certificate：对每一对 `(lambda,c_u)`，只需因式分解单个整数

\[
\mathscr S_\lambda(c_u)=5^{3\lambda}+1587c_u,
\]
取其 `(19L_*,20L_*)` 内奇因子，并检查 (5.3)。不再需要搜索 `g,a_3` 的大区间。

---

## 7. 更新后的 closure target

唯一 `c=2` type 当前可以规范地表述为：

\[
\boxed{
\exists\lambda\equiv8\pmod{11},\ c_u,\ \theta,\ \iota
}
\]
满足

\[
\boxed{
\begin{aligned}
&c_u\text{ obeys source-content window and prime support},\\
&\theta\mid5^{3\lambda}+1587c_u,\\
&19L_*<\theta<20L_*,\\
&0<R_3^{\rm CRT}(\lambda,c_u,\theta,\iota)<\mathfrak M_3/10.
\end{aligned}}
\tag{7.1}

这已经是 source-only divisor/natural-representative problem。后续若继续无界 closure，目标应是证明 (7.1) 为空，或证明其 solution强迫 fixed `23` common depth进入已知 odd class。
# A2 CRT orientation carrier 与 centered Hensel 核的 signed bridge

> **依赖：** `spontaneous-crt-gaussian-slot-orientation.md`、`endpoint-lattice.md` §§16.23–16.30。
>
> **严格状态：**Gaussian high-factor side此前由外部符号 `epsilon=±1` 表示。前一文件证明该 side可由整数 `O_Delta=2^{A_G}Q_Delta-5^{B_G}k_h^3` 的符号完全恢复；`endpoint-lattice.md` 又已证明 mixed Hensel scalar `chi_E` 的符号等于 `epsilon z_E`，其中 `z_E` 是由真实 denominator defect `H mod g` 唯一确定的 centered odd representative。本文合并二者，得到纯整数三重符号律 `O_Delta z_E chi_E<0`，并把 `epsilon` 从 mixed lift中完全消去。本文是 signed interface，不单独产生矛盾，因此不关闭 A2。

---

## 1. CRT integer orientation carrier

前一文件定义

\[
A_G:=\frac{M+5\eta}{2}+8,
\qquad
B_G:=3M-d-\eta-3,
\]

以及

\[
\boxed{
\mathscr O_\Delta
:=2^{A_G}Q_\Delta-5^{B_G}k_h^3.}
\tag{1.1}
\]

并严格证明

\[
\boxed{
\varepsilon=-1
\iff
\mathscr O_\Delta>0,}
\tag{1.2-}
\]

\[
\boxed{
\varepsilon=+1
\iff
\mathscr O_\Delta<0.}
\tag{1.2+}
\]

因此统一写成

\[
\boxed{
\operatorname{sgn}(\mathscr O_\Delta)=-\varepsilon.}
\tag{1.3}
\]

特别地 `O_Delta` 永不为零。

---

## 2. centered Hensel representative and mixed sign

`endpoint-lattice.md` §16.23 定义唯一 centered odd representative

\[
\boxed{
-\frac g2<z_E<\frac g2,
\qquad
c_-z_E\equiv-5^{d+1}H\pmod g,}
\tag{2.1}
\]

并证明

\[
\boxed{z_E\ne0,\qquad \gcd(z_E,g)=1.}
\tag{2.2}
\]

后续 mixed lift定义 `chi_E`，满足 exact identity

\[
\boxed{
g\chi_E=c_uC+\varepsilon a_2c_-z_E.}
\tag{2.3}
\]

其中 endpoint narrowness给

\[
0<c_uC<a_2c_-|z_E|.
\tag{2.4}
\]

所以大项唯一决定符号：

\[
\boxed{
\operatorname{sgn}(\chi_E)
=\operatorname{sgn}(\varepsilon z_E).}
\tag{2.5}
\]

并且 `chi_E!=0`。

---

## 3. fixed negative triple sign

由 (1.3),(2.5)：

\[
\operatorname{sgn}(\mathscr O_\Delta z_E\chi_E)
=(-\varepsilon)\cdot\operatorname{sgn}(z_E)
\cdot\varepsilon\operatorname{sgn}(z_E)
=-1.
\]

因此得到

\[
\boxed{
\mathscr O_\Delta\,z_E\,\chi_E<0.}
\tag{3.1}
\]

三因子均为非零整数，所以这是严格 signed allocation，而不是弱不等式。

等价地：

\[
\boxed{
\operatorname{sgn}(\mathscr O_\Delta)
=-\operatorname{sgn}(z_E\chi_E).}
\tag{3.2}
\]

于是 additive CRT quotient的 normalized side与真实 decimal defect `H mod g` 产生的 centered Hensel side已经直接对接。

---

## 4. eliminate the external Gaussian-side symbol

由 (1.3)：

\[
\varepsilon=-\operatorname{sgn}(\mathscr O_\Delta).
\]

代入 (2.3)：

\[
\boxed{
 g\chi_E
 =c_uC
 -\operatorname{sgn}(\mathscr O_\Delta)
  a_2c_-z_E.}
\tag{4.1}
\]

所以 reflection high-2 的 mixed signed kernel可以完全写成

\[
\boxed{
(\mathscr O_\Delta,z_E,\chi_E)}
\tag{4.2}
\]

三个 ordinary integers；不再需要把 `epsilon` 当作一个独立 binary choice带到后续证明中。

这点对有限 slot 特别有用：任何后续 congruence、natural-representative 或 sign estimate如果能从 `(Q_Delta,H)` 独立决定 `O_Delta` 与 `z_E chi_E` 同号，就会与 (3.1) 立即矛盾。

---

## 5. quantitative contact remains extremely narrow

`endpoint-lattice.md` 还已有

\[
\left|
\frac{g\chi_E}{\varepsilon a_2c_-z_E}-1
\right|<\frac3{50000}.
\]

用 `epsilon=-sgn(O_Delta)` 改写：

\[
\boxed{
\left|
\frac{g\chi_E}
{-\operatorname{sgn}(\mathscr O_\Delta)a_2c_-z_E}
-1
\right|<\frac3{50000}.}
\tag{5.1}
\]

所以 (3.1) 不只是象限关系：`chi_E` 在由 `O_Delta` 选定的反向 ray 上具有小于 `6e-5` 的相对偏差。

---

## 6. current role

本文没有产生新的 independent character；它把此前两个已经严格的 Archimedean inputs组合成同一 signed integer interface。

新的 closure target可以明确写成：从 additive CRT residue / exact `2,5` gap phase与 centered congruence

\[
c_-z_E\equiv-5^{d+1}H\pmod g
\]

推出 `O_Delta z_E chi_E>0`，或直接固定 `O_Delta` 的错误符号。任一结果都会与 (3.1) 冲突并排除相应 high-2 allocation。

A2 仍为 `待证`。

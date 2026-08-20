# A2 fixed `23` `eta=2`, `v_23(c_Q)=1` 的 high-2/source-ratio bridge

> **依赖：** `spontaneous-cq-fixed23-eta2-slots.md`、`spontaneous-cq-relative-depth-nogo.md`、`spontaneous-cq-canonical-defect-overlap.md`、`endpoint-lattice.md` §16.7。
>
> **严格状态：**`eta=2` 的 fixed-`23` high-2 lattice 已压成三型，其中两个 `d=2` 类型满足 `v_23(c_Q)=1`。本文利用 high-2 equality 与 canonical `c_- / c_+` allocation，把 source ratio `rho=z/c_u` 与 normalized denominator `q_1=Q/23` 直接联立。两个 surviving `c=1` 类型给出完全相同的 bridge。再与 fixed-`23` prefix 二阶式和 orientation gate 联立，得到显式 `(kappa,h_N)` 曲线，并识别四条 orientation-independent 的 `M mod 506` 强制 depth-1 class。这里的“强制 depth 1”指 pure-`c_Q` common depth 在 `23` 处恰为奇数 `1`，并不排除 arithmetic state。

---

## 1. 两个 `c=1` high-2 类型共享同一个 odd product

`spontaneous-cq-fixed23-eta2-slots.md` 的三型中，两个 `v_23(c_Q)=1` 类型为

\[
(d,c_Q,k_h,\varepsilon)
=(2,23,9,-),
\qquad
(2,207,1,-).
\tag{1.1}
\]

写

\[
c_Q=23\bar c.
\]

则两型分别有

\[
(\bar c,k_h)=(1,9),
\qquad
(9,1),
\]
所以统一满足

\[
\boxed{\bar c\,k_h=9.}
\tag{1.2}
\]

此外 `eta=2,d=2` 给

\[
M=2m-2,
\qquad
M\equiv16\pmod{22}.
\tag{1.3}
\]

因此

\[
N:=10^M\equiv4\pmod{23},
\qquad
B:=b_2\equiv-2N\equiv15\pmod{23}.
\tag{1.4}
\]

由 `2m=M+2` 与 (1.3)，

\[
m\equiv9\text{ or }20\pmod{22},
\]
故无论哪一类

\[
\boxed{T^2=10^{2m}\equiv9\pmod{23}.}
\tag{1.5}
\]

---

## 2. high-2 equality 直接恢复 `g mod 23`

令

\[
s=+1
\quad\Longleftrightarrow\quad23\mid c_-,
\]

\[
s=-1
\quad\Longleftrightarrow\quad23\mid c_+.
\tag{2.1}
\]

canonical factorization 给

\[
H_0\equiv sY_3=sga_3\pmod{23}.
\tag{2.2}
\]

high-2 equality 为

\[
H_0+\varepsilon Y_2=\frac{g^2k_h}{2},
\qquad
Y_2=a_2c_Q5^d.
\tag{2.3}
\]

由于 `23|c_Q`，模 `23` 时 `Y_2=0`。又 `23∤gk_h`，所以 (2.2)–(2.3) 给

\[
\boxed{
g\equiv\frac{2sa_3}{k_h}\pmod{23}.}
\tag{2.4}
\]

注意这个 congruence 不依赖 high-2 side `varepsilon`；`s` 只记录 canonical `Y_3` orientation。

---

## 3. 消去 `g/c_u` 得到 normalized denominator bridge

定义

\[
\rho:=\frac{q5^\lambda}{c_u},
\qquad
q_1:=\frac Q{23}.
\tag{3.1}
\]

因为

\[
Q=2^{M+1}c_Qq
=23\cdot2^{M+1}\bar c\,q,
\]
所以

\[
\boxed{q_1=2^{M+1}\bar c\,q.}
\tag{3.2}
\]

而 reflection denominator 为

\[
B=2^{M+m+1}c_ug.
\tag{3.3}
\]

由 (3.1)–(3.3) 与 (2.4)：

\[
\begin{aligned}
\rho
&=q5^\lambda\frac1{c_u}
=q5^\lambda\frac{2^{M+m+1}g}{B}\\
&\equiv
s\frac{2q_1a_3T}{\bar c\,k_h\,B5^d}
\pmod{23}.
\end{aligned}
\tag{3.4}
\]

这里使用

\[
2^{m+1}5^\lambda=\frac{2T}{5^d}.
\]

对两个 surviving 类型，(1.2)、`d=2`、(1.4)–(1.5) 给

\[
\frac{2T^2}{\bar c k_h B5^d}
\equiv
\frac{18}{9\cdot15\cdot25}
\equiv20
\pmod{23}.
\]

写

\[
\zeta:=\frac{a_3}{T}.
\]
于是统一得到

\[
\boxed{
\rho\equiv20s\,q_1\zeta\pmod{23}.}
\tag{3.5}

这条式同时适用于 `(23,9)` 与 `(207,1)` 两型。

---

## 4. canonical orientation 把 `zeta` 消去

`spontaneous-cq-canonical-defect-overlap.md` 有 exact identity

\[
K-\rho\zeta=(\rho+1)J.
\tag{4.1}
\]

fixed `23` 第一层 `K=16 mod23`。

### minus orientation: `23|c_-`

此时

\[
J=0\pmod{23},
\]
所以

\[
\boxed{\zeta=\frac{16}{\rho}.}
\tag{4.2-}
\]

代入 (3.5)，且 `s=+1`：

\[
\boxed{
\rho^2=21q_1\pmod{23}.}
\tag{4.3-}
\]

### plus orientation: `23|c_+`

此时

\[
J+2\zeta=0\pmod{23},
\]
从 (4.1) 得

\[
\boxed{\zeta=-\frac{16}{\rho+2}.}
\tag{4.2+}
\]

代入 (3.5)，且 `s=-1`：

\[
\boxed{
\rho(\rho+2)=21q_1\pmod{23}.}
\tag{4.3+}
\]

由 primitive orientation separation，minus 中 `rho!=0`，plus 中 `rho(rho+2)!=0`，所以两式都自动保证

\[
q_1\ne0,
\]
与 `v_23(c_Q)=1` 一致。

---

## 5. 与 additive gate 和 prefix 二阶式联立

写

\[
K=16+23\kappa,
\qquad
N^2=16+23h_N.
\]

fixed-`23` prefix equation在 `N=4 mod23` 时为

\[
\boxed{
9\kappa=16h_N+22-16q_1.
}
\tag{5.1}

orientation gates为

\[
\boxed{
\rho(1+14\kappa)-9-18\kappa=0
}
\tag{5.2-}
\]

和

\[
\boxed{
\rho(1+14\kappa)+11=0.
}
\tag{5.2+}
\]

把 (4.3±)、(5.1)、(5.2±) 在 `F_23` 中消去 `rho,q_1`，得到：

### plus orientation

\[
\boxed{
11h_N\kappa^2-5h_N\kappa-h_N
+\kappa^3+5\kappa^2-9\kappa-2=0.
}
\tag{5.3+}
\]

### minus orientation

\[
\boxed{
11h_N\kappa^2-5h_N\kappa-h_N
+\kappa^3+4\kappa^2-3\kappa+7=0.
}
\tag{5.3-}
\]

两式的 `h_N` 系数相同：

\[
11\kappa^2-5\kappa-1.
\]

该系数在 `F_23` 中唯一零点是 `kappa=18`；代回常数项为 `20!=0`，所以这正好恢复 shared pole `kappa=18` 的不能提升。

`kappa=11` 需另外按 source unit boundary 删除：plus 给 `rho=-2`，minus 给 `rho=0`。

---

## 6. length image 与强制 depth-1 classes

当前 `M=16 mod22`，写

\[
M=16+22r,
\qquad0\le r<23.
\]

已有

\[
\boxed{h_N=5+3r\pmod{23}.}
\tag{6.1}

对所有

\[
\kappa\in\mathbf F_{23}\setminus\{11,18\}
\]
逐一使用 (5.3±)，得到 second-layer compatible length images：

### plus orientation compatible

\[
\boxed{
M\bmod506\in
\{38,104,126,192,214,258,280,302,324,390,412,434,456,478,500\}.
}
\tag{6.2+}

所以 plus orientation 的强制 depth-1 classes 为

\[
\boxed{
\{16,60,82,148,170,236,346,368\}\pmod{506}.}
\tag{6.3+}

### minus orientation compatible

\[
\boxed{
M\bmod506\in
\{16,82,104,126,214,236,258,302,324,368,434,456\}.
}
\tag{6.2-}

所以 minus orientation 的强制 depth-1 classes 为

\[
\boxed{
\{38,60,148,170,192,280,346,390,412,478,500\}\pmod{506}.}
\tag{6.3-}

两种 canonical orientation 的 forbidden length 交集是

\[
\boxed{
M\equiv60,148,170,346\pmod{506}.}
\tag{6.4}

因此，无论 `23` 被 allocated 到 `c_-` 还是 `c_+`，只要处于两个 `eta=2,d=2,c=1` high-2 类型之一，并且

\[
M\equiv60,148,170,346\pmod{506},
\]
那么 selected additive gate 都不能与 prefix 一起提升到 `23^2`。于是 pure-`c_Q` common depth 精确停在

\[
\boxed{d_{23}=1.}
\tag{6.5}

这四类是 orientation-independent 的强制 odd-depth classes，不是 arithmetic-state exclusion。

---

## 7. 结果的作用边界

本文首次把 `eta=2` high-2 equality 真正送入 fixed-`23` source ratio；(4.3±) 不属于此前 `theta/omega` source quotient 的代数闭包，因为它使用了独立的 Gaussian high-2 equality。

它仍没有消去全部 `c=1` 类型。对 (6.2±) 中的 compatible classes，局部二阶系统存在满足 high-2/source/prefix/additive 四层条件的 residue，因此继续只做 `mod23` 消元不会关闭它们。

下一步最自然的是：

1. 对第三型 `(d,c_Q,k_h)=(1,1587,1)`，其中 `v_23(c_Q)=2`，建立对应的 `q_2=Q/23^2` high-2 bridge并进入第三层 prefix；
2. 对两个 `c=1` 类型，把 (4.3±) 与 `C` 的 canonical `23^2` residue和 `g/2^m` CRT natural representative联立；
3. 在 global parity ledger 中记录 (6.4) 的四条 forced odd `23` classes，避免后续把“不能 lift”误记成候选被删。
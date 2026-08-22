# A2 rational-root sieve 的五点 cofactor extension

> **依赖：** `endpoint-lattice.md` §§16.27–16.38，尤其 (16.209)–(16.216)、(16.234)–(16.256)。
>
> **严格状态：**canonical 主线此前只使用 rational-root 两侧的 `j=2,3,4` 三点，得到 `Xi_-,Xi_C,Xi_+`。本文证明同一机制可无损扩展到 `j=1,5`：新增两个正奇 `5`-进单位 cofactor，对应大除数 `2D-C` 与 `2D+C`。五个连续 cofactor全部共享同一个模 `L=2^m5^d` 平方类，故产生四个正整数 normalized gaps；由于它们来自同一个 cubic secant quotient，四阶有限差分严格为零，得到新的 exact 四-gap 关系。对 odd `p|g, p!=3`，四个 gap 的 `p`-接触又被四个互不同时为零的线性 third factors控制。本文增强三点 additive sieve，但尚未证明五点系统与 `(z_E,chi_E)` 不相容，因此 A2 仍为 `待证`；后续应把该四-gap selector直接回写 canonical `endpoint-lattice.md`。

---

## 1. 所有整数点都有 rational-root divisor

沿用

\[
r=J_{\rm def}=\frac ND=3-\frac CD,
\qquad
N=3D-C,
\qquad \gcd(C,D)=1,
\]

以及 canonical quartic `F(J)`。对任意整数 `j` 定义

\[
\boxed{s_j:=jD-N=(j-3)D+C.}
\tag{1.1}
\]

`endpoint-lattice.md` (16.210) 的 rational-root argument 本来就是对任意整数 `j` 成立：

\[
\boxed{s_j\mid F(j).}
\tag{1.2}
\]

此前只取 `j=2,4`。现在同时取

\[
\boxed{j=1,2,3,4,5.}
\]

五个 divisor 的绝对值为

\[
\boxed{
2D-C,\quad D-C,\quad C,\quad D+C,\quad2D+C.}
\tag{1.3}
\]

由于

\[
s_j-s_i=(j-i)D,
\qquad
\gcd(s_i,D)=1,
\]

任意共同因子满足

\[
\boxed{
\gcd(s_i,s_j)\mid |i-j|.}
\tag{1.4}
\]

所以这五个大除数在 odd support 上几乎完全互素：唯一可能的非平凡 odd cross-gcd 是 prime `3`，且只能出现在距离恰为 `3` 的两对 `(j,i)=(4,1),(5,2)`。不存在 generic moving common support。

---

## 2. `j=1,5` 继承同一个 exact `2,5` content

写

\[
F(J)
=b_2^2T\,J(TJ+2a_3)(K-J)^2
-Q^2N_0(TJ+a_3)^2.
\tag{2.1}
\]

当前 deep-even endpoint 已有

\[
v_2(Q)=M+1,
\qquad
v_5(N_0)=\nu_5,
\]

且 `a_3` 为 odd `5`-unit。因此对任意固定整数 `j`，

\[
TJ+a_3
\]

仍是 odd `5`-unit。特别地 `j=1,5` 的第二项都具有 exact valuation

\[
2M+2\quad\text{at }2,
\qquad
\nu_5\quad\text{at }5.
\]

第一项的 `2`-depth因 `v_2(b_2)=M+m+t`、`t>=3` 而严格更深；其 `5`-depth至少含完整 `T=10^m`，而当前 core 的 `nu_5=m-3d<m`。`j=5` 还额外得到 `5|(j(K-j)^2)`，只会更深。

所以原 (16.211) 同样扩展为

\[
\boxed{
 v_2(F(1))=v_2(F(5))=2M+2,
 \qquad
 v_5(F(1))=v_5(F(5))=\nu_5.
}
\tag{2.2}
\]

---

## 3. 两个新点的符号与正 cofactor

令

\[
R(J):=
\frac{J(TJ+2a_3)(K-J)^2}{(TJ+a_3)^2}.
\]

因为 `B/A=R(r)`，`F(J)` 的符号由 `R(J)-R(r)` 决定。直接求导：

\[
R'(J)
=
\frac{2(J-K)}{(TJ+a_3)^3}
\left[
J^3T^2+3J^2Ta_3+3Ja_3^2-Ka_3^2
\right].
\tag{3.1}
\]

在

\[
1\le J\le5,
\qquad
1<\frac{a_3}{T}<\frac{251}{250},
\qquad
K>9\cdot10^{11},
\]

方括号严格为负，而 `J-K<0`，故

\[
\boxed{R'(J)>0\qquad(1\le J\le5).}
\tag{3.2}
\]

又 `2<r<3`，因此

\[
\boxed{F(1),F(2)<0<F(3),F(4),F(5).}
\tag{3.3}
\]

由于 `s_j` 具有完全相同的符号模式 `--+++`，可统一定义

\[
\boxed{
\Xi_j:=
\frac{F(j)}
{2^{2M+2}5^{\nu_5}s_j}
\in\mathbf Z_{>0},
\qquad j=1,\dots,5.
}
\tag{3.4}
\]

其中

\[
\Xi_2=\Xi_-,
\qquad
\Xi_3=\Xi_C,
\qquad
\Xi_4=\Xi_+.
\]

由 §2：

\[
\boxed{
\gcd(\Xi_1\Xi_2\Xi_3\Xi_4\Xi_5,10)=1.
}
\tag{3.5}
\]

---

## 4. denominator-wide residue 对五点全部成立

(16.215) 的推导其实也不依赖 `j=2,4`。去掉共同 `2,5` content 后，写

\[
\frac{F(j)}{2^{2M+2}5^{\nu_5}}
=
c_u^2g^2L^3\mathscr A_j
-q^2c_+^2YN\mathscr B_j,
\]

其中

\[
\mathscr B_j=(jT+a_3)^2,
\qquad
N=jD-s_j,
\qquad D=gL.
\]

减去 `s_j q^2c_+^2Y B_j` 后，余项显式被 `D` 整除；又 `gcd(s_j,D)=1`。因此

\[
\boxed{
\Xi_j
\equiv
q^2c_+^2Y(jT+a_3)^2
\pmod D,
\qquad j=1,\dots,5.
}
\tag{4.1}
\]

因为

\[
T=L5^\lambda,
\]

有

\[
(jT+a_3)^2\equiv a_3^2\pmod L,
\]
所以五点共享同一个 denominator square class：

\[
\boxed{
\Xi_1\equiv\Xi_2\equiv\Xi_3\equiv\Xi_4\equiv\Xi_5
\equiv Y(qc_+a_3)^2
\pmod L.
}
\tag{4.2}

特别地五点全部满足

\[
\Xi_j\equiv Y\pmod8.
\]

---

## 5. 四个 normalized gaps 与 cubic fourth difference

定义四个相邻 gap：

\[
\boxed{
\begin{aligned}
\Delta_{--}&:=\frac{\Xi_2-\Xi_1}{L},\\
\Delta_-&:=\frac{\Xi_3-\Xi_2}{L},\\
\Delta_+&:=\frac{\Xi_4-\Xi_3}{L},\\
\Delta_{++}&:=\frac{\Xi_5-\Xi_4}{L}.
\end{aligned}}
\tag{5.1}
\]

`R(J)` 在 `[1,5]` 上严格递增，而且 canonical secant quotient在该区间保持严格递增，因此四者均为正整数；中间两项就是旧 `Delta_-,Delta_+`。

更关键的是

\[
\Xi_j=
\frac{\mathscr H(j)}{2^{2M+2}5^{\nu_5}D},
\]

而 `H(J)=F(J)/(J-r)` 是 cubic。因此五个连续值的四阶有限差分恒为零：

\[
\Xi_1-4\Xi_2+6\Xi_3-4\Xi_4+\Xi_5=0.
\tag{5.2}
\]

用 (5.1) 改写：

\[
\boxed{
\Delta_{--}-3\Delta_-+3\Delta_+-\Delta_{++}=0.
}
\tag{5.3}

所以

\[
\boxed{
\Delta_{--}-\Delta_{++}
=3(\Delta_--\Delta_+)
=3\Gamma_\Delta>0.
}
\tag{5.4}

这是一条三点系统中不存在的新 exact additive relation。

进一步，secant cubic 的 leading coefficient为

\[
a_{\rm cub}
=
\frac{b_2^2T^2}
{2^{2M+2}5^{\nu_5}D}.
\]

由 `b_2=2^{M+m+1}c_ug`、`D=g2^m5^d`、`nu_5=m-3d`：

\[
\boxed{
\frac{a_{\rm cub}}L
=2^{2m}5^{m+d}c_u^2g
=:A_{\rm cub}\in\mathbf Z_{>0}.
}
\tag{5.5}

cubic 的第三有限差分于是给另外两条 exact identities：

\[
\boxed{
\Delta_{--}-2\Delta_-+\Delta_+
=6A_{\rm cub},}
\tag{5.6}
\]

\[
\boxed{
\Delta_--2\Delta_++\Delta_{++}
=6A_{\rm cub}.}
\tag{5.7}

结合旧

\[
\Gamma_\Delta
=2^{m+1}5^dc_u^2\mathscr B_\Delta
=2Lc_u^2\mathscr B_\Delta
\]

与 `B_Delta>gT(2K-15)`，有

\[
\Gamma_\Delta>6A_{\rm cub}
\]

（事实上比值为 `B_Delta/(3gT)> (2K-15)/3`）。故四个 gap严格下降：

\[
\boxed{
\Delta_{--}>\Delta_->\Delta_+>\Delta_{++}>0.
}
\tag{5.8}

其中

\[
\Delta_- -\Delta_+=\Gamma_\Delta,
\]

而左右两侧的下降量分别是

\[
\Gamma_\Delta+6A_{\rm cub},
\qquad
\Gamma_\Delta-6A_{\rm cub}.
\]

---

## 6. odd denominator primes 对四 gap 至多命中一项

由 (4.1)，相邻差满足

\[
\Xi_{j+1}-\Xi_j
\equiv
q^2c_+^2Y\,T\bigl((2j+1)T+2a_3\bigr)
\pmod D.
\]

除以 `L` 并使用 `T/L=5^lambda`，得到模 `g`：

\[
\boxed{
\Delta_j
\equiv
q^2c_+^2Y5^\lambda
\bigl((2j+1)T+2a_3\bigr)
\pmod g,
}
\tag{6.1}
\]

其中 `j=1,2,3,4` 分别对应

\[
\Delta_{--},\Delta_-,\Delta_+,\Delta_{++}.
\]

当前 prefactor与 `g` 互素。因此对 odd prime

\[
p\mid g,
\qquad p\ne3,
\]

有

\[
\boxed{
 p\mid\Delta_j
\iff
p\mid(2j+1)T+2a_3.}
\tag{6.2}

四个 linear factors为

\[
3T+2a_3,\quad5T+2a_3,\quad7T+2a_3,\quad9T+2a_3.
\]

若同一 `p!=3` 命中其中两个，则由相减得到

\[
p\mid2(j-i)T.
\]

因 `1<=|j-i|<=3`、`p` odd、`p!=3`、`gcd(T,g)=1`，不可能。因此

\[
\boxed{
 p\mid g,\ p\text{ odd},\ p\ne3
\Longrightarrow
p\text{ 至多整除四个 normalized gaps中的一个}.}
\tag{6.3}

在危险 `Z≡1 mod4` channel中已有 `3∤g`，所以该 selector覆盖 `g` 的全部 odd prime support。

---

## 7. center saturation 只杀一个 cofactor，不杀两个 central gaps

若 `p^e||g` 的 odd prime进入 §16.31 的 center-saturated channel，first layer为

\[
p\mid A_3:=3T+a_3.
\]

由 (4.1)：

\[
p\mid\Xi_3,
\]

但

\[
2T+a_3\equiv-T,
\qquad
4T+a_3\equiv T
\pmod p,
\]
所以

\[
\boxed{p\nmid\Xi_2\Xi_4.}
\tag{7.1}

相应地，(6.1) 给

\[
5T+2a_3\equiv-T,
\qquad
7T+2a_3\equiv T,
\]
故

\[
\boxed{
\Delta_-\equiv-\Delta_+\not\equiv0\pmod p,
\qquad
p\mid(\Delta_-+\Delta_+).}
\tag{7.2}

所以 odd-saturation 不是“三 cofactor character全部消失”；它是一个单点零化机制，两个 central gap仍保持 unit并被固定为相反 residue。后续可把 (7.2) 与中心核 `(z_E,chi_E)` 或五点 relation (5.3) 联立，而不再把 saturated prime当成完全自由异常。

---

## 8. 当前新增 frontier

原三点主线只有

\[
\Xi_-,\Xi_C,\Xi_+,
\qquad
\Delta_->\Delta_+>0.
\]

现在提升为五点：

\[
\boxed{
\Xi_1<\Xi_2<\Xi_3<\Xi_4<\Xi_5,}
\]

四个 gap不仅共享 exact denominator square class，还满足

\[
\boxed{
\Delta_{--}>\Delta_->\Delta_+>\Delta_{++}>0,}
\]

以及 (5.3),(5.6),(5.7) 的 cubic exact relations。对 dangerous `Z=1` 的全部 odd denominator support，每枚 prime又至多命中一个 gap；center-saturated prime只能杀中心 cofactor，不能杀 central gaps。

这组约束尚未单独推出空性。最窄下一步是把五点 gap selector和

\[
g\chi_E=c_uC+\varepsilon a_2c_-z_E,
\qquad
\left|\frac{g\chi_E}{\varepsilon a_2c_-z_E}-1\right|<\frac3{50000}
\]

联立，或者把四 gap 的 odd-prime support直接送入 additive CRT / source allocation。本文不把五点增强误写为 A2 closure。

A2 仍为 `待证`。

---

## 9. verification

```bash
uv run python scripts/exact-lift/a2-only/research-checks/check_a2_endpoint_five_point_cofactors.py
```

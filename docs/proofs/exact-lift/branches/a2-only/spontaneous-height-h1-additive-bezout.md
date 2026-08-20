# A2 moving height `H_1` / additive 的 exact Bézout depth bridge

> **依赖：** `spontaneous-height-parity-ledger.md`、`spontaneous-height-resultant-parity.md`、`spontaneous-height-moving-singular-nogo.md`。
>
> **严格状态：**moving endpoint-height common channel 已被压成两张 pure-prefix sphere orientations `H_1,H_2` 与 additive carrier `J_H`。本文对第一张 orientation 给出新的 exact Bézout identity，并把已有 `J_H/B_W mod W_q` square bridge代入，得到 `H_1,B_W` 与新 positive `3 mod4` carrier `R_H1` 的逐 prime-power 三项关系。对 genuine external height prime，在 `W_q` depth 内若 `H_1` 与 `B_W` 深度不等，则 `R_H1` 的深度精确等于较浅者；只有 equal-depth cancellation 才可能产生额外 lift。该 equal-depth normalized ratio本身是 square class，所以普通 quadratic-character 路线再次严格降级。本文不处理 `H_2` orientation，也不关闭 moving height pool。

---

## 1. notation

本文件固定 decimal length quantity

\[
N:=N_{\rm dec}=10^M
\]
以避免与 canonical height-side integer重名。沿用

\[
A:=a_2,
\qquad B:=b_2,
\qquad Q:=B+2N,
\]

\[
K:=9N+10A,
\qquad
N_0:=\left(\frac{9B}{2}\right)^2+A^2.
\]

定义

\[
\boxed{F_W(K):=(K-5)(5K-11)=5K^2-36K+55.}
\tag{1.1}

additive-height pure decimal carrier为

\[
\boxed{
\mathcal J_H
:=B^2F_W(K)-Q^2N_0.}
\tag{1.2}

第一张 sphere orientation integer为

\[
\boxed{
\mathcal H_1
:=2025B^4+A^2\mathcal C_H,}
\tag{1.3}

其中引入

\[
\boxed{
\mathcal C_H
:=101B^2+4BN+4N^2.}
\tag{1.4}

`spontaneous-height-parity-ledger.md` 的 normalized polynomial正是

\[
H_1(x,y)
=202500x^4+(101x^2+4x+4)y^2.
\]

---

## 2. exact Bézout identity

定义第三个 pure-prefix integer

\[
\boxed{
\mathscr R_{H1}
:=4\mathcal C_HF_W(K)-81Q^4.}
\tag{2.1}

直接展开有

\[
\boxed{
4\mathcal C_H\mathcal J_H
+4Q^2\mathcal H_1
=B^2\mathscr R_{H1}.}
\tag{2.2}

证明只需代入 (1.2)--(1.4)：

\[
\begin{aligned}
4\mathcal C_H\mathcal J_H
+4Q^2\mathcal H_1
={}&4B^2\mathcal C_HF_W
-81B^2Q^2\mathcal C_H\\
&-4A^2Q^2\mathcal C_H
+8100B^4Q^2.
\end{aligned}
\]

而

\[
\mathcal C_H-100B^2
=B^2+4BN+4N^2
=Q^2.
\]

所以后三项合并为

\[
-81B^2Q^4,
\]
得到 (2.2)。

这不是 first-layer resultant，而是对所有整数 endpoint都成立的 exact identity。

---

## 3. `R_H1` 是 positive primitive `3 mod4` carrier

reflection deep-even 中

\[
B=2^{M+m+1}b_0,
\qquad
N=2^M5^M,
\]
其中 `b_0` odd，且 `M>=11,m>=1`。

由 (1.4)，唯一最浅项是 `4N^2`：

\[
\boxed{
v_2(\mathcal C_H)=2M+2,}
\tag{3.1}

\[
\boxed{
\frac{\mathcal C_H}{2^{2M+2}}
\equiv1\pmod4.}
\tag{3.2}

又 `A` odd 而 `M>=2`，故

\[
K=9N+10A\equiv2\pmod4.
\]
因此

\[
K-5\equiv1\pmod4,
\qquad
5K-11\equiv3\pmod4,
\]

\[
\boxed{F_W(K)\equiv3\pmod4.}
\tag{3.3}

第一项 `4 C_H F_W` 的 `2`-进深度是 `2M+4`；第二项 `81Q^4` 的深度是 `4M+4`。于是

\[
\boxed{v_2(\mathscr R_{H1})=2M+4,}
\tag{3.4}

并且

\[
\boxed{
\widehat{\mathscr R}_{H1}
:=\frac{\mathscr R_{H1}}{2^{2M+4}}
\equiv3\pmod4.}
\tag{3.5}

它在真实 endpoint 上也严格为正。写

\[
x=B/N,
\qquad y=10A/N,
\qquad \tau=N^{-1},
\qquad s=9+y.
\]
则

\[
\frac{\mathscr R_{H1}}{N^4}
=4(101x^2+4x+4)(s-5\tau)(5s-11\tau)
-81(x+2)^4.
\tag{3.6}

当前 endpoint满足

\[
x<\frac2{19}<1,
\qquad y>\frac{249}{250}>\frac9{10},
\qquad0<\tau<10^{-11}<\frac1{100}.
\]
所以

\[
101x^2+4x+4>4,
\]

\[
s-5\tau>\frac{197}{20},
\qquad
5s-11\tau>\frac{4939}{100},
\]
而 `x+2<3`。故

\[
4\cdot4\cdot\frac{197}{20}\cdot\frac{4939}{100}
>81\cdot3^4,
\]
从而 (3.6) 正。于是

\[
\boxed{
\widehat{\mathscr R}_{H1}>0,
\qquad
\widehat{\mathscr R}_{H1}\equiv3\pmod4.}
\tag{3.7}

---

## 4. 送入 `W_q` height bridge

`spontaneous-height-resultant-parity.md` 已证明

\[
\boxed{
\widehat{\mathcal J}_H
\equiv(2^mg)^2\mathscr B_W
\pmod{W_q},}
\tag{4.1}

其中

\[
\mathcal J_H=2^{2M+2}\widehat{\mathcal J}_H.
\]
又 reflection denominator为

\[
B=2^{M+m+1}c_ug.
\]
因此 (4.1) 可无分母地写成

\[
\boxed{
c_u^2\mathcal J_H
\equiv B^2\mathscr B_W
\pmod{W_q}.}
\tag{4.2}

把 (4.2) 代入 (2.2)，得到新的三-carrier congruence：

\[
\boxed{
B^2c_u^2\mathscr R_{H1}
\equiv
4\mathcal C_HB^2\mathscr B_W
+4Q^2c_u^2\mathcal H_1
\pmod{W_q}.}
\tag{4.3}

这是本文的主要 bridge。

---

## 5. genuine `H_1` height prime 上所有 coefficient 都是 units

固定 endpoint-external non-`3` inert prime

\[
p^h\Vert W_q,
\qquad h>=1,
\]
并假设它进入第一张 angle-height orientation：

\[
p\mid\mathcal H_1.
\]

primitive/external separation给

\[
p\nmid2BQc_u.
\tag{5.1}

还必须有

\[
\boxed{p\nmid\mathcal C_H.}
\tag{5.2}

因为若 `p|C_H`，由 (1.3) 和 `p|H_1` 会推出

\[
p\mid2025B^4,
\]
与 `p\nmid3\cdot5\cdot B` 矛盾。

所以 (4.3) 的三个显式 coefficient在 `p` 上全是 units。

另外由 `H_1=0 mod p`：

\[
A^2\mathcal C_H
\equiv-2025B^4\pmod p.
\]
因此

\[
\boxed{
\mathcal C_H
\equiv-\left(\frac{45B^2}{A}\right)^2
\pmod p.}
\tag{5.3}

对 `p=3 mod4`，`C_H` 是 non-square unit。

---

## 6. unequal-depth law

定义截断前的三个 depths

\[
e_B:=v_p(\mathscr B_W),
\qquad
e_1:=v_p(\mathcal H_1),
\qquad
e_R:=v_p(\mathscr R_{H1}).
\]

在

\[
\min(e_B,e_1)<h
\]
范围内，(4.3) 是两个 unit-coefficient terms 的和。

若

\[
e_B<e_1,
\]
则第二项更深，不能取消第一项，所以

\[
\boxed{e_R=e_B.}
\tag{6.1}

若

\[
e_1<e_B,
\]
则同理

\[
\boxed{e_R=e_1.}
\tag{6.2}

因此

\[
\boxed{
e_B\ne e_1,
\quad\min(e_B,e_1)<h
\Longrightarrow
v_p(\mathscr R_{H1})=\min(e_B,e_1).}
\tag{6.3}

只有

\[
\boxed{e_B=e_1<h}
\tag{6.4}

时，normalized cancellation才可能使 `R_H1` 比共同深度继续提升。

这把第一张 moving-height orientation的高阶未知压成单个 equal-depth shell。

---

## 7. equal-depth cancellation 的 ratio 是 square shadow

设

\[
e_B=e_1=e<h.
\]
若 `R_H1` 额外提升，则 (4.3) 除以 `p^e` 后要求

\[
\mathcal C_HB^2
\frac{\mathscr B_W}{p^e}
+Q^2c_u^2
\frac{\mathcal H_1}{p^e}
\equiv0\pmod p.
\]
于是

\[
\boxed{
\frac{\mathscr B_W/p^e}{\mathcal H_1/p^e}
\equiv
-\frac{Q^2c_u^2}{\mathcal C_HB^2}
\pmod p.}
\tag{7.1}

由 (5.3)，`-C_H^{-1}` 是 square：若

\[
\mathcal C_H=-r^2,
\]
则

\[
-\mathcal C_H^{-1}=r^{-2}.
\]
因此 (7.1) 的右边是显式 square class：

\[
\boxed{
-\frac{Q^2c_u^2}{\mathcal C_HB^2}
\in(\mathbf F_p^\times)^2.}
\tag{7.2}

所以 equal-depth extra lift不能通过再叠一个 Legendre character排除；它是 ordinary normalized square synchronization。

这与 `spontaneous-height-companion-cross.md`、`spontaneous-height-moving-singular-nogo.md` 的结论一致：真正剩余困难是 simple higher-depth / natural-representative synchronization。

---

## 8. updated frontier for orientation `H_1`

第一张 moving height common sheet现在有严格分层：

\[
\boxed{
\begin{array}{c|c}
e_B\ne e_1<h&\mathscr R_{H1}\text{ 精确读取较浅 depth}\\
e_B=e_1<h&\text{唯一可能的 extra-cancellation shell}\\
\min(e_B,e_1)\ge h&\text{height exponent 已完全 saturated}
\end{array}}
\tag{8.1
}

前两行中的 character geometry已经完全审计；尤其 unequal-depth区不再是开放 parity mechanism。

本文不对 `H_2` 宣称同型公式。下一步若继续 moving height，最有价值的是为 `H_2` 寻找对应的 exact Bézout carrier，或直接在 saturated `H_1` equal-depth shell加入 `W_q=alpha/omega` 的 natural representative。
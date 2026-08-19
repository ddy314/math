# A2 equal-depth height resonance 的 decimal companion pair

> **依赖：** `spontaneous-height-equal-depth-resonance.md`、`spontaneous-height-oversaturation-depth-ledger.md`、`spontaneous-height-content-oversaturation.md`、`primitive-reduction.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文继续处理唯一尚可无界深化的 `e=v_p(omega)=v_p(W_q)=h` branch。把 `B_W` oversaturation 与 equal-depth cross resonance 合并后，构造两个完全由真实 decimal concatenations 读取的正整数 `E_+`,`E_-`。二者都恰有 `m+3M+4` 位且极其接近；指定 oversaturation prime 在 `E_-` 中恰有 `h` 层，而 `E_+` 至少有 `2h+min(r_B,h,rho_p)` 层，特别地 deep resonance `rho_p>=1` 强迫 `p^(2h+1)|E_+`。这把 projective source-unit resonance 真正变成了同位数 natural representatives 的 p-adic depth asymmetry。本文仍不能控制 `rho_p>min(r_B,h)` 的更高 tail，因此不关闭 A2。

---

## 1. equal-depth setting

固定 genuine non-`3` inert oversaturation prime `p`，沿用

\[
e=v_p(\omega)=h=v_p(W_q)\ge1.
\tag{1.1}
\]

令

\[
V:=v_p(\mathscr B_W)=h+r_B,
\qquad r_B\ge1,
\tag{1.2}
\]

以及 equal-depth resonance depth

\[
\rho_p
:=v_p\left(2DgK\omega_0-fqW_0\right),
\tag{1.3}
\]
其中

\[
\omega=p^h\omega_0,
\qquad
W_q=p^hW_0.
\]

因此

\[
\boxed{v_p(L_{JB})=h+\rho_p,}
\qquad
L_{JB}=2Dg\omega K-fqW_q.
\tag{1.4}
\]

parent 文件还给

\[
\boxed{
\mathcal P_{\omega H}(K)
:=6K^2-36K+55,
}
\tag{1.5}
\]

以及

\[
\boxed{
\mathscr B_W
=c_u^2\mathcal P_{\omega H}(K)
+g\omega(g\omega-2c_u)K^2.}
\tag{1.6}
\]

在 equal-depth oversaturation 中，第二项恰有 `h` 层而左边至少有 `h+1` 层，所以

\[
\boxed{v_p(\mathcal P_{\omega H}(K))=h.}
\tag{1.7}
\]

---

## 2. 一个 source subresultant 承担 resonance 首项

定义

\[
\boxed{
F_H(K):=5K^2-36K+55
=\mathcal P_{\omega H}(K)-K^2.
}
\tag{2.1}
\]

以及

\[
\boxed{
R_+:=DF_H(K)+KN.
}
\tag{2.2}
\]

因为

\[
qW_q=DK-N,
\]
所以也可写成

\[
\boxed{
R_+=D\mathcal P_{\omega H}(K)-KqW_q.}
\tag{2.3}
\]

另令

\[
A_H:=g\omega,
\qquad
f=A_H+c_u,
\qquad
z=A_H-c_u.
\]

由 (1.6)、(1.4) 直接展开得到 exact Bezout identity

\[
\boxed{
\begin{aligned}
c_u^2fR_+
={}&Df\mathscr B_W
-DzA_H^2K^2\\
&+Kc_u^2L_{JB}.
\end{aligned}}
\tag{2.4}
\]

当前 prime 与 `D,f,z,K,c_u` 全部分离。三项的赋值依次至少为

\[
h+r_B,
\qquad
2h,
\qquad
h+\rho_p.
\]
因此

\[
\boxed{
v_p(R_+)
\ge h+\min\{r_B,h,\rho_p\}.}
\tag{2.5}
\]

特别地，若 resonance 真正继续一层

\[
\rho_p\ge1,
\]
则

\[
\boxed{p^{h+1}\mid R_+.}
\tag{2.6}
\]

注意这里没有使用新的 Legendre condition；这是纯 prime-power depth transfer。

---

## 3. complementary source form 永远是 p-unit

定义

\[
\boxed{
R_-:=DF_H(K)-KN.
}
\tag{3.1}
\]

由 (1.7) 与 `p^h|qW_q`，(2.3) 至少给

\[
p^h\mid R_+.
\tag{3.2}
\]

而

\[
R_-=R_+-2KN.
\]
由于 genuine height prime 满足

\[
p\nmid2KN,
\]
所以

\[
\boxed{v_p(R_-)=0.}
\tag{3.3}
\]

因此 equal-depth resonance 在 source 层已经天然形成一个 `deep / unit` companion pair。

---

## 4. 乘回真实 decimal concatenations 后 source 全部消失

令

\[
E_M:=2^{M+1}c_Q,
\]
于是

\[
Q=E_Mq,
\qquad
S=E_MD.
\]

真实拼接整数为

\[
\boxed{
\alpha:=TK+a_3=\omega W_q,
\qquad
\beta:=TQ+b_3=\omega S.}
\tag{4.1}
\]

parent 文件的 exact decimal determinant 为

\[
\boxed{
\Delta_\omega:=Kb_3-Qa_3=E_MN\omega>0.}
\tag{4.2}
\]

定义两个真正的 decimal natural representatives

\[
\boxed{
\mathcal E_+
:=F_H(K)\beta+K\Delta_\omega,}
\tag{4.3+}
\]

\[
\boxed{
\mathcal E_-
:=F_H(K)\beta-K\Delta_\omega.}
\tag{4.3-}
\]

利用

\[
\beta=E_MD\omega,
\qquad
\Delta_\omega=E_MN\omega,
\]
立即得到 exact identities

\[
\boxed{
\mathcal E_+=E_M\omega R_+,}
\tag{4.4+}
\]

\[
\boxed{
\mathcal E_-=E_M\omega R_-.}
\tag{4.4-}
\]

因此 source variables `D,q,W_q,omega` 在 (4.3±) 的定义中已经完全消失；它们只用于证明赋值。

由于当前 prime 满足 `p\nmid E_M`，由 (2.5)、(3.3)：

\[
\boxed{
v_p(\mathcal E_-)=h,}
\tag{4.5-}
\]

\[
\boxed{
v_p(\mathcal E_+)
\ge2h+\min\{r_B,h,\rho_p\}.}
\tag{4.5+}
\]

特别地

\[
\boxed{
\rho_p\ge1
\Longrightarrow
p^{2h+1}\mid\mathcal E_+.}
\tag{4.6}
\]

所以 projective unit resonance 已变成一个完全 decimal 的 p-adic depth asymmetry：

\[
\boxed{
\mathcal E_-:\ h\text{ 层},
\qquad
\mathcal E_+:\ \ge2h+1\text{ 层}
\quad(\rho_p\ge1).}
\tag{4.7}
\]

---

## 5. 两个 decimal carriers 都是 positive，而且几乎相等

沿用 endpoint normalized variables

\[
x=\frac{B}{N},
\qquad
y=\frac{10a_2}{N},
\qquad
s=9+y=\frac KN,
\]

\[
w=\frac{b_3}{T},
\qquad
\zeta=\frac{a_3}{T}.
\]

当前最危险 endpoint box 给

\[
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1,
\tag{5.1}
\]

\[
1<\zeta<\frac{251}{250},
\qquad
0<w<\frac{843}{1000},
\qquad
N=10^M\ge10^{11}.
\tag{5.2}
\]

由 (4.2)：

\[
\frac{\Delta_\omega}{TN}
=sw-(x+2)\zeta>0.
\tag{5.3}
\]

另外

\[
\frac{F_H(K)}{N^2}
=5s^2-\frac{36s}{N}+\frac{55}{N^2},
\tag{5.4}
\]

\[
\frac\beta{TN}
=x+2+\frac wN.
\tag{5.5}
\]

所以

\[
\boxed{
\frac{\mathcal E_\pm}{TN^3}
=\left(5s^2-\frac{36s}{N}+\frac{55}{N^2}\right)
\left(x+2+\frac wN\right)
\pm\frac{s}{N}
\left(sw-(x+2)\zeta\right).}
\tag{5.6}
\]

由 `s<10,w<843/1000`：

\[
0<\frac{s}{N}
\left(sw-(x+2)\zeta\right)
<\frac{843}{10N}.
\tag{5.7}
\]

对主项，使用 `s>2499/250`、`x+2>21/10`：

\[
\left[
5\left(\frac{2499}{250}\right)^2
-\frac{360}{10^{11}}
\right]\frac{21}{10}
-\frac{843}{10^{12}}
>1049.
\tag{5.8}
\]

而使用 `s<10`、`x+2<40/19`：

\[
\left(500+\frac{55}{10^{22}}\right)
\left(
\frac{40}{19}+\frac{843}{10^{14}}
\right)
+\frac{843}{10^{12}}
<1053.
\tag{5.9}
\]

因此得到统一 fixed window

\[
\boxed{
1049\,TN^3
<\mathcal E_-
<\mathcal E_+
<1053\,TN^3.}
\tag{5.10}
\]

特别地两者都严格为正，并且

\[
\boxed{
\mathcal E_\pm
\text{ 恰有 }m+3M+4\text{ 个十进制数字}.}
\tag{5.11}
\]

它们的差值则极小：

\[
\mathcal E_+-\mathcal E_-
=2K\Delta_\omega.
\]
由 `\Delta_omega<Kb_3`、`K<10N`、`b_3<843T/1000`：

\[
\boxed{
0<\mathcal E_+-\mathcal E_-
<\frac{843}{5}\,TN^2.}
\tag{5.12}
\]

相对 (5.10)，两个 `m+3M+4` 位正整数只在约 `1/N` 的相对尺度上分开。

---

## 6. deep resonance 的新 fixed-length depth bound

若

\[
\rho_p\ge1,
\]
则 (4.6)、(5.10) 给

\[
\boxed{
p^{2h+1}
<1053\cdot10^{m+3M}.}
\tag{6.1}
\]

更一般地，由 (4.5+)：

\[
\boxed{
p^{2h+\min(r_B,h,\rho_p)}
<1053\cdot10^{m+3M}.}
\tag{6.2}
\]

在 endpoint 的 low-`m` cone

\[
m\le\frac{6M}{11}
\]
中进一步得到

\[
\boxed{
p^{2h+1}
<1053\cdot10^{39M/11}
\qquad(\rho_p\ge1).}
\tag{6.3}
\]

这比只用 `J_H` 的 `h+1` 层 `4M`-scale bound 更直接地控制 deep equal-depth synchronization。

---

## 7. 当前 frontier

现在 equal-depth branch 可再分成：

\[
\boxed{
\begin{array}{ll}
\rho_p=0:&
\mathcal E_-\text{ 恰有 }h\text{ 层，}\mathcal E_+\text{ 至少 }2h\text{ 层};\\[1mm]
\rho_p\ge1:&
\mathcal E_-\text{ 恰有 }h\text{ 层，}\mathcal E_+\text{ 至少 }2h+1\text{ 层}.
\end{array}}
\tag{7.1}
\]

并且 `E_+,E_-` 是两个同样只有 `m+3M+4` 位、彼此极近的真实十进制正整数。

本文真正新增的信息不是 quadratic character，而是：

\[
\boxed{
\text{equal-depth projective resonance}
\Longrightarrow
\text{fixed-length near-equal decimal pair with asymmetric p-depth}.}
\tag{7.2}
\]

剩余困难也更精确了：`E_+` 当前只能读取到

\[
\min(r_B,h,\rho_p)
\]
层 resonance tail；若 `rho_p` 超过 `h` 或 `r_B`，(2.4) 中的 `A_H^2` / `B_W` 项会成为新的深度瓶颈。继续推进需要构造一个**二阶 corrected decimal carrier**，消掉该 `2h` 项，或把 `E_+/E_-` 的极窄 Archimedean gap 与其它 pure-prefix depth carrier 联立。
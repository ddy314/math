# A2 height companion oversaturation 回流到 `omega` content

> **依赖：** `spontaneous-height-resultant-parity.md`、`spontaneous-height-companion-cross.md`、`primitive-reduction.md`、`source-discriminant.md`、`spontaneous-height-parity-ledger.md`。
>
> **严格状态：**本文处理一个比 first-layer common height 更深的交叉情形：某 prime 的 `W_q` height exponent 已被共同 gcd `D_H` 完整吃掉，但 `J_H` 与 `B_W` 两个 companion 在该 prime 上仍同时继续加深。利用 cross linear gate 与 `qW_q=DK-N`，证明这种 oversaturation 必强迫 `p|omega`；于是 `B_W` 在 source triangle 上退化为固定 quadratic `6K^2-36K+55`。进一步把该 quadratic 拉回真实第三块，得到正定整数 `R_{omega H}=6(a_3+3T)^2+T^2`，并证明 `T^2 B_W-c_u^2R_{omega H}` 的精确 `p`-进赋值就是 `v_p(omega)`。本轮又恢复出 exact decimal content determinant `K b_3-Q a_3=2^{M+1}c_Q10^M omega`，并把 oversaturation 的共同深度进一步推到完全不含第三块、source 变量和 `K` 的 pure-prefix resultant `R_{omega H}^{pref}`；该整数恰有 `8M+2` 位，primitive part 为 `1 mod 8`。所有 genuine non-`3` roots 仍是 simple，且 inert prime 只能落在 `p=7,11 (mod 24)`。本文仍不排除所有 simple moving prefix roots，也不关闭 A2。

---

## 1. oversaturation setting

令

\[
D_H=\gcd(\mathscr B_W,W_q)=\gcd(\widehat J_H,W_q),
\]

\[
B^\circ=\mathscr B_W/D_H,
\qquad
J^\circ=\widehat J_H/D_H,
\qquad
W^\circ=W_q/D_H.
\]

固定 genuine non-`3` inert prime `p`，并假设：

1. `p|W_q`，所以它是真正 height-supported prime；
2. `p|B^circ`；
3. `p|J^circ`。

由于 `D_H` 已经是 `B_W` 与 `W_q` 的完整 gcd，`p|B^circ` 强迫 `D_H` 在 p 上已经吃掉 `W_q` 的全部 exponent。因此

\[
\boxed{p\nmid W^\circ.}
\tag{1.1}
\]

`spontaneous-height-companion-cross.md` 的 difference identity 于是给 cross linear gate

\[
\boxed{L_{JB}:=DzK+fN\equiv0\pmod p,}
\tag{1.2}
\]

在 genuine external/content-free denominator separation 下 `p\nmid qz`。

---

## 2. `L_JB` modulo `W_q` 精确回到 `omega K`

使用

\[
qW_q=DK-N,
\qquad
z=g\omega-c_u,
\qquad
f=g\omega+c_u.
\]

有 exact Euclidean identity

\[
\begin{aligned}
L_{JB}
&=DzK+f(DK-qW_q)\\
&=DK(z+f)-fqW_q\\
&=2Dg\omega K-fqW_q.
\end{aligned}
\]

所以

\[
\boxed{
L_{JB}=2Dg\omega K-fqW_q.}
\tag{2.1}
\]

若 `p|W_q` 且 `p|L_JB`：

\[
\boxed{p\mid2Dg\omega K.}
\tag{2.2}
\]

`primitive-reduction.md` 已证明 genuine non-`3` height prime 满足

\[
p\nmid2\cdot5\cdot g,
\]
故 `p\nmid D`。它还满足 `p\nmid a_3`。而

\[
TK+a_3=\omega W_q\equiv0\pmod p.
\]
若 `p|K`，则上式会给 `p|a_3`，矛盾。因此

\[
\boxed{p\nmid K.}
\tag{2.3}
\]

由 (2.2)：

\[
\boxed{p\mid\omega.}
\tag{2.4}
\]

所以 height-supported `J^circ/B^circ` oversaturation 不能留在 generic endpoint-external pool；它必回到 concatenation content `omega`。

---

## 3. `B_W` 在 omega-content 上退化为固定 quadratic

由 source triangle，模 `p|omega`：

\[
z=g\omega-c_u\equiv-c_u,
\]

\[
f=g\omega+c_u\equiv c_u.
\tag{3.1}
\]

而

\[
\mathscr B_W
=c_u^2(5K^2-36K+55)+z^2K^2.
\]

所以

\[
\boxed{
\mathscr B_W
\equiv
c_u^2(6K^2-36K+55)
\pmod p.}
\tag{3.2}
\]

height prime 与 `c_u` 分离，因此 `p|B_W` 等价于

\[
\boxed{
\mathcal P_{\omega H}(K)
:=6K^2-36K+55
\equiv0\pmod p.}
\tag{3.3}
\]

这是一条完全 source-ratio-free 的固定 K-quadratic。

---

## 4. 所有 non-3 roots 都是 simple

其 discriminant 为

\[
\boxed{
\operatorname{Disc}(\mathcal P_{\omega H})
=(-36)^2-4\cdot6\cdot55
=-24.}
\tag{4.1}
\]

因此 repeated root 只可能出现在

\[
p\mid24,
\]
即 `p=2` 或 `3`。所以

\[
\boxed{
\text{对所有 genuine non-`3` odd primes，}
\mathcal P_{\omega H}\text{ 的 root 都是 simple。}}
\tag{4.2}
\]

height-supported companion oversaturation 因此不存在新的 singular Hensel tree。

---

## 5. inert quadratic character 只是 source-discriminant shadow

对

\[
p\equiv3\pmod4,
\quad p\ne3,
\]
(3.3) 有 root iff

\[
\left(\frac{-24}{p}\right)=1.
\]
因为 `4` 为平方且 `(-1/p)=-1`：

\[
\boxed{
\left(\frac6p\right)=-1.}
\tag{5.1}
\]

另一方面 `source-discriminant.md` 给

\[
\mathscr D_W=55z^2-49c_u^2.
\]
模 `omega` 有 `z=-c_u`，因此

\[
\boxed{
\mathscr D_W\equiv6c_u^2\pmod\omega.}
\tag{5.2}
\]

所以对 `p|omega`：

\[
\boxed{
\left(\frac{\mathscr D_W}{p}\right)
=\left(\frac6p\right)=-1.}
\tag{5.3}
\]

这正是一般 external `B_W` root 已有的 discriminant nonresidue condition。故 (5.1) 不是新的 independent character；它只是 source triangle 在 omega-content 上的投影。

---

## 6. updated height cross ledger

height `J/B` cross-overlap 现在严格分成两类：

### A. `p\nmid W_q`

这是 `spontaneous-height-companion-cross.md` 的 generic residual overlap：

\[
\mathscr B_W=0,
\quad
DzK+fN=0,
\quad
\mathscr R_{JB}=0,
\]

只剩 positive norm / simple p-adic synchronization。

### B. `p\mid W_q`

若 height exponent 已经被 `D_H` 完整吃掉后 `J^circ,B^circ` 仍共同加深，则

\[
\boxed{p\mid\omega,}
\]
并且

\[
\boxed{6K^2-36K+55=0\pmod p}
\]
是 simple fixed quadratic。

因此

\[
\boxed{
\text{height-supported companion oversaturation}
\Longrightarrow
\text{simple omega-content orbit}.}
\tag{6.1}
\]

没有第三种 hidden prime-source mechanism。

---

## 7. fixed `K` quadratic 拉回真实第三块正定型

注意

\[
\mathcal P_{\omega H}(K)
=6(K-3)^2+1.
\tag{7.1}
\]

令

\[
\boxed{
\mathscr R_{\omega H}
:=6(a_3+3T)^2+T^2>0.
}
\tag{7.2}
\]

利用真实拼接 numerator

\[
\alpha=TK+a_3=\omega W_q,
\]
直接展开得到

\[
\boxed{
T^2\mathcal P_{\omega H}(K)-\mathscr R_{\omega H}
=6\alpha(TK-6T-a_3).
}
\tag{7.3}
\]

因此若

\[
e:=v_p(\omega),
\qquad
h:=v_p(W_q),
\]
则

\[
v_p(\alpha)=e+h,
\]
且

\[
\boxed{
T^2\mathcal P_{\omega H}(K)
\equiv\mathscr R_{\omega H}
\pmod{p^{e+h}}.
}
\tag{7.4}
\]

这一步把 moving `K` root 精确拉回真实第三块数字 `a_3`，没有引入新的自由变量。

---

## 8. `B_W` 与第三块正定型之间有 exact valuation bridge

由 `z=g\omega-c_u`，有精确展开

\[
\begin{aligned}
\mathscr B_W
&=c_u^2\mathcal P_{\omega H}(K)
+g\omega(g\omega-2c_u)K^2.
\end{aligned}
\tag{8.1}
\]

把 (7.3) 代入并使用 `\alpha=\omega W_q`：

\[
\boxed{
T^2\mathscr B_W-c_u^2\mathscr R_{\omega H}
=\omega\,\mathscr E_{\omega H},
}
\tag{8.2}
\]

其中

\[
\boxed{
\begin{aligned}
\mathscr E_{\omega H}:={}&
6c_u^2W_q(TK-6T-a_3)\\
&+gT^2K^2(g\omega-2c_u).
\end{aligned}}
\tag{8.3}
\]

在当前 oversaturation prime 上 `p|W_q`、`p|omega`，而

\[
p\nmid2g c_uTK.
\]
故

\[
\mathscr E_{\omega H}
\equiv-2gc_uT^2K^2\not\equiv0\pmod p.
\tag{8.4}
\]

于是得到精确赋值公式

\[
\boxed{
v_p\!\left(
T^2\mathscr B_W-c_u^2\mathscr R_{\omega H}
\right)
=v_p(\omega)=e.
}
\tag{8.5}
\]

这比模 `p` 的 quadratic gate 更强：`omega` content 的深度已经成为 `B_W` 与真实第三块正定型之间的精确距离。

---

## 9. oversaturation depth 必须由 `R_{omega H}` 支付

写

\[
V:=v_p(\mathscr B_W).
\]
由于 `D_H` 已完整吃掉 `W_q` 的 `p^h`，而 `p|B^circ`，有

\[
\boxed{V\ge h+1.}
\tag{9.1}
\]

又因 `p\nmid Tc_u`，由 (8.5) 对两个整数

\[
T^2\mathscr B_W,
\qquad
c_u^2\mathscr R_{\omega H}
\]
应用非阿基米德赋值，得到

\[
\boxed{
\begin{cases}
v_p(\mathscr R_{\omega H})=\min\{e,V\},&e\ne V,\\[2mm]
v_p(\mathscr R_{\omega H})\ge V,&e=V.
\end{cases}}
\tag{9.2}
\]

特别地统一有

\[
\boxed{
v_p(\mathscr R_{\omega H})
\ge\min\{e,h+1\}.}
\tag{9.3}
\]

于是出现一个干净的 depth dichotomy：

### shallow content: `e<=h`

此时 `e<V`，所以

\[
\boxed{v_p(\mathscr R_{\omega H})=e.}
\tag{9.4}
\]

`omega` 的全部 p-depth 在真实第三块正定型中被**精确读取**。

### deep content: `e>=h+1`

此时至少有

\[
\boxed{p^{h+1}\mid\mathscr R_{\omega H}.}
\tag{9.5}
\]

所以想让 companion 在完整 height exponent 之后继续加深一层，必须先让第三块正定型承担至少 `h+1` 层同一 prime power。

---

## 10. natural third-block root 仍然 simple，并得到显式高度上界

由 (9.3)，oversaturation 至少强迫

\[
p\mid\mathscr R_{\omega H}.
\]

若 `p|(a_3+3T)`，则 (7.2) 会给 `p|T`，不可能。因此

\[
p\nmid a_3+3T.
\]

把 `R_{omega H}` 看成 `a_3` 的 quadratic，其导数为

\[
12(a_3+3T),
\]
对 genuine non-`3` odd prime 是 unit。故

\[
\boxed{
\mathscr R_{\omega H}=0\pmod p
\text{ 在真实第三块坐标上也是 simple root。}}
\tag{10.1}
\]

再令 `u=a_3/T` 于模 `p` 中，则

\[
6(u+3)^2+1\equiv0\pmod p.
\]
对 `p=3 mod 4`、`p\ne3`，这等价于

\[
\left(\frac6p\right)=-1.
\]
按模 `24` 的四个可能类检查：

\[
\boxed{
p\equiv7\ \text{或}\ 11\pmod{24}.}
\tag{10.2}
\]

最后，第三分子有 `m+1` 位，因此

\[
T\le a_3<10T.
\]
于是

\[
4T\le a_3+3T<13T,
\]
从而

\[
\boxed{
97T^2\le\mathscr R_{\omega H}<1015T^2.
}
\tag{10.3}
\]

结合 (9.3)：

\[
\boxed{p^{\min(e,h+1)}
<1015\cdot10^{2m}.}
\tag{10.4}
\]

特别地每个 oversaturation prime 都满足

\[
\boxed{p<1015\cdot10^{2m}.}
\tag{10.5}
\]

---

## 11. `omega` 有一个 exact decimal determinant 读取器

令

\[
\boxed{E_M:=2^{M+1}c_Q.}
\tag{11.1}
\]

由 `primitive-reduction.md`：

\[
Q=E_Mq,
\qquad
S=E_MD,
\]

\[
\alpha=TK+a_3=\omega W_q,
\qquad
\beta=TQ+b_3=\omega S,
\]
以及

\[
qW_q=DK-N,
\qquad N=10^M.
\]

定义真实十进制 determinant

\[
\boxed{
\Delta_\omega:=Kb_3-Qa_3.
}
\tag{11.2}
\]

则

\[
\begin{aligned}
\Delta_\omega
&=K(\beta-TQ)-Q(\alpha-TK)\\
&=K\beta-Q\alpha\\
&=\omega(KS-QW_q)\\
&=E_M\omega(KD-qW_q)\\
&=E_MN\omega.
\end{aligned}
\]

因此得到 exact identity

\[
\boxed{
Kb_3-Qa_3
=2^{M+1}c_Q10^M\omega>0.
}
\tag{11.3}
\]

这给出严格的斜率方向

\[
\boxed{
\frac{a_3}{b_3}<\frac KQ.
}
\tag{11.4}
\]

在当前 oversaturation prime 上，`p|W_q` 与 `gcd(W_q,c_Q)=1` 给 `p\nmid c_Q`；又 `p\nmid10`。所以若

\[
e=v_p(\omega),
\]
则

\[
\boxed{v_p(\Delta_\omega)=e.}
\tag{11.5}
\]

也就是说 denominator content 的完整 `p`-depth 有一个不含 source quotient 的真实 decimal natural representative。

必须审计：`endpoint-lattice.md` §9 已经给出 `c_Q omega` 的 Hensel slot，因此 (11.3) 不能再被当作一个独立 source obstruction。它的新用途是**自然代表、符号和 Archimedean 大小**。

当前 endpoint 有

\[
K<10N,
\qquad
0<b_3<\frac{843}{1000}T.
\]
由 `Qa_3>0`：

\[
0<\Delta_\omega<Kb_3
<\frac{843}{100}NT.
\]
结合 (11.3)：

\[
\boxed{
0<\omega<
\frac{843}{100}\,
\frac{T}{2^{M+1}c_Q}.
}
\tag{11.6}
\]

故对 `p^e||omega`：

\[
\boxed{
p^e\le\omega<
\frac{843}{100}\,
\frac{10^m}{2^{M+1}c_Q}.}
\tag{11.7}
\]

由于 (10.2) 中最小可能 prime 为 `7`，任一 oversaturation state 还必须满足

\[
\boxed{
2^{M+1}c_Q
<\frac{843}{700}\,10^m.
}
\tag{11.8}
\]

这并不替代 endpoint 已有的 high/low-`m` cone，但它对**完整 content prime-power `p^e`**给出了比 (10.4) 更锋利的线性尺度上界。

---

## 12. height depth 也能投影成 pure-prefix quadratic

沿用

\[
B=b_2,
\qquad
Q=B+2N,
\qquad
N_0=\left(\frac{9B}{2}\right)^2+a_2^2.
\]

定义 pure-prefix positive integer

\[
\boxed{
\mathscr H_{\omega H}^{\rm pref}
:=B^2K^2+Q^2N_0>0.
}
\tag{12.1}
\]

`spontaneous-height-parity-ledger.md` 的 exact height square 为

\[
\boxed{
N_0b_3^2+B^2a_3^2
=\left(\frac{BH_0}{g}\right)^2,
\qquad
H_0=c_uW_q.
}
\tag{12.2}
\]

左边记为 `H_3`。因为当前 height prime 与 `B,c_u,g` 分离：

\[
\boxed{v_p(H_3)=2h.}
\tag{12.3}
\]

另一方面使用

\[
a_3=\alpha-TK,
\qquad
b_3=\beta-TQ
\]
直接展开：

\[
\boxed{
\begin{aligned}
T^2\mathscr H_{\omega H}^{\rm pref}
={}&H_3
+2T\left(B^2K\alpha+N_0Q\beta\right)\\
&-B^2\alpha^2-N_0\beta^2.
\end{aligned}}
\tag{12.4}
\]

又

\[
B^2K\alpha+N_0Q\beta
=\omega\left(B^2KW_q+N_0QS\right).
\]
因为 `p|W_q`，而 `p\nmid N_0QS`：

\[
\boxed{
v_p(B^2K\alpha+N_0Q\beta)=e.}
\tag{12.5}
\]

同时

\[
v_p(\alpha)=e+h,
\qquad
v_p(\beta)=e.
\]
所以从 (12.3)–(12.5) 得到精确 depth law：

\[
\boxed{
\begin{cases}
v_p(\mathscr H_{\omega H}^{\rm pref})=\min\{e,2h\},&e\ne2h,\\[2mm]
v_p(\mathscr H_{\omega H}^{\rm pref})\ge2h,&e=2h.
\end{cases}}
\tag{12.6}
\]

特别地

\[
\boxed{
v_p(\mathscr H_{\omega H}^{\rm pref})
\ge\min\{e,2h\}.}
\tag{12.7}
\]

第三块 height square 因而已经被投影成只依赖前两块的 quadratic gate。

---

## 13. `K` 也能完全消掉：pure-prefix resultant

记

\[
\mathcal P_{\omega H}(K)=6K^2-36K+55,
\]
并写

\[
X:=B^2,
\qquad
Y:=Q^2N_0.
\]
则

\[
\mathscr H_{\omega H}^{\rm pref}=XK^2+Y.
\]

由 (8.1)，若

\[
V=v_p(\mathscr B_W)\ge h+1,
\]
则 `g omega(g omega-2c_u)K^2` 的赋值精确为 `e`，故

\[
\boxed{
v_p(\mathcal P_{\omega H}(K))
\ge\min\{e,h+1\}.}
\tag{13.1}
\]

设

\[
\boxed{\ell_p:=\min\{e,h+1\}.}
\tag{13.2}
\]

由 `h>=1`，有 `2h>=h+1`；所以 (12.7) 与 (13.1) 给

\[
p^{\ell_p}\mid\mathcal P_{\omega H}(K),
\qquad
p^{\ell_p}\mid(XK^2+Y).
\tag{13.3}
\]

现在直接消去 `K`：

\[
\boxed{
\begin{aligned}
\mathscr R_{\omega H}^{\rm pref}
&:=\operatorname{Res}_K
\left(6K^2-36K+55,\ XK^2+Y\right)\\
&=3025X^2+636XY+36Y^2.
\end{aligned}}
\tag{13.4}
\]

定义线性 subresultant

\[
\boxed{
L_{\rm pref}
:=X\mathcal P_{\omega H}-6(XK^2+Y)
=-36XK+55X-6Y.
}
\tag{13.5}
\]

有 exact Bezout identity

\[
\boxed{
\begin{aligned}
\mathscr R_{\omega H}^{\rm pref}
={}&1296X(XK^2+Y)\\
&+2(55X-6Y)L_{\rm pref}-L_{\rm pref}^2.
\end{aligned}}
\tag{13.6}
\]

由 (13.3)，`p^{ell_p}` 同时整除 `XK^2+Y` 与 `L_pref`，所以

\[
\boxed{
p^{\ell_p}\mid\mathscr R_{\omega H}^{\rm pref}.}
\tag{13.7}
\]

这一步非常关键：

\[
\boxed{
\mathscr R_{\omega H}^{\rm pref}
=3025B^4
+636B^2Q^2N_0
+36Q^4N_0^2
}
\tag{13.8}
\]

已经完全不含

\[
a_3,b_3,\omega,W_q,K,q,f,g,c_u.
\]

因此 height-supported omega oversaturation 的 `ell_p` 层 prime-power 现在必须由**纯前两块 decimal integer**承担。

它还有两个 exact completion：

\[
\boxed{
\mathscr R_{\omega H}^{\rm pref}
=(55X-6Y)^2+1296XY,
}
\tag{13.9}
\]

以及

\[
\boxed{
\mathscr R_{\omega H}^{\rm pref}
=(6Y+53X)^2+6(6X)^2>0.
}
\tag{13.10}
\]

把 (13.4) 看成 `Y` 的 quadratic，其 discriminant 为

\[
\boxed{
\operatorname{Disc}_Y
\left(36Y^2+636XY+3025X^2\right)
=-31104X^2
=-6(72X)^2.
}
\tag{13.11}
\]

所以除 `2,3` 外所有 root 都是 simple。对 inert `p=3 mod4`，root 条件

\[
\left(\frac{-6}{p}\right)=1
\]
仍等价于

\[
\left(\frac6p\right)=-1,
\]
恰好还是 (10.2) 的 `p=7,11 mod24`。因此该 resultant **没有制造新的 Legendre obstruction**；它的新信息是 prime-power depth 已经脱离第三块并进入 pure prefix。

---

## 14. prefix resultant 恰有 `8M+2` 个十进制数字

`spontaneous-height-parity-ledger.md` 给

\[
B=2^{M+m+1}b_0,
\qquad
Q=2^{M+1}Q_0,
\]
其中 `b_0,Q_0,N_0` 均为奇数。由 (13.8) 三项的二进深度：

\[
4M+4m+4,
\qquad
4M+2m+6,
\qquad
4M+6,
\]
最浅项唯一为最后一项。因此

\[
\boxed{
v_2(\mathscr R_{\omega H}^{\rm pref})=4M+6.}
\tag{14.1}
\]

而 primitive quotient 精确为

\[
\begin{aligned}
\widehat{\mathscr R}_{\omega H}^{\rm pref}
={}&9Q_0^4N_0^2
+159\cdot2^{2m}b_0^2Q_0^2N_0\\
&+3025\cdot2^{4m-2}b_0^4.
\end{aligned}
\]

若 `m=1`，后两项各为 `4 mod8`；若 `m>=2`，后两项都为 `0 mod8`。首项恒为 `1 mod8`。故统一有

\[
\boxed{
\widehat{\mathscr R}_{\omega H}^{\rm pref}
\equiv1\pmod8.}
\tag{14.2}
\]

所以该 pure-prefix carrier 自身具有 even total inert parity。

现在再使用 endpoint box

\[
\frac1{10}<x:=\frac BN<\frac2{19},
\qquad
\frac{249}{250}<y:=\frac{10a_2}{N}<1,
\qquad
N=10^M,\ M\ge11.
\]

有

\[
\frac{N_0}{N^2}
=\frac{81}{4}x^2+\frac{y^2}{100}.
\]
直接由端点得到

\[
\frac{53}{250}
<\frac{N_0}{N^2}
<\frac{8461}{36100}.
\tag{14.3}
\]

又 `Q/N=x+2`，于是对 `Y=Q^2N_0`：

\[
\boxed{
\frac{93}{100}N^4
<Y
<\frac{26}{25}N^4.}
\tag{14.4}
\]

同时

\[
0<X=B^2<\frac4{361}N^2.
\tag{14.5}
\]

由 (13.4) 下界：

\[
\mathscr R_{\omega H}^{\rm pref}
>36\left(\frac{93}{100}\right)^2N^8
>31N^8.
\tag{14.6}
\]

上界则为

\[
\begin{aligned}
\mathscr R_{\omega H}^{\rm pref}
<&36\left(\frac{26}{25}\right)^2N^8\\
&+636\frac4{361}\frac{26}{25}N^6
+3025\left(\frac4{361}\right)^2N^4.
\end{aligned}
\]

第一项系数为 `38.9376`；而 `N>=10^11` 时后两项相对 `N^8` 小于 `10^{-20}`。因此严格有

\[
\boxed{
31N^8
<\mathscr R_{\omega H}^{\rm pref}
<39N^8.}
\tag{14.7}
\]

由于 `N=10^M`：

\[
\boxed{
\mathscr R_{\omega H}^{\rm pref}
\text{ 恰有 }8M+2\text{ 个十进制数字}.}
\tag{14.8}
\]

综合 (11.7)、(13.7)、(14.2)、(14.8)，height-supported omega oversaturation 现在必须同时满足

\[
\boxed{
\begin{gathered}
p\equiv7,11\pmod{24},\\
p^e\le\omega<
\dfrac{843}{100}\dfrac{10^m}{2^{M+1}c_Q},\\
p^{\min(e,h+1)}\mid
\mathscr R_{\omega H}^{\rm pref},\\
\mathscr R_{\omega H}^{\rm pref}>0,
\quad
\dfrac{\mathscr R_{\omega H}^{\rm pref}}{2^{4M+6}}\equiv1\pmod8,\\
31\cdot10^{8M}
<\mathscr R_{\omega H}^{\rm pref}
<39\cdot10^{8M}.
\end{gathered}}
\tag{14.9}
\]

这仍不是 A2 closure：`R_pref` 的 simple root 可以随前两块移动，且其 `1 mod8` orientation 只控制总 inert parity，不能保证指定 oversaturation prime 的实际赋值 parity。但当前 orbit 已从 third-block/source Hensel synchronization 进一步压成一个**固定十进制长度的 pure-prefix simple norm**。下一步必须研究它与其它 pure-prefix carriers（尤其 `Delta_0`、`C_omega` 或 `J_H` 的自然代表）的 gcd/resultant，而不能继续叠同一个 `sqrt(-6)` quadratic character。

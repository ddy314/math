# A2 height companion oversaturation 回流到 `omega` content

> **依赖：** `spontaneous-height-resultant-parity.md`、`spontaneous-height-companion-cross.md`、`primitive-reduction.md`、`source-discriminant.md`。
>
> **严格状态：**本文处理一个比 first-layer common height 更深的交叉情形：某 prime 的 `W_q` height exponent 已被共同 gcd `D_H` 完整吃掉，但 `J_H` 与 `B_W` 两个 companion 在该 prime 上仍同时继续加深。利用 cross linear gate 与 `qW_q=DK-N`，证明这种 oversaturation 必强迫 `p|omega`；于是 `B_W` 在 source triangle 上退化为固定 quadratic `6K^2-36K+55`。进一步把该 quadratic 拉回真实第三块，得到正定整数 `R_{omega H}=6(a_3+3T)^2+T^2`，并证明 `T^2 B_W-c_u^2R_{omega H}` 的精确 `p`-进赋值就是 `v_p(omega)`。因此 oversaturation 的 prime-power 深度必须由这个真实第三块正定型支付；所有 non-`3` roots 都是 simple，且 inert prime 只能落在 `p=7,11 (mod 24)`。本文仍不排除所有 simple omega roots，也不关闭 A2。

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
\boxed{
p^{\min(e,h+1)}
<1015\cdot10^{2m}.}
\tag{10.4}
\]

特别地每个 oversaturation prime 都满足

\[
\boxed{p<1015\cdot10^{2m}.}
\tag{10.5}
\]

因此该 channel 已从“任意 simple omega-content root”进一步压成：

\[
\boxed{
\begin{gathered}
p\equiv7,11\pmod{24},\\
p^{\min(v_p(\omega),v_p(W_q)+1)}\mid
6(a_3+3T)^2+T^2,\\
6(a_3+3T)^2+T^2<1015T^2.
\end{gathered}}
\tag{10.6}
\]

这仍不是全局空性，因为 `m` 无界且 simple p-adic roots 可以随第三块移动；但 hidden singular tree 与无代价的 prime-power 加深都已经被排除。后续若要关闭这一 orbit，需要把 (10.6) 与 `omega=gcd(alpha,beta)` 的 denominator content depth 或其它 independent natural representative 联立，而不能继续只叠 quadratic character。

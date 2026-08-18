# A2 spontaneous/additive denominator common-carrier bridge

> **依赖：** `spontaneous-angle.md`、`spontaneous-angle-overlap-depth.md`、`spontaneous-angle-parity.md`、`spontaneous-prefix-eliminant.md`、`endpoint-lattice.md` §§16.56–16.72。
>
> **严格状态：**本文把 angle primitive carrier 与 additive cofactor 的 denominator pool 对齐。核心结论是：additive denominator odd excess 只能出现在完整 prime-power saturation `p^e || qf, p^e | L_23`；若同一个 prime 还属于 angle/additive common gcd，则它自动落回旧 denominator-prefix excess `Psi_f = Delta_0 = 0`。q-side 随即降为一个永远 simple 的 decimal-length quadratic；f-side 降为一个固定 octic，其 genuine non-3 inert singular Hensel tree 为空。本文不证明所有 simple common roots 都不存在，也不宣称 A2 全局关闭。

---

## 1. additive denominator odd excess 只剩完整 saturation

沿用 `endpoint-lattice.md` 的

\[
\mathscr L_{23}:=\frac{9T}{2}+a_3.
\]

旧共同-kernel 审计已经严格证明

\[
\gcd(\mathscr D_Z,qf)=\gcd(\mathscr L_{23}^2,qf),
\]
以及逐素数赋值律：若

\[
p^e\Vert qf,
\]
则

\[
\min\{v_p(\mathscr D_Z),e\}
=\min\{2v_p(\mathscr L_{23}),e\}.
\]

所以未饱和层全部以偶深度进入；non-`3` inert denominator prime 若要承担 additive odd excess，只能进入

\[
\boxed{
p^e\Vert qf,
\qquad
p^e\mid\mathscr L_{23}.}
\tag{1.1}
\]

因为 `p` 为奇素数，(1.1) 等价于

\[
\boxed{p^e\mid 2a_3+9T.}
\tag{1.2}
\]

本文从这个已经严格建立的 saturation 层开始，不重新收费未饱和 denominator contact。

---

## 2. `已严格完成`：common carrier 自动落回 `Psi_f`

记

\[
B=b_2,
\qquad
Q=2\cdot10^M+B,
\qquad
K=9\cdot10^M+10a_2,
\]

以及 pure f-prefix polynomial

\[
\boxed{
\Psi_f=B^2(K^2-26)-Q^2N_0.}
\tag{2.1}
\]

`spontaneous-prefix-eliminant.md` 已证明 exact identity

\[
\boxed{
\Theta_{\rm dec}
=T\Psi_f
-B^2(2K-9)(2a_3+9T).
}
\tag{2.2}
\]

现在设 genuine odd inert prime `p` 同时满足：

- denominator saturation (1.2)；
- additive contact `p | Theta_dec`。

由于 `p \nmid T`，(2.2) 模 `p` 立即给

\[
\boxed{p\mid\Psi_f.}
\tag{2.3}
\]

所以 additive denominator saturation 一旦真正进入 common gcd，就自动命中旧 denominator-prefix polynomial；没有新的第四种 denominator source。

---

## 3. `已严格完成`：angle denominator contact 自动落回 `Delta_0`

使用 normalized prefix variables

\[
x=\frac{B}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}},
\]
以及

\[
\boxed{
\Delta_0:=2025x^2-18y-y^2.}
\tag{3.1}
\]

### q-side

source formula 为

\[
q=\frac{U(x+2)}{2c_Q}.
\]
对 genuine q-prime，`U,2c_Q` 为单位，所以

\[
p\mid q\Longrightarrow x+2\equiv0\pmod p.
\]
`spontaneous-angle.md` 的 exact q-side identity 为

\[
\Omega_{\rm sp}(-2,y,r_s)=400r_s\Delta_0(-2,y).
\]
因此 genuine `p | q,Omega_sp` 给

\[
\boxed{p\mid\Delta_0.}
\tag{3.2q}
\]

### f-side

令

\[
F_f:=r_s(x+2)+2x.
\]
旧 exact Bezout identity 为

\[
\boxed{
(x+2)\Omega_{\rm sp}
-A_{\rm sp}F_f
=-200x^3\Delta_0.}
\tag{3.3}
\]

对 genuine `p | f`，`F_f=0` 且 `x(x+2)A_sp` 为单位，所以 `p | Omega_sp` 同样强迫

\[
\boxed{p\mid\Delta_0.}
\tag{3.2f}
\]

因此任何 denominator common carrier 必满足统一三重接触

\[
\boxed{
p\mid qf,
\qquad
p\mid\Psi_f,
\qquad
p\mid\Delta_0.}
\tag{3.4}
\]

这正是旧 denominator-prefix excess 与新的 angle/additive common gcd 的交界。

---

# q-side

## 4. `已严格完成`：q common overlap 只剩一个 decimal-length quadratic

令

\[
N:=10^M,
\qquad
\tau=N^{-1},
\qquad
s:=9+y.
\]

q-line 给

\[
x=-2\pmod p.
\tag{4.1}
\]

由 `Delta_0=0`：

\[
8100-18y-y^2=0,
\]
即

\[
\boxed{s^2=(y+9)^2=8181=3^4\cdot101.}
\tag{4.2}
\]

另一方面 q-line 上

\[
Q=N(x+2)\equiv0\pmod p.
\]
由 `Psi_f=0` 与 genuine `p \nmid B`：

\[
\boxed{K^2\equiv26\pmod p.}
\tag{4.3}
\]

而 exact decimal identity

\[
K=N(9+y)=Ns
\]
把 (4.2)–(4.3) 合成

\[
\boxed{
\mathcal R_q(N)
:=8181N^2-26
\equiv0\pmod p.}
\tag{4.4}
\]

所以 q-side saturated common overlap 的 length coordinate 已完全从 `x,y,r_s,a_3,b_3` 中消去。

---

## 5. `已严格完成`：q-side length root 对所有 genuine odd prime都 simple

\[
\mathcal R_q'(N)=2\cdot8181N.
\]

若某 odd prime同时满足

\[
\mathcal R_q(N)\equiv
\mathcal R_q'(N)\equiv0\pmod p,
\]
由于 `N=10^M` 为 `p`-进单位，只能有

\[
p\mid8181.
\]
但原方程随后要求

\[
p\mid26.
\]
而

\[
\gcd(8181,26)=1.
\]
矛盾。因此

\[
\boxed{
\text{q-side common length root 对每个 genuine odd prime 都是 simple。}}
\tag{5.1}
\]

不存在 q-side 新 singular decimal Hensel tree。

第一层还立即给两个 independent split conditions：`Delta_0` 的 y-discriminant 是

\[
18^2+4\cdot8100=324\cdot101,
\]
所以 genuine root 要求

\[
\boxed{\left(\frac{101}{p}\right)=1.}
\tag{5.2}
\]

而 (4.3) 要求

\[
\boxed{\left(\frac{26}{p}\right)=1.}
\tag{5.3}
\]

这些只是必要 character，不单独构成 closure。

---

# f-side

## 6. `已严格完成`：f-line、angle 与 saturation 显式固定第三块

f-line 为

\[
F_f=r_s(x+2)+2x=0.
\]
由

\[
r_s=\frac{x}{\bar w},
\qquad
\bar w:=\frac{b_3}{T10^M},
\]
得到

\[
\boxed{\bar w=-\frac{x+2}{2}.}
\tag{6.1}
\]

saturation (1.2) 在 normalized third numerator

\[
\bar\zeta:=\frac{a_3}{T10^M}
\]
中写成

\[
\boxed{2\bar\zeta+9\tau=0,
\qquad
\bar\zeta=-\frac92\tau.}
\tag{6.2}
\]

angle contact又给 `Delta_0=0`。

exact sphere 为

\[
x^2\bar w^2(s+\bar\zeta)^2
=(x+2+\bar w)^2
\left(
\frac{2025x^2+y^2}{100}\bar w^2
+x^2\bar\zeta^2
\right).
\tag{6.3}
\]

在 `Delta_0=0` 上

\[
2025x^2+y^2=2ys.
\tag{6.4}
\]

把 (6.1)–(6.4) 代入并约去 genuine units，得到线性 saturation sphere target

\[
\boxed{
\mathcal L_f^{\rm sat}
:=200x^2(s-9\tau)-y(x+2)^2
=0.}
\tag{6.5}
\]

另一方面 `Psi_f=0` 除以 `B^2N^2` 后是

\[
\boxed{
\mathcal P_f
:=100x^2(s^2-26\tau^2)
-(x+2)^2(2025x^2+y^2)
=0.}
\tag{6.6}
\]

所以 f-side common saturation 的第三块和 source ratio 已经完全消失，只剩

\[
\boxed{
\Delta_0=0,
\qquad
\mathcal L_f^{\rm sat}=0,
\qquad
\mathcal P_f=0.}
\tag{6.7}
\]

---

## 7. `已严格完成`：f-side 最终只剩一个固定 octic

先对 `tau` 消去 (6.5)–(6.6)，再对 `y` 与 `Delta_0` 消元。exact resultant 为

\[
\boxed{
\operatorname{Res}_y
\left(
\Delta_0,
\operatorname{Res}_{\tau}(\mathcal P_f,\mathcal L_f^{\rm sat})
\right)
=164025000000\,x^8\mathcal F_{f,\rm sat}(x),}
\tag{7.1}
\]

其中整体符号依 resultant convention 可改变，而 primitive octic 为

\[
\boxed{
\begin{aligned}
\mathcal F_{f,\rm sat}(x)={}&
1150871947369x^8
-233661590896x^7\\
&-130208799184x^6
+3933739968x^5\\
&-5129302560x^4
+594074368x^3\\
&+85765888x^2
+2675712x
+389376.
\end{aligned}}
\tag{7.2}
\]

因此 genuine `p \nmid 2\cdot3\cdot5\cdot x` 的 f-side common carrier 必满足

\[
\boxed{\mathcal F_{f,\rm sat}(x)\equiv0\pmod p.}
\tag{7.3}
\]

这把 denominator common overlap 从四变量系统降为一条固定 degree-8 prefix curve。

---

## 8. `有限 exact 证书`：真实 endpoint interval 内没有 octic root

真实 denominator defect 为

\[
u:=10x-1=\frac{H}{5^{M-1}},
\qquad
0<u<\frac1{19}.
\]

令

\[
\mathcal F_{H,\rm sat}(u)
:=10^8\mathcal F_{f,\rm sat}\left(\frac{1+u}{10}\right).
\]

Sturm exact root count 给

\[
\boxed{
\#\{u\in(0,1/19):\mathcal F_{H,\rm sat}(u)=0\}=0.}
\tag{8.1}
\]

而两个端点函数值均为正。因此 f-side common overlap 与此前其它 moving branches 一样，没有 Archimedean root；任何 surviving state 都只能来自真正的 p-adic wrapping。

---

## 9. `有限 exact 证书`：f-side common octic 没有 genuine inert singular root

其整数判别式精确分解为

\[
\boxed{
\begin{aligned}
\operatorname{Disc}(\mathcal F_{f,\rm sat})={}&
2^{114}3^{20}5^{22}11^6 13^3 41^4 101^8 181^2\\
&\cdot5927^2\cdot197377693^2\cdot326937937\cdot1484772181.
\end{aligned}}
\tag{9.1}
\]

所有显示的大因子均为素数。限制到 non-`3` inert primes `p=3 mod 4`，只有

\[
\boxed{p=11,\ 5927}
\tag{9.2}
\]
需要审计。

### p=11

\[
\gcd(\mathcal F_{f,\rm sat},\mathcal F_{f,\rm sat}')
\equiv(x+2)^3\pmod{11}.
\]
唯一 repeated x-root 是

\[
x=-2.
\]
但 f-line 在该点为

\[
F_f=r_s(x+2)+2x=-4\not\equiv0\pmod{11}.
\]
所以它是 q-boundary，不是 genuine f-state。

### p=5927

`5927` 整除 octic leading coefficient，故判别式因 degree drop 含该素数；但有限域中

\[
\boxed{
\gcd(\mathcal F_{f,\rm sat},\mathcal F_{f,\rm sat}')=1
\quad\text{in }\mathbf F_{5927}[x].}
\tag{9.3}
\]

所以没有 finite repeated root。

因此

\[
\boxed{
\text{f-side saturated common overlap 不存在 genuine non-3 inert singular Hensel tree。}}
\tag{9.4}
\]

所有 genuine f-side common roots 都是 simple moving roots。

---

## 10. denominator parity 图的更新

现在 additive 与 angle 的 denominator pools 已对齐到同一旧接口：

\[
\boxed{
\text{saturated additive denominator}
+\text{angle contact}
\Longrightarrow
qf\cap\Psi_f\cap\Delta_0.}
\tag{10.1}
\]

并且 common part 的局部几何已经完全正规化：

\[
\boxed{
\begin{array}{c|c|c}
\text{channel}&\text{common reduced object}&\text{singular tree}\\ \hline
q&8181\cdot10^{2M}-26&\text{none}\\
f&\mathcal F_{f,\rm sat}(x)&\text{none genuine inert}
\end{array}}
\tag{10.2}
\]

所以 denominator pool 后续不应再做 singular-prime hunting。真正未闭合的是 **simple depth/parity synchronization**：比较

\[
\min\{v_p(\Omega_{\rm sp}),e\}
=\min\{v_p(\Delta_0),e\}
\]
与 additive saturation 的

\[
\min\{v_p(\mathscr D_Z),e\}
=\min\{2v_p(\mathscr L_{23}),e\},
\]
其中 `p^e || qf`。若能证明 simple q/f roots 的 residual parity 在两侧相同，或其差总为偶数，就可从 `G_sp mod 4` dichotomy 中消去 denominator residual branch。本文尚未证明这一最后 parity equality。

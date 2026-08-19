# A2 `H_4` coefficient singularity 的统一 short degree-4 prefix carrier

> **依赖：** `spontaneous-crt-pure-h4-projective-center.md`、`spontaneous-crt-pure-h4-prefix.md`。
>
> **严格状态：**generic `H_4` coefficient singularity已固定 projective norm ratio `c/s^2=3097/1296 mod p`。本文直接清去 `c,s` 的定义，得到一个统一 7 项、degree-4、irreducible pure-prefix carrier `V_4(x,y)`；两张 sphere orientation不再需要各自的 degree-32/40 numerator。`V_4` 与全部 principal old prefix gates互素，并在真实 dangerous endpoint上严格为负且 `43000<-V_4<86000`。因此 generic low coefficient singularity由一个固定符号的 short normalized prefix integer读取。本文尚未把所需 p-depth与该 height窗口联立到矛盾，因此不关闭 A2。

---

## 1. clear the fixed projective center

上一文件证明：除 fixed coefficient exceptions `p|E_4` 外，`H_4` singular branch满足

\[
\boxed{
\frac{c}{s^2}\equiv\frac{3097}{1296}\pmod p,}
\tag{1.1}

其中

\[
s=9+y,
\]

\[
c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.
\]

清分母：

\[
1296(x+2)^2(2025x^2+y^2)
-309700x^2(9+y)^2
\equiv0\pmod p.
\tag{1.2}

左边恰有固定因子 `4`。定义 primitive carrier

\[
\boxed{
\begin{aligned}
\mathscr V_4(x,y):={}&
656100x^4+2624400x^3\\
&-77101x^2y^2-1393650x^2y\\
&-3647025x^2+1296xy^2+1296y^2.
\end{aligned}}
\tag{1.3}

于是 generic `H_4` singular prime满足

\[
\boxed{p\mid\mathscr V_4(x,y).}
\tag{1.4}

两张 sphere orientation都读入同一个 `V_4`；此前 degree-32/40 branch numerators只是 `h_4(u_i)=0` 的另一投影。

---

## 2. irreducible and independent of all old gates

exact factorization over `Q[x,y]` 给

\[
\boxed{\mathscr V_4\text{ irreducible}.}
\tag{2.1}

并且

\[
\boxed{\deg\mathscr V_4=4,\qquad \#\operatorname{supp}(\mathscr V_4)=7.}
\tag{2.2}

对 principal old prefix gates

\[
d:=225x^2-y,
\]

\[
A_{sp}=4d^2-xy^2(99x-4),
\]

\[
A_-=A_{sp}-2y^2(x+2)^2,
\]

\[
A_+=202500x^4+99x^2y^2-4xy^2-4y^2,
\]

\[
\Delta_0=2025x^2-18y-y^2,
\]
以及 `C_*`，全部有

\[
\boxed{
\gcd(\mathscr V_4,F)=1.}
\tag{2.3}

所以这个 short quartic不是 source/common-alpha/prefix-defect/branch-collision 的旧 component。

---

## 3. exact normalized identity

由 `c/s^2` 定义可重写 (1.3)：

\[
\boxed{
\mathscr V_4
=25x^2s^2
\left(
1296\frac{c}{s^2}-3097
\right).}
\tag{3.1}

这给 real sign与 height一个无损接口。

---

## 4. fixed negative window on the dangerous endpoint

上一文件已证明

\[
0<\frac{c}{s^2}<\frac{21}{20}.
\]

所以括号严格为负：

\[
1296\frac{c}{s^2}-3097
<1296\frac{21}{20}-3097
=-\frac{8681}{5}.
\]

结合

\[
x>1/10,
\qquad
s>2499/250,
\]
得到

\[
-\mathscr V_4
>
25\left(\frac1{10}\right)^2
\left(\frac{2499}{250}\right)^2
\frac{8681}{5}
=
\frac{54212853681}{1250000}
>43000.
\tag{4.1}

另一方面只用 `c/s^2>0`：

\[
-\mathscr V_4
<25x^2s^2\cdot3097.
\]

而

\[
x<2/19,
\qquad
s<10,
\]
故

\[
-\mathscr V_4
<25\frac4{361}\cdot100\cdot3097
=\frac{1630000}{19}
<86000.
\tag{4.2}

所以整个 dangerous endpoint上有统一 fixed window：

\[
\boxed{
43000<-\mathscr V_4(x,y)<86000.}
\tag{4.3}

这是 normalized prefix scale；若清回原整数 `x=B/N,y=10A/N`，相应 numerator是 `N^4` 级别的 7 项 integer carrier。

---

## 5. integer clearing

把

\[
x=B/N,
\qquad y=10A/N
\]
代入并乘 `N^4`，得到 ordinary integer

\[
\boxed{
\begin{aligned}
V_4^{int}:={}&
656100B^4+2624400B^3N\\
&-7710100B^2A^2-13936500B^2AN\\
&-3647025B^2N^2+129600BA^2N\\
&+129600A^2N^2.
\end{aligned}}
\tag{5.1}

并且

\[
\boxed{V_4^{int}=N^4\mathscr V_4.}
\tag{5.2}

所以 generic `H_4` singular prime满足

\[
\boxed{p\mid V_4^{int}.}
\tag{5.3}

而 real size为

\[
\boxed{
43000N^4<-V_4^{int}<86000N^4.}
\tag{5.4}

因此 low coefficient singularity已经拥有一个真正可用于 prime-product budget的短 ordinary integer carrier。

---

## 6. revised low-singular frontier

除 fixed coefficient exceptions `p|E_4` 外，`H_4` branch现在同时满足：

1. `h_4(z/s)=0`；
2. `c/s^2=3097/1296 mod p`；
3. `p|V_4^{int}`；
4. `V_4^{int}` 的实值固定为 negative `O(10^5 N^4)`；
5. `V_4` 与所有 principal old prefix gates互素。

这比 degree-32/40 branch-specific curve更适合后续全局 budget。下一步若能证明 coefficient-singular common depth至少是二层或半深度，可立刻将其 product收费到 `V_4^{int}`；若只有 first layer，仍需和 parity/product ledger联立。

A2 仍为 `待证`。

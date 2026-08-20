# A2 moving height central exception 的 `23`-norm 与 source-signed quartic

> **依赖：** `spontaneous-height-sign-companion-shadow.md`、`spontaneous-height-parity-ledger.md`、`height-cofactor.md`。
>
> **严格状态：**same-sign companion audit 留下显式 central support `p|(2K-9)`。本文单独处理该 branch。height/additive common condition `B_W=0` 立即给 `(9rho)^2=23 mod p`，所以 genuine inert central prime必须满足 `(23/p)=1`，等价于 `(p/23)=-1`。把 central relation送入两张 decimal height orientations后，所得两个 degree-8 resultants都精确是 `Q(sqrt(23))` 的 quartic norm；其 exceptional common-root resultants不产生任何 `(23/p)=-1` 之外的新 character。保留 `sqrt(23)=±9rho` 后，每张 orientation进一步化成 source-signed quartic `A_i±9rho B_i=0`。因此 central branch不再是未分类的 sign-companion exception；它被压成固定 quadratic field中的显式 source/decimal orbit。本文不证明这些 quartic orbit为空。

---

## 1. central condition fixes the source square root of `23`

固定 genuine endpoint-external height/common prime

\[
p\equiv3\pmod4,
\qquad p\ne3,5,
\]
并进入 central support

\[
\boxed{2K-9\equiv0\pmod p.}
\tag{1.1}

于是

\[
K\equiv\frac92\pmod p.
\]

height resultant

\[
\mathscr B_W
=c_u^2F_W(K)+(q5^\lambda K)^2
=c_u^2\left[F_W(K)+\rho^2K^2\right],
\]
其中

\[
\rho:=\frac{q5^\lambda}{c_u}.
\]

central point上

\[
F_W(9/2)=-\frac{23}{4},
\qquad
K^2=\frac{81}{4}.
\]
所以 `p|B_W` 等价于

\[
\boxed{81\rho^2\equiv23\pmod p.}
\tag{1.2}

特别地 `rho` 是 unit，故 `p!=23`，并且

\[
\boxed{\left(\frac{23}{p}\right)=1.}
\tag{1.3}

因为 `p` 与 `23` 都为 `3 mod4`，二次互反律给

\[
\boxed{\left(\frac p{23}\right)=-1.}
\tag{1.4}

这与旧 height/saturation character一致。

---

## 2. central relation in normalized decimal coordinates

写

\[
x:=B/N_{\rm dec},
\qquad
y:=10A/N_{\rm dec},
\qquad
\tau:=N_{\rm dec}^{-1}.
\]

因为

\[
K=N_{\rm dec}(y+9),
\]
central condition (1.1) becomes

\[
\boxed{2(y+9)=9\tau.}
\tag{2.1}

moving additive-height polynomial为

\[
G_H=100x^2\left[5(y+9)^2-36(y+9)\tau+55\tau^2\right]
-(x+2)^2(2025x^2+y^2).
\]
代入 (2.1)：

\[
\boxed{G_H=-\frac1{81}\,C_{23}(x,y),}
\tag{2.2}

其中

\[
\boxed{
\begin{aligned}
C_{23}:={}&164025x^4+656100x^3+2381x^2y^2+41400x^2y\\
&+842400x^2+324xy^2+324y^2.
\end{aligned}}
\tag{2.3}

所以 central moving system只需研究

\[
H_i=C_{23}=0.
\]

---

## 3. orientation `H_1`: degree-8 resultant is a `23`-norm

第一 orientation

\[
H_1=202500x^4+(101x^2+4x+4)y^2.
\]
直接消去 `y`：

\[
\boxed{
\operatorname{Res}_y(H_1,C_{23})
=4100625x^4P_1(x),}
\tag{3.1}

其中

\[
\boxed{
\begin{aligned}
P_1={}&52862746561x^8-297975024x^7+3382320136x^6\\
&-1007998624x^5-296526576x^4+68673664x^3\\
&+46155008x^2+9850880x+2768896.
\end{aligned}}
\tag{3.2}

令

\[
D_1:=52862746561=229919^2,
\]

\[
\boxed{
\begin{aligned}
A_1={}&52862746561x^4-148987512x^3+2287110116x^2\\
&+681039760x+382854784,
\end{aligned}}
\tag{3.3}

\[
\boxed{
B_1=1655416800x^3+1636358400x^2-5328000x-2995200.}
\tag{3.4}

exact calculation gives

\[
\boxed{A_1^2-23B_1^2=D_1P_1.}
\tag{3.5}

所以 `P_1` 是一个显式 `Q(sqrt(23))` norm。

若 `(23/p)=-1` 且 `p∤D_1`，任何 `P_1(x)=0 mod p` 都会强迫

\[
A_1(x)=B_1(x)=0\pmod p.
\]
而

\[
\boxed{
\operatorname{Res}(A_1,B_1)
=2^{38}3^85^{12}13^2 19^6 23^2 101^2 12101^6.}
\tag{3.6}

`D_1=19*12101`。其中所有 `3 mod4` factors只有 `19,23`，且

\[
\left(\frac{23}{19}\right)=1,
\]
而 `23` 为 ramified prime。故不存在 genuine inert `(23/p)=-1` root。

因此 orientation `H_1` central root无条件满足

\[
\boxed{\left(\frac{23}{p}\right)=1.}
\tag{3.7}

与 source equation (1.2) 完全一致。

---

## 4. orientation `H_2`: the same quadratic field

第二 orientation消元为

\[
\boxed{
\operatorname{Res}_y(H_2,C_{23})
=269042006250000x^8(25x^2+1)^2P_2(x),}
\tag{4.1}

其中对 inert `p`，`25x^2+1=0` 无 root。剩余

\[
\boxed{
\begin{aligned}
P_2={}&36718521895561x^8+38488616399376x^7+56248633454536x^6\\
&+35159103841376x^5+26427713499024x^4+10019584910464x^3\\
&+4638014590208x^2+892499578880x+250864746496.
\end{aligned}}
\tag{4.2}

令

\[
D_2:=36718521895561=6059581^2,
\]

\[
\boxed{
\begin{aligned}
A_2={}&36718521895561x^4+19244308199688x^3+23396680107716x^2\\
&+6119130687760x+3439943737984,
\end{aligned}}
\tag{4.3}

\[
\boxed{
\begin{aligned}
B_2={}&-1003466613600x^3-1275716491200x^2\\
&-600588144000x-337627929600.
\end{aligned}}
\tag{4.4}

则

\[
\boxed{A_2^2-23B_2^2=D_2P_2.}
\tag{4.5}

并且

\[
\boxed{
\begin{aligned}
\operatorname{Res}(A_2,B_2)
={}&2^{36}3^{10}5^8 11^6 13^2 23^8 83^6 101^2\\
&\cdot251\cdot6637^6\cdot5419.
\end{aligned}}
\tag{4.6}

`D_2=11*83*6637`。所有显示的 `3 mod4` prime

\[
11,83,251,5419
\]
都满足

\[
\left(\frac{23}{p}\right)=1;
\]
`23` 自身仍为 ramified prime。因此同样不存在 genuine inert `(23/p)=-1` central root。

故

\[
\boxed{H_2\text{ central root}\Longrightarrow(23/p)=1.}
\tag{4.7}

---

## 5. keep the sign: source-signed quartics

source equation (1.2)给

\[
r:=9\rho,
\qquad r^2=23\pmod p.
\tag{5.1}

在任一 orientation，norm identity

\[
A_i^2-23B_i^2=0
\]
于是分成

\[
\boxed{A_i-rB_i=0}
\qquad\text{or}\qquad
\boxed{A_i+rB_i=0}
\pmod p.
\tag{5.2}

也就是

\[
\boxed{A_i(x)\pm9\rho B_i(x)=0\pmod p.}
\tag{5.3}

所以 central branch的真正剩余信息不是一个新的 Legendre symbol，而是一个带 source sign的 degree-4 decimal gate。

---

## 6. updated central frontier

central same-sign exception现在严格变成：

\[
\boxed{
(9\rho)^2=23,
\qquad
A_i(x)\pm9\rho B_i(x)=0,
\qquad i\in\{1,2\}.}
\tag{6.1}

第一式固定 quadratic field，第二式保留 source root sign并把它接到 decimal prefix。

因此继续只做 quadratic reciprocity不会增加约束；下一步若处理 central branch，应把 signed quartic与 `rho=z/c_u` 的 source triangle或 `W_q=alpha/omega` natural representative联立。
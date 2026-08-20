# A2-only Height Ledger

> 本文件是细粒度研究记录的机械归并账本。各来源的标题、正文和证明状态原样保留；账本中的局部闭合、有限证书或降级路线均不表示该分支或主不存在性命题已经关闭。

## 来源索引

- [`spontaneous-height-angle-additive-norm-bridge.md`](#source-spontaneous-height-angle-additive-norm-bridge)
- [`spontaneous-height-central-23-norm.md`](#source-spontaneous-height-central-23-norm)
- [`spontaneous-height-companion-cross.md`](#source-spontaneous-height-companion-cross)
- [`spontaneous-height-content-oversaturation.md`](#source-spontaneous-height-content-oversaturation)
- [`spontaneous-height-equal-depth-decimal-pair.md`](#source-spontaneous-height-equal-depth-decimal-pair)
- [`spontaneous-height-equal-depth-decimal-tropical-identity.md`](#source-spontaneous-height-equal-depth-decimal-tropical-identity)
- [`spontaneous-height-equal-depth-double-serial-budget.md`](#source-spontaneous-height-equal-depth-double-serial-budget)
- [`spontaneous-height-equal-depth-dual-short-carriers.md`](#source-spontaneous-height-equal-depth-dual-short-carriers)
- [`spontaneous-height-equal-depth-fixed-exception-transversality.md`](#source-spontaneous-height-equal-depth-fixed-exception-transversality)
- [`spontaneous-height-equal-depth-fixed-second-layer-squeeze.md`](#source-spontaneous-height-equal-depth-fixed-second-layer-squeeze)
- [`spontaneous-height-equal-depth-fixed2671-h1-squeeze.md`](#source-spontaneous-height-equal-depth-fixed2671-h1-squeeze)
- [`spontaneous-height-equal-depth-fixed7-audit.md`](#source-spontaneous-height-equal-depth-fixed7-audit)
- [`spontaneous-height-equal-depth-fixed7-h1-audit.md`](#source-spontaneous-height-equal-depth-fixed7-h1-audit)
- [`spontaneous-height-equal-depth-fixed7-h1-orthogonal-audit.md`](#source-spontaneous-height-equal-depth-fixed7-h1-orthogonal-audit)
- [`spontaneous-height-equal-depth-fixed7-hensel.md`](#source-spontaneous-height-equal-depth-fixed7-hensel)
- [`spontaneous-height-equal-depth-four-sheet-split.md`](#source-spontaneous-height-equal-depth-four-sheet-split)
- [`spontaneous-height-equal-depth-geometric-selector.md`](#source-spontaneous-height-equal-depth-geometric-selector)
- [`spontaneous-height-equal-depth-global-decimal-gcd.md`](#source-spontaneous-height-equal-depth-global-decimal-gcd)
- [`spontaneous-height-equal-depth-middle-near-pair.md`](#source-spontaneous-height-equal-depth-middle-near-pair)
- [`spontaneous-height-equal-depth-mod24-parity.md`](#source-spontaneous-height-equal-depth-mod24-parity)
- [`spontaneous-height-equal-depth-orthogonal-decimal-norm.md`](#source-spontaneous-height-equal-depth-orthogonal-decimal-norm)
- [`spontaneous-height-equal-depth-resonance.md`](#source-spontaneous-height-equal-depth-resonance)
- [`spontaneous-height-equal-depth-serial-conjugates.md`](#source-spontaneous-height-equal-depth-serial-conjugates)
- [`spontaneous-height-equal-depth-serial-gcd-selectors.md`](#source-spontaneous-height-equal-depth-serial-gcd-selectors)
- [`spontaneous-height-equal-depth-serial-parity-neutrality.md`](#source-spontaneous-height-equal-depth-serial-parity-neutrality)
- [`spontaneous-height-equal-depth-serial-tropical-bridge.md`](#source-spontaneous-height-equal-depth-serial-tropical-bridge)
- [`spontaneous-height-equal-depth-source-orientation.md`](#source-spontaneous-height-equal-depth-source-orientation)
- [`spontaneous-height-equal-depth-square-core.md`](#source-spontaneous-height-equal-depth-square-core)
- [`spontaneous-height-equal-depth-tail-gcd-ladder.md`](#source-spontaneous-height-equal-depth-tail-gcd-ladder)
- [`spontaneous-height-equal-depth-tail-imbalance.md`](#source-spontaneous-height-equal-depth-tail-imbalance)
- [`spontaneous-height-equal-depth-tail-normalization.md`](#source-spontaneous-height-equal-depth-tail-normalization)
- [`spontaneous-height-equal-depth-tail-reader.md`](#source-spontaneous-height-equal-depth-tail-reader)
- [`spontaneous-height-equal-depth-tail-source-separation.md`](#source-spontaneous-height-equal-depth-tail-source-separation)
- [`spontaneous-height-equal-depth-target-ladder.md`](#source-spontaneous-height-equal-depth-target-ladder)
- [`spontaneous-height-equal-depth-target-selector.md`](#source-spontaneous-height-equal-depth-target-selector)
- [`spontaneous-height-equal-depth-three-cancellation-readers.md`](#source-spontaneous-height-equal-depth-three-cancellation-readers)
- [`spontaneous-height-equal-depth-triple-orientation.md`](#source-spontaneous-height-equal-depth-triple-orientation)
- [`spontaneous-height-equal-depth-tropical-balance.md`](#source-spontaneous-height-equal-depth-tropical-balance)
- [`spontaneous-height-h1-additive-bezout.md`](#source-spontaneous-height-h1-additive-bezout)
- [`spontaneous-height-h2-additive-bezout.md`](#source-spontaneous-height-h2-additive-bezout)
- [`spontaneous-height-moving-singular-nogo.md`](#source-spontaneous-height-moving-singular-nogo)
- [`spontaneous-height-resultant-parity.md`](#source-spontaneous-height-resultant-parity)
- [`spontaneous-height-sign-companion-shadow.md`](#source-spontaneous-height-sign-companion-shadow)

<a id="source-spontaneous-height-angle-additive-norm-bridge"></a>

> 整合来源：`spontaneous-height-angle-additive-norm-bridge.md`

# A2 moving height angle-norm / additive 的 universal exact bridge

> **依赖：** `spontaneous-height-parity-ledger.md`、`spontaneous-height-resultant-parity.md`、`height-cofactor.md`、`spontaneous-height-moving-singular-nogo.md`。
>
> **严格状态：**本文给两张 moving height orientations 一个共同的高阶接口。把 angle-height norm `H_O` 与 additive-height `J_H` 精确消去 `N_0`，得到新的 positive primitive `3 mod4` carrier `R_HO`；再代入 `J_H/B_W mod W_q` 的 square-coefficient bridge，得到 `H_O,B_W,R_HO` 在整个 `W_q` depth 内的三项关系。若 angle-height 与 additive-height 深度不等，则 `R_HO` 精确读取较浅者；只有 equal-depth cancellation 能 extra lift，而且该 cancellation 强迫 normalized `B_W/H_O` ratio 为一个显式 non-square `-square`。因此 moving height 的普通 unequal-depth区全部从开放 parity mechanism中删除；剩余核心成为 same-prime orientation 是否能把这个 ratio独立固定为 square。本文不证明该最后 square/non-square 矛盾，因此不关闭 height pool。

---

## 1. notation

固定 reflection endpoint：

\[
N:=N_{\rm dec}=10^M,
\quad T:=10^m,
\quad A:=a_2,
\quad B:=b_2,
\]

\[
Q:=B+2N,
\qquad
K:=9N+10A,
\]

\[
N_0:=\left(\frac{9B}{2}\right)^2+A^2.
\]

angle pure-prefix integer为

\[
\boxed{
\mathcal U_\Omega
:=(45B^2-2AN)^2-A^2B(99B-4N).}
\tag{1.1}

angle-height norm为

\[
\boxed{
\mathcal H_O
:=N_0\mathcal U_\Omega^2
+4A^4B^2Q^2K^2.}
\tag{1.2}

additive-height pure-prefix carrier为

\[
\boxed{
\mathcal J_H
:=B^2F_W(K)-Q^2N_0,}
\tag{1.3}

其中

\[
\boxed{
F_W(K):=(K-5)(5K-11)=5K^2-36K+55.}
\tag{1.4}

---

## 2. exact angle-norm/additive identity

定义新的 pure-prefix integer

\[
\boxed{
\mathscr R_{HO}
:=F_W(K)\mathcal U_\Omega^2
+4A^4Q^4K^2.}
\tag{2.1}

由 (1.3)：

\[
Q^2N_0=B^2F_W-\mathcal J_H.
\]
将其代入 `Q^2 H_O`：

\[
\begin{aligned}
Q^2\mathcal H_O
&=(B^2F_W-\mathcal J_H)\mathcal U_\Omega^2
+4A^4B^2Q^4K^2.
\end{aligned}
\]
所以得到 exact identity

\[
\boxed{
Q^2\mathcal H_O
+\mathcal U_\Omega^2\mathcal J_H
=B^2\mathscr R_{HO}.}
\tag{2.2}

它不选择 `H_1/H_2` orientation。因为已有

\[
\mathcal H_1\mathcal H_2=4\mathcal H_O,
\]
所以 (2.2) 同时覆盖两张 moving height sheets。

---

## 3. `R_HO` 是 positive primitive `3 mod4` carrier

真实 endpoint 中

\[
K>5,
\]
故

\[
F_W(K)=(K-5)(5K-11)>0.
\]
式 (2.1) 是两个非负项之和，第一项严格正，因此

\[
\boxed{\mathscr R_{HO}>0.}
\tag{3.1}

已有 angle parity audit：

\[
\boxed{
v_2(\mathcal U_\Omega)=2M+2,}
\tag{3.2}

并且

\[
\boxed{
\frac{\mathcal U_\Omega}{2^{2M+2}}
\equiv1\pmod4.}
\tag{3.3}

同时 `K=2 mod4`，所以

\[
F_W(K)\equiv3\pmod4.
\tag{3.4}

在 (2.1) 中第一项的 `2`-进深度为

\[
4M+4,
\]
第二项因为

\[
v_2(Q)=M+1,\qquad v_2(K)=1
\]
具有深度

\[
2+4(M+1)+2=4M+8,
\]
严格更深。因此

\[
\boxed{v_2(\mathscr R_{HO})=4M+4,}
\tag{3.5}

并且

\[
\boxed{
\widehat{\mathscr R}_{HO}
:=\frac{\mathscr R_{HO}}{2^{4M+4}}
>0,
\qquad
\widehat{\mathscr R}_{HO}\equiv3\pmod4.}
\tag{3.6}

所以 `R_HO` 自身又是一份 positive odd-inert-parity carrier。

---

## 4. 代入 `J_H/B_W` height square bridge

`spontaneous-height-resultant-parity.md` 已证明

\[
\widehat{\mathcal J}_H
\equiv(2^mg)^2\mathscr B_W
\pmod{W_q},
\]
并且

\[
\mathcal J_H=2^{2M+2}\widehat{\mathcal J}_H,
\qquad
B=2^{M+m+1}c_ug.
\]
因此无分母地：

\[
\boxed{
c_u^2\mathcal J_H
\equiv B^2\mathscr B_W
\pmod{W_q}.}
\tag{4.1}

把 (4.1) 代入 (2.2) 乘 `c_u^2` 后的形式，得到 universal bridge

\[
\boxed{
B^2c_u^2\mathscr R_{HO}
\equiv
Q^2c_u^2\mathcal H_O
+\mathcal U_\Omega^2B^2\mathscr B_W
\pmod{W_q}.}
\tag{4.2}

这里两项的显式 coefficients

\[
Q^2c_u^2=(Qc_u)^2,
\]

\[
\mathcal U_\Omega^2B^2=(\mathcal U_\Omega B)^2
\]
都是完整 squares。

---

## 5. genuine external height prime上的 unit audit

固定 genuine non-`3` inert external height prime

\[
p^h\Vert W_q,
\qquad p\equiv3\pmod4,
\qquad p\ne3,5.
\]

primitive/external separation给

\[
p\nmid BQc_u.
\tag{5.1}

若该 prime进入 angle-height sheet，则某一个 raw angle integer

\[
\mathcal O_\pm
=T\mathcal U_\Omega\pm2A^2Qb_3
\]
被 `p` 整除。第二项是 external unit，因此

\[
\boxed{p\nmid\mathcal U_\Omega.}
\tag{5.2}

所以 (4.2) 的三个 coefficients在该 prime上全部为 units。

`spontaneous-height-parity-ledger.md` 还给

\[
\min\{v_p(\mathcal H_O),h\}
=
\min\{v_p(\mathcal O_{\rm hit}),h\},
\]
所以 `H_O` 正是两张 height orientations共同可用的 angle-depth reader。

---

## 6. universal unequal-depth law

定义

\[
e_B:=v_p(\mathscr B_W),
\qquad
e_O:=v_p(\mathcal H_O),
\qquad
e_R:=v_p(\mathscr R_{HO}).
\]

若

\[
\min(e_B,e_O)<h
\]
且两者不等，则 (4.2) 中较浅的 unit-coefficient term不可能被较深项取消。因此：

\[
\boxed{
e_B<e_O<h\Longrightarrow e_R=e_B,}
\tag{6.1}

\[
\boxed{
e_O<e_B<h\Longrightarrow e_R=e_O.}
\tag{6.2}

统一写成

\[
\boxed{
e_B\ne e_O,
\quad\min(e_B,e_O)<h
\Longrightarrow
v_p(\mathscr R_{HO})=\min(e_B,e_O).}
\tag{6.3}

所以 ordinary unequal-depth moving contact不会产生隐藏 extra lift。

---

## 7. equal-depth extra lift强迫 normalized non-square ratio

现在设

\[
e_B=e_O=e<h.
\]

若 `R_HO` 的 valuation严格超过 `e`，则 (4.2) 除以 `p^e` 后必须满足

\[
Q^2c_u^2\frac{\mathcal H_O}{p^e}
+\mathcal U_\Omega^2B^2\frac{\mathscr B_W}{p^e}
\equiv0\pmod p.
\]
所以

\[
\boxed{
\frac{\mathscr B_W/p^e}{\mathcal H_O/p^e}
\equiv
-\left(
\frac{Qc_u}{\mathcal U_\Omega B}
\right)^2
\pmod p.}
\tag{7.1}

右边是 `-1` 乘一个非零平方。因为

\[
p\equiv3\pmod4,
\]
有

\[
\boxed{
\left(
\frac{(\mathscr B_W/p^e)/(\mathcal H_O/p^e)}p
\right)=-1.}
\tag{7.2}

因此 equal-depth extra lift 需要一个非常具体的 same-prime orientation：normalized additive-height / angle-height ratio必须是 non-square。

这与单独对 `B_W` 或 `H_i` 做 discriminant character不同；(7.2) 是两个真实 depth readers之间的**相对 orientation**。

---

## 8. updated moving-height frontier

结合 `spontaneous-height-moving-singular-nogo.md`，moving height common channel现在满足：

1. 所有 genuine singular Hensel trees已删除；
2. unequal-depth simple contacts由 (6.3) 精确同步；
3. 唯一仍可能产生 extra depth的 unsaturated shell为
   \[
   e_B=e_O<h;
   \]
4. 该 shell若 extra lift，必须满足 relative non-square law (7.2)。

所以剩余目标已从“继续找 local singular prime”变成：

\[
\boxed{
\text{从 actual/conjugate angle sheet、canonical Gaussian orientation
或 }W_q=\alpha/\omega\text{ 的 natural representative，}
}
\]

\[
\boxed{
\text{独立确定 }
(\mathscr B_W/p^e)/(\mathcal H_O/p^e)
\text{ 的 square class。}}
\]

若该独立 orientation给 square，则 (7.2) 立即矛盾，整个 unsaturated equal-depth shell即关闭。

---

<a id="source-spontaneous-height-central-23-norm"></a>

> 整合来源：`spontaneous-height-central-23-norm.md`

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

---

<a id="source-spontaneous-height-companion-cross"></a>

> 整合来源：`spontaneous-height-companion-cross.md`

# A2 `J_H` / `B_W` residual cross-overlap 的 linear gate 与 positive norm

> **依赖：** `spontaneous-height-resultant-parity.md`、`source-discriminant.md`、`height-cofactor.md`。
>
> **严格状态：**本文研究从共同 height gcd `D_H` 中约去以后，pure-decimal companion `J^circ` 与 source-side resultant companion `B^circ` 能否再次共享 odd prime。利用前一文件的 exact difference，generic external overlap首先被压到线性 K-gate `DzK+fN=0`；再与 `B_W=0` 消去 K，得到 positive definite quadratic `R_JB`，其 discriminant恰为 `-4 D^2 c_u^2 f^2 z^2 D_W`。因此所有 simple cross-overlap只重复 `B_W` 已有的 source-discriminant square class；没有第二个 independent Legendre obstruction，也没有实根。本文不排除 simple p-adic roots，不关闭 A2。

---

## 1. 从 common height part 中约去

定义

\[
D_H=\gcd(\widehat J_H,W_q)=\gcd(\mathscr B_W,W_q),
\]

\[
J^\circ:=\widehat J_H/D_H,
\qquad
B^\circ:=\mathscr B_W/D_H,
\qquad
W^\circ:=W_q/D_H.
\]

于是

\[
\boxed{
\gcd(J^\circ,W^\circ)=
\gcd(B^\circ,W^\circ)=1.}
\tag{1.1}
\]

前一文件 (6.1) 除以 `D_H` 后给

\[
\begin{aligned}
5^{2d}J^\circ
-2^{2m}5^{2d}g^2B^\circ
={}&q^2W^\circ\Bigl[
(g^2\omega^2-c_u^2)W_q\\
&\qquad -2g^2\omega TK
\Bigr].
\end{aligned}
\tag{1.2}

因此若 odd prime `p` 同时满足

\[
p\mid J^\circ,\qquad p\mid B^\circ,
\]
则由 (1.1)，`p\nmid W^circ`。在 genuine external channel再假设

\[
p\nmid q,
\]
就必须有

\[
\boxed{
(g^2\omega^2-c_u^2)W_q
-2g^2\omega TK
\equiv0\pmod p.}
\tag{1.3}
\]

---

## 2. bracket 精确化成 linear K-gate

沿用 source triangle

\[
z:=q5^\lambda=g\omega-c_u,
\qquad
f=g\omega+c_u,
\]
所以

\[
\boxed{g^2\omega^2-c_u^2=zf.}
\tag{2.1}
\]

另有

\[
qW_q=DK-N,
\qquad
D=g2^m5^d,
\qquad
T=2^m5^{d+\lambda}.
\]

直接展开：

\[
\boxed{
q\Bigl[
(g^2\omega^2-c_u^2)W_q-2g^2\omega TK
\Bigr]
=-z(DzK+fN).}
\tag{2.2}
\]

因此 genuine `p\nmid qz` external overlap满足真正的一次条件

\[
\boxed{DzK+fN\equiv0\pmod p.}
\tag{2.3}
\]

这里

\[
N=3D-C=c_-^2X>0
\]
是 canonical height-side integer；不要与 decimal `10^M` 混淆。

所以 `J^circ/B^circ` overlap并不是新的三变量 Hensel system：K 坐标已被一条 unit-slope linear equation固定。

---

## 3. 消掉 K 得到显式 positive norm

写

\[
A_W:=5c_u^2+z^2,
\]

\[
\mathscr B_W
=A_WK^2-36c_u^2K+55c_u^2.
\]

对 K 求 resultant：

\[
\boxed{
\operatorname{Res}_K(
\mathscr B_W,\ DzK+fN
)
=
\mathscr R_{JB},}
\tag{3.1}
\]

其中

\[
\boxed{
\begin{aligned}
\mathscr R_{JB}:={}&
55D^2c_u^2z^2
+36DNc_u^2fz\\
&+N^2f^2(5c_u^2+z^2).
\end{aligned}}
\tag{3.2}
\]

所有显示量在真实 endpoint 中均正，因此立刻有

\[
\boxed{\mathscr R_{JB}>0.}
\tag{3.3}
\]

更强的是 exact completion：

\[
\boxed{
A_W\mathscr R_{JB}
=
(A_WfN+18Dc_u^2z)^2
+D^2c_u^2z^2\mathscr D_W,}
\tag{3.4}
\]

其中

\[
\mathscr D_W=55z^2-49c_u^2>0.
\]

所以该 cross-resultant 是严格 positive definite 的 source norm；它在真实轴上不存在任何 zero / near-sign-change mechanism。

---

## 4. discriminant 只是旧 source-discriminant shadow

把 (3.2) 看成 N 的 quadratic。其 discriminant exact 为

\[
\boxed{
\operatorname{Disc}_N(\mathscr R_{JB})
=-4D^2c_u^2f^2z^2\mathscr D_W.}
\tag{4.1}
\]

所以对 genuine odd inert prime

\[
p\equiv3\pmod4,
\qquad
p\nmid2D c_u fz\mathscr D_W,
\]
若 `R_JB=0 mod p` 有 root，必要且充分的 quadratic character是

\[
\left(\frac{-\mathscr D_W}{p}\right)=1.
\]
由于 `(-1/p)=-1`：

\[
\boxed{
\left(\frac{\mathscr D_W}{p}\right)=-1.}
\tag{4.2}
\]

但这正是 `B_W(K)=0` 在 nonzero-discriminant external height channel中的已有 square-class condition。故 (4.2) 只是同一 quadratic extension的 shadow，不能作为第二个 Legendre obstruction收费。

若

\[
p\mid\mathscr D_W,
\]
则进入已经单列的 external double-root / source-discriminant channel；本文不重复其 linear-decimal audit。

---

## 5. cross-companion frontier

因此 generic `J^circ/B^circ` common prime必须依次满足

\[
\boxed{
\mathscr B_W(K)=0,
\qquad
DzK+fN=0,
\qquad
\mathscr R_{JB}=0.}
\tag{5.1}

其中：

- 第二式线性固定 K；
- 第三式是 positive norm；
- nonzero-discriminant root只使用 `B_W` 原有的 square class；
- discriminant-zero branch回流到已知 `D_W=0` external double root。

所以这条 cross-pair不能通过继续叠 quadratic character关闭。它的剩余自由也是 **simple p-adic/natural-representative synchronization**。

这给 global parity ledger一个重要 no-go：即使 `J^circ` 与 `B^circ` 都携带 odd inert parity，也不能仅凭各自的 quadratic character证明二者不能由同一 generic prime承担。真正的新输入必须来自 linear gate (2.3) 的 decimal/height orbit或 size。

---

<a id="source-spontaneous-height-content-oversaturation"></a>

> 整合来源：`spontaneous-height-content-oversaturation.md`

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

---

<a id="source-spontaneous-height-equal-depth-decimal-pair"></a>

> 整合来源：`spontaneous-height-equal-depth-decimal-pair.md`

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

---

<a id="source-spontaneous-height-equal-depth-decimal-tropical-identity"></a>

> 整合来源：`spontaneous-height-equal-depth-decimal-tropical-identity.md`

# A2 equal-depth tropical balance 的 fully-decimal identity

> **依赖：** `spontaneous-height-equal-depth-tropical-balance.md`、`spontaneous-height-equal-depth-tail-reader.md`、`spontaneous-height-equal-depth-decimal-pair.md`、`source-discriminant.md`。
>
> **严格状态：**此前 tropical law仍通过 source Bezout中的 `B_W,z,f,D,g omega,L_JB` 证明。本文把三项全部乘回真实 decimal plane。定义 `B_dec=b_3^2(5K^2-36K+55)+T^2Q^2K^2`，它在 genuine target 上精确读取 `h+r_B`；随后把 source Bezout 改写成只含 `E_+`,`B_dec`,`Lambda_dec`, `alpha/beta/Delta` 等真实整数的 exact identity。该 identity 的三项深度精确为 `2h+r_B,3h,2h+rho_p`，所以 tropical minimum law与所有 tie sectors现在完全 source-free。本文只自然化 tie cancellation，不排除 tie 本身，因此不关闭 A2。

---

## 1. source ratios 的 decimal realizations

沿用

\[
\alpha=TK+a_3,
\qquad
\beta=TQ+b_3,
\qquad
\Delta=Kb_3-Qa_3.
\]

令

\[
c:=E_M\omega=\frac{\Delta}{N}.
\]

已有

\[
\boxed{cD=\beta,\qquad cR_+=E_+.}
\tag{1.1}
\]

`source-discriminant.md` 与 full-tail reader给

\[
\boxed{b_3z=Tc_uQ,}
\tag{1.2}
\]

\[
\boxed{b_3(g\omega)=c_u\beta.}
\tag{1.3}
\]

写

\[
A_H:=g\omega,
\qquad
f=A_H+c_u.
\]

由 (1.3)：

\[
b_3f
=b_3A_H+b_3c_u
=c_u(\beta+b_3).
\]
而

\[
\beta+b_3=TQ+2b_3.
\]
所以定义

\[
\boxed{F_{\rm dec}:=TQ+2b_3}
\tag{1.4}
\]
后有

\[
\boxed{b_3f=c_uF_{\rm dec}.}
\tag{1.5}
\]

在 genuine target prime上 `p∤b_3c_uf`，因此

\[
\boxed{p\nmid F_{\rm dec}.}
\tag{1.6}
\]

---

## 2. `B_W` 的 pure-decimal exact reader

沿用

\[
F_H(K):=5K^2-36K+55.
\]

source height companion为

\[
B_W=c_u^2F_H(K)+z^2K^2.
\tag{2.1}
\]

定义完全由真实 decimal quantities组成的正整数

\[
\boxed{
B_{\rm dec}
:=b_3^2F_H(K)+T^2Q^2K^2.}
\tag{2.2}
\]

由 (1.2)：

\[
b_3^2z^2=c_u^2T^2Q^2.
\]
因此

\[
\boxed{
b_3^2B_W=c_u^2B_{\rm dec}.}
\tag{2.3}
\]

当前 genuine target 与 `b_3c_u` 分离，所以若

\[
v_p(B_W)=h+r_B,
\]
则

\[
\boxed{v_p(B_{\rm dec})=h+r_B.}
\tag{2.4}
\]

这给 `r_B` 一个不再含 source quotient 的 exact natural reader。

---

## 3. full tail 的 decimal reader

沿用

\[
\boxed{
\Lambda_{\rm dec}
=2\beta\Delta+TQ^2\alpha.}
\tag{3.1}
\]

full-tail 文件已证明

\[
\boxed{
b_3cL_{JB}=c_u\Lambda_{\rm dec},}
\tag{3.2}
\]

以及 equal-depth target上

\[
\boxed{v_p(\Lambda_{\rm dec})=2h+\rho_p.}
\tag{3.3}
\]

---

## 4. source Bezout 的 complete decimalization

原 exact Bezout 为

\[
\boxed{
c_u^2fR_+
=DfB_W-DzA_H^2K^2+Kc_u^2L_{JB}.}
\tag{4.1}
\]

现在逐项使用 §§1--3。

由

\[
D=\beta/c,
\qquad
R_+=E_+/c,
\]

\[
f=c_uF_{\rm dec}/b_3,
\qquad
z=c_uTQ/b_3,
\]

\[
A_H=c_u\beta/b_3,
\]

\[
B_W=c_u^2B_{\rm dec}/b_3^2,
\qquad
L_{JB}=c_u\Lambda_{\rm dec}/(b_3c),
\]
代入 (4.1)。乘去共同 denominator并约掉 `c_u^3`，得到：

\[
\boxed{
 b_3^2F_{\rm dec}E_+
 =
 \beta F_{\rm dec}B_{\rm dec}
 -\beta^3TQK^2
 +Kb_3^2\Lambda_{\rm dec}.}
\tag{4.2}
\]

所有量均为原 decimal/prefix 整数；source variables

\[
D,z,f,c_u,g\omega,L_{JB},B_W
\]
已全部从最终 identity中消失。

---

## 5. four exact depth readers in one equation

固定 genuine deep equal-depth target：

\[
v_p(\omega)=v_p(W_q)=h,
\]

\[
v_p(B_W)=h+r_B,
\qquad
v_p(L_{JB})=h+\rho_p,
\]
并定义

\[
r_+=v_p(E_+)-2h.
\]

已有

\[
\boxed{v_p(\beta)=h,}
\tag{5.1}
\]

\[
\boxed{v_p(B_{\rm dec})=h+r_B,}
\tag{5.2}
\]

\[
\boxed{v_p(\Lambda_{\rm dec})=2h+\rho_p,}
\tag{5.3}
\]

\[
\boxed{v_p(E_+)=2h+r_+.}
\tag{5.4}
\]

而 genuine separation给

\[
p\nmid b_3F_{\rm dec}TQK.
\tag{5.5}
\]

因此 (4.2) 的 LHS 与三个 RHS terms赋值精确为

\[
\boxed{
\begin{array}{c|c}
\text{term}&p\text{-depth}\\ \hline
b_3^2F_{\rm dec}E_+&2h+r_+\\
\beta F_{\rm dec}B_{\rm dec}&2h+r_B\\
-\beta^3TQK^2&3h\\
Kb_3^2\Lambda_{\rm dec}&2h+\rho_p.
\end{array}}
\tag{5.6}

提出共同 `p^{2h}` 后，整个 tropical ledger就是四个 natural integers的 residual depth equation：

\[
\boxed{r_+\quad\leftrightarrow\quad r_B,\ h,\ \rho_p.}
\tag{5.7}

---

## 6. fully-decimal tropical law

由 (5.6)，令

\[
m_*:=\min\{r_B,h,\rho_p\}.
\]

立刻重新得到

\[
\boxed{r_+\ge m_*.}
\tag{6.1}
\]

若 minimum 唯一，则 RHS有唯一最浅 natural term，因此

\[
\boxed{r_+=m_*.}
\tag{6.2}
\]

若

\[
r_+>m_*,
\]
则至少两个 RHS natural terms必须在 depth `2h+m_*` 上发生 normalized cancellation。

所以此前 source-level tropical law现在可以完全改写为：

\[
\boxed{
\text{extra }E_+\text{ depth只可能来自 }
\beta B_{\rm dec},\ \beta^3,\ \Lambda_{\rm dec}
\text{ 三个 decimal channels的 minimum tie}.}
\tag{6.3}

---

## 7. the three pair-tie normalized equations

(4.2) 还给后续 tie audit一个 canonical starting point。只记录 strict-extra 所需的 first normalized congruence；不在本文宣称它们矛盾。

### `r_B=h<rho_p`

第一、第二 RHS terms同深，tail term更深。若 `r_+>h`，则

\[
\boxed{
\beta_0F_{\rm dec}B_0
\equiv
\beta_0^3TQK^2
\pmod p,}
\tag{7.1}
\]
其中

\[
\beta_0:=\beta/p^h,
\qquad
B_0:=B_{\rm dec}/p^{2h}.
\]

即

\[
\boxed{
F_{\rm dec}B_0
\equiv
\beta_0^2TQK^2
\pmod p.}
\tag{7.2}
\]

### `r_B=\rho_p<h`

square-content term更深。若 `r_+>r_B`，则

\[
\boxed{
\beta_0F_{\rm dec}B_0
+Kb_3^2\Lambda_0
\equiv0\pmod p,}
\tag{7.3}
\]
其中

\[
B_0:=B_{\rm dec}/p^{h+r_B},
\qquad
\Lambda_0:=\Lambda_{\rm dec}/p^{2h+\rho_p}.
\]

### `h=\rho_p<r_B`

`B_dec` term更深。若 `r_+>h`，则

\[
\boxed{
-\beta_0^3TQK^2
+Kb_3^2\Lambda_0
\equiv0\pmod p.}
\tag{7.4}

即

\[
\boxed{
b_3^2\Lambda_0
\equiv
\beta_0^3TQK
\pmod p.}
\tag{7.5}

triple tie

\[
r_B=h=\rho_p
\]
则三项同时保留。

这些 congruences 是下一层真正值得审计的 normalized unit conditions；如果其中某条被证明只是已有 exact identity的投影，应明确降级，而不能重复计作 obstruction。

---

## 8. current tie frontier

现在 equal-depth resonance的所有 depth变量都有 canonical decimal readers：

\[
\boxed{
\begin{array}{c|c}
\text{depth}&\text{reader}\\ \hline
h&\beta\text{ 或 }\Delta\\
r_B&B_{\rm dec}\\
\rho_p&\Lambda_{\rm dec}\text{ / }\Lambda_{\rm tail}\\
r_+&E_+.
\end{array}}
\tag{8.1}

因此后续不必再回到 projective source units追 `R_+` cancellation。唯一剩余的 unbounded local mechanism就是 §§7 的 pair/triple minimum ties。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-double-serial-budget"></a>

> 整合来源：`spontaneous-height-equal-depth-double-serial-budget.md`

# A2 double-serial resonance 的 weighted global budget

> **依赖：** `spontaneous-height-equal-depth-serial-gcd-selectors.md`、`spontaneous-height-equal-depth-serial-conjugates.md`、`spontaneous-height-equal-depth-middle-near-pair.md`、`spontaneous-height-equal-depth-decimal-pair.md`、`spontaneous-height-equal-depth-tail-reader.md`。
>
> **严格状态：**canonical selector `Sigma_double` 精确标记两级 serial nodes 都发生 strict-extra 的 genuine targets。本文把这些 primes 的逐素数深度聚合成 global divisibility。double-serial prime满足 `r_B=h<c_p=rho_p<r_+`，因此在 short middle carrier、full tail、actual `E_+` 与 second conjugate `D_E` 中分别承担 `>=2h+1`, `=2h+c_p>=3h+1`, `>=3h+2`, `=2h+c_p` 层。全局得到 `G_dbl^3 rad(G_dbl)^2 | E_+`，以及 exact weighted core `W_dbl | D_E`, `W_dbl rad(G_dbl)|E_+`。本文给出强高度预算但不证明 `G_dbl=1`，因此不关闭 A2。

---

## 1. double-serial prime data

固定 genuine target prime属于 `Sigma_double`。serial gcd selector theorem给

\[
\boxed{
r_B=h<c_p=\rho_p<r_+.}
\tag{1.1}
\]

所有量均为正整数，所以

\[
\boxed{c_p\ge h+1,}
\tag{1.2}
\]

\[
\boxed{r_+\ge c_p+1\ge h+2.}
\tag{1.3}
\]

---

## 2. four carrier depths

middle near-pair给

\[
v_p(C_+)=h+c_p,
\qquad
v_p(C_-)=h.
\]

因此由 (1.2)：

\[
\boxed{v_p(C_+)\ge2h+1.}
\tag{2.1}
\]

full-tail reader给

\[
\boxed{v_p(\Lambda_{\rm dec})=2h+\rho_p=2h+c_p\ge3h+1.}
\tag{2.2}
\]

second serial conjugate在 strict tie上精确满足

\[
\boxed{v_p(D_E)=2h+c_p.}
\tag{2.3}
\]

actual decimal companion则有

\[
v_p(E_+)=2h+r_+.
\]

由 (1.3)：

\[
\boxed{v_p(E_+)\ge2h+c_p+1\ge3h+2.}
\tag{2.4}
\]

所以 double-serial target在 actual sheet上比 exact conjugate还必多至少一层。

---

## 3. baseline/radical aggregate

设所有 genuine double-serial primes组成集合 `E_dbl`。写

\[
\boxed{
G_{\rm dbl}:=\prod_{p\in E_{\rm dbl}}p^{h_p},}
\tag{3.1}
\]

\[
\boxed{
R_{\rm dbl}:=\operatorname{rad}(G_{\rm dbl})
=\prod_{p\in E_{\rm dbl}}p.}
\tag{3.2}
\]

由 (2.4)，逐 prime 有

\[
p^{3h_p+2}\mid E_+.
\]

不同 primes互素，所以

\[
\boxed{
G_{\rm dbl}^3R_{\rm dbl}^2\mid E_+.}
\tag{3.3}
\]

利用 decimal-pair window

\[
0<E_+<1053TN^3,
\]
得到

\[
\boxed{
G_{\rm dbl}^3R_{\rm dbl}^2
<1053TN^3
=1053\cdot10^{m+3M}.}
\tag{3.4}
\]

这比 ordinary deep equal-depth pool 的 `G^2 rad(G)` surcharge严格多出一份 baseline与一份 radical。

---

## 4. immediate corollaries

因为

\[
R_{\rm dbl}\le G_{\rm dbl},
\]
(3.4) 至少给

\[
\boxed{G_{\rm dbl}^3<1053TN^3,}
\tag{4.1}
\]

以及

\[
\boxed{R_{\rm dbl}^5<1053TN^3.}
\tag{4.2}
\]

所以

\[
\boxed{
G_{\rm dbl}< (1053TN^3)^{1/3},}
\tag{4.3}
\]

\[
\boxed{
R_{\rm dbl}< (1053TN^3)^{1/5}.}
\tag{4.4}
\]

第二式特别说明 double-serial distinct-prime support的增长速度只能是总 decimal height的五分之一幂量级。

---

## 5. exact weighted core

更精确地定义

\[
\boxed{
W_{\rm dbl}
:=\prod_{p\in E_{\rm dbl}}p^{2h_p+c_p}.}
\tag{5.1}
\]

second conjugate exact-depth (2.3) 给

\[
\boxed{W_{\rm dbl}\mid D_E.}
\tag{5.2}
\]

actual sheet (2.4) 则逐 prime至少再多一层：

\[
\boxed{W_{\rm dbl}R_{\rm dbl}\mid E_+.}
\tag{5.3}
\]

serial-conjugate window为

\[
0<D_E<1339T^2N^4,
\]
所以

\[
\boxed{W_{\rm dbl}<1339T^2N^4.}
\tag{5.4}
\]

而由 (5.3)：

\[
\boxed{W_{\rm dbl}R_{\rm dbl}<1053TN^3.}
\tag{5.5}
\]

虽然 `D_E` 是 exact weighted baseline reader，actual `E_+` 的更短 Archimedean scale加上 extra radical通常给更强高度约束。

---

## 6. middle/tail companion budgets

由 (2.1)：

\[
\boxed{G_{\rm dbl}^2R_{\rm dbl}\mid C_+.}
\tag{6.1}
\]

middle window给

\[
\boxed{G_{\rm dbl}^2R_{\rm dbl}<843TN^3.}
\tag{6.2}
\]

由 (2.2)：

\[
\boxed{G_{\rm dbl}^3R_{\rm dbl}\mid\Lambda_{\rm dec},}
\tag{6.3}
\]

所以

\[
\boxed{G_{\rm dbl}^3R_{\rm dbl}<45T^2N^3.}
\tag{6.4}
\]

这些是 (3.4) 的 companion budgets；它们可在未来不同 `m/M` cone 中择优使用。

---

## 7. weighted log form

(3.4) 等价于

\[
\boxed{
\sum_{p\in E_{\rm dbl}}(3h_p+2)\log p
<\log1053+(m+3M)\log10.}
\tag{7.1}
\]

而 exact weighted core给

\[
\boxed{
\sum_{p\in E_{\rm dbl}}(2h_p+c_p)\log p
<\log1339+(2m+4M)\log10.}
\tag{7.2}
\]

以及 actual surcharge

\[
\boxed{
\sum_{p\in E_{\rm dbl}}(2h_p+c_p+1)\log p
<\log1053+(m+3M)\log10.}
\tag{7.3}
\]

---

## 8. current role

`Sigma_double` 现在不仅是 canonical support selector，而且其 prime support必须支付三重 baseline加双 radical的 short-decimal成本：

\[
\boxed{G_{\rm dbl}^3R_{\rm dbl}^2<1053TN^3.}
\]

因此 double-serial pool 已不再是可无代价增长的 moving-prime family。后续若能从 global inert parity、square-core residue或 top-defect得到对 `R_dbl` / `G_dbl` 的独立下界，就有机会直接关闭 `Sigma_double`。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-dual-short-carriers"></a>

> 整合来源：`spontaneous-height-equal-depth-dual-short-carriers.md`

# A2 equal-depth target 的 dual short carriers 与 exact sheet split

> **依赖：** `spontaneous-height-content-oversaturation.md`、`spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-equal-depth-square-core.md`、`primitive-reduction.md`。
>
> **严格状态：**本文把 omega-height target 的 fixed prefix quadratic 与真实第三块正定型放到同一个短-carrier框架中。当前 endpoint 下 prefix carrier `P=6K^2-36K+55` 恰有 `2M+3` 位，而 third carrier `R_3=6(a_3+3T)^2+T^2` 实际落在极窄区间 `97T^2<R_3<98T^2`。对 equal-depth target，二者的 p-depth 都精确等于 baseline `h`。更进一步，exact identity `T^2P-R_3=6 alpha L_3` 把 `gcd(P,R_3)` 精确分成互素的 numerator sheet `gcd(P,alpha)` 与 conjugate sheet `gcd(P,L_3)`，其中 `L_3=T(K-6)-a_3`；真正 equal-depth target 只进入 numerator sheet，并在那里以 exact depth `h` 出现。本文提供纯 decimal / prefix 的 baseline selector和全局乘积预算，不排除该 selector 的 inert support，因此不关闭 A2。

---

## 1. 两个 short carriers

沿用

\[
N=10^M,\qquad T=10^m,
\]

\[
\boxed{P:=\mathcal P_{\omega H}(K)=6K^2-36K+55,}
\tag{1.1}
\]

以及 `spontaneous-height-content-oversaturation.md` 的第三块正定型

\[
\boxed{R_3:=\mathscr R_{\omega H}=6(a_3+3T)^2+T^2.}
\tag{1.2}
\]

`spontaneous-height-equal-depth-target-ladder.md` 已证明

\[
\boxed{599N^2<P<600N^2,}
\tag{1.3}
\]

所以 `P` 恰有 `2M+3` 位。

当前 endpoint 更强地有

\[
1<\frac{a_3}{T}<\frac{251}{250}.
\tag{1.4}
\]

因此

\[
4<\frac{a_3+3T}{T}<\frac{1001}{250},
\]

从而

\[
97
<\frac{R_3}{T^2}
<6\left(\frac{1001}{250}\right)^2+1
=\frac{3037253}{31250}
<98.
\]

即

\[
\boxed{97T^2<R_3<98T^2.}
\tag{1.5}
\]

这把旧的粗界 `R_3<1015T^2` 收紧了一个数量级，并且只使用当前 endpoint 的真实 third-digit window。

---

## 2. 两个 primitive parts 都是 `3 mod 4`

当前 `a_2` 为奇数，且 `M>=11`，所以

\[
9\cdot10^{M-1}+a_2
\]

为奇数。由于

\[
K=10(9\cdot10^{M-1}+a_2),
\]
有

\[
\boxed{K\equiv10\pmod{20}.}
\tag{2.1}
\]

于是

\[
P=6K^2-36K+55\equiv15\pmod{20}.
\]
特别地 `5|P`，并且

\[
\boxed{\frac P5\equiv3\pmod4.}
\tag{2.2}
\]

另一方面 `a_3` 为奇数，而当前 `m>=5`，故 `T` 被 `8` 整除。于是

\[
(a_3+3T)^2\equiv1\pmod8,
\qquad T^2\equiv0\pmod8,
\]
所以

\[
\boxed{R_3\equiv6\pmod8,}
\tag{2.3}
\]

即

\[
\boxed{v_2(R_3)=1,
\qquad \frac{R_3}{2}\equiv3\pmod4.}
\tag{2.4}
\]

因此 prefix carrier 与 third carrier 在除去固定 decimal prime 后都各自携带 odd inert parity。本文不把这两份 parity自动视作独立 obstruction；下面先审计它们的公共 prime 如何分配。

---

## 3. exact two-sheet identity

真实 concatenated numerator 为

\[
\boxed{\alpha=TK+a_3.}
\tag{3.1}
\]

定义 conjugate linear form

\[
\boxed{L_3:=T(K-6)-a_3.}
\tag{3.2}
\]

直接展开：

\[
\begin{aligned}
T^2P-R_3
&=T^2(6K^2-36K+55)
  -\bigl(6a_3^2+36Ta_3+55T^2\bigr)\\
&=6(TK+a_3)(TK-a_3-6T).
\end{aligned}
\]

因此

\[
\boxed{T^2P-R_3=6\alpha L_3.}
\tag{3.3}
\]

同时

\[
\boxed{\alpha+L_3=2T(K-3),}
\tag{3.4}
\]

而

\[
\boxed{P=6(K-3)^2+1.}
\tag{3.5}
\]

所以

\[
\boxed{\gcd(P,K-3)=1.}
\tag{3.6}
\]

这将把 (3.3) 的两个 third-root sheets完全分离。

---

## 4. `gcd(P,R_3)` 的 exact coprime factorization

令

\[
G_{P3}:=\gcd(P,R_3).
\]

先注意 `P` 为奇数且

\[
P\equiv1\pmod3,
\]
所以 `2,3` 不整除 `G_{P3}`。

另外当前 source/primitive reduction给 `5\nmid\omega W_q=\alpha`，故 `5\nmid a_3`。因为 `T\equiv0 (mod 5)`：

\[
R_3\equiv6a_3^2\not\equiv0\pmod5.
\]
所以

\[
\boxed{\gcd(G_{P3},6T)=1.}
\tag{4.1}
\]

固定任意 `p|G_{P3}`，令

\[
r:=\min\{v_p(P),v_p(R_3)\}.
\]

由 (3.3)、(4.1)：

\[
p^r\mid\alpha L_3.
\tag{4.2}
\]

但 `p` 不可能同时整除 `alpha,L_3`。否则由 (3.4) 与 `p\nmid2T`：

\[
p\mid K-3,
\]
与 (3.6) 及 `p|P` 矛盾。

因此每个 `p|G_{P3}` 唯一落在两条 sheet 之一。

反过来，若 `p^s|P` 且 `p^s|alpha`，则 (3.3) 给 `p^s|R_3`；若 `p^s|P` 且 `p^s|L_3`，同理也有 `p^s|R_3`。逐 prime 比较 valuation 后得到 exact global factorization：

\[
\boxed{
\gcd(P,R_3)
=\gcd(P,\alpha)\,\gcd(P,L_3).}
\tag{4.3}
\]

并且由上面的 mutual exclusion：

\[
\boxed{
\gcd\bigl(\gcd(P,\alpha),\gcd(P,L_3)\bigr)=1.}
\tag{4.4}
\]

所以 `R_3` 的两个 p-adic roots已经在整数层被拆成两个互素 natural sheets：

- numerator sheet `alpha=0`；
- conjugate sheet `L_3=0`。

---

## 5. equal-depth target 只进入 numerator sheet，而且 depth 恰为 `h`

固定 genuine equal-depth omega-height target：

\[
v_p(\omega)=v_p(W_q)=h\ge1.
\]

于是

\[
\boxed{v_p(\alpha)=2h.}
\tag{5.1}
\]

而 target-ladder 已证明

\[
\boxed{v_p(P)=h.}
\tag{5.2}
\]

所以直接有

\[
\boxed{v_p(\gcd(P,\alpha))=h.}
\tag{5.3}
\]

由 (4.4)：

\[
\boxed{p\nmid\gcd(P,L_3).}
\tag{5.4}
\]

因此真正 equal-depth target 完全落在 numerator sheet，不会混入 conjugate sheet。

再由 (3.3)，因为 `v_p(alpha)=2h>h=v_p(P)` 且 `p\nmid T`：

\[
\boxed{v_p(R_3)=h.}
\tag{5.5}
\]

这也直接恢复了 equal-depth case 下 third carrier 的 exact baseline depth，而不需要额外使用 valuation bridge。

---

## 6. 所有 targets 的 global dual-carrier budget

令 `E_tar` 为所有当前 genuine equal-depth omega-height targets，并定义

\[
G_{\rm tar}:=\prod_{p\in E_{\rm tar}}p^{h_p}.
\]

由 (5.2)、(5.5)：

\[
\boxed{
G_{\rm tar}\mid P,
\qquad
G_{\rm tar}\mid R_3.}
\tag{6.1}
\]

更强地，由 (5.3)：

\[
\boxed{G_{\rm tar}\mid\gcd(P,\alpha).}
\tag{6.2}
\]

因此

\[
\boxed{
G_{\rm tar}\mid\gcd(P,R_3)
=\gcd(P,\alpha)\gcd(P,L_3).}
\tag{6.3}
\]

且所有 target prime powers都在第一个互素 factor 中。

由 (1.3)、(1.5)：

\[
\boxed{
G_{\rm tar}
<\min\{600N^2,98T^2\}.}
\tag{6.4}
\]

即

\[
\boxed{
\sum_{p\in E_{\rm tar}}h_p\log p
<\min\{\log600+2M\log10,
         \log98+2m\log10\}.}
\tag{6.5}
\]

这是一个完全不使用 source quotient 的 dual-length baseline budget。

---

## 7. composite target congruence

每个 target prime满足 `p^(2h_p)|alpha`，所以

\[
G_{\rm tar}^2\mid\alpha.
\tag{7.1}
\]

又 `G_tar|P,R_3`。把 (3.3) 除以 `G_tar`：

\[
T^2\frac{P}{G_{\rm tar}}
-\frac{R_3}{G_{\rm tar}}
=6\frac{\alpha}{G_{\rm tar}}L_3.
\]

右边仍被 `G_tar` 整除，因此

\[
\boxed{
T^2\frac{P}{G_{\rm tar}}
\equiv
\frac{R_3}{G_{\rm tar}}
\pmod{G_{\rm tar}}.}
\tag{7.2}
\]

而 target support 上两边都是 units。它把 prefix 与 third-block 两个短 carrier的 normalized first layer统一到同一个 composite modulus。

必须审计：该 congruence来自 exact sheet identity与 `alpha` square depth，本身不是新的独立 character obstruction；它的价值是给后续 global CRT / Archimedean comparison一个 source-free接口。

---

## 8. 当前 dual-short frontier

现在真正 equal-depth target baseline可以完全不用 source/sphere记号地读取：

\[
\boxed{
G_{\alpha P}:=\gcd(P,\alpha).}
\tag{8.1}
\]

对每个 target prime：

\[
\boxed{v_p(G_{\alpha P})=h_p.}
\tag{8.2}
\]

而第三块 companion给独立的短 carrier和 exact sheet audit：

\[
\boxed{
\gcd(P,R_3)
=G_{\alpha P}\cdot\gcd(P,L_3),
\qquad
\gcd(G_{\alpha P},\gcd(P,L_3))=1.}
\tag{8.3}
\]

因此后续若要关闭 `Sigma_deep` 的 inert support，不再需要把 third-block quadratic的另一根与 target混在一起；真正 target 已 canonical 地锁在 numerator sheet `G_{alpha P}` 中。

下一步最有价值的接口是：

1. 把 `Sigma_deep` 与 `G_{alpha P}` 取 gcd，得到 fully decimal target-baseline selector；
2. 审计 numerator/conjugate 两个互素 sheets各自承担的 `3 mod 4` parity；
3. 或把 (7.2) 与 `C_alpha=10TN-alpha` 的小 residue联立。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-fixed-exception-transversality"></a>

> 整合来源：`spontaneous-height-equal-depth-fixed-exception-transversality.md`

# A2 equal-depth fixed `7/2671` exceptions 的二阶横截性

> **依赖：** `spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-equal-depth-triple-orientation.md`、`spontaneous-height-equal-depth-fixed7-hensel.md`。
>
> **严格状态：**前面的 next-depth 审计留下两个 fixed exceptions：`p=7` 控制 source-prefix resultant `R_PD` 是否能超过 baseline，`p=2671` 控制 source/third orientation carrier `L_D3` 是否能超过 baseline。本文证明两例中的“quadratic target root”与“exceptional linear root”都只在 first layer 相交：相应 Bezout 常数在 fixed prime 上恰有赋值 `1`，所以两个 simple Hensel branches 不可能同时提升到 `p^2`。显式地，`7` 的两个 lifts 为 `32` 与 `18 mod 49`，`2671` 的两个 lifts 为 `2825391` 与 `5707400 mod 2671^2`。因此 fixed exceptions 本身不产生新的 singular/unbounded Hensel tree；任何更高 extra depth 必须来自 normalized companion cancellation。本文仍不排除这种 cancellation，因此不关闭 A2。

---

## 1. fixed `7` 的两个 first-layer equations

记

\[
R_{PD}:=55D^2-36DN+6N^2,
\]

\[
F_7:=36D-11N.
\]

此前已证明：若 deep equal-depth target 使

\[
v_7(R_{PD})>h,
\]
则必须进入 fixed branch

\[
\boxed{7\mid R_{PD},\qquad 7\mid F_7.}
\tag{1.1}
\]

并且

\[
D\equiv4N\pmod7.
\tag{1.2}
\]

已有 exact Bezout identity

\[
\boxed{
1296R_{PD}
-(1980D-691N)F_7
=175N^2.}
\tag{1.3}
\]

由于 genuine target 满足 `7\nmid N`，右端赋值为

\[
\boxed{v_7(175N^2)=1.}
\tag{1.4}
\]

在 `D=4N mod 7` 上，另一个 coefficient 为

\[
1980D-691N
\equiv(1980\cdot4-691)N
\equiv5N\not\equiv0\pmod7.
\tag{1.5}
\]

而 `1296` 也是 `7`-进单位。

所以若 `R_PD` 与 `F_7` 都被 `49` 整除，则 (1.3) 左端被 `49` 整除，与 (1.4) 矛盾。因此

\[
\boxed{
\min\{v_7(R_{PD}),v_7(F_7)\}=1
\qquad\text{在 fixed-7 first-layer intersection 上}.}
\tag{1.6}
\]

特别地，真正 extra-resultant branch有 `v_7(R_PD)>h>=1`，故

\[
\boxed{v_7(F_7)=1.}
\tag{1.7}
\]

也就是说 `F_7` 的 exceptional linear root永远只贡献第一层；`R_PD` 若继续深化，不是因为同一个 linear root继续 Hensel 跟随。

---

## 2. fixed `7` 两个 Hensel roots 在 `49` 上显式分离

写 unit ratio

\[
d:=D/N.
\]

`R_PD=0` 化为

\[
\boxed{55d^2-36d+6=0.}
\tag{2.1}
\]

fixed first root是

\[
d\equiv4\pmod7.
\]

其 derivative

\[
110d-36
\]
在 `d=4` 时为 unit，因此唯一 Hensel lift。直接计算：

\[
\boxed{d\equiv32\pmod{49}.}
\tag{2.2}
\]

另一方面 linear exception

\[
36d-11=0
\]
的唯一 lift为

\[
\boxed{d\equiv18\pmod{49}.}
\tag{2.3}
\]

显然

\[
32\not\equiv18\pmod{49}.
\]

所以：

\[
\boxed{
R_{PD}=0\text{ 与 }F_7=0
\text{ 的两个 simple 7-adic branches只在 mod }7\text{ 相交}.}
\tag{2.4}
\]

---

## 3. fixed `2671` 的 exact Bezout同样只有一层

令

\[
p_*:=2671,
\]

\[
P:=6K^2-36K+55,
\qquad
F_*:=5K-36.
\]

triple-orientation 文件证明，若 `L_D3` 想超过 target baseline，则唯一可能先满足

\[
\boxed{p_*\mid P,\qquad p_*\mid F_*.}
\tag{3.1}
\]

其共同 first root为

\[
\boxed{K\equiv2144\pmod{2671}.}
\tag{3.2}
\]

exact Bezout为

\[
\boxed{
25P-(30K+36)F_*=2671.}
\tag{3.3}
\]

右端有精确赋值

\[
\boxed{v_{2671}(2671)=1.}
\tag{3.4}
\]

在 `K=2144 mod 2671` 上

\[
30K+36\equiv252\not\equiv0\pmod{2671},
\tag{3.5}
\]

且 `25` 也是 unit。因此完全同理：

\[
\boxed{
\min\{v_{2671}(P),v_{2671}(F_*)\}=1.}
\tag{3.6}
\]

对 target baseline

\[
h:=v_{2671}(P),
\]
立刻得到 dichotomy：

\[
\boxed{
 h\ge2
 \Longrightarrow
 v_{2671}(F_*)=1,}
\tag{3.7}
\]

以及

\[
\boxed{
 v_{2671}(F_*)\ge2
 \Longrightarrow
 h=1.}
\tag{3.8}
\]

所以 linear orientation exception 与 target quadratic baseline不可能同时具有二阶深度。

---

## 4. fixed `2671` 的两个 `p^2` lifts 也显式不同

`P'(K)=12K-36`，在 (3.2) 为 `2671`-进 unit，因此 `P=0` 的 root唯一提升。

计算得到

\[
\boxed{
K_P\equiv2825391\pmod{2671^2}.}
\tag{4.1}
\]

而 linear root `5K-36=0` 的唯一提升为

\[
\boxed{
K_F\equiv5707400\pmod{2671^2}.}
\tag{4.2}
\]

两者都回到

\[
2144\pmod{2671},
\]
但

\[
\boxed{K_P\not\equiv K_F\pmod{2671^2}.}
\tag{4.3}
\]

事实上

\[
\frac{K_P-K_F}{2671}
\equiv1592\not\equiv0\pmod{2671}.
\tag{4.4}
\]

这与 Bezout valuation (3.6) 完全一致。

---

## 5. normalized first digits被 Bezout精确固定

`2671` 例还可以读取两个 root branches分离后的 first normalized digit。

若沿 target quadratic Hensel branch

\[
P\equiv0\pmod{2671^2},
\]
则把 (3.3) 除以 `2671` 并模 `2671`：

\[
-(30K+36)\frac{F_*}{2671}\equiv1\pmod{2671}.
\]

在 first root上 `30K+36=252`，所以

\[
\boxed{
\frac{F_*}{2671}
\equiv-252^{-1}
\equiv2618\pmod{2671}.}
\tag{5.1}
\]

相反，若沿 linear branch

\[
F_*\equiv0\pmod{2671^2},
\]
则

\[
25\frac P{2671}\equiv1\pmod{2671},
\]
即

\[
\boxed{
\frac P{2671}\equiv25^{-1}\equiv2030\pmod{2671}.}
\tag{5.2}
\]

所以二阶分叉不仅存在，而且两个 normalized transverse digits 都是固定 nonzero units。

---

## 6. 对 fixed exceptions 的正确解释

此前 `7` 与 `2671` 被称为 fixed exceptions，是因为普通 first-layer next-depth argument在这些 primes上失去 unit coefficient。

本文说明它们都**不是** singular Hensel exceptions：

\[
\boxed{
\text{quadratic target root与 exceptional linear root均为 simple，且只在 first layer相交}.}
\tag{6.1}
\]

因此：

- fixed `7` 中，`F_7` 在真正 extra-resultant branch上精确只有一层；
- fixed `2671` 中，若 target baseline `h>=2`，`F_*` 也精确只有一层；若 `F_*` 自己继续深化，则 target baseline只能是 `h=1`；
- 任意更高 companion depth必须来自 `R_+`、`U`、`alpha` 等 normalized terms之间的 cancellation，而不能解释成 exceptional root本身继续跟随。

这把两个 fixed branches从“可能的额外 Hensel tree”降级为“first-layer transverse collision + higher normalized cancellation”。

---

## 7. 当前 fixed-prime frontier

fixed exceptions现在具有统一结构：

\[
\boxed{
\begin{array}{c|c|c|c}
 p&\text{quadratic carrier}&\text{linear exception}&\text{intersection depth}\\ \hline
7&R_{PD}&36D-11N&1\\
2671&P&5K-36&1
\end{array}}
\tag{7.1}
\]

所以后续不应继续机械提升这两个 linear roots。真正的新目标应是对它们的 normalized cancellation构造 natural corrected carrier，或者把这种 cancellation与 `Lambda_tail` 的 exact resonance depth联立。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-fixed-second-layer-squeeze"></a>

> 整合来源：`spontaneous-height-equal-depth-fixed-second-layer-squeeze.md`

# A2 fixed `7/2671` exceptional directions 的统一 second-layer squeeze

> **依赖：** `spontaneous-height-equal-depth-orthogonal-decimal-norm.md`、`spontaneous-height-equal-depth-fixed-exception-transversality.md`、`spontaneous-height-equal-depth-decimal-pair.md`。
>
> **严格状态：**本文处理 fixed exceptions 真正剩余的 normalized cancellation。对 baseline depth `h>=2`，fixed `7` 的两张 roots与 fixed `2671` orientation root都具有同一结构：exceptional linear coefficient在 target quadratic Hensel branch上精确只有一层 `p`。因此若相应 exceptional natural direction不只多一层、而是 excess `sigma>=2`，则 decimal companion `E_+` 必须恰好具有最小 deep depth `2h+1`。结合已有 `v_p(E_+)>=2h+min(r_B,h,rho_p)`，进一步强迫 `min(r_B,rho_p)=1`。所以 `h>=2,r_B>=2,rho_p>=2` 时所有 fixed exceptional directions都至多只有一个 extra digit。本文不处理 `h=1` 的三项同深 cancellation，因此不关闭 A2。

---

## 1. common notation

固定 genuine deep equal-depth target：

\[
v_p(\omega)=v_p(W_q)=h\ge1,
\qquad
\rho_p\ge1.
\]

沿用

\[
U=DK-N,
\qquad
P=6K^2-36K+55,
\]

\[
R_+=DP-KU,
\]

以及 decimal pair

\[
E_+=E_M\omega R_+.
\]

因为

\[
v_p(E_M\omega)=h,
\]
定义

\[
\boxed{
r_+:=v_p(R_+)-h=v_p(E_+)-2h.}
\tag{1.1}
\]

已有 deep resonance transfer

\[
\boxed{r_+\ge1}
\tag{1.2}
\]

以及更强下界

\[
\boxed{
r_+\ge\min\{r_B,h,\rho_p\},}
\tag{1.3}
\]
其中

\[
v_p(B_W)=h+r_B,
\qquad r_B\ge1.
\]

---

## 2. fixed `7`, root `K=2`: `R_PD` direction

在 fixed-7 extra-resultant root

\[
K\equiv2\pmod7
\]
上，已有 exact identity

\[
\boxed{
R_{PD}
=DR_+ +(36D-11N)U-5U^2.}
\tag{2.1}
\]

记

\[
F_7:=36D-11N.
\]

若现在

\[
\boxed{h\ge2,}
\tag{2.2}
\]
则 `R_PD` 本身至少被 `7^h` 整除。fixed-exception transversality 的 Bezout

\[
1296R_{PD}-(1980D-691N)F_7=175N^2
\]
右端只有一层 `7`，所以在该 root 上

\[
\boxed{v_7(F_7)=1.}
\tag{2.3}
\]

三项赋值为

\[
v_7(DR_+)=h+r_+,
\]

\[
v_7(F_7U)=h+1,
\]

\[
v_7(5U^2)=2h\ge h+2.
\tag{2.4}
\]

定义 extra-resultant depth

\[
\boxed{
\sigma_{7,-}:=v_7(R_{PD})-h\ge1.}
\tag{2.5}
\]

若

\[
r_+\ge2,
\]
则 (2.4) 中 `F_7U` 是唯一最浅项，故

\[
\boxed{\sigma_{7,-}=1.}
\tag{2.6}
\]

逆否命题即

\[
\boxed{
\sigma_{7,-}\ge2
\Longrightarrow
r_+=1.}
\tag{2.7}
\]

用 orthogonal-decimal 文件的

\[
\Xi_{PD}=c^2R_{PD},\qquad v_7(c)=h,
\]
也可完全 decimal 地写成

\[
\boxed{
v_7(\Xi_{PD})\ge3h+2
\Longrightarrow
v_7(E_+)=2h+1.}
\tag{2.8}
\]

---

## 3. fixed `7`, root `K=4`: orthogonal direction

另一张 fixed-7 root为

\[
K\equiv4\pmod7.
\]

orthogonal file证明

\[
\boxed{
L_\perp
=(55D-18N)\alpha
+3TR_+
+T(53-15K)U.}
\tag{3.1}
\]

记

\[
F_\perp:=53-15K.
\]

`P` 与该 linear factor有

\[
75P+(74-30K)(15K-53)=203=7\cdot29.
\tag{3.2}
\]

在 `K=4 mod7` 时 `74-30K` 为 `7`-进单位；又 `h>=2` 意味着 `v_7(P)>=2`。因此 (3.2) 强迫

\[
\boxed{v_7(F_\perp)=1.}
\tag{3.3}
\]

三项赋值为

\[
v_7((55D-18N)\alpha)=2h,
\]

\[
v_7(3TR_+)=h+r_+,
\]

\[
v_7(TF_\perp U)=h+1.
\tag{3.4}
\]

其中 `2h>=h+2`。定义

\[
\boxed{
\sigma_{7,+}:=v_7(L_\perp)-h\ge1.}
\tag{3.5}
\]

若 `r_+>=2`，第三项唯一最浅，因此

\[
\sigma_{7,+}=1.
\]
于是

\[
\boxed{
\sigma_{7,+}\ge2
\Longrightarrow
r_+=1.}
\tag{3.6}
\]

利用

\[
\Xi_\perp=cL_\perp,
\]
等价的 pure-decimal form为

\[
\boxed{
v_7(\Xi_\perp)\ge2h+2
\Longrightarrow
v_7(E_+)=2h+1.}
\tag{3.7}
\]

---

## 4. fixed `2671`: parallel orientation direction

令

\[
p_*=2671,
\qquad
F_*:=5K-36.
\]

parallel carrier identity为

\[
\boxed{
L_{D3}
=TR_+-TF_*U-6N\alpha.}
\tag{4.1}
\]

在 fixed root

\[
K\equiv2144\pmod{2671}
\]
上，transversality 已证明：若

\[
h=v_{p_*}(P)\ge2,
\]
则

\[
\boxed{v_{p_*}(F_*)=1.}
\tag{4.2}
\]

所以三项赋值为

\[
h+r_+,
\qquad
h+1,
\qquad
2h\ge h+2.
\tag{4.3}
\]

定义

\[
\boxed{
\sigma_{2671}:=v_{2671}(L_{D3})-h\ge1.}
\tag{4.4}
\]

若 `r_+>=2`，中间项 `-TF_*U` 唯一最浅，因此

\[
\sigma_{2671}=1.
\]
故

\[
\boxed{
\sigma_{2671}\ge2
\Longrightarrow
r_+=1.}
\tag{4.5}
\]

又

\[
\Xi_{\parallel}=cL_{D3},
\]
所以 decimal form为

\[
\boxed{
v_{2671}(\Xi_{\parallel})\ge2h+2
\Longrightarrow
v_{2671}(E_+)=2h+1.}
\tag{4.6}
\]

---

## 5. unified second-layer squeeze

综合 §§2--4。对三种 exceptional direction中的任意一个，若

\[
\boxed{h\ge2}
\]
且它的 extra depth 不止一层：

\[
\boxed{\sigma\ge2,}
\]
则统一有

\[
\boxed{r_+=1,}
\tag{5.1}
\]
即

\[
\boxed{v_p(R_+)=h+1,}
\tag{5.2}
\]

以及完全 decimal 的

\[
\boxed{v_p(E_+)=2h+1.}
\tag{5.3}
\]

因此 fixed exception越想继续加深，`E_+` 反而越被锁到最浅的 deep level；不存在 `exceptional direction` 与 `E_+` 同时继续无界加深的 branch。

---

## 6. full tail / B_W residual 必有一个只有一层

由 (1.3)、(5.1)：

\[
1=r_+\ge\min\{r_B,h,\rho_p\}.
\]

当前

\[
h\ge2,
\qquad r_B\ge1,
\qquad\rho_p\ge1.
\]

所以严格得到

\[
\boxed{
\min\{r_B,\rho_p\}=1.}
\tag{6.1}
\]

而 full tail reader 已证明

\[
\rho_p=v_p(\Lambda_{\rm tail}).
\]

所以也可写成

\[
\boxed{
\min\{r_B,v_p(\Lambda_{\rm tail})\}=1.}
\tag{6.2}
\]

特别地：

\[
\boxed{
h\ge2,\quad r_B\ge2,\quad\rho_p\ge2
\Longrightarrow
\sigma=1}
\tag{6.3}

对三种 fixed exceptional directions全部成立。

这删除了最危险的三重深同步：

\[
\boxed{
\text{fixed exceptional depth}\ge2,
\quad B_W\text{ residual depth}\ge2,
\quad resonance tail depth\ge2
}
\]
不能同时发生。

---

## 7. normalized first-digit consequences

当 `sigma>=2` 时，除了 `r_+=1`，还得到一个显式 first normalized cancellation。

写

\[
R_+=p^{h+1}R_1,
\qquad
U=p^hU_0,
\qquad
p\nmid R_1U_0.
\]

### `7`, root `K=2`

由 quadratic root提升 `K=23 mod49` 与 `U=0 mod49` 得

\[
D/N\equiv32\pmod{49},
\qquad
\frac{36D-11N}{7N}\equiv2\pmod7.
\]

(2.1) 除以 `7^(h+1)` 后得到

\[
\boxed{2R_1+U_0\equiv0\pmod7.}
\tag{7.1}
\]

### `7`, root `K=4`

`P=0` 的 `mod49` lift为

\[
K\equiv32\pmod{49},
\]
并且

\[
\frac{53-15K}{7}\equiv2\pmod7.
\]

由 (3.1)：

\[
\boxed{3R_1+2U_0\equiv0\pmod7.}
\tag{7.2}
\]

### `2671`

fixed-exception transversality 已给 quadratic branch上

\[
\frac{5K-36}{2671}\equiv2618\equiv-53\pmod{2671}.
\]

由 (4.1)：

\[
\boxed{R_1+53U_0\equiv0\pmod{2671}.}
\tag{7.3}
\]

所以第二层 cancellation并非自由参数：三条 exceptional branches各自只允许一个 fixed normalized ratio `R_1/U_0`。

---

## 8. remaining frontier

fixed exceptions现在被压成：

1. excess `sigma=1`：只多一个 digit，已无需继续 Hensel root分类；
2. excess `sigma>=2` 且 `h>=2`：强迫
   \[
   v_p(E_+)=2h+1,
   \qquad
   \min(r_B,\rho_p)=1,
   \]
   并满足 §§7 的 fixed normalized ratio；
3. 唯一未被本文覆盖的低 baseline 是
   \[
   h=1,
   \]
   因为此时 `alpha`/`U^2` 也正好落在 `h+1=2` 层，三项可能共同 cancellation。

因此 fixed-prime frontier已经从“任意深 Hensel exception”缩成了：

\[
\boxed{
h=1\text{ low-baseline residue problem}
\quad\text{或}\quad
h\ge2\text{ 的单层 }E_+\text{ / tail gate}.}
\]

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-fixed2671-h1-squeeze"></a>

> 整合来源：`spontaneous-height-equal-depth-fixed2671-h1-squeeze.md`

# A2 fixed `2671`, baseline `h=1` 的 low-depth squeeze

> **依赖：** `spontaneous-height-equal-depth-triple-orientation.md`、`spontaneous-height-equal-depth-fixed-exception-transversality.md`、`spontaneous-height-equal-depth-tropical-balance.md`。
>
> **严格状态：**本文补齐 fixed `2671` 在 `h=1` 时未被一般 second-layer squeeze覆盖的三项同深情形。若 exceptional linear factor `F_*=5K-36` 自己提升到第二层，则 `F_*U` 至少有三层；此时 parallel carrier `L_D3` 若还要达到第三层，就强迫 `R_+` 精确停在第二层，因此 decimal `E_+` 精确只有三层。反之，若 `L_D3` 与 `E_+` 同时继续到下一层，则 `F_*` 必须精确只有一层，并由 tropical balance 强迫 `r_B` 或 full tail `rho_2671` 至少一个精确等于 `1`。本文不排除剩余 normalized unit cancellation，因此不关闭 A2。

---

## 1. fixed low-baseline setting

令

\[
p:=2671.
\]

固定 genuine deep equal-depth target，且

\[
\boxed{h=v_p(P)=v_p(U)=1.}
\tag{1.1}
\]

这里

\[
P=6K^2-36K+55,
\qquad
U=DK-N.
\]

fixed parallel exception 的 first root为

\[
\boxed{K\equiv2144\pmod p,}
\tag{1.2}
\]

并定义

\[
\boxed{F_*:=5K-36.}
\tag{1.3}
\]

因此

\[
p\mid F_*.
\]

同时 equal depth给

\[
\boxed{v_p(\alpha)=2,}
\tag{1.4}
\]
而 deep resonance transfer给

\[
\boxed{v_p(R_+)\ge2.}
\tag{1.5}
\]

parallel orientation carrier满足 exact identity

\[
\boxed{
L_{D3}=TR_+-TF_*U-6N\alpha.}
\tag{1.6}
\]

当前 `p∤6NT`。

---

## 2. linear branch若进入第二层，就不能和 deep `E_+` 一起供给 parallel extra

先假设 exceptional linear factor自己继续提升：

\[
\boxed{v_p(F_*)\ge2.}
\tag{2.1}
\]

由 `v_p(U)=1`：

\[
\boxed{v_p(F_*U)\ge3.}
\tag{2.2}
\]

若同时

\[
\boxed{v_p(R_+)\ge3,}
\tag{2.3}
\]
那么 (1.6) 三项的赋值分别至少为

\[
3,\qquad3,\qquad2.
\]

最后一项 `-6Nalpha` 是唯一最浅项，而且其 normalized coefficient为 unit。因此不能被前两项消去：

\[
\boxed{v_p(L_{D3})=2.}
\tag{2.4}
\]

所以得到严格互斥：

\[
\boxed{
v_p(F_*)\ge2,
\quad v_p(R_+)\ge3
\Longrightarrow
v_p(L_{D3})=2.}
\tag{2.5}
\]

等价地：

\[
\boxed{
v_p(F_*)\ge2,
\quad v_p(L_{D3})\ge3
\Longrightarrow
v_p(R_+)=2.}
\tag{2.6}
\]

---

## 3. pure-decimal consequence

沿用

\[
E_+=E_M\omega R_+,
\qquad
v_p(E_M\omega)=h=1,
\]
以及

\[
\Xi_{\parallel}=cL_{D3},
\qquad
v_p(c)=1.
\]

所以 (2.6) 等价于

\[
\boxed{
v_p(F_*)\ge2,
\quad v_p(\Xi_{\parallel})\ge4
\Longrightarrow
v_p(E_+)=3.}
\tag{3.1}
\]

也就是说 fixed `2671` 的 linear Hensel branch若自己继续一层，parallel decimal direction 与 `E_+` 不可能同时继续 deeper。

---

## 4. explicit linear lift

fixed-exception transversality 已计算 linear root的 `p^2` lift：

\[
\boxed{
K_F\equiv5707400\pmod{2671^2}.}
\tag{4.1}
\]

它满足

\[
\boxed{v_{2671}(5K_F-36)\ge2.}
\tag{4.2}
\]

所以在这一 explicit residue class中：

\[
\boxed{
v_{2671}(L_{D3})\ge3
\Longrightarrow
v_{2671}(E_+)=3.}
\tag{4.3}
\]

因此 linear Hensel orbit不是 low-baseline 深同步的危险源。

---

## 5. 若 parallel 与 `E_+` 都 deeper，则 linear factor必须精确一层

取 (2.5) 的逆否结构。若

\[
\boxed{
v_p(L_{D3})\ge3,
\qquad
v_p(R_+)\ge3,}
\tag{5.1}
\]
则不可能有 `v_p(F_*)>=2`，而 first root本来保证 `p|F_*`。因此：

\[
\boxed{v_p(F_*)=1.}
\tag{5.2}
\]

换成 decimal depth：

\[
\boxed{
v_p(\Xi_{\parallel})\ge4,
\qquad
v_p(E_+)\ge4
\Longrightarrow
v_p(5K-36)=1.}
\tag{5.3}
\]

所以所有真正 low-baseline double-deep states都必须离开 linear `p^2` Hensel root，留在 first-order transverse classes。

---

## 6. tropical tail squeeze

当前 `h=1`。若

\[
v_p(E_+)\ge4,
\]
则 `spontaneous-height-equal-depth-tropical-balance.md` 已无条件证明

\[
\boxed{
\min\{r_B,\rho_p\}=1.}
\tag{6.1}
\]

因此若 parallel carrier也继续 deeper：

\[
\boxed{
v_p(L_{D3})\ge3,
\qquad
v_p(E_+)\ge4
\Longrightarrow
\begin{cases}
v_p(5K-36)=1,\\
\min(r_B,\rho_{2671})=1.
\end{cases}}
\tag{6.2}
\]

这删除了 fixed `2671,h=1` 中最危险的四重同步：

\[
\boxed{
\text{linear depth}\ge2,
\quad\text{parallel depth}\ge3,
\quad E_+\text{ depth}\ge4
}
\]
不可能同时发生；而后两者同时 deep时，`B_W` residual或 full tail至少一个精确只有一层。

---

## 7. current fixed-2671 frontier

fixed `2671` 现在全部分层如下：

- `h>=2`：已有 unified second-layer squeeze；exceptional direction若多于一层，`E_+` 精确停在 `2h+1`，并有 `min(r_B,rho)=1`；
- `h=1` 且 `v(F_*)>=2`：本文证明 parallel second-extra 与 deep `E_+` 互斥；
- `h=1` 且 parallel 与 `E_+` 都 deep：只能有 `v(F_*)=1`，并且 `min(r_B,rho)=1`。

因此 fixed `2671` 不再有“linear root、parallel carrier、E_+、tail/residual”四者同时无界的局部机制。剩余自由只在 first-order transverse classes的 normalized unit cancellation。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-fixed7-audit"></a>

> 整合来源：`spontaneous-height-equal-depth-fixed7-audit.md`

# A2 equal-depth target 的 fixed `7` residue audit

> **依赖：** `spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-oversaturation-depth-ledger.md`、`spontaneous-height-content-oversaturation.md`、`endpoint-lattice.md`。
>
> **严格状态：**前一 target-ladder 文件证明：若 deep equal-depth target `p` 使 source-prefix resultant `R_PD` 的 p-depth超过 baseline `h`，则唯一可能是 `p=7`，并且必须有 `D≡4N`、`K≡2 (mod 7)`。本文把真正 target 还必须满足的 pure-prefix height congruence `H_pref=B^2K^2+Q^2N_0≡0 (mod 7)` 代回原始 decimal definitions，完整枚举 `M mod 6` 的六个 `N=10^M mod 7` 相位。结果只有 `M≡1,5 (mod 6)` 存活，每个相位只剩两个 `B mod 7` residue；其余四个长度相位严格排除 fixed-7 extra-depth orbit。本文是有限模 `7` 局部证书，不排除两个 surviving phases，也不关闭 A2。

---

## 1. fixed `7` extra-depth setting

沿用前一文件的唯一 exceptional branch：

\[
\boxed{p=7,}
\tag{1.1}
\]

并且

\[
\boxed{
D\equiv4N\pmod7,
\qquad
K\equiv2\pmod7.}
\tag{1.2}
\]

这里

\[
N=10^M.
\]

由于 `10≡3 (mod 7)`：

\[
\boxed{N\equiv3^M\pmod7,}
\tag{1.3}
\]

所以只需检查 `M mod 6`。

---

## 2. `K≡2` 唯一确定 `A=a_2 mod 7`

原 prefix 定义为

\[
\boxed{K=9N+10A.}
\tag{2.1}
\]

模 `7` 有 `9≡2`、`10≡3`，所以 fixed-7 branch满足

\[
2N+3A\equiv2\pmod7.
\]

因为 `3^{-1}≡5 (mod 7)`：

\[
\boxed{
A\equiv3(1-N)\pmod7.}
\tag{2.2}
\]

因此一旦 `M mod 6` 固定，`N mod 7` 与 `A mod 7` 都不再自由。

---

## 3. target height gate 模 `7` 变成一个一元 quartic

真正的 equal-depth omega-height target 已由 parent 文件证明

\[
v_7(\mathscr H_{\omega H}^{\rm pref})=h\ge1,
\]
其中

\[
\boxed{
\mathscr H_{\omega H}^{\rm pref}
=B^2K^2+Q^2N_0,}
\tag{3.1}
\]

\[
Q=B+2N,
\qquad
N_0=\left(\frac{9B}{2}\right)^2+A^2.
\tag{3.2}
\]

因此必有

\[
\boxed{B^2K^2+Q^2N_0\equiv0\pmod7.}
\tag{3.3}
\]

当前 genuine height prime 与 `BQN_0` 分离，所以还必须保留

\[
\boxed{7\nmid BQN_0.}
\tag{3.4}
\]

在模 `7` 下，`K≡2`，而

\[
\frac92\equiv1\pmod7
\]
（因为 `2^{-1}≡4`）。所以

\[
N_0\equiv B^2+A^2\pmod7.
\tag{3.5}
\]

于是 height gate 化为

\[
\boxed{
F_{N,A}(B)
:=4B^2+(B+2N)^2(B^2+A^2)
\equiv0\pmod7.}
\tag{3.6}
\]

其中 `A` 已由 (2.2) 唯一决定。

---

## 4. 六个 `M mod 6` 相位的完整表

逐个代入

\[
N=3^M\pmod7,
\qquad
A=3(1-N)\pmod7,
\]
并只保留满足 (3.4) 的 `B`：

\[
\boxed{
\begin{array}{c|c|c|c}
M\bmod6 & N\bmod7 & A\bmod7 & \text{admissible }B\bmod7\\ \hline
0&1&0&\varnothing\\
1&3&1&\{2,4\}\\
2&2&4&\varnothing\\
3&6&6&\varnothing\\
4&4&5&\varnothing\\
5&5&2&\{1,3\}
\end{array}}
\tag{4.1}
\]

所以 fixed `7` extra-depth target 必须满足

\[
\boxed{M\equiv1\text{ 或 }5\pmod6.}
\tag{4.2}
\]

其它四个长度相位

\[
\boxed{M\equiv0,2,3,4\pmod6}
\tag{4.3}
\]

已严格排除该 orbit。

---

## 5. surviving residues 的完整局部数据

对两个 surviving phases，把 `Q` 与 `N_0` 也列出：

### `M≡1 (mod 6)`

此时

\[
N\equiv3,
\qquad
A\equiv1.
\]

两个解分别为

\[
\boxed{
(B,Q,N_0)\equiv(2,1,5),\ (4,3,3)\pmod7.}
\tag{5.1}
\]

### `M≡5 (mod 6)`

此时

\[
N\equiv5,
\qquad
A\equiv2.
\]

两个解分别为

\[
\boxed{
(B,Q,N_0)\equiv(1,4,5),\ (3,6,6)\pmod7.}
\tag{5.2}
\]

所有显示的 `B,Q,N_0` 都是 `7`-进单位，符合 genuine target separation。

另外四个 `N_0` residue

\[
5,3,5,6
\]
均为模 `7` 非平方，这与已有 height character

\[
\left(\frac{N_0}{7}\right)=-1
\]
一致；因此该 character在这里没有进一步删除 surviving states，不能重复收费。

---

## 6. quartic factor audit

在两个 surviving phases，(3.6) 的 quartic分别分解为

\[
\boxed{
M\equiv1:\quad
F(B)
=(B-2)(B+3)(B^2-3B+1)
\pmod7,}
\tag{6.1}
\]

\[
\boxed{
M\equiv5:\quad
F(B)
=(B-3)(B-1)(B^2+3B-2)
\pmod7.}
\tag{6.2}
\]

两个 quadratic factors 在模 `7` 均不产生额外 admissible root；真正 surviving roots正是 (4.1) 中四个 linear residues。

这说明 fixed `7` extra-depth orbit 已经降成四个 simple local states，而不是一个未解析 quartic branch。

---

## 7. 当前 fixed-7 frontier

综合 target-ladder 与本文：

\[
\boxed{
\begin{gathered}
\rho_7\ge1,
\quad
v_7(\mathscr R_{PD})>h
\\
\Longrightarrow
K\equiv2,
\quad
D\equiv4N\pmod7,
\\
M\equiv1,5\pmod6,
\\
(B,Q,N_0)\text{ 仅有 (5.1)、(5.2) 四个 residue states.}
\end{gathered}}
\tag{7.1}
\]

因此 fixed `7` 的 extra-resultant branch 已从无限长度族缩成两个 `M mod 6` phase、四个 mod-`7` states。

下一步若继续攻击 `7`，应提升这四个 simple states到 `mod 49`，并与

\[
v_7(\mathcal P_{\omega H}(K))=h,
\qquad
v_7(\Lambda_{\rm tail})=\rho_7
\]
的 gcd ladder联立；普通模 `7` quadratic character已无额外信息。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-fixed7-h1-audit"></a>

> 整合来源：`spontaneous-height-equal-depth-fixed7-h1-audit.md`

# A2 fixed `7`, `K=2`, baseline `h=1` 的低层 residue compression

> **依赖：** `spontaneous-height-equal-depth-fixed-second-layer-squeeze.md`、`spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-equal-depth-decimal-pair.md`。
>
> **严格状态：**上一层 second-layer squeeze 对 `h>=2` 已把 fixed exceptions 压到最浅 `E_+` depth；唯一未覆盖的是 `h=1` 时 `R_+`、`F_7U`、`U^2` 同时可能落在第二层。本文对最危险的 fixed `7`, `K=2` extra-resultant root做完整低层展开。deep condition先唯一强迫 `D/N=32 mod49`；若 `R_PD` 还要超过一层，则进一步唯一强迫 `D/N=179 mod343`。在该状态下六个 exact-`h=1` 的 `K mod49` classes中，只有 `K=9 mod49` 能让 `E_+` 超过最小 deep depth `3`；其余五类全部精确 `v_7(E_+)=3`。本文不排除 `K=9 mod49` 的继续 lift，也不处理 fixed-7 的另一根 `K=4`，因此不关闭 A2。

---

## 1. unit-normalized source variables

固定

\[
p=7,
\qquad
h=v_7(P)=v_7(U)=1,
\]
并处在 fixed extra-resultant root

\[
\boxed{K\equiv2\pmod7.}
\tag{1.1}
\]

这里

\[
P=6K^2-36K+55,
\qquad
U=DK-N,
\]

\[
R_+=DP-KU,
\qquad
R_{PD}=55D^2-36DN+6N^2.
\]

因为 `7∤N`，可在 `Z_7` 中定义 unit ratio

\[
\boxed{d:=D/N.}
\tag{1.2}
\]

于是

\[
\frac UN=dK-1,
\tag{1.3}
\]

\[
\frac{R_+}{N}
=dP-K(dK-1),
\tag{1.4}
\]

\[
\frac{R_{PD}}{N^2}
=55d^2-36d+6.
\tag{1.5}
\]

fixed root `K=2` 与 `U=0 mod7` 给

\[
\boxed{d\equiv4\pmod7.}
\tag{1.6}
\]

写

\[
\boxed{K=2+7k,\qquad d=4+7\ell.}
\tag{1.7}
\]

---

## 2. first normalized digits

直接展开并除以 `7`：

\[
P
=7\left(1-12k+42k^2\right),
\]
所以

\[
\boxed{\frac P7\equiv1+2k\pmod7.}
\tag{2.1}
\]

又

\[
dK-1
=7\left(1+4k+2\ell+7k\ell\right),
\]
故

\[
\boxed{
\frac{U}{7N}
\equiv1+4k+2\ell\pmod7.}
\tag{2.2}
\]

对 `R_+`，由 (1.4) 展开得到

\[
\boxed{
\frac{R_+}{7N}
\equiv2+3\ell\pmod7.}
\tag{2.3}
\]

注意 (2.3) 中 `k` 完全消失。这是 low-baseline branch 的第一个 rigidity。

---

## 3. deep resonance 唯一决定 `D/N mod49`

当前 genuine deep target满足

\[
\boxed{v_7(R_+)\ge2.}
\tag{3.1}
\]

由 (2.3)：

\[
2+3\ell\equiv0\pmod7,
\]
所以

\[
\boxed{\ell\equiv4\pmod7.}
\tag{3.2}
\]

于是

\[
\boxed{d=D/N\equiv32\pmod{49}.}
\tag{3.3}
\]

这恰好与 fixed-7 quadratic Hensel root一致，但这里它不是额外假设，而是由 `h=1 + deep R_+` 直接恢复。

把 `ell=4` 代回 (2.2)：

\[
\frac{U}{7N}
\equiv2+4k
=2(1+2k)
\pmod7.
\]
结合 (2.1)：

\[
\boxed{
\frac{U}{7N}
\equiv2\frac P7
\pmod7.}
\tag{3.4}
\]

因此

\[
\boxed{
v_7(P)=v_7(U)=1
\Longleftrightarrow
k\not\equiv3\pmod7.}
\tag{3.5}
\]

`k=3` 正是 `K=23 mod49` 的 quadratic lift，会把 baseline提升到 `h>=2`，所以必须从当前 `h=1` case删除。

---

## 4. 若 `R_PD` 再多一层，则 `D/N mod343` 也唯一

现在进一步假设 fixed resultant 不只达到 `h+1=2` 层，而是

\[
\boxed{v_7(R_{PD})\ge3.}
\tag{4.1}
\]

由 (3.3) 写

\[
\boxed{d=32+49j.}
\tag{4.2}
\]

代入 (1.5)，除以 `49` 后模 `7`：

\[
\boxed{
\frac{R_{PD}}{49N^2}
\equiv6+5j\pmod7.}
\tag{4.3}
\]

所以 (4.1) 强迫

\[
6+5j\equiv0\pmod7,
\]
即

\[
\boxed{j\equiv3\pmod7.}
\tag{4.4}
\]

因此

\[
\boxed{
D/N\equiv179\pmod{343}.}
\tag{4.5}
\]

所以 fixed-7 `h=1` branch若想让 `R_PD` 出现第二个 extra digit，source ratio 到 `7^3` 已经完全无自由。

---

## 5. `E_+` 的 next depth只剩一个 `K mod49` class

在 (4.5) 下，把

\[
K=2+7k+49k_2
\]
代入 (1.4)。直接展开后，`k_2` 在下一 residue 中消失，并得到

\[
\boxed{
\frac{R_+}{49N}
\equiv
6k^2+4k+4
=6(k-1)(k-3)
\pmod7.}
\tag{5.1}
\]

由当前 exact baseline (3.5)，`k=3` 已被排除。因此：

\[
\boxed{
v_7(R_+)\ge3
\Longleftrightarrow
k\equiv1\pmod7.}
\tag{5.2}
\]

而

\[
E_+=E_M\omega R_+,
\qquad
v_7(E_M\omega)=h=1,
\]
所以

\[
\boxed{
v_7(E_+)\ge4
\Longleftrightarrow
k\equiv1\pmod7.}
\tag{5.3}
\]

也就是

\[
\boxed{
v_7(E_+)\ge4
\Longleftrightarrow
K\equiv9\pmod{49}.}
\tag{5.4}
\]

所有其它 exact-`h=1` classes都满足

\[
\boxed{v_7(E_+)=3.}
\tag{5.5}
\]

---

## 6. 完整 `K mod49` table

`K=2+7k` 且 `k!=3`，所以六个 admissible classes为

\[
\boxed{
K\equiv2,9,16,30,37,44\pmod{49}.}
\tag{6.1}
\]

在 `v_7(R_PD)>=3` 下：

\[
\boxed{
\begin{array}{c|c|c}
K\bmod49&k\bmod7&v_7(E_+)\\ \hline
2&0&3\\
9&1&\ge4\\
16&2&3\\
30&4&3\\
37&5&3\\
44&6&3
\end{array}}
\tag{6.2}
\]

因此最危险的 low-baseline triple cancellation从六个 local states再压成唯一 `K=9 mod49` state。

---

## 7. current low-baseline frontier

fixed `7`, root `K=2` 现在严格分成：

1. `v_7(R_PD)=2`：只有一个 extra digit；
2. `v_7(R_PD)>=3` 且 `K!=9 mod49`：
   \[
   D/N=179\pmod{343},
   \qquad v_7(E_+)=3;
   \]
3. 唯一还能同时让 `R_PD` 与 `E_+` 继续深化的 state：
   \[
   \boxed{D/N\equiv179\pmod{343},\qquad K\equiv9\pmod{49}.}
   \]

后续若继续 fixed-7 low baseline，应该只追最后这一条 state与 `Lambda_tail` / `B_W` residual的 next digit，不再枚举其它 `K mod49` classes。

本文不处理 `K=4` orthogonal exception或 fixed `2671,h=1`；A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-fixed7-h1-orthogonal-audit"></a>

> 整合来源：`spontaneous-height-equal-depth-fixed7-h1-orthogonal-audit.md`

# A2 fixed `7`, `K=4`, baseline `h=1` 的 orthogonal 低层 residue compression

> **依赖：** `spontaneous-height-equal-depth-orthogonal-decimal-norm.md`、`spontaneous-height-equal-depth-fixed-second-layer-squeeze.md`、`spontaneous-height-equal-depth-tropical-balance.md`。
>
> **严格状态：**本文补齐 fixed `7` 的另一张 quadratic root。对 `K=4 mod7`, `h=1` 的 orthogonal exception，deep `R_+` 先强迫 `D/N` 的第一提升 digit 与 `K` 同步；若 `L_perp` 再获得第二个 extra digit，则 `D/N` 的下一 digit也被唯一决定。此时 `E_+` 想超过最小 deep depth `3`，必须命中一个由 `K mod49` 唯一决定的 normalized numerator unit `a=alpha/(49T) mod7`。六个 exact-h=1 classes中，`K=46 mod49` 会要求 `a=0`，与 `v_7(alpha)=2` 冲突，故直接删除；其余五类各只剩一个 `a mod7`。本文不排除这五个 residue states 的更高 lift，因此不关闭 A2。

---

## 1. local normalization

固定

\[
p=7,
\qquad
h=v_7(P)=v_7(U)=1,
\]
并处在 orthogonal exceptional root

\[
\boxed{K\equiv4\pmod7.}
\tag{1.1}
\]

沿用

\[
P=6K^2-36K+55,
\qquad
U=DK-N,
\]

\[
R_+=DP-KU,
\]

以及

\[
L_\perp=(55D-18N)\alpha+3TR_++T(53-15K)U.
\tag{1.2}
\]

因为 `7∤NT`，定义

\[
\boxed{d:=D/N\in\mathbf Z_7^\times.}
\tag{1.3}
\]

`U=0 mod7` 与 `K=4 mod7` 给

\[
\boxed{d\equiv2\pmod7.}
\tag{1.4}
\]

写

\[
\boxed{K=4+7k+49k_2,\qquad d=2+7\ell+49\ell_2.}
\tag{1.5}
\]

又 equal depth `h=1` 给

\[
v_7(\alpha)=2.
\]
所以定义 unit

\[
\boxed{a:=\frac{\alpha}{49T}\in\mathbf Z_7^\times.}
\tag{1.6}
\]

后文只使用它模 `7` 的 residue。

---

## 2. first normalized digits

由 `K=4+7k+49k_2` 直接展开：

\[
\boxed{\frac P7\equiv1+5k\pmod7.}
\tag{2.1}
\]

并且

\[
\boxed{\frac{U}{7N}\equiv1+2k+4\ell\pmod7.}
\tag{2.2}
\]

由

\[
\frac{R_+}{N}=dP-K(dK-1)
\]
得到

\[
\boxed{\frac{R_+}{7N}\equiv5+2k+5\ell\pmod7.}
\tag{2.3}
\]

---

## 3. deep `R_+` 唯一同步 first lift

当前 deep resonance要求

\[
\boxed{v_7(R_+)\ge2.}
\tag{3.1}
\]

由 (2.3)：

\[
5+2k+5\ell\equiv0\pmod7.
\]
因为 `5^{-1}=3 mod7`：

\[
\boxed{\ell\equiv k+6\pmod7.}
\tag{3.2}
\]

代回 (2.2)：

\[
\frac{U}{7N}
\equiv1+2k+4(k+6)
\equiv4+6k.
\]
而

\[
2\frac P7
\equiv2+10k
\equiv2+3k.
\]
两者都恰在

\[
k\equiv4\pmod7
\]
时消失。事实上 `P/7=0` 也由 (2.1) 给同一条件。因此：

\[
\boxed{
v_7(P)=v_7(U)=1
\Longleftrightarrow
k\not\equiv4\pmod7.}
\tag{3.3}
\]

`k=4` 即

\[
K\equiv32\pmod{49},
\]
是 `P=0` 的 quadratic Hensel lift，属于 `h>=2` 而非本文低 baseline。

---

## 4. orthogonal second extra digit 唯一决定 `D/N` 的下一位

现在进一步要求

\[
\boxed{v_7(L_\perp)\ge3.}
\tag{4.1}
\]

把 (1.5)、(1.6) 与 (3.2) 代入 exact identity (1.2)，除以 `49NT` 后模 `7`，得到

\[
\boxed{
\frac{L_\perp}{49NT}
\equiv
 a+k^2+6k+6k_2+\ell_2
\pmod7.}
\tag{4.2}
\]

所以 (4.1) 唯一强迫

\[
\boxed{
\ell_2
\equiv
k_2+k-k^2-a
\pmod7.}
\tag{4.3}
\]

这说明 orthogonal exception一旦再多一层，source ratio的第二 lift digit不再自由。

---

## 5. `E_+` deeper 的唯一 numerator-unit condition

在 (3.2) 下直接展开

\[
\boxed{
\frac{R_+}{49N}
\equiv
3k+2k_2+5\ell_2+6
\pmod7.}
\tag{5.1}
\]

再代入 (4.3)，`k_2` 完全消失：

\[
\boxed{
\frac{R_+}{49N}
\equiv
2a+2k^2+k-1
\pmod7.}
\tag{5.2}
\]

由于

\[
E_+=E_M\omega R_+,
\qquad v_7(E_M\omega)=1,
\]
所以

\[
\boxed{
v_7(E_+)\ge4
\Longleftrightarrow
2a+2k^2+k-1\equiv0\pmod7.}
\tag{5.3}
\]

等价地

\[
\boxed{
a\equiv-k^2+3k+4\pmod7.}
\tag{5.4}
\]

因此给定 `K mod49` 后，只有唯一一个 normalized numerator unit `a mod7` 能让 `E_+` 再继续一层。

---

## 6. complete low-baseline table

exact `h=1` 排除 `k=4`，所以六个 admissible `k` 与 `K mod49` 为

\[
\boxed{
\begin{array}{c|c|c}
k&K\bmod49&\text{若 }v_7(E_+)\ge4\text{ 所需 }a\\ \hline
0&4&4\\
1&11&6\\
2&18&6\\
3&25&4\\
5&39&1\\
6&46&0
\end{array}}
\tag{6.1}
\]

但 `a` 由 (1.6) 是 `7`-进单位，因此

\[
\boxed{a\not\equiv0\pmod7.}
\tag{6.2}
\]

所以最后一行严格不可能：

\[
\boxed{
K\equiv46\pmod{49},\quad v_7(L_\perp)\ge3
\Longrightarrow
v_7(E_+)=3.}
\tag{6.3}
\]

其余五个 classes若要 `E_+` deeper，也各自只剩表 (6.1) 中唯一 `a`。

---

## 7. tropical consequence

若某个 surviving class确实满足

\[
v_7(E_+)\ge4,
\]
则 `spontaneous-height-equal-depth-tropical-balance.md` 的 universal `h=1` squeeze 给

\[
\boxed{
\min\{r_B,\rho_7\}=1.}
\tag{7.1}
\]

所以这些 low-baseline states仍不可能同时承担第二层 `B_W` residual与第二层 full resonance tail。

---

## 8. fixed-7 low-baseline frontier after both roots

fixed `7`, `h=1` 的两个 roots现在均已离散化：

- `K=2 mod7` / `R_PD` exception：若 `R_PD` 有第二个 extra digit，六个 `K mod49` classes中只有 `K=9` 能让 `E_+` deeper；
- `K=4 mod7` / `L_perp` exception：若 `L_perp` 有第二个 extra digit，六个 exact-h=1 classes中 `K=46` 被直接删除，其余五类各只允许唯一 `alpha/(49T) mod7` residue使 `E_+` deeper。

因此 fixed `7` 的低 baseline已从连续三项 cancellation降成有限 first/second normalized templates。后续若继续 `7`，应把这些模板与 `Lambda_tail` 的 first normalized unit或 `B_W` residual unit联立，而不再扫描全部 `7`-adic roots。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-fixed7-hensel"></a>

> 整合来源：`spontaneous-height-equal-depth-fixed7-hensel.md`

# A2 fixed `7` extra-depth target 的 two-orbit Hensel rigidity

> **依赖：** `spontaneous-height-equal-depth-fixed7-audit.md`、`spontaneous-height-equal-depth-target-ladder.md`。
>
> **严格状态：**前一 fixed-7 audit把 extra-resultant branch压成 `M≡1,5 (mod 6)` 与四个 mod-`7` states。本文证明这些 states 全部为 simple Hensel roots：exceptional quadratic root `K≡2 (mod 7)` 唯一提升；`U=DK-N` 随后唯一确定 `D mod 7^h`，prefix identity唯一确定 `A mod 7^h`；而每个 surviving phase 的两个 `B mod 7` roots 对 pure-prefix height polynomial 的导数均为 `7`-进单位，因此各自唯一提升到任意 `7^h`。所以对每个允许的长度相位与 fixed baseline depth `h`，prefix target只剩两条 canonical 7-adic orbits，而不是指数增长的 residue tree。本文不证明两条 orbits 不存在，不关闭 A2。

---

## 1. exceptional `K` root 是 simple

沿用

\[
\mathcal P_{\omega H}(K)=6K^2-36K+55.
\]

fixed-7 extra-depth branch已经强迫

\[
\boxed{K\equiv2\pmod7.}
\tag{1.1}
\]

导数为

\[
\mathcal P'_{\omega H}(K)=12K-36.
\]

在 `K=2`：

\[
\boxed{
\mathcal P'_{\omega H}(2)
=-12\equiv2\not\equiv0\pmod7.}
\tag{1.2}
\]

所以 `K≡2` 是 simple root。

由 Hensel lemma，对每个

\[
r\ge1
\]
存在唯一 residue

\[
\boxed{\kappa_r\pmod{7^r}}
\tag{1.3}
\]
满足

\[
\kappa_r\equiv2\pmod7,
\qquad
\mathcal P_{\omega H}(\kappa_r)\equiv0\pmod{7^r}.
\tag{1.4}
\]

例如第一层提升为

\[
\boxed{\kappa_2\equiv23\pmod{49}.}
\tag{1.5}
\]

若 target baseline depth为

\[
v_7(\mathcal P_{\omega H}(K))=h,
\]
则必有

\[
\boxed{K\equiv\kappa_h\pmod{7^h},}
\tag{1.6}
\]

且 exact depth `h` 进一步要求 `K` 不落入下一层 root class `kappa_{h+1} mod 7^{h+1}`。

---

## 2. `D` 与 `A` 随 `K` 唯一恢复

目标还有

\[
U=DK-N=qW_q,
\qquad
v_7(U)=h.
\]

由于 `K≡2 (mod 7)` 是 unit：

\[
DK\equiv N\pmod{7^h}
\]
唯一给出

\[
\boxed{
D\equiv NK^{-1}\pmod{7^h}.}
\tag{2.1}
\]

在 `h=1` 时恢复前一文件的

\[
D\equiv4N\pmod7.
\]

在 `h=2`、`K≡23 (mod 49)` 时

\[
23^{-1}\equiv32\pmod{49},
\]
所以

\[
\boxed{D\equiv32N\pmod{49}.}
\tag{2.2}
\]

原 prefix identity

\[
K=9N+10A
\]
中 `10` 对 `7` 为 unit，因此

\[
\boxed{
A\equiv(K-9N)10^{-1}\pmod{7^h}.}
\tag{2.3}
\]

所以给定真实 `M` 与 baseline depth `h`，`K,D,A mod 7^h` 全部不再分支。

---

## 3. `B` 的 target equation

定义

\[
\boxed{
F_h(B)
:=B^2K^2+(B+2N)^2
\left[\left(\frac{9B}{2}\right)^2+A^2\right].}
\tag{3.1}
\]

这就是

\[
\mathscr H_{\omega H}^{\rm pref}
\]
作为 `B` 的 polynomial。

真正 target 满足

\[
v_7(\mathscr H_{\omega H}^{\rm pref})=h,
\]
故至少

\[
F_h(B)\equiv0\pmod{7^h}.
\tag{3.2}
\]

其 coefficients中的 `N,K,A` 按 §§1–2 已在每层唯一确定。

---

## 4. 四个 mod-`7` roots 全部 simple

前一 finite audit得到：

### `M≡1 (mod 6)`

\[
N\equiv3,
\quad A\equiv1,
\quad B\equiv2,4\pmod7.
\]

对应的 mod-`7` polynomial为

\[
F(B)
=(B-2)(B+3)(B^2-3B+1).
\]

直接求导得到

\[
\boxed{
F'(2)\equiv2,
\qquad
F'(4)\equiv3
\pmod7.}
\tag{4.1}
\]

### `M≡5 (mod 6)`

\[
N\equiv5,
\quad A\equiv2,
\quad B\equiv1,3\pmod7,
\]

且

\[
F(B)
=(B-3)(B-1)(B^2+3B-2).
\]

有

\[
\boxed{
F'(1)\equiv3,
\qquad
F'(3)\equiv4
\pmod7.}
\tag{4.2}
\]

所以四个 surviving roots 全部满足

\[
\boxed{7\nmid F'(B_0).}
\tag{4.3}
\]

---

## 5. 每个 phase 只有两条唯一 `7`-adic B-orbits

由 (4.3) 与 Hensel lemma，每个 mod-`7` root都唯一提升到任意

\[
7^r,
\qquad r\ge1.
\]

因此：

### `M≡1 (mod 6)`

存在唯一两条 compatible residue chains

\[
\boxed{
B_{2,r}\equiv2\pmod7,
\qquad
B_{4,r}\equiv4\pmod7,}
\tag{5.1}
\]

满足

\[
F_h(B_{2,r})\equiv
F_h(B_{4,r})\equiv0\pmod{7^r}.
\]

### `M≡5 (mod 6)`

同样只有

\[
\boxed{
B_{1,r}\equiv1\pmod7,
\qquad
B_{3,r}\equiv3\pmod7.}
\tag{5.2}
\]

两条 compatible chains。

因此对 fixed real length `M` 和 baseline depth `h`：

\[
\boxed{
\text{fixed-7 extra-depth prefix target至多有两条 }7\text{-adic residue orbits}.}
\tag{5.3}
\]

这里的“至多”保留 exact valuation `h`、真实 digit window及其它 source 条件可能继续删除某条 orbit 的可能性。

---

## 6. mod `49` sanity check

`K` 的 exceptional lift为

\[
K\equiv23\pmod{49}.
\]

逐真实 `M mod 42` 相位代入 `N=10^M mod 49`、由 (2.3) 恢复 `A` 后，每个满足

\[
M\equiv1,5\pmod6
\]
的相位确实恰好出现两个 admissible `B mod 49` roots；其它 phase 没有从 mod-`7` elimination中复活。

这一有限检查只作为 Hensel uniqueness 的 sanity certificate；一般 `7^h` 结论来自 simple-root theorem，而非枚举。

---

## 7. fixed-7 frontier

fixed `7` extra-depth target现在具有 deterministic prefix pipeline：

\[
\boxed{
M
\Longrightarrow
N=10^M
\Longrightarrow
K=\kappa_h
\Longrightarrow
D,A
\Longrightarrow
\text{两条 }B\text{-Hensel orbits}.}
\tag{7.1}
\]

所以 fixed `7` branch 已不再有 moving residue-tree complexity。真正剩余的自由是：

1. 两条 simple orbit中是否有一条能同时满足 full tail condition
   \[
   v_7(\Lambda_{\rm tail})=\rho_7>0;
   \]
2. exact valuation `v_7(P)=h`、`v_7(H_pref)=h` 后的下一 digit是否与 residual companion oversaturation兼容；
3. 真实 decimal endpoint interval是否最终排除某条 lifted orbit。

后续若继续 fixed `7`，应该直接沿这两条 Hensel chains计算 normalized next-digit equations，而无需再枚举全部 residues。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-four-sheet-split"></a>

> 整合来源：`spontaneous-height-equal-depth-four-sheet-split.md`

# A2 target 的 source/third four-sheet split

> **依赖：** `spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-equal-depth-dual-short-carriers.md`、`spontaneous-height-equal-depth-triple-orientation.md`。
>
> **严格状态：**本文识别 source-prefix resultant 与 prefix quadratic之间和 third carrier完全平行的 exact two-sheet factorization。`D^2P-R_PD=6UL_D`，其中 target source sheet `U=DK-N=qW_q`，conjugate source sheet `L_D=D(K-6)+N`；在 genuine non-`2,3,5` common sector，两条 sheet互斥。与 third-side 的 `T^2P-R_3=6 alpha L_3` 联立后，任何同时进入三个 norm carriers `P,R_PD,R_3` 的 genuine prime唯一落入四个 source/third sheet pairs之一。真正 equal-depth target被 canonical 地锁在 `(alpha,U)` sheet；其它三格是 conjugate collisions。本文完成 root-sheet allocation，不排除 target sheet本身，因此不关闭 A2。

---

## 1. source-prefix identity本身已经因式分解

沿用

\[
P=6K^2-36K+55,
\qquad
U=DK-N,
\]

\[
R_{PD}=55D^2-36DN+6N^2.
\]

`spontaneous-height-equal-depth-target-ladder.md` 给出的 identity为

\[
D^2P
=R_{PD}+(12N-36D)U+6U^2.
\]

右侧 correction可以直接因式分解：

\[
(12N-36D)U+6U^2
=6U(U+2N-6D).
\]

而

\[
U+2N-6D
=DK-N+2N-6D
=D(K-6)+N.
\]

定义 source conjugate sheet

\[
\boxed{L_D:=D(K-6)+N.}
\tag{1.1}
\]

于是得到完全对称于 third carrier 的 exact identity：

\[
\boxed{D^2P-R_{PD}=6U L_D.}
\tag{1.2}
\]

与 third-side

\[
\boxed{T^2P-R_3=6\alpha L_3,}
\qquad
L_3=T(K-6)-a_3,
\tag{1.3}
\]

形成一对平行 sheet factorizations。

---

## 2. source 两条 sheet 在 genuine common sector互斥

两条 source linear forms满足

\[
\boxed{U+L_D=2D(K-3).}
\tag{2.1}
\]

而

\[
P=6(K-3)^2+1
\]
给

\[
\boxed{\gcd(P,K-3)=1.}
\tag{2.2}
\]

固定 odd prime

\[
p\nmid6DN,
\qquad p\mid P.
\]

若 `p|U,L_D`，则由 (2.1) 强迫 `p|K-3`，与 (2.2) 矛盾。因此

\[
\boxed{
p\mid P
\Longrightarrow
p\text{ 不可能同时进入 }U,L_D
\quad(p\nmid6D).}
\tag{2.3}
\]

另一方面若 `p|P,R_PD`，由 (1.2) 且 `p\nmid6D`：

\[
p\mid U L_D.
\]
结合 (2.3)：

\[
\boxed{
p\mid P,R_{PD}
\Longrightarrow
\text{恰有一条 }U=0\text{ 或 }L_D=0\pmod p.}
\tag{2.4}
\]

所以 source-prefix common root不是一个模糊 quadratic collision，而是两个明确互斥的 Hensel sheets。

---

## 3. source sheet 的 `sqrt(-6)` orientation

定义

\[
X_P=6(K-3),
\qquad
X_D=\frac{55D-18N}{N}.
\]

若取 target source sheet

\[
U=DK-N\equiv0\pmod p,
\]
则前一文件已证明

\[
\boxed{X_D\equiv-X_P\pmod p.}
\tag{3.1}
\]

若改取 conjugate source sheet

\[
L_D=D(K-6)+N\equiv0\pmod p,
\]
则

\[
\frac DN\equiv-\frac1{K-6}\pmod p.
\]
于是

\[
X_D
\equiv-\frac{55}{K-6}-18
=\frac{53-18K}{K-6}.
\]

而使用 `P=0`：

\[
6(K-3)(K-6)
=6K^2-54K+108
\equiv53-18K.
\]

所以

\[
\boxed{L_D=0\Longrightarrow X_D\equiv+X_P\pmod p.}
\tag{3.2}
\]

因此 source 两 sheets 正好就是 `sqrt(-6)` 的 `-/+` 两个 orientations。

---

## 4. third 两 sheets 同样是 `-/+` orientations

`spontaneous-height-equal-depth-dual-short-carriers.md` 已有

\[
\alpha=TK+a_3,
\qquad
L_3=T(K-6)-a_3.
\]

定义

\[
X_3=6\frac{a_3+3T}{T}.
\]

若

\[
\alpha\equiv0\pmod p,
\]
则 `a_3/T=-K`，故

\[
\boxed{X_3\equiv-X_P\pmod p.}
\tag{4.1}
\]

若

\[
L_3\equiv0\pmod p,
\]
则 `a_3/T=K-6`，故

\[
\boxed{X_3\equiv+X_P\pmod p.}
\tag{4.2}
\]

所以 source 与 third 两侧都具有同一 canonical sign convention：

\[
\boxed{
\begin{array}{c|c}
\text{sheet}&\sqrt{-6}\text{ orientation}\\ \hline
U&-\\
L_D&+\\
\alpha&-\\
L_3&+
\end{array}}
\tag{4.3}
\]

---

## 5. 三个 norm carriers 的 four-sheet partition

固定 genuine prime

\[
p\nmid30DN,
\]
并假设

\[
p\mid P,
\qquad
p\mid R_{PD},
\qquad
p\mid R_3.
\]

source two-sheet split (2.4) 给唯一选择

\[
U\quad\text{or}\quad L_D,
\]

third two-sheet split给唯一选择

\[
\alpha\quad\text{or}\quad L_3.
\]

因此 `p` 唯一落入四格之一：

\[
\boxed{
\begin{array}{c|c|c}
&\text{third }- &\text{third }+\\ \hline
\text{source }-&(U,\alpha)&(U,L_3)\\
\text{source }+&(L_D,\alpha)&(L_D,L_3)
\end{array}}
\tag{5.1}
\]

其中 diagonal 两格 orientation相同，off-diagonal 两格 orientation相反。

`spontaneous-height-equal-depth-triple-orientation.md` 的 cross carrier

\[
\mathcal L_{D3}=TN(X_D-X_3)
\]

正好在两个 diagonal sheets 上 first-layer 消失；它的 fixed `2671` next-depth exception是在真正 target diagonal `(U,alpha)` 上继续审计 normalized depth所得。

---

## 6. 真正 equal-depth target 被锁在 `(U,alpha)` sheet

对 genuine equal-depth omega-height target：

\[
U=qW_q,
\qquad
v_p(U)=h\ge1,
\]

以及

\[
\alpha=\omega W_q,
\qquad
v_p(\alpha)=2h.
\]

所以它必在

\[
\boxed{(U,\alpha)}
\tag{6.1}
\]

这一格。

而 source/third conjugates满足

\[
\boxed{p\nmid L_D L_3.}
\tag{6.2}
\]

因此后续研究 target无需再携带另外三种 root signs；它们是明确的 non-target sheet collisions。

此外 target-ladder给

\[
v_p(P)=v_p(R_{PD})=h
\quad(p\ne7,\ \rho_p\ge1),
\]

dual-short文件给

\[
v_p(R_3)=h.
\]

所以 moving target `p\ne7` 在三个 norm carriers上都以同一 baseline depth `h` 进入同一个 `(-,-)` sheet。

---

## 7. canonical sheet selectors

定义两个普通整数 gcd：

\[
\boxed{G_{P,U}:=\gcd(P,U),}
\tag{7.1}
\]

\[
\boxed{G_{P,\alpha}:=\gcd(P,\alpha).}
\tag{7.2}
\]

对真正 equal-depth target：

\[
\boxed{
v_p(G_{P,U})=h,
\qquad
v_p(G_{P,\alpha})=h.}
\tag{7.3}
\]

所以 target baseline可以进一步写成 fully integer intersection

\[
\boxed{G_{--}:=\gcd(P,U,\alpha).}
\tag{7.4}
\]

并在 target support上精确读取 `h`。

`G_{--}` 本身可能含不满足 residual oversaturation / equal-depth resonance 的额外 primes，因此它是 sheet selector而不是完整 target selector。完整 deep target仍需与 `G_JB`、`Lambda_tail` 等 canonical gates联立。

---

## 8. 当前 four-sheet frontier

三个 `sqrt(-6)` norm carriers 的 moving root ambiguity现在已经全部离散化：

\[
\boxed{
P
\rightsquigarrow
\begin{cases}
U\text{ or }L_D,\\
\alpha\text{ or }L_3,
\end{cases}}
\]

而真正 target固定为

\[
\boxed{U=0,\qquad\alpha=0}
\]

的 double-minus sheet。

所以 moving `p\notin\{7,2671\}` 的剩余困难不再包含 quadratic root sign选择；prefix/source/third orientation全部已经固定。剩余自由只在：

1. baseline 后的 p-adic unit digits；
2. `Lambda_tail` 的 excess depth `rho_p`；
3. global product / parity allocation。

下一步应把 `G_{--}` 与 `Sigma_deep` 合成 fully canonical double-minus target carrier，并检查其 primitive parity / height是否足以承担 global odd-inert excess。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-geometric-selector"></a>

> 整合来源：`spontaneous-height-equal-depth-geometric-selector.md`

# A2 deep equal-depth target 的 geometric carrier selector

> **依赖：** `spontaneous-height-equal-depth-target-selector.md`、`spontaneous-height-equal-depth-four-sheet-split.md`、`spontaneous-height-equal-depth-triple-orientation.md`、`spontaneous-height-equal-depth-tail-gcd-ladder.md`。
>
> **严格状态：**本文用 four-sheet geometry进一步简化 deep-target selector。对 genuine non-`2,3,5` sector，`P=R_PD=0` 只允许 source 的 `U`/`L_D` 两个 orientations；`alpha=0` 固定 third 为 minus orientation，而 `L_D3=0` 强迫 source 与 third orientation一致，因此自动选择 target source sheet `U=0`。再与 residual companion carrier `G_JB` 和 canonical tail quotient `Lambda_tail` 取 gcd，得到 `Sigma_geom=gcd(G_JB,P,R_PD,alpha,L_D3,Lambda_tail)`。在当前 genuine denominator-separated sector，它无需显式输入 `Gamma` 或人工 prime list即可选择 residual oversaturation + double-minus source/third sheet + equal-depth deep resonance。本文仍需 inert congruence filter，不宣称 A2 closure。

---

## 1. 已有 four-sheet geometry

沿用

\[
P=6K^2-36K+55,
\]

\[
R_{PD}=55D^2-36DN+6N^2,
\]

\[
\alpha=TK+a_3,
\]

以及 cross-orientation carrier

\[
\mathcal L_{D3}=55TD-36TN-6Na_3.
\]

`spontaneous-height-equal-depth-four-sheet-split.md` 已证明：对 genuine prime

\[
p\nmid30DN,
\qquad p\mid P,R_{PD},
\]

source root唯一落在

\[
U:=DK-N=0
\]

或

\[
L_D:=D(K-6)+N=0
\]

两条互斥 sheets之一；其 `sqrt(-6)` orientations分别为

\[
U:\ -,
\qquad
L_D:\ +.
\tag{1.1}
\]

third side同理：

\[
\alpha:\ -,
\qquad
L_3:=T(K-6)-a_3:\ +.
\tag{1.2}
\]

而

\[
\boxed{
\mathcal L_{D3}=TN(X_D-X_3)}
\tag{1.3}
\]

正是 source/third normalized roots之差。

---

## 2. `P,R_PD,alpha,L_D3` 自动选择 double-minus sheet

固定 genuine prime满足

\[
\boxed{
p\mid P,
\quad p\mid R_{PD},
\quad p\mid\alpha,
\quad p\mid\mathcal L_{D3}.}
\tag{2.1}
\]

由 `p|alpha`，third side被固定为 minus orientation：

\[
\boxed{X_3\equiv-X_P\pmod p.}
\tag{2.2}
\]

由 `p|P,R_PD`，source side只有两种可能：

\[
X_D\equiv-X_P
\quad\text{或}\quad
X_D\equiv+X_P.
\tag{2.3}
\]

又 `p|L_D3` 与 (1.3) 给

\[
X_D\equiv X_3\pmod p.
\]

结合 (2.2)：

\[
\boxed{X_D\equiv-X_P.}
\tag{2.4}
\]

因此 source 不能是 plus sheet `L_D=0`，必须是

\[
\boxed{U=DK-N\equiv0\pmod p.}
\tag{2.5}
\]

所以四个自然 carriers `P,R_PD,alpha,L_D3` 已经在 first layer自动选择真正 target 的 double-minus geometry：

\[
\boxed{(U,\alpha).}
\tag{2.6}
\]

这一步不需要显式把 `U` 放进 gcd selector。

---

## 3. double-minus sheet + `Lambda_tail` 自动恢复 equal depth

由 (2.5) 和

\[
U=qW_q,
\]
当前 genuine denominator separation `p\nmid q` 给

\[
\boxed{p\mid W_q.}
\tag{3.1}
\]

写

\[
e=v_p(\omega),
\qquad
h=v_p(W_q)\ge1.
\]

`spontaneous-height-equal-depth-tail-gcd-ladder.md` 在当前 genuine coefficient-separated sector证明

\[
 v_p(\Lambda_{\rm tail})
 =
 \begin{cases}
 0,&e\ne h,\\
 \rho_p,&e=h.
 \end{cases}
\tag{3.2}
\]

这里允许 `e=0<h`：此时仍落在第一行，tail 是 p-unit。

因此若在 double-minus sheet上再有

\[
p\mid\Lambda_{\rm tail},
\]
则必有

\[
\boxed{e=h\ge1,
\qquad\rho_p>0.}
\tag{3.3}
\]

所以 `Gamma=gcd(omega,W_q)` 虽然仍是有用的 square-core reader，却不再是**定义 deep target support**所必需的 selector input。

---

## 4. residual oversaturation carrier

沿用

\[
D_H
=\gcd(\widehat{\mathcal J}_H,W_q)
=\gcd(\mathscr B_W,W_q),
\]

\[
J^\circ=\widehat{\mathcal J}_H/D_H,
\qquad
B^\circ=\mathscr B_W/D_H,
\]

以及

\[
\boxed{G_{JB}:=\gcd(J^\circ,B^\circ).}
\tag{4.1}
\]

因此

\[
p\mid G_{JB}
\]

精确表示完整 height gcd约去后两个 companions仍继续共享 `p`。

---

## 5. geometric deep-target selector

定义普通整数

\[
\boxed{
\Sigma_{\rm geom}
:=\gcd(
G_{JB},
P,
R_{PD},
\alpha,
\mathcal L_{D3},
\Lambda_{\rm tail}
).}
\tag{5.1}
\]

固定当前 genuine non-`3` denominator-separated prime `p`。

若

\[
p\mid\Sigma_{\rm geom},
\]
则：

1. `p|G_JB`：residual `J^circ/B^circ` oversaturation；
2. `p|P,R_PD,alpha,L_D3`：由 §2 自动进入 double-minus `(U,alpha)` sheet；
3. `p|U`：故 `p|W_q`；
4. `p|Lambda_tail`：由 §3 强迫 `e=h` 且 `rho_p>0`。

所以

\[
\boxed{
 p\mid\Sigma_{\rm geom}
 \Longrightarrow
 \begin{cases}
 p\mid J^\circ,B^\circ,\\
 p\mid U,\alpha,\\
 v_p(\omega)=v_p(W_q)\ge1,\\
 \rho_p>0.
 \end{cases}}
\tag{5.2}
\]

反过来，真正 deep equal-depth residual target满足上述所有条件，并且 target-ladder / dual-short / triple-orientation文件分别给

\[
p\mid P,R_{PD},\alpha,\mathcal L_{D3},\Lambda_{\rm tail},G_{JB}.
\]

因此在该 genuine sector有 support equivalence：

\[
\boxed{
 p\mid\Sigma_{\rm geom}
 \Longleftrightarrow
 p\text{ 是 deep equal-depth residual double-minus target prime},}
\tag{5.3}
\]

这里尚未编码 `p≡3 mod4` / inertness；split common primes也会被 selector看见。

---

## 6. target p-depth of the geometric selector

对真正 target写

\[
h=v_p(\omega)=v_p(W_q),
\qquad
r_{JB}:=v_p(G_{JB})\ge1.
\]

已有

\[
v_p(P)=h,
\qquad
v_p(\alpha)=2h,
\qquad
v_p(\Lambda_{\rm tail})=\rho_p.
\]

对 moving primes：

\[
v_p(R_{PD})=h\quad(p\ne7),
\]

\[
v_p(\mathcal L_{D3})=h\quad(p\ne2671).
\]

但即使 `p=7` 或 `2671`，`P` 本身仍只有 exact depth `h`。所以统一有

\[
\boxed{
 v_p(\Sigma_{\rm geom})
 =\min\{r_{JB},h,\rho_p\}.}
\tag{6.1}
\]

也就是说 fixed `7/2671` 的 companion extra-depth不会人为放大 selector；prefix carrier `P` 自动把 selector截回真实 baseline `h`。

---

## 7. 与旧 `Sigma_deep` 的关系

旧 selector为

\[
\Sigma_{\rm deep}
=\gcd(G_{JB},\Gamma,\Lambda_{\rm tail}).
\]

它通过 `Gamma` 选择 common equal-depth sector。

新 selector改用 four-sheet geometry：

\[
P,R_{PD},\alpha,\mathcal L_{D3}
\Longrightarrow U\text{ sheet},
\]

再由

\[
U+\Lambda_{\rm tail}
\Longrightarrow e=h,\rho_p>0.
\]

所以 `Sigma_geom` 是一个独立的 geometric realization：它把 equal-depth source/third orientation显式编码进 natural carriers，而不是先调用 square-core gcd。

两个 selector可互相审计，但本文不把它们的形式差异当作新的 obstruction。

---

## 8. 当前 frontier

现在 deep target有两种 fully canonical描述：

\[
\boxed{
\Sigma_{\rm deep}
=\gcd(G_{JB},\Gamma,\Lambda_{\rm tail}),}
\]

以及

\[
\boxed{
\Sigma_{\rm geom}
=\gcd(G_{JB},P,R_{PD},\alpha,\mathcal L_{D3},\Lambda_{\rm tail}).}
\]

后者的优势是直接暴露四个 natural carriers：prefix、source-prefix、true numerator、source/third orientation。

因此下一步可不再逐 prime追踪 root signs，而直接研究

\[
\boxed{\operatorname{Supp}_{3\bmod4}(\Sigma_{\rm geom})}
\]

的 primitive parity 与高度；或者比较 `Sigma_geom` 与 `Sigma_deep` 的 inert parts，寻找一个完全 global 的 parity mismatch。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-global-decimal-gcd"></a>

> 整合来源：`spontaneous-height-equal-depth-global-decimal-gcd.md`

# A2 equal-depth square core 与 decimal pair 的 global gcd bridge

> **依赖：** `spontaneous-height-equal-depth-square-core.md`、`spontaneous-height-equal-depth-decimal-pair.md`、`spontaneous-height-content-oversaturation.md`。
>
> **严格状态：**本文把 equal-depth square core `G_eq` 与 decimal companion pair `E_+,E_-` 联立。所有 equal-depth oversaturation primes 在 `alpha,E_+` 中承担完整平方深度，在 `Delta_omega,E_-` 中只承担一半深度，因此得到 composite-modulus unit ratio。随后审计发现该 first-layer ratio 等价于已知 fixed quadratic `P_{omega H}(K)=0`，不能重复收费。真正新增的是 deep resonance 子集 `rho_p>=1` 会在 `E_+` 中比 square core 多贡献一份 squarefree radical：`G_deep^2 rad(G_deep)|E_+`。本文把局部 deep resonance 提升为全局 weighted-prime budget，但仍不关闭 A2。

---

## 1. equal-depth oversaturation product

沿用 square-core 文件的 prime 集合

\[
E_{\rm eq}
=\left\{
 p:\ p\text{ 为当前 genuine equal-depth oversaturation prime}
\right\}.
\]

对每个 `p in E_eq` 写

\[
\boxed{
v_p(\omega)=v_p(W_q)=h_p\ge1.}
\tag{1.1}
\]

定义

\[
\boxed{
G_{\rm eq}:=\prod_{p\in E_{\rm eq}}p^{h_p}.}
\tag{1.2}
\]

square-core 文件已经证明

\[
\boxed{G_{\rm eq}^2\mid\alpha.}
\tag{1.3}
\]

而 exact decimal determinant

\[
\Delta_\omega=E_MN\omega
\]
在每个 target prime 上满足 `p not| E_MN`，故

\[
\boxed{v_p(\Delta_\omega)=h_p.}
\tag{1.4}
\]

所以全局有

\[
\boxed{G_{\rm eq}\mid\Delta_\omega,}
\tag{1.5}
\]
并且相对于 modulus `G_eq^2` 是 exact half-depth：

\[
\boxed{
\gcd(\Delta_\omega,G_{\rm eq}^2)
=G_{\rm eq}.}
\tag{1.6}
\]

---

## 2. decimal companion pair 对同一 square core 的深度

`spontaneous-height-equal-depth-decimal-pair.md` 已证明逐 prime

\[
\boxed{v_p(\mathcal E_-)=h_p,}
\tag{2.1}
\]

\[
\boxed{
v_p(\mathcal E_+)
\ge2h_p+\min(r_{B,p},h_p,\rho_p).}
\tag{2.2}
\]

特别地无论 `rho_p` 是否为正：

\[
\boxed{v_p(\mathcal E_+)\ge2h_p.}
\tag{2.3}
\]

因此聚合所有 distinct primes：

\[
\boxed{G_{\rm eq}^2\mid\mathcal E_+,}
\tag{2.4}
\]

\[
\boxed{
\gcd(\mathcal E_-,G_{\rm eq}^2)
=G_{\rm eq}.}
\tag{2.5}
\]

于是同一个 equal-depth square modulus 在三个真实 decimal integers 中的 target-prime 深度是

\[
\boxed{
\begin{array}{c|c}
\text{integer}&E_{\rm eq}\text{ prime depth}\\ \hline
\alpha&2h_p\\
\mathcal E_+&\ge2h_p\\
\Delta_\omega&h_p\\
\mathcal E_-&h_p.
\end{array}}
\tag{2.6}
\]

这已经完全摆脱 source quotient。

---

## 3. composite-modulus unit ratio

两个 decimal companions 满足 exact difference

\[
\boxed{
\mathcal E_+-\mathcal E_-
=2K\Delta_\omega.}
\tag{3.1}
\]

由 (2.4)：

\[
\mathcal E_-+2K\Delta_\omega
\equiv0\pmod{G_{\rm eq}^2}.
\tag{3.2}
\]

由 (1.5)、(2.5) 可除去一份 `G_eq`：

\[
\boxed{
\frac{\mathcal E_-}{G_{\rm eq}}
\equiv
-2K\frac{\Delta_\omega}{G_{\rm eq}}
\pmod{G_{\rm eq}}.}
\tag{3.3}
\]

并且两边都是 modulus `G_eq` 的单位：

\[
\boxed{
\gcd\left(\frac{\mathcal E_-}{G_{\rm eq}},G_{\rm eq}\right)
=
\gcd\left(\frac{\Delta_\omega}{G_{\rm eq}},G_{\rm eq}\right)
=1.}
\tag{3.4}
\]

所以 equal-depth pool 已经产生一个单一 composite modulus 上的 projective unit synchronization，而不需要逐 prime 写 `omega_0,W_0`。

---

## 4. no-double-count audit：first-layer unit ratio 只是 `P_omegaH` root

必须检查 (3.3) 是否真的独立。

由

\[
\Delta_\omega=K\beta-Q\alpha
\tag{4.1}
\]
以及 `G_eq^2|alpha`：

\[
\frac{\Delta_\omega}{G_{\rm eq}}
\equiv
K\frac\beta{G_{\rm eq}}
\pmod{G_{\rm eq}}.
\tag{4.2}
\]

另一方面

\[
\mathcal E_-
=F_H(K)\beta-K\Delta_\omega,
\]
其中

\[
F_H(K)=5K^2-36K+55.
\]
除以 `G_eq` 并使用 (4.2)：

\[
\frac{\mathcal E_-}{G_{\rm eq}}
\equiv
\left(F_H(K)-K^2\right)
\frac\beta{G_{\rm eq}}
\pmod{G_{\rm eq}}.
\tag{4.3}
\]

把 (3.3) 右边也用 (4.2) 改写，并利用 `beta/G_eq`、`K` 都是 units，得到

\[
F_H(K)-K^2
\equiv-2K^2
\pmod{G_{\rm eq}}.
\]
也就是

\[
\boxed{
6K^2-36K+55
=\mathcal P_{\omega H}(K)
\equiv0
\pmod{G_{\rm eq}}.}
\tag{4.4}
\]

这正是 parent oversaturation 已经得到的 fixed quadratic root，聚合到 composite modulus 后的重写。

所以：

\[
\boxed{
\text{(3.3) 的 first layer 不构成新的 obstruction。}}
\tag{4.5}
\]

它的作用是给后面的 deep-radical amplification 提供完全 decimal 的统一接口。

---

## 5. deep resonance primes 额外贡献一份 radical

定义 deep subset

\[
\boxed{
E_{\rm deep}
:=\{p\in E_{\rm eq}:\rho_p\ge1\}.}
\tag{5.1}
\]

令

\[
\boxed{
G_{\rm deep}
:=\prod_{p\in E_{\rm deep}}p^{h_p},
\qquad
R_{\rm deep}
:=\operatorname{rad}(G_{\rm deep})
=\prod_{p\in E_{\rm deep}}p.}
\tag{5.2}
\]

对每个 deep prime，decimal-pair 文件给

\[
v_p(\mathcal E_+)\ge2h_p+1.
\]
由于这些 prime 互异，直接聚合：

\[
\boxed{
G_{\rm deep}^2R_{\rm deep}
\mid\mathcal E_+.}
\tag{5.3}
\]

这就是 first-layer square core 之外真正新增的 global cost：每一枚 deep resonance prime 至少还要额外支付**一份 squarefree radical**。

由 fixed decimal window

\[
\mathcal E_+<1053\,TN^3
=1053\cdot10^{m+3M}
\]
得到

\[
\boxed{
G_{\rm deep}^2R_{\rm deep}
<1053\cdot10^{m+3M}.}
\tag{5.4}
\]

等价地

\[
\boxed{
\sum_{p\in E_{\rm deep}}
(2h_p+1)\log p
<
\log1053+(m+3M)\log10.}
\tag{5.5}
\]

这把局部 `rho_p>=1` 提升成了一个全局 weighted-prime budget。

---

## 6. 同一个 square modulus 现在控制两个真实 decimal residues

square-core 文件还给

\[
\boxed{
10TN\equiv C_\alpha
\pmod{G_{\rm eq}^2},}
\tag{6.1}
\]
其中

\[
0<C_\alpha<\frac{TN}{250}.
\]

而本文有

\[
\boxed{
\mathcal E_-
\equiv-2K\Delta_\omega
\pmod{G_{\rm eq}^2}.}
\tag{6.2}
\]

因此同一个 original-integer square core `G_eq^2` 已同时控制：

1. `10TN` 的小 positive endpoint residue `C_alpha`；
2. `E_-` 的 determinant residue `-2K Delta_omega`；
3. deep subset 还通过 (5.3) 在 `E_+` 上额外支付 radical。

这正是前一 square-core 文件留下的“两个 independent decimal residues”接口。

---

## 7. 当前 global frontier

综合本文：

\[
\boxed{
\begin{gathered}
G_{\rm eq}^2\mid\alpha,\mathcal E_+,\\
\gcd(\Delta_\omega,G_{\rm eq}^2)
=\gcd(\mathcal E_-,G_{\rm eq}^2)
=G_{\rm eq},\\
10TN\equiv C_\alpha\pmod{G_{\rm eq}^2},\\
\mathcal E_-\equiv-2K\Delta_\omega
\pmod{G_{\rm eq}^2},\\
G_{\rm deep}^2\operatorname{rad}(G_{\rm deep})
\mid\mathcal E_+.
\end{gathered}}
\tag{7.1}
\]

其中 composite unit congruence 的 first layer 已审计为旧 `P_{omega H}` root，不重复计作障碍；真正新信息是 deep subset 的额外 radical 与两个真实 decimal residue共享同一 square modulus。

下一步若要逼近 closure，应研究：

- `C_alpha` 很小时，(6.1) 对 `G_eq^2` 的 natural representative 是否与 (6.2) 同时可行；
- `G_deep^2 rad(G_deep)` 与 `alpha` 的更短 `m+M+1` 位 square-core budget 是否可联合给出 radical 过饱和；
- 或构造二阶 corrected `E_+`，继续读取 `rho_p>min(h_p,r_{B,p})` 的 tail。

---

<a id="source-spontaneous-height-equal-depth-middle-near-pair"></a>

> 整合来源：`spontaneous-height-equal-depth-middle-near-pair.md`

# A2 serial middle carrier 的 short near-pair

> **依赖：** `spontaneous-height-equal-depth-serial-tropical-bridge.md`。
>
> **严格状态：**本文把 serial middle carrier `C_BE` 再改写为两项 close pair。定义 `A_P=4K^2-36K+55` 与 `C_-=A_P beta-b_3P`，则 `C_BE=A_P beta+b_3P`，两者只相差 `2b_3P=O(TN^2)`，但都处在 `839..843` 的 `TN^3` 短窗口。对每一个 genuine deep equal-depth target，`C_BE` 至少有 `h+1` 层，而 `C_-` 精确只有 `h` 层。于是 first tropical node有一个完全 natural 的 `deep/exact` near-pair。本文不利用该 pair 完成 modulus-height contradiction，因此不关闭 A2。

---

## 1. exact close-pair decomposition

沿用

\[
P=6K^2-36K+55,
\qquad
F_{\rm dec}=TQ+2b_3,
\qquad
\beta=TQ+b_3,
\]

\[
C_{BE}=F_{\rm dec}P-2K^2\beta.
\]

定义

\[
\boxed{A_P:=4K^2-36K+55=P-2K^2.}
\tag{1.1}
\]

因为

\[
F_{\rm dec}P-2K^2\beta
=(TQ+2b_3)P-2K^2(TQ+b_3),
\]
直接整理得到

\[
\boxed{
C_+:=C_{BE}=A_P\beta+b_3P.}
\tag{1.2}
\]

定义 conjugate

\[
\boxed{
C_-:=A_P\beta-b_3P.}
\tag{1.3}
\]

于是

\[
\boxed{C_+-C_-=2b_3P,}
\tag{1.4}
\]

\[
\boxed{C_++C_-=2A_P\beta.}
\tag{1.5}
\]

所以 `(C_+,C_-)` 是一个完全由真实 decimal/prefix quantities构成的 close pair。

---

## 2. target local units

固定 genuine deep equal-depth target `p`：

\[
v_p(P)=v_p(\beta)=h\ge1.
\]

当前 separation给

\[
p\nmid2Kb_3.
\]

又由 `p|P` 与 (1.1)：

\[
A_P\equiv-2K^2\pmod p,
\]
所以

\[
\boxed{p\nmid A_P.}
\tag{2.1}
\]

因此两项

\[
A_P\beta,
\qquad
b_3P
\]
都具有精确赋值

\[
\boxed{h.}
\tag{2.2}
\]

serial bridge 已证明

\[
v_p(C_+)=h+c_p,
\qquad
c_p\ge1.
\]

所以

\[
\boxed{v_p(C_+)\ge h+1.}
\tag{2.3}
\]

---

## 3. conjugate is exact baseline for every deep target

写

\[
A_P\beta=p^hu,
\qquad
b_3P=p^hv,
\]
其中 `u,v` 为 `p`-units。

由 (1.2)、(2.3)：

\[
u+v\equiv0\pmod p.
\]

所以

\[
u-v\equiv-2v\not\equiv0\pmod p
\]
因为 `p` 为 odd。由 (1.3)：

\[
\boxed{v_p(C_-)=h.}
\tag{3.1}
\]

这是无条件的 deep-target exactness，不要求 first-node strict-extra。

因此：

\[
\boxed{
\begin{array}{c|c}
\text{carrier}&p\text{-depth}\\ \hline
C_+&h+c_p\ge h+1\\
C_-&h.
\end{array}}
\tag{3.2}
\]

若进一步处在 first-node strict-extra

\[
r_B=h<\rho_p,
\qquad
r_+>h,
\]
serial bridge给 `c_p>h`，所以

\[
\boxed{v_p(C_+)>2h,\qquad v_p(C_-)=h.}
\tag{3.3}
\]

---

## 4. same short Archimedean window

serial bridge已有

\[
839TN^3<C_+<843TN^3.
\tag{4.1}
\]

又 dual-short carrier 已给

\[
0<P<600N^2,
\]
以及

\[
0<b_3<\frac{843}{1000}T.
\]

由 (1.4)：

\[
0<C_+-C_-=2b_3P
<\frac{2\cdot843\cdot600}{1000}TN^2
<1012TN^2.
\tag{4.2}
\]

因为 `N>=10^11`，serial bridge 的实际 lower margin大于 `0.328 TN^3`，而 (4.2) 小于 `1.012*10^-8 TN^3`。因此仍有

\[
\boxed{839TN^3<C_-.}
\tag{4.3}
\]

显然 `C_-<C_+<843TN^3`，故

\[
\boxed{
839TN^3<C_-<C_+<843TN^3.}
\tag{4.4}
\]

特别地两者都为正，且都恰有

\[
\boxed{m+3M+3}
\]
个十进制数字。

---

## 5. relative gap

由 (1.4)、(4.2)、(4.4)：

\[
\boxed{
0<C_+-C_-<1012TN^2,}
\tag{5.1}
\]
而两者都大于 `839TN^3`。因此

\[
\boxed{
0<\frac{C_+-C_-}{C_-}
<\frac{1012}{839N}.}
\tag{5.2}
\]

所以 pair 的相对距离是 `O(10^{-M})`。

---

## 6. current use

`C_+/C_-` 给 first serial node 一个和此前 `E_+/E_-` 类似但更短的 natural pair：

- same decimal length；
- relative gap `O(1/N)`；
- target prime在 actual sheet `C_+` 至少多一层；
- conjugate `C_-` 对所有 deep target精确只有 baseline `h`。

因此 first-node higher cancellation不再需要通过抽象 normalized units描述；它已经有一个 short natural near-pair可用于后续 gcd、modulus-height 或 parity allocation。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-mod24-parity"></a>

> 整合来源：`spontaneous-height-equal-depth-mod24-parity.md`

# A2 equal-depth dual short carriers 的 mod-24 双字符 parity ledger

> **依赖：** `spontaneous-height-equal-depth-dual-short-carriers.md`、`spontaneous-height-equal-depth-four-sheet-split.md`。
>
> **严格状态：**此前已经证明 prefix carrier `P=6K^2-36K+55` 与真实 third carrier `R_3=6(a_3+3T)^2+T^2` 都是短的 primitive odd-inert parity suppliers，并且 `gcd(P,R_3)` 精确分成 numerator/conjugate 两张互素 sheets。本文把这一 pair 从 `mod 4` 提升到 `mod 24`：`P/5` 与 `R_3/2` 都恒为 `11 mod 24`。任何非 `2,3,5` 公共 prime 都落在 `1,5,7,11 mod 24` 的 Klein 四群，因此约去完整公共 gcd 后两个 residual 不仅 `mod 4` 相同，而且 `mod 24` 完全相同。本文同时审计：该双字符 parity 只控制两张 sheet 的乘积类，不能单独固定 target numerator sheet 的 residue class，所以它本身不是 A2 closure。

---

## 1. 记号

沿用

\[
P:=6K^2-36K+55,
\]

\[
R_3:=6(a_3+3T)^2+T^2,
\]

\[
\alpha=TK+a_3,
\qquad
L_3=T(K-6)-a_3.
\]

当前 endpoint 中

- `K=10r`，其中 `r` 为奇数；
- `m>=5`，故 `T=10^m`；
- `a_3` 为奇数；
- primitive reduction 给 `5\nmid a_3`。

此前已有 exact identity

\[
\boxed{T^2P-R_3=6\alpha L_3}
\tag{1.1}
\]

以及 exact coprime sheet split

\[
\boxed{
G_{P3}:=\gcd(P,R_3)
=G_-G_+,}
\tag{1.2}
\]

其中

\[
\boxed{
G_-:=\gcd(P,\alpha),
\qquad
G_+:=\gcd(P,L_3),
\qquad
\gcd(G_-,G_+)=1.}
\tag{1.3}
\]

真正 equal-depth target 只进入 `G_-` numerator sheet。

---

## 2. prefix primitive carrier 恒为 `11 mod 24`

因为 `K=10r` 且 `r` 为奇数，

\[
K\equiv2\pmod4.
\]

所以 `K^2` 被 `4` 整除，而更精确地

\[
6K^2\equiv0\pmod{24}.
\]

同时 `K` 为偶数，故

\[
36K\equiv0\pmod{24}.
\]

于是

\[
\boxed{P\equiv55\equiv7\pmod{24}.}
\tag{2.1}
\]

`K` 被 `10` 整除，因此 `P` 被 `5` 整除。由于 `5` 在 `mod 24` 下可逆且

\[
5^{-1}\equiv5\pmod{24},
\]
得到

\[
\boxed{\frac P5\equiv7\cdot5\equiv11\pmod{24}.}
\tag{2.2}
\]

这里不声称 `v_5(P)=1`；即使 `P` 还含更高 `5`-primary，(2.2) 仍是严格整数同余。

---

## 3. third primitive carrier 也恒为 `11 mod 24`

当 `m>=5` 时

\[
T=10^m\equiv16\pmod{48}.
\tag{3.1}
\]

因此

\[
3T\equiv0\pmod{48},
\qquad
T^2\equiv16\pmod{48}.
\]

`a_3` 为奇数，所以任意奇数平方满足

\[
a_3^2\equiv1\pmod8.
\]

乘以 `6` 后该信息正好提升为

\[
6a_3^2\equiv6\pmod{48}.
\]

于是

\[
\begin{aligned}
R_3
&=6(a_3+3T)^2+T^2\\
&\equiv6a_3^2+16\\
&\equiv22\pmod{48}.
\end{aligned}
\]

所以

\[
\boxed{R_3\equiv22\pmod{48},}
\tag{3.2}
\]

并可合法除以 `2` 得

\[
\boxed{\frac{R_3}{2}\equiv11\pmod{24}.}
\tag{3.3}
\]

因此两个 short primitive carriers 具有完全相同的 `mod 24` orientation：

\[
\boxed{
\frac P5\equiv\frac{R_3}{2}\equiv11\pmod{24}.}
\tag{3.4}
\]

---

## 4. 公共 prime 只能来自四个 `sqrt(-6)` classes

先注意

\[
\gcd(G_{P3},30)=1.
\tag{4.1}
\]

`2,3` 不整除 `P`；而 `5\nmid R_3`，因为 `T\equiv0 (mod 5)` 且 `5\nmid a_3` 给

\[
R_3\equiv6a_3^2\not\equiv0\pmod5.
\]

固定 odd prime

\[
p\mid G_{P3}.
\]

则 `p|P` 且 `p\ne2,3`。由

\[
P=6(K-3)^2+1
\]
有

\[
(6(K-3))^2\equiv-6\pmod p.
\]

所以

\[
\boxed{\left(\frac{-6}{p}\right)=1.}
\tag{4.2}
\]

对 `p\nmid6`，这等价于

\[
\boxed{p\equiv1,5,7,11\pmod{24}.}
\tag{4.3}
\]

记

\[
\mathcal H_{24}:=\{1,5,7,11\}\subset(\mathbb Z/24\mathbb Z)^\times.
\]

它是 Klein 四群，且每个元素都满足

\[
u^{-1}=u\pmod{24}.
\tag{4.4}
\]

因为 `G_{P3}` 的每个 prime factor都在这些 classes中，

\[
\boxed{G_{P3}\bmod24\in\mathcal H_{24}.}
\tag{4.5}
\]

---

## 5. 约去完整 common gcd 后，两边 residual 的 `mod 24` 完全相同

定义

\[
\boxed{
P^{\rm res}:=\frac{P}{5G_{P3}},
\qquad
R_3^{\rm res}:=\frac{R_3}{2G_{P3}}.}
\tag{5.1}
\]

因为 `G_{P3}` 是完整 gcd，且固定 primes `2,5` 不共享，

\[
\boxed{\gcd(P^{\rm res},R_3^{\rm res})=1.}
\tag{5.2}
\]

由 (3.4)、(4.4)：

\[
\boxed{
P^{\rm res}
\equiv
R_3^{\rm res}
\equiv
11G_{P3}
\pmod{24}.}
\tag{5.3}
\]

所以完整 residue table 是

\[
\boxed{
\begin{array}{c|c|c}
G_{P3}\bmod24
&P^{\rm res}\bmod24
&R_3^{\rm res}\bmod24\\ \hline
1&11&11\\
5&7&7\\
7&5&5\\
11&1&1
\end{array}}
\tag{5.4}
\]

这是此前 `mod 4` parity pair 的严格增强。

---

## 6. 两个独立 binary characters 同时复制

表 (5.4) 同时编码两个 parity bits。

### 6.1 `3 mod 4` inert parity

两 residual 都为 `3 mod 4` 当且仅当

\[
G_{P3}\equiv1\pmod4.
\]

所以

\[
\boxed{
G_{P3}\equiv1\pmod4
\Longrightarrow
P^{\rm res}\equiv R_3^{\rm res}\equiv3\pmod4.}
\tag{6.1}
\]

由于两 residual 互素，它们各自必须携带一份 odd total `3 mod 4` prime parity，而且不能复用同一 prime。

### 6.2 `mod 3` nonresidue parity

两 residual 都为 `2 mod 3` 当且仅当

\[
G_{P3}\equiv1\pmod3.
\]

所以

\[
\boxed{
G_{P3}\equiv1\pmod3
\Longrightarrow
P^{\rm res}\equiv R_3^{\rm res}\equiv2\pmod3.}
\tag{6.2}
\]

因此同一个 common gcd 还决定是否复制第二份 `mod 3` nonresidue parity。

特别地：

- `G_{P3}=1 mod24`：两个 parity bits 同时复制；
- `G_{P3}=5 mod24`：只复制 odd-inert bit；
- `G_{P3}=7 mod24`：只复制 mod-3 bit；
- `G_{P3}=11 mod24`：两 bit 都由 common gcd 吸收，两个 residual 均 `1 mod24`。

---

## 7. 与 exact numerator/conjugate sheet split 联立

已有

\[
G_{P3}=G_-G_+,
\qquad
\gcd(G_-,G_+)=1,
\]

其中 target baseline primes只进入

\[
G_-:=\gcd(P,\alpha).
\]

由于 `G_-`、`G_+` 的 prime factors同样来自 `H_24`，

\[
G_-\bmod24,\ G_+\bmod24\in\mathcal H_{24}.
\tag{7.1}
\]

但 (5.4) 只固定乘积

\[
\boxed{G_-G_+=G_{P3}\pmod{24}.}
\tag{7.2}
\]

它**不固定** `G_-` 或 `G_+` 单独属于哪一个 class。

例如 `G_{P3}=11 mod24` 可以由

\[
(1,11),\ (11,1),\ (5,7),\ (7,5)
\]
四种 ordered sheet classes产生。

所以：

\[
\boxed{
\text{dual-short mod-24 parity 本身不能把某个 parity bit强制指派给 target numerator sheet }G_-.}
\tag{7.3}
\]

这是一条重要 no-double-count 审计。后续若要从 global parity 真正关闭 target，必须再加入一个能区分 `G_-` 与 `G_+` 的 independent orientation / additive input；不能只凭两个 short carriers都是 `11 mod24` 就宣称 target sheet承担奇 parity。

---

## 8. 当前 parity frontier

现在 dual-short pair 的 global arithmetic 被压成：

\[
\boxed{
\frac P5\equiv\frac{R_3}{2}\equiv11\pmod{24},}
\]

\[
\boxed{
G_{P3}=G_-G_+,\quad \gcd(G_-,G_+)=1,}
\]

\[
\boxed{
P^{\rm res}\equiv R_3^{\rm res}\equiv11G_{P3}\pmod{24}.}
\]

因此 common gcd 是否吸收/复制两个 parity bits 已完全确定；尚未确定的唯一离散自由是这两个 bits 在 numerator/conjugate 两张 common sheets之间的分配。

这说明下一步最有价值的输入应来自：

1. 能区分 `alpha` 与 `L_3` 的第二个 natural carrier；或
2. fixed `7/2671` 的 higher-depth Bezout；或
3. `Sigma_geom` 与 residual parity carrier之间的独立 additive relation。

本文不关闭 A2。

---

<a id="source-spontaneous-height-equal-depth-orthogonal-decimal-norm"></a>

> 整合来源：`spontaneous-height-equal-depth-orthogonal-decimal-norm.md`

# A2 equal-depth target 的 orthogonal decimal norm 与 fixed-exception complementarity

> **依赖：** `spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-equal-depth-triple-orientation.md`、`spontaneous-height-equal-depth-fixed-exception-transversality.md`、`spontaneous-height-equal-depth-dual-short-carriers.md`、`spontaneous-height-equal-depth-decimal-pair.md`。
>
> **严格状态：**本文把 source-prefix resultant `R_PD`、source/third cross orientation `L_D3` 与它的正交 companion 全部乘回真实 decimal concatenations。得到三个完全 source-free 的 natural integers，并证明它们满足一个 exact positive binary-norm identity。新的 orthogonal carrier 在所有 genuine deep equal-depth targets 上除 fixed `7` 的另一根外都精确读取 baseline；在 `p=7` 时，它与 `R_PD` 的 extra-depth root 恰好互补：`K=2` 只让 `R_PD` 加深，`K=4` 只让 orthogonal carrier 加深，二者不能同时坏。fixed `2671` 则只有 parallel cross carrier加深，另外两条仍精确 baseline。本文完成 fixed-exception 的三方向分流，但不排除 normalized higher cancellation，因此不关闭 A2。

---

## 1. decimal scaling

沿用

\[
\alpha=TK+a_3,\qquad
\beta=TQ+b_3,
\]

以及 exact determinant

\[
\Delta:=\Delta_\omega=Kb_3-Qa_3=E_MN\omega.
\]

记

\[
\boxed{c:=E_M\omega=\frac{\Delta}{N}.}
\tag{1.1}
\]

`Delta/N` 是整数。由

\[
\beta=E_MD\omega,
\qquad
U:=DK-N=qW_q,
\]
和 `E_+=E_M omega R_+`，有四条 exact decimalization：

\[
\boxed{cD=\beta,\qquad cN=\Delta,\qquad cU=Q\alpha,\qquad cR_+=E_+.}
\tag{1.2}
\]

其中第三条也可直接从

\[
K\beta-\Delta=Q\alpha
\]
看出。

对 genuine equal-depth target

\[
v_p(\omega)=v_p(W_q)=h\ge1,
\]
当前 denominator separation 给 `p∤E_MN`，因此

\[
\boxed{v_p(c)=h.}
\tag{1.3}
\]

---

## 2. source-prefix resultant 的完全 decimal 版本

定义

\[
R_{PD}:=55D^2-36DN+6N^2.
\]

把 (1.2) 直接代入，得到

\[
\boxed{
\Xi_{PD}
:=55\beta^2-36\beta\Delta+6\Delta^2
=c^2R_{PD}.}
\tag{2.1}
\]

它还具有正定形式

\[
\boxed{
\Xi_{PD}
=\beta^2+6(\Delta-3\beta)^2>0.}
\tag{2.2}
\]

以及

\[
\boxed{
55\Xi_{PD}
=(55\beta-18\Delta)^2+6\Delta^2.}
\tag{2.3}
\]

因此 target 上

\[
\boxed{
v_p(\Xi_{PD})=2h+v_p(R_{PD}).}
\tag{2.4}
\]

此前 target-ladder 已证明 deep resonance 中

\[
p\ne7\Longrightarrow v_p(R_{PD})=h.
\]
所以

\[
\boxed{
p\ne7\Longrightarrow v_p(\Xi_{PD})=3h.}
\tag{2.5}
\]

而 fixed `7` extra-resultant root会使 `v_7(Xi_PD)>3h`。

---

## 3. parallel cross carrier 的完全 decimal 版本

沿用

\[
L_{D3}
=T(55D-18N)-6N(a_3+3T).
\]

定义

\[
\boxed{
\Xi_{\parallel}
:=55T\beta-36T\Delta-6a_3\Delta.}
\tag{3.1}
\]

利用 (1.2)：

\[
\begin{aligned}
\Xi_{\parallel}
&=c\left[T(55D-18N)-6N(a_3+3T)\right]\\
&=cL_{D3}.
\end{aligned}
\]

所以

\[
\boxed{
\Xi_{\parallel}=cL_{D3},
\qquad
v_p(\Xi_{\parallel})=h+v_p(L_{D3}).}
\tag{3.2}
\]

`spontaneous-height-equal-depth-triple-orientation.md` 给

\[
p\ne2671\Longrightarrow v_p(L_{D3})=h.
\]
因此

\[
\boxed{
p\ne2671\Longrightarrow v_p(\Xi_{\parallel})=2h.}
\tag{3.3}
\]

fixed `2671` orientation exception 则满足

\[
\boxed{v_{2671}(\Xi_{\parallel})>2h.}
\tag{3.4}
\]

另由 decimal-pair identity `E_+=cR_+`、`cU=Qalpha` 可写成完全等价的 corrected form

\[
\boxed{
\Xi_{\parallel}
=T\left(E_+-(5K-36)Q\alpha\right)-6\Delta\alpha.}
\tag{3.5}
\]

这说明 fixed `2671` 的 normalized cancellation可以完全在真实 decimal integers中读取。

---

## 4. 新的 orthogonal cross carrier

令

\[
A_D:=55D-18N,
\qquad
u_3:=a_3+3T.
\]

`L_D3` 是

\[
L_{D3}=TA_D-6N\nu_3.
\]

定义其 binary norm 的正交 companion

\[
\boxed{
L_\perp:=A_D\nu_3+NT.}
\tag{4.1}
\]

乘以 `c` 后定义 pure decimal integer

\[
\boxed{
\Xi_\perp
:=(55\beta-18\Delta)(a_3+3T)+\Delta T.}
\tag{4.2}
\]

由 (1.2) 立刻有

\[
\boxed{
\Xi_\perp=cL_\perp.}
\tag{4.3}
\]

所以 target 上

\[
\boxed{
v_p(\Xi_\perp)=h+v_p(L_\perp).}
\tag{4.4}
\]

---

## 5. `L_perp` 的 deep next-layer formula

把

\[
a_3=\alpha-TK,
\qquad
U=DK-N,
\qquad
R_+=DP-KU,
\]

其中

\[
P=6K^2-36K+55,
\]
代入 (4.1)，直接展开得到

\[
\boxed{
L_\perp
=(55D-18N)\alpha
+3TR_+
+T(53-15K)U.}
\tag{5.1}
\]

固定 deep equal-depth target。已有

\[
v_p(\alpha)=2h,
\qquad
v_p(R_+)\ge h+1,
\qquad
v_p(U)=h.
\tag{5.2}
\]

且 `55D-18N` 是 p-unit：若 `p` 同时整除它与 `R_PD`，由

\[
55R_{PD}=(55D-18N)^2+6N^2
\]
和 `p∤6N` 得矛盾。

写

\[
U=p^hU_0,
\qquad p\nmid U_0.
\]

将 (5.1) 除以 `p^h` 并模 `p`，前两项消失，得到

\[
\boxed{
\frac{L_\perp}{p^h}
\equiv
T(53-15K)U_0
\pmod p.}
\tag{5.3}
\]

因此

\[
\boxed{
v_p(L_\perp)>h
\Longleftrightarrow
15K-53\equiv0\pmod p.}
\tag{5.4}
\]

---

## 6. orthogonal extra-depth 只有 fixed `7`，而且是 `P` 的另一根

`P` 与 `15K-53` 有 exact Bezout identity

\[
\boxed{
75P+(74-30K)(15K-53)=203=7\cdot29.}
\tag{6.1}
\]

因此若 genuine target prime同时满足

\[
p\mid P,
\qquad
p\mid15K-53,
\]
则

\[
p\mid203.
\]

当前 genuine inert target 满足

\[
p\equiv7\text{ 或 }11\pmod{24}.
\]
`29≡5 mod24` 不属于 genuine inert class，所以只剩

\[
\boxed{p=7.}
\tag{6.2}
\]

于是

\[
\boxed{
p\ne7\Longrightarrow v_p(L_\perp)=h}
\tag{6.3}
\]

以及纯 decimal 版本

\[
\boxed{
p\ne7\Longrightarrow v_p(\Xi_\perp)=2h.}
\tag{6.4}
\]

模 `7`，quadratic `P` 恰有两根

\[
\boxed{K\equiv2,4\pmod7.}
\tag{6.5}
\]

而

\[
15K-53\equiv K-4\pmod7,
\]
所以 orthogonal extra-depth精确选择

\[
\boxed{K\equiv4\pmod7.}
\tag{6.6}
\]

另一方面 target-ladder 的 fixed-7 `R_PD` exception满足

\[
36D-11N\equiv0\pmod7.
\]
配合 `DK≡N mod7`，它等价于

\[
36-11K\equiv0\pmod7,
\]
即

\[
\boxed{K\equiv2\pmod7.}
\tag{6.7}
\]

所以 fixed `7` 的两个 extra directions正好命中 `P` 的两张不同 simple roots。

---

## 7. fixed `7` 的 complementarity theorem

由 §§2、6：

### root `K=2 mod 7`

\[
\boxed{
v_7(R_{PD})>h,
\qquad
v_7(L_\perp)=h.}
\tag{7.1}
\]

对应 decimal depths

\[
\boxed{
v_7(\Xi_{PD})>3h,
\qquad
v_7(\Xi_\perp)=2h.}
\tag{7.2}
\]

### root `K=4 mod 7`

此时 `R_PD` 的 exceptional linear coefficient为 unit，所以

\[
\boxed{
v_7(R_{PD})=h,
\qquad
v_7(L_\perp)>h.}
\tag{7.3}
\]

对应

\[
\boxed{
v_7(\Xi_{PD})=3h,
\qquad
v_7(\Xi_\perp)>2h.}
\tag{7.4}
\]

因此无条件得到

\[
\boxed{
\min\{v_7(R_{PD}),v_7(L_\perp)\}=h.}
\tag{7.5}
\]

换句话说，fixed `7` 不可能同时让 source-prefix norm 与 orthogonal cross direction超过 baseline；两个“坏方向”被两张不同 roots彻底拆开。

---

## 8. exact decimal norm identity

由

\[
55R_{PD}=A_D^2+6N^2,
\qquad
R_3=T^2+6\nu_3^2,
\]
二次型 Lagrange identity给

\[
\boxed{
55R_{PD}R_3
=L_{D3}^2+6L_\perp^2.}
\tag{8.1}
\]

乘以 `c^2`，再使用 §§2--4 的 decimalization：

\[
\boxed{
55\Xi_{PD}R_3
=\Xi_{\parallel}^2+6\Xi_\perp^2.}
\tag{8.2}
\]

这是一个完全由真实 decimal concatenations / prefix integers构成的 positive binary norm identity。

---

## 9. 三方向 exact-depth table

对 genuine deep equal-depth target，三个 decimal directions现在有：

\[
\boxed{
\begin{array}{c|c|c|c}
\text{prime sector}
&v_p(\Xi_{PD})
&v_p(\Xi_{\parallel})
&v_p(\Xi_\perp)\\ \hline
p\notin\{7,2671\}
&3h&2h&2h\\
7,\ K\equiv2
&>3h&2h&2h\\
7,\ K\equiv4
&3h&2h&>2h\\
2671
&3h&>2h&2h
\end{array}}
\tag{9.1}
\]

其中 fixed `2671` 行使用 `2671≠7`，所以 `Xi_PD` 与 `Xi_perp` 都仍是 exact baseline。

这张表说明：

\[
\boxed{
\text{任何 genuine deep target 至多只有一个 orthogonal natural direction能超过 baseline。}}
\tag{9.2}
\]

moving sector三个方向全部 exact；fixed `7` 的两个 roots分别把 extra depth送入 `Xi_PD` 或 `Xi_perp`；fixed `2671` 只把 extra depth送入 `Xi_parallel`。

---

## 10. 当前 frontier

fixed exceptions现在已经被统一为同一个 decimal norm plane：

\[
55\Xi_{PD}R_3
=\Xi_{\parallel}^2+6\Xi_\perp^2.
\]

所以后续不再需要分别把 `7`、`2671` 当成孤立 resultant accident。真正剩余的是：

1. `p=7,K=2` 时 `Xi_parallel` 与 `Xi_perp` 两个 exact-baseline squares为何能在 (8.2) 中继续 cancellation；
2. `p=7,K=4` 时 orthogonal extra-depth `Xi_perp` 的 normalized cancellation；
3. `p=2671` 时 parallel extra-depth `Xi_parallel` 与 canonical full tail `Lambda_tail` 的关系；
4. moving `p∉{7,2671}` 时三方向全部 exact，因此所有 excess仍只能留在 `Lambda_tail` / residual companion sector。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-resonance"></a>

> 整合来源：`spontaneous-height-equal-depth-resonance.md`

# A2 height oversaturation 的 equal-depth resonance

> **依赖：** `spontaneous-height-oversaturation-depth-ledger.md`、`spontaneous-height-content-oversaturation.md`、`source-discriminant.md`、`primitive-reduction.md`。
>
> **严格状态：**前一 depth ledger 已证明 `e=v_p(omega)` 与 `h=v_p(W_q)` 不相等时，`J_H/B_W` 的较浅 residual oversaturation 被 `min(e,h)` 封顶。因此真正可能继续无界加深的只剩 `e=h`。本文把该 equal-depth branch 改写成两个自然整数 `A_H=g omega=z+c_u` 与 `B_H=qW_q=DK-N` 的 unit-ratio synchronization，并证明它对应的二次判别式恒为显式平方；所以 ordinary quadratic character / discriminant 不能再关闭该 branch。本文把剩余困难精确压成一个 projective unit ratio，不宣称 A2 closure。

---

## 1. equal-depth setting

固定 genuine non-`3` inert oversaturation prime `p`，令

\[
 e=v_p(\omega),
 \qquad
 h=v_p(W_q).
\]

本文只处理

\[
\boxed{e=h.}
\tag{1.1}
\]

写

\[
\omega=p^h\omega_0,
\qquad
W_q=p^hW_0,
\qquad
p\nmid\omega_0W_0.
\tag{1.2}
\]

于是原拼接 numerator

\[
\alpha=TK+a_3=\omega W_q
\]
满足精确赋值

\[
\boxed{v_p(\alpha)=2h.}
\tag{1.3}
\]

所以 equal-depth branch 的第一条硬结构是：指定 oversaturation prime 在真实 concatenated numerator 中形成一个**恰好偶深度的 p-primary block**。

---

## 2. 两个 natural height/content 线性形式具有同一深度

source triangle 为

\[
z=g\omega-c_u,
\qquad
f=g\omega+c_u,
\]
故

\[
\boxed{
g\omega=z+c_u.}
\tag{2.1}
\]

另有

\[
\boxed{qW_q=DK-N.}
\tag{2.2}
\]

定义

\[
\boxed{
A_H:=g\omega=z+c_u,
\qquad
B_H:=qW_q=DK-N.}
\tag{2.3}
\]

当前 prime 与 `gq` 分离，因此 (1.1) 等价于

\[
\boxed{
v_p(A_H)=v_p(B_H)=h.}
\tag{2.4}
\]

写

\[
A_H=p^hA_0,
\qquad
B_H=p^hB_0,
\qquad
p\nmid A_0B_0.
\tag{2.5}
\]

又因为 `alpha=omega W_q`：

\[
\boxed{A_HB_H=gq\alpha.}
\tag{2.6}
\]

因此 equal-depth 的两个 unit 并非独立：它们的乘积已经由真实 concatenated numerator 固定。

---

## 3. cross linear gate 变成唯一的 unit-ratio synchronization

前一文件的 cross gate 为

\[
L_{JB}=DzK+fN.
\]

利用

\[
f=z+2c_u,
\qquad
B_H=DK-N,
\qquad
A_H=z+c_u,
\]
直接展开：

\[
\begin{aligned}
L_{JB}
&=zDK+(z+2c_u)N\\
&=z(DK-N)+2N(z+c_u)\\
&=zB_H+2NA_H.
\end{aligned}
\]

所以有 exact identity

\[
\boxed{
L_{JB}=2NA_H+zB_H.}
\tag{3.1}
\]

定义 resonance depth

\[
\boxed{
\rho_p
:=v_p(2NA_0+zB_0)\ge0.}
\tag{3.2}
\]

则

\[
\boxed{v_p(L_{JB})=h+\rho_p.}
\tag{3.3}
\]

特别地，`rho_p>=r` 等价于唯一 projective ratio

\[
\boxed{
B_0\equiv-2Nz^{-1}A_0\pmod{p^r}.}
\tag{3.4}
\]

所以 equal-depth 的所有额外 Hensel 深化不再是一棵多分支系统：给定 `A_0` 后，`B_0` 的 unit class 被唯一确定。

---

## 4. resonance 与 `J_H/B_W` difference 的精确深度

前一 depth ledger 已得到

\[
5^{2d}
\left(
\widehat{\mathcal J}_H-(2^mg)^2\mathscr B_W
\right)
=-qzW_qL_{JB}.
\tag{4.1}
\]

由于 `p\nmid5qz`，结合 (3.3)：

\[
\boxed{
v_p\!\left(
\widehat{\mathcal J}_H-(2^mg)^2\mathscr B_W
\right)
=2h+\rho_p.}
\tag{4.2}
\]

这说明 equal-depth branch 中所有超出 generic `2h` 的 companion synchronization，都被**同一个** `rho_p` 精确读取。

---

## 5. `A_H,B_H,L_JB` 自带一个 exact square discriminant

由 (2.6) 与 (3.1)，把 `B_H` 消掉：

\[
A_H(L_{JB}-2NA_H)
=zA_HB_H
=zgq\alpha.
\]
因此

\[
\boxed{
2NA_H^2-L_{JB}A_H+zgq\alpha=0.}
\tag{5.1}
\]

把它看成关于 `A_H` 的 quadratic，判别式为

\[
\Delta_{\rm eq}
:=L_{JB}^2-8Nzgq\alpha.
\tag{5.2}
\]

但直接使用 (3.1)、(2.6)：

\[
\begin{aligned}
\Delta_{\rm eq}
&=(2NA_H+zB_H)^2-8NzA_HB_H\\
&=(2NA_H-zB_H)^2.
\end{aligned}
\]

所以得到 exact square identity

\[
\boxed{
L_{JB}^2-8Nzgq\alpha
=(2NA_H-zB_H)^2.}
\tag{5.3}
\]

这不是新 obstruction；它说明 equal-depth resonance 的 quadratic discriminant **全局就是平方**。

---

## 6. deep resonance 下 complementary linear form 恰停在 `h`

设

\[
\rho_p\ge1.
\]

由 (3.2)：

\[
2NA_0+zB_0\equiv0\pmod p.
\tag{6.1}
\]

定义 complementary form

\[
\boxed{M_{JB}:=2NA_H-zB_H.}
\tag{6.2}
\]

除以 `p^h` 后，利用 (6.1)：

\[
\frac{M_{JB}}{p^h}
=2NA_0-zB_0
\equiv4NA_0\not\equiv0\pmod p,
\]
因为 genuine prime 满足 `p\nmid2NA_0`。于是

\[
\boxed{v_p(M_{JB})=h
\qquad(\rho_p\ge1).}
\tag{6.3}
\]

因此 (5.3) 的右侧在 deep resonance 中赋值**精确**为 `2h`。

---

## 7. quadratic-character 路线在 equal-depth resonance 中自动退化

把 (5.3) 除以 `p^{2h}`，并令

\[
\alpha_0:=\alpha/p^{2h}.
\]

若 `rho_p>=1`，则模 `p` 有

\[
-8Nzgq\alpha_0
\equiv
\left(\frac{M_{JB}}{p^h}\right)^2
\equiv
(4NA_0)^2.
\tag{7.1}
\]

所以任何试图从 resonance 导出

\[
\left(\frac{-8Nzgq\alpha_0}{p}\right)=-1
\]
的 ordinary discriminant obstruction 都不可能成立；实际恒有

\[
\boxed{
\left(\frac{-8Nzgq\alpha_0}{p}\right)=1.}
\tag{7.2}
\]

而且这个 square class 已由 (3.4) 的 unit ratio自动解释，不是独立条件。

因此：

\[
\boxed{
\text{equal-depth resonance}
\Longrightarrow
\text{projective unit synchronization, not a new quadratic character}.}
\tag{7.3}
\]

---

## 8. 当前 equal-depth frontier

综合 §§1–7，真正剩余的 branch 已压成

\[
\boxed{
\begin{gathered}
p\equiv7,11\pmod{24},\\
v_p(\omega)=v_p(W_q)=h\ge1,\\
v_p(\alpha)=2h,\\
v_p(g\omega)=v_p(qW_q)=h,\\
B_0/A_0
\equiv-2Nz^{-1}\pmod{p^{\rho_p}},\\
v_p\!\left(
\widehat{\mathcal J}_H-(2^mg)^2\mathscr B_W
\right)=2h+\rho_p.
\end{gathered}}
\tag{8.1}
\]

同时 (5.3) 已证明 discriminant/Legendre 方向只是平方 shadow。

所以后续真正可能推进 closure 的输入只能来自：

1. 把 ratio (3.4) 与 decimal determinant `K b_3-Q a_3` 联立；
2. 把 `A_H=z+c_u`、`B_H=DK-N` 的单位代表与 endpoint Hensel slot 的**自然代表大小**联立；
3. 或证明 `alpha=TK+a_3` 的 exact square p-primary depth `2h` 与第三块窄窗不相容。

继续 ordinary quadratic character、判别式或重复 simple-root Hensel 不会产生新 closure。

---

<a id="source-spontaneous-height-equal-depth-serial-conjugates"></a>

> 整合来源：`spontaneous-height-equal-depth-serial-conjugates.md`

# A2 serial tropical nodes 的 conjugate exact-depth sheets

> **依赖：** `spontaneous-height-equal-depth-serial-tropical-bridge.md`。
>
> **严格状态：**serial bridge 把旧四类 minimum ties压成两个二项 cancellation nodes。本文对两个节点分别加入 sum/difference conjugate。若某一张 sheet 发生 strict-extra，另一张 conjugate sheet在 odd target上必精确停在 baseline，不能同时深化。第二节点的 conjugate `D_E=beta C_BE-K Lambda_dec` 还是一个 positive pure-decimal integer，并有 `1311 T^2 N^4 < D_E < 1339 T^2 N^4`。本文完成 tie-sheet separation，但不排除 deep sheet本身，因此不关闭 A2。

---

## 1. notation

沿用

\[
F:=F_{\rm dec}=TQ+2b_3,
\]

\[
C:=C_{BE}=FP-2K^2\beta,
\]

以及 serial exact bridges

\[
\boxed{FB_{\rm dec}-TQK^2\beta^2=b_3^2C,}
\tag{1.1}
\]

\[
\boxed{FE_+=K\Lambda_{\rm dec}+\beta C.}
\tag{1.2}
\]

固定 genuine deep equal-depth odd prime `p`，并写

\[
v_p(B_{\rm dec})=h+r_B,
\quad
v_p(C)=h+c_p,
\]

\[
v_p(\Lambda_{\rm dec})=2h+\rho_p,
\quad
v_p(E_+)=2h+r_+.
\]

所有显式 coefficients 在 target上均为 `p`-units。

---

## 2. first-node conjugate

定义

\[
\boxed{
D_B:=FB_{\rm dec}+TQK^2\beta^2.}
\tag{2.1}
\]

考虑 first-node strict-extra branch

\[
\boxed{r_B=h,\qquad c_p>h.}
\tag{2.2}
\]

此时

\[
v_p(FB_{\rm dec})=2h,
\qquad
v_p(TQK^2\beta^2)=2h,
\]
而由 (1.1)

\[
v_p(FB_{\rm dec}-TQK^2\beta^2)>2h.
\]

写

\[
FB_{\rm dec}=p^{2h}u,
\qquad
TQK^2\beta^2=p^{2h}v,
\]
其中 `u,v` 为 units。difference deep说明

\[
u\equiv v\pmod p.
\]

因为 `p` 为 odd：

\[
u+v\equiv2u\not\equiv0\pmod p.
\]

所以

\[
\boxed{v_p(D_B)=2h.}
\tag{2.3}
\]

即 first node 的 difference sheet `C` 一旦 extra，sum sheet `D_B` 精确 baseline。

---

## 3. second-node conjugate

定义

\[
\boxed{
D_E:=\beta C-K\Lambda_{\rm dec}.}
\tag{3.1}
\]

考虑 second-node strict tie

\[
\boxed{c_p=\rho_p=:s,\qquad r_+>s.}
\tag{3.2}
\]

于是

\[
v_p(\beta C)=2h+s,
\qquad
v_p(K\Lambda_{\rm dec})=2h+s,
\]
而 (1.2) 给

\[
v_p(K\Lambda_{\rm dec}+\beta C)>2h+s.
\]

写

\[
\beta C=p^{2h+s}u,
\qquad
K\Lambda_{
m dec}=p^{2h+s}v,
\]
其中 `u,v` 为 units。sum deep说明

\[
u+v\equiv0\pmod p,
\qquad
u\equiv-v\pmod p.
\]

因此

\[
u-v\equiv-2v\not\equiv0\pmod p
\]
因为 `p` odd。故

\[
\boxed{v_p(D_E)=2h+s.}
\tag{3.3}
\]

所以 second node 的 actual sum sheet `FE_+` 一旦 strict-extra，conjugate difference sheet `D_E` 恰好停在 tied baseline。

---

## 4. `D_E` is positive and short

serial bridge 已证明

\[
839TN^3<C<843TN^3.
\tag{4.1}
\]

已有 endpoint bounds

\[
\frac{21}{10}<\frac{\beta}{TN}<\frac{211}{100},
\tag{4.2}
\]

\[
\frac{2499}{250}<\frac KN<10,
\tag{4.3}
\]

以及 full-tail window

\[
44T^2N^3<\Lambda_{\rm dec}<45T^2N^3.
\tag{4.4}
\]

因此

\[
\frac{D_E}{T^2N^4}
=
\frac{\beta}{TN}\frac{C}{TN^3}
-
\frac KN\frac{\Lambda_{\rm dec}}{T^2N^3}.
\]

下界：

\[
\frac{D_E}{T^2N^4}
>
\frac{21}{10}\cdot839-10\cdot45
=1311.9>1311.
\]

上界：

\[
\frac{D_E}{T^2N^4}
<
\frac{211}{100}\cdot843
-
\frac{2499}{250}\cdot44
=1338.906<1339.
\]

所以

\[
\boxed{
1311T^2N^4<D_E<1339T^2N^4.}
\tag{4.5}
\]

特别地

\[
\boxed{D_E>0}
\]
且

\[
\boxed{D_E\text{ 恰有 }2m+4M+4\text{ 位}.}
\tag{4.6}
\]

---

## 5. sum/difference recovery

由定义与 (1.2)：

\[
\boxed{
FE_++D_E=2\beta C,}
\tag{5.1}
\]

\[
\boxed{
FE_+-D_E=2K\Lambda_{\rm dec}.}
\tag{5.2}
\]

因此 second-node 的 actual/conjugate pair完全恢复两个 tied components。

在 strict tie target上：

\[
\boxed{
\begin{array}{c|c}
\text{carrier}&p\text{-depth}\\ \hline
FE_+&>2h+s\\
D_E&=2h+s.
\end{array}}
\tag{5.3}
\]

这与 earlier `E_+/E_-`、source/third four-sheet split具有同样的“one deep / one exact”结构。

---

## 6. current interpretation

serial tie mechanism现在不仅被压成两个节点，而且每个节点内部也只有一张 sheet可继续 deep：

- first-node extra：`C` deep，`D_B` exact baseline；
- second-node extra：`FE_+` deep，`D_E` exact baseline。

因此不存在同一节点的 sum/difference 双深机制。后续真正需要控制的是 deep sheet 本身的 higher normalized unit，而不是继续寻找同节点的第二条深 Hensel branch。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-serial-gcd-selectors"></a>

> 整合来源：`spontaneous-height-equal-depth-serial-gcd-selectors.md`

# A2 serial strict resonance 的 canonical gcd selectors

> **依赖：** `spontaneous-height-equal-depth-serial-tropical-bridge.md`、`spontaneous-height-equal-depth-middle-near-pair.md`、`spontaneous-height-equal-depth-tail-normalization.md`、`spontaneous-height-equal-depth-geometric-selector.md`。
>
> **严格状态：**本文把 serial bridge 剩下的 two-node higher cancellation完全改写成 ordinary integer gcd ladders，不再预枚举 target primes。first-node relevant strict branch由两个 `Omega`-ladder quotients选择；second-node 的“`c_p=rho_p` 且 `r_+>rho_p`”则由单个 two-level gcd quotient自动选择，连 equal-depth 条件都无需单独写。二者交集精确对应唯一的 double-serial danger `r_B=h<c_p=rho_p<r_+`。本文把剩余局部机制 canonical 化，但不证明这些 selectors 为 `1`，因此不关闭 A2。

---

## 1. canonical residual readers

沿用 middle near-pair

\[
C_+=C_{BE},
\qquad
C_-=A_P\beta-b_3P,
\]

并定义

\[
\boxed{G_C:=\gcd(C_+,C_-),}
\tag{1.1}
\]

\[
\boxed{C_{\rm tail}:=\frac{C_+}{G_C}.}
\tag{1.2}
\]

对 genuine deep equal-depth target，middle near-pair 已证明

\[
v_p(C_+)=h+c_p,
\qquad
v_p(C_-)=h.
\]

因此

\[
\boxed{v_p(G_C)=h,}
\tag{1.3}
\]

\[
\boxed{v_p(C_{\rm tail})=c_p.}
\tag{1.4}
\]

full-tail normalization 已有 canonical quotient

\[
\Lambda_{\rm tail}
:=\frac{\Lambda_{\rm dec}}{\gcd(\alpha,\Lambda_{\rm dec})},
\]
并在 equal-depth target 上精确满足

\[
\boxed{v_p(\Lambda_{\rm tail})=\rho_p.}
\tag{1.5}
\]

最后定义 baseline common carrier

\[
\boxed{\Omega:=\gcd(P,\beta).}
\tag{1.6}
\]

因为 target 上

\[
v_p(P)=v_p(\beta)=h,
\]
故

\[
\boxed{v_p(\Omega)=h.}
\tag{1.7}
\]

所以 `(Omega,C_tail,Lambda_tail)` 分别给出

\[
\boxed{h,\ c_p,\ \rho_p}
\]
三个完全 canonical 的 local depth readers。

---

## 2. first-node depth-over-baseline ladder

对任意正整数 `X` 定义相对于 `Omega` 的二级 quotient

\[
\boxed{
\mathcal R_\Omega(X)
:=
\frac{\gcd(\Omega^2,X)}{\gcd(\Omega,X)}.}
\tag{2.1}
\]

分母总整除分子，因为 `Omega|Omega^2`。

若 target 上

\[
v_p(\Omega)=h,
\qquad
v_p(X)=x,
\]
则

\[
\boxed{
v_p(\mathcal R_\Omega(X))
=\min(2h,x)-\min(h,x).}
\tag{2.2}
\]

因此

\[
\boxed{
p\mid\mathcal R_\Omega(X)
\Longleftrightarrow
x>h.}
\tag{2.3}
\]

应用于两个 residual readers：

\[
\boxed{
R_C:=\mathcal R_\Omega(C_{\rm tail}),}
\tag{2.4}
\]

\[
\boxed{
R_\Lambda:=\mathcal R_\Omega(\Lambda_{\rm tail}).}
\tag{2.5}
\]

于是 target 上

\[
\boxed{p\mid R_C\Longleftrightarrow c_p>h,}
\tag{2.6}
\]

\[
\boxed{p\mid R_\Lambda\Longleftrightarrow \rho_p>h.}
\tag{2.7}
\]

---

## 3. canonical first-node strict selector

沿用此前 geometric deep-target selector `Sigma_geom`。定义

\[
\boxed{
\Sigma_{\rm first}
:=\gcd(\Sigma_{\rm geom},R_C,R_\Lambda).}
\tag{3.1}
\]

在 genuine deep target sector 中：

\[
\boxed{
p\mid\Sigma_{\rm first}
\Longleftrightarrow
c_p>h,\quad\rho_p>h.}
\tag{3.2}
\]

serial first-node law 又说明 `c_p>h` 只能发生在

\[
\boxed{r_B=h.}
\tag{3.3}
\]

而 `c_p,rho_p>h` 使 second-node minimum本身已大于 `h`，所以

\[
\boxed{r_+>h.}
\tag{3.4}
\]

因此 `Sigma_first` 在当前 genuine sector精确选择此前的 first-node relevant strict mechanism：

\[
\boxed{
r_B=h<\rho_p,\quad r_+>h}
\]
以及其中可能进一步满足 `c_p=rho_p` 的更深 subcase。

更规范地说，它选择

\[
\boxed{r_B=h,\quad c_p>h,\quad\rho_p>h.}
\tag{3.5}
\]

---

## 4. second-node common core

定义两个 residual readers 的 common core

\[
\boxed{
G_2:=\gcd(C_{\rm tail},\Lambda_{\rm tail}).}
\tag{4.1}
\]

在 target 上令

\[
s:=\min(c_p,\rho_p).
\]
则

\[
\boxed{v_p(G_2)=s.}
\tag{4.2}
\]

不需要预先判断 `c_p=rho_p`；`G_2` 只记录两者的公共最浅层。

---

## 5. second-node strict ladder

定义

\[
\boxed{
A_1:=\gcd(\Omega^2G_2,\ F_{\rm dec}E_+),}
\tag{5.1}
\]

\[
\boxed{
A_2:=\gcd(\Omega^2G_2^2,\ F_{\rm dec}E_+),}
\tag{5.2}
\]

以及 quotient

\[
\boxed{
R_{\rm second}:=\frac{A_2}{A_1}.}
\tag{5.3}
\]

因为 `G_2|G_2^2`，有

\[
\Omega^2G_2\mid\Omega^2G_2^2,
\]
故 `A_1|A_2`，所以 (5.3) 是整数。

在 genuine target 上 `F_dec` 是 unit，并且

\[
v_p(E_+)=2h+r_+.
\]

所以

\[
v_p(A_1)
=\min(2h+s,2h+r_+).
\]

serial law 给

\[
r_+\ge s,
\]
故

\[
\boxed{v_p(A_1)=2h+s.}
\tag{5.4}
\]

同理

\[
v_p(A_2)
=2h+\min(2s,r_+).
\]

因此

\[
\boxed{
v_p(R_{\rm second})
=\min(2s,r_+)-s
=\min(s,r_+-s).}
\tag{5.5}
\]

这是 second-node strictness 的 canonical valuation formula。

---

## 6. equal-depth condition is detected automatically

若

\[
c_p\ne\rho_p,
\]
serial second-node law给唯一 minimum：

\[
r_+=s.
\]

代入 (5.5)：

\[
\boxed{v_p(R_{\rm second})=0.}
\tag{6.1}
\]

若

\[
c_p=\rho_p=s,
\]
则：

- 若没有 strict cancellation，`r_+=s`，仍有 `v_p(R_second)=0`；
- 若发生 strict cancellation，`r_+>s`，则
  \[
  \boxed{v_p(R_{\rm second})=\min(s,r_+-s)>0.}
  \tag{6.2}
  \]

所以在 genuine deep target sector：

\[
\boxed{
p\mid R_{\rm second}
\Longleftrightarrow
c_p=\rho_p=:s,\quad r_+>s.}
\tag{6.3}
\]

这是最重要的点：一个 ordinary gcd quotient自动同时检测了

1. second-node 两 residual depths相等；
2. actual sum sheet发生 strict-extra。

无需 factorization，也无需把 `c_p=rho_p` 当作额外负条件手工检查。

---

## 7. canonical second-node selector

定义

\[
\boxed{
\Sigma_{\rm second}
:=\gcd(\Sigma_{\rm geom},R_{\rm second}).}
\tag{7.1}
\]

则在 current genuine deep target sector：

\[
\boxed{
p\mid\Sigma_{\rm second}
\Longleftrightarrow
c_p=\rho_p,\quad r_+>\rho_p.}
\tag{7.2}
\]

所以 serial bridge 的第二个 remaining mechanism现在也被一个 canonical integer selector完全恢复。

---

## 8. double-serial selector

最后定义

\[
\boxed{
\Sigma_{\rm double}
:=\gcd(\Sigma_{\rm first},\Sigma_{\rm second}).}
\tag{8.1}
\]

若 genuine target prime进入该 gcd，则同时有

\[
c_p>h,
\qquad
\rho_p>h,
\]
以及

\[
c_p=\rho_p,
\qquad
r_+>\rho_p.
\]

所以精确得到

\[
\boxed{
r_B=h<c_p=\rho_p<r_+.}
\tag{8.2}
\]

反过来任何满足 (8.2) 的 genuine deep target都进入 `Sigma_double`。

因此：

\[
\boxed{
p\mid\Sigma_{\rm double}
\Longleftrightarrow
r_B=h<c_p=\rho_p<r_+.}
\tag{8.3}
\]

这就是 serial hierarchy 中唯一“两级都 extra”的最危险 orbit。

---

## 9. current canonical frontier

剩余 equal-depth local danger现在可完全由三个普通整数描述：

\[
\boxed{
\Sigma_{\rm first},\qquad
\Sigma_{\rm second},\qquad
\Sigma_{\rm double}.}
\]

其中：

- `Sigma_first`：第一节点超过 baseline，同时 tail也超过 baseline；
- `Sigma_second`：第二节点 equal-depth 后 actual sheet strict-extra；
- `Sigma_double`：唯一双级 serial extra，满足
  \[
  r_B=h<c_p=\rho_p<r_+.
  \]

后续无需继续 prime-by-prime 分类旧四种 tie。最值得攻击的是 `Sigma_double` 的全局高度/奇素数 parity；若它为空，则两个 serial nodes不能同时无界深化。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-serial-parity-neutrality"></a>

> 整合来源：`spontaneous-height-equal-depth-serial-parity-neutrality.md`

# A2 serial-first pool 对 `B_W` inert parity 的中性化

> **依赖：** `source-discriminant.md`、`spontaneous-height-equal-depth-serial-gcd-selectors.md`。
>
> **严格状态：**source cofactor `B_W` 是 positive `7 mod 8` integer，因此其 `3 mod 4` prime总赋值 parity为奇。本文观察到所有 genuine `Sigma_first` primes均满足 `r_B=h`，故在 `B_W` 中的 exponent 恰为 `2h`，对 inert parity贡献恒为偶。于是 serial-first pool（更包括其子池 `Sigma_double`）不可能承担 `B_W` 的全局奇 parity；必存在至少一枚 `3 mod 4` 的 complement prime在 `B_W` 中具有奇赋值。本文只给 parity allocation，不证明该 complement prime与其它 companion supplier必须不同，因此不关闭 A2。

---

## 1. global source parity

`source-discriminant.md` 已证明

\[
\boxed{\mathscr B_W\equiv7\pmod8.}
\tag{1.1}
\]

因此 `B_W` 为 positive odd `3 mod 4` integer，并有

\[
\boxed{
\sum_{\substack{r\equiv3\ (4)}}
v_r(\mathscr B_W)
\equiv1\pmod2.}
\tag{1.2}
\]

这里求和遍历 `B_W` 的全部 odd inert prime divisors，包括 fixed 与 moving sources。

---

## 2. every serial-first target has even `B_W` exponent

固定 genuine prime由 `Sigma_first` 选择。serial gcd selector theorem给

\[
\boxed{r_B=h,}
\tag{2.1}
\]

其中定义

\[
v_p(\mathscr B_W)=h+r_B.
\]

所以

\[
\boxed{v_p(\mathscr B_W)=2h.}
\tag{2.2}
\]

当前 genuine target primes满足

\[
p\equiv7\text{ or }11\pmod{24},
\]
特别地

\[
p\equiv3\pmod4.
\]

因此每一个 serial-first target虽然本身是 inert prime，但它对 (1.2) 的 parity贡献为

\[
\boxed{2h\equiv0\pmod2.}
\tag{2.3}
\]

---

## 3. the whole serial-first pool is parity-neutral

令 `E_first` 表示 genuine `Sigma_first` target prime集合。则由 (2.2)：

\[
\boxed{
\sum_{p\in E_{\rm first}}v_p(\mathscr B_W)
=2\sum_{p\in E_{\rm first}}h_p
\equiv0\pmod2.}
\tag{3.1}
\]

所以从 global parity ledger (1.2) 中删去整个 serial-first pool后，剩余 complement仍必须保持奇 parity：

\[
\boxed{
\sum_{\substack{r\equiv3\ (4)\\r\notin E_{\rm first}}}
v_r(\mathscr B_W)
\equiv1\pmod2.}
\tag{3.2}
\]

特别地，存在至少一枚 odd prime

\[
\boxed{r\equiv3\pmod4,\qquad r\notin E_{\rm first}}
\tag{3.3}
\]
满足

\[
\boxed{v_r(\mathscr B_W)\text{ 为奇数}.}
\tag{3.4}
\]

这是严格的存在性，不依赖 factorization certificate。

---

## 4. double-serial pool is also neutral

已有

\[
\Sigma_{\rm double}\mid\Sigma_{\rm first}
\]
在 support意义上成立，因为

\[
\Sigma_{\rm double}=\gcd(\Sigma_{\rm first},\Sigma_{\rm second}).
\]

所以 genuine double-serial prime同样满足 (2.2)。令 `E_dbl` 为 genuine double-serial prime集合，则

\[
\boxed{
\sum_{p\in E_{\rm dbl}}v_p(\mathscr B_W)
\equiv0\pmod2.}
\tag{4.1}
\]

因此 `Sigma_double` 即使非空，也不可能自己解释 `B_W≡7 mod8` 的奇 inert parity。

---

## 5. correct allocation consequence

本文并没有证明 (3.3) 的 complement prime属于哪个旧 source label。严格结论只有：

\[
\boxed{
B_W\text{ 的必需 odd inert parity必须由 serial-first pool之外的 support承担}.}
\tag{5.1}
\]

所以后续若能结合已有 residual parity doubling / support separation证明：

- complement prime不能回到 fixed denominator/content support；
- 或 companion residual parity不能复用这枚 complement prime；

就会被迫生成第二枚独立 inert prime并产生新的 product-height surcharge。

不能仅凭 (5.1) 宣称 contradiction。

---

## 6. current role

serial hierarchy现在同时具有：

1. canonical selectors `Sigma_first`, `Sigma_second`, `Sigma_double`；
2. double-serial weighted budget `G_dbl^3 rad(G_dbl)^2`；
3. 本文的 source parity neutrality。

所以 double/first serial pools一方面昂贵，另一方面又不能承担 `B_W` 的全局 odd-inert parity。下一步最有价值的是把强制存在的 complement inert prime送入已有 residual-parity support ledger，尝试证明它与 serial pool及 companion parity supplier三者两两分离。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-serial-tropical-bridge"></a>

> 整合来源：`spontaneous-height-equal-depth-serial-tropical-bridge.md`

# A2 equal-depth minimum ties 的 serial tropical bridge

> **依赖：** `spontaneous-height-equal-depth-decimal-tropical-identity.md`、`spontaneous-height-equal-depth-three-cancellation-readers.md`。
>
> **严格状态：**此前 `E_+` 的 strict-extra 只能来自 `min(r_B,h,rho_p)` 的三类 pair tie 或 triple tie。本文引入一个新的纯 decimal 中间 carrier `C_BE=F_dec P-2K^2 beta`，证明原三项 tropical identity 精确分解成两条二项 bridge。第一节点只比较 `r_B` 与 `h`，第二节点只比较新的中间深度 `c_p` 与 `rho_p`。因此四种旧 tie 被压成两个串联 cancellation nodes；特别地，triple tie 若要 `E_+` strict-extra，第一节点反而必须精确停在 baseline，不能同时 extra。本文不排除第二节点的 higher cancellation，因此不关闭 A2。

---

## 1. notation

沿用

\[
P:=6K^2-36K+55,
\qquad
F_{\rm dec}:=TQ+2b_3,
\]

\[
\alpha=TK+a_3,
\qquad
\beta=TQ+b_3,
\]

以及三个 decimal readers

\[
B_{\rm dec}
=b_3^2(P-K^2)+T^2Q^2K^2,
\]

\[
E_+=P\beta-KQ\alpha,
\]

\[
\Lambda_{\rm dec}
=2K\beta^2-QF_{\rm dec}\alpha.
\]

固定 genuine deep equal-depth target prime `p`：

\[
v_p(P)=v_p(\beta)=h\ge1,
\qquad
v_p(\alpha)=2h,
\]

\[
v_p(B_{\rm dec})=h+r_B,
\qquad
v_p(\Lambda_{\rm dec})=2h+\rho_p,
\]

\[
v_p(E_+)=2h+r_+,
\qquad
r_B,\rho_p,r_+\ge1.
\]

当前 genuine separation 给

\[
p\nmid b_3TQKF_{\rm dec}.
\]

---

## 2. middle decimal carrier

定义

\[
\boxed{
C_{BE}:=F_{\rm dec}P-2K^2\beta.}
\tag{2.1}
\]

它完全由真实 prefix/decimal integers 构成。

### 2.1 first exact bridge

由

\[
B_{\rm dec}
=b_3^2P+K^2(TQ-b_3)\beta
\]
直接计算：

\[
\begin{aligned}
F_{\rm dec}B_{\rm dec}-TQK^2\beta^2
={}&b_3^2F_{\rm dec}P\\
&+K^2\beta\left[F_{\rm dec}(TQ-b_3)-TQ\beta\right].
\end{aligned}
\]

因为

\[
F_{\rm dec}(TQ-b_3)-TQ\beta
=(TQ+2b_3)(TQ-b_3)-TQ(TQ+b_3)
=-2b_3^2,
\]
所以

\[
\boxed{
F_{\rm dec}B_{\rm dec}
-TQK^2\beta^2
=b_3^2C_{BE}.}
\tag{2.2}
\]

### 2.2 second exact bridge

另一方面

\[
\begin{aligned}
F_{\rm dec}E_+-K\Lambda_{\rm dec}
={}&F_{\rm dec}(P\beta-KQ\alpha)\\
&-K(2K\beta^2-QF_{\rm dec}\alpha)\\
={}&\beta(F_{\rm dec}P-2K^2\beta).
\end{aligned}
\]

故

\[
\boxed{
F_{\rm dec}E_+
-K\Lambda_{\rm dec}
=\beta C_{BE}.}
\tag{2.3}
\]

原三项 tropical identity因此不是一个不可分的三项式，而是 (2.2) 与 (2.3) 两个串联二项节点。

---

## 3. `C_BE` 的 short positive window

写

\[
s:=K/N,
\qquad q:=Q/N,
\qquad w:=b_3/T.
\]

endpoint 给

\[
\frac{2499}{250}<s<10,
\qquad
\frac{21}{10}<q<\frac{40}{19},
\qquad
0<w<\frac{843}{1000},
\qquad
N\ge10^{11}.
\]

由定义

\[
\frac{C_{BE}}{TN^3}
=
q\left(4s^2-\frac{36s}{N}+\frac{55}{N^2}\right)
+\frac{2w}{N}
\left(5s^2-\frac{36s}{N}+\frac{55}{N^2}\right).
\tag{3.1}
\]

第二项为正。用 `q>21/10,s>2499/250,s<10,N>=10^11`：

\[
\frac{C_{BE}}{TN^3}
>
\frac{21}{10}
\left[
4\left(\frac{2499}{250}\right)^2
-\frac{360}{10^{11}}
\right]
>839.
\]

上界则丢掉所有负项并用 `q<40/19,s<10,w<843/1000`：

\[
\frac{C_{BE}}{TN^3}
<
\frac{40}{19}
\left(400+\frac{55}{10^{22}}\right)
+
\frac{2}{10^{11}}\frac{843}{1000}
\left(500+\frac{55}{10^{22}}\right)
<843.
\]

所以

\[
\boxed{
839TN^3<C_{BE}<843TN^3.}
\tag{3.2}
\]

特别地

\[
\boxed{C_{BE}>0}
\]
并且

\[
\boxed{C_{BE}\text{ 恰有 }m+3M+3\text{ 位}.}
\tag{3.3}
\]

它比 `E_+` 的 `m+3M+4` 位短一位十进制数字。

---

## 4. first-node valuation law

定义中间 residual depth

\[
\boxed{c_p:=v_p(C_{BE})-h.}
\tag{4.1}
\]

由 (2.2)，三项赋值为

\[
v_p(F_{\rm dec}B_{\rm dec})=h+r_B,
\]

\[
v_p(TQK^2\beta^2)=2h,
\]

\[
v_p(b_3^2C_{BE})=h+c_p.
\]

因此

\[
\boxed{c_p\ge\min(r_B,h).}
\tag{4.2}
\]

若

\[
r_B\ne h,
\]
左边差式中存在唯一最浅项，所以

\[
\boxed{c_p=\min(r_B,h).}
\tag{4.3}
\]

只有

\[
\boxed{r_B=h}
\tag{4.4}
\]
时，第一节点才能让 `C_BE` 比 `2h` 更深，即

\[
c_p>h.
\]

另外当前 `r_B,h>=1`，故无条件有

\[
\boxed{c_p\ge1,\qquad p^{h+1}\mid C_{BE}.}
\tag{4.5}
\]

---

## 5. second-node valuation law

由 (2.3)：

\[
F_{\rm dec}E_+=K\Lambda_{\rm dec}+\beta C_{BE}.
\]

三项赋值为

\[
v_p(F_{\rm dec}E_+)=2h+r_+,
\]

\[
v_p(K\Lambda_{\rm dec})=2h+\rho_p,
\]

\[
v_p(\beta C_{BE})=2h+c_p.
\]

所以

\[
\boxed{r_+\ge\min(\rho_p,c_p).}
\tag{5.1}
\]

若

\[
\rho_p\ne c_p,
\]
右边有唯一最浅项，因此

\[
\boxed{r_+=\min(\rho_p,c_p).}
\tag{5.2}
\]

所以 second-node strict cancellation只有在

\[
\boxed{\rho_p=c_p}
\tag{5.3}
\]
时才可能发生。

---

## 6. four old minimum ties collapse to two serial mechanisms

现在重新审计此前的四类 strict-extra frontier。

### 6.1 `r_B=h<rho_p`

假设

\[
r_+>h.
\]

若 `c_p=h`，则 `rho_p>c_p`，由 (5.2) 必有

\[
r_+=c_p=h,
\]
矛盾。因此

\[
\boxed{
r_B=h<\rho_p,\quad r_+>h
\Longrightarrow
c_p>h.}
\tag{6.1}
\]

所以这类 strict-extra 完全由**第一节点**的额外 cancellation产生：

\[
F_{\rm dec}B_{\rm dec}
\equiv TQK^2\beta^2
\pmod{p^{2h+1}}.
\]

特别地

\[
\boxed{p^{2h+1}\mid C_{BE}.}
\tag{6.2}
\]

### 6.2 `r_B=\rho_p<h`

由 `r_B<h`，(4.3) 给

\[
c_p=r_B=\rho_p.
\]

所以 strict-extra `r_+>r_B` 精确进入第二节点 tie：

\[
\boxed{c_p=\rho_p=r_B.}
\tag{6.3}
\]

### 6.3 `h=\rho_p<r_B`

由 `r_B>h`，(4.3) 给

\[
c_p=h=\rho_p.
\]

因此 strict-extra 同样只能来自第二节点：

\[
\boxed{c_p=\rho_p=h.}
\tag{6.4}
\]

### 6.4 triple tie `r_B=h=\rho_p`

第一节点只给

\[
c_p\ge h.
\]

若 `c_p>h`，则

\[
\rho_p=h<c_p,
\]
由 (5.2) 反而强迫

\[
r_+=h.
\]

所以若 triple tie 还要求 strict-extra

\[
r_+>h,
\]
就必须有

\[
\boxed{c_p=h.}
\tag{6.5}
\]

并且第二节点恰发生 tie：

\[
\boxed{c_p=\rho_p=h.}
\tag{6.6}
\]

这是重要的互斥：triple tie 中 `C_BE` 不能同时 extra；第一节点若继续深化，第二节点反而失去 tie，`E_+` 被锁回最低深度。

---

## 7. serial cancellation picture

四类旧 frontier因此被压成：

\[
\boxed{
\begin{array}{c|c}
\text{old tie}&\text{actual strict-extra mechanism}\\ \hline
r_B=h<\rho_p&\text{first node: }c_p>h\\
r_B=\rho_p<h&\text{second node: }c_p=\rho_p\\
h=\rho_p<r_B&\text{second node: }c_p=\rho_p\\
r_B=h=\rho_p&\text{second node: }c_p=\rho_p=h
\end{array}}
\tag{7.1}
\]

所以只有两个真正 remaining higher-cancellation problems：

1. first-node extra
   \[
   r_B=h<\rho_p,\qquad c_p>h;
   \]
2. second-node extra
   \[
   c_p=\rho_p,\qquad r_+>\rho_p.
   \]

后续无需继续分别维护三种 pair tie和 triple tie。

---

## 8. current frontier

`C_BE` 给出了一个新的 canonical short reader：

\[
\boxed{
C_{BE}=F_{\rm dec}P-2K^2\beta,
\qquad
839TN^3<C_{BE}<843TN^3.}
\]

完整 depth pipeline 变成

\[
\boxed{
(r_B,h)
\longrightarrow c_p
\longrightarrow(\rho_p,c_p)
\longrightarrow r_+.}
\tag{8.1}
\]

因此 equal-depth deep resonance 的局部无界机制已从四个 minimum-tie cases压成两个串联二项 cancellation nodes。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-source-orientation"></a>

> 整合来源：`spontaneous-height-equal-depth-source-orientation.md`

# A2 moving height equal-depth 的 actual-carrier / source orientation law

> **依赖：** `spontaneous-height-angle-additive-norm-bridge.md`、`primitive-reduction.md`、`spontaneous-height-parity-ledger.md`、`source-discriminant.md`。
>
> **严格状态：**前一文件证明 moving height 的 unsaturated equal-depth extra lift 强迫 normalized `B_W/H_O` ratio为 `-square`。本文把 `H_O` 和 `B_W` 分别还原到实际 angle/additive primitive carriers，在 `p^h||W_q`、common depth `e<h` 上计算精确的一阶 resultant coefficient。利用 original sphere、`alpha=omega W_q`、`beta=omega S`、height square与 denominator ratio，最终把 equal-depth condition化成
> \[
> \left(\frac{(\Theta_{dec}/p^e)/(\mathcal O_+/p^e)}p\right)
> =\left(\frac{-\rho}p\right),
> \qquad \rho=q5^\lambda/c_u.
> \]
> 因而剩余 relative orientation 已直接接到真实 source ratio；不再含 `H_O`、`B_W` 或 auxiliary carrier。本文尚未从 sign-companion / source orbit独立固定左边或 `rho` 的 character，所以不关闭 equal-depth shell。

---

## 1. height prime 与原拼接 content

固定 genuine non-`3` inert endpoint-external height prime

\[
p^h\Vert W_q,
\qquad h\ge1,
\qquad p\equiv3\pmod4.
\tag{1.1}

允许 `p` 同时进入 `omega`；写

\[
w:=v_p(\omega)\ge0.
\]

primitive reduction 已给

\[
\boxed{
\alpha:=TK+a_3=\omega W_q,}
\tag{1.2}

\[
\boxed{
\beta:=TQ+b_3=\omega S,
\qquad \gcd(W_q,S)=1.}
\tag{1.3}

所以

\[
v_p(\alpha)=w+h,
\qquad
v_p(\beta)=w.
\tag{1.4}

原 exact sphere为

\[
\boxed{
B^2b_3^2\alpha^2
=\beta^2
\left(N_0b_3^2+B^2a_3^2\right).}
\tag{1.5}

external separation给 `p∤Bb_3S`，因此 (1.4)--(1.5) 精确推出

\[
\boxed{
v_p(N_0b_3^2+B^2a_3^2)=2h.}
\tag{1.6}

---

## 2. `alpha=0` height quadratic 在 mod `p^h` 内无损

定义 angle resultant使用的 quadratic

\[
\boxed{
\mathscr H_0
:=N_0b_3^2+B^2T^2K^2.}
\tag{2.1}

由 `a_3=alpha-TK`：

\[
\mathscr H_0-
(N_0b_3^2+B^2a_3^2)
=B^2(2\alpha TK-\alpha^2).
\tag{2.2}

右边至少有 `p^{h+w}`，而 (1.6) 有 `p^{2h}`。所以无条件有

\[
\boxed{p^h\mid\mathscr H_0.}
\tag{2.3}

这里不需要假设 `p∤omega`；即使 `omega` 带同 prime content，`p^h` height depth仍保留。

---

## 3. angle resultant 的一阶 coefficient

actual raw angle carrier为

\[
\boxed{
\mathcal O_+
=T\mathcal U_\Omega+2A^2Qb_3.}
\tag{3.1}

记

\[
L:=\mathcal O_+.
\]

由

\[
2A^2Qb_3=L-T\mathcal U_\Omega
\]
直接展开：

\[
\begin{aligned}
(2A^2Q)^2\mathscr H_0
={}&N_0(L-T\mathcal U_\Omega)^2
+4A^4Q^2B^2T^2K^2\\
={}&N_0L^2-2N_0T\mathcal U_\Omega L
+T^2\mathcal H_O.
\end{aligned}
\]
因此 exact identity为

\[
\boxed{
T^2\mathcal H_O
=(2A^2Q)^2\mathscr H_0
-N_0L^2
+2N_0T\mathcal U_\Omega L.}
\tag{3.2}

设 actual angle depth

\[
e:=v_p(L)<h.
\tag{3.3}

由 (2.3)，第一项比 `p^e` 更深；`L^2` 有深度 `2e>e`。故除以 `p^e` 并模 `p`：

\[
\boxed{
\frac{\mathcal H_O/p^e}{\mathcal O_+/p^e}
\equiv
\frac{2N_0\mathcal U_\Omega}{T}
\pmod p.}
\tag{3.4}

这是 height norm resultant 在 simple unsaturated root上的精确 derivative coefficient。

---

## 4. additive carrier 的一阶 coefficient

actual additive raw carrier为

\[
\boxed{
\Theta_{\rm dec}
=T\mathcal J_H
-2B^2(2K-9)\alpha.}
\tag{4.1}

若 common additive depth同样为 `e<h`，则第二项因 `v_p(alpha)>=h` 更深，所以

\[
\boxed{
\frac{\Theta_{\rm dec}}{p^e}
\equiv
T\frac{\mathcal J_H}{p^e}
\pmod p.}
\tag{4.2}

已有 height square bridge

\[
c_u^2\mathcal J_H
\equiv B^2\mathscr B_W
\pmod{W_q}.
\]
因此在 `e<h`：

\[
\boxed{
\frac{\Theta_{\rm dec}/p^e}{\mathscr B_W/p^e}
\equiv
T\left(\frac B{c_u}\right)^2
\pmod p.}
\tag{4.3}

angle 与 additive raw carriers都除以相同 primitive `2`-power
`2^{2M+m+2}`，所以它们的 normalized ratio与 primitive ratio完全相同。

---

## 5. `2 N_0 U_Omega` 的 character 精确等于 source `rho`

height square exact identity为

\[
\boxed{
b_3^2N_0+B^2a_3^2
=\left(\frac{BH_0}{g}\right)^2,}
\tag{5.1}

且 `H_0=c_uW_q`。模 `p|W_q`：

\[
\boxed{
N_0
\equiv-\left(\frac{Ba_3}{b_3}\right)^2
\pmod p.}
\tag{5.2}

所以

\[
\left(\frac{N_0}{p}\right)=-1.
\tag{5.3}

另一方面 actual angle first layer `O_+=0` 给

\[
T\mathcal U_\Omega
\equiv-2A^2Qb_3
\pmod p.
\]
因此

\[
2\mathcal U_\Omega
\equiv-\frac{4A^2Qb_3}{T}
\pmod p.
\tag{5.4}

source denominator ratio为

\[
\boxed{b_3z=Tc_uQ,}
\tag{5.5}

其中

\[
z=q5^\lambda,
\qquad
\rho:=\frac z{c_u}.
\tag{5.6}

由 (5.5)：

\[
\frac{Qb_3}{T}
=\frac{b_3^2z}{T^2c_u}.
\]
除显式 squares 后：

\[
\boxed{
\left(\frac{2\mathcal U_\Omega}{p}\right)
=\left(\frac{-\rho}{p}\right).}
\tag{5.7}

结合 (5.3)，因为 `p=3 mod4`：

\[
\boxed{
\left(\frac{2N_0\mathcal U_\Omega}{p}\right)
=\left(\frac{\rho}{p}\right).}
\tag{5.8}

`T` 只会在 (3.4) 中出现；稍后与 additive coefficient 的 `T` 精确相消，因此无需单独确定 `(T/p)`。

---

## 6. 把 `B_W/H_O` ratio换成 actual carrier ratio

由 (3.4) 与 (4.3)：

\[
\frac{\mathscr B_W/p^e}{\mathcal H_O/p^e}
\equiv
\frac{(\Theta_{\rm dec}/p^e)/(\mathcal O_+/p^e)}
{2N_0\mathcal U_\Omega}
\left(\frac{c_u}{B}\right)^2
\pmod p.
\tag{6.1}

这里两个 `T` 已经抵消。

所以 Legendre character为

\[
\boxed{
\left(
\frac{(\mathscr B_W/p^e)/(\mathcal H_O/p^e)}p
\right)
=
\left(
\frac{(\Theta_{\rm dec}/p^e)/(\mathcal O_+/p^e)}p
\right)
\left(\frac{\rho}{p}\right).}
\tag{6.2}

---

## 7. equal-depth extra lift的 source-orientation law

`spontaneous-height-angle-additive-norm-bridge.md` 已证明：若

\[
v_p(\mathscr B_W)=v_p(\mathcal H_O)=e<h
\]
且 auxiliary carrier `R_HO` 继续 extra lift，则

\[
\left(
\frac{(\mathscr B_W/p^e)/(\mathcal H_O/p^e)}p
\right)=-1.
\tag{7.1}

与 (6.2) 合并：

\[
\boxed{
\left(
\frac{(\Theta_{\rm dec}/p^e)/(\mathcal O_+/p^e)}p
\right)
=-\left(\frac{\rho}{p}\right).}
\tag{7.2}

因为 `(-1/p)=-1`，也可写成更对称的形式

\[
\boxed{
\left(
\frac{(\Theta_{\rm dec}/p^e)/(\mathcal O_+/p^e)}p
\right)
=
\left(\frac{-\rho}{p}\right).}
\tag{7.3}

这就是 moving-height equal-depth extra cancellation 的 actual-carrier / source orientation law。

---

## 8. updated frontier

现在 unsaturated moving height shell已经连续经历三次压缩：

1. singular bad-reduction tree 全部删除；
2. unequal-depth由 universal norm bridge精确同步；
3. equal-depth extra lift若发生，实际 angle/additive normalized ratio必须与 source ratio满足 (7.3)。

所以剩余问题不再需要 auxiliary `H_O/B_W` variables。规范目标是：

\[
\boxed{
\text{独立计算 actual sign pair / cross-sign sphere 对 }
(\Theta_{dec}/p^e)/(\mathcal O_+/p^e)
\text{ 的 character，}}
\]

或独立固定 `rho` 的 sign/quartic orientation。

若 sign-companion geometry给出的左侧 character与 `(7.3)` 相反，则整个 unsaturated equal-depth moving-height shell立即关闭。

---

<a id="source-spontaneous-height-equal-depth-square-core"></a>

> 整合来源：`spontaneous-height-equal-depth-square-core.md`

# A2 equal-depth oversaturation 的 concatenated square core

> **依赖：** `spontaneous-height-equal-depth-resonance.md`、`spontaneous-height-oversaturation-depth-ledger.md`、`primitive-reduction.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文把逐 prime 的 `e=v_p(omega)` / `h=v_p(W_q)` 二分提升为 `alpha=omega W_q` 的全局 square-core factorization。`Gamma=gcd(omega,W_q)` 的平方完整进入真实拼接 numerator，而 residual cofactor 的逐 prime 深度恰为 `|e-h|`；更进一步，`Gamma` 可完全恢复为原始整数的三重 gcd `gcd(alpha,beta,H_0)`，所以该 square core 无需 source 记号即可定义。对当前 endpoint，`alpha` 恰有 `m+M+1` 位，并且距顶部 `10TN` 只有一个显式小 defect `C_alpha=10Te_2-a_3`。所有 equal-depth oversaturation primes 的总平方块共同整除 `alpha`，从而受到单一 `sqrt(alpha)` 高度约束；若该平方模数超过 `C_alpha`，后者就是 `10TN` 模整个 equal-depth square core 的最小正代表。本文给出新的 global allocation / CRT 接口，不宣称 A2 closure。

---

## 1. `omega/W_q` 的 canonical square-core decomposition

沿用

\[
\boxed{\alpha=TK+a_3=\omega W_q.}
\tag{1.1}
\]

定义

\[
\boxed{\Gamma:=\gcd(\omega,W_q),}
\tag{1.2}
\]
以及

\[
\boxed{
\omega^\circ:=\frac\omega\Gamma,
\qquad
W^\circ:=\frac{W_q}{\Gamma}.}
\tag{1.3}
\]

由 gcd 定义：

\[
\boxed{\gcd(\omega^\circ,W^\circ)=1.}
\tag{1.4}
\]

因此

\[
\boxed{
\alpha
=\Gamma^2\omega^\circ W^\circ.}
\tag{1.5}
\]

这给出了 `alpha` 的 canonical common-square / imbalance factorization。

`primitive-reduction.md` 已经证明

\[
\omega=\gcd(\alpha,\beta),
\qquad
W_q=\gcd(\alpha,H_0),
\tag{1.6}
\]
并且

\[
\beta=\omega S,
\qquad
H_0=c_uW_q,
\qquad
\gcd(W_q,S)=1,
\qquad
\gcd(\omega,c_u)=1.
\tag{1.7}
\]

因此 `Gamma` 还有一个完全 original-integer 的读取器：

\[
\boxed{
\Gamma
=\gcd(\omega,W_q)
=\gcd(\alpha,\beta,H_0).}
\tag{1.8}
\]

逐 prime 验证很直接。若

\[
e=v_p(\omega),\quad
h=v_p(W_q),\quad
s=v_p(S),\quad
c=v_p(c_u),
\]
则 (1.7) 给

\[
\min(h,s)=0,
\qquad
\min(e,c)=0.
\]
而三原始整数的赋值分别为

\[
e+h,\qquad e+s,\qquad c+h.
\]
所以

\[
\min(e+h,e+s,c+h)=\min(e,h),
\]
恰好就是 `v_p(Gamma)`。

因此本文的 common square core 不依赖后续 source quotient 的选取：它就是**原拼接 numerator、原拼接 denominator 与整数 sphere height 的三重公共部分**。

逐 prime 写

\[
e_p:=v_p(\omega),
\qquad
h_p:=v_p(W_q).
\]
则

\[
v_p(\Gamma)=\min(e_p,h_p),
\]
而

\[
\boxed{
v_p(\omega^\circ W^\circ)
=|e_p-h_p|.}
\tag{1.9}
\]

所以：

\[
\boxed{
e_p=h_p
\Longleftrightarrow
p\mid\Gamma\ \text{且}\ p\nmid\omega^\circ W^\circ}
\tag{1.10}
\]
（这里默认 `e_p=h_p>=1`）。

换句话说，前两轮逐 prime 发现的 equal-depth / unequal-depth dichotomy 已经有一个完全 canonical 的全局含义：

- equal-depth common prime 完全被吸收到 `Gamma^2`；
- unequal-depth common prime 在抽掉共同平方后仍留下 `|e_p-h_p|` 层，并且因为 (1.4) 只能留在 `omega^circ` 或 `W^circ` 的一边。

---

## 2. equal-depth oversaturation primes 的总平方块

令 `E_eq` 为当前 height companion oversaturation 中满足

\[
p\equiv7,11\pmod{24},
\qquad
v_p(\omega)=v_p(W_q)=h_p\ge1
\]
的 distinct primes 集合。

定义

\[
\boxed{
G_{\rm eq}:=\prod_{p\in E_{\rm eq}}p^{h_p}.}
\tag{2.1}
\]

由 (1.5)、(1.10)：

\[
\boxed{G_{\rm eq}\mid\Gamma,}
\tag{2.2}
\]

且更重要地

\[
\boxed{G_{\rm eq}^2\mid\alpha.}
\tag{2.3}
\]

同时每个 `p in E_eq` 在

\[
\alpha/G_{\rm eq}^2
\]
中已没有剩余 p-factor。因此 equal-depth oversaturation 的整个指定 prime pool 在真实 numerator 中表现为一个**完整平方块**，不再只是若干互不关联的局部条件。

---

## 3. 真实拼接 numerator `alpha` 恰有 `m+M+1` 位

当前 endpoint defect parametrization 为

\[
\boxed{
a_2=10^{M-1}-e_2,}
\qquad
0<e_2<\frac{10^{M-1}}{250},
\tag{3.1}
\]

以及

\[
\boxed{
a_3=T+h_3,}
\qquad
0<h_3<\frac{T}{250},
\qquad T=10^m.
\tag{3.2}
\]

令

\[
N=10^M.
\]
则

\[
K=9N+10a_2
=10N-10e_2.
\tag{3.3}
\]

由 `e_2<N/2500`：

\[
\boxed{
\frac{2499}{250}N<K<10N.}
\tag{3.4}
\]

因此

\[
\alpha=TK+a_3
>\frac{2499}{250}TN.
\tag{3.5}
\]

另一方面 `e_2>=1`，而

\[
a_3<\frac{251}{250}T.
\]
所以

\[
\begin{aligned}
\alpha
&=10TN-10Te_2+a_3\\
&<10TN-10T+\frac{251}{250}T\\
&=10TN-\frac{2249}{250}T
<10TN.
\end{aligned}
\tag{3.6}
\]

于是

\[
\boxed{
\frac{2499}{250}\,10^{m+M}
<\alpha
<10^{m+M+1}.}
\tag{3.7}
\]

特别地

\[
\boxed{
\alpha
\text{ 恰有 }m+M+1\text{ 个十进制数字}.}
\tag{3.8}
\]

---

## 4. 单个 equal-depth prime 的 square-depth 高度界

若

\[
v_p(\omega)=v_p(W_q)=h,
\]
则由 `alpha=omega W_q`：

\[
\boxed{v_p(\alpha)=2h.}
\tag{4.1}
\]

所以

\[
\boxed{p^{2h}\Vert\alpha.}
\tag{4.2}
\]

结合 (3.7)：

\[
\boxed{p^{2h}<10^{m+M+1}.}
\tag{4.3}
\]

这比 `E_+` 的 `m+3M+4` 位 bound 更短；`E_+` 的额外价值在于读取 resonance tail `rho_p`，而 `alpha` 则是 equal-depth **基础平方深度 `2h`** 的最短自然代表。

---

## 5. 所有 equal-depth oversaturation primes 的 global product bound

由 (2.3)、(3.7)：

\[
G_{\rm eq}^2\le\alpha<10TN.
\]
所以

\[
\boxed{
G_{\rm eq}
<\sqrt{10TN}
=10^{(m+M+1)/2}.}
\tag{5.1}
\]

等价地

\[
\boxed{
\sum_{p\in E_{\rm eq}}h_p\log p
<\frac12(m+M+1)\log10.}
\tag{5.2}
\]

这是一条真正的 global allocation inequality：所有 equal-depth oversaturation primes 不再能各自独立消耗高度，它们必须共同装进同一个 `alpha` square core。

---

## 6. 顶部 complement 是一个远小于 `alpha` 的真实 endpoint defect

定义

\[
\boxed{
C_\alpha:=10TN-\alpha.}
\tag{6.1}
\]

由 (3.3)：

\[
\boxed{
C_\alpha=10Te_2-a_3.}
\tag{6.2}
\]

由于 `e_2>=1`、`a_3<251T/250`：

\[
\boxed{
C_\alpha>\frac{2249}{250}T.}
\tag{6.3}
\]

另一方面 `e_2<N/2500` 且 `a_3>T>0`：

\[
C_\alpha
<\frac{TN}{250}-T
<\frac{TN}{250}.
\]
所以

\[
\boxed{
\frac{2249}{250}T
<C_\alpha
<\frac1{250}TN.}
\tag{6.4}
\]

因此 `alpha` 位于十进制顶部 `10TN` 下方一个相对小于 `1/2500` 的显式整数 defect 内。

---

## 7. equal-depth square core 的 CRT natural representative

由 (2.3)：

\[
\alpha\equiv0\pmod{G_{\rm eq}^2}.
\]
结合 (6.1)：

\[
\boxed{
10TN\equiv C_\alpha
\pmod{G_{\rm eq}^2}.}
\tag{7.1}
\]

所有 `p in E_eq` 都是 genuine non-`3` inert prime，因此

\[
\gcd(G_{\rm eq},10TN)=1.
\]
从 (7.1) 也有

\[
\boxed{
\gcd(G_{\rm eq},C_\alpha)=1.}
\tag{7.2}
\]

若进一步进入规模区间

\[
\boxed{G_{\rm eq}^2>C_\alpha,}
\tag{7.3}
\]
那么 (7.1)、`0<C_alpha<G_eq^2` 立即说明：

\[
\boxed{
C_\alpha
=10TN\bmod G_{\rm eq}^2
}
\tag{7.4}
\]
是最小正代表。

所以 large equal-depth square core 不再只是抽象因子乘积；它会把真实 endpoint defect `10Te_2-a_3` 直接固定成一个 CRT representative。

---

## 8. 当前 square-core frontier

现在 `omega/W_q` overlap 可统一看成

\[
\boxed{
\alpha
=\Gamma^2\omega^\circ W^\circ,
\qquad
\Gamma=\gcd(\alpha,\beta,H_0),
\qquad
\gcd(\omega^\circ,W^\circ)=1,}
\tag{8.1}
\]

其中

\[
v_p(\omega^\circ W^\circ)=|e_p-h_p|.
\]

因此：

- unequal-depth sector 已由 residual-depth ledger 控制，并显式留在 imbalance cofactor；
- equal-depth sector 完全进入由原始整数三重 gcd 读取的 square core；
- equal-depth oversaturation pool 的总尺度满足 (5.1)；
- 当该 pool 足够大时，顶部小 defect `C_alpha` 成为其平方模数的 exact natural residue。

下一步若要继续压缩 equal-depth pool，最有希望的接口是把 (7.1) 与 `E_+/E_-` 的 near-equal decimal pair 或 determinant `Delta_omega=E_MN omega` 联立，从而让同一个 `G_eq` 同时控制两个独立的真实 decimal residues。

---

<a id="source-spontaneous-height-equal-depth-tail-gcd-ladder"></a>

> 整合来源：`spontaneous-height-equal-depth-tail-gcd-ladder.md`

# A2 equal-depth resonance 的 canonical gcd ladder

> **依赖：** `spontaneous-height-equal-depth-tail-imbalance.md`、`spontaneous-height-equal-depth-tail-source-separation.md`、`primitive-reduction.md`。
>
> **严格状态：**本文研究上一层留下的 `gcd(Gamma,Lambda_tail)`。在当前 genuine non-`3` denominator-separated height sector，tail equation `Lambda_tail=A omega^circ+B W^circ` 的两个固定 coefficient `A=2E_MNS`、`B=TQ^2` 都是 p-adic units。由此证明：若 `e=v_p(omega)` 与 `h=v_p(W_q)` 不相等，则抽掉共同 `Gamma` 后恰有一个 imbalance factor仍含 `p`，另一个为 unit，故 `p` 不可能整除 `Lambda_tail`；若 `e=h`，则 `v_p(Lambda_tail)=rho_p`。因此 `gcd(Gamma,Lambda_tail)` 在 genuine sector 精确选择 equal-depth 且 `rho_p>0` 的 resonant common primes。进一步定义 `D_k=gcd(Gamma^k,Lambda_tail)`，其 p-depth 恰为 `min(kh,rho_p)`，从而形成一个不需要事先枚举 target primes 的 canonical resonance-depth ladder。本文仍不证明该 ladder 为空，因此不关闭 A2。

---

## 1. 记号与 genuine coefficient separation

令

\[
e:=v_p(\omega),
\qquad
h:=v_p(W_q),
\qquad
\gamma:=\min(e,h).
\tag{1.1}
\]

沿用

\[
\Gamma=\gcd(\omega,W_q),
\]
所以

\[
v_p(\Gamma)=\gamma.
\tag{1.2}
\]

以及

\[
\omega^\circ=\omega/\Gamma,
\qquad
W^\circ=W_q/\Gamma.
\]
故

\[
\boxed{
v_p(\omega^\circ)=e-\gamma,
\qquad
v_p(W^\circ)=h-\gamma.}
\tag{1.3}
\]

本文只讨论当前 oversaturation 分析中已经分离出的 genuine non-`3` height sector；这里

\[
\boxed{p\nmid2E_MNSTQ.}
\tag{1.4}
\]

特别地，tail equation

\[
\boxed{
\Lambda_{\rm tail}
=A\omega^\circ+B W^\circ,
\qquad
A:=2E_MNS,
\quad
B:=TQ^2}
\tag{1.5}
\]

中的 `A,B` 都是 p-units。

---

## 2. unequal-depth common prime 不可能进入 tail

先设

\[
e>h.
\]

则 `gamma=h`，由 (1.3)：

\[
v_p(\omega^\circ)=e-h>0,
\qquad
v_p(W^\circ)=0.
\]

由 (1.4)、(1.5)：

\[
\Lambda_{\rm tail}
\equiv BW^\circ\not\equiv0\pmod p.
\]
所以

\[
\boxed{e>h\Longrightarrow v_p(\Lambda_{\rm tail})=0.}
\tag{2.1}
\]

同理若

\[
h>e,
\]
则 `omega^circ` 为 unit、`W^circ` 被 p 整除，因此

\[
\Lambda_{\rm tail}
\equiv A\omega^\circ\not\equiv0\pmod p,
\]
即

\[
\boxed{h>e\Longrightarrow v_p(\Lambda_{\rm tail})=0.}
\tag{2.2}
\]

合并：

\[
\boxed{
e\ne h
\Longrightarrow
v_p(\Lambda_{\rm tail})=0.}
\tag{2.3}
\]

这是一个比旧 residual-depth cap 更直接的 global quotient statement：所有 unequal-depth common primes 在 canonical tail quotient 中完全消失。

---

## 3. equal-depth prime 的 tail depth 恰为 `rho_p`

若

\[
e=h\ge1,
\]
则

\[
\gamma=h,
\qquad
p\nmid\omega^\circ W^\circ.
\]

`spontaneous-height-equal-depth-tail-normalization.md` 已证明

\[
\boxed{
v_p(\Lambda_{\rm tail})=\rho_p.}
\tag{3.1}
\]

所以在 genuine common-prime sector：

\[
\boxed{
 v_p(\Lambda_{\rm tail})
 =
 \begin{cases}
 0,&e\ne h,\\[1mm]
 \rho_p,&e=h.
 \end{cases}}
\tag{3.2}
\]

这已经把 equal/unequal depth dichotomy 内置进一个单一 canonical integer。

---

## 4. `gcd(Gamma,Lambda_tail)` 是 first resonance selector

定义

\[
\boxed{
D_{\rm res}:=\gcd(\Gamma,\Lambda_{\rm tail}).}
\tag{4.1}
\]

若 `e!=h`，由 (2.3)：

\[
v_p(D_{\rm res})=0.
\]

若 `e=h>=1`，由 (1.2)、(3.1)：

\[
v_p(D_{\rm res})
=\min(h,\rho_p).
\]

所以

\[
\boxed{
 v_p(D_{\rm res})
 =
 \begin{cases}
 0,&e\ne h,\\[1mm]
 \min(h,\rho_p),&e=h.
 \end{cases}}
\tag{4.2}
\]

特别地：

\[
\boxed{
p\mid D_{\rm res}
\Longleftrightarrow
e=h\ge1
\text{ 且 }\rho_p>0}
\tag{4.3}
\]

对当前 genuine sector成立。

因此 `D_res` 无需预先知道哪些 common primes 是 equal-depth，也无需逐 prime 计算 `omega_0,W_0`；一个普通整数 gcd 就能选择 first resonant support。

---

## 5. `Gamma^k` gcd ladder 读取更深 tail

对整数

\[
k\ge1
\]
定义

\[
\boxed{
D_k:=\gcd(\Gamma^k,\Lambda_{\rm tail}).}
\tag{5.1}
\]

若 `e!=h`，仍由 (2.3)：

\[
v_p(D_k)=0.
\]

若 `e=h`，则

\[
v_p(\Gamma^k)=kh,
\qquad
v_p(\Lambda_{\rm tail})=\rho_p.
\]
所以

\[
\boxed{
 v_p(D_k)
 =
 \begin{cases}
 0,&e\ne h,\\[1mm]
 \min(kh,\rho_p),&e=h.
 \end{cases}}
\tag{5.2}
\]

因此对 fixed equal-depth prime，随着 `k` 增长：

\[
\min(h,\rho_p),
\min(2h,\rho_p),
\min(3h,\rho_p),\ldots
\]

逐层恢复完整 `rho_p`。

---

## 6. ladder 的 successive quotient

令

\[
\boxed{
E_k:=D_{k+1}/D_k.}
\tag{6.1}
\]

因为 `D_k|D_{k+1}`，这是整数。

对 equal-depth prime：

\[
\begin{aligned}
v_p(E_k)
&=\min((k+1)h,\rho_p)-\min(kh,\rho_p).
\end{aligned}
\tag{6.2}
\]

所以：

- 若 `rho_p<=kh`，则 `v_p(E_k)=0`；
- 若 `kh<rho_p<(k+1)h`，则 `v_p(E_k)=rho_p-kh`；
- 若 `rho_p>=(k+1)h`，则 `v_p(E_k)=h`。

因此 `E_k` 正好记录 resonance tail 穿过第 `k` 个 baseline-height block 时的新深度。

---

## 7. stable gcd 等于 `Gamma`-supported full tail

因为 `Lambda_tail` 是固定正整数，存在有限 `k_0` 使得

\[
\Gamma^{k_0}
\]

在每个 `p|Gamma` 上的 exponent 都不小于 `v_p(Lambda_tail)`。
于是

\[
D_k=D_{k_0}
\qquad(k\ge k_0).
\]

稳定值

\[
\boxed{
D_\infty:=D_{k_0}}
\tag{7.1}
\]

就是 `Lambda_tail` 的 `Gamma`-primary part。

在当前 genuine sector，它的 non-`3` prime valuations 精确为：

\[
\boxed{
 v_p(D_\infty)
 =
 \begin{cases}
 0,&e\ne h,\\[1mm]
 \rho_p,&e=h.
 \end{cases}}
\tag{7.2}
\]

所以 full equal-depth resonance tail 已经可以通过普通整数 gcd ladder 恢复，不需要显式 factorization 才能定义。

---

## 8. 与 oversaturation target 的关系

本文的 `D_res,D_k,D_infty` 选择的是所有 genuine equal-depth resonant common primes；height companion oversaturation target 还额外满足 parent 文件的 `B_W/J_H` 条件，例如

\[
\mathcal P_{\omega H}(K)
=6K^2-36K+55
\equiv0\pmod p.
\]

因此本文没有把“resonant common prime”与“oversaturation target”混为一谈。

真正 target pool 可在 gcd ladder 基础上再与 fixed quadratic / companion carriers 取交；但 unequal-depth common primes 已经由 (2.3) 自动从 ladder 中消失。

---

## 9. 当前 frontier

现在 equal-depth analysis 有一个无需 prime list 的 canonical pipeline：

\[
\boxed{
\begin{aligned}
\omega&=\gcd(\alpha,\beta),\\
\Gamma&=\frac{\gcd(\alpha,\Lambda_{\rm dec})}{\gcd(\alpha,\beta)},\\
\Lambda_{\rm tail}
&=\frac{\Lambda_{\rm dec}}{\gcd(\alpha,\Lambda_{\rm dec})},\\
D_k&=\gcd(\Gamma^k,\Lambda_{\rm tail}).
\end{aligned}}
\tag{9.1}
\]

其中 genuine non-`3` common primes 的 unequal-depth sector完全不进入 `D_k`；equal-depth resonance 则由 ladder 精确读取。

所以接下来真正需要攻击的对象已经从 moving p-adic unit ratio 压成整数序列

\[
\boxed{D_1,D_2,\ldots,D_\infty.}
\tag{9.2}
\]

下一步应把该 ladder 与 `P_omegaH(K)` 的 target selector、`C_alpha` 的小 residue，或 `J_H/H_pref` 的 `4M+1` 位 carriers 联立，尝试证明 target part of `D_infty` 为空或高度不足。

---

<a id="source-spontaneous-height-equal-depth-tail-imbalance"></a>

> 整合来源：`spontaneous-height-equal-depth-tail-imbalance.md`

# A2 resonance tail 的 coprime imbalance equation

> **依赖：** `spontaneous-height-equal-depth-tail-normalization.md`、`spontaneous-height-equal-depth-square-core.md`、`primitive-reduction.md`。
>
> **严格状态：**前一文件定义 canonical tail quotient `Lambda_tail=Lambda_dec/(omega Gamma)`，并证明 equal-depth target prime 上 `v_p(Lambda_tail)=rho_p`。本文把 `omega=Gamma omega^circ`、`W_q=Gamma W^circ` 代入，得到 exact reduced equation `Lambda_tail=2E_MNS omega^circ+TQ^2W^circ`，其中 `gcd(omega^circ,W^circ)=1`。利用 `gcd(W_q,2E_MNS)=1` 进一步证明全局 coprimality `gcd(Lambda_tail,W^circ)=1`。因此 reduced height numerator 的 residual prime support 与 resonance tail support 完全分离；equal-depth tail 只能通过两个 p-adic units 的线性 cancellation 产生。本文仍不能排除这种 cancellation，因此不关闭 A2。

---

## 1. square-core imbalance factors

沿用

\[
\Gamma:=\gcd(\omega,W_q),
\]
并定义

\[
\boxed{
\omega^\circ:=\frac\omega\Gamma,
\qquad
W^\circ:=\frac{W_q}{\Gamma}.}
\tag{1.1}
\]

于是

\[
\boxed{
\gcd(\omega^\circ,W^\circ)=1,}
\tag{1.2}
\]

以及

\[
\alpha
=\Gamma^2\omega^\circ W^\circ.
\tag{1.3}
\]

逐 prime 有

\[
v_p(\omega^\circ W^\circ)
=|v_p(\omega)-v_p(W_q)|.
\tag{1.4}
\]

因此 equal-depth target prime 不整除 `omega^circ W^circ`。

---

## 2. full-tail reader 除去 baseline gcd 后变成两项线性式

已有

\[
\Lambda_{\rm dec}
=2\beta\Delta_\omega+TQ^2\alpha,
\tag{2.1}
\]

以及

\[
\beta=\omega S,
\qquad
\Delta_\omega=E_MN\omega,
\qquad
\alpha=\omega W_q.
\tag{2.2}
\]

所以

\[
\begin{aligned}
\Lambda_{\rm dec}
&=2(\omega S)(E_MN\omega)
+TQ^2(\omega W_q)\\
&=\omega\left(
2E_MNS\omega+TQ^2W_q
\right).
\end{aligned}
\tag{2.3}
\]

前一文件证明

\[
\gcd(\alpha,\Lambda_{\rm dec})
=\omega\Gamma,
\]
所以

\[
\Lambda_{\rm tail}
:=\frac{\Lambda_{\rm dec}}{\omega\Gamma}.
\]

把

\[
\omega=\Gamma\omega^\circ,
\qquad
W_q=\Gamma W^\circ
\]
代入 (2.3)，得到 exact reduced equation：

\[
\boxed{
\Lambda_{\rm tail}
=2E_MNS\omega^\circ
+TQ^2W^\circ.}
\tag{2.4}
\]

它的两项都是正整数，因此

\[
\Lambda_{\rm tail}>0.
\]

---

## 3. equal-depth tail 是两个 global units 的纯 cancellation

固定 equal-depth target prime `p`。由定义：

\[
p\nmid\omega^\circ W^\circ.
\tag{3.1}
\]

并且 genuine height prime 与 `2E_MNSTQ` 分离，所以 (2.4) 的两个 summand 都是 p-adic units：

\[
v_p(2E_MNS\omega^\circ)=0,
\qquad
v_p(TQ^2W^\circ)=0.
\tag{3.2}
\]

另一方面前一文件给

\[
\boxed{v_p(\Lambda_{\rm tail})=\rho_p.}
\tag{3.3}
\]

所以

\[
\boxed{
\rho_p
=v_p\left(
2E_MNS\omega^\circ+TQ^2W^\circ
\right).}
\tag{3.4}
\]

这已经完全删除 baseline `h`：resonance tail 就是两个互素 global imbalance cofactors 的 unit cancellation depth。

---

## 4. tail quotient 与 residual height numerator 全局互素

`primitive-reduction.md` 与前一 normalization 已证明

\[
\boxed{
\gcd(W_q,2E_MNS)=1.}
\tag{4.1}
\]

因为 `W^circ|W_q`：

\[
\gcd(W^\circ,2E_MNS)=1.
\tag{4.2}
\]

现在对 (2.4) 模 `W^circ`：

\[
\Lambda_{\rm tail}
\equiv2E_MNS\omega^\circ
\pmod{W^\circ}.
\]

由 (1.2)、(4.2)，右侧与 `W^circ` 互素。因此

\[
\boxed{
\gcd(\Lambda_{\rm tail},W^\circ)=1.}
\tag{4.3}
\]

这是一个 global support separation，不只是对 equal-depth target pool 成立。

---

## 5. `W^circ` 也有纯 decimal gcd 读取器

前一 normalization 给

\[
\gcd(\alpha,\Lambda_{\rm dec})
=\omega\Gamma.
\]

而

\[
\alpha=\omega W_q.
\]

因此

\[
\boxed{
W^\circ
=\frac{W_q}{\Gamma}
=\frac{\alpha}{\gcd(\alpha,\Lambda_{\rm dec})}.}
\tag{5.1}
\]

所以 (4.3) 可完全改写为真实 decimal integers：

\[
\boxed{
\gcd\!\left(
\frac{\Lambda_{\rm dec}}{\gcd(\alpha,\Lambda_{\rm dec})},
\frac{\alpha}{\gcd(\alpha,\Lambda_{\rm dec})}
\right)=1.}
\tag{5.2}
\]

当然 (5.2) 也可视为 gcd 约去后的 tautological coprimality；真正的结构信息是 (2.4)：这两个 coprime quotients 恰好对应 resonance tail 与 reduced-height imbalance，而不是任意 gcd quotient。

---

## 6. `omega^circ` 的 pure-gcd recovery

已有

\[
\omega=\gcd(\alpha,\beta),
\qquad
\Gamma=
\frac{\gcd(\alpha,\Lambda_{\rm dec})}
{\gcd(\alpha,\beta)}.
\]

所以

\[
\boxed{
\omega^\circ
=\frac\omega\Gamma
=
\frac{\gcd(\alpha,\beta)^2}
{\gcd(\alpha,\Lambda_{\rm dec})}.}
\tag{6.1}
\]

于是 (2.4) 的两个 imbalance variables `omega^circ,W^circ` 都可以完全通过真实 decimal gcd data 恢复。

这说明 equal-depth tail 的剩余 unit equation不再依赖隐藏 source quotient：

\[
\boxed{
\Lambda_{\rm tail}
=2E_MNS\omega^\circ+TQ^2W^\circ,
\quad
\gcd(\omega^\circ,W^\circ)=1,}
\tag{6.2}
\]

其中所有量都有 canonical original-integer meaning。

---

## 7. 与 unequal-depth sector 的全局分离

由 (1.4)，若某 prime 满足

\[
v_p(\omega)\ne v_p(W_q),
\]
它会以深度

\[
|v_p(\omega)-v_p(W_q)|
\]
留在 `omega^circ W^circ`。

而 equal-depth target prime 满足

\[
p\nmid\omega^\circ W^\circ,
\]
其全部额外信息则进入 `Lambda_tail` 的 `rho_p`。

所以现在有真正的 canonical allocation：

\[
\boxed{
\begin{array}{c|c}
\text{sector}&\text{global carrier}\\ \hline
v_p(\omega)\ne v_p(W_q)&\omega^\circ W^\circ\\
v_p(\omega)=v_p(W_q)&\Gamma^2\\
\text{equal-depth extra resonance}&\Lambda_{\rm tail}
\end{array}}
\tag{7.1}
\]

并且 `Lambda_tail` 与 `W^circ` 已由 (4.3) 完全互素。

---

## 8. 当前 frontier

height/content overlap 已从最初的 moving source roots 压成三个 canonical integers：

\[
\boxed{
\Gamma,
\qquad
\omega^\circ W^\circ,
\qquad
\Lambda_{\rm tail}.}
\tag{8.1}
\]

其中：

- `Gamma^2` 承担 equal-depth baseline square core；
- `omega^circ W^circ` 承担所有 content/height imbalance；
- `Lambda_tail` 精确承担全部 extra resonance depth；
- `gcd(Lambda_tail,W^circ)=1` 已把 residual height support 与 tail support 全局分开。

下一步真正有机会关闭 equal-depth orbit 的方向是继续研究

\[
\gcd(\Lambda_{\rm tail},\Gamma),
\qquad
\gcd(\Lambda_{\rm tail},\omega^\circ),
\]

或把 reduced linear equation (2.4) 与 `C_alpha` 的小正 residue 联立。

---

<a id="source-spontaneous-height-equal-depth-tail-normalization"></a>

> 整合来源：`spontaneous-height-equal-depth-tail-normalization.md`

# A2 equal-depth resonance tail 的 canonical gcd normalization

> **依赖：** `spontaneous-height-equal-depth-tail-reader.md`、`spontaneous-height-equal-depth-square-core.md`、`primitive-reduction.md`。
>
> **严格状态：**`spontaneous-height-equal-depth-tail-reader.md` 已构造纯 decimal integer `Lambda_dec` 并证明 equal-depth target prime 上 `v_p(Lambda_dec)=2h+rho_p`。本文进一步证明 exact global gcd `gcd(alpha,Lambda_dec)=omega Gamma`，其中 `omega=gcd(alpha,beta)`、`Gamma=gcd(omega,W_q)`。因此 `Gamma` 可仅由真实 concatenated integers 恢复为 `gcd(alpha,Lambda_dec)/gcd(alpha,beta)`，无需 sphere height `H_0`；而 canonical quotient `Lambda_tail=Lambda_dec/gcd(alpha,Lambda_dec)` 在每个 equal-depth target prime 上的赋值恰为 `rho_p`。这把 baseline square depth 与 resonance tail 完全分层。本文不证明 tail quotient 没有 target prime，因此不关闭 A2。

---

## 1. 已有 primitive data

沿用

\[
\boxed{
\alpha=\omega W_q,
\qquad
\beta=\omega S,
\qquad
\gcd(W_q,S)=1.}
\tag{1.1}
\]

`primitive-reduction.md` 还证明

\[
\boxed{
W_q\text{ 为奇数},
\quad
5\nmid W_q,
\quad
\gcd(W_q,gc_Q)=1.}
\tag{1.2}
\]

令

\[
E_M=2^{M+1}c_Q,
\qquad
N=10^M,
\]
则 determinant 为

\[
\boxed{
\Delta_\omega=E_MN\omega.}
\tag{1.3}
\]

而 full-tail reader 是

\[
\boxed{
\Lambda_{\rm dec}
=2\beta\Delta_\omega+TQ^2\alpha.}
\tag{1.4}
\]

---

## 2. `W_q` 与 `2E_MNS` 完全互素

由

\[
E_M=2^{M+1}c_Q,
\qquad
N=2^M5^M,
\]
以及

\[
S=2^{M+m+1}gc_Q5^d,
\]
`2E_MNS` 的所有 prime support 都来自

\[
2,5,g,c_Q.
\]

结合 (1.2)：

\[
\boxed{
\gcd(W_q,2E_MNS)=1.}
\tag{2.1}
\]

这条全局 coprimality 是下面 exact gcd 的全部输入。

---

## 3. `gcd(alpha,Lambda_dec)` 精确等于 `omega Gamma`

由 (1.4) 模 `alpha`：

\[
\Lambda_{\rm dec}
\equiv2\beta\Delta_\omega
\pmod\alpha.
\]
因此

\[
\begin{aligned}
\gcd(\alpha,\Lambda_{\rm dec})
&=\gcd(\alpha,2\beta\Delta_\omega)\\
&=\gcd(\omega W_q,
2E_MNS\omega^2).
\end{aligned}
\tag{3.1}
\]

约出一份 `omega`：

\[
\gcd(\alpha,\Lambda_{\rm dec})
=\omega\,
\gcd(W_q,2E_MNS\omega).
\tag{3.2}
\]

由 (2.1)：

\[
\gcd(W_q,2E_MNS\omega)
=\gcd(W_q,\omega).
\]

定义

\[
\boxed{
\Gamma:=\gcd(\omega,W_q).}
\tag{3.3}
\]

于是得到 exact global identity

\[
\boxed{
\gcd(\alpha,\Lambda_{\rm dec})
=\omega\Gamma.}
\tag{3.4}
\]

这不是逐 target-prime 截断，而是所有 prime 同时成立的整数 gcd 等式。

---

## 4. square core 现在只靠 concatenated decimal integers 就能恢复

已有

\[
\boxed{\omega=\gcd(\alpha,\beta).}
\tag{4.1}
\]

把它代入 (3.4)：

\[
\boxed{
\Gamma
=
\frac{\gcd(\alpha,\Lambda_{\rm dec})}
{\gcd(\alpha,\beta)}.}
\tag{4.2}
\]

因此此前 square-core 文件的

\[
\Gamma=\gcd(\alpha,\beta,H_0)
\]
有了一个新的、完全不使用 sphere height 的读取器。

也就是说：

\[
\boxed{
\text{common square core }
\Gamma
\text{ 可由 }(\alpha,\beta,\Lambda_{\rm dec})
\text{ 三个真实 decimal integers 独立恢复}.}
\tag{4.3}
\]

这给后续纯 concatenation CRT 一个更干净的入口。

---

## 5. canonical tail quotient 精确删除 baseline depth

定义

\[
\boxed{
\Lambda_{\rm tail}
:=
\frac{\Lambda_{\rm dec}}
{\gcd(\alpha,\Lambda_{\rm dec})}
=
\frac{\Lambda_{\rm dec}}{\omega\Gamma}.}
\tag{5.1}
\]

固定 equal-depth target prime：

\[
v_p(\omega)=v_p(W_q)=h.
\]
因此

\[
\boxed{v_p(\Gamma)=h.}
\tag{5.2}
\]

full-tail reader 给

\[
\boxed{v_p(\Lambda_{\rm dec})=2h+\rho_p.}
\tag{5.3}
\]

所以从 (5.1)：

\[
\boxed{
v_p(\Lambda_{\rm tail})
=(2h+\rho_p)-h-h
=\rho_p.}
\tag{5.4}
\]

这是最干净的 tail normalization：

\[
\boxed{
\text{baseline }2h
\text{ 全部进入 }\gcd(\alpha,\Lambda_{\rm dec}),
\quad
\text{剩余赋值恰为 }\rho_p.}
\tag{5.5}
\]

因此 deep resonance `rho_p>=1` 等价于该 target prime 真正进入 `Lambda_tail`。

---

## 6. full tail product 直接整除 canonical quotient

令 `E_eq` 为 equal-depth oversaturation target pool，并定义

\[
\boxed{
R_\rho:=\prod_{p\in E_{\rm eq}}p^{\rho_p}.}
\tag{6.1}
\]

由 (5.4) 聚合：

\[
\boxed{
R_\rho\mid\Lambda_{\rm tail}.}
\tag{6.2}
\]

并且 target support 上是 exact：每个 `p in E_eq` 在 `Lambda_tail` 中恰出现 `rho_p` 次。

由 tail-reader 的 fixed window

\[
\Lambda_{\rm dec}<45T^2N^3
\]
有

\[
\boxed{
R_\rho
\le\Lambda_{\rm tail}
<
\frac{45T^2N^3}{\omega\Gamma}.}
\tag{6.3}
\]

相比原来的

\[
G_{\rm eq}^2R_\rho<45T^2N^3,
\]
(6.3) 的优点是 denominator `omega Gamma` 是一个 exact global gcd，而不是手工挑出的 target-prime product。

---

## 7. square/imbalance/tail 三层 canonical factorization

此前 square-core 文件给

\[
\alpha
=\Gamma^2\omega^\circ W^\circ,
\qquad
\gcd(\omega^\circ,W^\circ)=1.
\tag{7.1}
\]

本文则给

\[
\Lambda_{\rm dec}
=\omega\Gamma\Lambda_{\rm tail}.
\tag{7.2}
\]

所以 `alpha/Lambda_dec` 两个真实整数现在具有平行的 canonical decomposition：

\[
\boxed{
\begin{array}{c|c}
\alpha&\Gamma^2\cdot(\omega^\circ W^\circ)\\
\Lambda_{\rm dec}&\omega\Gamma\cdot\Lambda_{\rm tail}
\end{array}}
\tag{7.3}
\]

逐 equal-depth target prime：

- `Gamma^2` 读取 baseline `2h`；
- `omega^circ W^circ` 完全删除该 prime；
- `omega Gamma` 读取 `Lambda_dec` 中 baseline `2h`；
- `Lambda_tail` 精确读取剩余 `rho_p`。

因此前几轮的逐 prime depth ledger 已被提升为真正的 global gcd factorization。

---

## 8. 当前 frontier

现在 equal-depth resonance 的两个核心量都已 canonical 化：

\[
\boxed{
\Gamma
=
\frac{\gcd(\alpha,\Lambda_{\rm dec})}
{\gcd(\alpha,\beta)},
\qquad
\Lambda_{\rm tail}
=
\frac{\Lambda_{\rm dec}}
{\gcd(\alpha,\Lambda_{\rm dec})}.}
\tag{8.1}
\]

所以后续不再需要 source units `omega_0,W_0` 来描述剩余困难。

真正未关闭的对象已经压成：

\[
\boxed{
\text{一个短 square core }\Gamma^2\mid\alpha
\quad+\quad
\text{一个 pure decimal tail quotient }\Lambda_{\rm tail}.}
\tag{8.2}
\]

下一步最有价值的是研究 `Lambda_tail` 与 square-free imbalance cofactor `omega^circ W^circ`、顶部 defect `C_alpha` 或 prefix carriers 的 gcd。若能证明 target inert support 无法同时进入这些互补 natural quotients，就有机会真正关闭 equal-depth orbit。

---

<a id="source-spontaneous-height-equal-depth-tail-reader"></a>

> 整合来源：`spontaneous-height-equal-depth-tail-reader.md`

# A2 equal-depth resonance 的 full decimal tail reader

> **依赖：** `spontaneous-height-equal-depth-resonance.md`、`spontaneous-height-equal-depth-square-core.md`、`spontaneous-height-equal-depth-global-decimal-gcd.md`、`source-discriminant.md`、`primitive-reduction.md`。
>
> **严格状态：**前面的 decimal pair `E_+` 只能给 `v_p(E_+) >= 2h+min(r_B,h,rho_p)`，因此当 resonance tail `rho_p` 超过 `h` 或 `r_B` 时会被截断。本文构造新的纯 decimal 正整数 `Lambda_dec=2 beta Delta_omega+TQ^2 alpha`，并利用 source ratio 的 exact decimal realization 证明对每个 equal-depth oversaturation prime 都有精确公式 `v_p(Lambda_dec)=2h+rho_p`。因此整个 resonance tail `rho_p` 被完整读取，不再有 `h`-cap 或 companion-depth cap。`Lambda_dec` 恰有 `2m+3M+2` 位，并与 `TQ^2 alpha` 只相差一个 `<36 T^2N^2` 的正整数。所有 equal-depth primes 的 weighted tail 可聚合为单一 global divisibility `G_eq^2 R_rho | Lambda_dec`。本文仍不排除这些 weighted primes 的存在，因此不关闭 A2。

---

## 1. equal-depth setting

沿用 genuine non-`3` inert equal-depth oversaturation prime `p`：

\[
\boxed{
v_p(\omega)=v_p(W_q)=h\ge1.}
\tag{1.1}
\]

定义 resonance tail

\[
\boxed{
\rho_p:=v_p(2DgK\omega_0-fqW_0),}
\tag{1.2}
\]

其中

\[
\omega=p^h\omega_0,
\qquad
W_q=p^hW_0.
\]

`spontaneous-height-equal-depth-resonance.md` 已证明

\[
\boxed{
v_p(L_{JB})=h+\rho_p,}
\tag{1.3}
\]

其中

\[
L_{JB}=2N(g\omega)+z(qW_q).
\tag{1.4}
\]

本文的目标是把 (1.3) 完全乘回真实 decimal integers。

---

## 2. source ratio 有两个 exact decimal realizations

`source-discriminant.md` 已证明

\[
\boxed{b_3z=Tc_uQ.}
\tag{2.1}
\]

又因为

\[
g\omega=z+c_u,
\qquad
\beta=TQ+b_3,
\]
所以把 (2.1) 加上 `b_3c_u`：

\[
\boxed{
b_3(g\omega)=c_u\beta.}
\tag{2.2}
\]

因此两个 source linear pieces 都能通过真实 denominator concatenation 读取：

\[
\boxed{
\frac{z}{c_u}=\frac{TQ}{b_3},
\qquad
\frac{g\omega}{c_u}=\frac{\beta}{b_3}.}
\tag{2.3}
\]

这一步是下面 full-tail decimalization 的关键。

---

## 3. `L_JB` 乘回 decimal plane 后得到一个极简单的正整数

沿用

\[
E_M:=2^{M+1}c_Q,
\qquad
Q=E_Mq,
\]

\[
\alpha=\omega W_q,
\qquad
\Delta_\omega=E_MN\omega=Kb_3-Qa_3,
\]

\[
\beta=TQ+b_3.
\]

定义

\[
\boxed{
\Lambda_{\rm dec}
:=2\beta\Delta_\omega+TQ^2\alpha.}
\tag{3.1}
\]

它完全由真实 decimal quantities 组成，而且严格为正。

现在从 (1.4) 出发。第一项：

\[
\begin{aligned}
b_3E_M\omega\,2N(g\omega)
&=2N(E_M\omega)\,b_3(g\omega)\\
&=2N(E_M\omega)c_u\beta\\
&=2c_u\beta\Delta_\omega.
\end{aligned}
\tag{3.2}
\]

第二项使用 (2.1)：

\[
\begin{aligned}
b_3E_M\omega\,z(qW_q)
&=(b_3z)(E_Mq)(\omega W_q)\\
&=(Tc_uQ)Q\alpha\\
&=c_uTQ^2\alpha.
\end{aligned}
\tag{3.3}
\]

相加得到核心 exact identity：

\[
\boxed{
b_3E_M\omega L_{JB}
=c_u\Lambda_{\rm dec}.}
\tag{3.4}
\]

这里没有 rational normalization，也没有 residual source quotient。

---

## 4. `Lambda_dec` 精确读取全部 resonance tail

当前 genuine height prime 与

\[
2\cdot5\cdot b_3\cdot E_M\cdot c_u
\]
分离；特别地

\[
p\nmid b_3E_Mc_u.
\]

由 (1.1)、(1.3)、(3.4)：

\[
\begin{aligned}
v_p(\Lambda_{\rm dec})
&=v_p(\omega)+v_p(L_{JB})\\
&=h+(h+\rho_p).
\end{aligned}
\]

所以得到本文最重要的精确公式：

\[
\boxed{
v_p(\Lambda_{\rm dec})=2h+\rho_p.}
\tag{4.1}
\]

这与旧 `E_+` bound 的差别是本质性的：

\[
\boxed{
\rho_p\text{ 无论多深，都被 }\Lambda_{\rm dec}\text{ 完整读取。}}
\tag{4.2}
\]

没有 `min(h,...)`，也没有 `min(r_B,...)`。

---

## 5. `Lambda_dec` 与 baseline square carrier 形成 near-equal pair

由定义：

\[
\boxed{
\Lambda_{\rm dec}-TQ^2\alpha
=2\beta\Delta_\omega>0.}
\tag{5.1}
\]

对 equal-depth prime，已有

\[
v_p(\alpha)=2h,
\qquad
v_p(\beta)=h,
\qquad
v_p(\Delta_\omega)=h.
\]
且 `p\nmid TQ`。因此

\[
\boxed{
v_p(TQ^2\alpha)=2h,}
\tag{5.2}
\]

\[
\boxed{
v_p(2\beta\Delta_\omega)=2h.}
\tag{5.3}
\]

而 (4.1) 给

\[
\boxed{
v_p(\Lambda_{\rm dec})=2h+\rho_p.}
\tag{5.4}
\]

所以 full resonance tail 正是两个 baseline-depth `2h` 正整数相加后的额外 p-adic cancellation。

---

## 6. `Lambda_dec` 恰有 `2m+3M+2` 位

写 endpoint normalized variables

\[
x=\frac BN,
\qquad
Q/N=x+2,
\]

并沿用

\[
\frac1{10}<x<\frac2{19},
\qquad
N=10^M\ge10^{11}.
\]

square-core 文件给

\[
\frac{2499}{250}
<\frac{\alpha}{TN}<10.
\tag{6.1}
\]

而 decimal-pair 文件给

\[
0<\frac{\Delta_\omega}{TN}<\frac{843}{100},
\tag{6.2}
\]

以及

\[
\frac\beta{TN}
=\frac QN+\frac{b_3/T}{N}
<\frac{211}{100}.
\tag{6.3}
\]

于是

\[
\frac{\Lambda_{\rm dec}}{T^2N^3}
=
\left(\frac QN\right)^2
\frac{\alpha}{TN}
+
\frac2N
\frac\beta{TN}
\frac{\Delta_\omega}{TN}.
\tag{6.4}
\]

下界直接忽略第二个正项：

\[
\frac{\Lambda_{\rm dec}}{T^2N^3}
>
\left(\frac{21}{10}\right)^2
\frac{2499}{250}
=44.08236>44.
\tag{6.5}
\]

上界使用 (6.2)、(6.3)：

\[
\frac{\Lambda_{\rm dec}}{T^2N^3}
<
\left(\frac{40}{19}\right)^2 10
+
\frac2{10^{11}}\frac{211}{100}\frac{843}{100}
<45.
\tag{6.6}
\]

因此

\[
\boxed{
44T^2N^3
<\Lambda_{\rm dec}
<45T^2N^3.}
\tag{6.7}
\]

因为 `T=10^m,N=10^M`：

\[
\boxed{
\Lambda_{\rm dec}
\text{ 恰有 }2m+3M+2\text{ 个十进制数字}.}
\tag{6.8}
\]

同时由 (5.1)、(6.2)、(6.3)：

\[
0<\Lambda_{\rm dec}-TQ^2\alpha
<36T^2N^2.
\tag{6.9}
\]

所以这两个约 `44T^2N^3` 规模的正整数，只在相对 `O(1/N)` 的尺度上分开。

---

## 7. 单个 prime 的 full-tail 高度界

由 (4.1)、(6.7)：

\[
\boxed{
p^{2h+\rho_p}
<45\cdot10^{2m+3M}.}
\tag{7.1}
\]

因此

\[
\boxed{
(2h+\rho_p)\log p
<\log45+(2m+3M)\log10.}
\tag{7.2}
\]

与旧 `p^{2h+1}|E_+` 相比，这条界读取的是**完整 rho_p**，不是只知道它至少为 `1`。

---

## 8. 所有 equal-depth primes 的 full weighted product

令 `E_eq` 为所有当前 equal-depth oversaturation primes，沿用

\[
G_{\rm eq}:=\prod_{p\in E_{\rm eq}}p^{h_p}.
\]

再定义 resonance-tail product

\[
\boxed{
R_\rho
:=\prod_{p\in E_{\rm eq}}p^{\rho_p}.}
\tag{8.1}
\]

其中允许 `rho_p=0`。

由 (4.1) 逐 prime 聚合：

\[
\boxed{
G_{\rm eq}^2R_\rho
\mid\Lambda_{\rm dec}.}
\tag{8.2}
\]

更精确地，对 target prime pool：

\[
\boxed{
\gcd\!\left(
\frac{\Lambda_{\rm dec}}{G_{\rm eq}^2},
\operatorname{SuppMod}(E_{\rm eq})
\right)
\text{ 的 p-depth 恰为 }\rho_p,}
\tag{8.3}
\]

其中 (8.3) 只表示逐 target prime 的 exact valuation，不把 `SuppMod` 当作新的仓库记号。

由 (6.7)：

\[
\boxed{
G_{\rm eq}^2R_\rho
<45\cdot10^{2m+3M}.}
\tag{8.4}
\]

即

\[
\boxed{
\sum_{p\in E_{\rm eq}}
(2h_p+\rho_p)\log p
<\log45+(2m+3M)\log10.}
\tag{8.5}
\]

这严格强化了前一文件只对 `rho_p>=1` 支付一份 radical 的 budget：现在每一层 resonance tail 都要真实支付。

---

## 9. composite tail modulus 上的 exact decimal synchronization

由 (5.1)，并且 `G_eq^2|TQ^2 alpha` 与 `G_eq^2|2 beta Delta_omega`：

\[
\frac{\Lambda_{\rm dec}}{G_{\rm eq}^2}
=
\frac{TQ^2\alpha}{G_{\rm eq}^2}
+
\frac{2\beta\Delta_\omega}{G_{\rm eq}^2}.
\tag{9.1}
\]

对于任一 `rho_p>0` 的 target prime，两项右侧都是 p-units，而左侧含 `p^{rho_p}`。因此若令

\[
R_\rho^+:=\prod_{\rho_p>0}p^{\rho_p},
\]
则有 canonical composite congruence

\[
\boxed{
\frac{TQ^2\alpha}{G_{\rm eq}^2}
\equiv
-\frac{2\beta\Delta_\omega}{G_{\rm eq}^2}
\pmod{R_\rho^+}.}
\tag{9.2}
\]

这就是原 projective source-unit synchronization 的 full decimal version，而且 modulus 读取完整 `rho_p` prime powers。

---

## 10. 当前 frontier

此前 equal-depth branch 的主要缺口是：`rho_p` 一旦超过 `h` 或 companion residual depth，就没有 natural integer 能完整读取。

本文已经消掉这个缺口：

\[
\boxed{
\Lambda_{\rm dec}=2\beta\Delta_\omega+TQ^2\alpha,
\qquad
v_p(\Lambda_{\rm dec})=2h+\rho_p.}
\tag{10.1}
\]

因此真正剩余的问题不再是“如何读取 rho_p”，而是：

1. 如何把 `Lambda_dec` 的 full weighted product bound 与更短的 `alpha` square-core bound 联立；
2. 如何利用 near-equality
   \[
   0<\Lambda_{\rm dec}-TQ^2\alpha<36T^2N^2
   \]
   和两边巨大的共同 square core；
3. 或把 (9.2) 与顶部 defect residue `10TN=C_alpha (mod G_eq^2)` 联立，得到对 `R_rho` 的独立 Archimedean/CRT 限制。

ordinary quadratic character 与 first-layer simple-root 条件已经不再是主要缺口。

---

<a id="source-spontaneous-height-equal-depth-tail-source-separation"></a>

> 整合来源：`spontaneous-height-equal-depth-tail-source-separation.md`

# A2 resonance tail 与 imbalance support 的 source separation

> **依赖：** `spontaneous-height-equal-depth-tail-imbalance.md`、`source-discriminant.md`、`primitive-reduction.md`。
>
> **严格状态：**前一文件得到 `Lambda_tail=2E_MNS omega^circ+TQ^2W^circ` 与 `gcd(omega^circ,W^circ)=1`，并证明 `gcd(Lambda_tail,W^circ)=1`。本文进一步利用 source triangle `z=q5^lambda=g omega-c_u` 证明 `gcd(omega,q5)=1`，再结合 `alpha` 为奇数得到 `gcd(omega,2Tq)=1`。于是 `Lambda_tail` 与 `omega^circ` 的 overlap 精确等于 `gcd(c_Q^2,omega^circ)`，从而 `gcd(Lambda_tail,omega^circ W^circ)|c_Q^2`。因此除 `c_Q` support 外，resonance tail 与全部 content/height imbalance support 全局互素；当前 genuine height target primes 又与 `c_Q` 分离，所以 target tail 和 imbalance sector 已完全 prime-source 分开。本文不排除 tail primes 留在 square core `Gamma` 中，因此不关闭 A2。

---

## 1. `omega` 与 q-side source 完全互素

source triangle 为

\[
\boxed{
z=q5^\lambda=g\omega-c_u.}
\tag{1.1}
\]

并且已有

\[
\boxed{\gcd(\omega,c_u)=1.}
\tag{1.2}
\]

若某 prime `r` 同时整除 `omega` 与 `z`，则由 (1.1)

\[
c_u=g\omega-z
\]
也被 `r` 整除，与 (1.2) 矛盾。因此

\[
\boxed{\gcd(\omega,z)=1.}
\tag{1.3}
\]

因为

\[
z=q5^\lambda,
\qquad \lambda>0,
\]
所以

\[
\boxed{\gcd(\omega,q5)=1.}
\tag{1.4}
\]

---

## 2. `omega` 也是奇数

当前 denominator `b_3` 含非平凡 `2`-power，而

\[
\gcd(a_3,b_3)=1.
\]
所以 `a_3` 为奇数。

另一方面

\[
\alpha=TK+a_3,
\]
其中 `TK` 为偶数，因此

\[
\boxed{\alpha\text{ 为奇数}.}
\tag{2.1}
\]

又 `omega|alpha`，故

\[
\boxed{2\nmid\omega.}
\tag{2.2}
\]

结合 (1.4) 与 `T=2^m5^m`：

\[
\boxed{\gcd(\omega,Tq)=1.}
\tag{2.3}
\]

同样对 `omega^circ|omega`：

\[
\boxed{\gcd(\omega^\circ,Tq)=1.}
\tag{2.4}
\]

---

## 3. `TQ^2` 与 `omega^circ` 的 overlap 只来自 `c_Q`

由

\[
Q=2^{M+1}c_Qq,
\]
有

\[
TQ^2
=2^{m+2M+2}5^m c_Q^2q^2.
\]

使用 (2.4)：

\[
\boxed{
\gcd(TQ^2,\omega^\circ)
=\gcd(c_Q^2,\omega^\circ).}
\tag{3.1}
\]

因此任何 odd prime 同时进入 `TQ^2` 与 `omega^circ`，都必须来自 `c_Q` support。

---

## 4. tail 与 `omega^circ` 的 exact gcd

前一文件得到

\[
\boxed{
\Lambda_{\rm tail}
=2E_MNS\omega^\circ
+TQ^2W^\circ,}
\tag{4.1}
\]

以及

\[
\boxed{\gcd(\omega^\circ,W^\circ)=1.}
\tag{4.2}
\]

模 `omega^circ`：

\[
\Lambda_{\rm tail}
\equiv TQ^2W^\circ
\pmod{\omega^\circ}.
\]

由 (4.2)：

\[
\gcd(TQ^2W^\circ,\omega^\circ)
=\gcd(TQ^2,\omega^\circ).
\]

结合 (3.1)：

\[
\boxed{
\gcd(\Lambda_{\rm tail},\omega^\circ)
=\gcd(c_Q^2,\omega^\circ).}
\tag{4.3}
\]

这是 exact gcd identity，不只是 support inclusion。

---

## 5. tail 与整个 imbalance cofactor 的 overlap 只在 `c_Q`

前一文件已经证明

\[
\boxed{
\gcd(\Lambda_{\rm tail},W^\circ)=1.}
\tag{5.1}
\]

又

\[
\gcd(\omega^\circ,W^\circ)=1.
\]

所以

\[
\begin{aligned}
\gcd(
\Lambda_{\rm tail},
\omega^\circ W^\circ)
&=\gcd(\Lambda_{\rm tail},\omega^\circ)\\
&=\gcd(c_Q^2,\omega^\circ).
\end{aligned}
\]

即

\[
\boxed{
\gcd(
\Lambda_{\rm tail},
\omega^\circ W^\circ)
=\gcd(c_Q^2,\omega^\circ)
\mid c_Q^2.}
\tag{5.2}
\]

因此把 `c_Q` support 删除后：

\[
\boxed{
\operatorname{Supp}(\Lambda_{\rm tail})
\cap
\operatorname{Supp}(\omega^\circ W^\circ)
=\varnothing
\quad\text{outside }c_Q.}
\tag{5.3}
\]

---

## 6. 对 genuine equal-depth height target，separation 是完全的

`primitive-reduction.md` 已证明任何 genuine non-`3` height prime `p|W_q` 满足

\[
\boxed{p\nmid c_Q.}
\tag{6.1}
\]

因此对本文 equal-depth target prime：

\[
p\mid\Gamma,
\qquad
p\nmid\omega^\circ W^\circ c_Q.
\]

若 `rho_p>0`，则

\[
p\mid\Lambda_{\rm tail}.
\]

结合 (5.2)：该 prime 的 tail appearance 不可能来自 imbalance cofactor 的复用。

所以 canonical prime allocation 已变成：

\[
\boxed{
\begin{array}{c|c}
\text{mechanism}&\text{carrier}\ \hline
\text{unequal depth}&\omega^\circ W^\circ\\
\text{equal-depth baseline}&\Gamma^2\\
\text{equal-depth resonance tail}&\Lambda_{\rm tail}
\end{array}}
\tag{6.2}
\]

且最后一行与第一行对 genuine height primes 已完全 support-separated。

---

## 7. 当前剩余 overlap 被压到 `Gamma`

由 (5.2)，tail 与 imbalance sector 的 generic overlap 已经清空。

因此 equal-depth deep resonance 的 target primes若继续出现，只能来自它们本来就所在的 common square core：

\[
\boxed{
p\mid\Gamma
\quad\text{且}\quad
p^{\rho_p}\mid\Lambda_{\rm tail}.}
\tag{7.1}
\]

换句话说，真正尚未关闭的 gcd 已经压成单一对象

\[
\boxed{
\gcd(\Gamma,\Lambda_{\rm tail}).}
\tag{7.2}
\]

更高 `rho_p` 则对应该 gcd 在同一 prime 上的更深提升，直到超过 `v_p(\Gamma)` 后进入 higher tail powers。

下一步不再需要研究 `omega^circ W^circ` 与 tail 的 generic collision；应直接攻击 (7.2)，或把它与顶部小 defect `C_alpha` 的 square-modulus residue 联立。

---

<a id="source-spontaneous-height-equal-depth-target-ladder"></a>

> 整合来源：`spontaneous-height-equal-depth-target-ladder.md`

# A2 equal-depth resonance 的 target-prefix ladder 与 fixed `7` exception

> **依赖：** `spontaneous-height-equal-depth-tail-gcd-ladder.md`、`spontaneous-height-equal-depth-decimal-pair.md`、`spontaneous-height-equal-depth-tail-normalization.md`、`primitive-reduction.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文把上一层 canonical resonance ladder 再与真正的 omega-height target selector 联立。对每个 genuine non-`3` equal-depth oversaturation target，fixed quadratic `P_{omega H}(K)=6K^2-36K+55` 的 p-depth恰为 `h=v_p(W_q)=v_p(omega)`；而在当前 endpoint，它本身只是一个恰有 `2M+3` 位的 pure-prefix positive integer。因此所有 target baseline prime powers 的乘积统一装入同一个短 prefix carrier。再把 `P_{omega H}` 与 `qW_q=DK-N` 消去 `K`，得到 source-prefix resultant `R_PD=55D^2-36DN+6N^2`。若 target resonance 真正满足 `rho_p>=1`，则除固定素数 `7` 外有 `v_p(R_PD)=h` 精确等号；`R_PD` 可能比 baseline 多一层的全部 moving prime 被 exact Bezout identity 压成唯一 fixed exception `p=7`。本文不排除 `p=7`，也不宣称 A2 closure。

---

## 1. target setting

固定当前 genuine non-`3` inert equal-depth omega-height oversaturation target prime `p`。写

\[
\boxed{
v_p(\omega)=v_p(W_q)=h\ge1.}
\tag{1.1}
\]

沿用

\[
\boxed{
\mathcal P_{\omega H}(K)
:=6K^2-36K+55.}
\tag{1.2}
\]

`spontaneous-height-equal-depth-decimal-pair.md` 已从 `B_W` oversaturation 精确得到

\[
\boxed{
v_p(\mathcal P_{\omega H}(K))=h.}
\tag{1.3}
\]

另一方面

\[
\boxed{qW_q=DK-N,}
\tag{1.4}
\]

且当前 genuine height prime 与 `qD` 分离，因此

\[
\boxed{
v_p(DK-N)=h.}
\tag{1.5}
\]

记

\[
U:=DK-N=qW_q.
\tag{1.6}
\]

于是 target baseline 已同时落在一个 quadratic value 与一个 linear value 上：

\[
\boxed{
p^h\Vert \mathcal P_{\omega H}(K),
\qquad
p^h\Vert U.}
\tag{1.7}
\]

---

## 2. `P_{omega H}(K)` 是一个只有 `2M+3` 位的 pure-prefix carrier

当前 endpoint 写

\[
N=10^M,
\qquad
\frac{249}{250}<y:=\frac{10a_2}{N}<1,
\]

所以

\[
\frac KN=9+y
\]
满足

\[
\boxed{
\frac{2499}{250}<\frac KN<10.}
\tag{2.1}
\]

又 `M>=11`。因此

\[
\frac{\mathcal P_{\omega H}(K)}{N^2}
=6\left(\frac KN\right)^2
-\frac{36}{N}\frac KN
+\frac{55}{N^2}.
\tag{2.2}
\]

下界使用 `K/N>2499/250`、`K/N<10` 与 `N>=10^11`：

\[
\frac{\mathcal P_{\omega H}(K)}{N^2}
>
6\left(\frac{2499}{250}\right)^2
-\frac{360}{10^{11}}
>599.
\tag{2.3}
\]

上界则由 `K<10N` 且 `K>=1`：

\[
6K^2<600N^2,
\qquad
-36K+55<0,
\]
所以

\[
\boxed{
599N^2
<\mathcal P_{\omega H}(K)
<600N^2.}
\tag{2.4}
\]

因此

\[
\boxed{
\mathcal P_{\omega H}(K)
\text{ 恰有 }2M+3\text{ 个十进制数字}.}
\tag{2.5}
\]

这比此前 `J_H/H_pref` 的 `4M+1` 位 carrier 更短；它直接读取 target baseline `h`，但不读取 resonance tail `rho_p`。

---

## 3. 所有 equal-depth oversaturation targets 的 baseline product 共享同一短 carrier

令 `E_tar` 为当前所有 genuine non-`3` equal-depth omega-height oversaturation target primes。对每个

\[
p\in E_{\rm tar}
\]
写

\[
h_p:=v_p(\omega)=v_p(W_q).
\]

定义

\[
\boxed{
G_{\rm tar}:=
\prod_{p\in E_{\rm tar}}p^{h_p}.}
\tag{3.1}
\]

由 (1.3)，不同 target primes 的对应 prime powers 全部整除同一个 `P_{omega H}(K)`：

\[
\boxed{
G_{\rm tar}\mid\mathcal P_{\omega H}(K).}
\tag{3.2}
\]

而且 target support 上是 exact baseline depth：

\[
\boxed{
v_p(\mathcal P_{\omega H}(K))=h_p.}
\tag{3.3}
\]

结合 (2.4)：

\[
\boxed{
G_{\rm tar}<600\cdot10^{2M}.}
\tag{3.4}
\]

等价地

\[
\boxed{
\sum_{p\in E_{\rm tar}}h_p\log p
<\log600+2M\log10.}
\tag{3.5}
\]

这是一个只依赖 `M` 的 target-baseline global budget；第三块长度 `m` 已完全消失。

---

## 4. target-specific gcd ladder 可以直接用 `P_{omega H}` 代替 `Gamma`

上一层定义了 canonical full-tail quotient

\[
\Lambda_{\rm tail},
\]

并对 equal-depth target prime证明

\[
\boxed{v_p(\Lambda_{\rm tail})=\rho_p.}
\tag{4.1}
\]

对 `k>=1` 定义纯 prefix target ladder

\[
\boxed{
T_k
:=\gcd\!\left(
\mathcal P_{\omega H}(K)^k,
\Lambda_{\rm tail}
\right).}
\tag{4.2}
\]

则对每个真正 target prime，由 (1.3)、(4.1)：

\[
\boxed{
v_p(T_k)=\min(kh_p,\rho_p).}
\tag{4.3}
\]

所以 target 的完整 resonance tail 可以在一个 `2M+3` 位 pure-prefix base 上逐层读取。

必须审计：`T_k` 可能还含有并非 omega-height oversaturation target 的其它 common primes，因此 (4.3) 只对真实 target support 给出 exact valuation；本文不把 `T_k` 的全部 support 误称为 target set。

---

## 5. 消去 `K`：一个 source-prefix resultant

由

\[
U=DK-N
\]
定义

\[
\boxed{
\mathscr R_{PD}
:=55D^2-36DN+6N^2.}
\tag{5.1}
\]

直接展开 `D^2 P_{omega H}(K)`：

\[
\boxed{
D^2\mathcal P_{\omega H}(K)
=
\mathscr R_{PD}
+(12N-36D)U
+6U^2.}
\tag{5.2}
\]

所以由 (1.7)：

\[
\boxed{p^h\mid\mathscr R_{PD}.}
\tag{5.3}
\]

也就是说 target baseline `h` 还必须由一个完全不含 `K,omega,W_q,a_3,b_3` 的 source-prefix quadratic 承担。

模 `p` 看 (5.1)，因为 `p\nmid N`：

\[
55\left(\frac DN\right)^2
-36\frac DN+6\equiv0\pmod p.
\tag{5.4}
\]

其 discriminant 仍为

\[
36^2-4\cdot55\cdot6=-24,
\]
所以这里的 first-layer quadratic character仍只是已有 `sqrt(-6)` orbit 的重写；本文不把它计作新的 Legendre obstruction。

---

## 6. deep resonance 把 `R_PD/p^h` 压成一个线性 factor

现在进一步假设

\[
\boxed{\rho_p\ge1.}
\tag{6.1}
\]

`spontaneous-height-equal-depth-decimal-pair.md` 定义

\[
R_+=D\mathcal P_{\omega H}(K)-KU
\tag{6.2}
\]

并证明 deep resonance 时

\[
\boxed{p^{h+1}\mid R_+.}
\tag{6.3}
\]

写

\[
\mathcal P_{\omega H}(K)=p^hP_0,
\qquad
U=p^hU_0,
\qquad
p\nmid P_0U_0.
\tag{6.4}
\]

由 (6.2)–(6.3) 除以 `p^h`：

\[
\boxed{DP_0\equiv KU_0\pmod p.}
\tag{6.5}
\]

另一方面 `U=DK-N` 且 `p|U`，所以

\[
\boxed{DK\equiv N\pmod p.}
\tag{6.6}
\]

将 (5.2) 除以 `p^h` 并模 `p`，`U^2/p^h` 因 `h>=1` 消失：

\[
\frac{\mathscr R_{PD}}{p^h}
\equiv
D^2P_0-(12N-36D)U_0
\pmod p.
\]

再用 (6.5)、(6.6)：

\[
D^2P_0
\equiv DKU_0
\equiv NU_0
\pmod p.
\]

因此得到关键 next-layer identity：

\[
\boxed{
\frac{\mathscr R_{PD}}{p^h}
\equiv
(36D-11N)U_0
\pmod p.}
\tag{6.7}
\]

由于 `U_0` 为 p-unit：

\[
\boxed{
v_p(\mathscr R_{PD})>h
\Longleftrightarrow
p\mid(36D-11N)
\qquad(\rho_p\ge1).}
\tag{6.8}
\]

所以 moving deep resonance 若想让 source-prefix resultant 继续超过 baseline depth，已经被压到一个单独的线性 source ratio。

---

## 7. 线性 exceptional overlap 只能是固定素数 `7`

`R_PD` 与 `36D-11N` 有 exact Bezout identity

\[
\boxed{
1296\mathscr R_{PD}
-(1980D-691N)(36D-11N)
=175N^2.}
\tag{7.1}
\]

直接展开即可验证。

若 genuine target prime满足

\[
p\mid\mathscr R_{PD},
\qquad
p\mid(36D-11N),
\]
则由 `p\nmid6N` 和 (7.1)：

\[
p\mid175=5^2\cdot7.
\]

当前 prime 非 `5`，因此

\[
\boxed{p=7.}
\tag{7.2}
\]

结合 (6.8)：

\[
\boxed{
\rho_p\ge1,\ p\ne7
\Longrightarrow
v_p(\mathscr R_{PD})=h.}
\tag{7.3}
\]

这是一条新的 exact-depth statement：所有 moving deep target primes 在 `R_PD` 上都只能支付 baseline `h`，唯一可能让该 resultant继续 Hensel 加深的 prime 被固定为 `7`。

---

## 8. `p=7` 的固定局部形状

本文不排除 `p=7`，但其 first-layer residue 已完全固定。

若

\[
7\mid(36D-11N),
\]
则

\[
\boxed{D\equiv4N\pmod7.}
\tag{8.1}
\]

又 `U=DK-N` 被 `7` 整除，所以

\[
4K-1\equiv0\pmod7,
\]
即

\[
\boxed{K\equiv2\pmod7.}
\tag{8.2}
\]

而

\[
\mathcal P_{\omega H}(2)
=24-72+55=7,
\]
所以这与 `P_{omega H}` 的 simple `7`-root完全一致。

因此 fixed `7` branch 是一个真正的 simple local orbit，不能仅凭 first-order resultant排除；若后续需要关闭它，应单独使用更高 `7`-adic digit、source allocation 或 endpoint size，而不能把 (7.2) 误写成矛盾。

---

## 9. 当前 target frontier

现在 equal-depth omega-height target 已有三层 canonical reader：

\[
\boxed{
\begin{array}{c|c|c}
\text{层}&\text{carrier}&\text{target p-depth}\\ \hline
\text{baseline prefix}
&\mathcal P_{\omega H}(K)
&h\\
\text{full resonance tail}
&\Lambda_{\rm tail}
&\rho_p\\
\text{source-prefix check}
&\mathscr R_{PD}
&h\quad(p\ne7,\ \rho_p\ge1).
\end{array}}
\tag{9.1}
\]

其中 `P_{omega H}` 只有 `2M+3` 位，并统一容纳所有 target baseline prime powers；`Lambda_tail` 读取全部 tail；`R_PD` 则证明除 fixed `7` 外 deep target 的 source-prefix resultant不能继续超过 baseline。

下一步最有价值的攻击点已经变成：

1. 单独处理 fixed `7` orbit；
2. 对 `p!=7`，把两个 exact-baseline carriers `P_{omega H}` 与 `R_PD` 的 unit quotients联立 `Lambda_tail`，尝试产生第二个不再属于 `sqrt(-6)` shadow 的线性/Archimedean约束；
3. 或利用 global bound `G_tar<600*10^{2M}` 与 `Lambda_tail` 的 full-tail budget证明 target weighted product过饱和。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-target-selector"></a>

> 整合来源：`spontaneous-height-equal-depth-target-selector.md`

# A2 deep equal-depth oversaturation 的 canonical target selector

> **依赖：** `spontaneous-height-companion-cross.md`、`spontaneous-height-equal-depth-tail-gcd-ladder.md`、`spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-resultant-parity.md`。
>
> **严格状态：**前面的论证已经分别 canonical 化了三件事：`J_H/B_W` 在完整 height gcd 之后是否继续共享 prime、`omega/W_q` 是否为 equal-depth common prime、以及该 equal-depth prime 是否具有 `rho_p>0` 的 resonance tail。本文把三层合成一个普通整数 gcd `Sigma_deep=gcd(G_JB,Gamma,Lambda_tail)`。在当前 genuine non-`3` denominator-separated sector，`p|Sigma_deep` 当且仅当 `p` 同时是 residual `J^circ/B^circ` common prime、equal-depth `omega/W_q` common prime、且 resonance tail 为正。因此 deep equal-depth omega-height oversaturation support 不再需要预先列 prime 集合即可定义。本文只给 support selector；split primes 或其它非目标 sector仍需按既有 genuine/inert 条件过滤，不宣称 A2 closure。

---

## 1. residual companion common carrier

已有全局 height gcd

\[
\boxed{
D_H
:=\gcd(\widehat{\mathcal J}_H,W_q)
=\gcd(\mathscr B_W,W_q).}
\tag{1.1}
\]

定义 height-free companions

\[
\boxed{
J^\circ:=\frac{\widehat{\mathcal J}_H}{D_H},
\qquad
B^\circ:=\frac{\mathscr B_W}{D_H}.}
\tag{1.2}
\]

再定义

\[
\boxed{
G_{JB}:=\gcd(J^\circ,B^\circ).}
\tag{1.3}
\]

于是对任意 odd prime：

\[
\boxed{
p\mid G_{JB}
\Longleftrightarrow
p\mid J^\circ\ \text{且}\ p\mid B^\circ.}
\tag{1.4}
\]

所以 `G_JB` 正是“完整 height part 已约掉以后，两个 companions仍然复用同一 prime”的 canonical integer carrier。

---

## 2. equal-depth common square carrier

此前 square-core / tail-normalization 文件定义

\[
\boxed{
\Gamma:=\gcd(\omega,W_q).}
\tag{2.1}
\]

逐 common prime写

\[
e=v_p(\omega),
\qquad
h=v_p(W_q).
\]

则

\[
v_p(\Gamma)=\min(e,h).
\tag{2.2}
\]

同时 canonical tail quotient为

\[
\boxed{
\Lambda_{\rm tail}
=\frac{\Lambda_{\rm dec}}
{\gcd(\alpha,\Lambda_{\rm dec})}.}
\tag{2.3}
\]

`spontaneous-height-equal-depth-tail-gcd-ladder.md` 已在当前 genuine non-`3` denominator-separated common-prime sector证明

\[
\boxed{
 v_p(\Lambda_{\rm tail})
 =
 \begin{cases}
 0,&e\ne h,\\[1mm]
 \rho_p,&e=h.
 \end{cases}}
\tag{2.4}
\]

因此

\[
\boxed{
p\mid\gcd(\Gamma,\Lambda_{\rm tail})
\Longleftrightarrow
e=h\ge1\ \text{且}\ \rho_p>0}
\tag{2.5}
\]

在该 genuine sector成立。

---

## 3. 三层合并成一个 ordinary gcd

定义

\[
\boxed{
\Sigma_{\rm deep}
:=\gcd(
G_{JB},
\Gamma,
\Lambda_{\rm tail}
).}
\tag{3.1}
\]

固定当前 genuine non-`3` denominator-separated common prime `p`。

若

\[
p\mid\Sigma_{\rm deep},
\]
则：

1. `p|G_JB`，故完整 height gcd 约去后仍有
   \[
   p\mid J^\circ,
   \qquad
   p\mid B^\circ;
   \]
2. `p|Gamma`，故 `p` 同时进入 `omega,W_q`；
3. `p|Lambda_tail`，结合 (2.4) 强迫
   \[
   e=h,
   \qquad
   \rho_p>0.
   \]

反过来，若 `p` 满足

\[
p\mid J^\circ,
\quad
p\mid B^\circ,
\quad
e=h\ge1,
\quad
\rho_p>0,
\]
则显然

\[
p\mid G_{JB},
\quad
p\mid\Gamma,
\quad
p\mid\Lambda_{\rm tail},
\]
所以

\[
p\mid\Sigma_{\rm deep}.
\]

因此得到 exact support equivalence：

\[
\boxed{
 p\mid\Sigma_{\rm deep}
 \Longleftrightarrow
 \begin{cases}
 p\mid J^\circ,\ B^\circ,\\
 v_p(\omega)=v_p(W_q)\ge1,\\
 \rho_p>0,
 \end{cases}}
\tag{3.2}
\]

对当前 genuine non-`3` denominator-separated common-prime sector成立。

---

## 4. inert omega-height targets 现在只是 `Sigma_deep` 的一个 filtered support

本文的 `Sigma_deep` 本身不编码 quadratic inertness。真正当前 parity target 还要求

\[
p\equiv3\pmod4,
\]
以及 parent omega-height analysis给出的

\[
\boxed{p\equiv7\text{ 或 }11\pmod{24}.}
\tag{4.1}
\]

所以真正 deep equal-depth inert oversaturation target support 可以理解为

\[
\boxed{
\operatorname{Supp}(\Sigma_{\rm deep})
\cap
\{p:p\equiv7,11\pmod{24}\},}
\tag{4.2}
\]

并继续排除仓库中已经单列的 fixed / denominator / central exceptions。

重要的是：prime set 现在只是 `Sigma_deep` 的 support filter，而不再是定义 resonance branch 所必需的外部数据。

---

## 5. selected target 自动进入短 prefix quadratic

`spontaneous-height-equal-depth-target-ladder.md` 已证明：对真正 equal-depth omega-height oversaturation target，

\[
\boxed{
v_p(\mathcal P_{\omega H}(K))=h,}
\tag{5.1}
\]
其中

\[
\mathcal P_{\omega H}(K)
=6K^2-36K+55
\]
并且

\[
\boxed{
599N^2
<\mathcal P_{\omega H}(K)
<600N^2.}
\tag{5.2}
\]

所以每个 inert target prime `p|Sigma_deep` 在通过既有 omega-height target 条件后，其 baseline `p^h` 都由一个恰有 `2M+3` 位的 pure-prefix integer精确读取。

因此可以定义无需 prime list 的 candidate prefix selector

\[
\boxed{
G_{\rm pref}
:=\gcd(
\Gamma,
\mathcal P_{\omega H}(K)
).}
\tag{5.3}
\]

对每个真正 selected target：

\[
\boxed{v_p(G_{\rm pref})=h.}
\tag{5.4}
\]

`G_pref` 可能含有不满足 residual companion condition的额外 prime，因此 (5.4) 是 target-support exactness，而不是 converse characterization。

---

## 6. deep target ladder 的 fully canonical pipeline

现在无需预先 factorization或手工 prime pool即可写出：

\[
\boxed{
\begin{aligned}
D_H
&=\gcd(\widehat{\mathcal J}_H,W_q),\\
G_{JB}
&=\gcd(\widehat{\mathcal J}_H/D_H,
        \mathscr B_W/D_H),\\
\Gamma
&=\gcd(\omega,W_q),\\
\Lambda_{\rm tail}
&=\Lambda_{\rm dec}/\gcd(\alpha,\Lambda_{\rm dec}),\\
\Sigma_{\rm deep}
&=\gcd(G_{JB},\Gamma,\Lambda_{\rm tail}),\\
G_{\rm pref}
&=\gcd(\Gamma,\mathcal P_{\omega H}(K)).
\end{aligned}}
\tag{6.1}
\]

在 genuine inert target sector，`Sigma_deep` 选择 deep equal-depth residual overlap support，而 `G_pref` 为这些 selected targets 读取完整 baseline `h`。

这把此前的逻辑

\[
\text{residual overlap}
+\text{equal depth}
+\text{deep unit resonance}
+\text{target quadratic}
\]

压成了一组 ordinary integer gcds。

---

## 7. 当前 frontier

现在真正需要关闭的 moving object不再是一个人工定义的 prime family，而是 canonical integer

\[
\boxed{\Sigma_{\rm deep}.}
\tag{7.1}
\]

对其 genuine inert support：

- baseline depth由 `G_pref` / `P_{omega H}` 的 `2M+3` 位窗口控制；
- full resonance depth由 `Lambda_tail` 控制；
- source-prefix resultant `R_PD` 已证明除 fixed `7` 外只能保持 baseline `h`；
- fixed `7` extra-depth branch已进一步压成 `M≡1,5 (mod 6)` 的四个 mod-`7` states。

所以后续最直接的 closure target是证明

\[
\boxed{
\operatorname{Supp}_{\rm inert}(\Sigma_{\rm deep})
=\varnothing,}
\tag{7.2}
\]

或至少证明其 weighted product不足以承担 global odd-inert parity。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-three-cancellation-readers"></a>

> 整合来源：`spontaneous-height-equal-depth-three-cancellation-readers.md`

# A2 equal-depth 的 three decimal cancellation readers 与 first-tail shadow

> **依赖：** `spontaneous-height-equal-depth-decimal-tropical-identity.md`、`spontaneous-height-equal-depth-tail-reader.md`、`spontaneous-height-equal-depth-dual-short-carriers.md`。
>
> **严格状态：**本文把 `B_dec`,`E_+`,`Lambda_dec` 各自改写成一个两项 cancellation。对 equal-depth target，三者分别测量 `r_B,r_+,rho_p`。在 first normalized layer，`B_dec` residual equation与 `E_+` residual equation已经自动推出 `Lambda_dec` 的第一层 tail equation；因此 `rho_p>=1` 的 first digit在这个三-reader系统里不是第三条独立 obstruction。真正独立的新信息从第二个 excess digit或 minimum-tie后的 next normalized unit开始。本文是 no-double-count 与 canonical-normalization lemma，不关闭 A2。

---

## 1. three exact two-term readers

沿用

\[
P:=6K^2-36K+55,
\]

\[
F_H:=P-K^2=5K^2-36K+55,
\]

\[
\alpha=TK+a_3,
\qquad
\beta=TQ+b_3,
\]

\[
\Delta=K\beta-Q\alpha.
\]

### 1.1 `B_dec`

前一文件定义

\[
B_{\rm dec}
=b_3^2F_H+T^2Q^2K^2.
\]

由于 `F_H=P-K^2`：

\[
\begin{aligned}
B_{\rm dec}
&=b_3^2P+K^2(T^2Q^2-b_3^2)\\
&=b_3^2P+K^2(TQ-b_3)(TQ+b_3).
\end{aligned}
\]
而 `TQ+b_3=beta`，所以

\[
\boxed{
B_{\rm dec}
=b_3^2P+K^2(TQ-b_3)\beta.}
\tag{1.1}
\]

### 1.2 `E_+`

由定义

\[
E_+=F_H\beta+K\Delta.
\]
使用 `F_H=P-K^2` 和 `Delta=Kbeta-Qalpha`：

\[
\boxed{
E_+=P\beta-KQ\alpha.}
\tag{1.2}
\]

所以 `r_+` 就是两个 baseline-depth `2h` products之间的 excess cancellation。

### 1.3 `Lambda_dec`

full-tail reader定义

\[
\Lambda_{\rm dec}=2\beta\Delta+TQ^2\alpha.
\]
代入 `Delta=Kbeta-Qalpha`：

\[
\begin{aligned}
\Lambda_{\rm dec}
&=2K\beta^2-2Q\alpha\beta+TQ^2\alpha\\
&=2K\beta^2+Q\alpha(TQ-2\beta).
\end{aligned}
\]
而

\[
TQ-2\beta=-(TQ+2b_3).
\]
令

\[
F_{\rm dec}:=TQ+2b_3,
\]
得到

\[
\boxed{
\Lambda_{\rm dec}
=2K\beta^2-QF_{\rm dec}\alpha.}
\tag{1.3}
\]

---

## 2. target normalized units

固定 genuine deep equal-depth target：

\[
v_p(P)=v_p(\beta)=h,
\qquad
v_p(\alpha)=2h.
\]

写

\[
\boxed{
P=p^hP_0,
\qquad
\beta=p^h\beta_0,
\qquad
\alpha=p^{2h}A_0,}
\tag{2.1}
\]
其中

\[
p\nmid P_0\beta_0A_0.
\]

因为 `p|beta=TQ+b_3`：

\[
\boxed{TQ\equiv-b_3\pmod p.}
\tag{2.2}
\]

所以

\[
\boxed{TQ-b_3\equiv-2b_3\pmod p,}
\tag{2.3}
\]

\[
\boxed{F_{\rm dec}=TQ+2b_3\equiv b_3\pmod p.}
\tag{2.4}
\]

当前 `p∤2b_3KQ`。

---

## 3. `B_dec` 的 first residual equation

oversaturation给

\[
v_p(B_{\rm dec})=h+r_B,
\qquad r_B\ge1.
\]

把 (1.1) 除以 `p^h` 并模 `p`：

\[
b_3^2P_0
+K^2(TQ-b_3)\beta_0
\equiv0.
\]
用 (2.3)：

\[
b_3^2P_0-2b_3K^2\beta_0\equiv0.
\]
除以 unit `b_3`：

\[
\boxed{
b_3P_0\equiv2K^2\beta_0\pmod p.}
\tag{3.1}

这是 height residual `r_B>=1` 的 first normalized cancellation。

---

## 4. `E_+` 的 first residual equation

在 deep branch中

\[
v_p(E_+)\ge2h+1.
\]

由 (1.2) 除以 `p^{2h}`：

\[
\boxed{
\beta_0P_0
\equiv
KQ A_0
\pmod p.}
\tag{4.1}

它把 square-core unit `A_0` 与 prefix/denominator baseline units同步。

---

## 5. first tail equation自动推出

把 (3.1) 乘以 `beta_0`：

\[
b_3\beta_0P_0
\equiv2K^2\beta_0^2.
\tag{5.1}
\]

再用 (4.1)：

\[
b_3KQ A_0
\equiv2K^2\beta_0^2.
\]
除以 unit `K`：

\[
\boxed{
Qb_3A_0
\equiv2K\beta_0^2
\pmod p.}
\tag{5.2}

另一方面由 (1.3)、(2.4)：

\[
\frac{\Lambda_{\rm dec}}{p^{2h}}
\equiv
2K\beta_0^2-Qb_3A_0
\pmod p.
\]

所以 (5.2) 精确等价于

\[
\boxed{p^{2h+1}\mid\Lambda_{\rm dec}.}
\tag{5.3}

也就是

\[
\boxed{\rho_p\ge1.}
\tag{5.4}

因此在同时知道 `r_B>=1` 与 `E_+` first excess 的三-reader视角中，first tail digit自动成立。

---

## 6. converse redundancy

同样地，三条 first normalized equations中任意两条可以恢复第三条。

例如 (3.1) 与 tail equation (5.2) 给

\[
P_0=2K^2\beta_0/b_3,
\qquad
Q A_0=2K\beta_0^2/b_3,
\]
所以

\[
\beta_0P_0
=KQ A_0,
\]
即恢复 (4.1)。

因此 first layer 的三个 cancellation conditions只有 rank `2`：

\[
\boxed{
\{B_{\rm dec},E_+,\Lambda_{\rm dec}\}
\text{ 的 first residual equations存在一条结构性依赖}.}
\tag{6.1}

本文不把这个 rank-2 statement外推到 higher digits；higher residual depths正是后续 tie analysis 的新信息来源。

---

## 7. correct interpretation of `rho>=1`

full-tail reader当然仍然严格给

\[
v_p(\Lambda_{\rm dec})=2h+\rho_p
\]
并完整读取任意高的 `rho_p`。

本文只审计它的第一个 extra digit：

\[
\boxed{
\rho_p\ge1\text{ 的 first normalized equation
在 }r_B\ge1\text{ 与 }E_+\ge2h+1\text{ 后是 shadow}.}
\tag{7.1}

所以后续不能把

\[
r_B\ge1,
\quad E_+\ge2h+1,
\quad\rho_p\ge1
\]
当成三条独立 first-order local constraints。

真正新增的 tail information是：

\[
\boxed{\rho_p\ge2}
\]
或更高 normalized digits，以及它们与 `r_B,h` minimum ties 的相对深度。

---

## 8. current higher-digit frontier

three-reader系统现在具有清楚的层次：

- first digit：rank-2，tail first digit自动 shadow；
- unique-minimum higher depth：由 tropical law直接 exact；
- pair/triple minimum ties：只有这里可能出现真正新的 higher cancellation；
- full tail arbitrary depth：仍由 `Lambda_tail` 精确读取。

因此下一步应直接计算 §§ pair-tie 的第二 normalized digit，而不再重复 first-layer Legendre/root/cancellation条件。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-triple-orientation"></a>

> 整合来源：`spontaneous-height-equal-depth-triple-orientation.md`

# A2 equal-depth target 的 triple `sqrt(-6)` orientation 与 fixed `2671`

> **依赖：** `spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-equal-depth-dual-short-carriers.md`、`spontaneous-height-equal-depth-decimal-pair.md`。
>
> **严格状态：**本文把 prefix quadratic `P`、source-prefix resultant `R_PD` 与真实 third carrier `R_3` 统一写成同一个 `sqrt(-6)` norm orbit，并识别真正 equal-depth numerator sheet在 source 与 third 两侧采取同一反向 orientation。由此构造 cross-orientation linear carrier `L_D3=55TD-36TN-6Na_3`。在 deep resonance `rho_p>=1` 下，所有 genuine moving target primes 都满足 `v_p(L_D3)=h`；若 `L_D3` 想超过 baseline `h`，exact Bezout 强迫唯一 fixed prime `p=2671`。因此 moving deep target 的两个独立 next-depth directions现已分别只留下 fixed `7`（source-prefix）与 fixed `2671`（source-vs-third orientation）两个例外。本文不排除 fixed `2671`，不关闭 A2。

---

## 1. 三个 `sqrt(-6)` carriers

沿用

\[
\boxed{P:=6K^2-36K+55=6(K-3)^2+1.}
\tag{1.1}
\]

source-prefix resultant 为

\[
\boxed{R_{PD}:=55D^2-36DN+6N^2.}
\tag{1.2}
\]

直接配方：

\[
\boxed{
55R_{PD}=(55D-18N)^2+6N^2.}
\tag{1.3}
\]

真实 third carrier 为

\[
\boxed{R_3:=6(a_3+3T)^2+T^2.}
\tag{1.4}
\]

所以三个 target conditions 都在同一个 quadratic extension `sqrt(-6)` 中。

定义对应的 normalized square roots

\[
\boxed{
X_P:=6(K-3),
\qquad
X_D:=\frac{55D-18N}{N},
\qquad
X_3:=6\frac{a_3+3T}{T}.}
\tag{1.5}
\]

对 genuine target prime `p`，`N,T` 都是 p-units。

由 `p|P`：

\[
X_P^2\equiv-6\pmod p.
\tag{1.6}
\]

由 `p|R_PD`：

\[
X_D^2\equiv-6\pmod p.
\tag{1.7}
\]

由 `p|R_3`：

\[
X_3^2\equiv-6\pmod p.
\tag{1.8}
\]

---

## 2. source-prefix root 与 prefix root 取反 orientation

真正 target 还有

\[
U:=DK-N=qW_q,
\qquad p^h\Vert U,
\]

所以 first layer

\[
DK\equiv N\pmod p.
\tag{2.1}
\]

于是

\[
\frac DN\equiv K^{-1}\pmod p.
\]

利用 `P(K)=0 mod p`：

\[
6K^2-36K+55\equiv0,
\]
故

\[
55-18K
\equiv18K-6K^2
=-6K(K-3).
\]

除以 unit `K`：

\[
\boxed{
X_D
=\frac{55D-18N}{N}
\equiv-6(K-3)
=-X_P
\pmod p.}
\tag{2.2}
\]

所以 source-prefix resultant选择的是 `P` root 的反向 `sqrt(-6)` orientation。

---

## 3. numerator sheet 的 third root也取反 orientation

真正 equal-depth target满足

\[
p\mid\alpha,
\qquad
\alpha=TK+a_3.
\]

因此

\[
\frac{a_3}{T}\equiv-K\pmod p.
\]

于是

\[
\boxed{
X_3
=6\left(\frac{a_3}{T}+3\right)
\equiv-6(K-3)
=-X_P
\pmod p.}
\tag{3.1}
\]

所以 numerator sheet 上

\[
\boxed{X_D\equiv X_3\equiv-X_P\pmod p.}
\tag{3.2}
\]

与 `spontaneous-height-equal-depth-dual-short-carriers.md` 的 exact sheet split一致：conjugate sheet `L_3=0` 会取 `X_3=+X_P`，而真正 target 的 `alpha=0` sheet取反向 root。

---

## 4. source 与 third orientation 的自然线性差

由 (3.2)，定义 integer cross carrier

\[
\boxed{
\begin{aligned}
\mathcal L_{D3}
&:=TN(X_D-X_3)\\
&=T(55D-18N)-6N(a_3+3T)\\
&=55TD-36TN-6Na_3.
\end{aligned}}
\tag{4.1}
\]

每个 genuine equal-depth target first layer都满足

\[
p\mid\mathcal L_{D3}.
\]

但 deep resonance允许我们精确读取它的下一层。

---

## 5. `L_D3` 与 deep companion 的 exact identity

沿用

\[
R_+:=DP-KU,
\qquad
U=DK-N,
\]

以及

\[
\alpha=TK+a_3.
\]

直接展开得到

\[
\boxed{
\mathcal L_{D3}
=TR_+ +T(36-5K)U-6N\alpha.}
\tag{5.1}
\]

固定 deep equal-depth target：

\[
v_p(P)=h,
\qquad
v_p(U)=h,
\qquad
v_p(\alpha)=2h,
\qquad
\rho_p\ge1.
\]

`spontaneous-height-equal-depth-decimal-pair.md` 已证明

\[
\boxed{v_p(R_+)\ge h+1.}
\tag{5.2}
\]

写

\[
U=p^hU_0,
\qquad p\nmid U_0.
\]

将 (5.1) 除以 `p^h` 并模 `p`。第一项由 (5.2) 消失，第三项因 `2h>=h+1` 也消失，所以

\[
\boxed{
\frac{\mathcal L_{D3}}{p^h}
\equiv
T(36-5K)U_0
\pmod p.}
\tag{5.3}
\]

由于 `T,U_0` 为 p-units：

\[
\boxed{
 v_p(\mathcal L_{D3})>h
 \Longleftrightarrow
 5K-36\equiv0\pmod p
 \qquad(\rho_p\ge1).}
\tag{5.4}
\]

所以 source-vs-third orientation想继续超过 baseline，只可能撞一个新的线性 K-exception。

---

## 6. linear exception 唯一固定为 `2671`

`P` 与 `5K-36` 有 exact Bezout identity

\[
\boxed{
25P-(30K+36)(5K-36)=2671.}
\tag{6.1}
\]

直接展开即可验证。

若 genuine target prime同时满足

\[
p\mid P,
\qquad
p\mid5K-36,
\]
则

\[
p\mid2671.
\]

而

\[
\boxed{2671\text{ 是素数},
\qquad2671\equiv7\pmod{24}.}
\tag{6.2}
\]

因此该 fixed prime确实落在允许的 inert class 中，不能靠 first-layer character排除。

结合 (5.4)：

\[
\boxed{
\rho_p\ge1,
\quad p\ne2671
\Longrightarrow
v_p(\mathcal L_{D3})=h.}
\tag{6.3}
\]

这与 target-ladder 的

\[
\rho_p\ge1,\ p\ne7
\Longrightarrow
v_p(R_{PD})=h
\]

是两个不同的 next-depth directions：

- `7` 控制 source-prefix resultant是否超过 baseline；
- `2671` 控制 source root与真实 third root的 orientation差是否超过 baseline。

---

## 7. fixed `2671` 的 first-layer residue

若进入唯一 exception：

\[
5K-36\equiv0\pmod{2671}.
\]

因为 `5^{-1}\equiv2137 (mod 2671)`：

\[
\boxed{K\equiv2144\pmod{2671}.}
\tag{7.1}
\]

由 `U=DK-N`：

\[
\boxed{D\equiv NK^{-1}\pmod{2671}.}
\tag{7.2}
\]

由 numerator sheet：

\[
\boxed{a_3\equiv-TK\pmod{2671}.}
\tag{7.3}
\]

本文暂不枚举 `M mod ord_{2671}(10)` 或 prefix `B` roots；这应作为 fixed-prime orbit单独处理，而不是把 (6.2) 误写成矛盾。

---

## 8. 当前 triple-orientation frontier

moving deep target现在有四个互补 reader：

\[
\boxed{
\begin{array}{c|c}
\text{carrier}&\text{target depth}\\ \hline
P&h\\
R_3&h\\
R_{PD}&h\quad(p\ne7)\\
\mathcal L_{D3}&h\quad(p\ne2671).
\end{array}}
\tag{8.1}
\]

full resonance tail仍由

\[
v_p(\Lambda_{\rm tail})=\rho_p
\]

精确读取。

因此所有 moving `p\notin\{7,2671\}` deep targets在 prefix、third、source-prefix、cross-orientation四个自然整数上都只能保持 baseline `h`；额外 resonance depth只能留在 canonical tail quotient中，不能再伪装成这些 companion carriers的额外 p-depth。

下一步最自然的是：

1. 单独压 fixed `2671` 的 length/prefix Hensel orbit；
2. 对 moving `p\notin\{7,2671\}`，利用四个 exact-baseline readers与 `Lambda_tail` 的 excess depth做 product/CRT separation；
3. 检查 `7` 与 `2671` 是否可能同时进入同一 global parity allocation。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-equal-depth-tropical-balance"></a>

> 整合来源：`spontaneous-height-equal-depth-tropical-balance.md`

# A2 equal-depth `R_+` 的 tropical depth balance

> **依赖：** `spontaneous-height-equal-depth-decimal-pair.md`、`spontaneous-height-equal-depth-tail-reader.md`。
>
> **严格状态：**此前 decimal-pair 文件只使用 exact Bezout 给出 `v_p(R_+)>=h+min(r_B,h,rho_p)`。本文保留三项的精确赋值，得到更强的 tropical law：若 `r_B,h,rho_p` 的最小值唯一，则 `R_+` 的 excess depth恰等于该最小值；只有至少两项在最低层并列时，`R_+` 才可能进一步 cancellation。作为直接推论，baseline `h=1` 时若 `E_+` 超过最小 deep depth `3`，则 `r_B` 或 full tail `rho_p` 至少一个必须精确等于 `1`。本文是 valuation allocation lemma，不关闭 A2。

---

## 1. equal-depth notation

固定 genuine non-`3` equal-depth oversaturation target：

\[
v_p(\omega)=v_p(W_q)=h\ge1.
\]

写

\[
\boxed{v_p(B_W)=h+r_B,\qquad r_B\ge1,}
\tag{1.1}
\]

以及 full resonance depth

\[
\boxed{v_p(L_{JB})=h+\rho_p,\qquad\rho_p\ge0.}
\tag{1.2}
\]

在本文关注的 deep branch中

\[
\rho_p\ge1.
\]

定义

\[
\boxed{r_+:=v_p(R_+)-h.}
\tag{1.3}
\]

因为

\[
E_+=E_M\omega R_+,
\qquad v_p(E_M\omega)=h,
\]
所以

\[
\boxed{v_p(E_+)=2h+r_+.}
\tag{1.4}
\]

---

## 2. exact three-term Bezout

沿用

\[
A_H:=g\omega,
\qquad
f=A_H+c_u,
\qquad
z=A_H-c_u.
\]

decimal-pair 文件证明

\[
\boxed{
c_u^2fR_+
=DfB_W-DzA_H^2K^2+Kc_u^2L_{JB}.}
\tag{2.1}
\]

当前 genuine target 与

\[
D,f,z,K,c_u,g
\]
全部分离，因此这些系数都是 p-units。

又

\[
v_p(A_H)=v_p(g\omega)=h.
\]

于是 (2.1) 右侧三项的赋值不是只有 lower bounds，而是精确为

\[
\boxed{
\begin{array}{c|c}
\text{term}&p\text{-depth}\\ \hline
DfB_W&h+r_B\\
DzA_H^2K^2&2h\\
Kc_u^2L_{JB}&h+\rho_p.
\end{array}}
\tag{2.2}
\]

左侧 coefficient `c_u^2f` 也是 unit，所以

\[
\boxed{v_p(\text{LHS})=h+r_+.}
\tag{2.3}
\]

---

## 3. tropical minimum law

令

\[
\boxed{m_*:=\min\{r_B,h,\rho_p\}.}
\tag{3.1}
\]

从 (2.2) 提出共同 `p^h` 后，右侧三项的 residual depths就是

\[
r_B,\quad h,\quad\rho_p.
\]

非阿基米德三角不等式立即给旧结论

\[
\boxed{r_+\ge m_*.}
\tag{3.2}
\]

但如果 `m_*` 在

\[
r_B,h,\rho_p
\]
中只由一个量取得，那么右侧存在唯一最浅项。其它两项都至少再多一层 `p`，因此不可能消去该唯一最浅 residual unit。

所以：

\[
\boxed{
\text{若 }m_*\text{ 是唯一最小值，则 }r_+=m_*.}
\tag{3.3}
\]

等价的逆命题为

\[
\boxed{
r_+>m_*
\Longrightarrow
m_*\text{ 至少由 }r_B,h,\rho_p\text{ 中两项同时取得}.}
\tag{3.4}
\]

这就是 equal-depth resonance 的 tropical balance law。

---

## 4. 三个 unique-minimum sectors 都变成 exact reader

(3.3) 给三个直接可复用的 exact cases。

### `B_W` residual 最浅

若

\[
r_B<\min\{h,\rho_p\},
\]
则

\[
\boxed{r_+=r_B.}
\tag{4.1}
\]

于是

\[
\boxed{v_p(E_+)=2h+r_B.}
\tag{4.2}
\]

### square-content term 最浅

若

\[
h<\min\{r_B,\rho_p\},
\]
则

\[
\boxed{r_+=h,}
\tag{4.3}
\]

即

\[
\boxed{v_p(E_+)=3h.}
\tag{4.4}
\]

### full resonance tail 最浅

若

\[
\rho_p<\min\{r_B,h\},
\]
则

\[
\boxed{r_+=\rho_p,}
\tag{4.5}
\]

所以 decimal carrier `E_+` 在这一 sector 直接精确读取 full tail：

\[
\boxed{v_p(E_+)=2h+\rho_p.}
\tag{4.6}
\]

因此 `E_+` 只有在 minimum-tie sectors中才会丢失 exact reader 性质。

---

## 5. `h=1` 的 universal tail squeeze

现在固定

\[
\boxed{h=1}
\tag{5.1}
\]
并仍在 deep branch

\[
r_B\ge1,
\qquad\rho_p\ge1.
\]

于是

\[
m_*=1.
\]

若

\[
\boxed{v_p(E_+)\ge4,}
\tag{5.2}
\]
则由 (1.4)

\[
r_+\ge2>m_*.
\]

根据 (3.4)，最低值 `1` 必须至少出现两次。`h=1` 已经提供一次，因此 `r_B` 或 `rho_p` 至少一个也必须为 `1`：

\[
\boxed{
\min\{r_B,\rho_p\}=1.}
\tag{5.3}
\]

利用 full-tail reader

\[
\rho_p=v_p(\Lambda_{\rm tail}),
\]
也可写成

\[
\boxed{
\min\{r_B,v_p(\Lambda_{\rm tail})\}=1.}
\tag{5.4}
\]

所以 baseline `h=1` 时不存在

\[
\boxed{
v_p(E_+)\ge4,\quad r_B\ge2,\quad\rho_p\ge2}
\tag{5.5}

的三重 deep state。

---

## 6. 与 fixed-7 low-baseline audit 的结合

`spontaneous-height-equal-depth-fixed7-h1-audit.md` 已证明：在 fixed `7`, `K=2`, `h=1` 且

\[
v_7(R_{PD})\ge3
\]
时，只有

\[
K\equiv9\pmod{49}
\]
可能满足

\[
v_7(E_+)\ge4.
\]

本文 (5.3) 于是继续给该唯一 dangerous state：

\[
\boxed{
K\equiv9\pmod{49},\quad v_7(E_+)\ge4
\Longrightarrow
\min\{r_B,\rho_7\}=1.}
\tag{6.1}
\]

所以即使这一唯一 low-baseline residue继续存活，它也不能同时携带第二层 `B_W` residual 与第二层 full resonance tail。

---

## 7. current frontier

现在 `R_+ / E_+` 的 excess不应再被视为一个独立自由深度。其严格结构是：

\[
\boxed{
r_+\ge\min(r_B,h,\rho_p),}
\]
且 strict inequality 只可能发生在 minimum tie 上。

因此后续最有效的 case split是按

\[
\boxed{
\operatorname*{argmin}\{r_B,h,\rho_p\}}
\]
而不是继续单独枚举 `r_+`。

特别地：

- unique-minimum sectors：`E_+` 已是 exact reader；
- tie sectors：真正剩余的是两个或三个 normalized units 的 cancellation；
- `h=1`：任何 `E_+` second-extra state都强迫 `r_B=1` 或 `rho_p=1`。

A2 仍为 `待证`。

---

<a id="source-spontaneous-height-h1-additive-bezout"></a>

> 整合来源：`spontaneous-height-h1-additive-bezout.md`

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

---

<a id="source-spontaneous-height-h2-additive-bezout"></a>

> 整合来源：`spontaneous-height-h2-additive-bezout.md`

# A2 moving height `H_2` / additive 的 exact Bézout depth bridge

> **依赖：** `spontaneous-height-parity-ledger.md`、`spontaneous-height-resultant-parity.md`、`spontaneous-height-h1-additive-bezout.md`、`spontaneous-height-angle-additive-norm-bridge.md`。
>
> **严格状态：**`H_1` orientation 已有 exact Bézout depth bridge；本文补齐第二张 pure-prefix sphere orientation `H_2`。首先把 `H_2` 精确分成一个整数平方与 `Q^2N_0` 项，随后与 additive-height carrier `J_H` 消去 `N_0`，得到新的 positive primitive `3 mod4` carrier `R_H2`。对 genuine external height prime，若 `H_2` 与 `B_W` 深度不等，`R_H2` 精确读取较浅者；equal-depth extra lift 则强迫 normalized `B_W/H_2` ratio 为 `-square`，即 non-square。它与 `H_1` bridge 的 square ratio形成严格互补。本文不宣称 equal-depth shell 已全部关闭。

---

## 1. notation

固定 reflection endpoint：

\[
N:=N_{\rm dec}=10^M,
\qquad A:=a_2,
\qquad B:=b_2,
\]

\[
Q:=B+2N,
\qquad K:=9N+10A,
\]

\[
N_0:=\left(\frac{9B}{2}\right)^2+A^2,
\]

\[
F_W(K):=(K-5)(5K-11)=5K^2-36K+55.
\tag{1.1}
\]

additive-height pure decimal carrier为

\[
\boxed{
\mathcal J_H:=B^2F_W(K)-Q^2N_0.}
\tag{1.2}

第二张 sphere orientation integer 是

\[
\boxed{
\begin{aligned}
\mathcal H_2={}&
404A^4B^2+16A^4BN+16A^4N^2
+1440A^3B^2N\\
&-16119A^2B^4+324A^2B^3N
+1620A^2B^2N^2\\
&-29160AB^4N+164025B^6.
\end{aligned}}
\tag{1.3}

---

## 2. `H_2` 有一个此前未显式记录的 exact square decomposition

定义

\[
\boxed{
\mathcal L_2:=20A^2+36AN-405B^2.}
\tag{2.1}

直接展开得到

\[
\boxed{
\mathcal H_2
=B^2\mathcal L_2^2+4A^2Q^2N_0.}
\tag{2.2}

这是纯整数恒等式。验证只需展开右端：

\[
B^2(20A^2+36AN-405B^2)^2
+4A^2(B+2N)^2
\left(\frac{81B^2}{4}+A^2\right),
\]
逐项即恢复 (1.3)。

这个形式还给 genuine external `H_2` prime 一个简单 unit audit。若

\[
p\mid\mathcal H_2,
\qquad p\nmid2AQN_0,
\]
而又 `p|L_2`，则 (2.2) 会迫使

\[
p\mid4A^2Q^2N_0,
\]
矛盾。因此

\[
\boxed{p\nmid\mathcal L_2}
\tag{2.3}

在 genuine `H_2` locus 自动成立。

---

## 3. exact Bézout identity

由 (1.2)：

\[
4A^2\mathcal J_H
=4A^2B^2F_W-4A^2Q^2N_0.
\]
与 (2.2) 相加，`Q^2N_0` 精确消失：

\[
\boxed{
4A^2\mathcal J_H+\mathcal H_2
=B^2\mathscr R_{H2},}
\tag{3.1}

其中定义

\[
\boxed{
\mathscr R_{H2}
:=\mathcal L_2^2+4A^2F_W(K).}
\tag{3.2}

这就是第二张 orientation 的 exact Bézout carrier。

---

## 4. `R_H2` 是 positive primitive `3 mod4` carrier

真实 endpoint中 `K>5`，所以

\[
F_W(K)=(K-5)(5K-11)>0.
\]
于是 (3.2) 为一个平方加一个严格正项：

\[
\boxed{\mathscr R_{H2}>0.}
\tag{4.1}

再看二进方向。reflection deep-even 中

\[
N=2^M5^M,
\qquad
B=2^{M+m+1}b_0,
\qquad A\text{ odd},
\]
且 `M>=11,m>=1`。

由 (2.1)，`20A^2` 的 2-adic depth恰为 `2`，其余两项深度严格大于 `2`，所以

\[
v_2(\mathcal L_2)=2.
\tag{4.2}

因此

\[
v_2(\mathcal L_2^2)=4.
\]
另一方面 `F_W(K)` 为 odd，所以

\[
v_2(4A^2F_W)=2.
\]
两项深度不同，故

\[
\boxed{v_2(\mathscr R_{H2})=2.}
\tag{4.3}

并且除以 `4` 后，平方项仍为偶数的平方、模 `4` 消失：

\[
\frac{\mathscr R_{H2}}4
\equiv A^2F_W(K)
\pmod4.
\]
当前 `K=2 mod4`，于是

\[
F_W(K)=(K-5)(5K-11)\equiv1\cdot3\equiv3\pmod4.
\]
而 `A^2=1 mod4`，所以

\[
\boxed{
\widehat{\mathscr R}_{H2}
:=\frac{\mathscr R_{H2}}4
>0,
\qquad
\widehat{\mathscr R}_{H2}\equiv3\pmod4.}
\tag{4.4}

因此 `R_H2` 和 `H_1` 文件中的 `R_H1`、universal `R_HO` 一样，提供一份真实 positive odd-inert parity carrier。

---

## 5. 送入 `W_q` height bridge

`spontaneous-height-resultant-parity.md` 已证明

\[
\boxed{
c_u^2\mathcal J_H
\equiv B^2\mathscr B_W
\pmod{W_q}.}
\tag{5.1}

把 (5.1) 代入 (3.1) 乘 `c_u^2` 的形式：

\[
\boxed{
B^2c_u^2\mathscr R_{H2}
\equiv
4A^2B^2\mathscr B_W
+c_u^2\mathcal H_2
\pmod{W_q}.}
\tag{5.2}

与 `H_1` bridge相比，这里的两个 depth-reader coefficients

\[
(2AB)^2,
\qquad c_u^2
\]
本身都是完整 squares。

---

## 6. genuine `H_2` height prime上的 coefficient audit

固定 endpoint-external non-`3` inert prime

\[
p^h\Vert W_q,
\qquad h\ge1,
\qquad p\equiv3\pmod4,
\qquad p\ne3,5,
\]
并假设它进入第二张 sphere orientation：

\[
p\mid\mathcal H_2.
\]

primitive/external separation给

\[
\boxed{p\nmid2ABc_u.}
\tag{6.1}

所以 (5.2) 中

\[
B^2c_u^2,
\qquad4A^2B^2,
\qquad c_u^2
\]
全是 `p`-adic units。由 §2 还知道 `L_2` 本身也是 unit，但后面的 depth law甚至不需要使用这一点。

---

## 7. unequal-depth law

写

\[
e_B:=v_p(\mathscr B_W),
\qquad
e_2:=v_p(\mathcal H_2),
\qquad
e_R:=v_p(\mathscr R_{H2}).
\]

在

\[
\min(e_B,e_2)<h
\]
范围内，(5.2) 是两个 unit-coefficient项之和。

若

\[
e_B<e_2,
\]
则第二项严格更深，不能取消第一项：

\[
\boxed{e_R=e_B.}
\tag{7.1}

若

\[
e_2<e_B,
\]
同理

\[
\boxed{e_R=e_2.}
\tag{7.2}

因此

\[
\boxed{
e_B\ne e_2,
\quad\min(e_B,e_2)<h
\Longrightarrow
v_p(\mathscr R_{H2})=\min(e_B,e_2).}
\tag{7.3}

第二张 orientation 的普通 unequal-depth区由此完全同步。

---

## 8. equal-depth extra lift强迫 `-square`

现在固定唯一危险层

\[
e_B=e_2=e<h.
\]

若 `R_H2` 比共同深度额外提升，则 (5.2) 除以 `p^e` 后必须满足

\[
4A^2B^2\frac{\mathscr B_W}{p^e}
+c_u^2\frac{\mathcal H_2}{p^e}
\equiv0\pmod p.
\]
因此

\[
\boxed{
\frac{\mathscr B_W/p^e}{\mathcal H_2/p^e}
\equiv
-\left(\frac{c_u}{2AB}\right)^2
\pmod p.}
\tag{8.1}

因为 `p=3 mod4`，`-1` 为 non-square，而括号中是 unit square，所以

\[
\boxed{
\left(
\frac{(\mathscr B_W/p^e)/(\mathcal H_2/p^e)}p
\right)=-1.}
\tag{8.2}

这与第一张 orientation 的结果严格互补。`spontaneous-height-h1-additive-bezout.md` 在 `H_1` equal-depth extra-lift shell得到

\[
\boxed{
(\mathscr B_W/p^e)/(\mathcal H_1/p^e)
\text{ 是 square},}
\tag{8.3}

而本文得到

\[
\boxed{
(\mathscr B_W/p^e)/(\mathcal H_2/p^e)
\text{ 是 non-square}.}
\tag{8.4}

因此 moving-height 两张 sphere orientations现在携带一个明确的 relative character label：

\[
\boxed{
H_1:\ +1,
\qquad
H_2:\ -1.}
\tag{8.5}

这个 label 来自 exact Bézout coefficients，不是另一次 singular-resultant audit。

---

## 9. 与 universal angle-norm bridge 的组合

`spontaneous-height-angle-additive-norm-bridge.md` 已证明，在 universal equal-depth extra-lift shell中

\[
\boxed{
(\mathscr B_W/p^e)/(\mathcal H_O/p^e)
\text{ 是 non-square},}
\tag{9.1}

且

\[
\mathcal H_1\mathcal H_2=4\mathcal H_O.
\tag{9.2}

因此在 companion orientation为 unit 的场合，可把 (8.3)–(8.4) 与 (9.1) 转成 companion character：

- `H_1` equal-depth extra lift若同时由 universal bridge读取，并且 `p∤H_2`，则
  \[
  \boxed{\left(\frac{\mathcal H_2}{p}\right)=-1;}
  \tag{9.3a}
  \]
- `H_2` equal-depth extra lift若同时由 universal bridge读取，并且 `p∤H_1`，则
  \[
  \boxed{\left(\frac{\mathcal H_1}{p}\right)=+1.}
  \tag{9.3b}
  
这是一个新的 cross-orientation character ledger。本文不假定两个 orientation在所有 prime上自动互斥，因此 (9.3) 明确保留 companion-unit 前提。

---

## 10. updated moving-height frontier

两张 moving sphere sheets 的 exact additive bridges现已对称完备：

\[
\boxed{
\begin{array}{c|c|c}
\text{orientation}&\text{new positive }3\bmod4\text{ carrier}&\text{equal-depth ratio}\\ \hline
H_1&\widehat{\mathscr R}_{H1}&\text{square}\\
H_2&\widehat{\mathscr R}_{H2}&\text{non-square}
\end{array}}
\tag{10.1}

加上 universal `H_O` bridge，所有 unequal-depth simple contacts都已有 exact depth reader；剩余 unsaturated kernel只在 equal-depth cancellation，并且现在带有 orientation-specific character。

下一步最有价值的目标不再是给 `H_2` 做新的 singular resultant，而是：

1. 审计 genuine external prime是否能同时进入 `H_1,H_2`；
2. 在 orientation互斥后，用 (9.3) 与 actual/conjugate angle sheet或 `W_q=alpha/omega` natural representative独立计算 companion character；
3. 若得到相反 character，即可关闭对应 equal-depth shell。

---

<a id="source-spontaneous-height-moving-singular-nogo"></a>

> 整合来源：`spontaneous-height-moving-singular-nogo.md`

# A2 moving endpoint-height common channel 的 singular no-go

> **依赖：** `spontaneous-height-parity-ledger.md`、`primitive-reduction.md`。
>
> **严格状态：**`spontaneous-height-parity-ledger.md` 已把 genuine endpoint-external height prime 同时进入 angle/additive common gcd 的 first-layer geometry降成纯 decimal system
> \[
> H_1H_2=0,\qquad J_H=0.
> \]
> 本文对两个 sphere orientations逐一完成 singular bad-reduction audit。结论是：对任意 genuine non-`3` inert external prime，full three-variable system没有 surviving singular Hensel tree。`H_1` 本身在 genuine locus光滑；`H_2` 的 intrinsic singularity只出现在 `x=-2` denominator boundary。若 `J_H` 对 decimal phase出现 repeated root，第一 orientation只有三个 genuine singular primes `102251,630451,136776907`，第二 orientation只有 `8971`；四个有限状态全部在 `p^2` carry compatibility上失败。`p=11` 单独审计后也只有 `x=y=0` boundary。本文不排除 simple moving roots，因此不关闭 height pool或 A2；它删除的是 moving height common channel 的最后一类 singular branching 解释。

---

## 1. normalized moving system

沿用

\[
x:=\frac BN,
\qquad
y:=\frac{10A}{N},
\qquad
\tau:=N^{-1}=10^{-M}.
\]

`spontaneous-height-parity-ledger.md` 的两个 orientation polynomials 为

\[
\boxed{
H_1
=202500x^4+(101x^2+4x+4)y^2,}
\tag{1.1}

\[
\boxed{
\begin{aligned}
H_2={}&
410062500x^6-402975x^4y^2-7290000x^4y\\
&+8100x^3y^2+101x^2y^4+3600x^2y^3\\
&+40500x^2y^2+4xy^4+4y^4.
\end{aligned}}
\tag{1.2}

additive-height carrier `J_H` 除去 decimal unit后为

\[
\boxed{
\begin{aligned}
G_H(x,y,\tau)
={}&100x^2\left[5(y+9)^2-36(y+9)\tau+55\tau^2\right]\\
&-(x+2)^2(2025x^2+y^2).
\end{aligned}}
\tag{1.3}

所以 genuine external common prime必须在某个 orientation上满足

\[
\boxed{H_i=G_H=0\pmod p.}
\tag{1.4}

本文固定

\[
p\equiv3\pmod4,
\qquad p\ne3,5,
\]
并使用 external separation：

\[
\boxed{x\ne0,\quad y\ne0,\quad x+2\ne0\pmod p.}
\tag{1.5}

最后一项就是 `p\nmid Q`；fixed denominator `23` 等非-external channel不属于本文。

---

## 2. full-system singularity 的两种来源

因为

\[
\partial_\tau H_i=0,
\]
若

\[
\partial_\tau G_H\ne0,
\]
则只要 `grad H_i` 非零，两行 Jacobian自动线性独立。

因此 rank drop只能来自：

1. `H_i` 自身 intrinsic singular：
   \[
   H_i=H_{i,x}=H_{i,y}=0;
   \]
2. phase repeated root：
   \[
   G_{H,\tau}=0,
   \]
   且两个 `(x,y)` gradients线性相关。

下面分别审计。

---

# I. intrinsic sphere-orientation singularity

## 3. `H_1` 在 genuine locus 自动光滑

写

\[
C_1(x):=101x^2+4x+4.
\]
则

\[
H_1=202500x^4+C_1y^2,
\]

\[
H_{1,y}=2C_1y.
\]

在 genuine locus中 `p` 为奇数且 `y` 是 unit。若 `H_{1,y}=0`，则

\[
C_1=0.
\]
代回 `H_1=0`：

\[
202500x^4=0.
\]
由于 `p\ne2,3,5` 且 `x` 为 unit，矛盾。因此

\[
\boxed{\nabla H_1\ne0}
\tag{3.1}

对所有 genuine target primes成立。

---

## 4. `H_2` intrinsic singularity 只剩 denominator boundary

消去 `y` 得

\[
\boxed{
\begin{aligned}
\operatorname{Res}_y(H_2,H_{2,y})
={}&c_y\,x^{14}(x+2)^4 C_2(x)A_6(x),
\end{aligned}}
\tag{4.1}

其中 `c_y` 只含 `2,3,5`，

\[
C_2=101x^2+4x+4,
\]

\[
\boxed{
A_6=
64478501x^6+1908012x^5+9602508x^4+106144x^3
+438960x^2+4800x+8000.}
\tag{4.2}

另一方面

\[
\boxed{
\operatorname{Res}_y(H_2,H_{2,x})
=c_x\,x^{16}(x+2)^4A_8(x),}
\tag{4.3}

`c_x` 同样只含 `2,3,5`，且

\[
\boxed{
\begin{aligned}
A_8={}&6512328601x^8+708537220x^7+1501885036x^6
+121752064x^5\\
&+219524016x^4+3371072x^3+8584000x^2+89600x+128000.
\end{aligned}}
\tag{4.4}

非边界 common x-root只能来自 `C_2A_6` 与 `A_8`。两个整数 resultant 分别为

\[
\boxed{
\operatorname{Res}(C_2,A_8)
=2^{24}13^2 101^2\cdot59729\cdot22177889,}
\tag{4.5}

\[
\boxed{
\begin{aligned}
\operatorname{Res}(A_6,A_8)
={}&2^{72}5^9 17^6\cdot31\cdot47^6\cdot101^6\cdot181^2\cdot251\\
&\cdot371069497788281179471251313.
\end{aligned}}
\tag{4.6}

限制到 non-`3` inert prime，只剩

\[
\boxed{31,47,251.}
\tag{4.7}

checker 在这三个有限域上直接计算 polynomial gcd：

- `p=31` 的非边界 resultant gcd只有 `x=8`，但 `H_2,H_{2,x},H_{2,y}` 在该 `x` 下没有共同 `y`；
- `p=47` 的非边界 x-gcd为 `1`；
- `p=251` 的非边界 resultant gcd只有 `x=51`，同样没有共同 `y`。

完整 singular states 中出现的其余点都来自共享显式因子

\[
x+2=0,
\]
即 denominator boundary，违反 (1.5)。因此

\[
\boxed{H_2\text{ 在 genuine external locus也无 intrinsic singular point}.}
\tag{4.8}

---

# II. repeated decimal-phase branch

## 5. `p != 11` 时 repeated `tau` 精确降成同一个 `D_H`

由 (1.3)：

\[
G_{H,\tau}
=100x^2\left[-36(y+9)+110\tau\right].
\]
对 `p\ne11` 且 `x` 为 unit：

\[
\boxed{
G_{H,\tau}=0
\iff
55\tau=18(y+9).}
\tag{5.1}

代入

\[
\tau=\frac{18}{55}(y+9)
\]
后有精确恒等式

\[
\boxed{
G_H=-\frac1{11}D_H(x,y),}
\tag{5.2}

其中

\[
\boxed{
\begin{aligned}
D_H={}&22275x^4+89100x^3+991x^2y^2+17640x^2y\\
&+168480x^2+44xy^2+44y^2.
\end{aligned}}
\tag{5.3}

因为在 repeated root上 `G_{H,\tau}=0`，chain rule给

\[
(G_{H,x},G_{H,y})
=-\frac1{11}(D_{H,x},D_{H,y}).
\]
所以 full rank drop等价于 plane intersection

\[
H_i=D_H=0
\]
本身为 singular intersection。

---

## 6. orientation `H_1`: fixed bad primes

直接消去 `y`：

\[
\boxed{
\operatorname{Res}_y(H_1,D_H)
=164025x^4P_1(x),}
\tag{6.1}

其中

\[
\boxed{
\begin{aligned}
P_1={}&240046103025x^8-431151600x^7+18108996360x^6
-937618080x^5\\
&+354227216x^4+108902528x^3+76745984x^2
+8466432x+2768896.
\end{aligned}}
\tag{6.2}

其判别式为

\[
\boxed{
\begin{aligned}
\operatorname{Disc}(P_1)
={}&2^{120}3^75^{34}7^{28}11^4 13^4 89^2 101^4 367^2\\
&\cdot102251\cdot630451\cdot136776907.
\end{aligned}}
\tag{6.3}

因此 non-`3` inert bad-reduction候选为

\[
\boxed{7,11,367,102251,630451,136776907.}
\tag{6.4}

`7` 没有 full singular state，`367` 没有 `F_p` repeated x-root；`11` 稍后单列。剩下三个 prime各有唯一 genuine finite state：

\[
\boxed{
\begin{array}{c|c|c|c}
p&x_0&y_0&\tau_0\\ \hline
102251&61220&95782&35068\\
630451&340435&610253&474828\\
136776907&4766067&102799536&58512016
\end{array}}
\tag{6.5}

其中 `tau_0=18(y_0+9)/55 mod p`。

---

## 7. `H_1` 三个 singular states 全部没有 `p^2` lift

在标准 representatives上写

\[
x=x_0+pX,\quad y=y_0+pY,\quad\tau=\tau_0+pT_1.
\]

两行 Jacobian模 `p` 线性相关：

\[
\nabla G_H=c_p\nabla H_1.
\]

对应 carry compatibility residual

\[
\boxed{
r_p
:=\frac{G_H(x_0,y_0,\tau_0)}p
-c_p\frac{H_1(x_0,y_0)}p
\pmod p}
\tag{7.1}

必须为 `0` 才能 lift。exact certificate给

\[
\boxed{
\begin{array}{c|c|c}
p&c_p&r_p\\ \hline
102251&51620&99510\\
630451&365778&401091\\
136776907&46110684&133381104
\end{array}}
\tag{7.2}

三者都非零。因此

\[
\boxed{
\text{orientation }H_1\text{ 没有 surviving repeated-phase singular lift}.}
\tag{7.3}

---

## 8. orientation `H_2`: fixed bad primes

消去 `y` 得

\[
\boxed{
\operatorname{Res}_y(H_2,D_H)
=430467210000\,x^8(25x^2+1)^2P_2(x),}
\tag{8.1}

其中

\[
\boxed{
\begin{aligned}
P_2={}&629879737734025x^8+220216678224400x^7
+297840014098760x^6\\
&+74145474010720x^5+52673580295056x^4
+7788392965248x^3\\
&+3650462246144x^2+247566938112x+80965287936.
\end{aligned}}
\tag{8.2}

对 inert `p`，`25x^2+1=0` 没有 `F_p` root，因为这等价于 `-1` 为平方。因此只需看 `P_2`。

其判别式为

\[
\boxed{
\begin{aligned}
\operatorname{Disc}(P_2)
={}&2^{116}3^55^{26}7^{64}11^4 13^4 19^2 101^4
\cdot5827^2\cdot9323^2\\
&\cdot8971\cdot5019481^2\cdot833453052690874208617.
\end{aligned}}
\tag{8.3}

non-`3` inert candidates为

\[
\boxed{7,11,19,5827,8971,9323.}
\tag{8.4}

其中：

- `7,5827,9323` 没有 genuine full singular state；
- `19` 只给 `x=y=0` boundary；
- `11` 单列；
- `8971` 唯一给
  \[
  \boxed{(x_0,y_0,\tau_0)=(2914,6787,4997).}
  \tag{8.5}
  
该点 Jacobian比例与 carry residual为

\[
\boxed{c_{8971}=8281,\qquad r_{8971}=3710\ne0.}
\tag{8.6}

所以它也没有 `8971^2` lift。

因此

\[
\boxed{
\text{orientation }H_2\text{ 没有 surviving repeated-phase singular lift}.}
\tag{8.7}

---

## 9. exceptional `p=11` 的直接 full-system audit

`p=11` 时不能从 `G_{H,\tau}=0` 除以 `55`。因此 checker直接遍历

\[
(x,y,\tau)\in\mathbf F_{11}^3
\]
并同时检查

\[
H_i=G_H=0
\]
及两行 Jacobian rank `<2`。

两个 orientations 的全部 singular states都是

\[
\boxed{x=y=0,\qquad\tau\text{ arbitrary}.}
\tag{9.1}

它们违反 genuine conditions (1.5)。所以 `11` 不产生 external singular state。

---

## 10. final local classification

综合 intrinsic 与 repeated-phase 两部分：

\[
\boxed{
\text{genuine non-`3` inert moving height common channel
没有 surviving singular Hensel tree}.}
\tag{10.1}

所有能够继续到高 prime-power depth的 moving external common state都必须位于

\[
\boxed{H_i=G_H=0}
\]
的 simple branches。

这与 source、pure-`c_Q`、omega-content 等此前审计的模式一致：local singular mechanism 已经不是 A2 剩余 parity 的来源。

---

## 11. proof boundary

本文没有证明 moving height common prime不存在，也没有证明它对

\[
G_{\rm sp}
=\gcd(\widehat{\mathcal O}_{\rm sp},\widehat{\mathcal T}_2)
\]
的 valuation 必为偶数。simple roots仍可沿真实 decimal orbit逐层 Hensel lift。

所以后续不得把本文解释成 height pool closure。真正剩余的是

\[
\boxed{
\text{simple moving decimal orbit}
+\text{natural representative / global parity allocation}.}
\]

若继续 height pool，最有价值的输入应来自 `W_q` 作为 reduced numerator 的真实 decimal representative，或 same-prime Gaussian orientation；再做 singular discriminant/resultant只会重复本文已经完成的局部审计。

---

<a id="source-spontaneous-height-resultant-parity"></a>

> 整合来源：`spontaneous-height-resultant-parity.md`

# A2 `B_W` / reduced-height 的第二个 global parity pair

> **依赖：** `endpoint-lattice.md` (16.427)、`height-cofactor.md`、`source-discriminant.md`、`spontaneous-height-parity-ledger.md`。
>
> **严格状态：**本文把 height-cofactor resultant `B_W` 与 reduced numerator `W_q` 直接视为第二个 global parity pair。`B_W` 是 positive `7 mod 8` integer，而 `W_q≡3Z mod4`。因此在 `Z≡1 mod4` orientation 中，两者都是 `3 mod4`，其 gcd恰为 additive height common part `D_H`; 若 `D_H≡1 mod4`，两个互素 residual quotients都被迫携带 odd inert parity。本文还把 pure-decimal `J_H` 与 `B_W` 放进一个 exact square-coefficient congruence modulo `W_q`，为下一层 cross-companion 分析提供接口。本文不证明这些 residual primes不存在，也不关闭 A2。

---

## 1. height gcd 的三个等价读取器

沿用

\[
\alpha=TK+a_3=\omega W_q,
\qquad
H_0=c_uW_q,
\]

以及

\[
\boxed{
\mathscr B_W
=c_u^2(5K^2-36K+55)+(q5^\lambda K)^2.}
\tag{1.1}
\]

`height-cofactor.md` 已证明

\[
\boxed{
D_H:=\gcd(\widehat{\mathcal T}_2,W_q)
=\gcd(\mathscr B_W,W_q).}
\tag{1.2}
\]

`spontaneous-height-parity-ledger.md` 又给 pure-decimal

\[
\mathcal J_H=B^2(5K^2-36K+55)-Q^2N_0,
\]

\[
\widehat{\mathcal J}_H=\mathcal J_H/2^{2M+2},
\]
以及

\[
\boxed{
D_H=\gcd(\widehat{\mathcal J}_H,W_q).}
\tag{1.3}
\]

所以同一个 height common part有三个完全等价的读取器：

\[
\boxed{
D_H
=\gcd(\widehat T_2,W_q)
=\gcd(\widehat J_H,W_q)
=\gcd(\mathscr B_W,W_q).}
\tag{1.4}
\]

---

## 2. `B_W` 本身是 positive `3 mod 4` carrier

`source-discriminant.md` 已证明

\[
\boxed{\mathscr B_W\equiv7\pmod8.}
\tag{2.1}
\]

正性也直接来自当前 endpoint 的巨大正 `K`：

\[
5K^2-36K+55=(K-5)(5K-11)>0,
\]
且第二项为平方。因此

\[
\boxed{\mathscr B_W>0,\qquad \mathscr B_W\equiv3\pmod4.}
\tag{2.2}
\]

于是 `B_W` 自身强迫一份 odd total inert parity。

---

## 3. `W_q` 的真实 mod-4 orientation

`endpoint-lattice.md` (16.427) 给无条件 identity

\[
\boxed{W_q\equiv3Z\pmod4.}
\tag{3.1}
\]

所以

\[
\boxed{
Z\equiv1\pmod4\Longrightarrow W_q\equiv3\pmod4,}
\tag{3.2a}
\]

\[
\boxed{
Z\equiv3\pmod4\Longrightarrow W_q\equiv1\pmod4.}
\tag{3.2b}
\]

这条 orientation此前主要用于 prime-source 分类；和 (2.2) 合并后，它直接产生一个新的 gcd parity dichotomy。

---

## 4. `Z=1 mod4` 时 `B_W` 与 `W_q` 形成完整 parity pair

定义

\[
\boxed{
B^\circ:=\frac{\mathscr B_W}{D_H},
\qquad
W^\circ:=\frac{W_q}{D_H}.}
\tag{4.1}
\]

由 gcd 定义：

\[
\boxed{\gcd(B^\circ,W^\circ)=1.}
\tag{4.2}
\]

若

\[
Z\equiv1\pmod4,
\]
则由 (2.2)、(3.2a)：

\[
\mathscr B_W\equiv W_q\equiv3\pmod4.
\]
因此

\[
\boxed{
B^\circ\equiv W^\circ
\equiv3D_H^{-1}\pmod4.}
\tag{4.3}
\]

于是得到严格 dichotomy：

\[
\boxed{
\begin{array}{c|c|c}
D_H\bmod4&B^\circ\bmod4&W^\circ\bmod4\\ \hline
1&3&3\\
3&1&1
\end{array}}
\qquad(Z\equiv1\bmod4).
\tag{4.4}
\]

所以当

\[
D_H\equiv1\pmod4
\]
时，`B^circ` 与 `W^circ` 是两个互素 positive `3 mod4` integers：

\[
\boxed{
\text{height common part若不承担 odd inert parity，}
\text{则必须出现两份互不复用的 height residual odd parity。}}
\tag{4.5}
\]

这与 `G_sp` 和 angle/additive companion pair的 parity doubling完全同型，但来源不同：这里一边是 cofactor resultant，一边是真实 reduced numerator。

---

## 5. `Z=3 mod4` orientation 是 parity transfer 而非 doubling

若

\[
Z\equiv3\pmod4,
\]
则

\[
W_q\equiv1\pmod4,
\qquad
\mathscr B_W\equiv3\pmod4.
\]
所以

\[
\boxed{
B^\circ\equiv3D_H^{-1},
\qquad
W^\circ\equiv D_H^{-1}\pmod4.}
\tag{5.1}
\]

即

\[
\boxed{
\begin{array}{c|c|c}
D_H\bmod4&B^\circ\bmod4&W^\circ\bmod4\\ \hline
1&3&1\\
3&1&3
\end{array}}
\qquad(Z\equiv3\bmod4).
\tag{5.2}
\]

这里始终只有 `B_W` 与 `D_H/W^circ` 两边之一承担 residual odd parity；不存在双份复制。因此后续 global ledger必须保留 `Z` orientation，不能把两种情况混为一个无条件 doubling。

---

## 6. `J_H` 与 `B_W` 的 exact square-coefficient bridge modulo height

令

\[
z:=q5^\lambda,
\qquad
D=g2^m5^d,
\qquad
T=10^m,
\]
并使用 canonical height equality

\[
H_0^2-g^2a_3^2=5^\lambda c_Q^2XY,
\qquad
H_0=c_uW_q.
\]

把 `J_H` 除去 primitive 2-scale后直接展开，可得 exact integer identity

\[
\boxed{
\begin{aligned}
5^{2d}\widehat{\mathcal J}_H
&-2^{2m}5^{2d}g^2\mathscr B_W\\
&=q^2W_q\left[
(g^2\omega^2-c_u^2)W_q
-2g^2\omega TK
\right].
\end{aligned}}
\tag{6.1}
\]

左边 `B_W` 的 coefficient

\[
2^{2m}g^2=(2^mg)^2
\]
是完整平方。特别地 modulo `W_q`：

\[
\boxed{
5^{2d}\widehat J_H
\equiv
(2^mg)^2 5^{2d}\mathscr B_W
\pmod{W_q}.}
\tag{6.2}
\]

由于 `gcd(W_q,10g)=1`：

\[
\boxed{
\widehat J_H\equiv(2^mg)^2\mathscr B_W
\pmod{W_q}}
\tag{6.3}
\]
在局部 square-class 意义下完全无损。这重新证明两者与 `W_q` 读取相同 `D_H`，并说明它们在每个 height prime上的 residual unit只差一个显式平方。

这也意味着：继续给 `J_H` 与 `B_W` 各自叠加同一个 Legendre condition不会产生新的 obstruction；真正的新信息只能来自两者在离开 `W_q` 后的 additive difference / natural representative。

---

## 7. global ledger 的更新

在 `Z=1 mod4` orientation 中，现在至少有三种独立的 parity-doubling结构：

1. actual/conjugate angle pair；
2. actual additive / `J_H` pair after removing common height;
3. `B_W/W_q` height-resultant pair (本文)。

它们的共同点是：common gcd若为 `1 mod4`，两个互素 residuals都被迫为 `3 mod4`。

但本文仍不构成 closure。尤其 `B^circ` 与其它 companion residual可能共享同一个 external prime；要继续推进必须研究这种 cross-companion overlap，而不是再证明单个 carrier是 `3 mod4`。

---

<a id="source-spontaneous-height-sign-companion-shadow"></a>

> 整合来源：`spontaneous-height-sign-companion-shadow.md`

# A2 moving height equal-depth 的 same-sign companion shadow

> **依赖：** `spontaneous-height-equal-depth-source-orientation.md`、`spontaneous-sign-companion-parity.md`。
>
> **严格状态：**本文检查同号 companions `O_-`、`Theta_+` 是否能为 moving-height equal-depth shell 提供独立 quadratic character。结论：在 generic noncentral height prime 上，它们与两个 sign-product 的 character 精确合并回既有
> \[
> \chi\!\left((\Theta_-/p^e)/(\mathcal O_+/p^e)\right)=\chi(-\rho).
> \]
> 因此 same-sign companion Legendre calculation 没有新增局部约束。

## 1. companion first layer

固定
\[
p^h\Vert W_q,\qquad e<h,\qquad p\equiv3\pmod4,
\]
并假设
\[
v_p(\mathcal O_+)=v_p(\Theta_-)=e,
\qquad p\nmid K(2K-9)ABQb_3Tc_uz.
\]

由
\[
\mathcal O_+-\mathcal O_-=4A^2Qb_3
\]
与 `p|O_+`：
\[
\boxed{\mathcal O_-\equiv-4A^2Qb_3\pmod p.}
\tag{1.1}
\]

又
\[
\Theta_+-\Theta_-=4B^2(2K-9)a_3,
\]
而 height prime 上 `a_3=-TK mod p`，故
\[
\boxed{\Theta_+\equiv-4TB^2K(2K-9)\pmod p.}
\tag{1.2}
\]

使用 `b_3z=Tc_uQ` 与 `rho=z/c_u`：
\[
\boxed{
\left(\frac{\Theta_+/\mathcal O_-}{p}\right)
=
\left(\frac{K(2K-9)/\rho}{p}\right).}
\tag{1.3}
\]

## 2. sign-product character

height product bridge给
\[
T^2\mathcal H_O\equiv N_0\mathcal O_+\mathcal O_-\pmod{W_q}.
\]
所以在 `e<h`
\[
\frac{\mathcal O_+\mathcal O_-}{p^e}
\equiv
\frac{T^2}{N_0}\frac{\mathcal H_O}{p^e}\pmod p.
\tag{2.1}
\]

另一方面 `alpha=TK+a_3` 有深度至少 `h`，从 additive pair 得
\[
\frac{\Theta_-\Theta_+}{p^e}
\equiv
-4T^2B^2K(2K-9)\frac{\mathcal J_H}{p^e}\pmod p.
\tag{2.2}
\]

height square给 `(N_0/p)=-1`。在 equal-depth extra shell，`J_H/B_W` 只差 square，而 universal norm bridge要求
\[
\left(
\frac{(\mathscr B_W/p^e)/(\mathcal H_O/p^e)}p
\right)=-1.
\]
因此
\[
\boxed{
\left(
\frac{(\Theta_-\Theta_+/p^e)/(\mathcal O_+\mathcal O_-/p^e)}p
\right)
=-\left(\frac{K(2K-9)}p\right).}
\tag{2.3}
\]

## 3. companion calculation is the same law

分解 sign-product ratio：
\[
\frac{\Theta_-\Theta_+}{\mathcal O_+\mathcal O_-}
=
\frac{\Theta_-}{\mathcal O_+}
\frac{\Theta_+}{\mathcal O_-}.
\]
结合 (1.3)、(2.3)：
\[
\boxed{
\left(
\frac{(\Theta_-/p^e)/(\mathcal O_+/p^e)}p
\right)
=-\left(\frac\rho p\right)
=\left(\frac{-\rho}p\right).}
\tag{3.1}
\]

这与 `spontaneous-height-equal-depth-source-orientation.md` 完全相同。

故在 generic noncentral moving-height shell，同号 companion character 只是既有 source-orientation law 的代数投影。继续处理时应转向 cross-sign sphere、`p|(2K-9)` 的显式例外，或 global `W_q=alpha/omega` representative。

---

<a id="source-spontaneous-height-oversaturation-depth-ledger"></a>

> 整合来源：`spontaneous-height-oversaturation-depth-ledger.md`

# A2 height companion oversaturation 的 residual-depth ledger

> **依赖：** `spontaneous-height-content-oversaturation.md`、`spontaneous-height-resultant-parity.md`、`spontaneous-height-companion-cross.md`、`spontaneous-height-parity-ledger.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文是 `spontaneous-height-content-oversaturation.md` 的下一层 depth audit。对已经满足 `p|omega`、`p|W_q` 且 `J_H/B_W` 在完整 height gcd 之后继续共同加深的 genuine non-`3` inert prime，本文证明：`J_H` 本身就是一个恰有 `4M+1` 位的 positive pure-prefix carrier，并完整承担 `p^{h+1}`；更短的 prefix height carrier `H_pref=B^2K^2+Q^2N_0` 只需 `4M+1` 位便承担 `p^{min(e,h+1)}`，在 `e<=h` 时其 p-adic 深度精确等于 `e`。此外利用 `J_H/B_W` 的 exact difference，若 `e!=h`，两 companion 的较浅 oversaturation residual depth 至多为 `min(e,h)`，若两边深度不同则恰等于 `min(e,h)`。因此任意超出这一 cap 的行为只能进入唯一的 equal-depth resonance `e=h`。本文不排除该 resonance，也不关闭 A2。

---

## 1. 记号与 oversaturation 深度

沿用 parent 文件的 genuine non-`3` inert prime `p`。令

\[
 e:=v_p(\omega)\ge1,
 \qquad
 h:=v_p(W_q)\ge1,
\]

并记

\[
 j:=v_p(\widehat{\mathcal J}_H)
   =v_p(\mathcal J_H),
 \qquad
 V:=v_p(\mathscr B_W).
\]

因为 `D_H` 在该 prime 上已经完整吃掉 `W_q` 的 `p^h`，而

\[
p\mid J^\circ,
\qquad
p\mid B^\circ,
\]
所以

\[
\boxed{j\ge h+1,\qquad V\ge h+1.}
\tag{1.1}
\]

定义两个 residual depths

\[
\boxed{
r_J:=j-h\ge1,
\qquad
r_B:=V-h\ge1.}
\tag{1.2}
\]

parent 文件已经证明

\[
\boxed{p\mid\omega,}
\tag{1.3}
\]

并定义 fixed quadratic

\[
\boxed{
\mathcal P_{\omega H}(K)
:=6K^2-36K+55.
}
\tag{1.4}
\]

---

## 2. `J_H` 自身已经给出一个更短的 pure-prefix depth carrier

沿用

\[
B=b_2,
\qquad
Q=B+2N,
\qquad
N=10^M,
\]

\[
N_0=\left(\frac{9B}{2}\right)^2+a_2^2,
\]
以及

\[
\mathcal J_H
=B^2(5K^2-36K+55)-Q^2N_0.
\tag{2.1}
\]

由 (1.1) 直接有

\[
\boxed{p^{h+1}\mid\mathcal J_H.}
\tag{2.2}
\]

这比 parent 文件的 resultant depth

\[
p^{\min(e,h+1)}\mid\mathscr R_{\omega H}^{\rm pref}
\]
在 `e<h+1` 时更强，因为 (2.2) **无条件读取完整 `h+1` depth**。

当前 endpoint box 为

\[
\frac1{10}<x:=\frac BN<\frac2{19},
\qquad
\frac{249}{250}<y:=\frac{10a_2}{N}<1,
\qquad
\tau=N^{-1}<10^{-11},
\]

并令

\[
s:=9+y.
\]
则

\[
\frac{\mathcal J_H}{N^4}
=x^2\left(5s^2-36s\tau+55\tau^2\right)
-(x+2)^2
\left(\frac{2025x^2+y^2}{100}\right).
\tag{2.3}
\]

由

\[
x>\frac1{10},
\quad
s>\frac{2499}{250},
\quad
(x+2)^2\frac{2025x^2+y^2}{100}<\frac{26}{25},
\]
有

\[
\frac{\mathcal J_H}{N^4}
>
\frac1{100}
\left[
5\left(\frac{2499}{250}\right)^2
-\frac{360}{10^{11}}
\right]
-\frac{26}{25}
>rac{79}{20}.
\tag{2.4}
\]

另一方面忽略负项并用 `x<2/19`、`s<10`：

\[
\frac{\mathcal J_H}{N^4}
<
\frac4{361}
\left(500+\frac{55}{10^{22}}\right)
<\frac{111}{20}.
\tag{2.5}
\]

所以

\[
\boxed{
\frac{79}{20}N^4
<\mathcal J_H
<\frac{111}{20}N^4.
}
\tag{2.6}
\]

特别地

\[
\boxed{
\mathcal J_H
\text{ 恰有 }4M+1\text{ 个十进制数字}.}
\tag{2.7}
\]

结合 (2.2)：

\[
\boxed{
p^{h+1}<\frac{111}{20}\,10^{4M}.}
\tag{2.8}
\]

因此 oversaturation 的完整 height depth `h+1` 已经被一个比 `8M+2` 位 resultant 短一半的 pure-prefix natural representative 控制。

---

## 3. `J_H` 的 primitive orientation 实际是 `7 mod 8`

已有

\[
B=2^{M+m+1}b_0,
\qquad
Q=2^{M+1}Q_0,
\]
其中 `b_0,Q_0` 为奇数。

当前 endpoint 还有

\[
\lambda>\frac{3M}{7},
\qquad
m\ge\lambda,
\qquad
M\ge11,
\]
故

\[
\boxed{m\ge5.}
\tag{3.1}
\]

`N_0` 为奇数，并且更精确地

\[
N_0\equiv a_2^2\equiv1\pmod8,
\tag{3.2}
\]
因为 `(9B/2)^2` 含很深的 `2`-power。

把 (2.1) 除以 `2^{2M+2}`：第一项含因子 `2^{2m}`，由 (3.1) 在模 `8` 下消失；第二项给

\[
-Q_0^2N_0\equiv-1\equiv7\pmod8.
\]
所以

\[
\boxed{
v_2(\mathcal J_H)=2M+2,
\qquad
\frac{\mathcal J_H}{2^{2M+2}}
\equiv7\pmod8.}
\tag{3.3}
\]

这强化了旧的 `3 mod 4` orientation；但它仍只是 global parity information，不能单独排除指定的 oversaturation prime。

---

## 4. 更短的 `H_pref` carrier：只有 `4M+1` 位

定义 parent 文件已经使用的

\[
\boxed{
\mathscr H_{\omega H}^{\rm pref}
:=B^2K^2+Q^2N_0.
}
\tag{4.1}
\]

有 exact identity

\[
\boxed{
\mathcal J_H
=B^2\mathcal P_{\omega H}(K)
-\mathscr H_{\omega H}^{\rm pref}.}
\tag{4.2}
\]

parent 文件给

\[
\ell_p:=\min(e,h+1),
\]

\[
p^{\ell_p}\mid\mathcal P_{\omega H}(K).
\tag{4.3}
\]

而 (2.2) 当然也给

\[
p^{\ell_p}\mid\mathcal J_H.
\]
由于 `p\nmid B`，由 (4.2)：

\[
\boxed{
p^{\ell_p}\mid
\mathscr H_{\omega H}^{\rm pref}.}
\tag{4.4}
\]

这条 divisibility 不需要再经过 degree-2 resultant。

写

\[
n_0:=\frac{N_0}{N^2}
=\frac{81}{4}x^2+\frac{y^2}{100}.
\]
则

\[
\frac{\mathscr H_{\omega H}^{\rm pref}}{N^4}
=x^2s^2+(x+2)^2n_0.
\tag{4.5}
\]

利用

\[
 n_0>\frac{53}{250},
 \qquad
 (x+2)^2>\left(\frac{21}{10}\right)^2,
\]
以及 `x>1/10,s>2499/250`：

\[
\frac{\mathscr H_{\omega H}^{\rm pref}}{N^4}
>
\frac1{100}\left(\frac{2499}{250}\right)^2
+\left(\frac{21}{10}\right)^2\frac{53}{250}
>rac{193}{100}.
\tag{4.6}
\]

上界则由

\[
x^2s^2<\frac{400}{361},
\qquad
(x+2)^2n_0<\frac{26}{25}
\]
得到

\[
\frac{\mathscr H_{\omega H}^{\rm pref}}{N^4}
<\frac{400}{361}+\frac{26}{25}
<\frac{43}{20}.
\tag{4.7}
\]

因此

\[
\boxed{
\frac{193}{100}N^4
<\mathscr H_{\omega H}^{\rm pref}
<\frac{43}{20}N^4.}
\tag{4.8}
\]

特别地

\[
\boxed{
\mathscr H_{\omega H}^{\rm pref}
\text{ 也恰有 }4M+1\text{ 个十进制数字}.}
\tag{4.9}
\]

由 (4.4)：

\[
\boxed{
p^{\min(e,h+1)}
<\frac{43}{20}\,10^{4M}.}
\tag{4.10}
\]

这把 parent 文件的

\[
p^{\min(e,h+1)}<39\cdot10^{8M}
\]
提升为真正的 `4M`-scale bound。

---

## 5. `H_pref` 的 primitive orientation 为 `1 mod 8`

`K=10P` 且 `P` 为奇数，所以

\[
v_2(K)=1.
\]

因此 `B^2K^2` 的二进深度为

\[
2M+2m+4,
\]
而 `Q^2N_0` 的二进深度恰为

\[
2M+2.
\]
故

\[
\boxed{
v_2(\mathscr H_{\omega H}^{\rm pref})=2M+2.}
\tag{5.1}
\]

除去该 primitive `2`-scale 后，第一项至少仍含 `2^{2m+2}`，第二项为 `Q_0^2N_0`。所以

\[
\boxed{
\frac{\mathscr H_{\omega H}^{\rm pref}}{2^{2M+2}}
\equiv1\pmod8.}
\tag{5.2}
\]

于是 `J_H/H_pref` 在 primitive orientation 上形成

\[
\boxed{7\pmod8\quad/\quad1\pmod8}
\tag{5.3}
\]
的 pure-prefix pair。

这并没有自动产生矛盾，因为它们可以共享指定的 inert prime后再由其它素数补偿 orientation；真正可用的是下面的 **exact residual-depth law**。

---

## 6. shallow content 中 `H_pref` 精确读取全部 `omega` depth

parent 文件的 exact decomposition 为

\[
\boxed{
\mathscr B_W
=c_u^2\mathcal P_{\omega H}(K)
+g\omega(g\omega-2c_u)K^2.}
\tag{6.1}
\]

第二项在当前 prime 上的赋值恰为 `e`。

若

\[
e\le h,
\]
则 `V>=h+1>e`。为了使 (6.1) 的和达到 `V`，必有

\[
\boxed{v_p(\mathcal P_{\omega H}(K))=e.}
\tag{6.2}
\]

另一方面 `j>=h+1>e`。由 (4.2) 且 `p\nmid B`：

\[
\boxed{
v_p(\mathscr H_{\omega H}^{\rm pref})=e
\qquad(e\le h).}
\tag{6.3}
\]

所以 shallow-content 分支中，`omega` 的**完整** p-adic depth 已经由一个恰有 `4M+1` 位、primitive `1 mod 8` 的 pure-prefix integer 精确读取。

---

## 7. exact `J_H/B_W` difference 把 oversaturation residual depth 封顶

`spontaneous-height-resultant-parity.md` 给

\[
5^{2d}\widehat{\mathcal J}_H
-2^{2m}5^{2d}g^2\mathscr B_W
=q^2W_q\,\mathscr C_{JB},
\tag{7.1}
\]
其中

\[
\mathscr C_{JB}
=(g^2\omega^2-c_u^2)W_q
-2g^2\omega TK.
\]

`spontaneous-height-companion-cross.md` 又有

\[
\boxed{
q\mathscr C_{JB}
=-zL_{JB},
}
\tag{7.2}
\]
其中

\[
L_{JB}=DzK+fN
=2Dg\omega K-fqW_q.
\tag{7.3}
\]

把 (7.2) 代入 (7.1)：

\[
\boxed{
5^{2d}
\left(
\widehat{\mathcal J}_H-(2^mg)^2\mathscr B_W
\right)
=-qzW_qL_{JB}.}
\tag{7.4}
\]

当前 prime 满足

\[
p\nmid5qz(2^mg),
\]
所以

\[
\boxed{
v_p\!\left(
\widehat{\mathcal J}_H-(2^mg)^2\mathscr B_W
\right)
=h+v_p(L_{JB}).}
\tag{7.5}
\]

而 (7.3) 的两个 coefficient

\[
2DgK,
\qquad fq
\]
都是 p-adic units。因此如果

\[
e\ne h,
\]
两项赋值不同，不可能首层抵消，于是

\[
\boxed{v_p(L_{JB})=\min(e,h).}
\tag{7.6}
\]

合并：

\[
\boxed{
v_p\!\left(
\widehat{\mathcal J}_H-(2^mg)^2\mathscr B_W
\right)
=h+\min(e,h)
\qquad(e\ne h).}
\tag{7.7}
\]

---

## 8. unequal content/height depth 时，较浅 residual 被 `min(e,h)` 精确控制

回忆

\[
j=v_p(\widehat{\mathcal J}_H),
\qquad
V=v_p(\mathscr B_W),
\]
且 `(2^mg)^2` 为 unit。

若

\[
j\ne V,
\]
则两个 summand 赋值不同，因此

\[
v_p\!\left(
\widehat{\mathcal J}_H-(2^mg)^2\mathscr B_W
\right)
=\min(j,V).
\]
与 (7.7) 比较：

\[
\boxed{
\min(j,V)=h+\min(e,h)
\qquad(e\ne h,\ j\ne V).}
\tag{8.1}
\]

也就是 residual depths 满足

\[
\boxed{
\min(r_J,r_B)=\min(e,h)
\qquad(e\ne h,\ r_J\ne r_B).}
\tag{8.2}
\]

若 `j=V`，左边 difference 的赋值至少为 `j`。结合 (7.7) 立刻得到

\[
\boxed{j=V\le h+\min(e,h).}
\tag{8.3}
\]

所以无论两边是否等深，都有统一 cap：

\[
\boxed{
1\le\min(r_J,r_B)\le\min(e,h)
\qquad(e\ne h).}
\tag{8.4}
\]

因此在 unequal content/height depth 上，companion oversaturation 的较浅额外深度永远不能超过 `min(e,h)`；若两 companion 深度本身不同，这个 cap 还是精确等号。

---

## 9. 唯一未被该 cap 控制的机制是 `e=h` equal-depth resonance

现在令

\[
e=h.
\]
写

\[
\omega=p^h\omega_0,
\qquad
W_q=p^hW_0,
\qquad
p\nmid\omega_0W_0.
\]

由 (7.3)：

\[
L_{JB}
=p^h
\left(
2DgK\omega_0-fqW_0
\right).
\tag{9.1}
\]

定义唯一的 resonance depth

\[
\boxed{
\rho_p
:=v_p\!\left(
2DgK\omega_0-fqW_0
\right)\ge0.}
\tag{9.2}
\]

于是

\[
\boxed{v_p(L_{JB})=h+\rho_p,}
\tag{9.3}
\]

并由 (7.5)：

\[
\boxed{
v_p\!\left(
\widehat{\mathcal J}_H-(2^mg)^2\mathscr B_W
\right)
=2h+\rho_p.}
\tag{9.4}
\]

所以所有可能突破 §8 cap 的行为都已经严格集中到一个 unit synchronization：

\[
\boxed{
2DgK\omega_0
\equiv fqW_0
\pmod{p^r}.}
\tag{9.5}
\]

换言之，height-supported omega oversaturation 现在分成：

\[
\boxed{
\begin{array}{ll}
e\ne h:&
\min(r_J,r_B)\le\min(e,h),\\[1mm]
e=h:&
\text{只剩单一 equal-depth unit resonance }\rho_p.
\end{array}}
\tag{9.6}
\]

这比“simple moving root”更窄：真正无界的 deep synchronization 已经只剩 codimension-one 的 equal-depth resonance。

---

## 10. 当前统一 depth/height ledger

综合 parent 文件和本文：

\[
\boxed{
\begin{gathered}
p\equiv7,11\pmod{24},\\
e=v_p(\omega)\ge1,
\qquad
h=v_p(W_q)\ge1,\\
p^{h+1}\mid\mathcal J_H,
\qquad
\frac{79}{20}10^{4M}<\mathcal J_H<\frac{111}{20}10^{4M},\\
p^{\min(e,h+1)}\mid\mathscr H_{\omega H}^{\rm pref},
\qquad
\frac{193}{100}10^{4M}
<\mathscr H_{\omega H}^{\rm pref}
<\frac{43}{20}10^{4M},\\
\frac{\mathcal J_H}{2^{2M+2}}\equiv7\pmod8,
\qquad
\frac{\mathscr H_{\omega H}^{\rm pref}}{2^{2M+2}}\equiv1\pmod8,\\
e\le h
\Longrightarrow
v_p(\mathscr H_{\omega H}^{\rm pref})=e,\\
e\ne h
\Longrightarrow
1\le\min(r_J,r_B)\le\min(e,h).
\end{gathered}}
\tag{10.1}
\]

其中若 `e!=h` 且 `r_J!=r_B`，最后一个不等式强化为等式。

所以后续再推进时不应继续研究 generic `e!=h` 的无界 oversaturation tree；它已经有显式 residual cap。真正剩余的目标是：

\[
\boxed{
 e=h,
 \qquad
 2DgK\omega_0-fqW_0
 \text{ 的 unit resonance}.}
\tag{10.2}
\]

需要把该 unit congruence再投影到 decimal determinant、`H_pref/J_H` natural representatives 或现有 source slot 上，才能继续逼近 closure。

---

<a id="source-spontaneous-height-parity-ledger"></a>

> 整合来源：`spontaneous-height-parity-ledger.md`

# A2 spontaneous/additive height parity ledger

> **依赖：** `primitive-reduction.md`、`height-cofactor.md`、`spontaneous-angle-parity.md`、`spontaneous-prefix-eliminant.md`、`decimal-prefix-bridge.md`。
>
> **严格状态：**本文把 reduced numerator `W_q` 与 angle/additive 两个 primitive `3 mod 4` carrier 的 height-supported 部分改写为纯 decimal integers。additive-height 由一个新的 positive `3 mod 4` integer `J_H` 精确读取；angle-height 则由 actual/conjugate 两个 positive `3 mod 4` angle sheets 的乘积读取，并产生一个 positive `1 mod 8` height norm `H_O`。对 endpoint-external height prime，actual 与 conjugate sheet互斥，且 `H_O` 与命中的 angle sheet在 `v_p(W_q)` 深度内具有相同截断赋值。本文不证明所有 additive external odd prime 必进入 `W_q`，也不宣称 A2 全局关闭。

---

## 1. 记号

固定 reflection endpoint：

\[
N=10^M,
\quad T=10^m,
\quad A=a_2,
\quad B=b_2,
\]

\[
Q=B+2N,
\qquad
K=9N+10A,
\]

\[
N_0=\left(\frac{9B}{2}\right)^2+A^2.
\tag{1.1}
\]

angle pure-prefix integer为

\[
\boxed{
\mathcal U_\Omega
=(45B^2-2AN)^2-A^2B(99B-4N).
}
\tag{1.2}
\]

原 angle raw carrier记作

\[
\boxed{
\mathcal O_+
:=T\mathcal U_\Omega+2A^2Qb_3.
}
\tag{1.3}
\]

已有

\[
\mathcal O_+
=2^{2M+m+2}\widehat{\mathcal O}_{\rm sp},
\qquad
\widehat{\mathcal O}_{\rm sp}>0,
\qquad
\widehat{\mathcal O}_{\rm sp}\equiv3\pmod4.
\tag{1.4}
\]

height/reduced numerator为

\[
\boxed{
\alpha=TK+a_3=\omega W_q,
\qquad
H_0=c_uW_q.
}
\tag{1.5}

---

## 2. additive-height 的 pure-decimal bridge

定义

\[
\boxed{
\mathcal J_H
:=B^2(5K^2-36K+55)-Q^2N_0.
}
\tag{2.1}
\]

由

\[
\Theta_{\rm dec}
=T\bigl[B^2(K^2-18K+55)-Q^2N_0\bigr]
-2B^2(2K-9)a_3
\]
和

\[
a_3=\omega W_q-TK
\]
直接得到

\[
\boxed{
\Theta_{\rm dec}
=T\mathcal J_H
-2B^2(2K-9)\omega W_q.
}
\tag{2.2}
\]

`W_q` 为 odd 且 `gcd(T,W_q)=1`，故

\[
\boxed{
\gcd(\Theta_{\rm dec},W_q)
=
\gcd(\mathcal J_H,W_q).
}
\tag{2.3}
\]

又

\[
\Theta_{\rm dec}=2^{2M+m+2}\widehat{\mathcal T}_2,
\]
所以

\[
\boxed{
\gcd(\widehat{\mathcal T}_2,W_q)
=
\gcd(\mathcal J_H,W_q).
}
\tag{2.4}
\]

逐 prime-power 地，若

\[
p^h\Vert W_q,
\]
则

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),h\}
=
\min\{v_p(\mathcal J_H),h\}.
}
\tag{2.5}
\]

这把 additive-height depth 从 source quantity `B_W` 再降成一个完全 source-free 的 decimal integer。

---

## 3. `J_H` 是 positive primitive `3 mod 4` integer

reflection deep-even 中

\[
B=2^{M+m+1}b_0,
\qquad
Q=2^{M+1}Q_0,
\]
其中 `b_0,Q_0` 为奇数，且 `A,N_0` 均为奇数。

`5K^2-36K+55` 为奇数。因此 `J_H` 两项的 `2`-进深度分别是

\[
2M+2m+2,
\qquad
2M+2.
\]

由于 `m>=1`：

\[
\boxed{v_2(\mathcal J_H)=2M+2.}
\tag{3.1}
\]

令

\[
\widehat{\mathcal J}_H
:=\frac{\mathcal J_H}{2^{2M+2}}.
\]
第一项被 `4` 整除，而第二项模 `4` 为 `-Q_0^2N_0=-1`，故

\[
\boxed{
\widehat{\mathcal J}_H\equiv3\pmod4.
}
\tag{3.2}
\]

它还严格为正。令

\[
x=B/N,
\quad y=10A/N,
\quad \tau=N^{-1},
\quad s=9+y.
\]
则

\[
\frac{100\mathcal J_H}{N^4}
=
100x^2(5s^2-36s\tau+55\tau^2)
-(x+2)^2(2025x^2+y^2).
\tag{3.3}
\]

endpoint box 给

\[
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1,
\qquad
0<\tau<10^{-11}.
\]

第一项统一 `>499`；第二项统一 `<104`。因此

\[
\boxed{
\mathcal J_H>0,
\qquad
\widehat{\mathcal J}_H>0,
\qquad
\widehat{\mathcal J}_H\equiv3\pmod4.
}
\tag{3.4}

---

## 4. actual/conjugate angle sheets

定义

\[
\boxed{
\mathcal O_\pm
:=T\mathcal U_\Omega\pm2A^2Qb_3.
}
\tag{4.1}
\]

所以

\[
\boxed{
\mathcal O_+-\mathcal O_-=4A^2Qb_3.
}
\tag{4.2}
\]

`spontaneous-angle-parity.md` 已证明

\[
\frac{T\mathcal U_\Omega}{2^{2M+m+2}}
\equiv1\pmod4,
\]
而

\[
\frac{2A^2Qb_3}{2^{2M+m+2}}
\equiv2\pmod4.
\]
由于 `+2` 与 `-2` 模 `4` 都等于 `2`：

\[
\boxed{
 v_2(\mathcal O_+)
=v_2(\mathcal O_-)
=2M+m+2,
}
\tag{4.3}
\]

\[
\boxed{
\widehat{\mathcal O}_+
\equiv
\widehat{\mathcal O}_-
\equiv3\pmod4.
}
\tag{4.4}
\]

两者在真实 endpoint 上都为正。事实上

\[
\mathcal U_\Omega=\frac{N^4}{100}A_{\rm sp},
\qquad
\bar w=\frac{b_3}{TN},
\]
给

\[
\boxed{
\mathcal O_\pm
=\frac{TN^4}{100}
\left(A_{\rm sp}\pm2y^2(x+2)\bar w\right).
}
\tag{4.5}
\]

已有 `A_sp>5`，而 `M>=11` 与 `b_3/T<843/1000` 给 `bar w<10^{-11}`，故两个括号都严格为正。

因此 actual 与 conjugate angle sheet **各自**都是 positive primitive `3 mod 4` carrier。

---

## 5. height norm 与两个 angle sheets 的 exact product bridge

定义

\[
\boxed{
\mathcal H_O
:=N_0\mathcal U_\Omega^2
+4A^4B^2Q^2K^2.
}
\tag{5.1}
\]

由

\[
\mathcal O_+\mathcal O_-
=T^2\mathcal U_\Omega^2-4A^4Q^2b_3^2
\]
有

\[
T^2\mathcal H_O-N_0\mathcal O_+\mathcal O_-
=
4A^4Q^2\left(b_3^2N_0+B^2T^2K^2\right).
\tag{5.2}
\]

使用

\[
TK=\omega W_q-a_3
\]
及 exact height square

\[
\boxed{
 b_3^2N_0+B^2a_3^2
=\left(\frac{BH_0}{g}\right)^2
}
\tag{5.3}
\]
和 `H_0=c_uW_q`，得到

\[
\boxed{
\begin{aligned}
T^2\mathcal H_O
={}&N_0\mathcal O_+\mathcal O_-\\
&+4A^4Q^2W_q
\left[
W_q\left(\left(\frac{Bc_u}{g}\right)^2+B^2\omega^2\right)
-2B^2\omega a_3
\right].
\end{aligned}}
\tag{5.4}
\]

因此

\[
\boxed{
T^2\mathcal H_O
\equiv
N_0\mathcal O_+\mathcal O_-
\pmod{W_q}.
}
\tag{5.5}
\]

这是 height-supported angle parity 的核心 product bridge。

---

## 6. endpoint-external height prime 上两张 sheet互斥

固定 non-`3` inert endpoint-external height prime

\[
p^h\Vert W_q,
\qquad
p\nmid qf.
\]

height 本原性与 angle-content 分离给

\[
p\nmid10AQb_3N_0.
\tag{6.1}
\]

由 (4.2)，这种 prime 不可能同时整除 `O_+` 与 `O_-`。

因此若 `p|O_+`，则 `O_-` 是单位，结合 (5.5)：

\[
\boxed{
\min\{v_p(\mathcal H_O),h\}
=
\min\{v_p(\mathcal O_+),h\}.
}
\tag{6.2+}
\]

若 `p|O_-`，同理

\[
\boxed{
\min\{v_p(\mathcal H_O),h\}
=
\min\{v_p(\mathcal O_-),h\}.
}
\tag{6.2-}
\]

q-side fixed `23` 允许 `Q=0 mod23`，因此不被本节偷偷包含；它已经在 `fixed-denominator-height-angle.md` 中单列。

---

## 7. `H_O` 分裂成两个 pure-prefix sphere orientations

定义

\[
\boxed{
\mathcal H_1
=2025B^4+101A^2B^2+4A^2BN+4A^2N^2,
}
\tag{7.1}
\]

\[
\boxed{
\begin{aligned}
\mathcal H_2={}&
404A^4B^2+16A^4BN+16A^4N^2
+1440A^3B^2N\\
&-16119A^2B^4+324A^2B^3N
+1620A^2B^2N^2\\
&-29160AB^4N+164025B^6.
\end{aligned}}
\tag{7.2}
\]

直接展开：

\[
\boxed{
\mathcal H_1\mathcal H_2=4\mathcal H_O.
}
\tag{7.3}
\]

normalized factors为

\[
H_1(x,y)
=202500x^4+101x^2y^2+4xy^2+4y^2,
\tag{7.4}
\]

\[
\begin{aligned}
H_2(x,y)={}&
410062500x^6-402975x^4y^2-7290000x^4y\\
&+8100x^3y^2+101x^2y^4+3600x^2y^3\\
&+40500x^2y^2+4xy^4+4y^4.
\end{aligned}
\tag{7.5}
\]

当 angle condition固定 third denominator，并令 height root

\[
\bar\zeta=-s,
\qquad s=9+y,
\]
exact sphere remainder精确为

\[
\boxed{
\mathscr S\big|_{\Omega,\bar\zeta=-s}
=-\frac{A_-^2H_1H_2}{1600y^8(x+2)^4}.
}
\tag{7.6}
\]

所以在 genuine `A_-xy(x+2) != 0` channel：

\[
\boxed{
\text{angle}\cap\text{height}
\Longrightarrow
H_1H_2=0.
}
\tag{7.7}

它们就是 sphere 两个 rational orientations撞上 height root `bar zeta=-s` 的两张 pure-prefix sheet。

---

## 8. orientation integers 的 `2`-进方向

由

\[
B=2^{M+m+1}b_0,
\qquad
N=2^M5^M,
\qquad
A\text{ odd},
\]
在 `H_1` 中唯一最浅项为 `4A^2N^2`：

\[
\boxed{
v_2(\mathcal H_1)=2M+2,
\qquad
\frac{\mathcal H_1}{2^{2M+2}}\equiv1\pmod4.
}
\tag{8.1}
\]

在 `H_2` 中唯一最浅项为 `16A^4N^2`：

\[
\boxed{
v_2(\mathcal H_2)=2M+4,
\qquad
\frac{\mathcal H_2}{2^{2M+4}}\equiv1\pmod4.
}
\tag{8.2}

由 (7.3)：

\[
\boxed{v_2(\mathcal H_O)=4M+4.}
\tag{8.3}
\]

而 (5.1) 中第一项在该深度唯一最浅，且 `N_0` 与 `U_Omega/2^{2M+2}` 都是 `1 mod8` square class。因此

\[
\boxed{
\widehat{\mathcal H}_O
:=\frac{\mathcal H_O}{2^{4M+4}}
>0,
\qquad
\widehat{\mathcal H}_O\equiv1\pmod8.
}
\tag{8.4}

`H_O>0` 与 `H_1>0` 再由 (7.3) 给 `H_2>0`。

---

## 9. height parity ledger

当前 height-supported prime flow 已可写成

\[
\boxed{
\begin{array}{c|c|c}
\text{channel}&\text{pure decimal carrier}&\text{primitive orientation}\\ \hline
\text{additive}\cap W_q&\widehat{\mathcal J}_H&3\pmod4\\
\text{actual angle}&\widehat{\mathcal O}_+&3\pmod4\\
\text{conjugate angle}&\widehat{\mathcal O}_-&3\pmod4\\
\text{angle product over height}&\widehat{\mathcal H}_O&1\pmod8.
\end{array}}
\tag{9.1}

并有

\[
\boxed{
\gcd(\widehat{\mathcal T}_2,W_q)
=
\gcd(\widehat{\mathcal J}_H,W_q).
}
\tag{9.2}

对 endpoint-external angle-height prime，对应 sheet还有

\[
\boxed{
\min(v_p(\widehat{\mathcal O}_\pm),v_p(W_q))
=
\min(v_p(\widehat{\mathcal H}_O),v_p(W_q)).
}
\tag{9.3}

因此若同一个 endpoint-external inert prime同时进入

\[
W_q,
\quad
\widehat{\mathcal O}_{\rm sp},
\quad
\widehat{\mathcal T}_2,
\]
其 first-layer common geometry完全由 pure decimal system

\[
\boxed{
H_1H_2=0,
\qquad
\mathcal J_H=0
}
\tag{9.4}
\]
读取。

---

## 10. 当前边界

本文没有证明

\[
G_{\rm sp}
=\gcd(\widehat{\mathcal O}_{\rm sp},\widehat{\mathcal T}_2)
\equiv3\pmod4.
\]

但 height pool 已经不再需要 source ratio、third-block Hensel 或额外 Gaussian character：

- saturated height corrections只剩 fixed `7,23,43`，见 `fixed-denominator-height-angle.md`；
- moving endpoint-external angle-height由 `H_1,H_2` 两张互斥 sheet控制；
- additive-height由 positive `3 mod4` carrier `J_H` 控制。

下一步最值得做的是：

1. 研究 moving system `H_1H_2=J_H=0` 的 prime-source / decimal-orbit；
2. 或证明 additive external odd carrier必须进入 `W_q`，从而把 additive residual parity全部拉进本文 ledger；
3. 利用 actual/conjugate `O_+,O_-` 在 external `W_q` 上互斥，进一步压缩 `G_sp=1 mod4` 所要求的两份独立 residual parity。

在此之前 A2 仍为 open。

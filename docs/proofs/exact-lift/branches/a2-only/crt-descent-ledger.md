# A2-only Crt Descent Ledger

> 本文件是细粒度研究记录的机械归并账本。各来源的标题、正文和证明状态原样保留；账本中的局部闭合、有限证书或降级路线均不表示该分支或主不存在性命题已经关闭。

## 来源索引

- [`spontaneous-crt-descendant-balance-coprimality.md`](#source-spontaneous-crt-descendant-balance-coprimality)
- [`spontaneous-crt-descendant-balance-gcd-ladder.md`](#source-spontaneous-crt-descendant-balance-gcd-ladder)
- [`spontaneous-crt-descendant-balance-tail.md`](#source-spontaneous-crt-descendant-balance-tail)
- [`spontaneous-crt-descendant-common-parity.md`](#source-spontaneous-crt-descendant-common-parity)
- [`spontaneous-crt-descendant-companion-separation.md`](#source-spontaneous-crt-descendant-companion-separation)
- [`spontaneous-crt-descendant-linear-depth-reader.md`](#source-spontaneous-crt-descendant-linear-depth-reader)
- [`spontaneous-crt-descendant-projective-depth-reader.md`](#source-spontaneous-crt-descendant-projective-depth-reader)
- [`spontaneous-crt-descendant-projective-integer.md`](#source-spontaneous-crt-descendant-projective-integer)
- [`spontaneous-crt-descendant-quartic-tail-hierarchy.md`](#source-spontaneous-crt-descendant-quartic-tail-hierarchy)
- [`spontaneous-crt-descendant-quotient-gate.md`](#source-spontaneous-crt-descendant-quotient-gate)
- [`spontaneous-crt-descendant-second-order-balance.md`](#source-spontaneous-crt-descendant-second-order-balance)
- [`spontaneous-crt-descendant-second-order-gcd-ladder.md`](#source-spontaneous-crt-descendant-second-order-gcd-ladder)
- [`spontaneous-crt-descendant-second-order-tail.md`](#source-spontaneous-crt-descendant-second-order-tail)
- [`spontaneous-crt-descendant-terminal-character.md`](#source-spontaneous-crt-descendant-terminal-character)
- [`spontaneous-crt-descendant-third-order-balance.md`](#source-spontaneous-crt-descendant-third-order-balance)
- [`spontaneous-crt-descendant-third-order-parity-spill.md`](#source-spontaneous-crt-descendant-third-order-parity-spill)
- [`spontaneous-crt-descendant-transport-resonance.md`](#source-spontaneous-crt-descendant-transport-resonance)
- [`spontaneous-crt-descendant-unequal-parent-depth.md`](#source-spontaneous-crt-descendant-unequal-parent-depth)
- [`spontaneous-crt-descended-quotient-orientation.md`](#source-spontaneous-crt-descended-quotient-orientation)
- [`spontaneous-crt-descent-overlap-nogo.md`](#source-spontaneous-crt-descent-overlap-nogo)
- [`spontaneous-crt-dual-gap-mobius.md`](#source-spontaneous-crt-dual-gap-mobius)
- [`spontaneous-crt-dual-gap-remainder.md`](#source-spontaneous-crt-dual-gap-remainder)
- [`spontaneous-crt-external-center-fixed139-463.md`](#source-spontaneous-crt-external-center-fixed139-463)
- [`spontaneous-crt-extra-d-z-reader.md`](#source-spontaneous-crt-extra-d-z-reader)
- [`spontaneous-crt-f-descent-separation.md`](#source-spontaneous-crt-f-descent-separation)
- [`spontaneous-crt-f1270-source-audit.md`](#source-spontaneous-crt-f1270-source-audit)
- [`spontaneous-crt-floorfree-full2-square.md`](#source-spontaneous-crt-floorfree-full2-square)
- [`spontaneous-crt-floorfree-modulus-overlap.md`](#source-spontaneous-crt-floorfree-modulus-overlap)
- [`spontaneous-crt-floorfree-odd3-unit.md`](#source-spontaneous-crt-floorfree-odd3-unit)
- [`spontaneous-crt-floorfree-parity.md`](#source-spontaneous-crt-floorfree-parity)
- [`spontaneous-crt-gap-full5-residue.md`](#source-spontaneous-crt-gap-full5-residue)
- [`spontaneous-crt-gaussian-floorfree-carrier.md`](#source-spontaneous-crt-gaussian-floorfree-carrier)
- [`spontaneous-crt-gaussian-slot-orientation.md`](#source-spontaneous-crt-gaussian-slot-orientation)
- [`spontaneous-crt-height-descent-overlap.md`](#source-spontaneous-crt-height-descent-overlap)
- [`spontaneous-crt-height-primitive-remainder.md`](#source-spontaneous-crt-height-primitive-remainder)
- [`spontaneous-crt-height-remainder-descent.md`](#source-spontaneous-crt-height-remainder-descent)
- [`spontaneous-crt-hensel-sign-bridge.md`](#source-spontaneous-crt-hensel-sign-bridge)
- [`spontaneous-crt-l9-singular-audit.md`](#source-spontaneous-crt-l9-singular-audit)
- [`spontaneous-crt-omega-content-descent.md`](#source-spontaneous-crt-omega-content-descent)
- [`spontaneous-crt-omega-content-fixed7.md`](#source-spontaneous-crt-omega-content-fixed7)
- [`spontaneous-crt-pure-branch-defect.md`](#source-spontaneous-crt-pure-branch-defect)
- [`spontaneous-crt-pure-coefficient-singular.md`](#source-spontaneous-crt-pure-coefficient-singular)
- [`spontaneous-crt-pure-h24-parity.md`](#source-spontaneous-crt-pure-h24-parity)
- [`spontaneous-crt-pure-h24-projective.md`](#source-spontaneous-crt-pure-h24-projective)
- [`spontaneous-crt-pure-h4-parity.md`](#source-spontaneous-crt-pure-h4-parity)
- [`spontaneous-crt-pure-h4-prefix.md`](#source-spontaneous-crt-pure-h4-prefix)
- [`spontaneous-crt-pure-h4-projective-center.md`](#source-spontaneous-crt-pure-h4-projective-center)
- [`spontaneous-crt-pure-h4-short-carrier.md`](#source-spontaneous-crt-pure-h4-short-carrier)
- [`spontaneous-crt-pure-prefix-elimination.md`](#source-spontaneous-crt-pure-prefix-elimination)
- [`spontaneous-crt-pure-projective-carrier.md`](#source-spontaneous-crt-pure-projective-carrier)
- [`spontaneous-crt-q-descent-separation.md`](#source-spontaneous-crt-q-descent-separation)
- [`spontaneous-crt-quotient-endpoint-parameterization.md`](#source-spontaneous-crt-quotient-endpoint-parameterization)
- [`spontaneous-crt-quotient-source-scale.md`](#source-spontaneous-crt-quotient-source-scale)
- [`spontaneous-crt-source-descent-depth.md`](#source-spontaneous-crt-source-descent-depth)
- [`spontaneous-crt-source-descent-overlap.md`](#source-spontaneous-crt-source-descent-overlap)
- [`spontaneous-crt-target-descent-depth-squeeze.md`](#source-spontaneous-crt-target-descent-depth-squeeze)
- [`spontaneous-crt-target-descent-fixed-h1-third.md`](#source-spontaneous-crt-target-descent-fixed-h1-third)
- [`spontaneous-crt-target-descent-fixed-h1.md`](#source-spontaneous-crt-target-descent-fixed-h1)
- [`spontaneous-crt-target-descent-global-gcd.md`](#source-spontaneous-crt-target-descent-global-gcd)
- [`spontaneous-crt-target-descent-overlap.md`](#source-spontaneous-crt-target-descent-overlap)
- [`spontaneous-crt-universal-descendant-cubic.md`](#source-spontaneous-crt-universal-descendant-cubic)

<a id="source-spontaneous-crt-descendant-balance-coprimality"></a>

> 整合来源：`spontaneous-crt-descendant-balance-coprimality.md`

# A2 parent-balance tail 的 coprime coordinates、`1/23` gap 与 cross-gate reuse

> **依赖：** `spontaneous-crt-descendant-balance-tail.md`、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descended-quotient-orientation.md`。
>
> **严格状态：**canonical balance tail使用 parent summands `X=5^lambda Rstar_63`、`Y=g2^m Dhat_63`。本文证明它们的完整 gcd恰为 `G_Delta`：`Rstar` 已与 `10g` 互素，而 `Dhat` 模5是显式 unit。故除去 common baseline后得到互素正整数 coordinates `Xbar,Ybar`。old short-remainder height drop立即给 `0<Xbar/Ybar<1/23`，与 recycling geometric ratio `<-1` 形成超过1的 real gap。balance tail进一步写成 `81 Xbar A_< + 2 Ybar A_>` 的正两项和；互素性给 exact cross-gcd identities，说明 tail prime若回流到某个 parent residual coordinate，必须命中另一侧 fixed gate。本文仍不排除完全 external tail prime或 p-adic balance wrapping，因此不关闭 A2。

---

## 1. `Dhat_63` is a `5`-adic unit

已有

\[
\widehat{\mathscr D}_{63}=c_u^2\mathscr F_{63},
\]

\[
\mathscr F_{63}
=(2K-9)B_\Delta-rac{63}{16}gTK^2,
\]

\[
B_\Delta=g((2K-9)T-a_3)-H_0.
\]

当前

\[
K\equiv0\pmod5,
\qquad T\equiv0\pmod5,
\]
所以

\[
2K-9\equiv1\pmod5,
\]
且 `F_63` 的第二项模5消失。

source relation

\[
H_0=g(3T+a_3)-5^\lambda C
\]
给

\[
H_0\equiv ga_3\pmod5.
\]

因此

\[
B_\Delta
\equiv-ga_3-H_0
\equiv-2ga_3\pmod5,
\]
从而

\[
\boxed{
\widehat{\mathscr D}_{63}
\equiv-2c_u^2ga_3\not\equiv0\pmod5.}
\tag{1.1}

这里 `5∤c_ug` 由 source/mixed coprimality，`5∤a_3` 由 `5|b_3` 与 `(a_3,b_3)=1`。

所以

\[
\boxed{\gcd(\widehat D_{63},5)=1.}
\tag{1.2}

---

## 2. the full parent gcd is exactly `G_Delta`

定义

\[
X=5^\lambda Rstar,
\qquad
Y=g2^mDhat.
\]

已有

\[
\gcd(Rstar,10g)=1,
\]
所以

\[
\gcd(Rstar,g2^m)=1.
\]

由 (1.2)：

\[
\gcd(Dhat,5^\lambda)=1.
\]

同时 source coprimality给 `gcd(5,g)=1`。因此任意 common prime of `X,Y` 必同时来自 `Rstar,Dhat`；反向显然成立。于是

\[
\boxed{
\gcd(X,Y)
=\gcd(Rstar,Dhat)
=G_\Delta.}
\tag{2.1}

定义 reduced parent coordinates

\[
\boxed{
\bar X:=X/G_\Delta,
\qquad
\bar Y:=Y/G_\Delta.}
\tag{2.2}

则

\[
\boxed{
\bar X,\bar Y\in\mathbf Z_{>0},
\qquad
\gcd(\bar X,\bar Y)=1.}
\tag{2.3}

`Xbar` 为 odd，而 `Ybar` 保留 parent 2-power scale。

---

## 3. exact `1/23` real balance window

short remainder descent已有严格 height drop

\[
\boxed{
0<X=5^\lambda Rstar
<\frac1{24}\widehat T_2.}
\tag{3.1}

而

\[
\widehat T_2=X+Y.
\]

所以

\[
24X<X+Y
\Longrightarrow
23X<Y.
\]

因此

\[
\boxed{
0<\frac XY<\frac1{23}.}
\tag{3.2}

除去共同正因子不改变 ratio：

\[
\boxed{
0<\frac{\bar X}{\bar Y}<\frac1{23}.}
\tag{3.3}

这就是 equal-depth parent unit的真实 Archimedean代表。

上一 balance-tail theorem则证明 recycling需要的纯几何 ratio满足

\[
\boxed{
\chi_{geom}
=-\frac{2\mathfrak G_>}{81\mathfrak G_<}
<-1.}
\tag{3.4}

所以

\[
\boxed{
\frac{\bar X}{\bar Y}-\chi_{geom}>1.}
\tag{3.5}

real balance gap不只是异号，而是统一超过1。

---

## 4. balance tail is a positive coprime two-summand form

定义 positive fixed gates

\[
\boxed{A_<:=-\mathfrak G_< >0,}
\qquad
\boxed{A_>:=-\mathfrak G_> >0.}
\tag{4.1}

balance-tail definition化为

\[
\boxed{
\mathscr B_{63}
=81\bar X A_<+2\bar Y A_>.}
\tag{4.2}

所以其正性完全显式，不依赖 cancellation estimate。

结合 (3.4)：

\[
\mathscr B_{63}
=81\bar YA_<
\left(
\frac{\bar X}{\bar Y}-\chi_{geom}
\right).
\tag{4.3}

由 (3.5) 还得到严格 lower bound

\[
\boxed{
\mathscr B_{63}>81\bar Y A_<.}
\tag{4.4}

---

## 5. exact cross-gcd identities

由 (4.2) 与 `gcd(Xbar,Ybar)=1`：

\[
\begin{aligned}
\gcd(\mathscr B_{63},\bar X)
&=\gcd(2\bar YA_>,\bar X)\\
&=\gcd(A_>,\bar X),
\end{aligned}
\]
因为 `Xbar` 为 odd。因此

\[
\boxed{
\gcd(\mathscr B_{63},\bar X)
=\gcd(A_>,\bar X).}
\tag{5.1}

同理

\[
\begin{aligned}
\gcd(\mathscr B_{63},\bar Y)
&=\gcd(81\bar XA_<,\bar Y)\\
&=\boxed{
\gcd(81A_<,\bar Y).}
\end{aligned}
\tag{5.2}

所以对 non-`3` odd prime：

\[
\boxed{
p\mid\mathscr B_{63},\ p\mid\bar X
\Longrightarrow p\mid A_>,}
\tag{5.3}

\[
\boxed{
p\mid\mathscr B_{63},\ p\mid\bar Y,\ p\ne3
\Longrightarrow p\mid A_<.}
\tag{5.4}

tail若回流到某一 residual parent coordinate，必须支付**另一侧** unequal-depth fixed gate。

---

## 6. support trichotomy for balance-tail primes

任意 genuine non-`3` odd prime `r|B_63` 现在只有三种位置：

1. `r|Xbar`：由 (5.3) 同时 `r|A_>`；
2. `r|Ybar`：由 (5.4) 同时 `r|A_<`；
3. `r∤Xbar Ybar`：真正的 parent-external balance-tail prime。

由于 `Xbar,Ybar` 已互素，不存在第四种同时回流两边的 residual support。

特别地 same-prime recycling prime本身在 equal baseline除去 `G_Delta` 后属于第三类：它不再整除 `Xbar,Ybar`，却通过 p-adic ratio `chi_p=chi_geom` 整除 `B_63`。

---

## 7. updated frontier

canonical balance tail现在同时具有：

- positive integer form；
- exact parent baseline removal；
- coprime parent coordinates；
- real ratio window `(0,1/23)` vs geometric `<-1`；
- residual parent reuse的 cross-gate identities。

所以后续若要关闭 balance-tail odd parity，最自然的分类已经变成：

- cross-gate reuse (`A_<`/`A_>` fixed algebraic support)；
- genuine parent-external tail；
- equal-baseline same-prime p-adic balance wrapping。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-balance-gcd-ladder"></a>

> 整合来源：`spontaneous-crt-descendant-balance-gcd-ladder.md`

# A2 descendant same-prime recycling 的 canonical gcd ladder 与 first-baseline depth law

> **依赖：** `spontaneous-crt-descendant-balance-tail.md`、`spontaneous-crt-descendant-balance-coprimality.md`、`spontaneous-crt-descendant-projective-depth-reader.md`。
>
> **严格状态：**canonical positive balance tail `B_63` 已精确选择 linear-remainder overdepth support。本文继续读取 depth。对 common baseline `h=v_p(G_Delta)`，transport/EUCLIDEAN exact expansion中 linear part为 p-unit乘 `G_Delta B_63`，而所有其余项至少二次于 parent errors，故至少含 `p^(2h)`。因此 `min(v_p(M_63),2h)=h+min(v_p(B_63),h)`：若 balance-tail depth小于一个完整 baseline，linear remainder的额外深度被 `B_63` 精确读取；只有 `p^h|B_63` 时二阶 transport才有资格参与。定义 `Sigma_rec=gcd(G_Delta,B_63)` 与 ladder `D_j=gcd(G_Delta^j,B_63)` 后，same-prime recycling获得 ordinary gcd selector，结构与早先 omega-height resonance ladder同型。本文尚未处理 `p^h|B_63` 后的 second-order resonance，因此不关闭 A2。

---

## 1. baseline and balance-tail depth

固定 genuine common prime `p`，记

\[
\boxed{h:=v_p(G_\Delta)\ge1,}
\tag{1.1}

以及 balance-tail depth

\[
\boxed{\rho_p:=v_p(\mathscr B_{63})\ge0.}
\tag{1.2}

由 balance-tail theorem，`rho_p>0` 当且仅当该 common label在 linear remainder中至少再循环一层。

---

## 2. exact first-order scale

balance-tail proof给 transported/Euclidean first-order identity

\[
M^{(1)}
=\frac{64s_L}{5^711^7K^6}
\left(81XG_<+2YG_>\right).
\]

清 third denominator后

\[
\mathfrak G_<=T^6G_<,
\qquad
\mathfrak G_>=T^6G_>,
\]
而

\[
81X\mathfrak G_<+2Y\mathfrak G_>
=-G_\Delta\mathscr B_{63}.
\]

因此

\[
\boxed{
M^{(1)}
=U_{bal}\,G_\Delta\mathscr B_{63},}
\tag{2.1}

其中

\[
U_{bal}
=-\frac{64s_L}{5^711^7K^6T^6}
\]
在当前 genuine non-`3`, non-`5,11`, noncentral external prime上为 p-unit。

所以

\[
\boxed{v_p(M^{(1)})=h+\rho_p.}
\tag{2.2}

---

## 3. every omitted term is at least quadratic in parent errors

transport identity

\[
E_{proj}
=\text{unit}\cdot
[\Phi(J+F/U,R+K^2L)-\Phi(J,R)]
\]
的 constant term为零；一阶项已经全部进入 (2.1)。其余 monomials对 `(F,L)` 的总次数至少2。

而 parent common baseline给

\[
v_p(F)\ge h,
\qquad
v_p(L)\ge h.
\]

Euclidean quotient从 first-layer value到 actual value的变化也是 `O(L)`，再乘外面的 `L` 后同样至少二次。

因此 exact remainder可写

\[
\boxed{
M=M^{(1)}+M^{(\ge2)},}
\tag{3.1}

并有

\[
\boxed{v_p(M^{(\ge2)})\ge2h.}
\tag{3.2}

---

## 4. exact truncated valuation law

由 (2.2),(3.2)：

### `rho_p<h`

此时

\[
h+\rho_p<2h,
\]
linear term唯一最浅，所以

\[
\boxed{v_p(M)=h+\rho_p.}
\tag{4.1}

### `rho_p>=h`

此时 linear term与 higher terms都至少含 `p^(2h)`，所以

\[
\boxed{v_p(M)\ge2h.}
\tag{4.2}

两种情况统一为

\[
\boxed{
\min\{v_p(M),2h\}
=h+\min\{\rho_p,h\}.}
\tag{4.3}

等价地

\[
\boxed{
\min\{v_p(M)-h,h\}
=\min\{v_p(\mathscr B_{63}),h\}.}
\tag{4.4}

所以 `B_63` 精确读取第一个完整 baseline以内的所有 extra depth。

---

## 5. canonical recycling selector

定义 ordinary gcd

\[
\boxed{
\Sigma_{rec}
:=\gcd(G_\Delta,\mathscr B_{63}).}
\tag{5.1}

逐 common prime：

\[
\boxed{
v_p(\Sigma_{rec})
=\min(h,\rho_p).}
\tag{5.2}

特别地

\[
\boxed{
p\mid\Sigma_{rec}
\Longleftrightarrow
v_p(M)>h.}
\tag{5.3}

在当前 genuine regular sector成立。

这把“same-prime recycling”变成一个无需人工 prime list的 canonical integer support selector。

---

## 6. full balance gcd ladder

对任意整数 `j>=1` 定义

\[
\boxed{
D_j^{bal}
:=\gcd(G_\Delta^j,\mathscr B_{63}).}
\tag{6.1}

则逐 common prime

\[
\boxed{
v_p(D_j^{bal})
=\min(jh,\rho_p).}
\tag{6.2}

所以随 `j` 增大，stable ladder读取 `B_63` 上该 common label的完整 balance-tail exponent `rho_p`。

注意 (6.2) 本身是 ordinary gcd identity；其与 actual remainder depth的联系由 §4 的 truncated transport law提供。

---

## 7. the only second-order escape

由 (4.1)：只要

\[
\rho_p<h,
\]
actual remainder depth已经完全确定，没有更高 cancellation自由。

因此要越过 first extra baseline，必要条件是

\[
\boxed{\rho_p\ge h,}
\tag{7.1}

等价于

\[
\boxed{p^h\mid\mathscr B_{63}.}
\tag{7.2}

对整个 common product，这一危险层由

\[
\gcd(G_\Delta,\mathscr B_{63})
\]
是否保留完整 local baseline读取。

所以新的真正 second-order frontier已经明确变成：在 canonical balance equation本身发生**完整 baseline saturation**以后，二次 transported terms是否还能与 linear term继续抵消。

---

## 8. relation to earlier equal-depth ladders

结构上现在有明显平行：

- omega-height equal depth：`Gamma` baseline + `Lambda_tail` resonance ladder；
- descendant same-prime recycle：`G_Delta` baseline + `B_63` balance ladder。

两者都把原先人工的 valuation branch压成 ordinary gcd chain，并把真正无界自由推到“tail至少吞下一个完整 baseline”以后。

因此后续不应再回到 first-layer prime-source enumeration；应直接构造 `rho_p>=h` 下的 second-order normalized balance equation。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-balance-tail"></a>

> 整合来源：`spontaneous-crt-descendant-balance-tail.md`

# A2 descendant same-prime recycling 的 canonical parent-balance tail

> **依赖：** `spontaneous-crt-descendant-unequal-parent-depth.md`、`spontaneous-crt-descendant-linear-depth-reader.md`、`spontaneous-crt-descendant-transport-resonance.md`。
>
> **严格状态：**前一文件按 `a=v_p(Rstar_63)`、`b=v_p(Dhat_63)` 分出两条 unequal-depth coefficient gates；equal depth仍保留一个 normalized parent unit。本文把三种情况重新齐次化。令 parent 两个正 summands为 `X=5^lambda Rstar_63`、`Y=g2^m Dhat_63`，则 projective/additive error与 descendant error满足 exact linear identities `L=s_L(X+Y)`、`F=K^2s_LY`。代入 transported error再减 Euclidean quotient后，一阶 remainder恰为共同 unit乘 `81X G_<+2Y G_>`。因此除去 canonical common baseline `G_Delta` 后得到 positive integer tail `B_63`，其 p-support精确等价于 same-prime linear-remainder overdepth。equal depth时 resonance unit被唯一固定为 `chi=-2G_>/(81G_<)`；真实 endpoint上该几何 ratio严格小于 `-1`。若 parent自身先发生 `chi=-1` cancellation，再要求 child recycling，其 collision resultant恰回到 central / old singular / `H_2,H_10` tangent gates。于是 generic parent-cancelled equal-depth branch不能继续 recycling。本文仍未排除 `chi=chi_geom` 的 p-adic wrapping，因此不关闭 A2。

---

## 1. homogeneous parent coordinates

fully primitive parent descent写成

\[
\boxed{
\widehat{\mathcal T}_2=X+Y,}
\tag{1.1}

其中定义两个 positive integers

\[
\boxed{X:=5^\lambda\mathscr R_{63}^\star,}
\tag{1.2}

\[
\boxed{Y:=g2^m\widehat{\mathscr D}_{63}.}
\tag{1.3}

记

\[
G_\Delta=\gcd(\mathscr R_{63}^\star,
                  \widehat{\mathscr D}_{63}).
\]

因为 `Rstar_63` 与 `10g` 互素，`G_Delta` 与 parent scale `5g2` 互素。因此

\[
\boxed{G_\Delta\mid X,\qquad G_\Delta\mid Y.}
\tag{1.4}

---

## 2. exact errors in terms of `X,Y`

前一 depth theorem给

\[
L
=\frac{2^{2M+2}}{5^mB^2K^2}\widehat T_2.
\]

定义 p-unit/rational scale

\[
\boxed{s_L:=\frac{2^{2M+2}}{5^mB^2K^2}.}
\tag{2.1}

由 (1.1)：

\[
\boxed{L=s_L(X+Y).}
\tag{2.2}

另一方面

\[
F=\frac{\widehat D_{63}}{c_u^2gT}.
\]

直接使用

\[
B^2=2^{2M+2m+2}c_u^2g^2,
\qquad
T=2^m5^m
\]
可验证

\[
\boxed{F=K^2s_LY.}
\tag{2.3}

这两个 identities是 exact，不是只在某个 valuation case成立。

---

## 3. first-order remainder is one homogeneous parent form

transported error的一阶部分为

\[
C_{tr}
\left[
\frac{\Phi_J}{U}F
-K^2(J+\zeta)^2L
\right],
\]
其中

\[
C_{tr}=\frac{65536U^4}{K^8},
\qquad U=2K-9.
\]

Euclidean remainder为

\[
M=E-Q L.
\]

把 (2.2),(2.3) 代入，得到一阶式

\[
M^{(1)}
=s_L\left[
X(C_<-Q_0)+Y(C_>-Q_0)
\right],
\tag{3.1}

其中 `C_<,C_>,Q_0` 正是 unequal-depth文件的 coefficient functions。

该文件定义 primitive integer gates

\[
\mathcal G_<,\qquad\mathcal G_>,
\]
并且 checker给 exact raw normalizations

\[
\boxed{
C_<-Q_0
=\frac{5184}{5^711^7K^6}\mathcal G_<,}
\tag{3.2}

\[
\boxed{
C_>-Q_0
=\frac{128}{5^711^7K^6}\mathcal G_>.}
\tag{3.3}

因为

\[
5184=64\cdot81,
\qquad
128=64\cdot2,
\]
有

\[
\boxed{
M^{(1)}
=\frac{64s_L}{5^711^7K^6}
\left(81X\mathcal G_<+2Y\mathcal G_>\right).}
\tag{3.4}

所有被除 scale在 genuine non-`3`, non-`5,11`, noncentral external prime上均为 units。

---

## 4. clear the third-block denominator

`G_<,G_>` 为 total-degree-6 polynomials in `(K,zeta)`，而

\[
\zeta=a_3/T.
\]

定义 ordinary integer gates

\[
\boxed{
\mathfrak G_<
:=T^6\mathcal G_<(K,a_3/T),}
\tag{4.1}

\[
\boxed{
\mathfrak G_>
:=T^6\mathcal G_>(K,a_3/T).}
\tag{4.2}

`T` 是 genuine p-unit，所以 valuation/support不变。

前一文件 projective Bernstein audit等价于真实 endpoint上

\[
\boxed{
\mathfrak G_<<0,
\qquad
\mathfrak G_><0.}
\tag{4.3}

---

## 5. canonical positive balance tail

定义 homogeneous resonance numerator

\[
\boxed{
\mathscr H_{bal}
:=81X\mathfrak G_<+2Y\mathfrak G_>.}
\tag{5.1}

由 (1.4)：

\[
G_\Delta\mid\mathscr H_{bal}.
\]

又由 `X,Y>0` 与 (4.3)：

\[
\boxed{\mathscr H_{bal}<0.}
\tag{5.2}

因此定义 canonical positive integer

\[
\boxed{
\mathscr B_{63}
:=-\frac{\mathscr H_{bal}}{G_\Delta}
\in\mathbf Z_{>0}.}
\tag{5.3}

这就是 parent-balance tail。

---

## 6. exact support equivalence with same-prime recycling

固定 genuine common prime `p`，写

\[
k=v_p(G_\Delta),
\]

\[
X=p^kX_0,
\qquad
Y=p^kY_0,
\]
其中至少一个 `X_0,Y_0` 为 unit。

所有 transported higher-order terms对 parent errors的总次数至少2，所以至少含 `p^(2k)`。由 (3.4)，再用 `k>=1`：

\[
\boxed{
\frac{M}{p^k}
\equiv
u_p\left(
81X_0\mathfrak G_<
+2Y_0\mathfrak G_>
\right)
\pmod p,}
\tag{6.1}

其中 `nu_p` 为显式 p-unit。

而 (5.3) 除去的 `G_Delta` 在 p 上恰为 `p^k`。因此

\[
\boxed{
p\mid\mathscr B_{63}
\Longleftrightarrow
v_p(M)>k.}
\tag{6.2}

这在当前 genuine regular sector是 exact support selector：same-prime linear-tail recycling不再需要预先按 `a<b,a=b,b<a` 分类。

---

## 7. previous depth cases are the projective limits

若

\[
a=v_p(Rstar)<b=v_p(Dhat),
\]
则模 p

\[
X_0\ne0,\qquad Y_0=0.
\]
(6.1) 恢复

\[
\boxed{\mathfrak G_<\equiv0.}
\tag{7.1}

若

\[
b<a,
\]
则

\[
X_0=0,\qquad Y_0\ne0,
\]
恢复

\[
\boxed{\mathfrak G_>\equiv0.}
\tag{7.2}

所以两个 degree-48 unequal-depth gates只是 homogeneous parent line在 `0` 与 `infinity` 两个 projective endpoints。

---

## 8. equal depth: a canonical parent-balance unit

现在令

\[
a=b=h.
\]
则 `X_0,Y_0` 都是 units。定义

\[
\boxed{
\chi_p:=X_0/Y_0
=\frac{5^\lambda Rstar/p^h}
       {g2^mDhat/p^h}.}
\tag{8.1}

parent sum满足

\[
\frac{\widehat T_2}{p^h}
=Y_0(1+\chi_p).
\]
所以

\[
\boxed{
v_p(\widehat T_2)>h
\Longleftrightarrow
\chi_p\equiv-1\pmod p.}
\tag{8.2}

如果 parent没有额外 cancellation，即 `chi_p!=-1`，same-prime recycling由 (6.1) 唯一锁定：

\[
\boxed{
\chi_p
=-\frac{2\mathfrak G_>}
        {81\mathfrak G_<}
\pmod p.}
\tag{8.3}

因此 equal-depth中最后的 residual unit自由已压成一个 canonical parent-balance unit。

---

## 9. the geometric balance lies strictly below `-1` on the real endpoint

projective gates都为负。进一步定义

\[
\mathfrak H_{-1}
:=81\mathfrak G_<-2\mathfrak G_>.
\]

在 projective `(r,u)` box `[0,10^-3]^2` 上，exact Bernstein audit给全部49个 coefficients严格为正；最小值为

\[
\boxed{
\frac{24267959613723206789529}{6250000000}>0.}
\tag{9.1}

所以真实 endpoint上

\[
\boxed{81\mathfrak G_<-2\mathfrak G_> >0.}
\tag{9.2}

由于 denominator `81G_<` 为负，(8.3) 的 real geometric value满足

\[
\boxed{
\chi_{geom}
:=-\frac{2\mathfrak G_>}{81\mathfrak G_<}
<-1.}
\tag{9.3}

而真实 parent ratio

\[
X/Y>0.
\]
所以 equal-depth recycling也没有 real balance point；只能依赖 p-adic wrapping。

---

## 10. parent cancellation plus child recycling is exactly the tangent collision

若 parent先有额外 cancellation，则

\[
\chi_p=-1.
\]

若同时要求 child recycling，(8.3) 强迫

\[
\boxed{
81\mathfrak G_<-2\mathfrak G_>\equiv0\pmod p.}
\tag{10.1}

乘/除 `T^6` 不改变 genuine p-support。对 primitive `(K,zeta)` polynomial

\[
81\mathcal G_<-2\mathcal G_>
\]
与 universal cubic消去 `zeta`，exact resultant为

\[
\boxed{
\begin{aligned}
&2^{43}3^2(2K-9)^{13}
(K^2-576K+1296)^2\\
&\qquad\cdot G_D(K)^2H_2(K)H_{10}(K),
\end{aligned}}
\tag{10.2}

差一个无关整体正负号。

这与 `spontaneous-crt-descendant-transport-resonance.md` 的 rational-root tangent resultant完全相同。

因此在排除 central / old zero-root / alpha-height / `H_2,H_10` tangent gates后：

\[
\boxed{
\chi_p=-1
\Longrightarrow
p\nmid\mathscr B_{63}.}
\tag{10.3}

也就是说 generic parent-cancelled equal-depth branch**不能继续 same-prime recycling**。

---

## 11. revised final generic bottleneck

same-prime recycling的 parent-depth自由现在已完全 canonical 化：

- unequal depths：fixed projective endpoint gates `G_<,G_>`；
- equal depth + parent cancellation `chi=-1`：只在已知 tangent factor set中重合；
- genuine remaining generic branch：
  \[
  \boxed{
  a=b=h,
  \quad\chi_p\ne-1,
  \quad\chi_p=\chi_{geom}< -1\text{ (real)}
  }
  \]
  通过 p-adic wrapping实现。

而所有 same-prime recycling support统一由 positive canonical integer `B_63` 读取。

下一步最窄目标已经变成：为 `B_63` 建立 height / primitive parity，或把 `chi_p=chi_geom` 与 parent positive ratio的 natural representative做 prime-power budget。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-common-parity"></a>

> 整合来源：`spontaneous-crt-descendant-common-parity.md`

# A2 fully primitive descendant pair 的 canonical common-parity dichotomy

> **依赖：** `spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descended-quotient-orientation.md`、`spontaneous-crt-target-descent-global-gcd.md`、`spontaneous-crt-source-descent-depth.md`。
>
> **严格状态：**fully primitive positive descent产生 `Rstar_63,Dhat_63` 两个 odd descendant carriers。本文取它们的完整 common gcd，并把 mod-4 parity精确分配到 common part与互素 residuals。危险 orientation `Z=1 mod4` 中，若 common gcd为 `1 mod4`，两个 residual都是 `3 mod4` 并强迫两枚 distinct inert suppliers；若 common gcd为 `3 mod4`，双 parity被 common part吸收。另一 orientation `Z=3 mod4` 中，无论 common gcd orientation如何，总有且仅有一个 residual为 `3 mod4`。结合已完成的 target/source overlap audit，common parity若被吸收，只能由 fixed target `31/179`、受双短 carrier控制的 source-common overlap、或真正 external common kernel承担。本文尚未排除最后一类，因此不关闭 A2。

---

## 1. the descendant pair

fully primitive height descent为

\[
\boxed{
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.}
\tag{1.1}
\]

已有

\[
\boxed{
\mathscr R_{63}^\star>0,
\qquad
\mathscr R_{63}^\star\equiv3\pmod4,}
\tag{1.2}
\]

\[
\boxed{
\widehat{\mathscr D}_{63}>0,
\qquad
\widehat{\mathscr D}_{63}\equiv3Z\pmod4,}
\tag{1.3}
\]

其中 `Z` 为 odd endpoint orientation，所以

\[
Z\equiv1\text{ or }3\pmod4.
\]

两个 carriers都是 positive odd integers。

---

## 2. canonical common gcd

定义完整 common gcd

\[
\boxed{
G_\Delta
:=\gcd(\mathscr R_{63}^\star,
          \widehat{\mathscr D}_{63}).}
\tag{2.1}
\]

以及 coprime residuals

\[
\boxed{
R_\Delta^\circ
:=\frac{\mathscr R_{63}^\star}{G_\Delta},
\qquad
D_\Delta^\circ
:=\frac{\widehat{\mathscr D}_{63}}{G_\Delta}.}
\tag{2.2}
\]

则

\[
\boxed{\gcd(R_\Delta^\circ,D_\Delta^\circ)=1.}
\tag{2.3}
\]

`G_Delta` 为 odd，因此模 `4` 可逆。由 (1.2),(1.3)：

\[
\boxed{
R_\Delta^\circ
\equiv3G_\Delta^{-1}\pmod4.}
\tag{2.4}
\]

\[
\boxed{
D_\Delta^\circ
\equiv3ZG_\Delta^{-1}\pmod4.}
\tag{2.5}
\]

---

## 3. dangerous `Z=1`: either common parity or two distinct residual suppliers

固定

\[
\boxed{Z\equiv1\pmod4.}
\tag{3.1}
\]

此时两个 parent 都是 `3 mod4`：

\[
\mathscr R_{63}^\star
\equiv
\widehat{\mathscr D}_{63}
\equiv3\pmod4.
\]

### common gcd `1 mod4`

若

\[
G_\Delta\equiv1\pmod4,
\]
由 (2.4),(2.5)：

\[
\boxed{
R_\Delta^\circ
\equiv
D_\Delta^\circ
\equiv3\pmod4.}
\tag{3.2}
\]

两个 residual positive、odd、coprime，因此每个都必须含至少一枚 `3 mod4` prime到奇次，而且 suppliers不能相同：

\[
\boxed{
Z\equiv1,\quad G_\Delta\equiv1\pmod4
\Longrightarrow
\text{至少两枚 distinct residual inert primes}.}
\tag{3.3}
\]

### common gcd `3 mod4`

若

\[
G_\Delta\equiv3\pmod4,
\]
则

\[
\boxed{
R_\Delta^\circ
\equiv
D_\Delta^\circ
\equiv1\pmod4.}
\tag{3.4}
\]

此时两个 parent 的 odd-inert parity可以由 common gcd整体承担。由于

\[
G_\Delta\equiv3\pmod4,
\]
`G_Delta` 自身必含至少一枚 inert prime到奇次。

所以危险 orientation 的 strict dichotomy为

\[
\boxed{
Z\equiv1:
\quad
\begin{cases}
G_\Delta\equiv1:&\text{两个 distinct residual suppliers},\\
G_\Delta\equiv3:&\text{common gcd承担 odd parity}.
\end{cases}}
\tag{3.5}
\]

---

## 4. `Z=3`: one residual parity always survives

现在固定

\[
\boxed{Z\equiv3\pmod4.}
\tag{4.1}
\]

则

\[
\mathscr R_{63}^\star\equiv3,
\qquad
\widehat{\mathscr D}_{63}\equiv1
\pmod4.
\]

若 `G_Delta≡1`：

\[
R_\Delta^\circ\equiv3,
\qquad
D_\Delta^\circ\equiv1.
\]

若 `G_Delta≡3`，因为 `3^{-1}≡3 mod4`：

\[
R_\Delta^\circ\equiv1,
\qquad
D_\Delta^\circ\equiv3.
\]

所以无论 common gcd orientation如何：

\[
\boxed{
Z\equiv3\pmod4
\Longrightarrow
\text{恰有一个 coprime descendant residual为 }3\pmod4.}
\tag{4.2}
\]

因此总有一枚 odd-inert supplier位于 common gcd之外：

\[
\boxed{
Z\equiv3
\Longrightarrow
\text{至少一份 non-common descendant inert parity}.}
\tag{4.3}
\]

---

## 5. common parity can now be split by prime-source origin

危险 `Z=1,G_Delta≡3` 分支中真正需要解释的是 common gcd 的 odd parity。

此前两套 overlap audit已经给：

### target labels

若 common prime同时属于 equal-depth target pool，则 prime label只能是

\[
\boxed{31\text{ or }179.}
\tag{5.1}
\]

与 target baseline 的 canonical common factor为 squarefree

\[
\boxed{G_{TD}\mid31\cdot179.}
\tag{5.2}
\]

### source-common labels

若 common prime同时属于 source common gcd，则其三重 common depth `k_r` 必须通过

\[
H_{SD}
=
\prod r^{\lceil k_r/2\rceil}
\]
收费，且

\[
\boxed{H_{SD}\mid18K-55.}
\tag{5.3}
\]

\[
\boxed{
H_{SD}\mid\mathscr H_{S63}.}
\tag{5.4}
\]

其中

\[
\mathscr H_{S63}
=102383gT-29952ga_3+14976C5^\lambda.
\]

此外 source common 与 target support完全分离。

因此 `G_Delta` 的 inert parity supplier若既不是 fixed `31/179`，也不是 source-common overlap，就必须进入一个真正的

\[
\boxed{\text{external descendant-common kernel}.}
\tag{5.5}
\]

这给后续 closure一个明确对象，而不再把所有 common primes混在同一 gcd 中。

---

## 6. revised parity frontier

fully primitive descent现在提供如下全局分叉：

1. `Z=3`：自动有一份 non-common descendant inert parity；
2. `Z=1,G_Delta=1 mod4`：自动有两份 distinct non-common descendant inert parity；
3. `Z=1,G_Delta=3 mod4`：唯一逃逸方式是 common gcd自身含 odd inert parity；该 parity的 old-pool来源已被压成
   - fixed target `31/179`；
   - source-common double-short depth；
   - residual external common kernel。

所以下一步真正需要关闭的是第三项中的 external common parity，或者证明前两类 old-pool parity无法使整个 `G_Delta` 达到 `3 mod4`。ordinary resultant/Legendre路线此前已经审计为 no-go，因此应优先使用 height drop、natural representative或其它 prime-source ledger。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-companion-separation"></a>

> 整合来源：`spontaneous-crt-descendant-companion-separation.md`

# A2 descendant external common 与 `G_JB` companion-common support 的严格分离

> **依赖：** `spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-pure-prefix-elimination.md`、`spontaneous-companion-external-tail-budget.md`、`spontaneous-height-equal-depth-target-selector.md`。
>
> **严格状态：**此前 `G_JB` 的 generic external common depth会无损进入 `Lambda_tail`，因此需要确认新 descended common kernel是否自动属于该 old external pool。本文证明答案恰好相反：在 `alpha`-separated genuine sector，若 prime已经进入 descendant common gcd，则它整除 `J_Hhat` 当且仅当它进入 central gate `2K-9`。因此 generic pure-spontaneous noncentral descendant-common prime必满足 `p∤J_Hhat`，从而与 `G_JB` support严格互斥。故 `Lambda_tail` 的 external companion budget不能用于支付 generic descendant-only external parity；两类 external pool必须分开记账。本文不排除 descendant-only pool本身，因此不关闭 A2。

---

## 1. descendant common always enters the original additive carrier

fully primitive descent给

\[
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.
\]

若 odd prime `p` 进入 descendant common gcd

\[
\boxed{
p\mid\mathscr R_{63}^\star,
\qquad
p\mid\widehat{\mathscr D}_{63},}
\tag{1.1}
\]

则立刻

\[
\boxed{p\mid\widehat{\mathcal T}_2.}
\tag{1.2}
\]

这一步不使用任何 prime-source 标签。

---

## 2. height-free identity gives an exact central equivalence

已有 height-free additive identity

\[
\boxed{
\widehat{\mathcal T}_2
=5^m\widehat{\mathcal J}_H
-2^{m+1}B_0^2(2K-9)\alpha,}
\tag{2.1}
\]

其中

\[
B_0=c_ug,
\qquad
\alpha=TK+a_3=\omega W_q.
\]

固定 genuine odd prime满足

\[
\boxed{p\nmid2\cdot5\cdot B_0\alpha.}
\tag{2.2}
\]

在 descendant common support 上由 (1.2)，(2.1) 化为

\[
\boxed{
5^m\widehat{\mathcal J}_H
\equiv
2^{m+1}B_0^2(2K-9)\alpha
\pmod p.}
\tag{2.3}
\]

(2.2) 说明除 `2K-9` 外所有乘子均为 unit，所以得到 exact support equivalence

\[
\boxed{
p\mid\widehat{\mathcal J}_H
\Longleftrightarrow
p\mid2K-9,}
\tag{2.4}
\]

前提是 `p` 已满足 descendant common (1.1) 与 separation (2.2)。

---

## 3. generic pure-spontaneous descendant support is `J_H`-free

`spontaneous-prefix-branch-audit.md` / `spontaneous-crt-pure-prefix-elimination.md` 的 genuine pure-spontaneous generic branch本来就要求

\[
\boxed{p\nmid\alpha,}
\tag{3.1}
\]

并单列 central line，所以 generic branch还有

\[
\boxed{p\nmid2K-9.}
\tag{3.2}
\]

source/content separation同时保证 (2.2) 的其余 unit条件。

因此由 (2.4)：

\[
\boxed{p\nmid\widehat{\mathcal J}_H.}
\tag{3.3}
\]

这是比“没有证据说明它进入 companion pool”更强的结论：generic pure-spontaneous descendant-common prime**严格不能**进入 `J_H` support。

---

## 4. consequence for the canonical companion-common carrier

canonical height decomposition定义

\[
D_H=\gcd(\widehat{\mathcal J}_H,W_q),
\]

\[
J^\circ=\widehat{\mathcal J}_H/D_H,
\qquad
B^\circ=\mathscr B_W/D_H,
\]

\[
\boxed{G_{JB}:=\gcd(J^\circ,B^\circ).}
\tag{4.1}
\]

显然

\[
p\mid G_{JB}
\Longrightarrow
p\mid J^\circ
\Longrightarrow
p\mid\widehat{\mathcal J}_H.
\tag{4.2}
\]

与 (3.3) 合并：

\[
\boxed{
\operatorname{Supp}_{\rm gen\,pure}(G_\Delta)
\cap
\operatorname{Supp}(G_{JB})
=\varnothing.}
\tag{4.3}
\]

这里左侧只指 `alpha`-free、noncentral genuine pure-spontaneous descendant-common sector；height/content/central/fixed sectors仍按既有文件单列。

---

## 5. `Lambda_tail` external budget cannot pay this pool

`spontaneous-companion-external-tail-budget.md` 已证明 generic external companion-common subproduct

\[
G_{JB}^{\rm ext}
\]
完整整除

\[
\Lambda_{\rm tail}.
\]

但 (4.3) 现在说明：新 pure-prefix descendant external carrier与该 external companion pool support严格互斥。

因此不能把

\[
G_\Delta^{\rm pure,ext}
\]
错误地装进 `Lambda_tail` 的旧预算。正确 ledger 是两类独立 external pool：

\[
\boxed{
\begin{array}{c|c|c}
\text{pool}&\text{defining common support}&\text{canonical reader}\\ \hline
\text{companion external}&J^\circ\cap B^\circ&\Lambda_{\rm tail}\\
\text{descendant-only external}&R_{63}^\star\cap\widehat D_{63}&\mathcal X_{63,i}^{\rm pref}
\end{array}}
\tag{5.1}

并且 generic supports互斥。

---

## 6. only the central gate can reconnect them

由 (2.4)，在 `alpha`-separated descendant common sector中，若还要求

\[
p\mid\widehat{\mathcal J}_H,
\]
则必须

\[
\boxed{p\mid2K-9.}
\tag{6.1}
\]

所以 descendant common 与 companion/`J_H` support重新接触的唯一入口就是已经反复出现的 central line。

该 central line已有 fixed/content/omega-content audits；本文不重复，也不把它混回 generic pure-prefix carrier。

---

## 7. updated frontier

这一步关闭了一个潜在但错误的 product-budget shortcut：generic pure-spontaneous descendant common depth**不能**借 `G_JB^ext|Lambda_tail` 付账。

因此剩余 A2 external parity确实集中在新构造的 pure-prefix side：

- generic coefficient：`X_63,i^pref(x,y)=0`；
- low coefficient singular：short `V_4`，primitive `7 mod8`；
- high coefficient singular：compact `V_24`，primitive `5 mod8`。

下一步应直接为这些 descendant-only pure-prefix carriers建立自己的 height/depth budget，而不是继续复用旧 companion tail。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-linear-depth-reader"></a>

> 整合来源：`spontaneous-crt-descendant-linear-depth-reader.md`

# A2 descendant-only external depth 的 shorter linear-remainder carrier

> **依赖：** `spontaneous-crt-descendant-projective-depth-reader.md`、`spontaneous-crt-descendant-projective-integer.md`。
>
> **严格状态：**projective depth theorem用 resultant integer `P_63` 读取完整 descendant common baseline，但 `P_63` 的 clearing scale为 `R^8Y^8`。本文回到 universal cubic对 branch quadratic的 Euclidean remainder `M_63=A r+B` 本身。清去固定 `5^7 11^7` denominator后，`A#` 在真实 projective box严格为正、`B#` 严格为负；因 `r=1/K` 极小，`M_63` 真实值严格为负。统一清 `u,v` denominator只需 `R^7Y^4`，得到更短 ordinary integer `M_63^int`。它同样读取完整 common baseline，且 `v_2(M_63^int)=8M+7m+33`。取 positive carrier `H_M63=-M_63^int` 后 primitive part总为 `1 mod4`：`m` 偶时 `5 mod8`，`m` 奇时 `1 mod8`。因此 pure external common product若自身为 `3 mod4`，从这个更短 carrier中约去 baseline后仍强迫一份 `3 mod4` tail。本文尚未排除 linear-remainder overdepth，因此不关闭 A2。

---

## 1. integer-normalized projective remainder

沿用 projective Euclidean division

\[
\mathscr E_{\rm proj}
=Q_{63}\mathscr L_{\rm proj}
+M_{63},
\]

\[
\boxed{M_{63}=A(u,v)r+B(u,v),}
\tag{1.1}

其中

\[
r=1/K,
\qquad
u=a_3/(TK),
\qquad
v=Q^2N_0/(B^2K^2).
\]

exact coefficient audit给

\[
\deg_v A=3,
\qquad
\deg_v B=4,
\]

\[
\deg_u A=\deg_u B=7,
\]

且二者 coefficient denominator的共同固定尺度为

\[
\boxed{D_0:=5^7 11^7.}
\tag{1.2}

定义 integer polynomials

\[
\boxed{A^\#:=D_0A,\qquad B^\#:=D_0B.}
\tag{1.3}

它们分别有 `20` 与 `24` 个 monomials。

---

## 2. exact sign on the actual projective box

真实 box仍为

\[
0<u<1/1000,
\qquad
937/1000<v<939/1000.
\]

对 `A#`,`B#` 分别做 exact rational tensor-Bernstein audit，得到

\[
\boxed{
\frac{186871147561988154254304}{15625}
<A^\#
<
\frac{5744925543296429255273134446887094}
{476837158203125}.}
\tag{2.1}

特别地

\[
\boxed{A^\#>0.}
\tag{2.2}

对 `B#`：

\[
\boxed{
-\frac{82743358059276934923729}{1953125}
<B^\#
<
-\frac{18219304842663055778170041164244}
{476837158203125}<0.}
\tag{2.3}

这里右端是离零最近的 upper bound。

而实际 `K>9*10^11`，本文甚至只用极弱的

\[
K>1000.
\]

两端 exact difference为

\[
\boxed{
-\sup B^\#-\frac{\sup A^\#}{1000}
=
\frac{6237189649683313261448453358678453}
{238418579101562500}>0.}
\tag{2.4}

因此

\[
\boxed{
\frac{A^\#}{K}+B^\#<0.}
\tag{2.5}

即 normalized linear remainder在整个真实 dangerous endpoint严格为负。

---

## 3. clear only the necessary denominators

继续记

\[
R:=TK,
\qquad
X:=Q^2N_0,
\qquad
Y:=B^2K^2.
\]

由于 `deg_u<=7, deg_v<=4`，定义 ordinary integer

\[
\boxed{
\begin{aligned}
\mathscr M_{63}^{\rm int}
:=R^7Y^4\Bigl[&
A^\#(a_3/R,X/Y)\\
&+K B^\#(a_3/R,X/Y)
\Bigr].
\end{aligned}}
\tag{3.1}

它只有 `20+24` 个 composite input terms，清分母尺度仅为

\[
R^7Y^4,
\]
明显短于 projective resultant reader的 `R^8Y^8`。

由 (1.1),(1.3)：

\[
\boxed{
\mathscr M_{63}^{\rm int}
=D_0 K R^7Y^4\,M_{63}.}
\tag{3.2}

在 genuine external sector，`D_0 KRY` 全为 p-units，所以

\[
\boxed{
v_p(\mathscr M_{63}^{\rm int})=v_p(M_{63}).}
\tag{3.3}

前一 depth theorem已有 `v_p(M_63)>=k_p`，故

\[
\boxed{v_p(\mathscr M_{63}^{\rm int})\ge k_p.}
\tag{3.4}

由 (2.5) 与 positive clearing：

\[
\boxed{\mathscr M_{63}^{\rm int}<0.}
\tag{3.5}

定义 positive carrier

\[
\boxed{H_{M63}:=-\mathscr M_{63}^{\rm int}>0.}
\tag{3.6}

---

## 4. exact binary ledger

已有

\[
v_2(a_3)=0,
\qquad
v_2(R)=m+1,
\]

\[
v_2(X)=2M+2,
\qquad
v_2(Y)=2M+2m+2t+2.
\]

对 `A#` monomial `a_ij u^i v^j`，(3.1) 中相应 term depth为

\[
v_2(a_{ij})+(7-i)(m+1)+j(2M+2)+(4-j)(2M+2m+2t+2).
\]

`B#` monomial还多一个 `K`，所以再加 `1`。

抽出公共

\[
7(m+1)+4(2M+2),
\]
后，extra depths分别为

\[
\epsilon^A_{ij}
=v_2(a_{ij})-i(m+1)+(4-j)(2m+2t),
\tag{4.1}

\[
\epsilon^B_{ij}
=v_2(b_{ij})+1-i(m+1)+(4-j)(2m+2t).
\tag{4.2}

checker验证所有 support上的 `m,t` slopes非负，所以最小值在 `(m,t)=(5,3)` 读取。

唯一 minimum来自 `K B#` 的

\[
(i,j)=(0,4)
\]
项，其 coefficient为

\[
\boxed{
b_{0,4}
=2^{17}3^{12}5^3 11^3 13.}
\tag{4.3}

它给

\[
\boxed{\epsilon^B_{0,4}=18.}
\tag{4.4}

第二浅层已经是 `21`，所以不存在 first-layer cancellation。

因此

\[
\boxed{
 v_2(\mathscr M_{63}^{\rm int})
=7(m+1)+4(2M+2)+18
=8M+7m+33.}
\tag{4.5}

---

## 5. signed and positive primitive orientations

除去 (4.5) 后只剩 dominant `(0,4)` term。记

\[
k_0:=K/2\quad\text{odd}.
\]

有

\[
R/2^{m+1}=5^m k_0.
\]

因此 signed primitive unit为

\[
\begin{aligned}
\frac{\mathscr M_{63}^{\rm int}}{2^{8M+7m+33}}
&\equiv
\frac{b_{0,4}}{2^{17}}
\,k_0\,(5^m k_0)^7
\left(\frac X{2^{2M+2}}\right)^4\\
&\equiv3\cdot5^m\pmod8,
\end{aligned}
\tag{5.1}

因为 `k_0^8≡1`、odd fourth power也为 `1 mod8`。

所以

\[
\boxed{
\frac{\mathscr M_{63}^{\rm int}}{2^{8M+7m+33}}
\equiv
\begin{cases}
3\pmod8,&m\text{ even},\\
7\pmod8,&m\text{ odd}.
\end{cases}}
\tag{5.2}

但正 carrier为相反数。定义

\[
\boxed{
H_{M63}^\circ
:=\frac{H_{M63}}{2^{8M+7m+33}}.}
\tag{5.3}

则

\[
\boxed{
H_{M63}^\circ
\equiv
\begin{cases}
5\pmod8,&m\text{ even},\\
1\pmod8,&m\text{ odd}.
\end{cases}}
\tag{5.4}

特别地无条件

\[
\boxed{H_{M63}^\circ\equiv1\pmod4.}
\tag{5.5}

---

## 6. full common baseline and parity tail

定义 genuine descendant-only external baseline product

\[
G_\Delta^{\rm pure}
=\prod p^{k_p}.
\]

由 (3.4)：

\[
\boxed{G_\Delta^{\rm pure}\mid H_{M63}^\circ.}
\tag{6.1}

若该 pure external common product承担 odd parity：

\[
G_\Delta^{\rm pure}\equiv3\pmod4,
\]
则 (5.5) 强迫

\[
\boxed{
\frac{H_{M63}^\circ}{G_\Delta^{\rm pure}}
\equiv3\pmod4.}
\tag{6.2}

所以从更短的 linear-remainder carrier中也会产生一份 baseline之外的 odd-inert tail。

同一 prime若想再次承担该 tail，就必须满足

\[
\boxed{v_p(M_{63})>k_p.}
\tag{6.3}

因此下一步无需继续使用更大的 `P_63`：generic same-prime recycling的最短 target已经变成 linear remainder的 overdepth。

---

## 7. updated frontier

new external ledger现在有两层 reader：

- `P_63`：resultant reader，结构最 canonical；
- `H_M63`：linear-remainder reader，scale更短，完整读取同一 baseline。

`H_M63^circ≡1 mod4` 意味着 common product若为 `3 mod4`，必留下另一份 odd tail。故 generic closure可以进一步集中为：

\[
\boxed{v_p(M_{63})>k_p}
\]
的 same-prime overdepth是否可能无限发生。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-projective-depth-reader"></a>

> 整合来源：`spontaneous-crt-descendant-projective-depth-reader.md`

# A2 descendant-only external common depth 的 projective reader 与 resonance tail

> **依赖：** `spontaneous-crt-descendant-projective-integer.md`、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descended-quotient-orientation.md`、`endpoint-lattice.md` 的 exact rational-root equation。
>
> **严格状态：**上一文件构造 positive canonical integer `P_63`，但只记录 support。本文证明 descendant common gcd 的完整 baseline exponent逐 prime都进入 `P_63`。核心是把 universal cubic恢复成 exact rational-root polynomial `Phi(J,R)` 在 additive approximation `R_0` 与 descendant approximation `J_0` 上的值：`Phi(J_0,R_0)=E_63/[65536(2K-9)^4]`，而 `R_0-R` 正比于 projective branch error `L_proj`，`J_0-J` 正比于 descendant error `F_Delta`。因此 common depth `k` 同时进入 `L_proj,E_proj`，继而进入 projective resultant与 `P_63`。本文还给 resultant 的 exact local identity，证明在 coefficient/repeated-root singular gates之外，额外 projective depth只能来自一次 equal-depth normalized cancellation。于是若 pure external common product本身承担 odd parity，`P_63^circ≡1 mod8` 会强迫一份额外 inert tail；同一 prime若想重复支付，必须进入该 resonance tail。本文仍未排除 resonance tail，因此不关闭 A2。

---

## 1. common baseline depth

固定 genuine alpha-free、noncentral descendant-only external prime `p`。写

\[
a_p:=v_p(\mathscr R_{63}^\star),
\qquad
b_p:=v_p(\widehat{\mathscr D}_{63}),
\]

\[
\boxed{k_p:=\min(a_p,b_p)\ge1.}
\tag{1.1}

fully primitive descent为

\[
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.
\]

在 genuine external sector `p∤10g`，所以

\[
\boxed{v_p(\widehat{\mathcal T}_2)\ge k_p.}
\tag{1.2}

若 `a_p!=b_p`，两项深度不同，甚至有

\[
\boxed{v_p(\widehat{\mathcal T}_2)=k_p.}
\tag{1.3}

只有 equal descendant depth `a_p=b_p` 时，parent descent本身才可能继续 cancellation。

---

## 2. exact rational-root error coordinates

令真实 finite-defect root为

\[
J:=3-C/D,
\]
并记

\[
\zeta:=a_3/T,
\qquad
R:=Q^2N_0/B^2.
\]

exact rational-root equation为

\[
\boxed{
\Phi(J,R)
:=J(J+2\zeta)(K-J)^2
-R(J+\zeta)^2
=0.}
\tag{2.1}

additive carrier对应的 zero approximation为

\[
\boxed{
R_0
:=K^2-(18+4\zeta)K+18\zeta+55.}
\tag{2.2}

projective variables

\[
r=1/K,
\qquad
u=\zeta/K,
\qquad
v=R/K^2
\]
下

\[
\mathscr L_{\rm proj}
=55r^2+18(u-1)r+1-4u-v.
\]

直接乘回 `K^2`：

\[
\boxed{
R_0-R=K^2\mathscr L_{\rm proj}.}
\tag{2.3}

另一方面定义 descendant residual

\[
\boxed{
F_\Delta
:=(2K-9)(2K-9-J-2\zeta)
-\frac{63}{16}K^2.}
\tag{2.4}

由

\[
\widehat{\mathscr D}_{63}
=c_u^2gT\,F_\Delta
\]
在 genuine sector `p∤c_ugT` 得

\[
\boxed{v_p(F_\Delta)=b_p\ge k_p.}
\tag{2.5}

令

\[
\boxed{
J_0
:=\frac{K^2-64K\zeta-576K+288\zeta+1296}
{16(2K-9)}.}
\tag{2.6}

从 (2.4) 直接解出

\[
\boxed{
J_0-J=\frac{F_\Delta}{2K-9}.}
\tag{2.7}

所以 additive 与 descendant 两个 approximation errors都至少有 `k_p` 层。

---

## 3. universal cubic is exactly the transported rational-root error

`spontaneous-crt-universal-descendant-cubic.md` 定义 `E_63(K,zeta)`。直接代入 (2.2),(2.6) 并清分母，得到 exact identity

\[
\boxed{
\Phi(J_0,R_0)
=
\frac{\mathcal E_{63}(K,\zeta)}
{65536(2K-9)^4}.}
\tag{3.1}

因为真实 `Phi(J,R)=0`，而

\[
J_0=J+F_\Delta/(2K-9),
\]

\[
R_0=R+K^2\mathscr L_{\rm proj},
\]
所以

\[
\Phi(J_0,R_0)-\Phi(J,R)
\]
是关于两个 error variables

\[
F_\Delta,
\qquad
\mathscr L_{\rm proj}
\]
的 polynomial，且没有 constant term。所有清分母只使用 `2K-9`，在 noncentral genuine sector为 unit。

因此只要

\[
v_p(F_\Delta)\ge k_p,
\qquad
v_p(\mathscr L_{\rm proj})\ge k_p,
\]
就有

\[
\boxed{v_p(\mathcal E_{63})\ge k_p.}
\tag{3.2}

而 (1.2) 与 `Theta_dec=B^2TK^2 L_proj`、primitive normalization只差 `2,5` units，给

\[
\boxed{v_p(\mathscr L_{\rm proj})\ge k_p.}
\tag{3.3}

故 (3.2) 无条件适用于当前 generic descendant common prime。

---

## 4. move the depth into the projective resultant

在 actual projective point

\[
r=1/K,
\qquad
u=\zeta/K,
\qquad
v=R/K^2,
\]
定义

\[
\mathscr E_{\rm proj}(r,u)
=r^8\mathcal E_{63}(1/r,u/r).
\]

`p∤K`，所以由 (3.2)

\[
\boxed{v_p(\mathscr E_{\rm proj})\ge k_p.}
\tag{4.1}

将 `E_proj` 对 quadratic `L_proj` 做 Euclidean division：

\[
\boxed{
\mathscr E_{\rm proj}
=Q_{63}\mathscr L_{\rm proj}
+M_{63},}
\tag{4.2}

\[
\boxed{M_{63}=A_{63}^{\rm proj}r+B_{63}^{\rm proj}.}
\tag{4.3}

division denominator只含 `55=5*11`；当前 genuine branch排除 `5,11`。由 (3.3),(4.1)：

\[
\boxed{v_p(M_{63})\ge k_p.}
\tag{4.4}

projective resultant `X_63^proj` 除 fixed content `5^7 11^7` 外，正是 `L_proj` 与 `M_63` 的 resultant。因此

\[
\boxed{v_p(\mathscr X_{63}^{\rm proj})\ge k_p.}
\tag{4.5}

最后 canonical integer clearing

\[
\mathscr P_{63}
=(TK)^8(B^2K^2)^8
\mathscr X_{63}^{\rm proj}(a_3/(TK),Q^2N_0/(B^2K^2))
\]
只乘 genuine p-units，故

\[
\boxed{v_p(\mathscr P_{63})\ge k_p.}
\tag{4.6}

---

## 5. global full-baseline divisibility

令 `E_pure` 为当前 genuine alpha-free noncentral descendant-only external primes，并定义 baseline common product

\[
\boxed{
G_\Delta^{\rm pure}
:=\prod_{p\in E_{pure}}p^{k_p}.}
\tag{5.1}

逐 prime由 (4.6)：

\[
\boxed{G_\Delta^{\rm pure}\mid\mathscr P_{63}.}
\tag{5.2}

由于 `G_pure` 为 odd，而上一文件证明

\[
v_2(\mathscr P_{63})=16M+8m+58,
\]
定义 positive odd primitive carrier

\[
\boxed{
\mathscr P_{63}^\circ
:=\frac{\mathscr P_{63}}{2^{16M+8m+58}}.}
\tag{5.3}

则仍有完整 baseline divisibility

\[
\boxed{G_\Delta^{\rm pure}\mid\mathscr P_{63}^\circ.}
\tag{5.4}

---

## 6. exact local resultant identity and the only generic overdepth mechanism

写 projective quadratic

\[
L(r)=55r^2+br+c,
\]
其中

\[
b=18(u-1),
\qquad
c=1-4u-v,
\]
以及 linear remainder

\[
M(r)=Ar+B.
\]

其 raw resultant为

\[
X=55B^2-bAB+cA^2.
\]

对任意 evaluation point `r` 有 exact identity

\[
\boxed{
X
=A^2L(r)-A L'(r)M(r)+55M(r)^2.}
\tag{6.1}

固定 prime满足 coefficient/repeated-root separation

\[
\boxed{p\nmid A L'(r).}
\tag{6.2}

记

\[
\ell:=v_p(L(r)),
\qquad
\mu:=v_p(M(r)).
\]

若

\[
\ell<\mu,
\]
则 (6.1) 唯一最低项是 `A^2L`：

\[
\boxed{v_p(X)=\ell.}
\tag{6.3}

若

\[
\mu<\ell,
\]
唯一最低项是 `-AL'M`：

\[
\boxed{v_p(X)=\mu.}
\tag{6.4}

所以

\[
\boxed{
\ell\ne\mu
\Longrightarrow
v_p(X)=\min(\ell,\mu).}
\tag{6.5}

额外 projective depth只能发生在

\[
\boxed{\ell=\mu=:h.}
\tag{6.6}

此时写

\[
L=p^hL_0,
\qquad
M=p^hM_0,
\]
其中 `L_0,M_0` 为 units。除以 `p^h` 后，`55M^2` 至少还含 `p^h`，所以 extra depth iff

\[
\boxed{
A L_0-L'(r)M_0\equiv0\pmod p.}
\tag{6.7}

因此 generic same-prime overdepth不是任意现象，而是一条明确的 equal-depth normalized resonance。

若 `p|A`，进入已单列的 coefficient-singular `H_4/H_24`；若 `p|L'`，进入 `spontaneous-single-branch.md` 的 repeated-root tangent。本文不把这两类算作 generic resonance。

---

## 7. parity consequence of the full baseline reader

上一文件证明

\[
\boxed{
\mathscr P_{63}^\circ>0,
\qquad
\mathscr P_{63}^\circ\equiv1\pmod8.}
\tag{7.1}

定义 projective tail

\[
\boxed{
\mathscr T_{63}^{\rm proj}
:=\frac{\mathscr P_{63}^\circ}{G_\Delta^{\rm pure}}.}
\tag{7.2}

若 pure external common product本身承担 odd inert parity，即

\[
G_\Delta^{\rm pure}\equiv3\pmod4,
\]
则由 (7.1)

\[
\boxed{
\mathscr T_{63}^{\rm proj}\equiv3\pmod4.}
\tag{7.3}

所以 common baseline若想吸收一份 descendant odd parity，canonical projective carrier中自动出现另一份 odd-inert valuation **超过 baseline common product**。

这份 tail可以由另一枚 inert prime承担；若仍想由同一个 common label重复承担，则必须有

\[
\boxed{v_p(\mathscr P_{63})>k_p,}
\tag{7.4}

并进入 §6 的 projective overdepth mechanism（或 coefficient/repeated-root singular gates）。

---

## 8. updated closure target

pure descendant external common escape现在不再只是一个任意 common gcd：

1. full baseline depth由 `P_63` 读取；
2. `P_63^circ` 为 positive `1 mod8`；
3. common product若为 `3 mod4`，其 quotient自动再产生 `3 mod4` tail；
4. same-prime tail recycling只剩：
   - generic equal-depth resonance (6.7)；
   - coefficient singular `H_4/H_24`；
   - repeated-root tangent。

因此下一步最窄的 generic closure target已经变成排除或收费 (6.7) 的 normalized equal-depth resonance，而不是继续扩张 prime-source 分类。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-projective-integer"></a>

> 整合来源：`spontaneous-crt-descendant-projective-integer.md`

# A2 descendant-only external pool 的 canonical projective integer carrier

> **依赖：** `spontaneous-crt-pure-projective-carrier.md`、`spontaneous-crt-descendant-companion-separation.md`、deep-even primitive reduction。
>
> **严格状态：**generic descendant-only external support已经与 old `G_JB/Lambda_tail` companion pool严格分离，因此需要自己的 ordinary integer reader。本文直接把 dimensionless projective carrier `X_63^proj(u,v)` 代回真实整数 ratios `u=a_3/(TK)`、`v=Q^2N_0/(B^2K^2)`，清去统一 denominator，得到一个只含59个 composite monomials的 canonical integer `P_63`。其真实 endpoint值严格为正；完整二进 content为 `2^(16M+8m+58)`，positive primitive quotient恒为 `1 mod8`。于是 descendant-only external pool现在有了独立 natural carrier与 exact parity orientation，不再借用 `Lambda_tail`。本文尚未把 common-prime depth与该 carrier的 Archimedean height压成矛盾，因此不关闭 A2。

---

## 1. actual projective ratios

前一文件的 dimensionless variables可直接写成真实 integer blocks：

\[
\boxed{
u=\frac{a_3}{TK},}
\tag{1.1}
\]

\[
\boxed{
v=\frac{Q^2N_0}{B^2K^2}.}
\tag{1.2}
\]

这里

\[
N=10^M,
\qquad T=10^m,
\qquad B=b_2,
\qquad Q=B+2N,
\]

\[
K=9N+10A,
\qquad
N_0=(9B/2)^2+A^2.
\]

定义三个 positive blocks

\[
\boxed{R:=TK,\qquad X:=Q^2N_0,\qquad Y:=B^2K^2.}
\tag{1.3}
\]

于是

\[
u=a_3/R,
\qquad
v=X/Y.
\]

---

## 2. clear the projective carrier

`spontaneous-crt-pure-projective-carrier.md` 定义 primitive irreducible polynomial

\[
\boxed{
\mathscr X_{63}^{\rm proj}(u,v)
=\sum c_{ij}u^iv^j,}
\tag{2.1}

满足

\[
\deg_u=\deg_v=8,
\qquad
\deg_{\rm total}=11,
\qquad
\#\operatorname{supp}=59.
\]

定义 ordinary integer clearing

\[
\boxed{
\mathscr P_{63}
:=R^8Y^8
\mathscr X_{63}^{\rm proj}(a_3/R,X/Y).}
\tag{2.2}

展开仍只有同样59个 composite terms：

\[
\boxed{
\mathscr P_{63}
=\sum c_{ij}
 a_3^iR^{8-i}X^jY^{8-j}.}
\tag{2.3}

对于 genuine descendant-only external prime，`p` 与 `RY` 以及 fixed content `5^7 11^7` 分离，因此

\[
\boxed{p\mid\mathscr P_{63}.}
\tag{2.4}

这给新 external pool一个无需 branch-specific sphere denominator的 canonical integer reader。

---

## 3. real endpoint lies in a tiny positive projective box

已有 exact window

\[
\boxed{
\frac{937}{1000}<v<\frac{939}{1000}.}
\tag{3.1}

对 `u`，第三块 endpoint给

\[
1<\frac{a_3}{T}<\frac{251}{250},
\]
而

\[
K/N=9+y>\frac{2499}{250},
\qquad
N\ge10^{11}.
\]

所以

\[
0<u
<\frac{251}{2499}\,10^{-11}
<\frac1{1000}.
\tag{3.2}

因此真实 point 位于 rational rectangle

\[
\boxed{
\mathcal R_{\rm act}
=[0,1/1000]\times[937/1000,939/1000].}
\tag{3.3}

---

## 4. exact positivity of the projective carrier

将 `X_63^proj` 仿射搬到 unit square对应 (3.3)，再转成 bidegree `(8,8)` tensor Bernstein basis。

checker逐一验证全部81个 exact rational Bernstein coefficients严格为正。最小 coefficient仍为

\[
\boxed{
\frac{170202247140227961698711469574928714478754971}
{9313225746154785156250}>0.}
\tag{4.1}

所以 Bernstein convex-hull property给

\[
\boxed{
\mathscr X_{63}^{\rm proj}(u,v)>0
\qquad((u,v)\in\mathcal R_{\rm act}).}
\tag{4.2}

因为 `R,Y>0`，真实 dangerous endpoint上

\[
\boxed{\mathscr P_{63}>0.}
\tag{4.3}

---

## 5. exact binary depths of the blocks

当前 deep-even normal form给：

\[
\boxed{a_3\text{ odd},}
\tag{5.1}

因为 `b_3` 为偶且 `(a_3,b_3)=1`。

另外

\[
\boxed{v_2(R)=v_2(TK)=m+1,}
\tag{5.2}

因为 `v_2(T)=m`、`v_2(K)=1`。

对 `X`：

\[
Q=2^{M+1}Q_0,
\qquad Q_0,N_0\text{ odd},
\]
所以

\[
\boxed{v_2(X)=2M+2.}
\tag{5.3}

对 `Y`：

\[
v_2(B)=M+m+t,
\qquad v_2(K)=1,
\]
故

\[
\boxed{v_2(Y)=2M+2m+2t+2.}
\tag{5.4}

记

\[
\delta:=v_2(Y)-v_2(X)=2m+2t\ge16.
\tag{5.5}

---

## 6. unique lowest monomial

对 projective carrier coefficients做 exact audit。最高 `v` 次只有一个 monomial

\[
\boxed{c_{0,8}v^8,}
\]
其中

\[
\boxed{c_{0,8}=2^{34}3^{24}13^2.}
\tag{6.1}

对任意 support monomial `(i,j)`，(2.3) 的二进深度为

\[
v_2(c_{ij})
+(8-i)(m+1)
+j(2M+2)
+(8-j)(2M+2m+2t+2).
\]

抽出公共项

\[
8(m+1)+8(2M+2),
\]
剩余 extra depth 为

\[
\boxed{
\epsilon_{ij}
=v_2(c_{ij})-i(m+1)+(8-j)(2m+2t).}
\tag{6.2}

checker对全部59项验证：

1. `16-i-2j>=0`，所以 `epsilon_ij` 对 `m>=5` 不会下降；
2. `16-2j>=0`，所以对 `t>=3` 也不会下降；
3. 在最小 `(m,t)=(5,3)` 上，唯一 minimum 是
   \[
   \boxed{\epsilon_{0,8}=34,}
   \]
   第二浅层至少为
   \[
   \boxed{39.}
   \]

因此不存在 lowest-layer cancellation。

---

## 7. exact primitive orientation

由 §6：

\[
\boxed{
 v_2(\mathscr P_{63})
=8(m+1)+8(2M+2)+34
=16M+8m+58.}
\tag{7.1}

除去该完整二进 content，模 `8` 只剩 `(i,j)=(0,8)` 项：

\[
\frac{\mathscr P_{63}}{2^{16M+8m+58}}
\equiv
\frac{c_{0,8}}{2^{34}}
\left(\frac R{2^{m+1}}\right)^8
\left(\frac X{2^{2M+2}}\right)^8
\pmod8.
\]

三个括号均为 odd units，且 odd eighth power恒为 `1 mod8`。又

\[
\frac{c_{0,8}}{2^{34}}
=3^{24}13^2
\equiv1\pmod8.
\]

故

\[
\boxed{
\frac{\mathscr P_{63}}{2^{16M+8m+58}}
\equiv1\pmod8.}
\tag{7.2}

结合 (4.3)，这是 positive primitive `1 mod8` orientation。

---

## 8. parity role

`P_63` 的 positive primitive part为 `1 mod4`，所以其全部 `3 mod4` prime valuation总 parity为偶数。

这与 coefficient-singular low branch

\[
H_{V4}^\circ\equiv7\pmod8
\]
形成明确对照：

- generic descendant-only external natural carrier：`1 mod8`，parity-neutral；
- `H_4` coefficient singular escape：`7 mod8`，额外 odd-inert surcharge；
- `H_24` coefficient singular escape：`5 mod8`，total inert parity even。

所以 generic pool现在已有自己的 canonical reader与 exact orientation，但这仍没有证明某个 particular inert common prime不能整除 `P_63`。

---

## 9. updated frontier

`spontaneous-crt-descendant-companion-separation.md` 已证明 generic descendant-only external support不能借 `Lambda_tail` 付账。本文补上其独立 reader：

\[
\boxed{
\mathscr P_{63}>0,
\qquad
v_2(\mathscr P_{63})=16M+8m+58,
\qquad
\mathscr P_{63}^{\circ}\equiv1\pmod8.}
\]

下一步应把 `G_Delta` 的 actual external common depth与 `P_63` 的 valuation做 exact comparison；若能证明 `v_p(P_63)`只读取 first-layer/simple depth，而 `G_Delta` 需要 odd excess，就可能关闭 generic common-parity escape。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-quartic-tail-hierarchy"></a>

> 整合来源：`spontaneous-crt-descendant-quartic-tail-hierarchy.md`

# A2 descendant recycling 的 finite quartic tail hierarchy

> **依赖：** `spontaneous-crt-descendant-second-order-tail.md`、`spontaneous-crt-descendant-second-order-gcd-ladder.md`、`spontaneous-crt-descendant-transport-resonance.md`。
>
> **严格状态：**exact transported/Euclidean remainder对 parent errors `(F,L)` 的总次数最高只有4。本文把 cubic 与 quartic homogeneous blocks canonical 清分母，并递归定义 third tail `C_63^(3)` 与 terminal fourth tail `C_63^(4)`。每一层都用上一层 ordinary gcd saturation作为全局整数 divisor；由此得到完整四层 local valuation resolution：若某一 tail没有吞下完整 common baseline，则 actual remainder depth在该层立刻精确停止；连续三层都 full-saturated 后，terminal fourth tail读取**全部剩余 p-adic depth**，因为再无第五阶项。本文还证明 cubic/terminal parent numerators在真实 endpoint均严格为负；第三阶 positive primitive parent carrier为 `3 mod4`，额外携带 odd-inert parity，而 terminal positive primitive为 `5 mod8`。本文仍未排除 terminal modular roots，因此不关闭 A2。

---

## 1. exact degree of the transported remainder

沿用 parent errors

\[
F=K^2s_LY,
\qquad
L=s_L(X+Y),
\]
其中

\[
X=5^\lambda\mathscr R_{63}^\star,
\qquad
Y=g2^m\widehat{\mathscr D}_{63}.
\]

对 exact transported polynomial与 exact Euclidean quotient直接展开。checker验证 remainder只含 monomials

\[
F,\ L,\ F^2,\ FL,\ L^2,\ F^3,\ F^2L,\ L^3,\ F^4,\ L^4.
\]

所以

\[
\boxed{
M=M^{(1)}+M^{(2)}+M^{(3)}+M^{(4)},}
\tag{1.1}
\]

并且

\[
\boxed{M^{(n)}\text{ 对 }(X,Y)\text{ 齐次次数 }n.}
\tag{1.2}
\]

不存在 `M^(>=5)`。

---

## 2. primitive cubic and quartic forms

将 `s_L^n` 抽出后，exact coefficient audit给

\[
\boxed{
M^{(3)}
=s_L^3
\frac{8192\,\mathcal H_3(X,Y;K,\zeta)}
{5^5 11^5K^2},}
\tag{2.1}
\]

其中

\[
\boxed{
\deg_{X,Y}\mathcal H_3=3,
\quad
\deg_\zeta\mathcal H_3=2,
\quad
\#\operatorname{supp}=24.}
\tag{2.2}
\]

四阶更简单：

\[
\boxed{
M^{(4)}
=s_L^4
\frac{65536\,\mathcal H_4(X,Y)}{5^4 11^4},}
\tag{2.3}
\]

其中 exact

\[
\boxed{
\mathcal H_4(X,Y)
=2\cdot3^{12}\cdot13\,(X+Y)^4
+5^4 11^4Y^4.}
\tag{2.4}
\]

所以

\[
\boxed{\mathcal H_4>0}
\tag{2.5}
\]
对 positive parent coordinates无条件成立。

`H_3` 的 expanded 24 项由 checker canonical 重建。其 projective form在

\[
0<1/K<10^{-3},
\qquad
0<\zeta/K<10^{-3},
\qquad
0<X/Y<1/23
\]
上的全部 36 个 exact Bernstein coefficients严格为正：

\[
\boxed{
77742383923
\le b
\le
\frac{70017378306520823817}{760437500}.}
\tag{2.6}
\]

故真实 endpoint上

\[
\boxed{\mathcal H_3>0.}
\tag{2.7}
\]

---

## 3. recursive third-order integer

上一层定义

\[
\mathscr N_{63}^{(2)}
=U_2(M^{(1)}+M^{(2)}),
\]
其中 `U_2` 为 genuine p-unit rational scale。

定义

\[
\boxed{
\begin{aligned}
\mathscr N_{63}^{(3)}:={}&
5^mB^2\mathscr N_{63}^{(2)}\\
&+2^{4M+17}5^2 11^2T^6
\mathcal H_3(X,Y;K,a_3/T).
\end{aligned}}
\tag{3.1}
\]

直接代

\[
s_L=\frac{2^{2M+2}}{5^mB^2K^2}
\]
验证：

\[
\boxed{
\mathscr N_{63}^{(3)}
=U_3(M^{(1)}+M^{(2)}+M^{(3)}),}
\tag{3.2}
\]

其中

\[
U_3=(5^mB^2)U_2
\]
仍为 genuine p-unit rational scale。

定义

\[
S_1:=\gcd(G_\Delta,\mathscr B_{63}),
\qquad
S_2:=\gcd(G_\Delta,\mathscr C_{63}^{(2)}).
\tag{3.3}
\]

已有

\[
\mathscr N_{63}^{(2)}
=-G_\Delta S_1\mathscr C_{63}^{(2)}.
\]

所以第一行被 `G_Delta S_1 S_2` 整除。

第二行中 `H_3` 对 `(X,Y)` 齐次三次，而 `G_Delta|X,Y`；故被 `G_Delta^3` 整除。因为 `S_1,S_2|G_Delta`：

\[
\boxed{
G_\Delta S_1S_2
\mid\mathscr N_{63}^{(3)}.}
\tag{3.4}
\]

---

## 4. third-order real sign

写 reduced real parent ratio

\[
\chi=X/Y,
\qquad
w:=s_LY.
\]

由

\[
L=s_L(X+Y)=w(1+\chi)
\]
以及 actual projective box：

\[
0<w<L<\frac8{125}.}
\tag{4.1}
\]

令

\[
M^{(n)}=w^n h_n(K,\zeta,\chi).
\]

exact Bernstein bounds给

\[
\boxed{h_1<-350000,}
\tag{4.2}
\]

\[
\boxed{h_2<0,}
\tag{4.3}
\]

\[
\boxed{0<h_3<1500000.}
\tag{4.4}
\]

于是

\[
h_1+w h_2+w^2h_3
<h_1+\left(\frac8{125}\right)^2 1500000<0.
\]

故

\[
\boxed{
M^{(1)}+M^{(2)}+M^{(3)}<0,}
\tag{4.5}
\]
从 (3.2)：

\[
\boxed{\mathscr N_{63}^{(3)}<0.}
\tag{4.6}
\]

定义 positive third tail

\[
\boxed{
\mathscr C_{63}^{(3)}
:=-\frac{\mathscr N_{63}^{(3)}}{G_\Delta S_1S_2}
\in\mathbf Z_{>0}.}
\tag{4.7}
\]

---

## 5. recursive terminal fourth-order integer

定义

\[
S_3:=\gcd(G_\Delta,\mathscr C_{63}^{(3)}).
\tag{5.1}
\]

再定义 terminal integer

\[
\boxed{
\begin{aligned}
\mathscr N_{63}^{(4)}:={}&
5^mB^2\mathscr N_{63}^{(3)}\\
&+2^{6M+22}5^3 11^3T^6
\mathcal H_4(X,Y).
\end{aligned}}
\tag{5.2}
\]

同样直接代 `s_L` 与 (2.3)：

\[
\boxed{
\mathscr N_{63}^{(4)}
=U_4M,}
\tag{5.3}
\]

其中

\[
U_4=(5^mB^2)U_3
\]
为 genuine p-unit rational scale。这里使用了 (1.1)：四阶以后没有任何 remainder。

由 (4.7)，第一行被

\[
G_\Delta S_1S_2S_3
\]
整除；第二行因 `H_4` 齐次四次而被 `G_Delta^4` 整除。因此

\[
\boxed{
G_\Delta S_1S_2S_3
\mid\mathscr N_{63}^{(4)}.}
\tag{5.4}
\]

---

## 6. terminal real sign

(2.4) 给 `h_4>0`。actual ratio `chi<1/23` 还给粗但严格界

\[
\boxed{0<h_4<183000.}
\tag{6.1}
\]

结合 §4 与 `w<8/125`：

\[
\begin{aligned}
&h_1+w h_2+w^2h_3+w^3h_4\\
&< -350000
+\left(\frac8{125}\right)^2 1500000
+\left(\frac8{125}\right)^3 183000
<0.
\end{aligned}
\]

所以 exact full remainder在真实 endpoint满足

\[
\boxed{M<0,}
\tag{6.2}
\]
从而

\[
\boxed{\mathscr N_{63}^{(4)}<0.}
\tag{6.3}
\]

定义 positive terminal tail

\[
\boxed{
\mathscr C_{63}^{(4)}
:=-\frac{\mathscr N_{63}^{(4)}}
{G_\Delta S_1S_2S_3}
\in\mathbf Z_{>0}.}
\tag{6.4}
\]

---

## 7. exact recursive support laws

固定 genuine common prime，写

\[
h=v_p(G_\Delta),
\quad
\rho=v_p(B_{63}),
\quad
\sigma=v_p(C_{63}^{(2)}),
\quad
\tau=v_p(C_{63}^{(3)}),
\quad
\kappa=v_p(C_{63}^{(4)}).
\]

逐层使用 `S_i` 的定义，有：

### first unsaturated layer

若

\[
\rho<h,
\]
则已有

\[
\boxed{v_p(M)=h+\rho.}
\tag{7.1}
\]

### second unsaturated layer

若

\[
\rho\ge h,
\qquad
\sigma<h,
\]
则

\[
\boxed{v_p(M)=2h+\sigma.}
\tag{7.2}
\]

### third unsaturated layer

若

\[
\rho\ge h,
\qquad
\sigma\ge h,
\qquad
\tau<h,
\]
则 `N_63^(3)` 有 exact depth `3h+tau`，而 quartic block至少 `4h`，所以

\[
\boxed{v_p(M)=3h+\tau.}
\tag{7.3}
\]

### all first three layers saturated

若

\[
\rho\ge h,
\qquad
\sigma\ge h,
\qquad
\tau\ge h,
\]
则 denominator in (6.4)在 `p` 上恰为 `p^(4h)`。由于 `N_63^(4)=U_4M` 且 `U_4` 为 p-unit：

\[
\boxed{
v_p(M)=4h+\kappa.}
\tag{7.4}
\]

这里没有 truncation：四阶就是 terminal exact formula。

所以 entire p-adic depth被有限四层 ordinary tails完全解析：

\[
\boxed{
\begin{array}{c|c}
\rho<h & h+\rho,\\
\rho\ge h,\ \sigma<h & 2h+\sigma,\\
\rho,\sigma\ge h,\ \tau<h & 3h+\tau,\\
\rho,\sigma,\tau\ge h & 4h+\kappa.
\end{array}}
\tag{7.5}
\]

因此**不再存在未显式记录的 fifth-order normalized unit**。

---

## 8. third-order 2-adic parity surcharge

`H_3` 清 `T^6` 后，checker验证唯一最低 binary monomial为

\[
\boxed{
-8800610472\,X^3\zeta^2
=-2^3 3^8\cdot107\cdot1567\,X^3\zeta^2.}
\tag{8.1}
\]

对应 ordinary term为

\[
-2^3 3^8\cdot107\cdot1567\,X^3a_3^2T^4.
\]

其它23项在 `(m,t)=(5,3)` 已至少更深6层，且相对 slopes非负。因此 (3.1) cubic block唯一控制 `N_63^(3)` 的最低 binary layer；第一行额外至少深 `2t>=6`。

于是

\[
\boxed{
v_2(\mathscr N_{63}^{(3)})
=4M+4m+20.}
\tag{8.2}

除去该幂后：

\[
\frac{\mathscr N_{63}^{(3)}}{2^{4M+4m+20}}
\equiv3X\pmod8.
\tag{8.3}

已有

\[
X=5^\lambda Rstar,
\qquad
Rstar\equiv3\pmod4,
\]
所以

\[
X\equiv3\pmod4.
\]
故 (8.3) 给

\[
\boxed{
\frac{\mathscr N_{63}^{(3)}}{2^{4M+4m+20}}
\equiv1\pmod4.}
\tag{8.4}

结合 `N_63^(3)<0`：

\[
\boxed{
\frac{-\mathscr N_{63}^{(3)}}{2^{4M+4m+20}}
\equiv3\pmod4.}
\tag{8.5}

所以 third-order positive parent numerator必含 odd number of `3 mod4` prime valuations：连续两层 full-baseline saturation进入三阶时会产生一份新的 odd-inert parity surcharge。

---

## 9. terminal 2-adic orientation

`H_4` 中 `Y` 带额外 binary depth，唯一最低项是

\[
2\cdot3^{12}\cdot13\,X^4.
\]

清 `T^6` 后仍唯一最低。由 (5.2)：

\[
\boxed{
v_2(\mathscr N_{63}^{(4)})
=6M+6m+23.}
\tag{9.1}
\]

第一行至少再深

\[
2t-3\ge3
\]
层。

primitive residue为

\[
5^3 11^3\cdot3^{12}\cdot13
\equiv3\pmod8,
\]
且 `X^4`、`(T/2^m)^6` 都为 `1 mod8`。所以

\[
\boxed{
\frac{\mathscr N_{63}^{(4)}}{2^{6M+6m+23}}
\equiv3\pmod8.}
\tag{9.2}

结合 negativity：

\[
\boxed{
\frac{-\mathscr N_{63}^{(4)}}{2^{6M+6m+23}}
\equiv5\pmod8.}
\tag{9.3}

terminal positive parent numerator的 total inert parity因此为偶数。

---

## 10. revised descendant frontier

same-prime descendant recycling现在已经不再有无限-order local ambiguity。所有 depth都由

\[
\boxed{
B_{63},\quad
C_{63}^{(2)},\quad
C_{63}^{(3)},\quad
C_{63}^{(4)}}
\]
四个 ordinary integers递归读取；第四个是 terminal exact tail。

真正 generic branch若想连续跨越前三个 common baselines，必须同时满足

\[
\boxed{
\rho\ge h,
\qquad
\sigma\ge h,
\qquad
\tau\ge h,}
\]
并且此过程还伴随 §8 的 new odd-inert third-order surcharge。

下一步最值得做的已经不是继续 Taylor expansion，而是：

1. 审计 third-order surcharge能否由原 `G_Delta` / target / source pools复用；
2. 在 fully saturated branch上研究 terminal `C_63^(4)` 与 parent coordinates的 gcd；
3. 或把 simple quartic coefficient (2.4) 与 first-order balance ratio联立，得到 terminal saturation的固定 algebraic gate。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-quotient-gate"></a>

> 整合来源：`spontaneous-crt-descendant-quotient-gate.md`

# A2 descendant projective Euclidean quotient gate 的 parity charge 与 overdepth split

> **依赖：** `spontaneous-crt-descendant-linear-depth-reader.md`、`spontaneous-crt-descendant-projective-depth-reader.md`。
>
> **严格状态：**generic same-prime recycling 现在只需理解 linear remainder `M_63=E_proj-Q_63 L_proj` 是否比 common baseline 更深。本文先隔离 Euclidean quotient `Q_63`：清去固定 `5^7 11^7` denominator后得到 degree-6、50项的 integer projective polynomial `Q#`，它在真实 `(r,u,v)` box严格为正。清回 decimal blocks得到 positive ordinary integer `Q_63^int`，完整二进 depth为 `6M+6m+29`，primitive unit恒为 `3 mod8`。因此 quotient-singular prime并非免费 exception；该 gate自身携带 odd-inert parity。另一方面 valuation split说明 `p|Q_63` 本身不会制造 baseline-level cancellation：若 `v_p(Q_63)>0`，linear remainder overdepth必先要求 upstream `E_proj` 已 overdeep。于是 generic closure可继续集中到 upstream transported-error resonance。本文仍未排除该 resonance，因此不关闭 A2。

---

## 1. projective Euclidean quotient

沿用 exact division

\[
\boxed{
\mathscr E_{\rm proj}
=\mathscr Q_{63}\mathscr L_{\rm proj}
+\mathscr M_{63}.}
\tag{1.1}

其中

\[
\mathscr L_{\rm proj}
=55r^2+18(u-1)r+1-4u-v,
\]

\[
\mathscr M_{63}=A(u,v)r+B(u,v).
\]

Euclidean quotient满足

\[
\boxed{
\deg_r\mathscr Q_{63}=6,
\quad
\deg_u\mathscr Q_{63}=6,
\quad
\deg_v\mathscr Q_{63}=3,}
\tag{1.2}

\[
\boxed{
\deg_{\rm total}\mathscr Q_{63}=6,
\qquad
\#\operatorname{supp}(\mathscr Q_{63})=50.}
\tag{1.3}

全部 rational coefficient的共同 denominator仍恰为

\[
\boxed{D_0=5^7 11^7.}
\tag{1.4}

定义 integer projective quotient

\[
\boxed{
\mathscr Q_{63}^\#:=D_0\mathscr Q_{63}
\in\mathbf Z[r,u,v].}
\tag{1.5}

---

## 2. exact positivity on the real endpoint box

实际变量满足更强窗口，但本文只使用宽松 rational box

\[
\boxed{
0<r<\frac1{1000},
\qquad
0<u<\frac1{1000},
\qquad
\frac{937}{1000}<v<\frac{939}{1000}.}
\tag{2.1}

把 `Q#` 仿射搬到 unit cube，并转成 tensor Bernstein basis。其 bidegrees为 `(6,6,3)`，所以共有

\[
7\cdot7\cdot4=196
\]
个 exact rational Bernstein coefficients。checker验证全部严格为正，且

\[
\boxed{
\min b_{ijk}
=
\frac{10423408247410155008672}{15625}>0,}
\tag{2.2}

\[
\boxed{
\max b_{ijk}
=
\frac{10299944552027210611196952289529}
{15258789062500}.}
\tag{2.3}

因此真实 dangerous endpoint上

\[
\boxed{\mathscr Q_{63}^\#>0.}
\tag{2.4}

---

## 3. clear to an ordinary integer

继续用

\[
R:=TK,
\qquad
X:=Q^2N_0,
\qquad
Y:=B^2K^2,
\]
并注意

\[
r=1/K=T/R,
\qquad
u=a_3/R,
\qquad
v=X/Y.
\]

因为 `deg_(r,u)<=6`、`deg_v<=3`，定义 compact ordinary integer

\[
\boxed{
\mathscr Q_{63}^{\rm int}
:=R^6Y^3
\mathscr Q_{63}^\#(T/R,a_3/R,X/Y).}
\tag{3.1}

它仍只有50个 composite monomials。由 (2.4) 及 `R,Y>0`：

\[
\boxed{\mathscr Q_{63}^{\rm int}>0.}
\tag{3.2}

对 genuine external prime `p\nmid5\cdot11RY`：

\[
\boxed{
v_p(\mathscr Q_{63}^{\rm int})
=v_p(\mathscr Q_{63}).}
\tag{3.3}

所以 quotient-singular support也有 canonical ordinary integer reader。

---

## 4. exact 2-adic depth

若 `Q#` 中 monomial为

\[
q_{abj}r^au^bv^j,
\]
则清回 (3.1) 后对应

\[
q_{abj}T^a a_3^bR^{6-a-b}X^jY^{3-j}.
\]

已有

\[
v_2(T)=m,
\quad
v_2(a_3)=0,
\quad
v_2(R)=m+1,
\]

\[
v_2(X)=2M+2,
\quad
v_2(Y)=2M+2m+2t+2.
\]

checker对全部50项审计。唯一最低项为

\[
\boxed{(a,b,j)=(0,0,3),}
\tag{4.1}

其 coefficient为

\[
\boxed{
q_{003}
=150659459039232000
=2^{17}3^{12}5^3 11^3 13.}
\tag{4.2}

对应 depth

\[
17+6(m+1)+3(2M+2)
=6M+6m+29.
\]

所有其它项相对该层的 `m,t` slopes均非负；在最小 `(m,t)=(5,3)` 已至少再深3层。因此

\[
\boxed{
v_2(\mathscr Q_{63}^{\rm int})
=6M+6m+29.}
\tag{4.3}

---

## 5. positive primitive orientation is `3 mod 8`

除去完整二进 content，模8只剩 (4.1) 项：

\[
\frac{\mathscr Q_{63}^{\rm int}}
{2^{6M+6m+29}}
\equiv
\frac{q_{003}}{2^{17}}
\left(\frac R{2^{m+1}}\right)^6
\left(\frac X{2^{2M+2}}\right)^3
\pmod8.
\]

第一 factor满足

\[
q_{003}/2^{17}\equiv3\pmod8.
\]

又 `R/2^(m+1)` 为 odd，故六次幂为 `1 mod8`。同时

\[
X/2^{2M+2}=Q_0^2N_0.
\]

`Q_0` 为 odd，所以 `Q_0^2≡1 mod8`；而 `A=a_2` 为 odd、`B/2` 被4整除，故

\[
N_0=(9B/2)^2+A^2\equiv1\pmod8.
\]

因此

\[
\boxed{
\mathscr Q_{63}^{\rm int}/2^{6M+6m+29}
\equiv3\pmod8.}
\tag{5.1}

结合 (3.2)，这是 positive primitive `3 mod8` carrier。故 quotient-singular gate自身必带一份 odd-inert parity。

---

## 6. quotient valuation does not create baseline cancellation by itself

固定 descendant-only common prime，记

\[
k=k_p,
\quad
q=v_p(\mathscr Q_{63}),
\quad
\ell=v_p(\mathscr L_{\rm proj}),
\]

\[
e=v_p(\mathscr E_{\rm proj}),
\quad
\mu=v_p(\mathscr M_{63}).
\]

已有

\[
\ell,e,\mu\ge k.
\]

由 exact division (1.1)：

\[
\mathscr M_{63}
=\mathscr E_{\rm proj}
-\mathscr Q_{63}\mathscr L_{\rm proj}.
\tag{6.1}

### `q>0`

此时

\[
q+\ell>k.
\]

若 `e=k`，两项 depth不同，故

\[
\boxed{\mu=k.}
\tag{6.2}

所以

\[
\boxed{q>0,\ \mu>k\Longrightarrow e>k.}
\tag{6.3}

quotient singularity本身不会制造 baseline overdepth；它只能伴随 upstream `E_proj` 已 overdeep。

### `q=0`

若

\[
e\ne\ell,
\]
则两项 depth不同：

\[
\boxed{\mu=\min(e,\ell).}
\tag{6.4}

因此 `mu>k` 只可能来自：

1. `min(e,ell)>k`；或
2. `e=ell=k`，并发生 normalized cancellation
   \[
   \boxed{
   E_0\equiv Q_0L_0\pmod p.}
   \tag{6.5}
   \]

这里 `E=p^kE_0`、`L=p^kL_0`、`Q=Q_0`，三者 normalized units。

---

## 7. revised overdepth frontier

same-prime linear-tail recycling现在只有三类输入：

1. upstream transported error本身已 overdeep：`e>k`；
2. generic unit-quotient equal-depth resonance (6.5)；
3. quotient-singular gate `p|Q_63`，但该 gate自身由 positive primitive `3 mod8` integer收费，而且仍需 `e>k` 才能让 `M_63` overdeep。

所以 quotient factor已经从“潜在第三种自由 cancellation source”降成一个带独立 parity surcharge的显式 gate。下一步应直接分析 `e=v_p(E_proj)>k` 的 transported-error条件。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-second-order-balance"></a>

> 整合来源：`spontaneous-crt-descendant-second-order-balance.md`

# A2 descendant balance saturation 的 second-order coefficient 与 fixed degree-110 gate

> **依赖：** `spontaneous-crt-descendant-balance-gcd-ladder.md`、`spontaneous-crt-descendant-balance-tail.md`、`spontaneous-crt-descendant-transport-resonance.md`。
>
> **严格状态：**balance gcd ladder 已证明：若 `h=v_p(G_Delta)`、`rho=v_p(B_63)`，则 `rho<h` 时 linear remainder depth精确为 `h+rho`；只有 `rho>=h` 时 quadratic transport才可能参与。本文把 exact rational-root transport与 Euclidean quotient展开到二阶，并在 first-order recycling ratio `chi=chi_geom` 上化简。second-order coefficient的 denominator只含 `81 K^4 G_<^2`，numerator是 primitive total-degree-16 polynomial `S_2(K,zeta)`。它与 universal cubic消去 `zeta` 后精确只剩 central `(2K-9)^8` 与一个 irreducible degree-110 pure-K gate `P_110(K)`。因此当 `rho>h` 时，若 actual remainder还要越过 `2h`，genuine noncentral prime必须命中 `P_110`；没有新的 moving second-order unit。`rho=h` 时 linear balance unit与 quadratic coefficient恰同处 `2h`，仍留下一个 normalized second-order cancellation，这成为下一层唯一 generic自由。本文不排除 `P_110` 的 modular roots，也未关闭 `rho=h` cancellation，因此不关闭 A2。

---

## 1. exact quadratic transported term

沿用 first-layer point

\[
J_0=J+F/U,
\qquad
R_0=R+K^2L,
\qquad
U=2K-9,
\]

其中

\[
F=F_\Delta,
\qquad
L=\mathscr L_{\rm proj}.
\]

写

\[
C_{tr}:=\frac{65536U^4}{K^8}.
\]

exact transported error为

\[
E_{proj}
=C_{tr}
\left[
\Phi(J_0,R_0)-\Phi(J_0-F/U,R_0-K^2L)
\right].
\]

Euclidean remainder满足

\[
M=E_{proj}-Q(r,u,v_0-L)L,
\]
其中 `v_0=R_0/K^2`。

在 `(F,L)` 中取 total degree 2 的 homogeneous part，直接 Taylor 展开得到

\[
\boxed{
\begin{aligned}
M^{(2)}={}&C_{tr}
\left[
-\frac{\Phi_{JJ}(J_0,R_0)}{2U^2}F^2
+\frac{2(J_0+\zeta)K^2}{U}FL
\right]\\
&+Q_v(r,u,v_0)L^2.
\end{aligned}}
\tag{1.1}

这里 `Phi` 对 `R` 仅一次，所以没有 transported `L^2` 项；最后的 `L^2` 完全来自 Euclidean quotient对 `v` 的变化。

---

## 2. normalize by the homogeneous parent coordinates

balance-tail chain给 exact parent errors

\[
F=K^2s_LY,
\qquad
L=s_L(X+Y),
\]
其中

\[
X=5^\lambda Rstar,
\qquad
Y=g2^mDhat,
\]
且 `s_L` 为 genuine p-unit scale。

在 equal parent depth处写

\[
\chi:=X/Y.
\]

从 (1.1) 抽出 `s_L^2Y^2` 后，quadratic coefficient为

\[
\boxed{
\begin{aligned}
\mathcal Q_2(K,\zeta;\chi):={}&
C_{tr}\left[
-\frac{\Phi_{JJ,0}}{2U^2}K^4
+\frac{2(J_0+\zeta)K^4}{U}(\chi+1)
\right]\\
&+Q_{v,0}(\chi+1)^2,
\end{aligned}}
\tag{2.1}

其中

\[
\Phi_{JJ,0}=\Phi_{JJ}(J_0,R_0),
\]

\[
Q_{v,0}
=\partial_vQ_{63}(1/K,\zeta/K,R_0/K^2).
\]

first-order same-prime recycling已经唯一固定

\[
\boxed{
\chi_{geom}
=-\frac{2\mathcal G_>}{81\mathcal G_<}.}
\tag{2.2}

---

## 3. second-order coefficient has no new denominator gate

将 (2.2) 代入 (2.1)。exact simplification给

\[
\boxed{
\mathcal Q_2(K,\zeta;\chi_{geom})
=
\frac{256\,\mathcal S_2(K,\zeta)}
{81K^4\mathcal G_<^2}.}
\tag{3.1}

其中 `S_2` 取 primitive integer normalization，满足

\[
\boxed{
\deg_{total}\mathcal S_2=16,
\qquad
\deg_\zeta\mathcal S_2=14,}
\tag{3.2}

\[
\boxed{
\#\operatorname{supp}(\mathcal S_2)=150.}
\tag{3.3}

所以二阶 normalization没有产生第三张 denominator sheet；唯一 denominator正是 first-order gate `G_<` 的平方，加上 genuine unit `K`。

---

## 4. eliminate `zeta`: only a central factor and one degree-110 gate

对 `S_2` 与 universal cubic

\[
\mathcal E_{63}(K,\zeta)=0
\]
关于 `zeta` 求 exact resultant。得到

\[
\boxed{
\operatorname{Res}_{\zeta}
(\mathcal E_{63},\mathcal S_2)
=-2^{140}3^{11}(2K-9)^8P_{110}(K).}
\tag{4.1}

其中

\[
\boxed{\deg P_{110}=110,}
\tag{4.2}

并且

\[
\boxed{P_{110}\text{ 在 }\mathbf Q[K]\text{ 中不可约}.}
\tag{4.3}

`P_110` 有111个 nonzero coefficients。正文不抄写巨大系数；checker从 (2.1)--(3.1) canonical 重建 `S_2` 与 resultant，并验证 fixed content、degree与不可约性。

因此 genuine noncentral second-order coefficient若消失，只能进入

\[
\boxed{P_{110}(K)\equiv0\pmod p.}
\tag{4.4}

---

## 5. the second-order coefficient has no real endpoint zero

定义 projective form

\[
\boxed{
\mathcal S_2^{proj}(r,u)
:=r^{16}\mathcal S_2(1/r,u/r).}
\tag{5.1}

它仍有150个 monomials，bidegrees为

\[
\boxed{\deg_r=16,\qquad\deg_u=14.}
\tag{5.2}

真实 endpoint满足

\[
0<r<10^{-3},
\qquad
0<u<10^{-3}.
\]

把 (5.1) 仿射搬到 `[0,1]^2` 并转成 tensor Bernstein basis，共

\[
17\cdot15=255
\]
个 exact rational coefficients。checker验证全部严格为正；其中

\[
\boxed{
\min b_{ij}
=
\frac{198730569009592634141902074605524422074200621380891689557678786752875433}
{3725290298461914062500000000000000000000}>0,}
\tag{5.3}

\[
\boxed{
\max b_{ij}
=162937721250850407546364808657801>0.}
\tag{5.4}

所以

\[
\boxed{
\mathcal S_2(K,\zeta)>0}
\tag{5.5}

在整个真实 dangerous endpoint成立。second-order gate没有 real degeneration；任何 modular root只能来自 p-adic wrapping。

---

## 6. depth trichotomy at the saturated balance layer

继续固定 common baseline

\[
h=v_p(G_\Delta),
\]
及 balance depth

\[
\rho=v_p(B_{63}).
\]

前一 gcd-ladder theorem已证明：

\[
M=M^{(1)}+M^{(\ge2)},
\qquad
v_p(M^{(1)})=h+\rho,
\qquad
v_p(M^{(\ge2)})\ge2h.
\]

### `rho<h`

已有 exact law

\[
\boxed{v_p(M)=h+\rho.}
\tag{6.1}

### `rho>h`

此时

\[
v_p(M^{(1)})>2h.
\]

quadratic term独占可能的 `2h` 层。若 coefficient regular，即

\[
p\nmid K\mathcal G_<,
\]
则

\[
\boxed{
p\nmid\mathcal S_2
\Longrightarrow
v_p(M)=2h.}
\tag{6.2}

因此若

\[
\boxed{\rho>h,\qquad v_p(M)>2h,}
\tag{6.3}

则 genuine noncentral prime必须满足

\[
\boxed{p\mid P_{110}(K).}
\tag{6.4}

### `rho=h`

此时 linear balance term与 quadratic transported term都恰可能处在 `2h` 层。因此还留下一个 normalized second-order cancellation：

\[
\boxed{
\frac{M^{(1)}}{p^{2h}}
+rac{M^{(2)}}{p^{2h}}
\equiv0\pmod p.}
\tag{6.5}

这是当前唯一仍含一个新 normalized unit的 generic second-order branch。

---

## 7. revised second-order frontier

balance saturation现在进一步分成：

- `rho<h`：depth已完全读取；
- `rho>h`：越过 `2h` 只能命中 fixed irreducible `P_110`；
- `rho=h`：恰一整个 baseline 的 balance saturation，留下唯一 second-order normalized cancellation。

因此真正无界 unit自由已经从

\[
\rho\ge h
\]
进一步缩成

\[
\boxed{\rho=h.}
\]

这与 earlier equal-depth bottlenecks再次同型：**过深反而固定化，恰等深才保留 normalized resonance。**

下一步应为 `rho=h` 定义 canonical second-order balance unit / tail，而不再扩大 `P_110` 的 ordinary discriminant分析。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-second-order-gcd-ladder"></a>

> 整合来源：`spontaneous-crt-descendant-second-order-gcd-ladder.md`

# A2 descendant recycling 的 nested second-order gcd ladder

> **依赖：** `spontaneous-crt-descendant-balance-gcd-ladder.md`、`spontaneous-crt-descendant-second-order-tail.md`。
>
> **严格状态：**first balance tail `B_63` 读取 `h` 到 `2h` 之间的全部 depth；second-order tail `C_63^(2)` 已精确选择 saturated balance branch中越过 `2h` 的 labels。本文继续利用 exact degree filtration：linear+quadratic block的 local depth由 `C_63^(2)` 精确读取，而所有 cubic 及更高 transport项至少有 `3h` 层。因此在 `rho>=h` 后，`C_63^(2)` 又精确读取第二个完整 baseline以内的所有 extra depth；只有它自身再吞下完整 `p^h` 时三阶 transport才有资格参与。于是 descendant recycling形成两级 ordinary gcd ladder，而真正 generic unit自由被推进到连续两次 full-baseline saturation之后。本文尚未计算 third-order coefficient，因此不关闭 A2。

---

## 1. notation

固定 genuine common prime `p`，写

\[
\boxed{h:=v_p(G_\Delta)\ge1,}
\tag{1.1}
\]

first balance depth

\[
\boxed{\rho:=v_p(\mathscr B_{63}),}
\tag{1.2}
\]

以及 canonical second-order tail depth

\[
\boxed{\sigma:=v_p(\mathscr C_{63}^{(2)}).}
\tag{1.3}
\]

上一文件已证明

\[
p\mid\mathscr C_{63}^{(2)}
\Longleftrightarrow
\rho\ge h
\text{ and }
v_p(M)>2h.
\]

所以 `sigma` 只在 first balance 已饱和的 branch上承担 actual second-order意义。

---

## 2. exact depth of the linear+quadratic block

定义

\[
M_{\le2}:=M^{(1)}+M^{(2)}.
\]

`spontaneous-crt-descendant-second-order-tail.md` 构造 p-unit rational scale `U_2`，使

\[
\mathscr N_{63}^{(2)}=U_2 M_{\le2},
\]
并定义

\[
\mathscr C_{63}^{(2)}
=-\frac{\mathscr N_{63}^{(2)}}{G_\Delta S_{bal}},
\qquad
S_{bal}=\gcd(G_\Delta,\mathscr B_{63}).
\]

若

\[
\boxed{\rho\ge h,}
\tag{2.1}
\]
则

\[
v_p(S_{bal})=h,
\]
所以

\[
v_p(G_\Delta S_{bal})=2h.
\]
由于 `U_2` 为 p-unit：

\[
\boxed{
v_p(M_{\le2})
=2h+\sigma.}
\tag{2.2}
\]

这不是 truncated inequality，而是 exact equality。

---

## 3. every omitted term starts at the third baseline

exact transport/Euclidean expansion按 parent errors `(F,L)` 总次数分级：

\[
M=M^{(1)}+M^{(2)}+M^{(\ge3)}.
\]

common baseline给

\[
v_p(F)\ge h,
\qquad
v_p(L)\ge h.
\]

每个 `M^(>=3)` monomial总次数至少3，因此

\[
\boxed{
v_p(M^{(\ge3)})\ge3h.}
\tag{3.1}
\]

---

## 4. exact second-baseline valuation law

继续假设 `rho>=h`。

### `sigma<h`

由 (2.2)：

\[
2h+\sigma<3h.
\]

所以 `M_<=2` 是唯一最浅 block；由 (3.1) 不可能发生跨阶 cancellation：

\[
\boxed{
v_p(M)=2h+\sigma.}
\tag{4.1}
\]

### `sigma>=h`

此时

\[
v_p(M_{\le2})\ge3h,
\]
且 higher block也至少 `3h`，故

\[
\boxed{
v_p(M)\ge3h.}
\tag{4.2}

统一写成

\[
\boxed{
\min\{v_p(M),3h\}
=2h+\min\{\sigma,h\}
\qquad(\rho\ge h).}
\tag{4.3}
\]

或等价地

\[
\boxed{
\min\{v_p(M)-2h,h\}
=\min\{v_p(\mathscr C_{63}^{(2)}),h\}.}
\tag{4.4}
\]

所以 `C_63^(2)` 精确读取第二个完整 baseline以内的全部 remainder depth。

---

## 5. second-order gcd ladder

对 `j>=1` 定义

\[
\boxed{
D_j^{(2)}
:=\gcd(G_\Delta^j,\mathscr C_{63}^{(2)}).}
\tag{5.1}
\]

逐 common prime：

\[
\boxed{
v_p(D_j^{(2)})=\min(jh,\sigma).}
\tag{5.2}
\]

因此 stable ladder读取 second-order tail上的完整 local exponent `sigma`。

真正 third-order dangerous layer是

\[
\boxed{
\rho\ge h,
\qquad
\sigma\ge h.}
\tag{5.3}
\]

即 first 与 second tail连续各吞下至少一个完整 common baseline。

---

## 6. nested tropical law

结合 first balance ladder，generic common prime现在满足严格三段式：

\[
\boxed{
\begin{array}{c|c}
\rho<h
&v_p(M)=h+\rho,\\[2mm]
\rho\ge h,\ \sigma<h
&v_p(M)=2h+\sigma,\\[2mm]
\rho\ge h,\ \sigma\ge h
&v_p(M)\ge3h.
\end{array}}
\tag{6.1}
\]

前两行已经没有 normalized-unit自由。

注意此前 second-order coefficient theorem还给：若 `rho>h` 且第二行继续失败、即越过 `2h`，则 prime必须命中 fixed `P_110(K)`。所以真正 generic moving frontier更窄地位于

\[
\boxed{
\rho=h,
\qquad
\sigma\ge h.}
\tag{6.2}
\]

这与 earlier omega-height / first descendant balance 的 equal-depth现象完全同型：只有**恰 baseline saturation**反复保留新的 normalized resonance。

---

## 7. next frontier

目前 descendant same-prime recycling 已有：

1. `B_63` first tail；
2. `C_63^(2)` second tail；
3. 两层 ordinary gcd ladders；
4. exact depth laws直到 `3h`。

所以下一步不应回到 first/second-order ordinary resultant。真正有价值的是在

\[
\rho=h,
\qquad
\sigma\ge h
\]
上构造 cubic transported coefficient与 canonical third-order tail，或者证明这两个 full-baseline saturation不能同时由 generic external prime承担。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-second-order-tail"></a>

> 整合来源：`spontaneous-crt-descendant-second-order-tail.md`

# A2 descendant recycling 的 canonical second-order tail

> **依赖：** `spontaneous-crt-descendant-balance-tail.md`、`spontaneous-crt-descendant-balance-gcd-ladder.md`、`spontaneous-crt-descendant-second-order-balance.md`。
>
> **严格状态：**first-order balance tail `B_63` 已读取一个完整 common baseline 以内的全部 recycling depth；此前唯一 generic unit 自由停在 `rho=v_p(B_63)=h=v_p(G_Delta)`。本文把 exact linear 与 quadratic transported terms一起清分母，构造 ordinary integer `N_63^(2)`。令 `S_bal=gcd(G_Delta,B_63)`，则 `G_Delta S_bal | N_63^(2)` 全局成立；正 quotient `C_63^(2)` 精确选择“balance 已至少饱和一个 baseline 且 actual remainder 越过 `2h`”的 common primes。于是 `rho=h` 的 normalized second-order cancellation不再是手工 p-adic unit equation，而由普通 gcd `gcd(G_Delta,C_63^(2))` canonical 读取。本文还证明 parent numerator严格为负，其正相反数的 primitive 2-adic orientation为 `1 mod 8`。本文没有关闭 `rho=h` 的 modular roots，因此不关闭 A2。

---

## 1. parent notation

沿用 fully primitive parent coordinates

\[
X:=5^\lambda\mathscr R_{63}^\star,
\qquad
Y:=g2^m\widehat{\mathscr D}_{63},
\]

\[
G_\Delta:=\gcd(X,Y)
=\gcd(\mathscr R_{63}^\star,\widehat{\mathscr D}_{63}).
\]

first-order fixed gates清 third denominator后记为

\[
\mathfrak G_<:=T^6\mathcal G_<(K,a_3/T),
\qquad
\mathfrak G_>:=T^6\mathcal G_>(K,a_3/T).
\]

真实 endpoint上已有

\[
\boxed{\mathfrak G_<<0,\qquad \mathfrak G_><0.}
\tag{1.1}
\]

balance tail为

\[
\boxed{
\mathscr B_{63}
=-\frac{81X\mathfrak G_<+2Y\mathfrak G_>}{G_\Delta}
>0.}
\tag{1.2}
\]

定义 truncated saturation gcd

\[
\boxed{
S_{bal}:=\gcd(G_\Delta,\mathscr B_{63}).}
\tag{1.3}
\]

逐 genuine common prime `p`，写

\[
h:=v_p(G_\Delta)\ge1,
\qquad
\rho:=v_p(\mathscr B_{63}),
\]
则

\[
\boxed{v_p(S_{bal})=\min(h,\rho).}
\tag{1.4}
\]

---

## 2. primitive quadratic transported numerator

`spontaneous-crt-descendant-second-order-balance.md` 定义 exact quadratic coefficient

\[
\mathcal Q_2(K,\zeta;\chi)
\]
使 equal-parent normalization中的 quadratic term为

\[
s_L^2Y^2\mathcal Q_2(K,\zeta;X/Y).
\]

对 `X,Y` 齐次化。exact denominator audit给唯一 primitive polynomial

\[
\boxed{
\mathcal H_2(X,Y;K,\zeta)\in\mathbf Z[X,Y,K,\zeta]}
\tag{2.1}
\]
满足

\[
\boxed{
Y^2\mathcal Q_2(K,\zeta;X/Y)
=
\frac{256\,\mathcal H_2(X,Y;K,\zeta)}
{5^5 11^6 K^4}.}
\tag{2.2}
\]

其结构为

\[
\boxed{
\deg_{X,Y}\mathcal H_2=2,
\qquad
\deg_\zeta\mathcal H_2=4,
\qquad
\#\operatorname{supp}=45.}
\tag{2.3}
\]

`H_2` 的完整 coefficients由 checker从 exact Taylor formula canonical 重建，正文不抄机械 45 项。

---

## 3. clear the linear and quadratic terms simultaneously

first-order exact term为

\[
M^{(1)}
=
\frac{64s_L}{5^7 11^7K^6T^6}
\left(81X\mathfrak G_<+2Y\mathfrak G_>\right).
\tag{3.1}
\]

quadratic exact term为

\[
M^{(2)}=s_L^2Y^2\mathcal Q_2(K,\zeta;X/Y).
\tag{3.2}
\]

定义 ordinary integer

\[
\boxed{
\begin{aligned}
\mathscr N_{63}^{(2)}:={}&
64\,5^mB^2
\left(81X\mathfrak G_<+2Y\mathfrak G_>\right)\\
&+2^{2M+10}5^2\cdot11\,T^6
\mathcal H_2(X,Y;K,a_3/T).
\end{aligned}}
\tag{3.3}
\]

`T^6 H_2(K,a_3/T)` 为整数，因为 `deg_zeta H_2<=4`。

令

\[
D_0:=5^7 11^7K^6.
\]

直接代

\[
s_L=\frac{2^{2M+2}}{5^mB^2K^2}
\]
与 (2.2)，得到 exact rational scaling

\[
\boxed{
\mathscr N_{63}^{(2)}
=
\frac{5^mB^2D_0T^6}{s_L}
\left(M^{(1)}+M^{(2)}\right).}
\tag{3.4}
\]

右侧 prefactor在 genuine non-`2,5,11`, noncentral external prime上是 p-unit，因此 `N_63^(2)` 无损读取 linear+quadratic remainder depth。

---

## 4. a global integer divisor `G_Delta S_bal`

由 (1.2)：

\[
81X\mathfrak G_<+2Y\mathfrak G_>
=-G_\Delta\mathscr B_{63}.
\]

所以 (3.3) 第一项被

\[
G_\Delta S_{bal}
\]
整除，因为 `S_bal|B_63`。

另一方面 `H_2` 对 `(X,Y)` 齐次二次，而

\[
G_\Delta\mid X,
\qquad
G_\Delta\mid Y.
\]
故第二项被 `G_Delta^2` 整除。又 `S_bal|G_Delta`，所以同样被 `G_Delta S_bal` 整除。

因此得到全局 ordinary divisibility：

\[
\boxed{
G_\Delta S_{bal}\mid\mathscr N_{63}^{(2)}.}
\tag{4.1}
\]

---

## 5. real sign: both first and quadratic pieces are negative

第一项 bracket由 (1.1) 与 `X,Y>0` 立即严格为负。

对 quadratic piece，projectivize

\[
r=1/K,
\qquad
u=\zeta/K,
\qquad
\chi=X/Y.
\]

真实 endpoint已有

\[
0<r<10^{-3},
\qquad
0<u<10^{-3},
\qquad
0<\chi<1/23.
\]

将 (2.2) 的 numerator projectivize后，是 bidegree `(4,4)`、`chi` 次数 2 的 45 项 polynomial。checker在 box

\[
[0,10^{-3}]\times[0,10^{-3}]\times[0,1/23]
\]
上做 exact tensor Bernstein audit，全部 `5*5*3=75` 个 coefficients严格为负；其中

\[
\boxed{
-\frac{1094168903517053204517852672}{129150390625}
\le b
\le
-\frac{14436349673818491223824}{1953125}<0.}
\tag{5.1}
\]

所以

\[
\boxed{
\mathcal H_2(X,Y;K,a_3/T)<0.}
\tag{5.2}
\]

因此 (3.3) 两项同号：

\[
\boxed{
\mathscr N_{63}^{(2)}<0.}
\tag{5.3}
\]

定义 canonical positive second-order tail

\[
\boxed{
\mathscr C_{63}^{(2)}
:=-\frac{\mathscr N_{63}^{(2)}}{G_\Delta S_{bal}}
\in\mathbf Z_{>0}.}
\tag{5.4}
\]

---

## 6. exact second-order support law

exact transport/Euclidean expansion可写

\[
M=M^{(1)}+M^{(2)}+M^{(\ge3)},
\]
其中每个 omitted monomial对 parent errors `(F,L)` 的总次数至少 3。因此在 common baseline `h` 上

\[
\boxed{v_p(M^{(\ge3)})\ge3h.}
\tag{6.1}
\]

### unsaturated balance: `rho<h`

此时

\[
v_p(M^{(1)})=h+\rho<2h,
\]
而 quadratic/higher terms至少 `2h`。所以 linear term唯一最浅；结合 (3.4),(4.1)：

\[
\boxed{p\nmid\mathscr C_{63}^{(2)}.}
\tag{6.2}
\]

### saturated balance: `rho>=h`

此时

\[
v_p(G_\Delta S_{bal})=2h.
\]
又 `3h>=2h+1`。因此由 (3.4)：

\[
\boxed{
p\mid\mathscr C_{63}^{(2)}
\Longleftrightarrow
v_p(M^{(1)}+M^{(2)})>2h
\Longleftrightarrow
v_p(M)>2h.}
\tag{6.3}

合并两支得到 canonical exact selector：

\[
\boxed{
p\mid\mathscr C_{63}^{(2)}
\Longleftrightarrow
\rho\ge h
\ \text{and}\ 
v_p(M)>2h.}
\tag{6.4}

这正是此前 `rho=h` normalized second-order cancellation所缺的 ordinary integer reader。

---

## 7. canonical second-order recycling gcd

定义

\[
\boxed{
\Sigma_{rec}^{(2)}
:=\gcd(G_\Delta,\mathscr C_{63}^{(2)}).}
\tag{7.1}
\]

则 genuine regular common prime满足

\[
\boxed{
p\mid\Sigma_{rec}^{(2)}
\Longleftrightarrow
\rho\ge h
\ \text{and}\ 
v_p(M)>2h.}
\tag{7.2}

已有 second-order theorem进一步说明：

- 若 `rho>h` 且 `p|Sigma_rec^(2)`，则 genuine noncentral prime必须命中 fixed irreducible `P_110(K)`；
- 因此 generic 未固定化分支只剩
  \[
  \boxed{\rho=h,\quad p\mid\Sigma_{rec}^{(2)}.}
  \tag{7.3}
  \]

所以 second-order normalized unit已从“手工 congruence”降成普通 gcd support。

---

## 8. exact binary orientation of the parent numerator

`G_Delta,S_bal` 都是 odd，因此先审计 `-N_63^(2)` 的完整二进 content。

### first-order block is safely deeper

checker对 `T^6 G_<`、`T^6 G_>` 的所有 terms给 uniform lower bounds

\[
v_2(\mathfrak G_<)\ge18,
\qquad
v_2(\mathfrak G_>)\ge17
\]
在 `m>=5` 成立。

又

\[
v_2(B)=M+m+t,
\qquad
v_2(Y)=m+t-1,
\qquad t\ge3.
\]
所以 (3.3) 第一行至少有

\[
\boxed{
v_2(\text{first line})
\ge2M+2m+2t+24.}
\tag{8.1}

### quadratic block has a unique shallowest term

primitive `H_2` 中唯一最低 2-adic monomial为

\[
\boxed{
18283339035648\,X^2\zeta^4
=2^{10}3^{14}\cdot3733\,X^2\zeta^4.}
\tag{8.2}

清 `T^6` 后成为

\[
2^{10}3^{14}\cdot3733\,X^2a_3^4T^2.
\]

checker对全部45项验证：在最小 `(m,t)=(5,3)` 已是唯一 minimum，下一层至少高 4；每项相对 baseline 的 `m,t` slopes均非负。因此对所有 dangerous endpoint

\[
\boxed{
v_2(\text{quadratic line})
=2M+2m+20.}
\tag{8.3}

由 (8.1)，第一行至少再深 `2t+4>=10` 层，所以不会干扰。

于是

\[
\boxed{
v_2(\mathscr N_{63}^{(2)})
=2M+2m+20.}
\tag{8.4}

除去该幂后模 `8` 仍只剩 (8.2)。因为

\[
5^2\cdot11\equiv3\pmod8,
\qquad
3^{14}\cdot3733\equiv5\pmod8,
\]
而所有 odd square/fourth powers为 `1 mod8`，故

\[
\boxed{
\frac{\mathscr N_{63}^{(2)}}{2^{2M+2m+20}}
\equiv7\pmod8.}
\tag{8.5}

结合 `N_63^(2)<0`：

\[
\boxed{
\frac{-\mathscr N_{63}^{(2)}}{2^{2M+2m+20}}
\equiv1\pmod8.}
\tag{8.6}

所以二阶 parent numerator的 positive primitive orientation是 parity-neutral `1 mod8`；它不会凭空再制造一份 odd-inert surcharge。

对 quotient本身：

\[
\boxed{
\frac{\mathscr C_{63}^{(2)}}{2^{2M+2m+20}}
\equiv(G_\Delta S_{bal})^{-1}\pmod8.}
\tag{8.7}

---

## 9. revised frontier

现在 descendant same-prime recycling已有两层 ordinary gcd ladder：

1. first order:
   \[
   \Sigma_{rec}=\gcd(G_\Delta,B_{63});
   \]
2. second order:
   \[
   \Sigma_{rec}^{(2)}=\gcd(G_\Delta,C_{63}^{(2)}).
   \]

其中 second-order selector严格排除 `rho<h`，并在 saturated branch上等价读取 `v_p(M)>2h`。

`rho>h` 的 second-order escape已被 `P_110` 固定化，因此真正 generic frontier进一步缩成

\[
\boxed{
\rho=h,
\qquad
p\mid\Sigma_{rec}^{(2)}.}
\]

下一步应对该 branch构造 third-order normalized balance，或者利用 `C_63^(2)` 与 parent coordinates / `P_63` 的 gcd support做新的 cross-reuse audit；不应再返回 first-order prime-source枚举。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-terminal-character"></a>

> 整合来源：`spontaneous-crt-descendant-terminal-character.md`

# A2 terminal descendant overdepth 的 fixed `-26` fourth-power character

> **依赖：** `spontaneous-crt-descendant-quartic-tail-hierarchy.md`、`spontaneous-crt-descendant-balance-tail.md`。
>
> **严格状态：**finite quartic hierarchy 已证明 exact remainder在四阶终止。本文审计 fully saturated generic equal-parent branch的 terminal coefficient。quartic homogeneous form精确化成 `26[27(X+Y)]^4+[55Y]^4`。因此若前三层已使 lower block严格深于 `4h`，而 actual remainder仍越过 `4h`，则 `-26` 必须是模 `p` 的第四次幂。对 genuine inert prime `p=3 mod4`，第四次幂集合与平方集合相同，故必要条件等价于 `(26/p)=-1`。这给 terminal overdepth一个固定 quadratic-character filter，不依赖尚未完全分解的 degree-192 ordinary resultant。本文没有排除满足该 character的 primes，因此不关闭 A2。

---

## 1. terminal quartic form

finite hierarchy给

\[
M^{(4)}
=s_L^4
\frac{65536\,\mathcal H_4(X,Y)}{5^4 11^4},
\]

其中

\[
\boxed{
\mathcal H_4(X,Y)
=2\cdot3^{12}\cdot13(X+Y)^4
+5^4 11^4Y^4.}
\tag{1.1}
\]

利用

\[
3^{12}=27^4,
\qquad
5^411^4=55^4,
\qquad
2\cdot13=26,
\]
得到 exact compact form

\[
\boxed{
\mathcal H_4(X,Y)
=26[27(X+Y)]^4+[55Y]^4.}
\tag{1.2}
\]

---

## 2. local terminal baseline

固定 genuine same-prime common label，记

\[
h=v_p(G_\Delta)\ge1.
\]

在 generic moving equal-parent branch写

\[
X=p^hX_0,
\qquad
Y=p^hY_0,
\qquad
p\nmid X_0Y_0.
\tag{2.1}
\]

finite hierarchy中前三层若已全部 saturated到使

\[
v_p(M^{(1)}+M^{(2)}+M^{(3)})>4h,
\tag{2.2}
\]
则 quartic block normally独占 `4h` 层。

因此若 actual remainder还满足

\[
\boxed{v_p(M)>4h,}
\tag{2.3}
\]
必要地

\[
\boxed{
\mathcal H_4(X_0,Y_0)\equiv0\pmod p.}
\tag{2.4}
\]

注意若 `X_0+Y_0=0 mod p`，(1.2) 只剩 `[55Y_0]^4`，为 unit，故 (2.4) 不可能。因此 terminal overdepth本身自动排除 parent cancellation `chi=-1`。

---

## 3. `-26` must be a fourth power

由 (1.2),(2.4)，且 `p` 与 `3,5,11,13,Y_0,X_0+Y_0` 分离：

\[
26[27(X_0+Y_0)]^4
\equiv-[55Y_0]^4\pmod p.
\]

所以

\[
\boxed{
\left(
\frac{55Y_0}{27(X_0+Y_0)}
\right)^4
\equiv-26\pmod p.}
\tag{3.1}
\]

因此

\[
\boxed{-26\text{ 是模 }p\text{ 的第四次幂}.}
\tag{3.2}
\]

---

## 4. inert primes: fourth powers equal squares

当前 genuine parity carrier只关心

\[
\boxed{p\equiv3\pmod4.}
\tag{4.1}
\]

此时

\[
p-1=2m_p
\]
且 `m_p` 为奇数。平方子群 `QR_p` 的阶就是奇数 `m_p`。映射

\[
x\mapsto x^2
\]
在奇阶群 `QR_p` 上是 automorphism，所以每个平方都唯一地是某个平方的平方。故

\[
\boxed{
(\mathbf F_p^\times)^4
=(\mathbf F_p^\times)^2.}
\tag{4.2}
\]

因此 (3.2) 等价于

\[
\boxed{
\left(\frac{-26}{p}\right)=1.}
\tag{4.3}
\]

又 `(−1/p)=-1`，于是

\[
\boxed{
\left(\frac{26}{p}\right)=-1.}
\tag{4.4}
\]

这就是 terminal overdepth 的 fixed character filter。

---

## 5. residue classes

`(26/p)` 对 genuine `p\nmid26` 只依赖 `p mod 104`。在 `p=3 mod4` 的 classes中，(4.4) 精确留下

\[
\boxed{
p\equiv
3,7,15,27,31,35,43,47,51,63,71,75
\pmod{104}.}
\tag{5.1}
\]

这里 (5.1) 仅是 character bookkeeping；它不声称这些 classes都实际出现 descendant roots。

---

## 6. role in the finite hierarchy

finite quartic hierarchy已经保证没有 fifth-order transport项。因此 terminal branch只有两种机制：

1. quartic coefficient为 unit：actual depth精确停在 `4h`；
2. quartic coefficient发生 p-adic cancellation：其全部额外 terminal depth由 `C_63^(4)` 读取，并且 prime首先必须满足 fixed character (4.4)。

所以 terminal overdepth已经没有新的 normalized parent ratio自由；它只剩 ordinary terminal tail与 fixed `-26` character。

下一步最值得做的是把该 character与 descendant-only external 的 projective carrier / prime-source character交叉，或者审计 `C_63^(4)` 与 `G_Delta` 的 common gcd高度。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-third-order-balance"></a>

> 整合来源：`spontaneous-crt-descendant-third-order-balance.md`

# A2 descendant balance saturation 的 third-order coefficient 与 fixed degree-148 gate

> **依赖：** `spontaneous-crt-descendant-second-order-gcd-ladder.md`、`spontaneous-crt-descendant-quartic-tail-hierarchy.md`、`spontaneous-crt-descendant-balance-tail.md`。
>
> **严格状态：**finite quartic hierarchy 已把 generic same-prime recycling 的真正 moving frontier推进到 first balance `rho=h` 且 second tail至少吞下一个 baseline `sigma>=h`。本文审计 strict branch `sigma>h`：此时 linear+quadratic block已严格深于 `3h`，若 actual remainder还要越过 `3h`，cubic homogeneous coefficient必须模 `p` 消失。first-order recycling已把 parent ratio唯一固定为 `chi_geom=-2G_>/(81G_<)`；在此 ratio上，cubic coefficient的 primitive numerator是 degree-20 polynomial `S_3(K,zeta)`。与 universal cubic消去 `zeta` 后只剩 central `(2K-9)^3`、旧 descendant-height gate `G_D(K)^2`，以及一个 irreducible degree-148 pure-K gate `P_148(K)`。所以 generic noncentral、non-height moving branch中，`sigma>h` 的 third-order overdepth只能命中 fixed `P_148`；真正未固定化的 third-order resonance进一步缩成 exact saturation `sigma=h`。本文不排除 `P_148` 的 modular roots，因此不关闭 A2。

---

## 1. cubic homogeneous coefficient

沿用 parent coordinates

\[
X=5^\lambda\mathscr R_{63}^\star,
\qquad
Y=g2^m\widehat{\mathscr D}_{63},
\]

以及

\[
\chi:=X/Y.
\]

finite quartic hierarchy 已证明 exact cubic block为

\[
\boxed{
M^{(3)}
=s_L^3
\frac{8192\,\mathcal H_3(X,Y;K,\zeta)}
{5^5 11^5K^2},}
\tag{1.1}
\]

其中 `H_3` 对 `(X,Y)` 齐次三次，`zeta` 次数2，共24项。

除去 `Y^3`，定义 ratio coefficient

\[
\mathcal Q_3(K,\zeta;\chi)
:=\mathcal H_3(\chi,1;K,\zeta).
\tag{1.2}
\]

first-order same-prime recycling在 equal parent depth上已唯一固定

\[
\boxed{
\chi_{geom}
=-\frac{2\mathcal G_>}{81\mathcal G_<}.}
\tag{1.3}
\]

---

## 2. primitive numerator at the geometric balance

将 (1.3) 代入 (1.2)。exact simplification给

\[
\boxed{
\mathcal Q_3(K,\zeta;\chi_{geom})
=
\frac{2^{13}\,\mathcal S_3(K,\zeta)}
{81K^2\mathcal G_<^3}.}
\tag{2.1}
\]

这里 `S_3` 取 primitive integer normalization，checker给

\[
\boxed{
\deg_{total}\mathcal S_3=20,
\qquad
\deg_\zeta\mathcal S_3=19,}
\tag{2.2}
\]

\[
\boxed{
\#\operatorname{supp}(\mathcal S_3)=230.}
\tag{2.3}
\]

所以 third-order normalization没有产生新的 denominator sheet；denominator只有 genuine unit `K` 与 first-order gate `G_<` 的三次方。

---

## 3. eliminate `zeta`: one new degree-148 gate

与 universal descendant cubic

\[
\mathcal E_{63}(K,\zeta)=0
\]

对 `zeta` 求 exact resultant。得到

\[
\boxed{
\operatorname{Res}_{\zeta}
(\mathcal E_{63},\mathcal S_3)
=
2^{174}3^{10}
(2K-9)^3
G_D(K)^2
P_{148}(K),}
\tag{3.1}
\]

其中

\[
G_D(K)=11K^2-240K+432,
\]

而

\[
\boxed{
\deg P_{148}=148,}
\tag{3.2}
\]

\[
\boxed{
P_{148}\text{ 在 }\mathbf Q[K]\text{ 中不可约},}
\tag{3.3}
\]

并且 `P_148` 恰有149个 nonzero coefficients。

因此排除 central `2K-9` 与旧 height/descendant gate `G_D` 后：

\[
\boxed{
\mathcal E_{63}=\mathcal S_3=0
\Longrightarrow
P_{148}(K)=0.}
\tag{3.4}
\]

正文不抄写149项大多项式；checker从 exact cubic block与 `chi_geom` canonical 重建并验证 factorization、degree与 irreducibility。

---

## 4. no real third-order degeneration

定义 projective form

\[
\boxed{
\mathcal S_3^{proj}(r,u)
:=r^{20}\mathcal S_3(1/r,u/r).}
\tag{4.1}
\]

exact audit给

\[
\deg_r=20,
\qquad
\deg_u=19,
\qquad
\#\operatorname{supp}=230.
\]

真实 endpoint包含于粗 box

\[
0<r<10^{-3},
\qquad
0<u<10^{-3}.
\]

将 (4.1) 搬到 unit square并转 tensor Bernstein basis，共

\[
21\cdot20=420
\]
个 exact rational coefficients。checker验证全部严格为负；极值为

\[
\boxed{
\min b_{ij}
=
-\frac{110643494138140653988416850451597394424139780430491531767088006331095359222500626733242735149107}
{29103830456733703613281250000000000000000000000000},}
\tag{4.2}
\]

\[
\boxed{
\max b_{ij}
=-2741384670235465948046260545341682788232526505<0.}
\tag{4.3}
\]

所以

\[
\boxed{\mathcal S_3(K,\zeta)<0}
\tag{4.4}
\]

在整个真实 dangerous endpoint成立。`P_148` branch没有 real third-order cancellation point；任何 surviving root只能来自 p-adic wrapping。

---

## 5. depth consequence

固定 genuine common prime，记

\[
h=v_p(G_\Delta),
\qquad
\rho=v_p(B_{63}),
\qquad
\sigma=v_p(C_{63}^{(2)}).
\]

当前 generic equal-parent moving branch已被前层压到

\[
\rho=h.
\]

若进一步

\[
\boxed{\sigma>h,}
\tag{5.1}
\]

second-order ladder给

\[
v_p(M^{(1)}+M^{(2)})
=2h+\sigma>3h.
\]

而 cubic block normally具有 baseline `3h`。因此若 actual remainder还满足

\[
\boxed{v_p(M)>3h,}
\tag{5.2}
\]

cubic coefficient必须模 `p` 消失。在 first recycling ratio已固定为 `chi_geom` 后，就是

\[
\mathcal S_3(K,\zeta)\equiv0\pmod p.
\]

结合 universal cubic与 §3：

\[
\boxed{
\rho=h,
\quad
\sigma>h,
\quad
v_p(M)>3h
\Longrightarrow
p\mid P_{148}(K),}
\tag{5.3}
\]

在 genuine noncentral、non-`G_D` sector成立。

所以 strict second-tail overdepth再次被一个 fixed irreducible pure-K gate固定化。

---

## 6. revised generic third-order frontier

目前 generic moving same-prime branch可进一步收缩：

- `rho<h`：first ladder exact；
- `rho>h` 且越过 `2h`：进入 fixed `P_110`；
- `rho=h, sigma<h`：second ladder exact；
- `rho=h, sigma>h` 且越过 `3h`：进入 fixed `P_148`；
- 所以真正仍保留未固定 normalized third-order resonance的 moving branch只剩
  \[
  \boxed{\rho=h,\qquad\sigma=h.}
  \tag{6.1}
  \]

下一步应直接在 `rho=sigma=h` 上读取 third tail `C_63^(3)` 的 exact saturation；不应继续扩大 `P_148` 的 ordinary discriminant分析。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-third-order-parity-spill"></a>

> 整合来源：`spontaneous-crt-descendant-third-order-parity-spill.md`

# A2 exact triple saturation 的 third-order parity spill

> **依赖：** `spontaneous-crt-descendant-quartic-tail-hierarchy.md`、`spontaneous-crt-descendant-third-order-balance.md`。
>
> **严格状态：**finite quartic hierarchy证明 third-order positive parent numerator `-N_63^(3)` 的 odd primitive part为 `3 mod4`。本文固定真正未固定化的 terminal moving labels，即 first、second、third tails都恰好饱和一个 baseline `rho=sigma=tau=h`。对每枚这样的 prime，`N_63^(3)` 的 local depth精确为 `4h`，因此该 prime对 third-order parent parity贡献为偶数，并且除去其完整 fourth-power baseline后不再出现。于是所有 exact triple-saturated labels的 baseline fourth power从 positive third carrier约掉以后，quotient仍为 `3 mod4`，必含一枚 odd-inert prime到奇次，而该 supplier严格位于 terminal recycling pool之外。本文尚未排除这枚外部 supplier为 prime `3`，因此只证明 support spill，不宣称新的 non-3 prime或 A2 closure。

---

## 1. exact terminal moving set

固定 genuine common inert labels中仍未被 fixed gates固定化的 local branch：

\[
\boxed{
\rho_p=h_p,
\qquad
\sigma_p=h_p,
\qquad
\tau_p=h_p,}
\tag{1.1}
\]

其中

\[
h_p=v_p(G_\Delta),
\]

\[
\rho_p=v_p(B_{63}),
\qquad
\sigma_p=v_p(C_{63}^{(2)}),
\qquad
\tau_p=v_p(C_{63}^{(3)}).
\]

`rho>h` / `sigma>h` 的进一步 overdepth分别被 fixed `P_110` / `P_148` gates固定化；`tau>h` 的 terminal overdepth首先承担 fixed `-26` character。因此 (1.1) 是 generic moving terminal resonance的 exact triple-saturation core。

令其 prime集合为 `E_term`，定义 baseline product

\[
\boxed{
G_{term}:=
\prod_{p\in E_{term}}p^{h_p}.}
\tag{1.2}

---

## 2. every terminal moving prime enters the third parent to even depth

third tail定义为

\[
\mathscr C_{63}^{(3)}
=-\frac{\mathscr N_{63}^{(3)}}{G_\Delta S_1S_2},
\]

其中

\[
S_1=\gcd(G_\Delta,B_{63}),
\qquad
S_2=\gcd(G_\Delta,C_{63}^{(2)}).
\]

在 (1.1) 的 prime `p` 上：

\[
v_p(S_1)=v_p(S_2)=h_p,
\]
并且

\[
v_p(C_{63}^{(3)})=\tau_p=h_p.
\]

所以 exact：

\[
\boxed{
v_p(-\mathscr N_{63}^{(3)})
=h_p+h_p+h_p+h_p
=4h_p.}
\tag{2.1}

特别地这是偶数。

于是

\[
\boxed{G_{term}^4\mid-\mathscr N_{63}^{(3)}.}
\tag{2.2}

而且对每个 `p in E_term`，(2.1) 是 exact equality，所以约掉 `G_term^4` 后这些 primes完全消失：

\[
\boxed{
\gcd\!\left(
G_{term},
\frac{-\mathscr N_{63}^{(3)}}{G_{term}^4}
\right)=1.}
\tag{2.3}

---

## 3. remove the binary content

quartic hierarchy已经证明

\[
\boxed{
v_2(\mathscr N_{63}^{(3)})=4M+4m+20,}
\tag{3.1}
\]

以及 positive primitive orientation

\[
\boxed{
H_3^{par}
:=\frac{-\mathscr N_{63}^{(3)}}{2^{4M+4m+20}}
>0,
\qquad
H_3^{par}\equiv3\pmod4.}
\tag{3.2}

`G_term` 为 odd，所以 (2.2) 同样给

\[
G_{term}^4\mid H_3^{par}.
\]

定义 spilled quotient

\[
\boxed{
\mathscr Q_{spill}
:=\frac{H_3^{par}}{G_{term}^4}.}
\tag{3.3}

由 (2.3)：

\[
\boxed{\gcd(\mathscr Q_{spill},G_{term})=1.}
\tag{3.4}

---

## 4. parity survives the fourth-power removal

任意 odd integer的 fourth power都满足

\[
G_{term}^4\equiv1\pmod4.
\]

所以由 (3.2),(3.3)：

\[
\boxed{
\mathscr Q_{spill}>0,
\qquad
\mathscr Q_{spill}\equiv3\pmod4.}
\tag{4.1}

因此其 prime factorization中必有至少一枚

\[
\boxed{q\equiv3\pmod4}
\tag{4.2}

出现奇数次。

结合 (3.4)：

\[
\boxed{q\notin\operatorname{Supp}(G_{term}).}
\tag{4.3}

所以 exact triple-saturated terminal recycling pool自身对 third-order parent parity完全中性；third-order positive carrier必把一份 odd-inert parity溢出到该 pool之外。

---

## 5. what this does and does not prove

本文严格证明的是 support spill：

\[
\boxed{
\text{terminal exact-saturation primes}
\text{不能独自承担 third-order odd parity}.}
\tag{5.1}

外部 supplier `q` 可能属于：

- fixed prime `3`；
- 已有 target/source/height pool；
- descendant residual/external pool；
- 或真正新的 external label。

本文没有完成这些来源的二次审计，因此不把 (4.3) 夸大成“存在新的 non-3 prime”。下一步若能排除 `q=3` 并把 old pools与 `Q_spill` 做 support separation，就会把本 surcharge升级成真正的 independent-prime product cost。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-transport-resonance"></a>

> 整合来源：`spontaneous-crt-descendant-transport-resonance.md`

# A2 descendant transported-error overdepth 的 linear resonance 与 fixed tangent gates

> **依赖：** `spontaneous-crt-descendant-projective-depth-reader.md`、`spontaneous-crt-descendant-quotient-gate.md`、`spontaneous-crt-universal-descendant-cubic.md`、`endpoint-lattice.md` 的 exact rational-root equation。
>
> **严格状态：**linear remainder overdepth若不是 quotient-level normalized cancellation，就必须来自 upstream `E_proj` 已比 common baseline更深。本文把 `E_proj` 恢复为 exact rational-root polynomial在两个真实 errors `F_Delta,L_proj` 上的 transport，并写出其一阶项。generic 情形下，额外 `E`-depth只可能是两个 normalized residual units的一次线性 cancellation；coefficient singularity只有 `J+zeta=0` 或 rational-root tangent `Phi_J=0`。前者在 descendant first layer上回到已有 `L=K^2-576K+1296` / alpha-height `G_D` gates；后者与 universal cubic消元后仅新增一个 quadratic `H_2(K)` 与一个 irreducible decic `H_10(K)`。两者真实都为正，primitive orientations分别为 `7 mod8` 与 `5 mod8`。因此 low tangent exception自身带 odd-inert surcharge，高 tangent exception total inert parity为偶。本文尚未排除 generic normalized transport resonance，因此不关闭 A2。

---

## 1. exact transported errors

沿用真实 rational-root polynomial

\[
\boxed{
\Phi(J,R)
=J(J+2\zeta)(K-J)^2-R(J+\zeta)^2,}
\tag{1.1}

其中真实 endpoint满足

\[
\Phi(J,R)=0.
\]

两个 descendant/additive approximations为

\[
R_0=R+K^2L,
\qquad
J_0=J+\frac{F}{U},
\tag{1.2}

其中

\[
\boxed{L:=\mathscr L_{\rm proj},}
\qquad
\boxed{F:=F_\Delta,}
\qquad
\boxed{U:=2K-9.}
\]

已有 exact identity

\[
\boxed{
\mathscr E_{\rm proj}
=\frac{65536U^4}{K^8}
\left[\Phi(J+F/U,R+K^2L)-\Phi(J,R)\right].}
\tag{1.3}

在 genuine noncentral sector，前面的 scale为 p-unit。

---

## 2. first-order transported resonance

对 (1.3) 关于 `F,L` 展开。因为 constant term由 `Phi(J,R)=0` 消失，一阶项为

\[
\boxed{
\frac{\Phi_J(J,R)}U F
-K^2(J+\zeta)^2L.}
\tag{2.1}

其余每一项对 `(F,L)` 的总次数至少为2。

设

\[
f=v_p(F),
\qquad
\ell=v_p(L),
\qquad
k=\min(f,\ell)\ge1.
\]

若 coefficient均为 units：

\[
p\nmid\Phi_J(J,R)(J+\zeta)KU,
\tag{2.2}
\]
则：

- `f<ell` 时，唯一最低项来自 `F`，所以
  \[
  \boxed{v_p(E_{proj})=f;}
  \tag{2.3}
  \]
- `ell<f` 时，唯一最低项来自 `L`，所以
  \[
  \boxed{v_p(E_{proj})=\ell.}
  \tag{2.4}
  \]

因此 generic upstream overdepth只能在

\[
\boxed{f=\ell=:h}
\tag{2.5}

发生。写

\[
F=p^hF_0,
\qquad
L=p^hL_0,
\]
其中 `F_0,L_0` 为 units，则因二次项至少含 `p^(2h)`：

\[
\boxed{
 v_p(E_{proj})>h
\iff
\frac{\Phi_J}U F_0
-K^2(J+\zeta)^2L_0
\equiv0\pmod p.}
\tag{2.6}

这就是 generic transported-error normalized resonance。

---

## 3. the two coefficient-singular mechanisms

(2.1) 的系数退化只可能来自

\[
\boxed{J+\zeta\equiv0\pmod p}
\tag{3.1}

或

\[
\boxed{\Phi_J(J,R)\equiv0\pmod p.}
\tag{3.2}

`K,U` 已由 genuine/noncentral separation保证为 units。

### 3.1 `J+zeta=0`

在 exact root `Phi=0` 上，若 `J+zeta=0`，则

\[
\Phi=-J^2(K-J)^2=0.
\]

所以

\[
J=0
\quad\text{或}\quad
J=K.
\]

若 `J=0`，则 `zeta=0`。再代 descendant first-layer `F=0`：

\[
16(2K-9)^2=63K^2,
\]
即

\[
\boxed{K^2-576K+1296=0.}
\tag{3.3}

若 `J=K`，则 `zeta=-K`，所以

\[
\alpha=T(K+\zeta)=0,
\]
回到已经单列的 alpha-supported sector；`F=0` 同时给

\[
\boxed{G_D(K)=11K^2-240K+432=0.}
\tag{3.4}

因此 `J+zeta` singularity没有产生新的 generic pure-spontaneous gate。

---

## 4. rational-root tangent elimination

现在处理

\[
\Phi_J=0.
\]

在 `J+zeta` 为 unit且使用 exact `Phi=0` 消去 `R` 后：

\[
\boxed{
\Phi_J
=\frac{2(J-K)}{J+\zeta}
\left(
J^3+3J^2\zeta+3J\zeta^2-K\zeta^2
\right).}
\tag{4.1}

将 descendant first-layer substitutions

\[
J=J_0(K,\zeta),
\qquad
R=R_0(K,\zeta)
\]
代回 `Phi_J`，清去 `2K-9` denominator；再与 universal cubic

\[
\mathcal E_{63}(K,\zeta)=0
\]
关于 `zeta` 求 resultant。exact factorization为

\[
\boxed{
\begin{aligned}
\operatorname{Res}_{\zeta}
(\mathcal E_{63},\operatorname{num}\Phi_J(J_0,R_0))
={}&-2^{43}3^2(2K-9)^{13}\\
&\cdot(K^2-576K+1296)^2\\
&\cdot G_D(K)^2\\
&\cdot H_2(K)H_{10}(K),
\end{aligned}}
\tag{4.2}

其中

\[
\boxed{H_2(K)=47K^2+144K-416,}
\tag{4.3}

以及 primitive irreducible decic

\[
\boxed{
\begin{aligned}
H_{10}(K)={}&388341K^{10}-601739280K^9
+229469500800K^8\\
&+1907909697024K^7+388001070336K^6\\
&+472180427182080K^5-5611474473205760K^4\\
&+24390734431518720K^3-51182973630480384K^2\\
&+52664489116434432K-21375786688708608.
\end{aligned}}
\tag{4.4}

前三个 factors分别是已知 central、`J+zeta` zero-root、height/alpha-supported gates。故 genuine alpha-free noncentral tangent support新增的只有

\[
\boxed{H_2(K)=0\quad\text{或}\quad H_{10}(K)=0.}
\tag{4.5}

---

## 5. low tangent gate is positive primitive `7 mod 8`

因为 `K=2k_0` 且 `k_0` odd：

\[
H_2=188k_0^2+288k_0-416.
\]

第一项精确有 `v_2=2`，其它两项至少有 `v_2=5`。因此

\[
\boxed{v_2(H_2)=2.}
\tag{5.1}

除以4：

\[
\frac{H_2}{4}
\equiv47k_0^2
\equiv7\pmod8.
\tag{5.2}

当前 `K>9*10^11`，显然

\[
\boxed{H_2>0.}
\tag{5.3}

所以 low tangent singular gate自身携带 odd-inert parity surcharge。

---

## 6. high tangent gate is positive primitive `5 mod 8`

对 `H_10` 各项使用 `v_2(K)=1`。唯一最低项是 leading term：

\[
v_2(388341K^{10})=10.
\]

第二浅层已经是 `13`，故

\[
\boxed{v_2(H_{10})=10.}
\tag{6.1}

又

\[
388341\equiv5\pmod8,
\]
而 odd `k_0^{10}≡1 mod8`，因此

\[
\boxed{H_{10}/2^{10}\equiv5\pmod8.}
\tag{6.2}

正性也可完全初等地读取。对 `K>=2000`：

\[
388341K^{10}-601739280K^9>0.
\]

另外分别用 positive lower-degree terms覆盖三个剩余 negative terms：

\[
229469500800K^8>5611474473205760K^4,
\]

\[
1907909697024K^7>51182973630480384K^2,
\]

\[
472180427182080K^5>21375786688708608.
\]

其余显示项为正或不需要用于下界。因此

\[
\boxed{H_{10}>0\qquad(K\ge2000).}
\tag{6.3}

当前 endpoint远强于该条件。

所以 high tangent gate的 positive primitive part为 `5 mod8`，total inert parity为偶。

---

## 7. updated overdepth frontier

upstream `E_proj` overdepth现在严格分成：

1. generic equal-depth transported resonance (2.6)；
2. old `J+zeta` / alpha-height gates；
3. new low tangent `H_2`, positive primitive `7 mod8`；
4. new high tangent `H_10`, positive primitive `5 mod8`。

结合 Euclidean quotient theorem，same-prime recycling已被连续压成两层 normalized resonance，加上少量 fixed singular carriers；其中所有 low-degree singular escape都额外支付 odd-inert parity。

下一步最窄的 generic target是把 (2.6) 与 descendant parent depths `a_p,b_p` 直接联立，判断 unequal parent depths是否已经自动排除 transported resonance。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descendant-unequal-parent-depth"></a>

> 整合来源：`spontaneous-crt-descendant-unequal-parent-depth.md`

# A2 descendant-only external 的 unequal parent-depth branches 只剩 fixed projective gates

> **依赖：** `spontaneous-crt-descendant-linear-depth-reader.md`、`spontaneous-crt-descendant-transport-resonance.md`、`spontaneous-crt-descendant-quotient-gate.md`。
>
> **严格状态：**记 `a=v_p(Rstar_63)`、`b=v_p(Dhat_63)`。generic same-prime linear-tail recycling此前仍可能来自 transported error与 Euclidean quotient的 normalized cancellation。本文证明当 `a!=b` 时，parent descent已经把所有 normalized unit ratio固定：若 `a<b`，transport baseline只来自 additive error `L_proj`；若 `b<a`，exact normalization给 `F_0=K^2L_0`。因此 `M_63` overdepth分别等价于两个只依赖 `(K,zeta)` 的 coefficient gates `G_<,G_>`。每个 gate清分母后总次数6、28项；与 universal cubic消去 `zeta` 后各得到一个 irreducible degree-48 pure-K polynomial。projective forms在真实 `0<r,u<10^-3` box都严格为负，所以 unequal-depth recycling只能通过 p-adic wrapping。真正仍保留自由 normalized unit ratio的 generic parent branch因此只剩 `a=b`。本文没有排除两个 degree-48 modular gates，因此不关闭 A2。

---

## 1. exact normalizations of `L` and `F`

记

\[
a:=v_p(\mathscr R_{63}^\star),
\qquad
b:=v_p(\widehat{\mathscr D}_{63}),
\qquad
k:=\min(a,b).
\]

projective additive error满足 exact scaling

\[
\boxed{
\widehat{\mathcal T}_2
=\frac{5^mB^2K^2}{2^{2M+2}}\,L,}
\tag{1.1}

其中

\[
L:=\mathscr L_{\rm proj}.
\]

验证只需用

\[
K^2L=R_0-R,
\qquad
R=Q^2N_0/B^2,
\]
以及 `widehat(T)_2` 的 explicit formula。

另一方面 descendant error满足

\[
\boxed{
\widehat{\mathscr D}_{63}
=c_u^2gT\,F,}
\tag{1.2}

其中

\[
F:=F_\Delta.
\]

所有显示 scale在 genuine external odd prime上均为 units。

parent descent为

\[
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.
\tag{1.3}

---

## 2. case `a<b`: `F` is deeper and `L` alone controls the baseline

若

\[
\boxed{a<b,}
\tag{2.1}

则由 (1.3)

\[
v_p(\widehat T_2)=a=k,
\]
所以

\[
v_p(L)=k,
\qquad
v_p(F)=b>k.
\]

transport theorem的一阶式因此模 `p^(k+1)` 只剩 `L` 项：

\[
\frac{E_{proj}}{p^k}
\equiv
C_<\,L_0
\pmod p,
\tag{2.2}

其中在 first-layer point

\[
J=J_0(K,\zeta),
\qquad
R=R_0(K,\zeta),
\]
有

\[
\boxed{
C_<
:=-\frac{65536(2K-9)^4}{K^6}
(J_0+\zeta)^2.}
\tag{2.3}

Euclidean division

\[
M=E-Q L
\]
给

\[
\frac M{p^k}
\equiv(C_<-Q_0)L_0\pmod p,
\tag{2.4}

其中

\[
Q_0:=Q_{63}(1/K,\zeta/K,R_0/K^2).
\]

所以

\[
\boxed{
a<b,\quad v_p(M)>k
\Longrightarrow
C_<-Q_0\equiv0\pmod p.}
\tag{2.5}

在 coefficient units成立时反向也成立。

---

## 3. case `b<a`: the two real errors have a fixed ratio

若

\[
\boxed{b<a,}
\tag{3.1}

则 (1.3) baseline由 descended quotient独占：

\[
\widehat T_2/p^b
\equiv
g2^m\widehat D_{63}/p^b
\pmod p.
\]

由 (1.1),(1.2) 比较 normalized units：

\[
\frac{L_0}{F_0}
=
\frac{2^{2M+2}}{5^mB^2K^2}
\cdot g2^m
\cdot c_u^2gT.
\]

使用

\[
B^2=2^{2M+2m+2}c_u^2g^2,
\qquad
T=2^m5^m,
\]
所有 source scales精确抵消：

\[
\boxed{L_0/F_0=1/K^2,}
\tag{3.2}

即

\[
\boxed{F_0=K^2L_0.}
\tag{3.3}

因此 transported first-order coefficient退化为纯几何量

\[
\boxed{
C_>
:=\frac{65536(2K-9)^3}{K^6}
\left[
\Phi_J(J_0,R_0)
-(2K-9)(J_0+\zeta)^2
\right].}
\tag{3.4}

于是

\[
\frac M{p^k}
\equiv(C_>-Q_0)L_0\pmod p,
\]
并有

\[
\boxed{
b<a,\quad v_p(M)>k
\Longrightarrow
C_>-Q_0\equiv0\pmod p.}
\tag{3.5}

所以第二个 unequal-depth branch也没有未知 residual-unit ratio。

---

## 4. two compact degree-6 coefficient gates

定义

\[
\boxed{
\mathcal G_<
:=\operatorname{pp}_{\mathbf Z[K,\zeta]}
\operatorname{num}(C_<-Q_0),}
\tag{4.1}

\[
\boxed{
\mathcal G_>
:=\operatorname{pp}_{\mathbf Z[K,\zeta]}
\operatorname{num}(C_>-Q_0).}
\tag{4.2}

exact audit给

\[
\boxed{
\deg\mathcal G_<
=\deg\mathcal G_>=6,}
\tag{4.3}

\[
\boxed{
\#\operatorname{supp}(\mathcal G_<)
=\#\operatorname{supp}(\mathcal G_>)=28.}
\tag{4.4}

两者 denominator只含 fixed `5^7 11^7 K^6`，在 genuine branch为 units。

---

## 5. eliminate `zeta`: two irreducible degree-48 `K` gates

与 universal cubic

\[
\mathcal E_{63}(K,\zeta)=0
\]
分别消去 `zeta`。exact resultants为

\[
\boxed{
\operatorname{Res}_{\zeta}(E_{63},G_<)
=-2^{54}3^3\,P_{48,<}(K),}
\tag{5.1}

\[
\boxed{
\operatorname{Res}_{\zeta}(E_{63},G_>)
=-2^{51}3^5\,P_{48,>}(K).}
\tag{5.2}

两个 primitive polynomials均满足

\[
\boxed{
\deg P_{48,<}=\deg P_{48,>}=48,}
\tag{5.3}

并且在 `Q[K]` 中均不可约。

正文不抄写两个49-coefficient大多项式；checker由 (4.1),(4.2) canonical 重建并核对 degree、content与不可约性。

因此每个 unequal-depth same-prime recycling candidate的 `K mod p` 都必须落入固定 degree-48 algebraic gate；不再存在自由 normalized unit。

---

## 6. projective real exclusion

令

\[
r=1/K,
\qquad
u=\zeta/K.
\]

将 (4.1),(4.2) projectivize：

\[
\boxed{
G_<^{proj}(r,u)
=r^6G_<(1/r,u/r),}
\tag{6.1}

\[
\boxed{
G_>^{proj}(r,u)
=r^6G_>(1/r,u/r).}
\tag{6.2}

primitive normalization后两者仍恰有28项、总次数6。

实际 endpoint满足远强于下列 box的条件：

\[
0<r<1/1000,
\qquad
0<u<1/1000.
\]

对两个 projective gates分别做 exact tensor Bernstein audit，全部49个 coefficients严格为负。

对 `G_<^proj`：

\[
\boxed{
-\frac{112029905407645176473437498709}
{976562500000000}
\le b_{ij}
\le-104415810491281<0.}
\tag{6.3}

对 `G_>^proj`：

\[
\boxed{
-\frac{9078214206708903545409301301679}
{1953125000000000}
\le b_{ij}
\le-4264617552904693<0.}
\tag{6.4}

所以真实 endpoint上

\[
\boxed{G_<^{proj}<0,\qquad G_>^{proj}<0.}
\tag{6.5}

unequal-depth gates没有 real degeneration；任何 surviving root只能是 p-adic wrapping。

---

## 7. updated generic frontier

parent-depth split现在变成：

- `a<b`：overdepth只能命中 fixed `G_<` / `P_48,<`；
- `b<a`：overdepth只能命中 fixed `G_>` / `P_48,>`；
- `a=b`：normalized parent sum允许真正的 free unit ratio，仍需单独 resonance analysis。

因此 generic same-prime recycling中，**唯一仍保留 valuation-unit自由的 parent branch已经严格缩成 equal depth `a=b`**。

这与早先 omega-height equal-depth bottleneck的结构非常相似，下一步应直接为 `a=b` 构造 canonical parent resonance tail，而不再继续扩大 unequal-depth fixed gates。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descended-quotient-orientation"></a>

> 整合来源：`spontaneous-crt-descended-quotient-orientation.md`

# A2 descended quotient `Dhat_63` 的 parity orientation 与 denominator gate

> **依赖：** `spontaneous-crt-height-remainder-descent.md`、`spontaneous-crt-height-primitive-remainder.md`、`endpoint-lattice.md` 的 `W_q mod 4` orientation 与 mixed coprimality。
>
> **严格状态：**positive descent `That_2=5^lambda Rstar_63+gD_63` 中，`D_63` 仍含显式 `2^m`。本文除去它，定义 positive odd primitive quotient `Dhat_63=D_63/2^m=c_u^2F_63`。其 mod-4 orientation精确等于 `3Z`，所以在危险 `Z=1 mod4` orientation中它本身也是 positive `3 mod4` inert carrier。另一方面它与 denominator `g` 的全部 common support精确等于 central gate `gcd(2K-9,g)`；因此 descended parity不能自由回落到 denominator support。本文不排除 central gate本身，因此不关闭 A2。

---

## 1. primitive descended quotient

前一 descent theorem给

\[
\boxed{
\mathscr D_{63}=2^m c_u^2\mathscr F_{63}>0,}
\tag{1.1}
\]

其中

\[
\boxed{
\mathscr F_{63}
=(2K-9)B_\Delta-\frac{63}{16}gTK^2,}
\tag{1.2}
\]

\[
\boxed{
B_\Delta:=g((2K-9)T-a_3)-H_0.}
\tag{1.3}
\]

`F_63` 已证明为 odd，因此定义

\[
\boxed{
\widehat{\mathscr D}_{63}
:=\frac{\mathscr D_{63}}{2^m}
=c_u^2\mathscr F_{63}
\in\mathbf Z_{>0}\text{ odd}.}
\tag{1.4}
\]

---

## 2. mod-4 orientation

因为

\[
g=2^{t-1}\rho,
\qquad t\ge3,
\]
有

\[
g\equiv0\pmod4.
\]

所以由 (1.3)：

\[
B_\Delta\equiv-H_0\pmod4.
\tag{2.1}
\]

source relation为

\[
H_0=g(3T+a_3)-5^\lambda C.
\]

第一项被 `4` 整除，而 `5^lambda≡1 mod4`，故

\[
\boxed{H_0\equiv-C\pmod4,}
\tag{2.2}
\]

于是

\[
\boxed{B_\Delta\equiv C\pmod4.}
\tag{2.3}
\]

又 `K=10P`，所以 `2K` 被 `4` 整除：

\[
\boxed{2K-9\equiv3\pmod4.}
\tag{2.4}
\]

第二项

\[
\frac{63}{16}gTK^2
\]
在当前 `m>=5,t>=3` 下仍被 `4` 整除。因此

\[
\boxed{
\mathscr F_{63}\equiv3C\pmod4.}
\tag{2.5}
\]

`c_u` 只含 `1 mod4` primes，所以 `c_u^2≡1 mod4`：

\[
\boxed{
\widehat{\mathscr D}_{63}
\equiv3C\pmod4.}
\tag{2.6}
\]

---

## 3. identify `C mod 4` with the old `Z` orientation

已有

\[
H_0=c_uW_q,
\qquad
W_q\equiv3Z\pmod4.
\tag{3.1}
\]

又 `c_u≡1 mod4`，所以

\[
H_0\equiv3Z\pmod4.
\tag{3.2}
\]

与 (2.2) 的 `H_0≡-C≡3C mod4` 比较：

\[
3Z\equiv3C\pmod4.
\]

消去 `3`：

\[
\boxed{C\equiv Z\pmod4.}
\tag{3.3}
\]

代回 (2.6)：

\[
\boxed{
\widehat{\mathscr D}_{63}
\equiv3Z\pmod4.}
\tag{3.4}
\]

特别地在最危险 orientation

\[
\boxed{Z\equiv1\pmod4}
\]
时：

\[
\boxed{
\widehat{\mathscr D}_{63}>0,
\qquad
\widehat{\mathscr D}_{63}\equiv3\pmod4.}
\tag{3.5}
\]

所以 original `That_2`、fully primitive remainder `Rstar_63` 与 descended primitive quotient `Dhat_63` 在该 orientation中都需要 odd-inert parity。

---

## 4. denominator overlap is exactly the central gate

模 `g`，由 (1.3) 与 source relation：

\[
B_\Delta
\equiv-H_0
\equiv5^\lambda C
\pmod g.
\tag{4.1}
\]

(1.2) 第二项显式含 `g`，所以

\[
\boxed{
\mathscr F_{63}
\equiv5^\lambda C(2K-9)
\pmod g.}
\tag{4.2}
\]

mixed/source coprimality已有

\[
\gcd(5c_uC,g)=1.
\tag{4.3}
\]

由于 `Dhat_63=c_u^2F_63`：

\[
\boxed{
\gcd(\widehat{\mathscr D}_{63},g)
=\gcd(2K-9,g).}
\tag{4.4}
\]

所以 descended quotient若想把其 inert parity落回 denominator `g` support，只能通过唯一 central linear gate

\[
\boxed{2K-9.}
\tag{4.5}
\]

不存在 generic denominator reuse。

---

## 5. relation to the nested descent

fully primitive positive descent为

\[
\boxed{
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g\,2^m\widehat{\mathscr D}_{63}.}
\tag{5.1}
\]

其中

\[
\widehat{\mathcal T}_2\equiv3\pmod4,
\qquad
\mathscr R_{63}^\star\equiv3\pmod4,
\qquad
\gcd(\mathscr R_{63}^\star,10g)=1.
\]

在 `Z=1 mod4` 时再加 (3.5)，得到三层 positive `3 mod4` package：

\[
\boxed{
\widehat{\mathcal T}_2,
\quad
\mathscr R_{63}^\star,
\quad
\widehat{\mathscr D}_{63}
\text{ 均为 positive }3\bmod4.}
\tag{5.2}
\]

若 parity试图复用同一 prime，则 parent theorem已经要求该 prime同时进入 `Rstar_63,Dhat_63`；本文又说明若它还位于 denominator support，就必须进入 `2K-9` central gate。

---

## 6. current role

本文没有排除 `gcd(2K-9,g)`。它把 descended quotient的 denominator overlap精确压回仓库已经反复出现的 central sheet。

因此后续 nested descent的 support审计只需区分：

1. central `2K-9` support；
2. genuine external support。

尤其在 `Z=1 mod4` orientation，若能进一步证明 `Rstar_63/Dhat_63` 的 common inert supplier不能进入 central sheet，就会强制原 carrier、short remainder与 descended quotient至少使用两枚不同 inert primes。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-descent-overlap-nogo"></a>

> 整合来源：`spontaneous-crt-descent-overlap-nogo.md`

# A2 `Rstar_63/D_63` overlap 的 resultant no-go

> **依赖：** `spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-height-remainder-descent.md`。
>
> **严格状态：**fully primitive short remainder `Rstar_63` 与 descended quotient `D_63` 的 common prime正是 original/remainder parity reuse的唯一剩余 overlap。本文审计两个最自然的 elimination方向。对 top defect `C` 的 linear resultant精确退化为 `(2K-9)That_2`，在 common branch上完全自动；对 `K` 的 resultant虽产生一个新 quadratic discriminant，但其唯一 nonsquare-looking factor `H_63` 在 `That_2=0` 上精确退化为 `c_u^2g^2(TK-9T-2a_3)^2`。因此 ordinary resultant/Legendre路线没有新的 generic obstruction；只有两个显式 singular gates `TK-9T-2a_3` 与 `1270B^2-Q^2N_0` 值得继续。本文是 no-go + singular reduction，不关闭 A2。

---

## 1. cleared overlap equations

令

\[
A_m:=2^m,
\qquad
V_d:=5^d,
\qquad
P_\lambda:=5^\lambda,
\]
所以

\[
T=A_mV_dP_\lambda.
\]

将 descended primitive quadratic `F_63` 清掉 denominator `16`：

\[
\boxed{
\begin{aligned}
F_{63}^{(16)}:={}&
16(2K-9)
\{g((2K-12)T-2a_3)+P_\lambda C\}\\
&-63gTK^2.
\end{aligned}}
\tag{1.1}
\]

对 genuine overlap prime `p∤2c_u`：

\[
p\mid\mathscr D_{63}
\Longleftrightarrow
p\mid F_{63}^{(16)}.
\]

另一方面 fully primitive remainder的 exact formula由 parent expansion给

\[
\boxed{
\begin{aligned}
16\mathscr R_{63}^\star
={}&A_m^2V_dc_u^2g^2
(15K^2+384K-848)\\
&-16A_mgc_u^2C(2K-9)\\
&-16V_dQ_0^2N_0.
\end{aligned}}
\tag{1.2}
\]

记右边为 `R_63^(16)`。

所以 genuine common support满足

\[
F_{63}^{(16)}=R_{63}^{(16)}=0\pmod p.
\]

---

## 2. eliminating `C` exactly recovers the original carrier

两式对 `C` 都是一次式。直接求 resultant并使用 `T=A_mV_dP_lambda`：

\[
\boxed{
\operatorname{Res}_C(
F_{63}^{(16)},R_{63}^{(16)}
)
=256(2K-9)\widehat{\mathcal T}_2.}
\tag{2.1}
\]

这里

\[
\boxed{
\begin{aligned}
\widehat{\mathcal T}_2
={}&A_mc_u^2g^2
[TK^2-(18T+4a_3)K+18a_3+55T]\\
&-5^mQ_0^2N_0.
\end{aligned}}
\tag{2.2}
\]

但是 parent descent已经证明

\[
p\mid\mathscr R_{63}^\star,\quad
p\mid\mathscr D_{63}
\Longrightarrow
p\mid\widehat{\mathcal T}_2.
\]

所以 (2.1) 对 noncentral `p∤2K-9` 不增加任何条件；central `2K-9` 也已是旧 additive overlap gate。

因此：

\[
\boxed{
C\text{-resultant is an exact syzygy, not a new obstruction}.}
\tag{2.3}
\]

---

## 3. eliminating `K` gives only a quadratic in `C`

反过来对 `K` 求 resultant。除去显式 unit/content factor

\[
256A_m^2g^2V_d^2,
\]
剩余是关于 `C` 的 quadratic `R_C(C)`。

无需记录其冗长 coefficients；真正决定 generic root character的是 discriminant。直接 factor得到

\[
\boxed{
\begin{aligned}
\operatorname{Disc}_C(R_C)
={}&4096P_\lambda^2c_u^2
\left(
1270A_m^2c_u^2g^2-N_0Q_0^2
\right)^2\\
&\cdot\mathscr H_{63},
\end{aligned}}
\tag{3.1}
\]

其中

\[
\boxed{
\mathscr H_{63}
:=
c_u^2g^2(26T^2+18Ta_3+4a_3^2)
+5^{2m}Q_0^2N_0.}
\tag{3.2}
\]

所以除 fixed/content factors外，表面上唯一可能产生 independent quadratic character的是 `H_63`。

---

## 4. `H_63` becomes an exact square on the original carrier

在任何 genuine common prime上已有

\[
\widehat{\mathcal T}_2\equiv0\pmod p.
\]

由 (2.2)：

\[
5^mQ_0^2N_0
\equiv
A_mc_u^2g^2
[TK^2-(18T+4a_3)K+18a_3+55T]
\pmod p.
\]

再乘 `5^m`，并使用

\[
A_m5^m=T:
\]

\[
5^{2m}Q_0^2N_0
\equiv
Tc_u^2g^2
[TK^2-(18T+4a_3)K+18a_3+55T]
\pmod p.
\tag{4.1}
\]

代入 (3.2)：

\[
\begin{aligned}
\mathscr H_{63}
\equiv c_u^2g^2\{&
26T^2+18Ta_3+4a_3^2\\
&+T[TK^2-(18T+4a_3)K+18a_3+55T]
\}.
\end{aligned}
\]

大括号精确平方：

\[
\boxed{
26T^2+18Ta_3+4a_3^2
+T[TK^2-(18T+4a_3)K+18a_3+55T]
=(TK-9T-2a_3)^2.}
\tag{4.2}
\]

因此

\[
\boxed{
\mathscr H_{63}
\equiv
c_u^2g^2(TK-9T-2a_3)^2
\pmod p.}
\tag{4.3}
\]

在 `p∤c_ug` generic sector，这就是显式平方。

故 (3.1) 的整个 discriminant在 generic overlap上自动为平方：

\[
\boxed{
\text{ordinary }K\text{-resultant Legendre test adds no new generic obstruction}.}
\tag{4.4}
\]

---

## 5. only two singular gates remain

`K`-resultant quadratic出现 repeated root只可能来自 discriminant factors。

除固定 `2,5,c_u` 外，真正需要单列的是：

### A. third/central gate

\[
\boxed{TK-9T-2a_3\equiv0\pmod p.}
\tag{5.1}
\]

这正是此前 source/shifted-pair analysis中已经出现的 central third-block linear form。

### B. pure-prefix gate

另一个 square factor为

\[
1270A_m^2c_u^2g^2-N_0Q_0^2.
\]

使用

\[
A_m c_ug=\frac{B}{2^{M+1}},
\qquad
Q_0=\frac{Q}{2^{M+1}},
\]
乘回公共 denominator得到 pure-prefix integer

\[
\boxed{
\mathscr F_{1270}
:=1270B^2-Q^2N_0.}
\tag{5.2}
\]

所以第二个 singular branch只是

\[
\boxed{p\mid\mathscr F_{1270}.}
\tag{5.3}
\]

真实 endpoint中 `Q^2N_0` 为 `O(N^4)` 而 `1270B^2` 仅 `O(N^2)`，故 `F_1270<0` 对大 `M` 明显远离 real zero；但 simple p-adic roots仍可能存在，不能仅凭符号排除。

---

## 6. revised overlap frontier

因此 `Rstar_63/D_63` common support的 generic quadratic elimination已经审计完毕：

1. 消 `C` 只回到 original `That_2`；
2. 消 `K` 的 apparent new discriminant在 `That_2=0` 上自动成为平方；
3. 剩余 singular support只在
   \[
   TK-9T-2a_3
   \]
   与
   \[
   1270B^2-Q^2N_0
   \]
   两张显式低维 gate。

所以下一步不应继续叠 ordinary resultants/Legendre symbols。最有价值的是审计 `F_1270` 与 original prime-source三类的 support交集，或者利用 `Rstar_63<That_2/(24*5^lambda)` 的 height drop做 multiplicative budget。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-dual-gap-mobius"></a>

> 整合来源：`spontaneous-crt-dual-gap-mobius.md`

# A2 dual additive gaps 的 full-`5^lambda` Möbius synchronization

> **依赖：** `spontaneous-crt-gap-full5-residue.md`、`endpoint-lattice.md` §§16.34–16.38。
>
> **严格状态：**前一层给出右 gap `Delta_+` 的 full-`5^lambda` residue。本文把 exact curvature `Gamma_Delta=Delta_--Delta_+` 加回去，得到左 gap `Delta_-` 的同深 residue。两者的比值因此在模 `5^lambda` 下等于一个只含 `(qW_q,D,C)` 的 source Möbius ratio。Archimedean 上，真实 gap ratio 的 excess over `1` 约为 `60/K`，source ratio只约为 `1/K`，所以二者严格有序。其 cross-determinant 是正整数、被 `5^lambda` 整除；除去该完整 `5`-层后得到一个 normalized value落在固定 `(6,10)` 窗口的新 positive carrier。本文不证明该 carrier为空，因此不关闭 A2。

---

## 1. right gap full residue

沿用

\[
\Delta_+:=\frac{\Xi_+-\Xi_C}{L}>0,
\qquad L=2^m5^d,
\]

以及前一文件的 full-depth residue

\[
\boxed{
\Delta_+
\equiv
c_u^2a_3[D(20-4K)-2C]
\pmod{5^\lambda}.}
\tag{1.1}
\]

同时

\[
\boxed{v_5(\Delta_+)=0.}
\tag{1.2}
\]

---

## 2. curvature modulo `5^lambda`

记

\[
\Gamma_\Delta:=\Delta_--\Delta_+.
\]

`endpoint-lattice.md` (16.245) 给 exact formula

\[
\boxed{
\Gamma_\Delta
=2^{m+1}5^dc_u^2
\{g((2K-9)T-a_3)-H_0\}.}
\tag{2.1}
\]

使用

\[
H_0=g(3T+a_3)-5^\lambda C
\]
可把 bracket 精确写成

\[
g((2K-12)T-2a_3)+5^\lambda C.
\]

因为 `T` 的 `5`-进深度为 `m=lambda+d`，乘上前面的 `5^d` 后，所有含 `T` 或 `5^lambda C` 的项在模 `5^lambda` 下消失。只剩

\[
\Gamma_\Delta
\equiv
-2^{m+2}5^dg c_u^2a_3
\pmod{5^\lambda}.
\]

而

\[
D=g2^m5^d,
\]
所以

\[
\boxed{
\Gamma_\Delta
\equiv-4Dc_u^2a_3
\pmod{5^\lambda}.}
\tag{2.2}
\]

---

## 3. left gap full residue

由 `Delta_-=Delta_++Gamma_Delta`，结合 (1.1),(2.2)：

\[
\boxed{
\Delta_-
\equiv
c_u^2a_3[D(16-4K)-2C]
\pmod{5^\lambda}.}
\tag{3.1}
\]

模 `5` 仍有

\[
\Delta_-
\equiv-2c_u^2a_3C\not\equiv0\pmod5,
\]
所以

\[
\boxed{v_5(\Delta_-)=0.}
\tag{3.2}
\]

用

\[
qW_q=DK-(3D-C)
\]
可写成对称 height form：

\[
\boxed{
\Delta_-
\equiv
2c_u^2a_3(2D+C-2qW_q)
\pmod{5^\lambda},}
\tag{3.3-}
\]

\[
\boxed{
\Delta_+
\equiv
2c_u^2a_3(4D+C-2qW_q)
\pmod{5^\lambda}.}
\tag{3.3+}
\]

---

## 4. positive source Möbius pair

真实 endpoint 中 `K` 巨大，因此定义两个正整数

\[
\boxed{
A_s:=2qW_q-2D-C
=2D(K-4)+C,}
\tag{4.1}
\]

\[
\boxed{
B_s:=2qW_q-4D-C
=2D(K-5)+C.}
\tag{4.2}
\]

显然

\[
A_s=B_s+2D>B_s>0.
\]

因为 `5|D` 而 `5\nmid C`：

\[
\boxed{5\nmid A_sB_s.}
\tag{4.3}
\]

(3.3±) 于是等价于

\[
\Delta_-\equiv-2c_u^2a_3A_s,
\qquad
\Delta_+\equiv-2c_u^2a_3B_s
\pmod{5^\lambda}.
\]

消去共同 unit：

\[
\boxed{
\Delta_-B_s
\equiv
\Delta_+A_s
\pmod{5^\lambda}.}
\tag{4.4}
\]

或者在 unit ratio语言中

\[
\boxed{
\frac{\Delta_-}{\Delta_+}
\equiv
\frac{A_s}{B_s}
\pmod{5^\lambda}.}
\tag{4.5}
\]

---

## 5. the real gap ratio is much steeper

由 `Delta_-=Delta_++Gamma_Delta`：

\[
\frac{\Delta_-}{\Delta_+}
=1+\frac{\Gamma_\Delta}{\Delta_+}.
\]

`endpoint-lattice.md` 已给 bracket的安全窗口

\[
gT(2K-15)
<g((2K-9)T-a_3)-H_0
<2gTK.
\tag{5.1}
\]

于是 (2.1) 与 `D=g2^m5^d` 给

\[
2Dc_u^2T(2K-15)
<\Gamma_\Delta
<4Dc_u^2TK.
\tag{5.2}
\]

另一方面 `spontaneous-crt-quotient-source-scale.md` 已证明

\[
\frac{TK^2}{17}
<\mathscr S_+
<\frac{TK^2}{15},
\]
且

\[
\Delta_+=c_u^2D\mathscr S_+.
\]

所以对当前 `K>9*10^11`：

\[
\boxed{
1+\frac{59}{K}
<
\frac{\Delta_-}{\Delta_+}
<
1+\frac{68}{K}.}
\tag{5.3}
\]

这里下界只用

\[
\frac{30(2K-15)}{K^2}>rac{59}{K}
\qquad(K>450).
\]

---

## 6. source ratio has only `1/K` excess

由 (4.1),(4.2)：

\[
\frac{A_s}{B_s}
=1+\frac{2D}{2D(K-5)+C}
=1+\frac1{K-5+C/(2D)}.
\]

而

\[
0<\frac C{2D}<\frac3{500}<1.
\]

所以

\[
\boxed{
1+\frac1{K-4}
<
\frac{A_s}{B_s}
<
1+\frac1{K-5}.}
\tag{6.1}
\]

因此 `K>10` 时：

\[
\boxed{
\frac{57}{K}
<
\frac{\Delta_-}{\Delta_+}
-
\frac{A_s}{B_s}
<
\frac{68}{K}.}
\tag{6.2}
\]

真实 cubic-gap curvature相对于 source Möbius slope存在固定数量级差，不可能在实数上相等。

---

## 7. positive full-depth cross-determinant

定义

\[
\boxed{
\mathscr E_\Delta
:=\Delta_-B_s-\Delta_+A_s.}
\tag{7.1}
\]

由 (4.4)：

\[
\boxed{5^\lambda\mid\mathscr E_\Delta.}
\tag{7.2}
\]

由 (6.2) 与正性：

\[
\mathscr E_\Delta
=\Delta_+B_s
\left(
\frac{\Delta_-}{\Delta_+}
-
\frac{A_s}{B_s}
\right)>0.
\tag{7.3}
\]

使用

\[
\frac{c_u^2DTK^2}{17}<\Delta_+<\frac{c_u^2DTK^2}{15},
\]

\[
2D(K-5)<B_s<2D(K-4),
\]
和 (6.2)，可安全得到

\[
\boxed{
6c_u^2D^2TK^2
<\mathscr E_\Delta
<10c_u^2D^2TK^2.}
\tag{7.4}
\]

因此定义 positive integer

\[
\boxed{
\widehat{\mathscr E}_\Delta
:=\frac{\mathscr E_\Delta}{5^\lambda}
\in\mathbf Z_{>0}.}
\tag{7.5}
\]

由于 `T=L5^lambda`：

\[
\boxed{
6c_u^2D^2LK^2
<\widehat{\mathscr E}_\Delta
<10c_u^2D^2LK^2.}
\tag{7.6}
\]

所以 normalized cross-determinant拥有固定 `(6,10)` Archimedean window。

---

## 8. role of the new carrier

`Ehat_Delta` 同时读取：

1. additive cubic curvature `Delta_-/Delta_+`；
2. source reduced-height ratio `qW_q/D`；
3. 完整 reflection `5^lambda` synchronization；
4. 一个固定 positive natural-representative window。

它没有自动变成 `<1`，所以本文不把 (7.6) 冒充高度矛盾。真正可继续收费的是：把 `Ehat_Delta` 与 `Z_Delta` 的 extra-`d` reader或三 cofactor 的 `3 mod4` parity联立，检查同一 full-`5` cancellation是否还能同时承担 centered Hensel digit。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-dual-gap-remainder"></a>

> 整合来源：`spontaneous-crt-dual-gap-remainder.md`

# A2 dual-gap synchronization 产生的 short `3 mod 4` remainder

> **依赖：** `spontaneous-crt-dual-gap-mobius.md`、`spontaneous-crt-quotient-source-scale.md`、`endpoint-lattice.md` §§16.34–16.38。
>
> **严格状态：**前一文件构造 positive full-`5^lambda` cross-determinant `E_Delta`，除去 `5^lambda` 后粗略落在 `(6,10)` natural-scale window。本文使用 `S_+/T` 的 exact quadratic form把该窗口压到 `(7.87,63/8)`。因此从上端最佳有理近似 `63/8` 提取出 canonical positive integer remainder `R_63=63B_Delta-8 Ehat_Delta`，其高度严格小于 parent scale的 `1/25`。更重要的是，exact `2`-adic gap valuations给 `v_2(R_63)=m+4`，其 primitive quotient恒为 `3 mod4`，所以这个缩短后的 remainder必产生一份 odd-inert parity。本文仍未证明该新 parity support与已有 pools完全分离，因此不关闭 A2。

---

## 1. normalized cross-determinant

沿用 positive full-depth cross determinant

\[
\mathscr E_\Delta
:=\Delta_-B_s-\Delta_+A_s,
\]

\[
5^\lambda\mid\mathscr E_\Delta,
\qquad
\widehat{\mathscr E}_\Delta
:=\frac{\mathscr E_\Delta}{5^\lambda}>0.
\]

定义 parent natural scale

\[
\boxed{
\mathscr B_\Delta
:=c_u^2D^2LK^2,}
\qquad T=L5^\lambda.
\tag{1.1}
\]

记

\[
\delta:=\frac CD,
\qquad
r:=3-\delta,
\qquad
\zeta:=\frac{a_3}{T}.
\]

已有

\[
0<\delta<\frac3{250},
\qquad
\frac{747}{250}<r<3,
\qquad
1<\zeta<\frac{251}{250}.
\tag{1.2}
\]

cross determinant可写成

\[
\mathscr E_\Delta
=\Gamma_\Delta B_s-2D\Delta_+,
\]

其中 exact

\[
\Gamma_\Delta
=2c_u^2DT(2K-12-2\zeta+\delta),
\]

\[
B_s=D(2K-10+\delta),
\]

\[
\Delta_+=c_u^2D\mathscr S_+.
\]

所以

\[
\boxed{
\frac{\widehat{\mathscr E}_\Delta}{\mathscr B_\Delta}
=2\frac{(2K-12-2\zeta+\delta)(2K-10+\delta)}{K^2}
-2\frac{\mathscr S_+/T}{K^2}.}
\tag{1.3}
\]

所有 factor-allocation scale已经消失。

---

## 2. exact expansion around `63/8`

前一 source-scale文件给

\[
\frac{\mathscr S_+}{T}
=
\frac{
\zeta^2K^2-2\mathcal L(r,\zeta)K+\mathcal C(r,\zeta)
}{(r+\zeta)^2}.
\]

代入 (1.3) 并整理：

\[
\boxed{
\frac{\widehat{\mathscr E}_\Delta}{\mathscr B_\Delta}
=
8-rac{2\zeta^2}{(r+\zeta)^2}
+\frac{C_1(r,\zeta)}K
+\frac{C_2(r,\zeta)}{K^2},}
\tag{2.1}
\]

其中

\[
\boxed{
C_1
=-4\frac{
2r^3+4r^2\zeta+9r^2+r\zeta^2+18r\zeta+9\zeta^2
}{(r+\zeta)^2},}
\tag{2.2}
\]

\[
\boxed{
C_2
=2\frac{
r^4+2r^3\zeta+9r^3+18r^2\zeta+26r^2
+9r\zeta^2+52r\zeta+26\zeta^2
}{(r+\zeta)^2}.}
\tag{2.3}
\]

在 box (1.2) 中直接粗估即可得到

\[
\boxed{-70<C_1<-40,\qquad0<C_2<130.}
\tag{2.4}
\]

---

## 3. strict upper bound `63/8`

因为 `r<3`、`zeta>1`：

\[
3\zeta>r,
\]
所以

\[
\frac\zeta{r+\zeta}>\frac14.
\]

因此 leading part严格满足

\[
8-rac{2\zeta^2}{(r+\zeta)^2}
<8-\frac18
=\frac{63}{8}.
\tag{3.1}
\]

由 (2.4)，只要 `K>4`：

\[
\frac{C_1}{K}+\frac{C_2}{K^2}
<-rac{40}{K}+rac{130}{K^2}<0.
\]

当前 `K>9*10^{11}`，故

\[
\boxed{
\frac{\widehat{\mathscr E}_\Delta}{\mathscr B_\Delta}
<\frac{63}{8}.}
\tag{3.2}
\]

---

## 4. strict lower bound `7.87`

由

\[
r>\frac{747}{250},
\qquad
\zeta<\frac{251}{250},
\]
有

\[
\frac\zeta{r+\zeta}<\frac{251}{998}.
\]

所以 leading part

\[
8-rac{2\zeta^2}{(r+\zeta)^2}
>
8-2\left(\frac{251}{998}\right)^2
>7.87349.
\tag{4.1}
\]

由 (2.4)：

\[
\frac{C_1}{K}+\frac{C_2}{K^2}
>-rac{70}{K}.
\]

而 `K>9*10^{11}`，故

\[
\boxed{
\frac{787}{100}=7.87
<
\frac{\widehat{\mathscr E}_\Delta}{\mathscr B_\Delta}.}
\tag{4.2}
\]

结合 (3.2)：

\[
\boxed{
\frac{787}{100}
<
\frac{\widehat{\mathscr E}_\Delta}{\mathscr B_\Delta}
<
\frac{63}{8}.}
\tag{4.3}
\]

---

## 5. canonical `63/8` remainder drops height by at least `25`

定义 ordinary integer

\[
\boxed{
\mathscr R_{63}
:=63\mathscr B_\Delta
-8\widehat{\mathscr E}_\Delta.}
\tag{5.1}
\]

由 (4.3)：

\[
\boxed{\mathscr R_{63}>0.}
\tag{5.2}
\]

下界 `Ehat/B>787/100` 又给

\[
\frac{\mathscr R_{63}}{\mathscr B_\Delta}
<63-8\cdot\frac{787}{100}
=\frac1{25}.
\]

所以

\[
\boxed{
0<\mathscr R_{63}
<\frac1{25}\mathscr B_\Delta.}
\tag{5.3}
\]

这是一个真正的 natural-representative descent：没有改变原 endpoint，只从 exact full-`5` synchronization中构造出一个至少短 `25` 倍的正整数。

---

## 6. exact two-adic depth of the cross determinant

已有

\[
\boxed{v_2(\Gamma_\Delta)=m+1,}
\tag{6.1}
\]

而 `B_s=2D(K-5)+C` 为 odd。

另一方面

\[
v_2(\Delta_+)=1,
\qquad
v_2(D)=m+t-1,
\qquad t\ge3.
\]

所以

\[
v_2(2D\Delta_+)=m+t+1\ge m+4.
\]

由

\[
\mathscr E_\Delta=\Gamma_\Delta B_s-2D\Delta_+
\]
第一项唯一最浅：

\[
\boxed{v_2(\mathscr E_\Delta)=m+1.}
\tag{6.2}
\]

`5^lambda` 为 odd，故

\[
\boxed{v_2(\widehat{\mathscr E}_\Delta)=m+1.}
\tag{6.3}
\]

---

## 7. exact two-adic depth of the short remainder

parent scale有

\[
\mathscr B_\Delta=c_u^2D^2LK^2.
\]

其中

\[
v_2(D)=m+t-1,
\quad v_2(L)=m,
\quad v_2(K)=1,
\quad c_u\text{ odd}.
\]

因此

\[
\boxed{v_2(\mathscr B_\Delta)=3m+2t.}
\tag{7.1}
\]

而

\[
v_2(8\widehat{\mathscr E}_\Delta)=m+4.
\]

因为 `m>=5,t>=3`：

\[
3m+2t>m+4.
\]

所以 (5.1) 中第二项唯一最浅：

\[
\boxed{v_2(\mathscr R_{63})=m+4.}
\tag{7.2}
\]

定义 primitive positive remainder

\[
\boxed{
\widehat{\mathscr R}_{63}
:=\frac{\mathscr R_{63}}{2^{m+4}}
\in\mathbf Z_{>0}\text{ odd}.}
\tag{7.3}
\]

---

## 8. primitive remainder is always `3 mod 4`

先读 `Ehat` 的 primitive unit。由 §6：

\[
\frac{\mathscr E_\Delta}{2^{m+1}}
\equiv
5^dc_u^2
\{g((2K-9)T-a_3)-H_0\}B_s
\pmod4.
\]

因为 `g` 被 `4` 整除：

\[
g((2K-9)T-a_3)-H_0
\equiv-H_0\pmod4.
\]

又 `D` 被 `4` 整除，所以

\[
B_s=2D(K-5)+C\equiv C\pmod4.
\]

而 source relation

\[
H_0=g(3T+a_3)-5^\lambda C
\]
给

\[
H_0\equiv-C\pmod4.
\]

由于 `5^d,c_u^2,5^lambda` 都为 `1 mod4`：

\[
\boxed{
\frac{\widehat{\mathscr E}_\Delta}{2^{m+1}}
\equiv(-H_0)C
\equiv C^2
\equiv1\pmod4.}
\tag{8.1}
\]

parent term `63B_Delta` 在除以 `2^{m+4}` 后仍被 `4` 整除，因为其二进深度远大于 `m+6`。所以从 (5.1)：

\[
\widehat{\mathscr R}_{63}
\equiv
-\frac{\widehat{\mathscr E}_\Delta}{2^{m+1}}
\equiv-1
\equiv3\pmod4.
\]

因此

\[
\boxed{
\widehat{\mathscr R}_{63}
>0,
\qquad
\widehat{\mathscr R}_{63}\equiv3\pmod4.}
\tag{8.2}
\]

所以它必含至少一枚 `3 mod4` prime到奇次。

---

## 9. current role

这是当前 additive CRT / Gaussian chain中第一条同时具有以下四点的 carrier：

1. 由 full `5^lambda` synchronization自然产生；
2. real height相对 parent natural scale严格下降至少 `25` 倍；
3. exact primitive `2`-depth为 `m+4`；
4. primitive quotient无条件为 positive `3 mod4`。

因此 `Rhat_63` 是一个新的短 odd-inert parity supplier。下一步最有价值的是研究它与原 `widehat T_2`、`P_Delta` 以及 source-common/target pools的 support overlap；若能证明至少一组 separation，就会把这份下降后的 parity升级成真正的新 distinct-prime cost。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-external-center-fixed139-463"></a>

> 整合来源：`spontaneous-crt-external-center-fixed139-463.md`

# A2 external discriminant-zero center 与 descendant common 的 fixed `139/463` orbits

> **依赖：** `external-secant-center.md`、`length-orbit.md`、`spontaneous-crt-universal-descendant-cubic.md`、`spontaneous-crt-height-descent-overlap.md`。
>
> **严格状态：**universal descendant cubic限制到 external discriminant-zero center `K=55/18, zeta=-55/18` 后，genuine external character只留下 fixed `139,463`。本文把这两枚 prime代回 `length-orbit.md` 的 fully coupled三方程，并与真实 decimal multiplicative orbit联立。`139` 留一组 genuine state，`463` 留两组；三点 full Jacobian均非零，且 `10` 的 exponent direction在相应 order上都非-Wieferich，所以每组至多一条唯一 p-adic decimal lift。它们与此前 height/source-common/descendant triple-overlap 的 fixed set `{139,463}` 完全一致，不构成新的第四 prime-source。本文不排除这三条 simple orbits，因此不关闭 A2。

---

## 1. universal cubic reduces the external center to `139,463`

external discriminant-zero common center给

\[
\boxed{
K_*=\frac{55}{18},
\qquad
\zeta_*=-\frac{55}{18}.}
\tag{1.1}

所以

\[
\alpha=T(K_*+\zeta_*)=0.
\]

universal descendant cubic在 `alpha=0`, 即 `zeta=-K`, 上因成

\[
\boxed{
\mathcal E_{63}(K,-K)
=-9G_D(K)^2Q_4(K),}
\tag{1.2}

其中

\[
G_D(K)=11K^2-240K+432,
\]

\[
Q_4(K)=5055K^4-44640K^3-91424K^2+612864K-539136.
\]

代入 `K=55/18`：

\[
\boxed{
G_D(55/18)
=-\frac{64357}{324}
=-\frac{139\cdot463}{324},}
\tag{1.3}

\[
\boxed{
Q_4(55/18)
=-\frac{12349325707}{34992}
=-\frac{257\cdot48051851}{34992}.}
\tag{1.4}

fully coupled external prime还必须满足

\[
p\equiv3\pmod4,
\qquad
\left(\frac{55}{p}\right)=1.
\tag{1.5}

四个 odd numerator primes中：

- `139,463` 均为 `3 mod4` 且 `(55/p)=1`；
- `257` 为 `1 mod4`；
- `48051851` 为 `3 mod4`，但 `(55/p)=-1`。

因此

\[
\boxed{
\text{external center}\cap\text{descendant common}
\subseteq\{139,463\}.}
\tag{1.6}

---

## 2. fully coupled finite-field equations

`length-orbit.md` 使用

\[
\boxed{s=36\cdot10^{M-1},}
\qquad
Y_s=11-9s,
\tag{2.1}

以及 external prefix root

\[
y=Y_s/s.
\tag{2.2}

三个 fully coupled equations为

\[
\boxed{
\mathcal N_{sp}(s,x)
=(x+2)^2(2025s^2x^2+Y_s^2)+10780x^2,}
\tag{2.3}

\[
\boxed{
\begin{aligned}
\mathcal O_{sp}(s,x,r_s)={}&
r_s[4(225sx^2+9s-11)^2\\
&\qquad-xY_s^2(99x-4)]
+2xY_s^2(x+2),
\end{aligned}}
\tag{2.4}

\[
\boxed{
\mathcal G_{sp}(x,r_s)
=55r_s^2(x+2)^2-49x^2.}
\tag{2.5}

当前 fixed-prime audit只保留满足

\[
\mathcal N_{sp}=\mathcal O_{sp}=\mathcal G_{sp}=0
\]
且 `s` 位于真实 decimal orbit `36<10>` 的 unit states。

---

## 3. `p=139`: exactly one genuine state

模 `139`：

\[
\operatorname{ord}_{139}(10)=46.
\]

遍历完整 decimal orbit

\[
s=36\cdot10^{M-1}
\]
并对每个 orbit point解 (2.3)--(2.5)，只得到

\[
\boxed{
(s,x,y,r_s)=(94,124,34,41)
\pmod{139}.}
\tag{3.1}

对应 exponent phase为

\[
\boxed{M\equiv44\pmod{46}.}
\tag{3.2}

它满足全部 genuine separation：

\[
x(x+2)y\ne0,
\]

\[
\boxed{
\Phi_s=(99x-4)r_s-2x-4
\equiv137\ne0\pmod{139},}
\tag{3.3}

\[
\boxed{
r_s(x+2)+2x\equiv132\ne0\pmod{139}.}
\tag{3.4}

所以既不是 source Hensel line，也不是 f-denominator boundary。

---

## 4. `p=463`: exactly two genuine states

模 `463`：

\[
\operatorname{ord}_{463}(10)=154.
\]

完整 decimal-orbit枚举只留下两组：

\[
\boxed{
(s,x,y,r_s)=(141,299,349,458),}
\tag{4.1}

\[
\boxed{
(s,x,y,r_s)=(172,328,376,416)
\pmod{463}.}
\tag{4.2}

对应

\[
\boxed{M\equiv140\pmod{154},}
\tag{4.3}

\[
\boxed{M\equiv147\pmod{154}.}
\tag{4.4}

两组均 genuine：

第一组

\[
\boxed{
\Phi_s\equiv36,
\qquad
r_s(x+2)+2x\equiv19
\pmod{463},}
\tag{4.5}

第二组

\[
\boxed{
\Phi_s\equiv318,
\qquad
r_s(x+2)+2x\equiv425
\pmod{463}.}
\tag{4.6}

全部为 units。

---

## 5. all three states are simple in the full system

对

\[
(\mathcal N_{sp},\mathcal O_{sp},\mathcal G_{sp})
\]
关于 `(s,x,r_s)` 的 Jacobian determinant，三点分别为

\[
\boxed{111\pmod{139},}
\tag{5.1}

\[
\boxed{397,\qquad159\pmod{463}.}
\tag{5.2}

全部非零。因此 multivariate Hensel lemma给：

\[
\boxed{
\text{每个 finite-field state至多有一条 compatible }p\text{-adic lift}.}
\tag{5.3}

不存在 external-center descendant singular tree。

---

## 6. decimal exponent direction is also simple

直接计算：

\[
\boxed{
10^{46}
\equiv1+43\cdot139
\pmod{139^2},}
\tag{6.1}

\[
\boxed{
10^{154}
\equiv1+217\cdot463
\pmod{463^2}.}
\tag{6.2}

`43,217` 都是相应 prime的 units，所以

\[
v_{139}(10^{46}-1)=1,
\qquad
v_{463}(10^{154}-1)=1.
\]

因此每个 simple state与 decimal exponent orbit联立后仍只有唯一 exponent lift：

\[
\boxed{
139:\ 1\text{ 条 unique decimal-Hensel orbit},}
\tag{6.3}

\[
\boxed{
463:\ 2\text{ 条 unique decimal-Hensel orbits}.}
\tag{6.4}

继续机械提升 `p^k` 只会刚性化这些 branches，不会自动制造局部空性。

---

## 7. these are exactly the known triple-overlap labels

`spontaneous-crt-height-descent-overlap.md` 已独立证明：若 descendant common prime同时属于 sphere-height 与 source-common support，则

\[
\boxed{p\in\{139,463\}.}
\tag{7.1}

external discriminant-zero center本身含 source-common center

\[
18K-55=0,
\]
并处于 `alpha=0` 的 content/height decomposition。

因此本文 surviving `139/463` states并不是新的第四类 descendant-common prime-source；它们正是既有 fixed triple-overlap labels的 actual fully-coupled local realizations。

所以 global common-parity ledger中不应把

\[
\text{external center }139/463
\]
与

\[
\text{height/source-common overlap }139/463
\]
重复计数。

---

## 8. current role

external discriminant-zero center + descendant common已从 moving prime问题压成：

\[
\boxed{
1\text{ 条 }139\text{-adic simple orbit}
+2\text{ 条 }463\text{-adic simple orbits}.}
\]

它们没有被 local finite-field compatibility排除，但也没有任何 local branching自由。

下一步若继续该 fixed center，应把三条 unique lifts接到 finite-defect centered representative或 descent height bound；继续只做 Hensel lift属于机械刚性化。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-extra-d-z-reader"></a>

> 整合来源：`spontaneous-crt-extra-d-z-reader.md`

# A2 additive CRT 的 extra-`d` centered-`z_E` reader

> **依赖：** `spontaneous-crt-gap-full5-residue.md`、`spontaneous-crt-gaussian-floorfree-carrier.md`、`endpoint-lattice.md` §§16.22–16.24。
>
> **严格状态：**前一文件证明 floor-free orientation carrier `P_Delta` 在完整 `5^lambda` 上具有显式 unit residue；endpoint Hensel kernel已有 exact lift `g r_E=c_+c_u+5^{lambda-d}z_E`。本文把两式合并。由于 reflection 中 `lambda>2d`，平方 lift 的二次 `z_E^2` 项在模 `5^lambda` 自动消失；除去公共 `5^{lambda-d}` 后，恰好剩下 `d` 个 digits，并线性读取 `z_E mod 5^d`。因此由 decimal defect `H mod g` 唯一中心化的 `z_E` 现在还必须满足一个来自 additive CRT/Gaussian carrier的独立 `5^d` 余类。本文把旧 extra-`d` alignment变成显式双模 compatibility，但尚未证明该系统无解，因此不关闭 A2。

---

## 1. full-`5` CRT residue

令

\[
\boxed{
R_\Delta^{(5)}
:=D(20-4K)-2C.}
\tag{1.1}
\]

前一文件给

\[
\boxed{
\mathscr P_\Delta
\equiv
2^{A_G}c_u^2a_3R_\Delta^{(5)}
\pmod{5^\lambda}.}
\tag{1.2}
\]

并证明

\[
5\nmid R_\Delta^{(5)}c_ua_3\mathscr P_\Delta.
\tag{1.3}
\]

---

## 2. exact centered Hensel lift

`endpoint-lattice.md` §16.23 定义

\[
\boxed{
n_5:=5^{\lambda-d}}
\tag{2.1}
\]

以及 centered odd representative `z_E`，并有 exact identity

\[
\boxed{
g r_E=c_+c_u+n_5z_E.}
\tag{2.2}
\]

reflection 的 primitive `5`-depth满足

\[
\nu_5=\lambda-2d>0.
\tag{2.3}
\]

因此

\[
2(\lambda-d)=\lambda+\nu_5>\lambda,
\]
即

\[
\boxed{n_5^2\equiv0\pmod{5^\lambda}.}
\tag{2.4}
\]

---

## 3. square the Hensel lift only to first order in `z_E`

由 (2.2)：

\[
c_+c_u=gr_E-n_5z_E.
\]

平方：

\[
c_+^2c_u^2
=g^2r_E^2-2gr_En_5z_E+n_5^2z_E^2.
\]

使用 (2.4)：

\[
\boxed{
c_+^2c_u^2
\equiv
g^2r_E^2-2gr_En_5z_E
\pmod{5^\lambda}.}
\tag{3.1}
\]

所以 full `5^lambda` 层只保留 `z_E` 的**线性**修正；quadratic lift自动落到模数之外。

---

## 4. define the top-`d` digit carrier

将 (1.2) 乘以 `c_+^2`，再代入 (3.1)：

\[
\begin{aligned}
c_+^2\mathscr P_\Delta
\equiv{}&
2^{A_G}a_3R_\Delta^{(5)}g^2r_E^2\\
&-2^{A_G+1}a_3R_\Delta^{(5)}gr_E\,n_5z_E
\pmod{5^\lambda}.
\end{aligned}
\tag{4.1}
\]

特别地，第一层模 `n_5` 已给

\[
\boxed{
n_5\mid
\left(
c_+^2\mathscr P_\Delta
-2^{A_G}a_3R_\Delta^{(5)}g^2r_E^2
\right).}
\tag{4.2}
\]

因此定义 ordinary integer

\[
\boxed{
\mathscr Z_\Delta
:=
\frac{
c_+^2\mathscr P_\Delta
-2^{A_G}a_3R_\Delta^{(5)}g^2r_E^2
}{n_5}.}
\tag{4.3}
\]

由于

\[
5^\lambda=n_5\,5^d,
\]
把 (4.1) 除以 `n_5` 正好得到最后 `d` digits：

\[
\boxed{
\mathscr Z_\Delta
\equiv
-2^{A_G+1}a_3R_\Delta^{(5)}gr_Ez_E
\pmod{5^d}.}
\tag{4.4}
\]

---

## 5. eliminate `r_E` from the coefficient

由 (2.2)：

\[
gr_E\equiv c_+c_u\pmod{n_5}.
\]

又因 `lambda>2d`：

\[
\lambda-d>d,
\]
故该同余当然可降到模 `5^d`：

\[
\boxed{gr_E\equiv c_+c_u\pmod{5^d}.}
\tag{5.1}
\]

代入 (4.4)：

\[
\boxed{
\mathscr Z_\Delta
\equiv
-2^{A_G+1}a_3R_\Delta^{(5)}c_+c_u z_E
\pmod{5^d}.}
\tag{5.2}
\]

所有 coefficient都是 `5`-进 units：

\[
5\nmid2a_3R_\Delta^{(5)}c_+c_u.
\]

因此可以唯一反解

\[
\boxed{
z_E
\equiv
-\left(
2^{A_G+1}a_3R_\Delta^{(5)}c_+c_u
\right)^{-1}
\mathscr Z_\Delta
\pmod{5^d}.}
\tag{5.3}
\]

这是真正的 extra-`d` digit reader。

---

## 6. combine with the decimal-defect centered representative

同一个 `z_E` 此前已经由真实 denominator defect `H` 唯一确定：

\[
\boxed{
-\frac g2<z_E<\frac g2,}
\tag{6.1}
\]

\[
\boxed{
c_-z_E
\equiv-5^{d+1}H
\pmod g,}
\tag{6.2}
\]

并且

\[
\gcd(z_E,g)=1.
\]

由于

\[
\gcd(g,5)=1,
\]
(5.3),(6.2) 形成真正的 coprime two-modulus compatibility：

\[
\boxed{
\begin{cases}
 c_-z_E\equiv-5^{d+1}H\pmod g,\\[1mm]
 2^{A_G+1}a_3R_\Delta^{(5)}c_+c_u z_E
 \equiv-\mathscr Z_\Delta\pmod{5^d},\\[1mm]
 |z_E|<g/2.
\end{cases}}
\tag{6.3}
\]

第一式已经唯一选出 `z_E` 的 centered integer；第二式因此不是新的自由选择，而是对该唯一自然代表施加一个深 `5^d` compatibility test。

---

## 7. relation to the old extra-`d` alignment

`endpoint-lattice.md` §16.8 曾把 Gaussian quotient kernel压成两个 `5`-primitive vectors，其 projective determinant仍被迫额外对齐恰好 `d` 位。此前这份 `d`-depth主要以 Gaussian orientation存在。

本文表明 additive CRT exact gap也读取**同一层数**：

\[
5^\lambda
=
5^{\lambda-d}\cdot5^d
\]

中的前 `lambda-d` digits由 centered scalar `r_E` 读取，最后 `d` digits恰线性读取 `z_E`。

所以 old extra-`d` alignment现在有一个纯整数 additive representative `Z_Delta`，而不是只存在于 Gaussian determinant中。

---

## 8. revised frontier

当前 reflection high-2 mixed kernel可以按下面顺序完全 canonical 化：

\[
H\bmod g
\Longrightarrow
z_E\in(-g/2,g/2)
\Longrightarrow
r_E
\Longrightarrow
\mathscr P_\Delta
\Longrightarrow
\mathscr Z_\Delta\bmod5^d.
\]

真正新的 closure target是证明唯一 centered `z_E` 从 (6.2) 得到的自然值不满足 (5.3)。由于 `d` 随 `M` 可线性增长，这不再是固定层的小同余；它是一个无界 mixed-radix compatibility。

若能把 (5.3) 进一步只写成 `(H,C)` 或 `(z_E,chi_E)` 的低高度函数，就有机会利用 `|z_E|<g/2` 与 signed bridge `P_Delta z_E chi_E<0` 完成矛盾。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-f-descent-separation"></a>

> 整合来源：`spontaneous-crt-f-descent-separation.md`

# A2 f-denominator inert carrier 与 descendant common support 只剩 fixed height `7`

> **依赖：** `spontaneous-denominator-depth-matrix.md`、`endpoint-lattice.md` 的 canonical factor allocation、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-target-descent-overlap.md`。
>
> **严格状态：**完整 f-saturation 中，third-block saturation给 `2a_3+9T=0`，exact factor allocation进一步在完整 `p^e` 深度给 `DK=6D+C`。代入 descended quotient后，`Dhat_63` 的截断深度被 pure quadratic `G_D=11K^2-240K+432` 精确读取。原 f-additive denominator depth则由 `P_f=3K^2-36K+26` 读取。两 quadratic 的 resultant只有 `2,7,73,977`，唯一 inert prime是 fixed `7`。该 root `K=1 mod7` 又强迫 `7|W_q,H_0`，所以它实际属于已有 sphere-height channel，并且由于 resultant中 `7` 只出现一层，f-denominator/descent common gcd在该 label上最多只贡献一层。本文删除 generic f-denominator common channel，但不排除 fixed height-7 本身，因此不关闭 A2。

---

## 1. saturated f-prime data

固定 genuine non-`3` inert prime

\[
p^e\Vert f,
\qquad
p^e\mid\mathscr L_{23},
\qquad e\ge1,
\]

其中

\[
\mathscr L_{23}=\frac{9T}{2}+a_3.
\]

于是

\[
\boxed{2a_3+9T\equiv0\pmod{p^e}.}
\tag{1.1}

`spontaneous-denominator-depth-matrix.md` 已把 original additive f-depth降成

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),e\}
=
\min\{v_p(P_f(K)),e\},}
\tag{1.2}

\[
\boxed{P_f(K):=3K^2-36K+26.}
\tag{1.3}

---

## 2. exact f-allocation gives `DK=6D+C mod p^e`

沿用 canonical Gaussian factor equalities

\[
\mathcal A-Z=5^{\lambda-d}fN,
\tag{2.1}
\]

\[
\mathcal A+Z=5^{\lambda-d}q c_+^2Y,
\tag{2.2}
\]

以及

\[
\mathcal A=c_u5^{\lambda-d}DK.
\tag{2.3}
\]

模 `p^e`，因为 `p^e|f`，(2.1) 给

\[
Z\equiv\mathcal A.
\]

所以 (2.2) 给

\[
2c_uDK
\equiv q c_+^2Y
\pmod{p^e}.
\tag{2.4}

又

\[
f=5^\lambda q+2c_u
\equiv0\pmod{p^e},
\]
所以

\[
q\equiv-2c_u5^{-\lambda}\pmod{p^e}.
\]

代入 (2.4)，消去 unit `2c_u`：

\[
5^\lambda DK+c_+^2Y\equiv0\pmod{p^e}.
\tag{2.5}

reflection factor equality为

\[
\boxed{
c_+^2Y
=g(3T+2a_3)-5^\lambda C.}
\tag{2.6}

由 (1.1)：

\[
3T+2a_3\equiv-6T\pmod{p^e}.
\]

再用

\[
gT=D5^\lambda,
\]
得到

\[
c_+^2Y
\equiv-5^\lambda(6D+C)\pmod{p^e}.
\]

代回 (2.5)，并消去 `5^lambda`：

\[
\boxed{
DK\equiv6D+C\pmod{p^e}.}
\tag{2.7}

因为 f-prime与 `D` 分离，定义

\[
\delta:=C/D
\]
后：

\[
\boxed{\delta\equiv K-6\pmod{p^e}.}
\tag{2.8}

这是一条 full prime-power allocation，不只是 first-layer relation。

---

## 3. descendant depth becomes a second pure K-quadratic

cleared descended quotient为

\[
\boxed{
\begin{aligned}
F_{63}^{(16)}={}&
16(2K-9)
\{g((2K-12)T-2a_3)+5^\lambda C\}\\
&-63gTK^2.
\end{aligned}}
\tag{3.1}

`Dhat_63` 与它只差 genuine p-units。

除以 unit `gT`，再使用 (1.1),(2.8)：

\[
\frac{F_{63}^{(16)}}{gT}
\equiv
32(K-6)K-144(K-6)+K^2-384K+432.
\]

右边精确化简为

\[
\boxed{
\frac{F_{63}^{(16)}}{gT}
\equiv3G_D(K)\pmod{p^e},}
\tag{3.2}

其中

\[
\boxed{G_D(K):=11K^2-240K+432.}
\tag{3.3}

`p` 为 non-3，所以 `3` 为 unit。因此

\[
\boxed{
\min\{v_p(\widehat{\mathscr D}_{63}),e\}
=
\min\{v_p(G_D(K)),e\}.}
\tag{3.4}

这给 saturated f-channel 一个新的 descendant depth reader。

---

## 4. two pure quadratics leave only fixed `7,73,977`

若 f-denominator prime同时进入 descendant common support，则 first layer必须

\[
P_f(K)\equiv0,
\qquad
G_D(K)\equiv0
\pmod p.
\]

resultant为

\[
\boxed{
\operatorname{Res}_K(P_f,G_D)
=-1996988
=-2^2\cdot7\cdot73\cdot977.}
\tag{4.1}

三个 odd candidates的 mod-4 classes为

\[
7\equiv3,
\qquad
73\equiv1,
\qquad
977\equiv1
\pmod4.
\]

所以 genuine inert overlap只剩

\[
\boxed{p=7.}
\tag{4.2}

common root唯一为

\[
\boxed{K\equiv1\pmod7.}
\tag{4.3}

因此 generic f-denominator inert support与 descendant common kernel完全分离；唯一例外是 fixed `7`。

---

## 5. fixed `7` automatically belongs to the height channel

在 `p=7,K=1` 下，由 (2.8)：

\[
\delta\equiv K-6\equiv2\pmod7.
\]

而

\[
N=3D-C=D(3-\delta),
\]
所以

\[
\boxed{N\equiv D\pmod7.}
\tag{5.1}

于是

\[
DK-N
\equiv D-N
\equiv0\pmod7.
\tag{5.2}

又 `7|f`，而 source split有

\[
\gcd(q,f)=1.
\]

因此

\[
7\nmid q.
\]

由全局 quotient

\[
DK-N=qW_q
\]
可消去 q-unit：

\[
\boxed{7\mid W_q.}
\tag{5.3}

已有 height theorem 对每个 non-3 inert divisor of `W_q` 给

\[
\boxed{v_7(W_q)=v_7(H_0),}
\tag{5.4}

\[
\boxed{\left(\frac{N_0}{7}\right)=-1.}
\tag{5.5}

因此 fixed f/descent overlap并不是新的 denominator-external label，而是

\[
\boxed{
\text{fixed }7\text{ sphere-height channel}.}
\tag{5.6}

---

## 6. the fixed overlap is transverse and contributes only one common layer

resultant (4.1) 中 `7` 的 exponent恰为 `1`。因此 Bezout identity给：

\[
\boxed{
\min\{v_7(P_f),v_7(G_D)\}=1}
\tag{6.1}

在任何 simultaneous f/descent lift上成立。

由 depth readers (1.2),(3.4)，若 `e>=2`，则 original additive f-depth与 descended quotient depth不可能同时超过一层；若 `e=1` 更是平凡。

而 descendant common factor

\[
G_\Delta=\gcd(Rstar_{63},Dhat_{63})
\]
若在 `7` 上有两层，则 descent identity会使 `That_2,Dhat_63` 都至少有两层，与 (6.1) 矛盾。因此

\[
\boxed{
v_7(G_\Delta)=1}
\tag{6.2}

在 fixed f-denominator overlap存在时成立。

所以它最多向 descendant common parity支付一份 squarefree `7`，不存在 f-denominator 驱动的 deep common Hensel tree。

---

## 7. denominator channels are now removed from generic common parity

结合 q-side complete separation：

\[
\boxed{
q\text{-denominator inert}
\cap\operatorname{Supp}(G_\Delta)=\varnothing,}
\tag{7.1}

而本文给

\[
\boxed{
f\text{-denominator inert}
\cap\operatorname{Supp}(G_\Delta)
\subseteq\{7\},}
\tag{7.2}

且 `7` 已重分类到 sphere-height support并仅一层。

因此 `spontaneous-crt-descendant-common-parity.md` 中尚未解释的 common inert parity已经不再含 generic q/f denominator source。剩余 old-pool labels为：

1. fixed target `31/179`；
2. source-common overlap的 double-short depth；
3. fixed height shadow `7`；
4. genuinely endpoint-external/spontaneous common kernel。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-f1270-source-audit"></a>

> 整合来源：`spontaneous-crt-f1270-source-audit.md`

# A2 descent singular gate `F_1270` 的 prime-source audit

> **依赖：** `spontaneous-crt-descent-overlap-nogo.md`、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-source-target-support-separation.md`、`spontaneous-height-equal-depth-dual-short-carriers.md`。
>
> **严格状态：**`Rstar_63/D_63` overlap 的 ordinary resultant审计只留下 pure-prefix singular gate `F_1270=1270B^2-Q^2N_0` 与 third-central gate。本文专门审计 `F_1270`。与 original carrier `That_2` 联立后，`F_1270` 自动产生一个 third/prefix quadratic `G_1270`。该 quadratic与 central/source-common/omega/height/target carriers的 resultants全部显式且短。特别地，若 `F_1270` overlap同时属于 equal-depth target，则 moving prime被压成 fixed set `{7,79,107,199}`；四个 common third-block roots均为 first-layer transverse collision，不产生新的双深 Hensel tree。本文没有排除这四个 fixed primes及 generic external `F_1270` roots，因此不关闭 A2。

---

## 1. positive form and primitive orientation of the pure-prefix gate

定义 singular factor

\[
\boxed{
F_{1270}:=1270B^2-Q^2N_0.}
\tag{1.1}
\]

真实 endpoint中更自然使用正整数

\[
\boxed{
H_{1270}:=-F_{1270}=Q^2N_0-1270B^2.}
\tag{1.2}
\]

利用

\[
x=B/N,\qquad y=10A/N,
\]

\[
\frac{N_0}{N^2}=rac{2025x^2+y^2}{100},
\]
有

\[
\frac{H_{1270}}{N^4}
=
\frac{(x+2)^2(2025x^2+y^2)}{100}
-rac{1270x^2}{N^2}.
\tag{1.3}
\]

endpoint box与 `N>=10^11` 给安全窗口

\[
\boxed{
\frac{117}{125}N^4
<H_{1270}
<\frac{26}{25}N^4.}
\tag{1.4}
\]

所以 `F_1270` 在实数上远离零；它只可能作为 p-adic singular gate出现。

二进结构也固定。`Q=2^{M+1}Q_0`、`N_0` odd，而 `1270B^2` 比 `Q^2N_0` 多至少 `2m+1` 层二进深度。因此

\[
\boxed{
v_2(H_{1270})=2M+2,}
\tag{1.5}
\]

\[
\boxed{
\frac{H_{1270}}{2^{2M+2}}
\equiv Q_0^2N_0
\equiv1\pmod8.}
\tag{1.6}
\]

所以 `H_1270` 本身是 positive `1 mod8` primitive carrier；它不额外强迫 odd-inert parity。

---

## 2. intersection with the original forced carrier gives `G_1270`

令

\[
U:=2^{M+1}.
\]

由 denominator normal forms可把 original primitive additive carrier写成 exact identity

\[
\boxed{
U^2 2^m\widehat{\mathcal T}_2
=
B^2F_0-TQ^2N_0,}
\tag{2.1}
\]

其中

\[
\boxed{
F_0
:=TK^2-(18T+4a_3)K+18a_3+55T.}
\tag{2.2}
\]

固定 genuine odd prime `p`，并假设

\[
p\mid\widehat{\mathcal T}_2,
\qquad
p\mid F_{1270}.
\tag{2.3}
\]

`gcd(That_2,10c_ug)=1`，而 `B=2^{M+m+1}c_ug`，所以

\[
\boxed{p\nmid B.}
\tag{2.4}
\]

由 `F_1270=0`：

\[
Q^2N_0\equiv1270B^2\pmod p.
\]

代入 (2.1) 并消去 `B^2`：

\[
\boxed{
G_{1270}
:=TK^2-(18T+4a_3)K+18a_3-1215T
\equiv0\pmod p.}
\tag{2.5}
\]

等价地

\[
\boxed{
G_{1270}
=T(K^2-18K-1215)-2a_3(2K-9).}
\tag{2.6}
\]

所以 noncentral `F_1270` overlap会唯一同步 `a_3/T` 的 projective unit；central branch需要单列。

---

## 3. central overlap collapses to fixed `7`

直接对 `K` 求 resultant：

\[
\boxed{
\operatorname{Res}_K(G_{1270},2K-9)
=-5103T
=-3^6\cdot7\,T.}
\tag{3.1}
\]

在 genuine non-`3` sector，`p∤T`，因此

\[
\boxed{
p\mid G_{1270},\quad p\mid2K-9
\Longrightarrow p=7.}
\tag{3.2}
\]

所以 `F_1270` singular overlap若再次进入 central additive sheet，不存在 moving prime；只剩 fixed `7`。

---

## 4. source-common overlap pays a short third-block linear carrier

source-common moving support进入

\[
18K-55.
\]

resultant为

\[
\boxed{
\operatorname{Res}_K(G_{1270},18K-55)
=1872a_3-408455T.}
\tag{4.1}
\]

定义 positive carrier

\[
\boxed{
L_{1270}^{src}
:=408455T-1872a_3.}
\tag{4.2}
\]

由

\[
1<a_3/T<251/250
\]
得到

\[
\boxed{
406575T<L_{1270}^{src}<406583T.}
\tag{4.3}
\]

因此任何 source-common prime若同时进入 `F_1270` singular overlap，其 prime depth至少需要在这个只有 `m+6` 位量级的 third-block linear integer中重新出现。

---

## 5. omega-content overlap produces a new fixed-`79` third carrier

若

\[
p\mid\omega,
\]
则

\[
\alpha=TK+a_3\equiv0\pmod p.
\]

resultant：

\[
\operatorname{Res}_K(G_{1270},TK+a_3)
=T(-1215T^2+36Ta_3+5a_3^2).
\]

定义 positive odd carrier

\[
\boxed{
H_{79}:=1215T^2-36Ta_3-5a_3^2.}
\tag{5.1}
\]

则 genuine omega-overlap满足

\[
\boxed{p\mid H_{79}.}
\tag{5.2}
\]

endpoint window给

\[
\boxed{
1173T^2<H_{79}<1174T^2.}
\tag{5.3}
\]

`T` 为偶、`a_3` odd，因此

\[
\boxed{H_{79}\equiv3\pmod4.}
\tag{5.4}
\]

把 `H_79` 看成关于 `a_3` 的 quadratic，其 discriminant为

\[
\boxed{
\operatorname{Disc}_{a_3}(H_{79})
=25596T^2
=18^2\cdot79\,T^2.}
\tag{5.5}
\]

所以对 genuine inert prime `p≡3 mod4`、`p∤2\cdot3\cdot79T`：

\[
\boxed{p\mid H_{79}\Longrightarrow(79/p)=1.}
\tag{5.6}
\]

因为 `79≡3 mod4`，quadratic reciprocity给

\[
\boxed{(p/79)=-1.}
\tag{5.7}
\]

这是 `F_1270` omega-content overlap的 fixed-79 orientation。仓库此前没有使用该 `79` character；本文暂不宣称它与其它 character独立到足以闭环。

---

## 6. `q/W_q` support pays a short source-defect carrier

任意 prime若进入 `qW_q` support，则

\[
DK-(3D-C)\equiv0\pmod p.
\]

对 `K` 消元：

\[
\boxed{
\begin{aligned}
\operatorname{Res}_K(
G_{1270},DK-(3D-C))
={}&C^2T+12CDT+4CDa_3\\
&-1260D^2T+6D^2a_3.
\end{aligned}}
\tag{6.1}
\]

定义其正相反数

\[
\boxed{
L_{1270}^{H}
:=1260D^2T-6D^2a_3
-12CDT-4CDa_3-C^2T.}
\tag{6.2}
\]

写 `delta=C/D`、`zeta=a_3/T`：

\[
\frac{L_{1270}^{H}}{D^2T}
=1260-6\zeta-(12+4\zeta)\delta-\delta^2.
\]

由

\[
0<\delta<3/250,
\qquad1<\zeta<251/250
\]
得到

\[
\boxed{
1253D^2T<L_{1270}^{H}<1254D^2T.}
\tag{6.3}
\]

所以 `q` denominator / `W_q` height overlap也不能自由复用；必须进入一个显式 short source-defect natural representative。

---

## 7. equal-depth target overlap collapses to four fixed primes

真正 equal-depth target同时满足

\[
p\mid\omega
\]
和 third short carrier

\[
p\mid R_3,
\qquad
R_3=6(a_3+3T)^2+T^2.
\]

由 §5 同时有 `p|H_79`。直接 resultant：

\[
\boxed{
\operatorname{Res}_{a_3}(H_{79},R_3)
=58875145T^4
=5\cdot7\cdot79\cdot107\cdot199\,T^4.}
\tag{7.1}
\]

在 genuine non-`5` target sector：

\[
\boxed{
F_{1270}\text{ singular overlap}
+\text{equal-depth target}
\Longrightarrow
p\in\{7,79,107,199\}.}
\tag{7.2}
\]

所以这部分 moving target support完全消失，只剩四个 fixed primes。

逐 prime把 `T` 归一为 `1`，并同时施加

\[
H_{79}=R_3=0,
\qquad
P(K)=6K^2-36K+55=0,
\qquad
G_{1270}=0
\]
得到唯一 first-layer state：

\[
\boxed{
\begin{array}{c|c|c}
p&a_3/T\pmod p&K\pmod p\\ \hline
7&5&2\\
79&28&51\\
107&11&96\\
199&83&116
\end{array}}
\tag{7.3}
\]

`p=7,K=2` 正好与已经存在的 fixed-7 equal-depth target orbit对齐。

---

## 8. the four target collisions are only first-layer transverse

(7.1) 中每个 genuine candidate prime `7,79,107,199` 的 exponent都恰为 `1`。

resultant的 Bezout identity因此说明：若同一 candidate上

\[
p^2\mid H_{79},
\qquad
p^2\mid R_3,
\]
则会迫使 `p^2` 整除 (7.1) 的右边，矛盾。

因此

\[
\boxed{
\min\{v_p(H_{79}),v_p(R_3)\}=1
\qquad
(p\in\{7,79,107,199\}).}
\tag{8.1}
\]

特别地，若 target baseline `h=v_p(R_3)>=2`，则

\[
\boxed{v_p(H_{79})=1.}
\tag{8.2}
\]

所以 `F_1270` 与 equal-depth target的 fixed collision不会形成一个新的双深/奇异 Hensel tree。

---

## 9. target-resultant character is only the old `sqrt(-6)` shadow

直接消去 `K`：

\[
\boxed{
\operatorname{Res}_K(G_{1270},P(K))
=57169585T^2-543816Ta_3+1392a_3^2.}
\tag{9.1}
\]

记右边为 `H_6`。endpoint中

\[
56624000T^2<H_6<56628000T^2.
\]

其 discriminant为

\[
\boxed{
\operatorname{Disc}_{a_3}(H_6)
=-22584407424T^2
=-6(61352T)^2.}
\tag{9.2}
\]

所以 ordinary quadratic character只重复 target quadratic `P(K)` 已有的 `sqrt(-6)` orientation；不能把 (9.1) 再当一条 independent Legendre obstruction收费。

真正新的 target信息是 §7 的 fixed-prime collapse，而不是这个 discriminant。

---

## 10. revised singular frontier

`F_1270` singular sheet现在按已有 prime-source分成：

1. central `2K-9` overlap：只剩 fixed `7`；
2. source-common `18K-55` overlap：进入 short linear `L_1270^src`；
3. omega-content overlap：进入 positive `3 mod4` short carrier `H_79`，并获得 fixed-79 orientation；
4. q/height support：进入 short `L_1270^H`；
5. equal-depth target：moving support完全缩成 fixed `{7,79,107,199}`，且共同 third depth横截。

因此 `F_1270` 仍可能有 generic external simple roots，但它与已经昂贵/已分类的 prime pools的交集都已大幅缩窄。

下一步最值得做的是审计 fully primitive short remainder `Rstar_63` 的 forced inert prime能否属于 generic external `F_1270` root；若不能，original/remainder parity就必须真正分裂为不同 primes。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-floorfree-full2-square"></a>

> 整合来源：`spontaneous-crt-floorfree-full2-square.md`

# A2 floor-free CRT carrier 的 full-`2^{A_G}` square class

> **依赖：** `spontaneous-crt-gaussian-floorfree-carrier.md`、`spontaneous-crt-gap-full5-residue.md`、`endpoint-lattice.md` low-`m` reflection bounds。
>
> **严格状态：**`P_Delta` 的 mod-8 orientation此前已用于 parity。本文证明低 `m` reflection cone中 `D^2` 实际被完整 `2^{A_G}` 吞掉，因此 `P_Delta` 在同一增长模数上精确满足 `P_Delta≡5^{B_G}k_h^3 C^2 mod2^{A_G}`。也就是说除去显式 odd factor后，floor-free CRT/Gaussian carrier具有由真实 top defect `C` 给出的完整 2-adic square root。结合已有 full-`5^lambda` residue，`P_Delta` 现在同时携带两个随 `M` 增长的独立 local fingerprints。本文不单独关闭 A2。

---

## 1. exponents

定义

\[
A_G:=\frac{M+5\eta}{2}+8,
\qquad
B_G:=3M-d-\eta-3,
\qquad
\eta=2m-M.
\]

因此

\[
\boxed{A_G=5m-2M+8.}
\tag{1.1}
\]

reflection source factor为

\[
g=2^{t-1}\rho,
\qquad t\ge3,
\]
所以

\[
D=g2^m5^d
\]
满足

\[
\boxed{v_2(D)=m+t-1\ge m+2.}
\tag{1.2}
\]

于是

\[
2v_2(D)\ge2m+4.
\]

比较 (1.1)：

\[
2m+4-A_G
=2M-3m-4.
\]

当前 low-`m` cone有

\[
m\le\frac{6M}{11},
\qquad M\ge11.
\]

因此

\[
2M-3m-4
\ge\frac{4M}{11}-4
\ge0.
\]

所以

\[
\boxed{2v_2(D)\ge A_G.}
\tag{1.3}
\]

等价地

\[
\boxed{2^{A_G}\mid D^2.}
\tag{1.4}
\]

---

## 2. CRT modulus modulo the full 2-adic scale

令

\[
M_\Delta:=D^2-C^2.
\]

由 (1.4)：

\[
\boxed{
M_\Delta\equiv-C^2\pmod{2^{A_G}}.}
\tag{2.1}
\]

`C` 为 odd，所以 `C^2` 是模 `2^{A_G}` 的 unit square。

---

## 3. full square-class formula for `P_Delta`

floor-free carrier定义为

\[
\mathscr P_\Delta
=2^{A_G}\Delta_+
-5^{B_G}k_h^3M_\Delta.
\]

模 `2^{A_G}` 第一项消失；用 (2.1)：

\[
\boxed{
\mathscr P_\Delta
\equiv
5^{B_G}k_h^3C^2
\pmod{2^{A_G}}.}
\tag{3.1}
\]

因为 `5,k_h,C` 都为 odd，右边是 unit。

把显式 unit移到左边：

\[
\boxed{
\mathscr P_\Delta
(5^{B_G}k_h^3)^{-1}
\equiv C^2
\pmod{2^{A_G}}.}
\tag{3.2}
\]

所以 `P_Delta/(5^{B_G}k_h^3)` 的完整 2-adic unit class不只是 mod-8 square character；其实际 square root就是 top defect `C`。

---

## 4. signed absolute-value version

已有

\[
\operatorname{sgn}(\mathscr P_\Delta)=-\varepsilon.
\]

所以

\[
|\mathscr P_\Delta|=(-\varepsilon)\mathscr P_\Delta.
\]

由 (3.1)：

\[
\boxed{
|\mathscr P_\Delta|
\equiv
(-\varepsilon)5^{B_G}k_h^3C^2
\pmod{2^{A_G}}.}
\tag{4.1}
\]

因此 Gaussian side `epsilon` 精确决定绝对 carrier相对于显式 factor `5^{B_G}k_h^3` 是 `+square` 还是 `-square` 的完整 2-adic lift。

模 `8` 时 (4.1) 正好恢复 parent parity theorem；本文是其 full-depth strengthening。

---

## 5. combine with the full-`5^lambda` fingerprint

前一文件已有

\[
\boxed{
\mathscr P_\Delta
\equiv
2^{A_G}c_u^2a_3[D(20-4K)-2C]
\pmod{5^\lambda},}
\tag{5.1}
\]

且

\[
v_5(\mathscr P_\Delta)=0.
\]

现在同一个 ordinary integer `P_Delta` 同时满足：

\[
\boxed{
\begin{cases}
\mathscr P_\Delta
\equiv5^{B_G}k_h^3C^2
\pmod{2^{A_G}},\\[1mm]
\mathscr P_\Delta
\equiv2^{A_G}c_u^2a_3[D(20-4K)-2C]
\pmod{5^\lambda},\\[1mm]
\operatorname{sgn}(\mathscr P_\Delta)=-\varepsilon.
\end{cases}}
\tag{5.2}
\]

由于 `gcd(2^{A_G},5^lambda)=1`，(5.2) 是一个真正的 bi-adic signed fingerprint，而不是同一 local congruence的重复写法。

---

## 6. current role

full `2`-adic square root直接使用真实 top defect `C`，full `5`-adic residue则已经在 `spontaneous-crt-extra-d-z-reader.md` 中线性读取 centered `z_E mod5^d`。

所以后续可尝试把 `(C,z_E)` 两个自然代表共同送入 `P_Delta` 的 CRT class；若 combined residue的最小 signed representative与 `sgn(P_Delta)=-epsilon` 不相容，就能真正排除 Gaussian side。

目前 modulus product仍不足以单靠大小覆盖 `|P_Delta|`，因此本文不宣称 natural representative唯一，也不关闭 A2。

---

<a id="source-spontaneous-crt-floorfree-modulus-overlap"></a>

> 整合来源：`spontaneous-crt-floorfree-modulus-overlap.md`

# A2 floor-free carrier 与 CRT modulus 的 adjacent-contact overlap

> **依赖：** `spontaneous-crt-gaussian-floorfree-carrier.md`、`spontaneous-crt-quotient-source-scale.md`、`endpoint-lattice.md` §§16.33–16.38。
>
> **严格状态：**当 `|P_Delta|≡3 mod4` 时，它产生新的 odd-inert parity；CRT modulus `D^2-C^2` 本身也为 `3 mod4`。本文审计两份 parity能否由同一 prime复用。由于 `P_Delta` 模 CRT modulus只剩 `2^{A_G}Delta_+`，common gcd精确等于 `gcd(Delta_+,D^2-C^2)`。利用 `D Delta_+` 的显式整数式，在 `D-C`、`D+C` 两张互素 denominator sheet上得到 exact divisibility decompositions：任何 common prime的完整 exponent必须进入两个固定-sign adjacent contact carrier `F_2` 或 `F_4`。二者绝对值都只有约 `50 c_u^2 T N^2`。因此 parity reuse要么分裂成不同 residual primes，要么支付给这两个短 contact carriers之一。本文不证明 `F_2,F_4` 无 genuine roots，因此不关闭 A2。

---

## 1. common gcd reduces to the right gap

定义

\[
M_\Delta:=D^2-C^2=(D-C)(D+C).
\]

`D` 为偶、`C` 为奇，所以 `M_Delta` 为 positive odd integer，并且

\[
\gcd(D-C,D+C)=1.
\tag{1.1}
\]

floor-free carrier为

\[
\mathscr P_\Delta
=2^{A_G}\Delta_+-5^{B_G}k_h^3M_\Delta.
\]

因为 `M_Delta` 为 odd，`2^{A_G}` 在其每个 prime factor上为 unit。因此

\[
\boxed{
\gcd(\mathscr P_\Delta,M_\Delta)
=\gcd(\Delta_+,M_\Delta).}
\tag{1.2}
\]

并且由 (1.1)：

\[
\boxed{
\gcd(\Delta_+,M_\Delta)
=\gcd(\Delta_+,D-C)\,\gcd(\Delta_+,D+C).}
\tag{1.3}
\]

两因子互素。

---

## 2. exact integer formula for `D Delta_+`

沿用

\[
N_s:=3D-C.
\]

已有

\[
\boxed{
\begin{aligned}
D\Delta_+
={}&c_u^2\Bigl[
D^2(TK^2-14KT-4Ka_3+37T+14a_3)\\
&+DN_s(-2KT+7T+2a_3)+TN_s^2
\Bigr]\\
&-z^2N_s(TN_s+2a_3D).
\end{aligned}}
\tag{2.1}
\]

该式是下面两张 denominator sheet 的 complete natural representative。

---

## 3. `D-C` sheet: full common depth enters `F_2`

定义

\[
\boxed{
\begin{aligned}
F_2:={}&
c_u^2[TK^2-(18T+4a_3)K+55T+18a_3]\\
&-4z^2(T+a_3).
\end{aligned}}
\tag{3.1}
\]

直接展开 (2.1) 得 exact decomposition

\[
\boxed{
D\Delta_+
=D^2F_2+(C-D)R_2,}
\tag{3.2}
\]

其中

\[
\boxed{
\begin{aligned}
R_2={}&CT(c_u^2-z^2)
+2DKTc_u^2-12DTc_u^2+5DTz^2\\
&-2Da_3c_u^2+2Da_3z^2.
\end{aligned}}
\tag{3.3}
\]

固定 odd prime `p` 且

\[
p^k\mid\Delta_+,
\qquad
p^k\mid D-C.
\]

由 `gcd(C,D)=1`，若 `p|D-C` 则 `p∤D`。因此 (3.2) 给

\[
\boxed{p^k\mid F_2.}
\tag{3.4}
\]

注意这是完整 common exponent `k`，不是只读 first layer。

---

## 4. `D+C` sheet: full common depth enters `F_4`

定义

\[
\boxed{
\begin{aligned}
F_4:={}&
c_u^2[TK^2-(22T+4a_3)K+81T+22a_3]\\
&-8z^2(2T+a_3).
\end{aligned}}
\tag{4.1}
\]

同样 exact 展开：

\[
\boxed{
D\Delta_+
=D^2F_4+(C+D)R_4,}
\tag{4.2}
\]

其中

\[
\boxed{
\begin{aligned}
R_4={}&CT(c_u^2-z^2)
+2DKTc_u^2-14DTc_u^2+7DTz^2\\
&-2Da_3c_u^2+2Da_3z^2.
\end{aligned}}
\tag{4.3}
\]

因此

\[
p^k\mid\Delta_+,
\qquad p^k\mid D+C
\]
强迫

\[
\boxed{p^k\mid F_4.}
\tag{4.4}
\]

---

## 5. both contact carriers have fixed Archimedean sign

利用 source identity

\[
\frac z{c_u}=\frac{TQ}{b_3}=\frac Qw,
\qquad w:=\frac{b_3}{T},
\tag{5.1}
\]

以及 normalized variables

\[
s:=\frac KN,
\qquad x:=\frac BN,
\qquad \zeta:=\frac{a_3}{T},
\]
有

\[
\frac{F_2}{c_u^2TN^2}
=s^2-rac{(18+4\zeta)s}{N}
+rac{55+18\zeta}{N^2}
-4\left(\frac{2+x}{w}\right)^2(1+\zeta),
\tag{5.2}
\]

\[
\frac{F_4}{c_u^2TN^2}
=s^2-rac{(22+4\zeta)s}{N}
+rac{81+22\zeta}{N^2}
-8\left(\frac{2+x}{w}\right)^2(2+\zeta).
\tag{5.3}
\]

当前 endpoint box为

\[
\frac1{10}<x<\frac2{19},
\quad
\frac{2499}{250}<s<10,
\quad
1<\zeta<\frac{251}{250},
\quad
\frac{837}{1000}<w<\frac{843}{1000},
\quad N\ge10^{11}.
\]

直接取端点可得到安全 strict windows

\[
\boxed{
49<\frac{F_2}{c_u^2TN^2}<51,}
\tag{5.4}
\]

\[
\boxed{
48<\frac{-F_4}{c_u^2TN^2}<53.}
\tag{5.5}
\]

所以

\[
\boxed{F_2>0,\qquad F_4<0.}
\tag{5.6}
\]

两张 overlap sheet分别由一个 positive 和一个 negative short natural carrier读取，尺度都只有 `~50 c_u^2 T N^2`。

---

## 6. canonical parity-reuse dichotomy

当

\[
|\mathscr P_\Delta|\equiv3\pmod4
\]
时，`P_Delta` 强迫一份 odd-inert parity；另一方面

\[
M_\Delta=D^2-C^2\equiv3\pmod4
\]
也强迫一份。

定义

\[
G_{PM}:=\gcd(|\mathscr P_\Delta|,M_\Delta).
\]

约去 common gcd：

\[
P_1:=|\mathscr P_\Delta|/G_{PM},
\qquad
M_1:=M_\Delta/G_{PM},
\]
且

\[
\gcd(P_1,M_1)=1.
\]

若

\[
G_{PM}\equiv1\pmod4,
\]
则

\[
P_1\equiv M_1\equiv3\pmod4,
\]
所以两份 parity必须由两个不同 residual primes承担。

若

\[
G_{PM}\equiv3\pmod4,
\]
则 common gcd本身承担 odd-inert parity；而 §§3–4 说明其中每一枚 genuine common prime的完整 exponent都必须进入 `F_2` 或 `F_4`。

因此

\[
\boxed{
\text{`P_Delta` / CRT-modulus parity reuse}
\Longrightarrow
\begin{cases}
\text{two distinct residual inert suppliers},\\
\text{or}\quad
\text{full-depth adjacent contact in }F_2\text{ or }F_4.
\end{cases}}
\tag{6.1}
\]

这把“新 parity是否会被旧 CRT modulus免费复用”改写成一个明确的 short-contact问题。

---

## 7. current frontier

下一步若能证明 genuine inert roots of `F_2,F_4` 只能落在 fixed / already-paid support，四个 `eta=1` parity-active types就会真正获得 distinct-prime surcharge。

目前 `F_2,F_4` 的 quadratic discriminants仍允许 simple moving roots，因此本文不把 short contact误称为空性。它的作用是把 common support从两个大 integers压到两条 explicit adjacent-secant natural representatives。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-floorfree-odd3-unit"></a>

> 整合来源：`spontaneous-crt-floorfree-odd3-unit.md`

# A2 floor-free CRT carrier 在 odd `3`-defect 中排除 prime `3`

> **依赖：** `spontaneous-crt-floorfree-parity.md`、`spontaneous-crt-quotient-source-scale.md`、`endpoint-lattice.md` §16.11。
>
> **严格状态：**前一 parity 文件只在 `eta=1,k_h=3` 类型证明 `3∤P_Delta`。本文指出该论证只使用 `v_3(k_h)` 为奇数时 §16.11 的统一结构，因此可推广到全部 reflection high-2 odd-`3` defect：若 `v_3(k_h)` 为奇数，则 `Delta_+` 与 `P_Delta` 都是 `3`-进 units。故任何由 `|P_Delta|≡3 mod4` 触发的 odd-inert parity都必须由 non-`3` inert prime支付。本文是 general surcharge lemma，不关闭 A2。

令

\[
e_3:=v_3(k_h).
\]

`endpoint-lattice.md` §16.11 已证明，若 `e_3` 为奇数，则只有两个局部通道，但二者统一满足

\[
\boxed{3\mid a_2,\qquad3\mid a_3,\qquad3\nmid b_2b_3g.}
\tag{1.1}
\]

同时 high/low 两个因子的 `3`-进深度都至少为一，因此

\[
3\mid H_0,\qquad3\mid Y_2.
\tag{1.2}
\]

由

\[
H_0=g(3T+a_3)-5^\lambda C
\]
及 (1.1)：

\[
\boxed{3\mid C.}
\tag{1.3}
\]

又

\[
K=9N+10a_2
\]
给

\[
\boxed{3\mid K.}
\tag{1.4}
\]

记

\[
N_s:=3D-C.
\]

由 (1.3)：

\[
\boxed{3\mid N_s.}
\tag{1.5}
\]

由于 `3∤b_2` 且

\[
b_2=2^{M+m+1}c_ug,
\]
有

\[
3\nmid c_ugD.
\tag{1.6}
\]

现在使用 exact right-gap formula

\[
\begin{aligned}
D\Delta_+
={}&c_u^2\Bigl[
D^2(TK^2-14KT-4Ka_3+37T+14a_3)\\
&+DN_s(-2KT+7T+2a_3)+TN_s^2
\Bigr]\\
&-z^2N_s(TN_s+2a_3D).
\end{aligned}
\]

模 `3` 使用 (1.1),(1.4),(1.5)，所有项消失，只剩

\[
D\Delta_+
\equiv c_u^2D^2T
\not\equiv0\pmod3.
\]

所以

\[
\boxed{e_3\text{ odd}\Longrightarrow3\nmid\Delta_+.}
\tag{1.7}
\]

floor-free carrier为

\[
\mathscr P_\Delta
=2^{A_G}\Delta_+
-5^{B_G}k_h^3(D^2-C^2).
\]

若 `e_3` 为奇数，则第二项被 `3` 整除，而第一项由 (1.7) 是 unit。因此

\[
\boxed{e_3\text{ odd}\Longrightarrow3\nmid\mathscr P_\Delta.}
\tag{1.8}
\]

另一方面 parent parity theorem给

\[
|\mathscr P_\Delta|\equiv3\pmod4
\iff
\varepsilon=(-1)^{e_3}.
\]

所以在 odd-`e_3` branch 中，只要 parity criterion触发，即 `epsilon=-1`，就严格有

\[
\boxed{
|\mathscr P_\Delta|\equiv3\pmod4,
\qquad3\nmid\mathscr P_\Delta,
}
\]

从而 `|P_Delta|` 必含至少一枚

\[
\boxed{p\ne3,\qquad p\equiv3\pmod4}
\]
到奇次。

这把 `eta=1,k_h=3` 的 non-`3` surcharge推广到整个 odd `3`-primary Gaussian defect。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-floorfree-parity"></a>

> 整合来源：`spontaneous-crt-floorfree-parity.md`

# A2 floor-free CRT/Gaussian carrier 的 mod-8 parity ledger

> **依赖：** `spontaneous-crt-gaussian-floorfree-carrier.md`、`endpoint-lattice.md` §§16.4–16.6、§16.11。
>
> **严格状态：**floor-free carrier `P_Delta` 已经读取 Gaussian side的符号。本文继续读取其 primitive `mod 8` orientation。由于 `2^{A_G}Delta_+` 含极深 `2`-幂，而 `D^2-C^2≡7 mod8`，有 `P_Delta≡5^{B_G}k_h mod8`。结合 `sgn(P_Delta)=-epsilon`，绝对值 `|P_Delta|` 是否为 `3 mod4` 只由 `epsilon` 与 `v_3(k_h)` 奇偶决定。施加到 `eta=1` 的五个 surviving Gaussian types，五型中四型强迫 `|P_Delta|≡3 mod4`。其中唯一 `k_h=3` 类型还可证明 `3∤P_Delta`，故必须生成一枚新的 non-`3` inert prime。本文给出 parity surcharge，但不排除该 prime由其它 residual support复用，因此不关闭 A2。

---

## 1. mod-8 orientation of `P_Delta`

定义

\[
\mathscr P_\Delta
=2^{A_G}\Delta_+
-5^{B_G}k_h^3(D^2-C^2),
\]

其中

\[
A_G=\frac{M+5\eta}{2}+8,
\qquad
B_G=3M-d-\eta-3.
\]

当前 `A_G>=8`，所以

\[
2^{A_G}\Delta_+\equiv0\pmod8.
\tag{1.1}
\]

`D=g2^m5^d` 有 `v_2(D)>=2`，而 `C` 为奇数。因此

\[
D^2-C^2\equiv-1\equiv7\pmod8.
\tag{1.2}
\]

于是

\[
\mathscr P_\Delta
\equiv-7\cdot5^{B_G}k_h^3
\equiv5^{B_G}k_h^3
\pmod8.
\]

任意奇数 `u` 满足 `u^3≡u mod8`，故

\[
\boxed{
\mathscr P_\Delta
\equiv5^{B_G}k_h
\pmod8.}
\tag{1.3}
\]

特别地模 `4`：

\[
\boxed{
\mathscr P_\Delta\equiv k_h\pmod4.}
\tag{1.4}
\]

---

## 2. absolute-value parity is controlled by the Gaussian side

已知

\[
\operatorname{sgn}(\mathscr P_\Delta)=-\varepsilon.
\]

所以

\[
|\mathscr P_\Delta|
=(-\varepsilon)\mathscr P_\Delta.
\]

由 (1.4)：

\[
\boxed{
|\mathscr P_\Delta|
\equiv(-\varepsilon)k_h
\pmod4.}
\tag{2.1}
\]

`endpoint-lattice.md` 已证明：若 `p|k_h` 且 `p≡3 mod4`，则只能 `p=3`。所以

\[
\boxed{
k_h\equiv(-1)^{v_3(k_h)}\pmod4.}
\tag{2.2}
\]

因此

\[
\boxed{
|\mathscr P_\Delta|\equiv3\pmod4
\iff
\varepsilon=(-1)^{v_3(k_h)}.}
\tag{2.3}
\]

若 (2.3) 成立，则 positive odd integer `|P_Delta|` 必含至少一枚 `3 mod4` prime到奇次。

---

## 3. apply to the five `eta=1` Gaussian types

`endpoint-lattice.md` (16.21) 已把 `eta=1` high-2 branch压成五型：

\[
\begin{array}{c|c}
d&(c_Q,k_h,\text{slot})\\ \hline
1&(3,53,+),(103,1,-),(159,1,+)\\
2&(7,3,-),(31,1,+).
\end{array}
\]

这里 `+/- slot` 就是 `epsilon=+1/-1`。

由于 `eta=1`，`M` 必为奇数。逐型使用 (1.3)：

\[
\boxed{
\begin{array}{c|c|c}
(d,c_Q,k_h,\varepsilon)&B_G\bmod2&|\mathscr P_\Delta|\bmod8\\ \hline
(1,3,53,+)&0&3\\
(1,103,1,-)&0&1\\
(1,159,1,+)&0&7\\
(2,7,3,-)&1&7\\
(2,31,1,+)&1&3
\end{array}}
\tag{3.1}
\]

所以五型中只有

\[
\boxed{(d,c_Q,k_h,\varepsilon)=(1,103,1,-)}
\]
不由 `P_Delta` 强迫 odd-inert parity；其余四型全部满足

\[
\boxed{|\mathscr P_\Delta|\equiv3\pmod4.}
\tag{3.2}
\]

---

## 4. the stubborn `k_h=3` type cannot pay with prime `3`

考虑

\[
(d,c_Q,k_h,\varepsilon)=(2,7,3,-).
\tag{4.1}
\]

`endpoint-lattice.md` (16.23) 已证明该型满足

\[
\boxed{3\mid a_2,\quad3\mid a_3,\quad3\nmid b_2b_3.}
\tag{4.2}
\]

由

\[
b_2=2^{M+m+1}c_ug
\]
得到

\[
3\nmid c_ug.
\tag{4.3}
\]

所以 `D=g2^m5^d` 也是 `3`-进 unit。

该型还使 `3|H_0`。由

\[
H_0=g(3T+a_3)-5^\lambda C
\]
和 (4.2),(4.3)：

\[
\boxed{3\mid C.}
\tag{4.4}
\]

又

\[
K=9N+10a_2,
\]
所以

\[
3\mid K.
\tag{4.5}
\]

记 `N_s=3D-C`，则由 (4.4)：

\[
3\mid N_s.
\tag{4.6}
\]

现在使用 `spontaneous-crt-quotient-source-scale.md` 的 exact formula

\[
\begin{aligned}
D\Delta_+
={}&c_u^2\Bigl[
D^2(TK^2-14KT-4Ka_3+37T+14a_3)\\
&+DN_s(-2KT+7T+2a_3)+TN_s^2
\Bigr]\\
&-z^2N_s(TN_s+2a_3D).
\end{aligned}
\]

模 `3`，使用 (4.2),(4.5),(4.6)，所有项消失，只剩

\[
\boxed{
D\Delta_+
\equiv c_u^2D^2T
\not\equiv0\pmod3.}
\tag{4.7}
\]

因 `D` 为 unit：

\[
\boxed{3\nmid\Delta_+.}
\tag{4.8}
\]

而 `3|k_h^3`，所以

\[
\mathscr P_\Delta
=2^{A_G}\Delta_+
-5^{B_G}k_h^3(D^2-C^2)
\equiv2^{A_G}\Delta_+
ot\equiv0\pmod3.
\]

故

\[
\boxed{3\nmid\mathscr P_\Delta.}
\tag{4.9}
\]

结合该型 `|P_Delta|≡7 mod8`：

\[
\boxed{
\text{该 }k_h=3\text{ 型必含一枚 non-`3` }p\equiv3\pmod4
\text{ prime 到奇次}.}
\tag{4.10}
\]

所以这里的 odd-inert surcharge不能由 Gaussian norm中已有的特殊 `3` defect支付。

---

## 5. current role

`P_Delta` 的 parity不是新的 quadratic character；它是 floor-free CRT/Gaussian signed carrier自身的 global arithmetic orientation。

对 `eta=1`：

- 四个 surviving types自动产生一份 odd-inert parity；
- 唯一 `k_h=3` 类型中，该 parity必须来自 non-`3` inert prime；
- `(1,103,1,-)` 是唯一 `P_Delta` parity-neutral type。

下一步若能证明这些 `P_Delta` inert suppliers与 `D^2-C^2`、`widehat T_2` 或已有 source-common/target pools不能复用，就会把四型升级成真正的 distinct-prime surcharge。本文尚未完成该 support separation，因此 A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-gap-full5-residue"></a>

> 整合来源：`spontaneous-crt-gap-full5-residue.md`

# A2 additive CRT right gap 的 full-`5^lambda` residue

> **依赖：** `endpoint-lattice.md` §§16.36–16.38、`spontaneous-crt-quotient-source-scale.md`、`spontaneous-crt-gaussian-floorfree-carrier.md`。
>
> **严格状态：**`Delta_+=(Xi_+-Xi_C)/(2^m5^d)` 此前只知道 `v_2(Delta_+)=1`，未显式记录其剩余 `5`-进深度。本文使用 additive lift `Ttilde_2-(D-C)Gammatilde_Delta=g Delta_+`，把两项在完整 `5^lambda` 层正规化，得到 `Delta_+` 的显式 full-depth residue。特别地 `Delta_+` 是精确 `5`-进单位。floor-free Gaussian orientation carrier `P_Delta` 继承同一 `5^lambda` unit residue。因此 additive exact gap、Gaussian side与 Hensel 的完整 reflection `5`-深度首次位于同一 ordinary integer carrier上。本文不单独关闭 A2。

---

## 1. additive lift

沿用

\[
L:=2^m5^d,
\qquad
D=gL,
\qquad
T=10^m,
\qquad
m=\lambda+d,
\]

以及

\[
\nu_5:=\lambda-2d>0.
\]

`endpoint-lattice.md` (16.265) 已有 exact integer lift

\[
\boxed{
\widetilde{\mathcal T}_2
-(D-C)\widetilde\Gamma_\Delta
=g\Delta_+.}
\tag{1.1}
\]

其中

\[
\boxed{
\widetilde\Gamma_\Delta
=c_u^2\{g((2K-9)T-a_3)-H_0\}.}
\tag{1.2}
\]

并且

\[
H_0=g(3T+a_3)-5^\lambda C.
\tag{1.3}
\]

---

## 2. `Gammatilde_Delta` modulo `5^lambda`

由 (1.2),(1.3)：

\[
\begin{aligned}
\widetilde\Gamma_\Delta
&=c_u^2\{g((2K-12)T-2a_3)+5^\lambda C\}.
\end{aligned}
\]

因为

\[
v_5(T)=m=\lambda+d>\lambda,
\]
所以模 `5^lambda`：

\[
\boxed{
\widetilde\Gamma_\Delta
\equiv-2gc_u^2a_3
\pmod{5^\lambda}.}
\tag{2.1}
\]

---

## 3. explicit formula for `Ttilde_2`

`endpoint-lattice.md` (16.259) 为

\[
\mathcal T_2
=
\frac{
2b_2^2T\,[TK^2-(18T+4a_3)K+18a_3+55T]
-2Q^2N_0T^2
}
{2^{2M+2}5^{\nu_5}DL}.
\]

又

\[
\widetilde{\mathcal T}_2
:=\frac{\mathcal T_2}{2^{m+1}5^d}.
\]

使用

\[
b_2=2^{M+m+1}c_ug,
\qquad
Q=2^{M+1}Q_0,
\qquad
\nu_5+2d=\lambda,
\]
逐项约分，得到 exact formula

\[
\boxed{
\begin{aligned}
\widetilde{\mathcal T}_2
={}&Lc_u^2g^2
[TK^2-(18T+4a_3)K+18a_3+55T]\\
&-5^{\lambda+2d}Q_0^2N_0.
\end{aligned}}
\tag{3.1}
\]

模 `5^lambda` 时所有含 `T` 的项都消失，最后一项也消失。因此

\[
\boxed{
\widetilde{\mathcal T}_2
\equiv
Lc_u^2g^2a_3(18-4K)
\pmod{5^\lambda}.}
\tag{3.2}
\]

---

## 4. full-depth residue for `Delta_+`

把 (2.1),(3.2) 代入 (1.1)：

\[
\begin{aligned}
g\Delta_+
&\equiv
Lc_u^2g^2a_3(18-4K)
+2g c_u^2a_3(D-C)\\
&=gc_u^2a_3
[D(18-4K)+2D-2C]\\
&=gc_u^2a_3
[D(20-4K)-2C]
\pmod{5^\lambda}.
\end{aligned}
\]

当前 source split给

\[
\gcd(g,5)=1,
\]
所以可以消去 `g`：

\[
\boxed{
\Delta_+
\equiv
c_u^2a_3[D(20-4K)-2C]
\pmod{5^\lambda}.}
\tag{4.1}
\]

这比只模 `n_5=5^{lambda-d}` 更强整整 `d` 层。

---

## 5. height form

使用

\[
qW_q=DK-(3D-C),
\]
有

\[
D(20-4K)-2C
=2(4D+C-2qW_q).
\]

所以 (4.1) 等价于

\[
\boxed{
\Delta_+
\equiv
2c_u^2a_3(4D+C-2qW_q)
\pmod{5^\lambda}.}
\tag{5.1}
\]

这把 additive right gap的 full `5`-residue直接接回 reduced height numerator `W_q`。

---

## 6. `Delta_+` is exactly a `5`-adic unit

reflection 中 `d>=1`，故

\[
5\mid D.
\]

同时

\[
K=10P,
\qquad 5\mid K.
\]

由 primitive reduction / defect coprimality：

\[
5\nmid c_ua_3C.
\]

将 (4.1) 模 `5`：

\[
\boxed{
\Delta_+
\equiv-2c_u^2a_3C
\not\equiv0\pmod5.}
\tag{6.1}
\]

因此

\[
\boxed{v_5(\Delta_+)=0.}
\tag{6.2}
\]

所以三个 cofactor先约去公共 `5^d` 后，右 gap没有任何隐藏的额外 `5`-depth。

---

## 7. floor-free Gaussian carrier inherits the full residue

`spontaneous-crt-gaussian-floorfree-carrier.md` 定义

\[
\mathscr P_\Delta
=2^{A_G}\Delta_+
-5^{B_G}k_h^3(D^2-C^2),
\]

其中

\[
A_G=\frac{M+5\eta}{2}+8,
\qquad
B_G=3M-d-\eta-3.
\]

在 current low-`m` reflection cone，`m<=6M/11`，故

\[
B_G-\lambda
=4M-3m-3
>0.
\tag{7.1}
\]

所以

\[
5^\lambda\mid5^{B_G}k_h^3(D^2-C^2).
\]

由 (4.1)：

\[
\boxed{
\mathscr P_\Delta
\equiv
2^{A_G}c_u^2a_3[D(20-4K)-2C]
\pmod{5^\lambda}.}
\tag{7.2}
\]

等价地

\[
\boxed{
\mathscr P_\Delta
\equiv
2^{A_G+1}c_u^2a_3(4D+C-2qW_q)
\pmod{5^\lambda}.}
\tag{7.3}
\]

模 `5` 使用 (6.1)：

\[
\boxed{
\mathscr P_\Delta
\equiv
-2^{A_G+1}c_u^2a_3C
\not\equiv0\pmod5.}
\tag{7.4}
\]

所以

\[
\boxed{v_5(\mathscr P_\Delta)=0.}
\tag{7.5}
\]

现在 `P_Delta` 同时具有：

1. `sgn(P_Delta)=-epsilon`；
2. `P_Delta` 为 odd integer；
3. `P_Delta` 为 `5`-adic unit；
4. 模 `5^lambda` 的显式 residue (7.2)/(7.3)。

---

## 8. current interface

Hensel scalar `r_E` 的中心模数为

\[
n_5=5^{\lambda-d},
\]
而 (7.2) 已覆盖更深的 `5^lambda`。因此 `P_Delta` 与 centered Hensel kernel现在确实处在同一 `5`-adic tower，而非仅共享 endpoint parameters。

下一步可把

\[
gr_E\equiv c_+c_u\pmod{5^{\lambda-d}}
\]
代入 (7.2)，尝试把 `c_u^2` 换成 centered Hensel unit `r_E^2`；随后再与 `P_Delta z_E chi_E<0` 的符号律联立。若 natural representative被该 residue固定到错误符号，即可排除对应 Gaussian side。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-gaussian-floorfree-carrier"></a>

> 整合来源：`spontaneous-crt-gaussian-floorfree-carrier.md`

# A2 CRT/Gaussian orientation 的 floor-free integer carrier

> **依赖：** `spontaneous-crt-gaussian-slot-orientation.md`、`endpoint-lattice.md` §§16.33–16.38。
>
> **严格状态：**前一文件用 `Q_Delta=floor(Delta_+/(D^2-C^2))` 构造 normalized orientation reader。本文直接在未取 floor 的 real quotient上乘回全部 lattice scale与 CRT modulus，得到 ordinary integer `P_Delta=2^{A_G}Delta_+-5^{B_G}k_h^3(D^2-C^2)`。其符号与 Gaussian high-factor side完全等价，并且距离零有固定相对 margin。因此 Gaussian side已经可由 additive exact gap `Delta_+` 本身读取，不依赖 Euclidean quotient的取整误差。本文不单独关闭 A2。

---

## 1. lattice exponents

定义

\[
\boxed{
A_G:=\frac{M+5\eta}{2}+8,
\qquad
B_G:=3M-d-\eta-3.}
\tag{1.1}
\]

在 reflection high-2 lattice 中二者均为正整数。

前一文件已证明，对 real CRT quotient

\[
Y_\Delta:=\frac{\Delta_+}{D^2-C^2}
\]
有

\[
\boxed{
\mathcal Y_{\Delta,G}
:=\frac{2^{A_G}}{5^{B_G}k_h^3}Y_\Delta
=
\frac{1000s^2x^2}{\sigma_\varepsilon^3}\Psi_\Delta.}
\tag{1.2}
\]

这里所有量均为正，且

\[
\frac1{17}<\Psi_\Delta<\frac{1001}{15000}.
\]

---

## 2. define the floor-free integer

定义

\[
\boxed{
\mathscr P_\Delta
:=
2^{A_G}\Delta_+
-5^{B_G}k_h^3(D^2-C^2).}
\tag{2.1}
\]

`Delta_+,D,C,k_h` 均为整数，所以 `P_Delta` 是 ordinary integer。

直接除以正整数

\[
5^{B_G}k_h^3(D^2-C^2)
\]
得到 exact identity

\[
\boxed{
\frac{\mathscr P_\Delta}
{5^{B_G}k_h^3(D^2-C^2)}
=
\mathcal Y_{\Delta,G}-1.}
\tag{2.2}
\]

因此其符号完全由未取 floor 的 Gaussian-normalized CRT quotient决定。

---

## 3. minus side is uniformly positive

前一文件的 raw bound给

\[
\frac{44}{25}
<\mathcal Y_{\Delta,G}
<\frac{12}{5}
\qquad(\varepsilon=-1).
\]

由 (2.2)：

\[
\boxed{
\frac{19}{25}
<
\frac{\mathscr P_\Delta}
{5^{B_G}k_h^3(D^2-C^2)}
<\frac75.}
\tag{3.1}
\]

特别地

\[
\boxed{
\varepsilon=-1
\Longrightarrow
\mathscr P_\Delta>0.}
\tag{3.2}
\]

---

## 4. plus side is uniformly negative

同理，plus side有

\[
\frac{51}{100}
<\mathcal Y_{\Delta,G}
<\frac7{10}
\qquad(\varepsilon=+1).
\]

所以

\[
\boxed{
-\frac{49}{100}
<
\frac{\mathscr P_\Delta}
{5^{B_G}k_h^3(D^2-C^2)}
<-\frac3{10}.}
\tag{4.1}
\]

特别地

\[
\boxed{
\varepsilon=+1
\Longrightarrow
\mathscr P_\Delta<0.}
\tag{4.2}
\]

两侧距离零都有绝对常数 margin；这里完全没有 floor correction。

---

## 5. exact orientation equivalence

high factor只有 `epsilon=±1` 两侧，所以 §§3–4 合并为

\[
\boxed{
\operatorname{sgn}(\mathscr P_\Delta)=-\varepsilon.}
\tag{5.1}
\]

即

\[
\boxed{
\varepsilon=-1
\iff\mathscr P_\Delta>0,
\qquad
\varepsilon=+1
\iff\mathscr P_\Delta<0.}
\tag{5.2}
\]

因此

\[
\boxed{\mathscr P_\Delta\ne0.}
\tag{5.3}
\]

由于 `D` 为偶数、`C` 为奇数，`D^2-C^2` 为奇数；`k_h` 也为奇数，而 `A_G>=1`。所以 (2.1) 的第一项为偶数、第二项为奇数：

\[
\boxed{\mathscr P_\Delta\equiv1\pmod2.}
\tag{5.4}
\]

这是一个 nonzero odd signed integer carrier。

---

## 6. relation to the quotient carrier

令 Euclidean remainder

\[
R_\Delta
:=\Delta_+-Q_\Delta(D^2-C^2),
\qquad
0\le R_\Delta<D^2-C^2.
\tag{6.1}
\]

前一文件定义

\[
\mathscr O_\Delta
:=2^{A_G}Q_\Delta-5^{B_G}k_h^3.
\]

于是 exact 有

\[
\boxed{
\mathscr P_\Delta
=(D^2-C^2)\mathscr O_\Delta
+2^{A_G}R_\Delta.}
\tag{6.2}
\]

所以 `P_Delta` 是 quotient sign carrier的 floor-free parent。真正的 additive data位于 `P_Delta`：它直接使用 exact gap `Delta_+`，而不是先做 Euclidean division。

---

## 7. interface with the centered Hensel sign

`spontaneous-crt-hensel-sign-bridge.md` 使用

\[
\operatorname{sgn}(\chi_E)
=\operatorname{sgn}(\varepsilon z_E),
\qquad z_E\ne0.
\]

由 (5.1) 可直接把 `O_Delta` 替换为更自然的 `P_Delta`：

\[
\boxed{
\mathscr P_\Delta\,z_E\,\chi_E<0.}
\tag{7.1}
\]

因此 CRT exact gap、Gaussian side和 centered Hensel kernel现在共享一个完全 floor-free 的 signed integer interface。

后续若 additive CRT residue / natural representative能独立推出 `P_Delta z_E chi_E>0`，即直接形成矛盾。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-gaussian-slot-orientation"></a>

> 整合来源：`spontaneous-crt-gaussian-slot-orientation.md`

# A2 additive CRT quotient 的 Gaussian-slot orientation reader

> **依赖：** `spontaneous-crt-quotient-endpoint-parameterization.md`、`spontaneous-crt-quotient-source-scale.md`、`endpoint-lattice.md` §§13–16。
>
> **严格状态：**此前已把 `Q_Delta` 的绝对无界尺度正规化到 endpoint lattice 参数 `(M,eta,d,c_Q)`。本文进一步使用 high-2 Gaussian factor 的 exact slot equality 消去 `c_Q,w`，得到一个真正与 Gaussian side 同尺度的 normalized CRT quotient `Q_{Delta,G}`。在 reflection high-2 lattice 中，minus/high factor 与 plus/high factor 分别强迫 `Q_{Delta,G}` 落入两个严格不交的固定实区间；因此 `Q_Delta` 本身已经成为 Gaussian side 的 orientation reader。进一步把阈值 `Q_{Delta,G}=1` 乘回整数平面，得到奇整数 sign carrier `O_Delta=2^{A_G}Q_Delta-5^{B_G}k_h^3`，其符号与 Gaussian side完全等价。本文没有把该 sign carrier 与 additive CRT residue / source Hensel phase联立到矛盾，因此不关闭 A2。

---

## 1. notation

沿用 dangerous reflection core：

\[
N=10^M,\qquad T=10^m,\qquad \eta=2m-M,
\]

\[
x=\frac{b_2}{N},\qquad s=\frac K N,\qquad w=\frac{b_3}{T},
\]

以及

\[
\frac1{10}<x<\frac2{19},\qquad
\frac{2499}{250}<s<10.
\tag{1.1}
\]

令

\[
\delta:=\frac CD,\qquad 0<\delta<\frac3{250}.
\tag{1.2}
\]

`spontaneous-crt-quotient-source-scale.md` 已证明

\[
\frac{\Delta_+}{D^2-C^2}
=
\mathfrak a_\Delta\,\Psi_\Delta,
\tag{1.3}
\]

其中

\[
\mathfrak a_\Delta
=\frac{c_u^25^\lambda}{g}K^2,
\tag{1.4}
\]

\[
\Psi_\Delta
:=
\frac{\mathscr S_+}{TK^2}
\frac1{1-\delta^2}.
\tag{1.5}
\]

已有严格窗

\[
\boxed{
\frac1{17}<\Psi_\Delta
<\frac{1001}{15000}.}
\tag{1.6}
\]

这里上界使用 `S_+/(TK^2)<1/15` 与 `1/(1-delta^2)<1001/1000`。

---

## 2. exact Gaussian high-factor coordinate

令 high factor 的真实 normalized coordinate 为

\[
\boxed{
\sigma_\varepsilon
:=\frac{H_0+\varepsilon Y_2}{gT},
\qquad \varepsilon\in\{-1,+1\}.}
\tag{2.1}
\]

其中 `epsilon` 表示 high-2 factor 实际落在 `H_0-Y_2` 或 `H_0+Y_2`。

由 `endpoint-lattice.md` §13 的 exact high-factor equality

\[
H_0+\varepsilon Y_2=\frac{g^2k_h}{2},
\]
得到

\[
\boxed{
\frac gT=\frac{2\sigma_\varepsilon}{k_h}.}
\tag{2.2}
\]

endpoint short windows给

\[
\boxed{
\frac{393}{125}<\sigma_-<\frac{1607}{500},}
\tag{2.3-}
\]

\[
\boxed{
\frac{2389}{500}<\sigma_+<\frac{606}{125}.}
\tag{2.3+}
\]

这两段本身已经不交。

---

## 3. eliminate `c_Q,w` from the CRT main scale

前一文件给

\[
\mathfrak a_\Delta
=
\frac{s^2w^3}{4xc_Q^3}
2^{(\eta-M)/2}5^{3M+2\eta-4d}.
\tag{3.1}
\]

另一方面 Gaussian slot equality `endpoint-lattice.md` (16.2) 可写为

\[
\boxed{c_Qk_h
=2^{\eta+2}5^{\eta+1-d}
\frac{\sigma_\varepsilon w}{u},}
\tag{3.2}
\]

其中

\[
u:=1+\frac{H}{5^{M-1}}.
\]

但由真实第二 denominator defect

\[
b_2=10^{M-1}+2^{M-1}H
\]
可精确得到

\[
\boxed{u=10x.}
\tag{3.3}
\]

把 (3.2),(3.3) 代入 (3.1)，`c_Q,w` 完全消失：

\[
\boxed{
\mathfrak a_\Delta
=
\frac{1000s^2x^2k_h^3}{\sigma_\varepsilon^3}
2^{-(M+5\eta)/2-8}
5^{3M-d-\eta-3}.}
\tag{3.4}
\]

所以 Gaussian slot并不是 `Q_Delta` 外部的另一套尺度；它正好把 CRT main scale正规化成一个固定连续系数。

---

## 4. Gaussian-normalized CRT quotient

定义

\[
\boxed{
\mathcal Q_{\Delta,G}
:=
\frac{2^{(M+5\eta)/2+8}}
{5^{3M-d-\eta-3}k_h^3}
Q_\Delta.}
\tag{4.1}
\]

因为 `eta=2m-M`，`M+eta` 同偶奇，所以 `(M+5eta)/2` 为整数。

先忽略 floor，定义 real quotient

\[
Y_\Delta:=\frac{\Delta_+}{D^2-C^2}.
\]

由 (1.3),(3.4)：

\[
\boxed{
\frac{2^{(M+5\eta)/2+8}}
{5^{3M-d-\eta-3}k_h^3}
Y_\Delta
=
\frac{1000s^2x^2}{\sigma_\varepsilon^3}
\Psi_\Delta.}
\tag{4.2}
\]

因此所有 `(M,eta,d,c_Q,k_h)` 的绝对指数尺度都已经从右边消失；只剩 endpoint box 与 Gaussian side。

---

## 5. floor correction is uniformly tiny

记

\[
\epsilon_{\rm fl}
:=
\frac{2^{(M+5\eta)/2+8}}
{5^{3M-d-\eta-3}k_h^3}.
\tag{5.1}
\]

当前 reflection high-2 lattice位于 low-`m` cone，已有

\[
M\ge11,
\qquad
\eta\le\frac M{11},
\qquad
d<\frac{9M}{77},
\qquad k_h\ge1.
\tag{5.2}
\]

于是

\[
\frac{M+5\eta}{2}+8<M+8,
\]

并且

\[
3M-d-\eta-3>2M.
\]

因此

\[
0<\epsilon_{\rm fl}
<256\left(\frac2{25}\right)^M
<\frac1{100}
\qquad(M\ge11).
\tag{5.3}
\]

又 `Q_Delta=floor(Y_Delta)`，故

\[
\boxed{
\frac{1000s^2x^2}{\sigma_\varepsilon^3}\Psi_\Delta
-\frac1{100}
<\mathcal Q_{\Delta,G}
<
\frac{1000s^2x^2}{\sigma_\varepsilon^3}\Psi_\Delta.}
\tag{5.4}
\]

---

## 6. two Gaussian sides give disjoint fixed bands

### 6.1 minus side

使用 (1.1),(1.6),(2.3-)：

\[
\frac{1000s^2x^2}{\sigma_-^3}\Psi_\Delta
>
1000\left(\frac{2499}{250}\right)^2
\left(\frac1{10}\right)^2
\frac1{17}
\left(\frac{500}{1607}\right)^3
>\frac{44}{25}.
\]

上界为

\[
\frac{1000s^2x^2}{\sigma_-^3}\Psi_\Delta
<
1000(10)^2\left(\frac2{19}\right)^2
\frac{1001}{15000}
\left(\frac{125}{393}\right)^3
<\frac{12}{5}.
\]

结合 floor correction `<1/100`：

\[
\boxed{
\frac74
<\mathcal Q_{\Delta,G}
<\frac{12}{5}
\qquad(\varepsilon=-1).}
\tag{6.1}
\]

### 6.2 plus side

同理，由 (2.3+)：

\[
\frac{1000s^2x^2}{\sigma_+^3}\Psi_\Delta
>
1000\left(\frac{2499}{250}\right)^2
\left(\frac1{10}\right)^2
\frac1{17}
\left(\frac{125}{606}\right)^3
>\frac{51}{100},
\]

而

\[
\frac{1000s^2x^2}{\sigma_+^3}\Psi_\Delta
<
1000(10)^2\left(\frac2{19}\right)^2
\frac{1001}{15000}
\left(\frac{500}{2389}\right)^3
<\frac7{10}.
\]

所以

\[
\boxed{
\frac12
<\mathcal Q_{\Delta,G}
<\frac7{10}
\qquad(\varepsilon=+1).}
\tag{6.2}
\]

两个区间严格不交，并且被 `1` 完全分开。

---

## 7. CRT quotient canonically reads the Gaussian side

由 (6.1),(6.2)：

\[
\boxed{
\varepsilon=-1
\iff
\mathcal Q_{\Delta,G}>1,}
\tag{7.1-}
\]

\[
\boxed{
\varepsilon=+1
\iff
\mathcal Q_{\Delta,G}<1.}
\tag{7.1+}
\]

所以 additive CRT quotient 与 Gaussian allocation 不再只是“共享同一 `(eta,d,c_Q)` 参数”：`Q_Delta` 经过 canonical lattice normalization 后直接恢复 Gaussian side orientation。

---

## 8. integer sign carrier

令

\[
\boxed{
A_G:=\frac{M+5\eta}{2}+8,
\qquad
B_G:=3M-d-\eta-3.}
\tag{8.1}
\]

当前 lattice 中二者均为整数，且 `A_G>=1,B_G>=1`。定义纯整数

\[
\boxed{
\mathscr O_\Delta
:=2^{A_G}Q_\Delta-5^{B_G}k_h^3.}
\tag{8.2}
\]

由 (4.1)：

\[
\frac{\mathscr O_\Delta}{5^{B_G}k_h^3}
=\mathcal Q_{\Delta,G}-1.
\tag{8.3}
\]

因此 (7.1±) 等价于

\[
\boxed{
\varepsilon=-1
\iff
\mathscr O_\Delta>0,}
\tag{8.4-}
\]

\[
\boxed{
\varepsilon=+1
\iff
\mathscr O_\Delta<0.}
\tag{8.4+}
\]

特别地

\[
\boxed{\mathscr O_\Delta\ne0.}
\tag{8.5}
\]

因为 `k_h` 为正奇数而 `A_G>=1`，第一项为偶数、第二项为奇数，所以

\[
\boxed{\mathscr O_\Delta\equiv1\pmod2.}
\tag{8.6}
\]

并有 exact residue

\[
\boxed{
\mathscr O_\Delta
\equiv-5^{B_G}k_h^3
\pmod{2^{A_G}},}
\tag{8.7}
\]

\[
\boxed{
\mathscr O_\Delta
\equiv2^{A_G}Q_\Delta
\pmod{5^{B_G}}.}
\tag{8.8}
\]

所以 Gaussian side 已经被转换为一个 ordinary odd integer 的**符号问题**，同时该整数带有显式深 `2/5` residue。这比只保留实数 slot 更适合继续与 centered source-Hensel representatives `(z_E,chi_E)`、additive CRT residue以及 exact gap valuations联立。

---

## 9. revised frontier

粗 Gaussian slots此前在 `eta>=1` 确实有实区间交点，因此不能靠 `G=g/T` 本身统一排除。

本文给出的新对象

\[
\mathcal Q_{\Delta,G}
\]
把两侧分成

\[
\left(\frac12,\frac7{10}\right)
\quad\text{和}\quad
\left(\frac74,\frac{12}{5}\right),
\]
并进一步变成整数 carrier `O_Delta` 的正负号。

所以下一步最自然的是证明 additive CRT 的唯一 residue class、`v_2/v_5` exact gap phase，或 `(z_E,chi_E)` source-Hensel centered representative固定 `O_Delta` 的相反符号。如果能做到，就会直接排除对应 Gaussian side，而无需再做 coarse slot comparison。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-height-descent-overlap"></a>

> 整合来源：`spontaneous-crt-height-descent-overlap.md`

# A2 sphere-height / descendant common overlap 的 fixed-`67` orientation

> **依赖：** `primitive-reduction.md`、`spontaneous-height-equal-depth-target-selector.md`、`spontaneous-residual-parity-doubling.md`、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-target-descent-overlap.md`。
>
> **严格状态：**每个 non-3 inert divisor of `W_q` 已被锁到真实 height `H_0`。本文进一步要求该 prime进入 fully primitive descendant common gcd。`alpha,H_0` 同时消失后，descended quotient强迫固定 quadratic `G_D=11K^2-240K+432`；original carrier又强迫该 prime进入 `J_H`，因此回流到 canonical height gcd `D_H=gcd(B_W,W_q)`。消去 `K` 后得到 source quartic `H_67`，其 square completion只含 fixed discriminant `67`。generic height/descent common inert prime必须满足 `(67/r)=1`，而 ramified `r=67` 因要求一个非平方 `63` 成为 `(z/c_u)^2` 被严格排除。若再与 source-common sheet相交，resultant只剩 fixed `139,463`。本文仍允许满足 fixed-67 orientation的 moving height primes，因此不关闭 A2。

---

## 1. height prime entering descendant common support

固定 odd prime

\[
r\ne3,
\qquad
r\equiv3\pmod4,
\qquad
r\mid W_q,
\]
并假设它还进入 descendant common gcd

\[
G_\Delta
=
\gcd(\mathscr R_{63}^\star,
     \widehat{\mathscr D}_{63}).
\]

已有 height theorem 给

\[
\boxed{
r\nmid c_Qc_ugXY,}
\tag{1.1}

\[
\boxed{
v_r(W_q)=v_r(H_0),}
\tag{1.2}

\[
\boxed{
\left(\frac{N_0}{r}\right)=-1.}
\tag{1.3}

因为

\[
\alpha=\omega W_q,
\qquad
H_0=c_uW_q,
\]
立刻有

\[
\boxed{r\mid\alpha,\qquad r\mid H_0.}
\tag{1.4}

---

## 2. descendant equation forces `G_D(K)=0`

fully primitive descended quotient满足 exact identity

\[
\boxed{
16\mathscr F_{63}
=3gT G_D(K)
-16(2K-9)(g\alpha+H_0),}
\tag{2.1}

其中

\[
\boxed{G_D(K)=11K^2-240K+432.}
\tag{2.2}

`Dhat_63=c_u^2 F_63`，且由 (1.1) `r∤3c_ugT`。使用 (1.4)：

\[
\boxed{r\mid\widehat{\mathscr D}_{63}
\Longrightarrow
G_D(K)\equiv0\pmod r.}
\tag{2.3}

所以 every height/descent common prime被送进同一固定 K-quadratic。

它的 discriminant为

\[
\boxed{
\operatorname{Disc}(G_D)
=38592
=24^2\cdot67.}
\tag{2.4}

---

## 3. original carrier sends the same prime back to the canonical height gcd

height-free additive identity为

\[
\boxed{
\widehat{\mathcal T}_2
=5^m\widehat{\mathcal J}_H
-2^{m+1}B_0^2(2K-9)\alpha,}
\tag{3.1}

其中 `B_0=c_ug`。

若 `r|G_Delta`，positive descent说明

\[
r\mid\widehat{\mathcal T}_2.
\]

再用 (1.4)，(3.1) 模 `r` 化为

\[
0\equiv5^m\widehat{\mathcal J}_H.
\]

所以

\[
\boxed{r\mid\widehat{\mathcal J}_H.}
\tag{3.2}

而已有 canonical height gcd identity

\[
\boxed{
D_H
:=\gcd(\widehat{\mathcal J}_H,W_q)
=\gcd(\mathscr B_W,W_q).}
\tag{3.3}

结合 `r|W_q`：

\[
\boxed{r\mid\mathscr B_W.}
\tag{3.4}

所以 height/descent common prime不是新的自由 source label；它自动落入既有 height gcd `D_H`。

---

## 4. eliminate `K`: the source quartic `H_67`

source companion为

\[
\boxed{
\mathscr B_W
=c_u^2(5K^2-36K+55)+z^2K^2.}
\tag{4.1}

由 (1.1)，`c_u` 为 r-unit。

先注意 `z` 也不能在 genuine inert common root上为零。若 `r|z`，(4.1) 与 (3.4) 会给

\[
5K^2-36K+55\equiv0.
\]

但

\[
\boxed{
\operatorname{Res}_K(
G_D,
5K^2-36K+55)
=527017
=17\cdot29\cdot1069,}
\tag{4.2}

三个 odd prime全部为 `1 mod4`。所以 inert r不可能来自 `z=0`。

因此可定义 r-unit

\[
v:=z/c_u.
\]

将 (4.1) 除以 `c_u^2`，与 `G_D=0` 对 K 消元：

\[
\boxed{
186624v^4+779040v^2+527017
\equiv0\pmod r.}
\tag{4.3}

乘回 `c_u^4`，定义 ordinary positive source carrier

\[
\boxed{
\mathscr H_{67}
:=186624z^4
+779040z^2c_u^2
+527017c_u^4.}
\tag{4.4}

于是

\[
\boxed{r\mid\mathscr H_{67}.}
\tag{4.5}

---

## 5. exact square completion and fixed-67 orientation

(4.4) 有精确 completion：

\[
\boxed{
9\mathscr H_{67}
=
(1296z^2+2705c_u^2)^2
-67(196c_u^2)^2.}
\tag{5.1}

验证只需展开；系数恒等式为

\[
2705^2-67\cdot196^2
=9\cdot527017.
\]

对 `r\ne67`，由 (4.5)、`r∤3c_u`：

\[
\left(
\frac{1296z^2+2705c_u^2}{196c_u^2}
\right)^2
\equiv67\pmod r.
\]

所以

\[
\boxed{
\left(\frac{67}{r}\right)=1.}
\tag{5.2}

由于

\[
67\equiv r\equiv3\pmod4,
\]
quadratic reciprocity给

\[
\boxed{
\left(\frac r{67}\right)=-1.}
\tag{5.3}

因此 every generic height/descent common inert prime都被固定到 mod-67 nonresidue orientation。

---

## 6. ramified prime `67` is impossible

若 `r=67`，(5.1) 与 `H_67=0` 给

\[
1296z^2+2705c_u^2\equiv0\pmod{67}.
\]

因 `c_u` 为 unit：

\[
\boxed{
(z/c_u)^2
\equiv-2705\cdot1296^{-1}
\equiv63\pmod{67}.}
\tag{6.1}

但直接 Euler criterion / quadratic-residue table给

\[
\boxed{
\left(\frac{63}{67}\right)=-1.}
\tag{6.2}

左边 `(z/c_u)^2` 必为平方，矛盾。因此

\[
\boxed{67\notin\operatorname{Supp}(G_\Delta)
\quad\text{through the height channel}.}
\tag{6.3}

所以 fixed discriminant prime本身没有 singular Hensel branch。

---

## 7. triple overlap with source-common is only fixed `139,463`

若同一 height/descent common prime还属于 source common gcd，已有 collision sheet

\[
18K-55\equiv0\pmod r.
\]

与 (2.2) resultant：

\[
\boxed{
\operatorname{Res}_K(G_D,18K-55)
=-64357
=-139\cdot463.}
\tag{7.1}

因此 genuine triple overlap满足

\[
\boxed{
r\in\{139,463\}.}
\tag{7.2}

两个 fixed primes都为 `3 mod4`；对应 K states唯一：

\[
\boxed{
K\equiv88\pmod{139},
\qquad
K\equiv286\pmod{463}.}
\tag{7.3}

所以 source-common与 height-common 两类 old source label若同时试图承担 descendant common parity，不存在 moving intersection。

---

## 8. revised height/common frontier

height/descent common support现在满足三层规范约束：

1. canonical gcd:
   \[
   r\mid D_H=\gcd(B_W,W_q);
   \]
2. fixed K quadratic:
   \[
   G_D(K)\equiv0;
   \]
3. source quartic / character:
   \[
   r\mid H_{67},
   \qquad
   (r/67)=-1,
   \qquad r\ne67.
   \]

若再进入 source-common pool，只剩 fixed `139,463`。

因此 descendant common parity的 remaining height source已经不再是任意 `W_q` prime；它必须同时通过 canonical height gcd和 fixed-67 orientation。尚缺的是排除满足这些条件的 moving height prime，或证明其 common exponent parity不能使 `G_Delta≡3 mod4`。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-height-primitive-remainder"></a>

> 整合来源：`spontaneous-crt-height-primitive-remainder.md`

# A2 height descent remainder 的 exact `5^{2d}` primitive reduction

> **依赖：** `spontaneous-crt-height-remainder-descent.md`、`spontaneous-crt-dual-gap-remainder.md`。
>
> **严格状态：**前一 descent theorem构造 positive primitive-2 remainder `Rhat_63`，并得到 `That_2=5^{nu_5}Rhat_63+gD_63`。本文继续审计 `Rhat_63` 的 5-adic content，证明其深度精确为 `2d`。除去该 content 后得到 fully `(2,5)`-primitive positive `3 mod4` carrier `Rstar_63`，且 `gcd(Rstar_63,10g)=1`。由于 `nu_5+2d=lambda`，descent 自动升级为 `That_2=5^lambda Rstar_63+gD_63`；小余数承担的是完整 reflection `5^lambda` depth，并仍小于原 carrier的 `1/24`。本文尚未把 `Rstar_63` 重新识别为原 decimal structural class，因此不宣称 infinite descent或 A2 closure。

---

## 1. exact formula for `J_Delta`

前一 theorem定义

\[
\mathscr J_\Delta
=
\frac{
D(2K-9)\widetilde\Gamma_\Delta
-\widetilde{\mathcal T}_2
}{5^{\lambda-d}}.
\tag{1.1}
\]

使用

\[
D=gL,
\qquad
L=2^m5^d,
\]

\[
\widetilde\Gamma_\Delta
=c_u^2\{g((2K-12)T-2a_3)+5^\lambda C\},
\]

以及

\[
\widetilde{\mathcal T}_2
=Lc_u^2g^2
[TK^2-(18T+4a_3)K+18a_3+55T]
-5^{\lambda+2d}Q_0^2N_0,
\]
直接展开 numerator。

其中不含 `C` 的两个大 bracket发生精确消元：

\[
\boxed{
(2K-9)((2K-12)T-2a_3)
-
[TK^2-(18T+4a_3)K+18a_3+55T]
=T(3K^2-24K+53).}
\tag{1.2}
\]

因此除去 `5^{lambda-d}` 后得到 exact positive formula

\[
\boxed{
\begin{aligned}
\mathscr J_\Delta
=5^{2d}\Bigl[
&2^{2m}5^dc_u^2g^2(3K^2-24K+53)\\
&+2^mgc_u^2C(2K-9)\\
&+5^dQ_0^2N_0
\Bigr].
\end{aligned}}
\tag{1.3}
\]

---

## 2. exact `5`-depth of `J_Delta`

定义中括号为 `J_0`。当前

\[
5\nmid g c_u C Q_0N_0,
\qquad
K=10P,
\]
所以

\[
2K-9\equiv-9\equiv1\pmod5.
\]

(1.3) 中第一、第三项都含显式 `5^d`，而第二项为 unit。因此

\[
\boxed{
\mathscr J_0
\equiv2^mgc_u^2C
\not\equiv0\pmod5.}
\tag{2.1}
\]

故

\[
\boxed{v_5(\mathscr J_\Delta)=2d.}
\tag{2.2}
\]

---

## 3. `U_63` is much deeper at `5`

前一 theorem写

\[
\widehat{\mathscr R}_{63}
=U_{63}-\mathscr J_\Delta,
\]

\[
U_{63}
:=\frac{63c_u^2D^2LK^2}{2^{m+4}}.
\]

因为

\[
v_5(D)=d,
\qquad
v_5(L)=d,
\qquad
v_5(K)=1,
\]
有

\[
\boxed{v_5(U_{63})=3d+2.}
\tag{3.1}
\]

而 `d>=1`：

\[
3d+2>2d.
\]

由 (2.2)，两项 5-depth不同，所以不存在首层 cancellation：

\[
\boxed{v_5(\widehat{\mathscr R}_{63})=2d.}
\tag{3.2}
\]

---

## 4. fully primitive short remainder

定义

\[
\boxed{
\mathscr R_{63}^\star
:=
\frac{\widehat{\mathscr R}_{63}}{5^{2d}}.}
\tag{4.1}
\]

前一 theorem已有

\[
\widehat{\mathscr R}_{63}>0,
\qquad
\widehat{\mathscr R}_{63}\equiv3\pmod4,
\qquad
\gcd(\widehat{\mathscr R}_{63},g)=1.
\]

由于 `5^{2d}≡1 mod4`，结合 (3.2)：

\[
\boxed{
\mathscr R_{63}^\star>0,
\qquad
\mathscr R_{63}^\star\equiv3\pmod4,}
\tag{4.2}
\]

\[
\boxed{
\gcd(\mathscr R_{63}^\star,10g)=1.}
\tag{4.3}
\]

所以 `Rstar_63` 是真正的 fully `(2,5)`-primitive external odd-inert carrier。

模 `5` 还能从 (2.1) 读取：由于 `U_63/5^{2d}` 仍被 `5` 整除，

\[
\boxed{
\mathscr R_{63}^\star
\equiv
-2^mgc_u^2C
\pmod5.}
\tag{4.4}
\]

---

## 5. denominator residue after primitive reduction

前一 theorem有

\[
\widehat{\mathscr R}_{63}
\equiv-c_u^25^dC^2
\pmod g.
\]

代入 `Rhat=5^{2d}Rstar`，并消去一个 `5^d`：

\[
\boxed{
5^d\mathscr R_{63}^\star
\equiv-c_u^2C^2
\pmod g.}
\tag{5.1}
\]

因此

\[
\boxed{
5^\lambda\mathscr R_{63}^\star
\equiv
-c_u^25^{\lambda-d}C^2
\equiv
\widehat{\mathcal T}_2
\pmod g.}
\tag{5.2}
\]

---

## 6. descent upgrades from `5^{nu_5}` to full `5^lambda`

前一 theorem定义

\[
\mathscr D_{63}
=
\frac{
\widehat{\mathcal T}_2
-5^{\nu_5}\widehat{\mathscr R}_{63}
}{g}.
\]

因为

\[
\widehat{\mathscr R}_{63}=5^{2d}\mathscr R_{63}^\star,
\qquad
\nu_5+2d=\lambda,
\]
得到真正的 fully primitive descent：

\[
\boxed{
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g\mathscr D_{63}.}
\tag{6.1}
\]

三因子满足

\[
\widehat{\mathcal T}_2>0,
\qquad
\mathscr R_{63}^\star>0,
\qquad
\mathscr D_{63}>0.
\]

---

## 7. the full-`5^lambda` remainder is still under `1/24`

此前已有

\[
0<5^{\nu_5}\widehat{\mathscr R}_{63}
<\frac1{24}\widehat{\mathcal T}_2.
\]

左边正是

\[
5^{\nu_5+2d}\mathscr R_{63}^\star
=5^\lambda\mathscr R_{63}^\star.
\]

因此

\[
\boxed{
0<5^\lambda\mathscr R_{63}^\star
<\frac1{24}\widehat{\mathcal T}_2.}
\tag{7.1}
\]

等价地

\[
\boxed{
0<\mathscr R_{63}^\star
<\frac{
\widehat{\mathcal T}_2
}{24\cdot5^\lambda}.}
\tag{7.2}
\]

这是相对于 original forced inert carrier 的 full reflection-depth height drop。

---

## 8. nested support identity in fully primitive form

由 (4.3) 与 (6.1)：

\[
\begin{aligned}
\gcd(\widehat{\mathcal T}_2,\mathscr R_{63}^\star)
&=\gcd(g\mathscr D_{63},\mathscr R_{63}^\star)\\
&=\boxed{
\gcd(\mathscr D_{63},\mathscr R_{63}^\star).}
\end{aligned}
\tag{8.1}
\]

所以 original carrier 与 fully primitive short remainder若共享 odd prime，该 prime必须继续进入 descended quotient `D_63`。

而

\[
\widehat{\mathcal T}_2\equiv3\pmod4,
\qquad
\mathscr R_{63}^\star\equiv3\pmod4.
\]

因此 global parity要想用同一 inert prime复用两份 `3 mod4` orientation，必须支付一个三重 overlap：

\[
\boxed{
p\mid
\widehat{\mathcal T}_2,
\quad
p\mid\mathscr R_{63}^\star,
\quad
p\mid\mathscr D_{63}.}
\tag{8.2}
\]

---

## 9. current role

原 A2 核现在存在一个相当强的 strict descent package：

\[
\boxed{
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star+g\mathscr D_{63},}
\]

其中

- `Rstar_63` 是 positive、fully `(2,5)`-primitive、`3 mod4`；
- `gcd(Rstar_63,g)=1`；
- scaled remainder `<That_2/24`；
- any parity reuse with original forces entry into positive quotient `D_63`.

这已经比普通“存在另一个 inert carrier”强很多，但还不能称为 infinite descent：`Rstar_63` 尚未证明具有原 `That_2` 的 rational-root/cofactor origin，`D_63` 也尚未回到同一 coefficient plane。

下一步应优先研究 `gcd(Rstar_63,D_63)` 的 explicit gate，或证明 `Rstar_63` 的 inert prime无法属于原三类 prime-source中的任一 already-paid support。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-height-remainder-descent"></a>

> 整合来源：`spontaneous-crt-height-remainder-descent.md`

# A2 forced inert carrier 经 `R_63` 的 positive height descent

> **依赖：** `spontaneous-crt-dual-gap-remainder.md`、`endpoint-lattice.md` §§16.37–16.39。
>
> **严格状态：**前一文件从 dual-gap full-`5^lambda` synchronization构造 positive primitive `3 mod4` remainder `Rhat_63`。本文证明它不是与原核心 carrier `That_2` 平行的新对象：二者在完整 denominator modulus `g` 上满足 `That_2≡5^{nu_5}Rhat_63 mod g`。因此可定义 positive descended quotient `D_63=(That_2-5^{nu_5}Rhat_63)/g`。更强地，`5^{nu_5}Rhat_63` 小于原 `That_2` 的 `1/24`，而 `D_63` 有显式 positive quadratic form与窄 `(31/500,1/16)` normalized window。原 carrier与短 remainder若复用 prime，该 prime必须继续进入 `D_63`。这构成 nested support/height descent，但尚未证明可无限迭代回同一 decimal class，因此不关闭 A2。

---

## 1. notation

沿用

\[
\nu_5:=\lambda-2d>0,
\qquad
n_5:=5^{\lambda-d}=5^{\nu_5+d},
\]

\[
L=2^m5^d,
\qquad
D=gL,
\]

以及 additive lift

\[
\boxed{
\widetilde{\mathcal T}_2
-(D-C)\widetilde\Gamma_\Delta
=g\Delta_+.}
\tag{1.1}
\]

这里

\[
\widetilde{\mathcal T}_2=5^d\widehat{\mathcal T}_2,
\tag{1.2}
\]

\[
\widetilde\Gamma_\Delta
=c_u^2\{g((2K-9)T-a_3)-H_0\}.
\tag{1.3}
\]

定义 bracket

\[
\boxed{
B_\Delta
:=g((2K-9)T-a_3)-H_0.}
\tag{1.4}
\]

所以 `Gammatilde_Delta=c_u^2 B_Delta`。

---

## 2. cross determinant is itself an additive lift quotient

前一文件定义

\[
\mathscr E_\Delta
=\Gamma_\Delta B_s-2D\Delta_+,
\]

其中

\[
\Gamma_\Delta=2L\widetilde\Gamma_\Delta,
\qquad
B_s=2D(K-5)+C.
\]

由 (1.1)：

\[
2D\Delta_+
=2L\{
\widetilde{\mathcal T}_2-(D-C)\widetilde\Gamma_\Delta
\}.
\]

所以

\[
\begin{aligned}
\mathscr E_\Delta
&=2L\left[
\widetilde\Gamma_\Delta(B_s+D-C)
-\widetilde{\mathcal T}_2
\right]\\
&=2L\left[
D(2K-9)\widetilde\Gamma_\Delta
-\widetilde{\mathcal T}_2
\right].
\end{aligned}
\]

因此

\[
\boxed{
\mathscr E_\Delta
=2L\left[
D(2K-9)\widetilde\Gamma_\Delta
-\widetilde{\mathcal T}_2
\right].}
\tag{2.1}
\]

前一文件证明 `5^lambda|E_Delta`。因为

\[
\frac{2L}{5^\lambda}
=\frac{2^{m+1}}{n_5},
\]
得到

\[
\boxed{
\widehat{\mathscr E}_\Delta
=2^{m+1}\mathscr J_\Delta,}
\tag{2.2}
\]

其中 ordinary integer

\[
\boxed{
\mathscr J_\Delta
:=
\frac{
D(2K-9)\widetilde\Gamma_\Delta
-\widetilde{\mathcal T}_2
}{n_5}.}
\tag{2.3}
\]

这直接解释 `v_2(Ehat_Delta)=m+1`。

---

## 3. `J_Delta` has a pure square residue modulo `g`

先由 (1.1)：

\[
\widetilde{\mathcal T}_2
\equiv(D-C)\widetilde\Gamma_\Delta
\equiv-C\widetilde\Gamma_\Delta
\pmod g.
\tag{3.1}
\]

另一方面

\[
B_\Delta=g((2K-9)T-a_3)-H_0
\equiv-H_0\pmod g.
\]

source identity

\[
H_0=g(3T+a_3)-5^\lambda C
\]
给

\[
B_\Delta\equiv5^\lambda C\pmod g.
\]

因此

\[
\boxed{
\widetilde\Gamma_\Delta
\equiv c_u^25^\lambda C
\pmod g,}
\tag{3.2}
\]

\[
\boxed{
\widetilde{\mathcal T}_2
\equiv-c_u^25^\lambda C^2
\pmod g.}
\tag{3.3}
\]

在 (2.3) 中第一项含 `D`，故模 `g` 消失：

\[
n_5\mathscr J_\Delta
\equiv c_u^25^\lambda C^2
\pmod g.
\]

`5` 与 `g` 互素，所以消去 `n_5=5^{lambda-d}`：

\[
\boxed{
\mathscr J_\Delta
\equiv c_u^25^dC^2
\pmod g.}
\tag{3.4}
\]

---

## 4. short remainder modulo `g`

前一文件定义

\[
\widehat{\mathscr R}_{63}
:=\frac{
63\mathscr B_\Delta-8\widehat{\mathscr E}_\Delta
}{2^{m+4}},
\]

其中

\[
\mathscr B_\Delta=c_u^2D^2LK^2.
\]

由 (2.2)：

\[
\boxed{
\widehat{\mathscr R}_{63}
=
\frac{63\mathscr B_\Delta}{2^{m+4}}
-\mathscr J_\Delta.}
\tag{4.1}
\]

第一项为整数，并且含完整 factor `g`：确实

\[
\frac{\mathscr B_\Delta}{2^{m+4}g}
=
\frac{c_u^2gL^3K^2}{2^{m+4}}
\in\mathbf Z.
\]

因此由 (3.4)：

\[
\boxed{
\widehat{\mathscr R}_{63}
\equiv-c_u^25^dC^2
\pmod g.}
\tag{4.2}
\]

已有

\[
\gcd(c_uC,5g)=1.
\]

所以立即得到

\[
\boxed{
\gcd(\widehat{\mathscr R}_{63},g)=1.}
\tag{4.3}
\]

新 short `3 mod4` parity因此完全位于 denominator `g` support之外。

---

## 5. original carrier has the matching deeper residue

由 (1.2),(3.3)：

\[
5^d\widehat{\mathcal T}_2
\equiv-c_u^25^\lambda C^2
\pmod g.
\]

消去 `5^d`：

\[
\boxed{
\widehat{\mathcal T}_2
\equiv
-c_u^25^{\lambda-d}C^2
\pmod g.}
\tag{5.1}
\]

而

\[
\nu_5=\lambda-2d.
\]

把 (4.2) 乘 `5^{nu_5}`：

\[
5^{\nu_5}\widehat{\mathscr R}_{63}
\equiv
-c_u^25^{\lambda-d}C^2
\pmod g.
\]

所以

\[
\boxed{
\widehat{\mathcal T}_2
\equiv
5^{\nu_5}\widehat{\mathscr R}_{63}
\pmod g.}
\tag{5.2}
\]

这是 original forced inert carrier 与 short remainder之间的 exact denominator bridge。

---

## 6. define the descended positive quotient

由 (5.2) 定义 integer

\[
\boxed{
\mathscr D_{63}
:=
\frac{
\widehat{\mathcal T}_2
-5^{\nu_5}\widehat{\mathscr R}_{63}
}{g}.}
\tag{6.1}
\]

下面证明它严格为正，并给出 natural form。

---

## 7. exact closed form for `D_63`

由 (4.1)：

\[
\widehat{\mathscr R}_{63}=U_{63}-\mathscr J_\Delta,
\qquad
U_{63}:=\frac{63\mathscr B_\Delta}{2^{m+4}}.
\]

而 (2.3) 与 `n_5=5^{nu_5+d}` 给

\[
5^{\nu_5}\mathscr J_\Delta
=
\frac{D(2K-9)\widetilde\Gamma_\Delta}{5^d}
-\widehat{\mathcal T}_2.
\]

代入 (6.1) 后 `That_2` 完全消去：

\[
\widehat{\mathcal T}_2
-5^{\nu_5}\widehat{\mathscr R}_{63}
=
\frac{D(2K-9)\widetilde\Gamma_\Delta}{5^d}
-5^{\nu_5}U_{63}.
\]

利用

\[
D/5^d=g2^m,
\qquad
\widetilde\Gamma_\Delta=c_u^2B_\Delta,
\]
以及直接整理 `U_63` 的 powers，得到

\[
\boxed{
\mathscr D_{63}
=2^mc_u^2\mathscr F_{63},}
\tag{7.1}
\]

其中

\[
\boxed{
\mathscr F_{63}
:=(2K-9)B_\Delta
-\frac{63}{16}gTK^2.}
\tag{7.2}
\]

`gTK^2/16` 为整数，因为

\[
v_2(gTK^2)\ge(t-1)+m+2\ge9.
\]

---

## 8. `F_63` is positive and almost exactly `1/16` of the parent scale

写

\[
\delta=C/D,
\qquad
\zeta=a_3/T.
\]

有 exact

\[
\frac{B_\Delta}{gT}
=2K-12-2\zeta+\delta.
\]

因此

\[
\boxed{
\frac{\mathscr F_{63}}{gTK^2}
=
\frac1{16}
-rac{2(21+2\zeta-\delta)}K
+rac{9(12+2\zeta-\delta)}{K^2}.}
\tag{8.1}
\]

当前

\[
1<\zeta<251/250,
\qquad0<\delta<3/250,
\qquad K>9\cdot10^{11}.
\]

所以 correction的绝对量远小于 `10^{-9}`，并且线性负项主导正的 `K^{-2}` 项。安全地得到

\[
\boxed{
\frac{31}{500}
<
\frac{\mathscr F_{63}}{gTK^2}
<
\frac1{16}.}
\tag{8.2}
\]

结合 (7.1)：

\[
\boxed{
\frac{31}{500}
<
\frac{\mathscr D_{63}}
{2^mc_u^2gTK^2}
<
\frac1{16}.}
\tag{8.3}
\]

特别地

\[
\boxed{\mathscr D_{63}>0.}
\tag{8.4}
\]

此外 `B_Delta` 为 odd，`2K-9` 为 odd，而 `63gTK^2/16` 被 `4` 整除，因此 `F_63` 为 odd：

\[
\boxed{v_2(\mathscr D_{63})=m.}
\tag{8.5}
\]

---

## 9. the original carrier itself has a narrow natural window

为了比较 remainder relative size，先把 `That_2` 的 natural scale写清楚。由 §3 的 exact formula：

\[
\widehat{\mathcal T}_2
=2^mc_u^2g^2
[TK^2-(18T+4a_3)K+18a_3+55T]
-5^mQ_0^2N_0.
\]

定义

\[
\boxed{
\mathscr S_T:=2^mc_u^2g^2TK^2.}
\tag{9.1}
\]

令

\[
y:=\frac{10a_2}{N},
\qquad s=9+y.
\]

第二项相对主尺度精确为

\[
\boxed{
R_T(x,y)
:=\frac{Q^2N_0}{B^2K^2}
=
\frac{(x+2)^2(2025x^2+y^2)}
{100x^2(9+y)^2}.}
\tag{9.2}
\]

直接求导：

\[
\partial_xR_T
=
\frac{(x+2)(2025x^3-2y^2)}
{50x^3(y+9)^2}>0,
\]

\[
\partial_yR_T
=
-\frac{9(x+2)^2(225x^2-y)}
{50x^2(y+9)^3}<0
\]
在 endpoint box成立。因此 extremum在 corners：

\[
\boxed{
\frac{7497}{8000}
<R_T
<\frac{234947716}{250493929}.}
\tag{9.3}
\]

结合 `K>9*10^11` 的 negligible linear correction，得到

\[
\boxed{
\frac{31}{500}
<
\frac{\widehat{\mathcal T}_2}{\mathscr S_T}
<
\frac{63}{1000}.}
\tag{9.4}
\]

这也重新给出 `That_2>0` 的定量版本。

---

## 10. the residue is less than `1/24` of the original carrier

前一 remainder theorem给

\[
\widehat{\mathscr R}_{63}
<
\frac{\mathscr B_\Delta}{25\cdot2^{m+4}}.
\]

而 powers exact 满足

\[
\boxed{
\frac{5^{\nu_5}\mathscr B_\Delta}{2^{m+4}}
=\frac{\mathscr S_T}{16}.}
\tag{10.1}
\]

所以

\[
5^{\nu_5}\widehat{\mathscr R}_{63}
<\frac{\mathscr S_T}{400}.
\tag{10.2}
\]

用 (9.4) 的 lower bound：

\[
\frac{
5^{\nu_5}\widehat{\mathscr R}_{63}
}{\widehat{\mathcal T}_2}
<
\frac{1/400}{31/500}
=\frac5{124}
<\frac1{24}.
\]

所以

\[
\boxed{
0<5^{\nu_5}\widehat{\mathscr R}_{63}
<\frac1{24}\widehat{\mathcal T}_2.}
\tag{10.3}
\]

结合 (6.1)：

\[
\boxed{
\widehat{\mathcal T}_2
=5^{\nu_5}\widehat{\mathscr R}_{63}
+g\mathscr D_{63},}
\tag{10.4}
\]

其中两项均严格为正。

这是一条真正的 positive height descent decomposition。

---

## 11. nested support identity

由 (4.3)：

\[
\gcd(\widehat{\mathscr R}_{63},g)=1.
\]

从 (10.4)：

\[
\begin{aligned}
\gcd(\widehat{\mathcal T}_2,\widehat{\mathscr R}_{63})
&=
\gcd(g\mathscr D_{63},\widehat{\mathscr R}_{63})\\
&=
\boxed{
\gcd(\mathscr D_{63},\widehat{\mathscr R}_{63}).}
\end{aligned}
\tag{11.1}
\]

所以 original carrier 与 short remainder若复用任意 odd prime，该 prime必须继续进入 descended quotient `D_63`。

特别地，两者都是 positive `3 mod4` integers：

\[
\widehat{\mathcal T}_2\equiv3\pmod4,
\qquad
\widehat{\mathscr R}_{63}\equiv3\pmod4.
\]

因此它们的 odd-inert parity若试图共享 support，shared parity不能停在第一层；必须同时进入

\[
\boxed{
\widehat{\mathcal T}_2,
\quad
\widehat{\mathscr R}_{63},
\quad
\mathscr D_{63}.}
\tag{11.2}
\]

这就是 nested support descent。

---

## 12. current frontier

现在 original A2 inert carrier已被写成

\[
\boxed{
\widehat{\mathcal T}_2
=\underbrace{5^{\nu_5}\widehat{\mathscr R}_{63}}_{<\widehat T_2/24}
+\underbrace{g\mathscr D_{63}}_{>0}.}
\]

其中：

- `Rhat_63` 比其 parent natural scale短至少 `25` 倍，且为 `3 mod4`；
- `Rhat_63` 与 `g` 完全互素；
- `D_63` 相对 original scale少一整份 factor `g`，并有显式 positive quadratic form；
- any common prime of original/remainder must also divide `D_63`.

还不能称为 infinite descent，因为 `D_63` 尚未证明重新满足原 decimal/cofactor structural class。下一步最值得攻击的是

\[
\gcd(\mathscr D_{63},\widehat{\mathscr R}_{63}),
\]

若能把它压到 fixed/denominator support，就会强迫 original carrier和 short remainder使用不同 inert primes，从而给 global A2 parity一个真实 multiplicative surcharge。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-hensel-sign-bridge"></a>

> 整合来源：`spontaneous-crt-hensel-sign-bridge.md`

# A2 CRT orientation carrier 与 centered Hensel 核的 signed bridge

> **依赖：** `spontaneous-crt-gaussian-slot-orientation.md`、`endpoint-lattice.md` §§16.23–16.30。
>
> **严格状态：**Gaussian high-factor side此前由外部符号 `epsilon=±1` 表示。前一文件证明该 side可由整数 `O_Delta=2^{A_G}Q_Delta-5^{B_G}k_h^3` 的符号完全恢复；`endpoint-lattice.md` 又已证明 mixed Hensel scalar `chi_E` 的符号等于 `epsilon z_E`，其中 `z_E` 是由真实 denominator defect `H mod g` 唯一确定的 centered odd representative。本文合并二者，得到纯整数三重符号律 `O_Delta z_E chi_E<0`，并把 `epsilon` 从 mixed lift中完全消去。本文是 signed interface，不单独产生矛盾，因此不关闭 A2。

---

## 1. CRT integer orientation carrier

前一文件定义

\[
A_G:=\frac{M+5\eta}{2}+8,
\qquad
B_G:=3M-d-\eta-3,
\]

以及

\[
\boxed{
\mathscr O_\Delta
:=2^{A_G}Q_\Delta-5^{B_G}k_h^3.}
\tag{1.1}
\]

并严格证明

\[
\boxed{
\varepsilon=-1
\iff
\mathscr O_\Delta>0,}
\tag{1.2-}
\]

\[
\boxed{
\varepsilon=+1
\iff
\mathscr O_\Delta<0.}
\tag{1.2+}
\]

因此统一写成

\[
\boxed{
\operatorname{sgn}(\mathscr O_\Delta)=-\varepsilon.}
\tag{1.3}
\]

特别地 `O_Delta` 永不为零。

---

## 2. centered Hensel representative and mixed sign

`endpoint-lattice.md` §16.23 定义唯一 centered odd representative

\[
\boxed{
-\frac g2<z_E<\frac g2,
\qquad
c_-z_E\equiv-5^{d+1}H\pmod g,}
\tag{2.1}
\]

并证明

\[
\boxed{z_E\ne0,\qquad \gcd(z_E,g)=1.}
\tag{2.2}
\]

后续 mixed lift定义 `chi_E`，满足 exact identity

\[
\boxed{
g\chi_E=c_uC+\varepsilon a_2c_-z_E.}
\tag{2.3}
\]

其中 endpoint narrowness给

\[
0<c_uC<a_2c_-|z_E|.
\tag{2.4}
\]

所以大项唯一决定符号：

\[
\boxed{
\operatorname{sgn}(\chi_E)
=\operatorname{sgn}(\varepsilon z_E).}
\tag{2.5}
\]

并且 `chi_E!=0`。

---

## 3. fixed negative triple sign

由 (1.3),(2.5)：

\[
\operatorname{sgn}(\mathscr O_\Delta z_E\chi_E)
=(-\varepsilon)\cdot\operatorname{sgn}(z_E)
\cdot\varepsilon\operatorname{sgn}(z_E)
=-1.
\]

因此得到

\[
\boxed{
\mathscr O_\Delta\,z_E\,\chi_E<0.}
\tag{3.1}
\]

三因子均为非零整数，所以这是严格 signed allocation，而不是弱不等式。

等价地：

\[
\boxed{
\operatorname{sgn}(\mathscr O_\Delta)
=-\operatorname{sgn}(z_E\chi_E).}
\tag{3.2}
\]

于是 additive CRT quotient的 normalized side与真实 decimal defect `H mod g` 产生的 centered Hensel side已经直接对接。

---

## 4. eliminate the external Gaussian-side symbol

由 (1.3)：

\[
\varepsilon=-\operatorname{sgn}(\mathscr O_\Delta).
\]

代入 (2.3)：

\[
\boxed{
 g\chi_E
 =c_uC
 -\operatorname{sgn}(\mathscr O_\Delta)
  a_2c_-z_E.}
\tag{4.1}
\]

所以 reflection high-2 的 mixed signed kernel可以完全写成

\[
\boxed{
(\mathscr O_\Delta,z_E,\chi_E)}
\tag{4.2}
\]

三个 ordinary integers；不再需要把 `epsilon` 当作一个独立 binary choice带到后续证明中。

这点对有限 slot 特别有用：任何后续 congruence、natural-representative 或 sign estimate如果能从 `(Q_Delta,H)` 独立决定 `O_Delta` 与 `z_E chi_E` 同号，就会与 (3.1) 立即矛盾。

---

## 5. quantitative contact remains extremely narrow

`endpoint-lattice.md` 还已有

\[
\left|
\frac{g\chi_E}{\varepsilon a_2c_-z_E}-1
\right|<\frac3{50000}.
\]

用 `epsilon=-sgn(O_Delta)` 改写：

\[
\boxed{
\left|
\frac{g\chi_E}
{-\operatorname{sgn}(\mathscr O_\Delta)a_2c_-z_E}
-1
\right|<\frac3{50000}.}
\tag{5.1}
\]

所以 (3.1) 不只是象限关系：`chi_E` 在由 `O_Delta` 选定的反向 ray 上具有小于 `6e-5` 的相对偏差。

---

## 6. current role

本文没有产生新的 independent character；它把此前两个已经严格的 Archimedean inputs组合成同一 signed integer interface。

新的 closure target可以明确写成：从 additive CRT residue / exact `2,5` gap phase与 centered congruence

\[
c_-z_E\equiv-5^{d+1}H\pmod g
\]

推出 `O_Delta z_E chi_E>0`，或直接固定 `O_Delta` 的错误符号。任一结果都会与 (3.1) 冲突并排除相应 high-2 allocation。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-l9-singular-audit"></a>

> 整合来源：`spontaneous-crt-l9-singular-audit.md`

# A2 descent singular gate `L_9` 的 support audit

> **依赖：** `spontaneous-crt-descent-overlap-nogo.md`、`spontaneous-crt-f1270-source-audit.md`、`spontaneous-height-equal-depth-dual-short-carriers.md`。
>
> **严格状态：**`Rstar_63/D_63` overlap 的 `K`-resultant除 `F_1270` 外还留下 singular linear gate `L_9=TK-9T-2a_3`。本文证明 `L_9=alpha-3(3T+a_3)`，所以任何 non-3 alpha-supported prime进入该 gate都会强迫 `3T+a_3=0`；这与 target third carrier `R_3=6(3T+a_3)^2+T^2` 立即矛盾。因此整个 genuine equal-depth target support与 `L_9` singular branch完全分离。对 source-common、central、q/height supports，`L_9` 的 resultants均为极短 positive linear carriers。本文仍不排除 generic alpha-free external `L_9` roots，因此不关闭 A2。

---

## 1. the singular linear form

定义

\[
\boxed{L_9:=TK-9T-2a_3.}
\tag{1.1}
\]

真实 concatenated numerator为

\[
\alpha=TK+a_3.
\]

令

\[
\boxed{A_3:=3T+a_3.}
\tag{1.2}
\]

则有 exact identity

\[
\boxed{L_9=\alpha-3A_3.}
\tag{1.3}
\]

所以该 singular gate不是新的任意 third linear form；它直接测量 concatenated numerator与 shifted third coordinate的差。

---

## 2. any alpha-supported non-3 prime is forced into `A_3`

固定 odd prime `p\ne3`。若

\[
p\mid\alpha,
\qquad
p\mid L_9,
\]
由 (1.3)：

\[
\boxed{p\mid A_3=3T+a_3.}
\tag{2.1}
\]

这与 `endpoint-lattice.md` 旧 mixed/saturation audit中的唯一 zero-factor `A_3` 完全一致：`L_9` 在 alpha-supported sector没有产生新的 prime source，只回流到已知 shifted-third saturation。

---

## 3. equal-depth target support is impossible on `L_9`

真正 equal-depth target prime满足

\[
p\mid\omega W_q=\alpha
\]
并且进入 short third carrier

\[
\boxed{
R_3:=6(a_3+3T)^2+T^2
=6A_3^2+T^2.}
\tag{3.1}
\]

若同时 `p|L_9`，由 §2：

\[
p\mid A_3.
\]

于是

\[
R_3\equiv T^2\pmod p.
\]

所有 genuine target prime与 `10` 分离，所以 `p∤T`。故

\[
\boxed{p\nmid R_3,}
\]
与 target condition矛盾。

因此

\[
\boxed{
\operatorname{Supp}_{\rm target}^{\rm gen}
\cap
\operatorname{Supp}(L_9)
=\varnothing.}
\tag{3.2}
\]

这对 entire equal-depth target pool成立，不留 fixed exception。

结合 `spontaneous-crt-f1270-source-audit.md`：descent-overlap的两个 singular branches在 target sector已经完全分类为

\[
\boxed{
L_9:\ \varnothing,
\qquad
F_{1270}:\ \{7,79,107,199\}.}
\tag{3.3}
\]

所以 moving equal-depth target不能藏在 descent overlap的 singular locus中。

---

## 4. source-common overlap pays `107T+36a_3`

source-common linear sheet为

\[
18K-55.
\]

直接 resultant：

\[
\boxed{
\operatorname{Res}_K(L_9,18K-55)
=107T+36a_3.}
\tag{4.1}
\]

定义

\[
\boxed{L_9^{src}:=107T+36a_3.}
\tag{4.2}
\]

endpoint给

\[
1<a_3/T<251/250,
\]
所以

\[
\boxed{
143T<L_9^{src}<144T.}
\tag{4.3}
\]

因此 singular `L_9` 若与 source-common pool复用 prime，要支付给一个只有 `m+3` 位量级的 positive third-block linear integer。

---

## 5. central overlap pays `9T+4a_3`

与 central additive gate

\[
2K-9
\]
消元：

\[
\boxed{
\operatorname{Res}_K(L_9,2K-9)
=9T+4a_3.}
\tag{5.1}
\]

定义

\[
\boxed{L_9^{cen}:=9T+4a_3.}
\tag{5.2}
\]

则

\[
\boxed{
13T<L_9^{cen}<14T.}
\tag{5.3}
\]

所以 central/singular reuse同样由一个极短 positive third integer读取；不存在 free central overlap。

---

## 6. q/height overlap pays `CT+2DA_3`

source/height linear equation为

\[
DK-(3D-C)=0.
\]

resultant：

\[
\boxed{
\operatorname{Res}_K(
L_9,DK-(3D-C))
=CT+6DT+2Da_3.}
\tag{6.1}
\]

使用 `A_3=3T+a_3`：

\[
\boxed{
L_9^{H}:=CT+2DA_3.}
\tag{6.2}
\]

它显然 positive。归一化：

\[
\frac{L_9^{H}}{DT}
=\frac CD+2\left(3+\frac{a_3}{T}\right).
\]

所以

\[
\boxed{
8<\frac{L_9^{H}}{DT}<\frac{201}{25}.}
\tag{6.3}
\]

即 `q` denominator或 `W_q` height support若命中 `L_9`，完整 first-layer contact被压到一个约 `8DT` 的 source/third natural carrier。

---

## 7. target quadratic resultant is only the old `sqrt(-6)` shadow

若只把 `L_9` 与 target prefix quadratic

\[
P(K)=6K^2-36K+55
\]
消元，得到

\[
\boxed{
\operatorname{Res}_K(P,L_9)
=217T^2+144Ta_3+24a_3^2.}
\tag{7.1}
\]

其关于 `a_3` 的 discriminant为

\[
\boxed{-96T^2=-6(4T)^2.}
\tag{7.2}
\]

所以 ordinary quadratic character只重复 target已有 `sqrt(-6)` shadow。真正排除 target的是 §3 的 exact `alpha/A_3/R_3` argument，而不是这个 Legendre condition。

---

## 8. revised singular frontier

对 descent-overlap singular locus：

- `L_9` 与 entire genuine target pool完全分离；
- `L_9` 与 source-common、central、q/height support的 intersections分别进入约 `143T`、`13T`、`8DT` 的短 carriers；
- alpha-supported overlap只回到 old `A_3` saturation channel；
- target quadratic resultant本身只是旧 `sqrt(-6)` character。

所以 singular moving difficulty现在只剩 **generic alpha-free, source-free, noncentral external `L_9` roots**，以及 `F_1270` 的 generic external roots。它们不再能免费复用 equal-depth target pool。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-omega-content-descent"></a>

> 整合来源：`spontaneous-crt-omega-content-descent.md`

# A2 omega-content / descendant common overlap 的唯一 top-defect residue

> **依赖：** `spontaneous-omega-content-common.md`、`spontaneous-omega-biquadratic.md`、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descended-quotient-orientation.md`。
>
> **严格状态：**omega-content common prime满足 `p|omega`，因而 `alpha=beta=0 mod p`，但一般不进入 `W_q` height。本文把 source triangle与全局 quotient `qW_q=DK-N` 代入 descended quotient，消去 `W_q,H_0`。非central branch中，真实 top defect `delta=C/D` 被 `K` 唯一确定；乘回整数得到正 natural carrier `H_{omega Delta}`。central branch `2K-9=0` 与 descendant equation只可能在 fixed non-3 prime `7` 相交。本文没有排除 simple p-adic wrapping，因此不关闭 A2。

---

## 1. omega-content first layer

固定 genuine odd non-`3` inert prime

\[
p\mid\omega.
\]

由

\[
\alpha=TK+a_3=\omega W_q,
\qquad
\beta=TQ+b_3=\omega S
\]
有

\[
\boxed{\alpha\equiv\beta\equiv0\pmod p.}
\tag{1.1}

`spontaneous-omega-content-common.md` 已证明 omega-content 与 denominator/source-discriminant 分离：

\[
\boxed{p\nmid qf c_u gT.}
\tag{1.2}

source triangle为

\[
z=g\omega-c_u=q5^\lambda.
\]
所以模 `p|omega`：

\[
\boxed{q5^\lambda\equiv-c_u\pmod p.}
\tag{1.3}

---

## 2. height value becomes a rational defect expression

全局 height quotient为

\[
qW_q=DK-N,
\qquad
H_0=c_uW_q.
\]

由 (1.3) 且 `q` 为 unit：

\[
\frac{c_u}{q}\equiv-5^\lambda\pmod p.
\]

因此

\[
H_0
=c_u\frac{DK-N}{q}
\equiv
-5^\lambda(DK-N)
\pmod p.
\tag{2.1}

又

\[
D=g2^m5^d,
\qquad
T=2^m5^{\lambda+d},
\]
故

\[
\boxed{gT=D5^\lambda.}
\tag{2.2}

所有量在 p 处为 unit，可除得

\[
\frac{H_0}{gT}
\equiv
-\frac{DK-N}{D}
\pmod p.
\]

写

\[
\delta:=\frac CD,
\qquad
N=3D-C=D(3-\delta),
\]
于是

\[
\boxed{
\frac{H_0}{gT}
\equiv3-K-\delta
\pmod p.}
\tag{2.3}

所以 omega-content虽然不令 `H_0=0`，但把它完全恢复成 `(K,delta)` 的线性式。

---

## 3. descended common equation fixes `delta`

fully primitive descended quotient满足 exact identity

\[
\boxed{
16\mathscr F_{63}
=3gT G_D(K)
-16(2K-9)(g\alpha+H_0),}
\tag{3.1}

其中

\[
\boxed{G_D(K)=11K^2-240K+432.}
\tag{3.2}

若同一个 omega-content prime还进入 descendant common gcd，则

\[
p\mid\widehat{\mathscr D}_{63}
\Longrightarrow
p\mid\mathscr F_{63}.
\]

利用 `alpha=0` 与 (2.3)，除去 unit `gT`：

\[
\boxed{
3G_D(K)
-16(2K-9)(3-K-\delta)
\equiv0\pmod p.}
\tag{3.3}

若

\[
2K-9\not\equiv0\pmod p,
\]
则 top defect residue唯一：

\[
\boxed{
\delta
\equiv
3-K-
\frac{3G_D(K)}{16(2K-9)}
\pmod p.}
\tag{3.4}

完全化简为

\[
\boxed{
\delta
\equiv
\frac{-65K^2+960K-1728}
{16(2K-9)}
\pmod p.}
\tag{3.5}

所以 simple omega-content root一旦给定 `K mod p`，descendant common condition不再留下独立的 `C/D` first digit。

---

## 4. positive natural representative

将 (3.5) 乘回 `D`，定义 ordinary integer

\[
\boxed{
\mathscr H_{\omega\Delta}
:=D(65K^2-960K+1728)
+16C(2K-9).}
\tag{4.1}

每个 noncentral omega-content/descent common prime都满足

\[
\boxed{p\mid\mathscr H_{\omega\Delta}.}
\tag{4.2}

真实 endpoint中

\[
K>9\cdot10^{11},
\qquad
D>0,
\qquad C>0.
\]

并且

\[
65K^2-960K+1728>0,
\qquad
2K-9>0,
\]
所以

\[
\boxed{\mathscr H_{\omega\Delta}>0.}
\tag{4.3}

粗尺度为

\[
\boxed{
65DK^2-960DK
<\mathscr H_{\omega\Delta}
<66DK^2}
\tag{4.4}

对当前 huge K成立；右端使用 `C<D` 与低阶项被 `DK^2` 吸收。

这不是小到能单独排除 p-adic wrapping，但它给 content/descent common support一个 explicit natural representative，而不是未命名的 resultant。

---

## 5. Archimedean direction is opposite to the real endpoint

把 (3.5) 的右边当作实函数

\[
\delta_{\omega\Delta}(K)
:=
\frac{-65K^2+960K-1728}{16(2K-9)}.
\]

对 `K>9*10^11`：numerator严格为负、denominator严格为正，所以

\[
\boxed{\delta_{\omega\Delta}(K)<0.}
\tag{5.1}

而真实 finite-defect endpoint满足

\[
\boxed{0<\delta=C/D<3/250.}
\tag{5.2}

因此 omega-content/descent common root不可能来自真实邻域中的实交点：

\[
\boxed{
\text{every such common root is genuinely p-adic wrapping}.}
\tag{5.3}

这与 `spontaneous-omega-biquadratic.md` 中 content roots本身避开真实 numerator window的结论方向一致，但二者是不同的 Archimedean separation：这里直接发生在 top defect `C/D`。

---

## 6. central branch is only fixed `7`

现在考虑

\[
2K-9\equiv0\pmod p.
\]

由 descendant equation (3.3)，第二项消失，所以还必须

\[
G_D(K)\equiv0\pmod p.
\]

resultant：

\[
\boxed{
\operatorname{Res}_K(G_D,2K-9)
=-1701
=-3^5\cdot7.}
\tag{6.1}

在 genuine non-`3` sector：

\[
\boxed{p=7.}
\tag{6.2}

因此 noncentral formula (3.5) 唯一的 denominator exception不是 moving branch，只是 fixed `7`。

该 fixed `7` 是否实际满足 omega-content pure-prefix curve需要单独 finite/Hensel审计；本文不据 (6.2) 自动宣称存在或不存在。

---

## 7. revised alpha-supported content frontier

omega-content + descendant common 现在具有以下规范形式：

- pure-prefix content root仍由 `C_omega=J_H=0` / biquadratic tower读取；
- noncentral descendant condition唯一确定
  \[
  C/D\pmod p;
  \]
- common prime必须进入 positive natural carrier `H_{omega Delta}`；
- real endpoint与 required defect residue方向相反，所以只有 p-adic wrapping；
- central branch只剩 fixed `7`。

这删除了 omega-content descendant overlap中的一个自由 local coordinate，但尚未排除 simple moving content primes。下一步应把 (3.5) 与 content biquadratic的 decimal orbit `tau=10^{-M}` 联立，或对 fixed `7` 做完整 content-state audit。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-omega-content-fixed7"></a>

> 整合来源：`spontaneous-crt-omega-content-fixed7.md`

# A2 fixed `7` omega-content / descendant central branch 的 finite Hensel audit

> **依赖：** `spontaneous-crt-omega-content-descent.md`、`spontaneous-omega-content-common.md`、`spontaneous-omega-biquadratic.md`。
>
> **严格状态：**omega-content/descendant overlap的 central denominator `2K-9=0` 只可能在 fixed non-3 prime `7` 出现。本文把 content angle gate、additive content gate与 central equation在 `F_7` 中完整枚举，只剩两组 genuine unit states；两点 Jacobian均非零，因此各自只有唯一 Hensel lift。fixed `7` central exception存在局部 branches，但没有 singular tree。本文是 finite/local rigidity，不是 global exclusion，也不关闭 A2。

---

## 1. normalized content system

沿用 omega-content normalized variables

\[
x=B/N,
\qquad y=10A/N,
\qquad \tau=N^{-1}=10^{-M}.
\]

content angle gate为

\[
\boxed{
F(x,y):=
202500x^4-(101x^2+4x+4)y^2-1800x^2y.}
\tag{1.1}

additive content gate为

\[
\boxed{
\begin{aligned}
G(x,y,\tau):={}&
100x^2[5(y+9)^2-36(y+9)\tau+55\tau^2]\\
&-(x+2)^2(2025x^2+y^2).
\end{aligned}}
\tag{1.2}

而

\[
K=N(9+y)=\frac{9+y}{\tau}.
\]

central descendant branch为

\[
2K-9\equiv0\pmod7.
\]

清去 unit `tau` 后定义

\[
\boxed{C_7(x,y,\tau):=2(y+9)-9\tau.}
\tag{1.3}

所以 fixed-7 local system为

\[
\boxed{F=G=C_7=0\quad\text{in }\mathbf F_7.}
\tag{1.4}

---

## 2. complete finite enumeration

枚举

\[
\tau\in\mathbf F_7^\times,
\qquad
x\in\mathbf F_7^\times,
\qquad
y\in\mathbf F_7
\]
并排除 q-boundary `x=-2`，得到恰好两组：

\[
\boxed{
(\tau,x,y)=(4,1,2),
\qquad
(5,4,3)
\pmod7.}
\tag{2.1}

两组都满足 `x(x+2) !=0`，故不是 denominator boundary。

source collision sheet为

\[
y=225x^2.
\]

模 `7` 有 `225=1`，而两点分别满足

\[
2\ne1^2,
\qquad
3\ne4^2=2.
\]

因此

\[
\boxed{\text{两点都不在 source sheet}.}
\tag{2.2}

结合 alpha-supported sheet uniqueness，它们是真正 omega-content states，而不是 height/source collision的重命名。

---

## 3. decimal length phases

因为

\[
\tau=10^{-M}\pmod7,
\qquad10\equiv3\pmod7,
\]
且

\[
\operatorname{ord}_7(10)=6,
\]
直接查六相位：

\[
\boxed{
\tau=4\Longleftrightarrow M\equiv2\pmod6,}
\tag{3.1}

\[
\boxed{
\tau=5\Longleftrightarrow M\equiv1\pmod6.}
\tag{3.2}

所以 central fixed-7 content/descent branch只存在于

\[
\boxed{M\equiv1\text{ or }2\pmod6.}
\tag{3.3}

注意这与此前 fixed-7 equal-depth target的 `M≡1 or5 mod6` 是不同局部 branch，不可混为同一 orbit。

---

## 4. both states are nonsingular

对三方程

\[
(F,G,C_7)
\]
关于

\[
(x,y,\tau)
\]
取 Jacobian determinant。

在两点分别得到

\[
\boxed{
\det J(1,2,4)\equiv1\pmod7,}
\tag{4.1}

\[
\boxed{
\det J(4,3,5)\equiv5\pmod7.}
\tag{4.2}

全部非零。因此 multivariate Hensel lemma给：

\[
\boxed{
\text{每个 first-layer state至多有一条 compatible }7\text{-adic lift}.}
\tag{4.3}

所以 fixed7 central omega-content/descent exception不是 singular Hensel tree，也不会在每层产生指数多个 residue choices。

---

## 5. current role

omega-content/descendant common branch现在分为：

1. noncentral simple branch：`C/D` 由 `K` 唯一确定，并进入 positive natural carrier `H_{omega Delta}`；
2. central branch：仅 fixed `7`，且只剩本文两条 simple Hensel orbits。

本文没有证明这两条 `7`-adic decimal exponent orbit最终不命中真实 integer candidate；机械继续提升 `7^k` 只会唯一固定更细相位，不能当作空性。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-pure-branch-defect"></a>

> 整合来源：`spontaneous-crt-pure-branch-defect.md`

# A2 pure-spontaneous / descendant common branch 的 canonical defect residue

> **依赖：** `spontaneous-prefix-branch-audit.md`、`spontaneous-sphere-roots.md`、`spontaneous-crt-height-primitive-remainder.md`。
>
> **严格状态：**genuine alpha-free noncentral spontaneous common prime精确选择 `Q_1,Q_2` 中一个 branch；相应 third numerator由显式 sphere root `z_i(x,y)` 唯一恢复。本文把该 branch root代入 descended quotient，证明 top finite defect `delta=C/D` 也随之被唯一恢复。两 branch要求的 real defect都严格为负，而真实 endpoint defect严格为正，因此所有 pure-spontaneous/descendant common roots都必须依赖 p-adic wrapping。本文减少一个 local coordinate，但不排除 modular wrapping，因此不关闭 A2。

---

## 1. unique pure-spontaneous branch

沿用

\[
\tau=10^{-M},
\qquad
x=B/N,
\qquad
y=10A/N,
\]
并记

\[
\boxed{s:=9+y.}
\tag{1.1}

在 genuine pure-spontaneous noncentral sector：

\[
p\nmid\alpha(2K-9),
\]
且排除既有 source/denominator/prefix boundaries。

`spontaneous-prefix-branch-audit.md` 已证明此时恰有唯一

\[
i\in\{1,2\}
\]
满足

\[
\boxed{\mathcal Q_i(\tau;x,y)\equiv0\pmod p.}
\tag{1.2}

`spontaneous-sphere-roots.md` 把两支恢复成显式 normalized third numerator

\[
\boxed{
\bar\zeta=z_i(x,y),}
\tag{1.3}

其中

\[
\bar\zeta:=\frac{a_3}{TN}.
\]

所以在该 branch：

\[
\boxed{
K=\frac{s}{\tau},
\qquad
\zeta:=\frac{a_3}{T}=\frac{z_i}{\tau}.}
\tag{1.4}

---

## 2. universal descendant defect equation

fully primitive descended quotient可写成

\[
\widehat{\mathscr D}_{63}=c_u^2\mathscr F_{63},
\]

\[
\mathscr F_{63}
=(2K-9)\{g((2K-9)T-a_3)-H_0\}
-\frac{63}{16}gTK^2.
\tag{2.1}

finite-defect height identity为

\[
\boxed{
\frac{H_0}{gT}
=3+\zeta-\delta,
\qquad
\delta:=C/D.}
\tag{2.2}

所以除以 positive/genuine unit `gT`：

\[
\frac{\mathscr F_{63}}{gT}
=(2K-9)(2K-12-2\zeta+\delta)
-\frac{63}{16}K^2.
\tag{2.3}

若 prime进入 descendant common support，`F63=0 mod p`。在 noncentral sector `2K-9` 为 unit，故

\[
\boxed{
\delta
\equiv
12+2\zeta-2K
+\frac{63K^2}{16(2K-9)}
\pmod p.}
\tag{2.4}

因此 descendant condition本身已唯一固定 top defect first digit。

---

## 3. substitute the unique sphere branch

代入 (1.4)：

\[
\delta_i
=
12+rac{2z_i-2s}{\tau}
+rac{63s^2}{16\tau(2s-9\tau)}.
\]

统一清成一个分式：

\[
\boxed{
\delta_i
\equiv
\frac{
-s^2+672s\tau+64sz_i
-1728\tau^2-288\tau z_i
}
{16\tau(2s-9\tau)}
\pmod p.}
\tag{3.1}

所以两个 quadratic branches不再携带一个额外独立的 finite-defect parameter：

\[
\boxed{
(x,y,\tau,i)
\Longrightarrow
z_i
\Longrightarrow
\delta_i\pmod p}
\tag{3.2}

是 canonical chain。

这与 omega-content branch的 defect map同型，但此处不使用 `alpha=0` 或 source triangle。

---

## 4. both real branch defects are strictly negative

真实 dangerous endpoint满足

\[
\frac{249}{250}<y<1,
\qquad
s=9+y>\frac{2499}{250},
\]

\[
0<\tau\le10^{-11}.
\]

`spontaneous-sphere-roots.md` 已证明两支都满足

\[
\boxed{z_i<-4.778.}
\tag{4.1}

分母

\[
16\tau(2s-9\tau)>0.
\]

看 numerator

\[
N_i
=-s^2+672s\tau
+z_i(64s-288\tau)
-1728\tau^2.
\tag{4.2}

这里

\[
64s-288\tau
>64\frac{2499}{250}-288\cdot10^{-11}>639,
\]
所以由 `z_i<-4.778`：

\[
z_i(64s-288\tau)<-4.778\cdot639<-3052.
\]

而唯一正项满足

\[
672s\tau<6720\cdot10^{-11}<10^{-7}.
\]

其余两项 `-s^2,-1728tau^2` 非正。因此

\[
\boxed{N_i<0.}
\tag{4.3}

故两支 required real defect均满足

\[
\boxed{\delta_i<0.}
\tag{4.4}

---

## 5. opposite to the actual finite-defect endpoint

真实 rational-root state为

\[
J_{def}=3-C/D
\]
且 endpoint shell已给

\[
\boxed{0<\delta=C/D<3/250.}
\tag{5.1}

与 (4.4) 比较：

\[
\boxed{
\delta_{actual}>0,
\qquad
\delta_i^{real}<0
\quad(i=1,2).}
\tag{5.2}

所以不存在 real-nearby pure-spontaneous/descendant intersection。任何 modular common prime都必须让 branch root跨过一个固定符号间隔，通过 genuine p-adic wrapping匹配真实 positive defect。

这不是单独的矛盾：模 p 的同余不要求实数接近。它的严格新增作用是把 descendant common branch从

\[
\text{prefix branch}+\text{free }C/D
\]
压成

\[
\boxed{\text{prefix branch}+\text{canonical }C/D\text{ residue}.}
\tag{5.3}

---

## 6. revised pure-spontaneous external kernel

在 alpha-free、noncentral、source/denominator-separated sector，真正 remaining descendant common prime现在必须同时满足：

1. 唯一 `Q_i` decimal branch；
2. sphere root `z_i(x,y)`；
3. canonical defect residue (3.1);
4. actual decimal orbit `tau=10^{-M}`。

所以 local freedom只剩 prefix decimal orbit本身；third numerator与 finite defect都已被 branch唯一恢复。

下一步最自然的是把 (3.1) 与 `C` 的 centered Hensel representative `(z_E,chi_E)` 联立，或清分母得到 branch-specific natural integer并对其 required p-depth做 height comparison。ordinary discriminant stacking仍不会新增 obstruction。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-pure-coefficient-singular"></a>

> 整合来源：`spontaneous-crt-pure-coefficient-singular.md`

# A2 pure-spontaneous descendant coefficient singularity 只剩 projective ratio gates

> **依赖：** `spontaneous-crt-pure-prefix-elimination.md`、`spontaneous-single-branch.md`。
>
> **严格状态：**generic pure-spontaneous descendant compatibility在 branch quadratic 上降成 `A_63 tau+B_63=0`；只有 `A_63=B_63=0` 时 decimal phase不能被唯一恢复。本文直接消去 prefix norm ratio `c`，证明 coefficient-singular locus分解成两个只依赖 projective ratio `u=z/s=a_3/(TK)` 的齐次 gate `H_4,H_24`，次数分别 4 与24。因此 singular coefficient branch不会重新长回二维 local family；它只是一维 ratio bad locus。本文不排除这些 finite-field ratio roots，因此不关闭 A2。

---

## 1. branch remainder

沿用 compact single-branch variables

\[
s=9+y,
\qquad z=z_i(x,y),
\]

\[
c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2},
\qquad
\tau=10^{-M}.
\]

universal descendant cubic modulo branch quadratic给 primitive linear remainder

\[
\boxed{
\widetilde E_{63}
\equiv A_{63}(s,z,c)\tau+B_{63}(s,z,c)
\pmod{L_z}.}
\tag{1.1}

已有

\[
\deg A_{63}=7,
\qquad A_{63}\text{ 有 }20\text{ 项},
\]

\[
\deg B_{63}=8,
\qquad B_{63}\text{ 有 }24\text{ 项}.
\]

在

\[
A_{63}\not\equiv0\pmod p
\]
时

\[
\tau\equiv-B_{63}A_{63}^{-1}\pmod p
\]
唯一，所以只需单列 coefficient-singular branch

\[
\boxed{A_{63}=B_{63}=0.}
\tag{1.2}

---

## 2. eliminate `c`

把 `A_63,B_63` 看成 `c` 的多项式：

\[
\deg_c A_{63}=3,
\qquad
\deg_c B_{63}=4.
\]

直接求 resultant并取 primitive part，得到完全因子化：

\[
\boxed{
\operatorname{Res}_c(A_{63},B_{63})
=2^{72}3^{32}5^9 11^9\,
H_4(s,z)H_{24}(s,z).}
\tag{2.1}

这里

\[
\boxed{
\begin{aligned}
H_4(s,z)={}&31476144004s^4
+114775877404s^3z\\
&+90353275489s^2z^2
-46902675456sz^3\\
&-29520930816z^4,
\end{aligned}}
\tag{2.2}

而 `H_24` 是 primitive homogeneous degree-24 polynomial，恰有25个 nonzero monomials。

完整 `H_24` coefficients由 checker从 `A_63,B_63` 直接重建并验证 factorization；正文不重复塞入机械大整数。

当前 genuine pure-spontaneous prime已排除 fixed coefficient primes `2,3,5,11`，所以 (2.1) 给严格必要条件

\[
\boxed{
A_{63}=B_{63}=0
\Longrightarrow
H_4(s,z)=0
\quad\text{或}\quad
H_{24}(s,z)=0.}
\tag{2.3}

---

## 3. both gates are projective

`H_4,H_24` 都是齐次式：

\[
H_4(s,z)=s^4 h_4(z/s),
\]

\[
H_{24}(s,z)=s^{24}h_{24}(z/s).
\]

而 genuine branch中 `s` 是 unit。因此 coefficient singularity只依赖

\[
\boxed{u:=z/s.}
\tag{3.1}

真实意义上

\[
u=rac{\bar\zeta}{9+y}
=rac{a_3}{TK}.}
\tag{3.2}

所以原来可能看似依赖

\[
(s,z,c,\tau)
\]
四个坐标的 singular coefficient condition，实际上已降成一个单 projective ratio 的 finite-field root问题。

---

## 4. low-degree ratio gate

令 `s=1,z=u`，低次 gate为

\[
\boxed{
\begin{aligned}
h_4(u)={}&
-29520930816u^4
-46902675456u^3\\
&+90353275489u^2
+114775877404u\\
&+31476144004.
\end{aligned}}
\tag{4.1}

其 discriminant support为

\[
\boxed{
2^{21}3^{13}5^{13}7^6 11^{12}13^3 19\,29^2\,163\,
6661944924691447.}
\tag{4.2}

本文只记录该 bad-prime support，不把 discriminant character误当作 generic closure：simple roots of `h_4` 仍可存在于其它 primes。

真实 roots约为

\[
-2.273557786\ldots,
\qquad
1.718575838\ldots,
\]

另有一对非实共轭根。该 real information只用于后续 Archimedean audit，不是 modular exclusion。

---

## 5. no renewed Hensel dimension

因此 pure-spontaneous descendant branch的 local structure现在严格分成：

### generic coefficient

\[
A_{63}\ne0:
\quad
\boxed{\tau=-B_{63}/A_{63}}
\]
唯一，随后 `C/D` 也由 descendant defect map唯一恢复。

### coefficient singular

\[
A_{63}=0:
\]
common compatibility还要求 `B_63=0`，从而

\[
\boxed{h_4(u)=0\quad\text{或}\quad h_{24}(u)=0.}
\]
只剩一维 projective ratio root。

所以 coefficient singularity不会重新产生一个自由 `(tau,c)` Hensel sheet；其维数已经被 resultant压缩。

---

## 6. next use

后续最值得做的是：

1. 把 `h_4/h_24` 与两张 explicit sphere ratio `u_i=z_i/(9+y)` 联立；
2. 或对 generic `A_63!=0` 分支把 `tau=-B/A` 清成 natural decimal representative，与 `tau=10^{-M}` 的 orbit做高度/符号同步。

单独继续审 `h_4/h_24` 的 ordinary discriminant不会自动关闭 simple roots。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-pure-h24-parity"></a>

> 整合来源：`spontaneous-crt-pure-h24-parity.md`

# A2 `H_24` projective carrier 的 compact integer clearing 与 exact `5 mod 8` orientation

> **依赖：** `spontaneous-crt-pure-h24-projective.md`、deep-even primitive reduction、`spontaneous-crt-pure-h4-parity.md`。
>
> **严格状态：**`H_24` coefficient-singular component把 projective norm ratio `v=c/s^2` 送入 primitive irreducible degree-24 polynomial `P_24(v)`，且真实 endpoint `0<v<21/20` 上 `P_24` 无零点。本文识别 `v=Q^2N_0/(B^2K^2)`，将 `P_24` 清成仅 25 个 composite monomials 的 ordinary integer carrier。利用 deep-even 中 `B^2K^2` 比 `Q^2N_0` 至少多 16 层二进深度，证明最高次 `v^24` 项是唯一最低层，从而 `v_2(V_24)=48M+147`，positive primitive quotient恒为 `5 mod8`。所以高次 coefficient-singular branch本身不强迫 odd-inert surcharge；这与 `H_4` 的 `7 mod8` orientation严格不同。本文仍不排除 modular `H_24` roots，因此不关闭 A2。

---

## 1. the projective norm ratio is an exact prefix quotient

沿用

\[
x=B/N,
\qquad y=10A/N,
\qquad s=9+y=K/N,
\]

以及

\[
c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.
\]

因为

\[
Q=B+2N,
\qquad
100N_0=2025B^2+100A^2,
\]
直接得到

\[
\boxed{
c=\frac{Q^2N_0}{B^2N^2}.}
\tag{1.1}
\]

再除以

\[
s^2=K^2/N^2,
\]
所以 `H_24` projective ratio精确为

\[
\boxed{
v:=\frac c{s^2}
=\frac{Q^2N_0}{B^2K^2}.}
\tag{1.2}
\]

定义两个 positive integer blocks

\[
\boxed{X:=Q^2N_0,\qquad Y:=B^2K^2.}
\tag{1.3}
\]

于是 `v=X/Y`。

---

## 2. compact ordinary integer carrier

前一文件定义 leading coefficient为正的 primitive polynomial

\[
\boxed{
\mathscr P_{24}(v)=\sum_{j=0}^{24}p_jv^j
\in\mathbf Z[v].}
\tag{2.1}
\]

定义 ordinary integer clearing

\[
\boxed{
\mathscr V_{24}
:=Y^{24}\mathscr P_{24}(X/Y)
=\sum_{j=0}^{24}p_jX^jY^{24-j}.}
\tag{2.2}
\]

所以尽管清回原 prefix variables后总次数很高，结构上只有 `25` 个 composite monomials。

任何 `H_24` coefficient-singular prime在 fixed denominator/content exceptions之外都必须满足

\[
\boxed{p\mid\mathscr V_{24}.}
\tag{2.3}
\]

---

## 3. exact binary depths of the two blocks

当前 deep-even normal form给

\[
Q=2^{M+1}Q_0,
\qquad Q_0\text{ odd},
\]
而 `A` 为奇数、`B/2` 为偶数，所以

\[
\boxed{N_0\text{ odd}.}
\tag{3.1}
\]

因此

\[
\boxed{v_2(X)=2M+2.}
\tag{3.2}
\]

另一方面

\[
\boxed{v_2(B)=M+m+t.}
\tag{3.3}
\]

又

\[
K=9N+10A,
\]
其中 `9N` 被 `4` 整除而 `10A\equiv2 mod4`，故

\[
\boxed{v_2(K)=1.}
\tag{3.4}
\]

所以

\[
\boxed{v_2(Y)=2M+2m+2t+2.}
\tag{3.5}
\]

两块深度差为

\[
\boxed{\delta:=v_2(Y)-v_2(X)=2m+2t\ge16,}
\tag{3.6}
\]
因为 dangerous branch中 `m>=5,t>=3`。

---

## 4. coefficient audit: the `X^24` term is uniquely shallowest

对 `P_24` 的 25 个 primitive integer coefficients做 exact `2`-adic audit。最高次 coefficient满足

\[
\boxed{v_2(p_{24})=99,}
\tag{4.1}
\]

并且

\[
\boxed{p_{24}/2^{99}\equiv5\pmod8.}
\tag{4.2}
\]

对其余 `j<24`，checker验证统一 inequality

\[
\boxed{
\min_{0\le j\le23}
\left(v_2(p_j)+(24-j)\cdot16\right)=109>99.}
\tag{4.3}
\]

实际 `delta>=16`，所以 (2.2) 中第 `j` 项相对于公共 `24v_2(X)` 的额外 depth为

\[
v_2(p_j)+(24-j)\delta.
\]

因此 `j=24` 是唯一最低层，不存在 first-layer cancellation：

\[
\boxed{
 v_2(\mathscr V_{24})
=24(2M+2)+99
=48M+147.}
\tag{4.4}

---

## 5. primitive orientation is `5 mod 8`

除以 (4.4) 的完整二进 content，模 `8` 只剩最高次项：

\[
\frac{\mathscr V_{24}}{2^{48M+147}}
\equiv
\frac{p_{24}}{2^{99}}
\left(
\frac{X}{2^{2M+2}}
\right)^{24}
\pmod8.
\]

`X/2^{2M+2}` 为奇数，而任意奇数的偶次平方满足

\[
\left(X/2^{2M+2}\right)^{24}\equiv1\pmod8.
\]

结合 (4.2)：

\[
\boxed{
\frac{\mathscr V_{24}}{2^{48M+147}}
\equiv5\pmod8.}
\tag{5.1}

---

## 6. positivity on the real endpoint

`spontaneous-crt-pure-h24-projective.md` 已证明

\[
\mathscr P_{24}(v)\ne0
\qquad(0<v<21/20),
\]
且 primitive normalization取 positive leading coefficient。checker同时验证

\[
\boxed{\mathscr P_{24}(0)=p_0>0.}
\tag{6.1}
\]

因为 `(0,21/20)` 内没有实根，`P_24` 在该连通区间不变号，所以

\[
\boxed{\mathscr P_{24}(v)>0
\qquad(0<v<21/20).}
\tag{6.2}
\]

又 `Y>0`，故真实 endpoint上

\[
\boxed{\mathscr V_{24}>0.}
\tag{6.3}

因此 (5.1) 是 positive primitive orientation。

---

## 7. contrast with the low component

两条 coefficient-singular escape现在有不同的 parity ledger：

\[
\boxed{
H_4:\quad
H_{V4}/2^{2M+6}\equiv7\pmod8,}
\tag{7.1}
\]

所以 low component自身强迫 odd-inert parity；而本文给

\[
\boxed{
H_{24}:\quad
\mathscr V_{24}/2^{48M+147}\equiv5\pmod8.}
\tag{7.2}

`5 mod8` 在模 `4` 下为 `1`，因此 `H_24` compact carrier的 total `3 mod4` prime valuation parity为偶数。

这不排除某枚 inert prime整除 `V_24`；它只说明 high coefficient-singular escape**没有像 `H_4` 那样自动再产生一份 odd-inert surcharge**。

---

## 8. updated frontier

coefficient-singular sector现在已完成结构与 parity 分流：

- `H_4`：short irreducible degree-4 prefix carrier，positive primitive `7 mod8`；
- `H_24`：25-term compact block carrier，positive primitive `5 mod8`，real endpoint singularity为空。

因此继续对 `H_24` 做 discriminant hunting收益已经很低。真正剩余的大块回到 generic `A_63!=0` pure-prefix carrier与 descendant common gcd 的 global depth/product allocation。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-pure-h24-projective"></a>

> 整合来源：`spontaneous-crt-pure-h24-projective.md`

# A2 `H_24` coefficient singularity 的 projective elimination 与 real exclusion

> **依赖：** `spontaneous-crt-pure-coefficient-singular.md`、`spontaneous-crt-pure-h4-projective-center.md`、`spontaneous-single-branch.md`。
>
> **严格状态：**`A_63=B_63=0` 的 coefficient-singular locus 已分成 projective gates `H_4(s,z)=0` 与 `H_24(s,z)=0`。低次 `H_4` 已进一步压成固定 projective norm center。本文处理高次 `H_24`：最后一次 subresultant 在 `H_24` component 上仍只有一次 `v=c/s^2` 自由，写成 `a_15(u)v+b_17(u)=0`；消去 `u=z/s` 得到一个 primitive irreducible degree-24 polynomial `P_24(v)`。精确 Sturm 计数证明 `P_24` 的四个实根分别落在 `(-7,-6),(-6,-5),(6/5,5/4),(16,17)`，因而真实 endpoint 的 `0<v<21/20` 完全不可能。该结论只排除实退化；模素数的 `p`-adic wrapping 仍可能存在，所以不关闭 A2。

---

## 1. projective variables

沿用 coefficient-singular remainder

\[
A_{63}(s,z,c)\tau+B_{63}(s,z,c).
\]

定义 projective ratios

\[
\boxed{
u:=\frac zs,\qquad v:=\frac c{s^2}.}
\tag{1.1}
\]

其中 genuine branch 中 `s` 为 unit。把 `s=1,z=u,c=v` 代入：

\[
\boxed{
A(u,v):=A_{63}(1,u,v),
\qquad
B(u,v):=B_{63}(1,u,v).}
\tag{1.2}
\]

已有

\[
\deg_v A=3,
\qquad
\deg_v B=4.
\tag{1.3}
\]

`spontaneous-crt-pure-coefficient-singular.md` 已证明

\[
\operatorname{Res}_v(A,B)
=\text{fixed content}\cdot h_4(u)h_{24}(u),
\tag{1.4}
\]

其中 `h_24` primitive irreducible，次数 `24`。

---

## 2. `H_24` component 上 `v` 仍只有一层自由

对 `A,B` 关于 `v` 取 subresultant sequence。最后一个正次数 subresultant 恰为一次式：

\[
\boxed{
S_1(u,v)=a_{15}(u)v+b_{17}(u).}
\tag{2.1}
\]

其中 primitive coefficient polynomials 满足

\[
\boxed{
\deg a_{15}=15,
\qquad
\deg b_{17}=17,}
\tag{2.2}
\]

并且二者在 `Q[u]` 中均不可约。

因此在任意 characteristic-zero `H_24` common point上，`v` 不会重新成为独立参数；若 `a_15(u)\ne0`，则

\[
\boxed{
v=-\frac{b_{17}(u)}{a_{15}(u)}.}
\tag{2.3}
\]

模素数时，`a_15` 与 `h_24` 的 fixed resultant support需要单列为 coefficient exceptions；这仍是固定 prime set，不产生 moving two-dimensional Hensel sheet。

---

## 3. eliminate `u`: a single degree-24 norm-ratio polynomial

定义 canonical projected polynomial

\[
\boxed{
\mathscr P_{24}(v)
:=\operatorname{pp}_{\mathbf Z[v]}
\operatorname{Res}_u
\bigl(h_{24}(u),a_{15}(u)v+b_{17}(u)\bigr),}
\tag{3.1}
\]

并取 leading coefficient为正的 primitive normalization。

checker 直接从 universal cubic、branch quadratic 与 subresultant sequence重建该对象。精确得到

\[
\boxed{
\deg\mathscr P_{24}=24,
\qquad
\#\operatorname{supp}(\mathscr P_{24})=25,}
\tag{3.2}
\]

以及

\[
\boxed{
\mathscr P_{24}\text{ 在 }\mathbf Q[v]\text{ 中不可约}.}
\tag{3.3}
\]

正文不抄写 25 个巨大 coefficient；(3.1) 是 canonical exact definition，而 checker验证 primitive normalization、次数、support与不可约性。

任何 real coefficient-singular point落在 `H_24` component时，都必须满足

\[
\boxed{\mathscr P_{24}(v)=0.}
\tag{3.4}
\]

---

## 4. exact Sturm audit

对 `P_24` 使用 exact rational Sturm root count，得到

\[
\boxed{
N_{\mathbf R}(\mathscr P_{24})=4.}
\tag{4.1}
\]

并且四个实根分别且唯一地位于

\[
\boxed{
(-7,-6),
\quad(-6,-5),
\quad\left(\frac65,\frac54\right),
\quad(16,17).}
\tag{4.2}
\]

四个区间已经贡献全部四个实根，因此不存在其它 real root。

特别地

\[
\boxed{
N_{(0,21/20)}(\mathscr P_{24})=0.}
\tag{4.3}
\]

这完全是整数/有理 Sturm certificate，不依赖 floating-point root approximation。

---

## 5. real endpoint exclusion

真实 dangerous endpoint 的 norm ratio为

\[
\boxed{
v_{\rm end}
=\frac c{s^2}
=\frac{(x+2)^2(2025x^2+y^2)}
{100x^2(9+y)^2}.}
\tag{5.1}
\]

`H_4` projective audit 已严格证明统一窗口

\[
\boxed{0<v_{\rm end}<\frac{21}{20}.}
\tag{5.2}
\]

结合 (4.3)：

\[
\boxed{
\text{真实 endpoint 上不存在 real }H_{24}
\text{ coefficient-singular point}.}
\tag{5.3}
\]

所以 `H_24` 与 `H_4` 一样，任何 surviving congruence都必须来自真正的 `p`-adic wrapping，而不可能来自实数 singular geometry。

注意 `H_24` 与 `H_4` 的刚性程度仍不同：`H_4` generic component把 `v` 压成固定常数 `3097/1296`，而 `H_24` 只给 algebraic degree-24 projection `P_24(v)=0`。

---

## 6. updated coefficient-singular frontier

coefficient-singular escape现分成：

1. `H_4`：统一 short degree-4 prefix carrier `V_4`，并有 primitive `7 mod 8` parity surcharge；
2. `H_24`：projective `v` 被 degree-24 irreducible `P_24` 控制，且 real endpoint interval完全无根。

两支都已经排除 real singular degeneration，也都没有重新长回自由 `(tau,c)` sheet。

因此后续不应继续对 `h_24` 做普通 discriminant hunting。更值得做的是：

- 把 `P_24(v)` 清回 compact pure-prefix natural carrier并估计其 primitive parity/height；或
- 回到 generic `A_63\ne0` 的 degree-16 pure-prefix carrier，和 `Lambda_tail` / descendant common gcd 做全局 depth-product budget。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-pure-h4-parity"></a>

> 整合来源：`spontaneous-crt-pure-h4-parity.md`

# A2 `H_4` short prefix carrier 的 exact 2-adic parity

> **依赖：** `spontaneous-crt-pure-h4-short-carrier.md`、deep-even primitive reduction。
>
> **严格状态：**generic low coefficient singularity由 ordinary integer `V_4^int` 读取，且真实值严格为负。本文审计其完整二进 content：七项中唯一最低层是 `129600A^2N^2`，所以 `v_2(V_4^int)=2M+6`，primitive unit为 `1 mod8`。取正 carrier `H_V4=-V_4^int` 后 primitive orientation变成 `7 mod8`，因此每个 generic `H_4` singular candidate都伴随一份 odd-inert parity。本文没有证明这份 parity不能由原 singular prime自身支付，因此不关闭 A2。

---

## 1. integer short carrier

沿用

\[
N=10^M,
\qquad A=a_2,
\qquad B=b_2.
\]

前一文件得到

\[
\boxed{
\begin{aligned}
V_4^{int}={}&
656100B^4+2624400B^3N\\
&-7710100B^2A^2-13936500B^2AN\\
&-3647025B^2N^2+129600BA^2N\\
&+129600A^2N^2.
\end{aligned}}
\tag{1.1}

并且 real endpoint上

\[
\boxed{V_4^{int}<0.}
\tag{1.2}

所以定义 positive carrier

\[
\boxed{H_{V4}:=-V_4^{int}>0.}
\tag{1.3}

---

## 2. exact binary depths of the prefix blocks

当前 deep-even normal form给

\[
\boxed{v_2(N)=M,}
\tag{2.1}

\[
\boxed{B=2^{M+m+1}c_ug,}
\]
且

\[
g=2^{t-1}\rho,
\qquad c_u,\rho\text{ odd}.
\]
因此

\[
\boxed{v_2(B)=M+m+t.}
\tag{2.2}

primitive prefix中 `B` 为偶数，所以

\[
\boxed{A\text{ odd}.}
\tag{2.3}

同时 coefficient depths为

\[
v_2(656100)=2,
\qquad
v_2(2624400)=4,
\]

\[
v_2(7710100)=v_2(13936500)=2,
\]

\[
v_2(3647025)=0,
\qquad
\boxed{v_2(129600)=6.}
\tag{2.4}

---

## 3. the last term is uniquely shallowest

七项二进深度分别至少为

\[
2+4(M+m+t),
\]

\[
4+3(M+m+t)+M,
\]

\[
2+2(M+m+t),
\]

\[
2+2(M+m+t),
\]

\[
2(M+m+t)+2M,
\]

\[
6+(M+m+t)+M,
\]

和

\[
\boxed{6+2M}
\tag{3.1}

对应最后一项 `129600A^2N^2`。

因为 dangerous branch有

\[
m\ge5,
\qquad t\ge3,
\]
其它六项都严格高于 `2M+6`。故不存在 lowest-layer cancellation：

\[
\boxed{v_2(V_4^{int})=2M+6.}
\tag{3.2}

---

## 4. primitive unit modulo 8

除以 `2^{2M+6}` 后，模 `8` 只剩最后一项：

\[
\frac{V_4^{int}}{2^{2M+6}}
\equiv
\frac{129600}{64}
A^2\left(\frac{N}{2^M}\right)^2
\pmod8.
\]

现在

\[
129600/64=2025\equiv1\pmod8,
\]

\[
A^2\equiv1\pmod8,
\qquad
N/2^M=5^M,
\qquad
5^{2M}\equiv1\pmod8.
\]

所以

\[
\boxed{
\frac{V_4^{int}}{2^{2M+6}}
\equiv1\pmod8.}
\tag{4.1}

但 positive carrier是其相反数，因此

\[
\boxed{
\frac{H_{V4}}{2^{2M+6}}
\equiv-1\equiv7\pmod8.}
\tag{4.2}

---

## 5. odd-inert parity surcharge

定义 odd primitive part

\[
\boxed{
H_{V4}^{\circ}
:=\frac{H_{V4}}{2^{2M+6}}.}
\tag{5.1}

则

\[
H_{V4}^{\circ}>0,
\qquad
H_{V4}^{\circ}\equiv7\pmod8,
\]
特别地

\[
\boxed{H_{V4}^{\circ}\equiv3\pmod4.}
\tag{5.2}

因此 `H_V4^circ` 必含至少一枚

\[
\boxed{r\equiv3\pmod4}
\]
到奇 exponent。

所以 generic low coefficient-singular descendant common branch自身会生成一份 odd-inert parity surcharge。

这还不是 distinct-prime theorem：原 coefficient-singular common prime本身可能同时整除 `H_V4^circ` 并支付该 parity。下一步若要真正加一枚新 prime，需要审计 singular prime在 `V_4^int` 中的 exponent parity，或证明它与 parent descendant common gcd的 relevant inert supplier不能复用。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-pure-h4-prefix"></a>

> 整合来源：`spontaneous-crt-pure-h4-prefix.md`

# A2 coefficient-singular `H_4` 产生两张新的 irreducible pure-prefix curves

> **依赖：** `spontaneous-crt-pure-coefficient-singular.md`、`spontaneous-sphere-roots.md`、`spontaneous-prefix-branch-audit.md`。
>
> **严格状态：**coefficient-singular branch `A_63=B_63=0` 的低次 projective gate为 quartic `h_4(u)=0`, `u=z/s`。本文把两张 explicit sphere ratio `u_i=z_i/(9+y)` 代入，清分母后得到两张只含 `(x,y)` 的 primitive curves。它们分别 degree 32/40，在 `Q[x,y]` 中均不可约，并且与所有主要旧 prefix collision gates `A_sp,A_+,A_-,Delta_0,225x^2-y,C_*` 两两互素。因此 `h_4` singularity不是旧 source/common-alpha/central/prefix-defect shadow，而是一条 genuinely new pure-prefix bad locus。本文不排除其 finite-field roots，因此不关闭 A2。

---

## 1. projective quartic

前一文件得到

\[
\boxed{
\begin{aligned}
h_4(u)={}&
-29520930816u^4
-46902675456u^3\\
&+90353275489u^2
+114775877404u\\
&+31476144004.
\end{aligned}}
\tag{1.1}

coefficient-singular branch若进入低次 component，必须

\[
\boxed{h_4(z/s)=0,}
\qquad
s=9+y.
\tag{1.2}

两张 sphere roots为

\[
\boxed{
z_1=-\frac{A_+A_{sp}}
{400x^2y^3(x+2)^2},}
\tag{1.3}

\[
\boxed{
z_2=\frac{A_{sp}G_*}
{400x^2y^3(x+2)^2\Delta_0}.}
\tag{1.4}

所有 denominator在 genuine pure-spontaneous sector中为 units。

---

## 2. branch-specific primitive numerators

定义

\[
\boxed{
\mathscr S_{4,i}(x,y)
:=\operatorname{primnum}
 h_4\!\left(\frac{z_i(x,y)}{9+y}\right),
\qquad i=1,2.}
\tag{2.1}

exact expansion给：

\[
\boxed{
\deg\mathscr S_{4,1}=32,
\qquad
\#\operatorname{supp}(\mathscr S_{4,1})=137,}
\tag{2.2}

\[
\boxed{
\deg\mathscr S_{4,2}=40,
\qquad
\#\operatorname{supp}(\mathscr S_{4,2})=272.}
\tag{2.3}

两者 integer content均为 `1`，所以已经 primitive。

完整 coefficients由 checker从 (1.1),(1.3),(1.4) 重建；正文不手抄数百项。

---

## 3. both prefix curves are irreducible over `Q`

对两张 primitive numerator做 exact multivariate factorization：

\[
\boxed{
\mathscr S_{4,1}\text{ 在 }\mathbf Q[x,y]\text{ 中不可约},}
\tag{3.1}

\[
\boxed{
\mathscr S_{4,2}\text{ 在 }\mathbf Q[x,y]\text{ 中不可约}.}
\tag{3.2}

因此低次 ratio singularity没有继续分裂成一堆旧小 gate；每张 sphere orientation只产生一张真正的 irreducible prefix curve。

这不表示它们在有限域中无根；这里只是结构独立性结论。

---

## 4. gcd audit against all principal old prefix gates

沿用旧 objects：

\[
d=225x^2-y,
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
以及 branch-collision central kernel

\[
\begin{aligned}
C_*={}&164025x^4+656100x^3
+2381x^2y^2+41400x^2y\\
&+842400x^2+324xy^2+324y^2.
\end{aligned}
\]

对每个

\[
F\in\{d,A_{sp},A_-,A_+,\Delta_0,C_*\}
\]
exact polynomial gcd均给

\[
\boxed{
\gcd(\mathscr S_{4,1},F)
=\gcd(\mathscr S_{4,2},F)=1.}
\tag{4.1}

所以 `H_4` singular curves不是以下任何旧 mechanism 的 component：

- source line `d=0`；
- spontaneous coefficient degeneration `A_sp=0`；
- common-alpha branch `A_-=0`；
- sphere numerator factor `A_+=0`；
- prefix norm defect `Delta_0=0`；
- central branch collision `C_*=0`。

---

## 5. source-line restriction as an independent sanity audit

虽然 genuine branch已排除 source line，仍可把

\[
y=225x^2
\]
作为 independence sanity check。

此时两张 sphere roots合并为

\[
z_1=z_2
=\frac{9x^2(99x-4)^2}{16(x+2)^2}.
\]

将 full pure-prefix descendant resultant限制到该 line，并 primitive factor，可见一个显式 factor

\[
\boxed{(25x^2+1)^5.}
\tag{5.1}

对 inert prime `p=3 mod4`，`25x^2+1=0` 会强迫 `-1` 为平方，因此该 factor本身无 genuine inert root。

剩余还有一个 degree-8 与一个 degree-30 factor，所以 full descendant prefix carrier并不在 source line上恒等消失。这再次确认新 compatibility不是旧 source equation的重写。

本文不把 source-line剩余 factors计入 genuine branch obstruction，因为该 line本来已经由 prime-source separation排除。

---

## 6. revised coefficient-singular frontier

coefficient singularity现在严格分成：

1. low ratio component `h_4=0`：两张新 irreducible prefix curves `S_{4,1},S_{4,2}`；
2. high ratio component `h_24=0`：尚未做 branch-specific factorization。

所以 generic decimal-phase recovery失败的低次部分已经完全转化为两个 independent pure-prefix bad loci；它不会回流到任何已知 boundary/collision gate。

下一步若继续 singular side，应对 `h_24` 做同样 gcd/factor audit；若继续 generic side，则应使用 `X_{63,i}^{pref}` 的 natural representative/prime-product budget。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-pure-h4-projective-center"></a>

> 整合来源：`spontaneous-crt-pure-h4-projective-center.md`

# A2 `H_4` coefficient-singular component 的 fixed projective norm center

> **依赖：** `spontaneous-crt-pure-coefficient-singular.md`、`spontaneous-crt-pure-h4-prefix.md`、`spontaneous-single-branch.md`。
>
> **严格状态：**低次 coefficient-singular component满足 `h_4(u)=0`, `u=z/s`。本文继续把 `A_63=B_63=0` projectivize，令 `v=c/s^2`。关于 `v` 的 subresultant在 quotient ring modulo `h_4` 中精确退化成 `C_4(u)(1296v-3097)`。因此除一个固定 coefficient-exception resultant外，所有 `H_4` singular roots都强迫同一个 projective norm ratio `v=3097/1296 mod p`。真实 endpoint却有 `0<v<21/20`，所以该 singular component与真实 norm ratio存在统一 Archimedean gap，只能通过 p-adic wrapping实现。本文保留固定 coefficient exceptions，不关闭 A2。

---

## 1. projectivize the coefficient equations

coefficient-singular branch为

\[
A_{63}(s,z,c)=0,
\qquad
B_{63}(s,z,c)=0.
\]

两式是 weighted homogeneous，其中

\[
\deg s=\deg z=1,
\qquad
\deg c=2.
\]

在 genuine branch中 `s` 为 unit，所以定义

\[
\boxed{u:=z/s,}
\qquad
\boxed{v:=c/s^2.}
\tag{1.1}

除去 `s^7,s^8`，得到

\[
a(u,v)=0,
\qquad
b(u,v)=0,
\]
其中

\[
\deg_v a=3,
\qquad
\deg_v b=4.
\]

低次 resultant component为

\[
\boxed{h_4(u)=0,}
\tag{1.2}

其中 `h_4` 为前一文件的 irreducible quartic。

---

## 2. the final `v`-subresultant is linear

对 `a,b` 关于 `v` 取 subresultant sequence。最后一个非零的正次数 subresultant次数恰为 `1`：

\[
S_1(u,v)=A_1(u)v+B_1(u).
\]

现在在 quotient

\[
\mathbf Q[u]/(h_4)
\]
中把两个 coefficient降到 degree `<4`。exact computation给

\[
\boxed{
1296B_1(u)+3097A_1(u)
\equiv0\pmod{h_4(u)}.}
\tag{2.1}

而 `A_1 mod h_4` 是一个 nonzero fixed scalar乘一个 primitive cubic `C_4(u)`：

\[
\boxed{
A_1(u)\equiv\kappa\,C_4(u)\pmod{h_4},}
\qquad \kappa\in\mathbf Q^\times.
\tag{2.2}

`C_4` 的完整大整数 coefficients由 checker重建；这里只需要其次数

\[
\boxed{\deg C_4=3.}
\tag{2.3}

因此 modulo `h_4`：

\[
\boxed{
S_1(u,v)
\equiv
\frac{\kappa C_4(u)}{1296}
(1296v-3097).}
\tag{2.4}

---

## 3. fixed coefficient-exception integer

定义固定 nonzero integer

\[
\boxed{
\mathfrak E_4
:=\operatorname{Res}_u(h_4,C_4).}
\tag{3.1}

它是一个 315 位整数。其显式已知 small-prime content为

\[
\boxed{
2^{84}3^{83}5^{13}7^{11}11^{12}13^{40}29^2}
\tag{3.2}

乘一个固定 171 位余因子。

本文不需要把该余因子完全分解；所有

\[
p\mid\mathfrak E_4
\]
只是**有限 coefficient exceptions**，应按 fixed-prime audit处理，而不是混进 generic moving branch。

若

\[
p\nmid2\cdot3\cdot\mathfrak E_4
\]
且 `h_4(u)=0`，则 `C_4(u)` 为 unit。由 `A=B=0` 与 (2.4)：

\[
\boxed{
1296v-3097\equiv0\pmod p.}
\tag{3.3}

所以 generic low singular component具有 universal projective center

\[
\boxed{
\frac{c}{s^2}
\equiv\frac{3097}{1296}\pmod p.}
\tag{3.4}

---

## 4. the real endpoint ratio is below `21/20`

真实 ratio为

\[
\boxed{
 v_{real}
=
\frac{(x+2)^2(2025x^2+y^2)}
{100x^2(9+y)^2}.}
\tag{4.1}

endpoint box：

\[
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1.
\]

粗但严格地：

\[
(x+2)^2<\left(\frac{40}{19}\right)^2,
\]

\[
2025x^2+y^2
<2025\left(\frac2{19}\right)^2+1
=\frac{8461}{361},
\]

\[
100x^2>1,
\qquad
(9+y)^2>\left(\frac{2499}{250}\right)^2.
\]

因此

\[
\boxed{
0<v_{real}
<\frac{846100000000}{813854775321}
<\frac{21}{20}.}
\tag{4.2}

另一方面

\[
\boxed{
\frac{3097}{1296}>\frac{119}{50}>2.38.}
\tag{4.3}

所以 generic `H_4` projective center与真实 endpoint严格分离：

\[
\boxed{
\frac{3097}{1296}-v_{real}
>\frac{119}{50}-\frac{21}{20}
=\frac{133}{100}.}
\tag{4.4}

至少有 `1.33` 的固定实数 gap。

---

## 5. interpretation

除 fixed coefficient exceptions `p|E_4` 外，`H_4` coefficient singularity不再是一条任意 ratio curve：

\[
\boxed{
 h_4(u)=0,
\qquad
 v=3097/1296.}
\tag{5.1}

因此它同时固定 third/prefix projective direction和 prefix norm projective scale。

真实 endpoint中 `v<1.05`，而 modular center是 `>2.38`。故任何 surviving generic root必须依赖真正的 p-adic wrapping；没有 real-near singular degeneration。

这仍不是 global contradiction，因为 congruence不要求实数接近。下一步若要关闭 `H_4` branch，应把 fixed gap (4.4) 与清分母 natural numerator的 required p-depth联立，或逐个审计 `E_4` 的 finite coefficient primes。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-pure-h4-short-carrier"></a>

> 整合来源：`spontaneous-crt-pure-h4-short-carrier.md`

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

---

<a id="source-spontaneous-crt-pure-prefix-elimination"></a>

> 整合来源：`spontaneous-crt-pure-prefix-elimination.md`

# A2 pure-spontaneous / descendant common kernel 的最终 pure-prefix elimination

> **依赖：** `spontaneous-single-branch.md`、`spontaneous-sphere-roots.md`、`spontaneous-crt-universal-descendant-cubic.md`。
>
> **严格状态：**generic pure-spontaneous common prime已选定唯一 sphere branch `z_i(x,y)`，并满足 compact quadratic `L_i(tau)=0`。本文把 universal descendant cubic `E_63(K,zeta)=0` 代入 `K=s/tau,zeta=z_i/tau`，乘 `tau^8` 后对 `L_i` 做 exact Euclidean division。degree-8 compatibility modulo branch quadratic只剩一次 remainder `A_63 tau+B_63`；因此 generic coefficient branch中 decimal phase `tau=10^{-M}` 被唯一恢复。继续取 resultant可完全消去 `tau`，得到 degree-16 universal carrier `X_63(s,z,c)`；代入 `z_i(x,y),c(x,y)` 后成为只含 `(x,y)` 的 pure-prefix necessary condition。至此 third numerator、finite defect、prefix norm ratio和 decimal phase均已从 descendant common kernel消去。本文尚未证明 branch-specific pure-prefix carrier无有限域根，因此不关闭 A2。

---

## 1. compact branch quadratic

记

\[
s:=9+y,
\]

以及任一已选 sphere orientation

\[
z:=z_i(x,y),
\qquad i\in\{1,2\}.
\]

再定义

\[
\boxed{
c:=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.}
\tag{1.1}

`spontaneous-single-branch.md` 已证明 generic branch equation就是

\[
\boxed{
L_z(\tau)
:=55\tau^2+18(z-s)\tau+s^2-4sz-c=0.}
\tag{1.2}

这里

\[
\tau=10^{-M},
\qquad
K=s/\tau,
\qquad
\zeta=z/\tau.
\tag{1.3}

所有 sphere-root denominator在 genuine pure-spontaneous channel中均为 unit。

---

## 2. substitute the universal descendant cubic

前一文件构造 universal cubic

\[
\mathcal E_{63}(K,\zeta).
\]

定义

\[
\boxed{
\widetilde E_{63}(\tau;s,z)
:=\tau^8
\mathcal E_{63}(s/\tau,z/\tau).}
\tag{2.1}

因为 `E_63` 对 `K` 总次数最多 `8`，对 `zeta` 次数 `3`，(2.1) 是 genuine integer polynomial in `tau,s,z`，且

\[
\boxed{\deg_\tau \widetilde E_{63}=8.}
\tag{2.2}

现在在 polynomial ring

\[
\mathbf Z[s,z,c][\tau]
\]
中对 monic-up-to-unit quadratic `L_z` 做 Euclidean reduction。为避免除 `55` 引入无关 rational content，允许先在 `Q[s,z,c][tau]` 取余再清 primitive denominator。

exact computation给

\[
\boxed{
\widetilde E_{63}
\equiv
A_{63}(s,z,c)\tau+B_{63}(s,z,c)
\pmod{L_z}.}
\tag{2.3}

primitive normalization可选到

\[
\boxed{
\deg A_{63}=7,
\qquad A_{63}\text{ 有 }20\text{ 个 nonzero terms},}
\tag{2.4}

\[
\boxed{
\deg B_{63}=8,
\qquad B_{63}\text{ 有 }24\text{ 个 nonzero terms}.}
\tag{2.5}

完整 coefficients由 checker从 `E_63,L_z` 直接重建；正文不手抄机械大整数。

---

## 3. generic descendant branch uniquely recovers the decimal phase

若 genuine pure-spontaneous prime同时满足 branch equation与 descendant compatibility：

\[
L_z(\tau)\equiv0,
\qquad
\widetilde E_{63}(\tau;s,z)\equiv0
\pmod p,
\]
则由 (2.3)：

\[
\boxed{
A_{63}\tau+B_{63}\equiv0\pmod p.}
\tag{3.1}

若

\[
A_{63}\not\equiv0\pmod p,
\]
则 decimal phase不再是 free Hensel coordinate：

\[
\boxed{
\tau\equiv-B_{63}A_{63}^{-1}\pmod p.}
\tag{3.2}

所以在 generic coefficient branch中

\[
\boxed{
(x,y,i)
\Longrightarrow z_i
\Longrightarrow \tau
\Longrightarrow C/D}
\tag{3.3}

整个 first-layer local state已由 pure prefix branch唯一恢复。

若 `A_63=0`，common root还必须 `B_63=0`；这是新的 coefficient-singular subbranch，需单列，不能偷偷除去。

---

## 4. eliminate `tau` completely

对 quadratic (1.2) 与 linear remainder (3.1) 取 resultant。若写

\[
A:=A_{63},
\qquad B:=B_{63},
\]
则直接代 `tau=-B/A` 可得 universal formula

\[
\boxed{
\mathcal X_{63}(s,z,c)
:=55B^2
-18(z-s)AB
+(s^2-4sz-c)A^2.}
\tag{4.1}

任何 common root，无论 `A` 是否为零，都必须满足

\[
\boxed{\mathcal X_{63}\equiv0\pmod p.}
\tag{4.2}

exact coefficient audit给：未 primitive 化的 (4.1) 的全部 coefficient gcd恰为

\[
\boxed{5^7 11^7.}
\tag{4.3}

除去该固定 content后定义 primitive

\[
\boxed{
\mathcal X_{63}^{\rm prim}
:=\frac{\mathcal X_{63}}{5^7 11^7}.}
\tag{4.4}

它满足

\[
\boxed{
\deg\mathcal X_{63}^{\rm prim}=16,}
\tag{4.5}

并且 expanded support只有

\[
\boxed{59\text{ 个 nonzero monomials}.}
\tag{4.6}

当前 genuine pure-spontaneous prime已经排除 fixed coefficient primes `5,11`，所以 primitive normalization不丢任何 relevant root。

---

## 5. substitute the two rational sphere roots: pure prefix only

对每个 branch

\[
z=z_i(x,y),
\]
以及 (1.1) 的

\[
c=c(x,y),
\]
代入 (4.4)。清去 sphere-root denominator后定义 branch-specific primitive numerator

\[
\boxed{
\mathcal X_{63,i}^{\rm pref}(x,y)
:=
\operatorname{primnum}
\mathcal X_{63}^{\rm prim}
(s=9+y,z=z_i(x,y),c=c(x,y)).}
\tag{5.1}

于是 generic pure-spontaneous/descendant common prime必须满足

\[
\boxed{
\mathcal X_{63,i}^{\rm pref}(x,y)
\equiv0\pmod p}
\tag{5.2}

对它实际选择的唯一 branch `i`。

这是真正的 final local elimination：

\[
\boxed{
(a_3,b_3,C/D,\tau,Q^2N_0/B^2)
}
\]
全部不再出现在必要条件中，只剩

\[
\boxed{(x,y)\text{ 的 pure-prefix curve}.}
\tag{5.3}

---

## 6. relation to previous branch eliminants

旧 `Q_i(tau;x,y)=0` 单独允许一维 simple p-adic root family，因为 `tau` 仍是 decimal phase。

本文新增 `E_63=0` 后：

1. `E_63` modulo `Q_i/L_i` 只剩 linear remainder；
2. generic `tau` 被唯一恢复；
3. resultant `X_63` 进一步彻底消掉 `tau`。

因此 external descendant common kernel已从

\[
\text{single quadratic branch in }\tau
\]
下降成

\[
\boxed{\text{single pure-prefix algebraic curve in }(x,y).}
\]

这与旧 two-branch resultant `A_- C_*` 不同：本文没有让 `Q_1,Q_2` 同时消失，而是在**每个 branch内部**加入 descendant compatibility并消去 decimal phase。

---

## 7. proof boundary and next target

本文是结构性降维，不声称 degree-16 prefix carrier没有 finite-field roots。

下一步应分别对

\[
\mathcal X_{63,1}^{pref},
\qquad
\mathcal X_{63,2}^{pref}
\]
做：

- source line `d=225x^2-y` resultant；
- prefix norm defect `Delta_0` resultant；
- external discriminant `E_W` resultant；
- 或与 decimal relation `x=B/N,y=10A/N` 的 natural representative高度联立。

尤其应先检查 branch-specific numerator是否因回旧 `A_-`, `C_*`, `A_sp`；若只是旧 collision kernel，应明确降级。若出现新的 primitive factor，则它就是当前 alpha-free external common parity最直接的 pure-prefix obstruction。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-pure-projective-carrier"></a>

> 整合来源：`spontaneous-crt-pure-projective-carrier.md`

# A2 generic pure-spontaneous descendant kernel 的 dimensionless projective carrier

> **依赖：** `spontaneous-crt-pure-prefix-elimination.md`、`spontaneous-sphere-roots.md`、`spontaneous-crt-universal-descendant-cubic.md`。
>
> **严格状态：**此前 generic branch用 `(s,z,c,tau)` 表示，并在 branch quadratic上把 descendant compatibility降成 `A_63 tau+B_63`，最终得到 degree-16 pure-prefix carrier。本文进一步除去无意义的 overall scale：令 `r=tau/s=1/K`、`u=z/s=a_3/(TK)`、`v=c/s^2=Q^2N_0/(B^2K^2)`，则 branch quadratic与 universal descendant cubic都变成完全 dimensionless 的 `(r,u,v)` 系统。消去 `r` 得到 primitive irreducible total-degree-11 projective carrier `X_63^proj(u,v)`，只有59项。对第一张 sphere orientation，exact rational Bernstein certificate证明真实 endpoint映入 `-0.93<u<-0.54`、`0.937<v<0.939`，而 `X_63^proj` 在整个该 rectangle严格为负。因此 branch 1 的最终 descendant compatibility在实 endpoint上完全无根；任何 surviving congruence只能来自 p-adic wrapping。本文不排除 modular roots，也不证明 branch 2 的 real emptiness，因此不关闭 A2。

---

## 1. remove the scale `s`

沿用

\[
s=9+y,
\qquad z=z_i(x,y),
\qquad c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2},
\qquad \tau=10^{-M}.
\]

定义 dimensionless variables

\[
\boxed{
r:=\frac{\tau}{s}=\frac1K,}
\tag{1.1}
\]

\[
\boxed{
u:=\frac zs=\frac{a_3}{TK},}
\tag{1.2}
\]

\[
\boxed{
v:=\frac c{s^2}
=\frac{Q^2N_0}{B^2K^2}.}
\tag{1.3}
\]

最后一个 exact identity已在 `H_24` projective文件中证明。

---

## 2. branch quadratic becomes universal

原 compact branch equation为

\[
55\tau^2+18(z-s)\tau+s^2-4sz-c=0.
\]

除以 `s^2`，得到

\[
\boxed{
\mathscr L_{\rm proj}(r;u,v)
:=55r^2+18(u-1)r+1-4u-v=0.}
\tag{2.1}

这里没有任何 `M,N,s`。

universal descendant cubic同样只依赖

\[
K=1/r,
\qquad
\zeta=u/r.
\]

定义

\[
\boxed{
\mathscr E_{\rm proj}(r,u)
:=r^8\mathcal E_{63}(1/r,u/r).}
\tag{2.2}

它是 degree-8 polynomial in `r`。

所以 generic descendant common condition本质上就是

\[
\boxed{
\mathscr L_{\rm proj}=0,
\qquad
\mathscr E_{\rm proj}=0.}
\tag{2.3}

---

## 3. eliminate `r`: a compact projective carrier

对 (2.1),(2.2) 关于 `r` 取 resultant。全部 coefficient gcd恰为

\[
\boxed{5^7 11^7.}
\tag{3.1}

除去该 fixed content并取 primitive normalization，定义

\[
\boxed{
\mathscr X_{63}^{\rm proj}(u,v)
:=\operatorname{pp}
\operatorname{Res}_r
(\mathscr L_{\rm proj},\mathscr E_{\rm proj}).}
\tag{3.2}

exact audit给

\[
\boxed{
\deg_{\rm total}\mathscr X_{63}^{\rm proj}=11,}
\tag{3.3}
\]

\[
\boxed{
\deg_u\mathscr X_{63}^{\rm proj}
=\deg_v\mathscr X_{63}^{\rm proj}=8,}
\tag{3.4}
\]

\[
\boxed{
\#\operatorname{supp}(\mathscr X_{63}^{\rm proj})=59,}
\tag{3.5}

并且

\[
\boxed{
\mathscr X_{63}^{\rm proj}\text{ 在 }\mathbf Q[u,v]\text{ 中不可约}.}
\tag{3.6}

这就是 degree-16 branch-specific prefix carrier背后的 scale-free核心。

任何 genuine generic pure-spontaneous descendant common prime，除固定 `5,11` 外，都必须满足

\[
\boxed{
\mathscr X_{63}^{\rm proj}(u_i,v)\equiv0\pmod p.}
\tag{3.7}

---

## 4. exact real window for `v`

由

\[
v(x,y)
=\frac{(x+2)^2(2025x^2+y^2)}{100x^2(9+y)^2},
\]
直接求导：

\[
\boxed{
\frac{\partial v}{\partial x}
=\frac{(x+2)(2025x^3-2y^2)}{50x^3(y+9)^2}>0,}
\tag{4.1}
\]
因为

\[
2025x^3-2y^2
>\frac{2025}{1000}-2
=\frac1{40}.
\]

另有

\[
\boxed{
\frac{\partial v}{\partial y}
=-\frac{9(x+2)^2(225x^2-y)}{50x^2(y+9)^3}<0,}
\tag{4.2}
\]
因为 endpoint上

\[
225x^2-y>\frac94-1=\frac54.
\]

所以真实 box

\[
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1
\]
给精确 extremal values

\[
\boxed{
\frac{7497}{8000}
<v
<\frac{234947716}{250493929}.}
\tag{4.3}

特别地

\[
\boxed{
\frac{937}{1000}<v<\frac{939}{1000},}
\tag{4.4}

因为左差恰为 `1/8000`，而

\[
\frac{939}{1000}
-\frac{234947716}{250493929}
=\frac{266083331}{250493929000}>0.
\]

---

## 5. branch 1 maps into a fixed rational `u` interval

第一张 sphere root为

\[
\boxed{
 z_1
=-\frac{A_+A_{sp}}
{400x^2y^3(x+2)^2},}
\tag{5.1}

所以

\[
 u_1
=-\frac{A_+A_{sp}}
{400x^2y^3(x+2)^2(9+y)}.
\tag{5.2}

记正 denominator

\[
D_1:=400x^2y^3(x+2)^2(9+y),
\]

\[
N_1:=A_+A_{sp}>0.
\]

要证明

\[
-\frac{93}{100}<u_1< -\frac{27}{50},
\]
等价于

\[
93D_1-100N_1>0,
\tag{5.3}
\]

\[
50N_1-27D_1>0.
\tag{5.4}

checker把 `(x,y)` box仿射搬到 `[0,1]^2`，对两个 polynomial使用 exact rational Bernstein basis。全部 Bernstein coefficients严格为正；其中最小系数分别为

\[
\boxed{
\frac{1041285803156808768}{6634204312890625}>0,}
\tag{5.5}

\[
\boxed{
\frac{73}{25}>0.}
\tag{5.6}

因此

\[
\boxed{
-\frac{93}{100}<u_1< -\frac{27}{50}.}
\tag{5.7}

---

## 6. exact Bernstein exclusion for branch 1

定义 rational rectangle

\[
\boxed{
\mathcal R_1
=
\left[-\frac{93}{100},-\frac{27}{50}\right]
\times
\left[\frac{937}{1000},\frac{939}{1000}\right].}
\tag{6.1}

由 (4.4),(5.7)，真实 branch-1 image严格位于其内部。

将 `X_63^proj(u,v)` 仿射搬到 unit square，并转成 bidegree `(8,8)` Bernstein basis。checker逐一验证全部

\[
9\times9=81
\]
个 exact rational Bernstein coefficients都严格为负。

其中最大的 coefficient仍为

\[
\boxed{
-\frac{77096177819298948415154163591507164734582999}
{7450580596923828125}<0.}
\tag{6.2}

因此 Bernstein convex-hull property给

\[
\boxed{
\mathscr X_{63}^{\rm proj}(u,v)<0
\qquad((u,v)\in\mathcal R_1).}
\tag{6.3}

于是整个真实 endpoint上

\[
\boxed{
\mathscr X_{63}^{\rm proj}(u_1,v)<0.}
\tag{6.4}

特别地 branch 1 没有任何 real descendant-compatible point。

---

## 7. interpretation

(6.4) 不是 modular empty theorem：prime divisibility只要求

\[
\mathscr X_{63}^{\rm proj}(u_1,v)\equiv0\pmod p,
\]
仍可通过 p-adic wrapping实现。

但它比此前“sphere modular root在负侧、真实 third digit为正”的中间 sign gap更接近最终对象：这里被证明严格离开 real zero的已经是**最终 universal descendant projective carrier本身**。

因此 branch 1 后续若继续，应直接把这个固定负 natural representative与所需 prime-power depth联立，而不应再做 local discriminant stacking。

本文没有对 branch 2 给出同样结论；其 projective carrier在粗 real box上确实可能改变符号，因此 branch 2需另行处理。

---

## 8. updated generic frontier

现在 generic pure-spontaneous descendant-only external sector有统一 compact reader

\[
\mathscr X_{63}^{\rm proj}(u,v).
\]

- branch 1：真实 endpoint上严格负，只有 p-adic wrapping；
- branch 2：仍需独立 global audit；
- coefficient singular `H_4/H_24` 已分别有 short/compact parity carriers。

所以最直接的下一步是给 branch 1 的 negative projective value做 integer clearing与 2-adic/depth budget，同时单独定位 branch 2 的 real zero locus。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-q-descent-separation"></a>

> 整合来源：`spontaneous-crt-q-descent-separation.md`

# A2 q-denominator inert carrier 与 descendant common support 完全分离

> **依赖：** `spontaneous-denominator-depth-matrix.md`、`endpoint-lattice.md` §§16.71–16.73、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descent-overlap-nogo.md`。
>
> **严格状态：**完整 q-saturation 中，additive denominator carrier由 `K^2-26` 读取，third-block saturation给 `2a_3+9T=0`，而 canonical square-side allocation对每个 q-prime无条件给 `N=DK`。本文把这三条 first-layer关系代入 descended common equation `F63^(16)`；它塌成 `-K(31K+144)`。与 `K^2-26` 的 resultant只有 `2,5,17`，其中唯一 odd non-5 prime `17` 为 `1 mod4`。因此整个 genuine non-3 inert q-denominator carrier与 `Rstar_63/Dhat_63` common support完全不相交，包括旧 fixed `11,23` special branches。本文是 complete support separation lemma，不关闭 A2。

---

## 1. q-denominator carrier data

固定 genuine non-`3` inert prime `p` 属于 saturated q-denominator additive carrier。于是存在

\[
p^e\Vert q,
\qquad
p^e\mid\mathscr L_{23},
\qquad e\ge1.
\]

其中

\[
\mathscr L_{23}=\frac{9T}{2}+a_3.
\]

所以 first layer有

\[
\boxed{2a_3+9T\equiv0\pmod p.}
\tag{1.1}

`spontaneous-denominator-depth-matrix.md` 给 additive q-side pure-prefix root

\[
\boxed{K^2-26\equiv0\pmod p.}
\tag{1.2}

另一方面 canonical square-side allocation在 `endpoint-lattice.md` (16.416) 对每个 q-prime、在进入 rational-root分支以前就已经给

\[
\boxed{N\equiv DK\pmod p.}
\tag{1.3}

这里

\[
N=3D-C.
\]

所有 genuine q-prime满足 `p∤D`，所以定义

\[
\delta:=C/D
\]
并由 (1.3)：

\[
\boxed{\delta\equiv3-K\pmod p.}
\tag{1.4}

该关系对 generic branch 与 fixed `11,23` 都成立；后两者只是 higher-depth budget不同，不改变 first-layer canonical allocation。

---

## 2. descendant common equation under q-saturation

若同一个 `p` 还进入 descendant common support，则

\[
p\mid\widehat{\mathscr D}_{63}
\]
并等价于

\[
p\mid F_{63}^{(16)},
\]
其中

\[
\boxed{
\begin{aligned}
F_{63}^{(16)}={}&
16(2K-9)
\{g((2K-12)T-2a_3)+5^\lambda C\}\\
&-63gTK^2.
\end{aligned}}
\tag{2.1}

对 q-prime有

\[
\gcd(p,2\cdot5\cdot gT)=1.
\]

使用

\[
gT=D5^\lambda
\]
把 (2.1) 除以 unit `gT`。由 (1.1)：

\[
\frac{F_{63}^{(16)}}{gT}
\equiv
32\delta K-144\delta+K^2-384K+432
\pmod p.
\tag{2.2}

再代入 canonical allocation (1.4)：

\[
\boxed{
\frac{F_{63}^{(16)}}{gT}
\equiv-K(31K+144)
\pmod p.}
\tag{2.3}

---

## 3. q-root and descendant root have no inert common prime

由 (1.2)，对 genuine non-`2,13` prime有 `K` 为 unit。当前关注 non-3 inert prime，因此当然可消去 `K`。若 descendant common仍成立，(2.3) 强迫

\[
\boxed{31K+144\equiv0\pmod p.}
\tag{3.1}

与 q-root联立，直接 resultant：

\[
\boxed{
\operatorname{Res}_K(K^2-26,31K+144)
=-4250
=-2\cdot5^3\cdot17.}
\tag{3.2}

所以 odd non-5 common prime只可能是

\[
p=17.
\]

但

\[
17\equiv1\pmod4,
\]
并非 inert prime。因此

\[
\boxed{
\operatorname{Supp}_{\rm inert}^{\rm gen}(q\text{-denominator carrier})
\cap
\operatorname{Supp}(G_\Delta)
=\varnothing,}
\tag{3.3}

其中

\[
G_\Delta=\gcd(\mathscr R_{63}^\star,\widehat{\mathscr D}_{63}).
\]

---

## 4. fixed `11,23` require no separate exception

旧 q-carrier audit在 higher depth中保留 fixed `11,23`：

- `11`：middle/third 双因子预算；
- `23`：third branch 与 height depth同步。

但 (1.3) 是对所有 q-prime的 canonical first-layer statement，(1.1) 与 (1.2) 在 fixed branches同样成立。因此 §§2–3 已自动包含 `11,23`。

事实上二者均不整除 (3.2) 的 resultant：

\[
11,23\nmid4250.
\]

故

\[
\boxed{
11,23\notin\operatorname{Supp}(G_\Delta)
\quad\text{when they act as q-denominator carriers}.}
\tag{4.1}

这不禁止 `11,23` 通过其它已知 prime-source label出现；这里只关闭 q-denominator → descendant-common 的复用通道。

---

## 5. consequence for descendant common parity

`spontaneous-crt-descendant-common-parity.md` 把危险 `Z=1,G_Delta=3 mod4` 的 common parity来源分为 old-pool 与 external kernel。

本文删除 entire q-denominator old-pool contribution：

\[
\boxed{
\text{q-denominator inert parity cannot be the common descendant supplier}.}
\tag{5.1}

因此 common inert parity目前可来自：

1. fixed equal-depth target labels `31/179`；
2. source-common overlap（受 `18K-55` 与 `H_S63` 的 square-root-depth双收费）；
3. f-denominator channel（尚待下一步审计）；
4. genuine endpoint-external/spontaneous common kernel。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-quotient-endpoint-parameterization"></a>

> 整合来源：`spontaneous-crt-quotient-endpoint-parameterization.md`

# A2 additive CRT quotient 的 endpoint-lattice parameterization

> **依赖：** `spontaneous-crt-quotient-source-scale.md`、`endpoint-lattice.md`。
>
> **严格状态：**前一层把 `Q_Delta` 的全部无界尺度隔离为 `a_Delta=(c_u^2 5^lambda/g)K^2`。本文用真实第二/第三 denominator normal forms消去 `c_u/g`，把该尺度完全恢复成 endpoint-lattice 参数 `(M,m,lambda,d,c_Q)` 与窄 normalized variables `(x,s,w)`。其连续 coefficient严格落在 `(139,150)`，所以 `Q_Delta` 获得固定 normalized window。对固定 `(eta,d,c_Q)`，绝对 `Q_Delta` 仍指数增长，因此“证明 Q_Delta=O(1)”路线严格降级；正确后续接口是比较 normalized quotient 与 Gaussian/source Hensel 的离散 slot。本文不建立该最终比较，因此不关闭 A2。

---

## 1. normalized decimal variables

记

\[
x:=\frac{B}{N},
\qquad
s:=\frac{K}{N},
\qquad
w:=\frac{b_3}{T},
\qquad
N=10^M.
\]

当前 dangerous endpoint box给

\[
\boxed{
\frac1{10}<x<\frac2{19},
\qquad
\frac{2499}{250}<s<10,
\qquad
\frac{837}{1000}<w<\frac{843}{1000}.}
\tag{1.1}
\]

前一文件定义

\[
\boxed{
\mathfrak a_\Delta
:=\frac{c_u^25^\lambda}{g}K^2.}
\tag{1.2}
\]

并证明

\[
\boxed{
\frac{\mathfrak a_\Delta}{17}-1
<Q_\Delta
<\frac{\mathfrak a_\Delta}{14}.}
\tag{1.3}
\]

---

## 2. recover `c_u` from the third denominator

第三块 denominator normal form为

\[
\boxed{
b_3=2^{M+m+1}5^dc_Qc_u.}
\tag{2.1}
\]

又

\[
b_3=wT,
\qquad
T=2^m5^m,
\qquad
m=d+\lambda.
\]

所以

\[
w2^m5^m
=2^{M+m+1}5^dc_Qc_u.
\]

约去 `2^m5^d`：

\[
\boxed{
c_u
=\frac{w5^\lambda}{2^{M+1}c_Q}.}
\tag{2.2}
\]

---

## 3. recover `g` from the second denominator

第二块 denominator normal form为

\[
\boxed{B=2^{M+m+1}c_ug.}
\tag{3.1}
\]

另一方面

\[
B=xN=x2^M5^M.
\]

代入 (2.2)：

\[
\begin{aligned}
g
&=\frac{x2^M5^M}
{2^{M+m+1}c_u}\\
&=\frac{x2^M5^M c_Q}
{2^m w5^\lambda}.
\end{aligned}
\]

因此

\[
\boxed{
g
=\frac{x c_Q}{w}
2^{M-m}5^{M-\lambda}.}
\tag{3.2}
\]

所以 `c_u/g` 不再是一个额外 allocation parameter；它由真实 endpoint variables完全恢复。

---

## 4. exact endpoint formula for `a_Delta`

将 (2.2),(3.2) 代入 (1.2)，并使用

\[
K=sN=s2^M5^M.
\]

直接整理 `2,5` exponents：

\[
\boxed{
\mathfrak a_\Delta
=
\frac{s^2w^3}{4xc_Q^3}
2^{m-M}5^{4\lambda+M}.}
\tag{4.1}
\]

现在令 endpoint-lattice 的离散参数

\[
\boxed{\eta:=2m-M.}
\tag{4.2}
\]

因为

\[
m=\frac{M+\eta}{2},
\qquad
\lambda=m-d,
\]
所以

\[
m-M=\frac{\eta-M}{2},
\]

\[
4\lambda+M
=3M+2\eta-4d.
\]

故 (4.1) 等价为

\[
\boxed{
\mathfrak a_\Delta
=
\frac{s^2w^3}{4xc_Q^3}
2^{(\eta-M)/2}
5^{3M+2\eta-4d}.}
\tag{4.3}
\]

这已经把 CRT quotient主尺度完全接回原 Gaussian allocation lattice。

---

## 5. the continuous coefficient lies in `(139,150)`

定义

\[
\boxed{
\kappa_\Delta:=\frac{s^2w^3}{4x}.}
\tag{5.1}
\]

由 (1.1)，下界取 `s,w` 的下端与 `x` 的上端：

\[
\kappa_\Delta
>
\frac{(2499/250)^2(837/1000)^3}
{4(2/19)}
>139.
\tag{5.2}
\]

上界取 `s,w` 的上端与 `x` 的下端：

\[
\kappa_\Delta
<
\frac{10^2(843/1000)^3}
{4(1/10)}
<150.
\tag{5.3}
\]

所以

\[
\boxed{139<\kappa_\Delta<150.}
\tag{5.4}
\]

定义纯离散 scale

\[
\boxed{
\mathcal R_{\eta,d,M}
:=2^{(\eta-M)/2}5^{3M+2\eta-4d}
=2^{m-M}5^{4\lambda+M}.}
\tag{5.5}
\]

于是

\[
\boxed{
\frac{139}{c_Q^3}\mathcal R_{\eta,d,M}
<\mathfrak a_\Delta
<\frac{150}{c_Q^3}\mathcal R_{\eta,d,M}.}
\tag{5.6}
\]

---

## 6. fixed normalized window for `Q_Delta`

把 (5.6) 代入前层 (1.3)：

\[
Q_\Delta
>
\frac{139}{17c_Q^3}\mathcal R_{\eta,d,M}-1
>
\frac8{c_Q^3}\mathcal R_{\eta,d,M}-1,
\]

以及

\[
Q_\Delta
<
\frac{150}{14c_Q^3}\mathcal R_{\eta,d,M}
<
\frac{11}{c_Q^3}\mathcal R_{\eta,d,M}.
\]

所以

\[
\boxed{
\frac8{c_Q^3}\mathcal R_{\eta,d,M}-1
<Q_\Delta
<\frac{11}{c_Q^3}\mathcal R_{\eta,d,M}.}
\tag{6.1}
\]

换言之，normalized CRT quotient

\[
\boxed{
\mathcal Q_\Delta^{\rm norm}
:=
\frac{c_Q^3Q_\Delta}
{2^{m-M}5^{4\lambda+M}}
}
\tag{6.2}
\]

被困在一个固定常数带；忽略 floor 的 `-1` correction后，它始终在 `(8,11)` 内。

严格地由 (6.1)：

\[
8-\frac{c_Q^3}{\mathcal R_{\eta,d,M}}
<\mathcal Q_\Delta^{\rm norm}
<11.
\tag{6.3}
\]

---

## 7. constant-quotient strategy is impossible

固定任意允许的

\[
(\eta,d,c_Q).
\]

则

\[
\mathcal R_{\eta,d,M}
=2^{\eta/2}5^{2\eta-4d}
\left(\frac{125}{\sqrt2}\right)^M.
\tag{7.1}
\]

在 parity-compatible `M` subsequence上这是严格指数增长。由 (6.1)：

\[
\boxed{Q_\Delta\to\infty}
\]

随 `M` 增长。

因此后续不应再尝试证明

\[
Q_\Delta=O(1)
\]
或把它直接压成固定有限整数表；那与 exact endpoint scale不相容。

真正可比较的对象是 normalized quotient (6.2)。

---

## 8. revised global interface

`endpoint-lattice.md` 中 Gaussian allocation也按

\[
(\eta,d,c_Q,k_h,\text{slot})
\]
组织。

本文说明 additive CRT quotient使用**完全相同的离散参数**，而连续 endpoint dependence只剩

\[
\kappa_\Delta\in(139,150).
\]

所以最自然的下一步不是单独估计 `Q_Delta`，而是把

\[
\boxed{
\mathcal Q_\Delta^{\rm norm}}
\]
与 Gaussian/source-Hensel 一侧已经存在的 normalized slot scalar联立，寻找两个固定窄区间或离散 residue之间的不相容。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-quotient-source-scale"></a>

> 整合来源：`spontaneous-crt-quotient-source-scale.md`

# A2 additive CRT quotient 的 exact source-scale normalization

> **依赖：** `endpoint-lattice.md` §§16.33–16.38、`source-discriminant.md`。
>
> **严格状态：**`endpoint-lattice.md` 已把三个 rational-root cofactor 的右 gap `Delta_+` 固定在模 `D^2-C^2` 的唯一 CRT 余类，但缺少商 `Q_Delta=floor(Delta_+/(D^2-C^2))` 的无界高度控制。本文首先把 §16.35 的 prefactor精确约成 `c_u^2 D`，再利用 source identities把 `S_+` 中唯一的 rational term完全整数化。最终 `D Delta_+` 成为显式 `(C,D,z,c_u,K,T,a_3)` 整数多项式；归一化后证明 `Q_Delta` 的尺度只剩 `c_u^2/g` 这一项 source allocation ratio。CRT、third-coordinate 与顶部 defect不再引入独立无界尺度。本文没有控制 `c_u^2/g`，所以不关闭 A2。

---

## 1. notation from the additive CRT core

沿用 dangerous reflection core：

\[
L:=2^m5^d,
\qquad
D=gL,
\qquad
T=10^m=L5^\lambda,
\]

\[
N_s:=3D-C,
\qquad
r:=\frac{N_s}{D}=3-\frac CD,
\]

以及

\[
0<\frac CD<\frac3{250}.
\tag{1.1}
\]

第三块写成

\[
\zeta:=\frac{a_3}{T},
\qquad
1<\zeta<\frac{251}{250}.
\tag{1.2}
\]

§16.35 定义

\[
\Delta_+
=\frac{A\mathscr S_+}
{2^{2M+2}5^{\nu_5}DL},
\qquad
A=b_2^2T,
\tag{1.3}
\]

其中

\[
\nu_5=\lambda-2d,
\]

以及

\[
\begin{aligned}
\mathscr S_+={}&
TK^2-4a_3K
-T^2\frac{f(r)}{h(r)}\\
&+(r+7)(2a_3-2KT)
+(r^2+7r+37)T,
\end{aligned}
\tag{1.4}
\]

\[
f(r)=r(Tr+2a_3)(K-r)^2,
\qquad
h(r)=(Tr+a_3)^2.
\tag{1.5}
\]

---

## 2. the huge prefactor collapses exactly to `c_u^2 D`

当前 denominator normal form为

\[
b_2=2^{M+m+1}c_ug.
\tag{2.1}
\]

因此 (1.3) 的 prefactor为

\[
\frac{b_2^2T}
{2^{2M+2}5^{\nu_5}DL}.
\]

使用 `D=gL`：

\[
\begin{aligned}
\frac{b_2^2T}
{2^{2M+2}5^{\nu_5}DL}
&=
\frac{2^{2M+2m+2}c_u^2g^2T}
{2^{2M+2}5^{\nu_5}gL^2}\\
&=
\frac{2^{2m}c_u^2gT}
{5^{\nu_5}L^2}.
\end{aligned}
\]

由于

\[
L=2^m5^d,
\qquad
\nu_5+2d=\lambda,
\qquad
T=L5^\lambda,
\]
得到

\[
\boxed{
\frac{b_2^2T}
{2^{2M+2}5^{\nu_5}DL}
=c_u^2D.}
\tag{2.2}
\]

所以右 gap具有极简 exact form：

\[
\boxed{\Delta_+=c_u^2D\mathscr S_+.}
\tag{2.3}
\]

这一步已经把原 cofactor / rational-root normalization 的所有巨大公共 scale约掉。

---

## 3. naturalize the only rational term

source identities给

\[
Tr+a_3=\frac{H_0}{g}
=\frac{c_uW_q}{g},
\tag{3.1}
\]

以及

\[
K-r
=K-\frac{N_s}{D}
=\frac{DK-N_s}{D}
=\frac{qW_q}{D}.
\tag{3.2}
\]

另有

\[
z=q5^\lambda,
\qquad
\frac{qgT}{D}=q5^\lambda=z.
\tag{3.3}
\]

把 (3.1)–(3.3) 代入 (1.5)：

\[
\boxed{
T^2\frac{f(r)}{h(r)}
=
\frac{
 z^2N_s(TN_s+2a_3D)
}{c_u^2D^2}.}
\tag{3.4}
\]

因此 (2.3) 中唯一的 rational source term也完全可乘回整数平面。

---

## 4. fully integral formula for `D Delta_+`

把 (3.4) 代入 (1.4)，并用 `r=N_s/D`，得到

\[
\boxed{
\begin{aligned}
D\Delta_+
={}&c_u^2\Bigl[
D^2(TK^2-14KT-4Ka_3+37T+14a_3)\\
&\qquad
+DN_s(-2KT+7T+2a_3)
+TN_s^2
\Bigr]\\
&-z^2N_s(TN_s+2a_3D).
\end{aligned}}
\tag{4.1}
\]

所有量均为原 endpoint/source integers；`f(r)/h(r)` 已消失。

再用 `N_s=3D-C`，(4.1) 等价于

\[
\boxed{
\begin{aligned}
D\Delta_+
={}&c_u^2\Bigl[
C^2T+2CDKT-13CDT-2CDa_3\\
&\qquad+D^2K^2T-20D^2KT-4D^2Ka_3
+67D^2T+20D^2a_3
\Bigr]\\
&+z^2\Bigl[
-C^2T+6CDT+2CDa_3
-9D^2T-6D^2a_3
\Bigr].
\end{aligned}}
\tag{4.2}
\]

所以 additive CRT quotient现在已有一个完全显式的 integer numerator。

---

## 5. normalized `S_+` is a quadratic in `K`

将

\[
r=3-C/D,
\qquad
\zeta=a_3/T
\]
代入 (1.4)，除以 `T`。精确得到

\[
\boxed{
\frac{\mathscr S_+}{T}
=
\frac{
\zeta^2K^2-2\mathcal L(r,\zeta)K+\mathcal C(r,\zeta)
}{(r+\zeta)^2},}
\tag{5.1}
\]

其中

\[
\boxed{
\begin{aligned}
\mathcal L(r,\zeta)={}&
2r^2\zeta+7r^2+5r\zeta^2+14r\zeta\\
&+2\zeta^3+7\zeta^2,
\end{aligned}}
\tag{5.2}
\]

\[
\boxed{
\begin{aligned}
\mathcal C(r,\zeta)={}&
2r^3\zeta+7r^3+5r^2\zeta^2+28r^2\zeta+37r^2\\
&+2r\zeta^3+35r\zeta^2+74r\zeta
+14\zeta^3+37\zeta^2.
\end{aligned}}
\tag{5.3}
\]

在 current box中 `L,C>0`。

首项 coefficient满足

\[
\boxed{
\frac1{16}
<\frac{\zeta^2}{(r+\zeta)^2}
<\frac4{63}.}
\tag{5.4}
\]

左端由 `r<3, zeta>1` 严格得到；右端可在 box端点直接验证。

---

## 6. fixed quadratic window for `S_+`

§16.35 已证明

\[
\frac{\mathscr S_+}{T}
>\frac{K^2}{16}-28K.
\]

由于

\[
K>9\cdot10^{11}>7616,
\]
有

\[
\boxed{
\frac{\mathscr S_+}{T}>rac{K^2}{17}.}
\tag{6.1}
\]

对上界，(5.1) 中 linear term严格为负；在

\[
2.988<r<3,
\qquad
1<\zeta<1.004
\]
内粗略有

\[
\frac{\mathcal C(r,\zeta)}{(r+\zeta)^2}<2500.
\]

结合 (5.4)：

\[
\frac{\mathscr S_+}{T}
<\frac4{63}K^2+2500.
\]

而 `K>9*10^11` 远强于 `K^2/315>2500`，故

\[
\boxed{
\frac{\mathscr S_+}{T}<\frac{K^2}{15}.}
\tag{6.2}
\]

综上：

\[
\boxed{
\frac{TK^2}{17}
<\mathscr S_+
<\frac{TK^2}{15}.}
\tag{6.3}
\]

---

## 7. `Q_Delta` has only one unbounded source scale

additive CRT modulus为

\[
M_\Delta:=D^2-C^2
=D^2\left(1-(C/D)^2\right).
\]

由 (2.3)：

\[
\boxed{
\frac{\Delta_+}{D^2-C^2}
=
\frac{c_u^2\mathscr S_+}
{D\left(1-(C/D)^2\right)}.}
\tag{7.1}
\]

定义唯一剩余的 source allocation scale

\[
\boxed{
\mathfrak a_\Delta
:=\frac{c_u^2TK^2}{D}
=\frac{c_u^25^\lambda}{g}K^2.}
\tag{7.2}
\]

因为 `0<C/D<3/250`，

\[
1<\frac1{1-(C/D)^2}<\frac{1001}{1000}.
\]

结合 (6.3)：

\[
\boxed{
\frac{\mathfrak a_\Delta}{17}
<
\frac{\Delta_+}{D^2-C^2}
<
\frac{\mathfrak a_\Delta}{14}.}
\tag{7.3}
\]

因此

\[
\boxed{
\frac{\mathfrak a_\Delta}{17}-1
< Q_\Delta
<\frac{\mathfrak a_\Delta}{14}.}
\tag{7.4}
\]

所以 `Q_Delta` 的无界性已被严格隔离到单一 scalar

\[
\boxed{c_u^2/g.}
\]

`C/D`、`a_3/T`、三 cofactor 与 CRT residue本身都只在固定窄区间内改变常数因子。

---

## 8. revised CRT frontier

此前 README 把下一缺口写成“控制无界 CRT 商 `Q_Delta`”。本文将其收紧为：

\[
\boxed{
\text{控制 source allocation ratio }c_u^2/g.}
\tag{8.1}
\]

一旦 `c_u^2/g` 在某个 allocation branch获得上下界，(7.3) 会立刻把 `Q_Delta` 压成对应的 finite / short interval；无需重新分析 cubic cofactor 或 CRT residue。

因此最值得与本文联立的是已经包含 `c_u,g` 的 Gaussian/source allocation equations，而不是继续对 `Delta_+` 做独立粗估计。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-source-descent-depth"></a>

> 整合来源：`spontaneous-crt-source-descent-depth.md`

# A2 source-common / height-descent overlap 的 square-root depth theorem

> **依赖：** `spontaneous-crt-source-descent-overlap.md`、`spontaneous-source-parity-common-gcd.md`、`spontaneous-crt-height-primitive-remainder.md`。
>
> **严格状态：**上一文件只对 source-common/descent-common 的 support radical给出双短-carrier约束。本文利用 `F63^(16)` 与 source collision sheet之间的 exact Bezout identity，把完整 common gcd 的一半深度也收费到同一两个短 carrier。若 `k_r` 是某 genuine prime在 source common gcd、`Rstar_63`、`Dhat_63` 三者中的共同深度，则 `r^{ceil(k_r/2)}` 同时整除 `18K-55` 与 `H_S63`。因此整个 common gcd满足 square-root-depth product bound，而不仅是 squarefree radical bound。本文不证明该 common gcd为空，因此不关闭 A2。

---

## 1. common-depth notation

沿用 source common gcd 的 genuine unit-separated部分

\[
G_S^{\rm gen}
=
\prod_{r\in E_S^{\rm gen}}r^{s_r},
\qquad
s_r:=v_r(G_S).
\tag{1.1}
\]

旧 source square-collision theorem 已证明

\[
\boxed{
v_r(18K-55)
\ge
\left\lceil\frac{s_r}{2}\right\rceil.}
\tag{1.2}
\]

现在同时考虑 fully primitive descended pair

\[
\mathscr R_{63}^\star,
\qquad
\widehat{\mathscr D}_{63}.
\]

对每个 genuine source-common prime定义三重 common depth

\[
\boxed{
k_r
:=
\min\!\left\{
 s_r,
 v_r(\mathscr R_{63}^\star),
 v_r(\widehat{\mathscr D}_{63})
\right\}.}
\tag{1.3}
\]

只有 `k_r>=1` 的 prime真正属于 source-common/descent-common overlap。

定义完整 common factor

\[
\boxed{
G_{SD}
:=
\prod_{r\in E_S^{\rm gen}}r^{k_r}.}
\tag{1.4}
\]

---

## 2. exact Bezout between descendant equation and source sheet

上一文件定义

\[
\boxed{
\mathscr H_{S63}
=102383gT-29952ga_3+14976C5^\lambda.}
\tag{2.1}
\]

以及 cleared descended equation

\[
\boxed{
\begin{aligned}
F_{63}^{(16)}={}&
16(2K-9)
\{g((2K-12)T-2a_3)+5^\lambda C\}\\
&-63gTK^2.
\end{aligned}}
\tag{2.2}
\]

resultant `Res_K(F63^(16),18K-55)=-H_S63` 事实上来自一个更强的 exact polynomial Bezout：

\[
\boxed{
324F_{63}^{(16)}+\mathscr H_{S63}
=(18K-55)\mathscr Q_{S63},}
\tag{2.3}
\]

其中

\[
\boxed{
\mathscr Q_{S63}
:=576C5^\lambda
+18KgT
-12041gT
-1152ga_3.}
\tag{2.4}
\]

直接展开即可验证。

---

## 3. each common prime pays half its depth into `H_S63`

固定 `r` 满足 `k_r>=1`。由定义

\[
v_r(\widehat{\mathscr D}_{63})\ge k_r.
\]

`Dhat_63` 与 `F63^(16)` 只差 genuine `r`-units / fixed powers of `2,c_u`，所以

\[
\boxed{v_r(F_{63}^{(16)})\ge k_r.}
\tag{3.1}
\]

另一方面由 (1.2)，并因 `s_r>=k_r`：

\[
\boxed{
v_r(18K-55)
\ge
\left\lceil\frac{s_r}{2}\right\rceil
\ge
\left\lceil\frac{k_r}{2}\right\rceil.}
\tag{3.2}
\]

令

\[
t_r:=\left\lceil\frac{k_r}{2}\right\rceil.
\]

在 Bezout (2.3) 中：

- `324F63^(16)` 至少有 `k_r>=t_r` 层；
- `(18K-55)Q_S63` 至少有 `t_r` 层。

所以二者之差 `H_S63` 也至少有 `t_r` 层：

\[
\boxed{
v_r(\mathscr H_{S63})
\ge
\left\lceil\frac{k_r}{2}\right\rceil.}
\tag{3.3}
\]

这把上一文件的 first-layer support statement升级为完整 square-root-depth收费。

---

## 4. global square-root-depth product divides both short carriers

定义

\[
\boxed{
H_{SD}
:=
\prod_{r\in E_S^{\rm gen}}
 r^{\lceil k_r/2\rceil}.}
\tag{4.1}
\]

逐 prime由 (3.2),(3.3)：

\[
\boxed{H_{SD}\mid18K-55,}
\tag{4.2}
\]

\[
\boxed{H_{SD}\mid\mathscr H_{S63}.}
\tag{4.3}
\]

而 endpoint bounds为

\[
0<18K-55<180N,
\]

\[
0<\mathscr H_{S63}
<\frac{9076339}{125}gT.
\]

因此

\[
\boxed{
H_{SD}
<
\min\!\left\{
180N,
\frac{9076339}{125}gT
\right\}.}
\tag{4.4}
\]

所以 source/descent common gcd的完整深度不能任意堆积在 descendant internal syzygy中；至少一半深度必须同时由两个独立尺度的短 natural representatives承担。

---

## 5. exact square-root bookkeeping identity

定义 common gcd 中 odd-exponent radical

\[
\boxed{
R_{SD}^{\rm odd}
:=
\prod_{\substack{r\in E_S^{\rm gen}\\k_r\text{ odd}}}r.}
\tag{5.1}
\]

逐 exponent 有

\[
2\left\lceil\frac{k_r}{2}\right\rceil
=
k_r+(k_r\bmod2).
\]

所以

\[
\boxed{
H_{SD}^2
=G_{SD}\,R_{SD}^{\rm odd}.}
\tag{5.2}
\]

结合 (4.4)：

\[
\boxed{
G_{SD}R_{SD}^{\rm odd}
<(180N)^2,}
\tag{5.3}
\]

并且同时有

\[
\boxed{
G_{SD}R_{SD}^{\rm odd}
<\left(\frac{9076339}{125}gT\right)^2.}
\tag{5.4}
\]

注意这不是说 `G_SD` 本身整除两个短 carrier；整除的是其 canonical square-root-depth lift `H_SD`。本文严格保留这一差别。

---

## 6. relation to target overlap

source-common genuine support与 entire equal-depth target support已经有 complete separation：

\[
\operatorname{Supp}_{\rm gen}(G_S)
\cap
\operatorname{Supp}_{\rm gen}(G_{\rm tar})
=\varnothing.
\tag{6.1}
\]

所以新 common factor `G_SD` 与此前 fixed target/descent common factor

\[
G_{TD}\mid31\cdot179
\]
在 genuine support上互素：

\[
\boxed{\gcd(G_{SD},G_{TD})=1.}
\tag{6.2}
\]

因此 target reuse 与 source-common reuse可在 global product/parity ledger中独立收费，不存在同一 genuine prime被两套 overlap账本重复计算的问题。

---

## 7. revised descendant-overlap frontier

当前 `Rstar_63/Dhat_63` common support的两大 old-source channels都已有 canonical计价：

1. target overlap：固定 squarefree
   \[
   G_{TD}\mid5549;
   \]
2. source-common overlap：完整 common depth通过
   \[
   H_{SD}^2=G_{SD}R_{SD}^{odd},
   \qquad
   H_{SD}\mid\gcd(18K-55,H_{S63})
   \]
   收费。

且两者 genuine support互素。

下一步若做 global parity，应把 `G_TD` 与 `G_SD` 从 descendant common gcd中分开，再审计仍未归属 target/source-common 的 residual common parity。若 residual common part为空，则在 `Z=1 mod4` 的 parity-doubling分支会真正迫使两枚不同 generic inert primes。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-source-descent-overlap"></a>

> 整合来源：`spontaneous-crt-source-descent-overlap.md`

# A2 source-common 与 height-descent common support 的短 carrier

> **依赖：** `spontaneous-source-parity-common-gcd.md`、`spontaneous-source-parity-collision-gate.md`、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descent-overlap-nogo.md`。
>
> **严格状态：**source parity 的 genuine reused prime必须进入 `18K-55`；height-descent parity若由同一 prime在 `Rstar_63,Dhat_63` 中复用，则该 prime也进入 cleared descendant equation `F63^(16)`。本文直接消去 `K`，resultant退化成一个只有 third/source 尺度的正线性 carrier `H_S63`。所以 source-common/descent common support不能自由复用：每个 genuine common prime必须同时进入 `18K-55` 与 `H_S63`。此外 fixed `13` 被严格排除。本文尚未证明这两个短 carrier互素，因此不关闭 A2。

---

## 1. two common-support equations

source common gcd 的 genuine unit-separated prime `r` 满足

\[
\boxed{r\mid18K-55.}
\tag{1.1}
\]

这是 exact square collision

\[
55\mathscr B_W-K^2\mathscr D_W
=c_u^2(18K-55)^2
\]
的直接结果。

另一方面 fully primitive height descent中

\[
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.
\]

若同一个 genuine prime同时进入

\[
r\mid\mathscr R_{63}^\star,
\qquad
r\mid\widehat{\mathscr D}_{63},
\tag{1.2}
\]
则 descended quotient的 cleared equation为

\[
\boxed{
\begin{aligned}
F_{63}^{(16)}:={}&
16(2K-9)
\{g((2K-12)T-2a_3)+5^\lambda C\}\\
&-63gTK^2,
\end{aligned}}
\tag{1.3}
\]
且

\[
\boxed{r\mid F_{63}^{(16)}.}
\tag{1.4}
\]

由

\[
\gcd(\mathscr R_{63}^\star,10g)=1
\]
还自动有

\[
\boxed{r\nmid10g.}
\tag{1.5}
\]

---

## 2. eliminate `K`: a short mixed source carrier

直接对 (1.3) 与 `18K-55` 求 resultant：

\[
\boxed{
\operatorname{Res}_K(F_{63}^{(16)},18K-55)
=-\mathscr H_{S63},}
\tag{2.1}
\]

其中

\[
\boxed{
\mathscr H_{S63}
:=102383\,gT
-29952\,g a_3
+14976\,C5^\lambda.}
\tag{2.2}
\]

因此任意 genuine source-common/descent-common prime满足

\[
\boxed{
r\mid\mathscr H_{S63}.}
\tag{2.3}
\]

所以 common support被同时装入两个短整数：

\[
\boxed{
r\mid\gcd(18K-55,\mathscr H_{S63}).}
\tag{2.4}
\]

这里没有 quadratic character，也没有 resultant degree增长；`K` 被线性 source sheet完全消掉。

---

## 3. `H_S63` is positive and short

写 endpoint normalized variables

\[
\zeta:=\frac{a_3}{T},
\qquad
\delta:=\frac CD.
\]

由

\[
gT=D5^\lambda
\]
可把 (2.2) 除以 `gT`：

\[
\boxed{
\frac{\mathscr H_{S63}}{gT}
=102383-29952\zeta+14976\delta.}
\tag{3.1}
\]

当前 dangerous endpoint给

\[
1<\zeta<\frac{251}{250},
\qquad
0<\delta<\frac3{250}.
\]

所以

\[
\boxed{
\frac{9038899}{125}
<\frac{\mathscr H_{S63}}{gT}
<\frac{9076339}{125}.}
\tag{3.2}
\]

即

\[
\boxed{
72311.192\,gT
<\mathscr H_{S63}
<72610.712\,gT.}
\tag{3.3}
\]

特别地 `H_S63` 是严格正的 natural representative，而不是只有模 `r` 意义的形式。

source sheet本身还有

\[
0<18K-55<180N.
\tag{3.4}
\]

因此 source/descent common support同时受一个 `N`-scale linear carrier和一个 `gT`-scale mixed carrier控制。

---

## 4. fixed `13` is impossible

系数分解为

\[
\boxed{
14976=2^7\cdot3^2\cdot13,}
\tag{4.1}
\]

\[
29952=2\cdot14976,
\]

\[
\boxed{102383=43\cdot2381.}
\tag{4.2}
\]

模 `13`：

\[
14976\equiv29952\equiv0,
\qquad
102383\equiv8\not\equiv0.
\]

若 `r=13` 同时进入 (2.3)，则

\[
0\equiv\mathscr H_{S63}
\equiv8gT\pmod{13}.
\]

但 descendant common prime由 (1.5) 与 `13\nmid10` 满足 `13\nmid g`，同时 `13\nmid T`。矛盾。

所以

\[
\boxed{13\notin
\operatorname{Supp}_{\rm gen}
(\text{source-common}\cap\text{descent-common}).}
\tag{4.3}
\]

这也意味着旧 source collision sheet与 additive central sheet的唯一 odd common prime `13` 不能充当新的 descent parity reuse通道。

---

## 5. support radical budget

令 `E_SD` 为 genuine source-common primes中同时进入 `Rstar_63,Dhat_63` 的 support，并定义 squarefree radical

\[
\boxed{R_{SD}:=\prod_{r\in E_{SD}}r.}
\tag{5.1}
\]

由 (2.4)：

\[
\boxed{
R_{SD}\mid\gcd(18K-55,\mathscr H_{S63}).}
\tag{5.2}
\]

因此

\[
\boxed{
R_{SD}<180N,}
\tag{5.3}
\]

并同时

\[
\boxed{
R_{SD}<\frac{9076339}{125}gT.}
\tag{5.4}
\]

(5.3) 对 support radical已经很短；若要对 source common gcd的完整 exponent收费，仍应使用既有 square-root-depth product `H_S^gen|18K-55`，本文不把 radical bound误写成 full-depth bound。

---

## 6. current source/descent frontier

现在 descended common parity与两个主要旧 prime-source pools的 overlap都已被压缩：

- equal-depth target pool：只剩 fixed squarefree `G_TD|31*179`；
- source-common pool：必须进入
  \[
  \gcd(18K-55,\mathscr H_{S63}),
  \]
  且 fixed `13` 不可能。

所以一个 target-free descendant common inert supplier若还想复用 source parity，必须支付两个独立短 natural carriers，而不能只依靠 `Rstar/Dhat` 的 internal syzygy。

下一步最有价值的是把 `H_S63` 与 source discriminant `D_W` / source triangle联立，继续压缩 fixed coefficient primes `43,2381` 与 generic source root；或在 global parity ledger中先除去 `R_SD`，研究剩余 descendant pair是否仍强迫 distinct inert support。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-target-descent-depth-squeeze"></a>

> 整合来源：`spontaneous-crt-target-descent-depth-squeeze.md`

# A2 fixed `31/179` target/descent overlap 的 exact depth squeeze

> **依赖：** `spontaneous-crt-target-descent-overlap.md`、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-residual-parity-doubling.md`。
>
> **严格状态：**前一文件把 equal-depth target/descent reuse压成 fixed `31/179`，并证明 baseline `h>=2` 时 `v_p(Dhat_63)=1`。本文使用 original additive carrier的 target depth与 fully primitive positive descent，进一步证明同样 `v_p(Rstar_63)=1`。因此任意高 baseline target `p^h,h>=2` 在两个 descended carriers中都只留下 first-layer shadow；无界 target depth不能随 descent reuse传播。唯一可能继续发生 second-layer cancellation的只剩 fixed `31/179,h=1`。本文不排除这两个低 baseline templates，因此不关闭 A2。

---

## 1. original target depth

height-free additive identity之前给

\[
\widehat{\mathcal T}_2
=5^m\widehat{\mathcal J}_H
-2^{m+1}B_0^2(2K-9)\alpha,
\tag{1.1}
\]

其中 `B_0=c_ug`。

真正 equal-depth oversaturation target满足

\[
v_p(\widehat{\mathcal J}_H)\ge h+1,
\]

\[
v_p(\alpha)=2h.
\]

所以

\[
\boxed{
v_p(\widehat{\mathcal T}_2)
\ge\min(h+1,2h)=h+1.}
\tag{1.2}
\]

这里允许两项进一步 cancellation；本文只需要 lower bound。

---

## 2. descended quotient depth for high baseline

前一 target-overlap theorem已经证明：若

\[
p\in\{31,179\},
\qquad h\ge2,
\]
则

\[
\boxed{v_p(\widehat{\mathscr D}_{63})=1.}
\tag{2.1}
\]

这些 primes与 `2\cdot5g` 分离，所以

\[
\boxed{
v_p(g2^m\widehat{\mathscr D}_{63})=1.}
\tag{2.2}
\]

---

## 3. positive descent forces the short remainder to the same first layer

fully primitive descent为

\[
\boxed{
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.}
\tag{3.1}
\]

由 (1.2)，当 `h>=2`：

\[
v_p(\widehat{\mathcal T}_2)\ge h+1\ge3.
\tag{3.2}
\]

而 (2.2) 的第二项精确只有一层。

如果第一项深度大于 `1`，右边和的唯一最浅项就是第二项，整个右边只能有 depth `1`，与 (3.2) 矛盾。

如果第一项不被 `p` 整除，右边则为 unit，也矛盾。

所以第一项必须精确同深：

\[
\boxed{
v_p(5^\lambda\mathscr R_{63}^\star)=1.}
\tag{3.3}
\]

`p\ne5`，故

\[
\boxed{
v_p(\mathscr R_{63}^\star)=1.}
\tag{3.4}
\]

---

## 4. complete high-baseline depth profile

结合 target baseline

\[
v_p(P)=h
\]
和前一 theorem：

\[
\boxed{
\begin{array}{c|c}
\text{carrier}&p\text{-depth}\\ \hline
P(K)&h\\
\widehat{\mathcal T}_2&\ge h+1\\
\widehat{\mathscr D}_{63}&1\\
\mathscr R_{63}^\star&1
\end{array}
\qquad
(p=31,179,\ h\ge2).}
\tag{4.1}
\]

所以 target baseline可以随 `h` 增长，但 descent overlap完全停留在 first layer。

特别地：

\[
\boxed{
\text{unbounded equal-depth target resonance cannot propagate into the height-descent pair}.}
\tag{4.2}
\]

---

## 5. only low-baseline fixed templates remain

真正尚未由本链精确锁死的 target/descent reuse只有

\[
\boxed{
(p,h)=(31,1),\quad(179,1).}
\tag{5.1}
\]

此时 target-overlap identity中 main term与 `H_0` error都只有一层，`Dhat_63` 可能发生 next-digit cancellation；positive descent也允许 `Rstar_63` 同步继续一层。

因此若要彻底删除 target reuse，只需对两个 fixed roots

\[
K\equiv9\pmod{31},
\qquad
K\equiv71\pmod{179}
\]
做一次 mod-`p^2` normalized audit。没有任何 moving prime或 high-depth Hensel family需要继续处理。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-target-descent-fixed-h1-third"></a>

> 整合来源：`spontaneous-crt-target-descent-fixed-h1-third.md`

# A2 fixed `31/179,h=1` 的 third-layer triple-deep points

> **依赖：** `spontaneous-crt-target-descent-fixed-h1.md`、`spontaneous-height-equal-depth-decimal-pair.md`、`spontaneous-height-equal-depth-tropical-balance.md`。
>
> **严格状态：**上一文件把 `p^2|Dhat_63` 压成每个 fixed prime唯一一个模 `p^2` state，并把 `p^3|Dhat_63` 压成一条 affine next-digit line。本文再要求原 deep decimal direction也继续一层，即 `v_p(R_+)>=3`（等价于 `v_p(E_+)>=4`，因为 `h=1`）。`R_+` 给第二条 affine line；两线横截后每个 prime只剩唯一一个模 `p^3` state。随后 tropical balance强迫 `min(r_B,rho_p)=1`，所以这些 triple-deep points仍不能同时携带第二层 companion residual与第二层 full tail。本文不排除这两个 fixed third-order points，因此不关闭 A2。

---

## 1. recall the unique second-layer states

上一文件已证明：若 fixed `p=31,179`, baseline `h=1` 的 genuine deep target还满足

\[
p^2\mid\widehat{\mathscr D}_{63},
\]
则唯一可能为

\[
\boxed{
\begin{array}{c|c|c}
p&K_2\pmod{p^2}&d_2=D/N\pmod{p^2}\\ \hline
31&9&7\\
179&15823&25476.
\end{array}}
\tag{1.1}
\]

写第三位

\[
K=K_2+p^2\kappa,
\qquad
d=d_2+p^2\mu.
\tag{1.2}
\]

并仍有 exact baseline

\[
v_p(P)=v_p(U)=v_p(R_{PD})=1.
\tag{1.3}
\]

---

## 2. descended quotient 的 third-layer lines

上一文件已从 full resonance `rho_p>=1` 得到：

### `p=31`

\[
\boxed{p^3\mid\widehat{\mathscr D}_{63}
\iff
\mu\equiv17+21\kappa\pmod{31}.}
\tag{2.1}
\]

### `p=179`

\[
\boxed{p^3\mid\widehat{\mathscr D}_{63}
\iff
\mu\equiv58+21\kappa\pmod{179}.}
\tag{2.2}
\]

所以 descent 自己在 third digit只留一条 affine line。

---

## 3. `R_+` 的 third-layer lines

仍用

\[
\frac{R_+}{N}=dP-K(dK-1).
\tag{3.1}
\]

在 (1.1) 的 unique second-layer state中已经有 `p^2|R_+`。把 (1.2) 代入，除以 `p^2N` 并模 `p`。

### `p=31`

直接展开得到

\[
\boxed{
\frac{R_+}{31^2N}
\equiv1+7\kappa+12\mu
\pmod{31}.}
\tag{3.2}
\]

所以

\[
\boxed{
v_{31}(R_+)\ge3
\iff
\mu\equiv18+2\kappa\pmod{31}.}
\tag{3.3}
\]

### `p=179`

同理：

\[
\boxed{
\frac{R_+}{179^2N}
\equiv61+71\kappa+150\mu
\pmod{179},}
\tag{3.4}
\]

故

\[
\boxed{
v_{179}(R_+)\ge3
\iff
\mu\equiv70+58\kappa\pmod{179}.}
\tag{3.5}
\]

由于

\[
E_+=E_M\omega R_+,
\qquad v_p(E_M\omega)=h=1,
\]
这两条也就是

\[
\boxed{v_p(E_+)\ge4}
\tag{3.6}
\]
的 exact third-digit conditions。

---

## 4. two affine lines intersect in one point

### `p=31`

联立 (2.1),(3.3)：

\[
17+21\kappa\equiv18+2\kappa\pmod{31}.
\]

于是

\[
19\kappa\equiv1\pmod{31},
\]
唯一得到

\[
\boxed{\kappa\equiv18,\qquad\mu\equiv23\pmod{31}.}
\tag{4.1}
\]

所以唯一 triple-deep state 为

\[
\boxed{
K\equiv17307\pmod{31^3},
\qquad
D/N\equiv22110\pmod{31^3}.}
\tag{4.2}
\]

### `p=179`

联立 (2.2),(3.5)：

\[
58+21\kappa\equiv70+58\kappa\pmod{179},
\]
即

\[
37\kappa\equiv-12\pmod{179}.
\]

唯一得到

\[
\boxed{\kappa\equiv169,\qquad\mu\equiv27\pmod{179}.}
\tag{4.3}
\]

所以唯一 triple-deep state 为

\[
\boxed{
K\equiv5430752\pmod{179^3},
\qquad
D/N\equiv890583\pmod{179^3}.}
\tag{4.4}
\]

两点都仍满足

\[
\boxed{v_p(P)=v_p(U)=1,}
\tag{4.5}
\]

所以它们不是 baseline Hensel lift伪装出来的 high-`h` states。

---

## 5. tropical balance caps the remaining tail freedom

在两个 points中，(3.6) 给

\[
v_p(E_+)\ge4.
\]

而当前 baseline 为

\[
h=1,
\qquad r_B\ge1,
\qquad\rho_p\ge1.
\]

`spontaneous-height-equal-depth-tropical-balance.md` 的 universal `h=1` law 因此直接给

\[
\boxed{\min\{r_B,\rho_p\}=1.}
\tag{5.1}
\]

等价地：

\[
\boxed{
\text{在 (4.2)/(4.4) 中，不可能同时有 }r_B\ge2\text{ 且 }\rho_p\ge2.}
\tag{5.2}
\]

所以即使 fixed `31/179` 继续同时深化 descent 与 `E_+`，extra depth也不能在 companion residual和 full resonance tail两边同时传播。

---

## 6. current low-baseline frontier

fixed target/descent reuse 的危险局部状态现在形成严格塔：

\[
\boxed{
\begin{array}{c|c|c|c}
p&\text{first layer}&\text{second layer}&\text{descent + }E_+\text{ third layer}\\ \hline
31&K=9\bmod31&(K,d)=(9,7)\bmod31^2&(17307,22110)\bmod31^3\\
179&K=71\bmod179&(K,d)=(15823,25476)\bmod179^2&(5430752,890583)\bmod179^3
\end{array}}
\tag{6.1}
\]

并且 third-layer points都满足 tail cap (5.1)。

因此 `31/179,h=1` 已不再是自由 two-variable Hensel family：second layer是单点，最危险的 simultaneous third layer仍是单点。剩余若继续推进，应把这两个 fixed mod-`p^3` points送入 `B_W/J_H` normalized unit equation或 decimal exponent orbit；继续只升 `K,d` 会进入机械 Hensel，而不会自动产生新的 obstruction。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-target-descent-fixed-h1"></a>

> 整合来源：`spontaneous-crt-target-descent-fixed-h1.md`

# A2 fixed `31/179`, baseline `h=1` 的 target/descent 低层压缩

> **依赖：** `spontaneous-crt-target-descent-overlap.md`、`spontaneous-crt-target-descent-depth-squeeze.md`、`spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-equal-depth-decimal-pair.md`。
>
> **严格状态：**此前 equal-depth target 与 height-descent overlap 已只剩 fixed `p=31,179`；对 `h>=2` 已证明两个 descended carriers 都只能保留一层。本文处理剩余的 `h=1`。先把 source ratio `d=D/N` 与 target root `K` 在模 `p^2` 展开；deep resonance `p^2|R_+` 给一条线性 digit relation，而 `p^2|Dhat_63` 再给第二条。两式联立后，每个 fixed prime 都只剩唯一一个模 `p^2` collision state。进一步利用 full resonance `rho_p>=1` 的 projective unit relation，可把 `p^3|Dhat_63` 再压成唯一一条 affine next-digit line。本文尚未排除这两条 third-layer lines，因此不关闭 A2。

---

## 1. low-baseline setting

固定

\[
p\in\{31,179\},
\qquad h=v_p(P)=v_p(U)=1,
\]

其中

\[
P(K):=6K^2-36K+55,
\qquad
U:=DK-N=qW_q.
\]

此前 target/descent overlap 已证明 first-layer root 唯一为

\[
\boxed{
(p,K_0)=(31,9),\qquad(179,71).}
\tag{1.1}
\]

因为 `p∤N`，在 `Z_p` 中定义

\[
\boxed{d:=D/N.}
\tag{1.2}
\]

由 `p|U`：

\[
dK\equiv1\pmod p.
\]

所以 first source roots 为

\[
\boxed{
(p,d_0)=(31,7),\qquad(179,58).}
\tag{1.3}
\]

写

\[
K=K_0+pk,
\qquad
d=d_0+p\ell
\qquad(k,\ell\in\mathbf F_p).
\tag{1.4}
\]

并记

\[
u_0:=\frac{dK-1}{p}\pmod p,
\qquad
P_0:=\frac{P(K)}p\pmod p.
\tag{1.5}
\]

当前 exact `h=1` 要求

\[
P_0u_0\ne0.
\tag{1.6}
\]

---

## 2. deep resonance 的第一条 digit line

由

\[
R_+=DP-KU
\]
除以 `N`：

\[
\frac{R_+}{N}=dP-K(dK-1).
\tag{2.1}
\]

真正 deep target 满足 `rho_p>=1`，所以

\[
\boxed{p^2\mid R_+.}
\tag{2.2}
\]

除以 `pN` 并模 `p`：

\[
\boxed{d_0P_0-K_0u_0\equiv0\pmod p.}
\tag{2.3}
\]

### 2.1 `p=31`

直接展开：

\[
\boxed{P_0\equiv7+10k,}
\tag{2.4}
\]

\[
\boxed{u_0\equiv2+7k+9\ell.}
\tag{2.5}
\]

代入 (2.3)：

\[
7k+12\ell\equiv0\pmod{31},
\]
所以

\[
\boxed{\ell\equiv2k\pmod{31}.}
\tag{2.6}
\]

### 2.2 `p=179`

对应展开为

\[
\boxed{P_0\equiv155+100k,}
\tag{2.7}
\]

\[
\boxed{u_0\equiv23+58k+71\ell.}
\tag{2.8}
\]

(2.3) 化为

\[
18+71k+150\ell\equiv0\pmod{179},
\]
即

\[
\boxed{\ell\equiv50+58k\pmod{179}.}
\tag{2.9}
\]

所以仅 deep target 本身仍各留 `p-1` 个 exact-`h=1` digit classes；下面的 descended quotient 会把它们压成一个。

---

## 3. descended quotient 的 exact source form

沿用

\[
\widehat{\mathscr D}_{63}=c_u^2\mathscr F_{63},
\]

以及 exact identity

\[
16\mathscr F_{63}
=3gT G_D(K)
-16(2K-9)(g\alpha+H_0),
\tag{3.1}
\]

其中

\[
\boxed{G_D(K):=11K^2-240K+432.}
\tag{3.2}
\]

在 `h=1` 中写

\[
\omega=p\omega_0,
\qquad
U=qW_q.
\]

source triangle 给

\[
g\omega=q5^\lambda+c_u.
\tag{3.3}
\]

因此

\[
\begin{aligned}
g\alpha+H_0
&=(g\omega+c_u)W_q\\
&=(2g\omega-q5^\lambda)\frac Uq.
\end{aligned}
\]

令

\[
t:=\frac{g\omega_0}{q}\in\mathbf Z_p,
\]
则有 exact identity

\[
\boxed{
g\alpha+H_0=(2pt-5^\lambda)U.}
\tag{3.4}
\]

又因

\[
gT=D5^\lambda,
\]
将 (3.4) 代入 (3.1)：

\[
\boxed{
16\mathscr F_{63}
=5^\lambda\bigl[3DG_D+16(2K-9)U\bigr]
-32p(2K-9)tU.}
\tag{3.5}
\]

除去 `N` 并使用 `D=dN,U=N(dK-1)`：

\[
\boxed{
\frac{16\mathscr F_{63}}N
=5^\lambda A
-32p(2K-9)t(dK-1),}
\tag{3.6}
\]

其中

\[
\boxed{
A:=3dG_D+16(2K-9)(dK-1).}
\tag{3.7}
\]

first target layer使 `p|G_D` 且 `p|(dK-1)`。所以第二项自动含 `p^2`，从而

\[
\boxed{
p^2\mid\widehat{\mathscr D}_{63}
\iff
\frac Ap\equiv0\pmod p.}
\tag{3.8}
\]

等价地

\[
\boxed{
3d_0\frac{G_D(K)}p
+16(2K_0-9)u_0
\equiv0\pmod p.}
\tag{3.9}
\]

这里 `c_u,N,5^lambda` 全为 p-units，所以没有隐藏零因子。

---

## 4. `p=31`: second layer 只有 `K=9, d=7 mod31^2`

在 `K=9+31k` 下：

\[
\boxed{
\frac{G_D(K)}{31}
\equiv4+20k\pmod{31}.}
\tag{4.1}
\]

将 deep line `ell=2k` 代入 (3.9)，所有常数项消掉，只剩

\[
\boxed{21k\equiv0\pmod{31}.}
\tag{4.2}
\]

因此

\[
\boxed{k\equiv0,\qquad\ell\equiv0\pmod{31}.}
\tag{4.3}
\]

也就是

\[
\boxed{
K\equiv9\pmod{31^2},
\qquad
\frac DN\equiv7\pmod{31^2}.}
\tag{4.4}
\]

该 state 确实仍是 exact `h=1`：

\[
\boxed{
P/31\equiv7,
\qquad
U/(31N)\equiv2
\pmod{31}.}
\tag{4.5}
\]

并且 source-prefix reader 保持 exact baseline：

\[
\boxed{
\frac{R_{PD}}{31N^2}\equiv17\pmod{31}.}
\tag{4.6}
\]

所以这不是 baseline 被偷偷提升到 `h>=2` 的假状态。

---

## 5. `p=179`: second layer 也只有一个 state

在 `K=71+179k` 下：

\[
\boxed{
\frac{G_D(K)}{179}
\equiv38+69k\pmod{179}.}
\tag{5.1}
\]

将 deep line

\[
\ell\equiv50+58k
\]
代入 (3.9)，得到

\[
\boxed{129+86k\equiv0\pmod{179}.}
\tag{5.2}
\]

唯一解为

\[
\boxed{k\equiv88\pmod{179}.}
\tag{5.3}
\]

进而

\[
\boxed{\ell\equiv142\pmod{179}.}
\tag{5.4}
\]

所以唯一 second-layer collision 为

\[
\boxed{
K\equiv15823\pmod{179^2},
\qquad
\frac DN\equiv25476\pmod{179^2}.}
\tag{5.5}
\]

同样 exact baseline 没有提升：

\[
\boxed{
P/179\equiv5,
\qquad
U/(179N)\equiv173
\pmod{179},}
\tag{5.6}
\]

\[
\boxed{
\frac{R_{PD}}{179N^2}\equiv68\pmod{179}.}
\tag{5.7}
\]

---

## 6. second-layer compression theorem

综合 §§2–5：

\[
\boxed{
\begin{array}{c|c|c}
p&K\pmod{p^2}&D/N\pmod{p^2}\\ \hline
31&9&7\\
179&15823&25476
\end{array}}
\tag{6.1}
\]

是 fixed `31/179,h=1` deep target 中使

\[
p^2\mid\widehat{\mathscr D}_{63}
\]
成为可能的全部 states。

fully primitive descent为

\[
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.
\]

而 `h=1` target 已有

\[
p^2\mid\widehat{\mathcal T}_2.
\]

所有 prefactors 对 `31,179` 都是 units，所以

\[
\boxed{
p^2\mid\widehat{\mathscr D}_{63}
\iff
p^2\mid\mathscr R_{63}^\star.}
\tag{6.2}
\]

因此 (6.1) 同时也是两个 descended carriers 的完整 second-layer collision table。

---

## 7. full resonance 把 third layer 再压成一条 affine line

现在固定 (6.1) 的 unique second-layer state，并写

\[
K=K_2+p^2\kappa,
\qquad
d=d_2+p^2\mu.
\tag{7.1}
\]

令

\[
u_1:=\frac{dK-1}{p}\pmod p.
\]

full equal-depth resonance `rho_p>=1` 来自

\[
L_{JB}=2Dg\omega K-fqW_q,
\qquad p^2\mid?\text{ no; }v_p(L_{JB})\ge2.
\]

除去一层 `p` 并用

\[
f=g\omega+c_u\equiv-q5^\lambda\pmod p
\]
得到

\[
\boxed{2dK\,t+5^\lambda u_1\equiv0\pmod p.}
\tag{7.2}
\]

而 `dK≡1 mod p`，所以

\[
\boxed{t\equiv-\frac{5^\lambda}{2}u_1\pmod p.}
\tag{7.3}
\]

在 unique second-layer state中 `p^2|A`。将 (3.6) 除以 `p^2` 并模 `p`，再代入 (7.3)，得到完全不含 `t` 的 third-layer criterion：

\[
\boxed{
p^3\mid\widehat{\mathscr D}_{63}
\iff
\frac{A}{p^2}
+16(2K_0-9)u_1^2
\equiv0\pmod p.}
\tag{7.4}
\]

直接展开 (7.4)：

### `p=31`

\[
K=9+31^2\kappa,
\qquad d=7+31^2\mu,
\]
给

\[
\boxed{9+2\kappa+25\mu\equiv0\pmod{31},}
\tag{7.5}
\]
即

\[
\boxed{\mu\equiv17+21\kappa\pmod{31}.}
\tag{7.6}
\]

### `p=179`

\[
K=15823+179^2\kappa,
\qquad d=25476+179^2\mu,
\]
给

\[
\boxed{20+106\kappa+12\mu\equiv0\pmod{179},}
\tag{7.7}
\]
即

\[
\boxed{\mu\equiv58+21\kappa\pmod{179}.}
\tag{7.8}

所以 second layer 的单点并不会重新炸成 `p^2` 个 third-digit states；每个 fixed prime只剩一条 `p` 点 affine line。

---

## 8. current fixed-`31/179` frontier

当前 target/descent reuse 的 low-baseline局部结构已经压成：

\[
\boxed{
\begin{array}{c|c|c}
p&\text{second layer}&\text{third layer}\\ \hline
31&(K,d)=(9,7)\bmod31^2
&\mu=17+21\kappa\bmod31\\
179&(K,d)=(15823,25476)\bmod179^2
&\mu=58+21\kappa\bmod179
\end{array}}
\tag{8.1}
\]

同时两 second-layer states都满足：

\[
v_p(P)=v_p(U)=v_p(R_{PD})=1.
\]

所以没有 hidden baseline lift，也没有 source-prefix exceptional branch。

这已经删除了 fixed `31/179,h=1` 的大部分 next-digit自由，但尚未证明 affine third-layer line为空。下一步应把 (7.6)/(7.8) 与 `H_pref/J_H` 的 oversaturation second digit或 `Lambda_tail` 的 exact tail digit联立；继续只升 `K,d` 自身不会自动产生矛盾。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-target-descent-global-gcd"></a>

> 整合来源：`spontaneous-crt-target-descent-global-gcd.md`

# A2 target baseline 与 height-descent pair 的 fixed squarefree common gcd

> **依赖：** `spontaneous-crt-target-descent-overlap.md`、`spontaneous-crt-target-descent-depth-squeeze.md`、`spontaneous-crt-target-descent-fixed-h1.md`、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descended-quotient-orientation.md`。
>
> **严格状态：**此前逐 prime 证明 equal-depth target 若与 fully primitive height-descent pair复用 prime，则只能是 fixed `31,179`；高 baseline `h>=2` 时两个 descended carriers在该 prime上都精确只有一层，而 `h=1` 时 target baseline自身只有一层。本文把这些局部结论合成为一个 global gcd identity：target product `G_tar` 与 `Rstar_63,Dhat_63` 的 common part完全相同，是 `31*179` 的 squarefree divisor。除去该固定 common part后，两个 descended carriers都与全部 target baseline support互素。结合 primitive mod-4 orientation，在 `Z=1 mod4` 分支中，若 fixed overlap的数量为偶数，则两个 target-free residual carriers仍各自为 `3 mod4`，因此各自必须产生 target-disjoint inert parity。本文不证明这两份新 parity彼此也不复用，因此不关闭 A2。

---

## 1. target baseline product

令 `E_tar` 为当前所有 genuine deep equal-depth omega-height target primes，并写

\[
h_p:=v_p(\omega)=v_p(W_q)\ge1.
\]

定义 baseline product

\[
\boxed{
G_{\rm tar}:=\prod_{p\in E_{\rm tar}}p^{h_p}.}
\tag{1.1}
\]

已有 target ladder 给

\[
G_{\rm tar}\mid P(K),
\]
并且对每个 target prime

\[
\boxed{v_p(P)=h_p.}
\tag{1.2}
\]

fully primitive height descent为

\[
\boxed{
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.}
\tag{1.3}
\]

其中

\[
\boxed{
\mathscr R_{63}^\star>0,
\qquad
\mathscr R_{63}^\star\equiv3\pmod4,
\qquad
\gcd(\mathscr R_{63}^\star,10g)=1.}
\tag{1.4}
\]

---

## 2. target overlap support is only `31,179`

`spontaneous-crt-target-descent-overlap.md` 已证明：若 genuine target prime `p` 还满足

\[
p\mid\widehat{\mathscr D}_{63}
\]
或

\[
p\mid\mathscr R_{63}^\star,
\]
则

\[
\boxed{p\in\{31,179\}.}
\tag{2.1}
\]

更精确地，对应的 target root必须分别落在

\[
\boxed{
K\equiv9\pmod{31},
\qquad
K\equiv71\pmod{179}.}
\tag{2.2}
\]

另一个 `P(K)` root并不属于 descent overlap sheet。

所以 moving target support 与整个 descended pair已经完全分离。

---

## 3. within the target pool, the two descended carriers have identical support

固定 `p\in E_tar`。target oversaturation给

\[
\boxed{v_p(\widehat{\mathcal T}_2)\ge h_p+1\ge2.}
\tag{3.1}
\]

且 genuine target 与 `5g2` 分离。

由 descent identity (1.3)：

- 若 `p|Dhat_63` 而 `p∤Rstar_63`，右边第一项为 unit，故 `That_2` 为 unit，矛盾；
- 若 `p|Rstar_63` 而 `p∤Dhat_63`，同理右边第二项为 unit，仍矛盾。

因此

\[
\boxed{
 p\in E_{\rm tar}
\Longrightarrow
\bigl[p\mid\widehat{\mathscr D}_{63}
\iff p\mid\mathscr R_{63}^\star\bigr].}
\tag{3.2}
\]

结合 §2，两者在 target pool内的 common support完全相同，而且至多是 `31,179`。

---

## 4. common target depth is always exactly one layer

现在审计 gcd 中的 exponent。

### high baseline `h_p>=2`

`spontaneous-crt-target-descent-depth-squeeze.md` 已证明，对 fixed overlap primes `31,179`：

\[
\boxed{
v_p(\widehat{\mathscr D}_{63})
=v_p(\mathscr R_{63}^\star)=1.}
\tag{4.1}
\]

因此与 `G_tar` 的 common exponent为

\[
\min(h_p,1)=1.
\]

### low baseline `h_p=1`

即使 descended carrier继续 Hensel加深，`G_tar` 在该 prime上本身只有一层：

\[
v_p(G_{\rm tar})=1.
\]

所以 gcd exponent仍然只能是

\[
\boxed{1.}
\tag{4.2}
\]

因此 target/descent common factor在所有 baseline depth下都 squarefree。

---

## 5. canonical global common factor

定义

\[
\boxed{
G_{TD}
:=\gcd(G_{\rm tar},\mathscr R_{63}^\star).}
\tag{5.1}
\]

由 §§2--4：

\[
\boxed{
G_{TD}\mid31\cdot179,
\qquad G_{TD}\text{ squarefree}.}
\tag{5.2}
\]

而 (3.2) 与相同的 depth audit给

\[
\boxed{
G_{TD}
=\gcd(G_{\rm tar},\widehat{\mathscr D}_{63}).}
\tag{5.3}
\]

因此

\[
\boxed{
G_{TD}\in\{1,31,179,31\cdot179\}.}
\tag{5.4}
\]

它是 entire target baseline 与 descended pair之间唯一可能的 common bookkeeping factor。

定义 target-free quotients

\[
\boxed{
R_{TD}^\circ:=\frac{\mathscr R_{63}^\star}{G_{TD}},
\qquad
D_{TD}^\circ:=\frac{\widehat{\mathscr D}_{63}}{G_{TD}}.}
\tag{5.5}
\]

则严格有

\[
\boxed{
\gcd(R_{TD}^\circ,G_{\rm tar})
=\gcd(D_{TD}^\circ,G_{\rm tar})=1.}
\tag{5.6}
\]

所以除去最多 `5549` 的 fixed factor以后，两个 descended carriers都与全部 target baseline support真正分离。

---

## 6. mod-4 parity after removing target overlap

因为

\[
31\equiv179\equiv3\pmod4,
\]
所以

\[
\boxed{
G_{TD}\equiv
\begin{cases}
1\pmod4,&G_{TD}=1\text{ or }31\cdot179,\\
3\pmod4,&G_{TD}=31\text{ or }179.
\end{cases}}
\tag{6.1}
\]

而

\[
\mathscr R_{63}^\star\equiv3\pmod4.
\]
故

\[
\boxed{
R_{TD}^\circ\equiv
\begin{cases}
3\pmod4,&G_{TD}\equiv1\pmod4,\\
1\pmod4,&G_{TD}\equiv3\pmod4.
\end{cases}}
\tag{6.2}
\]

因此若 fixed target overlap数量为偶数（`G_TD=1` 或 `31*179`），则 positive target-free integer `R_TD^circ` 仍为 `3 mod4`，必含至少一枚 odd inert prime到奇次；由 (5.6)，这枚 prime不属于任何 equal-depth target baseline support：

\[
\boxed{
G_{TD}\equiv1\pmod4
\Longrightarrow
R_{TD}^\circ\text{ 强迫一份 target-disjoint inert parity}.}
\tag{6.3}
\]

---

## 7. dangerous `Z=1 mod4` branch duplicates the target-free parity

`spontaneous-crt-descended-quotient-orientation.md` 已证明

\[
\boxed{
\widehat{\mathscr D}_{63}\equiv3Z\pmod4.}
\tag{7.1}
\]

在最危险 orientation

\[
\boxed{Z\equiv1\pmod4,}
\tag{7.2}
\]
有

\[
\widehat{\mathscr D}_{63}\equiv3\pmod4.
\]

所以和 (6.2) 完全同型：若 `G_TD≡1 mod4`，则

\[
\boxed{D_{TD}^\circ\equiv3\pmod4.}
\tag{7.3}
\]

结合 (5.6)：

\[
\boxed{
Z\equiv1\pmod4,\quad
G_{TD}\equiv1\pmod4
\Longrightarrow
R_{TD}^\circ,D_{TD}^\circ
\text{ 各自都需要 target-disjoint inert parity}.}
\tag{7.4}
\]

本文尚未证明这两份 parity彼此不能由同一个 generic non-target prime复用；该 cross-descendant overlap正是下一层应审计的对象。

---

## 8. revised global frontier

height descent与 equal-depth target之间现在只剩一个绝对有界的接口：

\[
\boxed{G_{TD}\mid5549.}
\]

因此后续 global parity/product arguments可以先无损除去 `G_TD`，再把 descended pair视为 target-free carriers。

特别地：

- `G_TD=1` 或 `31*179`：`Rstar_63` 的 odd-inert parity不能由 target pool支付；在 `Z=1` 中 `Dhat_63` 同样如此；
- `G_TD=31` 或 `179`：恰有一个 fixed target prime可以支付 descended parity，是唯一 target-reuse escape channel。

所以 target/descent reuse已经从任意 moving support压成一个四值 squarefree bookkeeping variable，而不再是 unbounded prime-allocation问题。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-target-descent-overlap"></a>

> 整合来源：`spontaneous-crt-target-descent-overlap.md`

# A2 equal-depth target 与 height-descent overlap 只剩 fixed `31/179`

> **依赖：** `spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descended-quotient-orientation.md`、`spontaneous-crt-descent-overlap-nogo.md`、`spontaneous-crt-f1270-source-audit.md`、`spontaneous-crt-l9-singular-audit.md`、equal-depth target chain。
>
> **严格状态：**本文直接把 equal-depth target relations代入 descended primitive quotient `Dhat_63`，得到一个只含 `K` 的 quadratic `G_D=11K^2-240K+432`。它与 target quadratic `P=6K^2-36K+55` 的 resultant仅为 `31*179*269`；target inert class排除 `269`，所以任何 target/descent reuse只剩 fixed `31,179`。fully primitive remainder `Rstar_63` 给同一 fixed set。更强地，`31,179` 在 resultant中只出现一层，所以 target baseline `h>=2` 时 `Dhat_63` 在该 prime上精确只有一层。结合此前两个 singular-gate audit，`31/179` 与所有 target singular candidates完全错开，因此 target/descent reuse只发生在 generic simple branch。本文尚未排除 `h=1` 的 fixed `31/179` first-layer cancellation，因此不关闭 A2。

---

## 1. exact target decomposition of the descended quotient

fully primitive descent中

\[
\widehat{\mathscr D}_{63}
=c_u^2\mathscr F_{63},
\]

\[
\mathscr F_{63}
=(2K-9)B_\Delta-\frac{63}{16}gTK^2,
\]

\[
B_\Delta=g((2K-9)T-a_3)-H_0.
\]

使用 exact concatenation

\[
\alpha=TK+a_3
\]
把 `a_3=alpha-TK` 代入：

\[
B_\Delta
=3gT(K-3)-g\alpha-H_0.
\tag{1.1}
\]

所以

\[
\begin{aligned}
16\mathscr F_{63}
={}&48gT(2K-9)(K-3)
-63gTK^2\\
&-16(2K-9)(g\alpha+H_0).
\end{aligned}
\]

前两项的 quadratic恰好因成

\[
48(2K-9)(K-3)-63K^2
=3(11K^2-240K+432).
\]

定义

\[
\boxed{G_D(K):=11K^2-240K+432.}
\tag{1.2}
\]

得到 exact identity

\[
\boxed{
16\mathscr F_{63}
=3gT G_D(K)
-16(2K-9)(g\alpha+H_0).}
\tag{1.3}

---

## 2. equal-depth target first layer

真正 equal-depth target满足

\[
v_p(\omega)=v_p(W_q)=h\ge1,
\]

\[
\alpha=\omega W_q,
\qquad
H_0=c_uW_q.
\]

所以

\[
\boxed{v_p(\alpha)=2h,\qquad v_p(H_0)=h.}
\tag{2.1}
\]

`p` 与 `gc_uT` 分离，因此两 summands深度不同：

\[
\boxed{v_p(g\alpha+H_0)=h.}
\tag{2.2}
\]

若 target prime还满足

\[
p\mid\widehat{\mathscr D}_{63},
\]
则由 (1.3)，模 `p` 的 error消失，得到

\[
\boxed{p\mid G_D(K).}
\tag{2.3}
\]

---

## 3. target resultant leaves only `31,179,269`

目标 prefix quadratic为

\[
\boxed{P(K)=6K^2-36K+55.}
\tag{3.1}
\]

直接 resultant：

\[
\boxed{
\operatorname{Res}_K(P,G_D)
=1492681
=31\cdot179\cdot269.}
\tag{3.2}
\]

所有 genuine target inert primes满足

\[
p\equiv7\text{ or }11\pmod{24}.
\]

而

\[
31\equiv7,
\qquad179\equiv11,
\qquad269\equiv5
\pmod{24}.
\]

所以

\[
\boxed{
\operatorname{Supp}_{\rm target}^{\rm gen}
\cap
\operatorname{Supp}(\widehat{\mathscr D}_{63})
\subseteq\{31,179\}.}
\tag{3.3}
\]

两 fixed roots唯一为

\[
\boxed{
K\equiv9\pmod{31},
\qquad
K\equiv71\pmod{179}.}
\tag{3.4}
\]

---

## 4. the fully primitive remainder gives the same fixed set

fully primitive remainder满足 exact formula

\[
\begin{aligned}
16\mathscr R_{63}^\star
={}&2^{2m}5^dc_u^2g^2
(15K^2+384K-848)\\
&-16\cdot2^mgc_u^2C(2K-9)\\
&-16\cdot5^dQ_0^2N_0.
\end{aligned}
\tag{4.1}
\]

在 target上：

\[
\alpha\equiv0
\Longrightarrow
a_3\equiv-TK,
\tag{4.2}
\]

\[
qW_q=DK-(3D-C)\equiv0
\Longrightarrow
C\equiv D(3-K),
\tag{4.3}
\]

而 original carrier `That_2=0` 与 (4.2)、`P=0` 给

\[
\boxed{
Q_0^2N_0
\equiv-2^{2m}c_u^2g^2K^2
\pmod p.}
\tag{4.4}
\]

代入 (4.1)：

\[
\boxed{
16\mathscr R_{63}^\star
\equiv
2^{2m}5^dc_u^2g^2
G_R(K)
\pmod p,}
\tag{4.5}
\]

其中

\[
\boxed{G_R(K):=63K^2+144K-416.}
\tag{4.6}
\]

resultant：

\[
\boxed{
\operatorname{Res}_K(P,G_R)
=13434129
=3^2\cdot31\cdot179\cdot269.}
\tag{4.7}
\]

因此 target与 `Rstar_63` 的 genuine inert overlap同样只可能是

\[
\boxed{31,179.}
\tag{4.8}
\]

对应 common K roots仍是 (3.4)。

事实上

\[
\boxed{G_R=16P-3G_D,}
\tag{4.9}
\]

所以两个 fixed-set resultants是同一 descent relation的不同投影。

---

## 5. transverse depth: high-baseline target can enter `Dhat_63` only once

(3.2) 中 `31,179,269` 全部只出现 exponent `1`。resultant Bezout identity因此给：在任一 fixed common root，

\[
\boxed{
\min\{v_p(P),v_p(G_D)\}=1.}
\tag{5.1}
\]

目标 baseline已有 exact

\[
\boxed{v_p(P)=h.}
\tag{5.2}
\]

所以若

\[
h\ge2,
\]
则

\[
\boxed{v_p(G_D)=1.}
\tag{5.3}
\]

另一方面由 (2.2)，(1.3) 的 error term

\[
16(2K-9)(g\alpha+H_0)
\]
在 `31/179` 上具有 exact depth `h`；两个 fixed states中

\[
2K-9\not\equiv0\pmod p.
\]

当 `h>=2`，main term `3gTG_D` 的 depth为 `1`，唯一最浅。因此

\[
\boxed{
 v_p(\mathscr F_{63})=1,
 \qquad
 v_p(\widehat{\mathscr D}_{63})=1
 \quad(p=31,179;\ h\ge2).}
\tag{5.4}

所以 deep target baseline不能在 descended quotient里继续携带同样的无界深度。

---

## 6. singular locus is completely disjoint from the target reuse candidates

此前两个 singular audit给：

\[
\boxed{
L_9\text{ target branch}:\ \varnothing,}
\tag{6.1}
\]

\[
\boxed{
F_{1270}\text{ target branch}:\ \{7,79,107,199\}.}
\tag{6.2}
\]

本文的 actual descent target reuse candidates为

\[
\boxed{\{31,179\}.}
\tag{6.3}
\]

三集合互不相交。因此

\[
\boxed{
\text{任何 genuine target/descent reuse 都位于 generic simple }K\text{-resultant branch}.}
\tag{6.4}
\]

不存在 target supplier藏进 descent singular Hensel tree的可能。

---

## 7. current frontier

original/short-remainder parity若试图复用 equal-depth target prime，现在只剩两个 fixed first-layer candidates：

\[
31,\quad179.
\]

若 target baseline `h>=2`，它们在 `Dhat_63` 中又只能精确出现一层。

唯一尚未精确关闭的是 `h=1` 时 fixed `31/179` 的 next-digit cancellation：此时 (1.3) 的 main/error 两项都只有一层，可能继续抵消。若需要彻底禁止 target reuse，下一步可只审这两个 fixed prime的 mod-`p^2` normalized equation，不再需要任何 moving-prime分析。

A2 仍为 `待证`。

---

<a id="source-spontaneous-crt-universal-descendant-cubic"></a>

> 整合来源：`spontaneous-crt-universal-descendant-cubic.md`

# A2 descendant common support 的 universal `(K,zeta)` cubic

> **依赖：** `endpoint-lattice.md` 的 exact rational-root quartic、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-pure-branch-defect.md`、`spontaneous-prefix-eliminant.md`。
>
> **严格状态：**descendant common condition先唯一恢复 finite-defect root `r=J_def`；original additive carrier再唯一恢复 prefix ratio `Q^2N_0/B^2`。本文把二者代回 exact rational-root quartic，消去 `C,D,B,Q,N_0`，得到一个只依赖真实 prefix integer `K` 与 third phase `zeta=a_3/T` 的 universal cubic `E_63(K,zeta)`。其 zeta-discriminant完全因子化：除一个新的 degree-8 kernel `H_8(K)` 外，其余 singular factors都是已知 central/descendant gates且以平方出现。对 generic pure-spontaneous branch，这给 `Q_i=0` 之外真正的第二个独立 compatibility equation。本文尚未完成 branchwise resultant，因此不关闭 A2。

---

## 1. normalized rational-root equation

exact rational-root polynomial为

\[
F(J)=
B^2T\,J(TJ+2a_3)(K-J)^2
-Q^2N_0(TJ+a_3)^2.
\]

令

\[
\boxed{\zeta:=a_3/T,}
\qquad
\boxed{R:=Q^2N_0/B^2.}
\]

除去 genuine units `B^2T^2`，root `r=J_def` 满足

\[
\boxed{
\Phi(r)
:=r(r+2\zeta)(K-r)^2
-R(r+\zeta)^2=0.}
\tag{1.1}

这里

\[
r=3-C/D.
\]

---

## 2. additive carrier eliminates `R`

height/additive identity为

\[
\widehat{\mathcal T}_2=0
\Longleftrightarrow
T\mathcal J_H
-2B^2(2K-9)\alpha=0
\pmod p,
\]

其中

\[
\mathcal J_H
=B^2(5K^2-36K+55)-Q^2N_0,
\]

\[
\alpha=T(K+\zeta).
\]

对 descendant common prime，`p|Rstar,Dhat` 由 positive descent自动给

\[
p\mid\widehat{\mathcal T}_2.
\]

除去 `B^2T`：

\[
5K^2-36K+55-R
-2(2K-9)(K+\zeta)=0.
\]

所以

\[
\boxed{
R
=K^2-(18+4\zeta)K+18\zeta+55.}
\tag{2.1}

这一步已经把 prefix norm ratio从 rational-root equation中完全移除。

---

## 3. descendant equation eliminates `r`

`spontaneous-crt-pure-branch-defect.md` 的 universal descendant equation为

\[
(2K-9)(2K-9-2\zeta-r)
=\frac{63}{16}K^2.
\tag{3.1}

在 noncentral sector

\[
2K-9\not\equiv0\pmod p
\]
可唯一解出

\[
\boxed{
 r
=
\frac{
K^2-64K\zeta-576K+288\zeta+1296
}
{16(2K-9)}.}
\tag{3.2}

所以 descendant common prime同时把 rational-root中的两个 auxiliary quantities `R,r` 都降成 `(K,zeta)` 的有理函数。

---

## 4. substitute into `Phi`: universal cubic

将 (2.1),(3.2) 代入 (1.1)。清去 denominator

\[
65536(2K-9)^4
\]
后定义 primitive numerator

\[
\boxed{\mathcal E_{63}(K,\zeta).}
\tag{4.1}

为方便审计，记

\[
U:=2K-9,
\qquad
L:=K^2-576K+1296,
\]

并定义四个小 coefficient polynomials

\[
A:=5K^2+144K-324,
\]

\[
B_2:=381K^4-78048K^3-277520K^2+2392704K-3074112,
\]

\[
B_1:=189K^4-126720K^3+132784K^2+1359360K-2218752,
\]

\[
B_0:=63K^4-54432K^3+136672K^2+239616K-539136.
\]

则完整 cubic具有高度因子化的系数：

\[
\boxed{
\begin{aligned}
\mathcal E_{63}(K,\zeta)
={}&98304U^3A\,\zeta^3\\
&-1024U^2B_2\,\zeta^2\\
&+32ULB_1\,\zeta\\
&-L^2B_0.
\end{aligned}}
\tag{4.2}

因此每个 genuine noncentral descendant common prime都满足

\[
\boxed{\mathcal E_{63}(K,\zeta)\equiv0\pmod p.}
\tag{4.3}

这是完全独立于 `C,D,B,Q,N_0` 的 universal third/prefix carrier。

---

## 5. cubic discriminant factorization

直接对 `zeta` 求 discriminant。定义

\[
\boxed{
\begin{aligned}
H_8(K):={}&
28539K^8-33511968K^7+7112503200K^6\\
&+135023040000K^5-985065366784K^4\\
&+1911068393472K^3-377731358720K^2\\
&-2065729978368K+1344988053504.
\end{aligned}}
\tag{5.1}

则

\[
\boxed{
\begin{aligned}
\operatorname{Disc}_{\zeta}(\mathcal E_{63})
={}&-2^{34}3^2
(2K-9)^{10}\\
&\cdot(K^2-576K+1296)^2\\
&\cdot(11K^2-240K+432)^2\\
&\cdot H_8(K).
\end{aligned}}
\tag{5.2}

所以 ordinary repeated-root locus分成：

1. central gate `2K-9`；
2. quadratic gate `L=K^2-576K+1296`；
3. known descendant-height quadratic `G_D=11K^2-240K+432`；
4. genuinely new singular kernel `H_8`。

前三项全部以偶 exponent进入 discriminant，不能再次当 independent Legendre obstruction收费。

---

## 6. the new `L` gate itself has fixed-7 discriminant

\[
L=K^2-576K+1296
\]
的 discriminant为

\[
\boxed{
576^2-4\cdot1296
=326592
=216^2\cdot7.}
\tag{6.1}

所以 generic inert prime `p!=7` 若进入 `L=0`，必须满足

\[
\boxed{\left(\frac7p\right)=1.}
\tag{6.2}

因为 `7,p=3 mod4`，互反律等价于

\[
\boxed{\left(\frac p7\right)=-1.}
\tag{6.3}

这只是 singular-gate orientation，不自动排除 moving prime；ramified `7` 需另行审计。

---

## 7. consistency on `alpha=0`

作为结构审计，把

\[
\alpha=0
\Longrightarrow
\zeta=-K
\]
代入 universal cubic。精确因子化为

\[
\boxed{
\mathcal E_{63}(K,-K)
=-9G_D(K)^2\,Q_4(K),}
\tag{7.1}

其中

\[
\boxed{
Q_4(K)
=5055K^4-44640K^3-91424K^2+612864K-539136.}
\tag{7.2}

所以此前 target/height analysis中反复出现的 `G_D(K)=0` 正是 universal cubic 在 alpha-supported sector中的 double factor；这验证本文的降维与既有 target/height结果一致。

剩余 quartic `Q_4` 对应其它 alpha-supported content possibility，不应与 `G_D^2` 重复计数。

---

## 8. pure-spontaneous branch now has two independent equations

在 genuine alpha-free、noncentral pure-spontaneous sector，已有唯一 branch

\[
\mathcal Q_i(\tau;x,y)=0,
\qquad i\in\{1,2\},
\]
以及

\[
K=\frac{9+y}{\tau},
\qquad
\zeta=\frac{z_i(x,y)}{\tau}.
\]

本文再给第二条 independent compatibility：

\[
\boxed{
\mathcal E_{63}\!\left(
\frac{9+y}{\tau},
\frac{z_i(x,y)}{\tau}
\right)=0.}
\tag{8.1}

所以 remaining external kernel已从“一个可自由 simple-Hensel 的 quadratic branch”升级成两方程交集：

\[
\boxed{
\mathcal Q_i=0
\quad\cap\quad
\mathcal E_{63}=0.}
\tag{8.2}

而 `C/D` 又由前一文件唯一恢复。即 third numerator、finite defect、prefix norm ratio都不再是自由变量。

下一步最直接的是对每个 `i` 在 sphere-root quotient ring中求 (8.2) 的 branchwise resultant，审计是否塌成 fixed primes/短 decimal carrier。若 resultant再次只回到 `A_-`, `C_*` 等旧 collision，应明确降级；若出现新 pure-prefix factor，则它就是当前最有希望的 global external obstruction。

A2 仍为 `待证`。

---

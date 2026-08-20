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

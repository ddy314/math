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
K\Lambda_{m dec}=p^{2h+s}v,
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

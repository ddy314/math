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

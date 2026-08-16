# DD Good slot capacity frontier — 2026-08-16

> 本文接续 [`dd-frontier-continuation-2026-08-16.md`](dd-frontier-continuation-2026-08-16.md)。
> 适用范围始终是一个假想满足
> \[
> \frac{n_3}{S}\to6.308883577618\ldots
> \]
> 的 DD frontier sequence，并进一步处于 full rational-contact Good 主质量。
> 本文中的 `main prime-power` 均默认删去 coefficient overlap、conjugate overlap、Bad mass 等总高度为 \(o(S)\) 的 exceptional core。
>
> **状态边界：**本文给出新的严格 frontier 条件蕴含和 no-go 审计；它仍不证明 DD 全局空性。

---

## 1. 基线

沿用

\[
A=s\theta q_c,
\qquad
b=5^T\widetilde r,
\]

\[
c=\widetilde r5^{T-m_2}U,
\qquad
d=s^2\widetilde w2^{m_2},
\]

\[
R_\pm=b\pm A=D_\pm h_\pm,
\qquad
J_\pm=c\pm d=D_\pm j_\pm,
\]

\[
E=D_+D_-,
\qquad V=Ee_0,
\]

以及 cofactor system

\[
H_R=h_+h_-,
\qquad H_J=j_+j_-,
\]

\[
S_c=\frac{bc-Ad}{E},
\qquad
T_c=e_0\widetilde r^{\,2}5^{T-m_2},
\]

\[
S_c^2-H_RH_J=T_c^2.
\tag{CF1}
\]

axis norm 记为

\[
C_*:=\frac{g_0a_2B}{2},
\qquad
N_{\rm ax}=C_*^2+R_0^2,
\qquad
N_c=\frac{N_{\rm ax}}E.
\]

Good square-Plücker 系统使用

\[
S_-=\Pi_-\overline{\Pi_+}K,
\qquad
S_+=\Pi_+\overline{\Pi_-}\,\overline K,
\qquad
N(K)=N_c,
\]

以及

\[
2\,5^{m-T}\widehat\Delta_1
=
\overline{\Pi_+}^{\,2}K h_+
-
\overline{\Pi_-}^{\,2}\overline K h_-,
\tag{G1}
\]

\[
2\,5^{T-m_2}\widehat\Delta_U
=
\overline{\Pi_+}^{\,2}K j_+
-
\overline{\Pi_-}^{\,2}\overline K j_-.
\tag{G2}
\]

最新 continuation 已证明

\[
\log(B_+B_-)=o(S),
\]

且 selected / conjugate orientation 在 \(\Delta_U\) 中的重复总质量均为 \(o(S)\)。

---

## 2. 一个此前未单独写出的 \(\Delta_U\)-norm cofactor identity

已有精确式

\[
5^{T-m_2}L_U=C_*d-iR_0c,
\qquad
L_U=\Pi\Delta_U.
\]

取范数：

\[
C_L5^{2(T-m_2)}N(\Delta_U)
=C_*^2d^2+R_0^2c^2.
\]

另一方面

\[
C_*^2+R_0^2=EN_c,
\qquad
c^2-d^2=EH_J.
\]

所以右端可以完全改写为

\[
\begin{aligned}
C_*^2d^2+R_0^2c^2
&=(C_*^2+R_0^2)d^2+R_0^2(c^2-d^2)\\
&=E(d^2N_c+R_0^2H_J).
\end{aligned}
\]

因此得到精确恒等式

\[
\boxed{
d^2N_c+R_0^2H_J
=
\frac{C_L}{E}
5^{2(T-m_2)}N(\Delta_U).
}
\tag{NcU-elim}
\]

它与已有

\[
\boxed{
\widetilde r^{\,2}5^{4T-2m}N_c
-g_0^2a_2^22^{2m-4}H_R
=
\frac{C_L}{E}N(\Delta_1)
}
\tag{Nc1-elim}
\]

形成一对：前者控制 \((N_c,H_J)\)，后者控制 \((N_c,H_R)\)。

### Good 的 rational norm 形式

Bad 已关闭，同时 conjugate overlap 已是 \(o(S)\)，故 full rational Good 主质量满足

\[
\boxed{
\log\gcd(C_L,N(\Delta_U))=o(S).
}
\tag{Good-norm}
\]

由 `(NcU-elim)`，删去 \(C_L/E\) 与 coefficient exceptional core 后等价地有

\[
\boxed{
\log\gcd
\bigl(C_L,d^2N_c+R_0^2H_J\bigr)
=o(S).
}
\tag{Good-cofactor-unit}
\]

所以 Good 可以完全翻译为 cofactor 层的一条 **unit condition**，而不必继续携带 \(\Delta_U\)。

---

## 3. main prime 的精确 slot theorem

只写 \(D_+\)；\(D_-\) 完全共轭对称。

固定 main

\[
p^h\Vert D_+,
\qquad
p=\pi\bar\pi,
\qquad
\pi^h\Vert\Pi_+.
\]

删去 exceptional core 后

\[
p\nmid2T_c,
\qquad
p\nmid h_-j_-,
\]

并且 Good / conjugate exclusion 给

\[
v_\pi(\widehat\Delta_U)
=v_{\bar\pi}(\widehat\Delta_U)=0.
\]

定义四个非负深度

\[
r:=v_p(h_+),
\qquad
j:=v_p(j_+),
\]

\[
k:=v_\pi(K),
\qquad
\bar k:=v_{\bar\pi}(K).
\]

### 3.1 rational endpoint repeat 互斥

由

\[
j_-h_+-j_+h_-=2T_c
\]

且右端为 \(p\)-unit，立刻得到

\[
\boxed{\min(r,j)=0.}
\tag{Slot-RJ}
\]

也就是说，同一 main prime 不可能同时在 \(R_+\) 与 \(J_+\) 的 reduced cofactor 中继续获得正深度。

### 3.2 Good 强迫 \(K\) 只可能使用 conjugate orientation

在 `(G2)` 的 \(\bar\pi\)-valuation 上：

- 第一项含 \(\overline{\Pi_+}^{\,2}\)，故 valuation 至少 \(2h\)；
- 第二项的 valuation 为 \(k\)，因为 \(j_-\) 与 \(\overline{\Pi_-}\) 都是 \(p\)-unit；
- 左端是 \(\bar\pi\)-unit。

故必有

\[
\boxed{k=0.}
\tag{K-orientation}
\]

于是 main \(p\)-part若进入 \(K\)，只能进入 \(\bar\pi\)-orientation。

特别地

\[
\boxed{v_p(N_c)=\bar k.}
\tag{Nc-slot}
\]

再看 `(G2)` 的 selected \(\pi\)-valuation。两项 valuation 分别为

\[
j,\qquad \bar k.
\]

左端为 unit，因此

\[
\boxed{\min(j,\bar k)=0.}
\tag{Slot-JK}
\]

也就是说，`next-J` 与 axis/carrier repeat 同样逐素数互斥。

综合 `(Slot-RJ)` 与 `(Slot-JK)`：

\[
\boxed{
j>0\Longrightarrow r=\bar k=0.}
\tag{J-isolated}
\]

而 \(r\) 与 \(\bar k\) 可以同时为正。

---

## 4. radius repeat 的精确分解

令

\[
a:=v_\pi(\widehat\Delta_1).
\]

conjugate overlap exclusion 说明它同时也是 main rational depth

\[
a=v_p(N(\Delta_1)).
\]

由 `(G1)` 在 selected \(\pi\) 上，两项 valuation 正好是

\[
r,\qquad\bar k.
\]

因此：

- 若 \(r<\bar k\)，则 \(a=r\)；
- 若 \(\bar k<r\)，则 \(a=\bar k\)；
- 若 \(r=\bar k\)，还可能发生进一步 unit cancellation。

统一写成

\[
\boxed{
a=\min(r,\bar k)+\varepsilon_p,}
\tag{Radius-split}
\]

其中

\[
\varepsilon_p\ge0
\]

且

\[
\boxed{
\varepsilon_p>0
\Longrightarrow r=\bar k.
}
\tag{Pure-equal}
\]

特别地，当

\[
r=\bar k=0,
\qquad
\varepsilon_p>0,
\]

radius repeat 完全来自 `(G1)` 中两个 \(p\)-units 的高阶 cancellation；本文称之为

\[
\boxed{\text{pure-radius slot}.}
\]

这正是简单 slot-counting 无法删掉的通道。

注意 `J-isolated` 并不禁止 pure-radius：若 \(j>0\)，则 \(r=\bar k=0\)，此时 `(G1)` 仍可能出现 \(\varepsilon_p>0\)。

---

## 5. 同一结论的纯 rational cofactor 版本

`(Nc1-elim)` 在 main \(p\) 上所有显式 coefficient 都是 units。结合

\[
v_p(N_c)=\bar k,
\qquad
v_p(H_R)=r,
\]

可把 `(Radius-split)` 完全写成

\[
\boxed{
v_p(N(\Delta_1))
=
v_p\!\left(
\widetilde r^{\,2}5^{4T-2m}N_c
-g_0^2a_2^22^{2m-4}H_R
\right).
}
\tag{Radius-rational}
\]

而 Good 则由 `(NcU-elim)` 给出

\[
\boxed{
p\nmid d^2N_c+R_0^2H_J.}
\tag{Good-rational-local}
\]

因此 Good 的 local algebra 已经可以完全压缩成三个 cofactor slots

\[
H_R,\qquad H_J,\qquad N_c
\]

和一条 equal-depth cancellation `(Radius-rational)`。

这一步不再需要新 Gaussian quotient。

---

## 6. radius repeat 等价于完整拼接分子 repeat

已有 terminal exact identities

\[
g_0(\alpha-a_3)
=2\cdot5^T(UA_0+R_0),
\tag{6.1}
\]

\[
VA_0-g_0a_3
=2\cdot5^TR_0.
\tag{6.2}
\]

由 (6.2)

\[
g_0a_3=VA_0-2\cdot5^TR_0.
\]

代入 (6.1)：

\[
\begin{aligned}
g_0\alpha
&=VA_0+2\cdot5^TUA_0\\
&=(V+2\cdot5^TU)A_0.
\end{aligned}
\]

而

\[
V=2^HZ-5^TU,
\]

故得到新的 exact bridge

\[
\boxed{
g_0\alpha=(2^HZ+5^TU)A_0.}
\tag{Concat-radius}
\]

对 main \(p^h\Vert C_L\)：

\[
p\mid V,
\qquad
(U,V)=(Z,V)=1,
\qquad p\ne2,5.
\]

所以若 \(p\mid2^HZ+5^TU\)，则它同时整除和与差，从而整除 \(2^{H+1}Z\)，矛盾。故

\[
p\nmid2^HZ+5^TU.
\]

再删去 \(p\mid g_0\) 的 exceptional core，有

\[
\boxed{v_p(A_0)=v_p(\alpha).}
\tag{Radius=Concat}
\]

与 continuation 中

\[
v_p(A_0)=v_\pi(\Delta_1)
\]

合并：

\[
\boxed{
\text{secondary/radius repeat}
\Longleftrightarrow
\text{full concatenated numerator }\alpha\text{ repeat}
}
\tag{Secondary=Radius=Concat}
\]

逐 main prime-depth 成立。

这把 pure-radius 从“神秘 Gaussian cancellation”重新翻译成了十进制 digit-shell 问题。

---

## 7. radius 的 digital Gaussian carrier

令

\[
Y:=2\,10^dA_{12}.
\]

numerator reconstruction

\[
UA_0+R_0=g_0B10^dA_{12}
\tag{7.1}
\]

在 radius prime \(p\mid A_0\) 上给

\[
R_0\equiv g_0B10^dA_{12}\pmod{p^a}.
\]

### \(D_+\) channel

由

\[
\Pi_+\mid C_*+iR_0,
\qquad
C_*=\frac{g_0a_2B}{2},
\]

消去公共 unit 得

\[
\boxed{
\Pi_{R,+}\mid a_2+iY.
}
\tag{Radius-G+}
\]

### \(D_-\) channel

同理

\[
\boxed{
\Pi_{R,-}\mid a_2-iY.
}
\tag{Radius-G-}
\]

若将两 sign 统一定向为

\[
\Gamma_R:=\Pi_{R,+}\overline{\Pi_{R,-}},
\]

则

\[
\boxed{
\Gamma_R\mid a_2+iY.
}
\tag{Radius-digital}
\]

这是 pure-radius 的自然 decimal Gaussian carrier。

---

## 8. radius digital carrier 与 axis carrier 的直接 resultant 仍然退化

full rational axis carrier 为

\[
\Gamma:=\Pi_+\overline{\Pi_-}\mid C_*+iR_0.
\]

若同一 radius subcore 同时进入 `(Radius-digital)`，最自然的 \(2\times2\) determinant 是

\[
C_*Y-R_0a_2.
\]

利用

\[
C_*Y
=
\frac{g_0a_2B}{2}\cdot2\,10^dA_{12}
=a_2g_0B10^dA_{12}
\]

与 (7.1)，得到

\[
\boxed{
C_*Y-R_0a_2
=a_2UA_0.
}
\tag{Radius-resultant-collapse}
\]

右端恰好重新含有 radius payer \(A_0\)。

所以“axis Gaussian carrier + radius digital Gaussian carrier 直接取 determinant”不会产生新独立模量；它只把 `(Radius=Concat)` 换了一种写法。

**状态：`失效/降级`。**

---

## 9. 为什么简单的总容量相加关不掉 Good

当前三个 cofactor 的 frontier Archimedean heights 为

\[
\log H_R
=1.617767155236\ldots S+o(S),
\]

\[
\log H_J
=1.602059991328\ldots S+o(S),
\]

而

\[
N_c=\frac{C_*^2+R_0^2}{E}
\]

具有约 \(2S\) 的尺度。

同时

\[
\log N(\Delta_1)
=1.308883577618\ldots S+o(S).
\]

因此每个单独 slot 都有能力承载一个 \(S\)-级 main divisor。互斥关系

\[
\min(r,j)=0,
\qquad
\min(j,\bar k)=0
\]

虽然真实，但仅靠这些容量上界仍得不到

\[
\text{总容量}<S.
\]

尤其 pure-radius 只消耗 \(N(\Delta_1)\) 的 residual capacity，而该 residual height 本身大于 \(S\)。

所以 continuation §18 中的 “slot capacity” 必须理解为：

> 先做逐素数 mutually-exclusive allocation，再对最后留下的 equal-depth / pure-radius slot 寻找 **新的 digit-shell strict bound**。

不能把它简化成对 \(H_R,H_J,N_c,N(\Delta_1)\) 的普通高度求和。

---

## 10. 当前严格压缩后的 Good frontier

截至本文，full rational Good 可以重写成以下有限类型的 local network：

1. `next-R`：\(p\mid H_R\)；
2. `next-J`：\(p\mid H_J\)；
3. `axis/carrier`：\(p\mid N_c\)，且只能取与 selected \(\Pi\) 相反的 Gaussian orientation；
4. `radius overlap`：由 \(\min(v_p(H_R),v_p(N_c))\) 自动支付；
5. `pure-radius`：\(H_R,N_c\) 均为 units（或 equal-depth 已抽掉 baseline）后，`(Nc1-elim)` 的 unit-unit cancellation；它等价于 \(p\mid\alpha\)。

并且：

\[
\boxed{
\text{next-J 与 next-R / axis-repeat 逐素数互斥；}
}
\]

\[
\boxed{
\text{Good 同时要求 }p\nmid d^2N_c+R_0^2H_J;
}
\]

\[
\boxed{
\text{pure-radius 的最后新信息位于完整拼接分子 }\alpha\text{ 的 digit shell。}
}
\]

因此 full rational Good 的真正未决核已经从“若干未定义 slots”缩成：

\[
\boxed{
\text{equal-depth }(H_R,N_c)
\text{ cancellation}
\;\cup\;
\text{pure numerator-shell contact }(C_L,\alpha).
}
\]

下一步若继续 full rational Good，首选目标应是一个 **primitive digit-shell lemma**：证明 main pair-max modulus 在已经满足 rational sign contact 与 `(Good-cofactor-unit)` 后，不可能再以正线性高度进入 \(\alpha\) 或 equal-depth residual。

若这个 lemma 只能再次退回 `(Concat-radius)` / hidden square / `(CF1)`--`(CF5)`，则 full rational Good 的局部代数已经真正闭包，应停止继续造 local resultant，转向 genuine-Gaussian split-prime/digit-shell branch。

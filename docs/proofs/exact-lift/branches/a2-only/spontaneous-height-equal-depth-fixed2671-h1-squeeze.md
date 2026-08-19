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

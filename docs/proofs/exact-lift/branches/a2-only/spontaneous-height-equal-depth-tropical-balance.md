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

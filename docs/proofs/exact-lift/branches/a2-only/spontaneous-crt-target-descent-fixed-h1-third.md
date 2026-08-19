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

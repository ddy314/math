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

# A2 source equal-depth angle cancellation 的 normalized Hensel gate

> **依赖：** `hensel.md`、`spontaneous-angle.md`、`spontaneous-angle-overlap-depth.md`。
>
> **严格状态：**`spontaneous-angle-overlap-depth.md` 已证明 source excess 对 angle carrier 产生奇 valuation 只能发生在 `v_p(d)=h` 的等深 cancellation 层。本文进一步利用旧第二 Hensel Bézout identity，把这一层正规化：证明 `v_p(Psi_9)=h` 精确成立，并把 angle cancellation 改写成只含 normalized source units `sigma^sharp`、`Phi^sharp`、`Psi_9^sharp` 的显式 square-class / quadratic congruence。本文仍未排除该 normalized gate，也不宣称 A2 全局关闭。

---

## 1. 等深 source shell

固定 genuine non-`3` inert source excess prime

\[
p\equiv3\pmod4,
\qquad
p^{2h}\Vert\sigma,
\qquad h\ge1.
\]

reflection endpoint `a_1=9` 中记

\[
d:=225x^2-y,
\]

\[
\Phi_s=(99x-4)r_s-2x-4,
\]

\[
\Psi_9=3600(r_s+1)^2-y(99r_s-2)^2.
\]

旧 source Hensel 结果为

\[
v_p(\Phi_s)=2h,
\qquad
v_p(d)\ge h.
\]

本文只处理 angle odd-depth 唯一可能的 threshold：

\[
\boxed{v_p(d)=h.}
\tag{1.1}
\]

定义 normalized units

\[
d^\sharp:=d/p^h,
\qquad
\Phi^\sharp:=\Phi_s/p^{2h},
\qquad
\sigma^\sharp:=\sigma/p^{2h}.
\tag{1.2}
\]

它们都是 `p`-进单位。

---

## 2. `已严格完成`：第二 Hensel 深度在 threshold 上精确为 `h`

令

\[
A_s:=99x-4.
\]

`hensel.md` 的 exact Bézout identity 在 `a_1=9` 时为

\[
\boxed{
A_s^2\Psi_9-163216d
=\Phi_s\mathcal Q,
}
\tag{2.1}
\]

其中

\[
163216=404^2,
\]
而 genuine source prime 已有

\[
p\nmid A_s\cdot404.
\tag{2.2}
\]

在 (1.1) 下，第二项 `163216d` 恰有 valuation `h`，右边 `Phi_s Q` 至少有 valuation `2h`。因此两者 valuation 不同：

\[
\boxed{v_p(\Psi_9)=h.}
\tag{2.3}
\]

定义

\[
\Psi_9^\sharp:=\Psi_9/p^h.
\tag{2.4}
\]

把 (2.1) 除以 `p^h` 再模 `p`，右边消失，得到

\[
\boxed{
A_s^2\Psi_9^\sharp
\equiv404^2d^\sharp
\pmod p.}
\tag{2.5}
\]

因此

\[
\boxed{
\left(\frac{\Psi_9^\sharp}{p}\right)
=
\left(\frac{d^\sharp}{p}\right).
}
\tag{2.6}
\]

第二 Hensel unit 的 square class 已不再独立。

---

## 3. `已严格完成`：angle extra lift 的 normalized source equation

旧 second-angle exact integer 为

\[
\boxed{
E_1=5^\lambda L_0^2-2c_u\sigma a_2^2.
}
\tag{3.1}
\]

而 reflection source formula 给

\[
\boxed{
L_0=-5^M10^{M-1}d.
}
\tag{3.2}
\]

在 (1.1) 下：

\[
v_p(L_0)=h
\]
因为 `p!=2,5`。定义

\[
L_0^\sharp:=L_0/p^h
=-5^M10^{M-1}d^\sharp.
\tag{3.3}
\]

`Omega_sp` 与 `E_1` 只差 genuine `p`-进单位尺度，因此 angle valuation 超过 baseline `2h` 等价于

\[
E_1/p^{2h}\equiv0\pmod p.
\]
即

\[
\boxed{
5^\lambda(L_0^\sharp)^2
\equiv2c_u\sigma^\sharp a_2^2
\pmod p.}
\tag{3.4}
\]

这就是 source equal-depth cancellation 的规范形式。

---

## 4. 必要 quadratic character

(3.4) 两边的 `L_0^sharp`、`a_2` 都是单位，且其平方不影响 Legendre symbol。因此 extra angle lift 必须满足

\[
\boxed{
\left(\frac{2c_u\sigma^\sharp}{p}\right)
=
\left(\frac{5^\lambda}{p}\right).
}
\tag{4.1}
\]

等价地

\[
\boxed{
\left(\frac{2c_u\sigma^\sharp5^\lambda}{p}\right)=1.
}
\tag{4.2}
\]

所以 source odd residual parity 已被压成一个明确的 normalized quadratic gate，而不是任意 source root。

---

## 5. 用 `Phi^sharp` 改写同一个 gate

`hensel.md` 还有 exact source identity

\[
\boxed{4\sigma=5^Mc_Q\Phi_s.}
\tag{5.1}
\]

除去 `p^{2h}`：

\[
\boxed{
4\sigma^\sharp=5^Mc_Q\Phi^\sharp.
}
\tag{5.2}
\]

代入 (4.2)，并注意 `4` 是平方、`2^{-1}` 与 `2` 有相同 Legendre character：

\[
\boxed{
\left(
\frac{2c_uc_Q\Phi^\sharp5^{M+\lambda}}p
\right)=1.
}
\tag{5.3}
\]

这把 angle extra-lift gate 完全写成 source linear Hensel 的 normalized unit `Phi^sharp`。

---

## 6. `已严格完成`：消去 `d^sharp` 后的二单位 congruence

由 (2.5)：

\[
d^\sharp
\equiv\frac{A_s^2}{404^2}\Psi_9^\sharp
\pmod p.
\tag{6.1}
\]

由 (3.3)：

\[
L_0^\sharp
\equiv
-5^M10^{M-1}
\frac{A_s^2}{404^2}\Psi_9^\sharp
\pmod p.
\tag{6.2}
\]

代入 (3.4)，得到只含两个 normalized source units 的 congruence：

\[
\boxed{
2c_u\sigma^\sharp a_2^2\,404^4
\equiv
5^\lambda
\left(5^M10^{M-1}\right)^2
A_s^4(\Psi_9^\sharp)^2
\pmod p.}
\tag{6.3}
\]

因此危险 source shell 已从原来的

\[
(x,y,r_s)\text{ + 两个 Hensel 深度}
\]
压成

\[
\boxed{
(\sigma^\sharp,\Psi_9^\sharp)
\text{ 的一个 quadratic congruence}.}
\tag{6.4}
\]

所有其它因子都是已知 unit 或平方尺度。

---

## 7. 对 parity 闭环的意义

结合 `spontaneous-angle-overlap-depth.md`：

- 若 `v_p(d)>h`，source angle valuation 精确为 `2h`，必偶；
- 若 `v_p(d)=h` 但 (3.4) 不成立，valuation 仍精确为 `2h`；
- source pool 只有在 (1.1)+(3.4) 同时成立时才可能贡献 angle residual odd parity。

所以 source residual odd-inert supplier 已严格缩成

\[
\boxed{
\begin{gathered}
v_p(d)=h,\\
v_p(\Phi_s)=2h,\quad v_p(\Psi_9)=h,\\
5^\lambda(L_0^\sharp)^2
=2c_u\sigma^\sharp a_2^2\pmod p.
\end{gathered}}
\tag{7.1}

下一步不能再靠普通 resultant；必须独立固定 `sigma^sharp` 或 `Phi^sharp` 的 square class，或者把 (6.3) 与 source length orbit / natural representative 做 higher-depth synchronization。本文保留该 gate 为真实开放项。

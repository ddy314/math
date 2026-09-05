# DD corrected terminal 的 pair-max gap-fiber rational reconstruction

> 日期：2026-08-22
>
> 依赖：[`dd-corrected-pairmax-short-suffix-reader-2026-08-22.md`](dd-corrected-pairmax-short-suffix-reader-2026-08-22.md)、[`dd-corrected-neighborhood-gap-fiber-entropy-2026-08-22.md`](dd-corrected-neighborhood-gap-fiber-entropy-2026-08-22.md)、[`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)、[`dd-corrected-carry-u-pairmax-crt-2026-08-22.md`](dd-corrected-carry-u-pairmax-crt-2026-08-22.md)。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` terminal neighborhood；fixed denominator/S-unit data）。**
>
> 前一 short-suffix theorem 已把每个 quantitative pair-max orientation 上的 `a_2` 固定到一个 residue modulo近 `S` 高度的 `v_2`，并留下 ratio congruence
> \[
> g_0a_2c_2
> \equiv
> 2\cdot5^T\iota_p c_3R_0
> \pmod{p^h}
> \qquad(p^h\Vert v_2).
> \]
> 本文不再把它只当作 `a_2` reader，而把它视为小 primitive gap fraction
> \[
> R_0/g_0
> \]
> 的 modular rational reconstruction。
>
> 聚合 Gaussian orientation 后，同一个 orientation fiber 中有
> \[
> \boxed{
> K_\Omega R_0\equiv A_2g_0\pmod{v_2},
> }
> \]
> 其中 `K_Omega` 是 `v_2`-unit。若有两个不同 reduced gap fractions，则 `v_2` 必整除它们的 Farey determinant；另一方面 gap-fiber defect bound使该 determinant 只有 `delta S+o(S)` 高度。于是只要
> \[
> \boxed{
> 1-C_{\rm one}\delta>\delta,
> }
> \]
> 就不可能存在两个不同 gap fibers。
>
> 这给显式阈值
> \[
> \boxed{
> \delta<\delta_{\rm gap}
> :=\frac1{1+C_{\rm one}}
> =\frac6{17+10\log_{10}2}
> =0.299845580176277\ldots.
> }
> \]
>
> 因为
> \[
> \delta_{UV}=0.238062349248111\ldots<\delta_{\rm gap},
> \]
> 原 `U × v_2` uniqueness neighborhood 内的最后一份正线性 numerator entropy——gap fiber `10^{\delta S}`——全部消失：
> \[
> \boxed{
> N_{\rm num}(S;\delta)=10^{o(S)}
> \qquad(\delta<\delta_{UV})
> }
> \]
> 对 fixed denominator/S-unit data 成立。

---

## 1. 已有的 oriented gap congruence

沿用 canonical notation
\[
F:=5^T,
\qquad
q_{\rm lcm}=\operatorname{lcm}(b_1,b_2,b_3),
\]
\[
c_2:=q_{\rm lcm}/b_2,
\qquad
c_3:=q_{\rm lcm}/b_3.
\]

quantitative large pair-max channel写
\[
V=v_1v_2,
\]
并对每个
\[
p^h\Vert v_2
\]
有 denominator pattern
\[
v_p(b_1)=r,
\qquad
v_p(b_2)=v_p(b_3)=r+h.
\]
因此
\[
\boxed{p\nmid c_2c_3.}
\tag{1.1}

`dd-corrected-neighborhood-pairmax-fixed-crt-2026-08-22.md` 还证明在这些 target primes 上
\[
\boxed{p\nmid g_0R_0 10.}
\tag{1.2}

pair-max Gaussian orientation可选择 Hensel root
\[
\iota_p^2\equiv-1\pmod{p^h}.
\]
前一 short-suffix theorem 已严格得到
\[
\boxed{
 g_0a_2c_2
 \equiv
 2F\iota_pc_3R_0
 \pmod{p^h}.}
\tag{Gap-p-local}

注意 `(1.1)--(1.2)` 说明右侧 coefficient
\[
2F\iota_pc_3
\]
是 `p`-unit。

---

## 2. 聚合成一个 modulo `v_2` 的 rational line

固定一个完整 Gaussian orientation vector
\[
\Omega=(\iota_p)_{p^h\Vert v_2}.
\]
不同 prime powers互素，所以 Chinese remainder theorem给唯一 residue
\[
\boxed{
\iota_\Omega\pmod{v_2}
}
\]
满足
\[
\iota_\Omega\equiv\iota_p\pmod{p^h}
\]
对所有 `p^h||v_2` 成立。

定义
\[
\boxed{
K_\Omega:=2F\iota_\Omega c_3,
\qquad
A_2:=a_2c_2.
}
\tag{2.1}

由 `(1.1)`：
\[
\boxed{(K_\Omega,v_2)=1.}
\tag{2.2}

逐 prime-power 聚合 `(Gap-p-local)`：
\[
\boxed{
K_\Omega R_0
\equiv
A_2g_0
\pmod{v_2}.}
\tag{Gap-v2-line}

所以固定 denominator/S-unit data、orientation `Omega` 与 short suffix `a_2` 后，所有合法 primitive gap fractions
\[
R_0/g_0,
\qquad(R_0,g_0)=1,
\]
都落在同一个 projective residue class modulo `v_2`。

---

## 3. 两个 gap fractions 强迫一个 `v_2`-deep Farey determinant

假设同一 fixed denominator/S-unit/orientation/`a_2` fiber 中存在两个合法 gap pairs
\[
(R_0,g_0),
\qquad
(R_0',g_0').
\]

由 `(Gap-v2-line)`：
\[
K_\Omega R_0\equiv A_2g_0\pmod{v_2},
\]
\[
K_\Omega R_0'\equiv A_2g_0'\pmod{v_2}.
\]
第一式乘 `g_0'`，第二式乘 `g_0`，相减：
\[
K_\Omega(R_0g_0'-R_0'g_0)
\equiv0\pmod{v_2}.
\]
由 `(2.2)` 可约去 `K_Omega`：
\[
\boxed{
 v_2\mid
 \Delta_{\rm gap}
 :=R_0g_0'-R_0'g_0.}
\tag{Gap-Farey-divisor}

若两个 reduced fractions不同，则
\[
\boxed{\Delta_{\rm gap}\ne0.}
\tag{3.1}
因为 `(R_0,g_0)=(R_0',g_0')=1` 且所有量为正整数；相同 rational number的最低项表示唯一。

这一步把 pair-max Gaussian orientation转成了一个 ordinary integer Farey determinant divisor。

---

## 4. determinant 的高度只有一份 `delta S`

`dd-corrected-neighborhood-gap-fiber-entropy-2026-08-22.md` 定义
\[
P_{\rm gap}
:=\frac1S\log_{10}\operatorname{core}_{10}(H_{\rm sph}-y_3),
\]
以及 rough overlap height
\[
R:=\frac1S\log_{10}\gamma_0.
\]
并证明每个 gap fiber满足
\[
\boxed{
\log_{10}R_0
\le P_{\rm gap}S+o(S),
}
\tag{4.1}
\[
\boxed{
\log_{10}g_0
\le RS+o(S),
}
\tag{4.2}
以及共同 defect budget
\[
\boxed{
P_{\rm gap}+R\le\delta+o(1).
}
\tag{4.3}

这里 fixed denominator/S-unit data下 `R` 固定。即使两个 numerator candidates对应不同的 `P_gap`，由 `(4.3)` 仍统一有
\[
P_{\rm gap},P_{\rm gap}'
\le\delta-R+o(1).
\]

因此两个 cross products分别满足
\[
\begin{aligned}
\log_{10}(R_0g_0')
&\le(P_{\rm gap}+R)S+o(S)\\
&\le\delta S+o(S),
\end{aligned}
\]
以及同样的
\[
\log_{10}(R_0'g_0)
\le\delta S+o(S).
\]

所以
\[
\boxed{
0<|\Delta_{\rm gap}|
\le10^{\delta S+o(S)}
}
\tag{Gap-Farey-height}
对任何两个不同 gap fractions成立。

这里至关重要的是：cross determinant只花 **一份** `P_gap+R` budget；不能把两个 candidates的 `R_0g_0` product bounds机械平方成 `2delta S`。

---

## 5. `v_2` 比 Farey determinant 更大时 gap fiber唯一

quantitative one-channel theorem给
\[
\boxed{
\frac{\log_{10}v_2}{S}
\ge
1-C_{\rm one}\delta-o(1),
}
\tag{5.1}
其中
\[
\boxed{
C_{\rm one}
=1+\frac{5(1+2a)}6
=2.335049992773302\ldots,
\qquad a:=\log_{10}2.
}
\tag{5.2}

若
\[
1-C_{\rm one}\delta>\delta,
\]
则 `(5.1)` 与 `Gap-Farey-height` 给 sufficiently large `S`：
\[
v_2>|\Delta_{\rm gap}|.
\]
但 `Gap-Farey-divisor` 又要求非零 `Delta_gap` 被 `v_2` 整除，矛盾。

所以此时同一个 fixed denominator/S-unit/orientation/`a_2` fiber 中 gap fraction至多一个。

解阈值：
\[
\boxed{
\delta
<\delta_{\rm gap}
:=\frac1{1+C_{\rm one}}.
}
\tag{5.3}
使用 `(5.2)`：
\[
1+C_{\rm one}
=2+\frac{5(1+2a)}6
=\frac{17+10a}{6},
\]
故
\[
\boxed{
\delta_{\rm gap}
=\frac6{17+10\log_{10}2}
=0.299845580176277\ldots.}
\tag{Gap-threshold}

于是：
\[
\boxed{
\delta<\delta_{\rm gap}
\Longrightarrow
\#\{(R_0,g_0)\mid
\text{fixed denominator/S-unit data, }\Omega,a_2\}
\le1.
}
\tag{Gap-fiber-unique}

---

## 6. short suffix已经在更宽 neighborhood 中唯一

前一 short-suffix theorem证明
\[
\boxed{
\delta<\delta_{a_2}
:=0.322366428371977\ldots
}
\]
时，每个 orientation vector `Omega` 的合法 digit interval中至多一个 `a_2`。

而
\[
\boxed{
\delta_{\rm gap}
=0.299845580176277\ldots
<\delta_{a_2}.
}
\tag{6.1}

所以整个 `delta<delta_gap` neighborhood内，对 fixed denominator/S-unit data 与 fixed orientation：

1. `a_2` 至多一个；
2. 随后 `(R_0,g_0)` 至多一个。

orientation vectors 总数仍由前一 theorem 控制：
\[
\boxed{
2^{\omega(v_2)}=10^{o(S)}.}
\tag{6.2}

因此 fixed denominator/S-unit data 下：
\[
\boxed{
\#\{(\Omega,a_2,R_0,g_0)\}
=10^{o(S)}
\qquad(\delta<\delta_{\rm gap}).
}
\tag{Gap-orientation-collapse}

原 gap-fiber count
\[
10^{\delta S+o(S)}
\]
在这个 neighborhood 中被完全消去。

---

## 7. 与 `U × v_2` period 合并后的 numerator entropy

`dd-corrected-carry-u-pairmax-crt-2026-08-22.md` 给 fixed `(R_0,g_0,a_2)` fiber
\[
\#\{A_{12}\}
\le
10^{[C_{UV}\delta-U_*]_+S+o(S)},
\tag{7.1}
其中
\[
\boxed{
C_{UV}=2+3a
=2.903089986991944\ldots,
}
\]
\[
\boxed{
U_*=0.691116422381969\ldots.
}
\]

由 `Gap-orientation-collapse`，当
\[
\delta<\delta_{\rm gap}
\]
时，fixed denominator/S-unit data 下全部 numerator candidates满足改进后的全局计数
\[
\boxed{
N_{\rm num}(S;\delta)
\le
10^{[C_{UV}\delta-U_*]_+S+o(S)}.
}
\tag{Numerator-after-gap-lattice}

特别地 `U × v_2` uniqueness threshold为
\[
\boxed{
\delta_{UV}
:=\frac{U_*}{C_{UV}}
=0.238062349248111\ldots,
}
且
\[
\delta_{UV}<\delta_{\rm gap}.
\]
因此
\[
\boxed{
N_{\rm num}(S;\delta)
=10^{o(S)}
\qquad
(\delta<0.238062349248111\ldots)
}
\tag{Numerator-subexponential}
对 fixed denominator/S-unit data成立。

这严格加强前一 short-suffix theorem 的
\[
N_{\rm num}\le10^{\delta S+o(S)}.
\]

---

## 8. 方法边界

本文使用的 pair-max depth已在 sphere orientation中支付；这里仅把它转成 modular rational reconstruction / candidate uniqueness，不把 `v_2` 再作为新的 local height payer。

`Numerator-subexponential` 也没有直接产生 strict slope gap，因为 denominator/S-unit data本身仍可指数移动。它完成的是当前 numerator side 的一个明确缺口：

\[
\boxed{
\text{在 }\delta<\delta_{UV}\text{ 内，fixed denominator/S-unit fiber 的 numerator entropy已降到 }o(S).
}
\]

因此下一步可以把注意力完全移到 denominator/S-unit family：
\[
\boxed{
Q=Uq,
\qquad
b_3=BVq,
\qquad
2^HZ-5^TU=V,
\qquad
V=v_1v_2.
}
\]

尤其值得研究：

1. `b_2=v_2·10^{O(delta S)+o(S)}` 与 decimal concat `Q=b_1 10^{m_2}+b_2` 的 global compatibility；
2. `U,Z` 的 near-critical product `UZ=10^{S+O(delta S)}` 与 `Q=Uq` 的 source quotient位置；
3. split-prime orientation choices是否能与 long decimal block `b_2` 的 digit shell同时保持指数多种可能。

这些已经是 denominator-side 问题，不再需要继续扩大 numerator CRT 列表。

---

## 9. verification scope

配套有限审计：

```bash
uv run python scripts/exact-lift/double-deficit/research-checks/tail/check_dd_corrected_gap_fiber_pairmax_rational_reconstruction.py
```

脚本只检查：

- 常数 `delta_gap=1/(1+C_one)` 与各 neighborhood 阈值的数值顺序；
- small Farey model 中，当 modulus严格大于 cross-determinant box时，同一 modular projective residue class中 reduced positive fraction至多一个；
- `Numerator-after-gap-lattice` 的 exponent bookkeeping。

无界证明来自正文；有限枚举不承担全局覆盖。

---

## 10. 状态摘要

- **已严格完成：** oriented local gap congruence聚合成 `Gap-v2-line`。
- **已严格完成：** two-gap `Gap-Farey-divisor`。
- **已严格完成：** cross determinant只消耗一份 `P_gap+R`，得到 `Gap-Farey-height`。
- **已严格完成：** gap uniqueness threshold `delta_gap=0.299845580176277...`。
- **已严格完成：** `delta<delta_gap` 时 gap/suffix fibers只有 `10^{o(S)}` orientation entropy。
- **已严格完成：** `delta<delta_UV=0.238062349248111...` 时 fixed denominator/S-unit data 下完整 numerator entropy为 `10^{o(S)}`。
- **仍待证：** denominator/S-unit entropy；unique-lift digit-shell exclusion；explicit strict slope gap；DD emptiness与有效绝对高度界。

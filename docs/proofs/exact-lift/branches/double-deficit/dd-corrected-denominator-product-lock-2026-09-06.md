# DD corrected terminal 的 denominator `qZ` product lock 与 fixed-`v_2` residual core

> 日期：2026-09-06
>
> 依赖：[`dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md`](dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md)、[`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)、[`dd-corrected-gap-fiber-pairmax-rational-reconstruction-2026-08-22.md`](dd-corrected-gap-fiber-pairmax-rational-reconstruction-2026-08-22.md)、[`dd-corrected-terminal-denominator-sunit-entropy-2026-08-22.md`](dd-corrected-terminal-denominator-sunit-entropy-2026-08-22.md)。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` terminal neighborhood 的 denominator-side reconstruction theorem）。**
>
> 本文不宣称 DD 为空，也不把已有 pair-max 高度重复计费。它处理此前 denominator-side frontier 中明确留下的
> \[
> b_2=v_2\cdot10^{O(\delta S)+o(S)},\qquad
> Q=b_1 10^{m_2}+b_2,\qquad Q=Uq
> \]
> 与 S-unit phase 的 global compatibility。结论是：在一个显式正宽度 terminal neighborhood 内，long pair-max core `v_2` 会把原本两个 source variables `q,Z` 压成一个 **唯一的小整数乘积** `qZ`。因此固定 `v_2` 后，完整 denominator/S-unit fiber 的正线性自由度只剩短 decimal head `b_1`；再接已有 numerator reconstruction 后，fixed-`v_2` 的完整 Exact-Lift candidate family 只有
> \[
> 10^{\kappa_{\rm dig}\delta S+o(S)}
> \]
> 个。

---

## 1. 输入与常数

记

\[
a:=\log_{10}2,
\qquad
\lambda:=\frac{2+a}{1+2a},
\]

\[
U_*:=0.691116422381969\ldots,
\qquad
z_*:=1-U_*=0.308883577618031\ldots.
\]

quantitative digit polarization 的短块常数为

\[
\boxed{
\kappa_{\rm dig}=\frac{2+a}{3}
=0.767009998554660\ldots.}
\tag{1.1}
\]

one-channel lower 为

\[
\boxed{
\frac{\log_{10}v_2}{S}
\ge1-C_{\rm one}\delta-o(1),
}
\tag{1.2}
\]

其中

\[
\boxed{
C_{\rm one}
=1+\frac{5(1+2a)}6
=2.335049992773302\ldots.}
\tag{1.3}
\]

`U/Z` neighborhood 给

\[
\boxed{
\frac{\log_{10}U}{S}
\ge
U_*-(1+a)\delta-o(1),
}
\tag{1.4}
\]

以及

\[
\boxed{
\frac{\log_{10}Z}{S}
\le
z_*+C_Z\delta+o(1),
}
\tag{1.5}
\]

其中

\[
\boxed{
C_Z:=2a+\frac12+\frac1{2\lambda}
=1.450178006813822\ldots.}
\tag{1.6}
\]

同时 prefix denominator concat `Q` 是 `S=m_1+m_2` 位正整数，因此

\[
Q<10^S.
\tag{1.7}
\]

---

## 2. `qZ` 的 uniform upper

由

\[
Q=Uq
\]

及 `(1.4),(1.7)`：

\[
\begin{aligned}
\frac{\log_{10}q}{S}
&<1-\frac{\log_{10}U}{S}\\
&\le z_*+(1+a)\delta+o(1).
\end{aligned}
\]

故

\[
\boxed{
\frac{\log_{10}(qZ)}{S}
\le
2z_*+C_{qZ}\delta+o(1),
}
\tag{2.1}
\]

其中

\[
\boxed{
C_{qZ}:=(1+a)+C_Z
=\frac32+3a+\frac1{2\lambda}
=2.751208002477803\ldots.}
\tag{2.2}
\]

与 `(1.2)` 比较，定义

\[
\boxed{
\delta_{qZ}
:=
\frac{1-2z_*}{C_{\rm one}+C_{qZ}}
=0.075150109396892\ldots.}
\tag{2.3}
\]

于是对任意 fixed

\[
\boxed{0\le\delta<\delta_{qZ},}
\tag{2.4}
\]

存在只依赖该 fixed margin 的 `S_0`，使所有 `S>=S_0` 的 candidate 满足

\[
\boxed{0<qZ<v_2.}
\tag{Small-product}
\]

这里使用的是严格正 margin

\[
1-2z_*-(C_{\rm one}+C_{qZ})\delta>0.
\]

---

## 3. denominator concat 与 S-unit 给同一个 modulo `v_2` 的 product residue

corrected canonical phase中

\[
\boxed{Q=Uq,}
\tag{3.1}
\]

\[
\boxed{Q=b_1 10^{m_2}+b_2,}
\tag{3.2}
\]

\[
\boxed{2^HZ-5^TU=V=v_1v_2,}
\tag{3.3}
\]

并且

\[
\boxed{v_2\mid b_2.}
\tag{3.4}
\]

由 `(3.1)--(3.2),(3.4)`：

\[
\boxed{
Uq\equiv b_1 10^{m_2}\pmod{v_2}.}
\tag{3.5}
\]

由 `(3.3)`：

\[
\boxed{
2^HZ\equiv5^TU\pmod{v_2}.}
\tag{3.6}
\]

将 `(3.6)` 乘 `q`，再用 `(3.5)` 消去 `Uq`：

\[
\boxed{
2^HqZ
\equiv
5^Tb_1 10^{m_2}
\pmod{v_2}.}
\tag{Product-congruence}
\]

canonical one-channel 中 `(V,10)=1`，而 `v_2|V`，故

\[
(v_2,2)=1.
\]

因此 `2^H` 在 modulo `v_2` 下可逆。定义 least nonnegative residue

\[
\boxed{
\rho_{v_2}
:=
\left[
2^{-H}5^Tb_1 10^{m_2}
\right]_{v_2},
\qquad
0\le\rho_{v_2}<v_2.
}
\tag{3.7}
\]

则 `(Product-congruence)` 等价于

\[
\boxed{qZ\equiv\rho_{v_2}\pmod{v_2}.}
\tag{3.8}
\]

---

## 4. small-product residue lock

在 `delta<delta_qZ` 中，`(Small-product)` 与 `(3.8)` 同时成立：

\[
0<qZ<v_2,
\qquad
0\le\rho_{v_2}<v_2.
\]

同一 residue class 在 `[0,v_2)` 内只有一个代表，所以立即得到 exact equality

\[
\boxed{
qZ=\rho_{v_2}.}
\tag{qZ-product-lock}
\]

特别地，若右侧 residue 为 `0`，则该 denominator data 直接不可能产生 candidate。

这一步没有使用概率、均匀分布或 finite search；它只是把已有 global identities 与严格 height separation 联立。

---

## 5. fixed `v_2,b_1` 后 `(q,Z)` 只有 divisor entropy

固定

\[
(v_2,b_1,H,T,m_2)
\]

以及 terminal combinatorial/exponent layer。由 `(qZ-product-lock)`，整数

\[
N_{qZ}:=qZ=\rho_{v_2}
\]

已经唯一确定。

因此所有可能的 ordered positive pairs `(q,Z)` 都来自 `N_qZ` 的 divisor pairs，数目至多

\[
\boxed{\tau(N_{qZ}).}
\tag{5.1}
\]

由于 `N_qZ<v_2<=10^{O(S)}`，标准 divisor bound 给

\[
\boxed{
\tau(N_{qZ})=10^{o(S)}.}
\tag{5.2}
\]

所以原本 Farey/projective side 的两个 moving integers `q,Z`，在 fixed long-core residue fiber 中已经没有 positive-linear entropy。

---

## 6. fixed `v_2,b_1` 后整个 denominator/S-unit data 只有 `10^{o(S)}`

one-channel decomposition 还有

\[
V=v_1v_2,
\qquad
v_1\mid b_1.
\tag{6.1}
\]

固定 `b_1` 后，`v_1` 只有

\[
\tau(b_1)=10^{o(S)}
\]

种可能。

对每个 `(q,Z,v_1)`，令

\[
V=v_1v_2.
\]

S-unit identity `(3.3)` 唯一给出候选

\[
\boxed{
U=\frac{2^HZ-V}{5^T}.}
\tag{6.2}
\]

若右侧不是正整数则该分支立即淘汰。若合法，则

\[
Q=Uq
\]

唯一，并由 decimal concat 唯一恢复

\[
\boxed{
b_2=Q-b_1 10^{m_2}.}
\tag{6.3}
\]

再检查 `b_2>0`、digit length 与 `v_2|b_2`。若通过，置

\[
t_1=b_1/v_1,
\qquad
t_2=b_2/v_2,
\qquad
\gamma=t_1t_2;
\]

则

\[
b_1b_2=\gamma V
\]

自动恢复。固定 `(m,T)` 时 smooth factor

\[
B=\frac{10^m}{2\cdot5^T}
\]

唯一，第三分母再由已有 exact identity

\[
\boxed{b_3=BVq}
\tag{6.4}
\]

唯一恢复或因 integrality/digit test 淘汰。

因此：

\[
\boxed{
N_{\rm den/SU}
\bigm|
(v_2,b_1,\text{exponent layer})
=10^{o(S)}
\qquad(\delta<\delta_{qZ}).}
\tag{Fixed-v2-b1-collapse}
\]

所有 exponent coordinates 都是 `O(S)` 的整数；允许它们在 fixed terminal window 内移动只带来 `S^{O(1)}=10^{o(S)}` 的额外 multiplicity。

---

## 7. fixed `v_2` 后只剩短 decimal head 的正线性自由度

quantitative digit polarization 已给

\[
\boxed{
m_1\le\kappa_{\rm dig}\delta S+o(S).}
\tag{7.1}
\]

所以 fixed `v_2` 后，枚举所有合法 `b_1` 的最粗整数上界已经是

\[
\#\{b_1\}
\le10^{\kappa_{\rm dig}\delta S+o(S)}.
\]

与 `(Fixed-v2-b1-collapse)` 合并：

\[
\boxed{
N_{\rm den/SU}
\bigm|
v_2
\le
10^{\kappa_{\rm dig}\delta S+o(S)}
\qquad(\delta<\delta_{qZ}).}
\tag{Fixed-v2-den-entropy}
\]

数值即

\[
\boxed{
N_{\rm den/SU}
\bigm|
v_2
\le
10^{0.767009998555\,\delta S+o(S)}.}
\tag{7.2}
\]

在 equality-scale limit `delta->0` 中，fixed-`v_2` denominator/S-unit fiber 因而退化为 `10^{o(S)}`。

---

## 8. 接上已有 numerator collapse：fixed `v_2` 的完整 candidate fiber

已有 pair-max rational reconstruction 与 `U × v_2` reconstruction 给

\[
N_{\rm num}(S;\delta)
=10^{o(S)}
\qquad
(\delta<\delta_{UV}),
\]

其中

\[
\delta_{UV}=0.238062349248111\ldots.
\]

而

\[
\delta_{qZ}=0.075150109396892\ldots<\delta_{UV}.
\]

故在本文 neighborhood 中，denominator reconstruction 之后的 numerator multiplicity仍只有 `10^{o(S)}`。于是完整 Exact-Lift candidate fiber满足

\[
\boxed{
N_{\rm full}
\bigm|
v_2
\le
10^{\kappa_{\rm dig}\delta S+o(S)}
\qquad(\delta<\delta_{qZ}).}
\tag{Fixed-v2-full-residual}
\]

因此 corrected terminal near-frontier 的 residual positive-linear freedom可以进一步定位为：

\[
\boxed{
\text{long one-channel core }v_2
\quad+\quad
\text{short decimal head }b_1.
}
\tag{Residual-core}
\]

固定 long core 后，其余 S-unit、source product、factor assignment、gap、orientation 与 numerator data均不再携带独立 `S`-scale entropy。

---

## 9. no-double-count 与方法边界

`(Product-congruence)` 只由

\[
Q=Uq,
\quad
Q=b_1 10^{m_2}+b_2,
\quad
v_2|b_2,
\quad
2^HZ-5^TU=v_1v_2
\]

消元得到，所以它不是新的 local height payer；本文使用它的方式是 **reconstruction**：已有 height windows 先证明 `qZ<v_2`，随后一个 modular residue 变成 ordinary integer equality。

因此不得把 `v_2` 在 pair-max/Gaussian ledger 中的高度再次与 `(qZ-product-lock)` 相加收费。

本文仍没有控制 `v_2` 本身在所有 denominator/S-unit candidates 中的 global movement，也没有把 residual long-core family与 decimal top-residue / split-prime digit shell 做最终不相容比较。安全结论是：

\[
\boxed{
\text{在 }\delta<0.075150109396892\ldots
\text{ 内，fixed-}v_2\text{ fiber 已降到短块尺度；}
}
\]

而不是 DD 全局为空或已经得到 strict slope gap。

---

## 10. 下一主目标

经过本文，terminal denominator-side 的下一目标可以缩成单一问题：

\[
\boxed{
\text{控制 long pair-max core }v_2
\text{ 的 global decimal/split-prime movement。}
}
\]

优先可尝试把 `(qZ-product-lock)` 与以下已经存在的两个独立坐标联立：

1. `b_2=v_2 t_2` 且 `t_2=10^{O(\delta S)+o(S)}` 的 long decimal-block shell；
2. numerator `Top-residue` 的 exponentially thin decimal cell。

若能证明 `v_2` 的 admissible residue family本身只有 `10^{o(S)}` 或与上述 decimal cell不相容，则当前 terminal neighborhood 会从 fixed-core collapse 升级为真正的 strict-gap/emptiness statement。

---

## 11. verification scope

配套机械审计：

```bash
uv run python scripts/exact-lift/double-deficit/research-checks/tail/check_dd_corrected_denominator_product_lock.py
```

脚本只检查：

- `C_qZ`、`C_one`、`delta_qZ` 的常数计算与阈值顺序；
- toy exact identities 中 `(Product-congruence)`；
- `qZ<v_2` 时 least-residue lock 的有限 sanity check。

无界 theorem 来自正文的现有 quantitative windows、exact congruence 与 divisor bound；有限脚本不承担 asymptotic coverage。

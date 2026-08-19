# A2 equal-depth resonance 的 canonical gcd ladder

> **依赖：** `spontaneous-height-equal-depth-tail-imbalance.md`、`spontaneous-height-equal-depth-tail-source-separation.md`、`primitive-reduction.md`。
>
> **严格状态：**本文研究上一层留下的 `gcd(Gamma,Lambda_tail)`。在当前 genuine non-`3` denominator-separated height sector，tail equation `Lambda_tail=A omega^circ+B W^circ` 的两个固定 coefficient `A=2E_MNS`、`B=TQ^2` 都是 p-adic units。由此证明：若 `e=v_p(omega)` 与 `h=v_p(W_q)` 不相等，则抽掉共同 `Gamma` 后恰有一个 imbalance factor仍含 `p`，另一个为 unit，故 `p` 不可能整除 `Lambda_tail`；若 `e=h`，则 `v_p(Lambda_tail)=rho_p`。因此 `gcd(Gamma,Lambda_tail)` 在 genuine sector 精确选择 equal-depth 且 `rho_p>0` 的 resonant common primes。进一步定义 `D_k=gcd(Gamma^k,Lambda_tail)`，其 p-depth 恰为 `min(kh,rho_p)`，从而形成一个不需要事先枚举 target primes 的 canonical resonance-depth ladder。本文仍不证明该 ladder 为空，因此不关闭 A2。

---

## 1. 记号与 genuine coefficient separation

令

\[
e:=v_p(\omega),
\qquad
h:=v_p(W_q),
\qquad
\gamma:=\min(e,h).
\tag{1.1}
\]

沿用

\[
\Gamma=\gcd(\omega,W_q),
\]
所以

\[
v_p(\Gamma)=\gamma.
\tag{1.2}
\]

以及

\[
\omega^\circ=\omega/\Gamma,
\qquad
W^\circ=W_q/\Gamma.
\]
故

\[
\boxed{
v_p(\omega^\circ)=e-\gamma,
\qquad
v_p(W^\circ)=h-\gamma.}
\tag{1.3}
\]

本文只讨论当前 oversaturation 分析中已经分离出的 genuine non-`3` height sector；这里

\[
\boxed{p\nmid2E_MNSTQ.}
\tag{1.4}
\]

特别地，tail equation

\[
\boxed{
\Lambda_{\rm tail}
=A\omega^\circ+B W^\circ,
\qquad
A:=2E_MNS,
\quad
B:=TQ^2}
\tag{1.5}
\]

中的 `A,B` 都是 p-units。

---

## 2. unequal-depth common prime 不可能进入 tail

先设

\[
e>h.
\]

则 `gamma=h`，由 (1.3)：

\[
v_p(\omega^\circ)=e-h>0,
\qquad
v_p(W^\circ)=0.
\]

由 (1.4)、(1.5)：

\[
\Lambda_{\rm tail}
\equiv BW^\circ\not\equiv0\pmod p.
\]
所以

\[
\boxed{e>h\Longrightarrow v_p(\Lambda_{\rm tail})=0.}
\tag{2.1}
\]

同理若

\[
h>e,
\]
则 `omega^circ` 为 unit、`W^circ` 被 p 整除，因此

\[
\Lambda_{\rm tail}
\equiv A\omega^\circ\not\equiv0\pmod p,
\]
即

\[
\boxed{h>e\Longrightarrow v_p(\Lambda_{\rm tail})=0.}
\tag{2.2}
\]

合并：

\[
\boxed{
e\ne h
\Longrightarrow
v_p(\Lambda_{\rm tail})=0.}
\tag{2.3}
\]

这是一个比旧 residual-depth cap 更直接的 global quotient statement：所有 unequal-depth common primes 在 canonical tail quotient 中完全消失。

---

## 3. equal-depth prime 的 tail depth 恰为 `rho_p`

若

\[
e=h\ge1,
\]
则

\[
\gamma=h,
\qquad
p\nmid\omega^\circ W^\circ.
\]

`spontaneous-height-equal-depth-tail-normalization.md` 已证明

\[
\boxed{
v_p(\Lambda_{\rm tail})=\rho_p.}
\tag{3.1}
\]

所以在 genuine common-prime sector：

\[
\boxed{
 v_p(\Lambda_{\rm tail})
 =
 \begin{cases}
 0,&e\ne h,\\[1mm]
 \rho_p,&e=h.
 \end{cases}}
\tag{3.2}
\]

这已经把 equal/unequal depth dichotomy 内置进一个单一 canonical integer。

---

## 4. `gcd(Gamma,Lambda_tail)` 是 first resonance selector

定义

\[
\boxed{
D_{\rm res}:=\gcd(\Gamma,\Lambda_{\rm tail}).}
\tag{4.1}
\]

若 `e!=h`，由 (2.3)：

\[
v_p(D_{\rm res})=0.
\]

若 `e=h>=1`，由 (1.2)、(3.1)：

\[
v_p(D_{\rm res})
=\min(h,\rho_p).
\]

所以

\[
\boxed{
 v_p(D_{\rm res})
 =
 \begin{cases}
 0,&e\ne h,\\[1mm]
 \min(h,\rho_p),&e=h.
 \end{cases}}
\tag{4.2}
\]

特别地：

\[
\boxed{
p\mid D_{\rm res}
\Longleftrightarrow
e=h\ge1
\text{ 且 }\rho_p>0}
\tag{4.3}
\]

对当前 genuine sector成立。

因此 `D_res` 无需预先知道哪些 common primes 是 equal-depth，也无需逐 prime 计算 `omega_0,W_0`；一个普通整数 gcd 就能选择 first resonant support。

---

## 5. `Gamma^k` gcd ladder 读取更深 tail

对整数

\[
k\ge1
\]
定义

\[
\boxed{
D_k:=\gcd(\Gamma^k,\Lambda_{\rm tail}).}
\tag{5.1}
\]

若 `e!=h`，仍由 (2.3)：

\[
v_p(D_k)=0.
\]

若 `e=h`，则

\[
v_p(\Gamma^k)=kh,
\qquad
v_p(\Lambda_{\rm tail})=\rho_p.
\]
所以

\[
\boxed{
 v_p(D_k)
 =
 \begin{cases}
 0,&e\ne h,\\[1mm]
 \min(kh,\rho_p),&e=h.
 \end{cases}}
\tag{5.2}
\]

因此对 fixed equal-depth prime，随着 `k` 增长：

\[
\min(h,\rho_p),
\min(2h,\rho_p),
\min(3h,\rho_p),\ldots
\]

逐层恢复完整 `rho_p`。

---

## 6. ladder 的 successive quotient

令

\[
\boxed{
E_k:=D_{k+1}/D_k.}
\tag{6.1}
\]

因为 `D_k|D_{k+1}`，这是整数。

对 equal-depth prime：

\[
\begin{aligned}
v_p(E_k)
&=\min((k+1)h,\rho_p)-\min(kh,\rho_p).
\end{aligned}
\tag{6.2}
\]

所以：

- 若 `rho_p<=kh`，则 `v_p(E_k)=0`；
- 若 `kh<rho_p<(k+1)h`，则 `v_p(E_k)=rho_p-kh`；
- 若 `rho_p>=(k+1)h`，则 `v_p(E_k)=h`。

因此 `E_k` 正好记录 resonance tail 穿过第 `k` 个 baseline-height block 时的新深度。

---

## 7. stable gcd 等于 `Gamma`-supported full tail

因为 `Lambda_tail` 是固定正整数，存在有限 `k_0` 使得

\[
\Gamma^{k_0}
\]

在每个 `p|Gamma` 上的 exponent 都不小于 `v_p(Lambda_tail)`。
于是

\[
D_k=D_{k_0}
\qquad(k\ge k_0).
\]

稳定值

\[
\boxed{
D_\infty:=D_{k_0}}
\tag{7.1}
\]

就是 `Lambda_tail` 的 `Gamma`-primary part。

在当前 genuine sector，它的 non-`3` prime valuations 精确为：

\[
\boxed{
 v_p(D_\infty)
 =
 \begin{cases}
 0,&e\ne h,\\[1mm]
 \rho_p,&e=h.
 \end{cases}}
\tag{7.2}
\]

所以 full equal-depth resonance tail 已经可以通过普通整数 gcd ladder 恢复，不需要显式 factorization 才能定义。

---

## 8. 与 oversaturation target 的关系

本文的 `D_res,D_k,D_infty` 选择的是所有 genuine equal-depth resonant common primes；height companion oversaturation target 还额外满足 parent 文件的 `B_W/J_H` 条件，例如

\[
\mathcal P_{\omega H}(K)
=6K^2-36K+55
\equiv0\pmod p.
\]

因此本文没有把“resonant common prime”与“oversaturation target”混为一谈。

真正 target pool 可在 gcd ladder 基础上再与 fixed quadratic / companion carriers 取交；但 unequal-depth common primes 已经由 (2.3) 自动从 ladder 中消失。

---

## 9. 当前 frontier

现在 equal-depth analysis 有一个无需 prime list 的 canonical pipeline：

\[
\boxed{
\begin{aligned}
\omega&=\gcd(\alpha,\beta),\\
\Gamma&=\frac{\gcd(\alpha,\Lambda_{\rm dec})}{\gcd(\alpha,\beta)},\\
\Lambda_{\rm tail}
&=\frac{\Lambda_{\rm dec}}{\gcd(\alpha,\Lambda_{\rm dec})},\\
D_k&=\gcd(\Gamma^k,\Lambda_{\rm tail}).
\end{aligned}}
\tag{9.1}
\]

其中 genuine non-`3` common primes 的 unequal-depth sector完全不进入 `D_k`；equal-depth resonance 则由 ladder 精确读取。

所以接下来真正需要攻击的对象已经从 moving p-adic unit ratio 压成整数序列

\[
\boxed{D_1,D_2,\ldots,D_\infty.}
\tag{9.2}
\]

下一步应把该 ladder 与 `P_omegaH(K)` 的 target selector、`C_alpha` 的小 residue，或 `J_H/H_pref` 的 `4M+1` 位 carriers 联立，尝试证明 target part of `D_infty` 为空或高度不足。
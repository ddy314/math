# DD corrected S-unit phase 的 Euclidean remainder lock

> 日期：2026-09-06
>
> 依赖：[`dd-corrected-high-funnel-quantitative-defect-2026-08-22.md`](dd-corrected-high-funnel-quantitative-defect-2026-08-22.md)、[`dd-corrected-terminal-digit-polarization-2026-08-22.md`](dd-corrected-terminal-digit-polarization-2026-08-22.md)、[`dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md`](dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md)、[`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)、[`dd-corrected-terminal-rough-source-sharp-2026-08-22.md`](dd-corrected-terminal-rough-source-sharp-2026-08-22.md)、[`dd-corrected-schmidt-farey-slack-2026-08-22.md`](dd-corrected-schmidt-farey-slack-2026-08-22.md)。
>
> **严格状态：已严格完成（整个 corrected canonical `t_2=1` quantitative one-channel neighborhood `delta<=1/2`）。**
>
> canonical S-unit equation为
> \[
> \boxed{2^HZ-5^TU=V,\qquad (UVZ,10)=1.}
> \]
> 过去主要把它视为 `Z/U` 对 `5^T/2^H` 的 Farey approximation。本文保留 quantitative defects 的共享预算，证明在整个 one-channel neighborhood 中其实有
> \[
> \boxed{0<Z<5^T,\qquad 0<V<5^T.}
> \]
> 因此上式同时是一条 ordinary Euclidean division identity：
> \[
> \boxed{
> U=\left\lfloor\frac{2^HZ}{5^T}\right\rfloor,
> \qquad
> V=2^HZ\bmod5^T.}
> \]
> 又因 `2^H` 是 modulo `5^T` 的 unit 且 `0<Z<5^T`，有
> \[
> \boxed{Z=[2^{-H}V]_{5^T}.}
> \]
> 所以固定 `(H,T,V)` 后，整个 S-unit pair `(U,Z)` **至多一个**。这不使 Farey/Schmidt slack自动消失，因为 `V` 本身仍可移动；它把 residual projective freedom从 two-variable Farey pair重新定位为 single remainder coordinate `V`。

---

## 1. constants 与 uncoarsened identities

令

\[
a:=\log_{10}2,
\qquad b:=1-a=\log_{10}5,
\]

\[
A:=\frac{2(1+2a)}3,
\qquad
\lambda:=\frac{2+a}{1+2a},
\]

\[
M_*:=2.808883577618031\ldots,
\qquad
z_*:=0.308883577618031\ldots,
\]

并写

\[
\delta:=c_*-\frac nS,
\qquad
\mu:=M_*-\frac mS.
\]

terminal geometry 已给

\[
\boxed{0\le\mu\le\delta+o(1).}
\tag{1.1}
\]

5-resonance为

\[
\boxed{
\frac TS
=\frac{2M+2Q_5-2G_5+N_5}{3}.}
\tag{1.2}
\]

所以

\[
\frac1S\log_{10}5^T
=b\frac TS
\]

的 frontier baseline为

\[
\boxed{
T_{5,*}:=\frac{2bM_*}{3}
=1.308883577618031\ldots
=1+z_*.}
\tag{1.3}

`Z` 的 uncoarsened identity为

\[
\boxed{
\frac{\log_{10}Z}{S}-z_*
=2a\mu-2aQ_2-aN_2+aG_2-bG_5-R+o(1).}
\tag{1.4}

quantitative digit proof在粗化前给 short denominator

\[
\boxed{
\begin{aligned}
\frac{m_1}{S}
\le{}&\frac\delta2
-\left(1-\frac b3\right)\mu
-\frac b3Q_5
+\frac b3G_5\\
&-\frac b6N_5
+\frac R2+o(1),
\end{aligned}}
\tag{m1-sharp}
\]

而 two-adic reader给

\[
\boxed{
aG_2\le\frac{m_1}{S}+aQ_2+o(1).}
\tag{G2-via-m1}
\]

最后沿用 exact normalized Schmidt relation

\[
\boxed{
A\mu
=\sigma_S+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)+2R+o(1).}
\tag{Mu-budget}
\]

---

## 2. `Z` 比 `5^T` 小一个整 `S` baseline

由 `(1.2)--(1.4)`：

\[
\begin{aligned}
\frac1S\log_{10}\frac{5^T}{Z}-1
={}&-\left(\frac{2b}{3}+2a\right)\mu
+2aQ_2+aN_2-aG_2\\
&+\frac{2b}{3}Q_5
+\frac b3G_5
+\frac b3N_5+R+o(1).
\end{aligned}
\tag{2.1}

这里使用了 `T_{5,*}-z_*=1`。

由 `(G2-via-m1)`：

\[
-aG_2\ge-\frac{m_1}{S}-aQ_2-o(1).
\]

代入 `(m1-sharp)` 后，`G_5` 精确 cancellation，并得到

\[
\boxed{
\begin{aligned}
\frac1S\log_{10}\frac{5^T}{Z}-1
\ge{}&-\frac\delta2-a\mu
+aQ_2+aN_2+bQ_5\\
&+\frac b2N_5+\frac R2-o(1).
\end{aligned}}
\tag{2.2}

将 `(Mu-budget)` 代入 `-a mu`。其中可能给 lower bound造成损失的只有 `sigma_S,G_5,R` 三项；其 loss/quantitative-defect cost ratios分别为

\[
\frac{a/A}{\lambda}
=0.196236030971719\ldots,
\]

\[
\frac{4ab/(3A)}{2b(2\lambda-1)/3}
=\boxed{a=0.301029995663981\ldots,}
\]

\[
\frac{2a/A-1/2}{2\lambda-1}
=0.034019997109321\ldots.
\]

最大者恰为 `a`。因此同一份 quantitative defect budget统一给

\[
\boxed{
\frac1S\log_{10}\frac{5^T}{Z}
\ge
1-\left(\frac12+a\right)\delta-o(1).}
\tag{Five-over-Z}

数值上

\[
\frac12+a
=0.801029995663981\ldots.
\]

在现行 one-channel 作用域

\[
0\le\delta\le\frac12
\]

中，右侧至少趋向

\[
1-0.400514997831991>0.
\]

故 sufficiently large `S` 上统一有

\[
\boxed{0<Z<5^T.}
\tag{Z-below-five}

---

## 3. `V` 同样严格小于 `5^T`

canonical `G=gamma V` 与 `log G/S=1+o(1)` 给

\[
\boxed{
\frac{\log_{10}V}{S}
=1-aG_2-bG_5-R+o(1).}
\tag{3.1}

另一方面由 `(1.2)`：

\[
\frac1S\log_{10}5^T-T_{5,*}
=-\frac{2b}{3}\mu
+\frac{2b}{3}Q_5
-\frac{2b}{3}G_5
+\frac b3N_5.
\]

两式相减，并使用 `T_{5,*}-1=z_*`：

\[
\begin{aligned}
\frac1S\log_{10}\frac{5^T}{V}
={}&z_*
-\frac{2b}{3}\mu
+aG_2+rac{2b}{3}Q_5\\
&+rac b3G_5+rac b3N_5+R+o(1).
\end{aligned}
\tag{3.2}

除 `mu` 外所有显示项均非负。由 `(1.1)`：

\[
\boxed{
\frac1S\log_{10}\frac{5^T}{V}
\ge
z_*-rac{2b}{3}\delta-o(1).}
\tag{Five-over-V}

在 `delta<=1/2` 时右侧下界为

\[
z_*-rac b3
=0.075893579064050\ldots>0.
\]

因此 sufficiently large `S` 上：

\[
\boxed{0<V<5^T.}
\tag{V-below-five}

---

## 4. S-unit identity变成 ordinary Euclidean division

canonical phase exact identity为

\[
\boxed{2^HZ=5^TU+V.}
\tag{4.1}

由 `(V-below-five)`：

\[
0<V<5^T.
\]

所以 `(4.1)` 已经是 `2^HZ` 除以 `5^T` 的标准 quotient-remainder decomposition：

\[
\boxed{
U=\left\lfloor\frac{2^HZ}{5^T}\right\rfloor,}
\tag{Euclid-U}

\[
\boxed{
V=2^HZ\bmod5^T.}
\tag{Euclid-V}

这不是 asymptotic approximation，而是 sufficiently large `S` 后的 exact integer statement。

---

## 5. fixed `(H,T,V)` 后 `Z,U` 唯一恢复

由 `(4.1)` modulo `5^T`：

\[
2^HZ\equiv V\pmod{5^T}.
\]

因为 `2^H` 在 modulo `5^T` 下可逆，定义 least nonnegative residue

\[
\boxed{
\rho_5(H,T,V)
:=\left[2^{-H}V\right]_{5^T},
\qquad0\le\rho_5<5^T.}
\tag{5.1}

由 `(Z-below-five)`，合法 `Z` 同时满足

\[
0<Z<5^T.
\]

所以 residue class中只能取唯一 representative：

\[
\boxed{Z=\rho_5(H,T,V).}
\tag{Z-residue-lock}

若 `rho_5=0`，则该 `(H,T,V)` fiber直接为空；事实上 `(V,5)=1` 已排除这种情况。

随后 `(4.1)` 唯一恢复

\[
\boxed{
U=\frac{2^HZ-V}{5^T}.}
\tag{U-reconstruct}

因此：

\[
\boxed{
(H,T,V)
\Longrightarrow
(Z,U)
\text{ 至多唯一}.}
\tag{Phase-from-V}

这把 S-unit phase的 projective degrees of freedom从 pair `(U,Z)`压成 single integer remainder coordinate `V`。

---

## 6. 更小 neighborhood 中还有 modulo `U` 的第二个 least-residue reader

从同样的 uncoarsened `U,Z` identities直接相减，并使用 `(G2-via-m1)+(m1-sharp)`，得到

\[
\boxed{
\frac1S\log_{10}\frac UZ
\ge
(U_*-z_*)-\delta
+2b\mu+aN_2-R-o(1).}
\tag{6.1}

再用 `(Mu-budget)`，`2b mu-R` 的所有 residual coefficients非负，因此

\[
\boxed{
\frac1S\log_{10}\frac UZ
\ge
1-2z_* -\delta-o(1).}
\tag{U-over-Z}

其中

\[
\boxed{1-2z_*=0.382232844763938\ldots.}
\]

所以在

\[
\boxed{
\delta<1-2z_*
=0.382232844763938\ldots}
\tag{6.2}

时，eventually `0<Z<U`。

S-unit identity modulo `U` 给

\[
2^HZ\equiv V\pmod U.
\]

因为 `(U,2)=1`，定义

\[
\rho_U(H,U,V):=[2^{-H}V]_U.
\]

由 `0<Z<U`：

\[
\boxed{Z=\rho_U(H,U,V).}
\tag{U-residue-lock}

这条第二 reader 与 `Z-residue-lock` 来自同一 exact S-unit equation，不能重复计作独立 height payer；它的作用是显示 near-frontier 时 `Z` 同时位于两个 ordinary least-residue cells中。

---

## 7. 与 Farey slack 的关系

已有

\[
\boxed{
\frac{\log(UZ)}S=1+\sigma_S+o(1),}
\tag{7.1}

以及

\[
\left|\frac ZU-\frac{5^T}{2^H}\right|
=\frac{10^{\sigma_SS+o(S)}}{U^2}.
\]

本文没有证明 `sigma_S=0`。原因现在可以更精确地描述：fixed `(H,T,V)` 虽然唯一恢复 `(U,Z)`，但 `V` 本身仍可在不同 S-unit remainder cells之间移动；旧 Farey count正是在间接计数这种 moving remainder freedom。

所以 after this theorem，terminal projective bottleneck可以重写成：

\[
\boxed{
\text{控制 admissible }V
\text{ 的全局 movement，}
\quad
Z=[2^{-H}V]_{5^T},
\quad
U=(2^HZ-V)/5^T.}
\tag{V-bottleneck}

这比把 `(U,Z)` 继续视为两个独立 Farey variables更尖锐。

---

## 8. 与 denominator-side attack 的组合

`dd-corrected-common-scale-ray-sharp-2026-09-06.md` 已证明整个 `delta<=1/2` one-channel neighborhood中，fixed S-unit phase和 factor split后 denominator shape只有 common-scale ray。

本文进一步说明 fixed `(H,T,V)` 已经唯一决定该 S-unit phase。因此整个 scale-quotiented denominator primitive shape可以按

\[
\boxed{
(H,T,V)
\quad+\quad
V=v_1v_2\text{ divisor split}}
\]

参数化，其中 exponent pair `(H,T)` 只有 `S^{O(1)}=10^{o(S)}` 种，factor split只花 divisor entropy。

所以在 exponent层与 subexponential factor assignment之外，真正还携带 positive-linear projective freedom的只剩 **single remainder integer `V`**。

在更小

\[
\delta<0.191116422381969\ldots
\]

sharp product-lock neighborhood内，还可以同时使用 `qZ<v_2` 与 ordinary `qZ` lock；这继续约束由 `V` 产生的 denominator realization，但本文不把两条同源 congruence重复收费。

---

## 9. 方法边界与下一目标

本文没有添加新的 prime-depth条件；所有 residue locks都只是把已经存在的 S-unit equality在严格 height separation后升级为 ordinary integer reconstruction。

安全的新结论是：

\[
\boxed{
\text{one-channel terminal 的 Farey/S-unit residual可从 }(U,Z)
\text{ 降维为单一 }V.}
\]

下一步真正值得攻击的是 `V` 本身，尤其是同时利用：

1. `V=v_1v_2` 且 `v_2` 承担近整份 pair-max split-prime height；
2. `Z=[2^{-H}V]_{5^T}` 的 exponentially larger 5-adic residue cell；
3. denominator common-scale ray / decimal block admissibility；
4. numerator Gaussian orientation与 Top-residue cell。

如果这些条件能迫使 admissible `V` 只有 `10^{o(S)}` 种，原 `sigma_S` Farey entropy就会被真正消去；若进一步为空，则得到 strict slope gap。

---

## 10. verification scope

配套机械审计：

```bash
uv run python scripts/exact-lift/double-deficit/research-checks/tail/check_dd_corrected_sunit_euclidean_lock.py
```

脚本检查：

- `T_{5,*}=1+z_*`；
- `Five-over-Z` 的 symbolic cancellation与最大 loss ratio `a`；
- `Five-over-V` 在 `delta<=1/2` 下仍有正 margin；
- `U-over-Z` 的 shared-defect cancellation；
- toy S-unit examples 中 Euclidean quotient/remainder 与 least-residue reconstruction。

有限 checks只核对 algebra/constants；渐近 theorem由正文引用的 corrected inequalities承担。

---

## 11. 状态摘要

- **已严格完成：** entire one-channel `Z<5^T`、`V<5^T`。
- **已严格完成：** exact `Euclid-U`、`Euclid-V`。
- **已严格完成：** fixed `(H,T,V)` 的 `Z-residue-lock` 与 `(U,Z)` uniqueness。
- **额外 near-frontier reader：** `delta<1-2z*=0.382232844763938...` 时 `Z<U`，故有第二个 modulo-`U` least residue。
- **结构降维：** Farey/S-unit residual从 pair `(U,Z)` 重写为 single moving remainder `V`。
- **仍待证：** admissible `V` 的 subexponential/empty classification；explicit strict slope gap；DD emptiness；更低 post-tail / non-canonical dominant states 的统一 simultaneous height bound。

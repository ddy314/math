# `double-deficit`（DD）分支

这是 DD 的**当前权威状态入口**。

2026-08-22 的 discriminant-root audit 发现：unified integer discriminant root 与 §18 reduced root 之间存在真实 normalization factor。旧稿中把两者直接认同后得到的 5-adic high-funnel closure 已撤销。历史账本继续保留原来源块用于审计；若状态冲突，以本 README 和 2026-08-22 correction notes 为准。

## 1. 当前安全主结论

DD 尚未证明为空，也没有 effective absolute height bound。

当前安全全局渐近界为

\[
\boxed{
\limsup_{\rm DD}\frac{n_3}{S_{12}}
\le6.308883577618\ldots
}
\]

阈值依赖 Schmidt Subspace Theorem，因此非有效。

corrected canonical `t_2=1` double-resonant high funnel 已独立重证同一常数。令

\[
a=\log_{10}2,
\]

则

\[
\boxed{
\limsup\frac nS
\le
\frac{8+7a}{1+2a}
=6.308883577618031\ldots.
}
\]

若 equality ray 可实现，则 corrected dual rigidity 强迫

\[
Q_5,G_5,N_5,R\to0,
\qquad
\frac mS\to2.808883577618\ldots,
\qquad
\frac dS\to\frac72.
\]

旧 `6.308883...` terminal ratios 因而仍是真正 extremal geometry；当前没有正确证明将 `<=` 升级为严格 `<`。

主要修正文：

- [`dd-discriminant-root-dependency-audit-2026-08-22.md`](dd-discriminant-root-dependency-audit-2026-08-22.md)：错误 normalization 的依赖审计。
- [`dd-corrected-high-funnel-schmidt-2026-08-22.md`](dd-corrected-high-funnel-schmidt-2026-08-22.md)：corrected high-funnel Schmidt + exact-small-factor proof。
- [`frontier.md`](frontier.md)：terminal odd moving-core 与历史 conditional/no-go 规范账本。

## 2. 已撤销 / 降级的旧 high-funnel 结论

以下内容不得再作为覆盖整个 canonical funnel 的 theorem 引用：

1. 旧 `frontier-five-adic-closure` 给出的
   \[
   \limsup n/S<6.308883577618\ldots;
   \]
2. exhaustive
   \[
   \text{Defect-heavy}\cup\text{Tail-short}
   \]
   `Five-dichotomy`；
3. 旧
   \[
   3v_5(\Xi)=5q_5+4g_5+n_5-m;
   \]
4. 由此推出的 generic denominator-max exhaustion 与 `Final-5` 必然性；
5. 依赖上述 exhaustion 合并出的 whole canonical `<=6`。

`Final-5`、Tail-short 等额外条件 sheet 内部不依赖错误 normalization 的局部式仍可条件使用。

## 3. corrected 5-adic high-funnel ledger

记

\[
E_5=\max_i v_5(b_i),
\qquad B_5=v_5(b_3),
\qquad q_5=v_5(Q).
\]

在相应 `B_5<m` discriminant-separation region，正确深度为

\[
\boxed{v_5(\Xi)=q_5+E_5-B_5.}
\]

对应 sphere gap：

\[
\boxed{v_5(H_{\rm sph}-y_3)=T+(E_5-B_5).}
\]

normalized overlap

\[
\widehat g=\gamma/c_3
\]

满足

\[
v_5(\widehat g)=g_5-(E_5-B_5),
\]

因此 actual small factor 中 max deficit 精确抵消：

\[
\boxed{
v_5((H_{\rm sph}-y_3)\widehat g)=T+g_5.
}
\]

配合

\[
F_-=2^{H+1}Z(H_{\rm sph}-y_3)\widehat g
\]

得到 whole-funnel lower，再与 Schmidt-safe budget作 dual，恢复 `6.308883...`。

## 4. equality terminal 的安全结构

若存在 sequence 满足

\[
\frac nS\to6.308883577618\ldots,
\]

则旧 terminal conditional identities在不依赖错误 discriminant normalization 的范围内继续可用：

\[
5^TU+V=2^HZ,
\]

\[
V=C_Lv_0,
\qquad
\log C_L=S+o(S),
\qquad
\log v_0=o(S),
\]

\[
q_c=10^{z_*S+o(S)},
\qquad
z_*=0.308883577618\ldots,
\qquad
(C_L,q_c)=1,
\]

\[
N(\Pi)=C_L,
\qquad
\Pi^2\mid y_2+i y_3.
\]

另有

\[
\log U=(1-z_*)S+o(S),
\qquad
\log Z=z_*S+o(S),
\]

以及 denominator quotient

\[
R_2=\frac{5^T\widetilde r+s q_c\theta}{2^{m_2}},
\qquad
\log R_2=1.007853581954\ldots S+o(S).
\]

terminal 的真正指数级移动对象仍是 odd split-prime pair-max core `(C_L,Pi)`。

## 5. full rational-contact：Bad 已关闭

full rational-contact 指

\[
D_+D_-=C_L^{1-o(1)}.
\]

已有严格 continuation 给

\[
\boxed{
\log(B_+B_-)=o(S).
}
\]

selected / conjugate orientation 在 `Delta_U` 中的 repeat也只有 `o(S)`。所以 leading mass 是 Good。

Good 的 cofactor Lorentz system、`Good-cofactor-unit`、slot mutual exclusion、derivative orientation reconstruction均继续有效。

## 6. full rational Good 的 same-prime local algebra：当前视为闭包

2026-08-22 新增：

[`dd-frontier-good-digit-shell-local-closure-2026-08-22.md`](dd-frontier-good-digit-shell-local-closure-2026-08-22.md)

证明 radius / equal-depth residual 对完整拼接 numerator 的 local digit condition，在 quotient-level `A_12` compatibility中精确退回

\[
B10^d\Sigma-U10^{m+d}=B10^dV.
\]

因为 main prime-power 已整除 `V`，该 compatibility在允许深度内自动成立。

因此以下尝试不再作为优先任务：

- pure-radius 再造第三条 same-prime CRT；
- equal-depth residual 再做同素数 digit resultant；
- axis Gaussian carrier与 radius digital carrier继续取普通 determinant。

它们都会回到 `Concat-radius`、hidden square、已有 quotient parent 或 `V` baseline。

full rational Good 仍可能需要**全局** split-prime / digit-location theorem，但其已知 same-prime local parent algebra没有显示新的正线性 surplus。

## 7. genuine-Gaussian 的 radius × pair-max local route也闭包

[`dd-frontier-genuine-radius-pairmax-collapse-2026-08-22.md`](dd-frontier-genuine-radius-pairmax-collapse-2026-08-22.md) 给出统一 radius digital carrier

\[
\pi^r\mid2b10^dA_{12}+ia_2A.
\]

与原 pair-max line消元时，terminal denominator normalization

\[
b_2=JC_0\widetilde r,
\qquad
b_3=ABJC_0
\]

强迫自然 determinant 精确为零：

\[
2b\beta_2-A10^m\beta_3=0.
\]

所以 genuine radius repeat不会自动回流到 rational sign contact，也不会产生新的 same-prime digit obstruction。

结论：rational/genuine 两侧都不应继续迭代普通 radius Hensel/resultant。

## 8. source core 与 projective denominator

[`dd-frontier-source-core-projective-denominator-2026-08-22.md`](dd-frontier-source-core-projective-denominator-2026-08-22.md) 给出新 exact allocation。

terminal sphere：

\[
H_{\rm sph}-y_3=2\cdot5^T\rho_0,
\qquad\log\rho_0=o(S),
\]

\[
H_{\rm sph}+y_3=q_c^2K_+.
\]

若

\[
g=(y_1,y_2),
\qquad r_p=v_p(g),
\qquad\omega_p=v_p(X^2+Y^2),
\]

则

\[
Z_0=\frac{H_{\rm sph}+y_3}{(g,H_{\rm sph}+y_3)}.
\]

逐 non-decimal prime可得

\[
\boxed{
v_p(Z_0)
\ge
\max\left(0,
v_p(q_c)-\left\lfloor\frac{v_p(\rho_0)}2\right\rfloor
\right).
}
\]

故 effective core 上

\[
\boxed{q_c/10^{o(S)}\mid Z_0.}
\]

特别地

\[
\boxed{
\log Z_0\ge z_*S-o(S).
}
\]

所以此前可能的“证明 `Z_0` 次指数，从而压小 `(q,Z)`”路线已关闭：`Z_0` 本来就是 source core 的自然 projective reader。

## 9. source / pair-max projective 极化

[`dd-frontier-projective-source-pairmax-polarization-2026-08-22.md`](dd-frontier-projective-source-pairmax-polarization-2026-08-22.md) 进一步证明：删去 `o(S)` exceptional core后，对 main

\[
p^e\Vert C_L
\]

one-channel denominator pattern为

\[
v_p(b_1)=0,
\qquad
v_p(b_2)=v_p(b_3)=e.
\]

因此

\[
v_p(y_1)\ge e,
\qquad
v_p(y_2)=v_p(y_3)=0,
\qquad
v_p(H_{\rm sph})\ge e.
\]

于是

\[
\boxed{v_p(Z_0)=0}
\]

并且

\[
\boxed{
v_p(N(y_1+i y_2))=0.
}
\]

全局即

\[
\boxed{
q_c/10^{o(S)}\mid Z_0,
\qquad
(C_L,Z_0)=10^{o(S)},
}
\]

同时 primitive stereographic numerator对 main `C_L` 也是 Gaussian unit。

这说明 coefficient-circle / `Z_0` geometry主要读取 source `q_c`；pair-max orientation存在于 `y_2+i y_3`，不会自动传播到 primitive stereographic coordinate。

因此旧“把 terminal `C_L` orientation直接接回 `Z_0` / coefficient circle”路线降级。

## 10. `a_3` triple CRT 与 `rho_*`：只作 coordinate/counting view

[`dd-frontier-a3-triple-crt-residual-2026-08-22.md`](dd-frontier-a3-triple-crt-residual-2026-08-22.md) 证明固定 orientation fiber中，`a_3` 同时有：

- decimal `10^d` period；
- clean-source `q_c^2` period；
- pair-max `C_L^2` rational period。

联合 period高度为

\[
6.117767155236\ldots S+o(S),
\]

留下形式尺度

\[
\rho_*S,
\qquad
\rho_*=rac12-z_*=0.191116422382\ldots.
\]

且

\[
\rho_*S
=\log|\Pi|-\log q_c+o(S)
=\log U-\log|\Pi|+o(S).
\]

但这**不是真正的 frontier entropy**：已有 `A_0` 双重重构把固定 denominator-tail fiber中的 `A_0` 压到至多一个，随后

\[
VA_0-g_0a_3=2\cdot5^TR_0
\]

精确决定 `a_3`。

所以 `rho_*` 只保留为 source/orientation 的自然中间尺度，不能被解释成尚有 `10^{rho_*S}` 个真实自由候选。

## 11. source/orientation Euclidean quotient：真实但临界

[`dd-frontier-source-orientation-euclidean-quotient-2026-08-22.md`](dd-frontier-source-orientation-euclidean-quotient-2026-08-22.md) 将 `|Pi|/q_c` integralize。

写 secondary factorization

\[
\Pi\Delta_1=Pq_c-iI.
\]

Gaussian Euclidean division

\[
\Pi=q_cK+\varrho,
\qquad
N(\varrho)\le q_c^2/2
\]

给

\[
\log|K|=\rho_*S+o(S)
\]

以及 exact

\[
\boxed{
q_cE_\rho=\varrho\Delta_1+iI,
\qquad
E_\rho=P-K\Delta_1\ne0.
}
\]

但

\[
\log|E_\rho|
\le0.654441788809\ldots S+o(S),
\]

恰与 `|Delta_1|` 同尺度；同时

\[
\log(q_c,N(\Delta_1))=o(S).
\]

因此 ordinary Gaussian Euclidean iteration目前只产生临界 continued-fraction step，没有新的 positive-linear divisor。

## 12. 当前已判死 / 不应重开的 terminal 路线

除旧账本已记录的 no-go 外，2026-08-22 后再加入：

- old discriminant-root 5-adic mismatch；
- Five-dichotomy / Xi-slack / denominator-max exhaustion；
- full rational Bad 作为开放 branch；
- Good pure-radius/equal-depth 的第三 same-prime digit CRT；
- genuine radius × pair-max ordinary determinant；
- 证明 `Z_0=10^{o(S)}`；
- 通过 primitive stereographic coordinate直接传播 main `C_L` orientation；
- 将 `rho_*` 当作真实 candidate entropy；
- ordinary Euclidean division of `Pi/q_c` 本身作为 strict-gap mechanism。

## 13. 当前真正的优先任务

terminal strict-gap 工作已经显著收窄。现在优先级为：

1. **moving pair-max global compatibility**：保留 raw pair-max line `y_2+i y_3` 与 derivative/secondary orientation，寻找跨 prime / 跨 digit block 的 global condition；不再经过 `Z_0` 作为 `C_L` reader。
2. **denominator-prefix × pair-max orientation**：利用 `C_L` 几乎全部位于长 denominator block `b_2`，把 decimal concat relation、S-unit source relation与 chosen Gaussian orientation放入同一 global congruence，而不是继续单 prime Hensel。
3. **global split-prime distribution / digit-shell**：若所有自然 exact eliminants继续临界，则需要真正利用 `C_L` 由 split primes组成且同时是 decimal block大 core这一全局性质。
4. **post-tail / non-canonical feedback**：只有在 terminal 得到新 strict payer后，才把它反馈到 global branch partition；不要再用已撤销的 5-adic closure提前宣称 strict gap。

DD 当前仍为：

\[
\boxed{
\text{全局空性待证，安全渐近界 }\limsup n_3/S_{12}\le6.308883577618\ldots.
}
\]

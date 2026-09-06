# DD corrected quartic / product-orientation dependency audit

> 日期：2026-09-06
>
> 依赖：[`dd-corrected-scale-free-secondary-carrier-2026-09-06.md`](dd-corrected-scale-free-secondary-carrier-2026-09-06.md)、[`dd-corrected-v2-projective-polarization-2026-09-06.md`](dd-corrected-v2-projective-polarization-2026-09-06.md)、`dd-frontier-secondary-quadratic-reciprocity-2026-08-22.md`、`good-genuine-ledger.md` 中 W-free fixed `A_12` CRT，以及 [`dd-discriminant-root-dependency-audit-2026-08-22.md`](dd-discriminant-root-dependency-audit-2026-08-22.md)。
>
> **状态：依赖审计 / no-go 定位。** 本文不新增 slope bound。目标是回答一个具体问题：2026-09-06 已经把 chosen pair-max orientation正规化成 neighborhood-valid `Pi_Omega | (...)` 后，能否立刻用 quartic reciprocity把它与 denominator prefix闭环？结论是：当前安全 parent family 中仍缺第二个 genuinely orientation-sensitive reader；只使用 rational prefix/phase/Top-residue/W-free CRT 时，quartic product orientation没有独立的交换端。

---

## 1. 当前安全的 chosen orientation parent

2026-09-06 已证明整个 corrected one-channel neighborhood存在

\[
\boxed{
\Pi_\Omega\mid
A_V2^{m-2}q_V-iB_V5^{2T-m},
\qquad N(\Pi_\Omega)=v_2,}
\]

其中

\[
A_V=g_0a_2v_1,
\qquad
B_V=R_0\tau_2.
\]

这条确实区分 `Pi_Omega` 与其 conjugate，并且完全避开旧 discriminant-root identification。

但它来自 pair-max orientation + gap reconstruction；因此与 raw pair-max line

\[
\Pi_\Omega^2\mid y_2+i y_3
\]
属于同一个 sphere/orientation parent family，不能把二者当成两个 independent orientation readers。

---

## 2. rational parents 对 conjugation 不敏感

当前其它安全的强结构包括：

\[
Uq_V=b_1^{(V)}10^{m_2}+v_2\tau_2,
\]

\[
2^HZ-5^TU=v_1v_2,
\]

Top-residue / exact carry，及 W-free fixed `A_12` CRT。

这些 identities 中 pair-max moving object只通过 rational integer

\[
\boxed{v_2=N(\Pi_\Omega)=\Pi_\Omega\overline{\Pi_\Omega}}
\]
出现。因此它们在形式上全部保持 involution

\[
\boxed{
\Pi_\Omega\longleftrightarrow\overline{\Pi_\Omega}.}
\tag{Conjugation-blind}
\]

也就是说，单靠这些 rational parents最多读取：

- rational splitting `p=pi bar pi`；
- norm / quadratic character；
- `v_2` 的 ordinary residue；

但不能选择 `pi` 与 `bar pi` 中哪一个是 candidate 的 actual orientation。

---

## 3. W-free genuine CRT 仍是 rational sphere-paid reader

`good-genuine-ledger.md` 的 W-free fixed `A_12` CRT使用已经 sphere-paid 的 rational carrier

\[
\Theta=(\kappa+G)A_c\beta+\mathscr T a_3^2,
\qquad C_G^2\mid\Theta,
\]

再结合 exact carry得到一个 fixed linear congruence modulo `C_G`。

它的重要价值是去掉旧 coefficient 中的 discriminant root `W`；但最终 reader仍然是 rational `A_12 mod C_G`，并不携带一个独立 Gaussian prime product whose conjugate choice is fixed by a different parent.

因此它可继续用于 CRT / numerator reconstruction，却不能直接作为 quartic reciprocity的第二 orientation endpoint。

---

## 4. 旧 discriminant Gaussian carrier 当前不可作为替代

历史 genuine/frontier 账本中确实存在看起来“independent-looking”的第二 Gaussian carrier，其中 chosen pair-max prime会与 discriminant/tail-root carrier比较。

但当前 canonical dependency audit已经明确：旧 DD 证明曾错误识别两个 discriminant roots；凡依赖该 identification 的 orientation/valuation continuation都必须重新证明，不能作为现行 strict-gap parent直接调用。

因此在没有完成新的 W-free Gaussian-valued replacement前，不能用这条历史 carrier补足 quartic reciprocity的第二端。

---

## 5. ordinary quadratic reciprocity为什么只能给有限 character

旧 corrected frontier secondary theorem已经从 chosen Gaussian source line安全导出 quadratic character compatibility：main pair-max primes除了 `p=1 mod 4` 外，还满足一个额外 moving quadratic splitting condition。

这是真约束，但每个 prime只增加有限 `+/-1` character；对应 prime set仍可有正密度。因此它不能单独制造 `exp(-epsilon S)` 级 height saving。

quartic reciprocity若要真正升级，必须保留 `pi/bar pi` 的 chosen orientation。由 §§2--4，当前 safe rational parents无法提供独立的 conjugation-sensitive comparison，所以仅把 quadratic symbol机械替换成 quartic symbol不会自动产生闭环。

---

## 6. 成功标准

后续 quartic/product-orientation attack只有在找到以下任一对象后才值得继续：

1. 一个 W-free Gaussian integer `G_dec`，来自 genuinely different decimal/full-concat parent，并满足 selected `pi_p` 对 `G_dec` 的 divisibility/orientation；
2. 一个 global product sign/argument invariant，能区分 `Pi_Omega` 与 `bar Pi_Omega`，且不是 pair-max sphere line本身的重写；
3. 一个 deterministic Archimedean sector for `Delta_V` whose conjugate sector is forbidden by decimal digit data。

在此之前，继续对 rational prefix、phase、Top-residue、`K_V`、`J_V` 取 norm/Jacobi/quartic symbols都不会新增独立 parent。

---

## 7. 状态摘要

- **安全 chosen orientation parent：** scale-free secondary carrier `Pi_Omega | (...)`；
- **同源 parent：** raw pair-max line `Pi_Omega^2 | y_2+i y_3`，不可重复收费；
- **W-free genuine reader：** 仅 rational `A_12` CRT，conjugation-blind；
- **历史第二 Gaussian carrier：** discriminant-root dependency未重新证明，当前不可用；
- **结论：** quartic route 当前缺第二个 independent orientation-sensitive parent；
- **下一目标：** W-free decimal/full-concat Gaussian carrier，或 `Delta_V` 的 deterministic oriented digit-shell location。

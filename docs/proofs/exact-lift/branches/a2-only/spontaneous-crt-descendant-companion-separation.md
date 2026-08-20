# A2 descendant external common 与 `G_JB` companion-common support 的严格分离

> **依赖：** `spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-pure-prefix-elimination.md`、`spontaneous-companion-external-tail-budget.md`、`spontaneous-height-equal-depth-target-selector.md`。
>
> **严格状态：**此前 `G_JB` 的 generic external common depth会无损进入 `Lambda_tail`，因此需要确认新 descended common kernel是否自动属于该 old external pool。本文证明答案恰好相反：在 `alpha`-separated genuine sector，若 prime已经进入 descendant common gcd，则它整除 `J_Hhat` 当且仅当它进入 central gate `2K-9`。因此 generic pure-spontaneous noncentral descendant-common prime必满足 `p∤J_Hhat`，从而与 `G_JB` support严格互斥。故 `Lambda_tail` 的 external companion budget不能用于支付 generic descendant-only external parity；两类 external pool必须分开记账。本文不排除 descendant-only pool本身，因此不关闭 A2。

---

## 1. descendant common always enters the original additive carrier

fully primitive descent给

\[
\widehat{\mathcal T}_2
=5^\lambda\mathscr R_{63}^\star
+g2^m\widehat{\mathscr D}_{63}.
\]

若 odd prime `p` 进入 descendant common gcd

\[
\boxed{
p\mid\mathscr R_{63}^\star,
\qquad
p\mid\widehat{\mathscr D}_{63},}
\tag{1.1}
\]

则立刻

\[
\boxed{p\mid\widehat{\mathcal T}_2.}
\tag{1.2}
\]

这一步不使用任何 prime-source 标签。

---

## 2. height-free identity gives an exact central equivalence

已有 height-free additive identity

\[
\boxed{
\widehat{\mathcal T}_2
=5^m\widehat{\mathcal J}_H
-2^{m+1}B_0^2(2K-9)\alpha,}
\tag{2.1}
\]

其中

\[
B_0=c_ug,
\qquad
\alpha=TK+a_3=\omega W_q.
\]

固定 genuine odd prime满足

\[
\boxed{p\nmid2\cdot5\cdot B_0\alpha.}
\tag{2.2}
\]

在 descendant common support 上由 (1.2)，(2.1) 化为

\[
\boxed{
5^m\widehat{\mathcal J}_H
\equiv
2^{m+1}B_0^2(2K-9)\alpha
\pmod p.}
\tag{2.3}
\]

(2.2) 说明除 `2K-9` 外所有乘子均为 unit，所以得到 exact support equivalence

\[
\boxed{
p\mid\widehat{\mathcal J}_H
\Longleftrightarrow
p\mid2K-9,}
\tag{2.4}
\]

前提是 `p` 已满足 descendant common (1.1) 与 separation (2.2)。

---

## 3. generic pure-spontaneous descendant support is `J_H`-free

`spontaneous-prefix-branch-audit.md` / `spontaneous-crt-pure-prefix-elimination.md` 的 genuine pure-spontaneous generic branch本来就要求

\[
\boxed{p\nmid\alpha,}
\tag{3.1}
\]

并单列 central line，所以 generic branch还有

\[
\boxed{p\nmid2K-9.}
\tag{3.2}
\]

source/content separation同时保证 (2.2) 的其余 unit条件。

因此由 (2.4)：

\[
\boxed{p\nmid\widehat{\mathcal J}_H.}
\tag{3.3}
\]

这是比“没有证据说明它进入 companion pool”更强的结论：generic pure-spontaneous descendant-common prime**严格不能**进入 `J_H` support。

---

## 4. consequence for the canonical companion-common carrier

canonical height decomposition定义

\[
D_H=\gcd(\widehat{\mathcal J}_H,W_q),
\]

\[
J^\circ=\widehat{\mathcal J}_H/D_H,
\qquad
B^\circ=\mathscr B_W/D_H,
\]

\[
\boxed{G_{JB}:=\gcd(J^\circ,B^\circ).}
\tag{4.1}
\]

显然

\[
p\mid G_{JB}
\Longrightarrow
p\mid J^\circ
\Longrightarrow
p\mid\widehat{\mathcal J}_H.
\tag{4.2}
\]

与 (3.3) 合并：

\[
\boxed{
\operatorname{Supp}_{\rm gen\,pure}(G_\Delta)
\cap
\operatorname{Supp}(G_{JB})
=\varnothing.}
\tag{4.3}
\]

这里左侧只指 `alpha`-free、noncentral genuine pure-spontaneous descendant-common sector；height/content/central/fixed sectors仍按既有文件单列。

---

## 5. `Lambda_tail` external budget cannot pay this pool

`spontaneous-companion-external-tail-budget.md` 已证明 generic external companion-common subproduct

\[
G_{JB}^{\rm ext}
\]
完整整除

\[
\Lambda_{\rm tail}.
\]

但 (4.3) 现在说明：新 pure-prefix descendant external carrier与该 external companion pool support严格互斥。

因此不能把

\[
G_\Delta^{\rm pure,ext}
\]
错误地装进 `Lambda_tail` 的旧预算。正确 ledger 是两类独立 external pool：

\[
\boxed{
\begin{array}{c|c|c}
\text{pool}&\text{defining common support}&\text{canonical reader}\\ \hline
\text{companion external}&J^\circ\cap B^\circ&\Lambda_{\rm tail}\\
\text{descendant-only external}&R_{63}^\star\cap\widehat D_{63}&\mathcal X_{63,i}^{\rm pref}
\end{array}}
\tag{5.1}

并且 generic supports互斥。

---

## 6. only the central gate can reconnect them

由 (2.4)，在 `alpha`-separated descendant common sector中，若还要求

\[
p\mid\widehat{\mathcal J}_H,
\]
则必须

\[
\boxed{p\mid2K-9.}
\tag{6.1}
\]

所以 descendant common 与 companion/`J_H` support重新接触的唯一入口就是已经反复出现的 central line。

该 central line已有 fixed/content/omega-content audits；本文不重复，也不把它混回 generic pure-prefix carrier。

---

## 7. updated frontier

这一步关闭了一个潜在但错误的 product-budget shortcut：generic pure-spontaneous descendant common depth**不能**借 `G_JB^ext|Lambda_tail` 付账。

因此剩余 A2 external parity确实集中在新构造的 pure-prefix side：

- generic coefficient：`X_63,i^pref(x,y)=0`；
- low coefficient singular：short `V_4`，primitive `7 mod8`；
- high coefficient singular：compact `V_24`，primitive `5 mod8`。

下一步应直接为这些 descendant-only pure-prefix carriers建立自己的 height/depth budget，而不是继续复用旧 companion tail。

A2 仍为 `待证`。

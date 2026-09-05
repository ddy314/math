# DD discriminant-root normalization 的依赖审计

> **依赖：** [`dd-general-transfer-correction-2026-08-22.md`](dd-general-transfer-correction-2026-08-22.md)、
> [`core.md`](core.md)、[`tail-allocation-ledger.md`](tail-allocation-ledger.md)、
> [`high-funnel-ledger.md`](high-funnel-ledger.md)、[`good-genuine-ledger.md`](good-genuine-ledger.md)。
>
> **状态：** `纠错 / proof-status audit`。本文不添加新的 DD 全局不存在性结论；
> 它确定统一二次判别根与 DD §18 gap 判别根的 normalization 后，逐条标记旧证明树中
> 依赖错误识别的结论，并给出仍可安全使用的基线。

---

## 1. 两个判别根必须分开

DD §18 定义

\[
\Xi=\mathcal M-C_0a,
\qquad
W_{\rm gap}=L\Xi,
\qquad
C_0=LQ+2\tau.
\]

统一二次式的正判别根另记为

\[
\widetilde W^2
=(\kappa GC)^2
-\kappa(\kappa+2G)Q^2\mathcal N_{12}.
\]

`dd-general-transfer-correction-2026-08-22.md` 已严格证明

\[
\boxed{
\widetilde W
=\frac{\kappa G}{q_{\rm lcm}}\,|\Xi|,
}
\tag{1.1}
\]

其中

\[
q_{\rm lcm}=\operatorname{lcm}(b_1,b_2,b_3).
\]

因此一般并没有

\[
\widetilde W=L\Xi.
\]

两者之比为

\[
\boxed{
\frac{\widetilde W}{|W_{\rm gap}|}
=\frac{\kappa G}{q_{\rm lcm}L}.
}
\tag{1.2}
\]

任何同时引用“unified discriminant valuation”和“§18 `W=LXi`”的证明，都必须先检查是否漏掉 `(1.2)`。

---

## 2. `tail-rough-general-transfer` 的最后 contradiction 失效

旧 `tail-rough-general-transfer.md` 在 hard local sheet 中先正确得到 unified root 的 valuation，
随后把它直接当成 §18 的 `LXi`，由此制造所谓 derivative extra depth。

修正后该 extra depth精确等于

\[
v_p(\kappa G/q_{\rm lcm}).
\]

而 gap root本身只有已有 baseline depth。故旧结论

\[
\boxed{
x_p\le
\max(v_p(C),v_p(N_0),v_p(R_3^{\rm den}))}
\tag{Old-general-transfer}
\]

当前状态应改为

\[
\boxed{\text{待证 / suspended}.}
\]

因此以下依赖其“整个 `X_Q` support 已穷尽”的 downstream statements 不能再按原作用域引用：

- `tail-rough-gaussian-payer-split`；
- `tail-rough-angular-source-transfer`；
- `tail-rough-canonical-payer-decomposition`；
- `tail-rough-projective-bottom-two-payer`；
- `tail-rough-z0-only-frontier`；
- 2026-08-21 新增 Gaussian continuation 中依赖全 support 穷尽性的 status line。

这些文件中的局部 Gaussian identities、sphere identities、bottom determinant identities 等，
在其显式 hypotheses 下仍可单独使用；撤销的是“它们已经穷尽所有 `X_Q` hard mass”的结论。

---

## 3. `frontier-five-adic-closure` 的原 contradiction 失效

旧 equality-frontier closure 也把 unified root 与 `LXi` 识别为同一个整数，
随后比较 tail-decimal 两项的 5-adic valuation得到 mismatch。

修正 `(1.1)` 后，显式 normalization factor恰好补回该差值；原 mismatch 不存在。
因此旧文件不能继续证明

\[
\limsup_{\rm DD}n_3/S<6.308883577618\ldots.
\]

在找到独立 strict-gap proof 之前，安全的全局 statement退回 `core.md` 的 Schmidt bound

\[
\boxed{
\limsup_{\rm DD}\frac{n_3}{S}
\le6.308883577618\ldots.
}
\tag{Global-safe}
\]

注意 `(Global-safe)` 来自更早的 global tail / fixed-target Schmidt analysis，
不是本文撤销的 equality-frontier 5-adic closure。

---

## 4. `high-funnel-five-adic-dichotomy` 的 valuation mismatch 消失

在 canonical high funnel 中记

\[
B_5=v_5(b_3),\quad q_5=v_5(Q),\quad g_5=v_5(G),\quad
n_5=v_5(\mathcal N_{12}),\quad k_5=v_5(\kappa).
\]

5-resonance 与 tail weight仍严格给

\[
3k_5=2m+2q_5+g_5+n_5,
\tag{4.1}
\]

\[
k_5=m+q_5+g_5-B_5,
\tag{4.2}
\]

故

\[
3B_5=m+q_5+2g_5-n_5.
\tag{4.3}
\]

在 slope `>7` 的 asymptotic high funnel 中，global tail bound `m/S<=5+o(1)` 给
`d>2S-o(S)`，而 `q_5<\log_5(10)S`; 因而 eventually `d>q_5`。
统一判别式两项于是严格分离，并给

\[
\boxed{v_5(\widetilde W)=2k_5-m.}
\tag{4.4}
\]

另一方面 tail-root original identity为

\[
\mathscr T a_3
=\kappa G^2 10^dA_{12}
+\eta(\kappa+G)\widetilde W,
\qquad
\mathscr T=\frac{\kappa^2(\kappa+2G)}{10^m}.
\tag{4.5}
\]

由于 `k_5>g_5`：

\[
v_5(\mathscr T a_3)=2k_5+g_5-m,
\tag{4.6}
\]

而 `(4.4)` 同时给

\[
\boxed{
v_5((\kappa+G)\widetilde W)
=g_5+(2k_5-m)
=2k_5+g_5-m.}
\tag{4.7}
\]

两项 **精确同深**。

旧 `high-funnel-five-adic-dichotomy.md` 的

\[
\text{Defect-heavy}\ \cup\ \text{Tail-short}
\]

二分正是依靠错误替换 `\widetilde W=LXi` 后得到的 strict valuation difference。
因此该二分目前失效；`Tail-short` LP 仍是一个正确的**条件 LP**，但不能再声称它与
`Defect-heavy` 穷尽整个 high funnel。

---

## 5. `high-funnel-xi-depth` 的正确替代式

令

\[
E_5:=v_5(q_{\rm lcm})=\max_i v_5(b_i).
\]

由 `(1.1)` 与 `(4.4)`：

\[
\begin{aligned}
v_5(\Xi)
&=v_5(\widetilde W)
-v_5(\kappa G/q_{\rm lcm})\\
&=(2k_5-m)-(k_5+g_5-E_5)\\
&=k_5-m-g_5+E_5.
\end{aligned}
\]

使用 `(4.2)`：

\[
\boxed{
v_5(\Xi)=q_5+E_5-B_5.}
\tag{Xi-correct}
\]

这取代旧式

\[
3v_5(\Xi)=5q_5+4g_5+n_5-m.
\]

特别地：

\[
E_5=B_5
\Longrightarrow
\boxed{v_5(\Xi)=q_5.}
\tag{5.1}
\]

若 prefix denominator 在 5-adic 上超过第三分母，则 `Xi` 的额外深度恰好是

\[
E_5-B_5.
\]

---

## 6. corrected gap / sphere ledger

仍在 high-funnel、eventually `d>q_5` 的范围内。令

\[
\delta_5:=E_5-B_5=v_5(y_3)\ge0.
\]

写

\[
\omega=(10^m,b_3),\qquad
L=10^m/\omega,\qquad
\tau=b_3/\omega.
\]

由

\[
\Xi=Qy_3-\tau a
\]

和 `(Xi-correct)`，先得到

\[
v_5(\tau a)\ge q_5+\delta_5.
\tag{6.1}
\]

又

\[
v_5(L)=(m-B_5)_+,
\qquad
v_5(\tau)=(B_5-m)_+.
\]

因为 `k_5>g_5` 等价于

\[
m+q_5-B_5>0,
\]

`(6.1)` 强迫

\[
v_5(H-y_3)=v_5(La)>\delta_5.
\]

因此 odd-prime two-factor lemma给

\[
\boxed{
v_5(H)=v_5(y_3)=v_5(H+y_3)=\delta_5.}
\tag{6.2}
\]

sphere factorization

\[
(H-y_3)(H+y_3)=y_1^2+y_2^2
\]

与

\[
y_1^2+y_2^2
=(q_{\rm lcm}/G)^2\mathcal N_{12}
\]

于是给

\[
\boxed{
v_5(H-y_3)
=m+q_5+E_5-2B_5.}
\tag{6.3}
\]

进一步

\[
\boxed{
v_5(\tau a)=q_5+E_5-B_5=v_5(\Xi).}
\tag{6.4}
\]

若 remaining high-slope 中 `B_5<m`，则 `tau` 为 5-unit，因此

\[
\boxed{
v_5(a)=v_5(\Xi)=q_5+E_5-B_5,}
\tag{Gap-correct}
\]

\[
\boxed{
v_5(H-y_3)=m+q_5+E_5-2B_5.}
\tag{Gap-depth-correct}
\]

将 `(Gap-depth-correct)` 代回 sphere 只恢复 `(4.3)`；它不产生旧 denominator-max
proof 中的额外 inequality。

因此旧结论

\[
E_5>B_5\Longrightarrow n<6S+O(1)
\]

当前没有证明。

当 `E_5=B_5` 时，仍严格有

\[
\boxed{
v_5(a)=v_5(\Xi)=q_5,}
\tag{B3-max-gap}
\]

\[
\boxed{
v_5(H-y_3)=m+q_5-B_5.}
\tag{B3-max-gap-depth}
\]

但旧 `Final-5-lock`

\[
B_5=q_5+2g_5,
\qquad
m=2q_5+4g_5+n_5
\]

不再由这些式子推出。

---

## 7. downstream high-funnel status

因此下列**全 funnel / branch-exhaustion** claims必须降级：

- `high-funnel-five-adic-dichotomy` 的 exhaustive dichotomy；
- `high-funnel-xi-depth` 中把 defect-heavy slack识别为 `3v_5(Xi)` 的部分；
- `high-funnel-gap-depth` 中基于旧 `Xi-slack` 的 extra-gap formula；
- `high-funnel-denominator-max-lock` 的 non-max `<=6` 与 `Final-5-lock` 穷尽性；
- 依赖上述 branch tree 的 `canonical <=6.215...`、`<=6.25`、`<=6` 合并结论；
- `high-funnel-tail-short-schmidt-upgrade` 的 whole-sector `<=6` status。

以下内容仍可按原条件使用：

1. 5-resonance `(4.1)` 与 tail weight `(4.2)`；
2. `B_5>=m => n<6S+O(1)`：其证明只使用 `(4.3)` 与 defect-stability；
3. `high-funnel-defect-optimization` 的 `Defect-stability`、`Combined-height` 与
   Tail-short **conditional** LP certificate；
4. exact `t_2=1` small-factor normalization
   \[
   F_-=\frac{2^{H+2}5^TZ}{s}\,a\frac{g_*}{V};
   \]
5. sphere `c_3` inequality本身；
6. gap/recovery square identities与其 no-double-pay audit，在不使用 `Final-5-lock`
   specialization时仍保持严格。

---

## 8. `Subspace-defect` 可独立恢复

旧文件中 stronger Schmidt budget虽然后来被放在依赖 `Final-5` 的 branch tree中引用，
但它本身可以直接由 canonical `t_2=1` S-unit phase重证，不需要 `(Old-general-transfer)`、
`Five-dichotomy` 或 `Final-5-lock`。

写

\[
a_2=\log_{10}2,
\qquad b_5=\log_{10}5,
\]

归一化

\[
M=m/S,\quad Q_2=\mathfrak q/S,\quad N_2=\mathfrak n/S,
\]

\[
Q_5=q_5/S,\quad G_5=g_5/S,\quad N_5=n_5/S,
\]

以及

\[
R=\log_{10}\gamma_0/S.
\]

S-unit phase为

\[
\kappa=2\gamma5^TU,
\qquad
\kappa+2G=2\gamma2^HZ,
\qquad
2^HZ-5^TU=V.
\]

两侧 decimal pinning给

\[
\log_{10}\kappa=2S+O(1),
\qquad
\log_{10}(\kappa+2G)=2S+O(1).
\]

固定目标 Schmidt 给

\[
\log_{10}U+\log_{10}Z\ge S-o(S).
\]

2-resonance给

\[
H/S=2M+2Q_2+N_2-2G_2+o(1).
\]

消去 `U,Z,H,G_2` 后得到

\[
\boxed{
\frac{2(1+2a_2)}3M
+2a_2Q_2+a_2N_2
+\frac{b_5}{3}(2Q_5+4G_5+N_5)
+2R
\le3.
}
\tag{Subspace-defect-safe}
\]

所以 stronger Schmidt budget本身仍是可靠工具；失效的是把它与错误 5-adic branch tree
合并后的 whole-sector conclusions。

---

## 9. 当前安全 DD picture

截至本审计：

- 全局 tail：
  \[
  \boxed{\limsup m_3/S\le5}
  \]
  保持；
- non-dominant：由 `d<=S` 仍有
  \[
  \boxed{\limsup n_3/S\le6};
  \]
- 全 DD safe asymptotic：
  \[
  \boxed{\limsup n_3/S\le6.308883577618\ldots};
  \]
- equality frontier 的旧 strict 5-adic closure撤销；
- post-tail second-Schmidt 的 hard source改由
  `dd-corrected-hard-source-split-2026-08-22.md` 中的 `X_H` / `X_{H,D}` 记录；
- high-funnel 5-adic主接口改为 `(Xi-correct)`、`(Gap-correct)`、
  `(Subspace-defect-safe)`。

下一 quantitative target 应从 corrected hard-source / corrected high-funnel 两条线中寻找
真正独立于 unified discriminant normalization 的第二个 global reader。

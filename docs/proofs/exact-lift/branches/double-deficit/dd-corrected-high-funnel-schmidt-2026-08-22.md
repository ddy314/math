# DD corrected high-funnel：无 5-adic dichotomy 的 Schmidt bound

> **依赖：** [`dd-discriminant-root-dependency-audit-2026-08-22.md`](dd-discriminant-root-dependency-audit-2026-08-22.md)、
> [`high-funnel-ledger.md`](high-funnel-ledger.md) 中仍独立成立的 `t_2=1` S-unit phase、
> exact small-factor normalization、defect-stability，以及 [`core.md`](core.md) 的 decimal pinning / fixed-target Schmidt。
>
> **严格状态：** `已严格完成（corrected canonical t_2=1 double-resonant high funnel）`。
>
> 本文不使用已经撤销的 `high-funnel-five-adic-dichotomy`、旧 `Xi-slack`、
> denominator-max `Final-5-lock` 或 `general-transfer-local`。在统一判别根 normalization 修正后，
> 直接把 corrected 5-adic gap ledger、exact `F_-` factorization 与固定目标 Schmidt budget联立，
> 恢复
> \[
> \boxed{
> \limsup\frac nS
> \le
> 6.308883577618031\ldots.}
> \]
> 其 equality LP 仍唯一指向旧 `6.308883...` 比例射线；本文不排除该射线。

---

## 1. corrected high-funnel 5-adic data

记

\[
B_5=v_5(b_3),\qquad
E_5=\max_i v_5(b_i),
\]
\[
q_5=v_5(Q),\quad g_5=v_5(G),\quad n_5=v_5(\mathcal N_{12}),
\]
\[
k_5=v_5(\kappa).
\]

canonical high funnel 有

\[
5\mid b_3,\qquad k_5>g_5,
\]

以及 exact resonance / tail weight

\[
\boxed{3k_5=2m+2q_5+g_5+n_5,}
\tag{1.1}
\]

\[
\boxed{k_5=m+q_5+g_5-B_5.}
\tag{1.2}
\]

因此

\[
\boxed{3B_5=m+q_5+2g_5-n_5.}
\tag{1.3}
\]

对任何试图保持 slope `>6` 的无界 high-funnel sequence，旧的独立 lemma
`B_5>=m => n<6S+O(1)` 已经排除 `B_5>=m`；所以只需研究 eventually

\[
\boxed{B_5<m.}
\tag{1.4}
\]

令

\[
\delta_5:=E_5-B_5\ge0.
\]

`dd-discriminant-root-dependency-audit-2026-08-22.md` 已严格恢复

\[
\boxed{v_5(a)=v_5(\Xi)=q_5+\delta_5,}
\tag{1.5}
\]

以及

\[
\boxed{v_5(H_{\rm sph}-y_3)
=m+q_5+E_5-2B_5.}
\tag{1.6}
\]

定义 S-unit exponent

\[
\boxed{T:=k_5-g_5.}
\]

由 `(1.2)`：

\[
\boxed{T=m+q_5-B_5.}
\tag{1.7}
\]

所以 `(1.6)` 精确改写为

\[
\boxed{v_5(H_{\rm sph}-y_3)=T+\delta_5.}
\tag{Gap5-corrected}
\]

---

## 2. denominator-max deficit 在 `gap * overlap` 中精确消失

canonical `t_2=1` phase写

\[
G=\gamma V,
\qquad (V,10)=1.
\]

因此

\[
v_5(\gamma)=g_5.
\]

同时

\[
c_3:=q_{\rm lcm}/b_3
\]
满足

\[
v_5(c_3)=E_5-B_5=\delta_5.
\]

exact overlap normalization给

\[
\widehat g:=\frac{g_*}{V}=\frac\gamma{c_3}\in\mathbf Z_{>0}.
\]

所以

\[
\boxed{v_5(\widehat g)=g_5-\delta_5.}
\tag{2.1}
\]

与 `(Gap5-corrected)` 相加：

\[
\boxed{
v_5\bigl((H_{\rm sph}-y_3)\widehat g\bigr)
=T+g_5.}
\tag{Five-cancel}
\]

这一步很关键：`b_3` 是否为 5-adic maximum 完全不再需要分类。
若 prefix max 高出 `delta_5`，sphere gap恰多 `delta_5`，normalized overlap恰少
`delta_5`；二者乘积的实际 small-factor 5-depth不变。

---

## 3. corrected universal `F_-` lower

exact S-unit factorization为

\[
\boxed{
F_-
=2^{H+1}Z\,(H_{\rm sph}-y_3)\widehat g,
}
\tag{3.1}
\]

其中 `Z` 为 10-unit。

canonical funnel 中 `b_3` 是二进 unique maximum，所以

\[
v_2(c_3)=0,
\qquad
v_2(\widehat g)=v_2(\gamma)=:\mathfrak g.
\]

sphere gap 的 2-depth非负，因此从 `(3.1)` 安全得到（忽略绝对 `O(1)`）

\[
\log_{10}F_-
\ge
H\log_{10}2
+\mathfrak g\log_{10}2
+(T+g_5)\log_{10}5
+\log_{10}Z
-O(1).
\tag{3.2}
\]

令

\[
a:=\log_{10}2,\qquad b:=\log_{10}5=1-a,
\]

并记 normalized rough overlap

\[
R:=\frac{\log_{10}\gamma_0}{S},
\qquad
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0.
\]

S-unit pinning

\[
\kappa+2G=2\gamma2^HZ
\]

与 `log10(kappa+2G)=2S+O(1)` 给

\[
a\frac HS+rac{\log_{10}Z}{S}
=2-aG_2-bG_5-R+o(1),
\tag{3.3}
\]

其中

\[
G_2=\mathfrak g/S,\qquad G_5=g_5/S.
\]

把 `(3.3)` 代入 `(3.2)`，`G_2,G_5` 精确抵消：

\[
\boxed{
\frac{\log_{10}F_-}{S}
\ge
2+b\frac TS-R-o(1).
}
\tag{Fminus-corrected-lower}

这是替代旧 `Final-5` 分支 smooth lower 的统一 high-funnel inequality。

---

## 4. 与 Archimedean upper 联立

`high-funnel-defect-optimization.md` 的 d-dominant small-factor upper不依赖
5-adic dichotomy：

\[
\boxed{
\log_{10}F_-<4S+2m-n+O(1).}
\tag{4.1}
\]

沿任意实现 limsup 的 subsequence，记

\[
\mathcal N:=\limsup\frac nS,
\quad
M:=m/S,
\quad Q_5:=q_5/S,
\quad G_5:=g_5/S,
\quad N_5:=n_5/S.
\]

由 `(1.1)`：

\[
\boxed{
\frac TS
=\frac{2M+2Q_5-2G_5+N_5}{3}.}
\tag{4.2}
\]

`(Fminus-corrected-lower)` 与 `(4.1)` 因而给

\[
\boxed{
\begin{aligned}
\mathcal N
\le{}&2
+\frac{2(2+a)}3M
-\frac{2b}{3}Q_5
+\frac{2b}{3}G_5\\
&-\frac b3N_5+R.
\end{aligned}}
\tag{Corrected-stability}

---

## 5. stronger Schmidt budget 可独立恢复

令

\[
Q_2=\mathfrak q/S,\qquad N_2=\mathfrak n/S.
\]

canonical `t_2=1` phase有

\[
\kappa=2\gamma5^TU,
\qquad
\kappa+2G=2\gamma2^HZ,
\]

以及 fixed-target Schmidt

\[
\log_{10}U+\log_{10}Z\ge S-o(S).
\]

2-resonance给

\[
H/S=2M+2Q_2+N_2-2G_2+o(1).
\]

直接消去 `U,Z,H,G_2`，得到无需 `Final-5-lock` 的安全 budget：

\[
\boxed{
A M
+2aQ_2+aN_2
+\frac b3(2Q_5+4G_5+N_5)
+2R
\le3,
}
\tag{Schmidt-safe}
\]

其中

\[
\boxed{A:=\frac{2(1+2a)}3.}
\]

后续只需丢掉非负 `Q_2,N_2`，得到

\[
\boxed{
A M
+\frac b3(2Q_5+4G_5+N_5)
+2R
\le3.
}
\tag{5.1}

---

## 6. 闭式 dual：恢复 `6.308883...`

`Corrected-stability` 的 `M` coefficient为

\[
\frac{2(2+a)}3.
\]

取

\[
\boxed{
\lambda:=\frac{2+a}{1+2a}.}
\tag{6.1}
\]

则

\[
\lambda A=\frac{2(2+a)}3.
\]

将 `(5.1)` 乘 `lambda`：

- `M` coefficient与 `Corrected-stability` 正好相等；
- `Q_5,N_5` 在目标中本来就是非正 coefficient；
- 对 `G_5`，
  \[
  \lambda\frac{4b}{3}>\frac{2b}{3};
  \]
- 对 `R`，
  \[
  2\lambda>1.
  \]

所有 variables均非负，因此

\[
\boxed{
\mathcal N
\le2+3\lambda.}
\tag{6.2}

即

\[
\boxed{
\mathcal N
\le
2+3\frac{2+a}{1+2a}
=\frac{8+7a}{1+2a}.}
\tag{Corrected-6308}

数值为

\[
\boxed{
\frac{8+7\log_{10}2}{1+2\log_{10}2}
=6.308883577618031\ldots.}
\]

所以原 canonical high-funnel 的 Schmidt frontier常数在纠错后仍被恢复，
但证明不再经过任何 fake 5-adic valuation mismatch。

---

## 7. equality rigidity

上述 dual 中：

- `G_5` coefficient有严格正 slack；
- `R` coefficient有严格正 slack；
- `Q_5,N_5` 在 `Corrected-stability` 中为负，而 Schmidt combination中为非负。

因此若存在 sequence逼近 `(Corrected-6308)`，必须有

\[
\boxed{Q_5,G_5,N_5,R\to0.}
\tag{7.1}
\]

而 `(5.1)` 必须饱和，所以

\[
A M\to3.
\]

即

\[
\boxed{
M\to\frac3A
=\frac{9}{2(1+2a)}
=2.808883577618031\ldots.}
\tag{7.2}
\]

这正是旧 `6.308883...` equality frontier 的 tail ratio。

由 `Corrected-stability` equality再恢复

\[
\boxed{
d/S\to7/2.}
\]

其余 `U,Z,T,H` 比例可继续由 canonical S-unit pinning恢复为 `core.md` 已记录的旧 terminal ratios。

因此 corrected proof picture 是：

\[
\boxed{
\text{`6.308883...` frontier 仍是唯一 equality geometry，}
\text{但目前没有正确的 5-adic argument 将它排除。}}
\]

---

## 8. 与旧 high-funnel 文件的关系

本文取代下列用途：

1. 不再用 `Five-dichotomy` 把 funnel 人为分成 Tail-short / Defect-heavy；
2. 不再用错误 `Xi-slack` 进入 `Final-5-lock`；
3. 不再依赖 denominator-max nonmax `<=6`；
4. 不再需要合并旧 branch tree 才恢复 `6.308883...`。

仍可独立保留：

- `B_5>=m => n<6S+O(1)`；
- exact small-factor normalization；
- gap/recovery square identities；
- sphere `c_3` lower inequality；
- q-Z / projective identities在各自显式 hypotheses 下的局部内容。

当前下一目标很明确：若要获得 strict improvement，必须在 equality rigidity `(7.1)--(7.2)`
上找到一个**不来自 unified discriminant normalization**的新正线性 payer。

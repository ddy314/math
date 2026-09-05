# DD post-tail corrected split：explicit payer layers + hard source core

> **依赖：** [`dd-general-transfer-correction-2026-08-22.md`](dd-general-transfer-correction-2026-08-22.md)、
> [`tail-allocation-ledger.md`](tail-allocation-ledger.md) 中 `tail-rough-cq-excess`、
> `tail-rough-bottom-small-factor-charge`、`tail-rough-z0-only-frontier` 的 gap charge，
> 以及 `tail-pure-cancellation-three-sheet` 的 local identities。
>
> **严格状态：** `已严格完成（不使用已暂停的 General-transfer-local）`。
>
> general-transfer 修正后，不能再声称每个 source overflow 必定完全进入旧 numerator/projective
> payers。本文改用一个无需 contradiction theorem 的 canonical exponent allocation：
> 对每个 `p^x || X_Q`，依次分给 bottom coefficient、gap、prefix norm、third denominator，
> 余下部分定义为真正 hard source core。
>
> 该定义自动穷尽整个 `X_Q`。更重要的是，只要 hard residual 为正，旧 general-transfer proof
> 在错误判别根出现以前的有效部分就强制
> \[
> \alpha=t+(E-j)_+,
> \]
> 从而 hard residual 获得 exact source ledger
> \[
> \boxed{
> c=h+2t+n_0+\max(E,j)+j.
> }
> \]
> 于是 hard source 又可严格分成 source-square 与 deep-source 两层；真正可能保留 full `S`
> height 的只剩 baseline-dominating deep source core。

---

## 1. local notation

固定
\[
p^x\Vert X_Q,
\qquad p\nmid10.
\]
写
\[
E=v_p(b_1)=v_p(b_2),
\qquad
j=v_p(b_3),
\qquad
M:=\max(E,j),
\]
\[
c=v_p(C_Q),
\qquad
t=v_p(C)=v_p(A_{12}),
\]
\[
n_0=v_p(N_0),
\qquad
r=(j-E)_+,
\qquad
\alpha=v_p(a).
\]

`tail-rough-cq-excess` 已严格证明
\[
\boxed{
x=\max(c-j-\min(E,j),0).}
\tag{1.1}
本文只讨论 `x>0`。

---

## 2. 无需 transfer theorem 的五层定义

定义 remainder sequence：
\[
x_0:=x,
\]
\[
\boxed{e_B:=\min(x_0,t),\qquad x_1:=x_0-e_B,}
\tag{2.1}
\[
\boxed{e_a:=\min(x_1,\alpha),\qquad x_2:=x_1-e_a,}
\tag{2.2}
\[
\boxed{e_N:=\min(x_2,n_0),\qquad x_3:=x_2-e_N,}
\tag{2.3}
\[
\boxed{e_3:=\min(x_3,r),\qquad h:=x_3-e_3.}
\tag{2.4}

于是完全由定义得到
\[
\boxed{x=e_B+e_a+e_N+e_3+h.}
\tag{Corrected-local-split}

没有使用 `General-transfer-local`，也没有假设 `h=0`。

逐 prime 聚合定义
\[
X_B:=\prod p^{e_B},
\quad
X_a:=\prod p^{e_a},
\quad
X_N:=\prod p^{e_N},
\quad
X_3:=\prod p^{e_3},
\quad
X_H:=\prod p^h.
\]
因此全局严格有
\[
\boxed{
X_Q=X_BX_aX_NX_3X_H.
}
\tag{Corrected-global-split}

---

## 3. 前四层都有真实 reader

### bottom

因为 `e_B<=t` 且 `p^x|C_Q|Q`，
\[
p^{e_B}\mid(A_{12},Q).
\]
所以
\[
\boxed{X_B\mid C_{12}:=(A_{12},Q).}
\tag{3.1}

已有 exact bottom charge 对任意该因子成立：
\[
\boxed{X_BG<F_-.}
\tag{Bottom-charge-corrected}

### gap

由定义 `e_a<=alpha=v_p(a)`：
\[
\boxed{X_a\mid a.}
\tag{3.2}
而 existing gap factorization 给
\[
\boxed{X_aQ<F_-.}
\tag{Gap-charge-corrected}

### prefix norm

直接由 `e_N<=n_0`：
\[
\boxed{X_N\mid\operatorname{core}_{10}(N_0).}
\tag{3.3}

### third denominator

由 `e_3<=r=v_p(R_3^{\rm den})`：
\[
\boxed{X_3\mid\operatorname{core}_{10}(R_3^{\rm den}).}
\tag{3.4}

`R_3^{den}|Z_0a` 的 projective divisibility只使用 sphere/projective denominator formula，
不依赖已暂停的 general-transfer contradiction。因此仍有
\[
\boxed{X_3\mid\operatorname{core}_{10}(Z_0a).}
\tag{3.5}

唯一没有预先 reader 的就是 `X_H`。

---

## 4. hard residual 为正时自动进入 corrected hard sheet

若
\[
\boxed{h>0,}
\tag{4.1}
则 `(2.1)--(2.4)` 中四个 `min` 都必须取满容量：
\[
\boxed{
e_B=t,
\qquad e_a=\alpha,
\qquad e_N=n_0,
\qquad e_3=r.}
\tag{4.2}

特别地
\[
x>t,
\qquad x>n_0,
\qquad x>r.
\tag{4.3}
所以 `dd-general-transfer-correction` 中的 hard hypothesis成立。

旧 general-transfer proof 的 §1–4 不使用错误的 unified/gap root identification；其
`Gap-baseline-lock` 因而仍给
\[
\boxed{
\alpha=t+(E-j)_+.
}
\tag{Gap-lock-hard}

于是
\[
\boxed{
h=x-t-\alpha-n_0-r.}
\tag{4.4}

---

## 5. hard source 的 exact ledger

将 `(1.1)` 与 `(Gap-lock-hard)` 代入 `(4.4)`。

### `E>=j`

此时
\[
x=c-2j,
\qquad
\alpha=t+E-j,
\qquad
r=0.
\]
故
\[
\begin{aligned}
h
&=c-2j-t-(t+E-j)-n_0\\
&=c-2t-n_0-E-j.
\end{aligned}
\]

### `j>E`

此时
\[
x=c-j-E,
\qquad
\alpha=t,
\qquad
r=j-E.
\]
故
\[
\begin{aligned}
h
&=c-j-E-t-t-n_0-(j-E)\\
&=c-2t-n_0-2j.
\end{aligned}
\]

两式用 `M=max(E,j)` 统一为
\[
\boxed{
 c=h+2t+n_0+M+j.
}
\tag{Hard-source-ledger}

定义 local hard cofactor depth
\[
\boxed{
y:=c-h=2t+n_0+M+j.}
\tag{5.1}
于是
\[
\boxed{c=h+y}
\tag{5.2}
为 exact equality。

这条 equality 是 corrected post-tail 中替代“`h=0`”的核心结构。

---

## 6. hard source-square / deep 二分

对 `h>0` 的 prime 按
\[
\boxed{h\le y}
\tag{6.1}
与
\[
\boxed{h>y}
\tag{6.2}
分类。

### source-square hard part

若 `h<=y`，则
\[
2h\le h+y=c,
\]
所以
\[
\boxed{p^{2h}\mid C_Q.}
\tag{Hard-square-local}

令
\[
X_{H,S}:=\prod_{h\le y}p^h.
\]
各 prime support 不交，故
\[
\boxed{X_{H,S}^2\mid C_Q.}
\tag{Hard-square-global}

于是
\[
\boxed{
\log_{10}X_{H,S}<\frac S2.
}
\tag{Hard-square-half-S}

### deep hard source

若 `h>y`，定义
\[
X_{H,D}:=\prod_{h>y}p^h,
\qquad
Y_{H,D}:=\prod_{h>y}p^y.
\]
由 `(5.2)`：
\[
\boxed{X_{H,D}Y_{H,D}\mid C_Q.}
\tag{Deep-hard-source-product}

并且逐 prime
\[
\boxed{y<h.}
\tag{6.3}

把 cofactor进一步按 exact layers写成
\[
T_H:=\prod p^t,
\quad
N_H:=\prod p^{n_0},
\quad
M_H:=\prod p^M,
\quad
J_H:=\prod p^j
\]
（均只在 deep-hard support上），则
\[
\boxed{
Y_{H,D}=T_H^2N_HM_HJ_H.
}
\tag{Deep-hard-cofactor}

所以
\[
\boxed{
\log X_{H,D}
+2\log T_H
+\log N_H
+\log M_H
+\log J_H
<S.
}
\tag{Deep-hard-height-tradeoff}

若 `X_{H,D}` 接近整份 `S` 高度，则 coefficient、prefix norm 与全部 denominator maximum
baseline都自动只有 sublinear aggregate height。

这比原 `X_Q` frontier 更精确：唯一 full-height escape 必须是一个
**asymptotically baseline-free pure source cancellation core**。

---

## 7. corrected second-Schmidt bootstrap

`tail-rough-cq-excess` 的原始、仍有效 second-Schmidt inequality为
\[
\log R_x+\log(g_*/v)
\ge S-\log X_Q-o(S),
\]
左侧是真实 `F_-` factors，因此写 `f=log F_-`：
\[
f\ge S-\log X_Q-o(S).
\tag{7.1}

由 `Corrected-global-split`：
\[
\log X_Q
=\log X_B+\log X_a
+\log X_N+\log X_3+\log X_H.
\]

而两条 exact small-factor charge给
\[
\log X_B\le f-S+O(1),
\qquad
\log X_a\le f-S+O(1).
\]
代回 `(7.1)`：
\[
\boxed{
3f+\log(X_NX_3X_H)
\ge3S-o(S).
}
\tag{Corrected-triple-bootstrap}

这是此前 triple bootstrap 的 corrected version：
它不再把 residual 错误识别成 `Z_0-only`；真正 residual 是
\[
\boxed{X_NX_3X_H.}
\]
其中前两项有 concrete norm/projective readers，最后一项再按
\[
X_H=X_{H,S}X_{H,D}
\]
分成 half-`S` source-square 与 deep pure-source core。

---

## 8. deep source 对 bootstrap 的 exact tradeoff

若暂时把其它 residual reader单独记账，只看 deep-hard contribution `X_{H,D}`，
`Deep-hard-source-product` 给
\[
\log X_{H,D}\le S-\log Y_{H,D}+O(1).
\]
所以它在 `Corrected-triple-bootstrap` 中造成的最坏 loss可改写为 source-cofactor tradeoff。

特别地，危险极限
\[
\log X_{H,D}=S-o(S)
\]
自动强迫
\[
\boxed{
\log Y_{H,D}=o(S),
}
即
\[
\log T_H,
\quad\log N_H,
\quad\log M_H,
\quad\log J_H
=o(S).
\]

因此下一步无需再对 generic denominator/common-norm 情形使用局部 contradiction；
真正需要新的 global theorem 的情形已经压成：

\[
\boxed{
\begin{gathered}
X_{H,D}\mid C_Q,\qquad
\log X_{H,D}=S-o(S),\\
\text{coefficient / prefix norm / denominator baselines}=10^{o(S)},\\
\text{local unit-Hensel 已由 sphere-parent 精确支付，无独立 local height。}
\end{gathered}}
\tag{Pure-source-terminal}

这说明 corrected frontier 的下一机制必须真正是 global source/digit-shell mechanism。

---

## 9. 与旧 Gaussian continuation 的关系

若某个 explicit `X_N` layer进一步含 genuine primitive split-Gaussian angular depth，则
`tail-rough-angular-source-transfer` 及本分支最近的 oriented identities仍可在该**已确认的 local
Gaussian sheet**内使用。

但它们不再覆盖 `X_H`。因此当前证明树应分成两条独立 continuation：

1. `X_N / X_3` explicit-reader continuation：Gaussian / projective / carrier geometry；
2. `X_{H,D}` pure-source continuation：global decimal cancellation。

第二条才是 general-transfer correction 后新增、不能省略的主 hard branch。

---

## 10. 状态摘要

- **`已严格完成`**：无需 transfer theorem 的 `Corrected-local/global-split`。
- **`已严格完成`**：`Hard-source-ledger`。
- **`已严格完成`**：hard source-square/deep split与 `Deep-hard-height-tradeoff`。
- **`已严格完成`**：`Corrected-triple-bootstrap`。
- **`结构压缩`**：唯一可能保留 full `S` height 的新增 obstruction 是
  asymptotically baseline-free `X_{H,D}` pure-source core。
- **`待证`**：`X_N/X_3` simultaneous height；`X_{H,D}` global digit-shell control；
  corrected non-canonical LP；DD global `<=6` / absolute height。

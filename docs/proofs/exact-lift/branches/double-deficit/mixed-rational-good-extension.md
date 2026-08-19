# DD mixed frontier：partial rational core 的 Bad closure 与 Good normalization

> **依赖：** `frontier.md` 的 rational/genuine split、Bad elimination、Good slot theorem；[`good-radius-excess.md`](good-radius-excess.md)、[`good-axis-normalization.md`](good-axis-normalization.md)。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。旧 continuation 最终在 full rational-contact 情形 `E=D_+D_-=C_L^{1-o(1)}` 中关闭 Bad，并发展 Good slot / excess normalization。本文审计证明：Bad closure 的 local prime-support argument实际上不要求 `E` 占满 `C_L`。对任意 mixed split
> \[
> E\cdot C_G=C_L\cdot10^{o(S)},
> \]
> partial rational-contact main prime仍无法由 `e_0=V/E` 中的 genuine complement支付，因为它们是不同 prime support。因此 Bad 在 partial rational core中仍只有 `10^{o(S)}` mass；剩余 rational-contact main mass全部进入 Good。
>
> 同时，Good 的 local slot theorem、axis-normalized excess与 gcd ladder只依赖 target prime上的 unit ledger，故可将原 full-rational `C_L` 无损替换为 partial rational core `E`。

---

## 1. mixed rational/genuine split

沿用

\[
R_+=b+A,
\qquad
R_-=b-A,
\]

\[
D_+=(V,R_+),
\qquad
D_-=(V,R_-).
\]

定义 rational-contact main core

\[
\boxed{E:=D_+D_-}
\tag{1.1}

并定义 genuine complement

\[
\boxed{C_G:=\frac{C_L}{E}}
\tag{1.2}

均按删除 `10^{o(S)}` coefficient / sign-overlap exceptional core后理解。

已有 split 给

\[
\boxed{
EC_G=C_L\cdot10^{o(S)},
\qquad
(E,C_G)=10^{o(S)}.
}
\tag{1.3}

写

\[
\boxed{V=Ee_0.}
\tag{1.4}

由于

\[
V=C_Lv_0,
\]

有

\[
e_0=C_Gv_0\cdot10^{o(S)}.
\tag{1.5}

关键点：虽然 `e_0` 的**高度**在 mixed branch可以是正线性的，但对任一 main prime

\[
p^h\Vert E
\]

删除 `(E,v_0)` exceptional overlap后仍有

\[
\boxed{p\nmid e_0.}
\tag{1.6}

不同 genuine primes不会支付这个 rational prime的 same-prime divisibility。

---

## 2. Bad tangent elimination 不使用 `e_0=o(S)` 直到最后一步

旧 Bad elimination 对 `D_+` / `D_-` 的 main Bad subcores给出 oriented tangent congruences

\[
\boxed{
B_+^{\flat}\mid d h_+ + b j_+,
}
\tag{2.1+}

\[
\boxed{
B_-^{\flat}\mid b j_- - d h_-.
}
\tag{2.1-}

其中 `B_sigma^flat` 与 Bad main mass只差 `10^{o(S)}` exceptional core。

再利用 sign-Farey identities 与

\[
Ac-bd=ET_c,
\]

旧证明把同一个 oriented Bad prime-power继续压入

\[
\boxed{
T_c=e_0\widetilde r^{\,2}5^{T-m_2}.
}
\tag{2.2}

这一步是逐 prime 的 divisibility statement；并没有使用

\[
\log e_0=o(S).
\]

full-rational 旧稿只在最后用 `e_0=o(S)` 把 Bad 总质量判成 `o(S)`。

---

## 3. mixed split 中同一个 Bad prime仍不能进入 `T_c`

固定 main Bad prime

\[
p^h\Vert B_\sigma^{\flat}\mid E.
\]

由 `(1.6)`：

\[
p\nmid e_0.
\]

main coefficient-unit ledger还给

\[
p\nmid\widetilde r5.
\]

因此

\[
\boxed{p\nmid T_c.}
\tag{3.1}

但 Bad elimination要求该 same prime进入 `(2.2)`，矛盾。

所以删除 exceptional core后没有 main Bad prime：

\[
\boxed{B_+^{\flat}=B_-^{\flat}=1.}
\tag{3.2}

恢复 exceptional factors：

\[
\boxed{
\log(B_+B_-)=o(S)
}
\tag{Partial-Bad-closed}

对**任意** rational/genuine mixed split成立。

这比旧状态更强：Bad closure不是 full-rational 专属结论。

---

## 4. partial rational-contact main mass 因而几乎全是 Good

令 rational-contact main mass分解为

\[
E=B_R G_R
\]

其中 `B_R` 为 Bad、`G_R` 为 Good，忽略 `10^{o(S)}` overlap。

由 `(Partial-Bad-closed)`：

\[
\boxed{
G_R=E\cdot10^{o(S)}.
}
\tag{Partial-Good-main}

因此以后 mixed branch中的 rational-contact prime可直接按 Good local ledger处理；无需再保留正线性 Bad 子支。

---

## 5. Good slot theorem 对 partial `E` 原样成立

在每个

\[
p^h\Vert E^{\rm main}
\]

上，sign contact仍使用完整 prime-power depth。写

\[
R_\pm=D_\pm h_\pm,
\qquad
J_\pm=D_\pm j_\pm,
\]

\[
H_R=h_+h_-,
\qquad
H_J=j_+j_-.
\]

axis norm满足

\[
C_*^2+R_0^2=EN_c
\tag{5.1}

定义 integer `N_c`。

Good selected/conjugate exclusion的证明逐 prime使用：

- target `p` 在 `E` 中的完整 contact depth；
- `p\nmid e_0`；
- coefficient units；
- Bad / conjugate exceptional exclusion。

这些条件在 §3 后的 partial main core全部保留。因此原 slot theorem仍成立：若

\[
r_p=v_p(H_R),
\quad
j_p=v_p(H_J),
\quad
n_p=v_p(N_c),
\]

则

\[
\boxed{\min(r_p,j_p)=0,}
\tag{Slot-RJ-partial}

\[
\boxed{\min(j_p,n_p)=0.}
\tag{Slot-JN-partial}

radius split同样为

\[
\boxed{
a_p=\min(r_p,n_p)+\varepsilon_p,}
\tag{Radius-partial}

\[
\boxed{
\varepsilon_p>0\Longrightarrow r_p=n_p.
}
\tag{Equal-partial}

其中

\[
a_p=v_p(A_0)=v_p(\alpha)
\]

沿用 `Radius=Concat`。

---

## 6. axis-normalized excess 公式也不需要 `E=C_L`

`good-axis-normalization.md` 的局部证明只使用 `(Radius-partial)` 与 `(Equal-partial)`，故立即得到

\[
\boxed{
\varepsilon_p
=\max(v_p(\alpha)-v_p(N_c),0).
}
\tag{6.1}

所以对 partial rational core定义

\[
\boxed{
E_N:=\frac{E}{(E,N_c)},
}
\tag{6.2}

\[
\boxed{
A_N:=\frac{\alpha}{(\alpha,N_c)}.
}
\tag{6.3}

则逐 `p^h||E`：

\[
v_p(E_N)=\max(h-v_p(N_c),0),
\]

\[
v_p(A_N)=\varepsilon_p.
\]

定义 partial rational excess

\[
\boxed{
G_{\rm exc}^{(R)}
:=\gcd(E_N,A_N).
}
\tag{6.4}

它正是旧 full-rational `G_exc` 在 mixed split中的自然替代。

---

## 7. gcd ladder 原样延伸

对

\[
k\ge1
\]

定义

\[
\boxed{
D_k^{(R)}:=\gcd(E_N^k,A_N).
}
\tag{7.1}

则逐 main rational prime：

\[
\boxed{
v_p(D_k^{(R)})
=\min\left(
k\max(h-v_p(N_c),0),
\varepsilon_p
\right).
}
\tag{7.2}

第一层为

\[
\boxed{D_1^{(R)}=G_{\rm exc}^{(R)}.}
\tag{7.3}

稳定层、denominator deficit / numerator overflow separation与旧 `good-excess-gcd-ladder.md` 完全相同，只需将

\[
C_N\rightsquigarrow E_N.
\]

所以 mixed frontier 的 rational Good困难仍可 canonical 化，而无需 full-rational 假设。

---

## 8. 与 large-genuine threshold 的合并

`genuine-large-core-crt.md` 已证明：若

\[
c:=\frac{\log C_G}{S}
>0.382232844764\ldots,
\]

则 fixed genuine fiber中 `A_12` 至多一个。

其补集满足

\[
\frac{\log E}{S}
\ge0.617767155236\ldots+o(1).
\]

本文说明该 rational-heavy mass并不会分散到 Bad；它几乎全部进入 Good：

\[
\boxed{
\frac{\log G_R}{S}
\ge0.617767155236\ldots+o(1).
}
\tag{8.1}

因此 large-genuine threshold以下的真正未决核已经压成：

\[
\boxed{
\text{至少 }0.617767155236\ldots S
\text{ 的 partial-rational Good core}
}
\]

加上至多 `0.382232844764...S` 的 orientation-locked genuine complement。

下一步可以直接对这个 quantitative mixed Good core重做 axis/excess mass ledger；不需要再考虑 Bad。

---

## 9. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：partial rational Bad closure、partial Good main reduction、slot theorem extension、axis-normalized excess公式、partial `E_N/A_N/G_exc^(R)` 与 gcd ladder。
- **`有限/结构结论`**：large-genuine threshold以下 rational Good mass至少 `0.617767155236...S`。
- **`待证`**：partial Good quantitative mass allocation；`G_exc^(R)` strict digit-shell bound；mixed/genuine frontier emptiness；DD 全局空性。

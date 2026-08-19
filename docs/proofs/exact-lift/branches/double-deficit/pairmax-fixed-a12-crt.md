# DD one-channel pair-max 的 split-independent fixed `A_12` CRT

> **依赖：** `frontier.md` 的 one-channel pair-max reduction、sphere carrier、exact carry；[`genuine-elliptic-collapse.md`](genuine-elliptic-collapse.md) 中的 `Sphere-pay-identity`；[`genuine-a12-fixed-crt.md`](genuine-a12-fixed-crt.md) 的 carry-square extraction 模板。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。此前 W-free carrier
> \[
> \Theta=(\kappa+G)Q(a_2b_1)^2\beta+\mathscr T a_3^2
> \]
> 是在 genuine orientation audit 中发现的，但其 `Sphere-pay-identity` 实际只依赖 one-channel pair-max sphere depth，完全不使用 rational/genuine split。本文因此将其全局化到整个 main `C_L`，证明
> \[
> (C_L^{\rm main})^2\mid\Theta.
> \]
> 再代入 exact decimal carry，得到一个 coefficients 固定、effective period为整个 `C_L` 的线性 `A_12` congruence。与 clean-source `q_c^2` period 联立后，**任意 terminal frontier fixed fiber** 中 `A_12` / `a_1` 都至多一个；此前 `c>0.382232...` 的 large-genuine threshold因此降级为被本文统一结论覆盖的中间分支结果。
>
> 本文仍只给 uniqueness/counting，不证明唯一 candidate 不存在。

---

## 1. 全 main pair-max 的共同 unit ledger

one-channel reduction已经把 moving pair-max main core全部放入 `(b_2,b_3)` channel。固定

\[
p^h\Vert C_L^{\rm main}.
\]

删除 all-three/common、coefficient 与 rough overlaps 的 `10^{o(S)}` exceptional core后：

\[
\boxed{
v_p(b_2)=v_p(b_3)=v_p(q)=h,}
\tag{1.1}

\[
\boxed{p\nmid b_1a_2a_3Q10.}
\tag{1.2}

写

\[
G=b_1b_2,
\qquad y:=a_2b_1.
\]

则

\[
\boxed{v_p(G)=h,\qquad p\nmid y.}
\tag{1.3}

这些结论对 rational-contact / genuine 两类 main prime完全相同。

---

## 2. original sphere norm 在每个 main prime上有 `4h` 深度

定义

\[
\boxed{
\mathcal S_{\rm raw}
:=y^2b_3^2+G^2a_3^2
=b_1^2\left[(a_2b_3)^2+(a_3b_2)^2\right].
}
\tag{2.1}

pair-max Gaussian sphere carrier给

\[
\Pi^2\mid y_2+i y_3,
\qquad N(\Pi)=C_L.
\]

对当前 `p^h`，清除

\[
y_2=a_2q/b_2,
\qquad
y_3=a_3q/b_3
\]

中的 p-unit quotient后，得到 normalized square-depth

\[
p^{2h}\mid
 a_2^2(b_3/p^h)^2
+a_3^2(b_2/p^h)^2.
\]

重新乘回 shared denominator baseline `p^{2h}`：

\[
\boxed{p^{4h}\mid\mathcal S_{\rm raw}.}
\tag{Sphere-raw-global}

因此

\[
\boxed{(C_L^{\rm main})^4\mid\mathcal S_{\rm raw}}
\tag{2.2}

按 main-primary depth理解。

---

## 3. W-free `Theta` 的 sphere-pay identity本来就是 split-independent

定义

\[
T_3:=10^{m_3},
\qquad
A_c:=Qy^2,
\]

\[
\boxed{
\mathscr T:=\frac{\kappa^2(\kappa+2G)}{T_3}\in\mathbf Z_{>0},
}
\tag{3.1}

以及

\[
\boxed{
\Theta
:=(\kappa+G)A_c\beta+\mathscr T a_3^2.
}
\tag{3.2}

`genuine-elliptic-collapse.md` 已机械验证 exact identity

\[
\boxed{
T_3G^2\Theta
=\kappa\left[
\kappa(\kappa+2G)\mathcal S_{\rm raw}
+G^2y^2b_3^2
\right].
}
\tag{Sphere-pay-global}

它的推导只使用

\[
\beta=T_3Q+b_3,
\qquad
\kappa b_3=T_3QG,
\]

以及

\[
(\kappa+G)^2=\kappa(\kappa+2G)+G^2.
\]

**没有使用**：

- `A≡±b`；
- `D_±`；
- rational-contact；
- genuine complement；
- same/opp orientation。

所以 `(Sphere-pay-global)` 对整个 one-channel main core都成立。

---

## 4. 全局得到 `C_L^2 | Theta`

固定 `p^h||C_L^{main}`。

由 `(Sphere-raw-global)`：

\[
v_p(\mathcal S_{\rm raw})\ge4h.
\]

第二项显然满足

\[
v_p(G^2y^2b_3^2)=4h.
\]

同时 main unit ledger给

\[
p\nmid T_3\kappa.
\]

所以 `(Sphere-pay-global)` 右端至少有 `4h` 深度，而左端显式 `G^2` 含恰好 `2h`。故

\[
\boxed{v_p(\Theta)\ge2h.}
\tag{4.1}

聚合全部 main prime-powers：

\[
\boxed{
(C_L^{\rm main})^2\mid\Theta.
}
\tag{Pairmax-Theta}

这是真正 split-independent 的 W-free square-depth carrier。

注意它完全由 sphere carrier支付；本文仍不把该 depth算作新的 local height surplus。

---

## 5. exact carry平方展开

沿用

\[
V=C_Lv_0,
\tag{5.1}

以及 exact carry

\[
\boxed{
g_0Ua_3
=g_0B10^dVA_{12}-\Sigma R_0.}
\tag{Carry}

把 `(Carry)` 平方：

\[
\begin{aligned}
g_0^2U^2a_3^2
={}&g_0^2B^210^{2d}V^2A_{12}^2\\
&-2g_0B10^dV\Sigma R_0A_{12}
+\Sigma^2R_0^2.
\end{aligned}
\tag{5.2}

代入 `g_0^2U^2 Theta`：

\[
\begin{aligned}
g_0^2U^2\Theta
={}&H_{L,0}
-2\mathscr T g_0B10^dV\Sigma R_0A_{12}\\
&+\mathscr T g_0^2B^210^{2d}V^2A_{12}^2,
\end{aligned}
\tag{5.3}

其中定义 split-independent constant part

\[
\boxed{
H_{L,0}
:=g_0^2U^2(\kappa+G)A_c\beta
+\mathscr T\Sigma^2R_0^2.
}
\tag{5.4}

`H_{L,0}` 不含

\[
A_{12},\quad a_3,\quad W,
\]

也不依赖 rational/genuine orientation split。

---

## 6. 第一层 `C_L` 自动进入 constant part

由 `(Pairmax-Theta)`：

\[
(C_L^{\rm main})^2
\mid g_0^2U^2\Theta
\]

（删去 `g_0U` coefficient overlap）。

在 `(5.3)` 中：

- linear term含 `V=C_Lv_0`，故至少一层 `C_L`；
- quadratic term含 `V^2`，故至少两层 `C_L`。

所以模 `C_L` 只剩 constant part：

\[
\boxed{C_L^{\rm main}\mid H_{L,0}.}
\tag{6.1}

定义 integer quotient

\[
\boxed{
M_{L,0}:=\frac{H_{L,0}}{C_L^{\rm main}}.
}
\tag{6.2}

为简洁，下文把删除 exceptional core后的 `C_L^{main}` 仍写作 `C_L`。

---

## 7. split-independent fixed `C_L` residue

把 `(5.3)` 除以 `C_L`，使用

\[
V=C_Lv_0.
\]

得到

\[
\begin{aligned}
\frac{g_0^2U^2\Theta}{C_L}
={}&M_{L,0}
-2\mathscr T g_0B10^d v_0\Sigma R_0A_{12}\\
&+C_L\mathscr T g_0^2B^210^{2d}v_0^2A_{12}^2.
\end{aligned}
\tag{7.1}

左边仍被 `C_L` 整除；最后一项显式含 `C_L`。因此：

\[
\boxed{
2\mathscr T g_0B10^d v_0\Sigma R_0A_{12}
\equiv M_{L,0}
\pmod{C_L}.
}
\tag{Pairmax-GCRT0}

这就是整个 moving pair-max core上的 fixed decimal reader。

---

## 8. effective period 为完整 `C_L`

对 main `p^h||C_L`，需审计 coefficient

\[
2\mathscr T g_0B10^d v_0\Sigma R_0.
\]

main setup已经删除

\[
p\mid2\cdot5\cdot g_0BR_0v_0
\]

的 `10^{o(S)}` exceptional core。

另外：

### 8.1 `Sigma` 是 p-unit

由

\[
V=X-Y\equiv0\pmod p
\]

且 `X,Y` 为 p-units，

\[
\Sigma=X+Y\equiv2Y\not\equiv0\pmod p.
\]

故

\[
p\nmid\Sigma.
\tag{8.1}

### 8.2 `mathscr T` 是 p-unit

统一 tail-root linearization给

\[
\mathscr T a_3
=\kappa G^2C_{\rm DD}+\eta(\kappa+G)W.
\]

main p上 `G≡0`，而 `a_3,\kappa,W` 为 units，所以

\[
\mathscr T a_3
\equiv\eta\kappa W\not\equiv0\pmod p.
\]

故

\[
p\nmid\mathscr T.
\tag{8.2}

因此 `(Pairmax-GCRT0)` 的 effective period为

\[
\boxed{C_L/10^{o(S)}}.
\tag{8.3}

---

## 9. 与 fixed `q_c^2` residue 联立

clean-source exact identity已经给

\[
\boxed{
g_0B10^dVA_{12}-XR_0
=Uq_c^2L_{\rm clean}.}
\tag{9.1}

所以

\[
\boxed{
g_0B10^dVA_{12}
\equiv XR_0\pmod{q_c^2}.}
\tag{Q-fixed}

其 effective period为

\[
q_c^2/10^{o(S)}.
\]

同时

\[
(C_L,q_c)=10^{o(S)}.
\]

故 `(Pairmax-GCRT0)` 与 `(Q-fixed)` 的联合 period为

\[
\boxed{
M_{\rm pairmax}
=\frac{C_Lq_c^2}{10^{o(S)}}.
}
\tag{9.2}

frontier heights：

\[
\log C_L=S+o(S),
\]

\[
\log q_c=z_*S+o(S),
\qquad
z_*=0.308883577618\ldots.
\]

所以

\[
\boxed{
\log M_{\rm pairmax}
=1.617767155236\ldots S+o(S).
}
\tag{Full-period-height}

---

## 10. universal fixed-fiber prefix uniqueness

prefix polarization给

\[
\boxed{\log A_{12}=S+o(S).}
\]

固定 terminal denominator/source/small-prefix fiber，使两个 congruences的 coefficients、RHS、`C_L,q_c` 固定。

若有两个不同合法

\[
A_{12}^{(1)}\ne A_{12}^{(2)}
\]

同时满足 `(Pairmax-GCRT0)` 与 `(Q-fixed)`，则

\[
M_{\rm pairmax}
\mid A_{12}^{(1)}-A_{12}^{(2)}.
\]

但

\[
|A_{12}^{(1)}-A_{12}^{(2)}|
<10^{S+o(S)},
\]

而

\[
M_{\rm pairmax}
=10^{1.617767155236\ldots S+o(S)}.
\]

sufficiently large `S` 矛盾。因此：

\[
\boxed{
\#\{A_{12}\text{ in any fixed terminal frontier fiber}\}\le1.
}
\tag{Universal-A12-unique}

固定 subexponential suffix `(n_2,a_2)` 后同样有

\[
\boxed{
\#\{a_1\text{ in the fixed fiber}\}\le1.
}
\tag{Universal-a1-unique}

这不再需要 rational/genuine split或 genuine-mass threshold。

---

## 11. 对此前分支结果的更新

本文说明以下中间状态需要降级：

1. `genuine-large-core-crt.md` 的 threshold
   \[
   c>0.382232844764\ldots
   \]
   仍是正确 sufficient condition，但已被 `Universal-A12-unique` 全面覆盖；不再是当前 frontier 的真实分支边界。
2. full-rational `GCRT+` 的 period仍是正确局部 reader，但不再需要靠 rational contact才能获得 `C_L`-级 second-order decimal period；`Pairmax-GCRT0` 已统一覆盖整个 one-channel core。
3. rational/genuine mixed split仍可用于其他 cofactor/slot 分析，但 **prefix uniqueness 不再依赖该 split**。

---

## 12. no-double-count 与未解决部分

`Pairmax-GCRT0` 的 `C_L` period来自 sphere-paid `Theta` depth。因此它可用于：

- CRT uniqueness；
- candidate counting；
- digit-shell location。

不能把 `C_L` 再当作 sphere square-depth之外的新 local height surplus。

本文仍没有证明唯一 CRT lift不落入合法 decimal window。因此 DD frontier emptiness依然开放。

真正下一步已压成：

> 对 split-independent 联合 CRT
> \[
> A_{12}\pmod{C_Lq_c^2}
> \]
> 的唯一 lift做 Archimedean digit-window location，或者构造一个不由 sphere/carry/clean-source parents重构的第三 fixed residue。

---

## 13. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：global `Sphere-raw-4h`、split-independent `C_L^2|Theta`、fixed `Pairmax-GCRT0`、effective period `C_L`、与 `q_c^2` 联合 period `1.617767155236...S`、universal fixed-fiber `A_12/a_1` uniqueness。
- **`失效/降级`**：将 `c>0.382232844764...` 当作当前必要分支阈值；认为只有 full-rational / large-genuine 才有 `C_L`-级 prefix period。
- **`有限/计数结论`**：universal uniqueness仍不是 emptiness。
- **`待证`**：unique CRT lift的 Archimedean location；独立第三 fixed residue若存在；DD frontier emptiness与全局 DD closure。

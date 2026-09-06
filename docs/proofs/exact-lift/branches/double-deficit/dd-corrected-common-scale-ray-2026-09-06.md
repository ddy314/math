# DD corrected terminal 的 cofactor projective lock 与 common-scale ray

> 日期：2026-09-06
>
> 依赖：[`dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md`](dd-corrected-terminal-two-adic-uz-neighborhood-2026-08-22.md)、[`dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md`](dd-corrected-terminal-one-channel-neighborhood-2026-08-22.md)、[`dd-corrected-terminal-digit-polarization-2026-08-22.md`](dd-corrected-terminal-digit-polarization-2026-08-22.md)、[`dd-corrected-terminal-denominator-sunit-entropy-2026-08-22.md`](dd-corrected-terminal-denominator-sunit-entropy-2026-08-22.md)、[`dd-corrected-denominator-product-lock-2026-09-06.md`](dd-corrected-denominator-product-lock-2026-09-06.md)。
>
> **严格状态：已严格完成（corrected canonical `t_2=1` terminal neighborhood 的 denominator-side projective reconstruction theorem）。**
>
> 本文处理旧 denominator/S-unit entropy theorem 中仍被作为独立整数枚举的 rough overlap `gamma_0`。关键结论是：在一个显式正宽度 neighborhood 内，固定 S-unit phase 与 `V=v_1v_2` 的 factor split 后，所有 cofactor pairs 不再形成二维整数族，而只能落在同一条 primitive rational ray 上。进一步利用 `Q=Uq`，整条 denominator family 精确写成
>
> \[
> \boxed{
> (b_1,b_2,b_3,q,\gamma)
> =
> (\ell\bar b_1,\ell\bar b_2,\ell\bar b_3,
> \ell\bar q,\ell^2\bar\gamma).
> }
> \]
>
> 因此 fixed phase/factor split 中 rough `gamma` 的可移动部分本质上是 **common denominator scale**，不是第二个独立 projective denominator shape。这个结论不证明 DD 为空；它把 denominator residual core 从“Farey phase + rough gamma integer + factor assignments”压成“Farey phase + divisor factor split + one common scale ray”。

---

## 1. notation 与 quantitative bounds

令

\[
a:=\log_{10}2,
\qquad
U_*:=0.691116422381969\ldots.
\]

quantitative digit polarization 给

\[
\boxed{
\frac{m_1}{S}
\le
\kappa_{\rm dig}\delta+o(1),
\qquad
\kappa_{\rm dig}
=\frac{2+a}{3}
=0.767009998554660\ldots.
}
\tag{1.1}
\]

one-channel theorem 给

\[
\boxed{
\frac{\log_{10}v_2}{S}
\ge1-C_{\rm one}\delta-o(1),
}
\]

以及其直接 consequence

\[
\boxed{
\frac1S\log_{10}\frac{b_2}{v_2}
\le C_{\rm one}\delta+o(1),
}
\tag{1.2}
\]

其中

\[
\boxed{
C_{\rm one}
=1+\frac{5(1+2a)}6
=2.335049992773302\ldots.
}
\tag{1.3}
\]

`U` 的 corrected lower window 为

\[
\boxed{
\frac{\log_{10}U}{S}
\ge
U_*-(1+a)\delta-o(1).
}
\tag{1.4}
\]

沿 denominator entropy theorem 写

\[
\boxed{V=v_1v_2,}
\qquad
v_i\mid b_i,
\]

并为避免与 canonical phase 标签 `t_2=1` 混淆，定义新的 cofactor 记号

\[
\boxed{
\tau_1:=\frac{b_1}{v_1},
\qquad
\tau_2:=\frac{b_2}{v_2}.}
\tag{1.5}
\]

由

\[
G=b_1b_2=\gamma V
\]

有 exact identity

\[
\boxed{\tau_1\tau_2=\gamma.}
\tag{1.6}
\]

从 `(1.1)` 与 `v_1>=1`：

\[
\boxed{
\frac{\log_{10}\tau_1}{S}
\le\kappa_{\rm dig}\delta+o(1).}
\tag{1.7}
\]

从 `(1.2)`：

\[
\boxed{
\frac{\log_{10}\tau_2}{S}
\le C_{\rm one}\delta+o(1).}
\tag{1.8}
\]

---

## 2. denominator concat 给 modulo `U` 的 cofactor projective line

prefix concat 与 canonical source split为

\[
\boxed{
Q=b_1 10^{m_2}+b_2=Uq.}
\tag{2.1}
\]

代入 `(1.5)`：

\[
\boxed{
v_1 10^{m_2}\tau_1+v_2\tau_2=Uq.}
\tag{2.2}
\]

canonical S-unit phase有

\[
(U,V)=1,
\qquad (U,10)=1.
\]

因为 `v_1v_2=V`，所以

\[
\boxed{(U,v_1v_2 10)=1.}
\tag{2.3}
\]

将 `(2.2)` 模 `U`：

\[
\boxed{
v_1 10^{m_2}\tau_1+v_2\tau_2\equiv0\pmod U.}
\tag{Cofactor-line}
\]

这是一条 denominator-only projective residue line。它没有使用 Gaussian depth，也没有引入新的 local payer。

---

## 3. 两个 cofactor pairs 强迫一个 `U`-deep determinant

固定同一

\[
(U,Z,H,T,V,v_1,v_2,m_2)
\]

phase/factor fiber。假设存在两个合法 cofactor pairs

\[
(\tau_1,\tau_2),
\qquad
(\tau_1',\tau_2').
\]

分别应用 `(Cofactor-line)`：

\[
v_1 10^{m_2}\tau_1+v_2\tau_2\equiv0\pmod U,
\]

\[
v_1 10^{m_2}\tau_1'+v_2\tau_2'\equiv0\pmod U.
\]

第一式乘 `tau_1'`，第二式乘 `tau_1`，相减：

\[
v_2(\tau_2\tau_1'-\tau_2'\tau_1)
\equiv0\pmod U.
\]

由 `(2.3)` 可约去 `v_2`：

\[
\boxed{
U\mid
\Delta_\tau
:=\tau_2\tau_1'-\tau_2'\tau_1.}
\tag{Cofactor-determinant}
\]

若两个 positive rational ratios `tau_2/tau_1` 不同，则

\[
\Delta_\tau\ne0.
\]

由 `(1.7)--(1.8)`，两个 cross products统一满足

\[
\log_{10}(\tau_2\tau_1')
\le
(\kappa_{\rm dig}+C_{\rm one})\delta S+o(S),
\]

同理对另一项成立。因此

\[
\boxed{
0<|\Delta_\tau|
\le
10^{(\kappa_{\rm dig}+C_{\rm one})\delta S+o(S)}.
}
\tag{3.1}
\]

常数恰为

\[
\boxed{
\kappa_{\rm dig}+C_{\rm one}
=\frac52+2a
=3.102059991327962\ldots.}
\tag{3.2}
\]

---

## 4. explicit projective-lock threshold

比较 `(1.4)` 与 `(3.1)`。若

\[
U_*-(1+a)\delta
>
(\kappa_{\rm dig}+C_{\rm one})\delta,
\]

则 sufficiently large `S` 上

\[
U>|\Delta_\tau|.
\]

与 `(Cofactor-determinant)` 对非零 determinant 的整除性矛盾。

定义

\[
\boxed{
\delta_{\rm ray}
:=
\frac{U_*}
{(1+a)+\kappa_{\rm dig}+C_{\rm one}}
=0.156961684731344\ldots.}
\tag{4.1}
\]

因为

\[
(1+a)+\kappa_{\rm dig}+C_{\rm one}
=4.403089986991944\ldots,
\]

得到：

\[
\boxed{
\delta<\delta_{\rm ray}
\Longrightarrow
\text{同一 fixed phase/factor fiber 中全部 }(\tau_1,\tau_2)
\text{ 具有相同 rational ratio}.}
\tag{Projective-cofactor-lock}
\]

这个 neighborhood 比前一 `qZ` product lock 的

\[
\delta_{qZ}=0.075150109396892\ldots
\]

更宽。

---

## 5. primitive ratio 与 common scalar

在一个非空 fixed phase/factor fiber 中，令唯一 rational ratio 的最低项为

\[
\boxed{
\frac{\tau_2}{\tau_1}=\frac sr,
\qquad (r,s)=1,
\qquad r,s>0.}
\tag{5.1}
\]

于是每个 candidate 都存在唯一正整数 `k` 使

\[
\boxed{
\tau_1=kr,
\qquad
\tau_2=ks.}
\tag{5.2}
\]

将 `(5.2)` 代入 exact concat `(2.2)`，定义

\[
\boxed{
D:=v_1r10^{m_2}+v_2s.}
\tag{5.3}
\]

则

\[
\boxed{Uq=kD.}
\tag{5.4}
\]

令

\[
g:=(U,D),
\qquad U=gU_0,
\qquad D=gD_0,
\qquad (U_0,D_0)=1.
\tag{5.5}
\]

由 `(5.4)`：

\[
U_0q=kD_0.
\]

因 `(U_0,D_0)=1`：

\[
\boxed{U_0\mid k.}
\tag{5.6}
\]

写

\[
\boxed{k=U_0\ell,}
\qquad \ell\in\mathbf Z_{>0}.
\tag{5.7}
\]

则 `(5.4)` 进一步给

\[
\boxed{q=D_0\ell.}
\tag{5.8}
\]

---

## 6. denominator data 精确落在一条 common-scale ray

由 `b_i=v_i tau_i` 与 `(5.2),(5.7)`：

\[
\boxed{
b_1=\ell\bar b_1,
\qquad
\bar b_1:=v_1U_0r,}
\tag{6.1}
\]

\[
\boxed{
b_2=\ell\bar b_2,
\qquad
\bar b_2:=v_2U_0s.}
\tag{6.2}
\]

`q` 由 `(5.8)` 给

\[
\boxed{q=\ell\bar q,
\qquad \bar q:=D_0.}
\tag{6.3}
\]

canonical exact third-denominator factorization为

\[
\boxed{b_3=BVq,}
\qquad
B=\frac{10^m}{2\cdot5^T}.
\tag{6.4}
\]

固定 exponent layer 时 `B,V` 固定，因此

\[
\boxed{
b_3=\ell\bar b_3,
\qquad
\bar b_3:=BV D_0.}
\tag{6.5}
\]

最后由 `gamma=tau_1tau_2`：

\[
\boxed{
\gamma
=\ell^2\bar\gamma,
\qquad
\bar\gamma:=U_0^2rs.}
\tag{6.6}
\]

综合：

\[
\boxed{
(b_1,b_2,b_3,q,\gamma)
=
(\ell\bar b_1,
 \ell\bar b_2,
 \ell\bar b_3,
 \ell\bar q,
 \ell^2\bar\gamma).}
\tag{Common-scale-ray}
\]

因此 fixed S-unit phase / `V` factor split 中，所有 denominator candidates 的 projective shape至多一个；剩余移动坐标只有 common scalar `ell`。

---

## 7. `ell` 是 Exact-Lift 的真实 common-denominator scale

这一 ray 不是纯 bookkeeping。固定 numerator triple `(a_1,a_2,a_3)` 与原 decimal widths `(m_1,m_2,m_3)`，定义 padded denominator word

\[
\bar\beta
:=
\bar b_1 10^{m_2+m_3}
+\bar b_2 10^{m_3}
+\bar b_3.
\]

只要某个 `ell` 使三个 actual blocks

\[
b_i=\ell\bar b_i
\]

仍具有 prescribed digit lengths `m_i`，则 actual denominator concat exact 地满足

\[
\boxed{\beta=\ell\bar\beta.}
\tag{7.1}
\]

同时

\[
r_i=\frac{a_i}{b_i}
=\frac1\ell\frac{a_i}{\bar b_i},
\]

所以

\[
\boxed{
\sqrt{r_1^2+r_2^2+r_3^2}
=
\frac1\ell
\sqrt{
(a_1/\bar b_1)^2+
(a_2/\bar b_2)^2+
(a_3/\bar b_3)^2}.}
\tag{7.2}
\]

numerator concat `alpha` 不变，故

\[
\frac\alpha\beta
=
\frac1\ell\frac\alpha{\bar\beta}.
\tag{7.3}
\]

因此在 fixed padded widths 下，Exact-Lift equality 对 common denominator scaling是齐次的：

\[
\boxed{
\frac\alpha\beta
=\sqrt{r_1^2+r_2^2+r_3^2}
\iff
\frac\alpha{\bar\beta}
=
\sqrt{
(a_1/\bar b_1)^2+
(a_2/\bar b_2)^2+
(a_3/\bar b_3)^2}.}
\tag{Scale-homogeneity}
\]

右侧的 `bar b_i` 可以视为保留原 block widths 的 padded primitive shape；它们本身不要求满足原问题的“无前导零”条件。

所以 `ell` 的真正作用只剩 admissibility filter：

1. `ell bar b_i` 必须各自落在 `m_i` 位区间；
2. `(a_i,ell bar b_i)=1` 必须保持 reducedness。

它不再改变 underlying Exact-Lift algebraic equality。

---

## 8. rough-`gamma` entropy 的状态降级

旧 denominator/S-unit theorem 为一个 fixed `(sigma_S,R)` layer 使用

\[
N_{\rm den/SU}
\le10^{(\sigma_S+R)S+o(S)}.
\]

其中 `R` 来自 rough core

\[
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0,
\qquad
R=\frac1S\log_{10}\gamma_0.
\]

`(Common-scale-ray)` 说明 fixed phase/factor split 后

\[
\gamma=\ell^2\bar\gamma.
\]

因此 common scale 的 non-decimal core满足

\[
\operatorname{core}_{10}(\ell)^2\mid\gamma_0,
\]

从而

\[
\operatorname{core}_{10}(\ell)
\le10^{RS/2+o(S)}.
\]

`2,5`-smooth part of `ell` 只有 `O(S)^2=10^{o(S)}` 个 exponent choices，所以一个 fixed phase/factor split 上的 full scale multiplicity至多

\[
\boxed{
N_{\rm scale}
\le10^{(R/2)S+o(S)}.}
\tag{8.1}
\]

另一方面 fixed `(U,Z)` 后 `V` 已确定，`V=v_1v_2` 的 factor split只花 divisor entropy `10^{o(S)}`。Farey side仍花

\[
10^{\sigma_SS+o(S)}.
\]

因此在

\[
\delta<\delta_{\rm ray}
\]

中可以把旧 denominator/S-unit count sharpen 为

\[
\boxed{
N_{\rm den/SU}
\le
10^{(\sigma_S+R/2)S+o(S)}.}
\tag{Ray-refined-den-entropy}
\]

这是 candidate-specific 的严格改进；当 `R` 是正线性 defect carrier 时，指数直接少 `R/2`。

但 quantitative defect仍只有

\[
\delta
\ge
\lambda\sigma_S+(2\lambda-1)R-o(1).
\]

对 objective `sigma_S+R/2` 做最坏优化时，最大 cost ratio仍来自 `sigma_S`：

\[
\frac1\lambda
>
\frac1{2(2\lambda-1)}.
\]

因此 uniform 粗化仍只是

\[
\boxed{
\sigma_S+\frac R2
\le\frac\delta\lambda+o(1).}
\tag{8.2}
\]

也就是说，本文**没有**单独降低旧 `delta/lambda` 的全局最坏 coefficient；它证明最坏情形必须进一步向 Farey/projective slack `sigma_S` 极化，rough `gamma` 已不能同时保持原先的独立 full entropy。

---

## 9. 与 `qZ` product lock 合并后的 residual core

前一 `dd-corrected-denominator-product-lock-2026-09-06.md` 在更小范围

\[
\delta<\delta_{qZ}=0.075150109396892\ldots
\]

证明 fixed `v_2` 后 full candidate fiber只剩 short head `b_1` 的

\[
10^{\kappa_{\rm dig}\delta S+o(S)}
\]

级 freedom。

本文说明：一旦再固定 S-unit phase `(U,Z,V)` 与 divisor split `(v_1,v_2)`，这份 `b_1` movement也不再是 arbitrary short integer shape；由 `(Common-scale-ray)`：

\[
\boxed{b_1=\ell\bar b_1.}
\]

所以 product-lock 之后的 `short decimal head` 可以进一步解释成 **common-scale coordinate**。在两条 theorem 的公共 neighborhood 内，真正的 denominator projective shape residual只剩：

\[
\boxed{
\text{Farey/S-unit phase}
\quad+\quad
V\text{ 的 divisor split};
}
\]

而 rough common scale `ell` 是齐次方向，不是新的 projective shape。

---

## 10. 对下一轮 DD 攻击的意义

本文把 corrected terminal denominator problem 再分成两个逻辑不同的部分：

1. **projective shape problem**：控制 `U,Z` 的 Farey phase；在 fixed phase 后 denominator shape已经唯一到 divisor entropy；
2. **common-scale admissibility problem**：沿唯一 ray 选择 `ell`，只检查 digit-length 与 reducedness。

因此下一轮若要得到 strict gap，不应继续把 `gamma_0` 当成与 Farey phase并列的 arbitrary moving core。真正的 uniform worst case已经被迫向

\[
\boxed{\sigma_S\text{-dominant Farey/projective sector}}
\]

集中。

这也解释为什么单纯继续优化 `gamma` height不会关闭 DD：`ell` 是 exact homogeneous direction。要产生新的不存在性输入，必须作用于 scale-quotiented primitive shape，或者证明某个 original no-leading-zero / reducedness condition 与唯一 common-scale ray全局不相容。

---

## 11. verification scope

配套机械审计：

```bash
uv run python scripts/exact-lift/double-deficit/research-checks/tail/check_dd_corrected_common_scale_ray.py
```

脚本检查：

- `delta_ray` 常数与 `delta_qZ` 的数值顺序；
- toy modular cofactor line 中 two-solution determinant 必被 `U` 整除；
- primitive ratio 后 `k=U_0 ell` 与 `q=D_0 ell` 的 exact arithmetic；
- denominator triple 与 `gamma` 的 common-scale formulas；
- fixed padded widths 下 Exact-Lift 两侧同时按 `1/ell` 缩放。

有限 toy checks只核对 algebra；无界 theorem来自正文的 corrected height windows与 determinant comparison。

---

## 12. 状态摘要

- **已严格完成：** `Cofactor-line` 与 `Cofactor-determinant`。
- **已严格完成：** projective lock threshold
  \[
  \delta_{\rm ray}=0.156961684731344\ldots.
  \]
- **已严格完成：** fixed phase/factor split 的 exact `Common-scale-ray`。
- **已严格完成：** common denominator scale下的 padded-width Exact-Lift homogeneity。
- **计数 sharpen：** denominator/S-unit entropy从 candidate-specific `sigma_S+R` 改为 `sigma_S+R/2`；uniform `delta/lambda` 最坏 coefficient暂未改变。
- **结构降级：** rough `gamma` 不再视为独立 projective denominator shape；其 movable part是 common-scale direction。
- **仍待证：** scale-quotiented Farey/projective primitive shape exclusion；explicit strict slope gap；DD emptiness；更低 post-tail / non-canonical dominant states 的统一 simultaneous height bound。

# DD genuine-Gaussian 的 full-concat square-depth carrier

> **依赖：** [`genuine-denominator-cleared-carrier.md`](genuine-denominator-cleared-carrier.md) 与全局 exact lift `q alpha=H beta`。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。上一文件的 cube-depth original-integer carrier在除去一份 shared-denominator baseline 后可进一步精确识别：其中的大 denominator expression
> \[
> 10^{m_3}Q+b_3
> \]
> 正是完整拼接分母 `beta`。因此 genuine branch 得到一个非常简洁的 square-depth full-concat carrier：
> \[
> C_\sigma^2
> \mid
> Q a_2^2b_1^2\beta\pm Wa_3.
> \]
> 这把 genuine same-prime cancellation 直接放到 `(beta,a3)` digit shell 上。再利用 `q alpha=H beta`，同一 carrier可无损推到 `(alpha,a3)` numerator shell。
>
> 本文不证明该 carrier 高度足够小；它完成的是 genuine branch 从 Gaussian ghost orientation 到真实 concatenated integers 的桥接。

---

## 1. denominator-cleared carrier 的进一步因式分解

上一文件定义

\[
\Phi_\sigma
=Q a_2^2b_1b_3(\kappa+G)
\pm Wa_3b_2,
\]

并证明

\[
\boxed{C_\sigma^3\mid\Phi_\sigma}
\tag{1.1}
\]

对 `sigma=same,opp` 成立；其中符号约定为

\[
\Phi_{\rm same}
=Q a_2^2b_1b_3(\kappa+G)-Wa_3b_2,
\]

\[
\Phi_{\rm opp}
=Q a_2^2b_1b_3(\kappa+G)+Wa_3b_2.
\]

利用 DD tail weight

\[
\kappa=\frac{10^{m_3}QG}{b_3},
\qquad
G=b_1b_2,
\]

有

\[
\begin{aligned}
Q a_2^2b_1b_3(\kappa+G)
&=Q a_2^2b_1b_3
\left(
\frac{10^{m_3}Qb_1b_2}{b_3}+b_1b_2
\right)\\
&=Q a_2^2b_1^2b_2
\left(10^{m_3}Q+b_3\right).
\end{aligned}
\tag{1.2}

所以

\[
\boxed{
\Phi_\sigma
=b_2\left[
Q a_2^2b_1^2(10^{m_3}Q+b_3)
\pm Wa_3
\right].
}
\tag{1.3}

---

## 2. 括号中的 denominator quantity 就是 `beta`

完整 denominator concatenation 为

\[
\beta
=b_1 10^{m_2+m_3}+b_2 10^{m_3}+b_3.
\]

而

\[
Q=b_1 10^{m_2}+b_2.
\]

因此 exact 地

\[
\boxed{
\beta=10^{m_3}Q+b_3.
}
\tag{Beta-tail}

把它代入 `(1.3)`，定义

\[
\boxed{
\Psi_{\rm same}
:=Q a_2^2b_1^2\beta-Wa_3,
}
\tag{2.1}

\[
\boxed{
\Psi_{\rm opp}
:=Q a_2^2b_1^2\beta+Wa_3.
}
\tag{2.2}

则得到 exact factorization

\[
\boxed{
\Phi_\sigma=b_2\Psi_\sigma.
}
\tag{Phi-Psi}

---

## 3. cube-depth 减去 denominator baseline 后正好剩 square depth

固定

\[
p^h\Vert C_\sigma.
\]

one-channel main prime满足

\[
v_p(b_2)=h.
\]

由 `(1.1)` 与 `(Phi-Psi)`：

\[
h+v_p(\Psi_\sigma)
=v_p(\Phi_\sigma)
\ge3h.
\]

因此

\[
\boxed{v_p(\Psi_\sigma)\ge2h.}
\tag{3.1}

聚合：

\[
\boxed{
C_{\rm same}^2
\mid
Q a_2^2b_1^2\beta-Wa_3,
}
\tag{Concat-same}

\[
\boxed{
C_{\rm opp}^2
\mid
Q a_2^2b_1^2\beta+Wa_3.
}
\tag{Concat-opp}

这就是 genuine-Gaussian 的 full-denominator square-depth carrier。

---

## 4. 两个 summands 在 target prime 上都是 units

main genuine prime有

\[
p\nmid Q a_2b_1Wa_3.
\]

还需要检查 `beta`。

因为

\[
p^h\mid b_2,b_3,
\qquad
p\nmid b_1 10,
\]

所以

\[
\beta
=b_1 10^{m_2+m_3}
+b_2 10^{m_3}
+b_3
\equiv
b_1 10^{m_2+m_3}
ot\equiv0\pmod p.
\]

故

\[
\boxed{p\nmid\beta.}
\tag{Beta-unit}

因此 `(Concat-same/opp)` 的 `2h` 深度完全来自两个 p-units 的 cancellation；没有剩余 denominator factor藏在括号中。

这比 cube-depth 形式更规范：

\[
\boxed{
\underbrace{C_\sigma}_{b_2\text{ baseline}}
\times
\underbrace{C_\sigma^2}_{\Psi_\sigma\text{ primitive cancellation}}
}
\]

已经精确分开。

---

## 5. orientation-free full-concat product

两 sign cores 互素且

\[
C_G^{\rm main}=C_{\rm same}C_{\rm opp}
\]

差 `10^{o(S)}` exceptional core。因此

\[
\boxed{
(C_G^{\rm main})^2
\mid
\bigl(Q a_2^2b_1^2\beta\bigr)^2
-(Wa_3)^2.
}
\tag{Concat-product}

它完全使用 original integers 与统一 discriminant root `W`，不再出现 sphere ghosts或 Gaussian orientation choice。

---

## 6. exact lift 把 denominator carrier 推到 numerator shell

全局 exact lift 给

\[
\boxed{q\alpha=H\beta.}
\tag{6.1}

固定 sign core `C_sigma`。pair-max main prime在 `q` 与 `H` 中至少各含完整 `C_sigma` depth，因此定义整数

\[
q_\sigma:=\frac q{C_\sigma},
\qquad
H_\sigma:=\frac H{C_\sigma}.
\tag{6.2}

由 `(6.1)`：

\[
q_\sigma\alpha=H_\sigma\beta.
\tag{6.3}

将 `Psi_sigma` 乘以 `H_sigma`：

\[
\begin{aligned}
H_\sigma\Psi_\sigma
&=Q a_2^2b_1^2H_\sigma\beta
\pm H_\sigma W a_3\\
&=q_\sigma Q a_2^2b_1^2\alpha
\pm H_\sigma W a_3.
\end{aligned}
\]

由于

\[
C_\sigma^2\mid\Psi_\sigma,
\]

得到 numerator-shell version

\[
\boxed{
C_\sigma^2
\mid
q_\sigma Q a_2^2b_1^2\alpha
\pm H_\sigma W a_3.
}
\tag{Numerator-carrier}

注意乘 `H_sigma` 可能在个别 prime 上增加额外深度；本文只使用安全的 lower bound `C_sigma^2`，不把该额外深度计作新的 obstruction。

---

## 7. target prime 上 `alpha` repeat 与 sphere-height excess完全相同

固定

\[
p^h\Vert C_\sigma.
\]

由于 pair-max channel 在 `q` 中已达到深度 `h`：

\[
v_p(q)=h.
\]

而 `(Beta-unit)` 给

\[
v_p(\beta)=0.
\]

从

\[
q\alpha=H\beta
\]

得到 exact valuation identity：

\[
\boxed{
v_p(\alpha)=v_p(H)-h.}
\tag{Alpha-height-excess}

同时

\[
v_p(q_\sigma)=0,
\qquad
v_p(H_\sigma)=v_p(\alpha).
\tag{7.1}

因此 `(Numerator-carrier)` 中两个 summands 自带完全相同的 `alpha` baseline：若

\[
e_p:=v_p(\alpha),
\]

则

\[
\boxed{
\begin{aligned}
v_p(q_\sigma Q a_2^2b_1^2\alpha)&=e_p,\\
v_p(H_\sigma W a_3)&=e_p.
\end{aligned}}
\tag{7.2}

所以把共同 `p^{e_p}` 抽掉后，仍需承担原 `Psi_sigma` 的完整 `2h` unit cancellation。

换言之，exact-lift push 不会凭空支付 genuine square-depth；它只是把同一 p-adic phase从 `(beta,a3)` 坐标图搬到 `(alpha,a3)` 坐标图。

---

## 8. 与 full-rational `G_exc` 的区别

full-rational Good 中，最后困难被压成

\[
(C_N,A_N)=G_{\rm exc}
\]

的一份 **额外 numerator depth**。

这里 genuine-Gaussian carrier 的结构不同：即使

\[
v_p(\alpha)=0,
\]

仍有

\[
p^{2h}\mid\Psi_\sigma
\]

的 primitive unit-unit cancellation。因此 genuine branch 的 square-depth contact不是由 numerator repeat 才出现；它已经存在于 `(beta,a3,W)` phase 本身。

这说明 genuine branch 确实需要与 full-rational `G_exc` 不同的 closure mechanism。

---

## 9. 新 frontier

目前 genuine branch 已从抽象 orientation 走到两个 exact original-integer forms：

\[
\boxed{
C_\sigma^2
\mid
Q a_2^2b_1^2\beta\pm Wa_3,
}
\tag{9.1}

以及

\[
\boxed{
C_\sigma^2
\mid
q_\sigma Q a_2^2b_1^2\alpha
\pm H_\sigma W a_3.
}
\tag{9.2}

前者是 **full denominator concat carrier**，后者是 **full numerator concat carrier**。

两式是同一 p-adic phase 的 exact-lift 两个坐标图，不能重复收费；但它们提供了一个干净接口，可继续与十进制 shell

\[
\alpha=A_{12}10^{n_3}+a_3,
\qquad
\beta=Q10^{m_3}+b_3
\]

联立。

下一步最有价值的是：把 `(9.1)` 中的 `beta=Q10^m+b3` 和 `a3` 做 Euclidean/digit remainder normalization，看看 `C_sigma^2` 是否强迫一个短于 `2 log C_sigma` 的 remainder；若该 remainder又完整退回 discriminant identity，则记录 no-go。

---

## 10. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`Phi_sigma=b2 Psi_sigma`；`Beta-tail`；primitive `Concat-same/opp`；`Beta-unit`；orientation-free `Concat-product`；exact-lift `Numerator-carrier`；`Alpha-height-excess`。
- **`失效/降级`**：把 denominator carrier与 numerator carrier当成两份独立 p-adic收费。
- **`待证`**：`Psi_sigma` 的 decimal remainder normalization；genuine-Gaussian closure；DD 全局空性。

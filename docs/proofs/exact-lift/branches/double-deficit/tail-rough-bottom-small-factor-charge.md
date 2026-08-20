# DD post-tail bottom payer 的 exact small-factor charge

> **依赖：** [`tail-rough-projective-bottom-two-payer.md`](tail-rough-projective-bottom-two-payer.md)、
> `core.md` 的 decimal determinant `E` 与 universal identity
> \[
> F_-Q(\kappa+G)=E\kappa(\kappa+2G).
> \]
>
> **严格状态：** `已严格完成（整个 `X_B` support）`。
>
> two-payer theorem写
> \[
> X_Q=X_PX_B,
> \qquad
> X_P\mid Z_0a,
> \qquad
> X_B\mid C_{12}:=(A_{12},Q).
> \]
> 本文证明 bottom payer `X_B` 其实已经被真实 small factor `F_-` 支付，并且带一整份
> prefix denominator product `G=b_1b_2` 的折扣：
> \[
> \boxed{X_BG<F_-.}
> \tag{Bottom-charge}
> \]
> 因 `m_1+m_2=S`，
> \[
> \boxed{
> \log_{10}X_B
> <\log_{10}F_- -S+O(1).
> }
> \tag{Bottom-height-charge}
> \]
> 因而 post-tail second-Schmidt loss中 `X_B` 不再是一份自由 `S`-height；真正尚未
> 直接收费的只剩 projective/gap payer `X_P`。

---

## 1. `C_12` 自动整除真实 decimal determinant

DD decimal determinant为
\[
\boxed{
E=b_3A_{12}10^d-a_3Q>0.
}
\tag{1.1}
定义
\[
C_{12}:=(A_{12},Q).
\]
两项都显然被 `C_12` 整除，所以
\[
\boxed{C_{12}\mid E.}
\tag{1.2}

two-payer theorem已有
\[
X_B\mid\operatorname{core}_{10}(C_{12}),
\]
故特别地
\[
\boxed{X_B\mid E.}
\tag{1.3}

---

## 2. universal identity把 `E G` 严格放进 `F_-`

`core.md` 的 universal identity是
\[
\boxed{
F_-Q(\kappa+G)=E\kappa(\kappa+2G).
}
\tag{2.1}
所有量均为正整数。整理：
\[
\boxed{
\frac{EG}{F_-}
=
\frac{QG}{\kappa}
\frac{\kappa+G}{\kappa+2G}.
}
\tag{2.2}

DD unified tail window严格有
\[
\boxed{QG<\kappa.}
\tag{2.3}
同时 `G>0` 给
\[
\boxed{\kappa+G<\kappa+2G.}
\tag{2.4}
所以 `(2.2)` 的两个因子都严格小于 1：
\[
\boxed{EG<F_-.}
\tag{2.5}

结合 `(1.3)` 与正整数性：
\[
X_BG\le EG<F_-.
\]
即
\[
\boxed{X_BG<F_-.}
\tag{Bottom-charge}

注意这不是 ordinary size guess，而是 exact universal identity + tail interval 的直接推论。

---

## 3. 一整份 `S` 的 Archimedean 折扣

`b_i` 分别有 `m_i` 位，所以
\[
10^{m_i-1}\le b_i<10^{m_i}.
\]
而
\[
m_1+m_2=S.
\]
因此
\[
\boxed{
10^{S-2}\le G=b_1b_2<10^S.
}
\tag{3.1}

由 `Bottom-charge`：
\[
\log_{10}X_B
<\log_{10}F_- -\log_{10}G.
\]
使用 `(3.1)`：
\[
\boxed{
\log_{10}X_B
<\log_{10}F_- -S+2.
}
\tag{Bottom-height-charge}

所以任何 linearly large bottom source loss都必须先让 `F_-` 比它多承担约一整份 `S`
高度。

---

## 4. 与第二次 Schmidt 的自举

`tail-rough-cq-excess.md` 已有 second fixed-target Schmidt：
\[
\boxed{
\log R_x+\log(g_*/v)
\ge S-\log X_Q-o(S),
}
\tag{4.1}
其中 `R_x` 与 `g_*/v` 都是真实 `F_-` factors。
因此安全地
\[
\boxed{
\log F_-
\ge S-\log X_Q-o(S).
}
\tag{4.2}

使用 two-payer
\[
X_Q=X_PX_B
\]
与 `Bottom-height-charge`：
\[
\begin{aligned}
\log F_-
&\ge S-\log X_P-\log X_B-o(S)\\
&>S-\log X_P-
(\log F_- -S+O(1))-o(S).
\end{aligned}
\]
所以
\[
\boxed{
2\log F_-+\log X_P
\ge2S-o(S).
}
\tag{Bootstrap}

等价地
\[
\boxed{
\log F_-
\ge S-\frac12\log X_P-o(S).
}
\tag{Bootstrap-F}

这说明 bottom loss已经从 Schmidt budget中消去；代价只是 projective loss `log X_P`
的系数被减半。

---

## 5. 当前 branch-reoptimization frontier

post-tail hard rough mass经历
\[
C_Q\to X_Q\to(X_P,X_B)
\]
后，`X_B` 又由 `Bottom-charge` 进入真实 small factor。因此当前唯一未直接收费的量是
\[
\boxed{X_P\mid Z_0a.}
\]
并且它只以半权重出现在 bootstrap lower bound：
\[
\log F_-
\ge S-\frac12\log X_P-o(S).
\]

下一步只需对 projective/gap payer建立统一 height cap，或把 `X_P` 的一部分再次送进
`F_-` / carrier-circle。无需再对 denominator source cancellation或 bottom layer做新的 rough
Schmidt。

---

## 6. 状态摘要

- **`已严格完成`**：`C_12|E`、`EG<F_-`、`Bottom-charge`。
- **`已严格完成`**：`Bottom-height-charge`、second-Schmidt `Bootstrap`。
- **`结构压缩`**：post-tail reoptimization唯一尚未直接收费的 hard loss为 projective/gap `X_P`。
- **`待证`**：projective payer `X_P` height / further charge；non-canonical branch reoptimization；DD global explicit `<=6` / absolute height。

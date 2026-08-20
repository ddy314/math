# DD post-tail rough loss 的 `Z_0`-only frontier

> **依赖：** [`tail-rough-projective-bottom-two-payer.md`](tail-rough-projective-bottom-two-payer.md)、
> [`tail-rough-bottom-small-factor-charge.md`](tail-rough-bottom-small-factor-charge.md)、
> `gcd-normal-exact-small-factor.md`。
>
> **严格状态：** `已严格完成（整个 post-tail `X_Q` support）`。
>
> two-payer theorem给
> \[
> X_Q=X_PX_B,
> \qquad X_P\mid Z_0a,
> \qquad X_B\mid C_{12}.
> \]
> 本文把 projective product继续分成 sphere-gap 与 true projective denominator：
> \[
> X_P=X_aX_Z,
> \qquad X_a\mid a,
> \qquad X_Z\mid Z_0.
> \]
> exact small factor不仅支付 `X_B`，也支付 gap payer，并且两者各带一整份 prefix
> denominator height：
> \[
> \boxed{X_BG<F_-,}
> \qquad
> \boxed{X_aQ<F_-.}
> \]
> 因而 second-Schmidt 可自举为
> \[
> \boxed{
> 3\log F_-+\log X_Z\ge3S-o(S),
> }
> \tag{Triple-bootstrap}
> \]
> 即
> \[
> \boxed{
> \log F_-
> \ge S-\frac13\log X_Z-o(S).
> }
> \tag{Z0-bootstrap}
> \]
> 而 `X_Z` 同时仍是 `X_Q` 的 factor，所以
> \[
> \boxed{X_Z\mid\gcd(C_Q,Z_0).}
> \tag{Z0-only-loss}
> \]
> post-tail branch reoptimization因此只剩一个真正未收费对象：primitive denominator source
> concat `C_Q` 与 stereographic denominator `Z_0` 的 rough gcd。

---

## 1. projective payer 的 gap / denominator exponent split

`tail-rough-projective-bottom-two-payer.md` 对每个
\[
p^e\Vert X_P
\]
给
\[
e\le v_p(Z_0a)=v_p(Z_0)+v_p(a).
\]
定义 sequential split
\[
\boxed{e_a:=\min(e,v_p(a)),}
\tag{1.1}
\[
\boxed{e_Z:=e-e_a.}
\tag{1.2}
则自动有
\[
e_Z\le v_p(Z_0).
\]

全局定义
\[
\boxed{X_a:=\prod p^{e_a(p)},}
\qquad
\boxed{X_Z:=\prod p^{e_Z(p)}.}
\]
于是
\[
\boxed{X_P=X_aX_Z,}
\tag{1.3}
\[
\boxed{X_a\mid\operatorname{core}_{10}(a),}
\qquad
\boxed{X_Z\mid\operatorname{core}_{10}(Z_0).}
\tag{1.4}

结合 two-payer：
\[
\boxed{X_Q=X_aX_ZX_B.}
\tag{1.5}

---

## 2. gap payer同样带一整份 `S` discount

`gcd-normal-exact-small-factor.md` 的 exact factorization为
\[
\boxed{
F_-=a\,g_*\,L\frac{LQ+2\tau}{\tau}.
}
\tag{2.1}

unified tail weight给
\[
\frac\tau L=\frac{QG}{\kappa}.
\]
而严格 tail window
\[
QG<\kappa
\]
意味着
\[
\boxed{L/\tau>1.}
\tag{2.2}

所以从 `(2.1)`：
\[
\frac{F_-}{a}
=g_*L\frac{LQ+2\tau}{\tau}
>g_*L\frac{LQ}{\tau}
=g_*LQ\frac L\tau.
\]
其中 `g_*>=1`, `L>=1`, `L/tau>1`，故
\[
\boxed{aQ<F_-.}
\tag{Gap-charge}

由 `X_a|a`：
\[
\boxed{X_aQ<F_-.}
\tag{2.3}

ordinary denominator concat
\[
Q=b_1 10^{m_2}+b_2
\]
恰有 `S=m_1+m_2` 位，所以
\[
\boxed{10^{S-1}\le Q<10^S.}
\tag{2.4}
因此
\[
\boxed{
\log X_a<\log F_- -S+1.
}
\tag{Gap-height-charge}

---

## 3. bottom payer已有同样 discount

`tail-rough-bottom-small-factor-charge.md` 已严格证明
\[
\boxed{X_BG<F_-,}
\]
且
\[
10^{S-2}\le G<10^S.
\]
因此
\[
\boxed{
\log X_B<\log F_- -S+2.
}
\tag{Bottom-height-charge}

---

## 4. second-Schmidt 的 triple bootstrap

`tail-rough-cq-excess.md` 已有
\[
\boxed{
\log F_-
\ge S-\log X_Q-o(S).
}
\tag{4.1}
使用 `(1.5)`：
\[
\log F_-
\ge S-\log X_a-\log X_Z-\log X_B-o(S).
\]
再用 `Gap-height-charge` 与 `Bottom-height-charge`：
\[
\begin{aligned}
\log F_-
&\ge S-
(\log F_- -S+O(1))
-\log X_Z\\
&\qquad-
(\log F_- -S+O(1))-o(S).
\end{aligned}
\]
所以
\[
\boxed{
3\log F_-+\log X_Z
\ge3S-o(S).
}
\tag{Triple-bootstrap}

等价地
\[
\boxed{
\log F_-
\ge S-\frac13\log X_Z-o(S).
}
\tag{Z0-bootstrap}

由于 `X_Z|X_Q|C_Q` 且 `X_Z|Z_0`：
\[
\boxed{X_Z\mid\gcd(C_Q,Z_0).}
\tag{Z0-only-loss}

粗略使用 `C_Q<Q<10^S` 已给
\[
\log X_Z\le S+O(1),
\]
所以无条件还有
\[
\boxed{
\log F_-\ge\frac23S-o(S).
}
\tag{Two-thirds-F}
这已排除 post-tail small factor退化到 subexponential height，但尚不足以单独完成 full side-branch LP。

---

## 5. 当前唯一 hard object

现在 rough-source chain为
\[
C_Q
\to X_Q
\to(X_P,X_B)
\to(X_a,X_Z,X_B)
\to\boxed{X_Z=(C_Q,Z_0)\text{ 的一部分}}.
\]

其中：

- `X_a` 已由 exact gap factor带 `Q~10^S` 收费；
- `X_B` 已由 decimal determinant / universal identity带 `G~10^S` 收费；
- common numerator与 Gaussian angular depth都已在 projective theorem中吸收到 `Z_0a`；
- 唯一还没获得额外 `S` discount的是 `X_Z|gcd(C_Q,Z_0)`。

因此下一步不应再做 generic source gcd、Gaussian norm或 bottom determinant allocation。真正目标只有：

\[
\boxed{
\text{控制 primitive denominator concat }C_Q
\text{ 与 stereographic denominator }Z_0
\text{ 的 common rough height。}
}

可行接口包括 coefficient circle的 homogeneous equation、projective denominator exact valuation
formula，以及 `C_Q=B_1 10^{m_2}+B_2` 的 source root。

---

## 6. 状态摘要

- **`已严格完成`**：projective `X_a/X_Z` split。
- **`已严格完成`**：`Gap-charge` 与 `Gap-height-charge`。
- **`已严格完成`**：`Triple-bootstrap`、`Two-thirds-F`。
- **`结构压缩`**：post-tail branch reoptimization只剩 `X_Z|gcd(C_Q,Z_0)`。
- **`待证`**：`C_Q-Z_0` common rough height；non-canonical dominant branch reoptimization；DD global explicit `<=6` / absolute height。

# DD `Z_0` residual 的 angular-only collapse

> **依赖：** [`tail-rough-z0-two-sheet-collapse.md`](tail-rough-z0-two-sheet-collapse.md)、
> [`tail-rough-bottom-small-factor-charge`](tail-allocation-ledger.md#source-tail-rough-bottom-small-factor-charge)、
> [`tail-rough-z0-only-frontier`](tail-allocation-ledger.md#source-tail-rough-z0-only-frontier)、
> [`tail-rough-angular-source-transfer`](tail-allocation-ledger.md#source-tail-rough-angular-source-transfer)。
>
> **严格状态：** `已严格完成（整个 post-tail X_Q odd rough support）`。
>
> 前一条 two-sheet theorem 把
> \[
> X_Z=X_{Z,3}X_{Z,N}
> \]
> 分成 third-covered 与 norm-overflow 两个互斥 prime-support sheet。本文继续证明：
>
> 1. third-covered residual `X_{Z,3}` 与整个 gap payer `X_a` 一起获得一整份 prefix
>    denominator `Q` 的 exact small-factor charge；
> 2. norm-overflow residual `X_{Z,N}` 可按 exponent layer 分成
>    \[
>    X_{Z,N}=X_{Z,C}X_{Z,A},
>    \]
>    其中 `X_{Z,C}` 已被原 bottom payer逐 prime覆盖，而真正独立的 `X_{Z,A}` 同时进入
>    primitive Gaussian angular norm `N_ang` 与 pure-numerator orientation reader `N_num`；
> 3. 因而 post-tail `Z_0` hard loss 最终只剩一个 **split-Gaussian angular-only layer**。
>
> 更精确地：
> \[
> \boxed{X_aX_{Z,3}Q<F_-,}
> \tag{Third-gap-charge}
> \]
> \[
> \boxed{X_{Z,C}\mid X_B,}
> \tag{Common-under-bottom}
> \]
> \[
> \boxed{
> X_{Z,A}\mid\operatorname{core}_{10}(N_{\rm ang}),
> \qquad
> X_{Z,A}\mid\operatorname{core}_{10}(N_{\rm num}),
> }
> \tag{Angular-double-reader}
> \]
> 且每个 odd prime divisor of `X_{Z,A}` 都满足 `p≡1 (mod 4)`。
>
> 这一步把此前的匿名 `gcd(C_Q,Z_0)`，以及前一条 two-sheet theorem 的两个 quotient
> readers，再压到一个有明确 Gaussian orientation 的单层 residual。

---

## 1. third-exclusive reader 本身带一整份 `Q` discount

记
\[
R:=\operatorname{core}_{10}(R_3^{\rm den}).
\]
由定义
\[
R_3^{\rm den}
=
\frac{b_3}{(b_3,\operatorname{lcm}(b_1,b_2))}.
\]
另一方面 unified tail normalization 写
\[
L=\frac{10^\ell}{\delta_3},
\qquad
\tau=\frac{b_3}{\delta_3},
\qquad
\delta_3=(10^\ell,b_3).
\]

固定 odd prime `p∤10`。因为 `delta_3` 只含 `2,5` primes，
\[
v_p(\tau)=v_p(b_3).
\]
而
\[
v_p(R_3^{\rm den})\le v_p(b_3).
\]
所以逐 prime 有
\[
\boxed{R\mid\tau.}
\tag{1.1}
\]
特别地
\[
R\le\tau.
\tag{1.2}
\]

exact small-factor normalization 给
\[
\boxed{
F_-
=a\,g_*\,L\frac{LQ+2\tau}{\tau}.
}
\tag{1.3}
\]
unified tail weight 又有
\[
\frac\tau L=\frac{QG}{\kappa}.
\]
严格 tail window
\[
QG<\kappa
\]
因此
\[
\boxed{\tau<L.}
\tag{1.4}
\]

由 `(1.3)`：
\[
\begin{aligned}
\frac{F_-}{aRQ}
&=g_*\frac{L(LQ+2\tau)}{\tau RQ}\\
&>g_*\frac{L^2}{\tau R}.
\end{aligned}
\]
利用 `g_*>=1`、`R<=tau<L`：
\[
\frac{L^2}{\tau R}
\ge
\frac{L^2}{\tau^2}
>1.
\]
于是得到新的 exact charge：
\[
\boxed{aRQ<F_-.}
\tag{Third-reader-charge}
\]

这条式子对整个 odd rough `R` 成立，不依赖某个单独 source prime。

---

## 2. Sheet T 与 gap payer 一起消失

`tail-rough-z0-two-sheet-collapse.md` 已定义 third-covered support
\[
X_{Z,3}
\]
并证明
\[
X_{Z,3}\mid R.
\]
`Z_0`-only frontier 又有
\[
X_a\mid a.
\]
因此作为正整数
\[
X_aX_{Z,3}\le aR.
\]
结合 `Third-reader-charge`：
\[
\boxed{
X_aX_{Z,3}Q<F_-.
}
\tag{Third-gap-charge}
\]

这比只对 `X_a` 使用
\[
X_aQ<F_-
\]
更强：所有 third-covered `Z_0` residual 都免费并入同一个 prefix-`Q` charge。

在 primewise bookkeeping 上，前一 theorem 还给更精细的 Sheet T relation
\[
X_{a,T}X_{Z,3}\mid R_3^{\rm den},
\]
所以这里没有把同一 third-reader valuation 误当成两份独立容量。

---

## 3. Sheet N 的 common / angular exponent split

固定 Sheet N prime，即
\[
x>r+t.
\]
沿用前一 theorem 的局部记号：
\[
t=v_p(C),
\qquad
r=v_p(R_3^{\rm den}),
\]
\[
g=v_p(g_n),
\qquad
\omega=v_p(N_{\rm ang}),
\qquad
\alpha=v_p(a).
\]
已有
\[
g\le t,
\tag{3.1}
\]
并且 Sheet N 上 bottom payer 饱和：
\[
\boxed{e_B=t.}
\tag{3.2}
\]
前一 theorem 的 sharpened residual bound 为
\[
\boxed{
 e_Z\le(2g+\omega-t-\alpha)_+.
}
\tag{3.3}
\]
由 `t>=g`：
\[
2g+\omega-t-\alpha
\le
 g+\omega-\alpha.
\]
所以
\[
\boxed{
 e_Z\le(g+\omega-\alpha)_+.
}
\tag{3.4}

定义 gap 后仍可能留下的 common numerator capacity
\[
\boxed{c_p:=(g-\alpha)_+.}
\tag{3.5}
\]
再定义两段 residual：
\[
\boxed{e_{Z,C}:=\min(e_Z,c_p),}
\tag{3.6}
\]
\[
\boxed{e_{Z,A}:=e_Z-e_{Z,C}.}
\tag{3.7}
\]
显然
\[
\boxed{e_Z=e_{Z,C}+e_{Z,A}.}
\tag{3.8}

---

## 4. common residual 已在 bottom payer 内

由 `(3.6)`：
\[
e_{Z,C}\le c_p\le g.
\]
再用 `(3.1),(3.2)`：
\[
\boxed{e_{Z,C}\le g\le t=e_B.}
\tag{4.1}
\]

对所有 Sheet N primes 定义
\[
X_{Z,C}:=\prod p^{e_{Z,C}(p)}.
\]
由于 primewise `e_{Z,C}<=e_B`，直接得到
\[
\boxed{X_{Z,C}\mid X_{B,N}\mid X_B.}
\tag{Common-under-bottom}
\]

因此 `X_{Z,C}` 不是新的高度池；它的每一层 valuation 都已经存在于原 bottom payer 中。
原 bottom exact charge
\[
X_BG<F_-
\]
已经支付这部分深度。

---

## 5. remainder 只有 primitive Gaussian angular depth

### Lemma 5.1

对每个 Sheet N prime，
\[
\boxed{e_{Z,A}\le\omega.}
\tag{5.1}
\]

### Proof

若 `alpha>=g`，则 `c_p=0`，所以
\[
e_{Z,A}=e_Z.
\]
由 `(3.4)`：
\[
e_{Z,A}
\le(g+\omega-\alpha)_+
\le\omega.
\]

若 `alpha<g`，则
\[
c_p=g-\alpha.
\]
若 `e_Z<=c_p`，则 `e_{Z,A}=0`。否则由 `(3.4)`：
\[
\begin{aligned}
e_{Z,A}
&=e_Z-(g-\alpha)\\
&\le(g+\omega-\alpha)-(g-\alpha)\\
&=\omega.
\end{aligned}
\]
两种情况都得到 `(5.1)`。∎

定义
\[
X_{Z,A}:=\prod p^{e_{Z,A}(p)}.
\]
由 `e_{Z,A}<=omega=v_p(N_ang)`：
\[
\boxed{
X_{Z,A}\mid\operatorname{core}_{10}(N_{\rm ang}).
}
\tag{5.2}
\]

而 `N_ang` 是 primitive sum of two squares，所以每个 odd prime divisor 满足
\[
\boxed{
 p\mid X_{Z,A}
 \Longrightarrow
 p\equiv1\pmod4.
}
\tag{5.3}

于是 norm-overflow `Z_0` residual 中所有 inert (`3 mod 4`) depth 已经全部落入
`X_{Z,C}|X_B`；独立 remainder 只支撑在 split Gaussian primes。

---

## 6. angular remainder 同时进入 pure-numerator orientation reader

`tail-rough-angular-source-transfer` 已证明，在 `X_Q` support 上若
\[
c:=v_p(C_Q),
\]
则
\[
\boxed{
v_p(N_{\rm num})\ge\min(c,\omega).
}
\tag{6.1}
\]
同时
\[
p^x\Vert X_Q,
\qquad X_Q\mid C_Q
\]
给
\[
\boxed{x\le c.}
\tag{6.2}

由定义
\[
e_{Z,A}\le e_Z\le e_P\le x,
\]
再结合 `(5.1)`：
\[
e_{Z,A}\le\min(x,\omega)\le\min(c,\omega).
\]
所以由 `(6.1)`：
\[
\boxed{
e_{Z,A}\le v_p(N_{\rm num}).
}
\tag{6.3}

逐 prime 相乘：
\[
\boxed{
X_{Z,A}\mid\operatorname{core}_{10}(N_{\rm num}).
}
\tag{6.4}

结合 `(5.2)`：
\[
\boxed{
X_{Z,A}
\mid
\operatorname{core}_{10}\gcd(N_{\rm ang},N_{\rm num}).
}
\tag{Angular-double-reader}
\]
这里的重点是同一 exponent layer 同时具有 primitive angular 与 pure-numerator orientation
两种语义，不能再把它当作 ordinary projective gcd。

---

## 7. global factorization

由前一 theorem
\[
X_Z=X_{Z,3}X_{Z,N},
\]
而 `(3.8)` 给
\[
\boxed{X_{Z,N}=X_{Z,C}X_{Z,A}.}
\tag{7.1}
\]
注意 `X_{Z,C}` 与 `X_{Z,A}` 是同一 prime 上的 exponent layers，故不要求互素。

因此 `Z_0`-only factorization
\[
X_Q=X_aX_ZX_B
\]
变成
\[
\boxed{
X_Q
=(X_aX_{Z,3})\,X_B\,X_{Z,C}\,X_{Z,A}.
}
\tag{Angular-only-factorization}
\]
其中：

- `X_aX_{Z,3}` 由 `Third-gap-charge` 以一整份 `Q` discount 支付；
- `X_B` 由 `X_BG<F_-` 以一整份 `G` discount 支付；
- `X_{Z,C}|X_B`，所以这层没有独立 reader capacity；
- 唯一新的 independent reader 是 `X_{Z,A}`，并且满足 `Angular-double-reader`。

这就是所需的 angular-only collapse。

---

## 8. Schmidt bookkeeping consequence

second fixed-target Schmidt 给
\[
\log F_-
\ge
S-\log X_Q-o(S).
\tag{8.1}
\]

由
\[
10^{S-1}\le Q<10^S,
\qquad
10^{S-2}\le G<10^S,
\]
`Third-gap-charge` 与 bottom charge 分别给
\[
\log(X_aX_{Z,3})
\le\log F_- -S+O(1),
\tag{8.2}
\]
\[
\log X_B
\le\log F_- -S+O(1).
\tag{8.3}
\]
又 `X_{Z,C}|X_B`：
\[
\log X_{Z,C}\le\log X_B
\le\log F_- -S+O(1).
\tag{8.4}
\]
把 `Angular-only-factorization` 代入 `(8.1)`：
\[
\boxed{
4\log F_-+\log X_{Z,A}
\ge4S-o(S).
}
\tag{Angular-only-bootstrap}
\]
等价地
\[
\boxed{
\log F_-
\ge
S-\frac14\log X_{Z,A}-o(S).
}
\tag{8.5}

**解释边界。** 这条 bootstrap 的主要价值是 bookkeeping：把 second-Schmidt 的唯一独立
rough loss 压到 `X_{Z,A}`。作为单独的 Archimedean lower bound，它并不比已有
`F_->Q` / `F_->G` 自动给出的 `log F_- >= S-O(1)` 更强，因此不能把 `(8.5)` 误报成新的
数值 slope improvement。

真正的新信息是：任何仍想在线性高度上损害 Schmidt 的 residual，必须同时满足
\[
X_{Z,A}\mid N_{\rm ang},
\qquad
X_{Z,A}\mid N_{\rm num},
\qquad
p\mid X_{Z,A}\Rightarrow p\equiv1\pmod4.
\]

---

## 9. 下一 frontier

post-tail hard chain 现在变为
\[
C_Q
\to X_Q
\to X_Z
\to(X_{Z,3},X_{Z,N})
\to(X_{Z,C},X_{Z,A})
\to\boxed{X_{Z,A}}.
\]

`X_{Z,A}` 具有三重限制：

1. **split support**：odd primes 全 `1 mod 4`；
2. **primitive angular reader**：`X_{Z,A}|N_ang`；
3. **pure-numerator orientation reader**：`X_{Z,A}|N_num`。

因此下一步应直接研究
\[
\gcd(N_{\rm ang},N_{\rm num})
\]
在 source concat / coefficient circle 下的 rough height，特别是利用已有
\[
\operatorname{core}_{10}\gcd(A^\circ,N_{\rm num})
\mid10^{2|s_2|}+1
\]
与 Gaussian orientation。继续对 `gcd(C_Q,Z_0)`、整个 `N_0` 或整个 `X_Q` 做 generic gcd
height 会丢掉当前已经建立的 payer overlap 信息。

---

## 10. verification scope

对应有限 algebra audit：

```bash
uv run python scripts/exact-lift/double-deficit/research-checks/tail-allocation/check_dd_tail_rough_z0_angular_only.py
```

脚本枚举 bounded valuation tuples，核对 Sheet N 上
\[
e_{Z,C}\le e_B,
\qquad
e_{Z,A}\le\omega,
\]
以及 `e_{Z,A}<=min(x,omega)` 的 orientation-transfer接口。

`Third-reader-charge` 依赖的是 §§1--2 的 exact integer inequalities，不由有限枚举认证。
有限脚本只作 algebra consistency audit，不能替代正文的无界证明。

---

## 11. 状态摘要

- **`已严格完成`**：`R|tau`、`Third-reader-charge`、`Third-gap-charge`。
- **`已严格完成`**：Sheet N common/angular split、`Common-under-bottom`。
- **`已严格完成`**：`Angular-double-reader` 与 split-prime support。
- **`已严格完成`**：`Angular-only-factorization`。
- **`结构压缩`**：post-tail second-Schmidt 的唯一 independent rough reader 已压到
  split-Gaussian `X_{Z,A}`。
- **`待证`**：`gcd(N_ang,N_num)` 的 simultaneous rough height / coefficient-circle charge；
  non-canonical DD dominant-state reoptimization；DD global explicit `<=6` / absolute height。

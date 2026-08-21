# A2 descendant-only projective carrier 的 unequal/equal-depth reader

> **依赖：** `spontaneous-crt-pure-prefix-elimination.md`、`spontaneous-crt-pure-projective-carrier.md`、`spontaneous-crt-descendant-projective-integer.md`、`spontaneous-crt-pure-coefficient-singular.md`。
>
> **严格状态：**前一版本错误地把 projective quadratic `L(r)` 当成真实整数恒等式 `L=0`，从而错误宣称 `v_p(P_63)=v_p(q)`。本版本撤销该结论并保留正确的 exact identity。实际上 `K^2L=R_0-R` 正是 normalized additive error；若 `q=Ar+B` 是 universal descendant polynomial 模 `L` 的一次余式，则
> \[
> X_{63}^{proj}=55q^2-A L'(r)q+A^2L.
> \]
> 在 coefficient-generic、simple-root prime 上，若 `a=v_p(q), b=v_p(L)`，则 `a!=b` 时严格有 `v_p(X)=min(a,b)`；只有 `a=b` 时才可能产生额外 resultant 深度，而且 next digit 由唯一 normalized cancellation `A L_b-L' q_a=0 mod p` 控制。故 projective resultant 的高阶自由度被严格压到 equal-depth branch；本文不宣称 A2 关闭。

---

## 1. projective additive/descendant system

沿用

\[
r=\frac1K,
\qquad
u=\frac{a_3}{TK},
\qquad
v=\frac{Q^2N_0}{B^2K^2},
\]

并把第二个变量记为

\[
u:=\frac{a_3}{TK}.
\]

定义 projective quadratic

\[
\boxed{
L(r):=55r^2+18(u-1)r+1-4u-v.
}
\tag{1.1}
\]

这里必须强调：`L` 不是实 endpoint 上恒等为零的 sphere relation。令

\[
\zeta:=a_3/T,
\qquad
R:=Q^2N_0/B^2.
\]

代回

\[
r=1/K,
\quad u=\zeta/K,
\quad v=R/K^2,
\]

得到

\[
\boxed{
K^2L
=
K^2-(18+4\zeta)K+18\zeta+55-R.
}
\tag{1.2}
\]

而 `spontaneous-crt-universal-descendant-cubic.md` §2 中 additive common condition正是

\[
R_0:=K^2-(18+4\zeta)K+18\zeta+55.
\]

所以

\[
\boxed{K^2L=R_0-R.}
\tag{1.3}
\]

因此 `L` 是 projectivized additive error。对 relevant common prime 它可以有正 `p`-进深度，但不能在整数层面偷偷设成零。

---

## 2. universal descendant remainder

projectivize universal cubic：

\[
E_{\rm proj}(r,u)
:=r^8\mathcal E_{63}(1/r,u/r).
\tag{2.1}
\]

在 `Q(u,v)[r]` 中对 `L` 做 Euclidean division：

\[
\boxed{
E_{\rm proj}=Q_LL+Ar+B,
}
\tag{2.2}
\]

其中

\[
A=A_{63}(u,v),
\qquad
B=B_{63}(u,v).
\]

定义一次 descendant compatibility residual

\[
\boxed{q:=Ar+B.}
\tag{2.3}
\]

所以 `q` 与 `L` 是当前 projective elimination 中真正需要同时追踪的两条 local errors。

---

## 3. resultant 的 exact 三项恒等式

quadratic `L` 与 linear remainder `Ar+B` 的 resultant为

\[
\boxed{
X_{\rm lin}
=55B^2-18(u-1)AB+(1-4u-v)A^2.
}
\tag{3.1}
\]

full degree-8 resultant满足

\[
\boxed{
\operatorname{Res}_r(L,E_{\rm proj})
=5^7 11^7X_{\rm lin}.
}
\tag{3.2}
\]

固定 content `5^7 11^7` 已在 generic external sector分离。

又

\[
L'(r)=110r+18(u-1).
\tag{3.3}
\]

直接展开 `q=Ar+B` 得到 exact identity

\[
\boxed{
X_{\rm lin}
=55q^2-A L'(r)q+A^2L(r).
}
\tag{3.4}
\]

这是本文件真正的主恒等式。前一版本从这里错误地继续代入 `L=0`；该步现已撤销。

---

## 4. unequal-depth branch 完全横截

固定 genuine odd prime `p`，并处于 generic sector：

\[
\boxed{p\nmid A L'(r),}
\tag{4.1}
\]

同时排除固定 resultant content prime `5,11`。

设

\[
a:=v_p(q)\ge1,
\qquad
b:=v_p(L)\ge1.
\tag{4.2}
\]

### 4.1 `a<b`

(3.4) 三项的赋值分别至少为

\[
2a,\qquad a,\qquad b.
\]

由于

\[
a<2a,\qquad a<b,
\]

中间项是唯一最浅项，且其 coefficient `-AL'` 为 unit。因此

\[
\boxed{a<b\Longrightarrow v_p(X_{\rm lin})=a.}
\tag{4.3}
\]

### 4.2 `b<a`

三项赋值为

\[
2a,\qquad a,\qquad b,
\]

此时 `A^2L` 是唯一最浅项。因此

\[
\boxed{b<a\Longrightarrow v_p(X_{\rm lin})=b.}
\tag{4.4}
\]

合并：

\[
\boxed{
a\ne b
\Longrightarrow
v_p(X_{\rm lin})=\min\{a,b\}.}
\tag{4.5}
\]

所以 resultant 在 unequal-depth branch 上既不会吞深度，也不会制造额外深度。

---

## 5. 只有 equal-depth 才能继续 cancellation

现在设

\[
a=b=e.
\]

写

\[
q=p^eq_e,
\qquad
L=p^eL_e,
\qquad
q_eL_e\not\equiv0\pmod p.
\]

将 (3.4) 除以 `p^e`。第一项 `55q^2/p^e` 仍被 `p^e` 整除，所以模 `p` 消失；剩下

\[
\frac{X_{\rm lin}}{p^e}
\equiv
-A L'q_e+A^2L_e
\pmod p.
\]

即

\[
\boxed{
\frac{X_{\rm lin}}{p^e}
\equiv
A\bigl(AL_e-L'q_e\bigr)
\pmod p.
}
\tag{5.1}
\]

因为 `A` 是 unit，得到精确 criterion：

\[
\boxed{
v_p(X_{\rm lin})>e
\Longleftrightarrow
AL_e-L'q_e\equiv0\pmod p.}
\tag{5.2}
\]

因此 projective resultant 的 higher multiplicity并不是第三个自由 Hensel direction；它恰好就是 additive 与 descendant 两条 normalized errors 在 equal-depth 层的一次线性 tie。

这与既有 descendant second/third/quartic transport hierarchy 的结构完全一致：真正需要继续追踪的是 equal-depth normalized cancellation，而不是机械提高 resultant modulus。

---

## 6. ordinary integer carrier `P_63`

`spontaneous-crt-descendant-projective-integer.md` 定义

\[
\mathscr P_{63}
=R_c^8Y^8
\mathscr X_{63}^{proj}
\left(\frac{a_3}{R_c},\frac XY\right),
\]

其中 `R_c=TK`，为避免与上文 prefix ratio `R` 混淆这里改写为 `R_c`。

在 genuine descendant-only external prime 上，denominator clearing 与 fixed content均为 units。因此

\[
v_p(\mathscr P_{63})=v_p(X_{\rm lin}).
\tag{6.1}
\]

结合 §4–§5：

\[
\boxed{
a\ne b
\Longrightarrow
v_p(\mathscr P_{63})=\min\{a,b\},}
\tag{6.2}
\]

而 `a=b=e` 时

\[
\boxed{
v_p(\mathscr P_{63})>e}
\]

当且仅当 (5.2) 的 normalized tie 成立。

这才是旧 integer-carrier 文件所需的正确 depth comparison。

---

## 7. parity consequence

已有

\[
\mathscr P_{63}>0,
\qquad
\mathscr P_{63}^{\circ}\equiv1\pmod8.
\]

故 `P_63` 中全部 `3 mod4` prime exponents 的总 parity为偶。

本文件现在给出严格可用的接口：

- unequal-depth external common prime的 carrier exponent就是较浅 common error depth；
- 若该较浅 depth 为奇，则 `P_63^circ≡1 mod4` 强迫至少另一枚 `3 mod4` prime以奇次出现；
- 若试图通过 extra resultant multiplicity逃避，只能进入 equal-depth normalized tie (5.2)，之后必须交给已有 serial/transport hierarchy继续审计。

因此 generic external pool 的自由度被明确二分为

\[
\boxed{
\text{unequal-depth parity surcharge}
\quad\text{或}\quad
\text{equal-depth transport cancellation}.}
\tag{7.1}
\]

A2 仍为 `待证`。

---

## 8. verification

```bash
uv run python scripts/exact-lift/a2-only/research-checks/crt-descent/check_a2_descendant_projective_exact_depth_reader.py
```

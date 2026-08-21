# A2 descendant-only projective carrier 的 exact depth reader

> **依赖：** `spontaneous-crt-pure-prefix-elimination.md`、`spontaneous-crt-pure-projective-carrier.md`、`spontaneous-crt-descendant-projective-integer.md`、`spontaneous-crt-pure-coefficient-singular.md`。
>
> **严格状态：**generic descendant-only external pool 已有 projective carrier `X_63^proj(u,v)` 与 ordinary integer clearing `P_63`，但旧文只记录 `p|P_63`，没有比较 common-prime 深度与 carrier 深度。本文证明 universal resultant 在真实 branch quadratic 上存在一个 exact two-factor identity：若 `q=A_63 r+B_63` 是 descendant polynomial 对 branch quadratic 的线性余式，则 `X_63^proj=q(55q-A_63L'(r))`。因此对 coefficient-generic、sphere-simple 的 genuine prime，第二因子始终是 unit，得到完整 prime-power 等式 `v_p(X_63^proj)=v_p(q)`；清 denominator 后同样有 `v_p(P_63)=v_p(q)`。这关闭了“resultant 可能额外增深”的自由度，但 `q` 与原 `G_Delta` common depth之间仍可能经过 descendant transport cancellation，因此本文尚不宣称 generic external pool为空或 A2 关闭。

---

## 1. projective branch system

沿用 dimensionless variables

\[
r=\frac1K,
\qquad
u=\frac{a_3}{TK},
\qquad
v=\frac{Q^2N_0}{B^2K^2}.
\]

为避免与 valuation 记号混淆，下文仍把第二个变量写成 `u`：

\[
u:=\frac{a_3}{TK}.
\]

真实 sphere/rational-root branch 满足 exact quadratic

\[
\boxed{
L(r):=55r^2+18(u-1)r+1-4u-v=0.
}
\tag{1.1}
\]

universal descendant polynomial projectivize为

\[
E_{\rm proj}(r,u)
:=r^8\mathcal E_{63}(1/r,u/r).
\tag{1.2}
\]

在 `Q(u,v)[r]` 中对 `L` 做 Euclidean division：

\[
\boxed{
E_{\rm proj}=Q_L L+Ar+B,
}
\tag{1.3}
\]

其中

\[
A=A_{63}(u,v),
\qquad
B=B_{63}(u,v).
\]

定义真正的一次 compatibility residual

\[
\boxed{q:=Ar+B.}
\tag{1.4}
\]

因为真实 branch满足 `L(r)=0` 精确成立，实际点上

\[
\boxed{E_{\rm proj}(r,u)=q.}
\tag{1.5}
\]

所以后续无需再把 degree-8 polynomial 当作独立对象；其全部 actual p-adic compatibility已经被 `q` 读取。

---

## 2. resultant 的 exact 三项恒等式

quadratic 与 linear remainder 的 resultant为

\[
\boxed{
X_{m lin}
=55B^2-18(u-1)AB+(1-4u-v)A^2.
}
\tag{2.1}
\]

直接计算 full resultant 得

\[
\boxed{
\operatorname{Res}_r(L,E_{\rm proj})
=5^7 11^7 X_{\rm lin}.
}
\tag{2.2}
\]

固定 content `5^7 11^7` 正是旧 projective carrier 中已经剥去的 coefficient content；genuine generic external prime已与 `5,11` 分离，因此不影响任何 relevant valuation。

现在求

\[
L'(r)=110r+18(u-1).
\tag{2.3}
\]

把 `q=Ar+B` 代入右边展开，得到 exact polynomial identity

\[
\boxed{
X_{m lin}
=55q^2-A L'(r)q+A^2L(r).
}
\tag{2.4}
\]

它不是模 `p` 的 first-layer approximation，而是 `Q(u,v,r)` 中的恒等式。

也可定义 conjugate companion

\[
\boxed{
C_q:=A L'(r)-55q
=55(Ar-B)+18A(u-1),
}
\tag{2.5}
\]

则

\[
\boxed{
X_{m lin}=-qC_q+A^2L(r).
}
\tag{2.6}
\]

---

## 3. 真实 branch 上降成 two-factor identity

由 (1.1)，真实 endpoint 精确满足

\[
L(r)=0.
\]

因此 (2.4) 立即化为

\[
\boxed{
X_{m lin}
=q\bigl(55q-A L'(r)\bigr)
=-qC_q.
}
\tag{3.1}
\]

这说明 projective resultant 在 actual branch上并不是一个可能产生神秘额外 multiplicity 的 degree-11 黑盒；它只是：

1. 真正 descendant compatibility residual `q`；
2. 一个明确的 conjugate derivative factor。

---

## 4. generic coefficient + simple sphere 给 complete depth equality

固定 genuine odd prime `p` 属于 coefficient-generic、sphere-simple branch，即

\[
\boxed{p\nmid A,}
\tag{4.1}
\]

以及

\[
\boxed{p\nmid L'(r).}
\tag{4.2}
\]

前者的失败正是旧 `A=B=0` coefficient-singular channel；后者的失败正是 branch quadratic 的 double-root/discriminant channel。两者都已在历史 proof tree中单列，不能混入 generic pool。

若

\[
p\mid q,
\]
则由 (3.1) 的第二因子

\[
55q-A L'(r)
\equiv-A L'(r)
ot\equiv0\pmod p.
\tag{4.3}
\]

因此该因子是完整的 `p`-adic unit，不会在更高 lift 中突然获得一层 `p`。于是对任意 `e>=1`：

\[
\boxed{
v_p(q)=e
\Longrightarrow
v_p(X_{m lin})=e.
}
\tag{4.4}
\]

反过来在 `p|q` 的 common branch上当然同样成立，因此可直接写成

\[
\boxed{
v_p(X_{m lin})=v_p(q).}
\tag{4.5}
\]

这是一条**全深度** reader，而不是 truncated equality。

---

## 5. ordinary integer carrier `P_63` 继承同一深度

`spontaneous-crt-descendant-projective-integer.md` 定义

\[
\mathscr P_{63}
=R^8Y^8
\mathscr X_{63}^{\rm proj}
\left(\frac{a_3}{R},\frac XY\right),
\]

其中 genuine descendant-only external prime满足

\[
p\nmid RY,
\qquad p\notin\{5,11\}.
\]

所以 denominator clearing 与 fixed resultant content均为 `p`-units。结合 (2.2),(4.5)：

\[
\boxed{
v_p(\mathscr P_{63})=v_p(q)}
\tag{5.1}
\]

对全部 generic coefficient/simple-sphere common primes成立。

这严格补上旧 integer-carrier 文件留下的缺口：`P_63` 不仅知道 support，而且不会自行增加或吞掉任何 descendant compatibility depth。

---

## 6. 这一步尚未自动等于 `G_Delta` depth

必须保留一个重要边界。`q=E_proj(r,u)` 是把：

- original additive relation；
- descended relation；
- exact rational-root equation

消元后的 universal compatibility residual。

若

\[
h_p:=v_p(G_\Delta)
=\min\{v_p(\mathscr R_{63}^\star),v_p(\widehat{\mathscr D}_{63})\},
\]
则 common depth至少把 corresponding additive/descendant errors送入 `q`；但在 higher transport layers，这些 errors仍可能发生 canonical balance cancellation。历史 second/third/quartic descendant hierarchy正是在审计这种现象。

所以本文**不**把 (5.1) 夸大成未经证明的

\[
v_p(\mathscr P_{63})=h_p.
\]

严格新增的是：

\[
\boxed{
\text{一旦 compatibility residual }q\text{ 的深度确定，}
\mathscr P_{63}\text{ 精确原样读取该深度。}}
\tag{6.1}
\]

因此后续真正需要比较的只剩 `q` 与 terminal transport depth；resultant 自身已经从开放变量中删除。

---

## 7. parity implication

旧 integer-carrier theorem 已证明

\[
\mathscr P_{63}>0,
\qquad
\mathscr P_{63}^{\circ}\equiv1\pmod8.
\]

所以 generic external carrier全部 `3 mod4` prime exponents的总 parity为偶。

结合 (5.1)，若后续 terminal transport证明某枚 generic external inert prime在 `q` 中必须以奇深度出现，则 `P_63` 的 `1 mod4` orientation会自动强迫至少另一枚 distinct inert prime以奇深度出现。这个 surcharge现在是合法的，因为 (5.1) 排除了 resultant multiplicity扭曲 parity的可能。

本文尚未证明 terminal spill 的 particular supplier必在 `q` 中为奇深度，因此这里只记录接口，不提前收费。

A2 仍为 `待证`。

---

## 8. verification

```bash
uv run python scripts/exact-lift/a2-only/research-checks/crt-descent/check_a2_descendant_projective_exact_depth_reader.py
```

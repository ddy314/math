# A2 external shared-outer reuse 塌缩到两个 fixed templates

> **依赖：** `outer-descendant-additive-lock.md`；`crt-descent-ledger.md` 中 `spontaneous-crt-universal-descendant-cubic.md`、`spontaneous-crt-pure-coefficient-singular.md`；`endpoint-lattice.md` 的 rational-root divisibility。
>
> **严格状态：**危险 `Z≡1 (mod4)` orientation 中，若同一 non-`3` inert prime `p` 同时支付两个 outer cofactors `Xi_-,Xi_+` 并属于 descendant common gcd `G_Delta`，则 additive coefficient-ratio lock 把它压到 `K=3`、central `2K-9=0` 或 quartic `Q_4(K)=0`。本文再加入 universal descendant cubic `E_63=0`，完整审计真实 `F_p` 公共根，并恢复 actual defect root `J=3-C/D`。central sheet无 non-`3` odd root；quartic apparent factors `23,31` 没有真实三方 root，`11491` 只给 `K=0` projective boundary。两个大 generic candidates又分别落在 `J=2`、`J=4`，因此必须通过 outer denominator 除法后的 derivative gate，但其导数均为 unit，故严格排除。最终 shared external reuse只剩 coefficient-singular `p=7` 模板与一枚 generic fixed prime `24303427940647`。本文不排除这两个模板，因此不宣称 A2 closure。

---

## 1. additive-locked outer pair

沿用

\[
R_0(K,\zeta)=K^2-(18+4\zeta)K+18\zeta+55
\]

以及

\[
\Phi(J)=J(J+2\zeta)(K-J)^2-R_0(J+\zeta)^2.
\]

若 `p|G_Delta` 且同一 `p` 还整除 `Xi_-`,`Xi_+`，则

\[
\Phi_2:=\Phi(2)\equiv0,
\qquad
\Phi_4:=\Phi(4)\equiv0\pmod p.
\]

令

\[
H_{24}:=\frac{\Phi_4-\Phi_2}{4}.
\]

已有 exact resultant

\[
\boxed{
\operatorname{Res}_{\zeta}(\Phi_2,H_{24})
=2(K-3)^2(2K-9)Q_4(K),
}
\]

其中

\[
\boxed{
Q_4(K)=676K^4-8004K^3+34801K^2-65868K+45964
}
\]

在 `Q[K]` 中不可约。

所以 shared supplier 只能落在

\[
K=3,
\qquad
2K-9=0,
\qquad
Q_4(K)=0.
\]

---

## 2. 加入 universal descendant cubic

真正的 descendant-common prime还必须满足

\[
\boxed{\mathcal E_{63}(K,\zeta)=0.}
\]

central sheet首先立刻消失：

\[
\operatorname{Res}_{\zeta}
\bigl(\Phi_2(9/2,\zeta),H_{24}(9/2,\zeta)\bigr)=144.
\]

故

\[
\boxed{p\ne3\Longrightarrow 2K-9=0\text{ 不可能支付两个 outer cofactors}.}
\]

在 `K=3` 上，`Phi_2,H_24` 的 characteristic-zero common root唯一为

\[
\zeta=-3.
\]

代入 universal cubic：

\[
\boxed{
\mathcal E_{63}(3,-3)
=3^{10}\cdot5\cdot7^2\cdot41\cdot173.
}
\]

其中唯一 non-`3` inert support为

\[
\boxed{p=7.}
\]

对应 first-layer state

\[
\boxed{(p,K,\zeta)=(7,3,4).}
\]

---

## 3. quartic component 的线性 `zeta` reader

`Phi_2,H_24` 的 subresultant chain 中，quartic component上的倒数第二项为

\[
2(2K-9)(A(K)\zeta+B(K)),
\]

其中

\[
\boxed{A(K)=(2K-9)(9K^2-52K+72),}
\]

\[
\boxed{B(K)=26K^3-297K^2+1052K-1158.}
\]

所以在 generic coefficient sector

\[
\zeta=-B/A.
\]

把它代入 `E_63`，乘 `A^3` 后模 `Q_4` 取 remainder，得到一个 degree-3 `K` polynomial。与 `Q_4` 求 resultant，其完整 support为

\[
\begin{aligned}
&2^{50}3^6 7\,13^{84}23^6 29^6 31^6\cdot1069\cdot11491^2\cdot408461\\
&\qquad\cdot39054007\cdot5070995047\cdot24303427940647.
\end{aligned}
\]

只需审计其中 `3 mod4` factors。直接在 `F_p` 中计算 `gcd(Phi_2,H_24,E_63)`：

- `23`：无真实 `zeta` common root；
- `31`：无真实 `zeta` common root；
- `11491`：唯一 triple为 `K=0,zeta=743`，属于 `r=1/K` 的 nongenuine projective boundary；
- 剩余 genuine triples为

\[
\boxed{(7,3,4),}
\]

\[
\boxed{(39054007,14318314,3933315),}
\]

\[
\boxed{(5070995047,1187202050,2738876184),}
\]

\[
\boxed{(24303427940647,21805672591624,9250192938088).}
\]

所以 moving external kernel已经被固定成四个 first-layer templates。

---

## 4. 恢复 actual defect root

universal descendant equation在 noncentral sector唯一恢复

\[
\boxed{
J=
\frac{K^2-64K\zeta-576K+288\zeta+1296}
{16(2K-9)}.
}
\]

四个状态分别给

\[
\boxed{
\begin{array}{c|c|c}
p&J\pmod p&C/D=3-J\pmod p\\ \hline
7&3&0\\
39054007&2&1\\
5070995047&4&-1\\
24303427940647&3&0
\end{array}}
\]

中间两行不是无害 residue：它们恰好撞到 outer cofactors 已经除去的 denominator。

---

## 5. divided difference 删除 `39054007`

实际 root为

\[
J=3-C/D.
\]

若 `J=2 mod p`，则

\[
p\mid D-C.
\]

又 `F(J)=0` 为 exact rational-root equation。写 polynomial divided difference：

\[
F(2)-F(J)=(2-J)\,\mathscr D_F(2,J).
\]

因为

\[
2-J=-\frac{D-C}{D},
\]

所以在 `p∤D` 下

\[
\frac{F(2)}{D-C}
\equiv
-\frac{F'(2)}{D}
\pmod p.
\]

`Xi_-` 与左边只差 `p`-adic units。因此若 `p|Xi_-`，必要条件是

\[
\boxed{F'(2)\equiv0\pmod p.}
\]

除去 `B^2T^2` 的 unit scale，等价检查 `Phi'(2)`。

在 fixed state

\[
p=39054007,
\quad(K,\zeta)=(14318314,3933315)
\]

checker给

\[
\boxed{
\Phi'(2)\equiv36568040\not\equiv0\pmod{39054007}.}
\]

矛盾。因此

\[
\boxed{39054007\text{ 不能同时支付 }\Xi_-,\Xi_+.}
\]

---

## 6. divided difference 删除 `5070995047`

同理若 `J=4 mod p`，则

\[
p\mid D+C.
\]

因为

\[
4-J=\frac{D+C}{D},
\]

有

\[
\frac{F(4)}{D+C}
\equiv
\frac{F'(4)}{D}
\pmod p.
\]

故 `p|Xi_+` 必须满足

\[
\Phi'(4)=0.
\]

但 fixed state

\[
p=5070995047,
\quad(K,\zeta)=(1187202050,2738876184)
\]

满足

\[
\boxed{
\Phi'(4)\equiv1135701515\not\equiv0\pmod{5070995047}.}
\]

所以

\[
\boxed{5070995047\text{ 同样被严格排除}.}
\]

---

## 7. 真正剩余的两个 fixed templates

于是 external shared-outer descendant reuse只剩

\[
\boxed{(p,K,\zeta)=(7,3,4)}
\]

与

\[
\boxed{
(p,K,\zeta)=
(24303427940647,
21805672591624,
9250192938088).
}
\]

两者都满足

\[
J=3,
\qquad p\mid C,
\]

所以 §5–§6 的 outer-denominator divided-difference squeeze不适用。

进一步，`7` 状态落在 descendant Euclidean remainder的 coefficient-singular sector `A_63=B_63=0`；大素数状态则是 generic coefficient state。故最终 frontier自然分成：

1. **fixed singular 7**：应送入 `H_4/H_24` projective ratio gates继续审计；
2. **fixed generic**
   \[
   p_\infty:=24303427940647;
   \]
   应利用 `J=3`, `p_infty|C`、unique projective phase与 natural-representative depth继续审计。

这已经把此前的 genuinely external moving shared-reuse family完全固定化，但尚未把最后两个模板排空。

A2 仍为 `待证`。

---

## 8. verification

```bash
uv run python scripts/exact-lift/a2-only/research-checks/crt-descent/check_a2_external_shared_outer_fixed_templates.py
```

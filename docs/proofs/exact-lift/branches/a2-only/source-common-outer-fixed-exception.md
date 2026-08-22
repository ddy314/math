# A2 source-common outer fixed-exception audit（已被 additive lock 覆盖）

> **状态：** `已严格完成 / 后续加强覆盖`。
>
> 本文件保留一条较弱 elimination 的审计记录。只联立 source-common line `18K-55=0`、free-ratio outer-pair cubic `G_pm=0` 与 universal descendant cubic `E_63=0` 时，全部 non-`3` inert support 会塌成唯一 fixed prime
> \[
> p_\star=740759498168792879433565547.
> \]
> checker `check_a2_source_common_outer_fixed_exception.py` 仍验证这一较弱 necessary condition、完整 resultant factorization 与真实 `F_{p_*}` 公共根。
>
> **但是 `p_*` 不再是活跃 frontier。** 后续 [`outer-descendant-additive-lock.md`](outer-descendant-additive-lock.md) 使用新证明的
> \[
> \gcd(\widehat{\mathcal T}_2,\mathscr R_{63}^\star)
> =\gcd(\widehat{\mathcal T}_2,\widehat{\mathscr D}_{63})
> =G_\Delta
> \]
> 把 original additive coefficient ratio 重新锁回 rational-root quartic，并严格证明 source-common shared outer/descendant inert pool **为空**。因此本文件不得再被引用为“存在一个未决 giant prime exception”的依据。

---

## 1. 较弱 elimination 留下的 fixed prime

令

\[
\zeta=a_3/T,
\qquad
K\equiv55/18
\]

来自 source-common line。把 shared-outer free-ratio gate代入得到

\[
G_S(\zeta)=217\zeta^3+219\zeta^2-1728\zeta-1152.
\]

把 universal descendant cubic在同一 `K=55/18` 上清分母得到 primitive cubic `E_S(\zeta)`。checker 验证

\[
\begin{aligned}
\left|\operatorname{Res}_\zeta(G_S,E_S)\right|
={}&41\cdot64217\cdot72238473017\\
&\cdot2679539349324345019093\\
&\cdot740759498168792879433565547.
\end{aligned}
\]

前四枚 prime 都是 `1 mod4`，唯一 inert factor 是 `p_*`。并且

\[
\gcd_{\mathbf F_{p_*}[\zeta]}(G_S,E_S)
=
\zeta-121854543490110025177920950,
\]

所以它确实是该**较弱系统**的真实 first-layer `F_p` 交点，而非扩域伪根。

此外 checker 记录

\[
\left(\frac{55}{p_*}\right)=1,
\qquad
\left(\frac{-26}{p_*}\right)=-1,
\]

说明重复旧 quadratic characters 也不会杀掉这个较弱 candidate。

---

## 2. 后续 additive lock 为什么删除 `p_*`

较弱系统漏掉了一条后来才显式接上的信息：若 prime 属于 descendant common gcd `G_Delta`，新的 gcd theorem 同时强迫

\[
p\mid\widehat{\mathcal T}_2.
\]

于是 rational-root quartic 中原本被交叉消掉的 coefficient ratio 实际必须满足

\[
\frac{Q^2N_0}{b_2^2}
\equiv
R_0(K,\zeta)
:=K^2-(18+4\zeta)K+18\zeta+55
\pmod p.
\]

因此 shared outer supplier必须满足更强的

\[
\Phi_0(2)=\Phi_0(4)=0.
\]

[`outer-descendant-additive-lock.md`](outer-descendant-additive-lock.md) 对这两个式子完成 exact elimination，并证明再与 `18K-55=0` 相交后 odd primes 只剩

\[
13,\qquad1350049,
\]

且两者都为 `1 mod4`。所以

\[
\boxed{
\text{genuine source-common shared outer/descendant inert pool}=\varnothing.
}
\]

特别地，在旧 `p_*` residue上直接有

\[
\Phi_0(2)\not\equiv0,
\qquad
\Phi_0(4)\not\equiv0
\pmod{p_*}.
\]

故 `p_*` 已严格删除，不再属于当前 A2 frontier。

---

## 3. verification

较弱 audit：

```bash
uv run python scripts/exact-lift/a2-only/research-checks/crt-descent/check_a2_source_common_outer_fixed_exception.py
```

加强后的真正 frontier certificate：

```bash
uv run python scripts/exact-lift/a2-only/research-checks/crt-descent/check_a2_outer_descendant_additive_lock.py
```

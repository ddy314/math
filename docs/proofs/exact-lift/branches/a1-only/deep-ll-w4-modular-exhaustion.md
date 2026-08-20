# A1 minimal diagonal: `(z,w)=(1,4)` moderate-LL modular exhaustion

> 日期：2026-08-20。依赖 `deep-ll-pell-normal-form.md`、`deep-typewise-r-window.md`、`deep-moderate-block-partition.md` 与原 rational-contact square。当前范围 `k=g>=31`。

本文关闭第一个完整 moderate-LL prefix type：

\[
\boxed{(z,w)=(1,4),\quad \text{moderate LL is empty for all }k\ge31.}
\]

方法与 central modular exhaustion 同型：不求 Pell 基本解，而是把 fixed LL supply quadratic 与原 contact square 在有限素数模下联立，再用 `10^k mod p` 的有限周期做 exact cover。

状态：**已严格完成；附 C++ exact certificate。**

---

## 1. 完整 finite LL parameter set

`deep-typewise-r-window.md` 给 `(1,4)`：

\[
\boxed{216090\le r\le4394372.}
\]

LL valuation identities 为

\[
v_2(r)=A+2\nu_2+2,
\qquad
v_5(r)=B+2\nu_5,
\]

其中 `A,B>0`。因为 `w=4`，deep 2-adic parity theorem 强迫

\[
\boxed{A\text{ odd}.}
\]

本类型所有 `A>0` 都是原 contact 的 strict 2-low，因此 `deep-moderate-block-partition.md` 还给

\[
\boxed{r_{10}\equiv1\pmod4.}
\]

固定 `(r,nu_2,nu_5)` 后

\[
D=2^A5^B
\]

固定，并且 `deep-ll-pell-normal-form.md` 给 typewise gap interval

\[
15.0949872D<\gamma<21.00225945D.
\]

`B` 的完整 `Q_2/Q_5` squareclass 进一步把 `gamma` 限在两个 `mod 40` classes。

对所有这些必要条件做 exact integer enumeration，共得到

\[
\boxed{4,331,873}
\tag{1}
\]

个 local-compatible fixed LL Pell families。

注意此集合故意仍包含 square-`A_{gamma,r,D}` 的退化 families，所以它是实际剩余核心的安全超集。

---

## 2. odd-prime modular condition

LL fixed quadratic 为

\[
C_0N_0^2-uLN_0+1000\gamma^2L^2+\gamma R=0,
\]

其中

\[
C_0=156,
\quad R=r/D,
\quad u=790\gamma+Dr,
\quad L=10^k/D.
\]

对奇素数 `p!=2,5`，给定

\[
(r\bmod p,D\bmod p,\gamma\bmod p,k\bmod\operatorname{ord}_p(10)),
\]

该式关于 `N_0 mod p` 是一个普通二次方程，因此至多需要检查两个根。

每个根还必须通过原 rational-contact square：写

\[
\rho=N_0-\frac{\gamma}{D10^k},
\]

则

\[
K-2\rho(10^kQ)\mathcal N
\]

必须是 `mod p` 的平方剩余。

因此每个 `p` 精确给出允许的 `k` residue set。

---

## 3. common period-420 stage

取

\[
\boxed{
\mathcal P_0=
\{3,7,11,13,29,31,37,41,43,61,71,101,127\}.}
\]

这些素数均满足

\[
\operatorname{ord}_p(10)\mid420.
\]

把 (1) 的每个 family 的允许 classes 拉回 `k mod 420` 后求交，得到：

\[
\boxed{
4,331,873\longrightarrow18,342\text{ families},
}
\tag{2}
\]

总 surviving `k mod420` states 为

\[
\boxed{28,788.}
\tag{3}
\]

---

## 4. supplemental individual CRT pruning

再使用

\[
\boxed{
\mathcal P_1=
\{17,19,73,89,113,137,251,337,1009,4201\}.}
\]

对每个 family，若其 `k mod420` mask 与某个 `p` 的允许 `k mod ord_p(10)` classes 在

\[
\gcd(420,\operatorname{ord}_p(10))
\]

上已经不兼容，则立即删除。

这一安全 pruning 把 (2) 压到

\[
\boxed{2,271}
\tag{4}
\]

个 families。

---

## 5. exact joint period `277200`

`P_1` 中所有乘法阶与 `420` 的最小公倍数恰为

\[
\boxed{277200.}
\]

所以对 (4) 的每个 family，可把 surviving `k mod420` mask 精确提升到

\[
k\bmod277200
\]

并同时与全部 `P_1` residue sets 求交。

完整联合交集后只剩

\[
\boxed{154}
\tag{5}
\]

个 families 具有任何周期状态。

---

## 6. final order-dividing cover

最后加入

\[
\boxed{
\mathcal P_2=
\{67,151,181,211,239,241,271,281,421,631,1933,2161,2689\}.}
\]

这些素数的 `ord_p(10)` 都整除 `277200`，因此无需再扩周期：直接在现有 `k mod277200` states 上逐素数相交即可。

结果：

\[
\boxed{154\longrightarrow0.}
\tag{6}
\]

没有任何 residue state 存活。

---

## 7. 结论

所有步骤只使用：

- exact typewise finite `r` window；
- LL valuation identities；
- strict-2-low parity / `r_10 mod4`；
- exact local `gamma mod40` squareclasses；
- fixed LL supply quadratic；
- 原 rational-contact square；
- finite multiplicative orders 与 CRT。

没有截断 `k`，也没有 factor `b_1,Q`。

因此：

\[
\boxed{
\forall k\ge31,
\quad
(z,w)=(1,4)\text{ moderate LL is impossible}.}
\tag{7}
\]

结合 `deep-double-5high-collapse.md`：`(1,4)` moderate double-deep 从此只可能位于 `HL`；`LL` 与已关闭的 `LH` 都已消失。

---

## 8. 可复核证书

脚本：

`../../../../../scripts/exact-lift/a1-only/check_a1_deep_ll_w4_modular_exhaustion.cpp`

最终断言统计：

```text
local=4331873
common_families=18342
common_k420_states=28788
after_individual_supplement=2271
joint_k277200_families=154
final=0
CERTIFICATE OK
```

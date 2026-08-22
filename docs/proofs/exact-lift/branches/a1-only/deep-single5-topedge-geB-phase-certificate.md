# A1 minimal diagonal: close top-edge `v5(N)>=B` by phase-gap certificate

> 日期：2026-08-22。
>
> 依赖：`deep-single5-topedge-finite-height.md`、`deep-single5-topedge-phase-shell.md`、`deep-single5-decimal-height-collapse.md`。
>
> 可复核脚本：
> `scripts/exact-lift/a1-only/research-checks/topedge-geB-phase/check_topedge_geB_phase.py`。

状态：**严格有限证书。** 本文同时关闭 top edge 的 5-adic resonance `v5(N)=B` 与 high-5 `v5(N)>B` 两支。

---

## 1. finite box

沿用 theorem-derived bounds：

\[
32\le k\le k_{\max}(z,w),
\]

\[
(k_{\max})=(77,75,74,72,74,73),
\]

以及

\[
1000B<2293k+7570.
\]

所以 certificate 只处理先被严格压成有限的 top edge。

---

## 2. `v5(N)>=B` 的两个 Hensel progressions

固定 `(k,z,w)`，写

\[
N=(A_0+N_0)^2+C_0^2,
\]

其中

\[
A_0=100T^3+(10(5-z-w)+1)T-1,
\]

\[
C_0=(10T^2-z)(10T^2-w).
\]

条件

\[
v_5(N)\ge B
\]

等价于

\[
N\equiv0\pmod{5^B}.
\]

由于 `5∤C0`，令 `i^2=-1 mod 5^B`，全部解恰为

\[
\boxed{
N_0\equiv-A_0\pm C_0i\pmod{5^B}.
}
\tag{1}

这同时覆盖 resonance 与 high-5，不需要先知道 exact `v5(N)`。

---

## 3. phase-gap residue

置

\[
d=B-k.
\]

phase shell 与 gap integrality 给

\[
\boxed{
h2^{3k}=5^{d-1}L+\varepsilon,}
\tag{2}
\]

\[
\boxed{0<\varepsilon<6\,5^d,}
\tag{3}
\]

其中

\[
L=(10T^2-(15-z))N_0-c_{z,w}T.
\]

因此必须

\[
\boxed{
\varepsilon\equiv-5^{d-1}L\pmod{2^{3k}}.
}
\tag{4}

把 (1) 写成 `N0=r+t5^B` 后，(4) 是关于 `t` 的线性 modular interval：

\[
0<(at+b)\bmod2^{3k}<6\,5^d.
\tag{5}

脚本使用 exact floor-sum 直接统计 (5)，不展开 progression 中的每个 `N0`。

---

## 4. certificate totals

在完整 theorem-derived finite box 中：

- 非空 Hensel progressions：
  \[
  \boxed{11853};
  \]
- 它们在十进制窗口中代表的 `N0` 总数：
  \[
  \boxed{216756621563705118896955};
  \]
- 满足 phase-gap residue (3),(4) 的总数：
  \[
  \boxed{0}.
  \]

因此

\[
\boxed{
\lambda_2=2k-1,\qquad v_5(N)\ge B
\Longrightarrow\text{empty}.
}
\tag{6}

---

## 5. updated top-edge frontier

结合本文，single-5 top edge 只可能位于

\[
\boxed{v_5(N)<B.}
\]

也就是说 5-adic resonance 与 high-5 全部消失。下一步只需处理 §3.1 的 strict-5-low exact depth

\[
d_5=2k+\frac{3B-v_5(N)}2,
\]

并与同一个 phase-gap residue、high 2-adic sign equation 联立。
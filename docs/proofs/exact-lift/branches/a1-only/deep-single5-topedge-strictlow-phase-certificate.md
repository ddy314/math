# A1 minimal diagonal: close top-edge strict-5-low by phase-gap certificate

> 日期：2026-08-22。
>
> 依赖：`deep-single5-topedge-finite-height.md`、`deep-single5-topedge-phase-shell.md`、`deep-single5-decimal-height-collapse.md`。
>
> 可复核脚本：
> `scripts/exact-lift/a1-only/research-checks/topedge-strictlow-phase/check_topedge_strictlow_phase.py`。

状态：**严格有限证书；关闭 single-5 top edge 的整个 strict-5-low branch `v5(N)<B`.**

---

## 1. strict-low 的最弱 possible decimal height

记

\[
n_5:=v_5(N)<B.
\]

`deep-single5-decimal-height-collapse.md` 的 exact 5-adic depth 为

\[
\boxed{
d_5=2k+\frac{3B-n_5}{2}.}
\tag{1}
\]

平方 parity 强迫

\[
B\equiv n_5\pmod2.
\]

由于 `n5<B`，因此

\[
\boxed{B-n_5\ge2.}
\tag{2}
\]

strict-low 中 `d5>B+k`，decimal synchronization 强迫实际 completion height

\[
n=d_5.
\]

由 (1),(2)，所有 strict-low states 都至少满足

\[
\boxed{n\ge B+2k+1.}
\tag{3}
\]

等号对应最弱、最容易满足的 `n5=B-2`。所以若连 (3) 的最弱 high-sign divisibility 都无解，更深的 `n5` states 自动全空。

---

## 2. high-sign congruence 与 phase-gap identity

置

\[
d=B-k,
\qquad c=5^{B+2k}.
\]

top-edge high sign 满足

\[
\boxed{
v_2(h+cQ)=n-1.}
\tag{4}
\]

特别由 (3)：

\[
\boxed{h+cQ\equiv0\pmod{2^{B+2k}}.}
\tag{5}
\]

另一方面 phase-gap exact identity 为

\[
\boxed{h2^{3k}=5^{d-1}L+\varepsilon,}
\tag{6}
\]

\[
\boxed{0<\varepsilon<6\,5^d,}
\tag{7}
\]

其中

\[
L=(10T^2-(15-z))N_0-c_{z,w}T.
\]

将 (5) 乘以 `2^(3k)` 并代入 (6)，得到所有 strict-low candidate 都必须满足的较弱必要条件

\[
\boxed{
\varepsilon
\equiv-\left(5^{d-1}L+cQ2^{3k}\right)
\pmod{2^{B+5k}}.
}
\tag{8}

注意这里已经把 exact `n5` 消掉；任何更低的 `n5` 只会要求比 (8) 更深的 2-adic congruence。

---

## 3. 对整个 decimal prefix interval 的 exact counting

固定 `(z,w,k,B)` 后，(8) 右侧关于 `N0` 是线性的。因此在完整 prefix interval

\[
10^{k-1}\le N_0<10^k
\]

上，只需统计

\[
\boxed{
0<(aN_0+b)\bmod2^{B+5k}<6\,5^d.
}
\tag{9}

脚本用 exact integer `floor_sum` 一次性统计每个完整十进制区间，不逐点枚举 `N0`，也不需要 factor `b1,Q`。

finite-height theorem 与 `B<2.293k+7.57` 给总共

\[
\boxed{19613}
\]

个 `(type,k,B)` 组合。

---

## 4. certificate result

对全部 19613 个组合，(9) 的总命中数为

\[
\boxed{0}.
\]

因此

\[
\boxed{
\lambda_2=2k-1,\qquad v_5(N)<B
\Longrightarrow\text{empty}.
}
\tag{10}

---

## 5. single-5 top edge fully closed

`deep-single5-topedge-geB-phase-certificate.md` 已证明

\[
v_5(N)\ge B\Longrightarrow\text{empty}.
\]

本文证明互补分支

\[
v_5(N)<B\Longrightarrow\text{empty}.
\]

故

\[
\boxed{
\text{single-5 top edge }\lambda_2=2k-1\text{ is empty}.
}
\tag{11}

结合此前 low-edge closure，整个 minimal-diagonal single-5 deep sector 为空：

\[
\boxed{\text{single-5 deep}=\varnothing.}
\tag{12}

下一步应做 sector-exhaustion audit：把 single-2、single-5、double-deep 与 central denominator 的既有关闭逐条拼接，确认 minimal diagonal 是否已经可以正式升级为全空。
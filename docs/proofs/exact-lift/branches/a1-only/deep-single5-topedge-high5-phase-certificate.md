# A1 minimal diagonal: close top-edge high-5 by phase-gap certificate

> 日期：2026-08-22。
>
> 依赖：`deep-single5-topedge-finite-height.md`、`deep-single5-topedge-phase-shell.md`、`deep-single5-decimal-height-collapse.md`。
>
> 可复核脚本：
> `scripts/exact-lift/a1-only/research-checks/topedge-high5-phase/check_topedge_high5_phase.py`。

状态：**严格有限证书；关闭 single-5 top edge 的整个 `v5(N)>B` branch。** 不依赖 `b1,Q` 的完整 factorization。

---

## 1. theorem-derived finite box

由 `deep-single5-topedge-finite-height.md`，top edge 只可能出现在

\[
32\le k\le k_{\max}(z,w),
\]

其中

\[
(k_{\max})=(77,75,74,72,74,73)
\]

按六类型顺序排列。

又由 `deep-single5-topedge-supply-compression.md`：

\[
B<2.293k+7.57.
\]

因此以下 certificate 只扫描先由证明严格推出的有限 `(k,B,type)` 盒。

---

## 2. high-5 prefix 是两个 simple Hensel progressions

固定 `(k,z,w)`，写

\[
a_1=A_0+N_0,
\]

\[
A_0=100T^3+(10(5-z-w)+1)T-1,
\]

\[
C_0=(10T^2-z)(10T^2-w).
\]

则

\[
N=(A_0+N_0)^2+C_0^2.
\]

若

\[
\boxed{v_5(N)>B,}
\tag{1}
\]

则

\[
N\equiv0\pmod{5^{B+1}}.
\]

由于 `5∤C0`，这是 simple Hensel 情形。令

\[
i^2\equiv-1\pmod{5^{B+1}},
\]

则全部 high-5 prefixes 精确落在两条 progressions

\[
\boxed{
N_0\equiv-A_0\pm C_0i
\pmod{5^{B+1}}.
}
\tag{2}

脚本用纯整数逐位 Hensel lift 构造两个 `i`，不调用概率 factorization。

---

## 3. phase shell 与 gap integrality 给 `2^(3k)` 超深 residue

置

\[
d=B-k.
\]

`deep-single5-topedge-phase-shell.md` 给 phase remainder

\[
E=5^dA_{z,w}-10\,2^k\gamma,
\]

\[
0<E<30\,5^d.
\]

令

\[
\varepsilon=E/5.
\]

则

\[
\boxed{0<\varepsilon<6\,5^d.}
\tag{3}
\]

`deep-single5-topedge-finite-height.md` 的 exact identity 为

\[
\boxed{
h2^{3k}=5^{d-1}L+\varepsilon,}
\tag{4}
\]

其中

\[
L=(10T^2-(15-z))N_0-c_{z,w}T,
\]

\[
c_{1,w}=339-40w,
\qquad
c_{3,w}=237-20w.
\]

因为 `h` 为整数，(4) 立刻给

\[
\boxed{
\varepsilon
\equiv-5^{d-1}L
\pmod{2^{3k}}.
}
\tag{5}

这比仅由 `gamma∈Z` 得到的 `2^(k+1)` phase residue 强两个完整 `k`-layers。

---

## 4. Hensel progression 上变成 exact modular-interval counting

每条 (2) 写成

\[
N_0=r+t5^{B+1}
\]

并只保留十进制窗口

\[
10^{k-1}\le N_0<10^k.
\]

由于 `L` 对 `N0` 是线性的，(5) 沿 progression 变成

\[
\varepsilon_t
\equiv at+b
\pmod{2^{3k}}
\]

其中 `a,b` 都由 `(k,B,z,w,r)` 精确确定。

需要计数的不是所有 `t`，而是

\[
\boxed{
0<(at+b)\bmod2^{3k}<6\,5^d.
}
\tag{6}

脚本使用标准 exact `floor_sum` 恒等式在 `O(log 2^(3k))` 时间内统计一个 progression 的 (6) 命中数；因此即使 progression 含有天文多个 `N0`，也无需逐点枚举。

---

## 5. 完整 certificate 结果

在全部 theorem-derived finite `(k,B,type)` 盒内：

- 非空 Hensel progressions 数：
  \[
  \boxed{11335};
  \]
- 这些 progressions 在十进制窗口中代表的原始 `N0` 状态总数：
  \[
  \boxed{43351324312741023779405};
  \]
- 满足 phase-gap residue (3),(5) 的状态数：
  \[
  \boxed{0}.
  \]

因此

\[
\boxed{
\lambda_2=2k-1,\qquad v_5(N)>B
\Longrightarrow\text{empty}.
}
\tag{7}

这排除了 full sign 与 matching sign 中所有可能依赖 `v5(N)>B` 的 top-edge states；没有使用 Q-side / b1-side factorization，也没有使用抽样或浮点。

---

## 6. 更新后的 single-5 top-edge frontier

结合 low-edge closure 与本文，single-5 仅剩 top-edge 中不满足 (1) 的 5-adic allocation，也就是

\[
\boxed{v_5(N)\le B}
\]

相关终端（若 corrected sign-allocation 仍允许）。

下一步应直接对 `v5(N)<B` 与 resonance `v5(N)=B` 使用 §3.1/§3.3 的 exact 5-adic denominator depths，再与同一个 phase-gap residue (5) 联立。
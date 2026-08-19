# A1 minimal diagonal `k=g=6, ell=6` residual-shell certificate

> 日期：2026-08-19。
> 本文继续 `k6-first-boundary-certificate.md`，关闭下一条 tail shell
> \[
> \boxed{
> d=2,\quad r=s=1,\quad k=g=6,\quad \ell=6.
> }
> \]

结论：

\[
\boxed{\text{该 shell 为空。}}
\]

验证脚本：

```bash
uv run python scripts/exact-lift/a1-only/check_a1_top_diag_k6_ell6.py
```

状态：**有限 divisor-congruence 证书。**

---

## 1. residual 窗只有 `6,...,50`

`positive-tail-residual.md` 给出

\[
5.09\,10^{\ell-k}<t<50.45\,10^{\ell-k}.
\]

当前

\[
\ell=k=6,
\]

所以

\[
5.09<t<50.45.
\]

因此

\[
\boxed{t\in\{6,7,\ldots,50\}.}
\tag{1}
\]

---

## 2. 整个 shell 都属于 regular residual regime

对 `6<=t<=50`：

\[
v_2(t)\le5<6,
\]

\[
v_5(t)\le2<6.
\]

因此 `residual-shell-supply.md` 对全部 45 个 residual 都适用。

令

\[
a_t=2^{v_2(t)}5^{v_5(t)},
\qquad
\widehat t=t/a_t.
\]

任何 exact candidate 都必须满足

\[
\boxed{b_3=a_t h,}
\tag{2}
\]

其中 `h` 属于完整 odd-prime supply，并且

\[
\boxed{
\frac{10^6}{a_t}\mid h+\widehat t.
}
\tag{3}
\]

一旦通过，prefix integer 唯一恢复为

\[
\boxed{
N_0=\frac{a_t(h+\widehat t)}{10^6}.
}
\tag{4}
\]

再要求

\[
10^5\le N_0<10^6.
\]

---

## 3. 完整 supply

与 `k6-first-boundary-certificate.md` 相同，`k=6` 四种 `w` 的 odd-prime supply 数为：

| `w` | `#h` |
|---:|---:|
| `1` | `64` |
| `2` | `32` |
| `3` | `2` |
| `4` | `8` |

这些集合已包含所有可能的 Q-side divisor 和所有允许的 `b_1` 侧 `1 mod4` whole prime-power block selectors。

---

## 4. 精确结果

脚本对每个

\[
w\in\{1,2,3,4\},
\qquad
6\le t\le50,
\qquad
h\in\mathcal H_{6,w}
\]

检查 (3) 与 `N_0` 位数条件。

结果：

| `w` | shell hits |
|---:|---:|
| `1` | `0` |
| `2` | `0` |
| `3` | `0` |
| `4` | `0` |
| **总计** | **0** |

因此 even before 使用 `z`、prefix coprimality、`K>0` 或 rational-square sieve，必要 divisor-congruence 超集已经为空。

所以

\[
\boxed{
 d=2,\ r=s=1,\ k=g=6,\ \ell=6
\text{ 为空。}
}
\tag{5}

---

## 5. `k=6` 当前剩余前沿

positive residual theorem 已经排除

\[
\ell\le4.
\]

第一 boundary certificate 排除

\[
\ell=5.
\]

本文再排除

\[
\ell=6.
\]

因此任何尚存的 `k=g=6` candidate 必须满足

\[
\boxed{\ell\ge7.}
\tag{6}
\]

从 `ell=7` 开始，residual 窗为

\[
50.9<t<504.5,
\]

即 `t=51,...,504`。其中大多数 residual 仍满足 regular-shell 条件；只有少量具有 `v_2(t)>=7` 或 `v_5(t)>=7` 的 deep-2/5 residual 需要单独处理。下一步可以把 `ell=7` 分成 regular 与 deep-2/5 两部分继续压缩。
# A1 minimal diagonal `k=g=6` first-boundary certificate

> 日期：2026-08-19。
> 本文关闭当前首个未完成层中的第一条尾长边界
> \[
> \boxed{
> d=2,\quad r=s=1,\quad k=g=6,\quad \ell=k-1=5.
> }
> \]

结论：

\[
\boxed{\text{该 boundary 为空。}}
\]

验证脚本：

```bash
uv run python scripts/exact-lift/a1-only/check_a1_top_diag_k6_boundary.py
```

状态：**有限 divisor-congruence 证书。**

---

## 1. 不再枚举 prefix 区间

`positive-tail-residual.md` 已证明第一 boundary 只有

\[
t\in\{1,2,3,4,5\}.
\]

`boundary-residual-2adic.md` 又把 even-`w` 类型收紧为

\[
w=2\Longrightarrow t=3,
\]

\[
w=4\Longrightarrow t=1.
\]

因此需要检查的 residual 集合为

\[
\begin{array}{c|c}
w&t\\
\hline
1&1,2,3,4,5\\
2&3\\
3&1,2,3,4,5\\
4&1
\end{array}
\]

另一方面 `boundary-decimal-supply.md` 已证明：令

\[
a_t=2^{v_2(t)}5^{v_5(t)},
\qquad
\widehat t=t/a_t,
\]

则

\[
b_3=a_t h
\]

且必须

\[
\boxed{
\frac{10^{k-1}}{a_t}\mid h+\widehat t.
}
\tag{1}
\]

一旦 `h` 固定，prefix integer 由

\[
\boxed{
N_0=\frac{a_t(h+\widehat t)}{10^{k-1}}
}
\tag{2}
\]

唯一恢复。

所以本证书根本不扫描

\[
10^5\le N_0<10^6
\]

的九十万个整数；只需枚举 denominator prime graph 给出的有限 `h` supply。

---

## 2. `k=6` 的完整 odd-prime supply 数量

这里

\[
b_1=10^{13}-w,
\qquad
Q=10b_1+1.
\]

对每个 `w`，脚本精确分解 `b_1,Q`，构造

\[
h=q\,s,
\]

其中

\[
q\mid Q
\]

而 `s` 是 `b_1` 中 `1 mod4` odd prime-power blocks 的 whole-block selector。

得到完整 supply 数：

| `w` | `#h` |
|---:|---:|
| `1` | `64` |
| `2` | `32` |
| `3` | `2` |
| `4` | `8` |

脚本把这些数量写成断言，因此未来若因子分解或 supply 实现被修改，会立即报错。

---

## 3. decimal congruence 检查结果

对 §1 中每个允许的 `(w,t)`，逐个 `h` 检查 (1)，并在通过时再恢复 (2) 并检查

\[
10^5\le N_0<10^6.
\]

结果为：

| `w` | `t` | divisor-congruence hits |
|---:|---:|---:|
| `1` | `1` | `0` |
| `1` | `2` | `0` |
| `1` | `3` | `0` |
| `1` | `4` | `0` |
| `1` | `5` | `0` |
| `2` | `3` | `0` |
| `3` | `1` | `0` |
| `3` | `2` | `0` |
| `3` | `3` | `0` |
| `3` | `4` | `0` |
| `3` | `5` | `0` |
| `4` | `1` | `0` |

因此

\[
\boxed{
\text{total divisor-congruence hits}=0.
}
\tag{3}
\]

注意这里甚至没有使用：

- `z`；
- `gcd(a_1,b_1)=1`；
- `K>0`；
- partial-data rational-square sieve；
- `boundary-prime-sieve.md` 的 mod `3/7/11` 条件。

也就是说，一个更宽的 necessary-condition 超集已经为空，所以完整 exact-lift boundary 必然为空。

---

## 4. 证书完备性

完整性来自三条已经证明的 reduction：

1. positive residual theorem 保证 `ell=5` 时只有 `t=1,...,5`；
2. 2-adic boundary theorem 对 `w=2,4` 删除其余 residual；
3. odd-prime supply theorem 保证任何候选的 `h` 必在脚本枚举的有限 supply 中。

对固定 `(h,t)`，式

\[
b_3=a_th=N_0 10^5-t
\]

又唯一决定 `N_0`。因此没有遗漏任何连续变量或 exponent lattice。

于是严格得到

\[
\boxed{
 d=2,\ r=s=1,\ k=g=6,\ \ell=5
\text{ 为空。}
}
\tag{4}

---

## 5. 对 `k=6` 剩余部分的意义

这还没有关闭整个 `k=g=6` diagonal，因为仍需处理

\[
\boxed{\ell\ge6.}
\]

但 `ell<=4` 已由 positive residual theorem 全局排除，`ell=5` 又由本文证书排除。因此 `k=6` 现在可以无条件进入

\[
\boxed{\ell\ge k=6.}
\]

并且 `ell=6` 时 residual 只有

\[
\boxed{t\in\{6,7,\ldots,50\}.}
\]

下一步应把同一个 decimal-supply reduction 推到 `ell=k`：对每个 `t=6,...,50`，先剥离其 `2/5` 部分，再用有限 `h` supply 检查

\[
\frac{10^k}{a_t}\mid h+\widehat t.
\]

这有可能在不调用 rational-square sieve 的情况下继续关闭 `k=6` 的下一层 tail shell。
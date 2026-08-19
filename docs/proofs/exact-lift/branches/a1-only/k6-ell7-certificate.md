# A1 minimal diagonal `k=g=6, ell=7` residual-shell certificate

> 日期：2026-08-19。
> 本文继续关闭 `k=g=6` 的下一条 tail shell：
> \[
> \boxed{d=2,\quad r=s=1,\quad k=g=6,\quad \ell=7.}
> \]

结论：

\[
\boxed{\text{该 shell 为空。}}
\]

验证脚本：

```bash
uv run python scripts/exact-lift/a1-only/check_a1_top_diag_k6_ell7.py
```

状态：**regular/deep-2 分裂后的有限 divisor-congruence 证书。**

---

## 1. residual 窗

positive residual theorem 给出

\[
5.09\,10^{\ell-k}<t<50.45\,10^{\ell-k}.
\]

当前 `ell-k=1`，所以

\[
50.9<t<504.5.
\]

因此

\[
\boxed{t\in\{51,52,\ldots,504\}.}
\tag{1}
\]

共 `454` 个 residual。

---

## 2. regular 与 deep residual 的精确分裂

`residual-shell-supply.md` 的 regular 条件是

\[
v_2(t)<7,
\qquad
v_5(t)<7.
\]

在区间 (1) 中，`5^7=78125` 已远大于上界，所以没有 deep-5 residual。

满足 `v_2(t)>=7` 的只有

\[
\boxed{t\in\{128,256,384\}.}
\tag{2}
\]

因此：

- regular residual：其余 `451` 个；
- deep-2 residual：恰好 `128,256,384` 三个。

---

## 3. 451 个 regular residual 全部零命中

对 regular `t`，令

\[
a_t=2^{v_2(t)}5^{v_5(t)},
\qquad
\widehat t=t/a_t.
\]

任何候选必须满足

\[
b_3=a_t h,
\]

以及

\[
\boxed{
\frac{10^7}{a_t}\mid h+\widehat t.
}
\tag{3}
\]

其中 `h` 属于 `k=6` 的完整 odd-prime supply：

| `w` | `#h` |
|---:|---:|
| `1` | `64` |
| `2` | `32` |
| `3` | `2` |
| `4` | `8` |

脚本枚举全部 regular `(w,t,h)`，再由

\[
N_0=\frac{a_t(h+\widehat t)}{10^7}
\]

恢复 prefix integer 并检查

\[
10^5\le N_0<10^6.
\]

结果：

\[
\boxed{\text{regular hits}=0.}
\tag{4}
\]

---

## 4. 三个 deep-2 residual 也全部零命中

现在取

\[
t\in\{128,256,384\}.
\]

三者都满足

\[
v_5(t)=0.
\]

而

\[
b_3=N_0 10^7-t.
\]

第一项被 `5^7` 整除，第二项不被 `5` 整除，所以

\[
\boxed{v_5(b_3)=0.}
\tag{5}
\]

因此第三分母只能写成

\[
\boxed{b_3=h2^u,\qquad u\ge0,}
\tag{6}
\]

其中 `h` 仍来自同一个有限 odd-prime supply。

当前

\[
m_3=k+\ell=13,
\]

所以

\[
10^{12}\le b_3<10^{13}.
\]

对固定 `h`，满足

\[
10^{12}\le h2^u<10^{13}
\]

的整数 `u` 只有有限几个。脚本逐一检查

\[
10^7\mid h2^u+t
\]

并恢复

\[
N_0=\frac{h2^u+t}{10^7}.
\]

结果：

\[
\boxed{\text{deep-2 hits}=0.}
\tag{7}
\]

---

## 5. 结论

regular 与 deep-2 两部分共同覆盖 (1) 的全部 `454` 个 residual，因此

\[
\boxed{
 d=2,\ r=s=1,\ k=g=6,\ \ell=7
\text{ 为空。}
}
\tag{8}

注意本证书仍然没有使用 rational-square sieve；denominator prime supply、positive residual 和十进制恢复已经足够。

---

## 6. `k=6` 当前前沿

已有：

\[
\ell\le4\quad\text{全局排除},
\]

\[
\ell=5\quad\text{boundary certificate 排除},
\]

\[
\ell=6\quad\text{regular shell certificate 排除},
\]

\[
\ell=7\quad\text{本文排除}.
\]

所以 `k=g=6` 的剩余候选现在可以无条件假设

\[
\boxed{\ell\ge8.}
\]

下一层 `ell=8` 的 residual 窗为

\[
509<t<5045,
\]

即

\[
t\in\{510,\ldots,5044\}.
\]

同样可以分成 regular 与少量 deep-2/5 residual，再使用有限 `h` supply 推进。
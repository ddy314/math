# A1 minimal diagonal boundary decimal-supply reduction

> 日期：2026-08-19。依赖 `positive-tail-residual.md`、`boundary-residual-2adic.md` 与 minimal-diagonal odd-prime supply。
> 当前范围：
> \[
> k=g\ge6,\qquad \ell=k-1.
> \]

第一 boundary 已有

\[
b_3=N_0 10^{k-1}-t,
\qquad
t\in\{1,2,3,4,5\}.
\]

本文指出：一旦 `t` 固定，`b_3` 的全部 `2/5` 指数也被 `t` 固定，因此第三分母不再需要枚举 `(x,y)`。若

\[
a_t:=2^{v_2(t)}5^{v_5(t)},
\qquad
\widehat t:=\frac{t}{a_t},
\]

则

\[
\boxed{b_3=a_t h,}
\tag{1}
\]

其中 `h` 正是 denominator prime graph 给出的有限 odd-prime supply。并且必须满足十进制同余

\[
\boxed{
h+\widehat t
\equiv0
\pmod{10^{k-1}/a_t}.}
\tag{2}
\]

恢复公式为

\[
\boxed{
N_0
=\frac{a_t(h+\widehat t)}{10^{k-1}}.
}
\tag{3}
\]

所以对固定 `k,w,t`，第一 boundary 的候选数至多就是有限的 `#h`，无需扫描 `N_0` 的整个 k-digit 区间。

状态：**已严格完成。**

---

## 1. `b_3` 的 `2/5` 赋值等于 `t` 的赋值

当前

\[
b_3=N_0 10^{k-1}-t.
\]

因为

\[
k\ge6,
\qquad
1\le t\le5,
\]

有

\[
v_2(t),v_5(t)<k-1.
\]

而第一项 `N_0 10^{k-1}` 同时至少被

\[
2^{k-1},\qquad5^{k-1}
\]

整除。因此低赋值项由 `t` 唯一承担：

\[
\boxed{v_2(b_3)=v_2(t),}
\tag{4}
\]

\[
\boxed{v_5(b_3)=v_5(t).}
\tag{5}
\]

令

\[
a_t=2^{v_2(t)}5^{v_5(t)}.
\]

把 `b_3` 的 `2/5` 部分提出后，剩余部分恰与 `10` 互素，所以

\[
\boxed{b_3=a_t h,
\qquad \gcd(h,10)=1.}
\tag{6}
\]

这里的 `h` 与 odd-prime supply theorem 中的 `h` 完全相同。

---

## 2. `h` 仍只来自 `Q` 与 `b_1` 的 whole blocks

已有 theorem 给出

\[
\boxed{h=q\,s,}
\tag{7}
\]

其中

\[
q\mid Q,
\]

而 `s` 是 `b_1` 中所有 `1 mod4` 奇素 prime-power blocks 的 whole-block selector。

因此对固定 `k,w`，`h` 属于一个显式有限集合

\[
\boxed{\mathcal H_{k,w}.}
\tag{8}
\]

这个集合只由

\[
b_1=10^{2k+1}-w,
\qquad
Q=10b_1+1
\]

的因子分解决定，与 `N_0`、`z`、第三分子本身无关。

---

## 3. residual 直接变成 `h` 的十进制同余

把

\[
t=a_t\widehat t,
\qquad \gcd(\widehat t,10)=1
\]

和 (6) 代回

\[
b_3=N_0 10^{k-1}-t:
\]

\[
a_t h
=N_0 10^{k-1}-a_t\widehat t.
\]

于是

\[
a_t(h+\widehat t)
=N_0 10^{k-1}.
\]

由于 `a_t|10^{k-1}`，得到

\[
\boxed{
\frac{10^{k-1}}{a_t}
\mid h+\widehat t.}
\tag{9}
\]

也就是主同余 (2)。

同时 `N_0` 被唯一恢复为

\[
\boxed{
N_0
=\frac{a_t(h+\widehat t)}{10^{k-1}}.}
\tag{10}
\]

再检查

\[
10^{k-1}\le N_0<10^k
\]

即可。

因此第一 boundary 的搜索方向应从

\[
N_0\text{ 的 }9\cdot10^{k-1}\text{ 个整数}
\]

彻底反转成

\[
\boxed{
h\in\mathcal H_{k,w}}
\]

的有限 supply 枚举。

---

## 4. 五个 residual 的具体同余

分别计算 `a_t,hat t`：

| `t` | `a_t` | `hat t` | 必要同余 |
|---:|---:|---:|---|
| `1` | `1` | `1` | `h+1 ≡ 0 (mod 10^{k-1})` |
| `2` | `2` | `1` | `h+1 ≡ 0 (mod 10^{k-1}/2)` |
| `3` | `1` | `3` | `h+3 ≡ 0 (mod 10^{k-1})` |
| `4` | `4` | `1` | `h+1 ≡ 0 (mod 10^{k-1}/4)` |
| `5` | `5` | `1` | `h+1 ≡ 0 (mod 10^{k-1}/5)` |

结合二进 boundary collapse：

### `w=2`

只有

\[
t=3,
\]

所以只需检查

\[
\boxed{
h\equiv-3\pmod{10^{k-1}}.}
\tag{11}
\]

### `w=4`

只有

\[
t=1,
\]

所以只需检查

\[
\boxed{
h\equiv-1\pmod{10^{k-1}}.}
\tag{12}
\]

这两个 even-`w` 类型尤其简单：每个合法 `h` 直接给至多一个 `N_0`，不存在任何额外 `2/5` exponent 搜索。

---

## 5. 对固定 k 的证书复杂度

设

\[
H_{k,w}=\#\mathcal H_{k,w}.
\]

第一 boundary 的完整 supply 检查只需要至多

\[
5H_{k,w}
\]

个小同余测试；对 even-`w` 实际只需

\[
H_{k,w}
\]

个。

这和旧的 `(h,x,y)` tail 枚举相比已经发生本质变化：第一 boundary 现在是一个**有限 divisor-congruence certificate**。

下一步可以：

1. 对当前首个未关闭层 `k=6` 给出完整 boundary certificate；
2. 搜索能统一排除 (11)、(12) 的 divisor congruence 机制；
3. 对奇 `w` 把本同余与 `boundary-prime-sieve.md` 的 mod `3/11` forbidden classes 联用。
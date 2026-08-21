# A1 minimal diagonal: sharpened global `w=1` complement minimum

> 日期：2026-08-21。依赖 `deep-b1-sharp-mandatory-blocks`、`deep-w1-joint-complement-minimum`、`deep-q-side-proper-divisor` 与 `deep-complement-height`。当前范围为 surviving double-deep 2-high / 5-low master，`k=g>=32`。

旧的 joint argument 已证明

\[
M:=uv\ge621
\qquad(w=1).
\]

本文继续利用 `b_1=10^{2k+1}-1` 的 cyclotomic period，把旧的最弱 `r_3=1,u=27` 分支直接排除，并把 `r_3=0` 分支的额外 `3 mod4` prime 从旧的 `31` 提到 `71`。最终得到

\[
\boxed{w=1:\qquad M=uv\ge4473.}
\]

因此 denominator cap 从旧的

\[
D<17T^2
\]

进一步收缩为

\[
\boxed{
D<\frac{10001}{4473}T^2<2.236T^2<3T^2.}
\]

特别地，前一阶段研究的

\[
D/T^2\ge12,
\qquad(u,v)=(27,23)
\]

fixed-pair endpoint 实际为空；`w1-fixed-pair-descent.md` 中的推导只保留为该假设下的条件性 descent，不再属于当前 surviving frontier。

状态：**已严格完成。** 小素数 order 表由一个显式有限审计脚本核对；无界结论来自下面的分支证明。

---

## 1. 基本记号

写

\[
n:=2k+1,
\qquad
r_3:=v_3(n).
\]

对

\[
b_1=10^n-1
\]

LTE 给

\[
\boxed{v_3(b_1)=2+r_3.}
\tag{1}
\]

whole-block selector `s` 只能选取 `p=1 mod4` 的完整 prime-power blocks，因此

\[
u=b_1/s
\]

保留全部 `p=3 mod4` blocks。

Q-side complementary divisor

\[
v=Q/q
\]

满足

\[
\boxed{v\equiv3\pmod4.}
\tag{2}
\]

并且对 `w=1`：

\[
3,11\nmid Q,
\]

\[
7\mid Q\iff k\equiv0\pmod3,
\]

\[
19\mid Q\iff k\equiv4\pmod9.
\tag{3}
\]

下面按 `r_3` 分四类。

---

## 2. `r_3=1`：旧的 `u=27` 分支不可能发生

设

\[
r_3=1.
\]

则

\[
n=3m,
\qquad
m\text{ odd},
\qquad
3\nmid m.
\]

由 LTE：

\[
v_3(10^m-1)=2.
\]

因此

\[
\boxed{
A_m:=\frac{10^m-1}{9}
}
\tag{4}
\]

是奇整数且 `3` 不整除 `A_m`。

由于当前 `k>=32`，当然 `m>=2`。而

\[
10^2\equiv28\pmod{36},
\qquad
28\cdot10\equiv28\pmod{36},
\]

故所有 `m>=2` 都有

\[
10^m\equiv28\pmod{36}.
\]

于是

\[
10^m-1\equiv27\pmod{36},
\]

除以 9 得

\[
\boxed{A_m\equiv3\pmod4.}
\tag{5}
\]

如果 `u=27`，那么 `b_1` 中除了 `3^3` 之外不能再有任何 `p=3 mod4` prime-power block；特别地，`A_m` 的所有素因子都必须为 `1 mod4`。这会强迫

\[
A_m\equiv1\pmod4,
\]

与 (5) 矛盾。

所以

\[
\boxed{r_3=1\Longrightarrow u>27.}
\tag{6}
\]

所有小于 31 的 `3 mod4` primes

\[
7,11,19,23
\]

在 base 10 下的 order 分别为

\[
6,2,18,22,
\]

全为偶数，不能整除 odd exponent `n`。因此 (6) 中额外的 `3 mod4` block 至少来自 prime 31：

\[
\boxed{r_3=1\Longrightarrow u\ge27\cdot31=837.}
\tag{7}
\]

另一方面 `r_3=1` 等价于

\[
k\equiv1,7\pmod9.
\]

故 7 不整除 Q；19 的 Q-side period要求 `k=4 mod9`，也不可能。结合 `3,11 not|Q`：

\[
\boxed{v\ge23.}
\tag{8}
\]

所以

\[
\boxed{r_3=1:\qquad M=uv\ge837\cdot23=19251.}
\tag{9}
\]

这同时严格排除了旧的 `(u,v)=(27,23)` fixed pair。

---

## 3. `r_3=0`：额外 `3 mod4` prime 实际至少为 71

现在

\[
3\nmid n.
\]

由 (1)，3-primary block 正好为

\[
3^2=9\equiv1\pmod4.
\]

但

\[
b_1=10^n-1\equiv3\pmod4,
\]

所以还必须存在至少一个 `p=3 mod4` prime-power block以 odd parity贡献。

要找这个 block 的最小可能 prime，只需检查小于 71 的 `3 mod4` primes：

\[
7,11,19,23,31,43,47,59,67.
\]

它们的 `ord_p(10)` 为

\[
\boxed{
\begin{array}{c|ccccccccc}
p&7&11&19&23&31&43&47&59&67\\ \hline
\operatorname{ord}_p(10)&6&2&18&22&15&21&46&58&33
\end{array}}
\tag{10}
\]

其中：

- `6,2,18,22,46,58` 为偶数，不能整除 odd `n`；
- `15,21,33` 都被 3 整除，而当前 `3 not|n`，同样不能整除 `n`。

因此这些 prime 全部不可能整除 `10^n-1`。

下一个 `3 mod4` prime 是 71，并且

\[
\operatorname{ord}_{71}(10)=35,
\]

它是奇数且不被 3 整除，所以这里不能再用 `r_3=0` 的结构排除。

故安全得到

\[
\boxed{r_3=0\Longrightarrow u\ge9\cdot71=639.}
\tag{11}
\]

Q-side 保留统一最小值

\[
\boxed{v\ge7.}
\tag{12}
\]

于是

\[
\boxed{r_3=0:\qquad M=uv\ge639\cdot7=4473.}
\tag{13}
\]

这将成为四个分支中的全局最弱值。

---

## 4. `r_3>=3` 为奇数

若 `r_3` 为奇数且至少 3，则 (1) 给

\[
u\ge3^{2+r_3}\ge3^5=243.
\tag{14}
\]

又 `9|n`，所以

\[
k\equiv4\pmod9.
\]

因此 `k=1 mod3`，7 不整除 Q；而 19 正好是该 `mod9` 类允许的第一个 `3 mod4` Q-side prime。结合 `3,11 not|Q`：

\[
\boxed{v\ge19.}
\tag{15}
\]

故

\[
\boxed{r_3\ge3\text{ odd}:\qquad M\ge243\cdot19=4617.}
\tag{16}
\]

---

## 5. `r_3>=2` 为偶数

此时 3-primary exponent

\[
2+r_3
\]

为偶数，所以它本身是 `1 mod4`。仍需另一个 `3 mod4` block。

旧 mandatory-block argument 已给

\[
u\ge3^4\cdot31=2511.
\tag{17}
\]

同时 `9|n`，仍有

\[
k\equiv4\pmod9,
\]

故同上一节

\[
v\ge19.
\tag{18}
\]

于是

\[
\boxed{r_3\ge2\text{ even}:\qquad M\ge2511\cdot19=47709.}
\tag{19}
\]

---

## 6. 四分支合并

综上：

\[
\boxed{
M\ge
\begin{cases}
4473,&r_3=0,\\
19251,&r_3=1,\\
4617,&r_3\ge3\text{ odd},\\
47709,&r_3\ge2\text{ even}.
\end{cases}}
\tag{20}
\]

因此统一：

\[
\boxed{w=1:\qquad M=uv\ge4473.}
\tag{21}
\]

相比旧的 `621`，提高约 7.2 倍。

---

## 7. denominator cap 立即降到 `2.236T^2`

在 surviving double-deep 中 complement height 给

\[
\frac{MD}{T^2}<10001.
\]

结合 (21)：

\[
\boxed{
\frac D{T^2}<\frac{10001}{4473}
=2.2358596\ldots<2.236.}
\tag{22}
\]

所以可写成更简洁但稍弱的整数 cap：

\[
\boxed{D<3T^2.}
\tag{23}
\]

旧的 `D<17T^2` 从此可淘汰。

---

## 8. 对研究前沿的影响

1. `D/T^2>=12` 的整个旧 fixed-pair top endpoint 为空；因此 `w1-fixed-pair-descent.md` 不再是 surviving branch，只保留为被排除假设下的条件性推导记录。
2. `w=1` 的 denominator wedge 现在只有
   \[
   0<D/T^2<2.236.
   \]
3. 后续若继续做 period-coupled complement minima，真正需要攻击的是 `r_3=0` 的候选极值 `u>=639,v>=7`，以及它们能否同时接近最小值；任何进一步 joint incompatibility 都会直接继续降低 2.236 这个 cap。

---

## 9. 有限 order 审计

小素数表 (10) 与 `ord_71(10)=35` 可用：

```bash
uv run python scripts/exact-lift/a1-only/research-checks/deep-denominator/check_w1_global_complement_minimum.py
```

脚本通过逐个检查 `d|p-1` 来精确求最小 multiplicative order，不依赖概率分解或浮点计算；它只承担有限的小素数表核对。

# A1 minimal diagonal: deep-gap valuation normal form

> 日期：2026-08-19。依赖 `gap-denominator-normal-form.md` 与 minimal-diagonal valuation normal form。
> 当前统一范围可取 `k=g>=26`。

本文研究 reduced denominator 不整除 `10^k` 的 deep sector。

把归一化 gap 既约写成

\[
\boxed{
\Gamma_k:=10^k(N_0-\rho)
=\frac{\gamma}{2^A5^B},
}
\tag{1}
\]

其中

\[
A,B\ge0,
\qquad
\gcd(\gamma,2^A5^B)=1.
\]

central sector 恰为 `A=B=0`；deep sector 至少有一个正指数。

核心结论：`A,B` 与原来的 2/5 resonance thresholds 精确对齐，并带有平方赋值奇偶锁。特别地：

- `w=2,4` 时
  \[
  \boxed{A>0\Longrightarrow A\text{ 为奇数};}
  \]
- `w=1,3` 时，若 `n_2:=v_2(N)`，则
  \[
  A=1+n_2
  \]
  是二进 resonance；严格低侧只允许
  \[
  \boxed{A\equiv1+n_2\pmod2;}
  \]
- 若 `n_5:=v_5(N)`，则
  \[
  B=n_5
  \]
  是五进 resonance；当 `B>n_5` 时必须
  \[
  \boxed{B\equiv n_5\pmod2.}
  \]

状态：**已严格完成。**

---

## 1. deep excess 与原 reduced denominator

沿用 `gap-denominator-normal-form.md`：

\[
\rho=\frac nd,
\qquad d=2^a5^b,
\qquad\gcd(n,d)=1.
\]

乘以 `10^k` 后，约去共同的 `2/5` 因子，得到 (1)，其中

\[
\boxed{
A=(a-k)_+,
\qquad
B=(b-k)_+.}
\tag{2}
\]

所以

\[
\boxed{
\text{deep sector}
\iff A>0\text{ or }B>0.}
\tag{3}
\]

---

## 2. 把 rational square 写到 gap 坐标

minimal diagonal 的 rational square 为

\[
V^2=K-2\rho DN,
\qquad D=10^kQ.
\]

由

\[
\rho=N_0-\frac{\Gamma_k}{10^k}
\]

得到

\[
\boxed{
V^2
=J+2\Gamma_k QN,}
\tag{4}
\]

其中

\[
\boxed{
J:=K-2N_0 10^kQN\in\mathbf Z.}
\tag{5}
\]

这一步把 deep denominator 完全移到第二项 `2 Gamma_k QN`。

---

## 3. `J` 的 2/5 赋值仍由 `K` 精确承担

记

\[
e=v_2(w),
\qquad n_2=v_2(N),
\qquad n_5=v_5(N).
\]

已有

\[
v_2(K)=2e,
\qquad v_5(K)=0,
\]

而 `Q` 与 `10` 互素。

第二整数项满足

\[
v_2(2N_0 10^kQN)\ge1+k>2e
\]

（当前 `k>=26`，而 `2e<=4`），以及

\[
v_5(2N_0 10^kQN)\ge k>0.
\]

所以两项赋值严格不同：

\[
\boxed{v_2(J)=2e,}
\tag{6}
\]

\[
\boxed{v_5(J)=0.}
\tag{7}
\]

---

## 4. 二进 deep excess

若 `A>0`，则 `gamma` 为奇数。由 (1)、(4)：

\[
v_2(2\Gamma_kQN)
=1+n_2-A.
\tag{8}
\]

与 (6) 比较。

### low-side

若

\[
1+n_2-A<2e,
\]

等价于

\[
\boxed{A>1+n_2-2e,}
\tag{9}
\]

则第二项严格承担 `V^2` 的二进赋值：

\[
v_2(V^2)=1+n_2-A.
\]

有理平方的赋值必须为偶数，因此

\[
\boxed{
A\equiv1+n_2\pmod2.}
\tag{10}
\]

### resonance

两项赋值相等恰在

\[
\boxed{A=1+n_2-2e.}
\tag{11}
\]

### high-side

若

\[
A<1+n_2-2e,
\]

则 `J` 严格承担低赋值，`v_2(J)=2e` 本身已经是偶数，所以这一层没有额外 parity obstruction。

---

## 5. 六类型的二进 deep 表

### `w=2`

这里

\[
e=1,
\qquad n_2=0.
\]

resonance 值为

\[
1+0-2=-1,
\]

不属于 `A>0`。所以每个 2-deep 状态都在 strict low-side，并由 (10)：

\[
\boxed{A=1,3,5,\ldots.}
\tag{12}
\]

### `w=4`

这里

\[
e=2,
\qquad n_2=0,
\]

resonance 值为 `-3`，同样不在 deep sector。因此

\[
\boxed{A=1,3,5,\ldots.}
\tag{13}
\]

### `w=1,3`

这里 `e=0`，而已知

\[
n_2\in\{0,1\}.
\]

若 `n_2=0`：

\[
\boxed{A=1\text{ resonance},}
\]

strict low-side `A>=2` 中 (10) 只允许

\[
\boxed{A=3,5,7,\ldots.}
\tag{14}
\]

特别地 `A=2` 被直接排除。

若 `n_2=1`：

\[
A=1\text{ 在 high-side},
\]

\[
\boxed{A=2\text{ resonance},}
\]

而 `A>=3` 的 strict low-side 只允许

\[
\boxed{A=4,6,8,\ldots.}
\tag{15}
\]

特别地 `A=3,5,7,...` 全部排除。

---

## 6. 五进 deep excess

若 `B>0`，则 `gamma` 不被 `5` 整除。由 (4)：

\[
v_5(2\Gamma_kQN)
=n_5-B.
\tag{16}
\]

与 `v_5(J)=0` 比较。

### low-side

若

\[
\boxed{B>n_5,}
\tag{17}
\]

则第二项严格承担五进赋值：

\[
v_5(V^2)=n_5-B.
\]

故

\[
\boxed{B\equiv n_5\pmod2.}
\tag{18}
\]

### resonance

\[
\boxed{B=n_5}
\tag{19}
\]

恰为五进 resonance。

### high-side

若

\[
0<B<n_5,
\]

则整数项 `J` 承担低赋值 `0`，没有新的 parity obstruction。

---

## 7. 与旧 `(x,y)` resonance line 完全一致

若原 reduced denominator 在 2 侧 deep：

\[
a=k+A,
\qquad x=-a=-k-A.
\]

旧二进 threshold 为

\[
x_*=2e-1-k-n_2.
\]

所以

\[
\boxed{
x-x_*=-(A-(1+n_2-2e)).}
\tag{20}
\]

因此 (9)、(11) 与 high-side 三种情况正好就是

\[
x<x_*,\qquad x=x_*,\qquad x>x_*.
\]

五进同理：若 `b=k+B`，则

\[
y=-k-B,
\qquad y_*=-k-n_5,
\]

故

\[
\boxed{y-y_*=-(B-n_5).}
\tag{21}
\]

所以 deep-gap denominator normal form 并没有引入新的独立分类；它把旧 resonance geometry 精确翻译成了“归一化 gap 的 reduced denominator excess”。

---

## 8. 当前意义

central sector 已经变成固定 24 个整数 gap，并进一步缩到 30 个 surviving type-gap combinations。

本文则把 genuinely noninteger gap 的 deep sector 变成：

- 一个 2-adic excess `A`，带显式 resonance level 与 parity lattice；
- 一个 5-adic excess `B`，带显式 resonance level `n_5` 与 parity lattice；
- 归一化实窗
  \[
  15.09<\gamma/(2^A5^B)<39.003.
  \]

特别地 even-`w` 的全部 2-deep 状态只可能出现在奇数 `A` 层。

下一步 deep sector 应继续在这些 parity-compatible 层上加入 square-unit residue（2-adic unit mod 8、5-adic unit mod 5）以及 primitive cross-corridor caps；已经无需再把所有 `A,B` 当作无结构二维格点。
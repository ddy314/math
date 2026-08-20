# A1 minimal diagonal: complete central modular exhaustion

> 日期：2026-08-19。依赖 `central-supply-pell-normal-form.md`、`central-pell-local-squareclass.md`、`central-double-square-valuation-lock.md` 与原 contact square。
> 当前统一范围为
> \[
> d=2,\qquad r=s=1,\qquad k=g\ge26.
> \]

本文关闭 minimal diagonal 的整个 **central denominator sector**。

此前 central 已从 144 个 type-gap 组合压到 30 个，并把每个组合的全部无界 `k` 归约为一个与 `k` 无关的有限 `U` 窗。这里不再尝试逐个求 generalized Pell 基本解，而是把：

1. supply quadratic；
2. supply-Pell 判别式的 `2/5` local squareclass；
3. 原 rational-contact integer square；
4. `10^k` 在奇素数模下的有限周期；

直接组合成一个精确有限模覆盖。

最终结果：

\[
\boxed{\text{central denominator sector 在全部 }k\ge26\text{ 上为空}.}
\]

状态：**已严格完成；附带 C++ exact certificate。**

---

## 1. 输入：30 个 surviving central type-gap

central gap 为整数

\[
\Gamma=10^k(N_0-\rho).
\]

经过 `central-gap-2adic.md` 与 `central-gap-sign-collapse.md` 后，只剩：

\[
\begin{array}{c|l}
(z,w)&\Gamma\\ \hline
(1,1)&32,34,36,38\\
(1,3)&24,26,28,30,32,34,36,38\\
(3,1)&22,24,26,28,30,32,34,36,38\\
(1,2)&30,32,38\\
(3,2)&22,30,32,38\\
(1,4)&24,26
\end{array}
\tag{1}
\]

唯一 crossing `(3,1,22)` 还使用 `central-crossing-sharp.md` 的

\[
N_0/10^k<0.250261,
\qquad U\ge3,867,967.
\tag{2}
\]

---

## 2. 固定 `(z,w,Gamma)` 后的有限 `t` 坐标

定义

\[
c=2^{v_2(\Gamma)}5^{v_5(\Gamma)},
\qquad r=\Gamma/c,
\qquad C_0=w(10w-1),
\]

\[
L=10^k/c,
\qquad U_0=10c\Gamma(20w-1),
\qquad t=U-U_0>0.
\]

`central-supply-pell-normal-form.md` 给出 `k`-independent 的严格 `U` 窗

\[
c(C_0+1000\Gamma^2)
<U
<c(C_0/10+10000\Gamma^2)+1.
\tag{3}
\]

因此每个 type-gap 的 `t` 从一开始就是一个绝对有限整数区间。

同时

\[
B_U=-4C_0rt.
\tag{4}
\]

若 exact candidate 存在，则 supply quadratic 的判别式必须平方，所以 `B_U` 必须同时属于 `Q_2`、`Q_5` 的平方类。

进一步由 `central-double-square-valuation-lock.md`：

\[
\boxed{
v_2(N_0)=\frac{v_2(t)-v_2(C_0)}2,
\qquad
v_5(N_0)=\frac{v_5(t)}2.}
\tag{5}
\]

所以可把原 contact integer square 模 `2^12` 与 `5^6` 的全部 residue classes 反推回 `t`。

这一步不是抽样：

- 若 `N_0=0 mod 2^12` 的 class 不允许，则所有更深 `v_2(N_0)>=12` 同时被排除；
- `5^6` 同理。

因此 `(3)-(5)` 加上完整 2/5 unit square 条件给出一个**有限且完整**的 local-compatible `t` 集合。

30 个 type-gap 合计恰有

\[
\boxed{93,580,902}
\tag{6}
\]

个这样的 `t`。

注意这里故意没有删除 `A_U` 恰为平方的退化 family；因此本证书覆盖的集合比此前的 nonsquare-Pell 核心更大，结论更安全。

---

## 3. 对每个奇素数的 exact modular necessary condition

固定一个奇素数

\[
p\ne2,5.
\]

令

\[
T=10^k\pmod p,
\qquad L=T/c\pmod p.
\]

给定 `t` 后

\[
U=U_0+t
\]

固定。任何 exact candidate 都必须存在某个

\[
N_0\pmod p
\]

同时满足下面两个条件。

### 3.1 supply quadratic

\[
\boxed{
C_0N_0^2
-U L N_0
+1000c^4r^2L^2
+rU
-10c^2r^2(20w-1)
\equiv0\pmod p.}
\tag{7}
\]

### 3.2 原 contact square

用

\[
b_1=10T^2-w,
\qquad a_2=10T^2-z,
\]

\[
Q=100T^2-10w+1,
\]

\[
a_1=100T^3+igl(10(5-z-w)+1\bigr)T+N_0-1,
\]

\[
C=10T^2a_1+a_2,
\]

\[
\mathcal N=a_1^2+(a_2b_1)^2,
\]

\[
D=TQ,
\qquad K=b_1^2C^2-D^2\mathcal N,
\]

以及 central

\[
B=N_0T-\Gamma,
\]

原 rational-contact 必要平方就是

\[
\boxed{
R=K-2BQ\mathcal N
\text{ 必须是模 }p\text{ 的平方剩余}.}
\tag{8}
\]

定义

\[
S_p(t)
:=
\left\{
k\bmod \operatorname{ord}_p(10):
\exists N_0\bmod p\text{ 同时满足 (7),(8)}
\right\}.
\tag{9}
\]

任何 exact candidate 都必须满足

\[
k\bmod\operatorname{ord}_p(10)\in S_p(t)
\]

对所有所选素数同时成立。

---

## 4. period-420 公共覆盖

取公共素数集

\[
\begin{aligned}
\mathcal P_0=\{&3,7,11,13,29,31,37,41,43,61,71,101,127,211,239,241,\\
&271,281,421,1933,2161,2689,3541,4649\}.
\end{aligned}
\tag{10}
\]

这些素数都满足

\[
\boxed{\operatorname{ord}_p(10)\mid420.}
\tag{11}
\]

所以对每个固定 `t`，把所有 `S_p(t)` 拉回 `k mod 420` 后直接求交即可。

对 (6) 的 93,580,902 个完整 local-compatible `t` 做 exact integer enumeration 后，只剩

\[
\boxed{33}
\tag{12}
\]

个 `(t,k mod420)` 状态。

只有下列 type-gap 在公共覆盖后仍非空：

\[
\begin{array}{c|r}
(z,w,\Gamma)&\text{common-period survivors}\\ \hline
(1,1,32)&11\\
(1,1,36)&1\\
(1,3,24)&3\\
(1,3,32)&2\\
(1,3,36)&1\\
(3,1,24)&2\\
(3,1,28)&4\\
(3,1,32)&7\\
(3,1,38)&1\\
(1,2,30)&1
\end{array}
\tag{13}
\]

其余 20 个 type-gap 已经在 `P_0` 上直接归零。

---

## 5. 最后的 33 个状态也全部 CRT 不兼容

对 (12) 中的状态，再使用有限补充集

\[
\boxed{
\mathcal P_1
=
\{17,19,73,89,113,137,251,337,1009,4201\}.}
\tag{14}
\]

这里不要求 order 整除 420。

若当前状态已有

\[
k\equiv a\pmod{420},
\]

而某个 `p in P_1` 允许的 classes 为

\[
k\equiv b\pmod{o_p},
\qquad o_p=\operatorname{ord}_p(10),
\]

两者能同时成立当且仅当

\[
\boxed{
a\equiv b\pmod{\gcd(420,o_p)}}.
\tag{15}
\]

附带证书逐个检查 (12) 的 33 个状态。每一个状态至少被 `P_1` 中一个素数违反 (15)，最终留下

\[
\boxed0
\tag{16}
\]

个状态。

---

## 6. 结论

所有步骤只使用：

- `k`-independent 的严格有限 `U/t` 窗；
- exact `2/5` local-square 与 contact-square residues；
- exact integer congruence；
- `10^k mod p` 的有限乘法阶；
- CRT compatibility。

没有使用概率分解，没有截断 `k`，也没有假设 generalized Pell primitive-divisor theorem 可直接套用。

因此得到：

\[
\boxed{
\forall k=g\ge26,
\qquad
\text{minimal diagonal central denominator sector is empty}.}
\tag{17}
\]

结合 `k<=30` 的 fixed-layer certificates，当前 minimal diagonal 的任何剩余候选都必须同时满足

\[
\boxed{k\ge31}
\]

并位于

\[
\boxed{\text{deep denominator sector}.}
\]

所以后续统一证明已经无需再处理 central Pell families；全部精力可以转向 deep denominator lattice。

---

## 7. 可复核证书

源文件：

`../../../../../scripts/exact-lift/a1-only/check_a1_central_modular_exhaustion.cpp`

典型运行：

```bash
g++ -O3 -std=c++17 check_a1_central_modular_exhaustion.cpp -o /tmp/a1-central
/tmp/a1-central
```

证书最终断言：

```text
TOTAL local=93580902 common=33 final=0
CERTIFICATE OK: all k>=26 central denominator states are empty.
```

枚举量较大，但每一步都是固定宽度整数模运算；分块或并行运行不会改变证明内容。
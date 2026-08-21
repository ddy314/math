# `A_1`-only 分支

这是 `A_1` 分支的规范状态入口。当前 A1 整体仍为 **待证**；本文档中的“关闭”只指 minimal diagonal 子问题。

## 当前严格前沿

fixed-layer certificates 已关闭

\[
\boxed{1\le k=g\le31.}
\]

central denominator 已统一关闭

\[
\boxed{k=g\ge26\Longrightarrow\text{central empty}.}
\]

因此任何尚存 minimal-diagonal candidate 必须满足

\[
\boxed{k=g\ge32}
\qquad\text{且}\qquad
\boxed{\text{deep denominator}.}
\]

全局 positive/contact window：

\[
\Gamma:=10^k(N_0-\rho),
\qquad
\boxed{15.09<\Gamma<39.003},
\]

并且 `rho<N_0`、saturated 为空、`ell>=k-1`。

原 contact-square leading sign 已进一步给 typewise continuous windows：

\[
\begin{array}{c|c}
(z,w)&\Gamma\\ \hline
(1,1)&30.0399<\Gamma<33.003\\
(1,2)&26.0399<\Gamma<29.003\\
(1,3)&22.0399<\Gamma<25.003\\
(1,4)&18.0399<\Gamma<21.003\\
(3,1)&21.8199<\Gamma<39.003\\
(3,2)&19.8199<\Gamma<37.003
\end{array}
\]

四个 `z=1` 类型的 deep gap 已被压到宽度不足 3。

---

## 推荐阅读顺序

细粒度 continuation 已归并为 [`boundary-and-tail-ledger.md`](boundary-and-tail-ledger.md)、[`central-denominator-ledger.md`](central-denominator-ledger.md)、[`deep-denominator-ledger.md`](deep-denominator-ledger.md) 与 [`finite-layer-certificates-ledger.md`](finite-layer-certificates-ledger.md)。下列链接直接落到各原来源锚点；账本中的局部“关闭”不改变 A1 整体仍为待证。

1. [`core.md`](core.md)、[`rational-contact.md`](rational-contact.md)：A1 rational contact / denominator funnel / corridor。
2. [`top-layer.md`](top-layer.md)、[`diagonal.md`](diagonal.md)：minimal diagonal 与 odd-prime supply。
3. [`positive-tail-residual.md`](boundary-and-tail-ledger.md#source-positive-tail-residual)、[`sharp-positive-tail-window.md`](boundary-and-tail-ledger.md#source-sharp-positive-tail-window)：正号与窄 gap。
4. [`uniform-2adic-prefix.md`](boundary-and-tail-ledger.md#source-uniform-2adic-prefix)：
   \[
   \boxed{\underline x_*(k)=-k-2.}
   \]
5. [`gap-denominator-normal-form.md`](boundary-and-tail-ledger.md#source-gap-denominator-normal-form)：central / deep 分裂。
6. [`central-modular-exhaustion.md`](central-denominator-ledger.md#source-central-modular-exhaustion)：central all-`k` 关闭。
7. [`deep-complement-height.md`](deep-denominator-ledger.md#source-deep-complement-height)、[`deep-first-complement-remainder.md`](deep-denominator-ledger.md#source-deep-first-complement-remainder)、[`deep-balanced-collapse.md`](deep-denominator-ledger.md#source-deep-balanced-collapse)。
8. [`deep-universal-factorization.md`](deep-denominator-ledger.md#source-deep-universal-factorization)、[`deep-four-factor-frame.md`](deep-denominator-ledger.md#source-deep-four-factor-frame)：single/double deep 公共 skeleton。
9. [`deep-double-5high-collapse.md`](deep-denominator-ledger.md#source-deep-double-5high-collapse)、[`deep-ll-modular-exhaustion.md`](deep-denominator-ledger.md#source-deep-ll-modular-exhaustion)：double-deep 旧 LL/LH 分支关闭。
10. [`deep-double-2high-master.md`](deep-denominator-ledger.md#source-deep-double-2high-master)：当前 double-deep 唯一 master branch。
11. [`deep-2high-mod8-lock.md`](deep-denominator-ledger.md#source-deep-2high-mod8-lock)、[`deep-2high-mod5-lock.md`](deep-denominator-ledger.md#source-deep-2high-mod5-lock)：真正独立的 2/5 local locks。
12. [`deep-hl-one-exponent-divisor-family.md`](deep-denominator-ledger.md#source-deep-hl-one-exponent-divisor-family)、[`deep-hl-local-signature-count.md`](deep-denominator-ledger.md#source-deep-hl-local-signature-count)：moderate 部分降成 finite coefficients + 单指数 `d`。
13. [`deep-contact-q-square-blocks.md`](deep-denominator-ledger.md#source-deep-contact-q-square-blocks)、[`deep-contact-q-resultant-loss.md`](deep-denominator-ledger.md#source-deep-contact-q-resultant-loss)、[`deep-hl-q-superlinear.md`](deep-denominator-ledger.md#source-deep-hl-q-superlinear)：原 rational-contact square 的独立 Q-side block lifting。
14. [`deep-hl-hensel-dependency-audit.md`](deep-denominator-ledger.md#source-deep-hl-hensel-dependency-audit)、[`deep-root-factor-splitting.md`](deep-denominator-ledger.md#source-deep-root-factor-splitting)：依赖审计，防止重复计算同一 obstruction。
15. [`deep-single5-first-remainder-height.md`](deep-denominator-ledger.md#source-deep-single5-first-remainder-height)：single-5 strict-low 的当前高度压缩。
16. [`k31-uniform-certificate.md`](finite-layer-certificates-ledger.md#source-k31-uniform-certificate)：最新 fixed-layer 保险证书。
17. [`w1-fixed-pair-descent.md`](w1-fixed-pair-descent.md)：`w=1,D/T^2>=12` fixed pair 的参数化、局部锁与高度降维。

---

## Central denominator：已完全关闭

central modular certificate 对全部 93,580,902 个 local-compatible finite states 做 exact periodic cover：

\[
93,580,902
\longrightarrow33\text{ 个 }(t,k\bmod420)
\longrightarrow\boxed0.
\]

所以 central Pell / primitive-divisor 已退出当前前沿。

---

# Deep universal skeleton

写 reduced gap

\[
\Gamma=\frac\gamma D,
\qquad D=2^A5^B,
\]

并把 non-deep side 的 numerator powers 记成

\[
\lambda=2^{\lambda_2}5^{\lambda_5}.
\]

则

\[
\boxed{DTN_0-\gamma=h\lambda},
\qquad T=10^k,
\]

其中

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1,
\]

而 `s` 只能按 `p=1 mod4` complete prime-power blocks 选择。

## complement height

令

\[
M=Qb_1/h,
\qquad
\mu=MD/(\lambda T^2).
\]

则

\[
1000<\mu<10001,
\]

\[
0<\frac{MDN_0}{\lambda T^3}-1000<\frac{390100}{T^2}.
\]

first remainder：

\[
MDN_0=1000\lambda T^3+R_1,
\]

\[
\boxed{14300\lambda T<R_1<390100\lambda T.}
\]

fully-balanced deep 已全部排除。

## universal factor / four-factor

对任意 single / double deep 存在正整数 `t,a,b`：

\[
\boxed{10\gamma T-wDN_0=sa},
\]

\[
\boxed{100\gamma T-(10w-1)DN_0=qb},
\]

\[
\boxed{ab=t}.
\]

写

\[
\bar q=Q/q,
\qquad
\bar s=b_1/s,
\]

则

\[
qb-10sa=DN_0,
\]

\[
\bar s b-\bar q a=10\lambda T.
\]

同时

\[
S^2=100\lambda^2T^2+4tM,
\]

\[
S-10\lambda T=2a\bar q,
\qquad
S+10\lambda T=2b\bar s.
\]

---

# Double-deep：只剩统一 2-high / 5-low master branch

此前已严格关闭：

- high-high（balanced collapse）；
- moderate LH（全部 5-high）；
- 5-extreme；
- moderate LL 六类型。

LL exact modular exhaustion 共处理

\[
\boxed{522,664,766}
\]

个 local-compatible fixed Pell families，最终 survivors 为

\[
\boxed0.
\]

因此所有尚存 double-deep 都是

\[
\boxed{2\text{-high}/5\text{-low}.}
\]

## master coordinates

定义

\[
\boxed{\eta:=A-(2k+3)},
\qquad
A=2k+3+\eta.
\]

- `eta<=0`：旧 moderate HL；
- `eta>0`：旧 2-extreme `E_2`。

再令

\[
Y=B+\nu_5<k+1,
\qquad
c=k+1+\eta+\nu_2,
\qquad
d=k+1-Y.
\]

则

\[
v_2(t)=2k+3,
\qquad
v_5(t)=2Y,
\]

所以

\[
t=2^{2k+3}5^{2Y}r_{10},
\qquad (r_{10},10)=1.
\]

令

\[
\xi=t/D,
\]

则

\[
\boxed{\xi=2^{-\eta}5^{B+2\nu_5}r_{10}.}
\]

contact sign 给 typewise `xi` 下界；旧 global upper 仍为 `15,214,000`。

factor quotients：

\[
a=2^{k+1}5^Y\alpha,
\qquad
b=2^{k+2}5^Y\beta,
\]

\[
\alpha\beta=r_{10},
\qquad
\gcd(\alpha,\beta)=1.
\]

stripped master equations：

\[
\boxed{2\beta u-\alpha v=5^d},
\]

\[
\boxed{\beta q-5\alpha s=2^c n_0},
\]

以及 adjugates

\[
2^{c+1}n_0u-5^dq=\alpha,
\]

\[
2^cn_0v-5^{d+1}s=\beta.
\]

## master local locks

2-adic：

\[
\boxed{r_{10}\equiv-5^{B+1}QN_2\pmod8.}
\]

特别是 `w=2,4`：

\[
B\text{ even}\Rightarrow r_{10}\equiv3\pmod8,
\]

\[
B\text{ odd}\Rightarrow r_{10}\equiv7\pmod8.
\]

5-adic contact Legendre：

\[
\boxed{
\left(\frac{wr_{10}N_5}{5}\right)=(-1)^A.}
\]

这两条是安全独立 local inputs。

## dependency audit

以下两项**不能**再当独立筛重复使用：

1. denominator-free root square：它在 four-factor frame 中自动因式分裂；
2. old growing-depth HL Hensel lock：其 exact valuation 已由 stripped four-factor identities 自动推出。

纯 5-adic contact-square lifting也只有 mod-5 Legendre class；高阶 Hensel lift自动存在。

## `w=1` joint top endpoint：`D/T^2>=12` 锁成固定 pair

令

\[
\delta:=D/T^2,
\qquad
M:=uv.
\]

`deep-w1-joint-complement-minimum` 已证明

\[
\boxed{M\ge621.}
\]

这里还能把最小值分支继续细化。写

\[
r_3:=v_3(2k+1).
\]

- `r_3=0` 时，已有 `u>=279`,`v>=7`，所以 `M>=1953`；
- `r_3>=2` 时，已有下界远大于 `837`；
- 只有 `r_3=1` 能达到全局 minimum，此时 `u>=27`。又 `k=1 mod3`，所以 `7` 不整除 `Q`；而 `19|Q` 会强迫 `k=4 mod9`，与 `r_3=1` 的 `k=1 or 7 mod9` 冲突。结合 universal `3,11 not|Q`，得到
  \[
  v\ge23.
  \]

在 `r_3=1` 分支，如果 `v>23`，则下一个可能的 `3 mod4` complement 至少为 `31`，从而

\[
M\ge27\cdot31=837.
\]

如果 `u>27`，由于 `v_3(b_1)=3` 已固定，而所有小于 `31`、不同于 `3` 的素数都不能在 odd exponent 的 `10^{2k+1}-1` 中提供新的 whole block，额外 complement factor 也至少为 `31`，同样有 `M>837`。

因此

\[
\boxed{M<837\Longrightarrow(u,v)=(27,23).}
\tag{A1-E1}
\]

另一方面 complement height 给

\[
M\delta<10001.
\]

所以只要

\[
\boxed{\delta\ge12,}
\]

就有

\[
M<10001/12<837,
\]

于是

\[
\boxed{
D/T^2\ge12
\Longrightarrow
(u,v,M)=(27,23,621).}
\tag{A1-E2}
\]

这把 `w=1` 的全局 cap

\[
D/T^2<10001/621<16.11
\]

中的顶端条带 `[12,16.11)` 变成 fixed-coefficient branch。

周期条件也完全固定。`u=27` 强迫

\[
v_3(2k+1)=1
\Longleftrightarrow
k\equiv1,7\pmod9.
\]

而 `v=23` 要求 `23|Q`。由 `ord_23(10)=22` 且 `10^{18}=9 mod23`：

\[
23|Q
\Longleftrightarrow
2k+2\equiv18\pmod{22}
\Longleftrightarrow
k\equiv8\pmod{11}.
\]

CRT 因而给出

\[
\boxed{k\equiv19\text{ or }52\pmod{99}.}
\tag{A1-E3}
\]

在这两个类上，master equations 降成

\[
\boxed{54\beta-23\alpha=5^d,}
\]

以及用 `s=b_1/27` 化简后的

\[
\boxed{5^{d+1}s+\beta=23\cdot2^c n_0.}
\tag{A1-E4}
\]

状态：**已严格完成（仅关闭为 fixed pair，不排除该 fixed pair 本身）。** 对应短周期核对脚本：

`research-checks/deep-denominator/check_w1_joint_endpoint_periods.py`。

进一步 descent 见 [`w1-fixed-pair-descent.md`](w1-fixed-pair-descent.md)。其中已经严格推出

\[
\boxed{Y<0.139k+7,\qquad d>0.861k-6,\qquad\eta>4.321k-16,}
\]

以及

\[
\boxed{v_2(m)=2,\quad r_{10}\equiv1\pmod8,\quad\left(\frac{r_{10}}5\right)=-1.}
\]

---

# Moderate 2-high：finite signatures + one exponent

moderate 即 `eta<=0`，此时 `xi=r` 为有限整数。

contact-sign sharpened windows：

\[
\begin{array}{c|c}
(z,w)&r\\ \hline
(1,1)&973440\le r\le10885221\\
(1,2)&734410\le r\le8400003\\
(1,3)&529000\le r\le6236387\\
(1,4)&357210\le r\le4394372\\
(3,1)&519840\le r\le15204352\\
(3,2)&428490\le r\le13677244
\end{array}
\]

全部独立 local filters + odd-`w` whole-block orientation 后，`5|r` 的初始

\[
11,051,041
\]

个整数只剩

\[
\boxed{3,019,293}
\]

个 safe `r` signatures：

\[
\begin{array}{c|r}
(1,1)&579692\\
(1,2)&383278\\
(1,3)&328609\\
(1,4)&201854\\
(3,1)&863426\\
(3,2)&662434
\end{array}
\]

对固定 finite `(w,Y,alpha,beta)`，令

\[
d=k+1-Y,
\]

则整个 unbounded complement problem 已化成

\[
\boxed{
\begin{aligned}
&u\mid10^{2d+2Y-1}-w,\\
&v\mid10^{2d+2Y}-(10w-1),\\
&2\beta u-\alpha v=5^d.
\end{aligned}}
\]

即 finite coefficients + **单一指数 `d`**。

## strong scale separation

moderate branch 中：

\[
\boxed{q>10,900,000T},
\qquad
\boxed{v<10^{-5}T},
\]

\[
\boxed{u<5\cdot10^{-6}T},
\qquad
\boxed{s>1.8\cdot10^6T}.
\]

所以 complementary divisors `u,v=o(T)`，selected supply `q,s>>T`。

---

# 原 contact square 的独立 Q-side block lifting

把 contact square 乘 gap denominator 后，存在整数 `Z`：

\[
\boxed{
(Db_1C-Z)(Db_1C+Z)
=D N q^2v(DT^2v+2s).}
\]

令

\[
L_\pm=Db_1C\pm Z.
\]

若 `p^e||q` 且 `p\nmid C`，则

\[
\boxed{p^{2e}\mid L_-\text{ or }L_+.}
\]

一般 exceptional loss 由

\[
g=\gcd(q,C)
\]

控制，并且

\[
10C\equiv E_C\pmod Q,
\qquad
\boxed{g=\gcd(q,E_C)<1599T.}
\]

因此 guaranteed lifted product 是

\[
\boxed{q^2/g}.
\]

moderate 中 sharp q bound 又给

\[
\boxed{q/g>6800\cdot2^{k-32}.}
\]

所以至少一个 selected Q-primary block 必然发生 strict exponent amplification；contact exceptional part 不可能吞掉全部 `q`。

对 `w=1,4`，mandatory `3|u` 再与 contact square 联立得到

\[
N_0\not\equiv2\pmod3
\Longrightarrow
r_{10}\equiv-(-1)^{\eta+B}(N_0+1)\pmod3,
\]

特别地

\[
3\mid r_{10}\Longrightarrow N_0\equiv2\pmod3.
\]

---

# Single-deep

single-deep 尚未关闭，但共享 universal factor / four-factor / first remainder。

strict single-5 (`A=0,B>v_5(N)`) 已有：

\[
0\le\lambda_2\le2k,
\]

\[
\boxed{B+v_5(N_0)<2.3k+8.}
\]

所以 strict single-5 的任意深 5-excess 已被压成线性高度 strip。5-adic resonance/high 与 single-2 仍待继续处理。

---

# Fixed-layer 保险线

完整 exact certificates：

\[
\boxed{k=1,2,\ldots,31.}
\]

最新 `k=31`：

\[
(|H_1|,|H_2|,|H_3|,|H_4|)=(16384,96,16,96),
\]

finite box

\[
(x,y)\in[-321,284]\times[-120,58],
\]

exact decade states

\[
\boxed{6,146,672},
\]

旧宽 gap window 下仍 `0` hits。首个未关闭 fixed layer：

\[
\boxed{k=32.}
\]

---

# 下一步

minimal diagonal 当前真正的统一核心：

1. **moderate 2-high one-exponent families**：利用 `u,v<<T`、mandatory/cyclotomic blocks 与 contact forced Q-side lift，关闭
   \[
   2\beta u-\alpha v=5^d.
   \]
2. **eta>0 pure-2 denominator side**：`w=1,D/T^2>=12` 已进一步压到 `Y<0.139k+7`、`eta>4.321k-16` 与超深同余 `m=-5^dR mod 2^c`；下一步直接攻击该 2-adic 近整，或把 typewise contact window 再压入 `x=m/5^d`。
3. **single-deep**：优先 single-5 resonance/high 与 single-2。
4. fixed `k>=32` 仅作为保险线推进，不替代统一证明。

`d=1,0,-1` 等 A1 其他 top-layer 无界核心仍待处理。

## 主要可复核脚本

位于 [`scripts/exact-lift/a1-only/`](../../../../../scripts/exact-lift/a1-only/)：

- `check_a1_central_modular_exhaustion.cpp`：central all-`k`；
- `check_a1_deep_ll_modular_exhaustion.cpp`：moderate LL all-`k`；
- `check_a1_deep_hl_local_signatures.cpp`：moderate 2-high local `r` signatures；
- `check_a1_top_diag_uniform_layer_31.py`：fixed `k=31`；
- `check_a1_top_diag_uniform_layers*.py`：早期 fixed layers；
- `research-checks/deep-denominator/check_w1_joint_endpoint_periods.py`：`w=1` joint endpoint 的短周期核对；
- `research-checks/deep-denominator/check_w1_fixed_pair_local_locks.py`：fixed-pair 参数化与 mod-8/mod-5 核对；
- `research-checks/deep-denominator/check_w1_fixed_pair_height_collapse.py`：`Y<0.139k+7` 高度压缩常数核对；
- 以及 near-integer / unit-square / factorization 审计脚本。

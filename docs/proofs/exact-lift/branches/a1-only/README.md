# `A_1`-only 分支

这是 `A_1` 分支的唯一规范编辑入口。内容按“统一框架 → moving-prefix/top layer → minimal diagonal”组织。

## 阅读顺序

1. [`core.md`](core.md)：A1 主框架与审计边界。
2. [`rational-contact.md`](rational-contact.md)：rational-contact、integer-gap、universal denominator funnel、resonance、cross-corridor。
3. [`top-layer.md`](top-layer.md)：moving-prefix 四层压缩、`d=2` endpoint kernel、positive excess 与 minimal-surplus 分裂。
4. [`diagonal.md`](diagonal.md)：`k=g` minimal diagonal、valuation normal form、odd-prime supply、早期有限证书。
5. [`near-integer-tail.md`](near-integer-tail.md)：把 `rho=b_3/10^ell` 压到明确整数 `N_0=j-10^k+1` 的 `O(10^-k)` 邻域。
6. [`positive-tail-residual.md`](positive-tail-residual.md)：确定 gap 正号，排除 saturated sector 与 `ell<=k-2`。
7. [`sharp-positive-tail-window.md`](sharp-positive-tail-window.md)：统一加强为
   \[
   \boxed{15.09\,10^{-k}<N_0-\rho<39.003\,10^{-k}.}
   \]
8. [`uniform-2adic-prefix.md`](uniform-2adic-prefix.md)：`2`-进 prefix 完全解析，
   \[
   \boxed{\underline x_*(k)=-k-2.}
   \]
9. [`gap-denominator-normal-form.md`](gap-denominator-normal-form.md)：按 reduced denominator 把 gap desert 分成 central / deep 两块。
10. [`central-gap-2adic.md`](central-gap-2adic.md)：central 的整数平方核模 `64/256`，`144 -> 48` 个 type-gap 组合。
11. [`central-gap-sign-collapse.md`](central-gap-sign-collapse.md)：平方核最高阶符号再排除 `18` 个，`48 -> 30`。
12. [`central-supply-pell-normal-form.md`](central-supply-pell-normal-form.md)：把 central odd-supply 做两级十进制 Euclidean descent；每个剩余 type-gap 被归约为有限个 `U` 与固定系数
   \[
   Y^2=A_U L^2+B_U,
   \qquad L=10^k/c_\Gamma
   \]
   的 generalized Pell / Thue-Mahler families。
13. [`deep-gap-valuation-normal-form.md`](deep-gap-valuation-normal-form.md)：把 noninteger normalized gap 的 denominator excess `(A,B)` 精确对齐到原 2/5 resonance，并得到 deep parity lattice。
14. [`boundary-residual-2adic.md`](boundary-residual-2adic.md)、[`boundary-prime-sieve.md`](boundary-prime-sieve.md)、[`boundary-decimal-supply.md`](boundary-decimal-supply.md)、[`residual-shell-supply.md`](residual-shell-supply.md)：早期 residual-shell / decimal-supply 压缩。
15. [`k3-certificate.md`](k3-certificate.md)、[`k4-k5-certificates.md`](k4-k5-certificates.md)：关闭 `k=3,4,5`。
16. [`k6-first-boundary-certificate.md`](k6-first-boundary-certificate.md)、[`k6-ell6-certificate.md`](k6-ell6-certificate.md)、[`k6-ell7-certificate.md`](k6-ell7-certificate.md)：早期逐 `ell` 的 `k=6` 局部证书，现已被统一证书覆盖。
17. [`k6-uniform-tail-certificate.md`](k6-uniform-tail-certificate.md)：首次消去 `ell`，整个 `k=6` 一次性关闭。
18. [`uniform-layer-finite-box.md`](uniform-layer-finite-box.md)：generic fixed-`k` finite-box theorem；关闭 `k=6,...,23`。
19. [`k24-k25-uniform-certificates.md`](k24-k25-uniform-certificates.md)：继续关闭 `k=24,25`。
20. [`short-tail-saturation.md`](short-tail-saturation.md)：保留 positive-sign theorem 之前的中间记录；其 saturated 分支已被后续结果完全排除。

## 当前状态

A1 整体仍为 `待证`，但 minimal diagonal 已严格关闭

\[
\boxed{1\le k=g\le25.}
\]

因此首个未关闭 fixed layer 为

\[
\boxed{k=g\ge26.}
\]

### 统一 near-integer 输入

对全部 `k>=3`：

\[
\boxed{
15.09\,10^{-k}
<N_0-\rho
<39.003\,10^{-k}.}
\]

故

\[
\rho<N_0,
\qquad L>1,
\qquad \ell\ge k-1,
\]

且归一化 gap

\[
\Gamma_k:=10^k(N_0-\rho)
\]

必须满足

\[
\boxed{15.09<\Gamma_k<39.003.}
\]

### 2-adic prefix 已完全解析

对合法 prefix：

\[
w\text{ even}\Longrightarrow v_2(N)=0,
\]

\[
w\text{ odd}\Longrightarrow v_2(N)\le1.
\]

因此

\[
\boxed{\underline x_*(k)=-k-2}
\]

对所有 `k>=3` 都是闭式。

### reduced-denominator split

写既约

\[
\rho=\frac nd,
\qquad d=2^a5^b,
\qquad r=N_0d-n.
\]

则

\[
\gcd(r,d)=1,
\qquad
\Gamma_k=\frac{10^k r}{d},
\]

并有

\[
\boxed{d>10^k/39.003.}
\]

若 `d|10^k`，进入 central sector；否则进入 deep sector：

\[
\boxed{a>k\quad\text{或}\quad b>k.}
\]

## Central sector

若 `d|10^k`，则 `Gamma_k` 为整数，最初只有

\[
\Gamma\in\{16,17,\ldots,39\}.
\]

同时

\[
\boxed{x=-k+v_2(\Gamma),\qquad y=-k+v_5(\Gamma),}
\]

\[
\boxed{
2^{v_2(\Gamma)}5^{v_5(\Gamma)}h
=N_0 10^k-\Gamma.}
\]

`central-gap-2adic.md` 与 `central-gap-sign-collapse.md` 已把六类型乘 24 gaps 的 `144` 个组合压到以下 `30` 个：

| `(z,w)` | remaining `Gamma` |
|---|---|
| `(1,1)` | `32,34,36,38` |
| `(1,3)` | `24,26,28,30,32,34,36,38` |
| `(3,1)` | `22,24,26,28,30,32,34,36,38` |
| `(1,2)` | `30,32,38` |
| `(3,2)` | `22,30,32,38` |
| `(1,4)` | `24,26` |

其中 `(3,1,Gamma=22)` 还要求

\[
N_0<0.251\,10^k.
\]

### Central odd supply 已降为 finite Pell families

对固定 central `Gamma`，令

\[
c=c_\Gamma=2^{v_2(\Gamma)}5^{v_5(\Gamma)},
\qquad r=\Gamma/c,
\qquad L=10^k/c.
\]

central decimal equation 为

\[
\boxed{h=N_0L-r.}
\]

由完整 odd-prime supply 的弱必要条件

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1
\]

得到

\[
\boxed{h\mid Qb_1.}
\]

而

\[
Qb_1
=1000c^4L^4
+10c^2(1-20w)L^2
+w(10w-1)
\]

只含 `L^4,L^2,1` 三层。对商做两级 Euclidean descent 后产生整数 `U`，严格满足

\[
\boxed{
C_0N_0^2
-U L N_0
+1000c^4r^2L^2
+rU
-10c^2r^2(20w-1)=0,}
\]

其中

\[
C_0=w(10w-1).
\]

更关键地，`U` 落在与 `k` 无关的绝对有限窗

\[
\boxed{
 c(C_0+1000\Gamma^2)
<U
<c(C_0/10+10000\Gamma^2)+1.}
\]

把上式看成关于 `N_0` 的二次方程，判别式必须平方：

\[
\boxed{
Y^2=A_U L^2+B_U,}
\]

\[
A_U=U^2-4000C_0c^4r^2,
\]

\[
B_U=-4C_0rU+40C_0c^2r^2(20w-1).
\]

而

\[
L=2^{k-v_2(c)}5^{k-v_5(c)}.
\]

因此 central 的 `k>=26` 无界问题现已严格归约成：

\[
\boxed{
30\text{ 个固定 type-gap}
\times
\text{有限 }U
\times
\text{固定系数 }2/5\text{-unit Pell families}.}
\]

完整 supply 还保留：

\[
q\mid(10w-1)N_0^2-100\Gamma^2,
\]

\[
s\mid wN_0^2-10\Gamma^2.
\]

这部分尚未全部解完，但已经没有随 `k` 新增的自由系数。

## Deep sector

把 noninteger normalized gap 既约写成

\[
\Gamma_k=\frac{\gamma}{2^A5^B},
\qquad
A=(a-k)_+,
\quad B=(b-k)_+.
\]

central 恰为 `A=B=0`，deep 至少一个正。

平方条件可改写为

\[
V^2=J+2\Gamma_kQN,
\]

其中

\[
\boxed{v_2(J)=2v_2(w),\qquad v_5(J)=0.}
\]

因此 deep excess 与旧 resonance line 完全一致：

- `w=2,4`：任何 `A>0` 都在 strict 2-adic low-side，且
  \[
  \boxed{A\text{ 必为奇数};}
  \]
- `w=1,3` 且 `v_2(N)=0`：`A=1` resonance，之后只允许 `A=3,5,7,...`；
- `w=1,3` 且 `v_2(N)=1`：`A=1` high-side，`A=2` resonance，之后只允许 `A=4,6,8,...`；
- 若 `B>v_5(N)`，则
  \[
  \boxed{B\equiv v_5(N)\pmod2,}
  \]
  而 `B=v_5(N)` 正好是五进 resonance。

所以 deep 也不再是无结构二维格点，而是带明确 resonance level 与 parity lattice 的 reduced-denominator problem。

## Fixed-layer certificates

`uniform-layer-finite-box.md` 已把每个固定 `k` 的整个第三尾压成 finite `(h,x,y)` box，与 `ell` 无关。当前严格关闭

\[
\boxed{k=6,7,\ldots,25.}
\]

结合 `k=1..5` 旧证书：

\[
\boxed{1\le k=g\le25\text{ 全部为空}.}
\]

## 下一步

现在 minimal diagonal 的 `k>=26` 统一核心进一步明确成：

1. **central finite Pell core**：对有限 `U` families 先做深 `2/5`-adic square-residue 过滤；`A_U` 为平方时可直接用差平方排除，大头则进入固定 generalized Pell / Thue-Mahler 方程；同时继续利用 Q-side / whole-block resultants。
2. **deep parity-compatible core**：只处理上面 parity/resonance 允许的 `(A,B)` 层，再加入 2-adic unit mod `8`、5-adic unit mod `5` 与 primitive cross-corridor caps。

如果这两块统一关闭，minimal diagonal 全部 `k>=26` 会一次消失，无需继续逐层 factor certificate。

`d=1,0,-1` 等其他 A1 无界核心仍待处理。

## 可复核脚本

分支专用脚本位于 [`scripts/exact-lift/a1-only/`](../../../../../scripts/exact-lift/a1-only/)。主要包括：

- `check_a1_top_diag_k1.py`、`check_a1_top_diag_k2.py`、`check_a1_top_diag_k3.py`；
- `check_a1_top_diag_k45.py`；
- `check_a1_top_diag_k6_uniform_tail.py`；
- `check_a1_top_diag_uniform_layers.py`：`k=6..23`；
- `check_a1_top_diag_uniform_layers_24_25.py`：`k=24,25`；
- `check_a1_near_integer_tail_constants.py`；
- `check_a1_sharp_positive_tail_constants.py`；
- `check_a1_central_gap_2adic.py`；
- `check_a1_central_gap_sign.py`；
- `check_a1_central_supply_pell_normal_form.py`。
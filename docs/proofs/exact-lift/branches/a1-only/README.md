# `A_1`-only 分支

这是 `A_1` 分支的规范编辑入口。当前主线已经从 fixed-prefix finite theorem 推进到 minimal diagonal 的统一 central/deep denominator 分裂；fixed-layer 证书作为独立保险线同步推进。

## 阅读顺序

1. [`core.md`](core.md)：A1 主框架与审计边界。
2. [`rational-contact.md`](rational-contact.md)：rational-contact、integer-gap、universal denominator funnel、resonance、cross-corridor 与 fixed-prefix finite theorem。
3. [`top-layer.md`](top-layer.md)：moving-prefix 四层压缩、`d=2` endpoint kernel、positive excess 与 minimal-surplus 分裂。
4. [`diagonal.md`](diagonal.md)：`k=g` minimal diagonal、valuation normal form、odd-prime supply 与早期有限证书接口。
5. [`near-integer-tail.md`](near-integer-tail.md)、[`positive-tail-residual.md`](positive-tail-residual.md)、[`sharp-positive-tail-window.md`](sharp-positive-tail-window.md)：最终得到
   \[
   \boxed{15.09\,10^{-k}<N_0-\rho<39.003\,10^{-k}.}
   \]
6. [`uniform-2adic-prefix.md`](uniform-2adic-prefix.md)：`2`-进 prefix 完全解析，
   \[
   \boxed{\underline x_*(k)=-k-2.}
   \]
7. [`gap-denominator-normal-form.md`](gap-denominator-normal-form.md)：按 normalized gap 的 reduced denominator 分成 central / deep 两块。
8. [`central-gap-2adic.md`](central-gap-2adic.md)：central integer-square kernel，`144 -> 48` 个 type-gap。
9. [`central-gap-sign-collapse.md`](central-gap-sign-collapse.md)：最高阶符号继续 `48 -> 30`。
10. [`central-crossing-sharp.md`](central-crossing-sharp.md)：唯一 sign-crossing `(3,1,22)` 收紧为 `N_0/10^k<0.250261`，并推出 `U>=3,867,967`。
11. [`central-supply-pell-normal-form.md`](central-supply-pell-normal-form.md)：两级十进制 Euclidean descent，把 central odd supply 归约成绝对有限 `U` 与固定 generalized Pell families。
12. [`central-pell-local-squareclass.md`](central-pell-local-squareclass.md)：square-`A_U` 退化族统一无解；其余 `U` 必须落入显式 `Q_2/Q_5` squareclasses。
13. [`central-double-square-valuation-lock.md`](central-double-square-valuation-lock.md)：把 supply-Pell 判别式平方与原 contact 平方核联立；`t=U-U_0` 精确决定 `v_2(N_0),v_5(N_0)`，并把多个 family 的 `v_2(t),v_5(t)` 压成绝对有限集合。
14. [`deep-gap-valuation-normal-form.md`](deep-gap-valuation-normal-form.md)：把 deep denominator excess `(A,B)` 对齐到 2/5 resonance，并给出 parity lattice。
15. [`deep-gap-unit-square.md`](deep-gap-unit-square.md)：加入 mod-8 square-unit 与 mod-5 Legendre lock；strict 2-deep 中 Q-side divisor 的 `mod 4` 方向被固定。
16. [`deep-q-side-proper-divisor.md`](deep-q-side-proper-divisor.md)：证明 strict 2-deep 的 `q|Q` 永远是 proper divisor，并有 `q<=Q/7`（`w=1,3,4`）或 `q<=Q/3`（`w=2`）。
17. [`deep-b1-block-loss.md`](deep-b1-block-loss.md)：补上 `b_1` whole-block 侧永久损失，得到 strict 2-deep 的统一 `h` 上界。
18. [`boundary-residual-2adic.md`](boundary-residual-2adic.md)、[`boundary-prime-sieve.md`](boundary-prime-sieve.md)、[`boundary-decimal-supply.md`](boundary-decimal-supply.md)、[`residual-shell-supply.md`](residual-shell-supply.md)：早期 residual-shell 原型。
19. [`k3-certificate.md`](k3-certificate.md)、[`k4-k5-certificates.md`](k4-k5-certificates.md)、[`k6-uniform-tail-certificate.md`](k6-uniform-tail-certificate.md)、[`uniform-layer-finite-box.md`](uniform-layer-finite-box.md)、[`k24-k25-uniform-certificates.md`](k24-k25-uniform-certificates.md)、[`k26-k30-uniform-certificates.md`](k26-k30-uniform-certificates.md)：fixed-layer 精确证书。
20. [`short-tail-saturation.md`](short-tail-saturation.md)：positive-sign theorem 之前的历史中间记录；saturated 分支已被后续结果完全排除。

## 当前状态

A1 整体仍为 `待证`。minimal diagonal 已严格关闭

\[
\boxed{1\le k=g\le30.}
\]

所以首个尚未由 fixed-layer certificate 关闭的层为

\[
\boxed{k=g\ge31.}
\]

对全部 `k>=3`，写

\[
\rho=\frac{b_3}{10^\ell},\qquad
N_0=j-10^k+1,\qquad
\Gamma_k=10^k(N_0-\rho),
\]

则

\[
\boxed{15.09<\Gamma_k<39.003.}
\]

并且 `rho<N_0`、saturated sector 为空、`ell>=k-1`。

## Central denominator sector

写既约 `rho=n/d`、`d=2^a5^b`。若 `d|10^k`，则 `Gamma_k` 为整数。经 2-adic square kernel 与 sign collapse 后只剩 30 个组合：

| `(z,w)` | remaining `Gamma` |
|---|---|
| `(1,1)` | `32,34,36,38` |
| `(1,3)` | `24,26,28,30,32,34,36,38` |
| `(3,1)` | `22,24,26,28,30,32,34,36,38` |
| `(1,2)` | `30,32,38` |
| `(3,2)` | `22,30,32,38` |
| `(1,4)` | `24,26` |

唯一 crossing family `(3,1,22)` 现在严格满足

\[
\boxed{N_0/10^k<0.250261.}
\]

令

\[
c=2^{v_2(\Gamma)}5^{v_5(\Gamma)},\quad
r=\Gamma/c,\quad
L=10^k/c,\quad
C_0=w(10w-1).
\]

central decimal equation为 `h=N_0L-r`。由弱 supply 条件 `h|Qb_1` 做两级 Euclidean descent，得到绝对有限整数 `U`：

\[
C_0N_0^2-U L N_0
+1000c^4r^2L^2+rU
-10c^2r^2(20w-1)=0,
\]

\[
\boxed{
c(C_0+1000\Gamma^2)<U<c(C_0/10+10000\Gamma^2)+1.}
\]

判别式必须满足

\[
\boxed{Y^2=A_UL^2+B_U,}
\]

\[
A_U=U^2-4000C_0c^4r^2,
\qquad
B_U=-4C_0rU+40C_0c^2r^2(20w-1).
\]

定义

\[
U_0=10c\Gamma(20w-1),\qquad V_0=10c\Gamma,
\]

则

\[
U_0^2-V_0^2=4000C_0c^4r^2,
\qquad
\boxed{B_U=-4C_0r(U-U_0).}
\]

允许窗统一满足 `U>U_0`，故 `A_U>0,B_U<0`。若 `A_U` 是整数平方，则由相邻平方间隙在 `k>=26` 统一排除；剩余 family 必须是 nonsquare 且

\[
\boxed{B_U\in\mathbf Q_2^{\times2}\cap\mathbf Q_5^{\times2}.}
\]

更强地，写

\[
t=U-U_0>0,
\]

由二次公式 `2C_0N_0=UL\pm Y` 与 `L` 的深 2/5 赋值，精确得到

\[
\boxed{
v_2(N_0)=\frac{v_2(t)-v_2(C_0)}2,
\qquad
v_5(N_0)=\frac{v_5(t)}2.}
\]

再与原 contact square 联立，得到例如：

\[
\begin{array}{c|c}
(z,w,\Gamma)&v_2(t)\\ \hline
(1,2,30)&\{3,7,9\}\\
(1,2,38)&\{3,7\}\\
(3,2,22)&\{3,7\}\\
(3,2,30)&\{3,5\}\\
(3,2,38)&\{3,5\}\\
(1,4,24)&\{4,6\}
\end{array}
\]

以及

\[
\begin{array}{c|c}
(z,w,\Gamma)&v_5(t)\\ \hline
(1,1,34)&\{0\}\\
(1,1,36)&\{0,2\}\\
(1,1,38)&\{0\}\\
(3,2,38)&\{0\}\\
(1,4,24)&\{0\}\\
(1,4,26)&\{0,2\}.
\end{array}
\]

因此 central 进入 Pell/Thue-Mahler 阶段时应按这些真实 `(v_2(t),v_5(t))` cells 分流，而不再扫描完整 `U` 窗。

## Deep denominator sector

若 `d` 不整除 `10^k`，写

\[
\Gamma_k=\frac{\gamma}{2^A5^B},
\qquad A=(a-k)_+,\quad B=(b-k)_+,
\]

其中至少一个正。平方条件可写成

\[
V^2=J+2\Gamma_kQN,
\qquad
\boxed{v_2(J)=2v_2(w),\quad v_5(J)=0.}
\]

已有 parity/resonance：

- `w=2,4`：`A>0` 时 `A` 必为奇数；
- `w=1,3`、`v_2(N)=0`：`A=1` resonance，strict-low 只允许 `A=3,5,...`；
- `w=1,3`、`v_2(N)=1`：`A=1` high-side、`A=2` resonance，strict-low 只允许 `A=4,6,...`；
- `B>v_5(N)` 时 `B≡v_5(N) (mod 2)`，而 `B=v_5(N)` 是 5-adic resonance。

strict 2-low 的单位平方锁为

\[
\boxed{\gamma QN_2 5^B\equiv1\pmod8.}
\]

它进一步强迫

\[
w\text{ odd}\Rightarrow q\equiv1\pmod4,
\qquad
w\text{ even}\Rightarrow q\equiv3\pmod4,
\]

其中 `h=qs`、`q|Q`，而 `s` 是 `b_1` 的 `1 mod4` whole-block selector。于是 `Q/q≡3 mod4`，从而

\[
\boxed{
q\le Q/7\ (w=1,3,4),
\qquad q\le Q/3\ (w=2).}
\]

`b_1` 侧还存在永久 whole-block loss：

\[
B_+\le
\begin{cases}
b_1/3,&w=1,\\
b_1/14,&w=2,\\
b_1,&w=3,\\
b_1/12,&w=4.
\end{cases}
\]

所以 strict 2-deep 的完整 odd supply 统一加强为

\[
\boxed{
h\le
\begin{cases}
Qb_1/21,&w=1,\\
Qb_1/42,&w=2,\\
Qb_1/7,&w=3,\\
Qb_1/84,&w=4.
\end{cases}}
\]

strict 5-low 还满足 Legendre lock

\[
\boxed{
\left(\frac{hN_5}{5}\right)=(-1)^{1-A+\lambda_2}.}
\]

因此 deep 剩余是带 **resonance parity + 2/5 unit square + directed Q-side supply + permanent block loss** 的 denominator lattice。

## Fixed-layer certificates

完整精确证书当前关闭

\[
\boxed{k=1,2,\ldots,30.}
\]

其中 `k=26..30` 仍检查旧的更宽窗口

\[
5.09<10^k(\lceil\rho\rceil-\rho)<50.45,
\]

所以对当前 sharpened window 是更强排除。最新五层数据：

| `k` | `H counts (w=1..4)` | box `(xmin,xmax;ymin,ymax)` | decade states | hits |
|---:|---|---|---:|---:|
| 26 | `(128,24,32,256)` | `(-329,239;-126,49)` | `146580` | 0 |
| 27 | `(12288,160,32,512)` | `(-339,245;-130,51)` | `4238867` | 0 |
| 28 | `(256,768,16,64)` | `(-330,255;-126,52)` | `390688` | 0 |
| 29 | `(64,96,128,256)` | `(-343,263;-131,54)` | `196277` | 0 |
| 30 | `(32768,128,64,64)` | `(-378,273;-145,56)` | `11672944` | 0 |

首个尚未关闭 fixed layer 是 `k=31`。当前本地精确 factorization 已完成其大部分 prefix；`w=4` 的 `Q=10^64-39` 尚未获得完整 factorization，因此这里不把 partial factor data 冒充证书。

## 下一步

minimal diagonal 的统一剩余核心仍是两块：

1. **central nonsquare Pell core**：只研究 double-square local cells 中的 nonsquare-`A_U` families；优先利用 `L=2^\alpha5^\beta` 的 `S`-unit 结构、generalized Pell recurrence/primitive-divisor，以及 Q-side / whole-block resultants。
2. **deep unit-compatible core**：把新的 `h` 上界与 cross-corridor decade bound 联用，尝试把 `(A,B)` 进一步压成绝对高度；even-`w` 同时要求 `Q` 真正提供非平凡 `3 mod4` proper divisor。

fixed-layer 证书继续作为保险线，但不替代上述 uniform proof。

`d=1,0,-1` 等其他 A1 无界核心仍待处理。

## 可复核脚本

分支脚本位于 [`scripts/exact-lift/a1-only/`](../../../../../scripts/exact-lift/a1-only/)。主要包括：

- `check_a1_top_diag_k1.py`、`check_a1_top_diag_k2.py`、`check_a1_top_diag_k3.py`；
- `check_a1_top_diag_k45.py`；
- `check_a1_top_diag_k6_uniform_tail.py`；
- `check_a1_top_diag_uniform_layers.py`：`k=6..23`；
- `check_a1_top_diag_uniform_layers_24_25.py`：`k=24,25`；
- `check_a1_top_diag_uniform_layers_26_30.py`：`k=26..30`；
- `check_a1_sharp_positive_tail_constants.py`；
- `check_a1_central_gap_2adic.py`；
- `check_a1_central_gap_sign.py`；
- `check_a1_central_supply_pell_normal_form.py`；
- `check_a1_central_pell_local_squareclass.py`；
- `check_a1_central_double_square_valuations.py`；
- `check_a1_deep_gap_unit_square.py`。
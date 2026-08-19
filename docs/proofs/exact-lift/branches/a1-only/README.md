# `A_1`-only 分支

这是 `A_1` 分支的规范编辑入口。当前主线已经从 fixed-prefix finite theorem 推进到 minimal diagonal 的统一 central/deep denominator 分裂。

## 阅读顺序

1. [`core.md`](core.md)：A1 主框架与审计边界。
2. [`rational-contact.md`](rational-contact.md)：rational-contact、integer-gap、universal denominator funnel、resonance、cross-corridor 与 fixed-prefix finite theorem。
3. [`top-layer.md`](top-layer.md)：moving-prefix 四层压缩、`d=2` endpoint kernel、positive excess 与 minimal-surplus 分裂。
4. [`diagonal.md`](diagonal.md)：`k=g` minimal diagonal、valuation normal form、odd-prime supply 与早期有限证书接口。
5. [`near-integer-tail.md`](near-integer-tail.md)、[`positive-tail-residual.md`](positive-tail-residual.md)、[`sharp-positive-tail-window.md`](sharp-positive-tail-window.md)：把第三尾压到整数左侧的二阶窄窗，最终得到
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
10. [`central-supply-pell-normal-form.md`](central-supply-pell-normal-form.md)：两级十进制 Euclidean descent，把 central odd supply 归约成绝对有限 `U` 与固定系数 generalized Pell families。
11. [`central-pell-local-squareclass.md`](central-pell-local-squareclass.md)：证明所有 square-`A_U` 退化 Pell families 统一无解；其余 `U` 必须落入显式 `Q_2/Q_5` squareclasses。
12. [`deep-gap-valuation-normal-form.md`](deep-gap-valuation-normal-form.md)：把 deep denominator excess `(A,B)` 精确对齐到 2/5 resonance，并给出 parity lattice。
13. [`deep-gap-unit-square.md`](deep-gap-unit-square.md)：加入 mod-8 square-unit 与 mod-5 Legendre lock；strict 2-deep 中 Q-side divisor 的 `mod 4` 方向被固定。
14. [`boundary-residual-2adic.md`](boundary-residual-2adic.md)、[`boundary-prime-sieve.md`](boundary-prime-sieve.md)、[`boundary-decimal-supply.md`](boundary-decimal-supply.md)、[`residual-shell-supply.md`](residual-shell-supply.md)：早期逐 residual-shell 压缩，现作为统一理论的局部原型保留。
15. [`k3-certificate.md`](k3-certificate.md)、[`k4-k5-certificates.md`](k4-k5-certificates.md)、[`k6-uniform-tail-certificate.md`](k6-uniform-tail-certificate.md)、[`uniform-layer-finite-box.md`](uniform-layer-finite-box.md)、[`k24-k25-uniform-certificates.md`](k24-k25-uniform-certificates.md)：fixed-layer 精确证书。
16. [`short-tail-saturation.md`](short-tail-saturation.md)：positive-sign theorem 之前的中间记录；其 saturated 分支已被后续结果完全排除。

## 当前状态

A1 整体仍为 `待证`。minimal diagonal 已严格关闭

\[
\boxed{1\le k=g\le25.}
\]

所以首个未关闭 fixed layer 为

\[
\boxed{k=g\ge26.}
\]

对全部 `k>=3`，写

\[
\rho=\frac{b_3}{10^\ell},
\qquad
N_0=j-10^k+1,
\qquad
\Gamma_k=10^k(N_0-\rho),
\]

则

\[
\boxed{15.09<\Gamma_k<39.003.}
\]

并且 `rho<N_0`、saturated sector 为空、`ell>=k-1`。

## Central denominator sector

写 `rho=n/d`、`d=2^a5^b`。若 `d|10^k`，则 `Gamma_k` 必为整数，因此最初只有

\[
\Gamma\in\{16,17,\ldots,39\}.
\]

2-adic square kernel 与最高阶符号已把六类型乘 24 gaps 的 144 个组合压到 30 个：

| `(z,w)` | remaining `Gamma` |
|---|---|
| `(1,1)` | `32,34,36,38` |
| `(1,3)` | `24,26,28,30,32,34,36,38` |
| `(3,1)` | `22,24,26,28,30,32,34,36,38` |
| `(1,2)` | `30,32,38` |
| `(3,2)` | `22,30,32,38` |
| `(1,4)` | `24,26` |

其中 `(3,1,Gamma=22)` 还要求 `N_0<0.251*10^k`。

令

\[
c=2^{v_2(\Gamma)}5^{v_5(\Gamma)},
\qquad r=\Gamma/c,
\qquad L=10^k/c,
\qquad C_0=w(10w-1).
\]

central decimal equation 为

\[
h=N_0L-r.
\]

利用 `h=qs`、`q|Q`、`s|b_1` 的弱必要条件 `h|Qb_1`，两级 Euclidean descent 产生一个与 `k` 无关的有限整数 `U`，满足

\[
C_0N_0^2-U L N_0
+1000c^4r^2L^2+rU
-10c^2r^2(20w-1)=0,
\]

以及

\[
\boxed{
 c(C_0+1000\Gamma^2)
<U
<c(C_0/10+10000\Gamma^2)+1.}
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

新定义

\[
U_0=10c\Gamma(20w-1),
\qquad
V_0=10c\Gamma
\]

给出精确恒等式

\[
U_0^2-V_0^2=4000C_0c^4r^2,
\]

\[
\boxed{B_U=-4C_0r(U-U_0).}
\]

允许窗统一满足 `U>U_0`，所以

\[
\boxed{A_U>0,\qquad B_U<0.}
\]

若 `A_U=S^2`，则

\[
Y^2=(SL)^2-|B_U|
\]

在 `k>=26` 时严格夹于 `(SL-1)^2` 与 `(SL)^2` 之间。因此

\[
\boxed{A_U\text{ square 的全部退化族已经统一排空}.}
\]

其余 nonsquare family 还必须满足完整的局部条件

\[
\boxed{B_U\in\mathbf Q_2^{\times2}\cap\mathbf Q_5^{\times2}.}
\]

若 `t=U-U_0=2^a5^bm`、`gcd(m,10)=1`，则 `a,b` 的 parity 被固定，`m mod 8` 唯一，`m mod 5` 只剩两个 Legendre classes；也就是每个 valuation pair 至多两条 `mod 40` squareclass ray。

完整 supply 仍保留

\[
q\mid(10w-1)N_0^2-100\Gamma^2,
\qquad
s\mid wN_0^2-10\Gamma^2.
\]

因此 central 目前只剩：**nonsquare、local-compatible 的固定 generalized Pell / Thue-Mahler families**。

## Deep denominator sector

若 `d` 不整除 `10^k`，则至少有

\[
A=(a-k)_+>0
\quad\text{或}\quad
B=(b-k)_+>0.
\]

把 normalized gap 既约写成

\[
\Gamma_k=\frac{\gamma}{2^A5^B}.
\]

平方条件可改写为

\[
V^2=J+2\Gamma_kQN,
\]

其中

\[
\boxed{v_2(J)=2v_2(w),\qquad v_5(J)=0.}
\]

valuation parity 给出：

- `w=2,4`：任何 `A>0` 都是 strict 2-low，且 `A` 必为奇数；
- `w=1,3`、`v_2(N)=0`：`A=1` resonance，之后只允许 `A=3,5,7,...`；
- `w=1,3`、`v_2(N)=1`：`A=1` high-side，`A=2` resonance，之后只允许 `A=4,6,8,...`；
- `B>v_5(N)` 时 `B≡v_5(N) (mod 2)`，`B=v_5(N)` 是 5-adic resonance。

新的 unit-square 条件继续给出 strict 2-low：

\[
\boxed{
\gamma QN_2 5^B\equiv1\pmod8,
\qquad N_2=N/2^{v_2(N)}.}
\]

六类型因此统一成

\[
\boxed{
 w\in\{1,3\}\Longrightarrow h\equiv1\pmod4,
}
\]

\[
\boxed{
 w\in\{2,4\}\Longrightarrow h\equiv3\pmod4.
}
\]

而 `h=qs` 中 whole-block selector `s≡1 mod4`，故 Q-side divisor 必须满足

\[
\boxed{
 w\text{ odd}\Longrightarrow q\equiv1\pmod4,
\qquad
 w\text{ even}\Longrightarrow q\equiv3\pmod4.}
\]

strict 5-low 还满足

\[
\boxed{
\left(\frac{hN_5}{5}\right)
=(-1)^{1-A+\lambda_2},
}
\]

其中 `N_5=N/5^{v_5(N)}`，而 `lambda_2=0`（`A>0`）或 `lambda_2=k+x`（`A=0`）。

所以 deep 已经从 parity lattice 进一步压成带明确 **Q-side orientation + 2/5 unit-square** 的格子。

## Fixed-layer certificates

已有精确证书关闭

\[
\boxed{k=1,2,\ldots,25.}
\]

其中 `k=6..25` 使用与 `ell` 无关的 finite `(h,x,y)` box；首个尚未关闭 fixed layer 为 `k=26`。

## 下一步

minimal diagonal 的统一剩余核心现在只有两块：

1. **central nonsquare Pell core**：只研究通过 `Q_2/Q_5` squareclass 的 nonsquare-`A_U` families；下一入口是 primitive-divisor / Lucas-Pell 的 `2/5`-unit denominator obstruction，并继续保留 Q-side / whole-block resultants。
2. **deep unit-compatible core**：只研究符合 resonance parity、mod-8 unit lock、mod-5 Legendre lock 与 Q-side orientation 的 `(A,B,h=q s)`；优先利用 `q mod4` 定向缩小 Q-side supply，再与 primitive cross-corridor caps 联用。

如果这两块统一关闭，minimal diagonal 的全部 `k>=26` 将一次消失，无需继续逐层 factor certificate。

`d=1,0,-1` 等其他 A1 无界核心仍待处理。

## 可复核脚本

分支专用脚本位于 [`scripts/exact-lift/a1-only/`](../../../../../scripts/exact-lift/a1-only/)。主要包括：

- `check_a1_top_diag_k1.py`、`check_a1_top_diag_k2.py`、`check_a1_top_diag_k3.py`；
- `check_a1_top_diag_k45.py`；
- `check_a1_top_diag_k6_uniform_tail.py`；
- `check_a1_top_diag_uniform_layers.py`：`k=6..23`；
- `check_a1_top_diag_uniform_layers_24_25.py`：`k=24,25`；
- `check_a1_sharp_positive_tail_constants.py`；
- `check_a1_central_gap_2adic.py`；
- `check_a1_central_gap_sign.py`；
- `check_a1_central_supply_pell_normal_form.py`；
- `check_a1_central_pell_local_squareclass.py`；
- `check_a1_deep_gap_unit_square.py`。
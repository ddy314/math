# A2 fixed `199` f-side angle residual

> **依赖：** [`fixed-prime-asymmetric-lifts.md`](fixed-prime-asymmetric-lifts.md)；[`source-angle-ledger.md`](source-angle-ledger.md) 中整合来源 `spontaneous-denominator-depth-matrix.md` 与 `spontaneous-denominator-depth-residuals.md`。
>
> **严格状态：**本文识别 f-side height center 上一个此前未单列的 coefficient-degeneration prime `199`。它不进入 additive cofactor，而只出现在 angle/depth-mismatch residual 一侧。本文给出两条 genuine first-layer state、唯一 `199^2` height-angle lifts、精确第一层 residual，以及 decimal-orbit 审计。本文仍**不宣称 A2 全局关闭**。

---

## 1. f-side depth residual 的 Bezout 结构

沿用 pure-prefix angle defect

\[
D_{\rm pref}:=A_{\rm pref}-K^2,
\qquad
A_{\rm pref}:=2025b_2^2+81N^2,
\qquad N=10^M.
\tag{1.1}
\]

f-side additive quadratic为

\[
\boxed{P_f(K):=3K^2-36K+26.}
\tag{1.2}
\]

`spontaneous-denominator-depth-residuals.md` 定义

\[
\boxed{
R_f^{\rm len}(A):=9A^2-1140A+676,
}
\tag{1.3}
\]

以及 exact Bezout identity

\[
\boxed{
R_f^{\rm len}
=P_f(K)U_f+D_{\rm pref}V_f,
}
\tag{1.4}
\]

其中

\[
U_f=3A_{\rm pref}+26+36K,
\qquad
V_f=3U_f-1296.
\tag{1.5}
\]

在 ordinary common root `P_f=D_pref=0` 上，旧账本已经证明 `U_f,V_f` 对 genuine non-`3` inert prime 均为单位，所以 residual 只承担 simple depth mismatch。

本文研究另一种边界：**height center + angle contact**。

---

## 2. `已严格完成`：height center 把 fixed factors 精确分成 `7,43` 与 `199`

height+saturation 给

\[
\boxed{K\equiv\frac92\pmod p.}
\tag{2.1}
\]

若 angle 也接触，则

\[
D_{\rm pref}\equiv0,
\]
故

\[
A_{\rm pref}\equiv K^2\equiv\frac{81}{4}\pmod p.
\tag{2.2}
\]

把这个共同 center 直接代入 (1.2)、(1.5)：

\[
\boxed{
P_f\left(\frac92\right)
=-\frac{301}{4}
=-\frac{7\cdot43}{4},
}
\tag{2.3}
\]

而

\[
\boxed{
U_f\left(\frac{81}{4},\frac92\right)
=\frac{995}{4}
=\frac{5\cdot199}{4}.
}
\tag{2.4}
\]

所以在 non-`5` inert prime 中出现严格二分：

1. `p=7,43`：`P_f=0`，即历史 fixed additive-height common pool；
2. `p=199`：`P_f` 为单位，但 Bezout coefficient `U_f=0`。

并且

\[
R_f^{\rm len}\left(\frac{81}{4}\right)
=-\frac{299495}{16}
=-\frac{5\cdot7\cdot43\cdot199}{16}.
\tag{2.5}
\]

因此

\[
\boxed{
199\text{ 是 f-side height/angle center 上唯一新的 non-3 inert coefficient-degeneration prime}.}
\tag{2.6}
\]

它与 `7,43` 的性质不同：`199` 不进入 additive root。

---

## 3. f-saturation + angle + height 的纯 prefix system

使用 normalized variables

\[
x=\frac{b_2}{10^M},
\qquad
y=\frac{10a_2}{10^M},
\qquad
\tau=10^{-M},
\qquad s=y+9.
\]

f-line、saturation 与 exact sphere 在 angle sheet 上给出

\[
D:=2025x^2-18y-y^2=0,
\tag{3.1}
\]

\[
L:=200x^2(s-9\tau)-y(x+2)^2=0.
\tag{3.2}
\]

height center 为

\[
H:=2s-9\tau=0.
\tag{3.3}
\]

利用 `H=0` 消去 `tau`，再以 `s=y+9` 改写：

\[
2025x^2-s^2+81=0,
\]

\[
-200x^2s-(s-9)(x+2)^2=0.
\]

对 `s` 求 resultant 得

\[
\boxed{
2025x^2F_H(x),
}
\tag{3.4}
\]

其中

\[
\boxed{
F_H(x)=40401x^4+1608x^3+3240x^2+96x+80.
}
\tag{3.5}
\]

所以 genuine state 只需考察 `F_H(x)=0` 的非零根。

---

## 4. `有限 exact 证书`：`p=199` 恰有两条 genuine first-layer state

模 `199`，(3.5) 的根恰为

\[
\boxed{x=22,124.}
\tag{4.1}
\]

由 (3.1)–(3.3) 唯一恢复

\[
\boxed{
(x,y,\tau)=(22,83,131),
\qquad
(124,146,145)
\pmod{199}.}
\tag{4.2}
\]

两点中的 `x,y,tau,x+2,s` 全部为单位，因此不落在 q-boundary、zero-height 或 decimal boundary。

并且

\[
K=s/\tau\equiv9/2\pmod{199},
\]
故

\[
\boxed{P_f(K)\equiv74\not\equiv0\pmod{199}.}
\tag{4.3}
\]

结合完整 saturation depth law

\[
\min\{v_{199}(\widehat{\mathcal T}_2),e\}
=
\min\{v_{199}(P_f(K)),e\},
\]
得到

\[
\boxed{199\nmid\widehat{\mathcal T}_2.}
\tag{4.4}
\]

因此 `199` 是严格的 **angle-only residual correction**：它可以进入 saturated denominator + height + angle，却不进入 additive side。

---

## 5. `已严格完成`：两条 `199` state 都只有唯一 height-angle Hensel branch

对 `(D,L,H)` 关于 `(x,y,tau)` 的 Jacobian，在 (4.2) 两点的 determinant 分别为

\[
\boxed{58,53\pmod{199},}
\tag{5.1}
\]

均为单位。因此两点各自唯一提升到所有 `199^k`。

第二层为

\[
\boxed{
\begin{array}{c|c|c}
(x,y,\tau)\bmod199&(x,y,\tau)\bmod199^2&M\bmod19701\\ \hline
(22,83,131)&(3206,36102,21225)&7549\\
(124,146,145)&(12462,17260,21438)&9224
\end{array}}
\tag{5.2}
\]

这里

\[
19701=99\cdot199
=\operatorname{ord}_{199^2}(10).
\]

---

## 6. `已严格完成`：deep height-angle branch 上 mismatch residual 永远精确一层

若 `(D,L,H)` 已提升到模 `199^2`，则

\[
D_{\rm pref}\equiv0\pmod{199^2},
\qquad
K\equiv\frac92\pmod{199^2}.
\tag{6.1}
\]

所以 (1.3) 在整条 deep branch 上满足

\[
R_f^{\rm len}
\equiv
-\frac{299495}{16}
\pmod{199^2}.
\tag{6.2}
\]

而

\[
v_{199}(299495)=1.
\]

因此

\[
\boxed{v_{199}(R_f^{\rm len})=1.}
\tag{6.3}
\]

这说明 coefficient degeneration 也没有形成新的无界 residual Hensel tree：`199` 的特殊性只存在第一层；一旦 height 与 angle 继续加深，`R_f^{len}` 立刻停在精确深度 `1`。

---

## 7. `已严格完成 / 降级`：higher decimal orbit 仍不会排除 `199`

模 `199` 有

\[
\operatorname{ord}_{199}(10)=99.
\tag{7.1}
\]

并且

\[
\boxed{
10^{99}\equiv1+165\cdot199\pmod{199^2},
}
\tag{7.2}
\]

其中 `165` 为模 `199` 单位。因此

\[
\boxed{
\operatorname{ord}_{199^k}(10)=99\cdot199^{k-1}.
}
\tag{7.3}
\]

两条 first-layer states 已分别满足

\[
M\equiv25,17\pmod{99},
\]
第二层则细化为 (5.2) 的两个 class。继续做纯 `tau in <10>` 检查只会唯一提升 `M`，不会产生局部空性。

---

## 8. 更新后的 fixed residual frontier

当前 f-side height-supported fixed phenomena 可严格分成：

\[
\boxed{
\begin{array}{c|c|c}
\text{prime}&\text{mechanism}&\text{additive contact}\\ \hline
7,43&P_f(9/2)=0&\text{yes}\\
199&U_f(81/4,9/2)=0&\text{no}
\end{array}}
\tag{8.1}
\]

其中：

- `7,43` 的 denominator-height-angle-additive pool 已由 `fixed-prime-asymmetric-lifts.md` 压成两条 unique asymmetric branches；
- `199` 只有两条 unique height-angle branches，additive depth 恒为 `0`，mismatch residual 在 deep branch 上精确 depth `1`；
- 四类 branch 都不能靠继续机械 decimal lifting 关闭。

因此 fixed local exceptional pool 已经没有多分叉或 singular Hensel tree。若这些固定 corrections 最终要从 `G_sp mod 4` parity ledger 中删除，需要新的**全局 prime allocation / natural representative** 输入，而不是更多同一局部方程的升模。

---

## 9. 验证

```bash
uv run python scripts/exact-lift/a2-only/check_a2_fixed199_angle_residual.py
```

脚本核对 center factorization、quartic eliminant、两条 first-layer state、Jacobian、`199^2` lifts、decimal classes、additive unit 与 residual exact-depth-one 结论。

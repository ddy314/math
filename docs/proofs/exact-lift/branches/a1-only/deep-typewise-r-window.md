# A1 minimal diagonal: typewise moderate `r` windows

> 日期：2026-08-20。依赖 `sharp-positive-tail-window.md` 与 `deep-moderate-factorization.md`。当前范围 `k=g>=31`。

moderate double-deep 中此前只使用统一粗界

\[
196000<r<15214000.
\]

本文把六个 prefix 类型各自的 sharpened gap window 保留下来，得到更窄的 exact integer intervals。

状态：**已严格完成。**

---

## 1. `r` 的 exact real formula

写

\[
T=10^k,
\qquad s:=N_0/T\in[0.1,1],
\qquad \Gamma:=\Gamma_k=\gamma/D.
\]

moderate factorization 中

\[
X_1=10\gamma T-wDN_0,
\qquad
X_2=100\gamma T-(10w-1)DN_0,
\]

\[
h=DTN_0-\gamma,
\qquad
X_1X_2=Drh.
\]

除去 `D^2 T^2` 后精确得到

\[
\boxed{
 r=
\frac{
(10\Gamma-ws)
(100\Gamma-(10w-1)s)
}{
s-\Gamma/T^2
}.
}
\tag{1}
\]

当前 `Gamma<39.003`、`T>=10^31`，分母严格为正。

---

## 2. 单调性

记分子

\[
P=(10\Gamma-ws)(100\Gamma-(10w-1)s)>0,
\]

分母

\[
H=s-\Gamma/T^2>0.
\]

对 `Gamma`：两个分子因子都严格增加，而 `H` 严格减少，所以

\[
\boxed{\partial_\Gamma r>0.}
\tag{2}
\]

对 `s`：两个分子因子都严格减少，所以 `partial_s P<0`，而 `partial_s H=1`。因此

\[
\partial_s r
=\frac{(\partial_sP)H-P}{H^2}<0.
\]

故

\[
\boxed{\partial_s r<0.}
\tag{3}
\]

所以每个类型的最小 `r` 在 `s=1`、typewise lower gap endpoint；最大 `r` 在 `s=0.1`、typewise upper endpoint。

---

## 3. typewise gap constants

`sharp-positive-tail-window.md` 的严格 typewise lower constants 可取：

\[
\begin{array}{c|c}
(z,w)&L_{z,w}\\ \hline
(1,1)&27.6949968\\
(1,2)&23.4949936\\
(1,3)&19.2949904\\
(1,4)&15.0949872\\
(3,1)&19.6949978\\
(3,2)&17.4949956
\end{array}
\]

同一文件的 typewise upper computation给出安全严格上界：

\[
\begin{array}{c|c}
(z,w)&U_{z,w}\\ \hline
(1,1)&33.00225945\\
(1,2)&29.00225945\\
(1,3)&25.00225945\\
(1,4)&21.00225945\\
(3,1)&39.00225945\\
(3,2)&37.00225945
\end{array}
\]

这些常数本来用 `epsilon<=10^-6` 推出，所以当前 `k>=31` 当然安全。

---

## 4. exact integer windows

把上述端点代入 (1)，并在最坏 `T=10^31` 下用 exact rational arithmetic 取严格整数内窗，得到：

\[
\boxed{
\begin{array}{c|c}
(z,w)&r\\ \hline
(1,1)&761760\le r\le10885221\\
(1,2)&542890\le r\le8400003\\
(1,3)&361000\le r\le6236387\\
(1,4)&216090\le r\le4394372\\
(3,1)&384160\le r\le15204352\\
(3,2)&299290\le r\le13677244
\end{array}}
\tag{4}
\]

因为 `Gamma/T^2` 随 `T` 增大而变小，上述 `T=10^31` 端点对全部更大 `k` 同样安全；脚本使用 exact fractions 审计这些整数截断。

---

## 5. valuation 改进

从 (4) 立即得到：

\[
\boxed{
v_2(r)\le22
\quad\text{for }(1,3),(1,4),}
\tag{5}
\]

其余四类型仍安全使用 `v_2(r)<=23`。

五进方面：

\[
5^{10}=9765625.
\]

所以

\[
\boxed{
v_5(r)\le9
\quad\text{for }(1,2),(1,3),(1,4),}
\tag{6}
\]

而 `(1,1),(3,1),(3,2)` 仍用 `v_5(r)<=10`。

当前 moderate double-deep 已全部处于 5-low，因此

\[
B+2\nu_5=v_5(r).
\]

于是进一步：

\[
\boxed{
B+2\nu_5\le9
\quad\text{for }(1,2),(1,3),(1,4),}
\tag{7}
\]

其余三类型有 `<=10`。

---

## 6. 当前用途

后续 LL/HL 的 finite `r` / block-partition exhaustion 不应再扫描统一粗窗。应直接按 (4) 的 typewise interval，并在入口先应用：

- `r_10 mod 4` branch filter；
- `v_5(r)` 的 typewise cap；
- `(1,3),(1,4)` 的更强 `v_2(r)<=22`。

这会进一步降低 moderate branch 的 finite parameter volume。
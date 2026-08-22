# A2 fixed `3` 的 `f`-contact orientation selector

> **依赖：** `fixed3-terminal-spill.md`、`fixed3-exception-collapse.md`、`endpoint-lattice.md` §§16.7、16.11、16.57–16.59，以及 `primitive-reduction.md`。
>
> **严格状态：**本文处理 `fixed3-exception-collapse.md` 尚未关闭的一般 `eta>=2`、`a_2`-shallow `3|f` 通道，但不试图用一个模 `3` 条件错误地宣称它为空。结论是：`f`-contact 会把 Gaussian high-2 side 完全定向。若 `e_3=v_3(k_h)=1`，high-2 factor 必在正号槽；若 `e_3=3`，必在负号槽。并同时固定 `c_Q5^d`、`gc_u` 与 `omega` 的模 `3` 相位。历史 `eta=1` 唯一 odd-`3` 类型 `(d,c_Q,k_h,slot)=(2,7,3,-)` 因此作为立即推论被排除。一般 `eta>=2` 中与 selector 相容的两类仍可能存在，所以 A2 仍为 `待证`。

---

## 1. `a_2`-shallow odd-`3` channel

固定 `Z≡1 mod4` orientation 的第二个 odd-`3` endpoint channel：

\[
\boxed{
v_3(a_2)=1,
\qquad
v_3(a_3)\ge2.}
\tag{1.1}
\]

写

\[
a_2=3a,
\qquad 3\nmid a.
\tag{1.2}
\]

`endpoint-lattice.md` §16.11 已严格证明

\[
\boxed{
e_3:=v_3(k_h)\in\{1,3\},}
\tag{1.3}
\]

同时 sphere norm 的总 `3`-depth为 `4`。令 high-2 factor 的方向为

\[
\boxed{
H_0+\varepsilon Y_2=\frac{g^2k_h}{2},
\qquad
\varepsilon\in\{-1,+1\},}
\tag{1.4}
\]

以及

\[
Y_2=a_2c_Q5^d.
\tag{1.5}
\]

则另一个 low-2 factor 是 `H_0-epsilon Y_2`，两者 `3`-进深度精确为

\[
\boxed{
\bigl(v_3(H_0+\varepsilon Y_2),
      v_3(H_0-\varepsilon Y_2)\bigr)
=(e_3,4-e_3).}
\tag{1.6}
\]

---

## 2. 假设 `3|f` 后的两个 normalized units

现在进入旧 fixed sheet

\[
\boxed{3\mid f.}
\tag{2.1}
\]

由 `primitive-reduction.md`

\[
H_0=c_uW_q,
\qquad
\alpha=\omega W_q,
\qquad
f=g\omega+c_u.
\tag{2.2}
\]

当前 `a_2`-shallow channel 中

\[
\alpha=TK+a_3,
\qquad
\frac\alpha3\equiv a\pmod3,
\tag{2.3}
\]

因为 `K≡a_2 mod9`、`a_3` 至少含 `3^2`，且 `T=10^m≡1 mod3`。

由 (2.1),(2.2)，`g,omega,c_u` 都是 `3`-units 且

\[
\frac{c_u}{\omega}\equiv-g\pmod3.
\tag{2.4}
\]

所以

\[
\boxed{
\frac{H_0}{3}\equiv-ag\pmod3.}
\tag{2.5}
\]

定义

\[
\boxed{B:=c_Q5^d.}
\tag{2.6}
\]

则

\[
\boxed{
\frac{Y_2}{3}\equiv aB\pmod3.}
\tag{2.7}
\]

这里 `B` 是 unit，因为 odd-`3` channel 已有 `3∤c_Q`。

---

## 3. exact factor depths 决定 `epsilon B/g`

### 3.1 `e_3=1`

此时 high-2 factor 深度为 `1`，另一个 factor 深度为 `3`。因此

\[
3^2\mid
\frac{H_0-\varepsilon Y_2}{3}.
\]

特别地模 `3`：

\[
-ag-\varepsilon aB\equiv0.
\]

约去 unit `a`：

\[
\boxed{\varepsilon B\equiv-g\pmod3.}
\tag{3.1}
\]

### 3.2 `e_3=3`

现在 high-2 factor 本身深度为 `3`，所以

\[
3^2\mid
\frac{H_0+\varepsilon Y_2}{3}.
\]

由 (2.5),(2.7)：

\[
-ag+\varepsilon aB\equiv0,
\]

即

\[
\boxed{\varepsilon B\equiv g\pmod3.}
\tag{3.2}
\]

为统一记号，令

\[
\sigma=
\begin{cases}
-1,&e_3=1,\\
+1,&e_3=3.
\end{cases}
\]

则 (3.1),(3.2) 可写成

\[
\boxed{\varepsilon B\equiv\sigma g\pmod3.}
\tag{3.3}
\]

---

## 4. source `Q_0` identity 强迫唯一 orientation

另一方面，source split 给

\[
f=5^\lambda q+2c_u,
\qquad
Q_0=c_Qq=5^M+2^mgc_u,
\qquad
\lambda=m-d.
\tag{4.1}
\]

由 `3|f`：

\[
q\equiv(-1)^\lambda c_u\pmod3.
\tag{4.2}
\]

代入第二式：

\[
c_Q(-1)^\lambda c_u
\equiv
(-1)^M+(-1)^mgc_u
\pmod3.
\]

约去 `c_u`，再用 `lambda=m-d` 与 `B=c_Q(-1)^d`：

\[
\boxed{
B\equiv g+\delta c_u^{-1}\pmod3,}
\tag{4.3}
\]

其中

\[
\boxed{
\delta:=(-1)^{M+m}=(-1)^{m-\eta},
\qquad
\eta=2m-M.}
\tag{4.4}
\]

把 (3.3) 写成

\[
B\equiv\sigma\varepsilon g.
\]

与 (4.3) 比较：

\[
\delta c_u^{-1}
\equiv
(\sigma\varepsilon-1)g.
\tag{4.5}
\]

左边是 unit，因此右边不能为零。于是

\[
\boxed{\sigma\varepsilon=-1.}
\tag{4.6}
\]

这立即给出本文主 selector：

\[
\boxed{
\begin{array}{c|c}
e_3&\varepsilon\\ \hline
1&+1\\
3&-1
\end{array}}
\tag{4.7}
\]

也即

\[
\boxed{
e_3=1\Longrightarrow\text{positive high-2 slot},}
\tag{4.8}
\]

\[
\boxed{
e_3=3\Longrightarrow\text{negative high-2 slot}.}
\tag{4.9}
\]

所以 `f`-contact 并不是一个可同时出现在两张 Gaussian sheets 上的自由异常；它严格选中其中一张。

---

## 5. 同时固定三个 source-unit phases

由 (4.6)，`sigma epsilon=-1`，所以 (3.3) 进一步给

\[
\boxed{B\equiv-g\pmod3.}
\tag{5.1}
\]

而 (4.5) 化成

\[
\delta c_u^{-1}\equiv g,
\]
故

\[
\boxed{gc_u\equiv\delta=(-1)^{m-\eta}\pmod3.}
\tag{5.2}
\]

再由 `f=gomega+c_u≡0 mod3`：

\[
\boxed{
\omega\equiv-\delta
=(-1)^{m-\eta+1}\pmod3.}
\tag{5.3}
\]

因此 general `a_2`-shallow `f`-contact 不仅选择 slot，还把

\[
(c_Q5^d,\ gc_u,\ \omega)
\]

的全部 first `3`-adic unit phase固定下来。

用 `S=2^{M+m+1}gc_Q5^d`、`beta=Somega` 还可校验

\[
S\equiv\delta,
\qquad
\boxed{\beta\equiv-1\pmod3.}
\tag{5.4}
\]

这与 §16.11 已有 `3∤beta` 完全一致，而不是新的矛盾；故本文不把 (5.4) 误写成 closure。

---

## 6. `eta=1` 旧异常成为立即推论

`fixed3-exception-collapse.md` 中 `eta=1` 唯一 odd-`3` survivor 是

\[
(d,c_Q,k_h,slot)=(2,7,3,-).
\tag{6.1}
\]

这里

\[
e_3=v_3(k_h)=1,
\qquad
\varepsilon=-1.
\]

但 (4.7) 对 `e_3=1` 强迫 `epsilon=+1`。矛盾。

因此旧结论

\[
\boxed{
\eta=1,\ a_2\text{-shallow}
\Longrightarrow 3\nmid f}
\tag{6.2}
\]

现在不再依赖该单点的专门 high-factor 数值 `3g^2/2`；它只是 general orientation selector 的一个特例。

---

## 7. revised fixed-`3` frontier

`a_2`-shallow `f`-contact 的一般开放集从

\[
\eta\ge2,\quad e_3\in\{1,3\},\quad\varepsilon\in\{\pm1\}
\]

严格缩成

\[
\boxed{
\begin{cases}
e_3=1,\ \varepsilon=+1,\\
\text{or}\\
e_3=3,\ \varepsilon=-1,
\end{cases}}
\tag{7.1}
\]

并附带 (5.1)–(5.4) 的完整 mod-`3` source phase。

这还不是空集。后续若继续局部关闭该 sheet，应把 (5.1)–(5.4) 与 `endpoint-lattice.md` 的 high-2 slot natural representative、`C` phase 或 Gaussian composition identity 联立，而不是继续机械提升 `f mod 9`。

另一方面，`a_3`-shallow residual

\[
3\mid f,
\qquad
v_3(2K-9)=2
\]

在一般情形确实可以使 third-order parent获得 odd `3`-depth；因此全局闭环不能要求“fixed 3 永远为偶”。正确的终局接口必须允许 `3` 支付 third-order spill，再从 `3∤widehat{T}_2` 与 old-pool support separation中强迫一枚独立 non-`3` inert supplier。

A2 仍为 `待证`。

---

## 8. verification

```bash
uv run python scripts/exact-lift/a2-only/research-checks/crt-descent/check_a2_fixed3_f_contact_orientation.py
```

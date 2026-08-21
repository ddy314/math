# A1 minimal diagonal: single-5 low-edge collapse by small odd supply

> 日期：2026-08-22。
>
> 依赖：`deep-single5-decimal-height-collapse.md`、`deep-denominator-ledger.md` 中 universal factorization、`sharp-positive-tail-window`。
>
> 范围：minimal diagonal `k=g>=32` 的唯一 surviving single-5 low edge
> \[
> (z,w)=(1,4),\qquad \lambda_2=1,\qquad B=k+1.
> \]

状态：**已严格完成。本文关闭整个 single-5 low edge。**

---

## 1. low-edge 数据

令

\[
T=10^k.
\]

当前 cell 有

\[
D_{\rm gap}=5^{k+1},
\qquad
\lambda=2,
\qquad
w=4.
\]

normalized positive gap 写成

\[
\Gamma=10^k(N_0-\rho),
\qquad
15.09<\Gamma<39.003,
\tag{1}
\]

且

\[
\frac T{10}\le N_0\le T.
\tag{2}
\]

odd supply 写

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1,
\tag{3}
\]

其中 `q,s` 与 5 互素。

single-5 gap identity 为

\[
5^{k+1}TN_0-\gamma=2h,
\qquad
\Gamma=\frac{\gamma}{5^{k+1}}.
\tag{4}
\]

所以

\[
\boxed{
2h=5^{k+1}(TN_0-\Gamma).
}
\tag{5}

---

## 2. 构造只有 `O(T)` 大小的两个 supply carriers

minimal diagonal 中

\[
b_1=10T^2-w=10T^2-4.
\]

`deep-single5-decimal-height-collapse.md` 已证明该 low edge 的 decimal recovery height 为

\[
n_3=B+k=2k+1.
\]

因此

\[
10^{n_3}=10^{2k+1}=10T^2,
\qquad
b_3=10T^2\rho.
\]

定义整数

\[
\boxed{R:=b_1N_0-b_3.}
\tag{6}
\]

由 `b1=10T^2-4` 与 `rho=N0-Gamma/T`：

\[
\begin{aligned}
R
&=(10T^2-4)N_0-10T^2\rho\\
&=10T^2(N_0-\rho)-4N_0\\
&=\boxed{10T\Gamma-4N_0}.
\end{aligned}
\tag{7}

所以看似由巨大十进制块构成的 `R` 实际只有 `O(T)` 大小。

---

## 3. universal factorization 强迫 `q,s` 分别进入两个小整数

universal factorization 在任意 deep state 给

\[
X_1=10\gamma T-wD_{\rm gap}N_0=sa,
\]

\[
X_2=100\gamma T-(10w-1)D_{\rm gap}N_0=qb
\]

对某些正整数 `a,b`。

在当前 `w=4`,`D_gap=5^{k+1}` 中，由 `gamma=5^{k+1}Gamma` 与 (7)：

\[
X_1
=5^{k+1}(10\Gamma T-4N_0)
=5^{k+1}R.
\tag{8}
\]

而

\[
\begin{aligned}
X_2
&=5^{k+1}(100\Gamma T-39N_0)\\
&=5^{k+1}\bigl(10(10\Gamma T-4N_0)+N_0\bigr)\\
&=5^{k+1}(10R+N_0).
\end{aligned}
\tag{9}

因为 `q,s` 都是 5-adic units，(8)-(9) 分别给

\[
\boxed{s\mid R,}
\tag{10}
\]

\[
\boxed{q\mid10R+N_0.}
\tag{11}
\]

于是

\[
\boxed{h=qs\le R(10R+N_0).}
\tag{12}
\]

---

## 4. small-supply 上界

由 (1)-(2) 与 (7)：

\[
R
<10(39.003)T
=390.03T.
\tag{13}
\]

同时 `R>0`，因为 `X1=sa>0`。

于是

\[
10R+N_0
<3900.3T+T
=3901.3T.
\tag{14}
\]

由 (12)：

\[
\boxed{
h<390.03\cdot3901.3\,T^2.}
\tag{15}
\]

而

\[
390.03\cdot3901.3=1,521,623.139<1,522,000.
\]

故可取整洁安全上界

\[
\boxed{h<1,522,000\,T^2.}
\tag{16}
\]

---

## 5. gap identity 给指数级下界

由 (2)：

\[
TN_0\ge\frac{T^2}{10}.
\]

当前 `k>=32`，所以 `T^2` 极大；特别有

\[
\frac{T^2}{10}-39.003>\frac{T^2}{11}.
\]

结合 `Gamma<39.003`：

\[
TN_0-\Gamma>\frac{T^2}{11}.
\tag{17}
\]

代入 (5)：

\[
\boxed{
h>\frac{5^{k+1}}{22}T^2.}
\tag{18}
\]

而在 `k=10` 已有

\[
\frac{5^{11}}{22}>2,219,000>1,522,000,
\]

且左侧随 `k` 严格增长。因此对当前全部 `k>=32`：

\[
\frac{5^{k+1}}{22}>1,522,000.
\tag{19}
\]

(16) 与 (18)-(19) 矛盾。

因此

\[
\boxed{
(z,w)=(1,4),\ \lambda_2=1,\ B=k+1
\quad\Longrightarrow\quad\varnothing.
}
\tag{20}

---

## 6. consequence

`deep-single5-decimal-height-collapse.md` 已证明：除本文 low edge 外，single-5 只剩

\[
\boxed{\lambda_2=2k-1}
\]

的 top-edge sign-allocation branch。

本文关闭 low edge，所以当前 minimal-diagonal single-5 frontier 已缩为唯一 top edge。

注意本文的 small-supply bound **只依赖当前 `B=k+1`**：此时可以从 (8)-(9) 合法约去完整 `5^{k+1}`。对一般 top edge `B>k+1`，不能把同一上界直接照搬；必须只约去 `X1,X2` 实际具有的 5-adic depth。
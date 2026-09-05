# DD `Z_0` residual 的 two-sheet simultaneous payer collapse

> **依赖：** [`tail-rough-general-transfer`](tail-allocation-ledger.md#source-tail-rough-general-transfer)、
> [`tail-rough-canonical-payer-decomposition`](tail-allocation-ledger.md#source-tail-rough-canonical-payer-decomposition)、
> [`tail-rough-projective-bottom-two-payer`](tail-allocation-ledger.md#source-tail-rough-projective-bottom-two-payer)、
> [`tail-rough-z0-only-frontier`](tail-allocation-ledger.md#source-tail-rough-z0-only-frontier)。
>
> **严格状态：** `已严格完成（整个 post-tail X_Q odd rough support）`。
>
> `Z_0`-only frontier 仍把剩余 loss 写成一个抽象的
> \[
> X_Z\mid\gcd(C_Q,Z_0).
> \]
> 本文继续使用 canonical payer 的局部约束，证明 `X_Z` 的每个 prime-power 实际只能进入两个
> 互斥 sheet：
>
> 1. **third / bottom-covered sheet**：gap payer 与 `Z_0` residual 的乘积一起由
>    `R_3^{\rm den}` 支付；
> 2. **norm-overflow sheet**：bottom payer 已经饱和，bottom + gap + `Z_0` residual
>    三者的乘积一起由 `N_0` 支付。
>
> 因而 `X_Z` 可进一步写成互素 support factorization
> \[
> \boxed{X_Z=X_{Z,3}X_{Z,N},\qquad (X_{Z,3},X_{Z,N})=1,}
> \]
> 且
> \[
> \boxed{
> X_{Z,3}\mid\operatorname{core}_{10}\!\left(
> \frac{R_3^{\rm den}}{(R_3^{\rm den},a)}
> \right),
> }
> \]
> \[
> \boxed{
> X_{Z,N}\mid\operatorname{core}_{10}\!\left(
> \frac{N_0}{(N_0,Ca)}
> \right).
> }
> \]
> 这把此前的 `gcd(C_Q,Z_0)` hard object 压成两个已经扣除了既有 payer 容量的
> **exact quotient readers**。

---

## 1. local data

固定 odd rough prime
\[
p^x\Vert X_Q.
\]
沿用 canonical payer 记号
\[
t:=v_p(C),
\qquad
r:=v_p(R_3^{\rm den}),
\]
\[
g:=v_p(g_n),
\qquad
\omega:=v_p(N_{\rm ang}),
\]
其中
\[
g_n=(a_1,a_2),
\qquad
N_0=g_n^2N_{\rm ang}.
\]
所以
\[
\boxed{v_p(N_0)=2g+\omega.}
\tag{1.1}
\]
记
\[
n:=2g+\omega.
\]
`tail-rough-general-transfer` 与 Gaussian split 已严格给出
\[
\boxed{g\le t,}
\tag{1.2}
\]
以及
\[
\boxed{x\le\max(t,n,r).}
\tag{1.3}
\]

canonical decomposition 首先取
\[
e_3=\min(x,r),
\]
再取
\[
e_B=\min(x-e_3,t).
\]
把非 bottom 的 projective payer 深度记为
\[
\boxed{e_P:=x-e_B.}
\tag{1.4}
\]
这与 two-payer theorem 的
\[
X_Q=X_PX_B
\]
逐 prime 一致。

最后令
\[
\alpha:=v_p(a),
\]
并按 `Z_0`-only frontier 做 gap / projective denominator split：
\[
e_a:=\min(e_P,\alpha),
\qquad
\boxed{e_Z:=e_P-e_a=(e_P-\alpha)_+.}
\tag{1.5}
\]

---

## 2. hidden max-payer inequality

### Lemma 2.1

在上述条件下，
\[
\boxed{
 e_P\le\max(r,n-t).
}
\tag{2.1}
\]

### Proof

分两种互斥情况。

#### Sheet T: `x<=r+t`

若 `x<=r`，则
\[
e_3=x,
\qquad e_B=0,
\qquad e_P=x\le r.
\]

若
\[
r<x\le r+t,
\]
则
\[
e_3=r,
\qquad
x-e_3=x-r\le t,
\]
所以
\[
e_B=x-r,
\qquad
\boxed{e_P=x-e_B=r.}
\tag{2.2}
\]

因此整个 Sheet T 都有
\[
\boxed{e_P\le r.}
\tag{2.3}
\]

#### Sheet N: `x>r+t`

此时同时有
\[
x>r,
\qquad x>t.
\]
于是 `(1.3)` 中 `r,t` 都无法达到 `x`，只能由 `n` 支付：
\[
\boxed{x\le n.}
\tag{2.4}
\]
又因为
\[
e_3=r,
\qquad x-r>t,
\]
所以 bottom payer 饱和：
\[
\boxed{e_B=t.}
\tag{2.5}
\]
从而
\[
\boxed{
 e_P=x-t\le n-t.
}
\tag{2.6}
\]

`(2.3)` 与 `(2.6)` 合并即得 `(2.1)`。∎

---

## 3. `Z_0` residual 的 sharpened local bound

由 `(1.5)` 与 `(2.1)`：
\[
\begin{aligned}
e_Z
&=(e_P-\alpha)_+\\
&\le
\left(\max(r,n-t)-\alpha\right)_+\\
&=
\max\!\left(
(r-\alpha)_+,
(n-t-\alpha)_+
\right).
\end{aligned}
\]
因此
\[
\boxed{
 e_Z\le
 \max\!\left(
 (r-\alpha)_+,
 (2g+\omega-t-\alpha)_+
 \right).
}
\tag{Z0-max-payer}
\]

这严格强于只使用 stereographic denominator formula 得到的安全界
\[
e_Z\le(r+g+\omega-\alpha)_+.
\]
尤其这里 `r` 与 `g+\omega` 不再按和式重复出现；第二个分支还额外扣除了 bottom coefficient
深度 `t`。

---

## 4. 两个 exact quotient readers

定义
\[
R_{3/a}
:=
\frac{R_3^{\rm den}}{(R_3^{\rm den},a)}.
\]
则
\[
\boxed{
v_p(R_{3/a})=(r-\alpha)_+.
}
\tag{4.1}
\]

再定义
\[
N_{0/(Ca)}
:=
\frac{N_0}{(N_0,Ca)}.
\]
由于
\[
v_p(Ca)=t+\alpha,
\]
有
\[
\boxed{
v_p(N_{0/(Ca)})=(2g+\omega-t-\alpha)_+.
}
\tag{4.2}
\]

现在按 Lemma 2.1 的两个 sheet 分割 `X_Z` 的 prime support：

- 若 `x<=r+t`，把该 prime 的 `p^{e_Z}` 放入 `X_{Z,3}`；
- 若 `x>r+t`，把该 prime 的 `p^{e_Z}` 放入 `X_{Z,N}`。

两类 support 互斥，所以
\[
\boxed{
X_Z=X_{Z,3}X_{Z,N},
\qquad
(X_{Z,3},X_{Z,N})=1.
}
\tag{4.3}
\]

在 Sheet T，由 `(2.3)`：
\[
e_a+e_Z=e_P\le r.
\]
特别地
\[
e_Z\le(r-\alpha)_+,
\]
故
\[
\boxed{
X_{Z,3}\mid\operatorname{core}_{10}(R_{3/a}).
}
\tag{4.4}
\]

在 Sheet N，由 `(2.5)` 与 `(2.4)`：
\[
e_B=t,
\]
并且
\[
 e_B+e_a+e_Z
 =t+e_P
 =x
 \le n=v_p(N_0).
\]
因此有更强的 simultaneous product relation
\[
\boxed{
X_{B,N}X_{a,N}X_{Z,N}
\mid\operatorname{core}_{10}(N_0),
}
\tag{4.5}
\]
其中 `X_{B,N},X_{a,N}` 表示 `X_B,X_a` 在 Sheet N support 上的对应 factors。
特别地由 `(4.2)`：
\[
\boxed{
X_{Z,N}\mid\operatorname{core}_{10}(N_{0/(Ca)}).
}
\tag{4.6}
\]

同理 Sheet T 还保留
\[
\boxed{
X_{a,T}X_{Z,3}
\mid\operatorname{core}_{10}(R_3^{\rm den}).
}
\tag{4.7}
\]

`(4.5)` 与 `(4.7)` 是本条结果相较单独 divisibility 更重要的部分：它们记录了同一 prime
上的 payer 已经消耗了多少 reader 深度，后续做 height LP 时不能再次把这些深度当成独立预算。

---

## 5. inert / split Gaussian refinement

若
\[
p\equiv3\pmod4,
\]
primitive sum of two squares 给
\[
\omega=0.
\]
于是 Sheet N 上
\[
 e_Z
 \le(2g-t-\alpha)_+
 \le(g-\alpha)_+,
\]
这里最后一步用了 `g<=t`。因此
\[
\boxed{
 p\equiv3\pmod4,\ p\mid X_{Z,N}
 \Longrightarrow
 g>\alpha.
}
\tag{5.1}
\]
也就是说，inert rough prime 若还能留在 norm-overflow `Z_0` residual 中，只能来自
**common-numerator depth 超过 gap depth** 的部分；deep primitive Gaussian angle 完全不参与。

真正的 angular excess 仍只可能出现在
\[
p\equiv1\pmod4
\]
的 split Gaussian primes。这与 general projective/common-scale 与 angular 分开处理的后续方向一致。

---

## 6. 对 `Z_0`-only frontier 的更新

此前唯一 hard object 写成
\[
X_Z\mid\gcd(C_Q,Z_0).
\]
现在可以进一步替换为
\[
\boxed{
X_Z=X_{Z,3}X_{Z,N},
}
\]
其中
\[
\boxed{
X_{Z,3}\mid
\operatorname{core}_{10}\!\left(
\frac{R_3^{\rm den}}{(R_3^{\rm den},a)}
\right),
}
\]
\[
\boxed{
X_{Z,N}\mid
\operatorname{core}_{10}\!\left(
\frac{N_0}{(N_0,Ca)}
\right).
}
\]
并且 norm-overflow support 上 bottom payer 自动饱和，满足 simultaneous relation `(4.5)`。

因此下一步 height 工作应直接研究：

1. `R_3^{den}` 在扣除 sphere-gap `a` 后还能剩多少 rough height；
2. `N_0` 在同一 prime 上先扣除 coefficient `C` 与 gap `a` 后还能剩多少 rough height；
3. split primes 的第二项如何与 pure numerator Gaussian orientation / coefficient circle 联合。

继续把整个 `gcd(C_Q,Z_0)` 当成一个高度至多 `S` 的匿名整数，会丢失 `(4.5)` 与 `(4.7)` 的
simultaneous charging 信息。

---

## 7. verification scope

对应的有限代数审计脚本：

```bash
uv run python scripts/exact-lift/double-deficit/research-checks/tail-allocation/check_dd_tail_rough_z0_two_sheet.py
```

脚本枚举有限范围内所有满足
\[
g\le t,
\qquad
x\le\max(t,2g+\omega,r)
\]
的抽象 valuation tuples，并核对 `(2.1)`、两个 sheet 的 simultaneous product inequalities 与
`Z0-max-payer`。

该脚本只是对上面的无界代数证明做有限一致性审计；严格结论来自 §§2--4 的逐情况推导。

---

## 8. 状态摘要

- **`已严格完成`**：hidden max-payer inequality `(2.1)`。
- **`已严格完成`**：`Z0-max-payer`。
- **`已严格完成`**：two-sheet support factorization `(4.3)` 与 exact quotient readers `(4.4),(4.6)`。
- **`已严格完成`**：Sheet N simultaneous product `(4.5)`、Sheet T simultaneous product `(4.7)`。
- **`已严格完成`**：odd inert refinement `(5.1)`。
- **`待证`**：两个 quotient readers 的 global simultaneous height bound；由此改进 `Triple-bootstrap` 并完成 non-canonical DD reoptimization。

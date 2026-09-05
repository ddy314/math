# DD frontier: source/orientation Euclidean quotient 的临界审计

> 日期：2026-08-22
>
> 作用域：假想 corrected `6.308883...` terminal one-channel frontier。
>
> 本文把
> \[
> |\Pi|/q_c=10^{(1/2-z_*)S+o(S)}
> \]
> 的实数高度差实现为真正的 Gaussian integer quotient，并审计其是否产生 strict surplus。

## 1. secondary Gaussian factorization

terminal secondary line写成

\[
\boxed{
\Pi\Delta_1=Pq_c-iI,
}
\tag{1.1}
\]

其中

\[
P:=A_*2^{m-2},
\qquad
I:=B_*5^{2T-m},
\]

且

\[
\log|A_*|,\log|B_*|=o(S).
\]

terminal heights为

\[
\log|\Pi|=\frac12S+o(S),
\qquad
\log q_c=z_*S+o(S),
\]

\[
z_*=0.308883577618\ldots,
\]

\[
\log|\Delta_1|
=0.654441788809\ldots S+o(S),
\]

\[
\log P
=0.845558211191\ldots S+o(S),
\]

\[
\log I
=0.654441788809\ldots S+o(S).
\]

因此

\[
\log(Pq_c)-\log I
=\frac12S+o(S).
\tag{1.2}
\]

## 2. Gaussian Euclidean division

在 `Z[i]` 中对 `Pi` 除以 rational integer `q_c`：存在

\[
K,\varrho\in\mathbf Z[i]
\]

使

\[
\boxed{
\Pi=q_cK+\varrho,
\qquad
N(\varrho)\le\frac12q_c^2.
}
\tag{2.1}
\]

由于

\[
|\Pi|/q_c
=10^{\rho_*S+o(S)},
\qquad
\rho_*:=\frac12-z_*,
\]

得到

\[
\boxed{
\log|K|=\rho_*S+o(S),
\qquad
\rho_*=0.191116422382\ldots.
}
\tag{2.2}
\]

这给 `rho_*` 一个真正 integral 的 realization；后续不需要把 `Pi/q_c` 当作形式商。

## 3. exact Euclidean remainder identity

将 `(2.1)` 代入 `(1.1)`：

\[
(q_cK+\varrho)\Delta_1=Pq_c-iI.
\]

移项：

\[
\boxed{
q_cE_\rho
=\varrho\Delta_1+iI,
}
\tag{Euclid-transfer}
\]

其中

\[
\boxed{
E_\rho:=P-K\Delta_1\in\mathbf Z[i].
}
\tag{3.1}
\]

因此 `source/orientation quotient` 确实产生一个新的 integral remainder coordinate。

## 4. `E_rho` 非零

反设

\[
E_\rho=0.
\]

则

\[
K\Delta_1=P
\]

并由 `(Euclid-transfer)`：

\[
\varrho\Delta_1=-iI.
\]

因此 `Delta_1` 在 `Z[i]` 中同时整除两个 rational integers `P` 与 `I`。

但 `P` 与 `I` 的主 smooth parts分别来自互异 decimal primes：

\[
P=A_*2^{m-2},
\qquad
I=B_*5^{2T-m}.
\]

它们的非 decimal coefficient overlap只有 `10^{o(S)}` 高度。因此任何 Gaussian integer同时整除 `P,I`，其 norm只有 `10^{o(S)}` 的 nontrivial height。

另一方面

\[
\boxed{
N(\Delta_1)
=10^{1.308883577618\ldots S+o(S)}.
}
\]

矛盾。故

\[
\boxed{E_\rho\ne0.}
\tag{Euclid-nonzero}
\]

## 5. Archimedean size：恰好临界

由 `(Euclid-transfer)` 与 `(2.1)`：

\[
|E_\rho|
\le
\frac{|\varrho||\Delta_1|+I}{q_c}.
\]

因为

\[
|\varrho|\ll q_c,
\]

且

\[
\log I=\log|\Delta_1|+o(S),
\]

得到

\[
\boxed{
\log|E_\rho|
\le
0.654441788809\ldots S+o(S).
}
\tag{5.1}
\]

这正好等于 `|Delta_1|` 的 leading height；Euclidean division本身没有产生 strict saving。

同样从定义

\[
E_\rho=P-K\Delta_1
\]

可见两个主项高度都为

\[
\begin{aligned}
\log P
&=0.845558211191\ldots S+o(S),\\
\log|K\Delta_1|
&=(0.191116422382+0.654441788809)S+o(S)\\
&=0.845558211191\ldots S+o(S).
\end{aligned}
\]

所以 `(3.1)` 是一份精确 `rho_*S` 级 Archimedean cancellation，但 remainder仍处在 `Delta_1` 本身的尺度。

## 6. source 与 secondary norm 的 gcd 只有次线性高度

取 `(1.1)` 的 norm：

\[
\boxed{
C_LN(\Delta_1)=P^2q_c^2+I^2.
}
\tag{6.1}
\]

因为

\[
(C_L,q_c)=1
\]

在 main core上成立，若 rational prime-power进入

\[
(q_c,N(\Delta_1)),
\]

则由 `(6.1)` 它必须同时进入 `I^2`。但 `I=B_*5^{2T-m}`，而 equality rigidity使 `q_c` 的 decimal-prime overlap只有 `o(S)`，`B_*` 也只有 `o(S)` 高度。因此

\[
\boxed{
\log(q_c,N(\Delta_1))=o(S).
}
\tag{6.2}
\]

同理，若 prime同时进入 `P` 与 `N(Delta_1)`，由 `(6.1)` 它也必须进入 `I`；而 `(P,I)` 只有 coefficient / decimal exceptional overlap。因此

\[
\boxed{
\log(P,N(\Delta_1))=o(S).
}
\tag{6.3}
\]

所以 modulo `q_c`，`Delta_1` 在 main mass上可逆，而 `(Euclid-transfer)` 只是固定 `varrho` 的 residue：

\[
\varrho\Delta_1\equiv-iI\pmod{q_c}.
\]

这没有再给 `E_rho` 一个正线性 divisor。

## 7. 方法结论

`rho_*` 高度差确实可以 integralize：

\[
\Pi=q_cK+\varrho,
\qquad
\log|K|=\rho_*S+o(S).
\]

但对应的新 integer

\[
E_\rho=P-K\Delta_1
\]

满足：

- `E_rho != 0`；
- `|E_rho|` 最坏仍与 `|Delta_1|` 同尺度；
- `q_c` 与 `N(Delta_1)` 只有次线性 gcd；
- 因而 Euclidean quotient没有自动生成新的 positive-linear divisor。

所以当前证据支持：

\[
\boxed{
\text{source/orientation Euclidean quotient 是一条真实但临界的 Gaussian continued-fraction step。}
}
\]

若后续没有额外 global prime-support theorem作用于 `K` 或 `E_rho`，继续迭代普通 Euclidean division不会产生 strict-gap surplus。

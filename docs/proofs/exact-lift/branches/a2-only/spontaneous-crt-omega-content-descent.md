# A2 omega-content / descendant common overlap 的唯一 top-defect residue

> **依赖：** `spontaneous-omega-content-common.md`、`spontaneous-omega-biquadratic.md`、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-descended-quotient-orientation.md`。
>
> **严格状态：**omega-content common prime满足 `p|omega`，因而 `alpha=beta=0 mod p`，但一般不进入 `W_q` height。本文把 source triangle与全局 quotient `qW_q=DK-N` 代入 descended quotient，消去 `W_q,H_0`。非central branch中，真实 top defect `delta=C/D` 被 `K` 唯一确定；乘回整数得到正 natural carrier `H_{omega Delta}`。central branch `2K-9=0` 与 descendant equation只可能在 fixed non-3 prime `7` 相交。本文没有排除 simple p-adic wrapping，因此不关闭 A2。

---

## 1. omega-content first layer

固定 genuine odd non-`3` inert prime

\[
p\mid\omega.
\]

由

\[
\alpha=TK+a_3=\omega W_q,
\qquad
\beta=TQ+b_3=\omega S
\]
有

\[
\boxed{\alpha\equiv\beta\equiv0\pmod p.}
\tag{1.1}

`spontaneous-omega-content-common.md` 已证明 omega-content 与 denominator/source-discriminant 分离：

\[
\boxed{p\nmid qf c_u gT.}
\tag{1.2}

source triangle为

\[
z=g\omega-c_u=q5^\lambda.
\]
所以模 `p|omega`：

\[
\boxed{q5^\lambda\equiv-c_u\pmod p.}
\tag{1.3}

---

## 2. height value becomes a rational defect expression

全局 height quotient为

\[
qW_q=DK-N,
\qquad
H_0=c_uW_q.
\]

由 (1.3) 且 `q` 为 unit：

\[
\frac{c_u}{q}\equiv-5^\lambda\pmod p.
\]

因此

\[
H_0
=c_u\frac{DK-N}{q}
\equiv
-5^\lambda(DK-N)
\pmod p.
\tag{2.1}

又

\[
D=g2^m5^d,
\qquad
T=2^m5^{\lambda+d},
\]
故

\[
\boxed{gT=D5^\lambda.}
\tag{2.2}

所有量在 p 处为 unit，可除得

\[
\frac{H_0}{gT}
\equiv
-\frac{DK-N}{D}
\pmod p.
\]

写

\[
\delta:=\frac CD,
\qquad
N=3D-C=D(3-\delta),
\]
于是

\[
\boxed{
\frac{H_0}{gT}
\equiv3-K-\delta
\pmod p.}
\tag{2.3}

所以 omega-content虽然不令 `H_0=0`，但把它完全恢复成 `(K,delta)` 的线性式。

---

## 3. descended common equation fixes `delta`

fully primitive descended quotient满足 exact identity

\[
\boxed{
16\mathscr F_{63}
=3gT G_D(K)
-16(2K-9)(g\alpha+H_0),}
\tag{3.1}

其中

\[
\boxed{G_D(K)=11K^2-240K+432.}
\tag{3.2}

若同一个 omega-content prime还进入 descendant common gcd，则

\[
p\mid\widehat{\mathscr D}_{63}
\Longrightarrow
p\mid\mathscr F_{63}.
\]

利用 `alpha=0` 与 (2.3)，除去 unit `gT`：

\[
\boxed{
3G_D(K)
-16(2K-9)(3-K-\delta)
\equiv0\pmod p.}
\tag{3.3}

若

\[
2K-9\not\equiv0\pmod p,
\]
则 top defect residue唯一：

\[
\boxed{
\delta
\equiv
3-K-
\frac{3G_D(K)}{16(2K-9)}
\pmod p.}
\tag{3.4}

完全化简为

\[
\boxed{
\delta
\equiv
\frac{-65K^2+960K-1728}
{16(2K-9)}
\pmod p.}
\tag{3.5}

所以 simple omega-content root一旦给定 `K mod p`，descendant common condition不再留下独立的 `C/D` first digit。

---

## 4. positive natural representative

将 (3.5) 乘回 `D`，定义 ordinary integer

\[
\boxed{
\mathscr H_{\omega\Delta}
:=D(65K^2-960K+1728)
+16C(2K-9).}
\tag{4.1}

每个 noncentral omega-content/descent common prime都满足

\[
\boxed{p\mid\mathscr H_{\omega\Delta}.}
\tag{4.2}

真实 endpoint中

\[
K>9\cdot10^{11},
\qquad
D>0,
\qquad C>0.
\]

并且

\[
65K^2-960K+1728>0,
\qquad
2K-9>0,
\]
所以

\[
\boxed{\mathscr H_{\omega\Delta}>0.}
\tag{4.3}

粗尺度为

\[
\boxed{
65DK^2-960DK
<\mathscr H_{\omega\Delta}
<66DK^2}
\tag{4.4}

对当前 huge K成立；右端使用 `C<D` 与低阶项被 `DK^2` 吸收。

这不是小到能单独排除 p-adic wrapping，但它给 content/descent common support一个 explicit natural representative，而不是未命名的 resultant。

---

## 5. Archimedean direction is opposite to the real endpoint

把 (3.5) 的右边当作实函数

\[
\delta_{\omega\Delta}(K)
:=
\frac{-65K^2+960K-1728}{16(2K-9)}.
\]

对 `K>9*10^11`：numerator严格为负、denominator严格为正，所以

\[
\boxed{\delta_{\omega\Delta}(K)<0.}
\tag{5.1}

而真实 finite-defect endpoint满足

\[
\boxed{0<\delta=C/D<3/250.}
\tag{5.2}

因此 omega-content/descent common root不可能来自真实邻域中的实交点：

\[
\boxed{
\text{every such common root is genuinely p-adic wrapping}.}
\tag{5.3}

这与 `spontaneous-omega-biquadratic.md` 中 content roots本身避开真实 numerator window的结论方向一致，但二者是不同的 Archimedean separation：这里直接发生在 top defect `C/D`。

---

## 6. central branch is only fixed `7`

现在考虑

\[
2K-9\equiv0\pmod p.
\]

由 descendant equation (3.3)，第二项消失，所以还必须

\[
G_D(K)\equiv0\pmod p.
\]

resultant：

\[
\boxed{
\operatorname{Res}_K(G_D,2K-9)
=-1701
=-3^5\cdot7.}
\tag{6.1}

在 genuine non-`3` sector：

\[
\boxed{p=7.}
\tag{6.2}

因此 noncentral formula (3.5) 唯一的 denominator exception不是 moving branch，只是 fixed `7`。

该 fixed `7` 是否实际满足 omega-content pure-prefix curve需要单独 finite/Hensel审计；本文不据 (6.2) 自动宣称存在或不存在。

---

## 7. revised alpha-supported content frontier

omega-content + descendant common 现在具有以下规范形式：

- pure-prefix content root仍由 `C_omega=J_H=0` / biquadratic tower读取；
- noncentral descendant condition唯一确定
  \[
  C/D\pmod p;
  \]
- common prime必须进入 positive natural carrier `H_{omega Delta}`；
- real endpoint与 required defect residue方向相反，所以只有 p-adic wrapping；
- central branch只剩 fixed `7`。

这删除了 omega-content descendant overlap中的一个自由 local coordinate，但尚未排除 simple moving content primes。下一步应把 (3.5) 与 content biquadratic的 decimal orbit `tau=10^{-M}` 联立，或对 fixed `7` 做完整 content-state audit。

A2 仍为 `待证`。

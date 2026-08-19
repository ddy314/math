# A2 `H_4` short prefix carrier 的 exact 2-adic parity

> **依赖：** `spontaneous-crt-pure-h4-short-carrier.md`、deep-even primitive reduction。
>
> **严格状态：**generic low coefficient singularity由 ordinary integer `V_4^int` 读取，且真实值严格为负。本文审计其完整二进 content：七项中唯一最低层是 `129600A^2N^2`，所以 `v_2(V_4^int)=2M+6`，primitive unit为 `1 mod8`。取正 carrier `H_V4=-V_4^int` 后 primitive orientation变成 `7 mod8`，因此每个 generic `H_4` singular candidate都伴随一份 odd-inert parity。本文没有证明这份 parity不能由原 singular prime自身支付，因此不关闭 A2。

---

## 1. integer short carrier

沿用

\[
N=10^M,
\qquad A=a_2,
\qquad B=b_2.
\]

前一文件得到

\[
\boxed{
\begin{aligned}
V_4^{int}={}&
656100B^4+2624400B^3N\\
&-7710100B^2A^2-13936500B^2AN\\
&-3647025B^2N^2+129600BA^2N\\
&+129600A^2N^2.
\end{aligned}}
\tag{1.1}

并且 real endpoint上

\[
\boxed{V_4^{int}<0.}
\tag{1.2}

所以定义 positive carrier

\[
\boxed{H_{V4}:=-V_4^{int}>0.}
\tag{1.3}

---

## 2. exact binary depths of the prefix blocks

当前 deep-even normal form给

\[
\boxed{v_2(N)=M,}
\tag{2.1}

\[
\boxed{B=2^{M+m+1}c_ug,}
\]
且

\[
g=2^{t-1}\rho,
\qquad c_u,\rho\text{ odd}.
\]
因此

\[
\boxed{v_2(B)=M+m+t.}
\tag{2.2}

primitive prefix中 `B` 为偶数，所以

\[
\boxed{A\text{ odd}.}
\tag{2.3}

同时 coefficient depths为

\[
v_2(656100)=2,
\qquad
v_2(2624400)=4,
\]

\[
v_2(7710100)=v_2(13936500)=2,
\]

\[
v_2(3647025)=0,
\qquad
\boxed{v_2(129600)=6.}
\tag{2.4}

---

## 3. the last term is uniquely shallowest

七项二进深度分别至少为

\[
2+4(M+m+t),
\]

\[
4+3(M+m+t)+M,
\]

\[
2+2(M+m+t),
\]

\[
2+2(M+m+t),
\]

\[
2(M+m+t)+2M,
\]

\[
6+(M+m+t)+M,
\]

和

\[
\boxed{6+2M}
\tag{3.1}

对应最后一项 `129600A^2N^2`。

因为 dangerous branch有

\[
m\ge5,
\qquad t\ge3,
\]
其它六项都严格高于 `2M+6`。故不存在 lowest-layer cancellation：

\[
\boxed{v_2(V_4^{int})=2M+6.}
\tag{3.2}

---

## 4. primitive unit modulo 8

除以 `2^{2M+6}` 后，模 `8` 只剩最后一项：

\[
\frac{V_4^{int}}{2^{2M+6}}
\equiv
\frac{129600}{64}
A^2\left(\frac{N}{2^M}\right)^2
\pmod8.
\]

现在

\[
129600/64=2025\equiv1\pmod8,
\]

\[
A^2\equiv1\pmod8,
\qquad
N/2^M=5^M,
\qquad
5^{2M}\equiv1\pmod8.
\]

所以

\[
\boxed{
\frac{V_4^{int}}{2^{2M+6}}
\equiv1\pmod8.}
\tag{4.1}

但 positive carrier是其相反数，因此

\[
\boxed{
\frac{H_{V4}}{2^{2M+6}}
\equiv-1\equiv7\pmod8.}
\tag{4.2}

---

## 5. odd-inert parity surcharge

定义 odd primitive part

\[
\boxed{
H_{V4}^{\circ}
:=\frac{H_{V4}}{2^{2M+6}}.}
\tag{5.1}

则

\[
H_{V4}^{\circ}>0,
\qquad
H_{V4}^{\circ}\equiv7\pmod8,
\]
特别地

\[
\boxed{H_{V4}^{\circ}\equiv3\pmod4.}
\tag{5.2}

因此 `H_V4^circ` 必含至少一枚

\[
\boxed{r\equiv3\pmod4}
\]
到奇 exponent。

所以 generic low coefficient-singular descendant common branch自身会生成一份 odd-inert parity surcharge。

这还不是 distinct-prime theorem：原 coefficient-singular common prime本身可能同时整除 `H_V4^circ` 并支付该 parity。下一步若要真正加一枚新 prime，需要审计 singular prime在 `V_4^int` 中的 exponent parity，或证明它与 parent descendant common gcd的 relevant inert supplier不能复用。

A2 仍为 `待证`。

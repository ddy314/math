# A2 exact triple saturation 的 third-order parity spill

> **依赖：** `spontaneous-crt-descendant-quartic-tail-hierarchy.md`、`spontaneous-crt-descendant-third-order-balance.md`。
>
> **严格状态：**finite quartic hierarchy证明 third-order positive parent numerator `-N_63^(3)` 的 odd primitive part为 `3 mod4`。本文固定真正未固定化的 terminal moving labels，即 first、second、third tails都恰好饱和一个 baseline `rho=sigma=tau=h`。对每枚这样的 prime，`N_63^(3)` 的 local depth精确为 `4h`，因此该 prime对 third-order parent parity贡献为偶数，并且除去其完整 fourth-power baseline后不再出现。于是所有 exact triple-saturated labels的 baseline fourth power从 positive third carrier约掉以后，quotient仍为 `3 mod4`，必含一枚 odd-inert prime到奇次，而该 supplier严格位于 terminal recycling pool之外。本文尚未排除这枚外部 supplier为 prime `3`，因此只证明 support spill，不宣称新的 non-3 prime或 A2 closure。

---

## 1. exact terminal moving set

固定 genuine common inert labels中仍未被 fixed gates固定化的 local branch：

\[
\boxed{
\rho_p=h_p,
\qquad
\sigma_p=h_p,
\qquad
\tau_p=h_p,}
\tag{1.1}
\]

其中

\[
h_p=v_p(G_\Delta),
\]

\[
\rho_p=v_p(B_{63}),
\qquad
\sigma_p=v_p(C_{63}^{(2)}),
\qquad
\tau_p=v_p(C_{63}^{(3)}).
\]

`rho>h` / `sigma>h` 的进一步 overdepth分别被 fixed `P_110` / `P_148` gates固定化；`tau>h` 的 terminal overdepth首先承担 fixed `-26` character。因此 (1.1) 是 generic moving terminal resonance的 exact triple-saturation core。

令其 prime集合为 `E_term`，定义 baseline product

\[
\boxed{
G_{term}:=
\prod_{p\in E_{term}}p^{h_p}.}
\tag{1.2}

---

## 2. every terminal moving prime enters the third parent to even depth

third tail定义为

\[
\mathscr C_{63}^{(3)}
=-\frac{\mathscr N_{63}^{(3)}}{G_\Delta S_1S_2},
\]

其中

\[
S_1=\gcd(G_\Delta,B_{63}),
\qquad
S_2=\gcd(G_\Delta,C_{63}^{(2)}).
\]

在 (1.1) 的 prime `p` 上：

\[
v_p(S_1)=v_p(S_2)=h_p,
\]
并且

\[
v_p(C_{63}^{(3)})=\tau_p=h_p.
\]

所以 exact：

\[
\boxed{
v_p(-\mathscr N_{63}^{(3)})
=h_p+h_p+h_p+h_p
=4h_p.}
\tag{2.1}

特别地这是偶数。

于是

\[
\boxed{G_{term}^4\mid-\mathscr N_{63}^{(3)}.}
\tag{2.2}

而且对每个 `p in E_term`，(2.1) 是 exact equality，所以约掉 `G_term^4` 后这些 primes完全消失：

\[
\boxed{
\gcd\!\left(
G_{term},
\frac{-\mathscr N_{63}^{(3)}}{G_{term}^4}
\right)=1.}
\tag{2.3}

---

## 3. remove the binary content

quartic hierarchy已经证明

\[
\boxed{
v_2(\mathscr N_{63}^{(3)})=4M+4m+20,}
\tag{3.1}
\]

以及 positive primitive orientation

\[
\boxed{
H_3^{par}
:=\frac{-\mathscr N_{63}^{(3)}}{2^{4M+4m+20}}
>0,
\qquad
H_3^{par}\equiv3\pmod4.}
\tag{3.2}

`G_term` 为 odd，所以 (2.2) 同样给

\[
G_{term}^4\mid H_3^{par}.
\]

定义 spilled quotient

\[
\boxed{
\mathscr Q_{spill}
:=\frac{H_3^{par}}{G_{term}^4}.}
\tag{3.3}

由 (2.3)：

\[
\boxed{\gcd(\mathscr Q_{spill},G_{term})=1.}
\tag{3.4}

---

## 4. parity survives the fourth-power removal

任意 odd integer的 fourth power都满足

\[
G_{term}^4\equiv1\pmod4.
\]

所以由 (3.2),(3.3)：

\[
\boxed{
\mathscr Q_{spill}>0,
\qquad
\mathscr Q_{spill}\equiv3\pmod4.}
\tag{4.1}

因此其 prime factorization中必有至少一枚

\[
\boxed{q\equiv3\pmod4}
\tag{4.2}

出现奇数次。

结合 (3.4)：

\[
\boxed{q\notin\operatorname{Supp}(G_{term}).}
\tag{4.3}

所以 exact triple-saturated terminal recycling pool自身对 third-order parent parity完全中性；third-order positive carrier必把一份 odd-inert parity溢出到该 pool之外。

---

## 5. what this does and does not prove

本文严格证明的是 support spill：

\[
\boxed{
\text{terminal exact-saturation primes}
\text{不能独自承担 third-order odd parity}.}
\tag{5.1}

外部 supplier `q` 可能属于：

- fixed prime `3`；
- 已有 target/source/height pool；
- descendant residual/external pool；
- 或真正新的 external label。

本文没有完成这些来源的二次审计，因此不把 (4.3) 夸大成“存在新的 non-3 prime”。下一步若能排除 `q=3` 并把 old pools与 `Q_spill` 做 support separation，就会把本 surcharge升级成真正的 independent-prime product cost。

A2 仍为 `待证`。

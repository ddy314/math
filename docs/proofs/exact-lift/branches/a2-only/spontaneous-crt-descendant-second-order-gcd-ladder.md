# A2 descendant recycling 的 nested second-order gcd ladder

> **依赖：** `spontaneous-crt-descendant-balance-gcd-ladder.md`、`spontaneous-crt-descendant-second-order-tail.md`。
>
> **严格状态：**first balance tail `B_63` 读取 `h` 到 `2h` 之间的全部 depth；second-order tail `C_63^(2)` 已精确选择 saturated balance branch中越过 `2h` 的 labels。本文继续利用 exact degree filtration：linear+quadratic block的 local depth由 `C_63^(2)` 精确读取，而所有 cubic 及更高 transport项至少有 `3h` 层。因此在 `rho>=h` 后，`C_63^(2)` 又精确读取第二个完整 baseline以内的所有 extra depth；只有它自身再吞下完整 `p^h` 时三阶 transport才有资格参与。于是 descendant recycling形成两级 ordinary gcd ladder，而真正 generic unit自由被推进到连续两次 full-baseline saturation之后。本文尚未计算 third-order coefficient，因此不关闭 A2。

---

## 1. notation

固定 genuine common prime `p`，写

\[
\boxed{h:=v_p(G_\Delta)\ge1,}
\tag{1.1}
\]

first balance depth

\[
\boxed{\rho:=v_p(\mathscr B_{63}),}
\tag{1.2}
\]

以及 canonical second-order tail depth

\[
\boxed{\sigma:=v_p(\mathscr C_{63}^{(2)}).}
\tag{1.3}
\]

上一文件已证明

\[
p\mid\mathscr C_{63}^{(2)}
\Longleftrightarrow
\rho\ge h
\text{ and }
v_p(M)>2h.
\]

所以 `sigma` 只在 first balance 已饱和的 branch上承担 actual second-order意义。

---

## 2. exact depth of the linear+quadratic block

定义

\[
M_{\le2}:=M^{(1)}+M^{(2)}.
\]

`spontaneous-crt-descendant-second-order-tail.md` 构造 p-unit rational scale `U_2`，使

\[
\mathscr N_{63}^{(2)}=U_2 M_{\le2},
\]
并定义

\[
\mathscr C_{63}^{(2)}
=-\frac{\mathscr N_{63}^{(2)}}{G_\Delta S_{bal}},
\qquad
S_{bal}=\gcd(G_\Delta,\mathscr B_{63}).
\]

若

\[
\boxed{\rho\ge h,}
\tag{2.1}
\]
则

\[
v_p(S_{bal})=h,
\]
所以

\[
v_p(G_\Delta S_{bal})=2h.
\]
由于 `U_2` 为 p-unit：

\[
\boxed{
v_p(M_{\le2})
=2h+\sigma.}
\tag{2.2}

这不是 truncated inequality，而是 exact equality。

---

## 3. every omitted term starts at the third baseline

exact transport/Euclidean expansion按 parent errors `(F,L)` 总次数分级：

\[
M=M^{(1)}+M^{(2)}+M^{(\ge3)}.
\]

common baseline给

\[
v_p(F)\ge h,
\qquad
v_p(L)\ge h.
\]

每个 `M^(>=3)` monomial总次数至少3，因此

\[
\boxed{
v_p(M^{(\ge3)})\ge3h.}
\tag{3.1}

---

## 4. exact second-baseline valuation law

继续假设 `rho>=h`。

### `sigma<h`

由 (2.2)：

\[
2h+\sigma<3h.
\]

所以 `M_<=2` 是唯一最浅 block；由 (3.1) 不可能发生跨阶 cancellation：

\[
\boxed{
v_p(M)=2h+\sigma.}
\tag{4.1}

### `sigma>=h`

此时

\[
v_p(M_{\le2})\ge3h,
\]
且 higher block也至少 `3h`，故

\[
\boxed{
v_p(M)\ge3h.}
\tag{4.2}

统一写成

\[
\boxed{
\min\{v_p(M),3h\}
=2h+\min\{\sigma,h\}
\qquad(\rho\ge h).}
\tag{4.3}

或等价地

\[
\boxed{
\min\{v_p(M)-2h,h\}
=\min\{v_p(\mathscr C_{63}^{(2)}),h\}.}
\tag{4.4}

所以 `C_63^(2)` 精确读取第二个完整 baseline以内的全部 remainder depth。

---

## 5. second-order gcd ladder

对 `j>=1` 定义

\[
\boxed{
D_j^{(2)}
:=\gcd(G_\Delta^j,\mathscr C_{63}^{(2)}).}
\tag{5.1}

逐 common prime：

\[
\boxed{
v_p(D_j^{(2)})=\min(jh,\sigma).}
\tag{5.2}

因此 stable ladder读取 second-order tail上的完整 local exponent `sigma`。

真正 third-order dangerous layer是

\[
\boxed{
\rho\ge h,
\qquad
\sigma\ge h.}
\tag{5.3}

即 first 与 second tail连续各吞下至少一个完整 common baseline。

---

## 6. nested tropical law

结合 first balance ladder，generic common prime现在满足严格三段式：

\[
\boxed{
\begin{array}{c|c}
\rho<h
&v_p(M)=h+\rho,\\[2mm]
\rho\ge h,\ \sigma<h
&v_p(M)=2h+\sigma,\\[2mm]
\rho\ge h,\ \sigma\ge h
&v_p(M)\ge3h.
\end{array}}
\tag{6.1
\]

前两行已经没有 normalized-unit自由。

注意此前 second-order coefficient theorem还给：若 `rho>h` 且第二行继续失败、即越过 `2h`，则 prime必须命中 fixed `P_110(K)`。所以真正 generic moving frontier更窄地位于

\[
\boxed{
\rho=h,
\qquad
\sigma\ge h.}
\tag{6.2}

这与 earlier omega-height / first descendant balance 的 equal-depth现象完全同型：只有**恰 baseline saturation**反复保留新的 normalized resonance。

---

## 7. next frontier

目前 descendant same-prime recycling 已有：

1. `B_63` first tail；
2. `C_63^(2)` second tail；
3. 两层 ordinary gcd ladders；
4. exact depth laws直到 `3h`。

所以下一步不应回到 first/second-order ordinary resultant。真正有价值的是在

\[
\rho=h,
\qquad
\sigma\ge h
\]
上构造 cubic transported coefficient与 canonical third-order tail，或者证明这两个 full-baseline saturation不能同时由 generic external prime承担。

A2 仍为 `待证`。

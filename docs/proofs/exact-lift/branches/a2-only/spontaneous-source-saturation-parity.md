# A2 source saturation 对 angle parity 永远是偶深度

> **依赖：** `hensel.md`、`spontaneous-angle.md`、`spontaneous-angle-overlap-depth.md`、`spontaneous-source-equal-depth-nogo.md`。
>
> **严格状态：**本文澄清 source excess 在 angle primitive carrier 中的 parity bookkeeping。对真正 source inert prime，source integer `sigma` 的完整 `p^{2h}` primary part总是完整进入 `E_1` / angle carrier，因此 source-supported depth本身严格为偶数。equal-depth cancellation 若产生奇 valuation，奇的部分必来自超出 `v_p(sigma)=2h` 的 extra angle depth，而不是 source content 本身。本文不证明该 extra depth 必进入 additive common gcd，因此不是 A2 closure；它只把 source base parity 从开放列表中删除。

---

## 1. exact gcd identity

旧 second-angle integer 为

\[
\boxed{
E_1=5^\lambda L_0^2-2c_u\sigma a_2^2.}
\tag{1.1}

对任意整数 `sigma`，直接使用

\[
\gcd(X-Y,Y)=\gcd(X,Y)
\]
得到

\[
\boxed{
\gcd(E_1,\sigma)
=
\gcd(5^\lambda L_0^2,\sigma).}
\tag{1.2}

这条恒等式不需要 source Hensel 假设。

---

## 2. source inert prime 的完整 `sigma` primary part全部进入 `E_1`

固定 genuine source excess inert prime

\[
p\equiv3\pmod4,
\qquad
p^{2h}\Vert\sigma,
\qquad h\ge1.
\]

旧 source separation 给

\[
p\nmid 10c_u a_2,
\tag{2.1}
\]
而双 Hensel resultant 已证明

\[
\boxed{v_p(L_0)\ge h.}
\tag{2.2}

因为 `p != 5`，(1.2) 在该 prime 上给

\[
\begin{aligned}
v_p(\gcd(E_1,\sigma))
&=\min\{2v_p(L_0),2h\}\\
&=2h.
\end{aligned}
\]

因此

\[
\boxed{
\min\{v_p(E_1),v_p(\sigma)\}=2h,}
\tag{2.3}

特别地

\[
\boxed{p^{2h}\mid E_1.}
\tag{2.4}

所以 source primary part不是“至少一半深度”进入 angle integer；**完整的 source exponent `2h` 都进入，而且是偶深度。**

---

## 3. angle primitive carrier 有相同局部赋值

`spontaneous-angle.md` 有 exact rational identity

\[
\frac{E_1}{\Sigma a_2^2}
=
\frac{\Omega_{\rm sp}}
{y^2(x+2)F_f},
\]
其中

\[
\Sigma=c_Q^2qf.
\]

真正 source excess prime与 denominator/source-content 分离，因此

\[
p\nmid \Sigma a_2y(x+2)F_f.
\tag{3.1}

故

\[
\boxed{v_p(E_1)=v_p(\Omega_{\rm sp}).}
\tag{3.2}

`spontaneous-angle-parity.md` 的 primitive integer `widehat(O)_sp` 与 `Omega_sp` 也只差 genuine p-adic unit与固定 2-power，所以

\[
\boxed{
v_p(\widehat{\mathcal O}_{\rm sp})
=v_p(E_1).}
\tag{3.3}

结合 (2.3)：

\[
\boxed{
\min\{v_p(\widehat{\mathcal O}_{\rm sp}),2h\}=2h.}
\tag{3.4}

---

## 4. source-saturated residual depth

定义局部 extra angle depth

\[
\boxed{
e_p^{\rm extra}
:=v_p(\widehat{\mathcal O}_{\rm sp})-2h
\ge0.}
\tag{4.1}

因为 `2h` 为偶数：

\[
\boxed{
v_p(\widehat{\mathcal O}_{\rm sp})
\equiv e_p^{\rm extra}\pmod2.}
\tag{4.2}

所以 source primary part本身对 angle `mod 4` parity严格中性；所有奇 parity 都来自超出完整 source exponent 的 extra depth。

更具体地：

- `v_p(d)>h` 时，`spontaneous-angle-overlap-depth.md` 已证明
  \[
  v_p(\widehat O_{\rm sp})=2h,
  \]
  所以 `e_p^extra=0`；
- `v_p(d)=h` 但 normalized angle cancellation失败时同样 `e_p^extra=0`；
- 只有 `spontaneous-source-equal-depth-nogo.md` 的 simple second-order correction成立时，才可能
  \[
  e_p^{\rm extra}>0.
  \]

因此 source pool 的规范 parity decomposition 是

\[
\boxed{
\underbrace{2h}_{\text{source saturation, even}}
+
\underbrace{e_p^{\rm extra}}_{\text{angle-over-source residual}}.}
\tag{4.3}

---

## 5. `审计`：不能把 extra depth再称为“source parity”

此前 `G_sp mod 4` residual quotient 的 prime-source bookkeeping 中，若一个 source prime满足

\[
v_p(\widehat O_{\rm sp})=2h+1
\]
可能被口头描述成“source pool 提供一份 odd inert parity”。(4.3) 说明这种说法会混淆两个层次：

- `p^{2h}` 是原 source integer `sigma` 已有的完整 primary content，严格偶深；
- 多出来的 `p` 已经是 angle equation 在 source primary饱和后的**额外接触**。

因此后续 global parity ledger 应把 source inert primary先完整饱和，再研究 extra quotient。source base contribution永远为 `1 mod 4`。

形式上，若只取 source inert primary square

\[
S_{\rm src}:=
\prod_{p\in\mathcal S_{\rm src}}p^{2h_p},
\]
则

\[
\boxed{S_{\rm src}\equiv1\pmod4.}
\tag{5.1}

从 `widehat(O)_sp` 中约去这些完整 source powers不会改变全局 `3 mod 4` orientation。

---

## 6. 对 parity 闭环的更新

本文并没有排除

\[
e_p^{\rm extra}\equiv1\pmod2.
\]
`spontaneous-source-equal-depth-nogo.md` 恰恰证明局部 source geometry允许这种 extra lift。

但开放问题现在应准确表述为：

\[
\boxed{
\text{source-saturated angle residual 是否能在没有 additive common contact 时保留 odd extra depth？}}
\tag{6.1}

而不是“source excess 本身是否贡献奇 parity”。后者已经严格回答：**不会。**

下一步必须把 `e_p^extra` 与 source 外部对象联立，最自然的是

\[
\widehat{\mathcal T}_2,
\quad
G_{\rm sp},
\quad
D_{\rm src}\text{ 的 natural representative},
\quad
\text{或 global Gaussian allocation}.
\]

这一重新分类删除了 source base-depth 的假自由度，但不把 extra angle-over-source residual错误地宣称为已关闭。

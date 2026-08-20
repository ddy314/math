# DD genuine-Gaussian 的 discriminant square carrier

> **依赖：** [`global-framework.md`](../../global-framework.md) 的统一 `Q,G,N_12,kappa,W` 判别平方；[`frontier.md`](frontier.md) 的 one-channel pair-max reduction 与 genuine-Gaussian branch。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文第一次离开 full-rational `A≡±b` sheet，直接处理 genuine-Gaussian main core。对每个 one-channel pair-max prime-power `p^h`，统一判别平方本身会产生第二个 depth `2h` 的 sum-of-two-squares carrier：
> \[
> p^{2h}\mid W^2+\Omega^2,
> \qquad
> \Omega:=Q(a_2b_1)(\kappa+G).
> \]
> 该 carrier 不使用 rational sign degeneration。进一步与原 pair-max carrier比较 orientation，可把 genuine core 分成 same/opposite 两类，并得到两个 **square-depth rational cross determinants**。
>
> 本文不证明这些 determinants 足够短，因此不关闭 genuine-Gaussian branch；但它把此前“需要新的 Gaussian/projective same-prime elimination”具体化成一个可核验的二 carrier orientation problem。

---

## 1. one-channel genuine main prime 的本原数据

统一前两块对象为

\[
Q=b_1 10^{m_2}+b_2,
\qquad
G=b_1b_2,
\tag{1.1}
\]

\[
\mathcal N_{12}
=(a_1b_2)^2+(a_2b_1)^2.
\tag{1.2}
\]

为避免与 moving core `C_G` 混淆，把 unified DD coefficient 记为

\[
\boxed{
\mathscr C
:=10^{m_2+k_{12}}a_1+10^{d_3}a_2.
}
\tag{1.3}
\]

DD 中

\[
\boxed{
\kappa=\frac{10^{m_3}QG}{b_3}\in\mathbf Z.
}
\tag{1.4}
\]

固定 genuine-Gaussian main prime-power

\[
p^h\Vert C_G^{\rm main}.
\]

one-channel pair-max normalization 删除 all-three/common 与另一 pair channel 的 `o(S)` exceptional core 后，恰有

\[
\boxed{
v_p(b_2)=v_p(b_3)=h,
\qquad p\nmid b_1,
\qquad p\ne2,5.}
\tag{1.5}
\]

由 reducedness：

\[
\boxed{p\nmid a_2a_3.}
\tag{1.6}
\]

于是

\[
Q\equiv b_1 10^{m_2}\not\equiv0\pmod p,
\]

故

\[
\boxed{v_p(Q)=0.}
\tag{1.7}
\]

同时

\[
\boxed{v_p(G)=h.}
\tag{1.8}
\]

由 `(1.2)`：

\[
\mathcal N_{12}
\equiv(a_2b_1)^2\not\equiv0\pmod p,
\]

因此

\[
\boxed{v_p(\mathcal N_{12})=0.}
\tag{1.9}
\]

最后由 `(1.4)`：

\[
v_p(\kappa)
=v_p(G)-v_p(b_3)=h-h=0,
\]

所以

\[
\boxed{p\nmid\kappa(\kappa+2G).}
\tag{1.10}
\]

这组 unit facts 全部不使用 rational contact。

---

## 2. 两个自然平方近似都精确到 `p^(2h)`

定义

\[
x:=a_1b_2,
\qquad
y:=a_2b_1.
\tag{2.1}
\]

则

\[
\mathcal N_{12}=x^2+y^2.
\]

由 `p^h|b_2`：

\[
\boxed{
\mathcal N_{12}\equiv y^2\pmod{p^{2h}}.}
\tag{2.2}
\]

另一方面

\[
\kappa(\kappa+2G)
=\kappa^2+2\kappa G,
\]

而

\[
(\kappa+G)^2
=\kappa^2+2\kappa G+G^2.
\]

由 `p^h|G`：

\[
\boxed{
\kappa(\kappa+2G)
\equiv(\kappa+G)^2
\pmod{p^{2h}}.}
\tag{2.3}
\]

甚至两者乘积的误差也可 exact 展开：

\[
\begin{aligned}
&\mathcal N_{12}\kappa(\kappa+2G)
-y^2(\kappa+G)^2\\
&\qquad=
\boxed{
x^2\kappa(\kappa+2G)-y^2G^2.}
\end{aligned}
\tag{2.4}
\]

右端两项都被 `p^(2h)` 整除，因此

\[
\boxed{
\mathcal N_{12}\kappa(\kappa+2G)
\equiv
(a_2b_1)^2(\kappa+G)^2
\pmod{p^{2h}}.}
\tag{Square-approx}
\]

---

## 3. 判别平方产生新的 depth-`2h` sum-of-two-squares carrier

统一判别平方在 DD (`D=Q`) 中为

\[
W^2
=\kappa\bigl(
\kappa(G^2\mathscr C^2-Q^2\mathcal N_{12})
-2GQ^2\mathcal N_{12}
\bigr).
\]

整理：

\[
\boxed{
W^2
+Q^2\mathcal N_{12}\kappa(\kappa+2G)
=(\kappa G\mathscr C)^2.
}
\tag{Disc-square}
\]

定义全局整数

\[
\boxed{
\Omega
:=Q(a_2b_1)(\kappa+G).
}
\tag{3.1}
\]

由 `(Square-approx)`：

\[
Q^2\mathcal N_{12}\kappa(\kappa+2G)
\equiv\Omega^2\pmod{p^{2h}}.
\]

而 `(1.8)` 给

\[
p^{2h}\mid(\kappa G\mathscr C)^2.
\]

代入 `(Disc-square)`：

\[
\boxed{
p^{2h}\mid W^2+\Omega^2.}
\tag{Disc-carrier-local}
\]

聚合 genuine main prime-powers：

\[
\boxed{
(C_G^{\rm main})^2
\mid W^2+\Omega^2.
}
\tag{Disc-carrier-global}
\]

这里没有出现 `A±b`、`D_±`、`R_±` 或 full-rational cofactor sheet，因此该 carrier genuine branch 也可用。

---

## 4. carrier 在 genuine main core 上是 primitive 的

由 §§1：

\[
p\nmid Q(a_2b_1)(\kappa+G),
\]

所以

\[
\boxed{p\nmid\Omega.}
\tag{4.1}
\]

若 `p|W`，由 `(Disc-carrier-local)` 模 `p` 会得到

\[
\Omega^2\equiv0\pmod p,
\]

矛盾。因此

\[
\boxed{p\nmid W\Omega.}
\tag{4.2}
\]

于是 `-1` 在每个 genuine main prime 上为 quadratic residue；特别地

\[
\boxed{p\equiv1\pmod4.}
\tag{4.3}
\]

更重要的是，`W+iOmega` 的 `p`-norm depth `2h` 不可能同时分给 conjugate 两侧：若 `pi` 与 `bar pi` 都整除 `W+iOmega`，则 `p` 同时整除 `W` 与 `Omega`，与 `(4.2)` 冲突。

因此对每个 `p^h` 存在唯一 orientation（差一个 Gaussian unit）使

\[
\pi_p^{2h}\mid W+i\Omega.
\]

聚合得到一个 oriented Gaussian factor

\[
\boxed{
N(\Pi_{\rm disc})=C_G^{\rm main},
\qquad
\Pi_{\rm disc}^{\,2}\mid W+i\Omega.
}
\tag{Disc-Gaussian}
\]

所以统一判别平方现在自身也是 pair-max orientation 的一个 reader。

---

## 5. 与原 pair-max orientation 比较

原 pair-max core给出另一个 oriented factor

\[
\boxed{
N(\Pi_{\rm sph})=C_G^{\rm main},
\qquad
\Pi_{\rm sph}^{\,2}\mid y_2+i y_3.
}
\tag{Sphere-Gaussian}
\]

对每个 genuine main `p^h`，比较 `Pi_disc` 与 `Pi_sph` 的 local orientation。

定义：

- `same`：两者选择同一个 `pi_p`；
- `opposite`：一个选择 `pi_p`，另一个选择 `bar pi_p`。

相应把 genuine core 分成互素（差 `10^{o(S)}` exceptional overlap）的两个 rational divisors

\[
\boxed{
C_G^{\rm main}=C_{\rm same}C_{\rm opp}.}
\tag{5.1}
\]

---

## 6. same orientation 给 square-depth difference determinant

若 `p^h|C_same`，则

\[
\pi_p^{2h}\mid y_2+i y_3,
\qquad
\pi_p^{2h}\mid W+i\Omega.
\]

考虑 Gaussian linear combination：

\[
\Omega(y_2+i y_3)-y_3(W+i\Omega)
=\Omega y_2-Wy_3.
\]

右边是 rational integer，却被 `pi_p^(2h)` 整除。对 rational integer，`v_pi=v_p`，故

\[
p^{2h}\mid\Omega y_2-Wy_3.
\]

聚合：

\[
\boxed{
C_{\rm same}^{\,2}
\mid
\Theta_{\rm same},
\qquad
\Theta_{\rm same}:=\Omega y_2-Wy_3.
}
\tag{Same-det}
\]

`Theta_same` 可能为零；若为零，则得到 exact slope lock

\[
\boxed{
\frac W\Omega=\frac{y_2}{y_3}.}
\tag{Same-zero}
\]

这需要后续单独审计。

---

## 7. opposite orientation 给 square-depth positive determinant

若 `p^h|C_opp`，取 `Pi_sph` 的 orientation 为 `pi_p`，则 discriminant carrier在同一 `pi_p` 上表现为

\[
\pi_p^{2h}\mid W-i\Omega.
\]

于是

\[
\Omega(y_2+i y_3)+y_3(W-i\Omega)
=\Omega y_2+Wy_3.
\]

故

\[
p^{2h}\mid\Omega y_2+Wy_3.
\]

聚合：

\[
\boxed{
C_{\rm opp}^{\,2}
\mid
\Theta_{\rm opp},
\qquad
\Theta_{\rm opp}:=\Omega y_2+Wy_3.
}
\tag{Opp-det}
\]

所有 terminal quantities 为正，所以

\[
\boxed{\Theta_{\rm opp}>0.}
\tag{7.1}
\]

因此 opposite orientation 不存在 zero-determinant 逃逸；它必须真实支付一个 positive rational integer 的 square-depth divisibility。

---

## 8. orientation-free product form

由 `(Same-det)` 与 `(Opp-det)`：

\[
C_{\rm same}^2C_{\rm opp}^2
\mid
\Theta_{\rm same}\Theta_{\rm opp}.
\]

结合 `(5.1)`：

\[
\boxed{
(C_G^{\rm main})^2
\mid
(\Omega y_2)^2-(Wy_3)^2.
}
\tag{Cross-product}
\]

这条 product form 不需要预先固定每个 prime 的 orientation。

但目前不能仅凭其 Archimedean size关闭 genuine branch：`W,Omega,y_2,y_3` 的 raw heights 很大，普通 capacity bound 仍可能容纳 `2 log C_G`。

因此 `(Cross-product)` 的价值主要是：把 genuine-Gaussian 的同素数问题从抽象“另找一个 Gaussian eliminant”压成两个 explicit rational integers `Theta_same,Theta_opp`。

---

## 9. 当前新的 genuine-Gaussian frontier

现在 genuine branch 至少具有两套 independent-looking Gaussian carriers：

\[
\Pi_{\rm sph}^{\,2}\mid y_2+i y_3,
\]

\[
\Pi_{\rm disc}^{\,2}\mid W+i\Omega,
\qquad
\Omega=Q(a_2b_1)(\kappa+G).
\]

比较 orientations 后：

\[
\boxed{
C_{\rm same}^{\,2}\mid\Omega y_2-Wy_3,
\qquad
C_{\rm opp}^{\,2}\mid\Omega y_2+Wy_3.
}
\tag{9.1}
\]

下一步不应立刻取 norm 再做 generic height sum；应该分别研究：

1. `same` 的 zero case `(Same-zero)` 是否会精确退回已有 projective/source relation；
2. `same` 非零时，`Theta_same` 是否有 hidden small factor / cancellation；
3. `opposite` 中 `Theta_opp>0`，能否在除去 explicit smooth/source factors 后得到严格小于 `2 log C_opp` 的 core height；
4. 若两 determinant 都只是 primitive carrier tetrahedron 的旧 edges，则把该等价关系明确写出并继续寻找真正 global digit carrier。

---

## 10. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：genuine main prime 上 `Q,N_12,kappa,kappa+2G` 为 units；`N_12` 与 `kappa(kappa+2G)` 的 `p^(2h)` natural square approximations；`Disc-carrier-global`；primitive discriminant Gaussian orientation；same/opposite orientation split；`Same-det`、`Opp-det` 与 orientation-free `Cross-product`。
- **`有限证书`**：可用脚本机械检查 `(2.4)`、`Disc-square` 重排和两个 Gaussian cross combinations。
- **`待证`**：`Same-zero` audit；两个 cross determinant 的 normalized core height；genuine-Gaussian closure；DD 全局空性。

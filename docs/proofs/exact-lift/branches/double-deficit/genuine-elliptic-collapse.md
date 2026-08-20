# DD genuine-Gaussian surviving elliptic second lift 的 sphere-pay collapse

> **依赖：** [`genuine-tail-root-orientation-lock.md`](genuine-tail-root-orientation-lock.md)、[`genuine-full-concat-carrier.md`](genuine-full-concat-carrier.md)。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。orientation lock 已证明 genuine main core 只保留一个全局 relative orientation，且其 sign 满足
> \[
> \epsilon_\sigma\eta=+1.
> \]
> 本文继续审计 surviving full-concat square-depth。消去 `W` 后得到 W-free carrier
> \[
> \Theta
> =(\kappa+G)Q(a_2b_1)^2\beta+\mathscr T a_3^2.
> \]
> 随后证明一个 exact identity：`Theta` 的全部 `C_G^2` depth 已由原 pair-max sphere norm 的 `2h` excess 加上显式 denominator baseline支付。因此 discriminant/full-concat second lift在 surviving elliptic class 上不构成第二份独立 obstruction。
>
> 结论：本轮 discriminant carrier 的真正新增信息只有 **global orientation lock**；其 surviving square-depth 是 sphere carrier 的重写。

---

## 1. surviving elliptic sign

沿用全局 tail-root sign

\[
\eta\in\{\pm1\}
\]

以及

\[
\epsilon_{\rm same}=-1,
\qquad
\epsilon_{\rm opp}=+1.
\]

前一文件证明 genuine main primes 必须满足

\[
\boxed{\epsilon_\sigma\eta=+1.}
\tag{1.1}

因此 surviving class 的 sign 实际满足

\[
\boxed{\epsilon_\sigma=\eta.}
\tag{1.2}

以下记其 main core 为

\[
C_{\rm ell}=C_G^{\rm main}\cdot10^{o(S)}.
\]

为了避免与 denominator core 混淆，继续把统一 DD coefficient 写成

\[
C_{\rm DD}=10^{d_3}A_{12}.
\]

---

## 2. 从 full-concat carrier 消去 `W`

定义

\[
y:=a_2b_1,
\qquad
A_c:=Qy^2.
\]

surviving full-concat carrier 为

\[
\boxed{
\Psi_{\rm ell}
=A_c\beta+\eta Wa_3,
\qquad
C_{\rm ell}^2\mid\Psi_{\rm ell}.
}
\tag{2.1}

而 tail-root original identity 为

\[
\boxed{
\mathscr T a_3
=\kappa G^2C_{\rm DD}
+\eta(\kappa+G)W,
}
\tag{2.2}

其中

\[
\mathscr T
=\frac{\kappa^2(\kappa+2G)}{10^{m_3}}.
\]

由 `(2.2)`：

\[
\eta(\kappa+G)W
=\mathscr T a_3-\kappa G^2C_{\rm DD}.
\]

乘 `(2.1)` 以 `kappa+G`：

\[
\begin{aligned}
(\kappa+G)\Psi_{\rm ell}
&=(\kappa+G)A_c\beta
+\eta(\kappa+G)Wa_3\\
&=(\kappa+G)A_c\beta
+\mathscr T a_3^2
-\kappa G^2C_{\rm DD}a_3.
\end{aligned}
\]

定义 W-free integer

\[
\boxed{
\Theta
:=(\kappa+G)A_c\beta
+\mathscr T a_3^2.
}
\tag{Theta-def}

于是有 exact relation

\[
\boxed{
\Theta
=(\kappa+G)\Psi_{\rm ell}
+\kappa G^2C_{\rm DD}a_3.
}
\tag{Theta-from-Psi}

由于

\[
C_{\rm ell}^2\mid\Psi_{\rm ell},
\qquad
C_{\rm ell}^2\mid G^2,
\]

立刻有

\[
\boxed{C_{\rm ell}^2\mid\Theta.}
\tag{2.3}

但这一步还不能说明 `Theta` 是独立 obstruction；下面做 no-double-count 审计。

---

## 3. 定义 original-integer sphere norm carrier

令

\[
\boxed{
\mathcal S_{\rm raw}
:=y^2b_3^2+G^2a_3^2.
}
\tag{3.1}

使用

\[
y=a_2b_1,
\qquad
G=b_1b_2,
\]

可写成

\[
\boxed{
\mathcal S_{\rm raw}
=b_1^2\left[(a_2b_3)^2+(a_3b_2)^2\right].
}
\tag{3.2}

它就是 `(y_2,y_3)` sphere norm 清除 pair-max denominator 后的 original-integer 版本。

固定

\[
p^h\Vert C_{\rm ell}.
\]

写

\[
b_2=p^hb_{2,p},
\qquad
b_3=p^hb_{3,p}.
\]

前一文件的 `(Sphere-normalized)` 给

\[
p^{2h}\mid
a_2^2b_{3,p}^2+a_3^2b_{2,p}^2.
\]

因此 `(3.2)` 给

\[
\boxed{p^{4h}\mid\mathcal S_{\rm raw}.}
\tag{Sphere-raw-4h}

这里前 `2h` 是 `b_2,b_3` shared denominator baseline，后 `2h` 是 pair-max Gaussian square-depth。

---

## 4. `Theta` 与 sphere norm 的 exact identity

记

\[
T_3:=10^{m_3}.
\]

使用

\[
\beta=T_3Q+b_3,
\tag{4.1}
\]

\[
\kappa b_3=T_3QG,
\tag{4.2}
\]

以及

\[
\mathscr T=\frac{\kappa^2(\kappa+2G)}{T_3},
\]

从 `(Theta-def)` 直接展开：

\[
\Theta
=(\kappa+G)Qy^2(T_3Q+b_3)
+\frac{\kappa^2(\kappa+2G)}{T_3}a_3^2.
\tag{4.3}

乘以 `T_3 G^2`，并用 `(4.2)` 消去 `T_3QG`：

\[
\begin{aligned}
T_3G^2\Theta
&=\kappa^2(\kappa+G)^2y^2b_3^2/\kappa
+\kappa^2(\kappa+2G)G^2a_3^2\\
&=\kappa\Bigl[
(\kappa+G)^2y^2b_3^2
+\kappa(\kappa+2G)G^2a_3^2
\Bigr].
\end{aligned}
\]

使用

\[
(\kappa+G)^2
=\kappa(\kappa+2G)+G^2,
\]

得到精确恒等式

\[
\boxed{
T_3G^2\Theta
=\kappa\left[
\kappa(\kappa+2G)\mathcal S_{\rm raw}
+G^2y^2b_3^2
\right].
}
\tag{Sphere-pay-identity}

这是本文的核心 no-double-count identity。

---

## 5. `Theta` 的 `2h` 深度全部由 sphere carrier 支付

固定 `p^h||C_ell`。main ledger 给

\[
p\nmid T_3\kappa y.
\]

同时

\[
v_p(G)=v_p(b_3)=h.
\]

由 `(Sphere-raw-4h)`：

\[
v_p(\mathcal S_{\rm raw})\ge4h.
\]

而第二项显然有

\[
v_p(G^2y^2b_3^2)=4h.
\]

所以 `(Sphere-pay-identity)` 的右端满足

\[
v_p(\text{RHS})\ge4h.
\]

左端的显式 `G^2` 已支付恰好 `2h`：

\[
v_p(T_3G^2\Theta)=2h+v_p(\Theta).
\]

因此仅由 sphere norm 与 denominator baseline 就已经推出

\[
\boxed{v_p(\Theta)\ge2h.}
\tag{Sphere-pays-Theta}

这与 `(2.3)` 完全相同。

所以：

\[
\boxed{
C_{\rm ell}^2\mid\Theta
\text{ 并不是 discriminant/full-concat 提供的第二份独立 square depth；}
\text{它已经被原 sphere square-depth精确支付。}
}
\tag{Elliptic-collapse}

---

## 6. 对 two-layer Hensel 的含义

此前 genuine two-layer ledger 写成

\[
R_\sigma=C_\sigma K_\sigma,
\qquad
v_p(R_\sigma)=h,
\]

以及

\[
C_\sigma\mid K_\sigma+A_c\frac{b_3}{C_\sigma}.
\]

orientation lock 后只剩 `ell` class。

`Theta-from-Psi` 与 `Sphere-pay-identity` 说明：如果试图用 tail-root identity 消去 `K_ell` 中的 `W`，second lift最终会落回 `mathcal S_raw` 的 sphere norm；不会产生一个新的 `<C_ell` natural representative。

因此此前的 closure target

\[
\text{“从 }K_\sigma\text{ 的 source residue 提取独立短代表”}
\]

在当前 discriminant/tail-root algebra 内已经完成审计：

\[
\boxed{
\text{它只能恢复 sphere-paid elliptic depth。}
}
\tag{K-route-nogo}

**状态：`失效/降级`。**

---

## 7. genuine branch 的更新 frontier

经过最近几层：

1. discriminant square carrier存在；
2. raw cross determinant没有 Archimedean saving；
3. denominator-cleared / full-concat carrier存在；
4. two-layer Hensel存在；
5. tail-root linearization把 relative orientation 锁成全局唯一 class；
6. wrong hyperbolic class严格矛盾；
7. surviving elliptic second lift由 sphere square-depth完全支付。

因此同-prime discriminant/tail-root algebra 已经闭合到：

\[
\boxed{
\text{orientation reader only, no independent positive-linear depth.}
}
\]

真正未解决的 genuine-Gaussian 问题重新变得清楚：

> 为什么一个正线性高度的 one-channel pair-max core 能长期由 split primes `p≡1 mod4` 承担，同时满足 denominator/source digit shells？

接下来不应继续从 `W,Omega,K_sigma` 造同素数 eliminant；应转向 **global split-prime / digit-shell distribution**，尤其利用现在已经没有 relative-orientation entropy这一点。

---

## 8. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：W-free `Theta`、`Theta-from-Psi`、original `mathcal S_raw`、`Sphere-pay-identity`、`Sphere-pays-Theta`。
- **`失效/降级`**：orientation lock 后继续从 `K_sigma/W` algebra寻找第二份 square-depth或 short representative；surviving elliptic second lift 已被 sphere carrier支付。
- **`待证`**：global split-prime / digit-shell distribution；genuine-Gaussian closure；DD 全局空性。

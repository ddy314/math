# DD full-rational Good 的 axis-normalized excess 与三重 reader

> **依赖：** [`frontier.md`](frontier.md) 的 `Radius-split`、`Radius=Concat`、`Nc-slot`、`Nc1-elim`、`Concat-radius` 与 full rational axis factorization；以及 [`good-radius-excess.md`](good-radius-excess.md) 的 canonical `G_exc`。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文仍只处理假想
> \[
> \frac{n_3}{S}\to6.308883577618\ldots
> \]
> 的 full rational-contact Good 主质量，并默认删除总高度为 `o(S)` 的 coefficient / conjugate / Bad exceptional core。
>
> 本文完成三件事：
>
> 1. 证明 pure excess 的局部深度可只用 `alpha` 与 axis quotient `N_c` 读取：
>    \[
>    \varepsilon_p=\max(v_p(\alpha)-v_p(N_c),0).
>    \]
> 2. 将上一文件的 `G_exc` 改写成只含 `C_L,N_c,alpha` 的 canonical gcd；`H_R` 从 excess reader 中完全消失。
> 3. 构造一个由 axis Gaussian carrier 与最后两块 numerator 形成的 exact companion pair，并证明其 gcd quotient 在每个 main prime 上精确读取 `epsilon_p`。与 `N(Delta_1)` tail 一起得到三条等价 reader。
>
> 本文不证明 `G_exc` 为 subexponential，也不关闭 full rational Good。

---

## 1. 局部账本：`epsilon_p` 其实只是 `alpha` 超过 `N_c` 的深度

固定 main prime-power

\[
p^h\Vert C_L^{\rm main}.
\]

记

\[
r:=v_p(H_R),
\qquad
n:=v_p(N_c),
\qquad
a:=v_p(A_0)=v_p(\alpha).
\tag{1.1}
\]

最后一个等号使用 `Radius=Concat`；main coefficient-unit 条件保证

\[
p\nmid g_0(2^HZ+5^TU).
\]

`Radius-split` 给出

\[
\boxed{
a=\min(r,n)+\varepsilon_p,}
\tag{1.2}
\]

其中

\[
\varepsilon_p\ge0,
\qquad
\boxed{
\varepsilon_p>0\Longrightarrow r=n.
}
\tag{1.3}
\]

于是可以完全消去 `r`。

### 命题 1.1

对每个 main prime：

\[
\boxed{
\varepsilon_p
=\max(a-n,0)
=\max(v_p(\alpha)-v_p(N_c),0).
}
\tag{Axis-excess-local}
\]

### 证明

若 `epsilon_p=0`，则由 `(1.2)`

\[
a=\min(r,n)\le n,
\]

所以

\[
\max(a-n,0)=0=\varepsilon_p.
\]

若 `epsilon_p>0`，由 `(1.3)` 有 `r=n`，再由 `(1.2)`：

\[
a=n+\varepsilon_p,
\]

所以

\[
\max(a-n,0)=\varepsilon_p.
\]

证毕。

这说明此前写成

\[
\text{equal-depth }(H_R,N_c)
\text{ cancellation}
\]

的最后 tail，在真正扣除旧 payer 后只依赖：

\[
\boxed{
\text{concatenated numerator }\alpha
\quad\text{相对于 axis quotient }N_c\text{ 的正深度差。}
}
\]

---

## 2. `G_exc` 的 axis-normalized decimal gcd

令

\[
\boxed{
C_N
:=
\frac{C_L^{\rm main}}
{\gcd(C_L^{\rm main},N_c)},
}
\tag{2.1}
\]

以及真正的 decimal quotient

\[
\boxed{
A_N
:=
\frac{\alpha}{\gcd(\alpha,N_c)}.
}
\tag{2.2}
\]

对 `p^h || C_L^{main}`：

\[
v_p(C_N)=\max(h-n,0),
\tag{2.3}
\]

而命题 1.1 给

\[
\boxed{v_p(A_N)=\varepsilon_p.}
\tag{2.4}
\]

上一文件定义的 excess depth 为

\[
x_p
=\min(h,a)-\min(h,r,n).
\tag{2.5}
\]

如果 `epsilon_p=0`，则 `a=min(r,n)`，故 `x_p=0`。

如果 `epsilon_p>0`，则 `r=n`、`a=n+epsilon_p`，于是

\[
\begin{aligned}
x_p
&=\min(h,n+\varepsilon_p)-\min(h,n)\\
&=\min\bigl(\max(h-n,0),\varepsilon_p\bigr).
\end{aligned}
\tag{2.6}
\]

因此得到新的 exact reader：

\[
\boxed{
G_{\rm exc}
=\gcd(C_N,A_N)
}
\tag{Axis-decimal-gcd}
\]

按 `C_L^{main}` 的逐 prime-depth 精确成立。

换言之，`G_exc` 不再需要显式写成

\[
\frac{\gcd(C_L^{\rm main},\alpha)}
{\gcd(C_L^{\rm main},H_R,N_c)};
\]

它可以直接解释为：

\[
\boxed{
\text{未被 }N_c\text{ 支付的 main core}
\quad\cap\quad
\text{未被 }N_c\text{ 支付的真实 numerator}.}
\tag{2.7}
\]

这一步把 `H_R` 从 primitive excess 的定义中完全删掉。

---

## 3. canonical imbalance：core residual 与 numerator tail 逐素数只留一边

定义

\[
\boxed{
C_{\rm free}:=\frac{C_N}{G_{\rm exc}},
\qquad
A_{\rm tail}:=\frac{A_N}{G_{\rm exc}}.
}
\tag{3.1}
\]

由 `G_exc=gcd(C_N,A_N)` 立即有

\[
\boxed{
\gcd(C_{\rm free},A_{\rm tail})=1
}
\tag{Axis-imbalance}
\]

在 main core 上严格成立。

逐 prime 看，若 `epsilon_p>0`：

\[
v_p(C_N)=\max(h-n,0),
\qquad
v_p(A_N)=\varepsilon_p.
\]

抽掉最小值 `x_p` 后，只能剩下其中一边：

\[
\boxed{
\begin{array}{c|c|c}
\varepsilon_p<h-n
& p\mid C_{\rm free}
& p\nmid A_{\rm tail}\\
\varepsilon_p=h-n
& p\nmid C_{\rm free}A_{\rm tail}
& \\
\varepsilon_p>h-n
& p\nmid C_{\rm free}
& p\mid A_{\rm tail}.
\end{array}}
\tag{3.2}
\]

因此 `G_exc` 之后的 residual 不是两个仍然纠缠的 slots；它是一个真正的 **denominator-vs-numerator imbalance**。

---

## 4. 最后两块 numerator 自带一个 full-core Gaussian carrier

定义 full rational axis carrier

\[
\boxed{
Z_{\rm ax}:=C_*+iR_0,
\qquad
C_*:=\frac{g_0a_2B}{2}.
}
\tag{4.1}
\]

并沿用统一 orientation

\[
\Gamma:=\Pi_+\overline{\Pi_-},
\qquad
N(\Gamma)=E=D_+D_-.
\tag{4.2}
\]

full rational sign factorization 已给

\[
\boxed{\Gamma\mid Z_{\rm ax}.}
\tag{4.3}
\]

定义只使用最后两块 numerator 与 decimal tail 的 Gaussian integer

\[
\boxed{
Z_{23}
:=2a_3+i10^m a_2.
}
\tag{4.4}
\]

使用 exact bridge

\[
VA_0-g_0a_3=2\cdot5^TR_0
\tag{4.5}
\]

和

\[
10^m=2B5^T,
\tag{4.6}
\]

直接展开：

\[
\begin{aligned}
g_0Z_{23}
&=2g_0a_3+i g_0a_2 10^m\\
&=2VA_0-4\cdot5^TR_0
+4i5^TC_*\\
&=\boxed{
2VA_0+4i5^T(C_*+iR_0)}.
\end{aligned}
\tag{Tail-axis}
\]

因为

\[
E\mid V,
\qquad
\Gamma\mid Z_{\rm ax},
\]

且 main core 与 `g_0` 只有 `o(S)` overlap，所以

\[
\boxed{
\Gamma\mid Z_{23}
}
\tag{Two-block-carrier}
\]

在 full rational main orientation 上成立。

这是一条新的 terminal projection：pair-max rational-contact orientation 已经可以仅从

\[
2a_3+i10^m a_2
\]

读取；不需要 `A_{12}` 或 `Y=2\,10^dA_{12}`。

取范数还得到必要条件

\[
\boxed{
E\mid4a_3^2+10^{2m}a_2^2
}
\tag{4.7}
\]

按 main prime mass 理解。

> **审计边界：**`Two-block-carrier` 本身是 full-depth baseline，不应把它当成 `G_exc` 的第二次收费。真正的 excess 必须在除去 axis/common depth后读取。

---

## 5. axis / two-block carrier 的 exact companion pair

考虑 Gaussian product

\[
Z_{\rm ax}\overline{Z_{23}}
=(C_*+iR_0)(2a_3-i10^m a_2).
\]

定义其实部、虚部：

\[
\boxed{
\mathcal T_+
:=2C_*a_3+R_0 10^m a_2,
}
\tag{5.1}
\]

\[
\boxed{
\mathcal T_-
:=2R_0a_3-C_*10^m a_2.
}
\tag{5.2}
\]

### 5.1 `T_+` 精确等于 `V A_0` 通道

利用 `(4.5)`、`C_*=g_0a_2B/2` 与 `10^m=2B5^T`：

\[
\begin{aligned}
\mathcal T_+
&=g_0a_2Ba_3
+2B5^TR_0a_2\\
&=Ba_2(g_0a_3+2\cdot5^TR_0)\\
&=\boxed{Ba_2VA_0.}
\end{aligned}
\tag{Tplus}
\]

### 5.2 `T_-` 精确等于 `A_0/N_c` difference

由同一组恒等式：

\[
\begin{aligned}
g_0\mathcal T_-
&=2g_0R_0a_3-g_0C_*10^m a_2\\
&=2VR_0A_0
-4\cdot5^TR_0^2
-4\cdot5^TC_*^2.
\end{aligned}
\]

又有

\[
C_*^2+R_0^2=EN_c,
\qquad
V=Ee_0,
\]

所以

\[
\boxed{
g_0\mathcal T_-
=2E\bigl(e_0R_0A_0-2\cdot5^TN_c\bigr).}
\tag{Tminus}
\]

因此 `T_+` 与 `T_-` 是一个 exact companion pair：前者读取 `A_0`，后者比较 `A_0` 与 axis quotient `N_c`。

---

## 6. companion gcd quotient 精确读取 `epsilon_p`

定义

\[
\boxed{
\Lambda_{\rm ax}
:=
\frac{\mathcal T_+}
{\gcd(\mathcal T_+,\mathcal T_-)}.
}
\tag{6.1}
\]

若 `T_-<0`，gcd 取 `|T_-|`；这不影响任何赋值。对 main prime，`B,a_2,e_0,R_0,g_0,2,5` 都是 units。

由 `(Tplus)`：

\[
\boxed{v_p(\mathcal T_+)=h+a.}
\tag{6.2}
\]

由 `(Tminus)`，括号内两项的深度分别为 `a` 与 `n`。

### 情形一：`epsilon_p=0`

此时

\[
a=\min(r,n)\le n.
\]

若 `a<n`，则

\[
v_p(\mathcal T_-)=h+a.
\]

若 `a=n`，两项可能继续 cancellation，但至少有

\[
v_p(\mathcal T_-)\ge h+a.
\]

因为 `T_+` 的深度恰为 `h+a`，两种情况下都有

\[
v_p\gcd(\mathcal T_+,\mathcal T_-)=h+a,
\]

故

\[
v_p(\Lambda_{\rm ax})=0.
\tag{6.3}
\]

### 情形二：`epsilon_p>0`

由 `(1.3)`：

\[
r=n,
\qquad
a=n+\varepsilon_p>n.
\]

于是 `(Tminus)` 中两项深度不等，较浅项为 `N_c`：

\[
\boxed{v_p(\mathcal T_-)=h+n.}
\tag{6.4}
\]

因此

\[
\begin{aligned}
v_p(\Lambda_{\rm ax})
&=(h+n+\varepsilon_p)-(h+n)\\
&=\varepsilon_p.
\end{aligned}
\]

统一得到：

\[
\boxed{
v_p(\Lambda_{\rm ax})=\varepsilon_p}
\tag{Axis-tail-reader}
\]

对每个 main prime 精确成立。

所以 `Lambda_ax` 是一个 canonical **pure excess tail quotient**：full pair-max depth `h` 与 axis baseline `min(a,n)` 都已经被 ordinary gcd 自动删掉，只留下真正的 unit-unit excess。

---

## 7. `N(Delta_1)` 也给出同一个 tail reader

定义

\[
\boxed{
D_1
:=
\gcd\bigl(N(\Delta_1),H_R,N_c\bigr),
}
\tag{7.1}
\]

以及

\[
\boxed{
\Lambda_1
:=
\frac{N(\Delta_1)}{D_1}.
}
\tag{7.2}
\]

对 main prime，`Radius-split` 给

\[
v_p(N(\Delta_1))=\min(r,n)+\varepsilon_p.
\]

因此

\[
v_p(D_1)=\min(r,n),
\]

从而

\[
\boxed{v_p(\Lambda_1)=\varepsilon_p.}
\tag{Norm-tail-reader}
\]

这说明 cofactor norm tail、axis companion tail 与 decimal numerator tail 三者在 main support 上读取的是**同一个**深度函数 `epsilon_p`。

---

## 8. 三重 canonical gcd ladder

综合 §§2、6、7：

\[
v_p(A_N)
=v_p(\Lambda_{\rm ax})
=v_p(\Lambda_1)
=\varepsilon_p.
\tag{8.1}
\]

而

\[
v_p(C_N)=\max(h-n,0).
\]

所以同一个 `G_exc` 有三条完全等价的 reader：

\[
\boxed{
G_{\rm exc}
=\gcd(C_N,A_N)
=\gcd(C_N,\Lambda_{\rm ax})
=\gcd(C_N,\Lambda_1)
}
\tag{Gcd-ladder}
\]

按 `C_L^{main}` 的 prime-depth 精确成立。

这张 ladder 的三个坐标具有不同语义：

1. `A_N`：真实 concatenated numerator 的 axis-normalized quotient；
2. `Lambda_ax`：最后两块 Gaussian carrier 与 axis carrier 的 companion gcd quotient；
3. `Lambda_1`：secondary norm `N(Delta_1)` 去掉 `(H_R,N_c)` baseline 后的 quotient。

于是 pure excess 已从一条局部 cancellation 改写成一个 **同一 denominator residual `C_N` 与三个 natural tail readers 的公共 gcd**。

---

## 9. no-double-count 审计：raw `Z_23` 只读取 baseline

`Two-block-carrier` 给

\[
\Gamma\mid Z_{23}
\]

对整个 full rational main core成立，而不需要 `epsilon_p>0`。

所以后续不能把

\[
C_L\mid N(Z_{23})
\]

再次算作 pure excess 的独立模量。

真正的新 tail 位于

\[
\Lambda_{\rm ax}
=\mathcal T_+/\gcd(\mathcal T_+,\mathcal T_-),
\]

即先把 full axis / pair-max common depth自动删掉后剩下的 quotient。

同理，`Lambda_1` 必须先除以

\[
D_1=\gcd(N(\Delta_1),H_R,N_c)
\]

才能作为 excess reader；直接使用整个 `N(Delta_1)` 会重复计算 radius baseline。

---

## 10. 当前更新后的 primitive digit-shell 目标

上一文件把目标写成证明

\[
\log G_{\rm exc}=o(S).
\]

本文把可用输入进一步正规化为

\[
\boxed{
\begin{gathered}
C_N=\frac{C_L^{\rm main}}{(C_L^{\rm main},N_c)},\\[1mm]
A_N=\frac{\alpha}{(\alpha,N_c)},\\[1mm]
\Lambda_{\rm ax}
=\frac{\mathcal T_+}{(\mathcal T_+,\mathcal T_-)},\\[1mm]
\Lambda_1
=\frac{N(\Delta_1)}{(N(\Delta_1),H_R,N_c)},\\[1mm]
G_{\rm exc}
=(C_N,A_N)
=(C_N,\Lambda_{\rm ax})
=(C_N,\Lambda_1).
\end{gathered}}
\tag{10.1}
\]

因此下一条真正有价值的 strict lemma 已经可以表述得更窄：

> **Axis-normalized digit-shell separation（待证）**：证明 `C_N` 的正线性 main mass不能同时进入 `A_N` 与任一 independent normalized tail reader；或者证明 `A_N`、`Lambda_ax`、`Lambda_1` 在除去已知 common algebra 后的共同 main support只有 `10^{o(S)}`。

如果继续消元后只恢复 `(Tail-axis)`、`(Tplus)`、`(Tminus)` 或 `Nc1-elim`，则属于同一 local algebra 的重写，不得重复计费。

---

## 11. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`epsilon_p=max(v_p(alpha)-v_p(N_c),0)`；`G_exc=(C_N,A_N)`；canonical denominator/numerator imbalance；two-block full Gaussian carrier `Gamma | 2a_3+i10^m a_2`；exact companion pair `(Tplus)/(Tminus)`；`v_p(Lambda_ax)=epsilon_p`；`v_p(Lambda_1)=epsilon_p`；三重 gcd ladder `(Gcd-ladder)`。
- **`失效/降级`**：把 raw `Z_23` 的 full `C_L` divisibility 当作 excess surplus；未先删除 `(H_R,N_c)` baseline 就直接对 `N(Delta_1)` 收费。
- **`待证`**：axis-normalized digit-shell separation；`log G_exc=o(S)`；full rational Good emptiness；genuine-Gaussian split-prime / digit-shell closure；DD 全局空性与有效绝对高度界。

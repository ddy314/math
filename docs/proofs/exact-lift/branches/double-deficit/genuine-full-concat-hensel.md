# DD genuine-Gaussian full-concat carrier 的两层 Hensel 分解

> **依赖：** [`genuine-full-concat-carrier.md`](genuine-full-concat-carrier.md) 与 terminal factorization
> \[
> b_3=BJC_0q_c\theta s,
> \qquad
> C_0s=C_Lv_0.
> \]
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。上一文件给
> \[
> C_\sigma^2\mid
> Q a_2^2b_1^2\beta\pm Wa_3.
> \]
> 本文利用 `beta=Q10^{m_3}+b_3` 将这份 square depth 分成两个连续层：第一层作用于
> \[
> R_\sigma=Q^2a_2^2b_1^2 10^{m_3}\pm Wa_3,
> \]
> 且对每个 target `p^h` 有 **exact depth** `v_p(R_sigma)=h`；除去这一层后，第二 quotient 与 `b_3/C_sigma` 再发生至少 `h` 深度的 unit-unit cancellation。
>
> 这给 genuine branch 一个真正的 two-level Hensel ledger，并把第二层显式接到 `q_c` source factor上。

---

## 1. 统一 sign 记号

定义

\[
\boxed{A_c:=Q a_2^2b_1^2.}
\tag{1.1}

对 `sigma=same,opp` 取符号

\[
\epsilon_{\rm same}=-1,
\qquad
\epsilon_{\rm opp}=+1.
\]

上一文件的 carrier 统一写成

\[
\boxed{
\Psi_\sigma
=A_c\beta+\epsilon_\sigma Wa_3,
\qquad
C_\sigma^2\mid\Psi_\sigma.
}
\tag{1.2}

利用

\[
\beta=Q10^{m_3}+b_3,
\]

定义 first-layer integer

\[
\boxed{
R_\sigma
:=A_cQ10^{m_3}+\epsilon_\sigma Wa_3
=Q^2a_2^2b_1^2 10^{m_3}
+\epsilon_\sigma Wa_3.
}
\tag{1.3}

则 exact 地

\[
\boxed{
\Psi_\sigma=R_\sigma+A_cb_3.
}
\tag{Layer-decomp}

---

## 2. 第一层：`C_sigma | R_sigma`

因为

\[
C_\sigma\mid b_3
\]

且

\[
C_\sigma^2\mid\Psi_\sigma,
\]

从 `(Layer-decomp)` 模 `C_sigma` 立刻得到

\[
\boxed{C_\sigma\mid R_\sigma.}
\tag{Hensel-1}

因此定义整数 quotient

\[
\boxed{
K_\sigma:=\frac{R_\sigma}{C_\sigma}.
}
\tag{2.1}

同时定义

\[
\boxed{
b_{3,\sigma}:=\frac{b_3}{C_\sigma}.}
\tag{2.2}

将 `(Layer-decomp)` 除以 `C_sigma`：

\[
\boxed{
\frac{\Psi_\sigma}{C_\sigma}
=K_\sigma+A_cb_{3,\sigma}.
}
\tag{2.3}

---

## 3. 第二层：`C_sigma | K_sigma+A_c b_{3,sigma}`

由

\[
C_\sigma^2\mid\Psi_\sigma
\]

和 `(2.3)`：

\[
\boxed{
C_\sigma
\mid
K_\sigma+A_cb_{3,\sigma}.
}
\tag{Hensel-2}

这就是 square-depth carrier 的第二层 quotient congruence。

它与第一层的变量不同：

- 第一层把 `Wa3` 与 pure decimal term `A_c Q 10^m` 对齐；
- 第二层把第一层 quotient `K_sigma` 与 denominator tail `A_c b3/C_sigma` 对齐。

---

## 4. 第一层深度事实上恰好是 `h`

固定

\[
p^h\Vert C_\sigma.
\]

main unit ledger 给

\[
p\nmid A_c.
\]

并且

\[
v_p(b_3)=h,
\]

所以

\[
\boxed{p\nmid b_{3,\sigma}.}
\tag{4.1}

因此

\[
A_cb_{3,\sigma}
\]

是 p-unit。

由 `(Hensel-2)`：

\[
K_\sigma+A_cb_{3,\sigma}
\equiv0\pmod p.
\]

若 `p|K_sigma`，左边模 `p` 会等于非零 unit `A_cb_{3,sigma}`，矛盾。故

\[
\boxed{p\nmid K_\sigma.}
\tag{K-unit}

由于

\[
R_\sigma=C_\sigma K_\sigma,
\]

得到精确赋值：

\[
\boxed{
v_p(R_\sigma)=h.
}
\tag{Hensel-1-exact}

所以 genuine square-depth 不可能全部堆在第一层；第一层只拿走恰好一份 `h`。

---

## 5. 第二层至少再承担完整 `h`

由

\[
\Psi_\sigma
=C_\sigma\left(K_\sigma+A_cb_{3,\sigma}\right)
\]

以及

\[
v_p(\Psi_\sigma)\ge2h,
\]

立刻得到

\[
\boxed{
v_p\left(K_\sigma+A_cb_{3,\sigma}\right)\ge h.}
\tag{Hensel-2-depth}

而 §4 已证明两项都是 p-units：

\[
\boxed{
p\nmid K_\sigma A_cb_{3,\sigma}.}
\tag{5.1}

因此第二层是 genuine unit-unit cancellation，不含第一层的 denominator baseline。

整个 local depth ledger 为

\[
\boxed{
\begin{array}{c|c}
\text{层}&\text{target depth}\\ \hline
R_\sigma=C_\sigma K_\sigma&h\ \text{(exact)}\\
K_\sigma+A_cb_{3,\sigma}&\ge h.
\end{array}}
\tag{Two-layer-ledger}

---

## 6. 第二层显式含 `q_c` source factor

terminal factorization 为

\[
b_3=BJC_0q_c\theta s,
\]

而

\[
C_0s=C_Lv_0.
\]

故

\[
\boxed{
b_3=BJq_c\theta C_Lv_0.}
\tag{6.1}

因为

\[
C_\sigma\mid C_L,
\]

定义

\[
C_{\rm co,\sigma}:=\frac{C_L}{C_\sigma}.
\]

则

\[
\boxed{
b_{3,\sigma}
=BJq_c\theta v_0 C_{\rm co,\sigma}.}
\tag{6.2}

代入 `(Hensel-2)`：

\[
\boxed{
C_\sigma
\mid
K_\sigma
+A_c BJq_c\theta v_0 C_{\rm co,\sigma}.
}
\tag{Source-Hensel-2}

这就是 genuine branch 到 clean source core `q_c` 的第一个 explicit second-layer interface。

注意

\[
(C_\sigma,q_c)=1
\]

沿用 main `C_L` 与 clean source 的 asymptotic coprimality（删除 `o(S)` overlap）。所以第二项中的 `q_c` 不支付 `C_sigma` depth；它只控制 moving residue 的 source shape。

---

## 7. 也可消去 `J q_c theta`

terminal overlap还有

\[
Q=JUq_c\theta.
\]

所以

\[
Jq_c\theta=\frac QU.
\]

并且 `U` 整除 `Q` 于当前 terminal identity 中。于是 `(6.2)` 还可写成

\[
\boxed{
b_{3,\sigma}
=Bv_0 C_{\rm co,\sigma}\frac QU.}
\tag{7.1}

相应第二层为

\[
\boxed{
C_\sigma
\mid
K_\sigma
+A_c Bv_0 C_{\rm co,\sigma}\frac QU.
}
\tag{Source-Hensel-2b}

两种写法用途不同：

- `(Source-Hensel-2)` 显式保留 clean core `q_c`；
- `(Source-Hensel-2b)` 把它换成 denominator prefix `Q` 与 S-unit cofactor `U`。

二者是同一 identity，不能重复计费。

---

## 8. 第一层也是一个纯 digit/discriminant congruence

`Hensel-1` 展开为

\[
\boxed{
C_\sigma
\mid
Q^2a_2^2b_1^2 10^{m_3}
+\epsilon_\sigma Wa_3.
}
\tag{Digit-Hensel-1}

所有 coefficient 在 target prime 上均为 units。因此第一层给出一个 canonical root：

\[
\boxed{
Wa_3
\equiv
-\epsilon_\sigma Q^2a_2^2b_1^2 10^{m_3}
\pmod{C_\sigma}.
}
\tag{8.1}

其 lifting quotient就是 `K_sigma`；第二层再要求 `K_sigma` 命中明确的 denominator/source residue。

这把 genuine branch真正改写成了：

\[
\boxed{
\text{一个 first digit root}
\quad+\quad
\text{一个 source-controlled second lift}.}
\tag{8.2}

---

## 9. 当前最具体的 closure target

现有 p-adic 信息已经不再模糊：

\[
R_\sigma=C_\sigma K_\sigma,
\qquad
p\nmid K_\sigma,
\]

\[
C_\sigma
\mid
K_\sigma+A_cBJq_c\theta v_0C_{\rm co,\sigma}.
\]

所以要关闭 genuine branch，最自然的新目标是证明 second-lift quotient `K_sigma` 无法同时满足：

1. 它来自 exact first-layer digit integer
   \[
   K_\sigma
   =\frac{Q^2a_2^2b_1^2 10^{m_3}+\epsilon_\sigma Wa_3}{C_\sigma};
   \]
2. 它在模 `C_sigma` 下等于一个显式 `q_c`-source residue；
3. `K_sigma` 对 target primes 为 unit；
4. `C_sigma` 与 `q_c` 只有 subexponential overlap。

若能从 `K_sigma` 抽出一个 `<C_sigma` 的 natural representative，即可真正获得 strict surplus。若完整代入只重构 discriminant identity / `b3` factorization，则记录该 second-layer route 的 no-go。

---

## 10. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`Layer-decomp`、`Hensel-1`、`Hensel-2`、`K-unit`、`Hensel-1-exact`、second-layer full depth、`Source-Hensel-2` 与 `Source-Hensel-2b`。
- **`失效/降级`**：把两种 source 写法当两份独立 congruence。
- **`待证`**：second-lift quotient `K_sigma` 的 natural short representative / strict height bound；genuine-Gaussian closure；DD 全局空性。

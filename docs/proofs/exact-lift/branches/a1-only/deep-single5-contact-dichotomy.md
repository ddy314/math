# A1 minimal diagonal: strict single-5 contact-lift dichotomy

> 日期：2026-08-20。依赖 `deep-single5-first-remainder-height.md` 与 `deep-contact-q-square-blocks-universal.md`。

本文把 strict single-5-deep 进一步分成一个显式 low-ratio strip 与一个 forced contact-lift strip。

状态：**已严格完成；single-5 尚未整体关闭。**

---

## 1. strict single-5 coordinates

single-5：

\[
A=0,
\qquad D=5^B,
\qquad B>0.
\]

2-side 非 deep，记

\[
\lambda=2^{\lambda_2},
\qquad 0\le\lambda_2\le2k
\]

（strict 5-low 时由 cross-corridor `x<=k`）。

记

\[
\nu=v_5(N_0),
\qquad Y=B+\nu.
\]

`deep-single5-first-remainder-height.md` 可保留 `lambda_2` 后写成更精确形式：

\[
5^Y<R_1<390100\,2^{\lambda_2}10^k.
\]

使用

\[
390100<5^8,
\qquad2<5^{0.431},
\qquad10<5^{1.431},
\]

得到

\[
\boxed{
B+\nu
<8+1.431k+0.431\lambda_2.}
\tag{1}

旧 `2.3k+8` 是把 `lambda_2<=2k` 代入后的粗化。

---

## 2. contact forced-lift threshold

universal contact theorem给：若

\[
\frac D\lambda>K_{z,w}T,
\]

则 `q>gcd(q,C)`，必有 genuine Q-side exponent amplification。

single-5 中

\[
\frac D\lambda=\frac{5^B}{2^{\lambda_2}}.
\]

所以 forced-lift 条件是

\[
5^B>K_{z,w}\,2^{\lambda_2}10^k.
\tag{2}

等价地，使用安全十进制：

\[
\boxed{
B>\kappa_{z,w}+1.431k+0.431\lambda_2
\Longrightarrow
\text{forced contact lift},}
\tag{3}

其中可取

\[
\boxed{
\begin{array}{c|c}
(z,w)&\kappa_{z,w}\\ \hline
(1,1)&5.92\\
(1,2)&5.42\\
(1,3)&7.33\\
(1,4)&5.97\\
(3,1)&5.50\\
(3,2)&5.01
\end{array}}
\tag{4}

这些数均严格大于 `log_5 K_(z,w)`。

---

## 3. strict single-5 的两条带

因此每个 strict single-5 candidate 必落入以下之一。

### low-ratio strip

\[
\boxed{
B<\kappa_{z,w}+1.431k+0.431\lambda_2.}
\tag{5}

这里不保证 contact exponent amplification，但 denominator slope 已显式受控。

### forced-lift strip

若 (5) 不成立，则 contact square 必强迫至少一个 selected Q-primary block在 `L_-` 或 `L_+` 中出现 strict exponent amplification。

同时 first remainder 又要求 (1)：

\[
B+
u<8+1.431k+0.431\lambda_2.
\]

所以 forced-lift strip 在 B 方向的宽度最多只有

\[
\boxed{8-\kappa_{z,w}-\nu}
\tag{6}

个 5-adic exponent units（严格不等式意义下）。

六类型的最坏常数宽度约为：

\[
\begin{array}{c|c}
(z,w)&8-\kappa_{z,w}\\ \hline
(1,1)&2.08\\
(1,2)&2.58\\
(1,3)&0.67\\
(1,4)&2.03\\
(3,1)&2.50\\
(3,2)&2.99
\end{array}
\]

而 `nu>=1` 时还会再缩 1。

所以 strict single-5 的 contact-lift区域其实只是 first-remainder top edge 附近的绝对常数宽薄带。

---

## 4. 与 parity 联立

strict 5-low 已有

\[
B>v_5(N),
\qquad
B\equiv v_5(N)\pmod2.
\]

因此在 forced-lift strip 的宽度至多约 3 的情况下，每个 fixed

\[
(k,\lambda_2,\text{prefix 5-adic branch})
\]

实际上至多只剩 1--2 个 parity-compatible B。

这为后续把 single-5 top strip 做 periodic contact-block certificate 提供了有限接口。

---

## 5. 当前意义

strict single-5 已从一个 unbounded B-half-plane 变成：

1. 显式线性 low-ratio strip (5)；
2. first-remainder 顶部一个宽度 <3 的 forced-contact-lift strip。

下一步可分别：

- low-ratio strip：继续结合 denominator funnel / prefix 5-adic root branches；
- top strip：直接利用 universal contact Q-side lifted blocks。

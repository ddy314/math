# A2 fixed `23` `eta=2` `c=2` 的 centered `a_3` map

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-source-divisor-certificate.md`、`spontaneous-cq-fixed23-eta2-c2-centered-source-slot.md`、`spontaneous-cq-fixed23-eta2-c2-full-a3-crt.md`。
>
> **严格状态：**source divisor certificate以 `theta` 参数化每个候选，并分别计算 binary Hensel root。本文改用 centered variable `varrho=20L_*-theta`。由于 `L_*` 同时含完整 `2^m` 与 `5^lambda`，局部有 `theta=-varrho`；再利用 `gtheta=S_lambda(c_u)`，binary polynomial在变量 `u=varrho*a_3` 下完全消去 `theta,g,varrho`，变成只依赖 `(lambda,c_u)` 的唯一 Hensel root。long-5 residue也化成 `varrho^{-1}` 的仿射式。因此同一 `(lambda,c_u)` 下所有 source divisors共享一套预计算 local data。

---

## 1. centered source variable

定义

\[
c:=c_Qc_u=1587c_u,
\]

\[
\boxed{
S:=\mathscr S_\lambda(c_u)
=5^{3\lambda}+c.}
\tag{1.1}

已有

\[
g\theta=S.
\tag{1.2}

同时

\[
L_*=2^m5^\lambda c_u,
\qquad
\boxed{\varrho:=20L_*-\theta.}
\tag{1.3}

centered source-slot proof给

\[
\frac14L_*<\varrho<\frac12L_*,
\qquad
\gcd(\varrho,L_*)=1.
\tag{1.4}

特别地 `varrho` 是 `2`-进与 `5`-进 unit。

因为

\[
2^m\mid L_*,
\qquad
5^{\lambda-1}\mid L_*,
\]
在两套 local rings 中统一有

\[
\boxed{\theta\equiv-\varrho.}
\tag{1.5}

---

## 2. binary polynomial 在 `u=varrho a_3` 下完全 source-only

前面的 binary bridge为

\[
\theta\left(\frac{g^2}{4}+a_3^2\right)
-ca_3
\equiv0
\pmod{2^m}.
\tag{2.1}

由 (1.2)、(1.5)：

\[
g\equiv-S\varrho^{-1}\pmod{2^m}.
\tag{2.2}

将其代入 (2.1)：

\[
-\varrho
\left(
\frac{S^2}{4\varrho^2}+a_3^2
\right)
-ca_3
\equiv0.
\]
乘以 unit `-varrho`：

\[
\varrho^2a_3^2
+c\varrho a_3
+\frac{S^2}{4}
\equiv0
\pmod{2^m}.
\]
定义

\[
\boxed{u:=\varrho a_3.}
\tag{2.3}

得到完全 source-only 的二次式

\[
\boxed{
F_{\rm cent}(u)
:=u^2+cu+\frac{S^2}{4}
\equiv0
\pmod{2^m}.}
\tag{2.4}

这里 `S` 被 `4` 整除，因为 `S=gtheta`、`v_2(g)>=2`，所以 `S^2/4` 为整数。

---

## 3. centered binary root 对每个 `(lambda,c_u)` 唯一

导数为

\[
\boxed{F_{\rm cent}'(u)=2u+c.}
\tag{3.1}

`c=1587c_u` 为奇数，所以

\[
\boxed{F_{\rm cent}'(u)\equiv1\pmod2.}
\tag{3.2}

模 `2` 时 `S^2/4` 为偶数，因为 `v_2(S)>=2`，而 `u` 必为奇数，因此

\[
F_{\rm cent}(1)
\equiv1+1+0
\equiv0\pmod2.
\]
ordinary Hensel lemma给出唯一

\[
\boxed{u_2(\lambda,c_u)\pmod{2^m}}
\tag{3.3}

满足 (2.4)。

于是对同一 `(lambda,c_u)` 下任何 admissible source divisor `theta`，只需计算

\[
\varrho=20L_*-\theta
\]
并取 inverse：

\[
\boxed{
a_{3,(2)}
\equiv
u_2\varrho^{-1}
\pmod{2^m}.}
\tag{3.4}

binary Hensel tree只需预计算一次。

---

## 4. long-5 root 也变成 centered affine map

source-divisor certificate 的 long-5 residue为

\[
a_{3,(5)}
\equiv
\frac c2
\left(
\theta^{-1}
-45\iota\,2^{3\lambda+2}
\right)
\pmod{5^{\lambda-1}}.
\tag{4.1}

由 (1.5)：

\[
\theta^{-1}\equiv-\varrho^{-1}
\pmod{5^{\lambda-1}}.
\]
所以

\[
\boxed{
a_{3,(5)}
\equiv
-\frac c2\varrho^{-1}
-\frac{45c}{2}\iota\,2^{3\lambda+2}
\pmod{5^{\lambda-1}}.}
\tag{4.2}

固定 `(lambda,c_u,iota)` 后，第二项是常量，divisor dependency只在 `varrho^{-1}`。

若改写成 `u=varrho a_3`：

\[
\boxed{u_{(5)}
\equiv
-\frac c2
-\frac{45c}{2}\iota\,2^{3\lambda+2}\varrho
\pmod{5^{\lambda-1}}.}
\tag{4.3}

因此 `u` 的 binary residue完全固定，而 5-adic residue对 `varrho` 只是线性函数。

---

## 5. full CRT 的 centered implementation

对 fixed `(lambda,c_u)` 可预计算：

\[
A:=2^m,
\qquad
B:=5^{\lambda-1},
\qquad
u_2\pmod A.
\]

然后每个 source divisor只需：

1. `varrho=20L_*-theta`；
2. 检查 centered slot `L_*/4<varrho<L_*/2`；
3. 计算 `varrho^{-1} mod A,B`；
4. 用 (3.4)、(4.2) 得两条 `a_3` residue；
5. 加入 canonical `c_Q` root并做 full CRT `1/15870` cell test。

这把每 divisor 的 expensive local lifting替换为常数次 modular inverse / affine arithmetic。

---

## 6. source discriminant interpretation

(2.4) 的判别式为

\[
\begin{aligned}
\Delta_{\rm cent}
&=c^2-S^2\\
&=c^2-(5^{3\lambda}+c)^2\\
&=\boxed{-5^{3\lambda}(5^{3\lambda}+2c).}
\end{aligned}
\tag{6.1}

由于 `c=1587c_u` 且 `c_u=1 mod4`，直接检查有

\[
\Delta_{\rm cent}\equiv1\pmod8,
\]
所以它在 `Z_2^times` 中确实为平方。这个 character没有提供额外 obstruction；真正有用的信息是 derivative unit导致的**唯一 centered branch**。

---

## 7. updated frontier

当前 source divisor family 的 local dependence 已降到：

\[
\boxed{
\theta
\longleftrightarrow
\varrho
\longmapsto
\left(
\nu_2\varrho^{-1},
-\frac c2\varrho^{-1}-K_5
\right),}
\]
其中 `u_2` 和 `K_5` 对固定 `(lambda,c_u,orientation)` 都预先确定。

因此若继续统一 closure，最自然的对象已是 centered divisor `varrho` 在 full CRT cell 中的 Möbius/affine image，而不是重新研究 `g,a_3` 的 local Hensel lifting。
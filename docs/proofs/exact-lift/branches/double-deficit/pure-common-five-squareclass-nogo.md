# DD pure common-scale 的 5-adic square-class no-go

> **依赖：** [`high-funnel-two-adic-balance.md`](high-funnel-two-adic-balance.md)、
> [`high-funnel-denominator-max-lock.md`](high-funnel-denominator-max-lock.md) 与
> `core.md` 的 overlap parameterization / scale-free quadratic。
>
> **严格状态：** `已严格完成（pure-common conditional audit）`。
> 本文不关闭 pure common-scale branch；它证明一个重要方法边界：
> scale-free quadratic 在该 branch 中产生的看似深达 `5^{2g_5}` 的 Hensel
> 条件，约去 forced common scale 后只剩一个普通 5-adic unit square class。
> 因而继续增加同一个 5-adic Hensel 深度不会产生正线性高度障碍。

---

## 1. pure common-scale ledger

假设 `Final-5-lock` 落在 endpoint

\[
\boxed{
q_5=n_5=0,
\qquad
m=4g,
\qquad
T=2g,
}
\tag{Pure}

其中 `g:=g_5>0`。

`high-funnel-two-adic-balance.md` 已证明 denominator 5-depth 必为

\[
\boxed{
v_5(b_1)=g,
\qquad
v_5(b_2)=0,
\qquad
v_5(b_3)=2g.
}
\tag{1.1}

令

\[
\omega=(10^m,b_3),
\qquad
L=10^m/\omega.
\]

于是

\[
\boxed{v_5(\omega)=v_5(L)=2g.}
\tag{1.2}

在 overlap 参数化

\[
Q=\eta Q_1,
\qquad
\tau=\eta v,
\qquad
u=LQ_1,
\]

\[
D=vc\lambda,
\qquad
C=\lambda w,
\qquad
g_*=vc\lambda r
\]

中，`q_5=0` 和 `tau` 为 5-unit 给

\[
\eta,Q_1,v\ \text{均为 5-units}.
\]

又 `v_5(H_sph)=0`，所以 `D=(H_sph,q_lcm)` 为 5-unit；因此

\[
\boxed{v_5(c)=v_5(\lambda)=v_5(w)=0.}
\tag{1.3}

`a=ca_0` 且 pure branch有 `v_5(a)=0`，故

\[
\boxed{v_5(a_0)=0.}
\tag{1.4}

最后 denominator overlap 在 5 处为

\[
v_5(g_*)=g,
\]

所以由 `g_*=vc lambda r`：

\[
\boxed{v_5(r)=g.}
\tag{1.5}

定义 5-units

\[
L'=L/5^{2g},
\qquad
r'=r/5^g,
\qquad
\omega'=\omega/5^{2g}.
\]

---

## 2. 清分母后的 scale-free quadratic

`core.md` 的 scale-free quadratic为

\[
\begin{aligned}
0={}&
L c^4\lambda^2r^2w(LQ_1+2v)x^2\\
&-2L c^4\lambda^2r^2v(LQ_1+v)A_{12}10^d x\\
&+\eta^2\mathcal N_{12}Q_1w,
\end{aligned}
\tag{SFQ}

其中

\[
x=a_0/\omega.
\]

乘 `omega^2` 后，三项的 5-depth分别为

\[
4g,
\qquad
d+6g,
\qquad
4g.
\]

所以除以 `5^{4g}w` 后得到

\[
\boxed{
L'c^4\lambda^2r'^2(LQ_1+2v)a_0^2
+\eta^2\mathcal N_{12}Q_1\omega'^2
\equiv0
\pmod{5^{d+2g}}.
}
\tag{2.1}

这确实是一个很深的 two-unit cancellation；但下面说明其深度本身没有新信息。

---

## 3. prefix norm 在 `5^{2g}` 下退化成一个平方

写

\[
X=a_1b_2,
\qquad
Y=a_2b_1,
\qquad
\mathcal N_{12}=X^2+Y^2.
\]

由 `(1.1)` 与 reducedness：

\[
v_5(X)=0,
\qquad
v_5(Y)\ge g.
\]

因此

\[
\boxed{
\mathcal N_{12}\equiv X^2\pmod{5^{2g}}.
}
\tag{3.1}

将 `(2.1)` 降到模 `5^{2g}` 并使用 `(3.1)`，所有出现的分母都是
5-units，于是

\[
\boxed{
-\frac{Q_1}{L'(LQ_1+2v)}
\in
\left((\mathbf Z/5^{2g}\mathbf Z)^\times\right)^2.
}
\tag{3.2}

更显式地，右边的一个平方根由

\[
\frac{c^2\lambda r'a_0}{\eta X\omega'}
\]

给出（符号和选取不影响 square class）。

---

## 4. square class 精确化成 `UV`

S-unit phase有

\[
LQ_1=u=2\cdot5^TU,
\qquad
v=V,
\qquad
T=2g.
\]

所以

\[
\boxed{L'Q_1=2U.}
\tag{4.1}

并且

\[
LQ_1+2v
=2(5^TU+V)
=2^{H+1}Z.
\tag{4.2}

由 `(4.1)`–`(4.2)`：

\[
-\frac{Q_1}{L'(LQ_1+2v)}
=
-\frac{Q_1^2}{2^{H+2}UZ}.
\tag{4.3}

`Q_1^2` 是平方，而 `-1` 在 `Z_5` 中也是平方；`2^{H+2}` 与
`2^H` 只差平方因子 `4`。故 `(3.2)` 等价于

\[
\boxed{
2^HUZ
\in
\left((\mathbf Z/5^{2g}\mathbf Z)^\times\right)^2.
}
\tag{4.4}

但 phase equation

\[
2^HZ=5^{2g}U+V
\]

模 `5^{2g}` 给

\[
2^HZ\equiv V\pmod{5^{2g}}.
\]

最终得到最简形式

\[
\boxed{
UV
\in
\left((\mathbf Z/5^{2g}\mathbf Z)^\times\right)^2.
}
\tag{UV-square}

---

## 5. 为什么这没有线性高度收益

对奇素数 `p`，一个 `p`-adic unit是模 `p^k` 的平方，当且仅当它模 `p`
是平方；任意非零平方根随后由普通 Hensel lemma唯一提升。

所以 `(UV-square)` 的全部深度条件严格等价于

\[
\boxed{
UV\text{ 是模 }5\text{ 的 quadratic residue}.
}
\tag{UV-mod5}

因此 `2g` 即使随 `S` 线性增长，也不会产生 `2g` 份独立约束。它只保留
一个 square-class bit。

这正是 common-scale branch 与 genuine angular branch 的差别：前者的深
5-adic denominator可以被一个 unit square root自动吸收，继续做 same-prime
Hensel lifting不会得到新的 Archimedean 费用。

---

## 6. 方法边界

- **`已严格完成`**：`(2.1)`、`(UV-square)`、`(UV-mod5)`。
- **`失效/降级`**：把 pure common-scale 的 `5^{2g}` Hensel 深度本身视作线性高度 obstruction。
- **`待证`**：把 `UV` 的 square class 与 moving split-prime orientation / `q,Z` rough allocation 联立；或从另一个独立 carrier得到第二个不兼容的 square class。

所以 pure common-scale 的下一步应该是跨 prime 或跨 carrier，而不是继续提高同一个 5-adic lifting 阶数。

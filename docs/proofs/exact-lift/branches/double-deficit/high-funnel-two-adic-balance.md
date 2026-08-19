# DD high-funnel 的 2-adic shallow-gap 与 tail-root balance

> **依赖：** `core.md` 的 `t_2=1` S-unit funnel、overlap 参数化与 scale-free quadratic，
> [`high-funnel-denominator-max-lock.md`](high-funnel-denominator-max-lock.md) 的 `Final-5-lock`，以及固定目标 Schmidt Subspace Theorem。
>
> **严格状态：** `已严格完成（canonical t_2=1 double-resonant funnel）`。
> 本文不声称新的全 DD 数值 `limsup`。新增的核心是两个 exact finite-height 结论：
>
> 1. 在 `b_3` 二进 unique maximum、`t_2=1` 的 canonical funnel 中，sphere gap 必为二进浅因子
>    \[
>    \boxed{v_2(H_{\rm sph}-y_3)=1.}
>    \]
> 2. unified tail-root 的二进投影给 exact dichotomy
>    \[
>    \boxed{
>    d\le m+2\mathfrak q+\mathfrak n+\mathfrak g-1
>    }
>    \tag{2-short}
>    \]
>    或
>    \[
>    \boxed{
>    2\mathfrak g=m+\mathfrak q+\ell-2.
>    }
>    \tag{2-balanced}
>    \]
>
> 其中
> \(\mathfrak q=v_2(Q)\)、\(\mathfrak g=v_2(G)\)、
> \(\mathfrak n=v_2(\mathcal N_{12})\)，且
> \[
> \ell=v_2(L)=\begin{cases}1,&\mathfrak q=0,\\0,&\mathfrak q\ge1.\end{cases}
> \]
>
> 在 `Final-5-lock` 上，本文还恢复一个 defect-aware Schmidt budget
> \[
> \boxed{
> (1+a)m+2a\mathfrak q+a\mathfrak n+2\log_{10}\gamma_0
> \le3S+o(S),
> }
> \]
> 其中 \(a=\log_{10}2\)，
> \(\gamma=2^{\mathfrak g}5^{g_5}\gamma_0\)、\((\gamma_0,10)=1\)。
> 这些公式是后续处理 pure/common-scale sheet 的新接口。

---

## 1. 2-adic denominator baseline

仍在旧证明已经严格压出的 canonical funnel：

\[
5\text{-resonance}
+ b_3\text{ 二进 unique maximum}
+t_2=1
+2\text{-resonance}.
\]

记

\[
\mathfrak B:=v_2(b_3),\qquad
\mathfrak q:=v_2(Q),\qquad
\mathfrak g:=v_2(G),\qquad
\mathfrak n:=v_2(\mathcal N_{12}).
\]

`t_2=1` 的定义给

\[
\boxed{v_2(\kappa)=\mathfrak g+1.}
\tag{1.1}
\]

由 tail weight

\[
\kappa b_3=10^mQG
\]

取二进赋值：

\[
\boxed{
\mathfrak B=m+\mathfrak q-1.
}
\tag{B2}

因为 `b_3` 是二进 unique maximum，整数球面中的第三坐标是唯一二进单位坐标；因此

\[
\boxed{v_2(y_3)=v_2(H_{\rm sph})=0.}
\tag{1.2}

令

\[
\omega=(10^m,b_3),\qquad L=10^m/\omega.
\]

由 `(B2)`：

\[
\boxed{
\ell:=v_2(L)
=\begin{cases}
1,&\mathfrak q=0,\\
0,&\mathfrak q\ge1.
\end{cases}}
\tag{ell}

确实，`q=0` 时 `mathfrak B=m-1`，否则 `mathfrak B>=m`。

---

## 2. overlap 参数在 2 处的精确账本

使用 `core.md` 的 overlap 参数：

\[
\eta=(Q,\tau),\quad Q=\eta Q_1,\quad \tau=\eta v,
\]

\[
u=LQ_1,\qquad (LQ_1,v)=1,
\]

以及

\[
D=vc\lambda,\quad C=\lambda w,\quad
g_*=vc\lambda r,
\]

\[
G=\varepsilon vc^2\lambda r.
\]

在当前 funnel 中

\[
u=2\cdot5^TU,\qquad v=V,\qquad (UV,10)=1.
\]

所以

\[
\boxed{v_2(u)=1,\qquad v_2(v)=0.}
\tag{2.1}

由 `u=LQ_1` 与 `(ell)`：

\[
\boxed{v_2(Q_1)=1-\ell.}
\tag{2.2}

又

\[
v_2(\eta)=\mathfrak q-v_2(Q_1)
=\boxed{\mathfrak q-1+\ell.}
\tag{2.3}

`b_3` 二进 unique maximum 时，denominator overlap
\[
g_*=(b_1,b_2)(\operatorname{lcm}(b_1,b_2),b_3)
\]
在 2 处恰恢复 prefix 总深度：

\[
\boxed{v_2(g_*)=\mathfrak g.}
\tag{2.4}

另一方面 `v,c,lambda` 都是二进单位，因此

\[
\boxed{v_2(r)=\mathfrak g.}
\tag{2.5}

最后，

\[
u+v=5^TU+V=2^HZ
\]

且 `epsilon,w` 为二进单位；所以

\[
\boxed{v_2(LQ_1+v)=H,}
\tag{2.6}

\[
LQ_1+2v=2(5^TU+V)=2^{H+1}Z,
\]

故

\[
\boxed{v_2(LQ_1+2v)=H+1.}
\tag{2.7}

---

## 3. sphere 的两个二进因子只能有一个浅因子

令

\[
D_-:=v_2(H_{\rm sph}-y_3).
\]

由 `(1.2)`，`H_sph,y_3` 都是奇数，因此 `H_sph-y_3` 与
`H_sph+y_3` 中恰有一个的二进赋值为 1。

另一方面

\[
y_1^2+y_2^2
=\left(\frac{q_{\rm lcm}}G\right)^2\mathcal N_{12}.
\]

因为 `b_3` 是二进 unique maximum，

\[
v_2(q_{\rm lcm})=\mathfrak B,
\]

所以

\[
\boxed{
R:=v_2(y_1^2+y_2^2)
=2(\mathfrak B-\mathfrak g)+\mathfrak n.
}
\tag{3.1}

sphere factorization

\[
(H_{\rm sph}-y_3)(H_{\rm sph}+y_3)=y_1^2+y_2^2
\]

于是

\[
\boxed{D_-\in\{1,R-1\}.}
\tag{3.2}

又 `H_sph-y_3=La`，所以若记

\[
A_2:=v_2(a),
\]

则

\[
\boxed{D_-=\ell+A_2.}
\tag{3.3}

---

## 4. scale-free quadratic 排除 deep-gap orientation

`core.md` 的 scale-free quadratic 为

\[
\begin{aligned}
0={}&
L c^4\lambda^2r^2w(LQ_1+2v)x^2\\
&-2L c^4\lambda^2r^2v(LQ_1+v)A_{12}10^d x\\
&+\eta^2\mathcal N_{12}Q_1w,
\end{aligned}
\tag{SFQ}
\]

其中

\[
x=\frac{a_0}{\omega},\qquad a=ca_0.
\]

在当前二进位置，`c` 为二进单位，所以

\[
v_2(a_0)=A_2.
\]

而

\[
v_2(\omega)=m-\ell,
\]

故

\[
v_2(x)=A_2-m+\ell.
\tag{4.1}

令 `(SFQ)` 三项赋值依次为 `V_1,V_2,V_3`。使用 §2 的账本及
2-resonance

\[
\boxed{
\mathfrak f+\mathfrak g+3
=2m+2\mathfrak q+\mathfrak n,
}
\tag{2-res}

并且

\[
\mathfrak f=v_2(\kappa+2G)=\mathfrak g+H+1,
\]

可逐项化简为

\[
\boxed{
V_1=2\mathfrak q+\mathfrak n+3\ell-3+2A_2,
}
\tag{4.2}

\[
\boxed{
V_3=2\mathfrak q+\mathfrak n-1+\ell,
}
\tag{4.3}

以及

\[
\boxed{
V_2=d-m+1+2\ell+2\mathfrak g+v_2(A_{12})+A_2.
}
\tag{4.4}

所以

\[
\boxed{V_1-V_3=2(D_--1).}
\tag{4.5}

反设 sphere gap 取深因子：

\[
D_-=R-1>1.
\]

由 `(B2)`、`(3.1)`、`(3.3)` 代回 `(4.4)-(4.3)`，所有 valuation
变量精确消去，得到

\[
\boxed{
V_2-V_3=d+m-1+v_2(A_{12})>0.
}
\tag{4.6}

同时 `(4.5)` 给 `V_1>V_3`。因此 `(SFQ)` 中第三项是唯一最浅项，
三个整数/有理数项不可能相加为零，矛盾。

故只剩浅因子：

\[
\boxed{v_2(H_{\rm sph}-y_3)=1.}
\tag{Shallow-gap}

结合 `(3.3)`：

\[
\boxed{
v_2(a)=1-\ell
=\begin{cases}
0,&\mathfrak q=0,\\
1,&\mathfrak q\ge1.
\end{cases}}
\tag{a2-lock}

这是 exact finite-height conclusion，不使用任何 asymptotic equality ray。

---

## 5. tail-root 的 2-adic exact dichotomy

unified tail-root identity为

\[
\boxed{
\mathscr T a_3
=\kappa G^2 10^dA_{12}
+\eta_0(\kappa+G)W,
}
\tag{5.1}

其中

\[
\mathscr T=\frac{\kappa^2(\kappa+2G)}{10^m},
\qquad \eta_0\in\{\pm1\}.
\]

模 `2^d`：

\[
\boxed{
\mathscr T a_3
\equiv
\eta_0(\kappa+G)W
\pmod{2^d}.}
\tag{Tail-2}

因为 `b_3` 偶且 `(a_3,b_3)=1`，`a_3` 为奇数。

由 `(1.1)`、`(2-res)`：

\[
\boxed{
r_2:=v_2(\mathscr T a_3)
=m+2\mathfrak q+\mathfrak n+\mathfrak g-1.
}
\tag{r2}

现在使用

\[
\Xi=|\mathcal M-C_0a|,
\qquad W=L\Xi,
\]

以及

\[
C_0=LQ\frac{\kappa+2G}{\kappa}.
\]

由 `(a2-lock)` 可得

\[
\boxed{
A:=v_2(C_0a)
=2m+3\mathfrak q+\mathfrak n-2\mathfrak g-3.
}
\tag{5.2}

又 `high-funnel-gap-depth.md` 中的 decimal factorization实际上同时给

\[
\mathcal M=10^d(10^{n_2}b_1y_1+b_2y_2),
\]

所以

\[
\boxed{v_2(\mathcal M)\ge d.}
\tag{5.3}

因此：

- 若 `A<d`，则 `v_2(Xi)=A`；
- 若 `A>=d`，则 `v_2(Xi)>=d`。

并且 `t_2=1` 给 `v_2(kappa+G)=mathfrak g`。

若 `d<=r_2`，直接得到第一支

\[
\boxed{d\le m+2\mathfrak q+\mathfrak n+\mathfrak g-1.}
\tag{2-short}

现在设 `d>r_2`。`Tail-2` 要求右边也有恰好 `r_2<d` 的 valuation；
故不可能处在 `A>=d`，只能 `A<d`，而且

\[
r_2
=\mathfrak g+\ell+A.
\]

代入 `(r2)` 与 `(5.2)`：

\[
\boxed{2\mathfrak g=m+\mathfrak q+\ell-2.}
\tag{2-balanced}

因此 `(2-short)` 与 `(2-balanced)` 穷尽当前 funnel。

---

## 6. Schmidt lower bound 的 defect-aware 重写

写 gcd-normal form

\[
\kappa=\gamma u,\qquad G=\gamma v,
\]

以及 `t_2=1` S-unit phase

\[
u=2\cdot5^TU,\qquad v=V,
\]

\[
5^TU+V=2^HZ.
\]

再写

\[
\boxed{
\gamma=2^{\mathfrak g}5^{g_5}\gamma_0,
\qquad (\gamma_0,10)=1.
}
\tag{6.1}

由 decimal pinning

\[
\log_{10}\kappa=2S+O(1),
\qquad
\log_{10}(\kappa+2G)=2S+O(1).
\]

而

\[
\kappa=2\gamma5^TU,
\]

\[
\kappa+2G=2\gamma2^HZ.
\]

所以

\[
\begin{aligned}
\log_{10}U+\log_{10}Z
={}&4S-2\log_{10}\gamma-aH-bT+O(1),
\end{aligned}
\tag{6.2}

其中常数 `-2a` 已吸收到 `O(1)`。

二进 resonance给

\[
H=2m+2\mathfrak q+\mathfrak n-2\mathfrak g-4,
\tag{6.3}

五进 resonance给

\[
3T=2m+2q_5-2g_5+n_5.
\tag{6.4}

将 `(6.1)`–`(6.4)` 代回 `(6.2)`，`mathfrak g` 完全消去，得到

\[
\boxed{
\begin{aligned}
\log_{10}U+\log_{10}Z
={}&4S
-\frac{2(1+2a)}3m\\
&-(2a\mathfrak q+a\mathfrak n)
-\frac b3(2q_5+4g_5+n_5)\\
&-2\log_{10}\gamma_0+O(1).
\end{aligned}}
\tag{UZ-exact-height}

旧固定目标 Schmidt Subspace Theorem 对整个该 S-unit funnel给

\[
\liminf\frac{\log_{10}U+\log_{10}Z}{S}\ge1.
\]

因此任何无界 sequence 满足

\[
\boxed{
\frac{2(1+2a)}3m
+2a\mathfrak q+a\mathfrak n
+\frac b3(2q_5+4g_5+n_5)
+2\log_{10}\gamma_0
\le3S+o(S).
}
\tag{Subspace-defect}

在 [`high-funnel-denominator-max-lock.md`](high-funnel-denominator-max-lock.md) 的
`Final-5-lock`

\[
m=2q_5+4g_5+n_5
\]

上，它进一步化成

\[
\boxed{
(1+a)m
+2a\mathfrak q+a\mathfrak n
+2\log_{10}\gamma_0
\le3S+o(S).
}
\tag{Subspace-Final5}

这比此前只保留 multiplicative height 的 `Combined-height` 在该 sheet 上更强。

---

## 7. `Final-5` 上的两个 sector diagnostics

以下只是当前 sheet 的显式诊断，不替代仓库已经更强的全局非有效
`limsup < 6.308883...`。

### 7.1 整个 `Final-5` sheet 的粗 bound

由 small-factor upper 与 exact

\[
v_2(F_-)=\mathfrak f+1,\qquad v_5(F_-)=k_5=m-g_5
\]

可直接得到

\[
\boxed{
n
<4S+b m
-2a\mathfrak q-a\mathfrak n
+a\mathfrak g+b g_5+O(1).
}
\tag{Raw-F}

又 `G=gamma V` 且 `V>=1`，故

\[
\boxed{
a\mathfrak g+b g_5+\log_{10}\gamma_0\le S+O(1).}
\tag{Gamma-height}

代入 `(Raw-F)`：

\[
n<5S+b m-2a\mathfrak q-a\mathfrak n-\log_{10}\gamma_0+O(1).
\]

再用 `(Subspace-Final5)`，丢掉非负 defect，得到

\[
\boxed{
\limsup_{\rm Final5}\frac nS
\le
5+\frac{3b}{1+a}
=
\frac{8+2a}{1+a}
=6.611730721041\ldots.
}
\tag{Final5-coarse}

这个数值高于已有全 DD strict limsup bound，因此它的意义是
`Final-5` sheet 的内部收费结构，不是新的全局常数。

### 7.2 `2-balanced` sector

由 `(2-balanced)`：

\[
\mathfrak g=\frac12m+\frac12\mathfrak q+O(1).
\]

代回 `(Raw-F)`：

\[
n
<4S+\left(1-\frac a2\right)m
-\frac{3a}{2}\mathfrak q-a\mathfrak n
+b g_5+O(1).
\]

`Final-5-lock` 给

\[
4g_5\le m.
\]

所以

\[
n
<4S+rac{5-3a}{4}m+O(1)
\]

（继续丢掉非正 defect）。再用 `(Subspace-Final5)`：

\[
\boxed{
\limsup_{\rm Final5,\,2-balanced}
\frac nS
\le
4+\frac{3(5-3a)}{4(1+a)}
=
\frac{31+7a}{4(1+a)}
=6.361730721041\ldots.
}
\tag{Balanced-sector}

同样，这个 sector 数值仍高于仓库已有的全局 strict `6.308883...`，
所以不能被宣传为新的 DD 全局 bound。

---

## 8. pure common-scale endpoint 的额外 exact shape

`Final-5-lock` 的 LP endpoint为

\[
q_5=n_5=0,\qquad m=4g_5,\qquad T=2g_5.
\]

此时 `Q=b_1 10^{m_2}+b_2` 是 5-unit，而

\[
v_5(b_1)+v_5(b_2)=g_5.
\]

因为第一项 `b_1 10^{m_2}` 具有正 5-depth（若 `g_5>0`），要使 `Q`
为 5-unit，必须

\[
\boxed{v_5(b_1)=g_5,\qquad v_5(b_2)=0.}
\tag{Pure-denominator5}

从 reduced-tail identities

\[
u=2\cdot5^TU,\qquad Q=Uq,\qquad ut=10^mQ,\qquad b_3=Vt
\]

还得到 exact

\[
\boxed{
b_3=2^{m-1}5^{m-T}qV.}
\tag{b3-reduced}

因为 `b_3` 恰有 `m` 位：

\[
10^{m-1}\le b_3<10^m.
\]

除以 `(b3-reduced)` 的 smooth factor可得

\[
\boxed{
bT+a-1\le\log_{10}(qV)<bT+a.}
\tag{qV-window}

特别地 pure common-scale 中

\[
\boxed{
\log_{10}(qV)=\frac b2m+O(1).
}
\tag{Pure-qV}

这说明剩余 rough denominator freedom并非任意；`qV` 本身被锁在一个固定高度窗口。

---

## 9. 当前边界

本文新增的 `Shallow-gap` 与 `2-short/2-balanced` 是 exact finite-height
结构。它们把最后 high-funnel sheet 的二进自由度压成了两个明确状态。

目前还不能据此宣布 DD closure，也不能给出低于既有 global strict
`6.308883...` 的显式常数。下一步应优先处理：

1. `2-short` 中 `q,V,gamma_0` 的 rough-height allocation；
2. `2-balanced` 中 pure common-scale 的 deep 5-adic unit cancellation；
3. 将 `(qV-window)` 与 `u(u+2v)|F_-Q` 的大除数连接，寻找不能由 `q` 支付的 `Z`-rough mass。

# DD canonical `t_2=1` funnel 的 exact small-factor normalization

> **依赖：** `core.md` §27.33 的 gcd-normal form、`t_2=1` S-unit phase、通用恒等式
> \(F_-Q(\kappa+G)=E\kappa(\kappa+2G)\)、§35 的 exact small-factor factorization、§37 的 overlap 参数化。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
>
> 本文修正一个容易混淆的记号点：§6 gcd-normal form 的 reduced quotient 与后续
> `Q=Uq` 中的 source factor `q` 并不必然相同；两者只差一个 `2,5`-smooth gcd。
> 正确拆分后，旧 terminal 工作中看似需要研究的 `gcd(q,Z)` 可以从 exact
> small-factor identity 中完全消去。最终得到
> \[
> \boxed{
> F_-=
> \frac{2^{H+2}5^TZ}{(2\cdot5^T,q)}
> \;a\frac{g_*}{V}.
> }
> \]
> 特别地 `Z` 是 10-unit，因此
> \[
> \boxed{Z\mid F_-.}
> \]

---

## 1. 区分两个 `q`

gcd-normal form 先写

\[
\kappa=\gamma u,
\qquad
G=\gamma v,
\qquad
(u,v)=1,
\]

并定义

\[
d_0=(u,Q),
\qquad
u=d_0r,
\qquad
Q=d_0q_{\rm red},
\qquad
(r,q_{\rm red})=1,
\]

其中

\[
r\mid10^m.
\]

在 canonical `t_2=1` S-unit phase 中，另一方面写

\[
\boxed{
u=2\cdot5^TU,\qquad v=V,}
\tag{1.1}
\]

\[
\boxed{Q=Uq,}
\tag{1.2}
\]

并有

\[
(UV,10)=1,
\qquad
(U,V)=1.
\]

这里 `(1.2)` 中的 `q` 不应未经审计地与 `q_red` 认同。令

\[
\boxed{r_0:=2\cdot5^T,}
\qquad
\boxed{s:=(r_0,q).}
\tag{1.3}

则

\[
(u,Q)
=(r_0U,Uq)
=U(r_0,q)
=Us.
\]

所以真正的 gcd-normal reduced pair 为

\[
\boxed{
r=\frac{r_0}{s},
\qquad
q_{\rm red}=\frac q s.
}
\tag{1.4}

特别地

\[
(r,q_{\rm red})=1.
\]

这正是此前直接从 `Q=Uq` 推断 `(q,10)=1` 的错误所在：只有
`q_red` 与 `r` 互素；source factor `q` 自己可以携带被 `s` 记录的
`2,5`-depth。

---

## 2. tail recovery 精确给出 `L` 与 `tau`

原 gcd-normal tail recovery 为

\[
\boxed{b_3=vt,\qquad ut=10^mQ.}
\tag{2.1}

代入 `(1.1)`、`(1.2)`：

\[
r_0Ut=10^mUq,
\]

约去 `U`：

\[
\boxed{r_0t=10^mq.}
\tag{2.2}

使用 `(1.4)`：

\[
rt=10^mq_{\rm red}.
\]

因为 `(r,q_red)=1` 且 `r|10^m`，有

\[
\boxed{
t=\frac{10^m}{r}\,q_{\rm red}.}
\tag{2.3}

现在 `b_3=Vt`，而 `(r,V)=1` 来自 `(u,v)=1`。于是

\[
\begin{aligned}
\omega
&=(10^m,b_3)\\
&=\left(10^m,
V\frac{10^m}{r}q_{\rm red}\right)\\
&=\frac{10^m}{r}
\,(r,Vq_{\rm red})\\
&=\frac{10^m}{r}.
\end{aligned}
\]

因此 DD tail normalization

\[
L=\frac{10^m}{\omega},
\qquad
\tau=\frac{b_3}{\omega}
\]

精确化成

\[
\boxed{
L=r=\frac{2\cdot5^T}{s},
\qquad
\tau=q_{\rm red}V=\frac q sV.
}
\tag{Tail-reduced}

这里没有渐近误差。

---

## 3. reduced source factor自动整除真实 decimal determinant

DD determinant 为

\[
\boxed{
E=b_3A_{12}10^d-a_3Q.
}
\tag{3.1}

由 `(Tail-reduced)`：

\[
b_3=\omega q_{\rm red}V,
\qquad
Q=Usq_{\rm red}.
\]

所以

\[
\boxed{q_{\rm red}\mid E.}
\tag{3.2}

定义

\[
\boxed{
E_0:=\frac{E}{q_{\rm red}}
=\omega VA_{12}10^d-a_3Us.
}
\tag{3.3}

这一步是 exact integer cancellation；不能把它错误加强为 `q|E`，因为
`s` 未必为 1。

---

## 4. universal identity 中的 rough `q` 层全部约掉

令

\[
\boxed{X:=2^HZ,\qquad Y:=5^TU.}
\tag{4.1}

S-unit phase 为

\[
X-Y=V.
\]

于是

\[
u=2Y,
\qquad
u+v=X+Y,
\qquad
u+2v=2X.
\]

通用恒等式

\[
F_-Q(\kappa+G)=E\kappa(\kappa+2G)
\]

在

\[
Q=Uq,
\quad
\kappa=2\gamma5^TU,
\quad
G=\gamma V
\]

下化为

\[
\boxed{
F_-q(X+Y)
=4E\gamma\,2^H5^TZ.
}
\tag{4.2}

使用

\[
q=sq_{\rm red},
\qquad
E=q_{\rm red}E_0,
\]

约去 `q_red`：

\[
\boxed{
F_-s(X+Y)
=4E_0\gamma\,2^H5^TZ.
}
\tag{4.3}

注意 `q-Z` 的所有 non-decimal common prime已经不再出现在 `(4.3)` 左边的
source factor中；唯一留下的是 `s|(2*5^T)` 的 decimal smooth overlap。

---

## 5. `X+Y` 与 smooth--`Z` carrier互素

由 `(UV,10)=1`，`U,V` 都是奇数且为 5-units；所以

\[
5^TU+V
\]

为偶数，从而 `H>=1`。

若某个 odd prime `p|U,Z`，则由

\[
2^HZ-5^TU=V
\]

强迫 `p|V`，与 `(U,V)=1` 矛盾。因此

\[
\boxed{(U,Z)=1.}
\tag{5.1}

故

\[
(X,Y)=1.
\]

于是

\[
(X+Y,X)=1.
\]

又 `X+Y` 为奇数；若 `T>0`，则

\[
X+Y\equiv X\not\equiv0\pmod5,
\]

而 `T=0` 时没有 5-factor需要处理。因此统一有

\[
\boxed{
(X+Y,\,2^{H+2}5^TZ)=1.
}
\tag{5.2}

从 `(4.3)` 与 `(5.2)`：

\[
\boxed{X+Y\mid E_0\gamma.}
\tag{5.3}

定义正整数

\[
\boxed{
R:=\frac{E_0\gamma}{X+Y}>0.
}
\tag{5.4}

则 `(4.3)` 给

\[
\boxed{
F_-
=\frac{2^{H+2}5^TZ}{s}\,R.
}
\tag{5.5}

因为 `s|2*5^T`，右侧 smooth coefficient是整数。

特别地 `Z` 为 10-unit，因此

\[
\boxed{Z\mid F_-.}
\tag{Z-divides-Fminus}

这条结论完全没有 `gcd(q,Z)` 损失。

---

## 6. `R` 精确等于 sphere-gap × normalized overlap

`core.md` §35 的 exact factorization 为

\[
\boxed{
F_-
=a\,g_*
\frac{L(LQ+2\tau)}{\tau}.
}
\tag{6.1}

使用 `(Tail-reduced)`：

\[
L=\frac{2\cdot5^T}{s},
\qquad
Q=Usq_{\rm red},
\qquad
\tau=q_{\rm red}V.
\]

于是

\[
\begin{aligned}
LQ+2\tau
&=2\cdot5^TUq_{\rm red}+2q_{\rm red}V\\
&=2q_{\rm red}(5^TU+V)\\
&=2q_{\rm red}X.
\end{aligned}
\tag{6.2}

代回 `(6.1)`：

\[
\begin{aligned}
F_-
&=a g_*
\frac{L\,2q_{\rm red}X}{q_{\rm red}V}\\
&=\frac{2a g_*LX}{V}\\
&=\frac{2^{H+2}5^TZ}{s}
\;a\frac{g_*}{V}.
\end{aligned}
\tag{6.3}

§37 overlap 参数化写

\[
g_*=vc\lambda r_*,
\]

其中这里的 reduced tail denominator `v` 正是当前 `V`。因此

\[
\boxed{V\mid g_*.}
\tag{6.4}

比较 `(5.5)` 与 `(6.3)`，得到 canonical normalized quotient

\[
\boxed{
R=a\frac{g_*}{V}\in\mathbf Z_{>0}.
}
\tag{R-exact}

最终 exact small-factor normalization 为

\[
\boxed{
F_-=
\frac{2^{H+2}5^TZ}{(2\cdot5^T,q)}
\;a\frac{g_*}{V}.
}
\tag{Exact-Fminus-t2}

---

## 7. height 形式

取十进制对数，`(Exact-Fminus-t2)` 给

\[
\boxed{
\log_{10}F_-
=(H+2)\log_{10}2
+T\log_{10}5
+\log_{10}Z
-\log_{10}s
+\log_{10}a
+\log_{10}\frac{g_*}{V}.
}
\tag{7.1}

又

\[
2^HZ=5^TU+V
=5^TU\left(1+\frac{V}{5^TU}\right),
\]

所以

\[
\boxed{
\begin{aligned}
\log_{10}F_-
={}&2T\log_{10}5+\log_{10}U\\
&+\log_{10}\left(1+\frac{V}{5^TU}\right)
+2\log_{10}2\\
&-\log_{10}s
+\log_{10}a
+\log_{10}\frac{g_*}{V}.
\end{aligned}}
\tag{7.2}

这把旧 stability 中被压缩的 payer完整暴露为：

- forced S-unit baseline `2T log 5 + log U`；
- smooth overlap loss `log s`；
- sphere-gap quotient `a`；
- normalized denominator overlap `g_*/V`。

其中不再出现 `gcd(q,Z)`。

---

## 8. 与旧 `q-Z` allocation 的关系

`high-funnel-qz-gcd-allocation.md` 与
`high-funnel-qz-projective-allocation.md` 中的 divisibility ledger本身仍然成立；
但它们把 `gcd(q,Z)` 当作 `L_Z|F_-` 中的 potential height loss继续分配给
`gamma / R_3^den / Z_0 / a`。

`(Exact-Fminus-t2)` 更强：在同一个 canonical `t_2=1` funnel 中，经过
正确区分 `q` 与 `q_red` 后，full 10-unit `Z` 已经无条件整除 `F_-`。
因此这些 `q-Z` payer files 应降级为**正确但被更强 exact normalization 覆盖的中间账本**，不再是当前 bottleneck。

下一目标应改为研究

\[
\boxed{a\,g_*/V}
\]

的 Archimedean height / prime allocation，而不是继续尝试从
`p|gcd(q,Z)` 推出两条 carrier residual 的传播。

---

## 9. 状态摘要

- **`已严格完成`**：`Tail-reduced`、`q_red|E`、rough-`q` cancellation、
  `Z|F_-`、`R-exact`、`Exact-Fminus-t2`。
- **`失效/降级`**：把 `q-Z gcd` 当作 canonical `t_2=1` funnel 的真实
  small-factor height bottleneck；以及从 `Q=Uq` 未经审计地推断 `(q,10)=1`。
- **`待证`**：对 `a(g_*/V)` 建立新的 global charge；由 `(7.2)` 恢复更强的
  defect-aware stability；DD 全局空性 / effective height bound。

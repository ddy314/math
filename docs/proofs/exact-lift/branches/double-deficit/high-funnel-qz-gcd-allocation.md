# DD high-funnel 的 `q-Z` gcd allocation

> **依赖：** `core.md` 的 gcd-normal form、`t_2=1` S-unit phase、denominator
> prime graph 与 carrier large-divisor identity；
> [`high-funnel-two-adic-balance.md`](high-funnel-two-adic-balance.md) 只作为后续接口。
>
> **严格状态：** `已严格完成（canonical t_2=1 funnel）`。
> 本文不假设 `gcd(q,Z)=10^{o(S)}`。相反，它把这个 gcd 的每个 prime-power
> 深度精确分配到两个已有 payer：denominator overlap `gamma` 与第三分母相对
> prefix lcm 的 unique-max excess。

---

## 1. 从 `u(u+2v)|F_-Q` 抽出 `Z`-divisor

`core.md` 的 gcd-normal form为

\[
\kappa=\gamma u,
\qquad
G=\gamma v,
\qquad
(u,v)=1,
\]

并已有通用整除

\[
\boxed{u(u+2v)\mid F_-Q.}
\tag{1.1}

在 `t_2=1` S-unit phase：

\[
u=2\cdot5^TU,
\qquad
v=V,
\qquad
Q=Uq,
\]

\[
5^TU+V=2^HZ.
\]

所以

\[
u+2v=2(5^TU+V)=2^{H+1}Z.
\]

又 `(UV,10)=1`、`(U,V)=1`。若某个 odd prime `p|U,Z`，phase equation
模 `p` 会强迫 `p|V`，矛盾；因此

\[
\boxed{(U,2\cdot5Z)=1.}
\tag{1.2}

将 `(1.1)` 写成

\[
2^{H+2}5^T UZ\mid F_-Uq
\]

并用 `(1.2)` 约掉 `U`：

\[
\boxed{
2^{H+2}5^TZ\mid F_-q.
}
\tag{Z-divisor-product}

因此 canonical large divisor

\[
\boxed{
L_Z:=
\frac{2^{H+2}5^TZ}
{\gcd(2^{H+2}5^TZ,q)}
\mid F_-.
}
\tag{LZ}

旧 terminal 工作把 bottleneck指向 `gcd(q,Z)`；`(LZ)` 说明同一个
bottleneck其实已经存在于整个 canonical `t_2=1` funnel。

---

## 2. `q-Z` common prime 自动避开 `U,V`

定义

\[
\boxed{D_{qZ}:=\gcd(q,Z).}
\tag{2.1}

因为 `Z` 为 10-unit，`D_{qZ}` 也是 10-unit。

固定

\[
p\mid D_{qZ},
\qquad p\nmid10.
\]

由 `p|Z` 与 phase equation：

- 若 `p|U`，则 `p|V`，与 `(U,V)=1` 矛盾；
- 若 `p|V`，则 `p|U`，同样矛盾。

所以

\[
\boxed{p\nmid UV.}
\tag{2.2}

因此

\[
v_p(Q)=v_p(q),
\qquad
v_p(G)=v_p(\gamma),
\]

且

\[
v_p(\kappa)=v_p(\gamma),
\]

因为 `u=2*5^T U` 也是 `p`-unit。

---

## 3. denominator valuation ledger

写

\[
e_i:=v_p(b_i),
\qquad
r:=v_p(q)=v_p(Q).
\]

由 tail weight

\[
\kappa b_3=10^mQG
\]

和 §2：

\[
v_p(\gamma)+e_3
=r+v_p(\gamma),
\]

所以

\[
\boxed{e_3=r.}
\tag{3.1}

同时

\[
\boxed{v_p(\gamma)=e_1+e_2.}
\tag{3.2}

令

\[
M:=\max(e_1,e_2),
\qquad
m_0:=\min(e_1,e_2).
\]

由于

\[
Q=b_1 10^{m_2}+b_2,
\qquad p\nmid10,
\]

有标准二项赋值二分：

- 若 `e_1 != e_2`，则
  \[
  r=m_0;
  \]
- 若 `e_1=e_2=M`，则
  \[
  r\ge M,
  \]
  超出的 `r-M` 正是 prefix denominator concat 的额外 `p`-adic cancellation。

---

## 4. 第三分母 unique-max excess

定义

\[
\boxed{
R_3^{\rm den}:=
\frac{b_3}{\gcd(b_3,\operatorname{lcm}(b_1,b_2))}.
}
\tag{4.1}

于是

\[
\boxed{
v_p(R_3^{\rm den})=\max(r-M,0).}
\tag{4.2}

我们现在证明

\[
\boxed{
2r\le v_p(\gamma)+2v_p(R_3^{\rm den}).
}
\tag{4.3}

若 `r<=M`：

- `e_1 != e_2` 时 `r=m_0`，故
  \[
  2r=2m_0\le M+m_0=e_1+e_2=v_p(\gamma);
  \]
- `e_1=e_2=M` 时 `r<=M` 与 `r>=M` 合起来给 `r=M`，于是
  \[
  2r=2M=v_p(\gamma).
  \]

若 `r>M`，则必有 `e_1=e_2=M`，所以

\[
v_p(\gamma)=2M,
\qquad
v_p(R_3^{\rm den})=r-M,
\]

从而

\[
2r=2M+2(r-M)
=v_p(\gamma)+2v_p(R_3^{\rm den}).
\]

因此 `(4.3)` 对所有 `p|D_qZ` 成立。

---

## 5. 全局 gcd allocation

对

\[
s_p:=v_p(D_{qZ})\le r
\]

由 `(4.3)`：

\[
2s_p
\le
v_p(\gamma)+2v_p(R_3^{\rm den}).
\]

逐素数相乘，得到 exact integer divisibility

\[
\boxed{
D_{qZ}^{\,2}
\mid
\gamma\,(R_3^{\rm den})^2.
}
\tag{qZ-allocation}

因此

\[
\boxed{
\log D_{qZ}
\le
\frac12\log\gamma
+
\log R_3^{\rm den}.
}
\tag{5.1}

这不是一个假设的 gcd-smallness，而是一条无条件 payer decomposition。

还可以定义 canonical paid/excess split

\[
D_{\gamma}:=\gcd(D_{qZ}^2,\gamma),
\qquad
D_{3}:=D_{qZ}^2/D_{\gamma}.
\]

则

\[
\boxed{D_3\mid(R_3^{\rm den})^2.}
\tag{5.2}

所以 `q-Z` overlap不能凭空消失：未被 `gamma` 支付的部分只能进入第三
分母 unique-max excess。

---

## 6. third-excess 进入 ghost common scale

令整数球面 ghost common scale

\[
\boxed{g_y:=\gcd(y_1,y_2).}
\]

固定 `p|R_3^{den}`，写

\[
c:=v_p(R_3^{\rm den})=e_3-\max(e_1,e_2)>0.
\]

此时 lcm denominator 的 `p`-depth为 `e_3`，所以

\[
v_p(y_i)=e_3-e_i\ge c
\qquad(i=1,2).
\]

故

\[
\boxed{
\operatorname{core}_{10}(R_3^{\rm den})\mid g_y.
}
\tag{ghost-pay}

这里取 `core_10` 只是为了与 `(qZ-allocation)` 的 non-decimal support
一致；2、5 的 depth另有独立账本。

因此 `(qZ-allocation)` 的第二个 payer并非新自由池，它正是 projective
系统中已经出现的 ghost common scale。

---

## 7. `L_Z` 的 height form

因为 `Z` 是 10-unit，

\[
\gcd(2^{H+2}5^TZ,q)
\mid
2^{\mathfrak q}5^{q_5}D_{qZ}.
\]

所以 `(LZ)` 与 `(5.1)` 给

\[
\boxed{
\begin{aligned}
\log_{10}F_-
\ge{}&aH+bT+\log_{10}Z\\
&-a\mathfrak q-bq_5
-\frac12\log_{10}\gamma
-\log_{10}R_3^{\rm den}
+O(1).
\end{aligned}}
\tag{LZ-height}

这条式子把最后的 `q-Z` loss完全暴露成两个具体 payer：`gamma` 与
`R_3^{den}`。

如果后续证明 `R_3^{den}` 只有 subexponential height，则
`Subspace-defect` 中的 `gamma` 费用会立刻使 `(LZ-height)` 产生新的
线性余量；若 `R_3^{den}` 有正线性高度，则 `(ghost-pay)` 把问题转入
projective common-scale / carrier-tetrahedron branch。

---

## 8. 当前边界

- **`已严格完成`**：`Z-divisor-product`、`L_Z|F_-`、
  `qZ-allocation`、`ghost-pay`、`LZ-height`。
- **`结构压缩`**：`gcd(q,Z)` 的全部高度只能由 denominator overlap
  `gamma` 或 third-exclusive ghost common scale支付。
- **`待证`**：对 `R_3^{den}` / `g_y` 建立 projective carrier收费；把
  `(LZ-height)` 与 `Subspace-defect` 联立成新的 explicit slope，或得到
  absolute-height contradiction。

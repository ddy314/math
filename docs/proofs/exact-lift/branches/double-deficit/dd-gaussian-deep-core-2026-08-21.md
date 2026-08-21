# DD Gaussian frontier：source-square split 与 deep oriented core

> **依赖：** [`dd-gaussian-oriented-transversality-2026-08-21.md`](dd-gaussian-oriented-transversality-2026-08-21.md)、
> [`dd-gaussian-overlap-stripped-2026-08-21.md`](dd-gaussian-overlap-stripped-2026-08-21.md)、
> [`dd-third-excess-collapse-2026-08-21.md`](dd-third-excess-collapse-2026-08-21.md)。
>
> **严格状态：** `已严格完成（final Gaussian residual 的全局 source-square/deep 分层）`。
>
> 前一文件对每个 final Gaussian residual prime \(p^e\Vert X_\omega^\flat\) 得到 exact source ledger
> \[
> \boxed{c=e+2t+g+E+j,}
> \]
> 其中 \(c=v_p(C_Q)\)。本文按 \(e\) 是否超过 source depth的一半做 canonical split。
>
> - 若 \(2e\le c\)，则 \(p^{2e}\mid C_Q\)，这部分 Gaussian residual 只有半份 prefix height；
> - 若 \(2e>c\)，则
>   \[
>   \boxed{e>2t+g+E+j,}
>   \]
>   oriented depth严格大于 coefficient/common/two-denominator 全部 baseline 的总和。
>
> 因而可能保留 full \(S\)-height 的 Gaussian 对象被进一步缩成一个 **deep oriented core**。
> 对该 core 还存在 exact source-cofactor tradeoff：若
> \[
> Y_D:=\prod p^{c-e},
> \]
> 则
> \[
> \boxed{X_DY_D\mid C_Q,}
> \qquad
> \boxed{Y_D= T_D^2G_DE_DJ_D,}
> \]
> 其中四个 factors精确记录 \(t,g,E,j\) baseline。于是任何接近整份 \(S\) 的 deep core
> 都自动强迫所有这些 baseline 变成 sublinear height。

---

## 1. local exact ledger

固定
\[
p^e\Vert X_\omega^\flat.
\]
沿用
\[
c=v_p(C_Q),
\quad
t=v_p(A_{12}),
\quad g=v_p(a_1,a_2),
\quad E=v_p(b_1)=v_p(b_2),
\quad j=v_p(b_3).
\]

`dd-gaussian-oriented-transversality-2026-08-21.md` 已严格证明
\[
\boxed{c=e+2t+g+E+j.}
\tag{Source-ledger}

定义 local source cofactor exponent
\[
\boxed{y:=c-e=2t+g+E+j.}
\tag{1.1}

于是
\[
\boxed{c=e+y.}
\tag{1.2}

注意这里没有 inequality slack；\(y\) 恰好包含所有已知 non-oriented local baseline。

---

## 2. source-square / deep 二分

定义两类 support：

### source-square
\[
\boxed{e\le y}
\quad\Longleftrightarrow\quad
\boxed{2e\le c.}
\tag{2.1}

### deep oriented
\[
\boxed{e>y}
\quad\Longleftrightarrow\quad
\boxed{2e>c.}
\tag{2.2}

由于 \(y=2t+g+E+j\)，deep sheet 立即满足
\[
\boxed{e>2t+g+E+j.}
\tag{Deep-dominance}

所以在 deep support：
\[
e>2t,
\qquad e>g,
\qquad e>E,
\qquad e>j.
\tag{2.3}

而 coefficient overlap depth
\[
a^\circ=t-g\le t
\]
也满足
\[
\boxed{a^\circ<e/2<e.}
\tag{2.4}

前一文件还给
\[
\alpha=t+(E-j)_+.
\]
显然
\[
\alpha\le t+E<e,
\]
故
\[
\boxed{\alpha<e.}
\tag{2.5}

primitive bottom edge则有 exact
\[
v_p(\theta_{12})=E+t.
\]
由 `Deep-dominance`：
\[
\boxed{v_p(\theta_{12})=E+t<e.}
\tag{Deep-bottom-shallow}

因此 deep oriented exponent严格深过：

- coefficient cyclotomic orientation \(a^\circ\)；
- sphere gap depth \(\alpha\)；
- primitive bottom determinant depth \(E+t\)；
- source complementary depth \(y=c-e\)。

这使 deep core 成为真正 transverse 的 Gaussian layer。

---

## 3. source-square Gaussian product只有半份 `S`

定义
\[
\boxed{
X_{\omega,S}
:=
\prod_{\substack{p^e\Vert X_\omega^\flat\\2e\le c_p}}p^e.
}
\tag{3.1}

逐 prime `2e<=c_p` 给
\[
\boxed{X_{\omega,S}^2\mid C_Q.}
\tag{Gaussian-square-source}

而
\[
C_Q\le Q<10^S.
\]
因此
\[
\boxed{
\log_{10}X_{\omega,S}<\frac S2.
}
\tag{Gaussian-square-half-S}

这与前序 `X_T^2|C_Q` 是不同的 whole-prime split：这里处理的是已经进入 final Gaussian reader
以后，orientation exponent仍不超过 source depth一半的 primes。

---

## 4. deep oriented core 与 exact source cofactor

定义
\[
\boxed{
X_D
:=
\prod_{\substack{p^e\Vert X_\omega^\flat\\2e>c_p}}p^e.
}
\tag{4.1}

两类 support不交，所以
\[
\boxed{X_\omega^\flat=X_{\omega,S}X_D.}
\tag{4.2}

对 deep support定义
\[
\boxed{
Y_D
:=
\prod_{p^e\Vert X_D}p^{c_p-e}.
}
\tag{4.3}

由 `Source-ledger`：
\[
c_p-e=2t_p+g_p+E_p+j_p.
\]
因此定义 layer products
\[
\boxed{T_D:=\prod_{p^e\Vert X_D}p^{t_p},}
\]
\[
\boxed{G_D:=\prod_{p^e\Vert X_D}p^{g_p},}
\]
\[
\boxed{E_D:=\prod_{p^e\Vert X_D}p^{E_p},}
\]
\[
\boxed{J_D:=\prod_{p^e\Vert X_D}p^{j_p}.}
\]
逐 exponent 恰有
\[
\boxed{
Y_D=T_D^2G_DE_DJ_D.
}
\tag{Deep-cofactor-factorization}

而 \(p^{c_p}\mid C_Q\)，所以
\[
\boxed{X_DY_D\mid C_Q.}
\tag{Deep-source-product}

由于 deep 条件 \(c_p-e<e\)，逐 prime还有
\[
\boxed{Y_D<X_D}
\tag{4.4}
当 deep support非空时成立；这条大小关系本身不是最终 height charge，但精确记录了
oriented mass已经超过 source complementary mass。

---

## 5. deep baseline products都有 concrete readers

这些 layer products都来自已有自然整数：

\[
\boxed{T_D\mid\operatorname{core}_{10}(A_{12}).}
\tag{5.1}

而 final Gaussian residual有 \(e>0\)，故其 source overflow \(x\) 严格大于 \(t\)；
charged-first bottom exponent在该 prime上因此完整取到 \(t\)。所以更精确地
\[
\boxed{T_D\mid X_B^\sharp.}
\tag{5.2}

已有 bottom charge于是给
\[
\boxed{T_DG<F_-}
\tag{5.3}
（实际有更强的 \(X_B^\sharp G<F_-\)）。

common numerator product满足
\[
\boxed{G_D\mid(a_1,a_2).}
\tag{5.4}

prefix denominator baseline满足
\[
\boxed{E_D\mid(b_1,b_2).}
\tag{5.5}

第三 denominator baseline满足
\[
\boxed{J_D\mid b_3.}
\tag{5.6}

此外 gap lock
\[
\alpha_p=t_p+(E_p-j_p)_+
\]
定义 deep gap product
\[
A_D:=\prod_{p^e\Vert X_D}p^{\alpha_p}.
\]
则
\[
\boxed{A_D\mid a.}
\tag{5.7}
并且逐 prime
\[
\alpha_p\le t_p+E_p,
\]
故
\[
\boxed{A_D\mid T_DE_D}
\tag{5.8}
在 exponent-wise divisibility 意义下成立。

所以 deep source cofactor里的每一层都已有 concrete numerator/denominator/gap reader；唯一没有
被这些 baseline reader表达的正线性对象就是 \(X_D\) 自身的 orientation。

---

## 6. global source-cofactor height tradeoff

由 `Deep-source-product` 与
\[
C_Q<10^S
\]
得到无条件
\[
\boxed{
\log X_D+\log Y_D<S.
}
\tag{Deep-height-tradeoff}

代入 `Deep-cofactor-factorization`：
\[
\boxed{
\log X_D
+2\log T_D
+\log G_D
+\log E_D
+\log J_D
<S.
}
\tag{Deep-baseline-tradeoff}

这给出一个非常有用的 extremal rigidity。

若某个候选序列满足
\[
\log X_D\ge(1-\eta)S
\]
（忽略 \(O(1)\)），则自动
\[
\boxed{
2\log T_D+\log G_D+\log E_D+\log J_D
\le\eta S+O(1).
}
\tag{6.1}

因此
\[
\log T_D,
\quad\log G_D,
\quad\log E_D,
\quad\log J_D
\le\eta S+O(1).
\tag{6.2}

又由 `(5.8)`：
\[
\boxed{
\log A_D\le\log T_D+\log E_D
\le\eta S+O(1).
}
\tag{6.3}

换言之：

\[
\boxed{
\text{deep Gaussian core 若接近整份 }S\text{ 高度，}
\Longrightarrow
\text{coefficient/common/denominator/gap baseline全部只有 }o(S)\text{ 高度。}
}
\tag{Deep-full-height-rigidity}

这把“full-height Gaussian escape”进一步压成 asymptotically baseline-free 的 oriented source
问题。

---

## 7. 对 prefix-max / third-max 两张 sheet 的解释

前一文件已经证明 final Gaussian support只有：

### `E>=j`
\[
\alpha=t+E-j,
\qquad
r=0.
\]
若该 prime还属于 deep core，则
\[
e>2t+g+E+j.
\]
所以 prefix denominator baseline与 coefficient/gap baseline全部严格浅于 \(e\)。

### `j>E`
该 Gaussian prime必来自 third->Gaussian whole-prime transfer，并有
\[
t=g=\alpha=0.
\]
此时 source ledger简化为
\[
\boxed{c=e+E+j.}
\tag{7.1}
而 deep 条件为
\[
\boxed{e>E+j.}
\tag{7.2}

所以第三 denominator unique-maximum sheet 上真正可能 full-height 的 Gaussian core甚至只剩
两个 denominator baseline \(E,j\)，且二者总深度小于 orientation 本身。

---

## 8. updated Gaussian hard object

截至本文：
\[
X_\omega^\flat
=X_{\omega,S}X_D,
\]
其中
\[
\boxed{X_{\omega,S}^2\mid C_Q,}
\qquad
\boxed{\log X_{\omega,S}<S/2,}
\]
而 deep core满足
\[
\boxed{X_DY_D\mid C_Q,}
\]
\[
\boxed{Y_D=T_D^2G_DE_DJ_D,}
\]
\[
\boxed{e_p>v_p(Y_D)\quad(p\mid X_D),}
\]
以及 chosen-orientation / bottom transversality：
\[
v_\pi(R_2-iQ_2)=a^\circ<e,
\]
\[
v_p(\theta_{12})=E+t<e.
\]

所以后续无需再研究整个 \(N_{\rm num}\) 或整个 \(X_\omega^\flat\)。真正可能阻止 global
`<=6` 的对象只有
\[
\boxed{X_D=\text{deep, baseline-dominating, oriented Gaussian source core}.}
\]

---

## 9. 下一 quantitative interface

`Deep-baseline-tradeoff` 给出两种后续入口：

1. 若 \(X_D\) 没有接近 \(10^S\)，其缺失高度可直接回到 second-Schmidt allocation；
2. 若 \(X_D\) 接近 \(10^S\)，则 \(T_D,G_D,E_D,J_D,A_D\) 全部 sublinear，问题退化为
   一个 asymptotically baseline-free split-prime orientation system。

后一系统同时具有：
\[
\pi_p^{e_p}\mid Z_{\rm num},Z_{\rm ang},
\]
\[
p^{e_p+y_p}\mid C_Q,
\qquad y_p=o(e_p)\text{ in aggregate},
\]
并且 bottom edge不携带 \(e_p\)。这正是可与 carrier tetrahedron / fixed-target Gaussian
Subspace theorem / digit-shell product formula继续联立的最小 hard core。

---

## 10. 状态摘要

- **`已严格完成`**：Gaussian source-square/deep canonical split。
- **`已严格完成`**：`Gaussian-square-source` 与 `Gaussian-square-half-S`。
- **`已严格完成`**：deep source cofactor exact factorization
  \(Y_D=T_D^2G_DE_DJ_D\)。
- **`已严格完成`**：`Deep-source-product`、`Deep-baseline-tradeoff` 与 full-height rigidity。
- **`结构压缩`**：唯一可能保留 full \(S\)-height 的 Gaussian 对象缩成 \(X_D\)，且它若接近 full
  height，则所有已知 local baseline 自动 sublinear。
- **`待证`**：deep oriented core的 independent Archimedean / Subspace charge；把
  `Deep-baseline-tradeoff` 与 second-Schmidt精确联合优化；DD global explicit `<=6` / absolute height。

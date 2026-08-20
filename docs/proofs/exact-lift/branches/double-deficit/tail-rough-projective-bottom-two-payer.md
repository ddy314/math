# DD post-tail rough loss 的 projective / bottom two-payer collapse

> **依赖：** [`tail-rough-canonical-payer-decomposition.md`](tail-rough-canonical-payer-decomposition.md)、
> [`tail-rough-third-angular-absorption.md`](tail-rough-third-angular-absorption.md)、
> `core.md` 的 stereographic projective denominator formula。
>
> **严格状态：** `已严格完成（整个 `X_Q` odd rough support）`。
>
> canonical four-payer decomposition写
> \[
> x=e_3+e_B+e_G+e_A
> \]
> primewise。本文证明 projective/gap reader `Z_0a` 不只支付 third-exclusive `e_3`：
> 它自动同时支付 denominator-induced ghost common depth、numerator common depth与 primitive
> Gaussian angular depth。因此
> \[
> \boxed{
> e_3+e_G+e_A\le v_p(Z_0a).
> }
> \tag{Projective-absorb-all}
> \]
> 对每个 `p|X_Q` 成立。
>
> 定义
> \[
> e_P:=e_3+e_G+e_A.
> \]
> 全局得到最终 two-payer normal form
> \[
> \boxed{X_Q=X_PX_B,}
> \]
> \[
> \boxed{X_P\mid\operatorname{core}_{10}(Z_0a),}
> \]
> \[
> \boxed{X_B\mid\operatorname{core}_{10}(C_{12})\mid\operatorname{core}_{10}(R_{12}).}
> \]
> 因而 second-Schmidt 的唯一 rough loss不再需要独立的 Gaussian/common-numerator height
> pool：最终只剩 **projective/gap sheet** 与 **bottom-carrier sheet**。

---

## 1. local denominator / numerator data

固定
\[
p^x\Vert X_Q,
\qquad p\nmid10.
\]
`tail-rough-d0-allocation.md` 已证明
\[
\boxed{v_p(b_1)=v_p(b_2)=E.}
\tag{1.1}
写
\[
j:=v_p(b_3),
\qquad
M:=\max(E,j),
\]
并定义 third-exclusive depth
\[
\boxed{r:=(j-E)_+=M-E.}
\tag{1.2}
这正是
\[
v_p(R_3^{\rm den})=r.
\]

令 numerator valuations
\[
A_i:=v_p(a_i),
\]
以及 common numerator depth
\[
\boxed{g:=\min(A_1,A_2)=v_p(a_1,a_2).}
\tag{1.3}
`tail-rough-angular-source-transfer.md` 已证明在 `X_Q` support上这也等于
cross numerator common scale `g_A` 的 p-depth。

因为 `q_lcm` 的 p-depth为 `M`：
\[
y_i=a_iq_{\rm lcm}/b_i
\]
给
\[
v_p(y_1)=A_1+r,
\qquad
v_p(y_2)=A_2+r.
\]
因此 ghost common scale
\[
g_y=(y_1,y_2)
\]
满足
\[
\boxed{v_p(g_y)=r+g.}
\tag{Ghost-common}

---

## 2. primitive ghost angular depth就是 `N_ang`

写
\[
y_1=p^{r+g}Y_1,
\qquad
 y_2=p^{r+g}Y_2,
\]
其中 `(Y_1,Y_2)` 至少一项为 p-unit。

又写
\[
b_i=p^EB_i,
\qquad p\nmid B_1B_2,
\]
后者来自 `p|X_Q|C_Q=B_1 10^{m_2}+B_2` 与 `(B_1,B_2)=1`。

令
\[
\bar a_i=a_i/(a_1,a_2).
\]
则 p-adically `(Y_1,Y_2)` 与
\[
(\bar a_1B_2,\bar a_2B_1)
\]
只差共同 p-unit scale。因此
\[
\boxed{
\omega:=v_p(N_{\rm ang})
=v_p(Y_1^2+Y_2^2),
}
\tag{Angular=ghost-general}
其中
\[
N_{\rm ang}
=(\bar a_1B_2)^2+(\bar a_2B_1)^2.
\]

所以
\[
\boxed{
v_p(y_1^2+y_2^2)=2(r+g)+\omega.}
\tag{2.1}

---

## 3. stereographic denominator直接吸收 common + angle

DD sphere factorization：
\[
(H-y_3)(H+y_3)=y_1^2+y_2^2.
\]
gap normalization：
\[
H-y_3=La.
\]
当前 `p∤10` 且 `L|10^m`，故
\[
p\nmid L,
\qquad
\alpha:=v_p(La)=v_p(a).
\]

`core.md` 的 exact projective denominator formula为
\[
\boxed{
v_p(Z_0)=
\max(0,v_p(g_y)+\omega-\alpha).
}
\tag{3.1}
使用 `(Ghost-common)`：
\[
\boxed{
v_p(Z_0)=
\max(0,r+g+\omega-v_p(a)).
}
\tag{3.2}
因此
\[
\begin{aligned}
v_p(Z_0a)
&=v_p(a)+v_p(Z_0)\\
&=\max(v_p(a),r+g+\omega).
\end{aligned}
\]
特别地
\[
\boxed{
v_p(Z_0a)\ge r+g+\omega.}
\tag{Projective-capacity}

这条式子同时包含上一文件 third-angular two-sheet theorem；后者是 `g=0,r>0`
时的显式 sphere-sheet展开。

---

## 4. canonical angular remainder总有 `e_A<=omega`

`tail-rough-canonical-payer-decomposition.md` 定义
\[
e_3=\min(x,r),
\]
随后按顺序定义 `e_B,e_G,e_A`，并有
\[
e_G\le g.
\]
显然
\[
\boxed{e_3\le r,
\qquad e_G\le g.}
\tag{4.1}
唯一需要重新确认的是
\[
e_A\le\omega.
\]

若 `e_A=0` 无事可证。设 `e_A>0`。这意味着前三层不足以支付 `x`，所以它们
都达到容量：
\[
e_3=r,
\qquad e_B=t,
\qquad e_G=g,
\]
其中
\[
t:=v_p(C).
\]
于是
\[
\boxed{x>r+t+g.}
\tag{4.2}

`tail-rough-gaussian-payer-split.md` 的 general transfer refinement给
\[
\boxed{x\le\max(t,2g+\omega,r).}
\tag{4.3}
由于 `(4.2)` 特别给 `x>t,r`，只能
\[
x\le2g+\omega.
\]
而 `g<=t`，故
\[
\begin{aligned}
e_A
&=x-r-t-g\\
&\le2g+\omega-r-t-g\\
&=\omega-(r+t-g)\\
&\le\omega.
\end{aligned}
\]
所以
\[
\boxed{e_A\le\omega.}
\tag{Angular-capacity}

---

## 5. 三个 non-bottom layers一次性进入 `Z_0a`

由 `(4.1)` 与 `(Angular-capacity)`：
\[
 e_3+e_G+e_A
\le r+g+\omega.
\]
再由 `(Projective-capacity)`：
\[
\boxed{
 e_3+e_G+e_A
\le v_p(Z_0a).
}
\tag{Projective-absorb-all}

定义
\[
\boxed{e_P:=e_3+e_G+e_A.}
\tag{5.1}
则逐 prime有
\[
p^{e_P}\mid Z_0a.
\]

剩余唯一 layer就是 `e_B`，且
\[
x=e_P+e_B.
\tag{5.2}

---

## 6. global two-payer factorization

定义
\[
\boxed{X_P:=\prod_{p|X_Q}p^{e_P(p)},}
\]
\[
\boxed{X_B:=\prod_{p|X_Q}p^{e_B(p)}.}
\]
由 `(5.2)`：
\[
\boxed{X_Q=X_PX_B.}
\tag{Two-payer-product}

`Projective-absorb-all` 给
\[
\boxed{X_P\mid\operatorname{core}_{10}(Z_0a).}
\tag{Projective-payer}

而 canonical payer decomposition已证明
\[
\boxed{X_B\mid\operatorname{core}_{10}(C_{12}),}
\qquad
C_{12}=(A_{12},Q),
\]
并由 orientation-uniform bottom identity
\[
\boxed{C_{12}\mid R_{12}}
\]
得到
\[
\boxed{X_B\mid\operatorname{core}_{10}(R_{12}).}
\tag{Bottom-payer}

所以最终：
\[
\boxed{
X_Q=X_PX_B,
\quad
X_P\mid Z_0a,
\quad
X_B\mid C_{12}\mid R_{12}.
}
\tag{Two-payer-normal-form}

---

## 7. 对此前 payer files 的重新定位

这条 theorem严格加强前几步：

- `tail-rough-gaussian-payer-split.md` 的 `N_ang` 仍提供 primitive angular reader，但其
  height不再需要单独计入最终 `X_Q` budget；
- `tail-rough-angular-source-transfer.md` 的 `N_num` orientation与 cyclotomic overlap仍是
  bottom/angular local structure，但不是最终必需的第三 height pool；
- `tail-rough-third-angular-absorption.md` 是本文在 `r>0,g=0` 子情形的更显式
  sphere two-sheet版本；
- `tail-rough-bottom-angular-cyclotomic-split.md` 仍是正确的细分，但 two-payer theorem
  对最终 height accounting更强。

因此 branch reoptimization 的 hard loss已从
\[
C_Q\to X_Q\to\text{four/five payers}
\]
进一步压成
\[
\boxed{
X_Q\rightsquigarrow
\text{projective/gap }(Z_0a)
+\text{ bottom }(C_{12},R_{12}).
}

---

## 8. 下一步

第二次 Schmidt已有
\[
\log R_x+\log(g_*/v)
\ge S-\log X_Q-o(S),
\]
而 `R_x` 与 `g_*/v` 都是真实 `F_-` factors。
现在唯一 loss为
\[
\log X_P+\log X_B,
\]
并有两个 concrete readers：
\[
X_P\mid Z_0a,
\qquad
X_B\mid R_{12}.
\]

下一任务因此非常明确：

1. 对 simultaneous projective/bottom depth建立 carrier-circle / determinant-tetrahedron
   eliminant；或
2. 证明两者任一达到正线性 `S` 高度时，已有 small-factor / digit-shell budget自动付费。

一旦 `log X_P+log X_B` 能得到比自由 `S` 更小的统一上界，就可把第二次 Schmidt
真正转成新的 explicit global slope，并继续冲击 DD `<=6`。

---

## 9. 状态摘要

- **`已严格完成`**：`Ghost-common`、`Angular=ghost-general`、`Projective-capacity`。
- **`已严格完成`**：`e_A<=omega` 与 `Projective-absorb-all`。
- **`已严格完成`**：`Two-payer-product / payer / normal-form`。
- **`结构压缩`**：post-tail rough loss最终只剩 projective/gap 与 bottom 两条 carrier边。
- **`待证`**：projective-bottom simultaneous eliminant / height；non-canonical branch reoptimization；DD global explicit `<=6` / absolute height。

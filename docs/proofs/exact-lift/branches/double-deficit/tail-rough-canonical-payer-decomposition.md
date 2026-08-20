# DD post-tail rough overflow 的 canonical four-payer decomposition

> **依赖：** [`tail-rough-general-transfer.md`](tail-rough-general-transfer.md)、
> [`tail-rough-angular-source-transfer.md`](tail-rough-angular-source-transfer.md)、
> [`high-funnel-qz-bottom-orientation-correction.md`](high-funnel-qz-bottom-orientation-correction.md)。
>
> **严格状态：** `已严格完成（整个 `X_Q` odd rough support）`。
>
> 之前的结果已经证明 `X_Q` 的每个 prime-power只能由 denominator third-excess、
> numerator coefficient/common-square、或 split-Gaussian angle支付。本文把这种“max payer”
> 改写成一个**逐 exponent 的 canonical decomposition**。
>
> 对每个
> \[
> p^x\Vert X_Q
> \]
> 定义四段深度：
> \[
> e_3=\min(x,r),
> \]
> \[
> e_B=\min(x-e_3,t),
> \]
> \[
> e_G=\min(x-e_3-e_B,g),
> \]
> \[
> e_A=x-e_3-e_B-e_G,
> \]
> 其中
> \[
> r=v_p(R_3^{\rm den}),\quad
> t=v_p(C),\quad
> g=v_p((a_1,a_2)).
> \]
> 则 `e_A` 自动满足
> \[
> \boxed{e_A\le v_p(N_{\rm num}).}
> \]
> 因此存在 canonical integers
> \[
> \boxed{X_Q=X_3X_BX_GX_A}
> \]
> （四者不要求 pairwise coprime；同一 prime 的不同 exponent layers可落入不同 payer），且
> \[
> \boxed{
> X_3\mid\operatorname{core}_{10}(R_3^{\rm den})\mid Z_0a,
> }
> \]
> \[
> \boxed{
> X_B\mid\operatorname{core}_{10}(C_{12})\mid\operatorname{core}_{10}(R_{12}),
> }
> \]
> \[
> \boxed{X_G\mid\operatorname{core}_{10}(a_1,a_2),}
> \]
> \[
> \boxed{X_A\mid\operatorname{core}_{10}(N_{\rm num}).}
> \]
> 这里
> \[
> C_{12}=(A_{12},Q),
> \]
> 而 `R_12` 是 orientation-uniform primitive bottom determinant reader。
>
> 这把 second-Schmidt 的 loss从一个匿名整数 `X_Q` 变成四条可分别收费的
> **projective / bottom / common-numerator / Gaussian-angular** carrier layers。

---

## 1. local data

固定
\[
p^x\Vert X_Q.
\]
`tail-rough-general-transfer.md` 与随后 Gaussian split使用：
\[
t:=v_p(C),
\qquad
r:=v_p(R_3^{\rm den}),
\]
\[
g:=v_p(g_n),
\qquad g_n=(a_1,a_2),
\]
\[
\omega:=v_p(N_{\rm ang}),
\qquad
u:=v_p(N_{\rm num}).
\]

在 `X_Q` support上
\[
\boxed{g\le t,}
\tag{1.1}
\]
且
\[
\boxed{
x\le\max(t,2g+\omega,r).}
\tag{1.2}

另一方面若 `omega>0`，`tail-rough-angular-source-transfer.md` 的同向 Gaussian transfer给
\[
\boxed{
\nu\ge\min(c,\omega),
}
\tag{1.3}
\]
其中
\[
c=v_p(C_Q),
\]
并且 `X_Q|C_Q` 给
\[
\boxed{x\le c.}
\tag{1.4}

---

## 2. canonical sequential allocation

定义
\[
\boxed{e_3:=\min(x,r).}
\tag{2.1}
\]
令
\[
x_1=x-e_3.
\]
再定义
\[
\boxed{e_B:=\min(x_1,t),}
\tag{2.2}
\]
\[
x_2=x_1-e_B.
\]
再定义
\[
\boxed{e_G:=\min(x_2,g),}
\tag{2.3}
\]
以及最后 remainder
\[
\boxed{e_A:=x_2-e_G.}
\tag{2.4}
显然
\[
\boxed{x=e_3+e_B+e_G+e_A.}
\tag{2.5}

前三段分别自动满足
\[
e_3\le r,
\qquad e_B\le t,
\qquad e_G\le g.
\]
唯一需要证明的是
\[
e_A\le\nu.
\]

---

## 3. angular remainder 必被 `N_num` 支付

若
\[
e_A=0,
\]
无事可证。以下设
\[
e_A>0.
\]
这意味着在 sequential allocation 后仍有 depth，因而
\[
\boxed{x>r+t+g.}
\tag{3.1}
特别地
\[
x>r,\qquad x>t.
\]
所以 `(1.2)` 的最大值只能由
\[
2g+\omega
\]
支付：
\[
\boxed{x\le2g+\omega.}
\tag{3.2}
由于 `t>=g`，从 `(3.1)` 还有
\[
x>t+g\ge2g,
\]
所以
\[
\omega>0.
\]
由 `(3.2)`：
\[
\boxed{\omega\ge x-2g.}
\tag{3.3}

另一方面 `(1.3),(1.4)` 给
\[
\nu\ge\min(c,\omega).
\]
因为 `c>=x`，而 `(3.3)` 给 `omega>=x-2g`：
\[
\boxed{\nu\ge x-2g.}
\tag{3.4}

最后由定义，`e_A>0` 时前三段都已达到各自容量：
\[
e_3=r,\qquad e_B=t,\qquad e_G=g.
\]
故
\[
e_A=x-r-t-g.
\]
而
\[
r+t-g\ge0
\]
因为 `t>=g`。所以
\[
\begin{aligned}
e_A
&=x-r-t-g\\
&\le x-2g\\
&\le\nu.
\end{aligned}
\]
证明
\[
\boxed{e_A\le v_p(N_{\rm num}).}
\tag{Angular-remainder}

---

## 4. global four-payer integers

对每个 `p|X_Q` 取上述四个 exponents，定义
\[
\boxed{X_3:=\prod_{p|X_Q}p^{e_3(p)},}
\]
\[
\boxed{X_B:=\prod_{p|X_Q}p^{e_B(p)},}
\]
\[
\boxed{X_G:=\prod_{p|X_Q}p^{e_G(p)},}
\]
\[
\boxed{X_A:=\prod_{p|X_Q}p^{e_A(p)}.}
\]
由 `(2.5)`：
\[
\boxed{X_Q=X_3X_BX_GX_A.}
\tag{Four-payer-product}

注意这些 integers 的 prime supports可以重叠，因为这里刻意分解的是**同一 prime 的
valuation layers**，不是做 coprime support partition。

逐定义立即有
\[
\boxed{X_3\mid\operatorname{core}_{10}(R_3^{\rm den}),}
\tag{4.1}
\]
\[
\boxed{X_G\mid\operatorname{core}_{10}(g_n),}
\tag{4.2}
\]
\[
\boxed{X_A\mid\operatorname{core}_{10}(N_{\rm num}).}
\tag{4.3}

下一节处理 `X_B`。

---

## 5. coefficient layer 自动进入 bottom carrier

固定 `p|X_B`。有
\[
e_B\le t=v_p(C).
\]
DD coefficient
\[
C=10^dA_{12}
\]
且 `p` 不整除 10，所以
\[
\boxed{e_B\le v_p(A_{12}).}
\tag{5.1}

另一方面
\[
e_B\le x\le c=v_p(C_Q),
\]
而
\[
Q=(b_1,b_2)C_Q,
\]
故
\[
\boxed{e_B\le v_p(Q).}
\tag{5.2}

因此
\[
\boxed{
p^{e_B}\mid C_{12}:=(A_{12},Q).}
\tag{5.3}
逐 prime相乘：
\[
\boxed{X_B\mid\operatorname{core}_{10}(C_{12}).}
\tag{5.4}

`high-funnel-qz-bottom-orientation-correction.md` 已证明，不论 `k-d` 正负，
orientation-uniform bottom reader
\[
R_{12}:=\Delta_{12}/10^{\min(k,d)}
\]
均满足
\[
\boxed{C_{12}\mid R_{12}.}
\tag{5.5}
所以
\[
\boxed{X_B\mid\operatorname{core}_{10}(R_{12}).}
\tag{Bottom-reader}

因此 coefficient payer不是一个普通 height pool；它必同时制造 genuine bottom-carrier depth。

---

## 6. third layer进入 projective/gap

已有 general projective allocation：
\[
\boxed{
\operatorname{core}_{10}(R_3^{\rm den})\mid Z_0a.
}
\]
结合 `(4.1)`：
\[
\boxed{X_3\mid\operatorname{core}_{10}(Z_0a).}
\tag{Projective-reader}

所以 four payer 的四条 canonical readers为
\[
\boxed{
\begin{array}{c|c}
\text{layer}&\text{reader}\\ \hline
X_3&Z_0a\\
X_B&C_{12}\mid R_{12}\\
X_G&(a_1,a_2)\\
X_A&N_{\rm num}
\end{array}}
\tag{Reader-table}

---

## 7. height form

由 exact product decomposition：
\[
\boxed{
\log X_Q
=\log X_3+\log X_B+\log X_G+\log X_A.
}
\]
并且安全有
\[
\boxed{
\log X_Q
\le
\log\operatorname{core}_{10}(Z_0a)
+\log\operatorname{core}_{10}(C_{12})
+\log\operatorname{core}_{10}(a_1,a_2)
+\log\operatorname{core}_{10}(N_{\rm num}).
}
\tag{Height-four-payer}

这比一个单独 `X_Q|product` 更适合后续 LP：每一份 valuation depth都只出现一次，且
`X_B` 已经带有 bottom-carrier语义，`X_A` 已带同向 Gaussian orientation。

---

## 8. 当前 branch-reoptimization frontier

post-tail source cancellation的 local complexity已经被压成四个 reader：

1. **projective/gap** `Z_0a`；
2. **bottom carrier** `R_12`；
3. **common numerator scale** `(a_1,a_2)`；
4. **pure numerator split-Gaussian angle** `N_num`。

因此下一步不应再做 ordinary denominator gcd allocation。真正目标变成：

- 用 carrier tetrahedron / circle eliminant限制 `X_B` 与 `X_3` 同时线性大；
- 用 numerator digit shell / cyclotomic overlap限制 `X_B` 与 `X_A`；
- common numerator `X_G` 的总高度最多由前两 numerator 的共同位数支付。

如果能证明这四个 layer总高度严格小于 `S` 的 Schmidt loss threshold，就可完成
non-canonical dominant side branch reoptimization，并有希望把全 DD explicit limsup推到 `<=6`。

---

## 9. 状态摘要

- **`已严格完成`**：canonical exponent allocation、`Angular-remainder`。
- **`已严格完成`**：`Four-payer-product`。
- **`已严格完成`**：`Bottom-reader` / `Projective-reader` / `Reader-table`。
- **`结构压缩`**：`X_Q` 已从单一匿名 loss变成四条可分别用不同算术机制收费的 carrier layers。
- **`待证`**：four-payer simultaneous height bound；non-canonical dominant branch reoptimization；DD global explicit `<=6` / absolute height。

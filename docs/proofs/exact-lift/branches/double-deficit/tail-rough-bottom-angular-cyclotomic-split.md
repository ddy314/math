# DD residual bottom / Gaussian-angular payer 的 cyclotomic sheet split

> **依赖：** [`tail-rough-canonical-payer-decomposition.md`](tail-rough-canonical-payer-decomposition.md)、
> [`tail-rough-third-angular-absorption.md`](tail-rough-third-angular-absorption.md)、
> [`tail-rough-angular-source-transfer.md`](tail-rough-angular-source-transfer.md)。
>
> **严格状态：** `已严格完成（整个 `X_Q` odd rough support）`。
>
> 前两步已经把 post-tail hard loss写成 projective layer、bottom layer、common numerator
> layer与 residual Gaussian layer。本文进一步抽掉 bottom 与 Gaussian 的共同 primitive
> numerator depth。最终得到 exact exponent-layer factorization
> \[
> \boxed{
> X_Q=X_P\,X_C\,D_{BA}^{\,2}\,B_0A_0,
> }
> \tag{Cyclotomic-normal-form}
> \]
> 其中
> \[
> \boxed{X_P\mid\operatorname{core}_{10}(Z_0a),}
> \]
> \[
> \boxed{X_C\mid\operatorname{core}_{10}(a_1,a_2)^2,}
> \]
> \[
> \boxed{D_{BA}\mid10^{2|s_2|}+1,}
> \]
> 并且
> \[
> \boxed{(B_0,A_0)=1.}
> \]
> `B_0` 是 primitive bottom-only leftover，`A_0` 是 residual split-Gaussian-only
> leftover。也就是说，bottom 与 Gaussian 若在同一 rough prime上同时线性深，重叠部分
> 必须由显式 decimal cyclotomic carrier支付；除掉这部分后二者 prime support互斥。

---

## 1. 从 third-angular absorption后的 local layers开始

对每个
\[
p^x\Vert X_Q
\]
`tail-rough-canonical-payer-decomposition.md` 给
\[
x=e_3+e_B+e_G+e_A.
\]
`tail-rough-third-angular-absorption.md` 又把 `r>0` support上的 `e_3+e_A`
合并进 projective reader。记
\[
e_P:=e_3+e_{A,3},
\]
其中 `e_{A,3}=e_A` 当 `r>0`，否则为 0；并记 residual angular
\[
e_{A,0}:=e_A-e_{A,3}.
\]
于是逐 prime
\[
\boxed{x=e_P+e_B+e_G+e_{A,0}.}
\tag{1.1}
且
\[
\boxed{p^{e_P}\mid Z_0a.}
\tag{1.2}
此外
\[
e_{A,0}>0\Longrightarrow r=0.
\tag{1.3}

---

## 2. bottom depth中先抽一份 common numerator scale

令
\[
g_n=(a_1,a_2),
\qquad g:=v_p(g_n).
\]
定义 primitive numerator concat
\[
A^\circ=A_{12}/g_n.
\]
因为 `p` 不整除 10：
\[
\boxed{
v_p(C)=v_p(A_{12})=g+v_p(A^\circ).}
\tag{2.1}

bottom layer满足
\[
e_B\le v_p(C).
\]
定义
\[
\boxed{e_{B,g}:=\min(e_B,g),}
\tag{2.2}
\]
\[
\boxed{e_B^\circ:=e_B-e_{B,g}.}
\tag{2.3}
显然
\[
\boxed{e_B^\circ\le v_p(A^\circ).}
\tag{2.4}

另一方面原 common layer有
\[
e_G\le g.
\]
所以定义总 common-square layer
\[
\boxed{e_C:=e_{B,g}+e_G,}
\tag{2.5}
立刻有
\[
\boxed{e_C\le2g.}
\tag{2.6}

逐 prime将 `(1.1)` 重写为
\[
\boxed{x=e_P+e_C+e_B^\circ+e_{A,0}.}
\tag{2.7}

---

## 3. primitive bottom / angular overlap进入 cyclotomic carrier

`tail-rough-angular-source-transfer.md` 已证明
\[
\boxed{
\operatorname{core}_{10}\gcd(A^\circ,N_{\rm num})
\mid10^{2|s_2|}+1.
}
\tag{3.1}
其中
\[
N_{\rm num}
=(\bar a_1 10^{m_2})^2+\bar a_2^2.
\]

residual angular layer满足
\[
\boxed{e_{A,0}\le v_p(N_{\rm num}).}
\tag{3.2}
结合 `(2.4)`，定义 local overlap
\[
\boxed{d_p:=\min(e_B^\circ,e_{A,0}).}
\tag{3.3}
则
\[
d_p\le v_p(A^\circ),
\qquad d_p\le v_p(N_{\rm num}),
\]
所以由 `(3.1)`：
\[
\boxed{
p^{d_p}\mid10^{2|s_2|}+1.}
\tag{Cyclotomic-local}

定义剩余单侧 layers
\[
\boxed{b_p:=e_B^\circ-d_p,}
\qquad
\boxed{a_p:=e_{A,0}-d_p.}
\tag{3.4}
由 `d_p=min(...)`：
\[
\boxed{\min(a_p,b_p)=0.}
\tag{3.5}
这就是 bottom / angular 的 two-sheet residue：抽掉 cyclotomic overlap后，每个 prime只能留在一侧。

---

## 4. global canonical factors

定义
\[
X_P:=\prod_{p|X_Q}p^{e_P(p)},
\]
\[
X_C:=\prod_{p|X_Q}p^{e_C(p)},
\]
\[
D_{BA}:=\prod_{p|X_Q}p^{d_p},
\]
\[
B_0:=\prod_{p|X_Q}p^{b_p},
\qquad
A_0:=\prod_{p|X_Q}p^{a_p}.
\]
由 `(2.7)` 与 `(3.4)`：
\[
\boxed{
X_Q=X_PX_CD_{BA}^2B_0A_0.
}
\tag{Cyclotomic-normal-form}

各 payer满足：

### projective/gap
由 third-angular absorption：
\[
\boxed{X_P\mid\operatorname{core}_{10}(Z_0a).}
\tag{4.1}

### common numerator square
由 `(2.6)`：
\[
\boxed{X_C\mid\operatorname{core}_{10}(g_n)^2.}
\tag{4.2}

### bottom/angular overlap
由 `(Cyclotomic-local)`：
\[
\boxed{D_{BA}\mid10^{2|s_2|}+1.}
\tag{4.3}
（`D_BA` 本身无 2、5 primes，因此不必再取 `core_10`。）

### one-sided residuals
由定义：
\[
\boxed{B_0\mid\operatorname{core}_{10}(A^\circ),}
\tag{4.4}
\[
\boxed{A_0\mid\operatorname{core}_{10}(N_{\rm num}).}
\tag{4.5}
并由 `(3.5)`：
\[
\boxed{(B_0,A_0)=1.}
\tag{4.6}

此外原 bottom reader仍给
\[
B_0\mid X_B\mid C_{12}\mid R_{12}
\]
在对应 exponent layers上的整除，因此 `B_0` 保留 genuine bottom-carrier语义；`A_0`
保留 numerator Gaussian orientation语义。

---

## 5. 基本 height caps

这一步还未完成 final LP，但已经给几条无条件 cap。

### common numerator
因为
\[
g_n\le\min(a_1,a_2),
\]
且 DD `d`-dominant surplus simplex有
\[
n_1+n_2=S+s_1+s_2\le S+2,
\]
所以
\[
\boxed{
\log_{10}X_C
\le2\log_{10}g_n
\le S+O(1).
}
\tag{5.1}

### primitive bottom
\[
B_0\mid A^\circ,
\]
且
\[
A^\circ=A_{12}/g_n<10^{n_1+n_2}/g_n,
\]
故
\[
\boxed{
\log_{10}B_0
\le S-\log_{10}g_n+O(1).
}
\tag{5.2}

同时 `B_0` 还是 bottom reader `R_12` 的 divisor。

### cyclotomic overlap
\[
\boxed{
\log_{10}D_{BA}
\le2|s_2|+O(1).
}
\tag{5.3}

### residual Gaussian
`A_0|N_num`，而
\[
N_{\rm num}
=(\bar a_1 10^{m_2})^2+\bar a_2^2,
\]
所以其 height由纯 numerator digit shape控制；后续应与 `(B_0,A_0)=1` 和 projective
layer联立，而不是把 `log N_num` 全额当独立 loss。

---

## 6. 对 branch reoptimization 的意义

第二次 Schmidt要求 rough mass约为 `S`。经过当前链条：
\[
\text{anonymous }X_Q
\rightsquigarrow
X_P\,X_C\,D_{BA}^2\,B_0A_0,
\]
其中：

- `X_P` 是单一 projective/gap reader；
- `X_C` 是 numerator common square，最多由前两 numerator共同位数支付；
- bottom / Gaussian simultaneous same-prime depth已被显式 cyclotomic integer
  `10^{2|s_2|}+1` 抽掉；
- 剩余 `B_0,A_0` **互素**，分别落在 bottom 与 Gaussian sheets。

因此下一 LP 不再需要给 `C_Q` 一个自由 `S` 高度。真正未知只剩：

1. `X_P` 的 global height；
2. coprime one-sided leftovers `B_0,A_0` 能否同时线性大；
3. `s_2` cyclotomic budget与 surplus simplex如何联立。

---

## 7. 状态摘要

- **`已严格完成`**：bottom common/primitive split、`Cyclotomic-local`。
- **`已严格完成`**：`Cyclotomic-normal-form`、`(B_0,A_0)=1`。
- **`结构压缩`**：post-tail hard rough loss被压成 projective、common-square、explicit cyclotomic 与两个互素 one-sided sheets。
- **`待证`**：`X_P/B_0/A_0` simultaneous height；post-tail branch reoptimization；DD global explicit `<=6` / absolute height。

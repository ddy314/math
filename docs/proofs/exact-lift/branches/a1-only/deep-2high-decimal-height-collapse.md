# A1 minimal diagonal: double-deep 2-high collapse by decimal-height synchronization

> 日期：2026-08-22。
>
> 依赖：
> - `deep-denominator-ledger.md` 中 `deep-double-2high-master.md`；
> - `global-squarefree-terminal.md`；
> - `decimal-height-synchronization.md`。
>
> 当前范围：minimal diagonal、`k=g>=32`、double-deep。此前所有 surviving double-deep 已严格统一到 2-high / 5-low master。

状态：**已严格完成。本文关闭整个 surviving double-deep master。**

---

## 1. master data

令

\[
T=10^k.
\]

当前唯一 double-deep master 写成

\[
D_{\rm gap}=2^A5^B,
\qquad
A=2k+3+\eta,
\tag{1}
\]

并且

\[
B>0,
\qquad
Y:=B+\nu_5<k+1,
\tag{2}
\]

其中

\[
\nu_5=v_5(N_0)\ge0.
\]

因此

\[
\boxed{B\le k.}
\tag{3}
\]

master 还给

\[
\boxed{
\xi
=2^{-\eta}5^{B+2\nu_5}r_{10},
}
\tag{4}
\]

其中

\[
r_{10}\in\mathbf Z_{>0},
\qquad
(r_{10},10)=1,
\]

并有全局上界

\[
\boxed{\xi<15,214,000.}
\tag{5}
\]

---

## 2. 把 deep denominator 翻译成全局 `(L,M,kappa)`

在 double-deep 中 `lambda=1`。`deep-complement-height.md` 的精确恒等式为

\[
D_{\rm gap}T\rho=h,
\qquad
(h,10)=1.
\tag{6}
\]

另一方面全局 A1 normalization 写

\[
\rho=\frac ML,
\qquad
(L,M)=1,
\]

且 `L` 只含 `2,5`。由 (6) 的既约性立即得到

\[
\boxed{
L=D_{\rm gap}T,
\qquad
M=h.
}
\tag{7}
\]

因此

\[
\boxed{
v_2(L)=A+k=3k+3+\eta,}
\tag{8}
\]

\[
\boxed{
v_5(L)=B+k.}
\tag{9}

minimal diagonal 中 `b_2=1`，故

\[
G=b_1,
\qquad
b_1=10T^2-w,
\qquad
Q=10b_1+1.
\]

令 supply complement

\[
M_c:=\frac{QG}{h}.
\]

全局整数 tail weight

\[
\kappa=\frac{10^gLQG}{M}
\]

在 `g=k` 下由 (7) 化为

\[
\boxed{
\kappa=D_{\rm gap}T^2M_c.
}
\tag{10}

因为

\[
b_1\equiv-w\not\equiv0\pmod5,
\qquad
Q\equiv1\pmod5,
\]

所以

\[
5\nmid QG,
\qquad
5\nmid M_c.
\]

因此

\[
\boxed{
v_5(\kappa)=B+2k.}
\tag{11}

---

## 3. 2-side `L` height 已严格高于 5-side `L` height

由 (4)-(5) 以及

\[
5^{B+2\nu_5}r_{10}\ge1
\]

可得

\[
2^{-\eta}<15,214,000<2^{24}.
\]

故

\[
\boxed{\eta>-24.}
\tag{12}

于是对 `k>=32`：

\[
v_2(L)=3k+3+\eta
>3k-21
>2k
\ge B+k=v_5(L),
\]

其中最后使用 (3)。所以

\[
\boxed{v_2(L)>v_5(L).}
\tag{13}

`decimal-height-synchronization.md` 说明，若真实第三 block 存在，则归一化第三分子

\[
x_\sigma=\frac{X_\sigma}{Y_\sigma}
\]

的 reduced denominator 5-height `d_5` 必须把 5-side completion height 追到 2-side：

\[
\boxed{
d_5\ge v_2(L)=3k+3+\eta.}
\tag{14}

---

## 4. `x_sigma` 的精确 5-adic denominator depth

沿用全局 terminal：

\[
W^2
=\kappa\bigl(\kappa K-2GD_c^2N\bigr),
\tag{15}
\]

其中为避免与 gap denominator 混淆，记 A1 coefficient denominator

\[
D_c:=10^gQ=TQ.
\]

形式根的归一化第三分子为

\[
x_\sigma
=
\frac{
X_\sigma
}{
\kappa^2(\kappa+2G)
},
\tag{16}
\]

\[
X_\sigma
=\kappa G^2C+\sigma(\kappa+G)W.
\tag{17}
\]

minimal diagonal 中

\[
a_2=10T^2-z,
\qquad z\in\{1,3\}.
\]

所以

\[
C=a_1 10^{n_2}+a_2
\equiv-z\not\equiv0\pmod5.
\]

结合 `5 not|G,Q`：

\[
\boxed{v_5(C)=v_5(G)=v_5(Q)=0.}
\tag{18}

因此

\[
v_5(D_c)=k
\]

且

\[
K=G^2C^2-D_c^2N
\equiv G^2C^2\not\equiv0\pmod5,
\]

故

\[
\boxed{v_5(K)=0.}
\tag{19}

再由 (11) 且 `5 not|G`：

\[
\boxed{v_5(\kappa+2G)=0.}
\tag{20}

记

\[
n_5:=v_5(N)\ge0,
\qquad
a:=B+2k=v_5(\kappa).
\tag{21}

于是 (15) 中两项的 5-adic valuations 分别为

\[
v_5(\kappa K)=a=B+2k,
\]

\[
v_5(2GD_c^2N)=2k+n_5.
\]

分三种情况。

### Case I: `n_5<B`

此时第二项严格更浅，所以

\[
v_5(W)
=\frac{B+4k+n_5}{2}
=2k+\frac{B+n_5}{2}.
\tag{22}

并且

\[
v_5(W)<a.
\]

在 (17) 中两项 valuation 不同，因此没有 cancellation：

\[
v_5(X_\sigma)=v_5(W)
\]

对两个 sign 都成立。由 (16),(20)：

\[
\boxed{
 d_5
=2a-v_5(W)
=2k+\frac{3B-n_5}{2}.
}
\tag{23}

### Case II: `n_5>B`

此时 `kappa K` 更浅，所以

\[
v_5(W)=a.
\]

(17) 的两项均至少有 valuation `a`，从而

\[
v_5(X_\sigma)\ge a.
\]

因此

\[
\boxed{d_5\le a=B+2k.}
\tag{24}

### Case III: `n_5=B`

两项同深，可能发生 resonance，但这只能增加

\[
v_5(\kappa K-2GD_c^2N).
\]

因此

\[
v_5(W)\ge a,
\qquad
v_5(X_\sigma)\ge a,
\]

仍有

\[
\boxed{d_5\le B+2k.}
\tag{25}

所以 Case II-III 可统一为

\[
\boxed{
n_5\ge B\Longrightarrow d_5\le B+2k.}
\tag{26}

---

## 5. height synchronization 与 `xi` 上界直接矛盾

### Case A: `n_5>=B`

由 (14),(26)：

\[
3k+3+\eta
\le B+2k,
\]

所以

\[
\boxed{
\eta\le B-k-3.
}
\tag{27}

代入 (4)，并只使用 `nu_5>=0,r_10>=1`：

\[
\xi
\ge2^{-\eta}5^B
\ge2^{k+3-B}5^B
=2^{k+3}\left(\frac52\right)^B.
\]

因为 `B>0`：

\[
\boxed{\xi>2^{k+3}.}
\tag{28}

### Case B: `n_5<B`

由 (14),(23)：

\[
3k+3+\eta
\le
2k+\frac{3B-n_5}{2},
\]

故

\[
\boxed{
\eta
\le
\frac{3B-n_5}{2}-k-3.
}
\tag{29}

于是

\[
\begin{aligned}
\xi
&\ge2^{-\eta}5^B\\
&\ge
2^{k+3-(3B-n_5)/2}5^B\\
&=
2^{k+3+n_5/2}
\left(\frac{5}{2^{3/2}}\right)^B.
\end{aligned}
\]

而

\[
25>8
\Longrightarrow
\frac5{2^{3/2}}>1.
\]

又 `B>0,n_5>=0`，故同样得到

\[
\boxed{\xi>2^{k+3}.}
\tag{30}

两种情况合并：任何合法 double-deep master candidate 都必须满足

\[
\xi>2^{k+3}.
\]

但当前

\[
k\ge32,
\]

所以

\[
\xi>2^{35}=34,359,738,368,
\]

这与 (5)

\[
\xi<15,214,000
\]

矛盾。

因此

\[
\boxed{
\text{minimal diagonal 中所有 surviving double-deep 2-high/5-low states 为空.}
}
\tag{31}

---

## 6. consequence

此前已经严格证明：

- high-high 为空；
- 所有 5-high double-deep 为空；
- moderate LL 已 exact modular exhaustion 关闭；
- 因而任何 surviving double-deep 都属于本文统一的 2-high/5-low master。

本文关闭该 master，所以

\[
\boxed{
\text{minimal diagonal 的 double-deep sector 全部关闭.}
}
\tag{32}

这一步不使用 fixed local-signature enumeration，也不使用旧 high-order Hensel lock；唯一新增输入是全局 exact decimal-height synchronization。

A1 整体仍不能据此标记为空：minimal diagonal 之外的 moving-prefix 层，以及 minimal diagonal 的 surviving single-deep sector 仍需分别关闭。

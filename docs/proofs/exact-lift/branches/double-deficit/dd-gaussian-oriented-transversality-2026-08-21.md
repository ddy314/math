# DD Gaussian frontier：oriented transversality、gap baseline lock 与 exact source ledger

> **依赖：** [`dd-gaussian-overlap-stripped-2026-08-21.md`](dd-gaussian-overlap-stripped-2026-08-21.md)、
> [`dd-third-excess-collapse-2026-08-21.md`](dd-third-excess-collapse-2026-08-21.md)、
> [`tail-allocation-ledger.md`](tail-allocation-ledger.md) 中 `tail-rough-general-transfer`、
> `tail-rough-angular-source-transfer`，以及 [`core.md`](core.md) 的 DD gap quadratic、
> integer sphere、primitive bottom determinant。
>
> **严格状态：** `已严格完成（final Gaussian residual 的全部 odd rough support）`。
>
> 前一文件把最后可能携带 full orientation height 的对象压成
> \[
> X_\omega^\flat\mid N_{\rm num}^{\rm exc}.
> \]
> 本文继续保留 \(\mathbf Z[i]\) 中的 \(\pi/\bar\pi\) orientation，得到三个新的 exact 结论：
>
> 1. coefficient overlap 在 chosen Gaussian orientation 上**恰好**等于 explicit decimal
>    cyclotomic depth；剩余 Gaussian exponent 不再进入该 digit factor；
> 2. 同一 Gaussian residual prime 在 primitive bottom determinant 中只有
>    \(E+t\) 的精确 baseline，Gaussian excess 不进入 bottom edge；
> 3. gap quadratic 强制
>    \[
>    \boxed{\alpha=t+(E-j)_+,}
>    \]
>    从而 source concat depth 有统一的 exact decomposition
>    \[
>    \boxed{c=e+2t+g+E+j.}
>    \]
>
> 此外，若 \(j>E\)，则 non-third Gaussian residual 与 sphere two-sheet矛盾；因此 third-denominator
> unique-maximum 的 Gaussian prime只能来自上一文件已经处理的 `third -> Gaussian` whole-prime
> transfer，并满足 \(t=g=\alpha=0\)。

---

## 1. local notation 与 orientation

固定
\[
p^e\Vert X_\omega^\flat,
\qquad p\nmid10,
\qquad e>0.
\]

沿用
\[
E=v_p(b_1)=v_p(b_2),
\qquad
j=v_p(b_3),
\qquad
r=(j-E)_+,
\]
\[
c=v_p(C_Q),
\qquad
x=v_p(X_Q),
\]
\[
t=v_p(A_{12}),
\qquad
g=v_p(a_1,a_2),
\qquad
\alpha=v_p(a),
\qquad
\omega=v_p(N_{\rm ang}).
\]

令
\[
g_n=(a_1,a_2),
\qquad
\bar a_i=a_i/g_n,
\]
以及
\[
\boxed{
A^\circ
=\bar a_1 10^{n_2}+\bar a_2,
\qquad
a^\circ:=v_p(A^\circ)=t-g.
}
\tag{1.1}

在 `X_Q` support 写
\[
b_i=p^E B_i\quad(i=1,2),
\qquad p\nmid B_1B_2,
\]
且
\[
\boxed{C_Q=B_1 10^{m_2}+B_2.}
\tag{1.2}

定义
\[
\boxed{
Z_{\rm num}
=-\bar a_1 10^{m_2}+i\bar a_2,
}
\tag{1.3}
\[
\boxed{
Z_{\rm ang}
=\bar a_1B_2+i\bar a_2B_1.
}
\tag{1.4}

前序文件已经证明 Gaussian residual 强迫 \(\omega>0\)，故
\[
p\equiv1\pmod4.
\]
在 \(\mathbf Z[i]\) 中写
\[
p=\pi\bar\pi
\]
并选择 orientation 使
\[
\boxed{\pi^\omega\mid Z_{\rm ang}.}
\tag{1.5}
primitive 性保证 \(\bar\pi\nmid Z_{\rm ang}\)。

same-orientation source transfer与前一文件的 overlap stripping 给
\[
\boxed{
\pi^{a^\circ+e}\mid Z_{\rm num},
}
\tag{1.6}
因为
\[
a^\circ+e\le\min(c,\omega).
\]
又 \(p\nmid\bar a_1\bar a_2\)，所以 \(Z_{\rm num}\) 的两个坐标都是 p-units；因此
\[
\boxed{\bar\pi\nmid Z_{\rm num}.}
\tag{1.7}

---

## 2. coefficient overlap 的 oriented digit identity

为避免与 third denominator depth \(r\) 混淆，记
\[
Q_2:=10^{m_2},
\qquad
R_2:=10^{n_2}.
\]

直接使用 `(1.1),(1.3)`：
\[
\begin{aligned}
A^\circ+iZ_{\rm num}
&=(\bar a_1R_2+\bar a_2)
+i(-\bar a_1Q_2+i\bar a_2)\\
&=\bar a_1(R_2-iQ_2).
\end{aligned}
\]
所以有 exact Gaussian identity
\[
\boxed{
A^\circ+iZ_{\rm num}
=\bar a_1(R_2-iQ_2).
}
\tag{Digit-oriented}

作为伴随式，同样直接展开得到
\[
\boxed{
Q_2A^\circ+R_2Z_{\rm num}
=\bar a_2(Q_2+iR_2).
}
\tag{Digit-companion}

### 2.1 chosen orientation 上 digit depth 恰为 `a^circ`

因为 \(A^\circ\) 是 rational integer：
\[
v_\pi(A^\circ)=v_{\bar\pi}(A^\circ)=a^\circ.
\]
而 `(1.6)` 给
\[
v_\pi(Z_{\rm num})\ge a^\circ+e>a^\circ.
\]
所以 `(Digit-oriented)` 左侧两项在 \(\pi\) 处 valuation 不同，得到
\[
\boxed{
v_\pi(R_2-iQ_2)=a^\circ.
}
\tag{Chosen-digit-exact}

这比 ordinary cyclotomic divisibility更精确：真正承载 residual orientation 的 \(\pi\) 上，
coefficient overlap恰好用尽 \(a^\circ\) 层，此后的 \(e\) 层全部 transverse 于 digit factor。

若 \(a^\circ>0\)，由 `(1.7)`：
\[
v_{\bar\pi}(A^\circ)>0,
\qquad
v_{\bar\pi}(Z_{\rm num})=0,
\]
故
\[
\boxed{
v_{\bar\pi}(R_2-iQ_2)=0.}
\tag{Opposite-digit-unit}

于是取 norm：
\[
N(R_2-iQ_2)=R_2^2+Q_2^2.
\]
对 non-decimal p，抽掉 \(10^{2\min(m_2,n_2)}\) 不改变 valuation，所以当
\(a^\circ>0\) 时进一步有
\[
\boxed{
v_p(10^{2|s_2|}+1)=a^\circ.}
\tag{Cyclotomic-exact-on-residual}

因此前一文件的
\[
A_\omega\mid10^{2|s_2|}+1
\]
在 Gaussian residual support 上没有隐藏额外 same-prime cyclotomic depth：正的 coefficient
companion恰好就是全部 cyclotomic p-depth。

---

## 3. denominator-side oriented digit factor

已有 source identity
\[
Z_{\rm ang}-B_1Z_{\rm num}=\bar a_1C_Q.
\]
另一方面由 `(Digit-oriented)` 与 `(1.2)` 可直接得到
\[
\boxed{
B_1(R_2-iQ_2)+iC_Q
=B_1R_2+iB_2.
}
\tag{Den-digit-linear}

还可从 \(A^\circ,Z_{\rm ang}\) 直接展开：
\[
\boxed{
B_1A^\circ+iZ_{\rm ang}
=\bar a_1(B_1R_2+iB_2).
}
\tag{Den-oriented}

由于
\[
v_\pi(Z_{\rm ang})=\omega\ge a^\circ+e>a^\circ,
\]
而 \(v_\pi(A^\circ)=a^\circ\)，同样得到
\[
\boxed{
v_\pi(B_1R_2+iB_2)=a^\circ.}
\tag{Den-digit-exact}

所以 numerator digit factor \(R_2-iQ_2\) 与 denominator digit factor
\(B_1R_2+iB_2\) 在 chosen orientation 上都只有 coefficient baseline \(a^\circ\)；
Gaussian excess \(e\) 不进入任一 explicit digit factor。

---

## 4. primitive bottom determinant 的 exact transversality

定义 p-adic bottom digit difference
\[
\boxed{
D_{\rm bot}
:=\bar a_1B_2R_2-\bar a_2B_1Q_2.
}
\tag{4.1}

由 `(1.1),(1.2)` 有 exact integer identity
\[
\begin{aligned}
B_2A^\circ-\bar a_2C_Q
&=B_2(\bar a_1R_2+\bar a_2)
-\bar a_2(B_1Q_2+B_2)\\
&=D_{\rm bot}.
\end{aligned}
\]
因此
\[
\boxed{D_{\rm bot}=B_2A^\circ-\bar a_2C_Q.}
\tag{Bottom-source-linear}

前一文件给
\[
a^\circ+e\le c,
\qquad e>0,
\]
所以
\[
\boxed{c>a^\circ.}
\tag{4.2}

而 \(B_2,\bar a_2\) 都是 p-units，于是 `(Bottom-source-linear)` 的两项 valuation
分别为 \(a^\circ,c\)，严格不同。故
\[
\boxed{v_p(D_{\rm bot})=a^\circ.}
\tag{Bottom-exact}

这给出 Gaussian residual 与 bottom carrier 的 exact transversality。

DD primitive bottom determinant为
\[
\Delta_{12}
=a_1b_2 10^{k_{12}}-a_2b_1 10^{d_3}.
\]
在 \(\mathbf Q_p\) 中乘以 decimal p-unit \(10^{m_2-d_3}\)，并抽掉
\(p^E\) 与 numerator common depth \(g\)，恰得到 `(4.1)`。因此
\[
\boxed{
v_p(\Delta_{12})=E+g+a^\circ=E+t.
}
\tag{Bottom-determinant-depth}

primitive normalization中的
\[
g_1=(10^{k_{12}},b_1),
\qquad
g_2=(10^{d_3},b_2)
\]
只含 2,5-primes，所以对当前 p 均为 units。于是
\[
\boxed{
v_p(\theta_{12})=E+t.
}
\tag{Bottom-theta-exact}

特别地，\(e\) 不出现在右端。也就是说 coefficient overlap 被扣除后，剩余 Gaussian
orientation depth在 primitive bottom edge上严格为零。

---

## 5. non-third Gaussian support 的 gap baseline lock

先处理没有来自 third-excess whole-prime transfer 的 Gaussian residual。此时
\[
R_*=(r-t-\alpha)_+=0,
\]
且
\[
\boxed{e=x-t-\alpha-g>0.}
\tag{5.1}

所以
\[
x>t+\alpha+g>t,
\qquad
r\le t+\alpha<x.
\tag{5.2}

由 general transfer
\[
x\le\max(t,2g+\omega,r),
\]
只能有
\[
\boxed{x\le2g+\omega.}
\tag{5.3}

记
\[
M=\max(E,j),
\qquad
\delta=(E-j)_+.
\]
又记
\[
n_0=v_p(N_0)=2g+\omega.
\]
所以 `(5.3)` 给
\[
\boxed{n_0\ge x.}
\tag{5.4}

DD general-transfer proof中的 gap quadratic
\[
C_0a^2-2\mathcal Ma+Q\frac{\mathcal S_{12}}L=0
\]
三项 valuations为
\[
\boxed{
G_1=j+2\alpha,
\qquad
G_2=M+t+\alpha,
\qquad
G_3=c-E+2M+n_0.
}
\tag{5.5}

三个整数项和为零，所以最低 valuation至少出现两次。

### 5.1 `E>=j`

此时
\[
M=E,
\qquad
\delta=E-j,
\qquad
x=c-2j>0,
\]
即
\[
c=x+2j.
\tag{5.6}

于是
\[
G_3=x+2j+E+n_0.
\]
由 `(5.2),(5.4)`：
\[
\begin{aligned}
G_3-G_1
&=x+j+E+n_0-2\alpha\\
&\ge2x+E+j-2\alpha>0,
\end{aligned}
\]
以及
\[
\begin{aligned}
G_3-G_2
&=x+2j+n_0-t-\alpha\\
&\ge2x+2j-t-\alpha>0.
\end{aligned}
\]
因此第三项严格更深，只能
\[
G_1=G_2.
\]
即
\[
j+2\alpha=E+t+\alpha,
\]
从而
\[
\boxed{\alpha=t+E-j=t+\delta.}
\tag{5.7}

### 5.2 `j>E`

此时
\[
M=j,
\qquad
\delta=0,
\qquad
x=c-j-E>0,
\]
即
\[
c=x+j+E.
\tag{5.8}

于是
\[
G_3=x+3j+n_0.
\]
同样由 `(5.2),(5.4)`：
\[
G_3-G_1
=x+2j+n_0-2\alpha>0,
\]
\[
G_3-G_2
=x+2j+n_0-t-\alpha>0.
\]
所以仍只能
\[
G_1=G_2,
\]
得到
\[
\boxed{\alpha=t.}
\tag{5.9}

综上：
\[
\boxed{
\alpha=t+(E-j)_+.
}
\tag{Gaussian-gap-lock}

---

## 6. `j>E` 的 non-third Gaussian sheet 实际为空

现在假设 non-third Gaussian residual 且
\[
j>E.
\]
则
\[
r=j-E>0,
\]
而 `(Gaussian-gap-lock)` 给
\[
\alpha=t.
\]
non-third 条件 \(R_*=0\) 又要求
\[
r\le t+\alpha=2t.
\]
所以
\[
\boxed{t>0.}
\tag{6.1}

但 \(j>E\) 时第三 denominator 是 p-adic unique maximum。因为 \(j>0\) 且
\((a_3,b_3)=1\)：
\[
v_p(y_3)=0.
\]
前两 ghost 坐标至少有 common depth \(r+g>0\)，sphere equation模 p因而给
\[
v_p(H)=0.
\]
odd-prime sphere factorization于是只有两个 sheets：
\[
\boxed{
\{v_p(H-y_3),v_p(H+y_3)\}
=\{0,2(r+g)+\omega\}.
}
\tag{6.2}

而
\[
v_p(H-y_3)=v_p(La)=\alpha=t>0.
\]
所以 `(6.2)` 强迫
\[
\boxed{t=2(r+g)+\omega.}
\tag{6.3}

另一方面 Gaussian overlap theorem给
\[
\omega\ge e+a^\circ
=e+t-g.
\]
代入 `(6.3)`：
\[
\begin{aligned}
t
&=2r+2g+\omega\\
&\ge2r+2g+e+t-g,
\end{aligned}
\]
于是
\[
0\ge2r+g+e,
\]
与 \(r,e>0\) 矛盾。

因此
\[
\boxed{
\text{不存在 }j>E\text{ 的 non-third Gaussian residual prime.}
}
\tag{Third-max-nonthird-empty}

结合 `dd-third-excess-collapse-2026-08-21.md`：
\[
\boxed{
j>E
\Longrightarrow
\text{若 p 进入 final Gaussian residual，则它只能来自 third->Gaussian，}
\quad t=g=\alpha=0.
}
\tag{Third-max-pure-Gaussian}

---

## 7. Gaussian gap lock 对全部 final residual 统一成立

third->Gaussian support 已经有
\[
j>E,
\qquad
\delta=0,
\qquad
t=\alpha=0.
\]
所以 `(Gaussian-gap-lock)` 在这类 primes上同样成立。

因此对**全部** final Gaussian residual primes都有
\[
\boxed{
\alpha=t+\delta,
\qquad
\delta=(E-j)_+.
}
\tag{7.1}

non-third 情形 `(5.1)` 给
\[
e=x-t-\alpha-g.
\]
third->Gaussian 情形有 \(t=g=\alpha=\delta=0,e=x\)。所以两类可统一为
\[
\boxed{
e=x-2t-\delta-g.}
\tag{Gaussian-residual-exact}

而 overflow 定义在 \(x>0\) 时为
\[
\boxed{x=c-j-\min(E,j).}
\tag{7.2}

代入 `(Gaussian-residual-exact)`：
\[
c
=e+2t+\delta+g+j+\min(E,j).
\]
注意恒等式
\[
\delta+j+\min(E,j)=E+j
\]
对 \(E\ge j\) 与 \(j>E\) 两种 order 都成立，所以最终得到本文最重要的 source ledger：
\[
\boxed{
 c=e+2t+g+E+j.
}
\tag{Gaussian-source-ledger}

等价地
\[
\boxed{
 c-e=2t+g+E+j.
}
\tag{Gaussian-source-cofactor}

这条式子把 primitive denominator concat 的 p-depth精确分成：

\[
\boxed{
\text{oriented Gaussian residual }e
+2\times\text{numerator coefficient depth }t
+\text{common numerator depth }g
+\text{two denominator baselines }E+j.
}
\tag{7.3}

没有剩余匿名 valuation。

---

## 8. current Gaussian frontier 的两种 canonical denominator orders

由 `Third-max-nonthird-empty`，final Gaussian residual只有两种 denominator order。

### Prefix-max/equal sheet

\[
\boxed{E\ge j.}
\]
这里
\[
r=0,
\qquad
\alpha=t+E-j,
\]
并且
\[
\boxed{
e=x-2t-(E-j)-g.}
\tag{8.1}

### Third-max pure Gaussian sheet

\[
\boxed{j>E.}
\]
这时必来自 third->Gaussian whole-prime transfer，因此
\[
\boxed{t=g=\alpha=0,}
\]
\[
\boxed{e=x>j-E.}
\tag{8.2}

两者都满足统一 source ledger `(Gaussian-source-ledger)`。

---

## 9. 对 carrier / digit-shell 路线的意义

本文已经排除了三种可能的 double counting：

- coefficient overlap 的 chosen orientation depth恰为 \(a^\circ\)，并在
  \(10^{2|s_2|}+1\) 中 exact saturation；
- primitive bottom edge有 exact depth \(E+t\)，不含 \(e\)；
- source concat 的剩余 cofactor不再未知，而是 exact
  \[
  c-e=2t+g+E+j.
  \]

所以真正需要继续处理的 full-height Gaussian mass已经具有明确含义：它是同一 source prime中
超过 coefficient / common / denominator 全部 baseline 后的 **oriented excess**。

下一步应把 `(Gaussian-source-cofactor)` 按
\[
e\le c/2
\quad\text{与}\quad
e>c/2
\]
分层：前者自动给 source-square charge，后者则强制 oriented depth严格大于
\(2t+g+E+j\)，成为一个 baseline-free-in-relative-size 的 deep Gaussian core。

---

## 10. 状态摘要

- **`已严格完成`**：`Digit-oriented`、chosen-orientation exact depth、正 overlap 时的
  `Cyclotomic-exact-on-residual`。
- **`已严格完成`**：`Bottom-source-linear`、`Bottom-theta-exact`，Gaussian excess与 bottom
  carrier严格 transverse。
- **`已严格完成`**：non-third `Gaussian-gap-lock`。
- **`已严格完成`**：`j>E` non-third Gaussian sheet为空。
- **`已严格完成`**：全部 final Gaussian residual 的 `Gaussian-source-ledger`
  \(c=e+2t+g+E+j\)。
- **`结构压缩`**：final Gaussian support只剩 prefix-max/equal 与 third-max pure-Gaussian 两张 sheet。
- **`待证`**：deep/square Gaussian split的全局 height accounting；deep oriented core的
  Archimedean reader；把精确 source ledger喂回 non-canonical side-branch LP；DD global explicit
  `<=6` / absolute height。

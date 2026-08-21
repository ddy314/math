# DD Gaussian frontier：coefficient-overlap stripping 与 exact norm saturation

> **依赖：** [`dd-third-excess-collapse-2026-08-21.md`](dd-third-excess-collapse-2026-08-21.md)、
> [`dd-z0-charged-first-2026-08-21.md`](dd-z0-charged-first-2026-08-21.md)、
> [`tail-allocation-ledger.md`](tail-allocation-ledger.md) 中 `tail-rough-angular-source-transfer` 的
> same-orientation transfer / cyclotomic overlap，以及 `tail-rough-general-transfer`。
>
> **严格状态：** `已严格完成（updated charged-first Gaussian residual 的全部 odd rough support）`。
>
> 上一文件将 third-excess full-height reader关闭后，dominant post-tail 中唯一仍可能携带完整
> orientation height 的对象为
> \[
> X_\omega^{\flat}\mid N_{\rm num}.
> \]
> 本文证明这里仍有一层可严格删除的重复深度：若
> \[
> A^\circ=A_{12}/(a_1,a_2),
> \]
> 则每个 Gaussian residual exponent `e_p` 不仅进入 `N_num`，而且进入 `N_num` 时还位于
> `A^circ` 的全部 local depth **之上**。因此真正 canonical reader可改写成
> \[
> \boxed{
> X_\omega^{\flat}
> \mid
> \operatorname{core}_{10}\!\left(
> \frac{N_{\rm num}}{(A^\circ,N_{\rm num})}
> \right).
> }
> \]
> 被除掉的 overlap 已由已有 cyclotomic theorem控制：
> \[
> \boxed{
> \operatorname{core}_{10}(A^\circ,N_{\rm num})
> \mid10^{2|s_2|}+1.
> }
> \]
> 所以后续 Gaussian height不能再把 coefficient-overlap depth作为独立自由质量重复计入。

---

## 1. local notation

固定一个最终 Gaussian residual prime
\[
p^e\Vert X_\omega^{\flat},
\qquad p\nmid10.
\]

沿用
\[
x=v_p(X_Q),
\qquad
c=v_p(C_Q),
\qquad
r=v_p(R_3^{\rm den}),
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
\[
\boxed{
A^\circ=A_{12}/g_n
=\bar a_1 10^{n_2}+\bar a_2.
}
\tag{1.1}

因为
\[
A_{12}=g_nA^\circ,
\]
有 exact local split
\[
\boxed{
a^\circ:=v_p(A^\circ)=t-g\ge0.
}
\tag{1.2}

纯 numerator Gaussian norm仍为
\[
\boxed{
N_{\rm num}
=(\bar a_1 10^{m_2})^2+\bar a_2^2,
}
\tag{1.3}
并记
\[
u:=v_p(N_{\rm num}).
\]

已有 same-orientation source transfer：
\[
\boxed{u\ge\min(c,\omega).}
\tag{1.4}

另外所有 `X_Q` primes都有
\[
\boxed{x\le c.}
\tag{1.5}

---

## 2. Gaussian residual 有两种来源

`dd-third-excess-collapse-2026-08-21.md` 的 updated allocation 中，Gaussian exponent `e`
只有两种来源。

### 2.1 非 third-excess support：`R_*=0`

这里
\[
R_*=(r-t-\alpha)_+=0,
\tag{2.1}
所以
\[
r\le t+\alpha.
\tag{2.2}

charged-first residual为
\[
z=(x-t-\alpha)_+.
\]
Gaussian layer只有在
\[
z>g
\]
时为正，此时
\[
\boxed{
e=z-g=x-t-\alpha-g.
}
\tag{2.3}

### 2.2 third-excess 转入 Gaussian 的 support

上一文件已经证明这一类 prime满足
\[
\boxed{t=g=\alpha=0,}
\tag{2.4}
并且由于 `x>r`，general transfer强迫
\[
\boxed{x\le\omega.}
\tag{2.5}

whole-prime reallocation定义
\[
\boxed{e=x.}
\tag{2.6}

此时由 `(1.2)`：
\[
\boxed{a^\circ=0.}
\tag{2.7}

---

## 3. coefficient-overlap depth 必须位于 Gaussian residual 之下

我们证明统一不等式
\[
\boxed{
e+a^\circ\le\min(c,\omega).}
\tag{Overlap-below-Gaussian}

### 3.1 非 third-excess case

由 `(2.3)` 与 `a^circ=t-g`：
\[
\begin{aligned}
e+a^\circ
&=x-t-\alpha-g+t-g\\
&=x-\alpha-2g.
\end{aligned}
\tag{3.1}

因为 `e>0`，有
\[
x>t+\alpha+g>t.
\tag{3.2}

又由 `(2.2)`：
\[
r\le t+\alpha<x.
\tag{3.3}

现有 general transfer refinement为
\[
x\le\max(t,2g+\omega,r).
\]
`(3.2),(3.3)` 排除了 `t,r` 两个 maxima，只能
\[
\boxed{x\le2g+\omega.}
\tag{3.4}

代入 `(3.1)`：
\[
e+a^\circ
=x-\alpha-2g
\le\omega-\alpha
\le\omega.
\tag{3.5}

另一方面由 `(1.5)`：
\[
e+a^\circ=x-\alpha-2g\le x\le c.
\tag{3.6}

故 `(Overlap-below-Gaussian)` 成立。

### 3.2 third-to-Gaussian case

这里 `a^circ=0,e=x`。上一文件已证明
\[
x\le\omega,
\qquad x<c,
\]
所以同样
\[
e+a^\circ=x\le\min(c,\omega).
\]

因此 `(Overlap-below-Gaussian)` 对所有最终 Gaussian residual primes统一成立。

---

## 4. `N_num` 至少含 `a^circ+e` 层

由 same-orientation transfer `(1.4)` 与 `(Overlap-below-Gaussian)`：
\[
\boxed{
u\ge a^\circ+e.}
\tag{4.1}

特别地，若 `e>0` 且 `a^circ>0`，则 `N_num` 不只是含 Gaussian residual 的 `p^e`：
它还在其下完整包含 `A^circ` 的所有 local `p`-depth。

令
\[
D_A:=(A^\circ,N_{\rm num}).
\]
因为
\[
v_p(A^\circ)=a^\circ,
\qquad
u\ge a^\circ+e>a^\circ,
\]
所以在当前 Gaussian support上
\[
\boxed{v_p(D_A)=a^\circ.}
\tag{4.2}

于是
\[
\boxed{
 e\le v_p(N_{\rm num}/D_A).
}
\tag{4.3}

逐 prime相乘得到本文第一个主结论：
\[
\boxed{
X_\omega^{\flat}
\mid
\operatorname{core}_{10}\!\left(
\frac{N_{\rm num}}{(A^\circ,N_{\rm num})}
\right).
}
\tag{Overlap-stripped-reader}

这是比 `X_omega^flat|N_num` 严格更 canonical 的 reader：所有已经属于 primitive numerator
coefficient 的同-prime depth都先被除掉。

---

## 5. 被剥掉的 overlap 是显式 cyclotomic depth

`tail-rough-angular-source-transfer` 已严格证明
\[
\boxed{
\operatorname{core}_{10}\gcd(A^\circ,N_{\rm num})
\mid10^{2|s_2|}+1.
}
\tag{Cyclotomic-overlap}

因此定义
\[
D_A^{(10)}:=\operatorname{core}_{10}(A^\circ,N_{\rm num}),
\]
则
\[
\boxed{D_A^{(10)}\mid10^{2|s_2|}+1.}
\tag{5.1}

而 `Overlap-stripped-reader` 等价于说 Gaussian residual只读取
\[
\boxed{
N_{\rm num}^{\rm exc}
:=
\operatorname{core}_{10}\!\left(N_{\rm num}/D_A^{(10)}\right)
}
\tag{5.2}
中的 exponent excess。

所以 coefficient / Gaussian 同 prime 深度现在被精确分成：
\[
\boxed{
\text{cyclotomic overlap }D_A^{(10)}
\quad+\quad
\text{Gaussian excess }N_{\rm num}^{\rm exc}.
}
\tag{5.3}

后续 height optimization不能再次把 `D_A^(10)` 同时作为 numerator coefficient 与 Gaussian
norm 的两份独立质量。

---

## 6. 一个 exact norm resultant：source transfer 已经饱和

这一步进一步审计 `N_ang -> N_num` 是否还隐藏额外 simultaneous depth。

写 primitive denominator concat
\[
\boxed{C_Q=B_1 10^{m_2}+B_2,}
\tag{6.1}
其中 `(B_1,B_2)=1`，且在 `X_Q` support上已有
\[
p\nmid B_1B_2.
\tag{6.2}

primitive angular norm为
\[
\boxed{
N_{\rm ang}
=(\bar a_1B_2)^2+(\bar a_2B_1)^2.
}
\tag{6.3}

直接展开得到 exact identity
\[
\begin{aligned}
B_1^2N_{\rm num}-N_{\rm ang}
&=\bar a_1^2
\left(B_1^2 10^{2m_2}-B_2^2\right)\\
&=\bar a_1^2
\left(B_1 10^{m_2}-B_2\right)
\left(B_1 10^{m_2}+B_2\right).
\end{aligned}
\]
所以
\[
\boxed{
B_1^2N_{\rm num}-N_{\rm ang}
=
\bar a_1^2
(B_1 10^{m_2}-B_2)C_Q.
}
\tag{Norm-resultant}

固定 Gaussian residual prime。因为 `e>0`，必有 `omega>0`，所以
\[
p\mid N_{\rm ang}.
\]
primitive coordinates与 `(6.2)` 强迫
\[
\boxed{p\nmid\bar a_1\bar a_2.}
\tag{6.4}

同时 source root `p|C_Q` 给
\[
B_1 10^{m_2}\equiv-B_2\pmod p,
\]
故 odd prime下
\[
B_1 10^{m_2}-B_2
\equiv-2B_2\not\equiv0\pmod p.
\]
因此 `(Norm-resultant)` 的右端有 exact valuation
\[
\boxed{
v_p(B_1^2N_{\rm num}-N_{\rm ang})=c.
}
\tag{6.5}

记
\[
u=v_p(N_{\rm num}),
\qquad
\omega=v_p(N_{\rm ang}).
\]
由 `(6.5)`，不可能同时有 `u>c` 与 `omega>c`；所以
\[
\min(u,\omega)\le c.
\]
显然同时
\[
\min(u,\omega)\le\omega.
\]
故
\[
\min(u,\omega)\le\min(c,\omega).
\tag{6.6}

另一方面 same-orientation transfer `(1.4)` 给
\[
u\ge\min(c,\omega),
\]
而 `omega` 自己当然也不小于 `min(c,omega)`。所以
\[
\min(u,\omega)\ge\min(c,\omega).
\tag{6.7}

合并得到 exact saturation law：
\[
\boxed{
\min\bigl(v_p(N_{\rm num}),v_p(N_{\rm ang})\bigr)
=
\min(c,\omega).
}
\tag{Norm-saturation}

因此 source-orientation transfer在 ordinary norm depth层面已经是 sharp 的；不存在一份还能
从 `N_ang` 与 `N_num` simultaneous divisibility 中免费提取的额外正线性 depth。

这也告诉后续路线应使用 Gaussian **orientation / digit shell**，而不应再尝试仅靠两个 norms
的普通 gcd 继续收费。

---

## 7. Gaussian companion overlap product

对 Gaussian residual support定义
\[
\boxed{
A_\omega
:=
\prod_{p^e\Vert X_\omega^{\flat}}p^{v_p(A^\circ)}.
}
\tag{7.1}

由 `(4.1)`：
\[
\boxed{A_\omega X_\omega^{\flat}\mid N_{\rm num}.}
\tag{7.2}

由 `(4.2)`：
\[
\boxed{A_\omega\mid D_A^{(10)}.}
\tag{7.3}

再用 `(5.1)`：
\[
\boxed{A_\omega\mid10^{2|s_2|}+1.}
\tag{7.4}

所以每当 Gaussian residual prime还同时携带 primitive coefficient depth时，这份 coefficient depth
必须出现为一个 explicit decimal cyclotomic companion，而 Gaussian residual本身位于其上的 norm
excess。

---

## 8. 对 current bootstrap 的更新

上一文件得到
\[
3\log F_-+\log X_\omega^{\flat}\ge2S-o(S)
\]
在 dominant sector成立。

本文不凭空给 `X_omega^flat` 一个尚未证明的更小 absolute height；它做的是把 hard object重新定义为
\[
\boxed{
X_\omega^{\flat}
\mid N_{\rm num}^{\rm exc}
=
\operatorname{core}_{10}\!\left(
N_{\rm num}/(A^\circ,N_{\rm num})
\right).
}
\tag{8.1}

并附带 exact companion
\[
\boxed{
A_\omega X_\omega^{\flat}\mid N_{\rm num},
\qquad
A_\omega\mid10^{2|s_2|}+1.
}
\tag{8.2}

所以新的定量目标不再是 generic `N_num` height，而是：

> **控制 coefficient-overlap 已剥离后的 oriented Gaussian divisor `N_num^exc`。**

这比直接对 `N_num` 做 size bound更精确，也自动兼容之前的 cyclotomic overlap bookkeeping。

---

## 9. 当前 frontier

截至本文，post-tail rough chain已经变成
\[
C_Q
\to X_Q
\to
(X_B^\sharp,X_a^\sharp,X_T,X_g^\flat,X_\omega^\flat),
\]
其中
\[
X_B^\sharp G<F_-,
\qquad
X_a^\sharp Q<F_-,
\]
\[
X_T^2\mid C_Q,
\qquad
\log X_T<S/2,
\]
\[
\log X_g^\flat<S/2+O(1),
\]
而唯一 full-orientation object满足
\[
\boxed{
X_\omega^\flat
\mid
N_{\rm num}^{\rm exc},
}
\]
并且其 coefficient overlap已经由
\[
10^{2|s_2|}+1
\]
显式记录。

进一步 ordinary norm resultant已经被 `Norm-saturation` 审计为 sharp，因此下一步最值得做的是：

1. 在 `Z[i]` 中保留 `pi` / `bar pi` orientation，而不再只看 norms；
2. 把 oriented divisor与 `A^circ` 的 digit shell、anti-source identity或 carrier determinant联立；
3. 寻找一个 Archimedean height小于 `N_num` 本身的 oriented reader；
4. 将其代回
   \[
   3\log F_-+\log X_\omega^\flat\ge2S-o(S)
   \]
   完成 non-canonical dominant LP。

---

## 10. 状态摘要

- **`已严格完成`**：所有 Gaussian residual primes满足 `e+v_p(A^circ)<=min(c,omega)`。
- **`已严格完成`**：`Overlap-stripped-reader`。
- **`已严格完成`**：被剥离 coefficient overlap进入 explicit `10^(2|s2|)+1` carrier。
- **`已严格完成`**：exact `Norm-resultant` 与 `Norm-saturation`。
- **`结构压缩`**：Gaussian hard object从 generic `N_num` 改成 coefficient-overlap-stripped `N_num^exc`；ordinary norm gcd路线已达到 sharp boundary。
- **`待证`**：oriented Gaussian divisor的 Archimedean height；non-canonical branch LP；DD global explicit `<=6` / absolute height。

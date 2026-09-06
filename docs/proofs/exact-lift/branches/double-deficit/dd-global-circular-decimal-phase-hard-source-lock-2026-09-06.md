# DD global circular-decimal phase hard-source lock

> 日期：2026-09-06
>
> 依赖：[`dd-global-euclidean-block-folding-hard-source-lock-2026-09-06.md`](dd-global-euclidean-block-folding-hard-source-lock-2026-09-06.md)、[`dd-corrected-hard-source-split-2026-08-22.md`](dd-corrected-hard-source-split-2026-08-22.md)、`core.md` 的 exact DD gap normalization。
>
> **严格状态：已严格完成（整个 corrected odd non-decimal hard sheet）。**
>
> Euclidean block folding把 hard source target压成 `10^{r_n}`，其中 `0<=r_n<m_2`。本文进一步利用两份此前未同时使用的 exact freedom：
>
> 1. full lift可先除去第三 denominator decimal block，得到 gap-normalized parent
>    \[
>    q_{\rm lcm}A_{12}10^d\equiv \tau a\pmod{\mathfrak C},\qquad d=n-m;
>    \]
> 2. hard modulus只含 odd non-decimal primes，因此 `10` 是 unit；coefficient/right side 中已有的整份 `10`-power可以移入 exponent，而 primitive prefix relation又允许 exponent按 `m_2` 双向折叠。
>
> 结果是一个真正的**圆周最短 decimal phase**
> \[
> \boxed{
> r_{\rm circ}
> =\min_{-s_{10}\le t\le c_{10}}\min_{k\in\mathbf Z}
> |d+t-km_2|,
> }
> \]
> 其中
> \[
> c_{10}=v_{10}(q_{\rm lcm}A_{12}),\qquad
> s_{10}=v_{10}(\tau a).
> \]
> 对同一个 hard modulus
> \[
> \boxed{\mathfrak C_E=X_HT_HN_HJ_H}
> \]
> 可以构造 coefficient-unit congruence读取 `10^{r_circ}`。严格有
> \[
> \boxed{
> 0\le r_{\rm circ}\le
> \max\!\left(0,\left\lfloor\frac{m_2-c_{10}-s_{10}}2\right\rfloor\right)
> \le\left\lfloor\frac{m_2}{2}\right\rfloor.
> }
> \]
> 因而 ordinary-lock failure sharpen 为
> \[
> \boxed{\log_{10}(X_HT_HN_HJ_H)\le r_{\rm circ}\le m_2/2.}
> \]
> 这把 Euclidean failure budget至少再砍半；若 `c_10+s_10>=m_2-1`，则 `r_circ=0`，hard modulus在 failure branch 中必须平凡。

---

## 1. gap-normalized source parent

沿 DD notation

\[
D_3:=H_{\rm sph}b_3-q_{\rm lcm}a_3.
\]

由

\[
H_{\rm sph}-y_3=La,
\qquad
b_3=\omega\tau,
\qquad
10^m=\omega L,
\]

得到 exact identity

\[
\boxed{D_3=10^m\tau a.}
\tag{1.1}
\]

full exact lift modulo primitive denominator prefix

\[
C_Q=Q/(b_1,b_2)
\]

给

\[
q_{\rm lcm}A_{12}10^n\equiv D_3\pmod{C_Q}.
\tag{1.2}
\]

本文只在 corrected hard support生成的 odd non-decimal modulus上工作。记该 modulus为 `mathfrak C_E`；已有 Euclidean theorem证明

\[
\boxed{\mathfrak C_E=X_HT_HN_HJ_H\mid C_Q,}
\tag{1.3}
\]

且

\[
(10,\mathfrak C_E)=1.
\]

因此把 `(1.1)` 代入 `(1.2)` 并在模 `mathfrak C_E` 下约去 `10^m`：

\[
\boxed{
q_{\rm lcm}A_{12}10^d
\equiv \tau a
\pmod{\mathfrak C_E},
\qquad d:=n-m>0.
}
\tag{Gap-normalized-parent}
\]

这与 full-lift parent同源；本文的 sharpen 来自更短 exponent normalization，而不是把它当第二 independent reader。

---

## 2. decimal coefficient phase interval

定义

\[
\boxed{
c_{10}:=v_{10}(q_{\rm lcm}A_{12}),}
\qquad
\boxed{s_{10}:=v_{10}(\tau a).}
\tag{2.1}
\]

这里 `v_10(N)=min(v_2(N),v_5(N))` 表示可整除出的完整十进制幂数。

任取

\[
0\le x\le c_{10},
\qquad
0\le y\le s_{10}.
\]

写

\[
q_{\rm lcm}A_{12}=10^x C_x,
\qquad
\tau a=10^y D_y.
\]

因为 `10` 在 `mathfrak C_E` 上可逆，`Gap-normalized-parent` 等价于 unit-group congruence

\[
\boxed{
C_x10^{d+x-y}\equiv D_y\pmod{\mathfrak C_E}.}
\tag{2.2}
\]

exponent shift

\[
t:=x-y
\]

可遍历所有整数

\[
\boxed{-s_{10}\le t\le c_{10}.}
\tag{2.3}
\]

即 hard source不是只看到单点 phase `d`，而是看到连续整数 interval

\[
[d-s_{10},\ d+c_{10}].
\]

---

## 3. primitive prefix允许双向 `m_2` folding

写

\[
C_Q=u_1 10^{m_2}+u_2,
\qquad (u_1,u_2)=1.
\]

对 `p|mathfrak C_E` 已有

\[
(p,10u_1u_2)=1,
\]

以及

\[
\boxed{u_1 10^{m_2}\equiv-u_2\pmod{\mathfrak C_E}.}
\tag{3.1}
\]

考虑任意 unit congruence

\[
A10^E\equiv B\pmod{\mathfrak C_E},
\qquad E\in\mathbf Z.
\]

若写

\[
E=km_2+r,
\qquad 0\le r<m_2,
\]

则：

- `k>=0` 时，乘 `u_1^k` 并使用 `(3.1)` 得
  \[
  A(-u_2)^k10^r\equiv Bu_1^k;
  \]
- `k<0` 时令 `ell=-k`，先乘 `10^{ell m_2}` 再乘 `u_1^ell`，得
  \[
  Au_1^\ell10^r\equiv B(-u_2)^\ell.
  \]

所以任意整数 phase都可化成 `[0,m_2)` 内 exponent，且两侧 coefficients仍是模 `mathfrak C_E` 的 units。

若 `r>m_2/2`，把 congruence乘 `10^{m_2-r}`，再用 `(3.1)` 处理 `10^{m_2}`，可把 exponent替换成

\[
m_2-r<m_2/2.
\]

因此任意 phase `E` 都可化成 target

\[
\boxed{10^{\operatorname{dist}(E,m_2\mathbf Z)}},
\]
其中

\[
\operatorname{dist}(E,m_2\mathbf Z)
:=\min_{k\in\mathbf Z}|E-km_2|.
\]

---

## 4. circular phase定义与 exact interval bound

定义

\[
\boxed{
 r_{\rm circ}
 :=\min_{-s_{10}\le t\le c_{10}}
 \operatorname{dist}(d+t,m_2\mathbf Z).
}
\tag{4.1}
\]

显然

\[
\boxed{0\le r_{\rm circ}\le\lfloor m_2/2\rfloor.}
\tag{4.2}
\]

还可利用 phase interval的长度得到更强 exact bound。令

\[
L_{10}:=c_{10}+s_{10}.
\]

interval `[d-s_10,d+c_10]` 含 `L_10+1` 个连续整数。

若它含某个 `m_2` 的倍数，则 `r_circ=0`。若不含，则整个 interval位于两个相邻 multiples `km_2,(k+1)m_2` 之间。设左右 endpoint到这两个 multiples的正整数距离分别为 `ell,rho`。则

\[
ell+L_{10}+\rho=m_2,
\qquad \ell,\rho\ge1,
\]

且

\[
r_{\rm circ}=\min(\ell,\rho).
\]

因此

\[
\boxed{
 r_{\rm circ}
 \le
 \max\!\left(
 0,
 \left\lfloor\frac{m_2-L_{10}}2\right\rfloor
 \right).
}
\tag{Circular-interval-bound}
\]

特别地

\[
\boxed{L_{10}\ge m_2-1\Longrightarrow r_{\rm circ}=0.}
\tag{4.3}
\]

---

## 5. hard local depth不受 decimal shifting影响

固定 corrected hard prime。记

\[
E=v_p(b_1)=v_p(b_2),
\quad j=v_p(b_3),
\quad M=\max(E,j),
\]

\[
t=v_p(A_{12}),
\quad n_0=v_p(N_0),
\quad h>0.
\]

corrected hard ledger为

\[
\boxed{c=h+2t+n_0+M+j.}
\tag{5.1}
\]

由于 `p` 是 odd non-decimal prime，所有 `10`-shifts均为 p-units。primitive prefix又给 `p\nmid u_1u_2`。

左侧 raw coefficient `q_lcm A_12` 的 p-depth为

\[
\boxed{M+t.}
\tag{5.2}
\]

右侧由 hard gap baseline

\[
v_p(a)=t+(E-j)_+,
\]
以及 `v_p(tau)=j` 得

\[
\boxed{
v_p(\tau a)
=j+t+(E-j)_+
=M+t.
}
\tag{5.3}
\]

因此无论选择 `(x,y)`、向左/向右 fold多少次，两个 coefficients在该 prime的 common depth始终精确为 `M+t`。约去后剩余 modulus exponent为

\[
\boxed{
c-(M+t)=h+t+n_0+j.}
\tag{5.4}
\]

这正是 Euclidean theorem中的 hard exponent。

所以 circular normalization读取的仍是**同一个** global hard modulus

\[
\boxed{
\mathfrak C_E=X_HT_HN_HJ_H.
}
\tag{Same-hard-modulus}
\]

---

## 6. phase-sharp ordinary lock / failure dichotomy

取达到 `(4.1)` 最小值的 `t` 与 nearest multiple，并按 §§2--3 做 coefficient-unit normalization。由 §5，存在整数 units `A_circ,B_circ` 满足

\[
\boxed{
\mathfrak C_E\mid
A_{\rm circ}10^{r_{\rm circ}}-B_{\rm circ},
\qquad
(A_{\rm circ}B_{\rm circ},\mathfrak C_E)=1.
}
\tag{Circular-reader}
\]

若

\[
\log_{10}\mathfrak C_E>r_{\rm circ},
\]

则

\[
0<10^{r_{\rm circ}}<\mathfrak C_E
\]

并得到 ordinary exact lock

\[
\boxed{
10^{r_{\rm circ}}
=[B_{\rm circ}A_{\rm circ}^{-1}]_{\mathfrak C_E}.
}
\tag{Circular-lock}
\]

若 ordinary criterion失败，则

\[
\boxed{
\log_{10}(X_HT_HN_HJ_H)
\le r_{\rm circ}.
}
\tag{Circular-failure-charge}
\]

结合 `(Circular-interval-bound)`：

\[
\boxed{
\log_{10}(X_HT_HN_HJ_H)
\le
\max\!\left(
0,
\left\lfloor\frac{m_2-c_{10}-s_{10}}2\right\rfloor
\right)
\le\frac{m_2}{2}.
}
\tag{6.1}

这严格优于上一 Euclidean theorem 的 `<=r_n<m_2` universal failure budget。

---

## 7. 作用域与 no-double-count

本文没有产生第二 independent source parent：

- `Gap-normalized-parent` 与 full exact lift是同一个 parent约去 `10^m` 后的形式；
- `(x,y)` 只使用 modulus上 `10` 为 unit，把已有 decimal smooth factor移入 exponent；
- 双向 `m_2` folding只使用 primitive denominator prefix relation。

所以这些变换不能与 Euclidean/sixfold reader重复计数成多个 moduli。

新增内容是**同一 exact parent的最短 phase normalization**：failure-side budget从 `<m_2` sharpen 到 `<=m_2/2`，并显式读取 coefficient/right-side 的 decimal smooth capacity。

---

## 8. 当前意义

corrected post-tail hard branch现在满足：

\[
\boxed{
\mathfrak C_E=X_HT_HN_HJ_H
}
\]

要么 exact ordinary读取一个长度

\[
\boxed{r_{\rm circ}\le m_2/2}
\]

的 pure decimal power，要么 hard/source+baseline全部高度由这份 circular phase支付。

结合后续 corrected failure bootstrap，可把 no-residual small-factor lower进一步 sharpen 到

\[
\log F_-\ge S-r_{\rm circ}/4-o(S),
\]

因此 universal consequence达到

\[
\log F_-\ge7S/8-o(S).
\]

该最后一步在独立 continuation 中记录，以保持 source lock 与 Schmidt/small-factor bookkeeping分离。

---

## 9. 状态摘要

- **已严格完成：** gap-normalized source parent；
- **已严格完成：** coefficient/right-side decimal phase interval；
- **已严格完成：** arbitrary integer phase的双向 primitive-prefix folding；
- **已严格完成：** exact circular interval bound；
- **已严格完成：** hard local residual `h+t+n_0+j` 在所有 decimal shifts下保持不变；
- **已严格完成：** circular ordinary-lock/failure-charge dichotomy；
- **未证明：** ordinary circular lock branch impossible、global explicit strict gap、DD emptiness。

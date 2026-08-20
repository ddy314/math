# A2-only Source Angle Ledger

> 本文件是细粒度研究记录的机械归并账本。各来源的标题、正文和证明状态原样保留；账本中的局部闭合、有限证书或降级路线均不表示该分支或主不存在性命题已经关闭。

## 来源索引

- [`spontaneous-alpha-supported-resultant.md`](#source-spontaneous-alpha-supported-resultant)
- [`spontaneous-angle-content.md`](#source-spontaneous-angle-content)
- [`spontaneous-angle-overlap-depth.md`](#source-spontaneous-angle-overlap-depth)
- [`spontaneous-angle-pair-cq-nogo.md`](#source-spontaneous-angle-pair-cq-nogo)
- [`spontaneous-angle-pair-q0-depth.md`](#source-spontaneous-angle-pair-q0-depth)
- [`spontaneous-angle-parity.md`](#source-spontaneous-angle-parity)
- [`spontaneous-angle.md`](#source-spontaneous-angle)
- [`spontaneous-bad-primes.md`](#source-spontaneous-bad-primes)
- [`spontaneous-companion-common-parity-dichotomy.md`](#source-spontaneous-companion-common-parity-dichotomy)
- [`spontaneous-companion-external-tail-budget.md`](#source-spontaneous-companion-external-tail-budget)
- [`spontaneous-cross-sign-biquadratic.md`](#source-spontaneous-cross-sign-biquadratic)
- [`spontaneous-cross-sign-height-shadow.md`](#source-spontaneous-cross-sign-height-shadow)
- [`spontaneous-cross-sign-height1-shadow.md`](#source-spontaneous-cross-sign-height1-shadow)
- [`spontaneous-cross-sign-sphere.md`](#source-spontaneous-cross-sign-sphere)
- [`spontaneous-cstar-audit.md`](#source-spontaneous-cstar-audit)
- [`spontaneous-denominator-common.md`](#source-spontaneous-denominator-common)
- [`spontaneous-denominator-depth-matrix.md`](#source-spontaneous-denominator-depth-matrix)
- [`spontaneous-denominator-depth-residuals.md`](#source-spontaneous-denominator-depth-residuals)
- [`spontaneous-denominator-repeated-common.md`](#source-spontaneous-denominator-repeated-common)
- [`spontaneous-fixed11-audit.md`](#source-spontaneous-fixed11-audit)
- [`spontaneous-jh-root-gap.md`](#source-spontaneous-jh-root-gap)
- [`spontaneous-omega-biquadratic.md`](#source-spontaneous-omega-biquadratic)
- [`spontaneous-omega-content-common.md`](#source-spontaneous-omega-content-common)
- [`spontaneous-oplus-thetaplus-root-gap.md`](#source-spontaneous-oplus-thetaplus-root-gap)
- [`spontaneous-prefix-boundaries.md`](#source-spontaneous-prefix-boundaries)
- [`spontaneous-prefix-branch-audit.md`](#source-spontaneous-prefix-branch-audit)
- [`spontaneous-prefix-eliminant.md`](#source-spontaneous-prefix-eliminant)
- [`spontaneous-pure-root-gap.md`](#source-spontaneous-pure-root-gap)
- [`spontaneous-residual-parity-doubling.md`](#source-spontaneous-residual-parity-doubling)
- [`spontaneous-sign-companion-parity.md`](#source-spontaneous-sign-companion-parity)
- [`spontaneous-single-branch-syzygy.md`](#source-spontaneous-single-branch-syzygy)
- [`spontaneous-single-branch.md`](#source-spontaneous-single-branch)
- [`spontaneous-source-common-gate.md`](#source-spontaneous-source-common-gate)
- [`spontaneous-source-common-integer.md`](#source-spontaneous-source-common-integer)
- [`spontaneous-source-common-parity.md`](#source-spontaneous-source-common-parity)
- [`spontaneous-source-conjugate-bridge.md`](#source-spontaneous-source-conjugate-bridge)
- [`spontaneous-source-depth-transfer.md`](#source-spontaneous-source-depth-transfer)
- [`spontaneous-source-equal-depth-nogo.md`](#source-spontaneous-source-equal-depth-nogo)
- [`spontaneous-source-equal-depth.md`](#source-spontaneous-source-equal-depth)
- [`spontaneous-source-halfdepth-blowup.md`](#source-spontaneous-source-halfdepth-blowup)
- [`spontaneous-source-numerator-length.md`](#source-spontaneous-source-numerator-length)
- [`spontaneous-source-parity-angle-budget.md`](#source-spontaneous-source-parity-angle-budget)
- [`spontaneous-source-parity-angle-overlap.md`](#source-spontaneous-source-parity-angle-overlap)
- [`spontaneous-source-parity-collision-gate.md`](#source-spontaneous-source-parity-collision-gate)
- [`spontaneous-source-parity-common-gcd.md`](#source-spontaneous-source-parity-common-gcd)
- [`spontaneous-source-parity-decimal-gcd.md`](#source-spontaneous-source-parity-decimal-gcd)
- [`spontaneous-source-parity-decimal-square-gate.md`](#source-spontaneous-source-parity-decimal-square-gate)
- [`spontaneous-source-parity-numerator-defect.md`](#source-spontaneous-source-parity-numerator-defect)
- [`spontaneous-source-parity-reuse-depth.md`](#source-spontaneous-source-parity-reuse-depth)
- [`spontaneous-source-prefix-simple.md`](#source-spontaneous-source-prefix-simple)
- [`spontaneous-source-primary-bridge.md`](#source-spontaneous-source-primary-bridge)
- [`spontaneous-source-reuse-cross-pair-asymmetry.md`](#source-spontaneous-source-reuse-cross-pair-asymmetry)
- [`spontaneous-source-reuse-cross-pair-fixed67.md`](#source-spontaneous-source-reuse-cross-pair-fixed67)
- [`spontaneous-source-reuse-cross-pair-length.md`](#source-spontaneous-source-reuse-cross-pair-length)
- [`spontaneous-source-saturation-parity.md`](#source-spontaneous-source-saturation-parity)
- [`spontaneous-source-sheet-collision.md`](#source-spontaneous-source-sheet-collision)
- [`spontaneous-source-singular-decimal-orbit.md`](#source-spontaneous-source-singular-decimal-orbit)
- [`spontaneous-source-singular-resolution.md`](#source-spontaneous-source-singular-resolution)
- [`spontaneous-source-target-support-separation.md`](#source-spontaneous-source-target-support-separation)
- [`spontaneous-sphere-roots.md`](#source-spontaneous-sphere-roots)
- [`spontaneous-tangent-decimal.md`](#source-spontaneous-tangent-decimal)
- [`spontaneous-tangent-f-denominator.md`](#source-spontaneous-tangent-f-denominator)
- [`spontaneous-tangent-psif-overlap.md`](#source-spontaneous-tangent-psif-overlap)
- [`spontaneous-triple-companion-external-budget.md`](#source-spontaneous-triple-companion-external-budget)

<a id="source-spontaneous-alpha-supported-resultant"></a>

> 整合来源：`spontaneous-alpha-supported-resultant.md`

# A2 `alpha`-supported angle/common global resultant

> **依赖：** `primitive-reduction.md`、`spontaneous-height-parity-ledger.md`、`spontaneous-omega-content-common.md`、`spontaneous-prefix-branch-audit.md`。
>
> **严格状态：**本文把所有 `p|alpha=TK+a_3` 的 angle contact一次性合并。把 exact sphere限制到 `alpha=0` 后，它精确分成 concatenated-content square与 height norm；再对 angle 的第三分母线性式消元，得到 `T^4 C_omega^2 H_O`。因此 `alpha`-supported angle sector只有三张 pure-prefix sheet：`A_-=0` 的 omega-content sheet、以及 `H_1=0,H_2=0` 的两张 height orientations。本文进一步审计三张 sheet 的 pairwise collision：对 genuine non-`3` inert prime，碰撞只会回到已知 source sheet、q-boundary，或 `K=0` 的 non-genuine height boundary；不存在第四种 sheet collision。本文不证明所有 simple alpha-supported common roots为空，也不宣称 A2 closure。

---

## 1. exact sphere 在 `alpha=0` 上完全分裂

固定 reflection endpoint：

\[
N=10^M,
\quad T=10^m,
\quad A=a_2,
\quad B=b_2,
\]

\[
Q=B+2N,
\qquad
K=9N+10A,
\]

\[
N_0=\left(\frac{9B}{2}\right)^2+A^2.
\]

原 sphere equation为

\[
B^2b_3^2(TK+a_3)^2
=(TQ+b_3)^2
\left(N_0b_3^2+B^2a_3^2\right).
\tag{1.1}
\]

令

\[
\alpha:=TK+a_3.
\]
在 `alpha=0` 上有

\[
a_3=-TK.
\]
因此 (1.1) 精确退化为

\[
\boxed{
(TQ+b_3)^2
\left(N_0b_3^2+B^2T^2K^2\right)=0.
}
\tag{1.2}
\]

这不是模素数猜测，而是 exact polynomial factorization。

两因子的几何意义正是：

- `TQ+b_3=0`：concatenated denominator也为零，即 `omega` content；
- `N_0b_3^2+B^2T^2K^2=0`：height / `W_q` sphere norm。

所以任何 `alpha`-supported angle contact从一开始就只能来自 content 或 height，没有第四种 third-block mechanism。

---

## 2. 消掉 third denominator：全局 resultant只有 `C_omega^2 H_O`

angle raw linear integer为

\[
\mathcal O_+
=T\mathcal U_\Omega+2A^2Qb_3,
\]

其中

\[
\mathcal U_\Omega
=(45B^2-2AN)^2-A^2B(99B-4N).
\]

`spontaneous-omega-content-common.md` 定义

\[
\boxed{
\mathcal C_\omega
:=\mathcal U_\Omega-2A^2Q^2.
}
\tag{2.1}
\]

`spontaneous-height-parity-ledger.md` 定义

\[
\boxed{
\mathcal H_O
:=N_0\mathcal U_\Omega^2
+4A^4B^2Q^2K^2.
}
\tag{2.2}

现在直接对 `b_3` 求 resultant：

\[
\boxed{
\begin{aligned}
&\operatorname{Res}_{b_3}
\Bigl(
T\mathcal U_\Omega+2A^2Qb_3,\\
&\qquad\qquad
(TQ+b_3)^2(N_0b_3^2+B^2T^2K^2)
\Bigr)\\
&\qquad
=T^4\mathcal C_\omega^2\mathcal H_O.
\end{aligned}}
\tag{2.3}
\]

因此 genuine `alpha`-supported angle contact 必满足

\[
\boxed{
\mathcal C_\omega\mathcal H_O=0.
}
\tag{2.4}

`C_omega` 对应 content root；`H_O` 对应 height roots。

---

## 3. primitive orientation：整个 alpha-resultant 是 `1 mod 8` norm

已有

\[
v_2(\mathcal C_\omega)=2M+2,
\]
且 signed primitive

\[
\mathcal C_\omega/2^{2M+2}\equiv3\pmod4.
\]
因此其平方 primitive恒为 `1 mod 8`。

另有

\[
v_2(\mathcal H_O)=4M+4,
\qquad
\widehat{\mathcal H}_O
:=\mathcal H_O/2^{4M+4}\equiv1\pmod8.
\]

定义

\[
\boxed{
\mathcal R_\alpha
:=\mathcal C_\omega^2\mathcal H_O.
}
\tag{3.1}
\]

则

\[
\boxed{
v_2(\mathcal R_\alpha)=8M+8,}
\tag{3.2}
\]

\[
\boxed{
\widehat{\mathcal R}_\alpha
:=\frac{\mathcal R_\alpha}{2^{8M+8}}>0,
\qquad
\widehat{\mathcal R}_\alpha\equiv1\pmod8.
}
\tag{3.3}
\]

所以整个 `alpha`-supported angle resultant是一个 positive even-inert-parity natural norm。注意这并不单独证明实际 `alpha`-supported prime子集的 parity为偶；resultant仍可能包含不进入实际 `alpha` 的额外 primes。它的严格作用是把 alpha-sector全部装进一个 `1 mod 8` carrier。

---

## 4. pure-prefix 三-sheet factorization

使用 normalized variables

\[
x=B/N,
\qquad y=10A/N.
\]

content sheet为

\[
\boxed{
A_-(x,y)
=202500x^4-(101x^2+4x+4)y^2-1800x^2y.
}
\tag{4.1}
\]

height ledger给两张 orientation：

\[
\boxed{
H_1(x,y)
=202500x^4+101x^2y^2+4xy^2+4y^2,
}
\tag{4.2}
\]

\[
\boxed{
\begin{aligned}
H_2(x,y)={}&
410062500x^6-402975x^4y^2-7290000x^4y\\
&+8100x^3y^2+101x^2y^4+3600x^2y^3\\
&+40500x^2y^2+4xy^4+4y^4.
\end{aligned}}
\tag{4.3}
\]

而 exact integer factorization为

\[
\mathcal H_1\mathcal H_2=4\mathcal H_O.
\]
因此 (2.4) 在 genuine scaling下就是

\[
\boxed{
A_-\,H_1\,H_2=0.
}
\tag{4.4}

所以 `alpha`-supported angle prime具有三种、且仅三种 prefix标签：

\[
\boxed{
\text{omega-content},\quad
\text{height-1},\quad
\text{height-2}.
}
\tag{4.5}

下面审计标签是否会重叠。

---

# pairwise collision audit

## 5. 三个 exact pairwise resultants

直接对 `y` 求 resultant：

\[
\boxed{
\operatorname{Res}_y(A_-,H_1)
=164025000000\,x^8P(x)R(x),
}
\tag{5.1}
\]

\[
\boxed{
\operatorname{Res}_y(A_-,H_2)
=672605015625000000\,x^{12}(x+2)^4P(x)R(x),
}
\tag{5.2}
\]

\[
\boxed{
\operatorname{Res}_y(H_1,H_2)
=10761680250000000000\,x^{12}P(x)R(x)Q_\times(x),
}
\tag{5.3}
\]

其中

\[
\boxed{P(x):=101x^2+4x+4,}
\tag{5.4}
\]

\[
\boxed{R(x):=101x^2+4x+8,}
\tag{5.5}
\]

\[
\boxed{Q_\times(x):=2500x^4+101x^2+4x+4.}
\tag{5.6}
\]

因此除 `x=0`、`x=-2` 等既有 boundary外，三张 sheet 的所有 overlap都由 `P,R,Q_x` 控制。

---

## 6. `P=0` 对 inert prime完全不可能

注意

\[
\boxed{
P(x)=(10x)^2+(x+2)^2.
}
\tag{6.1}
\]

若

\[
p\equiv3\pmod4,
\qquad p\nmid2x(x+2),
\]
则两个平方和不可能为零。因此

\[
\boxed{P(x)\not\equiv0\pmod p.}
\tag{6.2}

等价地，其 discriminant

\[
4^2-4\cdot101\cdot4=-1600=-40^2
\]
也直接要求 `-1` 为平方。

所以 `P` factor在 genuine inert channel完全删除。

---

## 7. `R=0` 精确回流到 source first layer

把 `A_-` 看成 `y` 的二次式。其 discriminant为

\[
\boxed{
\operatorname{Disc}_y(A_-)
=810000x^4R(x).
}
\tag{7.1}
\]

当 `R=0` 且 `x` 为 unit时，`A_-=0` 只有一个 double root。因为

\[
P=R-4=-4,
\]
该 root为

\[
\boxed{y=225x^2.}
\tag{7.2}
\]

这正是 source first-layer sheet

\[
d:=225x^2-y=0.
\]

直接代入三张 sheet也有

\[
A_-(x,225x^2)
=-50625x^4R(x),
\tag{7.3}
\]

\[
H_1(x,225x^2)
=50625x^4R(x),
\tag{7.4}
\]

\[
H_2(x,225x^2)
=102515625x^6(25x^2+1)R(x).
\tag{7.5}
\]

所以所有 `R`-collision都只是重新落回已规范化的 source sheet；它不是新的 alpha-supported overlap mechanism。

---

## 8. `H_1/H_2` 的 quartic collision只剩 source或 `K=0`

对 `P` 为 unit，`H_2` 除以 `H_1` 的余式精确为

\[
\boxed{
\frac{7290000x^4}{P(x)}
\left[
22500x^4-(201x^2+4x+4)y-900x^2
\right].
}
\tag{8.1}
\]

因此共同根还必须满足

\[
(201x^2+4x+4)y=900x^2(25x^2-1).
\tag{8.2}

把该线性根代回 `H_1`，numerator分解为

\[
\boxed{
202500x^4R(x)Q_\times(x).
}
\tag{8.3}

所以在已经排除 `R=0` source collision后，只剩

\[
Q_\times(x)=0.
\]

而 `H_1=0` 与 `Q_x=0` 给

\[
P=-2500x^4,
\]
从而

\[
-2500x^4y^2+202500x^4=0,
\]
即

\[
\boxed{y^2=81.}
\tag{8.4}

因此 `y=\pm9`。

- `y=-9` 直接给
  \[
  K=N(y+9)=0.
  \]
  在 height channel `alpha=TK+a_3=0` 下进一步强迫
  \[
  a_3=0\pmod p,
  \]
  与 genuine height prime的 `p\nmid a_3` 分离条件冲突。

- `y=+9` 若同时满足 `H_2=0`，除 `Q_x=0` 外还必须有
  \[
  201x^2+4x+4=0.
  \]
  这与 `Q_x=0` 的 non-`3` inert exception若发生，会进一步落入 `R=0`；例如唯一小 inert coincidence `p=107,x=43` 满足
  \[
  225x^2\equiv9=y\pmod{107},
  \]
  所以仍是 §7 的 source sheet，而不是新分支。

因此严格地：

\[
\boxed{
H_1=H_2=0
\Longrightarrow
\text{source collision}
\quad\text{或}\quad
K=0\text{ non-genuine height boundary}.
}
\tag{8.5}

---

## 9. alpha-supported angle标签唯一性

综合 §§5--8。对 genuine non-`3` inert prime，排除已有

- source sheet `d=0`；
- q-boundary `x=-2`；
- trivial `x=0`；
- non-genuine `K=0` height boundary；

以后：

\[
\boxed{
A_-=0,\quad H_1=0,\quad H_2=0
}
\]
三张 sheet 两两互斥。

所以每一枚 genuine `alpha`-supported angle prime都有唯一来源标签：

\[
\boxed{
\omega\text{-content}
\quad\text{or}\quad
W_q\text{-height orientation 1}
\quad\text{or}\quad
W_q\text{-height orientation 2}.
}
\tag{9.1}

这消除了 global parity ledger 中 content/height double-counting 的歧义。

---

## 10. 加入 additive carrier

在 `alpha=0` 上，`spontaneous-height-parity-ledger.md` 的 exact identity退化为

\[
\boxed{
\Theta_{\rm dec}=T\mathcal J_H.
}
\tag{10.1}
\]

因此 `alpha`-supported angle/additive common prime的完整 pure-prefix first-layer系统只有

\[
\boxed{
\mathcal J_H=0,
\qquad
A_-H_1H_2=0.
}
\tag{10.2}

并且三张 angle sheet在 genuine nonboundary channel具有唯一标签。

这比逐个 source ratio / third block审计更强：整个 common-`alpha` sector已经被压成第一、二 decimal blocks上的三个 simple sheet与一个 additive quadratic。

---

## 11. 对 global parity 的意义

本文得到

\[
\widehat{\mathcal R}_\alpha\equiv1\pmod8
\]
以及三-sheet唯一性，但仍不能单独推出实际 `alpha`-supported common gcd的 inert parity为偶，因为 resultant可能含不进入 `alpha` 的额外 prime。

严格的新信息是：

1. alpha-supported angle contact的**全部自然候选**位于一个 positive `1 mod8` norm carrier；
2. content / height / height 两张 orientation不会在 genuine prime上重复计数；
3. 加入 additive以后只需研究 `J_H` 与三张 prefix sheets的 simple decimal orbit。

因此 `G_sp=1 mod4` 所需的“两个 residual odd suppliers”若继续躲在 `alpha`-supported sector，必须分布在这些唯一标签的 simple branches上；不存在隐藏的第四种 overlap或 singular branching。

A2 仍保持 open。

---

<a id="source-spontaneous-angle-content"></a>

> 整合来源：`spontaneous-angle-content.md`

# A2 spontaneous angle primitive carrier 的 source-content 分离

> **依赖：** `spontaneous-angle-parity.md`、`source-discriminant.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文证明 `spontaneous-angle-parity.md` 的 primitive positive `3 mod 4` integer `widehat(O)_sp` 不能从 source content `c_u g` 中获得任何 non-`5` odd prime，特别不能从那里获得 `3 mod 4` inert parity。这个结论与已有 `gcd(widehat(T)_2,10c_ug)=1` 平行。本文并不排除 denominator/source-excess/spontaneous primes，也不宣称 A2 全局关闭。

---

## 1. primitive angle integer

沿用

\[
\widehat{\mathcal O}_{\rm sp}
=5^m\mathcal U_\Omega^\sharp
+2A^2Q_0b_{30},
\tag{1.1}
\]
其中

\[
A=a_2,
\qquad
b_0=c_ug,
\qquad
b_{30}=5^dc_Qc_u,
\tag{1.2}
\]

\[
Q_0=c_Qq=5^M+2^mgc_u,
\tag{1.3}
\]
以及

\[
\begin{aligned}
\mathcal U_\Omega^\sharp
={}&\left(45\,2^{M+2m+1}b_0^2-A5^M\right)^2\\
&-A^2 2^{m+1}b_0
\left(99\,2^{m-1}b_0-5^M\right).
\end{aligned}
\tag{1.4}
\]

已有

\[
\widehat{\mathcal O}_{\rm sp}>0,
\qquad
\widehat{\mathcal O}_{\rm sp}\equiv3\pmod4.
\tag{1.5}
\]

---

## 2. `已严格完成`：任何 odd prime `p|c_u`, `p!=5` 都不能整除 angle carrier

设

\[
p\mid c_u,
\qquad p\ne2,5.
\]

则 `b_0` 与 `b_30` 都被 `p` 整除。因此 (1.4) 给

\[
\mathcal U_\Omega^\sharp
\equiv A^25^{2M}\pmod p,
\]
而 (1.1) 的第二项为零：

\[
\boxed{
\widehat{\mathcal O}_{\rm sp}
\equiv A^25^{2M+m}\pmod p.
}
\tag{2.1}
\]

因为 `c_u|B=b_2` 且 `(A,B)=1`，故 `p∤A`；又 `p!=5`。于是右边为单位：

\[
\boxed{
p\mid c_u,\ p\ne2,5
\Longrightarrow
p\nmid\widehat{\mathcal O}_{\rm sp}.}
\tag{2.2}
\]

特别地任意 `3 mod 4` prime 都满足 `p!=5`，所以 angle side 的 inert parity 绝不来自 `c_u`。

---

## 3. `已严格完成`：任何 odd `p|g`, `p!=5` 也不能整除 angle carrier

设

\[
p\mid g,
\qquad p\ne2,5.
\]

则

\[
b_0=c_ug\equiv0\pmod p,
\]
所以仍有

\[
\mathcal U_\Omega^\sharp
\equiv A^25^{2M}\pmod p.
\tag{3.1}
\]

由 (1.3)：

\[
Q_0\equiv5^M\pmod p.
\tag{3.2}
\]

代入 (1.1)：

\[
\begin{aligned}
\widehat{\mathcal O}_{\rm sp}
&\equiv
A^25^{2M+m}
+2A^25^M5^dc_Qc_u\\
&=A^25^{M+d}
\left(5^{M+m-d}+2c_Qc_u\right).
\end{aligned}
\]

记

\[
\lambda=m-d.
\]
旧 source relation 为

\[
5^{M+\lambda}+c_Qc_u=g\theta.
\tag{3.3}
\]

所以模 `p|g`：

\[
5^{M+m-d}+2c_Qc_u
=5^{M+\lambda}+2c_Qc_u
\equiv c_Qc_u.
\]
因此

\[
\boxed{
\widehat{\mathcal O}_{\rm sp}
\equiv A^25^{M+d}c_Qc_u
\pmod p.}
\tag{3.4}
\]

对于 odd prime `p|g`：

- `(A,B)=1` 且 `g|B`，故 `p∤A`；
- `gcd(c_u,g)=1`，故 `p∤c_u`；
- `g=2^{t-1}\rho` 且旧本原性 `gcd(c_Q,\rho)=1`，故 odd `p|g` 时 `p∤c_Q`；
- 本节假设 `p!=5`。

故 (3.4) 为单位：

\[
\boxed{
p\mid g,\ p\ne2,5
\Longrightarrow
p\nmid\widehat{\mathcal O}_{\rm sp}.}
\tag{3.5}
\]

---

## 4. inert source-content exclusion

综合 §§2–3，任意 odd inert prime

\[
p\equiv3\pmod4
\]
自动满足 `p!=5`，所以

\[
\boxed{
p\mid c_ug,
\quad p\equiv3\pmod4
\Longrightarrow
p\nmid\widehat{\mathcal O}_{\rm sp}.}
\tag{4.1}
\]

也就是说 `widehat(O)_sp≡3 mod4` 所强迫的 odd inert parity 必须来自 `c_ug` 之外。

已有 additive side 更强的

\[
\boxed{
\gcd(\widehat{\mathcal T}_2,10c_ug)=1.
}
\tag{4.2}
\]

所以两侧 parity carrier 在 source content 上完全对齐：

\[
\boxed{
\begin{array}{c|c}
\text{primitive object}&\text{non-5 odd source-content primes}\\ \hline
\widehat{\mathcal O}_{\rm sp}&\text{none from }c_ug\\
\widehat{\mathcal T}_2&\text{none from }c_ug
\end{array}}
\tag{4.3}
\]

---

## 5. 与 prime-source 图的意义

这一步不能单独强迫

\[
G_{\rm sp}
=\gcd(\widehat{\mathcal O}_{\rm sp},\widehat{\mathcal T}_2)
\equiv3\pmod4.
\]

如果 `G_sp≡1 mod4`，两侧 residual quotient 仍可能各自携带不同 inert prime。但 (4.3) 已经排除了最廉价的一整类解释：这些 residual inert primes 不可能只是 source content `c_u` 或 `g` 的旧因子。

因此 residual parity 现在必须进入真正的 prime-source geometry：

- q/f denominator contact；
- source excess (`Phi_s / D_src`)；
- 或 pure spontaneous contact。

下一步应该把 `Omega_sp` 与 q/f/source 三条 overlap resultant 的 valuation parity，和 additive side 已有 saturation/height 分类逐类对齐；若 residual denominator/source contribution 都能证明为偶 parity，就会强迫 `G_sp≡3 mod4`。

---

<a id="source-spontaneous-angle-overlap-depth"></a>

> 整合来源：`spontaneous-angle-overlap-depth.md`

# A2 spontaneous angle 与 source/q/f overlap 的赋值定律

> **依赖：** `spontaneous-angle.md`、`hensel.md`、`spontaneous-angle-parity.md`、`spontaneous-angle-content.md`。
>
> **严格状态：**旧 `Omega_sp` resultant 已把 source、q-side、f-side 的一阶交点分别压回 `D_src` 或 `Delta_0`。本文把这些一阶 resultant 升级为 exact `p`-adic depth laws：在 genuine units 下，angle valuation 由两个接触深度的较浅者决定，只有**等深 cancellation**才可能额外提升。source excess 尤其强：非等深时 angle valuation 精确为偶数 `2h`。因此 angle primitive integer 的 residual odd inert parity 若来自 source pool，只能集中在 source 等深 cancellation 层；q/f pool 也只有等深层能产生超出较浅深度的额外奇偶。本文不宣称这些等深层已经排除，也不宣称 A2 全局关闭。

---

## 1. 统一记号

沿用

\[
d:=225x^2-y,
\qquad
\Delta_0:=2025x^2-18y-y^2,
\]

\[
\Phi_s=(99x-4)r_s-2x-4,
\]

\[
A_{\rm sp}=4d^2-xy^2(99x-4),
\]

\[
\boxed{
\Omega_{\rm sp}
=A_{\rm sp}r_s+2xy^2(x+2)
=4r_sd^2-xy^2\Phi_s.
}
\tag{1.1}
\]

f-denominator line 为

\[
F_f:=r_s(x+2)+2x.
\tag{1.2}
\]

以下所有 valuation law 都只声称用于 genuine non-`2,3,5` inert prime；因此相关 decimal/source denominators、`x,y,r_s,A_sp` 等按对应 channel 的 separation 假设均为单位，除非明确写出的接触量。

---

## 2. `已严格完成`：source excess 非等深时 angle valuation 精确为偶数

设 `p` 为 genuine source excess inert prime，并写

\[
p^{2h}\Vert\sigma,
\qquad h\ge1.
\]

`hensel.md` 已严格证明

\[
\boxed{v_p(\Phi_s)=2h,}
\tag{2.1}
\]

以及

\[
\boxed{v_p(d)\ge h.}
\tag{2.2}
\]

令

\[
e_d:=v_p(d).
\]

由 (1.1)，两项 valuation 分别为

\[
v_p(4r_sd^2)=2e_d,
\]

\[
v_p(xy^2\Phi_s)=2h.
\]

因为 `e_d>=h`，只有两种情况。

### 2.1 严格深于 threshold

若

\[
e_d>h,
\]
则

\[
2h<2e_d.
\]
两项 valuation 不同，较浅项不可能被较深项抵消，因此

\[
\boxed{
v_p(\Omega_{\rm sp})=2h.}
\tag{2.3}
\]

特别地 valuation 必为偶数。

### 2.2 唯一危险层：等深

若

\[
e_d=h,
\]
则两项都恰有深度 `2h`：

\[
\boxed{
v_p(\Omega_{\rm sp})\ge2h,}
\tag{2.4}
\]

而额外提升是否发生只取决于 normalized cancellation

\[
\boxed{
4r_s\left(\frac d{p^h}\right)^2
-xy^2\frac{\Phi_s}{p^{2h}}
\equiv0\pmod p.
}
\tag{2.5}
\]

所以：

\[
\boxed{
\text{source excess 对 angle carrier 产生奇 valuation}
\Longrightarrow
v_p(d)=h
\text{ 且发生 normalized equal-depth cancellation}.}
\tag{2.6}
\]

这比旧 `p^h|D_src` 更明确：source pool 的 ordinary non-equal-depth 部分对 angle inert parity 完全是偶贡献。

---

## 3. `已严格完成`：f-line 的 exact Bézout depth law

从定义直接展开：

\[
\boxed{
(x+2)\Omega_{\rm sp}
-A_{\rm sp}F_f
=-200x^3\Delta_0.
}
\tag{3.1}
\]

这就是旧 resultant

\[
\operatorname{Res}_{r_s}(F_f,\Omega_{\rm sp})
=-200x^3\Delta_0
\]
的无除法版本。

设 genuine prime 同时接触 f-line 与 angle：

\[
p\mid F_f,
\qquad p\mid\Omega_{\rm sp}.
\]
旧一阶结论给

\[
p\mid\Delta_0.
\]

写

\[
e_f:=v_p(F_f),
\qquad
e_\Delta:=v_p(\Delta_0),
\qquad
e_\Omega:=v_p(\Omega_{\rm sp}).
\]

在 genuine f-contact 中

\[
p\nmid x(x+2)A_{\rm sp},
\]
所以 (3.1) 左右三个显式系数都是单位。

若

\[
e_f<e_\Delta,
\]
则右边两项 `A_sp F_f` 与 `200x^3 Delta_0` 深度不同，故

\[
\boxed{e_\Omega=e_f.}
\tag{3.2}
\]

若

\[
e_\Delta<e_f,
\]
则

\[
\boxed{e_\Omega=e_\Delta.}
\tag{3.3}
\]

若

\[
e_f=e_\Delta=e,
\]
则

\[
\boxed{e_\Omega\ge e,}
\tag{3.4}
\]
且只有 normalized cancellation

\[
A_{\rm sp}\frac{F_f}{p^e}
-200x^3\frac{\Delta_0}{p^e}
\equiv0\pmod p
\tag{3.5}
\]
才会使 angle depth 超过 `e`。

因此 compact 写成：

\[
\boxed{
\begin{aligned}
e_f\ne e_\Delta
&\Longrightarrow
v_p(\Omega_{\rm sp})=\min(e_f,e_\Delta),\\
e_f=e_\Delta
&\Longrightarrow
v_p(\Omega_{\rm sp})\ge e_f,
\end{aligned}}
\tag{3.6}
\]

并且只有第二行存在额外 lift。

---

## 4. `已严格完成`：q-line 也有同型 depth law

对 `Omega_sp` 关于 `x+2` 做 exact Euclidean division，可得到

\[
\boxed{
\Omega_{\rm sp}
=400r_s\Delta_0+(x+2)J_q,
}
\tag{4.1}
\]
其中

\[
\boxed{
\begin{aligned}
J_q={}&202500r_sx^3-405000r_sx^2
-99r_sxy^2-1800r_sxy\\
&+202r_sy^2+3600r_sy+2xy^2.
\end{aligned}}
\tag{4.2}
\]

q-denominator formula 为

\[
q=\frac{U(x+2)}{2c_Q},
\]
所以对 genuine q-prime，`U,2c_Q` 为单位且

\[
\boxed{v_p(q)=v_p(x+2).}
\tag{4.3}
\]

若 `p|q` 且 `p|Omega_sp`，旧 q-side resultant 重新给

\[
p\mid\Delta_0.
\]

现在关键是 `J_q` 在共同第一层根上为单位。由 `x=-2`：

\[
J_q(-2,y)
=4\left[100r_s(y^2+18y-8100)-y^2\right].
\]

而 `Delta_0(-2,y)=0` 等价于

\[
y^2+18y-8100=0.
\]
所以在共同根上

\[
\boxed{J_q\equiv-4y^2\not\equiv0\pmod p.}
\tag{4.4}
\]

写

\[
e_q:=v_p(q)=v_p(x+2),
\qquad
e_\Delta:=v_p(\Delta_0).
\]

由 (4.1)、(4.4)：

\[
\boxed{
\begin{aligned}
e_q\ne e_\Delta
&\Longrightarrow
v_p(\Omega_{\rm sp})=\min(e_q,e_\Delta),\\
e_q=e_\Delta
&\Longrightarrow
v_p(\Omega_{\rm sp})\ge e_q,
\end{aligned}}
\tag{4.5}
\]

而第二行的额外 lift 仍只能来自 normalized equal-depth cancellation。

---

## 5. 三类 overlap 的统一表

因此 genuine non-`3` inert overlap 有统一形态：

\[
\boxed{
\begin{array}{c|c|c|c}
\text{pool}&\text{depth 1}&\text{depth 2}&\text{angle depth away from equality}\\ \hline
\text{source}&2h&2e_d,\ e_d\ge h&2h\text{ (even)}\\
q&e_q&e_\Delta&\min(e_q,e_\Delta)\\
f&e_f&e_\Delta&\min(e_f,e_\Delta)
\end{array}}
\tag{5.1}
\]

所有“额外” angle depth 都只存在于

\[
\boxed{\text{equal-depth cancellation locus}.}
\tag{5.2}
\]

source pool 最强：普通非等深 source overlap 对 angle carrier 的 valuation 精确为 `2h`，完全不贡献 odd inert parity。

---

## 6. 对 `G_sp` parity dichotomy 的直接意义

`spontaneous-angle-parity.md` 定义

\[
G_{\rm sp}
=\gcd(\widehat{\mathcal O}_{\rm sp},\widehat{\mathcal T}_2),
\]
且如果

\[
G_{\rm sp}\equiv1\pmod4,
\]
angle residual quotient 必须携带一份 odd inert parity。

`spontaneous-angle-content.md` 已证明这份 parity 不能来自 `c_ug` source content。本文进一步证明：若它来自真正 source excess，则必须落在非常窄的

\[
\boxed{
v_p(d)=h\text{ 的 normalized equal-depth cancellation}}
\tag{6.1}
\]
层；所有 `v_p(d)>h` 的 source overlap 都只给偶 valuation。

q/f residual parity 同样不能来自普通“一个 contact 明显更浅”的情形之外的额外 lift；其未知自由度也被集中到 equal-depth loci。

所以接下来要逼

\[
G_{\rm sp}\equiv3\pmod4
\]
时，不再需要处理整个 source/q/f 参数空间，只需处理三个 equal-depth cancellation shell。特别是 source shell 已从无界二维 Hensel 接触缩成单个 normalized congruence (2.5)。

---

## 7. 当前开放项

本文没有证明 q/f 的 `min(e_*,e_Delta)` 自身一定为偶数，因此尚不能直接排除 denominator pool 对 residual odd parity 的贡献。

下一步最有价值的是：

1. 把 additive side 的 q/f **full saturation exponent** 与 (3.6)/(4.5) 对齐，看 denominator odd-excess 是否正好强迫 equal-depth；
2. 对 source equal-depth congruence (2.5)，利用 `Psi_9` / `D_src` 的第二 Hensel 条件求 normalized residue，尝试证明 cancellation 不发生或只能固定到有限素数；
3. 若三类 equal-depth shell 都被消掉，就会强迫 angle residual quotient `U≡1 mod4`，从而迫使 `G_sp≡3 mod4`。

---

<a id="source-spontaneous-angle-pair-cq-nogo"></a>

> 整合来源：`spontaneous-angle-pair-cq-nogo.md`

# A2 angle sign-pair 的 pure-`c_Q` unsaturated no-go

> **依赖：** `spontaneous-angle-pair-q0-depth.md`。
>
> **严格状态：**前一文件证明 pure `c_Q`-supported angle sign-pair common depth为 `min(v_p(Delta_0),2v_p(c_Q))`。本文证明不能仅靠 local `c_Q` geometry把 `v_p(Delta_0)` 强迫到完整 square depth `2v_p(c_Q)`：first-layer conic `x=-2,Delta_0=0` 对所有 genuine non-`3` inert primes均光滑，因而 unsaturated intermediate depth 是正常的 simple Hensel freedom。这个 no-go 阻止后续错误地从 `Q` 与 `b_3` 都含 `c_Q` 推出 angle pair gcd 自动 `1 mod 4`。本文不构造真实 global decimal solution，也不关闭 A2。

---

## 1. first-layer conic

对 pure `c_Q` prime `p`，前一文件给

\[
p\mid Q_0\Longrightarrow x=-2\pmod p,
\]

而 angle sign-pair common contact进一步要求

\[
\Delta_0(x,y)=2025x^2-18y-y^2=0\pmod p.
\]

所以

\[
\boxed{(y+9)^2=8181.}
\tag{1.1}
\]

其 partial derivatives 为

\[
\boxed{\partial_x\Delta_0=4050x,\qquad
\partial_y\Delta_0=-18-2y.}
\tag{1.2}
\]

在 `x=-2` 上

\[
\partial_x\Delta_0=-8100.
\]
对 genuine non-`3` inert prime `p`，`p\ne2,3,5`，故

\[
\boxed{\partial_x\Delta_0\not\equiv0\pmod p.}
\tag{1.3}
\]

同时若 `partial_y Delta_0=0`，则 `y=-9`，代入 (1.1) 会要求

\[
p\mid8181=3^4\cdot101.
\]
除 `3` 外只剩 `101=1 mod4`。因此 genuine non-`3` inert prime还满足

\[
\boxed{\partial_y\Delta_0\not\equiv0\pmod p.}
\tag{1.4}
\]

所以 pair-common conic在所有目标 inert primes上都是 smooth transverse curve。

---

## 2. why the `c_Q^2` cap does not force even depth

Write

\[
c:=v_p(c_Q)>0.
\]
For a pure `c_Q` prime, `q` is a unit and

\[
v_p(Q_0)=v_p(x+2)=c.
\]
The angle-pair depth law is

\[
\boxed{v_p(D_O)=\min\{v_p(\Delta_0),2c\}.}
\tag{2.1}
\]

One might hope that because `c_Q` occurs once in `Q` and once in `b_3`, every common pair contact automatically reaches `2c`. Equations (1.3)--(1.4) show why this is false locally.

Fix a first-layer root `(x_0,y_0)=(-2,y_0)`. Since `partial_y Delta_0` is a unit, the p-adic implicit-function theorem gives a unique smooth branch

\[
y=Y(x)
\]
with

\[
\Delta_0(x,Y(x))=0.
\]
For an actual `c_Q` displacement

\[
x=x_0+p^c\xi,
\qquad \xi\in\mathbf Z_p^\times,
\]
let `y_*:=Y(x)`. For any integer `d>=1`, perturb

\[
y=y_*+p^d\eta,
\qquad \eta\in\mathbf Z_p^\times.
\]
Taylor expansion gives

\[
\Delta_0(x,y)
=p^d\eta\,\partial_y\Delta_0(x,y_*)+O(p^{2d}).
\]
Because the derivative is a unit,

\[
\boxed{v_p(\Delta_0)=d.}
\tag{2.2}
\]

In particular every intermediate depth

\[
1\le d<2c
\]
is locally allowed. Choosing odd `d` gives an odd sign-pair common contribution through (2.1).

This is a local deformation statement only: the real decimal orbit may still fail to realize a chosen lift. But it proves that local algebra alone cannot upgrade the `2c` cap to a forced `2c` saturation.

---

## 3. consequence for global parity strategy

The pure `c_Q` part of `D_O` has the exact dichotomy:

\[
\boxed{
\begin{array}{c|c}
 v_p(\Delta_0)\ge2c & v_p(D_O)=2c\text{ (even)}\\
 v_p(\Delta_0)<2c & v_p(D_O)=v_p(\Delta_0)\text{ (simple unsaturated)}.
\end{array}}
\tag{3.1}
\]

The second row cannot be removed by another singular-discriminant audit: the underlying curve is smooth. Therefore a proof of

\[
D_O\equiv1\pmod4
\]
(if true) must use a global input such as decimal-orbit synchronization, natural representatives, or coupling to the additive/height ledger. It cannot follow merely from the square occurrence of `c_Q` in the third denominator data.

So the angle sign-pair common-gcd frontier is now exactly

\[
\boxed{\text{simple unsaturated }Q_0\text{-primary depth on }x=-2,\Delta_0=0.}
\]

---

<a id="source-spontaneous-angle-pair-q0-depth"></a>

> 整合来源：`spontaneous-angle-pair-q0-depth.md`

# A2 angle sign-pair common gcd 的 `Q_0` depth law

> **依赖：** `spontaneous-sign-companion-parity.md`、`spontaneous-angle-parity.md`、`spontaneous-denominator-depth-matrix.md`。
>
> **严格状态：**本文进一步压缩 actual/conjugate angle pair
> \(\widehat{\mathcal O}_+,\widehat{\mathcal O}_-\) 的共同 odd-inert support。先证明 non-`3,5` prime dividing `A=a_2` 不可能进入 angle carrier；因此 sign-pair common inert support从旧的 `A Q_0 c_Q` 精确缩到 `Q_0=c_Qq`。随后给出 `U_Omega` 的二阶 `Q`-adic identity，得到 pair-gcd 的完整 prime-power depth law：若 `e=v_p(Q_0)`、`c=v_p(c_Q)`，则共同 depth 恰为 `min(v_p(N^2 Delta_0),e+c)`。特别地 first layer 统一落在 `x=-2, Delta_0=0`，且所有 non-`3` inert roots均 simple。本文不证明该 common gcd 的总 mod-4 parity为偶，因此不关闭 A2。

---

## 1. 记号

固定 reflection endpoint：

\[
N=10^M,\qquad T=10^m,\qquad A=a_2,\qquad B=b_2,
\]

\[
Q=B+2N=2^{M+1}Q_0,
\qquad Q_0=c_Qq,
\]

\[
\mathcal U_\Omega=(45B^2-2AN)^2-A^2B(99B-4N),
\]

\[
\mathcal O_\pm=T\mathcal U_\Omega\pm2A^2Qb_3.
\]

primitive angle carriers are

\[
\widehat{\mathcal O}_\pm=\frac{\mathcal O_\pm}{2^{2M+m+2}},
\qquad
\widehat{\mathcal O}_\pm>0,
\qquad
\widehat{\mathcal O}_\pm\equiv3\pmod4.
\]

Define the integral prefix defect

\[
\boxed{
D_Q:=2025B^2-180AN-100A^2.
}
\tag{1.1}
\]

With

\[
x=B/N,\qquad y=10A/N,
\]
we have

\[
\boxed{D_Q=N^2\Delta_0,\qquad
\Delta_0=2025x^2-18y-y^2.}
\tag{1.2}
\]

---

## 2. `A=a_2` content cannot enter the genuine angle pair

Let `p` be an odd prime with

\[
p\mid A,\qquad p\notin\{3,5\}.
\]

Because `(A,B)=1`, one has `p\nmid B`. Modulo `p`,

\[
\mathcal U_\Omega\equiv(45B^2)^2\not\equiv0.
\]

Also the second term of `O_\pm` contains `A^2`, hence vanishes. Since `p\nmid T`,

\[
\boxed{
\mathcal O_\pm\equiv T(45B^2)^2\not\equiv0\pmod p.}
\tag{2.1}
\]

Therefore

\[
\boxed{
 p\mid A,\ p\notin\{3,5\}
 \Longrightarrow
 p\nmid\widehat{\mathcal O}_\pm.}
\tag{2.2}
\]

`spontaneous-sign-companion-parity.md` had already shown that any common odd prime of the two angle sheets divides

\[
A Q_0 5c_Qc_u.
\]

The angle-content lemma removes `c_u`, (2.2) removes `A`, and `c_Q\mid Q_0`. Thus for any genuine non-`3` inert common prime,

\[
\boxed{
 p\mid\gcd(\widehat{\mathcal O}_+,\widehat{\mathcal O}_-)
 \Longrightarrow p\mid Q_0.}
\tag{2.3}
\]

So the common sign-pair support is entirely `Q_0=c_Qq`-supported.

---

## 3. `U_Omega` 的 exact second-order `Q` bridge

A direct expansion gives the stronger identity

\[
\boxed{
\begin{aligned}
\mathcal U_\Omega
={}&-4N(B+N)D_Q\\
&-9Q^2(11A^2+20AN-225B^2).
\end{aligned}}
\tag{3.1}
\]

Hence

\[
\boxed{
\begin{aligned}
\mathcal O_\pm
={}&-4TN(B+N)D_Q\\
&+Q\Bigl[
-9TQ(11A^2+20AN-225B^2)
\pm2A^2b_3
\Bigr].
\end{aligned}}
\tag{3.2}
\]

This is the natural sign-pair analogue of the denominator depth bridges: the first term reads the pure prefix defect, while every sign-dependent term is pushed into a higher `Q/b_3` depth.

---

## 4. complete prime-power depth law

Fix a genuine odd inert prime `p` with

\[
p\mid Q_0.
\]

Write

\[
e:=v_p(Q_0)>0,
\qquad
c:=v_p(c_Q)\ge0.
\tag{4.1}
\]

Since

\[
Q=2^{M+1}Q_0,
\qquad
b_3=2^{M+m+1}5^dc_Qc_u,
\]
and `p\nmid2\cdot5\cdot c_u`,

\[
\boxed{v_p(Q)=e,\qquad v_p(b_3)=c.}
\tag{4.2}
\]

Because `p|Q`,

\[
B\equiv-2N\pmod p,
\]
so

\[
B+N\equiv-N\not\equiv0\pmod p.
\]
Thus the coefficient

\[
-4TN(B+N)
\]
is a `p`-adic unit.

The bracketed correction in (3.2) has valuation at least `c`, since its first term has depth `e>=c` and its second term has depth exactly `c`. Therefore the whole correction term is divisible by

\[
p^{e+c}.
\]
Consequently

\[
\boxed{
\mathcal O_\pm
\equiv
-4TN(B+N)D_Q
\pmod{p^{e+c}}.}
\tag{4.3}
\]

Moreover

\[
\mathcal O_+-\mathcal O_-=4A^2Qb_3,
\]
and (2.2) gives `p\nmid A`; hence

\[
\boxed{
v_p(\mathcal O_+-\mathcal O_-)=e+c.}
\tag{4.4}
\]

Let

\[
d_O(p):=\min\{v_p(\mathcal O_+),v_p(\mathcal O_-)\}.
\]
If `v_p(D_Q)<e+c`, (4.3) makes both angle valuations exactly `v_p(D_Q)`. If `v_p(D_Q)>=e+c`, (4.3) makes both at least `e+c`, while (4.4) prevents both from exceeding `e+c`. Therefore

\[
\boxed{
 d_O(p)=\min\{v_p(D_Q),e+c\}.}
\tag{4.5}
\]

Since primitive normalization removes only a power of `2`, the same formula holds for the primitive pair gcd:

\[
\boxed{
 v_p\!\left(
 \gcd(\widehat{\mathcal O}_+,\widehat{\mathcal O}_-)
 \right)
 =
 \min\{v_p(N^2\Delta_0),\ v_p(Q_0)+v_p(c_Q)\}.}
\tag{4.6}
\]

Because `p\nmid N`, this can be written simply as

\[
\boxed{
 v_p(D_O)
 =
 \min\{v_p(\Delta_0),\ v_p(q)+2v_p(c_Q)\}.}
\tag{4.7}
\]

Here `D_O=gcd(widehat(O)_+,widehat(O)_-)`.

Two useful special cases are immediate:

### q-supported prime, `p\nmid c_Q`

If `p^e||q`, then `c=0` and

\[
\boxed{v_p(D_O)=\min\{v_p(\Delta_0),e\}.}
\tag{4.8q}
\]

This exactly matches the existing q-denominator angle depth law.

### pure `c_Q`-supported prime, `p\nmid q`

If `p^c||c_Q`, then `e=c`, hence

\[
\boxed{v_p(D_O)=\min\{v_p(\Delta_0),2c\}.}
\tag{4.8c}
\]

Thus a fully saturated pure-`c_Q` sign-pair contribution has even depth `2c`; odd parity from `c_Q` can only occur in an **unsaturated** prefix contact `v_p(Delta_0)<2c`.

---

## 5. first-layer geometry is a single simple conic

From `p|Q_0` one has

\[
Q=N(x+2)\equiv0\pmod p,
\]
so

\[
\boxed{x\equiv-2\pmod p.}
\tag{5.1}
\]

If the prime also divides the angle sign-pair gcd, then (4.6) gives

\[
\Delta_0\equiv0\pmod p.
\]
At `x=-2`,

\[
\Delta_0(-2,y)
=8100-18y-y^2,
\]
so equivalently

\[
\boxed{(y+9)^2=8181=3^4\cdot101.}
\tag{5.2}
\]

The discriminant of the quadratic in `y` is

\[
18^2+4\cdot8100
=324\cdot101.
\tag{5.3}
\]

The only odd ramified prime apart from `3` is

\[
101\equiv1\pmod4.
\]
Therefore

\[
\boxed{
\text{every genuine non-`3` inert angle-sign common first-layer root is simple.}}
\tag{5.4}
\]

In particular the sign-pair gcd has no new inert singular Hensel tree. Its only remaining freedom is the simple prime-power depth in (4.7).

---

## 6. update to the global parity ledger

The old support statement

\[
\operatorname{Supp}_{3\bmod4}(D_O)
\subseteq\operatorname{Supp}(A Q_0c_Q)
\]
can now be replaced by the strictly sharper valuation statement

\[
\boxed{
\operatorname{Supp}_{3\bmod4}(D_O)
\subseteq\operatorname{Supp}(Q_0),
}
\]

\[
\boxed{
 v_p(D_O)
 =
 \min\{v_p(\Delta_0),v_p(q)+2v_p(c_Q)\}.
}
\tag{6.1}
\]

So the actual/conjugate angle pair can share inert parity only through the same q-type prefix conic `x=-2, Delta_0=0`. The `a_2` content source disappears completely, and pure `c_Q` contribution is parity-even once it reaches its full square depth `2v_p(c_Q)`.

This still does not prove `D_O=1 mod4`: an unsaturated simple `Delta_0` contact may stop at odd depth. The remaining task is therefore no longer a content classification problem; it is a **simple unsaturated depth synchronization problem on a single conic**.

---

<a id="source-spontaneous-angle-parity"></a>

> 整合来源：`spontaneous-angle-parity.md`

# A2 spontaneous angle 的 primitive `3 mod 4` carrier

> **依赖：** `spontaneous-prefix-eliminant.md`、`spontaneous-angle.md`、`primitive-reduction.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文把 `Omega_sp` 的原始 integer numerator 做精确 `2`-进本原化。结论是它与 `Theta_dec` 具有完全相同的 `2`-adic depth `2M+m+2`，并且两者除去该尺度后都严格为 `3 mod 4` 的正奇整数。因此 spontaneous angle 侧自身也携带一个全局 odd-inert parity excess。本文只建立 parity carrier 与后续 gcd dichotomy，不宣称这已经关闭 spontaneous common-prime channel，也不宣称 A2 全局关闭。

---

## 1. `Omega_sp` 的原始整数 numerator

沿用

\[
N=10^M,
\qquad A=a_2,
\qquad B=b_2,
\]

\[
Q=2N+B,
\qquad T=10^m.
\]

`spontaneous-prefix-eliminant.md` 定义

\[
\boxed{
\mathcal U_\Omega
=(45B^2-2AN)^2-A^2B(99B-4N).
}
\tag{1.1}
\]

并证明

\[
\boxed{
\Omega_{\rm sp}
=\frac{100B}{b_3N^4}
\left(T\mathcal U_\Omega+2A^2Qb_3\right).
}
\tag{1.2}
\]

因此定义

\[
\boxed{
\mathcal O_{\rm sp}
:=T\mathcal U_\Omega+2A^2Qb_3.
}
\tag{1.3}
\]

在真实 endpoint 中 `Omega_sp>0`，而 (1.2) 的 prefactor 为正，所以

\[
\boxed{\mathcal O_{\rm sp}>0.}
\tag{1.4}
\]

对 genuine odd spontaneous prime `p∤10Bb_3`，`p`-adic valuation 也无损：

\[
\boxed{
v_p(\Omega_{\rm sp})=v_p(\mathcal O_{\rm sp}).}
\tag{1.5}
\]

---

## 2. deep-even 的精确 `2`-进尺度

已有

\[
B=2^{M+m+1}c_ug,
\tag{2.1}
\]

\[
Q=2^{M+1}Q_0,
\qquad Q_0=c_Qq\ \text{odd},
\tag{2.2}
\]

\[
b_3=2^{M+m+1}5^dc_Qc_u.
\tag{2.3}
\]

把 odd parts 记为

\[
b_0:=c_ug,
\qquad
b_{30}:=5^dc_Qc_u.
\]

所以

\[
B=2^{M+m+1}b_0,
\qquad
b_3=2^{M+m+1}b_{30},
\]
且 `b_0,b_30,Q_0` 均为奇数。

又因 `(A,B)=1` 且 `B` 偶，故

\[
\boxed{A\text{ odd}.}
\tag{2.4}
\]

---

## 3. `U_Omega` 的 primitive quotient 恒为 `1 mod 4`

先处理第一平方项。因为

\[
N=2^M5^M,
\]
有

\[
\frac{45B^2-2AN}{2^{M+1}}
=45\,2^{M+2m+1}b_0^2-A5^M.
\tag{3.1}
\]

第一项被 `4` 整除，第二项为奇数，所以 (3.1) 是奇数；其平方满足

\[
\left(
\frac{45B^2-2AN}{2^{M+1}}
\right)^2
\equiv1\pmod8.
\tag{3.2}
\]

另一方面

\[
99B-4N
=2^{M+2}
\left(99\,2^{m-1}b_0-5^M\right),
\]
所以

\[
\boxed{
\frac{B(99B-4N)}{2^{2M+2}}
=2^{m+1}b_0
\left(99\,2^{m-1}b_0-5^M\right).
}
\tag{3.3}
\]

因为 `m>=1`，右边被 `4` 整除。于是

\[
\boxed{
\mathcal U_\Omega^
sharp
:=\frac{\mathcal U_\Omega}{2^{2M+2}}
\in\mathbf Z,
\qquad
\mathcal U_\Omega^\sharp\equiv1\pmod4.
}
\tag{3.4}
\]

特别地

\[
\boxed{v_2(\mathcal U_\Omega)=2M+2.}
\tag{3.5}
\]

---

## 4. `已严格完成`：`O_sp` 与 `Theta_dec` 有同一 `2`-adic depth

将 (3.4) 代入 (1.3)，除去

\[
2^{2M+m+2}.
\]

第一项给

\[
\frac{T\mathcal U_\Omega}{2^{2M+m+2}}
=5^m\mathcal U_\Omega^\sharp.
\tag{4.1}
\]

第二项利用 (2.2)–(2.3)：

\[
\frac{2A^2Qb_3}{2^{2M+m+2}}
=2A^2Q_0b_{30}.
\tag{4.2}
\]

因此定义

\[
\boxed{
\widehat{\mathcal O}_{\rm sp}
:=\frac{\mathcal O_{\rm sp}}{2^{2M+m+2}}
=5^m\mathcal U_\Omega^\sharp
+2A^2Q_0b_{30}.
}
\tag{4.3}
\]

第一项模 `4` 为 `1`，第二项因 `A,Q_0,b_30` 都奇而模 `4` 为 `2`。故

\[
\boxed{
\widehat{\mathcal O}_{\rm sp}
\equiv3\pmod4.
}
\tag{4.4}
\]

所以它是奇数，并且

\[
\boxed{
v_2(\mathcal O_{\rm sp})=2M+m+2.}
\tag{4.5}
\]

另一方面已有

\[
\Theta_{\rm dec}
=2^{2M+m+2}\widehat{\mathcal T}_2,
\qquad
\widehat{\mathcal T}_2\equiv3\pmod4.
\tag{4.6}
\]

综上：

\[
\boxed{
\begin{array}{c|c|c}
&v_2&\text{primitive mod }4\\ \hline
\mathcal O_{\rm sp}&2M+m+2&3\\
\Theta_{\rm dec}&2M+m+2&3
\end{array}}
\tag{4.7}
\]

这两个此前来自完全不同推导的对象，在 `2`-adic orientation 上精确对齐。

---

## 5. 两侧都存在 odd inert parity excess

由 (1.4)、(4.4)：

\[
\widehat{\mathcal O}_{\rm sp}>0,
\qquad
\widehat{\mathcal O}_{\rm sp}\equiv3\pmod4.
\]
所以

\[
\boxed{
\sum_{p\equiv3\ (4)}
v_p(\widehat{\mathcal O}_{\rm sp})
\equiv1\pmod2.
}
\tag{5.1}
\]

旧 additive cofactor 同样满足

\[
\boxed{
\sum_{p\equiv3\ (4)}
v_p(\widehat{\mathcal T}_2)
\equiv1\pmod2.
}
\tag{5.2}
\]

因此 spontaneous angle side 与 additive side 各自都强迫一份 odd inert excess，而真正 common spontaneous carrier 属于

\[
\gcd(\widehat{\mathcal O}_{\rm sp},\widehat{\mathcal T}_2).
\]

---

## 6. `已严格完成`：common-gcd 的 mod-4 parity dichotomy

令

\[
G_{\rm sp}:=\gcd(
\widehat{\mathcal O}_{\rm sp},
\widehat{\mathcal T}_2
),
\]
并写

\[
\widehat{\mathcal O}_{\rm sp}=G_{\rm sp}U,
\qquad
\widehat{\mathcal T}_2=G_{\rm sp}V,
\qquad
\gcd(U,V)=1.
\]

三个量都为正奇数。因为两侧都 `3 mod4`：

- 若 `G_sp≡3 mod4`，则 `U≡V≡1 mod4`；common gcd 本身携带 odd inert parity；
- 若 `G_sp≡1 mod4`，则 `U≡V≡3 mod4`；两侧各自仍需一份**互不相同**的 residual odd inert excess。

即

\[
\boxed{
\begin{array}{c|c}
G_{\rm sp}\bmod4&\text{forced parity allocation}\\ \hline
3&\text{common spontaneous gcd carries odd inert parity}\\
1&\text{both coprime quotients carry separate odd inert parity.}
\end{array}}
\tag{6.1}
\]

这不是 closure，但把“是否存在共同 spontaneous excess”升级成一个全局 parity dichotomy；后续 prime-source 分类可分别攻击 `G_sp≡3` 与 `G_sp≡1` 两支。

---

## 7. 更新后的开放方向

本文件新增的不是又一个 Legendre symbol，而是一份真正的全局 primitive integer：

\[
\boxed{
\widehat{\mathcal O}_{\rm sp}>0,
\qquad
\widehat{\mathcal O}_{\rm sp}\equiv3\pmod4.
}
\]

下一步最值得做的是把已知 source/q/f overlap resultants 用在 (6.1) 的 residual quotients 上：如果能证明 `U` 或 `V` 的 non-`3` inert odd factors只能来自已经排除/固定的 denominator-source pools，就会强迫 `G_sp≡3 mod4`，从而得到真正的 common spontaneous inert carrier，而不再只是“某一侧必有一个 inert prime”。

---

<a id="source-spontaneous-angle"></a>

> 整合来源：`spontaneous-angle.md`

# A2 spontaneous-angle master polynomial

> **依赖：** `core.md` §§14.1–15、`phase-and-defect.md` §§1.1–1.6、`height-cofactor.md`、`decimal-prefix-bridge.md`。
>
> **严格状态：**本文补上旧 §14.2-III 一直缺失的“第二 angle polynomial”。它把 `E_1` 的 spontaneous contact 变成关于 source-normalized ratio 的一个显式一次式，并用三个小 resultant 精确恢复 source / q-side / f-side 的旧边界。另给出 `\widehat{\mathcal T}_2` 的全局 pure-decimal carrier polynomial。本文仍**不宣称 A2 全局关闭**。

---

## 1. 避免 `z` 重名的统一记号

当前只处理 reflection endpoint，故

\[
a_1=9,\qquad \sigma_5=0,\qquad E_5=\lambda.
\]

沿用

\[
M=m_2,\qquad T=10^m,
\]

\[
x=\frac{b_2}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}}.
\]

`phase-and-defect.md` 原来把 source-normalized ratio 也记为 `z`；而后续 `source-discriminant.md` 已用 `z=q5^\lambda`。为避免混淆，本文把前者改记为

\[
\boxed{
r_s:=\frac{5^\lambda D_0}{c_Q}.}
\tag{1.1}
\]

于是 phase Hensel 线为

\[
\boxed{
\Phi_s(x,r_s)
=(99x-4)r_s-2x-4.
}
\tag{1.2}
\]

并有

\[
q=\frac{U(x+2)}{2c_Q},
\qquad
f=\frac{U}{2D_0}\bigl(r_s(x+2)+2x\bigr),
\qquad U=5^M.
\tag{1.3}
\]

令

\[
\Sigma=c_Q^2qf,
\qquad
\mathfrak n=2c_u\sigma
\tag{1.4}
\]

为 core §14.2 的 denominator/source 两个尺度。`phase-and-defect.md` 已证明

\[
\boxed{
\frac{\mathfrak n}{\Sigma}
=
\frac{x\Phi_s(x,r_s)}
{(x+2)\bigl(r_s(x+2)+2x\bigr)}.
}
\tag{1.5}
\]

---

## 2. `已严格完成`：`E_1` 恰由一个一次 angle polynomial 控制

`hensel.md` 恢复的旧第二层精确式是

\[
\boxed{
E_1=5^\lambda L_0^2-\mathfrak n a_2^2.
}
\tag{2.1}
\]

在当前 `a_1=9` endpoint，

\[
L_0=-U10^{M-1}(225x^2-y),
\qquad
a_2=y10^{M-1}.
\tag{2.2}
\]

另一方面由 (1.3)，

\[
\Sigma
=
\frac{c_QU^2}{4D_0}
(x+2)\bigl(r_s(x+2)+2x\bigr).
\tag{2.3}
\]

所以

\[
\frac{5^\lambda L_0^2}{\Sigma a_2^2}
=
\frac{4r_s(225x^2-y)^2}
{y^2(x+2)\bigl(r_s(x+2)+2x\bigr)}.
\tag{2.4}
\]

与 (1.5) 相减，得到真正缺失的 spontaneous angle polynomial：

\[
\boxed{
\Omega_{\rm sp}(x,y,r_s)
:=
4r_s(225x^2-y)^2
-xy^2\Phi_s(x,r_s).
}
\tag{2.5}
\]

并且不是只有模素数关系，而是精确有理恒等式

\[
\boxed{
\frac{E_1}{\Sigma a_2^2}
=
\frac{\Omega_{\rm sp}}
{y^2(x+2)\bigl(r_s(x+2)+2x\bigr)}.
}
\tag{2.6}
\]

因此对于与 `2,3,5,c_Q,q,f,\mathfrak n,\mathcal N_0` 分离的 genuine non-`3` spontaneous inert prime，`a_2` 也是单位，故

\[
\boxed{
p\mid E_1\iff p\mid\Omega_{\rm sp}.}
\tag{2.7}
\]

这补上了 `hensel.md` 末尾“为 spontaneous angle excess 寻找第二个角度多项式”的开放项。

---

## 3. `已严格完成`：spontaneous root 是唯一的一次 Hensel root

写

\[
d_s:=225x^2-y.
\]

(2.5) 关于 `r_s` 只有一次：

\[
\boxed{
\Omega_{\rm sp}
=A_{\rm sp}(x,y)r_s
+2xy^2(x+2),
}
\tag{3.1}
\]

其中

\[
\boxed{
A_{\rm sp}(x,y)
=4d_s^2-xy^2(99x-4).
}
\tag{3.2}
\]

在真正 spontaneous prime 上若
`p\nmid2xy(x+2)`，则 `p\mid\Omega_sp` 自动强迫 `A_sp` 为单位；否则常数项也必须为零，矛盾。因此

\[
\boxed{
r_s\equiv
-\frac{2xy^2(x+2)}{A_{\rm sp}(x,y)}
\pmod p.}
\tag{3.3}
\]

所以 spontaneous channel 不是新的高维 Hensel 树：在第一层分离假设下，它只有一个 source-ratio root，之后的 prime-power lift 也是唯一的一维 lift，除非另有固定 bad-reduction prime 使分离条件失效。

---

## 4. `已严格完成`：真实 endpoint window 中 `Omega_sp` 严格远离零

当前危险 endpoint 已有

\[
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1,
\qquad r_s>0.
\tag{4.1}
\]

因此

\[
d_s=225x^2-y>\frac94-1=\frac54.
\]

同时 `x(99x-4)` 在该区间递增，所以

\[
xy^2(99x-4)
<x(99x-4)
<\frac{244}{361}.
\]

故

\[
\boxed{
A_{\rm sp}
>\frac{25}{4}-\frac{244}{361}
=\frac{8049}{1444}>5.
}
\tag{4.2}
\]

从而

\[
\boxed{
\Omega_{\rm sp}
>\frac{8049}{1444}r_s>0.
}
\tag{4.3}
\]

结合 (2.6)，还重新得到一个严格的 endpoint 实数结论：

\[
\boxed{E_1>0.}
\tag{4.4}
\]

注意这不是模 `p` 排除；它的用途是说明 spontaneous congruence 的真实一次根在实轴上位于负侧，而实际 `r_s` 为正。若要把该符号错位升级成空性，仍需要 prime-power modulus / natural representative 的高度输入。

---

## 5. `已严格完成`：三个小 resultant 把旧 prime-source 图接成一张图

定义归一化 prefix defect

\[
\boxed{
\Delta_0(x,y)
:=2025x^2-18y-y^2
=\frac{\Delta_{\rm pref}}{10^{2M-2}}.
}
\tag{5.1}
\]

### 5.1 source line

直接对 `r_s` 求 resultant：

\[
\boxed{
\operatorname{Res}_{r_s}
(\Phi_s,\Omega_{\rm sp})
=
8(x+2)(225x^2-y)^2.
}
\tag{5.2}
\]

因此 source Hensel line 与 spontaneous line 的交点，在与 q-side 分离后只能回到

\[
225x^2-y,
\]

也就是 `hensel.md` 的 `D_src/L_0` 半深度 contact。没有第四种 source/spontaneous overlap。

### 5.2 f-side denominator line

令

\[
F_f:=r_s(x+2)+2x.
\]

则

\[
\boxed{
\operatorname{Res}_{r_s}
(F_f,\Omega_{\rm sp})
=-200x^3\Delta_0(x,y).
}
\tag{5.3}
\]

所以 f-denominator 与 spontaneous angle 的交点恰好就是旧 prefix-defect contact。

### 5.3 q-side denominator line

q-side 在 scale-free 坐标中由 `x+2=0` 表示。直接代入：

\[
\boxed{
\Omega_{\rm sp}(-2,y,r_s)
=400r_s\Delta_0(-2,y).
}
\tag{5.4}
\]

所以 q-side 同样只回到同一个 `Delta_pref`。

综上，旧 §14.2 的三类来源现在不是三套散乱条件：

\[
\boxed{
\begin{array}{ccl}
\text{source}&\longleftrightarrow&\Phi_s,\\
\text{denominator}&\longleftrightarrow&x+2\text{ 或 }F_f,\\
\text{spontaneous}&\longleftrightarrow&\Omega_{\rm sp},
\end{array}}
\]

而它们两两相交时只产生既有的 `D_src` 或 `Delta_pref`，没有新的未命名 prime pool。

---

## 6. `已严格完成 / 审计`：与 external double-root 的 resultant 只恢复 `sqrt(55)` gate

`source-discriminant.md` 使用的 source ratio

\[
r=\frac{5^\lambda2^mg}{c_Q}
\]

与本文 `r_s` 相同，因为 reflection 中 `D_0=2^mg`。external double-root 的 discriminant line 因而是

\[
\boxed{
\Gamma_W(x,r_s)
:=55r_s^2(x+2)^2-49x^2.
}
\tag{6.1}
\]

记 `A_sp` 如 (3.2)。消去 `r_s` 得

\[
\boxed{
\operatorname{Res}_{r_s}
(\Omega_{\rm sp},\Gamma_W)
=
x^2\left[
220y^4(x+2)^4-49A_{\rm sp}^2
\right].
}
\tag{6.2}
\]

所以在所有相关量均为单位时，再次得到

\[
\left(\frac{55}{p}\right)=1.
\]

这与 `source-discriminant.md` 的 double-root character 相同，因而 (6.2) **不应被重复收费成第二个 quadratic obstruction**。它的真正价值是：spontaneous/external overlap 现在也有了一个明确的二变量 resultant，可与 prefix/length 条件继续消元。

---

## 7. `已严格完成`：所有 odd cofactor carrier 都有一个 pure-decimal 二次接口

`endpoint-lattice.md` 的

\[
\widehat{\mathcal T}_2
=
2^mc_u^2g^2\mathscr S_0
-Q_0^2 5^{2\lambda-d}XY
\]

可完全乘回原始 decimal blocks。利用

\[
b_2=2^{M+m+1}c_ug,
\qquad
Q=2^{M+1}Q_0,
\qquad
N_0=5^{\lambda-2d}XY,
\qquad
m=\lambda+d,
\]

得到

\[
\boxed{
\Theta_{\rm dec}
:=b_2^2\mathscr S_0-TQ^2N_0
=2^{2M+m+2}\widehat{\mathcal T}_2.
}
\tag{7.1}
\]

所以 `\widehat{T}_2` 的**全部奇素数支持**，不仅 common-height / denominator 子通道，都等价于纯 decimal quadratic

\[
\Theta_{\rm dec}(K)\equiv0.
\]

又因为

\[
\mathscr S_0
=T(K^2-26)-(2K-9)(2a_3+9T),
\]

以及

\[
\Psi_f=b_2^2(K^2-26)-Q^2N_0,
\]

有

\[
\boxed{
\Theta_{\rm dec}
=T\Psi_f
-b_2^2(2K-9)(2a_3+9T).
}
\tag{7.2}
\]

若再写

\[
\alpha=TK+a_3,
\qquad
F_W(K)=5K^2-36K+55,
\]

则

\[
2a_3+9T=2\alpha-T(2K-9)
\]

给出第二种精确形态

\[
\boxed{
\Theta_{\rm dec}
=T\Phi_H
-2b_2^2(2K-9)\alpha,
}
\tag{7.3}
\]

其中

\[
\boxed{
\Phi_H
:=b_2^2F_W(K)-Q^2N_0.
}
\tag{7.4}
\]

因此任意 odd carrier 与 concatenated numerator `alpha` 的公共部分已经被单个 pure-prefix polynomial `Phi_H` 控制。结合

\[
\alpha=\omega W_q,
\]

common-`alpha` channel 随后严格分成 `W_q` height 与 `omega` content 两类；而真正 `p\nmid\alpha` 的 carrier 才是必须继续由 `Omega_sp / Theta_dec` 联立处理的 pure spontaneous angle channel。

---

## 8. 更新后的开放核

本轮没有证明 spontaneous channel 为空，但把旧的“未知第二角度多项式”问题改写为下面两个明确的一次/二次对象：

\[
\boxed{
\Omega_{\rm sp}(x,y,r_s)=0,
\qquad
\Theta_{\rm dec}(K)=0.
}
\]

并且：

1. `Omega_sp` 与 source line 的 resultant 只回到 `D_src`；
2. 与 q/f denominator line 的 resultant 只回到 `Delta_pref`；
3. 与 external double-root 的 resultant 只回到既有 `sqrt(55)` gate；
4. `Theta_dec` 覆盖 `widehat(T)_2` 的全部 odd support，消除了“只分析 common-height prime 是否遗漏真正 spontaneous carrier”的记号缺口。

下一步真正值得做的是：把 `Omega_sp` 与 `Theta_dec` 通过 third-block exact plane / finite-defect shell 消去 `r_s,a_3`，而不是继续添加 Legendre character。

---

<a id="source-spontaneous-bad-primes"></a>

> 整合来源：`spontaneous-bad-primes.md`

# A2 spontaneous length bad-prime audit

> **依赖：** `spontaneous-angle.md`、`length-orbit.md`。
>
> **严格状态：**本文只审计 fully coupled spontaneous/external 系统的 **singular / bad-reduction Hensel gates**。两个 fixed octic 的整数判别式给出有限候选；逐个代回 discriminant character、decimal multiplicative orbit、原三方程和二阶 Hensel compatibility 后，没有任何 genuine singular Hensel tree survives。generic/simple local branches仍可能存在，所以本文**不宣称 A2 全局关闭**。

---

## 1. 两个 octic 的 discriminant

沿用 `length-orbit.md`

\[
\mathcal P_1(s),\qquad\mathcal P_2(s).
\]

精确判别式分解为

\[
\boxed{
\begin{aligned}
\operatorname{Disc}(\mathcal P_1)
={}&2^{88}3^{75}5^{38}7^{12}11^{28}13^4 23^4 89^2 101^4\\
&\cdot181^2 367^2\cdot102251\cdot630451\cdot136776907\\
&\cdot74218718085901254661^2,
\end{aligned}}
\tag{1.1}
\]

\[
\boxed{
\begin{aligned}
\operatorname{Disc}(\mathcal P_2)
={}&2^{88}3^{101}5^{38}7^{24}11^{28}13^4 19^6 67^2 101^4 281^2\\
&\cdot8971\cdot5019481^2\cdot3833513^2\\
&\cdot833453052690874208617\\
&\cdot115850970866446584757213999^2.
\end{aligned}}
\tag{1.2}
\]

对 genuine non-`3` inert external prime，还必须有

\[
\left(\frac{55}{p}\right)=1,
\qquad p\nmid 2\cdot3\cdot5\cdot7\cdot11.
\tag{1.3}
\]

所以大部分 discriminant support 立即失去资格。下面只审计仍可能在 `F_p` 上产生 genuine bad root 的项。

---

## 2. `P_1`：三个移动 bad roots 中只有两个进入 decimal orbit，而二者都死在 `p^2`

### 2.1 `p=23`

`gcd(P_1,P_1')` 模 `23` 为

\[
s^2-3s+11.
\]

其判别式为 `11`，而

\[
\left(\frac{11}{23}\right)=-1.
\]

所以没有 `F_23` repeated length root。

### 2.2 `p=367`

唯一 repeated root 是

\[
s=0,
\]

但真实

\[
s=36\cdot10^{M-1}
\]

永远是单位，故排除。

### 2.3 `p=136776907`

唯一 repeated root 是

\[
s=8516046.
\]

这里

\[
\operatorname{ord}_p(10)=7598717,
\qquad [\mathbf F_p^\times:\langle10\rangle]=18.
\]

直接检查

\[
\left(8516046\cdot36^{-1}\right)^{7598717}
\not\equiv1\pmod p,
\]

所以该 root 不在 `36<10>` decimal orbit 中，排除。

### 2.4 `p=102251`

唯一 repeated length root

\[
s=81690
\]
确实在 decimal orbit 中。代回 `N_sp=R_spD=0` 后只有

\[
x=61220,
\qquad y=95782,
\qquad r_s=84227.
\]

它满足 q/f/source 分离条件，是 genuine 第一层解。但三方程

\[
(N_{sp},O_{sp},G_{sp})
\]
关于 `(s,x,r_s)` 的 Jacobian rank 为 `2`。写一次 Hensel 提升

\[
J\delta\equiv-\frac{F(s,x,r_s)}p\pmod p,
\]

右端不在 `J` 的像中，因此

\[
\boxed{\text{该解没有模 }102251^2\text{ 的提升}.}
\tag{2.1}
\]

### 2.5 `p=630451`

同理，repeated root

\[
s=271429
\]
在 decimal orbit 中，并恢复唯一第一层 genuine 解

\[
x=340435,
\quad y=610253,
\quad r_s=204669.
\]

Jacobian rank 同样为 `2`，二阶 Hensel compatibility 无解：

\[
\boxed{\text{不存在模 }630451^2\text{ 的提升}.}
\tag{2.2}
\]

所以 `P_1` 不留下任何 genuine singular p-adic tree。

---

## 3. `P_2`：`19` 的 bad root 非 genuine，`8971` 死在二阶，`67` 实际 nonsingular

### 3.1 `p=19`

`P_2` 的 repeated eliminant root 是

\[
s=-3\equiv16\pmod{19}.
\]

代回 `N_sp,R_spD` 的公共根只有

\[
x=0,
\]

与真实 denominator unit 条件矛盾。因此这不是 `length-orbit.md` 的 genuine `s=2` branch；后者本来就是 simple root。

### 3.2 `p=8971`

唯一 repeated root

\[
s=6356
\]
进入 decimal orbit，并恢复第一层 genuine 解

\[
x=2914,
\quad y=6787,
\quad r_s=7633.
\]

但 Jacobian rank 为 `2`，二阶 compatibility 再次失败：

\[
\boxed{\text{不存在模 }8971^2\text{ 的提升}.}
\tag{3.1}
\]

### 3.3 `p=67`

repeated length root 为

\[
s=17.
\]

它位于 decimal orbit：

\[
\operatorname{ord}_{67}(10)=33,
\qquad
36\cdot10^{32}\equiv17\pmod{67},
\]

所以

\[
M\equiv0\pmod{33}.
\]

原三方程恢复两组 genuine 解：

\[
\boxed{
(s,x,y,r_s)
=(17,53,35,63),
\quad
(17,37,35,57)
\pmod{67}.}
\tag{3.2}
\]

它们的 Jacobian determinants 分别为

\[
\boxed{32,\quad49\pmod{67},}
\tag{3.3}
\]

都非零。因此 `67` 虽是 **eliminant repeated root**，但原三方程本身完全 nonsingular；两组解各自只有一条唯一 Hensel lift。

其余 `3 mod 4` discriminant candidate 中，`7` 与巨素数

\[
115850970866446584757213999
\]
均满足

\[
\left(\frac{55}{p}\right)=-1,
\]

而 `11` 为被分离的固定 coefficient prime，故不能进入 genuine external discriminant-zero。

---

## 4. `已严格完成`：genuine singular Hensel gate 已清空

综合 §§2–3：

\[
\boxed{
\text{fully coupled spontaneous/external 系统没有 surviving genuine singular Hensel tree}.}
\tag{4.1}
\]

精确地说：

- `23`：无 `F_p` repeated root；
- `367`：只有非单位 root；
- `136776907`：root 不在 decimal orbit；
- `102251,630451,8971`：genuine 第一层解存在，但没有 `p^2` lift；
- `19` 的 repeated eliminant root：只给 `x=0`；
- `67`：两组 genuine 解，但 full Jacobian 非零，所以各自唯一提升。

因此后续不再需要为“moving singular Hensel branching”保留一个开放素数族。所有 genuine surviving local channel 都是**simple / unique lift**。

这仍不是全局空性：simple branches 可以存在到任意 p-adic depth。下一步必须使用 `C` 的自然代表、secant additive CRT、`W_q` parity 或 Archimedean size 来排除这些唯一分支，而不是继续审计 polynomial discriminant。

---

<a id="source-spontaneous-companion-common-parity-dichotomy"></a>

> 整合来源：`spontaneous-companion-common-parity-dichotomy.md`

# A2 `J^circ/B^circ` companion parity 的 canonical common-gcd dichotomy

> **依赖：** `spontaneous-height-resultant-parity.md`、`spontaneous-height-companion-cross.md`、`spontaneous-height-content-oversaturation.md`、`spontaneous-height-equal-depth-target-selector.md`。
>
> **严格状态：**`J^circ` 与 `B^circ` 是约去完整 height gcd `D_H` 后的两个 positive companion residual。本文用 `G_JB=gcd(J^circ,B^circ)` 统一审计它们的 odd-inert parity：当 parent orientation 为 `3 mod4` 时，`G_JB=1 mod4` 强迫两份 parity落在两个互素 residual 中；`G_JB=3 mod4` 则 common gcd本身承担 parity。进一步，common gcd中的 genuine external prime，其完整 gcd exponent全部进入 linear gate `L_JB=DzK+fN`；若 common prime同时 height-supported，则进入既有 omega-content oversaturation / target hierarchy。因此 equal-depth target并非由 companion parity无条件强制，但任何不进入 target 的 parity分配都必须走“两个分离 residual primes”或“external linear-depth”两类明确替代成本。本文不排除这些替代分支，因此不关闭 A2。

---

## 1. parent companions and their common gcd

沿用

\[
D_H
=\gcd(\widehat{\mathcal J}_H,W_q)
=\gcd(\mathscr B_W,W_q),
\]

\[
\boxed{
J^\circ:=\widehat{\mathcal J}_H/D_H,
\qquad
B^\circ:=\mathscr B_W/D_H.}
\tag{1.1}
\]

已有

\[
\widehat{\mathcal J}_H>0,
\qquad
\widehat{\mathcal J}_H\equiv3\pmod4,
\]

\[
\mathscr B_W>0,
\qquad
\mathscr B_W\equiv7\pmod8
\equiv3\pmod4.
\]

`D_H` 为 positive odd integer，所以

\[
\boxed{
J^\circ\equiv B^\circ
\equiv3D_H^{-1}\pmod4.}
\tag{1.2}
\]

定义完整 residual common gcd

\[
\boxed{G_{JB}:=\gcd(J^\circ,B^\circ).}
\tag{1.3}
\]

再定义 coprime residuals

\[
\boxed{
J_1:=J^\circ/G_{JB},
\qquad
B_1:=B^\circ/G_{JB}.}
\tag{1.4}
\]

于是

\[
\boxed{\gcd(J_1,B_1)=1.}
\tag{1.5}
\]

并且

\[
\boxed{
J_1\equiv B_1
\equiv3(D_HG_{JB})^{-1}\pmod4.}
\tag{1.6}
\]

---

## 2. complete mod-4 table

因为 `D_H,G_JB` 都为 odd，只需看两者的 `1/3 mod4` classes：

\[
\boxed{
\begin{array}{c|c|c}
D_H\bmod4&G_{JB}\bmod4&J_1\equiv B_1\pmod4\\ \hline
1&1&3\\
1&3&1\\
3&1&1\\
3&3&3
\end{array}}
\tag{2.1}
\]

因此 residual pair需要两份 independent odd-inert parity，当且仅当

\[
\boxed{G_{JB}\equiv D_H\pmod4.}
\tag{2.2}
\]

此时

\[
\boxed{J_1\equiv B_1\equiv3\pmod4,}
\tag{2.3}
\]

而 `J_1,B_1` positive、odd、coprime，所以它们各自至少含一枚 `3 mod4` prime到奇次，且两枚 suppliers必不同。

特别地，在此前最常用的 parity-doubling orientation

\[
\boxed{D_H\equiv1\pmod4,}
\]
有最简单的二分：

\[
\boxed{
G_{JB}\equiv1\pmod4
\Longrightarrow
J_1,B_1\equiv3\pmod4,}
\tag{2.4}
\]

即 common gcd不吸收 parity，必须生成两枚不同 residual inert suppliers；而

\[
\boxed{
G_{JB}\equiv3\pmod4}
\tag{2.5}
\]
意味着 common gcd本身含 odd total inert parity。

所以 companion parity并不无条件强迫 `G_JB` 非平凡；`G_JB=1` 完全允许，但代价是两份分离 parity。

---

## 3. common parity splits into external or height-supported support

若 `G_JB` 本身承担 odd inert parity，则至少有一枚 genuine inert prime

\[
p\mid G_{JB}.
\]

该 common prime有两类：

### 3.1 external common prime

若

\[
\boxed{p\nmid W_q,}
\tag{3.1}
\]

则它不属于 height-supported oversaturation。`spontaneous-height-companion-cross.md` 给出 genuine external linear gate

\[
\boxed{L_{JB}:=DzK+fN\equiv0\pmod p.}
\tag{3.2}
\]

### 3.2 height-supported common prime

若

\[
\boxed{p\mid W_q,}
\tag{3.3}
\]

则由于 `p|B^circ,J^circ`，完整 height exponent被 `D_H` 吃掉后 companion仍继续加深。`spontaneous-height-content-oversaturation.md` 已证明

\[
\boxed{p\mid\omega,}
\tag{3.4}
\]

并进入 fixed target quadratic

\[
\boxed{
P_{\omega H}(K)
=6K^2-36K+55
\equiv0\pmod p.}
\tag{3.5}
\]

随后才继续按 `e=v_p(omega)` 与 `h=v_p(W_q)` 分成 unequal-depth / equal-depth，equal-depth deep resonance再由 `Sigma_deep`,`Sigma_first`,`Sigma_second` 等 canonical selectors读取。

所以：

\[
\boxed{
\text{common companion parity}
\Longrightarrow
\text{external linear orbit}
\ \text{或}\
\text{height-supported omega/target orbit}.}
\tag{3.6}
\]

---

## 4. external common gcd pays its full depth to `L_JB`

现在固定 genuine external common prime，并假设标准 separation

\[
\boxed{p\nmid qzW^\circ,}
\qquad
W^\circ:=W_q/D_H.
\tag{4.1}
\]

写

\[
j:=v_p(J^\circ),
\qquad
b:=v_p(B^\circ),
\]

\[
\boxed{k:=v_p(G_{JB})=\min(j,b)\ge1.}
\tag{4.2}
\]

已有 exact difference

\[
5^{2d}J^\circ
-(2^mg)^2 5^{2d}B^\circ
=q^2W^\circ\,\mathcal B_p,
\tag{4.3}
\]

其中 bracket满足 exact relation

\[
\boxed{q\mathcal B_p=-zL_{JB}.}
\tag{4.4}
\]

在 (4.1) 下，`q,z,W^circ` 都是 p-adic units，两个左侧 coefficients也是 units。因此：

- 左边两个 summands均被 `p^k` 整除；
- 故其差至少有 depth `k`；
- (4.3),(4.4) 立即给
  \[
  \boxed{v_p(L_{JB})\ge k.}
  \tag{4.5}
  \]

若

\[
\boxed{j\ne b,}
\tag{4.6}
\]

左边有唯一最浅 summand，所以

\[
\boxed{v_p(L_{JB})=k.}
\tag{4.7}
\]

只有 equal companion depths `j=b` 时，linear gate本身才可能继续发生额外 cancellation。

因此 external common gcd不是免费的 support reuse：

\[
\boxed{
\text{每一份 external }G_{JB}\text{ depth都必须由 }L_{JB}\text{ 支付}.}
\tag{4.8}
\]

---

## 5. global parity trichotomy in the dangerous parent orientation

固定

\[
\boxed{D_H\equiv1\pmod4,}
\tag{5.1}
\]

于是 parent companions

\[
J^\circ\equiv B^\circ\equiv3\pmod4.
\]

现在 global companion parity严格只有三种实现方式：

### A. split residual parity

若

\[
G_{JB}\equiv1\pmod4,
\]
则 `J_1,B_1` positive coprime `3 mod4`，所以必须出现两枚不同 inert residual primes。

### B. common external parity

若 `G_JB≡3 mod4` 且承担其 odd parity的 common inert prime不在 `W_q` support，则该 prime进入 external linear gate `L_JB`，并按 §4 支付完整 common depth。

### C. common height-supported parity

若 common inert supplier同时位于 `W_q` support，则它进入 `omega` oversaturation / target hierarchy；equal-depth deep subbranch才进一步进入 `Sigma_deep` 与 serial selectors。

因此：

\[
\boxed{
\text{companion parity}
\Longrightarrow
\begin{cases}
\text{two distinct residual suppliers},\\
\text{external common linear-depth supplier},\\
\text{height-supported omega/target supplier}.
\end{cases}}
\tag{5.2}
\]

这给 global proof一个严格替代关系：**不能假设 target pool必然存在；但不进入 target，就必须支付另外两种明确且可继续量化的 prime成本。**

---

## 6. relation to complete source/target separation

最新 `spontaneous-source-target-support-separation.md` 已把 source-common genuine support与整个 equal-depth target support完全分离。

因此若 case C 最终进入 equal-depth target/serial sector，同时 source parity又调用 genuine source-common pool，则二者成本可以严格叠加，不存在 fixed `11` 复用。

而 case A/B 则给出 target-free alternatives，必须分别从 residual-prime multiplicity或 `L_JB` natural/decimal depth继续攻击。

所以当前正确的 global frontier不是“证明 target一定存在”，而是关闭 trichotomy (5.2) 的三条成本分支。

A2 仍为 `待证`。

---

<a id="source-spontaneous-companion-external-tail-budget"></a>

> 整合来源：`spontaneous-companion-external-tail-budget.md`

# A2 external `J^circ/B^circ` common depth 的 decimal tail budget

> **依赖：** `spontaneous-companion-common-parity-dichotomy.md`、`spontaneous-height-companion-cross.md`、`spontaneous-height-equal-depth-tail-reader.md`、`spontaneous-height-equal-depth-tail-normalization.md`。
>
> **严格状态：**上一层把 `G_JB=gcd(J^circ,B^circ)` 的 common parity分成 external 与 height-supported 两类，并证明 generic external common exponent `k` 全部进入 linear gate `L_JB`。本文进一步证明 generic external common prime不能进入 `omega` content：因为 `p∤W_q` 且 `L_JB=2Dg omega K-fqW_q`，若 `p|omega` 则第二项为唯一 unit，和 `p|L_JB` 矛盾。因此 external common prime与 `alpha=omega W_q` 分离；full-tail decimal identity随即把 `L_JB` 的完整深度无损搬到 `Lambda_dec`，而 tail normalization在该 prime上不约掉任何 p-factor。于是整个 generic external `G_JB` subproduct整除 pure-decimal `Lambda_tail`。本文不排除该 subproduct，因此不关闭 A2。

---

## 1. generic external common setting

固定 genuine inert external common prime `p`，满足

\[
p\mid G_{JB}:=\gcd(J^\circ,B^\circ),
\qquad
p\nmid W_q.
\tag{1.1}
\]

沿用 generic separation

\[
\boxed{
p\nmid2\cdot5\cdot DgKfqzb_3E_Mc_u.}
\tag{1.2}
\]

固定 source/contact exceptional primes继续由既有文件单列；本文只处理真正 moving generic external sector。

写

\[
j:=v_p(J^\circ),
\qquad
b:=v_p(B^\circ),
\]

\[
\boxed{k:=v_p(G_{JB})=\min(j,b)\ge1.}
\tag{1.3}
\]

上一层已证明

\[
\boxed{v_p(L_{JB})\ge k,}
\tag{1.4}
\]

若 `j!=b` 则等号成立。

---

## 2. external common prime cannot divide `omega`

已有 exact form

\[
\boxed{
L_{JB}=2Dg\omega K-fqW_q.}
\tag{2.1}
\]

由 (1.1),(1.2)：

\[
p\nmid fqW_q.
\]

若假设

\[
p\mid\omega,
\]

则 (2.1) 模 `p` 变成

\[
L_{JB}\equiv-fqW_q\not\equiv0\pmod p,
\]

与 `p|G_JB -> p|L_JB` 矛盾。

因此

\[
\boxed{p\nmid\omega.}
\tag{2.2}
\]

结合 `p∤W_q`：

\[
\boxed{p\nmid\alpha=\omega W_q.}
\tag{2.3}
\]

所以 generic external companion-common prime既不是 height prime，也不是 concatenated numerator-content prime。

---

## 3. full-tail identity reads `L_JB` exactly

full decimal tail reader已有全局 exact identity

\[
\boxed{
b_3E_M\omega L_{JB}
=c_u\Lambda_{\rm dec}.}
\tag{3.1}
\]

在当前 generic external prime上，由 (1.2),(2.2)：

\[
p\nmid b_3E_M\omega c_u.
\]

所以 (3.1) 给精确 valuation equality

\[
\boxed{
v_p(\Lambda_{\rm dec})
=v_p(L_{JB}).}
\tag{3.2}
\]

结合 (1.4)：

\[
\boxed{
v_p(\Lambda_{\rm dec})
\ge v_p(G_{JB}).}
\tag{3.3}
\]

如果 `j!=b`：

\[
\boxed{
v_p(\Lambda_{\rm dec})
=v_p(G_{JB})=k.}
\tag{3.4}
\]

只有 equal companion depth `j=b` 时，tail reader才可能继续更深。

---

## 4. normalization removes no external p-factor

canonical tail quotient为

\[
\boxed{
\Lambda_{\rm tail}
:=\frac{\Lambda_{\rm dec}}
{\gcd(\alpha,\Lambda_{\rm dec})}.}
\tag{4.1}
\]

由 (2.3)，`p∤alpha`，因此

\[
v_p(\gcd(\alpha,\Lambda_{\rm dec}))=0.
\]

所以

\[
\boxed{
v_p(\Lambda_{\rm tail})
=v_p(\Lambda_{\rm dec})
=v_p(L_{JB})
\ge k.}
\tag{4.2}
\]

这把 external common depth从 source linear gate完全搬到了 ordinary decimal tail quotient。

---

## 5. global generic external common product

令 `E_ext` 为 generic external common primes集合，并定义

\[
\boxed{
G_{JB}^{\rm ext}
:=\prod_{p\in E_{\rm ext}}
p^{v_p(G_{JB})}.}
\tag{5.1}
\]

逐 prime由 (4.2)：

\[
\boxed{G_{JB}^{\rm ext}\mid\Lambda_{\rm tail}.}
\tag{5.2}
\]

而 tail normalization给

\[
\Lambda_{\rm tail}
=\frac{\Lambda_{\rm dec}}{\omega\Gamma},
\qquad
\Gamma=\gcd(\omega,W_q),
\]
以及

\[
44T^2N^3<\Lambda_{\rm dec}<45T^2N^3.
\]

因此

\[
\boxed{
G_{JB}^{\rm ext}
\le\Lambda_{\rm tail}
<\frac{45T^2N^3}{\omega\Gamma}.}
\tag{5.3}
\]

若只需不含 source quantities 的粗界：

\[
\boxed{G_{JB}^{\rm ext}<45T^2N^3.}
\tag{5.4}
\]

---

## 6. updated companion-parity trichotomy

在危险 parent orientation `D_H=1 mod4` 中，上一层三岔现在加强为：

1. **split residual parity**：`G_JB=1 mod4`，需要两枚不同 inert residual suppliers；
2. **common external parity**：common inert supplier位于 external sector，其完整 `G_JB` depth进入 `Lambda_tail`，满足 (5.3)；
3. **common height-supported parity**：进入 omega-content oversaturation，随后按 unequal/equal-depth与 serial hierarchy继续分类。

因此 case B 已从 source linear gate升级为 pure-decimal global height budget。

特别地，不能把 case B 和 equal-depth tail混为同一 prime pool：external common prime满足

\[
p\nmid\omega W_q,
\]
而 equal-depth target prime满足

\[
p\mid\omega W_q.
\]

两者在 support 上严格互斥，只是都由同一个 canonical `Lambda_tail` 记录各自的 resonance depth。

A2 仍为 `待证`。

---

<a id="source-spontaneous-cross-sign-biquadratic"></a>

> 整合来源：`spontaneous-cross-sign-biquadratic.md`

# A2 conjugate-angle cross-sign branch as a quadratic norm with no real `tau` root

> **依赖：** `spontaneous-cross-sign-sphere.md`、`spontaneous-cross-sign-height-shadow.md`、`spontaneous-single-branch.md`。
>
> **严格状态：**conjugate angle sheet `O_-=0` 的 exact sphere只有一个 quadratic coordinate `v^2=-2X_cross`。本文显式写出两条 third-numerator orientations，并证明与 additive root相交得到的 quadratic norm在整个实 `tau` 轴上严格为正。因此 cross-sign common sector不存在任何 real decimal root；剩余接触只能来自真正的 finite-field / p-adic wrapping。本文不把实轴空性提升成 modular 空性，也不宣称 A2 closure。

---

## 1. normalized sphere

记

\[
x=\frac{b_2}{10^M},\qquad
y=\frac{a_2}{10^{M-1}},\qquad
\tau=10^{-M},\qquad s=9+y,
\]

\[
n=\frac{2025x^2+y^2}{100},\qquad
c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.
\]

exact sphere 为

\[
\mathscr S(w,z)
=x^2w^2(s+z)^2-(x+2+w)^2(nw^2+x^2z^2).
\tag{1.1}
\]

令

\[
d=225x^2-y,\qquad
A_{\rm sp}=4d^2-xy^2(99x-4),
\]

\[
W=\frac{A_{\rm sp}}{2y^2(x+2)}.
\tag{1.2}
\]

`O_-=0` 对应 conjugate angle root

\[
\boxed{w=W.}
\tag{1.3}
\]

---

## 2. sphere 的两个 quadratic orientations

定义

\[
H=202500x^4-99x^2y^2-1800x^2y+4xy^2+4y^2,
\tag{2.1}
\]

\[
H^\vee=H+2y^2(x+2)^2,
\tag{2.2}
\]

\[
D_z=101250x^4-49x^2y^2-900x^2y+4xy^2+4y^2,
\tag{2.3}
\]

以及

\[
\begin{aligned}
X_\times={}&205031250x^6+2025x^4y^2-1822500x^4y\\
&+8100x^3y^2-99x^2y^4-1800x^2y^3\\
&+4050x^2y^2+4xy^4+4y^4.
\end{aligned}
\tag{2.4}
\]

`spontaneous-cross-sign-sphere.md` 已给

\[
\operatorname{Disc}_{z}\mathscr S(W,z)
=-\frac{x^2H^2(H^\vee)^2X_\times}
{200y^{10}(x+2)^4}.
\tag{2.5}
\]

定义 quadratic coordinate

\[
\boxed{v^2=-2X_\times.}
\tag{2.6}
\]

把 `S(W,z)` 看成 `z` 的二次式，其 leading coefficient为

\[
[z^2]\mathscr S(W,z)=-\frac{2x^2D_z}{y^2},
\tag{2.7}
\]

center 为

\[
\boxed{
Z_c=\frac{sH^2}{8y^2(x+2)^2D_z}.
}
\tag{2.8}
\]

再令

\[
\boxed{
Z_v=\frac{HH^\vee}{80xy^3(x+2)^2D_z}.
}
\tag{2.9}
\]

quadratic formula因此给两根（正负号只决定标签）：

\[
\boxed{Z_\pm=Z_c\pm Z_vv.}
\tag{2.10}
\]

checker直接在

\[
\mathbf Q(x,y)[v]/(v^2+2X_\times)
\]
中验证

\[
\mathscr S(W,Z_c+Z_vv)=0.
\tag{2.11}
\]

---

## 3. endpoint 中 root formula 没有 pole

使用闭 endpoint box

\[
\frac1{10}\le x\le\frac2{19},\qquad
\frac{249}{250}\le y\le1.
\tag{3.1}
\]

对 `H`：

\[
\partial_xH
=810000x^3-198xy^2-3600xy+4y^2
>810-\frac{396}{19}-\frac{7200}{19}>0,
\]

\[
\partial_yH
=-198x^2y-1800x^2+8xy+8y
<-18+\frac{16}{19}+8<0.
\]

因此

\[
\boxed{H\ge H(1/10,1)=\frac{283}{50}>0.}
\tag{3.2}
\]

从而

\[
\boxed{H^\vee>H>0.}
\tag{3.3}
\]

同理：

\[
\partial_xD_z
>405-\frac{196}{19}-\frac{3600}{19}>0,
\]

\[
\partial_yD_z
<-9+\frac{16}{19}+8<0,
\]

故

\[
\boxed{D_z\ge D_z(1/10,1)=\frac{1007}{200}>0.}
\tag{3.4}
\]

已有 exact endpoint estimate

\[
\boxed{X_\times>56>0.}
\tag{3.5}
\]

所以 (2.8)–(2.10) 的 denominator 在整个真实 endpoint上均为正。

---

## 4. additive compact branches

对任意 fixed sphere root `z`，universal compact equation为

\[
\mathscr L(\tau,z)
=55\tau^2+18(z-s)\tau+s^2-4sz-c.
\tag{4.1}
\]

写成

\[
\boxed{\mathscr L(\tau,z)=A(\tau)+B(\tau)z,}
\tag{4.2}
\]

其中

\[
A(\tau)=55\tau^2-18s\tau+s^2-c,
\tag{4.3}
\]

\[
B(\tau)=18\tau-4s=2(9\tau-2s).
\tag{4.4}
\]

代入 (2.10)：

\[
\boxed{
\mathscr L_\pm^\times
=A+BZ_c\pm BZ_vv.
}
\tag{4.5}
\]

因此两支的 quadratic norm 是

\[
\boxed{
\begin{aligned}
\mathcal N_\times(\tau)
&=\mathscr L_+^\times\mathscr L_-^\times\\
&=(A+BZ_c)^2+2X_\times B^2Z_v^2.
\end{aligned}}
\tag{4.6}
\]

任何清分母后出现的 quartic `tau` eliminant都只是这个 quadratic norm，不是新的独立 quartic obstruction。

---

## 5. exact polynomial norm

定义公共正 denominator

\[
\boxed{
\mathscr D=200x^2y^3(x+2)^2D_z.
}
\tag{5.1}
\]

以及

\[
A_0
=100x^2(55\tau^2-18s\tau+s^2)
-(x+2)^2(2025x^2+y^2),
\tag{5.2}
\]

故 `A=A_0/(100x^2)`。

定义

\[
\boxed{
U_\times
=2y^3(x+2)^2D_zA_0+25x^2ysH^2B,
}
\tag{5.3}
\]

和（注意 `B=2(9tau-2s)`）

\[
\boxed{
V_\times
=5x(9\tau-2s)HH^\vee.
}
\tag{5.4}
\]

则 exact clearing identities 是

\[
\boxed{
\mathscr D(A+BZ_c)=U_\times,
\qquad
\mathscr D(BZ_v)=V_\times.
}
\tag{5.5}
\]

因此定义

\[
\boxed{
\mathfrak N_\times
=U_\times^2+2X_\times V_\times^2,
}
\tag{5.6}
\]

有

\[
\boxed{
\mathfrak N_\times
=\mathscr D^2\mathcal N_\times.
}
\tag{5.7}
\]

这给 modular work 一个完全 polynomial 的自然代表。

---

## 6. `已严格完成`：整个实 `tau` 轴无根

由 `X_cross>0`，(4.6) 是两个非负项之和：

\[
\mathcal N_\times
=(A+BZ_c)^2+2X_\times B^2Z_v^2\ge0.
\]

因为 endpoint 中 `Z_v!=0`，若等号成立，必须

\[
B(\tau)=0,
\]
即

\[
\boxed{\tau=\frac{2s}{9}.}
\tag{6.1}
\]

但此时

\[
\begin{aligned}
A(2s/9)
&=55\frac{4s^2}{81}-18s\frac{2s}{9}+s^2-c\\
&=-\frac{23}{81}s^2-c<0.
\end{aligned}
\tag{6.2}
\]

所以 `A+BZ_c=A!=0`，矛盾。故

\[
\boxed{
\mathcal N_\times(\tau)>0
\quad\text{for every }\tau\in\mathbf R.
}
\tag{6.3}
\]

由于 `D>0`，亦有

\[
\boxed{
\mathfrak N_\times(\tau)>0
\quad\text{for every }\tau\in\mathbf R.
}
\tag{6.4}
\]

这比“actual decimal phase离 roots 很远”更强：cross-sign common norm在整个实轴根本没有 root。

---

## 7. frontier

现在几类主要 external simple geometry的 Archimedean 状态已统一：

- actual pure-spontaneous branches：所有 real `tau` roots `>1`；
- additive height companion `J_H`：所有 real `tau` roots `>1`；
- omega-content branch：两张 real numerator roots避开真实 `y` window；
- conjugate-angle cross-sign branch：`N_cross(tau)>0` 对所有 real `tau`。

所以 global parity ledger留下的 residual primes都只能靠 genuine modular wrapping / decimal multiplicative orbit产生，而不能解释为 real near-root。

本文仍未把这一点提升为 modular emptiness。下一步最值得做的是审计 polynomial norm `N_frak` 的 singular bad reduction，或寻找它与 `tau=10^{-M}` multiplicative subgroup之间的统一 natural-representative约束。

---

<a id="source-spontaneous-cross-sign-height-shadow"></a>

> 整合来源：`spontaneous-cross-sign-height-shadow.md`

# A2 cross-sign quadratic gate 在两张 height sheets 上均为 square shadow

> **依赖：** `spontaneous-cross-sign-sphere.md`、`spontaneous-height-parity-ledger.md`。
>
> **严格状态：**`spontaneous-cross-sign-sphere.md` 定义 conjugate-angle quadratic gate `v^2=-2X_cross`。本文证明在 height-1 与 height-2 两张 sphere orientations上，`-2X_cross` 都具有显式 rational/polynomial square root，因此该 quadratic character在整个 height-supported sector都是自动 shadow，不能作为独立 obstruction。随后审计两个 square-root collision locus：所有 genuine non-`3` inert finite singular candidates都在第一次 `p^2` lifting时失败，因此 cross-sign angle/height sector没有 surviving singular Hensel tree，只剩 simple moving synchronization。本文不排除 simple roots，也不宣称 A2 closure。

---

## 1. 记号

定义

\[
P(x):=101x^2+4x+4,
\]

height-1 orientation：

\[
\boxed{
H_1:=202500x^4+P(x)y^2.
}
\tag{1.1}
\]

height-2 orientation：

\[
\boxed{
\begin{aligned}
H_2={}&410062500x^6-402975x^4y^2-7290000x^4y\\
&+8100x^3y^2+101x^2y^4+3600x^2y^3\\
&+40500x^2y^2+4xy^4+4y^4.
\end{aligned}}
\tag{1.2}
\]

cross-sign polynomial为

\[
\boxed{
\begin{aligned}
X_\times={}&205031250x^6+2025x^4y^2-1822500x^4y\\
&+8100x^3y^2-99x^2y^4-1800x^2y^3\\
&+4050x^2y^2+4xy^4+4y^4.
\end{aligned}}
\tag{1.3}
\]

conjugate-angle sphere在 genuine odd prime上有 third-numerator root所需的唯一 quadratic character是

\[
\left(\frac{-2X_\times}{p}\right)=1.
\tag{1.4}
\]

---

## 2. `已严格完成`：height-1 上 `-2X_cross` 是显式平方

定义

\[
\boxed{
R_1^{\rm sq}
:=20250x^3(9x-2)(11x+2)-90xyP(x).
}
\tag{2.1}
\]

直接 polynomial division 得 exact congruence

\[
\boxed{
P(x)^2(-2X_\times)
\equiv
\left(R_1^{\rm sq}\right)^2
\pmod{H_1}.
}
\tag{2.2}
\]

更强地，左减右恰为 `H_1` 乘一个显式整数 polynomial；checker逐项验证。

对 genuine non-`3` inert height-1 prime，`P(x)` 为 unit。事实上

\[
P(x)=(10x)^2+(x+2)^2,
\]
而 `p=3 mod4` 不允许两个 nonzero squares之和为零。

因此在 `H_1=0` 上：

\[
\boxed{
-2X_\times
\equiv
\left[
\frac{20250x^3(9x-2)(11x+2)}{P(x)}-90xy
\right]^2.
}
\tag{2.3}
\]

所以

\[
\boxed{
H_1=0
\Longrightarrow
\left(\frac{-2X_\times}{p}\right)=1
}
\tag{2.4}
\]

自动成立。

---

## 3. height-2 上也是显式平方

令

\[
D_2:=2025x^2-2y^2-27y.
\]

已有 exact syzygy

\[
X_\times=H_2-50x^2D_2^2.
\]

因此

\[
\boxed{
-2X_\times
\equiv
(10xD_2)^2
\pmod{H_2}.
}
\tag{3.1}
\]

所以 height-2 同样自动满足 cross-sign quadratic gate：

\[
\boxed{
H_2=0
\Longrightarrow
\left(\frac{-2X_\times}{p}\right)=1.
}
\tag{3.2}
\]

结论：cross-sign Legendre condition在两张 height orientations上都只是旧 sphere splitting 的投影，不能重复收费。

---

# square-root collision audit

## 4. height-1 collision只剩固定 quartic

height-1 的 cross square root消失意味着

\[
H_1=0,
\qquad
R_1^{\rm sq}=0.
\]

消去 `y`：

\[
\boxed{
\operatorname{Res}_y(H_1,R_1^{\rm sq})
=410062500x^6P(x)Q_1(x),
}
\tag{4.1}
\]

其中

\[
\boxed{
Q_1(x)=9801x^4-792x^3-372x^2+48x+32.
}
\tag{4.2}
\]

`x=0` 为 boundary；`P=0` 对 genuine inert prime不可能。因此只需审计 `Q_1`。

其判别式：

\[
\boxed{
\operatorname{Disc}(Q_1)
=2^{18}3^7 5^2 11^2\cdot3677363.
}
\tag{4.3}
\]

`p=11` 只导致 leading-degree drop，并无 finite repeated root。唯一 genuine non-`3` inert repeated finite candidate为

\[
\boxed{p=3677363.}
\tag{4.4}
\]

模 `p`：

\[
\gcd(Q_1,Q_1')=x-1336107.
\]

full system `H_1=R_1^{sq}=0` 唯一给

\[
\boxed{
(x,y)=(1336107,2340128)\pmod p.
}
\tag{4.5}
\]

该点 Jacobian determinant为零。写

\[
x=x_0+pX,
\qquad
y=y_0+pY,
\]
除以 `p` 后的 augmented linear system右端为

\[
\boxed{(482973,1688419).}
\tag{4.6}
\]

直接 rank compatibility检查失败，因此：

\[
\boxed{
\text{height-1 唯一 genuine singular cross collision不能 lift 到 }p^2.
}
\tag{4.7}
\]

---

## 5. height-2 collision只剩两个 genuine inert repeated candidates

height-2 square root消失意味着

\[
H_2=0,
\qquad
D_2=0.
\]

消去 `y`：

\[
\boxed{
\operatorname{Res}_y(H_2,D_2)
=672605015625x^6(25x^2+1)Q_2(x),
}
\tag{5.1}
\]

其中

\[
\boxed{
Q_2(x)
=10609x^4+2472x^3+3052x^2+432x+288.
}
\tag{5.2}
\]

对 `p=3 mod4`，`25x^2+1=0` 不可能有 genuine unit root。

quartic discriminant为

\[
\boxed{
\operatorname{Disc}(Q_2)
=2^{18}3^2 5^2\cdot61\cdot103^2\cdot2671\cdot6659.
}
\tag{5.3}
\]

`p=103` 只是 leading-degree drop，没有 finite repeated root。genuine inert repeated candidates只剩

\[
\boxed{p=2671,6659.}
\tag{5.4}
\]

### `p=2671`

repeated `x` root：

\[
x\equiv-56\equiv2615.
\]

`D_2=0` 有两个 `y` roots，但只有

\[
\boxed{(x,y)=(2615,601)}
\tag{5.5}
\]

同时满足 `H_2=0`。

该点 `p^2` linearization的右端为

\[
(1437,335),
\]
且 rank compatibility失败。

### `p=6659`

repeated `x` root：

\[
x=654.
\]

full collision唯一 genuine state：

\[
\boxed{(x,y)=(654,2478).}
\tag{5.6}
\]

`p^2` linearization右端：

\[
(4424,4966),
\]
同样不属于 Jacobian image。

因此：

\[
\boxed{
\text{height-2 cross square-root collision也没有 surviving singular Hensel tree.}
}
\tag{5.7}
\]

---

## 6. 严格结论

cross-sign conjugate-angle quadratic extension在 height-supported sector中的完整状态是：

\[
\boxed{
\begin{array}{c|c|c}
\text{height sheet}&-2X_\times&\text{singular collision}\\ \hline
H_1&\text{explicit square}&p=3677363\text{ dies at }p^2\\
H_2&\text{explicit square}&p=2671,6659\text{ die at }p^2.
\end{array}}
\tag{6.1}
\]

所以：

\[
\boxed{
\text{cross-sign angle/height interaction没有新的 quadratic obstruction，}
}
\]

并且

\[
\boxed{
\text{也没有新的 singular Hensel tree。}
}
\]

剩下的 height-supported cross-sign contacts全部是 simple moving decimal synchronization。继续追同一 quadratic character或 singular discriminant不会增加约束。

---

<a id="source-spontaneous-cross-sign-height1-shadow"></a>

> 整合来源：`spontaneous-cross-sign-height1-shadow.md`

# A2 cross-sign sphere 在 height-1 sheet 上的 exact square shadow

> **依赖：** `spontaneous-cross-sign-sphere.md`、`spontaneous-height-parity-ledger.md`。
>
> **严格状态：**`spontaneous-cross-sign-sphere.md` 已证明 conjugate-angle sphere 的唯一 quadratic extension 为 `v^2=-2X_cross`，并在 height-2 orientation 上给出 `2X_cross=-square`。该文件把 height-1 relative character留作开放项。本文补齐这一项：构造一个 exact integer syzygy，证明在 `H_1=0` 上同样有 `-2X_cross=square`。所以对两张 moving height orientations，cross-sign quadratic character都自动满足；它不能为 moving-height parity提供第二条独立 Legendre obstruction。仅 `X_cross=0` 的 discriminant collision仍需作为 singular intersection单列。

---

## 1. notation

沿用 normalized decimal variables

\[
x=B/N_{\rm dec},
\qquad
y=10A/N_{\rm dec}.
\]

height-1 polynomial为

\[
\boxed{
H_1
=202500x^4+(101x^2+4x+4)y^2.}
\tag{1.1}

定义

\[
\boxed{C_1:=101x^2+4x+4.}
\tag{1.2}

cross-sign sphere的 quadratic polynomial为

\[
\boxed{
\begin{aligned}
X_\times={}&205031250x^6+2025x^4y^2-1822500x^4y\\
&+8100x^3y^2-99x^2y^4-1800x^2y^3\\
&+4050x^2y^2+4xy^4+4y^4.
\end{aligned}}
\tag{1.3}

conjugate-angle sphere有 third-numerator root的 generic inert character gate为

\[
\left(\frac{-2X_\times}{p}\right)=1.
\tag{1.4}

---

## 2. exact square syzygy

定义

\[
\boxed{
S_1
:=90x\left[
225x^2(9x-2)(11x+2)-C_1y
\right].}
\tag{2.1}

再定义整数多项式

\[
\boxed{
\begin{aligned}
Q_1={}&20252025x^6+16200x^5-9999x^4y^2-181800x^4y+48600x^4\\
&+8x^3y^2-7200x^3y+64800x^3\\
&+24x^2y^2-7200x^2y+32400x^2\\
&+32xy^2+16y^2.
\end{aligned}}
\tag{2.2}

直接展开得到 exact identity

\[
\boxed{
S_1^2+2C_1^2X_\times
=2H_1Q_1.}
\tag{2.3}

这条式子在 `Z[x,y]` 中成立，不使用任何 modular root 假设。

---

## 3. genuine height-1 root 上 `C_1` 是 unit

固定 genuine non-`3` inert moving height prime，并假设

\[
H_1=0\pmod p.
\]

若同时 `C_1=0`，由 (1.1) 得

\[
202500x^4=0\pmod p.
\]
对 `p!=2,3,5` 且 external `x` 为 unit不可能。因此

\[
\boxed{C_1\ne0\pmod p.}
\tag{3.1}

所以可以在 `F_p` 中除以 `C_1^2`。

---

## 4. height-1 cross-sign character自动满足

在 `H_1=0` 上，(2.3) 退化为

\[
S_1^2+2C_1^2X_\times=0.
\]
因此

\[
\boxed{
-2X_\times
=\left(\frac{S_1}{C_1}\right)^2
\pmod p.}
\tag{4.1}

若 `X_cross` 为 unit，则右边非零，立即有

\[
\boxed{
\left(\frac{-2X_\times}{p}\right)=1.}
\tag{4.2}

所以 conjugate-angle cross-sign sphere要求的 quadratic character在 `H_1` sheet 上自动成立。

等价地，对 `p=3 mod4`：

\[
\boxed{
\left(\frac{2X_\times}{p}\right)=-1,}
\tag{4.3}

与 `spontaneous-cross-sign-sphere.md` 在 `H_2` sheet 上得到的结果完全一致。

---

## 5. both height sheets are now character shadows

旧 `H_2` syzygy为

\[
X_\times
=H_2-50x^2(2025x^2-2y^2-27y)^2,
\]
故在 `H_2=0` 上

\[
2X_\times
=-\left[10x(2025x^2-2y^2-27y)\right]^2.
\]

结合本文 (4.1)：

\[
\boxed{
\begin{array}{c|c}
H_1=0&-2X_\times=(S_1/C_1)^2\\
H_2=0&-2X_\times=[10x(2025x^2-2y^2-27y)]^2
\end{array}}
\tag{5.1}

因此两张 moving height orientations 都已经把 cross-sign quadratic extension split over the residue field。

---

## 6. updated cross-sign frontier

`spontaneous-cross-sign-sphere.md` 原先列出的 “height-1 orientation 与 `X_cross` 的相对 character” 可以删除。

对 moving height pool，cross-sign sphere尚有独立内容的只剩：

\[
\boxed{X_\times=0}
\]
的 discriminant collision / higher-depth intersection，以及不依附 height sheet的 generic cross-sign decimal orbit。

因此若目标仍是关闭 moving-height equal-depth shell，继续叠加 `(-2X_cross/p)=1` 不会增加约束；应转向 `X_cross=0` singular collision或 global natural representative。

---

<a id="source-spontaneous-cross-sign-sphere"></a>

> 整合来源：`spontaneous-cross-sign-sphere.md`

# A2 conjugate-angle cross-sign sphere 的 quadratic gate

> **依赖：** `spontaneous-sign-companion-parity.md`、`spontaneous-sphere-roots.md`、`spontaneous-height-parity-ledger.md`。
>
> **严格状态：**actual angle sheet `O_+=0` 已知使 exact sphere关于 third numerator完全 split。本文研究相反的 angle sign companion `O_-=0`。结论是：conjugate-angle sphere不再 split over `Q(x,y)`，而恰好引入一个 quadratic extension `v^2=-2X_cross`；在真实 endpoint 上 `X_cross>56`，所以该 sphere没有任何 real third-numerator root。对 genuine `p=3 mod4`，cross-sign overlap必须满足 `(-2X_cross/p)=1`。同时在旧 height-2 orientation上该 character自动退化成 `-1` times a square，因此不能重复收费。本文不排除 generic p-adic cross-sign roots，也不宣称 A2 closure。

---

## 1. normalized exact sphere与 angle sign roots

沿用

\[
x=\frac{b_2}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}},
\qquad
s=9+y,
\]

\[
n:=\frac{2025x^2+y^2}{100}.
\]

第三块 normalized variables 为

\[
\bar w=\frac{b_3}{T10^M},
\qquad
\bar\zeta=\frac{a_3}{T10^M}.
\]

exact sphere：

\[
\boxed{
\mathscr S(\bar w,\bar\zeta)
=x^2\bar w^2(s+\bar\zeta)^2
-(x+2+\bar w)^2
\left(n\bar w^2+x^2\bar\zeta^2\right).
}
\tag{1.1}
\]

定义

\[
d:=225x^2-y,
\]

\[
A_{\rm sp}:=4d^2-xy^2(99x-4),
\]

以及正的 rational magnitude

\[
\boxed{
W:=\frac{A_{\rm sp}}{2y^2(x+2)}.
}
\tag{1.2}
\]

actual angle carrier `O_+=0` 给

\[
\bar w=-W,
\]

而 sign companion `O_-=0` 给

\[
\boxed{\bar w=+W.}
\tag{1.3}
\]

`spontaneous-sphere-roots.md` 已证明 `bar w=-W` 时 sphere discriminant是完整平方。本文处理 (1.3)。

---

## 2. conjugate-angle discriminant完全因子化

定义

\[
\boxed{
H:=202500x^4-99x^2y^2-1800x^2y+4xy^2+4y^2,
}
\tag{2.1}
\]

\[
\boxed{
H^\vee:=H+2y^2(x+2)^2
=202500x^4-97x^2y^2-1800x^2y+12xy^2+12y^2.
}
\tag{2.2}
\]

再定义新的 cross polynomial

\[
\boxed{
\begin{aligned}
X_\times:={}&205031250x^6+2025x^4y^2-1822500x^4y\\
&+8100x^3y^2-99x^2y^4-1800x^2y^3\\
&+4050x^2y^2+4xy^4+4y^4.
\end{aligned}}
\tag{2.3}
\]

把 `bar w=W` 代入 (1.1)，视为 `bar zeta` 的二次式。直接 exact discriminant calculation 给

\[
\boxed{
\operatorname{Disc}_{\bar\zeta}
\mathscr S(W,\bar\zeta)
=
-\frac{
 x^2H^2(H^\vee)^2X_\times
}{
200y^{10}(x+2)^4
}.
}
\tag{2.4}
\]

除了 `X_cross` 外其余 nontrivial factors全为平方。

因为

\[
200=2\cdot10^2,
\]
对 genuine odd prime `p` 且所有 displayed denominator / square factors为 unit：

\[
\left(
\frac{\operatorname{Disc}}p
\right)
=
\left(\frac{-2X_\times}{p}\right).
\tag{2.5}
\]

所以 sphere 在 `F_p` 中有 third-numerator root的必要条件为

\[
\boxed{
\left(\frac{-2X_\times}{p}\right)=1.
}
\tag{2.6}
\]

若 `p=3 mod4`，也可写成

\[
\boxed{
\left(\frac{2X_\times}{p}\right)=-1.
}
\tag{2.7}
\]

---

## 3. quadratic tower坐标

定义 quadratic coordinate

\[
\boxed{v^2=-2X_\times.}
\tag{3.1}
\]

则 (2.4) 的平方根可以无 radical denominator 地写成

\[
\sqrt{\operatorname{Disc}}
=
\frac{xHH^\vee}{20y^5(x+2)^2}v.
\tag{3.2}
\]

因此 conjugate-angle sphere 的两个 third-numerator orientations已经完全进入单一 quadratic extension

\[
\mathbf Q(x,y)(v),
\qquad v^2=-2X_\times.
\]

所以 cross pair `(O_-,Theta_-)` 或 `(O_-,Theta_+)` 并不存在新的隐藏高次 extension；第一层恰好只是 (3.1)。后续把 additive linear root代入，只会在这一 quadratic extension上产生关于 `tau` 的二次式，其 pure-prefix quartic只是 quadratic norm。

---

## 4. `已严格完成`：真实 endpoint 中 `X_cross>56`

endpoint box：

\[
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1.
\]

把 (2.3) 分成三个显然可控的正块：

\[
\begin{aligned}
X_\times={}&
 x^4\bigl(
205031250x^2-1822500y+2025y^2
\bigr)\\
&+x^2y^2\bigl(
8100x-99y^2-1800y+4050
\bigr)\\
&+4y^4(x+1).
\end{aligned}
\tag{4.1}
\]

第一括号对 `x` 递增、对 `y` 递减，所以

\[
205031250x^2-1822500y+2025y^2
>
\frac{459675}{2}.
\]

故第一块

\[
>\frac{459675}{20000}>22.
\tag{4.2}
\]

第二括号同样在 `x=1/10,y=1` 取得粗下界：

\[
8100x-99y^2-1800y+4050>2961.
\]

因此第二块

\[
>
\frac1{100}\left(\frac{249}{250}\right)^2 2961
>29.
\tag{4.3}
\]

第三块显然

\[
4y^4(x+1)
>
4\left(\frac{249}{250}\right)^4\frac{11}{10}
>4.
\tag{4.4}
\]

合并：

\[
\boxed{X_\times>22+29+4=55.}
\]

用 exact fractions稍微保留余量可得到

\[
\boxed{X_\times>56.}
\tag{4.5}
\]

因此真实 endpoint中 (2.4) 严格为负：

\[
\boxed{
\operatorname{Disc}_{\bar\zeta}\mathscr S(W,\bar\zeta)<0.
}
\tag{4.6}
\]

所以 conjugate-angle sheet根本没有 real third-numerator orientation；任何 cross-sign contact都必须是纯 modular / p-adic phenomenon。

---

## 5. height-2 上 quadratic character是自动 shadow

`spontaneous-height-parity-ledger.md` 的第二 height orientation为

\[
\boxed{
\begin{aligned}
H_2={}&410062500x^6-402975x^4y^2-7290000x^4y\\
&+8100x^3y^2+101x^2y^4+3600x^2y^3\\
&+40500x^2y^2+4xy^4+4y^4.
\end{aligned}}
\tag{5.1}
\]

直接展开有 exact syzygy：

\[
\boxed{
X_\times
=H_2
-50x^2\left(2025x^2-2y^2-27y\right)^2.
}
\tag{5.2}
\]

因此在 `H_2=0` 上：

\[
\boxed{
2X_\times
=-\left[
10x(2025x^2-2y^2-27y)
\right]^2.
}
\tag{5.3}
\]

对 genuine `p=3 mod4` 且右边线性 factor为 unit：

\[
\left(\frac{2X_\times}{p}\right)
=\left(\frac{-1}{p}\right)
=-1.
\]

这正好等于 (2.7) 所需的 cross-sign character。

所以：

\[
\boxed{
\text{在 height-2 sheet 上，cross-sign quadratic character 自动满足。}
}
\tag{5.4}
\]

它只是旧 height geometry 的 shadow，不能作为第二个独立 obstruction再次收费。

若 (5.3) 的 square factor也为零，则进入 discriminant-zero collision；那是单独的 singular/common-root问题，本文不把它自动判空。

---

## 6. 更新后的 cross-pair frontier

结合 `spontaneous-sign-companion-parity.md`：

- same-sign-pair common support已经被压到 prefix content / central / `a_3`；
- 最难的 cross pair `O_-` 与 additive sheets必须先穿过 quadratic gate `v^2=-2X_cross`；
- 该 quadratic gate在 real endpoint完全没有 root；
- 在 height-2 上它又退化为自动 square shadow。

因此下一步若继续 cross allocation，真正有新增信息的只剩：

1. generic `X_cross` quadratic sheet上的 decimal `tau` orbit；
2. height-1 orientation与 `X_cross` 的相对 character/depth；
3. `X_cross=0` 的 singular bad-reduction audit。

继续在 height-2 上叠加同一 Legendre condition不会增加约束。

---

<a id="source-spontaneous-cstar-audit"></a>

> 整合来源：`spontaneous-cstar-audit.md`

# A2 `C_*` 的原始 decimal 形式与 external character 降级

> **依赖：** `spontaneous-single-branch-syzygy.md`、`decimal-prefix-bridge.md`、`external-secant-center.md`。
>
> **严格状态：**本文把 pure-prefix kernel `C_*` 乘回原始 decimal integers，并证明 single-branch repeated-root 导出的 character `(C_*/p)=(-55/p)` 在 external double-root/prefix-norm 子通道中已经由旧中心条件自动成立。因此该 character 不是新的独立 obstruction，必须降级，不能重复收费。本文仍**不宣称 A2 全局关闭**。

---

## 1. `C_*` 的 source-free 原始整数形式

记

\[
N=10^M,
\qquad A=a_2,
\qquad B=b_2,
\]

\[
Q=2N+B,
\qquad K=9N+10A,
\]

\[
N_0=\left(\frac{9B}{2}\right)^2+A^2.
\]

scale-free variables 为

\[
x=B/N,
\qquad y=10A/N.
\]

`spontaneous-prefix-eliminant.md` 定义

\[
\begin{aligned}
C_*={}&164025x^4+656100x^3
+2381x^2y^2+41400x^2y\\
&+842400x^2+324xy^2+324y^2.
\end{aligned}
\]

定义原始整数

\[
\boxed{
\mathcal C_*^{\rm int}
:=23B^2K^2+81Q^2N_0.
}
\tag{1.1}

直接代入 `x,y`：

\[
\boxed{
N^4C_*=100\mathcal C_*^{\rm int}.
}
\tag{1.2}

因为 external / spontaneous prime 与 `2,5,N` 分离，所以 `100/N^4` 是模 `p` 的平方。因此

\[
\boxed{
\left(\frac{C_*}{p}\right)
=
\left(\frac{\mathcal C_*^{\rm int}}p\right)
}
\tag{1.3}

只要两边都是单位。

(1.1) 也给出一个几何解释：

\[
\mathcal C_*^{\rm int}
=23(BK)^2
+(9QC_0)^2+(9QA)^2,
\qquad C_0=9B/2.
\tag{1.4}

所以 `C_*` 是一个 `Gaussian norm + 23 square` 的正三元型，而不是无来源的 resultant 系数。

---

## 2. `已严格完成`：`C_*` 与 external prefix norm 的精确桥

`decimal-prefix-bridge.md` 定义

\[
\boxed{
\mathscr R_N
=324Q^2N_0+2695B^2.
}
\tag{2.1}

由 (1.1)：

\[
4\mathcal C_*^{\rm int}
=92B^2K^2+324Q^2N_0.
\]
所以

\[
\boxed{
4\mathcal C_*^{\rm int}
=
\mathscr R_N+B^2(92K^2-2695).
}
\tag{2.2}

这把 single-branch central kernel 直接接回此前 external double-root 的 prefix norm target。

---

## 3. `已严格完成`：external center 自动固定 `C_*` 的 character

external discriminant-zero common-height center 已给

\[
18K-55\equiv0\pmod p,
\qquad
\mathscr R_N\equiv0\pmod p.
\tag{3.1}

所以

\[
K\equiv\frac{55}{18}.
\]
代入 (2.2)：

\[
\begin{aligned}
\mathcal C_*^{\rm int}
&\equiv
\frac{B^2}{4}
\left(92\frac{55^2}{18^2}-2695\right)\\
&=
-\frac{37180}{81}B^2.
\end{aligned}
\]

即

\[
\boxed{
\mathcal C_*^{\rm int}
\equiv
-\frac{4\cdot5\cdot11\cdot13^2}{9^2}B^2
\pmod p.
}
\tag{3.2}

对于 `p∤2·3·5·11·13·B`：

\[
\boxed{
\left(\frac{C_*}{p}\right)
=
\left(\frac{-55}{p}\right).
}
\tag{3.3}

因此如果 `p≡3 (mod 4)` 且 external discriminant-zero 还给

\[
\left(\frac{55}{p}\right)=1,
\]
则自动有

\[
\boxed{
\left(\frac{C_*}{p}\right)=-1.
}
\tag{3.4}

---

## 4. `已严格完成 / 降级`：repeated-root character 是旧中心的影子

`spontaneous-single-branch-syzygy.md` 独立从 repeated tangent 推出

\[
\left(\frac{C_*}{p}\right)
=
\left(\frac{-55}{p}\right).
\tag{4.1}

但 §3 证明：一旦同一个 prime 还处于 external double-root + prefix-norm center，(4.1) **在考虑 repeated root 之前就已经成立**。

所以 external singular 子通道中：

\[
\boxed{
\text{single-branch repeated character}
=\text{external center character shadow}.}
\tag{4.2}

它不能被当成第二个独立 Legendre obstruction，更不能用“external 要 `(55/p)=1`，repeated 要 `C_*` nonsquare”制造伪矛盾；external center 本身已经要求 `C_*` nonsquare。

这与此前多次 `-23` / principal-square character 降级现象一致：真正要继续推进 external singular branch，必须使用 prime-power depth、decimal orbit 或 natural representative，而不是再堆一个等价的 quadratic character。

---

## 5. 当前结论

`C_*` 现在有三重统一解释：

1. two-prefix-branch resultant 的 central kernel；
2. single branch 上 `central factor × orientation factor`；
3. 原始 decimal 三元型
   \[
   23(BK)^2+81Q^2N_0.
   \]

而 external center 精确固定它的 square class。所以下一步若处理 generic non-external moving branch，可以继续研究 `C_*`；但在 external subchannel 中，其 quadratic character 已经耗尽，不应重复追逐。

---

<a id="source-spontaneous-denominator-common"></a>

> 整合来源：`spontaneous-denominator-common.md`

# A2 spontaneous/additive denominator common-carrier bridge

> **依赖：** `spontaneous-angle.md`、`spontaneous-angle-overlap-depth.md`、`spontaneous-angle-parity.md`、`spontaneous-prefix-eliminant.md`、`endpoint-lattice.md` §§16.56–16.72。
>
> **严格状态：**本文把 angle primitive carrier 与 additive cofactor 的 denominator pool 对齐。核心结论是：additive denominator odd excess 只能出现在完整 prime-power saturation `p^e || qf, p^e | L_23`；若同一个 prime 还属于 angle/additive common gcd，则它自动落回旧 denominator-prefix excess `Psi_f = Delta_0 = 0`。q-side 随即降为一个永远 simple 的 decimal-length quadratic；f-side 降为一个固定 octic，其 genuine non-3 inert singular Hensel tree 为空。本文不证明所有 simple common roots 都不存在，也不宣称 A2 全局关闭。

---

## 1. additive denominator odd excess 只剩完整 saturation

沿用 `endpoint-lattice.md` 的

\[
\mathscr L_{23}:=\frac{9T}{2}+a_3.
\]

旧共同-kernel 审计已经严格证明

\[
\gcd(\mathscr D_Z,qf)=\gcd(\mathscr L_{23}^2,qf),
\]
以及逐素数赋值律：若

\[
p^e\Vert qf,
\]
则

\[
\min\{v_p(\mathscr D_Z),e\}
=\min\{2v_p(\mathscr L_{23}),e\}.
\]

所以未饱和层全部以偶深度进入；non-`3` inert denominator prime 若要承担 additive odd excess，只能进入

\[
\boxed{
p^e\Vert qf,
\qquad
p^e\mid\mathscr L_{23}.}
\tag{1.1}
\]

因为 `p` 为奇素数，(1.1) 等价于

\[
\boxed{p^e\mid 2a_3+9T.}
\tag{1.2}
\]

本文从这个已经严格建立的 saturation 层开始，不重新收费未饱和 denominator contact。

---

## 2. `已严格完成`：common carrier 自动落回 `Psi_f`

记

\[
B=b_2,
\qquad
Q=2\cdot10^M+B,
\qquad
K=9\cdot10^M+10a_2,
\]

以及 pure f-prefix polynomial

\[
\boxed{
\Psi_f=B^2(K^2-26)-Q^2N_0.}
\tag{2.1}
\]

`spontaneous-prefix-eliminant.md` 已证明 exact identity

\[
\boxed{
\Theta_{\rm dec}
=T\Psi_f
-B^2(2K-9)(2a_3+9T).
}
\tag{2.2}
\]

现在设 genuine odd inert prime `p` 同时满足：

- denominator saturation (1.2)；
- additive contact `p | Theta_dec`。

由于 `p \nmid T`，(2.2) 模 `p` 立即给

\[
\boxed{p\mid\Psi_f.}
\tag{2.3}
\]

所以 additive denominator saturation 一旦真正进入 common gcd，就自动命中旧 denominator-prefix polynomial；没有新的第四种 denominator source。

---

## 3. `已严格完成`：angle denominator contact 自动落回 `Delta_0`

使用 normalized prefix variables

\[
x=\frac{B}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}},
\]
以及

\[
\boxed{
\Delta_0:=2025x^2-18y-y^2.}
\tag{3.1}
\]

### q-side

source formula 为

\[
q=\frac{U(x+2)}{2c_Q}.
\]
对 genuine q-prime，`U,2c_Q` 为单位，所以

\[
p\mid q\Longrightarrow x+2\equiv0\pmod p.
\]
`spontaneous-angle.md` 的 exact q-side identity 为

\[
\Omega_{\rm sp}(-2,y,r_s)=400r_s\Delta_0(-2,y).
\]
因此 genuine `p | q,Omega_sp` 给

\[
\boxed{p\mid\Delta_0.}
\tag{3.2q}
\]

### f-side

令

\[
F_f:=r_s(x+2)+2x.
\]
旧 exact Bezout identity 为

\[
\boxed{
(x+2)\Omega_{\rm sp}
-A_{\rm sp}F_f
=-200x^3\Delta_0.}
\tag{3.3}
\]

对 genuine `p | f`，`F_f=0` 且 `x(x+2)A_sp` 为单位，所以 `p | Omega_sp` 同样强迫

\[
\boxed{p\mid\Delta_0.}
\tag{3.2f}
\]

因此任何 denominator common carrier 必满足统一三重接触

\[
\boxed{
p\mid qf,
\qquad
p\mid\Psi_f,
\qquad
p\mid\Delta_0.}
\tag{3.4}
\]

这正是旧 denominator-prefix excess 与新的 angle/additive common gcd 的交界。

---

# q-side

## 4. `已严格完成`：q common overlap 只剩一个 decimal-length quadratic

令

\[
N:=10^M,
\qquad
\tau=N^{-1},
\qquad
s:=9+y.
\]

q-line 给

\[
x=-2\pmod p.
\tag{4.1}
\]

由 `Delta_0=0`：

\[
8100-18y-y^2=0,
\]
即

\[
\boxed{s^2=(y+9)^2=8181=3^4\cdot101.}
\tag{4.2}
\]

另一方面 q-line 上

\[
Q=N(x+2)\equiv0\pmod p.
\]
由 `Psi_f=0` 与 genuine `p \nmid B`：

\[
\boxed{K^2\equiv26\pmod p.}
\tag{4.3}
\]

而 exact decimal identity

\[
K=N(9+y)=Ns
\]
把 (4.2)–(4.3) 合成

\[
\boxed{
\mathcal R_q(N)
:=8181N^2-26
\equiv0\pmod p.}
\tag{4.4}
\]

所以 q-side saturated common overlap 的 length coordinate 已完全从 `x,y,r_s,a_3,b_3` 中消去。

---

## 5. `已严格完成`：q-side length root 对所有 genuine odd prime都 simple

\[
\mathcal R_q'(N)=2\cdot8181N.
\]

若某 odd prime同时满足

\[
\mathcal R_q(N)\equiv
\mathcal R_q'(N)\equiv0\pmod p,
\]
由于 `N=10^M` 为 `p`-进单位，只能有

\[
p\mid8181.
\]
但原方程随后要求

\[
p\mid26.
\]
而

\[
\gcd(8181,26)=1.
\]
矛盾。因此

\[
\boxed{
\text{q-side common length root 对每个 genuine odd prime 都是 simple。}}
\tag{5.1}
\]

不存在 q-side 新 singular decimal Hensel tree。

第一层还立即给两个 independent split conditions：`Delta_0` 的 y-discriminant 是

\[
18^2+4\cdot8100=324\cdot101,
\]
所以 genuine root 要求

\[
\boxed{\left(\frac{101}{p}\right)=1.}
\tag{5.2}
\]

而 (4.3) 要求

\[
\boxed{\left(\frac{26}{p}\right)=1.}
\tag{5.3}
\]

这些只是必要 character，不单独构成 closure。

---

# f-side

## 6. `已严格完成`：f-line、angle 与 saturation 显式固定第三块

f-line 为

\[
F_f=r_s(x+2)+2x=0.
\]
由

\[
r_s=\frac{x}{\bar w},
\qquad
\bar w:=\frac{b_3}{T10^M},
\]
得到

\[
\boxed{\bar w=-\frac{x+2}{2}.}
\tag{6.1}
\]

saturation (1.2) 在 normalized third numerator

\[
\bar\zeta:=\frac{a_3}{T10^M}
\]
中写成

\[
\boxed{2\bar\zeta+9\tau=0,
\qquad
\bar\zeta=-\frac92\tau.}
\tag{6.2}
\]

angle contact又给 `Delta_0=0`。

exact sphere 为

\[
x^2\bar w^2(s+\bar\zeta)^2
=(x+2+\bar w)^2
\left(
\frac{2025x^2+y^2}{100}\bar w^2
+x^2\bar\zeta^2
\right).
\tag{6.3}
\]

在 `Delta_0=0` 上

\[
2025x^2+y^2=2ys.
\tag{6.4}
\]

把 (6.1)–(6.4) 代入并约去 genuine units，得到线性 saturation sphere target

\[
\boxed{
\mathcal L_f^{\rm sat}
:=200x^2(s-9\tau)-y(x+2)^2
=0.}
\tag{6.5}
\]

另一方面 `Psi_f=0` 除以 `B^2N^2` 后是

\[
\boxed{
\mathcal P_f
:=100x^2(s^2-26\tau^2)
-(x+2)^2(2025x^2+y^2)
=0.}
\tag{6.6}
\]

所以 f-side common saturation 的第三块和 source ratio 已经完全消失，只剩

\[
\boxed{
\Delta_0=0,
\qquad
\mathcal L_f^{\rm sat}=0,
\qquad
\mathcal P_f=0.}
\tag{6.7}
\]

---

## 7. `已严格完成`：f-side 最终只剩一个固定 octic

先对 `tau` 消去 (6.5)–(6.6)，再对 `y` 与 `Delta_0` 消元。exact resultant 为

\[
\boxed{
\operatorname{Res}_y
\left(
\Delta_0,
\operatorname{Res}_{\tau}(\mathcal P_f,\mathcal L_f^{\rm sat})
\right)
=164025000000\,x^8\mathcal F_{f,\rm sat}(x),}
\tag{7.1}
\]

其中整体符号依 resultant convention 可改变，而 primitive octic 为

\[
\boxed{
\begin{aligned}
\mathcal F_{f,\rm sat}(x)={}&
1150871947369x^8
-233661590896x^7\\
&-130208799184x^6
+3933739968x^5\\
&-5129302560x^4
+594074368x^3\\
&+85765888x^2
+2675712x
+389376.
\end{aligned}}
\tag{7.2}
\]

因此 genuine `p \nmid 2\cdot3\cdot5\cdot x` 的 f-side common carrier 必满足

\[
\boxed{\mathcal F_{f,\rm sat}(x)\equiv0\pmod p.}
\tag{7.3}
\]

这把 denominator common overlap 从四变量系统降为一条固定 degree-8 prefix curve。

---

## 8. `有限 exact 证书`：真实 endpoint interval 内没有 octic root

真实 denominator defect 为

\[
u:=10x-1=\frac{H}{5^{M-1}},
\qquad
0<u<\frac1{19}.
\]

令

\[
\mathcal F_{H,\rm sat}(u)
:=10^8\mathcal F_{f,\rm sat}\left(\frac{1+u}{10}\right).
\]

Sturm exact root count 给

\[
\boxed{
\#\{u\in(0,1/19):\mathcal F_{H,\rm sat}(u)=0\}=0.}
\tag{8.1}
\]

而两个端点函数值均为正。因此 f-side common overlap 与此前其它 moving branches 一样，没有 Archimedean root；任何 surviving state 都只能来自真正的 p-adic wrapping。

---

## 9. `有限 exact 证书`：f-side common octic 没有 genuine inert singular root

其整数判别式精确分解为

\[
\boxed{
\begin{aligned}
\operatorname{Disc}(\mathcal F_{f,\rm sat})={}&
2^{114}3^{20}5^{22}11^6 13^3 41^4 101^8 181^2\\
&\cdot5927^2\cdot197377693^2\cdot326937937\cdot1484772181.
\end{aligned}}
\tag{9.1}
\]

所有显示的大因子均为素数。限制到 non-`3` inert primes `p=3 mod 4`，只有

\[
\boxed{p=11,\ 5927}
\tag{9.2}
\]
需要审计。

### p=11

\[
\gcd(\mathcal F_{f,\rm sat},\mathcal F_{f,\rm sat}')
\equiv(x+2)^3\pmod{11}.
\]
唯一 repeated x-root 是

\[
x=-2.
\]
但 f-line 在该点为

\[
F_f=r_s(x+2)+2x=-4\not\equiv0\pmod{11}.
\]
所以它是 q-boundary，不是 genuine f-state。

### p=5927

`5927` 整除 octic leading coefficient，故判别式因 degree drop 含该素数；但有限域中

\[
\boxed{
\gcd(\mathcal F_{f,\rm sat},\mathcal F_{f,\rm sat}')=1
\quad\text{in }\mathbf F_{5927}[x].}
\tag{9.3}
\]

所以没有 finite repeated root。

因此

\[
\boxed{
\text{f-side saturated common overlap 不存在 genuine non-3 inert singular Hensel tree。}}
\tag{9.4}
\]

所有 genuine f-side common roots 都是 simple moving roots。

---

## 10. denominator parity 图的更新

现在 additive 与 angle 的 denominator pools 已对齐到同一旧接口：

\[
\boxed{
\text{saturated additive denominator}
+\text{angle contact}
\Longrightarrow
qf\cap\Psi_f\cap\Delta_0.}
\tag{10.1}
\]

并且 common part 的局部几何已经完全正规化：

\[
\boxed{
\begin{array}{c|c|c}
\text{channel}&\text{common reduced object}&\text{singular tree}\\ \hline
q&8181\cdot10^{2M}-26&\text{none}\\
f&\mathcal F_{f,\rm sat}(x)&\text{none genuine inert}
\end{array}}
\tag{10.2}
\]

所以 denominator pool 后续不应再做 singular-prime hunting。真正未闭合的是 **simple depth/parity synchronization**：比较

\[
\min\{v_p(\Omega_{\rm sp}),e\}
=\min\{v_p(\Delta_0),e\}
\]
与 additive saturation 的

\[
\min\{v_p(\mathscr D_Z),e\}
=\min\{2v_p(\mathscr L_{23}),e\},
\]
其中 `p^e || qf`。若能证明 simple q/f roots 的 residual parity 在两侧相同，或其差总为偶数，就可从 `G_sp mod 4` dichotomy 中消去 denominator residual branch。本文尚未证明这一最后 parity equality。

---

<a id="source-spontaneous-denominator-depth-matrix"></a>

> 整合来源：`spontaneous-denominator-depth-matrix.md`

# A2 denominator parity 的纯 prefix depth matrix

> **依赖：** `spontaneous-angle-overlap-depth.md`、`spontaneous-denominator-common.md`、`endpoint-lattice.md` §§16.56、16.68–16.70。
>
> **严格状态：**本文把 angle/additive 两侧的 denominator prime-power depth 统一降成三个 pure-prefix objects：`Delta_0`、`P_q(K)=K^2-26`、`P_f(K)=3K^2-36K+26`。q-side additive reduction来自旧 (16.412q)；f-side在旧 `Psi_f` reduction基础上进一步使用真实 sphere，把 `Psi_f` 也降成固定 K-quadratic。两个 additive quadratics 对所有 genuine non-3 inert prime 都是 simple-root。本文还给出 q-side 的 exact decimal-length三项 bridge，并审计 common channel 上旧 residual Legendre characters 都只是 sphere-square shadow。最后的 parity equality 尚未证明，所以 A2 仍未全局关闭。

---

## 1. angle side：denominator 截断深度统一由 `Delta_0` 读取

设 genuine non-`3` inert prime

\[
p^e\Vert qf,
\qquad e\ge1.
\]

`spontaneous-angle-overlap-depth.md` 已证明：

### q-side

因为

\[
v_p(q)=v_p(x+2)=e,
\]
且

\[
\Omega_{\rm sp}
=400r_s\Delta_0+(x+2)J_q,
\]
共同 first-layer root 上 `J_q` 为单位，所以

\[
\boxed{
\min\{v_p(\Omega_{\rm sp}),e\}
=
\min\{v_p(\Delta_0),e\}.}
\tag{1.1q}
\]

### f-side

由 exact Bezout

\[
(x+2)\Omega_{\rm sp}-A_{\rm sp}F_f
=-200x^3\Delta_0,
\]
以及

\[
v_p(F_f)=v_p(f)=e,
\]
得到

\[
\boxed{
\min\{v_p(\Omega_{\rm sp}),e\}
=
\min\{v_p(\Delta_0),e\}.}
\tag{1.1f}
\]

对 genuine denominator prime，`Omega_sp` 与 primitive integer `widehat(O)_sp` 只差 odd p-adic unit 和固定 2-power，因此可以统一写成

\[
\boxed{
\min\{v_p(\widehat{\mathcal O}_{\rm sp}),e\}
=
\min\{v_p(\Delta_0),e\}.}
\tag{1.2}
\]

也就是说 angle denominator projection 与 q/f 来源无关：两侧都只读同一个 prefix defect `Delta_0`。

---

## 2. additive q-side：旧 saturation reduction 已经是固定 quadratic

定义

\[
\boxed{\mathcal P_q(K):=K^2-26.}
\tag{2.1}
\]

`endpoint-lattice.md` (16.412q) 已严格证明，在完整 saturation

\[
p^e\Vert q,
\qquad
p^e\mid\mathscr L_{23}
\]
下：

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),e\}
=
\min\{v_p(\mathcal P_q(K)),e\}.}
\tag{2.2}
\]

所以 q-side additive denominator depth 已完全 source-free。

其 discriminant 为

\[
\operatorname{Disc}(\mathcal P_q)=104=2^3\cdot13.
\tag{2.3}
\]

唯一 odd ramified prime `13` 为 `1 mod 4`。故

\[
\boxed{
\text{对 genuine non-3 inert prime，q-side additive K-root 永远 simple。}}
\tag{2.4}

---

## 3. `已严格完成`：f-side sphere 在完整 saturation 深度内产生第二个固定 quadratic

旧 (16.408) 已有

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),e\}
=
\min\{v_p(\Psi_f),e\}
\qquad
(p^e\Vert f,\ p^e\mid\mathscr L_{23}).}
\tag{3.1}

现在进一步消去 `Psi_f`。

使用 normalized variables

\[
x=B/N,
\quad y=a_2/10^{M-1},
\quad \tau=N^{-1},
\quad s=K/N,
\]

\[
\bar w=b_3/(TN),
\qquad
\bar\zeta=a_3/(TN),
\]
其中 `N=10^M`。

对 `p^e || f`，source exact line 给

\[
2\bar w+x+2\equiv0\pmod{p^e}.
\tag{3.2}

saturation 给

\[
2\bar\zeta+9\tau\equiv0\pmod{p^e}.
\tag{3.3}

把 exact sphere 的 cleared polynomial记为

\[
\begin{aligned}
\mathscr S_{100}:={}&100x^2\bar w^2(s+\bar\zeta)^2\\
&-(x+2+\bar w)^2
\left[(2025x^2+y^2)\bar w^2+100x^2\bar\zeta^2\right].
\end{aligned}
\tag{3.4}
\]

真实 solution 满足 `S_100=0`。在多项式环 `Z[1/2][x,y,tau,w,z]` 中，对两个线性 ideal generators

\[
2\bar w+x+2,
\qquad
2\bar\zeta+9\tau
\]
取余，得到

\[
\boxed{
16\mathscr S_{100}
\equiv
(x+2)^2\mathscr R_f^{\rm sph}
\pmod{(2\bar w+x+2,\,2\bar\zeta+9\tau)},}
\tag{3.5}
\]

其中

\[
\boxed{
\mathscr R_f^{\rm sph}
:=400x^2s(s-9\tau)
-(2025x^2+y^2)(x+2)^2.}
\tag{3.6}

对 genuine f-prime，`2(x+2)` 为单位；由 (3.2)–(3.5)：

\[
\boxed{p^e\mid\mathscr R_f^{\rm sph}.}
\tag{3.7}

乘回原始 decimal blocks，(3.6) 与

\[
\mathscr R_{f,\rm int}^{\rm sph}
:=4B^2K(K-9)-Q^2N_0
\]
只差 p-adic unit `100/N^4`，故

\[
\boxed{
p^e\mid
\left[Q^2N_0-4B^2K(K-9)\right].}
\tag{3.8}

---

## 4. `已严格完成`：f-side `Psi_f` 截断深度等于固定 quadratic 深度

定义

\[
\boxed{
\mathcal P_f(K):=3K^2-36K+26.}
\tag{4.1}

存在 exact integer identity

\[
\boxed{
\Psi_f
+\left[Q^2N_0-4B^2K(K-9)\right]
=-B^2\mathcal P_f(K).}
\tag{4.2}

因为 genuine f-prime 满足 `p \nmid B`，结合 (3.8)：

\[
\boxed{
\min\{v_p(\Psi_f),e\}
=
\min\{v_p(\mathcal P_f(K)),e\}.}
\tag{4.3}

再与旧 (3.1) 合并：

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),e\}
=
\min\{v_p(\mathcal P_f(K)),e\}
\qquad
(p^e\Vert f,\ p^e\mid\mathscr L_{23}).}
\tag{4.4}

所以 f-side additive denominator depth 也彻底变成 pure K-quadratic；`Psi_f` 只保留为旧接口，不再是最终规范对象。

其 discriminant 为

\[
\boxed{
\operatorname{Disc}(\mathcal P_f)
=984=2^3\cdot3\cdot41.}
\tag{4.5}

唯一 non-`3` odd ramified prime `41` 为 `1 mod 4`。因此

\[
\boxed{
\text{对 genuine non-3 inert prime，f-side additive K-root 永远 simple。}}
\tag{4.6}

---

## 5. denominator depth matrix

综合 §§1–4，完整 saturation 内的规范对象只有

\[
\boxed{
\begin{array}{c|cc}
&\text{angle side}&\text{additive side}\\ \hline
q&\Delta_0&\mathcal P_q(K)=K^2-26\\[1mm]
f&\Delta_0&\mathcal P_f(K)=3K^2-36K+26.
\end{array}}
\tag{5.1}

逐 prime-power 截断赋值为

\[
\boxed{
\begin{aligned}
a_p&:=\min\{v_p(\widehat{\mathcal O}_{\rm sp}),e\}
=\min\{v_p(\Delta_0),e\},\\
t_p^{(q)}&:=\min\{v_p(\widehat{\mathcal T}_2),e\}
=\min\{v_p(\mathcal P_q(K)),e\},\\
t_p^{(f)}&:=\min\{v_p(\widehat{\mathcal T}_2),e\}
=\min\{v_p(\mathcal P_f(K)),e\}.
\end{aligned}}
\tag{5.2}

因此 denominator residual parity 已不再依赖 source ratios、third-block Hensel roots 或 curvature discriminants；它只取决于 `Delta_0` 与两个 simple K-roots 的 depth difference。

---

## 6. `已严格完成`：q-side depth mismatch 被一个 simple decimal-length target控制

有 exact identity

\[
\boxed{
\mathcal P_q(K)+N^2\Delta_0
-\left(8181N^2-26\right)
=Q(2025Q-8100N).}
\tag{6.1}

证明只需使用

\[
K=N(9+y),
\qquad
Q=N(x+2).
\]

若 `p^e || q` 且 genuine `p \nmid c_Q`，则

\[
v_p(Q)=e.
\]
所以模 `p^e`：

\[
\boxed{
\mathcal P_q(K)+N^2\Delta_0
\equiv
\mathcal R_q(N)
:=8181N^2-26
\pmod{p^e}.}
\tag{6.2}

`N^2` 是平方单位。于是令

\[
a=v_p(\mathcal P_q),
\quad d=v_p(\Delta_0),
\quad r=v_p(\mathcal R_q),
\]
并截断到 `e` 后，三者满足 ultrametric triangle：若最小深度小于 `e`，它不可能只出现一次。

特别地：

\[
\boxed{
\begin{aligned}
a<d,\ a<e&\Longrightarrow r=a,\\
d<a,\ d<e&\Longrightarrow r=d.
\end{aligned}}
\tag{6.3}

所以 q-side angle/additive depth 若不相等，较浅的那个 depth 必精确出现在 fixed decimal-length integer `R_q(N)` 中。

而

\[
\mathcal R_q'(N)=2\cdot8181N,
\qquad
\gcd(8181,26)=1,
\]
已证明 `R_q` 对所有 genuine odd prime 都没有 repeated root。因此 q-side parity mismatch 也只能沿 simple decimal-length Hensel orbit 传播，不存在新的 singular length tree。

---

## 7. `审计 / no-go`：common q-character 是 sphere-square shadow

若同一个 saturated q-prime还属于 angle common channel，则

\[
x=-2,
\qquad
\Delta_0=0,
\qquad
\bar\zeta=-\frac92\tau.
\]

在 exact sphere 中，`x+2=0` 后直接得到

\[
(2025x^2+y^2)\bar w^2
=400s(s-9\tau).
\]
乘回 `N_0=N^2(2025x^2+y^2)/100`：

\[
\boxed{
N_0\bar w^2
=4K(K-9)
\pmod p.}
\tag{7.1}

因此

\[
\boxed{
\left(\frac{N_0}{p}\right)
=
\left(\frac{K(K-9)}p\right).}
\tag{7.2}

这正是 `endpoint-lattice.md` (16.384) 的 q-side residual-unit character。也就是说一旦 prime 已进入 angle/additive common sphere，旧 q-character 自动由 square identity (7.1) 满足；它不能再被计作 independent obstruction。

---

## 8. `审计 / no-go`：common f-character 同样自动

对 saturated f-common prime，§3 的 sphere congruence给

\[
Q^2N_0
\equiv4B^2K(K-9).
\]
所以

\[
\boxed{
\left(\frac{N_0}{p}\right)
=
\left(\frac{K(K-9)}p\right).}
\tag{8.1}

而 additive f-root `P_f(K)=0` 等价于

\[
\boxed{K^2-26=4K(K-9).}
\tag{8.2}

因此

\[
\boxed{
\left(\frac{K^2-26}{p}\right)
=
\left(\frac{N_0}{p}\right).}
\tag{8.3}

这正是旧 (16.396) 的 generic f-prefix character。故 f-common channel 中该 character 也只是 sphere-square shadow。

结论与 q-side 一致：**不能再靠叠加旧 denominator Legendre characters 关闭 common branch。** 真正剩余的是 prime-power depth equality / decimal orbit，而不是 first-layer quadratic character。

---

## 9. 对 `G_sp` parity dichotomy 的更新

`spontaneous-angle-parity.md` 的 residual denominator 问题现在可以精确改写为：对每个 saturated inert primary `p^e || qf`，比较

\[
\boxed{
\min(v_p(\Delta_0),e)
}

与

\[
\boxed{
\begin{cases}
\min(v_p(K^2-26),e),&p\mid q,\\
\min(v_p(3K^2-36K+26),e),&p\mid f.
\end{cases}}
\tag{9.1}

三个对象的 genuine inert roots全部 simple。repeated spontaneous 与 saturated denominator 的交集又已经由 `spontaneous-denominator-repeated-common.md` 关闭。

因此 denominator pool 现在只剩一个真正开放机制：

\[
\boxed{
\text{simple-root depth mismatch / equal-depth normalized cancellation}.}
\tag{9.2}

若后续能证明 (9.1) 两侧的 parity difference 对所有 denominator primary 都为偶，则 `G_sp = 1 mod 4` 分支中的 residual odd supplier 将不能来自 denominator pool；届时只剩 `spontaneous-source-equal-depth.md` 的 source normalized gate 与 pure spontaneous external channel。

---

<a id="source-spontaneous-denominator-depth-residuals"></a>

> 整合来源：`spontaneous-denominator-depth-residuals.md`

# A2 denominator depth mismatch 的两个 simple residual

> **依赖：** `spontaneous-denominator-depth-matrix.md`。
>
> **严格状态：**denominator depth matrix 已把 angle/additive 两侧分别降成 `Delta_0` 与两个 K-quadratic。本文继续证明：q/f 两侧若出现 depth mismatch，较浅深度必须精确落在一个额外的 simple residual 上。q residual 只依赖 decimal length `N=10^M`；f residual只依赖前缀平方量 `A_pref=2025b_2^2+81N^2`。两个 residual 对所有 genuine non-3 inert prime 都无 repeated root。本文同时审计其 quadratic characters，证明它们与旧 additive roots 位于同一个 quadratic extension，因此 character stacking 是 no-go。本文仍不证明 simple-root depth mismatch 不存在，也不宣称 A2 全局关闭。

---

## 1. 统一整数 prefix defect

令

\[
N:=10^M,
\qquad
B:=b_2,
\qquad
K:=9N+10a_2.
\]

因为

\[
x=B/N,
\qquad
s=9+y=K/N,
\]
定义

\[
\boxed{
A_{\rm pref}:=2025B^2+81N^2.}
\tag{1.1}
\]

则

\[
\boxed{
D_{\rm pref}:=N^2\Delta_0
=A_{\rm pref}-K^2.}
\tag{1.2}

对 genuine odd prime，`N` 为单位，所以

\[
\boxed{v_p(D_{\rm pref})=v_p(\Delta_0).}
\tag{1.3}

这允许直接在整数环中比较 angle defect 与 additive K-root 的深度。

---

# q-side

## 2. q residual 是纯 decimal-length quadratic

定义

\[
\boxed{
P_q(K):=K^2-26,}
\tag{2.1}

\[
\boxed{
R_q(N):=8181N^2-26.}
\tag{2.2}

又有

\[
Q=B+2N.
\]

直接展开得到 exact identity

\[
\boxed{
P_q(K)+D_{\rm pref}-R_q(N)
=2025Q(B-2N).}
\tag{2.3}

等价地

\[
P_q(K)+N^2\Delta_0-R_q(N)
=Q(2025Q-8100N).
\]

若

\[
p^e\Vert q
\]
且属于 generic q-denominator layer `p∤c_Q`，则

\[
v_p(Q)=e.
\]
因此模 `p^e`：

\[
\boxed{P_q(K)+D_{\rm pref}\equiv R_q(N)\pmod{p^e}.}
\tag{2.4}

令

\[
a=v_p(P_q),
\qquad d=v_p(D_{\rm pref}),
\qquad r=v_p(R_q).
\]

如果最小深度严格小于 `e`，ultrametric law 立即给

\[
\boxed{
\begin{aligned}
a<d,\ a<e&\Longrightarrow r=a,\\
d<a,\ d<e&\Longrightarrow r=d.
\end{aligned}}
\tag{2.5}

所以 q-side angle/additive depth mismatch 的较浅一侧，必须以完全相同的深度出现在 `R_q` 中。

---

## 3. q residual 对所有 genuine odd prime 都 simple

\[
R_q'(N)=2\cdot8181N.
\]

若 odd prime同时使 `R_q=R_q'=0`，因为 `N` 为单位，只能

\[
p\mid8181.
\]
原方程又要求 `p|26`，与

\[
\gcd(8181,26)=1
\]
矛盾。因此

\[
\boxed{R_q\text{ 在任意 genuine odd prime 上没有 repeated root。}}
\tag{3.1}

q-side depth mismatch 只能沿唯一 simple decimal-length Hensel lift传播。

---

# f-side

## 4. f residual 只依赖 `A_pref`

定义 additive quadratic

\[
\boxed{P_f(K):=3K^2-36K+26.}
\tag{4.1}

由 (1.2)：

\[
P_f(K)+3D_{\rm pref}
=3A_{\rm pref}-36K+26.
\tag{4.2}

记

\[
C_f:=3A_{\rm pref}+26,
\]
以及

\[
\boxed{
R_f^{\rm len}(A_{\rm pref})
:=C_f^2-1296A_{\rm pref}
=9A_{\rm pref}^2-1140A_{\rm pref}+676.}
\tag{4.3}

有 exact Bezout identity

\[
\boxed{
R_f^{\rm len}
=
\bigl(P_f+3D_{\rm pref}\bigr)
\bigl(C_f+36K\bigr)
-1296D_{\rm pref}.}
\tag{4.4}

展开为关于两个 depth objects 的形式：

\[
\boxed{
R_f^{\rm len}
=P_fU_f+D_{\rm pref}V_f,}
\tag{4.5}

其中

\[
U_f:=C_f+36K,
\qquad
V_f:=3U_f-1296.
\tag{4.6}

---

## 5. common f-root 上两个 Bezout 系数都是单位

在 first-layer common root

\[
P_f\equiv0,
\qquad
D_{\rm pref}\equiv0
\pmod p,
\]
有

\[
A_{\rm pref}\equiv K^2.
\]
由 `P_f=0`：

\[
3K^2+26\equiv36K.
\]
所以

\[
\boxed{U_f\equiv72K\pmod p.}
\tag{5.1}

如果 `p|K`，`P_f(0)=26` 强迫 `p|26`，没有 genuine non-3 inert prime。故 `U_f` 为单位。

另一方面

\[
\boxed{V_f\equiv216(K-6)\pmod p.}
\tag{5.2}

若 `p|K-6`，则

\[
P_f(6)=-82=-2\cdot41,
\]
所以唯一 odd candidate 是 `41`，而

\[
41\equiv1\pmod4.
\]
因此对 genuine non-3 inert prime，`V_f` 也是单位。

于是令

\[
a=v_p(P_f),
\qquad d=v_p(D_{\rm pref}),
\qquad r=v_p(R_f^{\rm len}).
\]
由 (4.5)：

\[
\boxed{
\begin{aligned}
a<d&\Longrightarrow r=a,\\
d<a&\Longrightarrow r=d.
\end{aligned}}
\tag{5.3}

若两者等深，才可能因 normalized cancellation 使 residual 更深。

所以 f-side depth mismatch 也被一个低次 residual 精确承接，而不需要使用 `spontaneous-denominator-common.md` 的完整 octic。

---

## 6. f residual 同样没有 genuine inert repeated root

把 `R_f^{len}` 看成 `A_pref` 的 quadratic：

\[
9A^2-1140A+676.
\]
其判别式为

\[
\boxed{
\begin{aligned}
\operatorname{Disc}_A(R_f^{\rm len})
&=1140^2-4\cdot9\cdot676\\
&=1275264\\
&=2^7\cdot3^5\cdot41\\
&=72^2\cdot246.
\end{aligned}}
\tag{6.1}

唯一 non-`3` odd ramified prime仍是 `41=1 mod4`。因此

\[
\boxed{
R_f^{\rm len}\text{ 对所有 genuine non-3 inert prime 都只有 simple root。}}
\tag{6.2}

结合 §5，f-side parity mismatch 同样只能沿 simple Hensel orbit传播。

---

## 7. 两个 channel 的 residual 表

因此 denominator depth matrix 可进一步扩展为

\[
\boxed{
\begin{array}{c|c|c|c}
&\text{angle}&\text{additive}&\text{mismatch residual}\\ \hline
q&D_{\rm pref}&P_q(K)=K^2-26&R_q(N)=8181N^2-26\\[1mm]
f&D_{\rm pref}&P_f(K)=3K^2-36K+26&R_f^{\rm len}(A_{\rm pref})
\end{array}}
\tag{7.1}

三个 additive/residual polynomial 在 genuine non-3 inert primes 上全都 simple。

因此 denominator pool 中已经没有任何需要继续追踪的 singular polynomial tree。剩余自由只可能是：

1. 两个 simple depths 恰好相等后的 normalized cancellation；
2. 两个 simple roots沿 decimal/source orbit同步提升。

---

## 8. `审计 / no-go`：f residual 没有新的 quadratic character

additive f quadratic 的判别式为

\[
\operatorname{Disc}_K(P_f)=984=4\cdot246.
\tag{8.1}

而 (6.1) 给

\[
\operatorname{Disc}_{A}(R_f^{\rm len})=72^2\cdot246.
\tag{8.2}

因此两种 root 的 quadratic field完全相同：

\[
\boxed{
P_f\text{ has a simple root mod }p
\iff
R_f^{\rm len}\text{ 的 discriminant square class也是 }246.}
\tag{8.3}

所以从 residual 再提取

\[
\left(\frac{246}{p}\right)=1
\]
不是新 obstruction，而是同一个 quadratic extension 的影子。

q-side同样如此：

\[
R_q=0
\Longrightarrow
8181N^2=26,
\]
而 `8181=81*101`；其 character正是旧 common q-system 中 `(101/p)` 与 `(26/p)` 的组合，没有独立新信息。

结论：后续不得再沿 denominator residual 做 Legendre/Jacobi stacking。真正的前沿是 simple-root **depth synchronization**。

---

## 9. 当前 denominator 开放核

结合 `spontaneous-denominator-repeated-common.md`：repeated spontaneous 与 saturated denominator common 已没有 surviving unbounded Hensel branch。

本文又证明所有 depth-mismatch residual 都是 simple。因此 denominator residual odd parity 的最后规范形态是

\[
\boxed{
\text{simple }D_{\rm pref}\text{ root}
\quad\leftrightarrow\quad
\text{simple }P_q/P_f\text{ root}
\quad\leftrightarrow\quad
\text{simple }R_q/R_f\text{ root}.}
\tag{9.1}

下一步如果继续 denominator parity，应研究这些 simple roots 的**相对 Hensel derivative / decimal-orbit synchronization**，而不是再求 discriminant或 singular bad primes。若能证明每个 denominator primary 上 angle/additive depth差恒为偶数，就能从 `G_sp mod4` dichotomy 中完全删除 denominator residual supplier。

---

<a id="source-spontaneous-denominator-repeated-common"></a>

> 整合来源：`spontaneous-denominator-repeated-common.md`

# A2 repeated spontaneous 与 saturated additive denominator 的交集

> **依赖：** `spontaneous-tangent-decimal.md`、`spontaneous-denominator-common.md`、`endpoint-lattice.md` §§16.56–16.70。
>
> **严格状态：**本文处理最危险的交界：同一个 genuine non-`3` inert prime 一方面使 spontaneous branch 在真实 decimal length 上 repeated，另一方面又承担 additive denominator saturation。结论是 q-side 第一层即为空；f-side 只出现固定 prime `523` 的一个 genuine 第一层模板，但该模板不能提升到 `523^2`。因此 repeated spontaneous 与 saturated additive denominator 不存在 surviving unbounded Hensel tree。本文不排除 simple spontaneous/denominator common roots，也不宣称 A2 全局关闭。

---

## 1. repeated + saturation 固定唯一 K-center

`spontaneous-tangent-decimal.md` 的原始 repeated tangent 是

\[
\boxed{
L_{\rm tan}=9(TK-a_3)-55T.}
\tag{1.1}
\]

additive denominator odd excess 只有完整 saturation

\[
\boxed{p^e\Vert qf,
\qquad
p^e\mid 2a_3+9T.}
\tag{1.2}
\]

在第一层，把

\[
a_3/T\equiv-9/2
\]
代入 `L_tan=0`：

\[
9\left(K+\frac92\right)-55=0.
\]
所以任何 repeated+saturated common candidate 都必须满足

\[
\boxed{18K-29\equiv0\pmod p.}
\tag{1.3}
\]

这条线与此前 `Psi_f` 子通道出现的 `18K-29` 相同，但本文不假设 `Psi_f` 作为额外输入；它直接来自 repeated tangent 与 saturation。

---

# 2. f-saturation 本身还有一个此前未显式使用的 sphere quadratic

设 `p|f` 且进入 additive saturation。使用 normalized

\[
x=\frac{b_2}{10^M},
\quad
\tau=10^{-M},
\quad
s=9+y,
\]

\[
\bar w=\frac{b_3}{T10^M},
\qquad
\bar\zeta=\frac{a_3}{T10^M}.
\]

f-line 给

\[
\bar w\equiv-\frac{x+2}{2},
\tag{2.1}
\]
而 saturation 给

\[
\bar\zeta\equiv-\frac92\tau.
\tag{2.2}
\]

把 (2.1)–(2.2) 直接代入 exact sphere，不使用 `Omega_sp=0`，得到

\[
(2025x^2+y^2)(x+2)^2
\equiv
400x^2s(s-9\tau)
\pmod p.
\tag{2.3}
\]

乘回原始 decimal blocks

\[
B=b_2=Nx,
\qquad
Q=N(x+2),
\qquad
K=Ns,
\qquad N=10^M,
\]
以及

\[
N_0=\frac{N^2}{100}(2025x^2+y^2),
\]
(2.3) 精确化为 first-layer congruence

\[
\boxed{
Q^2N_0
\equiv
4B^2K(K-9)
\pmod p.}
\tag{2.4}

另一方面 saturation 与 additive contact 已由 `spontaneous-denominator-common.md` 给

\[
\Psi_f
=B^2(K^2-26)-Q^2N_0
\equiv0\pmod p.
\tag{2.5}

代入 (2.4)：

\[
K^2-26-4K(K-9)=0,
\]
即

\[
\boxed{
\mathcal P_f(K)
:=3K^2-36K+26
\equiv0\pmod p.}
\tag{2.6}

所以每个 saturated additive f-carrier 在 first layer 都落在一个固定 quadratic 上；source variables、third block 和 Gaussian allocation 全部消失。

其判别式为

\[
\boxed{
\operatorname{Disc}(\mathcal P_f)
=36^2-12\cdot26
=984=2^3\cdot3\cdot41.}
\tag{2.7}

因此 genuine non-`3` inert prime `p=3 mod 4` 不可能使 `P_f` 出现 repeated root：唯一 odd ramified prime `41` 满足

\[
41\equiv1\pmod4.
\]

于是

\[
\boxed{
\text{所有 genuine inert saturated f-carrier 的 K-root 都 simple。}}
\tag{2.8}

---

## 3. `审计 / no-go`：旧 f-prefix character 在该 quadratic 上自动成立

(2.6) 等价于

\[
\boxed{K^2-26=4K(K-9).}
\tag{3.1}

而 sphere identity (2.4) 已给

\[
\left(\frac{N_0}{p}\right)
=\left(\frac{K(K-9)}p\right)
\tag{3.2}
\]
对 genuine units 成立。

旧 f-saturation prefix character 是

\[
\left(\frac{K^2-26}{p}\right)
=\left(\frac{N_0}{p}\right).
\tag{3.3}

由 (3.1)，两边之比就是 `4`，所以 (3.3) 在 common sphere quadratic 上自动成立。它是 principal-square shadow，不是第二个 independent obstruction。

因此后续不能再尝试用旧 f-prefix Legendre character 排除 (2.6) 的 roots。

---

# 4. q-side repeated+saturated common 第一层为空

q-side additive saturation 已有 pure prefix root

\[
\boxed{K^2-26\equiv0\pmod p.}
\tag{4.1}

与 repeated center (1.3) 联立，把

\[
K=\frac{29}{18}
\]
代入：

\[
K^2-26
=-\frac{7583}{324}.
\]

`7583` 为素数且

\[
7583\equiv3\pmod4.
\]
所以唯一 genuine inert candidate 是

\[
\boxed{p=7583.}
\tag{4.2}

但 q-angle contact 还必须满足 `x=-2, Delta_0=0`。由

\[
\Delta_0(-2,y)=8100-18y-y^2,
\]
其 discriminant 为

\[
324\cdot101.
\]
故 first-layer y-root 必须满足

\[
\left(\frac{101}{p}\right)=1.
\tag{4.3}

对 `p=7583`，因为 `101=1 mod 4`，二次互反律给

\[
\left(\frac{101}{7583}\right)
=
\left(\frac{7583}{101}\right)
=\left(\frac8{101}\right).
\]
而 `101=5 mod 8`，所以

\[
\left(\frac2{101}\right)=-1,
\qquad
\left(\frac8{101}\right)=-1.
\]
与 (4.3) 矛盾。因此

\[
\boxed{
\text{repeated spontaneous}\cap q\text{-saturation common}
=\varnothing
\quad\text{already mod }p.}
\tag{4.4}

---

# 5. f-side 只剩固定 p=523

将 repeated center

\[
K=29/18
\]
代入 f-sphere quadratic (2.6)：

\[
\mathcal P_f(29/18)
=-\frac{2615}{108}
=-\frac{5\cdot523}{108}.
\]

对 genuine non-`5` inert prime，唯一候选为

\[
\boxed{p=523.}
\tag{5.1}

并且

\[
523\equiv3\pmod4.
\]

所以 repeated+saturated f-common shell 已从任意 moving prime 压成一个 fixed prime。

---

## 6. `有限 exact 证书`：p=523 恰有一个 genuine first-layer state

使用 f-side common system

\[
\Delta_0=0,
\]

\[
\mathcal L_f^{\rm sat}
=200x^2(s-9\tau)-y(x+2)^2=0,
\]

\[
\mathcal P_f^{\rm pref}
=100x^2(s^2-26\tau^2)
-(x+2)^2(2025x^2+y^2)=0,
\]
再加入 repeated center

\[
18s-29\tau=0.
\]

在 `F_523` 中完整枚举得到唯一 genuine solution

\[
\boxed{(x,y,\tau)=(115,215,121)\pmod{523}.}
\tag{6.1}

对应

\[
\boxed{
\begin{aligned}
x+2&=117,\\
s=9+y&=224,\\
2025x^2+y^2&=88,\\
A_{\rm sp}&=509,
\end{aligned}
\qquad\pmod{523}}
\tag{6.2}

全部为单位。恢复 third/source normalized values：

\[
r_s=-\frac{2x}{x+2}=302,
\qquad
\bar w=203,
\qquad
\bar\zeta=-\frac92\tau=240
\pmod{523},
\]
也全部为 genuine units。

---

## 7. `有限 exact 证书`：唯一 p=523 state 无 p^2 lift

记四个整数多项式

\[
F_1=\Delta_0,
\]

\[
F_2=\mathcal L_f^{\rm sat},
\]

\[
F_3=\mathcal P_f^{\rm pref},
\]

\[
F_4=18s-29\tau.
\]

在 first-layer point

\[
(x_0,y_0,\tau_0)=(115,215,121)
\]
写

\[
x=x_0+523X,
\quad
y=y_0+523Y,
\quad
\tau=\tau_0+523Z.
\]

模 `523^2` 的必要条件是 augmented linear system

\[
J(x_0,y_0,\tau_0)
\begin{pmatrix}X\\Y\\Z\end{pmatrix}
\equiv
-\begin{pmatrix}
F_1/p\\F_2/p\\F_3/p\\F_4/p
\end{pmatrix}
\pmod{523}.
\tag{7.1}

exact row reduction 得到最后一行

\[
\boxed{[0\ \ 0\ \ 0\mid27].}
\tag{7.2}

因为 `27 != 0 mod 523`，系统不相容。因此

\[
\boxed{
\text{唯一 genuine }523\text{-state 不存在 }523^2\text{ lift}.}
\tag{7.3}

---

## 8. repeated denominator/common shell 已关闭

综合 §§4–7：

\[
\boxed{
\begin{array}{c|c|c}
\text{channel}&\text{first-layer candidate}&\text{higher lift}\\ \hline
q&7583&\text{first layer already impossible}\\
f&523&\text{unique state, no }523^2\text{ lift}
\end{array}}
\tag{8.1}

所以

\[
\boxed{
\text{repeated spontaneous}
\cap
\text{saturated additive denominator}
\text{ has no surviving unbounded Hensel branch}.}
\tag{8.2}

这真正删除了一类 singular common carrier。剩余 denominator parity problem 只涉及 **simple q/f roots** 与 equal-depth normalized cancellation；后续不应再保留 repeated decimal branch 作为 denominator common 的无界机制。

---

<a id="source-spontaneous-fixed11-audit"></a>

> 整合来源：`spontaneous-fixed11-audit.md`

# A2 pure-spontaneous 固定 `p=11` 审计

> **依赖：** `spontaneous-prefix-boundaries.md`、`spontaneous-sphere-roots.md`、`spontaneous-single-branch-syzygy.md`。
>
> **严格状态：**`11` 在两个 prefix quadratic 的 resultant/subresultant 常数中出现，但 sphere 几何证明它并不是 branch-collision 的真实例外。对真实 decimal 相位 `tau=10^{-M}=±1 (mod 11)` 做完整第一层审计后，恰留下 12 个 genuine noncentral 状态，而且 12 个全部为 simple roots。因此 `11` 不能被局部排除，但在**实际 decimal 第一层**没有 singular state。这里不宣称任意抽象 `tau∈F_11` 都不存在 noncentral repeated root。本文仍**不宣称 A2 全局关闭**。

---

## 1. `11` 不是 branch-collision 例外

`spontaneous-prefix-branch-audit.md` 的 subresultant 含系数

\[
198000=2^4\cdot3^2\cdot5^3\cdot11,
\]
所以仅从该 subresultant 在模 `11` 下不能继续推出 branch 二分。但 sphere 几何本身没有这一问题。

若

\[
\Delta_0\ne0,
\]
两个 finite sphere roots 满足

\[
\bar\zeta_2-\bar\zeta_1
=\frac{9(225x^2-y)A_-A_{\rm sp}}
{200x^2y^3(x+2)^2\Delta_0}.
\tag{1.1}

在 genuine pure-spontaneous channel 中

\[
11\nmid xy(x+2)(225x^2-y)A_{\rm sp},
\]
而 `A_-=0` 已证明会强迫 concatenated numerator/denominator 双零，即退出 `p∤alpha` pure channel。因此

\[
\boxed{p=11,\ \Delta_0\ne0\Longrightarrow
\text{两个 admissible finite sphere roots 仍严格不同。}}
\tag{1.2}

若

\[
\Delta_0=0,
\]
`spontaneous-prefix-boundaries.md` 已证明 sphere 恰降为一次式，只有一个 finite root。

因此：

\[
\boxed{
p=11\text{ 不会因为 subresultant 的 coefficient }11
\text{ 制造真实 two-branch collision。}}
\tag{1.3}

resultant 中的 coefficient `11` 只是清分母/正规化层的坏系数，不能被解释成第二个 sphere orientation 合并。

---

## 2. `审计修正`：抽象 `F_11` repeated-root 不能从 syzygy 直接排除

compact branch 为

\[
\mathscr L(\tau)
=55\tau^2+18(z-s)\tau+s^2-4sz-c.
\]

模 `11` 后二次首项消失：

\[
\mathscr L'(\tau)
=110\tau+18(z-s)
\equiv7(z-s).
\tag{2.1}

所以 abstract repeated condition 只先给

\[
z\equiv s\pmod{11}.
\tag{2.2}

`spontaneous-single-branch-syzygy.md` 的 discriminant identity

\[
405x^2\mathscr D
=20x^2(81z+29s)^2+11C_*
\]
在模 `11` 下与 (2.2) 相容，并不会额外强迫

\[
9\tau=2s.
\]

因此旧的过强说法

\[
\text{“任意 }p=11\text{ repeated root 必 central”}
\]
撤回，不得使用。

本文真正需要的不是任意 abstract `tau`，而是原问题的真实 decimal phase；它只有两个 residue，下一节直接完整检查。

---

## 3. 真实 decimal length 在模 `11` 只有两个第一层相位

因为

\[
10\equiv-1\pmod{11},
\]
所以

\[
\boxed{
\tau=10^{-M}\equiv(-1)^M\in\{1,10\}\pmod{11}.}
\tag{3.1}

因此 fixed `11` 的真实第一层可以完整有限审计，而不需要扫描任意 `tau`。

对每个

\[
\tau\in\{1,10\},
\quad x,y\in\mathbf F_{11}^\times,
\]
逐项要求：

- `x+2`、`225x^2-y`、`A_sp` 为单位；
- normalized `N_0=2025x^2+y^2` 为单位；
- `Omega_sp` 唯一恢复的 `bar w` 为单位；
- q/f/source 三个分离量均为单位；
- `2(9+y)-9tau` 非零（noncentral）；
- `Theta` 恢复 `bar zeta`；
- exact sphere 成立；
- concatenated numerator `9+y+bar zeta` 非零。

完整枚举只剩 12 个状态。

---

## 4. `有限证书`：12 个 genuine noncentral `11`-states

按

\[
(\tau,x,y,\bar w,\bar\zeta)
\]
列出：

\[
\boxed{
\begin{array}{c|ccccc}
&\tau&x&y&\bar w&\bar\zeta\\ \hline
1&1&1&2&7&8\\
2&1&5&2&3&9\\
3&1&7&9&5&5\\
4&1&8&6&7&3\\
5&1&10&10&7&2\\
6&10&1&2&7&3\\
7&10&2&6&3&5\\
8&10&4&7&2&2\\
9&10&4&9&3&10\\
10&10&5&2&3&2\\
11&10&6&10&6&7\\
12&10&7&4&5&8
\end{array}}
\tag{4.1}

这些点全部满足 genuine denominator/source/base-norm separation，且

\[
\Delta_0A_-C_*\ne0\pmod{11}.
\tag{4.2}

所以没有一个靠 prefix-defect degree drop、common-`alpha` 或 central kernel 偷渡。

每个状态恰命中一个 finite sphere orientation；不存在双 branch。

---

## 5. `已严格完成`：真实 12 个状态全部 simple

compact branch derivative 为

\[
\mathscr L'(\tau)
=110\tau+18(z-s).
\]
在 `p=11` 下就是

\[
7(z-s).
\]

对 (4.1) 十二点依次得到

\[
\boxed{
1,8,8,4,2,10,7,1,10,3,4,9
\pmod{11}.}
\tag{5.1}

全部非零。因此：

\[
\boxed{
\text{真实 decimal 第一层的 12 个 genuine }11\text{-states 全部 simple。}}
\tag{5.2}

这才是 fixed `11` 的严格 singularity 结论：**实际相位上没有 repeated state**。它不推广到任意抽象 `tau∈F_11`。

---

## 6. `已严格完成 / 降级`：decimal exponent orbit 本身也不会自动杀掉 `11`

\[
10^2=100=1+9\cdot11,
\]
其中 `9` 是 `11`-进单位。因此

\[
\boxed{
\operatorname{ord}_{11^k}(10)
=2\cdot11^{k-1}
\qquad(k\ge1).
}
\tag{6.1}

所以 `tau=±1 (mod 11)` 的 decimal exponent classes 都有完整的一维 `11`-进 lift。第一层 simple 并不意味着完整 `(x,y)` 状态自动提升，但也说明“继续只升 exponent”不会制造空性；还需要真实 prefix variables 的 lift条件。

---

## 7. 更新后的 fixed-11 结论

`11` 应当从“可能的 branch-collision bad coefficient”重新分类为：

\[
\boxed{
\text{fixed local carrier with 12 genuine simple first-layer templates}.}
\]

严格来说：

- no two-branch collision；
- 对真实 `tau=±1`，没有 repeated state；
- 12 genuine noncentral first-layer states survive；
- decimal exponent residue classes本身可继续提升。

所以 `11` 尚未关闭，但后续不应再把 resultant coefficient `11` 当成 branch singularity。真正剩余问题是把这 12 个 template 与

\[
b_2=10^{M-1}+2^{M-1}H,
\qquad
a_2=10^{M-1}-e
\]
的真实 defect lift 联立。

---

<a id="source-spontaneous-jh-root-gap"></a>

> 整合来源：`spontaneous-jh-root-gap.md`

# A2 additive height companion `J_H` 的全部实 decimal roots都大于 `1`

> **依赖：** `spontaneous-height-parity-ledger.md`、`spontaneous-residual-parity-doubling.md`。
>
> **严格状态：**`J_H` 已知是 positive primitive `3 mod 4` integer，并通过 exact identity与 `widehat(T)_2` 共享相同 height part。本文进一步证明：把 `J_H=0` 看成 decimal phase `tau=10^{-M}` 的二次方程时，它若有实根，则两个实根全部严格大于 `1`；真实 endpoint `tau<=10^-11` 与它们有统一巨大距离。因此 `J_H` residual只能通过 genuine p-adic / multiplicative-decimal wrapping出现。本文不把实根分离误写成模素数空性，也不宣称 A2 closure。

---

## 1. normalized quadratic

沿用

\[
x=\frac{b_2}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}},
\qquad
\tau=10^{-M},
\]

并记

\[
s:=9+y.
\]

`spontaneous-height-parity-ledger.md` 的 pure-decimal additive-height carrier

\[
\mathcal J_H
=B^2(5K^2-36K+55)-Q^2N_0
\]
满足

\[
\boxed{
\frac{100\mathcal J_H}{10^{4M}}
=G_H(x,y,\tau),
}
\tag{1.1}
\]

其中

\[
\boxed{
G_H
=100x^2\left(5s^2-36s\tau+55\tau^2\right)
-(x+2)^2(2025x^2+y^2).
}
\tag{1.2}
\]

对固定 `(x,y)`，这是关于 `tau` 的开口向上二次式。

当前 endpoint box 为

\[
\boxed{
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1.
}
\tag{1.3}
\]

---

## 2. vertex 统一位于 `3.27` 之后

(1.2) 关于 `tau` 的 derivative 为

\[
\partial_\tau G_H
=100x^2(-36s+110\tau).
\]

所以 vertex 为

\[
\boxed{
\tau_H^*=\frac{18s}{55}
=\frac{18(y+9)}{55}.
}
\tag{2.1}
\]

由 `y>249/250`：

\[
\tau_H^*
>\frac{18}{55}\left(9+\frac{249}{250}\right)
=\frac{44982}{13750}
>3.
\tag{2.2}
\]

特别地

\[
\boxed{\tau_H^*>1.}
\tag{2.3}
\]

---

## 3. `tau=1` 时仍严格为正

代入 `tau=1`：

\[
5s^2-36s+55
=5y^2+54y+136.
\]

所以

\[
\boxed{
G_H(x,y,1)
=100x^2(5y^2+54y+136)
-(x+2)^2(2025x^2+y^2).
}
\tag{3.1}
\]

第一项用 box 下端粗界：

\[
100x^2(5y^2+54y+136)
>
5\left(\frac{249}{250}\right)^2
+54\frac{249}{250}+136.
\]

右端为

\[
\frac{12172701}{62500}>194.
\tag{3.2}
\]

第二项用 box 上端粗界：

\[
(x+2)^2(2025x^2+y^2)
<
\left(2+\frac2{19}\right)^2
\left(2025\left(\frac2{19}\right)^2+1\right).
\]

右端精确为

\[
\frac{1494400}{14440}<104.
\tag{3.3}
\]

因此

\[
\boxed{
G_H(x,y,1)>90>0.
}
\tag{3.4}
\]

这里故意使用很松的整数余量；无需做 endpoint 单调性或 Bernstein 审计。

---

## 4. 所有 real roots 都大于 `1`

若 `G_H` 的 discriminant <0，则没有 real root，结论自动成立。

现在假设 discriminant >=0，并记 real roots

\[
\tau_-\le\tau_+.
\]

因为开口向上，vertex 是两根中点：

\[
\tau_-\le\tau_H^*\le\tau_+.
\]

由 (2.3)，`tau_H^*>1`。

若

\[
\tau_-\le1,
\]
则 `tau_+>=tau_H^*>1`，所以 `tau=1` 位于两 roots 之间或恰在左 root上，从而必须有

\[
G_H(1)\le0,
\]
与 (3.4) 矛盾。

故

\[
\boxed{
1<\tau_-\le\tau_H^*\le\tau_+.
}
\tag{4.1}
\]

若 discriminant=0，则唯一 double root就是 `tau_H^*>3`，同样满足结论。

因此统一得到：

\[
\boxed{
J_H=0\text{ 的所有实 decimal roots 都严格大于 }1.
}
\tag{4.2}
\]

---

## 5. 与真实 decimal orbit 的距离

无界 endpoint 中

\[
M\ge11,
\]
故

\[
0<\tau_{actual}=10^{-M}\le10^{-11}.
\]

所以任意 real root `tau_r` 都满足

\[
\boxed{
\tau_r-\tau_{actual}>1-10^{-11}.
}
\tag{5.1}
\]

因此 `J_H` 的 real geometry不会产生 near-root；任何 prime divisibility / Hensel lift都必须来自真正的 modular wrapping。

---

## 6. 与 global parity ledger 的关系

现在三类关键 simple residual 都有同一 Archimedean 状态：

1. `spontaneous-pure-root-gap.md`：pure spontaneous `L_1,L_2` 的全部 real roots `>1`；
2. 本文：additive height companion `J_H` 的全部 real roots `>1`；
3. `spontaneous-omega-content-biquadratic.md`：omega-content 两个 real numerator roots避开真实 `y` window。

所以 `spontaneous-residual-parity-doubling.md` 强迫出来的 companion inert parity不能解释为真实根靠近 endpoint；只剩 decimal multiplicative orbit / natural representative。

这仍不是模 `p` 空性。后续若要关闭 residual parity，必须真正控制 `10^{-M}` 在这些 simple algebraic branches上的 prime-power orbit或 modulus-vs-height，而不是继续重复 real-root分析。

---

<a id="source-spontaneous-omega-biquadratic"></a>

> 整合来源：`spontaneous-omega-biquadratic.md`

# A2 omega-content simple branch as an explicit biquadratic tower

> **依赖：** `spontaneous-omega-content-common.md`、`spontaneous-alpha-supported-resultant.md`。
>
> **严格状态：**`spontaneous-omega-content-common.md` 已证明 omega-content angle/additive common curve没有 surviving genuine singular Hensel tree。本文进一步把该 simple curve从两个隐式方程 `A_-=0,J=0` 改写为两层显式 quadratic tower：第一层 `r^2=R(x)` 给 content 的两个 numerator orientations；第二层 `u^2=L_±(x,r)` 给 additive decimal root。此前出现的 degree-8 `Q_omega(x)` 恰是 `L_+L_-` 的 quadratic norm，不是新的黑箱多项式。本文还证明两个 real content roots都严格避开真实 endpoint numerator window。本文不排除 p-adic wrapping，也不宣称 A2 closure。

---

## 1. content first layer

omega-content angle gate的 normalized polynomial为

\[
\boxed{
A_-(x,y)
=202500x^4-(101x^2+4x+4)y^2-1800x^2y.
}
\tag{1.1}

定义

\[
\boxed{P(x):=101x^2+4x+4,}
\tag{1.2}
\]

\[
\boxed{R(x):=101x^2+4x+8=P(x)+4.}
\tag{1.3}

将 (1.1) 改写为

\[
P(x)y^2+1800x^2y-202500x^4=0.
\tag{1.4}

其 `y`-discriminant为

\[
\boxed{
\operatorname{Disc}_y(A_-)
=(900x^2)^2R(x).
}
\tag{1.5}

因此 genuine `P x !=0` content root首先要求

\[
\boxed{r^2=R(x).}
\tag{1.6}

两个 `y` roots原本是

\[
y=
\frac{-1800x^2\pm900x^2r}{2P}.
\]

利用

\[
P=r^2-4=(r-2)(r+2),
\]
可完全约简为

\[
\boxed{
y_+=\frac{450x^2}{2+r},}
\tag{1.7+}
\]

\[
\boxed{
y_-=\frac{450x^2}{2-r}.}
\tag{1.7-}

所以 omega-content first layer并非任意 quadratic extension；它是单一平方根 `r=sqrt(R)` 的两个 Möbius orientations。

---

## 2. source-line collision就是 `r=0`

`spontaneous-alpha-supported-resultant.md` 已发现 content 与 height sheet collision 的共同 factor `R(x)`。

从 (1.6) 看得更直接：

\[
R=0
\iff r=0.
\]

此时两张 orientation合并：

\[
y_+=y_-=225x^2.
\]

即

\[
\boxed{R=0\Longrightarrow y=225x^2,}
\tag{2.1}

正是 source first-layer sheet `d=225x^2-y=0`。

所以此前所有 `R` collision的几何含义统一为：**omega-content 的两个 numerator orientations发生 branch collision，并退化到 source line。**

---

## 3. additive quadratic

omega-content additive gate使用

\[
\boxed{
\begin{aligned}
J(x,y,\tau)
={}&100x^2\left[5(y+9)^2-36(y+9)\tau+55\tau^2\right]\\
&-(x+2)^2(2025x^2+y^2).
\end{aligned}}
\tag{3.1}

其 `tau`-discriminant为

\[
\boxed{
\operatorname{Disc}_\tau J
=2000x^2D_\omega(x,y),
}
\tag{3.2}

其中

\[
\boxed{
\begin{aligned}
D_\omega={}&22275x^4+89100x^3
+991x^2y^2+17640x^2y\\
&+168480x^2+44xy^2+44y^2.
\end{aligned}}
\tag{3.3}

`spontaneous-omega-content-common.md` 通过 `Res_y(A_-,D_omega)` 得到过 degree-8 polynomial。下面解释它的真实结构。

---

## 4. 在 content sheet 上，第二层 discriminant只剩一个线性 quadratic-unit

先取 `y_+=450x^2/(2+r)`。在 quotient ring

\[
\mathbf Q(x)[r]/(r^2-R(x))
\]
中直接化简 (3.3)，得到

\[
\boxed{
D_\omega(x,y_+)
=
\frac{405x^2}{(r+2)^2}
L_+(x,r),
}
\tag{4.1}

其中

\[
\boxed{
L_+(x,r)=A_L(x)+rB_L(x),
}
\tag{4.2}

\[
\boxed{
A_L(x)
=501055x^4+44440x^3+104756x^2+4304x+4992,
}
\tag{4.3}

\[
\boxed{
B_L(x)=4(4955x^2+220x+416).
}
\tag{4.4}

因为

\[
2000\cdot405=810000=900^2,
\]
(3.2) 进一步变成

\[
\boxed{
\operatorname{Disc}_\tau J\big|_{y_+}
=
\left(\frac{900x^2}{r+2}\right)^2L_+(x,r).
}
\tag{4.5+}

对 conjugate orientation `r -> -r`：

\[
\boxed{
L_-(x,r)=A_L(x)-rB_L(x),
}
\tag{4.6}

\[
\boxed{
\operatorname{Disc}_\tau J\big|_{y_-}
=
\left(\frac{900x^2}{2-r}\right)^2L_-(x,r).
}
\tag{4.5-}

因此第二层 root condition只是

\[
\boxed{u^2=L_\pm.}
\tag{4.7}

omega-content common curve由两层 quadratic choice完全描述：

\[
\boxed{
r^2=R(x),\qquad u^2=L_\pm(x,r).}
\tag{4.8}

---

## 5. degree-8 `Q_omega` 正是 quadratic norm

两张 content sheet的 additive discriminant units互为 `r`-conjugate，所以

\[
\operatorname{Norm}(L_+)
=L_+L_-
=A_L^2-RB_L^2.
\]

直接展开：

\[
\boxed{
L_+L_-
=\mathcal Q_\omega(x),
}
\tag{5.1}

其中

\[
\boxed{
\begin{aligned}
\mathcal Q_\omega(x)={}&
251056113025x^8+44533768400x^7+67275876360x^6\\
&+8529261920x^5+6336428816x^4+503628928x^3\\
&+239152384x^2+8466432x+2768896.
\end{aligned}}
\tag{5.2}

这正是 `spontaneous-omega-content-common.md` 中

\[
\operatorname{Res}_y(A_-,D_\omega)
=164025x^4\mathcal Q_\omega(x)
\]
的 degree-8 factor。

所以 `Q_omega` 不是新的 independent obstruction；它只是第二层 discriminant在第一层 quadratic extension中的 norm。

这也解释了为什么只盯 `Q_omega` 的 Legendre character不会自动关闭 actual content branch：actual branch只要求对应的 `L_+` 或 `L_-` 为平方，而其 conjugate可以自由补偿 norm character。

---

## 6. explicit tau roots

由 (3.1)，quadratic formula给

\[
\boxed{
\tau
=
\frac{18(y+9)}{55}
\pm
\frac{\sqrt{\operatorname{Disc}_\tau J}}{11000x^2}.
}
\tag{6.1}

在 `y_+` sheet，若 `u^2=L_+`，则

\[
\boxed{
\tau
=
\frac{18(y_++9)}{55}
\pm
\frac{9u}{110(r+2)}.
}
\tag{6.2+}

同理 `y_-` sheet：

\[
\boxed{
\tau
=
\frac{18(y_-+9)}{55}
\pm
\frac{9u}{110(2-r)}.
}
\tag{6.2-}

因此 simple omega-content common prime最终只需要同步：

1. first-layer square root `r`；
2. second-layer square root `u`；
3. decimal orbit `tau=10^{-M}`。

不存在额外 source ratio或 hidden Hensel coordinate。

---

## 7. real endpoint separation：两张 content roots都不进入 actual numerator window

真实 denominator phase满足

\[
\frac1{10}<x<\frac2{19}.
\tag{7.1}

因此

\[
R(x)
>R(1/10)
=\frac{941}{100}.
\]

故 positive real square root满足

\[
\boxed{r>\frac{301}{100}>3.}
\tag{7.2}

于是 negative-orientation denominator

\[
2-r<0,
\]
所以

\[
\boxed{y_-<0.}
\tag{7.3}

对 positive orientation：

\[
y_+
=\frac{450x^2}{2+r}
<
\frac{450(2/19)^2}{2+301/100}.
\]

右端精确为

\[
\boxed{
\frac{60000}{60287}
<\frac{249}{250}.
}
\tag{7.4}

因此

\[
\boxed{
y_+<\frac{60000}{60287}<\frac{249}{250}.}
\tag{7.5}

而真实 endpoint要求

\[
\boxed{
\frac{249}{250}<y<1.
}
\tag{7.6}

所以两张 algebraic content roots都与真实 numerator window严格分离：

\[
\boxed{
 y_-<0,
\qquad
 y_+<0.99524,
\qquad
 y_{\rm actual}>0.996.
}
\tag{7.7}

这不是模素数矛盾；它说明任何 omega-content common state必须依赖真正的 p-adic wrapping，而不是实数附近的 root。

---

## 8. quadratic-character no-go

本文件把 content branch精确写成

\[
r^2=R,
\qquad
u^2=L_\pm.
\]

这并没有产生一个固定 quadratic nonresidue：`L_+L_-=Q_omega` 只是 conjugate norm。对 finite field中的一个 actual sheet，`L_+` 可以为平方而 `L_-` 取任意 compatible character；反之亦然。

因此下面这种路线应正式降级：

- 从 `Disc_y(A_-)` 取一次 Legendre symbol；
- 再从 `Disc_tau(J)` 取一次 Legendre symbol；
- 希望两者自动冲突。

完整 quadratic tower显示两层 character是独立 sheet choices，没有固定符号矛盾。真正剩余的约束是 decimal orbit / natural representative。

---

## 9. 更新后的 omega-content frontier

结合前一文件：

- full common curve没有 surviving singular Hensel tree；
- first layer是显式 `r^2=R`；
- second layer是显式 `u^2=L_±`；
- degree-8 eliminant只是 `Norm(L_±)`；
- 两个 real `y` roots都严格避开 endpoint numerator window。

所以 omega-content 已经是一个完全显式的 **simple biquadratic decimal-orbit problem**。

若后续继续这条支线，应直接研究

\[
\tau=10^{-M}
\]
与 (6.2±) 的离散同步，或为 modulus/source content建立足够强的 natural-representative bound；不应再做 generic discriminant/Legendre stacking。

A2 仍保持 open。

---

<a id="source-spontaneous-omega-content-common"></a>

> 整合来源：`spontaneous-omega-content-common.md`

# A2 common-`alpha` / `omega` content branch

> **依赖：** `primitive-reduction.md`、`spontaneous-prefix-branch-audit.md`、`spontaneous-height-parity-ledger.md`、`source-discriminant.md`。
>
> **严格状态：**本文把拼接 content `omega=gcd(alpha,beta)` 与 angle/additive 两个 primitive carrier 的公共部分改写成两个 pure-prefix decimal integers `C_omega`、`J_H`。`C_omega=0` 正是此前 `A_-=0` 的 common-`alpha` branch；`J_H=0` 是 additive carrier在 `alpha=0` 上的降维。本文进一步完成这条二维 common-content curve 的 genuine non-`3` inert singular bad-reduction audit：除边界外只有一个巨大素数的 singular point，而它不能提升到 `p^2`。因此 omega-content common channel不存在 surviving singular Hensel tree，只剩 simple moving decimal orbit。本文不排除所有 simple content roots，也不宣称 A2 closure。

---

## 1. concatenated content

沿用 reflection endpoint：

\[
N=10^M,
\quad T=10^m,
\quad A=a_2,
\quad B=b_2,
\]

\[
Q=B+2N,
\qquad
K=9N+10A.
\]

原拼接 numerator / denominator为

\[
\boxed{
\alpha=TK+a_3=\omega W_q,
}
\tag{1.1}
\]

\[
\boxed{
\beta=TQ+b_3=\omega S,
}
\tag{1.2}
\]

其中

\[
\gcd(W_q,S)=1.
\]

因此

\[
\boxed{\omega=\gcd(\alpha,\beta).}
\tag{1.3}
\]

对本文关心的 odd inert prime `p|omega`，`T` 为 unit。

---

## 2. angle content gate 是 `A_-` 的原始整数代表

定义

\[
\mathcal U_\Omega
=(45B^2-2AN)^2-A^2B(99B-4N),
\]

以及 angle raw carrier

\[
\mathcal O_+
=T\mathcal U_\Omega+2A^2Qb_3.
\]

定义

\[
\boxed{
\mathcal C_\omega
:=\mathcal U_\Omega-2A^2Q^2.
}
\tag{2.1}
\]

由 `beta=TQ+b3`：

\[
\boxed{
\mathcal O_+
=T\mathcal C_\omega
+2A^2Q\beta.
}
\tag{2.2}
\]

所以若

\[
p^e\mid\omega,
\]
则

\[
\boxed{
\min\{v_p(\widehat{\mathcal O}_{\rm sp}),e\}
=
\min\{v_p(\mathcal C_\omega),e\}.
}
\tag{2.3}
\]

使用 normalized variables

\[
x=B/N,
\qquad y=10A/N,
\]
有

\[
\boxed{
\mathcal C_\omega
=\frac{N^4}{100}A_-(x,y),
}
\tag{2.4}
\]

其中

\[
\boxed{
A_-(x,y)
=202500x^4-(101x^2+4x+4)y^2-1800x^2y.
}
\tag{2.5}
\]

这正是 `spontaneous-prefix-branch-audit.md` 识别的 common-`alpha` collision locus。

真实 endpoint已有

\[
A_-<0,
\]
故

\[
\boxed{\mathcal C_\omega<0.}
\tag{2.6}
\]

---

## 3. `C_omega` 的 2-adic orientation

`spontaneous-angle-parity.md` 已证明

\[
v_2(\mathcal U_\Omega)=2M+2,
\qquad
\frac{\mathcal U_\Omega}{2^{2M+2}}\equiv1\pmod4.
\]

另一方面

\[
Q=2^{M+1}Q_0,
\qquad A,Q_0\text{ odd},
\]
所以

\[
v_2(2A^2Q^2)=2M+3.
\]

因此

\[
\boxed{
v_2(\mathcal C_\omega)=2M+2,
}
\tag{3.1}
\]

且

\[
\boxed{
\frac{\mathcal C_\omega}{2^{2M+2}}
\equiv1-2\equiv3\pmod4.
}
\tag{3.2}
\]

结合 `C_omega<0`：

\[
\boxed{
-\frac{\mathcal C_\omega}{2^{2M+2}}>0,
\qquad
-\frac{\mathcal C_\omega}{2^{2M+2}}\equiv1\pmod4.
}
\tag{3.3}
\]

所以 common-`alpha` angle gate作为**正的绝对自然代表**本身具有 even total inert parity；这和 additive content gate的 `3 mod4` orientation不同。

---

## 4. additive content gate正是 `J_H`

`spontaneous-height-parity-ledger.md` 定义

\[
\boxed{
\mathcal J_H
=B^2(5K^2-36K+55)-Q^2N_0
}
\tag{4.1}
\]

并证明

\[
\boxed{
\Theta_{\rm dec}
=T\mathcal J_H
-2B^2(2K-9)\alpha.
}
\tag{4.2}
\]

由 `alpha=omega Wq`，对 `p^e|omega`：

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),e\}
=
\min\{v_p(\mathcal J_H),e\}.
}
\tag{4.3}
\]

已有

\[
\boxed{
\widehat{\mathcal J}_H
:=\frac{\mathcal J_H}{2^{2M+2}}>0,
\qquad
\widehat{\mathcal J}_H\equiv3\pmod4.
}
\tag{4.4}

所以 omega-supported angle/additive common prime完全由

\[
\boxed{
\omega,
\qquad
\mathcal C_\omega,
\qquad
\mathcal J_H
}
\tag{4.5}
\]
读取；third block已消失。

---

## 5. omega-content 与 source discriminant / denominator 自动分离

`source-discriminant.md` 给 source triangle

\[
z=g\omega-c_u,
\qquad
f=g\omega+c_u,
\]

以及

\[
\mathscr D_W=55z^2-49c_u^2.
\]

旧本原性有

\[
\gcd(\omega,c_u)=1.
\]

若 genuine non-`3` inert prime `p|omega`，则

\[
z\equiv-c_u\pmod p,
\qquad
f\equiv c_u\pmod p.
\]

故

\[
\boxed{p\nmid qf c_u.}
\tag{5.1}
\]

同时

\[
\boxed{
\mathscr D_W
\equiv(55-49)c_u^2
=6c_u^2\not\equiv0\pmod p.
}
\tag{5.2}
\]

所以 omega-content 与 denominator saturation、source-discriminant double-root 均严格分离。它是 common-`alpha` content，不应混入 pure spontaneous external discriminant-zero channel。

---

## 6. normalized common-content curve

定义

\[
\boxed{F(x,y):=A_-(x,y).}
\tag{6.1}
\]

把 `J_H` 除去正的 decimal scale后，定义

\[
\boxed{
\begin{aligned}
G(x,y,\tau)
:={}&100x^2\left[5(y+9)^2-36(y+9)\tau+55\tau^2\right]\\
&-(x+2)^2(2025x^2+y^2).
\end{aligned}}
\tag{6.2}
\]

其中

\[
\tau=10^{-M}.
\]

于是 genuine omega-supported angle/additive common first layer必须落在

\[
\boxed{F=G=0.}
\tag{6.3}
\]

这是一条一维 moving curve；本文接下来审计其 singular bad reduction。

---

# singular audit I: `F` 本身奇异

## 7. rank-drop 的第一种机制

因为

\[
F_\tau=0,
\]
若 `G_tau` 为 unit，而系统 Jacobian rank小于 `2`，就必须有

\[
F_x=F_y=0.
\]

直接 elimination：

\[
\boxed{
\operatorname{Res}_y(F,F_y)
=810000x^4
(101x^2+4x+4)(101x^2+4x+8).
}
\tag{7.1}
\]

另有

\[
\boxed{
\begin{aligned}
\operatorname{Res}_y(F,F_x)
={}&164025000000x^6\\
&\cdot(10201x^4+1212x^3+1652x^2+128x+128).
\end{aligned}}
\tag{7.2}
\]

排除 `x=0` 后，两个 x-polynomial 的 resultant为

\[
\boxed{
2^{22}3^25^2\cdot17\cdot37\cdot67^2\cdot101^4.
}
\tag{7.3}
\]

所以 genuine non-`3` inert prime中唯一候选是

\[
\boxed{p=67.}
\]

完整有限域审计却给：模 `67` 的所有 full-system singular states都满足

\[
\boxed{x=y=0,}
\]

而 `tau` 任意。这是 prefix boundary，不是 genuine omega-content state。

故第一种 singular mechanism为空。

---

# singular audit II: repeated decimal root

## 8. `G_tau=0` 等价于一个固定 repeated-`tau` center

把 `G` 看成 `tau` 的二次式：

\[
G
=5500x^2\tau^2
-3600x^2(y+9)\tau+\cdots.
\]

对 `p\nmid2\cdot5\cdot11\cdot x`：

\[
\boxed{
G_\tau=0
\iff
55\tau=18(y+9).
}
\tag{8.1}
\]

其 discriminant精确为

\[
\boxed{
\operatorname{Disc}_\tau(G)
=2000x^2D_\omega(x,y),
}
\tag{8.2}
\]

其中

\[
\boxed{
\begin{aligned}
D_\omega={}&22275x^4+89100x^3
+991x^2y^2+17640x^2y\\
&+168480x^2+44xy^2+44y^2.
\end{aligned}}
\tag{8.3}
\]

所以 repeated-`tau` branch必须满足

\[
F=D_\omega=0.
\]

消去 `y`：

\[
\boxed{
\operatorname{Res}_y(F,D_\omega)
=164025x^4\mathcal Q_\omega(x),
}
\tag{8.4}
\]

其中

\[
\boxed{
\begin{aligned}
\mathcal Q_\omega(x)={}&
251056113025x^8+44533768400x^7+67275876360x^6\\
&+8529261920x^5+6336428816x^4+503628928x^3\\
&+239152384x^2+8466432x+2768896.
\end{aligned}}
\tag{8.5}
\]

所有系数均为正，所以

\[
\boxed{\mathcal Q_\omega(x)>0\quad(x>0).}
\tag{8.6}
\]

因此真实 endpoint没有 repeated-`tau` Archimedean root；只可能发生 p-adic wrapping。

---

## 9. fixed bad primes of the repeated-`tau` intersection

`Q_omega` 的整数判别式因子分解为

\[
\boxed{
\begin{aligned}
\operatorname{Disc}(\mathcal Q_\omega)
={}&2^{120}3^{11}5^{26}7^{12}11^4 13^4 23^2 101^8\\
&\cdot557\cdot4357^2\cdot7596456621900959.
\end{aligned}}
\tag{9.1}
\]

其中最后的大因子为素数。限制到 non-`3` inert prime，候选为

\[
\boxed{
7,\ 11,\ 23,\ 7596456621900959.
}
\tag{9.2}
\]

对 `7,11,23`，完整 `(F,G)` singular-state枚举都只得到

\[
x=y=0
\]
边界，没有 genuine finite state。

剩下

\[
\boxed{p=7596456621900959}
\tag{9.3}
\]
有唯一 genuine finite singular state：

\[
\boxed{
x_0=596722596594438,}
\tag{9.4}
\]

\[
\boxed{
y_0=7182062884214340,}
\tag{9.5}
\]

\[
\boxed{
\tau_0=7460836853203523
\pmod p.
}
\tag{9.6}
\]

---

## 10. 巨大 singular prime不能提升到 `p^2`

在 (9.4)--(9.6) 的标准 `[0,p)` representatives上写

\[
x=x_0+pX,
\qquad
y=y_0+pY,
\qquad
\tau=\tau_0+pT_1.
\]

把 `F=G=0 mod p^2` 线性化。两行 Jacobian模 `p` 分别为

\[
\boxed{
(3088566246132647,\ 763538860035101,\ 0),
}
\tag{10.1}
\]

\[
\boxed{
(5543473436650293,\ 7013503068586219,\ 0).
}
\tag{10.2}
\]

第二行是第一行的

\[
\boxed{2399356256055466}
\tag{10.3}
\]
倍。

而常数 carry为

\[
\boxed{
F(x_0,y_0)/p
\equiv7136724306802588\pmod p,
}
\tag{10.4}
\]

\[
\boxed{
G(x_0,y_0,\tau_0)/p
\equiv6411661286654023\pmod p.
}
\tag{10.5}
\]

compatibility residual为

\[
\boxed{
6411661286654023
-2399356256055466\cdot7136724306802588
\equiv4160590904825983\not\equiv0\pmod p.
}
\tag{10.6}
\]

因此 augmented linear system不相容：

\[
\boxed{
\text{该唯一 genuine singular state 没有 }p^2\text{ lift}.}
\tag{10.7}

---

## 11. omega-content common channel 的最终局部分类

综合 §§7--10：

\[
\boxed{
\text{genuine non-`3` inert omega-content angle/additive common curve}
}
\]

没有 surviving singular Hensel tree。

所有真正可能继续到任意深度的 omega-content state都必须位于

\[
\boxed{F=A_-=0,\qquad G=J=0}
\]
的 **simple moving branches** 上。

这和此前 source / denominator / height pool 的审计结果一致：A2 的局部 singular mechanisms基本都已被剥掉；剩余困难是 simple decimal-orbit / natural-representative synchronization与 global parity allocation。

---

## 12. 对 `G_sp` parity 的意义

omega-content 对 global common gcd 的贡献现在具有明确 ledger：

- angle content由 negative `C_omega` 读取，取绝对 primitive后是 `1 mod4`；
- additive content由 positive `J_H` 读取，primitive为 `3 mod4`；
- content prime与 denominator / source-discriminant double-root分离；
- angle/additive 同时 content contact只剩 simple moving curve。

所以后续不能再把 common-`alpha` content当成未命名的第四种奇异 supplier。若 `G_sp=1 mod4` 分支仍需要两份独立 residual inert parity，omega-content只能通过这条已完全正规化的 simple curve参与；它不再提供额外 singular branching。

A2 仍保持 open。

---

<a id="source-spontaneous-oplus-thetaplus-root-gap"></a>

> 整合来源：`spontaneous-oplus-thetaplus-root-gap.md`

# A2 actual-angle / conjugate-additive cross roots避开整个 `(0,1)` decimal interval

> **依赖：** `spontaneous-sphere-roots.md`、`spontaneous-single-branch.md`、`spontaneous-sign-companion-parity.md`。
>
> **严格状态：**actual angle sheet `O_+=0` 的 sphere已 split 为两个 rational roots `z_1,z_2`，并且在真实 endpoint 中 `z_2<z_1<-4.778`。本文把 additive sign companion `Theta_+=0` 加入：它只把 actual additive root `z_Theta` 换成 `-z_Theta`，所以 cross branches是 `L(tau,-z_i)=0`。证明每支恰有一根 `<0`、另一根 `>1`，因此整个真实 decimal interval `0<tau<=10^-11` 无 root。本文仍不把 real separation提升成 modular emptiness，也不宣称 A2 closure。

---

## 1. 两条 cross quadratics

记

\[
s=9+y,
\qquad
c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.
\]

对任意 sphere root `z`，compact equation为

\[
\mathscr L(\tau,z)
=55\tau^2+18(z-s)\tau+s^2-4sz-c.
\tag{1.1}
\]

actual additive carrier `Theta_-=0` 的 normalized root记作 `z_Theta`。sign companion `Theta_+=0` 精确对应

\[
\boxed{z=-z_\Theta.}
\tag{1.2}
\]

因此若 actual angle sphere root为 `z_i`，cross condition是

\[
-z_\Theta=z_i
\iff
z_\Theta=-z_i.
\]

利用 `L(tau,z)=0 iff z_Theta=z`，得到

\[
\boxed{
\mathscr L_i^\#(\tau)
:=\mathscr L(\tau,-z_i)=0,
\qquad i=1,2.
}
\tag{1.3}
\]

展开：

\[
\boxed{
\mathscr L_i^\#
=55\tau^2-18(s+z_i)\tau+s^2+4sz_i-c.
}
\tag{1.4}
\]

每支 leading coefficient均为 `55>0`。

---

## 2. `tau=0` 时统一严格为负

真实 endpoint：

\[
\frac{249}{250}<y<1,
\qquad
9<s<10,
\]

而 `spontaneous-sphere-roots.md` 已证明

\[
\boxed{z_2<z_1<-4.778<-4.}
\tag{2.1}
\]

由于 `c>0`：

\[
\begin{aligned}
\mathscr L_i^\#(0)
&=s^2+4sz_i-c\\
&<100-16s\\
&<100-16\cdot9\\
&=-44.
\end{aligned}
\]

所以

\[
\boxed{
\mathscr L_i^\#(0)<-44<0.
}
\tag{2.2}
\]

---

## 3. `tau=1` 时也统一严格为负

写

\[
A(\tau)=55\tau^2-18s\tau+s^2-c,
\]

\[
B(\tau)=18\tau-4s.
\]

则

\[
\mathscr L_i^\#=A-Bz_i.
\]

在 `tau=1`：

\[
A(1)=y^2-26-c<-25.
\tag{3.1}
\]

同时

\[
B(1)=18-4(9+y)=-18-4y<0,
\]

而 `z_i<0`，所以

\[
B(1)z_i>0.
\]

故

\[
\boxed{
\mathscr L_i^\#(1)
=A(1)-B(1)z_i
<A(1)<-25.
}
\tag{3.2}
\]

---

## 4. 两根的位置

`L_i#` 是开口向上的实二次式。由 (2.2) 它取负值，所以 discriminant必严格为正，存在两个不同实根：

\[
r_{i,-}<r_{i,+}.
\]

开口向上的二次式只在两根之间为负。由

\[
\mathscr L_i^\#(0)<0,
\qquad
\mathscr L_i^\#(1)<0,
\]
可知 `0` 与 `1` 都位于同一负区间，因此

\[
\boxed{
r_{i,-}<0<1<r_{i,+},
\qquad i=1,2.
}
\tag{4.1}
\]

特别地整个区间

\[
\boxed{0\le\tau\le1}
\]
都不包含 root。

而真实 endpoint有

\[
0<\tau_{actual}=10^{-M}\le10^{-11}<1.
\]

所以

\[
\boxed{
\mathscr L_i^\#(10^{-M})\ne0
\quad\text{over }\mathbf R,
\qquad i=1,2.
}
\tag{4.2}
\]

---

## 5. 四 sign combinations 的 Archimedean 状态

结合已有文件：

- `O_+ / Theta_-`（actual/actual）：pure-spontaneous real roots全部 `>1`；
- `O_+ / Theta_+`（actual/conjugate）：本文证明两根分别 `<0` 与 `>1`；
- `O_- / Theta_-`（conjugate/actual）：`spontaneous-cross-sign-biquadratic.md` 的 norm在整个实轴严格正，无 real root；
- `O_- / Theta_+` 可由同一 conjugate-angle quadratic extension处理；其 real third-numerator sphere本身已经不存在，因此同样没有真实 endpoint mechanism。

因此四个 sign carriers产生的 residual parity都没有 Archimedean near-root解释。剩余问题纯粹是 modular / decimal multiplicative orbit / natural representative。

---

<a id="source-spontaneous-prefix-boundaries"></a>

> 整合来源：`spontaneous-prefix-boundaries.md`

# A2 spontaneous prefix 的 `Delta_0=0` 降阶边界

> **依赖：** `spontaneous-prefix-eliminant.md`、`spontaneous-sphere-roots.md`、`spontaneous-prefix-branch-audit.md`。
>
> **严格状态：**此前为了把两个 sphere orientation 都写成有限有理函数，曾在 branch-collision 审计中单列 `p∤Delta_0`。本文直接处理 `Delta_0=0`：证明此时 `Omega_sp` 固定第三分母后，exact sphere 关于第三分子从二次式严格降为一次式，而且 genuine non-`3,5` prime 下线性系数绝不同时消失。因此只有一个有限第三分子 orientation；`Q_2` 在该边界上的额外清分母根是 projective/infinite-root artifact，不属于真实 third-coordinate branch。由此 generic pure-spontaneous 的“唯一 admissible branch”不再需要假设 `p∤Delta_0`。本文仍**不宣称 A2 全局关闭**。

---

## 1. 记号

沿用

\[
x=\frac{b_2}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}},
\]

\[
d=225x^2-y,
\qquad
A_{\rm sp}=4d^2-xy^2(99x-4),
\]

以及

\[
\boxed{
\Delta_0:=2025x^2-18y-y^2.
}
\tag{1.1}

`Omega_sp=0` 固定

\[
\bar w=-\frac{A_{\rm sp}}{2y^2(x+2)}.
\tag{1.2}

exact sphere 为

\[
x^2\bar w^2(9+y+\bar\zeta)^2
=(x+2+\bar w)^2
\left(
\frac{2025x^2+y^2}{100}\bar w^2+x^2\bar\zeta^2
\right).
\tag{1.3}

---

## 2. `已严格完成`：sphere 的最高次系数就是 `Delta_0`

把 (1.2) 代入 (1.3)，清去全部分母。关于 `bar zeta` 的 primitive numerator 写成

\[
\mathscr F_\zeta
=A_2\bar\zeta^2+A_1\bar\zeta+A_0.
\]

直接展开得到

\[
\boxed{
A_2
=160000x^4y^6(x+2)^4\Delta_0.
}
\tag{2.1}

所以

\[
\boxed{
\Delta_0=0
\Longrightarrow
\deg_{\bar\zeta}\mathscr F_\zeta\le1.
}
\tag{2.2}

这解释了 `spontaneous-sphere-roots.md` 中第二根

\[
\bar\zeta_2
=\frac{A_{\rm sp}G_*}
{400x^2y^3(x+2)^2\Delta_0}
\]
为什么在 `Delta_0=0` 上跑向 projective infinity；它不是一个仍应保留的有限第三分子值。

---

## 3. `已严格完成`：线性系数在 genuine 边界绝不消失

定义

\[
\boxed{
H_{\rm lin}
:=202500x^4-99x^2y^2-1800x^2y
+4xy^2+4y^2.
}
\tag{3.1}

同一展开给

\[
\boxed{
A_1
=800x^2y^4(x+2)^2(y+9)H_{\rm lin}^2.
}
\tag{3.2}

先控制 `y+9`。在 `Delta_0=0` 下

\[
2025x^2=y(y+18),
\]
所以 normalized base norm

\[
2025x^2+y^2=2y(y+9).
\tag{3.3}

对 genuine spontaneous prime，`p∤yN_0`，故

\[
\boxed{p\nmid y(y+9).}
\tag{3.4}

再对 `H_lin` 与 `Delta_0` 消去 `y`：

\[
\boxed{
\operatorname{Res}_y(H_{\rm lin},\Delta_0)
=4100625x^4(x+2)^4
=3^8 5^4x^4(x+2)^4.
}
\tag{3.5}

因此对 genuine

\[
p\ne3,5,
\qquad
p\nmid x(x+2),
\]
有

\[
\boxed{
\Delta_0\equiv0
\Longrightarrow
H_{\rm lin}\not\equiv0
\Longrightarrow
A_1\not\equiv0
\pmod p.
}
\tag{3.6}

结合 (2.2)：

\[
\boxed{
\Delta_0=0
\Longrightarrow
\mathscr F_\zeta\text{ 恰为一次式，且恰有一个有限根。}
}
\tag{3.7}

---

## 4. `已严格完成`：`Q_2` 的 `Delta_0` 根是清分母 artifact

`Q_1,Q_2` 是把 `Theta` root 与两个 projective sphere roots 比较后清分母所得。对 `Delta_0` 消去 `y` 时，`Q_2` 的 resultant 确实出现

\[
\boxed{
\begin{aligned}
\operatorname{Res}_y(\mathcal Q_2,\Delta_0)
={}&C\,x^{10}(x+2)^8(25x^2+1)\\
&\cdot(100x^2+4-\tau^2),
\end{aligned}}
\tag{4.1}

其中 `C` 只含 `2,3,5`。

在 `Delta_0=0` 下还有

\[
25x^2+1
=\frac{(y+9)^2}{81}.
\tag{4.2}

所以最后一因子等价于

\[
\tau^2=\frac{4(y+9)^2}{81},
\qquad
9\tau=\pm2(y+9).
\tag{4.3}

但 §3 已证明真实 sphere 此时只有**一个有限** `bar zeta` root；原来以 `1/Delta_0` 表示的第二 root 已位于无穷远。因此 (4.1)–(4.3) 只描述在统一清分母多项式里保留下来的 projective degeneration，不能当成第二个真实 third-coordinate branch 收费。

特别地，`9tau=2(y+9)` 确实重新命中旧 central line `2K-9=0`；负号对应 projective anti-central companion。二者都不恢复第二个有限 sphere orientation。

---

## 5. `已严格完成`：唯一 admissible branch 不再需要 `p∤Delta_0`

现在分两种情况：

### 5.1 `Delta_0` 为单位

`spontaneous-sphere-roots.md` 给两个有限 sphere roots。`spontaneous-prefix-branch-audit.md` 已证明在 pure-spontaneous noncentral channel：

- `A_-=0` 会落回 common-`alpha`；
- 两 branch 同时命中只可能命中 central `2K-9=0`（或 fixed coefficient prime `11`）。

所以非中心 pure branch 至多一个。

### 5.2 `Delta_0=0`

本文 §3 直接证明 sphere 只有一个有限 root，所以无论 `Q_2` 的 cleared polynomial 是否形式上为零，都只有一个 admissible third-coordinate orientation。

因此除 fixed coefficient prime `11` 与 central line 的单独审计外，可统一写成：

\[
\boxed{
\text{genuine pure-spontaneous, noncentral}
\Longrightarrow
\text{exactly one finite sphere orientation is admissible.}
}
\tag{5.1}

这里不再要求

\[
p\nmid\Delta_0.
\]

这修补了前一 branch-audit 中为了使用 `zeta_2` 有理式而保留的技术性边界。

---

## 6. 更新后的开放核

`Delta_0=0` 不产生新的 moving branch；它只是 sphere degree drop。于是 generic moving carrier 的规范分类现在是：

1. `Delta_0≠0`：两个 finite sphere orientations 中精确选择一个；
2. `Delta_0=0`：sphere 本身只有一个 finite orientation；
3. `A_-=0`：common-`alpha`，不属 pure spontaneous；
4. `2K-9=0`：central `C_*` 支，单列；
5. fixed coefficient prime `11`：仍需单列。

因此下一步对 generic moving prime 可以直接研究**唯一有限 orientation**的 compact quadratic / tangent，而无需再把 `Delta_pref` 零层视为额外 branch。

---

<a id="source-spontaneous-prefix-branch-audit"></a>

> 整合来源：`spontaneous-prefix-branch-audit.md`

# A2 spontaneous prefix branch-collision 审计

> **依赖：** `spontaneous-prefix-eliminant.md`。
>
> **严格状态：**本文解释两个 prefix quadratic gate `Q_1,Q_2` 的共同根究竟代表什么。结果是：除固定 coefficient prime `11` 外，branch collision 只有两种机制——`A_-=0` 是拼接分子/分母同时为零的 common-`alpha` 退化；另一种是 `2K-9=0` 的 `Theta_dec` 中心退化，其 pure-prefix 方程正是 `C_*=0`。因此在真正 `p∤alpha` 且 `p∤2K-9` 的 pure-spontaneous channel，两条 quadratic branch 严格互斥。本文仍**不宣称 A2 全局关闭**。

---

## 1. 记号

沿用 `spontaneous-prefix-eliminant.md`：

\[
\tau=10^{-M},
\qquad
x=\frac{b_2}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}},
\]

\[
d=225x^2-y,
\]

\[
A_{\rm sp}=4d^2-xy^2(99x-4),
\]

\[
A_-=A_{\rm sp}-2y^2(x+2)^2,
\]

\[
\Delta_0=2025x^2-18y-y^2.
\]

第三块消元后的两个 primitive gate 为

\[
\mathcal Q_1(\tau;x,y)=0,
\qquad
\mathcal Q_2(\tau;x,y)=0.
\]

定义

\[
\boxed{
\begin{aligned}
C_*={}&164025x^4+656100x^3
+2381x^2y^2+41400x^2y\\
&+842400x^2+324xy^2+324y^2.
\end{aligned}}
\tag{1.1}
\]

---

## 2. `已严格完成`：一次 subresultant 直接给出 branch-collision 二分

对 `Q_1,Q_2` 关于 `tau` 取 subresultant sequence。次数为 `1` 的项精确化为

\[
\boxed{
\begin{aligned}
\mathcal S_1
={}&198000\,x^2y^3(x+2)^2d\,A_-A_{\rm sp}\\
&\cdot\bigl(2(y+9)-9\tau\bigr).
\end{aligned}}
\tag{2.1}
\]

这里

\[
198000=2^4\cdot3^2\cdot5^3\cdot11.
\]

所以对 genuine non-`3` carrier，并进一步排除 fixed coefficient prime `11`，旧分离条件给

\[
p\nmid x y(x+2)dA_{\rm sp}.
\]

若同一个 `tau` 同时满足

\[
\mathcal Q_1\equiv\mathcal Q_2\equiv0\pmod p,
\]
则 subresultant 必为零，因此只有

\[
\boxed{
A_-\equiv0
\quad\text{或}\quad
9\tau\equiv2(y+9)
\pmod p.
}
\tag{2.2}
\]

这比只看最终 resultant 更强：它直接恢复共同根的几何位置。

---

## 3. `已严格完成`：`A_-=0` 恰是 concatenated numerator/denominator 双零

`spontaneous-prefix-eliminant.md` 已证明，在 `Omega_sp=0` 下

\[
\boxed{
\bar w:=\frac{w}{10^M}
=-\frac{A_{\rm sp}}{2y^2(x+2)}.
}
\tag{3.1}
\]

若

\[
A_-=A_{\rm sp}-2y^2(x+2)^2=0,
\]
则

\[
\boxed{
\bar w=-(x+2).
}
\tag{3.2}
\]

而真实拼接分母是

\[
TQ+b_3
=T10^M\bigl((x+2)+\bar w\bigr),
\]
所以

\[
\boxed{p\mid TQ+b_3.}
\tag{3.3}
\]

另一方面 exact sphere 的 scale-free 形式为

\[
x^2\bar w^2(9+y+\bar\zeta)^2
=(2+x+\bar w)^2
\left(
\frac{2025x^2+y^2}{100}\bar w^2
+x^2\bar\zeta^2
\right),
\tag{3.4}
\]

其中

\[
\bar\zeta=\frac{a_3}{T10^M}.
\]

由 (3.2)，右边整个平方因子消失；而 genuine channel 中 `x\bar w` 为单位，因此

\[
9+y+\bar\zeta\equiv0\pmod p.
\]

于是

\[
TK+a_3
=T10^M(9+y+\bar\zeta)
\equiv0\pmod p.
\]
即

\[
\boxed{
A_-=0
\Longrightarrow
p\mid(TQ+b_3)
\quad\text{且}\quad
p\mid\alpha:=TK+a_3.
}
\tag{3.5}
\]

所以 `A_-` collision branch 不是 pure spontaneous。它精确落回 `spontaneous-angle.md` §7 已分出的 common-`alpha` channel；若当前定义 genuine pure spontaneous 为

\[
p\nmid\alpha,
\]
则

\[
\boxed{p\nmid A_-.}
\tag{3.6}
\]

这一排除不需要 external discriminant-zero 假设，比 `spontaneous-prefix-eliminant.md` 中的 external resultant 更一般。

---

## 4. `已严格完成`：另一种 collision 恰是 `2K-9=0` 中心线

由

\[
K=10^M(9+y)=\frac{9+y}{\tau},
\]
(2.2) 的第二种可能

\[
9\tau=2(y+9)
\]
正好等价于

\[
\boxed{2K-9=0.}
\tag{4.1}
\]

记

\[
\boxed{\tau_c:=\frac{2(y+9)}9.}
\tag{4.2}
\]

把 `tau_c` 直接代回两个 exact quadratic gate，得到

\[
\boxed{
\mathcal Q_1(\tau_c)
=-\frac{2}{81}y^3(x+2)^2C_*,
}
\tag{4.3}
\]

\[
\boxed{
\mathcal Q_2(\tau_c)
=\frac{2}{81}y^3(x+2)^2\Delta_0C_*.
}
\tag{4.4}
\]

所以在 genuine prefix-defect separation `p∤y(x+2)Delta_0` 下：

\[
\boxed{
\tau=\tau_c,
\quad
\mathcal Q_1=\mathcal Q_2=0
\iff
C_*=0.
}
\tag{4.5}
\]

这解释了为什么 `C_*` 在两个 quadratic 的 resultant 中只出现一次：它就是 non-generic linear solve `2K-9=0` 的中心退化 locus。

---

## 5. `已严格完成`：`C_*` 直接由中心 `Theta` 方程恢复

在 `2K-9=0` 下

\[
K=\frac92,
\qquad
\tau=\tau_c.
\]

`Theta_dec` 的线性 `a_3` 项消失，只剩

\[
\mathcal R_\Theta
=B^2(K^2-18K+55)-Q^2N_0.
\]

由于

\[
K^2-18K+55=-\frac{23}{4},
\]
中心必要条件为

\[
-\frac{23}{4}B^2-Q^2N_0\equiv0.
\tag{5.1}
\]

把

\[
B=10^Mx,
\qquad
Q=10^M(x+2),
\qquad
N_0=\frac{10^{2M}}{100}(2025x^2+y^2),
\]
以及

\[
10^M=\frac{9}{2(y+9)}
\]
代入，清去单位后恰得到

\[
\boxed{
81(x+2)^2(2025x^2+y^2)
+2300x^2(y+9)^2=0.
}
\tag{5.2}
\]

展开 (5.2) 正是

\[
\boxed{C_*=0.}
\tag{5.3}
\]

因此 branch-resultant 的 `C_*` 与 `Theta_dec` central gate 是同一个对象，不应被计作两个独立 obstruction。

---

## 6. `已严格完成`：pure-spontaneous noncentral branch 严格互斥

综合 §§2–5。设 `p` 满足：

\[
p\equiv3\pmod4,
\qquad
p\notin\{3,5,11\},
\]

并处于 genuine pure-spontaneous channel：

\[
p\nmid x y(x+2)dA_{\rm sp}\Delta_0\alpha,
\]

且非中心：

\[
p\nmid2K-9.
\]

如果 `Q_1,Q_2` 同时为零，则 (2.2) 只能进入：

- `A_-=0`，但 §3 强迫 `p|alpha`，矛盾；
- `tau=tau_c`，但这等价于 `2K-9=0`，矛盾。

故

\[
\boxed{
\text{genuine pure-spontaneous + noncentral}
\Longrightarrow
\text{恰至多命中 }\mathcal Q_1,\mathcal Q_2\text{ 中的一支。}
}
\tag{6.1}
\]

结合 `spontaneous-prefix-eliminant.md` 已知至少一支必须命中，所以实际上：

\[
\boxed{
\text{generic common carrier 精确选择唯一一个 prefix quadratic branch。}
}
\tag{6.2}
\]

这里的“唯一”仍不是“不存在”；单支可以继续有 simple p-adic root。

---

## 7. `已严格完成 / no-go`：中心 sphere quadratic 的判别式自动是平方

中心线 `2K-9=0` 不能靠再加一个 Legendre character 关闭。

先只代入

\[
K=\frac92,
\qquad
10^M=\frac{9}{2(y+9)},
\]
以及 `Omega_sp` 给出的 `w`，暂不要求 `C_*=0`。把 exact sphere 看成关于

\[
\zeta=\frac{a_3}{T}
\]
的二次式。其 discriminant 精确为

\[
\boxed{
\begin{aligned}
\operatorname{disc}_{\zeta}
={}&\Bigl[
10497600\,x^2y^3(x+2)^2(y+9)\\
&\qquad\cdot(225x^2-y)A_-A_{\rm sp}
\Bigr]^2.
\end{aligned}}
\tag{7.1}
\]

也就是说中心 sphere 的两个 `zeta` root 在函数域 `Q(x,y)` 中已经是有理的；这里没有新的 quadratic-character obstruction。

所以 `C_*=0` 中心支若要关闭，必须继续利用：

- genuine/source/denominator separation；
- `tau=10^{-M}` 的真实 decimal orbit；
- 或 natural representative / finite-defect shell；

不能再从 sphere discriminant 收一次 Legendre 条件。

---

## 8. 更新后的开放核

`spontaneous-prefix-eliminant.md` 把第三块消成两个 quadratic；本文进一步证明：

\[
\boxed{
\begin{array}{ccl}
A_-=0
&\Longleftrightarrow&
\text{concatenated numerator/denominator 双零通道},\\
C_*=0
&\Longleftrightarrow&
\text{Theta central line }2K-9=0.
\end{array}}
\]

因此当前真正 generic 的 pure-spontaneous carrier 已变成：

\[
\boxed{
\begin{gathered}
p\notin\{3,5,11\},
\qquad p\nmid\alpha(2K-9),\\
\text{恰有一个 }i\in\{1,2\}
\text{ 使 }\mathcal Q_i(10^{-M};x,y)\equiv0\pmod p.
\end{gathered}}
\]

下一步最自然的对象已经不是第三块，也不是 branch resultant，而是**单个 quadratic branch 与真实 decimal prefix orbit 的同步**。应分别研究 `Q_1`、`Q_2` 的 repeated-root kernel 和它们与 `D_src / Delta_pref / C` 的 resultant；中心 `C_*` 与 fixed `11` 单列。

---

<a id="source-spontaneous-prefix-eliminant"></a>

> 整合来源：`spontaneous-prefix-eliminant.md`

# A2 spontaneous carrier 的 pure-prefix 消元

> **依赖：** `spontaneous-angle.md`、`phase-and-defect.md`、`endpoint-lattice.md` 的 reflection endpoint shell，以及 `spontaneous-bad-primes.md` / `external-secant-center.md` 对 fully coupled external 子通道的后续审计。
>
> **严格状态：**本文处理 `spontaneous-angle.md` 留下的 generic common-prime 问题：同一个 non-`3` inert prime 同时接触 spontaneous angle polynomial `Omega_sp` 与 pure-decimal odd-cofactor polynomial `Theta_dec`。主要结果是把第三块 `a_3,b_3` 完全消去，得到两个只依赖第一、二块 prefix 与 `10^{-M}` 的二次 gate；再求两个 gate 的 exact resultant，得到单一 branch-collision kernel。本文仍**不宣称 A2 全局关闭**。

---

## 1. 原始 decimal 记号

固定当前最危险 reflection endpoint：

\[
a_1=9,
\qquad
N:=10^M,
\qquad
T:=10^m.
\]

记

\[
A:=a_2,
\qquad
B:=b_2,
\]

\[
Q:=2N+B,
\qquad
K:=9N+10A,
\]

\[
C_0:=\frac{9B}{2},
\qquad
N_0:=C_0^2+A^2.
\tag{1.1}
\]

对应的 scale-free prefix variables 为

\[
x=\frac BN,
\qquad
y=\frac{10A}{N}.
\tag{1.2}
\]

第三块写成

\[
w:=\frac{b_3}{T},
\qquad
\zeta:=\frac{a_3}{T}.
\tag{1.3}
\]

`spontaneous-angle.md` 的 source-normalized variable 满足

\[
r_s=\frac{Nx}{w}=\frac{B}{w}=\frac{BT}{b_3}.
\tag{1.4}
\]

---

## 2. `已严格完成`：`Omega_sp` 对第三分母其实是纯整数一次式

定义

\[
d:=225x^2-y,
\]

\[
\boxed{
A_{\rm sp}
:=4d^2-xy^2(99x-4).
}
\tag{2.1}
\]

则

\[
\Omega_{\rm sp}
=A_{\rm sp}r_s+2xy^2(x+2).
\tag{2.2}
\]

把 (1.2)、(1.4) 代回并清去 `N`、`b_3`，定义纯 prefix 整数

\[
\boxed{
\mathcal U_\Omega
:=(45B^2-2AN)^2-A^2B(99B-4N).
}
\tag{2.3}
\]

直接展开得到精确恒等式

\[
\boxed{
\Omega_{\rm sp}
=\frac{100B}{b_3N^4}
\left(
T\mathcal U_\Omega+2A^2Qb_3
\right).
}
\tag{2.4}
\]

因此对 genuine spontaneous prime，`p` 与 `2·5·ABQb_3N` 分离，故

\[
\boxed{
p\mid\Omega_{\rm sp}
\iff
p\mid T\mathcal U_\Omega+2A^2Qb_3.
}
\tag{2.5}
\]

换成 `w=b_3/T`：

\[
\boxed{
w\equiv-\frac{\mathcal U_\Omega}{2A^2Q}\pmod p.}
\tag{2.6}
\]

在 scale-free 坐标中同一式进一步变成

\[
\boxed{
\frac wN
\equiv
-\frac{A_{\rm sp}}
{2y^2(x+2)}
\pmod p.
}
\tag{2.7}
\]

也就是说，`Omega_sp` 不是只固定抽象 source ratio；它实际上唯一固定了真实 third denominator 的 normalized decimal phase。

注意

\[
45B^2-2AN=\frac{20}{9}D_{\rm src},
\]
所以 (2.3) 仍保留旧 source-Hensel 几何的来源；这里没有制造新的独立 source quantity。

---

## 3. `已严格完成`：`Theta_dec` 对第三分子也是纯整数一次式

`spontaneous-angle.md` 已定义

\[
\Theta_{\rm dec}
=B^2\mathscr S_0-TQ^2N_0,
\]

其中

\[
\mathscr S_0
=T(K^2-26)-(2K-9)(2a_3+9T).
\]

定义

\[
\boxed{
\mathcal R_\Theta
:=B^2(K^2-18K+55)-Q^2N_0.
}
\tag{3.1}
\]

则完全展开后：

\[
\boxed{
\Theta_{\rm dec}
=T\mathcal R_\Theta
-2B^2(2K-9)a_3.
}
\tag{3.2}
\]

所以在非中心退化通道

\[
p\nmid2K-9
\tag{3.3}
\]
上，任意 odd carrier `p|Theta_dec` 唯一固定

\[
\boxed{
\zeta=\frac{a_3}{T}
\equiv
\frac{\mathcal R_\Theta}
{2B^2(2K-9)}
\pmod p.
}
\tag{3.4}
\]

因此 generic `Omega_sp ∩ Theta_dec` common prime 同时唯一固定 `w` 与 `zeta`；第三块已经没有自由 residue。

边界 `p|2K-9` 必须单列。此时 (3.2) 退化为

\[
p\mid\mathcal R_\Theta.
\]

在 `2K=9` 下

\[
\mathcal R_\Theta
=-\frac{23}{4}B^2-Q^2N_0,
\tag{3.5}
\]

即一个纯 prefix central gate。本文的二次消元只声称覆盖 (3.3) 的 generic channel；(3.5) 不被偷偷除掉。

---

## 4. `已严格完成`：真正的 sphere equation 只需原始 decimal blocks

当前拼接值本身是

\[
\mathcal R
=\frac{TK+a_3}{TQ+b_3}.
\tag{4.1}
\]

而原三项平方和为

\[
\frac{81}{4}+\frac{A^2}{B^2}+\frac{a_3^2}{b_3^2}
=\frac{N_0}{B^2}+\frac{a_3^2}{b_3^2}.
\]

因此 exact lift 的 sphere condition 等价于纯整数恒等式

\[
\boxed{
B^2b_3^2(TK+a_3)^2
=(TQ+b_3)^2
\left(
N_0b_3^2+B^2a_3^2
\right).
}
\tag{4.2}
\]

这就是消去 (2.6)、(3.4) 所需的第三条方程；不需要再引入 Gaussian quotient、`W_q` 或 finite-defect quotient。

---

## 5. `已严格完成`：第三块完全消去，只剩两个 `10^{-M}` 二次 gate

令

\[
\tau:=10^{-M}=N^{-1}
\]
在任意 `p\ne2,5` 的有限域中理解为 `N` 的逆元。

继续记

\[
\mathcal N(x,y):=2025x^2+y^2.
\tag{5.1}
\]

由 (2.7)：

\[
\boxed{
\bar w:=\frac wN
=-\frac{A_{\rm sp}}{2y^2(x+2)}.
}
\tag{5.2}
\]

由 (3.4) 除以 `N`，得到

\[
\boxed{
\bar\zeta:=\frac{\zeta}{N}
=
\frac{
 x^2\bigl((9+y)^2-18(9+y)\tau+55\tau^2\bigr)
 -\frac1{100}(x+2)^2\mathcal N(x,y)
}
{2x^2\bigl(2(9+y)-9\tau\bigr)}.
}
\tag{5.3}
\]

把 (5.2)–(5.3) 代入 (4.2) 并约掉共同 `N`-尺度，sphere equation 变成

\[
 x^2\bar w^2(9+y+\bar\zeta)^2
=(2+x+\bar w)^2
\left(
\frac{\mathcal N(x,y)}{100}\bar w^2
+x^2\bar\zeta^2
\right).
\tag{5.4}
\]

清去分母后的 numerator 在 `Q[tau,x,y]` 中精确分解为两个 primitive 二次因子：

\[
\boxed{
\mathcal P_{\rm sph}(\tau,x,y)
=-\mathcal Q_1(\tau;x,y)\mathcal Q_2(\tau;x,y).
}
\tag{5.5}
\]

这里 `Q_1,Q_2` 以 `tau` 次数为 `2`，按首项唯一正规化：

\[
\boxed{
[\tau^2]\mathcal Q_1
=11000x^2y^3(x+2)^2,
}
\tag{5.6}
\]

\[
\boxed{
[\tau^2]\mathcal Q_2
=-11000x^2y^3(x+2)^2\Delta_0(x,y),
}
\tag{5.7}
\]

其中

\[
\boxed{
\Delta_0(x,y)=2025x^2-18y-y^2.
}
\tag{5.8}
\]

两个二次式的完整 expanded coefficients 作为 literal polynomial 放在

`check_a2_spontaneous_prefix_eliminant.py`

中；checker 直接从 (5.2)–(5.4) 重建 numerator 并核对 (5.5)，所以正文不重复塞入约八十项机械系数。

于是 generic genuine common carrier 必满足

\[
\boxed{
\mathcal Q_1(10^{-M};x,y)\equiv0
\quad\text{或}\quad
\mathcal Q_2(10^{-M};x,y)\equiv0
\pmod p.
}
\tag{5.9}
\]

这是真正的新降维：

\[
(r_s,w,\zeta,a_3,b_3,m)
\]
全部从 common-prime condition 中消失，只剩第一、二块 prefix 与 decimal length phase `10^{-M}`。

注意 (5.9) 仍只是必要条件；二次 gate 可以有 simple roots，不能因为“只有两个 branch”就宣称空性。

---

## 6. `已严格完成`：两个 prefix branch 的共同根由单一 kernel 控制

除了 `A_sp`，再定义

\[
\boxed{
A_-:=A_{\rm sp}-2y^2(x+2)^2
}
\tag{6.1}
\]

即

\[
A_-
=202500x^4-101x^2y^2-1800x^2y
-4xy^2-4y^2,
\tag{6.2}
\]

以及

\[
\boxed{
\begin{aligned}
C_*:={}&164025x^4+656100x^3
+2381x^2y^2+41400x^2y\\
&+842400x^2+324xy^2+324y^2.
\end{aligned}}
\tag{6.3}
\]

对两个二次 gate 关于 `tau` 求 exact resultant，得到惊人的完全因子化：

\[
\boxed{
\begin{aligned}
\operatorname{Res}_{\tau}(\mathcal Q_1,\mathcal Q_2)
={}&-7128000\,x^2y^6(x+2)^4(225x^2-y)^2\\
&\cdot A_-^2A_{\rm sp}^2C_*.
\end{aligned}}
\tag{6.4}
\]

而

\[
7128000=2^6\cdot3^4\cdot5^3\cdot11.
\tag{6.5}
\]

对 genuine non-`3` spontaneous cofactor carrier，旧分离条件与 `spontaneous-angle.md` 已给

\[
p\nmid 2\cdot3\cdot5\,x y(x+2)(225x^2-y)A_{\rm sp}.
\tag{6.6}
\]

因此对 `p\ne11`：

\[
\boxed{
\mathcal Q_1\equiv\mathcal Q_2\equiv0
\Longrightarrow
p\mid A_-C_*.
}
\tag{6.7}
\]

所以 two-branch collision 不再是一个未命名 resultant；它只有两个显式二维 kernel `A_-` 与 `C_*`，外加固定 coefficient prime `11`。

这并不说明 generic carrier 必须让两个 branch 同时消失；单独的一条 simple branch 仍然是当前开放核。

---

## 7. `已严格完成`：fully coupled external 子通道中 `A_-` 整支自动消失

若同一个 prime 还处于 `spontaneous-angle.md` §6 的 external discriminant-zero channel，则

\[
\boxed{
E_W(x,y)
:=220y^4(x+2)^4-49A_{\rm sp}^2
\equiv0\pmod p.
}
\tag{7.1}
\]

对 `A_-` 与 `E_W` 消去 `y`，exact resultant 为

\[
\boxed{
\operatorname{Res}_y(A_-,E_W)
=2^{14}3^{18}5^{16}x^{16}(x+2)^8.
}
\tag{7.2}
\]

因此在 genuine external channel

\[
p\nmid2\cdot3\cdot5\,x(x+2)
\]
中：

\[
\boxed{p\nmid A_-.}
\tag{7.3}
\]

结合 (6.7)，若 fully coupled external prime 同时落在两个 prefix quadratic branch 上，则（`p\ne11`）只能满足

\[
\boxed{p\mid C_*.}
\tag{7.4}
\]

这与此前 fixed `19/47` secant 分类的角色不同：这里 `C_*` 控制的是 **two-prefix-branch collision**，不是 secant cofactor 本身。

---

## 8. `已严格完成 / 结构解释`：`67` 与 `47` 从 branch-collision 判别式中自然出现

两个 collision kernel 自身又都是关于 `y` 的二次式。

首先

\[
\boxed{
\operatorname{disc}_y(A_-)
=900^2x^4(101x^2+4x+8).
}
\tag{8.1}
\]

而内层 quadratic 满足

\[
\boxed{
\operatorname{disc}_x(101x^2+4x+8)
=-16\cdot3\cdot67.
}
\tag{8.2}
\]

所以旧 fully coupled local audit 中出现的 fixed `67` 并非完全孤立：它正是 `A_-` collision kernel 的 nested ramification prime。

另一方面

\[
\boxed{
\operatorname{disc}_y(C_*)
=-810^2x^2(x+2)^2
(2381x^2+324x+416),
}
\tag{8.3}
\]

且

\[
\boxed{
\operatorname{disc}_x(2381x^2+324x+416)
=-16\cdot23\cdot47\cdot223.
}
\tag{8.4}
\]

因此 `47` 也在 pure-prefix branch-collision 几何中有独立来源：它是 `C_*` 的 nested ramification prime之一。这与 `external-secant-center.md` 中 `47` 作为 `Xi_C` center-cancellation prime 的出现相互吻合，但两者不是同一条公式，不能重复收费。

同样必须审计边界：`23`、`223` 也出现在 (8.4)，所以 (8.4) 不能被误写成“只有 47”；它只识别 bad-reduction support。

---

## 9. 实数侧审计：这些 gate 都不是真实零点下降

endpoint window 中

\[
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1.
\]

`spontaneous-angle.md` 已证明

\[
A_{\rm sp}>\frac{8049}{1444}>5.
\]

同时 `C_*` 的全部显示项在 `x,y>0` 时为正，因此

\[
\boxed{C_*>0.}
\tag{9.1}
\]

所以 (6.7)、(7.4) 描述的是纯 modular / p-adic collision，而不是实数曲线真的穿过 endpoint box。这里同样不能从正性直接推出“没有素因子”。

---

## 10. 当前开放核

本层严格完成了下面的变量消去：

\[
\boxed{
\Omega_{\rm sp}=0,
\quad
\Theta_{\rm dec}=0,
\quad
\text{exact sphere}
}
\]

在 generic `p\nmid2K-9` 通道中推出

\[
\boxed{
\mathcal Q_1(10^{-M};x,y)
\mathcal Q_2(10^{-M};x,y)
\equiv0\pmod p.
}
\]

并进一步得到：

1. `Omega_sp` 唯一固定 `b_3/T`；
2. `Theta_dec` 唯一固定 `a_3/T`；
3. 第三块全部消去后只有两个 prefix quadratic branch；
4. 两 branch 的共同根只经过 `A_-`、`C_*` 或固定 `11`；
5. fully coupled external channel 中 `A_-` 被 exact resultant 完全排除，所以 branch collision 只剩 `C_*`；
6. `67` 与 `47` 分别作为 `A_-`、`C_*` 的 nested ramification prime 自然恢复。

**仍未完成：**单独一条 `Q_1` 或 `Q_2` 的 simple moving root 仍可以存在。所以下一步不应再研究第三块，而应直接研究这两个 prefix quadratic 对真实 decimal orbit

\[
\tau=10^{-M},
\qquad
x=\frac{b_2}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}}
\]

的 `p`-进同步；或者把 `Q_i` 与 `D_src / Delta_pref / C` 的 natural representative 做新的 resultant。中心退化线 `2K-9=0` 也需单列，不能被 generic 除法覆盖。

---

<a id="source-spontaneous-pure-root-gap"></a>

> 整合来源：`spontaneous-pure-root-gap.md`

# A2 pure-spontaneous branch 的全部实 `tau` roots 都大于 `1`

> **依赖：** `spontaneous-sphere-roots.md`、`spontaneous-single-branch.md`。
>
> **严格状态：**`spontaneous-single-branch.md` 只证明了每支 repeated critical point `tau_i^*>12/5`，并未排除较小 simple real root靠近 `tau=0`。本文补上这一缺口：利用 `Theta` third-numerator root 与第一 sphere root在 `tau=1` 的 exact gap，证明两支 quadratic `L_i` 在 `tau=1` 仍严格为正。结合 vertex `>12/5` 与 positive discriminant，得到两支的两个 real roots全部严格 `>1`。因此真实 decimal phase `tau<=10^-11` 与所有 pure-spontaneous real roots有统一巨大间隔；剩余 common contact只能来自 genuine p-adic wrapping。本文不把 Archimedean separation误写成 modular空性，A2 仍 open。

---

## 1. compact branch quadratic

沿用

\[
\tau=10^{-M},
\qquad
s:=9+y,
\]

以及两个 rational sphere roots

\[
z_i:=\bar\zeta_i,
\qquad i=1,2.
\]

记

\[
\boxed{
c(x,y)
:=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.}
\tag{1.1}

`spontaneous-single-branch.md` 已证明每支长度方程是

\[
\boxed{
\mathscr L_i(\tau)
=55\tau^2+18(z_i-s)\tau+s^2-4sz_i-c.
}
\tag{1.2}

其 vertex 为

\[
\boxed{
\tau_i^*=\frac{9(s-z_i)}{55}
>\frac{12}{5}.
}
\tag{1.3}

并且 discriminant

\[
\mathscr D_i>0
\]
在真实 endpoint上严格成立。因此每支有两个不同 real roots。

本文只需证明

\[
\boxed{\mathscr L_i(1)>0.}
\tag{1.4}

---

## 2. `L_i` 就是 Theta root 与 sphere root 的有符号距离

`Theta_dec=0` 的 normalized third-numerator root为

\[
\boxed{
\bar\zeta_\Theta(\tau)
=
\frac{
 x^2(s^2-18s\tau+55\tau^2)
 -\frac1{100}(x+2)^2(2025x^2+y^2)
}
{2x^2(2s-9\tau)}.
}
\tag{2.1}

从定义直接展开：

\[
\boxed{
\mathscr L_i(\tau)
=2(2s-9\tau)
\bigl(\bar\zeta_\Theta(\tau)-z_i\bigr).
}
\tag{2.2}

在 `tau=1`：

\[
2s-9=2y+9>0.
\]
所以

\[
\boxed{
\mathscr L_i(1)>0
\iff
\bar\zeta_\Theta(1)>z_i.
}
\tag{2.3}

已有 `spontaneous-sphere-roots.md` 的 strict ordering

\[
\boxed{z_2<z_1.}
\tag{2.4}

因此只需证明

\[
\boxed{\bar\zeta_\Theta(1)>z_1.}
\tag{2.5}

---

## 3. 定义关键 gap

endpoint rectangle为

\[
\boxed{
\frac1{10}\le x\le\frac2{19},
\qquad
\frac{249}{250}\le y\le1.
}
\tag{3.1}

实际 endpoint使用开区间；为了单调性证书方便，这里在闭包上证明更强结论。

定义

\[
\boxed{
G(x,y)
:=\bar\zeta_\Theta(1)-z_1(x,y).
}
\tag{3.2}

这里

\[
\bar\zeta_\Theta(1)
=
\frac{
 x^2(y^2-26)
 -\frac1{100}(x+2)^2(2025x^2+y^2)
}
{2x^2(2y+9)},
\tag{3.3}

因为

\[
s^2-18s+55=y^2-26.
\]

第一 sphere root为

\[
\boxed{
 z_1
=-\frac{A_+A_{sp}}
{400x^2y^3(x+2)^2},
}
\tag{3.4}

其中

\[
A_+
=202500x^4+99x^2y^2-4xy^2-4y^2,
\]

\[
A_{sp}
=4(225x^2-y)^2-xy^2(99x-4).
\]

所有 denominator在 (3.1) 上严格为正。

---

## 4. `有限 exact 证书`：`G` 对 `x` 增、对 `y` 减

直接求导并清去正 denominator。记

\[
\partial_xG
=\frac{P_x(x,y)}
{100x^3y^3(x+2)^3(2y+9)},
\tag{4.1}

\[
\partial_yG
=\frac{P_y(x,y)}
{400x^2y^4(x+2)^2(2y+9)^2}.
\tag{4.2}

本文不把 `P_x,P_y` 的几十项展开塞进正文；checker使用 exact rational Bernstein basis对整个 rectangle (3.1) 做符号证书。

映射

\[
x=\frac1{10}
+u\left(\frac2{19}-\frac1{10}\right),
\]

\[
y=\frac{249}{250}
+v\left(1-\frac{249}{250}\right),
\qquad
0\le u,v\le1.
\]

对 `P_x` 的 bidegree `(9,5)` Bernstein coefficients全部严格正；最小系数为

\[
\boxed{
\frac{2307239659}{400000}>0.
}
\tag{4.3}

对 `-P_y` 的 bidegree `(8,6)` Bernstein coefficients也全部严格正；最小系数为

\[
\boxed{
\frac{121236551}{2000}>0.
}
\tag{4.4}

因此在整个闭 rectangle 上：

\[
\boxed{
\partial_xG>0,
\qquad
\partial_yG<0.
}
\tag{4.5}

所以 `G` 的全局最小值位于

\[
\boxed{
x=\frac1{10},\qquad y=1.}
\tag{4.6}

---

## 5. exact 最小 gap

直接代入 (4.6)：

\[
\boxed{
G\left(\frac1{10},1\right)
=\frac{28283}{3880800}>0.
}
\tag{5.1}

因此整个 endpoint box都有

\[
\boxed{
\bar\zeta_\Theta(1)-z_1
\ge
\frac{28283}{3880800}>0.
}
\tag{5.2}

再用 `z_2<z_1`：

\[
\boxed{
\bar\zeta_\Theta(1)>z_1>z_2.
}
\tag{5.3}

由 (2.2)：

\[
\boxed{
\mathscr L_1(1)>0,
\qquad
\mathscr L_2(1)>0.
}
\tag{5.4}

事实上第一支最坏边界的 exact function value为

\[
\boxed{
\mathscr L_1(1)
=\frac{28283}{176400}>0
}
\]
在 `(x,y)=(1/10,1)` 达到该最小-gap配置。

---

## 6. 两个 real roots 全部大于 `1`

每个 `L_i` 是开口向上的二次式，且：

\[
\mathscr D_i>0,
\]
所以有两个不同 real roots，记

\[
\tau_{i,-}<\tau_i^*<\tau_{i,+}.
\]

又由 (1.3)：

\[
\tau_i^*>\frac{12}{5}>1.
\]

故 `tau=1` 位于 vertex 左侧。

若较小 root满足

\[
\tau_{i,-}\le1,
\]
则 `tau=1` 位于两 roots之间或恰在 root上，从而必有

\[
\mathscr L_i(1)\le0,
\]
与 (5.4) 矛盾。

因此

\[
\boxed{
1<\tau_{i,-}<\tau_i^*<\tau_{i,+}
\qquad(i=1,2).
}
\tag{6.1}

这是对**全部 simple real roots**的统一位置定理，而不只是 repeated critical point。

---

## 7. 与真实 decimal phase 的统一 gap

当前无界 endpoint有

\[
M\ge11,
\]
所以

\[
\boxed{0<\tau=10^{-M}\le10^{-11}.}
\tag{7.1}

结合 (6.1)：

\[
\boxed{
\tau_{i,\pm}-10^{-M}
>1-10^{-11}
\qquad(i=1,2).
}
\tag{7.2}

所以 alpha-free pure spontaneous 的所有实 branch roots都与真实 decimal orbit相差接近一个完整单位；不存在任何 Archimedean near-root mechanism。

---

## 8. 严格边界

本文**没有**从 (7.2) 推出模 `p` 空性。一个很大的 `p`-adic root仍可在实数轴上离 actual phase很远。

严格新结论是：

\[
\boxed{
\text{pure spontaneous branch 的所有 real roots都 } >1,
\quad
\tau_{actual}\le10^{-11}.
}
\]

因此：

- repeated-root real criticality 已彻底排除；
- simple-root real approximation也彻底排除；
- 剩余 common carrier只能通过 genuine p-adic wrapping / decimal multiplicative orbit产生。

后续若继续 alpha-free sector，应直接研究 prime-power orbit / natural representative；继续做 real-root或普通 discriminant character已不会增加约束。

A2 仍保持 open。

---

<a id="source-spontaneous-residual-parity-doubling"></a>

> 整合来源：`spontaneous-residual-parity-doubling.md`

# A2 residual parity doubling after removing height/content

> **依赖：** `spontaneous-height-parity-ledger.md`、`spontaneous-angle-parity.md`、`spontaneous-omega-content-common.md`、`primitive-reduction.md`。
>
> **严格状态：**本文把 additive carrier 与其 pure-decimal height companion `J_H` 的 primitive relation完全除去 2-adic scale，并同时记录 angle actual/conjugate sheets 的 primitive difference。结论是：去掉共同 height part 后，additive residual 与 `J_H` residual若再次共享 odd prime，该 prime只能来自 central factor `2K-9` 或 concatenated content `omega`；angle actual/conjugate residual的共同 odd prime则只能来自 numerator/denominator prefix content。于是 generic alpha-free、noncentral、denominator-free external sector中的 odd-inert parity不能在 companion sheets之间复用同一 prime。本文是 global parity allocation lemma，不证明 residual primes不存在，也不宣称 A2 closure。

---

## 1. 记号

固定 reflection endpoint：

\[
N=10^M,
\qquad T=10^m,
\qquad A=a_2,
\qquad B=b_2,
\]

\[
Q=B+2N,
\qquad K=9N+10A.
\]

由 deep-even denominator normal form：

\[
\boxed{B=2^{M+m+1}c_ug.}
\tag{1.1}
\]

记

\[
B_0:=c_ug,
\]
所以 `B_0` 为奇数。

已有 primitive height/reduced numerator：

\[
\boxed{
\alpha=TK+a_3=\omega W_q,
\qquad H_0=c_uW_q.
}
\tag{1.2}
\]

并且

\[
\gcd(W_q,10c_ug c_Q)=1.
\tag{1.3}
\]

---

# additive pair

## 2. `T_hat` 与 `J_H` 的 exact primitive identity

`spontaneous-height-parity-ledger.md` 定义

\[
\mathcal J_H
=B^2(5K^2-36K+55)-Q^2N_0
\]
并证明

\[
\boxed{
\Theta_{\rm dec}
=T\mathcal J_H
-2B^2(2K-9)\omega W_q.
}
\tag{2.1}
\]

同时

\[
\Theta_{\rm dec}
=2^{2M+m+2}\widehat{\mathcal T}_2,
\]

\[
\mathcal J_H
=2^{2M+2}\widehat{\mathcal J}_H,
\]

且

\[
\boxed{
\widehat{\mathcal T}_2>0,
\quad
\widehat{\mathcal J}_H>0,
\quad
\widehat{\mathcal T}_2\equiv
\widehat{\mathcal J}_H\equiv3\pmod4.
}
\tag{2.2}
\]

利用

\[
T=2^m5^m,
\qquad
B=2^{M+m+1}B_0,
\]
把 (2.1) 除以 `2^{2M+m+2}`，得到本文第一条核心恒等式：

\[
\boxed{
\widehat{\mathcal T}_2
=5^m\widehat{\mathcal J}_H
-2^{m+1}B_0^2(2K-9)\omega W_q.
}
\tag{2.3}
\]

这里没有 rational normalization；所有量都是整数。

---

## 3. 共同 height part完全相同

因为 `W_q` 为 odd 且 `5\nmid W_q`，(2.3) 模 `W_q` 给

\[
\widehat{\mathcal T}_2
\equiv5^m\widehat{\mathcal J}_H
\pmod{W_q}.
\]

故有全局 gcd identity

\[
\boxed{
D_H
:=\gcd(\widehat{\mathcal T}_2,W_q)
=
\gcd(\widehat{\mathcal J}_H,W_q).
}
\tag{3.1}
\]

定义 height-free quotients

\[
\boxed{
T^\circ:=\frac{\widehat{\mathcal T}_2}{D_H},
\qquad
J^\circ:=\frac{\widehat{\mathcal J}_H}{D_H},
\qquad
W^\circ:=\frac{W_q}{D_H}.
}
\tag{3.2}
\]

按 gcd 的定义：

\[
\boxed{
\gcd(T^\circ,W^\circ)
=
\gcd(J^\circ,W^\circ)=1.
}
\tag{3.3}
\]

将 (2.3) 再除以 `D_H`：

\[
\boxed{
T^\circ-5^mJ^\circ
=-2^{m+1}B_0^2(2K-9)\omega W^\circ.
}
\tag{3.4}
\]

---

## 4. `已严格完成`：height-free additive companions只能在 central/content 上再次共享 prime

令奇素数 `p` 同时满足

\[
p\mid T^\circ,
\qquad
p\mid J^\circ.
\]

由 (3.4)：

\[
p\mid B_0^2(2K-9)\omega W^\circ.
\]

但 (3.3) 给 `p\nmid W^circ`；又

\[
\gcd(\widehat{\mathcal T}_2,10c_ug)=1
\]
而 `T^circ|widehat(T)_2`，所以

\[
p\nmid B_0=c_ug.
\]

因此：

\[
\boxed{
 p\mid T^\circ,\ p\mid J^\circ
\Longrightarrow
p\mid(2K-9)\omega.
}
\tag{4.1}
\]

换句话说，在

\[
p\nmid(2K-9)\omega
\]
的 alpha-free、noncentral sector，两个 height-free additive companions不能复用同一个 odd prime。

定义

\[
E_H:=\gcd(T^\circ,J^\circ).
\]
则逐 prime 由 (4.1) 得

\[
\boxed{
\operatorname{Supp}_{odd}(E_H)
\subseteq
\operatorname{Supp}((2K-9)\omega).
}
\tag{4.2}
\]

这不是说右端 prime一定进入 `E_H`；只是所有再次 overlap 都被压回 central/content support。

---

## 5. additive residual parity复制

由 (2.2)，`D_H` 为 odd，所以

\[
T^\circ\equiv J^\circ
\equiv3D_H^{-1}\pmod4.
\tag{5.1}
\]

因此

\[
\boxed{
T^\circ\equiv J^\circ\pmod4.
}
\tag{5.2}
\]

具体地：

\[
\boxed{
D_H\equiv1\pmod4
\Longrightarrow
T^\circ\equiv J^\circ\equiv3\pmod4,
}
\tag{5.3}
\]

\[
\boxed{
D_H\equiv3\pmod4
\Longrightarrow
T^\circ\equiv J^\circ\equiv1\pmod4.
}
\tag{5.4}
\]

所以当 height common part本身为 `1 mod 4` 时，additive actual residual和 `J_H` residual **各自**都必须携带 odd total inert parity。由 §4，generic alpha-free noncentral部分不能由同一 prime同时承担这两份 parity。

---

# angle pair

## 6. actual/conjugate angle primitive difference

沿用 height ledger 的

\[
\mathcal O_\pm
=T\mathcal U_\Omega
\pm2A^2Qb_3,
\]

\[
\widehat{\mathcal O}_\pm
:=\frac{\mathcal O_\pm}{2^{2M+m+2}}.
\]

已有

\[
\boxed{
\widehat{\mathcal O}_+>0,
\quad
\widehat{\mathcal O}_->0,
\quad
\widehat{\mathcal O}_+\equiv
\widehat{\mathcal O}_-\equiv3\pmod4.
}
\tag{6.1}
\]

写

\[
Q=2^{M+1}Q_0,
\]
以及

\[
b_3=2^{M+m+1}5^dc_Qc_u.
\]

由

\[
\mathcal O_+-\mathcal O_-=4A^2Qb_3
\]
精确除去 primitive 2-power：

\[
\boxed{
\widehat{\mathcal O}_+
-
\widehat{\mathcal O}_-
=4A^2Q_0\,5^dc_Qc_u.
}
\tag{6.2}
\]

定义

\[
D_O:=\gcd(
\widehat{\mathcal O}_+,
\widehat{\mathcal O}_-
).
\tag{6.3}
\]

则任何 odd prime `p|D_O` 必满足

\[
\boxed{
p\mid A Q_0 5 c_Qc_u.}
\tag{6.4}
\]

而 angle primitive content lemma已有

\[
\gcd(\widehat{\mathcal O}_+,c_ug)=1.
\]

故对 non-`5` genuine inert common prime可进一步缩为

\[
\boxed{
 p\mid D_O,\ p\equiv3\pmod4,\ p\ne5
\Longrightarrow
p\mid A Q_0c_Q.
}
\tag{6.5}
\]

所以真正 prefix-content-free / denominator-free external prime不可能同时命中 actual 与 conjugate angle sheets。

---

## 7. angle residual parity也成对复制

令

\[
O_+^\circ
:=\frac{\widehat{\mathcal O}_+}{D_O},
\qquad
O_-^\circ
:=\frac{\widehat{\mathcal O}_-}{D_O}.
\]

则

\[
\gcd(O_+^\circ,O_-^\circ)=1
\]
且由 (6.1)：

\[
\boxed{
O_+^\circ\equiv O_-^\circ
\equiv3D_O^{-1}\pmod4.
}
\tag{7.1}
\]

所以：

\[
\boxed{
D_O\equiv1\pmod4
\Longrightarrow
O_+^\circ\equiv O_-^\circ\equiv3\pmod4.
}
\tag{7.2}
\]

此时两份 odd inert parity必须落在两个互素 residual integers中；由 (6.5)，generic external sector中不能用同一个 inert prime实现。

若

\[
D_O\equiv3\pmod4,
\]
则两个 residual均为 `1 mod 4`，odd parity已由共同 prefix-content部分 `D_O` 承担。

---

## 8. `global parity ledger` 的严格含义

现在 actual angle/additive 两个 `3 mod 4` carriers都有一个 companion：

\[
\widehat{\mathcal O}_+
\leftrightarrow
\widehat{\mathcal O}_-,
\]

\[
\widehat{\mathcal T}_2
\leftrightarrow
\widehat{\mathcal J}_H.
\]

并且：

1. angle pair 的 common support只能来自 `A Q_0 c_Q`（加固定 `5` / 已分离 content）；
2. additive pair在除去共同 height part以后，再次 common 的 support只能来自 `(2K-9)omega`；
3. 两个 pair 各自拥有相同的 mod-4 residual orientation；
4. 因而 generic alpha-free、noncentral、prefix-content-free external sector中的 odd inert parity具有 **doubling** 性质：若 actual residual需要一份 odd parity，它的 companion residual也需要一份，而两份不能由同一 generic prime复用。

这比单独知道

\[
\widehat{\mathcal O}_{sp}\equiv
\widehat{\mathcal T}_2\equiv3\pmod4
\]
更强，因为它明确限制 residual parity如何分配。

但这仍不是 closure：不同 generic external primes完全可能分别承担这些 parity。要最终关闭 `G_sp\equiv1 mod4` 分支，还需要证明这些分离 residual primes必须通过同一个 external prime-source / decimal orbit重新会合，或由 natural representative高度排除。

---

## 9. 后续接口

下一步最值得研究的是四个 primitive carriers之间的 **cross-pair** overlap：

\[
\gcd(O_+^\circ,J^\circ),
\qquad
\gcd(T^\circ,O_-^\circ).
\]

若能证明 cross-pair overlap也只能进入已知 `omega/source/denominator/central` fixed sheets，那么在 `G_sp\equiv1 mod4` 下就会被迫出现至少四份互不复用的 generic external odd parity。再结合最新 `spontaneous-pure-root-gap.md` 的全部 real roots `>1`，这会把剩余问题进一步压成纯 decimal multiplicative-orbit / height budget，而不再含局部几何自由度。

---

<a id="source-spontaneous-sign-companion-parity"></a>

> 整合来源：`spontaneous-sign-companion-parity.md`

# A2 angle/additive 的 natural sign-companion parity pairs

> **依赖：** `spontaneous-angle-parity.md`、`spontaneous-height-parity-ledger.md`、`height-cofactor.md`。
>
> **严格状态：**本文指出 actual angle 与 actual additive primitive carriers各自都有一个自然的 third-coordinate sign companion。四个 primitive integers全部为正且 `3 mod 4`。actual/conjugate angle pair的共同 odd support只能来自 prefix numerator/denominator content；actual/conjugate additive pair的共同 odd support只能来自 central factor `2K-9` 或 third-numerator content `a_3`。因此在 generic prefix-content-free、noncentral external sector中，每一对的 odd-inert parity不能复用同一 prime。本文是 global parity allocation结构，不宣称 A2 closure。

---

## 1. 记号

固定 reflection endpoint：

\[
N=10^M,
\qquad T=10^m,
\qquad A=a_2,
\qquad B=b_2,
\]

\[
Q=B+2N,
\qquad K=9N+10A,
\]

\[
N_0=\left(\frac{9B}{2}\right)^2+A^2.
\]

并使用

\[
B=2^{M+m+1}c_ug,
\qquad
Q=2^{M+1}Q_0,
\]

\[
b_3=2^{M+m+1}5^dc_Qc_u.
\]

---

# angle sign pair

## 2. actual / conjugate angle sheets

定义

\[
\mathcal U_\Omega
=(45B^2-2AN)^2-A^2B(99B-4N),
\]

\[
\boxed{
\mathcal O_\pm
=T\mathcal U_\Omega\pm2A^2Qb_3.
}
\tag{2.1}
\]

actual spontaneous angle carrier是 `O_+`。`spontaneous-height-parity-ledger.md` 已证明

\[
\boxed{
\widehat{\mathcal O}_\pm
:=\frac{\mathcal O_\pm}{2^{2M+m+2}}>0,
\qquad
\widehat{\mathcal O}_\pm\equiv3\pmod4.
}
\tag{2.2}
\]

两者差为

\[
\mathcal O_+-\mathcal O_-=4A^2Qb_3.
\]

除去 primitive scale：

\[
\boxed{
\widehat{\mathcal O}_+
-
\widehat{\mathcal O}_-
=4A^2Q_0\,5^dc_Qc_u.
}
\tag{2.3}
\]

因此若

\[
D_O:=\gcd(\widehat{\mathcal O}_+,\widehat{\mathcal O}_-),
\]
则任何 odd prime `p|D_O` 必整除

\[
A Q_0 5c_Qc_u.
\]

又 actual angle primitive 已与 `c_ug` 本原分离，所以对 genuine non-`5` inert prime：

\[
\boxed{
 p\mid D_O
\Longrightarrow
p\mid A Q_0c_Q.
}
\tag{2.4}
\]

故 prefix numerator / denominator content-free 的 external prime不可能同时命中两张 angle sign sheets。

---

# additive sign pair

## 3. actual additive carrier与 third-numerator conjugate

定义

\[
\boxed{
\mathcal R_\Theta
:=B^2(K^2-18K+55)-Q^2N_0.
}
\tag{3.1}
\]

actual additive carrier为

\[
\boxed{
\Theta_-
:=T\mathcal R_\Theta
-2B^2(2K-9)a_3
=\Theta_{\rm dec}.
}
\tag{3.2}
\]

定义 third-numerator sign companion

\[
\boxed{
\Theta_+
:=T\mathcal R_\Theta
+2B^2(2K-9)a_3.
}
\tag{3.3}
\]

两者差：

\[
\boxed{
\Theta_+-\Theta_-
=4B^2(2K-9)a_3.
}
\tag{3.4}
\]

已有

\[
\Theta_-
=2^{2M+m+2}\widehat{\mathcal T}_2,
\]

\[
\widehat{\mathcal T}_2>0,
\qquad
\widehat{\mathcal T}_2\equiv3\pmod4.
\tag{3.5}
\]

---

## 4. conjugate additive carrier具有完全相同的 primitive orientation

由

\[
B=2^{M+m+1}c_ug,
\]
(3.4) 的 2-adic depth为

\[
2M+2m+4.
\]

相比 actual primitive scale

\[
2M+m+2,
\]
多出

\[
\boxed{m+2\ge3}
\tag{4.1}
\]
层。因此定义

\[
\boxed{
\widehat\Theta_+
:=\frac{\Theta_+}{2^{2M+m+2}}
}
\tag{4.2}
\]
后有精确整数差

\[
\boxed{
\widehat\Theta_+
-
\widehat{\mathcal T}_2
=2^{m+2}(c_ug)^2(2K-9)a_3.
}
\tag{4.3}
\]

右端被 `8` 整除，所以

\[
\boxed{
\widehat\Theta_+
\equiv
\widehat{\mathcal T}_2
\pmod8.
}
\tag{4.4}
\]

特别地

\[
\boxed{
\widehat\Theta_+\equiv3\pmod4.
}
\tag{4.5}
\]

正性也无需重新估计。当前 endpoint

\[
2K-9>0,
\qquad a_3>0,
\]
所以由 (3.4)：

\[
\Theta_+>\Theta_->0.
\]
故

\[
\boxed{
\widehat\Theta_+>0.
}
\tag{4.6}
\]

因此 additive actual / conjugate也是一对 positive primitive `3 mod 4` carriers。

---

## 5. additive sign pair 的 common support

令

\[
D_T:=\gcd(
\widehat{\mathcal T}_2,
\widehat\Theta_+
).
\tag{5.1}
\]

由 (4.3)，`D_T` 为 odd 且

\[
D_T
\mid
(c_ug)^2(2K-9)a_3.
\]

但已有本原性

\[
\gcd(\widehat{\mathcal T}_2,10c_ug)=1.
\]

所以：

\[
\boxed{
D_T\mid |(2K-9)a_3|.
}
\tag{5.2}
\]

逐 prime 写就是

\[
\boxed{
 p\mid\widehat{\mathcal T}_2,
\ p\mid\widehat\Theta_+
\Longrightarrow
p\mid(2K-9)a_3.
}
\tag{5.3}
\]

因此 noncentral 且 third-numerator-content-free 的 generic external prime不可能同时命中 additive actual / conjugate sheets。

---

## 6. 两对 parity 的共同抽象结构

现在有四个 positive `3 mod 4` primitive integers：

\[
\boxed{
\widehat{\mathcal O}_+,
\quad
\widehat{\mathcal O}_-,
\quad
\widehat{\mathcal T}_2,
\quad
\widehat\Theta_+.
}
\tag{6.1}
\]

每一对都满足：

- actual 与 conjugate同为 `3 mod 4`；
- 去掉 pair gcd 后，两个 quotient互素且具有相同 mod-4 orientation；
- pair gcd若为 `1 mod 4`，两个 quotient都会是 `3 mod 4`，因此必须分别携带 odd inert parity；
- generic external prime不能在同一 sign pair中重复承担这两份 parity。

两对的例外 support完全显式：

\[
\boxed{
\begin{array}{c|c}
\text{pair}&\text{possible common odd support}\\ \hline
(O_+,O_-)&A Q_0c_Q\quad(\text{plus fixed }5/content)\\
(\Theta_-,\Theta_+)&(2K-9)a_3.
\end{array}}
\tag{6.2}
\]

因此 global `G_sp` parity问题现在不再只有两个 carrier；每个 actual carrier都带一个自然 companion。若最终要维持 `G_sp\equiv1 mod4`，odd parity必须在这四张 sheets及其显式 content exceptions之间完成一致分配。

---

## 7. 下一步：cross-sign sphere

同一 sign pair内部的 overlap已经由本文固定。剩余真正可能让 parity重新合流的是 cross-sign pair：

\[
(O_-,\Theta_-),
\qquad
(O_+,\Theta_+).
\]

它们不是任意新方程：`O_-` 对应第三分母 angle root取相反符号，`Theta_+` 对应第三分子 additive root取相反符号。把这些 sign roots代回 exact sphere即可得到 cross-sign pure-prefix norms。

若 cross-sign norms也只能回流到已知 height/source/content sheets，那么 `G_sp\equiv1 mod4` 所要求的分居 parity会被进一步强迫成多个互不复用的 pure external decimal orbits。

---

<a id="source-spontaneous-single-branch-syzygy"></a>

> 整合来源：`spontaneous-single-branch-syzygy.md`

# A2 single-branch 上的 `C_*` 精确线性分解

> **依赖：** `spontaneous-single-branch.md`、`spontaneous-prefix-branch-audit.md`。
>
> **严格状态：**本文证明 branch-collision/central kernel `C_*` 在任意一个 compact single branch 上自身分解成两个线性 length/orientation 因子。由此得到一个关键分离：noncentral repeated root 自动满足 `C_*≠0`；若 repeated root 与 `C_*` 同时接触，则必回到 central line `2K-9=0`。同时得到 repeated-root 的精确 square-class law。本文仍**不宣称 A2 全局关闭**。

---

## 1. compact branch

沿用

\[
\tau=10^{-M},
\qquad
s=9+y,
\]

\[
c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2},
\]

以及任意一个有限 sphere orientation

\[
z=z_i.
\]

`spontaneous-single-branch.md` 的 branch quadratic 为

\[
\boxed{
\mathscr L(\tau,z)
=55\tau^2+18(z-s)\tau+s^2-4sz-c.
}
\tag{1.1}

central kernel 记为

\[
\boxed{
\begin{aligned}
C_*={}&164025x^4+656100x^3
+2381x^2y^2+41400x^2y\\
&+842400x^2+324xy^2+324y^2.
\end{aligned}}
\tag{1.2}

---

## 2. `已严格完成`：`C_*` 模 branch quadratic 完全线性化

直接展开并按 `tau` 对 (1.1) 做 Euclidean division，得到精确恒等式

\[
\boxed{
\begin{aligned}
C_*={}&100x^2(9\tau-2s)
(495\tau+162z-52s)\\
&-8100x^2\mathscr L(\tau,z).
\end{aligned}}
\tag{2.1}

因此在任意真实 branch root

\[
\mathscr L(\tau,z_i)=0
\]
上：

\[
\boxed{
C_*
=100x^2(9\tau-2s)
(495\tau+162z_i-52s).
}
\tag{2.2}

第一因子与旧 central line 精确相同。因为

\[
K=\frac{s}{\tau},
\]
所以

\[
2K-9
=\frac{2s-9\tau}{\tau}.
\tag{2.3}

故

\[
\boxed{9\tau-2s=0\iff2K-9=0.}
\tag{2.4}

这说明 `C_*` 在 single branch 上并不是新的高次自由对象；它就是 central factor 乘另一个线性 orientation factor。

---

## 3. `已严格完成`：repeated root 与 `C_*` 相交必回 central

single branch 的 repeated-root tangent 为

\[
\boxed{55\tau=9(s-z).}
\tag{3.1}

定义

\[
U:=81z+29s.
\tag{3.2}

在 (3.1) 下：

\[
9\tau-2s
=-\frac{U}{55},
\tag{3.3}

而第二线性因子变成

\[
495\tau+162z-52s
=U.
\tag{3.4}

所以 (2.2) 精确退化为

\[
\boxed{
C_*=-\frac{20}{11}x^2U^2.
}
\tag{3.5}

若 genuine prime 满足

\[
p\ne2,5,11,
\qquad p\nmid x,
\]
并且 repeated root 同时有

\[
p\mid C_*,
\]
则 (3.5) 强迫

\[
U\equiv0\pmod p.
\]
再由 (3.3)：

\[
9\tau-2s\equiv0,
\]
即

\[
\boxed{
\text{repeated root}+C_*=0
\Longrightarrow
2K-9=0.
}
\tag{3.6}

因此：

\[
\boxed{
\text{noncentral single-branch repeated root}
\Longrightarrow C_*\ne0.
}
\tag{3.7}

这把 central bad reduction 与真正 moving singular branch 严格分离。

---

## 4. `已严格完成`：repeated-root 的 `C_*` square class

在 (3.5) 且 `C_*` 为单位时，对 odd prime `p` 取 Legendre symbol。因为 `x^2`、`4` 是平方，且 inverse 与原数有相同 quadratic character：

\[
\left(\frac{11^{-1}}p\right)
=\left(\frac{11}p\right),
\]
故

\[
\boxed{
\left(\frac{C_*}{p}\right)
=
\left(\frac{-55}{p}\right).
}
\tag{4.1}

对本文关心的 inert prime

\[
p\equiv3\pmod4,
\]
进一步有

\[
\boxed{
\left(\frac{C_*}{p}\right)
=-\left(\frac{55}{p}\right).
}
\tag{4.2}

特别地，若同一个 singular prime 还属于 external discriminant-zero 子通道，旧条件给

\[
\left(\frac{55}{p}\right)=1,
\]
于是

\[
\boxed{
\left(\frac{C_*}{p}\right)=-1.
}
\tag{4.3}

这是一条严格 necessary character，而不是 closure。当前没有独立证明 external singular branch 上 `C_*` 必为平方，所以 (4.3) 不能单独宣称矛盾。

---

## 5. 同一个 identity 也解释 compact discriminant

`spontaneous-single-branch.md` 的 discriminant 为

\[
\mathscr D
=324z^2+232sz+104s^2+220c.
\]
它还有等价形式

\[
\boxed{
405x^2\mathscr D
=20x^2(81z+29s)^2+11C_*.
}
\tag{5.1}

证明只需把

\[
23s^2+81c
\]
化简：

\[
\boxed{
23s^2+81c=\frac{C_*}{100x^2}.
}
\tag{5.2}

而 quadratic 在自己的根 `tau` 处满足

\[
\mathscr D=(\mathscr L'(\tau))^2.
\]
把这一平方关系代入 (5.1) 并因式分解，正好恢复 (2.2)。所以

- compact discriminant；
- central kernel `C_*`；
- branch tangent；
- branch collision

其实是同一个二次几何的不同投影，不能重复计作四个独立 obstruction。

---

## 6. 当前开放核

本文件把 single-branch singularity 进一步收紧成：

\[
\boxed{
\begin{gathered}
\mathscr L_i(10^{-M})\equiv0,\\
55\cdot10^{-M}\equiv9(s-z_i),\\
C_*\ne0,\\
\left(\frac{C_*}{p}\right)=\left(\frac{-55}{p}\right)
\end{gathered}}
\]
对 noncentral repeated root 成立。

所以下一步若继续处理 singular moving prime，最值得找的不是另一个 branch discriminant，而是 `C_*` 的**独立** square class / source meaning；若无法独立固定它，则 character route应降级，转去清分母 tangent 与 decimal multiplicative orbit 的 prime-power 同步。

---

<a id="source-spontaneous-single-branch"></a>

> 整合来源：`spontaneous-single-branch.md`

# A2 pure-spontaneous 单 branch 的 compact quadratic

> **依赖：** `spontaneous-sphere-roots.md`。
>
> **严格状态：**本文不再使用展开后的几十项 `Q_1,Q_2`，而把每一支写成 `Theta` root 与对应 sphere root 相交得到的统一小二次式。由此 single-branch repeated root 有显式临界长度 `tau_i^*`，并证明其真实 Archimedean 临界点统一大于 `12/5`，而实际 `10^{-M}<10^{-11}`。这说明 single-branch singularity 只能是纯 p-adic wrapping，不是实数临界退化。本文仍**不宣称 A2 全局关闭**。

---

## 1. 两个 sphere orientation

沿用

\[
\tau=10^{-M},
\qquad
s:=9+y,
\]

以及 `spontaneous-sphere-roots.md` 的两个有理函数根

\[
z_i:=\bar\zeta_i,
\qquad i=1,2.
\]

再记

\[
\boxed{
c(x,y):=
\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.}
\tag{1.1}
\]

`Theta_dec=0` 的 normalized root 为

\[
\bar\zeta_\Theta(\tau)
=
\frac{
 x^2(s^2-18s\tau+55\tau^2)
 -\frac1{100}(x+2)^2(2025x^2+y^2)
}
{2x^2(2s-9\tau)}.
\tag{1.2}
\]

---

## 2. `已严格完成`：每个 `Q_i` 只是同一个小二次模板

令

\[
\bar\zeta_\Theta(\tau)=z_i.
\]

从 (1.2) 直接清分母，除以 `x^2`，得到

\[
\boxed{
\mathscr L_i(\tau)
:=55\tau^2
+18(z_i-s)\tau
+s^2-4sz_i-c
=0.
}
\tag{2.1}

因此 `spontaneous-prefix-eliminant.md` 的 `Q_1,Q_2` 只是

\[
\boxed{
\mathcal Q_i
=\text{(sphere-root denominator)}\times\mathscr L_i
}
\tag{2.2}

的 primitive integer clearing。真正的长度几何完全由 (2.1) 读取，不必反复展开几十项系数。

---

## 3. `已严格完成`：single-branch repeated root 的唯一临界长度

(2.1) 对 `tau` 求导：

\[
\mathscr L_i'(\tau)
=110\tau+18(z_i-s).
\]

所以 repeated root 若存在，临界点唯一：

\[
\boxed{
\tau_i^*
=\frac{9(s-z_i)}{55}.
}
\tag{3.1}

相应 discriminant 为

\[
\boxed{
\begin{aligned}
\mathscr D_i
&:=\operatorname{disc}_\tau(\mathscr L_i)\\
&=324z_i^2+232sz_i+104s^2+220c.
\end{aligned}}
\tag{3.2}

完成平方：

\[
\boxed{
\mathscr D_i
=324\left(z_i+\frac{29s}{81}\right)^2
+\frac{5060}{81}s^2
+220c.
}
\tag{3.3}

其中

\[
5060=2^2\cdot5\cdot11\cdot23.
\]

因此在真实 endpoint `x,y>0` 上

\[
\boxed{\mathscr D_i>0.}
\tag{3.4}

这不是模素数排除；它只是证明真实二次式没有重根。模 `p` 的 repeated-root channel 仍可由 `D_i≡0` 产生。

---

## 4. `已严格完成`：真实临界长度远离 decimal orbit

endpoint box 中

\[
y>\frac{249}{250}
\quad\Longrightarrow\quad
s>\frac{2499}{250}.
\]

`spontaneous-sphere-roots.md` 又给

\[
z_i<-rac{1223295069}{256000000}
\qquad(i=1,2).
\]

代入 (3.1)：

\[
\tau_i^*
>
\frac9{55}
\left(
\frac{2499}{250}
+rac{1223295069}{256000000}
\right)
=
\frac{34040439621}{14080000000}.
\]

因此

\[
\boxed{
\tau_i^*>2.4176>\frac{12}{5}.
}
\tag{4.1}

另一方面当前无界核 `M>=11`，所以实际 decimal length phase 为

\[
\boxed{
0<\tau=10^{-M}\le10^{-11}.
}
\tag{4.2}

于是实数轴上：

\[
\boxed{
\tau_i^*-\tau>\frac{12}{5}-10^{-11}.
}
\tag{4.3}

single-branch singularity 的临界位置甚至不在 `[0,1]` 内，而真实 decimal orbit 已贴近 `0`。

---

## 5. `已严格完成`：modular singular branch 只剩一条线性 length target

若某个 odd prime `p` 使 `Q_i` 在真实 `tau=10^{-M}` 处成为 repeated root，则在所有 sphere-root denominator 为单位的 genuine channel：

\[
\boxed{
55\tau\equiv9(s-z_i)\pmod p,
}
\tag{5.1}

并且

\[
\boxed{
\mathscr D_i\equiv0\pmod p.
}
\tag{5.2}

反过来，(5.1) 与 `L_i(tau)=0` 等价于 (5.2)。所以 single-branch bad reduction 不再需要一个 degree-16/20 的未命名判别多项式；它就是 sphere orientation `z_i` 与一条显式 length tangent 的交点。

如果清去 `z_i` 的分母，(5.1) 对每一支都只给一个关于 `tau` 的**一次** pure-prefix polynomial。这是后续与 `tau=10^{-M}` 的 multiplicative orbit 做 Hensel 同步时应使用的规范形式。

---

## 6. 证明边界与下一步

本文件严格证明：

1. `Q_1,Q_2` 各自是统一 quadratic template (2.1)；
2. 每支 repeated root 只有唯一临界长度 (3.1)；
3. 真实 endpoint 的临界长度统一 `>12/5`，实际 `tau<=10^-11`；
4. modular bad reduction 可改写为一次 length tangent (5.1)。

但 (4.3) 仍只是 Archimedean separation；`p | Q_i`、`p | D_i` 可以通过取模绕回。因此尚不能据此关闭 moving simple/singular prime。

下一步应把 (5.1) 清分母后与：

- external discriminant line `E_W=0`；
- `D_src / Delta_pref`；
- 或真实 `10^{-M}` multiplicative orbit

做 resultant / Hensel 同步。若能证明 singular tangent 的 required prime-power depth 超过清分母整数高度，才可把这条实数远离转成真正空性。

---

<a id="source-spontaneous-source-common-gate"></a>

> 整合来源：`spontaneous-source-common-gate.md`

# A2 source angle-extra 进入 additive common gcd 的 pure-prefix gate

> **依赖：** `spontaneous-source-equal-depth-nogo.md`、`spontaneous-prefix-eliminant.md`、`spontaneous-angle.md`。
>
> **严格状态：**source equal-depth angle extra-lift本身是可解的二阶 Hensel自由度，不能靠 source 局部系统排除。本文加入真正独立的 additive condition `Theta_dec=0` 与 exact sphere：在 source first-layer curve上，第三块再次完全消去，sphere numerator塌成一个显式 quadratic 的平方。因此 source-supported angle prime要进一步进入 angle/additive common gcd，必须命中一个只含 `(x,tau=10^-M)` 的 pure-prefix decimal gate `C_src=0`。该 gate在真实 endpoint box 中统一大于 `448`，所以 common contact只能来自 p-adic wrapping。本文不排除这些 modular roots，也不宣称 A2 全局关闭。

---

## 1. source first-layer curve

沿用

\[
d=225x^2-y,
\qquad
\Phi_s=(99x-4)r_s-2x-4.
\]

真正 source excess prime在 first layer 满足

\[
d\equiv0,
\qquad
\Phi_s\equiv0.
\]

因此令

\[
\boxed{y=225x^2,}
\tag{1.1}

\[
A:=99x-4,
\qquad
\boxed{r_s=\frac{2(x+2)}A.}
\tag{1.2}

source separation保证

\[
p\nmid x(x+2)A.
\tag{1.3}

第三分母 normalized phase

\[
\bar w:=\frac{b_3}{T10^M}
\]
满足 `r_s=x/bar w`，所以

\[
\boxed{
\bar w=\frac{xA}{2(x+2)}.}
\tag{1.4}

---

## 2. additive root恢复第三分子

记

\[
\tau:=10^{-M},
\qquad
s:=9+y,
\]

以及

\[
\bar\zeta:=\frac{a_3}{T10^M}.
\]

`Theta_dec=0` 在 noncentral channel给

\[
\boxed{
\bar\zeta_\Theta
=
\frac{
 x^2(s^2-18s\tau+55\tau^2)
 -\frac1{100}(x+2)^2(2025x^2+y^2)
}
{2x^2(2s-9\tau)}.}
\tag{2.1}

本文只处理 denominator为单位的 generic noncentral source/common channel；central line已由 `spontaneous-prefix-branch-audit.md` 单列。

---

## 3. `已严格完成`：source first-layer 上 sphere numerator 是一个完整平方

exact sphere为

\[
 x^2\bar w^2(s+\bar\zeta)^2
=(x+2+\bar w)^2
\left(
\frac{2025x^2+y^2}{100}\bar w^2+x^2\bar\zeta^2
\right).
\tag{3.1}

把 (1.1)、(1.4)、(2.1) 全部代入 (3.1)，清去 rational denominators。直接因式分解得到

\[
\boxed{
\operatorname{num}(\text{sphere})
=-x^2(25x^2+1)\,\mathcal C_{\rm src}(x,\tau)^2.}
\tag{3.2}

其中

\[
\boxed{
\begin{aligned}
\mathcal C_{\rm src}(x,\tau)
={}&440(x+2)^2\tau^2\\
&+81(9401x^4-2392x^3-1600x^2-64x-64)\tau\\
&-324x(99x-4)(25x^2+1)(49x^2-4x-2).
\end{aligned}}
\tag{3.3}

对 genuine source prime，`x` 为单位；而在 source first layer

\[
2025x^2+y^2
=2025x^2(25x^2+1),
\]
且 base norm为单位，所以

\[
p\nmid25x^2+1.
\tag{3.4}

因此 (3.2) 给出精确 necessary-and-sufficient first-layer gate：

\[
\boxed{
\text{source first-layer angle root}+\Theta_{\rm dec}=0+\text{sphere}
\iff
\mathcal C_{\rm src}(x,\tau)=0\pmod p,}
\tag{3.5}

在本文列出的 genuine/noncentral denominator单位条件下成立。

这就是 source angle-extra 是否进一步成为 additive common carrier 的独立外部接口。

---

## 4. 二阶 source correction完全不进入 common gate

`spontaneous-source-equal-depth-nogo.md` 把 source equal-depth shell写成

\[
y=225x^2-\varepsilon d_1,
\]

\[
r_s=\frac{2(x+2)+\varepsilon^2\phi_2}{99x-4},
\qquad\varepsilon=p^h.
\]

angle extra-lift只是在二阶唯一选择 `phi_2`。而 (3.3) 完全不含

\[
d_1,\quad\phi_2,\quad\sigma^\sharp,\quad\Psi_9^\sharp.
\]

因此 source prime是否进入 additive common gcd，第一层已经由

\[
\boxed{\mathcal C_{\rm src}(x,10^{-M})\equiv0\pmod p}
\tag{4.1}

独立决定；不能通过重新调节二阶 source correction来改变。

这正是 source equal-depth no-go 所缺的“source 外部约束”。

---

## 5. `已严格完成`：defect 坐标中的短表达

真实 denominator defect记为

\[
u:=10x-1=\frac{H}{5^{M-1}},
\qquad
0<u<\frac1{19}.
\]

所以

\[
x=\frac{1+u}{10}.
\]

代入 (3.3) 并乘 `10000`，得到整数系数表达

\[
\boxed{
\begin{aligned}
10000\mathcal C_{\rm src}
={}&44000(u+21)^2\tau^2\\
&+81(9401u^4+13684u^3-175354u^2\\
&\hspace{22mm}-418156u-878519)\tau\\
&-81(u+1)(99u+59)(u^2+2u+5)\\
&\hspace{22mm}\cdot(49u^2+58u-191).
\end{aligned}}
\tag{5.1}

这比 expanded `(x,tau)` polynomial更适合 endpoint natural representative：所有真实 defect都只通过小正参数 `u` 出现。

---

## 6. `已严格完成`：真实 endpoint 上 `C_src` 统一远离零

在

\[
0<u<1/19
\]
中：

\[
u+1>1,
\qquad99u+59>59,
\qquad u^2+2u+5>5.
\]

又

\[
49u^2+58u-191
<\frac{49}{19^2}+\frac{58}{19}-191
< -187.
\]

因此 (5.1) 最后一项为正，而且除以 `10000` 后单独给出粗下界

\[
\frac{81\cdot59\cdot5\cdot187}{10000}>446.
\tag{6.1}

更直接使用原 `x`-box

\[
\frac1{10}<x<\frac2{19}
\]
可得到稍强的 constant-term 下界：

\[
\begin{aligned}
&-324x(99x-4)(25x^2+1)(49x^2-4x-2)\\
&\qquad>
324\cdot\frac1{10}\cdot\frac{59}{10}\cdot\frac54\cdot\frac{678}{361}
=
\frac{1620081}{3610}
>448.77.
\end{aligned}
\tag{6.2}

线性 coefficient

\[
H_4(x):=9401x^4-2392x^3-1600x^2-64x-64
\]
满足粗界

\[
|H_4(x)|<93
\tag{6.3}

因为各绝对项在 `x<2/19` 上总和小于 `93`。

而实际

\[
0<\tau=10^{-M}\le10^{-11}.
\]
因此线性项的绝对值小于

\[
81\cdot93\cdot10^{-11}<8\cdot10^{-8}.
\tag{6.4}

二次项非负。综合：

\[
\boxed{
\mathcal C_{\rm src}(x,10^{-M})>448.77-8\cdot10^{-8}>448.}
\tag{6.5}

所以 source→common gate在真实轴上与零有巨大的统一距离。

---

## 7. `审计`：这仍不是 modular contradiction

(6.5) 不能推出

\[
p\nmid\mathcal C_{\rm src}
\]
因为 `p`-adic divisibility不要求实数接近零。其意义与此前 sphere-root sign gap相同：所有 source→common contact都必须靠真正的 modular wrapping实现。

若要把 (6.5) 升级为空性，必须比较清分母后的自然整数 representative 与 source prime-power depth，或与 decimal orbit `tau=10^-M` 做高阶同步。

---

## 8. common gate 的 tau-discriminant

把 (3.3) 看成 `tau` 的 quadratic，其 discriminant为

\[
\boxed{
\operatorname{Disc}_\tau(\mathcal C_{\rm src})
=81\mathcal D_{\rm srccom}(x),}
\tag{8.1}

其中

\[
\boxed{
\begin{aligned}
\mathcal D_{\rm srccom}(x)={}&
8012458881x^8-332013104x^7+1027170624x^6\\
&+111485312x^5+130846848x^4+25281536x^3\\
&+12020736x^2+888832x+331776.
\end{aligned}}
\tag{8.2}

所以即使 source angle-extra已经存在，进一步进入 common gcd仍要求 decimal length在一个明确 quadratic extension 中选根。本文不把该 discriminant character当成 closure；它只是后续 decimal-orbit Hensel同步的规范对象。

---

## 9. 更新后的 source residual frontier

source angle residual现在具有两层彼此独立的结构：

1. source 局部二阶 extra-lift：
   \[
   \phi_2=
   \frac{8(x+2)}{50625(99x-4)x^5}d_1^2;
   \]
   这是 simple local freedom；
2. additive common gate：
   \[
   \mathcal C_{\rm src}(x,10^{-M})=0\pmod p;
   \]
   这是 pure-prefix/decimal external constraint。

因此 `G_sp=1 mod4` 中 source-over-saturated angle residual能否保持为“只在 angle side出现”的 prime，已经不再是模糊问题，而精确等价于：source extra-lift成立但 `C_src` 不成立。

下一步最值得做的是把 `C_src` 与 `D_src` / source length orbit / natural integer representative联立；继续只研究 `phi_2` 已无新增信息。

---

<a id="source-spontaneous-source-common-integer"></a>

> 整合来源：`spontaneous-source-common-integer.md`

# A2 source→common gate 的自然整数代表与 corrected transverse audit

> **依赖：** `spontaneous-source-common-gate.md`、`spontaneous-source-equal-depth-nogo.md`、`spontaneous-source-saturation-parity.md`、`spontaneous-source-prefix-simple.md`。
>
> **严格状态：**本文把 source→additive-common 的 first-layer gate `C_src(x,tau)` 精确乘回真实 denominator defect，并审计其 singular bad reduction。旧版 transverse checker 曾在 `F_p[epsilon]/(epsilon^3)` 中把 singular residue 当成精确零点，因而漏掉真实整数 representative 的 `p`-adic carry `C_src(x0,tau0)/p`；本文修正这一点。修正后，唯一 singular prime `p=1746991` 在 source half-depth `h>=2` 仍严格死亡，但 `h=1` 不死亡：二阶 full-system equation恰留下两个 normalized transverse templates `D=+-16651 mod p`。因此不存在沿 source half-depth 无界增长的 singular tree，但浅层 `h=1` 仍需继续审计。A2 仍未全局关闭。

---

## 1. source→common first-layer quadratic

在 source first layer

\[
d:=225x^2-y=0,
\qquad
\Phi_s=(99x-4)r_s-2x-4=0,
\]
有

\[
y=225x^2,
\qquad
r_s=\frac{2(x+2)}{99x-4}.
\]

把 `Theta_dec=0` 恢复出的第三分子代回 exact sphere 后，清分母 numerator 精确为

\[
-x^2(25x^2+1)\mathcal C_{\rm src}(x,\tau)^2,
\qquad \tau=10^{-M},
\tag{1.1}
\]

其中

\[
\boxed{
\begin{aligned}
\mathcal C_{\rm src}(x,\tau)
={}&440(x+2)^2\tau^2\\
&+81(9401x^4-2392x^3-1600x^2-64x-64)\tau\\
&-324x(99x-4)(25x^2+1)(49x^2-4x-2).
\end{aligned}}
\tag{1.2}
\]

对 genuine source prime，`x(99x-4)(25x^2+1)` 均为单位，所以 source-supported angle prime进入 additive common first layer 必须且只需满足

\[
\boxed{\mathcal C_{\rm src}(x,10^{-M})\equiv0\pmod p.}
\tag{1.3}
\]

---

# 第一部分：自然整数代表

## 2. defect integerization

令

\[
F:=5^{M-1},
\qquad E:=2^{M-1},
\qquad
x=\frac{F+H}{10F},
\qquad
\tau=\frac1{10EF}.
\]

则

\[
10E^2F^6\,(10000\mathcal C_{\rm src})
=\mathcal K_{\rm src}(H,E,F),
\tag{2.1}
\]

其中

\[
\boxed{
\begin{aligned}
\mathcal K_{\rm src}
={}&4400F^2(H+21F)^2\\
&+81EF\mathcal P_4(H,F)\\
&-810E^2(H+F)(99H+59F)\\
&\qquad\cdot(H^2+2HF+5F^2)(49H^2+58HF-191F^2),
\end{aligned}}
\tag{2.2}
\]

\[
\boxed{
\begin{aligned}
\mathcal P_4(H,F)
={}&9401H^4+13684H^3F-175354H^2F^2\\
&-418156HF^3-878519F^4.
\end{aligned}}
\tag{2.3}
\]

对 genuine `p!=2,5`，`E,F` 为单位，因此作为 first-layer projected gate：

\[
\boxed{p^k\mid\mathcal C_{\rm src}
\iff p^k\mid\mathcal K_{\rm src}.}
\tag{2.4}
\]

注意：`C_src` 是限制在 `d=Phi_s=0` slice 后得到的投影。式 (2.4) **不能**单独读取 full higher source/common system 的 transverse depth；后文显式保留 `d,Phi_s`。

---

# 第二部分：projected singular bad set

## 3. fixed bad primes

把 `C_src` 看成 `tau` 的 quadratic：

\[
\Disc_\tau(\mathcal C_{\rm src})=81\mathcal D_{\rm sc}(x),
\tag{3.1}
\]

\[
\begin{aligned}
\mathcal D_{\rm sc}(x)={}&8012458881x^8-332013104x^7+1027170624x^6\\
&+111485312x^5+130846848x^4+25281536x^3\\
&+12020736x^2+888832x+331776.
\end{aligned}
\tag{3.2}
\]

其 `x`-判别式精确分解：

\[
\boxed{
\Disc_x(\mathcal D_{\rm sc})
=2^{96}3^55^4 11^4 101^{24}\cdot109\cdot233
\cdot1746991\cdot405504443^2.}
\tag{3.3}
\]

所以 genuine non-`3` inert projected singularity 只需审计

\[
11,\quad1746991,\quad405504443.
\]

- `p=11`：`dC/dtau` 在 `F_11` 无根，因此无 finite singular projection；
- `p=405504443`：`gcd(D_sc,D_sc')` 是一个在 `F_p` 无根的二次式；
- 只剩
  \[
  \boxed{p=1746991.}
  \]

该 prime 唯一 genuine singular residue为

\[
\boxed{x_0=1362653,\qquad \tau_0=807263\pmod p.}
\tag{3.4}
\]

且

\[
\mathcal C_{\rm src}
=\partial_x\mathcal C_{\rm src}
=\partial_\tau\mathcal C_{\rm src}=0\pmod p.
\tag{3.5}
\]

所有 source/noncentral denominator factors均为单位。

---

## 4. projected gate 本身不能升到 `p^2`

取 (3.4) 的最小非负整数 representatives。直接 exact evaluation：

\[
\boxed{
\frac{\mathcal C_{\rm src}(x_0,\tau_0)}p
\equiv1642591\not\equiv0\pmod p.}
\tag{4.1}
\]

因为两个一阶 projected derivatives 都被 `p` 整除，任意

\[
x=x_0+pX,\qquad\tau=\tau_0+pT
\]
仍满足

\[
\boxed{v_p(\mathcal C_{\rm src})=1.}
\tag{4.2}
\]

这只证明 `d=Phi=0` 的 projected gate不能自己升到 `p^2`，**并不**排除 source transverse correction。

---

# 第三部分：corrected transverse audit

## 5. source equal-depth coordinates

若

\[
p^{2h}\Vert\sigma,\qquad h\ge1,
\]
且进入唯一可能产生 angle extra 的 equal-depth shell，写

\[
\varepsilon=p^h,
\qquad
d=\varepsilon D,\quad D\in\mathbf Z_p^\times,
\]

\[
\Phi_s=\varepsilon^2\phi,
\qquad
r_s=\frac{2(x+2)+\varepsilon^2\phi}{99x-4}.
\tag{5.1}
\]

angle extra-lift唯一给

\[
\phi\equiv
\frac{8(x+2)}{50625(99x-4)x^5}D^2\pmod p.
\tag{5.2}
\]

在 `p=1746991,(x_0,tau_0)` 上：

\[
\boxed{\phi\equiv1007439D^2\pmod p.}
\tag{5.3}
\]

---

## 6. exact tangency 与 valuation data

令 `S_Theta` 为用 `Theta_dec=0` 恢复第三分子后代回 sphere 的 rational residual。沿 source linear line `Phi_s=0`，在

\[
y_0=225x^2
\]
处有 exact tangency

\[
\boxed{
\left.\partial_y\mathscr S_\Theta\right|_{y=y_0}
=\mathcal C_{\rm src}(x,\tau)
\frac{\mathcal P_d(x,\tau)}
{23328(x+2)^4(50x^2+2-\tau)^3}.}
\tag{6.1}
\]

在 singular residue (3.4)，不仅 `C_src=0 mod p`，对应 `P_d` 也被 `p` 整除；exact integer/rational evaluation 给出：

\[
\boxed{
\begin{array}{c|c|c}
\text{coefficient}&v_p&\text{normalized residue}\\ \hline
\mathscr S_\Theta|_{d=\Phi=0}&2&572710\\
\partial_d\mathscr S_\Theta|_0&2&707577\\
\frac12\partial_d^2\mathscr S_\Theta|_0&0&32070\\
\partial_{\Phi}\mathscr S_\Theta|_0&0&1066442=-680549
\end{array}}
\tag{6.2}
\]

这里第一行就是旧 checker 漏掉的 `p`-adic carry。它来自真实整数 representative 的

\[
\mathcal C_{\rm src}(x_0,\tau_0)=p\cdot(1642591+O(p)).
\]

---

## 7. `已严格完成`：`h=1` 留下两个 transverse templates

取 `h=1`：

\[
d=pD,\qquad\Phi_s=p^2\phi.
\]

因为 projected `x,tau` 一阶修正不改变 `C_src/p mod p`，而 `partial_d S` 已有额外 `p^2`，二阶 sphere 方程精确化为

\[
\boxed{
\frac{\mathscr S_\Theta}{p^2}
\equiv572710+32070D^2-680549\phi\pmod p.}
\tag{7.1}
\]

代入 angle correction (5.3)：

\[
\boxed{
572710+286982D^2\equiv0\pmod{1746991}.}
\tag{7.2}
\]

即

\[
D^2\equiv1231223\pmod p.
\tag{7.3}
\]

而该 residue 是平方，恰有两个根：

\[
\boxed{D\equiv16651\quad\text{或}\quad1730340=-16651\pmod p.}
\tag{7.4}
\]

两根均为单位；对应 angle correction相同：

\[
\boxed{\phi\equiv987987\pmod p.}
\tag{7.5}
\]

因此旧版“`h=1` 无 lift”结论撤回。正确结论是：

\[
\boxed{
\text{the unique singular projected prime has exactly two normalized }h=1
\text{ transverse templates at second order}.}
\tag{7.6}
\]

这两条模板是否继续满足更高 common/additive depth，需要独立审计；本文不宣称它们为空。

---

## 8. `已严格完成`：`h>=2` 仍严格死亡

若 `h>=2`，由 (4.2) projected slice 的 `C_src` 始终只有一层，所以 `C_src^2` 在 sphere 中产生不可消失的 depth-2 主项，normalized residue就是 (6.2) 的 `572710`。

source transverse 项的最低可能深度为：

- linear `d`：`v_p(partial_d S)+h >= 2+h >=4`；
- quadratic `d^2`：`2h>=4`；
- `Phi_s` correction：`2h>=4`。

因此没有任何 transverse term能触及 depth `2` 主项：

\[
\boxed{
h\ge2\Longrightarrow\text{no full source/common lift at }p=1746991.}
\tag{8.1}
\]

所以 singular behavior在 source half-depth方向已经完全有界：

\[
\boxed{
\text{no singular source→common tree can persist to unbounded }h;
\text{ only the two shallow }h=1\text{ templates survive this audit}.}
\tag{8.2}
\]

---

# 第四部分：与 simple source prefix 的接口

## 9. `e`-Hensel 仍是 unit-slope

`spontaneous-source-prefix-simple.md` 给出

\[
D_{\rm src}
=\frac{9E^2}{4}(5F^2+18FH+9H^2)+9EF e,
\tag{9.1}
\]

所以 genuine source prime上

\[
\partial_eD_{\rm src}=9EF
\]
为单位。每个 `(H,M,p^h)` 只唯一确定一个 `e mod p^h`：

\[
4Fe\equiv-E(5F^2+18FH+9H^2)\pmod{p^h}.
\tag{9.2}
\]

而 `K_src` 不含 `e`，故消去 `e` 不会产生新的 residual。simple source/common frontier仍是 `(H,M)` common orbit + 唯一 `e` representative。

---

## 10. 更新后的严格 frontier

source-supported common channel目前严格分成：

1. **generic simple projected roots**：继续做 decimal/natural-representative synchronization；
2. **唯一 singular projected prime `1746991`**：
   - `h>=2` 已严格排除；
   - `h=1` 恰保留 `D=+-16651` 两个 normalized transverse templates；
3. source prefix `e` 始终是唯一 simple lift；
4. source base primary `p^{2h}` 对 angle parity仍为偶深。

因此下一步不应再做 projected singular-discriminant hunting。最具体的新任务是：对 `p=1746991,h=1,D=+-16651,phi=987987` 做下一层 full endpoint/common compatibility，或回到 generic simple `(H,M)` orbit的 natural representative。

---

<a id="source-spontaneous-source-common-parity"></a>

> 整合来源：`spontaneous-source-common-parity.md`

# A2 source→common natural gate 的 primitive `3 mod 8` orientation

> **依赖：** `spontaneous-source-common-integer.md`、`spontaneous-source-prefix-simple.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文对 source→common natural integer `K_src(H,E,F)` 做精确 `2`-进本原化。利用真实 denominator defect并非任意，而满足 `b_2=E(F+H)=2^{M+m+1}c_ug`，证明 `v_2(K_src)=8`，且正奇 quotient `K_src/2^8` 恒为 `3 mod 8`。因此 source→common gate 自身也是一个全局 odd-inert parity carrier。本文不声称 `K_src` 的每个 inert divisor都是真正 source prime，也不据此关闭 A2。

---

## 1. natural integer gate

沿用

\[
F:=5^{M-1},
\qquad
E:=2^{M-1},
\qquad
M\ge11.
\]

真实 denominator defect为

\[
b_2=E(F+H).
\tag{1.1}
\]

`spontaneous-source-common-integer.md` 定义

\[
\boxed{
\begin{aligned}
\mathcal K_{\rm src}
={}&4400F^2(H+21F)^2\\
&+81EF\,\mathcal P_4(H,F)\\
&-810E^2(H+F)(99H+59F)\\
&\qquad\cdot(H^2+2HF+5F^2)(49H^2+58HF-191F^2),
\end{aligned}}
\tag{1.2}
\]

其中

\[
\boxed{
\mathcal P_4
=9401H^4+13684H^3F-175354H^2F^2
-418156HF^3-878519F^4.}
\tag{1.3}
\]

并有 positive scaling identity

\[
\boxed{
\mathcal K_{\rm src}
=10E^2F^6\,(10000\mathcal C_{\rm src}).}
\tag{1.4}
\]

真实 endpoint 已证明

\[
\mathcal C_{\rm src}>448,
\]
所以

\[
\boxed{\mathcal K_{\rm src}>0.}
\tag{1.5}
\]

---

## 2. `已严格完成`：真实 denominator normal form强迫 `v_2(H+F)>=3`

deep-even normal form同时给

\[
\boxed{
b_2=2^{M+m+1}c_ug.}
\tag{2.1}
\]

与 (1.1) 比较，并用 `E=2^{M-1}`：

\[
\boxed{
H+F=2^{m+2}c_ug.}
\tag{2.2}
\]

当前 third block至少有一位，故 `m>=1`。因此

\[
\boxed{8\mid H+F.}
\tag{2.3}
\]

`F` 为奇数，于是 `H` 也为奇数。

进一步：

\[
H+21F=(H+F)+20F.
\]
第一项被 `8` 整除，第二项满足 `v_2(20F)=2`，所以

\[
\boxed{v_2(H+21F)=2.}
\tag{2.4}
\]

写

\[
\boxed{H+21F=4L,\qquad L\text{ odd}.}
\tag{2.5}
\]

---

## 3. 第一项精确停在 `2^8`

由 (2.5)：

\[
4400F^2(H+21F)^2
=4400\cdot16F^2L^2
=2^8\cdot275F^2L^2.
\tag{3.1}
\]

因此第一项满足

\[
\boxed{v_2=8,}
\tag{3.2}
\]

且因为 odd square模 `8` 恒为 `1`：

\[
\boxed{
\frac{4400F^2(H+21F)^2}{2^8}
\equiv275\equiv3\pmod8.}
\tag{3.3}
\]

---

## 4. 第二、第三项在除 `2^8` 后都消失模 `8`

先看 `P_4`。因为 `H,F` 都奇，模 `2` 只有两个 odd coefficient项留下：

\[
\mathcal P_4
\equiv H^4-F^4
\equiv1-1
\equiv0\pmod2.
\tag{4.1}
\]

所以

\[
v_2(81EF\mathcal P_4)
\ge(M-1)+1
=M
\ge11.
\tag{4.2}
\]

从而

\[
\boxed{
2^{-8}(81EF\mathcal P_4)
\equiv0\pmod8.}
\tag{4.3}
\]

第三项的 coefficient `810` 具有 `v_2=1`，所以无论后面 product 的额外 parity如何：

\[
v_2(810E^2\cdot\text{product})
\ge1+2(M-1)
\ge21.
\tag{4.4}
\]

故

\[
\boxed{
2^{-8}(810E^2\cdot\text{product})
\equiv0\pmod8.}
\tag{4.5}
\]

---

## 5. `已严格完成`：primitive source-common gate 恒为 `3 mod 8`

综合 §§3–4：

\[
\boxed{v_2(\mathcal K_{\rm src})=8.}
\tag{5.1}
\]

定义

\[
\boxed{
\widehat{\mathcal K}_{\rm src}
:=\frac{\mathcal K_{\rm src}}{2^8}.}
\tag{5.2}
\]

则由 (1.5)、(3.3)、(4.3)、(4.5)：

\[
\boxed{
\widehat{\mathcal K}_{\rm src}>0,
\qquad
\widehat{\mathcal K}_{\rm src}\equiv3\pmod8.}
\tag{5.3}
\]

因此

\[
\boxed{
\sum_{p\equiv3\ (4)}
v_p(\widehat{\mathcal K}_{\rm src})
\equiv1\pmod2.}
\tag{5.4}
\]

也就是说 source→common natural gate自身强迫一份 odd inert parity。

---

## 6. 与已有两个 parity carriers 的关系

目前 dangerous endpoint中已经有

\[
\widehat{\mathcal O}_{\rm sp}>0,
\qquad
\widehat{\mathcal O}_{\rm sp}\equiv3\pmod4,
\]

\[
\widehat{\mathcal T}_2>0,
\qquad
\widehat{\mathcal T}_2\equiv3\pmod4.
\]

本文新增第三个 primitive integer：

\[
\boxed{
\widehat{\mathcal K}_{\rm src}>0,
\qquad
\widehat{\mathcal K}_{\rm src}\equiv3\pmod8.}
\tag{6.1}
\]

但必须保留逻辑边界：`K_src` 是 source slice 的 **gate integer**。一个任意 prime整除 `K_src` 并不自动意味着它同时整除 source integer `sigma` / `D_src`。只有再加入 source Hensel condition后，该 prime才成为真正 source→common carrier。

因此 (6.1) 不能单独推出 `G_sp` 的 parity；它提供的是新的全局自然整数，供后续研究

\[
\gcd(\widehat K_{\rm src},D_{\rm src}),
\qquad
\gcd(\widehat K_{\rm src},\sigma),
\]
或 source half-depth saturation时使用。

---

## 7. 更新后的 source frontier

结合 `spontaneous-source-depth-transfer.md`：

- `C_src` 精确读取 source common 的低于 `h` 的 additive depth；
- `K_src` 是 `C_src` 的真实整数 representative；
- `K_src/2^8` 自身为 positive `3 mod 8`；
- source base primary `p^{2h}` 仍为 even parity；
- 真正困难因此进一步集中为：`K_src` 的 odd inert parity 中，多少能与 source primary同步，以及 half-depth saturation后的 normalized blow-up。

这比继续做 source singular/discriminant hunting更接近 `G_sp` 的全局 parity，但尚未形成 closure。

---

<a id="source-spontaneous-source-conjugate-bridge"></a>

> 整合来源：`spontaneous-source-conjugate-bridge.md`

# A2 source actual/conjugate gate 与 numerator residual 的 exact bridge

> **依赖：** `spontaneous-source-common-parity.md`、`spontaneous-source-numerator-length.md`、`spontaneous-source-sheet-collision.md`、`spontaneous-source-prefix-simple.md`。
>
> **严格状态：**本文把 source actual gate `K_src(H,E,F)`、共轭 square-sheet gate `K_src(-H-2F,E,F)` 与 pure numerator/length residual `R_src(e,M)` 放进同一个 integer congruence modulo source prefix linear form。对 source half-depth `p^h|D_src`，得到截断赋值律 `v(R_src)=v(K)+v(K^vee)`（截断到 `h`）。因此不发生 sheet collision时，`R_src` 与真实 `K_src/C_src` 读取完全相同的 half-depth；额外 valuation只能来自已经被固定 quartic控制的 conjugate-sheet collision。本文不排除 simple collision roots，也不宣称 A2 closure。

---

## 1. actual 与 conjugate denominator defects

沿用

\[
F=5^{M-1},
\qquad
E=2^{M-1},
\qquad
S=EF=10^{M-1},
\]

\[
x=\frac{H+F}{10F}.
\tag{1.1}
\]

定义 actual source-common natural gate

\[
\boxed{K:=\mathcal K_{\rm src}(H,E,F).}
\tag{1.2}
\]

source square relation的共轭 sheet是 `x -> -x`。保持 `E,F` 不变时，唯一对应的 defect substitution为

\[
\frac{H^\vee+F}{10F}
=-\frac{H+F}{10F},
\]
即

\[
\boxed{H^\vee=-H-2F.}
\tag{1.3}
\]

因此定义

\[
\boxed{
K^\vee
:=\mathcal K_{\rm src}(-H-2F,E,F).}
\tag{1.4}
\]

由 `K_src` 的 scaling identity：

\[
\boxed{
K=100000E^2F^6\mathcal C_{\rm src}(x,\tau),}
\tag{1.5}
\]

\[
\boxed{
K^\vee=100000E^2F^6\mathcal C_{\rm src}(-x,\tau),}
\tag{1.6}
\]

其中

\[
\tau=(10EF)^{-1}.
\]

---

## 2. source prefix equation 的 primitive linear form

`spontaneous-source-prefix-simple.md` 已有

\[
D_{\rm src}
=\frac{9E^2}{4}(5F^2+18FH+9H^2)+9EF e.
\]

提出固定 `9E/4`，定义 primitive linear form

\[
\boxed{
D_{\rm lin}
:=E(5F^2+18FH+9H^2)+4Fe.}
\tag{2.1}
\]

则

\[
\boxed{
D_{\rm src}=\frac{9E}{4}D_{\rm lin}.}
\tag{2.2}
\]

对 genuine non-`3` source prime，`9E/4` 是 unit，因此

\[
\boxed{v_p(D_{\rm lin})=v_p(D_{\rm src}).}
\tag{2.3}
\]

---

## 3. normalized product identity

`spontaneous-source-sheet-collision.md` 已证明在 quotient ring

\[
225x^2-y=0
\]
中：

\[
\boxed{
\mathcal R_{\rm src}^{(y)}
=5625^2\mathcal C_{\rm src}(x,\tau)
\mathcal C_{\rm src}(-x,\tau).}
\tag{3.1}
\]

而 source prefix relation正是

\[
225x^2-y
=\frac{D_{\rm src}}{9S^2}
=\frac{D_{\rm lin}}{4FS}.
\tag{3.2}
\]

同时 pure numerator integer residual满足

\[
\boxed{
\mathcal R_{\rm src}^{(y)}
=\frac{\mathscr R_{\rm src}}{100S^6}.}
\tag{3.3}
\]

所以乘回所有 `2,3,5,E,F` scales后，(3.1) 在整数多项式环中产生一个 modulo `D_lin` 的 exact product bridge。

---

## 4. `已严格完成`：integer congruence

把 (1.5)–(1.6)、(3.3) 代入 (3.1)；使用

\[
\frac{10^8}{5625^2}=\frac{256}{81},
\]
得到 source slice上的 equality

\[
81E^2KK^\vee=256F^6\mathscr R_{\rm src}.
\]

由于 source slice由 linear equation `D_lin=0` 定义，这等价于 polynomial congruence

\[
\boxed{
81E^2KK^\vee
\equiv
256F^6\mathscr R_{\rm src}
\pmod{D_{\rm lin}}.}
\tag{4.1}
\]

也就是说存在

\[
\mathcal L_{\rm conj}\in\mathbf Z[H,e,E,F]
\]
使

\[
81E^2KK^\vee
-256F^6\mathscr R_{\rm src}
=D_{\rm lin}\mathcal L_{\rm conj}.
\tag{4.2}
\]

`check_a2_spontaneous_source_conjugate_bridge.py` 对完整 expanded integers直接做 exact polynomial division验证 (4.2)，无需记录 90-term quotient本身。

---

## 5. source half-depth 下的截断 valuation law

固定 genuine source prime，且

\[
p^h\mid D_{\rm src}.
\]

由 (2.3)：

\[
p^h\mid D_{\rm lin}.
\]

又

\[
p\nmid2\cdot3\cdot5EF,
\]
所以 (4.1) 模 `p^h` 是两个 unit multiples 的 congruence：

\[
KK^\vee
\equiv u\,\mathscr R_{\rm src}
\pmod{p^h},
\qquad u\in\mathbf Z_p^\times.
\tag{5.1}
\]

因此逐 prime-power精确有

\[
\boxed{
\min\{v_p(\mathscr R_{\rm src}),h\}
=
\min\{v_p(K)+v_p(K^\vee),h\}.}
\tag{5.2}
\]

这不是只在 first layer成立，而是 source prefix half-depth内的完整 truncated law。

---

## 6. generic 单-sheet时 `R_src` 与 actual common gate完全同步

若共轭 gate为 unit：

\[
p\nmid K^\vee,
\tag{6.1}
\]
则 (5.2) 立即简化为

\[
\boxed{
\min\{v_p(\mathscr R_{\rm src}),h\}
=
\min\{v_p(K),h\}.}
\tag{6.2}
\]

对 genuine odd source prime，`K` 与 `C_src`只差 `2,5,E,F` units，因此

\[
\boxed{
\min\{v_p(\mathscr R_{\rm src}),h\}
=
\min\{v_p(\mathcal C_{\rm src}),h\}.}
\tag{6.3}
\]

再与 `spontaneous-source-depth-transfer.md` 合并：

\[
\boxed{
\min\{v_p(\mathscr R_{\rm src}),h\}
=
\min\{v_p(\widehat{\mathcal T}_2),h\}
=
\min\{v_p(G_{\rm sp}),h\}}
\tag{6.4}
\]

在 generic noncollision source primary上成立。

所以 pure numerator/length residual不再只是一个 necessary resultant：它精确读取真实 common depth，直到 source half-depth。

---

## 7. 唯一 correction：conjugate sheet collision

若

\[
p\mid K^\vee
\]
且 actual gate也命中，则两个 source square sheets同时 contact。`spontaneous-source-sheet-collision.md` 已证明这等价于

\[
\mathcal E=\mathcal O=0
\]
并被固定 quartic

\[
\mathcal Q_{\rm sheet}(y)=0
\]
控制。

而该 collision locus：

- 真实 endpoint interval无 Archimedean root；
- genuine non-`3` inert singular Hensel tree为空；
- 剩余只能是 simple fixed-quartic synchronization。

因此 (5.2) 中 `v_p(K^vee)` 是**唯一**可能使 `R_src` 比 actual `C_src` 多收 depth 的 correction；它不携带新的 source ratio或奇异分叉。

---

## 8. 与两个 mod-8 orientations 的关系

已有

\[
\widehat K_{\rm src}=K/2^8\equiv3\pmod8,
\]
而

\[
\mathscr R_{\rm src}\equiv1\pmod8.
\]

(4.1) 解释了两者为何并不矛盾：`R_src` 是 actual gate和共轭 gate的 source-sheet norm，而不是 actual gate本身。

形式上，在 source slice上：

\[
\boxed{
\text{numerator/length norm}
\sim
\text{actual gate}\times\text{conjugate gate}.}
\tag{8.1}
\]

所以 `1 mod 8` orientation正是两张 sheet parity合并后的结果。若要从全局 parity进一步逼 actual source common prime，必须控制 conjugate sheet 的 inert allocation；本文已经把这一 correction压到固定 simple quartic，避免把整个 `R_src` 错误地直接等同于 `K_src`。

---

## 9. 更新后的 source common ledger

source pool现在可以用四个对象完整记账：

\[
\boxed{
\begin{array}{c|c}
\mathcal S_{\rm src}&\text{source primary depth }2h\\
D_{\rm lin}&\text{source prefix half-depth }h\\
K&\text{actual source→common gate}\\
K^\vee&\text{conjugate-sheet correction}\\
\mathscr R_{\rm src}&\text{actual×conjugate numerator norm}
\end{array}}
\]

并有三条 exact depth bridge：

\[
81\mathcal O_{\rm sp}=400TD_{\rm src}^2-81A^2\mathcal S_{\rm src},
\]

\[
\min(v_p(\widehat T_2),h)=\min(v_p(K),h),
\]

\[
\min(v_p(\mathscr R_{\rm src}),h)=\min(v_p(K)+v_p(K^\vee),h).
\]

这已经把 source local algebra基本封装完成。真正开放项只剩 simple actual/conjugate decimal orbit和 global inert parity allocation。

---

<a id="source-spontaneous-source-depth-transfer"></a>

> 整合来源：`spontaneous-source-depth-transfer.md`

# A2 source→common 的 half-depth transfer

> **依赖：** `spontaneous-source-common-gate.md`、`spontaneous-source-prefix-simple.md`、`spontaneous-source-saturation-parity.md`、`spontaneous-angle.md`。
>
> **严格状态：**本文解释 `C_src(x,tau)` 的局部几何含义，并把 source half-depth 与 additive cofactor depth 对齐。对 genuine non-`3` inert source prime `p^{2h} || sigma`，source Hensel 给 `v_p(d)>=h`、`v_p(Phi_s)=2h`。本文证明真实 sphere third-numerator root在模 `p^h` 内必贴住 source slice 的 double root，而 `Theta_dec=0` 的 affine root与该 double root之差恰为 `C_src` 乘一个单位。因此在 generic noncentral channel有截断赋值律
>
> `min(v_p(widehat(T)_2),h)=min(v_p(C_src),h)`。
>
> 这给出 source 版的 depth matrix；它不证明 `C_src` 的 simple decimal lifts不存在，也不宣称 A2 全局关闭。

---

## 1. source slice 的 double-sphere root

沿用

\[
d:=225x^2-y,
\qquad
\Phi_s=(99x-4)r_s-2x-4.
\]

source first layer为

\[
y_0:=225x^2,
\qquad
r_0:=\frac{2(x+2)}{99x-4}.
\tag{1.1}
\]

用

\[
\bar w:=\frac{b_3}{T10^M},
\qquad r_s=\frac{x}{\bar w},
\]
可得 source slice 的 third-denominator phase

\[
\boxed{
\bar w_0
=\frac{x(99x-4)}{2(x+2)}.}
\tag{1.2}
\]

exact sphere写成

\[
\mathscr S(x,y,\bar w,\bar\zeta)
:=x^2\bar w^2(9+y+\bar\zeta)^2
-(x+2+\bar w)^2
\left(
\frac{2025x^2+y^2}{100}\bar w^2+x^2\bar\zeta^2
\right).
\tag{1.3}
\]

把 `(y,w)=(y_0,w_0)` 代入，直接因式分解：

\[
\boxed{
\mathscr S(x,y_0,\bar w_0,\bar\zeta)
=-\frac{x^2(25x^2+1)}{64(x+2)^4}
\left[
16(x+2)^2\bar\zeta-x^2(297x-12)^2
\right]^2.}
\tag{1.4}
\]

因此 source slice 上 sphere 有唯一 double root

\[
\boxed{
\bar\zeta_s
=\frac{x^2(297x-12)^2}{16(x+2)^2}.}
\tag{1.5}
\]

对 genuine source prime，`x(x+2)(25x^2+1)` 都是单位，所以 (1.4) 的 quadratic coefficient也是单位。事实上

\[
\boxed{
[\bar\zeta^2]\,\mathscr S(x,y_0,\bar w_0,\bar\zeta)
=-4x^2(25x^2+1).}
\tag{1.6}
\]

---

## 2. `已严格完成`：`C_src` 就是 additive root 到 double center 的距离

在 noncentral channel，`Theta_dec=0` 给

\[
\bar\zeta_\Theta(x,y,\tau)
=
\frac{
 x^2((9+y)^2-18(9+y)\tau+55\tau^2)
 -\frac1{100}(x+2)^2(2025x^2+y^2)
}
{2x^2(2(9+y)-9\tau)}.
\tag{2.1}
\]

把 `y=y_0=225x^2` 代入，和 (1.5) 相减。exact factorization为

\[
\boxed{
\bar\zeta_\Theta(x,y_0,\tau)-\bar\zeta_s
=
\frac{\mathcal C_{\rm src}(x,\tau)}
{144(x+2)^2(50x^2+2-\tau)}.}
\tag{2.2}
\]

这里 `C_src` 正是 `spontaneous-source-common-gate.md` 的

\[
\begin{aligned}
\mathcal C_{\rm src}(x,\tau)
={}&440(x+2)^2\tau^2\\
&+81(9401x^4-2392x^3-1600x^2-64x-64)\tau\\
&-324x(99x-4)(25x^2+1)(49x^2-4x-2).
\end{aligned}
\tag{2.3}
\]

因此 `C_src` 不是一个黑箱 resultant：它精确测量 additive affine root 与 source double-sphere center 的距离。

在本文 generic channel中

\[
p\nmid144(x+2)^2(50x^2+2-\tau),
\tag{2.4}
\]
所以

\[
\boxed{
v_p(\bar\zeta_\Theta(x,y_0,\tau)-\bar\zeta_s)
=v_p(\mathcal C_{\rm src}).}
\tag{2.5}
\]

---

## 3. source half-depth 把真实 third denominator贴到 slice达 `2h`

固定 genuine source excess prime

\[
p^{2h}\Vert\sigma,
\qquad h\ge1.
\]

旧 source Hensel 给

\[
\boxed{v_p(\Phi_s)=2h,}
\tag{3.1}
\]
以及

\[
\boxed{v_p(d)\ge h.}
\tag{3.2}
\]

令 `A=99x-4`。由

\[
\Phi_s=A(r_s-r_0)
\]
且 `A` 为单位，

\[
\boxed{v_p(r_s-r_0)=2h.}
\tag{3.3}
\]

又 `bar w=x/r_s` 且 `x,r_s,r_0` 都为单位，所以

\[
\boxed{v_p(\bar w-\bar w_0)=2h.}
\tag{3.4}
\]

同时

\[
y-y_0=-d,
\qquad
\boxed{v_p(y-y_0)\ge h.}
\tag{3.5}
\]

---

## 4. `已严格完成`：真实 sphere root 必在 `p^h` 内贴住 double center

令真实 third-numerator phase写成

\[
\bar\zeta=\bar\zeta_s+Z.
\]

把 exact sphere视为关于 `Z` 的 quadratic：

\[
aZ^2+bZ+c=0.
\tag{4.1}
\]

在 source slice `(y_0,w_0,zeta_s)` 上：

\[
\mathscr S=0,
\qquad
\partial_{\bar\zeta}\mathscr S=0,
\tag{4.2}
\]

并且还有关键 tangency

\[
\boxed{
\left.\partial_y\mathscr S\right|_{(y_0,\bar w_0,\bar\zeta_s)}=0.}
\tag{4.3}
\]

而

\[
\left.\partial_{\bar w}\mathscr S\right|_{(y_0,\bar w_0,\bar\zeta_s)}
=-\frac{81x^4(99x-4)^2(101x^2+4x+8)^2}
{128(x+2)^3},
\tag{4.4}
\]
可非零，但 (3.4) 已给 `bar w-bar w_0` 深度 `2h`。

因此由 Taylor 展开和 (3.4)–(3.5)：

\[
\boxed{v_p(c)\ge2h,}
\tag{4.5}
\]

\[
\boxed{v_p(b)\ge h.}
\tag{4.6}
\]

而由 (1.6)，quadratic coefficient `a` 仍为单位。

若反设 `v_p(Z)<h`，则三项深度分别满足

\[
2v_p(Z)
< h+v_p(Z),
\qquad
2v_p(Z)<2h,
\]
所以单位首项 `aZ^2` 具有唯一最小 valuation，不可能与其余两项相消。矛盾。

故

\[
\boxed{
v_p(\bar\zeta-\bar\zeta_s)\ge h.}
\tag{4.7}
\]

这个结论不需要 source roots在 `p^h` 层已经分开；即使额外 branch-collision 使分裂更深，也仍成立。

---

## 5. additive affine root 对真实 `y` 的移动也只有 `p^h`

由 (2.1) 直接相减可因式分解：

\[
\boxed{
\bar\zeta_\Theta(x,y,\tau)
-\bar\zeta_\Theta(x,y_0,\tau)
=(225x^2-y)\,\mathcal U_\Theta(x,y,\tau),}
\tag{5.1}
\]

其中 `U_Theta` 的 denominator在 generic source channel中为单位。因此 (3.2) 给

\[
\boxed{
v_p(
\bar\zeta_\Theta(x,y,\tau)
-\bar\zeta_\Theta(x,y_0,\tau))\ge h.}
\tag{5.2}
\]

结合 (2.2)、(4.7)：

\[
\bar\zeta_\Theta(x,y,\tau)-\bar\zeta
=
\frac{\mathcal C_{\rm src}}
{144(x+2)^2(50x^2+2-\tau)}
+O(p^h).
\tag{5.3}
\]

因此

\[
\boxed{
\min\left\{
v_p(\bar\zeta_\Theta-\bar\zeta),h
\right\}
=
\min\left\{
v_p(\mathcal C_{\rm src}),h
\right\}.}
\tag{5.4}
\]

---

## 6. `已严格完成`：source half-depth matrix

由

\[
\Theta_{\rm dec}
=T\mathcal R_\Theta-2B^2(2K-9)a_3
\]
和 `a_3=TN bar zeta`，得到 exact affine factorization

\[
\boxed{
\Theta_{\rm dec}
=2B^2(2K-9)TN
(\bar\zeta_\Theta-\bar\zeta).}
\tag{6.1}
\]

在 genuine noncentral source prime上，前面的 coefficient为 `p`-进单位；`widehat(T)_2` 与 `Theta_dec` 又只差固定 `2`-power。因此 (5.4) 给

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),h\}
=
\min\{v_p(\mathcal C_{\rm src}),h\}.}
\tag{6.2}

另一方面 `spontaneous-source-saturation-parity.md` 已有

\[
\boxed{v_p(\widehat{\mathcal O}_{\rm sp})\ge2h.}
\tag{6.3}

故对 common gcd

\[
G_{\rm sp}=\gcd(
\widehat{\mathcal O}_{\rm sp},
\widehat{\mathcal T}_2),
\]
也有

\[
\boxed{
\min\{v_p(G_{\rm sp}),h\}
=
\min\{v_p(\mathcal C_{\rm src}),h\}.}
\tag{6.4}

这就是 source pool 对 `G_sp` 的规范 half-depth matrix。

---

## 7. 新的 source common dichotomy

令

\[
c_p:=v_p(\mathcal C_{\rm src}).
\]

由 (6.2)：

### unsaturated source-common

若

\[
c_p<h,
\]
则

\[
\boxed{
v_p(\widehat{\mathcal T}_2)=v_p(G_{\rm sp})=c_p.}
\tag{7.1}
\]

因此 source common 的低于 half-depth 部分完全由 pure-prefix/decimal gate `C_src` 读取。

### half-depth saturation

若

\[
c_p\ge h,
\]
则

\[
\boxed{p^h\mid\widehat{\mathcal T}_2,}
\qquad
\boxed{p^h\mid G_{\rm sp}.}
\tag{7.2}

从这一层开始，source transverse split 与 additive root位于同一尺度；后续必须使用 normalized blow-up，而不能继续把 `C_src` 当作独立的一变量 root。

因此 source common 的开放机制已经被精确压成

\[
\boxed{
\text{simple unsaturated `C_src` depth}
\quad\text{or}\quad
\text{half-depth saturated blow-up}.}
\tag{7.3}

`spontaneous-source-singular-decimal-orbit.md` 已经关闭 projected singular sector，所以 generic `C_src` roots本身都是 simple；本文新增的是它们与真实 source half-depth / additive cofactor的精确 valuation transfer。

---

<a id="source-spontaneous-source-equal-depth-nogo"></a>

> 整合来源：`spontaneous-source-equal-depth-nogo.md`

# A2 source equal-depth angle gate 的二阶 Hensel no-go

> **依赖：** `spontaneous-source-equal-depth.md`、`hensel.md`、`spontaneous-angle.md`。
>
> **严格状态：**`spontaneous-source-equal-depth.md` 已把 source residual odd parity 压到 `v_p(d)=h` 的 normalized cancellation。本文进一步在该 source first-layer curve 上做精确二阶展开，证明 angle extra-lift 并不强迫 `x` 落入 fixed/singular locus；它只是唯一选择 source linear root `r_s` 的二阶 Hensel correction。因而继续仅在 source 局部系统内做 resultant、discriminant 或 singular-prime hunting不会关闭该 shell。要排除它必须引入 source 之外的 global allocation、natural representative 或与 additive common carrier 的独立同步。本文是严格 no-go，不宣称 A2 全局关闭。

---

## 1. source first-layer curve

固定 genuine non-`3` inert source excess prime

\[
p\equiv3\pmod4,
\qquad p\ne3,5.
\]

沿用

\[
d:=225x^2-y,
\]

\[
\Phi_s=(99x-4)r_s-2x-4,
\]

\[
\Psi_9=3600(r_s+1)^2-y(99r_s-2)^2,
\]

\[
\Omega_{\rm sp}=4r_sd^2-xy^2\Phi_s.
\]

source first layer `d=Phi_s=0` 给

\[
\boxed{y_0=225x^2,}
\tag{1.1}
\]

以及令

\[
A:=99x-4,
\]
则

\[
\boxed{r_0=\frac{2(x+2)}A.}
\tag{1.2}
\]

旧 genuine source separation 已证明

\[
p\nmid x(x+2)A,
\tag{1.3}
\]
并且 `p != 3,5`，所以本文出现的 `225,404,50625` 也都是单位。

在 (1.1)–(1.2) 上还有两个 exact elementary values：

\[
\boxed{
r_0+1=\frac{101x}{A},}
\tag{1.4}
\]

\[
\boxed{99r_0-2=\frac{404}{A}.}
\tag{1.5}

这正是旧 source resultant collapse 的 first-layer 几何。

---

## 2. 等深 shell 的规范二阶参数

设 source excess

\[
p^{2h}\Vert\sigma,
\qquad h\ge1,
\]
并处于 angle odd-depth 唯一可能的 threshold

\[
v_p(d)=h,
\qquad
v_p(\Phi_s)=2h.
\]

在局部 DVR 中取

\[
\varepsilon:=p^h.
\]

定义单位

\[
d_1:=d/\varepsilon,
\qquad
\phi_2:=\Phi_s/\varepsilon^2.
\]

于是可以**精确**写成

\[
\boxed{y=y_0-\varepsilon d_1,}
\tag{2.1}
\]

\[
\boxed{
r_s=\frac{2(x+2)+\varepsilon^2\phi_2}{A}
=r_0+\frac{\varepsilon^2\phi_2}{A}.}
\tag{2.2}

这里没有把 `x` 固定成 Teichmuller lift；`x` 可仍是任意满足 genuine unit 条件的 p-adic prefix variable。本文只把相对于当前 `x` 的 transverse source corrections显式化。

---

## 3. `已严格完成`：第二 Hensel 方程一阶只读取 `d_1`

把 (2.1)–(2.2) 代入 `Psi_9`。由于 `r_s-r_0` 从 `epsilon^2` 才开始，模 `epsilon^2` 时 `r_s` 可直接换成 `r_0`：

\[
\begin{aligned}
\Psi_9
&=3600(r_s+1)^2-y(99r_s-2)^2\\
&\equiv
3600(r_0+1)^2
-(y_0-\varepsilon d_1)(99r_0-2)^2
\pmod{\varepsilon^2}.
\end{aligned}
\]

first-layer constant term为零；使用 (1.5)：

\[
\boxed{
\Psi_9
\equiv
\varepsilon d_1\frac{404^2}{A^2}
\pmod{\varepsilon^2}.}
\tag{3.1}

因此

\[
\boxed{
\frac{\Psi_9}{\varepsilon}
\equiv
\frac{404^2}{A^2}d_1
\pmod p.}
\tag{3.2}

这重新、并以局部展开方式解释了 `spontaneous-source-equal-depth.md` 的

\[
v_p(\Psi_9)=h.
\]

更重要的是：第二 Hensel equation 在这一层只固定 `d_1` 的线性单位类；它**尚未**约束二阶参数 `phi_2`。

---

## 4. `已严格完成`：angle extra lift恰好线性解出 `phi_2`

由定义直接有

\[
\Omega_{\rm sp}
=4r_s\varepsilon^2d_1^2
-x(y_0-\varepsilon d_1)^2\varepsilon^2\phi_2.
\]

除以 `epsilon^2` 再模 `p`：

\[
\boxed{
\frac{\Omega_{\rm sp}}{\varepsilon^2}
\equiv
4r_0d_1^2-xy_0^2\phi_2
\pmod p.}
\tag{4.1}

使用

\[
r_0=\frac{2(x+2)}A,
\qquad
y_0=225x^2,
\]
得到

\[
\boxed{
\frac{\Omega_{\rm sp}}{\varepsilon^2}
\equiv
\frac{8(x+2)}A d_1^2
-50625x^5\phi_2
\pmod p.}
\tag{4.2}

因此 angle valuation 想从 baseline `2h` 再提升至少一层，等价于

\[
\boxed{
\phi_2
\equiv
\frac{8(x+2)}{50625Ax^5}d_1^2
\pmod p.}
\tag{4.3}

由 (1.3) 及 `p != 3,5`，右边所有分母都是单位。于是：

\[
\boxed{
\text{对每个 genuine first-layer }x
\text{ 和每个单位 }d_1,
\text{恰有一个 }\phi_2\pmod p
\text{使 angle extra lift发生。}}
\tag{4.4}

这不是 singularity；它是普通的一次 Hensel correction。

---

## 5. source unit `sigma^sharp` 同样只是被唯一选定

旧 exact source identity为

\[
4\sigma=5^Mc_Q\Phi_s.
\]

在当前 shell 除以 `epsilon^2`：

\[
\boxed{
4\sigma^\sharp=5^Mc_Q\phi_2,
\qquad
\sigma^\sharp:=\sigma/p^{2h}.}
\tag{5.1}

因此一旦 (4.3) 选择了 `phi_2`，normalized source unit也被唯一固定：

\[
\boxed{
\sigma^\sharp
\equiv
\frac{5^Mc_Q}{4}
\frac{8(x+2)}{50625Ax^5}d_1^2
\pmod p.}
\tag{5.2}

所以 `spontaneous-source-equal-depth.md` 中看起来尚有自由的 `sigma^sharp` 并不是另一个独立 branch parameter；在 angle extra-lift locus 上它只是二阶 correction 的线性像。

同理 (3.2) 给

\[
\Psi_9^\sharp
\equiv\frac{404^2}{A^2}d_1.
\]
于是该文件的二单位 congruence本质上就是 (4.3) 的坐标变换，而不是额外的独立 quadratic obstruction。

---

## 6. `审计 / no-go`：source 局部 resultant不会产生 fixed bad-prime set

关键点是 (4.3) 对 `phi_2` 的系数

\[
50625x^5
\]
在所有 genuine source primes 上为单位。因此 angle extra-lift equation 对二阶 transverse correction的 Jacobian 永远非零：

\[
\boxed{
\frac{\partial}{\partial\phi_2}
\left(\Omega_{\rm sp}/\varepsilon^2\right)
\equiv-50625x^5\not\equiv0\pmod p.}
\tag{6.1}

所以该 shell 没有任何由 local Jacobian rank drop 产生的 singular bad prime。

换句话说：

\[
\boxed{
\text{source equal-depth angle cancellation}
\text{ 是 genuine simple second-order Hensel freedom，}
\text{不是 fixed/singular locus。}}
\tag{6.2}

因此以下路线必须降级：

- 对 `(Phi_s,Psi_9,Omega_sp)` 再做普通 first-layer resultant；
- 对 (4.3) 再做 discriminant / singular-prime hunting；
- 仅靠 `sigma^sharp,Psi_9^sharp` 的 Legendre symbol尝试制造第二个 obstruction。

这些都只是在重新描述同一个可解的一次二阶 correction。

---

## 7. 对 `G_sp mod 4` 闭环的真实含义

`spontaneous-angle-parity.md` 的 `G_sp=1 mod4` 分支要求 angle residual quotient自身携带 odd inert parity。`spontaneous-angle-overlap-depth.md` 已将 source supplier 压到当前 equal-depth shell；本文证明该 shell**不能靠 source 局部几何自身排除**。

因此若最终要从 parity dichotomy 删除 source residual supplier，必须加入 source 系统之外的独立信息，例如：

1. `D_src/L_0` 的 natural integer representative 与 `p^h` 高度；
2. source correction 与 decimal exponent/prefix defect `(H,e,M)` 的同步；
3. 与 additive common carrier `Theta_dec` / `G_sp` 的独立 prime-power depth；
4. global Gaussian factor allocation / height channel。

规范开放项不再是“求 source equal-depth 的更多 resultant”，而是

\[
\boxed{
\text{把 simple second-order correction (4.3)
与一个 source 外部的全局约束联立。}}
\tag{7.1}

本文保留这一 no-go，避免后续重复局部代数。

---

<a id="source-spontaneous-source-equal-depth"></a>

> 整合来源：`spontaneous-source-equal-depth.md`

# A2 source equal-depth angle cancellation 的 normalized Hensel gate

> **依赖：** `hensel.md`、`spontaneous-angle.md`、`spontaneous-angle-overlap-depth.md`。
>
> **严格状态：**`spontaneous-angle-overlap-depth.md` 已证明 source excess 对 angle carrier 产生奇 valuation 只能发生在 `v_p(d)=h` 的等深 cancellation 层。本文进一步利用旧第二 Hensel Bézout identity，把这一层正规化：证明 `v_p(Psi_9)=h` 精确成立，并把 angle cancellation 改写成只含 normalized source units `sigma^sharp`、`Phi^sharp`、`Psi_9^sharp` 的显式 square-class / quadratic congruence。本文仍未排除该 normalized gate，也不宣称 A2 全局关闭。

---

## 1. 等深 source shell

固定 genuine non-`3` inert source excess prime

\[
p\equiv3\pmod4,
\qquad
p^{2h}\Vert\sigma,
\qquad h\ge1.
\]

reflection endpoint `a_1=9` 中记

\[
d:=225x^2-y,
\]

\[
\Phi_s=(99x-4)r_s-2x-4,
\]

\[
\Psi_9=3600(r_s+1)^2-y(99r_s-2)^2.
\]

旧 source Hensel 结果为

\[
v_p(\Phi_s)=2h,
\qquad
v_p(d)\ge h.
\]

本文只处理 angle odd-depth 唯一可能的 threshold：

\[
\boxed{v_p(d)=h.}
\tag{1.1}
\]

定义 normalized units

\[
d^\sharp:=d/p^h,
\qquad
\Phi^\sharp:=\Phi_s/p^{2h},
\qquad
\sigma^\sharp:=\sigma/p^{2h}.
\tag{1.2}
\]

它们都是 `p`-进单位。

---

## 2. `已严格完成`：第二 Hensel 深度在 threshold 上精确为 `h`

令

\[
A_s:=99x-4.
\]

`hensel.md` 的 exact Bézout identity 在 `a_1=9` 时为

\[
\boxed{
A_s^2\Psi_9-163216d
=\Phi_s\mathcal Q,
}
\tag{2.1}
\]

其中

\[
163216=404^2,
\]
而 genuine source prime 已有

\[
p\nmid A_s\cdot404.
\tag{2.2}
\]

在 (1.1) 下，第二项 `163216d` 恰有 valuation `h`，右边 `Phi_s Q` 至少有 valuation `2h`。因此两者 valuation 不同：

\[
\boxed{v_p(\Psi_9)=h.}
\tag{2.3}
\]

定义

\[
\Psi_9^\sharp:=\Psi_9/p^h.
\tag{2.4}
\]

把 (2.1) 除以 `p^h` 再模 `p`，右边消失，得到

\[
\boxed{
A_s^2\Psi_9^\sharp
\equiv404^2d^\sharp
\pmod p.}
\tag{2.5}
\]

因此

\[
\boxed{
\left(\frac{\Psi_9^\sharp}{p}\right)
=
\left(\frac{d^\sharp}{p}\right).
}
\tag{2.6}
\]

第二 Hensel unit 的 square class 已不再独立。

---

## 3. `已严格完成`：angle extra lift 的 normalized source equation

旧 second-angle exact integer 为

\[
\boxed{
E_1=5^\lambda L_0^2-2c_u\sigma a_2^2.
}
\tag{3.1}
\]

而 reflection source formula 给

\[
\boxed{
L_0=-5^M10^{M-1}d.
}
\tag{3.2}
\]

在 (1.1) 下：

\[
v_p(L_0)=h
\]
因为 `p!=2,5`。定义

\[
L_0^\sharp:=L_0/p^h
=-5^M10^{M-1}d^\sharp.
\tag{3.3}
\]

`Omega_sp` 与 `E_1` 只差 genuine `p`-进单位尺度，因此 angle valuation 超过 baseline `2h` 等价于

\[
E_1/p^{2h}\equiv0\pmod p.
\]
即

\[
\boxed{
5^\lambda(L_0^\sharp)^2
\equiv2c_u\sigma^\sharp a_2^2
\pmod p.}
\tag{3.4}
\]

这就是 source equal-depth cancellation 的规范形式。

---

## 4. 必要 quadratic character

(3.4) 两边的 `L_0^sharp`、`a_2` 都是单位，且其平方不影响 Legendre symbol。因此 extra angle lift 必须满足

\[
\boxed{
\left(\frac{2c_u\sigma^\sharp}{p}\right)
=
\left(\frac{5^\lambda}{p}\right).
}
\tag{4.1}
\]

等价地

\[
\boxed{
\left(\frac{2c_u\sigma^\sharp5^\lambda}{p}\right)=1.
}
\tag{4.2}
\]

所以 source odd residual parity 已被压成一个明确的 normalized quadratic gate，而不是任意 source root。

---

## 5. 用 `Phi^sharp` 改写同一个 gate

`hensel.md` 还有 exact source identity

\[
\boxed{4\sigma=5^Mc_Q\Phi_s.}
\tag{5.1}
\]

除去 `p^{2h}`：

\[
\boxed{
4\sigma^\sharp=5^Mc_Q\Phi^\sharp.
}
\tag{5.2}
\]

代入 (4.2)，并注意 `4` 是平方、`2^{-1}` 与 `2` 有相同 Legendre character：

\[
\boxed{
\left(
\frac{2c_uc_Q\Phi^\sharp5^{M+\lambda}}p
\right)=1.
}
\tag{5.3}
\]

这把 angle extra-lift gate 完全写成 source linear Hensel 的 normalized unit `Phi^sharp`。

---

## 6. `已严格完成`：消去 `d^sharp` 后的二单位 congruence

由 (2.5)：

\[
d^\sharp
\equiv\frac{A_s^2}{404^2}\Psi_9^\sharp
\pmod p.
\tag{6.1}
\]

由 (3.3)：

\[
L_0^\sharp
\equiv
-5^M10^{M-1}
\frac{A_s^2}{404^2}\Psi_9^\sharp
\pmod p.
\tag{6.2}
\]

代入 (3.4)，得到只含两个 normalized source units 的 congruence：

\[
\boxed{
2c_u\sigma^\sharp a_2^2\,404^4
\equiv
5^\lambda
\left(5^M10^{M-1}\right)^2
A_s^4(\Psi_9^\sharp)^2
\pmod p.}
\tag{6.3}
\]

因此危险 source shell 已从原来的

\[
(x,y,r_s)\text{ + 两个 Hensel 深度}
\]
压成

\[
\boxed{
(\sigma^\sharp,\Psi_9^\sharp)
\text{ 的一个 quadratic congruence}.}
\tag{6.4}
\]

所有其它因子都是已知 unit 或平方尺度。

---

## 7. 对 parity 闭环的意义

结合 `spontaneous-angle-overlap-depth.md`：

- 若 `v_p(d)>h`，source angle valuation 精确为 `2h`，必偶；
- 若 `v_p(d)=h` 但 (3.4) 不成立，valuation 仍精确为 `2h`；
- source pool 只有在 (1.1)+(3.4) 同时成立时才可能贡献 angle residual odd parity。

所以 source residual odd-inert supplier 已严格缩成

\[
\boxed{
\begin{gathered}
v_p(d)=h,\\
v_p(\Phi_s)=2h,\quad v_p(\Psi_9)=h,\\
5^\lambda(L_0^\sharp)^2
=2c_u\sigma^\sharp a_2^2\pmod p.
\end{gathered}}
\tag{7.1}

下一步不能再靠普通 resultant；必须独立固定 `sigma^sharp` 或 `Phi^sharp` 的 square class，或者把 (6.3) 与 source length orbit / natural representative 做 higher-depth synchronization。本文保留该 gate 为真实开放项。

---

<a id="source-spontaneous-source-halfdepth-blowup"></a>

> 整合来源：`spontaneous-source-halfdepth-blowup.md`

# A2 source odd-extra 在 half-depth saturation 后的 two-orientation blow-up

> **依赖：** `spontaneous-source-primary-bridge.md`、`spontaneous-source-depth-transfer.md`、`spontaneous-source-equal-depth-nogo.md`、`spontaneous-source-common-gate.md`。
>
> **严格状态：**source base primary `p^{2h}` 对 angle parity为偶；真正可能贡献 odd angle residual 的只有 equal-depth shell `v_p(d)=h` 加 normalized angle cancellation。本文把这个唯一危险 shell 与 source→additive-common 的 half-depth saturation `v_p(C_src)>=h` 联立，在 source double-sphere center做 blow-up。结论是：angle extra condition一旦成立，normalized sphere discriminant自动成为非零平方，产生两个严格不同的 simple orientations；超过 half-depth 的 additive lift分别落在两条互斥的 affine gate上，每条对 normalized `C_src` 都有 unit slope。因此 source odd-extra + common saturation不会产生新的 singular Hensel tree。simple affine decimal synchronization仍可能存在，故 A2 仍未全局关闭。

---

## 1. equal-depth source 坐标

固定 genuine non-`3` inert source prime

\[
p^{2h}\Vert\sigma,
\qquad h\ge1.
\]

真正可能产生 angle-over-source extra depth的唯一 shell为

\[
\boxed{v_p(d)=h,}
\qquad
 d:=225x^2-y,
\tag{1.1}
\]

同时

\[
\boxed{v_p(\Phi_s)=2h.}
\tag{1.2}
\]

令

\[
\boxed{d=p^hD,\qquad D\in\mathbf Z_p^\times,}
\tag{1.3}
\]

\[
\boxed{\Phi_s=p^{2h}\phi.}
\tag{1.4}
\]

写

\[
A_s:=99x-4,
\qquad
r_0:=\frac{2(x+2)}{A_s},
\]
则

\[
r_s=r_0+\frac{p^{2h}\phi}{A_s}.
\tag{1.5}
\]

source double-sphere center由 `spontaneous-source-depth-transfer.md` 给出：

\[
\boxed{
\bar\zeta_s
=\frac{x^2(297x-12)^2}{16(x+2)^2}.}
\tag{1.6}
\]

令真实 third-numerator phase写成

\[
\boxed{
\bar\zeta=\bar\zeta_s+p^h Z.}
\tag{1.7}
\]

---

## 2. `已严格完成`：sphere 的 normalized blow-up quadratic

把

\[
y=225x^2-p^hD,
\]

\[
r_s=r_0+p^{2h}\phi/A_s,
\qquad
\bar w=x/r_s,
\]
以及 (1.7) 代入 exact sphere。前 `p^0` 与 `p^h` coefficient均精确消失；除以 `p^{2h}` 再模 `p` 得

\[
\boxed{
\mathcal B_{\rm sph}(Z;D,\phi)
=a_ZZ^2+b_ZDZ+c_DD^2+c_\phi\phi=0,}
\tag{2.1}
\]

其中

\[
\boxed{a_Z=-4x^2(25x^2+1),}
\tag{2.2}
\]

\[
\boxed{
b_Z=-\frac{x^4(99x-4)^2}{2(x+2)^2},}
\tag{2.3}
\]

\[
\boxed{
 c_D=-\frac{x^2(99x-4)^2
(81x^2-36x+8)(121x^2+44x+8)}
{1600(x+2)^4},}
\tag{2.4}
\]

\[
\boxed{
 c_\phi=
\frac{81x^5(99x-4)^3(101x^2+4x+8)^2}
{512(x+2)^5}.}
\tag{2.5}
\]

所有 denominator在 genuine source channel中为 units。`a_Z` 是 source-slice sphere 的 unit quadratic coefficient。

---

## 3. sphere branch collision 的一般 discriminant

对 (2.1) 视为 `Z` 的 quadratic，直接因式分解：

\[
\boxed{
\begin{aligned}
\operatorname{Disc}_Z(\mathcal B_{\rm sph})
={}&
\frac{x^4(99x-4)^2(101x^2+4x+8)^2}
{800(x+2)^5}\\
&\cdot\left[
-8(x+2)D^2
+2025x^3(99x-4)(25x^2+1)\phi
\right].
\end{aligned}}
\tag{3.1}
\]

所以一般 source half-depth sphere collision对应最后方括号为零。本文真正关心的是它能否与 **odd angle-extra** 同时发生。

---

## 4. `已严格完成`：odd angle-extra 自动把 sphere discriminant变成非零平方

`spontaneous-source-primary-bridge.md` / `...equal-depth-nogo.md` 的 normalized angle extra condition在本文坐标中为

\[
\boxed{
\phi
=
\frac{8(x+2)}{50625(99x-4)x^5}D^2
\pmod p.}
\tag{4.1}
\]

把 (4.1) 代入 (3.1)，全部高次项塌掉：

\[
\boxed{
\operatorname{Disc}_Z
=
\frac{
D^2x^2(99x-4)^2(101x^2+4x+8)^2
}{2500(x+2)^4}.}
\tag{4.2}
\]

在 genuine pure source channel：

\[
p\nmid D\,x(x+2)(99x-4),
\]
且 source slice 上

\[
\boxed{
A_-ig|_{y=225x^2}
=-50625x^4(101x^2+4x+8).}
\tag{4.3}
\]

旧 `A_-=0` 已归入 common-`alpha` boundary，不属于 pure spontaneous/source channel。因此

\[
p\nmid101x^2+4x+8.
\tag{4.4}
\]

于是 (4.2) 是严格非零平方：

\[
\boxed{
\text{odd source angle-extra}
\Longrightarrow
\text{half-depth sphere 有两个不同 roots}.}
\tag{4.5}
\]

尤其 angle extra 与 sphere blow-up collision **不能同时发生**。

也可直接比较两种 `phi`：sphere collision要求

\[
\phi=\frac{8(x+2)}{2025x^3(99x-4)(25x^2+1)}D^2,
\]
而 angle extra要求 (4.1)。二者相等会强迫

\[
25x^2+1=25x^2,
\]
即 `1=0`，在任何 prime上都不可能。

---

## 5. `已严格完成`：两个 normalized sphere orientations 显式线性化

在 angle-extra condition (4.1) 下，(2.1) 的两个 roots精确为

\[
\boxed{Z_1=c_1D,\qquad Z_2=c_2D,}
\tag{5.1}
\]

其中

\[
\boxed{
 c_1=
-\frac{(99x-4)(99x^2-4x-8)}
{400x(x+2)^2},}
\tag{5.2}
\]

\[
\boxed{
 c_2=
-\frac{(99x-4)(2475x^4-100x^3+101x^2+4x+8)}
{400x(x+2)^2(25x^2+1)}.}
\tag{5.3}
\]

其差完全因子化：

\[
\boxed{
 c_2-c_1
=-\frac{(99x-4)(101x^2+4x+8)}
{200x(x+2)^2(25x^2+1)}.}
\tag{5.4}
\]

由 genuine units与 (4.4)：

\[
\boxed{c_2-c_1\in\mathbf Z_p^\times.}
\tag{5.5}
\]

所以两个 source-sphere orientations在 blow-up 后不是“同一个 root 的两种写法”，而是严格分离的两个 simple directions。

---

## 6. additive root在 half-depth 的 affine 坐标

source→common half-depth saturation定义为

\[
\boxed{v_p(\mathcal C_{\rm src})\ge h.}
\tag{6.1}
\]

令

\[
\boxed{C^\sharp:=\mathcal C_{\rm src}/p^h\pmod p.}
\tag{6.2}
\]

若实际 depth `>h`，则 `C^sharp=0`。

由 source-slice exact distance identity：

\[
\bar\zeta_\Theta(x,y_0,\tau)-\bar\zeta_s
=
\frac{\mathcal C_{\rm src}}
{144(x+2)^2(50x^2+2-\tau)},
\]
定义 unit

\[
\boxed{
 u_C:=\frac1{144(x+2)^2(50x^2+2-\tau)}.}
\tag{6.3}
\]

另一方面 `y=y_0-p^hD`。additive affine root对 `d=y_0-y` 的一阶 coefficient为

\[
\boxed{
 c_\Theta
=-\frac{
104\tau^2-8019\tau x^2+324\tau x
+200475x^4-8100x^3+8019x^2-324x
}
{324(50x^2+2-\tau)^2}.}
\tag{6.4}
\]

因此

\[
\boxed{
\frac{\bar\zeta_\Theta-\bar\zeta_s}{p^h}
\equiv
u_CC^\sharp+c_\Theta D
\pmod p.}
\tag{6.5}
\]

---

## 7. 超过 half-depth 的 additive/common lift只有两条 simple affine gate

在 angle-extra source branch上，真实 sphere orientation必须是 (5.1) 的其中之一。若 additive depth要从 baseline `h` 再提升至少一层，就必须使 normalized additive root与该 sphere root一致：

\[
\boxed{
\mathcal F_i(C^\sharp,D)
:=u_CC^\sharp+(c_\Theta-c_i)D
=0,
\qquad i=1,2.}
\tag{7.1}
\]

因为 `u_C` 为 unit：

\[
\boxed{
\frac{\partial\mathcal F_i}{\partial C^\sharp}=u_C\ne0.}
\tag{7.2}
\]

所以每条 orientation gate 对 normalized `C_src` 都是 simple linear Hensel equation。

而两条 gate的差为

\[
\boxed{
\mathcal F_1-\mathcal F_2
=(c_2-c_1)D.}
\tag{7.3}
\]

由 `D` unit及 (5.5)：

\[
\boxed{
\mathcal F_1=\mathcal F_2=0
\quad\text{不可能}.}
\tag{7.4}
\]

因此超过 source half-depth的 additive lift最多选择一个 sphere orientation；不存在 branch collision。

---

## 8. source odd residual + common saturation 的最终局部分类

对真正会影响 angle mod-4 parity 的 source residual，局部结构现在是：

1. source base primary：`2h`，严格偶深；
2. equal-depth angle-extra：由 (4.1) 唯一固定 normalized `phi`；
3. 若 `C_src` 未达 `h`，`spontaneous-source-depth-transfer.md` 已精确读取 common depth；
4. 若 `C_src` 达到 `h`，sphere blow-up自动分裂成两个不同 orientations；
5. additive/common 若继续超过 `h`，只能命中两条互斥且 unit-slope 的 affine gate (7.1)。

所以

\[
\boxed{
\text{source odd angle residual}
+\text{half-depth common saturation}
\text{ 不会产生新的 singular Hensel tree}.}
\tag{8.1}

剩余困难完全变成 simple branch 与真实 decimal/natural representative的同步，而不是 source local singularity。

这使 source pool与 denominator pool的最终形态高度一致：两者的 singular mechanisms都已剥掉，只剩 simple depth/orbit allocation。

---

<a id="source-spontaneous-source-numerator-length"></a>

> 整合来源：`spontaneous-source-numerator-length.md`

# A2 source→common 的 pure numerator/length eliminant

> **依赖：** `spontaneous-source-common-gate.md`、`spontaneous-source-prefix-simple.md`。
>
> **严格状态：**本文把 source first-layer square relation `225x^2=y` 与 source→common gate `C_src(x,tau)=0` 联立，完全消去 denominator phase `x`。resultant不是黑箱高次式，而精确写成 `E(y,tau)^2-14400 y O(y,tau)^2`。乘回真实 `A=a_2`、`S=10^{M-1}` 后得到整数 residual `R_src`; 在当前 endpoint中它严格为正且 `1 mod 8`。因此真正 source→common prime还必须命中一个只含 numerator defect `e` 与 decimal length `M` 的 pure-decimal gate。本文只给必要 projection与 parity，不声称其所有 modular roots都是真正 source primes，也不关闭 A2。

---

## 1. source square-root coordinate

source first layer为

\[
\boxed{225x^2-y=0.}
\tag{1.1}
\]

令

\[
\boxed{r:=15x,}
\qquad
\boxed{r^2=y.}
\tag{1.2}
\]

source→common gate沿用

\[
\begin{aligned}
\mathcal C_{\rm src}(x,\tau)
={}&440(x+2)^2\tau^2\\
&+81(9401x^4-2392x^3-1600x^2-64x-64)\tau\\
&-324x(99x-4)(25x^2+1)(49x^2-4x-2).
\end{aligned}
\tag{1.3}
\]

---

## 2. `已严格完成`：`C_src` 在 source square relation上只有 even/odd 两块

定义

\[
\boxed{
\begin{aligned}
\mathcal E(y,\tau):={}&
11000\tau^2y+9900000\tau^2\\
&+84609\tau y^2-3240000\tau y-29160000\tau\\
&-19404y^3-10836y^2+1474200y,
\end{aligned}}
\tag{2.1}
\]

以及

\[
\boxed{
\mathcal O(y,\tau):=
5500\tau^2-2691\tau y-16200\tau
+296y^2+1764y-8100.}
\tag{2.2}
\]

把 `x^2=y/225` 用于 (1.3) 的 even powers，而 odd powers提出一份 `x`，直接得到 exact identity

\[
\boxed{
5625\mathcal C_{\rm src}(x,\tau)
=\mathcal E(y,\tau)+120r\mathcal O(y,\tau),
\qquad r=15x,\ r^2=y.}
\tag{2.3}
\]

所以正负两个 source square-root branch只相差 `r` 的符号。

---

## 3. `已严格完成`：消去 `x` 后是单个平方差 residual

由 (2.3)：

\[
\boxed{
\mathcal R_{\rm src}^{(y)}(y,\tau)
:=\mathcal E(y,\tau)^2
-14400y\mathcal O(y,\tau)^2.}
\tag{3.1}
\]

直接 resultant计算给

\[
\boxed{
\operatorname{Res}_x
(225x^2-y,\mathcal C_{\rm src})
=2025^2\mathcal R_{\rm src}^{(y)}.}
\tag{3.2}
\]

因此对 genuine non-`3,5` source/common prime：

\[
\boxed{
p\mid\mathcal C_{\rm src},\quad p\mid225x^2-y
\Longrightarrow
p\mid\mathcal R_{\rm src}^{(y)}(y,\tau).}
\tag{3.3}
\]

这把 first-layer source→common 的必要条件从 `(x,y,tau)` 降成纯 `(y,tau)`。

展开 (3.1) 虽是 degree `(6,4)` polynomial，但 (3.1) 的平方差形式才是规范表达；不应以后把 expanded resultant当作新的黑箱对象。

---

## 4. 真实 numerator/length 的整数化

令

\[
\boxed{S:=10^{M-1},}
\qquad
\boxed{A:=a_2=S-e.}
\tag{4.1}
\]

则

\[
y=A/S,
\qquad
\tau=1/(10S).
\tag{4.2}
\]

定义

\[
\boxed{
\mathscr E:=10S^3\mathcal E(A/S,1/(10S)),}
\tag{4.3}
\]

\[
\boxed{
\mathscr O:=10S^2\mathcal O(A/S,1/(10S)).}
\tag{4.4}
\]

直接清分母得到

\[
\boxed{
\begin{aligned}
\mathscr E={}&-194040A^3-108360A^2S+84609A^2\\
&+14742000AS^2-3240000AS+1100A\\
&-29160000S^2+990000S,
\end{aligned}}
\tag{4.5}
\]

\[
\boxed{
\mathscr O=
2960A^2+17640AS-2691A
-81000S^2-16200S+550.}
\tag{4.6}
\]

于是定义 pure numerator/length integer residual

\[
\boxed{
\mathscr R_{\rm src}
:=\mathscr E^2-14400AS\mathscr O^2.}
\tag{4.7}
\]

并有 exact scaling

\[
\boxed{
\mathcal R_{\rm src}^{(y)}(A/S,1/(10S))
=\frac{\mathscr R_{\rm src}}{100S^6}.}
\tag{4.8}
\]

对 genuine odd prime `p!=5`，`S` 为单位，因此 (3.3) 可完全整数化为

\[
\boxed{p\mid\mathscr R_{\rm src}.}
\tag{4.9}
\]

---

## 5. defect form 与 `2`-进 orientation

把 `A=S-e` 代入：

\[
\boxed{
\begin{aligned}
\mathscr E={}&14439600S^3-13943160S^2e-32315391S^2\\
&-690480Se^2+3070782Se+991100S\\
&+194040e^3+84609e^2-1100e,
\end{aligned}}
\tag{5.1}
\]

\[
\boxed{
\mathscr O=
-60400S^2-23560Se-18891S
+2960e^2+2691e+550.}
\tag{5.2}
\]

当前 `M>=11`，所以

\[
2^{10}\mid S.
\tag{5.3}
\]

又 `A=a_2` 为奇数而 `S` 为偶数，故

\[
\boxed{e\text{ odd}.}
\tag{5.4}
\]

由 (5.1) 模 `8`，所有含 `S` 项消失；对 odd `e`：

\[
\mathscr E
\equiv194040e^3+84609e^2-1100e
\equiv0+1+4
\equiv5\pmod8.
\tag{5.5}
\]

由 (5.2) 模 `2`：

\[
\boxed{\mathscr O\equiv1\pmod2.}
\tag{5.6}
\]

而 `14400AS` 被 `2^6\cdot2^{10}` 整除，所以 (4.7) 给

\[
\boxed{
\mathscr R_{\rm src}
\equiv\mathscr E^2
\equiv1\pmod8.}
\tag{5.7}
\]

因此这个 pure numerator/length residual的 total inert valuation parity为偶数。

---

## 6. `已严格完成`：真实 endpoint 上 residual严格为正

真实 numerator window为

\[
249/250<y<1,
\qquad
0<\tau\le10^{-11}.
\tag{6.1}
\]

由 (2.1)：

\[
\mathcal E
\ge
\frac{249}{250}(1474200-10836-19404)
-(84609+3240000+29160000)10^{-11}.
\]
因此

\[
\boxed{\mathcal E>1.438\times10^6.}
\tag{6.2}
\]

而由 (2.2) 粗界

\[
|\mathcal O|
<296+1764+8100+(2691+16200)10^{-11}+5500\cdot10^{-22}
<10161.
\tag{6.3}
\]

故

\[
120\sqrt y\,|\mathcal O|
<120\cdot10161
<1.220\times10^6.
\tag{6.4}
\]

由 (6.2)–(6.4)：

\[
\mathcal E>120\sqrt y\,|\mathcal O|,
\]
所以

\[
\boxed{
\mathcal R_{\rm src}^{(y)}>0.}
\tag{6.5}
\]

再由正 scaling (4.8)：

\[
\boxed{\mathscr R_{\rm src}>0.}
\tag{6.6}
\]

综合 §§5–6：

\[
\boxed{
\mathscr R_{\rm src}>0,
\qquad
\mathscr R_{\rm src}\equiv1\pmod8.}
\tag{6.7}
\]

---

## 7. odd-valuation projection prime 自动看到 source square class

固定 odd prime

\[
p\nmid120AS.
\]

若

\[
v_p(\mathscr R_{\rm src})\text{ 为奇数},
\]
令

\[
a=v_p(\mathscr E),
\qquad b=v_p(\mathscr O).
\]

若 `a!=b`，(4.7) 两项深度不同，立即有

\[
v_p(\mathscr R_{\rm src})=2\min(a,b),
\]
为偶数，矛盾。因此 `a=b=k`。

除去 `p^{2k}` 后，odd residual valuation强迫

\[
\left(\frac{\mathscr E/p^k}{120\,\mathscr O/p^k}\right)^2
\equiv AS\pmod p.
\tag{7.1}
\]

所以

\[
\boxed{AS\text{ 是模 }p\text{ 的平方}.}
\tag{7.2}
\]

因为 `S^2` 是平方，等价于

\[
\boxed{y=A/S\text{ 是模 }p\text{ 的平方}.}
\tag{7.3}
\]

这说明 `R_src` 的 odd-valuation prime不会来自普通 nonsquare projection；它们自动落到 source square-root sheet。若 `E,O` 本身同时被 `p` 整除，则 first-layer两 sign branch同时接触；若至少一个为单位，则 (7.1) 唯一选择其中一个 sign branch。

但必须保留边界：实际 source prime还要满足真实 `Phi_s` / `sigma` Hensel condition。`R_src` 只消去了 `x`，没有消去 source structural orbit。因此 (7.3) 不能把 `R_src` 的所有 inert prime都直接计入 `G_sp`。

---

## 8. 新的 generic source simple frontier

真正 source→common prime现在有两套互补的 global gate：

1. denominator-defect representative
   \[
   \widehat K_{\rm src}=K_{\rm src}/2^8\equiv3\pmod8,
   \]
   只依赖 `(H,M)`；
2. numerator/length residual
   \[
   \mathscr R_{\rm src}\equiv1\pmod8,
   \]
   只依赖 `(e,M)`。

并且 `spontaneous-source-depth-transfer.md` 把 `C_src` depth精确转移到 additive/common depth直至 source half-depth `h`。

因此 generic source common 已从原来的多变量 Hensel系统压成：

\[
\boxed{
\begin{array}{l}
\text{source structural orbit }(\Phi_s,\sigma),\\
\widehat K_{\rm src}(H,M),\\
\mathscr R_{\rm src}(e,M),\\
\text{以及 half-depth saturation}. 
\end{array}}
\]

下一步若要真正关闭 source pool，最值得研究的是这两个相反 mod-8 orientation 的 natural integers在同一个 source primary上的 gcd/allocation；继续做单独的 singular discriminant已无新增信息。

---

<a id="source-spontaneous-source-parity-angle-budget"></a>

> 整合来源：`spontaneous-source-parity-angle-budget.md`

# A2 source odd-parity reuse 再进入 angle common 的 mixed support budget

> **依赖：** `spontaneous-source-parity-angle-overlap.md`、`spontaneous-source-parity-numerator-defect.md`、`endpoint-lattice.md` 的真实 denominator scale。
>
> **严格状态：**source odd/odd reused prime若还同时进入 angle actual/conjugate common support，只剩 numerator-defect sheet `324e-11` 或 denominator sheet `c_Q`。本文利用真实 third denominator ratio `w=2^(M+1)c_Qc_u/5^lambda<1` 给 `c_Q` 全局高度上界，并把全部 source-angle reused distinct support聚合为 `R_SA | c_Q(324e-11)`。这给出 mixed decimal/2-adic product budget，但不证明该 radical为空，因此不关闭 A2。

---

## 1. denominator height

当前真实 denominator scale给

\[
\boxed{
w=\frac{2^{M+1}c_Qc_u}{5^\lambda}<1,}
\tag{1.1}
\]

并且

\[
\boxed{\lambda\le m.}
\tag{1.2}
\]

所有量为正整数，所以从 (1.1)：

\[
c_Q<\frac{5^\lambda}{2^{M+1}c_u}.
\]

由于 `c_u>=1` 与 (1.2)：

\[
\boxed{
c_Q<\frac{5^m}{2^{M+1}}.}
\tag{1.3}
\]

这是不固定 `eta=2m-M` 的 uniform denominator-content height bound。

---

## 2. two allowed angle-common sheets

前文已经证明：若 genuine inert prime `r`

1. 同时承担 `B_W` 与 `D_W` 的 odd parity；
2. 又进入 angle actual/conjugate common gcd；

则必有

\[
\boxed{r\mid c_Q}
\tag{2.1}
\]

或者进入 numerator sheet并进一步满足

\[
\boxed{r\mid324e-11.}
\tag{2.2}
\]

generic `q`-sheet已经删除。

---

## 3. aggregate source-angle reused radical

令 `E_SA` 为所有同时满足 source odd/odd reuse 与 angle-common reuse的 genuine inert primes，并定义

\[
\boxed{R_{SA}:=\prod_{r\in E_{SA}}r.}
\tag{3.1}
\]

每个 distinct prime按 (2.1)/(2.2) 至少整除两个 integers之一，所以

\[
\boxed{R_{SA}\mid c_Q(324e-11).}
\tag{3.2}
\]

这里若某 prime同时整除两者，也只在 radical中计一次，因此 divisibility仍成立。

---

## 4. mixed height budget

numerator defect theorem给

\[
0<324e-11<\frac{81}{625}N.
\tag{4.1}
\]

结合 (1.3)、(3.2)：

\[
\boxed{
R_{SA}
<
\frac{81}{625}N\,
\frac{5^m}{2^{M+1}}.}
\tag{4.2}

用 `N=10^M=2^M5^M` 也可写成

\[
\boxed{
R_{SA}
<
\frac{81}{1250}
5^{M+m}.}
\tag{4.3}

因为

\[
\frac{10^M}{2^{M+1}}=\frac{5^M}{2}.
\]

这说明 source parity若连续复用到 angle common，distinct moving support只能在一个显式 `5^(M+m)` 尺度内增长。

---

## 5. combine with source reuse depth

source odd/odd reuse本身还有 weighted half-depth product

\[
H_{\rm reuse}\mid18K-55<180N.
\]

所以 `E_SA` 子池同时受到：

\[
\boxed{
\prod_{r\in E_{SA}}r^{(e_r+1)/2}<180N,}
\tag{5.1}
\]

和

\[
\boxed{
\prod_{r\in E_{SA}}r
<
\frac{81}{625}N\frac{5^m}{2^{M+1}}.}
\tag{5.2}
\]

第一式惩罚 odd source depth，第二式惩罚 distinct support。

---

## 6. current role

source-side两份 parity若完全 separate，会直接产生独立 primes；若复用，则支付 `18K-55` half-depth；若这枚 reused support还想被 angle pair再次 common-reuse，又必须支付本文的 `c_Q(324e-11)` mixed height。

因此 parity reuse现在形成严格的层级收费：

\[
\boxed{
\text{source reuse}
\Longrightarrow
\text{linear half-depth};
}
\]

\[
\boxed{
\text{source + angle reuse}
\Longrightarrow
\text{linear half-depth + mixed support budget}.}
\]

下一步若再把 additive individual residual support接入，就可以审计三重 parity reuse是否只剩 fixed denominator/numerator-length states。

A2 仍为 `待证`。

---

<a id="source-spontaneous-source-parity-angle-overlap"></a>

> 整合来源：`spontaneous-source-parity-angle-overlap.md`

# A2 source parity reused prime 与 angle common support 的交集压缩

> **依赖：** `spontaneous-source-parity-reuse-depth.md`、`source-discriminant.md`、`spontaneous-residual-parity-doubling.md`。
>
> **严格状态：**odd/odd source parity reused prime 已知位于 `18K-55=0` 且为 noncentral/noncontent。若它还想同时进入 angle actual/conjugate 的 common gcd，angle parity ledger只允许 `A Q_0 c_Q` support。本文利用 `Q_0=c_Qq` 与 `gcd(D_W,q)|49`，以及 `7|q => v_7(D_W)=2`，删除 genuine odd-parity reuse 的 `q`-sheet。最终 angle overlap只剩 numerator-length gate `A=0, 162*10^M-55=0` 或 denominator sheet `c_Q=0`。本文不关闭这两张 sheet，因此不关闭 A2。

---

## 1. source reused setting

固定 genuine inert prime `r`，并假设它真正同时承担两份 source odd parity：

\[
v_r(\mathscr B_W)=v_r(\mathscr D_W)=e
\]
其中 `e` 为奇数。

此前已证明：

\[
\boxed{r\mid18K-55,}
\tag{1.1}
\]

\[
\boxed{r\nmid(2K-9)\omega.}
\tag{1.2}
\]

并且

\[
r^{(e+1)/2}\mid18K-55.
\]

---

## 2. angle common support

residual parity doubling 对 angle actual/conjugate pair证明：若 genuine non-`5` inert prime同时进入两张 angle primitive sheets，则

\[
\boxed{r\mid A Q_0c_Q.}
\tag{2.1}
\]

这里

\[
Q=2^{M+1}Q_0,
\]
而当前 denominator normal form同时有

\[
Q=2^{M+1}c_Qq.
\]

所以

\[
\boxed{Q_0=c_Qq.}
\tag{2.2}
\]

因此 (2.1) 表面上有三种来源：

\[
r\mid A,
\qquad
r\mid c_Q,
\qquad
r\mid q.
\]

下面删除 genuine reused parity的 `q`-sheet。

---

## 3. `q`-sheet cannot carry odd `D_W` parity away from `c_Q`

假设

\[
r\mid Q_0,
\qquad
r\nmid c_Q.
\]

由 (2.2)：

\[
\boxed{r\mid q.}
\tag{3.1}
\]

`source-discriminant.md` 已严格证明

\[
\boxed{\gcd(\mathscr D_W,q)\mid49.}
\tag{3.2}
\]

而当前 reused prime本来就满足 `r|D_W`，所以

\[
\boxed{r=7.}
\tag{3.3}
\]

但同一文件还给出精确 `7`-primary rule：

\[
\boxed{7\mid q\Longrightarrow v_7(\mathscr D_W)=2.}
\tag{3.4}
\]

右边为偶数，与 reused setting中

\[
v_r(\mathscr D_W)=e\text{ odd}
\]
矛盾。

所以：

\[
\boxed{
r\mid Q_0,\quad v_r(\mathscr D_W)\text{ odd}
\Longrightarrow
r\mid c_Q.}
\tag{3.5}
\]

`q` 本身不能作为 odd/odd source parity reuse与 angle common 的独立 support。

---

## 4. angle overlap reduces to `A c_Q`

综合 (2.1)、(3.5)：

\[
\boxed{
\text{odd/odd source reused }r\text{ 若同时 common to angle pair}
\Longrightarrow
r\mid A c_Q.}
\tag{4.1}
\]

所以只剩两张 sheet：

1. numerator sheet `r|A`；
2. denominator prefix sheet `r|c_Q`。

---

## 5. numerator sheet becomes a pure decimal-length gate

当前

\[
K=9N+10A,
\qquad
N=10^M.
\]

于是

\[
18K-55
=162N+180A-55.
\tag{5.1}
\]

若 reused prime同时满足

\[
r\mid18K-55,
\qquad
r\mid A,
\]
则 (5.1) 模 `r` 给

\[
\boxed{r\mid162N-55.}
\tag{5.2}
\]

即

\[
\boxed{r\mid162\cdot10^M-55.}
\tag{5.3}
\]

因此 numerator-angle overlap不再含 `A` 自由 residue，而被投影成纯 decimal exponent orbit。

定义

\[
\boxed{L_M:=162\cdot10^M-55.}
\tag{5.4}
\]

则 reused numerator-angle prime必须同时满足

\[
\boxed{r\mid L_M,\qquad r\mid\mathscr D_W.}
\tag{5.5}
\]

---

## 6. quadratic-character consequence on the length sheet

在 genuine source-discriminant root上 `r\nmid55z c_u`，由

\[
55z^2\equiv49c_u^2\pmod r
\]
可知

\[
\boxed{\left(\frac{55}{r}\right)=1.}
\tag{6.1}
\]

而 length gate给

\[
10^M\equiv55\cdot162^{-1}\pmod r.
\]
由于

\[
162=2\cdot9^2,
\]
取 Legendre symbol：

\[
\boxed{
\left(\frac{10}{r}\right)^M
=\left(\frac2r\right).}
\tag{6.2}
\]

因此：

- 若 `M` 为偶数，LHS 为 `1`，故
  \[
  \boxed{\left(\frac2r\right)=1.}
  \tag{6.3}
  \]
  对 `r=3 mod4` 即 `r=7 mod8`；
- 若 `M` 为奇数，利用 `(10/r)=(2/r)(5/r)`：
  \[
  \boxed{\left(\frac5r\right)=1.}
  \tag{6.4}
  \]
  再由 `(55/r)=1` 得
  \[
  \boxed{\left(\frac{11}{r}\right)=1.}
  \tag{6.5}
  \]

这些只是 residue-class filters，不单独排除 moving primes。

---

## 7. denominator sheet

另一种可能是

\[
\boxed{r\mid c_Q.}
\tag{7.1}
\]

本文不宣称 `D_W` 与 `c_Q` 全局互素；source ratio在清去公共 denominator scale后本来就不含 `c_Q`，因此这种 overlap不能靠 (3.2) 删除。

所以 angle reuse的 denominator exception必须被明确保留为 genuine frontier，而不能误归入已经删除的 `q`-sheet。

---

## 8. current overlap frontier

source odd-parity reused prime若还想让 angle actual/conjugate pair复用同一 prime，只剩

\[
\boxed{
\begin{array}{ll}
\text{numerator-length:}&r\mid A,\quad r\mid162\cdot10^M-55,\\
\text{denominator:}&r\mid c_Q.
\end{array}}
\tag{8.1}

generic `q`-support已经严格删除。

因此 source parity reuse与 angle parity reuse的共同 moving freedom被压成一个 pure decimal exponent orbit加一个 denominator-content exception。后续应分别攻击 `L_M` 的 multiplicative order / short-height，以及 `c_Q` 的既有有限/height constraints。

A2 仍为 `待证`。

---

<a id="source-spontaneous-source-parity-collision-gate"></a>

> 整合来源：`spontaneous-source-parity-collision-gate.md`

# A2 `B_W / D_W` source parity suppliers 的 collision gate

> **依赖：** `source-discriminant.md`、`spontaneous-height-content-oversaturation.md`、`spontaneous-residual-parity-doubling.md`。
>
> **严格状态：**`B_W` 与 positive source discriminant `D_W/2` 都是 odd-inert parity suppliers。本文证明二者若复用同一 genuine prime，则该 prime必须进入固定 linear sheet `18K-55=0`；该 sheet与 additive residual overlap的 central factor `2K-9` 在 `3 mod 4` support上完全分离，并且与 omega-height target quadratic `P=6K^2-36K+55` 的共同 odd prime只能来自 `3,5,11`。因此 source parity若由一枚共同 moving inert prime承担，该 prime必是 noncentral、non-omega-target 的新 label。本文仍允许该 linear sheet本身存在，故不关闭 A2。

---

## 1. exact square collision identity

沿用

\[
\mathscr D_W:=55z^2-49c_u^2,
\]

\[
\mathscr B_W
=c_u^2(5K^2-36K+55)+z^2K^2.
\]

直接计算：

\[
\begin{aligned}
55\mathscr B_W-K^2\mathscr D_W
={}&55c_u^2(5K^2-36K+55)\\
&+55z^2K^2-K^2(55z^2-49c_u^2)\\
={}&c_u^2\left[55(5K^2-36K+55)+49K^2\right].
\end{aligned}
\]

而括号恰为

\[
324K^2-1980K+3025=(18K-55)^2.
\]

所以得到 exact identity

\[
\boxed{
55\mathscr B_W-K^2\mathscr D_W
=c_u^2(18K-55)^2.}
\tag{1.1}
\]

这不是 resultant only；它是整数平方恒等式。

---

## 2. common genuine prime must hit the linear sheet

令 odd prime `r` 满足

\[
r\mid\mathscr B_W,
\qquad
r\mid\mathscr D_W,
\qquad
r\nmid c_u.
\]

由 (1.1)：

\[
r\mid c_u^2(18K-55)^2.
\]

所以

\[
\boxed{r\mid18K-55.}
\tag{2.1}
\]

反过来若

\[
r\mid\mathscr D_W,
\qquad
r\mid18K-55,
\qquad
r\nmid55,
\]
则 (1.1) 给 `r|B_W`。因此在与 `55c_u` 分离的 genuine sector：

\[
\boxed{
r\mid\mathscr B_W,\mathscr D_W
\Longleftrightarrow
r\mid\mathscr D_W,\ 18K-55.}
\tag{2.2}
\]

所以两份 source parity的 moving overlap只有一张 fixed linear sheet。

---

## 3. collision sheet is disjoint from additive central overlap on inert support

additive residual parity doubling theorem证明，height-free additive companions若再次共享 odd prime，只能回到

\[
(2K-9)\omega.
\]

先比较两个 linear factors：

\[
(18K-55)-9(2K-9)=26.
\tag{3.1}
\]

因此

\[
\boxed{\gcd(18K-55,2K-9)\mid26.}
\tag{3.2}
\]

若 odd prime `r` 同时整除二者，则

\[
r=13.
\]
但

\[
13\equiv1\pmod4.
\]
所以对 inert prime：

\[
\boxed{
r\equiv3\pmod4,\ r\mid18K-55
\Longrightarrow
r\nmid2K-9.}
\tag{3.3}
\]

因此 source parity collision prime不可能再使用 additive central sheet。

---

## 4. collision prime is non-content

`source-discriminant.md` 已证明

\[
\boxed{\gcd(\mathscr D_W,\omega)\mid6.}
\tag{4.1}
\]

所以任意 non-`3` odd divisor of `D_W` 都满足

\[
\boxed{r\nmid\omega.}
\tag{4.2}
\]

特别地，任何 genuine non-`3` source parity collision prime同时具有

\[
\boxed{r\nmid(2K-9)\omega.}
\tag{4.3}
\]

结合 residual parity doubling：若这样一枚 prime恰进入某一个 additive height-free residual，它不可能同时进入另一个 residual；additive pair不能用它复用两份 parity。

注意本文不声称 collision prime必进入 additive residual pair中的任意一个。

---

## 5. collision sheet versus omega-height target quadratic

omega-height target quadratic为

\[
P_{\omega H}(K)=6K^2-36K+55.
\]

将 linear root `18K-55=0` 代入并清分母：

\[
18^2P_{\omega H}(55/18)=330.
\]
等价地 polynomial resultant 为

\[
\boxed{
\operatorname{Res}_K(P_{\omega H},18K-55)=330
=2\cdot3\cdot5\cdot11.}
\tag{5.1}
\]

因此任何 odd prime同时满足

\[
r\mid P_{\omega H}(K),
\qquad
r\mid18K-55
\]
必有

\[
\boxed{r\in\{3,5,11\}.}
\tag{5.2}
\]

在 genuine non-`3,5` height target sector只剩 fixed `11`。

而真正 serial/equal-depth target还满足 `r|omega`；由 (4.1)，non-`3` 的 `D_W` divisor不能同时整除 `omega`。所以 source parity collision sheet与 genuine serial target pool本身完全分离。

---

## 6. parity supplier dichotomy

`source-discriminant.md` 给两份 global odd-inert parity：

\[
\mathscr B_W\equiv7\pmod8,
\]

\[
\mathscr D_W/2\equiv3\pmod4.
\]

因此各自都必须含 `3 mod 4` prime到奇次。

现在两份 parity的 allocation只有两种可能：

1. **separate suppliers**：存在至少两枚不同 inert primes，分别承担 `B_W` 与 `D_W/2` 的奇 parity；
2. **reused supplier**：某枚 inert prime同时整除 `B_W,D_W`，此时由 §2 它必须满足
   \[
   \boxed{18K-55\equiv0\pmod r.}
   \]

而 reused supplier在 genuine non-`3` sector还自动满足

\[
r\nmid\omega,
\qquad
r\nmid2K-9,
\]
并且不能是 moving omega-height target。

这给 source parity一个严格的“两枚 prime product surcharge / 单枚 fixed linear sheet”二分。

---

## 7. current interface to residual parity doubling

若 source parity走 separate-supplier branch，则已经产生至少两枚不同 inert primes；后续可直接结合 natural representative高度做 product budget。

若走 reused-supplier branch，则唯一 reusable prime被压入

\[
18K-55=0
\]
且是 noncentral、noncontent。由 additive residual parity doubling theorem，这样的 prime不能同时承担 height-free additive actual/companion两份 parity。

所以后续最值得继续审计的是 linear sheet `18K-55` 与 angle pair common support

\[
AQ_0c_Q
\]
以及 additive individual residual supports的 cross-overlap。

A2 仍为 `待证`。

---

<a id="source-spontaneous-source-parity-common-gcd"></a>

> 整合来源：`spontaneous-source-parity-common-gcd.md`

# A2 source parity 的 canonical common gcd 与 square-root depth

> **依赖：** `source-discriminant.md`、`spontaneous-source-parity-collision-gate.md`、`spontaneous-source-parity-reuse-depth.md`。
>
> **严格状态：**`B_W` 与 `D_W/2` 都是 positive primitive `3 mod 4` source parity carriers。本文用完整 common gcd `G_S=gcd(B_W,D_W/2)` 统一此前的 separate/reused supplier讨论：约掉 `G_S` 后两个 coprime residual具有完全相同的 mod-4 orientation。若 `G_S=1 mod4`，两 residual各自必须携带独立 odd-inert parity；若 `G_S=3 mod4`，common gcd吸收 parity。进一步，exact square collision证明每个 genuine common prime的 gcd exponent `k` 至少以 `ceil(k/2)` 深度进入短 linear carrier `18K-55`；因此整个 generic common gcd的 square-root depth受 `<180N` 控制。本文仍保留 fixed `3,5,11` exceptions并不证明 residual primes不存在，故不关闭 A2。

---

## 1. two primitive source parity carriers

已有

\[
\boxed{\mathscr B_W\equiv7\pmod8,}
\tag{1.1}

所以

\[
\boxed{\mathscr B_W\equiv3\pmod4.}
\tag{1.2}

source discriminant满足

\[
\mathscr D_W\equiv6\pmod8,
\]
因此

\[
\boxed{\frac{\mathscr D_W}{2}\equiv3\pmod4.}
\tag{1.3}

两者均为 positive odd integers。

---

## 2. canonical common gcd and residuals

定义

\[
\boxed{
G_S:=\gcd\!\left(\mathscr B_W,\frac{\mathscr D_W}{2}\right).}
\tag{2.1}

由于 `B_W` 为 odd，也有

\[
G_S=\gcd(\mathscr B_W,\mathscr D_W).
\]

定义 coprime residuals

\[
\boxed{B_S:=\frac{\mathscr B_W}{G_S},}
\qquad
\boxed{D_S:=\frac{\mathscr D_W}{2G_S}.}
\tag{2.2}

显然

\[
\boxed{\gcd(B_S,D_S)=1.}
\tag{2.3}

由 (1.2),(1.3)，`G_S` 为 odd，因此模 `4` 可逆，并有

\[
\boxed{
B_S\equiv D_S\equiv3G_S^{-1}\pmod4.}
\tag{2.4}

---

## 3. canonical source parity doubling

若

\[
\boxed{G_S\equiv1\pmod4,}
\]
则 (2.4) 给

\[
\boxed{B_S\equiv D_S\equiv3\pmod4.}
\tag{3.1}

因为 `B_S,D_S` positive、odd、coprime，它们各自都必须含至少一枚 `3 mod4` prime到奇次，而且两枚 suppliers必不同。因此：

\[
\boxed{
G_S\equiv1\pmod4
\Longrightarrow
\text{source residual parity至少需要两枚 distinct inert primes}.}
\tag{3.2}

若

\[
\boxed{G_S\equiv3\pmod4,}
\]
则

\[
\boxed{B_S\equiv D_S\equiv1\pmod4.}
\tag{3.3}

此时两份 source odd parity已被 common gcd整体吸收；residuals不再被 mod-4 强迫各自生成 inert prime。

所以此前“separate / reused”讨论现在有 canonical integer formulation，而不需要先人为选择 supplier primes。

---

## 4. common-prime depth from the square collision

已有 exact identity

\[
\boxed{
55\mathscr B_W-K^2\mathscr D_W
=c_u^2L_S^2,}
\qquad
L_S:=18K-55.
\tag{4.1}

固定 odd common prime `r`，并假设 genuine unit separation

\[
\boxed{r\nmid55Kc_u.}
\tag{4.2}

写

\[
a:=v_r(\mathscr B_W),
\qquad
d:=v_r(\mathscr D_W),
\]

\[
\boxed{k:=v_r(G_S)=\min(a,d),}
\qquad
\ell:=v_r(L_S).
\tag{4.3}

### unequal source depths

若

\[
a\ne d,
\]
则 (4.1) 左端赋值精确为 `k`。右端赋值为 `2ell`，所以

\[
\boxed{k=2\ell.}
\tag{4.4}

特别地 `k` 自动为偶数，并且

\[
\boxed{\ell=k/2.}
\tag{4.5}

### equal source depths

若

\[
a=d=k,
\]
左端两个 summands等深，故

\[
v_r(55B_W-K^2D_W)\ge k.
\]

由 (4.1)：

\[
2\ell\ge k.
\]
所以

\[
\boxed{\ell\ge\left\lceil\frac k2\right\rceil.}
\tag{4.6}

综合两类：

\[
\boxed{
v_r(18K-55)
\ge\left\lceil\frac{v_r(G_S)}2\right\rceil}
\tag{4.7}

对每个 genuine unit-separated common prime成立。

---

## 5. global square-root-depth product

令 `E_S^gen` 为 `G_S` 的 genuine odd common prime support中满足 (4.2) 的 primes。定义

\[
\boxed{
H_S^{\rm gen}
:=\prod_{r\in E_S^{\rm gen}}
r^{\lceil v_r(G_S)/2\rceil}.}
\tag{5.1}

逐 prime由 (4.7)：

\[
\boxed{H_S^{\rm gen}\mid18K-55.}
\tag{5.2}

endpoint有

\[
0<K<10N,
\]
故

\[
\boxed{0<18K-55<180N.}
\tag{5.3}

因此

\[
\boxed{H_S^{\rm gen}<180N.}
\tag{5.4}

这对 common gcd的**全部 generic depth**收费，而不只对 odd/odd reused exponents收费。

---

## 6. squarefree form

令

\[
G_S^{\rm gen}:=\prod_{r\in E_S^{\rm gen}}r^{v_r(G_S)},
\]

以及 odd-exponent radical

\[
\boxed{
R_S^{\rm odd}
:=\prod_{\substack{r\in E_S^{\rm gen}\\v_r(G_S)\text{ odd}}}r.}
\tag{6.1}

则按 exponent逐项有

\[
\boxed{(H_S^{\rm gen})^2=G_S^{\rm gen}R_S^{\rm odd}.}
\tag{6.2}

所以 (5.4) 等价给

\[
\boxed{
G_S^{\rm gen}R_S^{\rm odd}
<(180N)^2.}
\tag{6.3}

若 `G_S≡3 mod4` 的奇 parity由 generic common support承担，则 `R_S^odd` 中至少含一枚 `3 mod4` prime。

---

## 7. fixed exceptions

(4.2) 故意保留固定 bad support。由 source-discriminant 的 gcd audit：

- `r|c_u` 的 nontrivial overlap只可能来自 `5,11`；
- `r=3` 为 source-discriminant fixed parity gate；
- `r|K` 与 (4.1) 的 common genuine root除固定 `5,11` 外不发生。

所以真正没有纳入 `H_S^gen` 的只是有限固定 small-prime bookkeeping；不存在额外 moving common family被隐藏。

---

## 8. relation to serial pool

serial-first target primes属于 `omega` support，而 source-discriminant满足

\[
\gcd(D_W,\omega)\mid6.
\]

因此 non-`3` serial pool与 `G_S^gen` support分离。

现在 source side可同时使用：

1. canonical parity dichotomy `G_S mod4`；
2. generic common-gcd square-root budget
   \[
   H_S^{gen}<180N;
   \]
3. serial/double pool的独立 weighted budget。

这为后续 global product allocation提供了不重复计数的两个 canonical sectors。

A2 仍为 `待证`。

---

<a id="source-spontaneous-source-parity-decimal-gcd"></a>

> 整合来源：`spontaneous-source-parity-decimal-gcd.md`

# A2 source parity common gcd 的 fully-decimal realization

> **依赖：** `spontaneous-source-parity-common-gcd.md`、`spontaneous-height-equal-depth-decimal-tropical-identity.md`、`source-discriminant.md`。
>
> **严格状态：**source common gcd `G_S=gcd(B_W,D_W/2)` 原先仍使用 `z,c_u`。本文利用 exact source ratio把 `D_W` 与已有 `B_dec` 同时乘回真实 decimal denominator plane，得到 `D_dec=55T^2Q^2-49b_3^2`。二者具有完全相同的 square scale `(b_3/c_u)^2`，所以对 `B_dec,D_dec/2` 取 ordinary gcd后再约掉，精确恢复 source coprime residuals `B_S,D_S`。source parity doubling因此可完全从原 decimal integers读取。并且 `D_dec` 只有 `2m+2M+3` 位、`B_dec` 只有 `2m+4M+3` 位。本文是 canonicalization，不关闭 A2。

---

## 1. decimal source discriminant

source ratio为

\[
\boxed{b_3z=Tc_uQ.}
\tag{1.1}

source discriminant

\[
\mathscr D_W=55z^2-49c_u^2.
\]

定义 pure-decimal integer

\[
\boxed{
D_{\rm dec}:=55T^2Q^2-49b_3^2.}
\tag{1.2}

由 (1.1)：

\[
b_3^2z^2=T^2c_u^2Q^2,
\]
所以

\[
\boxed{
b_3^2\mathscr D_W=c_u^2D_{\rm dec}.}
\tag{1.3}

当前 source geometry给 `D_W>0`，故

\[
\boxed{D_{\rm dec}>0.}
\tag{1.4}

---

## 2. common square scale

已有 decimal height reader

\[
\boxed{
b_3^2\mathscr B_W=c_u^2B_{\rm dec},}
\tag{2.1}

其中

\[
B_{\rm dec}
=b_3^2(5K^2-36K+55)+T^2Q^2K^2.
\]

endpoint denominator formula含 `c_u` 为因子，因此

\[
\boxed{L:=b_3/c_u\in\mathbb Z_{>0}.}
\tag{2.2}

由 (1.3),(2.1)：

\[
\boxed{D_{\rm dec}=L^2\mathscr D_W,}
\tag{2.3}

\[
\boxed{B_{\rm dec}=L^2\mathscr B_W.}
\tag{2.4}

两个 source carriers乘回 decimal plane时获得的是**完全相同的 square scale**。

---

## 3. fully-decimal common gcd

定义

\[
\boxed{
G_{\rm src}^{\rm dec}
:=\gcd\!\left(B_{\rm dec},\frac{D_{\rm dec}}2\right).}
\tag{3.1}

因为 `D_W/2` 为整数且 (2.3),(2.4)：

\[
\begin{aligned}
G_{\rm src}^{\rm dec}
&=\gcd\left(L^2B_W,L^2D_W/2\right)\\
&=L^2\gcd(B_W,D_W/2).
\end{aligned}
\]

所以

\[
\boxed{G_{\rm src}^{\rm dec}=L^2G_S.}
\tag{3.2}

定义 decimal residuals

\[
\boxed{
B_{\rm src}^\circ
:=\frac{B_{\rm dec}}{G_{\rm src}^{\rm dec}},}
\tag{3.3}

\[
\boxed{
D_{\rm src}^\circ
:=\frac{D_{\rm dec}}{2G_{\rm src}^{\rm dec}}.}
\tag{3.4}

则 square scale完全消失：

\[
\boxed{B_{\rm src}^\circ=B_S,}
\tag{3.5}

\[
\boxed{D_{\rm src}^\circ=D_S.}
\tag{3.6}

因此

\[
\boxed{\gcd(B_{\rm src}^\circ,D_{\rm src}^\circ)=1.}
\tag{3.7}

这给 source parity residuals 一个不再依赖 source variables的 ordinary decimal-gcd定义。

---

## 4. parity is readable directly from decimal quotients

source common-gcd theorem已有

\[
B_S\equiv D_S\pmod4,
\]
且两者只能同时为 `1` 或同时为 `3 mod4`。

由 (3.5),(3.6)：

\[
\boxed{
B_{\rm src}^\circ
\equiv D_{\rm src}^\circ\pmod4.}
\tag{4.1}

所以不必显式恢复 `L` 或 `G_S`：直接计算两个 pure-decimal gcd quotients即可判断 source parity allocation。

若

\[
\boxed{B_{\rm src}^\circ\equiv D_{\rm src}^\circ\equiv3\pmod4,}
\tag{4.2}

则它们 positive、odd、coprime，各自必须携带一份 odd inert parity，且 suppliers不同。

若

\[
\boxed{B_{\rm src}^\circ\equiv D_{\rm src}^\circ\equiv1\pmod4,}
\tag{4.3}

则 source residual pair不再强迫新增 inert supplier；parity已被完整 common gcd吸收。

---

## 5. short window for `D_dec`

写

\[
q:=Q/N,
\qquad w:=b_3/T.
\]

则

\[
\frac{D_{\rm dec}}{T^2N^2}
=55q^2-49\frac{w^2}{N^2}.
\tag{5.1}

endpoint给

\[
\frac{21}{10}<q<\frac{40}{19},
\qquad
0<w<\frac{843}{1000},
\qquad N\ge10^{11}.
\]

因此

\[
55\left(\frac{21}{10}\right)^2
-49\left(\frac{843}{1000\cdot10^{11}}\right)^2
>242,
\]

以及

\[
55\left(\frac{40}{19}\right)^2<244.
\]

所以

\[
\boxed{242T^2N^2<D_{\rm dec}<244T^2N^2.}
\tag{5.2}

特别地

\[
\boxed{D_{\rm dec}\text{ 恰有 }2m+2M+3\text{ 位}.}
\tag{5.3}

---

## 6. short window for `B_dec`

由定义

\[
\frac{B_{\rm dec}}{T^2N^4}
=
\frac{w^2}{N^2}
\left(5s^2-\frac{36s}{N}+\frac{55}{N^2}\right)
+q^2s^2,
\tag{6.1}

其中

\[
s:=K/N,
\qquad
\frac{2499}{250}<s<10.
\]

第一项非负。故

\[
\frac{B_{\rm dec}}{T^2N^4}
>
\left(\frac{21}{10}\right)^2
\left(\frac{2499}{250}\right)^2
>440.
\]

上界使用 `q<40/19,s<10,w<843/1000,N>=10^11`：

\[
\frac{B_{\rm dec}}{T^2N^4}
<
100\left(\frac{40}{19}\right)^2
+\frac1{10^{22}}
\left(\frac{843}{1000}\right)^2
\left(500+\frac{55}{10^{22}}\right)
<444.
\]

所以

\[
\boxed{440T^2N^4<B_{\rm dec}<444T^2N^4.}
\tag{6.2}

并且

\[
\boxed{B_{\rm dec}\text{ 恰有 }2m+4M+3\text{ 位}.}
\tag{6.3}

---

## 7. source parity now lives on two natural decimal scales

source residual parity的两个 parent carriers现在分别只有

\[
D_{\rm dec}\asymp T^2N^2,
\]

\[
B_{\rm dec}\asymp T^2N^4.
\]

其中较短的 `D_dec` 比 `B_dec` 少整整 `2M` 个 decimal digits。两者共享的巨大 denominator/source scale由 ordinary gcd `G_src^dec` 自动删掉。

因此后续 global source parity budget不必再回 `z,c_u,B_W,D_W`：可直接在

\[
\boxed{B_{\rm src}^\circ,D_{\rm src}^\circ}
\]
这两个 pure-decimal coprime integers上工作。

A2 仍为 `待证`。

---

<a id="source-spontaneous-source-parity-decimal-square-gate"></a>

> 整合来源：`spontaneous-source-parity-decimal-square-gate.md`

# A2 source common depth 的 fully-decimal square gate

> **依赖：** `spontaneous-source-parity-decimal-gcd.md`、`spontaneous-source-parity-common-gcd.md`。
>
> **严格状态：**本文把 source square collision也完全乘回 decimal plane：`55B_dec-K^2D_dec=b_3^2(18K-55)^2`。随后定义 `G_free=G_dec/gcd(G_dec,b_3^2)`，证明对所有与 `c_u` 分离的 genuine common primes，它精确恢复 source common gcd `G_S` 的局部 exponent；巨大 denominator square scale自动被 `b_3^2` gcd删掉。因此 source common depth和 linear square-root surcharge均可由真实 decimal integers canonical 读取，只剩 fixed `5/11` 的 `c_u` overlap需单列。本文不证明 `G_free=1`，故不关闭 A2。

---

## 1. decimal square collision

已有

\[
B_{\rm dec}=L^2\mathscr B_W,
\qquad
D_{\rm dec}=L^2\mathscr D_W,
\qquad
L=b_3/c_u.
\]

source square collision为

\[
55\mathscr B_W-K^2\mathscr D_W
=c_u^2(18K-55)^2.
\]

乘以 `L^2`，并使用 `L^2c_u^2=b_3^2`：

\[
\boxed{
55B_{\rm dec}-K^2D_{\rm dec}
=b_3^2(18K-55)^2.}
\tag{1.1}

全部量均为真实 decimal/prefix integers。

---

## 2. decimal common gcd contains one known square scale

定义

\[
G_{\rm dec}
:=\gcd\!\left(B_{\rm dec},D_{\rm dec}/2\right).
\]

已有精确式

\[
\boxed{G_{\rm dec}=L^2G_S,}
\tag{2.1}

其中

\[
G_S=\gcd(B_W,D_W/2).
\]

所以 `G_dec` 中的 huge denominator/source common factor `L^2` 完全是已知 square scale。

---

## 3. remove the square scale by one ordinary gcd

定义

\[
\boxed{
G_{\rm free}
:=\frac{G_{\rm dec}}{\gcd(G_{\rm dec},b_3^2)}.}
\tag{3.1}

这是整数。

固定 odd common prime `r`，并假设

\[
\boxed{r\nmid c_u.}
\tag{3.2}

写

\[
\ell:=v_r(L)=v_r(b_3),
\]

\[
k:=v_r(G_S).
\]

由 (2.1)：

\[
\boxed{v_r(G_{\rm dec})=2\ell+k.}
\tag{3.3}

而 (3.2) 下

\[
\boxed{v_r(b_3^2)=2\ell.}
\tag{3.4}

所以

\[
v_r(\gcd(G_{\rm dec},b_3^2))=2\ell,
\]
并得到

\[
\boxed{v_r(G_{\rm free})=k=v_r(G_S).}
\tag{3.5}

因此 `G_free` 在整个 genuine `c_u`-free common sector精确恢复 source common-gcd depth。

---

## 4. fixed `c_u` exceptions are finite

source discriminant gcd audit已有

\[
\gcd(D_W,c_u)\mid55.
\]

所以 odd common prime若违反 (3.2)，只能来自

\[
\boxed{5,11.}
\tag{4.1}

这些是固定 small-prime bookkeeping，不构成新的 moving support。

因此除 `5/11` 外：

\[
\boxed{
\operatorname{Supp}(G_{\rm free})
=\operatorname{Supp}(G_S),}
\tag{4.2}

且所有 local exponents完全相同。

---

## 5. decimal form of the square-root depth law

source common-gcd theorem证明，对 genuine unit common prime

\[
v_r(18K-55)
\ge\left\lceil\frac{v_r(G_S)}2\right\rceil.
\]

使用 (3.5)，可完全改写为

\[
\boxed{
 v_r(18K-55)
\ge\left\lceil\frac{v_r(G_{\rm free})}{2}\right\rceil}
\tag{5.1}

对所有 odd `r notin {5,11}` 且属于 genuine common sector成立。

所以 source common depth的 canonical decimal pipeline现在是

\[
\boxed{
(B_{\rm dec},D_{\rm dec},b_3)
\longrightarrow G_{\rm dec}
\longrightarrow G_{\rm free}
\longrightarrow18K-55.}
\tag{5.2}

不再需要显式恢复 `z,c_u,B_W,D_W`。

---

## 6. parity classification also stays decimal

前文定义

\[
B_{\rm src}^\circ=B_{\rm dec}/G_{\rm dec},
\qquad
D_{\rm src}^\circ=D_{\rm dec}/(2G_{\rm dec}).
\]

它们是 coprime odd integers且具有同一 mod-4 orientation。

所以 source side现在完全由以下原整数派生对象控制：

\[
\boxed{
G_{\rm free},\quad
B_{\rm src}^\circ,\quad
D_{\rm src}^\circ,\quad
18K-55.}
\]

- `G_free` 读 common depth；
- 两 residual quotients读 parity是否被 common gcd吸收；
- `18K-55` 支付 common depth的 square-root height。

---

## 7. current role

这一步把 source parity/common-depth ledger从 source coordinates彻底迁回 decimal plane。后续若做 global gcd ladder、parity allocation或 product-height比较，都可以只操作真实 decimal integers。

唯一需要保留的 source-side exception只是固定 `5/11`，而不是 moving prime family。

A2 仍为 `待证`。

---

<a id="source-spontaneous-source-parity-numerator-defect"></a>

> 整合来源：`spontaneous-source-parity-numerator-defect.md`

# A2 source parity numerator-angle reuse 的 pure defect gate

> **依赖：** `spontaneous-source-parity-angle-overlap.md`、`endpoint-lattice.md` 的最危险 `(a,k)=(9,2)` endpoint defect shell。
>
> **严格状态：**source odd/odd reused prime若进入 angle common numerator sheet，前文只把它投影到 `162*10^M-55` length gate。本文恢复 endpoint defect `a_2=10^(M-1)-e`，把该 gate进一步降到极短整数 `324e-11`。所有 numerator-angle reused primes的 radical都整除 `324e-11 < (81/625)N`。本文不排除该 defect integer拥有 inert divisors，因此不关闭 A2。

---

## 1. endpoint numerator defect

当前最危险 core 已严格固定

\[
\boxed{a_2=10^{M-1}-e,}
\tag{1.1}
\]

并有

\[
\boxed{0<e<\frac{10^{M-1}}{250}.}
\tag{1.2}
\]

令

\[
N=10^M.
\]

则

\[
10^{M-1}=\frac N{10},
\]
所以

\[
\boxed{a_2=\frac N{10}-e.}
\tag{1.3}
\]

当前

\[
K=9N+10a_2,
\]
因此

\[
\boxed{K=10(N-e).}
\tag{1.4}
\]

---

## 2. numerator overlap plus source collision

固定 source odd/odd reused prime `r`，并进一步假设它进入 angle numerator sheet：

\[
\boxed{r\mid a_2.}
\tag{2.1}
\]

source parity collision gate已有

\[
\boxed{r\mid18K-55.}
\tag{2.2}
\]

由 (1.3)、(2.1)：

\[
\boxed{N\equiv10e\pmod r.}
\tag{2.3}
\]

再由 (1.4)：

\[
18K-55
=180(N-e)-55.
\]

模 `r` 使用 (2.3)：

\[
18K-55
\equiv180(10e-e)-55
=1620e-55
=5(324e-11).
\]

因此 genuine reused prime `r!=5` 满足

\[
\boxed{r\mid324e-11.}
\tag{2.4}
\]

这比原 length gate

\[
r\mid162N-55
\]
更短，并且只依赖小 numerator defect `e`。

---

## 3. positive short window

由 `e>=1`：

\[
324e-11\ge313>0.
\]

由 (1.2)：

\[
e<\frac{N}{2500}.
\]
所以

\[
324e-11<\frac{324}{2500}N
=\frac{81}{625}N.
\]

因此定义

\[
\boxed{L_e:=324e-11}
\tag{3.1}
\]
后有

\[
\boxed{
0<L_e<\frac{81}{625}N<0.13N.}
\tag{3.2}
\]

这是一个仅 `O(10^M)`、且常数不到 `0.13` 的 pure-defect natural representative。

---

## 4. radical budget for numerator-angle reused primes

令 `E_A` 为所有同时满足

1. source odd/odd parity reuse；
2. angle common numerator sheet `r|a_2`；

的 genuine inert primes。

定义其 radical

\[
\boxed{R_A:=\prod_{r\in E_A}r.}
\tag{4.1}
\]

由 (2.4)，所有这些 distinct primes都整除同一个 `L_e`，所以

\[
\boxed{R_A\mid L_e.}
\tag{4.2}
\]

进而

\[
\boxed{R_A<\frac{81}{625}N.}
\tag{4.3}
\]

因此 numerator-angle reuse的 moving support无法比 `N` 更快增长，而且实际常数小于 `0.13`。

---

## 5. relation to reuse half-depth

source parity reuse depth theorem还给每个 `r in E_A`

\[
r^{(e_r+1)/2}\mid18K-55,
\]
其中 `e_r=v_r(B_W)=v_r(D_W)` 为奇数。

所以 numerator-angle reused pool同时受到两种独立形状的 natural representatives约束：

\[
\boxed{
\prod r^{(e_r+1)/2}\mid18K-55<180N,}
\tag{5.1}
\]

\[
\boxed{
\prod r\mid324e-11<\frac{81}{625}N.}
\tag{5.2}
\]

前者控制 depth，后者控制 distinct support。

---

## 6. current angle-reuse split

source parity reused prime若再被 angle pair复用，现在只剩：

### numerator-defect sheet

\[
\boxed{r\mid a_2,\qquad r\mid324e-11,}
\]
并有 radical budget (4.3)；

### denominator sheet

\[
\boxed{r\mid c_Q.}
\]

所以原来的 generic `A Q_0 c_Q` overlap已经从三块 support压成一个 very short defect carrier加一个 denominator-content exception。

A2 仍为 `待证`。

---

<a id="source-spontaneous-source-parity-reuse-depth"></a>

> 整合来源：`spontaneous-source-parity-reuse-depth.md`

# A2 source odd-parity reuse 的 linear half-depth surcharge

> **依赖：** `spontaneous-source-parity-collision-gate.md`。
>
> **严格状态：**若同一 genuine inert prime要同时承担 `B_W` 与 `D_W/2` 两份 odd parity，则它在两个 source carriers中的赋值都为奇数。利用 exact square collision identity，本文证明这两个奇赋值必须相等；随后 common linear sheet `18K-55` 至少承担 `(e+1)/2` 层该 prime。把所有 odd/odd reused primes聚合后得到一个仅 `O(N)` 的全局 height budget `H_reuse | 18K-55 < 180N`。因此 source parity要节省 prime support，就必须支付极短 linear depth。本文仍允许这样的 linear divisors存在，因此不关闭 A2。

---

## 1. exact collision identity

已有

\[
\boxed{
55\mathscr B_W-K^2\mathscr D_W
=c_u^2L_S^2,}
\qquad
\boxed{L_S:=18K-55.}
\tag{1.1}
\]

固定 genuine odd prime `r`，假设

\[
r\mid\mathscr B_W,
\qquad
r\mid\mathscr D_W,
\]

以及 unit separation

\[
r\nmid55Kc_u.
\tag{1.2}
\]

记

\[
\boxed{a:=v_r(\mathscr B_W),}
\qquad
\boxed{d:=v_r(\mathscr D_W),}
\qquad
\boxed{\ell:=v_r(L_S).}
\tag{1.3}
\]

由 (1.1)：

\[
\boxed{
v_r(55\mathscr B_W-K^2\mathscr D_W)=2\ell.}
\tag{1.4}
\]

---

## 2. odd/odd reuse forces equal depth

现在假设同一 prime真的同时承担两份 source odd parity，即

\[
\boxed{a\equiv d\equiv1\pmod2.}
\tag{2.1}
\]

若

\[
a\ne d,
\]
则 (1.2) 下两个 LHS summands赋值不同，非阿基米德赋值给

\[
v_r(55\mathscr B_W-K^2\mathscr D_W)
=\min(a,d).
\]

右边由 (1.4) 为偶数，而 `min(a,d)` 是奇数，矛盾。

所以必须

\[
\boxed{a=d=:e,}
\tag{2.2}
\]

并且

\[
\boxed{e\text{ 为奇数}.}
\tag{2.3}
\]

这说明 two-source parity reuse本身已经强迫一个新的 equal-depth collision。

---

## 3. linear sheet pays at least half the odd depth

在 (2.2) 下，LHS 两项均有精确赋值 `e`。

如果它们没有额外 cancellation，则 (1.4) 会给

\[
2\ell=e,
\]
但左边为偶数、右边为奇数，不可能。

因此 LHS 必至少再加深一层：

\[
2\ell\ge e+1.
\]

所以

\[
\boxed{
\ell=v_r(18K-55)
\ge\frac{e+1}{2}.}
\tag{3.1}
\]

因为 `e` 为奇数，右边是整数。

等价地：

\[
\boxed{
r^{(e+1)/2}\mid18K-55.}
\tag{3.2}
\]

所以复用两份 odd parity的 depth不能只藏在两个高次 source forms中；至少一半必须显式出现在固定 linear prefix integer里。

---

## 4. short Archimedean height

endpoint 有

\[
0<K<10N.
\]

当前 `K` 巨大且正，因此 `18K-55>0`；粗界足够：

\[
\boxed{0<18K-55<180N.}
\tag{4.1}
\]

于是单个 reused prime满足

\[
\boxed{
r^{(e+1)/2}<180N.}
\tag{4.2}
\]

这把两个 source carriers中的奇赋值深度压回一个只有 `M+3` 位量级的 linear integer。

---

## 5. global reused-prime product

令 `E_reuse` 为所有满足以下条件的 genuine primes：

\[
r\equiv3\pmod4,
\]

\[
a_r:=v_r(\mathscr B_W)\text{ odd},
\qquad
d_r:=v_r(\mathscr D_W)\text{ odd}.
\]

§2 已证明

\[
a_r=d_r=:e_r.
\]

定义 weighted reuse product

\[
\boxed{
H_{\rm reuse}
:=\prod_{r\in E_{\rm reuse}}
r^{(e_r+1)/2}.}
\tag{5.1}
\]

逐 prime由 (3.2) 且 primes互素：

\[
\boxed{H_{\rm reuse}\mid18K-55.}
\tag{5.2}
\]

因此

\[
\boxed{H_{\rm reuse}<180N.}
\tag{5.3}
\]

写

\[
G_{\rm reuse}:=\prod r^{e_r},
\qquad
R_{\rm reuse}:=\prod r,
\]
则

\[
H_{\rm reuse}^2=G_{\rm reuse}R_{\rm reuse}.
\]
所以还得到

\[
\boxed{
G_{\rm reuse}R_{\rm reuse}
<(180N)^2.}
\tag{5.4}
\]

---

## 6. parity allocation dichotomy with depth cost

source side的两份 odd parity现在有严格二分：

### separate support

若 `B_W` 与 `D_W/2` 的 odd parity不能全部由共同 odd/odd primes承担，则至少需要 distinct inert support；这直接产生 prime-count/product surcharge。

### reused support

任何真正同时承担两边奇 parity的 prime都进入 `E_reuse`，并支付

\[
\boxed{r^{(e+1)/2}\mid18K-55.}
\]

所有这种 reuse的总成本受

\[
\boxed{H_{\rm reuse}<180N}
\]
控制。

所以“省 prime”与“省 linear depth”不能同时发生。

---

## 7. relation to serial pool

source parity collision gate 已证明 non-`3` reused prime满足

\[
r\nmid\omega,
\qquad
r\nmid2K-9,
\]
且不属于 genuine omega-height serial target pool。

所以 `H_reuse` 与 `Sigma_first/Sigma_double` 是 support-separated 的新 source object。后续可以把

\[
G_{\rm dbl}^3R_{\rm dbl}^2<1053TN^3
\]
和

\[
H_{\rm reuse}<180N
\]
同时计入 product budget，而不会重复计算同一 genuine moving prime。

本文仍不证明这些 independent supports的 combined lower bound足以超过 decimal height；A2 仍为 `待证`。

---

<a id="source-spontaneous-source-prefix-simple"></a>

> 整合来源：`spontaneous-source-prefix-simple.md`

# A2 source common simple branch 的 prefix-`e` lift 与 resultant no-go

> **依赖：** `spontaneous-source-common-integer.md`、`hensel.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文把 source prefix integer `D_src` 精确写成真实 endpoint defects `(H,e,M)`。结论是：对 genuine non-`3` source prime，`D_src` 关于 numerator defect `e` 永远是 unit-slope linear Hensel equation，因此每个 `(H,M)` 与每个 source depth `p^h` 只对应唯一 `e mod p^h`。另一方面 source→common integer gate `K_src(H,E,F)` 完全不含 `e`，所以消去 `e` 不会产生新的 residual polynomial。本文明确把“继续做 `Res_e(D_src,K_src)`”降级为 no-go；真正剩余的是唯一 `e` residue 与真实窄窗的 natural-representative synchronization，而不是新的局部 singularity。本文不宣称 A2 全局关闭。

---

## 1. 真实 endpoint defects

沿用

\[
F:=5^{M-1},
\qquad
E:=2^{M-1},
\qquad
10^{M-1}=EF.
\]

最危险 reflection endpoint 中

\[
\boxed{b_2=10^{M-1}+2^{M-1}H=E(F+H),}
\tag{1.1}
\]

\[
\boxed{a_2=10^{M-1}-e=EF-e.}
\tag{1.2}
\]

并且真实窄窗为

\[
0<H<F/19,
\qquad
0<e<EF/250.
\tag{1.3}
\]

---

## 2. `已严格完成`：`D_src` 的 exact defect form

reflection 中 `a_1=9`，故

\[
A_0=9\cdot10^{M-1}=9EF,
\qquad
C_0=\frac{9b_2}{2}=\frac{9E(F+H)}2.
\]

source prefix integer为

\[
D_{\rm src}=C_0^2-A_0a_2.
\]

代入 (1.1)–(1.2)：

\[
\begin{aligned}
D_{\rm src}
&=\frac{81E^2(F+H)^2}{4}
-9EF(EF-e)\\
&=\frac{9E^2}{4}
\left[9(F+H)^2-4F^2\right]
+9EF e.
\end{aligned}
\]

因此

\[
\boxed{
D_{\rm src}
=
\frac{9E^2}{4}
(5F^2+18FH+9H^2)
+9EF e.}
\tag{2.1}
\]

因为当前 `M` 很大，`E` 被 `2` 高次整除，所以右边当然为整数；对 odd source prime则只需把 `4` 视为 unit。

这与 normalized identity

\[
D_{\rm src}
=9\cdot10^{2M-2}(225x^2-y)
\]
完全一致。

---

## 3. `已严格完成`：source half-depth 对 `e` 永远 simple

固定 genuine non-`3` source excess prime

\[
p\equiv3\pmod4,
\qquad p\ne3,5.
\]

source separation保证 `p` 不进入 decimal powers，因此

\[
\boxed{p\nmid 9EF.}
\tag{3.1}
\]

由 (2.1)：

\[
\boxed{
\frac{\partial D_{\rm src}}{\partial e}=9EF,}
\tag{3.2}
\]

在 `Z_p` 中为单位。因此无论 source half-depth `h` 多大，条件

\[
p^h\mid D_{\rm src}
\]
都等价于唯一线性 residue：

\[
\boxed{
4Fe
\equiv
-E(5F^2+18FH+9H^2)
\pmod{p^h}.}
\tag{3.3}
\]

因为 `4F` 为单位，对每个固定 `(H,E,F)`：

\[
\boxed{
\text{there is exactly one }e\pmod{p^h}
\text{ satisfying the source prefix depth}.}
\tag{3.4}
\]

所以 `D_src` 本身不可能产生 singular `e`-Hensel tree，也不存在第二个 `e` phase。

---

## 4. 与 source→common integer gate 的变量分离

`spontaneous-source-common-integer.md` 定义

\[
\mathcal K_{\rm src}(H,E,F),
\]
并证明 genuine source/common first layer 必须满足

\[
p\mid\mathcal K_{\rm src}(H,E,F).
\]

关键是

\[
\boxed{
\frac{\partial\mathcal K_{\rm src}}{\partial e}=0.}
\tag{4.1}
\]

也就是说两个条件的变量职责完全分离：

\[
\boxed{
\begin{array}{c|c}
\text{object}&\text{controls}\\ \hline
\mathcal K_{\rm src}&(H,M)\text{ common gate}\\
D_{\rm src}&e\text{ 的唯一 source residue}
\end{array}}
\tag{4.2}
\]

source local second-order correction `phi` 又已经由 angle extra-lift唯一决定。因此 simple source/common branch没有任何未命名局部 phase剩余。

---

## 5. `审计 / no-go`：消去 `e` 不会产生新的 residual

把 `D_src` 看成 `e` 的一次多项式，把 `K_src` 看成 `e` 的常数多项式。resultant定义立即给

\[
\boxed{
\operatorname{Res}_e
(D_{\rm src},\mathcal K_{\rm src})
=
\mathcal K_{\rm src}.}
\tag{5.1}
\]

至多差一个按 resultant convention 选择的单位幂；这里 `deg_e D_src=1`，所以恰好就是一份 `K_src`。

因此继续尝试

\[
\gcd(D_{\rm src},\mathcal K_{\rm src})
\]
的纯多项式消元，**不会**像 denominator `R_q/R_f` 那样掉出新的 simple residual。原因不是计算尚未做够，而是 `e` 只存在于一个 unit-slope linear equation中。

这条 no-go 必须保留，避免后续 agent 重复做一个注定退化的 resultant。

---

## 6. 真正剩余的是 natural representative

对 fixed `(p,h,H,M)`，(3.3) 给出唯一 residue

\[
e\equiv e_0\pmod{p^h}.
\]

但真实 decimal endpoint还要求

\[
\boxed{0<e<EF/250.}
\tag{6.1}
\]

因此 simple source/common branch是否真实存在，已经精确变成：

1. `(H,M)` 命中 common gate `K_src=0 mod p` 及其 simple lift；
2. source depth给出的唯一 `e mod p^h` 是否有 representative落进 (6.1)；
3. 同时满足其余 exact endpoint shell / additive depth。

这不是一个新的局部 algebraic-singularity 问题，而是 decimal-orbit / natural-representative synchronization。

---

## 7. 更新后的 source simple frontier

结合前两份 source 文件，现在 source-supported common channel可以规范写成

\[
\boxed{
\begin{array}{l}
\text{(i) }\mathcal K_{\rm src}(H,E,F)\equiv0\pmod p,\\
\text{(ii) }4Fe\equiv-E(5F^2+18FH+9H^2)\pmod{p^h},\\
\text{(iii) }0<H<F/19,\quad0<e<EF/250.
\end{array}}
\tag{7.1}
\]

其中：

- singular common gate 已审计并死亡；
- `(ii)` 对 `e` 唯一且 simple；
- local source angle correction也唯一；
- 所以剩下的全部自由都集中在 **simple `(H,M)` common orbit + natural representative**。

下一步若继续 source channel，应直接攻击 (7.1) 的 representative/orbit；不应再做 `e`-resultant、source singular-prime 或局部 Legendre stacking。

---

<a id="source-spontaneous-source-primary-bridge"></a>

> 整合来源：`spontaneous-source-primary-bridge.md`

# A2 source primary 与 angle primitive carrier 的 exact integer bridge

> **依赖：** `spontaneous-prefix-eliminant.md`、`spontaneous-source-saturation-parity.md`、`spontaneous-source-prefix-simple.md`、`hensel.md`。
>
> **严格状态：**本文把 source Hensel linear form、source prefix half-depth `D_src` 与 spontaneous angle raw integer `O_sp` 放进同一条 exact integer identity。核心公式是
>
> \[
> 81\mathcal O_{\rm sp}=400T D_{\rm src}^2-81A^2\mathcal S_{\rm src}.
> \]
>
> 对 genuine non-`3` source prime，`v_p(S_src)=2h`，因此 source base `p^{2h}` 完整进入 angle carrier，且只有 `v_p(D_src)=h` 的 equal-depth cancellation能够产生 extra angle depth。这给 `spontaneous-source-saturation-parity.md` 一个更短的原始整数证明，并明确 extra depth 的唯一 algebraic来源。本文不排除该 equal-depth cancellation，也不关闭 A2。

---

## 1. 原始 decimal blocks

固定 reflection endpoint，记

\[
N:=10^M,
\qquad
T:=10^m,
\qquad
A:=a_2,
\qquad
B:=b_2,
\]

\[
Q:=B+2N.
\tag{1.1}
\]

`spontaneous-prefix-eliminant.md` 的 angle raw integer为

\[
\boxed{
\mathcal O_{\rm sp}
:=T\mathcal U_\Omega+2A^2Qb_3,}
\tag{1.2}
\]

其中

\[
\boxed{
\mathcal U_\Omega
=(45B^2-2AN)^2-A^2B(99B-4N).}
\tag{1.3}
\]

对 genuine odd prime，`O_sp` 与 `Omega_sp` / primitive `widehat(O)_sp` 只差固定 `2`-power和 odd units。

---

## 2. `已严格完成`：source Hensel line 的原始整数

source normalized variables为

\[
x=B/N,
\qquad
r_s=BT/b_3.
\]

因此

\[
\Phi_s=(99x-4)r_s-2x-4
\]
满足

\[
\begin{aligned}
Nb_3\Phi_s
&=TB(99B-4N)-2Bb_3-4Nb_3\\
&=TB(99B-4N)-2Qb_3.
\end{aligned}
\]

定义

\[
\boxed{
\mathcal S_{\rm src}
:=TB(99B-4N)-2Qb_3.}
\tag{2.1}
\]

则有 exact identity

\[
\boxed{
\mathcal S_{\rm src}=Nb_3\Phi_s.}
\tag{2.2}
\]

对 genuine source excess prime，`p` 与 `Nb_3` 分离，旧 source Hensel给

\[
p^{2h}\Vert\sigma,
\qquad
v_p(\Phi_s)=2h.
\]

所以

\[
\boxed{v_p(\mathcal S_{\rm src})=2h.}
\tag{2.3}
\]

这就是 source primary depth 的纯 integer representative。

---

## 3. source prefix defect正好是 angle square term

reflection 中

\[
A_0=9\cdot10^{M-1}=9N/10,
\qquad
C_0=9B/2,
\]

并定义

\[
D_{\rm src}:=C_0^2-A_0A.
\]

直接计算：

\[
D_{\rm src}
=\frac{81}{4}B^2-\frac9{10}AN.
\]

因此

\[
\boxed{
45B^2-2AN=\frac{20}{9}D_{\rm src}.}
\tag{3.1}
\]

这解释了 `U_Omega` 第一平方项为何正好测量 source half-depth，而不是一个新的独立 prefix polynomial。

---

## 4. `已严格完成`：angle raw integer 的 source bridge

从 (1.2)–(1.3)：

\[
\begin{aligned}
\mathcal O_{\rm sp}
={}&T(45B^2-2AN)^2\\
&-A^2\bigl[TB(99B-4N)-2Qb_3\bigr].
\end{aligned}
\]

使用 (2.1)：

\[
\boxed{
\mathcal O_{\rm sp}
=T(45B^2-2AN)^2-A^2\mathcal S_{\rm src}.}
\tag{4.1}
\]

再用 (3.1)，清去固定 denominator `9^2`：

\[
\boxed{
81\mathcal O_{\rm sp}
=400T D_{\rm src}^2-81A^2\mathcal S_{\rm src}.}
\tag{4.2}
\]

这是 source primary、prefix half-depth和 angle carrier之间的 exact integer bridge。

---

## 5. exact gcd / truncated valuation law

由 (4.2)，对任意 prime `p !=2,3,5` 且 `p∤AT`：

\[
\gcd(81\mathcal O_{\rm sp},\mathcal S_{\rm src})
=
\gcd(400T D_{\rm src}^2,\mathcal S_{\rm src})
\]
在 `p`-primary上给

\[
\boxed{
\min\{v_p(\mathcal O_{\rm sp}),v_p(\mathcal S_{\rm src})\}
=
\min\{2v_p(D_{\rm src}),v_p(\mathcal S_{\rm src})\}.}
\tag{5.1}
\]

现在固定 genuine source prime：

\[
v_p(\mathcal S_{\rm src})=2h,
\qquad
v_p(D_{\rm src})\ge h.
\]

于是

\[
\boxed{
\min\{v_p(\mathcal O_{\rm sp}),2h\}=2h.}
\tag{5.2}
\]

这直接恢复 source base primary完整进入 angle carrier的结论。

因为 primitive `widehat(O)_sp` 与 `O_sp` 只差固定 `2`-power，对 odd source prime同样有

\[
\boxed{
\min\{v_p(\widehat{\mathcal O}_{\rm sp}),2h\}=2h.}
\tag{5.3}
\]

---

## 6. extra angle depth 的唯一来源

bridge (4.2) 还给出更精确的 dichotomy。

### 6.1 strict half-depth

若

\[
v_p(D_{\rm src})>h,
\]
则第一平方项深度严格大于 `2h`，第二项精确为 `2h`。所以

\[
\boxed{
v_p(\widehat{\mathcal O}_{\rm sp})=2h.}
\tag{6.1}
\]

没有任何 extra angle depth。

### 6.2 equal-depth shell

只有

\[
\boxed{v_p(D_{\rm src})=h}
\tag{6.2}
\]
时两项都恰处在 `2h`，才可能继续 cancellation。

令

\[
D^\sharp:=D_{\rm src}/p^h,
\qquad
S^\sharp:=\mathcal S_{\rm src}/p^{2h}.
\]

则 extra lift至少一层的必要且充分 normalized condition为

\[
\boxed{
400T(D^\sharp)^2
\equiv81A^2S^\sharp\pmod p.}
\tag{6.3}
\]

这就是此前 `spontaneous-source-equal-depth.md` / `...-nogo.md` 的 normalized cancellation，用完全原始 decimal integers重写后的形式。

因此 source parity ledger可以规范分成

\[
\boxed{
2h\quad+\quad
v_p\!\left(400T(D^\sharp)^2-81A^2S^\sharp\right),}
\tag{6.4}
\]

第一部分严格偶数，第二部分才是真正 angle-over-source residual。

---

## 7. 对后续全局 parity 的意义

本文证明 source base depth之所以为偶，并不是抽象 Gaussian parity巧合，而来自 raw angle integer自身的

\[
\boxed{
\text{square prefix term}-\text{source primary term}.}
\]

结合 `spontaneous-source-depth-transfer.md`，现在 source primary在两侧的规范 ledger为：

\[
\boxed{
\begin{array}{c|c}
\text{angle side}&2h+\text{normalized equal-depth extra}\\
\text{additive/common side}&\min(v_p(C_{\rm src}),h)\text{ until half-depth saturation.}
\end{array}}
\]

因此后续真正未闭的 source parity不再是 base `p^{2h}`，而只有：

1. equal-depth angle extra；
2. `C_src` half-depth saturation后的 transverse allocation；
3. generic simple decimal-orbit synchronization。

继续追 source singular discriminant或 source-base Legendre character都不会增加信息。

---

<a id="source-spontaneous-source-reuse-cross-pair-asymmetry"></a>

> 整合来源：`spontaneous-source-reuse-cross-pair-asymmetry.md`

# A2 source parity reuse 上的 cross-pair asymmetry

> **依赖：** `spontaneous-source-reuse-cross-pair-length.md`、`spontaneous-residual-parity-doubling.md`、`spontaneous-source-parity-collision-gate.md`。
>
> **严格状态：**`O/J` cross-pair 在 source-reuse sheet上被投影成两个 pure-length octics。本文审计另一个建议 cross-pair `T/O`，证明 first layer存在结构性自由：source reused prime是 noncentral且与 `B` 分离，而 raw additive carrier `Theta_dec` 对 third numerator `a_3` 是 unit-coefficient线性式，因此任意 prefix/angle first-layer state都唯一恢复一个 `a_3 mod r`。所以 `T/O` first layer不能再作为独立 prefix obstruction收费；真正新增信息必须来自真实 `a_3` digit window或更高 p-adic digit。本文是 no-double-count 审计，不关闭 A2。

---

## 1. source reused prime is noncentral and `B`-free

固定 genuine odd/odd source parity reused inert prime `r`。已有

\[
\boxed{r\mid18K-55,}
\tag{1.1}

并且 source parity collision theorem证明

\[
\boxed{r\nmid(2K-9)\omega.}
\tag{1.2}

另一方面 deep-even denominator为

\[
B=2^{M+m+1}c_ug.
\]

source-discriminant overlap给 genuine reused prime与 `c_u,g` 分离，因此

\[
\boxed{r\nmid B.}
\tag{1.3}

所以

\[
\boxed{2B^2(2K-9)\text{ 是模 }r\text{ 的单位}.}
\tag{1.4}

---

## 2. raw additive carrier is linear in `a_3`

height parity ledger给

\[
\boxed{
\Theta_{\rm dec}
=T\left[B^2(K^2-18K+55)-Q^2N_0\right]
-2B^2(2K-9)a_3.}
\tag{2.1}

若 residual

\[
r\mid T^\circ,
\]
则其 raw parent当然满足

\[
\boxed{r\mid\Theta_{\rm dec}.}
\tag{2.2}

由 (1.4)，(2.1) 对 `a_3` 是非退化的一次方程。因此 (2.2) 对任意已固定的 prefix state `(B,N)` 唯一恢复

\[
\boxed{
a_3
\equiv
\frac{T\left[B^2(K^2-18K+55)-Q^2N_0\right]}
{2B^2(2K-9)}
\pmod r.}
\tag{2.3}

不存在第二个 branch，也不存在 first-layer discriminant。

---

## 3. angle/source conditions do not remove this linear freedom

若同一 reused prime还进入某一 angle sheet `O_±`，source discriminant与 angle equation确实给 third-free必要 gate

\[
49\mathcal U_\Omega^2-220A^4Q^4=0\pmod r.
\tag{3.1}

再加 source collision

\[
18K-55=0
\]
后，(3.1) 是 `(B,N)` 上的一条 algebraic curve。

但它不含 `a_3`。因此在该 curve上的每个 genuine first-layer prefix point，(2.3) 仍然唯一给出一个 `a_3 mod r`。

所以：

\[
\boxed{
\text{source reuse}+O_\pm+T^\circ
\text{ 的 first layer保留一维 prefix freedom，且 }a_3\text{ 仅被唯一恢复}.}
\tag{3.2}

这与 `O/J` 情形完全不同：`J_H` 本身 pure-prefix，因此 `J_H=0` 与 (3.1) 两条 prefix equations对 `B` 消元后产生 pure-length octics。

---

## 4. cross-pair asymmetry

在 source odd/odd reuse sheet上：

### `J / angle`

\[
J_H=0,
\qquad
O_\pm=0
\]
投影到

\[
\boxed{\Phi_1(10^M)\Phi_2(10^M)=0\pmod r.}
\tag{4.1}

prefix continuous freedom消失。

### `T / angle`

\[
\Theta_{\rm dec}=0,
\qquad
O_\pm=0
\]
只给 angle prefix curve加唯一 `a_3` recovery (2.3)，不会生成纯 `N` first-layer resultant。

因此

\[
\boxed{
\text{两个 cross-pairs 在 source-reuse sheet上算术强度不对称}.}
\tag{4.2}

---

## 5. correct next target for the `T/O` side

由于 first layer的 `a_3 mod r` 总可唯一恢复，后续若继续 `T/O` overlap，不应再做普通 resultant/discriminant。真正可新增的输入只有：

1. 真实 third numerator defect
   \[
   a_3=T+h_3,
   \qquad0<h_3<T/250;
   \]
2. decimal exponent `m`；
3. `p^2` 以上要求恢复的 `a_3` residue必须与该 short digit interval相交。

所以 `T/O` 剩余问题属于 short-digit / multiplicative-orbit synchronization，而非 first-layer local geometry。

A2 仍为 `待证`。

---

<a id="source-spontaneous-source-reuse-cross-pair-fixed67"></a>

> 整合来源：`spontaneous-source-reuse-cross-pair-fixed67.md`

# A2 source-reuse `O/J` cross-pair 的 fixed `67` defect templates

> **依赖：** `spontaneous-source-reuse-cross-pair-length.md`、`endpoint-lattice.md` 的 defect coordinates。
>
> **严格状态：**pure-length projection的唯一 surviving repeated projection prime `67` 实际只有两个 simple full states。本文把它们代回真实 numerator/denominator defect，得到 `M=33t`, `e=10 mod67` 与四个 `(t mod2,B,H)` templates。所有模板仍局部可行，因此 `67` 被严格降级为 finite fixed simple templates，而非 singular Hensel exception。本文不排除这些 templates 的全局 lift，故不关闭 A2。

---

## 1. decimal length phase

cross-pair audit给

\[
\boxed{N=10^M\equiv1\pmod{67}.}
\tag{1.1}

直接计算

\[
\boxed{\operatorname{ord}_{67}(10)=33,}
\tag{1.2}

所以

\[
\boxed{M=33t,\qquad t\ge1.}
\tag{1.3}

---

## 2. numerator defect

source collision linear gate给

\[
18K-55=0\pmod{67}.
\]

因此

\[
\boxed{K\equiv44\pmod{67}.}
\tag{2.1}

由

\[
K=9N+10A
\]
和 `N=1`：

\[
\boxed{A\equiv37\pmod{67}.}
\tag{2.2}

endpoint numerator defect为

\[
A=N/10-e.
\]

因为

\[
10^{-1}\equiv47\pmod{67},
\]
得到

\[
\boxed{e\equiv47-37\equiv10\pmod{67}.}
\tag{2.3}

该 residue与 `0<e<N/2500` 并不冲突，因此不能删除 fixed `67`。

---

## 3. denominator phase

endpoint denominator defect为

\[
\boxed{B=N/10+2^{M-1}H.}
\tag{3.1}

cross-pair full system的两个 simple states为

\[
\boxed{B\equiv53,37\pmod{67}.}
\tag{3.2}

又

\[
2^{33}\equiv-1\pmod{67},
\qquad2^{-1}\equiv34\pmod{67}.
\]

所以对 `M=33t`：

\[
\boxed{
2^{M-1}
\equiv34(-1)^t
\equiv
\begin{cases}
33,&t\text{ odd},\\
34,&t\text{ even}
\end{cases}
\pmod{67}.}
\tag{3.3}

---

## 4. four exact templates

由 `N/10=47 mod67`，(3.1)--(3.3) 给

\[
\boxed{
\begin{array}{c|c|c}
t\bmod2&B\bmod67&H\bmod67\\ \hline
0&53&12\\
0&37&47\\
1&53&55\\
1&37&20
\end{array}}
\tag{4.1}

并统一有

\[
\boxed{e\equiv10\pmod{67}.}
\tag{4.2}

这四个 states的 parent `(B,N)` Jacobian均为 unit，因此各自若继续，只能沿唯一 simple local lift，不会形成 singular branching。

---

## 5. strict classification

fixed `67` 现在应分类为

\[
\boxed{
\text{four simple decimal-defect templates indexed by }t\bmod2,}
\]

而非

- resultant bad coefficient；
- repeated full-system root；
- singular Hensel tree。

后续若要删除 `67`，必须把表 (4.1) 与 source factor allocation、third defect或更高 decimal exponent lift联立；继续做 discriminant分析不会增加信息。

A2 仍为 `待证`。

---

<a id="source-spontaneous-source-reuse-cross-pair-length"></a>

> 整合来源：`spontaneous-source-reuse-cross-pair-length.md`

# A2 source parity reuse 与 `O/J` cross-pair 的 pure-length projection

> **依赖：** `spontaneous-source-parity-collision-gate.md`、`source-discriminant.md`、`spontaneous-height-parity-ledger.md`、`spontaneous-residual-parity-doubling.md`。
>
> **严格状态：**本文审计 source odd/odd parity reused prime进一步命中 angle/additive cross-pair `O_± / J_H` 的必要条件。source collision先固定 `18K-55=0`，source discriminant再把 third denominator从 angle sheet消掉，得到 third-free平方 gate。与 `J_H=0` 对 `B` 消元后，resultant精确分成两个固定八次 pure-length polynomials `Phi_1(N),Phi_2(N)`；真实 cross-pair overlap只能命中 `Phi_1(10^M)Phi_2(10^M)=0 mod r`。随后完整审计 projection 的 repeated roots：所有 genuine singular candidates除 fixed `67` 的两个 simple full states外都为 boundary、非 decimal orbit或在 `p^2` linearization时死亡。因此该 cross-pair没有 hidden singular Hensel tree，只剩 simple decimal-exponent synchronization。本文不排除 simple roots，故不关闭 A2。

---

## 1. source-reuse equations

固定 genuine source odd/odd reused inert prime `r`，处在 unit-separated sector。已有

\[
\boxed{r\mid18K-55,}
\tag{1.1}

以及

\[
\boxed{r\mid\mathscr D_W=55z^2-49c_u^2.}
\tag{1.2}

source ratio为

\[
\frac z{c_u}=\frac{TQ}{b_3}.
\]

因此 (1.2) 乘去单位分母给

\[
\boxed{55T^2Q^2-49b_3^2\equiv0\pmod r.}
\tag{1.3}

另一方面 angle sheets为

\[
\mathcal O_\pm=T\mathcal U_\Omega\pm2A^2Qb_3,
\]

\[
\mathcal U_\Omega=(45B^2-2AN)^2-A^2B(99B-4N).
\]

若 `r|O_±`，平方并使用 (1.3)：

\[
T^2\mathcal U_\Omega^2
=4A^4Q^2b_3^2
\equiv\frac{220}{49}T^2A^4Q^4.
\]

因为 `r` 与 `7T` 分离，在 genuine reused sector得到 third-free gate

\[
\boxed{
\mathcal X_{OJ}
:=49\mathcal U_\Omega^2-220A^4Q^4
\equiv0\pmod r.}
\tag{1.4}

该 gate同时覆盖 `O_+` 与 `O_-`；此处只作必要 projection，不把平方后的额外 roots误当成充分条件。

---

## 2. impose the source collision linear sheet

由 (1.1)：

\[
K=9N+10A\equiv\frac{55}{18}\pmod r.
\]

在 polynomial elimination中因此代入

\[
\boxed{A=\frac{55-162N}{180}.}
\tag{2.1}

additive height companion为

\[
\boxed{
\mathcal J_H
=B^2(5K^2-36K+55)-Q^2N_0,}
\tag{2.2}

\[
Q=B+2N,
\qquad
N_0=\left(\frac{9B}{2}\right)^2+A^2.
\]

若 cross-pair residual `J^circ` 被 `r` 整除，则 raw `J_H` 当然也被 `r` 整除。因此 genuine `O/J` cross-pair overlap必须满足

\[
\mathcal J_H=0,
\qquad
\mathcal X_{OJ}=0
\pmod r
\]
在 (2.1) 的 linear sheet上。

---

## 3. exact resultant factorization

把 (2.1) 代入 `J_H,X_OJ` 并清去有理分母，得到整数 polynomials

\[
J_*(B,N),\qquad X_*(B,N).
\]

直接对 `B` 求 resultant：

\[
\boxed{
\operatorname{Res}_B(J_*,X_*)
=C\,N^8(162N-55)^8\Phi_1(N)\Phi_2(N),}
\tag{3.1}

其中

\[
C=2^{28}3^{38}5^{16}7^4.
\tag{3.2}

两个 primitive octics为

\[
\boxed{\begin{aligned}
\Phi_1(N)={}&
152356364573249030359104N^8
-4097103068832023796480N^7\\
&+31384125262928360244960N^6
+18803025591118547565600N^5\\
&+2075376150266128766100N^4
+1943181330646900509000N^3\\
&+675406005318781110000N^2
-26358539660104162500N\\
&+244063541277015625,
\end{aligned}}
\tag{3.3}

\[
\boxed{\begin{aligned}
\Phi_2(N)={}&
40095472108377374070575040576N^8
+30284848824599488024870272000N^7\\
&+13738744691885641990863011040N^6
+4454752959867937104210016800N^5\\
&+1029832152338324301433146900N^4
+174239977384696722571611000N^3\\
&+19756759606772961743190000N^2
+621005812442557377412500N\\
&+5763793275102412515625.
\end{aligned}}
\tag{3.4}

`r` 为 odd/odd source reused prime。此前 `r=7` 不能承担 `D_W` odd parity，且 genuine sector排除 `2,3,5`，所以 `r∤C`。

`N=0` 为 decimal boundary；`162N-55=0` 等价于 `A=0` boundary。故 genuine overlap必要满足

\[
\boxed{
r\mid\Phi_1(N)\Phi_2(N).}
\tag{3.5}

真实 `N=10^M` 给 pure-length orbit

\[
\boxed{
r\mid\Phi_1(10^M)\Phi_2(10^M).}
\tag{3.6}

---

## 4. real-root audit: this is genuinely modular

令

\[
t:=162N-55.
\]

将 `N=(t+55)/162` 代入两个 octics并取 primitive numerator，得到的两个 degree-8 polynomials所有 coefficients均严格为正：

\[
\begin{aligned}
\widetilde\Phi_1(t)={}&104060401t^8+45333244000t^7+9201937926610t^6\\
&+1180976579420000t^5+105532829497813025t^4\\
&+6674082653480000000t^3+294411604662340000000t^2\\
&+8234566912000000000000t+107049369856000000000000,
\end{aligned}
\tag{4.1}

\[
\begin{aligned}
\widetilde\Phi_2(t)={}&3042830185641t^8+1711170805406040t^7\\
&+428435775972099610t^6+62469041502406486200t^5\\
&+5807836796958184695025t^4+352850034535729704600000t^3\\
&+13688106402633420340000000t^2\\
&+309923322789674880000000000t\\
&+3130230623959296000000000000.
\end{aligned}
\tag{4.2}

真实 endpoint有 `t=162N-55>0`，所以两者在实数上都严格为正。cross-pair contact只能来自 modular wrapping，不存在 real near-root解释。

---

## 5. repeated-root candidate audit

对 `Phi_1,Phi_2` 的 discriminants做 exact factorization，再限制到 source-reuse compatibility

\[
r\equiv3\pmod4,
\qquad
\left(\frac{55}{r}\right)=1,
\]
且排除 `2,3,5,7,11` unit exceptions后，finite repeated-root候选只需审计

\[
\boxed{19,23,67,367,8971,102251,630451,136776907.}
\tag{5.1}

逐一结果如下。

### `19`

唯一 full `J_*=X_*=0` state在 repeated `N=15` 上给

\[
B=0\pmod{19}.
\]

但 `B=2^{M+m+1}c_ug`，而 source discriminant与 `c_u,g` 的 non-fixed support分离，所以 reused `19` 必有 `19∤B`。该 state nongenuine。

### `23`

projection gcd为

\[
N^2+3N+11,
\]
在 `F_23` 无根，因此没有 finite repeated state。

### `367`

唯一 repeated root为

\[
N=0,
\]
是 boundary。

### `136776907`

唯一 finite repeated root为

\[
N=93550173\pmod{136776907}.
\]

而

\[
\operatorname{ord}_{136776907}(10)=7598717,
\]
且

\[
93550173^{7598717}\not\equiv1\pmod{136776907}.
\]

所以该 root不属于 decimal subgroup `〈10〉`，真实 `N=10^M` 永远不会命中。

---

## 6. the three genuine singular projection states die at `p^2`

剩余 singular candidates：

\[
8971,\qquad102251,\qquad630451.
\]

它们各自唯一的 full mod-`p` state为

\[
\boxed{(p,N,B)=(8971,8743,8433),}
\tag{6.1}

\[
\boxed{(102251,90859,35831),}
\tag{6.2}

\[
\boxed{(630451,110422,242244).}
\tag{6.3}

记 system

\[
F_1=J_*,\qquad F_2=X_*.
\]

在上述三个状态，Jacobian `d(F_1,F_2)/d(B,N)` 模 `p` 都 rank `1`。写

\[
B=B_0+pB_1,
\qquad
N=N_0+pN_1.
\]

除以 `p` 后的 augmented linear systems分别为

\[
\begin{array}{c|c}
p&(F_B,F_N\mid-F/p)\\ \hline
8971&(5124,6911\mid3110),\ (7124,6240\mid5864)\\
102251&(53480,77070\mid90010),\ (18723,47191\mid56760)\\
630451&(143149,160161\mid311616),\ (279823,277602\mid522614).
\end{array}
\tag{6.4}

逐个都有

\[
\boxed{
\operatorname{rank}(J)=1,
\qquad
\operatorname{rank}(J|b)=2.}
\tag{6.5}

因此三个 singular states全部无法 lift 到 `p^2`。

---

## 7. fixed `67` is simple, not singular

`p=67` 的 repeated projection root为

\[
N=1.
\]

full system有两个 states：

\[
\boxed{(B,N)=(53,1),(37,1)\pmod{67}.}
\tag{7.1}

对应 Jacobian determinants为

\[
\boxed{57,46\pmod{67},}
\tag{7.2}

均非零。

所以 `67` 只是两个 ordinary simple Hensel templates。它不能被本文局部排除，但不产生 singular branching。

---

## 8. strict conclusion

source odd/odd parity reused prime若进一步命中 `O/J` cross pair，则必须进入

\[
\boxed{\Phi_1(10^M)\Phi_2(10^M)=0\pmod r.}
\]

该 pure-length projection：

- 在真实正 endpoint无 real roots；
- 所有 genuine singular decimal candidates均在 boundary、subgroup filter或第一次 `p^2` lifting时消失；
- fixed `67` 只留下两个 simple templates；
- 其余 surviving roots全部属于 simple moving decimal synchronization。

所以 cross-pair overlap不再拥有 prefix/third continuous freedom，也没有 hidden singular Hensel tree。后续若要关闭它，应该研究 `10^M` 在 `Phi_1,Phi_2` simple roots上的 multiplicative orbit或 natural height，而不应继续做 discriminant singularity。

A2 仍为 `待证`。

---

<a id="source-spontaneous-source-saturation-parity"></a>

> 整合来源：`spontaneous-source-saturation-parity.md`

# A2 source saturation 对 angle parity 永远是偶深度

> **依赖：** `hensel.md`、`spontaneous-angle.md`、`spontaneous-angle-overlap-depth.md`、`spontaneous-source-equal-depth-nogo.md`。
>
> **严格状态：**本文澄清 source excess 在 angle primitive carrier 中的 parity bookkeeping。对真正 source inert prime，source integer `sigma` 的完整 `p^{2h}` primary part总是完整进入 `E_1` / angle carrier，因此 source-supported depth本身严格为偶数。equal-depth cancellation 若产生奇 valuation，奇的部分必来自超出 `v_p(sigma)=2h` 的 extra angle depth，而不是 source content 本身。本文不证明该 extra depth 必进入 additive common gcd，因此不是 A2 closure；它只把 source base parity 从开放列表中删除。

---

## 1. exact gcd identity

旧 second-angle integer 为

\[
\boxed{
E_1=5^\lambda L_0^2-2c_u\sigma a_2^2.}
\tag{1.1}

对任意整数 `sigma`，直接使用

\[
\gcd(X-Y,Y)=\gcd(X,Y)
\]
得到

\[
\boxed{
\gcd(E_1,\sigma)
=
\gcd(5^\lambda L_0^2,\sigma).}
\tag{1.2}

这条恒等式不需要 source Hensel 假设。

---

## 2. source inert prime 的完整 `sigma` primary part全部进入 `E_1`

固定 genuine source excess inert prime

\[
p\equiv3\pmod4,
\qquad
p^{2h}\Vert\sigma,
\qquad h\ge1.
\]

旧 source separation 给

\[
p\nmid 10c_u a_2,
\tag{2.1}
\]
而双 Hensel resultant 已证明

\[
\boxed{v_p(L_0)\ge h.}
\tag{2.2}

因为 `p != 5`，(1.2) 在该 prime 上给

\[
\begin{aligned}
v_p(\gcd(E_1,\sigma))
&=\min\{2v_p(L_0),2h\}\\
&=2h.
\end{aligned}
\]

因此

\[
\boxed{
\min\{v_p(E_1),v_p(\sigma)\}=2h,}
\tag{2.3}

特别地

\[
\boxed{p^{2h}\mid E_1.}
\tag{2.4}

所以 source primary part不是“至少一半深度”进入 angle integer；**完整的 source exponent `2h` 都进入，而且是偶深度。**

---

## 3. angle primitive carrier 有相同局部赋值

`spontaneous-angle.md` 有 exact rational identity

\[
\frac{E_1}{\Sigma a_2^2}
=
\frac{\Omega_{\rm sp}}
{y^2(x+2)F_f},
\]
其中

\[
\Sigma=c_Q^2qf.
\]

真正 source excess prime与 denominator/source-content 分离，因此

\[
p\nmid \Sigma a_2y(x+2)F_f.
\tag{3.1}

故

\[
\boxed{v_p(E_1)=v_p(\Omega_{\rm sp}).}
\tag{3.2}

`spontaneous-angle-parity.md` 的 primitive integer `widehat(O)_sp` 与 `Omega_sp` 也只差 genuine p-adic unit与固定 2-power，所以

\[
\boxed{
v_p(\widehat{\mathcal O}_{\rm sp})
=v_p(E_1).}
\tag{3.3}

结合 (2.3)：

\[
\boxed{
\min\{v_p(\widehat{\mathcal O}_{\rm sp}),2h\}=2h.}
\tag{3.4}

---

## 4. source-saturated residual depth

定义局部 extra angle depth

\[
\boxed{
e_p^{\rm extra}
:=v_p(\widehat{\mathcal O}_{\rm sp})-2h
\ge0.}
\tag{4.1}

因为 `2h` 为偶数：

\[
\boxed{
v_p(\widehat{\mathcal O}_{\rm sp})
\equiv e_p^{\rm extra}\pmod2.}
\tag{4.2}

所以 source primary part本身对 angle `mod 4` parity严格中性；所有奇 parity 都来自超出完整 source exponent 的 extra depth。

更具体地：

- `v_p(d)>h` 时，`spontaneous-angle-overlap-depth.md` 已证明
  \[
  v_p(\widehat O_{\rm sp})=2h,
  \]
  所以 `e_p^extra=0`；
- `v_p(d)=h` 但 normalized angle cancellation失败时同样 `e_p^extra=0`；
- 只有 `spontaneous-source-equal-depth-nogo.md` 的 simple second-order correction成立时，才可能
  \[
  e_p^{\rm extra}>0.
  \]

因此 source pool 的规范 parity decomposition 是

\[
\boxed{
\underbrace{2h}_{\text{source saturation, even}}
+
\underbrace{e_p^{\rm extra}}_{\text{angle-over-source residual}}.}
\tag{4.3}

---

## 5. `审计`：不能把 extra depth再称为“source parity”

此前 `G_sp mod 4` residual quotient 的 prime-source bookkeeping 中，若一个 source prime满足

\[
v_p(\widehat O_{\rm sp})=2h+1
\]
可能被口头描述成“source pool 提供一份 odd inert parity”。(4.3) 说明这种说法会混淆两个层次：

- `p^{2h}` 是原 source integer `sigma` 已有的完整 primary content，严格偶深；
- 多出来的 `p` 已经是 angle equation 在 source primary饱和后的**额外接触**。

因此后续 global parity ledger 应把 source inert primary先完整饱和，再研究 extra quotient。source base contribution永远为 `1 mod 4`。

形式上，若只取 source inert primary square

\[
S_{\rm src}:=
\prod_{p\in\mathcal S_{\rm src}}p^{2h_p},
\]
则

\[
\boxed{S_{\rm src}\equiv1\pmod4.}
\tag{5.1}

从 `widehat(O)_sp` 中约去这些完整 source powers不会改变全局 `3 mod 4` orientation。

---

## 6. 对 parity 闭环的更新

本文并没有排除

\[
e_p^{\rm extra}\equiv1\pmod2.
\]
`spontaneous-source-equal-depth-nogo.md` 恰恰证明局部 source geometry允许这种 extra lift。

但开放问题现在应准确表述为：

\[
\boxed{
\text{source-saturated angle residual 是否能在没有 additive common contact 时保留 odd extra depth？}}
\tag{6.1}

而不是“source excess 本身是否贡献奇 parity”。后者已经严格回答：**不会。**

下一步必须把 `e_p^extra` 与 source 外部对象联立，最自然的是

\[
\widehat{\mathcal T}_2,
\quad
G_{\rm sp},
\quad
D_{\rm src}\text{ 的 natural representative},
\quad
\text{或 global Gaussian allocation}.
\]

这一重新分类删除了 source base-depth 的假自由度，但不把 extra angle-over-source residual错误地宣称为已关闭。

---

<a id="source-spontaneous-source-sheet-collision"></a>

> 整合来源：`spontaneous-source-sheet-collision.md`

# A2 source→common 的共轭 square-sheet collision

> **依赖：** `spontaneous-source-numerator-length.md`、`spontaneous-source-common-gate.md`。
>
> **严格状态：**source first layer满足 `r^2=y`，真实 sheet为 `r=15x`。`spontaneous-source-numerator-length.md` 把 `C_src` 分成 `E+120rO`，因此 pure numerator/length residual正是两个共轭 source sheets 的乘积。本文审计两个 sheet同时命中 `C_src=0` 的 collision locus：它降成一个固定 quartic；在真实 numerator interval没有实根，且 genuine non-`3` inert singular Hensel tree为空。simple modular sheet-collisions仍可能存在，因此本文不宣称 A2 closure。

---

## 1. 两个 source square sheets

source first-layer relation为

\[
225x^2=y.
\]

令

\[
\boxed{r:=15x,\qquad r^2=y.}
\tag{1.1}
\]

已有 exact even/odd decomposition

\[
\boxed{
5625\mathcal C_{\rm src}(x,\tau)
=\mathcal E(y,\tau)+120r\mathcal O(y,\tau),}
\tag{1.2}
\]

其中

\[
\begin{aligned}
\mathcal E={}&11000\tau^2y+9900000\tau^2
+84609\tau y^2-3240000\tau y-29160000\tau\\
&-19404y^3-10836y^2+1474200y,
\end{aligned}
\tag{1.3}
\]

\[
\mathcal O=
5500\tau^2-2691\tau y-16200\tau
+296y^2+1764y-8100.
\tag{1.4}
\]

在共轭 sheet `r -> -r`，即 `x -> -x`：

\[
\boxed{
5625\mathcal C_{\rm src}(-x,\tau)
=\mathcal E-120r\mathcal O.}
\tag{1.5}
\]

所以

\[
\boxed{
\mathcal R_{\rm src}^{(y)}
=5625^2\mathcal C_{\rm src}(x,\tau)
\mathcal C_{\rm src}(-x,\tau)
}
\tag{1.6}
\]

在 quotient ring `225x^2-y=0` 中精确成立。这就是此前

\[
\mathcal R_{\rm src}^{(y)}=\mathcal E^2-14400y\mathcal O^2
\]
的几何意义。

---

## 2. 双-sheet collision 等价于 `E=O=0`

对 genuine odd source prime，`2,3,5,r` 都是单位。若同时

\[
p\mid C_{\rm src}(x,\tau),
\qquad
p\mid C_{\rm src}(-x,\tau),
\]
则由 (1.2)、(1.5)：

\[
\boxed{
p\mid\mathcal E,\qquad p\mid\mathcal O.}
\tag{2.1}
\]

反向也显然成立。因此两个 square sheets 的 first-layer collision精确由 `(E,O)` 的平面交控制。

---

## 3. `已严格完成`：collision消成一个固定 quartic

对 `tau` 求 resultant：

\[
\boxed{
\operatorname{Res}_{\tau}(\mathcal E,\mathcal O)
=-550000(y+9)^2\mathcal Q_{\rm sheet}(y),}
\tag{3.1}
\]

其中

\[
\boxed{
\begin{aligned}
\mathcal Q_{\rm sheet}(y)
={}&2461063649y^4+234628417800y^3\\
&+4390818840000y^2+17723448000000y\\
&-144342000000000.
\end{aligned}}
\tag{3.2}
\]

反向消去 `y` 也得到固定 decimal-length quartic：

\[
\boxed{
\operatorname{Res}_{y}(\mathcal E,\mathcal O)
=-1000000\tau^2\mathcal Q_{\tau}(\tau),}
\tag{3.3}
\]

\[
\boxed{
\begin{aligned}
\mathcal Q_{\tau}(	au)
={}&7444717538225\tau^4
+119322760549410\tau^3\\
&+292869540803250\tau^2
+743568561885024\tau\\
&-87085495164087.
\end{aligned}}
\tag{3.4}
\]

所以双-sheet collision没有新的 source ratio自由度；它是固定 `(y,tau)` algebraic intersection。

---

## 4. `y=-9` 因子不属于 genuine non-3 inert decimal collision

在 `y=-9`：

\[
\boxed{
\mathcal E=81\tau(121000\tau+84609),}
\tag{4.1}
\]

\[
\boxed{
\mathcal O=11\tau(500\tau+729).}
\tag{4.2}
\]

两个非零线性 factors 的 resultant为

\[
\boxed{45904500=2^2\cdot3^2\cdot5^3\cdot101^2.}
\tag{4.3}
\]

因此对 genuine non-`3` inert prime，两个式子共同为零只能来自

\[
\tau=0,
\]
但真实

\[
\tau=10^{-M}
\]
永远是单位。故 (3.1) 的 `(y+9)^2` 是非 decimal boundary，不属于本文的真实 collision。

---

## 5. 真实 endpoint interval 没有 Archimedean collision

真实 numerator phase满足

\[
249/250<y<1.
\]

`Q_sheet` 在正半轴严格递增，因为 derivative的全部 coefficient为正：

\[
\mathcal Q_{\rm sheet}'(y)>0
\qquad(y>0).
\tag{5.1}
\]

而

\[
\boxed{
\mathcal Q_{\rm sheet}(1)=-121990643678551<0.}
\tag{5.2}
\]

因此整个真实 interval上

\[
\boxed{
\mathcal Q_{\rm sheet}(y)<0.}
\tag{5.3}
\]

没有实数 sheet collision；任何 collision只能来自 modular wrapping。

---

## 6. singular bad-prime set

quartic的整数判别式为

\[
\boxed{
\operatorname{Disc}(\mathcal Q_{\rm sheet})
= -2^{32}3^{32}5^{25}101^7\cdot113\cdot7437536446892971.}
\tag{6.1}
\]

其中

\[
113\equiv1\pmod4,
\qquad
101\equiv1\pmod4,
\]
且

\[
\boxed{7437536446892971\equiv3\pmod4}
\tag{6.2}
\]
为素数。

另外 quartic leading coefficient

\[
2461063649=11^2\cdot1609\cdot12641,
\]
其中 `1609,12641` 都为 `1 mod4`。resultant content `550000` 还含一份 `11`。

所以 genuine non-`3` inert singular/degree-drop audit只需

\[
\boxed{p=11,\qquad p=7437536446892971.}
\tag{6.3}
\]

---

## 7. `p=11`：唯一 singular point是 `tau=0` boundary

完整枚举 `F_11^2` 中 `(E,O)=(0,0)` 得

\[
\boxed{
(y,\tau,J)=
(2,0,0),\quad(3,3,6),\quad(5,9,1),}
\tag{7.1}
\]

其中

\[
J:=\det\frac{\partial(\mathcal E,\mathcal O)}{\partial(y,\tau)}.
\]

唯一 singular intersection `(2,0)` 满足 `tau=0`，不是 decimal phase；其余两点 Jacobian均为单位。因此

\[
\boxed{p=11\text{ 没有 genuine singular sheet-collision branch}.}
\tag{7.2}
\]

simple `11` collision states本身没有被本文排除。

---

## 8. 大 inert singular prime不能升到 `p^2`

令

\[
\boxed{p=7437536446892971.}
\]

此时

\[
\gcd(\mathcal Q_{\rm sheet},\mathcal Q_{\rm sheet}')
=y+2367909658823161
\pmod p,
\]
所以唯一 repeated `y` residue为

\[
\boxed{y_0=5069626788069810.}
\tag{8.1}
\]

代回 `(E,O)`，共同 `tau` root唯一：

\[
\boxed{\tau_0=1327194327136915.}
\tag{8.2}
\]

这是 finite unit state，并且 `y_0` 本身是模 `p` 的平方，所以不能靠 source square-sheet condition直接排除。

在该点，Jacobian两行模 `p` 为

\[
(4769546899604225,\ 5300490912652323),
\]

\[
(2429430622649786,\ 4767246607889802).
\tag{8.3}
\]

第二行是第一行的

\[
\lambda=6415545761503029
\]
倍，因此 rank为 `1`。

取最小非负 representatives，normalized carries为

\[
\frac{\mathcal E(y_0,\tau_0)}p
\equiv1149464242486028,
\]

\[
\frac{\mathcal O(y_0,\tau_0)}p
\equiv2576181903398455
\pmod p.
\tag{8.4}
\]

若存在 `p^2` lift，增广线性化必须满足同一 row relation。但 compatibility residual为

\[
\boxed{
\lambda\cdot1149464242486028
-2576181903398455
\equiv762004648349653\not\equiv0\pmod p.}
\tag{8.5}
\]

因此

\[
\boxed{
\text{该唯一 genuine singular sheet collision无 }p^2\text{ lift}.}
\tag{8.6}
\]

---

## 9. 结论：共轭 sheet只留下 simple fixed-quartic synchronization

综合 §§6–8：

\[
\boxed{
\text{source conjugate-sheet collision不存在 surviving singular Hensel tree}.}
\tag{9.1}
\]

所以对 genuine source prime，如果

\[
p\nmid\mathcal Q_{\rm sheet}(y),
\]
共轭 gate `C_src(-x,tau)` 为单位，于是由 (1.6)：

\[
\boxed{
v_p(\mathcal R_{\rm src}^{(y)})
=v_p(\mathcal C_{\rm src}(x,\tau)).}
\tag{9.2}
\]

若命中 `Q_sheet`，则两张 source square sheets同时接触；本文证明它最多沿 simple fixed-quartic Hensel synchronization传播，不会产生新的 singular branching。

因此 numerator/length residual `R_src` 与真实 source-common gate `C_src` 的 valuation差异已经被局限到一个固定 simple collision locus。后续 parity ledger可以把它单独列为 `sheet-collision correction`，而无需再次引入 source ratio或第三块变量。

---

<a id="source-spontaneous-source-singular-decimal-orbit"></a>

> 整合来源：`spontaneous-source-singular-decimal-orbit.md`

# A2 source→common singular projection 的 decimal-orbit 排除

> **依赖：** `spontaneous-source-common-integer.md`、`spontaneous-source-singular-resolution.md`。
>
> **严格状态：**projected source→common gate 的唯一 genuine non-`3` inert singular algebraic point位于 `p=1746991`、`tau=807263 mod p`。本文证明该 `tau` 根本不属于 `10` 在 `F_p^×` 中生成的子群，因此不存在任何 decimal length `M` 使 `tau=10^{-M}`。所以无论 abstract transverse blow-up 是否存在，真实十进制 endpoint 永远不会进入该 singular point。结合其余 bad primes 的 finite-root audit，真实 A2 source→common singular sector因此全部关闭；剩余仅为 generic simple roots。本文仍不关闭整个 A2。

---

## 1. 唯一 algebraic singular point

`spontaneous-source-common-integer.md` 已证明：source→common first-layer gate

\[
\mathcal C_{\rm src}(x,\tau)=0
\]

在 genuine non-`3` inert primes上的 projected singular bad set只有

\[
11,\quad1746991,\quad405504443.
\]

其中：

- `p=11` 没有 finite singular point；
- `p=405504443` 的 repeated discriminant factor在 `F_p` 无根；
- 唯一 finite genuine singular point是

\[
\boxed{
p=1746991,\qquad
x_0=1362653,\qquad
\tau_0=807263.}
\tag{1.1}
\]

此前 transverse audit研究的是这个 algebraic point附近的 abstract `p`-adic geometry。真实 endpoint还必须额外满足 decimal orbit：

\[
\boxed{\tau=10^{-M}.}
\tag{1.2}
\]

---

## 2. `已严格完成`：`10` 的模 `p` 阶

精确计算：

\[
\boxed{
\operatorname{ord}_{1746991}(10)=174699.}
\tag{2.1}
\]

并且

\[
\boxed{
174699=3^2\cdot7\cdot47\cdot59.}
\tag{2.2}
\]

注意

\[
p-1=1746990=10\cdot174699,
\]
所以 `10` 只生成 `F_p^×` 的 index-`10` 子群。

所有真实 decimal phase

\[
10^{-M}
\]
当然都属于该子群，因此必要条件为

\[
\boxed{
\tau^{174699}=1\pmod p.}
\tag{2.3}
\]

---

## 3. singular `tau_0` 不在 decimal subgroup

直接 modular exponentiation：

\[
\boxed{
807263^{174699}
\equiv119562
\not\equiv1
\pmod{1746991}.}
\tag{3.1}
\]

因此

\[
\boxed{
807263\notin\langle10\rangle\subset\mathbf F_p^\times.}
\tag{3.2}
\]

等价地，不存在任何整数 `M` 满足

\[
\boxed{
10^{-M}\equiv807263\pmod{1746991}.}
\tag{3.3}
\]

所以 (1.1) 虽然是 source→common algebraic surface 的 genuine singular residue，却不是**十进制 length orbit**上的 residue。

---

## 4. 与 corrected transverse audit 的关系

`spontaneous-source-common-integer.md` 修正了旧 checker 的 `p`-adic carry，并得到 abstract transverse 结论：

- `h>=2` 无 full source/common lift；
- `h=1` 二阶 equation 有两个 normalized transverse roots
  \[
  D=\pm16651.
  \]

`spontaneous-source-singular-resolution.md` 又证明这两个 blow-up roots都是 simple。

这些结论描述的是**如果允许 tau 固定在 algebraic residue `807263`**时的局部几何。本文 (3.3) 说明真实 decimal endpoint根本到不了这个 base point，所以两个 abstract `h=1` branches也无需继续与真实 `(H,e)` 做同步：

\[
\boxed{
\text{decimal orbit exclusion occurs before transverse lifting.}}
\tag{4.1}
\]

因此 carry 修正仍必须保留——它纠正了局部数学事实；但对最终 A2 pruning，decimal-orbit lemma更强。

---

## 5. source→common singular sector 全部关闭

三个 projected bad primes逐一归纳：

\[
\boxed{
\begin{array}{c|c}
p&\text{status}\\ \hline
11&\partial_\tau C_{src}\text{ 无 }F_{11}\text{ 零点}\\
405504443&\text{repeated }D_{sc}\text{ factor无 }F_p\text{ 根}\\
1746991&\tau_0\notin\langle10\rangle
\end{array}}
\tag{5.1}
\]

所以：

\[
\boxed{
\text{真实 decimal A2 source→common channel不存在 singular first-layer state}.}
\tag{5.2}
\]

这比“没有 surviving singular Hensel tree”更强：真正 endpoint连 singular tree的根节点都不存在。

---

## 6. 更新后的 source frontier

source-supported common channel现在只剩

\[
\boxed{\text{generic simple roots of }\mathcal K_{src}(H,E,F)}
\]

与：

\[
4Fe\equiv-E(5F^2+18FH+9H^2)\pmod{p^h},
\]

以及真实窄窗

\[
0<H<F/19,
\qquad
0<e<EF/250
\]

的同步。

因此后续 source 工作不应再审计 singular primes，包括 `1746991`；最有价值的是 generic simple root 的 decimal/natural-representative closure。

---

<a id="source-spontaneous-source-singular-resolution"></a>

> 整合来源：`spontaneous-source-singular-resolution.md`

# A2 source→common 唯一 singular projection 的 blow-up resolution

> **依赖：** `spontaneous-source-common-integer.md`、`spontaneous-source-equal-depth-nogo.md`。
>
> **严格状态：**`spontaneous-source-common-integer.md` 的 corrected carry audit证明：唯一 projected singular prime `p=1746991` 在 source half-depth `h>=2` 全部死亡，而 `h=1` 恰留下两个 normalized transverse templates `D=+-16651`。本文继续证明这两个模板在 blow-up 坐标 `(D,phi)` 上都是 nonsingular：angle 与 sphere 的二阶 normalized equations 具有非零 Jacobian determinant。等价地，消去 `phi` 后的 effective quadratic在两个根上 derivative均非零。因此 projected singularity经过一次 source transverse blow-up 后严格分裂成两条 simple Hensel branches；不会再产生 singular branching。本文不证明这两条 simple branch最终存在，也不宣称 A2 全局关闭。

---

## 1. corrected `h=1` exceptional equation

固定

\[
\boxed{p=1746991,}
\]

projected singular residue

\[
\boxed{x_0=1362653,\qquad \tau_0=807263.}
\tag{1.1}
\]

source half-depth `h=1` 写成

\[
d=pD,
\qquad
\Phi_s=p^2\phi.
\]

angle extra-lift的 normalized equation是

\[
\boxed{
F_{\rm ang}(D,\phi)
:=a_DD^2+b_\phi\phi=0,}
\tag{1.2}
\]

其中

\[
a_D
:=\frac{8(x_0+2)}{99x_0-4}
\equiv-8\pmod p,
\tag{1.3}
\]

\[
b_\phi:=-50625x_0^5
\equiv883946\pmod p.
\tag{1.4}
\]

所以

\[
\phi\equiv1007439D^2\pmod p.
\tag{1.5}
\]

corrected sphere二阶 equation为

\[
\boxed{
F_{\rm sph}(D,\phi)
:=572710+32070D^2-680549\phi=0.}
\tag{1.6}
\]

这里常数 `572710` 是旧纯 `F_p[eps]` checker 漏掉的 genuine `p`-adic carry。

---

## 2. 两个 transverse roots

将 (1.5) 代入 (1.6)：

\[
\boxed{
F_{\rm eff}(D)
:=572710+286982D^2=0\pmod p.}
\tag{2.1}
\]

于是

\[
D^2\equiv1231223\pmod p,
\]
且恰有两个 roots：

\[
\boxed{
D_+=16651,
\qquad
D_-=1730340=-16651\pmod p.}
\tag{2.2}
\]

因为只依赖 `D^2`，两支具有相同 angle correction：

\[
\boxed{\phi_+=\phi_-=987987\pmod p.}
\tag{2.3}
\]

---

## 3. `已严格完成`：effective root均为 simple

由 (2.1)：

\[
F_{\rm eff}'(D)=2\cdot286982D.
\tag{3.1}
\]

逐根计算：

\[
\boxed{
F_{\rm eff}'(D_+)
\equiv1033794\not\equiv0\pmod p,}
\tag{3.2+}
\]

\[
\boxed{
F_{\rm eff}'(D_-)
\equiv713197\not\equiv0\pmod p.}
\tag{3.2-}
\]

所以二阶 exceptional equation 在 blow-up 坐标 `D` 上已经完全非奇异：

\[
\boxed{
D_+,D_-\text{ are two simple roots of }F_{\rm eff}.}
\tag{3.3}
\]

特别地，如果后续 higher endpoint equations允许继续提升，每一支的 `D` correction都由普通一元 Hensel lemma唯一确定；不会再次分叉。

---

## 4. `已严格完成`：完整 `(D,phi)` Jacobian也非奇异

更直接地保留两条 normalized equation

\[
F_{\rm ang}=0,
\qquad
F_{\rm sph}=0.
\]

Jacobian为

\[
J(D,\phi)
=
\begin{pmatrix}
2a_DD&b_\phi\\
64140D&-680549
\end{pmatrix}.
\tag{4.1}
\]

在两个 roots上：

\[
\boxed{
\det J(D_+,\phi_+)
\equiv1475138\not\equiv0\pmod p,}
\tag{4.2+}
\]

\[
\boxed{
\det J(D_-,\phi_-)
\equiv271853\not\equiv0\pmod p.}
\tag{4.2-}
\]

所以不是只有消元后碰巧 simple；完整 angle+sphere 二元系统本身在 blow-up exceptional divisor 上就是 transversal intersection。

---

## 5. singularity 的正确几何解释

projected `(x,tau)` gate在 `p=1746991` 有 singular point：

\[
\mathcal C_{\rm src}
=\partial_x\mathcal C_{\rm src}
=\partial_\tau\mathcal C_{\rm src}=0\pmod p.
\]

但真实 source system还带一个 transverse coordinate

\[
d/p=D.
\]

corrected carry表明：

- `h>=2` 时 transverse correction来得太晚，projected `p^2` 主项无法取消，因此全部死亡；
- `h=1` 时 `D` 恰好在同一 `p^2` 层进入，并把 singular projection分裂成两点；
- 这两点的 Jacobian非零，所以 blow-up 后立刻 smooth。

因此真正的局部图景是

\[
\boxed{
\text{one projected singular point}
\xrightarrow{\text{source blow-up}}
\text{two simple }h=1\text{ branches}.}
\tag{5.1}
\]

这比“singular point无 lift”更精确，也解释了为什么旧 checker若忽略 `p`-adic carry会得到错误结论。

---

## 6. 更新后的 strict frontier

对于 source→common singular sector，现在已经没有继续做 discriminant/Jacobian 的理由：

\[
\boxed{
\begin{array}{c|c}
\text{source half-depth}&\text{status}\\ \hline
h\ge2&\text{严格为空}\\
h=1&D=16651,-16651\text{ 两条 simple branches}
\end{array}}
\tag{6.1}
\]

因此下一步若继续 fixed `1746991`，应把这两条 **simple** branch 与真实 decimal orbit / natural representative / endpoint defect `e` 同步，而不是再次做 singular-prime hunting。

generic source→common roots同理已经属于 simple-orbit问题。A2 仍保持 open。

---

<a id="source-spontaneous-source-target-support-separation"></a>

> 整合来源：`spontaneous-source-target-support-separation.md`

# A2 source common gcd 与 equal-depth target pool 的 complete support separation

> **依赖：** `spontaneous-source-parity-common-gcd.md`、`spontaneous-source-parity-decimal-square-gate.md`、`spontaneous-height-equal-depth-target-ladder.md`、`spontaneous-height-content-oversaturation.md`。
>
> **严格状态：**source common gcd 的 genuine prime必须进入 linear sheet `18K-55`；equal-depth omega-height target baseline必须进入 quadratic `P=6K^2-36K+55`。二者 resultant 为 `330`，此前只把 moving support分离并保留 fixed `11` bookkeeping。本文补齐该 fixed case：共同 root `mod 11` 唯一强迫 `K=0 mod11`，但 genuine height target已有 `p∤K`。因此 source-common genuine support与整个 equal-depth target/serial genuine support完全不相交，不再保留 fixed `11` exception。本文是 support allocation lemma，不证明任一 pool为空，因此不关闭 A2。

---

## 1. source common support enters the linear sheet

fully-decimal source common depth reader为

\[
G_{\rm free}
:=\frac{G_{\rm dec}}{\gcd(G_{\rm dec},b_3^2)}.
\]

对任意 genuine odd source-common prime `r`，固定 small-prime bookkeeping除外，source square-root theorem给

\[
v_r(18K-55)
\ge\left\lceil\frac{v_r(G_{\rm free})}{2}\right\rceil\ge1.
\]

所以

\[
\boxed{
r\mid G_{\rm free}
\Longrightarrow
r\mid18K-55.}
\tag{1.1}
\]

---

## 2. equal-depth target baseline enters `P`

所有 genuine equal-depth omega-height target primes满足

\[
\boxed{r\mid P(K),}
\qquad
P(K):=6K^2-36K+55,
\tag{2.1}
\]

并且 target-ladder 给精确 baseline depth

\[
\boxed{v_r(P)=h_r.}
\tag{2.2}
\]

同一 genuine height sector此前还严格证明

\[
\boxed{r\nmid K.}
\tag{2.3}
\]

理由是 `TK+a_3=\omega W_q≡0 mod r`，而 primitive reduction 给 `r∤a_3T`；若 `r|K` 就会强迫 `r|a_3`，矛盾。

---

## 3. exact resultant leaves only `3,5,11`

直接计算

\[
\boxed{
\operatorname{Res}_K(P(K),18K-55)=330
=2\cdot3\cdot5\cdot11.}
\tag{3.1}
\]

所以任何 odd prime同时满足

\[
r\mid P(K),
\qquad
r\mid18K-55
\]
都必须属于

\[
\boxed{r\in\{3,5,11\}.}
\tag{3.2}
\]

`3,5` 已不属于当前 genuine non-`3,5` height target sector。此前唯一尚未清掉的是 `11`。

---

## 4. fixed `11` root is nongenuine

模 `11`，linear sheet化为

\[
18K-55\equiv7K\pmod{11}.
\]

因此

\[
11\mid18K-55
\Longrightarrow
\boxed{K\equiv0\pmod{11}.}
\tag{4.1}
\]

而

\[
P(0)=55\equiv0\pmod{11},
\]

所以这正是 resultant 中 fixed `11` collision 的唯一 root。

但 genuine target必须满足 (2.3)：

\[
11\nmid K.
\]

故 fixed `11` collision不能属于 genuine equal-depth target：

\[
\boxed{
11\mid P(K),\quad
11\mid18K-55
\Longrightarrow
\text{nongenuine target state}.}
\tag{4.2}
\]

因此 `11` 不再需要作为 source/target overlap exception保留。

---

## 5. complete genuine support separation

综合 §§1--4，在 genuine non-`3,5` height sector严格得到

\[
\boxed{
\operatorname{Supp}_{\rm gen}(G_{\rm free})
\cap
\operatorname{Supp}_{\rm gen}(P)
=\varnothing.}
\tag{5.1}
\]

特别地，所有 equal-depth target subclasses都与 source-common genuine support分离：

\[
\boxed{
E_{\rm first},\ E_{\rm second},\ E_{\rm double}
\quad\text{均不能与 }G_{\rm free}
\text{ 复用 genuine prime}.}
\tag{5.2}
\]

这比旧版本的 moving-support separation更强：现在没有 fixed `11` 尾项。

---

## 6. independent height budgets

source common generic square-root depth满足

\[
\boxed{H_S^{\rm gen}\mid18K-55<180N.}
\tag{6.1}
\]

而 equal-depth target baseline product

\[
G_{\rm tar}:=\prod p^{h_p}
\]
满足 dual-short carrier bound

\[
\boxed{G_{\rm tar}<98T^2.}
\tag{6.2}
\]

由于 (5.1) 是 genuine support完全分离，二者可无条件形成不重复计数的 product budget：

\[
\boxed{
H_S^{\rm gen}G_{\rm tar}
<17640\,NT^2.}
\tag{6.3}
\]

这仍只是上界，不是矛盾；作用是任何后续 lower-bound / parity allocation都可以同时向两池收费。

对 double-serial pool同样有

\[
\boxed{
\gcd_{\rm gen}(G_{\rm free},G_{\rm dbl})=1,}
\tag{6.4}
\]

所以 source square-root cost与

\[
G_{\rm dbl}^3R_{\rm dbl}^2<1053TN^3
\]
也是完全独立的两套 genuine support budget。

---

## 7. current role

A2 当前最重要的两套 moving/genuine prime池现在严格 disjoint：

1. source common / source parity reuse：linear carrier
   \[
   18K-55;
   \]
2. equal-depth target / serial resonance：quadratic carrier
   \[
   P(K)=6K^2-36K+55.
   \]

不存在 fixed `11` genuine bridge。

因此后续若 global parity被迫同时调用 source-common sector和 equal-depth target sector，就会真正增加 distinct prime support与 multiplicative cost；不可能再由同一 genuine prime在两个 ledger中重复承担。

A2 仍为 `待证`。

---

<a id="source-spontaneous-sphere-roots"></a>

> 整合来源：`spontaneous-sphere-roots.md`

# A2 spontaneous sphere 的两个有理第三分子根

> **依赖：** `spontaneous-prefix-eliminant.md`、`spontaneous-prefix-branch-audit.md`。
>
> **严格状态：**本文解释 `Q_1,Q_2` 为什么会出现：`Omega_sp=0` 固定第三分母后，exact sphere 关于 normalized third numerator 本身已经分裂成两个有理函数根；`Q_1,Q_2` 只是 `Theta_dec` root 与这两个 sphere root 的交点。还证明在真实 endpoint box 中两个 sphere root 都严格小于 `-4.77`，而真实 third digit phase 为正且 `O(10^{-M})`。这提供新的 Archimedean separation，但尚未把 modular divisibility 升级成全局矛盾。

---

## 1. 记号

继续使用

\[
x=\frac{b_2}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}},
\qquad
\tau=10^{-M}.
\]

定义

\[
d:=225x^2-y,
\]

\[
A_{\rm sp}:=4d^2-xy^2(99x-4),
\]

\[
A_-:=A_{\rm sp}-2y^2(x+2)^2,
\]

\[
\Delta_0:=2025x^2-18y-y^2.
\]

第三块 normalized decimal phases 为

\[
\bar w:=\frac{b_3}{T10^M},
\qquad
\bar\zeta:=\frac{a_3}{T10^M}.
\tag{1.1}
\]

`Omega_sp=0` 已给

\[
\boxed{
\bar w=-\frac{A_{\rm sp}}{2y^2(x+2)}.
}
\tag{1.2}
\]

---

## 2. `已严格完成`：固定 `bar w` 后 sphere discriminant 是完整平方

exact sphere 在 `(x,y,bar w,bar zeta)` 中为

\[
\boxed{
 x^2\bar w^2(9+y+\bar\zeta)^2
=(2+x+\bar w)^2
\left(
\frac{2025x^2+y^2}{100}\bar w^2
+x^2\bar\zeta^2
\right).
}
\tag{2.1}
\]

把 (1.2) 代入，把 (2.1) 看成 `bar zeta` 的二次式。直接计算 discriminant：

\[
\boxed{
\operatorname{disc}_{\bar\zeta}
=
\left[
7200x^2y^3(x+2)^2dA_-A_{\rm sp}
\right]^2.
}
\tag{2.2}
\]

所以一旦 spontaneous angle condition 固定第三分母，sphere 不再提供新的 quadratic-character gate：它已经在函数域 `Q(x,y)` 上完全 split。

这也解释 `spontaneous-prefix-eliminant.md` 为什么最终会得到两个而不是一个 quadratic branch。

---

## 3. `已严格完成`：两个 sphere root 显式化

定义

\[
\boxed{
A_+
:=202500x^4+99x^2y^2-4xy^2-4y^2,
}
\tag{3.1}
\]

以及

\[
\boxed{
\begin{aligned}
G_*:={}&410062500x^6
-407025x^4y^2
-7290000x^4y
-8100x^3y^2\\
&+99x^2y^4
+3600x^2y^3
+24300x^2y^2
-4xy^4-4y^4.
\end{aligned}}
\tag{3.2}
\]

则 (2.1) 的两个根精确为

\[
\boxed{
\bar\zeta_1
=-\frac{A_+A_{\rm sp}}
{400x^2y^3(x+2)^2},
}
\tag{3.3}
\]

\[
\boxed{
\bar\zeta_2
=\frac{A_{\rm sp}G_*}
{400x^2y^3(x+2)^2\Delta_0}.
}
\tag{3.4}
\]

它们的差进一步完全因子化：

\[
\boxed{
\bar\zeta_2-\bar\zeta_1
=\frac{
9dA_-A_{\rm sp}
}{
200x^2y^3(x+2)^2\Delta_0
}.
}
\tag{3.5}
\]

因此在 genuine separation

\[
p\nmid dA_-A_{\rm sp}\Delta_0xy(x+2)
\]
下，两个 sphere root 在模 `p` 中也严格不同。

`A_-=0` 正是 sphere double-root locus；`spontaneous-prefix-branch-audit.md` 已证明它同时是 concatenated numerator / denominator 双零的 common-`alpha` 通道。

---

## 4. `已严格完成`：`Q_1,Q_2` 就是 `Theta` root 撞两个 sphere roots

在 noncentral channel `2K-9\ne0`，`Theta_dec=0` 给 normalized root

\[
\boxed{
\bar\zeta_\Theta(\tau)
=
\frac{
 x^2\bigl((9+y)^2-18(9+y)\tau+55\tau^2\bigr)
 -\frac1{100}(x+2)^2(2025x^2+y^2)
}
{2x^2\bigl(2(9+y)-9\tau\bigr)}.
}
\tag{4.1}
\]

直接清分母可得：

\[
\boxed{
\operatorname{num}
(\bar\zeta_\Theta-\bar\zeta_1)
=\mathcal Q_1(\tau;x,y),
}
\tag{4.2}
\]

\[
\boxed{
\operatorname{num}
(\bar\zeta_\Theta-\bar\zeta_2)
=-\mathcal Q_2(\tau;x,y).
}
\tag{4.3}
\]

所以两个几十项 quadratic 的几何含义完全明确：

\[
\boxed{
\begin{array}{ccl}
\mathcal Q_1=0
&\Longleftrightarrow&
\bar\zeta_\Theta=\bar\zeta_1,\\
\mathcal Q_2=0
&\Longleftrightarrow&
\bar\zeta_\Theta=\bar\zeta_2.
\end{array}}
\tag{4.4}
\]

这不是两个任意 resultant factors，而是 sphere 的两种真实 algebraic orientation。

---

## 5. `已严格完成`：真实 endpoint box 中两个 sphere roots 都远在负半轴

当前危险 endpoint 有

\[
\frac1{10}<x<\frac2{19},
\qquad
\frac{249}{250}<y<1.
\tag{5.1}
\]

已有

\[
d>\frac54,
\qquad
\Delta_0>\frac54,
\qquad
A_{\rm sp}>\frac{8049}{1444}.
\tag{5.2}
\]

### 5.1 `A_-` 严格为负

\[
A_-
=202500x^4-101x^2y^2-1800x^2y-4xy^2-4y^2.
\]

在 (5.1) 上

\[
\frac{\partial A_-}{\partial x}>0,
\qquad
\frac{\partial A_-}{\partial y}<0.
\]

所以最大值位于

\[
x=\frac2{19},
\qquad
y=\frac{249}{250}.
\]

该点精确值为

\[
\boxed{
A_-
<-\frac{8129844}{16290125}<0.
}
\tag{5.3}
\]

于是由 (3.5)：

\[
\boxed{
\bar\zeta_2<\bar\zeta_1.
}
\tag{5.4}
\]

### 5.2 第一根已有统一负下界

`A_+` 在 box 中对 `x` 递增、对 `y` 递减，所以

\[
A_+>A_+(1/10,1)=\frac{421}{25}.
\tag{5.5}
\]

另一方面

\[
400x^2y^3(x+2)^2
<\frac{2560000}{130321}.
\tag{5.6}
\]

结合 (3.3)、(5.2)、(5.5)：

\[
\boxed{
\bar\zeta_1
<-\frac{1223295069}{256000000}
<-4.778.
}
\tag{5.7}
\]

再由 (5.4)：

\[
\boxed{
\bar\zeta_2<\bar\zeta_1<-4.778.
}
\tag{5.8}
\]

---

## 6. 真实 third digit phase 与 modular roots 的巨大符号错位

实际 endpoint 中

\[
1<\zeta=\frac{a_3}{T}<\frac{251}{250}.
\]

因此

\[
\boxed{
0<\bar\zeta
=\frac{a_3}{T10^M}
<\frac{251}{250}\,10^{-M}.
}
\tag{6.1}
\]

而 `M>=11`，所以真实 `bar zeta` 是极小正数；与 (5.8) 的两个 modular sphere roots 相比：

\[
\boxed{
\bar\zeta-\bar\zeta_i>4.778
\qquad(i=1,2)
}
\tag{6.2}
\]

在实数轴上二者根本不接近。换句话说，generic spontaneous common-prime condition 只能靠真正的 `p`-adic wrapping 实现，绝不来自真实 third coordinate 接近某个 sphere root。

这与 `spontaneous-angle.md` 已得到的 `Omega_sp>0` / modular source root 位于负侧是同一类 Archimedean separation，但这里作用在**第三分子方向**，是第二个独立的真实坐标错位。

---

## 7. 当前证明边界

本文件严格完成：

1. `Omega_sp=0` 后 sphere discriminant 是完整平方；
2. 两个 third-numerator root 显式化；
3. `Q_1,Q_2` 精确识别为 `Theta` root 与两个 sphere root 的交点；
4. genuine endpoint 中两 root 严格排序且都 `<-4.778`；
5. 真实 `bar zeta` 为极小正数，因此存在统一的 `>4.778` Archimedean gap。

但 congruence `p | Q_i` 不要求实数接近，所以 (6.2) **本身不是矛盾**。下一步若要利用这条 sign gap，必须把 `p`-进深度与清分母后的自然整数代表大小联立；例如证明 odd-excess 所需的 `p^e` 超过对应正整数 numerator 的高度。单纯重复“root 为负、实际值为正”不能关闭 A2。

---

<a id="source-spontaneous-tangent-decimal"></a>

> 整合来源：`spontaneous-tangent-decimal.md`

# A2 pure-spontaneous repeated tangent 的原始 decimal 接口

> **依赖：** `spontaneous-single-branch.md`、`spontaneous-single-branch-syzygy.md`、`spontaneous-prefix-eliminant.md`、`decimal-prefix-bridge.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文把两个 sphere orientation 的 repeated-root 条件统一消去，得到一个不含 `z_i,r_s,a_3,b_3` 的 pure-prefix tangent；随后将它乘回原始 decimal integers，并把它与 `Theta_dec`、拼接分子 `alpha`、`R_N`、`Psi_f`、`S_0` 做 exact syzygy。结果把 genuine pure repeated spontaneous prime 与 height/external、q-side contact 严格分离，并把 f-side overlap 压到单一线性 prefix target。最后给出 tangent integer 的精确 `2`-进本原化与 `mod 4` parity law。本文仍**不宣称 A2 全局关闭**。

---

## 1. 两个 sphere orientation 的 repeated tangent 实际是同一条曲线

沿用 compact branch

\[
\mathscr L_i(\tau)
=55\tau^2+18(z_i-s)\tau+s^2-4sz_i-c,
\tag{1.1}
\]

其中

\[
\tau=10^{-M},
\qquad s=9+y,
\qquad
c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.
\tag{1.2}
\]

repeated root 满足

\[
\mathscr L_i(\tau)=0,
\qquad
\mathscr L_i'(\tau)=0.
\]

后者就是

\[
\boxed{55\tau=9(s-z_i).}
\tag{1.3}
\]

所以

\[
z_i=s-\frac{55}{9}\tau.
\]

代回 (1.1)，`z_i` 完全消失：

\[
\boxed{
\mathscr R_{\rm tan}(\tau;x,y)
:=495\tau^2-220s\tau+27s^2+9c
=0.
}
\tag{1.4}
\]

因此 `Q_1,Q_2` 的 repeated-root 风险并不是两套判别式：在 sphere-root denominator 为单位时，两支共享**同一个 pure-prefix tangent**。

---

## 2. `已严格完成`：tangent 与 `C_*` 是同一个正定平方恒等式

`spontaneous-single-branch-syzygy.md` 已证明

\[
23s^2+81c=\frac{C_*}{100x^2}.
\tag{2.1}
\]

对 (1.4) 围绕 central length

\[
\tau_c=\frac{2s}{9}
\]
完成平方：

\[
\begin{aligned}
\mathscr R_{\rm tan}
&=495\left(\tau-\frac{2s}{9}\right)^2
+\frac{23}{9}s^2+9c.
\end{aligned}
\]

结合 (2.1)：

\[
\boxed{
900x^2\mathscr R_{\rm tan}
=C_*+5500x^2(9\tau-2s)^2.
}
\tag{2.2}
\]

这同时解释：

- real endpoint 上 `C_*>0`，故 tangent 无真实根；
- repeated-root character 为 `(C_*/p)=(-55/p)`；
- central line `9tau-2s=0` 与 `C_*` 不是两套无关异常，而是同一 tangent 的两个组成部分。

---

## 3. `已严格完成`：乘回原始 decimal blocks 后只剩一个小整数

令

\[
N=10^M,
\qquad B=b_2,
\qquad A=a_2,
\]

\[
Q=2N+B,
\qquad
K=9N+10A,
\]

\[
N_0=\left(\frac{9B}{2}\right)^2+A^2.
\tag{3.1}
\]

则

\[
x=\frac BN,
\qquad
y=\frac{10A}{N},
\qquad
s=\frac KN,
\qquad
\tau=\frac1N.
\]

并且

\[
c=\frac{Q^2N_0}{B^2N^2}.
\tag{3.2}
\]

所以 (1.4) 乘 `B^2N^2` 后恰得到整数

\[
\boxed{
\mathcal R_{\rm tan}^{\rm int}
:=B^2(27K^2-220K+495)+9Q^2N_0.
}
\tag{3.3}
\]

以及精确尺度关系

\[
\boxed{
B^2N^2\mathscr R_{\rm tan}
=\mathcal R_{\rm tan}^{\rm int}.
}
\tag{3.4}
\]

因此对 genuine odd prime `p`，`p∤BN` 时：

\[
\boxed{
p\mid\mathscr R_{\rm tan}
\iff
p\mid\mathcal R_{\rm tan}^{\rm int}.}
\tag{3.5}
\]

这就是 repeated moving root 的 source-free 原始 decimal 判据。

---

## 4. `已严格完成`：与 `C_*` 原始整数的精确桥

`spontaneous-cstar-audit.md` 定义

\[
\mathcal C_*^{\rm int}
=23B^2K^2+81Q^2N_0.
\tag{4.1}
\]

直接展开：

\[
\boxed{
9\mathcal R_{\rm tan}^{\rm int}
=
\mathcal C_*^{\rm int}
+55B^2(2K-9)^2.
}
\tag{4.2}
\]

这正是 normalized identity (2.2) 的原始整数版本。

---

## 5. `已严格完成`：原始 tangent line 与拼接分子完全同步

令

\[
T=10^m,
\qquad
\alpha=TK+a_3.
\]

把 compact derivative (1.3) 乘回 `TN`。因为

\[
z_i=\frac{a_3}{TN},
\qquad
s=\frac KN,
\]
其原始整数形式为

\[
\boxed{
L_{\rm tan}
:=9(TK-a_3)-55T.
}
\tag{5.1}
\]

并有 exact identity

\[
\boxed{
9\alpha+L_{\rm tan}
=T(18K-55).
}
\tag{5.2}
\]

所以若 `p∤3T` 且

\[
p\mid L_{\rm tan},
\]
则

\[
\boxed{
p\mid\alpha\iff p\mid18K-55.}
\tag{5.3}
\]

特别地，对本文真正的 pure-spontaneous channel

\[
p\nmid\alpha,
\]
任何 repeated prime 自动满足

\[
\boxed{p\nmid18K-55.}
\tag{5.4}
\]

所以 pure repeated branch 与 external double-root 的线性中心严格互斥；反之 repeated prime 一旦进入 `alpha=W_q omega`，立即回到旧 height/content 线，而不再属于 pure spontaneous。

---

## 6. `已严格完成`：`Theta_dec`、tangent 与 `R_tan` 的三项 syzygy

`spontaneous-prefix-eliminant.md` 已有

\[
\Theta_{\rm dec}
=T\mathcal R_\Theta
-2B^2(2K-9)a_3,
\]

其中

\[
\mathcal R_\Theta
=B^2(K^2-18K+55)-Q^2N_0.
\]

与 (3.3)、(5.1) 直接展开得到

\[
\boxed{
9\Theta_{\rm dec}
+T\mathcal R_{\rm tan}^{\rm int}
=2B^2(2K-9)L_{\rm tan}.
}
\tag{6.1}
\]

因此 genuine noncentral repeated carrier 满足

\[
p\mid\Theta_{\rm dec},
\qquad
p\mid L_{\rm tan},
\qquad
p\nmid2B(2K-9)T
\]
时，自动有

\[
\boxed{p\mid\mathcal R_{\rm tan}^{\rm int}.}
\tag{6.2}
\]

更一般地设

\[
\theta=v_p(\Theta_{\rm dec}),
\quad
r=v_p(L_{\rm tan}),
\quad
u=v_p(\mathcal R_{\rm tan}^{\rm int}).
\]

由 (6.1)，若 `theta != r`，则较浅的一项不能被另一项抵消，故

\[
\boxed{
\theta<r\Longrightarrow\nu=\theta,
\qquad
r<\theta\Longrightarrow\nu=r.
}
\tag{6.3}
\]

只有 `theta=r` 时可能发生等深 cancellation，使 `nu` 更深。

---

## 7. `已严格完成`：与 external prefix norm 的 exact bridge

`decimal-prefix-bridge.md` 定义

\[
\mathscr R_N=324Q^2N_0+2695B^2.
\]

从 (3.3) 消去 `Q^2N_0`：

\[
\boxed{
36\mathcal R_{\rm tan}^{\rm int}
=
\mathscr R_N
+B^2(18K-55)(54K-275).
}
\tag{7.1}
\]

因此 external center

\[
18K-55=0,
\qquad
\mathscr R_N=0
\]
确实自动落在 tangent center 上。这不是新的独立 singular obstruction，而是 (5.2) 所解释的 common-`alpha` / external shadow。

对 pure-spontaneous repeated prime，因为 (5.4) 已知 `18K-55` 为单位，所以 (7.1) 不能被误读成 external overlap。

---

## 8. `已严格完成`：q-side additive contact 在 repeated branch 上完全不可能

记

\[
P_{\rm tan}(K):=27K^2-220K+495.
\tag{8.1}
\]

旧 additive prefix polynomial 为

\[
\mathscr S_0
=T(K^2-26)-(2K-9)(2a_3+9T).
\]

直接展开有

\[
\boxed{
9\mathscr S_0
+TP_{\rm tan}(K)
=2(2K-9)L_{\rm tan}.
}
\tag{8.2}
\]

设 `p` 为 genuine noncentral repeated spontaneous prime。若还假设

\[
p\mid\mathscr S_0,
\]
则由 `p|L_tan` 和 (8.2)：

\[
p\mid P_{\rm tan}(K).
\]

但 (3.3) 与 `p|R_tan^int` 立即给

\[
9Q^2N_0\equiv0\pmod p,
\]
与 genuine separation `p∤3QN_0` 矛盾。因此

\[
\boxed{
\text{genuine repeated spontaneous prime}
\Longrightarrow
p\nmid\mathscr S_0.
}
\tag{8.3}
\]

所以 repeated spontaneous carrier 不能回流成 q-side additive contact。

---

## 9. `已严格完成`：f-prefix overlap 只剩一条线性 target

纯 f-prefix polynomial 为

\[
\Psi_f=B^2(K^2-26)-Q^2N_0.
\]

与 (3.3) 相加：

\[
\boxed{
\mathcal R_{\rm tan}^{\rm int}+9\Psi_f
=B^2(2K-9)(18K-29).
}
\tag{9.1}
\]

所以 genuine noncentral repeated prime 若还进入 f-prefix contact

\[
p\mid\Psi_f,
\]
则

\[
\boxed{p\mid18K-29.}
\tag{9.2}
\]

central factor `2K-9` 已由 `spontaneous-prefix-branch-audit.md` 单列。

在 repeated tangent 上，(5.2) 还给

\[
9\alpha\equiv T(18K-55).
\]
若采用 (9.2)：

\[
\boxed{
9\alpha\equiv-26T\pmod p.
}
\tag{9.3}
\]

因此对 non-`3` inert prime（特别地 `p!=13`），该 f-overlap 仍满足 `p∤alpha`；它不会偷偷退回 height channel。真正的 repeated f-denominator overlap 从此只需研究固定线

\[
18K-29=0
\]
与旧 `f/Omega -> Delta_0` 边界，而不再需要一般 quadratic branch。

---

## 10. `已严格完成`：直接接入真实 `(H,e,M)` defect

endpoint `a=9,k=2` 已有

\[
b_2=10^{M-1}+2^{M-1}H,
\qquad
a_2=10^{M-1}-e,
\]

\[
0<H<\frac{5^{M-1}}{19},
\qquad
0<e<\frac{10^{M-1}}{250}.
\]

定义真实小参数

\[
\eta_H:=\frac{H}{5^{M-1}},
\qquad
\eta_e:=\frac{e}{10^{M-1}}.
\tag{10.1}
\]

则

\[
\boxed{
x=\frac{1+\eta_H}{10},
\qquad
y=1-\eta_e,
\qquad
s=10-\eta_e.}
\tag{10.2}
\]

而 (1.2) 的 `c` 精确变成

\[
\boxed{
c=
\frac{(\eta_H+21)^2
\bigl(4\eta_e^2-8\eta_e+81\eta_H^2+162\eta_H+85\bigr)}
{400(\eta_H+1)^2}.}
\tag{10.3}
\]

因此 repeated tangent 已被压成真正三变量 defect 方程

\[
\boxed{
\begin{aligned}
0={}&495\tau^2
-220(10-\eta_e)\tau
+27(10-\eta_e)^2\\
&+\frac{9(\eta_H+21)^2
\bigl(4\eta_e^2-8\eta_e+81\eta_H^2+162\eta_H+85\bigr)}
{400(\eta_H+1)^2},
\end{aligned}}
\tag{10.4}
\]

其中

\[
\tau=10^{-M},\qquad
0<\eta_H<\frac1{19},\qquad
0<\eta_e<\frac1{250}.
\]

这就是所需的 `(H,e,M)` 同步形式：没有 third block，也没有 source scale。实数上左侧严格为正；模 `p` 的 wrapping 是剩余唯一问题。

---

## 11. `已严格完成`：tangent integer 的精确 `2`-进本原化

已有 deep-even source 公式

\[
B=b_2=2^{M+m+1}c_ug,
\qquad
Q=2^{M+1}Q_0,
\tag{11.1}
\]
其中 `Q_0=c_Qq` 为奇数。又因 `B` 为偶数且 `(A,B)=1`，`A` 为奇数；所以

\[
N_0=\left(\frac{9B}{2}\right)^2+A^2\equiv1\pmod4.
\tag{11.2}
\]

(3.3) 的第二项恰有

\[
v_2(9Q^2N_0)=2M+2,
\]
而第一项满足

\[
v_2(B^2P_{\rm tan}(K))\ge2M+2m+2>2M+2,
\]
因为 `m>=1` 且 `P_tan(K)` 为奇数（`K=10P` 为偶数）。故

\[
\boxed{
v_2(\mathcal R_{\rm tan}^{\rm int})=2M+2.}
\tag{11.3}
\]

定义 odd primitive tangent integer

\[
\boxed{
\widehat{\mathcal R}_{\rm tan}
:=\frac{\mathcal R_{\rm tan}^{\rm int}}{2^{2M+2}}.}
\tag{11.4}
\]

由 (11.1)：

\[
\widehat{\mathcal R}_{\rm tan}
=2^{2m}c_u^2g^2P_{\rm tan}(K)
+9Q_0^2N_0.
\]
第一项被 `4` 整除，第二项为奇平方类，故

\[
\boxed{
\widehat{\mathcal R}_{\rm tan}\equiv1\pmod4.
}
\tag{11.5}
\]

于是其中所有 `3 mod 4` 素数的奇 valuation 总数必为偶数：

\[
\boxed{
\sum_{p\equiv3\ (4)}v_p(\widehat{\mathcal R}_{\rm tan})
\equiv0\pmod2.
}
\tag{11.6}
\]

这是 repeated tangent 自身的全局 inert-parity conservation。它尚未单独关闭 repeated carrier，但意味着任何以奇 tangent-depth 出现的 inert prime 必须由另一份 odd inert tangent-depth 配对。

---

## 12. 更新后的 repeated-spontaneous 开放核

本轮把 single-branch singularity 从“大判别式”改写成两条原始整数条件

\[
\boxed{
L_{\rm tan}\equiv0,
\qquad
\mathcal R_{\rm tan}^{\rm int}\equiv0.
}
\]

并严格得到：

1. pure repeated prime 与 `18K-55` external line 互斥；
2. q-side `S_0` overlap 不可能；
3. f-prefix overlap 只剩 `18K-29=0`；
4. tangent 已直接写成 `(H,e,M)` 三变量 defect 方程；
5. odd primitive tangent integer 恒为 `1 mod 4`，所以 inert tangent-depth 必成偶数总奇偶。

因此下一步不应再计算 `Q_1,Q_2` 的高次 discriminant。真正值得做的是：

- 审计 `18K-29` 与 `Delta_0=0` 的 repeated f-overlap；
- 对 pure moving repeated prime，把 (11.6) 与 `widehat(T)_2 == 3 mod 4` 的 odd-inert excess parity 联立；
- 或把 `L_tan` 与 finite-defect natural representative `C,D` 做 higher-depth CRT。

---

<a id="source-spontaneous-tangent-f-denominator"></a>

> 整合来源：`spontaneous-tangent-f-denominator.md`

# A2 repeated spontaneous 与真实 `f`-denominator line

> **依赖：** `spontaneous-angle.md`、`spontaneous-prefix-boundaries.md`、`spontaneous-tangent-decimal.md`。
>
> **严格状态：**本文处理一般 `p|f` 的 repeated spontaneous overlap，不假设 `Psi_f=0`。由真实 `f` denominator line 与 `Omega_sp=0` 先强迫 `Delta_0=0`，此时 sphere 降成唯一有限第三分子 orientation。加入 repeated tangent 后，整个系统降为两个 pure-prefix 方程 `Delta_0=G_f=0`，再消元得到一个显式八次式。本文完整审计该八次式的 inert singular bad primes，并证明所有 genuine singular candidate 都无法提升到 `p^2`。因此此 overlap 不存在新的 singular Hensel tree；但 generic simple roots 仍可能存在，所以本文不宣称该 denominator overlap 全局为空，也不宣称 A2 全局关闭。

---

## 1. `f` denominator line + `Omega_sp` 强迫 `Delta_0=0`

记

\[
F_f=r_s(x+2)+2x.
\]

若 genuine odd prime `p` 同时满足

\[
F_f\equiv0,
\qquad
\Omega_{\rm sp}\equiv0,
\]
且 `p∤x(x+2)`，则

\[
r_s\equiv-\frac{2x}{x+2}.
\tag{1.1}
\]

另一方面

\[
\Omega_{\rm sp}
=A_{\rm sp}r_s+2xy^2(x+2).
\]
代入 (1.1)：

\[
\Omega_{\rm sp}
=\frac{2x}{x+2}
\left[-A_{\rm sp}+y^2(x+2)^2\right].
\]

而 exact identity

\[
\boxed{
-A_{\rm sp}+y^2(x+2)^2
=-100x^2\Delta_0,
}
\tag{1.2}
\]
其中

\[
\Delta_0=2025x^2-18y-y^2.
\]
所以

\[
\boxed{
p\mid f,\ p\mid\Omega_{\rm sp}
\Longrightarrow
\Delta_0\equiv0\pmod p.}
\tag{1.3}
\]

这与旧 resultant `Res(F_f,Omega_sp)=-200x^3 Delta_0` 完全一致，但这里保留了 denominator root 本身。

---

## 2. 第三分母与 sphere 唯一 orientation 都显式化

`spontaneous-angle.md` 有

\[
r_s=\frac{x}{\bar w},
\qquad
\bar w:=\frac{b_3}{T10^M}.
\]
所以 (1.1) 给

\[
\boxed{
\bar w=-\frac{x+2}{2}.
}
\tag{2.1}
\]

令

\[
s=9+y,
\qquad
\bar\zeta=\frac{a_3}{T10^M}.
\]

exact sphere 为

\[
x^2\bar w^2(s+\bar\zeta)^2
=(x+2+\bar w)^2
\left(
\frac{2025x^2+y^2}{100}\bar w^2+x^2\bar\zeta^2
\right).
\tag{2.2}
\]

在 `Delta_0=0` 上

\[
2025x^2+y^2=2y(y+9)=2ys.
\tag{2.3}
\]

代入 (2.1)–(2.3) 并约去 genuine units，可得一次式

\[
x^2(s+2\bar\zeta)
=\frac{y(x+2)^2}{200}.
\]
因此唯一有限 sphere root 为

\[
\boxed{
\bar\zeta_f
=\frac{y(x+2)^2}{400x^2}-\frac{s}{2}.
}
\tag{2.4}
\]

这与 `spontaneous-prefix-boundaries.md` 的 `Delta_0=0` degree-drop 结论吻合：这里不存在第二个有限 orientation。

---

## 3. repeated tangent 唯一固定 decimal length residue

repeated branch derivative 为

\[
55\tau=9(s-\bar\zeta_f),
\qquad
\tau=10^{-M}.
\]
利用 (2.4)：

\[
\boxed{
\tau_f
=\frac9{55}
\left(
\frac{3s}{2}
-\frac{y(x+2)^2}{400x^2}
\right).
}
\tag{3.1}
\]

所以一般 `f`-denominator repeated overlap 不会固定 `K` 为常数；此前 `18K-29=0` 只属于额外 `Psi_f=0` 的更窄子通道。

---

## 4. `已严格完成`：repeated condition 在 `Delta_0=0` 上降成线性 `G_f`

把 (3.1) 代入统一 tangent

\[
\mathscr R_{\rm tan}
=495\tau^2-220s\tau+27s^2+9c,
\]
其中

\[
c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.
\]

清分母以后再对 `Delta_0` 做 Euclidean reduction，余式恰为 `243 G_f`，其中

\[
\boxed{
\begin{aligned}
G_f(x,y):={}&225x^2
(975627x^4+222616x^3+259848x^2+864x+432)\\
&-2(x+2)^2(27827x^2+108x+108)y.
\end{aligned}}
\tag{4.1}
\]

因此 genuine repeated `f`-denominator overlap 必满足

\[
\boxed{
\Delta_0(x,y)=0,
\qquad
G_f(x,y)=0.
}
\tag{4.2}
\]

这里 `G_f` 对 `y` 只有一次；third block、`r_s` 与 `tau` 都已经消失。

---

## 5. `已严格完成`：最终只剩一个八次 pure-prefix polynomial

直接对 (4.2) 消去 `y`：

\[
\boxed{
\operatorname{Res}_y(\Delta_0,G_f)
=-50625x^4\mathcal F_f(x),
}
\tag{5.1}
\]
其中

\[
\boxed{
\begin{aligned}
\mathcal F_f(x):={}&
951848043129x^8
+434380360464x^7
+560807241744x^6\\
&+134769639744x^5
+88351387616x^4
+5400711936x^3\\
&+2954700032x^2
+28892160x
+10416384.
\end{aligned}}
\tag{5.2}
\]

对 genuine `p∤3·5·x`：

\[
\boxed{
\Delta_0=G_f=0
\Longrightarrow
\mathcal F_f(x)=0\pmod p.}
\tag{5.3}
\]

所以一般 repeated `f`-denominator overlap 已从多变量 source system 降成单一 degree-8 prefix curve。

---

## 6. 真实 endpoint defect 上八次式严格为正

令真实 denominator defect

\[
u:=10x-1=\frac{H}{5^{M-1}},
\qquad0<u<\frac1{19}.
\tag{6.1}
\]

直接代入 `x=(1+u)/10`：

\[
10^8\mathcal F_f\left(\frac{1+u}{10}\right)
=\mathcal F_H(u),
\]
其中

\[
\boxed{
\begin{aligned}
\mathcal F_H(u)={}&
951848043129u^8
+11958587949672u^7\\
&+113139094614492u^6
+615777350903064u^5\\
&+2617235426677430u^4
+6748774195745624u^3\\
&+12182775750721052u^2
+12400944702783912u\\
&+5904991117326169.
\end{aligned}}
\tag{6.2}
\]

所有九个系数严格为正。因此

\[
\boxed{u>0\Longrightarrow\mathcal F_H(u)>0.}
\tag{6.3}
\]

所以 repeated `f`-overlap 完全没有 Archimedean root；任何 modular state 都是纯 `p`-adic wrapping。

---

## 7. `有限证书`：八次式 singular bad-prime set

八次式判别式精确分解为

\[
\boxed{
\begin{aligned}
\operatorname{disc}(\mathcal F_f)
={}&2^{136}3^{10}5^{20}11^4 17^4 23^6 43^2 101^8\\
&\cdot163\cdot673^2\cdot2521^2\cdot49663^2\cdot188359^2\\
&\cdot33719039\cdot118599997.
\end{aligned}}
\tag{7.1}
\]

限制到 non-`3` inert primes `p≡3 mod4`，只需审计

\[
\boxed{
11,23,43,163,49663,188359,33719039.}
\tag{7.2}
\]

逐个计算 `gcd(F_f,F_f')`：

- `p=11`：repeated roots 只有 `x=0,-1`（另一个二次因子无 `F_11` 根）；
- `p=23`：唯一 repeated root `x=-2`，为 denominator boundary；
- `p=43`：`gcd=1`，只是 leading-degree degeneration；
- `p=163`：唯一 repeated root `x=56`；
- `p=49663`：唯一 repeated root `x=41967`；
- `p=188359`：唯一 repeated root `x=28889`；
- `p=33719039`：唯一 repeated root `x=27256238`。

代回完整 system `Delta_0=G_f=0`：

\[
\boxed{
\begin{array}{c|c|c|c}
p&x&y&\text{状态}\\ \hline
11&0&0&x\text{ boundary}\\
11&10&9&\text{full singular candidate}\\
23&21&10,18&x+2=0\text{ boundary}\\
43&-&-&\text{no repeated root}\\
163&56&155&\text{full singular candidate}\\
49663&41967&-&\text{no }y\text{ solving full system}\\
188359&28889&-&\text{no }y\text{ solving full system}\\
33719039&27256238&16620484&\text{full singular candidate}
\end{array}}
\tag{7.3}
\]

三组 nonboundary full candidates 的 `x,x+2,y,s,d,A_sp,Nbar` 都为单位。

---

## 8. `有限证书`：三组 genuine singular candidate 全部无法升到 `p^2`

对

\[
F_1=\Delta_0,
\qquad
F_2=G_f
\]
在第一层解 `(x_0,y_0)` 写

\[
x=x_0+pX,
\qquad
y=y_0+pY.
\]

模 `p^2` 的必要条件是线性系统

\[
J(x_0,y_0)
\binom XY
\equiv
-\binom{F_1(x_0,y_0)/p}{F_2(x_0,y_0)/p}
\pmod p.
\tag{8.1}
\]

对三组 genuine singular candidate 做 exact modular row reduction，最后一零行的 augmented residue 分别为

\[
\boxed{
\begin{array}{c|c}
p&\kappa_p\\ \hline
11&10\\
163&148\\
33719039&30845985
\end{array}}
}
\tag{8.2}
\]

三者都非零，所以 (8.1) 均不相容：

\[
\boxed{
\text{三组 genuine singular first-layer state 均无 }p^2\text{ lift}.}
\tag{8.3}
\]

因此：

\[
\boxed{
\text{repeated spontaneous}\cap f\text{-denominator}
\text{ 中不存在 surviving singular Hensel tree}.}
\tag{8.4}
\]

注意这里消灭的是八次 reduced curve 的**进一步 singular branching**。`F_f(x)=0` 在其他 inert primes 上仍可能有 simple roots，所以不能把 (8.4) 写成整个 `f` overlap 为空。

---

## 9. 更新后的 denominator-overlap 核

一般 repeated spontaneous `f`-denominator overlap 现在规范化为

\[
\boxed{
\Delta_0=0,
\qquad
G_f=0,
\qquad
\mathcal F_f(x)=0.
}

并且：

- third block 与 source ratio 已完全消去；
- real endpoint 上 `F_H(u)>0`；
- 所有 inert singular bad primes 已审计；
- genuine singular candidates 全部不能升到 `p^2`。

所以后续若继续处理该 overlap，只需要研究 **simple modular roots of one fixed octic** 与真实 decimal defect orbit `u=H/5^{M-1}` 的同步；不应再做 singular-prime 或 curvature-character 枚举。

---

<a id="source-spontaneous-tangent-psif-overlap"></a>

> 整合来源：`spontaneous-tangent-psif-overlap.md`

# A2 repeated spontaneous 与 `Psi_f` pure-prefix overlap

> **依赖：** `spontaneous-tangent-decimal.md`、`decimal-prefix-bridge.md`、`endpoint-lattice.md` §§16.49–16.51。
>
> **严格状态：**本文只处理 repeated spontaneous prime 同时满足 `Psi_f=0` 的 **pure-prefix overlap**。这不是一般 `f`-denominator carrier 的同义词；一般 denominator contact 仍由 `f` 与 `R_f` 控制，另见 `spontaneous-tangent-f-denominator.md`。在 `Psi_f` overlap 上，prefix 被固定到 `18K-29=0`。若再额外假设同一个 prime 也整除 `f`，则旧 `f`-curvature kernel 可完全显式化，并证明 curvature character 只是旧 principal-square shadow。本文仍**不宣称 A2 全局关闭**。

---

## 1. repeated spontaneous + `Psi_f` 只剩 `18K-29=0`

已有 exact identity

\[
\mathcal R_{\rm tan}^{\rm int}+9\Psi_f
=B^2(2K-9)(18K-29).
\tag{1.1}
\]

若 genuine noncentral repeated prime `p` 满足

\[
p\mid\mathcal R_{\rm tan}^{\rm int},
\qquad p\mid\Psi_f,
\qquad p\nmid B(2K-9),
\]
则

\[
\boxed{18K-29\equiv0\pmod p.}
\tag{1.2}
\]

repeated tangent line

\[
L_{\rm tan}=9(TK-a_3)-55T
\]
随后给

\[
\boxed{
K\equiv\frac{29}{18},
\qquad
\frac{a_3}{T}\equiv-\frac92
\pmod p.}
\tag{1.3}
\]

并且

\[
9\alpha\equiv T(18K-55)\equiv-26T,
\]
所以 non-`3` inert prime `p!=13` 时仍有

\[
\boxed{p\nmid\alpha.}
\tag{1.4}
\]

因此这一 overlap 不会偷偷退回 height/common-`alpha` channel。

---

## 2. 若再额外进入 `f` denominator，则 `f`-channel 自身不能 double-root

本节额外加入

\[
p\mid f.
\tag{2.1}
\]

旧 `f`-channel double-root 必须满足

\[
K\equiv9+2a_3T^{-1}.
\tag{2.2}
\]

由 (1.3)，右边等于

\[
9+2(-9/2)=0.
\]

若 (2.2) 与 `18K=29` 同时成立，只能 `p=29`；但

\[
29\equiv1\pmod4.
\]

故对 odd inert prime：

\[
\boxed{
\text{repeated}+\Psi_f+f
\Longrightarrow
f\text{-channel 为 simple root}.}
\tag{2.3}
\]

注意这只是 triple overlap 的结论，不是对所有 `f`-denominator repeated spontaneous 状态的证明。

---

## 3. triple overlap 上 `R_23=13T^2`

旧 form

\[
\mathscr R_{23}=2a_3^2+9Ta_3+13T^2
\]
在 (1.3) 上给

\[
\boxed{\mathscr R_{23}=13T^2\pmod p.}
\tag{3.1}
\]

---

## 4. `f=0` 与 `Psi_f=0` 的 source-scale 消元

沿用

\[
B=2^{M+m+1}c_ug,
\qquad
Q=2^{M+1}c_Qq,
\]

\[
N_0=5^{\lambda-2d}XY,
\qquad
m=\lambda+d,
\qquad
A_f=2^m5^dg^2.
\]

`p|f` 给

\[
5^\lambda q\equiv-2c_u,
\qquad
q^2\equiv\frac{4c_u^2}{5^{2\lambda}}.
\tag{4.1}
\]

而 `Psi_f=0` 给

\[
Q^2N_0=B^2(K^2-26).
\]
在 `K=29/18`：

\[
K^2-26=-\frac{7583}{324}.
\]

逐项代入并用 `m=lambda+d`：

\[
\boxed{
c_Q^2XY
=-\frac{7583}{1296}A_fT
\pmod p.}
\tag{4.2}
\]

---

## 5. `R_{23,f}` 塌成 square-times-`A_f`

旧 discriminant kernel

\[
\mathscr R_{23,f}
=A_f\mathscr R_{23}+2Tc_Q^2XY.
\]

由 (3.1)、(4.2)：

\[
\boxed{
\mathscr R_{23,f}
=\frac{841}{648}A_fT^2
=\frac{29^2}{2^3 3^4}A_fT^2
\pmod p.}
\tag{5.1}
\]

在 genuine `p|f` 下有 `p∤10g`，且 inert `p!=29`，故

\[
\boxed{p\nmid\mathscr R_{23,f}.}
\tag{5.2}
\]

所以 triple overlap 中的 `f` root 确实 simple。

---

## 6. curvature character 是旧 principal-square shadow

因为

\[
A_f=2^m5^dg^2,
\]
而 `29^2,T^2,3^4,g^2` 都是平方，(5.1) 给

\[
\boxed{
\left(\frac{\mathscr R_{23,f}}p\right)
=
\left(\frac2p\right)^{m+3}
\left(\frac5p\right)^d.
}
\tag{6.1}
\]

这与旧 simple `f`-channel character 完全相同。因此在

\[
\text{repeated spontaneous}+\Psi_f+f
\]
子通道中，curvature character 不提供独立 obstruction：

\[
\boxed{
\text{new-looking curvature condition}
=\text{old principal-square shadow}.}
\tag{6.2}
\]

---

## 7. 证明边界

本文严格完成的是：

1. repeated + `Psi_f` overlap 固定 `18K-29=0`；
2. 若再加入 `p|f`，则 `f`-channel 只能 simple；
3. triple overlap 的 `R_{23,f}` 与 character 完全显式化并降级。

**没有**证明一般 `p|f` 的 repeated spontaneous carrier 必满足 `Psi_f=0`。一般 denominator overlap 必须从 `F_f/Omega -> Delta_0` 直接处理，不能把本文件结果外推。

---

<a id="source-spontaneous-triple-companion-external-budget"></a>

> 整合来源：`spontaneous-triple-companion-external-budget.md`

# A2 `T^circ/J^circ/B^circ` external triple-reuse 的 short central budget

> **依赖：** `spontaneous-residual-parity-doubling.md`、`spontaneous-companion-common-parity-dichotomy.md`、`spontaneous-companion-external-tail-budget.md`、`spontaneous-height-companion-cross.md`、`source-discriminant.md`。
>
> **严格状态：**在 `D_H=1 mod4` 的危险 orientation 中，`T^circ,J^circ,B^circ` 三个 residual companion 都是 positive `3 mod4`。本文审计“一枚 generic external inert prime同时复用三份 parity”的最省-prime情形。令 `G_TJB=gcd(T^circ,J^circ,B^circ)`。对 genuine external prime `p|G_TJB`，`T/J` difference把完整 triple-common exponent送入 central factor `2K-9`，`J/B` difference把同一 exponent送入 `L_JB`。二者与 `B_W` 联立后，把 source ratio消成固定 `23`-discriminant finite-defect quadratic `F_23(C,D)=1204C^2-6396CD+6489D^2`。因此整个 generic external triple-common subproduct整除 `2K-9<20*10^M`，且每个 inert supplier满足 `(p/23)=-1`。本文不排除这些 simple central/defect roots，因此不关闭 A2。

---

## 1. triple common gcd

沿用 height-free positive odd companions

\[
T^\circ,\qquad J^\circ,\qquad B^\circ.
\]

定义

\[
\boxed{G_{TJB}:=\gcd(T^\circ,J^\circ,B^\circ).}
\tag{1.1}
\]

固定 genuine generic external inert prime `p`：

\[
p\mid G_{TJB},
\qquad
p\nmid W_q,
\tag{1.2}
\]

并保留标准 unit separation

\[
\boxed{p\nmid2\cdot3\cdot5\cdot Dgqfzc_uK\omega W_q.}
\tag{1.3}
\]

`spontaneous-companion-external-tail-budget.md` 已证明 external `J/B` common prime自动满足 `p∤omega`，所以 (1.3) 与该结论一致。

写

\[
t:=v_p(T^\circ),
\qquad
j:=v_p(J^\circ),
\qquad
b:=v_p(B^\circ),
\]

\[
\boxed{k:=v_p(G_{TJB})=\min(t,j,b)\ge1.}
\tag{1.4}
\]

---

## 2. `T/J` common depth enters the central factor

residual-parity difference为

\[
\boxed{
T^\circ-5^mJ^\circ
=-2^{m+1}B_0^2(2K-9)\omega W^\circ,}
\tag{2.1}
\]

其中 `B_0=c_ug`，`W^circ=W_q/D_H`。

在 current external prime上右端除 `2K-9` 外的所有 factors都是 units。左端两个 summands均被 `p^k` 整除，所以

\[
\boxed{p^k\mid2K-9.}
\tag{2.2}
\]

若 `t!=j`，则左边有唯一最浅项，因此

\[
\boxed{v_p(2K-9)=\min(t,j).}
\tag{2.3}
\]

但本文只需要 universal lower bound (2.2)。

令

\[
\boxed{H:=2K-9.}
\tag{2.4}
\]

---

## 3. `J/B` common depth enters the linear gate

`spontaneous-companion-common-parity-dichotomy.md` 已证明 generic external common exponent全部进入

\[
\boxed{L_{JB}:=DzK+fN_s,}
\tag{3.1}
\]

其中为避免与 decimal `10^M` 混淆，本文把 source/finite-defect integer记成

\[
\boxed{N_s:=3D-C.}
\tag{3.2}
\]

因此

\[
\boxed{p^k\mid L_{JB}.}
\tag{3.3}
\]

---

## 4. central root converts `B_W` into a `23` source quadratic

source height carrier为

\[
\mathscr B_W
=c_u^2(5K^2-36K+55)+z^2K^2.
\tag{4.1}
\]

用

\[
K=(H+9)/2
\]
直接展开，得到 exact identity

\[
\boxed{
4\mathscr B_W
=(5c_u^2+z^2)H^2
+18(c_u^2+z^2)H
+S_{23},}
\tag{4.2}
\]

其中

\[
\boxed{S_{23}:=81z^2-23c_u^2.}
\tag{4.3}
\]

external prime满足 `p∤W_q`，所以 `D_H=gcd(B_W,W_q)` 在 p 上没有 exponent，因而

\[
v_p(B^\circ)=v_p(B_W)=b\ge k.
\]

结合 (2.2),(4.2)：

\[
\boxed{p^k\mid S_{23}.}
\tag{4.4}
\]

所以 triple reuse自动进入一个 fixed `23` source orientation。

---

## 5. central + `L_JB` gives a finite-defect linear form

由 `H=2K-9`：

\[
\begin{aligned}
2L_{JB}-DzH
&=2DzK+2fN_s-Dz(2K-9)\\
&=9Dz+2fN_s.
\end{aligned}
\]

所以

\[
\boxed{R_{23}:=9Dz+2fN_s}
\tag{5.1}
\]

也满足

\[
\boxed{p^k\mid R_{23}.}
\tag{5.2}
\]

使用

\[
f=z+2c_u,
\qquad
N_s=3D-C,
\]
得到完全显式线性式

\[
\boxed{
R_{23}
=(15D-2C)z+(12D-4C)c_u.}
\tag{5.3}
\]

记

\[
A:=15D-2C,
\qquad
B:=12D-4C.
\tag{5.4}
\]

则

\[
R_{23}=Az+Bc_u.
\]

---

## 6. eliminate the source ratio

定义 conjugate linear form

\[
\boxed{\overline R_{23}:=Az-Bc_u.}
\tag{6.1}
\]

由 (4.3)：

\[
S_{23}=81z^2-23c_u^2.
\]

直接计算 exact eliminant：

\[
\boxed{
A^2S_{23}
-81R_{23}\overline R_{23}
=c_u^2F_{23}(C,D),}
\tag{6.2}
\]

其中

\[
\boxed{
F_{23}(C,D)
:=1204C^2-6396CD+6489D^2.}
\tag{6.3}
\]

由于 `p∤c_u`，结合 (4.4),(5.2)：

\[
\boxed{p^k\mid F_{23}(C,D).}
\tag{6.4}
\]

因此同一个 triple-common exponent被同时读取于

\[
\boxed{2K-9}
\quad\text{和}\quad
\boxed{F_{23}(C,D)}.
\]

---

## 7. the fixed `23` character

把 `F_23` 看成关于 `C` 的 quadratic：

\[
\operatorname{Disc}_C(F_{23})
=(-6396D)^2
-4\cdot1204\cdot6489D^2.
\]

精确化简：

\[
\boxed{
\operatorname{Disc}_C(F_{23})
=2^6 3^8\cdot23\,D^2.}
\tag{7.1}
\]

在 genuine prime `p∤2\cdot3\cdot23D` 上，若 `F_23(C,D)=0 mod p` 有 root，必要且充分的 character为

\[
\boxed{\left(\frac{23}{p}\right)=1.}
\tag{7.2}
\]

当前 supplier是 inert prime

\[
p\equiv3\pmod4,
\]
而

\[
23\equiv3\pmod4.
\]

由 quadratic reciprocity：

\[
\boxed{
\left(\frac{p}{23}\right)
=-\left(\frac{23}{p}\right)
=-1.}
\tag{7.3}
\]

所以 external triple-reuse supplier只能落在 mod-`23` quadratic nonresidue classes。

这是一条 fixed orientation；本文不把它重复计作 q-channel `-23` curvature 的独立 character，除非后续另有条件强迫相反 `(p/23)`。

---

## 8. global short central budget

令 `E_TJB^ext` 为 generic external triple-common primes，并定义

\[
\boxed{
G_{TJB}^{\rm ext}
:=\prod_{p\in E_{TJB}^{\rm ext}}
p^{v_p(G_{TJB})}.}
\tag{8.1}
\]

逐 prime由 (2.2)：

\[
\boxed{G_{TJB}^{\rm ext}\mid2K-9.}
\tag{8.2}
\]

令 decimal scale

\[
N_{10}:=10^M.
\]

endpoint有

\[
0<K<10N_{10}.
\]

故

\[
\boxed{
0<2K-9<20N_{10}.}
\tag{8.3}
\]

于是

\[
\boxed{
G_{TJB}^{\rm ext}<20\cdot10^M.}
\tag{8.4}
\]

同时由 (6.4)：

\[
\boxed{G_{TJB}^{\rm ext}\mid F_{23}(C,D)}
\tag{8.5}
\]

在 generic support上逐 prime成立。

所以一枚 external prime若想同时承担 `T^circ,J^circ,B^circ` 三份 odd parity，它不再只受三个大 carrier约束，而必须把完整 triple-common depth塞进一个只有 `M+2` 位量级的 central integer `2K-9`。

---

## 9. global allocation consequence

在 `D_H=1 mod4` orientation 中，三个 parent companions均为 positive `3 mod4`：

\[
T^\circ\equiv J^\circ\equiv B^\circ\equiv3\pmod4.
\]

如果 global parity试图用同一枚 generic external inert prime复用三份 odd parity，则该 prime必须属于 `G_TJB^ext`，所以同时满足：

\[
\boxed{p^{k}\mid2K-9,}
\]

\[
\boxed{p^{k}\mid F_{23}(C,D),}
\]

\[
\boxed{(p/23)=-1.}
\]

且所有这种 triple reuse的完整 common depth乘积满足

\[
\boxed{G_{TJB}^{\rm ext}<20\cdot10^M.}
\]

因此 triple parity reuse是一个昂贵、短-central、fixed-character branch，而不再是自由 generic prime allocation。

A2 仍为 `待证`。

---

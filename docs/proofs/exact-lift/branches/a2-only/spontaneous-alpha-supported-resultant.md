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
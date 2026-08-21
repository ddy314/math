# A1 minimal diagonal: single-5 collapse by decimal-height synchronization

> 日期：2026-08-22。
>
> 依赖：`deep-denominator-ledger.md`、`global-squarefree-terminal.md`、`decimal-height-synchronization.md`。
>
> 范围：minimal diagonal，`k=g>=32`，single-5 deep sector
> \[
> A=0,
> \qquad D_{\rm gap}=5^B,
> \qquad B>0.
> \]

状态：**已严格完成 reduction。** 本文关闭 strict 5-low，并把整个 single-5 压成两个固定-height cells 与一个唯一 high-contact cell；single-5 尚未完全为空。

---

## 1. deep 与 non-deep 2-side

记

\[
T=10^k,
\qquad
\lambda=2^{\lambda_2},
\qquad
\lambda_2=k+x\ge0.
\]

由于当前是 single-5 deep，而 central denominator 已关闭，必有

\[
\boxed{B>k.}
\tag{1}

`deep-complement-height.md` 给

\[
5^BT\rho=h2^{\lambda_2},
\qquad
(h,10)=1.
\tag{2}

把

\[
\rho=M/L,
\qquad
(L,M)=1
\]

约到最低项，可得

\[
\boxed{
v_5(L)=B+k,}
\tag{3}
\]

\[
\boxed{
v_2(L)=(k-\lambda_2)_+.}
\tag{4}

因此总有

\[
\boxed{v_5(L)>v_2(L).}
\tag{5}

于是 exact decimal-height synchronization 强迫归一化第三分子 `x_sigma` 的 reduced denominator 具有

\[
\boxed{d_2=B+k.}
\tag{6}

特别地这里不是仅有 `d_2>=B+k`：因为 5-side completion height 已至少是 `B+k`，而两侧必须精确相等。

---

## 2. `kappa` 的局部赋值

令 supply complement

\[
M_c:=QG/h.
\]

由 (2) 与全局

\[
\kappa=10^kLQG/M
\]

得到

\[
\boxed{
\kappa=
\frac{5^BT^2M_c}{2^{\lambda_2}}.
}
\tag{7}

minimal diagonal 中

\[
e:=v_2(w)=v_2(G)\in\{0,1,2\},
\]

而 `Q,h` 都是奇数，所以

\[
\boxed{v_2(M_c)=e.}
\tag{8}

因此

\[
\boxed{
a:=v_2(\kappa)=2k+e-\lambda_2\ge0.}
\tag{9}

特别地

\[
\boxed{\lambda_2\le2k+e.}
\tag{10}

同一 minimal-diagonal prefix 还有

\[
v_2(C)=0,
\qquad
v_2(K)=2e,
\qquad
v_2(D_c)=k,
\tag{11}

其中 `D_c=10^kQ` 是 A1 coefficient denominator。记

\[
n_2:=v_2(N).
\]

已有 prefix theorem 给

\[
\boxed{n_2\in\{0,1\},}
\tag{12}

并且 `w` 偶时

\[
\boxed{n_2=0.}
\tag{13}

---

## 3. 先关闭整个 strict 5-low

记

\[
n_5:=v_5(N).
\]

由 (7)，`M_c` 是 5-unit，所以

\[
v_5(\kappa)=B+2k.
\]

同时 `G,C,Q,K` 都是 5-units，`v_5(D_c)=k`，且

\[
v_5(\kappa+2G)=0.
\]

若

\[
\boxed{n_5<B,}
\]

则 `kappa` square 中 5-adic 两项赋值不同，直接得到

\[
v_5(W)
=2k+\frac{B+n_5}{2}.
\]

形式根

\[
x_\sigma
=
\frac{
\kappa G^2C+\sigma(\kappa+G)W
}{
\kappa^2(\kappa+2G)
}
\]

的 numerator 由 `W` 项严格承担较浅赋值，所以两个 sign 都有

\[
\boxed{
 d_5
=2k+\frac{3B-n_5}{2}.
}
\tag{14}

但合法 third block 的 5-side completion height 是 `B+k`，故必须

\[
d_5\le B+k.
\]

而 (14) 给

\[
d_5-(B+k)
=k+\frac{B-n_5}{2}>0,
\]

矛盾。因此

\[
\boxed{
\text{single-5 strict 5-low }(n_5<B)\text{ 全部为空}.}
\tag{15}

这完全替代旧 `deep-single5-first-remainder-height` / `contact-dichotomy` 对 strict-low 的两条带：它们现在都不属于 surviving frontier。

---

## 4. high 5-prefix 中间带也为空

现在设

\[
n_5>B.
\]

写

\[
a_5=B+2k=v_5(\kappa),
\qquad
\kappa=5^{a_5}\kappa_0,
\qquad 5\nmid\kappa_0.
\]

因为 `n_5>B`，平方根可写

\[
W=5^{a_5}w_0,
\qquad5\nmid w_0.
\]

并且精确有

\[
\boxed{
 v_5\!\left(
 w_0^2-(\kappa_0GC)^2
 \right)=n_5-B.
}
\tag{16}

证明只需展开

\[
W^2
=\kappa^2G^2C^2
-\kappa D_c^2N(\kappa+2G),
\]

除去 `5^{2a_5}`；第二项的 valuation 正是 `n_5-B`，而来自 `K-G^2C^2` 的其余项更深。

因为 5 为奇素数，且 `w_0,kappa_0GC` 都是 5-units，(16) 说明两个共轭因子中恰有一个具有 valuation `n_5-B`，另一个为 unit。于是：

- 一个 sign 的形式根保持
  \[
  d_5=B+2k>B+k,
  \]
  自动死亡；
- 唯一可能的 matching sign 在 `n_5-B<a_5` 时满足
  \[
  d_5=2B+2k-n_5.
  \]
  若 `n_5-B>=a_5`，则结论只会更有利于 denominator cancellation。

因此要使 matching sign 满足 `d_5<=B+k`，必要条件统一为

\[
\boxed{n_5\ge B+k.}
\tag{17}

所以

\[
\boxed{
B<n_5<B+k
\Longrightarrow\text{empty}.}
\tag{18}

结合 (15)：所有 single-5 candidate 都必须满足

\[
\boxed{
 n_5=B
 \quad\text{or}\quad
 n_5\ge B+k.
}
\tag{19}

因为 `B>k`，第二支尤其满足

\[
\boxed{v_5(N)>2k.}
\tag{20}

---

## 5. 2-adic synchronization：一般区域

现在使用必要条件 (6)。令

\[
E=v_2(\kappa K)=a+2e,
\]

\[
F=v_2(2GD_c^2N)=2k+e+1+n_2.
\]

所以

\[
\boxed{E-F=2e-\lambda_2-1-n_2.}
\tag{21}

先假设

\[
\lambda_2\le2k-2.
\]

则 `a>=e+2`，从而

\[
v_2(\kappa+G)=e,
\qquad
v_2(\kappa+2G)=e+1.
\tag{22}

### 5.1 `E<F`

此时

\[
v_2(W)=a+e.
\]

形式根 numerator 的两个 summands 都从深度 `a+2e` 开始，因此

\[
v_2(X_\sigma)\ge a+2e.
\]

故

\[
\boxed{
 d_2\le2k-\lambda_2+1.
}
\tag{23}

与 (6)、`B>k` 联立，只能有

\[
\boxed{
\lambda_2=0,
\qquad
B=k+1.
}
\tag{24}

而 (21) 在 `lambda_2=0` 时要满足 `E<F`，结合 (12)-(13)，只有

\[
\boxed{e=0,}
\]

即 `w` 为奇数。

因此这一支唯一可能是

\[
\boxed{
\text{Cell I: }w\in\{1,3\},\quad
\lambda_2=0,\quad B=k+1.
}
\tag{25}

这里 `w=1` 包括 `(z,w)=(1,1),(3,1)`，`w=3` 包括 `(1,3)`。

### 5.2 `E>F`

此时平方存在首先要求

\[
a+F
=4k+2e-\lambda_2+1+n_2
\]

为偶数，即

\[
\boxed{\lambda_2\equiv1+n_2\pmod2.}
\tag{26}

两项赋值不同，较浅的 `W` 项唯一承担 numerator valuation，直接算得

\[
\boxed{
 d_2
=2k+e+\frac{1-n_2-3\lambda_2}{2}.
}
\tag{27}

利用 (6)、`B>k` 及 `E>F` 的小常数范围：

- `e=1` (`w=2`) 时唯一可能小 `lambda_2` 与 parity 冲突；
- `e=2` (`w=4`) 时唯一 surviving value 为
  \[
  \lambda_2=1,
  \]
  此时 (27) 为 `2k+1`，强迫
  \[
  B=k+1.
  \]

所以得到

\[
\boxed{
\text{Cell II: }w=4,\quad
\lambda_2=1,\quad B=k+1.
}
\tag{28}

### 5.3 `E=F`

由 (21)，只可能出现在绝对小的

\[
\lambda_2=2e-1-n_2.
\]

两侧除去公共 2-power 后都是 odd units，因此 inner difference 至少再多一个 2；平方条件又强迫额外 cancellation depth 为偶数。于是 `W` 项比 `kappa G^2C` 更深，得到精确

\[
 d_2=2k-\lambda_2+1.
\]

由 (6)、`B>k` 必有 `lambda_2=0`，但 available resonance values 分别是 `1` 或 `3`（even `w` 时 `n_2=0`），故无解：

\[
\boxed{E=F\Longrightarrow\text{empty}.}
\tag{29}

---

## 6. 2-adic top edge

若

\[
\lambda_2\ge2k,
\]

则

\[
a=2k+e-\lambda_2\le e,
\]

而

\[
v_2(\kappa+2G)=a.
\]

所以 raw denominator `kappa^2(kappa+2G)` 的 2-depth 至多

\[
3e\le6,
\]

不可能达到 (6) 的 `B+k>2k`. 因此

\[
\boxed{\lambda_2\ge2k\Longrightarrow\text{empty}.}
\tag{30}

只剩唯一 top-edge value

\[
\boxed{\lambda_2=2k-1.}
\tag{31}

此时

\[
a=e+1,
\qquad
v_2(W)=2e+1.
\]

令

\[
t_2:=v_2(\kappa+2G).
\]

如果 decimal recovery 成立，(6) 使 `d_2=B+k>=2k+1`。这首先迫使

\[
t_2>3e+1.
\]

另一方面

\[
X_\sigma
\equiv\kappa G^2C
\pmod{\kappa+2G},
\]

而

\[
v_2(\kappa G^2C)=3e+1<t_2.
\]

故两个 sign 都有

\[
v_2(X_\sigma)=3e+1.
\]

于是

\[
d_2=t_2-e+1.
\]

与 (6) 联立，得到唯一 high-contact equation

\[
\boxed{
 v_2(\kappa+2G)
=B+k+e-1.
}
\tag{32}

这就是

\[
\boxed{
\text{Cell III: }
\lambda_2=2k-1,\quad
v_2(\kappa+2G)=B+k+v_2(w)-1.
}
\tag{33}

---

## 7. single-5 的新严格前沿

所有 minimal-diagonal single-5 deep candidate 现在必须同时满足：

### prefix 5-depth

\[
\boxed{
 v_5(N)=B
 \quad\text{or}\quad
 v_5(N)\ge B+k;
}
\tag{34}

以及以下三个 2-adic cells 之一：

\[
\boxed{
\begin{array}{c|c|c|c}
\text{cell}&w&\lambda_2&B\\ \hline
I&1,3&0&k+1\\
II&4&1&k+1\\
III&1,2,3,4&2k-1&\text{subject to (32)}
\end{array}}
\tag{35}

`w=2` 已完全退出 low-`lambda_2` 区，只能存在于 Cell III。

所以此前 single-5 的 unbounded low-ratio / forced-lift strips 已被替换为：

- 两个 fixed-height cells `B=k+1`；
- 一个单一 exact high-contact equation；
- 且所有 cell 都必须承担 prefix 5-adic depth `B` 或至少 `B+k`。

下一步应直接攻击：

1. Cells I-II 中 `v_5(N)=k+1` 或 `v_5(N)>=2k+1` 的 prefix Hensel roots；
2. Cell III 的 exact congruence
   \[
   \kappa\equiv-2G
   \pmod{2^{B+k+e-1}}
   \]
   与 complement equation / odd-prime supply 的兼容性。

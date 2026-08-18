# A2 fixed `23` 在 `(a,k)=(9,2)` reflection `eta=2` high-2 lattice 的三型压缩

> **依赖：** `endpoint-lattice.md` §§16.1–16.7、`spontaneous-cq-relative-depth-nogo.md`、`spontaneous-cq-canonical-defect-overlap.md`。
>
> **严格状态：**本文把 pure-`c_Q` fixed prime `23` 放入 `endpoint-lattice.md` 的最危险 `(a,k)=(9,2)` reflection high-2 lattice，并固定 `eta:=2m-M=2`。利用已有 correlated endpoint interval、`23|c_Q`、high quotient 的 Gaussian norm support 与 `c_Q≡3 mod4`，把整个 `eta=2` fixed-`23` high-2 family 精确压成三个 `(d,c_Q,k_h,slot)` 类型。三型还统一满足 `M=16 mod22`。本文不排除这三个类型，因此不关闭 A2。

---

## 1. general fixed-`eta` slot equation

沿用 `endpoint-lattice.md`：

\[
\eta:=2m-M,
\qquad
d:=m-\lambda>0,
\]

\[
\chi:=1+\frac{H}{5^{M-1}},
\qquad
r:=\frac w\chi,
\qquad
\mathcal H:=3+\zeta-\frac CD.
\]

high-2 factor 取一侧

\[
H_0+\varepsilon Y_2=\frac{g^2k_h}{2},
\qquad
\varepsilon\in\{-1,+1\}.
\]

§16.2/16.7 的 scale equation 可统一写为

\[
\boxed{
K_{\eta,d}
:=
\frac{c_Qk_h5^{d-\eta-1}}{2^{\eta+2}}
=r(\mathcal H+\varepsilon yr).
}
\tag{1.1}

本文固定

\[
\boxed{\eta=2.}
\]

于是

\[
\boxed{
K_{2,d}
=\frac{c_Qk_h5^{d-3}}{16}.
}
\tag{1.2}

---

## 2. endpoint interval 的精确统一界

已有

\[
\frac45<r<\frac{843}{1000},
\]

\[
\frac{997}{250}<\mathcal H<\frac{1001}{250},
\qquad
\frac{249}{250}<y<1.
\tag{2.1}

对 minus slot

\[
K_-=r(\mathcal H-yr).
\]

在上述 rectangle 中，`K_-` 对 `r,mathcal H` 递增、对 `y` 递减，因此

\[
\boxed{
\frac{1594}{625}
<K_-
<\frac{666891399}{250000000}.
}
\tag{2.2-}

对 plus slot

\[
K_+=r(\mathcal H+yr).
\]

已有 §16.15 的 lower bound 与 §16.10 的 correlated upper bound：

\[
\boxed{
\frac{11962}{3125}
<K_+
<\frac{163}{40}.
}
\tag{2.2+}

这些界已经足够在 `eta=2` 上做完整整数筛选。

---

## 3. 把短实区间变成 `P=c_Qk_h` 的整数窗口

记

\[
P:=c_Qk_h.
\]

由 (1.2)，

\[
P=16\cdot5^{3-d}K_{2,d}.
\tag{3.1}

同时 fixed `23` 给

\[
23\mid c_Q
\Longrightarrow
23\mid P.
\tag{3.2}

`c_Q,k_h` 都为正奇数，并且 reflection 中都是 `5`-进单位，所以

\[
\boxed{P\text{ 为 odd }5\text{-unit 且 }23\mid P.}
\tag{3.3}

### `d=1`

minus window：

\[
1020.16<P<1067.026\ldots
\]

区间内仅有两个 `23` 的倍数

\[
1035,\qquad1058.
\]

前者被 `5` 整除，后者为偶数。因此

\[
\boxed{d=1,\ -\text{ slot 无解}.}
\tag{3.4-}

plus window：

\[
1531.136<P<1630.
\]

区间内 `23` 的倍数为

\[
1541,\ 1564,\ 1587,\ 1610.
\]

odd 5-unit 只剩

\[
\boxed{P\in\{1541,1587\}.}
\tag{3.4+}

### `d=2`

minus window：

\[
204.032<P<213.406,
\]
唯一 `23` 倍数是

\[
\boxed{P=207.}
\tag{3.5-}

plus window：

\[
306.2272<P<326,
\]
唯一 `23` 倍数是 `322`，为偶数。因此

\[
\boxed{d=2,\ +\text{ slot 无解}.}
\tag{3.5+}

### `d=3`

minus window落在

\[
40.8064<P<42.682,
\]
plus window落在

\[
61.2454<P<65.2.
\]

都没有 `23` 的倍数。

### `d>=4`

即使取 plus 的统一上界，

\[
P
<16\cdot5^{3-d}\frac{163}{40}
\le\frac{652}{50}<23,
\]
与 `23|P`, `P>0` 矛盾。

所以只需继续筛

\[
(d,slot,P)
=(1,+,1541),
(1,+,1587),
(2,-,207).
\tag{3.6}

---

## 4. Gaussian norm support 删除 `P=1541`

`endpoint-lattice.md` §16.7 已证明

\[
\boxed{\gcd(k_h,c_Q5^d)=1.}
\tag{4.1}

并且若

\[
r\mid k_h,
\qquad r\equiv3\pmod4,
\]
则只能有

\[
\boxed{r=3.}
\tag{4.2}

另外 core/source split 给

\[
\boxed{c_Q\equiv3\pmod4.}
\tag{4.3}

先看

\[
1541=23\cdot67.
\]

因为 `23|c_Q` 且 `(c_Q,k_h)=1`，只有两种 prime-power allocation：

1. `c_Q=23, k_h=67`；
2. `c_Q=1541, k_h=1`。

第一种违反 (4.2)，因为

\[
67\equiv3\pmod4,
\qquad67\ne3.
\]

第二种违反 (4.3)，因为

\[
1541\equiv1\pmod4.
\]

故

\[
\boxed{P=1541\text{ 被完全排除}.}
\tag{4.4}

---

## 5. 剩余两个 product 的完整 factor allocation

### `P=1587`

\[
1587=3\cdot23^2.
\]

因为 `23|c_Q` 且 `(c_Q,k_h)=1`，完整 `23^2` 必须进入 `c_Q`。prime `3` 只能完整进入其中一侧。

若

\[
c_Q=23^2=529,
\qquad k_h=3,
\]
则 `c_Q=1 mod4`，不合法。

唯一剩下

\[
\boxed{
(d,c_Q,k_h,slot)
=(1,1587,1,+).
}
\tag{5.1}

### `P=207`

\[
207=3^2\cdot23.
\]

同样由 `(c_Q,k_h)=1`，完整 `3^2` 只能进入一侧。因此两种合法 allocation 为

\[
\boxed{
(d,c_Q,k_h,slot)
=(2,23,9,-),
}
\tag{5.2a}

\[
\boxed{
(d,c_Q,k_h,slot)
=(2,207,1,-).
}
\tag{5.2b}

两者都满足 `c_Q=3 mod4`，且 `k_h` 的 `3 mod4` prime support只含允许的 `3`。

因此 `eta=2` fixed-`23` high-2 family 被完整压成

\[
\boxed{
\begin{array}{c|c|c|c}
d&c_Q&k_h&slot\\ \hline
1&1587&1&+\\
2&23&9&-\\
2&207&1&-
\end{array}}
\tag{5.3}

---

## 6. 三型统一进入 `M=16 mod22`

`eta=2` 定义给

\[
M=2m-2,
\]
所以

\[
\boxed{M\text{ 为偶数}.}
\tag{6.1}

fixed `23` angle first layer 已严格给出

\[
M\equiv5\text{ or }16\pmod{22}.
\tag{6.2}

第一类为奇数 residue，和 (6.1) 不相容。因此三型统一满足

\[
\boxed{M\equiv16\pmod{22}.}
\tag{6.3}

进一步，三型的 `M,lambda` 关系为：

- `(d,c_Q,k_h)=(1,1587,1)`：`m=lambda+1`，故
  \[
  \boxed{M=2\lambda.}
  \tag{6.4a}
  \]
- 两个 `d=2` 类型：`m=lambda+2`，故
  \[
  \boxed{M=2\lambda+2.}
  \tag{6.4b}
  \]

因此 fixed `23` 的 unbounded length 参数已经被放入两条精确 affine lattice。

---

## 7. 与 `eta<=1` 的现有结果合并

`endpoint-lattice.md` 已有：

- `eta=0` reflection high-2 allocation 全部排除；
- `eta=1` 最终只剩 (16.21) 的五型，其 `c_Q` 分别为
  \[
  3,103,159,7,31,
  \]
  均不被 `23` 整除。

所以 pure-`c_Q` fixed `23` 在当前 dangerous reflection high-2 core 中满足

\[
\boxed{
\eta\le1\Longrightarrow\text{无解},
}
\tag{7.1}

而

\[
\boxed{
\eta=2\Longrightarrow\text{只剩 (5.3) 三型}.}
\tag{7.2}

这是 fixed `23` 与 endpoint high-2 lattice 的第一次有限类型交叉压缩。

---

## 8. 更新后的 frontier

三个剩余类型已经足够具体，后续不应再研究 general `eta=2` real slots。下一步可以分别使用：

1. `(1,1587,1,+)` 中 `v_23(c_Q)=2`，直接接 `spontaneous-cq-canonical-defect-overlap.md` 的 `c>=2` `mod 506` length table；
2. `(2,23,9,-)` 与 `(2,207,1,-)` 都有 `v_23(c_Q)=1`，接 fixed-`23` normalized tail `q_1` / source-ratio Möbius compatibility；
3. 三型都满足 `M=16 mod22`，所以 decimal first-layer root统一为 `10^M=4 mod23`；
4. 再加入 canonical `C` residue 与 `C` 的 natural representative/CRT phase，目标已经是三个明确 lattice family，而非原无界参数空间。
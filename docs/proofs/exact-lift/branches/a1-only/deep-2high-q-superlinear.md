# A1 minimal diagonal: Q-side superlinear bound on the full 2-high master

> 日期：2026-08-20。依赖 `deep-double-2high-master.md`、`deep-complement-height.md`、`deep-contact-q-resultant-loss.md`。本文 supersede `deep-hl-q-superlinear.md` 中“仅 moderate”这一范围限制。

核心结论：对**全部** surviving double-deep 2-high / 5-low master states（包括 `eta<=0` moderate 与 `eta>0` former E2），当前 `k>=32` 都有

\[
\boxed{q>10,900,000T,}
\qquad
\boxed{v<10^{-5}T.}
\]

并且 contact exceptional loss `g=gcd(q,C)` 满足

\[
\boxed{q/g>6800\cdot2^{k-32}.}
\]

状态：**已严格完成。**

---

## 1. complement equation 的通用 q bound

master stripped complement equation始终为

\[
2\beta u-\alpha v=5^d>0,
\qquad M=uv.
\]

所以

\[
\alpha v<2\beta u,
\]

\[
v^2<\frac{2\beta}{\alpha}M.
\]

而 complement height 给

\[
M<10001\frac{T^2}{D}.
\]

因此

\[
v<T\sqrt{\frac{20002\beta}{\alpha D}}.
\]

使用 `Q>99T^2`：

\[
\boxed{
\frac qT
>99\sqrt{\frac{\alpha D}{20002\beta}}.}
\tag{1}

又

\[
\alpha\beta=r_{10},
\]

故

\[
\frac{\alpha D}{\beta}
=\frac{D\alpha^2}{r_{10}}
\ge\frac D{r_{10}}.
\tag{2}

---

## 2. master identity 消去 `eta`

完整 2-high master：

\[
D=2^{2k+3+\eta}5^B,
\]

\[
\xi:=\frac tD
=2^{-\eta}5^{B+2\nu_5}r_{10}.
\]

所以

\[
r_{10}=\xi\,2^\eta5^{-B-2\nu_5}.
\]

代回：

\[
\boxed{
\frac D{r_{10}}
=
\frac{2^{2k+3}5^{2B+2\nu_5}}\xi
=
\frac{2^{2k+3}5^{2Y}}\xi,}
\tag{3}

其中

\[
Y:=B+\nu_5\ge1.
\]

关键是 `eta` 完全消失；因此 moderate / extreme 在 q-scale 上没有区别。

---

## 3. uniform 数值

universal factor window：

\[
\xi<15,214,000.
\]

而 `Y>=1`，故

\[
\boxed{
\frac D{r_{10}}
>
\frac{25\cdot2^{2k+3}}{15,214,000}.}
\tag{4}

结合 (1)-(2)：

\[
\frac qT
>99\sqrt{
\frac{25\cdot2^{2k+3}}
{20002\cdot15,214,000}
}.
\]

最弱层 `k=32` 已大于 `10,900,000`，以后每增加一层精确多一个 factor 2。因此

\[
\boxed{q>10,900,000T.}
\tag{5}

---

## 4. `v` 与 contact exceptional part

由

\[
v=Q/q,
\qquad Q<101T^2,
\]

得到

\[
\boxed{v<10^{-5}T.}
\tag{6}

另一方面 contact resultant：

\[
\boxed{g:=\gcd(q,C)<1599T.}
\]

所以

\[
\boxed{
\frac qg>6800
}
\]

在 `k=32` 已成立，而且 q/T lower 每层翻倍、`g/T` bound 不变：

\[
\boxed{
\frac qg>6800\cdot2^{k-32}.}
\tag{7}

---

## 5. forced contact lift 覆盖 entire master

`deep-contact-q-resultant-loss.md` 给 contact factors `L_-,L_+` 的 guaranteed Q-side block product

\[
Q_-Q_+=q^2/g.
\]

因为 `q/g>1`，必有至少一个 selected Q-primary block满足 `e>v_p(C)`，并在某个 contact factor 中出现严格 amplification

\[
p^{2e-v_p(C)},
\qquad2e-v_p(C)>e.
\]

所以该 forced lifted-block event 现在覆盖：

- moderate 2-high；
- `eta>0` pure-2 denominator side；
- 换言之全部 surviving double-deep。

后续 contact descent 不应再把 `E_2` 当例外分支。

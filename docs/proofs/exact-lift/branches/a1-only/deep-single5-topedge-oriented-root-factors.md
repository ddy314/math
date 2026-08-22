# A1 minimal diagonal: oriented single-5 top-edge root factors

> 日期：2026-08-22。
>
> 依赖：`deep-single5-topedge-real-sign-orientation.md`、`deep-single5-topedge-u2-collapse.md`、`global-squarefree-terminal.md`。
>
> 范围：minimal diagonal `k=g>=32` 的 surviving single-5 top edge。

状态：**本文严格固定两个共轭 factor 的 2-adic 深度与 decimal odd-factor allocation。top edge 尚未整体关闭。**

---

## 1. 记号

沿用

\[
b_1=2^esu,
\qquad
Q=qv,
\qquad
h=qs,
\]

\[
c=5^{B+2k},
\qquad
s+cv=2^{n-1}R,
\qquad R\text{ odd}.
\]

前文已证明

\[
\gcd(u,R)=1,
\qquad
u\mid s+2cv.
\tag{1}
\]

并且

\[
\kappa=2^{e+1}cuv,
\qquad
G=2^esu,
\]

\[
\kappa+2G=2^{n+e}uR.
\tag{2}
\]

令

\[
n_2=v_2(N),
\qquad
n_5=v_5(N),
\qquad
N=2^{n_2}5^{n_5}N_{10},
\qquad (N_{10},10)=1.
\tag{3}
\]

由 real-sign orientation，真实 normalized decimal root 必须是 `X_-`：

\[
X_-=\kappa G^2C-(\kappa+G)W.
\tag{4}
\]

定义两个共轭因子

\[
\boxed{
F_-:=\kappa GC-W,
\qquad
F_+:=\kappa GC+W.
}
\tag{5}
\]

因为 discriminant 非退化且 `W<kappa G C`，二者均为正整数。

---

## 2. 精确 factor product

由 square terminal

\[
W^2
=\kappa^2G^2C^2
-\kappa D_c^2N(\kappa+2G),
\qquad
D_c=10^kQ,
\]

立即得到

\[
\boxed{
F_-F_+
=\kappa D_c^2N(\kappa+2G).
}
\tag{6}
\]

---

## 3. 负号真实根固定 `F_-` 为 2-adic shallow factor

已有 top-edge exact valuations

\[
v_2(\kappa)=e+1,
\qquad
v_2(G)=e,
\qquad
v_2(C)=0,
\qquad
v_2(W)=2e+1.
\]

所以 `kappa G C` 与 `W` 都恰有 valuation `2e+1`，从而

\[
v_2(F_-),v_2(F_+)\ge2e+2.
\tag{7}
\]

又

\[
X_-
=G F_- -\kappa W.
\tag{8}
\]

其中

\[
v_2(\kappa W)=3e+2.
\]

`deep-single5-topedge-real-sign-orientation.md` 已固定真实 `X_-` 必须是 high 2-adic numerator：

\[
v_2(X_-)=n+3e+1>3e+2.
\tag{9}
\]

若 `v2(F_-)>2e+2`，则 (8) 第一项会比 `kappa W` 更深，于是 `v2(X_-)=3e+2`，与 (9) 矛盾。

因此

\[
\boxed{v_2(F_-)=2e+2.}
\tag{10}
\]

由 (6)：

\[
\begin{aligned}
v_2(F_-F_+)
&=(e+1)+2k+n_2+(n+e)\\
&=n+2k+n_2+2e+1.
\end{aligned}
\]

减去 (10)：

\[
\boxed{
v_2(F_+)=n+2k+n_2-1.
}
\tag{11}
\]

所以真实负号根把 `F_-`、`F_+` 的 2-adic角色完全固定：前者 shallow，后者 deep。

---

## 4. Q-complement 的平方必须进入 `F_-`

先证

\[
\boxed{v^2\mid F_-.}
\tag{12}
\]

固定 `p^a||v`。因为 `p|Q` 而 `(q,v)=1`、`(Q,b1)=1`，有

\[
p\nmid G,
\qquad
v_p(D_c)=a.
\]

并且

\[
s+cv\equiv s\not\equiv0\pmod p,
\]

所以 `p∤kappa+2G`。由 `p^a|kappa` 和 square terminal，两项都被 `p^{2a}` 整除，因此

\[
p^a\mid W.
\]

写

\[
\kappa=p^a\kappa_0,
\qquad
W=p^aW_0.
\]

raw decimal denominator `Y=kappa^2(kappa+2G)` 在 `p` 上恰有深度 `2a`，因此 finite-decimal recovery 强迫

\[
p^{2a}\mid X_-.
\tag{13}
\]

把 (4) 除以 `p^a` 后模 `p^a`：

\[
\frac{X_-}{p^a}
\equiv
\kappa_0G^2C-GW_0
=G\left(\kappa_0GC-W_0\right)
=G\frac{F_-}{p^a}
\pmod{p^a}.
\]

`G` 为 unit，(13) 即给

\[
p^a\mid F_-/p^a.
\]

故

\[
p^{2a}\mid F_-.
\]

逐 block 相乘得到 (12)。

---

## 5. high-sign quotient `R` 必须完整进入 `F_+`

由

\[
s+cv=2^{n-1}R
\]

以及 `(s,v)=1`，有

\[
(R,v)=1.
\]

前文又证明 `(R,u)=1`，并且 `R` 与 `s` 互素，因为

\[
s+cv\equiv cv\not\equiv0\pmod s.
\]

所以

\[
\boxed{(R,G)=1.}
\tag{14}
\]

由 (2)：

\[
\kappa+2G\equiv0\pmod R,
\]

故

\[
\kappa+G\equiv-G\pmod R.
\]

raw denominator `Y` 含完整因子 `R`，finite-decimal recovery 因此要求

\[
R\mid X_-.
\]

由 (4) 模 `R`：

\[
X_-
\equiv
\kappa G^2C+GW
=G(\kappa GC+W)
=GF_+
\pmod R.
\]

结合 (14)：

\[
\boxed{R\mid F_+.}
\tag{15}
\]

这里不需要把 `R` 分成 regular / exceptional prime；整个 `R` 一次性进入 fixed factor `F_+`。

---

## 6. `u` 在两个 factors 中都恰好只出现一次

固定 `p^a||u`。`deep-single5-topedge-u2-collapse.md` 已证明 type II 不存在，所以

\[
p\nmid s+cv.
\]

因此 square terminal 中第二项严格承担较浅 `p`-valuation，得到

\[
\boxed{v_p(W)=a.}
\]

另一方面

\[
v_p(\kappa GC)\ge2a.
\]

所以在两个和差中都由 `W` 唯一承担最低赋值：

\[
\boxed{
v_p(F_-)=v_p(F_+)=a.
}
\tag{16}
\]

逐 primary block 合并：两个 factors 的公共 `b1`-complement 部分都恰好是 `u`，不存在额外 `u`-power。

---

## 7. oriented factor normalization

由 (10),(12),(16)，存在正整数 `A` 使

\[
\boxed{
F_-=2^{2e+2}u v^2 A.
}
\tag{17}

由 (11),(15),(16)，存在正整数 `B_*` 使

\[
\boxed{
F_+=2^{n+2k+n_2-1}uR B_*.
}
\tag{18}

把 (17)-(18) 代入 (6)。利用

\[
\kappa=2^{e+1}5^{B+2k}uv,
\]

\[
D_c=2^k5^kqv,
\]

\[
\kappa+2G=2^{n+e}uR,
\]

以及 (3)，全部 `2,u,R,v^2` 精确消去，得到

\[
\boxed{
A B_*
=5^{B+4k+n_5}\,q^2v\,N_{10}.
}
\tag{19}

这是 top-edge 的定向 factor-allocation equation。

后续不再允许交换两个 factors：

- `F_-` 是真实负号根对应的 2-shallow factor，并强制包含 `v^2`；
- `F_+` 是 2-deep factor，并强制包含完整 `R`；
- `u` 在两边都恰好出现一次。

下一步应把 (19) 与 `F_-` 的真实区间、5-adic full/matching depth和 Q-side `q^2` whole-block lifting联立。
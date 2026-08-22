# A1 minimal diagonal: exact decimal factor-pair equation on the single-5 top edge

> 日期：2026-08-22。
>
> 依赖：`deep-single5-topedge-contact-descaling.md`、`deep-single5-topedge-real-sign-orientation.md`。
>
> 范围：minimal diagonal `k=g>=32` 的 surviving single-5 top edge。

状态：**本文给出真实第三分子 `a3` 与去尺度 contact factor pair 的精确差式，并证明 selected Q-supply 的 primary blocks 在真实 decimal root 中没有 coefficient-exception loss。top edge 尚未整体关闭。**

---

## 1. raw normalized root 的完整等式

真实 root 已严格固定为

\[
x_-=rac{a_3}{10^n}.
\tag{1}
\]

另一方面

\[
x_-=rac{X_-}{Y},
\qquad
Y=\kappa^2(\kappa+2G).
\]

在 top edge：

\[
\kappa=2^{e+1}5^{B+2k}uv,
\]

\[
\kappa+2G=2^{n+e}uR.
\]

因此

\[
\boxed{
Y
=2^{n+3e+2}5^{2B+4k}u^3v^2R.
}
\tag{2}
\]

由 (1)：

\[
10^nX_-=a_3Y.
\]

故

\[
\boxed{
X_-
=2^{3e+2}
5^{2B+4k-n}
 a_3u^3v^2R.
}
\tag{3}
\]

这里 `2B+4k-n>=0`，因为 `n` 是 raw denominator 的 5-adic depth `2B+4k` 与 `L`-depth `B+k` 的 decimal completion，不可能超过前者。

---

## 2. 用两个 oriented factors 重写 `X_-`

由定义

\[
F_-=\kappa GC-W,
\qquad
F_+=\kappa GC+W,
\]

直接计算：

\[
\boxed{
2X_-=(\kappa+2G)F_- -\kappa F_+.
}
\tag{4}

`deep-single5-topedge-contact-descaling.md` 给

\[
F_-
=2^{n+2k+n_2-1}u v^2 5^{2k}A_0,
\tag{5}
\]

\[
F_+
=2^{2e+2}uR 5^{2k}vB_0,
\tag{6}
\]

以及

\[
\boxed{
A_0B_0=5^{B+n_5}q^2N_{10}.
}
\tag{7}

把 (5)-(6) 与 `kappa+2G=2^(n+e)uR`、`kappa=2^(e+1)5^(B+2k)uv` 代入 (4)，再和 (3) 比较。约去公共正因子

\[
2^{3e+3}5^{2k}u^2v^2R
\]

得到 exact decimal factor-pair equation

\[
\boxed{
2^J A_0
-5^{B+2k}B_0
=5^r a_3u,
}
\tag{8}

其中

\[
\boxed{
J:=2n+2k+n_2-2e-4,
}
\tag{9}

\[
\boxed{
r:=2B+2k-n\ge0.
}
\tag{10}

由于 `x_->0`，(8) 还给出严格方向

\[
\boxed{
2^J A_0>5^{B+2k}B_0.
}
\tag{11}

这与 contact-factor ordering `L_+>L_-` 给出的另一方向约束是不同的 exact linear combination。

---

## 3. `b1` 的 odd part 与 factor pair 完全互素

若奇素数 `p|b1`，第一分数既约给 `p∤a1`，而

\[
N=a_1^2+(a_2b_1)^2
\]

立即给

\[
p\nmid N.
\]

又 `(b1,Q)=1`，所以 `p∤q`。由 (7)：

\[
p\nmid A_0B_0.
\]

因此

\[
\boxed{
\gcd(A_0B_0,su)=1.
}
\tag{12}

---

## 4. selected Q-supply 没有 coefficient-exception loss

第三分母在 top edge 为

\[
b_3
=2^{n+k-1}5^{n-B-k}qs.
\]

所以由原第三分数既约性

\[
\boxed{
\gcd(a_3,q)=1.
}
\tag{13}

同时 `(q,u)=1`，且 `q` 与 `2,5` 互素。

固定任意素数 `p|q`。若同时

\[
p|A_0,
\qquad
p|B_0,
\]

则 (8) 左侧被 `p` 整除，而右侧 `5^r a3 u` 是 `p`-unit，与 (13) 矛盾。

所以

\[
\boxed{
\gcd(A_0,B_0,q)=1.
}
\tag{14}

设

\[
q=\prod p^{a_p}.
\]

由 product (7)，每个 `p|q` 在 `A0 B0` 中至少贡献 `p^(2a_p)`；由 (14)，该素数的全部幂只能落在唯一一个 factor 中。

因此存在唯一的 coprime whole-block partition

\[
\boxed{
q=q_-q_+,
\qquad(q_-,q_+)=1,
}
\tag{15}

使

\[
\boxed{
q_-^2\mid A_0,
\qquad
q_+^2\mid B_0.
}
\tag{16}

若某个 `p|q` 同时整除 `N10`，其来自 `N10` 的额外 `p`-power 也必须与 `q` 的 square block 一起全部落在同一个 factor；不能跨两边分配。

这比旧 contact-square 的 `q^2/gcd(q,C)` guaranteed lifting 更强：旧 factorization 单独允许 `p|C` 时两个 contact factors 共享 `p`；真实 decimal root 的 reducedness 加上 (8) 排除了这种共享。因此在当前 top edge，selected Q-supply 不再有 coefficient-exception loss。

---

## 5. 当前 exact system

结合 `deep-single5-topedge-contact-descaling.md`，真实 top-edge candidate 必须存在正整数 `A0,B0,a3,R` 满足

\[
\boxed{
\begin{gathered}
A_0B_0=5^{B+n_5}q^2N_{10},\\
2^EvA_0+RB_0=5^BsuC,\\
2^JA_0-5^{B+2k}B_0=5^ra_3u,\\
RB_0>2^EvA_0,\\
2^JA_0>5^{B+2k}B_0,\\
s+5^{B+2k}v=2^{n-1}R,\\
q=q_-q_+,\quad q_-^2|A_0,\quad q_+^2|B_0,
\end{gathered}}
\tag{17}
\]

其中

\[
E=n+2k+n_2-2e-3,
\qquad
J=2n+2k+n_2-2e-4,
\qquad
r=2B+2k-n.
\]

下一步应直接利用两个相反方向的 linear inequalities 与 q-square whole-block partition，而不再回到有 exceptional loss 的旧 contact factor bookkeeping。
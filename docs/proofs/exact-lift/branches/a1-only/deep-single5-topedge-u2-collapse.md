# A1 minimal diagonal: single-5 top-edge type-II complement collapse

> 日期：2026-08-22。
>
> 依赖：`deep-single5-topedge-odd-cancellation.md`、`global-squarefree-terminal.md`。
>
> 范围：minimal diagonal `k=g>=32` 的 surviving single-5 top edge
> \[
> D_{\rm gap}=5^B,\qquad B>k,\qquad \lambda_2=2k-1.
> \]

状态：**本文严格排除 `deep-single5-topedge-odd-cancellation.md` 中的全部 type-II `b_1` complement blocks。top edge 尚未整体关闭。**

---

## 1. 记号

沿用

\[
b_1=2^e s u,\qquad Q=qv,\qquad h=qs,
\]

\[
c=5^{B+2k},
\]

以及

\[
A=s+cv,\qquad B_1=s+2cv.
\]

surviving normalized decimal root 写成

\[
x_\sigma=\frac{X_\sigma}{Y},
\]

其中

\[
X_\sigma=\kappa G^2C+\sigma(\kappa+G)W,
\]

\[
Y=\kappa^2(\kappa+2G),
\]

并且 top edge 中

\[
\kappa=2^{e+1}cuv,
\qquad
G=b_1=2^esu,
\]

\[
\kappa+2G=2^{e+1}uA,
\qquad
\kappa+G=2^euB_1.
\]

finite-decimal recovery 强迫 `Y` 的全部 odd-to-10 part在同一个 `X_sigma` 中约掉。

---

## 2. 共轭 root numerators 的精确乘积

由

\[
W^2=\kappa\bigl(\kappa K-2GD_c^2N\bigr),
\qquad
K=G^2C^2-D_c^2N,
\]

其中 minimal diagonal 的

\[
D_c=10^kQ,
\]

直接展开得到

\[
\boxed{
X_+X_-
=-\kappa(\kappa+2G)
\left(
\kappa^2G^2C^2-D_c^2N(\kappa+G)^2
\right).
}
\tag{1}
\]

这只是 `X_+X_-=(\kappa G^2C)^2-(\kappa+G)^2W^2` 的代数化简，不增加额外假设。

---

## 3. 假设存在一个 type-II block

固定奇素数

\[
p^a\Vert u,
\qquad a\ge1.
\]

记

\[
r=v_p(A)=v_p(s+cv),
\qquad
 d=v_p(B_1)=v_p(s+2cv),
\qquad
 f=v_p(C).
\]

`deep-single5-topedge-odd-cancellation.md` 已证明

\[
\gcd(A,B_1)=1.
\]

所谓 type II 正是

\[
r>0.
\]

于是

\[
\boxed{d=0.}
\tag{2}
\]

并且该文件的 local dichotomy 已严格推出

\[
\boxed{r\ge2a+2f.}
\tag{3}
\]

因为 `p|b_1` 而 `(b_1,Q)=1`、第一分数既约，所以

\[
p\nmid D_c,
\qquad
p\nmid N.
\tag{4}
\]

---

## 4. `W` 与两个共轭 numerators 的最低赋值

square terminal 两项的 `p`-adic valuations 是

\[
v_p(\kappa^2G^2C^2)=4a+2f,
\]

\[
v_p\bigl(\kappa D_c^2N(\kappa+2G)\bigr)
=2a+r.
\]

由 (3)：

\[
2a+r\ge4a+2f.
\]

因此

\[
\boxed{v_p(W)\ge2a+f.}
\tag{5}
\]

另一方面

\[
v_p(\kappa G^2C)=3a+f.
\]

由 (2)：

\[
v_p(\kappa+G)=a.
\]

结合 (5)：

\[
v_p((\kappa+G)W)\ge3a+f.
\]

故两个共轭 numerators 都至少满足

\[
\boxed{
v_p(X_+)\ge3a+f,
\qquad
v_p(X_-)\ge3a+f.
}
\tag{6}
\]

---

## 5. decimal cancellation 与共轭乘积矛盾

由于

\[
Y=\kappa^2(\kappa+2G),
\]

type-II block 在 raw denominator 中的精确深度为

\[
\boxed{v_p(Y)=3a+r.}
\tag{7}
\]

真实 decimal root 的最简分母只能含 `2,5`，故实际 surviving sign `sigma` 必须满足

\[
\boxed{v_p(X_\sigma)\ge3a+r.}
\tag{8}
\]

现在计算 (1) 的精确赋值。

由 (2)：

\[
v_p(\kappa+G)=a.
\]

因此 (1) 中括号的两项分别有深度

\[
4a+2f,
\qquad
2a.
\]

第二项严格更浅，所以

\[
v_p\left(
\kappa^2G^2C^2-D_c^2N(\kappa+G)^2
\right)=2a.
\tag{9}
\]

再由

\[
v_p(\kappa)=a,
\qquad
v_p(\kappa+2G)=a+r,
\]

得到

\[
\boxed{v_p(X_+X_-)=4a+r.}
\tag{10}
\]

可是 (6),(8) 对两个共轭 signs 给出

\[
\begin{aligned}
v_p(X_+X_-)
&=v_p(X_\sigma)+v_p(X_{-\sigma})\\
&\ge(3a+r)+(3a+f)\\
&=6a+f+r\\
&>4a+r,
\end{aligned}
\]

因为 `a>=1,f>=0`。这与 (10) 矛盾。

因此

\[
\boxed{\text{type II 不存在}.}
\tag{11}
\]

---

## 6. entire `b1` odd complement 只能走 type I

所以对 `u` 的每个完整 primary block `p^a||u` 都有

\[
p\nmid s+cv
\]

以及

\[
p^a\mid s+2cv.
\]

whole blocks 相乘得到

\[
\boxed{
\gcd(u,s+cv)=1,
}
\tag{12}
\]

\[
\boxed{
u\mid s+2cv.
}
\tag{13}
\]

又 top-edge high-sign condition 写成

\[
s+cv=2^{n-1}R,
\qquad R\text{ odd},
\]

故 (12) 等价于

\[
\boxed{\gcd(u,R)=1.}
\tag{14}
\]

最后，由 `Q=qv=10b_1+1` 且 `u|b_1`，有

\[
Q\equiv1\pmod u.
\]

把 (13) 乘以 `q`：

\[
u\mid h+2cQ.
\]

于是进一步得到纯 supply/complement 形式

\[
\boxed{
u\mid h+2c.
}
\tag{15}
\]

这里

\[
c=5^{B+2k}.
\]

所以 top edge 的整个 `b_1` odd complement 不再允许平方分配到 `s+cv`；它必须完整进入单一线性 congruence `h+2c`。

下一步应把 (15) 与 `b_1=2^esu`、Q-side complement `v` 的同-sign decimal cancellation 以及两侧 coefficient resultants 联立。
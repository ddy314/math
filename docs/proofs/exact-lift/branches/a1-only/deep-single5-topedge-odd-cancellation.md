# A1 minimal diagonal: single-5 top-edge odd cancellation and complement lifting

> 日期：2026-08-22。
>
> 依赖：`deep-single5-decimal-height-collapse.md`、`decimal-height-synchronization.md`、`deep-single5-topedge-supply-compression.md`。
>
> 范围：minimal diagonal `k=g>=32` 的 surviving single-5 top edge
> \[
> D_{\rm gap}=5^B,\qquad B>k,\qquad \lambda_2=2k-1.
> \]

状态：**本文各 reduction 已严格完成；top edge 尚未整体关闭。**

---

## 1. odd complement 记号

令

\[
e=v_2(b_1)=v_2(w)\in\{0,1,2\}.
\]

把 legal odd supply 与其 complements 写成

\[
\boxed{
b_1=2^e s u,
\qquad Q=qv,
\qquad h=qs,}
\tag{1}
\]

其中

\[
(s,u)=(q,v)=1,
\qquad
(su,qv)=1,
\qquad
(u v,10)=1.
\]

这里 `s` 按 `b1` 的允许 whole prime-power blocks 选择，所以 `u` 也由未选择的完整 odd blocks 组成。

为避免与 reduced decimal numerator 混淆，本文始终把 `u` 仅用于 `b1` 的 odd complement。

置

\[
\boxed{c:=5^{B+2k}.}
\tag{2}

`deep-single5-topedge-supply-compression.md` 与 decimal-height synchronization 给 surviving sign 的 exact 2-adic condition

\[
\boxed{
v_2(s+cv)=n-1,}
\tag{3}

其中 `n=n3>=B+k` 是共同 decimal completion height。

因此定义

\[
\boxed{
R:=\frac{s+cv}{2^{n-1}}\in\mathbf Z_{>0},
\qquad R\text{ odd}.}
\tag{4}

---

## 2. raw normalized root 的 odd denominator 精确为 `u^3 v^2 R`

在 top edge，supply complement 为

\[
M_c=\frac{Qb_1}{h}=2^euv.
\]

所以

\[
\boxed{
\kappa
=\frac{5^BT^2M_c}{2^{2k-1}}
=2^{e+1}cuv.}
\tag{5}

又

\[
G=b_1=2^esu,
\]

因此由 (4)

\[
\begin{aligned}
\kappa+2G
&=2^{e+1}u(cv+s)\\
&=\boxed{2^{n+e}uR}.
\end{aligned}
\tag{6}

`decimal-height-synchronization.md` 的 normalized third numerator root 为

\[
x_\sigma=\frac{X_\sigma}{Y},
\]

\[
X_\sigma=\kappa G^2C+\sigma(\kappa+G)W,
\qquad
Y=\kappa^2(\kappa+2G).
\tag{7}

由 (5)-(6)，`Y` 的完整 odd-to-10 part 为

\[
\boxed{
Y_{10'}=u^3v^2R.}
\tag{8}

这里允许 `u` 与 `R` 有公共素因子；(8) 是逐素数带重数的精确等式。

若 `x_sigma` 真能恢复 decimal block，则

\[
x_\sigma=\frac{a_3}{10^n}.
\]

所以其最简分母不能含任何奇素数 `p!=5`。因此 `Y` 的全部 odd-to-10 part 必须在同一个 root numerator 中约掉：

\[
\boxed{
u^3v^2R\mid X_\sigma.}
\tag{9}

这是 finite-decimal recovery 的必要条件，不使用任何额外 Hensel 假设。

此外，top-edge 中

\[
v_2(Y)=n+3e+2.
\]

surviving sign 的 reduced 2-denominator depth 恰为 `n`，故同一个 numerator 还满足

\[
\boxed{v_2(X_\sigma)=3e+2.}
\tag{10}

---

## 3. 两个关键 linear forms 互素

由 (1) 可知

\[
(u,sv)=1,
\qquad (s,cv)=1.
\]

定义

\[
A:=s+cv,
\qquad
B_1:=s+2cv.
\tag{11}

则

\[
\gcd(A,B_1)
=\gcd(s+cv,cv)
=1.
\tag{12}

特别地，对任意 `p|u`，至多有一个条件

\[
p\mid A,
\qquad p\mid B_1
\]

成立。

另一方面由 (5)-(6)：

\[
\kappa+2G=2^{e+1}uA,
\tag{13}
\]

\[
\kappa+G=2^euB_1.
\tag{14}

---

## 4. 一个 `p^a || u` 的 exact local dichotomy

固定奇素数

\[
p^a\Vert u.
\]

因为 `p|b1` 且第一分数既约，

\[
p\nmid a_1.
\]

又

\[
N=a_1^2+(a_2b_1)^2,
\]

所以

\[
\boxed{p\nmid N.}
\tag{15}

同时 `p∤D_c=10^kQ`，因为 `(b1,Q)=1`。

记

\[
r:=v_p(A)=v_p(s+cv),
\]

\[
d:=v_p(B_1)=v_p(s+2cv),
\]

\[
f:=v_p(C).
\tag{16}

由 (12)：

\[
\boxed{\min(r,d)=0.}
\tag{17}

square terminal 为

\[
W^2
=\kappa^2G^2C^2
-\kappa D_c^2N(\kappa+2G).
\tag{18}

由 (13)-(16)，右侧两项的 valuations 分别是

\[
\boxed{4a+2f,}
\tag{19}

\[
\boxed{2a+r.}
\tag{20}

而 root numerator 两项

\[
\kappa G^2C,
\qquad
(\kappa+G)W
\]

第一项的 valuation 为

\[
\boxed{3a+f.}
\tag{21}

因为 (9) 要求同一个 surviving numerator 至少含

\[
p^{3a+r},
\tag{22}

下面分两种情况。

### 4.1 `r=0`

此时 (20) 等于 `2a`，严格小于 (19)，所以

\[
\boxed{v_p(W)=a.}
\tag{23}

由 (14)，root numerator 第二项的 valuation 为

\[
a+d+a=2a+d.
\tag{24}

第一项 (21) 已至少为 `3a`。若 `d<a`，则第二项严格更浅，整个 `X_sigma` 的 valuation 就是 `2a+d<3a`，与 (22) 矛盾。

因此

\[
\boxed{r=0\Longrightarrow d\ge a.}
\tag{25}

也就是

\[
\boxed{
p^a\mid s+2cv.}
\tag{26}

### 4.2 `r>0`

由 (17) 有 `d=0`。

假设反证

\[
r<2a+2f.
\tag{27}

则 (20) 严格小于 (19)，所以

\[
v_p(W)=a+\frac r2.
\tag{28}

（若 `r` 为奇数，则 (18) 本身已经不可能为平方。）

第二个 root-numerator summand 的 valuation 因 `d=0` 为

\[
2a+\frac r2.
\tag{29}

若它与第一项 (21) valuation 相等，则

\[
2a+\frac r2=3a+f,
\]

即

\[
r=2a+2f,
\]

与 (27) 矛盾。因此两个 summands valuations 不等，整个 numerator valuation 等于较小者，严格小于要求的 `3a+r`，与 (22) 再次矛盾。

故必有

\[
\boxed{
r\ge2a+2f.}
\tag{30}

特别地

\[
\boxed{
p^{2a}\mid s+cv.}
\tag{31}

更精确地还有

\[
\boxed{
p^{2a+2v_p(C)}\mid s+cv.}
\tag{32}

---

## 5. whole-block complement splitting

对 `u` 的每个完整 primary block `p^a||u`，由 §§4.1--4.2 必落入互斥两类之一：

- type I：`p∤s+cv`，并有 `p^a|s+2cv`；
- type II：`p|s+cv`，并有 `p^(2a)|s+cv`。

由于两个 linear forms 互素，whole blocks 可以唯一分组为互素正整数

\[
\boxed{u=u_1u_2,\qquad (u_1,u_2)=1,}
\tag{33}

满足

\[
\boxed{
u_1\mid s+2cv,}
\tag{34}

\[
\boxed{
u_2^2\mid s+cv.}
\tag{35}

这里 `u2^2` 还可以按 (32) 用 `C` 的 local exponents 进一步增强。

这是由 finite-decimal recovery 强迫出来的 `b1`-complement whole-block lifting；其来源与 rational-contact square 的 Q-side lifting 不同。

---

## 6. size consequence

由 (34)-(35) 与正性：

\[
u_1\le s+2cv,
\]

\[
u_2\le\sqrt{s+cv}.
\]

故

\[
\boxed{
u
\le
(s+2cv)\sqrt{s+cv}.}
\tag{36}

这只是本文 local lifting 的一个粗 size corollary；当前尚未单独构成矛盾。

后续应把 (33)-(35) 与独立的 Q-side contact-square block lifting 以及 `v=Q/q≡3 mod4` 联立。
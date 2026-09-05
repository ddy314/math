# A1 minimal diagonal: single-5 top-edge odd cancellation and one-sided complement lock

> 日期：2026-08-22。
>
> 依赖：`deep-single5-decimal-height-collapse.md`、`decimal-height-synchronization.md`、`deep-single5-topedge-supply-compression.md`。
>
> 范围：minimal diagonal `k=g>=32` 的 surviving single-5 top edge
> \[
> D_{\rm gap}=5^B,\qquad B>k,\qquad \lambda_2=2k-1.
> \]

状态：**本文各 reduction 已严格完成；top edge 尚未整体关闭。** 本版强化旧的 `u=u_1u_2` split：所谓 type-II block 实际全部不可能，因此整个 `b_1` odd complement 只能进入同一个线性因子。

---

## 1. odd complement 与 high-sign 线性因子

令

\[
e:=v_2(b_1)=v_2(w)\in\{0,1,2\},
\]

并把 legal odd supply 与 complements 写成

\[
\boxed{
b_1=2^esu,\qquad Q=qv,\qquad h=qs,
}
\tag{1}
\]

其中

\[
(s,u)=(q,v)=1,\qquad (su,qv)=1,\qquad (uv,10)=1.
\]

置

\[
\boxed{c:=5^{B+2k}.}
\tag{2}
\]

surviving high sign 的 decimal-height synchronization 给

\[
\boxed{v_2(s+cv)=n-1,}
\tag{3}
\]

其中 `n=n_3>=B+k`。定义

\[
\boxed{
A:=s+cv=2^{n-1}R,
\qquad R\in\mathbf Z_{>0}\text{ odd},
}
\tag{4}
\]

并令

\[
\boxed{B_1:=s+2cv.}
\tag{5}
\]

因为 `(s,cv)=1`，

\[
\boxed{(A,B_1)=1.}
\tag{6}
\]

---

## 2. normalized root 的完整 odd denominator

在 top edge，

\[
M_c=\frac{Qb_1}{h}=2^euv,
\]

所以

\[
\boxed{
\kappa
=\frac{5^BT^2M_c}{2^{2k-1}}
=2^{e+1}cuv.
}
\tag{7}
\]

又 `G=b_1=2^esu`，于是

\[
\boxed{
\kappa+2G=2^{e+1}uA=2^{n+e}uR,
}
\tag{8}
\]

\[
\boxed{
\kappa+G=2^euB_1.
}
\tag{9}
\]

`decimal-height-synchronization.md` 的 normalized third-numerator root 为

\[
x_\sigma=\frac{X_\sigma}{Y},
\]

\[
X_\sigma
=\kappa G^2C+\sigma(\kappa+G)W,
\qquad
Y=\kappa^2(\kappa+2G).
\tag{10}
\]

由 (7)-(8)，`Y` 的完整 non-`2,5` part 为

\[
\boxed{Y_{10'}=u^3v^2R.}
\tag{11}
\]

若真实 decimal block 存在，则

\[
x_\sigma=\frac{a_3}{10^n},
\]

故全部 odd denominator 必须在同一个 root numerator 中约掉：

\[
\boxed{u^3v^2R\mid X_\sigma.}
\tag{12}
\]

特别地，对任意 `p^a||u`，若

\[
r:=v_p(A),
\]

则

\[
\boxed{v_p(X_\sigma)\ge3a+r.}
\tag{13}
\]

---

## 3. 一个 `p^a||u` 的局部数据

固定奇素数

\[
p^a\Vert u.
\]

因为 `p|b_1` 且 `(a_1,b_1)=1`，有 `p∤a_1`。又

\[
N=a_1^2+(a_2b_1)^2,
\]

所以

\[
\boxed{p\nmid N.}
\tag{14}
\]

同时 `p∤D_c:=10^kQ`，因为 `(b_1,Q)=1`。

记

\[
r:=v_p(A),\qquad d:=v_p(B_1),\qquad f:=v_p(C).
\tag{15}
\]

由 (6)：

\[
\boxed{\min(r,d)=0.}
\tag{16}
\]

全局 square terminal 写成

\[
W^2
=\kappa^2G^2C^2
-\kappa D_c^2N(\kappa+2G).
\tag{17}
\]

右侧两项的 `p`-adic valuations 精确为

\[
\boxed{4a+2f,}
\tag{18}
\]

\[
\boxed{2a+r.}
\tag{19}
\]

而 `X_sigma` 的第一 summand

\[
\kappa G^2C
\]

有 valuation

\[
\boxed{3a+f.}
\tag{20}
\]

---

## 4. `r=0` 时强迫整块进入 `B_1`

若

\[
r=0,
\]

则 (19) 严格小于 (18)，故

\[
\boxed{v_p(W)=a.}
\tag{21}
\]

由 (9)，第二 root summand

\[
(\kappa+G)W
\]

的 valuation 为

\[
2a+d.
\tag{22}
\]

若 `d<a`，则该 summand 比第一项严格浅，故

\[
v_p(X_\sigma)=2a+d<3a,
\]

与 (13) 矛盾。因此

\[
\boxed{d\ge a.}
\tag{23}
\]

即

\[
\boxed{p^a\mid B_1=s+2cv.}
\tag{24}
\]

---

## 5. `r>0` 全部不可能

下面证明旧版保留的 type-II branch 实际为空。由 (16)，`r>0` 时必有

\[
d=0.
\tag{25}
\]

分三种情形。

### 5.1 `r<2a+2f`

此时 (19) 严格小于 (18)，所以

\[
v_p(W)=a+\frac r2.
\tag{26}
\]

若 `r` 为奇数，则 (17) 已不可能为平方；故只需看偶 `r`。

第二 root summand valuation 为

\[
2a+\frac r2.
\tag{27}
\]

它与第一项 (20) 相等当且仅当

\[
r=2a+2f,
\]

与当前严格不等式矛盾。因此两个 summands valuation 不等，且其中第二项满足

\[
2a+\frac r2<3a+r.
\]

于是

\[
v_p(X_\sigma)<3a+r,
\]

与 (13) 矛盾。

### 5.2 `r=2a+2f`

此时 (18)-(19) 同深。由 (17) 有

\[
v_p(W)\ge2a+f.
\]

定义

\[
F_\pm:=\kappa GC\pm W.
\]

则

\[
F_+F_-
=\kappa D_c^2N(\kappa+2G),
\]

故

\[
v_p(F_+F_-)=2a+r=4a+2f.
\tag{28}
\]

而 `v_p(\kappa GC)=2a+f`，所以每个 `F_\pm` 都至少含 `p^{2a+f}`。由 (28) 只能有

\[
\boxed{v_p(F_+)=v_p(F_-)=2a+f.}
\tag{29}
\]

再用恒等式

\[
X_+X_-
=-\kappa(\kappa+2G)
\left(
\kappa^2G^2C^2-D_c^2N(\kappa+G)^2
\right).
\tag{30}
\]

括号内两项 valuation 分别为

\[
4a+2f,
\qquad 2a
\]

（因为 `d=0`），故括号 valuation 精确为 `2a`。于是

\[
\boxed{v_p(X_+X_-)=6a+2f.}
\tag{31}
\]

另一方面原定义 (10) 中每个 `X_\pm` 的两个 summands 都至少有 valuation `3a+f`，所以

\[
v_p(X_\pm)\ge3a+f.
\]

与 (31) 联立得到

\[
\boxed{v_p(X_+)=v_p(X_-)=3a+f.}
\tag{32}
\]

但 decimal recovery 要求

\[
3a+r=5a+2f,
\]

严格大于 (32)，矛盾。

### 5.3 `r>2a+2f`

此时 (18) 严格小于 (19)，所以

\[
v_p(W)=2a+f.
\]

仍令 `F_\pm=\kappa GC\pm W`。由

\[
v_p(F_+F_-)=2a+r,
\]

以及

\[
F_++F_-=2\kappa GC,
\qquad
v_p(2\kappa GC)=2a+f,
\]

可知两个 factors 的 valuations 精确为

\[
\boxed{
\{v_p(F_+),v_p(F_-)\}
=
\{2a+f,\ r-f\}.
}
\tag{33}
\]

固定一个 root sign `sigma`。

若 `F_sigma` 取高 valuation `r-f`，使用

\[
\boxed{
X_\sigma=(\kappa+G)F_\sigma-\kappa^2GC
}
\tag{34}
\]

则两项 valuations 分别为

\[
a+r-f,
\qquad 3a+f.
\]

由 `r>2a+2f`，第一项更深，所以

\[
v_p(X_\sigma)=3a+f<3a+r.
\]

若 `F_sigma` 取低 valuation `2a+f`，则 opposite factor `F_{-sigma}` 取高 valuation `r-f`。使用等价恒等式

\[
\boxed{
X_\sigma
=\kappa GC(\kappa+2G)
-(\kappa+G)F_{-\sigma}
}
\tag{35}
\]

两项 valuations 分别为

\[
3a+f+r,
\qquad a+r-f.
\]

第二项严格更浅，因此

\[
v_p(X_\sigma)=a+r-f<3a+r.
\]

两种 signs 都与 (13) 矛盾。

所以

\[
\boxed{r>0\text{ 不可能}.}
\tag{36}

---

## 6. one-sided complement theorem

对 `u` 的每个完整 primary block `p^a||u`，§5 排除 `p|A`；于是必有 `r=0`，再由 §4 得

\[
p^a\mid B_1.
\]

逐块相乘即得：

\[
\boxed{\gcd(u,s+cv)=1,}
\tag{37}
\]

\[
\boxed{u\mid s+2cv.}
\tag{38}
\]

因为

\[
s+cv=2^{n-1}R,
\]

(37) 还给

\[
\boxed{(u,R)=1.}
\tag{39}
\]

而 (38) 可等价写成

\[
\boxed{u\mid 2^nR-s.}
\tag{40}
\]

这是当前 top edge 的 canonical `b_1`-complement constraint：所有未被 odd supply `s` 选择的完整 `b_1` blocks 都必须进入另一条线性式，不能进入承担 high 2-adic cancellation 的 `s+cv`。

后续应把 (37)-(40) 与 universal four-factor / contact-factor identities 联立；不能再把旧版 type-II square lifting 当独立可用分支。
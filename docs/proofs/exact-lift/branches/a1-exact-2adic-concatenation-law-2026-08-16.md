# A1 exact 2-adic concatenation law — 2026-08-16

本文从原始拼接整数关系

\[
q\alpha=H\beta
\]

与第三分数既约性推出一个覆盖整个 A1 的精确二进最大定律。

核心结论：

\[
\boxed{
v_2(b_3)\le\ell+v_2(D),
}
\]

且二进最大 denominator 的位置由 `v_2(b_3)` 与 `\ell+v_2(D)` 的比较精确决定。

本文结论均为 **已严格完成**。

---

## 1. 拼接分子分母没有 `2,5` 公因子

A1 中

\[
\alpha=TC+a_3,
\qquad
\beta=TD+b_3,
\qquad
T=10^\ell.
\]

对

\[
p\in\{2,5\},
\]

有

\[
\alpha\equiv a_3\pmod p,
\qquad
\beta\equiv b_3\pmod p.
\]

如果 `p` 同时整除 `\alpha,\beta`，则

\[
p\mid a_3,
\qquad
p\mid b_3,
\]

与

\[
\gcd(a_3,b_3)=1
\]

矛盾。

因此

\[
\boxed{
\gcd(\alpha,\beta)\text{ 不含素因子 }2,5.
}
\tag{1}
\]

---

## 2. 二进上 `\alpha` 必为奇数且 `v_2(\beta)=v_2(q)`

令

\[
e_i=v_2(b_i),
\qquad
E=\max(e_1,e_2,e_3)=v_2(q).
\]

整数球面模 `4` 已证明最大二进指数唯一取得。因此不可能有

\[
e_1=e_2=e_3=0,
\]

故

\[
\boxed{E>0.}
\tag{2}
\]

同时整数球面高度满足

\[
\boxed{H\text{ 为奇数}.}
\tag{3}
\]

原整数关系为

\[
q\alpha=H\beta.
\tag{4}
\]

如果 `\alpha` 为偶数，则 (4) 强迫 `\beta` 也为偶数，与 (1) 矛盾。

所以

\[
\boxed{v_2(\alpha)=0.}
\tag{5}
\]

对 (4) 取二进赋值，并使用 (3)、(5)：

\[
\boxed{
v_2(\beta)=v_2(q)=E.
}
\tag{6}
\]

这是精确等式，不只是 divisibility。

---

## 3. 比较 `TD` 与 `b_3`

记

\[
\boxed{d_2=v_2(D),}
\qquad
\boxed{e_3=v_2(b_3).}
\]

因为

\[
T=10^\ell,
\]

有

\[
\boxed{v_2(TD)=\ell+d_2.}
\tag{7}
\]

而

\[
\beta=TD+b_3.
\]

设

\[
A_2:=\ell+d_2.
\]

逐种比较 `e_3` 与 `A_2`。

---

## 4. 若 `e_3<A_2`，第三块就是唯一二进最大

若

\[
e_3<A_2,
\]

两项赋值不同，所以

\[
\boxed{v_2(\beta)=e_3.}
\]

由 (6)：

\[
E=e_3.
\]

而二进最大指数唯一取得，因此

\[
\boxed{
e_3>e_1,e_2.
}
\tag{8}
\]

所以

\[
\boxed{
 e_3<\ell+v_2(D)
\Longrightarrow
b_3\text{ 取得唯一二进最大}.}
\tag{9}

此前的 `e_3<\ell` unique-max 定理只是 (9) 的一个特例。

---

## 5. `e_3>A_2` 完全不可能

若

\[
e_3>A_2,
\]

则

\[
v_2(\beta)=A_2.
\]

但

\[
E=\max(e_1,e_2,e_3)\ge e_3>A_2,
\]

与 (6) 的

\[
E=v_2(\beta)
\]

矛盾。

所以

\[
\boxed{
e_3\le\ell+v_2(D).}
\tag{10}

---

## 6. 取等时主导权必转移到前缀

最后设

\[
\boxed{e_3=A_2=\ell+d_2.}
\tag{11}

写

\[
TD=2^{e_3}u,
\qquad
b_3=2^{e_3}v,
\]

其中 `u,v` 都为奇数。

于是

\[
\beta
=2^{e_3}(u+v),
\]

而奇数加奇数为偶数，所以

\[
\boxed{
v_2(\beta)
=e_3+v_2(u+v)>e_3.}
\tag{12}

由 (6)：

\[
E=v_2(\beta)>e_3.
\]

因此最大二进指数不在第三块，而必须由第一、第二块中的恰好一个取得。

所以

\[
\boxed{
\max(e_1,e_2)
=e_3+v_2(u+v),
}
\tag{13}

且最大者唯一。

换言之：

\[
\boxed{
 e_3=\ell+v_2(D)
\Longrightarrow
\text{prefix unique max，且深度由 }TD+b_3\text{ 的 cancellation 精确给出}.}
\tag{14}

---

## 7. 精确二进二分

整个 A1 的二进 denominator flow 现在可以压成：

### Third-max side

\[
\boxed{
 v_2(b_3)<\ell+v_2(D),
}
\]

且

\[
\boxed{
v_2(b_3)>
\max(v_2(b_1),v_2(b_2)).}
\]

### Prefix-cancellation side

\[
\boxed{
 v_2(b_3)=\ell+v_2(D),
}
\]

且第一、第二分母中恰好一个的二进指数等于

\[
\boxed{v_2(TD+b_3)}
\]

并严格大于第三块。

绝无

\[
v_2(b_3)>\ell+v_2(D)
\]

的候选。

这条定律对四个位数层全部有效。
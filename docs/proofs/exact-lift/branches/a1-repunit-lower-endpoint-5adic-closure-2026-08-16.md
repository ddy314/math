# A1 second-repunit lower-endpoint 5-adic closure — 2026-08-16

本文把 `a1-repunit-minimal-third-5adic-closure-2026-08-16.md` 从最小第三尾 `\ell=2k+1` 推广到任意第三尾长度。

当前仍处于 second-repunit edge：

\[
\boxed{
 g=0,
\quad n_2=2k,
\quad a_2=10^{2k}-1,
\quad b_2=10^{k-1},
\quad m_1\ge4k+1.
}
\]

核心结论：

\[
\boxed{
 b_3=10^{\ell-1}
\text{ 对任意 }\ell\text{ 都不可能}.}
\]

因此第三分母必须真正偏离其十进制下端点；结合安全二进结构，得到统一第三尾斜率

\[
\boxed{
10^{\ell-2k}>8\cdot2^k.
}
\]

---

## 1. 通用 lower-end 参数

令

\[
\boxed{s=\ell-2k\ge1,}
\qquad
\boxed{S=10^s,}
\]

并继续记

\[
\boxed{x=10^k,}
\qquad
\boxed{R=10^{m_1-4k}.}
\]

若第三分母恰处在十进制下端点，则

\[
\boxed{
 b_3=10^{\ell-1}
=\frac{Sx^2}{10}.
}
\tag{1}
\]

写第三分子为

\[
\boxed{
 a_3=10^\ell-h=Sx^2-h,
\qquad h\ge1.}
\tag{2}
\]

因为 `b_3` 是纯 `2,5`-幂，而

\[
\gcd(a_3,b_3)=1,
\]

所以

\[
\boxed{\gcd(h,10)=1.}
\tag{3}
\]

特别地

\[
v_5(h)=0.
\]

---

## 2. 五进 unsaturated 再次强迫 `v_5(d)=k-1`

(1) 给出

\[
v_5(b_3)=\ell-1<\ell.
\]

所以当前必在五进 unsaturated side。

而

\[
v_5(b_2)=k-1.
\]

因为

\[
\ell-1=2k+s-1>k-1,
\]

安全五进 sieve 中 triple tie 与 prefix pair-max 都不可能，只能是第三块 unique max。

因此 denominator prime graph 强迫

\[
\boxed{v_5(b_1)=v_5(b_2)=k-1.}
\tag{4}
\]

写

\[
 b_1=10^{m_1}-d,
\qquad d\ge1.
\]

由于 `m_1>k`，模 `5^k` 可得

\[
\boxed{v_5(d)=k-1.}
\tag{5}
\]

---

## 3. 通用 exact-lift 多项式

使用

\[
 b_1=Rx^4-d,
\qquad
 a_1=10Rx^4+e,
\]

\[
 b_2=\frac{x}{10},
\qquad
 a_2=x^2-1,
\]

\[
 b_3=\frac{Sx^2}{10},
\qquad
 a_3=Sx^2-h.
\]

将 exact lift 平方并清分母，得到整数多项式

\[
\boxed{\Phi(x,R,S,d,e,h)=0.}
\tag{6}
\]

下面只使用它的 monomial 5-adic ledger。

---

## 4. 唯一最浅 monomial

`\Phi` 中存在 monomial

\[
\boxed{-200\,x^7S^2d^2h^2.}
\tag{7}
\]

由

\[
v_5(x)=k,
\quad
v_5(S)=s,
\quad
v_5(d)=k-1,
\quad
v_5(h)=0,
\]

其总赋值为

\[
2+7k+2s+2(k-1)
=
\boxed{9k+2s.}
\tag{8}
\]

对任意其他 monomial

\[
c\,x^{a_x}R^{a_R}S^{a_S}d^{a_d}e^{a_e}h^{a_h},
\]

符号审计严格给出 ledger

\[
\left(
 a_x+a_d,
 a_R,
 a_S,
 v_5(c)-a_d
\right)
\]

逐坐标满足

\[
\boxed{
 a_x+a_d\ge9,
\quad
 a_R\ge0,
\quad
 a_S\ge2,
\quad
 v_5(c)-a_d\ge0,
}
\tag{9}
\]

并且没有任何另一项同时取得

\[
(9,0,2,0).
\]

由于

\[
k,r,s\ge1,
\]

且 `v_5(e)\ge0`，(9) 表明所有其他项的总 5-adic 赋值都严格大于

\[
9k+2s.
\]

所以 (7) 是唯一最浅项。

一个整数和若为零，不可能只有唯一一项取得严格最小 `5`-进赋值。因此 (6) 无解。

得到

\[
\boxed{
 b_3=10^{\ell-1}
\text{ 在整个 second-repunit edge 上为空}.}
\tag{10}

---

## 5. 第三分母必须有正 excess

所以任意剩余候选都可写成

\[
\boxed{
 b_3=10^{\ell-1}+f,
\qquad f>0.}
\tag{11}

此前第三端点几何已给出

\[
\boxed{
0<f<\frac18\,10^{\ell-2k}.}
\tag{12}

---

## 6. 安全二进结构强迫 `2^k\mid f`

记

\[
e_3=v_2(b_3).
\]

基项

\[
10^{\ell-1}
\]

含有 `2^{\ell-1}`，而本边缘

\[
v_2(b_2)=k-1.
\]

考虑 `t_f=v_2(f)`。

- 若 `t_f<\ell-1`，则
  \[
  e_3=t_f<\ell.
  \]
  安全二进 dichotomy 强迫第三块 unique max，所以
  \[
  t_f=e_3>k-1,
  \]
  即 `t_f\ge k`；
- 若 `t_f\ge\ell-1`，由于
  \[
  \ell-1\ge2k\ge k,
  \]
  也自动有 `t_f\ge k`。

因此无论是否出现二进 cancellation：

\[
\boxed{v_2(f)\ge k,}
\]

即

\[
\boxed{2^k\mid f.}
\tag{13}

因为 `f>0`：

\[
\boxed{f\ge2^k.}
\tag{14}

---

## 7. 新的统一第三尾斜率

由 (12)、(14)：

\[
2^k
<
\frac18\,10^{\ell-2k}.
\]

所以

\[
\boxed{
10^{\ell-2k}>8\cdot2^k.}
\tag{15}

取常用对数：

\[
\boxed{
\ell
>
(2+\log_{10}2)k+\log_{10}8.
}
\tag{16}

数值上

\[
\boxed{
\ell>2.301029995\ldots\,k+0.903089986\ldots.}
\tag{17}

因此 second-repunit edge 的第三尾从原先的 slope `2` 进一步整体推到至少约 `2.30103`。

---

## 8. 与 escape cone 联立

此前还有

\[
\boxed{
 m_1\ge5k-3
\quad\text{或}\quad
\ell\ge3k-3.}
\]

现在再加上 (16)，得到该边缘的两条独立逃逸约束：

1. 第三尾无条件至少按 slope `2.30103` 增长；
2. 若第三尾没有达到 slope `3` 左右，则第一分母必须接近 slope `5` 增长。

所以 second-repunit edge 已经被压进一个很窄的双斜率逃逸区。

---

## 9. 符号证书

脚本：

`scripts/check_a1_repunit_lower_endpoint_5adic.py`

它验证 (7)–(9) 的有限符号 monomial 事实；`k,r,s` 都不做有限枚举。
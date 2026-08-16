# A1 split pair-max valuation ledger — 2026-08-16

本文继续 `a1-split-pairmax-hensel-lock-2026-08-16.md` 与 `a1-safe-vieta-factor-pair-2026-08-16.md`，把唯一 remaining odd prime-power routing exception 的局部赋值全部列清。

结论：对于 split pair-max，额外指数差 `d=E-e` 不进入 `N,K,V,F_\pm`；它只进入整数球面高度 `H` 与深度 `2d` 的 Gaussian Hensel congruence。

本文结论均为 **已严格完成**。

---

## 1. 第一种 pair-max

设

\[
\boxed{
e_1=e_3=E>e_2=e,}
\qquad
\boxed{d=E-e>0,}
\]

其中

\[
p\equiv1\pmod4,
\qquad p\ne5.
\]

由既约性：

\[
p\nmid a_1,
\qquad
p\nmid a_3.
\]

由 routing classification：

\[
\boxed{v_p(Q)=e,}
\qquad
\boxed{v_p(D)=e.}
\tag{1}
\]

并且

\[
\boxed{v_p(G)=E+e.}
\tag{2}
\]

---

## 2. `N` 的赋值没有 cancellation

记

\[
N=(a_1b_2)^2+(a_2b_1)^2.
\]

第一项满足

\[
v_p(a_1b_2)=e,
\]

第二项满足

\[
v_p(a_2b_1)\ge E.
\]

因为

\[
e<E,
\]

两平方项的 `p`-进赋值严格不同，所以不可能发生首项抵消。

因此

\[
\boxed{v_p(N)=2e.}
\tag{3}
\]

---

## 3. `K` 的赋值精确等于 `4e`

前缀缺口为

\[
K=G^2C^2-D^2N.
\]

由 (1)–(3)：

\[
v_p(D^2N)=2e+2e=4e.
\]

另一方面

\[
v_p(G^2C^2)
\ge2(E+e)
=4e+2d
>4e.
\]

所以两项赋值严格不同，得到

\[
\boxed{v_p(K)=4e.}
\tag{4}
\]

这个结论与 `v_p(C)` 无关。

---

## 4. normalized discriminant root 的赋值

沿用

\[
V^2=K-2\rho DN,
\qquad
\rho=\frac{b_3}{T}.
\]

因为 `p\ne2,5`：

\[
v_p(\rho)=v_p(b_3)=E.
\]

所以修正项满足

\[
v_p(2\rho DN)
=E+e+2e
=E+3e
=4e+d.
\]

它严格高于 `v_p(K)=4e`。

因此

\[
\boxed{v_p(V^2)=4e,}
\qquad
\boxed{v_p(V)=2e.}
\tag{5}
\]

---

## 5. Safe Vieta 两侧具有相同的精确公共深度

安全 Vieta 对为

\[
F_-=TGC-W,
\qquad
F_+=TGC+W,
\]

其中

\[
W=TV.
\]

因为 `p\nmid T`：

\[
\boxed{v_p(W)=2e.}
\tag{6}
\]

另一方面

\[
v_p(TGC)
=E+e+v_p(C)
\ge E+e
=2e+d
>2e.
\]

所以在 `TGC\pm W` 中，`W` 项严格低阶，不会抵消。

因此

\[
\boxed{
v_p(F_-)=v_p(F_+)=2e.
}
\tag{7}
\]

这与乘积公式一致：

\[
v_p(TDN(TD+2b_3))
=e+2e+e=4e.
\]

值得强调：异常深度 `d` 在 safe Vieta pair 中完全消失。

---

## 6. 原始 concatenation 恢复给出 `H` 的精确赋值

原 exact lift 的整数提升满足

\[
\boxed{q\alpha=H\beta.}
\tag{8}
\]

这里

\[
v_p(q)=E.
\]

又

\[
\beta=TD+b_3.
\]

两项赋值分别为

\[
v_p(TD)=e,
\qquad
v_p(b_3)=E.
\]

由于 `e<E`，没有 cancellation，所以

\[
\boxed{v_p(\beta)=e.}
\tag{9}
\]

对 (8) 取赋值：

\[
E+v_p(\alpha)
=v_p(H)+e.
\]

所以

\[
\boxed{
v_p(H)=d+v_p(\alpha).
}
\tag{10}
\]

前文只得到 `v_p(H)\ge d`；现在得到精确公式。

---

## 7. Gap integer `A` 是 `p`-进单位

在本 pair-max 中

\[
v_p(y_3)=0,
\qquad
v_p(H)\ge d>0.
\]

所以

\[
U=H-y_3
\]

是 `p`-进单位：

\[
\boxed{v_p(U)=0.}
\]

而

\[
U=LA,
\]

且 `p\nmid L`，故

\[
\boxed{v_p(A)=0.}
\tag{11}
\]

所以 safe contact gap

\[
\mathcal E=\tau A
\]

具有精确赋值

\[
\boxed{v_p(\mathcal E)=E.}
\tag{12}
\]

---

## 8. Hensel 深度与 `\alpha` 的关系

前文已经得到

\[
y_1^2+y_3^2\equiv0\pmod{p^{2d}}.
\]

现在由 (10) 可进一步解释：

- 若 `p\nmid\alpha`，则
  \[
  v_p(H)=d;
  \]
- 若 `p\mid\alpha`，则
  \[
  v_p(H)>d.
  \]

而 `y_2` 的赋值恰为 `d`。因此若 `p\mid\alpha`，

\[
H^2-y_2^2
\]

的赋值恰为 `2d`，从而

\[
\boxed{
v_p(y_1^2+y_3^2)=2d
\qquad(p\mid\alpha).
}
\tag{13}
\]

也就是说，在 `p\mid\alpha` 子支中，`-1` Hensel congruence 的深度甚至是**精确** `2d`，不能继续提高。

---

## 9. 第二种 pair-max

若

\[
e_2=e_3=E>e_1=e,
\]

全部结论交换下标 `1,2` 后保持不变：

\[
\boxed{v_p(N)=2e,}
\]

\[
\boxed{v_p(K)=4e,}
\]

\[
\boxed{v_p(V)=2e,}
\]

\[
\boxed{v_p(F_-)=v_p(F_+)=2e,}
\]

\[
\boxed{v_p(H)=d+v_p(\alpha),}
\]

\[
\boxed{v_p(A)=0.}
\]

并且在 `p\mid\alpha` 时

\[
\boxed{v_p(y_2^2+y_3^2)=2d.}
\]

---

## 10. 当前局部核心

split pair-max 的局部自由度现在只剩：

1. Gaussian split prime `p\equiv1 mod4`；
2. 指数差 `d=E-e>0`；
3. 指定 unit ratio 在 `p^{2d}` 上实现 `\sqrt{-1}`；
4. full concatenated numerator `\alpha` 是否被 `p` 整除。

其余关键对象 `N,K,V,F_\pm,A,H` 的赋值已经全部由 `(e,d,v_p(\alpha))` 精确决定。

所以后续若继续攻击 odd exception，只需寻找一个与 `\alpha` 或指定 `\sqrt{-1}` root 不兼容的十进制同余；无需再保留额外局部赋值分支。
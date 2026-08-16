# A1 decimal-shift congruence — 2026-08-16

本文构造一个旧 A1 主线一直缺少的 `decimal-shift` 敏感对象。它直接在真实第三分母块长度

\[
10^{m_3}=10^{g+\ell}
\]

处截断原始平方恒等式，因此显式看到第二分子 `a_2` 的最后 `g` 位。

这条同余不使用 Gaussian flip，也不使用有问题的 `a_3/\delta_3` 正规化。

本文所有等式与同余均为 **已严格完成**；最后的攻关方向仍标为待证。

---

## 1. 基本记号

沿用

\[
T=10^\ell,
\qquad
D=10^gQ,
\]

\[
C=a_1 10^{n_2}+a_2,
\qquad
G=b_1b_2,
\]

\[
N=(a_1b_2)^2+(a_2b_1)^2.
\]

第三块仍记

\[
a=a_3,
\qquad b=b_3.
\]

原始 exact lift 的平方恒等式为

\[
\boxed{
G^2b^2(TC+a)^2
=(TD+b)^2(Nb^2+G^2a^2).
}
\tag{1}
\]

由 `a1-direct-padics-tail-collapse-2026-08-16.md` 已严格得到

\[
\boxed{T\mid Nb^4.}
\tag{2}
\]

---

## 2. 第二分子的 `g` 位 suffix

当 `g\ge1` 时定义

\[
\boxed{c_g:=a_2\bmod 10^g,
\qquad 0\le c_g<10^g.}
\tag{3}
\]

因为

\[
n_2=m_2+k+g>g,
\]

所以

\[
a_1 10^{n_2}\equiv0\pmod{10^g},
\]

从而

\[
\boxed{C\equiv c_g\pmod{10^g}.}
\tag{4}
\]

也就是说，在第三分母真实块长处，prefix numerator 唯一可见的 `g`-层信息就是 `a_2` 的最后 `g` 位。

---

## 3. 在真实第三分母块长处截断

注意

\[
TD=10^\ell 10^gQ=10^{g+\ell}Q.
\]

令

\[
M_3=10^{g+\ell}=10^gT.
\]

则

\[
TD+b\equiv b\pmod{M_3}.
\]

另一方面

\[
TC+a
\equiv
Tc_g+a
\pmod{M_3},
\]

因为把 `C` 改变 `10^g` 的倍数后，乘以 `T` 恰好改变 `M_3` 的倍数。

所以 (1) 模 `M_3` 给出

\[
G^2b^2(Tc_g+a)^2
\equiv
b^2(Nb^2+G^2a^2)
\pmod{10^gT}.
\]

消去两边公共的 `G^2a^2b^2` 项：

\[
\boxed{
10^gT
\mid
b^2\left(
2TG^2ac_g
+T^2G^2c_g^2
-Nb^2
\right).
}
\tag{5}
\]

这就是第一条 decimal-shift congruence。

---

## 4. 除去已经知道的 `T` 深度

由 (2)，

\[
\frac{Nb^4}{T}\in\mathbf Z.
\]

而 (5) 中整个被除数可以写成

\[
T\left(
2G^2ab^2c_g
+TG^2b^2c_g^2
-\frac{Nb^4}{T}
\right).
\]

所以 (5) 等价于纯 `g`-层整数同余

\[
\boxed{
\frac{Nb^4}{T}
\equiv
2G^2ab^2c_g
+TG^2b^2c_g^2
\pmod{10^g}.
}
\tag{6}
\]

这条公式的关键意义是：`\ell` 的公共十进制深度已经完全除去，剩下模数只剩真正的 decimal shift `10^g`。

---

## 5. 当 `ell >= g` 时的主同余

若

\[
\ell\ge g,
\]

则

\[
T=10^\ell\equiv0\pmod{10^g}.
\]

因此 (6) 简化为

\[
\boxed{
\frac{Nb_3^4}{10^\ell}
\equiv
2G^2a_3b_3^2c_g
\pmod{10^g},
\qquad
c_g=a_2\bmod10^g.
}
\tag{7}
\]

这正是一个同时对 `2`、`5` 和 `g` 敏感的 prefix-tail 接触式。

---

## 6. `c_g=0` 的全零 suffix 支

若

\[
10^g\mid a_2,
\]

则

\[
c_g=0.
\]

由 (6)（不需要 `\ell\ge g`，因为两项都含 `c_g`）直接得到

\[
\boxed{
10^g\mid\frac{Nb_3^4}{T}.
}
\]

即

\[
\boxed{
10^{g+\ell}\mid Nb_3^4.
}
\tag{8}
\]

这比 universal trailing-block 条件

\[
10^\ell\mid Nb_3^4
\]

整整多出 `g` 层十进制深度。

同时，因为

\[
\gcd(a_2,b_2)=1,
\]

若 `10^g\mid a_2` 且 `g\ge1`，则

\[
\boxed{\gcd(b_2,10)=1.}
\tag{9}
\]

所以全零 suffix 支还自动把第二分母送入 `2/5`-单位支。

---

## 7. 逐素数的 shift-resonance 接口

固定

\[
p\in\{2,5\}.
\]

记

\[
e=v_p(b_3),
\quad
\gamma=v_p(G),
\quad
n=v_p(N),
\quad
c=v_p(c_g),
\]

并约定 `c=+\infty` 当 `c_g=0`。

在 `\ell\ge g` 且 `c_g\ne0` 时，(7) 比较的是两个整数：

左边赋值

\[
\boxed{n+4e-\ell,}
\tag{10}
\]

右边赋值

\[
\boxed{v_p(2)+2\gamma+v_p(a_3)+2e+c.}
\tag{11}
\]

若这两个赋值不同且其中较小者 `<g`，则两边不可能模 `p^g` 同余。因此任何候选都必须满足以下三种状态之一：

1. **左侧低位与右侧低位精确相等**；
2. **两侧赋值都至少为 `g`**；
3. **相等赋值后发生更高阶 `p`-进抵消**。

特别地，若 `p\mid b_3`，则 `gcd(a_3,b_3)=1` 给出

\[
v_p(a_3)=0,
\]

于是非深区的必要线性关系简化为

\[
\boxed{
n+4e-\ell
=v_p(2)+2\gamma+2e+c,
}
\]

即

\[
\boxed{
2e
=\ell+v_p(2)+2\gamma+c-n.
}
\tag{12}
\]

这是一条新的 **decimal-shift resonance**：它不是旧判别平方中的 tail resonance，而是由真实 block boundary `10^{m_3}` 产生，并显式依赖 `a_2` 的 suffix 深度 `c=v_p(c_g)`。

---

## 8. 当前攻关方向

(6)–(12) 已经提供 archive 中曾经要求、但旧 A1 没有得到的 `decimal-shift` 敏感不变量。

下一步应按 `p=2,5` 同时研究：

- `c_g=0`：使用 (8) 的额外 `g` 层整除与 `gcd(b_2,10)=1`；
- `0\le v_p(c_g)<g`：使用 (12) 把第三分母赋值锁到 `\ell`、`G,N` 与 suffix 深度；
- `v_p(c_g)\ge g`：回到全零/深 suffix 支；
- 把二进与五进的两条 shift-resonance 同时代入 decade window 与 direct tail cap，寻找 prefix-uniform 高度矛盾。

这些后续排除尚为 **待证**；本文已经完成的是新的 exact congruence 与其必要赋值分层。

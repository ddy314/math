# A1 exact decimal-height synchronization

> 日期：2026-08-22。依赖 [`global-squarefree-terminal.md`](global-squarefree-terminal.md) 的 `kappa` square terminal 与 `(L,M)` recovery。
>
> 目的：把“第三分子/第三分母能否真的是同一个十进制 block”改写成一个只涉及形式根 `x_sigma` 的 **精确 2/5-adic height synchronization**。本文覆盖整个 A1 四层，不限 minimal diagonal。

状态：**本文定理已严格完成。A1 全局空性仍待证明所有形式根都违反本文 criterion。**

---

## 1. 归一化第三分子

沿用

\[
Q=b_1 10^{m_2}+b_2,
\qquad
G=b_1b_2,
\qquad
D=10^gQ,
\]

以及整数 `kappa,W`：

\[
QG<\kappa\le10QG,
\]

\[
\boxed{
\kappa\bigl(\kappa K-2GD^2N\bigr)=W^2.
}
\tag{1}
\]

令

\[
h=\gcd(\kappa,10^gQG),
\qquad
L=\frac\kappa h,
\qquad
M=\frac{10^gQG}{h}.
\tag{2}
\]

真正 A1 candidate 必须满足

\[
L=2^{\ell_2}5^{\ell_5},
\qquad
\gcd(L,M)=1,
\]

以及

\[
10^{g-1}\le \frac ML<10^g.
\tag{3}
\]

形式第三根为

\[
r_\sigma
=
\frac{
\kappa G^2C+\sigma(\kappa+G)W
}{
\kappa DG(\kappa+2G)
},
\qquad \sigma\in\{+1,-1\}.
\tag{4}
\]

定义归一化第三分子

\[
\boxed{
 x_\sigma
 :=
 \frac{10^gQG}{\kappa}r_\sigma.
}
\tag{5}
\]

由 `D=10^gQ`，(4) 立刻化为

\[
\boxed{
 x_\sigma
 =
 \frac{X_\sigma}{Y},
}
\tag{6}
\]

其中

\[
\boxed{
X_\sigma
=
\kappa G^2C+\sigma(\kappa+G)W,
}
\tag{7}
\]

\[
\boxed{
Y=\kappa^2(\kappa+2G).
}
\tag{8}
\]

关键点是：若候选真的来自第三块，则

\[
10^n=\omega L,
\qquad
b_3=\omega M,
\qquad
r_3=\frac{a_3}{b_3},
\]

所以

\[
\frac{10^gQG}{\kappa}
=\frac ML,
\]

从而

\[
\boxed{
 x_\sigma=\frac{a_3}{10^n}.
}
\tag{9}
\]

因此第三分子的位数条件恰好是

\[
\boxed{
\frac1{10}\le x_\sigma<1.
}
\tag{10}
\]

这把原来的“`a_3` 是 `n` 位整数”完全归一化掉了。

---

## 2. reduced decimal data

把正的形式根 (6) 约成最简分数

\[
\boxed{
 x_\sigma=\frac uv,
 \qquad
 \gcd(u,v)=1.
}
\tag{11}
\]

若 `v` 只含 `2,5`，写

\[
d_2=v_2(v),
\qquad
d_5=v_5(v).
\tag{12}
\]

同时写

\[
\ell_2=v_2(L),
\qquad
\ell_5=v_5(L).
\tag{13}
\]

定义两个 decimal completion heights

\[
\boxed{
H_2=\max(d_2,\ell_2),
\qquad
H_5=\max(d_5,\ell_5).
}
\tag{14}
\]

再令

\[
M_{10'}=rac{M}{2^{v_2(M)}5^{v_5(M)}}.
\tag{15}
\]

---

## 3. exact recovery theorem

### 定理 A1-DH

固定一个通过 `kappa` square terminal 的正形式根 `x_sigma=u/v`。它能恢复成某个合法第三 block

\[
(a_3,b_3,n),
\qquad
n=n_3\ge1,
\]

**当且仅当**以下四个条件同时成立：

1. 正确的第三分子窗口：
   \[
   \boxed{\frac1{10}\le\frac uv<1;}
   \tag{16}
   \]
2. `x_sigma` 是有限十进制数：
   \[
   \boxed{v=2^{d_2}5^{d_5};}
   \tag{17}
   \]
3. 两个 decimal completion heights 精确同步：
   \[
   \boxed{
   H_2=H_5=:n\ge1;
   }
   \tag{18}
   \]
4. reduced numerator 与 `M` 的非十进制部分互素：
   \[
   \boxed{
   \gcd(u,M_{10'})=1.
   }
   \tag{19}
   \]

若这些条件成立，则第三块被唯一恢复为

\[
\boxed{
 a_3=10^n\frac uv,
 \qquad
 b_3=10^n\frac ML.
}
\tag{20}
\]

### 证明：必要性

若真实第三块存在，由 (9)

\[
x_\sigma=\frac{a_3}{10^n}.
\]

因为 `a_3` 恰有 `n` 位，立即得到 (16)。把该分数约到最简后，分母只能来自 `10^n`，故得到 (17)。

又

\[
10^n=\omega L,
\]

所以 `L|10^n`，即

\[
\ell_2,\ell_5\le n.
\]

同理最简分母 `v|10^n`，故

\[
d_2,d_5\le n.
\]

固定 `p in {2,5}`。若

\[
n>\max(d_p,\ell_p),
\]

则在

\[
a_3=10^n u/v,
\qquad
b_3=10^n M/L
\]

中，`a_3` 与 `b_3` 都至少含一个因子 `p`：

- `a_3` 的 `p`-赋值至少为 `n-d_p>0`；
- `b_3` 的 `p`-赋值为
  \[
  n+v_p(M)-\ell_p>0.
  \]

这与原问题的

\[
\gcd(a_3,b_3)=1
\]

矛盾。因此

\[
n=\max(d_p,\ell_p)
\]

对 `p=2,5` 同时成立，得到 (18)。

最后，对任意奇素数 `p !=5` 且 `p|M_{10'}`，由于 `10^n/v` 只有 `2,5` 素因子，

\[
p|a_3
\Longleftrightarrow
p|u.
\]

而 `p|b_3`。既约性迫使 `p not|u`。对所有这类素数合并即得 (19)。

### 证明：充分性

反过来假设 (16)--(19)。令共同高度

\[
n=H_2=H_5\ge1
\]

并按 (20) 定义 `a_3,b_3`。

由

\[
d_p\le n,
\qquad
\ell_p\le n
\]

对 `p=2,5` 成立，且 `v,L` 都是 `2,5`-smooth，可知

\[
v|10^n,
\qquad
L|10^n.
\]

所以 (20) 中 `a_3,b_3` 都是正整数。

由 (16)：

\[
10^{n-1}\le a_3<10^n,
\]

故 `a_3` 恰有 `n` 位。

由 slope window (3)：

\[
10^{n+g-1}
\le b_3
<10^{n+g},
\]

故 `b_3` 恰有 `n+g=m_3` 位。

现在验证既约性。对 `p notin {2,5}`，(19) 保证 `a_3,b_3` 没有公共素因子。

对 `p in {2,5}`，记

\[
d=d_p,
\quad \ell=\ell_p,
\quad m=v_p(M).
\]

因为 `(L,M)=1`，有

\[
\min(\ell,m)=0.
\]

又由 (18)

\[
n=\max(d,\ell).
\]

- 若 `n=ell`，则 `ell>0` 时必有 `m=0`，于是
  \[
  v_p(b_3)=n+m-\ell=0;
  \]
- 若 `n=d>ell`，则 `d>0`，由 `(u,v)=1` 有 `p not|u`，于是
  \[
  v_p(a_3)=n-d=0.
  \]

两种情形至少一侧为 `p`-进单位，所以 `p` 也不进入 gcd。故

\[
\gcd(a_3,b_3)=1.
\]

最后 (5)、(9) 给

\[
r_\sigma
=\frac LM x_\sigma
=\frac{a_3}{b_3},
\]

而 `r_sigma` 已由 `kappa` square terminal 满足 rational contact quadratic；因此恢复出的第三块正是当前 prefix、`kappa` 的合法 A1 第三块。证毕。

---

## 4. raw valuation form

计算时无需先真的构造最简分数。令

\[
X_\sigma
=
\kappa G^2C+\sigma(\kappa+G)W,
\qquad
Y=\kappa^2(\kappa+2G).
\]

则约分后 `v` 的 `p`-指数为

\[
\boxed{
 d_p
 =
 \max\bigl(0,
 v_p(Y)-v_p(X_\sigma)
 \bigr),
 \qquad p=2,5.
}
\tag{21}
\]

因此真正需要证明的 2/5 terminal incompatibility 已经变成

\[
\boxed{
\max\!\left(
\max(0,v_2(Y)-v_2(X_\sigma)),
 v_2(L)
\right)
\ne
\max\!\left(
\max(0,v_5(Y)-v_5(X_\sigma)),
 v_5(L)
\right)
}
\tag{22}
\]

或在高度偶然相等时，再由 non-decimal denominator / (19) 排除。

这是一条逐素数可核验的目标式，正好替代早期预印本中没有定量内容的 “two gaps / scale incompatibility”。

---

## 5. 当前 closure target

整个 A1 的第三块现在可以完全删除。对每个 moving prefix 与

\[
QG<\kappa\le10QG
\]

只需：

1. 检查 `kappa( kappa K-2GD^2N )` 是否平方；
2. 恢复 `L,M`；
3. 对两个 `sigma` 计算 `X_sigma/Y`；
4. 证明至少有一项失败：
   - `x_sigma` 不在 `[1/10,1)`；
   - reduced denominator 含非 `2,5` 素数；
   - `H_2 != H_5`；
   - `gcd(u,M_10')>1`。

因此 A1 全局关闭已经被压成一个明确的 prefix-uniform local-height problem，而不再含任何自由第三尾参数。

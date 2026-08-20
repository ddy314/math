# A1 minimal diagonal short-tail saturation collapse

> 日期：2026-08-19。本文继续 `near-integer-tail.md`，研究仍未关闭的 minimal diagonal
> \[
> d=2,\qquad r=s=1,\qquad k=g\ge4.
> \]
> 记第三分子位数为
> \[
> \ell=n_3.
> \]

核心结论：

\[
\boxed{
\ell\le k-2
\Longrightarrow
10^\ell\mid b_3.
}
\]

因此所有 non-saturated 候选都必须满足

\[
\boxed{\ell\ge k-1.}
\]

并且第一条非饱和边界 `ell=k-1` 只剩七个显式整数 residual。

状态：**已严格完成。**

---

## 1. 把 near-integer gap 清成整数

沿用 near-integer theorem，令

\[
N=j-10^k+1\in\mathbb Z,
\qquad
\rho=\frac{b_3}{10^\ell}.
\]

对全部 `k>=3` 已证明

\[
\boxed{
-17.425\,10^{-k}
<N-\rho
<50.45\,10^{-k}.
}
\tag{1}
\]

乘以 `10^ell`。定义

\[
\boxed{
 t:=N10^\ell-b_3\in\mathbb Z.
}
\tag{2}
\]

则 (1) 精确变成

\[
\boxed{
-17.425\,10^{\ell-k}
<t
<50.45\,10^{\ell-k}.
}
\tag{3}
\]

关键变化是：连续误差现在夹住的是一个整数 `t`。

---

## 2. `ell<=k-2` 时 residual 只能为零

若

\[
\ell\le k-2,
\]

则

\[
10^{\ell-k}\le10^{-2}.
\]

所以 (3) 给出

\[
-0.17425<t<0.5045.
\]

区间中唯一整数是 `0`。因此

\[
\boxed{t=0.}
\tag{4}
\]

由定义 (2)：

\[
\boxed{
b_3=N10^\ell.}
\tag{5}
\]

故

\[
\boxed{10^\ell\mid b_3.}
\tag{6}
\]

这正是 `rational-contact.md` 中 saturated `L=1` 分支的定义。

于是得到统一结论

\[
\boxed{
\ell\le k-2
\Longrightarrow
L=1.
}
\tag{7}
\]

等价地，任何 non-saturated minimal-diagonal candidate 必须满足

\[
\boxed{
\ell\ge k-1.
}
\tag{8}
\]

这把第三块原先完全自由增长的位数参数第一次与 prefix 参数 `k` 直接绑定。

---

## 3. short-tail saturated sector 中 `tau` 被 prefix 精确决定

saturated 分支写成

\[
b_3=10^\ell\tau.
\]

由 (5) 立刻得到

\[
\boxed{
\tau=N=j-10^k+1.
}
\tag{9}
\]

而第三分母必须恰有 `m_3=k+ell` 位，所以

\[
10^{k-1}\le\tau<10^k.
\]

因此在 short-tail sector 中自动有

\[
\boxed{
10^{k-1}
\le j-10^k+1
<10^k.
}
\tag{10}
\]

也就是说 saturated 参数 `tau` 不再是独立自由变量，它就是 moving-prefix remainder `j` 的一个固定线性平移。

此外

\[
\theta=\frac{b_3}{10^\ell D}
=rac\tau D
=rac{j-10^k+1}{D},
\tag{11}
\]

因此 `theta` 同时完全脱离 `ell`。

这与旧 saturated rational-contact reduction 正好对接：固定 `(k,z,w,j)` 后，整个 contact quadratic 已经与第三块位数 `ell` 无关。

---

## 4. 第一条非饱和边界 `ell=k-1` 只有七个 residual

现在取

\[
\ell=k-1.
\]

由 (3)：

\[
-1.7425<t<5.045.
\]

所以

\[
\boxed{
 t\in\{-1,0,1,2,3,4,5\}.
}
\tag{12}
\]

因此

\[
\boxed{
 b_3=N10^{k-1}-t,
\qquad
t\in\{-1,0,1,2,3,4,5\}.
}
\tag{13}
\]

`t=0` 仍是 saturated；所有真正 non-saturated 的 `ell=k-1` 状态只剩六个非零 residual。

---

## 5. `ell=k-1` 非饱和状态的 `2/5` 指数被精确锁定

设 `t!=0` 且 `ell=k-1`。因为

\[
b_3=N10^\ell-t,
\]

有

\[
\gcd(b_3,10^\ell)=\gcd(t,10^\ell).
\]

所以既约正规化

\[
\rho=\frac{b_3}{10^\ell}
\]

的分母恰为

\[
\frac{10^\ell}{\gcd(t,10^\ell)}.
\]

写

\[
\rho=h2^x5^y,
\qquad
\gcd(h,10)=1.
\]

因为 `|t|<=5` 且 `ell=k-1>=3`，可直接得到

\[
\boxed{
 x=-(k-1-v_2(t)),
\qquad
 y=-(k-1-v_5(t)).
}
\tag{14}
\]

因此六个 nonzero residual 对应：

| `t` | `x` | `y` |
|---:|---:|---:|
| `-1` | `-(k-1)` | `-(k-1)` |
| `1` | `-(k-1)` | `-(k-1)` |
| `2` | `-(k-2)` | `-(k-1)` |
| `3` | `-(k-1)` | `-(k-1)` |
| `4` | `-(k-3)` | `-(k-1)` |
| `5` | `-(k-1)` | `-(k-2)` |

所以在第一条非饱和位数边界上，原本二维自由的 `(x,y)` 已完全消失：只剩由一个六值 residual `t` 决定的六条显式 valuation patterns。

---

## 6. 对 `k>=4` 前沿的结构性分裂

结合本文，尚未关闭的 minimal diagonal 可以严格分成：

### A. saturated short-tail sector

\[
\boxed{
\ell\le k-2,
\qquad
b_3=10^\ell(j-10^k+1),
}
\]

其中 `theta=(j-10^k+1)/D` 与 `ell` 无关。

### B. first nonsaturated boundary

\[
\boxed{
\ell=k-1,
}
\]

其中非饱和状态只有

\[
t\in\{-1,1,2,3,4,5\}
\]

及表 (14) 的六个精确 `(x,y)` patterns。

### C. genuinely long tail

\[
\boxed{
\ell\ge k.
}
\]

只有这一部分仍保留较大的 residual 自由度。

因此后续证明不应继续把 `ell` 当作完全无结构的无限参数。新的自然顺序是：先关闭 A，再关闭 B，最后研究 `ell>=k` 的长尾。

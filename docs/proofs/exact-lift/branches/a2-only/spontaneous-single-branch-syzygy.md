# A2 single-branch 上的 `C_*` 精确线性分解

> **依赖：** `spontaneous-single-branch.md`、`spontaneous-prefix-branch-audit.md`。
>
> **严格状态：**本文证明 branch-collision/central kernel `C_*` 在任意一个 compact single branch 上自身分解成两个线性 length/orientation 因子。由此得到一个关键分离：noncentral repeated root 自动满足 `C_*≠0`；若 repeated root 与 `C_*` 同时接触，则必回到 central line `2K-9=0`。同时得到 repeated-root 的精确 square-class law。本文仍**不宣称 A2 全局关闭**。

---

## 1. compact branch

沿用

\[
\tau=10^{-M},
\qquad
s=9+y,
\]

\[
c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2},
\]

以及任意一个有限 sphere orientation

\[
z=z_i.
\]

`spontaneous-single-branch.md` 的 branch quadratic 为

\[
\boxed{
\mathscr L(\tau,z)
=55\tau^2+18(z-s)\tau+s^2-4sz-c.
}
\tag{1.1}

central kernel 记为

\[
\boxed{
\begin{aligned}
C_*={}&164025x^4+656100x^3
+2381x^2y^2+41400x^2y\\
&+842400x^2+324xy^2+324y^2.
\end{aligned}}
\tag{1.2}

---

## 2. `已严格完成`：`C_*` 模 branch quadratic 完全线性化

直接展开并按 `tau` 对 (1.1) 做 Euclidean division，得到精确恒等式

\[
\boxed{
\begin{aligned}
C_*={}&100x^2(9\tau-2s)
(495\tau+162z-52s)\\
&-8100x^2\mathscr L(\tau,z).
\end{aligned}}
\tag{2.1}

因此在任意真实 branch root

\[
\mathscr L(\tau,z_i)=0
\]
上：

\[
\boxed{
C_*
=100x^2(9\tau-2s)
(495\tau+162z_i-52s).
}
\tag{2.2}

第一因子与旧 central line 精确相同。因为

\[
K=\frac{s}{\tau},
\]
所以

\[
2K-9
=\frac{2s-9\tau}{\tau}.
\tag{2.3}

故

\[
\boxed{9\tau-2s=0\iff2K-9=0.}
\tag{2.4}

这说明 `C_*` 在 single branch 上并不是新的高次自由对象；它就是 central factor 乘另一个线性 orientation factor。

---

## 3. `已严格完成`：repeated root 与 `C_*` 相交必回 central

single branch 的 repeated-root tangent 为

\[
\boxed{55\tau=9(s-z).}
\tag{3.1}

定义

\[
U:=81z+29s.
\tag{3.2}

在 (3.1) 下：

\[
9\tau-2s
=-\frac{U}{55},
\tag{3.3}

而第二线性因子变成

\[
495\tau+162z-52s
=U.
\tag{3.4}

所以 (2.2) 精确退化为

\[
\boxed{
C_*=-\frac{20}{11}x^2U^2.
}
\tag{3.5}

若 genuine prime 满足

\[
p\ne2,5,11,
\qquad p\nmid x,
\]
并且 repeated root 同时有

\[
p\mid C_*,
\]
则 (3.5) 强迫

\[
U\equiv0\pmod p.
\]
再由 (3.3)：

\[
9\tau-2s\equiv0,
\]
即

\[
\boxed{
\text{repeated root}+C_*=0
\Longrightarrow
2K-9=0.
}
\tag{3.6}

因此：

\[
\boxed{
\text{noncentral single-branch repeated root}
\Longrightarrow C_*\ne0.
}
\tag{3.7}

这把 central bad reduction 与真正 moving singular branch 严格分离。

---

## 4. `已严格完成`：repeated-root 的 `C_*` square class

在 (3.5) 且 `C_*` 为单位时，对 odd prime `p` 取 Legendre symbol。因为 `x^2`、`4` 是平方，且 inverse 与原数有相同 quadratic character：

\[
\left(\frac{11^{-1}}p\right)
=\left(\frac{11}p\right),
\]
故

\[
\boxed{
\left(\frac{C_*}{p}\right)
=
\left(\frac{-55}{p}\right).
}
\tag{4.1}

对本文关心的 inert prime

\[
p\equiv3\pmod4,
\]
进一步有

\[
\boxed{
\left(\frac{C_*}{p}\right)
=-\left(\frac{55}{p}\right).
}
\tag{4.2}

特别地，若同一个 singular prime 还属于 external discriminant-zero 子通道，旧条件给

\[
\left(\frac{55}{p}\right)=1,
\]
于是

\[
\boxed{
\left(\frac{C_*}{p}\right)=-1.
}
\tag{4.3}

这是一条严格 necessary character，而不是 closure。当前没有独立证明 external singular branch 上 `C_*` 必为平方，所以 (4.3) 不能单独宣称矛盾。

---

## 5. 同一个 identity 也解释 compact discriminant

`spontaneous-single-branch.md` 的 discriminant 为

\[
\mathscr D
=324z^2+232sz+104s^2+220c.
\]
它还有等价形式

\[
\boxed{
405x^2\mathscr D
=20x^2(81z+29s)^2+11C_*.
}
\tag{5.1}

证明只需把

\[
23s^2+81c
\]
化简：

\[
\boxed{
23s^2+81c=\frac{C_*}{100x^2}.
}
\tag{5.2}

而 quadratic 在自己的根 `tau` 处满足

\[
\mathscr D=(\mathscr L'(\tau))^2.
\]
把这一平方关系代入 (5.1) 并因式分解，正好恢复 (2.2)。所以

- compact discriminant；
- central kernel `C_*`；
- branch tangent；
- branch collision

其实是同一个二次几何的不同投影，不能重复计作四个独立 obstruction。

---

## 6. 当前开放核

本文件把 single-branch singularity 进一步收紧成：

\[
\boxed{
\begin{gathered}
\mathscr L_i(10^{-M})\equiv0,\\
55\cdot10^{-M}\equiv9(s-z_i),\\
C_*\ne0,\\
\left(\frac{C_*}{p}\right)=\left(\frac{-55}{p}\right)
\end{gathered}}
\]
对 noncentral repeated root 成立。

所以下一步若继续处理 singular moving prime，最值得找的不是另一个 branch discriminant，而是 `C_*` 的**独立** square class / source meaning；若无法独立固定它，则 character route应降级，转去清分母 tangent 与 decimal multiplicative orbit 的 prime-power 同步。

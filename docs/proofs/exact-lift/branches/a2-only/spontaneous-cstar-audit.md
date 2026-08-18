# A2 `C_*` 的原始 decimal 形式与 external character 降级

> **依赖：** `spontaneous-single-branch-syzygy.md`、`decimal-prefix-bridge.md`、`external-secant-center.md`。
>
> **严格状态：**本文把 pure-prefix kernel `C_*` 乘回原始 decimal integers，并证明 single-branch repeated-root 导出的 character `(C_*/p)=(-55/p)` 在 external double-root/prefix-norm 子通道中已经由旧中心条件自动成立。因此该 character 不是新的独立 obstruction，必须降级，不能重复收费。本文仍**不宣称 A2 全局关闭**。

---

## 1. `C_*` 的 source-free 原始整数形式

记

\[
N=10^M,
\qquad A=a_2,
\qquad B=b_2,
\]

\[
Q=2N+B,
\qquad K=9N+10A,
\]

\[
N_0=\left(\frac{9B}{2}\right)^2+A^2.
\]

scale-free variables 为

\[
x=B/N,
\qquad y=10A/N.
\]

`spontaneous-prefix-eliminant.md` 定义

\[
\begin{aligned}
C_*={}&164025x^4+656100x^3
+2381x^2y^2+41400x^2y\\
&+842400x^2+324xy^2+324y^2.
\end{aligned}
\]

定义原始整数

\[
\boxed{
\mathcal C_*^{\rm int}
:=23B^2K^2+81Q^2N_0.
}
\tag{1.1}

直接代入 `x,y`：

\[
\boxed{
N^4C_*=100\mathcal C_*^{\rm int}.
}
\tag{1.2}

因为 external / spontaneous prime 与 `2,5,N` 分离，所以 `100/N^4` 是模 `p` 的平方。因此

\[
\boxed{
\left(\frac{C_*}{p}\right)
=
\left(\frac{\mathcal C_*^{\rm int}}p\right)
}
\tag{1.3}

只要两边都是单位。

(1.1) 也给出一个几何解释：

\[
\mathcal C_*^{\rm int}
=23(BK)^2
+(9QC_0)^2+(9QA)^2,
\qquad C_0=9B/2.
\tag{1.4}

所以 `C_*` 是一个 `Gaussian norm + 23 square` 的正三元型，而不是无来源的 resultant 系数。

---

## 2. `已严格完成`：`C_*` 与 external prefix norm 的精确桥

`decimal-prefix-bridge.md` 定义

\[
\boxed{
\mathscr R_N
=324Q^2N_0+2695B^2.
}
\tag{2.1}

由 (1.1)：

\[
4\mathcal C_*^{\rm int}
=92B^2K^2+324Q^2N_0.
\]
所以

\[
\boxed{
4\mathcal C_*^{\rm int}
=
\mathscr R_N+B^2(92K^2-2695).
}
\tag{2.2}

这把 single-branch central kernel 直接接回此前 external double-root 的 prefix norm target。

---

## 3. `已严格完成`：external center 自动固定 `C_*` 的 character

external discriminant-zero common-height center 已给

\[
18K-55\equiv0\pmod p,
\qquad
\mathscr R_N\equiv0\pmod p.
\tag{3.1}

所以

\[
K\equiv\frac{55}{18}.
\]
代入 (2.2)：

\[
\begin{aligned}
\mathcal C_*^{\rm int}
&\equiv
\frac{B^2}{4}
\left(92\frac{55^2}{18^2}-2695\right)\\
&=
-\frac{37180}{81}B^2.
\end{aligned}
\]

即

\[
\boxed{
\mathcal C_*^{\rm int}
\equiv
-\frac{4\cdot5\cdot11\cdot13^2}{9^2}B^2
\pmod p.
}
\tag{3.2}

对于 `p∤2·3·5·11·13·B`：

\[
\boxed{
\left(\frac{C_*}{p}\right)
=
\left(\frac{-55}{p}\right).
}
\tag{3.3}

因此如果 `p≡3 (mod 4)` 且 external discriminant-zero 还给

\[
\left(\frac{55}{p}\right)=1,
\]
则自动有

\[
\boxed{
\left(\frac{C_*}{p}\right)=-1.
}
\tag{3.4}

---

## 4. `已严格完成 / 降级`：repeated-root character 是旧中心的影子

`spontaneous-single-branch-syzygy.md` 独立从 repeated tangent 推出

\[
\left(\frac{C_*}{p}\right)
=
\left(\frac{-55}{p}\right).
\tag{4.1}

但 §3 证明：一旦同一个 prime 还处于 external double-root + prefix-norm center，(4.1) **在考虑 repeated root 之前就已经成立**。

所以 external singular 子通道中：

\[
\boxed{
\text{single-branch repeated character}
=\text{external center character shadow}.}
\tag{4.2}

它不能被当成第二个独立 Legendre obstruction，更不能用“external 要 `(55/p)=1`，repeated 要 `C_*` nonsquare”制造伪矛盾；external center 本身已经要求 `C_*` nonsquare。

这与此前多次 `-23` / principal-square character 降级现象一致：真正要继续推进 external singular branch，必须使用 prime-power depth、decimal orbit 或 natural representative，而不是再堆一个等价的 quadratic character。

---

## 5. 当前结论

`C_*` 现在有三重统一解释：

1. two-prefix-branch resultant 的 central kernel；
2. single branch 上 `central factor × orientation factor`；
3. 原始 decimal 三元型
   \[
   23(BK)^2+81Q^2N_0.
   \]

而 external center 精确固定它的 square class。所以下一步若处理 generic non-external moving branch，可以继续研究 `C_*`；但在 external subchannel 中，其 quadratic character 已经耗尽，不应重复追逐。

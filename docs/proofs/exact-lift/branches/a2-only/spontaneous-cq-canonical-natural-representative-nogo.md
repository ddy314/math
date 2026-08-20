# A2 pure-`c_Q` canonical residue 与 `C` natural representative 的局部 no-go

> **依赖：** `spontaneous-cq-canonical-defect-overlap.md`、`endpoint-lattice.md` §16.15。
>
> **严格状态：**前一文件得到 canonical `c_- / c_+` allocation 在 finite-defect 顶部余量 `C` 上的精确 `p^{2c}` residue。本文检查最直接的下一步：把该 residue 代入 `(a,k)=(9,2)` reflection high-2 endpoint 的自然代表公式 (16.101)，是否会产生一个新的 pure-`c_Q` 局部 obstruction。结论是否定的：模 `p^{2c}` 后，(16.101) 精确退化为已有 high-2 equality 与 `H_0=±Y_3` canonical congruence。fixed `23` 的 simultaneous class 中，它进一步退化为 §16.37 已有的 directed square-root lock。新的信息只能来自与 `g/2^m` 等互素方向以及 `0<C<<L_0` 小代表区间的真正 CRT 比较。

---

## 1. endpoint natural representative

固定 `endpoint-lattice.md` 的危险 reflection high-2 core

\[
a=9,
\qquad k=2,
\qquad j=3,
\qquad T=10^m.
\]

§16.15 给出

\[
\boxed{
5^\lambda C
=gA_3+\varepsilon a_2c_Q5^d-\frac{g^2k_h}{2},
}
\tag{1.1}
\]

其中

\[
A_3=a_3+3T,
\qquad
\varepsilon\in\{-1,+1\},
\]

且 high-2 equality 为

\[
\boxed{
H_0+\varepsilon Y_2=\frac{g^2k_h}{2},
\qquad
Y_2=a_2c_Q5^d.
}
\tag{1.2}

另一方面 finite-defect/canonical 坐标满足

\[
5^\lambda D=gT,
\qquad
J=3-\frac CD,
\]

\[
H_0-Y_3=gTJ,
\qquad
H_0+Y_3=g(TJ+2a_3),
\qquad
Y_3=ga_3.
\tag{1.3}

---

## 2. minus orientation 代回 natural representative

固定 pure-`c_Q` prime

\[
p^c\Vert c_Q,
\qquad p\nmid q,
\qquad c\ge1,
\]
并假设

\[
p^c\Vert c_-.
\]

canonical factor 给

\[
p^{2c}\mid H_0-Y_3,
\]
所以前一文件得到

\[
\boxed{C\equiv3D\pmod{p^{2c}}.}
\tag{2.1}

用 `5^lambda D=gT`：

\[
5^\lambda C\equiv3gT\pmod{p^{2c}}.
\tag{2.2}

把 (2.2) 代入 (1.1)：

\[
3gT
\equiv
g(a_3+3T)+\varepsilon a_2c_Q5^d-rac{g^2k_h}{2}
\pmod{p^{2c}}.
\]

消去 `3gT`：

\[
\boxed{
\frac{g^2k_h}{2}
\equiv
ga_3+\varepsilon a_2c_Q5^d
\pmod{p^{2c}}.}
\tag{2.3}

但 minus canonical congruence本身就是

\[
H_0\equiv Y_3=ga_3\pmod{p^{2c}}.
\]

代入 high-2 equality (1.2) 后立刻得到 (2.3)。因此 minus side 没有新增局部条件。

---

## 3. plus orientation 同样退化

现在假设

\[
p^c\Vert c_+.
\]

前一文件给

\[
\boxed{
C\equiv
D\left(3+2a_3T^{-1}\right)
\pmod{p^{2c}}.}
\tag{3.1}

乘 `5^lambda`：

\[
5^\lambda C
\equiv
g(3T+2a_3)
\pmod{p^{2c}}.
\tag{3.2}

代入 (1.1)：

\[
g(3T+2a_3)
\equiv
g(a_3+3T)+\varepsilon a_2c_Q5^d-rac{g^2k_h}{2}.
\]

整理：

\[
\boxed{
\frac{g^2k_h}{2}
\equiv
-ga_3+\varepsilon a_2c_Q5^d
\pmod{p^{2c}}.}
\tag{3.3}

plus canonical congruence是

\[
H_0\equiv-Y_3=-ga_3\pmod{p^{2c}}.
\]

与 (1.2) 联立恰好就是 (3.3)。因此 plus side 也没有新的 pure-`c_Q` 局部 obstruction。

---

## 4. fixed `23` simultaneous class 只恢复 directed root lock

对 fixed `23` 的 simultaneous gate class，前一文件证明

\[
\kappa=4,
\qquad
\rho:=z/c_u=-1,
\qquad
\zeta:=a_3/T=7\pmod{23}.
\tag{4.1}

令

\[
X_h:=\frac{k_hg}{2}.
\]

因为 `23|c_Q`，(2.3)/(3.3) 模 `23` 时 `Y_2` 项消失，因此

### `23|c_-`

\[
\boxed{X_h\equiv a_3\equiv7T\pmod{23}.}
\tag{4.2-}

### `23|c_+`

\[
\boxed{X_h\equiv-a_3\equiv16T\pmod{23}.}
\tag{4.2+}

这正是 `endpoint-lattice.md` §16.37

\[
X_h\equiv a_3\pmod{5^dc_-},
\qquad
X_h\equiv-a_3\pmod{c_+}
\]
在 prime `23` 上的投影。

所以 fixed `23` 上把 `C` natural representative 再局部化，并不会得到第三个 orientation equation。

---

## 5. 审计结论

canonical residue 与 (16.101) 的关系可以准确记为

\[
\boxed{
\text{canonical }C\bmod p^{2c}
+
\text{natural representative (16.101) mod }p^{2c}
}
\]

\[
\boxed{
\Longleftrightarrow
H_0\equiv\pm Y_3\pmod{p^{2c}}
+
\text{high-2 equality mod }p^{2c}.
}
\tag{5.1}

因此以下路线应停止重复：

1. 单独把 (16.101) 再模 `23`, `23^2`, ...；
2. 把 resulting `X_h=±a_3` 当作新的 fixed-`23` obstruction；
3. 在同一个 pure-`c_Q` prime 上重复收取 canonical height 与 natural-representative 的局部 congruence。

真正仍然开放的对象是跨互素模数的自然代表问题。`endpoint-lattice.md` 还有

\[
c_uC\equiv-\varepsilon a_2 5^{M+d}\pmod g,
\]

\[
C\theta\equiv5^Ma_3\pmod{2^m},
\]
以及

\[
0<C<\frac{\mathfrak L_0}{1000},
\qquad
\mathfrak L_0=2c_u^2g^2.
\]

而本文/前一文件给出独立的

\[
C\equiv3D
\quad\text{or}\quad
C\equiv D(3+2a_3T^{-1})
\pmod{23^{2c}}.
\]

因为 `23∤2c_ug`，这些方向互素。下一步只有把它们组成真正的 CRT natural representative，并利用 `C` 的极小 Archimedean interval，才可能产生新的 fixed-`23` global obstruction。
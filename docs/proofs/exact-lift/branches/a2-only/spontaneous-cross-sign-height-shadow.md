# A2 cross-sign quadratic gate 在两张 height sheets 上均为 square shadow

> **依赖：** `spontaneous-cross-sign-sphere.md`、`spontaneous-height-parity-ledger.md`。
>
> **严格状态：**`spontaneous-cross-sign-sphere.md` 定义 conjugate-angle quadratic gate `v^2=-2X_cross`。本文证明在 height-1 与 height-2 两张 sphere orientations上，`-2X_cross` 都具有显式 rational/polynomial square root，因此该 quadratic character在整个 height-supported sector都是自动 shadow，不能作为独立 obstruction。随后审计两个 square-root collision locus：所有 genuine non-`3` inert finite singular candidates都在第一次 `p^2` lifting时失败，因此 cross-sign angle/height sector没有 surviving singular Hensel tree，只剩 simple moving synchronization。本文不排除 simple roots，也不宣称 A2 closure。

---

## 1. 记号

定义

\[
P(x):=101x^2+4x+4,
\]

height-1 orientation：

\[
\boxed{
H_1:=202500x^4+P(x)y^2.
}
\tag{1.1}
\]

height-2 orientation：

\[
\boxed{
\begin{aligned}
H_2={}&410062500x^6-402975x^4y^2-7290000x^4y\\
&+8100x^3y^2+101x^2y^4+3600x^2y^3\\
&+40500x^2y^2+4xy^4+4y^4.
\end{aligned}}
\tag{1.2}
\]

cross-sign polynomial为

\[
\boxed{
\begin{aligned}
X_\times={}&205031250x^6+2025x^4y^2-1822500x^4y\\
&+8100x^3y^2-99x^2y^4-1800x^2y^3\\
&+4050x^2y^2+4xy^4+4y^4.
\end{aligned}}
\tag{1.3}
\]

conjugate-angle sphere在 genuine odd prime上有 third-numerator root所需的唯一 quadratic character是

\[
\left(\frac{-2X_\times}{p}\right)=1.
\tag{1.4}
\]

---

## 2. `已严格完成`：height-1 上 `-2X_cross` 是显式平方

定义

\[
\boxed{
R_1^{\rm sq}
:=20250x^3(9x-2)(11x+2)-90xyP(x).
}
\tag{2.1}
\]

直接 polynomial division 得 exact congruence

\[
\boxed{
P(x)^2(-2X_\times)
\equiv
\left(R_1^{\rm sq}\right)^2
\pmod{H_1}.
}
\tag{2.2}
\]

更强地，左减右恰为 `H_1` 乘一个显式整数 polynomial；checker逐项验证。

对 genuine non-`3` inert height-1 prime，`P(x)` 为 unit。事实上

\[
P(x)=(10x)^2+(x+2)^2,
\]
而 `p=3 mod4` 不允许两个 nonzero squares之和为零。

因此在 `H_1=0` 上：

\[
\boxed{
-2X_\times
\equiv
\left[
\frac{20250x^3(9x-2)(11x+2)}{P(x)}-90xy
\right]^2.
}
\tag{2.3}
\]

所以

\[
\boxed{
H_1=0
\Longrightarrow
\left(\frac{-2X_\times}{p}\right)=1
}
\tag{2.4}
\]

自动成立。

---

## 3. height-2 上也是显式平方

令

\[
D_2:=2025x^2-2y^2-27y.
\]

已有 exact syzygy

\[
X_\times=H_2-50x^2D_2^2.
\]

因此

\[
\boxed{
-2X_\times
\equiv
(10xD_2)^2
\pmod{H_2}.
}
\tag{3.1}
\]

所以 height-2 同样自动满足 cross-sign quadratic gate：

\[
\boxed{
H_2=0
\Longrightarrow
\left(\frac{-2X_\times}{p}\right)=1.
}
\tag{3.2}
\]

结论：cross-sign Legendre condition在两张 height orientations上都只是旧 sphere splitting 的投影，不能重复收费。

---

# square-root collision audit

## 4. height-1 collision只剩固定 quartic

height-1 的 cross square root消失意味着

\[
H_1=0,
\qquad
R_1^{\rm sq}=0.
\]

消去 `y`：

\[
\boxed{
\operatorname{Res}_y(H_1,R_1^{\rm sq})
=410062500x^6P(x)Q_1(x),
}
\tag{4.1}
\]

其中

\[
\boxed{
Q_1(x)=9801x^4-792x^3-372x^2+48x+32.
}
\tag{4.2}
\]

`x=0` 为 boundary；`P=0` 对 genuine inert prime不可能。因此只需审计 `Q_1`。

其判别式：

\[
\boxed{
\operatorname{Disc}(Q_1)
=2^{18}3^7 5^2 11^2\cdot3677363.
}
\tag{4.3}
\]

`p=11` 只导致 leading-degree drop，并无 finite repeated root。唯一 genuine non-`3` inert repeated finite candidate为

\[
\boxed{p=3677363.}
\tag{4.4}
\]

模 `p`：

\[
\gcd(Q_1,Q_1')=x-1336107.
\]

full system `H_1=R_1^{sq}=0` 唯一给

\[
\boxed{
(x,y)=(1336107,2340128)\pmod p.
}
\tag{4.5}
\]

该点 Jacobian determinant为零。写

\[
x=x_0+pX,
\qquad
y=y_0+pY,
\]
除以 `p` 后的 augmented linear system右端为

\[
\boxed{(482973,1688419).}
\tag{4.6}
\]

直接 rank compatibility检查失败，因此：

\[
\boxed{
\text{height-1 唯一 genuine singular cross collision不能 lift 到 }p^2.
}
\tag{4.7}
\]

---

## 5. height-2 collision只剩两个 genuine inert repeated candidates

height-2 square root消失意味着

\[
H_2=0,
\qquad
D_2=0.
\]

消去 `y`：

\[
\boxed{
\operatorname{Res}_y(H_2,D_2)
=672605015625x^6(25x^2+1)Q_2(x),
}
\tag{5.1}
\]

其中

\[
\boxed{
Q_2(x)
=10609x^4+2472x^3+3052x^2+432x+288.
}
\tag{5.2}
\]

对 `p=3 mod4`，`25x^2+1=0` 不可能有 genuine unit root。

quartic discriminant为

\[
\boxed{
\operatorname{Disc}(Q_2)
=2^{18}3^2 5^2\cdot61\cdot103^2\cdot2671\cdot6659.
}
\tag{5.3}
\]

`p=103` 只是 leading-degree drop，没有 finite repeated root。genuine inert repeated candidates只剩

\[
\boxed{p=2671,6659.}
\tag{5.4}
\]

### `p=2671`

repeated `x` root：

\[
x\equiv-56\equiv2615.
\]

`D_2=0` 有两个 `y` roots，但只有

\[
\boxed{(x,y)=(2615,601)}
\tag{5.5}
\]

同时满足 `H_2=0`。

该点 `p^2` linearization的右端为

\[
(1437,335),
\]
且 rank compatibility失败。

### `p=6659`

repeated `x` root：

\[
x=654.
\]

full collision唯一 genuine state：

\[
\boxed{(x,y)=(654,2478).}
\tag{5.6}
\]

`p^2` linearization右端：

\[
(4424,4966),
\]
同样不属于 Jacobian image。

因此：

\[
\boxed{
\text{height-2 cross square-root collision也没有 surviving singular Hensel tree.}
}
\tag{5.7}
\]

---

## 6. 严格结论

cross-sign conjugate-angle quadratic extension在 height-supported sector中的完整状态是：

\[
\boxed{
\begin{array}{c|c|c}
\text{height sheet}&-2X_\times&\text{singular collision}\\ \hline
H_1&\text{explicit square}&p=3677363\text{ dies at }p^2\\
H_2&\text{explicit square}&p=2671,6659\text{ die at }p^2.
\end{array}}
\tag{6.1}
\]

所以：

\[
\boxed{
\text{cross-sign angle/height interaction没有新的 quadratic obstruction，}
}
\]

并且

\[
\boxed{
\text{也没有新的 singular Hensel tree。}
}
\]

剩下的 height-supported cross-sign contacts全部是 simple moving decimal synchronization。继续追同一 quadratic character或 singular discriminant不会增加约束。

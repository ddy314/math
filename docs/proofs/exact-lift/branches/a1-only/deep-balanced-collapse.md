# A1 minimal diagonal: balanced double-deep collapse

> 日期：2026-08-20。依赖 `deep-complement-height.md`。当前统一剩余范围为 `k=g>=31`，central 已关闭，因此只研究 deep denominator。

本文证明 double-deep 中一个大区域实际上完全为空。

写

\[
T=10^k,
\qquad
\Gamma_k=\frac{\gamma}{D},
\qquad
D=2^A5^B,
\qquad A,B>0,
\]

其中 `gcd(gamma,10)=1`，并且

\[
15.09<\Gamma_k<39.003.
\]

令

\[
e=v_2(w),
\qquad
\nu_2=v_2(N_0),
\qquad
\nu_5=v_5(N_0).
\]

核心结论是：若两侧 cancellation depth 都至少达到一个完整 `T`，即

\[
\boxed{
A+e+\nu_2\ge k,
\qquad
B+\nu_5\ge k,
}
\tag{1}
\]

则不存在 candidate。于是任何尚存 double-deep 必须满足

\[
\boxed{
A+e+\nu_2<k
\quad\text{或}\quad
B+\nu_5<k.
}
\tag{2}
\]

状态：**已严格完成。**

---

## 1. complement identity

沿用 `deep-complement-height.md`。double-deep 时 `lambda=1`，并有

\[
DTN_0-\gamma=h,
\qquad
M:=\frac{Qb_1}{h}\in\mathbf Z_{>0}.
\]

记

\[
P:=Qb_1
=1000T^4+c_2T^2+C_0,
\]

其中

\[
\boxed{c_2:=10(1-20w),}
\qquad
\boxed{C_0:=w(10w-1).}
\]

则

\[
\boxed{
M(DTN_0-\gamma)=P.
}
\tag{3}
\]

又有

\[
v_2(M)=e,
\qquad
v_5(M)=0.
\tag{4}
\]

---

## 2. balanced 条件产生 bounded integer `J`

由 (1)、(4)：

\[
v_2(MDTN_0)
=e+A+k+\nu_2
\ge2k,
\]

\[
v_5(MDTN_0)
=B+k+\nu_5
\ge2k.
\]

因此

\[
\boxed{T^2\mid MDTN_0.}
\tag{5}
\]

从 (3) 得

\[
M\gamma=MDTN_0-P.
\]

而

\[
P\equiv C_0\pmod{T^2},
\]

所以

\[
\boxed{T^2\mid M\gamma+C_0.}
\]

定义整数

\[
\boxed{
J:=\frac{M\gamma+C_0}{T^2}.
}
\tag{6}
\]

现在利用 complement-height 中

\[
\mu:=\frac{MD}{T^2},
\qquad
1000<\mu<10001.
\]

因为 `gamma=D Gamma_k`，有

\[
J=\mu\Gamma_k+\frac{C_0}{T^2}.
\]

于是

\[
J>1000\cdot15.09=15090,
\]

而 `C_0<=156`、`T>=10^31` 给

\[
J<10001\cdot39.003+1<390070.
\]

故

\[
\boxed{15091\le J\le390069.}
\tag{7}
\]

这一步把原本随 `k,A,B` 变化的 complement residue 压成一个绝对有限整数。

---

## 3. `Gamma_k` 的新有理表示

由 (6)：

\[
\boxed{M\gamma=JT^2-C_0.}
\tag{8}
\]

把它代回 (3)：

\[
MDTN_0
=P+M\gamma
=1000T^4+(c_2+J)T^2.
\]

令

\[
H:=MD.
\]

除以 `T` 得

\[
\boxed{
HN_0
=T\bigl(1000T^2+c_2+J\bigr).
}
\tag{9}
\]

另一方面由 (8)：

\[
H\Gamma_k=M\gamma=JT^2-C_0.
\tag{10}
\]

将 (9)、(10) 相除：

\[
\boxed{
\Gamma_k
=
\frac{
N_0(JT^2-C_0)
}{
T(1000T^2+c_2+J)
}.
}
\tag{11}
\]

这是 balanced double-deep 的关键新正规形。

---

## 4. denominator odd part 必须被分子完全吸收

记

\[
\boxed{C:=c_2+J,}
\qquad
\boxed{F:=1000T^2+C,}
\qquad
\boxed{G:=JT^2-C_0.}
\]

由 `w=1,2,3,4`：

\[
-790\le c_2\le-190.
\]

结合 (7)：

\[
\boxed{14301\le C\le389879.}
\tag{12}
\]

因为

\[
v_2(1000T^2)=2k+3\ge65,
\qquad
v_5(1000T^2)=2k+3\ge65,
\]

而 `C<390000`，所以两边赋值严格不同：

\[
\boxed{v_2(F)=v_2(C),}
\qquad
\boxed{v_5(F)=v_5(C).}
\tag{13}
\]

定义去掉全部 `2,5` 因子的 odd part

\[
\boxed{
F_0:=\frac{F}{2^{v_2(C)}5^{v_5(C)}}.
}
\tag{14}
\]

由 (12)：

\[
2^{v_2(C)}5^{v_5(C)}\le C\le389879,
\]

因此

\[
\boxed{
F_0>rac{1000T^2}{389879}.
}
\tag{15}
\]

但 `Gamma_k=gamma/D` 的既约分母 `D` 只含素数 `2,5`。在表示 (11) 中，`T` 同样只含 `2,5`。因此 `F` 的全部 odd-prime part 必须在分子 `N_0G` 中被消掉：

\[
oxed{F_0\mid N_0G.}
\tag{16}
\]

---

## 5. `F` 与 `G` 的 gcd 只有绝对常数大小

计算：

\[
\begin{aligned}
JF-1000G
&=J(1000T^2+C)-1000(JT^2-C_0)\\
&=JC+1000C_0.
\end{aligned}
\]

定义

\[
\boxed{R_J:=JC+1000C_0.}
\tag{17}
\]

于是

\[
\boxed{
\gcd(F,G)\mid R_J.
}
\tag{18}
\]

由

\[
J\le390069,
\qquad C\le389879,
\qquad C_0\le156,
\]

得到统一界

\[
\boxed{
0<R_J<152080000000.
}
\tag{19}
\]

令

\[
d:=\gcd(F_0,G).
\]

由 (16)：

\[
\frac{F_0}{d}\mid N_0.
\]

而 (18)-(19) 给

\[
d<152080000000.
\]

又 `N_0<T`，故

\[
\boxed{
F_0<152080000000\,T.
}
\tag{20}
\]

与 (15) 合并：

\[
\frac{1000T^2}{389879}
<152080000000\,T.
\]

因此

\[
T<
\frac{389879\cdot152080000000}{1000}
<6\times10^{13}.
\tag{21}
\]

但当前

\[
T=10^k,
\qquad k\ge31,
\]

显然矛盾。

所以 balanced region (1) 完全为空。

---

## 6. 当前 double-deep 的形状

结合 `deep-complement-height.md`，任何剩余 double-deep candidate 必须同时满足：

\[
2^{\min(A+e+\nu_2,3k)}
5^{B+\nu_5}
<390100\,10^k,
\qquad B+\nu_5<3k,
\]

以及本文新增的

\[
\boxed{
A+e+\nu_2<k
\quad\text{或}\quad
B+\nu_5<k.
}
\]

因此 double-deep 的中间 balanced rectangle 已被完全删除；剩余状态只能贴着至少一个 shallow side 运行。

下一步应分别处理：

1. `2`-shallow：`A+e+nu_2<k`；
2. `5`-shallow：`B+nu_5<k`；
3. 二者同时 shallow 的交集。

这些区域再与已有 parity/resonance、unit-square 与 Q-side orientation 联用。
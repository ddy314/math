# A1 minimal diagonal: fully-balanced deep collapse

> 日期：2026-08-20。依赖 `deep-complement-height.md`。当前统一剩余范围为 `k=g>=31`，central 已关闭，因此只研究 deep denominator。

本文把原先的 balanced double-deep collapse 推广到**任意 deep sector**。

沿用

\[
T=10^k,
\qquad
\Gamma_k=\frac{\gamma}{D},
\qquad
D=2^A5^B,
\qquad
15.09<\Gamma_k<39.003,
\]

以及非 deep 一侧的 numerator powers

\[
\lambda=2^{\lambda_2}5^{\lambda_5}.
\]

记

\[
e=v_2(w),
\qquad
\nu_2=v_2(N_0),
\qquad
\nu_5=v_5(N_0).
\]

核心结论：若两侧 cancellation depth 足以把整个 `lambda*T^2` 吃掉，即

\[
\boxed{
A+e+\nu_2\ge k+\lambda_2,
\qquad
B+\nu_5\ge k+\lambda_5,
}
\tag{1}
\]

则不存在 candidate。

所以任何尚存 deep candidate 必须满足

\[
\boxed{
A+e+\nu_2<k+\lambda_2
\quad\text{或}\quad
B+\nu_5<k+\lambda_5.
}
\tag{2}
\]

特别地，double-deep `A,B>0` 时 `lambda_2=lambda_5=0`，恢复

\[
\boxed{
A+e+\nu_2<k
\quad\text{或}\quad
B+\nu_5<k.
}
\tag{3}
\]

状态：**已严格完成。**

---

## 1. general deep complement identity

`deep-complement-height.md` 给出

\[
DTN_0-\gamma=h\lambda,
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

乘以 `M`：

\[
\boxed{
M(DTN_0-\gamma)=P\lambda.
}
\tag{4}
\]

仍有

\[
v_2(M)=e,
\qquad
v_5(M)=0.
\tag{5}
\]

---

## 2. fully-balanced 条件产生 bounded integer `J`

由 (1)、(5)：

\[
v_2(MDTN_0)
=e+A+k+\nu_2
\ge2k+\lambda_2,
\]

\[
v_5(MDTN_0)
=B+k+\nu_5
\ge2k+\lambda_5.
\]

因此

\[
\boxed{
\lambda T^2\mid MDTN_0.
}
\tag{6}
\]

由 (4)：

\[
M\gamma=MDTN_0-P\lambda.
\]

而

\[
P\lambda\equiv C_0\lambda\pmod{\lambda T^2},
\]

所以

\[
\boxed{
\lambda T^2\mid M\gamma+C_0\lambda.
}
\]

定义整数

\[
\boxed{
J:=\frac{M\gamma+C_0\lambda}{\lambda T^2}.
}
\tag{7}
\]

另一方面 complement-height 定义

\[
\mu:=\frac{MD}{\lambda T^2},
\qquad
1000<\mu<10001.
\]

因为 `gamma=D Gamma_k`：

\[
J=\mu\Gamma_k+\frac{C_0}{T^2}.
\]

于是完全独立于 deep 类型：

\[
\boxed{15091\le J\le390069.}
\tag{8}
\]

---

## 3. `lambda` 完全消失

由 (7)：

\[
\boxed{
M\gamma=\lambda(JT^2-C_0).
}
\tag{9}
\]

代回 (4)：

\[
MDTN_0
=\lambda\left(1000T^4+(c_2+J)T^2\right).
\tag{10}
\]

将 (9)、(10) 相除。左侧比值为

\[
\frac{M\gamma}{MDTN_0}
=\frac{\Gamma_k}{TN_0},
\]

而右侧的 `lambda` 精确约掉，所以仍得到

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

这是最关键的一点：**fully-balanced 后的有理正规形与 single/deep 类型、`lambda`、`A,B` 全部无关。**

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

由 `w=1,2,3,4` 与 (8)：

\[
\boxed{14301\le C\le389879.}
\tag{12}
\]

又

\[
v_2(1000T^2)=v_5(1000T^2)=2k+3\ge65,
\]

远大于 `C` 的可能赋值，所以

\[
\boxed{v_2(F)=v_2(C),}
\qquad
\boxed{v_5(F)=v_5(C).}
\tag{13}
\]

定义去掉全部 `2,5` 因子的部分

\[
\boxed{
F_0:=\frac{F}{2^{v_2(C)}5^{v_5(C)}}.
}
\tag{14}
\]

则

\[
\boxed{
F_0>\frac{1000T^2}{389879}.
}
\tag{15}
\]

无论 single-deep 还是 double-deep，`Gamma_k=gamma/D` 的既约分母 `D=2^A5^B` 都只含 `2,5`。而 (11) 中 `T` 也只含 `2,5`。因此 `F` 的全部非 `2,5` 因子必须在分子 `N_0G` 中完全消失：

\[
\boxed{F_0\mid N_0G.}
\tag{16}
\]

---

## 5. `F,G` 的公共 odd part 只有绝对常数大小

计算

\[
JF-1000G
=J(c_2+J)+1000C_0.
\]

定义

\[
\boxed{
R_J:=J(c_2+J)+1000C_0.
}
\tag{17}
\]

所以

\[
\boxed{
\gcd(F,G)\mid R_J.
}
\tag{18}
\]

由 (8)、(12) 与 `C_0<=156`：

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

而 (18)-(19)、`N_0<T` 给出

\[
\boxed{
F_0<152080000000\,T.
}
\tag{20}
\]

与 (15) 联立：

\[
\frac{1000T^2}{389879}
<152080000000\,T,
\]

故

\[
T<6\times10^{13}.
\tag{21}
\]

当前 `T=10^k`、`k>=31`，矛盾。

因此 fully-balanced 条件 (1) 下不存在任何 deep candidate。

---

## 6. 对各 deep sector 的直接推论

### double-deep

`A,B>0` 时

\[
\lambda_2=\lambda_5=0,
\]

所以任何 candidate 必须满足

\[
\boxed{
A+e+\nu_2<k
\quad\text{或}\quad
B+\nu_5<k.
}
\]

### single 2-deep

若

\[
A>0,\qquad B=0,
\]

则 `lambda_2=0`，`lambda_5=k+y>=0`。fully-balanced 区域

\[
A+e+\nu_2\ge k,
\qquad
\nu_5\ge k+\lambda_5
\]

全部为空。

### single 5-deep

若

\[
A=0,\qquad B>0,
\]

则 `lambda_5=0`，`lambda_2=k+x>=0`。fully-balanced 区域

\[
e+\nu_2\ge k+\lambda_2,
\qquad
B+\nu_5\ge k
\]

全部为空。

---

## 7. 当前 deep 几何

`deep-complement-height.md` 给出了 logarithmic height strip；本文又删除了所有 fully-balanced 点。因此剩余 deep 状态必须贴着至少一个**相对于 `lambda*T^2` 的 shallow side**。

后续不应再把 deep 当成完整二维 lattice。应分成：

1. 2-shallow：
   \[
   A+e+\nu_2<k+\lambda_2;
   \]
2. 5-shallow：
   \[
   B+\nu_5<k+\lambda_5;
   \]
3. 两者同时 shallow。

再分别加入 resonance parity、mod-8 / mod-5 unit locks、Q-side orientation 与 proper-divisor / whole-block loss。
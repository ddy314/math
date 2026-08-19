# A1 minimal diagonal: moderate double-deep factorization

> 日期：2026-08-20。依赖 `deep-balanced-collapse.md` 与 minimal-diagonal odd-prime supply。
> 当前统一范围 `k=g>=31`。

本文研究 double-deep

\[
\Gamma_k=\frac{\gamma}{D},
\qquad
D=2^A5^B,
\qquad A,B>0,
\qquad \gcd(\gamma,10)=1,
\]

中的 moderate 区域

\[
\boxed{A\le2k+3,\qquad B\le2k+3.}
\tag{1}
\]

核心结论是：这一看似二维的区域实际上只能落在两个绝对有限宽的边带中：

\[
\boxed{
A\le23
\quad\text{或}\quad
B\le10.
}
\tag{2}
\]

关键工具是一套 deep Euclidean descent，它把 supply divisibility 化成一个精确二因子分解。

状态：**已严格完成。**

---

## 1. deep Euclidean descent

记

\[
T=10^k,
\qquad
L:=DT,
\qquad
h:=DTN_0-\gamma=N_0L-\gamma.
\]

因为 double-deep 时 `lambda=1`，odd-prime supply 给

\[
h\mid P:=Qb_1.
\]

又 `gcd(h,D)=1`，所以

\[
h\mid D^4P.
\]

而

\[
\boxed{
D^4P
=1000L^4+c_2D^2L^2+C_0D^4,
}
\tag{3}
\]

其中

\[
c_2=10(1-20w),
\qquad
C_0=w(10w-1).
\]

对商 `(D^4P)/h` 按 `L` 做与 central sector 相同的两级 Euclidean division。由于

\[
\gcd(\gamma,L)=1,
\]

两个余数同余可以完全消去，得到某个整数 `U`，满足

\[
\boxed{
C_0D^4N_0^2
-U L N_0
+1000\gamma^2L^2
+\gamma U
+c_2D^2\gamma^2
=0.
}
\tag{4}
\]

这是 deep 版本的 supply quadratic。

---

## 2. `D^2 | U`

把 (4) 模 `D`。除 `gamma U` 外其余项都被 `D` 整除，因此

\[
\gamma U\equiv0\pmod D.
\]

由于 `gcd(gamma,D)=1`：

\[
D\mid U.
\]

写 `U=DU_1`，再把 (4) 模 `D^2`。此时除 `D gamma U_1` 外所有项都被 `D^2` 整除，所以

\[
D\gamma U_1\equiv0\pmod{D^2}.
\]

再次利用 `gcd(gamma,D)=1`：

\[
D\mid U_1.
\]

因此

\[
\boxed{D^2\mid U.}
\tag{5}
\]

写

\[
\boxed{U=D^2u,\qquad u\in\mathbf Z.}
\tag{6}
\]

将 (4) 除以 `D^2`，并使用 `L=DT`：

\[
\boxed{
C_0D^2N_0^2
-DuTN_0
+1000\gamma^2T^2
+\gamma u
+c_2\gamma^2
=0.
}
\tag{7}
\]

---

## 3. deep Pell normal form

把 (7) 看成关于 `N_0` 的二次方程。判别式除去显然平方因子 `D^2` 后，必须有整数 `y` 满足

\[
\boxed{
y^2=A_uT^2+B_u,}
\tag{8}
\]

其中

\[
\boxed{A_u=u^2-4000C_0\gamma^2,}
\]

\[
\boxed{B_u=-4C_0\gamma u-4C_0c_2\gamma^2.}
\]

定义天然平方点

\[
\boxed{u_0:=10\gamma(20w-1),}
\qquad
\boxed{v_0:=10\gamma.}
\]

因为

\[
u_0^2-v_0^2=4000C_0\gamma^2,
\]

并且 `c_2=-10(20w-1)`，所以

\[
\boxed{
A_u=u^2-(u_0^2-v_0^2),
}
\tag{9}
\]

\[
\boxed{
B_u=-4C_0\gamma(u-u_0).
}
\tag{10}

这与 central Pell normal form 具有完全相同的平方点结构，但参数 `gamma,D` 仍在变化。

---

## 4. `u-u0` 的 deep congruence

把 (7) 模 `D`。前两项消失，得到

\[
1000\gamma^2T^2+\gamma u+c_2\gamma^2\equiv0\pmod D.
\]

除以模 `D` 可逆的 `gamma`：

\[
u+c_2\gamma
\equiv-1000\gamma T^2\pmod D.
\]

而

\[
u_0=-c_2\gamma.
\]

因此

\[
\boxed{
 u-u_0
 \equiv-1000\gamma T^2
 \pmod D.
}
\tag{11}

当前

\[
v_2(1000T^2)=v_5(1000T^2)=2k+3.
\]

所以在 moderate 条件 (1) 下：

\[
\boxed{D\mid u-u_0.}
\tag{12}

写

\[
\boxed{u-u_0=Dr,\qquad r\in\mathbf Z.}
\tag{13}

---

## 5. `r` 是绝对有限正整数

从 (4) 直接解 `U`，再除以 `D^3`，令

\[
s:=N_0/T,
\qquad
\Gamma:=\gamma/D,
\]

得到精确式

\[
\boxed{
\frac uD
=
\frac{
C_0N_0^2+1000\Gamma^2T^2+c_2\Gamma^2
}{TN_0-\Gamma}.
}
\tag{14}

这里

\[
0.1<s\le1,
\qquad
15.09<\Gamma<39.003.
\]

当前 `T>=10^31`。用 `C_0>=0`、`c_2>=-790` 和上述窗口，可取安全界

\[
\boxed{
227000<\frac uD<15214000.
}
\tag{15}

另一方面

\[
0<\frac{u_0}{D}
=10\Gamma(20w-1)
<30813.
\]

故 (13) 给出

\[
\boxed{
196000<r<15214000.
}
\tag{16}

特别地

\[
\boxed{r>0,}
\]

且

\[
\boxed{v_2(r)\le23,}
\qquad
\boxed{v_5(r)\le10.}
\tag{17}

---

## 6. quadratic 精确因式分解

把

\[
u=u_0+Dr
\]

代回 (7)。注意

\[
\gamma u_0+c_2\gamma^2=0.
\]

剩余前三个主项具有判别式 `100`，并且恒等式

\[
\begin{aligned}
& C_0(DN_0)^2
-10(20w-1)(DN_0)(\gamma T)
+1000(\gamma T)^2\\
&\qquad=
(wDN_0-10\gamma T)
((10w-1)DN_0-100\gamma T).
\end{aligned}
\]

因此 (7) 精确化成

\[
\boxed{
(wDN_0-10\gamma T)
((10w-1)DN_0-100\gamma T)
=Dr(DTN_0-\gamma).
}
\tag{18}

因为

\[
10\Gamma-ws>150.9-4>0,
\]

\[
100\Gamma-(10w-1)s>1509-39>0,
\]

两个左侧括号都为负。定义正整数

\[
\boxed{X_1:=10\gamma T-wDN_0,}
\]

\[
\boxed{X_2:=100\gamma T-(10w-1)DN_0.}
\]

则

\[
\boxed{X_1X_2=Drh.}
\tag{19}

---

## 7. prime supply 自动把两个因子分流

完整 odd-prime supply 写成

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1,
\qquad \gcd(q,s)=1.
\]

### `s` 进入 `X1`

模 `s` 有

\[
DTN_0\equiv\gamma.
\]

因为 `T` 对 `s` 可逆：

\[
TX_1
\equiv
10\gamma T^2-w\gamma
=\gamma(10T^2-w)
=\gamma b_1
\equiv0\pmod s.
\]

所以

\[
\boxed{s\mid X_1.}
\tag{20}

### `q` 进入 `X2`

同理：

\[
TX_2
\equiv
100\gamma T^2-(10w-1)\gamma
=\gamma Q
\equiv0\pmod q.
\]

故

\[
\boxed{q\mid X_2.}
\tag{21}

于是存在正整数 `a,b` 使

\[
\boxed{X_1=sa,}
\qquad
\boxed{X_2=qb.}
\tag{22}

由 (19)、`h=qs`：

\[
\boxed{ab=Dr.}
\tag{23}

这就是 moderate double-deep 的精确 factor-pair normal form。

---

## 8. 5-adic valuation dichotomy

记

\[
\nu_5=v_5(N_0),
\qquad
Y:=B+\nu_5.
\]

由于 `q,s` 与 `10` 互素，由 (22)-(23)：

\[
v_5(X_1)+v_5(X_2)=B+v_5(r).
\tag{24}

在 `X_1` 中两项赋值为

\[
k+1,\qquad Y;
\]

在 `X_2` 中为

\[
k+2,\qquad Y.
\]

### low branch: `Y<k+1`

两处都由 `DN_0` 项严格承担低赋值：

\[
2Y=B+v_5(r).
\]

所以

\[
\boxed{
B+2\nu_5=v_5(r)\le10.
}
\tag{25}

特别地

\[
\boxed{B\le10.}
\tag{26}

### high branch: `Y>k+2`

两处都由 `gamma*T` 项承担低赋值：

\[
2k+3=B+v_5(r),
\]

即

\[
\boxed{B=2k+3-v_5(r).}
\tag{27}

### transition strip

只剩

\[
\boxed{Y\in\{k+1,k+2\},}
\tag{28}

其中可能发生额外 cancellation，需要单独保留。

---

## 9. 2-adic valuation dichotomy

记

\[
\nu_2=v_2(N_0),
\qquad
X:=A+\nu_2,
\qquad
e=v_2(w).
\]

`X_1` 两项赋值为

\[
k+1,\qquad X+e,
\]

`X_2` 两项赋值为

\[
k+2,\qquad X.
\]

由 (22)-(23)：

\[
v_2(X_1)+v_2(X_2)=A+v_2(r).
\tag{29}

### low branch: `X+e<k+1`

两处 `DN_0` 项严格主导：

\[
(X+e)+X=A+v_2(r).
\]

所以

\[
\boxed{
A+2\nu_2+e=v_2(r)\le23.
}
\tag{30}

特别地

\[
\boxed{A\le23.}
\tag{31}

### high branch: `X>k+2`

两处 `gamma*T` 项严格主导：

\[
2k+3=A+v_2(r),
\]

因此

\[
\boxed{A=2k+3-v_2(r).}
\tag{32}

### transition strip

其余状态全落入宽度至多 `4` 的带：

\[
\boxed{
k+1-e\le A+\nu_2\le k+2.}
\tag{33}

---

## 10. fully-balanced collapse 把 moderate region 压成两条有限宽边带

`deep-balanced-collapse.md` 已证明：double-deep candidate 必须满足

\[
A+e+\nu_2<k
\quad\text{或}\quad
B+\nu_5<k.
\tag{34}

若第一条成立，则当然

\[
A+\nu_2+e<k<k+1,
\]

所以必在 2-adic low branch；由 (31)：

\[
A\le23.
\]

若第二条成立，则

\[
B+\nu_5<k<k+1,
\]

所以必在 5-adic low branch；由 (26)：

\[
B\le10.
\]

因此无论哪一条 shallow side 出现，都得到

\[
\boxed{
A\le23
\quad\text{或}\quad
B\le10.
}
\]

这证明了主结论 (2)。

---

## 11. 当前 double-deep 剩余几何

moderate double-deep 已从二维无界区域压成：

1. `A=1,...,23` 的有限宽 vertical strips；或
2. `B=1,...,10` 的有限宽 horizontal strips。

同时还保留更细的 valuation dichotomy：另一侧要么也绝对小，要么位于 `k+O(1)` transition strip，要么被精确锁到

\[
A=2k+3-v_2(r)
\quad\text{或}\quad
B=2k+3-v_5(r),
\]

其中 `r` 属于绝对有限区间 (16)。

因此 moderate double-deep 已不再需要二维 exponent search。下一步可以对有限 `A<=23` / `B<=10` 条带分别做 periodic modular exhaustion，或继续利用 factor-pair (22)-(23) 的 Q-side / `b_1`-side来源。
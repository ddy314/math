# A2 length-orbit and fully coupled spontaneous reduction

> **依赖：** `source-length-resultant.md`、`spontaneous-angle.md`、`decimal-prefix-bridge.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文审计 fixed length polynomial 与真实十进制轨道 `36·10^{M-1}` 的 `p`-进同步，并把 spontaneous angle、external double-root 与 prefix norm 全部联立，消去 `r_s,x,y` 后得到两个固定八次 length polynomial。对 `p=19`，消元系统有两条局部解，但其中一条精确落回 `f`-denominator boundary；真正的 external/spontaneous 只剩一条唯一 Hensel 轨道。本文仍**不宣称 A2 全局关闭**。

---

## 1. `已严格完成 / 降级`：simple length root 只给唯一指数轨道

设 `F(s)∈Z[s]`、`p∤10`，且

\[
F(s_0)\equiv0\pmod p,
\qquad F'(s_0)\not\equiv0\pmod p.
\]

若 `s_0≡36·10^{n_0} (mod p)`，则 Hensel 引理把 `s_0` 唯一提升为 `s_*∈Z_p`。令

\[
d=\operatorname{ord}_p(10),
\qquad \nu=v_p(10^d-1).
\]

当 `ν=1` 时，`10^d=1+pu`，`u∈Z_p^×`，所以同一模 `p` 轨道中的单位由一个 `p`-进指数参数唯一控制。于是

\[
\boxed{
\text{simple root}+v_p(10^d-1)=1
\Longrightarrow
\text{至多一条 }p\text{-进 decimal exponent branch}.}
\tag{1.1}
\]

若 `ν>1`，最初只有一个有限 Wieferich 型 compatibility gate；通过后仍回到一维唯一 lift。因此“唯一”本身不是空性，generic closure 必须加入第二个全局条件。

---

## 2. `已严格完成 / 降级`：旧 source/external 的 `19`-进 length lift 只刚性化

`source-length-resultant.md` 的 quartic 满足

\[
\mathcal L_{SW}(s)\equiv(s-2)(s-8)\pmod{19}.
\]

并且

\[
\boxed{10^{18}=1+15\cdot19\pmod{19^2}},
\tag{2.1}
\]

故

\[
\boxed{\operatorname{ord}_{19^k}(10)=18\cdot19^{k-1}}.
\tag{2.2}
\]

两个 simple roots 都唯一提升。前四层为

\[
\boxed{
\begin{array}{c|c|c|c|c}
k&s_1&s_2&M_1&M_2\\ \hline
1&2&8&10\ (18)&8\ (18)\\
2&211&255&100\ (342)&224\ (342)\\
3&2016&255&2152\ (6498)&4670\ (6498)\\
4&22593&61986&8650\ (123462)&50156\ (123462)
\end{array}}
\tag{2.3}
\]

所以继续机械升 `19^k` 不会自动排除旧 source/external overlap。

---

# 第二部分：spontaneous angle + external double-root + prefix norm

## 3. 三个局部方程

令

\[
s=36\cdot10^{M-1},
\qquad Y_s=11-9s.
\]

external prefix root `36P-11≡0` 给

\[
y\equiv\frac{Y_s}{s}\pmod p.
\tag{3.1}
\]

`decimal-prefix-bridge.md` 的 `R_N`、`spontaneous-angle.md` 的 `Omega_sp` 与 external discriminant 分别化成

\[
\boxed{
\mathcal N_{sp}(s,x)
=(x+2)^2(2025s^2x^2+Y_s^2)+10780x^2,
}
\tag{3.2}
\]

\[
\boxed{
\begin{aligned}
\mathcal O_{sp}(s,x,r_s)={}&
r_s\left[4(225sx^2+9s-11)^2-xY_s^2(99x-4)\right]\\
&+2xY_s^2(x+2),
\end{aligned}}
\tag{3.3}
\]

\[
\boxed{
\mathcal G_{sp}(x,r_s)
=55r_s^2(x+2)^2-49x^2.
}
\tag{3.4}
\]

任何 fully coupled candidate 都必须满足

\[
\mathcal N_{sp}\equiv\mathcal O_{sp}\equiv\mathcal G_{sp}\equiv0\pmod p.
\tag{3.5}
\]

---

## 4. `已严格完成`：全部消元只剩两个固定八次 length polynomial

定义

\[
A_{sp}^{(s)}
=4(225sx^2+9s-11)^2-xY_s^2(99x-4),
\]

\[
\mathcal R_{spD}
=220Y_s^4(x+2)^4-49(A_{sp}^{(s)})^2.
\]

先消去 `r_s`，再对 `x` 求 resultant，得到

\[
\boxed{
\operatorname{Res}_x(\mathcal N_{sp},\mathcal R_{spD})
=C\,s^8(9s-11)^8\mathcal P_1(s)\mathcal P_2(s),
}
\tag{4.1}
\]

其中

\[
C=1205534785939344000000000000,
\]

\[
\boxed{
\begin{aligned}
\mathcal P_1(s)={}&
1382549089196025s^8-133844136247800s^7
+3690923035544910s^6\\
&+7960772236243860s^5+3163200960625101s^4
+10662174653755284s^3\\
&+13341353191482096s^2-1874385042496296s
+62480266566916,
\end{aligned}}
\tag{4.2}
\]

\[
\boxed{
\begin{aligned}
\mathcal P_2(s)={}&
363844061254628703225s^8+989345243267031420000s^7\\
&+1615741998157561468590s^6+1886040813505705898580s^5\\
&+1569626813501484989229s^4+956049258626593813836s^3\\
&+390256979886873318384s^2+44160413329248524616s
+1475531078426217604.
\end{aligned}}
\tag{4.3}
\]

对 genuine spontaneous prime，`s(9s-11)` 是单位，因此必须满足

\[
\boxed{
\mathcal P_1(36\cdot10^{M-1})\equiv0
\quad\text{或}\quad
\mathcal P_2(36\cdot10^{M-1})\equiv0\pmod p.}
\tag{4.4}
\]

---

## 5. `已严格完成 / 关键审计`：模 `19` 只有一条 genuine external/spontaneous 解

模 `19`：

\[
\mathcal P_1(s)
\equiv-2(s-9)(s^3-4s^2+6s+3)(s^4-2s^3+2s^2-4s-8),
\]

\[
\mathcal P_2(s)
\equiv-3(s-2)(s+3)^2(s^3+3s^2-4s+6).
\]

直接代回三方程 (3.5)，只有两组单位解：

\[
(s,x,y,r_s)=(2,11,6,9),
\qquad(9,3,7,14).
\tag{5.1}
\]

但 genuine external/spontaneous 还要求 `p∤f`。由

\[
\frac{q5^\lambda}{c_u}
=r_s\frac{x+2}{x},
\tag{5.2}
\]

第一组给

\[
\frac{q5^\lambda}{c_u}\equiv2\pmod{19},
\qquad f/c_u\equiv4\not\equiv0,
\tag{5.3}
\]

而第二组给

\[
\frac{q5^\lambda}{c_u}\equiv-2\pmod{19},
\qquad\boxed{19\mid f}.
\tag{5.4}
\]

所以第二组只是 `f`-denominator boundary，不能计入 genuine III 类。这恰好与

\[
\operatorname{Res}_{r_s}(F_f,\Omega_{sp})
=-200x^3\Delta_0
\]
的理论边界一致。

因此真正的 fixed `19` spontaneous branch 只有

\[
\boxed{(s,x,y,r_s)=(2,11,6,9)\pmod{19}.}
\tag{5.5}
\]

其 Jacobian determinant 为 `1 mod 19`，故唯一 Hensel 提升。前四层 `(s,x,r_s)` 为

\[
\boxed{
(2,11,9),
(2,239,199),
(2890,961,2726),
(50903,48974,16444),
}
\tag{5.6}
\]

对应

\[
\boxed{
M\equiv10\ (18),
82\ (342),
2818\ (6498),
100288\ (123462).
}
\tag{5.7}
\]

所以 `19` 没有被局部 Hensel 排掉，但从“两条分支”严格缩成了**一条 genuine branch**。

---

# 第三部分：fixed `19` 与 secant cofactor 的 prime-power 交点

## 6. `已严格完成`：第一层恰命中左 secant endpoint `J=2`

external common-height double-root 还给

\[
18K-55\equiv0,
\qquad18a_3+55T\equiv0,
\qquad D+18C\equiv0\pmod{19}.
\]

因为 `18≡-1`、`55≡-2 (mod 19)`：

\[
\boxed{
K\equiv2,
\qquad a_3\equiv-2T,
\qquad C\equiv D
\pmod{19}.}
\tag{6.1}
\]

所以 fixed `19` 恰好撞上 rational-root 三点的左端点 `J=2`。

三点 polynomial 为

\[
F(J)=b_2^2TJ(TJ+2a_3)(K-J)^2-Q^2N_0(TJ+a_3)^2.
\]

故

\[
F(2)=4b_2^2T(T+a_3)(K-2)^2-Q^2N_0(2T+a_3)^2,
\tag{6.2}
\]

在 (6.1) 下自动有

\[
\boxed{19^2\mid F(2).}
\tag{6.3}
\]

而 endpoint rational-root factorization 是

\[
\boxed{
\Xi_-=
\frac{-F(2)}{2^{2M+2}5^{\nu_5}(D-C)}.}
\tag{6.4}
\]

因此第一层至少给

\[
v_{19}(D-C)+v_{19}(\Xi_-)\ge2.
\tag{6.5}
\]

---

## 7. `已严格完成`：若 height 与 linear double-root 都进到第二层，则 `19` 只落在 `Xi_-` 一层

令

\[
h=v_{19}(W_q),
\qquad \ell=v_{19}(18K-55).
\]

假设

\[
\boxed{h\ge2,\qquad\ell\ge2.}
\tag{7.1}
\]

由

\[
18qW_q=D(18K-55)+(D+18C)
\]
且 `19∤qD`，得到

\[
19^2\mid D+18C.
\]

但

\[
D-C=(D+18C)-19C,
\]
且 `19∤C`，所以

\[
\boxed{v_{19}(D-C)=1.}
\tag{7.2}
\]

同样，由 `18\alpha=T(18K-55)+(18a_3+55T)`、`alpha=omega W_q` 且 `19∤omega`，(7.1) 强迫

\[
19^2\mid18a_3+55T.
\tag{7.3}
\]

于是

\[
18(K-2)=(18K-55)+19,
\]

\[
18(2T+a_3)=(18a_3+55T)-19T.
\]

在模 `19` 的二阶正规化中：

\[
\frac{K-2}{19}\equiv18^{-1},
\qquad
\frac{2T+a_3}{19}\equiv-18^{-1}T,
\qquad
T+a_3\equiv-T.
\tag{7.4}
\]

另一方面 external prefix norm `R_N≡0` 给

\[
Q^2N_0\equiv3b_2^2\pmod{19}.
\tag{7.5}
\]

把 (7.4)–(7.5) 代入 (6.2)：

\[
\boxed{
\frac{F(2)}{19^2}
\equiv
-\frac{7b_2^2T^2}{18^2}
\not\equiv0\pmod{19}.}
\tag{7.6}
\]

所以

\[
\boxed{v_{19}(F(2))=2.}
\tag{7.7}
\]

结合 (6.4)、(7.2)：

\[
\boxed{v_{19}(\Xi_-)=1.}
\tag{7.8}
\]

而第一层直接代入 `J=3,4` 有

\[
F(3)\equiv-6b_2^2T^2,
\qquad
F(4)\equiv-12b_2^2T^2
\pmod{19},
\tag{7.9}
\]

故

\[
\boxed{19\nmid\Xi_C\Xi_+.}
\tag{7.10}
\]

更精确地，由 `C≡D`：

\[
\frac{\Xi_+}{\Xi_C}
\equiv
\frac{F(4)}{F(3)}\frac{C}{D+C}
\equiv2\cdot\frac12
\equiv1\pmod{19}.
\]

所以

\[
\boxed{\Xi_+\equiv\Xi_C\pmod{19}.}
\tag{7.11}
\]

若

\[
\Delta_-=(\Xi_C-\Xi_-)/(2^m5^d),
\qquad
\Delta_+=(\Xi_+-\Xi_C)/(2^m5^d),
\]
则 `19∤2^m5^d`，于是 fixed deep branch 的 secant allocation 被定向为

\[
\boxed{
19\nmid\Delta_-,
\qquad19\mid\Delta_+.
}
\tag{7.12}
\]

`endpoint-lattice.md` 的 curvature formula

\[
\Delta_--\Delta_+
=2^{m+1}5^dc_u^2\{g((2K-9)T-a_3)-H_0\}
\]
在 `K=2,a_3=-2T,H_0≡0 (mod 19)` 下恰为单位，所以 (7.12) 与已有 curvature 相容；它是新的**非对称 prime allocation**，但尚未单独矛盾。

---

## 8. 当前开放核

本轮对 `19` 的结论应严格分成两层：

1. genuine spontaneous/external 第一层只剩唯一 branch (5.5)；
2. 若其 height 与 linear root 都继续到第二层，则 `19` 在三 secant cofactors 上只能出现为
   \[
   v_{19}(\Xi_-)=1,
   \qquad v_{19}(\Xi_C)=v_{19}(\Xi_+)=0,
   \qquad19\mid\Delta_+,\ 19\nmid\Delta_-.
   \]

因此下一步不应继续扩大 `19^k`。真正值得追的是：

- shallow case `v_{19}(W_q)=1` 与 `W_q/3^δ≡1 (mod 4)` 的 pairing；
- deep case (7.12) 与 additive CRT / `D±C` 的完整 prime-power structure；
- 或把唯一 lifted branch 接回 `C` 的自然代表和 finite-defect shell，寻找 Archimedean incompatibility。

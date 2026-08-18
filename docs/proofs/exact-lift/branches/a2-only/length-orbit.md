# A2 length-orbit and fully coupled spontaneous reduction

> **依赖：** `source-length-resultant.md`、`spontaneous-angle.md`、`decimal-prefix-bridge.md`。
>
> **严格状态：**本文审计 fixed length polynomial 与真实十进制轨道 `36·10^{M-1}` 的 `p`-进同步，并把 spontaneous angle、external double-root 与 prefix norm 全部联立，消去 `r_s,x,y` 后得到两个固定八次 length polynomial。固定 `p=19` 的完整局部系统继续存在，但只剩两条唯一 Hensel 轨道；因此单靠继续升模不能关闭它。本文仍**不宣称 A2 全局关闭**。

---

## 1. `已严格完成 / 降级`：simple length root 只给唯一指数轨道，不自动给空性

设 `F(s)∈Z[s]` 为固定 length polynomial，`p∤10`，且

\[
F(s_0)\equiv0\pmod p,
\qquad
F'(s_0)\not\equiv0\pmod p.
\]

若还存在 `n_0` 使

\[
s_0\equiv36\cdot10^{n_0}\pmod p,
\]

则 Hensel 引理把 `s_0` 唯一提升为 `s_*∈Z_p`。另一方面令

\[
d:=\operatorname{ord}_p(10),
\qquad
u:=v_p(10^d-1).
\]

当 `ν=1` 时，

\[
10^d=1+p u,\qquad u\in\mathbf Z_p^\times,
\]

所以映射

\[
t\longmapsto10^{dt}
\]

在 `1+pZ_p` 上给出一维 `p`-进参数；每个与 `36·10^{n_0}` 同模 `p` 的单位根，若位于这条乘法轨道中，就对应唯一的 `p`-进指数

\[
n=n_0+dt_*.
\]

因此：

\[
\boxed{
\text{simple polynomial root + }v_p(10^d-1)=1
\Longrightarrow
\text{至多一条 }p\text{-进 decimal exponent branch}.}
\tag{1.1}
\]

但“至多唯一”不是“不存在”。若该 branch 实际通过每一级 `p^k`，继续机械升模只会不断固定 `M mod d p^{k-1}`，不会制造新矛盾。

若 `ν>1`，则这是 base-10 Wieferich 型 bad orbit：最初 `ν-1` 层存在额外兼容门；一旦通过，之后仍回到一维唯一 lift。故 generic closure 需要第二个独立全局条件，而不能把 simple-root uniqueness 当成空性。

---

## 2. `已严格完成`：旧 source/external 的 `p=19` branch 永远不会被 length lift 自动杀掉

`source-length-resultant.md` 的固定 quartic在模 `19` 下为

\[
\mathcal L_{SW}(s)\equiv(s-2)(s-8)\pmod{19}.
\]

两个根都 simple。并且

\[
\boxed{
10^{18}=1+15\cdot19\pmod{19^2},
}
\tag{2.1}
\]

故

\[
\boxed{
\operatorname{ord}_{19^k}(10)=18\cdot19^{k-1}
\qquad(k\ge1).
}
\tag{2.2}
\]

也就是说 `10` 的模 `19` 原根轨道完整提升到每个 `19^k`；两个 simple roots 都对应唯一十进制长度分支。

前四层的精确 Hensel/离散指数为：

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

括号中为模数。于是

\[
\boxed{
p=19\text{ 的旧 source/external length route 只刚性化，不排除。}}
\tag{2.4}
\]

后续若仍处理 `19`，必须加入 `D_src` 的完整赋值、spontaneous angle 或另一个 decimal-plane 条件。

---

# 第二部分：把 spontaneous angle 与 external double-root 全部联立

## 3. 三个纯局部方程

继续使用

\[
s:=36\cdot10^{M-1}.
\]

external double-root 的 prefix linear root

\[
36P-11\equiv0\pmod p
\]
给出

\[
y=\frac{a_2}{10^{M-1}}
\equiv\frac{11-9s}{s}\pmod p.
\tag{3.1}
\]

记

\[
Y_s:=11-9s.
\]

`decimal-prefix-bridge.md` 的

\[
\mathscr R_N=324Q^2N_0+2695b_2^2
\]
在除去十进制单位后，化成关于 `(s,x)` 的纯整数式

\[
\boxed{
\mathcal N_{sp}(s,x)
:=(x+2)^2\left(2025s^2x^2+Y_s^2\right)
+10780x^2.
}
\tag{3.2}
\]

`spontaneous-angle.md` 的 `Omega_sp` 清去 `s^2` 分母后化成

\[
\boxed{
\begin{aligned}
\mathcal O_{sp}(s,x,r_s):={}&
r_s\Bigl[
4(225sx^2+9s-11)^2\\
&\qquad-xY_s^2(99x-4)
\Bigr]
+2xY_s^2(x+2).
\end{aligned}}
\tag{3.3}
\]

external discriminant-zero 仍是

\[
\boxed{
\mathcal G_{sp}(x,r_s)
:=55r_s^2(x+2)^2-49x^2.
}
\tag{3.4}
\]

因此 genuine spontaneous + external double-root common carrier 必满足

\[
\boxed{
\mathcal N_{sp}\equiv
\mathcal O_{sp}\equiv
\mathcal G_{sp}\equiv0\pmod p.
}
\tag{3.5}
\]

这已经把 `a_2,P,N_0` 全部消掉；剩余只有 `(s,x,r_s)`。

---

## 4. `已严格完成`：先消去 source ratio，再消去 prefix denominator

定义

\[
\boxed{
\begin{aligned}
A_{sp}^{(s)}(s,x):={}&
4(225sx^2+9s-11)^2\\
&-xY_s^2(99x-4).
\end{aligned}}
\tag{4.1}
\]

由 (3.3)–(3.4) 对 `r_s` 求 resultant，并除去 genuine channel 中的单位 `x^2`，得到

\[
\boxed{
\mathcal R_{spD}(s,x)
:=
220Y_s^4(x+2)^4
-49\left(A_{sp}^{(s)}(s,x)\right)^2.
}
\tag{4.2}
\]

所以 (3.5) 强迫

\[
\mathcal N_{sp}(s,x)\equiv0,
\qquad
\mathcal R_{spD}(s,x)\equiv0.
\tag{4.3}
\]

再对 `x` 求 resultant，精确因子分解为

\[
\boxed{
\operatorname{Res}_x
(\mathcal N_{sp},\mathcal R_{spD})
=C\,s^8(9s-11)^8\mathcal P_1(s)\mathcal P_2(s),
}
\tag{4.4}
\]

其中

\[
C=1205534785939344000000000000
\]

且

\[
\boxed{
\begin{aligned}
\mathcal P_1(s)={}&
1382549089196025s^8
-133844136247800s^7\\
&+3690923035544910s^6
+7960772236243860s^5\\
&+3163200960625101s^4
+10662174653755284s^3\\
&+13341353191482096s^2
-1874385042496296s\\
&+62480266566916,
\end{aligned}}
\tag{4.5}
\]

\[
\boxed{
\begin{aligned}
\mathcal P_2(s)={}&
363844061254628703225s^8
+989345243267031420000s^7\\
&+1615741998157561468590s^6
+1886040813505705898580s^5\\
&+1569626813501484989229s^4
+956049258626593813836s^3\\
&+390256979886873318384s^2
+44160413329248524616s\\
&+1475531078426217604.
\end{aligned}}
\tag{4.6}
\]

对 genuine spontaneous prime，`s` 与

\[
9s-11=-Y_s=-sy
\]

都是单位。因此整个 coupled channel 被压成：

\[
\boxed{
\mathcal P_1(36\cdot10^{M-1})\equiv0
\quad\text{或}\quad
\mathcal P_2(36\cdot10^{M-1})\equiv0
\pmod p.
}
\tag{4.7}
\]

原来的 `(r_s,x,y,a_2,P,N_0)` 全部消失，只剩两个固定 octic × decimal length orbit。

---

## 5. `已严格完成`：`p=19` 的 eliminant 与真实三方程解

模 `19`，两个 octic 分解为

\[
\boxed{
\mathcal P_1(s)
\equiv
-2(s-9)
(s^3-4s^2+6s+3)
(s^4-2s^3+2s^2-4s-8),
}
\tag{5.1}
\]

\[
\boxed{
\mathcal P_2(s)
\equiv
-3(s-2)(s+3)^2
(s^3+3s^2-4s+6).
}
\tag{5.2}
\]

但 eliminant root 不必都回升为原三方程解，所以必须把 (3.5) 直接代回检查。完整枚举 `F_19^×` 后只有两组 genuine solution：

\[
\boxed{
(s,x,y,r_s)\equiv
(2,11,6,9),
\quad
(9,3,7,14)
\pmod{19}.
}
\tag{5.3}
\]

对三方程

\[
(\mathcal N_{sp},\mathcal O_{sp},\mathcal G_{sp})
\]
关于 `(s,x,r_s)` 的 Jacobian determinant，在两点分别为

\[
\boxed{1,\quad10\pmod{19}.}
\tag{5.4}
\]

因此两点都是 nonsingular，且各自唯一 Hensel 提升到 `Z_19^3`。

前四层为：

\[
\boxed{
\begin{array}{c|c|c}
k&\text{branch A }(s,x,r_s)&\text{branch B }(s,x,r_s)\\ \hline
1&(2,11,9)&(9,3,14)\\
2&(2,239,199)&(47,3,356)\\
3&(2890,961,2726)&(47,6140,3966)\\
4&(50903,48974,16444)&(96073,88448,58838)
\end{array}}
\tag{5.5}
\]

而 `10` 在 `19^k` 上仍为原根，所以相应 `n=M-1` / `M` 轨道也是唯一的：

\[
\boxed{
\begin{array}{c|c|c|c}
k&n_A&n_B&\operatorname{ord}_{19^k}(10)\\ \hline
1&9&2&18\\
2&81&200&342\\
3&2817&1226&6498\\
4&100287&46712&123462
\end{array}}
\tag{5.6}
\]

即

\[
M_A=n_A+1,
\qquad M_B=n_B+1.
\]

所以完整 spontaneous + external + prefix-norm 系统在 `19` 上**仍不空**。它不再是一棵分叉 Hensel 树，而是两条唯一局部分支。

---

## 6. `已严格完成 / 审计降级`：继续做 `19^k` 本身不会闭环

(5.4) 已经说明两条 `19`-进解会唯一存在到任意深度；(2.2) 又说明每一个 lifted `s` 都唯一落在 decimal exponent orbit 上。因此：

\[
\boxed{
\text{继续把 }19^4\text{ 升到 }19^{20}
\text{ 只会继续固定 }M,
\text{ 不会产生局部矛盾。}
}
\tag{6.1}
\]

这是一个应明确记录的降级结论。若要杀掉 `19`，必须加入本系统尚未使用的全局输入，例如：

1. `C` 的自然代表 / finite-defect shell；
2. `W_q` 的 primitive parity 与 `Theta_dec` odd carrier；
3. source-excess 的**完整赋值**而非只取第一层 `D_src`；
4. Archimedean endpoint window 与 lifted rational representative 的大小不相容。

---

## 7. 更新后的开放核

经过 `spontaneous-angle.md` 与本文，旧 §14.2 的 III 类 prime 已经从“未知 angle excess”压成两级明确接口：

\[
\boxed{
\Omega_{sp}(x,y,r_s)=0
\Longrightarrow
\mathcal P_1(36\cdot10^{M-1})
\mathcal P_2(36\cdot10^{M-1})\equiv0.
}
\]

其中 fixed `19` 的完整 coupled local branch 已证明存在且唯一，所以它必须由**另一个未使用的全局条件**关闭；generic moving prime 则变成 fixed-octic simple/bad-reduction 与 decimal multiplicative orbit 的问题。

下一步最直接的非重复路线是把 `(5.3)` 的两条 `19`-进 branch 接回

\[
D+18C\equiv0,
\qquad
TK+a_3=\omega W_q,
\qquad
\Theta_{dec}=2^{2M+m+2}\widehat{\mathcal T}_2,
\]

优先利用 `0<C<3D/250` 的真实小代表，而不是继续扩大局部模数。
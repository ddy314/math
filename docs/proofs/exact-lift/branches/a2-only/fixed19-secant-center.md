# A2 fixed-19 secant center and exact gap depth

> **依赖：** `length-orbit.md`、`decimal-prefix-bridge.md`、`endpoint-lattice.md` §§16.29–16.38。
>
> **严格状态：**本文只处理 fully coupled spontaneous/external 通道中剩余的 genuine fixed `p=19` 分支。主要结论是：`19` 是唯一能让 external double-root 与三点 rational-root sieve 的采样点 `J=2,3,4` 发生 inert 端点共振的素数；在二阶 common-height / double-root / prefix-norm 深度下，三 secant cofactor 的 `19`-进中心可以精确求出，并进一步得到 `v_19(Delta_+)=1` 与 `19^2 | T_2`。本文仍**不宣称 A2 全局关闭**。

---

## 1. `19` 是唯一的 inert secant endpoint resonance

external discriminant-zero double-root 已经严格给出

\[
18K-55\equiv0\pmod p.
\tag{1.1}
\]

三点 rational-root sieve 只采样

\[
J=2,3,4.
\]

若 double-root 在模 `p` 下恰撞上某个采样点，即 `K≡J (mod p)`，则

\[
p\mid 55-18J.
\]

逐点只有

\[
\begin{array}{c|c}
J&55-18J\\ \hline
2&19\\
3&1\\
4&-17.
\end{array}
\]

因此对 inert prime `p≡3 (mod 4)`：

\[
\boxed{
K\equiv J\in\{2,3,4\}\pmod p
\Longrightarrow p=19,\ J=2.
}
\tag{1.2}
\]

`p=17` 只会撞 `J=4`，但 `17≡1 (mod 4)`，不属于 odd inert carrier。

height linear target 同时给

\[
18a_3+55T\equiv0\pmod p,
\]
所以

\[
\frac{a_3}{T}\equiv-\frac{55}{18}\pmod p.
\tag{1.3}
\]

于是第二项的 secant factor `JT+a_3` 发生零点时仍要求

\[
p\mid18J-55,
\]
得到同一个列表 `(19, none, 17)`。

第一项还有 `JT+2a_3`。在 (1.3) 下其零点要求

\[
p\mid 9J-55.
\]
对 `J=2,3,4` 分别只可能给 `37,7,19`。其中 `37≡1 (mod4)`；而 `p=7` 不可能进入 discriminant-zero external channel，因为

\[
\left(\frac{55}{7}\right)
=\left(\frac{-1}{7}\right)=-1,
\]
但 external discriminant-zero 必须满足 `(55/p)=1`。因此连第一项的 forced secant degeneration 也只剩

\[
\boxed{p=19,\quad J=2.}
\tag{1.4}
\]

所以 `19` 的特殊性不是有限枚举事故：它是**唯一的 genuine inert secant resonance**。

---

## 2. genuine `19` branch 的纯 decimal fingerprint

`length-orbit.md` 已审计：模 `19` 的两组 eliminant 解中，只有

\[
\boxed{(s,x,y,r_s)=(2,11,6,9)}
\tag{2.1}
\]
是 genuine external/spontaneous；另一组落回 `19|f` 的 denominator boundary。

同时

\[
M\equiv10\pmod{18}.
\tag{2.2}
\]

endpoint defect 记号为

\[
b_2=10^{M-1}+2^{M-1}H,
\qquad
a_2=10^{M-1}-e.
\]

因此

\[
10x-1=\frac{H}{5^{M-1}},
\qquad
1-y=\frac{e}{10^{M-1}}.
\tag{2.3}
\]

由 `ord_19(10)=18`、`10^9≡-1 (mod19)`、`5^9≡1 (mod19)`，(2.1)–(2.3) 给

\[
\boxed{H\equiv14,\qquad e\equiv5\pmod{19}.}
\tag{2.4}
\]

还可恢复完整 prefix residue：

\[
\boxed{
\begin{aligned}
b_2&\equiv4,\\
a_2&\equiv13,\\
C_0=9b_2/2&\equiv-1,\\
N_0=C_0^2+a_2^2&\equiv-1,\\
Q=2\cdot10^M+b_2&\equiv3
\end{aligned}
\pmod{19}.}
\tag{2.5}
\]

归一化 prefix defect / source contact 也都是单位：

\[
\Delta_0=2025x^2-18y-y^2\equiv9\pmod{19},
\tag{2.6}
\]

\[
2025x^2-9y\equiv4\pmod{19}.
\tag{2.7}
\]

所以 genuine `19` branch 在第一层确实与 denominator-prefix、source-contact 分离；它不是旧两类 contact 的伪装。

---

## 3. 二阶 deep branch 的四个 `19`-进中心

从此假设四个 residual 都至少进入第二层：

\[
19^2\mid18K-55,
\tag{3.1}
\]

\[
19^2\mid18a_3+55T,
\tag{3.2}
\]

\[
19^2\mid\mathscr R_N,
\qquad
\mathscr R_N:=324Q^2N_0+2695b_2^2,
\tag{3.3}
\]

\[
19^2\mid D+18C.
\tag{3.4}
\]

这里 `19` 与 `18,324,T,b_2,C` 都互素。定义 dimensionless variables

\[
a:=\frac{a_3}{T},
\qquad
R:=\frac{Q^2N_0}{b_2^2},
\qquad
d_C:=\frac DC.
\]

则 (3.1)–(3.4) 精确给出模 `19^2` 的四个中心：

\[
\boxed{
K\equiv\frac{55}{18},
\qquad
a\equiv-\frac{55}{18},
\qquad
R\equiv-\frac{2695}{324},
\qquad
d_C\equiv-18
\pmod{19^2}.}
\tag{3.5}
\]

在标准代表模 `361` 下即

\[
\boxed{K\equiv344,\quad a\equiv17,\quad R\equiv307,\quad d_C\equiv343.}
\tag{3.6}
\]

注意这只是 `19`-进中心；其中 `R_*=-2695/324<0` 与真实正实数 `R` 不矛盾。它的用途是控制局部 secant cofactor，而不是提供 Archimedean 候选。

---

## 4. 三个 secant 值在中心处可以完全求出

把三点 polynomial 除去公共 `b_2^2T^2`，定义

\[
\phi_J(K,a,R)
:=J(J+2a)(K-J)^2-R(J+a)^2,
\tag{4.1}
\]

于是

\[
F(J)=b_2^2T^2\phi_J.
\tag{4.2}
\]

在精确有理中心

\[
K_*=\frac{55}{18},
\qquad
a_*=-\frac{55}{18},
\qquad R_*=-\frac{2695}{324},
\tag{4.3}
\]
直接得到

\[
\boxed{
\phi_2^*
=\frac{19^2\cdot31}{18^4},
}
\tag{4.4}
\]

\[
\boxed{
\phi_3^*
=-\frac{7\cdot47}{18^4},
}
\tag{4.5}
\]

\[
\boxed{
\phi_4^*
=-\frac{17^2\cdot41}{18^4}.
}
\tag{4.6}
\]

这立即解释了 `length-orbit.md` 的现象：左点 `J=2` 自带**恰两层** `19`，而中心点和右点都是 `19`-进单位。

更重要的是，这些中心值对 (3.1)–(3.3) 的二阶扰动稳定到所需精度：`phi_3,phi_4` 模 `19^2` 只读取中心值；`phi_2/19^2` 模 `19` 也只读取中心值。因此后面的 cofactor ratio 不是一次偶然代值，而是整个二阶 deep residue class 的固定局部型。

---

## 5. 三 cofactor 的中心 ratio

记公共 `2,5` 归一化因子

\[
U_0:=2^{2M+2}5^{\nu_5}.
\]

endpoint-lattice 给

\[
\Xi_-=-\frac{F(2)}{U_0(D-C)},
\qquad
\Xi_C=\frac{F(3)}{U_0C},
\qquad
\Xi_+=\frac{F(4)}{U_0(D+C)}.
\tag{5.1}
\]

在中心 `d_C=-18` 下：

\[
\frac{C}{D-C}=-\frac1{19},
\qquad
\frac{C}{D+C}=-\frac1{17}.
\tag{5.2}
\]

代入 (4.4)–(4.6)：

\[
\boxed{
\left(\frac{\Xi_-}{\Xi_C}\right)_*
=-\frac{19\cdot31}{7\cdot47},
}
\tag{5.3}
\]

\[
\boxed{
\left(\frac{\Xi_+}{\Xi_C}\right)_*
=-\frac{17\cdot41}{7\cdot47}.
}
\tag{5.4}
\]

而

\[
-\frac{17\cdot41}{7\cdot47}-1
=-\frac{54\cdot19}{7\cdot47}.
\tag{5.5}
\]

所以第二个 ratio 与 `1` 的距离**恰含一层 `19`**。

将 (5.3)–(5.4) 化到模 `19^2=361`：

\[
\boxed{
\frac{\Xi_-}{\Xi_C}\equiv323=19\cdot17\pmod{361},
}
\tag{5.6}
\]

\[
\boxed{
\frac{\Xi_+}{\Xi_C}\equiv191=1+19\cdot10\pmod{361}.
}
\tag{5.7}

由于 `Xi_C` 是 `19`-进单位，这重新得到并加强旧结论：

\[
\boxed{v_{19}(\Xi_-)=1,\qquad19\nmid\Xi_C\Xi_+.}
\tag{5.8}
\]

---

## 6. `已严格完成`：右 gap 恰好只有一层 `19`

令

\[
L:=2^m5^d,
\]

\[
\Delta_-:=\frac{\Xi_C-\Xi_-}{L},
\qquad
\Delta_+:=\frac{\Xi_+-\Xi_C}{L}.
\tag{6.1}
\]

`19∤LXi_C`。由 (5.6)–(5.7)：

\[
\frac{L\Delta_-}{\Xi_C}
\equiv1-323
\equiv39
=1+2\cdot19
\pmod{361},
\tag{6.2}
\]

\[
\frac{L\Delta_+}{\Xi_C}
\equiv191-1
\equiv190
=10\cdot19
\pmod{361}.
\tag{6.3}
\]

因此：

\[
\boxed{
v_{19}(\Delta_-)=0,
\qquad
v_{19}(\Delta_+)=1.}
\tag{6.4}
\]

特别地，`length-orbit.md` 原先只有

\[
19\mid\Delta_+,
\]
现在已加强成精确深度：

\[
\boxed{19\Vert\Delta_+.}
\tag{6.5}
\]

并且 normalized right-gap slope 固定为

\[
\boxed{
\frac{\Delta_+}{19}
\equiv10\,\Xi_C L^{-1}\pmod{19}.}
\tag{6.6}
\]

这个结论对所有满足 (3.1)–(3.4) 的更深 lift 都保持不变：继续升到 `19^3,19^4,...` 不会让 `Delta_+` 再获得第二层 `19`。

---

## 7. `已严格完成`：additive cofactor 自动获得第二层 `19`

endpoint-lattice 的 additive curvature 恒等式为

\[
\mathcal T_2
=(D+C)\Delta_+ +(D-C)\Delta_-.
\tag{7.1}
\]

由 (3.5)，模 `361`：

\[
\frac{D+C}{C}\equiv-17,
\qquad
\frac{D-C}{C}\equiv-19.
\tag{7.2}
\]

再用 (6.2)–(6.3)：

\[
\frac{L\mathcal T_2}{C\Xi_C}
\equiv
(-17)(190)+(-19)(39)
=-3971
=-11\cdot361
\equiv0
\pmod{361}.
\]

所以

\[
\boxed{19^2\mid\mathcal T_2.}
\tag{7.3}
\]

所有从 `T_2` 到 `\widetilde T_2`、`\widehat T_2` 的标准 `2,5` 归一化因子都是 `19`-进单位，因此同样有

\[
\boxed{v_{19}(\widehat{\mathcal T}_2)\ge2.}
\tag{7.4}
\]

这不是新的 closure：若 `19` 真要承担 odd inert excess，它仍可能从深度 `3,5,...` 开始。严格新增的信息是：**deep fixed-19 branch 绝不允许 additive cofactor 只含一层 `19`**，而右 secant gap 却永远只含一层。

---

## 8. 为什么继续纯 `19`-进加深不会自动关闭

四个中心若在 `Z_19` 中取精确值

\[
K_*=55/18,
\quad a_*=-55/18,
\quad R_*=-2695/324,
\quad D/C=-18,
\]
则 (5.3)–(5.4) 是精确 `19`-进 ratio，而 (7.1) 的两项正好完全抵消。

等价地，定义

\[
J_*(K,a,R)
:=K^2-(18+4a)K+18a+55-R.
\]
在中心恰有

\[
\boxed{J_*(K_*,a_*,R_*)=0.}
\tag{8.1}
\]

而 `Theta_dec` / `widehat(T)_2` 正是这个 dimensionless cofactor kernel 乘 `19`-进单位尺度。因此 deep local system 本身有一个真正的 `19`-进零中心；不断机械提升局部 congruence 只会趋近这个中心，不会凭空产生矛盾。

所以 fixed `19` 后续必须加入**非局部输入**：例如 `C/D` 的真实小自然代表、`H,e,h` 的 Archimedean defect window，或与 `D±C` 之外的独立 integer divisor system 联立。不能把 (6.5) 再机械提升成“希望有一天 `19^k` 自己消失”。

---

## 9. 更新后的 fixed-19 开放核

对于 genuine fixed `19` spontaneous/external branch：

1. `19` 是唯一可能与 `J=2,3,4` 发生 inert secant endpoint resonance 的 double-root prime；
2. 第一层 decimal fingerprint 固定为
   \[
   M\equiv10\ (18),\ H\equiv14,\ e\equiv5\ (19);
   \]
3. 一旦 common-height / double-root / prefix-norm / natural-representative 都进入第二层，三 gap 精确满足
   \[
   v_{19}(\Delta_-)=0,
   \qquad v_{19}(\Delta_+)=1;
   \]
4. 同时 additive cofactor 至少含两层 `19`：
   \[
   v_{19}(\widehat{\mathcal T}_2)\ge2.
   \]

下一步真正值得打的是把 (2.4) 的真实小十进制缺口 `H,e` 与 (6.6) 的固定 right-gap slope、以及 `C/D<3/250` 放在同一个 integer representative 中，而不是继续做纯局部 Hensel 枚举。
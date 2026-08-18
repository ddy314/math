# A2 universal external secant center

> **依赖：** `decimal-discriminant.md`、`decimal-prefix-bridge.md`、`length-orbit.md`、`fixed19-secant-center.md`、`endpoint-lattice.md` 的三点 rational-root sieve。
>
> **严格状态：**本文把 external discriminant-zero / common-height / prefix-norm / natural-representative 的共同 `p`-进中心代回 `J=2,3,4` 三个 secant cofactor。三个中心值完全因子化后，所有可能的 non-`3` inert secant contact 只剩固定素数 `19` 与 `47`。`19` 已由 `fixed19-secant-center.md` 单列；本文进一步审计 `47`，证明它只给三条 simple unique Hensel branch，而不是新的 singular tree。本文仍**不宣称 A2 全局关闭**。

---

## 1. 四个共同中心与 normalized secant polynomial

在 external discriminant-zero common-height 通道中，若相应 residual 至少在模 `p` 层同时消失，则有

\[
K\equiv K_*:=\frac{55}{18},
\qquad
\frac{a_3}{T}\equiv a_*:=-\frac{55}{18},
\tag{1.1}
\]

\[
\frac{Q^2N_0}{b_2^2}
\equiv R_*:=-\frac{2695}{324},
\qquad
\frac DC\equiv d_*:=-18
\pmod p.
\tag{1.2}
\]

这里第四式来自 natural-representative target `D+18C≡0`；`p∤C`，否则 `p|D` 与 `gcd(C,D)=1` 矛盾。

定义 normalized secant polynomial

\[
\phi_J(K,a,R)
:=J(J+2a)(K-J)^2-R(J+a)^2,
\tag{1.3}
\]

于是

\[
F(J)=b_2^2T^2\phi_J.
\tag{1.4}
\]

对 external prime，`p∤2·3·5·b_2T`，所以 odd-prime support 可以直接在 `phi_J` 上读取。

---

## 2. `已严格完成`：三个中心值完全因子化

在精确有理中心 `(K_*,a_*,R_*)` 上：

\[
\boxed{
\phi_2^*
=\frac{19^2\cdot31}{18^4},
}
\tag{2.1}
\]

\[
\boxed{
\phi_3^*
=-\frac{7\cdot47}{18^4},
}
\tag{2.2}
\]

\[
\boxed{
\phi_4^*
=-\frac{17^2\cdot41}{18^4}.
}
\tag{2.3}
\]

而 `d_*=-18` 给

\[
D-C=-19C,
\qquad
D+C=-17C.
\tag{2.4}
\]

三 cofactor

\[
\Xi_-=-\frac{F(2)}{U_0(D-C)},
\qquad
\Xi_C=\frac{F(3)}{U_0C},
\qquad
\Xi_+=\frac{F(4)}{U_0(D+C)},
\tag{2.5}
\]
其中 `U_0=2^{2M+2}5^{nu_5}`。定义共同 `p`-进单位尺度

\[
\mathcal K_{sec}
:=\frac{b_2^2T^2}{U_0C\,18^4}.
\tag{2.6}
\]

则在中心处精确得到

\[
\boxed{
(\Xi_-^*,\Xi_C^*,\Xi_+^*)
=\mathcal K_{sec}
\bigl(19\cdot31,\,-7\cdot47,\,17\cdot41\bigr).
}
\tag{2.7}
\]

这三个看似复杂的巨大 cofactor 在共同 local center 上只剩六个固定小素数。

---

## 3. 两个 gap 的中心甚至只剩 `17` 与 `19`

由

\[
\Delta_-=(\Xi_C-\Xi_-)/L,
\qquad
\Delta_+=(\Xi_+-\Xi_C)/L,
\qquad L=2^m5^d,
\tag{3.1}
\]
直接相减：

\[
-7\cdot47-19\cdot31
=-918=-54\cdot17,
\tag{3.2}
\]

\[
17\cdot41+7\cdot47
=1026=54\cdot19.
\tag{3.3}
\]

所以

\[
\boxed{
(\Delta_-^*,\Delta_+^*)
=\frac{54\mathcal K_{sec}}L(-17,19).
}
\tag{3.4}
\]

并且 additive cofactor 的中心 cancellation 完全显式：

\[
(D+C)\Delta_+^*+(D-C)\Delta_-^*
\]

\[
=(-17C)(54\cdot19\mathcal K_{sec}/L)
+(-19C)(-54\cdot17\mathcal K_{sec}/L)
=0.
\tag{3.5}
\]

这解释了为什么 pure local deep lifting 能让 `widehat(T)_2` 趋向任意高 `p`-进深度：secant center 本身就是 additive cofactor 的精确 `p`-进零中心。

---

## 4. `已严格完成`：character 过滤后只剩固定 `19` 与 `47`

external discriminant-zero prime 必须满足

\[
\boxed{\left(\frac{55}{p}\right)=1.}
\tag{4.1}
\]

同时我们只关心

\[
p\equiv3\pmod4,
\qquad p\ne3.
\tag{4.2}
\]

逐个检查 (2.7)：

- `31≡3 (mod4)`，但 `(55/31)=-1`，排除；
- `7≡3 (mod4)`，但 `(55/7)=-1`，排除；
- `17,41≡1 (mod4)`，不是 inert carrier；
- `19≡3 (mod4)` 且 `(55/19)=1`；
- `47≡3 (mod4)` 且 `(55/47)=1`。

因此在共同 secant center 上：

\[
\boxed{
\begin{array}{c|c}
\text{object}&\text{possible non-3 inert discriminant-zero prime}\\ \hline
\Xi_-&19\\
\Xi_C&47\\
\Xi_+&\varnothing\\
\Delta_-&\varnothing\\
\Delta_+&19
\end{array}}
\tag{4.3}
\]

所以全部 fixed inert secant contact 被压成

\[
\boxed{\{19,47\}.}
\tag{4.4}
\]

`19` 是 endpoint-factor resonance，已由 `fixed19-secant-center.md` 处理；`47` 是**中心 cofactor cancellation**，不是 `K=J` 型端点共振。

---

# 第二部分：固定 `47` 的 fully coupled spontaneous branch

## 5. `47` 在原三方程中确实存在 genuine 解

沿用 `length-orbit.md` 的三方程：

\[
\mathcal N_{sp}(s,x)=0,
\qquad
\mathcal O_{sp}(s,x,r_s)=0,
\qquad
\mathcal G_{sp}(x,r_s)=0.
\tag{5.1}
\]

直接在 `F_47` 枚举并代回 genuine 分离条件

\[
x(x+2)y\ne0,
\qquad
r_s(x+2)+2x\ne0,
\qquad
\Phi_s(x,r_s)\ne0,
\tag{5.2}
\]
只剩三组：

\[
\boxed{
(s,x,y,r_s)
=(6,1,32,39),
(11,34,39,40),
(46,15,27,35)
\pmod{47}.}
\tag{5.3}
\]

三组的 `(f-line, source-line)` residue 分别为

\[
(25,33),\qquad(4,35),\qquad(14,7),
\tag{5.4}
\]
全部为单位。

相应 normalized base norm、source contact、prefix defect 也全部为单位：

\[
\begin{array}{c|ccc}
(s,x,y)&N_0/10^{2M-2}&D_{src}/10^{2M-2}&\Delta_0\\ \hline
(6,1,32)&41&45&2\\
(11,34,39)&35&43&4\\
(46,15,27)&31&46&14
\end{array}
\pmod{47}.
\tag{5.5}

所以这三组都是真正的 spontaneous/external 第一层解，不是 denominator 或 source boundary。

---

## 6. `已严格完成`：三组 `47` 解全部 nonsingular

对

\[
(\mathcal N_{sp},\mathcal O_{sp},\mathcal G_{sp})
\]
关于 `(s,x,r_s)` 的 Jacobian determinant，三点分别为

\[
\boxed{21,\qquad35,\qquad35\pmod{47}.}
\tag{6.1}
\]

全部非零。因此：

\[
\boxed{p=47\text{ 不产生 singular Hensel tree；只有三条唯一 simple lift。}}
\tag{6.2}
\]

这也解释了为什么 `spontaneous-bad-primes.md` 的 singular-prime 审计没有把 `47` 列为 bad prime：它的特殊性来自 secant center，而不是 octic repeated root。

---

## 7. 三条 `47` branch 都落在真实 decimal orbit

模 `47`：

\[
\operatorname{ord}_{47}(10)=46,
\]
所以 `10` 是 primitive root。解

\[
s=36\cdot10^{M-1}
\]
得到：

\[
\boxed{
\begin{array}{c|c|c}
s&M-1\pmod{46}&M\pmod{46}\\ \hline
6&44&45\\
11&23&24\\
46&19&20
\end{array}}
\tag{7.1}

并且

\[
\boxed{
10^{46}\equiv1+43\cdot47\pmod{47^2},
}
\tag{7.2}
\]
其中 `43` 为单位。因此

\[
\boxed{
\operatorname{ord}_{47^k}(10)=46\cdot47^{k-1}
\qquad(k\ge1).
}
\tag{7.3}

结合 §6，每个第一层解都对应唯一的 `47`-进 decimal exponent branch。和 fixed `19` 一样，继续机械升 `47^k` 只会固定更细的 `M` 同余类，并不会制造局部空性。

---

## 8. `47` 的 secant allocation

在共同 center 上 (2.7)：

\[
\Xi_-^*=589\mathcal K_{sec},
\qquad
\Xi_C^*=-329\mathcal K_{sec}=-7\cdot47\mathcal K_{sec},
\qquad
\Xi_+^*=697\mathcal K_{sec}.
\tag{8.1}

因此若四个 center residual 进一步都进入模 `47^2`，扰动为 `O(47^2)`，而中心 `Xi_C` 恰含一层 `47`；故

\[
\boxed{v_{47}(\Xi_C)=1,}
\tag{8.2}
\]

同时

\[
\boxed{47\nmid\Xi_-\Xi_+\Delta_-\Delta_+.}
\tag{8.3}

事实上模 `47`，去掉共同单位尺度：

\[
\Xi_-\equiv25,
\qquad
\Xi_C\equiv0,
\qquad
\Xi_+\equiv39,
\tag{8.4}

所以

\[
L\Delta_-\equiv-25,
\qquad
L\Delta_+\equiv39
\pmod{47}.
\tag{8.5}

而

\[
(D+C)/C\equiv-17,
\qquad
(D-C)/C\equiv-19,
\]
给

\[
(-17)\cdot39+(-19)\cdot(-25)
=-188=-4\cdot47.
\tag{8.6}

于是 additive cofactor 的第一层仍由两个 unit gap 的**加法 cancellation**产生，而不是某个 gap 自己携带 `47`。

若四个 center residual 都进入 `47^2`，由于 exact center 上 (3.5) 为零，整个 analytic expression 对二阶 perturbation 仍给

\[
\boxed{47^2\mid\mathcal T_2,}
\tag{8.7}

从而标准 `2,5` 归一化后

\[
\boxed{v_{47}(\widehat{\mathcal T}_2)\ge2.}
\tag{8.8}

与 `19` 相比，局部 allocation 完全不同：

\[
\boxed{
\begin{array}{c|cc}
&19&47\\ \hline
\text{secant cofactor carrying one layer}&\Xi_-&\Xi_C\\
\text{gap carrying one layer}&\Delta_+&\text{none}\\
\text{deep additive cofactor}&\ge2&\ge2
\end{array}}
\tag{8.9}

---

## 9. 更新后的 external/secant 开放核

这一层完成了固定 secant-prime 分类：

\[
\boxed{
\text{deep external discriminant-zero secant contact}
\Longrightarrow p\in\{19,47\}
}
\]
对 non-`3` inert prime 而言成立于共同 center 支持上。

- `19`：唯一 endpoint resonance，右 gap 精确一层；
- `47`：唯一 center-cofactor cancellation，三条 genuine simple local branches；
- 其余 genuine moving simple prime 不会从三点 secant center 获得固定 inert factor。

这仍未关闭 moving simple spontaneous carrier。下一步应把 generic `p\notin\{19,47\}` 从 secant 系统剥离后，直接研究 `Omega_sp` 与 `Theta_dec` 的共同 prime support；固定 `19/47` 则应使用真实 defect window `(H,e,h,C)`，而不是继续局部升模。
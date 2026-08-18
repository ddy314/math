# A2 spontaneous prefix branch-collision 审计

> **依赖：** `spontaneous-prefix-eliminant.md`。
>
> **严格状态：**本文解释两个 prefix quadratic gate `Q_1,Q_2` 的共同根究竟代表什么。结果是：除固定 coefficient prime `11` 外，branch collision 只有两种机制——`A_-=0` 是拼接分子/分母同时为零的 common-`alpha` 退化；另一种是 `2K-9=0` 的 `Theta_dec` 中心退化，其 pure-prefix 方程正是 `C_*=0`。因此在真正 `p∤alpha` 且 `p∤2K-9` 的 pure-spontaneous channel，两条 quadratic branch 严格互斥。本文仍**不宣称 A2 全局关闭**。

---

## 1. 记号

沿用 `spontaneous-prefix-eliminant.md`：

\[
\tau=10^{-M},
\qquad
x=\frac{b_2}{10^M},
\qquad
y=\frac{a_2}{10^{M-1}},
\]

\[
d=225x^2-y,
\]

\[
A_{\rm sp}=4d^2-xy^2(99x-4),
\]

\[
A_-=A_{\rm sp}-2y^2(x+2)^2,
\]

\[
\Delta_0=2025x^2-18y-y^2.
\]

第三块消元后的两个 primitive gate 为

\[
\mathcal Q_1(\tau;x,y)=0,
\qquad
\mathcal Q_2(\tau;x,y)=0.
\]

定义

\[
\boxed{
\begin{aligned}
C_*={}&164025x^4+656100x^3
+2381x^2y^2+41400x^2y\\
&+842400x^2+324xy^2+324y^2.
\end{aligned}}
\tag{1.1}
\]

---

## 2. `已严格完成`：一次 subresultant 直接给出 branch-collision 二分

对 `Q_1,Q_2` 关于 `tau` 取 subresultant sequence。次数为 `1` 的项精确化为

\[
\boxed{
\begin{aligned}
\mathcal S_1
={}&198000\,x^2y^3(x+2)^2d\,A_-A_{\rm sp}\\
&\cdot\bigl(2(y+9)-9\tau\bigr).
\end{aligned}}
\tag{2.1}
\]

这里

\[
198000=2^4\cdot3^2\cdot5^3\cdot11.
\]

所以对 genuine non-`3` carrier，并进一步排除 fixed coefficient prime `11`，旧分离条件给

\[
p\nmid x y(x+2)dA_{\rm sp}.
\]

若同一个 `tau` 同时满足

\[
\mathcal Q_1\equiv\mathcal Q_2\equiv0\pmod p,
\]
则 subresultant 必为零，因此只有

\[
\boxed{
A_-\equiv0
\quad\text{或}\quad
9\tau\equiv2(y+9)
\pmod p.
}
\tag{2.2}
\]

这比只看最终 resultant 更强：它直接恢复共同根的几何位置。

---

## 3. `已严格完成`：`A_-=0` 恰是 concatenated numerator/denominator 双零

`spontaneous-prefix-eliminant.md` 已证明，在 `Omega_sp=0` 下

\[
\boxed{
\bar w:=\frac{w}{10^M}
=-\frac{A_{\rm sp}}{2y^2(x+2)}.
}
\tag{3.1}
\]

若

\[
A_-=A_{\rm sp}-2y^2(x+2)^2=0,
\]
则

\[
\boxed{
\bar w=-(x+2).
}
\tag{3.2}
\]

而真实拼接分母是

\[
TQ+b_3
=T10^M\bigl((x+2)+\bar w\bigr),
\]
所以

\[
\boxed{p\mid TQ+b_3.}
\tag{3.3}
\]

另一方面 exact sphere 的 scale-free 形式为

\[
x^2\bar w^2(9+y+\bar\zeta)^2
=(2+x+\bar w)^2
\left(
\frac{2025x^2+y^2}{100}\bar w^2
+x^2\bar\zeta^2
\right),
\tag{3.4}
\]

其中

\[
\bar\zeta=\frac{a_3}{T10^M}.
\]

由 (3.2)，右边整个平方因子消失；而 genuine channel 中 `x\bar w` 为单位，因此

\[
9+y+\bar\zeta\equiv0\pmod p.
\]

于是

\[
TK+a_3
=T10^M(9+y+\bar\zeta)
\equiv0\pmod p.
\]
即

\[
\boxed{
A_-=0
\Longrightarrow
p\mid(TQ+b_3)
\quad\text{且}\quad
p\mid\alpha:=TK+a_3.
}
\tag{3.5}
\]

所以 `A_-` collision branch 不是 pure spontaneous。它精确落回 `spontaneous-angle.md` §7 已分出的 common-`alpha` channel；若当前定义 genuine pure spontaneous 为

\[
p\nmid\alpha,
\]
则

\[
\boxed{p\nmid A_-.}
\tag{3.6}
\]

这一排除不需要 external discriminant-zero 假设，比 `spontaneous-prefix-eliminant.md` 中的 external resultant 更一般。

---

## 4. `已严格完成`：另一种 collision 恰是 `2K-9=0` 中心线

由

\[
K=10^M(9+y)=\frac{9+y}{\tau},
\]
(2.2) 的第二种可能

\[
9\tau=2(y+9)
\]
正好等价于

\[
\boxed{2K-9=0.}
\tag{4.1}
\]

记

\[
\boxed{\tau_c:=\frac{2(y+9)}9.}
\tag{4.2}
\]

把 `tau_c` 直接代回两个 exact quadratic gate，得到

\[
\boxed{
\mathcal Q_1(\tau_c)
=-\frac{2}{81}y^3(x+2)^2C_*,
}
\tag{4.3}
\]

\[
\boxed{
\mathcal Q_2(\tau_c)
=\frac{2}{81}y^3(x+2)^2\Delta_0C_*.
}
\tag{4.4}
\]

所以在 genuine prefix-defect separation `p∤y(x+2)Delta_0` 下：

\[
\boxed{
\tau=\tau_c,
\quad
\mathcal Q_1=\mathcal Q_2=0
\iff
C_*=0.
}
\tag{4.5}
\]

这解释了为什么 `C_*` 在两个 quadratic 的 resultant 中只出现一次：它就是 non-generic linear solve `2K-9=0` 的中心退化 locus。

---

## 5. `已严格完成`：`C_*` 直接由中心 `Theta` 方程恢复

在 `2K-9=0` 下

\[
K=\frac92,
\qquad
\tau=\tau_c.
\]

`Theta_dec` 的线性 `a_3` 项消失，只剩

\[
\mathcal R_\Theta
=B^2(K^2-18K+55)-Q^2N_0.
\]

由于

\[
K^2-18K+55=-\frac{23}{4},
\]
中心必要条件为

\[
-\frac{23}{4}B^2-Q^2N_0\equiv0.
\tag{5.1}
\]

把

\[
B=10^Mx,
\qquad
Q=10^M(x+2),
\qquad
N_0=\frac{10^{2M}}{100}(2025x^2+y^2),
\]
以及

\[
10^M=\frac{9}{2(y+9)}
\]
代入，清去单位后恰得到

\[
\boxed{
81(x+2)^2(2025x^2+y^2)
+2300x^2(y+9)^2=0.
}
\tag{5.2}
\]

展开 (5.2) 正是

\[
\boxed{C_*=0.}
\tag{5.3}
\]

因此 branch-resultant 的 `C_*` 与 `Theta_dec` central gate 是同一个对象，不应被计作两个独立 obstruction。

---

## 6. `已严格完成`：pure-spontaneous noncentral branch 严格互斥

综合 §§2–5。设 `p` 满足：

\[
p\equiv3\pmod4,
\qquad
p\notin\{3,5,11\},
\]

并处于 genuine pure-spontaneous channel：

\[
p\nmid x y(x+2)dA_{\rm sp}\Delta_0\alpha,
\]

且非中心：

\[
p\nmid2K-9.
\]

如果 `Q_1,Q_2` 同时为零，则 (2.2) 只能进入：

- `A_-=0`，但 §3 强迫 `p|alpha`，矛盾；
- `tau=tau_c`，但这等价于 `2K-9=0`，矛盾。

故

\[
\boxed{
\text{genuine pure-spontaneous + noncentral}
\Longrightarrow
\text{恰至多命中 }\mathcal Q_1,\mathcal Q_2\text{ 中的一支。}
}
\tag{6.1}
\]

结合 `spontaneous-prefix-eliminant.md` 已知至少一支必须命中，所以实际上：

\[
\boxed{
\text{generic common carrier 精确选择唯一一个 prefix quadratic branch。}
}
\tag{6.2}
\]

这里的“唯一”仍不是“不存在”；单支可以继续有 simple p-adic root。

---

## 7. `已严格完成 / no-go`：中心 sphere quadratic 的判别式自动是平方

中心线 `2K-9=0` 不能靠再加一个 Legendre character 关闭。

先只代入

\[
K=\frac92,
\qquad
10^M=\frac{9}{2(y+9)},
\]
以及 `Omega_sp` 给出的 `w`，暂不要求 `C_*=0`。把 exact sphere 看成关于

\[
\zeta=\frac{a_3}{T}
\]
的二次式。其 discriminant 精确为

\[
\boxed{
\begin{aligned}
\operatorname{disc}_{\zeta}
={}&\Bigl[
10497600\,x^2y^3(x+2)^2(y+9)\\
&\qquad\cdot(225x^2-y)A_-A_{\rm sp}
\Bigr]^2.
\end{aligned}}
\tag{7.1}
\]

也就是说中心 sphere 的两个 `zeta` root 在函数域 `Q(x,y)` 中已经是有理的；这里没有新的 quadratic-character obstruction。

所以 `C_*=0` 中心支若要关闭，必须继续利用：

- genuine/source/denominator separation；
- `tau=10^{-M}` 的真实 decimal orbit；
- 或 natural representative / finite-defect shell；

不能再从 sphere discriminant 收一次 Legendre 条件。

---

## 8. 更新后的开放核

`spontaneous-prefix-eliminant.md` 把第三块消成两个 quadratic；本文进一步证明：

\[
\boxed{
\begin{array}{ccl}
A_-=0
&\Longleftrightarrow&
\text{concatenated numerator/denominator 双零通道},\\
C_*=0
&\Longleftrightarrow&
\text{Theta central line }2K-9=0.
\end{array}}
\]

因此当前真正 generic 的 pure-spontaneous carrier 已变成：

\[
\boxed{
\begin{gathered}
p\notin\{3,5,11\},
\qquad p\nmid\alpha(2K-9),\\
\text{恰有一个 }i\in\{1,2\}
\text{ 使 }\mathcal Q_i(10^{-M};x,y)\equiv0\pmod p.
\end{gathered}}
\]

下一步最自然的对象已经不是第三块，也不是 branch resultant，而是**单个 quadratic branch 与真实 decimal prefix orbit 的同步**。应分别研究 `Q_1`、`Q_2` 的 repeated-root kernel 和它们与 `D_src / Delta_pref / C` 的 resultant；中心 `C_*` 与 fixed `11` 单列。

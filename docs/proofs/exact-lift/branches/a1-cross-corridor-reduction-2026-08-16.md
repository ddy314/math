# A1 double-nonresonant cross-corridor reduction — 2026-08-16

本文继续 `a1-resonance-collapse-2026-08-16.md`，研究其中唯一可能承载无界尾长的 double-nonresonant sector。

核心结论：双非 resonance 的四个赋值象限中，有两个象限固定前缀下自动有限；真正可能无限的只剩两条交叉走廊。

本文结论均为 **已严格完成**，最后一节给出新的剩余核心。

---

## 1. 固定阈值坐标

沿用

\[
x=u-\ell,
\qquad
y=v-\ell,
\]

以及 decade window

\[
\boxed{
10^{g-1}\le h2^x5^y<10^g.
}
\tag{1}
\]

二进 resonance 阈值为

\[
\boxed{
 x_*=v_2(K)-1-g-v_2(Q)-v_2(N),
}
\tag{2}
\]

五进 resonance 阈值为

\[
\boxed{
 y_*=v_5(K)-g-v_5(Q)-v_5(N).
}
\tag{3}
\]

在 denominator square

\[
W^2=T(TK-2b_3DN)
\]

中，二进两项的赋值分别为

\[
e_2=\ell+v_2(K),
\]

\[
f_2=1+u+g+v_2(Q)+v_2(N).
\]

代入 `u=\ell+x`，得到

\[
f_2-e_2=x-x_*.
\]

因此

\[
\boxed{
\begin{aligned}
x>x_*&\iff e_2<f_2,\\
x=x_*&\iff e_2=f_2,\\
x<x_*&\iff e_2>f_2.
\end{aligned}
}
\tag{4}
\]

完全不再含 `\ell`。

同理五进有

\[
e_5=\ell+v_5(K),
\]

\[
f_5=v+g+v_5(Q)+v_5(N),
\]

且

\[
f_5-e_5=y-y_*.
\]

所以

\[
\boxed{
\begin{aligned}
y>y_*&\iff e_5<f_5,\\
y=y_*&\iff e_5=f_5,\\
y<y_*&\iff e_5>f_5.
\end{aligned}
}
\tag{5}
\]

这说明 A1 的 2/5-adic 位置图在 `(x,y)` 平面中就是两条固定直线

\[
x=x_*,
\qquad y=y_*.
\]

---

## 2. `++` 象限固定前缀下有限

考虑

\[
 x>x_* ,
\qquad y>y_*.
\]

因为 `x,y` 为整数，

\[
x\ge x_*+1,
\qquad y\ge y_*+1.
\]

另一方面 decade window 上界给出

\[
h2^x5^y<10^g.
\]

固定 `h,g,x_*,y_*` 后，若固定 `y\ge y_*+1`，则

\[
2^x<\frac{10^g}{h5^{y_*+1}},
\]

所以 `x` 有统一上界。

同理 `x\ge x_*+1` 给出 `y` 的统一上界。

因此

\[
\boxed{
(x>x_*,\ y>y_*)
\text{ 与 decade window 的整数交集有限。}
}
\tag{6}
\]

每个固定 `(x,y)` 又令

\[
\rho=h2^x5^y
\]

固定，故按照 resonance-collapse 中相同的 rational-contact argument，每个 `(h,x,y,\pm)` 至多对应一个 `\ell`。

所以整个 `++` 象限固定前缀下严格有限。

---

## 3. `--` 象限固定前缀下有限

考虑

\[
 x<x_* ,
\qquad y<y_*.
\]

于是

\[
x\le x_*-1,
\qquad y\le y_*-1.
\]

此时 decade window 下界

\[
h2^x5^y\ge10^{g-1}
\]

反过来给出两个坐标的下界。

例如使用 `y\le y_*-1`：

\[
h2^x5^{y_*-1}
\ge h2^x5^y
\ge10^{g-1},
\]

故

\[
2^x
\ge
\frac{10^{g-1}}{h5^{y_*-1}},
\]

从而 `x` 有统一下界。

对称地，使用 `x\le x_*-1` 得到 `y` 的统一下界。

因此

\[
\boxed{
(x<x_*,\ y<y_*)
\text{ 与 decade window 的整数交集有限。}
}
\tag{7}
\]

再由固定 `(x,y)` 后 `\rho` 固定、`r_3` 固定、既约分母必须等于 `b_3` 的 argument，每个状态至多一个 `\ell`。

所以整个 `--` 象限固定前缀下严格有限。

---

## 4. 只有两个交叉象限能出现无穷整数偏移

剩余两个 double-nonresonant 象限为

\[
\boxed{
\mathcal C_{2+5-}:
\quad x>x_*,\ y<y_*
}
\tag{8}
\]

以及

\[
\boxed{
\mathcal C_{2-5+}:
\quad x<x_*,\ y>y_*.
}
\tag{9}
\]

在第一条走廊中，`x` 可以向 `+\infty` 增长，同时 `y` 向 `-\infty` 补偿，使

\[
h2^x5^y
\]

继续停留在一个固定十进制 decade 中。

第二条走廊完全对称：`x\to-\infty`、`y\to+\infty`。

由于

\[
\frac{\log2}{\log5}\notin\mathbf Q,
\]

单凭实数位数窗无法把这两条走廊截成有限整数集；这正是剩余的近 `S`-unit / Diophantine approximation 现象。

因此：

\[
\boxed{
\text{任何真正的 A1 无界尾族，只可能位于这两个 cross corridors 中。}
}
\tag{10}
\]

---

## 5. cross corridors 中的平方赋值奇偶锁

虽然两个交叉走廊仍可能无限，但 square certificate 已给出奇偶锁。

### 5.1 `\mathcal C_{2+5-}`

这里

\[
x>x_*\iff e_2<f_2,
\]

所以二进低赋值来自 `TK` 项。平方赋值要求

\[
\boxed{v_2(K)\equiv0\pmod2}.
\tag{11}
\]

另一方面

\[
y<y_*\iff f_5<e_5,
\]

五进低赋值来自 `2b_3DN` 项，因此

\[
\boxed{
\ell+v+g+v_5(Q)+v_5(N)
\equiv0\pmod2.
}
\tag{12}
\]

利用 `v=\ell+y`，化成

\[
\boxed{
y+g+v_5(Q)+v_5(N)\equiv0\pmod2.}
\tag{13}
\]

所以该走廊中的奇偶条件同样已经与 `\ell` 解耦。

### 5.2 `\mathcal C_{2-5+}`

这里二进由 `b_3` 项给出低赋值，因此

\[
\ell+1+u+g+v_2(Q)+v_2(N)
\equiv0\pmod2.
\]

代入 `u=\ell+x`：

\[
\boxed{
1+x+g+v_2(Q)+v_2(N)
\equiv0\pmod2.
}
\tag{14}
\]

五进则由 `TK` 项给出低赋值，所以必须

\[
\boxed{v_5(K)\equiv0\pmod2.}
\tag{15}
\]

因此若

\[
v_2(K)\text{ 为奇数},
\]

第一条 cross corridor `\mathcal C_{2+5-}` 整体为空；若

\[
v_5(K)\text{ 为奇数},
\]

第二条 cross corridor `\mathcal C_{2-5+}` 整体为空。

特别地若

\[
\boxed{v_2(K),v_5(K)\text{ 均为奇数},}
\]

则两个可能无界的 cross corridors 都为空，而其余 resonance / same-direction sectors 已经固定前缀有限。

所以这类前缀完全不存在无界 A1 尾族。

---

## 6. universal factor-pair identity

整数平方证书还有一个对 cross corridor 很有用的等价形式。

由

\[
W^2=T^2K-2Tb_3DN
\]

和

\[
K=G^2C^2-D^2N
\]

直接得到

\[
T^2G^2C^2-W^2
=T^2D^2N+2Tb_3DN.
\]

因此

\[
\boxed{
(TGC-W)(TGC+W)
=TDN(TD+2b_3).
}
\tag{16}
\]

又因为

\[
TD=10^{m_3}Q,
\]

可写成

\[
\boxed{
(TGC-W)(TGC+W)
=10^{m_3}Q\,N\,(10^{m_3}Q+2b_3).
}
\tag{17}
\]

左侧是两个中心在 `TGC`、间距 `2W` 的整数因子；右侧则由十进制主尺度和真实第三分母构成。

这个 factor-pair identity 将是继续攻击两个 cross corridors 的主算术入口之一。

---

## 7. A1 当前唯一可能的无界尾核心

经过 rational contact、denominator funnel、resonance collapse 和本文件，A1 的无界尾问题已经严格缩成两个一维 cross corridors：

\[
\boxed{
\mathcal C_{2+5-}:
\quad
x>x_*,\ y<y_*,
\quad v_2(K)\text{ 必须为偶数},
}
\]

\[
\boxed{
\mathcal C_{2-5+}:
\quad
x<x_*,\ y>y_*,
\quad v_5(K)\text{ 必须为偶数}.
}
\]

每条走廊还同时满足：

\[
10^{g-1}\le h2^x5^y<10^g,
\qquad h\mid Q^2G,
\]

相应的 parity congruence (13) 或 (14)，以及 factor-pair identity (16)。

其余 A1 tail sectors 都已证明不能承载固定前缀下的无界 `\ell`。

下一步只需针对这两个交叉走廊加入平方单位部分的局部二次剩余条件，以及利用 (16) 研究两因子的 `2/5` prime-flow；无需再回到完整四象限。

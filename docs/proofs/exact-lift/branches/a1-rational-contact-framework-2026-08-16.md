# A1 rational-contact framework — 2026-08-16

本文只研究 `A_1`-only 分支，并以原始拼接恒等式重新建立一套不依赖 Gaussian flip 的主框架。

状态约定：

- 标为 **已严格完成** 的结论均直接由原问题定义与初等代数推出；
- 标为 **审计警告** 的内容指出旧统一正规化中需要重新核查的步骤；
- 标为 **待证** 的内容是当前 A1 真正剩余的无界核心。

依赖：

- `../problem-and-carrier.md` 的原问题与 carrier 分支划分；
- `../notation.md` 的统一记号；
- `a1-only.md` 的旧 A1 基线。

---

## 1. A1 位数参数的精确消元（已严格完成）

A1 条件为

\[
s_3\le 0,\qquad s_2+s_3>0.
\]

记

\[
g=-s_3\ge 0,\qquad k=s_2+s_3\ge 1.
\]

则

\[
\boxed{s_2=k+g}.
\]

另一方面旧稿定义的有效第三尾长为

\[
\ell=m_3-g.
\]

但 A1 中

\[
n_3=m_3+s_3=m_3-g,
\]

所以实际上有精确恒等式

\[
\boxed{\ell=n_3}.
\]

因此

\[
\boxed{m_3=g+n_3},
\qquad
\boxed{k=s_2-g=n_2-m_2-g}.
\]

特别地

\[
\boxed{0\le g\le s_2-1=n_2-m_2-1}.
\]

这说明：对固定前两块数据，`g` 从一开始就是有限的；A1 中真正可能随着第三块增长的是 `n_3=\ell`。

这不是全局有限性结论，因为前两块本身仍可变化。

---

## 2. carrier 给出的第二个 `g` 上界（已严格完成）

A1 中

\[
\Lambda_2=10^{-g}\le 1,
\]

故

\[
\Lambda_2r_2<R,
\qquad
r_3<R.
\]

正权平均要等于 `R`，第一坐标必须严格承担 carrier：

\[
\boxed{10^k r_1>R>r_2}.
\]

于是

\[
r_2<10^k r_1.
\]

利用位数粗界

\[
10^{s_i-1}<r_i<10^{s_i+1}
\]

得到

\[
10^{k+g-1}<r_2<10^k r_1<10^{k+s_1+1},
\]

从而

\[
\boxed{g\le s_1+1}.
\]

所以 A1 必须满足

\[
\boxed{s_1\ge -1}.
\]

若 `n_1\le m_1-2`，A1 立即为空。

还有更精确的 carrier 必要条件：

\[
10^{2k}r_1^2>R^2>r_1^2+r_2^2,
\]

故

\[
\boxed{
\frac{r_2}{10^k r_1}
<\sqrt{1-10^{-2k}}.
}
\]

这是一个完全由前两块决定的薄环筛选条件。

---

## 3. 前两块压成单一 rational contact 参数（已严格完成）

定义前两分母拼接

\[
\boxed{Q=b_1 10^{m_2}+b_2}
\]

以及前两分子拼接

\[
\boxed{C=a_1 10^{n_2}+a_2}.
\]

旧 A1 coefficient 中

\[
10^{g+k+m_2}a_1+a_2
\]

由于 `g+k=s_2=n_2-m_2`，恰好就是上面的 `C`。因此 A1 的 numerator coefficient 与 `g` 无关。

再记

\[
\boxed{D=10^gQ},
\qquad
\boxed{P=\frac CD}.
\]

因为 `\ell=n_3`，原始三块拼接可精确写成

\[
\boxed{\alpha=10^{\ell}C+a_3},
\]

\[
\boxed{\beta=10^{\ell}D+b_3}.
\]

令

\[
r=r_3=\frac{a_3}{b_3},
\qquad
\boxed{\theta=\frac{b_3}{10^{\ell}D}}
=\frac{b_3}{10^{m_3}Q}.
\]

由于 `b_3` 恰有 `m_3` 位，

\[
\boxed{
\frac1{10Q}\le\theta<\frac1Q.
}
\]

于是 exact lift 的拼接比严格化成

\[
\boxed{
R=\frac{P+\theta r}{1+\theta}.
}
\]

换言之，整个 A1 是前两块 rational number `P` 与第三分数 `r_3` 的一次严格 mediant/contact。

因为 `R>r_3`，上式立刻给出

\[
\boxed{P>R>r_3}.
\]

并且

\[
\boxed{
\frac{P-R}{R-r_3}=\theta
\in\left[\frac1{10Q},\frac1Q\right).
}
\]

这条比例关系是后续 A1 的主几何坐标。

---

## 4. A1 universal rational-contact quadratic（已严格完成）

定义前两平方和

\[
\boxed{S=r_1^2+r_2^2}.
\]

球面条件为

\[
R^2=S+r^2.
\]

把

\[
R=\frac{P+\theta r}{1+\theta}
\]

代入并清理，得到关于 `r=r_3` 的二次式

\[
\boxed{
(1+2\theta)r^2
-2\theta P r
+(1+\theta)^2S-P^2
=0.
}
\]

其判别式为

\[
\boxed{
\Delta_r
=4(1+\theta)^2
\left(P^2-(1+2\theta)S\right).
}
\]

由于 `r_3` 是有理数，必要条件是

\[
\boxed{
\Xi:=P^2-(1+2\theta)S
\text{ 是非负有理平方}.
}
\]

这是 A1 的统一判别平方；它直接来自原始拼接和球面，不使用第三块 Gaussian 正规化。

特别地，由

\[
\theta\ge\frac1{10Q}
\]

得到纯前缀必要条件

\[
\boxed{
P^2\ge
\left(1+\frac1{5Q}\right)S.
}
\]

即

\[
\boxed{
\left(\frac{C}{10^gQ}\right)^2
\ge
\left(1+\frac1{5Q}\right)
(r_1^2+r_2^2).
}
\]

因此 `g` 还满足一个纯前缀上界：若右侧比值小于 1，则该 `g` 直接排除；等价地

\[
\boxed{
10^{2g}
\le
\frac{C^2}{Q^2S(1+1/(5Q))}.
}
\]

由于每增加 `g` 一次，`P^2` 精确缩小 `100` 倍，这个筛选对 A1 很强。

若 `\Xi=z^2`，则第三分数只能取

\[
\boxed{
 r
=
\frac{
\theta P\pm(1+\theta)z
}{1+2\theta}.
}
\]

因此在固定 `(prefix,g,\theta)` 后，`r_3` 至多只有两个候选。

---

## 5. saturated `L=1` 的重新参数化（已严格完成）

旧稿中 saturated 定义为

\[
L=1,
\]

亦即

\[
10^{\ell}\mid b_3.
\]

写成

\[
\boxed{b_3=10^{\ell}\tau}.
\]

### 5.1 `g=0` 的 saturated 支为空

若 `g=0`，则 `m_3=\ell`，而 `b_3` 是 `\ell` 位整数，所以

\[
b_3<10^{\ell}.
\]

这与 `10^\ell\mid b_3` 矛盾。因此

\[
\boxed{L=1\Longrightarrow g\ge1}.
\]

### 5.2 `\tau` 恰为 `g` 位整数

当 `g\ge1` 时，由 `m_3=g+\ell` 得

\[
10^{g+\ell-1}\le b_3<10^{g+\ell}.
\]

除以 `10^\ell`：

\[
\boxed{10^{g-1}\le\tau<10^g}.
\]

此时

\[
\boxed{\theta=\frac\tau D},
\qquad D=10^gQ.
\]

关键点是：在 saturated 支中，`\theta` 已完全脱离 `\ell`。

---

## 6. saturated integer-square certificate（已严格完成）

统一判别平方变成

\[
\Xi
=
\frac{C^2}{D^2}
-
\left(1+\frac{2\tau}{D}\right)
\frac{\mathcal N_{12}}{G^2},
\]

其中

\[
G=b_1b_2,
\qquad
\mathcal N_{12}=(a_1b_2)^2+(a_2b_1)^2,
\qquad
S=\frac{\mathcal N_{12}}{G^2}.
\]

故

\[
\boxed{
\Xi
=
\frac{
G^2C^2-D(D+2\tau)\mathcal N_{12}
}{D^2G^2}.
}
\]

若 `\Xi` 是有理平方，则存在整数 `W\ge0` 使

\[
\boxed{
W^2
=G^2C^2-D(D+2\tau)\mathcal N_{12}.
}
\]

这把 saturated A1 直接压成一个整数平方条件。

记

\[
K=G^2C^2-D^2\mathcal N_{12}.
\]

则等价于

\[
\boxed{
W^2=K-2D\mathcal N_{12}\tau.
}
\]

因此

\[
\boxed{
\tau=\frac{K-W^2}{2D\mathcal N_{12}}.
}
\]

并且 `\tau` 还必须同时落在

\[
10^{g-1}\le\tau<10^g.
\]

所以 saturated 支的 `\tau` 不再是自由变量：它由一个处在明确区间、明确同余类中的整数平方 `W^2` 决定。

等价的差平方分解是

\[
\boxed{
(GC-W)(GC+W)
=D(D+2\tau)\mathcal N_{12}.
}
\]

这给出一个新的 divisor-pair 入口。

---

## 7. saturated 第三分母整除证书（已严格完成）

由二次根公式，在 `\Xi=(W/(DG))^2` 时，

\[
\boxed{
 r_3
=
\frac{
G\tau C\pm(D+\tau)W
}{DG(D+2\tau)}.
}
\]

而 `r_3=a_3/b_3` 已经是既约分数。因此它的既约分母必须整除上式的整数分母：

\[
\boxed{
 b_3\mid DG(D+2\tau).
}
\]

在 saturated 支 `b_3=10^\ell\tau`，故得到

\[
\boxed{
10^\ell\tau
\mid
10^gQ\,G\,(10^gQ+2\tau).
}
\]

这是一个不使用 `a_3/\delta_3` 正规化的 denominator-only certificate。

它立即表明：固定前两块、`g` 与 `\tau` 后，`\ell` 有显式有限上界；更强地，实际 `b_3` 必须是右侧固定整数的因子。

因此 saturated A1 对固定前缀已经归约为严格有限问题：

1. `g` 落在 §§1–4 的有限集合；
2. `\tau` 是 `g` 位整数并满足 §6 的整数平方条件；
3. `b_3=10^\ell\tau` 必须整除 `DG(D+2\tau)`；
4. `r_3` 由 §7 根式唯一恢复并检查位数、正号、既约性。

再次强调：这只证明 fixed-prefix finite reduction，不推出所有前缀的并集有限。

---

## 8. 对旧 `z_3=a_3/\delta_3` 正规化的审计警告

旧统一框架定义

\[
\delta_3=\gcd(10^\ell,b_3)
\]

后又写

\[
z_3=\frac{a_3}{\delta_3}
\]

并在 primitive tail quadratic 中按

\[
a_3=\delta_3z_3
\]

使用。

但原问题始终假设

\[
\gcd(a_3,b_3)=1.
\]

由于 `\delta_3\mid b_3`，必有

\[
\boxed{\gcd(a_3,\delta_3)=1}.
\]

所以除非 `\delta_3=1`，不能无条件断言 `z_3` 为整数，也不能无条件使用 `a_3=\delta_3z_3` 作为整数本原化。

因此：

\[
\boxed{
\text{A1 后续不把旧 primitive-tail quadratic 当作已验证入口；}
}
\]

本文 §§3–7 的 rational-contact 与 saturated certificate 完全绕开该问题。

这项审计也可能影响公共框架中的相应语句，但本文只记录 A1 的安全替代路线，不在此修改其他分支状态。

---

## 9. 当前 A1 证明树

现在可以把 A1 压成下面的结构：

\[
\text{A1 exact lift}
\]

\[
\Downarrow
\]

\[
\boxed{
\ell=n_3,
\quad
0\le g\le\min(s_2-1,s_1+1)
}
\]

\[
\Downarrow
\]

\[
\boxed{
P=\frac{C}{10^gQ},
\quad
\theta=\frac{b_3}{10^{m_3}Q}
\in[1/(10Q),1/Q)
}
\]

\[
\Downarrow
\]

\[
\boxed{
P^2-(1+2\theta)S=z^2\in\mathbf Q_{\ge0}^2
}
\]

\[
\Downarrow
\]

\[
\boxed{
P^2\ge(1+1/(5Q))S
}
\]

然后分成：

### non-saturated `L>1`

仍需把 `\theta=b_3/(10^{m_3}Q)` 的十进制分母结构与 rational-square 条件结合，寻找 prefix-uniform 的排除机制。

状态：**待证**。

### saturated `L=1`

已经进一步化为

\[
\boxed{
W^2=G^2C^2-D(D+2\tau)\mathcal N_{12}
}
\]

和

\[
\boxed{
10^\ell\tau\mid DG(D+2\tau),
\qquad
10^{g-1}\le\tau<10^g.
}
\]

状态：**已严格归约到 fixed-prefix finite divisor/square system；全局 prefix-uniform 空性仍待证**。

---

## 10. 下一步最值得攻击的核心

A1 已经没有必要继续围绕 Gaussian flip。优先级应为：

1. **saturated square congruence**：研究
   \[
   W^2\equiv G^2C^2\pmod D,
   \qquad D=10^gQ,
   \]
   与 `10^{g-1}\le\tau<10^g` 的兼容性；
2. **difference-of-squares factor split**：利用
   \[
   (GC-W)(GC+W)=D(D+2\tau)\mathcal N_{12}
   \]
   把 `2`、`5` 的深赋值强迫进入两个极接近因子之一；
3. **non-saturated rational-square sieve**：直接在
   \[
   P^2-(1+2\theta)S=z^2
   \]
   上研究 `\theta=b_3/(10^{m_3}Q)` 的十进制近似结构；
4. 任何有限枚举只用于验证由上述理论先给出的有界切片，不把 fixed-prefix finite reduction 误写为全局空性。

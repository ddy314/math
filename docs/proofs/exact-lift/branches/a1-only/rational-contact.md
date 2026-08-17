# A1 rational contact, denominator funnel and corridor reduction

> 本文件是按数学依赖整合的规范编辑入口。每个来源笔记只在本文件中保留一次；来源边界、原状态和公式正文均保留，避免日期文件之间形成平行副本。

## 整合顺序

`a1-rational-contact-framework-2026-08-16.md` → `a1-denominator-funnel-2026-08-16.md` → `a1-resonance-collapse-2026-08-16.md` → `a1-cross-corridor-reduction-2026-08-16.md` → `a1-cross-corridor-primitive-collapse-2026-08-16.md` → `a1-safe-integer-gap-recovery-2026-08-16.md`

---

## 1. A1 rational-contact framework — 2026-08-16

> 整合来源：`a1-rational-contact-framework-2026-08-16.md`。以下正文保留该来源的原始证明状态和审计边界。

本文只研究 `A_1`-only 分支，并以原始拼接恒等式重新建立一套不依赖 Gaussian flip 的主框架。

状态约定：

- 标为 **已严格完成** 的结论均直接由原问题定义与初等代数推出；
- 标为 **审计警告** 的内容指出旧统一正规化中需要重新核查的步骤；
- 标为 **待证** 的内容是当前 A1 真正剩余的无界核心。

依赖：

- `../../problem-and-carrier.md` 的原问题与 carrier 分支划分；
- `../../notation.md` 的统一记号；
- `core.md` 的旧 A1 基线。

---

### 1. A1 位数参数的精确消元（已严格完成）

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

### 2. carrier 给出的第二个 `g` 上界（已严格完成）

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

### 3. 前两块压成单一 rational contact 参数（已严格完成）

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

### 4. A1 universal rational-contact quadratic（已严格完成）

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

### 5. saturated `L=1` 的重新参数化（已严格完成）

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

#### 5.1 `g=0` 的 saturated 支为空

若 `g=0`，则 `m_3=\ell`，而 `b_3` 是 `\ell` 位整数，所以

\[
b_3<10^{\ell}.
\]

这与 `10^\ell\mid b_3` 矛盾。因此

\[
\boxed{L=1\Longrightarrow g\ge1}.
\]

#### 5.2 `\tau` 恰为 `g` 位整数

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

### 6. saturated integer-square certificate（已严格完成）

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

### 7. saturated 第三分母整除证书（已严格完成）

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

### 8. 对旧 `z_3=a_3/\delta_3` 正规化的审计警告

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

### 9. 当前 A1 证明树

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

#### non-saturated `L>1`

仍需把 `\theta=b_3/(10^{m_3}Q)` 的十进制分母结构与 rational-square 条件结合，寻找 prefix-uniform 的排除机制。

状态：**待证**。

#### saturated `L=1`

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

### 10. 下一步最值得攻击的核心

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

---

## 2. A1 universal denominator funnel — 2026-08-16

> 整合来源：`a1-denominator-funnel-2026-08-16.md`。以下正文保留该来源的原始证明状态和审计边界。

本文件继续 `rational-contact.md`，从其中的 universal rational-contact 判别式推出一个覆盖 saturated 与 non-saturated 的整数平方证书和第三分母 prime-supply 约束。

以下各节均为 **已严格完成**，最后一节列出尚未关闭的无界核心。

---

### 1. 记号

沿用 A1 rational-contact 框架：

\[
T=10^\ell=10^{n_3},
\qquad
D=10^gQ,
\]

\[
C=a_1 10^{n_2}+a_2,
\qquad
G=b_1b_2,
\]

\[
N=\mathcal N_{12}
=(a_1b_2)^2+(a_2b_1)^2,
\]

\[
P=\frac CD,
\qquad
S=\frac N{G^2},
\]

以及

\[
\theta=\frac{b_3}{TD}.
\]

记

\[
\boxed{K=G^2C^2-D^2N}.
\]

A1 rational-contact 判别平方是

\[
\Xi=P^2-(1+2\theta)S=z^2
\]

对某个 `z\in\mathbf Q_{\ge0}`。

---

### 2. universal integer-square certificate

直接代入 `P,S,\theta`：

\[
\Xi
=
\frac{C^2}{D^2}
-
\left(1+\frac{2b_3}{TD}\right)\frac N{G^2}.
\]

通分得到

\[
\boxed{
\Xi
=
\frac{TK-2b_3DN}{T D^2G^2}.
}
\]

因此

\[
z^2
=
\frac{TK-2b_3DN}{T(DG)^2}.
\]

两边乘以 `T^2D^2G^2`：

\[
(zTDG)^2
=T(TK-2b_3DN).
\]

右侧是整数；有理数的平方若为整数，则该有理数本身为整数。因此存在整数 `W\ge0` 满足

\[
\boxed{
W=zTDG
}
\]

以及

\[
\boxed{
W^2
=T(TK-2b_3DN)
=T^2K-2Tb_3DN.
}
\]

这是覆盖整个 A1 的整数平方证书。

特别地必须有

\[
\boxed{TK-2b_3DN\ge0}.
\]

因为

\[
b_3\ge10^{m_3-1}=10^{g+\ell-1}=10^{g-1}T,
\]

故得到纯前缀必要条件

\[
TK
\ge
2\cdot10^{g-1}T\cdot D N,
\]

即

\[
\boxed{
K\ge2\cdot10^{2g-1}QN.
}
\]

这与 rational-contact 框架中的

\[
P^2\ge\left(1+\frac1{5Q}\right)S
\]

完全等价。

---

### 3. universal root formula

由

\[
\Xi=z^2=\left(\frac{W}{TDG}\right)^2
\]

以及

\[
r_3
=
\frac{\theta P\pm(1+\theta)z}{1+2\theta}
\]

代入

\[
\theta=\frac{b_3}{TD},
\qquad
P=\frac CD,
\]

得到

\[
\boxed{
 r_3
=
\frac{
TG b_3 C
\pm
(TD+b_3)W
}{
TDG(TD+2b_3)
}.
}
\]

原问题中

\[
r_3=\frac{a_3}{b_3}
\]

已经既约，因此其既约分母 `b_3` 必须整除上述整数分母：

\[
\boxed{
 b_3\mid TDG(TD+2b_3).
}
\]

展开右侧并模 `b_3` 化简：

\[
TDG(TD+2b_3)
\equiv
T^2D^2G
\pmod{b_3}.
\]

于是得到更干净的 universal denominator certificate：

\[
\boxed{
 b_3\mid T^2D^2G.
}
\]

由于

\[
T=10^\ell,
\qquad
D=10^gQ,
\]

还可写成

\[
\boxed{
 b_3\mid10^{2m_3}Q^2G.
}
\]

这里使用了 `m_3=g+\ell`。

---

### 4. 第三分母的非十进制 prime supply 被前缀完全控制

令

\[
b_3=2^u5^v h,
\qquad
\gcd(h,10)=1.
\]

由

\[
b_3\mid10^{2m_3}Q^2G
\]

立刻得到

\[
\boxed{h\mid Q^2G}.
\]

更逐素数地，对每个奇素数 `p\ne5`，

\[
\boxed{
 v_p(b_3)
\le
2v_p(Q)+v_p(G).
}
\]

所以 A1 中第三分母的所有非 `2,5` 素数以及其指数，都由前两块的

\[
Q^2G
\]

控制。

这比“固定前缀下第三分母只有有限新奇素数”更具体：第三分母一定处在

\[
\boxed{
 b_3=h2^u5^v,
\qquad
h\mid Q^2G,
\quad\gcd(h,10)=1
}
\]

这一 near-`S`-unit funnel 中。

固定前缀后 `h` 只有有限多个选择；所有无界性只能来自 `2`、`5` 指数 `u,v`。

---

### 5. 2/5-adic parity split

整数平方证书

\[
W^2=T(TK-2b_3DN)
\]

对 `p\in\{2,5\}` 给出直接的赋值奇偶约束。

记

\[
e_p=v_p(TK)=\ell+v_p(K).
\]

再记

\[
f_2=v_2(2b_3DN)
=1+u+g+v_2(Q)+v_2(N),
\]

\[
f_5=v_5(2b_3DN)
=v+g+v_5(Q)+v_5(N).
\]

若 `e_p\ne f_p`，则

\[
v_p(TK-2b_3DN)=\min(e_p,f_p).
\]

由于 `W^2` 的 `p`-进赋值必须为偶数，得到

\[
\boxed{
\ell+\min(e_p,f_p)\equiv0\pmod2
\qquad(e_p\ne f_p).
}
\]

展开可分成：

#### `p=5`

若

\[
\ell+v_5(K)
<
v+g+v_5(Q)+v_5(N),
\]

则必须

\[
\boxed{v_5(K)\equiv0\pmod2}.
\]

若反向严格不等式成立，则必须

\[
\boxed{
\ell+v+g+v_5(Q)+v_5(N)
\equiv0\pmod2.
}
\]

相等时进入五进 resonance：

\[
\boxed{
\ell+v_5(K)
=v+g+v_5(Q)+v_5(N).
}
\]

#### `p=2`

若

\[
\ell+v_2(K)
<
1+u+g+v_2(Q)+v_2(N),
\]

则必须

\[
\boxed{v_2(K)\equiv0\pmod2}.
\]

若反向严格不等式成立，则必须

\[
\boxed{
\ell+1+u+g+v_2(Q)+v_2(N)
\equiv0\pmod2.
}
\]

相等时进入二进 resonance：

\[
\boxed{
\ell+v_2(K)
=1+u+g+v_2(Q)+v_2(N).
}
\]

因此整个 A1 的 2/5 无界尾部自然分成四类：

1. 二进非 resonance、五进非 resonance；
2. 仅二进 resonance；
3. 仅五进 resonance；
4. 双 resonance。

这给出了一个与 DD 分支类似、但由 A1 自身 rational-contact 方程直接产生的赋值分层。

---

### 6. saturated 支作为 universal funnel 的特例

若 `L=1`，则

\[
b_3=T\tau.
\]

代入 universal square certificate：

\[
W^2
=T^2(K-2\tau DN).
\]

所以 `T\mid W`。写

\[
W=T W_0,
\]

得到

\[
\boxed{
W_0^2
=K-2\tau DN
=G^2C^2-D(D+2\tau)N,
}
\]

恰好恢复 `rational-contact.md` 中 saturated integer-square certificate。

同理 universal denominator certificate 给出

\[
T\tau\mid T^2D^2G.
\]

而 saturated 专用根公式还能给出更锋利的

\[
T\tau\mid DG(D+2\tau).
\]

所以两个新框架彼此一致。

---

### 7. 当前无界核心

经过本文件，A1 的第三分母已被严格压入

\[
\boxed{
 b_3=h2^u5^v,
\qquad h\mid Q^2G
}
\]

并同时受

\[
\boxed{
W^2=T^2K-2Tb_3DN
}
\]

控制。

因此真正需要继续关闭的对象已经缩成：

\[
\boxed{
(h,u,v,\ell)
\text{ 的 near-}S\text{-unit square system}
}
\]

其中 `h` 来自固定前缀有限因子集，所有无界性集中在 `u,v,\ell`，并且二进、五进各自只有“低侧 / 高侧 / resonance”三种赋值位置。

下一步应优先证明：

- 双非 resonance 区域是否能由赋值奇偶 + 位数窗直接排空；
- 单 resonance 是否强迫一个 `2^a5^b` 近等式，从而只剩有限 offset；
- 双 resonance 是否能把 `u,v` 都线性锁定到 `\ell+g`，再用 `b_3` 的位数窗排除。

这些仍为 **待证**，不能把 fixed-prefix near-`S`-unit funnel 误写成 A1 已关闭。

---

## 3. A1 resonance collapse — 2026-08-16

> 整合来源：`a1-resonance-collapse-2026-08-16.md`。以下正文保留该来源的原始证明状态和审计边界。

本文继续：

- `rational-contact.md`；
- `rational-contact.md`。

目标是把 A1 denominator funnel 中所有至少含一个 `2`/`5` resonance 的尾部彻底压成固定前缀下的有限状态，并精确说明为什么这些状态不能承载 `\ell\to\infty`。

除最后的“剩余核心”外，本文结论均为 **已严格完成**。

---

### 1. 统一偏移坐标

由 denominator funnel，写

\[
\boxed{b_3=h2^u5^v},
\qquad
\gcd(h,10)=1,
\qquad
h\mid Q^2G.
\]

同时

\[
T=10^\ell=2^\ell5^\ell,
\qquad
m_3=g+\ell.
\]

定义两个尾赋值偏移

\[
\boxed{x=u-\ell},
\qquad
\boxed{y=v-\ell}.
\]

于是

\[
\boxed{
\frac{b_3}{T}=h2^x5^y.
}
\]

而 `b_3` 恰有 `m_3=g+\ell` 位，因此

\[
10^{g+\ell-1}\le b_3<10^{g+\ell}.
\]

除以 `T=10^\ell`，得到整个 A1 的统一 decade window：

\[
\boxed{
10^{g-1}
\le h2^x5^y
<10^g.
}
\tag{1}
\]

这是后面把 resonance 从一条无限直线压成有限整数点的关键。

---

### 2. 二进 resonance 精确锁定 `x`

沿用 denominator funnel 的记号

\[
K=G^2C^2-D^2N,
\qquad
D=10^gQ.
\]

二进 resonance 条件为

\[
\ell+v_2(K)
=
1+u+g+v_2(Q)+v_2(N).
\]

代入 `u=\ell+x`，消去 `\ell`：

\[
\boxed{
x=x_2^*}
\]

其中

\[
\boxed{
 x_2^*
=
v_2(K)-1-g-v_2(Q)-v_2(N).
}
\tag{2}
\]

所以二进 resonance 不只是控制赋值的增长率，而是把 `u-\ell` 精确固定成前缀常数。

把 (2) 代回 decade window (1)：

\[
10^{g-1}
\le h2^{x_2^*}5^y
<10^g.
\]

取对数可得

\[
\frac{(g-1)\log10-\log h-x_2^*\log2}{\log5}
\le y
<
\frac{g\log10-\log h-x_2^*\log2}{\log5}.
\]

这个实区间的长度恰为

\[
\frac{\log10}{\log5}
=1+\frac{\log2}{\log5}
<2.
\]

因此：

\[
\boxed{
\text{固定前缀与 }h\text{ 后，二进 resonance 至多留下两个整数 }y.
}
\tag{3}
\]

---

### 3. 五进 resonance 精确锁定 `y`

五进 resonance 条件为

\[
\ell+v_5(K)
=
v+g+v_5(Q)+v_5(N).
\]

代入 `v=\ell+y`，消去 `\ell`：

\[
\boxed{y=y_5^*}
\]

其中

\[
\boxed{
 y_5^*
=
v_5(K)-g-v_5(Q)-v_5(N).
}
\tag{4}
\]

代回 decade window：

\[
10^{g-1}
\le h2^x5^{y_5^*}
<10^g.
\]

于是

\[
\frac{(g-1)\log10-\log h-y_5^*\log5}{\log2}
\le x
<
\frac{g\log10-\log h-y_5^*\log5}{\log2}.
\]

区间长度为

\[
\frac{\log10}{\log2}
=1+\frac{\log5}{\log2}
<4.
\]

因此：

\[
\boxed{
\text{固定前缀与 }h\text{ 后，五进 resonance 至多留下四个整数 }x.
}
\tag{5}
\]

---

### 4. 双 resonance 更强：偏移唯一

若二进、五进同时 resonance，则

\[
\boxed{(x,y)=(x_2^*,y_5^*)}
\]

完全由前缀唯一确定。

此时只需检查一次 decade window

\[
10^{g-1}
\le h2^{x_2^*}5^{y_5^*}<10^g.
\]

若不成立，整个双 resonance 状态立即为空。

若成立，定义

\[
\boxed{\rho=h2^{x_2^*}5^{y_5^*}}.
\]

则

\[
\boxed{b_3=T\rho}.
\]

尽管 `\rho` 未必是整数，它是一个由前缀唯一确定的正有理数。

---

### 5. 任意单 resonance 都把 `b_3/T` 压成有限集合

二进 resonance 时，由 §2，`x=x_2^*`，而 `y` 至多两个可能值；因此

\[
\boxed{
\rho:=\frac{b_3}{T}=h2^x5^y
}
\]

只可能落在一个至多两元素集合中。

五进 resonance 时同理，`y=y_5^*`，`x` 至多四个可能值，因此 `\rho` 至多有四个值。

双 resonance 则至多一个值。

所以：

\[
\boxed{
\text{任意至少含一个 resonance 的 A1 状态，固定前缀与 }h\text{ 后，}
\rho=b_3/T\text{ 只有有限多个值。}
}
\tag{6}
\]

注意这一步没有使用任何有限枚举；有限性直接来自 resonance 等式和十进制位数窗。

---

### 6. 固定 `\rho` 后 `r_3` 也被固定

A1 rational-contact 参数为

\[
\theta=\frac{b_3}{TD}.
\]

若

\[
b_3=T\rho,
\]

则

\[
\boxed{\theta=\frac\rho D}
\]

与 `\ell` 无关。

而前缀 `P=C/D`、`S=N/G^2` 也均固定。故判别平方

\[
P^2-(1+2\theta)S=z^2
\]

若成立，则二次根公式给出的

\[
 r_3
=
\frac{\theta P\pm(1+\theta)z}{1+2\theta}
\]

也是固定有理数，至多两个符号候选。

写其既约形式为

\[
\boxed{r_3=\frac pq},
\qquad
\gcd(p,q)=1.
\]

原问题本身规定 `r_3=a_3/b_3` 已经既约，因此必须有

\[
\boxed{b_3=q}.
\tag{7}
\]

但另一方面

\[
b_3=T\rho=10^\ell\rho.
\]

把 `\rho=A/B` 写成既约正有理数，(7) 变成

\[
10^\ell\frac AB=q.
\]

所以

\[
\boxed{
10^\ell=\frac{qB}{A}.
}
\tag{8}
\]

右端是固定有理数。

因此每个固定 `(prefix,h,\rho,\pm)` 状态至多存在一个 `\ell`，并且只有当右端恰为十的非负整数幂时才可能存在。

于是得到本文核心结论：

\[
\boxed{
\text{A1 中所有至少含一个 }2/5\text{ resonance 的尾部，固定前缀后均无无界 }\ell\text{ 族。}
}
\tag{9}
\]

这比“固定前缀有限”更精确：对每一个 resonance offset 状态与根号符号，`\ell` 至多一个。

---

### 7. resonance 扇区的严格状态

综合 denominator funnel 中 `h\mid Q^2G`：

1. `h` 取自固定前缀的有限因子集；
2. 二进 resonance：每个 `h` 至多两个 `y`；
3. 五进 resonance：每个 `h` 至多四个 `x`；
4. 双 resonance：每个 `h` 至多一个 `(x,y)`；
5. 每个 offset 状态至多两个 `r_3` 根；
6. 每个根至多一个 `\ell`。

所以：

\[
\boxed{
\text{含 resonance 的全部 A1 扇区已经归约为显式、可审计的 fixed-prefix finite certificate。}
}
\]

这里仍不能推出所有前缀的并集有限；该结论的用途是严格证明：任何真正的 A1 无界尾族都只能藏在**二进、五进同时非 resonance**的区域。

---

### 8. 新的唯一无界尾核心

因此 A1 尾部的真正无限核心已经缩为

\[
\boxed{
\text{double-nonresonant sector}
}
\]

即同时满足

\[
\ell+v_2(K)
\ne
1+u+g+v_2(Q)+v_2(N),
\]

\[
\ell+v_5(K)
\ne
v+g+v_5(Q)+v_5(N),
\]

以及

\[
b_3=h2^u5^v,
\qquad h\mid Q^2G,
\]

\[
10^{g-1}\le h2^{u-\ell}5^{v-\ell}<10^g,
\]

\[
W^2=T^2K-2Tb_3DN.
\]

下一步不应再同时处理四个赋值扇区；只需专攻这个 double-nonresonant core。

---

## 4. A1 double-nonresonant cross-corridor reduction — 2026-08-16

> 整合来源：`a1-cross-corridor-reduction-2026-08-16.md`。以下正文保留该来源的原始证明状态和审计边界。

本文继续 `rational-contact.md`，研究其中唯一可能承载无界尾长的 double-nonresonant sector。

核心结论：双非 resonance 的四个赋值象限中，有两个象限固定前缀下自动有限；真正可能无限的只剩两条交叉走廊。

本文结论均为 **已严格完成**，最后一节给出新的剩余核心。

---

### 1. 固定阈值坐标

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

### 2. `++` 象限固定前缀下有限

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

### 3. `--` 象限固定前缀下有限

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

### 4. 只有两个交叉象限能出现无穷整数偏移

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

### 5. cross corridors 中的平方赋值奇偶锁

虽然两个交叉走廊仍可能无限，但 square certificate 已给出奇偶锁。

#### 5.1 `\mathcal C_{2+5-}`

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

#### 5.2 `\mathcal C_{2-5+}`

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

### 6. universal factor-pair identity

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

### 7. A1 当前唯一可能的无界尾核心

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

---

## 5. A1 cross-corridor primitive collapse — 2026-08-16

> 整合来源：`a1-cross-corridor-primitive-collapse-2026-08-16.md`。以下正文保留该来源的原始证明状态和审计边界。

本文继续 `rational-contact.md`，证明其中最后两条可能无界的 cross corridors 实际也不能承载固定前缀下的无界尾族。

关键新输入只有一个：原问题中的第三分数

\[
r_3=\frac{a_3}{b_3}
\]

始终是既约分数。

本文结论均为 **已严格完成**。

---

### 1. 归一化第三块

记

\[
T=10^\ell,
\qquad
\rho=\frac{b_3}{T},
\qquad
\eta=\frac{a_3}{T}.
\]

于是

\[
r_3=\frac{\eta}{\rho}.
\]

由

\[
b_3=h2^{\ell+x}5^{\ell+y}
\]

有

\[
\boxed{\rho=h2^x5^y}.
\]

A1 rational-contact 判别式给出

\[
V^2=K-2\rho DN
\tag{1}
\]

对某个 `V\in\mathbf Q`。这里可以直接取

\[
V=\frac WT,
\]

因为 denominator-funnel 中

\[
W^2=T^2K-2Tb_3DN
=T^2(K-2\rho DN).
\]

由 rational-contact 根公式，归一化分子满足

\[
\boxed{
\eta
=
\rho\,
\frac{
G\rho C\pm(D+\rho)V
}{DG(D+2\rho)}.
}
\tag{2}
\]

所有 `C,D,G,N,K` 都只由固定前两块与 `g` 决定。

---

### 2. 第一交叉走廊 `\mathcal C_{2+5-}` 的二进结构

该走廊定义为

\[
x>x_*,
\qquad y<y_*.
\]

由 `x>x_*`，在 (1) 中二进赋值由 `K` 项严格主导：

\[
v_2(K)<v_2(2\rho DN).
\]

平方存在首先要求

\[
\boxed{k_2:=v_2(K)\text{ 为偶数}.}
\]

并且

\[
\boxed{v_2(V)=\frac{k_2}{2}.}
\tag{3}
\]

记

\[
d_2=v_2(D),
\qquad
g_2=v_2(G),
\qquad c_2=v_2(C).
\]

若

\[
x>d_2,
\]

则

\[
v_2(D+\rho)=d_2,
\qquad
v_2(D+2\rho)=d_2,
\]

因为

\[
v_2(\rho)=x>d_2,
\qquad
v_2(2\rho)=x+1>d_2.
\]

由 (2)，方括号中两项的二进赋值分别为

\[
g_2+c_2+x
\]

与

\[
d_2+\frac{k_2}{2}.
\]

因此无论是否发生额外抵消，都有

\[
v_2\!\left(
G\rho C\pm(D+\rho)V
\right)
\ge
\min\left(
g_2+c_2+x,\ d_2+\frac{k_2}{2}\right).
\]

代回 (2)：

\[
\boxed{
 v_2(\eta)
\ge
x+
\min\left(
g_2+c_2+x,\ d_2+\frac{k_2}{2}\right)
-(2d_2+g_2).
}
\tag{4}
\]

当

\[
x>d_2+\frac{k_2}{2}-g_2-c_2,
\]

最小值已经固定为第二项，故

\[
\boxed{
 v_2(\eta)
\ge
x-d_2-g_2+\frac{k_2}{2}.
}
\tag{5}
\]

特别地，若再有

\[
x>d_2+g_2-\frac{k_2}{2},
\]

则

\[
\boxed{v_2(\eta)>0.}
\tag{6}
\]

---

### 3. 既约性与 (6) 直接矛盾

在第一交叉走廊中

\[
u=\ell+x.
\]

只要

\[
u>0,
\]

就有

\[
2\mid b_3.
\]

由于

\[
\gcd(a_3,b_3)=1,
\]

必有

\[
v_2(a_3)=0.
\]

所以

\[
\boxed{
 v_2(\eta)
=v_2(a_3)-v_2(T)
=-\ell
\le0.
}
\tag{7}
\]

这与 (6) 矛盾。

因此定义显式阈值

\[
\boxed{
X_{\max}
=
\max\left(
 d_2,
 d_2+\frac{k_2}{2}-g_2-c_2,
 d_2+g_2-\frac{k_2}{2},
 -\ell
\right)
}
\]

时最后一项不适合做前缀常数；更干净地分两步写：

- 若 `x\ge0`，则自动 `u=\ell+x>0`；
- 对 `x<0`，只有有限多个 `x` 落在 `x_*<x<0`。

故真正可能向 `+\infty` 延伸的部分满足 `x\ge0`，并且一旦

\[
\boxed{
 x>
X_0:=
\max\left(
0,
 d_2,
 d_2+\frac{k_2}{2}-g_2-c_2,
 d_2+g_2-\frac{k_2}{2}
\right),
}
\tag{8}
\]

便产生 (6) 与 (7) 的矛盾。

所以：

\[
\boxed{
\mathcal C_{2+5-}
\text{ 中所有可行整数 }x\text{ 都有固定前缀上界。}
}
\tag{9}
\]

结合 decade window，固定 `x` 后 `y` 落在长度小于 `2` 的区间，因此 `y` 也只有有限多个值。

于是第一交叉走廊固定前缀下严格有限。

---

### 4. 第二交叉走廊 `\mathcal C_{2-5+}` 的五进结构

现在考虑

\[
x<x_*,
\qquad y>y_*.
\]

由 `y>y_*`，(1) 中五进赋值由 `K` 项严格主导：

\[
v_5(K)<v_5(2\rho DN).
\]

平方存在要求

\[
\boxed{k_5:=v_5(K)\text{ 为偶数},}
\]

并且

\[
\boxed{v_5(V)=\frac{k_5}{2}.}
\tag{10}
\]

记

\[
d_5=v_5(D),
\qquad g_5=v_5(G),
\qquad c_5=v_5(C).
\]

若

\[
y>d_5,
\]

由于 `2` 是五进单位，

\[
v_5(D+\rho)=d_5,
\qquad
v_5(D+2\rho)=d_5.
\]

由 (2) 得

\[
\boxed{
 v_5(\eta)
\ge
 y+
\min\left(g_5+c_5+y,\ d_5+\frac{k_5}{2}\right)
-(2d_5+g_5).
}
\tag{11}
\]

一旦

\[
y>d_5+\frac{k_5}{2}-g_5-c_5,
\]

有

\[
 v_5(\eta)
\ge
 y-d_5-g_5+\frac{k_5}{2}.
\]

若再有

\[
y>d_5+g_5-\frac{k_5}{2},
\]

便得到

\[
\boxed{v_5(\eta)>0.}
\tag{12}
\]

另一方面，只要

\[
v=\ell+y>0,
\]

就有 `5\mid b_3`，既约性强迫

\[
v_5(a_3)=0,
\]

所以

\[
\boxed{v_5(\eta)=-\ell\le0,}
\tag{13}
\]

与 (12) 矛盾。

如第一走廊一样，所有 `y<0` 且 `y_*<y<0` 的状态本来就是有限的；真正可能向 `+\infty` 延伸的部分有 `y\ge0`。因此定义

\[
\boxed{
Y_0=
\max\left(
0,
 d_5,
 d_5+\frac{k_5}{2}-g_5-c_5,
 d_5+g_5-\frac{k_5}{2}
\right),
}
\tag{14}
\]

则任何可行解必须满足

\[
\boxed{y\le Y_0.}
\tag{15}
\]

固定 `y` 后 decade window 把 `x` 限制在长度小于 `4` 的整数区间。

所以第二交叉走廊固定前缀下也严格有限。

---

### 5. 两条 cross corridors 均不能承载无界尾族

结合 §§2–4：

\[
\boxed{
\mathcal C_{2+5-}
\text{ 的 }x\text{ 有显式前缀上界};
}
\]

\[
\boxed{
\mathcal C_{2-5+}
\text{ 的 }y\text{ 有显式前缀上界}.
}
\]

再结合 decade window，两个走廊的另一坐标也随之只剩有限整数集合。

固定 `(h,x,y)` 后

\[
\rho=h2^x5^y
\]

固定，进而 `\theta=\rho/D` 固定，rational-contact quadratic 给出的 `r_3` 至多两个固定有理根。原问题要求 `b_3` 正好等于该固定有理数的既约分母，而

\[
b_3=10^\ell\rho,
\]

故每个根至多对应一个 `\ell`。

因此：

\[
\boxed{
\text{A1 的两个 cross corridors 均为 fixed-prefix finite。}
}
\tag{16}
\]

---

### 6. A1 fixed-prefix finite theorem

此前已经证明：

- resonance sectors：fixed-prefix finite；
- double-nonresonant 的 `++`、`--` 象限：fixed-prefix finite；
- 本文：两个 cross corridors：fixed-prefix finite。

而 `h\mid Q^2G` 本身只有有限多个可能值，`g` 又满足

\[
0\le g\le\min(s_2-1,s_1+1)
\]

并受到 rational-contact prefix gap 的进一步限制。

所以得到完整结论：

\[
\boxed{
\text{对任意固定的前两块 }(a_1,b_1,a_2,b_2),
\text{ A1 第三块候选集合是有限的。}
}
\tag{17}
\]

而且这个有限性不是抽象存在：上述文件给出了 `g`、`h`、resonance 状态、cross-corridor offset 与每个 offset 的 `\ell` 恢复规则，可转化为显式有限证书。

必须保留证明边界：

\[
\boxed{
\text{(17) 仍不等于全局 A1 空性。}
}
\]

前两块本身尚未得到 prefix-uniform 的绝对高度上界，因此不能把所有 fixed-prefix finite 集合的并集称为有限。

下一阶段的唯一任务已经从“控制第三尾”转为：利用本框架对前缀对象 `C,D,G,N,K` 的必要条件，证明所有可能前缀本身为空，或把前缀压入一个全局有限盒。

---

## 6. A1 safe integer-gap recovery — 2026-08-16

> 整合来源：`a1-safe-integer-gap-recovery-2026-08-16.md`。以下正文保留该来源的原始证明状态和审计边界。

本文把 A1 rational-contact 框架重新接回整数球面，但完全避免使用有问题的 `a_3/\delta_3` 整数化。

核心结果是一个安全的 primitive gap recovery：

\[
\boxed{10^\ell E=b_3U}
\]

以及由此严格推出

\[
\boxed{U=LA,\qquad E=\tau A}
\]

其中 `A` 是新的正整数 gap 参数，与第三分子 `a_3` 无关。

本文结论均为 **已严格完成**。

---

### 1. 整数球面对象

令

\[
q=\operatorname{lcm}(b_1,b_2,b_3),
\]

并定义

\[
y_i=qr_i=\frac{qa_i}{b_i}.
\]

exact lift 强迫存在正整数 `H` 满足

\[
\boxed{H=qR}
\]

以及

\[
\boxed{H^2=y_1^2+y_2^2+y_3^2}.
\]

A1 rational-contact 框架中

\[
P=\frac CD,
\qquad
D=10^gQ,
\qquad
T=10^\ell,
\]

并有

\[
R=\frac{P+\theta r_3}{1+\theta},
\qquad
\theta=\frac{b_3}{TD}.
\]

等价地

\[
P-R=\theta(R-r_3).
\tag{1}
\]

---

### 2. contact gap 的整数化

定义两个正整数候选 gap：

\[
\boxed{E=Cq-DH}
\]

以及

\[
\boxed{U=H-y_3}.
\]

因为 A1 中

\[
P>R>r_3,
\]

故

\[
E>0,
\qquad U>0.
\]

把 (1) 写成

\[
\frac{Cq-DH}{Dq}
=
\frac{b_3}{TD}
\cdot
\frac{H-y_3}{q}.
\]

直接清分母得到

\[
\boxed{
T E=b_3 U.
}
\tag{2}
\]

这条等式完全由原始 exact lift 和整数球面推出，不需要 Gaussian integers，也没有对 `a_3` 做任何额外整除假设。

---

### 3. 安全的 `L,\tau` primitive recovery

定义

\[
\delta=\gcd(T,b_3),
\]

\[
\boxed{L=\frac T\delta},
\qquad
\boxed{\tau=\frac{b_3}{\delta}}.
\]

于是

\[
\gcd(L,\tau)=1.
\]

把 (2) 除以 `\delta`：

\[
L E=\tau U.
\]

由于 `L` 与 `\tau` 互素：

\[
L\mid U,
\qquad
\tau\mid E.
\]

因此存在唯一正整数 `A` 使

\[
\boxed{U=LA}
\]

以及

\[
\boxed{E=\tau A}.
\tag{3}
\]

这就是 A1 中合法的 primitive gap 参数。

需要特别强调：

\[
\boxed{A\text{ 与原第三分子 }a_3\text{ 没有被证明相等，也不应混同。}}
\]

旧公共框架中若某处把 `\delta\mid b_3` 进一步解释成 `\delta\mid a_3`，该步骤不能由 (2)–(3) 支持。

---

### 4. 球面因子分解恢复

由

\[
H^2-y_3^2=y_1^2+y_2^2
\]

有

\[
U(H+y_3)=y_1^2+y_2^2.
\]

代入 `U=LA`：

\[
\boxed{
LA(H+y_3)=y_1^2+y_2^2.
}
\tag{4}
\]

所以

\[
\boxed{LA\mid y_1^2+y_2^2.}
\tag{5}
\]

并且

\[
H+y_3
=
\frac{y_1^2+y_2^2}{LA}.
\]

与

\[
H-y_3=LA
\]

联立，严格恢复

\[
\boxed{
H
=\frac12\left(
LA+
rac{y_1^2+y_2^2}{LA}
\right),
}
\tag{6}
\]

\[
\boxed{
y_3
=\frac12\left(
\frac{y_1^2+y_2^2}{LA}-LA
\right).
}
\tag{7}
\]

因此旧 A1 基线中的球面 gap 分解可以保留，但其中的整数 `a` 应明确理解为本文的 gap 参数 `A`，不能理解成由 `a_3/\delta` 得到的第三分子正规化。

---

### 5. LCM 前缀化

令

\[
B=\operatorname{lcm}(b_1,b_2),
\qquad
d=\gcd(B,b_3).
\]

则

\[
q=\operatorname{lcm}(B,b_3)
=\frac{Bb_3}{d}.
\]

定义

\[
\boxed{c=\frac Bd},
\qquad
\boxed{t=\frac{b_3}{d}}.
\]

于是

\[
q=b_3c=Bt.
\]

第三坐标变成

\[
\boxed{y_3=ca_3,}
\]

前两坐标则为

\[
\boxed{
y_1=t\,a_1\frac{B}{b_1},
\qquad
y_2=t\,a_2\frac{B}{b_2}.}
\]

定义固定前两块平方和

\[
\boxed{
S_B=
\left(a_1\frac{B}{b_1}\right)^2
+
\left(a_2\frac{B}{b_2}\right)^2.
}
\]

则

\[
\boxed{y_1^2+y_2^2=t^2S_B.}
\tag{8}
\]

所以 (4) 进一步变成

\[
\boxed{
LA(H+ca_3)=t^2S_B.
}
\tag{9}
\]

这是一条安全的整数 divisibility 接口：所有第三块增长都集中在 `L,A,t,c` 中，而 `S_B` 由前两块固定。

---

### 6. contact determinant 的另一种表达

由 `E=\tau A` 与定义

\[
E=Cq-DH
\]

得到

\[
\boxed{Cq-DH=\tau A.}
\tag{10}
\]

另一方面从 `q=b_3c`、`y_3=ca_3` 和 `H=y_3+LA`：

\[
E
=C b_3c-D(ca_3+LA).
\]

又因

\[
b_3=\delta\tau,
\qquad T=\delta L,
\]

可写为

\[
\boxed{
 c(Cb_3-Da_3)
=A(\tau+DL).
}
\tag{11}
\]

也可直接由 (1) 清分母得到同一关系。

式 (11) 把正的 cross determinant

\[
Cb_3-Da_3>0
\]

与整数 gap `A`、尾 primitive pair `(L,\tau)` 精确联系起来。

---

### 7. 对旧 A1 基线的审计结论

现在可以严格区分两类陈述：

#### 可以安全保留

\[
U=LA,
\qquad
LA\mid y_1^2+y_2^2,
\]

以及由此得到的 `H,y_3` 两个半和/半差公式。

这些都由本文 (2)–(7) 独立重建。

#### 不能由本框架支持

若定义

\[
\delta=\gcd(T,b_3),
\]

则因为原问题有

\[
\gcd(a_3,b_3)=1,
\]

实际上

\[
\gcd(a_3,\delta)=1.
\]

所以除 `\delta=1` 外，不能把 `a_3/\delta` 当成整数 primitive numerator。

因此 A1 后续应使用本文的 gap integer `A` 作为球面 primitive recovery，而第三分子继续保持原始整数 `a_3`。

---

### 8. 与新 A1 主线的关系

目前 A1 有两套互补但兼容的安全坐标：

1. **rational-contact 坐标** `(\rho,V)`：适合控制第三分母 prime supply、2/5 resonance 与 fixed-prefix finite；
2. **integer-gap 坐标** `(L,\tau,A)`：适合连接整数球面、二平方因子分解与 Gaussian prime-flow，同时不触碰错误的 `a_3/\delta`。

下一步若要重新使用高斯整数，只应从

\[
LA(H+y_3)=y_1^2+y_2^2
\]

出发研究 `LA` 在二平方和中的因子分配，并额外验证变换是否保持 coefficient plane；不能再以 `a_3=\delta z_3` 为入口。

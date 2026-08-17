# A1 moving-prefix and top-layer endpoint kernels

> 本文件是按数学依赖整合的规范编辑入口。每个来源笔记只在本文件中保留一次；来源边界、原状态和公式正文均保留，避免日期文件之间形成平行副本。

## 整合顺序

`a1-prefix-contact-window-2026-08-16.md` → `a1-prefix-digit-collapse-2026-08-16.md` → `a1-global-four-layer-collapse-2026-08-17.md` → `a1-top-layer-endpoint-kernel-2026-08-17.md` → `a1-top-layer-residue-kernel-2026-08-17.md` → `a1-top-layer-half-gap-shell-2026-08-17.md` → `a1-top-layer-half-gap-sharpening-2026-08-17.md` → `a1-top-layer-excess-decomposition-2026-08-17.md` → `a1-top-layer-minimal-surplus-kernel-2026-08-17.md` → `a1-top-layer-minimal-offdiagonal-2026-08-17.md`

---

## 1. A1 moving-prefix contact window — 2026-08-16

> 整合来源：`a1-prefix-contact-window-2026-08-16.md`。以下正文保留该来源的原始证明状态和审计边界。

本文在完整 fixed-prefix finite theorem 之后，把 A1 的剩余问题改写成纯前缀对象 `(C,D,G,N,K)` 与一个紧致归一化第三块 `(\eta,\rho)` 的接触问题。

目标不是再次控制 `\ell`，而是精确描述移动前缀必须满足的必要条件。

本文结论均为 **已严格完成**；最后一节是当前剩余核心。

---

### 1. 完全消去尾长 `\ell`

记

\[
T=10^\ell,
\qquad
\eta=\frac{a_3}{T},
\qquad
\rho=\frac{b_3}{T}.
\]

因为 `a_3` 恰有 `\ell=n_3` 位，

\[
\boxed{\frac1{10}\le\eta<1.}
\tag{1}
\]

因为 `b_3` 恰有 `m_3=g+\ell` 位，

\[
\boxed{10^{g-1}\le\rho<10^g.}
\tag{2}
\]

并且

\[
\boxed{r_3=\frac\eta\rho.}
\tag{3}
\]

原始拼接为

\[
\alpha=T(C+\eta),
\qquad
\beta=T(D+\rho).
\]

所以 exact lift 等价于

\[
\boxed{
\frac{C+\eta}{D+\rho}
=
\sqrt{
\frac NG^2+\left(\frac\eta\rho\right)^2
}.
}
\tag{4}
\]

这里

\[
C=a_1 10^{n_2}+a_2,
\quad
D=10^gQ,
\quad
Q=b_1 10^{m_2}+b_2,
\]

\[
G=b_1b_2,
\qquad
N=(a_1b_2)^2+(a_2b_1)^2
\]

完全由前两块和 `g` 决定。

因此连续几何层面的 A1 剩余问题已经完全不含 `\ell`；尾长只负责把 `(\eta,\rho)` 实现成同一个十进制尺度上的既约整数对。

---

### 2. 归一化 cross determinant

定义

\[
\boxed{J=C\rho-D\eta.}
\]

由于 A1 contact 中

\[
P=\frac CD>R>r_3=\frac\eta\rho,
\]

有

\[
\boxed{J>0.}
\tag{5}
\]

而

\[
P-R
=
\frac{C\rho-D\eta}{D(D+\rho)}
=
\boxed{
\frac{J}{D(D+\rho)}
},
\tag{6}
\]

\[
R-r_3
=
\frac{C\rho-D\eta}{\rho(D+\rho)}
=
\boxed{
\frac{J}{\rho(D+\rho)}
}.
\tag{7}
\]

二者之比自动恢复

\[
\frac{P-R}{R-r_3}=\frac\rho D.
\]

球面差平方

\[
(R-r_3)(R+r_3)=\frac NG^2
\]

再与 (7) 联立，可得到完全归一化的 determinant identity：

\[
\boxed{
G^2(C\rho-D\eta)
(C\rho+D\eta+2\rho\eta)
=
N\rho^2(D+\rho)^2.
}
\tag{8}
\]

这是移动前缀与紧致尾矩形之间的一个纯有理代数曲面方程。

---

### 3. 前缀值 `P` 必须贴住球面

由

\[
P-R=\frac\rho D(R-r_3)
\]

和

\[
\frac\rho D<\frac1Q,
\]

有

\[
0<P-R<\frac{R-r_3}{Q}<\frac RQ.
\]

因此

\[
\boxed{
\frac{Q}{Q+1}P<R<P.
}
\tag{9}
\]

也就是说，前两块拼接值 `P` 与完整球面半径的相对误差严格小于 `1/Q`。

这是 A1 移动前缀最重要的实数接触条件之一。

---

### 4. `r_3` 的统一 digit window

由 (1)–(3)：

\[
\frac{1/10}{10^g}
<r_3<
\frac1{10^{g-1}},
\]

即

\[
\boxed{
10^{-g-1}<r_3<10^{1-g}.
}
\tag{10}
\]

因此

\[
\boxed{
\frac NG^2+10^{-2g-2}
<R^2
<
\frac NG^2+10^{2-2g}.
}
\tag{11}
\]

---

### 5. 前缀缺口 `K` 的第一个纯整数下界

定义

\[
\boxed{K=G^2C^2-D^2N.}
\]

由于

\[
P^2-
rac NG^2
=
\frac{K}{D^2G^2},
\]

而 `P>R`，由 (11) 的左侧得到

\[
P^2-
rac NG^2
>R^2-
rac NG^2
=r_3^2
>10^{-2g-2}.
\]

故

\[
K>D^2G^2\,10^{-2g-2}.
\]

利用

\[
D=10^gQ
\]

得到完全消去 `g` 的下界

\[
\boxed{
K>\frac{Q^2G^2}{100}.
}
\tag{12}
\]

因为 `K` 为整数，也可写成

\[
\boxed{
K\ge
\left\lfloor\frac{Q^2G^2}{100}\right\rfloor+1.
}
\]

---

### 6. 第二个纯前缀下界：切触判别

由 denominator-funnel 的 normalized square

\[
V^2=K-2\rho DN\ge0
\]

可得

\[
K\ge2\rho DN.
\]

而

\[
\rho\ge10^{g-1},
\qquad
D=10^gQ,
\]

所以

\[
\boxed{
K\ge
2\cdot10^{2g-1}QN
=
\frac{10^{2g}QN}{5}.
}
\tag{13}
\]

若考虑严格 `r_3>0` 对应的非退化接触，则实际候选还要满足相应根的正性；本文保留 (13) 作为无条件必要下界。

综合 (12)–(13)：

\[
\boxed{
K>
\max\left(
\frac{Q^2G^2}{100},
\frac{10^{2g}QN}{5}
\right)
}
\tag{14}
\]

（第二项若恰为整数边界，则按 (13) 使用非严格形式。）

---

### 7. 一个粗但纯前缀的上窗

由 (9)

\[
P<R\left(1+\frac1Q\right).
\]

于是

\[
P^2-
rac NG^2
<
\left(1+\frac1Q\right)^2
\left(
\frac NG^2+r_3^2
\right)
-
rac NG^2.
\]

利用

\[
r_3^2<10^{2-2g}
\]

得到

\[
P^2-
rac NG^2
<
\left(\frac2Q+\frac1{Q^2}\right)\frac NG^2
+
\left(1+\frac1Q\right)^2 10^{2-2g}.
\]

乘以 `D^2G^2=10^{2g}Q^2G^2`：

\[
\boxed{
K
<
10^{2g}(2Q+1)N
+100(Q+1)^2G^2.
}
\tag{15}
\]

因此 A1 moving prefix 必须把特殊整数二次型 `K` 放进明确的前缀窗

\[
\boxed{
\max\left(
\frac{Q^2G^2}{100},
\frac{10^{2g}QN}{5}
\right)
<K
<
10^{2g}(2Q+1)N+100(Q+1)^2G^2.
}
\tag{16}
\]

---

### 8. `K` 作为前两分子的显式不定二次型

记 `p=10^{n_2}`。则

\[
C=a_1p+a_2,
\]

所以

\[
K
=
\left(G^2p^2-D^2b_2^2\right)a_1^2
+2G^2p\,a_1a_2
+
\left(G^2-D^2b_1^2\right)a_2^2.
\tag{17}
\]

其中

\[
G^2-D^2b_1^2<0,
\]

而在 A1 carrier 可行区第一系数处于正侧。因此 `K` 是一个由 decimal-shift 参数固定的显式不定二元二次型。

A1 的剩余 prefix problem 可以表述为：

> 在 `a_i,b_i` 的位数、互素性和 carrier 约束下，证明这个特殊不定二次型无法同时落入 (16) 的接触窗，并支持 normalized square / primitive-gap 条件。

---

### 9. 当前移动前缀核心

第三尾的所有无界机制已被前序文件封锁后，A1 现在只剩以下移动前缀系统：

\[
\boxed{
0\le g\le\min(s_2-1,s_1+1),
}
\]

\[
\boxed{
K=G^2C^2-D^2N
}
\]

满足接触窗 (16)，并且存在

\[
\eta\in[1/10,1),
\qquad
\rho\in[10^{g-1},10^g)
\]

满足代数曲面 (8)，同时 `(\eta,\rho)` 必须来自同一十进制尺度 `T=10^\ell` 的既约整数对。

这就是当前 A1 的真正 moving-prefix core；后续任何“全局关闭”都应直接攻击这一系统，而无需再次分析第三尾的无界分类。

---

## 2. A1 generic prefix digit collapse — 2026-08-16

> 整合来源：`a1-prefix-digit-collapse-2026-08-16.md`。以下正文保留该来源的原始证明状态和审计边界。

本文继续 `top-layer.md`，把 moving-prefix core 的位数自由度进一步压缩。

核心结论：除两个低尺度角落 `(g,k)=(0,1),(0,2)` 外，A1 必须满足

\[
\boxed{g-1\le s_1\le g+2.}
\]

所以泛型 A1 的第一分数位数差只剩四条相邻层。

本文结论均为 **已严格完成**。

---

### 1. 无量纲前缀参数

A1 中

\[
k=s_2+s_3=s_2-g\ge1,
\]

所以

\[
s_2=k+g.
\]

定义

\[
\boxed{A_0=10^k r_1}
\]

以及 carrier ratio

\[
\boxed{
t=\frac{r_2}{A_0}
=
\frac{r_2}{10^k r_1}.}
\]

第一坐标严格承担 carrier，故

\[
\boxed{0<t<1.}
\tag{1}
\]

再定义前两分母拼接权

\[
\boxed{
\lambda=\frac{b_2}{Q},
\qquad
Q=b_1 10^{m_2}+b_2.
}
\]

因为 `b_2` 是 `m_2` 位数，

\[
b_2<10^{m_2}\le b_1 10^{m_2},
\]

故

\[
\boxed{0<\lambda<\frac12.}
\tag{2}
\]

同时

\[
Q\ge11.
\tag{3}
\]

---

### 2. 前缀拼接值的无量纲形式

A1 中

\[
P=\frac CD.
\]

把前两块解释成带权平均：

\[
P
=
(1-\lambda)10^kr_1
+
\lambda10^{-g}r_2.
\]

因此

\[
\boxed{
\frac P{A_0}
=(1-\lambda)+\lambda10^{-g}t.
}
\tag{4}
\]

另一方面

\[
S=r_1^2+r_2^2
=A_0^2\left(10^{-2k}+t^2\right).
\]

所以定义无量纲 prefix defect

\[
\boxed{
F:=\frac{P^2-S}{A_0^2},
}
\]

可精确写成

\[
\boxed{
F
=
\left((1-\lambda)+\lambda10^{-g}t\right)^2
-t^2-10^{-2k}.
}
\tag{5}
\]

---

### 3. contact 给出的 `F` 上界

由 rational contact

\[
P-R=\theta(R-r_3),
\qquad
0<\theta<\frac1Q,
\]

故

\[
P<R\left(1+\frac1Q\right).
\]

更直接地，

\[
P^2-S
=r_3^2+(P-R)(P+R).
\]

又

\[
P-R<\frac RQ,
\]

以及

\[
P+R<\left(2+\frac1Q\right)R.
\]

因此

\[
P^2-S
<
r_3^2
+
\frac{2+1/Q}{Q}R^2.
\tag{6}
\]

---

### 4. 泛型尺度 `k+2g\ge3`

第三、第二分数的位数窗给出

\[
r_3<10^{1-g},
\]

\[
r_2>10^{k+g-1}.
\]

所以

\[
\frac{r_3}{r_2}
<10^{2-k-2g}.
\]

若

\[
\boxed{k+2g\ge3,}
\tag{7}
\]

则

\[
\boxed{
\frac{r_3}{r_2}<\frac1{10}.
}
\tag{8}
\]

因为 `r_2=tA_0`，有

\[
\boxed{
\frac{r_3^2}{A_0^2}<\frac{t^2}{100}.
}
\tag{9}
\]

同时

\[
\frac{S}{A_0^2}=t^2+10^{-2k}\le t^2+\frac1{100},
\]

故

\[
\frac{R^2}{A_0^2}
=
\frac{S+r_3^2}{A_0^2}
<
\frac{101}{100}t^2+
rac1{100}.
\tag{10}
\]

由 `Q\ge11`：

\[
\frac{2+1/Q}{Q}
\le
\frac{23}{121}.
\]

把 (9)–(10) 代入 (6)，得到

\[
\boxed{
F
<
\frac{611}{3025}t^2
+
\frac{23}{12100}.
}
\tag{11}
\]

---

### 5. `t\le2/5` 与下界矛盾

由 (2) 与 `\lambda10^{-g}t>0`：

\[
(1-\lambda)+\lambda10^{-g}t>\frac12.
\]

而 `k\ge1`，故由 (5)

\[
\boxed{
F>
\frac14-t^2-\frac1{100}.
}
\tag{12}
\]

假设

\[
t\le\frac25.
\]

则 (12) 给出

\[
F>
\frac14-
rac4{25}-\frac1{100}
=
\frac2{25}.
\tag{13}
\]

另一方面 (11) 给出

\[
F
<
\frac{611}{3025}\frac4{25}
+
\frac{23}{12100}
<
\frac2{25}.
\tag{14}
\]

矛盾。

因此在所有满足 (7) 的 A1 候选中：

\[
\boxed{
 t=\frac{r_2}{10^kr_1}>\frac25.
}
\tag{15}
\]

---

### 6. 第一分数位数差被压成四层

由 (15)

\[
r_1
<
\frac52\,10^{-k}r_2.
\]

而

\[
r_2<10^{s_2+1}=10^{k+g+1},
\]

故

\[
r_1<\frac52\,10^{g+1}<10^{g+2}.
\]

另一方面若 `r_1` 的位数差为 `s_1`，则

\[
r_1>10^{s_1-1}.
\]

所以不可能有

\[
s_1\ge g+3.
\]

即

\[
\boxed{s_1\le g+2.}
\tag{16}
\]

此前 carrier 已严格给出

\[
\boxed{s_1\ge g-1.}
\tag{17}
\]

综合：

\[
\boxed{
 s_1\in\{g-1,g,g+1,g+2\}
}
\tag{18}
\]

对所有 `k+2g\ge3` 的 A1 候选成立。

---

### 7. 唯一两个低尺度例外

A1 中

\[
k\ge1,
\qquad g\ge0.
\]

不满足

\[
k+2g\ge3
\]

的整数对只有

\[
\boxed{(g,k)=(0,1)}
\]

和

\[
\boxed{(g,k)=(0,2).}
\]

因此 A1 moving-prefix problem 已严格分成：

#### 泛型 chamber

\[
\boxed{k+2g\ge3}
\]

且只剩四个位数层

\[
\boxed{s_1=g-1,g,g+1,g+2.}
\]

#### 低尺度 chamber

仅

\[
\boxed{(g,k)=(0,1),(0,2)}.
\]

这两个角落需要单独做更精确的实数矩形/局部算术分析。

---

### 8. 当前意义

这一步首次把 A1 的**移动前缀位数自由度**从无界二维区域压成：

- 一个泛型的四层带；
- 两个明确的低尺度角落。

因此后续无需再允许 `s_1-g\to+\infty`。任何全局 A1 候选都必须落在上述有限位数形状之一。

---

## 3. A1 global four-layer collapse — 2026-08-17

> 整合来源：`a1-global-four-layer-collapse-2026-08-17.md`。以下正文保留该来源的原始证明状态和审计边界。

本文继续 `top-layer.md`，把其中留下的两个低尺度角落

\[
(g,k)=(0,1),(0,2)
\]

也压回同一个四层位数带。

最终得到一个对整个 A1 无例外成立的结论：

\[
\boxed{s_1-g\in\{-1,0,1,2\}.}
\]

本文结论均为 **已严格完成**。

---

### 1. 统一无量纲变量

沿用前文记号

\[
A_0=10^k r_1,
\qquad
t=\frac{r_2}{A_0},
\qquad
q_0=\frac{r_3}{A_0}.
\]

A1 的第一坐标严格承担 carrier，因此

\[
0<t<1.
\]

再记

\[
R_0=\frac{\mathcal R}{A_0}.
\]

球面方程给出

\[
\boxed{R_0^2=t^2+10^{-2k}+q_0^2.}
\tag{1}
\]

令

\[
Q=b_1 10^{m_2}+b_2,
\qquad
\lambda=\frac{b_2}{Q}.
\]

A1 前两块拼接值满足

\[
\frac P{A_0}
=(1-\lambda)+\lambda10^{-g}t.
\tag{2}
\]

而 rational-contact 条件给出

\[
\frac{Q}{Q+1}P<\mathcal R<P.
\tag{3}
\]

---

### 2. 一个此前未单独提取的统一事实：`R_0>1/2`

设

\[
B=b_1 10^{m_2}.
\]

则

\[
Q=B+b_2.
\]

由 (2)，第二项严格为正，所以

\[
\frac P{A_0}
>
1-\lambda
=
\frac BQ.
\]

由 (3)：

\[
R_0
>
\frac{Q}{Q+1}\frac BQ
=
\frac{B}{Q+1}
=
\frac{B}{B+b_2+1}.
\]

因为 `b_2` 恰有 `m_2` 位，

\[
b_2+1\le10^{m_2}\le B,
\]

所以

\[
\frac{B}{B+b_2+1}\ge\frac12.
\]

前面的第一步是严格不等式，因此最终得到

\[
\boxed{R_0>\frac12.}
\tag{4}
\]

这个结论不依赖 `g,k` 的大小，也不依赖第三尾正规化。

---

### 3. 对任意 A1 的统一 `t` 下界公式

A1 位数给出

\[
s_2=k+g,
\qquad
s_3=-g.
\]

由十进制位数窗

\[
r_2>10^{k+g-1},
\qquad
r_3<10^{1-g},
\]

故

\[
\boxed{
\frac{r_3}{r_2}<10^{2-k-2g}.
}
\tag{5}
\]

因为

\[
q_0=\frac{r_3}{r_2}t,
\]

有

\[
q_0^2
<
10^{4-2k-4g}t^2.
\]

代入 (1)，再用 (4)：

\[
\frac14
<R_0^2
<
\left(1+10^{4-2k-4g}\right)t^2+10^{-2k}.
\]

因此

\[
\boxed{
 t^2>
\frac{
\frac14-10^{-2k}
}{
1+10^{4-2k-4g}
}.
}
\tag{6}
\]

这是覆盖整个 A1 的统一 carrier-ratio 下界。

---

### 4. 泛型区域的旧四层结论得到更干净的证明

若

\[
k+2g\ge3,
\]

则

\[
10^{4-2k-4g}\le\frac1{100}.
\]

又 `k\ge1`，所以

\[
10^{-2k}\le\frac1{100}.
\]

由 (6)：

\[
t^2>
\frac{
1/4-1/100
}{1+1/100}
=
\frac{24}{101}.
\]

于是

\[
\boxed{t>\sqrt{\frac{24}{101}}>\frac25.}
\tag{7}
\]

这重新得到前文用于四层压缩的下界，而且常数更强。

由

\[
r_1=\frac{r_2}{10^k t}
\]

和

\[
r_2<10^{k+g+1}
\]

可得

\[
r_1<\sqrt{\frac{101}{24}}\,10^{g+1}<10^{g+2}.
\]

因此

\[
s_1\le g+2.
\]

另一方面旧 carrier cap 已严格给出

\[
s_1\ge g-1.
\]

所以泛型区域仍为

\[
\boxed{s_1-g\in\{-1,0,1,2\}.}
\tag{8}
\]

---

### 5. 低尺度角落 `(g,k)=(0,2)` 也只有四层

此时 (6) 变成

\[
t^2>
\frac{
1/4-10^{-4}
}{2}
=
\frac{2499}{20000}.
\]

故

\[
t>\sqrt{\frac{2499}{20000}}>\frac13.
\]

于是

\[
r_1
=
\frac{r_2}{100t}
<
\frac{10^3}{100t}
=
\frac{10}{t}
<30.
\]

若 `s_1\ge3`，则位数窗强迫

\[
r_1>10^{s_1-1}\ge100,
\]

矛盾。

所以

\[
\boxed{s_1\le2.}
\]

而 `g=0` 时 carrier 下界为

\[
s_1\ge-1.
\]

故

\[
\boxed{(g,k)=(0,2)\Longrightarrow s_1\in\{-1,0,1,2\}.}
\tag{9}
\]

---

### 6. 低尺度角落 `(g,k)=(0,1)` 先压到五层

现在 (6) 给出

\[
t^2>
\frac{
1/4-1/100
}{101}
=
\frac{24}{10100}.
\]

因此

\[
t>\sqrt{\frac{24}{10100}}.
\]

从而

\[
r_1
=
\frac{r_2}{10t}
<
\frac{10^2}{10t}
=
\frac{10}{t}
<206.
\]

所以不可能有 `s_1\ge4`，即

\[
s_1\le3.
\]

结合 `s_1\ge-1`，暂时只剩

\[
s_1\in\{-1,0,1,2,3\}.
\]

---

### 7. `(g,k)=(0,1)` 的最高层 `s_1=3` 直接为空

假设

\[
g=0,
\qquad k=1,
\qquad s_1=3.
\]

则

\[
r_1>10^{s_1-1}=100,
\]

故

\[
A_0=10r_1>1000.
\]

又 `s_2=1`、`s_3=0`，因此

\[
r_2<100,
\qquad
r_3<10.
\]

于是

\[
t=\frac{r_2}{A_0}<\frac1{10},
\qquad
q_0=\frac{r_3}{A_0}<\frac1{100}.
\]

由球面式 (1)：

\[
R_0^2
<
\frac1{100}
+
\frac1{100}
+
\frac1{10000}
=
\frac{201}{10000}
<\frac14.
\]

这与统一结论 (4)

\[
R_0>\frac12
\]

矛盾。

所以

\[
\boxed{(g,k)=(0,1),\ s_1=3\text{ 为空}.}
\tag{10}
\]

因此该低尺度角落最终也只剩

\[
\boxed{s_1\in\{-1,0,1,2\}.}
\tag{11}
\]

---

### 8. 全局四层定理

综合泛型区域 (8)、低尺度 `(0,2)` 的 (9) 与 `(0,1)` 的 (11)，A1 的两个旧例外已经全部消失。

最终对每一个 A1 exact-lift 候选均有

\[
\boxed{
 g-1\le s_1\le g+2.
}
\]

等价地

\[
\boxed{
 s_1-g\in\{-1,0,1,2\}.
}
\tag{12}
\]

因此 A1 moving-prefix problem 不再需要分“泛型 + 两个低尺度角落”；从现在开始可以全局只研究四个位数层

\[
\boxed{d:=s_1-g=-1,0,1,2.}
\]

其中最高层 `d=2` 是十进制边界接触最强的一层，后续应优先处理。

---

## 4. A1 top layer endpoint kernel — 2026-08-17

> 整合来源：`a1-top-layer-endpoint-kernel-2026-08-17.md`。以下正文保留该来源的原始证明状态和审计边界。

本文研究全局四层定理中的最高层

\[
\boxed{d:=s_1-g=2.}
\]

这一层的十进制尺度恰好位于一个边界接触状态：`10^k r_1` 从上侧逼近同一十进制边界，而 `r_2` 从下侧逼近它。利用 rational contact 可以把这种直觉严格化为一个 endpoint-offset normal form。

核心结论：

1. 最高层全局满足
   \[
   \boxed{m_1\ge2k};
   \]
2. 令
   \[
   r=m_1-2k,
   \qquad
   s=m_2+g-k,
   \]
   则必有 `r,s\ge0`，并且四个前缀整数都被压在各自十进制端点附近；
3. 整个最高层可以写成一个紧致的四-offset kernel；
4. 若 `g\ge1`，进一步严格有
   \[
   \boxed{r\ge1,\qquad s\ge1};
   \]
5. 若 `g=0`，至少不能同时 `r=s=0`。

本文结论均为 **已严格完成**。

---

### 1. 最高层中的第三坐标极小

沿用

\[
A_0=10^k r_1,
\qquad
t=\frac{r_2}{A_0},
\qquad
q_0=\frac{r_3}{A_0},
\qquad
R_0=\frac{\mathcal R}{A_0}.
\]

由 `top-layer.md`：

\[
\boxed{R_0>\frac12.}
\tag{1}
\]

现在假设

\[
s_1=g+2.
\]

位数窗给出

\[
r_1>10^{g+1},
\qquad
r_3<10^{1-g}.
\]

于是

\[
A_0>10^{k+g+1},
\]

从而

\[
\boxed{q_0<10^{-k-2g}.}
\tag{2}
\]

球面式

\[
R_0^2=t^2+10^{-2k}+q_0^2
\]

与 (1)–(2) 联立得到

\[
t^2>
\frac14-10^{-2k}-10^{-2k-4g}.
\]

右侧在 `k\ge1,g\ge0` 时最小为

\[
\frac14-
rac1{100}-\frac1{100}=
rac{23}{100}.
\]

故

\[
\boxed{t>\frac{\sqrt{23}}{10}>\frac{47}{100}.}
\tag{3}
\]

---

### 2. 最高层的精确四因子分解

因为

\[
s_1=g+2,
\qquad
s_2=k+g,
\]

有

\[
n_1=m_1+g+2,
\qquad
n_2=m_2+k+g.
\]

直接检查十进制指数可得

\[
\boxed{
 t
=
\left(\frac{a_2}{10^{n_2}}\right)
\left(\frac{b_1}{10^{m_1}}\right)
\left(\frac{10^{n_1-1}}{a_1}\right)
\left(\frac{10^{m_2-1}}{b_2}\right).
}
\tag{4}
\]

四个因子都属于 `(0,1]`，而它们的乘积由 (3) 大于 `47/100`。因此每一个因子都严格大于 `47/100`：

\[
\boxed{a_2>\frac{47}{100}10^{n_2},}
\tag{5}
\]

\[
\boxed{b_1>\frac{47}{100}10^{m_1},}
\tag{6}
\]

\[
\boxed{a_1<\frac{100}{47}10^{n_1-1},}
\tag{7}
\]

\[
\boxed{b_2<\frac{100}{47}10^{m_2-1}.}
\tag{8}
\]

所以最高层从一开始就位于四个十进制端点组成的角落，而不是一个普通内部矩形。

---

### 3. contact 把 `1-t` 锁到 `10^{-2k}` 尺度

记

\[
Q=b_1 10^{m_2}+b_2,
\qquad
\lambda=\frac{b_2}{Q}.
\]

由 (6)、(8)：

\[
\lambda
<
\frac{b_2}{b_1 10^{m_2}}
<
\frac{1000}{2209}10^{-m_1}.
\tag{9}
\]

同样

\[
\frac1Q
<
\frac1{b_1 10^{m_2}}
<
\frac{100}{47}10^{-m_1-m_2}
\le
\frac{10}{47}10^{-m_1}.
\tag{10}
\]

rational contact 在无量纲坐标中为

\[
1-R_0
=
\lambda(1-10^{-g}t)
+
\theta(R_0-q_0),
\qquad
0<\theta<\frac1Q.
\]

因为 `R_0<1`，所以由 (9)–(10)

\[
\boxed{
1-R_0
<
\frac{1470}{2209}10^{-m_1}.
}
\tag{11}
\]

另一方面，(4) 中第二因子给出

\[
t<\frac{b_1}{10^{m_1}},
\]

所以

\[
1-t
>
1-\frac{b_1}{10^{m_1}}
\ge10^{-m_1}.
\tag{12}
\]

因此

\[
R_0-t
=(1-t)-(1-R_0)
>
\boxed{
\frac{739}{2209}10^{-m_1}.
}
\tag{13}
\]

另一方面由球面式

\[
R_0-t
=
\frac{10^{-2k}+q_0^2}{R_0+t}.
\]

由 (2)、(3)，

\[
R_0+t>2t>\frac{94}{100},
\]

故

\[
R_0-t
<
\frac{100}{94}
10^{-2k}(1+10^{-4g})
\le
\boxed{\frac{100}{47}10^{-2k}.}
\tag{14}
\]

若 `m_1\le2k-1`，则 (13) 给出

\[
R_0-t
>
\frac{7390}{2209}10^{-2k},
\]

但

\[
\frac{7390}{2209}>
rac{4700}{2209}=
rac{100}{47},
\]

与 (14) 矛盾。

所以最高层全局满足

\[
\boxed{m_1\ge2k.}
\tag{15}
\]

这已经把 `k` 压入第一分母位数的一半尺度：

\[
k\le\frac{m_1}{2}.
\]

---

### 4. 更强的贴边：`1-t<3\cdot10^{-2k}`

由 (15)：

\[
10^{-m_1}\le10^{-2k}.
\]

把它代入 (11)：

\[
1-R_0
<
\frac{1470}{2209}10^{-2k}.
\]

再与 (14) 相加：

\[
1-t
=(1-R_0)+(R_0-t)
<
\left(
\frac{1470}{2209}
+
\frac{4700}{2209}
\right)10^{-2k}.
\]

因此

\[
\boxed{
1-t
<
\frac{6170}{2209}10^{-2k}
<3\cdot10^{-2k}.
}
\tag{16}
\]

所以最高层的四因子乘积并非仅仅大于一个固定常数；它实际上以 `10^{-2k}` 的速度逼近 1。

---

### 5. 两个 surplus 与四个端点偏移

定义

\[
\boxed{r=m_1-2k\ge0.}
\tag{17}
\]

再定义

\[
\boxed{s=m_2+g-k.}
\tag{18}
\]

从 (4)、(16)，每个因子都大于

\[
1-3\cdot10^{-2k}.
\]

令端点偏移

\[
\boxed{w=10^{m_1}-b_1\ge1,}
\]

\[
\boxed{x=a_1-10^{n_1-1}\ge0,}
\]

\[
\boxed{z=10^{n_2}-a_2\ge1,}
\]

\[
\boxed{y=b_2-10^{m_2-1}\ge0.}
\]

则由四因子逐项得到

\[
\boxed{1\le w<3\cdot10^r,}
\tag{19}
\]

\[
\boxed{0\le x<4\cdot10^{r+g+1},}
\tag{20}
\]

\[
\boxed{1\le z<3\cdot10^s,}
\tag{21}
\]

\[
\boxed{0\le y<4\cdot10^{s-k-g-1}.}
\tag{22}
\]

其中 (20)、(22) 使用了

\[
\frac{3\cdot10^{-2k}}{1-3\cdot10^{-2k}}
<4\cdot10^{-2k}.
\]

由于 `z\ge1`，(21) 立即强迫

\[
\boxed{s\ge0,}
\tag{23}
\]

即

\[
\boxed{m_2+g\ge k.}
\]

特别地，若

\[
s=0,
\]

则

\[
\boxed{z\in\{1,2\}.}
\tag{24}
\]

若

\[
r=0,
\]

则同理

\[
\boxed{w\in\{1,2\}.}
\tag{25}
\]

此外若

\[
s\le k+g,
\]

则 (22) 的右侧小于 1，故整数 `y` 必须为零：

\[
\boxed{s\le k+g\Longrightarrow b_2=10^{m_2-1}.}
\tag{26}
\]

这时 `gcd(a_2,b_2)=1` 还等价强迫

\[
\boxed{\gcd(z,10)=1.}
\tag{27}
\]

因为

\[
a_2=10^{n_2}-z.
\]

---

### 6. endpoint normal form

利用

\[
m_1=2k+r,
\qquad
m_2=k-g+s,
\]

最高层的四个前缀整数可以统一写成

\[
\boxed{
b_1=10^{2k+r}-w,}
\tag{28}
\]

\[
\boxed{
a_1=10^{2k+r+g+1}+x,}
\tag{29}
\]

\[
\boxed{
b_2=10^{k-g+s-1}+y,}
\tag{30}
\]

\[
\boxed{
a_2=10^{2k+s}-z.}
\tag{31}
\]

所有增长已经从原来的四个大整数转移到 `k,g,r,s`，而 `w,x,y,z` 只允许在 (19)–(22) 的端点薄层中移动。

---

### 7. 精确 determinant 展开

定义第一、第二坐标十进制移位差

\[
\boxed{
\Delta
=10^k a_1b_2-a_2b_1
>0.
}
\tag{32}
\]

这里正性等价于 `t<1`。

把 (28)–(31) 代入并消去主导的相同十进制幂，可以得到完全正的展开：

\[
\boxed{
\begin{aligned}
\Delta={}&
10^{m_1+k+g+1}y
+10^{k+m_2-1}x
+10^kxy\\
&+10^{k+g+m_2}w
+b_1z.
\end{aligned}
}
\tag{33}
\]

右端五项全部非负，且最后两项严格为正。

定义统一尺度

\[
\boxed{
L_0=10^{m_1+m_2+g-k}=10^{2k+r+s}.
}
\tag{34}
\]

再定义紧致 offset 坐标

\[
\boxed{X=\frac{x}{10^{r+g+1}},}
\qquad
\boxed{W=\frac{w}{10^r},}
\]

\[
\boxed{Z=\frac{z}{10^s},}
\qquad
\boxed{Y=10^{k+g+1-s}y.}
\tag{35}
\]

并记

\[
\varepsilon=10^{-2k}.
\]

则 (33) 精确化成

\[
\boxed{
\frac{\Delta}{L_0}
=
X+W+Y+Z
+
\varepsilon(XY-WZ).
}
\tag{36}
\]

这就是最高层的紧致四-offset kernel。

还可以从

\[
1-t=\frac{\Delta}{10^k a_1b_2}
\]

得到另一条精确表达：

\[
\boxed{
\frac{\Delta}{L_0}
=
\frac{1-t}{\varepsilon}
(1+\varepsilon X)(1+\varepsilon Y).
}
\tag{37}
\]

由球面式

\[
R_0-t
>
\frac{\varepsilon}{2}
\]

可得

\[
1-t>\frac\varepsilon2,
\]

再结合 (16)、(37)：

\[
\boxed{
\frac12
<
\frac{\Delta}{L_0}
<
\frac72.
}
\tag{38}
\]

因此原本无界的最高层已经被压成一个固定宽度的 compact determinant window。

---

### 8. `g\ge1` 时两个 surplus 都必须严格为正

现在额外假设

\[
g\ge1.
\]

由 (16) 与四因子贴边：

\[
b_1>(1-3\varepsilon)10^{m_1},
\qquad
b_2<\frac{10^{m_2-1}}{1-3\varepsilon}.
\]

因为 `m_1\ge2k`、`m_2\ge1`、`\varepsilon\le1/100`，有

\[
\lambda<\frac\varepsilon9,
\qquad
\frac1Q<\frac\varepsilon9.
\]

所以

\[
\boxed{1-R_0<\frac{2}{9}\varepsilon.}
\tag{39}
\]

又由 `g\ge1` 和 (2)：

\[
q_0^2<\frac{\varepsilon}{10000}.
\]

设

\[
\delta=1-t.
\]

由

\[
1-R_0^2
=2\delta-\delta^2-\varepsilon-q_0^2
\]

以及

\[
1-R_0^2<2(1-R_0)<\frac49\varepsilon,
\]

再用 `\delta<3\varepsilon`，得到

\[
2\delta
<
\left(
\frac9{100}+1+\frac1{10000}+\frac49
\right)\varepsilon
<
\frac85\varepsilon.
\]

因此

\[
\boxed{\delta<\frac45\varepsilon.}
\tag{40}
\]

代回 (37)。由于

\[
\delta<\frac45\varepsilon\le\frac1{125},
\]

且

\[
1+\varepsilon X<\frac1{1-\delta},
\qquad
1+\varepsilon Y<\frac1{1-\delta},
\]

有

\[
\boxed{
\frac{\Delta}{L_0}<\frac56.
}
\tag{41}
\]

若 `r=0`，则 `W=w\ge1`，而 (33) 的归一化各项全为非负，故

\[
\frac{\Delta}{L_0}\ge W\ge1,
\]

与 (41) 矛盾。因此

\[
\boxed{g\ge1\Longrightarrow r\ge1.}
\tag{42}
\]

若 `s=0`，则 `Z=z\ge1`。在 (36) 中真正对应最后一项的是

\[
\frac{b_1}{10^{m_1}}Z.
\]

而

\[
\frac{b_1}{10^{m_1}}>t=1-\delta>\frac{124}{125}>\frac56.
\]

故单独这一项已经大于 `5/6`，再次与 (41) 矛盾。所以

\[
\boxed{g\ge1\Longrightarrow s\ge1.}
\tag{43}
\]

综合：

\[
\boxed{
 d=2,\ g\ge1
\Longrightarrow
m_1\ge2k+1,
\qquad
m_2+g\ge k+1.
}
\tag{44}
\]

---

### 9. `g=0` 时两个 equality surplus 不能同时出现

若 `g=0`，仍有 (39)。此时由 (2)

\[
q_0^2<\varepsilon.
\]

同样计算得到

\[
\delta<\frac{13}{10}\varepsilon.
\]

因此由 (37) 可取安全粗界

\[
\boxed{
\frac{\Delta}{L_0}<\frac75.
}
\tag{45}
\]

若同时

\[
r=s=0,
\]

则 `W=w\ge1`、`Z=z\ge1`，并且

\[
\frac{b_1}{10^{m_1}}>1-\delta>0.98.
\]

所以 (33) 归一化后的 `w` 项与 `z` 项之和已经严格大于

\[
1+0.98>\frac75,
\]

与 (45) 矛盾。

故

\[
\boxed{
 d=2,\ g=0
\Longrightarrow
(r,s)\ne(0,0).
}
\tag{46}
\]

---

### 10. 当前最高层剩余核心

最高层已经从原来的任意四整数前缀压缩成：

\[
\boxed{
 r=m_1-2k\ge0,
\qquad
s=m_2+g-k\ge0,
}
\]

加上紧致 offset

\[
(X,W,Y,Z)
\]

满足精确 determinant 核

\[
\boxed{
\frac{\Delta}{10^{2k+r+s}}
=X+W+Y+Z+10^{-2k}(XY-WZ),
}
\]

以及固定窗口

\[
\boxed{
\frac12<\frac{\Delta}{10^{2k+r+s}}<\frac72.
}
\]

在 `g\ge1` 时窗口进一步缩到

\[
\boxed{
\frac12<\frac{\Delta}{10^{2k+r+s}}<\frac56,
\qquad r,s\ge1.
}
\]

并且当 `s\le k+g` 时还有

\[
\boxed{b_2=10^{m_2-1},\qquad\gcd(z,10)=1.}
\]

因此 `d=2` 后续不应再以原始 `(a_1,b_1,a_2,b_2)` 为变量，而应直接攻击上述 `(k,g,r,s;X,W,Y,Z)` compact endpoint kernel，并把 normalized-square / 2,5-adic 条件转写到该坐标中。

---

## 5. A1 top layer coprime-residue kernel — 2026-08-17

> 整合来源：`a1-top-layer-residue-kernel-2026-08-17.md`。以下正文保留该来源的原始证明状态和审计边界。

本文继续 `top-layer.md`。最高层

\[
d=s_1-g=2
\]

已经被压入端点变量 `(w,x,y,z)`；本文进一步把四个端点变量合并成两个与既约性直接兼容的正整数余量。

核心结果为

\[
\boxed{a_1=10^{g+1}b_1+U_1,}
\qquad
\boxed{a_2=10^{k+g+1}b_2-U_2,}
\]

\[
\boxed{\gcd(U_1,b_1)=\gcd(U_2,b_2)=1,}
\]

以及 determinant 的二项正分解

\[
\boxed{
\Delta=10^k b_2U_1+b_1U_2.
}
\]

这把最高层改写成“同一十进制中心两侧的两个既约 rational defects”。本文结论均为 **已严格完成**。

---

### 1. 端点基线

沿用前文

\[
m_1=2k+r,
\qquad
m_2=k-g+s,
\]

以及

\[
b_1=10^{2k+r}-w,
\qquad
 a_1=10^{2k+r+g+1}+x,
\]

\[
b_2=10^{k-g+s-1}+y,
\qquad
 a_2=10^{2k+s}-z.
\]

其中

\[
w,z\ge1,
\qquad x,y\ge0.
\]

定义

\[
\boxed{
U_1=x+10^{g+1}w,
}
\tag{1}
\]

\[
\boxed{
U_2=z+10^{k+g+1}y.
}
\tag{2}
\]

二者均为正整数。

---

### 2. 两个原分数变成十进制中心加减既约余量

由

\[
10^{g+1}b_1
=10^{2k+r+g+1}-10^{g+1}w,
\]

结合 (1)：

\[
\boxed{
 a_1=10^{g+1}b_1+U_1.
}
\tag{3}
\]

同理

\[
10^{k+g+1}b_2
=10^{2k+s}+10^{k+g+1}y,
\]

结合 (2)：

\[
\boxed{
 a_2=10^{k+g+1}b_2-U_2.
}
\tag{4}
\]

因此

\[
\boxed{
 r_1=10^{g+1}+\frac{U_1}{b_1},
}
\tag{5}
\]

\[
\boxed{
 r_2=10^{k+g+1}-\frac{U_2}{b_2}.
}
\tag{6}
\]

令共同十进制中心

\[
\boxed{M=10^{k+g+1}.}
\]

则

\[
10^k r_1
=M+10^k\frac{U_1}{b_1},
\qquad
r_2
=M-\frac{U_2}{b_2}.
\]

所以最高层精确描述成第一 carrier 坐标从 `M` 的上侧逼近、第二坐标从 `M` 的下侧逼近。

---

### 3. 原始既约性直接传给两个余量

由 (3)：

\[
\gcd(a_1,b_1)
=
\gcd(U_1,b_1).
\]

原问题要求 `gcd(a_1,b_1)=1`，故

\[
\boxed{
\gcd(U_1,b_1)=1.
}
\tag{7}
\]

同理由 (4)：

\[
\boxed{
\gcd(U_2,b_2)=1.
}
\tag{8}
\]

因此两个 rational defects

\[
\frac{U_1}{b_1},
\qquad
\frac{U_2}{b_2}
\]

本身已经是既约分数。

---

### 4. carrier gap 的二项分解

定义

\[
\Delta=10^k a_1b_2-a_2b_1>0.
\]

把 (3)–(4) 代入：

\[
\begin{aligned}
\Delta
&=10^k(10^{g+1}b_1+U_1)b_2
 -(10^{k+g+1}b_2-U_2)b_1\\
&=10^k b_2U_1+b_1U_2.
\end{aligned}
\]

所以

\[
\boxed{
\Delta=10^k b_2U_1+b_1U_2.
}
\tag{9}
\]

除以 `G=b_1b_2`：

\[
\boxed{
10^k r_1-r_2
=
10^k\frac{U_1}{b_1}
+
\frac{U_2}{b_2}.
}
\tag{10}
\]

这就是最高层真正的 rational gap。

---

### 5. 与四-offset compact kernel 的精确对应

沿用

\[
\varepsilon=10^{-2k},
\]

\[
X=\frac{x}{10^{r+g+1}},
\quad
W=\frac{w}{10^r},
\quad
Y=10^{k+g+1-s}y,
\quad
Z=\frac{z}{10^s}.
\]

则

\[
\boxed{
\frac{U_1}{10^{r+g+1}}=X+W,
}
\tag{11}
\]

\[
\boxed{
\frac{U_2}{10^s}=Y+Z.
}
\tag{12}
\]

又

\[
\frac{b_1}{10^{m_1}}=1-\varepsilon W,
\qquad
\frac{b_2}{10^{m_2-1}}=1+\varepsilon Y.
\]

令

\[
L_0=10^{2k+r+s}.
\]

把 (9) 除以 `L_0`：

\[
\boxed{
\frac{\Delta}{L_0}
=(1+\varepsilon Y)(X+W)
 +(1-\varepsilon W)(Y+Z).
}
\tag{13}
\]

展开恰为前文

\[
X+W+Y+Z+\varepsilon(XY-WZ).
\]

所以 residue kernel 与 compact offset kernel 完全等价，但 (13) 保留了两个正的既约余量块，后续做素数与整除分析更自然。

---

### 6. `g\ge1` 时两个余量都有固定十进制上界

前文已经证明在 `g\ge1` 的最高层：

\[
\boxed{
\frac12<\frac{\Delta}{L_0}<\frac56,
}
\tag{14}
\]

并且

\[
\delta:=1-t<\frac45\varepsilon.
\]

因此

\[
\frac{b_1}{10^{m_1}}>t>1-\frac45\varepsilon
\ge\frac{124}{125},
\]

即

\[
1-\varepsilon W>\frac{124}{125}.
\tag{15}
\]

从 (13) 的第一正项：

\[
(1+\varepsilon Y)(X+W)<\frac56,
\]

故

\[
\boxed{
0<X+W<\frac56.
}
\tag{16}
\]

也就是

\[
\boxed{
0<U_1<\frac56\,10^{r+g+1}.
}
\tag{17}
\]

从第二正项及 (15)：

\[
\frac{124}{125}(Y+Z)<\frac56,
\]

所以

\[
\boxed{
0<Y+Z<\frac{625}{744}.
}
\tag{18}
\]

即

\[
\boxed{
0<U_2<\frac{625}{744}\,10^s.
}
\tag{19}
\]

另一方面，由 (13) 下界 `>1/2`。又由 `\delta<4\varepsilon/5` 可得

\[
1+\varepsilon Y<\frac1{1-\delta}<\frac{125}{124}.
\]

若同时

\[
X+W\le\frac{62}{249},
\qquad
Y+Z\le\frac{62}{249},
\]

则

\[
\frac{\Delta}{L_0}
<
\left(\frac{125}{124}+1\right)\frac{62}{249}
=\frac12,
\]

矛盾。因此

\[
\boxed{
\max\left(
\frac{U_1}{10^{r+g+1}},
\frac{U_2}{10^s}
\right)
>\frac{62}{249}.
}
\tag{20}
\]

也就是说，两个余量至少有一个必须占据其自然十进制尺度的约四分之一以上；不能同时退化成极小余量。

---

### 7. rational gap 的固定半尺度窗口

由 (10) 与

\[
\frac{\Delta}{G}
=
\frac{L_0}{G}\frac{\Delta}{L_0},
\]

而

\[
G=b_1b_2
=10^{3k+r+s-g-1}
(1-\varepsilon W)(1+\varepsilon Y),
\]

有

\[
\boxed{
10^k\frac{U_1}{b_1}+\frac{U_2}{b_2}
=
10^{g+1-k}
\frac{\Delta/L_0}
{(1-\varepsilon W)(1+\varepsilon Y)}.
}
\tag{21}
\]

在 `g\ge1` 时，利用

\[
\frac12<\frac{\Delta}{L_0}<\frac56,
\]

以及

\[
1-\varepsilon W>\frac{124}{125},
\qquad
1+\varepsilon Y<\frac{125}{124},
\]

得到安全窗口

\[
\boxed{
\frac{62}{125}\,10^{g+1-k}
<
10^k\frac{U_1}{b_1}+\frac{U_2}{b_2}
<
\frac{625}{744}\,10^{g+1-k}.
}
\tag{22}
\]

因此最高层的 carrier gap 已被固定在大约 `1/2` 个自然十进制单位上。

---

### 8. 后续接口

最高层 `d=2,g\ge1` 现在可以完全改写成：

\[
\boxed{
 r,s\ge1,
}
\]

两个既约 rational defects

\[
\boxed{
\frac{U_1}{b_1},\qquad\frac{U_2}{b_2},
\quad
(U_1,b_1)=(U_2,b_2)=1,
}
\]

满足

\[
\boxed{
\frac{62}{125}\,10^{g+1-k}
<
10^k\frac{U_1}{b_1}+\frac{U_2}{b_2}
<
\frac{625}{744}\,10^{g+1-k},
}
\]

以及 residue-size 条件 (17)、(19)、(20)。

这一坐标下一步应优先把 denominator prime graph、safe integer-gap identity

\[
10^\ell E=b_3U
\]

和第三分母 funnel 转写成关于 `(b_1,U_1;b_2,U_2)` 的素数流条件。这样可以直接攻击 moving prefix，而无需重新展开四个大整数。

---

## 6. A1 top-layer half-gap shell — 2026-08-17

> 整合来源：`a1-top-layer-half-gap-shell-2026-08-17.md`。以下正文保留该来源的原始证明状态和审计边界。

本文继续 `top-layer.md`，在最高层

\[
d=s_1-g=2,
\qquad g\ge1
\]

中把两个既约 rational defects 的总 gap 从此前的粗窗口进一步压到一个宽度约 `0.035` 的半单位壳层。

核心结论是

\[
\boxed{
\frac{499}{1000}
<
\frac{
10^kU_1/b_1+U_2/b_2
}{10^{g+1-k}}
<
\frac{267}{500}.
}
\]

特别地，最小第二 surplus `s=1` 时强迫

\[
\boxed{z\in\{1,3\}.}
\]

本文结论均为 **已严格完成**。

---

### 1. 记号

沿用

\[
M=10^{k+g+1},
\qquad
A_0=10^k r_1,
\]

\[
t=\frac{r_2}{A_0},
\qquad
R_0=\frac R{A_0},
\qquad
q_0=\frac{r_3}{A_0},
\]

以及

\[
\varepsilon=10^{-2k},
\qquad
\delta=1-t,
\qquad
\alpha=1-R_0.
\]

前文已严格证明，在 `d=2,g\ge1` 中

\[
r=m_1-2k\ge1,
\qquad
s=m_2+g-k\ge1,
\]

并且

\[
\boxed{0<\delta<\frac45\varepsilon.}
\tag{1}
\]

球面关系为

\[
R_0^2=t^2+\varepsilon+q_0^2.
\tag{2}
\]

---

### 2. `alpha/epsilon` 只有百分之二量级

contact 恒等式给出

\[
\alpha
=\lambda(1-10^{-g}t)
+
\theta(R_0-q_0),
\]

其中

\[
0<\theta<\frac1Q,
\qquad
\lambda=\frac{b_2}{Q}.
\]

所以

\[
\boxed{0<\alpha<\lambda+\frac1Q.}
\tag{3}
\]

最高层四因子分解与 (1) 说明每一个因子都大于 `t=1-delta`。因此

\[
\frac{b_1}{10^{m_1}}>1-\delta,
\qquad
\frac{b_2}{10^{m_2-1}}<\frac1{1-\delta}.
\]

于是

\[
\lambda
<
\frac{10^{-m_1-1}}{(1-\delta)^2}.
\]

因为

\[
m_1=2k+r,\qquad r\ge1,
\]

除以 `epsilon=10^{-2k}`：

\[
\frac\lambda\varepsilon
<
\frac{10^{-r-1}}{(1-\delta)^2}
\le
\frac{10^{-2}}{(1-0.008)^2}
<0.0102.
\tag{4}
\]

另一方面

\[
\frac1Q
<
\frac1{b_1 10^{m_2}}
<
\frac{10^{-m_1-m_2}}{1-\delta}.
\]

由于 `r\ge1,m_2\ge1`：

\[
\frac1{Q\varepsilon}
<
\frac{10^{-r-m_2}}{1-\delta}
\le
\frac{10^{-2}}{0.992}
<0.0101.
\tag{5}
\]

由 (3)–(5)：

\[
\boxed{
0<\frac\alpha\varepsilon<0.0203.
}
\tag{6}
\]

---

### 3. `delta/epsilon` 被压到 `1/2` 附近

由

\[
R_0=1-\alpha,
\qquad
t=1-\delta,
\]

把球面式 (2) 展开：

\[
1-2\alpha+\alpha^2
=1-2\delta+\delta^2+\varepsilon+q_0^2.
\]

所以

\[
\boxed{
2(\delta-\alpha)
=\varepsilon+q_0^2+\delta^2-\alpha^2.
}
\tag{7}
\]

最高层有

\[
q_0<10^{-k-2g},
\]

因此

\[
\boxed{
\frac{q_0^2}{\varepsilon}<10^{-4g}\le10^{-4}.
}
\tag{8}
\]

由 (1)：

\[
\frac{\delta^2}{2\varepsilon}
<\frac{8}{25}\varepsilon
\le0.0032.
\tag{9}
\]

结合 (6)–(9)，从 (7) 得到

\[
\frac\delta\varepsilon
<
\frac12+0.0203+0.00005+0.0032
<\frac{21}{40}.
\]

即

\[
\boxed{
\frac\delta\varepsilon<\frac{21}{40}.
}
\tag{10}
\]

下界方面，(6) 给出 `alpha<0.0203 epsilon`，故 `alpha^2<epsilon^2/1600`。由 (7) 丢掉正的 `alpha,q_0,delta^2` 项，仅保留可能的 `-alpha^2`：

\[
\frac\delta\varepsilon
>
\frac12-
rac{\alpha^2}{2\varepsilon}
>
\frac12-
rac1{320000}
>
\frac{499}{1000}.
\]

所以

\[
\boxed{
\frac{499}{1000}
<\frac\delta\varepsilon
<\frac{21}{40}.
}
\tag{11}
\]

---

### 4. carrier gap 的半单位壳层

定义真实 carrier gap

\[
D_0:=A_0-r_2=\delta A_0.
\]

自然十进制尺度为

\[
\boxed{
H_0=M\varepsilon=10^{g+1-k}.
}
\tag{12}
\]

端点坐标给出

\[
\frac{A_0}{M}
=
\frac{1+\varepsilon X}{1-\varepsilon W}.
\]

四因子乘积为 `t=1-delta`，故

\[
\frac1{1+\varepsilon X}>1-\delta,
\qquad
1-\varepsilon W>1-\delta.
\]

于是

\[
1<\frac{A_0}{M}<\frac1{(1-\delta)^2}
<\left(\frac{125}{124}\right)^2.
\tag{13}
\]

因为

\[
\frac{D_0}{H_0}
=\frac\delta\varepsilon\frac{A_0}{M},
\]

由 (11)–(13)：

\[
\frac{D_0}{H_0}>
rac{499}{1000},
\]

并且

\[
\frac{D_0}{H_0}
<
\frac{21}{40}\left(\frac{125}{124}\right)^2
<\frac{267}{500}.
\]

因此

\[
\boxed{
\frac{499}{1000}
<
\frac{D_0}{10^{g+1-k}}
<
\frac{267}{500}.
}
\tag{14}
\]

---

### 5. 用两个 coprime residues 重写半单位壳层

由 residue kernel：

\[
D_0
=10^k\frac{U_1}{b_1}+\frac{U_2}{b_2}.
\]

所以 (14) 等价于

\[
\boxed{
\frac{499}{1000}
<
\frac{
10^kU_1/b_1+U_2/b_2
}{10^{g+1-k}}
<
\frac{267}{500}.
}
\tag{15}
\]

此外利用

\[
U_1=10^{r+g+1}(X+W),
\qquad
b_1=10^{2k+r}(1-\varepsilon W),
\]

\[
U_2=10^s(Y+Z),
\qquad
b_2=10^{k-g+s-1}(1+\varepsilon Y),
\]

可以把 (15) 精确写成

\[
\boxed{
\frac{499}{1000}
<
\frac{X+W}{1-\varepsilon W}
+
\frac{Y+Z}{1+\varepsilon Y}
<
\frac{267}{500}.
}
\tag{16}
\]

这比此前 `Delta/L0` 的 `1/2`–`5/6` 窗显著更窄。

---

### 6. 最小第二 surplus `s=1`

若

\[
s=1,
\]

则前文已有

\[
s\le k+g,
\]

故

\[
y=0,
\qquad
b_2=10^{m_2-1}=10^{k-g},
\]

并且

\[
\gcd(z,10)=1.
\]

此时

\[
Y=0,
\qquad
Z=\frac z{10},
\]

而 (16) 中第一项严格为正。因此

\[
\frac z{10}<\frac{267}{500}=0.534,
\]

所以

\[
z\le5.
\]

再由 `gcd(z,10)=1`：

\[
\boxed{z\in\{1,3\}.}
\tag{17}
\]

两个子核分别满足：

#### `z=1`

\[
\boxed{
\frac{399}{1000}
<
\frac{X+W}{1-\varepsilon W}
<
\frac{217}{500}.
}
\tag{18}
\]

#### `z=3`

\[
\boxed{
\frac{199}{1000}
<
\frac{X+W}{1-\varepsilon W}
<
\frac{117}{500}.
}
\tag{19}
\]

所以 `s=1` 已经压成两个明确的第一余量窄窗。

---

### 7. 当前意义

最高层 `d=2,g\ge1` 现已具有一条真正的半单位刚性：

\[
10^k\frac{U_1}{b_1}+\frac{U_2}{b_2}
\]

只能落在

\[
(0.499,0.534)\cdot10^{g+1-k}
\]

中，而两个分数各自既约。

因此后续可以按 `s` 从小到大继续：

- `s=1` 已只剩 `z=1,3`；
- 一般短 `s\le k+g` 中 `y=0`，故第二项精确为 `z/10^s`，并且 `gcd(z,10)=1`；
- 长 `s>k+g` 才允许 `y>0`，需要单独研究。

这提供了一条比原四-offset kernel 更适合做有限 leading-digit / p-adic 分层的入口。

---

## 7. A1 top-layer half-gap lower-endpoint sharpening — 2026-08-17

> 整合来源：`a1-top-layer-half-gap-sharpening-2026-08-17.md`。以下正文保留该来源的原始证明状态和审计边界。

本文对 `top-layer.md` 的保守下界做一个严格加强。

原文件已经证明

\[
\frac{
10^kU_1/b_1+U_2/b_2
}{10^{g+1-k}}
<\frac{267}{500}.
\]

下界当时保守写成 `499/1000`。实际上 exact sphere 立即给出严格的

\[
\boxed{
\frac{
10^kU_1/b_1+U_2/b_2
}{10^{g+1-k}}
>\frac12.
}
\]

因此最高层 `d=2,g\ge1` 的真实 half-gap shell 为

\[
\boxed{
\frac12
<
\frac{
10^kU_1/b_1+U_2/b_2
}{10^{g+1-k}}
<\frac{267}{500}.
}

本文结论为 **已严格完成 / sharpening**。

---

### 1. `delta>alpha`

沿用

\[
R_0=1-\alpha,
\qquad
t=1-\delta.
\]

因为

\[
R^2=r_1^2+r_2^2+r_3^2>r_2^2,
\]

有

\[
R>r_2.
\]

除以 `A_0=10^kr_1>0`：

\[
R_0>t.
\]

因此

\[
\boxed{\delta>\alpha>0.}
\tag{1}
\]

---

### 2. 球面展开直接给 `delta/epsilon>1/2`

前文件已经得到精确恒等式

\[
2(\delta-\alpha)
=\varepsilon+q_0^2+\delta^2-\alpha^2.
\tag{2}
\]

由 (1)：

\[
\delta^2-\alpha^2>0.
\]

并且

\[
q_0^2>0.
\]

所以 (2) 立刻给出

\[
2(\delta-\alpha)>\varepsilon.
\]

从而

\[
\delta>\alpha+\frac\varepsilon2>
rac\varepsilon2.
\]

即

\[
\boxed{
\frac\delta\varepsilon>\frac12.
}
\tag{3}
\]

---

### 3. 真实 carrier gap 的严格半单位下界

真实 gap 为

\[
D_0=A_0-r_2=\delta A_0.
\]

自然尺度

\[
H_0=M\varepsilon,
\qquad
M=10^{k+g+1}.
\]

而 residue kernel 中

\[
A_0=M+10^k\frac{U_1}{b_1}>M.
\]

所以

\[
\frac{A_0}{M}>1.
\]

结合 (3)：

\[
\frac{D_0}{H_0}
=
\frac\delta\varepsilon\frac{A_0}{M}
>\frac12.
\]

因此

\[
\boxed{
\frac{D_0}{10^{g+1-k}}>\frac12.
}
\tag{4}
\]

再用

\[
D_0=10^k\frac{U_1}{b_1}+\frac{U_2}{b_2}
\]

得到

\[
\boxed{
\frac{
10^kU_1/b_1+U_2/b_2
}{10^{g+1-k}}
>\frac12.
}
\tag{5}
\]

---

### 4. 与既有上界合并

`top-layer.md` 已严格证明

\[
\frac{D_0}{10^{g+1-k}}<\frac{267}{500}.
\]

故最终壳层为

\[
\boxed{
\frac12
<
\frac{D_0}{10^{g+1-k}}
<\frac{267}{500}.
}
\tag{6}

其宽度仅为

\[
\frac{267}{500}-\frac12
=\frac{17}{500}
=0.034.
\]

---

### 5. `s=1` 两个子核的同步加强

当 `s=1` 时已知

\[
y=0,
\qquad z\in\{1,3\}.
\]

定义第一 residue contribution

\[
\Phi_1
=\frac{
10^kU_1/b_1
}{10^{g+1-k}}.
\]

第二项精确为

\[
\frac{U_2/b_2}{10^{g+1-k}}
=\frac z{10}.
\]

由 (6)：

#### `z=1`

\[
\boxed{
\frac25<\Phi_1<\frac{217}{500}.
}
\tag{7}
\]

#### `z=3`

\[
\boxed{
\frac15<\Phi_1<\frac{117}{500}.
}
\tag{8}
\]

所以第一余量分别严格位于 `2/5` 与 `1/5` 自然尺度的上侧；这正是 minimal-surplus 六类型核使用的加强版本。

---

## 8. A1 top-layer positive excess decomposition — 2026-08-17

> 整合来源：`a1-top-layer-excess-decomposition-2026-08-17.md`。以下正文保留该来源的原始证明状态和审计边界。

本文把最高层 `d=2` 的 half-gap 刚性进一步改写成一个精确的**正项分解**。

设两个 coprime residue 对 carrier gap 的自然尺度贡献为

\[
\phi_1
:=
\frac{10^kU_1/b_1}{10^{g+1-k}},
\qquad
\phi_2
:=
\frac{U_2/b_2}{10^{g+1-k}}.
\]

则真实 normalized carrier gap 是

\[
\phi_1+\phi_2.
\]

本文证明

\[
\boxed{
\begin{aligned}
2(\phi_1+\phi_2)-1
={}&
\frac{\mathfrak h}{M\varepsilon}
\left(
1+\varepsilon\phi_1+\frac RM
\right)\\
&+\frac{(r_3/M)^2}{\varepsilon}\\
&+\varepsilon
\left(
2\phi_1+\phi_2^2-\phi_1^2
\right)
+\varepsilon^2\phi_1^2,
\end{aligned}
}
\]

其中

\[
M=10^{k+g+1},
\qquad
\varepsilon=10^{-2k},
\qquad
\mathfrak h=10^kr_1-R>0.
\]

右端每一项都严格非负，第一项严格正。因此 half-gap 超过 `1/2` 的 excess 被拆成四个可独立估计的来源。

本文结论均为 **已严格完成**。

---

### 1. 中心化 residue 坐标

最高层 residue kernel 给出

\[
r_1=10^{g+1}+\frac{U_1}{b_1},
\]

\[
r_2=M-\frac{U_2}{b_2},
\qquad
M=10^{k+g+1}.
\]

定义自然 gap 尺度

\[
H_0=10^{g+1-k}=M\varepsilon,
\qquad
\varepsilon=10^{-2k}.
\]

令

\[
\boxed{
\phi_1=
\frac{10^kU_1/b_1}{H_0},
}
\tag{1}
\]

\[
\boxed{
\phi_2=
\frac{U_2/b_2}{H_0}.
}
\tag{2}
\]

于是得到三个精确中心化公式：

\[
\boxed{
\frac{10^kr_1}{M}
=1+\varepsilon\phi_1,
}
\tag{3}
\]

\[
\boxed{
\frac{r_2}{M}
=1-\varepsilon\phi_2,
}
\tag{4}
\]

\[
\boxed{
\frac{r_1}{M}
=10^{-k}(1+\varepsilon\phi_1)
=\sqrt\varepsilon(1+\varepsilon\phi_1).
}
\tag{5}
\]

因此

\[
10^kr_1-r_2
=M\varepsilon(\phi_1+\phi_2).
\tag{6}
\]

---

### 2. 球面在中心坐标中的精确式

记

\[
\zeta=\frac{r_3}{M},
\qquad
\widehat R=\frac RM.
\]

球面

\[
R^2=r_1^2+r_2^2+r_3^2
\]

结合 (4)–(5) 给出

\[
\boxed{
\widehat R^2
=(1-\varepsilon\phi_2)^2
+\varepsilon(1+\varepsilon\phi_1)^2
+\zeta^2.
}
\tag{7}
\]

另一方面令

\[
A_0=10^kr_1=M(1+\varepsilon\phi_1).
\]

则直接展开

\[
\frac{A_0^2-R^2}{M^2}
=
\varepsilon
\left[
2(\phi_1+\phi_2)-1
+\varepsilon(\phi_1^2-2\phi_1-\phi_2^2)
-\varepsilon^2\phi_1^2
\right]
-\zeta^2.
\tag{8}

---

### 3. contact height `h`

定义第一 carrier 与球面的正 gap

\[
\boxed{
\mathfrak h=A_0-R>0.
}
\tag{9}
\]

则差平方给出

\[
A_0^2-R^2
=\mathfrak h(A_0+R).
\]

除以 `M^2`：

\[
\boxed{
\frac{A_0^2-R^2}{M^2}
=
\frac{\mathfrak h}{M}
\left(
1+\varepsilon\phi_1+\widehat R
\right).
}
\tag{10}
\]

同时 rational contact 给出

\[
P-R=\theta(R-r_3),
\]

而前两块权重表达为

\[
P=(1-\lambda)A_0+\lambda10^{-g}r_2.
\]

故

\[
A_0-P
=\lambda(A_0-10^{-g}r_2).
\]

因此

\[
\boxed{
\frac{\mathfrak h}{M}
=
\lambda
\left[
(1+\varepsilon\phi_1)
-10^{-g}(1-\varepsilon\phi_2)
\right]
+\theta(\widehat R-\zeta).
}
\tag{11}
\]

右端两项均为正。

---

### 4. 正项 excess 分解

把 (10) 代入 (8)，再除以 `epsilon` 并移项：

\[
\begin{aligned}
2(\phi_1+\phi_2)-1
={}&
\frac{\mathfrak h}{M\varepsilon}
\left(
1+\varepsilon\phi_1+\widehat R
\right)\\
&+\frac{\zeta^2}{\varepsilon}\\
&+\varepsilon
\left(
2\phi_1+\phi_2^2-\phi_1^2
\right)\\
&+\varepsilon^2\phi_1^2.
\end{aligned}
\]

即

\[
\boxed{
\begin{aligned}
2(\phi_1+\phi_2)-1
={}&
\frac{\mathfrak h}{M\varepsilon}
\left(
1+\varepsilon\phi_1+\frac RM
\right)\\
&+\frac{(r_3/M)^2}{\varepsilon}\\
&+\varepsilon
\left(
2\phi_1+\phi_2^2-\phi_1^2
\right)
+\varepsilon^2\phi_1^2.
\end{aligned}
}
\tag{12}
\]

由于 half-gap shell 已给出

\[
0<\phi_1,\phi_2<\frac{267}{500}<1,
\]

所以

\[
2\phi_1+\phi_2^2-\phi_1^2
=\phi_1(2-\phi_1)+\phi_2^2>0.
\]

结合 (9)、`r_3>0`：式 (12) 右边四行全部为正。

这直接重新证明

\[
\boxed{\phi_1+\phi_2>\frac12.}
\]

---

### 5. 四种 excess source

式 (12) 把超过 `1/2` 的 excess 精确分成：

1. **prefix/contact height**
   \[
   \frac{\mathfrak h}{M\varepsilon}
   \left(1+\varepsilon\phi_1+R/M\right);
   \]
   其中 `h` 又按 (11) 分成 `lambda` 前缀混合与 `theta` 第三块接触两项；
2. **third-radius source**
   \[
   (r_3/M)^2/\varepsilon;
   \]
3. **first curvature source**
   \[
   \varepsilon\phi_1(2-\phi_1);
   \]
4. **second curvature source**
   \[
   \varepsilon\phi_2^2+\varepsilon^2\phi_1^2.
   \]

由于 `g\ge1` 时 half-gap sharpening 给出

\[
2(\phi_1+\phi_2)-1<\frac{34}{500}=0.068,
\]

上述每个正 source 都自动小于 `0.068`。

---

### 6. 最小双 surplus `r=s=1` 的进一步下推

现在取

\[
r=s=1,
\qquad g\ge1.
\]

此前已有

\[
b_2=10^{k-g},
\qquad
z\in\{1,3\},
\]

以及

\[
\phi_2=\frac z{10}.
\]

此时

\[
\lambda
=\frac{b_2}{b_1 10^{m_2}+b_2}
=\frac1{10b_1+1}.
\tag{13}
\]

又

\[
b_1=10^{2k+1}-w<10^{2k+1},
\]

所以

\[
\boxed{
\frac\lambda\varepsilon
>
\frac1{100}.
}
\tag{14}
\]

由 `g\ge1`、`t<1`：

\[
(1+\varepsilon\phi_1)
-10^{-g}(1-\varepsilon\phi_2)
>1-10^{-g}\ge\frac9{10}.
\]

故 (11)、(14) 给出

\[
\frac{\mathfrak h}{M\varepsilon}
>
\frac9{1000}.
\tag{15}
\]

同时

\[
R>r_2=M(1-\varepsilon\phi_2),
\]

所以

\[
1+\varepsilon\phi_1+\frac RM
>
2-\varepsilon\phi_2
\ge2-
rac3{1000}
>\frac{199}{100}.
\]

因此式 (12) 的第一 source 单独已经给出

\[
2(\phi_1+\phi_2)-1
>
\frac9{1000}\frac{199}{100}
>
\frac{17}{1000}.
\]

从而

\[
\boxed{
\phi_1+\phi_2>\frac{1017}{2000}=0.5085.
}
\tag{16}
\]

于是六类型中的第一余量窗同步加强为：

#### `z=1`

\[
\boxed{
\frac{817}{2000}
<\phi_1<\frac{217}{500},
}
\tag{17}
\]

即

\[
0.4085<\phi_1<0.434.
\]

#### `z=3`

\[
\boxed{
\frac{417}{2000}
<\phi_1<\frac{117}{500},
}
\tag{18}
\]

即

\[
0.2085<\phi_1<0.234.
\]

所以最小双 surplus 的两个 first-residue interval 宽度已经压到约 `0.0255`。

---

### 7. 后续用途

式 (12) 是当前最高层最适合作为下一阶段主方程的形式：

- 所有项同号，不能互相抵消；
- 可以按 `r,m_2,k,g` 分别估计 `lambda,theta,zeta,epsilon`；
- 边界 surplus 越小，`lambda/theta` source 越大；
- surplus 越大，half-gap 越趋近纯曲率中心 `1/2`；
- `g=0` 时 third-radius source 不再自动很小，正好解释该扇区为何需要单独处理。

后续关闭 `d=2` 应围绕这个 positive source decomposition 做 surplus source split，而无需重新回到四个原始大整数。

---

## 9. A1 top layer minimal-surplus kernel — 2026-08-17

> 整合来源：`a1-top-layer-minimal-surplus-kernel-2026-08-17.md`。以下正文保留该来源的原始证明状态和审计边界。

本文研究最高层

\[
d=2,\qquad g\ge1
\]

中的最小双 surplus 边界

\[
\boxed{r=s=1.}
\]

结合 coprime-residue kernel 与 half-gap shell，可以把这一边界压成 6 个 `(z,w)` 类型，并得到跨块整数 `a_2` 与 `b_1` 的绝对小差。

本文结论均为 **已严格完成**。

---

### 1. 边界形状

`r=s=1` 意味着

\[
m_1=2k+1,
\qquad
m_2=k-g+1.
\]

由于 `m_2\ge1`，必有

\[
\boxed{1\le g\le k.}
\tag{1}
\]

endpoint normal form 变成

\[
\boxed{b_1=10^{2k+1}-w,}
\tag{2}
\]

\[
\boxed{a_1=10^{2k+g+2}+x,}
\tag{3}
\]

\[
\boxed{b_2=10^{k-g}+y,}
\tag{4}
\]

\[
\boxed{a_2=10^{2k+1}-z.}
\tag{5}
\]

---

### 2. `s=1` 强迫 `y=0` 与 `z=1,3`

因为

\[
s=1\le k+g,
\]

endpoint kernel 已经给出

\[
\boxed{y=0.}
\]

所以

\[
\boxed{b_2=10^{k-g}.}
\tag{6}
\]

原既约性 `gcd(a_2,b_2)=1` 等价于

\[
\gcd(z,10)=1.
\]

half-gap shell 又给出

\[
\boxed{z\in\{1,3\}.}
\tag{7}
\]

因此第二块已经完全固定为两个形状：

\[
\boxed{
(a_2,b_2)
=
(10^{2k+1}-1,\ 10^{k-g})
}
\]

或

\[
\boxed{
(a_2,b_2)
=
(10^{2k+1}-3,\ 10^{k-g}).
}
\]

---

### 3. 第一余量位置强迫 `w` 进入绝对有限集合

在 `r=1` 时

\[
U_1=x+10^{g+1}w,
\]

自然余量尺度是

\[
10^{r+g+1}=10^{g+2}.
\]

令

\[
\Phi_1
:=
\frac{
10^kU_1/b_1
}{10^{g+1-k}}.
\]

则

\[
\Phi_1
=
\frac{10^{2k-g-1}U_1}{b_1}.
\tag{8}
\]

half-gap shell 在 `s=1` 时给出：

#### `z=1`

\[
\boxed{
\frac25<\Phi_1<\frac{217}{500}=0.434.
}
\tag{9}
\]

#### `z=3`

\[
\boxed{
\frac15<\Phi_1<\frac{117}{500}=0.234.
}
\tag{10}
\]

这里下界使用更强事实：总 normalized gap 严格大于 `1/2`；证明见后续 half-gap sharpening 注记。

另一方面由 (2)：

\[
b_1<10^{2k+1}.
\]

所以 (8) 给出

\[
\Phi_1
>
\frac{U_1}{10^{g+2}}.
\tag{11}
\]

若 `z=1`，由 (9)、(11)：

\[
U_1<0.434\cdot10^{g+2}
=4.34\cdot10^{g+1}.
\]

但

\[
U_1=x+10^{g+1}w\ge10^{g+1}w,
\]

故

\[
\boxed{z=1\Longrightarrow w\le4.}
\tag{12}
\]

若 `z=3`，同理由 (10)：

\[
U_1<0.234\cdot10^{g+2}
=2.34\cdot10^{g+1},
\]

所以

\[
\boxed{z=3\Longrightarrow w\le2.}
\tag{13}
\]

由于 `w\ge1`，最小双 surplus 边界只剩

\[
\boxed{
(z,w)
\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\}.
}
\tag{14}
\]

这是一个与 `k,g` 无关的绝对六类型核。

---

### 4. 跨块整数出现绝对小差

由 (2)、(5)：

\[
a_2-b_1
=(10^{2k+1}-z)-(10^{2k+1}-w)
=w-z.
\]

因此

\[
\boxed{a_2-b_1=w-z.}
\tag{15}
\]

对六种类型分别只有

\[
w-z\in\{-2,-1,0,1,2,3\}.
\]

更具体地：

| `z` | `w` | `a_2-b_1` |
|---:|---:|---:|
| 1 | 1 | 0 |
| 1 | 2 | 1 |
| 1 | 3 | 2 |
| 1 | 4 | 3 |
| 3 | 1 | -2 |
| 3 | 2 | -1 |

所以两个本来有 `2k+1` 位的跨块整数被强迫相差至多 3。

---

### 5. `a_2=b_1` 子型

六类型中唯一精确相等的是

\[
(z,w)=(1,1),
\]

此时

\[
\boxed{a_2=b_1=10^{2k+1}-1.}
\tag{16}
\]

而

\[
b_2=10^{k-g}.
\]

这个子型值得后续优先检查，因为：

- `a_2` 与 `b_1` 完全共享十进制 repunit-complement 形状；
- `G=b_1b_2` 与 `N=(a_1b_2)^2+(a_2b_1)^2` 因 `a_2=b_1` 明显简化；
- denominator prime graph 可直接按 `10^{2k+1}-1` 的素因子结构分析。

本文暂不声称该子型已经为空。

---

### 6. 第一余量的窄位置

还可把 `U_1` 写成

\[
U_1=x+10^{g+1}w.
\]

由 (9)–(10) 与

\[
b_1=10^{2k+1}-w
\]

得到：

#### `z=1`

\[
\frac25
<
\frac{10^{2k-g-1}U_1}{10^{2k+1}-w}
<0.434.
\]

#### `z=3`

\[
\frac15
<
\frac{10^{2k-g-1}U_1}{10^{2k+1}-w}
<0.234.
\]

因此 `U_1` 分别紧贴

\[
\frac25\,10^{g+2}
=4\cdot10^{g+1}
\]

或

\[
\frac15\,10^{g+2}
=2\cdot10^{g+1}
\]

的上侧。

这意味着六类型还可以继续按 `x` 相对于

\[
(4-w)10^{g+1}
\]

或

\[
(2-w)10^{g+1}
\]

的偏移做下一层整数化。

---

### 7. 当前意义

最高层最小边界

\[
r=s=1
\]

现已从两个无界大分母压成：

- `1\le g\le k`；
- `b_2=10^{k-g}`；
- `z\in\{1,3\}`；
- 绝对 6 个 `(z,w)` 类型；
- `a_2-b_1\in\{-2,-1,0,1,2,3\}`；
- 第一余量 `U_1` 位于 `2/5` 或 `1/5` 十进制尺度的窄上侧区间。

下一步应优先对六类型做模 `3,7,11`、`2/5` 赋值和 denominator prime graph 检查；其中 `(z,w)=(1,1)` 的 `a_2=b_1=10^{2k+1}-1` 是最刚性的首选子型。

---

## 10. A1 top-layer minimal-surplus off-diagonal squeeze — 2026-08-17

> 整合来源：`a1-top-layer-minimal-offdiagonal-2026-08-17.md`。以下正文保留该来源的原始证明状态和审计边界。

本文继续 `top-layer.md`，研究最小双 surplus

\[
r=s=1,
\qquad g\ge1
\]

中的 off-diagonal 区域

\[
\boxed{k>g.}
\]

此时第三 contact source 比 prefix source 至少再小一个十倍，且 `k\ge2` 令曲率参数

\[
\varepsilon=10^{-2k}
\]

至多为 `10^{-4}`。因此正项 excess 分解可以显著收紧。

核心结论：

\[
\boxed{
\frac{1017}{2000}
<\phi_1+\phi_2
<\frac{5111}{10000}.
}
\]

于是：

\[
\boxed{
z=1:\quad
\frac{817}{2000}<\phi_1<\frac{4111}{10000},
}
\]

\[
\boxed{
z=3:\quad
\frac{417}{2000}<\phi_1<\frac{2111}{10000}.
}
\]

两个 first-residue interval 的宽度都小于 `0.0026`。

本文结论均为 **已严格完成**。

---

### 1. 最小边界回顾

`r=s=1` 已有

\[
1\le g\le k,
\]

\[
b_1=10^{2k+1}-w,
\qquad
b_2=10^{k-g},
\]

\[
z\in\{1,3\},
\]

以及六类型

\[
(z,w)
\in
\{(1,1),(1,2),(1,3),(1,4),(3,1),(3,2)\}.
\]

定义

\[
\varepsilon=10^{-2k},
\]

\[
\phi_1
=\frac{10^kU_1/b_1}{10^{g+1-k}},
\qquad
\phi_2=\frac z{10}.
\]

positive excess decomposition 给出

\[
\begin{aligned}
2(\phi_1+\phi_2)-1
={}&
\frac{\mathfrak h}{M\varepsilon}
\left(1+\varepsilon\phi_1+\frac RM\right)\\
&+\frac{(r_3/M)^2}{\varepsilon}
+\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
+\varepsilon^2\phi_1^2.
\end{aligned}
\tag{1}
\]

并且此前已证明下界

\[
\boxed{
\phi_1+\phi_2>\frac{1017}{2000}.
}
\tag{2}
\]

---

### 2. `lambda/epsilon` 几乎精确等于 `1/100`

因为

\[
b_2=10^{k-g},
\qquad
m_2=k-g+1,
\]

有

\[
Q=10^{k-g}(10b_1+1),
\]

所以

\[
\lambda=\frac{b_2}{Q}
=\frac1{10b_1+1}.
\]

又

\[
b_1=10^{2k+1}-w,
\]

故

\[
\boxed{
\frac\lambda\varepsilon
=
\frac1{100-(10w-1)\varepsilon}.
}
\tag{3}
\]

六类型中 `w\le4`。

现在额外假设

\[
k>g\ge1.
\]

于是

\[
k\ge2,
\qquad
\varepsilon\le10^{-4}.
\]

因此

\[
100-(10w-1)\varepsilon
\ge100-39\cdot10^{-4}
=99.9961,
\]

所以

\[
\boxed{
\frac\lambda\varepsilon<0.010001.
}
\tag{4}
\]

---

### 3. `theta` source 再小一个十倍

在 `s=1` 时

\[
D=10^gQ=10^k(10b_1+1).
\]

又

\[
\theta=\frac\rho D,
\qquad
10^{g-1}\le\rho<10^g.
\]

所以

\[
\frac{\theta}{\lambda}
=\frac\rho{10^k}.
\]

若 `k>g`：

\[
\frac\rho{10^k}<10^{g-k}\le\frac1{10}.
\]

因此由 (4)

\[
\boxed{
\frac\theta\varepsilon<0.0010001.
}
\tag{5}
\]

---

### 4. contact-height source 的统一上界

此前 half-gap shell 给出

\[
0<\phi_1<0.434,
\qquad
0<\phi_2\le0.3.
\]

因此

\[
1+\varepsilon\phi_1<1.0000434.
\tag{6}
\]

contact height 满足

\[
\frac{\mathfrak h}{M}
=
\lambda
\left[(1+\varepsilon\phi_1)
-10^{-g}(1-\varepsilon\phi_2)\right]
+\theta\left(\frac RM-\frac{r_3}{M}\right).
\]

两个方括号均严格小于 `1+epsilon phi_1`，并且

\[
\frac RM<\frac{10^kr_1}{M}=1+\varepsilon\phi_1.
\]

于是由 (4)–(6)：

\[
\boxed{
\frac{\mathfrak h}{M\varepsilon}
<
(0.010001+0.0010001)\,1.0000434
<0.011002.
}
\tag{7}
\]

此外

\[
1+\varepsilon\phi_1+\frac RM
<2(1+\varepsilon\phi_1)
<2.0000868.
\]

所以 (1) 第一项严格小于

\[
\boxed{0.022005.}
\tag{8}
\]

---

### 5. 其余三个 source 的总量不到 `0.000196`

最高层有

\[
\frac{(r_3/M)^2}{\varepsilon}<10^{-4g}\le10^{-4}.
\tag{9}
\]

又

\[
2\phi_1+\phi_2^2-\phi_1^2
<2\phi_1+\phi_2^2
<2(0.434)+0.3^2
=0.958.
\]

因为 `epsilon<=10^{-4}`：

\[
\varepsilon(2\phi_1+\phi_2^2-\phi_1^2)
<0.0000958.
\tag{10}
\]

并且

\[
\varepsilon^2\phi_1^2
<10^{-8}(0.434)^2
<2\cdot10^{-9}.
\tag{11}
\]

所以 (9)–(11) 总和严格小于

\[
0.000196.
\tag{12}
\]

---

### 6. off-diagonal half-gap 被压到宽度 `0.0026`

把 (8)、(12) 代入 (1)：

\[
2(\phi_1+\phi_2)-1
<0.022201.
\]

因此

\[
\phi_1+\phi_2
<0.5111005
<\frac{5111}{10000}.
\]

结合 (2)：

\[
\boxed{
\frac{1017}{2000}
<\phi_1+\phi_2
<\frac{5111}{10000}.
}
\tag{13}
\]

#### `z=1`

此时 `phi_2=1/10`：

\[
\boxed{
\frac{817}{2000}
<\phi_1
<\frac{4111}{10000}.
}
\tag{14}
\]

即

\[
0.4085<\phi_1<0.4111.
\]

#### `z=3`

此时 `phi_2=3/10`：

\[
\boxed{
\frac{417}{2000}
<\phi_1
<\frac{2111}{10000}.
}
\tag{15}
\]

即

\[
0.2085<\phi_1<0.2111.
\]

两个区间宽度均为

\[
0.0026.
\]

---

### 7. 当前剩余分裂

最小双 surplus `r=s=1,g\ge1` 现在自然分成：

1. **off-diagonal** `k>g`：本文的极窄 first-residue interval；
2. **diagonal** `k=g`：`b_2=1`，且 `theta/lambda` 可在 `[1/10,1)` 中移动，需要单独处理。

因此六类型核中真正保留较大连续自由度的部分已经集中到

\[
\boxed{k=g.}
\]

后续应先攻击 diagonal kernel；off-diagonal 则适合继续做十进制 residue / congruence refinement。

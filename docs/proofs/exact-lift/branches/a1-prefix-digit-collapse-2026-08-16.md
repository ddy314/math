# A1 generic prefix digit collapse — 2026-08-16

本文继续 `a1-prefix-contact-window-2026-08-16.md`，把 moving-prefix core 的位数自由度进一步压缩。

核心结论：除两个低尺度角落 `(g,k)=(0,1),(0,2)` 外，A1 必须满足

\[
\boxed{g-1\le s_1\le g+2.}
\]

所以泛型 A1 的第一分数位数差只剩四条相邻层。

本文结论均为 **已严格完成**。

---

## 1. 无量纲前缀参数

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

## 2. 前缀拼接值的无量纲形式

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

## 3. contact 给出的 `F` 上界

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

## 4. 泛型尺度 `k+2g\ge3`

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
\frac{101}{100}t^2+rac1{100}.
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

## 5. `t\le2/5` 与下界矛盾

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
\frac14-rac4{25}-\frac1{100}
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

## 6. 第一分数位数差被压成四层

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

## 7. 唯一两个低尺度例外

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

### 泛型 chamber

\[
\boxed{k+2g\ge3}
\]

且只剩四个位数层

\[
\boxed{s_1=g-1,g,g+1,g+2.}
\]

### 低尺度 chamber

仅

\[
\boxed{(g,k)=(0,1),(0,2)}.
\]

这两个角落需要单独做更精确的实数矩形/局部算术分析。

---

## 8. 当前意义

这一步首次把 A1 的**移动前缀位数自由度**从无界二维区域压成：

- 一个泛型的四层带；
- 两个明确的低尺度角落。

因此后续无需再允许 `s_1-g\to+\infty`。任何全局 A1 候选都必须落在上述有限位数形状之一。

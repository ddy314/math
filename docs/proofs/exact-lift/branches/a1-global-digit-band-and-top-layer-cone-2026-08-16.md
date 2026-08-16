# A1 global digit band and top-layer cone — 2026-08-16

本文继续 `a1-prefix-digit-collapse-2026-08-16.md`。目标有两个：

1. 消去旧结论中 `(g,k)=(0,1),(0,2)` 两个低尺度例外，使第一分数位数带成为整个 A1 的无条件结论；
2. 对最高层 `s_1=g+2` 建立新的 denominator-position / contact 联立不等式，并推出显式 moving-prefix 锥。

除最后的研究含义说明外，本文命题均标记为 **已严格完成**。

---

## 1. 统一记号

沿用前文

\[
k=s_2-g\ge1,
\qquad
A_0=10^k r_1,
\qquad
 t=\frac{r_2}{A_0},
\]

\[
\lambda=\frac{b_2}{Q},
\qquad
Q=b_1 10^{m_2}+b_2,
\qquad
0<\lambda<\frac12,
\]

以及

\[
u:=\frac{P}{A_0}
=(1-\lambda)+\lambda10^{-g}t.
\]

记

\[
a=10^{-2k},
\qquad
z=\frac{r_3}{A_0},
\]

则无量纲 prefix defect 为

\[
\boxed{
F=u^2-t^2-a.
}
\tag{1}
\]

由 rational contact

\[
P-R<\frac RQ
\]

以及

\[
P^2-(r_1^2+r_2^2)
=r_3^2+(P-R)(P+R)
\]

得到

\[
\boxed{
F<z^2+c_Q\left(a+t^2+z^2\right),
\qquad
c_Q:=\frac{2+1/Q}{Q}.
}
\tag{2}
\]

又因为 `Q\ge11`，

\[
\boxed{c_Q\le\frac{23}{121}.}
\tag{3}
\]

---

## 2. 两个低尺度角落不再是例外

此前泛型论证覆盖

\[
k+2g\ge3,
\]

只留下

\[
(g,k)=(0,1),(0,2).
\]

现在证明这两个角落同样满足 `s_1\le g+2=2`。

假设反之

\[
s_1\ge3.
\]

因为 `g=0`，有 `s_3=0`。

### 2.1 对 `(g,k)=(0,1)`

位数窗给出

\[
r_1>10^2,
\qquad
r_2<10^2,
\qquad
r_3<10.
\]

因此

\[
A_0=10r_1>10^3,
\]

从而

\[
\boxed{t<\frac1{10},\qquad z<\frac1{100}.}
\tag{4}
\]

### 2.2 对 `(g,k)=(0,2)`

此时

\[
r_1>10^2,
\qquad
r_2<10^3,
\qquad
r_3<10,
\]

而

\[
A_0=100r_1>10^4.
\]

因此仍有更强的

\[
\boxed{t<\frac1{10},\qquad z<\frac1{100}.}
\tag{5}
\]

所以两个低尺度角落都可统一使用

\[
t<\frac1{10},
\qquad
z<\frac1{100},
\qquad
a\le\frac1{100}.
\tag{6}
\]

另一方面

\[
u=(1-\lambda)+\lambda t>1-\lambda>\frac12.
\]

由 (1)：

\[
F
>
\frac14-rac1{100}-\frac1{100}
=
\boxed{\frac{23}{100}}.
\tag{7}
\]

但由 (2)、(3)、(6)：

\[
F
<
\frac1{10^4}
+
\frac{23}{121}
\left(
\frac1{100}+\frac1{100}+\frac1{10^4}
\right)
<\frac1{250}.
\tag{8}
\]

而

\[
\frac1{250}<\frac{23}{100},
\]

矛盾。

故两个低尺度角落中都必有

\[
\boxed{s_1\le2.}
\tag{9}
\]

结合此前无条件 carrier 下界

\[
s_1\ge g-1,
\]

以及泛型区域已经证明的 `s_1\le g+2`，得到：

\[
\boxed{
\text{整个 A1 中恒有}
\qquad
g-1\le s_1\le g+2.
}
\tag{10}
\]

即

\[
\boxed{
s_1\in\{g-1,g,g+1,g+2\}.}
\tag{11}
\]

这条结论现在**没有任何低尺度例外**。

---

## 3. 泛型 contact 的更强统一下界

现在回到

\[
k+2g\ge3.
\]

由位数窗

\[
\frac{r_3}{r_2}<10^{2-k-2g}.
\]

记

\[
\boxed{\delta=10^{2-k-2g}\le\frac1{10}.}
\tag{12}
\]

则

\[
z<\delta t.
\]

将其代入 (2)：

\[
F
<
\delta^2t^2
+c_Q\left(a+(1+\delta^2)t^2\right).
\tag{13}
\]

而 `u>1-\lambda`，所以由 (1)、(13)：

\[
\boxed{
(1-\lambda)^2
<
(1+c_Q)
\left(a+(1+\delta^2)t^2\right).
}
\tag{14}
\]

这里还可以利用 `\lambda` 与 `Q` 并不独立。令

\[
h=\frac1Q.
\]

由于

\[
1-2\lambda
=
\frac{b_1 10^{m_2}-b_2}{Q}
\ge\frac1Q=h,
\]

有

\[
1+c_Q=(1+h)^2
\le4(1-\lambda)^2.
\tag{15}
\]

代入 (14)，约掉 `(1-\lambda)^2`：

\[
1<4\left(a+(1+\delta^2)t^2\right).
\]

而

\[
a\le\frac1{100},
\qquad
\delta^2\le\frac1{100},
\]

故

\[
\boxed{
t^2>\frac{24}{101}.}
\tag{16}
\]

即

\[
\boxed{
t>\sqrt{\frac{24}{101}}>\frac{12}{25}.}
\tag{17}
\]

这严格强化了前文的 `t>2/5`。

---

## 4. 最高位数层 `s_1=g+2` 的端点挤压

现在假设

\[
\boxed{s_1=g+2.}
\tag{18}
\]

令

\[
B=10^{m_1},
\qquad
M=10^{m_2},
\qquad
x=\frac{b_2}{M}\in\left[\frac1{10},1\right).
\]

由 `s_1=g+2`，

\[
n_1=m_1+g+2.
\]

直接从位数端点：

\[
a_2<10^{n_2},
\qquad
a_1\ge10^{n_1-1}=B10^{g+1}.
\]

所以

\[
t
=\frac{a_2b_1}{b_2 10^k a_1}
<
\frac{b_1}{10xB}.
\tag{19}
\]

又因为 `b_1<B` 且为整数，

\[
B\ge b_1+1.
\]

因此

\[
t
<
\frac{b_1}{10x(b_1+1)}.
\tag{20}
\]

而

\[
\lambda=\frac{x}{b_1+x}
\quad\Longrightarrow\quad
b_1=x\frac{1-\lambda}{\lambda}.
\]

代入 (20)：

\[
t
<
\frac{1-\lambda}
{10\left(x(1-\lambda)+\lambda\right)}.
\]

利用 `x\ge1/10`：

\[
\boxed{
 t<\frac{1-\lambda}{1+9\lambda}.
}
\tag{21}
\]

这条不等式是最高层独有的十进制端点损失：`t` 相对于 1 至少损失一个由 `\lambda` 控制的量。

结合 (17)、(21)：

\[
\frac{1-\lambda}{1+9\lambda}>\frac{12}{25},
\]

从而

\[
\boxed{
\lambda<\frac{13}{133}<\frac1{10}.
}
\tag{22}
\]

---

## 5. 最高层的纯 `(\lambda,k,g)` 必要不等式

由 (14) 和 (21)：

\[
(1-\lambda)^2
<
(1+c_Q)
\left(
 a+(1+\delta^2)
 \frac{(1-\lambda)^2}{(1+9\lambda)^2}
\right).
\]

约去 `(1-\lambda)^2`：

\[
\frac1{1+c_Q}
<
\frac{a}{(1-\lambda)^2}
+
\frac{1+\delta^2}{(1+9\lambda)^2}.
\tag{23}
\]

另一方面 `b_2\ge1`，所以

\[
\frac1Q\le\lambda.
\]

因而

\[
1+c_Q
=\left(1+\frac1Q\right)^2
\le(1+\lambda)^2.
\]

所以 (23) 强迫

\[
\boxed{
\frac1{(1+\lambda)^2}
<
\frac{a}{(1-\lambda)^2}
+
\frac{1+\delta^2}{(1+9\lambda)^2}.
}
\tag{24}
\]

这已经完全消去了第三块。

把不含 `\delta` 的两项作差：

\[
\frac1{(1+\lambda)^2}
-
\frac1{(1+9\lambda)^2}
=
\frac{16\lambda(1+5\lambda)}
{(1+\lambda)^2(1+9\lambda)^2}.
\tag{25}
\]

由 (22) 可使用 `0<\lambda<1/10`。于是

\[
\frac{16(1+5\lambda)}
{(1+\lambda)^2(1+9\lambda)^2}
>
\frac72.
\tag{26}
\]

例如右侧分母在该区间小于
`(11/10)^2(19/10)^2`，直接代入即可验证严格大于 `7/2`。

由 (24)–(26)：

\[
\frac72\lambda-\delta^2
<
\frac{a}{(1-\lambda)^2}
<
\frac{100}{81}a.
\]

因此得到最高层的统一锥：

\[
\boxed{
\lambda
<
\frac27\delta^2
+
\frac{200}{567}a.
}
\tag{27}
\]

代回

\[
a=10^{-2k},
\qquad
\delta^2=10^{4-2k-4g},
\]

即

\[
\boxed{
\lambda
<
\frac27\,10^{4-2k-4g}
+
\frac{200}{567}\,10^{-2k}.
}
\tag{28}
\]

---

## 6. 两个显式 moving-prefix 空锥

### 6.1 `g\ge1`

若 `g\ge1`，则

\[
\delta^2\le a=10^{-2k}.
\]

由 (27)：

\[
\lambda
<
\left(\frac27+\frac{200}{567}\right)10^{-2k}
=
\frac{362}{567}10^{-2k}
<
\frac23 10^{-2k}.
\tag{29}
\]

又因为 `x=b_2/10^{m_2}\ge1/10` 且由 (22) 有 `1-\lambda>9/10`：

\[
b_1=x\frac{1-\lambda}{\lambda}
>
\frac9{100\lambda}.
\]

结合 (29)：

\[
\boxed{
 b_1>\frac{27}{200}10^{2k}.
}
\tag{30}
\]

由于 `b_1<10^{m_1}`，必有

\[
\boxed{m_1\ge2k.}
\tag{31}
\]

因此最高层中

\[
\boxed{
g\ge1,\quad m_1<2k}
\]

整个区域为空。

### 6.2 `g=0` 的泛型部分

若 `g=0` 且仍处于泛型区域，则必有

\[
k\ge3.
\]

此时

\[
\delta^2=10^{4-2k},
\qquad
a=10^{-2k}=10^{-4}\delta^2.
\]

由 (27) 可粗化为

\[
\boxed{
\lambda<\frac3{10}10^{4-2k}.
}
\tag{32}
\]

于是

\[
b_1
>
\frac9{100\lambda}
>
\frac3{10}10^{2k-4}.
\tag{33}
\]

从 `b_1<10^{m_1}` 得

\[
\boxed{m_1\ge2k-4.}
\tag{34}
\]

所以最高层中

\[
\boxed{g=0,\quad k\ge3,\quad m_1<2k-4}
\]

整个区域为空。

---

## 7. 当前意义

A1 moving-prefix 的位数几何现在进一步变成：

\[
\boxed{
s_1-g\in\{-1,0,1,2\}}
\]

对**所有** A1 候选成立，不再存在低尺度例外。

其中最高层

\[
s_1-g=2
\]

还必须进入非常狭窄的 denominator-position 锥 (28)。特别地：

\[
\boxed{g\ge1\Longrightarrow m_1\ge2k,}
\]

而

\[
\boxed{g=0,\ k\ge3\Longrightarrow m_1\ge2k-4.}
\]

因此后续对最高层无需再研究整个 `(m_1,k)` 平面；只需研究上述两个极窄斜锥以及低尺度 `(g,k)=(0,1),(0,2)` 的 `s_1=2` 切片。

这仍未证明最高层全空，更未证明 A1 全空；它严格排除了最高层中两个无限的大区域，并把所有 A1 候选统一压入四个位数层。
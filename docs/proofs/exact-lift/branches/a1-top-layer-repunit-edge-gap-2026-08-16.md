# A1 top-layer repunit edge gap — 2026-08-16

本文继续 `a1-top-layer-boundary-closure-2026-08-16.md`。

最高层 `s_1=g+2` 的单边取等已经只剩 `g=0` 时的两个 repunit 型边缘族。本文继续证明：这两个边缘都不能紧贴 `2k` 边界继续增长；另一侧至少必须跳到斜率 `3`。

核心结论：

\[
\boxed{
 m_1=2k
\Longrightarrow
 g=0,
\ b_1=10^{2k}-1,
\ a_1=10^{2k+1},
\ n_2\ge3k+1,
}
\]

以及

\[
\boxed{
 n_2=2k
\Longrightarrow
 g=0,
\ a_2=10^{2k}-1,
\ b_2=10^{k-1},
\ m_1\ge3k+1.
}
\]

本文结论均为 **已严格完成**。

---

# 1. 第一 repunit 边缘：先把 `a_1` 偏移压成 0

由前文，若

\[
\boxed{m_1=2k,}
\]

则必有

\[
\boxed{g=0,
\qquad
b_1=10^{2k}-1,
\qquad
n_2\ge2k+1.}
\tag{1}
\]

最高层有

\[
n_1-1=m_1+1=2k+1.
\]

写

\[
\boxed{a_1=10^{2k+1}+e,
\qquad e\ge0.}
\tag{2}
\]

由 decimal normal form：

\[
e
<
\frac{5\cdot10^{-2k}}{1-5\cdot10^{-2k}}
10^{2k+1}
=
\frac{50}{1-5\cdot10^{-2k}}.
\]

因为 `k\ge1`，

\[
\boxed{0\le e\le52.}
\tag{3}
\]

沿用

\[
a=10^{-2k}.
\]

前文在 `m_1=2k` 边界已证明

\[
\lambda<\frac a9,
\qquad
F<\frac{251}{200}a.
\tag{4}
\]

四端点乘积中

\[
\frac{b_1}{10^{m_1}}=1-a,
\qquad
\frac{10^{n_1-1}}{a_1}
=\frac1{1+ea/10}.
\]

其余两个因子均不超过 `1`，所以

\[
t
\le
\frac{1-a}{1+ea/10}.
\tag{5}
\]

如果 `e\ge3`，则

\[
t
\le
\frac{1-a}{1+3a/10}
<1-\frac{129}{100}a.
\]

对 `a\le1/100`，进一步有

\[
\boxed{t^2<1-\frac{64}{25}a.}
\tag{6}
\]

又 `u>1-\lambda`，由 (4)：

\[
u^2>1-\frac29a.
\]

因此

\[
F=u^2-t^2-a
>
\left(
\frac{64}{25}-1-\frac29
\right)a
=
\frac{301}{225}a.
\]

而

\[
\frac{301}{225}>\frac{251}{200},
\]

与 (4) 矛盾。

故

\[
\boxed{e\in\{0,1,2\}.}
\tag{7}
\]

现在使用既约性：

- 若 `e=1`，则
  \[
  a_1=10^{2k+1}+1,
  \qquad
  b_1=10^{2k}-1.
  \]
  因 `10\equiv-1\pmod{11}`，二者都被 `11` 整除；
- 若 `e=2`，因 `10\equiv1\pmod3`，二者都被 `3` 整除。

都与

\[
\gcd(a_1,b_1)=1
\]

冲突。

因此唯一可能是

\[
\boxed{e=0,}
\]

即

\[
\boxed{
 a_1=10^{2k+1}.
}
\tag{8}

---

# 2. 第一边缘的下一层参数

令

\[
\boxed{q=n_2-2k\ge1.}
\tag{9}
\]

由于 `g=0` 且 `s_2=k`，

\[
n_2=m_2+k,
\]

故

\[
\boxed{m_2=k+q.}
\tag{10}
\]

下面证明

\[
1\le q\le k
\]

全部不可能。

记

\[
r=10^{-q}.
\]

若 `q\le k`，decimal normal form 中

\[
0\le e_2
<
\frac{5a}{1-5a}10^{m_2-1}
=
\frac{5}{1-5a}10^{q-k-1}
<1.
\]

所以

\[
\boxed{b_2=10^{m_2-1}.}
\tag{11}
\]

另一方面正 deficit

\[
d_2=10^{n_2}-a_2\ge1
\]

给出

\[
\frac{a_2}{10^{n_2}}
\le1-10^{-n_2}
=1-ar.
\]

而 (1)、(8) 给出另外两个端点因子

\[
\frac{b_1}{10^{m_1}}=1-a,
\qquad
\frac{10^{n_1-1}}{a_1}=1.
\]

因此

\[
\boxed{t\le(1-a)(1-ar).}
\tag{12}
\]

同时

\[
r_1
=\frac{10^{2k+1}}{10^{2k}-1}
=\frac{10}{1-a}.
\]

因为 `r_3<10`，

\[
\boxed{z^2<a(1-a)^2.}
\tag{13}
\]

---

# 3. 第一边缘：`1\le q\le k` 与 contact 冲突

由 (11)：

\[
\lambda
=\frac1{10b_1+1}
=\frac{a}{10-9a}
<\frac a9.
\tag{14}
\]

最高层统一有

\[
1-t<5a.
\]

而 `g=0` 时

\[
u=1-\lambda(1-t),
\]

所以

\[
u^2>1-10\lambda a
>1-\frac{10}{9}a^2.
\tag{15}
\]

由 (12)、(15)：

\[
F
>
1-\frac{10}{9}a^2
-(1-a)^2(1-ar)^2-a.
\tag{16}
\]

减去 (13) 的最大可能第三坐标贡献，得到

\[
F-a(1-a)^2
>
2ar
-\frac{a^2}{9}
-4a^2r
-a^2r^2
-a^3
+2a^3r
+2a^3r^2
-a^4r^2.
\tag{17}
\]

在 `1\le q\le k` 中：

\[
\sqrt a\le r\le\frac1{10},
\qquad a\le\frac1{100}.
\]

把 (17) 中正项丢掉，并逐项除以 `ar`，所有负误差之和小于 `1/2`。因此

\[
\boxed{
F-a(1-a)^2>\frac32 ar.
}
\tag{18}
\]

另一方面

\[
\frac1Q=\frac\lambda{b_2}.
\]

由 (10)–(11)：

\[
\frac1{b_2}
=10^{1-k-q}
=10\sqrt a\,r.
\]

结合 (14)：

\[
\frac1Q
<\frac{10}{9}a^{3/2}r
<\frac19 ar.
\]

于是

\[
c_Q<\frac13 ar.
\]

又

\[
a+t^2+z^2<1+2a<\frac{51}{50},
\]

所以 contact correction 满足

\[
\boxed{
c_Q(a+t^2+z^2)<\frac{17}{50}ar.}
\tag{19}
\]

由 (2)、(13)、(19)：

\[
F-a(1-a)^2<\frac{17}{50}ar,
\]

与 (18) 矛盾。

所以

\[
\boxed{q\ge k+1.}
\]

即

\[
\boxed{
 m_1=2k
\Longrightarrow
n_2\ge3k+1.
}
\tag{20}
\]

---

# 4. 第二 repunit 边缘

前文已经证明，若

\[
\boxed{n_2=2k,}
\]

则

\[
\boxed{
g=0,
\quad a_2=10^{2k}-1,
\quad b_2=10^{k-1},
\quad m_1\ge2k+1.}
\tag{21}
\]

令

\[
\boxed{q=m_1-2k\ge1,}
\qquad
r=10^{-q}.
\tag{22}
\]

下面同样排除 `q\le k`。

写 normal form

\[
b_1=10^{m_1}-d_1,
\qquad d_1\ge1,
\]

\[
a_1=10^{n_1-1}+e_1,
\qquad e_1\ge0.
\]

定义

\[
D_1=\frac{d_1}{10^{m_1}},
\qquad
E_1=\frac{e_1}{10^{n_1-1}}.
\]

由于 `d_1\ge1`：

\[
D_1\ge10^{-m_1}=ar.
\]

令

\[
\boxed{w=\frac{1-D_1}{1+E_1}.}
\]

则

\[
0<w\le1-ar.
\tag{23}
\]

在本边缘，四端点乘积精确化成

\[
\boxed{t=(1-a)w.}
\tag{24}
\]

同时

\[
r_1=10\frac{1+E_1}{1-D_1}=\frac{10}{w}.
\]

因 `r_3<10`：

\[
\boxed{z^2<aw^2\le a(1-ar)^2.}
\tag{25}
\]

---

# 5. 第二边缘：`1\le q\le k` 同样为空

由 `b_2=10^{k-1}`：

\[
\lambda=\frac1{10b_1+1}.
\]

normal form 给出

\[
b_1>(1-5a)10^{m_1}.
\]

所以

\[
\boxed{
\lambda
<
\frac{ar}{10(1-5a)}
<\frac2{19}ar.
}
\tag{26}
\]

仍有

\[
u=1-\lambda(1-t),
\qquad1-t<5a,
\]

故

\[
\boxed{
u^2>1-\frac{20}{19}a^2r.}
\tag{27}
\]

由 (23)–(24)：

\[
t\le(1-a)(1-ar).
\]

将它与 (25)、(27) 代入 defect，可得

\[
F-a(1-ar)^2
>
2ar
-a^2
-\frac{58}{19}a^2r
-a^2r^2
+2a^3r
+a^3r^2
-a^4r^2.
\tag{28}
\]

若 `q\le k`，则仍有

\[
\sqrt a\le r\le\frac1{10}.
\]

丢掉 (28) 中正项后，所有负误差除以 `ar` 的总和小于 `1/2`。因此

\[
\boxed{
F-a(1-ar)^2>\frac32 ar.
}
\tag{29}
\]

另一方面

\[
\frac1Q=\frac\lambda{b_2},
\qquad
\frac1{b_2}=10^{1-k}=10\sqrt a.
\]

由 (26)：

\[
\frac1Q<\frac{20}{19}a^{3/2}r
<\frac2{19}ar.
\]

所以

\[
c_Q<\frac6{19}ar.
\]

再用

\[
a+t^2+z^2<\frac{51}{50},
\]

得到

\[
\boxed{
 c_Q(a+t^2+z^2)<\frac13 ar.
}
\tag{30}
\]

由 contact (2)、(25)、(30)：

\[
F-a(1-ar)^2<\frac13ar,
\]

与 (29) 矛盾。

因此

\[
\boxed{q\ge k+1.}
\]

即

\[
\boxed{
 n_2=2k
\Longrightarrow
m_1\ge3k+1.
}
\tag{31}
\]

---

# 6. 最高层边缘的新形状

所以 `g=0` 时两个唯一边缘族已经进一步变成：

### 第一边缘

\[
\boxed{
 m_1=2k,
\quad b_1=10^{2k}-1,
\quad a_1=10^{2k+1},
\quad n_2\ge3k+1.
}
\]

### 第二边缘

\[
\boxed{
 n_2=2k,
\quad a_2=10^{2k}-1,
\quad b_2=10^{k-1},
\quad m_1\ge3k+1.
}
\]

因此最高层的两条边缘不只不能相交，也不能在距离 `2k` 小于等于 `k` 的区域内存在；它们若仍有候选，只能跃迁到另一方向至少 `3k+1` 的远端。
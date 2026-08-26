# A1 minimal diagonal: dual supply/complement slot shell

> 日期：2026-08-27。依赖 `deep-double-2high-master.md` 与 `deep-2high-normalized-complement-shell.md`。当前统一 frontier `k>=32`。
>
> 本文适用于全部 surviving double-deep 2-high / 5-low master，包括 moderate HL 与原 2-extreme `E_2`。

complement side 已有

\[
R:=2\beta u+\alpha v,
\qquad
f:=5^d,
\qquad
2\beta u-\alpha v=f.
\]

本文在 supply side 定义完全平行的坐标

\[
\boxed{S:=\beta q+5\alpha s,}
\qquad
\boxed{g:=2^cn_0=\beta q-5\alpha s.}
\]

核心结论是：若

\[
y:=R/f,
\qquad z:=S/g,
\]

则存在精确 Möbius 关系

\[
\boxed{
z=\frac{Hy+1}{H+y},
\qquad H:=20b_1+1,}
\tag{1}
\]

并且在当前 `k>=32` frontier 上

\[
\boxed{\lfloor z\rfloor=\lfloor y\rfloor.}
\tag{2}
\]

所以 normalized complement shell 的 finite leading slot

\[
m=\lfloor R/5^d\rfloor
\]

同时也是 supply quotient `S/g` 的 leading slot。写两边 fractional numerators

\[
R=mf+e,
\qquad S=mg+e',
\]

则

\[
\boxed{0<e<f,\qquad0<e'<g,}
\]

且满足 bounded determinant

\[
\boxed{eg-e'f=2r_{10}.}
\tag{3}

最终 four-factor master 可重写成同一个 slot `m` 上的四条正因子式：

\[
\boxed{
\begin{aligned}
4\beta u&=(m+1)f+e,\\
2\alpha v&=(m-1)f+e,\\
2\beta q&=(m+1)g+e',\\
10\alpha s&=(m-1)g+e'.
\end{aligned}}
\tag{4}

状态：**严格完成；这是 full master 的双壳坐标压缩，不单独宣称关闭 A1。**

---

## 1. supply-side sum/difference

master 两条 stripped equations 为

\[
2\beta u-\alpha v=f,
\tag{5}
\]

\[
\beta q-5\alpha s=g.
\tag{6}
\]

定义

\[
R=2\beta u+\alpha v,
\qquad
S=\beta q+5\alpha s.
\]

立即有

\[
R^2-f^2=8r_{10}uv=8r_{10}M,
\tag{7}
\]

\[
S^2-g^2=20r_{10}qs=20r_{10}h.
\tag{8}

另一方面，用

\[
qv-10su=1
\]

直接展开：

\[
\begin{aligned}
Rg-Sf
&=(2\beta u+\alpha v)(\beta q-5\alpha s)\\
&\quad-(\beta q+5\alpha s)(2\beta u-\alpha v)\\
&=2\alpha\beta(qv-10su).
\end{aligned}
\]

所以得到小行列式

\[
\boxed{Rg-Sf=2r_{10}.}
\tag{9}

特别地

\[
y-z=\frac{2r_{10}}{fg}>0.
\tag{10}

因为 (6) 右端正且 `beta q,5alpha s>0`，有

\[
S>g>0,
\]

故

\[
\boxed{y>z>1.}
\tag{11}

---

## 2. decimal source 产生一个 exact hyperbolic identity

令

\[
P:=Qb_1=Mh.
\]

由 (7)-(8)：

\[
(R^2-f^2)(S^2-g^2)
=160r_{10}^2P.
\]

再用 (9)：

\[
(y^2-1)(z^2-1)
=40P(y-z)^2.
\tag{12}

而

\[
Q=10b_1+1.
\]

定义

\[
\boxed{H:=20b_1+1.}
\tag{13}

则

\[
H^2
=400b_1^2+40b_1+1
=1+40b_1(10b_1+1)
=1+40P.
\]

所以 (12) 化为

\[
(y^2-1)(z^2-1)
=(H^2-1)(y-z)^2.
\tag{14}

利用恒等式

\[
(y^2-1)(z^2-1)
=(yz-1)^2-(y-z)^2,
\]

得到

\[
(yz-1)^2=H^2(y-z)^2.
\]

由 (11) 两边均正，故只能取正号：

\[
\boxed{yz-1=H(y-z).}
\tag{15}

解出 `z`：

\[
\boxed{z=\frac{Hy+1}{H+y}.}
\tag{16}

并且

\[
\boxed{y-z=\frac{y^2-1}{H+y}.}
\tag{17}

这就是 dual-shell Möbius relation。

---

## 3. exact integral reconstruction of the supply scale

把

\[
y=R/f
\]

代入 (16)。另一方面由 (7)

\[
y^2-1=\frac{8r_{10}M}{f^2},
\]

再和 (10)、(17) 比较：

\[
\frac{8r_{10}M/f^2}{H+R/f}
=\frac{2r_{10}}{fg}.
\]

消去 `2r10` 后得到

\[
\boxed{4Mg=Hf+R.}
\tag{18}

因此

\[
\boxed{g=\frac{Hf+R}{4M}.}
\tag{19}

再乘 (16)：

\[
\boxed{S=\frac{HR+f}{4M}.}
\tag{20}

所以 complement data `(f,R,M)` 会精确恢复 supply sum/difference `(g,S)`。

---

## 4. 两个 normalized quotients 必须具有同一个 floor

已有 full-master shell

\[
3780<y<78015.
\]

而

\[
H=20b_1+1
=200T^2-20w+1
>199T^2.
\]

又 double-deep 有 `Y>=1`，所以

\[
d=k+1-Y\le k,
\qquad
f=5^d<10^k=T.
\]

由 (17)：

\[
0<y-z
<\frac{78015^2}{199T^2}.
\]

当前 `k>=32`，特别有

\[
78015^2T<199T^2,
\]

故

\[
\boxed{0<y-z<1/T<1/f.}
\tag{21}

另一方面，从

\[
R-f=2\alpha v
\]

以及 `(alpha v,5)=1` 得

\[
5\nmid R.
\]

所以 `R/f` 绝不为整数。令

\[
m:=\lfloor y\rfloor.
\]

则存在整数

\[
1\le e\le f-1
\]

使

\[
y=m+e/f.
\]

因此

\[
y-m\ge1/f.
\]

结合 (21)：

\[
z>y-1/f\ge m,
\qquad
z<y<m+1.
\]

第一处实际为严格 `z>m`，故

\[
\boxed{m<z<m+1.}
\]

于是主结论：

\[
\boxed{\lfloor S/g\rfloor=\lfloor R/f\rfloor=m.}
\tag{22}

---

## 5. 双 fractional numerators

由 (22)，存在唯一整数

\[
\boxed{0<e<f,\qquad0<e'<g}
\tag{23}

使

\[
\boxed{R=mf+e,}
\qquad
\boxed{S=mg+e'.}
\tag{24}

把 (24) 代入小行列式 (9)：

\[
(mf+e)g-(mg+e')f=2r_{10},
\]

所以

\[
\boxed{eg-e'f=2r_{10}.}
\tag{25}

这说明两个 fractional parts

\[
e/f,\qquad e'/g
\]

之间的 cross determinant 是绝对有限 coefficient `2r10`。

---

## 6. symmetric four-factor slot equations

complement side：

\[
R+f=4\beta u,
\qquad
R-f=2\alpha v.
\]

代入 (24)：

\[
\boxed{4\beta u=(m+1)f+e,}
\tag{26}

\[
\boxed{2\alpha v=(m-1)f+e.}
\tag{27}

supply side：

\[
S+g=2\beta q,
\qquad
S-g=10\alpha s.
\]

所以

\[
\boxed{2\beta q=(m+1)g+e',}
\tag{28}

\[
\boxed{10\alpha s=(m-1)g+e'.}
\tag{29}

四式共享完全相同的 leading coefficients `(m+1,m-1)`。

因此 full 2-high master 可以组织成 finite leading slot `m` + two reduced fractions

\[
\boxed{
\frac ef-\frac{e'}g
=\frac{2r_{10}}{fg}.}
\tag{30}

---

## 7. immediate exact congruence interface

由 (26)-(27)：

\[
\boxed{
e\equiv-(m+1)f\pmod{4\beta},}
\tag{31}

\[
\boxed{
e\equiv-(m-1)f\pmod{2\alpha}.}
\tag{32}

这正是 old `R` CRT ray 在 fixed slot 中的 fractional form。

supply side 同理：

\[
\boxed{
e'\equiv-(m+1)g\pmod{2\beta},}
\tag{33}

\[
\boxed{
e'\equiv-(m-1)g\pmod{10\alpha}.}
\tag{34}

因为

\[
\gcd(2\beta,10\alpha)=2,
\]

它们对 fixed `(alpha,beta,m,g)` 给出一个模 `10r10` 的 unique compatible supply residue class。

再结合 (25)，可以选择从 `(f,e)` 或 `(g,e')` 任一侧恢复另一侧。

---

## 8. 后续用途

新的 certificate coordinate 可以写成

\[
\boxed{(w,\xi,\alpha,\beta,m; f,e,g,e')}
\]

其中：

- `m` 已被 contact/remainder coupling 大幅压缩；
- `(f,e)` 受 complement CRT 与 decimal divisor sources 控制；
- `(g,e')` 受 supply CRT、Q-side contact-square lifting 控制；
- 两边只能通过小行列式 `eg-e'f=2r10` 耦合。

这提供了一个比只保留 `(d,R)` 更对称的接口，尤其适合把现有 Q-side square-block lifting真正接到 finite `m` shell 上。

---

## 9. dependency audit

Möbius relation (16) 来自 four-factor determinant与 decimal identity `Q=10b1+1`，因此它属于现有 master skeleton 的精确重写。

真正新增的可用信息是当前大尺度 `H~200T^2` 与 finite shell `y<78015` 联立后得到的 same-floor theorem (22)：supply 与 complement 在当前 frontier 必须共享**同一个整数 leading slot**。后续证书可据此只维护一个 `m`，无需给 supply side 再引入独立无界 quotient。
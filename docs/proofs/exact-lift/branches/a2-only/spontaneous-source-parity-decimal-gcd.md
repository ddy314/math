# A2 source parity common gcd 的 fully-decimal realization

> **依赖：** `spontaneous-source-parity-common-gcd.md`、`spontaneous-height-equal-depth-decimal-tropical-identity.md`、`source-discriminant.md`。
>
> **严格状态：**source common gcd `G_S=gcd(B_W,D_W/2)` 原先仍使用 `z,c_u`。本文利用 exact source ratio把 `D_W` 与已有 `B_dec` 同时乘回真实 decimal denominator plane，得到 `D_dec=55T^2Q^2-49b_3^2`。二者具有完全相同的 square scale `(b_3/c_u)^2`，所以对 `B_dec,D_dec/2` 取 ordinary gcd后再约掉，精确恢复 source coprime residuals `B_S,D_S`。source parity doubling因此可完全从原 decimal integers读取。并且 `D_dec` 只有 `2m+2M+3` 位、`B_dec` 只有 `2m+4M+3` 位。本文是 canonicalization，不关闭 A2。

---

## 1. decimal source discriminant

source ratio为

\[
\boxed{b_3z=Tc_uQ.}
\tag{1.1}

source discriminant

\[
\mathscr D_W=55z^2-49c_u^2.
\]

定义 pure-decimal integer

\[
\boxed{
D_{\rm dec}:=55T^2Q^2-49b_3^2.}
\tag{1.2}

由 (1.1)：

\[
b_3^2z^2=T^2c_u^2Q^2,
\]
所以

\[
\boxed{
b_3^2\mathscr D_W=c_u^2D_{\rm dec}.}
\tag{1.3}

当前 source geometry给 `D_W>0`，故

\[
\boxed{D_{\rm dec}>0.}
\tag{1.4}

---

## 2. common square scale

已有 decimal height reader

\[
\boxed{
b_3^2\mathscr B_W=c_u^2B_{\rm dec},}
\tag{2.1}

其中

\[
B_{\rm dec}
=b_3^2(5K^2-36K+55)+T^2Q^2K^2.
\]

endpoint denominator formula含 `c_u` 为因子，因此

\[
\boxed{L:=b_3/c_u\in\mathbb Z_{>0}.}
\tag{2.2}

由 (1.3),(2.1)：

\[
\boxed{D_{\rm dec}=L^2\mathscr D_W,}
\tag{2.3}

\[
\boxed{B_{\rm dec}=L^2\mathscr B_W.}
\tag{2.4}

两个 source carriers乘回 decimal plane时获得的是**完全相同的 square scale**。

---

## 3. fully-decimal common gcd

定义

\[
\boxed{
G_{\rm src}^{\rm dec}
:=\gcd\!\left(B_{\rm dec},\frac{D_{\rm dec}}2\right).}
\tag{3.1}

因为 `D_W/2` 为整数且 (2.3),(2.4)：

\[
\begin{aligned}
G_{\rm src}^{\rm dec}
&=\gcd\left(L^2B_W,L^2D_W/2\right)\\
&=L^2\gcd(B_W,D_W/2).
\end{aligned}
\]

所以

\[
\boxed{G_{\rm src}^{\rm dec}=L^2G_S.}
\tag{3.2}

定义 decimal residuals

\[
\boxed{
B_{\rm src}^\circ
:=\frac{B_{\rm dec}}{G_{\rm src}^{\rm dec}},}
\tag{3.3}

\[
\boxed{
D_{\rm src}^\circ
:=\frac{D_{\rm dec}}{2G_{\rm src}^{\rm dec}}.}
\tag{3.4}

则 square scale完全消失：

\[
\boxed{B_{\rm src}^\circ=B_S,}
\tag{3.5}

\[
\boxed{D_{\rm src}^\circ=D_S.}
\tag{3.6}

因此

\[
\boxed{\gcd(B_{\rm src}^\circ,D_{\rm src}^\circ)=1.}
\tag{3.7}

这给 source parity residuals 一个不再依赖 source variables的 ordinary decimal-gcd定义。

---

## 4. parity is readable directly from decimal quotients

source common-gcd theorem已有

\[
B_S\equiv D_S\pmod4,
\]
且两者只能同时为 `1` 或同时为 `3 mod4`。

由 (3.5),(3.6)：

\[
\boxed{
B_{\rm src}^\circ
\equiv D_{\rm src}^\circ\pmod4.}
\tag{4.1}

所以不必显式恢复 `L` 或 `G_S`：直接计算两个 pure-decimal gcd quotients即可判断 source parity allocation。

若

\[
\boxed{B_{\rm src}^\circ\equiv D_{\rm src}^\circ\equiv3\pmod4,}
\tag{4.2}

则它们 positive、odd、coprime，各自必须携带一份 odd inert parity，且 suppliers不同。

若

\[
\boxed{B_{\rm src}^\circ\equiv D_{\rm src}^\circ\equiv1\pmod4,}
\tag{4.3}

则 source residual pair不再强迫新增 inert supplier；parity已被完整 common gcd吸收。

---

## 5. short window for `D_dec`

写

\[
q:=Q/N,
\qquad w:=b_3/T.
\]

则

\[
\frac{D_{\rm dec}}{T^2N^2}
=55q^2-49\frac{w^2}{N^2}.
\tag{5.1}

endpoint给

\[
\frac{21}{10}<q<\frac{40}{19},
\qquad
0<w<\frac{843}{1000},
\qquad N\ge10^{11}.
\]

因此

\[
55\left(\frac{21}{10}\right)^2
-49\left(\frac{843}{1000\cdot10^{11}}\right)^2
>242,
\]

以及

\[
55\left(\frac{40}{19}\right)^2<244.
\]

所以

\[
\boxed{242T^2N^2<D_{\rm dec}<244T^2N^2.}
\tag{5.2}

特别地

\[
\boxed{D_{\rm dec}\text{ 恰有 }2m+2M+3\text{ 位}.}
\tag{5.3}

---

## 6. short window for `B_dec`

由定义

\[
\frac{B_{\rm dec}}{T^2N^4}
=
\frac{w^2}{N^2}
\left(5s^2-\frac{36s}{N}+\frac{55}{N^2}\right)
+q^2s^2,
\tag{6.1}

其中

\[
s:=K/N,
\qquad
\frac{2499}{250}<s<10.
\]

第一项非负。故

\[
\frac{B_{\rm dec}}{T^2N^4}
>
\left(\frac{21}{10}\right)^2
\left(\frac{2499}{250}\right)^2
>440.
\]

上界使用 `q<40/19,s<10,w<843/1000,N>=10^11`：

\[
\frac{B_{\rm dec}}{T^2N^4}
<
100\left(\frac{40}{19}\right)^2
+\frac1{10^{22}}
\left(\frac{843}{1000}\right)^2
\left(500+\frac{55}{10^{22}}\right)
<444.
\]

所以

\[
\boxed{440T^2N^4<B_{\rm dec}<444T^2N^4.}
\tag{6.2}

并且

\[
\boxed{B_{\rm dec}\text{ 恰有 }2m+4M+3\text{ 位}.}
\tag{6.3}

---

## 7. source parity now lives on two natural decimal scales

source residual parity的两个 parent carriers现在分别只有

\[
D_{\rm dec}\asymp T^2N^2,
\]

\[
B_{\rm dec}\asymp T^2N^4.
\]

其中较短的 `D_dec` 比 `B_dec` 少整整 `2M` 个 decimal digits。两者共享的巨大 denominator/source scale由 ordinary gcd `G_src^dec` 自动删掉。

因此后续 global source parity budget不必再回 `z,c_u,B_W,D_W`：可直接在

\[
\boxed{B_{\rm src}^\circ,D_{\rm src}^\circ}
\]
这两个 pure-decimal coprime integers上工作。

A2 仍为 `待证`。

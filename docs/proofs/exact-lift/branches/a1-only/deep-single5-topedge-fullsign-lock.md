# A1 minimal diagonal: single-5 top-edge full-sign 5-adic complement lock

> 日期：2026-08-22。
>
> 依赖：`deep-single5-decimal-height-collapse.md`、`deep-single5-topedge-common-quotient.md`、`diagonal.md`。
>
> 范围：minimal diagonal `k=g>=32` 的 single-5 top edge，并假设 surviving 2-adic high sign 在 5-adic 一侧取 §3.2 的 **full sign**。

状态：**本文各结论均已严格完成；full-sign branch 尚未整体关闭。**

---

## 1. full-sign 的 decimal height

记

\[
n_5:=v_5(N),
\qquad
m:=n_5-B>0.
\tag{1}
\]

`deep-single5-decimal-height-collapse.md` 对 full sign 给

\[
d_5=B+2k.
\]

因为 `B>k`，这严格大于 `B+k`，所以 decimal-height synchronization 强迫

\[
\boxed{n=B+2k.}
\tag{2}

由 `deep-single5-topedge-common-quotient.md`：

\[
L=5^{B+k},
\qquad M=2^{k-1}h.
\]

因此实际第三分母的 5-adic depth 为

\[
\boxed{v_5(b_3)=n-(B+k)=k.}
\tag{3}

---

## 2. sphere common quotient 的 5-depth

令

\[
\mathfrak q=\operatorname{lcm}(b_1,b_2,b_3),
\qquad
S=y_1^2+y_2^2.
\]

minimal diagonal 中 `b2=1`，且 `b1` 为 5-unit。由 (3)：

\[
v_5(\mathfrak q)=k.
\]

又

\[
S=\left(\frac{\mathfrak q}{b_1}\right)^2N,
\]

所以

\[
\boxed{v_5(S)=2k+n_5.}
\tag{4}

因为 `5|b3`，第三分数既约给 `5∤a3`，从而 `y3` 是 5-unit。另一方面

\[
U=H-y_3=LA
\]

被 5 整除，故 `H≡y3 mod5`，于是

\[
H+y_3\equiv2y_3\not\equiv0\pmod5.
\]

球面分解

\[
U(H+y_3)=S
\]

因此给出

\[
B+k+v_5(A)=2k+n_5.
\]

即

\[
\boxed{v_5(A)=k+n_5-B=k+m.}
\tag{5}

由于 `M=2^(k-1)h` 为 5-unit：

\[
\boxed{v_5(\mathcal T)=k+m.}
\tag{6}

---

## 3. diagonal carrier gap 的固定 5-adic residue

`diagonal.md` 中

\[
\Delta=5b_1+J,
\]

\[
J=(5-z)w+Tj,
\qquad T=10^k.
\]

代入

\[
b_1=10T^2-w
\]

得到 exact identity

\[
\boxed{
\Delta=50T^2-zw+Tj.}
\tag{7}

因此

\[
\boxed{
\Delta\equiv-zw\pmod{5^k}.}
\tag{8}

特别地 `zw` 为 5-unit，所以

\[
\boxed{v_5(\Delta)=0.}
\tag{9}

---

## 4. full-sign 强迫 Q-complement 落入增长的 5-adic residue class

minimal diagonal safe recovery identity 为

\[
\mathcal T
=10^kQ\Delta-10^{2k}y_1+y_2.
\tag{10}

由 (6)，除以 `5^k` 后，左侧被 `5^m` 整除。

令

\[
m_0:=\min(m,k).
\tag{11}

模 `5^m0`：

- 第二项 `10^(2k)y1/5^k` 仍被 `5^k` 整除，因此消失；
- 第一项变成 `2^k Q Delta`；
- 由 (3) 可把 lcm 精确写成
  \[
  \mathfrak q
  =2^{n+k-1}5^kqsu,
  \]
  其中本文 `b1=2^e s u` 且 `u` 为 odd complement。

所以

\[
\frac{y_2}{5^k}
=a_2\,2^{n+k-1}qsu
=a_2\,2^{n+k-1-e}q b_1.
\tag{12}

在模 `5^m0` 下，由 `m0<=k`：

\[
a_2=10T^2-z\equiv-z,
\]

\[
b_1=10T^2-w\equiv-w,
\]

以及 (8)

\[
\Delta\equiv-zw.
\]

故 (10) 除 `5^k` 后的 `5^m0` 整除条件给

\[
-zw\,2^kQ
+zw\,2^{n+k-1-e}q
\equiv0
\pmod{5^{m_0}}.
\]

约去 units `zw,2^k,q`，并使用 `Q=qv`：

\[
\boxed{
 v\equiv2^{n-1-e}
 \pmod{5^{m_0}}.}
\tag{13}

结合 (2)：

\[
\boxed{
 v\equiv2^{B+2k-1-e}
 \pmod{5^{\min(n_5-B,k)}}.}
\tag{14}

这是 full-sign 的增长 5-adic complement lock。

top-edge 另有独立的 2-adic orientation

\[
\boxed{v\equiv3\pmod4.}
\tag{15}

所以 full-sign Q-complement 必须同时满足 (14)-(15)。

---

## 5. 一个新的 `b1`-coefficient resultant

minimal diagonal 的显式第一分子可写成

\[
a_1
=100T^3+igl(10(5-z-w)+1\bigr)T+N_0-1.
\tag{16}

又

\[
C=10T^2a_1+a_2,
\qquad b_1=10T^2-w.
\]

模 `b1` 有 `10T^2≡w`，并由 (16)

\[
a_1
\equiv(51-10z)T+N_0-1
\pmod{b_1}.
\]

因此

\[
\boxed{
C\equiv
E_b:=wN_0+w(51-10z)T-z
\pmod{b_1}.}
\tag{17}

于是

\[
\boxed{
\gcd(b_1,C)\mid E_b.}
\tag{18}

六类型中：

- `z=1` 时 `E_b<42wT<=168T`；
- `z=3` 时只出现 `w=1,2`，且 `E_b<22wT<=44T`。

故统一有

\[
\boxed{
\gcd(b_1,C)<168T.}
\tag{19}

这与已有

\[
\gcd(Q,C)<1599T
\]

形成两侧同时的 `O(T)` exceptional-coefficient bound。

---

## 6. consequence

full-sign branch 现在必须同时满足：

\[
\boxed{
\begin{gathered}
n=B+2k,\qquad n_5>B,\\
v_5(A)=k+n_5-B,\\
v\equiv2^{B+2k-1-e}
\pmod{5^{\min(n_5-B,k)}},\\
v\equiv3\pmod4,\\
\gcd(b_1,C)<168T,\qquad
\gcd(Q,C)<1599T.
\end{gathered}}
\]

本文只记录这些为严格必要条件；尚未由它们单独推出 full-sign 为空。
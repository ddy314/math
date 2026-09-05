# A1 minimal diagonal: single-5 top-edge full-sign audit and coefficient resultant

> 日期：2026-08-22。
>
> 依赖：`deep-single5-decimal-height-collapse.md`、`deep-single5-topedge-common-quotient.md`、`diagonal.md`。
>
> 范围：minimal diagonal `k=g>=32` 的 single-5 top edge，并假设真实负号根在 5-adic 一侧取 §3.2 的 **full sign**。

状态：**§§1--2 与 §4 的结论严格成立。旧版把两个不同的 `Delta` 误作同一对象；由此得到的 Q-complement 5-adic residue 已撤回，不能再作为证明输入。full-sign branch 尚未整体关闭。**

---

## 0. 记号审计：两个 `Delta` 必须区分

本项目中此前两个来源都使用过 `Delta`，但含义不同。

1. safe sphere recovery 中的整数球面 gap：
   \[
   \boxed{\Delta_H:=10^k y_1-H.}
   \]
   `deep-single5-topedge-common-quotient.md` 中的
   \[
   \mathcal T
   =10^kQ\Delta_H-10^{2k}y_1+y_2
   \]
   使用的是这个对象。

2. `diagonal.md` 中前两有理块的 determinant gap：
   \[
   \boxed{\Delta_{12}:=10^ka_1b_2-a_2b_1}
   \]
   （当前 `b2=1`），它满足
   \[
   \Delta_{12}=5b_1+J
   \]
   以及固定的十进制 residue。

两者没有被证明相等。旧版 §3--§4 将 `Delta_H` 直接替换为 `Delta_12`，因此那一段推导无效。

特别地，旧版曾声称

\[
v\equiv2^{B+2k-1-e}
\pmod{5^{\min(n_5-B,k)}}.
\]

**该式现已撤回。** 后续证明不得引用它。

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
\]

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
\]

因为 `5|b3`，第三分数既约给 `5\nmid a3`，从而 `y3` 是 5-unit。另一方面

\[
U=H-y_3=LA
\]

被 5 整除，故 `H\equiv y3 mod 5`，于是

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
\]

由于 `M=2^(k-1)h` 为 5-unit：

\[
\boxed{v_5(\mathcal T)=k+m.}
\tag{6}

这部分只使用 sphere common quotient，不依赖被撤回的 `Delta` 识别。

---

## 3. 被撤回的 5-adic residue 路线

`diagonal.md` 对 determinant gap 确实有严格恒等式

\[
\Delta_{12}=50T^2-zw+Tj,
\]

因此

\[
\Delta_{12}\equiv-zw\pmod{5^k}.
\]

但是 safe recovery 中出现的是 `Delta_H=10^ky1-H`。在没有额外桥梁证明

\[
\Delta_H\equiv\Delta_{12}\pmod{5^r}
\]

之前，不能把上述 residue 代入 `mathcal T`。

因此旧版基于这一替换得到的 full-sign `v mod 5^m` lock 已删除。

---

## 4. 独立有效的 `b1`-coefficient resultant

下面的结论与两个 gap 无关，仍然严格有效。

minimal diagonal 的显式第一分子可写成

\[
a_1
=100T^3+\bigl(10(5-z-w)+1\bigr)T+N_0-1.
\tag{7}

又

\[
C=10T^2a_1+a_2,
\qquad b_1=10T^2-w.
\]

模 `b1` 有 `10T^2\equiv w`，并由 (7)

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
\tag{8}

于是

\[
\boxed{
\gcd(b_1,C)\mid E_b.}
\tag{9}

六类型中：

- `z=1` 时 `E_b<42wT<=168T`；
- `z=3` 时只出现 `w=1,2`，且 `E_b<22wT<=44T`。

故统一有

\[
\boxed{
\gcd(b_1,C)<168T.}
\tag{10}

这与已有

\[
\gcd(Q,C)<1599T
\]

形成两侧同时的 `O(T)` coefficient-exception bound。

---

## 5. 当前保留的 full-sign 输入

修正后，full-sign branch 可安全使用的本文结论只有

\[
\boxed{
\begin{gathered}
n=B+2k,\qquad n_5>B,\\
v_5(A)=k+n_5-B,\\
\gcd(b_1,C)<168T,\qquad
\gcd(Q,C)<1599T.
\end{gathered}}
\]

此外仍可独立使用 `deep-single5-topedge-supply-compression.md` 的

\[
v\equiv3\pmod4,
\]

因为那条结论只来自 2-adic high-sign synchronization，与本文件撤回的 5-adic residue 无关。

full-sign 尚未关闭。
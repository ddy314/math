# A2 descent singular gate `F_1270` 的 prime-source audit

> **依赖：** `spontaneous-crt-descent-overlap-nogo.md`、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-source-target-support-separation.md`、`spontaneous-height-equal-depth-dual-short-carriers.md`。
>
> **严格状态：**`Rstar_63/D_63` overlap 的 ordinary resultant审计只留下 pure-prefix singular gate `F_1270=1270B^2-Q^2N_0` 与 third-central gate。本文专门审计 `F_1270`。与 original carrier `That_2` 联立后，`F_1270` 自动产生一个 third/prefix quadratic `G_1270`。该 quadratic与 central/source-common/omega/height/target carriers的 resultants全部显式且短。特别地，若 `F_1270` overlap同时属于 equal-depth target，则 moving prime被压成 fixed set `{7,79,107,199}`；四个 common third-block roots均为 first-layer transverse collision，不产生新的双深 Hensel tree。本文没有排除这四个 fixed primes及 generic external `F_1270` roots，因此不关闭 A2。

---

## 1. positive form and primitive orientation of the pure-prefix gate

定义 singular factor

\[
\boxed{
F_{1270}:=1270B^2-Q^2N_0.}
\tag{1.1}
\]

真实 endpoint中更自然使用正整数

\[
\boxed{
H_{1270}:=-F_{1270}=Q^2N_0-1270B^2.}
\tag{1.2}
\]

利用

\[
x=B/N,\qquad y=10A/N,
\]

\[
\frac{N_0}{N^2}=rac{2025x^2+y^2}{100},
\]
有

\[
\frac{H_{1270}}{N^4}
=
\frac{(x+2)^2(2025x^2+y^2)}{100}
-rac{1270x^2}{N^2}.
\tag{1.3}
\]

endpoint box与 `N>=10^11` 给安全窗口

\[
\boxed{
\frac{117}{125}N^4
<H_{1270}
<\frac{26}{25}N^4.}
\tag{1.4}
\]

所以 `F_1270` 在实数上远离零；它只可能作为 p-adic singular gate出现。

二进结构也固定。`Q=2^{M+1}Q_0`、`N_0` odd，而 `1270B^2` 比 `Q^2N_0` 多至少 `2m+1` 层二进深度。因此

\[
\boxed{
v_2(H_{1270})=2M+2,}
\tag{1.5}
\]

\[
\boxed{
\frac{H_{1270}}{2^{2M+2}}
\equiv Q_0^2N_0
\equiv1\pmod8.}
\tag{1.6}
\]

所以 `H_1270` 本身是 positive `1 mod8` primitive carrier；它不额外强迫 odd-inert parity。

---

## 2. intersection with the original forced carrier gives `G_1270`

令

\[
U:=2^{M+1}.
\]

由 denominator normal forms可把 original primitive additive carrier写成 exact identity

\[
\boxed{
U^2 2^m\widehat{\mathcal T}_2
=
B^2F_0-TQ^2N_0,}
\tag{2.1}
\]

其中

\[
\boxed{
F_0
:=TK^2-(18T+4a_3)K+18a_3+55T.}
\tag{2.2}
\]

固定 genuine odd prime `p`，并假设

\[
p\mid\widehat{\mathcal T}_2,
\qquad
p\mid F_{1270}.
\tag{2.3}
\]

`gcd(That_2,10c_ug)=1`，而 `B=2^{M+m+1}c_ug`，所以

\[
\boxed{p\nmid B.}
\tag{2.4}
\]

由 `F_1270=0`：

\[
Q^2N_0\equiv1270B^2\pmod p.
\]

代入 (2.1) 并消去 `B^2`：

\[
\boxed{
G_{1270}
:=TK^2-(18T+4a_3)K+18a_3-1215T
\equiv0\pmod p.}
\tag{2.5}
\]

等价地

\[
\boxed{
G_{1270}
=T(K^2-18K-1215)-2a_3(2K-9).}
\tag{2.6}
\]

所以 noncentral `F_1270` overlap会唯一同步 `a_3/T` 的 projective unit；central branch需要单列。

---

## 3. central overlap collapses to fixed `7`

直接对 `K` 求 resultant：

\[
\boxed{
\operatorname{Res}_K(G_{1270},2K-9)
=-5103T
=-3^6\cdot7\,T.}
\tag{3.1}
\]

在 genuine non-`3` sector，`p∤T`，因此

\[
\boxed{
p\mid G_{1270},\quad p\mid2K-9
\Longrightarrow p=7.}
\tag{3.2}
\]

所以 `F_1270` singular overlap若再次进入 central additive sheet，不存在 moving prime；只剩 fixed `7`。

---

## 4. source-common overlap pays a short third-block linear carrier

source-common moving support进入

\[
18K-55.
\]

resultant为

\[
\boxed{
\operatorname{Res}_K(G_{1270},18K-55)
=1872a_3-408455T.}
\tag{4.1}
\]

定义 positive carrier

\[
\boxed{
L_{1270}^{src}
:=408455T-1872a_3.}
\tag{4.2}
\]

由

\[
1<a_3/T<251/250
\]
得到

\[
\boxed{
406575T<L_{1270}^{src}<406583T.}
\tag{4.3}
\]

因此任何 source-common prime若同时进入 `F_1270` singular overlap，其 prime depth至少需要在这个只有 `m+6` 位量级的 third-block linear integer中重新出现。

---

## 5. omega-content overlap produces a new fixed-`79` third carrier

若

\[
p\mid\omega,
\]
则

\[
\alpha=TK+a_3\equiv0\pmod p.
\]

resultant：

\[
\operatorname{Res}_K(G_{1270},TK+a_3)
=T(-1215T^2+36Ta_3+5a_3^2).
\]

定义 positive odd carrier

\[
\boxed{
H_{79}:=1215T^2-36Ta_3-5a_3^2.}
\tag{5.1}
\]

则 genuine omega-overlap满足

\[
\boxed{p\mid H_{79}.}
\tag{5.2}
\]

endpoint window给

\[
\boxed{
1173T^2<H_{79}<1174T^2.}
\tag{5.3}
\]

`T` 为偶、`a_3` odd，因此

\[
\boxed{H_{79}\equiv3\pmod4.}
\tag{5.4}
\]

把 `H_79` 看成关于 `a_3` 的 quadratic，其 discriminant为

\[
\boxed{
\operatorname{Disc}_{a_3}(H_{79})
=25596T^2
=18^2\cdot79\,T^2.}
\tag{5.5}
\]

所以对 genuine inert prime `p≡3 mod4`、`p∤2\cdot3\cdot79T`：

\[
\boxed{p\mid H_{79}\Longrightarrow(79/p)=1.}
\tag{5.6}
\]

因为 `79≡3 mod4`，quadratic reciprocity给

\[
\boxed{(p/79)=-1.}
\tag{5.7}
\]

这是 `F_1270` omega-content overlap的 fixed-79 orientation。仓库此前没有使用该 `79` character；本文暂不宣称它与其它 character独立到足以闭环。

---

## 6. `q/W_q` support pays a short source-defect carrier

任意 prime若进入 `qW_q` support，则

\[
DK-(3D-C)\equiv0\pmod p.
\]

对 `K` 消元：

\[
\boxed{
\begin{aligned}
\operatorname{Res}_K(
G_{1270},DK-(3D-C))
={}&C^2T+12CDT+4CDa_3\\
&-1260D^2T+6D^2a_3.
\end{aligned}}
\tag{6.1}
\]

定义其正相反数

\[
\boxed{
L_{1270}^{H}
:=1260D^2T-6D^2a_3
-12CDT-4CDa_3-C^2T.}
\tag{6.2}
\]

写 `delta=C/D`、`zeta=a_3/T`：

\[
\frac{L_{1270}^{H}}{D^2T}
=1260-6\zeta-(12+4\zeta)\delta-\delta^2.
\]

由

\[
0<\delta<3/250,
\qquad1<\zeta<251/250
\]
得到

\[
\boxed{
1253D^2T<L_{1270}^{H}<1254D^2T.}
\tag{6.3}
\]

所以 `q` denominator / `W_q` height overlap也不能自由复用；必须进入一个显式 short source-defect natural representative。

---

## 7. equal-depth target overlap collapses to four fixed primes

真正 equal-depth target同时满足

\[
p\mid\omega
\]
和 third short carrier

\[
p\mid R_3,
\qquad
R_3=6(a_3+3T)^2+T^2.
\]

由 §5 同时有 `p|H_79`。直接 resultant：

\[
\boxed{
\operatorname{Res}_{a_3}(H_{79},R_3)
=58875145T^4
=5\cdot7\cdot79\cdot107\cdot199\,T^4.}
\tag{7.1}
\]

在 genuine non-`5` target sector：

\[
\boxed{
F_{1270}\text{ singular overlap}
+\text{equal-depth target}
\Longrightarrow
p\in\{7,79,107,199\}.}
\tag{7.2}
\]

所以这部分 moving target support完全消失，只剩四个 fixed primes。

逐 prime把 `T` 归一为 `1`，并同时施加

\[
H_{79}=R_3=0,
\qquad
P(K)=6K^2-36K+55=0,
\qquad
G_{1270}=0
\]
得到唯一 first-layer state：

\[
\boxed{
\begin{array}{c|c|c}
p&a_3/T\pmod p&K\pmod p\\ \hline
7&5&2\\
79&28&51\\
107&11&96\\
199&83&116
\end{array}}
\tag{7.3}
\]

`p=7,K=2` 正好与已经存在的 fixed-7 equal-depth target orbit对齐。

---

## 8. the four target collisions are only first-layer transverse

(7.1) 中每个 genuine candidate prime `7,79,107,199` 的 exponent都恰为 `1`。

resultant的 Bezout identity因此说明：若同一 candidate上

\[
p^2\mid H_{79},
\qquad
p^2\mid R_3,
\]
则会迫使 `p^2` 整除 (7.1) 的右边，矛盾。

因此

\[
\boxed{
\min\{v_p(H_{79}),v_p(R_3)\}=1
\qquad
(p\in\{7,79,107,199\}).}
\tag{8.1}
\]

特别地，若 target baseline `h=v_p(R_3)>=2`，则

\[
\boxed{v_p(H_{79})=1.}
\tag{8.2}
\]

所以 `F_1270` 与 equal-depth target的 fixed collision不会形成一个新的双深/奇异 Hensel tree。

---

## 9. target-resultant character is only the old `sqrt(-6)` shadow

直接消去 `K`：

\[
\boxed{
\operatorname{Res}_K(G_{1270},P(K))
=57169585T^2-543816Ta_3+1392a_3^2.}
\tag{9.1}
\]

记右边为 `H_6`。endpoint中

\[
56624000T^2<H_6<56628000T^2.
\]

其 discriminant为

\[
\boxed{
\operatorname{Disc}_{a_3}(H_6)
=-22584407424T^2
=-6(61352T)^2.}
\tag{9.2}
\]

所以 ordinary quadratic character只重复 target quadratic `P(K)` 已有的 `sqrt(-6)` orientation；不能把 (9.1) 再当一条 independent Legendre obstruction收费。

真正新的 target信息是 §7 的 fixed-prime collapse，而不是这个 discriminant。

---

## 10. revised singular frontier

`F_1270` singular sheet现在按已有 prime-source分成：

1. central `2K-9` overlap：只剩 fixed `7`；
2. source-common `18K-55` overlap：进入 short linear `L_1270^src`；
3. omega-content overlap：进入 positive `3 mod4` short carrier `H_79`，并获得 fixed-79 orientation；
4. q/height support：进入 short `L_1270^H`；
5. equal-depth target：moving support完全缩成 fixed `{7,79,107,199}`，且共同 third depth横截。

因此 `F_1270` 仍可能有 generic external simple roots，但它与已经昂贵/已分类的 prime pools的交集都已大幅缩窄。

下一步最值得做的是审计 fully primitive short remainder `Rstar_63` 的 forced inert prime能否属于 generic external `F_1270` root；若不能，original/remainder parity就必须真正分裂为不同 primes。

A2 仍为 `待证`。

# A1 minimal diagonal: single-5 low-edge sphere lock

> 日期：2026-08-22。
>
> 依赖：`deep-single5-decimal-height-collapse.md`、`rational-contact.md` 的 safe integer-gap recovery、minimal-diagonal odd supply。
>
> 范围：唯一 surviving single-5 low edge
> \[
> (z,w)=(1,4),\qquad
> B=k+1,\qquad
> \lambda_2=1,\qquad
> k\ge32.
> \]

状态：**本文各 valuation identity 已严格完成；low edge 尚未整体关闭。**

---

## 1. decimal recovery 数据

corrected single-5 reduction 已证明该 cell 的共同 decimal height 必为

\[
\boxed{n=2k+1.}
\tag{1}
\]

其 reduced tail pair 为

\[
\boxed{
L=2^{k-1}5^{2k+1},
\qquad
M=h,
}
\tag{2}
\]

其中 `(h,10)=1`。

因此

\[
\omega=\frac{10^n}{L}=2^{k+2},
\]

真实第三分母为

\[
\boxed{b_3=2^{k+2}h.}
\tag{3}
\]

因为 normalized third numerator 的 reduced 2-denominator depth正好是 `n`，真实 `a3` 为奇数：

\[
\boxed{v_2(a_3)=0.}
\tag{4}
\]

---

## 2. sphere lcm 的 2-adic 结构

minimal diagonal 中 `b2=1`，且当前

\[
b_1=10T^2-4=4b_{1,0},
\qquad b_{1,0}\text{ odd}.
\]

odd supply 写成

\[
h=qs,
\qquad s\mid b_1,
\]

其中 `s` 为 odd whole-block selector，因此 `s|b_{1,0}`。又 `q|Q` 与 `b1` 互素。

所以

\[
\gcd(b_1,b_3)=4s.
\]

令

\[
q_{\rm sph}=\operatorname{lcm}(b_1,b_2,b_3).
\]

则

\[
q_{\rm sph}
=2^{k+2}qsb_{1,0}/s
=2^{k+2}qb_{1,0}.
\]

于是球面坐标

\[
y_i=q_{\rm sph}\frac{a_i}{b_i}
\]

满足：

- `a1` 为奇数（因为 `b1` 偶且 `(a1,b1)=1`），故
  \[
  \boxed{v_2(y_1)=k;}
  \tag{5}
  \]
- `a2=10T^2-1` 为奇数，故
  \[
  \boxed{v_2(y_2)=k+2;}
  \tag{6}
  \]
- `q_sph/b3=b_{1,0}/s` 为奇数，且 `a3` 奇，故
  \[
  \boxed{v_2(y_3)=0.}
  \tag{7}
  \]

因此

\[
\boxed{
v_2(y_1^2+y_2^2)=2k.
}
\tag{8}
\]

---

## 3. safe gap integer 的 exact `2`-valuation

safe integer-gap recovery 给唯一正整数 `A_gap`：

\[
H-y_3=LA_{\rm gap},
\]

以及

\[
(H-y_3)(H+y_3)=y_1^2+y_2^2.
\tag{9}
\]

由 (7) 与

\[
H^2=y_1^2+y_2^2+y_3^2
\]

知 `H` 也是奇数。

而 `H-y3` 被 `L` 中的 `2^{k-1}` 整除，`k>=32`，所以

\[
H\equiv y_3\pmod4.
\]

因此

\[
\boxed{v_2(H+y_3)=1.}
\tag{10}
\]

由 (8)-(10)：

\[
v_2(H-y_3)=2k-1.
\]

再减去

\[
v_2(L)=k-1
\]

得到

\[
\boxed{v_2(A_{\rm gap})=k.}
\tag{11}
\]

---

## 4. `A_gap` 是 5-adic unit

safe determinant identity 为

\[
c(Cb_3-D_ca_3)
=A_{\rm gap}(M+D_cL),
\tag{12}
\]

其中 `D_c=TQ`。

当前：

- `C,b3,c` 都是 5-adic units；
- `D_c a3` 被 `5^k` 整除；
- `M=h` 是 5-unit；
- `D_cL` 被 `5^{3k+1}` 整除。

所以 (12) 左侧是 5-unit，右侧括号也是 5-unit。因此

\[
\boxed{v_5(A_{\rm gap})=0.}
\tag{13}
\]

综上可写

\[
\boxed{
A_{\rm gap}=2^kA_0,
\qquad (A_0,10)=1.
}
\tag{14}
\]

于是

\[
\boxed{
v_2(H-y_3)=2k-1,\qquad
v_5(H-y_3)=2k+1.
}
\tag{15}
\]

---

## 5. prefix norm 的 5-depth 必须恰好等于 `2k+1`

当前三个原分母在 5-adic 上都是单位：

\[
5\nmid b_1b_2b_3.
\]

因此 `q_sph` 也是 5-unit，并且

\[
y_1^2+y_2^2
=\left(\frac{q_{\rm sph}}{b_1}\right)^2
N,
\]

故

\[
\boxed{
v_5(y_1^2+y_2^2)=v_5(N).
}
\tag{16}
\]

另一方面 `y3` 是 5-unit。由 sphere equation，`H` 也是 5-unit。

由 (15)，

\[
5\mid H-y_3.
\]

于是

\[
H+y_3\equiv2y_3\not\equiv0\pmod5,
\]

所以

\[
\boxed{v_5(H+y_3)=0.}
\tag{17}
\]

再由 sphere factorization (9)：

\[
v_5(y_1^2+y_2^2)=2k+1.
\]

结合 (16)：

\[
\boxed{v_5(N)=2k+1.}
\tag{18}
\]

这把 corrected single-5 reduction 的必要条件

\[
v_5(N)\ge2k+1
\]

严格加强为 exact equality。

---

## 6. exact Hensel shell

当前 `(z,w)=(1,4)` 的显式 prefix 满足

\[
N\equiv(T+N_0-1)^2+16
\pmod{5^{2k+2}},
\]

这里模数可取 `5^{2k+2}`：

- `100T^3` 的 5-depth 是 `3k+2>2k+2`；
- `50T^2` 的 5-depth 是 `2k+2`，其对平方模 `5^{2k+2}` 的影响仍消失。

令

\[
j:=T+N_0-1.
\]

则 (18) 等价于

\[
\boxed{
v_5(j^2+16)=2k+1.}
\tag{19}
\]

也就是

\[
\boxed{
 j^2\equiv-16\pmod{5^{2k+1}},
\qquad
j^2\not\equiv-16\pmod{5^{2k+2}}.
}
\tag{20}
\]

同时 decimal prefix interval 给

\[
\boxed{1.1T-1\le j<2T-1.}
\tag{21}
\]

因此 low edge 已被压成两个 Hensel root branches 的**单层 shell**，而不是任意 high-depth branch。

下一步可直接研究 (20)-(21) 的 Hensel root size，或把 exact unit

\[
(j^2+16)/5^{2k+1}\not\equiv0\pmod5
\]

接回 sphere conjugate factor与 odd supply。

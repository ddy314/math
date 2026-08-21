# A1 minimal diagonal: single-5 top-edge common-quotient lock

> 日期：2026-08-22。
>
> 依赖：`deep-single5-decimal-height-collapse.md`、`global-terminal-bridge.md`、`diagonal.md`。
>
> 范围：minimal diagonal `k=g>=32` 的唯一 surviving single-5 top edge
> \[
> D_{\rm gap}=5^B,\qquad B>k,\qquad \lambda_2=2k-1.
> \]

状态：**本文各结论均已严格完成；top edge 尚未整体关闭。**

---

## 1. top edge 的 primitive tail pair

令

\[
T=10^k,
\qquad h=qs,
\qquad (h,10)=1.
\]

single-5 gap normalization 为

\[
5^BT\rho=h2^{2k-1},
\qquad
\rho=\frac{M}{L},
\qquad (L,M)=1.
\tag{1}
\]

因为

\[
T=2^k5^k,
\]

(1) 约到最低项后精确给出

\[
\boxed{
L=5^{B+k},
\qquad
M=2^{k-1}h.
}
\tag{2}

若第三分子位数为 `n=n_3`，safe normalization 写成

\[
10^n=\omega L,
\qquad
b_3=\omega M.
\]

于是

\[
\omega=2^n5^{n-B-k},
\]

特别地

\[
\boxed{n\ge B+k}
\tag{3}
\]

并且

\[
\boxed{
b_3=2^{n+k-1}5^{n-B-k}h.}
\tag{4}

所以

\[
\boxed{v_2(b_3)=n+k-1.}
\tag{5}

---

## 2. 整数球面的 2-adic parity

令

\[
\mathfrak q=\operatorname{lcm}(b_1,b_2,b_3),
\qquad
y_i=\frac{a_i\mathfrak q}{b_i}.
\]

minimal diagonal 中 `b2=1`，且

\[
b_1=10^{2k+1}-w,
\qquad e:=v_2(b_1)=v_2(w)\le2.
\]

由 (3),(5) 与 `k>=32`：

\[
v_2(b_3)=n+k-1>e,
\]

所以

\[
\boxed{v_2(\mathfrak q)=n+k-1.}
\tag{6}

又 `a2=10^(2k+1)-z` 为奇数，故

\[
\boxed{v_2(y_2)=n+k-1.}
\tag{7}

同时

\[
v_2(y_1)
=v_2(a_1)+n+k-1-e
\ge n+k-1-e>0,
\tag{8}
\]

所以 `y1,y2` 都为偶数。

另一方面 `b3` 为偶数，第三分数既约强迫 `a3` 为奇数；而 `mathfrak q/b3` 为奇数，因此 `y3` 为奇数。整数球面

\[
y_1^2+y_2^2+y_3^2=H^2
\]

于是给出

\[
\boxed{H\ \text{为奇数}.}
\tag{9}

定义 carrier integer gap

\[
\Delta:=10^ky_1-H>0.
\]

因为 `10^k y1` 为偶数、`H` 为奇数：

\[
\boxed{v_2(\Delta)=0.}
\tag{10}

---

## 3. safe common quotient 的 2-adic depth 精确为 1

`global-terminal-bridge.md` 的 safe gap 为

\[
U=H-y_3=LA,
\qquad
\mathcal T=MA,
\tag{11}
\]

其中本文用 `A` 表示唯一正整数 common quotient。

在 minimal diagonal `g=k,m2=1,b2=1` 中，safe recovery identity 精确化为

\[
\boxed{
\mathcal T
=10^kQ\Delta-10^{2k}y_1+y_2.
}
\tag{12}

由 (10)，第一项满足

\[
v_2(10^kQ\Delta)=k
\]

（`Q` 为奇数）。

由 (8)：

\[
v_2(10^{2k}y_1)>k,
\]

而由 (7) 与 (3)：

\[
v_2(y_2)=n+k-1>k.
\]

因此 (12) 中第一项唯一承担最低 2-adic valuation：

\[
\boxed{v_2(\mathcal T)=k.}
\tag{13}

另一方面由 (2),(11)：

\[
\mathcal T=2^{k-1}hA,
\]

其中 `h` 为奇数。与 (13) 比较即得

\[
\boxed{v_2(A)=1.}
\tag{14}

写

\[
\boxed{A=2A_0,\qquad A_0\ \text{奇}.}
\tag{15}

这把 top edge 的 sphere/common-quotient 2-part 完全锁死。

---

## 4. 一个 exact depth-`n-1` quotient

将 (12) 与

\[
\mathcal T=2^khA_0
\]

同时除以 `2^k`：

\[
 hA_0
=5^kQ\Delta
-2^k5^{2k}y_1
+\frac{y_2}{2^k}.
\tag{16}

由 (7)：

\[
v_2(y_2/2^k)=n-1.
\tag{17}

而由 (8)：

\[
\begin{aligned}
v_2(2^k5^{2k}y_1)
&=k+v_2(y_1)\\
&\ge n+2k-1-e\\
&>n-1,
\end{aligned}
\tag{18}

因为 `k>=32,e<=2`。

因此 (16) 的 correction 有精确 valuation

\[
\boxed{
v_2\!\left(hA_0-5^kQ\Delta\right)=n-1.
}
\tag{19}

---

## 5. 与 high-sign synchronization 联立

`deep-single5-decimal-height-collapse.md` 在 top edge 给出 surviving high sign 的精确条件

\[
\boxed{
v_2\!\left(h+5^{B+2k}Q\right)=n-1.}
\tag{20}

故存在奇整数 `R_1,R_2` 使

\[
h+5^{B+2k}Q=2^{n-1}R_1,
\tag{21}
\]

\[
hA_0-5^kQ\Delta=2^{n-1}R_2.
\tag{22}
\]

将 (21) 乘以奇数 `A0` 并与 (22) 相减：

\[
Q\left(5^{B+2k}A_0+5^k\Delta\right)
=2^{n-1}(R_1A_0-R_2).
\]

`R1,A0,R2` 都为奇数，所以括号 `R1 A0-R2` 为偶数。又 `Q` 为奇数，故

\[
\boxed{
2^n\mid \Delta+5^{B+k}A_0.
}
\tag{23}

这是 sphere common quotient 与 high-sign decimal synchronization 的一个 exact compatibility condition。

本文只记录 (23) 为必要条件；它本身尚未构成空性证明。

---

## 6. consequence

当前唯一 single-5 top-edge candidate 除此前的

\[
\lambda_2=2k-1,
\quad
v_2\!\left(s+5^{B+2k}v\right)=n-1,
\quad
n\ge B+k
\]

外，还必须满足

\[
\boxed{v_2(A)=1}
\]

以及 (19),(23)。

特别地，common quotient 不再携带任意 2-adic 深度；全部剩余巨大 2-depth 必须由 high-sign cancellation 本身提供。
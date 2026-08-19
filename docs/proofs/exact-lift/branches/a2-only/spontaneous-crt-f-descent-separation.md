# A2 f-denominator inert carrier 与 descendant common support 只剩 fixed height `7`

> **依赖：** `spontaneous-denominator-depth-matrix.md`、`endpoint-lattice.md` 的 canonical factor allocation、`spontaneous-crt-height-primitive-remainder.md`、`spontaneous-crt-target-descent-overlap.md`。
>
> **严格状态：**完整 f-saturation 中，third-block saturation给 `2a_3+9T=0`，exact factor allocation进一步在完整 `p^e` 深度给 `DK=6D+C`。代入 descended quotient后，`Dhat_63` 的截断深度被 pure quadratic `G_D=11K^2-240K+432` 精确读取。原 f-additive denominator depth则由 `P_f=3K^2-36K+26` 读取。两 quadratic 的 resultant只有 `2,7,73,977`，唯一 inert prime是 fixed `7`。该 root `K=1 mod7` 又强迫 `7|W_q,H_0`，所以它实际属于已有 sphere-height channel，并且由于 resultant中 `7` 只出现一层，f-denominator/descent common gcd在该 label上最多只贡献一层。本文删除 generic f-denominator common channel，但不排除 fixed height-7 本身，因此不关闭 A2。

---

## 1. saturated f-prime data

固定 genuine non-`3` inert prime

\[
p^e\Vert f,
\qquad
p^e\mid\mathscr L_{23},
\qquad e\ge1,
\]

其中

\[
\mathscr L_{23}=\frac{9T}{2}+a_3.
\]

于是

\[
\boxed{2a_3+9T\equiv0\pmod{p^e}.}
\tag{1.1}

`spontaneous-denominator-depth-matrix.md` 已把 original additive f-depth降成

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),e\}
=
\min\{v_p(P_f(K)),e\},}
\tag{1.2}

\[
\boxed{P_f(K):=3K^2-36K+26.}
\tag{1.3}

---

## 2. exact f-allocation gives `DK=6D+C mod p^e`

沿用 canonical Gaussian factor equalities

\[
\mathcal A-Z=5^{\lambda-d}fN,
\tag{2.1}
\]

\[
\mathcal A+Z=5^{\lambda-d}q c_+^2Y,
\tag{2.2}
\]

以及

\[
\mathcal A=c_u5^{\lambda-d}DK.
\tag{2.3}
\]

模 `p^e`，因为 `p^e|f`，(2.1) 给

\[
Z\equiv\mathcal A.
\]

所以 (2.2) 给

\[
2c_uDK
\equiv q c_+^2Y
\pmod{p^e}.
\tag{2.4}

又

\[
f=5^\lambda q+2c_u
\equiv0\pmod{p^e},
\]
所以

\[
q\equiv-2c_u5^{-\lambda}\pmod{p^e}.
\]

代入 (2.4)，消去 unit `2c_u`：

\[
5^\lambda DK+c_+^2Y\equiv0\pmod{p^e}.
\tag{2.5}

reflection factor equality为

\[
\boxed{
c_+^2Y
=g(3T+2a_3)-5^\lambda C.}
\tag{2.6}

由 (1.1)：

\[
3T+2a_3\equiv-6T\pmod{p^e}.
\]

再用

\[
gT=D5^\lambda,
\]
得到

\[
c_+^2Y
\equiv-5^\lambda(6D+C)\pmod{p^e}.
\]

代回 (2.5)，并消去 `5^lambda`：

\[
\boxed{
DK\equiv6D+C\pmod{p^e}.}
\tag{2.7}

因为 f-prime与 `D` 分离，定义

\[
\delta:=C/D
\]
后：

\[
\boxed{\delta\equiv K-6\pmod{p^e}.}
\tag{2.8}

这是一条 full prime-power allocation，不只是 first-layer relation。

---

## 3. descendant depth becomes a second pure K-quadratic

cleared descended quotient为

\[
\boxed{
\begin{aligned}
F_{63}^{(16)}={}&
16(2K-9)
\{g((2K-12)T-2a_3)+5^\lambda C\}\\
&-63gTK^2.
\end{aligned}}
\tag{3.1}

`Dhat_63` 与它只差 genuine p-units。

除以 unit `gT`，再使用 (1.1),(2.8)：

\[
\frac{F_{63}^{(16)}}{gT}
\equiv
32(K-6)K-144(K-6)+K^2-384K+432.
\]

右边精确化简为

\[
\boxed{
\frac{F_{63}^{(16)}}{gT}
\equiv3G_D(K)\pmod{p^e},}
\tag{3.2}

其中

\[
\boxed{G_D(K):=11K^2-240K+432.}
\tag{3.3}

`p` 为 non-3，所以 `3` 为 unit。因此

\[
\boxed{
\min\{v_p(\widehat{\mathscr D}_{63}),e\}
=
\min\{v_p(G_D(K)),e\}.}
\tag{3.4}

这给 saturated f-channel 一个新的 descendant depth reader。

---

## 4. two pure quadratics leave only fixed `7,73,977`

若 f-denominator prime同时进入 descendant common support，则 first layer必须

\[
P_f(K)\equiv0,
\qquad
G_D(K)\equiv0
\pmod p.
\]

resultant为

\[
\boxed{
\operatorname{Res}_K(P_f,G_D)
=-1996988
=-2^2\cdot7\cdot73\cdot977.}
\tag{4.1}

三个 odd candidates的 mod-4 classes为

\[
7\equiv3,
\qquad
73\equiv1,
\qquad
977\equiv1
\pmod4.
\]

所以 genuine inert overlap只剩

\[
\boxed{p=7.}
\tag{4.2}

common root唯一为

\[
\boxed{K\equiv1\pmod7.}
\tag{4.3}

因此 generic f-denominator inert support与 descendant common kernel完全分离；唯一例外是 fixed `7`。

---

## 5. fixed `7` automatically belongs to the height channel

在 `p=7,K=1` 下，由 (2.8)：

\[
\delta\equiv K-6\equiv2\pmod7.
\]

而

\[
N=3D-C=D(3-\delta),
\]
所以

\[
\boxed{N\equiv D\pmod7.}
\tag{5.1}

于是

\[
DK-N
\equiv D-N
\equiv0\pmod7.
\tag{5.2}

又 `7|f`，而 source split有

\[
\gcd(q,f)=1.
\]

因此

\[
7\nmid q.
\]

由全局 quotient

\[
DK-N=qW_q
\]
可消去 q-unit：

\[
\boxed{7\mid W_q.}
\tag{5.3}

已有 height theorem 对每个 non-3 inert divisor of `W_q` 给

\[
\boxed{v_7(W_q)=v_7(H_0),}
\tag{5.4}

\[
\boxed{\left(\frac{N_0}{7}\right)=-1.}
\tag{5.5}

因此 fixed f/descent overlap并不是新的 denominator-external label，而是

\[
\boxed{
\text{fixed }7\text{ sphere-height channel}.}
\tag{5.6}

---

## 6. the fixed overlap is transverse and contributes only one common layer

resultant (4.1) 中 `7` 的 exponent恰为 `1`。因此 Bezout identity给：

\[
\boxed{
\min\{v_7(P_f),v_7(G_D)\}=1}
\tag{6.1}

在任何 simultaneous f/descent lift上成立。

由 depth readers (1.2),(3.4)，若 `e>=2`，则 original additive f-depth与 descended quotient depth不可能同时超过一层；若 `e=1` 更是平凡。

而 descendant common factor

\[
G_\Delta=\gcd(Rstar_{63},Dhat_{63})
\]
若在 `7` 上有两层，则 descent identity会使 `That_2,Dhat_63` 都至少有两层，与 (6.1) 矛盾。因此

\[
\boxed{
v_7(G_\Delta)=1}
\tag{6.2}

在 fixed f-denominator overlap存在时成立。

所以它最多向 descendant common parity支付一份 squarefree `7`，不存在 f-denominator 驱动的 deep common Hensel tree。

---

## 7. denominator channels are now removed from generic common parity

结合 q-side complete separation：

\[
\boxed{
q\text{-denominator inert}
\cap\operatorname{Supp}(G_\Delta)=\varnothing,}
\tag{7.1}

而本文给

\[
\boxed{
f\text{-denominator inert}
\cap\operatorname{Supp}(G_\Delta)
\subseteq\{7\},}
\tag{7.2}

且 `7` 已重分类到 sphere-height support并仅一层。

因此 `spontaneous-crt-descendant-common-parity.md` 中尚未解释的 common inert parity已经不再含 generic q/f denominator source。剩余 old-pool labels为：

1. fixed target `31/179`；
2. source-common overlap的 double-short depth；
3. fixed height shadow `7`；
4. genuinely endpoint-external/spontaneous common kernel。

A2 仍为 `待证`。

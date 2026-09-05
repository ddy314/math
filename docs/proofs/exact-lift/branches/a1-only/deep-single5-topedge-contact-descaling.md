# A1 minimal diagonal: top-edge contact-factor descaling

> 日期：2026-08-22。
>
> 依赖：`deep-single5-topedge-oriented-root-factors.md`、`deep-contact-q-square-blocks-universal.md`。
>
> 范围：minimal diagonal `k=g>=32` 的 surviving single-5 top edge。

状态：**本文严格识别新 `F_\pm` 与旧 contact factors，并给出去公共尺度后的定向整数系统。该识别同时说明旧 Q-side `q^2` lifting 不能作为与 `F_\pm` 独立的第二个平方 obstruction 重复使用。**

---

## 1. global square 与旧 contact square 是同一个判别根

旧 rational-contact square 写成

\[
V^2=G^2C^2-D_c^2N-2\rho D_cN,
\qquad D_c=TQ.
\tag{1}
\]

而 global terminal 使用

\[
z^2=\frac{C^2}{D_c^2}-(1+2\theta)\frac N{G^2},
\qquad
\rho=D_c\theta.
\]

乘以 `D_c^2 G^2` 得

\[
(D_cGz)^2
=G^2C^2-D_c^2N-2\rho D_cN.
\]

因此可取

\[
\boxed{V=D_cGz.}
\tag{2}
\]

`global-squarefree-terminal.md` 中

\[
W=\kappa D_cGz,
\]

所以

\[
\boxed{W=\kappa V.}
\tag{3}
\]

---

## 2. `F_pm` 正好是旧 contact factors 的公共整数放大

single-5 中 gap denominator 为

\[
D_{\rm gap}=5^B.
\]

旧 contact integer root 为

\[
Z=5^BV,
\]

旧 factors 为

\[
\boxed{
L_-:=5^BGC-Z,
\qquad
L_+:=5^BGC+Z.
}
\tag{4}
\]

当前定向 factors 为

\[
F_-:=\kappa GC-W,
\qquad
F_+:=\kappa GC+W.
\]

由 (3)-(4)：

\[
\boxed{
F_\pm=\frac{\kappa}{5^B}L_\pm.
}
\tag{5}
\]

而 top edge

\[
\kappa=2^{e+1}5^{B+2k}uv,
\]

故公共放大因子精确为

\[
\boxed{
\frac\kappa{5^B}
=2^{e+1}5^{2k}uv.
}
\tag{6}
\]

所以旧 contact Q-side `q^2` whole-block lifting 与当前 `F_pm` factorization 是同一个平方在不同 normalization 下的表达；后续不能把两者统计为独立 obstruction。

---

## 3. integrality 强迫新的 `5^(2k)` 与 `v` divisibility

`deep-single5-topedge-oriented-root-factors.md` 已给

\[
F_-=2^{n+2k+n_2-1}uv^2A_-,
\tag{7}
\]

\[
F_+=2^{2e+2}uR B_+,
\tag{8}
\]

其中 `A_-,B_+` 为奇正整数，并且

\[
A_-B_+
=5^{B+4k+n_5}q^2vN_{10}.
\tag{9}
\]

由 (5)-(6)，每个 `F_pm` 都必须被

\[
2^{e+1}5^{2k}uv
\]

整除。

对 (7)，`2,u,v` 部分已经足够，且 `v^2` 还多一份；由于 `(5,uv)=1`，必须有

\[
\boxed{5^{2k}\mid A_-.}
\tag{10}
\]

对 (8)，已知

\[
(R,5v)=1
\]

（`R` 是 5-unit，且前文已证 `(R,v)=1`）。因此除去已有 `2,u` 后，完整的 `5^(2k)v` 都必须来自 `B_+`：

\[
\boxed{5^{2k}v\mid B_+.}
\tag{11}
\]

定义奇正整数

\[
\boxed{
A_- =5^{2k}A_0,
\qquad
B_+=5^{2k}vB_0.
}
\tag{12}
\]

则 (5),(7)-(8) 化成真正去公共尺度的 contact factors：

\[
\boxed{
L_-
=2^{n+2k+n_2-e-2}vA_0,
}
\tag{13}
\]

\[
\boxed{
L_+
=2^{e+1}RB_0.
}
\tag{14}
\]

而 (9) 精确降为

\[
\boxed{
A_0B_0
=5^{B+n_5}q^2N_{10}.
}
\tag{15}
\]

这里 `u` 与公共 `5^(2k)` 高度全部消失；Q-complement `v` 也已被定向吸收到 `L_-` 的显式因子中，而不再出现在 product (15)。

---

## 4. exact sum equation

由定义 (4)：

\[
L_-+L_+=2\cdot5^BGC.
\]

又 `G=2^esu`。把 (13)-(14) 代入并除以 `2^(e+1)`：

\[
\boxed{
2^{E}vA_0+RB_0=5^BsuC,
}
\tag{16}
\]

其中

\[
\boxed{
E:=n+2k+n_2-2e-3.
}
\tag{17}
\]

因为 `Z>0`，有 `L_+>L_-`，因此还得到严格方向

\[
\boxed{
RB_0>2^EvA_0.
}
\tag{18}
\]

与 (16) 联立：

\[
\boxed{
2^{E+1}vA_0<5^BsuC,
}
\tag{19}
\]

\[
\boxed{
2RB_0>5^BsuC.
}
\tag{20}
\]

所以 top edge 已化为一个定向的 sum-product system：

\[
\boxed{
\begin{gathered}
A_0B_0=5^{B+n_5}q^2N_{10},\\
2^EvA_0+RB_0=5^BsuC,\\
RB_0>2^EvA_0,\\
s+5^{B+2k}v=2^{n-1}R.
\end{gathered}}
\tag{21}
\]

下一步应直接研究 (21) 的 5-adic allocation 与高度；旧 `q^2` contact lifting 已包含在该系统中，不再单独重复计数。
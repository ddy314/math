# A2 floor-free CRT carrier 在 odd `3`-defect 中排除 prime `3`

> **依赖：** `spontaneous-crt-floorfree-parity.md`、`spontaneous-crt-quotient-source-scale.md`、`endpoint-lattice.md` §16.11。
>
> **严格状态：**前一 parity 文件只在 `eta=1,k_h=3` 类型证明 `3∤P_Delta`。本文指出该论证只使用 `v_3(k_h)` 为奇数时 §16.11 的统一结构，因此可推广到全部 reflection high-2 odd-`3` defect：若 `v_3(k_h)` 为奇数，则 `Delta_+` 与 `P_Delta` 都是 `3`-进 units。故任何由 `|P_Delta|≡3 mod4` 触发的 odd-inert parity都必须由 non-`3` inert prime支付。本文是 general surcharge lemma，不关闭 A2。

令

\[
e_3:=v_3(k_h).
\]

`endpoint-lattice.md` §16.11 已证明，若 `e_3` 为奇数，则只有两个局部通道，但二者统一满足

\[
\boxed{3\mid a_2,\qquad3\mid a_3,\qquad3\nmid b_2b_3g.}
\tag{1.1}
\]

同时 high/low 两个因子的 `3`-进深度都至少为一，因此

\[
3\mid H_0,\qquad3\mid Y_2.
\tag{1.2}
\]

由

\[
H_0=g(3T+a_3)-5^\lambda C
\]
及 (1.1)：

\[
\boxed{3\mid C.}
\tag{1.3}
\]

又

\[
K=9N+10a_2
\]
给

\[
\boxed{3\mid K.}
\tag{1.4}
\]

记

\[
N_s:=3D-C.
\]

由 (1.3)：

\[
\boxed{3\mid N_s.}
\tag{1.5}
\]

由于 `3∤b_2` 且

\[
b_2=2^{M+m+1}c_ug,
\]
有

\[
3\nmid c_ugD.
\tag{1.6}
\]

现在使用 exact right-gap formula

\[
\begin{aligned}
D\Delta_+
={}&c_u^2\Bigl[
D^2(TK^2-14KT-4Ka_3+37T+14a_3)\\
&+DN_s(-2KT+7T+2a_3)+TN_s^2
\Bigr]\\
&-z^2N_s(TN_s+2a_3D).
\end{aligned}
\]

模 `3` 使用 (1.1),(1.4),(1.5)，所有项消失，只剩

\[
D\Delta_+
\equiv c_u^2D^2T
\not\equiv0\pmod3.
\]

所以

\[
\boxed{e_3\text{ odd}\Longrightarrow3\nmid\Delta_+.}
\tag{1.7}
\]

floor-free carrier为

\[
\mathscr P_\Delta
=2^{A_G}\Delta_+
-5^{B_G}k_h^3(D^2-C^2).
\]

若 `e_3` 为奇数，则第二项被 `3` 整除，而第一项由 (1.7) 是 unit。因此

\[
\boxed{e_3\text{ odd}\Longrightarrow3\nmid\mathscr P_\Delta.}
\tag{1.8}
\]

另一方面 parent parity theorem给

\[
|\mathscr P_\Delta|\equiv3\pmod4
\iff
\varepsilon=(-1)^{e_3}.
\]

所以在 odd-`e_3` branch 中，只要 parity criterion触发，即 `epsilon=-1`，就严格有

\[
\boxed{
|\mathscr P_\Delta|\equiv3\pmod4,
\qquad3\nmid\mathscr P_\Delta,
}
\]

从而 `|P_Delta|` 必含至少一枚

\[
\boxed{p\ne3,\qquad p\equiv3\pmod4}
\]
到奇次。

这把 `eta=1,k_h=3` 的 non-`3` surcharge推广到整个 odd `3`-primary Gaussian defect。

A2 仍为 `待证`。

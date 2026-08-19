# A2 floor-free CRT carrier 的 full-`2^{A_G}` square class

> **依赖：** `spontaneous-crt-gaussian-floorfree-carrier.md`、`spontaneous-crt-gap-full5-residue.md`、`endpoint-lattice.md` low-`m` reflection bounds。
>
> **严格状态：**`P_Delta` 的 mod-8 orientation此前已用于 parity。本文证明低 `m` reflection cone中 `D^2` 实际被完整 `2^{A_G}` 吞掉，因此 `P_Delta` 在同一增长模数上精确满足 `P_Delta≡5^{B_G}k_h^3 C^2 mod2^{A_G}`。也就是说除去显式 odd factor后，floor-free CRT/Gaussian carrier具有由真实 top defect `C` 给出的完整 2-adic square root。结合已有 full-`5^lambda` residue，`P_Delta` 现在同时携带两个随 `M` 增长的独立 local fingerprints。本文不单独关闭 A2。

---

## 1. exponents

定义

\[
A_G:=\frac{M+5\eta}{2}+8,
\qquad
B_G:=3M-d-\eta-3,
\qquad
\eta=2m-M.
\]

因此

\[
\boxed{A_G=5m-2M+8.}
\tag{1.1}
\]

reflection source factor为

\[
g=2^{t-1}\rho,
\qquad t\ge3,
\]
所以

\[
D=g2^m5^d
\]
满足

\[
\boxed{v_2(D)=m+t-1\ge m+2.}
\tag{1.2}
\]

于是

\[
2v_2(D)\ge2m+4.
\]

比较 (1.1)：

\[
2m+4-A_G
=2M-3m-4.
\]

当前 low-`m` cone有

\[
m\le\frac{6M}{11},
\qquad M\ge11.
\]

因此

\[
2M-3m-4
\ge\frac{4M}{11}-4
\ge0.
\]

所以

\[
\boxed{2v_2(D)\ge A_G.}
\tag{1.3}
\]

等价地

\[
\boxed{2^{A_G}\mid D^2.}
\tag{1.4}
\]

---

## 2. CRT modulus modulo the full 2-adic scale

令

\[
M_\Delta:=D^2-C^2.
\]

由 (1.4)：

\[
\boxed{
M_\Delta\equiv-C^2\pmod{2^{A_G}}.}
\tag{2.1}
\]

`C` 为 odd，所以 `C^2` 是模 `2^{A_G}` 的 unit square。

---

## 3. full square-class formula for `P_Delta`

floor-free carrier定义为

\[
\mathscr P_\Delta
=2^{A_G}\Delta_+
-5^{B_G}k_h^3M_\Delta.
\]

模 `2^{A_G}` 第一项消失；用 (2.1)：

\[
\boxed{
\mathscr P_\Delta
\equiv
5^{B_G}k_h^3C^2
\pmod{2^{A_G}}.}
\tag{3.1}
\]

因为 `5,k_h,C` 都为 odd，右边是 unit。

把显式 unit移到左边：

\[
\boxed{
\mathscr P_\Delta
(5^{B_G}k_h^3)^{-1}
\equiv C^2
\pmod{2^{A_G}}.}
\tag{3.2}
\]

所以 `P_Delta/(5^{B_G}k_h^3)` 的完整 2-adic unit class不只是 mod-8 square character；其实际 square root就是 top defect `C`。

---

## 4. signed absolute-value version

已有

\[
\operatorname{sgn}(\mathscr P_\Delta)=-\varepsilon.
\]

所以

\[
|\mathscr P_\Delta|=(-\varepsilon)\mathscr P_\Delta.
\]

由 (3.1)：

\[
\boxed{
|\mathscr P_\Delta|
\equiv
(-\varepsilon)5^{B_G}k_h^3C^2
\pmod{2^{A_G}}.}
\tag{4.1}
\]

因此 Gaussian side `epsilon` 精确决定绝对 carrier相对于显式 factor `5^{B_G}k_h^3` 是 `+square` 还是 `-square` 的完整 2-adic lift。

模 `8` 时 (4.1) 正好恢复 parent parity theorem；本文是其 full-depth strengthening。

---

## 5. combine with the full-`5^lambda` fingerprint

前一文件已有

\[
\boxed{
\mathscr P_\Delta
\equiv
2^{A_G}c_u^2a_3[D(20-4K)-2C]
\pmod{5^\lambda},}
\tag{5.1}
\]

且

\[
v_5(\mathscr P_\Delta)=0.
\]

现在同一个 ordinary integer `P_Delta` 同时满足：

\[
\boxed{
\begin{cases}
\mathscr P_\Delta
\equiv5^{B_G}k_h^3C^2
\pmod{2^{A_G}},\\[1mm]
\mathscr P_\Delta
\equiv2^{A_G}c_u^2a_3[D(20-4K)-2C]
\pmod{5^\lambda},\\[1mm]
\operatorname{sgn}(\mathscr P_\Delta)=-\varepsilon.
\end{cases}}
\tag{5.2}
\]

由于 `gcd(2^{A_G},5^lambda)=1`，(5.2) 是一个真正的 bi-adic signed fingerprint，而不是同一 local congruence的重复写法。

---

## 6. current role

full `2`-adic square root直接使用真实 top defect `C`，full `5`-adic residue则已经在 `spontaneous-crt-extra-d-z-reader.md` 中线性读取 centered `z_E mod5^d`。

所以后续可尝试把 `(C,z_E)` 两个自然代表共同送入 `P_Delta` 的 CRT class；若 combined residue的最小 signed representative与 `sgn(P_Delta)=-epsilon` 不相容，就能真正排除 Gaussian side。

目前 modulus product仍不足以单靠大小覆盖 `|P_Delta|`，因此本文不宣称 natural representative唯一，也不关闭 A2。

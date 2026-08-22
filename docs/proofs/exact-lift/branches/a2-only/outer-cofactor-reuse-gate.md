# A2 outer rational-root cofactors 的 non-`3` surcharge 与 shared-reuse gate

> **依赖：** `endpoint-lattice.md` §§16.11、16.27–16.29、16.33–16.36、16.57–16.59；`spontaneous-crt-universal-descendant-cubic.md`（整合于 `crt-descent-ledger.md`）。
>
> **严格状态：**在危险 `Z≡1 (mod 4)` orientation 中，odd-`3` allocation 已迫使 `3|a_2,a_3` 且 `3∤b_2D`。本文把这一事实与 rational-root 的三个相邻整数值联立：`F(2),F(4)` 模 `3` 都是单位，而 `D-C|F(2)`,`D+C|F(4)`，故严格得到 `3|C`；两个 outer cofactors `Xi_-,Xi_+` 因此都是 `3`-进单位。又因三 cofactor 共享 `Y` 的 denominator-wide square class、且 `Y≡3 (mod4)`，两个 outer cofactors 都是 positive `3 mod4`，所以各自必须含 non-`3` inert supplier。若同一 genuine non-`3` prime试图同时支付两边，消去 `F(2),F(4)` 的共同 coefficient ratio得到 compact cubic `G_pm(K,zeta)`；再与 universal descendant cubic消元只剩一个 primitive irreducible degree-30 `K` gate。历史 fixed target roots `31:K=9` 与 `179:K=71` 均不落在该 gate上，因此 fixed `31/179` common label不能同时支付两个 outer cofactor parity；至少还需另一枚 distinct non-`3` inert prime。fixed height `7` 仍命中该 gate，故本文不宣称 old pool全部关闭，更不宣称 A2 空。

---

## 1. dangerous `Z=1` 的 odd-`3` input

`endpoint-lattice.md` §16.57–16.59 已证明，在

\[
Z\equiv1\pmod4
\]

时

\[
3\mid a_2,
\qquad
3\mid a_3,
\qquad
3\nmid b_2D,
\tag{1.1}
\]

并且 Gaussian factor orientation为

\[
\boxed{Y\equiv3\pmod4.}
\tag{1.2}
\]

同时 `N_0=C_0^2+a_2^2` 被 `9` 整除，因为 `C_0=9b_2/2`。

沿用 rational-root quartic

\[
\boxed{
F(J)=
 b_2^2T\,J(TJ+2a_3)(K-J)^2
-Q^2N_0(TJ+a_3)^2.}
\tag{1.3}
\]

当前 `T=10^m≡1 (mod3)`，而 `K=10(9\cdot10^{M-1}+a_2)` 也被 `3` 整除。

---

## 2. two adjacent values force `3|C`

把 (1.1) 代入 (1.3) 模 `3`。第二项因 `3|N_0` 消失。

对 `J=2`：

\[
J\equiv-1,
\quad TJ+2a_3\equiv-1,
\quad K-J\equiv1
\pmod3,
\]

所以

\[
\boxed{F(2)\equiv b_2^2\not\equiv0\pmod3.}
\tag{2.1}
\]

对 `J=4≡1` 同理：

\[
\boxed{F(4)\equiv b_2^2\not\equiv0\pmod3.}
\tag{2.2}
\]

另一方面 §16.29 的 exact rational-root divisibility 给

\[
D-C\mid F(2),
\qquad
D+C\mid F(4).
\tag{2.3}
\]

所以

\[
3\nmid(D-C),
\qquad
3\nmid(D+C).
\tag{2.4}
\]

而 `3∤D`。在 `F_3` 中，对 unit `D`，`D-C` 与 `D+C` 同时非零的唯一可能是

\[
\boxed{C\equiv0\pmod3.}
\tag{2.5}
\]

因此

\[
\boxed{3\mid C.}
\tag{2.6}
\]

这是 `endpoint-lattice.md` §16.48 所要求的 `C` natural-representative 接口的一条直接全局约束；它不是固定 `eta` 枚举。

---

## 3. both outer cofactors need non-`3` inert suppliers

定义

\[
\Xi_-:=
\frac{-F(2)}{2^{2M+2}5^{\nu_5}(D-C)},
\qquad
\Xi_+:=
\frac{F(4)}{2^{2M+2}5^{\nu_5}(D+C)}.
\tag{3.1}
\]

它们都是 positive odd integers。

由 (2.1)–(2.4)，所有显示 denominator在 `3` 上均为 units，于是

\[
\boxed{3\nmid\Xi_-\Xi_+.}
\tag{3.2}
\]

§16.29 又给 denominator-wide square class

\[
\Xi_\pm
\equiv
Y\,[q c_+(jT+a_3)]^2
\pmod{2^m5^d},
\qquad j=2,4.
\tag{3.3}
\]

当前 endpoint有 `m>=2`，由 (1.2) 取模 `4`：

\[
\boxed{
\Xi_-\equiv\Xi_+\equiv3\pmod4.}
\tag{3.4}
\]

故每个 outer cofactor 的 prime factorization都含至少一枚

\[
\ell_\pm\equiv3\pmod4
\]

到奇次。结合 (3.2)：

\[
\boxed{\ell_-\ne3,\qquad\ell_+\ne3.}
\tag{3.5}
\]

所以危险 `Z=1` orientation 无条件产生两份 **non-`3`** outer-cofactor inert parity。本文此处尚不声称两枚 prime必不同。

---

## 4. if one prime pays both outer cofactors, it hits a compact cubic

固定 genuine non-`3` inert prime `p`，并设

\[
p\mid\Xi_-,
\qquad
p\mid\Xi_+.
\tag{4.1}
\]

由定义必有

\[
p\mid F(2),
\qquad
p\mid F(4).
\tag{4.2}
\]

写

\[
F(J)=A f(J)-B h(J),
\]

其中

\[
A=b_2^2T,
\quad
B=Q^2N_0,
\]

\[
f(J)=J(TJ+2a_3)(K-J)^2,
\quad
h(J)=(TJ+a_3)^2.
\tag{4.3}
\]

对 genuine non-`3` inert supplier，endpoint primitive separation给 `p∤b_2T`，所以 `A` 是 unit。由两式交叉消去 `B/A`：

\[
f(2)h(4)-f(4)h(2)\equiv0\pmod p.
\tag{4.4}
\]

令

\[
\zeta:=a_3/T.
\]

直接展开并除去 unit `4T^3`，得到 compact cubic

\[
\boxed{
\begin{aligned}
\mathcal G_{\pm}(K,\zeta):={}&
-K^2\zeta^3-3K^2\zeta^2
+12K\zeta^3+60K\zeta^2\\
&+96K\zeta+64K
-28\zeta^3-156\zeta^2-288\zeta-192.
\end{aligned}}
\tag{4.5}
\]

因此

\[
\boxed{p\mid\mathcal G_{\pm}(K,\zeta).}
\tag{4.6}
\]

这把“同一 prime 同时支付两个 outer parity”的自由度压成一张总次数很低的 fixed projective sheet。

---

## 5. descendant reuse gives one irreducible degree-30 `K` gate

若同一 `p` 还属于 descendant common support，则 common baseline通过 universal rational-root compatibility进入

\[
\mathcal E_{63}(K,\zeta)\equiv0\pmod p.
\tag{5.1}
\]

对 (4.5),(5.1) 关于 `zeta` 求 exact resultant。checker canonical 重建并验证：

\[
\boxed{
\operatorname{Res}_{\zeta}
(\mathcal E_{63},\mathcal G_{\pm})
=P_{30}(K),}
\tag{5.2}
\]

其中 fixed content为 `±1`，且

\[
\boxed{
\deg P_{30}=30,
\qquad
P_{30}\text{ 在 }\mathbf Q[K]\text{ 中不可约}.}
\tag{5.3}
\]

所以 shared outer supplier 一旦还试图复用 descendant common support，就不再是自由 moving prime，而必须满足

\[
\boxed{p\mid P_{30}(K).}
\tag{5.4}
\]

正文不抄写31个大系数；checker由两个 compact polynomials唯一重建。

---

## 6. fixed target `31/179` cannot pay both outer parities

历史 target/descent first-layer roots为

\[
(p,K)=(31,9),
\qquad
(179,71).
\tag{6.1}
\]

checker精确给

\[
\boxed{P_{30}(9)\equiv16\pmod{31},}
\tag{6.2}
\]

\[
\boxed{P_{30}(71)\equiv63\pmod{179}.}
\tag{6.3}
\]

两者均非零。因此：

\[
\boxed{
\text{fixed }31/179\text{ descendant-common label}
\text{ 不可能同时整除 }\Xi_-\text{ 与 }\Xi_+.}
\tag{6.4}
\]

结合 §3，每个 outer cofactor都必须有 non-`3` inert supplier，所以若 `G_Delta` 的 odd common parity由 fixed `31` 或 fixed `179` 吸收，至多只能同步支付一个 outer cofactor；另一个 outer cofactor仍强迫至少一枚与该 fixed target不同的 non-`3` inert prime。

这给 fixed-target old-pool escape 一个新的 unconditional surcharge，不依赖 first/second serial node的选择。

---

## 7. fixed `7` remains the genuine exception

同一个 checker给

\[
\boxed{P_{30}(1)\equiv0\pmod7.}
\tag{7.1}
\]

而 fixed f/descent/height shadow正有 `K≡1 (mod7)`。所以本文不能把 (6.4) 推广到 fixed `7`：它确实仍可能同时落在 outer-pair reuse gate与 descendant common gate上。

因此更新后的 fixed old-pool frontier为：

1. fixed target `31/179`：**不能免费吸收全部 outer parity**，至少再付一枚 distinct non-`3` inert supplier；
2. fixed height `7`：仍是唯一 fixed single-prime reuse exception；
3. source-common与 genuine endpoint-external common kernel仍需继续审计 degree-30 gate或其它 natural-representative约束。

A2 仍为 `待证`。

---

## 8. verification

```bash
uv run python scripts/exact-lift/a2-only/research-checks/crt-descent/check_a2_outer_cofactor_reuse_gate.py
```

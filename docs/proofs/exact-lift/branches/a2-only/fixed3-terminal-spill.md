# A2 fixed `3` 的 third-order spill reduction

> **依赖：** `endpoint-lattice.md` §§16.11–16.12、16.57–16.59；`primitive-reduction.md` §§1–3；历史 descendant chain 中 `spontaneous-crt-descendant-second-order-tail.md`、`spontaneous-crt-descendant-quartic-tail-hierarchy.md` 与 `spontaneous-crt-descendant-third-order-parity-spill.md` 的 canonical formulas。
>
> **严格状态：**本文处理 third-order positive parent carrier 中固定素数 `3` 的首个可能 odd-parity contribution。结论是：在 `Z≡1 mod4` 的两个 odd-`3` endpoint channels 中，只要没有再次命中旧 fixed sheet，则 `v_3(N_63^(3))` 分别精确为 `6` 或 `10`，均为偶数。因此 fixed `3` 不能在 generic sector 中承担 `Q_spill` 的 odd-inert parity。所有逃逸被压回：`3|f`，以及第二通道中的 extra-central `v_3(2K-9)>=3`。本文尚未排除这两个 fixed-sheet exceptions，因此仍不宣称 A2 关闭。

---

## 1. endpoint fixed-`3` dichotomy

在 `Z≡1 mod4` orientation，`endpoint-lattice.md` 已证明

\[
\boxed{
\begin{cases}
v_3(a_3)=1,\quad v_3(a_2)\ge2,\\
\text{or}\\
v_3(a_2)=1,\quad v_3(a_3)\ge2,
\end{cases}}
\tag{1.1}
\]

同时

\[
3\nmid g,
\qquad
3\nmid c_u,
\qquad
3\nmid c_Q,
\qquad
3\nmid\beta.
\tag{1.2}
\]

而 `primitive-reduction.md` 给

\[
\alpha=\omega W_q,
\qquad
H_0=c_uW_q,
\qquad
\beta=S\omega,
\tag{1.3}
\]

其中 `3∤S` 于当前 odd-`3` channels 成立。因此

\[
\boxed{3\nmid\omega.}
\tag{1.4}
\]

又由 (1.1)，原拼接分子

\[
\alpha=TK+a_3
\]

恰含一个 `3`，所以

\[
\boxed{v_3(W_q)=v_3(H_0)=1.}
\tag{1.5}
\]

此外 `endpoint-lattice.md` §16.58 已给

\[
\boxed{3\nmid\widehat{\mathcal T}_2.}
\tag{1.6}
\]

---

## 2. descendant parent 与一个新的 exact source identity

为避免与 endpoint Gaussian factors `X,Y` 混淆，本节把 descendant parent coordinates 记为

\[
\boxed{
X_d:=5^\lambda\mathscr R_{63}^\star,
\qquad
Y_d:=g2^m\widehat{\mathscr D}_{63}.}
\tag{2.1}
\]

则

\[
\widehat{\mathcal T}_2=X_d+Y_d.
\tag{2.2}
\]

历史 descended quotient formula 是

\[
\widehat{\mathscr D}_{63}
=c_u^2\mathscr F_{63},
\tag{2.3}
\]

\[
\mathscr F_{63}
=(2K-9)B_\Delta
-\frac{63}{16}gTK^2,
\tag{2.4}
\]

其中

\[
B_\Delta=g((2K-9)T-a_3)-H_0.
\tag{2.5}
\]

利用

\[
H_0=c_u\frac{TK+a_3}{\omega},
\qquad
f=g\omega+c_u,
\]

可得到本文使用的 exact identity：

\[
\boxed{
\omega B_\Delta
=f((2K-9)T-a_3)
-3c_u(K-3)T.}
\tag{2.6}
\]

证明只是展开：

\[
\begin{aligned}
\omega B_\Delta
&=g\omega((2K-9)T-a_3)-c_u(TK+a_3)\\
&=(f-c_u)((2K-9)T-a_3)-c_u(TK+a_3)\\
&=f((2K-9)T-a_3)-3c_u(K-3)T.
\end{aligned}
\]

这条式子把 fixed-`3` descendant depth 与旧 denominator factor `f` 直接接起来。

---

## 3. `a_2`-shallow channel：generic third parent 的 `3`-depth 精确为 `6`

先固定

\[
\boxed{
v_3(a_2)=1,
\qquad
v_3(a_3)\ge2.}
\tag{3.1}
\]

写

\[
K=3k,
\qquad k\in\mathbf Z_3^\times,
\qquad
s:=(-1)^m\in\{\pm1\}.
\tag{3.2}
\]

此时

\[
v_3(2K-9)=1.
\tag{3.3}
\]

若进一步

\[
\boxed{3\nmid f,}
\tag{3.4}
\]

因为 `g,omega,c_u` 均为 `3`-units，且

\[
f=g\omega+c_u,
\]

模 `3` 两个单位之和非零只可能来自相同 residue，因此

\[
\boxed{c_u\equiv g\omega\pmod3.}
\tag{3.5}
\]

由 (2.6)：第二项含至少 `3^2`，而第一项恰含一个 `3`，所以

\[
v_3(B_\Delta)=1.
\]

更精确地，模 `3` 有

\[
\frac{2K-9}{3}\equiv2k,
\qquad
\frac{B_\Delta}{3}\equiv gk.
\tag{3.6}
\]

(2.4) 的第二项含 `3^4`，因此

\[
\frac{\widehat{\mathscr D}_{63}}9
\equiv2g\pmod3,
\tag{3.7}
\]

进而

\[
\boxed{
\frac{Y_d}{9}
\equiv2s\pmod3.}
\tag{3.8}
\]

另一方面，直接把 `a_2≡a_3≡K≡0 mod3` 代入 primitive additive carrier formula，可得

\[
\widehat{\mathcal T}_2\equiv(-1)^m=s\pmod3.
\tag{3.9}
\]

因 `9|Y_d`，由 (2.2)

\[
\boxed{X_d\equiv s\pmod3.}
\tag{3.10}
\]

现在进入 third-order canonical recursion。写

\[
X_d\equiv x,
\qquad
Y_d=9y,
\qquad
K=3k.
\]

checker 从 exact `G_<,G_>,H_2,H_3` 重建并抽取 `3^6` initial form，得到

\[
\boxed{
\frac{\mathscr N_{63}^{(3)}}{3^6}
\equiv
yk^2(x+s)(2y+sk^2)
\pmod3.}
\tag{3.11}
\]

代入

\[
x=s,\qquad y=2s,\qquad k^2=1
\]
后，三因子均为 units。因此

\[
\boxed{
v_3(\mathscr N_{63}^{(3)})=6.}
\tag{3.12}
\]

所以本通道只要 `3∤f`，fixed `3` 对 third-order positive primitive carrier 的贡献是偶数，不能承担 odd spill parity。

因此唯一逃逸是

\[
\boxed{3\mid f.}
\tag{3.13}
\]

这已经把第一个 odd-`3` channel 完全压回旧 f-denominator sheet。

---

## 4. `a_3`-shallow channel：generic third parent 的 `3`-depth 精确为 `10`

现在固定另一通道

\[
\boxed{
v_3(a_3)=1,
\qquad
v_3(a_2)\ge2.}
\tag{4.1}
\]

写

\[
\zeta=\frac{a_3}{T}=3z,
\qquad z\in\mathbf Z_3^\times,
\]

并抽出 guaranteed `3^2`：

\[
K=9k.
\tag{4.2}
\]

这里 `k mod3` 可以为 `0,1,2`；若 `k=0`，只是说明 `K` 实际深于 `3^2`。

central depth 由

\[
2K-9=9(2k-1)
\]
读取。因此

\[
\boxed{
v_3(2K-9)=2
\iff
k\not\equiv2\pmod3.}
\tag{4.3}
\]

先处于 generic central sector

\[
3\nmid f,
\qquad
v_3(2K-9)=2.
\tag{4.4}
\]

仍由 (3.5) 有 `c_u≡gomega mod3`。由 (2.6)，此时

\[
v_3(B_\Delta)=1,
\]

并从 (2.4) 得

\[
\boxed{v_3(\widehat{\mathscr D}_{63})=3.}
\tag{4.5}
\]

令

\[
y:=\frac{Y_d}{27}\pmod3.
\]

精确 normalized residue 为

\[
\boxed{
y=s(2k-1)z.}
\tag{4.6}
\]

同 §3，仍有

\[
X_d\equiv s\pmod3.
\tag{4.7}
\]

本通道中 checker 对 third recursion 抽取 `3^10` initial form。若

\[
X_d\equiv x,
\qquad
Y_d=27y,
\qquad
K=9k,
\qquad
\zeta=3z,
\]

则

\[
\boxed{
\frac{\mathscr N_{63}^{(3)}}{3^{10}}
\equiv
-y(k^2-k+1)\{z(k+1)-sy\}
\pmod3.}
\tag{4.8}
\]

代入 (4.6)：

\[
z(k+1)-sy
=z\{(k+1)-(2k-1)\}
=z(2-k).
\tag{4.9}
\]

在 generic central sector `k=0` 或 `1`：

\[
k^2-k+1\equiv1,
\qquad
2-k\not\equiv0,
\]

且 `y,z` 均为 units。因此

\[
\boxed{v_3(\mathscr N_{63}^{(3)})=10.}
\tag{4.10}
\]

同样是偶数。

所以第二通道中 fixed `3` 只有两种逃逸：

\[
\boxed{
3\mid f
\quad\text{或}\quad
v_3(2K-9)\ge3.}
\tag{4.11}
\]

第二个条件等价于

\[
K/9\equiv2\pmod3,
\]
即一个真正的 extra-central `3`-adic sheet，而不是新的 terminal coefficient root。

---

## 5. fixed `3` 的 terminal frontier 已缩成两个旧 sheet

合并 §§3–4：在 `Z≡1 mod4` 的全部 odd fixed-`3` endpoint channels 中，若

\[
3\nmid f,
\]

并且第二通道没有额外 central depth，则

\[
\boxed{
v_3(\mathscr N_{63}^{(3)})\in\{6,10\}.}
\tag{5.1}
\]

两者均为偶数。因此 third-order spill theorem 中的 odd-inert supplier若选择 `q=3`，它不可能来自 generic fixed-`3` sector；必须同时命中

\[
\boxed{
3\mid f
\quad\text{或}\quad
v_3(2K-9)\ge3.}
\tag{5.2}
\]

这把旧文的开放项

\[
\text{“Q_spill 的 supplier 可能只是固定 prime 3”}
\]

严格缩成两个已经存在于 proof tree 的 fixed sheets：

1. f-denominator `3`-contact；
2. central `2K-9` extra-depth。

没有新的 moving terminal `3`-branch。

下一步不应继续机械展开 `H_3`；应直接审计 (5.2) 两个 fixed sheets 的 higher `3`-depth，并证明它们在 `N_63^(3)` 中仍只产生偶 parity，或与 endpoint/source identities 冲突。

A2 仍为 `待证`。

---

## 6. verification

```bash
uv run python scripts/exact-lift/a2-only/check_a2_fixed3_terminal_spill.py
```

checker 从 canonical universal descendant cubic、Euclidean quotient与 transported polynomial重建 `G_<,G_>,H_2,H_3`，然后验证 (3.11)、(4.8) 及两个 source-unit substitutions。

# A2 descendant quotient 的 exact `f/G_D` bridge

> **依赖：** `fixed3-terminal-spill.md`；历史 `spontaneous-crt-descended-quotient-orientation.md`；`fixed-prime-descendant-transversality.md`。
>
> **严格状态：**`fixed3-terminal-spill.md` 已把 generic fixed-`3` third-order parity 排除，并把所有逃逸压回 `3|f` 或 extra-central `v_3(2K-9)>=3`。本文证明这两个异常并非独立：它们在 descended quotient `F_63` 中通过一个 exact 两项恒等式耦合。该 bridge 同时给出两条 fixed coefficient 的显式 central forms 与首层 `3`-进深度。本文尚未排除 bridge 上的高阶 cancellation，因此仍不宣称 A2 关闭。

---

## 1. descendant quotient

沿用

\[
\widehat{\mathscr D}_{63}=c_u^2\mathscr F_{63},
\]

\[
\mathscr F_{63}
=(2K-9)B_\Delta-\frac{63}{16}gTK^2,
\tag{1.1}
\]

\[
B_\Delta=g((2K-9)T-a_3)-H_0.
\tag{1.2}
\]

同时

\[
H_0=c_uW_q,
\qquad
W_q=\frac{TK+a_3}{\omega},
\qquad
f=g\omega+c_u.
\tag{1.3}
\]

`fixed3-terminal-spill.md` 已得到

\[
\omega B_\Delta
=f((2K-9)T-a_3)-3c_u(K-3)T.
\tag{1.4}
\]

---

## 2. `已严格完成`：exact `f/G_D` bridge

定义旧 descendant-height gate

\[
\boxed{G_D(K):=11K^2-240K+432}
\tag{2.1}
\]

和新的 coefficient

\[
\boxed{
J_f(K,a_3,T)
:=K^2T-576KT-32Ka_3+1296T+144a_3.}
\tag{2.2}
\]

把 (1.4) 代入 (1.1)，并用

\[
g\omega=f-c_u
\]
整理，得到 exact identity

\[
\boxed{
16\omega\mathscr F_{63}
=fJ_f-3c_uT\,G_D.}
\tag{2.3}
\]

这不是模素数的 resultant，而是全局整数恒等式。于是 `fixed3-terminal-spill.md` 的两个 exceptions

\[
3\mid f,
\qquad
v_3(2K-9)\ge3
\]

现在被放进同一个 descended quotient：前者提高第一项，后者通过 `G_D` 的 central expansion 控制第二项。

---

## 3. central coordinates

令

\[
U:=2K-9,
\qquad
\zeta:=a_3/T.
\]

直接代

\[
K=\frac{U+9}{2}
\]
得到

\[
\boxed{
\frac{4J_f}{T}
=U^2-64U\zeta-1134U-5103,}
\tag{3.1}
\]

\[
\boxed{
4G_D
=11U^2-282U-1701.}
\tag{3.2}
\]

固定系数分解为

\[
5103=3^6\cdot7,
\qquad
1134=2\cdot3^4\cdot7,
\]

\[
1701=3^5\cdot7,
\qquad
282=2\cdot3\cdot47.
\tag{3.3}
\]

特别地，旧 central/descendant transversality 正是 (3.2)。

---

## 4. `a_2`-shallow fixed-`3` channel

固定

\[
v_3(a_2)=1,
\qquad
v_3(a_3)\ge2.
\]

此时

\[
v_3(K)=1,
\qquad
v_3(U)=1.
\]

由 (3.1)，`U^2` 是唯一必然的 depth-2 leading term，所以

\[
\boxed{v_3(J_f)=2.}
\tag{4.1}
\]

写

\[
K=3k,
\qquad k\in\mathbf Z_3^\times.
\]

由 (3.2) 或直接计算：

\[
\frac{G_D}{9}
\equiv k(2k+1)\pmod3.
\tag{4.2}
\]

因此

\[
\boxed{
\begin{cases}
k\equiv2\pmod3&\Longrightarrow v_3(G_D)=2,\\
k\equiv1\pmod3&\Longrightarrow v_3(G_D)\ge3.
\end{cases}}
\tag{4.3}
\]

所以若 `3|f`，(2.3) 的两项从 depth `v_3(f)+2` 与 `1+v_3(G_D)` 开始竞争。fixed `3` 的剩余 odd contribution 必须来自这个明确的 two-term normalized cancellation；不存在第三个 coefficient source。

---

## 5. `a_3`-shallow fixed-`3` channel

固定

\[
v_3(a_3)=1,
\qquad
v_3(a_2)\ge2.
\]

令

\[
h:=v_3(U)\ge2.
\]

当 `h=2,3` 时，(3.1) 中 `U\zeta` 项给

\[
\boxed{v_3(J_f)=h+1,}
\tag{5.1}
\]

而 (3.2) 中 `282U` 项给

\[
\boxed{v_3(G_D)=h+1.}
\tag{5.2}
\]

因此若 `3\nmid f`，(2.3) 的第一项 depth 为 `h+1`，第二项为 `h+2`；不会在首层 cancellation：

\[
\boxed{3\nmid f,\ h\in\{2,3\}
\Longrightarrow
v_3(\mathscr F_{63})=h+1.}
\tag{5.3}
\]

`h=2` 正好恢复 `fixed3-terminal-spill.md` 的 generic descendant depth `3`。`h=3` 则把 extra-central exception 的 descendant depth固定为 `4`；真正待审计的是它进入 `N_63^{(3)}` 后的下一 normalized coefficient，而不是 `F_63` 自身仍有自由 Hensel depth。

---

## 6. revised fixed-`3` frontier

fixed `3` 的 terminal 问题现在可写成：

1. generic `3\nmid f`、central exact-depth sector已经由 `fixed3-terminal-spill.md` 给 third parent even depth `6/10`；
2. `3|f`：由 (2.3) 变成 `fJ_f` 与 `3c_uTG_D` 的单一 normalized collision；
3. `3\nmid f` 且 `v_3(U)=3`：由 (5.3) 已固定 `v_3(F_63)=4`，只需读取 third recursion 的下一 digit；
4. 更深 `U` 最终仍由 (3.1)–(3.2) 的固定系数 `3^6*7`、`3^5*7` 截断，不存在新的 moving polynomial family。

因此不应再把 `3|f` 与 extra-central 当作两棵平行 Hensel tree。下一步应使用 endpoint 的 `eta=1` Gaussian-support 分类，把 odd fixed-`3` orientation压到唯一 `(d,c_Q,k_h,slot)=(2,7,3,-)` 类型后，再在该类型中计算 (2.3) 的 normalized collision。

A2 仍为 `待证`。

---

## 7. verification

```bash
uv run python scripts/exact-lift/a2-only/check_a2_descendant_f_gd_bridge.py
```

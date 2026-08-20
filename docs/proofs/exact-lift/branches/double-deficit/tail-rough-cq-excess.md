# DD tail rough core 的 primitive `Q`-cancellation overflow

> **依赖：** [`tail-rough-d0-allocation.md`](tail-rough-d0-allocation.md)、
> [`gcd-normal-exact-small-factor.md`](gcd-normal-exact-small-factor.md)。
>
> **严格状态：** `已严格完成（non-decimal `d_0` support）`。
>
> 上一文件把第二次 Schmidt 的剩余 rough pool粗略压到
> \[
> C_Q=Q/(b_1,b_2).
> \]
> 本文继续逐 prime剥掉已经由 actual overlap `g_*/v` 支付的 denominator baseline。
> 对 `p` 不整除 10 且 `p|d_0`，写
> \[
> v_p(b_1)=v_p(b_2)=E,
> \qquad v_p(b_3)=j,
> \qquad c=v_p(C_Q).
> \]
> 则
> \[
> v_p(d_0)=E+c-j,
> \]
> 而未被 `g_*/v` 支付的精确 overflow为
> \[
> \boxed{
> x_p=
> \max\bigl(c-j-\min(E,j),0\bigr).
> }
> \]
> 因而真正的 hard rough pool不是整个 `C_Q`，而是 primitive concat cancellation
> 超过 `j+min(E,j)` denominator baseline后的部分。

---

## 1. local ledger

固定

\[
p\nmid10,\qquad p\mid d_0.
\]

`tail-rough-d0-allocation.md` 已证明

\[
\boxed{v_p(b_1)=v_p(b_2)=E.}
\tag{1.1}

记

\[
j:=v_p(b_3),
\qquad
c:=v_p(C_Q),
\qquad
h:=v_p(d_0).
\]

由

\[
Q=(b_1,b_2)C_Q
\]

以及 gcd-normal tail ledger

\[
v_p(Q)=h+j,
\]

得到

\[
\boxed{h=E+c-j>0.}
\tag{1.2}

---

## 2. actual overlap payer 的 exact depth

仍有

\[
\frac{g_*}{v}=\frac\gamma{c_3}.
\]

在当前 prime：

\[
v_p(\gamma)=2E,
\]

而

\[
v_p(c_3)=\max(E,j)-j.
\]

所以

\[
\boxed{
o:=v_p(g_*/v)
=2E-\max(E,j)+j.}
\tag{2.1}

分情况：

\[
\boxed{
o=
\begin{cases}
E+j,&E\ge j,\\
2E,&j>E.
\end{cases}}
\tag{2.2}

`o` 是已经真实出现在

\[
F_-=r(u+2v)\,a(g_*/v)
\]

中的 payer，不应再次记为 loss。

---

## 3. unpaid depth 的闭式

定义 local unpaid depth

\[
\boxed{x:=\max(h-o,0).}
\tag{3.1}

若 `E>=j`：

\[
h-o=(E+c-j)-(E+j)=c-2j.
\]

而 `min(E,j)=j`，所以

\[
x=\max(c-j-\min(E,j),0).
\]

若 `j>E`：

\[
h-o=(E+c-j)-2E=c-j-E,
\]

且 `min(E,j)=E`，得到同一式。

因此统一有

\[
\boxed{
 x_p
=\max\bigl(c-j-\min(E,j),0\bigr).
}
\tag{CQ-excess-local}

特别地：

- `E=j=0` 时
  \[
  x_p=c,
  \]
  整个 `C_Q` cancellation都是 hard excess；
- `E>0` 或 `j>0` 时，至少 `j+min(E,j)` 层 cancellation被 denominator
  baseline / actual overlap吸收；
- 若
  \[
  c\le j+\min(E,j),
  \]
  则该 prime对第二次 Schmidt不留下任何 unpaid `d_0` rough depth。

---

## 4. canonical excess integer

令

\[
D_{0,\rm rough}:=\operatorname{core}_{10}(d_0).
\]

逐 `p|D_{0,rough}` 定义

\[
X_Q:=\prod_{p\mid D_{0,\rm rough}}p^{x_p}.
\tag{4.1}

则从 `x_p=max(h-o,0)` 立即得到

\[
\boxed{
D_{0,\rm rough}
\mid
\frac{g_*}{v}\,X_Q.
}
\tag{4.2}

且

\[
\boxed{X_Q\mid C_Q.}
\tag{4.3}

所以 `tail-rough-d0-allocation.md` 的 coarse payer

\[
D_{0,\rm rough}\mid(g_*/v)C_Q
\]

可以严格加强成 `(4.2)`。

---

## 5. 第二次 Schmidt 的真正 loss

令

\[
R_x:=\operatorname{core}_{10}\bigl((u+2v)/(u,2)\bigr).
\]

第二次 Schmidt theorem给

\[
\log R_x+\log D_{0,\rm rough}\ge S-o(S).
\]

而 `R_x` 与 `g_*/v` 都已经进入 actual `F_-`。使用 `(4.2)`：

\[
\boxed{
\log R_x+\log(g_*/v)
\ge
S-\log X_Q-o(S).
}
\tag{5.1}

因此 post-tail branch reoptimization 唯一真正需要继续收费的是

\[
\boxed{X_Q,}
\]

而不是 `d_0` 或 `C_Q` 全体。

`X_Q` 的 primewise 定义说明它只由**超过 denominator baseline 的 primitive
prefix concat cancellation**组成。

---

## 6. prime-flow interpretation

对 `p|X_Q` 必有

\[
c>j+\min(E,j).
\]

因此 `Q/h_{12}` 在 `p` 处发生的 cancellation depth不仅超过第三 denominator
深度 `j`，还超过 prefix/tail 可共同支付的 `min(E,j)`。

在最危险的 baseline-free 情形

\[
E=j=0,
\]

这就是纯粹的

\[
B_1 10^{m_2}+B_2\equiv0\pmod{p^c}
\]

型 source cancellation；它与旧 canonical `U`-prime channel完全一致。

所以非-canonical side branches若携带显著 denominator common depth，`X_Q` 会自动
小于原 `C_Q`；真正可能保持正线性 loss的只剩接近 baseline-free 的 source
cancellation sheet。

---

## 7. 状态摘要

- **`已严格完成`**：`CQ-excess-local`、canonical `X_Q`、
  `D0_rough | (g_*/v) X_Q`。
- **`结构压缩`**：second-Schmidt post-tail loss只剩 primitive cancellation overflow
  `X_Q`。
- **`待证`**：对 `X_Q` 建立 source/Gaussian cancellation height bound；用其完成
  side-branch reoptimization并判断 global `6.215109...` 升级；DD absolute height。

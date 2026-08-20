# DD tail-root × decimal remainder 的 2-adic phase lock

> **依赖：** [`genuine-tail-root-orientation-lock.md`](genuine-tail-root-orientation-lock.md) 的 global `Tail-root-original`、`frontier.md` 的 terminal primitive overlap / exact decimal remainder / prefix polarization、[`pairmax-fixed-a12-crt.md`](pairmax-fixed-a12-crt.md) 使用的 one-channel unit ledger。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。将 exact top residue 与 tail-root linearization 联立，可消去 `A_12,a_3`，得到模 `10^d` 的 W-only congruence
> \[
> \mathscr T R_0+\eta g_0U\gamma W\equiv0\pmod{10^d}.
> \]
> 对其做 2-adic valuation，并与 unified discriminant 的 2-adic valuation比较，严格推出
> \[
> H=2m+o(S),
> \qquad
> v_2(W)=m+o(S).
> \]
> 再由 `X=2^HZ` 与 `log X=2S+o(S)` 得
> \[
> \log Z=z_*S+o(S),
> \qquad z_*=0.308883577618\ldots,
> \]
> 恰与 `q_c` 的 frontier height相同。
>
> 本文仍不单独关闭 terminal frontier，但新增一个此前未显式记录的 source-height lock。

---

## 1. tail-root 与 decimal carry 消去 prefix

统一 tail-root original identity为

\[
\boxed{
\mathscr T a_3
=\kappa G^2 10^dA_{12}
+\eta(\kappa+G)W,
}
\tag{1.1}

其中

\[
\mathscr T
=\frac{\kappa^2(\kappa+2G)}{10^m}.
\tag{1.2}

exact carry为

\[
\boxed{
g_0Ua_3
=g_0B10^dVA_{12}-\Sigma R_0.}
\tag{1.3}

把 `(1.1)` 乘 `g_0U`，模 `10^d`：

\[
g_0U\mathscr T a_3
\equiv
\eta g_0U(\kappa+G)W
\pmod{10^d}.
\tag{1.4}

把 `(1.3)` 乘 `mathscr T`，同样模 `10^d`：

\[
g_0U\mathscr T a_3
\equiv
-\mathscr T\Sigma R_0
\pmod{10^d}.
\tag{1.5}

因此

\[
\mathscr T\Sigma R_0
+\eta g_0U(\kappa+G)W
\equiv0\pmod{10^d}.
\tag{1.6}

terminal primitive overlap给

\[
\boxed{\kappa+G=\gamma\Sigma.}
\tag{1.7}

又 `Sigma` 是 10-adic unit：

- `V=X-Y` 为 odd；
- `Y=5^TU` 为 odd；
- 因此 `X=V+Y` 为 even；
- `Sigma=X+Y` 为 odd；
- 模 `5`，`Sigma≡X` 且 `X` 为 5-unit。

所以

\[
(\Sigma,10)=1.
\]

可从 `(1.6)` 在模 `10^d` 中约去 `Sigma`：

\[
\boxed{
\mathscr T R_0
+\eta g_0U\gamma W
\equiv0\pmod{10^d}.}
\tag{Tail-decimal}

---

## 2. terminal 2-adic primitive overlap

写

\[
F:=5^T.
\]

terminal overlap为

\[
\boxed{
\kappa=2\gamma FU,
\qquad
G=\gamma V,
\qquad
\kappa+2G=2\gamma X,
}
\tag{2.1}

其中

\[
(UVZ,10)=1,
\qquad
X=2^HZ.
\]

令

\[
g_2:=v_2(\gamma).
\]

则

\[
\boxed{v_2(\kappa)=1+g_2,}
\tag{2.2}

\[
\boxed{v_2(G)=g_2,}
\tag{2.3}

\[
\boxed{v_2(\kappa+2G)=1+g_2+H.}
\tag{2.4}

所以

\[
\boxed{
v_2(\mathscr T)
=H-m+3+3g_2.}
\tag{2.5}

one-channel asymptotic还给

\[
\log\gamma=o(S),
\]

因为

\[
G=\gamma V,
\quad
\log G=S+o(S),
\quad
\log V=S+o(S).
\]

故

\[
\boxed{g_2=o(S).}
\tag{2.6}

同时

\[
\log g_0=\log R_0=o(S),
\qquad
v_2(U)=0.
\tag{2.7}

---

## 3. `Q` 与 `N_12` 的 2-depth 都只有 `o(S)`

prefix polarization给

\[
m_1=o(S),
\qquad
n_2=o(S),
\qquad
m_2=S+o(S).
\]

one-channel给

\[
b_2=C_L\cdot10^{o(S)}
\]

按 logarithmic height理解，而 `C_L` 为 odd prime-to-10 main core。因此

\[
\boxed{v_2(b_1)=v_2(b_2)=v_2(a_2)=o(S).}
\tag{3.1}

### 3.1 `Q`

\[
Q=b_1 10^{m_2}+b_2.
\]

第一项的 2-depth为

\[
m_2+v_2(b_1)=S+o(S),
\]

第二项只有 `o(S)`；sufficiently large frontier上两者 valuation不同，所以

\[
\boxed{v_2(Q)=v_2(b_2)=o(S).}
\tag{3.2}

### 3.2 `N_12`

写

\[
x=a_1b_2,
\qquad
y=a_2b_1,
\qquad
\mathcal N_{12}=x^2+y^2.
\]

由 `(3.1)` 与 `n_2,m_1=o(S)`：

\[
\boxed{v_2(y)=o(S).}
\]

对任意整数 `x,y` 有 elementary sum-of-two-squares valuation：

\[
v_2(x^2+y^2)
\le2\min(v_2(x),v_2(y))+1.
\]

故

\[
\boxed{v_2(\mathcal N_{12})=o(S).}
\tag{3.3}

---

## 4. unified discriminant 精确给 `v_2(W)=H/2+o(S)`

DD discriminant identity为

\[
\boxed{
W^2
=(\kappa G\mathscr C)^2
-Q^2\mathcal N_{12}\kappa(\kappa+2G),
}
\tag{4.1}

其中 DD coefficient

\[
\boxed{\mathscr C=10^dA_{12}.}
\tag{4.2}

第一项 2-depth至少为

\[
\begin{aligned}
v_2((\kappa G\mathscr C)^2)
&\ge2\bigl[(1+g_2)+g_2+d\bigr]\\
&=2d+2+4g_2\\
&=7S+o(S),
\end{aligned}
\tag{4.3}

因为 frontier

\[
\boxed{d=3.5S+o(S).}
\tag{4.4}

第二项利用 §§2--3：

\[
\begin{aligned}
v_2(Q^2\mathcal N_{12}\kappa(\kappa+2G))
&=2v_2(Q)+v_2(\mathcal N_{12})\\
&\quad +(1+g_2)+(1+g_2+H)\\
&=\boxed{H+o(S).}
\end{aligned}
\tag{4.5}

另一方面

\[
X=2^HZ>0,
\qquad
X<\Sigma,
\]

且 decimal remainder analysis已经给

\[
\log\Sigma=2S+o(S).
\]

因为 `Z>=1`：

\[
H\log_{10}2
\le2S+o(S),
\]

即

\[
\boxed{
H\le\frac{2}{\log_{10}2}S+o(S)
=6.643856189774\ldots S+o(S).}
\tag{4.6}

所以 `(4.5)` 与 `(4.3)` 存在严格线性 gap：

\[
H+o(S)<7S+o(S).
\]

两项 2-adic valuations最终不同；对整数差，valuation等于较小者。因此

\[
2v_2(W)=H+o(S),
\]

即

\[
\boxed{v_2(W)=\frac H2+o(S).}
\tag{W2}

---

## 5. `Tail-decimal` 强迫两项 2-depth相等

对 `(Tail-decimal)` 两项记

\[
r:=v_2(\mathscr T R_0),
\qquad
s:=v_2(g_0U\gamma W).
\]

由 `(2.5)`--`(2.7)`：

\[
\boxed{r=H-m+o(S).}
\tag{5.1}

由 `(W2)`：

\[
\boxed{s=\frac H2+o(S).}
\tag{5.2}

而 `(Tail-decimal)` 要求

\[
2^d\mid \mathscr T R_0+\eta g_0U\gamma W.
\]

先排除

\[
\min(r,s)\ge d.
\]

若成立，则特别有

\[
s\ge d,
\]

故

\[
\frac H2\ge3.5S-o(S),
\]

即

\[
H\ge7S-o(S),
\]

与 `(4.6)` 矛盾。

因此

\[
\boxed{\min(r,s)<d.}
\tag{5.3}

若 `r!=s`，则 two-adic valuation of the sum等于 `min(r,s)<d`，又与 `2^d` divisibility矛盾。

所以必须

\[
\boxed{r=s.}
\tag{5.4}

代入 `(5.1)`--`(5.2)`：

\[
H-m=\frac H2+o(S).
\]

因此

\[
\boxed{H=2m+o(S).}
\tag{H-lock}

并由 `(W2)`：

\[
\boxed{v_2(W)=m+o(S).}
\tag{W2-lock}

---

## 6. `Z` 与 `q_c` 高度精确对齐

由

\[
\Sigma=X+Y,
\qquad
V=X-Y,
\]

有

\[
X=\frac{\Sigma+V}{2}.
\]

frontier

\[
\log\Sigma=2S+o(S),
\qquad
\log V=S+o(S),
\]

所以

\[
\boxed{\log X=2S+o(S).}
\tag{6.1}

又

\[
X=2^HZ,
\]

故

\[
\log Z
=2S-H\log_{10}2+o(S).
\]

使用 `(H-lock)` 与

\[
\frac mS\to2.808883577618\ldots:
\]

\[
\begin{aligned}
\frac{\log Z}{S}
&=2-2(2.808883577618\ldots)\log_{10}2+o(1)\\
&=\boxed{0.308883577618\ldots+o(1).}
\end{aligned}
\]

所以

\[
\boxed{
\log Z=z_*S+o(S),
\qquad
z_*=0.308883577618\ldots.}
\tag{Z-lock}

而已有

\[
\log q_c=z_*S+o(S).
\]

因此得到新的 exact leading-height symmetry：

\[
\boxed{
\log Z=\log q_c+o(S).}
\tag{Z-qc-lock}

---

## 7. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`Tail-decimal`、`v_2(Q)=o(S)`、`v_2(N_12)=o(S)`、`W2`、`H-lock`、`W2-lock`、`Z-lock`。
- **`新 frontier 约束`**：`H=2m+o(S)` 与 `log Z=log q_c+o(S)`。
- **`待证`**：利用 `Z/q_c` 同高度与 denominator/source orientation 构造新的 strict source relation；5-adic projection的剩余 unit phase；DD frontier emptiness。

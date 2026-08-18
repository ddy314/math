# A2 prime-source continuation

> **依赖：** `endpoint-lattice.md` §§16.45–16.73，尤其使用 (16.419)、(16.420)、(16.423)–(16.425)、(16.428)–(16.433)。
>
> **严格状态：**本文继续压缩 `A_2` reflection endpoint 的 non-`3` inert-prime 开放核。固定素数 `11,23` 不再需要作为两条独立的 Hensel 例外保留：`11` special branch 被强制吸收到 `c_Q` 的 plus-side square allocation，`23` special branch 被强制吸收到真实 sphere height `H_0`。本文仍**不宣称 A2 全局关闭**。

---

## 1. 统一记号

沿用 `endpoint-lattice.md` 的 endpoint 记号：

\[
D=g2^m5^d,
\qquad
N=3D-C=c_-^2X,
\qquad
c_Q=c_-c_+,
\]

\[
q\mid DK-N,
\qquad
W_q:=\frac{DK-N}{q}>0,
\]

并有全局正加性商

\[
2c_uW_q=c_+^2Y+5^\lambda c_-^2X.
\tag{1.1}
\]

对任意
\[
r\ne3,\qquad r\equiv3\pmod4,\qquad r\mid W_q,
\]
§16.73 已证明

\[
\boxed{r\nmid c_Qc_ugXY}
\tag{1.2}
\]

以及

\[
\boxed{
\left(\frac{N_0}{r}\right)=-1,
\qquad
v_r(W_q)=v_r(H_0).
}
\tag{1.3}
\]

以下只研究 §16.71 尚保留的两个 fixed-prime budgets。

---

## 2. `已严格完成`：固定 `11` 例外必进入 `c_+`，且没有 `W_q` 深度

考虑 §16.71 的 special `11` branch：

\[
11^e\Vert q,
\qquad
11^e\mid\mathscr L_{23},
\qquad
K\equiv9\pmod{11}.
\tag{2.1}
\]

记

\[
a:=v_{11}(c_Q),
\qquad
n_{11}=a+e,
\]

以及

\[
A_{11}:=KD-N,
\qquad
B_{11}:=TN+2a_3D.
\]

§16.71 的精确预算是

\[
\boxed{
v_{11}(B_{11})+2v_{11}(A_{11})=2(a+e).}
\tag{2.2}
\]

### 2.1 middle factor 至少含一份 `11`

由全局整除 (16.423)，

\[
q\mid A_{11},
\]

故

\[
N\equiv KD\equiv9D\pmod{11}.
\tag{2.3}
\]

另一方面 `11\mid\mathscr L_{23}` 等价于

\[
2a_3+9T\equiv0\pmod{11}.
\tag{2.4}
\]

所以

\[
B_{11}=TN+2a_3D
\equiv9TD-9TD
\equiv0\pmod{11}.
\]

即

\[
\boxed{v_{11}(B_{11})\ge1.}
\tag{2.5}
\]

### 2.2 `11` 必须整除 `c_Q`

若 `a=0`，则由 `q\mid A_{11}` 有

\[
v_{11}(A_{11})\ge e.
\]

代入 (2.2) 与 (2.5)：

\[
2e
= v_{11}(B_{11})+2v_{11}(A_{11})
\ge1+2e,
\]

矛盾。因此

\[
\boxed{11\mid c_Q.}
\tag{2.6}
\]

这已经说明 special `11` branch 不能存在于 `c_Q`-free generic 层；它必然属于旧 square-side overlap。

### 2.3 `W_q` 在 `11` 处必为单位

若再有 `11\mid W_q`，因为 `11\equiv3\pmod4` 且 `11\ne3`，(1.2) 会给出

\[
11\nmid c_Q,
\]

与 (2.6) 矛盾。故

\[
\boxed{v_{11}(W_q)=0.}
\tag{2.7}
\]

由
\[
A_{11}=qW_q
\]
立即得到

\[
\boxed{v_{11}(A_{11})=e.}
\tag{2.8}
\]

再代回 (2.2)：

\[
\boxed{v_{11}(B_{11})=2a.}
\tag{2.9}
\]

所以 §16.71 中看起来独立的 `11`-进 middle/third budget 已完全刚化：third factor 只含 `q` 自身的 `11^e`，middle factor 恰含 `c_Q` 中 `11`-primary part 的平方深度。

### 2.4 `11`-primary allocation 被强制定向到 `c_+`

由 (2.3)，`D` 是 `11`-进单位且 `K\equiv9`，所以

\[
11\nmid N.
\]

而

\[
N=c_-^2X.
\]

因此

\[
11\nmid c_-.
\]

结合 `c_Q=c_-c_+` 与 (2.6)，得到

\[
\boxed{
v_{11}(c_+)=v_{11}(c_Q)=a,
\qquad
v_{11}(c_-)=0.}
\tag{2.10}
\]

这也解释了 (2.9) 的偶深度。事实上由 reflection factor equality

\[
H_0+Y_3=c_+^2Y
\]
以及

\[
B_{11}
=TN+2a_3D
=2^m5^d(H_0+Y_3),
\tag{2.11}
\]

而 non-`3` inert prime `11` 不进入 `Y`，恰有

\[
v_{11}(B_{11})=2v_{11}(c_+)=2a.
\]

因此 fixed `11` budget 没有留下新的 Hensel phase；它只是既有 plus-side square allocation 的另一种投影。

综上：

\[
\boxed{
\begin{array}{c}
11^e\Vert q,\ 11^e\mid\mathscr L_{23},\ K\equiv9\pmod{11}
\\[1mm]
\Longrightarrow
\\[1mm]
v_{11}(c_+)=v_{11}(c_Q)>0,
\quad
v_{11}(W_q)=0,
\quad
v_{11}(TN+2a_3D)=2v_{11}(c_Q).
\end{array}}
\tag{2.12}
\]

所以 `11` 不再需要作为独立的 endpoint-external / fixed-Hensel 通道。它仍可能出现在纯 prefix gcd
\[
\gcd(q,K^2-26),
\]
中，但 special overlap 的额外深度已经全部被 `c_+^2` 吸收。

---

## 3. `已严格完成`：固定 `23` 例外强迫 `23\nmid c_Q`，并精确等于 height channel

考虑 §16.71 的 special `23` branch：

\[
23^e\Vert q,
\qquad
23^e\mid\mathscr L_{23},
\qquad
2K\equiv9\pmod{23}.
\tag{3.1}
\]

仍记

\[
a:=v_{23}(c_Q),
\qquad
n_{23}=a+e.
\]

§16.71 的精确预算为

\[
\boxed{
v_{23}(KD-N)
=n_{23}+v_{23}(TN+a_3D).}
\tag{3.2}
\]

而 §16.73 的精确 height identity 是

\[
TN+a_3D=2^m5^dH_0.
\tag{3.3}
\]

因为 `23\nmid10`，记

\[
h:=v_{23}(H_0)=v_{23}(TN+a_3D).
\]

另一方面 `KD-N=qW_q`，所以 (3.2) 给出

\[
e+v_{23}(W_q)=a+e+h,
\]
即

\[
\boxed{v_{23}(W_q)=a+h.}
\tag{3.4}
\]

若 `a>0`，则 (3.4) 强迫 `23\mid W_q`。但 `23\equiv3\pmod4`、`23\ne3`，(1.2) 随即强迫 `23\nmid c_Q`，矛盾。因此

\[
\boxed{v_{23}(c_Q)=0.}
\tag{3.5}
\]

代回 (3.4)：

\[
\boxed{v_{23}(W_q)=v_{23}(H_0).}
\tag{3.6}
\]

于是 fixed `23` budget 也不再产生独立例外：

- 若 `23\nmid H_0`，则 `23\nmid W_q`，special `23` root 没有 endpoint-external 深度；
- 若 `23\mid H_0`，则它已经精确属于 §16.73 的 height channel，并满足
  \[
  \boxed{\left(\frac{N_0}{23}\right)=-1.}
  \tag{3.7}
  \]

所以

\[
\boxed{
\text{fixed }23\text{ Hensel exception}
\subseteq
\text{existing }H_0\text{ prime-source channel}.}
\tag{3.8}
\]

---

## 4. `已严格完成`：special `23` height carrier 删除十个 `M mod 22` 类

当 (3.1) 且 `23\mid H_0` 时，还可以把 (3.7) 变成纯十进制长度条件。

令

\[
t:=10^{M-1}\pmod{23}.
\tag{4.1}
\]

由 (3.5) 与 `23\mid q`，

\[
Q_0=c_Qq\equiv0\pmod{23}.
\]

reflection source split 给出

\[
Q_0=5^M+2^mgc_u,
\]
故

\[
2^mgc_u\equiv-5^M\pmod{23}.
\tag{4.2}
\]

又

\[
b_2=2^{M+m+1}c_ug,
\qquad
C_0=\frac{9b_2}{2},
\]
所以由 (4.2)

\[
\frac{b_2}{2}
=2^M(2^mgc_u)
\equiv-10^M\pmod{23},
\]
从而

\[
\boxed{C_0\equiv-9\cdot10^M\equiv2t\pmod{23}.}
\tag{4.3}
\]

另一方面

\[
K=10P,
\qquad
P=9\cdot10^{M-1}+a_2.
\]

special root `2K\equiv9 (mod 23)` 给出

\[
20P\equiv9\pmod{23}.
\]

因为 `20^{-1}\equiv15 (mod 23)`，

\[
P\equiv20\pmod{23},
\]
于是

\[
\boxed{a_2\equiv20-9t\pmod{23}.}
\tag{4.4}
\]

因此 prefix Gaussian norm

\[
N_0=C_0^2+a_2^2
\]
满足

\[
\boxed{
N_0
\equiv
(2t)^2+(20-9t)^2
\equiv16t^2+8t+9
\pmod{23}.}
\tag{4.5}
\]

其判别式为

\[
8^2-4\cdot16\cdot9
\equiv17\pmod{23},
\]
而 `17` 是模 `23` 的非平方，因此 (4.5) 对 `t\ne0` 从不为零。

`10` 在 `F_23^×` 中的阶为 `22`。逐 `M-1 mod 22` 的精确有限检查，(3.7) 等价于

\[
\boxed{
M-1\equiv
0,1,7,8,9,11,12,14,16,18,19,21
\pmod{22}.}
\tag{4.6}
\]

亦即

\[
\boxed{
M\equiv
0,1,2,8,9,10,12,13,15,17,19,20
\pmod{22}.}
\tag{4.7}
\]

所以 special `23` 的真正 height-carrying 子支只允许 `22` 个长度类中的 `12` 个；其余 `10` 个被严格排除。这个有限 residue 检查由
`scripts/exact-lift/a2-only/check_a2_prime_source.py`
复核。

---

## 5. 更新后的开放核

§16.73 末尾把 non-`3` inert-prime frontier 列成：

1. 两个 pure-prefix gcd
   \[
   \gcd(q,K^2-26),
   \qquad
   \gcd(f,\Psi_f);
   \]
2. fixed `11,23` Hensel lifts；
3. endpoint-external sphere-height channel
   \[
   r\mid H_0,
   \qquad
   \left(\frac{N_0}{r}\right)=-1.
   \]

本文的 §§2–3 说明第 2 项可以从独立开放列表删除：

\[
\boxed{
\begin{aligned}
11\text{ special}
&\Longrightarrow
11\mid c_+,\quad11\nmid W_q,
\quad\text{仅留下 pure-prefix/c_Q overlap};\\
23\text{ special}
&\Longrightarrow
23\nmid c_Q,
\quad v_{23}(W_q)=v_{23}(H_0),
\quad\text{完全并入 height channel}.
\end{aligned}}
\tag{5.1}
\]

因此当前 non-`3` 无界核心可更紧地写成

\[
\boxed{
\text{two pure-prefix gcds}
\quad+\quad
\text{one sphere-height prime-source channel}.}
\tag{5.2}
\]

其中 `23` height 子支还附带 (4.7) 的 `M mod 22` 限制。

下一步最有价值的目标已经很明确：对一般
\[
r\equiv3\pmod4,
\qquad
r\mid H_0,
\qquad
\left(\frac{N_0}{r}\right)=-1
\]
把 sphere/high-factor equality 与 `C` 的自然代表 (16.101)–(16.104) 联立，证明 `v_r(H_0)` 在 `W_q` 中只能贡献偶深度；并平行处理两个 pure-prefix gcd 达到 saturation 深度后的 parity。继续把 `11,23` 当作独立例外分别 Hensel 展开已经没有新增信息。
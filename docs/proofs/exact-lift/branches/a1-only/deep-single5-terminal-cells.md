# A1 minimal diagonal: exact terminal forms for the remaining single-5 cells

> 日期：2026-08-22。
>
> 依赖：`deep-single5-decimal-height-collapse.md`、`diagonal.md`、`deep-denominator-ledger.md`。
>
> 范围：`k=g>=32` minimal diagonal，且已经使用 decimal-height synchronization 关闭 double-deep、single-2 与 single-5 strict-low / middle-high bands。

状态：**本文 reduction 均已严格完成。**

---

## 1. Cell I 实际为空

旧 reduction 的 Cell I 为

\[
w\in\{1,3\},
\qquad
\lambda_2=0,
\qquad
B=k+1.
\]

此时

\[
e=v_2(w)=0,
\qquad
n_2=v_2(N)\in\{0,1\},
\]

且

\[
a:=v_2(\kappa)=2k.
\]

在 `E<F` branch 中已有

\[
v_2(W)=2k.
\]

又因为 `G,C` 都是 2-units，且

\[
v_2(\kappa+G)=0,
\]

形式根 numerator

\[
X_\sigma
=\kappa G^2C+\sigma(\kappa+G)W
\]

的两个 summands 各自**恰好**具有 valuation `2k`。除去 `2^{2k}` 后二者都是奇数，所以无论 `sigma=+1` 还是 `-1`，其和/差都是偶数：

\[
\boxed{v_2(X_\sigma)\ge2k+1.}
\tag{1}
\]

另一方面

\[
v_2(\kappa+2G)=1,
\]

所以 raw denominator

\[
Y=\kappa^2(\kappa+2G)
\]

满足

\[
v_2(Y)=4k+1.
\]

因此 reduced 2-denominator depth 至多

\[
\boxed{d_2\le2k.}
\tag{2}
\]

但 Cell I 有

\[
v_5(L)=B+k=2k+1.
\]

5-side completion height 至少 `2k+1`，而 2-side completion height由 `v_2(L)=k` 与 (2) 给

\[
H_2\le2k.
\]

违反 exact decimal-height synchronization。故

\[
\boxed{\text{Cell I is empty}.}
\tag{3}
\]

因此 fixed-height single-5 只剩 Cell II。

---

## 2. Cell II 唯一类型

Cell II 为

\[
\boxed{
(z,w)=(1,4),
\qquad
\lambda_2=1,
\qquad
B=k+1.
}
\tag{4}
\]

此时

\[
L=2^{k-1}5^{2k+1},
\qquad
M=h,
\]

并且 gap identity 是

\[
\boxed{
2h=5^{k+1}T N_0-\gamma,
\qquad T=10^k.
}
\tag{5}
\]

其中 `(h,10)=1`，所以第一项被 `2^k` 整除而右侧差恰为 `2*odd`。故

\[
\boxed{v_2(\gamma)=1.}
\tag{6}
\]

`deep-single5-decimal-height-collapse.md` 已证明必要的 prefix 5-depth 只可能是

\[
\boxed{
v_5(N)=k+1
\quad\text{or}\quad
v_5(N)\ge2k+1.
}
\tag{7}

下面把这个条件完全写成 `N_0` 的 Hensel 条件。

---

## 3. Cell II 的 prefix norm 在高 5-adic 精度下只剩 `X^2+16`

minimal diagonal 的显式 prefix 为

\[
a_1
=100T^3+igl(10(5-z-w)+1\bigr)T+N_0-1,
\]

\[
a_2=10T^2-z,
\qquad
b_1=10T^2-w,
\]

\[
N=a_1^2+(a_2b_1)^2.
\]

在 `(z,w)=(1,4)` 中系数

\[
10(5-z-w)+1=1.
\]

所以

\[
a_1=100T^3+T+N_0-1.
\]

因为

\[
v_5(100T^3)=3k+2>2k+1,
\]

有

\[
a_1\equiv T+N_0-1\pmod{5^{2k+1}}.
\]

另一方面

\[
(a_2b_1)
=(10T^2-1)(10T^2-4)
=100T^4-50T^2+4.
\]

其中

\[
v_5(50T^2)=2k+2>2k+1,
\]

故

\[
a_2b_1\equiv4\pmod{5^{2k+1}}.
\]

定义

\[
\boxed{X:=T+N_0-1.}
\tag{8}
\]

于是得到 exact high-precision prefix normal form

\[
\boxed{
N\equiv X^2+16
\pmod{5^{2k+1}}.
}
\tag{9}

因此 (7) 精确分成：

### resonance

\[
\boxed{
v_5(X^2+16)=k+1;}
\tag{10}
\]

### high branch

\[
\boxed{5^{2k+1}\mid X^2+16.}
\tag{11}

---

## 4. Hensel root form

固定一个兼容 Hensel 系统 `iota_m`，满足

\[
\iota_m^2\equiv-1\pmod{5^m}.
\]

因为 `4` 是 5-unit，(10)-(11) 等价于：

### resonance

\[
X\equiv\pm4\iota_{k+1}\pmod{5^{k+1}},
\]

但对应 lift 不满足模 `5^{k+2}`；

### high branch

\[
\boxed{
X\equiv\pm4\iota_{2k+1}\pmod{5^{2k+1}}.
}
\tag{12}

又

\[
10^{k-1}\le N_0<10^k=T,
\]

所以

\[
1.1T-1\le X<2T-1.
\tag{13}

而

\[
5^{2k+1}>T
\]

对所有 `k>=1` 成立。因此 high branch 的每个 sign 在区间 (13) 中至多给出一个 `X`，即：

\[
\boxed{
\text{Cell II high branch 对每个 }k\text{ 至多两个 }N_0\text{ 候选}.}
\tag{14}

这不是全局有限性，但把 high branch 从 `9*10^{k-1}` 个 prefix integers 压到两个显式 Hensel residues。

---

## 5. Cell III：删除 `kappa`

现在处理旧 Cell III：

\[
\lambda_2=2k-1,
\]

\[
 v_2(\kappa+2G)
=B+k+e-1,
\qquad e=v_2(w).
\tag{15}

写

\[
G=2^e g,
\qquad g\text{ odd},
\]

以及 supply complement

\[
M_c=QG/h=2^e m,
\qquad m\text{ odd}.
\]

由 single-5 `kappa` formula：

\[
\kappa
=\frac{5^BT^2M_c}{2^{2k-1}}
=2^{e+1}5^{B+2k}m.
\]

而

\[
2G=2^{e+1}g.
\]

故

\[
v_2(\kappa+2G)
=e+1+v_2\bigl(5^{B+2k}m+g\bigr).
\]

由于

\[
\frac mg
=\frac{M_c}{G}
=\frac Qh,
\]

且 `g,h` 均为奇数，

\[
v_2\bigl(5^{B+2k}m+g\bigr)
=
v_2\bigl(5^{B+2k}Q+h\bigr).
\]

把它与 (15) 比较，得到 Cell III 的 exact divisor congruence：

\[
\boxed{
 v_2\!\left(h+5^{B+2k}Q\right)
=B+k-2.
}
\tag{16}

等价地

\[
\boxed{
h\equiv-5^{B+2k}Q
\pmod{2^{B+k-2}},}
\tag{17}
\]

但该同余不能提升到 `2^{B+k-1}`。

同时 `h` 仍必须是原 minimal-diagonal legal odd supply：

\[
\boxed{
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1,}
\tag{18}
\]

其中 `b_1` 侧只能选取允许的 `1 mod4` whole prime-power blocks。

所以 Cell III 已不再需要 `kappa,W` 描述；它是一个纯 divisor-congruence terminal：

\[
\boxed{
\begin{gathered}
h\in\mathcal H_{k,w},\\
v_2(h+5^{B+2k}Q)=B+k-2,\\
v_5(N)=B\text{ or }v_5(N)\ge B+k.
\end{gathered}}
\tag{19}

---

## 6. 当前 single-5 前沿

Cell I 已关闭。因此 surviving single-5 只有：

1. **Cell II resonance**：`(z,w)=(1,4)`, `B=k+1`, `lambda_2=1`, 且 (10)；
2. **Cell II high**：同一 fixed cell，且 (11)/(12)，每层至多两个 Hensel prefix candidates；
3. **Cell III**：满足 exact divisor congruence (16)-(19)。

下一步优先攻击 Cell II resonance 的 `k+1`-deep Hensel class；Cell III 则应把 (17) 与 `h=qs` 的 Q-side / b1-side whole-block restrictions 联用。

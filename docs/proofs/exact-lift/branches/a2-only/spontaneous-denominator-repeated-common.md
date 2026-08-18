# A2 repeated spontaneous 与 saturated additive denominator 的交集

> **依赖：** `spontaneous-tangent-decimal.md`、`spontaneous-denominator-common.md`、`endpoint-lattice.md` §§16.56–16.70。
>
> **严格状态：**本文处理最危险的交界：同一个 genuine non-`3` inert prime 一方面使 spontaneous branch 在真实 decimal length 上 repeated，另一方面又承担 additive denominator saturation。结论是 q-side 第一层即为空；f-side 只出现固定 prime `523` 的一个 genuine 第一层模板，但该模板不能提升到 `523^2`。因此 repeated spontaneous 与 saturated additive denominator 不存在 surviving unbounded Hensel tree。本文不排除 simple spontaneous/denominator common roots，也不宣称 A2 全局关闭。

---

## 1. repeated + saturation 固定唯一 K-center

`spontaneous-tangent-decimal.md` 的原始 repeated tangent 是

\[
\boxed{
L_{\rm tan}=9(TK-a_3)-55T.}
\tag{1.1}
\]

additive denominator odd excess 只有完整 saturation

\[
\boxed{p^e\Vert qf,
\qquad
p^e\mid 2a_3+9T.}
\tag{1.2}
\]

在第一层，把

\[
a_3/T\equiv-9/2
\]
代入 `L_tan=0`：

\[
9\left(K+\frac92\right)-55=0.
\]
所以任何 repeated+saturated common candidate 都必须满足

\[
\boxed{18K-29\equiv0\pmod p.}
\tag{1.3}
\]

这条线与此前 `Psi_f` 子通道出现的 `18K-29` 相同，但本文不假设 `Psi_f` 作为额外输入；它直接来自 repeated tangent 与 saturation。

---

# 2. f-saturation 本身还有一个此前未显式使用的 sphere quadratic

设 `p|f` 且进入 additive saturation。使用 normalized

\[
x=\frac{b_2}{10^M},
\quad
\tau=10^{-M},
\quad
s=9+y,
\]

\[
\bar w=\frac{b_3}{T10^M},
\qquad
\bar\zeta=\frac{a_3}{T10^M}.
\]

f-line 给

\[
\bar w\equiv-\frac{x+2}{2},
\tag{2.1}
\]
而 saturation 给

\[
\bar\zeta\equiv-\frac92\tau.
\tag{2.2}
\]

把 (2.1)–(2.2) 直接代入 exact sphere，不使用 `Omega_sp=0`，得到

\[
(2025x^2+y^2)(x+2)^2
\equiv
400x^2s(s-9\tau)
\pmod p.
\tag{2.3}
\]

乘回原始 decimal blocks

\[
B=b_2=Nx,
\qquad
Q=N(x+2),
\qquad
K=Ns,
\qquad N=10^M,
\]
以及

\[
N_0=\frac{N^2}{100}(2025x^2+y^2),
\]
(2.3) 精确化为 first-layer congruence

\[
\boxed{
Q^2N_0
\equiv
4B^2K(K-9)
\pmod p.}
\tag{2.4}

另一方面 saturation 与 additive contact 已由 `spontaneous-denominator-common.md` 给

\[
\Psi_f
=B^2(K^2-26)-Q^2N_0
\equiv0\pmod p.
\tag{2.5}

代入 (2.4)：

\[
K^2-26-4K(K-9)=0,
\]
即

\[
\boxed{
\mathcal P_f(K)
:=3K^2-36K+26
\equiv0\pmod p.}
\tag{2.6}

所以每个 saturated additive f-carrier 在 first layer 都落在一个固定 quadratic 上；source variables、third block 和 Gaussian allocation 全部消失。

其判别式为

\[
\boxed{
\operatorname{Disc}(\mathcal P_f)
=36^2-12\cdot26
=984=2^3\cdot3\cdot41.}
\tag{2.7}

因此 genuine non-`3` inert prime `p=3 mod 4` 不可能使 `P_f` 出现 repeated root：唯一 odd ramified prime `41` 满足

\[
41\equiv1\pmod4.
\]

于是

\[
\boxed{
\text{所有 genuine inert saturated f-carrier 的 K-root 都 simple。}}
\tag{2.8}

---

## 3. `审计 / no-go`：旧 f-prefix character 在该 quadratic 上自动成立

(2.6) 等价于

\[
\boxed{K^2-26=4K(K-9).}
\tag{3.1}

而 sphere identity (2.4) 已给

\[
\left(\frac{N_0}{p}\right)
=\left(\frac{K(K-9)}p\right)
\tag{3.2}
\]
对 genuine units 成立。

旧 f-saturation prefix character 是

\[
\left(\frac{K^2-26}{p}\right)
=\left(\frac{N_0}{p}\right).
\tag{3.3}

由 (3.1)，两边之比就是 `4`，所以 (3.3) 在 common sphere quadratic 上自动成立。它是 principal-square shadow，不是第二个 independent obstruction。

因此后续不能再尝试用旧 f-prefix Legendre character 排除 (2.6) 的 roots。

---

# 4. q-side repeated+saturated common 第一层为空

q-side additive saturation 已有 pure prefix root

\[
\boxed{K^2-26\equiv0\pmod p.}
\tag{4.1}

与 repeated center (1.3) 联立，把

\[
K=\frac{29}{18}
\]
代入：

\[
K^2-26
=-\frac{7583}{324}.
\]

`7583` 为素数且

\[
7583\equiv3\pmod4.
\]
所以唯一 genuine inert candidate 是

\[
\boxed{p=7583.}
\tag{4.2}

但 q-angle contact 还必须满足 `x=-2, Delta_0=0`。由

\[
\Delta_0(-2,y)=8100-18y-y^2,
\]
其 discriminant 为

\[
324\cdot101.
\]
故 first-layer y-root 必须满足

\[
\left(\frac{101}{p}\right)=1.
\tag{4.3}

对 `p=7583`，因为 `101=1 mod 4`，二次互反律给

\[
\left(\frac{101}{7583}\right)
=
\left(\frac{7583}{101}\right)
=\left(\frac8{101}\right).
\]
而 `101=5 mod 8`，所以

\[
\left(\frac2{101}\right)=-1,
\qquad
\left(\frac8{101}\right)=-1.
\]
与 (4.3) 矛盾。因此

\[
\boxed{
\text{repeated spontaneous}\cap q\text{-saturation common}
=\varnothing
\quad\text{already mod }p.}
\tag{4.4}

---

# 5. f-side 只剩固定 p=523

将 repeated center

\[
K=29/18
\]
代入 f-sphere quadratic (2.6)：

\[
\mathcal P_f(29/18)
=-\frac{2615}{108}
=-\frac{5\cdot523}{108}.
\]

对 genuine non-`5` inert prime，唯一候选为

\[
\boxed{p=523.}
\tag{5.1}

并且

\[
523\equiv3\pmod4.
\]

所以 repeated+saturated f-common shell 已从任意 moving prime 压成一个 fixed prime。

---

## 6. `有限 exact 证书`：p=523 恰有一个 genuine first-layer state

使用 f-side common system

\[
\Delta_0=0,
\]

\[
\mathcal L_f^{\rm sat}
=200x^2(s-9\tau)-y(x+2)^2=0,
\]

\[
\mathcal P_f^{\rm pref}
=100x^2(s^2-26\tau^2)
-(x+2)^2(2025x^2+y^2)=0,
\]
再加入 repeated center

\[
18s-29\tau=0.
\]

在 `F_523` 中完整枚举得到唯一 genuine solution

\[
\boxed{(x,y,\tau)=(115,215,121)\pmod{523}.}
\tag{6.1}

对应

\[
\boxed{
\begin{aligned}
x+2&=117,\\
s=9+y&=224,\\
2025x^2+y^2&=88,\\
A_{\rm sp}&=509,
\end{aligned}
\qquad\pmod{523}}
\tag{6.2}

全部为单位。恢复 third/source normalized values：

\[
r_s=-\frac{2x}{x+2}=302,
\qquad
\bar w=203,
\qquad
\bar\zeta=-\frac92\tau=240
\pmod{523},
\]
也全部为 genuine units。

---

## 7. `有限 exact 证书`：唯一 p=523 state 无 p^2 lift

记四个整数多项式

\[
F_1=\Delta_0,
\]

\[
F_2=\mathcal L_f^{\rm sat},
\]

\[
F_3=\mathcal P_f^{\rm pref},
\]

\[
F_4=18s-29\tau.
\]

在 first-layer point

\[
(x_0,y_0,\tau_0)=(115,215,121)
\]
写

\[
x=x_0+523X,
\quad
y=y_0+523Y,
\quad
\tau=\tau_0+523Z.
\]

模 `523^2` 的必要条件是 augmented linear system

\[
J(x_0,y_0,\tau_0)
\begin{pmatrix}X\\Y\\Z\end{pmatrix}
\equiv
-\begin{pmatrix}
F_1/p\\F_2/p\\F_3/p\\F_4/p
\end{pmatrix}
\pmod{523}.
\tag{7.1}

exact row reduction 得到最后一行

\[
\boxed{[0\ \ 0\ \ 0\mid27].}
\tag{7.2}

因为 `27 != 0 mod 523`，系统不相容。因此

\[
\boxed{
\text{唯一 genuine }523\text{-state 不存在 }523^2\text{ lift}.}
\tag{7.3}

---

## 8. repeated denominator/common shell 已关闭

综合 §§4–7：

\[
\boxed{
\begin{array}{c|c|c}
\text{channel}&\text{first-layer candidate}&\text{higher lift}\\ \hline
q&7583&\text{first layer already impossible}\\
f&523&\text{unique state, no }523^2\text{ lift}
\end{array}}
\tag{8.1}

所以

\[
\boxed{
\text{repeated spontaneous}
\cap
\text{saturated additive denominator}
\text{ has no surviving unbounded Hensel branch}.}
\tag{8.2}

这真正删除了一类 singular common carrier。剩余 denominator parity problem 只涉及 **simple q/f roots** 与 equal-depth normalized cancellation；后续不应再保留 repeated decimal branch 作为 denominator common 的无界机制。

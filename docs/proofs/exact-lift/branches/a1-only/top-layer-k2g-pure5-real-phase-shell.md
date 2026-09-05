# A1 top layer: `k=2g` pure-5 real phase shell

> 日期：2026-08-22。
>
> 依赖：`top-layer-k2g-gap-smallL-collapse.md`、`top-layer-k2g-prime-shape-collapse.md` 与原 normalized exact-lift 方程。
>
> 范围：
> \[
> d=2,\quad r=s=1,\quad g\ge1,\quad k=2g,\quad J=0,
> \]
> primitive pruning 后只剩
> \[
> (z,w)=(1,1),(1,3).
> \]

状态：**已严格完成。** 本文把旧的
\[
0<(10^g-\rho)10^{2g}<95
\]
收紧为两个宽度仅 `3/5` 的显式实相位壳层。

---

## 1. 显式 prefix

令
\[
H:=10^g.
\]
由 `k=2g,J=0,z=1`，有
\[
b_1=10H^4-w,
\qquad b_2=H,
\]
\[
a_2=10H^4-1,
\]
\[
a_1=H(100H^4+41-10w),
\]
其中
\[
w\in\{1,3\}.
\]
再令
\[
Q_0:=10b_1+1,
\qquad Q=HQ_0,
\qquad G=Hb_1,
\qquad D=H^2Q_0,
\]
\[
C=a_1(10H^4)+a_2,
\qquad
N=(a_1H)^2+(a_2b_1)^2.
\]

真实第三块正规化为
\[
\eta:=\frac{a_3}{10^n},
\qquad
\frac1{10}\le\eta<1,
\]
以及
\[
\rho=\frac ML,
\qquad
\frac H{10}\le\rho<H.
\]
定义 scaled tail gap
\[
\boxed{
t:=(H-\rho)H^2.
}
\tag{1}
\]
前文 ultrathin gap 已给
\[
\boxed{0<t<95.}
\tag{2}
\]

---

## 2. exact-lift 的清分母多项式

normalized exact-lift 方程为
\[
\frac{C+\eta}{D+\rho}
=
\sqrt{\frac N{G^2}+\left(\frac\eta\rho\right)^2}.
\]
平方并清分母：
\[
G^2\rho^2(C+\eta)^2
=(D+\rho)^2(N\rho^2+G^2\eta^2).
\tag{3}
\]
代入
\[
\rho=H-\frac t{H^2}
\]
并乘 `H^8`。定义
\[
F_w(H,\eta,t)
:=H^8\Bigl[
G^2\rho^2(C+\eta)^2
-(D+\rho)^2(N\rho^2+G^2\eta^2)
\Bigr].
\tag{4}
\]
真实 candidate 必须满足
\[
\boxed{F_w(H,\eta,t)=0.}
\tag{5}
\]

直接整数展开得到 `H` 次数恰为 30，并且最高两项为
\[
\boxed{
\begin{aligned}
F_w={}&
200000(-5\eta^2+10t+40w-339)H^{30}\\
&+200000(\eta-5)H^{29}+R_w(H,\eta,t),
\end{aligned}
}
\tag{6}
\]
其中 `R_w` 的 `H` 次数至多 28。

该展开与以下全部余项界由 exact-arithmetic certificate

`scripts/exact-lift/a1-only/research-checks/top-layer/check_a1_k2g_pure5_real_phase_shell.py`

逐系数核验；脚本只使用整数/有理数 SymPy 运算，不使用浮点判定。

---

## 3. `F_w` 对 `t` 严格递增

对 (6) 求 `t` 导数。`H^30` 的主项恰为
\[
2,000,000H^{30},
\]
而 `H^29` 项的导数为零。

对整个旧可行盒
\[
H\ge10,
\qquad
\frac1{10}\le\eta<1,
\qquad
0<t<95,
\]
逐单项取绝对值并用 `H^{-1}\le1/10`，certificate 给出
\[
\frac{|\partial_tR_1|}{H^{30}}<945519,
\]
\[
\frac{|\partial_tR_3|}{H^{30}}<910317.
\]
因此两型均有
\[
\boxed{\partial_tF_w>0.}
\tag{7}
\]
所以对固定 `H,eta,w`，方程 (5) 至多有一个 `t` 根；只需在两个显式端点定号。

---

## 4. `w=1` 的端点定号

现在
\[
w=1.
\]

### lower endpoint `t=299/10`

(6) 的最高项变成
\[
-1,000,000\eta^2H^{30}
\le-10,000H^{30}.
\]
又因 `eta<1`，实际上只需用较弱的
\[
200000(\eta-5)H^{29}
\le-800,000H^{29}
\le-80,000H^{30}.
\]
certificate 对 `H^{28}` 以下全部项给
\[
\frac{|R_1(H,\eta,299/10)|}{H^{30}}<10697.
\]
故
\[
\frac{F_1(H,\eta,299/10)}{H^{30}}
<-10000-80000+10697<0.
\]
即
\[
\boxed{F_1(H,\eta,299/10)<0.}
\tag{8}
\]

### upper endpoint `t=305/10`

最高项为
\[
2,000,000\left(\frac35-\frac{\eta^2}{2}\right)H^{30}
>200,000H^{30}.
\]
而
\[
200000(\eta-5)H^{29}>-1,000,000H^{29}\ge-100,000H^{30}.
\]
certificate 给
\[
\frac{|R_1(H,\eta,305/10)|}{H^{30}}<85231.
\]
所以
\[
\frac{F_1(H,\eta,305/10)}{H^{30}}
>200000-100000-85231>0.
\]
即
\[
\boxed{F_1(H,\eta,305/10)>0.}
\tag{9}
\]

由 (7)--(9)，真实根必须满足
\[
\boxed{
\frac{299}{10}<t<\frac{305}{10}
\qquad(w=1).
}
\tag{10}

---

## 5. `w=3` 的端点定号

现在
\[
w=3.
\]
完全同理。

在
\[
t=219/10
\]
时，最高项仍恰为
\[
-1,000,000\eta^2H^{30}\le-10,000H^{30},
\]
`H^29` 项至多为 `-80,000H^30`，而 certificate 给
\[
\frac{|R_3(H,\eta,219/10)|}{H^{30}}<7768.
\]
所以
\[
\boxed{F_3(H,\eta,219/10)<0.}
\tag{11}
\]

在
\[
t=225/10
\]
时，最高项严格大于 `200,000H^30`，`H^29` 项大于 `-100,000H^30`，而
\[
\frac{|R_3(H,\eta,225/10)|}{H^{30}}<62514.
\]
所以
\[
\boxed{F_3(H,\eta,225/10)>0.}
\tag{12}
\]

因此
\[
\boxed{
\frac{219}{10}<t<\frac{225}{10}
\qquad(w=3).
}
\tag{13}

---

## 6. pure-5 的整数相位形式

当前唯一未关闭的 prime shape 为
\[
L=5^b,
\qquad b\ge2\text{ 为偶数}.
\]

令
\[
A:=HL-M\in\mathbf Z_{>0}.
\]
则
\[
H-\rho=\frac AL,
\qquad
t=\frac{AH^2}{5^b}.
\tag{14}
\]

对 `g>=2` 的 pure-5 2-adic resonance，已有
\[
v_2(M)=2g-1,
\]
而 `HL` 的 2-depth 为 `g`，故
\[
v_2(A)=g.
\]
写
\[
A=2^ga_0,
\qquad a_0\in\mathbf Z_{>0}.
\]
由 `H^2=2^{2g}5^{2g}`：
\[
\boxed{
t=\frac{a_0\,2^{3g}}{5^{b-2g}}.}
\tag{15}
\]

因此 (10),(13) 分别化为
\[
\boxed{
\frac{299}{10}
<
\frac{a_0\,2^{3g}}{5^{b-2g}}
<
\frac{305}{10}
\qquad(w=1),
}
\tag{16}
\]
以及
\[
\boxed{
\frac{219}{10}
<
\frac{a_0\,2^{3g}}{5^{b-2g}}
<
\frac{225}{10}
\qquad(w=3).
}
\tag{17}

所以 pure-5 terminal 不再只是 `0<t<95`；其 integer gap numerator `a0` 被压进一个相对宽度约 2--3% 的单一 interval，并且还必须同时满足 2-adic resonance congruence 与 divisor recovery。

---

## 7. 当前前沿

截至本文，`k=2g,J=0` 只剩
\[
\boxed{L=5^b,\quad b\ge2\text{ even},}
\]
并且必须同时满足：

1. (16) 或 (17) 的宽度 `3/5` 实相位壳层；
2. pure-5 的 high-2 resonance；
3. `M|10^gQG` 与 exact decimal recovery；
4. global `kappa` square。

下一步应把 (16)-(17) 与 high-2 residue class 联立，优先证明 `b`/`g` 有全局有限高度；剩余小层再用 exact divisor certificate 关闭。

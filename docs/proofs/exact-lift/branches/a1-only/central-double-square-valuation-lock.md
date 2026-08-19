# A1 minimal diagonal: central double-square valuation lock

> 日期：2026-08-19。依赖 `central-pell-local-squareclass.md` 与 `central-gap-2adic.md`。
> 当前统一范围为 `k=g>=26`。

central sector 现在同时存在两个彼此独立的必要平方条件：

1. odd-supply Euclidean descent 的判别式平方
   \[
   Y^2=A_U L^2+B_U,
   \qquad L=10^k/c;
   \]
2. 原 rational-contact 的整数平方核
   \[
   R=K-2(10^k\rho)Q\mathcal N.
   \]

本文把两者局部联立。核心新结论是：第一个平方不仅要求 `B_U` 属于 `Q_2^2 cap Q_5^2`，还精确决定整数中心 `N_0` 的 `2/5` 赋值；再代入第二个平方已有的局部 residue table，可把若干 central families 的 `t=U-U_0` 赋值压成绝对有限集合。

状态：**已严格完成。**

---

## 1. 记号

固定 surviving central type-gap `(z,w,Gamma)`。令

\[
c=2^{v_2(\Gamma)}5^{v_5(\Gamma)},
\qquad r=\Gamma/c,
\qquad \gcd(r,10)=1,
\]

\[
C_0=w(10w-1),
\qquad L=10^k/c.
\]

由 `central-pell-local-squareclass.md`，定义

\[
U_0=10c\Gamma(20w-1),
\qquad t=U-U_0>0.
\]

则

\[
\boxed{B_U=-4C_0rt.}
\tag{1}
\]

同时 central supply quadratic 为

\[
C_0N_0^2-ULN_0+1000c^4r^2L^2+rt=0.
\tag{2}
\]

其判别式为 `Y^2`，故二次公式给出

\[
\boxed{2C_0N_0=UL\pm Y.}
\tag{3}
\]

下面只使用赋值，因此根号符号无关。

---

## 2. `UL` 比 `Y` 深得多

已有统一界

\[
v_2(L)=k-v_2(c)\ge21,
\qquad
v_5(L)=k-v_5(c)\ge25.
\tag{4}
\]

又所有 surviving families 满足

\[
0<|B_U|<4\cdot10^{11}.
\]

若 Pell 判别式有解，则 `B_U` 是 `Q_2`、`Q_5` 平方，且由于

\[
Y^2\equiv B_U\pmod{2^{2v_2(L)}},
\qquad
Y^2\equiv B_U\pmod{5^{2v_5(L)}},
\]

而 `v_p(B_U)` 远小于相应模深，得到

\[
\boxed{v_p(Y)=\frac12v_p(B_U),\qquad p=2,5.}
\tag{5}
\]

数值上 `|B_U|<4e11<2^39`，故 `v_2(Y)<=19<21`；同理 `5^17>4e11`，故 `v_5(Y)<=8<25`。

所以在 (3) 中

\[
v_p(UL)>v_p(Y),
\]

严格不同赋值，因而

\[
\boxed{v_p(2C_0N_0)=v_p(Y).}
\tag{6}
\]

---

## 3. `t` 精确决定 `N_0` 的 2/5 赋值

写

\[
a=v_2(t),
\qquad b=v_5(t).
\]

因为 `r` 与 `10` 互素，而

\[
C_0\in\{9,38,87,156\}
\]

均不被 `5` 整除，由 (1)：

\[
v_2(B_U)=2+v_2(C_0)+a,
\]

\[
v_5(B_U)=b.
\]

代入 (5)-(6)：

\[
1+v_2(C_0)+v_2(N_0)
=1+\frac{v_2(C_0)+a}{2},
\]

从而

\[
\boxed{
v_2(N_0)=\frac{a-v_2(C_0)}2.
}
\tag{7}
\]

五进则直接得到

\[
\boxed{
v_5(N_0)=\frac b2.
}
\tag{8}
\]

所以此前的 local-square parity

\[
a\equiv v_2(C_0)\pmod2,
\qquad b\equiv0\pmod2
\]

只是 (7)-(8) 的影子；事实上还必须满足非负性以及原 contact square 对 `N_0` residue 的全部限制。

特别地，`w=2,4` 时由 `gcd(a_1,b_1)=1` 已知 `N_0` 为偶数，因此

\[
\boxed{
w=2:\ a\ge3\text{ 且为奇数},
}
\tag{9}
\]

\[
\boxed{
w=4:\ a\ge4\text{ 且为偶数}.
}
\tag{10}
\]

---

## 4. 与原 contact square 的稳定局部核联立

对任意固定 `m<=k`，原 contact square 在 `p=2,5` 上都有稳定核

\[
\boxed{
R\equiv
(zw)^2
+2\Gamma(1-10w)
\left((N_0-1)^2+(zw)^2\right)
\pmod{p^m}.}
\tag{11}
\]

因此可在固定小模上精确枚举哪些 `v_p(N_0)` 仍可能使 `R` 为平方。

附带脚本使用

\[
2^{12}=4096,
\qquad5^6=15625
\]

做完整 residue enumeration。若 `N_0=0 mod p^m` 本身已不允许，则自动排除所有更深 `v_p(N_0)>=m`，所以表中的有限 valuation set 是严格的，不是截断实验。

---

## 5. even-`w` 的二进深度大量变成绝对有限

把 (7) 与 mod `2^12` contact-square table 联立，得到：

\[
\boxed{
\begin{array}{c|c}
(z,w,\Gamma)&v_2(t)\\ \hline
(1,2,30)&\{3,7,9\}\\
(1,2,38)&\{3,7\}\\
(3,2,22)&\{3,7\}\\
(3,2,30)&\{3,5\}\\
(3,2,38)&\{3,5\}\\
(1,4,24)&\{4,6\}
\end{array}}
\tag{12}
\]

剩下三个 even-`w` families 的 contact 2-adic square 在 `N_0=0` 的深类仍可 lift，因此这里只保留基线：

\[
\boxed{
(1,2,32),(3,2,32):\quad v_2(t)=3,5,7,\ldots,
}
\tag{13}
\]

\[
\boxed{
(1,4,26):\quad v_2(t)=4,6,8,\ldots.
}
\tag{14}
\]

对 odd `w`，`v_2(C_0)=0`，所以 `v_2(t)=2v_2(N_0)`。已有 central contact table 还给出：当 `Gamma=2 mod4` 时 `N_0` 必偶，故这些 families 至少满足

\[
\boxed{\Gamma\equiv2\pmod4\Longrightarrow v_2(t)\ge2\text{ 且为偶数}.}
\tag{15}
\]

---

## 6. 五进也出现固定深度坍缩

把 (8) 与 mod `5^6` 的 contact-square table 联立，得到以下严格有限结果：

\[
\boxed{
\begin{array}{c|c}
(z,w,\Gamma)&v_5(t)\\ \hline
(1,1,34)&\{0\}\\
(1,1,36)&\{0,2\}\\
(1,1,38)&\{0\}\\
(3,2,38)&\{0\}\\
(1,4,24)&\{0\}\\
(1,4,26)&\{0,2\}
\end{array}}
\tag{16}
\]

也就是说例如

\[
(1,4,24):
\qquad
v_2(t)\in\{4,6\},
\qquad
v_5(t)=0.
\tag{17}
\]

这一 family 的 `t` 已经完全离开 2/5 深尾；只剩一个 2-adic unit class 与其余奇素数部分。

其余 type-gap 若 `N_0=0` 是 contact square 的合法 `5`-adic limit，则本文不虚构上界，只保留 `v_5(t)` 为非负偶数的 Pell local-square 条件。

---

## 7. 当前意义

central 的两个平方条件现在真正耦合起来：

- supply Pell square 决定 `N_0` 的精确 2/5 valuation；
- contact square 再限制这些 valuation 是否能存在。

因此进入 generalized Pell / primitive-divisor 阶段之前，至少六个 even-`w` families 的 2-adic `t` 深度、六个 families 的 5-adic `t` 深度已经变成绝对有限集合。

后续 central 证书应按 `(v_2(t),v_5(t))` 的这些真实 surviving cells 分流，而不再只使用较弱的 parity squareclass。
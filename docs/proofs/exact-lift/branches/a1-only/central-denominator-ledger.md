# A1-only Central Denominator Ledger

> 本文件是细粒度研究记录的机械归并账本。各来源的标题、正文和证明状态原样保留；账本中的局部闭合、有限证书或降级路线均不表示该分支或主不存在性命题已经关闭。

## 来源索引

- [`central-crossing-sharp.md`](#source-central-crossing-sharp)
- [`central-double-square-valuation-lock.md`](#source-central-double-square-valuation-lock)
- [`central-gap-2adic.md`](#source-central-gap-2adic)
- [`central-gap-sign-collapse.md`](#source-central-gap-sign-collapse)
- [`central-modular-exhaustion.md`](#source-central-modular-exhaustion)
- [`central-pell-local-squareclass.md`](#source-central-pell-local-squareclass)
- [`central-supply-pell-normal-form.md`](#source-central-supply-pell-normal-form)

<a id="source-central-crossing-sharp"></a>

> 整合来源：`central-crossing-sharp.md`

# A1 minimal diagonal: sharp bound for the unique central sign crossing

> 日期：2026-08-19。依赖 `central-gap-sign-collapse.md` 与 `central-supply-pell-normal-form.md`。
> 当前统一范围为 `k=g>=26`。

`central-gap-sign-collapse.md` 中唯一没有固定正/负 leading sign 的 surviving family 是

\[
\boxed{(z,w,\Gamma)=(3,1,22).}
\]

旧安全界只记录

\[
N_0/10^k<0.251.
\]

本文利用当前真正前沿 `k>=26` 后极小的 normalized remainder，把它收紧到

\[
\boxed{
\frac{N_0}{10^k}<0.250261,
}
\]

并传入 central Pell descent，得到新的绝对 `U` 下界

\[
\boxed{U\ge3,867,967.}
\]

状态：**已严格完成。**

---

## 1. crossing leading polynomial

令

\[
T=10^k,
\qquad \sigma=N_0/T.
\]

该 family 的 contact integer square kernel 满足

\[
R=10000F(\sigma)T^{10}+\operatorname{Rem},
\]

其中

\[
\boxed{F(\sigma)=\sigma^2-240\sigma+60.}
\tag{1}
\]

且旧精确 coefficient audit 给出

\[
\boxed{|
\operatorname{Rem}|
\le101834561\,T^9.}
\tag{2}
\]

当前 `k>=26`，所以

\[
\frac{|\operatorname{Rem}|}{T^{10}}
\le\frac{101834561}{10^{26}}
<1.019\cdot10^{-18}.
\tag{3}
\]

---

## 2. `0.250261` 已经严格进入负区

取

\[
\sigma_0=\frac{250261}{10^6}.
\]

精确代入 (1)：

\[
F(\sigma_0)
=-9.431879\ldots\times10^{-6}.
\]

因此

\[
10000F(\sigma_0)<-0.0943.
\]

另一方面 `F'(sigma)=2sigma-240<0` 在当前 decade 上严格成立，所以若

\[
\sigma\ge\sigma_0,
\]

则

\[
10000F(\sigma)T^{10}
\le-0.0943T^{10}.
\]

这与 (3) 相比有超过 `10^16` 的安全余量，因此

\[
R<0,
\]

不可能是整数平方。

故 exact candidate 必须满足

\[
\boxed{\sigma<0.250261.}
\tag{4}
\]

---

## 3. 传入 Pell descent 的单调主函数

本 family 有

\[
w=1,
\quad C_0=9,
\quad\Gamma=22,
\quad c=2,
\quad r=11.
\]

central Pell note 使用

\[
L=T/c,
\qquad s=N_0/L=c\sigma.
\]

所以 (4) 给

\[
\boxed{s<0.500522.}
\tag{5}
\]

而 Euclidean descent 中已严格证明

\[
U>f(s),
\qquad
f(s)=C_0s+\frac{1000c^4r^2}{s}.
\tag{6}
\]

并且 `f` 在整个允许区间严格递减。由 (5)：

\[
U>f(0.500522).
\]

精确有理数计算为

\[
f(0.500522)
=\frac{44000051243192099}{11375500000}
=3867966.3525\ldots
\]

所以整数 `U` 必满足

\[
\boxed{U\ge3,867,967.}
\tag{7}
\]

相比此前只由 coarse decade 得到的

\[
U>968018,
\]

低端被删除了约三百万个整数。

---

## 4. 对 `t=U-U_0` 的直接结果

这里

\[
U_0=10c\Gamma(20w-1)
=8360.
\]

所以

\[
\boxed{t=U-U_0\ge3,859,607.}
\tag{8}
\]

另一方面原 k-independent upper window 不变，故该 crossing family 后续的 local-square / Pell 搜索应从 (7)-(8) 开始，不再扫描旧的 `[~0.96M,~9.68M]` 全窗。

---

<a id="source-central-double-square-valuation-lock"></a>

> 整合来源：`central-double-square-valuation-lock.md`

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

---

<a id="source-central-gap-2adic"></a>

> 整合来源：`central-gap-2adic.md`

# A1 minimal diagonal: central-gap 2-adic collapse

> 日期：2026-08-19。依赖 `gap-denominator-normal-form.md` 与 rational-contact square identity。
> 当前统一前沿可取 `k=g>=26`。

central denominator sector 已知

\[
\Gamma:=10^k(N_0-\rho)\in\{16,17,\ldots,39\},
\]

且

\[
B:=10^k\rho=N_0 10^k-\Gamma\in\mathbf Z.
\]

本文把 rational-contact square identity 模 `64/256`，得到：

- `w=1,3` 时
  \[
  \boxed{\Gamma\in\{16,18,20,22,24,26,28,30,32,34,36,38\};}
  \]
  且 `Gamma=2 mod 4` 时 `N_0` 必为偶数；
- `w=2` 时
  \[
  \boxed{\Gamma\in\{16,22,30,32,38\};}
  \]
- `w=4` 时
  \[
  \boxed{\Gamma\in\{24,26\}.}
  \]

因此六个 prefix 类型原先 `6*24=144` 个 central type-gap 组合被压到

\[
3\cdot12+2\cdot5+1\cdot2=\boxed{48}.
\]

状态：**已严格完成。**

---

## 1. representation-independent integer square

统一判别平方可写成

\[
V^2=K-2\rho D\mathcal N,
\]

其中

\[
D=10^kQ.
\]

central sector 中 `B=10^k rho` 为整数，因此

\[
\boxed{
R:=K-2BQ\mathcal N\in\mathbf Z,
\qquad V^2=R.
}
\tag{1}
\]

若有 exact candidate，则 `R` 必为整数平方。

注意这里不需要把 `B` 解释成原始第三块分母；它只是由 `rho` 定义出的整数。因而结论与实际 `ell` 无关。

---

## 2. 模 `2^m` 的稳定核

对任何固定 `m<=k`，所有含 `10^k` 或更高次十进制幂的 prefix 项在模 `2^m` 下消失。特别地对当前 `k>=26`，可安全使用 `m=6,8`。

minimal diagonal 数据给出

\[
G=b_1\equiv-w,
\qquad
C\equiv-z,
\]

所以

\[
\boxed{K\equiv(zw)^2\pmod{2^m}.}
\tag{2}
\]

同时

\[
Q\equiv1-10w\pmod{2^m}.
\tag{3}
\]

又

\[
a_1\equiv N_0-1,
\qquad
a_2b_1\equiv zw,
\]

故

\[
\boxed{
\mathcal N\equiv(N_0-1)^2+(zw)^2
\pmod{2^m}.}
\tag{4}
\]

最后

\[
B=N_0 10^k-\Gamma\equiv-\Gamma\pmod{2^m}.
\tag{5}
\]

代入 (1)：

\[
\boxed{
R\equiv
(zw)^2
+2\Gamma(1-10w)
\left((N_0-1)^2+(zw)^2\right)
\pmod{2^m}.}
\tag{6}
\]

这是 central-gap 的统一 2-adic square kernel。

---

## 3. odd `w`：所有 odd `Gamma` 消失

取 `w in {1,3}`。此时 `zw` 为奇数，所以模 `8`

\[
(zw)^2\equiv1,
\qquad 1-10w\text{ 为奇数}.
\]

若 `N_0` 偶，则 `(N_0-1)^2+1=2 mod 8`，所以当 `Gamma` 为奇数时

\[
R\equiv1+4\equiv5\pmod8,
\]

不是平方剩余。

若 `N_0` 奇，则 `(N_0-1)^2+1` 为奇数，odd `Gamma` 给

\[
R\equiv3\text{ 或 }7\pmod8,
\]

同样不是平方。

因此

\[
\boxed{
w\in\{1,3\}\Longrightarrow\Gamma\text{ 必为偶数}.}
\tag{7}
\]

结合 `16<=Gamma<=39`：

\[
\boxed{
\Gamma\in\{16,18,20,22,24,26,28,30,32,34,36,38\}.}
\tag{8}
\]

再看 `Gamma=2 mod 4`。若 `N_0` 奇，则 (6) 模 `8` 给 `R=5 mod 8`；所以

\[
\boxed{
 w\in\{1,3\},\quad \Gamma\equiv2\pmod4
 \Longrightarrow N_0\equiv0\pmod2.}
\tag{9}
\]

---

## 4. `w=2`：模 `32` 只剩五个 gap

当 `w=2`，`b_1` 为偶数。由 `gcd(a_1,b_1)=1`，`a_1` 为奇数，因此

\[
\boxed{N_0\text{ 为偶数}.}
\tag{10}
\]

把 (6) 模 `32`，并枚举 `N_0 mod 32` 的偶数类与整数平方剩余，可得到且仅得到

\[
\boxed{
\Gamma\in\{16,22,30,32,38\}.}
\tag{11}
\]

这一集合对 `z=1` 与 `z=3` 相同。

模 `64` 还给出 residue class：

- `(z,w)=(1,2)`：
  - `Gamma=22` 时 `N_0=4,6 mod 8`；
  - `Gamma=30,38` 时 `N_0=0,2 mod 8`；
  - `Gamma=16,32` 只要求 `N_0` 偶。
- `(z,w)=(3,2)`：
  - `Gamma=22` 时 `N_0=0,2 mod 8`；
  - `Gamma=30,38` 时 `N_0=4,6 mod 8`；
  - `Gamma=16,32` 只要求 `N_0` 偶。

这些 residue 条件可在后续 decimal-supply/resultant 攻击中直接使用。

---

## 5. `w=4`：模 `256` 只剩两个 gap

这里唯一类型是 `(z,w)=(1,4)`，同样有 `N_0` 偶。

从 (6) 开始逐级检查平方剩余：

- mod `16` 只剩 `16,18,24,26,32,34`；
- mod `32` 只剩 `16,24,26,32`；
- mod `64` 只剩 `24,26,32`；
- mod `256` 最终只剩
  \[
  \boxed{24,26.}
  \]

因此

\[
\boxed{(z,w)=(1,4)\Longrightarrow\Gamma\in\{24,26\}.}
\tag{12}
\]

---

## 6. central core 的新大小

六类型分别剩余：

- `(1,1)`：12 个；
- `(1,3)`：12 个；
- `(3,1)`：12 个；
- `(1,2)`：5 个；
- `(3,2)`：5 个；
- `(1,4)`：2 个。

总计

\[
\boxed{48}
\]

个 type-gap 组合。

这里的压缩完全独立于 `b_1,Q` 的具体 factorization，也独立于 `ell`。下一步 central sector 只需把这 48 个固定局部类型与

\[
c_\Gamma h=N_0 10^k-\Gamma,
\qquad h=q s,
\]

及 `q|Q` / whole-block selector 联用。

---

<a id="source-central-gap-sign-collapse"></a>

> 整合来源：`central-gap-sign-collapse.md`

# A1 minimal diagonal: central-gap sign collapse

> 日期：2026-08-19。依赖 `central-gap-2adic.md`。
> 本文研究 central denominator sector 的整数平方核
> \[
> R=K-2(10^k\rho)Q\mathcal N.
> \]

令

\[
T=10^k,
\qquad
s=\frac{N_0}{T}\in[0.1,1].
\]

把 central relation

\[
10^k\rho=N_0T-\Gamma
\]

代入后，`R` 是 `T,N_0` 的显式整数多项式。本文证明其最高阶项已经能统一排除 18 个 central type-gap 组合。

结合 `central-gap-2adic.md`，central core 从 `48` 个进一步降到

\[
\boxed{30}
\]

个 type-gap 组合。

状态：**已严格完成。**

---

## 1. 全部 prefix 写成 `T,N_0`

minimal diagonal 中

\[
b_1=10T^2-w,
\qquad
a_2=10T^2-z,
\]

\[
Q=100T^2-10w+1,
\qquad D=TQ.
\]

又 `j=N_0+T-1`，故

\[
a_1
=100T^3+igl(10(5-z-w)+1\bigr)T+N_0-1.
\tag{1}
\]

其余量为

\[
C=10T^2a_1+a_2,
\]

\[
\mathcal N=a_1^2+(a_2b_1)^2,
\]

\[
K=b_1^2C^2-D^2\mathcal N.
\]

central sector 中

\[
B:=10^k\rho=N_0T-\Gamma,
\]

所以整数平方必要条件为

\[
\boxed{
R=K-2BQ\mathcal N\ge0,
\qquad R\text{ 为整数平方}.}
\tag{2}
\]

---

## 2. 最高阶系数

把

\[
N_0=sT
\]

形式代入多项式并按 `T` 收集。精确得到

\[
\boxed{
R=10000F_{z,w,\Gamma}(s)T^{10}
+\sum_{j=0}^{9}c_j(s)T^j.}
\tag{3}
\]

六类型的 `F` 为：

\[
F_{1,1,\Gamma}(s)
=s^2-280s+200\Gamma-5980,
\]

\[
F_{1,2,\Gamma}(s)
=s^2-280s+200\Gamma-5180,
\]

\[
F_{1,3,\Gamma}(s)
=s^2-280s+200\Gamma-4380,
\]

\[
F_{1,4,\Gamma}(s)
=s^2-280s+200\Gamma-3580,
\]

\[
F_{3,1,\Gamma}(s)
=s^2-240s+200\Gamma-4340,
\]

\[
F_{3,2,\Gamma}(s)
=s^2-240s+200\Gamma-3940.
\tag{4}
\]

这些二次式在 `s in [0.1,1]` 上都严格递减，因为导数分别小于 `2-240<0`。

---

## 3. 低阶余项有绝对统一界

对六类型与整个粗区间

\[
16\le\Gamma\le39,
\]

把每个 `c_j(s)` 视为 `s` 的整数多项式。对 `|s|<=1` 用系数绝对值和估计，可精确审计得到

\[
\boxed{
\sum_{j=0}^{9}\|c_j\|_1
\le101834561.}
\tag{5}
\]

因此对 `T>=1`：

\[
\left|\sum_{j=0}^{9}c_j(s)T^j\right|
\le101834561\,T^9.
\tag{6}
\]

而当前 fixed-layer 统一范围从 `k>=6` 开始，所以

\[
T\ge10^6.
\]

于是归一化余项满足

\[
\boxed{
\frac{|\text{remainder}|}{T^{10}}
<102.}
\tag{7}
\]

---

## 4. 若 `F<=-0.799`，平方核必严格为负

由 (3) 与 (7)，只要

\[
F_{z,w,\Gamma}(s)\le-0.799,
\]

就有最高阶项至多

\[
-7990T^{10},
\]

远大于低阶余项的绝对值，所以

\[
R<0.
\]

实际下面使用的最弱负 margin 更强：`(z,w,Gamma)=(1,1,30)` 在 `s=0.1` 时已有

\[
F=-7.99.
\]

因此不存在边界问题。

---

## 5. 被统一杀掉的 18 个组合

结合 `central-gap-2adic.md` 已允许的 gap 集合，逐类型利用 `F` 在 `[0.1,1]` 上递减，只需检查 `s=0.1` 的最大值。

### `(1,1)`

\[
\boxed{
\Gamma=16,18,20,22,24,26,28,30
\Longrightarrow R<0.}
\]

剩余 `32,34,36,38`。

### `(1,3)`

\[
\boxed{
\Gamma=16,18,20,22
\Longrightarrow R<0.}
\]

剩余 `24,26,28,30,32,34,36,38`。

### `(3,1)`

\[
\boxed{
\Gamma=16,18,20
\Longrightarrow R<0.}
\]

`Gamma=22` 的 leading sign 在当前 decade 内发生一次转换；`24,...,38` 保留。

### `(1,2)`

\[
\boxed{
\Gamma=16,22
\Longrightarrow R<0.}
\]

剩余 `30,32,38`。

### `(3,2)`

\[
\boxed{
\Gamma=16\Longrightarrow R<0.}
\]

剩余 `22,30,32,38`。

### `(1,4)`

2-adic 层只剩 `24,26`，二者 leading sign 均为正，所以本层不再删除。

总删除数：

\[
8+4+3+2+1=\boxed{18}.
\]

因此 central core 从 48 个降为

\[
\boxed{30}.
\tag{8}
\]

---

## 6. 唯一 crossing case `(3,1,Gamma=22)`

这里

\[
F(s)=s^2-240s+60.
\]

在 `s=0.251`：

\[
F(0.251)=-0.176999\ldots
\]

最高阶贡献小于 `-1769 T^10`，仍压过 (7) 的低阶余项。因此

\[
\boxed{
(z,w,\Gamma)=(3,1,22)
\Longrightarrow
\frac{N_0}{10^k}<0.251.}
\tag{9}
\]

所以 crossing case 虽未完全关闭，也被压入 decade 的最左约 15.1% 区间 `[0.1,0.251)`。

---

## 7. central sector 当前剩余表

| `(z,w)` | remaining `Gamma` |
|---|---|
| `(1,1)` | `32,34,36,38` |
| `(1,3)` | `24,26,28,30,32,34,36,38` |
| `(3,1)` | `22,24,26,28,30,32,34,36,38` (`22` 还要求 `N_0<0.251*10^k`) |
| `(1,2)` | `30,32,38` |
| `(3,2)` | `22,30,32,38` |
| `(1,4)` | `24,26` |

总数

\[
4+8+9+3+4+2=\boxed{30}.
\]

下一步可以在这 30 个正号组合上继续研究“是否为平方”，而不再浪费精力在已经由符号排除的 central gaps 上。

---

<a id="source-central-modular-exhaustion"></a>

> 整合来源：`central-modular-exhaustion.md`

# A1 minimal diagonal: complete central modular exhaustion

> 日期：2026-08-19。依赖 `central-supply-pell-normal-form.md`、`central-pell-local-squareclass.md`、`central-double-square-valuation-lock.md` 与原 contact square。
> 当前统一范围为
> \[
> d=2,\qquad r=s=1,\qquad k=g\ge26.
> \]

本文关闭 minimal diagonal 的整个 **central denominator sector**。

此前 central 已从 144 个 type-gap 组合压到 30 个，并把每个组合的全部无界 `k` 归约为一个与 `k` 无关的有限 `U` 窗。这里不再尝试逐个求 generalized Pell 基本解，而是把：

1. supply quadratic；
2. supply-Pell 判别式的 `2/5` local squareclass；
3. 原 rational-contact integer square；
4. `10^k` 在奇素数模下的有限周期；

直接组合成一个精确有限模覆盖。

最终结果：

\[
\boxed{\text{central denominator sector 在全部 }k\ge26\text{ 上为空}.}
\]

状态：**已严格完成；附带 C++ exact certificate。**

---

## 1. 输入：30 个 surviving central type-gap

central gap 为整数

\[
\Gamma=10^k(N_0-\rho).
\]

经过 `central-gap-2adic.md` 与 `central-gap-sign-collapse.md` 后，只剩：

\[
\begin{array}{c|l}
(z,w)&\Gamma\\ \hline
(1,1)&32,34,36,38\\
(1,3)&24,26,28,30,32,34,36,38\\
(3,1)&22,24,26,28,30,32,34,36,38\\
(1,2)&30,32,38\\
(3,2)&22,30,32,38\\
(1,4)&24,26
\end{array}
\tag{1}
\]

唯一 crossing `(3,1,22)` 还使用 `central-crossing-sharp.md` 的

\[
N_0/10^k<0.250261,
\qquad U\ge3,867,967.
\tag{2}
\]

---

## 2. 固定 `(z,w,Gamma)` 后的有限 `t` 坐标

定义

\[
c=2^{v_2(\Gamma)}5^{v_5(\Gamma)},
\qquad r=\Gamma/c,
\qquad C_0=w(10w-1),
\]

\[
L=10^k/c,
\qquad U_0=10c\Gamma(20w-1),
\qquad t=U-U_0>0.
\]

`central-supply-pell-normal-form.md` 给出 `k`-independent 的严格 `U` 窗

\[
c(C_0+1000\Gamma^2)
<U
<c(C_0/10+10000\Gamma^2)+1.
\tag{3}
\]

因此每个 type-gap 的 `t` 从一开始就是一个绝对有限整数区间。

同时

\[
B_U=-4C_0rt.
\tag{4}
\]

若 exact candidate 存在，则 supply quadratic 的判别式必须平方，所以 `B_U` 必须同时属于 `Q_2`、`Q_5` 的平方类。

进一步由 `central-double-square-valuation-lock.md`：

\[
\boxed{
v_2(N_0)=\frac{v_2(t)-v_2(C_0)}2,
\qquad
v_5(N_0)=\frac{v_5(t)}2.}
\tag{5}
\]

所以可把原 contact integer square 模 `2^12` 与 `5^6` 的全部 residue classes 反推回 `t`。

这一步不是抽样：

- 若 `N_0=0 mod 2^12` 的 class 不允许，则所有更深 `v_2(N_0)>=12` 同时被排除；
- `5^6` 同理。

因此 `(3)-(5)` 加上完整 2/5 unit square 条件给出一个**有限且完整**的 local-compatible `t` 集合。

30 个 type-gap 合计恰有

\[
\boxed{93,580,902}
\tag{6}
\]

个这样的 `t`。

注意这里故意没有删除 `A_U` 恰为平方的退化 family；因此本证书覆盖的集合比此前的 nonsquare-Pell 核心更大，结论更安全。

---

## 3. 对每个奇素数的 exact modular necessary condition

固定一个奇素数

\[
p\ne2,5.
\]

令

\[
T=10^k\pmod p,
\qquad L=T/c\pmod p.
\]

给定 `t` 后

\[
U=U_0+t
\]

固定。任何 exact candidate 都必须存在某个

\[
N_0\pmod p
\]

同时满足下面两个条件。

### 3.1 supply quadratic

\[
\boxed{
C_0N_0^2
-U L N_0
+1000c^4r^2L^2
+rU
-10c^2r^2(20w-1)
\equiv0\pmod p.}
\tag{7}
\]

### 3.2 原 contact square

用

\[
b_1=10T^2-w,
\qquad a_2=10T^2-z,
\]

\[
Q=100T^2-10w+1,
\]

\[
a_1=100T^3+igl(10(5-z-w)+1\bigr)T+N_0-1,
\]

\[
C=10T^2a_1+a_2,
\]

\[
\mathcal N=a_1^2+(a_2b_1)^2,
\]

\[
D=TQ,
\qquad K=b_1^2C^2-D^2\mathcal N,
\]

以及 central

\[
B=N_0T-\Gamma,
\]

原 rational-contact 必要平方就是

\[
\boxed{
R=K-2BQ\mathcal N
\text{ 必须是模 }p\text{ 的平方剩余}.}
\tag{8}
\]

定义

\[
S_p(t)
:=
\left\{
k\bmod \operatorname{ord}_p(10):
\exists N_0\bmod p\text{ 同时满足 (7),(8)}
\right\}.
\tag{9}
\]

任何 exact candidate 都必须满足

\[
k\bmod\operatorname{ord}_p(10)\in S_p(t)
\]

对所有所选素数同时成立。

---

## 4. period-420 公共覆盖

取公共素数集

\[
\begin{aligned}
\mathcal P_0=\{&3,7,11,13,29,31,37,41,43,61,71,101,127,211,239,241,\\
&271,281,421,1933,2161,2689,3541,4649\}.
\end{aligned}
\tag{10}
\]

这些素数都满足

\[
\boxed{\operatorname{ord}_p(10)\mid420.}
\tag{11}
\]

所以对每个固定 `t`，把所有 `S_p(t)` 拉回 `k mod 420` 后直接求交即可。

对 (6) 的 93,580,902 个完整 local-compatible `t` 做 exact integer enumeration 后，只剩

\[
\boxed{33}
\tag{12}
\]

个 `(t,k mod420)` 状态。

只有下列 type-gap 在公共覆盖后仍非空：

\[
\begin{array}{c|r}
(z,w,\Gamma)&\text{common-period survivors}\\ \hline
(1,1,32)&11\\
(1,1,36)&1\\
(1,3,24)&3\\
(1,3,32)&2\\
(1,3,36)&1\\
(3,1,24)&2\\
(3,1,28)&4\\
(3,1,32)&7\\
(3,1,38)&1\\
(1,2,30)&1
\end{array}
\tag{13}
\]

其余 20 个 type-gap 已经在 `P_0` 上直接归零。

---

## 5. 最后的 33 个状态也全部 CRT 不兼容

对 (12) 中的状态，再使用有限补充集

\[
\boxed{
\mathcal P_1
=
\{17,19,73,89,113,137,251,337,1009,4201\}.}
\tag{14}
\]

这里不要求 order 整除 420。

若当前状态已有

\[
k\equiv a\pmod{420},
\]

而某个 `p in P_1` 允许的 classes 为

\[
k\equiv b\pmod{o_p},
\qquad o_p=\operatorname{ord}_p(10),
\]

两者能同时成立当且仅当

\[
\boxed{
a\equiv b\pmod{\gcd(420,o_p)}}.
\tag{15}
\]

附带证书逐个检查 (12) 的 33 个状态。每一个状态至少被 `P_1` 中一个素数违反 (15)，最终留下

\[
\boxed0
\tag{16}
\]

个状态。

---

## 6. 结论

所有步骤只使用：

- `k`-independent 的严格有限 `U/t` 窗；
- exact `2/5` local-square 与 contact-square residues；
- exact integer congruence；
- `10^k mod p` 的有限乘法阶；
- CRT compatibility。

没有使用概率分解，没有截断 `k`，也没有假设 generalized Pell primitive-divisor theorem 可直接套用。

因此得到：

\[
\boxed{
\forall k=g\ge26,
\qquad
\text{minimal diagonal central denominator sector is empty}.}
\tag{17}
\]

结合 `k<=30` 的 fixed-layer certificates，当前 minimal diagonal 的任何剩余候选都必须同时满足

\[
\boxed{k\ge31}
\]

并位于

\[
\boxed{\text{deep denominator sector}.}
\]

所以后续统一证明已经无需再处理 central Pell families；全部精力可以转向 deep denominator lattice。

---

## 7. 可复核证书

源文件：

`../../../../../scripts/exact-lift/a1-only/research-checks/central-denominator/check_a1_central_modular_exhaustion.cpp`

典型运行：

```bash
g++ -O3 -std=c++17 check_a1_central_modular_exhaustion.cpp -o /tmp/a1-central
/tmp/a1-central
```

证书最终断言：

```text
TOTAL local=93580902 common=33 final=0
CERTIFICATE OK: all k>=26 central denominator states are empty.
```

枚举量较大，但每一步都是固定宽度整数模运算；分块或并行运行不会改变证明内容。

---

<a id="source-central-pell-local-squareclass"></a>

> 整合来源：`central-pell-local-squareclass.md`

# A1 minimal diagonal: central Pell degeneracy and local squareclasses

> 日期：2026-08-19。依赖 `central-supply-pell-normal-form.md`。当前范围为 `k=g>=26`，central core 已压成 30 个 `(z,w,Gamma)` 组合及其绝对有限 `U` 窗。

本文继续研究

\[
Y^2=A_U L^2+B_U,
\qquad L=10^k/c,
\]

其中

\[
c=2^{v_2(\Gamma)}5^{v_5(\Gamma)},
\qquad r=\Gamma/c,
\qquad C_0=w(10w-1),
\]

\[
A_U=U^2-4000C_0c^4r^2,
\]

\[
B_U=-4C_0rU+40C_0c^2r^2(20w-1).
\]

核心结论：

1. 所有允许 `U` 都满足 `A_U>0`、`B_U<0`；
2. 若 `A_U` 是整数平方，则该 Pell family 在 `k>=26` **统一无解**；
3. 对任何尚存 nonsquare family，`B_U` 必须同时是 `Q_2` 与 `Q_5` 中的平方，因此 `U-U_0` 被压入显式 2/5-adic squareclasses。

状态：**已严格完成。**

---

## 1. 天然平方点 `(U_0,V_0)`

定义

\[
\boxed{U_0:=10c\Gamma(20w-1),}
\]

\[
\boxed{V_0:=10c\Gamma.}
\]

因为 `Gamma=cr`，有

\[
\begin{aligned}
U_0^2-V_0^2
&=100c^2\Gamma^2\bigl((20w-1)^2-1\bigr)\\
&=4000w(10w-1)c^2\Gamma^2\\
&=4000C_0c^4r^2.
\end{aligned}
\]

所以

\[
\boxed{
A_U=U^2-(U_0^2-V_0^2).
}
\tag{1}
\]

另一方面

\[
40C_0c^2r^2(20w-1)
=4C_0rU_0,
\]

故

\[
\boxed{
B_U=-4C_0r(U-U_0).
}
\tag{2}
\]

这两个恒等式揭示了 Pell 系数的真正中心。

---

## 2. 所有允许 `U` 都严格位于平方点右侧

已有 `U` 下界

\[
U>c(C_0+1000\Gamma^2).
\]

而

\[
U_0=10c\Gamma(20w-1).
\]

六类型中 `w<=4`，故 `20w-1<=79`。于是

\[
1000\Gamma^2
>790\Gamma
\]

对当前 `Gamma>=16` 显然成立。因此

\[
\boxed{U>U_0.}
\tag{3}
\]

由 (2)：

\[
\boxed{B_U<0.}
\tag{4}
\]

同时

\[
U_0^2=V_0^2+4000C_0c^4r^2
>4000C_0c^4r^2,
\]

故 `U>U_0` 还给出

\[
\boxed{A_U>V_0^2>0.}
\tag{5}
\]

所以 central Pell family 永远处于“正主系数 + 负固定 norm”的情形。

---

## 3. `A_U` 为平方的全部退化族统一无解

假设

\[
A_U=S^2,
\qquad S\in\mathbf Z_{>0}.
\]

则 Pell 方程成为

\[
Y^2=S^2L^2+B_U
=(SL)^2-|B_U|.
\tag{6}
\]

由 (5)，

\[
S>V_0=10c\Gamma.
\]

因此

\[
SL>10c\Gamma\frac{10^k}{c}
=10\Gamma\,10^k.
\]

当前 `Gamma>=16`、`k>=26`，故

\[
\boxed{SL>1.6\times10^{28}.}
\tag{7}
\]

另一方面 30 个 central 组合统一满足

\[
\boxed{|B_U|<4\times10^{11}.}
\tag{8}
\]

该数值界只使用 `w<=4`、`Gamma<=39`、`c<=32` 和已有 `U` 上窗；附带脚本用精确整数再次审计全部 30 个组合。

于是

\[
0<|B_U|<2SL-1.
\]

因此

\[
(SL-1)^2
=(SL)^2-2SL+1
<(SL)^2-|B_U|
<(SL)^2.
\]

也就是 `Y^2` 被严格夹在两个相邻整数平方之间，矛盾。

故

\[
\boxed{
A_U\text{ 为整数平方}
\Longrightarrow
\text{该 central family 在 }k\ge26\text{ 无解}.}
\tag{9}
\]

从此 central core 只需研究

\[
\boxed{A_U>0\text{ 且 nonsquare}.}
\]

---

## 4. `B_U` 必须同时是 2-adic 与 5-adic 平方

记

\[
e_2=v_2(L)=k-v_2(c),
\qquad
e_5=v_5(L)=k-v_5(c).
\]

central 范围中 `v_2(c)<=5`、`v_5(c)<=1`，所以 `k>=26` 给出

\[
\boxed{e_2\ge21,\qquad e_5\ge25.}
\tag{10}
\]

由 Pell 方程

\[
Y^2=A_UL^2+B_U
\]

可得

\[
Y^2\equiv B_U\pmod{2^{2e_2}},
\qquad
Y^2\equiv B_U\pmod{5^{2e_5}}.
\tag{11}
\]

而 (8) 保证非零 `B_U` 的 2/5 赋值远小于 `2e_2,2e_5`。因此 `B_U` 必须本身属于

\[
\boxed{\mathbf Q_2^{\times2}\cap\mathbf Q_5^{\times2}.}
\tag{12}
\]

这不是只检查一个低模平方剩余；它是完整的局部平方类条件。

---

## 5. 把局部平方类写成 `t=U-U_0` 的显式条件

令

\[
\boxed{t:=U-U_0>0.}
\]

由 (2)：

\[
B_U=-4C_0rt.
\tag{13}
\]

写

\[
\alpha=v_2(C_0r),
\qquad
\beta=v_5(C_0r),
\]

\[
a=v_2(t),
\qquad
b=v_5(t),
\]

并令

\[
t=2^a5^b m,
\qquad\gcd(m,10)=1.
\]

### 5.1 二进条件

因为前面的 `4` 已贡献偶赋值，`B_U` 为 `Q_2` 平方首先要求

\[
\boxed{a\equiv\alpha\pmod2.}
\tag{14}
\]

去掉全部 2 次幂后，奇单位必须为 `1 mod 8`：

\[
\boxed{
-\frac{C_0r}{2^\alpha}\,5^b m
\equiv1\pmod8.
}
\tag{15}
\]

### 5.2 五进条件

同理必须有

\[
\boxed{b\equiv\beta\pmod2.}
\tag{16}
\]

并且去掉全部 5 次幂后的单位必须是模 5 二次剩余：

\[
\boxed{
\left(
\frac{
-(C_0r/5^\beta)\,2^a m
}{5}
\right)=1.
}
\tag{17}
\]

其中括号是 Legendre symbol。

因此，对每一对 valuation `(a,b)`：

- `a,b` 的奇偶性已固定；
- `m mod 8` 被唯一锁定；
- `m mod 5` 只剩两个二次特征允许类。

由 CRT，`m` 只落在两个显式 `mod 40` residue classes 中。

所以 central 的有限 `U` 窗并非无结构大区间，而是进一步分裂成

\[
\boxed{
\text{有限 valuation pairs }(a,b)
\times
\text{每对至多两个 }m\pmod{40}
}
\tag{18}
\]

的局部平方类射线。

---

## 6. 当前 central Pell 核心

结合 `central-supply-pell-normal-form.md` 与本文：

1. type-gap 只剩 30 个；
2. 每个组合 `U` 落在绝对有限、`k`-independent 的整数窗；
3. 所有 `A_U` square 的退化族已经统一排空；
4. 剩余 `U` 必须满足 (14)-(17) 的完整 2/5-adic squareclass；
5. 对每个尚存 `U`，只剩真正 nonsquare generalized Pell
   \[
   Y^2-A_UL^2=B_U,
   \qquad L=10^k/c.
   \]

下一步应只研究这些 nonsquare、local-compatible families；无需再把 square-`A_U` 或局部不可能的 `U` 带入 Pell/primitive-divisor 阶段。

---

<a id="source-central-supply-pell-normal-form"></a>

> 整合来源：`central-supply-pell-normal-form.md`

# A1 minimal diagonal: central supply Pell normal form

> 日期：2026-08-19。依赖 `gap-denominator-normal-form.md`、`central-gap-2adic.md`、`central-gap-sign-collapse.md`。
> 当前统一前沿为 `k=g>=26`，central core 已只剩 30 个 `(z,w,Gamma)` 组合。

本文把 odd-prime supply 的粗必要条件

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1
\]

进一步转成一个与 `k` 无关的有限参数 `U`，并把所有剩余十进制尺度装进

\[
L=\frac{10^k}{c_\Gamma}.
\]

最终每个 central type-gap 组合都被严格归约为有限多个广义 Pell / Thue-Mahler 方程

\[
\boxed{Y^2=A_U L^2+B_U,\qquad L=10^k/c_\Gamma.}
\]

这一步尚未宣称这些方程全部无解，但它第一次把 central sector 中的 `k`-uniform odd-supply 问题降成**绝对有限个固定系数二次方程族**。

状态：**归约严格完成；方程族的统一无解性待证。**

---

## 1. central decimal equation

固定 central gap

\[
\Gamma\in\{16,\ldots,39\}.
\]

令

\[
\boxed{
c:=c_\Gamma
=2^{v_2(\Gamma)}5^{v_5(\Gamma)},}
\]

\[
\boxed{r:=\Gamma/c.}
\]

于是

\[
\gcd(r,10)=1.
\]

再令

\[
\boxed{L:=10^k/c.}
\]

因为当前 `k>=26` 而 `c<=32`，`L` 是一个巨大整数，并且

\[
\gcd(r,L)=1.
\]

central normal form

\[
c h=N_0 10^k-\Gamma
\]

精确化为

\[
\boxed{h=N_0L-r.}
\tag{1}
\]

---

## 2. odd supply 首先给出 `h | Q b1`

minimal-diagonal odd-prime theorem 给

\[
h=qs,
\qquad q\mid Q,
\]

而 `s` 是 `b_1` 的 whole-block selector，因此特别有

\[
s\mid b_1.
\]

又

\[
\gcd(Q,b_1)=1,
\]

所以

\[
\boxed{h\mid Qb_1.}
\tag{2}
\]

本文只使用 (2)，因此所得结论甚至比完整 whole-block supply 更弱、更安全；任何 exact candidate 必须通过它。

---

## 3. `Qb1` 在 `L` 坐标下只有三层

因为

\[
10^k=cL,
\]

有

\[
b_1=10c^2L^2-w,
\]

\[
Q=100c^2L^2-10w+1.
\]

记

\[
\boxed{C_0:=w(10w-1).}
\tag{3}
\]

直接相乘：

\[
\boxed{
Qb_1
=1000c^4L^4
+10c^2(1-20w)L^2
+C_0.}
\tag{4}
\]

没有 `L^3` 或 `L` 项。正是这个稀疏性允许做下面的十进制 Euclidean descent。

---

## 4. 第一次商余：固定小 residual `tau`

由 (2)，定义正整数

\[
\boxed{M:=\frac{Qb_1}{h}.}
\]

对 `L` 作 Euclidean division：

\[
\boxed{M=B L+m,\qquad0\le m<L.}
\tag{5}
\]

由 (1)：

\[
h\equiv-r\pmod L,
\]

由 (4)：

\[
Qb_1\equiv C_0\pmod L.
\]

所以

\[
-rm\equiv C_0\pmod L.
\]

即存在整数 `tau` 使

\[
\boxed{rm+C_0=\tau L.}
\tag{6}
\]

因为 `0<=m<L`、`L>C_0` 且 `r>=1`，有

\[
\boxed{1\le\tau\le r.}
\tag{7}
\]

因此第一次余数虽然 `m` 随 `L` 增长，但它由一个绝对小的 `tau` 唯一控制。

---

## 5. 第二次下降产生 bounded integer `U`

把

\[
Qb_1=(N_0L-r)(BL+m)
\]

展开，并使用 (4)、(6)。比较除去常数项后的 `L`-倍数，模 `L` 得

\[
N_0m-rB-\tau\equiv0\pmod L.
\]

乘以 `r` 并用

\[
rm=\tau L-C_0
\]

得到

\[
\boxed{
r^2B+N_0C_0+r\tau=UL}
\tag{8}
\]

对某个正整数 `U`。

将 (6)、(8) 全部代回精确乘积恒等式，所有 `B,m,tau` 消失，最终得到

\[
\boxed{
C_0N_0^2
-U L N_0
+1000c^4r^2L^2
+rU
-10c^2r^2(20w-1)
=0.}
\tag{9}
\]

这是 central odd-supply 的核心二次正规形。

---

## 6. `U` 的区间与 `k` 无关

由 (9) 也可直接解出

\[
\boxed{
U=
\frac{
C_0N_0^2
+1000c^4r^2L^2
-10c^2r^2(20w-1)
}{N_0L-r}.}
\tag{10}
\]

写

\[
s=N_0/L.
\]

由于

\[
10^{k-1}\le N_0<10^k=cL,
\]

有

\[
\boxed{c/10\le s<c.}
\tag{11}
\]

忽略 `O(L^-2)` 的精确主函数为

\[
f(s)=C_0s+\frac{1000c^4r^2}{s}.
\tag{12}
\]

在 (11) 上

\[
f'(s)=C_0-\frac{1000c^4r^2}{s^2}
< C_0-1000c^2r^2
=C_0-1000\Gamma^2<0.
\]

所以 `f` 严格递减。

从 (10) 直接比较可见 `U>f(s)`；而当前 `k>=26` 给出的 `L` 极大，使正误差严格小于 `1`。因此可取安全整数窗

\[
\boxed{
 c(C_0+1000\Gamma^2)
<U
<c\left(\frac{C_0}{10}+10000\Gamma^2\right)+1.}
\tag{13}
\]

关键点是：这个区间**完全不含 `k`**。

所以对每个固定 `(w,Gamma)`，`U` 只属于一个绝对有限整数集合。

---

## 7. 判别式给出 generalized Pell equation

把 (9) 看成关于整数 `N_0` 的二次方程。其判别式必须是整数平方：

\[
\boxed{Y^2=\Delta_U(L).}
\]

直接展开得到

\[
\boxed{
Y^2
=
\left(
U^2-4000C_0c^4r^2
\right)L^2
-4C_0rU
+40C_0c^2r^2(20w-1).}
\tag{14}
\]

定义固定整数

\[
\boxed{
A_U:=U^2-4000C_0c^4r^2,}
\]

\[
\boxed{
B_U:=-4C_0rU
+40C_0c^2r^2(20w-1).}
\]

则

\[
\boxed{Y^2=A_UL^2+B_U.}
\tag{15}
\]

而

\[
\boxed{
L=10^k/c
=2^{k-v_2(c)}5^{k-v_5(c)}.}
\tag{16}
\]

因此每个固定 `U` 对应一个固定系数的 generalized Pell / binary quadratic `S`-unit 方程，其中第二变量 `L` 只能沿一条纯 `2/5` 指数射线增长。

---

## 8. Q-side / b1-side resultants

完整 supply 还能保留更多信息。写

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1.
\]

由 central congruence

\[
N_0 10^k\equiv\Gamma\pmod q,
\]

以及

\[
Q=100(10^k)^2-(10w-1),
\]

得到

\[
\boxed{
q\mid
(10w-1)N_0^2-100\Gamma^2.}
\tag{17}
\]

同理，从 `s|b1` 得

\[
\boxed{
s\mid wN_0^2-10\Gamma^2.}
\tag{18}
\]

两个 resultant 还满足精确差式

\[
\boxed{
10(wN_0^2-10\Gamma^2)
-igl((10w-1)N_0^2-100\Gamma^2\bigr)
=N_0^2.}
\tag{19}
\]

这些关系将在继续筛选有限 `U` families 时保留 Q-side / whole-block side 的来源信息。

---

## 9. 当前 central core 的新形状

此前 central sector 经 2-adic + sign collapse 只剩 30 个 `(z,w,Gamma)`。

本文进一步证明：对每个这样的固定组合，任意 candidate 都必须给出一个整数 `U`，满足绝对有限窗 (13)，并使

\[
Y^2=A_UL^2+B_U,
\qquad L=10^k/c,\quad k>=26.
\]

所以 central sector 的无界问题已经从

- `k` 任意增长；
- `N_0` 有约 `9*10^(k-1)` 个值；
- odd-prime supply 随 `b_1,Q` factorization 改变；

归约为：

\[
\boxed{
30\text{ 个 type-gap}
\times
\text{每个一个固定有限 }U\text{ 区间}
\times
\text{固定系数 }S\text{-unit Pell families}.}
\]

下一步应优先利用：

1. `B_U` 必须同时是足够深的 `2`-adic、`5`-adic square residue；
2. 若 `A_U` 是整数平方，则 (15) 立即退化成固定因子差平方，`k` 大时极易排除；
3. 若 `A_U` 非平方，则 (15) 是一族固定 generalized Pell 方程，而 `L` 被限制为纯 `2/5`-unit，可继续用局部模筛、Lucas/Pell primitive divisor 或显式 Thue-Mahler 方法；
4. (17)-(19) 继续保留 full odd-prime source split，可进一步过滤 `U,N_0`。

本文只完成归约，不把这些后续算术任务误写成已经关闭。

---

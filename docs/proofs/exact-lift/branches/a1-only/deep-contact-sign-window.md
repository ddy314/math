# A1 minimal diagonal: continuous contact-sign window in deep sector

> 日期：2026-08-20。依赖 `central-gap-sign-collapse.md` 与 `sharp-positive-tail-window.md`。当前统一剩余范围可取 `k=g>=32`；本文估计实际从 `k>=31` 已足够。

`central-gap-sign-collapse.md` 的最高阶平方核并不依赖 `Gamma` 为整数。这里把同一个 leading-sign argument 直接用于 deep sector 的连续 normalized gap

\[
\Gamma=10^k(N_0-\rho).
\]

得到六类型新的 contact-sign 下沿，并把 double-deep 的 bounded renormalized 参数 `xi=t/D` 的下界同步抬高。

状态：**已严格完成。**

---

## 1. contact square leading term

令

\[
T=10^k,
\qquad s=N_0/T\in[0.1,1].
\]

原 rational-contact square kernel 写成

\[
R=10000F_{z,w,\Gamma}(s)T^{10}+E_9,
\]

其中 `central-gap-sign-collapse.md` 已严格给出

\[
|E_9|\le101834561T^9.
\]

六类型：

\[
F_{1,1}=s^2-280s+200\Gamma-5980,
\]

\[
F_{1,2}=s^2-280s+200\Gamma-5180,
\]

\[
F_{1,3}=s^2-280s+200\Gamma-4380,
\]

\[
F_{1,4}=s^2-280s+200\Gamma-3580,
\]

\[
F_{3,1}=s^2-240s+200\Gamma-4340,
\]

\[
F_{3,2}=s^2-240s+200\Gamma-3940.
\]

这些公式是关于 real/rational `Gamma` 的多项式恒等式；central 中取整数 gap 只是其特例。

---

## 2. deep candidate 必须有 `F` 非负到极小误差

任何 exact candidate 都要求

\[
R\ge0.
\]

故

\[
F_{z,w,\Gamma}(s)
\ge-rac{101834561}{10000T}.
\]

当前 `k>=31`：

\[
\frac{101834561}{10000T}<1.1\times10^{-27}.
\]

因此所有下面保留到 `10^-4` 的十进制下界都有巨大安全余量。

又每个 `F` 在 `s in[0.1,1]` 上严格递减，所以

\[
F(s)\le F(0.1).
\]

若 `F(s)` 能非负，则 `F(0.1)` 必须至少大于上述极小负误差。

由此得到：

\[
\boxed{
\begin{array}{c|c}
(z,w)&\Gamma\text{ 必须满足}\\ \hline
(1,1)&\Gamma>30.0399\\
(1,2)&\Gamma>26.0399\\
(1,3)&\Gamma>22.0399\\
(1,4)&\Gamma>18.0399\\
(3,1)&\Gamma>21.8199\\
(3,2)&\Gamma>19.8199
\end{array}}
\tag{1}

这比纯 positive-tail theorem 的类型下界再次提高约 `2--3` 个 gap units。

---

## 3. 与 sharpened upper window 合并

`sharp-positive-tail-window.md` 的类型上界可安全写成

\[
\boxed{
\begin{array}{c|c}
(z,w)&\Gamma\text{ window}\\ \hline
(1,1)&30.0399<\Gamma<33.003\\
(1,2)&26.0399<\Gamma<29.003\\
(1,3)&22.0399<\Gamma<25.003\\
(1,4)&18.0399<\Gamma<21.003\\
(3,1)&21.8199<\Gamma<39.003\\
(3,2)&19.8199<\Gamma<37.003
\end{array}}
\tag{2}

尤其四个 `z=1` 类型的 continuous gap 都被压到宽度不足 3 的窄带。

---

## 4. 对 renormalized factor 参数 `xi=t/D` 的影响

对任意 double-deep，universal factorization 给

\[
\boxed{
\xi:=\frac tD
=
\frac{
(10\Gamma T-wN_0)
(100\Gamma T-(10w-1)N_0)
}{TN_0-\Gamma}.}
\tag{3}

写 `s=N_0/T`：

\[
\xi
=
\frac{
(10\Gamma-ws)
(100\Gamma-(10w-1)s)
}{s-\Gamma/T^2}.
\tag{4}

在当前区域中，右侧对 `Gamma` 严格递增、对 `s` 严格递减。

另一方面 contact sign 本身给每个 `s` 的必要下界

\[
\Gamma
\gtrsim
\frac{C+a s-s^2}{200},
\]

其中 `(C,a)` 为对应 `F` 中常数与线性系数。把它代回 (4)，最小值发生在 `s=1`。忽略只会使 denominator 变小、从而使 `xi` 变大的 `Gamma/T^2` correction，得到严格安全整数下界：

\[
\boxed{
\begin{array}{c|c}
(z,w)&\xi\text{ 下界}\\ \hline
(1,1)&\xi>973439.975\\
(1,2)&\xi>734409.975\\
(1,3)&\xi>528999.975\\
(1,4)&\xi>357209.975\\
(3,1)&\xi>519839.975\\
(3,2)&\xi>428489.975
\end{array}}
\tag{5}

因此在 moderate branch `xi=r` 为整数时：

\[
\boxed{
\begin{array}{c|c}
(z,w)&r\ge\\ \hline
(1,1)&973440\\
(1,2)&734410\\
(1,3)&529000\\
(1,4)&357210\\
(3,1)&519840\\
(3,2)&428490
\end{array}}
\tag{6}

旧 typewise upper bounds 保持不变，所以新的 moderate `r` windows 为

\[
\boxed{
\begin{array}{c|c}
(z,w)&r\\ \hline
(1,1)&973440\le r\le10885221\\
(1,2)&734410\le r\le8400003\\
(1,3)&529000\le r\le6236387\\
(1,4)&357210\le r\le4394372\\
(3,1)&519840\le r\le15204352\\
(3,2)&428490\le r\le13677244
\end{array}}
\tag{7}

---

## 5. 当前用途

LL 已经关闭，所以 (7) 现在主要缩短 moderate 2-high master branch `eta<=0` 的 HL 参数窗。

对 `eta>0` 的 former `E_2`，(5) 同样适用于 bounded rational `xi`; 因此 extreme pure-2 denominator descent 也应使用新的 typewise lower bounds，而不再使用全局 `196000` 粗界。

更重要的是 (1)-(2) 是**原 rational-contact square 的独立全局输入**；它不属于 four-factor/Hensel skeleton，因此可以安全与后者联用。

# A1 minimal diagonal: contact square + mandatory `3`-block lock

> 日期：2026-08-20。依赖 `deep-double-2high-master.md`、`deep-four-factor-frame.md` 与原 rational-contact square。本文适用于 `w=1,4`，因为这两型的 `b_1` 永远含有 mandatory `3 mod 4` block。

状态：**已严格完成。**

---

## 1. `3` 永远在 complementary `u` 侧

若 `w=1` 或 `w=4`，则

\[
b_1=10^{2k+1}-w\equiv1-w\equiv0\pmod3.
\]

而

\[
3\equiv3\pmod4,
\]

所以 odd-prime supply selector `s` 不能使用整个 3-primary block。

因此

\[
\boxed{3\mid u=b_1/s,}
\qquad
\boxed{3\nmid s.}
\tag{1}

同时

\[
Q=10b_1+1\equiv1\pmod3,
\]

故 `q,v` 都是 3-adic units，且

\[
\boxed{qv\equiv1\pmod3.}
\tag{2}

---

## 2. stripped equations mod 3

master branch：

\[
2\beta u-\alpha v=5^d,
\]

\[
\beta q-5\alpha s=2^c n_0.
\]

由 `3|u`，第一式给

\[
-\alpha v\equiv(-1)^d\pmod3.
\]

所以

\[
v\equiv-(-1)^d\alpha^{-1},
\]

再由 (2)：

\[
\boxed{q\equiv-(-1)^d\alpha\pmod3.}
\tag{3}

第二式模 3 为

\[
\beta q+\alpha s\equiv(-1)^c n_0.
\]

代入 (3) 与 `alpha beta=r_10`：

\[
\alpha s
\equiv(-1)^c n_0+(-1)^d r_{10}.
\]

所以

\[
\begin{aligned}
h=qs
&\equiv q\alpha^{-1}igl((-1)^c n_0+(-1)^d r_{10}\bigr)\\
&\equiv-r_{10}-(-1)^{c+d}n_0
\pmod3.
\end{aligned}
\tag{4}

---

## 3. 把 `n_0` 换回 `N_0`

写

\[
N_0=2^{\nu_2}5^{\nu_5}n_0.
\]

模 3 中 `2≡5≡-1`，因此

\[
n_0\equiv(-1)^{\nu_2+\nu_5}N_0\pmod3.
\]

而

\[
c=k+1+\eta+\nu_2,
\]

\[
d=k+1-B-\nu_5.
\]

所以

\[
(-1)^{c+d}n_0
\equiv(-1)^{\eta+B}N_0\pmod3.
\]

于是 (4) 化成

\[
\boxed{
h\equiv-r_{10}-(-1)^{\eta+B}N_0\pmod3.}
\tag{5}

---

## 4. contact square mod 3

因为 `3|b_1`、`Q≡T≡1 mod3`，prefix norm 满足

\[
N=a_1^2+(a_2b_1)^2\equiv a_1^2\pmod3.
\]

六型公式给在 `w=1,4,z=1`：

\[
a_1\equiv N_0+1\pmod3.
\]

原 contact square

\[
V^2=K-2\rho TQN
\]

而模 3：

\[
K\equiv-N,
\qquad
\rho=\frac h{DT}.
\]

所以

\[
\boxed{
V^2\equiv-(1+2hD^{-1})a_1^2\pmod3.}
\tag{6}

若

\[
N_0\not\equiv2\pmod3,
\]

则 `a_1` 是 unit。非零平方模 3 只能为 1，因此 (6) 强迫

\[
-(1+2hD^{-1})\equiv1\pmod3.
\]

即

\[
\boxed{h\equiv2D\pmod3.}
\tag{7}

master branch 中

\[
A=2k+3+\eta,
\]

所以

\[
D=2^A5^B\equiv(-1)^{A+B}
=-(-1)^{\eta+B}\pmod3.
\]

又 `2=-1 mod3`，故

\[
\boxed{2D\equiv(-1)^{\eta+B}\pmod3.}
\tag{8}

把 (5),(7),(8) 联立：

\[
-r_{10}-(-1)^{\eta+B}N_0
\equiv(-1)^{\eta+B}
\pmod3.
\]

最终得到

\[
\boxed{
r_{10}
\equiv-(-1)^{\eta+B}(N_0+1)
\pmod3,}
\tag{9}

只要 `N_0 !=2 mod3`。

---

## 5. 一个立即推论

若

\[
3\mid r_{10},
\]

而 `N_0 !=2 mod3`，(9) 右侧非零，矛盾。

因此

\[
\boxed{
3\mid r_{10}
\Longrightarrow
N_0\equiv2\pmod3
\qquad(w=1,4).}
\tag{10}

在 `N_0=2 mod3` 时 `a_1=0 mod3`，contact square (6) 本身退化为 `0`，所以本文不虚构额外条件。

---

## 6. 意义

这是第一条把：

- mandatory `b_1` prime block；
- four-factor stripped equations；
- 原 rational-contact square；

三者联立后反推出 prefix `N_0` residue 的显式公式。

后续可对其他周期性 mandatory primes 做同样处理：固定某个 `p=3 mod4` 与 `d mod ord_p(10)`，若该 p-primary block 被迫留在 `u`，则 contact square可产生相应 `(r_10,N_0)` residue lock。

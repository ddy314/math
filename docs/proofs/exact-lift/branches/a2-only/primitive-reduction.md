# A2 primitive numerator reduction and carrier separation

> **依赖：** `endpoint-lattice.md` §§16.11–16.12、16.15、16.45–16.73，以及 `prime-source.md`。
>
> **严格状态：**本文识别 `W_q` 的全局本原含义，审计 height character 的独立性，并进一步分离 q/f saturation 与 sphere-height 通道。本文仍**不宣称 A2 全局关闭**。

---

## 1. `已严格完成`：`W_q` 与 sphere height 之间存在全局整数恒等式

§16.72 已得到

\[
2c_uW_q=c_+^2Y+5^\lambda c_-^2X.
\tag{1.1}
\]

而 reflection 的 canonical factor allocation 早已有

\[
H_0-Y_3=5^\lambda c_-^2X,
\qquad
H_0+Y_3=c_+^2Y.
\tag{1.2}
\]

把 (1.2) 两式相加：

\[
2H_0=c_+^2Y+5^\lambda c_-^2X.
\]

与 (1.1) 比较，得到此前只在逐素数层出现、但实际上更强的全局恒等式

\[
\boxed{H_0=c_uW_q.}
\tag{1.3}
\]

因此 §16.73 的

\[
v_r(W_q)=v_r(H_0)
\]

对任何 `r\nmid c_u` 都只是 (1.3) 的逐素数投影；并不需要再次从 rational-root equation 逐素数恢复。

---

## 2. `已严格完成`：`W_q` 就是旧 Hensel quotient `alpha_0`，也是 `gcd(alpha,H_0)`

§16.15 已从真实 concatenation plane 得到

\[
\alpha=\omega\alpha_0,
\qquad
H_0=c_u\alpha_0,
\qquad
\gcd(\omega,c_u)=1.
\tag{2.1}
\]

与 (1.3) 比较立刻有

\[
\boxed{W_q=\alpha_0.}
\tag{2.2}
\]

所以

\[
\boxed{
\alpha=\omega W_q,
\qquad
H_0=c_uW_q.
}
\tag{2.3}
\]

由于 `gcd(omega,c_u)=1`，

\[
\boxed{W_q=\gcd(\alpha,H_0).}
\tag{2.4}
\]

这给 `W_q` 一个完全 canonical 的含义：它不是 rational-root 后来新出现的自由 quotient，而是**原拼接分子与整数球面高度的最大公因子**。

当前 endpoint 为 `a_1=9`，第二分子有 `M-1` 位、第三分子有 `m+1` 位。令

\[
T=10^m,
\qquad
P=9\cdot10^{M-1}+a_2,
\qquad
K=10P,
\]

则原拼接分子精确为

\[
\alpha
=9\cdot10^{M+m}+a_2\cdot10^{m+1}+a_3
=TK+a_3.
\tag{2.5}
\]

故还可写成

\[
\boxed{TK+a_3=\omega W_q.}
\tag{2.6}
\]

---

## 3. `已严格完成`：`omega` 是拼接分子/分母的完整 gcd，`W_q` 是 reduced numerator

§16.15 的 LCM 为

\[
q_{\rm lcm}=b_2c_Q5^d=b_3g,
\]

且原整数平面在约去公共尺度后给出

\[
q_{\rm lcm}\omega=c_u\beta.
\tag{3.1}
\]

定义

\[
S:=\frac{q_{\rm lcm}}{c_u}.
\tag{3.2}
\]

reflection 中

\[
b_2=2^{M+m+1}c_ug,
\]

所以

\[
\boxed{S=2^{M+m+1}gc_Q5^d.}
\tag{3.3}
\]

接下来证明

\[
\boxed{\gcd(W_q,S)=1.}
\tag{3.4}
\]

逐个 prime source 检查即可：

1. §16.72 已给 `W_q mod 4`，故 `W_q` 为奇数；
2. (1.1) 模 `5` 时第二项消失，而 `c_u,c_+,Y` 都是 `5`-进单位，故 `5\nmid W_q`；
3. §16.30 有 `gcd(H_0,g)=1`，结合 (1.3) 得 `gcd(W_q,g)=1`；
4. 若 `p\mid c_+`，由 `H_0+Y_3=c_+^2Y` 得 `H_0\equiv-Y_3 (mod p)`；若 `p\mid c_-`，则由另一式得 `H_0\equiv Y_3 (mod p)`。因为 `c_Q\mid b_3`、`gcd(a_3,b_3)=1` 且 `gcd(g,c_Q)=1`，两种情形都有 `p\nmid Y_3=ga_3`。故 `gcd(H_0,c_Q)=1`，再由 (1.3) 得 `gcd(W_q,c_Q)=1`。

这证明 (3.4)。

由 (3.1) 有

\[
\beta=S\omega.
\tag{3.5}
\]

结合 `alpha=omega W_q` 与 (3.4)：

\[
\boxed{
\gcd(\alpha,\beta)=\omega.
}
\tag{3.6}
\]

所以原十进制拼接分数的最低项表示被完全识别：

\[
\boxed{
\frac{\alpha}{\beta}
=\frac{W_q}{S},
\qquad
\gcd(W_q,S)=1.
}
\tag{3.7}
\]

同时由

\[
H_0=c_uW_q,
\qquad
q_{\rm lcm}=c_uS
\]
还得到对 sphere lift 的对称 primitive recovery：

\[
\boxed{
\gcd(H_0,q_{\rm lcm})=c_u.
}
\tag{3.8}
\]

因此四个此前分散的量其实是两个最简分数的同一套 gcd 数据：

\[
\boxed{
\omega=\gcd(\alpha,\beta),
\qquad
c_u=\gcd(H_0,q_{\rm lcm}),
\qquad
W_q=\frac{\alpha}{\omega}=\frac{H_0}{c_u}.
}
\tag{3.9}
\]

---

## 4. `已严格完成 / 审计降级`：height channel 的 `N_0` 非剩余 character 是自动 shadow

设

\[
r\ne3,
\qquad
r\equiv3\pmod4,
\qquad
r\mid W_q.
\tag{4.1}
\]

由 (1.3)，`r\mid H_0`。§16.73 已证明这种 `r` 与 `5gc_QXY` 互素；也可从 §16.45 的本原性逐项恢复。

把 (1.2) 相乘并模 `r`：

\[
(H_0-Y_3)(H_0+Y_3)
=5^\lambda c_Q^2XY.
\]

因为 `H_0\equiv0 (mod r)`、`Y_3=ga_3`，

\[
-g^2a_3^2
\equiv
5^\lambda c_Q^2XY
\pmod r.
\tag{4.2}
\]

又

\[
N_0=5^{\nu_5}XY,
\qquad
\nu_5-\lambda=-2d,
\]
故

\[
\boxed{
N_0
\equiv
-\left(
\frac{ga_3}{c_Q5^d}
\right)^2
\pmod r.
}
\tag{4.3}
\]

由于 `r=3 mod 4`，`-1` 为非平方，于是

\[
\boxed{
\left(\frac{N_0}{r}\right)=-1.
}
\tag{4.4}
\]

因此 `prime-source.md` 与 §16.73 中记录的 height character (4.4) **不是独立 obstruction**：一旦 `r\mid W_q`，它已经由 canonical factor equality 自动推出。

后续不得再把

\[
r\mid H_0
\quad\text{和}\quad
\left(\frac{N_0}{r}\right)=-1
\]

当作两条独立局部条件收费。真正新增的 global input 必须来自 `W_q` 作为 reduced numerator 的十进制/prime-flow 结构，或来自它与 `widehat{T}_2` excess carrier 的进一步连接。

---

## 5. `已严格完成`：任意 saturation-height 交集都强迫 `2K-9=0`

设非 `3` inert prime `p` 同时满足

\[
p\mid W_q,
\qquad
p\mid\mathscr L_{23}.
\tag{5.1}
\]

第二式等价于

\[
2a_3+9T\equiv0\pmod p.
\tag{5.2}
\]

另一方面由 (2.6)，`p\mid W_q` 给出

\[
TK+a_3\equiv0\pmod p.
\tag{5.3}
\]

当前 `p\nmid10`，故 `T` 是单位。把 (5.2) 代入 (5.3)：

\[
K-\frac92\equiv0\pmod p.
\]

即

\[
\boxed{2K-9\equiv0\pmod p.}
\tag{5.4}
\]

这是 denominator saturation 与 sphere-height/reduced-numerator channel 的**统一交集 resultant**；它不依赖 `q/f` 侧别。

---

## 6. `已严格完成`：q-carrier 与 height channel 的交集只可能是 special `23`

若 (5.1) 中的 `p` 同时还是 q-side additive carrier，则 §16.67 给出

\[
K^2\equiv26\pmod p.
\tag{6.1}
\]

而 (5.4) 给出 `K=9/2`，故

\[
\frac{81}{4}\equiv26\pmod p,
\]
即

\[
p\mid(104-81)=23.
\]

因此

\[
\boxed{
q\text{-carrier}\cap\text{height channel}
\Longrightarrow p=23.
}
\tag{6.2}
\]

这把 `prime-source.md` 的 special `23` 重新解释为：它不是随意出现的 fixed exception，而是 **q-side saturation 与 reduced-numerator height channel 的唯一可能交点**。

这一结论还清理了 generic `c_Q` overlap。对 `p\ne11,23` 的 q-carrier，§16.72/16.73 已有

\[
v_p(W_q)=v_p(c_Q).
\tag{6.3}
\]

但 (3.4) 已证明 `gcd(W_q,c_Q)=1`，所以

\[
\boxed{
v_p(W_q)=v_p(c_Q)=0
\qquad(p\ne11,23,\ p\text{ q-carrier}).}
\tag{6.4}
\]

因此 generic q-carrier 的 `c_Q` overlap 实际全部消失。唯一 `c_Q`-overlap 是 `prime-source.md` 已识别的 special `11`，而该点满足 `11\nmid W_q`；special `23` 则满足 `23\nmid c_Q`。

所以 q-side 的 prime-source 图现在是严格三分：

\[
\boxed{
\begin{array}{ll}
\text{generic }p\ne11,23:& p\nmid c_QW_q,\\
\text{special }11:& 11\mid c_+,\ 11\nmid W_q,\\
\text{special }23:& 23\nmid c_Q,\ \text{且它是唯一可能的 height overlap}.
\end{array}}
\tag{6.5}
\]

---

## 7. `已严格完成`：f-carrier 若进入 height channel，必须满足两条独立 reciprocity 签名

现在设 `p` 是 f-side saturation carrier，并同时满足 `p\mid W_q`。由 (3.4) 有 `p\nmid c_Q`，所以 §16.67 的 generic f-side law 适用：

\[
K^2-26
\equiv
\left(\frac{2c_Q}{2^m5^\lambda g}\right)^2N_0
\pmod p.
\tag{7.1}
\]

由 (5.4)，`K=9/2`，故

\[
K^2-26=-\frac{23}{4}.
\]

再用 (4.4)：

\[
\left(\frac{-23}{p}\right)
=
\left(\frac{N_0}{p}\right)
=-1.
\tag{7.2}
\]

对 `p=3 mod 4`，二次互反律给出

\[
\left(\frac{-23}{p}\right)
=
\left(\frac p{23}\right).
\]

所以

\[
\boxed{\left(\frac p{23}\right)=-1.}
\tag{7.3}
\]

特别地 `p\ne23`。

还可以把 §16.50 的 curvature character 化成另一个固定签名。saturation 下

\[
a_3\equiv-\frac92T\pmod p,
\]
故

\[
\mathscr R_{23}
=2a_3^2+9Ta_3+13T^2
\equiv13T^2\pmod p.
\tag{7.4}
\]

另一方面由 (4.2)

\[
XY
\equiv
-\frac{g^2a_3^2}{5^\lambda c_Q^2}
\equiv
-\frac{81}{4}\frac{g^2T^2}{5^\lambda c_Q^2}
\pmod p.
\tag{7.5}
\]

在

\[
\mathscr R_{23,f}
=2^m5^dg^2\mathscr R_{23}+2Tc_Q^2XY
\]
中使用

\[
2^m5^d=\frac{T}{5^\lambda}
\]
得到

\[
\boxed{
\mathscr R_{23,f}
\equiv
-\frac{55}{2}\frac{g^2T^3}{5^\lambda}
\pmod p.
}
\tag{7.6}
\]

若 `p\mid\mathscr R_{23,f}`，因右侧所有其他量均为单位，只可能 `p=11`。但 §16.50 的 double-root law 此时给出

\[
K\equiv9+2a_3T^{-1}\equiv0\pmod{11},
\]
而 (5.4) 给出 `K=9/2\not\equiv0 (mod 11)`，矛盾。因此

\[
\boxed{p\ne11,23,\qquad p\nmid\mathscr R_{23,f}.}
\tag{7.7}
\]

于是 §16.50 的 simple-root curvature character 必须成立：

\[
\left(\frac{\mathscr R_{23,f}}p\right)
=
\left(\frac2p\right)^{m+3}
\left(\frac5p\right)^d.
\tag{7.8}
\]

把 (7.6) 代入，使用 `T=2^m5^m` 与 `d=m-\lambda`。两边相除后全部 `m,lambda,d` 指数消去，恰剩

\[
\boxed{\left(\frac{-55}{p}\right)=1.}
\tag{7.9}
\]

对于 `p=3 mod 4`，再次用二次互反律：

\[
\boxed{
\left(\frac p5\right)
\left(\frac p{11}\right)=1.
}
\tag{7.10}
\]

因此 f-side saturation 与 height channel 若相交，必须同时满足

\[
\boxed{
\begin{gathered}
p\equiv3\pmod4,
\qquad p\notin\{3,5,11,23\},\\
2K\equiv9\pmod p,\\
\left(\frac p{23}\right)=-1,
\qquad
\left(\frac p5\right)
\left(\frac p{11}\right)=1.
\end{gathered}}
\tag{7.11}
\]

这没有把 f-height intersection 全部排空，但已经把它从“任意 endpoint-external inert prime”压成一个固定的三二次域 reciprocity signature。

---

## 8. `已严格完成`：去掉 balanced `3` 后，`W_q` 的 non-`3` inert parity 总体为偶

§16.57、16.58 给出

\[
W_q\equiv3Z\pmod4,
\qquad
\delta=1\iff Z\equiv1\pmod4,
\qquad
\delta=0\iff Z\equiv3\pmod4.
\tag{8.1}
\]

当 `delta=1` 时，§16.11 还给出 `v_3(H_0)=1`；`3\nmid c_u`，所以由 (1.3)

\[
v_3(W_q)=1.
\tag{8.2}
\]

定义

\[
W_q^{\rm prim}:=\frac{W_q}{3^\delta}.
\tag{8.3}
\]

若 `delta=0`，(8.1) 直接给 `W_q\equiv1 (mod 4)`；若 `delta=1`，则 `W_q\equiv3 (mod 4)` 且恰约去一份 `3`。两种情形统一得到

\[
\boxed{W_q^{\rm prim}\equiv1\pmod4.}
\tag{8.4}
\]

因此 `W_q` 中除 balanced `3` 以外的所有 `3 mod 4` 素数，其**奇赋值 carrier 的总数必为偶数**：

\[
\boxed{
\sum_{\substack{r\ne3\\r\equiv3\ (4)}}v_r(W_q)
\equiv0\pmod2.
}
\tag{8.5}
\]

这里的和只需按模 `2` 理解。它不能推出每个 `v_r(W_q)` 都为偶数，但它说明任何 non-`3` height odd carrier 都不能作为唯一的未配对 inert source 出现。

---

## 9. 更新后的逻辑边界

本轮最重要的审计结论是：此前把 height channel 写成

\[
r\mid H_0,
\qquad
\left(\frac{N_0}{r}\right)=-1
\]

会让它看起来像“两条条件”。严格地说，第二条只是第一条通过 canonical factor equality 的 quadratic shadow。真正的新结构是

\[
\boxed{W_q=\gcd(\alpha,H_0)}
\]

以及 saturation-height 交集律

\[
\boxed{p\mid W_q,\ p\mid\mathscr L_{23}\Longrightarrow2K-9\equiv0\pmod p.}
\]

由此：

1. q-side 与 height 的交集只可能是 `23`；
2. generic q-carrier 的 `c_Q` overlap 全部消失；
3. f-side 与 height 的交集必须满足 (7.11) 的固定 reciprocity signature；
4. height character `(N_0/r)=-1` 不得重复计作独立 obstruction；
5. non-`3` height odd carriers 在 `W_q/3^delta` 中必须成总体偶 parity。

因此下一步不应继续尝试仅凭 (1.2) 的 sphere factor equality 证明每个 `v_r(H_0)` 都为偶；这些局部式本身已经只会重现 (4.4)。真正可能闭环的两个方向是：

- 把 `W_q` 作为**最低项拼接分子的 reduced numerator**，与 `widehat{\mathcal T}_2` 的 endpoint-external excess prime 建立逐 prime-power 的赋值桥；
- 对仍可能存在的 f-height intersection，把 (7.11) 与纯 prefix resultant `Psi_f` 的完整 `p^e` 深度联立，尝试把三个二次域 signature 提升成一个真正的 Hensel/resultant 矛盾。

---

## 10. `已严格完成`：f-height intersection 精确塌缩到固定素数 `7,43`，且不存在共同二阶深接触

§9 的第二个后续方向可以直接推进一步。仍设 `p` 是非 `3` 的 inert f-side saturation carrier，并且

\[
p\mid W_q.
\tag{10.1}
\]

由 (3.4)，`p\nmid c_Q`，因此 generic f-side law (7.1) 可用。关键是这里不再只取 Legendre symbol，而保留 (4.3) 的**完整剩余类**。

先把 canonical factor equality (1.2) 相乘：

\[
H_0^2-g^2a_3^2=5^\lambda c_Q^2XY.
\]

由于

\[
N_0=5^{\nu_5}XY,
\qquad
\nu_5-\lambda=-2d,
\]
实际存在精确有理恒等式

\[
\boxed{
N_0=
\left(\frac{H_0}{c_Q5^d}\right)^2
-
\left(\frac{ga_3}{c_Q5^d}\right)^2.
}
\tag{10.2}
\]

在当前 `p` 上所有分母都是 `p`-进单位，而 `H_0=c_uW_q`，故 (10.2) 模 `p` 正好恢复

\[
N_0\equiv-
\left(\frac{ga_3}{c_Q5^d}\right)^2
\pmod p.
\tag{10.3}
\]

把 (10.3) **直接**代入 f-side law (7.1)，并用 `lambda+d=m`：

\[
\begin{aligned}
K^2-26
&\equiv
-\left(
\frac{2c_Q}{2^m5^\lambda g}
\frac{ga_3}{c_Q5^d}
\right)^2\\
&=-\left(\frac{2a_3}{T}\right)^2
\pmod p.
\end{aligned}
\tag{10.4}
\]

另一方面 saturation `p\mid\mathscr L_{23}` 给出

\[
\frac{2a_3}{T}\equiv-9\pmod p,
\tag{10.5}
\]

而 height/saturation intersection (5.4) 给出

\[
K\equiv\frac92\pmod p.
\tag{10.6}
\]

于是 (10.4) 的两边分别变成

\[
K^2-26\equiv-\frac{23}{4},
\qquad
-\left(\frac{2a_3}{T}\right)^2\equiv-81.
\]

故

\[
\boxed{301\equiv0\pmod p.}
\tag{10.7}
\]

因为

\[
301=7\cdot43,
\]
得到严格固定素数塌缩

\[
\boxed{
p\in\{7,43\}.}
\tag{10.8}
\]

这比 (7.11) 强得多：旧的三二次域 signature 只给 residue class 条件，而 (10.8) 把整个无界 f-height prime support 压成两个固定素数。两者确实都满足 (7.11)，所以这里仍不是空性；验证脚本也显式检查了这一点。

还可以把同一计算提升到 prime-power 深度。写

\[
e:=v_p(f),
\qquad
h:=v_p(W_q)=v_p(H_0),
\qquad
\tau:=v_p(\widehat{\mathcal T}_2),
\tag{10.9}
\]

并假设完整 saturation

\[
p^e\mid\mathscr L_{23}.
\tag{10.10}
\]

由 §16.69 的截断赋值律，令

\[
s:=\min\{\tau,e\},
\]
则

\[
p^s\mid\Psi_f.
\tag{10.11}
\]

同时 `f=g\omega+c_u`，且 `p\mid f`、`p\nmid gc_u`，所以 `p\nmid\omega`。由 `alpha=omega W_q` 得

\[
v_p(\alpha)=h.
\tag{10.12}
\]

又

\[
\alpha-\mathscr L_{23}
=T\left(K-\frac92\right),
\]
故在

\[
t:=\min\{s,h\}=\min\{\tau,e,h\}
\tag{10.13}
\]

的深度上有

\[
K\equiv\frac92\pmod{p^t},
\qquad
\frac{2a_3}{T}\equiv-9\pmod{p^t}.
\tag{10.14}
\]

另一方面 (10.2) 给出

\[
N_0\equiv-
\left(\frac{ga_3}{c_Q5^d}\right)^2
\pmod{p^{2h}},
\tag{10.15}
\]

而 §16.69 的 `Psi_f` 同余与 `p^e\mid f` 把 (7.1) 同样提升到模 `p^s`。因此在共同深度 `t` 上，(10.4)–(10.7) 原样成立，得到

\[
\boxed{p^t\mid301.}
\tag{10.16}
\]

但 `301=7\cdot43` 在两个剩余素数上都只有一次赋值，所以

\[
\boxed{
\min\left\{
 v_p(\widehat{\mathcal T}_2),
 v_p(f),
 v_p(W_q)
\right\}=1.
}
\tag{10.17}
\]

这给出真正的 Hensel transversality：f-denominator saturation、height/reduced-numerator 深度和 odd-excess 深度**不能三者同时进入二阶**。特别地：

- 若 `v_p(f)>=2` 且 `v_p(W_q)>=2`，则必有 `v_p(widehat{T}_2)=1`；
- 若 odd excess 深度与 height 深度都至少为 `2`，则 `v_p(f)=1`；
- 若 odd excess 深度与 denominator 深度都至少为 `2`，则 `v_p(W_q)=1`。

因此 f-height intersection 的剩余核心已经从“任意素数、任意 Hensel 深度”压成固定 `7/43` 的**一阶横截或单侧浅层**问题。下一步应分别审计 `p=7` 与 `p=43` 的唯一 Hensel 轨道，并尝试与 `W_q^{\rm prim}\equiv1 (mod 4)` 的配对约束及 prefix digit phase 联立；不能再把 (7.11) 当作无界 prime family 处理。

### 验证

```bash
uv run python scripts/exact-lift/a2-only/check_a2_f_height_fixed_primes.py
```

脚本核对 `301/4` 的精确残差、`301=7*43` 的平方自由性，以及 `7,43` 对旧 reciprocity signature 的兼容性；它只验证上述代数/局部算术，不宣称 A2 全局关闭。

# A1 minimal diagonal: top 2-high endpoint collapse

> 日期：2026-08-20。依赖 `deep-2high-denominator-cap.md` 与 `deep-double-2high-master.md`。当前 `k>=32`。

当 `delta:=D/T^2` 靠近 typewise denominator cap 时，complement product

\[
M=uv<10001/\delta
\]

变成很小的整数。结合 `u,v` 的 mandatory block minima 与 `gcd(u,v)=1`，top endpoint 的 complementary divisors 被唯一锁死。

状态：**已严格完成。**

---

## 1. structural minima 与 next possible product

因为

\[
u\mid b_1,
\qquad v\mid Q,
\qquad\gcd(b_1,Q)=1,
\]

有

\[
\boxed{\gcd(u,v)=1.}
\tag{1}

结构性最小 pair：

\[
\boxed{
\begin{array}{c|c|c|c}
w&u_{\min}&v_{\min}&M_{\min}\\ \hline
1&3&7&21\\
2&14&3&42\\
3&1&7&7\\
4&12&7&84
\end{array}}
\tag{2}

并且 next possible product 可安全取：

\[
\boxed{
\begin{array}{c|c}
w&M_{\rm next}\\ \hline
1&33\\
2&66\\
3&11\\
4&132
\end{array}}
\tag{3}

理由：

- `w=1`：`u` 为 odd multiple of 3；`v>=7`, `v=3 mod4`, `3 not|Q`. 最小 21，下一可达至少 `3*11=33`。
- `w=2`：`u` 含 factor 2 与一个 `>=7` 的 `3 mod4` odd block，所以 `u>=14`; `v>=3`. 最小 42；下一至少 `22*3=66`。
- `w=3`：无 fixed u-loss，可有 `u=1`; `v>=7`, `v=3 mod4`; 下一 v 至少 11。
- `w=4`：`u` 含 `2^2` 与完整 3-primary block，所以 `u` 是至少 12 的 `v2=2` multiple；`v>=7`. 最小 84；下一至少 `12*11=132`。

---

## 2. endpoint threshold

complement height：

\[
M<10001\frac{T^2}{D}=\frac{10001}{\delta}.
\]

若

\[
\delta>10001/M_{\rm next},
\]

则

\[
M<M_{\rm next}.
\]

结合 `M>=M_min` 与 (3)，只能有

\[
M=M_{\min}.
\]

取整洁安全 threshold：

\[
\boxed{
\frac D{T^2}>
\begin{cases}
304,&w=1,\\
152,&w=2,\\
910,&w=3,\\
76,&w=4
\end{cases}}
\tag{4}

即可保证 endpoint collapse。

因此

\[
\boxed{
(u,v)=
\begin{cases}
(3,7),&w=1,\\
(14,3),&w=2,\\
(1,7),&w=3,\\
(12,7),&w=4.
\end{cases}}
\tag{5}

---

## 3. master complement equation 变成固定系数 S-unit equation

master：

\[
2\beta u-\alpha v=5^d.
\]

代入 (5)：

\[
\boxed{
\begin{array}{c|c}
w&\text{endpoint equation}\\ \hline
1&6\beta-7\alpha=5^d\\
2&28\beta-3\alpha=5^d\\
3&2\beta-7\alpha=5^d\\
4&24\beta-7\alpha=5^d
\end{array}}
\tag{6}

并仍有

\[
\alpha\beta=r_{10},
\qquad\gcd(\alpha,\beta)=1.
\]

---

## 4. supply equation 也统一简化

master supply：

\[
\beta q-5\alpha s=2^c n_0.
\]

endpoint 中

\[
q=Q/v,
\qquad s=b_1/u,
\qquad M=uv.
\]

乘以 `uv`：

\[
\beta uQ-5\alpha v b_1=M2^cn_0.
\]

利用

\[
Q=10b_1+1
\]

和

\[
2\beta u-\alpha v=5^d:
\]

\[
\begin{aligned}
\beta uQ-5\alpha vb_1
&=\beta u+5b_1(2\beta u-\alpha v)\\
&=\beta u+5^{d+1}b_1.
\end{aligned}
\]

因此 endpoint 统一满足

\[
\boxed{
5^{d+1}b_1+\beta u
=M2^c n_0.}
\tag{7}

其中 `u,M` 已由 w 固定。

---

## 5. 下一接口

(6)-(7) 把 top pure-2 endpoint 从 arbitrary divisor problem 化成四个 fixed-coefficient exponential systems。

下一步可直接研究：

1. (7) 的 growing 2-adic valuation `c=k+1+eta+nu_2`；
2. `b_1=10T^2-w` 在 `2^c` 下的稳定 truncation；
3. (6) 对 `alpha,beta` 的 mod `2^m` / mod `5^m` Hensel classes；
4. endpoint 中 `u,v` 的 exact divisibility 对 k 的短周期条件。

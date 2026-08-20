# A1 minimal diagonal: universal deep factorization

> 日期：2026-08-20。依赖 `deep-complement-height.md` 与 minimal-diagonal odd-prime supply。当前统一范围 `k=g>=31`。

本文证明：`deep-global-factorization.md` 的核心 factor-pair 并非 double-deep 特例，而是对**所有 deep denominator states** 都成立。

沿用

\[
T=10^k,
\qquad
D=2^A5^B,
\qquad
\Gamma_k=\frac{\gamma}{D},
\qquad \gcd(\gamma,D)=1,
\]

并令非 deep 一侧留下的 numerator powers 为

\[
\lambda=2^{\lambda_2}5^{\lambda_5}.
\]

于是

\[
\boxed{DTN_0-\gamma=h\lambda.}
\tag{1}
\]

核心结论：存在正整数 `t`，使

\[
\boxed{
(10\gamma T-wDN_0)
(100\gamma T-(10w-1)DN_0)
=t h.
}
\tag{2}

若完整 odd-prime supply 写成 `h=qs`，则存在正整数 `a,b`：

\[
\boxed{
10\gamma T-wDN_0=sa,
}
\]

\[
\boxed{
100\gamma T-(10w-1)DN_0=qb,
}
\]

并且

\[
\boxed{ab=t.}
\tag{3}

状态：**已严格完成。**

---

## 1. 对 `lambda D^4 Qb1` 做 Euclidean descent

记

\[
L=DT,
\qquad
H:=DTN_0-\gamma=N_0L-\gamma=h\lambda.
\]

因为 `h|Qb_1`，有

\[
H=h\lambda\mid\lambda Qb_1.
\]

于是当然

\[
H\mid\lambda D^4Qb_1.
\]

而

\[
\boxed{
\lambda D^4Qb_1
=
1000\lambda L^4
+c_2\lambda D^2L^2
+C_0\lambda D^4,
}
\tag{4}

其中

\[
c_2=10(1-20w),
\qquad
C_0=w(10w-1).
\]

对商按 `L` 做两级 Euclidean division，与 central / double-deep 的推导完全相同，得到整数 `U`：

\[
\boxed{
C_0\lambda D^4N_0^2
-U L N_0
+1000\lambda\gamma^2L^2
+\gamma U
+c_2\lambda D^2\gamma^2
=0.
}
\tag{5}

---

## 2. 仍然有 `D^2 | U`

模 `D` 看 (5)，只有 `gamma U` 可能不含 `D`。因为 `gcd(gamma,D)=1`：

\[
D\mid U.
\]

写 `U=DU_1`，再模 `D^2`：

\[
D\gamma U_1\equiv0\pmod{D^2}.
\]

故

\[
D\mid U_1.
\]

所以

\[
\boxed{D^2\mid U.}
\tag{6}

写

\[
\boxed{U=D^2u.}
\]

将 (5) 除以 `D^2`：

\[
\boxed{
C_0\lambda D^2N_0^2
-DuTN_0
+1000\lambda\gamma^2T^2
+\gamma u
+c_2\lambda\gamma^2
=0.
}
\tag{7}

---

## 3. universal natural square point

定义

\[
\boxed{
u_0:=10\lambda\gamma(20w-1).}
\tag{8}

从 (5) 解出 `u/D`，使用 `Gamma_k=gamma/D`：

\[
\boxed{
\frac uD
=\lambda
\frac{
C_0N_0^2+1000\Gamma_k^2T^2+c_2\Gamma_k^2
}{TN_0-\Gamma_k}.
}
\tag{9}

因此与 double-deep 相比只是整体乘上 `lambda`。同一组实数窗口给出安全界

\[
227000\lambda<\frac uD<15214000\lambda,
\]

而

\[
0<\frac{u_0}{D}<30813\lambda.
\]

所以

\[
\boxed{t:=u-u_0\in\mathbf Z_{>0}}
\tag{10}

且

\[
\boxed{
196000\lambda
<\frac tD
<15214000\lambda.
}
\tag{11}

---

## 4. `lambda` 从 factorization 中完全消失

把

\[
u=u_0+t
\]

代回 (7)。由于

\[
\gamma u_0+c_2\lambda\gamma^2=0,
\]

其余主项为

\[
\lambda\left[
C_0(DN_0)^2
-10(20w-1)(DN_0)(\gamma T)
+1000(\gamma T)^2
\right]
+t(\gamma-DTN_0).
\]

方括号精确因式分解为

\[
(wDN_0-10\gamma T)
((10w-1)DN_0-100\gamma T).
\]

而由 (1)：

\[
\gamma-DTN_0=-h\lambda.
\]

所以整体除以 `lambda` 后得到

\[
\boxed{
(wDN_0-10\gamma T)
((10w-1)DN_0-100\gamma T)
=t h.
}
\tag{12}

这证明了 universal factorization。

定义两个正因子

\[
\boxed{X_1:=10\gamma T-wDN_0,}
\]

\[
\boxed{X_2:=100\gamma T-(10w-1)DN_0.}
\]

则

\[
\boxed{X_1X_2=t h.}
\tag{13}

---

## 5. Q-side / b1-side 仍自动分流

完整 odd supply 为

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1,
\qquad \gcd(q,s)=1.
\]

(1) 给

\[
DTN_0\equiv\gamma\pmod h.
\]

因此

\[
TX_1\equiv\gamma b_1\equiv0\pmod s,
\]

\[
TX_2\equiv\gamma Q\equiv0\pmod q.
\]

`T` 与 `q,s` 互素，所以

\[
\boxed{s\mid X_1,}
\qquad
\boxed{q\mid X_2.}
\tag{14}

写

\[
X_1=sa,
\qquad
X_2=qb.
\]

由 (13)、`h=qs`：

\[
\boxed{ab=t.}
\tag{15}

因此 single-deep 与 double-deep 共享完全相同的 factor-pair / prime-supply skeleton。

---

## 6. universal congruence threshold

把 (7) 模 `D`。使用 `u_0=-c_2 lambda gamma`、`t=u-u_0`：

\[
\boxed{
 t\equiv-1000\lambda\gamma T^2\pmod D.
}
\tag{16}

右侧的 2/5 valuations 为

\[
\boxed{
 v_2(1000\lambda\gamma T^2)=2k+3+\lambda_2
}
\]

（当 `A>0` 时 `gamma` 是 2-adic unit；若 `A=0` 这一侧无 denominator excess），以及

\[
\boxed{
 v_5(1000\lambda\gamma T^2)=2k+3+\lambda_5
}
\]

在相应 deep side。

所以每个 deep prime side 都有统一 threshold

\[
\boxed{2k+3+\lambda_p.}
\tag{17}

超过 threshold 的 denominator excess 会精确转成 `t/D` 在该 prime 上的负 valuation；低于 threshold 则该 denominator prime power全部整除 `t`。

这把 single / double deep 的 excess geometry统一到同一个坐标系中。

---

## 7. 当前意义

此前：

- double-deep 有 global factorization；
- single-deep 主要通过 resonance / complement-height 单独处理。

本文说明二者其实拥有同一个 exact divisor skeleton：

\[
\boxed{
X_1=sa,
\qquad
X_2=qb,
\qquad
ab=t,
}
\]

以及同一个 shifted threshold

\[
2k+3+\lambda_p.
\]

因此下一阶段可以统一按 `t` 的 2/5 valuation 与 `a,b` 的 factor allocation 分类，而不再为 single / double deep 维护两套互不相干的算术框架。
# A1 minimal diagonal: global double-deep factorization and excess renormalization

> 日期：2026-08-20。依赖 `deep-complement-height.md` 与 minimal-diagonal odd-prime supply。当前统一范围 `k=g>=31`。

本文抽出 `deep-moderate-factorization.md` 背后的**全局**恒等式；这些结论不要求 `A,B<=2k+3`。

对任意 double-deep

\[
\Gamma_k=\frac{\gamma}{D},
\qquad
D=2^A5^B,
\qquad A,B>0,
\qquad \gcd(\gamma,10)=1,
\]

都存在一个正整数 `t`，使

\[
\boxed{
(10\gamma T-wDN_0)
(100\gamma T-(10w-1)DN_0)
=t(DTN_0-\gamma).
}
\]

进一步，若 `h=qs` 是完整 odd-prime supply 分裂，则两个 factor 自动分别吸收 `s` 与 `q`，从而

\[
\boxed{ab=t}
\]

对某些正整数 `a,b`。

`deep-moderate-factorization.md` 中的 `Dr` 只是这里 `t` 在 moderate 区域的特殊写法。

状态：**已严格完成。**

---

## 1. global deep supply quadratic

沿用

\[
T=10^k,
\qquad
L=DT,
\qquad
h=DTN_0-\gamma=N_0L-\gamma.
\]

对 `D^4Qb_1` 做两级 Euclidean descent，得到整数 `U` 满足

\[
C_0D^4N_0^2
-U L N_0
+1000\gamma^2L^2
+\gamma U
+c_2D^2\gamma^2
=0,
\tag{1}
\]

其中

\[
C_0=w(10w-1),
\qquad
c_2=10(1-20w).
\]

与 moderate 文件相同，模 `D`、再模 `D^2` 连续给出

\[
\boxed{D^2\mid U.}
\tag{2}
\]

写

\[
U=D^2u.
\]

则

\[
\boxed{
C_0D^2N_0^2
-DuTN_0
+1000\gamma^2T^2
+\gamma u
+c_2\gamma^2
=0.
}
\tag{3}

---

## 2. 天然平方点与正整数 `t`

定义

\[
\boxed{u_0:=10\gamma(20w-1).}
\]

由 (3) 解出 `u/D`：

\[
\boxed{
\frac uD
=
\frac{
C_0N_0^2+1000\Gamma_k^2T^2+c_2\Gamma_k^2
}{TN_0-\Gamma_k}.
}
\tag{4}

使用

\[
0.1T<N_0\le T,
\qquad
15.09<\Gamma_k<39.003,
\qquad T\ge10^{31},
\]

可取安全界

\[
227000<\frac uD<15214000,
\]

而

\[
0<\frac{u_0}{D}<30813.
\]

因此

\[
\boxed{t:=u-u_0\in\mathbf Z_{>0}}
\tag{5}
\]

并且统一有

\[
\boxed{
196000<\frac tD<15214000.
}
\tag{6}

---

## 3. global factorization

把

\[
u=u_0+t
\]

代回 (3)。由于

\[
\gamma u_0+c_2\gamma^2=0,
\]

得到精确恒等式

\[
\boxed{
(wDN_0-10\gamma T)
((10w-1)DN_0-100\gamma T)
=t(DTN_0-\gamma).
}
\tag{7}

两个左侧括号均为负。定义正整数

\[
\boxed{X_1:=10\gamma T-wDN_0,}
\]

\[
\boxed{X_2:=100\gamma T-(10w-1)DN_0.}
\]

则

\[
\boxed{X_1X_2=t h.}
\tag{8}

---

## 4. prime supply 仍精确分流

写完整 odd-prime supply

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1,
\qquad \gcd(q,s)=1.
\]

由

\[
DTN_0\equiv\gamma\pmod h
\]

分别模 `s,q`：

\[
TX_1\equiv\gamma b_1\equiv0\pmod s,
\]

\[
TX_2\equiv\gamma Q\equiv0\pmod q.
\]

因为 `T` 与 `q,s` 互素：

\[
\boxed{s\mid X_1,}
\qquad
\boxed{q\mid X_2.}
\tag{9}

所以存在正整数 `a,b`：

\[
\boxed{X_1=sa,}
\qquad
\boxed{X_2=qb.}
\]

结合 (8)、`h=qs`：

\[
\boxed{ab=t.}
\tag{10}

这条 factor-pair identity 对整个 double-deep 都成立。

---

## 5. `t` 的 2/5 congruence

把 (3) 模 `D`：

\[
1000\gamma^2T^2+\gamma u+c_2\gamma^2\equiv0\pmod D.
\]

用 `u_0=-c_2 gamma` 与 `t=u-u_0`：

\[
\boxed{
t\equiv-1000\gamma T^2\pmod D.
}
\tag{11}

又

\[
\boxed{
v_2(1000T^2)=v_5(1000T^2)=2k+3.}
\tag{12}

因此：

### 2-side

若 `A<=2k+3`，则

\[
\boxed{v_2(t)\ge A.}
\]

若 `A>2k+3`，由于 `gamma` 是 2-adic unit：

\[
\boxed{v_2(t)=2k+3.}
\tag{13}

### 5-side

若 `B<=2k+3`，则

\[
\boxed{v_5(t)\ge B.}
\]

若 `B>2k+3`：

\[
\boxed{v_5(t)=2k+3.}
\tag{14}

---

## 6. excess renormalization

定义 bounded positive rational

\[
\boxed{r_*:=\frac tD.}
\]

由 (6)：

\[
\boxed{196000<r_*<15214000.}
\tag{15}

由 (13)-(14)，`r_*` 的 reduced denominator 精确为

\[
\boxed{
\operatorname{den}(r_*)
=2^{(A-2k-3)_+}
 5^{(B-2k-3)_+}.
}
\tag{16}

所以超过 `2k+3` 的 deep excess 不会消失；它被完整地下沉成新的 bounded rational `r_*` 的 reduced denominator。

moderate 区域

\[
A,B\le2k+3
\]

恰好等价于

\[
\boxed{r_*\in\mathbf Z,}
\]

此时 `r_*=r`，恢复 `deep-moderate-factorization.md`。

---

## 7. extreme-excess 层数已有绝对粗上界

由 decade window

\[
\rho=\frac{h}{TD}\ge\frac T{10}
\]

以及 `h<=Qb_1<1000T^4`，得到

\[
\boxed{D<10000T^2.}
\tag{17}

因此

\[
A<2k\log_2 10+\log_2 10000,
\]

\[
B<2k\log_5 10+\log_5 10000.
\]

特别地，对 `k>=31`：

- `A` 不可能跨过四个完整的 `2k+3` blocks；
- `B` 不可能跨过两个完整的 `2k+3` blocks。

所以 excess renormalization 的层级本身只有绝对有限深度；真正需要继续研究的是如何把 bounded rational `r_*` 的剩余 `2/5` denominator 与 factor pair (10)、unit-square locks 和 complement-height 联立。

---

## 8. 与 moderate three-pattern 的关系

当 `r_*` 为整数时，(10) 变成

\[
ab=Dr,
\]

而 `deep-moderate-three-pattern.md` 已把整个 moderate region 压成 LL/LH/HL 三种显式模板。

因此 double-deep 的当前主线可以分为：

1. **moderate (`r_*` integer)**：已经是 three-pattern finite-width problem；
2. **extreme (`r_*` noninteger)**：其 denominator 正好记录 `A,B` 超过 `2k+3` 的 excess，并且 excess 层数由 (17) 绝对受限。
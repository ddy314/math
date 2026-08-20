# A1 minimal diagonal: moderate adjugate small remainders and gcd lock

> 日期：2026-08-20。依赖 `deep-moderate-factor-quotients.md`、`deep-four-factor-frame.md`、`deep-moderate-block-partition.md` 与 `deep-double-5high-collapse.md`。当前范围 `k=g>=31`。

moderate double-deep 现只剩 `LL` 与 `HL`。本文把 supply / complement 两条线性式同时 strip 掉已知的 2/5 powers。对应的 `2x2` determinant 恰为 `r_10`，所以取 adjugate 后得到右端只有 `alpha,beta` 的小余数式。

最终统一得到

\[
\boxed{
\gcd(N_0,h)=\gcd(N_0,\gamma)\mid r_{10}.
}
\]

因此 prefix integer `N_0` 与 normalized-gap numerator `gamma` 的 gcd 被绝对小参数 `r_10<15,214,000` 控制。

状态：**已严格完成。**

---

## 1. 公共记号

写

\[
N_0=2^{\nu_2}5^{\nu_5}n_0,
\qquad\gcd(n_0,10)=1,
\]

\[
r_{10}=r/2^{v_2(r)}5^{v_5(r)},
\qquad
\alpha\beta=r_{10},
\qquad
\gcd(\alpha,\beta)=1.
\]

完整 supply / complement 为

\[
h=qs,
\qquad qv=Q,
\qquad su=b_1,
\]

所以

\[
\boxed{qv-10su=1.}
\tag{1}
\]

另外 `gcd(Q,b_1)=1` 给

\[
\gcd(q,u)=\gcd(s,v)=1.
\tag{2}

---

## 2. `HL` 的两条 stripped equations

HL 中令

\[
Y:=B+\nu_5,
\qquad d:=k+1-Y>0.
\]

`deep-moderate-factor-quotients.md` 给

\[
a=2^{k+1}5^Y\alpha,
\qquad
b=2^{k+2}5^Y\beta.
\]

从 complementary relation

\[
bu-av=10T
\]

除去 `2^(k+1)5^Y`：

\[
\boxed{
2\beta u-\alpha v=5^d.
}
\tag{3}

另一方面 supply relation

\[
qb-10sa=DN_0
\]

给

\[
2^{k+2}5^Y(\beta q-5\alpha s)
=2^{A+\nu_2}5^Y n_0.
\]

因为 HL 有

\[
A=2k+3-v_2(r),
\]

定义

\[
\boxed{
c':=A+\nu_2-k-2
=k+1-v_2(r)+\nu_2>0,}
\]

得到

\[
\boxed{
\beta q-5\alpha s=2^{c'}n_0.
}
\tag{4}

---

## 3. `HL` 的 adjugate small remainders

把

\[
X:=\beta q,
\quad Y_1:=5\alpha s,
\quad U:=2\beta u,
\quad V:=\alpha v.
\]

则 (3)-(4) 是

\[
X-Y_1=2^{c'}n_0,
\qquad
U-V=5^d.
\]

而由 (1)：

\[
XV-Y_1U
=\alpha\beta(qv-10su)
=r_{10}.
\tag{5}

因此

\[
(X-Y_1)V-(U-V)Y_1=r_{10},
\]

除以 `alpha`：

\[
\boxed{
2^{c'}n_0v-5^{d+1}s=\beta.
}
\tag{6}

同理

\[
(X-Y_1)U-(U-V)X=r_{10},
\]

除以 `beta`：

\[
\boxed{
2^{c'+1}n_0u-5^dq=\alpha.
}
\tag{7}

---

## 4. `LL` 的 adjugate small remainders

LL 中写

\[
u=2^e u_0,
\qquad e=v_2(w),
\]

并定义

\[
c=k+1-(A+\nu_2+e)>0,
\qquad
d=k+1-(B+\nu_5)>0.
\]

strip complementary relation 得

\[
\boxed{
\beta u_0-\alpha v=2^c5^d.
}
\tag{8}

strip supply relation 得

\[
\boxed{
\beta q-2^{e+1}5\alpha s=n_0.
}
\tag{9}

这里使用

\[
q b-10sa=DN_0
\]

以及 LL 的

\[
a=2^{A+\nu_2+e}5^{B+\nu_5}\alpha,
\quad
b=2^{A+\nu_2}5^{B+\nu_5}\beta.
\]

注意由 `u=2^e u_0`，(1) 等价于

\[
qv-2^{e+1}5su_0=1.
\tag{10}

和 HL 完全同样的 determinant 计算给

\[
\boxed{
n_0v-2^{c+e+1}5^{d+1}s=\beta,}
\tag{11}

\[
\boxed{
n_0u_0-2^c5^dq=\alpha.}
\tag{12}

---

## 5. gcd lock

从 HL 的 (7)：若 `p|n_0` 且 `p|q`，则 `p|alpha`。因此

\[
\gcd(n_0,q)\mid\alpha.
\]

从 (6)：

\[
\gcd(n_0,s)\mid\beta.
\]

LL 的 (11)-(12) 给出完全相同的结论。

而 `q|Q`、`s|b_1`、`gcd(Q,b_1)=1`，故 `q,s` 互素。因此

\[
\gcd(n_0,qs)
=\gcd(n_0,q)\gcd(n_0,s)
\mid\alpha\beta=r_{10}.
\]

由于 `h=qs` 与 10 互素：

\[
\boxed{
\gcd(N_0,h)=\gcd(n_0,h)\mid r_{10}.
}
\tag{13}

在 double-deep 中

\[
h=DTN_0-\gamma,
\]

所以

\[
\gcd(N_0,h)=\gcd(N_0,\gamma).
\]

最终：

\[
\boxed{
\gcd(N_0,\gamma)\mid r_{10}.
}
\tag{14}

又

\[
196000<r<15214000,
\]

故

\[
\boxed{
\gcd(N_0,\gamma)<15,214,000.
}
\tag{15}

---

## 6. 当前用途

moderate `LL/HL` 现在除了 `r`、block-partition `(alpha,beta)` 外，还满足 gap numerator 与 decimal prefix 的 absolute gcd lock (14)。

这可直接加入：

- `deep-moderate-root-normal-form.md` 的 reduced-denominator 恢复；
- `deep-complement-height.md` 的 rational denominator cancellation；
- 后续对 `N_0` / `gamma` 的 resultant 或 primitive-divisor 分析。

尤其不能再允许 `gcd(N_0,gamma)` 随 `k` 自由增长。
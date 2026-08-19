# A1 minimal diagonal: extreme double-deep classification

> 日期：2026-08-20。依赖 `deep-global-factorization.md`、`deep-balanced-collapse.md`。当前范围 `k=g>=31`。

本文处理 double-deep 中超出 moderate threshold

\[
2k+3
\]

的 exponent。结论是：两侧不可能同时 extreme；任何 extreme candidate 只能是一侧 extreme-high、另一侧 shallow-low。

状态：**已严格完成。**

---

## 1. 两侧不能同时 extreme

已有粗 decade/supply 上界

\[
\boxed{D=2^A5^B<10000T^2.}
\tag{1}

若两侧同时 extreme，则整数指数至少满足

\[
A\ge2k+4,
\qquad
B\ge2k+4.
\]

于是

\[
D\ge2^{2k+4}5^{2k+4}
=10^{2k+4}
=10000T^2,
\]

与 (1) 矛盾。因此

\[
\boxed{
A>2k+3
\Longrightarrow B\le2k+3,
}
\tag{2}

\[
\boxed{
B>2k+3
\Longrightarrow A\le2k+3.
}
\tag{3}

所以 excess renormalization 的 reduced denominator永远只可能是纯 `2`-power 或纯 `5`-power，不会同时含两个 extreme prime sides。

---

## 2. 2-extreme 自动是 2-high

设

\[
A\ge2k+4.
\]

在 universal factor

\[
X_1=10\gamma T-wDN_0,
\]

两项的 2-adic valuations 为

\[
k+1,
\qquad A+e+\nu_2>k+1.
\]

因此

\[
\boxed{v_2(X_1)=k+1.}
\tag{4}

同理 `X_2` 两项赋值为

\[
k+2,
\qquad A+\nu_2>k+2,
\]

故

\[
\boxed{v_2(X_2)=k+2.}
\tag{5}

由于 `q,s` 与 2 互素且 `ab=t`：

\[
\boxed{v_2(t)=2k+3.}
\tag{6}

这也与 universal congruence

\[
t\equiv-1000\gamma T^2\pmod{2^A}
\]

完全一致。

定义 2-excess

\[
\boxed{E:=A-(2k+3)>0.}
\]

则

\[
\boxed{v_2(t/D)=-E.}
\tag{7}

---

## 3. fully-balanced collapse 强迫 5-shallow

2-extreme 下显然

\[
A+e+\nu_2>k.
\]

若再有

\[
B+\nu_5\ge k,
\]

则落入 `deep-balanced-collapse.md` 已排除的 double-deep balanced region。

所以任何 2-extreme candidate 必须满足

\[
\boxed{B+\nu_5<k.}
\tag{8}

特别地 5-side 一定处于 strict low branch，因为

\[
B+\nu_5<k<k+1.
\]

于是从 factor pair 的 5-adic valuation：

\[
\boxed{
v_5(X_1)=v_5(X_2)=B+\nu_5,}
\tag{9}

\[
\boxed{
v_5(t)=2B+2\nu_5.}
\tag{10}

所以 2-extreme 的唯一模板是

\[
\boxed{
2\text{-high extreme}/5\text{-low shallow}.}
\tag{11}

---

## 4. 5-extreme 完全对称

若

\[
B\ge2k+4,
\]

则

\[
\boxed{v_5(X_1)=k+1,}
\qquad
\boxed{v_5(X_2)=k+2,}
\]

所以

\[
\boxed{v_5(t)=2k+3.}
\tag{12}

定义

\[
\boxed{F:=B-(2k+3)>0,}
\]

则

\[
\boxed{v_5(t/D)=-F.}
\tag{13}

另一方面 balanced collapse 强迫

\[
\boxed{A+e+\nu_2<k.}
\tag{14}

因此 2-side 严格 low：

\[
\boxed{
v_2(X_1)=A+e+\nu_2,}
\]

\[
\boxed{
v_2(X_2)=A+\nu_2,}
\]

\[
\boxed{
v_2(t)=2A+2\nu_2+e.}
\tag{15}

所以 5-extreme 的唯一模板是

\[
\boxed{
2\text{-low shallow}/5\text{-high extreme}.}
\tag{16}

---

## 5. double-deep 的完整五模板分类

结合 `deep-moderate-three-pattern.md`：

### moderate

1. LL;
2. LH;
3. HL.

### extreme

4. 2-extreme HL：
   \[
   A\ge2k+4,
   \qquad B+\nu_5<k;
   \]
5. 5-extreme LH：
   \[
   B\ge2k+4,
   \qquad A+e+\nu_2<k.
   \]

不存在：

- transition strips；
- high-high；
- both-extreme。

因此

\[
\boxed{
\text{double-deep}
=LL\cup LH\cup HL\cup E_2\cup E_5.
}
\tag{17}

这已经把原始二维 `(A,B)` 平面替换成五条明确的 valuation templates。

---

## 6. extreme renormalized parameter

`deep-global-factorization.md` 定义

\[
r_*:=t/D,
\qquad
196000<r_*<15214000.
\]

在 2-extreme 中，由 (7)、而 5-side moderate：

\[
\boxed{
\operatorname{den}(r_*)=2^E.
}
\tag{18}

在 5-extreme 中：

\[
\boxed{
\operatorname{den}(r_*)=5^F.
}
\tag{19}

所以 extreme 分支各自只剩**单素数 denominator excess**。下一步可分别对 pure-2 与 pure-5 bounded rational `r_*` 做一维 denominator descent / local modular analysis。
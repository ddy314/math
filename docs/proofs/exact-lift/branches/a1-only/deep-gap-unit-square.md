# A1 minimal diagonal: deep-gap unit-square locks

> 日期：2026-08-19。依赖 `deep-gap-valuation-normal-form.md` 与 `diagonal.md` 的 odd-prime supply theorem。当前统一范围 `k=g>=26`。

已有 deep-gap 正规形

\[
\Gamma_k=\frac{\gamma}{2^A5^B},
\qquad
V^2=J+2\Gamma_kQN,
\]

其中

\[
v_2(J)=2v_2(w),
\qquad v_5(J)=0.
\]

上一层只使用了平方赋值必须为偶数。本文继续保留平方的**单位部分**，得到新的局部锁。

核心结论：

1. 在 strict 2-adic low-side，
   \[
   \boxed{\gamma QN_2 5^B\equiv1\pmod8,}
   \qquad N_2=N/2^{v_2(N)};
   \]
2. 于是所有 2-deep strict-low candidate 满足
   \[
   \boxed{
   w\in\{1,3\}\Longrightarrow h\equiv1\pmod4,
   }
   \]
   \[
   \boxed{
   w\in\{2,4\}\Longrightarrow h\equiv3\pmod4;
   }
   \]
3. 因为 `h=qs` 且 `s` 是 `1 mod 4` whole-block selector，故 Q-side 因子被定向为
   \[
   \boxed{
   w\text{ odd}\Longrightarrow q\equiv1\pmod4,
   \qquad
   w\text{ even}\Longrightarrow q\equiv3\pmod4.
   }
   \]
4. 在 strict 5-adic low-side 还得到显式 Legendre lock。

状态：**已严格完成。**

---

## 1. 2-adic strict-low 的单位平方条件

记

\[
n_2=v_2(N),
\qquad N_2=N/2^{n_2}.
\]

若 `A>0` 且位于 strict 2-adic low-side，则

\[
v_2(2\Gamma_kQN)=1+n_2-A
< v_2(J).
\]

已经证明该赋值必须为偶数。提出全部 2 次幂后，剩余 2-adic 单位为

\[
\gamma QN_2 5^{-B}.
\]

在模 8 中

\[
5^{-1}\equiv5\pmod8,
\]

所以 `5^{-B}≡5^B mod 8`。2-adic 单位平方必须同余 `1 mod 8`，于是

\[
\boxed{
\gamma QN_2 5^B\equiv1\pmod8.
}
\tag{1}
\]

这是 parity lock 之外真正新的 square-unit information。

---

## 2. even `w`：单位条件统一成 `gamma 5^B=1 mod 8`

### `w=2`

`b_1` 为偶数且 `gcd(a_1,b_1)=1`，故 `a_1` 为奇数，已有 `n_2=0`。

模 8：

\[
b_1\equiv6,
\]

而 `a_2` 为奇数，所以

\[
(a_2b_1)^2\equiv4\pmod8.
\]

因此

\[
N\equiv1+4=5\pmod8.
\]

同时

\[
Q=10b_1+1\equiv5\pmod8.
\]

故

\[
\boxed{QN_2\equiv5\cdot5\equiv1\pmod8.}
\tag{2}
\]

### `w=4`

同样 `a_1` 为奇数、`n_2=0`。此时

\[
b_1\equiv4\pmod8,
\]

所以

\[
(a_2b_1)^2\equiv0\pmod8,
\qquad N\equiv1\pmod8.
\]

并且

\[
Q\equiv1\pmod8.
\]

因此仍有

\[
\boxed{QN_2\equiv1\pmod8.}
\tag{3}
\]

由 (1)：

\[
\boxed{
\gamma5^B\equiv1\pmod8
\qquad(w=2,4).
}
\tag{4}
\]

---

## 3. even `w` 进一步强迫 `h=3 mod 4`

2-deep 意味着

\[
x=-k-A,
\qquad A>0.
\]

若 `B>0`，则同时 `y=-k-B`，从 gap 定义直接得到既约分子

\[
\gamma=2^A5^B10^kN_0-h.
\]

故

\[
\gamma\equiv-h\pmod8.
\tag{5}
\]

若 `B=0`，则 `y>=-k`。写

\[
e_5:=k+y\ge0.
\]

此时

\[
\gamma=2^A10^kN_0-h5^{e_5},
\]

所以

\[
\gamma\equiv-h5^{e_5}\pmod8.
\tag{6}
\]

结合 (4)：

- `B>0` 时
  \[
  h\equiv-5^B\pmod8;
  \]
- `B=0` 时
  \[
  h\equiv-5^{e_5}\pmod8.
  \]

而 `5^m mod 8` 只可能是 `1` 或 `5`，所以两种情况统一给出

\[
\boxed{
h\equiv3\text{ or }7\pmod8,}
\]

特别地

\[
\boxed{
h\equiv3\pmod4
\qquad(w=2,4).}
\tag{7}
\]

---

## 4. odd `w`：统一得到 `h=1 mod 4`

现在 `w=1,3`。模 4 有

\[
Q=10b_1+1\equiv3\pmod4.
\tag{8}
\]

还要证明

\[
\boxed{N_2\equiv1\pmod4.}
\tag{9}
\]

若 `n_2=0`，则 `a_1` 为偶数、`a_2b_1` 为奇数，所以

\[
N\equiv1\pmod4,
\]

即 (9)。

若 `n_2=1`，则 `a_1` 与 `a_2b_1` 都是奇数。两个奇平方均为 `1 mod 8`，故

\[
N\equiv2\pmod8,
\]

所以

\[
N_2=N/2\equiv1\pmod4.
\]

于是 (9) 对两种 `n_2` 都成立。

把 (1) 降模 4；`5^B≡1 mod 4`，故

\[
\gamma\cdot3\cdot1\equiv1\pmod4,
\]

从而

\[
\boxed{\gamma\equiv3\pmod4.}
\tag{10}
\]

另一方面，无论 `B>0` 还是 `B=0`，上一节的 gap numerator 公式降模 4 都统一给出

\[
\gamma\equiv-h\pmod4
\]

（因为任意 `5` 次幂均为 `1 mod 4`）。因此

\[
\boxed{
h\equiv1\pmod4
\qquad(w=1,3).}
\tag{11}
\]

---

## 5. Q-side orientation lock

minimal-diagonal odd-prime supply 精确写成

\[
h=qs,
\qquad q\mid Q,
\]

其中 `s` 是 `b_1` 中所有 `1 mod 4` prime-power blocks 的 whole-block selector。

所以必有

\[
\boxed{s\equiv1\pmod4.}
\tag{12}
\]

由 (7)、(11)：

\[
\boxed{
 w\in\{1,3\}
 \Longrightarrow
 q\equiv1\pmod4,
}
\tag{13}
\]

\[
\boxed{
 w\in\{2,4\}
 \Longrightarrow
 q\equiv3\pmod4.
}
\tag{14}
\]

这给 deep strict-2-low sector 一个新的 prime-supply 方向性：Q-side 因子不能再从 `Q` 的全部 divisors 中任意选取。

特别地，对 even `w`，任何 2-deep candidate 都要求 `Q` 实际提供一个 `3 mod 4` divisor；若某个 fixed layer 的 `Q` 没有这种供给，则该层的整个 2-deep sector立即为空。

---

## 6. 5-adic strict-low 的 Legendre lock

记

\[
n_5=v_5(N),
\qquad N_5=N/5^{n_5}.
\]

若

\[
B>n_5,
\]

则 second term 严格承担五进低赋值。提出 `5^{n_5-B}` 后，单位为

\[
2^{1-A}\gamma QN_5.
\]

又 `Q≡1 mod 5`，故必须有

\[
\boxed{
\left(\frac{2^{1-A}\gamma N_5}{5}\right)=1.
}
\tag{15}
\]

定义

\[
\lambda_2:=
\begin{cases}
0,&A>0,\\
k+x,&A=0,
\end{cases}
\]

则 `lambda_2>=0`，而 gap numerator 在模 5 下统一给出

\[
\gamma\equiv-h2^{\lambda_2}\pmod5.
\tag{16}
\]

由于

\[
\left(\frac{-1}{5}\right)=1,
\qquad
\left(\frac2{5}\right)=-1,
\]

(15)-(16) 化成

\[
\boxed{
\left(\frac{hN_5}{5}\right)
=(-1)^{1-A+\lambda_2}.
}
\tag{17}
\]

所以 5-deep strict-low 也不只有 `B≡n_5 mod 2` 的 valuation parity；其 5-adic 单位特征被精确锁定。

---

## 7. 当前 deep 核心

结合 `deep-gap-valuation-normal-form.md`，deep sector 现在同时受到：

1. `A,B` 的 resonance/奇偶格；
2. strict 2-low 的 mod-8 square-unit lock (1)；
3. Q-side orientation (13)-(14)；
4. strict 5-low 的 Legendre lock (17)；
5. primitive cross-corridor caps 与 decade window。

因此后续 fixed-layer 或统一 deep 证书应直接按这些局部单位类筛 `h=q s`，而不再只按 `(A,B)` 的赋值奇偶扫描。
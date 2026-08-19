# A2 source odd-parity reuse 再进入 angle common 的 mixed support budget

> **依赖：** `spontaneous-source-parity-angle-overlap.md`、`spontaneous-source-parity-numerator-defect.md`、`endpoint-lattice.md` 的真实 denominator scale。
>
> **严格状态：**source odd/odd reused prime若还同时进入 angle actual/conjugate common support，只剩 numerator-defect sheet `324e-11` 或 denominator sheet `c_Q`。本文利用真实 third denominator ratio `w=2^(M+1)c_Qc_u/5^lambda<1` 给 `c_Q` 全局高度上界，并把全部 source-angle reused distinct support聚合为 `R_SA | c_Q(324e-11)`。这给出 mixed decimal/2-adic product budget，但不证明该 radical为空，因此不关闭 A2。

---

## 1. denominator height

当前真实 denominator scale给

\[
\boxed{
w=\frac{2^{M+1}c_Qc_u}{5^\lambda}<1,}
\tag{1.1}
\]

并且

\[
\boxed{\lambda\le m.}
\tag{1.2}
\]

所有量为正整数，所以从 (1.1)：

\[
c_Q<\frac{5^\lambda}{2^{M+1}c_u}.
\]

由于 `c_u>=1` 与 (1.2)：

\[
\boxed{
c_Q<\frac{5^m}{2^{M+1}}.}
\tag{1.3}
\]

这是不固定 `eta=2m-M` 的 uniform denominator-content height bound。

---

## 2. two allowed angle-common sheets

前文已经证明：若 genuine inert prime `r`

1. 同时承担 `B_W` 与 `D_W` 的 odd parity；
2. 又进入 angle actual/conjugate common gcd；

则必有

\[
\boxed{r\mid c_Q}
\tag{2.1}
\]

或者进入 numerator sheet并进一步满足

\[
\boxed{r\mid324e-11.}
\tag{2.2}
\]

generic `q`-sheet已经删除。

---

## 3. aggregate source-angle reused radical

令 `E_SA` 为所有同时满足 source odd/odd reuse 与 angle-common reuse的 genuine inert primes，并定义

\[
\boxed{R_{SA}:=\prod_{r\in E_{SA}}r.}
\tag{3.1}
\]

每个 distinct prime按 (2.1)/(2.2) 至少整除两个 integers之一，所以

\[
\boxed{R_{SA}\mid c_Q(324e-11).}
\tag{3.2}
\]

这里若某 prime同时整除两者，也只在 radical中计一次，因此 divisibility仍成立。

---

## 4. mixed height budget

numerator defect theorem给

\[
0<324e-11<\frac{81}{625}N.
\tag{4.1}
\]

结合 (1.3)、(3.2)：

\[
\boxed{
R_{SA}
<
\frac{81}{625}N\,
\frac{5^m}{2^{M+1}}.}
\tag{4.2}

用 `N=10^M=2^M5^M` 也可写成

\[
\boxed{
R_{SA}
<
\frac{81}{1250}
5^{M+m}.}
\tag{4.3}

因为

\[
\frac{10^M}{2^{M+1}}=\frac{5^M}{2}.
\]

这说明 source parity若连续复用到 angle common，distinct moving support只能在一个显式 `5^(M+m)` 尺度内增长。

---

## 5. combine with source reuse depth

source odd/odd reuse本身还有 weighted half-depth product

\[
H_{\rm reuse}\mid18K-55<180N.
\]

所以 `E_SA` 子池同时受到：

\[
\boxed{
\prod_{r\in E_{SA}}r^{(e_r+1)/2}<180N,}
\tag{5.1}
\]

和

\[
\boxed{
\prod_{r\in E_{SA}}r
<
\frac{81}{625}N\frac{5^m}{2^{M+1}}.}
\tag{5.2}
\]

第一式惩罚 odd source depth，第二式惩罚 distinct support。

---

## 6. current role

source-side两份 parity若完全 separate，会直接产生独立 primes；若复用，则支付 `18K-55` half-depth；若这枚 reused support还想被 angle pair再次 common-reuse，又必须支付本文的 `c_Q(324e-11)` mixed height。

因此 parity reuse现在形成严格的层级收费：

\[
\boxed{
\text{source reuse}
\Longrightarrow
\text{linear half-depth};
}
\]

\[
\boxed{
\text{source + angle reuse}
\Longrightarrow
\text{linear half-depth + mixed support budget}.}
\]

下一步若再把 additive individual residual support接入，就可以审计三重 parity reuse是否只剩 fixed denominator/numerator-length states。

A2 仍为 `待证`。

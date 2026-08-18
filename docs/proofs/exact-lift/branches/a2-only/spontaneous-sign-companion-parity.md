# A2 angle/additive 的 natural sign-companion parity pairs

> **依赖：** `spontaneous-angle-parity.md`、`spontaneous-height-parity-ledger.md`、`height-cofactor.md`。
>
> **严格状态：**本文指出 actual angle 与 actual additive primitive carriers各自都有一个自然的 third-coordinate sign companion。四个 primitive integers全部为正且 `3 mod 4`。actual/conjugate angle pair的共同 odd support只能来自 prefix numerator/denominator content；actual/conjugate additive pair的共同 odd support只能来自 central factor `2K-9` 或 third-numerator content `a_3`。因此在 generic prefix-content-free、noncentral external sector中，每一对的 odd-inert parity不能复用同一 prime。本文是 global parity allocation结构，不宣称 A2 closure。

---

## 1. 记号

固定 reflection endpoint：

\[
N=10^M,
\qquad T=10^m,
\qquad A=a_2,
\qquad B=b_2,
\]

\[
Q=B+2N,
\qquad K=9N+10A,
\]

\[
N_0=\left(\frac{9B}{2}\right)^2+A^2.
\]

并使用

\[
B=2^{M+m+1}c_ug,
\qquad
Q=2^{M+1}Q_0,
\]

\[
b_3=2^{M+m+1}5^dc_Qc_u.
\]

---

# angle sign pair

## 2. actual / conjugate angle sheets

定义

\[
\mathcal U_\Omega
=(45B^2-2AN)^2-A^2B(99B-4N),
\]

\[
\boxed{
\mathcal O_\pm
=T\mathcal U_\Omega\pm2A^2Qb_3.
}
\tag{2.1}
\]

actual spontaneous angle carrier是 `O_+`。`spontaneous-height-parity-ledger.md` 已证明

\[
\boxed{
\widehat{\mathcal O}_\pm
:=\frac{\mathcal O_\pm}{2^{2M+m+2}}>0,
\qquad
\widehat{\mathcal O}_\pm\equiv3\pmod4.
}
\tag{2.2}
\]

两者差为

\[
\mathcal O_+-\mathcal O_-=4A^2Qb_3.
\]

除去 primitive scale：

\[
\boxed{
\widehat{\mathcal O}_+
-
\widehat{\mathcal O}_-
=4A^2Q_0\,5^dc_Qc_u.
}
\tag{2.3}
\]

因此若

\[
D_O:=\gcd(\widehat{\mathcal O}_+,\widehat{\mathcal O}_-),
\]
则任何 odd prime `p|D_O` 必整除

\[
A Q_0 5c_Qc_u.
\]

又 actual angle primitive 已与 `c_ug` 本原分离，所以对 genuine non-`5` inert prime：

\[
\boxed{
 p\mid D_O
\Longrightarrow
p\mid A Q_0c_Q.
}
\tag{2.4}
\]

故 prefix numerator / denominator content-free 的 external prime不可能同时命中两张 angle sign sheets。

---

# additive sign pair

## 3. actual additive carrier与 third-numerator conjugate

定义

\[
\boxed{
\mathcal R_\Theta
:=B^2(K^2-18K+55)-Q^2N_0.
}
\tag{3.1}
\]

actual additive carrier为

\[
\boxed{
\Theta_-
:=T\mathcal R_\Theta
-2B^2(2K-9)a_3
=\Theta_{\rm dec}.
}
\tag{3.2}
\]

定义 third-numerator sign companion

\[
\boxed{
\Theta_+
:=T\mathcal R_\Theta
+2B^2(2K-9)a_3.
}
\tag{3.3}
\]

两者差：

\[
\boxed{
\Theta_+-\Theta_-
=4B^2(2K-9)a_3.
}
\tag{3.4}
\]

已有

\[
\Theta_-
=2^{2M+m+2}\widehat{\mathcal T}_2,
\]

\[
\widehat{\mathcal T}_2>0,
\qquad
\widehat{\mathcal T}_2\equiv3\pmod4.
\tag{3.5}
\]

---

## 4. conjugate additive carrier具有完全相同的 primitive orientation

由

\[
B=2^{M+m+1}c_ug,
\]
(3.4) 的 2-adic depth为

\[
2M+2m+4.
\]

相比 actual primitive scale

\[
2M+m+2,
\]
多出

\[
\boxed{m+2\ge3}
\tag{4.1}
\]
层。因此定义

\[
\boxed{
\widehat\Theta_+
:=\frac{\Theta_+}{2^{2M+m+2}}
}
\tag{4.2}
\]
后有精确整数差

\[
\boxed{
\widehat\Theta_+
-
\widehat{\mathcal T}_2
=2^{m+2}(c_ug)^2(2K-9)a_3.
}
\tag{4.3}
\]

右端被 `8` 整除，所以

\[
\boxed{
\widehat\Theta_+
\equiv
\widehat{\mathcal T}_2
\pmod8.
}
\tag{4.4}
\]

特别地

\[
\boxed{
\widehat\Theta_+\equiv3\pmod4.
}
\tag{4.5}
\]

正性也无需重新估计。当前 endpoint

\[
2K-9>0,
\qquad a_3>0,
\]
所以由 (3.4)：

\[
\Theta_+>\Theta_->0.
\]
故

\[
\boxed{
\widehat\Theta_+>0.
}
\tag{4.6}
\]

因此 additive actual / conjugate也是一对 positive primitive `3 mod 4` carriers。

---

## 5. additive sign pair 的 common support

令

\[
D_T:=\gcd(
\widehat{\mathcal T}_2,
\widehat\Theta_+
).
\tag{5.1}
\]

由 (4.3)，`D_T` 为 odd 且

\[
D_T
\mid
(c_ug)^2(2K-9)a_3.
\]

但已有本原性

\[
\gcd(\widehat{\mathcal T}_2,10c_ug)=1.
\]

所以：

\[
\boxed{
D_T\mid |(2K-9)a_3|.
}
\tag{5.2}
\]

逐 prime 写就是

\[
\boxed{
 p\mid\widehat{\mathcal T}_2,
\ p\mid\widehat\Theta_+
\Longrightarrow
p\mid(2K-9)a_3.
}
\tag{5.3}
\]

因此 noncentral 且 third-numerator-content-free 的 generic external prime不可能同时命中 additive actual / conjugate sheets。

---

## 6. 两对 parity 的共同抽象结构

现在有四个 positive `3 mod 4` primitive integers：

\[
\boxed{
\widehat{\mathcal O}_+,
\quad
\widehat{\mathcal O}_-,
\quad
\widehat{\mathcal T}_2,
\quad
\widehat\Theta_+.
}
\tag{6.1}
\]

每一对都满足：

- actual 与 conjugate同为 `3 mod 4`；
- 去掉 pair gcd 后，两个 quotient互素且具有相同 mod-4 orientation；
- pair gcd若为 `1 mod 4`，两个 quotient都会是 `3 mod 4`，因此必须分别携带 odd inert parity；
- generic external prime不能在同一 sign pair中重复承担这两份 parity。

两对的例外 support完全显式：

\[
\boxed{
\begin{array}{c|c}
\text{pair}&\text{possible common odd support}\\ \hline
(O_+,O_-)&A Q_0c_Q\quad(\text{plus fixed }5/content)\\
(\Theta_-,\Theta_+)&(2K-9)a_3.
\end{array}}
\tag{6.2}
\]

因此 global `G_sp` parity问题现在不再只有两个 carrier；每个 actual carrier都带一个自然 companion。若最终要维持 `G_sp\equiv1 mod4`，odd parity必须在这四张 sheets及其显式 content exceptions之间完成一致分配。

---

## 7. 下一步：cross-sign sphere

同一 sign pair内部的 overlap已经由本文固定。剩余真正可能让 parity重新合流的是 cross-sign pair：

\[
(O_-,\Theta_-),
\qquad
(O_+,\Theta_+).
\]

它们不是任意新方程：`O_-` 对应第三分母 angle root取相反符号，`Theta_+` 对应第三分子 additive root取相反符号。把这些 sign roots代回 exact sphere即可得到 cross-sign pure-prefix norms。

若 cross-sign norms也只能回流到已知 height/source/content sheets，那么 `G_sp\equiv1 mod4` 所要求的分居 parity会被进一步强迫成多个互不复用的 pure external decimal orbits。

# A1 safe integer-gap recovery — 2026-08-16

本文把 A1 rational-contact 框架重新接回整数球面，但完全避免使用有问题的 `a_3/\delta_3` 整数化。

核心结果是一个安全的 primitive gap recovery：

\[
\boxed{10^\ell E=b_3U}
\]

以及由此严格推出

\[
\boxed{U=LA,\qquad E=\tau A}
\]

其中 `A` 是新的正整数 gap 参数，与第三分子 `a_3` 无关。

本文结论均为 **已严格完成**。

---

## 1. 整数球面对象

令

\[
q=\operatorname{lcm}(b_1,b_2,b_3),
\]

并定义

\[
y_i=qr_i=\frac{qa_i}{b_i}.
\]

exact lift 强迫存在正整数 `H` 满足

\[
\boxed{H=qR}
\]

以及

\[
\boxed{H^2=y_1^2+y_2^2+y_3^2}.
\]

A1 rational-contact 框架中

\[
P=\frac CD,
\qquad
D=10^gQ,
\qquad
T=10^\ell,
\]

并有

\[
R=\frac{P+\theta r_3}{1+\theta},
\qquad
\theta=\frac{b_3}{TD}.
\]

等价地

\[
P-R=\theta(R-r_3).
\tag{1}
\]

---

## 2. contact gap 的整数化

定义两个正整数候选 gap：

\[
\boxed{E=Cq-DH}
\]

以及

\[
\boxed{U=H-y_3}.
\]

因为 A1 中

\[
P>R>r_3,
\]

故

\[
E>0,
\qquad U>0.
\]

把 (1) 写成

\[
\frac{Cq-DH}{Dq}
=
\frac{b_3}{TD}
\cdot
\frac{H-y_3}{q}.
\]

直接清分母得到

\[
\boxed{
T E=b_3 U.
}
\tag{2}
\]

这条等式完全由原始 exact lift 和整数球面推出，不需要 Gaussian integers，也没有对 `a_3` 做任何额外整除假设。

---

## 3. 安全的 `L,\tau` primitive recovery

定义

\[
\delta=\gcd(T,b_3),
\]

\[
\boxed{L=\frac T\delta},
\qquad
\boxed{\tau=\frac{b_3}{\delta}}.
\]

于是

\[
\gcd(L,\tau)=1.
\]

把 (2) 除以 `\delta`：

\[
L E=\tau U.
\]

由于 `L` 与 `\tau` 互素：

\[
L\mid U,
\qquad
\tau\mid E.
\]

因此存在唯一正整数 `A` 使

\[
\boxed{U=LA}
\]

以及

\[
\boxed{E=\tau A}.
\tag{3}
\]

这就是 A1 中合法的 primitive gap 参数。

需要特别强调：

\[
\boxed{A\text{ 与原第三分子 }a_3\text{ 没有被证明相等，也不应混同。}}
\]

旧公共框架中若某处把 `\delta\mid b_3` 进一步解释成 `\delta\mid a_3`，该步骤不能由 (2)–(3) 支持。

---

## 4. 球面因子分解恢复

由

\[
H^2-y_3^2=y_1^2+y_2^2
\]

有

\[
U(H+y_3)=y_1^2+y_2^2.
\]

代入 `U=LA`：

\[
\boxed{
LA(H+y_3)=y_1^2+y_2^2.
}
\tag{4}
\]

所以

\[
\boxed{LA\mid y_1^2+y_2^2.}
\tag{5}
\]

并且

\[
H+y_3
=
\frac{y_1^2+y_2^2}{LA}.
\]

与

\[
H-y_3=LA
\]

联立，严格恢复

\[
\boxed{
H
=\frac12\left(
LA+rac{y_1^2+y_2^2}{LA}
\right),
}
\tag{6}
\]

\[
\boxed{
y_3
=\frac12\left(
\frac{y_1^2+y_2^2}{LA}-LA
\right).
}
\tag{7}
\]

因此旧 A1 基线中的球面 gap 分解可以保留，但其中的整数 `a` 应明确理解为本文的 gap 参数 `A`，不能理解成由 `a_3/\delta` 得到的第三分子正规化。

---

## 5. LCM 前缀化

令

\[
B=\operatorname{lcm}(b_1,b_2),
\qquad
d=\gcd(B,b_3).
\]

则

\[
q=\operatorname{lcm}(B,b_3)
=\frac{Bb_3}{d}.
\]

定义

\[
\boxed{c=\frac Bd},
\qquad
\boxed{t=\frac{b_3}{d}}.
\]

于是

\[
q=b_3c=Bt.
\]

第三坐标变成

\[
\boxed{y_3=ca_3,}
\]

前两坐标则为

\[
\boxed{
y_1=t\,a_1\frac{B}{b_1},
\qquad
y_2=t\,a_2\frac{B}{b_2}.}
\]

定义固定前两块平方和

\[
\boxed{
S_B=
\left(a_1\frac{B}{b_1}\right)^2
+
\left(a_2\frac{B}{b_2}\right)^2.
}
\]

则

\[
\boxed{y_1^2+y_2^2=t^2S_B.}
\tag{8}
\]

所以 (4) 进一步变成

\[
\boxed{
LA(H+ca_3)=t^2S_B.
}
\tag{9}
\]

这是一条安全的整数 divisibility 接口：所有第三块增长都集中在 `L,A,t,c` 中，而 `S_B` 由前两块固定。

---

## 6. contact determinant 的另一种表达

由 `E=\tau A` 与定义

\[
E=Cq-DH
\]

得到

\[
\boxed{Cq-DH=\tau A.}
\tag{10}
\]

另一方面从 `q=b_3c`、`y_3=ca_3` 和 `H=y_3+LA`：

\[
E
=C b_3c-D(ca_3+LA).
\]

又因

\[
b_3=\delta\tau,
\qquad T=\delta L,
\]

可写为

\[
\boxed{
 c(Cb_3-Da_3)
=A(\tau+DL).
}
\tag{11}
\]

也可直接由 (1) 清分母得到同一关系。

式 (11) 把正的 cross determinant

\[
Cb_3-Da_3>0
\]

与整数 gap `A`、尾 primitive pair `(L,\tau)` 精确联系起来。

---

## 7. 对旧 A1 基线的审计结论

现在可以严格区分两类陈述：

### 可以安全保留

\[
U=LA,
\qquad
LA\mid y_1^2+y_2^2,
\]

以及由此得到的 `H,y_3` 两个半和/半差公式。

这些都由本文 (2)–(7) 独立重建。

### 不能由本框架支持

若定义

\[
\delta=\gcd(T,b_3),
\]

则因为原问题有

\[
\gcd(a_3,b_3)=1,
\]

实际上

\[
\gcd(a_3,\delta)=1.
\]

所以除 `\delta=1` 外，不能把 `a_3/\delta` 当成整数 primitive numerator。

因此 A1 后续应使用本文的 gap integer `A` 作为球面 primitive recovery，而第三分子继续保持原始整数 `a_3`。

---

## 8. 与新 A1 主线的关系

目前 A1 有两套互补但兼容的安全坐标：

1. **rational-contact 坐标** `(\rho,V)`：适合控制第三分母 prime supply、2/5 resonance 与 fixed-prefix finite；
2. **integer-gap 坐标** `(L,\tau,A)`：适合连接整数球面、二平方因子分解与 Gaussian prime-flow，同时不触碰错误的 `a_3/\delta`。

下一步若要重新使用高斯整数，只应从

\[
LA(H+y_3)=y_1^2+y_2^2
\]

出发研究 `LA` 在二平方和中的因子分配，并额外验证变换是否保持 coefficient plane；不能再以 `a_3=\delta z_3` 为入口。

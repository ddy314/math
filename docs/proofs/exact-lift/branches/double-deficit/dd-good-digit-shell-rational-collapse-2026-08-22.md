# DD full-rational Good：pure-radius digit-shell 与 pair-max contact 的 exact collapse

> **适用范围：**假想 `n/S -> 6.308883577618...` terminal frontier，且处于 full rational-contact Good main mass。默认删去总高度 `o(S)` 的 coefficient / conjugate / Bad exceptional core。
>
> **状态：**`已严格完成（no-go audit）`。
>
> 本文检查 `frontier.md` 当前首选的 primitive digit-shell 方向中最直接的一条：把 pure-radius 的完整拼接分子 contact、radius digital Gaussian carrier 与原 pair-max sphere orientation联立。结果显示该 elimination 精确退回已经存在的 rational sign factor `R_±`，因此没有新的 prime-power capacity。

## 1. terminal exact blocks

沿用 terminal normalization

\[
Q=J(s\widetilde w10^{m_2}+C_0\widetilde r)
=JUq_c\theta,
\]

故前两 denominator blocks为

\[
\boxed{b_1=Js\widetilde w,\qquad b_2=JC_0\widetilde r.}
\tag{1.1}
\]

第三 denominator为

\[
\boxed{b_3=BJVq_c\theta
=BJC_0s q_c\theta,}
\tag{1.2}
\]

其中

\[
V=C_0s.
\]

另外

\[
\boxed{10^m=2\cdot5^T B.}
\tag{1.3}
\]

full rational sign variables为

\[
A=s\theta q_c,
\qquad
b=5^T\widetilde r,
\qquad
R_+=b+A,
\qquad
R_-=b-A.
\tag{1.4}
\]

## 2. pure-radius 给出的两个 numerator readers

令

\[
\alpha=A_{12}10^{n_3}+a_3,
\qquad
Y=2\,10^dA_{12},
\qquad n_3=m+d.
\]

`frontier.md` 已证明 radius repeat 与完整拼接分子 repeat逐 main prime-depth 等价：

\[
\boxed{v_p(A_0)=v_p(\alpha).}
\tag{2.1}
\]

同一 radius subcore在 Gaussian digit coordinate中满足

\[
\Pi_{R,+}\mid a_2+iY
\]

或共轭 sign 下

\[
\Pi_{R,-}\mid a_2-iY.
\]

另一方面 `p^r|alpha` 给

\[
A_{12}10^{m+d}+a_3\equiv0\pmod{p^r}.
\]

将其与 `a_2\pm2i10^dA_{12}` 联立，消去 `A_{12}`，得到相应 Gaussian integer reader

\[
\boxed{
D_{\rm num}^{(+)}:=10^m a_2-2ia_3
}
\tag{2.2+}
\]

以及共轭 orientation 下的

\[
\boxed{
D_{\rm num}^{(-)}:=10^m a_2+2ia_3.
}
\tag{2.2-}
\]

这里符号只跟随 selected Gaussian orientation；后面的 rational denominator factor按同一 sign 配对。

## 3. 与 pair-max sphere orientation 联立

main one-channel pair-max prime满足 `(b_2,b_3)` pair-max，并有一条 selected Gaussian orientation

\[
\pi^h\mid y_2+i y_3
\]

或其共轭，其中

\[
y_2=a_2\frac q{b_2},
\qquad
y_3=a_3\frac q{b_3}.
\]

由于 main prime在 `q,b_2,b_3` 中有相同 denominator baseline，扣掉共同 baseline后，该 orientation等价于原始 digit relation

\[
\boxed{a_2b_3+i a_3b_2\equiv0\pmod{\pi^h}}
\tag{3.1}
\]

（另一 orientation取共轭）。

对同一 selected orientation，若 `(2.2+)` 与 `(3.1)` 同时成立，则把它们视为关于 `(a_2,a_3)` 的两条齐次线性关系：

\[
10^m a_2-2ia_3\equiv0,
\qquad
a_2b_3+i a_3b_2\equiv0.
\]

其 coefficient determinant 为

\[
\det
\begin{pmatrix}
10^m&-2i\\
b_3&i b_2
\end{pmatrix}
=i(10^m b_2+2b_3).
\]

因 `i` 为 Gaussian unit，selected orientation必须整除 rational reader

\[
\boxed{10^m b_2+2b_3.}
\tag{3.2+}
\]

对相反 selected orientation，同样得到

\[
\boxed{10^m b_2-2b_3.}
\tag{3.2-}
\]

所以 primitive digit-shell + pair-max elimination产生的 rational reader恰为

\[
10^m b_2\pm2b_3.
\]

## 4. denominator reader 精确退回 `R_±`

使用 `(1.1)`--`(1.4)`：

\[
\begin{aligned}
10^m b_2+2b_3
&=(2\cdot5^TB)(JC_0\widetilde r)
+2(BJC_0s q_c\theta)\\
&=2BJC_0(5^T\widetilde r+s\theta q_c)\\
&=\boxed{2BJC_0R_+.}
\end{aligned}
\tag{4.1+}
\]

同理

\[
\boxed{
10^m b_2-2b_3
=2BJC_0R_-.
}
\tag{4.1-}
\]

这就是 collapse。

full rational main prime本来已经由

\[
D_+\mid R_+,
\qquad D_-\mid R_-
\]

承担第一份 rational sign contact；`C_0` 又是 denominator common scale。于是 pure-radius digit reader与 pair-max sphere reader联立后产生的全部 prime-power divisibility，正好由已有 `C_0 R_±` 支付。

没有出现第三个 independent short integer，也没有新的 Archimedean saving。

## 5. no-double-pay 结论

因此：

\[
\boxed{
\text{pure-radius }\alpha\text{ contact}
+\text{radius digital Gaussian}
+\text{pair-max sphere orientation}
\Longrightarrow
\text{existing }C_0R_\pm\text{ reader only}.
}
\]

这条最直接的 primitive digit-shell elimination不能关闭 full rational Good。

尤其不能把 `p|alpha` 与 pair-max orientation再计成 rational sign contact之外的一份新 modulus depth。

## 6. 对当前 frontier 的含义

full rational Good 的局部 algebra进一步确认已接近闭包：

- Bad 已关闭；
- radius digital与 axis direct resultant退回 `A_0`；
- 本文的 full-concat + pair-max elimination退回 `C_0R_±`；
- ordinary first-order / second-order Gaussian resultants已有 hidden-square / product-formula no-go。

因此若继续 full rational Good，必须使用真正的 **Archimedean digit-shell location**（例如唯一 CRT lift的位置），而不能再靠同一 main prime上的局部 elimination制造新 payer。

下一主线应优先检查 rational/genuine hybrid `C_L`-period是否已经在后续账本完成；若已完成，则直接研究 unique `A_12` lift 的 decimal location。否则先完成 split-independent period，再做 location。

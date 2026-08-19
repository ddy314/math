# A1 minimal diagonal: universal deep four-factor frame

> 日期：2026-08-20。依赖 `deep-universal-factorization.md`。当前范围 `k=g>=31`。

`deep-universal-factorization.md` 已证明，对任意 deep state 存在

\[
h=qs,
\qquad q\mid Q,
\qquad s\mid b_1,
\]

以及正整数 `a,b,t`：

\[
X_1=sa,
\qquad
X_2=qb,
\qquad
ab=t,
\]

其中

\[
X_1=10\gamma T-wDN_0,
\]

\[
X_2=100\gamma T-(10w-1)DN_0.
\]

本文把 complementary divisors

\[
\bar q:=Q/q,
\qquad
\bar s:=b_1/s
\]

也接入同一组坐标，并得到第二个整数平方与两个精确乘法恒等式。

状态：**已严格完成。**

---

## 1. 两条线性关系

直接相减：

\[
X_2-10X_1=DN_0.
\]

代入 `X_1=sa,X_2=qb`：

\[
\boxed{
qb-10sa=DN_0.
}
\tag{1}

另一方面，由

\[
DTN_0-\gamma=h\lambda=qs\lambda
\]

有

\[
\begin{aligned}
X_1
&=10(DTN_0-h\lambda)T-wDN_0\\
&=DN_0(10T^2-w)-10qs\lambda T\\
&=s\left(\bar sDN_0-10q\lambda T\right).
\end{aligned}
\]

所以

\[
\boxed{a=\bar sDN_0-10q\lambda T.}
\tag{2}

同理

\[
X_2
=q\left(\bar qDN_0-100s\lambda T\right),
\]

故

\[
\boxed{b=\bar qDN_0-100s\lambda T.}
\tag{3}

由 (2)-(3)：

\[
\begin{aligned}
\bar q a-\bar s b
&=-10Q\lambda T+100b_1\lambda T\\
&=-10\lambda T,
\end{aligned}
\]

因为 `Q=10b_1+1`。因此

\[
\boxed{
\bar s b-\bar q a=10\lambda T.
}
\tag{4}

(1) 与 (4) 是 supply / complement 的完全对偶线性坐标。

---

## 2. supply-side square

由 (1) 与 `qs=h`，把 `s` 消掉：

\[
bq^2-DN_0q-10ah=0.
\]

因此判别式必须是整数平方。存在 `R>0`：

\[
\boxed{
R^2=D^2N_0^2+40abh
=D^2N_0^2+40th.
}
\tag{5}

实际上

\[
\boxed{
R=2bq-DN_0=DN_0+20as.
}
\tag{6}

---

## 3. complement-side square

由 (4) 与 `\bar q\bar s=M:=Qb_1/h`，消去 `\bar s`：

\[
a\bar q^2+10\lambda T\bar q-bM=0.
\]

故存在 `S>0`：

\[
\boxed{
S^2=100\lambda^2T^2+4abM
=100\lambda^2T^2+4tM.
}
\tag{7}

并且根公式精确给出

\[
\boxed{
S=10\lambda T+2a\bar q
=2b\bar s-10\lambda T.
}
\tag{8}

所以

\[
\boxed{
S-10\lambda T=2a\bar q,
}
\tag{9}

\[
\boxed{
S+10\lambda T=2b\bar s.
}
\tag{10}

这把 complementary Q-side / `b_1`-side divisors 全部显式化。

---

## 4. 两个 supply-free product identities

由 `X_2=qb` 与 (9)：

\[
X_2(S-10\lambda T)
=2ab\,q\bar q
=2tQ.
\]

因此

\[
\boxed{
X_2(S-10\lambda T)=2tQ.
}
\tag{11}

同理由 `X_1=sa` 与 (10)：

\[
\boxed{
X_1(S+10\lambda T)=2tb_1.
}
\tag{12}

这里 `q,s,\bar q,\bar s` 已完全消失。

于是 universal deep 可同时使用两层描述：

- prime-source frame：`X_1=sa,X_2=qb`；
- supply-free frame：(11)-(12)。

---

## 5. `S/(lambda T)` 也落在固定实区间

由 `deep-universal-factorization.md`：

\[
196000\lambda<\frac tD<15214000\lambda.
\]

由 `deep-complement-height.md`：

\[
1000<\mu:=\frac{MD}{\lambda T^2}<10001.
\]

因此

\[
\frac{tM}{\lambda^2T^2}
=\frac{t}{D\lambda}\mu
\]

严格落在

\[
196000000
<\frac{tM}{\lambda^2T^2}
<152155214000.
\]

从 (7)：

\[
\boxed{
28000<\frac S{\lambda T}<780142.
}
\tag{13}

所以 complement square 也产生一个与 `k`、single/double-deep 类型无关的固定实数窗。

这为后续在某个 prime side 出现 `\lambda T|S` 时再次引入 bounded integer 参数提供了入口。

---

## 6. 当前意义

任意 deep candidate 现在同时满足：

\[
\boxed{
\begin{aligned}
&X_1=sa,\qquad X_2=qb,\qquad ab=t,\\
&qb-10sa=DN_0,\\
&\bar s b-\bar q a=10\lambda T,\\
&R^2=D^2N_0^2+40th,\\
&S^2=100\lambda^2T^2+4tM.
\end{aligned}}
\]

并且 (11)-(12) 把 prime supply 本身消掉后仍保留两个精确 product identities。

这套 four-factor frame 将用于继续攻击 moderate LL/LH/HL 和 single-deep；尤其 high branches 中 `a,b` 的大 `2/5` 次幂已经显式已知，可以直接转成 `q,s,\bar q,\bar s` 的局部限制。
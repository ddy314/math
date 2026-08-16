# A1 split pair-max Hensel lock — 2026-08-16

本文继续 `a1-odd-prime-power-routing-classification-2026-08-16.md`，分析唯一没有被 `Q` 完整吸收的 odd prime-power 异常。

这类异常必有

\[
p\equiv1\pmod4
\]

且第三分母与恰好一个前缀分母 pair-max。本文证明：指数差 `d` 会在整数球面上产生深度 `2d` 的平方根 `-1` Hensel 锁。

本文结论均为 **已严格完成**。

---

## 1. 第一种异常：`b_1,b_3` pair-max

设

\[
\boxed{
e_1=e_3=E>e_2=e,}
\qquad
\boxed{d=E-e>0,}
\tag{1}
\]

其中

\[
e_i=v_p(b_i),
\qquad
p\equiv1\pmod4,\ p\ne5.
\]

由 odd prime-power routing classification：

\[
\boxed{v_p(Q)=e.}
\tag{2}
\]

A1 中

\[
D=10^gQ,
\]

所以

\[
\boxed{v_p(D)=e.}
\tag{3}
\]

令

\[
q=\operatorname{lcm}(b_1,b_2,b_3).
\]

则

\[
v_p(q)=E.
\]

整数球面坐标满足

\[
y_i=\frac{qa_i}{b_i}.
\]

由既约性 `\gcd(a_i,b_i)=1`：

\[
\boxed{v_p(y_1)=0,
\qquad
v_p(y_3)=0,
\qquad
v_p(y_2)=d.}
\tag{4}
\]

---

## 2. 安全 contact gap 强迫 `p^d\mid H`

安全 gap 定义

\[
\mathcal E=Cq-DH
\]

并满足

\[
\boxed{\mathcal E=\tau A.}
\tag{5}
\]

因为 `p\ne2,5`，

\[
v_p(\tau)=v_p(b_3)=E.
\]

所以

\[
p^E\mid\mathcal E.
\]

同时 `p^E\mid q`，故

\[
p^E\mid Cq.
\]

由

\[
\mathcal E=Cq-DH
\]

可得

\[
p^E\mid DH.
\]

再由 (3)：

\[
\boxed{v_p(H)\ge E-e=d.}
\tag{6}
\]

即

\[
\boxed{p^d\mid H.}
\]

---

## 3. 球面给出双倍深度的 `-1` Hensel 锁

整数球面为

\[
H^2=y_1^2+y_2^2+y_3^2.
\]

由 (4)、(6)：

\[
p^{2d}\mid H^2,
\qquad
p^{2d}\mid y_2^2.
\]

因此

\[
\boxed{
y_1^2+y_3^2
=H^2-y_2^2
\equiv0\pmod{p^{2d}}.}
\tag{7}
\]

因为 `y_1,y_3` 都是 `p`-进单位，可除以 `y_3^2`：

\[
\boxed{
\left(\frac{y_1}{y_3}\right)^2
\equiv-1\pmod{p^{2d}}.
}
\tag{8}
\]

比例可以写回原分数：

\[
\frac{y_1}{y_3}
=
\frac{a_1b_3}{a_3b_1}.
\]

将共同的 `p^E` 从 `b_1,b_3` 中约去。写

\[
b_1=p^E\beta_1,
\qquad
b_3=p^E\beta_3,
\qquad
p\nmid\beta_1\beta_3a_1a_3,
\]

则 (8) 等价于

\[
\boxed{
(a_1\beta_3)^2
+(a_3\beta_1)^2
\equiv0\pmod{p^{2d}}.
}
\tag{9}
\]

因此异常指数差 `d` 不只要求 `p\equiv1 mod 4`；它还要求由真实 numerator / denominator unit parts 在深度 `2d` 上实现指定的平方根 `-1`。

---

## 4. 第二种异常：`b_2,b_3` pair-max

现在设

\[
\boxed{e_2=e_3=E>e_1=e,}
\qquad d=E-e>0.
\tag{10}
\]

完全同理：

\[
v_p(Q)=e,
\qquad
v_p(D)=e,
\]

整数球面坐标满足

\[
\boxed{v_p(y_2)=0,
\qquad
v_p(y_3)=0,
\qquad
v_p(y_1)=d.}
\tag{11}
\]

安全 gap 再次给出

\[
\boxed{p^d\mid H.}
\tag{12}
\]

因此球面方程模 `p^{2d}` 给出

\[
\boxed{
y_2^2+y_3^2\equiv0\pmod{p^{2d}}.}
\tag{13}
\]

写

\[
b_2=p^E\beta_2,
\qquad
b_3=p^E\beta_3,
\]

则

\[
\boxed{
(a_2\beta_3)^2
+(a_3\beta_2)^2
\equiv0\pmod{p^{2d}}.
}
\tag{14}
\]

---

## 5. 异常 prime-flow 的最终局部形状

因此，第三分母中任意奇素数 `p\ne5` 的完整 `p`-幂只有两种机制：

### Q-routed

\[
\boxed{v_p(b_3)\le v_p(Q).}
\]

### split pair-max Hensel exception

\[
\boxed{p\equiv1\pmod4}
\]

并且第三块与一个前缀 denominator pair-max；若指数差为

\[
d=E-e,
\]

则必须额外满足一个深度

\[
\boxed{p^{2d}}
\]

的 `-1` Hensel congruence，分别为 (9) 或 (14)。

所以此前所谓的 split pair-max part 已经进一步缩成一个指定 Gaussian root 的高深度局部通道。后续若能从十进制拼接、numerator coprimality 或 contact square 对这个 root 给出不兼容的第二个同余，就可以直接关闭该异常。
# A2 pure-decimal discriminant resultant

> **依赖：** `source-discriminant.md`，尤其 (3.2)、(4.1)、(6.1)、(7.2)、(7.4)、(9.6)。
>
> **严格状态：**本文把 `source-discriminant.md` 中仍含 `c_u,q,g,omega,c_Q` 的 discriminant/cofactor pair 乘去一个**完整平方尺度**，得到只含原始 decimal numerator/denominator blocks 的三个整数。external double-root 因而被改写成纯 decimal resultant。本文仍**不宣称 A2 全局关闭**。

---

## 1. 平方尺度与三个纯 decimal 整数

沿用

\[
z=q5^\lambda,
\qquad
b_3z=Tc_uQ.
\tag{1.1}
\]

reflection denominator formula 给

\[
b_3=2^{M+m+1}5^dc_Qc_u,
\]
所以

\[
\boxed{
B_3:=\frac{b_3}{c_u}
=2^{M+m+1}5^dc_Q\in\mathbf Z_{>0}.
}
\tag{1.2}
\]

由 (1.1)：

\[
\boxed{B_3z=TQ.}
\tag{1.3}
\]

`source-discriminant.md` 定义

\[
A_W=5c_u^2+z^2,
\]

\[
\mathscr B_W
=c_u^2(5K^2-36K+55)+z^2K^2,
\]

\[
\mathscr D_W=55z^2-49c_u^2.
\]

现在统一乘平方 `B_3^2`。定义

\[
\boxed{
\mathscr A_{\rm dec}
:=5b_3^2+T^2Q^2,
}
\tag{1.4}
\]

\[
\boxed{
\mathscr B_{\rm dec}
:=b_3^2(5K^2-36K+55)+T^2Q^2K^2,
}
\tag{1.5}
\]

\[
\boxed{
\mathscr D_{\rm dec}
:=55T^2Q^2-49b_3^2.
}
\tag{1.6}
\]

由 `B_3c_u=b_3` 与 (1.3) 逐项得到

\[
\boxed{
\mathscr A_{\rm dec}=B_3^2A_W,
\qquad
\mathscr B_{\rm dec}=B_3^2\mathscr B_W,
\qquad
\mathscr D_{\rm dec}=B_3^2\mathscr D_W.
}
\tag{1.7}
\]

这一步非常关键：三个旧 source 对象并没有被粗略近似，而是同时乘了**同一个精确平方**。因此任意奇素数的 valuation parity、Legendre/Jacobi square class 与 common-prime 深度都可以无损转移到纯 decimal 系统。

---

## 2. `已严格完成`：三条完全 source-free 的平方恒等式

令

\[
\boxed{
\mathscr L_{\rm dec}
:=\mathscr A_{\rm dec}K-18b_3^2.
}
\tag{2.1}
\]

把 `source-discriminant.md` (7.2) 乘 `B_3^4`：

\[
B_3^4 A_W\mathscr B_W
=B_3^4L_W^2+B_3^4c_u^2\mathscr D_W.
\]

利用 (1.7) 与

\[
B_3^2L_W
=(B_3^2A_W)K-18(B_3c_u)^2
=\mathscr L_{\rm dec},
\]
得到

\[
\boxed{
\mathscr A_{\rm dec}\mathscr B_{\rm dec}
=\mathscr L_{\rm dec}^2+b_3^2\mathscr D_{\rm dec}.
}
\tag{2.2}
\]

同理，(7.3) 与 (7.4) 分别变成

\[
\boxed{
55\mathscr A_{\rm dec}-\mathscr D_{\rm dec}
=(18b_3)^2,
}
\tag{2.3}
\]

\[
\boxed{
55\mathscr B_{\rm dec}-K^2\mathscr D_{\rm dec}
=b_3^2(18K-55)^2.
}
\tag{2.4}
\]

(2.2)–(2.4) 中已经完全没有

\[
c_u,q,g,\omega,c_Q,z.
\]

它们只读取真正的 decimal data

\[
\boxed{K,P,Q,T,b_3.}
\]

因此 external double-root 从此可以在纯十进制层研究，不必再回到 source split。

---

## 3. `已严格完成`：external prime 的完整 valuation 无损转移

对 `height-cofactor.md` 的 non-`3` endpoint-external height prime，已有

\[
p\nmid10c_Qc_ugXYqf.
\tag{3.1}
\]

而

\[
B_3=2^{M+m+1}5^dc_Q.
\]

所以

\[
\boxed{p\nmid B_3.}
\tag{3.2}
\]

由 (1.7)，对所有 `h>=1` 都有精确 valuation equality

\[
\boxed{
\begin{aligned}
v_p(\mathscr A_{\rm dec})&=v_p(A_W),\\
v_p(\mathscr B_{\rm dec})&=v_p(\mathscr B_W),\\
v_p(\mathscr D_{\rm dec})&=v_p(\mathscr D_W).
\end{aligned}}
\tag{3.3}
\]

所以 `source-discriminant.md` 的 double-root parity law、等深 cancellation、simple/double root 划分全部原样传到 decimal system；这里不存在任何因为“清除分母”而丢失的 prime-power 深度。

---

## 4. `已严格完成`：double-root 已变成纯 decimal 线性 resultant

设 `p` 为 non-`3` endpoint-external common prime，且进入 discriminant-zero 子支：

\[
p\mid\mathscr D_{\rm dec},
\qquad
p\mid\mathscr B_{\rm dec}.
\tag{4.1}
\]

由 (3.3) 与 `source-discriminant.md` §8，也可直接从 (2.4) 得到：对

\[
p\notin\{3,5,11\},
\qquad p\nmid b_3,
\]
有

\[
\boxed{
 p\mid\mathscr D_{\rm dec},\ p\mid\mathscr B_{\rm dec}
\iff
 p\mid\mathscr D_{\rm dec},\ p\mid18K-55.
}
\tag{4.2}
\]

因为 `K=10P`，

\[
18K-55=180P-55=5(36P-11).
\]

而 external prime `p\ne5`，故进一步有

\[
\boxed{p\mid36P-11.}
\tag{4.3}
\]

因此 quadratic double root 已经退化为真正的一次 prefix root。

---

## 5. `已严格完成`：加入 height 后前三个 target 全部是原始 decimal blocks

若再假设

\[
p\mid W_q,
\qquad
p\mid\widehat{\mathcal T}_2,
\]
则 `source-discriminant.md` §9 已给

\[
p\mid18a_3+55T.
\tag{5.1}
\]

结合 (1.6)、(4.3)，得到完全不含 source 变量的三路必要条件：

\[
\boxed{
 p\mid
\gcd\Bigl(
36P-11,
\ 18a_3+55T,
\ 55T^2Q^2-49b_3^2
\Bigr).
}
\tag{5.2}
\]

其中

\[
P=9\cdot10^{M-1}+a_2,
\qquad
Q=2\cdot10^M+b_2,
\qquad
T=10^m.
\tag{5.3}
\]

也就是说 external double-root 的前三个条件现在只读取原问题的

\[
\boxed{
(a_2,b_2;a_3,b_3;M,m)
}
\]

本身。

第四个 natural-representative target 仍为

\[
p\mid D+18C,
\tag{5.4}
\]

它负责把 pure decimal triple (5.2) 接回 finite-defect remainder。当前还没有证明 (5.2) 与 (5.4) 全局不相容。

---

## 6. `已严格完成`：纯 decimal quadratic 的判别式正好是 `-4b_3^2 D_dec`

把 (1.5) 看成关于 `K` 的二次式：

\[
\mathscr B_{\rm dec}
=(5b_3^2+T^2Q^2)K^2
-36b_3^2K
+55b_3^2.
\]

其判别式为

\[
\begin{aligned}
\Delta_{\rm dec}
&=(36b_3^2)^2
-4(5b_3^2+T^2Q^2)(55b_3^2)\\
&=-4b_3^2(55T^2Q^2-49b_3^2).
\end{aligned}
\]

即

\[
\boxed{
\Delta_{\rm dec}
=-4b_3^2\mathscr D_{\rm dec}.
}
\tag{6.1}
\]

又因 `b_3<T` 且 `Q>1`，

\[
55T^2Q^2>55T^2>49b_3^2,
\]
所以

\[
\boxed{
\mathscr D_{\rm dec}>0,
\qquad
\Delta_{\rm dec}<0.
}
\tag{6.2}
\]

因此 `\mathscr B_dec(K)` 在实数轴上是严格正定 quadratic；所有根现象都纯粹是 `p`-adic / modular，而不是 Archimedean root leakage。

---

## 7. `已严格完成`：higher-lift parity law 也完全 decimalize

固定

\[
p\notin\{2,3,5,11\},
\qquad
p\nmid b_3K,
\]
并设

\[
b=v_p(\mathscr B_{\rm dec}),
\qquad
d=v_p(\mathscr D_{\rm dec}),
\qquad
\ell=v_p(18K-55).
\tag{7.1}
\]

由 (2.4)，若 `b\ne d`，两项赋值不同，故

\[
\boxed{
\begin{aligned}
b<d&\Longrightarrow b=2\ell,\\
d<b&\Longrightarrow d=2\ell.
\end{aligned}}
\tag{7.2}
\]

若 `b=d`，则

\[
\boxed{2\ell\ge b=d.}
\tag{7.3}
\]

所以

\[
\boxed{
\min\{b,d\}\text{ 若为奇数，必有 }b=d.
}
\tag{7.4}
\]

这正是 `source-discriminant.md` (10.4)，但现在已经不需要知道 `c_u,q,z`。external double-root 的全部 higher-lift parity 只依赖 pure decimal pair

\[
\boxed{(\mathscr B_{\rm dec},\mathscr D_{\rm dec}).}
\]

---

## 8. `已严格完成`：leading-coefficient degeneration 也被纯 decimal 排除

若某个 odd external prime 同时满足

\[
p\mid\mathscr A_{\rm dec},
\qquad
p\mid\mathscr D_{\rm dec},
\]
则由 (2.3)

\[
p\mid(18b_3)^2.
\]

而 external prime `p\nmid b_3`，所以只能 `p\mid18`。非 `3` 情形矛盾。因此

\[
\boxed{
 p\mid\mathscr D_{\rm dec},\ p\ne3,\ p\nmid b_3
\Longrightarrow
p\nmid\mathscr A_{\rm dec}.
}
\tag{8.1}
\]

于是 pure decimal quadratic 也没有“判别式与 leading coefficient 同时为零”的第三种局部型。

---

## 9. 更新后的开放核

这一层的作用不是再增加一个 character，而是完成了一次变量消元：

\[
\boxed{
(A_W,\mathscr B_W,\mathscr D_W)
\xrightarrow{\times B_3^2}
(\mathscr A_{\rm dec},\mathscr B_{\rm dec},\mathscr D_{\rm dec})
}
\]

右边完全由原始 decimal blocks 决定，且所有 external odd-prime valuations 原样保留。

因此 moving double-root 的当前规范形式可以写成

\[
\boxed{
\begin{gathered}
p\equiv3\pmod4,
\qquad p\notin\{3,5,11\},\\
p\mid36P-11,\\
p\mid18a_3+55T,\\
p\mid55T^2Q^2-49b_3^2,\\
p\mid D+18C.
\end{gathered}}
\tag{9.1}
\]

前三条是真正的原 decimal numerator/denominator 条件，最后一条是 finite-defect natural representative。

下一步最值得做的是：

1. 以 `36P-11` 为线性消元轴，把 `\mathscr D_dec` 与 prefix norm `N_0` / `Psi_f` 做 resultant；
2. 把 `18a_3+55T` 与 third-coordinate primitive condition `gcd(a_3,b_3)=1`、sphere factor equality 联立；
3. 最后才把剩余 common prime 送进 `D+18C` 与 (16.101)–(16.104) 的自然代表区间。

从这一层开始，external double-root 的主问题已经可以完全用原题的 decimal blocks 表述。
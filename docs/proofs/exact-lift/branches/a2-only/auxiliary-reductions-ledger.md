# A2-only Auxiliary Reductions Ledger

> 本文件是细粒度研究记录的机械归并账本。各来源的标题、正文和证明状态原样保留；账本中的局部闭合、有限证书或降级路线均不表示该分支或主不存在性命题已经关闭。

## 来源索引

- [`decimal-discriminant.md`](#source-decimal-discriminant)
- [`decimal-prefix-bridge.md`](#source-decimal-prefix-bridge)
- [`external-secant-center.md`](#source-external-secant-center)
- [`fixed-denominator-height-angle.md`](#source-fixed-denominator-height-angle)
- [`fixed19-secant-center.md`](#source-fixed19-secant-center)
- [`height-cofactor.md`](#source-height-cofactor)
- [`length-orbit.md`](#source-length-orbit)
- [`source-discriminant.md`](#source-source-discriminant)
- [`source-length-resultant.md`](#source-source-length-resultant)
- [`source-spontaneous-bridge.md`](#source-source-spontaneous-bridge)

<a id="source-decimal-discriminant"></a>

> 整合来源：`decimal-discriminant.md`

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

---

<a id="source-decimal-prefix-bridge"></a>

> 整合来源：`decimal-prefix-bridge.md`

# A2 decimal height square and external-prefix separation

> **依赖：** `endpoint-lattice.md`、`height-cofactor.md`、`source-discriminant.md`、`decimal-discriminant.md`。
>
> **严格状态：**本文继续处理 pure-decimal external double-root。首先恢复一个原始 denominator/numerator blocks 上的精确三平方恒等式；随后将 double-root 的三个 decimal target 与纯 prefix resultant 联立，证明 moving inert double-root prime 不可能回流到 `q`-side 的 `K^2-26`、`S_0`，也不可能进入 `f`-side 的 `Psi_f`。因此该 moving prime 被严格隔离为真正的 endpoint-external/spontaneous carrier。本文仍**不宣称 A2 全局关闭**。

---

## 1. `已严格完成`：原始 decimal blocks 满足一个精确三平方恒等式

沿用

\[
C_0=\frac{9b_2}{2},
\qquad
N_0=C_0^2+a_2^2,
\]

以及 reflection denominator ratio

\[
\frac{b_3}{b_2}=\frac{5^dc_Q}{g}.
\tag{1.1}
\]

又有

\[
N_0=5^{\nu_5}XY,
\qquad
\nu_5=\lambda-2d,
\tag{1.2}
\]

和 canonical factor product

\[
H_0^2-Y_3^2
=5^\lambda c_Q^2XY,
\qquad
Y_3=ga_3.
\tag{1.3}
\]

因此

\[
\begin{aligned}
b_3^2N_0
&=\frac{b_2^25^{2d}c_Q^2}{g^2}\,5^{\nu_5}XY\\
&=\frac{b_2^2}{g^2}\,5^\lambda c_Q^2XY\\
&=\frac{b_2^2}{g^2}(H_0^2-g^2a_3^2).
\end{aligned}
\]

移项得到精确整数平方：

\[
\boxed{
\mathscr H_{\rm dec}
:=b_3^2N_0+b_2^2a_3^2
=\left(\frac{b_2H_0}{g}\right)^2.
}
\tag{1.4}
\]

因为 `N_0=C_0^2+a_2^2`，还可写成真正的三平方球面：

\[
\boxed{
(b_3C_0)^2+(b_3a_2)^2+(b_2a_3)^2
=\left(\frac{b_2H_0}{g}\right)^2.
}
\tag{1.5}
\]

而

\[
\frac{b_2}{g}=2^{M+m+1}c_u,
\qquad
H_0=c_uW_q.
\]

所以对任意 non-`3` external height prime

\[
p^h\Vert W_q,
\]
旧本原性给 `p\nmid2c_u`，从而

\[
\boxed{
v_p(\mathscr H_{\rm dec})=2h.}
\tag{1.6}
\]

这是一个此前没有显式记录的 even-depth decimal channel：height prime 在真实三平方对象中永远以精确偶深度出现。

---

## 2. `已严格完成`：double-root 三条件产生纯 prefix norm resultant

沿用 `decimal-discriminant.md`

\[
\mathscr D_{\rm dec}
=55T^2Q^2-49b_3^2,
\tag{2.1}
\]

以及 external double-root 的线性 third target

\[
L_3:=18a_3+55T.
\tag{2.2}
\]

定义正整数

\[
\boxed{
\mathscr R_N
:=324Q^2N_0+2695b_2^2,
\qquad2695=5\cdot7^2\cdot11.
}
\tag{2.3}
\]

由 (1.4) 直接展开得到精确 Bézout 型恒等式

\[
\boxed{
\begin{aligned}
b_3^2\mathscr R_N
={}&324Q^2\mathscr H_{\rm dec}
-55b_2^2\mathscr D_{\rm dec}\\
&+b_2^2Q^2(55T-18a_3)(55T+18a_3).
\end{aligned}}
\tag{2.4}
\]

最后一个正负号因子中的

\[
55T+18a_3=L_3.
\]

因此若 `p` 是 external height double-root，记

\[
h=v_p(W_q),
\qquad
d_\Delta=v_p(\mathscr D_{\rm dec}),
\qquad
\ell_3=v_p(L_3),
\]
则 `p\nmid b_2b_3QT(55T-18a_3)`，并由 (1.6)、(2.4) 至少得到

\[
\boxed{
v_p(\mathscr R_N)
\ge\min\{2h,d_\Delta,\ell_3\}.}
\tag{2.5}
\]

若三项最小赋值唯一，则 (2.4) 还给出相同的精确赋值；只有最小层发生并列时才可能有一次 normalized cancellation。

特别地在第一层：

\[
\boxed{p\mid\mathscr R_N.}
\tag{2.6}
\]

---

## 3. `已严格完成`：`Psi_f` 在 external double-root 上是固定非零负平方类

纯 prefix resultant 为

\[
\Psi_f=b_2^2(K^2-26)-Q^2N_0.
\tag{3.1}
\]

存在精确恒等式

\[
\boxed{
324\Psi_f+2704b_2^2
=b_2^2(18K-55)(18K+55)-\mathscr R_N,
}
\tag{3.2}
\]

其中

\[
2704=52^2.
\]

external double-root 已有

\[
p\mid18K-55,
\qquad
p\mid\mathscr R_N.
\]

故模 `p`：

\[
324\Psi_f\equiv-2704b_2^2.
\]

也就是

\[
\boxed{
\Psi_f
\equiv
-\left(\frac{26b_2}{9}\right)^2
\pmod p.
}
\tag{3.3}
\]

这里 `p\equiv3 (mod 4)`，且 external prime 不整除 `3\cdot13\cdot b_2`。因此

\[
\boxed{
p\nmid\Psi_f,
\qquad
\left(\frac{\Psi_f}{p}\right)=-1.}
\tag{3.4}
\]

所以 moving double-root prime **不可能进入 `f`-side pure-prefix gcd**

\[
\gcd(f,\Psi_f),
\]
甚至 `\Psi_f` 本身在该 prime 处就是显式非零非剩余类。

---

## 4. `已严格完成`：`K^2-26` 也不可能在 external double-root 上消失

由 linear root `18K-55` 有恒等式

\[
\boxed{
324(K^2-26)+5399
=(18K-55)(18K+55).
}
\tag{4.1}
\]

因此 external double-root prime 满足

\[
\boxed{
K^2-26\equiv-\frac{5399}{324}\pmod p.}
\tag{4.2}
\]

若 `p\mid K^2-26`，则 `p\mid5399`。整数 `5399` 为素数：只需试除所有不超过 `sqrt(5399)<74` 的素数即可。因此唯一可能是

\[
p=5399.
\tag{4.3}
\]

但 `\mathscr D_{\rm dec}\equiv0 (mod p)` 且 `p\nmid Tb_3Q` 强迫

\[
\left(\frac{55}{p}\right)=1.
\tag{4.4}
\]

对 `p=5399`，注意

\[
5399\equiv4\pmod5,
\qquad
5399\equiv9\pmod{11},
\qquad
5399\equiv3\pmod4.
\]

于是二次互反律给

\[
\left(\frac5{5399}\right)
=\left(\frac4{5}\right)=1,
\]

而 `11` 与 `5399` 都为 `3 mod 4`，所以

\[
\left(\frac{11}{5399}\right)
=-\left(\frac{9}{11}\right)=-1.
\]

故

\[
\boxed{
\left(\frac{55}{5399}\right)=-1,
}
\tag{4.5}
\]

与 (4.4) 矛盾。因此

\[
\boxed{p\nmid K^2-26.}
\tag{4.6}
\]

这把 moving double-root prime 从 q-side pure-prefix polynomial 也完全分离。

---

## 5. `已严格完成`：`S_0` 在 external double-root 上也是单位

回忆

\[
\mathscr S_0
=T F_W(K)-2\omega(2K-9)W_q,
\qquad
F_W(K)=5K^2-36K+55.
\tag{5.1}
\]

另有整数恒等式

\[
\boxed{
324F_W(K)+2695
=(18K-55)(90K-373).
}
\tag{5.2}
\]

所以 double-root 线性条件给

\[
F_W(K)
\equiv-\frac{2695}{324}\pmod p.
\tag{5.3}
\]

另一方面 `\mathscr D_dec\equiv0` 强迫 `(55/p)=1`，而

\[
2695=49\cdot55.
\]

故 `2695` 在模 `p` 下为非零平方类。因为 `p\equiv3 (mod 4)`，(5.3) 是非零非剩余；特别地

\[
p\nmid F_W(K).
\]

又 `p\mid W_q`，所以 (5.1) 给

\[
\boxed{p\nmid\mathscr S_0.}
\tag{5.4}
\]

因此 external double-root 也不能伪装成 q-side additive cofactor contact。

---

## 6. `已严格完成`：moving double-root 被严格隔离为 spontaneous/external prime

汇总 §§3–5。若 non-`3` inert prime `p` 同时满足

\[
p\mid W_q,
\qquad
p\mid\widehat{\mathcal T}_2,
\qquad
p\mid\mathscr D_{\rm dec},
\]
并属于 `decimal-discriminant.md` 的 moving external double-root，则

\[
\boxed{
 p\nmid
 qf\,\Psi_f\,(K^2-26)\,\mathscr S_0.
}
\tag{6.1}
\]

前两个 denominator factors `q,f` 来自 external 定义；后三个单位性由本文严格证明。

所以该 prime 已经不能再回流到 `endpoint-lattice.md` 的两个 pure-prefix gcd

\[
\gcd(q,K^2-26),
\qquad
\gcd(f,\Psi_f),
\]
也不能通过 `\mathscr S_0` 重新解释成 q-side denominator contact。

换言之：

\[
\boxed{
\text{moving external double-root}
=\text{genuinely spontaneous prime source}.}
\tag{6.2}
\]

这完成了此前 prime-source 分类里一直缺少的一项**严格互斥性**。

---

## 7. 更新后的开放核

本轮没有排除 spontaneous prime 本身，但它的来源现在完全清楚：

1. denominator-height common odd carrier 已固定在 `7,23,43`；
2. moving external double-root 与两个 denominator-prefix gcd 严格互斥；
3. moving double-root 的 height 深度在 pure decimal square `H_dec` 中自动变成精确偶深度 `2h`；
4. moving prime 仍必须同时满足
   \[
   p\mid36P-11,
   \quad
   p\mid18a_3+55T,
   \quad
   p\mid\mathscr D_{\rm dec},
   \quad
   p\mid D+18C.
   \]

因此下一步已进一步收窄为：

- 把 genuine spontaneous double-root 与 source-excess 的 `D_src` / `L_0` 接触比较，证明二者也互斥，或把交集压成固定素数；
- 对 `D+18C` 使用自然代表 (16.101)–(16.104) 做 **higher-depth** resultant，而不是重复其模 `p` 的一阶影子；
- 利用 (1.6) 的精确 `2h` 深度，与 `B_dec,D_dec` 的等深 odd-cancellation law 建立最终 parity conservation。

此时再研究普通 Legendre character 已不会增加约束。

---

<a id="source-external-secant-center"></a>

> 整合来源：`external-secant-center.md`

# A2 universal external secant center

> **依赖：** `decimal-discriminant.md`、`decimal-prefix-bridge.md`、`length-orbit.md`、`fixed19-secant-center.md`、`endpoint-lattice.md` 的三点 rational-root sieve。
>
> **严格状态：**本文把 external discriminant-zero / common-height / prefix-norm / natural-representative 的共同 `p`-进中心代回 `J=2,3,4` 三个 secant cofactor。三个中心值完全因子化后，所有可能的 non-`3` inert secant contact 只剩固定素数 `19` 与 `47`。`19` 已由 `fixed19-secant-center.md` 单列；本文进一步审计 `47`，证明它只给三条 simple unique Hensel branch，而不是新的 singular tree。本文仍**不宣称 A2 全局关闭**。

---

## 1. 四个共同中心与 normalized secant polynomial

在 external discriminant-zero common-height 通道中，若相应 residual 至少在模 `p` 层同时消失，则有

\[
K\equiv K_*:=\frac{55}{18},
\qquad
\frac{a_3}{T}\equiv a_*:=-\frac{55}{18},
\tag{1.1}
\]

\[
\frac{Q^2N_0}{b_2^2}
\equiv R_*:=-\frac{2695}{324},
\qquad
\frac DC\equiv d_*:=-18
\pmod p.
\tag{1.2}
\]

这里第四式来自 natural-representative target `D+18C≡0`；`p∤C`，否则 `p|D` 与 `gcd(C,D)=1` 矛盾。

定义 normalized secant polynomial

\[
\phi_J(K,a,R)
:=J(J+2a)(K-J)^2-R(J+a)^2,
\tag{1.3}
\]

于是

\[
F(J)=b_2^2T^2\phi_J.
\tag{1.4}
\]

对 external prime，`p∤2·3·5·b_2T`，所以 odd-prime support 可以直接在 `phi_J` 上读取。

---

## 2. `已严格完成`：三个中心值完全因子化

在精确有理中心 `(K_*,a_*,R_*)` 上：

\[
\boxed{
\phi_2^*
=\frac{19^2\cdot31}{18^4},
}
\tag{2.1}
\]

\[
\boxed{
\phi_3^*
=-\frac{7\cdot47}{18^4},
}
\tag{2.2}
\]

\[
\boxed{
\phi_4^*
=-\frac{17^2\cdot41}{18^4}.
}
\tag{2.3}
\]

而 `d_*=-18` 给

\[
D-C=-19C,
\qquad
D+C=-17C.
\tag{2.4}
\]

三 cofactor

\[
\Xi_-=-\frac{F(2)}{U_0(D-C)},
\qquad
\Xi_C=\frac{F(3)}{U_0C},
\qquad
\Xi_+=\frac{F(4)}{U_0(D+C)},
\tag{2.5}
\]
其中 `U_0=2^{2M+2}5^{nu_5}`。定义共同 `p`-进单位尺度

\[
\mathcal K_{sec}
:=\frac{b_2^2T^2}{U_0C\,18^4}.
\tag{2.6}
\]

则在中心处精确得到

\[
\boxed{
(\Xi_-^*,\Xi_C^*,\Xi_+^*)
=\mathcal K_{sec}
\bigl(19\cdot31,\,-7\cdot47,\,17\cdot41\bigr).
}
\tag{2.7}
\]

这三个看似复杂的巨大 cofactor 在共同 local center 上只剩六个固定小素数。

---

## 3. 两个 gap 的中心甚至只剩 `17` 与 `19`

由

\[
\Delta_-=(\Xi_C-\Xi_-)/L,
\qquad
\Delta_+=(\Xi_+-\Xi_C)/L,
\qquad L=2^m5^d,
\tag{3.1}
\]
直接相减：

\[
-7\cdot47-19\cdot31
=-918=-54\cdot17,
\tag{3.2}
\]

\[
17\cdot41+7\cdot47
=1026=54\cdot19.
\tag{3.3}
\]

所以

\[
\boxed{
(\Delta_-^*,\Delta_+^*)
=\frac{54\mathcal K_{sec}}L(-17,19).
}
\tag{3.4}
\]

并且 additive cofactor 的中心 cancellation 完全显式：

\[
(D+C)\Delta_+^*+(D-C)\Delta_-^*
\]

\[
=(-17C)(54\cdot19\mathcal K_{sec}/L)
+(-19C)(-54\cdot17\mathcal K_{sec}/L)
=0.
\tag{3.5}
\]

这解释了为什么 pure local deep lifting 能让 `widehat(T)_2` 趋向任意高 `p`-进深度：secant center 本身就是 additive cofactor 的精确 `p`-进零中心。

---

## 4. `已严格完成`：character 过滤后只剩固定 `19` 与 `47`

external discriminant-zero prime 必须满足

\[
\boxed{\left(\frac{55}{p}\right)=1.}
\tag{4.1}
\]

同时我们只关心

\[
p\equiv3\pmod4,
\qquad p\ne3.
\tag{4.2}
\]

逐个检查 (2.7)：

- `31≡3 (mod4)`，但 `(55/31)=-1`，排除；
- `7≡3 (mod4)`，但 `(55/7)=-1`，排除；
- `17,41≡1 (mod4)`，不是 inert carrier；
- `19≡3 (mod4)` 且 `(55/19)=1`；
- `47≡3 (mod4)` 且 `(55/47)=1`。

因此在共同 secant center 上：

\[
\boxed{
\begin{array}{c|c}
\text{object}&\text{possible non-3 inert discriminant-zero prime}\\ \hline
\Xi_-&19\\
\Xi_C&47\\
\Xi_+&\varnothing\\
\Delta_-&\varnothing\\
\Delta_+&19
\end{array}}
\tag{4.3}
\]

所以全部 fixed inert secant contact 被压成

\[
\boxed{\{19,47\}.}
\tag{4.4}
\]

`19` 是 endpoint-factor resonance，已由 `fixed19-secant-center.md` 处理；`47` 是**中心 cofactor cancellation**，不是 `K=J` 型端点共振。

---

# 第二部分：固定 `47` 的 fully coupled spontaneous branch

## 5. `47` 在原三方程中确实存在 genuine 解

沿用 `length-orbit.md` 的三方程：

\[
\mathcal N_{sp}(s,x)=0,
\qquad
\mathcal O_{sp}(s,x,r_s)=0,
\qquad
\mathcal G_{sp}(x,r_s)=0.
\tag{5.1}
\]

直接在 `F_47` 枚举并代回 genuine 分离条件

\[
x(x+2)y\ne0,
\qquad
r_s(x+2)+2x\ne0,
\qquad
\Phi_s(x,r_s)\ne0,
\tag{5.2}
\]
只剩三组：

\[
\boxed{
(s,x,y,r_s)
=(6,1,32,39),
(11,34,39,40),
(46,15,27,35)
\pmod{47}.}
\tag{5.3}
\]

三组的 `(f-line, source-line)` residue 分别为

\[
(25,33),\qquad(4,35),\qquad(14,7),
\tag{5.4}
\]
全部为单位。

相应 normalized base norm、source contact、prefix defect 也全部为单位：

\[
\begin{array}{c|ccc}
(s,x,y)&N_0/10^{2M-2}&D_{src}/10^{2M-2}&\Delta_0\\ \hline
(6,1,32)&41&45&2\\
(11,34,39)&35&43&4\\
(46,15,27)&31&46&14
\end{array}
\pmod{47}.
\tag{5.5}

所以这三组都是真正的 spontaneous/external 第一层解，不是 denominator 或 source boundary。

---

## 6. `已严格完成`：三组 `47` 解全部 nonsingular

对

\[
(\mathcal N_{sp},\mathcal O_{sp},\mathcal G_{sp})
\]
关于 `(s,x,r_s)` 的 Jacobian determinant，三点分别为

\[
\boxed{21,\qquad35,\qquad35\pmod{47}.}
\tag{6.1}
\]

全部非零。因此：

\[
\boxed{p=47\text{ 不产生 singular Hensel tree；只有三条唯一 simple lift。}}
\tag{6.2}
\]

这也解释了为什么 `spontaneous-bad-primes.md` 的 singular-prime 审计没有把 `47` 列为 bad prime：它的特殊性来自 secant center，而不是 octic repeated root。

---

## 7. 三条 `47` branch 都落在真实 decimal orbit

模 `47`：

\[
\operatorname{ord}_{47}(10)=46,
\]
所以 `10` 是 primitive root。解

\[
s=36\cdot10^{M-1}
\]
得到：

\[
\boxed{
\begin{array}{c|c|c}
s&M-1\pmod{46}&M\pmod{46}\\ \hline
6&44&45\\
11&23&24\\
46&19&20
\end{array}}
\tag{7.1}

并且

\[
\boxed{
10^{46}\equiv1+43\cdot47\pmod{47^2},
}
\tag{7.2}
\]
其中 `43` 为单位。因此

\[
\boxed{
\operatorname{ord}_{47^k}(10)=46\cdot47^{k-1}
\qquad(k\ge1).
}
\tag{7.3}

结合 §6，每个第一层解都对应唯一的 `47`-进 decimal exponent branch。和 fixed `19` 一样，继续机械升 `47^k` 只会固定更细的 `M` 同余类，并不会制造局部空性。

---

## 8. `47` 的 secant allocation

在共同 center 上 (2.7)：

\[
\Xi_-^*=589\mathcal K_{sec},
\qquad
\Xi_C^*=-329\mathcal K_{sec}=-7\cdot47\mathcal K_{sec},
\qquad
\Xi_+^*=697\mathcal K_{sec}.
\tag{8.1}

因此若四个 center residual 进一步都进入模 `47^2`，扰动为 `O(47^2)`，而中心 `Xi_C` 恰含一层 `47`；故

\[
\boxed{v_{47}(\Xi_C)=1,}
\tag{8.2}
\]

同时

\[
\boxed{47\nmid\Xi_-\Xi_+\Delta_-\Delta_+.}
\tag{8.3}

事实上模 `47`，去掉共同单位尺度：

\[
\Xi_-\equiv25,
\qquad
\Xi_C\equiv0,
\qquad
\Xi_+\equiv39,
\tag{8.4}

所以

\[
L\Delta_-\equiv-25,
\qquad
L\Delta_+\equiv39
\pmod{47}.
\tag{8.5}

而

\[
(D+C)/C\equiv-17,
\qquad
(D-C)/C\equiv-19,
\]
给

\[
(-17)\cdot39+(-19)\cdot(-25)
=-188=-4\cdot47.
\tag{8.6}

于是 additive cofactor 的第一层仍由两个 unit gap 的**加法 cancellation**产生，而不是某个 gap 自己携带 `47`。

若四个 center residual 都进入 `47^2`，由于 exact center 上 (3.5) 为零，整个 analytic expression 对二阶 perturbation 仍给

\[
\boxed{47^2\mid\mathcal T_2,}
\tag{8.7}

从而标准 `2,5` 归一化后

\[
\boxed{v_{47}(\widehat{\mathcal T}_2)\ge2.}
\tag{8.8}

与 `19` 相比，局部 allocation 完全不同：

\[
\boxed{
\begin{array}{c|cc}
&19&47\\ \hline
\text{secant cofactor carrying one layer}&\Xi_-&\Xi_C\\
\text{gap carrying one layer}&\Delta_+&\text{none}\\
\text{deep additive cofactor}&\ge2&\ge2
\end{array}}
\tag{8.9}

---

## 9. 更新后的 external/secant 开放核

这一层完成了固定 secant-prime 分类：

\[
\boxed{
\text{deep external discriminant-zero secant contact}
\Longrightarrow p\in\{19,47\}
}
\]
对 non-`3` inert prime 而言成立于共同 center 支持上。

- `19`：唯一 endpoint resonance，右 gap 精确一层；
- `47`：唯一 center-cofactor cancellation，三条 genuine simple local branches；
- 其余 genuine moving simple prime 不会从三点 secant center 获得固定 inert factor。

这仍未关闭 moving simple spontaneous carrier。下一步应把 generic `p\notin\{19,47\}` 从 secant 系统剥离后，直接研究 `Omega_sp` 与 `Theta_dec` 的共同 prime support；固定 `19/47` 则应使用真实 defect window `(H,e,h,C)`，而不是继续局部升模。

---

<a id="source-fixed-denominator-height-angle"></a>

> 整合来源：`fixed-denominator-height-angle.md`

# A2 fixed denominator–height–angle shallow templates `7,23,43`

> **依赖：** `height-cofactor.md`、`spontaneous-denominator-common.md`、`spontaneous-denominator-depth-matrix.md`。
>
> **严格状态：**`height-cofactor.md` 已证明：若 non-`3` inert prime 同时进入 saturated denominator、height `W_q` 与 additive cofactor `widehat(T)_2`，则 q-side 只能是 `23`，f-side只能是 `7,43`，且三对象共同深度最多一层。本文继续加入 spontaneous angle/common contact，完整枚举这三个 fixed primes 的 genuine first-layer decimal states。结论是恰有 5 个 genuine templates，全部 Jacobian nonsingular，且全部与真实 decimal orbit `tau=10^{-M}` 兼容。因此这些 primes 不能靠 first-layer/decimal枚举排除；它们应作为固定浅层 parity correction处理，而不是继续做机械三重 `p^k` lifting。本文不宣称 A2 closure。

---

## 1. height + saturation 固定共同 `K` center

若 prime同时满足 height

\[
p\mid W_q,
\]
则

\[
TK+a_3\equiv0\pmod p.
\tag{1.1}
\]

saturated denominator odd excess给

\[
2a_3+9T\equiv0\pmod p.
\tag{1.2}
\]

相消得到

\[
\boxed{2K-9\equiv0\pmod p,}
\qquad
\boxed{K\equiv9/2\pmod p.}
\tag{1.3}
\]

`height-cofactor.md` 随后用 `F_W/G_W` 的整数 Bézout identity证明：

\[
\boxed{q\text{-side}:p=23,}
\tag{1.4q}
\]

\[
\boxed{f\text{-side}:p\in\{7,43\},}
\tag{1.4f}
\]

并且三对象共享深度

\[
\min(v_p(\text{den}),v_p(W_q),v_p(\widehat T_2))=1.
\tag{1.5}
\]

本文只审计再加入 angle common 后的 first-layer状态。

---

# q-side: `p=23`

## 2. q-line 与 angle/common 方程

q denominator line给

\[
\boxed{x=-2.}
\tag{2.1}
\]

angle contact给

\[
\boxed{\Delta_0=2025x^2-18y-y^2=0.}
\tag{2.2}
\]

令

\[
s:=9+y,
\qquad
\tau:=10^{-M}.
\]

因为

\[
K=10^M(9+y)=s/\tau,
\]
center (1.3) 等价于

\[
\boxed{2s-9\tau=0.}
\tag{2.3}
\]

在 `x=-2`：

\[
\Delta_0=8181-s^2.
\]
所以 q-side fixed common system就是

\[
\boxed{s^2=8181,\qquad2s=9\tau\pmod{23}.}
\tag{2.4}
\]

模 `23`：

\[
8181\equiv16,
\]
因此

\[
s=4\quad\text{or}\quad19=-4.
\]

得到恰好两个 states：

\[
\boxed{(y,\tau)=(18,6),\qquad(10,17)\pmod{23}.}
\tag{2.5}
\]

---

## 3. 两个 q-states 都是 simple

取方程

\[
F_q:=2(y+9)-9\tau,
\qquad
G_q:=8100-18y-y^2.
\]

Jacobian determinant关于 `(y,tau)` 为

\[
\det\frac{\partial(F_q,G_q)}{\partial(y,\tau)}
=-18(y+9).
\tag{3.1}
\]

在两个 states上分别为 nonzero residues，因此

\[
\boxed{p=23\text{ 的两个 q-angle templates均 nonsingular}.}
\tag{3.2}
\]

---

## 4. 两个 q-states 都属于真实 decimal orbit

精确计算

\[
\boxed{\operatorname{ord}_{23}(10)=22.}
\tag{4.1}
\]

即 `10` 是 `F_23^×` 的生成元。因此所有 nonzero `tau` 都属于 decimal subgroup。

离散指数为

\[
10^{-16}\equiv6\pmod{23},
\qquad
10^{-5}\equiv17\pmod{23}.
\]
所以

\[
\boxed{
\begin{aligned}
(y,\tau)=(18,6)&\Longrightarrow M\equiv16\pmod{22},\\
(y,\tau)=(10,17)&\Longrightarrow M\equiv5\pmod{22}.
\end{aligned}}
\tag{4.2}
\]

first-layer decimal orbit不排除 `23`。

---

# f-side: `p=7,43`

## 5. f common 的三方程系统

f-line + saturation + exact sphere在 `spontaneous-denominator-common.md` 已降成

\[
\Delta_0=0,
\tag{5.1}
\]

\[
\mathcal L_f^{\rm sat}
:=200x^2(s-9\tau)-y(x+2)^2=0.
\tag{5.2}
\]

height+saturation center仍是

\[
\boxed{2s-9\tau=0.}
\tag{5.3}
\]

在该 center，additive f-quadratic

\[
P_f(K)=3K^2-36K+26
\]
取值

\[
P_f(9/2)=-301/4=-7\cdot43/4,
\]
正好解释 fixed primes `7,43`。

所以 f-side只需在 `F_p` 中解

\[
\boxed{
2(y+9)-9\tau=0,
\quad
2025x^2-18y-y^2=0,
\quad
200x^2(y+9-9\tau)-y(x+2)^2=0.}
\tag{5.4}
\]

---

## 6. `p=7`：唯一 genuine state

完整枚举 `F_7^3` 得两点：

\[
(x,y,\tau)=(4,6,1),\qquad(0,0,2).
\]

第二点具有 `x=y=0`，属于已排除 boundary。故 genuine state唯一：

\[
\boxed{p=7:\quad(x,y,\tau)=(4,6,1).}
\tag{6.1}
\]

对 (5.4) 三方程关于 `(x,y,tau)` 的 Jacobian determinant，在该点为

\[
\boxed{4\pmod7,}
\tag{6.2}
\]
所以它是 simple state。

又

\[
\boxed{\operatorname{ord}_7(10)=6,}
\]
且 `tau=1`，因此

\[
\boxed{M\equiv0\pmod6.}
\tag{6.3}

所以 first-layer decimal orbit也不排除 `7`。

---

## 7. `p=43`：恰有两个 genuine states

完整枚举 `F_43^3` 得

\[
(0,0,2),
\qquad
(5,37,15),
\qquad
(18,33,38).
\]

第一点同样是 `x=y=0` boundary。故 genuine states为

\[
\boxed{
(5,37,15),\qquad(18,33,38)\pmod{43}.}
\tag{7.1}

三方程 Jacobian determinants分别为

\[
\boxed{4,\qquad3\pmod{43},}
\tag{7.2}
\]
均为 units。

decimal subgroup：

\[
\boxed{\operatorname{ord}_{43}(10)=21.}
\tag{7.3}
\]

两个 `tau` 都属于该 index-2 subgroup：

\[
10^{-10}\equiv15\pmod{43},
\qquad
10^{-8}\equiv38\pmod{43}.
\]
因此

\[
\boxed{
\begin{aligned}
(5,37,15)&\Longrightarrow M\equiv10\pmod{21},\\
(18,33,38)&\Longrightarrow M\equiv8\pmod{21}.
\end{aligned}}
\tag{7.4}

first-layer decimal orbit不排除 `43`。

---

## 8. fixed shallow template table

综合 q/f 两侧：

\[
\boxed{
\begin{array}{c|c|c}
p&\text{genuine angle/common state}&M\text{ class}\\ \hline
23&(x,y,\tau)=(-2,18,6)&16\pmod{22}\\
23&(x,y,\tau)=(-2,10,17)&5\pmod{22}\\
7&(4,6,1)&0\pmod6\\
43&(5,37,15)&10\pmod{21}\\
43&(18,33,38)&8\pmod{21}
\end{array}}
\tag{8.1}
\]

五个 states均 nonsingular且 decimal-compatible。

---

## 9. `审计 / no-go`：不要继续做机械三重 `p^k` lifting

这里必须结合 `height-cofactor.md` 的深度结论：

\[
\boxed{
\min(v_p(\text{den}),v_p(W_q),v_p(\widehat T_2))=1
\quad(p=7,23,43).}
\tag{9.1}
\]

所以不存在“denominator + height + additive cofactor 三对象一起继续到 `p^2,p^3,...`”的无界树。至少一个对象在第一层后立即停止。

因此本文的 5 个 simple templates不应被机械地向同一三重系统做 `p^k` lift；那会研究一个旧定理已经证明不存在的对象。

它们真正的作用是 global parity ledger中的固定浅层 correction：

- 每个 fixed prime都为 `3 mod4`；
- 若实际 endpoint命中某个 template，它最多贡献一层三对象共同 support；
- 之后只能研究哪一对象继续加深，以及它与 angle/common gcd 的 residual allocation。

---

## 10. 更新后的 fixed-prime frontier

本文没有关闭 `7,23,43`，反而严格证明它们的 first-layer templates是真实的 modular possibilities。因此后续不能声称 fixed denominator-height pool为空。

正确状态是：

\[
\boxed{
\{7,23,43\}\text{ 是有限、nonsingular、decimal-compatible 的 shallow correction pool}.}
\tag{10.1}
\]

如果要把它们从最终 `G_sp` parity中删除，必须利用 shared depth停止后的 **asymmetric higher-depth allocation** 或真实 natural representative；first-layer Legendre、decimal subgroup、singularity audit均已无新增排除力。

---

<a id="source-fixed19-secant-center"></a>

> 整合来源：`fixed19-secant-center.md`

# A2 fixed-19 secant center and exact gap depth

> **依赖：** `length-orbit.md`、`decimal-prefix-bridge.md`、`endpoint-lattice.md` §§16.29–16.38。
>
> **严格状态：**本文只处理 fully coupled spontaneous/external 通道中剩余的 genuine fixed `p=19` 分支。主要结论是：`19` 是唯一能让 external double-root 与三点 rational-root sieve 的采样点 `J=2,3,4` 发生 inert 端点共振的素数；在二阶 common-height / double-root / prefix-norm 深度下，三 secant cofactor 的 `19`-进中心可以精确求出，并进一步得到 `v_19(Delta_+)=1` 与 `19^2 | T_2`。本文仍**不宣称 A2 全局关闭**。

---

## 1. `19` 是唯一的 inert secant endpoint resonance

external discriminant-zero double-root 已经严格给出

\[
18K-55\equiv0\pmod p.
\tag{1.1}
\]

三点 rational-root sieve 只采样

\[
J=2,3,4.
\]

若 double-root 在模 `p` 下恰撞上某个采样点，即 `K≡J (mod p)`，则

\[
p\mid 55-18J.
\]

逐点只有

\[
\begin{array}{c|c}
J&55-18J\\ \hline
2&19\\
3&1\\
4&-17.
\end{array}
\]

因此对 inert prime `p≡3 (mod 4)`：

\[
\boxed{
K\equiv J\in\{2,3,4\}\pmod p
\Longrightarrow p=19,\ J=2.
}
\tag{1.2}
\]

`p=17` 只会撞 `J=4`，但 `17≡1 (mod 4)`，不属于 odd inert carrier。

height linear target 同时给

\[
18a_3+55T\equiv0\pmod p,
\]
所以

\[
\frac{a_3}{T}\equiv-\frac{55}{18}\pmod p.
\tag{1.3}
\]

于是第二项的 secant factor `JT+a_3` 发生零点时仍要求

\[
p\mid18J-55,
\]
得到同一个列表 `(19, none, 17)`。

第一项还有 `JT+2a_3`。在 (1.3) 下其零点要求

\[
p\mid 9J-55.
\]
对 `J=2,3,4` 分别只可能给 `37,7,19`。其中 `37≡1 (mod4)`；而 `p=7` 不可能进入 discriminant-zero external channel，因为

\[
\left(\frac{55}{7}\right)
=\left(\frac{-1}{7}\right)=-1,
\]
但 external discriminant-zero 必须满足 `(55/p)=1`。因此连第一项的 forced secant degeneration 也只剩

\[
\boxed{p=19,\quad J=2.}
\tag{1.4}
\]

所以 `19` 的特殊性不是有限枚举事故：它是**唯一的 genuine inert secant resonance**。

---

## 2. genuine `19` branch 的纯 decimal fingerprint

`length-orbit.md` 已审计：模 `19` 的两组 eliminant 解中，只有

\[
\boxed{(s,x,y,r_s)=(2,11,6,9)}
\tag{2.1}
\]
是 genuine external/spontaneous；另一组落回 `19|f` 的 denominator boundary。

同时

\[
M\equiv10\pmod{18}.
\tag{2.2}
\]

endpoint defect 记号为

\[
b_2=10^{M-1}+2^{M-1}H,
\qquad
a_2=10^{M-1}-e.
\]

因此

\[
10x-1=\frac{H}{5^{M-1}},
\qquad
1-y=\frac{e}{10^{M-1}}.
\tag{2.3}
\]

由 `ord_19(10)=18`、`10^9≡-1 (mod19)`、`5^9≡1 (mod19)`，(2.1)–(2.3) 给

\[
\boxed{H\equiv14,\qquad e\equiv5\pmod{19}.}
\tag{2.4}
\]

还可恢复完整 prefix residue：

\[
\boxed{
\begin{aligned}
b_2&\equiv4,\\
a_2&\equiv13,\\
C_0=9b_2/2&\equiv-1,\\
N_0=C_0^2+a_2^2&\equiv-1,\\
Q=2\cdot10^M+b_2&\equiv3
\end{aligned}
\pmod{19}.}
\tag{2.5}
\]

归一化 prefix defect / source contact 也都是单位：

\[
\Delta_0=2025x^2-18y-y^2\equiv9\pmod{19},
\tag{2.6}
\]

\[
2025x^2-9y\equiv4\pmod{19}.
\tag{2.7}
\]

所以 genuine `19` branch 在第一层确实与 denominator-prefix、source-contact 分离；它不是旧两类 contact 的伪装。

---

## 3. 二阶 deep branch 的四个 `19`-进中心

从此假设四个 residual 都至少进入第二层：

\[
19^2\mid18K-55,
\tag{3.1}
\]

\[
19^2\mid18a_3+55T,
\tag{3.2}
\]

\[
19^2\mid\mathscr R_N,
\qquad
\mathscr R_N:=324Q^2N_0+2695b_2^2,
\tag{3.3}
\]

\[
19^2\mid D+18C.
\tag{3.4}
\]

这里 `19` 与 `18,324,T,b_2,C` 都互素。定义 dimensionless variables

\[
a:=\frac{a_3}{T},
\qquad
R:=\frac{Q^2N_0}{b_2^2},
\qquad
d_C:=\frac DC.
\]

则 (3.1)–(3.4) 精确给出模 `19^2` 的四个中心：

\[
\boxed{
K\equiv\frac{55}{18},
\qquad
a\equiv-\frac{55}{18},
\qquad
R\equiv-\frac{2695}{324},
\qquad
d_C\equiv-18
\pmod{19^2}.}
\tag{3.5}
\]

在标准代表模 `361` 下即

\[
\boxed{K\equiv344,\quad a\equiv17,\quad R\equiv307,\quad d_C\equiv343.}
\tag{3.6}
\]

注意这只是 `19`-进中心；其中 `R_*=-2695/324<0` 与真实正实数 `R` 不矛盾。它的用途是控制局部 secant cofactor，而不是提供 Archimedean 候选。

---

## 4. 三个 secant 值在中心处可以完全求出

把三点 polynomial 除去公共 `b_2^2T^2`，定义

\[
\phi_J(K,a,R)
:=J(J+2a)(K-J)^2-R(J+a)^2,
\tag{4.1}
\]

于是

\[
F(J)=b_2^2T^2\phi_J.
\tag{4.2}
\]

在精确有理中心

\[
K_*=\frac{55}{18},
\qquad
a_*=-\frac{55}{18},
\qquad R_*=-\frac{2695}{324},
\tag{4.3}
\]
直接得到

\[
\boxed{
\phi_2^*
=\frac{19^2\cdot31}{18^4},
}
\tag{4.4}
\]

\[
\boxed{
\phi_3^*
=-\frac{7\cdot47}{18^4},
}
\tag{4.5}
\]

\[
\boxed{
\phi_4^*
=-\frac{17^2\cdot41}{18^4}.
}
\tag{4.6}
\]

这立即解释了 `length-orbit.md` 的现象：左点 `J=2` 自带**恰两层** `19`，而中心点和右点都是 `19`-进单位。

更重要的是，这些中心值对 (3.1)–(3.3) 的二阶扰动稳定到所需精度：`phi_3,phi_4` 模 `19^2` 只读取中心值；`phi_2/19^2` 模 `19` 也只读取中心值。因此后面的 cofactor ratio 不是一次偶然代值，而是整个二阶 deep residue class 的固定局部型。

---

## 5. 三 cofactor 的中心 ratio

记公共 `2,5` 归一化因子

\[
U_0:=2^{2M+2}5^{\nu_5}.
\]

endpoint-lattice 给

\[
\Xi_-=-\frac{F(2)}{U_0(D-C)},
\qquad
\Xi_C=\frac{F(3)}{U_0C},
\qquad
\Xi_+=\frac{F(4)}{U_0(D+C)}.
\tag{5.1}
\]

在中心 `d_C=-18` 下：

\[
\frac{C}{D-C}=-\frac1{19},
\qquad
\frac{C}{D+C}=-\frac1{17}.
\tag{5.2}
\]

代入 (4.4)–(4.6)：

\[
\boxed{
\left(\frac{\Xi_-}{\Xi_C}\right)_*
=-\frac{19\cdot31}{7\cdot47},
}
\tag{5.3}
\]

\[
\boxed{
\left(\frac{\Xi_+}{\Xi_C}\right)_*
=-\frac{17\cdot41}{7\cdot47}.
}
\tag{5.4}
\]

而

\[
-\frac{17\cdot41}{7\cdot47}-1
=-\frac{54\cdot19}{7\cdot47}.
\tag{5.5}
\]

所以第二个 ratio 与 `1` 的距离**恰含一层 `19`**。

将 (5.3)–(5.4) 化到模 `19^2=361`：

\[
\boxed{
\frac{\Xi_-}{\Xi_C}\equiv323=19\cdot17\pmod{361},
}
\tag{5.6}
\]

\[
\boxed{
\frac{\Xi_+}{\Xi_C}\equiv191=1+19\cdot10\pmod{361}.
}
\tag{5.7}

由于 `Xi_C` 是 `19`-进单位，这重新得到并加强旧结论：

\[
\boxed{v_{19}(\Xi_-)=1,\qquad19\nmid\Xi_C\Xi_+.}
\tag{5.8}
\]

---

## 6. `已严格完成`：右 gap 恰好只有一层 `19`

令

\[
L:=2^m5^d,
\]

\[
\Delta_-:=\frac{\Xi_C-\Xi_-}{L},
\qquad
\Delta_+:=\frac{\Xi_+-\Xi_C}{L}.
\tag{6.1}
\]

`19∤LXi_C`。由 (5.6)–(5.7)：

\[
\frac{L\Delta_-}{\Xi_C}
\equiv1-323
\equiv39
=1+2\cdot19
\pmod{361},
\tag{6.2}
\]

\[
\frac{L\Delta_+}{\Xi_C}
\equiv191-1
\equiv190
=10\cdot19
\pmod{361}.
\tag{6.3}
\]

因此：

\[
\boxed{
v_{19}(\Delta_-)=0,
\qquad
v_{19}(\Delta_+)=1.}
\tag{6.4}
\]

特别地，`length-orbit.md` 原先只有

\[
19\mid\Delta_+,
\]
现在已加强成精确深度：

\[
\boxed{19\Vert\Delta_+.}
\tag{6.5}
\]

并且 normalized right-gap slope 固定为

\[
\boxed{
\frac{\Delta_+}{19}
\equiv10\,\Xi_C L^{-1}\pmod{19}.}
\tag{6.6}
\]

这个结论对所有满足 (3.1)–(3.4) 的更深 lift 都保持不变：继续升到 `19^3,19^4,...` 不会让 `Delta_+` 再获得第二层 `19`。

---

## 7. `已严格完成`：additive cofactor 自动获得第二层 `19`

endpoint-lattice 的 additive curvature 恒等式为

\[
\mathcal T_2
=(D+C)\Delta_+ +(D-C)\Delta_-.
\tag{7.1}
\]

由 (3.5)，模 `361`：

\[
\frac{D+C}{C}\equiv-17,
\qquad
\frac{D-C}{C}\equiv-19.
\tag{7.2}
\]

再用 (6.2)–(6.3)：

\[
\frac{L\mathcal T_2}{C\Xi_C}
\equiv
(-17)(190)+(-19)(39)
=-3971
=-11\cdot361
\equiv0
\pmod{361}.
\]

所以

\[
\boxed{19^2\mid\mathcal T_2.}
\tag{7.3}
\]

所有从 `T_2` 到 `\widetilde T_2`、`\widehat T_2` 的标准 `2,5` 归一化因子都是 `19`-进单位，因此同样有

\[
\boxed{v_{19}(\widehat{\mathcal T}_2)\ge2.}
\tag{7.4}
\]

这不是新的 closure：若 `19` 真要承担 odd inert excess，它仍可能从深度 `3,5,...` 开始。严格新增的信息是：**deep fixed-19 branch 绝不允许 additive cofactor 只含一层 `19`**，而右 secant gap 却永远只含一层。

---

## 8. 为什么继续纯 `19`-进加深不会自动关闭

四个中心若在 `Z_19` 中取精确值

\[
K_*=55/18,
\quad a_*=-55/18,
\quad R_*=-2695/324,
\quad D/C=-18,
\]
则 (5.3)–(5.4) 是精确 `19`-进 ratio，而 (7.1) 的两项正好完全抵消。

等价地，定义

\[
J_*(K,a,R)
:=K^2-(18+4a)K+18a+55-R.
\]
在中心恰有

\[
\boxed{J_*(K_*,a_*,R_*)=0.}
\tag{8.1}
\]

而 `Theta_dec` / `widehat(T)_2` 正是这个 dimensionless cofactor kernel 乘 `19`-进单位尺度。因此 deep local system 本身有一个真正的 `19`-进零中心；不断机械提升局部 congruence 只会趋近这个中心，不会凭空产生矛盾。

所以 fixed `19` 后续必须加入**非局部输入**：例如 `C/D` 的真实小自然代表、`H,e,h` 的 Archimedean defect window，或与 `D±C` 之外的独立 integer divisor system 联立。不能把 (6.5) 再机械提升成“希望有一天 `19^k` 自己消失”。

---

## 9. 更新后的 fixed-19 开放核

对于 genuine fixed `19` spontaneous/external branch：

1. `19` 是唯一可能与 `J=2,3,4` 发生 inert secant endpoint resonance 的 double-root prime；
2. 第一层 decimal fingerprint 固定为
   \[
   M\equiv10\ (18),\ H\equiv14,\ e\equiv5\ (19);
   \]
3. 一旦 common-height / double-root / prefix-norm / natural-representative 都进入第二层，三 gap 精确满足
   \[
   v_{19}(\Delta_-)=0,
   \qquad v_{19}(\Delta_+)=1;
   \]
4. 同时 additive cofactor 至少含两层 `19`：
   \[
   v_{19}(\widehat{\mathcal T}_2)\ge2.
   \]

下一步真正值得打的是把 (2.4) 的真实小十进制缺口 `H,e` 与 (6.6) 的固定 right-gap slope、以及 `C/D<3/250` 放在同一个 integer representative 中，而不是继续做纯局部 Hensel 枚举。

---

<a id="source-height-cofactor"></a>

> 整合来源：`height-cofactor.md`

# A2 height–cofactor bridge

> **依赖：** `endpoint-lattice.md` §§16.44–16.73、`prime-source.md`、`primitive-reduction.md`。
>
> **严格状态：**本文把 reduced numerator `W_q` 与本原 odd cofactor `\widehat{\mathcal T}_2` 直接接成逐 prime-power 的 gcd/valuation bridge，并将 denominator-saturation 与 height 的共同惰性素数压到三个固定素数：q-side 只剩 `23`，f-side 只剩 `7,43`。共同深度在三对象交集中至多一层。本文仍**不宣称 A2 全局关闭**。

---

## 1. 统一记号

沿用当前 reflection endpoint：

\[
T=10^m,
\qquad
\lambda=m-d,
\qquad
Q_0=c_Qq,
\]

\[
N=3D-C=c_-^2X,
\qquad
D=g2^m5^d,
\]

以及 `primitive-reduction.md` 已证明的

\[
\boxed{
H_0=c_uW_q,
\qquad
\alpha=TK+a_3=\omega W_q.
}
\tag{1.1}
\]

canonical factor equality 为

\[
H_0-Y_3=5^\lambda c_-^2X,
\qquad
H_0+Y_3=c_+^2Y,
\qquad
Y_3=ga_3.
\tag{1.2}
\]

所以

\[
\boxed{
H_0^2-Y_3^2
=5^\lambda c_Q^2XY.
}
\tag{1.3}
\]

另一方面 §16.44 的真正 `2,5`-本原 cofactor 是

\[
\boxed{
\widehat{\mathcal T}_2
=
2^mc_u^2g^2\mathscr S_0
-(c_Qq)^2 5^{2\lambda-d}XY,
}
\tag{1.4}
\]

其中

\[
\boxed{
\mathscr S_0
=T(K^2-26)-(2K-9)(2a_3+9T).
}
\tag{1.5}
\]

已有

\[
\widehat{\mathcal T}_2>0,
\qquad
\gcd(\widehat{\mathcal T}_2,10c_ug)=1,
\qquad
\widehat{\mathcal T}_2\equiv3\pmod4.
\tag{1.6}
\]

本文研究 `W_q` 与 (1.4) 的共同 odd-prime flow。

---

## 2. `已严格完成`：`\mathscr S_0` 在 reduced numerator 上精确线性化

由 (1.1)，

\[
a_3=\omega W_q-TK.
\tag{2.1}
\]

于是

\[
2a_3+9T
=2\omega W_q-T(2K-9).
\tag{2.2}
\]

代入 (1.5)：

\[
\begin{aligned}
\mathscr S_0
&=T(K^2-26)
-(2K-9)\bigl(2\omega W_q-T(2K-9)\bigr)\\
&=T\bigl(K^2-26+(2K-9)^2\bigr)
-2\omega(2K-9)W_q.
\end{aligned}
\]

定义

\[
\boxed{
F_W(K):=5K^2-36K+55.
}
\tag{2.3}
\]

其判别式恰为

\[
36^2-4\cdot5\cdot55=14^2,
\]
所以它在整数层完全分裂：

\[
\boxed{
F_W(K)=(K-5)(5K-11).
}
\tag{2.4}
\]

因此得到精确整数式

\[
\boxed{
\mathscr S_0
=T F_W(K)
-2\omega(2K-9)W_q.
}
\tag{2.5}
\]

这一步把原来的 numerator polynomial `\mathscr S_0` 直接接到 reduced numerator `W_q`；后续不再需要只通过 denominator gcd 间接接触两者。

---

## 3. `已严格完成`：`\widehat{\mathcal T}_2` 与 `W_q` 的全局 cofactor bridge

先用 (1.3) 改写 (1.4) 的 norm 项：

\[
(c_Qq)^2 5^{2\lambda-d}XY
=q^2 5^{\lambda-d}(H_0^2-Y_3^2).
\]

结合 (1.1)、`Y_3=ga_3`：

\[
\boxed{
\widehat{\mathcal T}_2
=
2^mc_u^2g^2\mathscr S_0
-q^2 5^{\lambda-d}
\bigl(c_u^2W_q^2-g^2a_3^2\bigr).
}
\tag{3.1}
\]

这里 `\lambda-d\ge0`，因为旧关系 `\nu_5=\lambda-2d\ge0`。

再把 (2.1)、(2.5) 代入 (3.1)。与 `W_q` 无关的常数项恰为

\[
2^mg^2T
\left(
 c_u^2F_W(K)+q^25^{2\lambda}K^2
\right),
\]
因为

\[
5^{\lambda-d}T^2
=2^mT5^{2\lambda}.
\]

定义新的 **height–cofactor resultant**

\[
\boxed{
\mathscr B_W
:=
c_u^2F_W(K)
+(q5^\lambda K)^2.
}
\tag{3.2}
\]

完整展开给出

\[
\boxed{
\widehat{\mathcal T}_2
=2^mg^2T\,\mathscr B_W
+W_q\mathscr E_W,
}
\tag{3.3}
\]

其中

\[
\begin{aligned}
\mathscr E_W={}&
-2^{m+1}c_u^2g^2\omega(2K-9)\\
&-q^25^{\lambda-d}c_u^2W_q
+q^25^{\lambda-d}g^2\omega^2W_q\\
&-2q^25^{\lambda-d}g^2\omega TK
\in\mathbf Z.
\end{aligned}
\tag{3.4}
\]

`primitive-reduction.md` 已证明 `W_q` 为奇数、`5\nmid W_q` 且 `\gcd(W_q,g)=1`。因此

\[
\gcd(2^mg^2T,W_q)=1.
\tag{3.5}
\]

由 (3.3) 得到全局 gcd identity：

\[
\boxed{
\gcd(\widehat{\mathcal T}_2,W_q)
=
\gcd(\mathscr B_W,W_q).
}
\tag{3.6}
\]

更精确地，若

\[
p^h\Vert W_q,
\]

则

\[
\boxed{
\min\{v_p(\widehat{\mathcal T}_2),h\}
=
\min\{v_p(\mathscr B_W),h\}.
}
\tag{3.7}
\]

这正是此前缺失的逐 prime-power bridge：`W_q` 与 odd inert excess 不再是两套平行的素因子列表。

---

## 4. `已严格完成`：height bridge 在第三分子上变成两个低次数二元型

若奇素数 `p\mid W_q`，由 (1.1)

\[
TK+a_3\equiv0\pmod{p^h},
\qquad h=v_p(W_q),
\]
所以

\[
K\equiv-a_3T^{-1}\pmod{p^h}.
\tag{4.1}
\]

将 (4.1) 代入 `F_W`，乘去单位 `T^2`：

\[
\boxed{
T^2F_W(K)
\equiv
(a_3+5T)(5a_3+11T)
\pmod{p^h}.
}
\tag{4.2}
\]

再定义

\[
\boxed{
G_W(K):=F_W(K)+4K^2
=9K^2-36K+55.
}
\tag{4.3}
\]

同样有

\[
\boxed{
T^2G_W(K)
\equiv
9a_3^2+36a_3T+55T^2
=(3a_3+6T)^2+19T^2
\pmod{p^h}.
}
\tag{4.4}
\]

所以 q-side 对应的是两个线性 third-numerator factors；f-side 则对应判别数 `-19` 的正定二元型。

---

## 5. `已严格完成`：q-saturation 与 height/cofactor 的共同深度只可能是一层 `23`

设

\[
p\ne3,
\qquad p\equiv3\pmod4,
\]
并同时满足

\[
p^e\Vert q,
\qquad
p^e\mid\mathscr L_{23},
\qquad
h:=v_p(W_q)>0,
\qquad
\tau:=v_p(\widehat{\mathcal T}_2)>0.
\tag{5.1}
\]

这里

\[
2\mathscr L_{23}=2a_3+9T.
\]

令

\[
\boxed{s:=\min\{e,h,\tau\}\ge1.}
\tag{5.2}
\]

由 (3.7)，`p^s\mid\mathscr B_W`。而 `p^e\mid q`，所以 (3.2) 的平方项在模 `p^s` 下消失；`p\nmid c_u` 来自 height-prime 的既有本原性。故

\[
\boxed{p^s\mid F_W(K).}
\tag{5.3}
\]

另一方面 `p^h\mid W_q` 与 `p^e\mid(2a_3+9T)` 给出

\[
2(TK+a_3)\equiv0\pmod{p^h},
\qquad
2a_3+9T\equiv0\pmod{p^e}.
\]

在深度 `s` 上相减，因 `p\nmid T`：

\[
\boxed{p^s\mid2K-9.}
\tag{5.4}
\]

现在使用整数 Bézout identity

\[
\boxed{
4F_W(K)+23
=(2K-9)(10K-27).
}
\tag{5.5}
\]

(5.3)–(5.5) 强迫

\[
p^s\mid23.
\]

所以

\[
\boxed{
p=23,
\qquad
s=1.
}
\tag{5.6}
\]

即

\[
\boxed{
\min\!\left\{
 v_{23}(q),
 v_{23}(W_q),
 v_{23}(\widehat{\mathcal T}_2)
\right\}=1
}
\tag{5.7}
\]

对任何真正同时进入 q-saturation、height 与 odd cofactor 的 `23` 成立。

这比 `primitive-reduction.md` 的“q-height 交集只可能是 `23`”更强：不仅素数被固定，**三对象共享的 prime-power 深度也不可能超过一层**。

---

## 6. `已严格完成`：f-saturation 与 height/cofactor 只可能是一层 `7` 或 `43`

现在设

\[
p^e\Vert f,
\qquad
p^e\mid\mathscr L_{23},
\qquad
h:=v_p(W_q)>0,
\qquad
\tau:=v_p(\widehat{\mathcal T}_2)>0,
\tag{6.1}
\]

仍令

\[
s:=\min\{e,h,\tau\}\ge1.
\tag{6.2}
\]

由

\[
f=5^\lambda q+2c_u
\]
得到完整深度

\[
q5^\lambda\equiv-2c_u\pmod{p^e}.
\tag{6.3}
\]

因此在模 `p^s` 下

\[
\mathscr B_W
\equiv
c_u^2\bigl(F_W(K)+4K^2\bigr)
=c_u^2G_W(K).
\]

结合 (3.7) 与 `p\nmid c_u`：

\[
\boxed{p^s\mid G_W(K).}
\tag{6.4}
\]

同 §5，height 与 saturation 给出

\[
p^s\mid2K-9.
\tag{6.5}
\]

而 `G_W` 满足第二个整数 Bézout identity

\[
\boxed{
4G_W(K)-301
=(2K-9)(18K+9).
}
\tag{6.6}
\]

故

\[
p^s\mid301=7\cdot43.
\]

`301` 平方自由，所以

\[
\boxed{
p\in\{7,43\},
\qquad
s=1.
}
\tag{6.7}
\]

也就是

\[
\boxed{
\min\!\left\{
 v_p(f),
 v_p(W_q),
 v_p(\widehat{\mathcal T}_2)
\right\}=1,
\qquad p=7\text{ or }43.
}
\tag{6.8}
\]

这把上一轮留下的无限 reciprocity class 压成了**两个固定素数**。

---

## 7. `已严格完成 / 审计降级`：f-height 的二次特征只是在 `7,43` 上的 shadow

由 (4.4)，任何 f-side common height prime 在简单层满足

\[
(3a_3+6T)^2\equiv-19T^2\pmod p.
\]

对 `p\ne19`：

\[
\left(\frac{-19}{p}\right)=1.
\]

当 `p\equiv3 (mod 4)` 时，二次互反律化为

\[
\boxed{\left(\frac p{19}\right)=1.}
\tag{7.1}
\]

但 §6 已把 saturation-height common prime 固定为 `7,43`，而直接检查

\[
\boxed{
\left(\frac7{19}\right)
=
\left(\frac{43}{19}\right)
=1.
}
\tag{7.2}
\]

同样，`primitive-reduction.md` 先前得到的

\[
\left(\frac p{23}\right)=-1,
\qquad
\left(\frac p5\right)\left(\frac p{11}\right)=1
\tag{7.3}
\]

对 `p=7,43` 都自动成立。

因此这些 quadratic signatures 在新的 finite resultant 之后不再提供额外排除力：

\[
\boxed{
\begin{array}{c|ccc}
p&(p/23)&(p/5)(p/11)&(p/19)\\ \hline
7&-1&1&1\\
43&-1&1&1
\end{array}}
\tag{7.4}
\]

后续若继续处理 `7,43`，必须使用更高 `p`-进深度、真实十进制代表或 Archimedean 大小；继续叠加同层 Legendre character 不会关闭它们。

---

## 8. `已严格完成`：denominator-height common inert support 已变成固定浅层集合

将 §§5–6 合并。若非 `3` inert prime 同时满足

1. `p\mid W_q`；
2. `p\mid\widehat{\mathcal T}_2`；
3. 它属于一个已饱和的 denominator primary factor `p^e\Vert qf`，即 `p^e\mid\mathscr L_{23}`；

则

\[
\boxed{
\begin{array}{c|c|c}
\text{side}&p&\min(v_p(\text{den}),v_p(W_q),v_p(\widehat{\mathcal T}_2))\\ \hline
q&23&1\\
f&7\text{ or }43&1.
\end{array}}
\tag{8.1}
\]

特别地

\[
\boxed{
\operatorname{Supp}^{\rm sat}_{3\bmod4}
(W_q,\widehat{\mathcal T}_2;qf)
\subseteq\{7,23,43\}.
}
\tag{8.2}
\]

所以“denominator odd excess”和“height odd carrier”不可能继续共享一个无界移动素数。任何无界移动的共同惰性素数都必须转入 endpoint-external channel。

---

## 9. `已严格完成`：endpoint-external common prime 被压成单个显式二次 Hensel 多项式

设

\[
p\ne3,
\qquad p\equiv3\pmod4,
\qquad
p\mid W_q,
\qquad
p\mid\widehat{\mathcal T}_2,
\qquad
p\nmid qf.
\tag{9.1}
\]

由 (3.6)，`p\mid\mathscr B_W`。写

\[
z:=q5^\lambda.
\]

则

\[
\boxed{
\mathscr B_W
=(5c_u^2+z^2)K^2
-36c_u^2K
+55c_u^2.
}
\tag{9.2}
\]

所以 endpoint-external common prime 不再是未命名 angle prime：它必须使一个显式二次式在真实 decimal prefix `K` 上消失。

它关于 `K` 的判别式为

\[
\boxed{
\Delta_W
=4c_u^2
\bigl(49c_u^2-55q^25^{2\lambda}\bigr).
}
\tag{9.3}
\]

因此模 `p` 有根必强迫

\[
\boxed{
49c_u^2-55q^25^{2\lambda}
\text{ 为 }0\text{ 或模 }p\text{ 平方}.
}
\tag{9.4}
\]

若 (9.4) 非零，则 `\mathscr B_W` 在模 `p` 上只有两个 simple root，之后每个 root 都唯一 Hensel 提升；若判别式为零，则共同 prime 被进一步压入单个 source-discriminant 接触

\[
\boxed{
p\mid49c_u^2-55q^25^{2\lambda}.}
\tag{9.5}
\]

此外 `p\nmid qf` 意味着归一化 source ratio

\[
\frac{q5^\lambda}{c_u}
\not\equiv0,-2\pmod p,
\tag{9.6}
\]

即 external channel 严格避开 q-side 与 f-side 两个 endpoint。

若需要直接使用第三分子而不是 `K`，(4.1) 还把 (9.2) 改写为

\[
\boxed{
 c_u^2(a_3+5T)(5a_3+11T)
 +(q5^\lambda a_3)^2
\equiv0\pmod p.
}
\tag{9.7}
\]

所以真正剩余的 moving common-prime 问题已经变成一个明确的二次 Hensel/resultant 问题，而不是抽象“spontaneous angle excess”。

---

## 10. 更新后的 A2 开放核

本轮没有证明 `A_2` 全局空性，但把 `primitive-reduction.md` 末尾的两条候选主线进一步压缩：

### 10.1 denominator 与 height 的共同 odd carrier

不再是无界素数族，而只剩

\[
\boxed{
q\text{-side}:23,
\qquad
f\text{-side}:7,43.
}
\tag{10.1}
\]

并且三对象共享的深度严格只有一层。要继续排除它们，需要研究“某一对象继续加深而另外两个已停止”的 higher-lift cancellation；普通二次特征已经没有新增信息。

### 10.2 endpoint-external common carrier

统一由

\[
\boxed{
\mathscr B_W
=c_u^2(K-5)(5K-11)+(q5^\lambda K)^2
}
\tag{10.2}
\]

控制，其判别式只含 source pair `(c_u,q5^\lambda)`：

\[
\boxed{
\Delta_W/(4c_u^2)
=49c_u^2-55q^25^{2\lambda}.
}
\tag{10.3}
\]

因此下一步最值得推进的是：

1. 对固定 `23,7,43`，把 `v_p(W_q)`、`v_p(\widehat{\mathcal T}_2)` 与 denominator exponent 超过共同第一层后的差值做一次显式 Hensel expansion；
2. 对 external common prime，把 (9.2)/(9.7) 与 source split 或 `D_{\rm src}` resultant 联立，优先处理判别式零通道 (9.5)；
3. 平行研究 `\widehat{\mathcal T}_2` 的 endpoint-external odd carrier 是否必须进入 `W_q`。如果能证明这一点，则 (8.2) 与 `W_q/3^\delta\equiv1 (mod 4)` 的偶 parity 会直接进入最终闭环。

继续单独追逐 `(N_0/p)=-1` 或 (7.3) 的 Legendre character 已经不会增加约束。

---

<a id="source-length-orbit"></a>

> 整合来源：`length-orbit.md`

# A2 length-orbit and fully coupled spontaneous reduction

> **依赖：** `source-length-resultant.md`、`spontaneous-angle.md`、`decimal-prefix-bridge.md`、`endpoint-lattice.md`。
>
> **严格状态：**本文审计 fixed length polynomial 与真实十进制轨道 `36·10^{M-1}` 的 `p`-进同步，并把 spontaneous angle、external double-root 与 prefix norm 全部联立，消去 `r_s,x,y` 后得到两个固定八次 length polynomial。对 `p=19`，消元系统有两条局部解，但其中一条精确落回 `f`-denominator boundary；真正的 external/spontaneous 只剩一条唯一 Hensel 轨道。本文仍**不宣称 A2 全局关闭**。

---

## 1. `已严格完成 / 降级`：simple length root 只给唯一指数轨道

设 `F(s)∈Z[s]`、`p∤10`，且

\[
F(s_0)\equiv0\pmod p,
\qquad F'(s_0)\not\equiv0\pmod p.
\]

若 `s_0≡36·10^{n_0} (mod p)`，则 Hensel 引理把 `s_0` 唯一提升为 `s_*∈Z_p`。令

\[
d=\operatorname{ord}_p(10),
\qquad \nu=v_p(10^d-1).
\]

当 `ν=1` 时，`10^d=1+pu`，`u∈Z_p^×`，所以同一模 `p` 轨道中的单位由一个 `p`-进指数参数唯一控制。于是

\[
\boxed{
\text{simple root}+v_p(10^d-1)=1
\Longrightarrow
\text{至多一条 }p\text{-进 decimal exponent branch}.}
\tag{1.1}
\]

若 `ν>1`，最初只有一个有限 Wieferich 型 compatibility gate；通过后仍回到一维唯一 lift。因此“唯一”本身不是空性，generic closure 必须加入第二个全局条件。

---

## 2. `已严格完成 / 降级`：旧 source/external 的 `19`-进 length lift 只刚性化

`source-length-resultant.md` 的 quartic 满足

\[
\mathcal L_{SW}(s)\equiv(s-2)(s-8)\pmod{19}.
\]

并且

\[
\boxed{10^{18}=1+15\cdot19\pmod{19^2}},
\tag{2.1}
\]

故

\[
\boxed{\operatorname{ord}_{19^k}(10)=18\cdot19^{k-1}}.
\tag{2.2}
\]

两个 simple roots 都唯一提升。前四层为

\[
\boxed{
\begin{array}{c|c|c|c|c}
k&s_1&s_2&M_1&M_2\\ \hline
1&2&8&10\ (18)&8\ (18)\\
2&211&255&100\ (342)&224\ (342)\\
3&2016&255&2152\ (6498)&4670\ (6498)\\
4&22593&61986&8650\ (123462)&50156\ (123462)
\end{array}}
\tag{2.3}
\]

所以继续机械升 `19^k` 不会自动排除旧 source/external overlap。

---

# 第二部分：spontaneous angle + external double-root + prefix norm

## 3. 三个局部方程

令

\[
s=36\cdot10^{M-1},
\qquad Y_s=11-9s.
\]

external prefix root `36P-11≡0` 给

\[
y\equiv\frac{Y_s}{s}\pmod p.
\tag{3.1}
\]

`decimal-prefix-bridge.md` 的 `R_N`、`spontaneous-angle.md` 的 `Omega_sp` 与 external discriminant 分别化成

\[
\boxed{
\mathcal N_{sp}(s,x)
=(x+2)^2(2025s^2x^2+Y_s^2)+10780x^2,
}
\tag{3.2}
\]

\[
\boxed{
\begin{aligned}
\mathcal O_{sp}(s,x,r_s)={}&
r_s\left[4(225sx^2+9s-11)^2-xY_s^2(99x-4)\right]\\
&+2xY_s^2(x+2),
\end{aligned}}
\tag{3.3}
\]

\[
\boxed{
\mathcal G_{sp}(x,r_s)
=55r_s^2(x+2)^2-49x^2.
}
\tag{3.4}
\]

任何 fully coupled candidate 都必须满足

\[
\mathcal N_{sp}\equiv\mathcal O_{sp}\equiv\mathcal G_{sp}\equiv0\pmod p.
\tag{3.5}
\]

---

## 4. `已严格完成`：全部消元只剩两个固定八次 length polynomial

定义

\[
A_{sp}^{(s)}
=4(225sx^2+9s-11)^2-xY_s^2(99x-4),
\]

\[
\mathcal R_{spD}
=220Y_s^4(x+2)^4-49(A_{sp}^{(s)})^2.
\]

先消去 `r_s`，再对 `x` 求 resultant，得到

\[
\boxed{
\operatorname{Res}_x(\mathcal N_{sp},\mathcal R_{spD})
=C\,s^8(9s-11)^8\mathcal P_1(s)\mathcal P_2(s),
}
\tag{4.1}
\]

其中

\[
C=1205534785939344000000000000,
\]

\[
\boxed{
\begin{aligned}
\mathcal P_1(s)={}&
1382549089196025s^8-133844136247800s^7
+3690923035544910s^6\\
&+7960772236243860s^5+3163200960625101s^4
+10662174653755284s^3\\
&+13341353191482096s^2-1874385042496296s
+62480266566916,
\end{aligned}}
\tag{4.2}
\]

\[
\boxed{
\begin{aligned}
\mathcal P_2(s)={}&
363844061254628703225s^8+989345243267031420000s^7\\
&+1615741998157561468590s^6+1886040813505705898580s^5\\
&+1569626813501484989229s^4+956049258626593813836s^3\\
&+390256979886873318384s^2+44160413329248524616s
+1475531078426217604.
\end{aligned}}
\tag{4.3}
\]

对 genuine spontaneous prime，`s(9s-11)` 是单位，因此必须满足

\[
\boxed{
\mathcal P_1(36\cdot10^{M-1})\equiv0
\quad\text{或}\quad
\mathcal P_2(36\cdot10^{M-1})\equiv0\pmod p.}
\tag{4.4}
\]

---

## 5. `已严格完成 / 关键审计`：模 `19` 只有一条 genuine external/spontaneous 解

模 `19`：

\[
\mathcal P_1(s)
\equiv-2(s-9)(s^3-4s^2+6s+3)(s^4-2s^3+2s^2-4s-8),
\]

\[
\mathcal P_2(s)
\equiv-3(s-2)(s+3)^2(s^3+3s^2-4s+6).
\]

直接代回三方程 (3.5)，只有两组单位解：

\[
(s,x,y,r_s)=(2,11,6,9),
\qquad(9,3,7,14).
\tag{5.1}
\]

但 genuine external/spontaneous 还要求 `p∤f`。由

\[
\frac{q5^\lambda}{c_u}
=r_s\frac{x+2}{x},
\tag{5.2}
\]

第一组给

\[
\frac{q5^\lambda}{c_u}\equiv2\pmod{19},
\qquad f/c_u\equiv4\not\equiv0,
\tag{5.3}
\]

而第二组给

\[
\frac{q5^\lambda}{c_u}\equiv-2\pmod{19},
\qquad\boxed{19\mid f}.
\tag{5.4}
\]

所以第二组只是 `f`-denominator boundary，不能计入 genuine III 类。这恰好与

\[
\operatorname{Res}_{r_s}(F_f,\Omega_{sp})
=-200x^3\Delta_0
\]
的理论边界一致。

因此真正的 fixed `19` spontaneous branch 只有

\[
\boxed{(s,x,y,r_s)=(2,11,6,9)\pmod{19}.}
\tag{5.5}
\]

其 Jacobian determinant 为 `1 mod 19`，故唯一 Hensel 提升。前四层 `(s,x,r_s)` 为

\[
\boxed{
(2,11,9),
(2,239,199),
(2890,961,2726),
(50903,48974,16444),
}
\tag{5.6}
\]

对应

\[
\boxed{
M\equiv10\ (18),
82\ (342),
2818\ (6498),
100288\ (123462).
}
\tag{5.7}
\]

所以 `19` 没有被局部 Hensel 排掉，但从“两条分支”严格缩成了**一条 genuine branch**。

---

# 第三部分：fixed `19` 与 secant cofactor 的 prime-power 交点

## 6. `已严格完成`：第一层恰命中左 secant endpoint `J=2`

external common-height double-root 还给

\[
18K-55\equiv0,
\qquad18a_3+55T\equiv0,
\qquad D+18C\equiv0\pmod{19}.
\]

因为 `18≡-1`、`55≡-2 (mod 19)`：

\[
\boxed{
K\equiv2,
\qquad a_3\equiv-2T,
\qquad C\equiv D
\pmod{19}.}
\tag{6.1}
\]

所以 fixed `19` 恰好撞上 rational-root 三点的左端点 `J=2`。

三点 polynomial 为

\[
F(J)=b_2^2TJ(TJ+2a_3)(K-J)^2-Q^2N_0(TJ+a_3)^2.
\]

故

\[
F(2)=4b_2^2T(T+a_3)(K-2)^2-Q^2N_0(2T+a_3)^2,
\tag{6.2}
\]

在 (6.1) 下自动有

\[
\boxed{19^2\mid F(2).}
\tag{6.3}
\]

而 endpoint rational-root factorization 是

\[
\boxed{
\Xi_-=
\frac{-F(2)}{2^{2M+2}5^{\nu_5}(D-C)}.}
\tag{6.4}
\]

因此第一层至少给

\[
v_{19}(D-C)+v_{19}(\Xi_-)\ge2.
\tag{6.5}
\]

---

## 7. `已严格完成`：若 height 与 linear double-root 都进到第二层，则 `19` 只落在 `Xi_-` 一层

令

\[
h=v_{19}(W_q),
\qquad \ell=v_{19}(18K-55).
\]

假设

\[
\boxed{h\ge2,\qquad\ell\ge2.}
\tag{7.1}
\]

由

\[
18qW_q=D(18K-55)+(D+18C)
\]
且 `19∤qD`，得到

\[
19^2\mid D+18C.
\]

但

\[
D-C=(D+18C)-19C,
\]
且 `19∤C`，所以

\[
\boxed{v_{19}(D-C)=1.}
\tag{7.2}
\]

同样，由 `18\alpha=T(18K-55)+(18a_3+55T)`、`alpha=omega W_q` 且 `19∤omega`，(7.1) 强迫

\[
19^2\mid18a_3+55T.
\tag{7.3}
\]

于是

\[
18(K-2)=(18K-55)+19,
\]

\[
18(2T+a_3)=(18a_3+55T)-19T.
\]

在模 `19` 的二阶正规化中：

\[
\frac{K-2}{19}\equiv18^{-1},
\qquad
\frac{2T+a_3}{19}\equiv-18^{-1}T,
\qquad
T+a_3\equiv-T.
\tag{7.4}
\]

另一方面 external prefix norm `R_N≡0` 给

\[
Q^2N_0\equiv3b_2^2\pmod{19}.
\tag{7.5}
\]

把 (7.4)–(7.5) 代入 (6.2)：

\[
\boxed{
\frac{F(2)}{19^2}
\equiv
-\frac{7b_2^2T^2}{18^2}
\not\equiv0\pmod{19}.}
\tag{7.6}
\]

所以

\[
\boxed{v_{19}(F(2))=2.}
\tag{7.7}
\]

结合 (6.4)、(7.2)：

\[
\boxed{v_{19}(\Xi_-)=1.}
\tag{7.8}
\]

而第一层直接代入 `J=3,4` 有

\[
F(3)\equiv-6b_2^2T^2,
\qquad
F(4)\equiv-12b_2^2T^2
\pmod{19},
\tag{7.9}
\]

故

\[
\boxed{19\nmid\Xi_C\Xi_+.}
\tag{7.10}
\]

更精确地，由 `C≡D`：

\[
\frac{\Xi_+}{\Xi_C}
\equiv
\frac{F(4)}{F(3)}\frac{C}{D+C}
\equiv2\cdot\frac12
\equiv1\pmod{19}.
\]

所以

\[
\boxed{\Xi_+\equiv\Xi_C\pmod{19}.}
\tag{7.11}
\]

若

\[
\Delta_-=(\Xi_C-\Xi_-)/(2^m5^d),
\qquad
\Delta_+=(\Xi_+-\Xi_C)/(2^m5^d),
\]
则 `19∤2^m5^d`，于是 fixed deep branch 的 secant allocation 被定向为

\[
\boxed{
19\nmid\Delta_-,
\qquad19\mid\Delta_+.
}
\tag{7.12}
\]

`endpoint-lattice.md` 的 curvature formula

\[
\Delta_--\Delta_+
=2^{m+1}5^dc_u^2\{g((2K-9)T-a_3)-H_0\}
\]
在 `K=2,a_3=-2T,H_0≡0 (mod 19)` 下恰为单位，所以 (7.12) 与已有 curvature 相容；它是新的**非对称 prime allocation**，但尚未单独矛盾。

---

## 8. 当前开放核

本轮对 `19` 的结论应严格分成两层：

1. genuine spontaneous/external 第一层只剩唯一 branch (5.5)；
2. 若其 height 与 linear root 都继续到第二层，则 `19` 在三 secant cofactors 上只能出现为
   \[
   v_{19}(\Xi_-)=1,
   \qquad v_{19}(\Xi_C)=v_{19}(\Xi_+)=0,
   \qquad19\mid\Delta_+,\ 19\nmid\Delta_-.
   \]

因此下一步不应继续扩大 `19^k`。真正值得追的是：

- shallow case `v_{19}(W_q)=1` 与 `W_q/3^δ≡1 (mod 4)` 的 pairing；
- deep case (7.12) 与 additive CRT / `D±C` 的完整 prime-power structure；
- 或把唯一 lifted branch 接回 `C` 的自然代表和 finite-defect shell，寻找 Archimedean incompatibility。

---

<a id="source-source-discriminant"></a>

> 整合来源：`source-discriminant.md`

# A2 source-discriminant and external double-root reduction

> **依赖：** `primitive-reduction.md`、`height-cofactor.md`，以及 `endpoint-lattice.md` 的 (16.101)、(16.424)、(16.432) 等 canonical identities。
>
> **严格状态：**本文继续处理 `height-cofactor.md` §9 留下的 endpoint-external common-prime channel。主要结果是恢复一个此前未显式列出的 source triangle，定义正的 source discriminant `D_W`，给出它与 `B_W` 的两个精确平方恒等式，并把 external double-root 从二次 Hensel 条件压成 source discriminant 与三个真实 decimal 线性代表的交点。本文仍**不宣称 A2 全局关闭**。

---

## 1. 统一记号

沿用当前 reflection endpoint：

\[
T=10^m,
\qquad
D=g2^m5^d,
\qquad
\lambda=m-d,
\]

\[
qW_q=DK-N,
\qquad
\alpha=TK+a_3=\omega W_q,
\qquad
H_0=c_uW_q.
\tag{1.1}
\]

并使用 `height-cofactor.md` 的缩写

\[
\boxed{z:=q5^\lambda.}
\tag{1.2}
\]

另有

\[
f=5^\lambda q+2c_u=z+2c_u.
\tag{1.3}
\]

本文件把 sphere scale `D` 与新的 source discriminant 区分开；后者记作 `\mathscr D_W`。

---

## 2. `已严格完成`：原拼接平面恢复出 source triangle

`endpoint-lattice.md` (16.432) 给出

\[
TN+a_3D=2^m5^dH_0.
\tag{2.1}
\]

另一方面由 (1.1)，

\[
\begin{aligned}
D\alpha-TqW_q
&=D(TK+a_3)-T(DK-N)\\
&=Da_3+TN.
\end{aligned}
\]

代入 `\alpha=\omega W_q`、(2.1) 与 `H_0=c_uW_q`：

\[
W_q(D\omega-Tq)=2^m5^dc_uW_q.
\]

`W_q>0`，故可约去：

\[
\boxed{D\omega-Tq=2^m5^dc_u.}
\tag{2.2}
\]

再除以 `2^m5^d`，利用 `D=g2^m5^d` 与

\[
\frac{T}{2^m5^d}=5^{m-d}=5^\lambda,
\]
得到新的全局整数恒等式

\[
\boxed{g\omega-q5^\lambda=c_u.}
\tag{2.3}
\]

即在 `z` 记号下

\[
\boxed{
z=g\omega-c_u,
\qquad
f=g\omega+c_u.
}
\tag{2.4}
\]

所以此前看起来独立的 `q`、`f` 两个 source endpoint，其实是同一个中心 `g\omega` 两侧的 difference/sum。

旧结果已有

\[
\gcd(g,c_u)=1,
\qquad
\gcd(\omega,c_u)=1.
\tag{2.5}
\]

故

\[
\boxed{
\gcd(g\omega,c_u)=1,
\qquad
\gcd(z,c_u)=\gcd(f,c_u)=1.
}
\tag{2.6}
\]

因为 `z,f` 都为正奇数，(2.4) 还重新恢复

\[
\boxed{\gcd(z,f)=1.}
\tag{2.7}
\]

这与旧的 `\gcd(q,f)=1` 一致，因为 `z=q5^\lambda` 且 `5\nmid f`。

---

## 3. `已严格完成`：source ratio 等于真实 denominator ratio

reflection endpoint 的 denominator formulas 为

\[
b_3=2^{M+m+1}5^dc_Qc_u,
\qquad
Q=2^{M+1}c_Qq.
\tag{3.1}
\]

乘以 `z=q5^\lambda`，并用 `d+\lambda=m`：

\[
\begin{aligned}
b_3z
&=2^{M+m+1}5^{d+\lambda}c_Qc_uq\\
&=2^{M+m+1}5^m c_Qc_uq\\
&=Tc_uQ.
\end{aligned}
\]

所以

\[
\boxed{b_3z=Tc_uQ,}
\tag{3.2}
\]

亦即

\[
\boxed{\frac z{c_u}=\frac{TQ}{b_3}.}
\tag{3.3}
\]

当前 endpoint 有 `b_3/T=w<843/1000<1`，而 `Q>1`，所以

\[
\boxed{z>c_u.}
\tag{3.4}
\]

事实上 `z/c_u>Q`，尺度分离极强。

---

## 4. `已严格完成`：正 source discriminant 与全局 inert parity supplier

`height-cofactor.md` 的二次式判别式使用

\[
49c_u^2-55z^2.
\]

由 (3.4) 它严格为负。定义正整数

\[
\boxed{
\mathscr D_W:=55z^2-49c_u^2>0.
}
\tag{4.1}
\]

`c_u,z` 都是奇数，因此

\[
\mathscr D_W
\equiv55-49
\equiv6\pmod8.
\]

于是

\[
\boxed{
\mathscr D_W\equiv6\pmod8,
\qquad
\frac{\mathscr D_W}{2}\equiv3\pmod4.
}
\tag{4.2}
\]

所以 `\mathscr D_W/2` 自身必含 `3 mod 4` 素数到奇次，并且总奇赋值 parity 为奇：

\[
\boxed{
\sum_{\substack{r\equiv3\ (4)}}
v_r(\mathscr D_W/2)
\equiv1\pmod2.
}
\tag{4.3}
\]

这提供了一个完全独立于 `\widehat{\mathcal T}_2\equiv3 (mod 4)` 的 source-side inert-prime supplier；但两者尚未证明必须使用同一个 prime，故 (4.3) 本身还不是 closure。

---

## 5. `已严格完成`：`\mathscr D_W` 与全部旧 source/denominator 因子的 overlap 固定化

由 (2.4)–(2.7) 可以直接逐模数观察 `\mathscr D_W`。

### 5.1 与 `c_u`

模 `c_u`：

\[
\mathscr D_W\equiv55z^2\pmod{c_u}.
\]

且 `\gcd(z,c_u)=1`，故

\[
\boxed{\gcd(\mathscr D_W,c_u)\mid55.}
\tag{5.1}
\]

特别地，若 `11\mid c_u`，则 `z` 为 `11`-进单位，第一项 `55z^2` 赋值恰为 `1`，而 `49c_u^2` 赋值至少为 `2`，所以

\[
\boxed{11\mid c_u\Longrightarrow v_{11}(\mathscr D_W)=1.}
\tag{5.2}
\]

若 `11\nmid c_u`，则 `11\nmid\mathscr D_W`。

### 5.2 与 `g`、`\omega`

由 `z=g\omega-c_u`，模 `g` 或模 `\omega` 都有 `z\equiv-c_u`。故

\[
\mathscr D_W
\equiv(55-49)c_u^2
=6c_u^2
\pmod g,
\]

以及同样的模 `\omega` 同余。结合 (2.5)：

\[
\boxed{
\gcd(\mathscr D_W,g)\mid6,
\qquad
\gcd(\mathscr D_W,\omega)\mid6.
}
\tag{5.3}
\]

所以任何非 `3` 的奇素数 divisor of `\mathscr D_W` 都不能来自 `g` 或 `\omega`。

### 5.3 与 `q`

因为 `z=q5^\lambda`，模 `q`：

\[
\mathscr D_W\equiv-49c_u^2\pmod q.
\]

旧 source split 给 `\gcd(q,c_u)=1`，故

\[
\boxed{\gcd(\mathscr D_W,q)\mid49.}
\tag{5.4}
\]

而且 `7`-primary 深度可以精确计价。若 `e=v_7(q)\ge1`，写
`z=7^ez_0`，其中 `7\nmid z_0c_u`。若 `e>1`，两项赋值分别至少 `4` 与恰 `2`，故 `v_7(\mathscr D_W)=2`。若 `e=1`，

\[
\frac{\mathscr D_W}{7^2}
=55z_0^2-c_u^2
\equiv-z_0^2-c_u^2\not\equiv0\pmod7,
\]

因为 `-1` 在模 `7` 下为非平方。因此统一有

\[
\boxed{7\mid q\Longrightarrow v_7(\mathscr D_W)=2.}
\tag{5.5}
\]

若 `7\nmid q`，则 (5.4) 直接给 `7\nmid\mathscr D_W`。所以 `7` 从不向 (4.3) 贡献奇 parity。

### 5.4 与 `f`

模 `f=z+2c_u` 有 `z\equiv-2c_u`，故

\[
\mathscr D_W
\equiv(220-49)c_u^2
=171c_u^2
=9\cdot19\,c_u^2
\pmod f.
\]

结合 `\gcd(f,c_u)=1`：

\[
\boxed{\gcd(\mathscr D_W,f)\mid171.}
\tag{5.6}
\]

特别地，非 `3` overlap 只可能是固定素数 `19`。而若 `19^e\Vert f`，则

\[
\boxed{
\min\{v_{19}(\mathscr D_W),e\}=1.
}
\tag{5.7}
\]

因为 `\mathscr D_W\equiv171c_u^2 (mod 19^e)`，右侧在 `e\ge2` 时赋值恰为 `1`，在 `e=1` 时截断深度也恰为 `1`。

因此，除固定素数

\[
\boxed{3,5,7,11,19}
\tag{5.8}
\]

外，`\mathscr D_W` 的奇素因子与

\[
c_u,g,\omega,q,f
\]
全部分离。对 `3 mod 4` support 而言，`7` 的深度又总为偶数，所以真正的固定 parity gates 只剩 `3,11,19`。

---

## 6. `已严格完成`：`\mathscr B_W` 也有固定全局 parity

沿用 `height-cofactor.md`：

\[
\mathscr B_W
=c_u^2(5K^2-36K+55)+z^2K^2.
\tag{6.1}
\]

当前 `b_2` 为偶数且 `\gcd(a_2,b_2)=1`，所以 `a_2` 为奇数。于是

\[
P=9\cdot10^{M-1}+a_2
\]

为奇数，故

\[
K=10P\equiv2\pmod4,
\qquad
K^2\equiv4\pmod8.
\tag{6.2}
\]

对

\[
F_W(K)=5K^2-36K+55
\]
有

\[
F_W(K)\equiv3\pmod8.
\]

又 `c_u,z` 为奇数，所以

\[
\boxed{\mathscr B_W\equiv3+4\equiv7\pmod8.}
\tag{6.3}
\]

特别地

\[
\boxed{
\sum_{\substack{r\equiv3\ (4)}}v_r(\mathscr B_W)
\equiv1\pmod2.
}
\tag{6.4}
\]

因此 source discriminant `\mathscr D_W/2` 与 cofactor resultant `\mathscr B_W` 都各自携带奇 inert parity。后续的关键不再是“供应惰性素数”，而是证明两套 parity 必须通过同一个 common-prime kernel 对齐。

---

## 7. `已严格完成`：两个精确平方恒等式

定义

\[
\boxed{A_W:=5c_u^2+z^2,}
\qquad
\boxed{L_W:=A_WK-18c_u^2.}
\tag{7.1}
\]

直接配方：

\[
\begin{aligned}
A_W\mathscr B_W
&=A_W^2K^2-36A_Wc_u^2K+55A_Wc_u^2\\
&=L_W^2+c_u^2(55z^2-49c_u^2).
\end{aligned}
\]

所以

\[
\boxed{
A_W\mathscr B_W
=L_W^2+c_u^2\mathscr D_W.
}
\tag{7.2}
\]

还有一个更适合 double-root 的 identity。由

\[
55A_W-\mathscr D_W
=324c_u^2=(18c_u)^2,
\tag{7.3}
\]
可直接展开得到

\[
\boxed{
55\mathscr B_W-K^2\mathscr D_W
=c_u^2(18K-55)^2.
}
\tag{7.4}
\]

(7.2) 是 `\mathscr B_W` 的 discriminant completion；(7.4) 则把 double-root 的公共素因子直接变成一个线性 prefix root。

---

## 8. `已严格完成`：external double-root 等价于 `18K-55` 的线性交点

设

\[
p\ne3,
\qquad
p\equiv3\pmod4,
\]
并假设

\[
p\mid\mathscr D_W,
\qquad
p\mid\mathscr B_W.
\tag{8.1}
\]

若 `p=5` 或 `11` 需单列；对 endpoint-external height prime，旧本原性已有 `p\nmid c_u`。现在固定

\[
p\notin\{3,5,11\},
\qquad p\nmid c_u.
\tag{8.2}
\]

由 (7.4)，(8.1) 立即给

\[
p\mid c_u^2(18K-55)^2.
\]

所以

\[
\boxed{p\mid18K-55.}
\tag{8.3}
\]

反过来，若 `p\mid\mathscr D_W` 且 `p\mid18K-55`，则 (7.4) 给
`55\mathscr B_W\equiv0 (mod p)`；在 (8.2) 下 `p\nmid55`，故

\[
\boxed{
 p\mid\mathscr D_W,\ p\mid\mathscr B_W
\iff
 p\mid\mathscr D_W,\ p\mid18K-55.
}
\tag{8.4}
\]

这把 `height-cofactor.md` 的 quadratic double-root 条件严格线性化。

还可检查 leading coefficient 不会同时退化。若 `p\mid A_W` 且
`p\mid\mathscr D_W`，则由 (7.3)

\[
p\mid324c_u^2,
\]

在 (8.2) 下只能 `p=3`，矛盾。因此

\[
\boxed{p\mid\mathscr D_W,\ p\ne3\Longrightarrow p\nmid A_W.}
\tag{8.5}
\]

所以这里确实是标准 quadratic double root，不存在“判别式与 leading coefficient 同时消失”的隐藏退化。

---

## 9. `已严格完成`：加入 `W_q` 后得到三个真实 decimal 线性 target

现在进一步假设 `p` 是真正的 external common height prime：

\[
p\mid W_q,
\qquad
p\mid\widehat{\mathcal T}_2,
\qquad
p\nmid qf,
\tag{9.1}
\]

并处于 discriminant-zero 子支 `p\mid\mathscr D_W`。由
`height-cofactor.md` 的 gcd bridge，`p\mid\mathscr B_W`，故 §8 给

\[
18K-55\equiv0\pmod p.
\tag{9.2}
\]

首先，`p` 不能整除 `\omega`。若 `p\mid\omega`，由 source triangle
`z=g\omega-c_u` 有 `z\equiv-c_u (mod p)`，于是

\[
\mathscr D_W
\equiv(55-49)c_u^2
=6c_u^2\not\equiv0\pmod p
\]

（`p\ne2,3` 且 `p\nmid c_u`），矛盾。因此

\[
\boxed{p\nmid\omega.}
\tag{9.3}
\]

所以 `v_p(\alpha)=v_p(W_q)`，特别地 `p\mid\alpha=TK+a_3`。利用

\[
18\alpha
=T(18K-55)+(18a_3+55T),
\]
与 (9.2)：

\[
\boxed{p\mid18a_3+55T.}
\tag{9.4}
\]

另一方面

\[
qW_q=D(K-3)+C
\]
来自 `N=3D-C`。乘以 `18`：

\[
18qW_q
=D(18K-55)+(D+18C).
\]

由 `p\nmid q`、`p\mid W_q` 与 (9.2)：

\[
\boxed{p\mid D+18C.}
\tag{9.5}
\]

因此 external double-root common prime 必落入四路交点

\[
\boxed{
 p\mid
\gcd\bigl(
\mathscr D_W,
18K-55,
18a_3+55T,
D+18C
\bigr).
}
\tag{9.6}
\]

其中后三个量全部是真实 decimal/prefix representative，而不再含 Gaussian quotient 或未命名 angle variable。

特别地模 `p`：

\[
\boxed{
K\equiv\frac{55}{18},
\qquad
\frac{a_3}{T}\equiv-\frac{55}{18},
\qquad
\frac CD\equiv-\frac1{18}.
}
\tag{9.7}
\]

于是 `J_def=N/D=3-C/D` 同样满足

\[
\boxed{J_{\rm def}\equiv K\equiv55/18\pmod p.}
\tag{9.8}
\]

---

## 10. `已严格完成`：double-root 的 prime-power 深度只有一个等深 cancellation

仍在 §8 的假设下。记

\[
b:=v_p(\mathscr B_W),
\qquad
d_s:=v_p(\mathscr D_W),
\qquad
\ell:=v_p(18K-55).
\tag{10.1}
\]

由 `p\mid\mathscr B_W` 可知 `p\nmid K`：否则 (6.1) 给
`\mathscr B_W\equiv55c_u^2 (mod p)`，与 `p\notin\{5,11\}` 矛盾。

所以 (7.4) 中 `55`、`K^2`、`c_u^2` 都是 `p`-进单位。若 `b\ne d_s`，两项赋值不同，故差的赋值就是较小者：

\[
\boxed{
\begin{aligned}
b<d_s&\Longrightarrow b=2\ell\ \text{为偶数},\\
d_s<b&\Longrightarrow d_s=2\ell\ \text{为偶数}.
\end{aligned}}
\tag{10.2}
\]

若 `b=d_s`，则两主项同深，只有一次 normalized cancellation 可继续提升，并且

\[
\boxed{2\ell\ge b=d_s.}
\tag{10.3}
\]

因此 double-root 的高阶行为不再有任意分支：

\[
\boxed{
\min\{b,d_s\}\text{ 若为奇数，必有 }b=d_s.
}
\tag{10.4}
\]

即 odd depth 只能发生在 `\mathscr B_W` 与 source discriminant **等深**后的一次 cancellation；若两者深度不同，较浅层自动为偶数。

结合 `height-cofactor.md`

\[
\min\{v_p(\widehat{\mathcal T}_2),v_p(W_q)\}
=
\min\{b,v_p(W_q)\},
\]
(10.2)–(10.4) 给出了 external common carrier 的第一条真正 higher-lift parity law。

---

## 11. `已严格完成`：固定 `23` 的 higher lift 只在深度 `2` 发生一次碰撞

`q`-side fixed intersection 的 `23` 还有一个独立的精确解释。回忆

\[
F_W(K)=(K-5)(5K-11).
\tag{11.1}
\]

在 special `23` root `2K\equiv9 (mod 23)` 下，

\[
K\equiv\frac{11}{5}\pmod{23},
\]
且 `K-5`、`5K+11` 都是 `23`-进单位。因此

\[
v_{23}(F_W(K))=v_{23}(5K-11).
\tag{11.2}
\]

关键的整数恒等式为

\[
\boxed{
25(K^2-26)
=(5K-11)(5K+11)-23^2.
}
\tag{11.3}
\]

特别地，`F_W` 的相关有理根

\[
K=\frac{11}{5}
\]
本身满足

\[
\boxed{
\left(\frac{11}{5}\right)^2-26
=-\frac{23^2}{25}.
}
\tag{11.4}
\]

所以 `11/5` 恰好已经是 `\sqrt{26}` 的模 `23^2` Hensel 近似，但不是一个真正的有理平方根。

令

\[
a:=v_{23}(5K-11).
\]

由 (11.3) 且 `5K+11` 为单位：

\[
\boxed{
\begin{aligned}
a<2&\Longrightarrow v_{23}(K^2-26)=a,\\
a>2&\Longrightarrow v_{23}(K^2-26)=2,\\
a=2&\Longrightarrow v_{23}(K^2-26)\ge2,
\end{aligned}}
\tag{11.5}
\]

最后一行的额外深度只能来自两个正规化 `23^2` 项的一次 cancellation。

这说明 special `23` 的高阶 q-prefix 行为不存在第二套无界 Hensel tree：`F_W` root 与 `\sqrt{26}` root 的差异被固定在**唯一阈值 `23^2`**。这与 `height-cofactor.md` 已证明的三对象共同深度只能一层相容，并进一步解释为什么 `23` 会作为唯一 q-height intersection 出现。

---

## 12. `已严格完成 / 审计降级`：全局 Jacobi reciprocity 不会自动闭环

(4.2) 与 (6.3) 给出

\[
\frac{\mathscr D_W}{2}\equiv3\pmod4,
\qquad
\mathscr B_W\equiv7\pmod8.
\]

看起来两边都是 odd inert parity supplier，似乎可以直接用 quadratic reciprocity 制造符号冲突。完整审计表明 generic coprime 层会精确自洽。

设

\[
D_0:=\mathscr D_W/2,
\]
并暂时假设

\[
\gcd(55\mathscr B_W,D_0)=1,
\qquad
11\nmid c_u.
\tag{12.1}
\]

由 (7.4) 模 `D_0`：

\[
55\mathscr B_W
\equiv c_u^2(18K-55)^2\pmod{D_0},
\]
所以

\[
\left(\frac{\mathscr B_W}{D_0}\right)
=
\left(\frac{55}{D_0}\right).
\tag{12.2}
\]

而由 `\mathscr D_W=55z^2-49c_u^2`，且 `5\nmid c_u`，有

\[
D_0\equiv3c_u^2\pmod5,
\qquad
D_0\equiv3c_u^2\pmod{11}.
\tag{12.3}
\]

因此

\[
\left(\frac{D_0}{5}\right)=-1,
\qquad
\left(\frac{D_0}{11}\right)=1.
\]

结合 `D_0\equiv3 (mod 4)` 的 reciprocity sign：

\[
\boxed{
\left(\frac{55}{D_0}\right)=1.
}
\tag{12.4}
\]

另一方面，由 (7.2) 模任意 `p\mid\mathscr B_W` 且 `p\nmid A_Wc_uD_0`：

\[
L_W^2\equiv-2c_u^2D_0\pmod p,
\]
故

\[
\left(\frac{D_0}{p}\right)
=
\left(\frac{-2}{p}\right).
\]

乘到整个 `\mathscr B_W`，并使用 `\mathscr B_W\equiv7 (mod 8)`：

\[
\left(\frac{D_0}{\mathscr B_W}\right)
=-1.
\tag{12.5}
\]

因为 `D_0\equiv\mathscr B_W\equiv3 (mod 4)`，二次互反律给

\[
\left(\frac{\mathscr B_W}{D_0}\right)
=-\left(\frac{D_0}{\mathscr B_W}\right)
=1,
\]
恰好与 (12.2)–(12.4) 相同。

所以

\[
\boxed{
\text{generic global Jacobi pass is an identity, not a contradiction.}
}
\tag{12.6}
\]

后续不能仅凭 `D_0,B_W` 都是 `3 mod 4` 再做一轮 Legendre/Jacobi bookkeeping；真正新信息必须来自 (9.6) 的 decimal linear representatives、(10.4) 的等深 cancellation，或固定 `3,11,19,23,7,43` 的 higher-lift gates。

---

## 13. 更新后的开放核

本轮把 `height-cofactor.md` 的 external channel 再压一层：

1. source 变量统一成
   \[
   \boxed{z=g\omega-c_u,\qquad f=g\omega+c_u};
   \]
2. 原判别式改成正整数
   \[
   \boxed{\mathscr D_W=55z^2-49c_u^2>0,\quad \mathscr D_W/2\equiv3\pmod4};
   \]
3. 除固定 `3,5,7,11,19` 外，`\mathscr D_W` 的奇素因子与 `c_u,g,\omega,q,f` 全部分离；`7` 的赋值永远为偶；
4. cofactor resultant 本身满足
   \[
   \boxed{\mathscr B_W\equiv7\pmod8};
   \]
5. double-root 精确等价于
   \[
   \boxed{p\mid\mathscr D_W,\quad p\mid18K-55};
   \]
6. 若再进入 height common channel，则还强迫
   \[
   \boxed{p\mid18a_3+55T,\quad p\mid D+18C};
   \]
7. double-root higher lift 的较浅赋值若为奇数，`\mathscr B_W` 与 `\mathscr D_W` 必须先达到同一深度；
8. special `23` 的 `F_W` root 与 `\sqrt{26}` root 只在固定阈值 `23^2` 发生一次 collision。

因此当前最值得继续推进的两个目标是：

- 对 (9.6) 求真正的 source/decimal resultant，优先利用 `C` 的自然代表 (16.101)–(16.104) 控制 `D+18C`；
- 把 (4.3)、(6.4)、`W_q/3^\delta\equiv1 (mod 4)` 三个 parity statement 接成一个 prime-flow conservation law，证明 `\widehat{\mathcal T}_2` 的 external odd carrier 必进入 `W_q` 或 `\mathscr D_W` 的 odd-depth kernel。

普通的 global Jacobi reciprocity 已由 §12 严格降级，不应再作为下一步主线。

---

<a id="source-source-length-resultant"></a>

> 整合来源：`source-length-resultant.md`

# A2 source–external length resultant

> **依赖：** `source-spontaneous-bridge.md`、`hensel.md`、`decimal-discriminant.md`。
>
> **严格状态：**本文继续处理 moving external double-root 与 source excess 的可能交集。把 source prefix contact `D_src`、linear prefix root `36P-11` 与固定 quartic `R_SW` 联立后，所有 `a_2,b_2,x,r` 都可消去，只剩 `s=36·10^{M-1}` 的固定四次 length polynomial。其 genuine inert **bad-reduction gate** 最终只剩 `p=19`；模 `19` 的实际有限根仍然是 simple roots，并进一步强迫 `M mod 18` 只取两类。本文仍**不宣称 A2 全局关闭**。

---

## 1. `D_src` 与 double-root prefix 的纯 decimal 合并

当前 endpoint 固定 `a_1=9`。令

\[
S:=10^{M-1},
\qquad
A_0=9S,
\qquad
P=A_0+a_2,
\qquad
C_0=\frac{9b_2}{2}.
\]

source prefix contact 为

\[
D_{\rm src}=C_0^2-A_0a_2.
\tag{1.1}
\]

moving external double-root 已由 `decimal-discriminant.md` / `decimal-prefix-bridge.md` 强迫

\[
36P-11\equiv0\pmod p.
\tag{1.2}
\]

把 `a_2=P-9S` 代入 `4D_src`：

\[
4D_{\rm src}
=81b_2^2-36Sa_2
=81b_2^2-36SP+324S^2.
\]

在 (1.2) 下得到新的纯 denominator/length contact：

\[
\boxed{
 p\mid D_{\rm src},\ p\mid36P-11
\Longrightarrow
p\mid81b_2^2+324S^2-11S.
}
\tag{1.3}
\]

现在写

\[
x=\frac{b_2}{10^M}=\frac{b_2}{10S},
\qquad
s:=36S.
\tag{1.4}
\]

因为 genuine external prime 不整除 `2·3·5S`，(1.3) 等价于

\[
\boxed{
225s x^2+9s-11\equiv0\pmod p.
}
\tag{1.5}
\]

---

## 2. `已严格完成`：消去 `x` 得到固定 length polynomial

`source-spontaneous-bridge.md` 已证明 source/external overlap 必满足

\[
\boxed{
\mathcal R_{SW}(x)
=-480029x^4+40568x^3+4496x^2+7040x+3520
\equiv0\pmod p.
}
\tag{2.1}
\]

将 (2.1) 与 (1.5) 对 `x` 求 resultant，得到只含 `s` 的固定 quartic：

\[
\boxed{
\begin{aligned}
\mathcal L_{SW}(s):={}&
19964008847990601s^4
+26176176015770484s^3\\
&-6142888878869754s^2
-12826705293056556s\\
&+3373694017753081.
\end{aligned}}
\tag{2.2}
\]

因此若 moving external double-root 同时承担 source excess，则

\[
\boxed{
\mathcal L_{SW}(36\cdot10^{M-1})\equiv0\pmod p.
}
\tag{2.3}
\]

这一步把 `(x,r,a_2,b_2)` 全部消掉；source/external overlap 已经变成一个**纯 decimal length Hensel condition**。

---

## 3. `已严格完成`：length polynomial 的 discriminant / bad-reduction gate 是固定有限集

(2.2) 的整数判别式因子分解为

\[
\boxed{
\begin{aligned}
\operatorname{Disc}(\mathcal L_{SW})
={}&-2^{48}3^{29}5^{28}7^6 11^{18}19^2\\
&\cdot101^4\cdot748057\cdot45503^2.
\end{aligned}}
\tag{3.1}
\]

其中

\[
748057\equiv1\pmod4,
\qquad
101\equiv1\pmod4,
\]

且 `748057` 与 `45503` 都是素数，而

\[
45503\equiv3\pmod4.
\tag{3.2}
\]

对 genuine non-`3` external inert prime：

- `p=7,11` 已由 `D_dec=55T^2Q^2-49b_3^2` 的单位性直接排除；
- `p=5,101,748057` 不是 `3 mod 4` inert gate；
- 因而 quartic 的 discriminant / degree-drop 审计只需继续检查 `19,45503`。

这里要区分两个概念：`p` 整除整数判别式意味着 degree-4 模型发生 bad reduction，**不自动等于实际有限根为重根**；`p=19` 正是这种区别必须保留的例子。

---

## 4. `已严格完成`：`45503` 与 discriminant-zero character 不相容

external discriminant-zero 条件

\[
55T^2Q^2\equiv49b_3^2\pmod p
\]
且 `p\nmid Tb_3Q` 强迫

\[
\boxed{\left(\frac{55}{p}\right)=1.}
\tag{4.1}
\]

对 `p=45503`：

\[
45503\equiv3\pmod5,
\qquad
45503\equiv7\pmod{11},
\qquad
45503\equiv3\pmod4.
\]

直接用二次互反律得到

\[
\boxed{
\left(\frac{55}{45503}\right)=-1.
}
\tag{4.2}
\]

因此

\[
\boxed{p=45503\text{ 不可能进入 genuine external double-root}.}
\tag{4.3}
\]

所以 source/external length polynomial 的 genuine inert bad-reduction gate 最终只剩

\[
\boxed{p=19.}
\tag{4.4}
\]

对所有其他 non-`3` inert external primes，`L_SW` 的 length root 都是 simple root，后续 `M`-方向只有唯一 Hensel lift。

---

## 5. `已严格完成`：固定 `19` 退化为二次式，但两个有限根仍然 simple

模 `19` 化简 (2.2)，高次 leading content 自动消去，实际有限多项式变成

\[
\boxed{
\mathcal L_{SW}(s)
\equiv(s-2)(s-8)\pmod{19}.
}
\tag{5.1}
\]

两个根 `2,8` 不同，因此 `19` 虽整除 degree-4 整数判别式，实际有限根仍为 simple roots；它只是**degree-drop bad-reduction gate**，不是新的 repeated-root Hensel tree。

`p=19` 的 source/external overlap 强迫

\[
s=36\cdot10^{M-1}\equiv2\text{ 或 }8\pmod{19}.
\tag{5.2}
\]

又

\[
\operatorname{ord}_{19}(10)=18,
\qquad36\equiv-2\pmod{19}.
\]

逐一解出：

\[
36\cdot10^n\equiv2\pmod{19}
\iff n\equiv9\pmod{18},
\]

\[
36\cdot10^n\equiv8\pmod{19}
\iff n\equiv7\pmod{18}.
\]

令 `n=M-1`，得到

\[
\boxed{
M\equiv8\text{ 或 }10\pmod{18}.
}
\tag{5.3}
\]

还可恢复对应 source prefix roots：

\[
\begin{array}{c|c}
s\pmod{19}&x=b_2/10^M\pmod{19}\\ \hline
2&13\\
8&15.
\end{array}
\tag{5.4}
\]

在两类上，source ratio (2.3) 都选择 external orientation

\[
\boxed{z/c_u\equiv2\pmod{19},}
\tag{5.5}
\]

故 `f=z+2c_u\equiv4c_u\not\equiv0 (mod 19)`，与 external 定义一致；另一根 `z/c_u=-2` 正是 f-side，已被排除在 moving external channel 之外。

---

## 6. 更新后的 source/external 开放核

若 moving external double-root 还想同时承担 source excess，现在必须经过以下链：

\[
\boxed{
\begin{array}{c}
p^s\mid D_{\rm src},\\
p\mid\mathscr R_{SW},\\
p\mid\mathcal L_{SW}(36\cdot10^{M-1}).
\end{array}}
\tag{6.1}
\]

其中：

1. `R_SW` 对所有 genuine inert external primes 都是 simple-root；
2. `L_SW` 的所有**实际有限根**对 genuine inert external primes 也都是 simple：普通 primes 由 discriminant 排除重根，唯一 bad-reduction prime `19` 的实际 reduction 是 `(s-2)(s-8)`；
3. `19` 还只允许
   \[
   M\equiv8,10\pmod{18};
   \]
4. 因此 source/external overlap 已不再有二维 source Hensel phase，也没有任何 surviving repeated-length branch。

这仍未证明交集为空。下一步若继续 source 线，应研究 simple root `L_SW(36·10^{M-1})` 与 `10` 的乘法轨道是否能和 `D_src` 的完整 `p^s` 深度长期同步；固定 `19` 则可以直接做两条 simple root 的 `19`-进二阶提升。

---

<a id="source-source-spontaneous-bridge"></a>

> 整合来源：`source-spontaneous-bridge.md`

# A2 source–spontaneous overlap resultant

> **依赖：** `hensel.md`、`source-discriminant.md`、`decimal-prefix-bridge.md`。
>
> **严格状态：**本文审计 genuine moving external double-root 是否还能同时属于旧 source-excess channel。交集尚未被证明为空，但 source Hensel 线性根与 source discriminant 根可以完全消元成一个固定 quartic；对所有 genuine non-`3` inert external primes，该 quartic 根必为 simple root，并有精确的 prime-power valuation threshold。因此 source/external overlap 不再携带额外 Hensel 分叉。本文仍**不宣称 A2 全局关闭**。

---

## 1. 当前 reflection 下的 source Hensel 变量

固定当前 endpoint `a_1=9`、`sigma_5=0`。沿用 `hensel.md` 的

\[
x=\frac{b_2}{10^M},
\qquad
r:=\frac{5^\lambda D_0}{c_Q},
\qquad
D_0=2^mg.
\tag{1.1}
\]

source Hensel 线性式为

\[
\boxed{
\Phi(x,r):=(99x-4)r-2x-4.
}
\tag{1.2}
\]

若 `p` 是 source excess prime，且

\[
p^{2s}\Vert\sigma,
\qquad p\equiv3\pmod4,
\]
则 `hensel.md` 已证明

\[
\boxed{v_p(\Phi)=2s,}
\tag{1.3}
\]

并且

\[
p^s\mid D_{\rm src}.
\tag{1.4}
\]

旧证明还给出对这种 inert prime

\[
\boxed{p\nmid99x-4.}
\tag{1.5}
\]

这里对 rational `x,r` 使用扩张赋值；source/external 分离保证其十进制分母都是 `p`-进单位。

---

## 2. `已严格完成`：source ratio 与新 discriminant ratio 的精确转换

source split 在 reflection 中为

\[
c_Qq=5^M+D_0c_u.
\tag{2.1}
\]

而

\[
b_2=2^{M+1}D_0c_u,
\]
故

\[
x=\frac{b_2}{10^M}
=\frac{2D_0c_u}{5^M}.
\]

于是

\[
\frac{5^M}{D_0c_u}=rac2x.
\tag{2.2}
\]

令 `source-discriminant.md` 的

\[
z=q5^\lambda.
\]

则由 (2.1)：

\[
\begin{aligned}
\frac z{c_u}
&=\frac{5^\lambda q}{c_u}\\
&=\frac{5^\lambda D_0}{c_Q}
\left(
\frac{5^M}{D_0c_u}+1
\right).
\end{aligned}
\]

所以

\[
\boxed{
\frac z{c_u}
=r\frac{x+2}{x}.
}
\tag{2.3}
\]

新 source discriminant

\[
\mathscr D_W=55z^2-49c_u^2
\]
因此满足

\[
\boxed{
\Gamma(x,r)
:=55r^2(x+2)^2-49x^2
=x^2\frac{\mathscr D_W}{c_u^2}.
}
\tag{2.4}
\]

对 genuine external prime，`p\nmid xc_u`，故

\[
\boxed{v_p(\Gamma)=v_p(\mathscr D_W)=v_p(\mathscr D_{\rm dec}).}
\tag{2.5}
\]

---

## 3. `已严格完成`：消去 source ratio 得到固定 quartic

把

\[
A:=99x-4,
\qquad
B:=2x+4
\]
写成

\[
\Phi=Ar-B.
\]

对 `r` 求 resultant：

\[
\boxed{
\begin{aligned}
\mathcal R_{SW}(x)
&:=\operatorname{Res}_r(\Phi,\Gamma)\\
&=-480029x^4+40568x^3+4496x^2+7040x+3520.
\end{aligned}}
\tag{3.1}
\]

无需除法的 Bézout identity 更精确：

\[
\boxed{
A^2\Gamma-\mathcal R_{SW}(x)
=55(x+2)^2\Phi\,(Ar+B).
}
\tag{3.2}
\]

因此 source-excess 与 external discriminant-zero 的交点不再是二维 `(x,r)` 接触；它必须落在一个固定 quartic 的根上。

为了完全整数化，令

\[
X_M:=10^M.
\]

定义

\[
\boxed{
\begin{aligned}
\mathscr R_{SW}:={}&X_M^4\mathcal R_{SW}(b_2/X_M)\\
={}&-480029b_2^4
+40568b_2^3X_M
+4496b_2^2X_M^2\\
&+7040b_2X_M^3
+3520X_M^4.
\end{aligned}}
\tag{3.3}
\]

对 `p\nmid10`，

\[
v_p(\mathscr R_{SW})=v_p(\mathcal R_{SW}(x)).
\tag{3.4}
\]

---

## 4. `已严格完成`：source depth 与 discriminant depth 只有一个等深 cancellation

设

\[
d_W:=v_p(\mathscr D_W)=v_p(\Gamma).
\]

source excess 给 `v_p(\Phi)=2s`。在共同模 `p` 根上，(1.5) 给 `A` 为单位；又 `x+2` 也是单位，否则 `B=0` 与 `Ar=B` 会强迫 `r=0`，违背 source/external 本原性。

而

\[
Ar+B\equiv2B=4(x+2)\not\equiv0\pmod p.
\]

所以 (3.2) 右边除 `Phi` 外的系数全部是 `p`-进单位（genuine external double-root 已排除 `p=5,11`）。因此

\[
\boxed{
\begin{aligned}
d_W<2s
&\Longrightarrow
v_p(\mathscr R_{SW})=d_W,\\
d_W>2s
&\Longrightarrow
v_p(\mathscr R_{SW})=2s,\\
d_W=2s
&\Longrightarrow
v_p(\mathscr R_{SW})\ge2s.
\end{aligned}}
\tag{4.1}
\]

最后一行只有一次 normalized equal-depth cancellation 可以继续提升。

所以 source/external overlap 的高阶自由度已经被压成一个明确阈值：

\[
\boxed{
\min\{d_W,2s\}
\text{ 若未发生等深碰撞，就等于 }
v_p(\mathscr R_{SW}).}
\tag{4.2}
\]

---

## 5. `已严格完成`：对 genuine inert external prime，quartic 根永远 simple

quartic (3.1) 的整数判别式精确为

\[
\boxed{
\operatorname{Disc}(\mathcal R_{SW})
=-2^{24}\cdot3\cdot5^2\cdot7^6\cdot11^2\cdot101^4\cdot748057.
}
\tag{5.1}
\]

其中 `748057` 是素数且

\[
748057\equiv1\pmod4,
\qquad
101\equiv1\pmod4.
\tag{5.2}
\]

故一个 `3 mod 4` 奇素数若整除 quartic discriminant，只可能来自

\[
3,7,11.
\]

但 genuine non-`3` external discriminant root 已有 `p\nmid b_3QT`，而

\[
\mathscr D_{\rm dec}=55T^2Q^2-49b_3^2.
\]

若 `p=7`，右边模 `7` 为 `55T^2Q^2\not\equiv0`；若 `p=11`，则为 `-49b_3^2\not\equiv0`。所以二者都不可能进入 discriminant-zero channel。

因此

\[
\boxed{
 p\ne3,\ p\equiv3\pmod4,\ p\text{ genuine external double-root}
\Longrightarrow
p\nmid\operatorname{Disc}(\mathcal R_{SW}).}
\tag{5.3}
\]

也就是说任何 source/external 交点在 quartic 上都是 simple root；一旦其模 `p` 根确定，后续只有唯一 Hensel lift，不存在第二棵无界分叉树。

---

## 6. `已严格完成`：若同时属于 source excess，只剩两个 pure-prefix contacts

若 moving external double-root 还承担 source excess，则除了

\[
p^s\mid D_{\rm src}
\]
外，本文还强迫

\[
p\mid\mathscr R_{SW},
\]
并由 §5 知 `\mathscr R_{SW}` 在该 prime 上是 simple-root contact。

因此 source/external intersection 的规范形式已经从原来的

\[
\Phi(x,r),\quad
\Psi_9(y,r),\quad
\mathscr D_W
\]
三套混合对象，压成

\[
\boxed{
D_{\rm src}
\quad+\quad
\mathscr R_{SW}(b_2,10^M),
}
\tag{6.1}
\]

两条 pure-prefix 条件，再附带 (4.1) 的单一 depth threshold。

这还不是矛盾；但它说明 moving double-root 即使回流到 source excess，也不再获得新的 source ratio 或 Hensel phase 自由度。

---

## 7. 更新后的开放核

本轮严格结论是：

1. moving external double-root 已由 `decimal-prefix-bridge.md` 与 denominator-prefix 完全分离；
2. 若它再进入 source excess，则 source ratio `r` 可完全消去，只留下固定 quartic `R_SW`；
3. 该 quartic 对所有 genuine non-`3` inert external primes 均为 simple-root，因此 source/external overlap 只有唯一 `p`-进 lift；
4. source depth `2s` 与 discriminant depth `d_W` 的相互作用只有 (4.1) 的一个等深 cancellation；
5. 剩余 source/external overlap 只需研究
   \[
   p^s\mid D_{\rm src},
   \qquad
   p\mid\mathscr R_{SW}.
   \]

下一步若继续这条线，应该直接消去 `b_2`，把 `D_src`、`R_SW` 与

\[
36P-11=0
\]
联成立一个只关于 `10^{M-1}` 的 length polynomial；继续在 `(x,r)` 空间做 Hensel 展开已经没有新增信息。

---

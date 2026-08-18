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
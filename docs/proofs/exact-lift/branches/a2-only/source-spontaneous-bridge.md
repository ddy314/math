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
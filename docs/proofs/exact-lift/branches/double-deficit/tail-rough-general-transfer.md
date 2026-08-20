# DD general rough `Q`-cancellation 的三 payer transfer

> **依赖：** [`tail-rough-cq-excess.md`](tail-rough-cq-excess.md)、[`tail-source-cancellation-transfer.md`](tail-source-cancellation-transfer.md)、[`tail-hard-source-derivative-sheet.md`](tail-hard-source-derivative-sheet.md)、`global-framework.md` 的 unified quadratic / primitive recovery，以及 `core.md` 的 DD gap quadratic 与 projective denominator formula。
>
> **严格状态：** `已严格完成（整个 gcd-normal DD tail 的 odd non-decimal `d_0` support）`。
>
> `tail-rough-cq-excess.md` 对每个 `p|core_10(d_0)` 写
> \[
> v_p(b_1)=v_p(b_2)=E,
> \qquad v_p(b_3)=j,
> \qquad c=v_p(C_Q),
> \]
> 并定义真正未被 denominator overlap 支付的 primitive concat overflow
> \[
> x_p=\max\bigl(c-j-\min(E,j),0\bigr).
> \]
> 本文证明该 overflow 不可能继续悬空。令
> \[
> h_{12}=(b_1,b_2),
> \qquad N_0:=\mathcal N_{12}/h_{12}^2,
> \]
> \[
> R_3^{\rm den}:=
> \frac{b_3}{(b_3,\operatorname{lcm}(b_1,b_2))}.
> \]
> 则逐 prime 有
> \[
> \boxed{
> x_p\le
> \max\Bigl(
> v_p(C),
> v_p(N_0),
> v_p(R_3^{\rm den})
> \Bigr).
> }
> \tag{General-transfer-local}
> \]
> 因而若 `X_Q` 是 `tail-rough-cq-excess.md` 的 canonical overflow integer，
> \[
> \boxed{
> X_Q\mid
> \operatorname{lcm}\!\left(
> \operatorname{core}_{10}(C),
> \operatorname{core}_{10}(N_0),
> \operatorname{core}_{10}(R_3^{\rm den})
> \right).
> }
> \tag{General-transfer-global}
> \]
> 再用 projective denominator 的逐 prime identity，第三 payer 可继续送入 `Z_0 a`：
> \[
> \boxed{
> X_Q\mid
> \operatorname{lcm}\!\left(
> \operatorname{core}_{10}(C),
> \operatorname{core}_{10}(N_0),
> \operatorname{core}_{10}(Z_0a)
> \right).
> }
> \tag{General-transfer-projective}
> \]
> 因此 post-tail 第二次 Schmidt 的唯一 rough loss已从匿名 denominator cancellation
> 压成三个明确 numerator/projective payer。

---

## 1. local denominator ledger

固定 odd prime
\[
p\nmid10,
\qquad p\mid d_0.
\]
`tail-rough-d0-allocation.md` 已证明前两 denominator 必须 equal valuation：
\[
\boxed{v_p(b_1)=v_p(b_2)=E.}
\tag{1.1}
\]
写
\[
j:=v_p(b_3),
\qquad c:=v_p(C_Q),
\qquad C_Q=Q/(b_1,b_2).
\]
则
\[
\boxed{v_p(Q)=E+c.}
\tag{1.2}
\]
而 `tail-rough-cq-excess.md` 给
\[
\boxed{x:=x_p=\max(c-j-\min(E,j),0).}
\tag{1.3}
\]
以下只需处理 `x>0`。

令
\[
M:=\max(E,j),
\qquad
\delta:=M-j=(E-j)_+.
\]
由 tail weight
\[
\kappa b_3=10^mQG,
\qquad v_p(G)=2E,
\]
得到
\[
\boxed{v_p(\kappa)=3E+c-j>2E.}
\tag{1.4}
\]
所以 `p` 为奇素数时
\[
\boxed{
 v_p(\kappa+G)
 =v_p(\kappa+2G)
 =2E.
}
\tag{1.5}

此外 `L|10^m`，故 `p` 不整除 `L`。若
\[
C_0=QL+2\tau,
\]
则 `v_p(QL)=E+c>j=v_p(\tau)`，于是
\[
\boxed{v_p(C_0)=j.}
\tag{1.6}

整数球面 lcm denominator记为 `q_lcm`。显然
\[
v_p(q_{\rm lcm})=M.
\tag{1.7}
\]
DD §17 的 exact simplification为
\[
\boxed{\mathcal M=q_{\rm lcm}C,}
\tag{1.8}
\]
故若
\[
t:=v_p(C),
\]
则
\[
\boxed{v_p(\mathcal M)=M+t.}
\tag{1.9}

最后
\[
\mathcal N_{12}=h_{12}^2N_0,
\qquad v_p(h_{12})=E,
\]
所以记
\[
\boxed{n_0:=v_p(N_0),}
\qquad
v_p(\mathcal N_{12})=2E+n_0.
\tag{1.10}

---

## 2. 反设 overflow 没有任何三 payer

反设
\[
\boxed{
x>t,\qquad x>n_0,\qquad x>(j-E)_+.}
\tag{2.1}
\]
我们将推出矛盾。

记
\[
A:=v_p(a),
\qquad r:=v_p(\mu),
\qquad s:=v_p(\nu),
\qquad g_0:=v_p(G_0).
\]
由
\[
\frac\mu\nu
=G(\mathcal R-r_3)
=\frac{GLa}{q_{\rm lcm}}
\]
得到
\[
\boxed{r-s=2E+A-M.}
\tag{2.2}
\]
由 primitive recovery
\[
10^mQG_0=2\kappa\mu\nu
\]
得到
\[
\boxed{g_0=2E-j+r+s.}
\tag{2.3}
\]
而 universal gap square-core
\[
LaG_0=2c_3\mu^2,
\qquad c_3=q_{\rm lcm}/b_3
\]
在当前 prime给
\[
\boxed{A+g_0=\delta+2r.}
\tag{2.4}
\]
这些关系与 `(2.2),(2.3)` 一致，并用于下面的 valuation case split。

---

## 3. gap quadratic 强制 `A=t+delta`

DD gap quadratic为
\[
\boxed{
C_0a^2-2\mathcal Ma+Q\frac{\mathcal S_{12}}L=0.
}
\tag{3.1}
\]
其中
\[
\mathcal S_{12}=y_1^2+y_2^2
=\left(\frac{q_{\rm lcm}}G\right)^2\mathcal N_{12}.
\]
因此三项 valuations为
\[
\boxed{
G_1=j+2A,
\qquad
G_2=M+t+A,
\qquad
G_3=c-E+2M+n_0.
}
\tag{3.2}
\]
三个整数和为零，所以最低 valuation至少出现两次。

### 3.1 `E>=j`

此时 `M=E`, `delta=E-j`，且 `(2.2)` 给
\[
r=E+A,\qquad s=0.
\]
由 `(2.3)`：
\[
g_0=3E-j+A.
\]
考察
\[
G_0\mid \mathcal N_{12}\nu^2-\mu^2.
\]
若 `A<delta`，则 `2v_p(mu)=2E+2A<g_0`。要使差仍被 `p^{g_0}` 整除，只可能两项先在更低层同 valuation，即
\[
n_0=2A.
\]
但 `(2.1)` 给 `x>2A`。此时
\[
G_3-G_1=E+c-j>0,
\]
故第三项严格更深，必须 `G_1=G_2`，即 `A=t+delta>=delta`，矛盾。

所以 `A>=delta`。此时若 `2E+n_0<g_0`，它不可能与 `2E+2A` 在同一较低层相消，因为
\[
2A\ge A+delta=g_0-2E.
\]
因此必有
\[
\boxed{n_0\ge A+delta.}
\tag{3.3}
\]
于是
\[
G_3-G_1
=E+c-j+n_0-2A
\ge x+2E-A>0,
\]
其中使用 `c=x+2j` 与 `x>n_0>=A`。同理
\[
G_3-G_2
=c+n_0-t-A
\ge x+E+j-t>0.
\]
所以第三项严格更深，必有
\[
\boxed{A=t+delta.}
\tag{3.4}

### 3.2 `j>E`

此时 `M=j`, `delta=0`，且 `(2.1)` 的第三个不等式给
\[
x>j-E.
\]
由于
\[
x=c-j-E,
\]
可得
\[
\boxed{c>2j.}
\tag{3.5}

由 `(2.2)`：
\[
r-s=2E+A-j.
\]
若右端非正，结合 `(2.3)` 的 `g_0>=0` 可知只能有 `A=0`（边界 `j=2E` 也同样给 `A=0`）。此时 `G_3>G_1=j`，最低层要求 `G_1=G_2`，故 `t=0=A`。

下面设右端为正。则
\[
r=2E+A-j,
\qquad s=0,
\qquad
 g_0=A+4E-2j.
\]
并且 `G_0|N_12 nu^2-mu^2` 迫使
\[
\boxed{n_0\ge A+2E-2j.}
\tag{3.6}
\]
（右端若为负则该不等式当然自动成立）。

若 `A<t`，则 `G_1<G_2`，最低层只能要求 `G_1=G_3`。这给
\[
n_0=2A-c+E-j.
\]
与 `(3.6)` 比较：
\[
A\ge c+E-j=x+2E,
\]
但 `A<t<x`，矛盾。

若 `A>t`，同理 `G_2<G_1`，只能 `G_2=G_3`，从而
\[
n_0=t+A-c+E-j.
\]
再与 `(3.6)` 比较得到
\[
t\ge c+E-j=x+2E,
\]
与 `t<x` 矛盾。

因此唯一可能为
\[
\boxed{A=t.}
\tag{3.7}

综上两种 denominator order统一得到
\[
\boxed{A=t+delta.}
\tag{Gap-baseline-lock}

---

## 4. 第三 gap term 必须严格更深

将 `A=t+delta` 代回 `(3.2)`：
\[
G_1=G_2=M+t+A.
\]
定义
\[
\boxed{
\Delta:=G_3-G_1
=c+j-E+n_0-2t.
}
\tag{4.1}

最低 valuation至少出现两次，所以 `Delta>=0`。事实上 `Delta=0` 也不可能。

若 `E>=j`，由 `(3.3)` 与 `A=t+delta`：
\[
n_0\ge t+2delta.
\]
于是
\[
\Delta
\ge x+E+j-t>0.
\]

若 `j>E` 且 `t=0`，显然 `Delta>0`。若 `t>0`，由 `(3.6)`：
\[
n_0\ge t+2E-2j.
\]
若反设 `Delta=0`，则
\[
t\ge c+E-j=x+2E,
\]
再次与 `t<x` 矛盾。

因此统一有
\[
\boxed{\Delta>0.}
\tag{Gap-extra}

gap quadratic因而给一条 genuine extra contact：
\[
\boxed{
v_p(C_0a-2\mathcal M)=M+t+\Delta.}
\tag{Gap-contact-general}

---

## 5. unified discriminant 给 derivative contact

统一判别核
\[
K_{C,Q}=G^2C^2-Q^2\mathcal N_{12}
\]
的两项 valuation分别为
\[
4E+2t,
\qquad
4E+2c+n_0.
\]
由 `c>x>t`，第二项严格更深，所以
\[
\boxed{v_p(K_{C,Q})=4E+2t.}
\tag{5.1}

unified discriminant为
\[
W^2
=\kappa\left(
\kappa K_{C,Q}-2GQ^2\mathcal N_{12}
\right).
\]
括号中两项 valuation差恰为
\[
\begin{aligned}
&\bigl(6E+2c+n_0\bigr)
-\bigl(7E+c-j+2t\bigr)\\
&=c+j-E+n_0-2t
=\Delta>0.
\end{aligned}
\]
故无 inner cancellation，并得到
\[
\boxed{v_p(W)=5E+c-j+t.}
\tag{W-general}

DD §18 有同一个判别根
\[
W=L\Xi,
\qquad
\Xi=\mathcal M-C_0a
\]
（绝对值不影响 valuation），且 `p` 不整除 `L`。另一方面
\[
v_p(\mathcal M)=M+t,
\]
而由 `Gap-baseline-lock`
\[
v_p(C_0a)=j+A=j+t+delta=M+t.
\]
所以 derivative extra depth为
\[
\boxed{
D_{\rm der}
:=v_p(\Xi)-(M+t)
=5E+c-j-M.
}
\tag{5.2}

---

## 6. derivative 与 gap 两 contacts 强迫 `D_der=0`

若
\[
D_{\rm der}>0,
\]
则 `(5.2)` 给
\[
\mathcal M\equiv C_0a
\pmod{p^{M+t+1}}.
\]
而 `(Gap-contact-general)` 与 `Delta>0` 给
\[
2\mathcal M\equiv C_0a
\pmod{p^{M+t+1}}.
\]
两式相减：
\[
p^{M+t+1}\mid\mathcal M.
\]
但 `(1.9)` 精确给
\[
v_p(\mathcal M)=M+t,
\]
矛盾。因此必须
\[
\boxed{D_{\rm der}=0.}
\tag{6.1}

现在解 `(5.2)`。

若 `E>=j`，则 `M=E`，所以
\[
D_{\rm der}=4E+c-j>0,
\]
与 `(6.1)` 矛盾。

若 `j>E`，则 `M=j`，故
\[
5E+c-2j=0,
\]
即
\[
\boxed{c=2j-5E.}
\tag{6.2}
\]
于是
\[
x=c-j-E=j-6E.
\]
但
\[
j-6E\le j-E=(j-E)_+,
\]
又与反设 `(2.1)` 的 `x>(j-E)_+` 矛盾。

所以反设不可能，证明
\[
\boxed{
 x_p\le
 \max\Bigl(v_p(C),v_p(N_0),v_p(R_3^{\rm den})\Bigr).
}
\]

---

## 7. 全局整数形式

对 `p|X_Q`，`tail-rough-d0-allocation.md` 已给 equal-prefix ledger，所以
\[
v_p(R_3^{\rm den})=(j-E)_+.
\]
`General-transfer-local` 因而说明
\[
v_p(X_Q)
\le
v_p\!\left(\operatorname{lcm}(C,N_0,R_3^{\rm den})\right).
\]
而 `X_Q` 只含 odd non-decimal primes，所以可安全抽掉 2、5 smooth part：
\[
\boxed{
X_Q\mid
\operatorname{lcm}\!\left(
\operatorname{core}_{10}(C),
\operatorname{core}_{10}(N_0),
\operatorname{core}_{10}(R_3^{\rm den})
\right).
}
\]

其中
\[
N_0=\frac{\mathcal N_{12}}{(b_1,b_2)^2}
\in\mathbf Z_{>0}.
\]
这严格推广了 `tail-source-cancellation-transfer.md` 的 baseline-free theorem；当
`E=j=0` 时，`R_3^{den}` 为 `p`-unit、`N_0=N_12`、`x_p=c`，恰恢复
\[
c\le\max(v_p(C),v_p(N_{12})).
\]

---

## 8. third payer 继续进入 projective/gap system

`R_3^{den}` 的 non-decimal prime `p^r` 使 `y_1,y_2` 同时至少含 `p^r`，因此
\[
\operatorname{core}_{10}(R_3^{den})\mid g_y:=\gcd(y_1,y_2).
\]
`core.md` 的 stereographic denominator formula
\[
v_p(Z_0)=\max(0,v_p(g_y)+\omega_p-v_p(a))
\]
立即给
\[
\boxed{
\operatorname{core}_{10}(R_3^{den})\mid Z_0a.
}
\tag{8.1}

所以最终有
\[
\boxed{
X_Q\mid
\operatorname{lcm}\!\left(
\operatorname{core}_{10}(C),
\operatorname{core}_{10}(N_0),
\operatorname{core}_{10}(Z_0a)
\right).
}
\tag{8.2}

这一步本身不宣称三个 payer 独立，也不把其高度机械相加；它只是 canonical
prime-power allocation。后续优化必须继续按 `lcm` / sheet allocation避免 double-count。

---

## 9. 对 post-tail branch reoptimization 的意义

`tail-rough-cq-excess.md` 已有第二次 Schmidt rough lower
\[
\log R_x+\log(g_*/v)
\ge S-\log X_Q-o(S),
\]
其中左边两项已真实进入 exact small factor。

本文把唯一 loss `X_Q` 完全改写为
\[
\boxed{
\text{prefix numerator rough }C
\ \cup\ 
\text{primitive Gaussian norm }N_0
\ \cup\ 
\text{projective/gap }Z_0a.
}
\]
因此 non-canonical side branches 的剩余困难不再是 denominator source cancellation
本身，而是这三类 numerator/projective payer能否同时承载正线性 rough height。

这正是下一步可与 carrier-circle / Gaussian angle / digit-shell height联立的接口。

---

## 10. 状态摘要

- **`已严格完成`**：`General-transfer-local/global/projective`。
- **`已严格完成`**：baseline-free `Source-transfer-local` 被本文严格包含为特例。
- **`结构压缩`**：post-tail second-Schmidt 的唯一 rough loss `X_Q` 被完全转移到
  `C / N_0 / Z_0a` 三 payer。
- **`待证`**：三 payer 的 independent excess height；完成 non-canonical dominant
  branch reoptimization，决定能否把全 DD explicit limsup升级到 `<=6`；absolute height / emptiness。

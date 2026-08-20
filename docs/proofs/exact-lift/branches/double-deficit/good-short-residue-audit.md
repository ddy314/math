# DD full-rational Good 的 short-residue audit 与 overflow 二次分层

> **依赖：** [`frontier.md`](frontier.md) 的 `CS` / `HS` / `R0-A12` / `Top-residue` / `Radius-resultant-collapse` / `Nc1-elim`，以及 [`good-axis-normalization.md`](good-axis-normalization.md)、[`good-excess-gcd-ladder.md`](good-excess-gcd-ladder.md)。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文继续只处理假想
> \[
> \frac{n_3}{S}\to 6.308883577618\ldots
> \]
> 的 full rational-contact Good 主质量，并删除总高度为 `o(S)` 的 coefficient / conjugate / Bad exceptional core。
>
> 本文做两件事：
>
> 1. 审计上一文件留下的“第二个 independent short residue”候选，证明三个最自然的局部候选分别退回 full rational carry、旧 `Delta_1` norm、旧 axis baseline，不能重复收费；
> 2. 将上一文件的 numerator overflow 再分成 **axis-reuse** 与 **deep overflow**，从而证明 `G_exc` 是 normalized numerator tail 中唯一真正面向尚未支付 `C_N` 深度的第一层。
>
> 本文仍不证明 `log G_exc=o(S)`，不关闭 full rational Good，也不关闭 DD。

---

## 1. 记号

令

\[
C:=C_L^{\rm main}.
\]

固定 main prime-power

\[
p^h\Vert C,
\qquad
n:=v_p(N_c).
\]

对 pure-excess 活跃 prime，沿用

\[
a:=v_p(A_0)=v_p(\alpha)=n+\varepsilon_p,
\qquad
\varepsilon_p>0.
\tag{1.1}
\]

并定义

\[
c_p:=\max(h-n,0),
\qquad
x_p:=\min(c_p,\varepsilon_p).
\tag{1.2}
\]

上一文件的 canonical objects 为

\[
G_{\rm ax}:=(C,N_c),
\qquad
C_N:=\frac{C}{G_{\rm ax}},
\tag{1.3}
\]

\[
A_N:=\frac{\alpha}{(\alpha,N_c)},
\tag{1.4}
\]

以及

\[
G_{\rm exc}:=(C_N,A_N).
\tag{1.5}
\]

逐 prime 有

\[
v_p(C_N)=c_p,
\qquad
v_p(A_N)=\varepsilon_p,
\qquad
v_p(G_{\rm exc})=x_p.
\tag{1.6}
\]

在真正的 `G_exc` target 上必有 `c_p>0`，故

\[
n<h.
\tag{1.7}
\]

---

## 2. `Top-residue` 在 main core 上不是第二条 residue

定义

\[
R_{\rm dec}
:=B10^dVA_{12}-Ua_3.
\tag{2.1}
\]

于是 exact identity 本身就是

\[
\boxed{
Ua_3+R_{\rm dec}
=B10^dVA_{12}.
}
\tag{2.2}
\]

由于

\[
C\mid V,
\]

立刻有

\[
\boxed{
Ua_3\equiv -R_{\rm dec}\pmod C.
}
\tag{2.3}
\]

因此当然也有

\[
Ua_3\equiv -R_{\rm dec}\pmod{G_{\rm exc}}.
\tag{2.4}
\]

另一方面 `Top-residue` 只是同一个 exact carry 在 decimal modulus 上的投影：

\[
Ua_3\equiv -R_{\rm dec}\pmod{10^d}.
\tag{2.5}
\]

所以若试图把 `(2.5)` 再投影到 `G_exc`，得到的不是第二个 p-adic residue；`(2.3)` 已经在完整 `C` 上给出了同一个 representative，而且它完全不需要 `alpha` repeat。

这可以用一个 exact compatibility identity写得更明显。由

\[
g_0B10^dA_{12}=UA_0+R_0,
\tag{2.6}
\]

以及

\[
g_0R_{\rm dec}=\Sigma R_0,
\qquad
\Sigma=V+2\cdot5^TU,
\tag{2.7}
\]

有

\[
\begin{aligned}
g_0(Ua_3+R_{\rm dec})
&=g_0B10^dVA_{12}\\
&=V(UA_0+R_0).
\end{aligned}
\tag{2.8}
\]

而使用

\[
g_0a_3=VA_0-2\cdot5^TR_0
\tag{2.9}
\]

展开左边也精确得到同一式。

所以：

\[
\boxed{
\text{`Top-residue` 的 main-}C\text{ 投影就是已有 }V\text{-contact，}
\text{不是 `G_exc` 的第二条 independent residue。}
}
\tag{Top-main-nogo}
\]

**状态：`失效/降级`。**

---

## 3. clean-source 的 square lift 确实存在

clean source 为

\[
\boxed{
VA_0=q_c^2L_{\rm clean}+5^TR_0.
}
\tag{CS'}
\]

由于 `G_exc|C|V`，又因为 `G_exc|A_N` 且 main target 上 `v_p(A_0)=n+epsilon_p>=x_p`，所以

\[
G_{\rm exc}\mid A_0.
\]

因此

\[
\boxed{
G_{\rm exc}^2
\mid
q_c^2L_{\rm clean}+5^TR_0.
}
\tag{Square-source}
\]

这是一条真实的 square-modulus congruence。注意这里的平方不是 Hensel 猜测，而只是来自两个独立整数因子

\[
G_{\rm exc}\mid V,
\qquad
G_{\rm exc}\mid A_0.
\]

在删除 clean-source exceptional core 后还可写成 unit synchronization

\[
q_c^2L_{\rm clean}
\equiv-5^TR_0
\pmod{G_{\rm exc}^2},
\tag{3.1}
\]

其中 target primes 不进入 `q_c L_clean R_0`。

看上去这很像新的 second-order short residue；下一节证明它仍然是旧 secondary norm 的投影。

---

## 4. `(Square-source)+HS` 精确退回 `Delta_1` norm

hidden square 为

\[
\boxed{
(C_LP_1)^2+P_0^2
=4\widetilde r^{\,2}5^TR_0L_{\rm clean},
}
\tag{HS}
\]

其中

\[
P_0=g_0a_2B\theta s.
\tag{4.1}
\]

因为 `G_exc|C_L`，模 `G_exc^2` 时 `(C_LP_1)^2` 消失。将 `(HS)` 乘以 `q_c^2`，再使用 `(Square-source)`，得到

\[
\boxed{
G_{\rm exc}^2
\mid
(q_cP_0)^2
+4\widetilde r^{\,2}5^{2T}R_0^2.
}
\tag{4.2}
\]

现在检查右边是不是新的 integer。

secondary Gaussian numerator 为

\[
\mathcal G_1
=g_0a_2\theta s\,2^{m-2}q_c
-i\widetilde rR_0\,5^{2T-m}
=\Pi\Delta_1,
\tag{4.3}
\]

而 terminal identity

\[
B=2^{m-1}5^{m-T}
\tag{4.4}
\]

给出

\[
\boxed{
2\,5^{m-T}\mathcal G_1
=q_cP_0-2i\widetilde r5^TR_0.
}
\tag{4.5}
\]

取范数：

\[
\boxed{
(q_cP_0)^2
+4\widetilde r^{\,2}5^{2T}R_0^2
=
4\,5^{2(m-T)}N(\mathcal G_1).
}
\tag{4.6}
\]

又因为

\[
\mathcal G_1=\Pi\Delta_1,
\qquad
N(\Pi)=C_L,
\]

故

\[
\boxed{
(q_cP_0)^2
+4\widetilde r^{\,2}5^{2T}R_0^2
=
4\,5^{2(m-T)}C_LN(\Delta_1).
}
\tag{Square-collapse}
\]

所以 `(4.2)` 并没有制造新的 second-order obstruction；它精确就是旧 `Delta_1` norm 的 smooth rescaling。

逐 target prime 也能直接看见这一点：

\[
v_p\bigl(N(\Delta_1)\bigr)=a=n+\varepsilon_p,
\]

于是 `(Square-collapse)` 右边的 p-depth 为

\[
h+a.
\]

而

\[
2x_p\le h+a
\]

只是

\[
x_p\le h,
\qquad
x_p\le a
\]

的直接和。因此 `G_exc^2` 的 divisibility 已完全被旧 `(C_L,N(Delta_1))` payer 覆盖。

结论：

\[
\boxed{
\text{clean-source square lift + hidden square}
\Longrightarrow
\text{旧 }\Delta_1\text{ norm，不能重复收费。}
}
\tag{Square-nogo}
\]

**状态：`失效/降级`。**

---

## 5. axis / radius-digital 的正交 companion 也只会回收 axis baseline

令

\[
Z_{\rm ax}:=C_*+iR_0,
\qquad
C_*:=\frac{g_0a_2B}{2},
\]

以及 radius digital carrier

\[
W:=a_2+iY,
\qquad
Y:=2\,10^dA_{12}.
\tag{5.1}
\]

考虑

\[
Z_{\rm ax}\overline W
=\mathcal D-i\mathcal I,
\tag{5.2}
\]

其中

\[
\boxed{
\mathcal I:=C_*Y-R_0a_2=a_2UA_0
}
\tag{5.3}
\]

正是 `Radius-resultant-collapse`，而正交坐标为

\[
\boxed{
\mathcal D:=C_*a_2+R_0Y.
}
\tag{5.4}
\]

利用 numerator reconstruction：

\[
10^dA_{12}
=\frac{UA_0+R_0}{g_0B},
\]

可得 exact identity

\[
\boxed{
g_0B\mathcal D
=2\bigl(EN_c+UR_0A_0\bigr),
}
\tag{Dot-exact}
\]

其中

\[
E=D_+D_-=C\cdot10^{o(S)}
\]

在 main primary depth 上等同于 `C`。

固定 pure-excess main prime，`a=n+epsilon_p`。由于 `g_0,B,U,R_0,a_2` 都是 p-units：

\[
v_p(\mathcal I)=n+\varepsilon_p.
\tag{5.5}
\]

`(Dot-exact)` 的两项深度分别为

\[
h+n,
\qquad
n+\varepsilon_p.
\]

若 `epsilon_p!=h`，较浅项唯一；若 `epsilon_p=h`，`mathcal D` 可能继续 cancellation，但 `mathcal I` 的深度恰为 `n+h`。因此无论 equal case 是否继续提升：

\[
\boxed{
v_p\bigl((\mathcal D,\mathcal I)\bigr)
=n+\min(h,\varepsilon_p).
}
\tag{Dot-gcd-depth}
\]

抽掉 common axis depth `n` 后，正交 companion 读取的只是

\[
\min(h,\varepsilon_p).
\]

定义 full-core first layer

\[
\boxed{
G_{\rm full}:=(C,A_N).
}
\tag{5.6}
\]

则

\[
\boxed{
v_p(G_{\rm full})=\min(h,\varepsilon_p).}
\tag{5.7}
\]

所以 `(Dot-gcd-depth)` 的 normalized content 恰好就是 `G_full`。

---

## 6. `G_full/G_exc` 全部由旧 axis baseline 支付

因为

\[
C_N=C/(C,N_c),
\]

有

\[
G_{\rm exc}=(C_N,A_N)\mid(C,A_N)=G_{\rm full}.
\]

定义

\[
\boxed{
G_{\rm reuse}
:=\frac{G_{\rm full}}{G_{\rm exc}}.
}
\tag{6.1}
\]

逐 prime：

\[
v_p(G_{\rm reuse})
=
\min(h,\varepsilon_p)
-
\min((h-n)_+,\varepsilon_p).
\tag{6.2}
\]

一个直接的 valuation inequality 给出

\[
\boxed{
0\le v_p(G_{\rm reuse})\le\min(h,n).
}
\tag{6.3}
\]

而

\[
v_p(G_{\rm ax})=v_p((C,N_c))=\min(h,n).
\]

故全局 main-primary 意义下：

\[
\boxed{
G_{\rm reuse}\mid G_{\rm ax}.
}
\tag{Axis-reuse}
\]

这说明把 `C_N` 换回完整 `C` 后多看到的 numerator overlap，没有产生任何新 unpaid mass；它全部落回已经被 `N_c` 占用的 axis baseline。

所以 axis/radius-digital 的 orthogonal coordinate虽然给出真实 gcd，但新增部分只是旧 payer：

\[
\boxed{
G_{\rm full}
=G_{\rm exc}\,G_{\rm reuse},
\qquad
G_{\rm reuse}\mid(C,N_c).
}
\tag{Full-vs-excess}
\]

**状态：新增结构 `已严格完成`；把 `G_reuse` 再计作 obstruction 属于 `失效/降级`。**

---

## 7. 上一文件的 `R_over` 可再拆成 axis-reuse + deep overflow

上一文件定义 `C_N^k` ladder 的 stable target tail `D_infty`，其 active main prime 上满足

\[
v_p(D_\infty)=\varepsilon_p.
\tag{7.1}
\]

并定义

\[
R_{\rm over}:=\frac{D_\infty}{G_{\rm exc}},
\]

所以

\[
v_p(R_{\rm over})
=\max(\varepsilon_p-c_p,0).
\tag{7.2}
\]

现在定义 full-core deep overflow

\[
\boxed{
R_{\rm deep}
:=\frac{D_\infty}{G_{\rm full}}.
}
\tag{7.3}
\]

因为 `c_p>0` 的 active support 上 `h>0`，有

\[
\boxed{
v_p(R_{\rm deep})
=\max(\varepsilon_p-h,0).
}
\tag{7.4}
\]

由定义立刻得到 exact factorization：

\[
\boxed{
R_{\rm over}
=G_{\rm reuse}\,R_{\rm deep}
}
\tag{Overflow-split}
\]

按 active main-primary part成立。

逐 prime 看得更清楚。令

\[
c=h-n>0.
\]

则：

\[
\boxed{
\begin{array}{c|c|c|c}
\varepsilon\le c
&G_{\rm exc}:\varepsilon
&G_{\rm reuse}:0
&R_{\rm deep}:0\\
 c<\varepsilon\le h
&G_{\rm exc}:c
&G_{\rm reuse}:\varepsilon-c
&R_{\rm deep}:0\\
 \varepsilon>h
&G_{\rm exc}:c
&G_{\rm reuse}:n
&R_{\rm deep}:\varepsilon-h.
\end{array}}
\tag{7.5}
\]

所以此前统称的 numerator overflow 实际包含两种完全不同的东西：

1. `G_reuse`：仍位于 full `C` 的可用 prime-power 深度以内，但这部分恰好被旧 axis baseline `(C,N_c)` 支付；
2. `R_deep`：已经超过整个 full `C` depth，属于同 support 上的 genuinely deep numerator tail，不能再拿来覆盖任何额外 `C`-depth。

因此：

\[
\boxed{
\text{normalized numerator tail 中唯一真正面向 unpaid }C_N
\text{ 第一层的对象就是 }G_{\rm exc}.}
\tag{Unique-unpaid-layer}
\]

这不是 `G_exc` 的小高度结论，但它封死了“从 overflow 再找一份可支付 `C_L` 的局部质量”的可能性。

---

## 8. nested gcd ladders

上一文件使用

\[
D_k^{(N)}:=\gcd(C_N^k,A_N).
\]

本文再定义 full-core ladder

\[
\boxed{
D_k^{(C)}:=\gcd(C^k,A_N).
}
\tag{8.1}
\]

逐 prime：

\[
v_p(D_k^{(C)})
=\min(kh,\varepsilon_p).
\tag{8.2}
\]

第一层为

\[
D_1^{(C)}=G_{\rm full}
=G_{\rm exc}G_{\rm reuse},
\]

而 stable layer 读取 `C` support 上完整 `epsilon_p`。在 `C_N` active support 上，两个 ladders 的 stable value一致，第一层之差恰为 `G_reuse`。

因此现在有 canonical nested picture：

\[
\boxed{
\begin{array}{c}
C_N\subset C,\\[1mm]
D_1^{(N)}=G_{\rm exc},\\[1mm]
D_1^{(C)}=G_{\rm exc}G_{\rm reuse},\\[1mm]
G_{\rm reuse}\mid(C,N_c),\\[1mm]
D_\infty/G_{\rm exc}
=G_{\rm reuse}R_{\rm deep}.
\end{array}}
\tag{Nested-ladders}
\]

这把 unpaid core、axis baseline 与 beyond-core overflow 三种深度完全分开。

---

## 9. 本轮 no-double-count 总结

当前最自然的三个“第二 short residue / second local payer”候选已经全部审计：

### 9.1 `Top-residue`

\[
Ua_3\equiv-R_{\rm dec}\pmod{G_{\rm exc}}
\]

只是

\[
C\mid Ua_3+R_{\rm dec}
\]

的弱化；full rational contact 已经提供它。

### 9.2 clean-source square lift

\[
G_{\rm exc}^2
\mid q_c^2L_{\rm clean}+5^TR_0
\]

与 hidden square联立后精确成为

\[
4\,5^{2(m-T)}C_LN(\Delta_1),
\]

即旧 secondary norm。

### 9.3 axis/radius-digital orthogonal companion

抽掉 common axis depth后读取

\[
G_{\rm full}=(C,A_N),
\]

但

\[
G_{\rm full}/G_{\rm exc}
\mid(C,N_c),
\]

新增部分全部是旧 axis payer。

因此：

\[
\boxed{
\text{full-rational Good 的现有 local Gaussian / carry / source algebra}
\text{没有再产生第二份 unpaid }G_{\rm exc}\text{ modulus。}
}
\tag{Local-closure-audit}
\]

这比“几条尝试失败”更强：它给出了失败对象各自精确退回的 canonical payer。

---

## 10. 更新后的 frontier

full rational Good 现在可以压成：

\[
\boxed{
\begin{gathered}
C_N=C/(C,N_c),\\
A_N=\alpha/(\alpha,N_c),\\
G_{\rm exc}=(C_N,A_N),\\
G_{\rm full}=(C,A_N)
=G_{\rm exc}G_{\rm reuse},\\
G_{\rm reuse}\mid(C,N_c),\\
R_{\rm over}=G_{\rm reuse}R_{\rm deep}.
\end{gathered}}
\tag{10.1}
\]

其中：

- `G_exc` 是唯一尚未被旧 axis payer覆盖、并且仍位于 unpaid denominator depth 内的 numerator contact；
- `G_reuse` 只是旧 `(C,N_c)` baseline 的重用；
- `R_deep` 已超过 full `C` prime-power depth，不能给 `C` closure 再支付一层；
- `Top-residue`、clean-source square lift、orthogonal digital companion 均已证明不能提供第二份独立 local modulus。

因此 full-rational Good 若继续推进，下一步不应再造同素数 local resultant。真正剩余的路线只剩两类：

1. 对已有 `QCRT + GCRT+` 唯一 `A_{12}` lift 做 **global digit-shell location / exclusion**；
2. 若该 location 仍只重构 carry/source algebra，则离开 full-rational local sheet，转向 genuine-Gaussian split-prime / digit-shell branch。

---

## 11. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`Top-residue` main projection no-go；`G_exc^2` clean-source square lift；其与 hidden square 精确退回 scaled `N(Delta_1)`；axis/radius digital orthogonal companion；`G_full/G_exc | (C,N_c)`；`R_over=G_reuse R_deep`；nested `C_N^k` / `C^k` gcd ladders。
- **`失效/降级`**：把 `Top-residue` 当 `G_exc` 第二 p-adic residue；把 clean-source square lift当第二个 local norm；把 `G_reuse` 当新的 unpaid modulus。
- **`待证`**：`log G_exc=o(S)` 或其它 strict digit-shell bound；`QCRT+GCRT+` 唯一 lift 的合法 digit-window exclusion；full rational Good emptiness；genuine-Gaussian closure；DD 全局空性与有效绝对高度界。

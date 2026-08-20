# DD post-tail rough payer 的 common / Gaussian-angular split

> **依赖：** [`tail-rough-general-transfer.md`](tail-rough-general-transfer.md)、
> `core.md` 的 prefix two-square norm 与 stereographic projective denominator。
>
> **严格状态：** `已严格完成（整个 `X_Q` odd rough support）`。
>
> `tail-rough-general-transfer.md` 已把第二次 Schmidt 剩余 overflow `X_Q`
> 压到三个 payer：
> \[
> C,\qquad
> N_0:=\frac{\mathcal N_{12}}{(b_1,b_2)^2},\qquad
> Z_0a.
> \]
> 本文继续把 `N_0` 中并不独立的 common numerator square剥掉。写
> \[
> b_i=h_{12}B_i,\qquad h_{12}=(b_1,b_2),\qquad(B_1,B_2)=1,
> \]
> \[
> X=a_1B_2,\qquad Y=a_2B_1,\qquad
> g_A=(X,Y),
> \]
> \[
> \boxed{
> N_{\rm ang}:=\frac{N_0}{g_A^2}
> =\left(\frac X{g_A}\right)^2+
> \left(\frac Y{g_A}\right)^2.
> }
> \]
> 则 `N_ang` 是 primitive sum of two squares；所以所有 odd prime divisor
> `p|N_ang` 都满足
> \[
> \boxed{p\equiv1\pmod4.}
> \]
> 更重要的是，在 `X_Q` 的 prime support上有
> \[
> v_p(g_A)\le v_p(C),
> \]
> 因而 general transfer 可全局加强成 product allocation
> \[
> \boxed{
> X_Q\mid
> \operatorname{core}_{10}(C)^2\,
> \operatorname{core}_{10}(N_{\rm ang})\,
> \operatorname{core}_{10}(Z_0a).
> }
> \tag{Angular-transfer}
> \]
> 于是 post-tail source loss中真正独立的 Gaussian payer只剩
> **split-prime angular norm** `N_ang`；`3 mod 4` rough primes不能藏在一个新的
> two-square norm pool里。

---

## 1. primitive prefix denominator blocks

令
\[
\boxed{h_{12}:=(b_1,b_2),}
\]
并写
\[
\boxed{b_1=h_{12}B_1,\qquad b_2=h_{12}B_2,}
\qquad(B_1,B_2)=1.
\tag{1.1}
\]
则 primitive denominator concat为
\[
\boxed{
C_Q=\frac Q{h_{12}}
=B_1 10^{m_2}+B_2.
}
\tag{1.2}

同时
\[
\begin{aligned}
N_0
&:=\frac{\mathcal N_{12}}{h_{12}^2}\\
&=(a_1B_2)^2+(a_2B_1)^2.
\end{aligned}
\tag{1.3}

沿用记号
\[
X:=a_1B_2,
\qquad
Y:=a_2B_1.
\]

---

## 2. `X_Q` prime不整除 primitive denominator blocks

固定
\[
p\mid X_Q.
\]
由 `tail-rough-cq-excess.md`：
\[
X_Q\mid C_Q,
\]
所以
\[
p\mid C_Q=B_1 10^{m_2}+B_2.
\tag{2.1}
\]
又 `p` 属于 `core_10(d_0)`，因此
\[
p\nmid10.
\]

若 `p|B_1`，由 `(2.1)` 会有 `p|B_2`，与 `(B_1,B_2)=1` 矛盾。
反向相同。因此
\[
\boxed{p\nmid B_1B_2.}
\tag{XQ-den-unit}

这一步非常关键：在真正需要支付的 `X_Q` support 上，`N_0` 的 common
`p`-depth只能来自 numerator `a_1,a_2`，不能再次来自 denominator baseline。

---

## 3. common numerator scale已被 `C` 支付

定义
\[
\boxed{g_A:=(X,Y)=(a_1B_2,a_2B_1).}
\tag{3.1}

固定 `p|X_Q`。由 `(XQ-den-unit)`：
\[
\boxed{
v_p(g_A)=\min(v_p(a_1),v_p(a_2)).
}
\tag{3.2}

DD numerator coefficient满足
\[
C=10^dA_{12},
\qquad
A_{12}=a_1 10^{n_2}+a_2.
\]
由于 `p` 不整除 10：
\[
v_p(C)=v_p(A_{12}).
\]
二项和总有
\[
v_p(A_{12})
\ge\min(v_p(a_1),v_p(a_2)).
\]
所以
\[
\boxed{
v_p(g_A)\le v_p(C)
\qquad(p\mid X_Q).
}
\tag{Common-paid}

因此 `N_0` 中平方 common factor `g_A^2` 的每一层，在 `X_Q` support 上都可由
`C^2` 支付。

---

## 4. 剩余 norm 是 genuine primitive Gaussian angle

定义
\[
\boxed{
N_{\rm ang}:=\frac{N_0}{g_A^2}.
}
\tag{4.1}
令
\[
X_0=X/g_A,
\qquad
Y_0=Y/g_A.
\]
则
\[
(X_0,Y_0)=1,
\]
且
\[
\boxed{N_{\rm ang}=X_0^2+Y_0^2.}
\tag{4.2}

固定 odd prime
\[
p\equiv3\pmod4.
\]
若 `p|N_ang`，则
\[
X_0^2+Y_0^2\equiv0\pmod p.
\]
因为 `-1` 在 `F_p` 中不是平方，唯一可能是
\[
p|X_0,\qquad p|Y_0,
\]
与 `(X_0,Y_0)=1` 矛盾。因此
\[
\boxed{
p\mid N_{\rm ang},\ p\text{ odd}
\Longrightarrow p\equiv1\pmod4.}
\tag{Angular-split}

特别地，对 `p=3 mod 4` 有 exact local valuation
\[
v_p(N_0)=2v_p(g_A)\le2v_p(C).
\tag{4.3}

所以 inert rough prime在 general transfer中若看似由 `N_0` 支付，其实只是
numerator common square的另一张投影，并不是独立 Gaussian payer。

---

## 5. 从 general transfer 得到 angular product allocation

`tail-rough-general-transfer.md` 对每个 `p|X_Q` 给
\[
 x_p\le
 \max\Bigl(
 v_p(C),
 v_p(N_0),
 v_p(R_3^{\rm den})
 \Bigr).
\tag{5.1}

写
\[
g_p:=v_p(g_A),
\qquad
\omega_p:=v_p(N_{\rm ang}),
\qquad
r_p:=v_p(R_3^{\rm den}).
\]
则
\[
v_p(N_0)=2g_p+\omega_p.
\]
由 `(Common-paid)`：
\[
g_p\le v_p(C)=:t_p.
\]
所以 `(5.1)` 安全推出
\[
\begin{aligned}
x_p
&\le\max(t_p,2g_p+\omega_p,r_p)\\
&\le2t_p+\omega_p+r_p.
\end{aligned}
\tag{5.2}

逐 `X_Q` prime相乘：
\[
\boxed{
X_Q
\mid
\operatorname{core}_{10}(C)^2\,
\operatorname{core}_{10}(N_{\rm ang})\,
\operatorname{core}_{10}(R_3^{\rm den}).
}
\tag{5.3}

这里使用 product 而非虚假的互素分配；三个 payer可以共享 prime，`(5.3)` 只是一条
逐 prime exponent inequality。

---

## 6. third-exclusive payer继续进入 projective/gap

`tail-rough-general-transfer.md` / 既有 projective ledger 已证明
\[
\boxed{
\operatorname{core}_{10}(R_3^{\rm den})\mid Z_0a.
}
\tag{6.1}

代入 `(5.3)`：
\[
\boxed{
X_Q
\mid
\operatorname{core}_{10}(C)^2\,
\operatorname{core}_{10}(N_{\rm ang})\,
\operatorname{core}_{10}(Z_0a).
}
\tag{Angular-transfer}

高度上安全得到
\[
\boxed{
\log X_Q
\le
2\log\operatorname{core}_{10}(C)
+\log\operatorname{core}_{10}(N_{\rm ang})
+\log\operatorname{core}_{10}(Z_0a).
}
\tag{6.2}

后续优化不能把这些高度视为独立而任意重复收费；本文的价值是**support 类型分离**：
`N_ang` 的所有 odd rough support均为 Gaussian split primes。

---

## 7. inert / split rough source 的 canonical interpretation

把 `X_Q` 的 odd support按模 4 分成
\[
X_Q=X_Q^{(+)}X_Q^{(-)},
\]
其中
\[
p|X_Q^{(+)}\Rightarrow p\equiv1\pmod4,
\]
\[
p|X_Q^{(-)}\Rightarrow p\equiv3\pmod4.
\]
（两个整数当然互素。）

对 inert part，由 `(4.3)` 与 general transfer可直接写成
\[
\boxed{
X_Q^{(-)}
\mid
\operatorname{lcm}\!\left(
\operatorname{core}_{10}(C)^2,
\operatorname{core}_{10}(R_3^{\rm den})
\right),
}
\tag{Inert-transfer}

进而
\[
\boxed{
X_Q^{(-)}
\mid
\operatorname{lcm}\!\left(
\operatorname{core}_{10}(C)^2,
\operatorname{core}_{10}(Z_0a)
\right).
}
\tag{Inert-projective}

所以 `3 mod 4` rough source完全不需要新的 Gaussian norm pool。

真正需要继续研究的只有 split part `X_Q^(+)`：当它没有被 `C` 或 `Z_0a`
支付时，`N_ang` 给出一个 primitive Gaussian orientation condition。

---

## 8. 当前 post-tail frontier

第二次 Schmidt的 hard loss已经经历：
\[
C_Q
\to X_Q
\to(C,N_0,Z_0a)
\to(C,N_{\rm ang},Z_0a),
\]
且最后一个新 norm满足
\[
\boxed{
\text{odd support}(N_{\rm ang})
\subset\{p:p\equiv1\pmod4\}.
}
\]

因此 side-branch reoptimization的下一步不再是 generic source cancellation：

1. inert rough mass只能进入 numerator coefficient `C` 或 projective/gap `Z_0a`；
2. 只有 split rough mass能进入 genuine Gaussian angular payer `N_ang`；
3. 应把 split `N_ang` 与 existing Gaussian carrier / determinant orientation 联立，而不是继续做普通 gcd height。

---

## 9. 状态摘要

- **`已严格完成`**：`XQ-den-unit`、`Common-paid`、`Angular-split`。
- **`已严格完成`**：`Angular-transfer` 与 `Inert-projective`。
- **`结构压缩`**：`N_0` 的独立 rough payer只剩 primitive split-Gaussian angle `N_ang`。
- **`待证`**：split `N_ang` 的 orientation / carrier charge；`C` 与 `Z_0a` 的 independent excess height；non-canonical dominant branch reoptimization；DD global explicit `<=6` / absolute height。

# DD third-exclusive / Gaussian-angular layers 的 sphere two-sheet absorption

> **依赖：** [`tail-rough-canonical-payer-decomposition.md`](tail-rough-canonical-payer-decomposition.md)、
> [`tail-rough-angular-source-transfer.md`](tail-rough-angular-source-transfer.md)、`core.md` 的
> integer sphere 与 stereographic denominator formula。
>
> **严格状态：** `已严格完成（`X_Q` support 中所有 third-exclusive primes）`。
>
> four-payer decomposition此前把同一 rough prime的 depth分为
> \[
> e_3+e_B+e_G+e_A.
> \]
> 本文证明：只要 third-exclusive capacity
> \[
> r:=v_p(R_3^{\rm den})>0,
> \]
> 同一个 prime上的 `e_3` 与 `e_A` 其实不需要两个 reader。integer sphere把
> third common scale与 primitive Gaussian angular depth锁在同一个二-sheet factorization里：
> \[
> \boxed{v_p(Z_0a)\ge r+\omega,}
> \qquad
> \omega:=v_p(N_{\rm ang}).
> \tag{Sphere-absorb}
> \]
> 而 canonical allocation在 `e_A>0` 时自动有
> \[
> e_3\le r,
> \qquad e_A\le\omega.
> \]
> 因此
> \[
> \boxed{p^{e_3+e_A}\mid Z_0a.}
> \tag{Layer-absorb-local}
> \]
>
> 结果：`X_A` 只有在 `R_3^{den}` 为 p-unit 的 primes上才需要继续作为独立
> numerator-Gaussian reader；所有与 third-exclusive denominator 共存的 angular depth都已
> 被 projective/gap sheet吸收。

---

## 1. third-exclusive prime 的 denominator / ghost ledger

固定
\[
p\mid X_Q,
\qquad p\nmid10,
\]
并假设
\[
\boxed{r:=v_p(R_3^{\rm den})>0.}
\tag{1.1}

`tail-rough-d0-allocation.md` 已给
\[
v_p(b_1)=v_p(b_2)=E.
\]
由 `R_3^{den}` 定义：
\[
\boxed{v_p(b_3)=j=E+r>E.}
\tag{1.2}
所以 `b_3` 是 p-adic unique maximum。

因为每个 `a_i/b_i` reduced：
\[
\boxed{p\nmid a_1a_2a_3.}
\tag{1.3}
整数球面 lcm denominator `q_lcm` 的 p-depth为 `j`，故
\[
y_i=a_iq_{\rm lcm}/b_i
\]
满足
\[
\boxed{
v_p(y_1)=v_p(y_2)=r,
\qquad v_p(y_3)=0.
}
\tag{1.4}

球面方程
\[
H^2=y_1^2+y_2^2+y_3^2
\]
模 `p` 于是给
\[
H^2\equiv y_3^2\not\equiv0\pmod p,
\]
所以
\[
\boxed{v_p(H)=0.}
\tag{1.5}

令
\[
g_y=(y_1,y_2).
\]
由 `(1.4)`：
\[
\boxed{v_p(g_y)=r.}
\tag{1.6}

---

## 2. primitive ghost angular depth就是 `N_ang`

写
\[
y_1=p^rY_1,
\qquad y_2=p^rY_2,
\]
其中 `Y_1,Y_2` 为 p-units。

另一方面
\[
b_i=p^EB_i\quad(i=1,2),
\qquad p\nmid B_1B_2.
\]
由于
\[
\frac{Y_1}{Y_2}
=rac{y_1}{y_2}
=rac{a_1b_2}{a_2b_1}
=rac{a_1B_2}{a_2B_1},
\]
存在 p-adic unit `lambda_p` 使
\[
(Y_1,Y_2)=\lambda_p(a_1B_2,a_2B_1)
\]
在 `Z_p^2` 中只差共同 unit scale。

而 `(1.3)` 与 `p∤B_1B_2` 给
\[
p\nmid(a_1,a_2),
\]
故在该 prime
\[
v_p(g_n)=0,
\qquad g_n=(a_1,a_2).
\]
所以
\[
N_{\rm ang}
=(\bar a_1B_2)^2+(\bar a_2B_1)^2
\]
的 p-depth正是 primitive ghost norm depth：
\[
\boxed{
\omega:=v_p(N_{\rm ang})
=v_p(Y_1^2+Y_2^2).
}
\tag{Angular=ghost}

因此
\[
\boxed{
v_p(y_1^2+y_2^2)=2r+\omega.}
\tag{2.1}

---

## 3. sphere factorization只有两个 sheets

integer sphere给
\[
(H-y_3)(H+y_3)=y_1^2+y_2^2.
\]
由 `(1.5)` 与 `v_p(y_3)=0`，`H,y_3` 都是 p-units。对 odd prime `p`：
\[
\boxed{
\min(v_p(H-y_3),v_p(H+y_3))=0,
}
\tag{3.1}
因为若两者同时被 p 整除，则 p同时整除 `2H,2y_3`，矛盾。

结合 `(2.1)`：
\[
\boxed{
\{v_p(H-y_3),v_p(H+y_3)\}
=\{0,2r+\omega\}.
}
\tag{Sphere-two-sheet}

DD gap normalization为
\[
H-y_3=La.
\]
当前 `p∤10` 且 `L|10^m`，故 `p∤L`。因此
\[
\boxed{v_p(a)=v_p(H-y_3).}
\tag{3.2}

所以两 sheets显式为：

### Gap sheet
\[
\boxed{
v_p(a)=2r+\omega,
\qquad v_p(H+y_3)=0.}
\tag{G}

### Complementary sheet
\[
\boxed{
v_p(a)=0,
\qquad v_p(H+y_3)=2r+\omega.}
\tag{C}

---

## 4. projective denominator 精确读取 complementary sheet

`core.md` 的 stereographic denominator为
\[
\boxed{
Z_0=\frac{H+y_3}{(g_y,H+y_3)}.
}
\tag{4.1}

在 Gap sheet，`H+y_3` 为 p-unit：
\[
v_p(Z_0)=0,
\]
故
\[
\boxed{v_p(Z_0a)=2r+\omega.}
\tag{4.2}

在 Complementary sheet：
\[
v_p(H+y_3)=2r+\omega,
\qquad v_p(g_y)=r,
\]
于是
\[
\boxed{v_p(Z_0)=r+\omega,}
\tag{4.3}
并因 `v_p(a)=0`：
\[
\boxed{v_p(Z_0a)=r+\omega.}
\tag{4.4}

两者统一：
\[
\boxed{
v_p(Z_0a)\ge r+\omega.
}
\tag{Sphere-absorb}

注意这比旧 general payer
\[
p^r\mid Z_0a
\]
多读出了整份 primitive Gaussian angular depth `omega`。

---

## 5. 吸收 canonical `e_3+e_A` layers

`tail-rough-canonical-payer-decomposition.md` 定义
\[
e_3=\min(x,r),
\]
然后顺序支付 `e_B,e_G,e_A`。
显然
\[
\boxed{e_3\le r.}
\tag{5.1}

当前 `r>0` 意味着 `j>E`；由 reducedness已在 §2 得到
\[
g=v_p(g_n)=0.
\tag{5.2}
因此 `e_G=0`。

若 `e_A=0`，直接由 `(Sphere-absorb)` 得
\[
e_3\le r\le v_p(Z_0a).
\]

下面设 `e_A>0`。sequential definition意味着
\[
x>r+t,
\]
其中 `t=v_p(C)`。general transfer在 `g=0` 时为
\[
x\le\max(t,\omega,r).
\]
因为 `x>t,r`，只能有
\[
\boxed{x\le\omega.}
\tag{5.3}
所以当然
\[
\boxed{e_A\le x\le\omega.}
\tag{5.4}

由 `(5.1),(5.4)`：
\[
e_3+e_A\le r+\omega.
\]
再用 `(Sphere-absorb)`：
\[
\boxed{
e_3+e_A\le v_p(Z_0a).
}
\tag{Layer-absorb-local}

---

## 6. global absorbed / residual angular split

把 `X_A` 按 `R_3^{den}` support分成 exponent layers：
\[
X_A=X_{A,3}X_{A,0},
\]
其中 `X_{A,3}` 收集所有 `r>0` primes上的 `e_A`，`X_{A,0}` 收集
`r=0` primes上的 `e_A`。

同样 `X_3` 全部只在 `r>0` support。逐 prime `(Layer-absorb-local)` 相乘得到
\[
\boxed{
X_3X_{A,3}\mid\operatorname{core}_{10}(Z_0a).
}
\tag{Global-absorb}

而 residual angular payer
\[
\boxed{X_{A,0}\mid\operatorname{core}_{10}(N_{\rm num})}
\tag{Residual-angular}
仍严格成立。

因此 four-payer decomposition可重写为
\[
\boxed{
X_Q
=(X_3X_{A,3})\,X_B\,X_G\,X_{A,0},
}
\]
其中第一括号已经是单一 projective/gap reader。

更重要的是：真正还需要独立 Gaussian orientation的 `X_{A,0}` 只支撑在
\[
\boxed{v_p(R_3^{\rm den})=0}
\]
的 primes上。也就是说 **third-exclusive denominator 与 Gaussian angular excess
不能形成两个独立 height pools**。

---

## 7. 当前 side-branch frontier

post-tail rough loss现在只剩三类真正不同机制：

1. **projective/gap combined layer**
   \[
   X_P:=X_3X_{A,3}\mid Z_0a;
   \]
2. **bottom/common numerator layers**
   \[
   X_B\mid C_{12}\mid R_{12},
   \qquad
   X_G\mid(a_1,a_2);
   \]
3. **residual split-Gaussian layer**
   \[
   X_{A,0}\mid N_{\rm num},
   \qquad R_3^{\rm den}\text{ is p-unit on its support}.
   \]

这比原 four-payer表少了一份可能重复计算的 `third + angular` height。
下一步应专门研究 residual `X_{A,0}` 与 bottom `X_B` / coefficient `A^circ` 的
cyclotomic overlap，以及 projective layer `X_P` 的 global height。

---

## 8. 状态摘要

- **`已严格完成`**：`Angular=ghost`、`Sphere-two-sheet`、`Sphere-absorb`。
- **`已严格完成`**：canonical `e_3+e_A` local absorption与 `Global-absorb`。
- **`结构压缩`**：third-exclusive denominator depth与同-prime Gaussian angular depth不再是独立 payer；residual Gaussian payer只存在于 `R_3^{den}`-unit support。
- **`待证`**：residual `X_{A,0}` / bottom `X_B` simultaneous height；projective layer `X_P` height；non-canonical dominant branch reoptimization；DD global explicit `<=6` / absolute height。

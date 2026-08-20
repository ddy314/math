# DD rough Gaussian payer 的 source-to-numerator orientation transfer

> **依赖：** [`tail-rough-gaussian-payer-split.md`](tail-rough-gaussian-payer-split.md)、
> [`tail-rough-general-transfer.md`](tail-rough-general-transfer.md)。
>
> **严格状态：** `已严格完成（整个 `X_Q` odd rough support）`。
>
> 上一文件把 post-tail rough loss写成
> \[
> X_Q\mid
> \operatorname{core}_{10}(C)^2
> \operatorname{core}_{10}(N_{\rm ang})
> \operatorname{core}_{10}(Z_0a),
> \]
> 其中 `N_ang` 已是 primitive split-Gaussian norm，但仍含 primitive denominator
> blocks `B_1,B_2`。本文利用 source cancellation本身把这份 orientation继续转移到
> 一个**纯 numerator norm**。
>
> 令
> \[
> g_n=(a_1,a_2),
> \qquad \bar a_i=a_i/g_n,
> \]
> 并定义
> \[
> \boxed{
> N_{\rm num}
> :=(\bar a_1 10^{m_2})^2+\bar a_2^2.
> }
> \]
> 则逐 `p|X_Q` 的 source/angular contact给同向 Gaussian transfer，最终得到
> \[
> \boxed{
> X_Q\mid
> \operatorname{core}_{10}(C)^2\,
> \operatorname{core}_{10}(N_{\rm num})\,
> \operatorname{core}_{10}(Z_0a).
> }
> \tag{Numerator-transfer}
> \]
> 此外若
> \[
> A^\circ:=A_{12}/g_n
> =\bar a_1 10^{n_2}+\bar a_2,
> \]
> 则 numerator coefficient与 Gaussian norm的 rough overlap受一个纯 decimal
> cyclotomic factor控制：
> \[
> \boxed{
> \operatorname{core}_{10}\gcd(A^\circ,N_{\rm num})
> \mid 10^{2|s_2|}+1,
> \qquad s_2=n_2-m_2.
> }
> \tag{Cyclotomic-overlap}
> \]
> 因而 `C` 与 `N_num` 也不是两个完全自由的 rough pools。

---

## 1. cross numerator common gcd 恰是 `(a_1,a_2)`

沿用
\[
b_i=h_{12}B_i,
\qquad(B_1,B_2)=1.
\]
定义
\[
X=a_1B_2,
\qquad Y=a_2B_1.
\]
上一文件写
\[
g_A=(X,Y).
\]
本文先证明
\[
\boxed{g_A=g_n:=(a_1,a_2).}
\tag{1.1}

显然 `g_n|g_A`。反过来，固定 prime `p|g_A`。若 `p` 不同时整除
`a_1,a_2`，则从
\[
p|a_1B_2,\qquad p|a_2B_1
\]
只能落入以下三种可能之一：

1. `p|B_1,B_2`，与 `(B_1,B_2)=1` 矛盾；
2. `p|a_1,B_1`，与 reducedness `(a_1,b_1)=1` 矛盾；
3. `p|a_2,B_2`，与 reducedness `(a_2,b_2)=1` 矛盾。

故必有 `p|min(a_1,a_2)`，并且逐 exponent同样成立。于是 `(1.1)` 成立。

因此
\[
\boxed{
N_{\rm ang}
=(\bar a_1B_2)^2+(\bar a_2B_1)^2,
}
\tag{1.2}
且两坐标互素。

---

## 2. source cancellation 给 exact Gaussian linear identity

primitive denominator concat为
\[
C_Q=B_1 10^{m_2}+B_2.
\]
定义两个 Gaussian integers
\[
\boxed{
Z_{\rm ang}:=\bar a_1B_2+i\bar a_2B_1,
}
\tag{2.1}
\]
\[
\boxed{
Z_{\rm num}:=-\bar a_1 10^{m_2}+i\bar a_2.
}
\tag{2.2}
\]
则直接展开得到
\[
\boxed{
Z_{\rm ang}-B_1Z_{\rm num}
=\bar a_1 C_Q.
}
\tag{Source-angular-linear}

其 norms分别为
\[
N(Z_{\rm ang})=N_{\rm ang},
\]
\[
\boxed{
N(Z_{\rm num})=N_{\rm num}
=(\bar a_1 10^{m_2})^2+\bar a_2^2.
}
\tag{2.3}

由于 `(\bar a_1,\bar a_2)=1`，`N_num` 的 odd non-decimal prime support同样全部是
`1 mod 4` split primes。

---

## 3. same-orientation transfer

固定
\[
p\mid X_Q.
\]
前一文件已证明
\[
p\nmid10B_1B_2.
\tag{3.1}
\]
写
\[
c=v_p(C_Q)>0,
\qquad
\omega=v_p(N_{\rm ang}).
\]
若 `omega=0` 本节无事可做。以下设 `omega>0`。

因为 `Z_ang` 的两个实坐标互素，`p|N_ang` 强迫
\[
p\equiv1\pmod4.
\]
在 `Z[i]` 中写
\[
p=\pi\bar\pi.
\]
primitive 性保证 `pi` 与 `bar pi` 不可能同时整除 `Z_ang`；故交换共轭后唯一有
\[
\boxed{\pi^\omega\mid Z_{\rm ang}.}
\tag{3.2}

另一方面 `p^c|C_Q` 作为 rational integer意味着
\[
\pi^c\bar\pi^c\mid C_Q.
\]
`(3.1)` 还给 `B_1` 为 `pi`-unit。把 `(Source-angular-linear)` 模
`pi^min(c,omega)` 观察：
\[
\boxed{
\pi^{\min(c,\omega)}\mid Z_{\rm num}.
}
\tag{Orientation-transfer}

因此取 norm：
\[
\boxed{
v_p(N_{\rm num})\ge\min(c,\omega).}
\tag{3.3}

这里保存的是同一 Gaussian orientation，而不只是 ordinary norm divisibility。

---

## 4. 消去 `N_ang` payer

固定 `p|X_Q`，记
\[
x=v_p(X_Q),
\quad t=v_p(C),
\quad g=v_p(g_n),
\quad \omega=v_p(N_{\rm ang}),
\quad r=v_p(R_3^{\rm den}),
\]
\[
u=v_p(N_{\rm num}).
\]
由上一文件：
\[
\boxed{x\le\max(t,2g+\omega,r),}
\tag{4.1}
\]
并且
\[
\boxed{g\le t.}
\tag{4.2}
又由 `x_p<=c` 显然有
\[
\boxed{x\le c.}
\tag{4.3}

我们证明
\[
\boxed{x\le2t+r+u.}
\tag{4.4}

若 `(4.1)` 的最大值由 `t` 或 `r` 支付，则显然成立。
只需考虑
\[
x\le2g+\omega.
\]
若已经 `x<=2t+r` 也结束。否则
\[
x>2t+r\ge2g,
\]
故
\[
\omega\ge x-2g>0.
\]
由 `(3.3),(4.3)`：
\[
u\ge\min(c,\omega)
\ge x-2g.
\]
所以
\[
2t+r+u
\ge2t+r+x-2g
\ge x.
\]
证明 `(4.4)`。

逐 prime相乘，并注意 `X_Q` 只含 odd non-decimal primes：
\[
\boxed{
X_Q\mid
\operatorname{core}_{10}(C)^2
\operatorname{core}_{10}(R_3^{\rm den})
\operatorname{core}_{10}(N_{\rm num}).
}
\tag{4.5}

再用
\[
\operatorname{core}_{10}(R_3^{\rm den})\mid Z_0a
\]
得到
\[
\boxed{
X_Q\mid
\operatorname{core}_{10}(C)^2
\operatorname{core}_{10}(N_{\rm num})
\operatorname{core}_{10}(Z_0a).
}
\tag{Numerator-transfer}

这样 denominator-dependent `N_ang` 已从最终 payer list中消失。

---

## 5. coefficient / numerator norm overlap只来自 `10^{2|s_2|}+1`

定义
\[
\boxed{
A^\circ:=A_{12}/g_n
=\bar a_1 10^{n_2}+\bar a_2.
}
\tag{5.1}
因为 `g_n|(a_1,a_2)`，这是整数；且
\[
(A^\circ,\bar a_1)=1
\tag{5.2}
\]
由 `(\bar a_1,\bar a_2)=1` 立即成立。

模 `A^circ` 有
\[
\bar a_2\equiv-\bar a_1 10^{n_2}.
\]
因此
\[
\begin{aligned}
N_{\rm num}
&=\bar a_1^2 10^{2m_2}+\bar a_2^2\\
&\equiv
\bar a_1^2
\left(10^{2m_2}+10^{2n_2}\right)
\pmod{A^\circ}.
\end{aligned}
\tag{5.3}

固定 `p\nmid10` 且
\[
p^r\mid(A^\circ,N_{\rm num}).
\]
由 `(5.2)` 有 `p\nmid\bar a_1`，所以 `(5.3)` 给
\[
p^r\mid10^{2m_2}+10^{2n_2}.
\]
抽掉 `10^{2min(m_2,n_2)}` 这个 `p`-unit：
\[
\boxed{
p^r\mid10^{2|n_2-m_2|}+1.}
\]
而
\[
s_2=n_2-m_2.
\]
逐 rough primes相乘得到
\[
\boxed{
\operatorname{core}_{10}\gcd(A^\circ,N_{\rm num})
\mid10^{2|s_2|}+1.
}
\tag{Cyclotomic-overlap}

这说明 numerator coefficient `C=10^dg_nA^circ` 与 `N_num` 的 primitive
concat部分若想同时支付同一 rough prime，其共同深度必须进入一个完全显式的 decimal
cyclotomic carrier。

---

## 6. 当前 side-branch payer list

post-tail rough loss现在有
\[
\boxed{
X_Q\mid
\operatorname{core}_{10}(C)^2
\operatorname{core}_{10}(N_{\rm num})
\operatorname{core}_{10}(Z_0a),
}
\]
其中：

1. `C=10^dA_12` 的 rough part来自普通 numerator prefix concat；
2. `N_num=(bar a_1 10^{m_2})^2+bar a_2^2` 是纯 numerator primitive Gaussian norm；
3. `Z_0a` 是 projective denominator / sphere gap；
4. `A^circ` 与 `N_num` 的 rough overlap被 `10^(2|s_2|)+1` 控制。

所以 non-canonical dominant branch reoptimization已经从 denominator source gcd问题转成
**三个 numerator/projective carriers及其 overlap**。特别地 split-Gaussian orientation现在有一个
不含 denominator blocks 的 canonical reader `Z_num`。

---

## 7. 状态摘要

- **`已严格完成`**：`g_A=g_n`、`Source-angular-linear`、same-orientation transfer。
- **`已严格完成`**：`Numerator-transfer`。
- **`已严格完成`**：`Cyclotomic-overlap`。
- **`结构压缩`**：独立 Gaussian payer已变成纯 numerator norm `N_num`，其与 primitive
  numerator concat的 rough overlap由 explicit `10^(2|s_2|)+1` 支付。
- **`待证`**：`N_num` 与 projective carrier的 simultaneous orientation；把三个 payer的
  height喂回 second-Schmidt inequality；完成 non-canonical dominant branch reoptimization；
  DD global explicit `<=6` / absolute height。

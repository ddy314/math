# A1 minimal diagonal: total resultant loss in contact Q-side lifting

> 日期：2026-08-20。依赖 `deep-contact-q-square-blocks.md`。

本文强化 contact Q-side block theorem：异常 prime contamination 的总损失不只在 support 上受控，而是其完整 `q`-primary gcd 因子本身被一个 `O(T)` resultant 控制。

状态：**已严格完成。**

---

## 1. `gcd(q,C)` 与线性 resultant 完全相同

`deep-contact-q-square-blocks.md` 已证明

\[
10C\equiv E_C\pmod Q,
\]

其中

\[
E_C=(10w-1)N_0+10(10w-1)(5-z)T-10z,
\]

且

\[
0<E_C<c_{z,w}T,
\qquad c_{z,w}\le1599.
\]

由于

\[
q\mid Q,
\qquad \gcd(10,q)=1,
\]

同余直接给出

\[
\boxed{
\gcd(q,C)=\gcd(q,E_C).}
\tag{1}

定义

\[
\boxed{g:=\gcd(q,C).}
\]

则

\[
\boxed{g<1599T.}
\tag{2}

按类型可用更小的 `369,779,1189,1599,189,399` 常数。

---

## 2. 每个 selected block 的 guaranteed exponent

仍记

\[
L_\pm=Db_1C\pm Z,
\]

以及

\[
L_-L_+=DNq^2v(DT^2v+2s).
\]

固定

\[
p^e\Vert q,
\qquad c=v_p(C).
\]

令

\[
x=v_p(L_-),
\qquad y=v_p(L_+).
\]

则

\[
x+y\ge2e.
\]

又

\[
\min(x,y)\le c
\]

因为 `gcd(L_-,L_+)|2Db1C`，而 `p` 与 `2Db1D` 互素。

同时当然

\[
\max(x,y)\ge e.
\]

所以若

\[
c_e:=\min(e,c)=v_p(g),
\]

则

\[
\boxed{
\max(x,y)\ge2e-c_e.}
\tag{3}

证明：

- 若 `c<e`，由 `x+y>=2e`、`min<=c` 得 `max>=2e-c`；
- 若 `c>=e`，则 `c_e=e`，而 `max>=e=2e-c_e`。

---

## 3. 全局 block partition

对每个 `p^e||q`，把 guaranteed block

\[
p^{2e-c_e}
\]

分配给实际承担较高 valuation 的 contact factor。

不同素数 blocks 两两互素，所以存在互素正整数 `Q_-`,`Q_+` 使

\[
\boxed{Q_-Q_+=\frac{q^2}{g},}
\tag{4}

并且

\[
\boxed{Q_-\mid L_-,
\qquad Q_+\mid L_+.}
\tag{5}

这里每个 `p` 的完整 guaranteed power `p^(2e-c_e)` whole-block 进入一边。

所以 contact square 对 Q-side supply 的统一结论可写成：

\[
\boxed{
\text{ideal }q^2\text{ square lifting}
\text{ 最多损失 }g=\gcd(q,C)<1599T.}
\tag{6}

---

## 4. regular / exceptional 情形作为特例

若 `g=1`，则

\[
Q_-Q_+=q^2,
\]

且每个 `p^e||q` 都以 `p^(2e)` 整块进入一边，恢复完全平方 whole-block partition。

一般情况下，所有异常损失的总乘积也只有 `g=O(T)`，而

\[
Q\asymp100T^2.
\]

因此在后续若能从 supply/four-factor 得到 `q` 的超线性下界，则 contact side 上必然出现一个显著的 lifted block；无需逐个追踪异常 prime support。

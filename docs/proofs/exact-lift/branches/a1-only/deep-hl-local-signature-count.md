# A1 minimal diagonal: moderate HL local-signature reduction

> 日期：2026-08-20。依赖 `deep-contact-sign-window.md`、`deep-double-2high-master.md`、`deep-2high-mod8-lock.md`、`deep-2high-mod5-lock.md` 与 `deep-moderate-block-partition.md`。

本文不宣称关闭 HL；目标是把后续 one-exponent divisor families 的 finite coefficient set 精确量化。只使用已经证明互相独立/安全的 local necessary conditions。

状态：**finite signature reduction 已严格审计。**

---

## 1. 输入 `r` windows

使用 contact-sign sharpened windows：

\[
\begin{array}{c|c}
(z,w)&r\\ \hline
(1,1)&973440\le r\le10885221\\
(1,2)&734410\le r\le8400003\\
(1,3)&529000\le r\le6236387\\
(1,4)&357210\le r\le4394372\\
(3,1)&519840\le r\le15204352\\
(3,2)&428490\le r\le13677244.
\end{array}
\]

HL 是 double-deep，所以

\[
v_5(r)=a_5\ge1.
\]

这些 windows 中全部 `5|r` 的整数合计

\[
\boxed{11,051,041}.
\]

---

## 2. finite local cells

对每个

\[
r=2^{a_2}5^{a_5}r_{10}
\]

枚举有限

\[
0\le\nu_5\le\lfloor(a_5-1)/2\rfloor,
\]

并令

\[
B=a_5-2\nu_5.
\]

只保留满足以下必要条件的 cell：

1. master parity `eta=-a_2` 与 prefix 2-adic branch兼容；
2. `deep-2high-mod8-lock.md`：
   \[
   r_{10}\equiv-5^{B+1}QN_2\pmod8;
   \]
3. `deep-2high-mod5-lock.md`：
   \[
   \left(\frac{wr_{10}N_5}{5}\right)=(-1)^A;
   \]
4. odd `w=1,3` 时，存在真正的 whole-block partition
   \[
   \alpha\beta=r_{10},\quad
   \alpha\equiv\beta\equiv3\pmod4.
   \]
   这等价于 `r_10` 至少含两个 residue `3 mod4` 的 prime-power blocks；
5. even `w` 时旧 orientation `alpha=1` 已提供一个安全 partition witness，所以这里只需前述 local locks。

prefix local compatibility 通过 `N_0 mod 16*5^6` 完整枚举。由于当前 `a_5<=10`，所以 `nu_5<=4`；`5^6` 足以精确分辨全部 `v_5(N_0)` cells。若 prefix norm `N` 在模 `5^6` 上仍为 0，则对其下一 5-adic unit class保留两种 Legendre 可能，故这是安全上集，不会误删真实 candidate。

---

## 3. 精确计数

最终 surviving `r` counts：

\[
\boxed{
\begin{array}{c|r}
(z,w)&\text{locally compatible }r\\ \hline
(1,1)&579692\\
(1,2)&383278\\
(1,3)&328609\\
(1,4)&201854\\
(3,1)&863426\\
(3,2)&662434
\end{array}}
\]

总计

\[
\boxed{3,019,293}.
\]

所以 local-independent filters 已把初始 `5|r` coefficient set

\[
11,051,041
\]

压缩约 72.7%。

---

## 4. 与 one-exponent family 的接口

每个 surviving finite signature 再选择允许的 `nu_5,B` 与 whole-block `(alpha,beta)`，随后 `deep-hl-one-exponent-divisor-family.md` 把全部 unbounded dependence 压到

\[
d=k+1-(B+\nu_5),
\]

以及

\[
2\beta u-\alpha v=5^d,
\]

\[
u\mid10^{2d+2Y-1}-w,
\qquad
v\mid10^{2d+2Y}-(10w-1).
\]

因此后续 proof search 不应再扫描 arbitrary `(r,k,A,B)`；应直接从这 3,019,293 个 finite `r` signatures 进入 single-exponent divisor analysis。

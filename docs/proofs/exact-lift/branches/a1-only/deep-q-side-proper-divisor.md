# A1 minimal diagonal: strict 2-deep Q-side proper-divisor cap

> 日期：2026-08-19。依赖 `deep-gap-unit-square.md`。

在 strict 2-adic low-side，已有

\[
h=qs,
\qquad q\mid Q,
\qquad s\equiv1\pmod4,
\]

以及 Q-side orientation

\[
w\text{ odd}\Longrightarrow q\equiv1\pmod4,
\]

\[
w\text{ even}\Longrightarrow q\equiv3\pmod4.
\]

本文把这个方向锁转成一个统一的 proper-divisor 与尺寸结论。

状态：**已严格完成。**

---

## 1. `Q mod 4`

minimal diagonal 中

\[
Q=10b_1+1,
\qquad b_1=10^{2k+1}-w.
\]

当前 `k>=26`，所以高十进制幂模 4 消失：

\[
b_1\equiv-w\pmod4.
\]

因此

\[
Q\equiv1-2w\pmod4.
\]

即

\[
\boxed{
Q\equiv3\pmod4\quad(w=1,3),
}
\tag{1}
\]

\[
\boxed{
Q\equiv1\pmod4\quad(w=2,4).
}
\tag{2}
\]

---

## 2. 补因子 `Q/q` 永远是 `3 mod 4`

### odd `w`

此时 `q≡1 mod4`，而 `Q≡3 mod4`。因为 `q` 为奇数，模 4 可逆，所以

\[
\boxed{Q/q\equiv3\pmod4.}
\tag{3}
\]

### even `w`

此时 `q≡3 mod4`，`Q≡1 mod4`。`3^{-1}≡3 mod4`，故仍有

\[
\boxed{Q/q\equiv3\pmod4.}
\tag{4}
\]

所以六类型统一：

\[
\boxed{
Q/q\equiv3\pmod4.
}
\tag{5}
\]

特别地

\[
\boxed{q<Q.}
\tag{6}
\]

strict 2-deep 中 Q-side 永远不能饱和地取完整 `Q`。

对 even `w` 还有 `q≡3 mod4`，因此

\[
\boxed{q>1.}
\tag{7}
\]

也就是说 even-`w` strict 2-deep 必须从 `Q` 中真正抽出一个非平凡 `3 mod 4` proper divisor。

---

## 3. 模 3 再给出统一尺寸 cap

令

\[
T=10^k.
\]

因为 `T≡1 mod3`，

\[
Q=100T^2-(10w-1)
\equiv1-(w-1)
=2-w
\pmod3.
\tag{8}
\]

所以

\[
3\mid Q
\iff w=2.
\tag{9}
\]

由 (5)，补因子 `Q/q` 是正整数且 `3 mod4`。

- 当 `w=2` 时，其最小可能值为 `3`，故
  \[
  \boxed{q\le Q/3.}
  \tag{10}
  \]
- 当 `w=1,3,4` 时，`3` 不整除 `Q`，因此 `Q/q` 不可能等于 `3`。正整数中下一个 `3 mod4` 的值是 `7`，故
  \[
  \boxed{q\le Q/7.}
  \tag{11}
  \]

于是统一尺寸表为

\[
\boxed{
\begin{array}{c|c}
w&q\text{ upper bound}\\ \hline
1&Q/7\\
2&Q/3\\
3&Q/7\\
4&Q/7
\end{array}}
\tag{12}
\]

---

## 4. 对 odd-prime supply 的新上界

完整 supply 为

\[
h=qs,
\]

其中 `s` 是 `b_1` 的 `1 mod4` whole-block selector。记全部可选 blocks 的乘积为 `B_+`，则

\[
s\le B_+.
\]

因此 strict 2-deep 中可统一加强原来的粗界 `h<=QB_+` 为

\[
\boxed{
h\le\frac{QB_+}{7}
\qquad(w=1,3,4),}
\tag{13}
\]

\[
\boxed{
h\le\frac{QB_+}{3}
\qquad(w=2).}
\tag{14}
\]

这个常数因子本身不足以关闭 deep sector，但它是 prefix-uniform 的真实供给损失，可直接塞回 finite exponent box / decade bound；更重要的是 even-`w` 还带有“`Q` 必须存在非平凡 `3 mod4` proper divisor”的结构条件。

---

## 5. 当前用途

后续 deep 证书不应再使用完整 `Q` 作为 Q-side 极值。strict 2-deep 可以直接使用 (12)-(14)。

对于 fixed `k`，若 `Q` 为素数，则 even-`w` 的 strict 2-deep 立即为空；更一般地，若 `Q` 没有 `3 mod4` proper divisor，则 even-`w` strict 2-deep 为空。

odd-`w` 虽允许 `q=1`，但 `q=Q` 已永久排除，并统一损失至少因子 `7`。
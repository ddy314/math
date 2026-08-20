# A2 `H_24` projective carrier 的 compact integer clearing 与 exact `5 mod 8` orientation

> **依赖：** `spontaneous-crt-pure-h24-projective.md`、deep-even primitive reduction、`spontaneous-crt-pure-h4-parity.md`。
>
> **严格状态：**`H_24` coefficient-singular component把 projective norm ratio `v=c/s^2` 送入 primitive irreducible degree-24 polynomial `P_24(v)`，且真实 endpoint `0<v<21/20` 上 `P_24` 无零点。本文识别 `v=Q^2N_0/(B^2K^2)`，将 `P_24` 清成仅 25 个 composite monomials 的 ordinary integer carrier。利用 deep-even 中 `B^2K^2` 比 `Q^2N_0` 至少多 16 层二进深度，证明最高次 `v^24` 项是唯一最低层，从而 `v_2(V_24)=48M+147`，positive primitive quotient恒为 `5 mod8`。所以高次 coefficient-singular branch本身不强迫 odd-inert surcharge；这与 `H_4` 的 `7 mod8` orientation严格不同。本文仍不排除 modular `H_24` roots，因此不关闭 A2。

---

## 1. the projective norm ratio is an exact prefix quotient

沿用

\[
x=B/N,
\qquad y=10A/N,
\qquad s=9+y=K/N,
\]

以及

\[
c=\frac{(x+2)^2(2025x^2+y^2)}{100x^2}.
\]

因为

\[
Q=B+2N,
\qquad
100N_0=2025B^2+100A^2,
\]
直接得到

\[
\boxed{
c=\frac{Q^2N_0}{B^2N^2}.}
\tag{1.1}
\]

再除以

\[
s^2=K^2/N^2,
\]
所以 `H_24` projective ratio精确为

\[
\boxed{
v:=\frac c{s^2}
=\frac{Q^2N_0}{B^2K^2}.}
\tag{1.2}
\]

定义两个 positive integer blocks

\[
\boxed{X:=Q^2N_0,\qquad Y:=B^2K^2.}
\tag{1.3}
\]

于是 `v=X/Y`。

---

## 2. compact ordinary integer carrier

前一文件定义 leading coefficient为正的 primitive polynomial

\[
\boxed{
\mathscr P_{24}(v)=\sum_{j=0}^{24}p_jv^j
\in\mathbf Z[v].}
\tag{2.1}
\]

定义 ordinary integer clearing

\[
\boxed{
\mathscr V_{24}
:=Y^{24}\mathscr P_{24}(X/Y)
=\sum_{j=0}^{24}p_jX^jY^{24-j}.}
\tag{2.2}
\]

所以尽管清回原 prefix variables后总次数很高，结构上只有 `25` 个 composite monomials。

任何 `H_24` coefficient-singular prime在 fixed denominator/content exceptions之外都必须满足

\[
\boxed{p\mid\mathscr V_{24}.}
\tag{2.3}
\]

---

## 3. exact binary depths of the two blocks

当前 deep-even normal form给

\[
Q=2^{M+1}Q_0,
\qquad Q_0\text{ odd},
\]
而 `A` 为奇数、`B/2` 为偶数，所以

\[
\boxed{N_0\text{ odd}.}
\tag{3.1}
\]

因此

\[
\boxed{v_2(X)=2M+2.}
\tag{3.2}
\]

另一方面

\[
\boxed{v_2(B)=M+m+t.}
\tag{3.3}
\]

又

\[
K=9N+10A,
\]
其中 `9N` 被 `4` 整除而 `10A\equiv2 mod4`，故

\[
\boxed{v_2(K)=1.}
\tag{3.4}
\]

所以

\[
\boxed{v_2(Y)=2M+2m+2t+2.}
\tag{3.5}
\]

两块深度差为

\[
\boxed{\delta:=v_2(Y)-v_2(X)=2m+2t\ge16,}
\tag{3.6}
\]
因为 dangerous branch中 `m>=5,t>=3`。

---

## 4. coefficient audit: the `X^24` term is uniquely shallowest

对 `P_24` 的 25 个 primitive integer coefficients做 exact `2`-adic audit。最高次 coefficient满足

\[
\boxed{v_2(p_{24})=99,}
\tag{4.1}
\]

并且

\[
\boxed{p_{24}/2^{99}\equiv5\pmod8.}
\tag{4.2}
\]

对其余 `j<24`，checker验证统一 inequality

\[
\boxed{
\min_{0\le j\le23}
\left(v_2(p_j)+(24-j)\cdot16\right)=109>99.}
\tag{4.3}
\]

实际 `delta>=16`，所以 (2.2) 中第 `j` 项相对于公共 `24v_2(X)` 的额外 depth为

\[
v_2(p_j)+(24-j)\delta.
\]

因此 `j=24` 是唯一最低层，不存在 first-layer cancellation：

\[
\boxed{
 v_2(\mathscr V_{24})
=24(2M+2)+99
=48M+147.}
\tag{4.4}

---

## 5. primitive orientation is `5 mod 8`

除以 (4.4) 的完整二进 content，模 `8` 只剩最高次项：

\[
\frac{\mathscr V_{24}}{2^{48M+147}}
\equiv
\frac{p_{24}}{2^{99}}
\left(
\frac{X}{2^{2M+2}}
\right)^{24}
\pmod8.
\]

`X/2^{2M+2}` 为奇数，而任意奇数的偶次平方满足

\[
\left(X/2^{2M+2}\right)^{24}\equiv1\pmod8.
\]

结合 (4.2)：

\[
\boxed{
\frac{\mathscr V_{24}}{2^{48M+147}}
\equiv5\pmod8.}
\tag{5.1}

---

## 6. positivity on the real endpoint

`spontaneous-crt-pure-h24-projective.md` 已证明

\[
\mathscr P_{24}(v)\ne0
\qquad(0<v<21/20),
\]
且 primitive normalization取 positive leading coefficient。checker同时验证

\[
\boxed{\mathscr P_{24}(0)=p_0>0.}
\tag{6.1}
\]

因为 `(0,21/20)` 内没有实根，`P_24` 在该连通区间不变号，所以

\[
\boxed{\mathscr P_{24}(v)>0
\qquad(0<v<21/20).}
\tag{6.2}
\]

又 `Y>0`，故真实 endpoint上

\[
\boxed{\mathscr V_{24}>0.}
\tag{6.3}

因此 (5.1) 是 positive primitive orientation。

---

## 7. contrast with the low component

两条 coefficient-singular escape现在有不同的 parity ledger：

\[
\boxed{
H_4:\quad
H_{V4}/2^{2M+6}\equiv7\pmod8,}
\tag{7.1}
\]

所以 low component自身强迫 odd-inert parity；而本文给

\[
\boxed{
H_{24}:\quad
\mathscr V_{24}/2^{48M+147}\equiv5\pmod8.}
\tag{7.2}

`5 mod8` 在模 `4` 下为 `1`，因此 `H_24` compact carrier的 total `3 mod4` prime valuation parity为偶数。

这不排除某枚 inert prime整除 `V_24`；它只说明 high coefficient-singular escape**没有像 `H_4` 那样自动再产生一份 odd-inert surcharge**。

---

## 8. updated frontier

coefficient-singular sector现在已完成结构与 parity 分流：

- `H_4`：short irreducible degree-4 prefix carrier，positive primitive `7 mod8`；
- `H_24`：25-term compact block carrier，positive primitive `5 mod8`，real endpoint singularity为空。

因此继续对 `H_24` 做 discriminant hunting收益已经很低。真正剩余的大块回到 generic `A_63!=0` pure-prefix carrier与 descendant common gcd 的 global depth/product allocation。

A2 仍为 `待证`。

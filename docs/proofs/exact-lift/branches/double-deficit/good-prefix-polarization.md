# DD full-rational Good 的 prefix polarization 与 leading-block CRT

> **依赖：** [`frontier.md`](frontier.md) 的 one-channel reduction、full-rational moving-core counting、`QCRT` / `GCRT+`，以及统一符号中
> \[
> A_{12}=a_1 10^{n_2}+a_2,
> \qquad S=m_1+m_2.
> \]
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文不新增 local Gaussian resultant；它把已有 `A12` 唯一 CRT lift 的十进制结构进一步定位到第一 numerator block `a1`。
>
> 核心结论是：full-rational frontier 已强迫前两块发生极端互补极化
> \[
> (n_1,m_1,n_2,m_2)
> =
> (S,0,0,S)+o(S),
> \]
> 因而 `A12` 的 suffix `a2` 只有 subexponential 位长。把 suffix 条件
> \[
> A_{12}\equiv a_2\pmod{10^{n_2}}
> \]
> 加到 `QCRT+GCRT+` 上只增加 `o(S)` 的 effective modulus，不能凭 modulus 高度本身把“至多一个”升级为 emptiness。另一方面，两条 CRT 可等价地下推为 `a1` 的 residue，联合有效 period 仍为
> \[
> 10^{1.617767155236\ldots S+o(S)},
> \]
> 而 `a1` 只有 `S+o(S)` 位，因此真正未决的 digit-shell 已缩成 **唯一 leading-block residue 的 Archimedean location**。

---

## 1. 已有 frontier 输入

沿用

\[
S=m_1+m_2.
\tag{1.1}
\]

one-channel reduction 已证明

\[
\boxed{m_2=S+o(S),}
\tag{1.2}
\]

并且

\[
b_2=C_L\cdot10^{o(S)}
\]

按 logarithmic height理解。

full-rational moving-core counting 的输入中已经使用并证明：

\[
\boxed{
\log a_2=o(S),
\qquad
\log g_0=o(S),
\qquad
\log R_0=o(S).
}
\tag{1.3}
\]

另一方面 second-order `A12` CRT 段给出

\[
\boxed{\log A_{12}=S+o(S).}
\tag{1.4}
\]

统一定义为

\[
\boxed{
A_{12}=a_1 10^{n_2}+a_2,
}
\tag{1.5}
\]

其中 `n_i` 是 `a_i` 的十进制位数。

---

## 2. 第二 numerator block 只有 `o(S)` 位

因为 `a_2` 是正整数且

\[
\log a_2=o(S),
\]

其十进制位数满足

\[
\boxed{n_2=o(S).}
\tag{2.1}
\]

这里 `log` 取何固定底数不影响 `o(S)` 结论。

所以 `A12` 的低位 suffix 模量只有

\[
\boxed{10^{n_2}=10^{o(S)}.}
\tag{2.2}
\]

这已经说明：任何仅仅把

\[
A_{12}\equiv a_2\pmod{10^{n_2}}
\]

当作第三个 CRT period 的方案，在 leading order 上只能增加 `o(S)` 模高。

---

## 3. 第一 numerator block 占满整个 `S` 尺度

由 `(1.5)`，`A12` 的十进制位数精确为

\[
n_1+n_2.
\]

因此

\[
\log A_{12}=n_1+n_2+O(1).
\tag{3.1}
\]

结合 `(1.4)` 与 `(2.1)`：

\[
\boxed{n_1=S+o(S).}
\tag{3.2}
\]

于是 numerator prefix 的全部正线性 digit entropy 都在第一块 `a1`，而 `a2` 只是 subexponential suffix。

---

## 4. denominator 两块发生完全相反的极化

由

\[
S=m_1+m_2
\]

与 `(1.2)`：

\[
\boxed{m_1=o(S).}
\tag{4.1}
\]

因此前两块的 digit-length profile 为

\[
\boxed{
\begin{array}{c|cc}
&\text{numerator digits}&\text{denominator digits}\\ \hline
1& S+o(S)&o(S)\\
2& o(S)&S+o(S).
\end{array}}
\tag{Block-polarization}
\]

等价地，对 surplus

\[
s_i=n_i-m_i
\]

有

\[
\boxed{
s_1=S+o(S),
\qquad
s_2=-S+o(S).
}
\tag{4.2}
\]

这与 DD 的 `d_3`-dominant surplus simplex 相容：前两块的正、负 surplus 在 leading order 精确互相抵消。

这个极化此前散落在 one-channel counting 的输入中；本文把它显式提升为后续 digit-shell 的规范 frontier 数据。

---

## 5. suffix CRT 不增加正线性 modulus surplus

已有两条 `A12` residues：

1. rational `QCRT`，有效 period
   \[
   M_Q=q_c^2/10^{o(S)},
   \qquad
   \log M_Q
   =0.617767155236\ldots S+o(S);
   \]
2. Gaussian `GCRT+` 对 rational integer `A12` 的有效 period
   \[
   M_G=E/10^{o(S)},
   \qquad
   \log M_G=S+o(S).
   \]

并且

\[
(M_Q,M_G)=10^{o(S)}.
\]

所以联合 effective period 为

\[
\boxed{
M_{QG}
=10^{1.617767155236\ldots S+o(S)}.
}
\tag{5.1}
\]

现在再加入 exact decimal suffix

\[
A_{12}\equiv a_2\pmod{10^{n_2}}.
\tag{5.2}
\]

main `M_QM_G` 与 `10` 的 overlap 已被 coefficient exceptional core 删除，而

\[
\log 10^{n_2}=o(S).
\]

故三者的联合 modulus 仍只有

\[
\boxed{
\log\operatorname{lcm}(M_Q,M_G,10^{n_2})
=1.617767155236\ldots S+o(S).
}
\tag{Suffix-no-surplus}
\]

因此 suffix condition 不能靠“再加一个 decimal modulus”产生新的正线性 surplus。

**状态：`失效/降级`**，若把 `10^{n_2}` 当成第三份 leading-order CRT height。

---

## 6. 两条 CRT 可直接下推到 `a1`

虽然 suffix 模高很小，它可以把变量从 `A12` 换成真正的 leading block `a1`。

由

\[
A_{12}=10^{n_2}a_1+a_2
\]

代入 `QCRT`：

\[
K_Q(10^{n_2}a_1+a_2)
\equiv R_Q
\pmod{M_Q},
\tag{6.1}
\]

其中

\[
K_Q=5^TB10^dV
\]

而 `R_Q=-Xa_3`；删除既有 coefficient exceptional core 后，`K_Q10^{n_2}` 是 `M_Q`-unit。因此得到唯一的

\[
\boxed{
a_1\equiv\rho_Q\pmod{M_Q}.}
\tag{Prefix-QCRT}
\]

同理，将

\[
A_{12}=10^{n_2}a_1+a_2
\]

代入 Gaussian congruence `GCRT+`：

\[
i g_0B10^de_0\overline\Gamma
(10^{n_2}a_1+a_2)
\equiv
\Sigma\overline K-M_+
\pmod\Gamma.
\tag{6.2}
\]

因为 `10` 与 main `Gamma` 互素，乘上 `10^{n_2}` 不改变从 rational integers 到 `Z[i]/(Gamma)` 的 kernel；删除 coefficient exceptional core 后得到

\[
\boxed{
a_1\equiv\rho_G\pmod{M_G}}
\tag{Prefix-GCRT}
\]

的 rational effective period 描述。

所以 `QCRT+GCRT+` 的联合 residue 可以完全转写为 `a1` 的 residue，且 period 高度不变：

\[
\boxed{
\log M_{\rm pref}
=1.617767155236\ldots S+o(S).
}
\tag{6.3}
\]

---

## 7. `a1` 也至多只有一个 candidate

由 `(3.2)`：

\[
\log a_1=S+o(S).
\]

而

\[
\log M_{\rm pref}
=1.617767155236\ldots S+o(S).
\]

因此 sufficiently large frontier 上

\[
0<a_1<M_{\rm pref}.
\]

所以 fixed terminal denominator-tail / axis data 与 fixed slow suffix `a2` 下：

\[
\boxed{\#\{a_1\}\le1.}
\tag{Prefix-unique}
\]

这与旧的 `#\{A12\}\le1` 在计数上等价，但语义更强：

\[
\boxed{
\text{唯一 CRT lift 的全部正线性十进制自由度都在 leading block }a_1.
}
\tag{Leading-block-location}
\]

`a2` 只改变该 residue 的 `10^{o(S)}` 级 slow-data fiber。

---

## 8. 第一 denominator block 也只能提供 `o(S)` 的附加筛选

由 `(4.1)`：

\[
\log b_1=o(S).
\]

因此 reducedness

\[
(a_1,b_1)=1
\]

以及任何只使用 `b1` 的 fixed congruence / divisor condition，最多贡献 `o(S)` 的 modulus / entropy。

所以在 leading order 上，不能期待用

- `A12` 的短 suffix `a2`；
- 第一 denominator block `b1`；
- 或它们的有限组合

给现有 `1.617767...S` CRT 再增加一份正线性 modulus surplus。

真正需要的是 **location**：证明 `(Prefix-QCRT)+(Prefix-GCRT)` 指定的唯一 residue `rho_pref` 不落在合法 `n1=S+o(S)` digit interval，或与一个来自大尺度对象的独立 sign / order / interval condition 冲突。

---

## 9. 更新后的 full-rational digit-shell target

经过本文，旧目标

\[
\text{“定位唯一 }A_{12}\text{ CRT lift”}
\]

可进一步收紧为

\[
\boxed{
\text{定位唯一 leading numerator block }a_1
\text{ 的 CRT residue。}
}
\tag{9.1}
\]

可用数据分成：

- **large-period arithmetic**：`QCRT + GCRT+`，总有效高度 `1.617767...S`；
- **slow suffix data**：`a2,n2,b1,m1,g0,R0,...=10^{o(S)}`；
- **合法 interval**：`a1` 必须是恰有 `n1=S+o(S)` 位的正整数；
- **reducedness**：`(a1,b1)=1`，但 `b1` 只有 subexponential height。

因此下一步若继续 full-rational Good，不应再增加 suffix modulus；应直接研究 `rho_pref` 的 Archimedean representative / sign / digit interval。

若该 representative 完整展开后再次只等价于 `R0-A12`、carry 或 clean-source reconstruction，则 full-rational digit-shell 的 algebraic elimination也已闭包，应转 genuine-Gaussian branch。

---

## 10. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`n2=o(S)`、`n1=S+o(S)`、`m1=o(S)`、`m2=S+o(S)` 的 block polarization；suffix modulus 只有 `10^{o(S)}`；`QCRT/GCRT+` 可无损下推为 `a1` residues；`a1` 至多一个 candidate。
- **`失效/降级`**：把 `A12≡a2 (mod 10^{n2})` 或 `b1`-based conditions 当作新的正线性 CRT height。
- **`待证`**：唯一 prefix residue 的合法 digit-window exclusion；`log G_exc=o(S)`；full rational Good emptiness；genuine-Gaussian closure；DD 全局空性。

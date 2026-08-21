# DD corrected hard source：decimal determinant + gap charged reduction

> **依赖：** [`dd-general-transfer-correction-2026-08-22.md`](dd-general-transfer-correction-2026-08-22.md)、[`tail-allocation-ledger.md`](tail-allocation-ledger.md) 中 `tail-rough-cq-excess`、`tail-rough-bottom-small-factor-charge`，以及 general exact gap factorization。
>
> **状态：** `已严格完成（corrected hard-source local reduction）`。
>
> 本文不恢复已撤销的 `General-transfer-local`。目标是直接处理 correction 后真正开放的 hard source sheet，并证明其中两层 source depth 可以分别由真实 decimal determinant 与 sphere gap 收费。最终 hard-specific 未收费 exponent 从 `x_p` 降为
> \[
> \boxed{h_p=(c-E-2j-2t)_+.}
> \]
> 因而任何仍有正 residual 的 prime 必须满足强阈值
> \[
> \boxed{c>E+2j+2t.}
> \]

---

## 1. corrected hard-sheet ledger

固定 odd non-decimal prime

\[
p\mid X_Q,
\qquad p\nmid10.
\]

`tail-rough-d0-allocation` 给 equal-prefix denominator depth

\[
\boxed{v_p(b_1)=v_p(b_2)=E.}
\]

写

\[
j:=v_p(b_3),
\qquad
C_Q:=Q/(b_1,b_2),
\qquad
c:=v_p(C_Q),
\]

以及

\[
t:=v_p(C),
\qquad C=10^dA_{12}.
\]

canonical unpaid source exponent为

\[
\boxed{x=x_p=c-j-\min(E,j)>0.}
\tag{1.1}
\]

这里已经进入 `x>0` support，所以不再写 positive part。

令

\[
M:=\max(E,j),
\qquad
\delta:=(E-j)_+.
\]

corrected hard sheet定义为

\[
\boxed{
x>t,
\qquad x>n_0,
\qquad x>(j-E)_+,}
\tag{Hard-H}
\]

其中 `n_0=v_p(N_0)`。

`dd-general-transfer-correction-2026-08-22.md` 已经在不使用错误 discriminant-root identification 的部分严格得到

\[
\boxed{v_p(a)=t+\delta.}
\tag{1.2}
\]

本文只使用 `(1.1)`、`(Hard-H)` 与 `(1.2)`，以及独立的 decimal determinant / small-factor identities。

---

## 2. hard prime 在真实 decimal determinant 中恰有 `j+t` 深度

定义 DD decimal determinant

\[
\boxed{
\mathcal E_{m dec}
:=b_3C-a_3Q
=b_3A_{12}10^d-a_3Q>0.
}
\tag{2.1}
\]

第一项 valuation为

\[
\boxed{v_p(b_3C)=j+t.}
\tag{2.2}
\]

另一方面

\[
v_p(Q)=E+c,
\]
所以

\[
v_p(a_3Q)=v_p(a_3)+E+c\ge E+c.
\tag{2.3}
\]

由 `(1.1)` 与 `x>t`：

\[
c=j+\min(E,j)+x
>j+\min(E,j)+t.
\]

因此

\[
E+c>j+t.
\tag{2.4}
\]

结合 `(2.3)`：

\[
v_p(a_3Q)>j+t.
\]

两个 determinant summands valuation严格不同，所以没有 cancellation：

\[
\boxed{
v_p(\mathcal E_{\rm dec})=j+t.}
\tag{Det-hard-depth}
\]

这一步完全不涉及 unified / gap discriminant roots。

---

## 3. charged-first local allocation

先把 hard source exponent交给 decimal determinant：

\[
\boxed{d_p:=\min(x,j+t).}
\tag{3.1}
\]

由 `(Det-hard-depth)`：

\[
\boxed{p^{d_p}\mid\mathcal E_{\rm dec}.}
\tag{3.2}
\]

余下

\[
x_1:=x-d_p=(x-j-t)_+.
\]

再把 gap 可用深度全部使用：

\[
\boxed{a_p^\sharp:=\min(x_1,t+\delta).}
\tag{3.3}
\]

由 `(1.2)`：

\[
\boxed{p^{a_p^\sharp}\mid a.}
\tag{3.4}
\]

最终定义 hard-specific residual

\[
\boxed{h_p:=x-d_p-a_p^\sharp.}
\tag{3.5}
\]

于是逐 prime 有 exact exponent identity

\[
\boxed{x=d_p+a_p^\sharp+h_p.}
\tag{3.6}

---

## 4. residual 的闭式

由 sequential definition：

\[
\begin{aligned}
h_p
&=(x-(j+t)-(t+\delta))_+\\
&=\boxed{(x-j-2t-\delta)_+.}
\end{aligned}
\tag{4.1}
\]

因为

\[
j+\delta=\max(E,j)=M,
\]
得到第一种规范形式

\[
\boxed{h_p=(x-M-2t)_+.}
\tag{Hard-residual-M}
\]

再使用

\[
x=c-j-\min(E,j)
\]
以及 elementary identity

\[
\min(E,j)+(E-j)_+=E,
\]
可得

\[
\begin{aligned}
x-j-2t-\delta
&=c-2j-\min(E,j)-\delta-2t\\
&=c-E-2j-2t.
\end{aligned}
\]

所以最终：

\[
\boxed{
h_p=(c-E-2j-2t)_+.}
\tag{Hard-residual-c}
\]

特别地

\[
\boxed{
h_p>0\Longrightarrow c>E+2j+2t.}
\tag{Ultra-hard-threshold}
\]

这说明 correction 后真正还未收费的 source cancellation必须远深于：

- 一份 prefix denominator baseline `E`；
- 两份 third denominator baseline `2j`；
- 两份 numerator coefficient depth `2t`。

最坏 endpoint仍可能是 baseline-free

\[
E=j=t=0,
\qquad h_p=c,
\]

所以本文还没有关闭 hard source sheet。

---

## 5. global hard factorization

令 `\mathcal H` 为满足 `(Hard-H)` 的 `X_Q` primes，并定义 hard source product

\[
\boxed{X_H:=\prod_{p\in\mathcal H}p^{x_p}.}
\tag{5.1}
\]

定义

\[
X_D:=\prod_{p\in\mathcal H}p^{d_p},
\qquad
X_a:=\prod_{p\in\mathcal H}p^{a_p^\sharp},
\qquad
X_R:=\prod_{p\in\mathcal H}p^{h_p}.
\tag{5.2}
\]

由 `(3.6)`：

\[
\boxed{X_H=X_DX_aX_R.}
\tag{Hard-product}
\]

且

\[
\boxed{X_D\mid\operatorname{core}_{10}(\mathcal E_{\rm dec}),}
\tag{5.3}
\]

\[
\boxed{X_a\mid\operatorname{core}_{10}(a).}
\tag{5.4}
\]

真正 hard-specific、尚无额外 reader 的对象只剩

\[
\boxed{
X_R
=\prod_{p\in\mathcal H}
 p^{(c_p-E_p-2j_p-2t_p)_+}.
}
\tag{5.5}

---

## 6. 两个 charged layers 都得到完整 `S` discount

`tail-rough-bottom-small-factor-charge` 的 universal identity为

\[
F_-Q(\kappa+G)
=\mathcal E_{\rm dec}\,\kappa(\kappa+2G),
\]

并已严格推出

\[
\boxed{\mathcal E_{\rm dec}G<F_-.}
\tag{6.1}
\]

因此由 `X_D|\mathcal E_dec`：

\[
\boxed{X_DG<F_-.}
\tag{Det-charge}
\]

而 general exact gap factorization已经给

\[
\boxed{aQ<F_-.}
\tag{6.2}
\]

故

\[
\boxed{X_aQ<F_-.}
\tag{Gap-charge-hard}
\]

又有 decimal size bounds

\[
10^{S-2}\le G<10^S,
\qquad
10^{S-1}\le Q<10^S.
\]

因此

\[
\boxed{
\log X_D<\log F_- -S+2,
}
\tag{6.3}
\]

\[
\boxed{
\log X_a<\log F_- -S+1.
}
\tag{6.4}

所以 correction 后的 hard source并非整份 `X_H` 都是自由 loss；其中 determinant 与 gap 两层各自具有真实的一份 prefix-height discount。

---

## 7. 与 whole `X_Q` 的安全接口

本文只对 hard support `\mathcal H` 作无条件结论。

令

\[
X_E:=X_Q/X_H.
\]

对 `p|X_E`，只是 `(Hard-H)` 的否定，因此 tautologically 有

\[
\boxed{
x_p\le\max(t_p,n_{0,p},(j_p-E_p)_+).}
\tag{7.1}
\]

这不恢复旧 `General-transfer-local`；旧 theorem声称 `(7.1)` 对**所有** `X_Q` primes 成立，而 corrected hard primes正是其反例候选。

因此当前 second-Schmidt loss应安全写成

\[
\boxed{X_Q=X_E\,X_D\,X_a\,X_R.}
\tag{7.2}
\]

其中：

- `X_D`：decimal determinant charged；
- `X_a`：gap charged；
- `X_E`：非-hard support，可按其显式 `C/N_0/R_3` reader继续审计；
- `X_R`：新的 ultra-hard source residual。

在没有重新完成 `X_E` 的独立 payer audit之前，不应把 `(6.3)--(6.4)` 直接宣称成 whole-`X_Q` triple bootstrap。

---

## 8. 下一 frontier

真正需要继续攻击的 local condition已经从 `(Hard-H)` 加强为

\[
\boxed{
\begin{gathered}
p\nmid10,
\qquad
p^c\mid C_Q,\\
c>E+2j+2t,\\
x=c-j-\min(E,j),\\
v_p(a)=t+(E-j)_+,\\
v_p(\mathcal E_{\rm dec})=j+t.
\end{gathered}}
\tag{Ultra-hard}
\]

最坏极限为

\[
\boxed{E=j=t=0,\qquad p^c\Vert C_Q,}
\]

此时 determinant 与 gap都是 p-units，全部 residual仍为 `c`。因此下一输入必须真正读取 primitive source cancellation本身，例如 full decimal concat、tail-root unit phase或新的 global fixed-target input；不能继续从同一 gap discriminant制造 derivative depth。

---

## 9. 状态摘要

- **`已严格完成`**：hard prime determinant depth `v_p(E_dec)=j+t`。
- **`已严格完成`**：hard source charged factorization `X_H=X_DX_aX_R`。
- **`已严格完成`**：`X_DG<F_-` 与 `X_aQ<F_-`，两层各带一份 `S` discount。
- **`结构压缩`**：hard-specific unresolved exponent降为
  \[
  h_p=(c-E-2j-2t)_+.
  \]
- **`待证`**：ultra-hard residual `X_R`；non-hard `X_E` 的 corrected payer audit；whole post-tail reoptimization；DD global explicit improvement / emptiness。

# A1-only: complete closure of the minimal diagonal

> 日期：2026-08-22。
>
> 范围：A1-only 的 minimal diagonal
> \[
> d=2,\qquad r=s=1,\qquad k=g\ge1.
> \]
>
> 本文只关闭 minimal diagonal；**不**宣称整个 A1-only 已关闭。

状态：**严格完成。**

---

## 1. theorem

\[
\boxed{
\forall k=g\ge1,
\qquad
\text{A1 minimal diagonal is empty}.
}
\tag{MD}
\]

证明由有限基区间与 `k>=32` 的 denominator-sector exhaustion 拼接而成。

---

## 2. fixed layers `1<=k<=31`

`finite-layer-certificates-ledger.md` 中的 exact finite certificates 已逐层关闭

\[
\boxed{1\le k=g\le31.}
\tag{1}
\]

这些证书枚举的是完整 minimal-diagonal necessary-state space：

- 完整合法 odd-prime supply；
- theorem-derived 完备 `2/5` exponent box；
- exact decade strip；
- near-integer / sharpened gap necessary condition；
- 必要时 rational-square sieve。

特别地 `k=31` 的 uniform certificate 对全部合法 supply 与完整 exponent box 检查旧的、更宽 one-sided gap window，得到零命中。因此 (1) 不是某个 denominator 子区的结论。

---

## 3. `k>=32` 的 denominator partition

minimal-diagonal normalized gap 写成既约形式

\[
\Gamma_k
=10^k(N_0-\rho)
=\frac{\gamma}{2^A5^B},
\qquad
A,B\ge0,
\qquad
(\gamma,10)=1.
\tag{2}
\]

因此 `k>=32` 的所有候选按 `(A,B)` 恰好落入以下四类之一：

\[
\boxed{
\begin{array}{c|c}
(A,B)&\text{sector}\\ \hline
(0,0)&\text{central denominator}\\
A>0,\ B=0&\text{single-2 deep}\\
A=0,\ B>0&\text{single-5 deep}\\
A>0,\ B>0&\text{double-deep}
\end{array}}
\tag{3}
\]

这四类两两不交并穷尽全部 normalized gap denominators。

---

## 4. central sector

`central-denominator-ledger.md` 的 `central-modular-exhaustion.md` 已严格证明

\[
\boxed{
A=B=0,\qquad k\ge26
\Longrightarrow\text{empty}.
}
\tag{4}
\]

其证书先把 central core 压到绝对有限 `t` 集合，再用 exact modular square conditions、`10^k mod p` 周期与 CRT compatibility 覆盖所有 `k>=26`，最终状态数为零。

所以对当前 `k>=32`，central sector 全空。

---

## 5. double-deep sector

此前 deep theory 已把全部 surviving double-deep states 统一到唯一的 2-high / 5-low master。

`deep-2high-decimal-height-collapse.md` 利用 exact decimal-height synchronization 证明该 master 的 2-side completion height严格高于允许的 5-side denominator capacity，并结合 master 的 bounded normalized parameter `xi` 得到矛盾。因此

\[
\boxed{
A>0,\ B>0,\qquad k\ge32
\Longrightarrow\text{empty}.
}
\tag{5}
\]

该 theorem 只依赖 double-deep master、global squarefree terminal 与 decimal-height synchronization，不依赖后来被撤回的 single-5 intermediate claims。

---

## 6. single-2 sector

`deep-single2-decimal-height-collapse.md` 中：

\[
v_2(L)=A+k>2k,
\]

而对两个 formal roots 均有

\[
d_5(x_\sigma)\le2k,
\qquad
v_5(L)\le k.
\]

故

\[
H_2>2k\ge H_5,
\]

违反 exact decimal-height synchronization `H2=H5`。因此

\[
\boxed{
A>0,\ B=0,\qquad k\ge32
\Longrightarrow\text{empty}.
}
\tag{6}

---

## 7. single-5 sector

corrected `deep-single5-decimal-height-collapse.md` 把 single-5 严格压成：

1. 唯一 low-edge cell；
2. 唯一 top edge `lambda_2=2k-1`。

### 7.1 low edge

`deep-single5-lowedge-small-supply-collapse.md` 定义 small supply remainders，并证明 selected odd supply `h=qs` 同时满足一个 `O(T^2)` 上界与 single-5 gap identity 给出的指数级下界，故

\[
\boxed{\text{single-5 low edge}=\varnothing.}
\tag{7}
\]

### 7.2 top edge

`deep-single5-topedge-finite-height.md` 先由 explicit phase shell 与 small-resultant argument 证明 top edge 只可能出现在 theorem-derived finite range

\[
32\le k\le77
\]

（各 type 还有更小的上界）。

随后：

- `deep-single5-topedge-geB-phase-certificate.md` 用两条 5-adic Hensel progressions与 exact `2^(3k)` phase-gap floor-sum certificate 证明
  \[
  v_5(N)\ge B\Longrightarrow\text{empty};
  \]
- `deep-single5-topedge-strictlow-phase-certificate.md` 利用 strict-low 的最弱 possible decimal height
  \[
  n\ge B+2k+1
  \]
  把 high-sign condition 与 phase-gap identity 合并成模 `2^(B+5k)` 的线性 modular-interval condition；对整个 decimal prefix interval做 exact floor-sum，全部 19,613 个 theorem-derived `(type,k,B)` 组合总命中数为零。因此
  \[
  v_5(N)<B\Longrightarrow\text{empty}.
  \]

两支互补，故

\[
\boxed{\text{single-5 top edge}=\varnothing.}
\tag{8}
\]

结合 (7)：

\[
\boxed{
A=0,\ B>0,\qquad k\ge32
\Longrightarrow\text{empty}.
}
\tag{9}

---

## 8. sector exhaustion

对 `k>=32`，(3) 的四个 exhaustive sectors 分别由 (4),(5),(6),(9) 排除。因此

\[
\boxed{k=g\ge32\Longrightarrow\text{minimal diagonal empty}.}
\tag{10}
\]

与 fixed-layer certificate (1) 拼接：

\[
\boxed{
\forall k=g\ge1,
\qquad
\text{minimal diagonal empty}.
}
\]

证毕。

---

## 9. proof-status boundary

本文不能被解释为整个 A1-only 的关闭。

minimal diagonal 是 A1 proof tree 中已经被单独隔离的一个子问题。full A1 仍包含 moving-prefix / non-minimal four-layer states；这些状态必须继续使用 global tail-weight `kappa`、safe common quotient、exact decimal recovery 与对应 coefficient-plane constraints 单独关闭。

因此当前严格状态是：

\[
\boxed{\text{minimal diagonal: CLOSED},}
\]

但

\[
\boxed{\text{A1-only overall: OPEN}.}
\]

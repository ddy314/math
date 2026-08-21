# DD ultra-hard baseline-free source：tail-root sign lock 与 exact collapse

> **依赖：** [`dd-general-transfer-correction-2026-08-22.md`](dd-general-transfer-correction-2026-08-22.md)、[`dd-hard-source-determinant-gap-charge-2026-08-22.md`](dd-hard-source-determinant-gap-charge-2026-08-22.md)、`good-genuine-ledger.md` 中 `Tail-root-original`，以及 DD gap normalization。
>
> **状态：** `已严格完成（no-go / sign lock）`。
>
> 上一文件把 corrected hard-specific residual压到
> \[
> h_p=(c-E-2j-2t)_+.
> \]
> 最坏端点仍是
> \[
> E=j=t=0,
> \qquad h_p=c.
> \]
> 本文审计 exact tail-root 是否能在这个 endpoint 提供第二份 independent contact。结论：它只固定一个全局 sign；surviving sign 下恒等式精确退回 gap/tail-weight algebra，没有新的 height。

---

## 1. baseline-free ultra-hard ledger

固定 odd prime

\[
p\nmid10b_1b_2b_3,
\qquad
p^c\Vert Q,
\qquad c>0,
\]

并进入 corrected ultra-hard endpoint

\[
\boxed{E=j=t=0,}
\tag{1.1}
\]

其中

\[
t=v_p(C),
\qquad C=10^dA_{12}.
\]

corrected hard-sheet formulas给

\[
\boxed{v_p(a)=0,}
\tag{1.2}
\]

\[
\boxed{v_p(\Xi)=0,}
\tag{1.3}
\]

以及由 tail weight local ledger

\[
\boxed{v_p(\kappa)=c,}
\tag{1.4}
\]

同时

\[
p\nmid q_{\rm lcm}GC_0C.
\tag{1.5}
\]

记

\[
q:=q_{\rm lcm}.
\]

---

## 2. corrected unified root

令 `\widetilde W>0` 为 unified discriminant root。correction 已证明

\[
\boxed{
\widetilde W
=\frac{\kappa G}{q}|\Xi|.
}
\tag{2.1}
\]

而 exact tail-root original identity为

\[
\boxed{
\mathscr T a_3
=\kappa G^2C
+\eta(\kappa+G)\widetilde W,
}
\tag{2.2}
\]

其中

\[
\mathscr T
=\frac{\kappa^2(\kappa+2G)}{10^m},
\qquad
\eta\in\{\pm1\}
\]

且 `eta` 是 global sign，不随 prime改变。

因为 `(1.3)` 保证 `Xi` 非零，令

\[
s:=\operatorname{sgn}(\Xi)\in\{\pm1\},
\qquad
\boxed{\varepsilon:=\eta s.}
\tag{2.3}
\]

于是

\[
\eta|\Xi|=\varepsilon\Xi.
\]

把 `(2.1)` 代入 `(2.2)` 并除以 `kappa G`：

\[
\boxed{
\frac{\mathscr T a_3}{\kappa G}
=GC+\varepsilon(\kappa+G)\frac{\Xi}{q}.
}
\tag{2.4}
\]

乘 `q`：

\[
\boxed{
\frac{q\mathscr T a_3}{\kappa G}
=qGC+\varepsilon(\kappa+G)\Xi.
}
\tag{Tail-normalized}

---

## 3. hyperbolic sign `epsilon=-1` 不可能

由 `(1.4)` 与 `p∤10G`：

\[
v_p(\mathscr T)
=2v_p(\kappa)+v_p(\kappa+2G)
=2c,
\]

因为 `kappa+2G` 是 p-unit。因此

\[
v_p\left(\frac{q\mathscr T a_3}{\kappa G}\right)
=c+v_p(a_3)
\ge c.
\tag{3.1}
\]

若

\[
\varepsilon=-1,
\]

则 `(Tail-normalized)` 右端模 `p^c` 为

\[
qGC-G\Xi,
\]
因为 `p^c|kappa`。而 DD gap exact identity

\[
\boxed{\Xi=qC-C_0a}
\tag{3.2}
\]
给

\[
qGC-G\Xi
=GC_0a.
\]

由 `(1.2),(1.5)`，这是 p-unit，与 `(3.1)` 矛盾。

因此任何 baseline-free ultra-hard prime都强迫

\[
\boxed{\varepsilon=+1.}
\tag{Sign-lock}

若存在至少一个这样的 prime，则 global product sign `eta*sgn(Xi)` 已被一次性固定。

---

## 4. surviving sign 下 tail-root 精确退回 gap algebra

取

\[
\varepsilon=+1.
\]

`(Tail-normalized)` 右端为

\[
qGC+(\kappa+G)\Xi.
\tag{4.1}
\]

使用 DD exact identities

\[
\boxed{\mathcal M=qC=QH+\tau a,}
\tag{4.2}
\]

\[
\boxed{\Xi=Qy_3-\tau a,}
\tag{4.3}
\]

以及 tail weight normalization

\[
\boxed{\kappa\tau=LQG,}
\tag{4.4}
\]

和

\[
La=H-y_3,
\tag{4.5}
\]

直接展开：

\[
\begin{aligned}
qGC+(\kappa+G)\Xi
&=G(QH+\tau a)+(\kappa+G)(Qy_3-\tau a)\\
&=Q\bigl(GH+(\kappa+G)y_3\bigr)-\kappa\tau a\\
&=Q\bigl(GH+(\kappa+G)y_3-GLa\bigr)\\
&=\boxed{Q(\kappa+2G)y_3.}
\end{aligned}
\tag{4.6}

另一方面，利用

\[
\mathscr T=\frac{\kappa^2(\kappa+2G)}{10^m}
\]
和 original tail weight

\[
\kappa b_3=10^mQG,
\]
有

\[
\begin{aligned}
\frac{q\mathscr T a_3}{\kappa G}
&=q\frac{\kappa(\kappa+2G)a_3}{10^mG}\\
&=q\frac{Q(\kappa+2G)a_3}{b_3}\\
&=\boxed{Q(\kappa+2G)y_3.}
\end{aligned}
\tag{4.7}

所以 surviving sign 下 `(Tail-normalized)` 的两边逐项化成完全相同的整数：

\[
\boxed{
\frac{q\mathscr T a_3}{\kappa G}
=qGC+(\kappa+G)\Xi
=Q(\kappa+2G)y_3.
}
\tag{Tail-collapse}

没有剩余 Hensel depth，也没有新的 short integer。

---

## 5. no-go 含义

baseline-free ultra-hard source的 tail-root unit phase只有两种作用：

1. 排除 `epsilon=-1`；
2. 对 `epsilon=+1` 精确恢复已有 gap/tail-weight identities。

因此不能把 tail-root equal-depth cancellation再作为 `p^c|Q` 之外的第二份 local modulus高度。

这与 discriminant-root correction 的方法边界一致：ultra-hard endpoint不能继续靠同一 gap / discriminant / tail-root algebra制造额外 source charge。

下一步需要 truly global input，例如：

- 对一批 baseline-free primitive source primes 的 simultaneous decimal concat作 fixed-target approximation；
- 使用与 `Q=b_1 10^{m_2}+b_2` 不同的第二个 global decimal relation；
- 或从全局 source product / digit-window 得到短 natural representative。

---

## 6. 状态摘要

- **`已严格完成`**：baseline-free ultra-hard `Sign-lock`。
- **`已严格完成`**：surviving sign 的 exact `Tail-collapse`。
- **`失效/降级`**：把 corrected tail-root equal-depth phase当作 ultra-hard source的独立 local height obstruction。
- **`待证`**：baseline-free ultra-hard source的 global decimal control；`X_R` height；whole post-tail reoptimization；DD global improvement / emptiness。

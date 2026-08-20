# A1 minimal diagonal: unified double-deep 2-high / 5-low master branch

> 日期：2026-08-20。依赖 `deep-moderate-three-pattern.md`、`deep-double-5high-collapse.md`、`deep-ll-modular-exhaustion.md`、`deep-extreme-height-collapse.md` 与 `deep-four-factor-frame.md`。

当前 double-deep 中：

- moderate LL 已全部关闭；
- moderate LH（5-high）已关闭；
- 5-extreme 已关闭；
- high-high 已由 balanced collapse 关闭。

所以所有尚存 double-deep candidate 实际都处于同一个方向：

\[
\boxed{2\text{-high}/5\text{-low}.}
\]

本文把此前分开的 moderate HL 与 2-extreme `E_2` 合并成一套单一正规形。

状态：**已严格完成。**

---

## 1. 统一偏移参数

写

\[
T=10^k,
\qquad D=2^A5^B,
\qquad N_0=2^{\nu_2}5^{\nu_5}n_0,
\]

其中 `(n_0,10)=1`。

在剩余 2-high branch 中定义

\[
\boxed{\eta:=A-(2k+3).}
\tag{1}

于是

\[
\boxed{A=2k+3+\eta.}
\tag{2}

- `eta<=0`：moderate HL；
- `eta=0`：moderate threshold；
- `eta>0`：原来的 2-extreme `E_2`。

所以 moderate / extreme 的区别只剩 `eta` 的符号。

---

## 2. 5-low 高度

记

\[
\boxed{Y:=B+\nu_5.}
\]

所有剩余 double-deep 都必须在 5-low：

\[
\boxed{Y<k+1.}
\tag{3}

定义

\[
\boxed{d:=k+1-Y>0.}
\tag{4}

---

## 3. `t` 的统一 valuation

universal factorization 给

\[
X_1=sa,
\qquad X_2=qb,
\qquad ab=t.
\]

2-high 时两项低 valuation 固定为

\[
v_2(X_1)=k+1,
\qquad
v_2(X_2)=k+2,
\]

而 5-low 给

\[
v_5(X_1)=v_5(X_2)=Y.
\]

所以

\[
\boxed{v_2(t)=2k+3,}
\qquad
\boxed{v_5(t)=2Y.}
\tag{5}

因此存在唯一正整数 `r_10`，满足

\[
\boxed{
t=2^{2k+3}5^{2Y}r_{10},
\qquad (r_{10},10)=1.}
\tag{6}

---

## 4. bounded renormalized gap 参数

令

\[
\boxed{\xi:=t/D.}
\]

由 (2)、(6)：

\[
\boxed{
\xi
=2^{-\eta}5^{B+2\nu_5}r_{10}.}
\tag{7}

universal real window 仍给

\[
\boxed{196000<\xi<15214000.}
\tag{8}

所以：

- `eta<=0` 时 `xi` 为整数，正是旧 moderate 参数 `r`；
- `eta>0` 时 `xi` 的 reduced denominator 是纯 `2^eta`，正是旧 `E_2` 的 pure-2 excess。

因此 moderate HL 与 2-extreme 在同一 `xi` 坐标中无缝连接。

---

## 5. factor quotients 统一

由 (5) 可写

\[
\boxed{
a=2^{k+1}5^Y\alpha,}
\]

\[
\boxed{
b=2^{k+2}5^Y\beta,}
\tag{9}

其中

\[
\boxed{\alpha\beta=r_{10},}
\qquad
\boxed{\gcd(\alpha,\beta)=1.}
\tag{10}

所以 `r_10` 的 prime-power blocks 仍必须 whole-block 分配给 `alpha` 或 `beta`。

---

## 6. stripped four-factor system

定义

\[
\boxed{c:=A+\nu_2-k-2
=k+1+\eta+\nu_2.}
\tag{11}

2-high 保证 `c>0`。

four-factor 两条线性式除去显式 2/5 powers 后统一变成

\[
\boxed{2\beta u-\alpha v=5^d,}
\tag{12}

\[
\boxed{\beta q-5\alpha s=2^c n_0.}
\tag{13}

其中

\[
su=b_1,
\qquad qv=Q,
\qquad qv-10su=1.
\]

取 adjugate：

\[
\boxed{2^{c+1}n_0u-5^dq=\alpha,}
\tag{14}

\[
\boxed{2^cn_0v-5^{d+1}s=\beta.}
\tag{15}

这四式对 moderate HL 与 `E_2` 完全相同；`eta` 只通过 `c` 出现。

---

## 7. 2-adic parity 也统一

因为

\[
A=2k+3+\eta,
\]

其 parity 只是 `1+eta mod 2`。

### even `w=2,4`

全部 2-deep strict-low 要求 `A` 为奇数，所以

\[
\boxed{\eta\equiv0\pmod2.}
\tag{16}

因此：

- moderate HL 的 `v_2(r)=-eta` 必为偶数；
- 2-extreme 的 excess `E=eta` 也必为偶数。

### odd `w=1,3`

若 `n_2=v_2(N)`，strict-low parity 为

\[
A\equiv1+n_2\pmod2.
\]

所以

\[
\boxed{\eta\equiv n_2\pmod2.}
\tag{17}

在 minimal diagonal 中 `n_2=0` 对应 `N_0` odd，`n_2=1` 对应 `N_0` even，因此 `eta` parity 同时锁定 prefix parity。

---

## 8. 当前意义

原来的分类

\[
HL_{\rm moderate}\cup E_2
\]

现在可直接替换成一个 master branch：

\[
\boxed{
\begin{gathered}
A=2k+3+\eta,\qquad Y=B+\nu_5<k+1,\\
t=2^{2k+3}5^{2Y}r_{10},\\
\xi=2^{-\eta}5^{B+2\nu_5}r_{10},\\
196000<\xi<15214000,\\
2\beta u-\alpha v=5^d,\\
\beta q-5\alpha s=2^c n_0,
\end{gathered}}
\]

其中

\[
c=k+1+\eta+\nu_2,
\qquad d=k+1-B-\nu_5.
\]

后续不再需要把 moderate HL 与 2-extreme 维护成两套算术证明；唯一差别只是 `eta<=0` 或 `eta>0`。

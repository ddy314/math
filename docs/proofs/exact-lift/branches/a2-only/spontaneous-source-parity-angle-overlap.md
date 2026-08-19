# A2 source parity reused prime 与 angle common support 的交集压缩

> **依赖：** `spontaneous-source-parity-reuse-depth.md`、`source-discriminant.md`、`spontaneous-residual-parity-doubling.md`。
>
> **严格状态：**odd/odd source parity reused prime 已知位于 `18K-55=0` 且为 noncentral/noncontent。若它还想同时进入 angle actual/conjugate 的 common gcd，angle parity ledger只允许 `A Q_0 c_Q` support。本文利用 `Q_0=c_Qq` 与 `gcd(D_W,q)|49`，以及 `7|q => v_7(D_W)=2`，删除 genuine odd-parity reuse 的 `q`-sheet。最终 angle overlap只剩 numerator-length gate `A=0, 162*10^M-55=0` 或 denominator sheet `c_Q=0`。本文不关闭这两张 sheet，因此不关闭 A2。

---

## 1. source reused setting

固定 genuine inert prime `r`，并假设它真正同时承担两份 source odd parity：

\[
v_r(\mathscr B_W)=v_r(\mathscr D_W)=e
\]
其中 `e` 为奇数。

此前已证明：

\[
\boxed{r\mid18K-55,}
\tag{1.1}
\]

\[
\boxed{r\nmid(2K-9)\omega.}
\tag{1.2}
\]

并且

\[
r^{(e+1)/2}\mid18K-55.
\]

---

## 2. angle common support

residual parity doubling 对 angle actual/conjugate pair证明：若 genuine non-`5` inert prime同时进入两张 angle primitive sheets，则

\[
\boxed{r\mid A Q_0c_Q.}
\tag{2.1}
\]

这里

\[
Q=2^{M+1}Q_0,
\]
而当前 denominator normal form同时有

\[
Q=2^{M+1}c_Qq.
\]

所以

\[
\boxed{Q_0=c_Qq.}
\tag{2.2}
\]

因此 (2.1) 表面上有三种来源：

\[
r\mid A,
\qquad
r\mid c_Q,
\qquad
r\mid q.
\]

下面删除 genuine reused parity的 `q`-sheet。

---

## 3. `q`-sheet cannot carry odd `D_W` parity away from `c_Q`

假设

\[
r\mid Q_0,
\qquad
r\nmid c_Q.
\]

由 (2.2)：

\[
\boxed{r\mid q.}
\tag{3.1}
\]

`source-discriminant.md` 已严格证明

\[
\boxed{\gcd(\mathscr D_W,q)\mid49.}
\tag{3.2}
\]

而当前 reused prime本来就满足 `r|D_W`，所以

\[
\boxed{r=7.}
\tag{3.3}
\]

但同一文件还给出精确 `7`-primary rule：

\[
\boxed{7\mid q\Longrightarrow v_7(\mathscr D_W)=2.}
\tag{3.4}
\]

右边为偶数，与 reused setting中

\[
v_r(\mathscr D_W)=e\text{ odd}
\]
矛盾。

所以：

\[
\boxed{
r\mid Q_0,\quad v_r(\mathscr D_W)\text{ odd}
\Longrightarrow
r\mid c_Q.}
\tag{3.5}
\]

`q` 本身不能作为 odd/odd source parity reuse与 angle common 的独立 support。

---

## 4. angle overlap reduces to `A c_Q`

综合 (2.1)、(3.5)：

\[
\boxed{
\text{odd/odd source reused }r\text{ 若同时 common to angle pair}
\Longrightarrow
r\mid A c_Q.}
\tag{4.1}
\]

所以只剩两张 sheet：

1. numerator sheet `r|A`；
2. denominator prefix sheet `r|c_Q`。

---

## 5. numerator sheet becomes a pure decimal-length gate

当前

\[
K=9N+10A,
\qquad
N=10^M.
\]

于是

\[
18K-55
=162N+180A-55.
\tag{5.1}
\]

若 reused prime同时满足

\[
r\mid18K-55,
\qquad
r\mid A,
\]
则 (5.1) 模 `r` 给

\[
\boxed{r\mid162N-55.}
\tag{5.2}
\]

即

\[
\boxed{r\mid162\cdot10^M-55.}
\tag{5.3}
\]

因此 numerator-angle overlap不再含 `A` 自由 residue，而被投影成纯 decimal exponent orbit。

定义

\[
\boxed{L_M:=162\cdot10^M-55.}
\tag{5.4}
\]

则 reused numerator-angle prime必须同时满足

\[
\boxed{r\mid L_M,\qquad r\mid\mathscr D_W.}
\tag{5.5}
\]

---

## 6. quadratic-character consequence on the length sheet

在 genuine source-discriminant root上 `r\nmid55z c_u`，由

\[
55z^2\equiv49c_u^2\pmod r
\]
可知

\[
\boxed{\left(\frac{55}{r}\right)=1.}
\tag{6.1}
\]

而 length gate给

\[
10^M\equiv55\cdot162^{-1}\pmod r.
\]
由于

\[
162=2\cdot9^2,
\]
取 Legendre symbol：

\[
\boxed{
\left(\frac{10}{r}\right)^M
=\left(\frac2r\right).}
\tag{6.2}
\]

因此：

- 若 `M` 为偶数，LHS 为 `1`，故
  \[
  \boxed{\left(\frac2r\right)=1.}
  \tag{6.3}
  \]
  对 `r=3 mod4` 即 `r=7 mod8`；
- 若 `M` 为奇数，利用 `(10/r)=(2/r)(5/r)`：
  \[
  \boxed{\left(\frac5r\right)=1.}
  \tag{6.4}
  \]
  再由 `(55/r)=1` 得
  \[
  \boxed{\left(\frac{11}{r}\right)=1.}
  \tag{6.5}
  \]

这些只是 residue-class filters，不单独排除 moving primes。

---

## 7. denominator sheet

另一种可能是

\[
\boxed{r\mid c_Q.}
\tag{7.1}
\]

本文不宣称 `D_W` 与 `c_Q` 全局互素；source ratio在清去公共 denominator scale后本来就不含 `c_Q`，因此这种 overlap不能靠 (3.2) 删除。

所以 angle reuse的 denominator exception必须被明确保留为 genuine frontier，而不能误归入已经删除的 `q`-sheet。

---

## 8. current overlap frontier

source odd-parity reused prime若还想让 angle actual/conjugate pair复用同一 prime，只剩

\[
\boxed{
\begin{array}{ll}
\text{numerator-length:}&r\mid A,\quad r\mid162\cdot10^M-55,\\
\text{denominator:}&r\mid c_Q.
\end{array}}
\tag{8.1}

generic `q`-support已经严格删除。

因此 source parity reuse与 angle parity reuse的共同 moving freedom被压成一个 pure decimal exponent orbit加一个 denominator-content exception。后续应分别攻击 `L_M` 的 multiplicative order / short-height，以及 `c_Q` 的既有有限/height constraints。

A2 仍为 `待证`。

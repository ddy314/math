# DD angular-only residual 的 coefficient-stripped normal form

> **依赖：** [`tail-rough-z0-angular-only-collapse.md`](tail-rough-z0-angular-only-collapse.md)、
> [`tail-rough-angular-source-transfer`](tail-allocation-ledger.md#source-tail-rough-angular-source-transfer)、
> [`tail-rough-bottom-angular-cyclotomic-split`](tail-allocation-ledger.md#source-tail-rough-bottom-angular-cyclotomic-split)。
>
> **严格状态：** `已严格完成（整个 angular-only residual support）`；末尾同时记录一条
> `失效/降级`：generic `gcd(N_ang,N_num)` 本身没有产生新的 independent height。
>
> 前一条 theorem 已把 post-tail 的唯一 independent rough layer 压到
> \[
> X_{Z,A}\mid N_{\rm ang},
> \qquad
> X_{Z,A}\mid N_{\rm num},
> \]
> 且其 odd support 全为 `1 mod 4` split primes。
>
> 本文利用此前尚未在该 bound 中完全使用的精确 coefficient identity
> \[
> \boxed{
> v_p(C)=v_p(g_n)+v_p(A^\circ)
> }
> \]
> 继续扣除 primitive numerator coefficient `A^circ` 的全部本地容量。最终得到：
> \[
> \boxed{
> X_{Z,A}\mid
> \operatorname{core}_{10}\!\left(
> \frac{N_{\rm ang}}{(N_{\rm ang},A^\circ)}
> \right),
> }
> \tag{Angular-after-coefficient}
> \]
> \[
> \boxed{
> X_{Z,A}\mid
> \operatorname{core}_{10}\!\left(
> \frac{N_{\rm num}}{(N_{\rm num},A^\circ)}
> \right),
> }
> \tag{Numerator-after-coefficient}
> \]
> 并且还同时有
> \[
> \boxed{
> X_{Z,A}\mid
> \operatorname{core}_{10}\!\left(
> \frac{C_Q}{(C_Q,A^\circ)}
> \right).
> }
> \tag{Source-after-coefficient}
> \]
>
> 更进一步，Gaussian linear identity 精确说明：在 `X_{Z,A}` support 上，前两个 normalized
> norm readers 的 common depth **恰好等于** normalized source/angular contact 的 common depth。
> 因此单独研究 `gcd(N_ang,N_num)` 不会再制造一份新的高度约束；下一步必须引入 coefficient
> circle / projective carrier 等第三个独立结构。

---

## 1. Sheet N 上 coefficient depth 的精确分解

固定
\[
p^{x}\Vert X_Q
\]
且处于 norm-overflow Sheet N：
\[
x>r+t.
\tag{1.1}
\]
沿用
\[
t=v_p(C),
\quad
r=v_p(R_3^{\rm den}),
\quad
g=v_p(g_n),
\quad
\omega=v_p(N_{\rm ang}),
\quad
\alpha=v_p(a).
\]

定义 primitive numerator concat
\[
A^\circ=A_{12}/g_n.
\]
记
\[
\boxed{q:=v_p(A^\circ).}
\tag{1.2}
\]
因为
\[
C=10^dA_{12}=10^dg_nA^\circ
\]
且 `p∤10`，有精确关系
\[
\boxed{t=g+q.}
\tag{Coefficient-depth}
\]

前一条 two-sheet theorem 在 Sheet N 给
\[
\boxed{
e_Z\le(2g+\omega-t-\alpha)_+.
}
\tag{1.3}
\]
代入 `t=g+q`：
\[
\boxed{
e_Z\le(g+\omega-q-\alpha)_+.
}
\tag{1.4}

angular-only collapse 定义
\[
c_p=(g-\alpha)_+,
\]
\[
e_{Z,C}=\min(e_Z,c_p),
\qquad
 e_{Z,A}=e_Z-e_{Z,C}.
\]
现在 `(1.4)` 会比此前只用 `t>=g` 得到更强的结论。

---

## 2. primitive coefficient depth 也被完整扣除

### Lemma 2.1

在 Sheet N 上，
\[
\boxed{
e_{Z,A}\le(\omega-q)_+.
}
\tag{2.1}

### Proof

若 `alpha<g`，则
\[
c_p=g-\alpha.
\]
当 `e_Z<=c_p` 时 `e_{Z,A}=0`。若 `e_Z>c_p`，由 `(1.4)`：
\[
\begin{aligned}
e_{Z,A}
&=e_Z-(g-\alpha)\\
&\le(g+\omega-q-\alpha)-(g-\alpha)\\
&=\omega-q.
\end{aligned}
\]

若 `alpha>=g`，则 `c_p=0`，所以 `e_{Z,A}=e_Z`。由 `(1.4)`：
\[
e_{Z,A}
\le(g+\omega-q-\alpha)_+
\le(\omega-q)_+.
\]
两种情况合并得到 `(2.1)`。∎

定义
\[
N_{\rm ang}^{(A)}
:=
\frac{N_{\rm ang}}{(N_{\rm ang},A^\circ)}.
\]
逐 prime 有
\[
v_p(N_{\rm ang}^{(A)})=(\omega-q)_+.
\]
所以由 `(2.1)`：
\[
\boxed{
X_{Z,A}\mid\operatorname{core}_{10}(N_{\rm ang}^{(A)}).
}
\tag{Angular-after-coefficient}

这说明最终 Gaussian residual 不只剥除了 common numerator 与 gap；primitive coefficient
`A^circ` 的同 prime depth也已经全部从 angular budget 中扣掉。

---

## 3. 同样扣除 pure-numerator orientation reader 中的 coefficient depth

记
\[
c:=v_p(C_Q),
\qquad
u:=v_p(N_{\rm num}).
\]
`X_Q|C_Q` 给
\[
\boxed{x\le c.}
\tag{3.1}

Sheet N 条件 `(1.1)` 与 `t=g+q` 给
\[
x>r+g+q>q,
\]
所以
\[
\boxed{c\ge x>q.}
\tag{3.2}

另一方面，除 `(2.1)` 外还有
\[
e_{Z,A}\le e_Z\le e_P=x-t=x-g-q<x-q+1.
\]
对整数 exponent，安全写成
\[
\boxed{e_{Z,A}\le x-q.}
\tag{3.3}

由 `(2.1),(3.3)`：若 `e_{Z,A}>0`，则 `q<omega` 且 `q<x`，并且
\[
\boxed{
e_{Z,A}\le\min(x,\omega)-q.
}
\tag{3.4}

same-orientation transfer 已证明
\[
\boxed{
\nu\ge\min(c,\omega).
}
\tag{3.5}
因为 `c>=x`：
\[
\nu
\ge\min(c,\omega)
\ge\min(x,\omega).
\]
结合 `(3.4)`：
\[
\boxed{q+e_{Z,A}\le\nu.}
\tag{3.6}

定义
\[
N_{\rm num}^{(A)}
:=
\frac{N_{\rm num}}{(N_{\rm num},A^\circ)}.
\]
其 p-depth 为
\[
v_p(N_{\rm num}^{(A)})=(\nu-q)_+.
\]
由 `(3.6)`：
\[
\boxed{
X_{Z,A}\mid\operatorname{core}_{10}(N_{\rm num}^{(A)}).
}
\tag{Numerator-after-coefficient}

所以 cyclotomic overlap
\[
(A^\circ,N_{\rm num})
\]
所能承担的 depth 已经在最终 residual 之前被完整扣掉；不能再把这部分 overlap 当成新的
angular height。

---

## 4. source concat 也可作同样的 coefficient-stripped reader

由 `(3.2)` 与 `(3.3)`：
\[
q+e_{Z,A}\le x\le c.
\]
定义
\[
C_Q^{(A)}
:=
\frac{C_Q}{(C_Q,A^\circ)}.
\]
则
\[
v_p(C_Q^{(A)})=(c-q)_+,
\]
从而
\[
\boxed{
X_{Z,A}\mid\operatorname{core}_{10}(C_Q^{(A)}).
}
\tag{Source-after-coefficient}

因此最终 residual 具有 coefficient-stripped triple-reader form：
\[
\boxed{
X_{Z,A}\mid
\operatorname{core}_{10}\gcd\!\left(
N_{\rm ang}^{(A)},
N_{\rm num}^{(A)},
C_Q^{(A)}
\right).
}
\tag{Coefficient-stripped-triple-reader}

这里三个 reader 都已经扣除了 `A^circ` 在同一 prime 上可贡献的 depth。

---

## 5. Gaussian linear identity 给 exact common-depth formula

接下来审计前两个 norm readers是否真的彼此独立。

沿用 Gaussian integers
\[
Z_{\rm ang}
=\bar a_1B_2+i\bar a_2B_1,
\]
\[
Z_{\rm num}
=-\bar a_1 10^{m_2}+i\bar a_2,
\]
以及 exact identity
\[
\boxed{
Z_{\rm ang}-B_1Z_{\rm num}
=\bar a_1C_Q.
}
\tag{5.1}

固定 `p|X_{Z,A}`。已有
\[
p\equiv1\pmod4.
\]
写
\[
p=\pi\bar\pi
\]
并选择 orientation 使
\[
\boxed{v_\pi(Z_{\rm ang})=\omega.}
\tag{5.2}

由于 `Z_ang` primitive，另一 orientation 的 valuation 为 0。`p|N_ang` 又强制
`p∤bar a_1 bar a_2`；而 `p|X_Q` 已知 `p∤B_1B_2`。所以 `bar a_1` 与 `B_1` 都是
`pi`-units。

rational integer `C_Q` 满足
\[
v_\pi(C_Q)=v_p(C_Q)=c.
\]
因此 `(5.1)` 给
\[
\boxed{
v_\pi(Z_{\rm ang}-B_1Z_{\rm num})=c.
}
\tag{5.3}

记
\[
u_\pi:=v_\pi(Z_{\rm num}).
\]
由非阿基米德 valuation：

- 若 `omega<c`，要让两个项之差的 valuation 从 `omega` 提升到 `c`，必须
  \[
  u_\pi=\omega;
  \]
- 若 `omega>c`，第一项 valuation 已超过 `c`，故第二项必须恰有
  \[
  u_\pi=c;
  \]
- 若 `omega=c`，必须有
  \[
  u_\pi\ge c.
  \]

`Z_num` 同样 primitive；一旦 `u_pi>0`，其 conjugate orientation valuation 为 0，因此
\[
\nu=v_p(N_{\rm num})=u_\pi.
\]
于是三种情况统一成 exact formula
\[
\boxed{
\min(\omega,\nu)=\min(\omega,c).
}
\tag{Exact-double-reader-depth}

---

## 6. coefficient-stripped 后仍精确退回 source contact

对 `p|X_{Z,A}`，由 §§2--4 已有
\[
q<\omega,
\qquad
q<c,
\qquad
q<\nu.
\]
所以从 `Exact-double-reader-depth`：
\[
\begin{aligned}
\min(\omega-q,\nu-q)
&=\min(\omega,\nu)-q\\
&=\min(\omega,c)-q\\
&=\min(\omega-q,c-q).
\end{aligned}
\]
也就是
\[
\boxed{
 v_p\gcd(N_{\rm ang}^{(A)},N_{\rm num}^{(A)})
 =
 v_p\gcd(N_{\rm ang}^{(A)},C_Q^{(A)})
}
\tag{Normalized-double-reader-no-go}
\]
对每个 `p|X_{Z,A}` 成立。

因此 `N_ang` 与 `N_num` 的共同 rough depth，在 coefficient-stripped 后仍然没有产生新的
independent p-adic capacity；它精确等价于同一 Gaussian orientation 下的 source concat contact。

这是一条 **no-go**，但它很有用：它阻止后续错误地把
\[
\gcd(N_{\rm ang},N_{\rm num})
\]
当成一份独立于 `C_Q` 的新 gcd height。

---

## 7. cyclotomic overlap 在最终 residual 中的位置

已有
\[
\operatorname{core}_{10}\gcd(A^\circ,N_{\rm num})
\mid10^{2|s_2|}+1.
\]
本文的 `Numerator-after-coefficient` 已经把
\[
(A^\circ,N_{\rm num})
\]
的全部 p-depth从 final residual 中减掉。因此 cyclotomic carrier 的正确用途是支付被剥除的
coefficient/angular overlap；它不会自动继续压缩 coefficient-stripped residual。

换言之，下一步若仍想获得线性高度收益，需要一个与 source-angular identity `(5.1)`
真正独立的结构，例如：

- coefficient circle 的 homogeneous equation；
- primitive projective denominator valuation formula 与该 angular orientation 的交叉；
- 其它能同时读取 `C_Q^(A)` 与 Gaussian orientation、且不由 `(5.1)` 恒等推出的 carrier。

---

## 8. verification scope

有限 algebra audit：

```bash
uv run python scripts/exact-lift/double-deficit/research-checks/tail-allocation/check_dd_tail_rough_angular_coefficient_stripped.py
```

脚本核对：

- `t=g+q` 下 `e_ZA <= (omega-q)_+`；
- `e_ZA <= (nu-q)_+` 与 `e_ZA <= (c-q)_+`；
- Gaussian valuation 三种 case 对 `Exact-double-reader-depth` 与
  `Normalized-double-reader-no-go` 的一致性。

脚本只是 bounded consistency audit；严格结论来自 §§1--6 的代数与 valuation proof。

---

## 9. 状态摘要

- **`已严格完成`**：`Coefficient-depth`、`Angular-after-coefficient`。
- **`已严格完成`**：`Numerator-after-coefficient`、`Source-after-coefficient`。
- **`已严格完成`**：`Coefficient-stripped-triple-reader`。
- **`已严格完成`**：`Exact-double-reader-depth`。
- **`失效/降级`**：generic `gcd(N_ang,N_num)` height；在 final residual support 上它精确退回
  normalized source/angular contact。
- **`待证`**：把 coefficient-stripped source/angular contact 与一个独立 coefficient-circle /
  projective carrier 联立；non-canonical dominant-state reoptimization；DD global explicit `<=6` /
  absolute height。

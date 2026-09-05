# DD `Z_0` frontier：charged-first reallocation 与 source-at-infinity split

> **依赖：** [`tail-allocation-ledger.md`](tail-allocation-ledger.md) 中
> `tail-rough-general-transfer`、`tail-rough-angular-source-transfer`、
> `tail-rough-projective-bottom-two-payer`、`tail-rough-bottom-small-factor-charge`、
> `tail-rough-z0-only-frontier`；以及 [`core.md`](core.md) 的 stereographic denominator exact formula。
>
> **严格状态：** `已严格完成（整个 post-tail X_Q odd rough support 的 valuation reallocation）`。
>
> 本文不宣称 DD 全局闭合。它把旧 `Z_0-only` hard object 再缩一层：先把每个 rough source prime
> 能由 numerator coefficient 与 sphere gap 支付的深度全部收费，剩余 projective depth具有一个
> exact local formula，并可进一步分解为 third-exclusive、prefix-common 与 Gaussian-at-infinity
> 三个显式 reader。最终未收费部分不再需要把 `Z_0` 当作匿名 height pool。

---

## 1. local ledger

固定

\[
p^x\Vert X_Q,
\qquad p\nmid10.
\]

沿用现有记号

\[
E=v_p(b_1)=v_p(b_2),
\qquad
j=v_p(b_3),
\qquad
r=(j-E)_+,
\]

\[
g=v_p(a_1,a_2),
\qquad
\omega=v_p(N_{\rm ang}),
\qquad
t=v_p(C)=v_p(A_{12}),
\]

以及

\[
\alpha=v_p(a).
\]

因为 `p` 为 non-decimal rough prime 且 `L\mid10^m`，有 `p\nmid L`，故
`alpha=v_p(La)`。

现有结果给出

\[
\boxed{g\le t,}
\tag{1.1}
\]

\[
\boxed{x\le \max(t,2g+\omega,r),}
\tag{1.2}
\]

以及 projective denominator exact valuation

\[
\boxed{
v_p(Z_0)=\max(0,r+g+\omega-\alpha).
}
\tag{1.3}

若写

\[
h_{12}=(b_1,b_2),
\qquad
C_Q=Q/h_{12},
\qquad
c=v_p(C_Q),
\]

则 `x<=c`，并且

\[
v_p(Q)=E+c.
\tag{1.4}
\]

---

## 2. charged-first exponent split

旧 two-payer decomposition先按 mechanism 分 `e_3,e_B,e_G,e_A`，再把 projective payer
拆成 `a/Z_0`。这对结构分类自然，但不保证先最大化两个已经有整份 `S` discount 的 reader。

现在改用 charged-first 顺序：

\[
\boxed{b:=\min(x,t),}
\tag{2.1}
\]

\[
\boxed{a_*:=\min(x-b,\alpha),}
\tag{2.2}
\]

\[
\boxed{z:=x-b-a_*=(x-t-\alpha)_+.}
\tag{2.3}

这里 `b` 先交给 bottom reader，`a_*` 再交给 gap reader，只有 `z` 留给真正未收费部分。

### 2.1 bottom depth 确实可全部这样分配

令

\[
C_{12}=(A_{12},Q).
\]

由 `(1.4)` 与 `x<=c`：

\[
v_p(C_{12})
=\min(t,E+c)
\ge\min(t,x)=b.
\]

所以

\[
\boxed{p^b\mid C_{12}.}
\tag{2.4}

### 2.2 gap depth

由定义 `a_*<=alpha=v_p(a)`：

\[
\boxed{p^{a_*}\mid a.}
\tag{2.5}

因此 `(2.1)--(2.3)` 没有使用任何虚构容量；前两层都进入已经存在 exact small-factor
charge 的真实整数 reader。

---

## 3. charged-first residual 自动进入 `Z_0`

我们证明

\[
\boxed{z\le v_p(Z_0).}
\tag{3.1}

若 `z=0` 显然。以下设 `z>0`。由 `(2.3)`：

\[
x>t+\alpha>t.
\tag{3.2}

因此 `(1.2)` 中 `t` 不可能支付 `x`，从而

\[
x\le\max(2g+\omega,r).
\tag{3.3}

减去 `t+alpha`：

\[
z
\le
\max(2g+\omega-t-\alpha,\ r-t-\alpha).
\tag{3.4}

由 `g<=t`：

\[
2g-t\le g,
\]

故得到更强的 local cap

\[
\boxed{
z
\le
\max\bigl(
0,
 g+\omega-\alpha,
 r-t-\alpha
\bigr).
}
\tag{Charged-first-cap}

而右端显然不超过

\[
\max(0,r+g+\omega-\alpha)=v_p(Z_0),
\]

证明 `(3.1)`。

这说明旧 `Z_0-only` residual 可以替换为一个 canonical、通常更小的 exponent：

\[
\boxed{z_p=(x_p-v_p(A_{12})-v_p(a))_+.}
\tag{3.5}

特别地，它要求同一 source depth **同时超过 numerator coefficient depth 与 gap depth之和**，
而不再只是“某一份 projective layer 恰好落在 `Z_0`”。

---

## 4. 全局 charged-first factorization

定义

\[
X_B^\sharp=\prod_{p\mid X_Q}p^{b(p)},
\qquad
X_a^\sharp=\prod_{p\mid X_Q}p^{a_*(p)},
\qquad
X_Z^\sharp=\prod_{p\mid X_Q}p^{z(p)}.
\]

逐 prime `(2.3)` 给

\[
\boxed{X_Q=X_B^\sharp X_a^\sharp X_Z^\sharp.}
\tag{4.1}

且

\[
\boxed{X_B^\sharp\mid\operatorname{core}_{10}(C_{12}),}
\tag{4.2}
\]

\[
\boxed{X_a^\sharp\mid\operatorname{core}_{10}(a),}
\tag{4.3}
\]

\[
\boxed{X_Z^\sharp\mid\operatorname{core}_{10}(Z_0).}
\tag{4.4}

与旧 `tail-rough-z0-only-frontier` 的 split 比较：旧 bottom exponent不超过 `t`，所以旧
`Z_0` residual逐 prime至少为 `(x-t-alpha)_+`。因此

\[
\boxed{X_Z^\sharp\mid X_Z^{\rm old}.}
\tag{4.5}

这是一条严格的 allocation improvement；没有改变 `X_Q`，只把已有可收费容量优先用满。

---

## 5. `Z_0` residual 不再需要匿名 projective reader

`Charged-first-cap` 还允许把 `z` 再拆成三个显式 source readers。

记

\[
R_*:=(r-t-\alpha)_+,
\qquad
G_*:=(g+\omega-\alpha)_+.
\tag{5.1}

由 `Charged-first-cap`：

\[
z\le\max(R_*,G_*).
\tag{5.2}

定义

\[
\boxed{z_3:=\min(z,R_*),}
\tag{5.3}
\]

\[
\boxed{z_{G}:=z-z_3.}
\tag{5.4}

若 `z<=R_*`，则 `z_G=0`；若 `z>R_*`，由 `(5.2)` 必有 `z<=G_*`，故

\[
\boxed{z_G\le G_*.}
\tag{5.5}

再定义

\[
\boxed{z_g:=\min(z_G,g),}
\tag{5.6}
\]

\[
\boxed{z_\omega:=z_G-z_g.}
\tag{5.7}

于是

\[
\boxed{z=z_3+z_g+z_\omega.}
\tag{5.8}

显然

\[
\boxed{z_3\le(r-t-\alpha)_+,}
\tag{5.9}
\]

\[
\boxed{z_g\le g.}
\tag{5.10}

最后证明

\[
\boxed{z_\omega\le\omega.}
\tag{5.11}

若 `z_G<=g`，左边为 0。若 `z_G>g`，则 `G_*>g`，并由 `(5.5)`：

\[
z_\omega=z_G-g
\le G_*-g
=g+\omega-\alpha-g
=\omega-\alpha
\le\omega.
\]

---

## 6. Gaussian-at-infinity residual 转入纯 numerator norm

沿用 `tail-rough-angular-source-transfer`：

\[
b_i=p^E B_i,
\qquad (B_1,B_2)=1,
\]

\[
g_n=(a_1,a_2),
\qquad
\bar a_i=a_i/g_n,
\]

并定义

\[
\boxed{
N_{\rm num}
=(\bar a_1 10^{m_2})^2+\bar a_2^2.
}
\tag{6.1}

source root

\[
p^c\mid C_Q=B_1 10^{m_2}+B_2
\]

与 primitive Gaussian orientation 已严格给出

\[
\boxed{
v_p(N_{\rm num})\ge\min(c,\omega).}
\tag{6.2}

而 `(5.11)` 给 `z_omega<=omega`，同时

\[
z_\omega\le z\le x\le c.
\]

所以

\[
\boxed{z_\omega\le v_p(N_{\rm num}).}
\tag{Gaussian-infinity-reader}

因此 Gaussian 部分的 charged-first `Z_0` residual 完全可以从 projective denominator
转读为**纯 numerator Gaussian norm**。

---

## 7. 最终 residual reader decomposition

定义 third-excess product

\[
\boxed{
R_{3,\rm exc}
:=
\prod_{p\mid X_Q}
 p^{(r_p-t_p-\alpha_p)_+}.
}
\tag{7.1}

以及

\[
X_3^\sharp=\prod p^{z_3(p)},
\qquad
X_g^\sharp=\prod p^{z_g(p)},
\qquad
X_\omega^\sharp=\prod p^{z_\omega(p)}.
\]

由 §5--6：

\[
\boxed{X_Z^\sharp=X_3^\sharp X_g^\sharp X_\omega^\sharp,}
\tag{7.2}
\]

\[
\boxed{X_3^\sharp\mid R_{3,\rm exc}\mid R_3^{\rm den},}
\tag{7.3}
\]

\[
\boxed{X_g^\sharp\mid(a_1,a_2),}
\tag{7.4}
\]

\[
\boxed{X_\omega^\sharp\mid\operatorname{core}_{10}(N_{\rm num}).}
\tag{7.5}

所以整个 post-tail rough source现在有 exact exponent-layer factorization

\[
\boxed{
X_Q
=
X_B^\sharp
X_a^\sharp
X_3^\sharp
X_g^\sharp
X_\omega^\sharp,
}
\tag{Charged-first-normal-form}

其中前两个 factors 已经由真实 small factor 收费，后三个都有不含匿名 `Z_0` 的 reader。

换言之，`Z_0-only frontier` 可以更新为

\[
\boxed{
\text{third excess beyond }(t+\alpha)
\quad\cup\quad
\text{prefix common scale}
\quad\cup\quad
\text{pure numerator Gaussian orientation}.
}
\tag{7.6}

---

## 8. reducedness 对 common reader 的进一步限制

若

\[
E=v_p(b_1)=v_p(b_2)>0,
\]

则 `(a_i,b_i)=1` 强制

\[
p\nmid a_1a_2,
\]

因此

\[
\boxed{E>0\Longrightarrow g=0.}
\tag{8.1}

所以 `X_g^sharp` 只可能支撑在 **prefix denominators 对 p 都是 units** 的 baseline-free
source primes 上。

特别地，在 `E>0` 的 sheet，若 third-excess reader不支付 residual，那么全部剩余 depth 都是
Gaussian-at-infinity depth，并由 `N_num` 读取。

---

## 9. `d_3`-dominant sector 中 common reader 只有半份 `S` 高度

在真正危险的 `d_3=max(s_1,s_2,d_3)` sector，surplus simplex 已给

\[
s_1+s_2\le2.
\]

因此

\[
n_1+n_2
=(m_1+s_1)+(m_2+s_2)
\le S+2.
\]

而

\[
X_g^\sharp\mid(a_1,a_2),
\qquad
a_i<10^{n_i},
\]

故

\[
\boxed{
\log_{10}X_g^\sharp
<\min(n_1,n_2)
\le\frac{S+2}{2}.
}
\tag{Common-half-S}

所以 prefix-common residual 即使达到其全部容量，也不再是一整份自由 `S` height。

---

## 10. second-Schmidt bootstrap 的更新

现有 post-tail inequality为

\[
\log F_-
\ge
S-\log X_Q-o(S).
\tag{10.1}

`tail-rough-bottom-small-factor-charge` 对任何 `X_B^sharp|C_12` 同样给

\[
\boxed{X_B^\sharp G<F_-,}
\tag{10.2}

而 gap exact factorization对 `X_a^sharp|a` 给

\[
\boxed{X_a^\sharp Q<F_-.}
\tag{10.3}

代入 `Charged-first-normal-form`：

\[
\boxed{
3\log F_-
+
\log(X_3^\sharp X_g^\sharp X_\omega^\sharp)
\ge
3S-o(S).
}
\tag{Charged-first-bootstrap}

等价地

\[
\boxed{
\log F_-
\ge
S-
\frac13
\log(X_3^\sharp X_g^\sharp X_\omega^\sharp)
-o(S).
}
\tag{10.4}

与旧 `Z_0-bootstrap` 相比，未收费对象不再只是抽象的 `gcd(C_Q,Z_0)`；它已经被分解成
`R_{3,exc}`、`(a_1,a_2)` 与 `N_num` 三个具体接口，其中 common reader在 dominant sector
最多只有 `S/2+O(1)` 高度。

---

## 11. 当前新 frontier

本文完成后，下一步不需要继续直接估计整个

\[
\gcd(C_Q,Z_0).
\]

更精确的目标是分别处理：

1. **third-excess sheet**
   \[
   (r-t-\alpha)_+>0,
   \]
   即第三 denominator exclusive depth必须同时超过 numerator coefficient 与 gap depth；
2. **baseline-free common sheet**，只支撑在 `E=0`，其总 height 已有 `<=S/2+O(1)`；
3. **Gaussian-at-infinity sheet**，由 source root 强制进入纯 numerator norm `N_num`，可继续与
   `A^circ` 的 cyclotomic overlap、carrier orientation 或 digit shell 联立。

最值得优先攻击的是第 1 与第 3 项；第 2 项已经失去“一整份 S rough loss”的能力。

---

## 12. 状态摘要

- **`已严格完成`**：`charged-first` local split `(2.1)--(2.3)`。
- **`已严格完成`**：`Charged-first-cap` 与 `X_Z^sharp|Z_0`。
- **`已严格完成`**：`z=z_3+z_g+z_omega` 三层 residual decomposition。
- **`已严格完成`**：Gaussian residual `X_omega^sharp|N_num`。
- **`已严格完成`**：`E>0 => g=0` 与 dominant `Common-half-S`。
- **`结构压缩`**：旧匿名 `Z_0-only` loss被替换为 third-excess / common / Gaussian 三个显式 reader；
  前两类已分别具有更强的 sheet 条件或高度上界。
- **`待证`**：`R_{3,exc}` 的 small-factor / tail charge；`N_num` 的 independent orientation height；
  把 `Charged-first-bootstrap` 喂回 non-canonical side-branch LP；DD global explicit `<=6` / absolute height。

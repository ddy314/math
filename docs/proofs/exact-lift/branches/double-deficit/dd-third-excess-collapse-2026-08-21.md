# DD charged-first frontier：third-excess collapse

> **依赖：** [`dd-z0-charged-first-2026-08-21.md`](dd-z0-charged-first-2026-08-21.md)、
> [`tail-allocation-ledger.md`](tail-allocation-ledger.md) 中
> `tail-rough-cq-excess`、`tail-rough-general-transfer`、
> `tail-rough-angular-source-transfer`、`tail-rough-projective-bottom-two-payer`，
> 以及 [`core.md`](core.md) 的 DD coefficient plane、integer sphere 与 stereographic denominator。
>
> **严格状态：** `已严格完成（charged-first residual 中全部 third-excess primes）`。
>
> `dd-z0-charged-first-2026-08-21.md` 将 post-tail rough loss 的未收费部分压成
> third-excess / prefix-common / Gaussian-at-infinity 三类 reader。本文证明第一类本身不再拥有
> 一整份自由 rough height：若某个 prime 真正进入 third-excess，则 gap、numerator coefficient 与
> prefix-common depth全部被强制为零。随后只有两个可能：
>
> 1. source overflow 不深过 third denominator excess，此时它的**平方**整除 primitive source concat
>    `C_Q`；
> 2. source overflow 深过 third denominator excess，此时整份 overflow 都转入纯 numerator Gaussian
>    norm `N_num`。
>
> 因而 genuine third-only residual product `X_T` 满足
> \[
> \boxed{X_T^2\mid C_Q,}
> \]
> 特别地
> \[
> \boxed{\log_{10}X_T<S/2.}
> \]
> third-excess 不再是 full-`S` height pool。

---

## 1. local setup

固定 odd non-decimal prime
\[
p^x\Vert X_Q,
\qquad p\nmid10.
\]

沿用 charged-first 记号
\[
E=v_p(b_1)=v_p(b_2),
\qquad
j=v_p(b_3),
\qquad
r=(j-E)_+,
\]
\[
t=v_p(C)=v_p(A_{12}),
\qquad
g=v_p(a_1,a_2),
\qquad
\omega=v_p(N_{\rm ang}),
\qquad
\alpha=v_p(a).
\]

primitive denominator concat为
\[
C_Q=Q/(b_1,b_2),
\qquad
c=v_p(C_Q),
\]
且已有 exact source-overflow formula
\[
\boxed{
x=\max\bigl(c-j-\min(E,j),0\bigr).
}
\tag{1.1}

只讨论 `x>0`。general transfer refinement给
\[
\boxed{x\le\max(t,2g+\omega,r),}
\tag{1.2}
并且 common numerator depth满足
\[
\boxed{g\le t.}
\tag{1.3}

charged-first residual为
\[
z=(x-t-\alpha)_+,
\]
而 third-excess capacity为
\[
R_*=(r-t-\alpha)_+.
\]

本文所谓一个 **third-excess prime**，是指 charged-first split 中
\[
\boxed{z_3=\min(z,R_*)>0.}
\tag{1.4}

因此自动有
\[
\boxed{x>t+\alpha,
\qquad
r>t+\alpha.}
\tag{1.5}

特别地 `r>0`，所以
\[
\boxed{j>E.}
\tag{1.6}

---

## 2. sphere two-sheet 强迫 `alpha=0`

由 `j>E`，整数球面的 lcm denominator `q_lcm` 在 `p` 处有 depth `j`。
又因 `p|b_3` 且 `(a_3,b_3)=1`：
\[
v_p(y_3)=0.
\tag{2.1}
\]

前两 ghost 坐标满足
\[
v_p(y_1),v_p(y_2)\ge r>0,
\]
所以 sphere equation
\[
H^2=y_1^2+y_2^2+y_3^2
\]
模 `p` 给
\[
\boxed{v_p(H)=0.}
\tag{2.2}

令
\[
g_y=(y_1,y_2).
\]
现有 projective ledger 已证明
\[
\boxed{v_p(g_y)=r+g,}
\tag{2.3}
以及 primitive ghost norm depth
\[
\boxed{
v_p(y_1^2+y_2^2)=2(r+g)+\omega.
}
\tag{2.4}

sphere factorization为
\[
(H-y_3)(H+y_3)=y_1^2+y_2^2.
\]
因为 `p` 为奇素数且 `H,y_3` 都是 units，`H-y_3` 与 `H+y_3` 不可能同时被 `p`
整除。因此
\[
\boxed{
\{v_p(H-y_3),v_p(H+y_3)\}
=
\{0,2(r+g)+\omega\}.
}
\tag{Sphere-two-sheet-general}

而 DD gap normalization
\[
H-y_3=La
\]
在 `p\nmid10`、`L|10^{m_3}` 下给
\[
v_p(H-y_3)=v_p(a)=\alpha.
\]
于是
\[
\boxed{
\alpha\in\{0,2(r+g)+\omega\}.
}
\tag{2.5}

third-excess 条件 `(1.5)` 给
\[
\alpha<r.
\]
但第二个候选满足
\[
2(r+g)+\omega\ge2r>r.
\]
故只能
\[
\boxed{\alpha=0.}
\tag{Gap-unit-third}

所以任何真正 third-excess prime 必定位于 sphere 的 complementary sheet：
\[
\boxed{
v_p(H-y_3)=0,
\qquad
v_p(H+y_3)=2(r+g)+\omega.}
\tag{2.6}

---

## 3. DD coefficient plane 再强迫 `t=0`

由 `(1.6)`，source overflow formula `(1.1)` 化成
\[
\boxed{x=c-j-E>0,}
\tag{3.1}
所以
\[
\boxed{c>j+E.}
\tag{3.2}

DD §17 coefficient plane可写成 exact identity
\[
\boxed{
\mathcal M-QH=\tau a,
}
\tag{3.3}
其中
\[
\boxed{\mathcal M=q_{\rm lcm}C.}
\tag{3.4}

在当前 prime：

- `v_p(q_lcm)=j`；
- `v_p(C)=t`；
- `v_p(Q)=E+c`；
- `v_p(H)=0` by `(2.2)`；
- `v_p(\tau)=j`，因为 `\tau=b_3/(10^{m_3},b_3)` 且 `p\nmid10`；
- `v_p(a)=\alpha=0` by `(Gap-unit-third)`。

因此 `(3.3)` 三个 relevant depths为
\[
v_p(\mathcal M)=j+t,
\tag{3.5}
\]
\[
v_p(QH)=E+c>j,
\tag{3.6}
\]
\[
v_p(\tau a)=j.
\tag{3.7}

若 `t>0`，则 `(3.5)` 与 `(3.6)` 都严格大于 `j`，故它们的差也严格被 `p^{j+1}`
整除，不可能等于 valuation 恰为 `j` 的右端 `(3.7)`。

所以
\[
\boxed{t=0.}
\tag{Coefficient-unit-third}

再由 `(1.3)`：
\[
\boxed{g=0.}
\tag{Common-unit-third}

因此 third-excess prime 上三个此前可能重复出现的 reader全部消失：
\[
\boxed{
\alpha=t=g=0.
}
\tag{Third-unit-triple}

特别地 charged-first 的前两层在这个 prime 上都是零，故
\[
\boxed{z=x.}
\tag{3.8}

---

## 4. local cap 退化成纯 `third / Gaussian` 二分

把 `(Third-unit-triple)` 代入 general transfer `(1.2)`：
\[
\boxed{x\le\max(r,\omega).}
\tag{Third-Gaussian-dichotomy}

因此只剩两个互补 cases。

### 4.1 Third-dominant：`x<=r`

由 `j=E+r` 与 `(3.1)`：
\[
c=x+j+E=x+2E+r.
\tag{4.1}

若
\[
x\le r,
\]
则
\[
c=x+2E+r\ge2x+2E\ge2x.
\]
所以
\[
\boxed{p^{2x}\mid C_Q.}
\tag{Third-square-local}

也就是说，真正由 third denominator excess 支付的 source overflow并不只是一份 `p^x`
进入 `R_3^{den}`；source root本身已经含有至少**双倍**这份 depth。

### 4.2 Gaussian-dominant：`x>r`

此时 `Third-Gaussian-dichotomy` 迫使
\[
\boxed{x\le\omega.}
\tag{4.2}

`tail-rough-angular-source-transfer` 的 same-orientation theorem给
\[
\boxed{
v_p(N_{\rm num})\ge\min(c,\omega),
}
\tag{4.3}
其中
\[
N_{\rm num}
=(\bar a_1 10^{m_2})^2+\bar a_2^2.
\]

又由 `(4.1)` 显然 `c>x`，与 `(4.2)` 合并：
\[
\min(c,\omega)\ge x.
\]
因此
\[
\boxed{p^x\mid N_{\rm num}.}
\tag{Third-to-Gaussian-local}

注意这里转移的是**整份** `p^x`，包含旧 charged-first split 中原本先分给 `z_3` 的那一段；
所以当 `x>r` 时，没有必要保留一个独立 third reader。

---

## 5. whole-prime reallocation

对所有满足 `(1.4)` 的 third-excess primes，按 `x<=r` / `x>r` 分成两个不交 support。
定义
\[
\boxed{
X_T
:=
\prod_{\substack{p:\ z_3(p)>0\\x_p\le r_p}}
p^{x_p},
}
\tag{5.1}

\[
\boxed{
X_{T\to G}
:=
\prod_{\substack{p:\ z_3(p)>0\\x_p>r_p}}
p^{x_p}.
}
\tag{5.2}

逐 prime 使用 `(Third-square-local)`：
\[
\boxed{X_T^2\mid C_Q.}
\tag{Third-square-global}

逐 prime 使用 `(Third-to-Gaussian-local)`：
\[
\boxed{X_{T\to G}\mid\operatorname{core}_{10}(N_{\rm num}).}
\tag{Third-Gaussian-global}

所以旧 `R_{3,exc}` reader可以完全替换为：
\[
\boxed{
\text{square-root source reader }X_T
\quad\cup\quad
\text{existing pure numerator Gaussian reader}.
}
\tag{5.3}

不存在第三个 full-height anonymous denominator pool。

---

## 6. `X_T` 只有半份 prefix height

ordinary prefix denominator concat满足
\[
10^{S-1}\le Q<10^S,
\qquad
C_Q=Q/(b_1,b_2)\le Q.
\]

由 `Third-square-global`：
\[
X_T^2\le C_Q<10^S.
\]
所以
\[
\boxed{
\log_{10}X_T<\frac S2.
}
\tag{Third-half-S}

这是一条 unconditional Archimedean charge：不需要估计 `b_3`、`R_3^{den}` 或
stereographic denominator `Z_0` 的整体大小。

---

## 7. charged-first residual 的更新 canonical form

对没有进入 third-excess 的 primes，保留 `dd-z0-charged-first-2026-08-21.md` 的
common / Gaussian split。

更具体地，令 residual exponent仍为
\[
z=(x-t-\alpha)_+.
\]

- 若 `R_*=(r-t-\alpha)_+>0`，则本文证明 `alpha=t=g=0`，于是 `z=x`：
  - `x<=r` 时把整份 `z=x` 分给 `X_T`；
  - `x>r` 时把整份 `z=x` 分给 Gaussian reader；
- 若 `R_*=0`，则没有 third layer，继续定义
  \[
  z_g=\min(z,g),
  \qquad
  z_\omega=z-z_g.
  \]

于是可以重新定义全局 residual factors
\[
X_g^{\flat}:=
\prod_{R_*=0}p^{z_g(p)},
\]
以及把两类 Gaussian exponent合并为
\[
X_\omega^{\flat}:=
X_{T\to G}
\prod_{R_*=0}p^{z_\omega(p)}.
\]

charged-first normal form因而加强为
\[
\boxed{
X_Q
=
X_B^\sharp
X_a^\sharp
X_T
X_g^{\flat}
X_\omega^{\flat}.
}
\tag{Updated-charged-first-normal-form}

其中
\[
\boxed{X_T^2\mid C_Q,}
\tag{7.1}
\]
\[
\boxed{X_g^{\flat}\mid(a_1,a_2),}
\tag{7.2}
\]
\[
\boxed{X_\omega^{\flat}\mid\operatorname{core}_{10}(N_{\rm num}).}
\tag{7.3}

而且 `X_T` support上
\[
\boxed{v_p(a)=v_p(A_{12})=v_p(a_1,a_2)=0.}
\tag{7.4}

这比旧
\[
R_{3,exc}\cup(a_1,a_2)\cup N_{num}
\]
三-reader frontier更强：third reader已经降为 square-root source height。

---

## 8. dominant sector 的 non-Gaussian residual budget

在 `d_3`-dominant sector，前一文件已经证明
\[
\log_{10}X_g^{\flat}
\le\log_{10}(a_1,a_2)
<\frac{S+2}{2}.
\]

本文又有
\[
\log_{10}X_T<\frac S2.
\]

因此
\[
\boxed{
\log_{10}(X_TX_g^{\flat})<S+1.
}
\tag{NonGaussian-one-S}

更重要的不是这条粗和式本身，而是两个 half-`S` reader 的来源已经完全不同且显式：

- `X_T` 来自 `C_Q` 的 square-root source depth；
- `X_g^flat` 来自 prefix numerator gcd；
- 唯一仍可能携带 full independent orientation height的是 `X_omega^flat`。

所以 post-tail reoptimization 的真正下一 hard object已经缩成 pure numerator Gaussian reader
\[
\boxed{X_\omega^{\flat}\mid N_{\rm num}.}
\]

---

## 9. second-Schmidt bootstrap 更新

已有 exact charges
\[
X_B^\sharp G<F_-,
\qquad
X_a^\sharp Q<F_-.
\]

将 `Updated-charged-first-normal-form` 代入第二次 Schmidt：
\[
\boxed{
3\log F_-
+
\log(X_TX_g^{\flat}X_\omega^{\flat})
\ge3S-o(S).
}
\tag{9.1}

利用 `(NonGaussian-one-S)` 可写成
\[
\boxed{
3\log F_-
+
\log X_\omega^{\flat}
\ge2S-o(S).
}
\tag{Gaussian-only-bootstrap}

其中常数 `+1` 被吸收到 `o(S)`。

这条式子的意义是：在 dominant side branch 中，所有**非 Gaussian** post-tail rough loss合计最多消耗一整份 `S`；要让 small factor继续显著低于 `2S/3`，必须由 pure numerator Gaussian orientation
`X_omega^flat` 单独承担正线性高度。

---

## 10. 当前 frontier

本文关闭了 charged-first frontier 中的 `R_{3,exc}` full-height 问题。下一步只需重点处理：

\[
\boxed{
X_\omega^{\flat}
\mid
N_{\rm num}
=(\bar a_1 10^{m_2})^2+\bar a_2^2.
}
\]

已有可直接复用的额外结构：

1. `X_omega^flat` 的 odd prime support全部是 `1 mod 4`；
2. source root `C_Q=B_1 10^{m_2}+B_2` 保留同一个 Gaussian orientation；
3. `A^circ` 与 `N_num` 的 rough overlap满足
   \[
   \operatorname{core}_{10}\gcd(A^\circ,N_{\rm num})
   \mid10^{2|s_2|}+1;
   \]
4. third-excess 转入 Gaussian 的 primes还额外满足
   \[
   v_p(a)=v_p(A_{12})=v_p(a_1,a_2)=0.
   \]

因此下一轮最自然的目标是：对 `N_num` 的 Gaussian divisor与 decimal digit shell / bottom carrier建立一个
orientation-preserving height bound，把 `Gaussian-only-bootstrap` 喂回 non-canonical dominant LP。

---

## 11. 状态摘要

- **`已严格完成`**：third-excess `=> alpha=0` 的 sphere two-sheet collapse。
- **`已严格完成`**：DD coefficient plane进一步强迫 `t=g=0`。
- **`已严格完成`**：`x<=max(r,omega)` 的 pure third/Gaussian dichotomy。
- **`已严格完成`**：`x<=r => p^(2x)|C_Q`。
- **`已严格完成`**：`x>r => p^x|N_num`，并且转移整份 overflow。
- **`已严格完成`**：`X_T^2|C_Q` 与 `Third-half-S`。
- **`结构压缩`**：`R_{3,exc}` 不再是 full-height reader；dominant post-tail 的唯一 full-orientation hard object为 `X_omega^flat|N_num`。
- **`待证`**：pure numerator Gaussian orientation height；non-canonical branch LP；DD global explicit `<=6` / absolute height。

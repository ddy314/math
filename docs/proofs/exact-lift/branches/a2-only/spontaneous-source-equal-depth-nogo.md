# A2 source equal-depth angle gate 的二阶 Hensel no-go

> **依赖：** `spontaneous-source-equal-depth.md`、`hensel.md`、`spontaneous-angle.md`。
>
> **严格状态：**`spontaneous-source-equal-depth.md` 已把 source residual odd parity 压到 `v_p(d)=h` 的 normalized cancellation。本文进一步在该 source first-layer curve 上做精确二阶展开，证明 angle extra-lift 并不强迫 `x` 落入 fixed/singular locus；它只是唯一选择 source linear root `r_s` 的二阶 Hensel correction。因而继续仅在 source 局部系统内做 resultant、discriminant 或 singular-prime hunting不会关闭该 shell。要排除它必须引入 source 之外的 global allocation、natural representative 或与 additive common carrier 的独立同步。本文是严格 no-go，不宣称 A2 全局关闭。

---

## 1. source first-layer curve

固定 genuine non-`3` inert source excess prime

\[
p\equiv3\pmod4,
\qquad p\ne3,5.
\]

沿用

\[
d:=225x^2-y,
\]

\[
\Phi_s=(99x-4)r_s-2x-4,
\]

\[
\Psi_9=3600(r_s+1)^2-y(99r_s-2)^2,
\]

\[
\Omega_{\rm sp}=4r_sd^2-xy^2\Phi_s.
\]

source first layer `d=Phi_s=0` 给

\[
\boxed{y_0=225x^2,}
\tag{1.1}
\]

以及令

\[
A:=99x-4,
\]
则

\[
\boxed{r_0=\frac{2(x+2)}A.}
\tag{1.2}
\]

旧 genuine source separation 已证明

\[
p\nmid x(x+2)A,
\tag{1.3}
\]
并且 `p != 3,5`，所以本文出现的 `225,404,50625` 也都是单位。

在 (1.1)–(1.2) 上还有两个 exact elementary values：

\[
\boxed{
r_0+1=\frac{101x}{A},}
\tag{1.4}
\]

\[
\boxed{99r_0-2=\frac{404}{A}.}
\tag{1.5}

这正是旧 source resultant collapse 的 first-layer 几何。

---

## 2. 等深 shell 的规范二阶参数

设 source excess

\[
p^{2h}\Vert\sigma,
\qquad h\ge1,
\]
并处于 angle odd-depth 唯一可能的 threshold

\[
v_p(d)=h,
\qquad
v_p(\Phi_s)=2h.
\]

在局部 DVR 中取

\[
\varepsilon:=p^h.
\]

定义单位

\[
d_1:=d/\varepsilon,
\qquad
\phi_2:=\Phi_s/\varepsilon^2.
\]

于是可以**精确**写成

\[
\boxed{y=y_0-\varepsilon d_1,}
\tag{2.1}
\]

\[
\boxed{
r_s=\frac{2(x+2)+\varepsilon^2\phi_2}{A}
=r_0+\frac{\varepsilon^2\phi_2}{A}.}
\tag{2.2}

这里没有把 `x` 固定成 Teichmuller lift；`x` 可仍是任意满足 genuine unit 条件的 p-adic prefix variable。本文只把相对于当前 `x` 的 transverse source corrections显式化。

---

## 3. `已严格完成`：第二 Hensel 方程一阶只读取 `d_1`

把 (2.1)–(2.2) 代入 `Psi_9`。由于 `r_s-r_0` 从 `epsilon^2` 才开始，模 `epsilon^2` 时 `r_s` 可直接换成 `r_0`：

\[
\begin{aligned}
\Psi_9
&=3600(r_s+1)^2-y(99r_s-2)^2\\
&\equiv
3600(r_0+1)^2
-(y_0-\varepsilon d_1)(99r_0-2)^2
\pmod{\varepsilon^2}.
\end{aligned}
\]

first-layer constant term为零；使用 (1.5)：

\[
\boxed{
\Psi_9
\equiv
\varepsilon d_1\frac{404^2}{A^2}
\pmod{\varepsilon^2}.}
\tag{3.1}

因此

\[
\boxed{
\frac{\Psi_9}{\varepsilon}
\equiv
\frac{404^2}{A^2}d_1
\pmod p.}
\tag{3.2}

这重新、并以局部展开方式解释了 `spontaneous-source-equal-depth.md` 的

\[
v_p(\Psi_9)=h.
\]

更重要的是：第二 Hensel equation 在这一层只固定 `d_1` 的线性单位类；它**尚未**约束二阶参数 `phi_2`。

---

## 4. `已严格完成`：angle extra lift恰好线性解出 `phi_2`

由定义直接有

\[
\Omega_{\rm sp}
=4r_s\varepsilon^2d_1^2
-x(y_0-\varepsilon d_1)^2\varepsilon^2\phi_2.
\]

除以 `epsilon^2` 再模 `p`：

\[
\boxed{
\frac{\Omega_{\rm sp}}{\varepsilon^2}
\equiv
4r_0d_1^2-xy_0^2\phi_2
\pmod p.}
\tag{4.1}

使用

\[
r_0=\frac{2(x+2)}A,
\qquad
y_0=225x^2,
\]
得到

\[
\boxed{
\frac{\Omega_{\rm sp}}{\varepsilon^2}
\equiv
\frac{8(x+2)}A d_1^2
-50625x^5\phi_2
\pmod p.}
\tag{4.2}

因此 angle valuation 想从 baseline `2h` 再提升至少一层，等价于

\[
\boxed{
\phi_2
\equiv
\frac{8(x+2)}{50625Ax^5}d_1^2
\pmod p.}
\tag{4.3}

由 (1.3) 及 `p != 3,5`，右边所有分母都是单位。于是：

\[
\boxed{
\text{对每个 genuine first-layer }x
\text{ 和每个单位 }d_1,
\text{恰有一个 }\phi_2\pmod p
\text{使 angle extra lift发生。}}
\tag{4.4}

这不是 singularity；它是普通的一次 Hensel correction。

---

## 5. source unit `sigma^sharp` 同样只是被唯一选定

旧 exact source identity为

\[
4\sigma=5^Mc_Q\Phi_s.
\]

在当前 shell 除以 `epsilon^2`：

\[
\boxed{
4\sigma^\sharp=5^Mc_Q\phi_2,
\qquad
\sigma^\sharp:=\sigma/p^{2h}.}
\tag{5.1}

因此一旦 (4.3) 选择了 `phi_2`，normalized source unit也被唯一固定：

\[
\boxed{
\sigma^\sharp
\equiv
\frac{5^Mc_Q}{4}
\frac{8(x+2)}{50625Ax^5}d_1^2
\pmod p.}
\tag{5.2}

所以 `spontaneous-source-equal-depth.md` 中看起来尚有自由的 `sigma^sharp` 并不是另一个独立 branch parameter；在 angle extra-lift locus 上它只是二阶 correction 的线性像。

同理 (3.2) 给

\[
\Psi_9^\sharp
\equiv\frac{404^2}{A^2}d_1.
\]
于是该文件的二单位 congruence本质上就是 (4.3) 的坐标变换，而不是额外的独立 quadratic obstruction。

---

## 6. `审计 / no-go`：source 局部 resultant不会产生 fixed bad-prime set

关键点是 (4.3) 对 `phi_2` 的系数

\[
50625x^5
\]
在所有 genuine source primes 上为单位。因此 angle extra-lift equation 对二阶 transverse correction的 Jacobian 永远非零：

\[
\boxed{
\frac{\partial}{\partial\phi_2}
\left(\Omega_{\rm sp}/\varepsilon^2\right)
\equiv-50625x^5\not\equiv0\pmod p.}
\tag{6.1}

所以该 shell 没有任何由 local Jacobian rank drop 产生的 singular bad prime。

换句话说：

\[
\boxed{
\text{source equal-depth angle cancellation}
\text{ 是 genuine simple second-order Hensel freedom，}
\text{不是 fixed/singular locus。}}
\tag{6.2}

因此以下路线必须降级：

- 对 `(Phi_s,Psi_9,Omega_sp)` 再做普通 first-layer resultant；
- 对 (4.3) 再做 discriminant / singular-prime hunting；
- 仅靠 `sigma^sharp,Psi_9^sharp` 的 Legendre symbol尝试制造第二个 obstruction。

这些都只是在重新描述同一个可解的一次二阶 correction。

---

## 7. 对 `G_sp mod 4` 闭环的真实含义

`spontaneous-angle-parity.md` 的 `G_sp=1 mod4` 分支要求 angle residual quotient自身携带 odd inert parity。`spontaneous-angle-overlap-depth.md` 已将 source supplier 压到当前 equal-depth shell；本文证明该 shell**不能靠 source 局部几何自身排除**。

因此若最终要从 parity dichotomy 删除 source residual supplier，必须加入 source 系统之外的独立信息，例如：

1. `D_src/L_0` 的 natural integer representative 与 `p^h` 高度；
2. source correction 与 decimal exponent/prefix defect `(H,e,M)` 的同步；
3. 与 additive common carrier `Theta_dec` / `G_sp` 的独立 prime-power depth；
4. global Gaussian factor allocation / height channel。

规范开放项不再是“求 source equal-depth 的更多 resultant”，而是

\[
\boxed{
\text{把 simple second-order correction (4.3)
与一个 source 外部的全局约束联立。}}
\tag{7.1}

本文保留这一 no-go，避免后续重复局部代数。

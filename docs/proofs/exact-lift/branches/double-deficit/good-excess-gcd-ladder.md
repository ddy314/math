# DD full-rational Good 的 canonical excess gcd ladder

> **依赖：** [`good-axis-normalization.md`](good-axis-normalization.md)。
>
> **严格状态：** `已严格完成（仅 frontier 条件蕴含）`。本文不增加新的 local resultant；它把上一文件得到的 axis-normalized depth
> \[
> c_p:=\max(h_p-v_p(N_c),0),
> \qquad
> \varepsilon_p:=\max(v_p(\alpha)-v_p(N_c),0)
> \]
> 提升成无需预先枚举 prime list 的 ordinary-integer gcd ladder。
>
> 核心结论：`G_exc` 是该 ladder 的第一层；稳定层读取 `C_N` support 上的完整 `epsilon_p`，而第一层之后的两个 residual 分别是 **unpaid denominator depth** 与 **numerator overflow**，逐 prime 永不同时出现。本文同时证明 `A_N`、`Lambda_ax`、`Lambda_1` 三条 ladder 在 main support 上完全相同，因此三者不能被误算成三份独立 obstruction。

---

## 1. 三个 tail reader 的共同局部深度

沿用

\[
C_N
=\frac{C_L^{\rm main}}
{(C_L^{\rm main},N_c)},
\]

\[
A_N
=\frac{\alpha}{(\alpha,N_c)},
\]

\[
\Lambda_{\rm ax}
=\frac{\mathcal T_+}{(\mathcal T_+,\mathcal T_-)},
\]

\[
\Lambda_1
=\frac{N(\Delta_1)}
{(N(\Delta_1),H_R,N_c)}.
\]

固定

\[
p^h\Vert C_L^{\rm main},
\qquad
n=v_p(N_c).
\]

定义

\[
\boxed{c_p:=v_p(C_N)=\max(h-n,0).}
\tag{1.1}
\]

上一文件已经证明

\[
\boxed{
v_p(A_N)
=v_p(\Lambda_{\rm ax})
=v_p(\Lambda_1)
=\varepsilon_p.}
\tag{1.2}
\]

其中

\[
\boxed{
\varepsilon_p
=\max(v_p(\alpha)-n,0).}
\tag{1.3}
\]

因此 main support 上的 primitive excess 已完全压成一对非负整数

\[
(c_p,\varepsilon_p).
\]

---

## 2. `G_exc` 是 ladder 的第一层

对任意 reader

\[
R\in\{A_N,\Lambda_{\rm ax},\Lambda_1\}
\]

定义

\[
\boxed{D_1(R):=\gcd(C_N,R).}
\tag{2.1}
\]

逐 prime：

\[
v_p(D_1(R))
=\min(c_p,\varepsilon_p).
\]

上一文件已识别该深度为 `x_p`，所以

\[
\boxed{
D_1(A_N)
=D_1(\Lambda_{\rm ax})
=D_1(\Lambda_1)
=G_{\rm exc}
}
\tag{2.2}
\]

按 `C_L^{main}` 的 prime-primary part 精确成立。

这里若三个普通 gcd 在 exceptional / non-main support 上还含其它因子，不把这些额外因子并入 `G_exc`；本文所有等号均指 main-primary projection，与前两文件约定一致。

---

## 3. `C_N^k` ladder 逐层读取完整 excess tail

对整数

\[
k\ge1
\]

和任一 reader `R` 定义

\[
\boxed{
D_k(R):=\gcd(C_N^k,R).
}
\tag{3.1}
\]

则

\[
\boxed{
v_p(D_k(R))
=\min(kc_p,\varepsilon_p).}
\tag{3.2}
\]

因此三条 ladder 的 main-primary part 对每个 `k` 都完全相同：

\[
\boxed{
D_k(A_N)^{\rm main}
=D_k(\Lambda_{\rm ax})^{\rm main}
=D_k(\Lambda_1)^{\rm main}.}
\tag{Reader-ladder-equality}
\]

这给出一个不需要 prime factorization 才能定义的 excess-depth reader。

---

## 4. successive quotient 读取第 `k` 个 core-height block

令

\[
\boxed{
E_k(R):=\frac{D_{k+1}(R)}{D_k(R)}.
}
\tag{4.1}
\]

由于 `D_k|D_{k+1}`，这是正整数。

逐 main prime：

\[
\boxed{
v_p(E_k(R))
=\min((k+1)c_p,\varepsilon_p)
-\min(kc_p,\varepsilon_p).}
\tag{4.2}
\]

所以：

- 若 `epsilon_p<=k c_p`，第 `k` 层以后不再出现该 prime；
- 若 `k c_p<epsilon_p<(k+1)c_p`，本层读取剩余 `epsilon_p-kc_p`；
- 若 `epsilon_p>=(k+1)c_p`，本层再读取完整一个 `c_p` block。

这把“excess 比剩余 main core 还深多少”变成普通 gcd successive quotients。

---

## 5. 稳定层与 full `C_N`-supported tail

对固定整数 reader `R`，存在有限 `k_0`，使得对所有 `k>=k_0`：

\[
D_k(R)=D_{k_0}(R)
\]

在 `C_N` support 上稳定。

记 main-primary 稳定值为

\[
\boxed{D_\infty.}
\tag{5.1}
\]

则

\[
\boxed{
v_p(D_\infty)=
\begin{cases}
\varepsilon_p,&c_p>0,\\
0,&c_p=0.
\end{cases}}
\tag{5.2}
\]

因此 `D_infty` 精确读取：**仍有未被 `N_c` 吃掉的 main denominator depth的 primes 上，完整的 numerator excess tail。**

如果 `n>=h`，则 `c_p=0`；即使 `alpha` 还有更深 p-depth，它也已不属于可用于关闭 main `C_L` 的 unpaid core，故不会进入 ladder。

---

## 6. 第一层之后的 canonical deficit / overflow 分解

第一层为

\[
G_{\rm exc}=D_1.
\]

定义 denominator residual

\[
\boxed{
C_{\rm rem}:=\frac{C_N}{G_{\rm exc}},}
\tag{6.1}
\]

以及 full supported tail 相对第一层的 overflow

\[
\boxed{
R_{\rm over}:=\frac{D_\infty}{G_{\rm exc}}.}
\tag{6.2}
\]

逐 prime：

\[
\boxed{
v_p(C_{\rm rem})
=\max(c_p-\varepsilon_p,0),}
\tag{6.3}
\]

\[
\boxed{
v_p(R_{\rm over})
=\max(\varepsilon_p-c_p,0).}
\tag{6.4}
\]

因此

\[
\boxed{
\gcd(C_{\rm rem},R_{\rm over})=1
}
\tag{Deficit-overflow-separation}
\]

在 main support 上严格成立。

这给出最终三分：

\[
\boxed{
\begin{array}{c|c}
\varepsilon_p<c_p
&\text{留下 unpaid denominator deficit }c_p-\varepsilon_p\\
\varepsilon_p=c_p
&\text{该 prime 在第一层恰好完全匹配}\\
\varepsilon_p>c_p
&\text{留下 numerator overflow }\varepsilon_p-c_p.
\end{array}}
\tag{6.5}
\]

其中 numerator overflow 已经超出原 `C_N` 可支付的 main depth，不能再拿来重复计算 `C_L` closure。

---

## 7. 三条 reader 不能当三份独立 obstruction

`Reader-ladder-equality` 是一个必须保留的 no-double-count 审计。

虽然

\[
A_N,
\qquad
\Lambda_{\rm ax},
\qquad
\Lambda_1
\]

分别来自：

- 真实 concatenated numerator；
- axis/two-block Gaussian companion；
- secondary norm quotient；

但在 main core 上它们的 p-depth函数都恒等于同一个

\[
\varepsilon_p=\max(v_p(\alpha)-v_p(N_c),0).
\]

所以：

\[
\boxed{
\text{三条 reader 是同一 pure excess tail 的不同坐标图，}
\text{不是三份可相加的 height。}}
\tag{Reader-no-triple-pay}
\]

特别地，单纯证明

\[
G_{\rm exc}\mid A_N,
\quad
G_{\rm exc}\mid\Lambda_{\rm ax},
\quad
G_{\rm exc}\mid\Lambda_1
\]

不能产生三倍 modulus surplus。

---

## 8. 真正剩下的 independent interface：small `R_0` remainder

虽然三条 tail reader 本身不独立，numerator reconstruction 仍给出一个不同性质的 **Archimedean-small remainder**：

\[
\boxed{
UA_0+R_0=g_0B10^dA_{12},
\qquad
\log R_0=o(S).}
\tag{8.1}
\]

令

\[
A_0^\circ:=\frac{A_0}{(A_0,N_c)}.
\tag{8.2}
\]

由命题 1.1，main prime 上

\[
v_p(A_0^\circ)=\varepsilon_p.
\]

所以所有 ladder target primes 同时满足

\[
\boxed{
g_0B10^dA_{12}\equiv R_0
\pmod{A_0^\circ_{\rm target}}.}
\tag{Small-remainder}
\]

这里右边只有 `10^{o(S)}` 高度；这与前三个 reader 的“同一 valuation shadow”不同，是后续 digit-shell separation 真正应该利用的接口。

但是 `(Small-remainder)` 单独还不能推出空性：模数的逆元可把小 `R_0` 映射到任意合法 `A_{12}` residue。必须再与一个不由 numerator reconstruction 重构的独立 residue/size condition 联立。

---

## 9. 当前 frontier

现在 full rational Good 的 pure excess 可用一条完全 canonical pipeline描述：

\[
\boxed{
\begin{aligned}
C_N&=C_L^{\rm main}/(C_L^{\rm main},N_c),\\
A_N&=\alpha/(\alpha,N_c),\\
D_k&=\gcd(C_N^k,A_N),\\
G_{\rm exc}&=D_1,\\
D_\infty&=\text{stable }C_N\text{-supported tail},\\
C_{\rm rem}&=C_N/G_{\rm exc},\\
R_{\rm over}&=D_\infty/G_{\rm exc},\\
(C_{\rm rem},R_{\rm over})&=1.
\end{aligned}}
\tag{9.1}
\]

`Lambda_ax` 与 `Lambda_1` 给相同 ladder，因此只作为交叉审计保留。

下一条真正可能推进 closure 的命题应直接针对 `(Small-remainder)`：寻找 `A_0^circ_target` 上第二个独立、同样具有短 natural representative 的 residue。若只能再次推出 `Tail-axis`、`Radius-resultant-collapse`、`Nc1-elim` 或 clean-source 的同一 reconstruction，则应判为重复投影。

---

## 10. 状态摘要

- **`已严格完成（frontier 条件蕴含）`**：`C_N^k` excess gcd ladder；`D_1=G_exc`；stable `D_infty`；canonical deficit/overflow separation；三条 reader ladder 在 main support 上相同；`R_0` small-remainder interface。
- **`失效/降级`**：把 `A_N/Lambda_ax/Lambda_1` 三条 reader 当作三份独立 height；把 `R_over` 再计入原 `C_N` 的可支付深度。
- **`待证`**：第二个 independent short residue；axis-normalized digit-shell separation；`log G_exc=o(S)` 或其它 strict bound；full rational Good emptiness；genuine-Gaussian closure；DD 全局空性。

# A2 additive CRT quotient 的 Gaussian-slot orientation reader

> **依赖：** `spontaneous-crt-quotient-endpoint-parameterization.md`、`spontaneous-crt-quotient-source-scale.md`、`endpoint-lattice.md` §§13–16。
>
> **严格状态：**此前已把 `Q_Delta` 的绝对无界尺度正规化到 endpoint lattice 参数 `(M,eta,d,c_Q)`。本文进一步使用 high-2 Gaussian factor 的 exact slot equality 消去 `c_Q,w`，得到一个真正与 Gaussian side 同尺度的 normalized CRT quotient `Q_{Delta,G}`。在 reflection high-2 lattice 中，minus/high factor 与 plus/high factor 分别强迫 `Q_{Delta,G}` 落入两个严格不交的固定实区间；因此 `Q_Delta` 本身已经成为 Gaussian side 的 orientation reader。进一步把阈值 `Q_{Delta,G}=1` 乘回整数平面，得到奇整数 sign carrier `O_Delta=2^{A_G}Q_Delta-5^{B_G}k_h^3`，其符号与 Gaussian side完全等价。本文没有把该 sign carrier 与 additive CRT residue / source Hensel phase联立到矛盾，因此不关闭 A2。

---

## 1. notation

沿用 dangerous reflection core：

\[
N=10^M,\qquad T=10^m,\qquad \eta=2m-M,
\]

\[
x=\frac{b_2}{N},\qquad s=\frac K N,\qquad w=\frac{b_3}{T},
\]

以及

\[
\frac1{10}<x<\frac2{19},\qquad
\frac{2499}{250}<s<10.
\tag{1.1}
\]

令

\[
\delta:=\frac CD,\qquad 0<\delta<\frac3{250}.
\tag{1.2}
\]

`spontaneous-crt-quotient-source-scale.md` 已证明

\[
\frac{\Delta_+}{D^2-C^2}
=
\mathfrak a_\Delta\,\Psi_\Delta,
\tag{1.3}
\]

其中

\[
\mathfrak a_\Delta
=\frac{c_u^25^\lambda}{g}K^2,
\tag{1.4}
\]

\[
\Psi_\Delta
:=
\frac{\mathscr S_+}{TK^2}
\frac1{1-\delta^2}.
\tag{1.5}
\]

已有严格窗

\[
\boxed{
\frac1{17}<\Psi_\Delta
<\frac{1001}{15000}.}
\tag{1.6}
\]

这里上界使用 `S_+/(TK^2)<1/15` 与 `1/(1-delta^2)<1001/1000`。

---

## 2. exact Gaussian high-factor coordinate

令 high factor 的真实 normalized coordinate 为

\[
\boxed{
\sigma_\varepsilon
:=\frac{H_0+\varepsilon Y_2}{gT},
\qquad \varepsilon\in\{-1,+1\}.}
\tag{2.1}
\]

其中 `epsilon` 表示 high-2 factor 实际落在 `H_0-Y_2` 或 `H_0+Y_2`。

由 `endpoint-lattice.md` §13 的 exact high-factor equality

\[
H_0+\varepsilon Y_2=\frac{g^2k_h}{2},
\]
得到

\[
\boxed{
\frac gT=\frac{2\sigma_\varepsilon}{k_h}.}
\tag{2.2}
\]

endpoint short windows给

\[
\boxed{
\frac{393}{125}<\sigma_-<\frac{1607}{500},}
\tag{2.3-}
\]

\[
\boxed{
\frac{2389}{500}<\sigma_+<\frac{606}{125}.}
\tag{2.3+}
\]

这两段本身已经不交。

---

## 3. eliminate `c_Q,w` from the CRT main scale

前一文件给

\[
\mathfrak a_\Delta
=
\frac{s^2w^3}{4xc_Q^3}
2^{(\eta-M)/2}5^{3M+2\eta-4d}.
\tag{3.1}
\]

另一方面 Gaussian slot equality `endpoint-lattice.md` (16.2) 可写为

\[
\boxed{c_Qk_h
=2^{\eta+2}5^{\eta+1-d}
\frac{\sigma_\varepsilon w}{u},}
\tag{3.2}
\]

其中

\[
u:=1+\frac{H}{5^{M-1}}.
\]

但由真实第二 denominator defect

\[
b_2=10^{M-1}+2^{M-1}H
\]
可精确得到

\[
\boxed{u=10x.}
\tag{3.3}
\]

把 (3.2),(3.3) 代入 (3.1)，`c_Q,w` 完全消失：

\[
\boxed{
\mathfrak a_\Delta
=
\frac{1000s^2x^2k_h^3}{\sigma_\varepsilon^3}
2^{-(M+5\eta)/2-8}
5^{3M-d-\eta-3}.}
\tag{3.4}
\]

所以 Gaussian slot并不是 `Q_Delta` 外部的另一套尺度；它正好把 CRT main scale正规化成一个固定连续系数。

---

## 4. Gaussian-normalized CRT quotient

定义

\[
\boxed{
\mathcal Q_{\Delta,G}
:=
\frac{2^{(M+5\eta)/2+8}}
{5^{3M-d-\eta-3}k_h^3}
Q_\Delta.}
\tag{4.1}
\]

因为 `eta=2m-M`，`M+eta` 同偶奇，所以 `(M+5eta)/2` 为整数。

先忽略 floor，定义 real quotient

\[
Y_\Delta:=\frac{\Delta_+}{D^2-C^2}.
\]

由 (1.3),(3.4)：

\[
\boxed{
\frac{2^{(M+5\eta)/2+8}}
{5^{3M-d-\eta-3}k_h^3}
Y_\Delta
=
\frac{1000s^2x^2}{\sigma_\varepsilon^3}
\Psi_\Delta.}
\tag{4.2}
\]

因此所有 `(M,eta,d,c_Q,k_h)` 的绝对指数尺度都已经从右边消失；只剩 endpoint box 与 Gaussian side。

---

## 5. floor correction is uniformly tiny

记

\[
\epsilon_{\rm fl}
:=
\frac{2^{(M+5\eta)/2+8}}
{5^{3M-d-\eta-3}k_h^3}.
\tag{5.1}
\]

当前 reflection high-2 lattice位于 low-`m` cone，已有

\[
M\ge11,
\qquad
\eta\le\frac M{11},
\qquad
d<\frac{9M}{77},
\qquad k_h\ge1.
\tag{5.2}
\]

于是

\[
\frac{M+5\eta}{2}+8<M+8,
\]

并且

\[
3M-d-\eta-3>2M.
\]

因此

\[
0<\epsilon_{\rm fl}
<256\left(\frac2{25}\right)^M
<\frac1{100}
\qquad(M\ge11).
\tag{5.3}
\]

又 `Q_Delta=floor(Y_Delta)`，故

\[
\boxed{
\frac{1000s^2x^2}{\sigma_\varepsilon^3}\Psi_\Delta
-\frac1{100}
<\mathcal Q_{\Delta,G}
<
\frac{1000s^2x^2}{\sigma_\varepsilon^3}\Psi_\Delta.}
\tag{5.4}
\]

---

## 6. two Gaussian sides give disjoint fixed bands

### 6.1 minus side

使用 (1.1),(1.6),(2.3-)：

\[
\frac{1000s^2x^2}{\sigma_-^3}\Psi_\Delta
>
1000\left(\frac{2499}{250}\right)^2
\left(\frac1{10}\right)^2
\frac1{17}
\left(\frac{500}{1607}\right)^3
>\frac{44}{25}.
\]

上界为

\[
\frac{1000s^2x^2}{\sigma_-^3}\Psi_\Delta
<
1000(10)^2\left(\frac2{19}\right)^2
\frac{1001}{15000}
\left(\frac{125}{393}\right)^3
<\frac{12}{5}.
\]

结合 floor correction `<1/100`：

\[
\boxed{
\frac74
<\mathcal Q_{\Delta,G}
<\frac{12}{5}
\qquad(\varepsilon=-1).}
\tag{6.1}
\]

### 6.2 plus side

同理，由 (2.3+)：

\[
\frac{1000s^2x^2}{\sigma_+^3}\Psi_\Delta
>
1000\left(\frac{2499}{250}\right)^2
\left(\frac1{10}\right)^2
\frac1{17}
\left(\frac{125}{606}\right)^3
>\frac{51}{100},
\]

而

\[
\frac{1000s^2x^2}{\sigma_+^3}\Psi_\Delta
<
1000(10)^2\left(\frac2{19}\right)^2
\frac{1001}{15000}
\left(\frac{500}{2389}\right)^3
<\frac7{10}.
\]

所以

\[
\boxed{
\frac12
<\mathcal Q_{\Delta,G}
<\frac7{10}
\qquad(\varepsilon=+1).}
\tag{6.2}
\]

两个区间严格不交，并且被 `1` 完全分开。

---

## 7. CRT quotient canonically reads the Gaussian side

由 (6.1),(6.2)：

\[
\boxed{
\varepsilon=-1
\iff
\mathcal Q_{\Delta,G}>1,}
\tag{7.1-}
\]

\[
\boxed{
\varepsilon=+1
\iff
\mathcal Q_{\Delta,G}<1.}
\tag{7.1+}
\]

所以 additive CRT quotient 与 Gaussian allocation 不再只是“共享同一 `(eta,d,c_Q)` 参数”：`Q_Delta` 经过 canonical lattice normalization 后直接恢复 Gaussian side orientation。

---

## 8. integer sign carrier

令

\[
\boxed{
A_G:=\frac{M+5\eta}{2}+8,
\qquad
B_G:=3M-d-\eta-3.}
\tag{8.1}
\]

当前 lattice 中二者均为整数，且 `A_G>=1,B_G>=1`。定义纯整数

\[
\boxed{
\mathscr O_\Delta
:=2^{A_G}Q_\Delta-5^{B_G}k_h^3.}
\tag{8.2}
\]

由 (4.1)：

\[
\frac{\mathscr O_\Delta}{5^{B_G}k_h^3}
=\mathcal Q_{\Delta,G}-1.
\tag{8.3}
\]

因此 (7.1±) 等价于

\[
\boxed{
\varepsilon=-1
\iff
\mathscr O_\Delta>0,}
\tag{8.4-}
\]

\[
\boxed{
\varepsilon=+1
\iff
\mathscr O_\Delta<0.}
\tag{8.4+}
\]

特别地

\[
\boxed{\mathscr O_\Delta\ne0.}
\tag{8.5}
\]

因为 `k_h` 为正奇数而 `A_G>=1`，第一项为偶数、第二项为奇数，所以

\[
\boxed{\mathscr O_\Delta\equiv1\pmod2.}
\tag{8.6}
\]

并有 exact residue

\[
\boxed{
\mathscr O_\Delta
\equiv-5^{B_G}k_h^3
\pmod{2^{A_G}},}
\tag{8.7}
\]

\[
\boxed{
\mathscr O_\Delta
\equiv2^{A_G}Q_\Delta
\pmod{5^{B_G}}.}
\tag{8.8}
\]

所以 Gaussian side 已经被转换为一个 ordinary odd integer 的**符号问题**，同时该整数带有显式深 `2/5` residue。这比只保留实数 slot 更适合继续与 centered source-Hensel representatives `(z_E,chi_E)`、additive CRT residue以及 exact gap valuations联立。

---

## 9. revised frontier

粗 Gaussian slots此前在 `eta>=1` 确实有实区间交点，因此不能靠 `G=g/T` 本身统一排除。

本文给出的新对象

\[
\mathcal Q_{\Delta,G}
\]
把两侧分成

\[
\left(\frac12,\frac7{10}\right)
\quad\text{和}\quad
\left(\frac74,\frac{12}{5}\right),
\]
并进一步变成整数 carrier `O_Delta` 的正负号。

所以下一步最自然的是证明 additive CRT 的唯一 residue class、`v_2/v_5` exact gap phase，或 `(z_E,chi_E)` source-Hensel centered representative固定 `O_Delta` 的相反符号。如果能做到，就会直接排除对应 Gaussian side，而无需再做 coarse slot comparison。

A2 仍为 `待证`。

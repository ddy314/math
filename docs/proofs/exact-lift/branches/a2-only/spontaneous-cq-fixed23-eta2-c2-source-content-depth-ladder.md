# A2 fixed `23` `eta=2` `c=2` 的 source-content depth ladder

> **依赖：** `spontaneous-cq-fixed23-eta2-c2-blowup-nogo.md`、`spontaneous-cq-fixed23-eta2-c2-source-content-mod23.md`、`spontaneous-cq-fixed23-eta2-c2-source-window.md`。
>
> **严格状态：**唯一 `c=2` type `(d,c_Q,k_h,slot)=(1,1587,1,+)` 已有 local 三变量 blow-up no-go。本文把真实 global relation `q_2=3*2^(2lambda+1) q` 与 `rho=q5^lambda/c_u` 直接代入 high-2 equation，把第三个 correction coordinate从自由 `q_2` 改成真实 source content `c_u`。得到的 normalized `(K,rho,c_u)` Jacobian仍为 unit，因此对每个 genuine orientation存在唯一 finite Hensel source-content branch：common depth `>=2,>=3,>=4` 分别强迫 `c_u` 落在唯一的 `mod 23,23^2,23^3` residue。与真实 source window / prime support联立后得到严格高度阶梯
> \[
> d_{23}\ge2\Rightarrow\lambda\ge63,
> \qquad
> d_{23}\ge3\Rightarrow\lambda\ge96,
> \qquad
> d_{23}=4\Rightarrow\lambda\ge129.
> \]
> 在 `lambda=96`，若 depth 能达到 `3`，canonical orientation 必须是 `23^2|c_-` 且 `c_u=533221`。这些条件均为必要条件；residue 命中本身不保证真实 arithmetic state 达到相应深度。

---

## 1. unique type 与真实 `q_2` coordinate

固定

\[
p:=23,
\qquad
c_Q=3p^2=1587,
\]

\[
M=2\lambda,
\qquad
m=\lambda+1,
\qquad
T=10^m,
\qquad
N=10^M.
\tag{1.1}

定义

\[
\rho:=\frac{q5^\lambda}{c_u},
\qquad
q_2:=\frac Q{p^2}.
\]

由真实 denominator relation

\[
Q=2^{M+1}c_Qq
\]
得到 exact `23`-adic identity

\[
\boxed{
q_2=\chi_\lambda\rho c_u,
\qquad
\chi_\lambda:=3\cdot2^{2\lambda+1}5^{-\lambda}
\in\mathbf Z_{23}^\times.}
\tag{1.2}

这里 `5^{-lambda}` 在 `Z_23` 中读取；它是 unit。

因此 blow-up proof 中看似独立的 `q_2` correction，在真实 arithmetic orbit上由 `(rho,c_u)` 唯一给出。

---

## 2. high-2 equation 改写成 source-content equation

沿用

\[
B=p^2q_2-2N,
\qquad
A=\frac{K-9N}{10}.
\tag{2.1}

`spontaneous-cq-fixed23-eta2-c2-blowup-nogo.md` 已给 finite-order high-2 bridges：

### minus canonical orientation `p^2||c_-`

\[
15B^2\rho^2
-2BKT^2q_2
-2p^2AT^2q_2^2
\equiv0\pmod{p^4}.
\tag{2.2-}

### plus canonical orientation `p^2||c_+`

\[
15B^2\rho^2(\rho+2)
-2B\rho KT^2q_2
-2p^2AT^2q_2^2(\rho+2)
\equiv0\pmod{p^4}.
\tag{2.2+}

代入 (1.2)。因为 `rho` 在两个 genuine orientations 中均为 unit，minus 可除去一份 `rho`，plus 可除去 `rho^2`。得到 analytic source-content forms：

\[
\boxed{
\begin{aligned}
\mathscr H_-
={}&15B^2\rho
-2BKT^2\chi_\lambda c_u\\
&-2p^2AT^2\chi_\lambda^2\rho c_u^2
\equiv0\pmod{p^4},
\end{aligned}}
\tag{2.3-}

\[
\boxed{
\begin{aligned}
\mathscr H_+
={}&15B^2(\rho+2)
-2BKT^2\chi_\lambda c_u\\
&-2p^2AT^2\chi_\lambda^2c_u^2(\rho+2)
\equiv0\pmod{p^4}.
\end{aligned}}
\tag{2.3+}

其中现在

\[
B=p^2\chi_\lambda\rho c_u-2N.
\tag{2.4}

所以 high-2 constraint 的第三个真实变量已经是 `c_u`。

---

## 3. normalized global Jacobian 仍为 unit

写

\[
K=16+p\kappa,
\qquad
N^2=16+ph_N.
\]

prefix 与 additive 的第一 normalized equations 为

\[
\boxed{F_1=16h_N+22-9\kappa,}
\tag{3.1}

\[
\boxed{F_{2,+}=\rho(1+14\kappa)+11,}
\tag{3.2+}

\[
\boxed{F_{2,-}=\rho(1+14\kappa)-9-18\kappa.}
\tag{3.2-}

而 (2.3) 降模 `p`，使用

\[
N\equiv4,
\quad
T^2\equiv9,
\quad
K\equiv16,
\quad
B\equiv15
\pmod p,
\]
后，乘去一个固定 unit，可分别写成

\[
\boxed{F_{3,-}=\rho-16\chi_\lambda c_u,}
\tag{3.3-}

\[
\boxed{F_{3,+}=\rho+2-16\chi_\lambda c_u.}
\tag{3.3+}

因此在 correction variables

\[
(\kappa,\rho,c_u)
\]
上，Jacobian 的三个 transverse diagonal entries 是

\[
-9,
\qquad
1+14\kappa,
\qquad
-16\chi_\lambda.
\]

故

\[
\boxed{
\det J_{\rm src}
=144\chi_\lambda(1+14\kappa).}
\tag{3.4}

`chi_lambda` 永远是 unit；genuine second-layer root 已排除 `kappa=18`，所以

\[
\boxed{\det J_{\rm src}\in\mathbf F_{23}^\times.}
\tag{3.5}

这给出 finite Hensel uniqueness：在 common-depth cap `4` 内，每升一层都会唯一固定 `c_u` 的下一位 `23`-adic digit。

---

## 4. canonical source-content branch

对固定 `lambda` 与 orientation `sigma in {-,+}`，若 `kappa` 为 `11` 或 `18`，selected additive gate 已在第一层停止，因此不定义 deeper branch。

其余情形定义三个唯一 residues

\[
C_{1,\sigma}(\lambda)\pmod p,
\]

\[
C_{2,\sigma}(\lambda)\pmod{p^2},
\]

\[
C_{3,\sigma}(\lambda)\pmod{p^3}
\]
为 §3 的 finite Hensel branch 的前三个 source-content truncations。

逻辑方向为

\[
\boxed{
d_{23}\ge2
\Longrightarrow
c_u\equiv C_{1,\sigma}(\lambda)\pmod p,}
\tag{4.1}

\[
\boxed{
d_{23}\ge3
\Longrightarrow
c_u\equiv C_{2,\sigma}(\lambda)\pmod{p^2},}
\tag{4.2}

\[
\boxed{
d_{23}\ge4
\Longrightarrow
c_u\equiv C_{3,\sigma}(\lambda)\pmod{p^3}.}
\tag{4.3}

反向命题不在本文声称范围内：一个 residue 命中只说明这一 source-content gate没有排除相应深度；真实 `K,rho` 仍须来自完整 decimal reconstruction。

---

## 5. 首批 height residues

当前 height lattice 为

\[
\lambda\equiv8\pmod{11}.
\]

exact checker 对 (2.2)–(3.3) 做逐位提升，得到：

\[
\boxed{
\begin{array}{c|c|ccc|ccc}
\lambda&\kappa
&C_{1,-}&C_{2,-}&C_{3,-}
&C_{1,+}&C_{2,+}&C_{3,+}\\ \hline
52&2&11&425&8360&12&288&11926\\
63&15&15&84&2200&8&192&1779\\
74&5&22&367&3012&1&300&7706\\
85&18&\multicolumn{3}{c|}{d_{23}=1}&\multicolumn{3}{c}{d_{23}=1}\\
96&8&12&518&3163&11&471&5232\\
107&21&20&411&5701&3&486&4189\\
118&11&\multicolumn{3}{c|}{d_{23}=1}&\multicolumn{3}{c}{d_{23}=1}\\
129&1&13&335&7741&10&148&11257
\end{array}}
\tag{5.1}

其中

\[
0\le C_1<23,
\quad
0\le C_2<529,
\quad
0\le C_3<12167.
\]

`C_1` 行与 `spontaneous-cq-fixed23-eta2-c2-source-content-mod23.md` 完全一致；`C_2,C_3` 是本文新增的 higher-depth global source-content filters。

---

# I. depth `>=2` 的高度下界

## 6. `d_23>=2` 强迫 `lambda>=63`

source-window proof 已严格给

\[
\lambda\ge52.
\]

在 `lambda=52` 唯一 source content 为

\[
c_u=29.
\]
而

\[
29\equiv6\pmod{23},
\]
与 (5.1) 的

\[
C_{1,-}=11,
\qquad
C_{1,+}=12
\]
均不相同。因此

\[
\boxed{\lambda=52\Longrightarrow d_{23}=1.}
\tag{6.1}

所以

\[
\boxed{d_{23}\ge2\Longrightarrow\lambda\ge63.}
\tag{6.2}

该 bound 对当前 filters 是 sharp 的：`lambda=63` 的 source window留下 `c_u=337`，且

\[
337\equiv15=C_{1,-}\pmod{23}.
\]
因此 minus orientation 的 second-layer source-content gate在 `lambda=63` 不再排除。

---

# II. depth `>=3` 的高度下界

## 7. `lambda=63,74,85` 都不能达到 depth `3`

### `lambda=63`

唯一 source content 为

\[
c_u=337.
\]
plus orientation 已在 `mod23` 失败。minus orientation虽然满足

\[
337\equiv15\pmod{23},
\]
但

\[
337\not\equiv84\pmod{529}=C_{2,-}(63).
\]
故

\[
\boxed{\lambda=63\Longrightarrow d_{23}<3.}
\tag{7.1}

### `lambda=74`

source support只留下

\[
c_u\in\{3917,3929\}.
\]
二者在第一层已同时违反两种 orientation 的 `C_1` 条件，所以

\[
\boxed{\lambda=74\Longrightarrow d_{23}=1.}
\tag{7.2}

### `lambda=85`

此时

\[
\kappa=18,
\]
additive gate强迫

\[
\boxed{d_{23}=1.}
\tag{7.3}

因此任何 depth `>=3` state 必有

\[
\lambda\ge96.
\]

---

## 8. `lambda=96` 的 depth-3 source content 唯一

source real window为

\[
\boxed{530249\le c_u\le534049.}
\tag{8.1}

### minus orientation

`d_23>=3` 要求

\[
c_u\equiv518\pmod{529}.
\]
区间内只有七个 representatives：

\[
530576,531105,531634,532163,532692,533221,533750.
\]

source content必须为奇数，且每个素因子都为 `1 mod4`，并且 `5` 不整除。逐项检查后唯一 survivor 是

\[
\boxed{533221=13\cdot41017,}
\tag{8.2}

其中两素因子均为 `1 mod4`。

### plus orientation

`d_23>=3` 要求

\[
c_u\equiv471\pmod{529}.
\]
区间内 representatives 为

\[
530529,531058,531587,532116,532645,533174,533703.
\]

它们分别被 `3`、偶性、`3 mod4`、偶性、`5`、偶性、`3` 排除，没有合法 source content。

因此

\[
\boxed{
d_{23}\ge3
\Longrightarrow
\lambda\ge96.}
\tag{8.3}

并且等号情形被压成

\[
\boxed{
\lambda=96,
\quad23^2\mid c_-,
\quad c_u=533221.}
\tag{8.4}

这里仍只声明 depth-3 的必要 source state；(8.4) 不保证真实 reconstructed candidate 存在或真的达到 depth `3`。

---

# III. full saturation `d_23=4` 的高度下界

## 9. `lambda=96` 不可能达到 depth `4`

minus orientation 的 depth-4 residue为

\[
C_{3,-}(96)=3163\pmod{12167},
\]
plus 为

\[
C_{3,+}(96)=5232\pmod{12167}.
\]

但 source interval (8.1) 的长度只有 `3801<12167`，而 exact representative check显示两种 residue在该 interval中都没有整数代表。因此

\[
\boxed{\lambda=96\Longrightarrow d_{23}<4.}
\tag{9.1}

---

## 10. `lambda=107` 的全部 depth-4 representatives违反 source support

source interval为

\[
\boxed{6172910\le c_u\le6217159.}
\tag{10.1}

### minus orientation

要求

\[
c_u\equiv5701\pmod{12167}.
\]
区间内只有

\[
6174370,
6186537,
6198704,
6210871.
\]

前三个分别含偶/`5`、`3`/`7`、偶因子；最后一个满足

\[
6210871=59\cdot105269
\]
且 `59=3 mod4`。所以全部不合法。

### plus orientation

要求

\[
c_u\equiv4189\pmod{12167}.
\]
区间内只有

\[
6185025,
6197192,
6209359.
\]

前两个分别含 `3,5` 与偶因子；最后一个

\[
6209359=13\cdot67\cdot7129
\]
含 `67=3 mod4`。同样全部不合法。

故

\[
\boxed{\lambda=107\Longrightarrow d_{23}<4.}
\tag{10.2}

---

## 11. `lambda=118` 已在第一层停止

此时

\[
\kappa=11,
\]
所以

\[
\boxed{d_{23}=1.}
\tag{11.1}

结合 §§9–11 与此前更低高度结果：

\[
\boxed{
d_{23}\ge4
\Longrightarrow
\lambda\ge129.}
\tag{11.2}

因为 cap 为 `4`，也可写成

\[
\boxed{d_{23}=4\Longrightarrow\lambda\ge129.}
\tag{11.3}

---

## 12. `lambda=129` 说明该 filter 到此达到边界

`lambda=129` 的 depth-4 residues为

\[
C_{3,-}=7741,
\qquad
C_{3,+}=11257
\pmod{12167}.
\]

source interval已经包含满足这些 congruences且满足 source prime support 的整数。例如 minus orientation 有

\[
\boxed{
836610661
=617\cdot1355933,}
\tag{12.1}

其中 `617` 与 `1355933` 都是 `1 mod4` primes；plus orientation有

\[
\boxed{836760181,}
\tag{12.2}

它本身为 `1 mod4` prime。

所以 source-window + `23^3` residue + prime-support 这套 filters 无法把 saturation height继续统一推到 `lambda>129`。更高 closure 必须使用 source divisor `theta`、full `a_3` CRT representative 或 deterministic reconstruction。

---

## 13. 更新后的 fixed-23 depth ledger

当前唯一 `c=2` type 的 source-content hierarchy为

\[
\boxed{
\begin{array}{c|c}
\text{desired common depth}&\text{necessary height/source consequence}\\ \hline
\ge2&\lambda\ge63\\
\ge3&\lambda\ge96;\ \lambda=96\Rightarrow(c_-,c_u=533221)\\
4&\lambda\ge129
\end{array}}
\tag{13.1}

它把 `spontaneous-cq-fixed23-eta2-c2-source-content-mod23.md` 的 single-digit filter扩展到了完整 square cap。

后续不应继续把 `q_2` 当作独立 local correction来枚举；对真实 arithmetic orbit，最规范的 `23`-adic source coordinate是本文的唯一 `c_u` finite-Hensel branch。